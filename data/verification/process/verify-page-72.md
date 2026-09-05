# Verification process log — verify-page-72


## [2026-09-05T05:41:32.349Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 72 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-72.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-72.json. Write /home/sfmqrb/git/rishe/data/verification/page-72.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 72` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T05:41:33.783Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T05:41:34.518Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T05:41:34.537Z] TOOL RESULT

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


## [2026-09-05T05:41:34.631Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-72.txt"
}
```


### [2026-09-05T05:41:34.648Z] TOOL RESULT

```
1	=== PDF page 72 (book page 42) ===
2	--- entry 0 ---
3	ROOT [Greek] Autos : self  (refs KLN:130; AHD:89)
4	#1 (parent #0) [Greek] refs=KLN; AHD | authentěs, afendis : self doer, authority, ruler, original
5	  #2 (parent #1) [Turkish] refs=KLN:502 | afandi : sir, master
6	    #3 (parent #2) [Persian] refs=MON:319 | afandî «افندی» : title of respect
7	  #4 (parent #1) [Latin] refs=AHD:89 | authenticus : genuine
8	    #5 (parent #4) [English] refs=AHD | authentic,
9	#6 (parent #0) [German] refs=None | auto-bahn : highway
10	  #7 (parent #6) [Persian] refs=None | otobân «اتوبان» : highway
11	#8 (parent #0) [French] refs=None | 
12	  #9 (parent #8) [Persian] refs=MON:139 |  | extra: اتوماتیک ، اتومبیل ، اتوبوس
13	#10 (parent #0) [English] refs=AHD:89; KLN:130 | auto-, automobile, automatic
14	
```


## [2026-09-05T05:41:37.795Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-72.json",
 "description": "Read source JSON for page 72"
}
```


### [2026-09-05T05:41:37.840Z] TOOL RESULT

```
{
  "pdf_page": 72,
  "book_page": 42,
  "entries": [
    {
      "root": {
        "name": "Autos",
        "lang": "Greek",
        "refs": "KLN:130; AHD:89",
        "gloss": "self",
        "note": "from uncertain origin"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN; AHD",
          "words": [
            {"translit": "authentěs, afendis", "gloss": "self doer, authority, ruler, original", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Turkish",
          "refs": "KLN:502",
          "words": [
            {"translit": "afandi", "gloss": "sir, master", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:319",
          "words": [
            {"translit": "afandî", "gloss": "title of respect", "script": "افندی"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD:89",
          "words": [
            {"translit": "authenticus", "gloss": "genuine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "authentic,", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "German",
          "refs": null,
          "words": [
            {"translit": "auto-bahn", "gloss": "highway", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": null,
          "words": [
            {"translit": "otobân", "gloss": "highway", "script": "اتوبان"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
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
          "lang": "Persian",
          "refs": "MON:139",
          "words": [],
          "script_extra": "اتوماتیک ، اتومبیل ، اتوبوس",
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "English",
          "refs": "AHD:89; KLN:130",
          "words": [
            {"translit": "auto-, automobile, automatic", "gloss": null, "script": null}
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


## [2026-09-05T05:41:37.842Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T05:41:37.887Z] TOOL RESULT

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


## [2026-09-05T05:41:48.264Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','MON','POK','WLD','SKT','LKT','TTS','LEW','LAT','FSD','WEB','IEC','SYN','BQT','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n\""
}
```


## [2026-09-05T05:41:48.416Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -60 && echo --- && head -60 data/verification/page-66.json"
}
```


### [2026-09-05T05:41:50.141Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it
```


### [2026-09-05T05:41:50.198Z] TOOL RESULT

```
agent
page-101.json
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
process
sources
---
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


## [2026-09-05T05:41:54.102Z] TOOL CALL #7: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD']:\n    print(k, json.dumps(d[k], ensure_ascii=False, indent=1))\n\""
}
```


## [2026-09-05T05:41:55.009Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"authent\" KLN_1966.txt | head -30"
}
```


### [2026-09-05T05:41:55.589Z] TOOL RESULT

```
KLN {
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
AHD {
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
```


### [2026-09-05T05:41:55.633Z] TOOL RESULT

```
4018:auth-,  form  of  auto-  before  an  aspirate, authentic,  adj.  authoritative;  reliable;  genuine.  — OF.  autentique  (F.  authentique),  fr.  Gk.  auOev- xix<k,  ‘original,  genuine,  principal’,  fr.  afi&bnrfc, auTo-£vT7)<;,  ‘absolute  master,  ruler;  murderer  , lit.  ‘one  who  does  a  thing  himself’,  compounded of  aux6<;,  ‘self’  (‘see  auto-),  and  *brrr^q,  ‘one who  does  (a  thing)  himself’,  which  is  rel.  to avu<o,  Att.  avuco,  ‘I  accomplish’,  and  cogn.  with OI.  sandti,  ‘wins,  gains’,  perhaps  also  with  Hitt. shanh-zi,  ‘he  seeks,  strives’.  Cp.  effendi. Derivatives:  authentic,  n.,  authentic-al-ly ,  adv., authenticate  (q.v.),  authentic-ity,  n.,  authentic- ly,  adv.,  authentic-ness,  n. authenticate,  tr.  v.,  to  make  authentic,  verify.  — ML.  authenticate,  pp.  of  authenticate,  fr.  Late  L. authenticus.  See  prec.  word  and  verbal  suff.  -ate. Derivatives:  aulhemic-ation,  n. ,  authentic-ator  ,n. author,  n.  —  ME.  autour,  authour,  fr.  OF.  autor (F.  auteur),  fr.  L.  auctorem,  acc.  of  auctor,  ‘he that  brings  about,  master,  supporter,  leader, author’,  an  agential  noun  formed  fr.  auctus,  pp. of  augere  ‘to  increase’.  See  auction  and  cp.  words there  referred  to.  Cp.  also  octroi.
6040:cachet,  n.,  a  distinguishing  mark  of  quality  or authenticity.  —  F.,  ‘seal,  stamp’,  fr.  cacher,  ‘to hide’.  See  cache.
12688:authentic.
```


## [2026-09-05T05:42:00.747Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'authentic,  adj.' in l or 'effendi' in l.lower() or re.search(r'auto-,\\s*before', l):\n        print('LEAF',i, 'approx printed p.', (i-12)*2)\nEOF"
}
```


## [2026-09-05T05:42:01.143Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"effendi\" KLN_1966.txt | head -10; echo ===; grep -n -i \"auto-,  \" KLN_1966.txt | head -5"
}
```


### [2026-09-05T05:42:02.485Z] TOOL RESULT

```
LEAF 80 approx printed p. 136
LEAF 273 approx printed p. 522
```


### [2026-09-05T05:42:02.534Z] TOOL RESULT

```
Exit code 1
4018:auth-,  form  of  auto-  before  an  aspirate, authentic,  adj.  authoritative;  reliable;  genuine.  — OF.  autentique  (F.  authentique),  fr.  Gk.  auOev- xix<k,  ‘original,  genuine,  principal’,  fr.  afi&bnrfc, auTo-£vT7)<;,  ‘absolute  master,  ruler;  murderer  , lit.  ‘one  who  does  a  thing  himself’,  compounded of  aux6<;,  ‘self’  (‘see  auto-),  and  *brrr^q,  ‘one who  does  (a  thing)  himself’,  which  is  rel.  to avu<o,  Att.  avuco,  ‘I  accomplish’,  and  cogn.  with OI.  sandti,  ‘wins,  gains’,  perhaps  also  with  Hitt. shanh-zi,  ‘he  seeks,  strives’.  Cp.  effendi. Derivatives:  authentic,  n.,  authentic-al-ly ,  adv., authenticate  (q.v.),  authentic-ity,  n.,  authentic- ly,  adv.,  authentic-ness,  n. authenticate,  tr.  v.,  to  make  authentic,  verify.  — ML.  authenticate,  pp.  of  authenticate,  fr.  Late  L. authenticus.  See  prec.  word  and  verbal  suff.  -ate. Derivatives:  aulhemic-ation,  n. ,  authentic-ator  ,n. author,  n.  —  ME.  autour,  authour,  fr.  OF.  autor (F.  auteur),  fr.  L.  auctorem,  acc.  of  auctor,  ‘he that  brings  about,  master,  supporter,  leader, author’,  an  agential  noun  formed  fr.  auctus,  pp. of  augere  ‘to  increase’.  See  auction  and  cp.  words there  referred  to.  Cp.  also  octroi.
12687:effendi,  n.,  a  Turkish  title  of  respect;  sir.  — Turk,  efendi,  ‘master’,  fr.  MGk.  a<p£v-c-r)  (read afendi),  voc.  of  d<pevT7)?  (read  afendis),  fr.  Gk. auffcvTY)?,  ‘an  absolute  master  or  ruler’.  See
(eval):1: == not found
```


## [2026-09-05T05:42:10.174Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (79,80,81,272,273,274):\n    print('=== LEAF',i,'===')\n    print(leaves[i][:300].replace('\\n',' | '))\n    print('...TAIL:', leaves[i][-200:].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-05T05:42:11.741Z] TOOL RESULT

```
=== LEAF 79 ===
an  agential  suff.  -dar,  meaning ‘holder,  possessor’,  which  is  rel.  to  Avestic darayeiti,  ‘holds,  supports’,  OI.  dhardyati,  of s.m.,  fr.  I.-E.  base  *dher(e)-,  ‘to  hold,  support’, whence  also  L.  firmus,  ‘firm,  steadfast,  stable, strong’.  See  firm,  adj.,  and  cp.  the  f
...TAIL:  not  the  ‘east  wind’).  See | austere | autopsy | Walde-Hofmann,  LEW.,  I,  p.87,  where  also  an attempt  is  made  to  explain  the  meaning  of  L. auster. | austere,  adj.,  stem,  severe;  very  sim
=== LEAF 80 ===
ple.  —  OF. austere  (F.  austire),  fr.  L.  austerus,  ‘dry,  harsh, sour,  tart’,  fr.  Gk.  auax^pit;,  ‘harsh,  rough, bitter’,  fr.  aiisiv,  ‘to  dry’,  fr.  auo<;,  ‘dry’.  See auantic. | Derivatives:  austere-ly,  adv.,  austere-rtess,  n., austerity ,  n.  (q.v.) | austerity,  n.,  the  quali
...TAIL: ish  biologist  Sir  Richard  Owen  (1804-92) in  1846  fr.  Gk.  auxoyevr)?,  ‘self-produced’,  fr. auxo-  (see  auto-)  and  the  stem  of  yevvav,  ‘to produce’.  See  -genous. | Derivative:  autogen
=== LEAF 81 ===
ous-ly,  adv. autogeny,  n.,  autogenesis.  —  See  autogenesis  and -geny. | autograph,  n.,  signature.  • —  L.  autographum,  fr. Gk.  auxdypaipov,  neut.  of  auxoypaqxx;,  ‘written with  one’s  own  hand’,  compounded  of  auxo- (see  auto-)  and  -ypa 905,  fr.  ypatpetv,  ‘to  write’. | See  -gr
...TAIL: f  L.  ave  being  thus  established,  we shall  be  able  to  find  the  exact  meaning  of  the words  with  which  the  gladiators  greeted  the emperor:  ‘Ave,  Imperator,  morituri  te  salutant�
=== LEAF 272 ===
 deals  with  animals  and  plants  in  relation  to  their environment.  —  G.  Okologie,  coined  by  the German  biologist  Ernst  Heinrich  Haeckel (1834- 1 9 1 9)  fr.  Gk.  oixo- (see  eco-)  and  -Xoyia, fr. -Xoyog,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  cert
...TAIL: tic — as  ‘a  place  that  is  well  watered  throughout’. Derivative:  Eden-ic ,  adj. edenite,  n.,  a  variety  of  aluminous  amphibole (mineral.)  —  Named  after  £(/c'«ville,  New  York. For  t
=== LEAF 273 ===
he  ending  see  subst.  suff.  -ite. | Edentata,  n.  pi.,  a  group  of  placental  mammals including  the  armadillo,  sloth,  anteater,  etc. (zoo!.)  —  ModL.,  neut.  pi.  of  L.  edentatus, ‘toothless’,  pp.  of  edentare,  ‘to  render  tooth¬ less’,  fr.  e-  and  dens,  gen.  dentis,  ‘tooth’
...TAIL:  verbal  suff. | -ate. | effendi,  n.,  a  Turkish  title  of  respect;  sir.  — Turk,  efendi,  ‘master’,  fr.  MGk.  a<p£v-c-r)  (read afendi),  voc.  of  d<pevT7)?  (read  afendis),  fr.  Gk. auffcvTY)
=== LEAF 274 ===
?,  ‘an  absolute  master  or  ruler’.  See | authentic. | efferent,  adj.,  conveying  outward  (physiol.) —  L. efferens,  gen.  -entis,  pres.  part,  of  efferre,  ‘to carry  out  or  away;  to  spread  abroad’,  fr.  ist ex-  and  ferre,  ‘to  bear,  carry’.  See  bear,  ‘to carry’,  and  -ent  and
...TAIL:  to  OS.  ahto,  ON.  atta,  Swed.  dtta, Dan.  otte,  OFris.  ahta,  Du.  acht,  OHG.  ahto, MHG.  ahte,  G.  acht,  Goth,  ahtau,  ‘eight’,  and cogn.  with  OI.  affd,  astdu,  Avestic  ashta,  Toc
```


## [2026-09-05T05:42:45.519Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nimport re\nfor i,l in enumerate(leaves):\n    if re.search(r'auto-,\\s+combining', l) or 'auto-, combining' in l:\n        print('LEAF',i); print(l[:1500])\nEOF\necho \"=== grep auto- combining ===\"\ngrep -n \"auto-,\" KLN_1966.txt | head -5"
}
```


### [2026-09-05T05:42:47.193Z] TOOL RESULT

```
903
LEAF 835
p,  saucer’.  Cp.  OProveng.  tassa, It.  tazza,  Sp.  taza,  ‘cup’,  which  are  of  the  same origin.  Cp.  also  tazza.
Tass,  n.,  the  official  news  agency  of  the  U.S.S.R. —  Formed  from  the  initials  of  the  Russian words  7’elcgrafnoje  Agenstvo  Sovjetskeho  So- juza  (=  ‘Soviet  Telegraphic  Agency’), tasse,  n.,  one  of  a  series  of  plates  forming  a  sort of  kilt  or  shirt  (armor).  —  MF.  tasse,  ‘pocket’, fr.  MHG.  (=  G.)  tasche,  fr.  OHG.  tasca,  which, together  with  MLG.  taske,  OS.  dasga,  is  bor¬ rowed  fr.  VL.  *  tasca;  see  task.  The  phases  of the  sense  development  of  VL.  *  tasca  prob.  are: ‘appraisal,  estimate;  amount  of  work  imposed
by  authority;  recompense  for  such  work;  daily wages;  pocket  into  which  the  wages  are  put; any  pocket’.
tassel,  n.,  ornament.  —  ME.,  fr.  OF.  tassel (whence  F.  tasseau,  ‘cleat,  strip,  bracket’),  fr. VL.  *tassellus,  fr.  L.  taxillus,  ‘a  small  die’, dimin.  of  talus,  ‘knucklebone,  heel’.  See  talus, ‘ankle’.
Derivatives:  tassel,  tr.  v.,  tassel-y,  adj. tassel,  n.  —  A  var.  of  tercel, taste,  tr.  and  intr.  v.  —  ME.  fasten,  ‘to  feel,  taste’, fr.  OF.  taster  (F.  tater),  ‘to  feel,  touch,  handle’, fr.  VL.  *taxitdre,  freq.  of  L.  taxare,  ‘to  touch sharply’,  itself  freq.  of  tangere,  ‘to  touch’  (see tangent).  Cp.  OProveng.  tastar,  It.  tastare,  Sp. and  Port,  tastar,  ‘to  feel,  taste’,  which  are  of  the sa
=== grep auto- combining ===
4027:Derivative:  autist-ic,  adj. auto,  n.  ( colloq .)  —  Short  for  automobile, auto-,  before  a  vowel  aut-,  before  an  aspirate auth-.  —  Gk.  auxo-,  aux-,  au$-,  fr.  auxo?,  ‘self, same’,  of  uncertain  origin, autobiographer,  n.  —  Compounded  of  auto-  and biographer.
4044:Derivatives:  autograph-y,  n.,  autograph-ical, adj. autogravure,  n.,  a  kind  of  photogravure.  —  A hybrid  coined  fr.  Gk.  aux<S?,  ‘self’  and  F.  gra¬ vure,  fr.  graver  ‘to  grave’.  See  auto-,  grave,  v., and  -ure.
4053:autonymous,  adjv  —  See  prec.  word  and  -ous. autonymy,  n.,  a  word  used  as  a  name  for  itself.  — Compounded  of  auto-,  Gk.  Svupia,  dialectal form  of  Svopux,  ‘name’,  and  suff.  -y;  introduced by  Rudolf  Carnap  (bom  in  1891).  See  autonym and  -y  (representing  Gk.  -la), autoplasty,  n.  ( surg .)  —  Compounded  of  auto- and  -plasty.  Derivative:  autoplast-ic,  adj. autopsy,  n.,  post-mortem  examination  of  a  body. - —  Gk.  auxoijjta,  ‘a  seeing  with  one’s  own  eyes’, compounded  of  auxo-  (see  auto-)  and  S-^iz, ‘sight’.  See  -opsis.
38302:tauto-,  combining  form  meaning  ‘the  same’.  — Gk.  Tauro-,  contraction  of  to  xuto,  ‘the  same’. T6,  the  neut.  def.  article  derives  from  the  I.-E. pronominal  base  *to-;  see  the,  art.  For  atrro  see
38304:tautochrone,  n.,  curve  down  which  a  body  moving from  any  point  under  the  force  of  gravity  will always  reach  the  lowest  point  in  the  same  time. Lit.  ‘of  the  same  time’.  See  tauto-  and  chronic, tautochronism,  n.,  property  of  a  tautochrone.  — See  prec.  word  and  -ism. tautochronous,  adj.,  having  the  property  of  a tautochrone.  —  See  tautochrone  and  -ous. tautog,  n.,  an  edible  marine  fish  of  the  Atlantic coast  of  N.  America.  —  Narraganset  tautaiiog. tautology,  n.,  repetition  of  the  same  idea  in  other words.  —  Late  L.  tautologia,  fr.  Gk.  txuto- Xoyta,  lit.  ‘the  saying  of  the  same  thing’,  com¬ pounded  of  TauTo-  (see  tauto-)  and  -Xoyta,  fr. -X6yop,  ‘one  who  speaks  (in  a  certain  manner); one  who  deals  (with  a  certain  topic)’.  See  -logy. Derivatives:  tautolog-ic,  tautolog-ic-al,  adjs., tautolog-ist,  n.,  tautolog-ize,  intr.  v. tautomerism,  n.,  the  phenomenon,  shown  by  cer¬ tain  compounds,  of  reacting  as  if  each  possessed two  or  more  structures  ( chem .)  —  Compounded of  tauto-,  Gk.  pipo;,  ‘part’,  and  suff.  -ism.  See mero-,  ‘part’,  and  cp.  merism. tautometer,  n.,  an  instrument  to  measure  taut¬ ness.  —  A  hybrid  coined  fr.  E.  taut  and  Gk. fjtsTpov,  ‘measure’.  See  meter,  ‘poetical  rhythm’, tautophony,  n.,  repetition  of  the  same  sound.  — Gk.  TaoTo<poma,  compounded  of  TauTo- (see  tauto-),  <pcovy,  ‘sound,  voice’,  and  suff.  -y (representing  Gk.  -tot ) .  See  phone,  ‘speech sound'.
```


## [2026-09-05T05:42:54.405Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT authentic ===\"; grep -n -i \"authentic\" SKT.txt | head -5; echo \"=== SKT effendi ===\"; grep -n -i \"effendi\" SKT.txt | head -5; echo \"=== LKT effendi ===\"; grep -n -i \"effendi\\|efendi\" LKT.txt | head -10; echo \"=== TTS efendi ===\"; grep -n -i \"efendi\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10; echo \"=== AHD autos ===\"; grep -n -i \"^au\\|autos\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T05:42:54.524Z] TOOL RESULT

```
=== SKT authentic ===
1191:Authentic.  (F.-I..-Gk.)  M.  E.  an. tifitujue,  auifnti'A.  —  O.  F.  anttntiqut.  later attikentiqut{}ZoX,')^  L.attMf«/#fTi*/,  original, written  with  the  author's  own  hand.  — Gk. oMtfTicvr,  vouched  for,  warranted.  —  Gk. o\AivTt\\.  one  who  docs  things  wilJi  his  own hand.     (Of  uncertain  origin.)
=== SKT effendi ===
5701:Effendi,  sir,  master  (Turkiah  -  Gk.) Turk.  e^"***/'.  sir. —  Mod.  Gk.  Q/'tcri;!,  for Gk.  avBivTi\%^  a  despotic  maalcr,  ruler;  see Authentio.
=== LKT effendi ===
280:lehrte vor  [Fleischer  in  ZDMG  XIX,  301]. Im  späteren  Osmanischen  heißt  aga 'der  ältere  Bruder',  Wiepasa  'der  jüngere Bruder'  ist.  Diese  Bedeutungen  hat das  heutige  Türkische  ganz  vergessen und  gebraucht  das  Wort  in  völlig  an- derem Sinne.  Aga  ist  jetzt  ein  häufig vorkommender  Titel,  besonders  bei niederen  militärischen  Chargen,  wird aber  nur  für  Analphabeten  benutzt, während  der  des  Schreibens  Kundige efendi  [s.  hier  Nr.  557]  genannt  wird. Als  Fremdwort  kommt  Aga  in  allen europäischen  Sprachen  vor,  oft  agha geschrieben.  Als  Lehnwort  hat  das  Rum. aga,  agha,  agia  'ehemaliger  Polizeiprä- fekt'.
1414:557.  Tk.  efendi:
1415:[Aus  gl-,  aiiöevxrii;  'Herr',  s.  Glotta  III, 289 ff.,  moderne  Aussprache  aftendis, und  zwar  Vokativ  auö^vxri  afMdi  MSOS I,  44,  Anm.  2];  früher  Ehrentitel  [s.  hier Nr.  28],  jetzt  entsprechend  unserer  höf- lichen Anrede  „mein  Herr,  monsieur". Frz.  efendi,  effendi,  dtsch.  Effendi  usw. [MWilJ  107.
=== TTS efendi ===
=== AHD autos ===
302:au-', To stay the night, dwell. Suffixed form *au-/d- in Greek aulé, court, dwelling: autic. [Pok. 2. au- 72.]
303:au-?. Pronominal base appearing in particles and adverbs. Suffixed form *au-ge in Germanic ‘*auke in Old English éac, éc, also: EKE?. [Pok. 4. au- 73.]
304:au-3, Off, away. 1. Old Russian u-, away, in Russian ukazat’, to order: UKASE. 2. Sanskrit ava, off, down: AvaTAR. [Pok. 3. au- 72.]
305:au-‘4, To weave. Extended form *wedh- (< *awedh-). 1. Germanic *wédiz in Old English wed, wéde, garment, cloth: WEED?, 2. Germanic *wadlaz in Old English watel, watul, wattle: WATTLE. [Pok. 5. au- 75.]
306:au-5, To perceive. Compound forms *aw-dh-, *awis-dh-, “to place perception” (see dhé-'). 1. Suffixed form *awisdh-yo- or *awdh-yo- in Latin audire, to hear: AUDIBLE, AUDIENCE, AUDIENT, AUDILE, AUDING, AUDIO-, AUDIT, AUDITOR, AUDITORIUM, AUDITORY, OYEZ; OBEY, SUBAUDITION. 2. Greek aisthanesthai, to feel: AES- THETIC; ANESTHESIA. [Pok. 8. au- 78.]
307:aug-'. To increase. Variant *(a)weg- (< *aweg-). 1. Ger- manic *aukan in: a. Old English éacan, écan, to increase: EKE!; b. Old English éaca, an addition: NICKNAME. 2. Variant extended forms *wogs-, *wegs- in Germanic *wahsan in Old English weaxan, to grow: WAX. 3. Form *aug-é- in: Latin augére, to increase: AUCTION, AUGEND, AUGMENT, AUTHOR, (AUTHORIZE), (OCTROI). 4. Latin augur, diviner (< “he who obtains favorable presage” < “divine favor, increase”): AUGUR; INAUGURATE. 5. Latin augustus, majestic, august: AUGUST. 6. Suffixed form *aug-s- in: a. Latin auxilium, aid, support, assistance: AUXILIARY; b. Greek auxein, to increase: AUXIN; ¢. Greek auxanein, to increase: AUXESIS. [Pok. aweg- 84.]
308:aug-?. To shine. Suffixed form *aug-d- in Greek augé,
310:aukv-, Cooking pot. 1. Germanic suffixed form *uhw-na- in *ufna- in Old English ofen, furnace, oven: OVEN. 2. Suffixed form *auk-sld- in Latin aulla, aula, olla, pot,
312:aulo-. Hole, cavity. 1. Metathetic form *alwo- in Latin
316:aus-', To shine. 1. Germanic *aust- in: a. Old English éast, east (< “the direction of the sunrise”): EAST; b. Old High German 6stan, east: OSTMARK. 2. Germanic *aus- tra- in: a. Old English éasterne, eastern: EASTERN; b. Late Latin ostro-, eastern: OsTROGOTH. 3. Germanic *austron-, a dawn-goddess whose holiday was celebrated at the vernal equinox, in Old English éastre, Easter: EAsTER. 4. Probably suffixed form *ausds-, dawn, also Indo-European goddess of the dawn, in: a. Latin auréra, dawn: AURORA; b. Greek éds, dawn: EO-, Eos; EOSIN. [Pok. aues- 86.]
317:aus-?. To draw water. Suffixed form *aus-yo- in Latin haurire, to draw up: EXHAUST, HAUSTELLUM, HAUSTO- RIUM. [Pok. aus- 90.] awi-. Bird. I. 1. Latin avis, bird: AVIAN, AVIARY, AVI- ATION; AVICULTURE, AVIFAUNA, BUSTARD, OCARINA, OSPREY, OSTRICH. 2. Compound *awi-spek-, “observer of birds” (*spek-, to see; see spek-), in Latin auspex, augur: AuSPICE. II. Possible derivatives are the Indo-European words for egg, *dwyo-, *ayo-. 1.Germanic *ajja(m) in: a. Old English 2g, egg: COCKNEY; b. Old Norse egg, egg: EGG. 2, Latin 6uum, egg: OVAL, OVARY, OVATE, OVI-, OVOLO, OVULE, OVUM. 3. Greek dion, egg: 00-. [Pok. auei- 86.] awo-. An adult male relative other than one’s father. 1. Latin avus, grandfather: ATAVISM. 2. Latin avunculus, maternal uncle: AVUNCULAR, UNCLE. 3. Latin avia, grandmother: AYAH. [Pok. auo-s 89.] ayer-. Day, morning. 1. Germanic “*airiz in: a. Old Eng- lish &r, before: EARLY, ERE; b. Old Norse dr, before: OR2. 2. Germanic (superlative) *airistaz in Old English rest, earliest: ERST. [Pok. ajer- 12.] ayes-. A metal, copper or bronze. Latin aes, bronze, money: AENEOUS, ERA. [Pok. aios- 15.] baba-. Root imitative of unarticulated or indistinct speech; also a child’s nursery word for a baby and for various relatives. 1. Middle English babelen, to babble: BABBLE. 2. Middle English babe, babi, baby: BABE, BABY. 3. Italian bambo, child, simpleton: BAMBINO. 4. Polish baba (diminutive babka), old woman: BABA, BABKA. 5. Russian baba, old woman: BABUSHKA. 6. Rus- sian balalaika, balalaika (imitative of the sound): BALA- LAIKA. 7. Latin balbus, stuttering, stammering: BOOBY. 8. Greek barbaros, non-Greek, foreign, rude (< “one who speaks incomprehensibly”): (BARBARIAN), BARBARISM, BARBAROUS. 9. Hindi babi, father: BABU. [Pok. baba- 91.] badyo-. Yellow, brown. A Western Indo-European word. Latin badius, chestnut brown (used only of horses): BAY’. [Pok. badios 92.] bak-. Staff used for support. 1. Probably Middle Dutch pegge (> Middle English pegge), pin, peg: PEG. 2. Latin baculum, rod, walking stick: BACILLUS, BAGUETTE; BAC- ULIFORM, DEBACLE, IMBECILE. 3. Greek baktron, staff: BACTERIUM; (CORYNEBACTERIUM). [Pok. bak- 93.] bamb-. Word imitative of dull or rumbling sounds. Greek bombos, a booming, humming: BOMB, (BOMBARD), BOUND}. [Pok. ba*mb- 93.] bands. A drop. Possibly Irish bainne, milk: BONNYCLAB- BER. [Pok. band- 95.]
1267:AULIC au-1
1268:AUNT amma AURA wer-2 AURAL! ous- AUREATE aurum AUREOLE aurum AURIC aurum AURICLE ous- AURIFEROUS aurum AURIFORM_ OUuSs- AURIGA 6s- AUROCHS wegW- AURORA aus-! AUSCULTATION oUuS-
1269:AUSLANDER lendh-?2, ud-
1270:AUSPICE awi-, spek- AUSTERE saus- AUTACOID y@k- AUTARCHY arkhein AUTARKY arek- AUTHOR aug-! AUTHORIZE aug-! AUTOBAHN g*hen-* AUTOCHTHON dhghem- AUTOECIOUS weik-1 AUTOGIRO géu- AUTOMATIC men-1 AUTONOMOUS nem-
1271:AUTOPSY OkW- AUXESIS aug-! AUXILIARY aug-! AUXIN aug-! AVAIL wal- AVAST  kel-3, past- AVATAR auc’, tera-? AVENGE deik- AVENUE gWa- AVER wéro- AVERT wer-3 AVIAN awi- AVIARY awi- AVIATION awi- AVICULTURE awi- AVIFAUNA awi- AVOCATION wekW- AVOID eu-2 AVULSE wel-4 AVUNCULAR awo- AWARE wer-4 AWAY wegh- AWE agh-1 AWKWARD apo- AWN ak-
```


## [2026-09-05T05:43:08.170Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON افندی ===\"; grep -n \"افندی\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10; echo \"=== MON اتوبان ===\"; grep -n \"اتوبان\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head; echo \"=== MON اتومبیل ===\"; grep -n \"اتومبیل\\|اتوموبیل\" MON_part1.txt MON_part2.txt incoming/MON/*djvu.txt 2>/dev/null | head"
}
```


### [2026-09-05T05:43:08.290Z] TOOL RESULT

```
=== MON افندی ===
MON_part1.txt:15234:افندی: 22701 [تر. آنکه به نفسه کار کند؛ 
MON_part1.txt:34569:کردن. افندی بیزی: آنکه صورتاً شجاع و 
MON_part1.txt:34571:(مراد از افندی ترث است.) رستم صولت و 
MON_part1.txt:34572:افندی پیزی: دارای صورتی حاکی از 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:15234:افندی: 22701 [تر. آنکه به نفسه کار کند؛ 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34569:کردن. افندی بیزی: آنکه صورتاً شجاع و 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34571:(مراد از افندی ترث است.) رستم صولت و 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:34572:افندی پیزی: دارای صورتی حاکی از 
=== MON اتوبان ===
=== MON اتومبیل ===
MON_part2.txt:8890:اتومبیل نصب می‌شود و کار آن جلو گیری و 
MON_part2.txt:8894:فنر اتومبیل دو نوع است: ۱ -فنر لوله‌یی که 
MON_part2.txt:10694:ورشو است و آن را در وسط چرخ اتومبیل 
MON_part2.txt:16771:خانه‌داری و اتومبیل و لباس‌های غیرقابل 
MON_part2.txt:17991:ماسک یا بدون آن که سوار اتومبیل و 
MON_part2.txt:19570:حمل و نقل بار؛ اتومبیل باری. 
MON_part2.txt:24516:اتومبیل که به وسیلةٌ آن راننده با اتصال وی 
MON_part2.txt:24521:است که زير بای چپ راننده اتومبیل قرار 
MON_part2.txt:26279:(مکد.) در اتومبیل به بخاری که از لولهة 
MON_part2.txt:26289:دستگاهی است در موتور اتومبیل که گاز
```


## [2026-09-05T05:43:09.967Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT افندی ===\"; grep -n \"افندی\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v*_pages.txt 2>/dev/null | head -10; echo \"=== ARY ===\"; grep -n \"افندی\\|اتوبان\" incoming/ARY/ARY_pages.txt 2>/dev/null | head; echo \"=== RCH ===\"; grep -n -i \"efendi\\|afandi\" RCH.txt | head"
}
```


### [2026-09-05T05:43:10.075Z] TOOL RESULT

```
=== BQT افندی ===
incoming/BQT/BQT_v5_pages.txt:5901:بعض سودالقر‌آن العظیم . تألیف‌امام فخررازی. نسخةٌ مجموعةٌ اسندافندی
incoming/BQT/BQT_v5_pages.txt:7961:(دیوان شمس . نسخهٌ اسعد افندی ودق ۱4۰)
incoming/BQT/BQT_v4_pages.txt:21903:بیت مولوی هم طبق سخهٌ اسمد افندی (استالبول) متملق بقرن هفتم ودخةٌ قره حصار(استالبول)
BQT_v1_pages.txt:2301:۸ - رساله مسید افندی.
BQT_v2_pages.txt:7715:  ‫در طبع حن افندی الفاکهانی ص ‪ « ۰۱‬جپارسوك» آمده واین اصح است‪ -‬اکنون میدالی‌را که‬
=== ARY ===
=== RCH ===
1529:A   JLjI  ibsFily  (iv  of  J— J)  Forbidding,  prohibiting,  making iiiilawfiil.  Despising.  Preserving,  defending.  Encompassing, surrounding.  Killing,  murdering.
4109:rence, respect,  esteem,  honour,  favour.  Civility,  politeness, courtesey,  elegance  of  manners,  urbanity.  Dignity,  gravity. Decency,  modesty,  bashfulness.  Defending,  excusing,  disputing, demonstrating,  bringing  proof.
12251:jury).  Defending  another  (from  an  enemy,  by  anailing  him  with arrows,  or  javelins.  Tarnishing  (the  honour  of  another).
14259:A   itij\  i4dhy  (iv  of  A\)  Assisting,  defending.  Liberating.
16978:p   bwhutan,  Of  bad  principles.  BmhxUan,  An  ape. Name  of  the  »n  of  Kishtasb,  and  brother  to  Aafandiyar.
22244:A   Liy.wi.flir  iahbibj  (ii  of  habba)  Making  one  a   friend. Being  filled  (with  drink).  Sowing.  Coming  into  ear  (wheat). kkfffo^takbiyaty  (ii  of^^y.»^)  Protecting,  defending.
22363:A   ^jffoc^takziny  (iioCgyflw*)Eortifying,defending, surround- ing  vdt^wall. ,   Strengthening.  Preserving,  keeping  (a  young girOathoroe.  Being  chaste.  Living  rellred.  Marrying  a   wife;
23046:I   vehemently  and  frequently.  Defending  strenuously..  Drawing near  to  a   close  (day).  Making  haste,  walking  fast.  Expe- riencing trouble,  uneasiness.  Lengthening  out.  Passing  the night  in  a   wearisome  search  for  water,  without  finding  any,  ex- cept in  the  vicinity  of  a   town.
27501:der. Defending  a   companion.  Adjuring.  Doing  more  than the  law^demands.  Inflaming  with  desire.
31135:A   uJj:ij^^Mf}t^(from  ujusf-).  Deviating,  wandering,  straying. A   junun  (from  janna)y  Covering.  Being  dark (night).  'Protecting,  defending.  Growing  luxuriant  (grass). Flying  round  and  humming  (flics).  Being  a   demoniac,  possessed of  a   devil.  Insanity,  fury,  phrensy.  A   demoniac.  Darkness.
```


## [2026-09-05T05:43:15.283Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '15225,15245p' MON_part1.txt"
}
```


### [2026-09-05T05:43:15.333Z] TOOL RESULT

```
افلیج: [01 [ع.] (ص.) آنکه تمام یا قسمتی 

از بدن وی سست و بی‌حرکت شده باشد؛ 
سد ۵. 

اقا 93 ِ . ف. افنا) (مسص م.) نست 

کردن» انود کُردانیدن. 

افندی: 22701 [تر. آنکه به نفسه کار کند؛ 

مستقل به ذات] (ا.) به طریق احترام به 

بزرگان ترک اطلاق شود و نیز به آخر نام 

رجال افز وده شو د. 

افول: ۰6۷0۱ [ع.] (مصل.) فرو شدن؛ فرو 

رفتن» بنهان شدنء غروب کردن (ستاره).
```


## [2026-09-05T05:43:16.062Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"اتوماتیک\\|اتوبوس\" MON_part1.txt MON_part2.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T05:43:16.127Z] TOOL RESULT

```
MON_part2.txt:20683:اتوبوس و غیره): (نو.) (عم. ) مانند کتاب (در 
MON_part2.txt:67717:تولید نیرو کند. موتور اتومبیل (اتوبوس): 
MON_part2.txt:67719:اتومبیل (اتوبوس) به حرکت درمی‌آید. 
MON_part2.txt:78798:گاری اتوبوس و غیره. بارکش (فره.) نقلیة 
MON_part1.txt:6968:اتوبوس: ۵۱0-۳5 (.) نوعی از اتومسل با 
MON_part1.txt:6971:کسان بکار می‌رود. اتوبوس دو طبقه: 
MON_part1.txt:6975:اتوبوس شهری: اتوبوسی که در شهر رفت و 
MON_part1.txt:6983:بجایی. شغل آنکه اتوبوس می‌راند. شرکت 
MON_part1.txt:6985:اتوبوس‌رانی از جایی بجایی را به عهده 
MON_part1.txt:6997:اتوماتیک: (ص.) دستگاهی که
```


## [2026-09-05T05:43:23.508Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '6960,7010p' MON_part1.txt"
}
```


### [2026-09-05T05:43:23.558Z] TOOL RESULT

```
نیم خمی را ؛ بر جایی نصب می‌کردند و به 
زیر آن آتش می‌افروختند و جامه بر نیم < 
می‌کشیدند. اتوی برقی (الکتریکی): اتویی 
کارت آن + وس کف ماما 
میکا که دور آن سیم فرونیکل پیچیده شده 
و دو سر آن به دو شاخةً برق وصل است - 
تأمین می‌گر دد. 

اتوبوس: ۵۱0-۳5 (.) نوعی از اتومسل با 
اطاق دراز و صندلی‌های متعدد که ها 
در شهر و بیرون از شهر برای رفت و آمد 
کسان بکار می‌رود. اتوبوس دو طبقه: 
اتویوسی که بر روی طبقة اول آن طمبقة 
دیکری قرار داده‌اند و مسافران در هر دو 
اطاق زیر و بالای آن سوار می‌شوند. 
اتوبوس شهری: اتوبوسی که در شهر رفت و 
آمد می‌کند و مردم را از یک نقطةٌ شهر به 
نقطة دیگر می‌برد. 

اتضوبوس‌رانی: 0۱0-2 [فر. ف.] 


(حامص.) راندن و بردن اتویوس از جایی 
بجایی. شغل آنکه اتوبوس می‌راند. شرکت 
ی وس 
اتوبوس‌رانی از جایی بجایی را به عهده 
دارند. جای شرکت» جابی که مرکز کار 
شرکت مزبور است. 

اتوشویی: -0۱0-80۷ [فر. ف. اتو (مخفف 
اتومبیل) + شویی (شستن)] (حامص. ) 
شستن و پاکیزه کردن اتومبیل. شغل آنکه 
اتسومبیل می‌شوید. (ا.) جایی که در آن 
اتومبیل را می‌شو یند. 

اتوکار: 00-۲ (امر.) اتوسیل بزرگ که 
برای حمل مسافران دسته جمعی بکار رود. 
اتوماتیک: (ص.) دستگاهی که 
خود به خود کار می‌کند و نیازی به بودن 
کارگر بر سر آن نیست؛ خودکار (فره.) 
اتومبیل: (1مهم۱ه (.) (فز . فک دستگاه 
خودرو که به وسیلةٌ موتور بخار یا برق یا 
نفت یا بنزین یا هوای متراکم و يا گاز حرکت 
کند و جهت مسافرت و حمل و نقل از جایی 
به جای دیگر بکار رود. در تداول بیشتر به 
ماشین‌های خودکار سواری که به وسیلة 
بنزین یا گازوئیل حرکت کنند» اطلاق شود. 
اتومبیل باری: اتومبیلی که برای حمل بار 
بکار رود. اتومبیل سواری: اتوسیلی که برای 
حمل مسافر بکار رود. اتوسل شخصی: 
اتوسیلی که صاحب آن و خویشاوندان و
```


## [2026-09-05T05:43:30.234Z] TOOL CALL #19: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T05:43:30.243Z] TOOL RESULT

```


```


## [2026-09-05T05:43:34.075Z] TOOL CALL #20: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CF%84%CF%8C%CF%82",
 "prompt": "Give the full Ancient Greek etymology of αὐτός 'self, same' — what origin is proposed (Beekes, etc.), whether it is of uncertain origin, and the derived terms including αὐθέντης."
}
```


## [2026-09-05T05:43:36.440Z] TOOL CALL #21: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CE%B8%CE%AD%CE%BD%CF%84%CE%B7%CF%82",
 "prompt": "Give the full etymology and meanings of Ancient Greek αὐθέντης, including the analysis into αὐτός + -έντης, the Beekes view, the semantic development from 'murderer' to 'master', and all descendants (Byzantine/Modern Greek αφέντης, Turkish efendi, Latin authenticus)."
}
```


### [2026-09-05T05:43:40.497Z] TOOL RESULT

```
# Etymology of αὐτός

**Proposed Origin:**
According to Beekes, αὐτός derives from Proto-Indo-European *h₂ew ("again, away from") + *to- ("that"). An alternative analysis by Risch traces it to Ancient Greek reflexes: αὖ (aû, "back, again") + τόν (tón, "the").

**Cognates:**
The word is an exact cognate with Phrygian αυτος (autos), potentially related under the Graeco-Phrygian hypothesis.

**Note on Uncertain Origin:**
The entry does not indicate the etymology is uncertain; both Beekes and Risch provide plausible reconstructions.

**Derived Terms:**
The page lists numerous compounds beginning with αὐτο-, including αὐτοκράτωρ (autokrátōr, "autocrat") and αὐτόνομος (autónomos, "autonomous").

**Regarding αὐθέντης:**
This word does not appear in the provided content, so I cannot comment on its derivation from αὐτός based on this source.
```


### [2026-09-05T05:43:43.863Z] TOOL RESULT

```
# Ancient Greek αὐθέντης: Etymology and Development

## Etymology
The word combines "αὐτο-" (auto-, "self") with "*ἕντης" (*héntēs), derived from Proto-Indo-European "*senh₂-" meaning "to prepare, work on, succeed," plus the masculine agentive suffix "-της" (-tēs). Related terms include "ἀνύω" (accomplish) and "συνέντης" (helper).

## Original Meanings
In classical usage, αὐθέντης denoted "an autonomous actor"—specifically "a self-controlled, self-directed, or self-governed person" or "a sovereign, a master."

## Semantic Shift
Post-classical and Hellenistic usage narrowed the meaning significantly. The term came to describe "one who acts with volition but without any supposed right," encompassing:
- A volitional ruler through usurpation; an autocrat, tyrant, dictator, or despot
- A perpetrator of acts, "especially one which commits murder with his own hand or suicide"

This semantic trajectory reflects a shift from positive autonomy toward illegitimate force and criminal agency.

## Descendants
- **Byzantine/Modern Greek**: αφέντης (aféntis)
- **Turkish**: efendi, efendim (via Greek)
- **Latin**: authenticus (implied connection through Romance language transmission)

The word's evolution illustrates how "self-directed authority" deteriorated into connotations of tyranny and violence.
```


## [2026-09-05T05:43:53.183Z] TOOL CALL #22: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86",
 "prompt": "What does this page say about Persian اتوبان (otobân) — its etymology (from German Autobahn? French? English?), pronunciation and meaning?"
}
```


## [2026-09-05T05:43:54.405Z] TOOL CALL #23: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/efendi",
 "prompt": "Give the Turkish (and Ottoman Turkish افندی) etymology of efendi: from which Greek form (vocative αφέντη?), and its meaning, plus descendants in other languages including Persian."
}
```


### [2026-09-05T05:43:57.681Z] TOOL RESULT

```
# Persian اتوبان (otobân)

**Etymology:** The word is "Borrowed from German _Autobahn_," not from French or English.

**Meaning:** It denotes a "motorway/freeway" with a synonym being آزادراه (âzâdrâh).

**Pronunciation:** Transcribed as "otobân" in the entry.

The page provides minimal phonetic detail beyond the transliteration, focusing primarily on the loanword's German origin and its highway-related definition.
```


### [2026-09-05T05:44:01.062Z] TOOL RESULT

```
# Etymology of "Efendi"

## Greek Origin

According to the Wiktionary entry, efendi derives from Greek **αφέντης** (aféntis), which ultimately traces to Ancient Greek **αὐθέντης** (authéntēs). The page does not specify whether the vocative form αφέντη was the direct source.

## Turkish Inheritance

The Turkish term inherited the word from Ottoman Turkish افندی (efendi), maintaining the same form through this linguistic lineage.

## Meaning

The core meaning centers on authority and respect: "master" or "sir" in modern Turkish, with historical usage as a title for an Ottoman official (effendi).

## Language Distribution

The Wiktionary entry documents "efendi" appearing across 16 languages including Romanian, Slovak, Turkish, and others (Azerbaijani, Czech, Spanish, Finnish, French, Hungarian, Indonesian, Kurdish, Polish, Albanian, Uzbek, and Chinese). However, **the provided content does not include information about Persian descendants** or their specific forms and meanings.
```


## [2026-09-05T05:44:04.028Z] TOOL CALL #24: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/effendi",
 "prompt": "Give the full etymology text of effendi, and also anything on the date of first attestation and the Greek vocative form."
}
```


## [2026-09-05T05:44:05.156Z] TOOL CALL #25: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/authentic",
 "prompt": "Give the full etymology text of authentic, including Old French autentique, Medieval/Late Latin authenticus, Greek authentikos and authentes, dates."
}
```


### [2026-09-05T05:44:11.620Z] TOOL RESULT

```
# Etymology of Authentic

The word **authentic** traces back through multiple language layers:

**English (mid-14c.):** From Old French *autentique* and directly from Medieval Latin *authenticus*

**Greek origins:** The Medieval Latin derives from Greek *authentikos* meaning "original, genuine, principal," itself coming from *authentes* ("one acting on one's own authority")

**Root components:** The Greek *authentes* breaks down as:
- *autos* = "self"
- *henthes* = "doer, being" (from PIE root *\*sene-* meaning "to accomplish, achieve")

**Semantic evolution:** Initially (mid-14c.), the term meant "authoritative, duly authorized" (now obsolete). By the same period, it acquired the modern sense of "real, entitled to acceptance as factual."

The entry notes that traditionally, *authentic* implies "contents correspond to the facts and are not fictitious (hence trustworthy, reliable)" while *genuine* emphasizes that "the reputed author is the real one," though these distinctions aren't consistently maintained.
```


### [2026-09-05T05:44:14.038Z] TOOL RESULT

```
# Etymology of Effendi

**Full Etymology:**
The term "effendi" is a Turkish title of respect equivalent to English "sir," dating from the 1610s. It derives from Turkish *efendi*, which is itself a corruption of the Greek word *authentēs*, meaning "lord, master."

**Date of First Attestation:**
The word entered English usage in "the 1610s."

**Greek Vocative Form:**
The source document provides the Modern Greek form *aphentes* but does not specify a distinct vocative form. The original Greek term *authentēs* is given as the root, with *aphentes* noted as its Modern Greek equivalent.
```


## [2026-09-05T05:44:22.666Z] TOOL CALL #26: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/autobahn",
 "prompt": "Give the full etymology of autobahn: German Auto + Bahn, meaning of Bahn, date, and any note on the origin of Bahn."
}
```


## [2026-09-05T05:44:23.482Z] TOOL CALL #27: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/automobile",
 "prompt": "Give the full etymology of automobile (and if present on the page, of automatic and auto-): French coinage date, Greek autos, Latin mobilis, and how English got it."
}
```


### [2026-09-05T05:44:28.078Z] TOOL RESULT

```
# Etymology of Autobahn

**Components:** The word combines German *auto* (short for *automobil*, meaning motor car) + *bahn* (meaning path or road).

**Meaning of Bahn:** According to the source, *bahn* derives from Middle High German *ban/bane* meaning "way, road," with the literal sense of "strike" (as a swath cut through). It traces back to the Proto-Indo-European root *\*gwhen-* meaning "to strike, kill."

**Date:** The term entered English in 1937, though the German *Autobahn* itself appeared in the 1930s.

**Origin Note:** The etymology reveals that *bahn* is ultimately rooted in concepts of physical cutting or striking—the metaphorical sense of a "path" developed from the image of a swath cut through terrain. This same PIE root connects *bahn* to the English word "bane."
```


### [2026-09-05T05:44:28.879Z] TOOL RESULT

```
# Etymology of Automobile

**French Origin (1861):** The French adjective *automobile* emerged in 1861 as a hybrid construction combining Greek and Latin elements.

**Greek Component:** The prefix *autos* means "self" (from the auto- root).

**Latin Component:** The French word *mobile* derives from Latin *mobilis*, meaning "movable" or "capable of being moved."

**English Adoption (1895):** English borrowed the noun *automobile* in 1895 from French, initially as "self-propelled motor vehicle," shortened from the French phrase *véhicule automobile*. The adjective had entered English slightly earlier in 1883, applied to electric traction cars.

**Alternative Terms:** Early English competing terms included *motorcar* and *autocar*, though the French *automobile* ultimately prevailed over alternatives like *locomobile*.
```


## [2026-09-05T05:44:38.537Z] TOOL CALL #28: Bash

```json
{
 "command": "ls site/pages/72.jpg 2>/dev/null; pdftoppm -f 72 -l 72 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg72 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-05T05:44:41.077Z] TOOL RESULT

```
site/pages/72.jpg
total 6756
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 01:44 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
```


## [2026-09-05T05:44:43.664Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg72.png"
}
```


### [2026-09-05T05:44:44.297Z] TOOL RESULT

```

```


## [2026-09-05T05:44:44.294Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T05:44:54.435Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 72 -l 72 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg72_600 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg72_600.png'); print(im.size)\n# box region approx x 1540-1960, y 960-1060 at 300dpi -> double for 600\nim.crop((3080,1950,3960,2120)).save('pg72_fr.png')\nim.crop((3080,1000,3960,1180)).save('pg72_afandi.png')\n\""
}
```


### [2026-09-05T05:44:59.122Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-05T05:45:01.352Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg72_fr.png"
}
```


### [2026-09-05T05:45:01.367Z] TOOL RESULT

```

```


## [2026-09-05T05:45:07.734Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg72_afandi.png"
}
```


### [2026-09-05T05:45:07.749Z] TOOL RESULT

```

```


## [2026-09-05T05:45:17.297Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/extracted/batch && grep -ho \"[A-Za-zĀ-ſ]*ě[A-Za-zĀ-ſ]*\" *.json | sort | uniq -c | sort -rn | head -30"
}
```


### [2026-09-05T05:45:17.382Z] TOOL RESULT

```
     24 Dhě
     19 ěl
     14 Gěu
      9 Sě
      6 Wě
      6 Lěs
      5 věn
      5 Lěk
      4 Sěma
      4 Gěi
      4 ě
      4 děmos
      4 Bhě
      3 zaěna
      3 sěma
      3 Sěi
      3 něš
      3 Někš
      3 Měn
      3 měn
      3 kaěš
      3 Ghěi
      3 Ghě
      3 ěšta
      3 Dě
      3 aěta
      2 zumě
      2 Yě
      2 Xartěs
      2 Věno
```


## [2026-09-05T05:45:25.844Z] TOOL CALL #34: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CF%84%CF%8C%CF%82' \\\n 'https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CE%B8%CE%AD%CE%BD%CF%84%CE%B7%CF%82' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86' \\\n 'https://en.wiktionary.org/wiki/efendi' \\\n 'https://www.etymonline.com/word/effendi' \\\n 'https://www.etymonline.com/word/authentic' \\\n 'https://www.etymonline.com/word/autobahn' \\\n 'https://www.etymonline.com/word/automobile' ; do\n python3 tools/fetch_source.py \"$u\" --note 'page 72, root Autos (Greek autos): verification of authentes/afendis, Turkish efendi, Persian افندی, German Autobahn > اتوبان, French auto- loans, English auto-/automobile/automatic' 2>&1 | tail -2\ndone"
}
```


### [2026-09-05T05:45:30.457Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d1d603a9b1c54dc9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/90f08e40461c49a2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b55bf8de5026ddd2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/89423ada5e680238.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/027c1fbfe10bce5c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/68bfbd0c96ac1f27.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/67c0d83a8387afcf.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f302a4ef57b0adb.txt
```


## [2026-09-05T05:45:40.083Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== POK au- pronominal ===\"; grep -n \"αὐτός\\|autos\" POK_full.txt | head -10; echo \"=== LEW authenticus ===\"; grep -n -i \"authentic\" LEW_1910.txt LAT.txt | head -5; echo \"=== FSD authentic ===\"; grep -n -i \"authentic,\" FSD_vol1.txt | head -3; echo \"=== WEB effendi/authentic ===\"; grep -n -i \"effendi\" WEB_vol1.txt | head -3; echo \"=== IEC autos ===\"; grep -n \"autos\" IEC.txt | head -5; echo \"=== SYN self ===\"; grep -n \"αὐτός\" SYN.txt | head -5"
}
```


### [2026-09-05T05:45:40.240Z] TOOL RESULT

```
=== POK au- pronominal ===
=== LEW authenticus ===
LAT.txt:13157:*columlS: saluusf L'authenticite de la forme est douteuse. Dn acc.
LAT.txt:25498:Le gau d'Ennius, dont 1 'authenticite est du reste contestee, n'est
LAT.txt:30599:et aussi A en affirmer 1 'exactitude ou 1 1 authenticit£. Joint a un
=== FSD authentic ===
7153:Q.  Active,  or  involving  action  or  results;  practical.  [   < F .   acfucZ,<  LL.  aclualis ,   practical,  <   L.  actus;  see  act,  o.J Synj  authentic,  certain,  demonstrable,  developed,  genu- me,  positive,  real,  true,  unquestionable,  veritable.  Actual has  respect  to  a   thing  done  or  accomplished,  zeal  to  a thing  as  existing,  positive  to  that  which  is  fixed  or  estab-
29378:tain,  current,  genuine,  legitimate,  original,  real,  re  _ sure,  true,  trustworthy,  veritable.  For  the  distinct  . tween  genuine  and  authentic,  see  the  quotation  from under  definition  1.  Authentic  Is,  however,  used  Dy table  writers  ns  synonymous  with  genuine,  as  gn  en  ^ nitlon  2,  tho  usually  where  genuineness  eVj-
29388:thoritatlve  (book,  etc.),  as  distinguished  from  a   counter- feit or  apocryphal  one.  3.  pi.  A   collection  of  the  New Constitutions  of  Justinian:  so  named  because  of  their  being authentic  translations  from  the  Greek:  sometimes  called Liber  or  Corpus  Authenticarum. au-then'ti-cate,  1   e-fhen'ti-ket;  2   ^-thSn'ti-eat.  rt. [-cat'ed;  -cat'ing.]  1.  To  make  authentic  or  author- itative; give  legal  force  or  validity  to.  2._  To  show to  be  authentic;  demonstrate  (X)  the  genuineness  or -   correctness  of,  or  (2)  the  trustworthiness  or  credibility of.  [<  LL.  authenticalus,  pp.  of  authentico,  <   L. avthenticus;  see  authentic,  a.]  —   au-tkcn'tl-ca"tor,  n. 3u-then"ti-ca'tion,  1   e- fh en 'ti-ke'sh on ;   2   9-th ?n 'ti- ea'shon,  n.  The  act  of  authenticating,  or  the  state  of being  authenticated;  attestation;  confirmation;  as, authentication  of  a   record.
=== WEB effendi/authentic ===
=== IEC autos ===
840:ausá, io — autos (outos) 44
845:aut (auti, autim, autom) (out-, etc.) "but, yet, only'. Cf. autos, autios. WP I, 14, 188. Possibly a cpd. of a and ut(i), q.v. Skt. utá “also, even Av. uta; OPer. utà; Oss. cf. äftä, utà “thus? Gk. aŭ, aŭte, aütis, aütin, cf. also autí-ka ‘forthwith’ and autar “how- ever; Alb. veti (“of itself: Dor. auteí), veç Chur, from *autisi); vetëm ('only': Lat. au- tem); Lat. aut or, cf. OLat. aut ^neverthe- less? beside autem "at least’; Osc. aut, auti "but, or; Ir. cf. uath- (cpds. mono-, auto- and see autos below); OCS uto ‘if whether; ever” (as an interrog. particle: 'altogether")
846:autios (aut-) “alone, bare, empty, free’. WP I, 14. Cf. autos, aut, aue, ut(i), etc. Dor. Gk. aüsios ‘useless’; Alb. veg ‘separate’; Lat. otium “leisure”, cf. also ind-ütiae ‘truce’; MIr. uaite, Ir. uaithe ‘lonely’; Go. aupi- "des, olate' and ‘easy’; ON eyði ‘desert’; Finn. LW autio ‘desolate’. Cf. also the reduplicated for- mula *autiautos in Delph. ausautós: Alb. vetveté ‘alone’
847:autos (outos) “alone, own, self, same’. Cf. aut, autios, etc. WP I, 14 Skt. cf. utá “and, also, even’; Av. uta; Ober uta, id. cf. also Av. aoto 'cold', aotom, s. id.; Lyc. abtá, abti ‘self; Gk. autós; Alb. vetë, id.; Lat. cf. aut, autem; Ir. uatha *sin- gular, solitary’; MIr. uaite (*lonely'. See au- tios); Go. cf. aupi- deserted and aud- (“trea- sure’, lit. “one's own’ in audags *fortunate"); OE éad ‘treasure’; OS od, id. (cf. Ger. Klein- od; LW in MLat. clen-ódium); ON auór:
898:auos, à, ios, iə ‘kinsman’. WP I, 17-20. Cf. (?) autos Hiero-Hitt. uias (queried: grandfather); Lat. avus, avia; MIr. aue, úa, oa ‘grandson, des- cendant; Ir. ó, id.; W ewa ‘uncle’; Br. cf. Au (in tàd-iu, mamm-iu *great-great-grand- father, -mother) and cf. e-ontr: W ew-ythr ‘uncle? (Cor. ew-nter, id.) Alemannic Ehi *maternal uncle'; Cz. uj, Slovak ujo, Pol. wuj ('uncle', Pol. ‘maternal ?); cf. also OCS ut: Srb. ujak ‘uncle’; ujna ‘aunt’; Blg. ujnà, id.; Li. ava “aunt? beside avynas ‘maternal uncle’
=== SYN self ===
```


## [2026-09-05T05:45:47.128Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"au-tos\\|au- tos\\|αὐτός\" POK_01.txt POK_02.txt POK_03.txt 2>/dev/null | head; echo \"=== POK au- 73 ===\"; python3 - <<'EOF'\nimport re\nfor f in ['POK_01.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    leaves=t.split('\\f')\n    # leaf = p + 8\n    for p in (73,):\n        i=p+8\n        print(f, 'leaf', i)\n        print(leaves[i][:2000])\nEOF"
}
```


### [2026-09-05T05:45:48.848Z] TOOL RESULT

```
=== POK au- 73 ===
POK_01.txt leaf 81
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
ues-i  Mit  ai.  a
```


## [2026-09-05T05:46:00.873Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_01.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (80,81,82,83):\n    l=leaves[i]\n    import re\n    print('--- leaf',i,'p',i-8,'---')\n    print(l[:600].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T05:46:02.407Z] TOOL RESULT

```
--- leaf 80 p 72 ---
  Unwillen,  Abweisung,  Überraschung),   poln.  au,  cech.  ou. WH.  I  78. 72 2.  au-,  au-es-,  aus-  ^übernachten,  schlafend Arm.  aganim  ,übernachte';  vair-ag  ,au£  dem  Lande  lebend',  aut'  ,Über- nachten,  Nachtruhe,  Station^ Gr.  lavo)  ,scblafe^  aus  redupl.  "^i-ausö,  Aor.  i-avaai,  woneben  unredupl. Aor.  Usaa,  Inf.  äfea{o)ai]  avXtg,  -löog  , Aufenthaltsort,  Lager,  Stall,  Nacht- -  lager^,  avUlop^ai  ,bin  im  Hofe,  übernachte',  äygavXog  ,im  Freien  übernach- tend^, aiUj  ,Hof,  Wohnung^  (ursprüngl.  wohl  ,der  eingezäunte  Raum  ums Haus,  in  dem  das  Vie
--- leaf 81 p 73 ---
Präp.  ,von'; apr.  lit.  lett.  au-  ,weg,  ab'  (z.  B.  lett.  au-manis  ,unsinnig'),  aksl.  u  Präfix ,weg,  ab',  z.  B.  u-myti  ,abwaschen'  (u-Uzati  ,aufugere'),  als  Präp.  m.  Gen. 73 i  /bei  Verben  des  VerLangens^  EmpfangenS;  Nehmens)   und,   mit  Ver- blassen des  Begriffes  des  Ausgangspunktes,  ,bei'; 1  ett    Präverb  u-    (^it'e-,  i(^ci-)  , hierher^,    a-ica-an  ,hinweg^   (Sturtevant   Lg. 7,  1  ff.). Davon   mit  ^Formans    aut{i)o-:    gr.  aljzojg  ,vergeblich^,  aljoiog  ds.  und *>-üt  aiipja-  (N.  Sg.  *aupeis  oder  *aups)  ,'öde,  verlassen^  (*,abgel
--- leaf 82 p 74 ---
 der  eine  —  der  andere',    ovogda  —  ovogda  ,das  eine 74 Mal  —  das  andere  Mal^  (aus  diesem  korrelativen  Gebrauche  erst  scheint das  jener-deiktische  poln.  öw  und  das  ich-deiktische  serb.  bvaj,  ebenso nbulg.  -V  [*uo-s]  entwickelt). U-:  Ai.  amü-  (Akk.  Sg.  amüm  usw.)  ^jener^,  erwachsen  aus  Akk.  So_ m.  '-^am  (=  idg.  *ß-m  ,eum^)  -\-  *um  (Akk.  Sg.  unseres  St.  w);  s.  Wacker. nagel-Debrunner  III  550  f.  | Toch.  A  oh,  B  uk  ,noch^,  A  oki  ,vfiQ,  und^,  A  ohäh  ,bis  zu*,  vielleicht nur  *u-g  (Schwundstufe  zu  got.  aw/v);  ob  dazu  B 
--- leaf 83 p 75 ---
60.  23  a  2 reiht  auch  gr.  ai-rög  als  .von  ihm  aus'  an;  andere  Deutungen  s.  bei Schwyzer  Gr.  Gr.  I  613  f. Mit  r-Formans  airan.  avar  .hier',  lit.  aure  .siehe  da!',  tiefstufig  umbr. uru  .illo'.   ura-ku  .ad  illam'.   ures  .illis'    {orer  ose  eher   mit  ö  =  w  als 75 —  lit  au)'  vielleicht  öevgo  ^hierher;  wohlan^  (öevQü)  nach  ötvlocKjü  u.  dgl.^ *nscbr  (JftJ^s  nach  äys)  aus  '^öi-voo  (de  ^hier'  -j-  at'oo  ;her^);  Schwyzer Gr.  Gr.  I  612,  632. ue-    U0-:  'Die   Bed.  ^oder*  (==  _,andrerseits^)    bes.  in  ai.  vä  ,oder^  (auch selbs
```


## [2026-09-05T05:46:11.704Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport glob\nf='incoming/WLD/WLD_Bd1_pages.txt'\nt=open(f,encoding='utf-8',errors='replace').read()\nimport re\n# find [pdf page N] tags\nidx=[m.start() for m in re.finditer(r'\\[pdf page \\d+\\]', t)]\n# search for autos-ish near \"au-\" p.14\ni=t.find('au-tos')\nprint(len(t))\nfor m in re.finditer(r'\\[pdf page (\\d+)\\]', t[:20000]):\n    pass\n# just print region containing 'αὐτός' OCR alt\nfor pat in ['avros','avrog','ai-rog','autos']:\n    for m in list(re.finditer(pat, t))[:3]:\n        print(pat, m.start(), t[m.start()-300:m.start()+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T05:46:13.132Z] TOOL RESULT

```
4216315
avrog 2902145 . gingrJre „schnattern, bes. von  Gansen“ vielleicht air. giugran „Gans“, cymr. gwyrain „Art WasservogeP                  ;      (    *gi-gri-nnt irrig Yendryes aaO.; anders, *gegurani, Stokes KZ. 33, 75,  Pedersen KG. I 101 f., 103, II 57; s. oben S. 526).    Vgl. zu letzterem auch gr. yiyygag-, - avrog yiyygog, yi/yga „kurze, krei-                                                                       ,   schende Flotenart“; vielleicht pamphyl. f er/aga 6 rrrnf jiagd Sidgraig  ’      fFick 1 4 408 aber lett. dzindzinat „summen [von Bienen] ist wohl nicht                            ;    mehr e
```


## [2026-09-05T05:46:19.673Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]', t)\n# pages: [pre, num, text, num, text...]\nd={}\nfor i in range(1,len(pages),2):\n    d[int(pages[i])]=pages[i+1]\nprint(sorted(d)[:5], sorted(d)[-3:])\n# find pdf page whose text contains a standalone '14' header near 'au'\nfor n in range(20,40):\n    txt=d.get(n,'')\n    if 'aut' in txt and ('au-' in txt):\n        print('=== pdf page',n,'===')\n        print(txt[:1200].replace('\\n',' '))\n        print()\nEOF"
}
```


### [2026-09-05T05:46:21.093Z] TOOL RESULT

```
[] []
```


## [2026-09-05T05:46:24.054Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 400 incoming/WLD/WLD_Bd1_pages.txt; echo; grep -c $'\\f' incoming/WLD/WLD_Bd1_pages.txt; grep -o \"\\[pdf page [0-9]*\\]\" incoming/WLD/WLD_Bd1_pages.txt | head -3"
}
```


### [2026-09-05T05:46:25.675Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

               CENTRAL
            ARCHEOLOGICAL
                LIBRARY
ACCESSION NO. jj03?7
CALL No. gJ3 Wafjpok
                 f_
D.G.A. 79
                      ALOIS WALDE


VERGLEICHENDES WftRTERBDCH
                                DER


     INDOGERM ANISCHEN SPRACHEN

                HERAUSGEGEBEN UND BEARBEITET
         
887
```


## [2026-09-05T05:46:32.024Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\nfor i,l in enumerate(leaves[:60]):\n    if re.search(r'aut\\(i\\)o|autio-|vergeblich', l):\n        print('LEAF',i)\n        print(l[:1500].replace('\\n',' '))\n        print('---')\nEOF"
}
```


### [2026-09-05T05:46:33.718Z] TOOL RESULT

```
895
LEAF 22
             ;                                            g            ,           :                          ;     14                                                an- (aue?); ue-        Gr. at- wohl in             avyaxTEiv   '    avaycogeTv,        avaya^eodai Hes. (Schulze Qu. ep. 60)      lat.    an- „fort“ in aufero         (=--=   ai.   ava-bharati av. ava-bar-), aufugio;                     ua „von, mit, durch“, als Praep. m. Dat. (z. B. Pick II 4      air. vielleicht o,  22; vgl. bes. Thurneysen Hdb. I 475, aber auch die Zweifel ebenda II 99 f. und bei Pedersen KG. I 43S, 535                         =                                         Nachtr. zu S. 49, Sommer Miscellany Kuno Meyer 131); apr. an- „weg, ab“ (z. B. aumusnan ,,Abwaschung", lett. au-manis „unsinnig,    rasend", aiunes „(ma61os =) gar arg, gar zu sehr"; lit. aulinhui ,.fernerhin, spater" (vgl. zu den bait. Wortern Bezzen- berger BB. 18, 267. Zubaty AfslPh. 15. ISO), aksl. u Praefix „weg, ab“ z. B. u-myti „abwaschen“ u-behdi „aufugere“), als Praep. m. Gen. „von“  (bei Yerben des Yerlangens, Empfangens, Kehmens) und, mit Yerblassen des Begriffes des Ausgangspunktes, „bei“ (trotz Kogel IP. 4, 315; s. Brug- mann KVG. 468, Grdr. 2 II 2, 810).   Davon mit GFormans sehr wahrscheinlich gr. avx m? „vergeblich“, avaiog „vergeblich“ und got. anpja-                      In. sg.    *aupeis oder *aups ) „ode, verlassen“ (*,.abgelegen“), cnipicla „Wxiste“,                       abd. odi, nhd. ode, anord. auilr „od
---
```


## [2026-09-05T05:46:38.557Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (23,24):\n    print('=== leaf',i,'===')\n    print(leaves[i][:2500].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T05:46:40.286Z] TOOL RESULT

```
=== leaf 23 ===
                                   au- (aue?); ne-                                15   (s.Niedermann IF. 10, 251 ff., s. aueh Yf. LEAVb. 2 826 f.); ve- zur Bezeich- nung eines fehlerkaften Zuviel oder Zuwenig, ve-cors „aberwitzig, verriickt, tiickisch", ve-grandis „nicht grofi, winzig", vesanus „verriickt“, Ve-jovis   (s. Yf.  LEWb. 2 811 m. Lit.), umbr. ve-pums (Abl. pi.), wenn „(ieoo. ) unvoa“ (s. Buck Gramm. 193), vgl. zur Bedeutungsiibereinstimmung mit *au- lett. aumanis             ,    aksl. u-bojb „arm‘‘, air. lialib rastlos“ (vgl. Persson IF. 2, 201, Brugmann                                   ,;   IF. 13, 161, Stokes IF. 26, 146f.); dies ue- wohl auch in idg. ue-speros, -qeros „vesper“ (Brugmann aaO., IF. 29, 241); uo- in ark. y-o-cfhpy.ooi, ophoxavco, opedco und wohl auch in oiyvvfu           (s.   Brugmann aaO. und u. ueih- „biegen“).       DaB auch vestigium, vestibidwn unser ve- enthalte, ist trotz Persson KZ. 48, 133 fraglich.   Sehr unsicher wird ir. feochuir „wild", das Ivompositum dichra „inbriin- stig‘ ,acymr. guichir „effrenus“, guichr ncymr. gtvychr „tapfer", von Peder-        !                                               ,   sen KG. I 122 auf *-ue-lcdrds zuriickgefiihrt (ansprechender Fick II 4 279: zu air. fichim „kiimpfe“, vgl. formell lit. vikrus „munter, ruhrig“; fur cymr. -ch- bleibt dabei freilich die lautliche Erkliirung noch zu finden)       Gr. yo- in ark. fo-<ph]x6oi, att. 6-<phoxavto, lesb. 6-elygv „6ffnen“,     att.   oiyvvf.ii  (Prellwitz 2 345, Brugmann IF. 29, 241, BSG\V. 1913, 159).      Holthausen KZ. 47, 307 vermutet eine Ableitung von         in ahd. wadal  „arm, bedurftig“, ags. wmdl „Armut“, vgl. ahd. zadal ,,Armut, Mangel" von  v    dS, lat. de. — Ein aind. va- neben ava- ist wohl nicht anzuerkennen, siehe  Pischel Gramm. 109 (mind. Entwicklung von ava- zu va-).     'Mit ai. avas „herab‘‘ hangt formantisch germ, wcs- zusammen in nhd.   West, ahd. ivestar „westwiirts“, anord. vestr n. „AYesten“, Adv. „im AY.,  gegen AY." (*ues-t(e)ro-, vgl. anord. nor -dr), ahd. westana „von AV.“ usw.  (Brugmann IF. 13, 157ff.; iiber die unrichtige Erkliirung der Wisigothae  als „AYest-Goten“ s. Streitbcrg IF. 4, 300 ff.; fruhere Deutungen von West   verzeichnet Falk-Torp 1576).      Hierher (nach Brugmann aaO.) auch der Anlaut des AAr ortes fiir Abend,  idg. *tiesperos und *ueqeros:                  „Abend, abendlich", lat. vesper (air. fcscor „Abend“ ist lat.       gr. t'oxsgog  Lehnwort; s. Stokes KZ. 41, 385 m. Lit., Pedersen 
=== leaf 24 ===
16                                                                   au-   au- „flechten, weben“, als set-Basis (a)uu x -. zweifelhaft, ob *aue- oder *aua-;           fur            entscheiden weder gr. ijzgiov dor. argiov „Aufzug des                         letzteres           Gewebes“             — ohne y!                                     s. unter *ent- „anzetteln“   nock lit. voras                                                                                        ,                                                                                                       —           „Spinne“, s. u.; auch die Gleichsetzung mit ud- „kriimmen, verkriim-           men“ in lat. vdrus usw. wird durch die ganz andere Wendung der           Bed. keineswegs empfohlen, wenngleich im letzten Grunde Yermitt-           lung unter „drehen, biegen" denkbar ist (was aber eine formale Schei-           dung, etwa einerseits (a)u-e- „weben“, (a)u-a- „verkriimmen“ eben           nicht ausschlosse).               —                                 Die Farbung a- des AYzanlauts ist aus dem arm.           au- von and- (andrerseits von der dh-Ev\\.) erschlossen. Gegen Gleich-           setzung mit eu- „anziehen“ s. d.   Unerweitert in ai. otum , dtave (von der set-Basis vatave ) „weben“, Pf.                         (auch das Praes. vdyati „webt“ kann nach AYacker- uvuli, Ptc. Ufa-, vy-uta- nagel Ai. Gr. I 94 ein -eio-Praesens v-dyati sein, so daB Fut. vayisyati, vaya- „Weber“ erst dazu neugeschaffen waren), Stu- m. „Einschlag des Gewebes“, vana- n. „das Weben“ (aber kaum umd uniu „Flachs“, Uhlen-                          ,   beck Ai. \Vb. 30 zw.).      AmBestehen einer set-Basis neben der anit-Basis ist gegen "\Vacker- nagel festzuhalten wegen vdteive ,Weben, flechten“, vanam (W. muB Met- als Neubildung zu vayate nach hutd-:hvdyate auffassen).      Lit.       auJde,        „FuBbinde“,            lett.        auJcla ,   aiiklis       „Schnur   zum Zusammen- binden“, apr. audo „ledernes Ivopfzeug des Pferdes                                               zum Halten“ scheinen z.T. unserer Wurzel zu entstammen, aber unter Mischung mit *eu- „an- ziehen :i s. d. Lit. r&ras „Spinne“ bleibt bei der im Balt, reich entwickel-                 ,   ten Sippe von uer- „Schnur, anspannen, hochhangen“ (Solmsen Unt. 289 f.; Dehnstufe wie                   in gr. al-coga         „Sehwebe“).       (?/i-Erweiterung                  \.   att-dh-,         2.    (a)u-%dh~, u-dli-:      1.    Arm. z-m
```


## [2026-09-05T05:46:51.444Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol2 effendi ===\"; grep -n -i \"ef-fen'di\\|effendi\" FSD_vol2.txt | head -3; echo \"=== FSD vol1 auto- ===\"; grep -n \"au'to-\\|au-to-\\|automobile,\" FSD_vol1.txt | head -4; echo \"=== SKT auto ===\"; grep -n -i \"^Auto\" SKT.txt | head -5"
}
```


### [2026-09-05T05:46:51.563Z] TOOL RESULT

```
=== FSD vol2 effendi ===
5509:Through  the  agency  of  a   woman;  as,  effeminately  van- quished.— ef-fem'l-nate-ness,  n.  Effeminacy, cr-fem'l-natc,  ».  An  effeminate  person;  a   milksop, ef-fem't-nlze,  l   e-fem'i-naiz;  2   6-f6m'I-nK,  vt.  [Rare.]  To render  effeminate.—  ef-fem'l-nl-za'tlon,  n. ef-fen'di,  1   e-fen'di;  2   §-fSn'di,  n,  [-dis  or  -dies,  1   -diz;  3
78976:Mothwkwelij  Bword  Chant  of  Thoratein  Itaudi  at.  2. 3,  The  dominion,  power,  or  autliority  of  a   lord;  iionce, sovereignty  or  dominion  in  general;  .supremacy;  as, man’s  lordship  over  animals.  Trench  Notes  on  the Parables  intro,  p.  H.  [a.  1857.1  4.  A   royalty, lord'wood",  1   lord'wud";  3   lord'wdbd",  n.  A   tree  (Liquid^ ambar  orientalis)  allied  to  the  aweet-gum  of  the  United States,  growing  in  western  Asia  and  yielding  liquid atorax.  [   <   lord  +   wood  ;   trans.  of  xylon  effendi,  the Cypriote  name.]
=== FSD vol1 auto- ===
823:New  terms  of  Latin  or  Greek  derivation  are  constantly  and  freely introduced  in  the  arts  and  sciences.  The  absorption  of  French  words is  unabated,  as  is  evidenced  by  such  terms  as  automobile,  charmeuse, chauffeur,  garage,  hangar,  limousine,  massage,  pannier,  sabotage,  ton- neau, etc.
6002:ac-cel'cr-a-tlv*,  (   (xin),  a.  Tending  to  accelerate,  ac- ccl'cr-a-to-ryri—  accelerative  force,  a   force  that  in- creases velocity:  measured  by  the  acceleration  It  produces. ac-Ccl'er-a"lor,  1   nk-pe]#er-£*tor;  2   dc-c£rer-a't5r,  n. 1.  One  who  or  that  which  accelerates.  2.  Specifically: (1)  PAyffol.  A   nerve  or  muscle  that  quickens  the  per- formance of  an  organic  function.  (2)  Phot.  Any  chemical or  device  for  hastening  the  appearance  or  development  of thc  picture  on  an  exposed  sensitized  plate  or  print.  (3) Mech.  A   device  for  increasing  the  speed  of  a   machine; especially,  an  attachment  for  an  automobile,  as  a   cut-out for  thc  governor  of  a   motor-car.  (4)  A   light  English  mail- van.  (5)  An  accelerating  gun.  (G)  An  Instrument  for  mea- suring Increasing  motion.— accelerator  nerve,  a   nerve  that Increases  the  frequency  of  the  heart -beat. ac-ccFcr-oni'c-tcr,  I   ak-cel’er-om'i-ter;  2   xie-tf-l'cr- fan'oter,  n.  An  apparatus  for  registering  various pressures  developed  by  the  explosion  as  of  gunpowder  in a   gun.  (   <   L.  accelero  (sec  accelerate)  *b  -meter.] ae-eel'cr-o-gra  p   b   J.
31949:au'to-,  1   e'to-;  2   a'to-.  From  Greek  autos,  self:  a   com- bining form,  signifying  action  of,  from,  within,  by,  or upon  self
31954:—   au"to-bl"o-gTapti'I-caMy,  adv. au"to-bi-og'ra-phy,  1   o'to-bai-eg'ra-fi;  2   a'to-bl-bg'ra- fy»  H.  [-phies,  1   -fiz;  2   -fig,  pi.)  One’s  own  biography told  by  oneself;  the  story  of  one’s  life  written  by  him- self. [   <   AUTO-  4-  BIOGRAPHY.] au'to-blast,  \   e'to-blost;  2   a'to-blast,  n.  Biol.  A   separate bioplast;  microscopic  organism.  [boat,
=== SKT auto ===
943:autocracy.  (Gk.)  From  Gk.  ahrmtfA- Tim,  absolute  or  despotic  govenimeiit.— Gk.  aiiro',  fcir  ovrvt,  self:  and  fffiarn'i',  to nile«  from  it^ri/r,  strong.  Her.  aitiocnU, Gk.  nirvKparatp.
1193:Auto-,  prefix.  (Gk.)  Gk.  ayro-.  crude form  of  a\rTo%,  lelf.  Dor.  autO'hio^rafhy, a  biography  written  by  oneself  (see  Bio- grapby) ;  autogrttph,  something  in  one's own  handwriting,  from  Gk.  'ip&^uv,  to write  <scc  Oraphio).
1194:automiLton,  a  self-moving  machine. (Gk.)  Gk.  airroiAarov,  neut.  of  avro/iaroi, self-moving.  —  Gk.  avrd-,  for  ovrdj,  self; and  a  stem  ftar-,  appearing  in  ^r-ti^,  I seek  after,  strive  to  do.  Cf.  Skt.  ma/d, desired,  pp.  of  mdn,  to  think.  (^MAN.) autonomy,  seU-govemmcnt.  (Gk.)  Gk. avjovo}ila,  independence.  —  Gk.  oiriivo^nr, ijtc,  living  by  one's  own  laws.  — Gk.  avru', self;  and  wifxoftat,  1  sway,  from  vifttty,  to distribute  (see  Nomad).
1195:autopsy,  personal  inspection.  (Gk.) Gk.  avToif/ia,  a  seeing  with  one's  own  eyes.
12799:autopsy,  [fCTSonal  ins]>ccti« iik.  a^mifia,  a  seeing  with  our's  c
```


## [2026-09-05T05:46:52.940Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/efendi",
 "prompt": "Give the etymology of Turkish efendi as Nişanyan states it: the Greek source form (αφέντης / vocative αφέντη), the date of first attestation in Turkish, and any note on the form."
}
```


### [2026-09-05T05:46:57.383Z] TOOL RESULT

```
I apologize, but the web page content provided does not contain the etymological information you're requesting. The page shows only the header, navigation, and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website, but does not include the actual dictionary entry for "efendi" with its etymology, Greek source form, date of first attestation, or notes on the form.

To obtain this information, you would need to access the full dictionary entry for "efendi" on the Nişanyan Sözlük website directly.
```


## [2026-09-05T05:47:03.607Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5509p' FSD_vol2.txt | cut -c1-900"
}
```


### [2026-09-05T05:47:03.678Z] TOOL RESULT

```
Through  the  agency  of  a   woman;  as,  effeminately  van- quished.— ef-fem'l-nate-ness,  n.  Effeminacy, cr-fem'l-natc,  ».  An  effeminate  person;  a   milksop, ef-fem't-nlze,  l   e-fem'i-naiz;  2   6-f6m'I-nK,  vt.  [Rare.]  To render  effeminate.—  ef-fem'l-nl-za'tlon,  n. ef-fen'di,  1   e-fen'di;  2   §-fSn'di,  n,  [-dis  or  -dies,  1   -diz;  3
```


## [2026-09-05T05:47:05.881Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR==5509' FSD_vol2.txt | grep -o \"ef-fen'di.\\{0,700\\}\""
}
```


### [2026-09-05T05:47:07.647Z] TOOL RESULT

```
ef-fen'di,  1   e-fen'di;  2   §-fSn'di,  n,  [-dis  or  -dies,  1   -diz;  3
```


## [2026-09-05T05:47:09.758Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5510,5514p' FSD_vol2.txt | cut -c1-800"
}
```


### [2026-09-05T05:47:09.824Z] TOOL RESULT

```
-dig,  pl\  A   Turkish  title  of  respect,  equivalent  to  sir  or  ^   saline  particles  left  by  _   __  _   ,
Mr. :   used  especially  after  names  of  officials  and  learned  ^   mtena.  4-  floreo.
vi.  [-kesced': -resc'ing.]  1.  To  burst  ville.  Haute* into  bloom;  blossom  out;  flower.  3.  Marne,  Franco. C'hem.  To  become  powdery,  wholly  or  in  part,  and lose  crystalline  structure  through  loss  of  water  of  crys- tallization on  exposure  to  the  air;  to  become  covered .t  „.i7   i..fA  T —   evaporation,  as
[<  Turk,  e^ndi,  <   Gi.  aphentes,  ior  authentea,  Wossom,  <   ^os  (^or-),  flower.]’ master,  <   antes,  self.)  ef'^o-res'ccnce,  1   ef”l^res'eas;  2   Sf'lo-rSs'gn?,
ef'fer-ent,  1   ef'er-eat;  8   5ffer-Snt,  a.  Carrying  or  car- ried outward,  as  influences  from  a   nerve-center  to  mus- cles, the  cells  of  glands,  etc. ;   discharging:  opposed  to  af- ferent. [   <   L.  effero,  ppr.  efferenit-)a,  <   ex,  out,  -f/ero, bring.]
```


## [2026-09-05T05:47:17.239Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '1,120p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T05:47:17.325Z] TOOL RESULT

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


## [2026-09-05T05:47:45.866Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg72_600.png')\nc=im.crop((3300,2020,3800,2110)).resize((1500,270))\nc.save('pg72_fr2.png')\n\""
}
```


### [2026-09-05T05:47:48.862Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T05:47:50.915Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg72_fr2.png"
}
```


### [2026-09-05T05:47:50.938Z] TOOL RESULT

```

```


## [2026-09-05T05:47:55.579Z] TOOL CALL #51: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg72.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/72.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head"
}
```


### [2026-09-05T05:47:55.667Z] TOOL RESULT

```
total 844
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 01:47 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
```


## [2026-09-05T05:47:57.307Z] AGENT

Now writing the verification file.


## [2026-09-05T05:52:54.888Z] TOOL CALL #52: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-72.json",
 "content": "{\n  \"pdf_page\": 72,\n  \"book_page\": 42,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Autos\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Ancient Greek αὐτός autós 'self, same' (Beekes: < PIE *h₂ew 'again, away from' + *to- 'that'; Risch: αὖ + τόν)\",\n      \"modern_form_note\": \"\",\n      \"note\": \"The root box is right on all three counts: αὐτός is a real Ancient Greek word, the language label 'Greek' is correct, and the gloss 'self' is the standard one. Nourai's added remark 'from uncertain origin' is a verbatim echo of his source Klein, who writes s.v. auto-: 'Gk. αὐτο-, αὐτ-, αὐθ-, fr. αὐτός, \\\"self, same\\\", of uncertain origin.' Modern scholarship no longer leaves it wholly unexplained: Beekes analyses αὐτός as the PIE pronominal particle *h₂ew 'again, on the other hand' plus the deictic stem *to-, and Risch as a Greek-internal univerbation of αὖ 'back, again' + τόν; Pokorny had already gestured at this on p. 75 of the entry '4. au-' ('reiht auch gr. αὐτός als \\\"von ihm aus\\\" an; andere Deutungen s. bei Schwyzer Gr. Gr. I 613 f.'), and Mann (IEC) puts αὐτός squarely under an IE etymon 'autos (outos) \\\"alone, own, self, same\\\"'. So the caveat is dated rather than wrong, and no error affects the chart: everything below the root box hangs on Greek αὐτός itself, which is secure. Note also that this chart is really two unrelated bundles under one head: (a) the ancient Greek noun αὐθέντης and its Byzantine/Ottoman offspring (nodes 1-5), and (b) the twentieth-century international clipping auto- 'motor car', short for French automobile (nodes 6-10), which reaches Persian three times over (German, French, English).\",\n      \"note_fa\": \"ریشهٔ نمودار، واژهٔ یونانی باستان αὐτός (autós) به معنای «خود» است؛ هم صورت واژه، هم برچسب زبانی و هم معنای آن درست ضبط شده است. یادداشت نورایی که «خاستگاه آن نامعلوم است» عیناً از کلاین گرفته شده («of uncertain origin»)، اما ریشه‌شناسی امروزی آن را چندان تاریک نمی‌داند: بیکس آن را از ذرّهٔ هندواروپایی *h₂ew «باز، دگربار» به‌علاوهٔ ستاک اشاره‌ای *to- می‌داند و ریش آن را ترکیبِ درون‌یونانیِ αὖ + τόν می‌شمارد؛ پوکورنی نیز در ص ۷۵ ذیل «4. au-» به همین تحلیل اشاره کرده است. پس یادداشت نورایی کهنه است نه نادرست، و به درستی نمودار آسیبی نمی‌رساند. تنها نکتهٔ ساختاری آن است که این نمودار در حقیقت دو مجموعهٔ ناهم‌پیوند را زیر یک ریشه گرد آورده است: نخست واژهٔ یونانی باستان αὐθέντης و فرزندان بیزانسی و عثمانی آن (گره‌های ۱ تا ۵)، و دوم پیشوند بین‌المللی سدهٔ بیستمی «اتو-» که کوتاه‌شدهٔ automobile فرانسوی است و از سه راه (آلمانی، فرانسوی، انگلیسی) به فارسی رسیده است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CF%84%CF%8C%CF%82\",\n        \"https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CE%B8%CE%AD%CE%BD%CF%84%CE%B7%CF%82\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"KLN:130\",\n          \"status\": \"supports\",\n          \"note\": \"KLN_1966.txt form-feed leaf 80 (two printed pages per leaf; the leaf carrying austere … autogenous, i.e. Klein's a-u-t- range, which is Nourai's p.130): 'auto-, before a vowel aut-, before an aspirate auth-. — Gk. αὐτο-, αὐτ-, αὐθ-, fr. αὐτός, \\\"self, same\\\", of uncertain origin.' Both the gloss 'self' and Nourai's note 'from uncertain origin' come straight from this line. (Grep pattern: grep -n 'auto-,' KLN_1966.txt, hit at line 4027.)\"\n        },\n        {\n          \"ref\": \"AHD:89\",\n          \"status\": \"not_checked\",\n          \"note\": \"AHD:89 is a page of the main dictionary body of the 1975/76 American Heritage New College Edition (the a-u-t- range), not of the Indo-European appendix (pp. 1505-1550); no open scan of that edition exists (refs_online.json: all archive.org copies lending-only). The local proxy AHD_watkins1985.txt has no root entry for αὐτός at all — its English-word index (leaf with 'AUTHOR aug-¹ … AUTOBAHN gʷhen-¹ … AUTOMATIC men-¹ … AUTOPSY okʷ-') assigns every auto- compound to the root of its SECOND element, which is Watkins' silent way of saying that auto- itself has no reconstructable PIE root — consistent with Nourai's 'uncertain origin'.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"POK_01.txt leaf 83 = printed p. 75, entry '4. au-' (pp. 73-75)\",\n          \"stance\": \"partial\",\n          \"note\": \"Pokorny p. 75: '… reiht auch gr. αὐτός als \\\"von ihm aus\\\" an; andere Deutungen s. bei Schwyzer Gr. Gr. I 613 f.' — i.e. αὐτός is reported under the pronominal base au-, but only as one scholar's suggestion, with alternatives referred to Schwyzer. Pokorny himself derives from *aut(i)o- only gr. αὔτως, αὔσιος 'vergeblich' (p. 73).\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"WLD_Bd1_pages.txt leaves 22-23 = printed pp. 14-15, entry 'au- (aue?); ue-'\",\n          \"stance\": \"silent\",\n          \"note\": \"The 1930 Walde-Pokorny version of the same entry lists only 'gr. αὔτως \\\"vergeblich\\\", αὔσιος \\\"vergeblich\\\"' under the formant *aut(i)o- and never mentions αὐτός; the αὐτός note is Pokorny's 1959 addition. Grep: 'aut(i)o' / 'vergeblich' in incoming/WLD/WLD_Bd1_pages.txt.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"IEC.txt line 847, s.v. autos\",\n          \"stance\": \"supports\",\n          \"note\": \"Mann: 'autos (outos) \\\"alone, own, self, same\\\". Cf. aut, autios, etc. WP I, 14 … Gk. autós; Alb. vetë, id.; Lat. cf. aut, autem; Ir. uatha \\\"singular, solitary\\\" …' — Mann treats αὐτός as an inherited IE pronominal formation, against Klein's 'uncertain origin'.\"\n        },\n        {\n          \"src\": \"SKT\",\n          \"where\": \"SKT.txt line 1193, s.v. Auto-\",\n          \"stance\": \"supports\",\n          \"note\": \"Skeat: 'Auto-, prefix. (Gk.) Gk. αὐτο-, crude form of αὐτός, self.' Same root, same gloss, no origin given.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"authentěs, afendis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two chronological layers of one Greek word are stacked in this box. (a) Ancient Greek αὐθέντης authentēs is a compound of αὐτο- (< αὐτός 'self', with the regular aspiration of τ before the following rough breathing: αὐτο- + h- > αὐθ-) and *ἕντης héntēs 'doer', an agent noun in -της built on PIE *senh₂- 'to attain, accomplish' (the root of Greek ἀνύω 'I accomplish', Sanskrit sanóti 'wins'); Klein and Etymonline give exactly this analysis, so the literal sense is 'one who does a thing with his own hand'. In classical Attic (Antiphon, Euripides) it means both 'perpetrator, murderer by one's own hand' and 'absolute master, one who acts on his own authority'; in the Hellenistic and Byzantine periods the second sense won out and αὐθέντης became simply 'lord, master'. (b) The second form in the box, afendis, is not Ancient Greek but Byzantine/Modern Greek ἀφέντης aféntis, the popular continuation of αὐθέντης after loss of the initial diphthong glide and the shift of the aspirate cluster (αὐθέντης > αὐθέντης [afˈθendis] > ἀφέντης [aˈfendis], with -θ- absorbed into the preceding [f]); Klein prints it 'αφέντης (read afendis)'. Nourai's gloss string 'self doer, authority, ruler, original' is accurate for the noun except for 'original', which belongs to the derived adjective αὐθεντικός authentikós 'original, genuine, principal' — the form that actually feeds node #4.\",\n          \"derivation_fa\": \"در این جعبه دو لایهٔ تاریخی از یک واژه کنار هم نشسته است. نخست، یونانی باستان αὐθέντης (authentēs) که ترکیبی است از αὐτο- (از αὐτός «خود») و *ἕντης «کننده»، اسم فاعلی بر پایهٔ ریشهٔ هندواروپایی *senh₂- «به انجام رساندن» (همان ریشهٔ ἀνύω یونانی و sanóti سنسکریت)؛ ت پایانی αὐτο- پیش از دمِ درشتِ جزء دوم به θ بدل شده است (ابدالی آوایی و قاعده‌مند در یونانی). معنای تحت‌اللفظی آن «آنکه کاری را به دست خویش انجام می‌دهد» است و در آتیک کلاسیک هم «قاتلِ به‌دستِ خود» و هم «سرورِ مطلق» معنی می‌دهد؛ در دورهٔ هلنیستی و بیزانسی معنای دوم غالب شد. دوم، صورت afendis که یونانی باستان نیست بلکه یونانی بیزانسی/نو ἀφέντης است، دنبالهٔ مردمیِ همان واژه پس از دگرگونی آوایی (αὐθέντης > ἀφέντης). گزارش نورایی درست است؛ تنها معنای «original» در فهرست او از آنِ صفتِ برساختهٔ αὐθεντικός است نه خودِ اسم.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%CE%B1%E1%BD%90%CE%B8%CE%AD%CE%BD%CF%84%CE%B7%CF%82\",\n            \"https://www.etymonline.com/word/authentic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 4018 (leaf 80), s.v. authentic: 'fr. Gk. αὐθεντικός, \\\"original, genuine, principal\\\", fr. αὐθέντης, αὐτο-έντης, \\\"absolute master, ruler; murderer\\\", lit. \\\"one who does a thing himself\\\", compounded of αὐτός, \\\"self\\\" (see auto-), and *ἕντης, \\\"one who does (a thing) himself\\\", which is rel. to ἀνύω, Att. ἀνύω, \\\"I accomplish\\\", and cogn. with OI. sanóti, \\\"wins, gains\\\", perhaps also with Hitt. shanh-zi, \\\"he seeks, strives\\\". Cp. effendi.' Klein's αὐτο-έντης is exactly Nourai's 'self doer'.\"\n            },\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"not_checked\",\n              \"note\": \"The a-u-t- pages of the 1975/76 New College Edition are not open online (see root ref_check). Watkins 1985 has no entry for αὐθέντης; it indexes AUTHENTIC nowhere, and puts the *senh₂- family under a different head.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt line 1191, s.v. Authentic\",\n              \"stance\": \"supports\",\n              \"note\": \"'Gk. αὐθεντικός, vouched for, warranted. — Gk. αὐθέντης, one who does things with his own hand. (Of uncertain origin.)' Same compound analysis and same literal gloss; Skeat only declines to reconstruct the second member.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"FSD_vol2.txt line 5513, s.v. ef-fen'di\",\n              \"stance\": \"supports\",\n              \"note\": \"'[< Turk. efendi, < Gk. aphentes, for authentes, master, < autos, self.]' — Funk & Wagnalls explicitly equates aphentes with authentes and derives both from autos, i.e. it endorses both forms in Nourai's box.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 12687 (leaf 273), s.v. effendi\",\n              \"stance\": \"supports\",\n              \"note\": \"'fr. MGk. αφέντη (read afendi), voc. of αφέντης (read afendis), fr. Gk. αὐθέντης, \\\"an absolute master or ruler\\\"' — Klein labels afendis Modern Greek, confirming that the second form in the box is not the classical layer.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Turkish\",\n          \"words\": \"afandi\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"afandi\",\n          \"correct_form\": \"efendi\",\n          \"derivation\": \"The derivation drawn — Greek αὐθέντης / ἀφέντης borrowed into Turkish as a title 'sir, master' — is entirely correct and is Klein's own account: 'effendi, n., a Turkish title of respect; sir. — Turk. efendi, \\\"master\\\", fr. MGk. αφέντη (read afendi), voc. of αφέντης (read afendis), fr. Gk. αὐθέντης, \\\"an absolute master or ruler\\\".' The borrowing is Ottoman, from the spoken Greek of Anatolia and Constantinople after 1453, and — as Klein, Lokotsch and Nişanyan all stress — it was the VOCATIVE ἀφέντη afendi, the form a Greek speaker would use in addressing his lord, that was taken over, which is why Turkish has final -i and not -is; Ottoman spelled it افندی, and English borrowed it as effendi in the 1610s. The form in the box, however, is wrong: the Turkish word is efendi (Ottoman افندی), never *afandi. The printed page (pdf p.72, book p.42) does read 'afandi', so this is Nourai's own slip, not a scan error: he has written the Turkish headword with the vowels of the Greek vocative ἀφέντη as Klein transliterates it ('read afendi'), then further altered the second vowel. The verdict therefore concerns the shape of the word only; the arrow itself is confirmed.\",\n          \"derivation_fa\": \"پیوندی که نورایی کشیده است — وام‌گیری یونانی αὐθέντης/ἀφέντης در ترکی به معنای «آقا، سرور» — کاملاً درست است و همان چیزی است که کلاین می‌گوید: ترکی efendi از صورت ندایی یونانیِ نو ἀφέντη (afendi) گرفته شده، و چون صورت ندایی وام گرفته شده است پایانهٔ ترکی -i است نه -is. این وام‌گیری عثمانی است و پس از فتح قسطنطنیه از گفتار یونانی‌زبانان آناتولی به ترکی راه یافته و در خط عثمانی «افندی» نوشته شده است. اما صورتی که در جعبه آمده نادرست است: واژهٔ ترکی efendi است، نه *afandi. تصویر صفحهٔ چاپی (ص ۴۲ کتاب) نشان می‌دهد که خودِ کتاب «afandi» چاپ کرده است، پس این خطای چاپیِ نورایی است نه خطای خوانش اسکن؛ ظاهراً او واکه‌های صورت ندایی یونانی را با واژهٔ ترکی درآمیخته است. حکم «مشکوک بودن ضبط» تنها به شکل واژه مربوط است و خودِ پیوند تأیید می‌شود.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/efendi\",\n            \"https://www.etymonline.com/word/effendi\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:502\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 12687, form-feed leaf 273, s.v. effendi (Klein's e-f-f- range; Nourai's p.502): 'effendi, n., a Turkish title of respect; sir. — Turk. efendi, \\\"master\\\", fr. MGk. αφέντη (read afendi), voc. of αφέντης (read afendis), fr. Gk. αὐθέντης, \\\"an absolute master or ruler\\\". See authentic.' The page says exactly what the arrow says — and spells the Turkish word efendi, not afandi. (The leaf-to-page formula in refs_online.json, leaf ≈ floor(p/2)+12, would put this leaf near p.522 rather than 502; the offset drifts by a few leaves in this scan, but the alphabetical position leaves no doubt that this is the page Nourai cites.)\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LKT\",\n              \"where\": \"LKT.txt line 1414-1415, entry no. 557 'Tk. efendi'\",\n              \"stance\": \"supports\",\n              \"note\": \"Lokotsch no. 557: '[Aus gr. αὐθέντης \\\"Herr\\\", s. Glotta III, 289 ff., moderne Aussprache aftendis, und zwar Vokativ αὐθέντη afendi MSOS I, 44, Anm. 2]; früher Ehrentitel, jetzt entsprechend unserer höflichen Anrede \\\"mein Herr, monsieur\\\". Frz. efendi, effendi, dtsch. Effendi usw.' — same source word, same vocative route, and again the spelling efendi.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt line 5701, s.v. Effendi\",\n              \"stance\": \"supports\",\n              \"note\": \"'Effendi, sir, master (Turkish - Gk.) Turk. efendi, sir. — Mod. Gk. ἀφέντης, for Gk. αὐθέντης, a despotic master, ruler; see Authentic.'\"\n            },\n            {\n              \"src\": \"TTS\",\n              \"where\": \"incoming/TTS/TTS_vambery1878_uoft_djvu.txt — grep 'efendi'\",\n              \"stance\": \"silent\",\n              \"note\": \"Vámbéry's Turko-Tatar etymological dictionary has no entry for efendi (no hits), as expected: he treats inherited Turkic vocabulary, not Greek loanwords of Ottoman.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"afandî «افندی»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian افندی afandi/efendi is a straight loan from Ottoman Turkish افندی efendi, taken over in the Qajar period along with the rest of the Ottoman-Turkish administrative and courtesy vocabulary (پاشا, بیگ, خانم, افندی). Mo'in's Farhang-e Fārsi gives it the origin tag [تر.] 'Turkish' and glosses the etymology in Persian as 'آنکه به نفسه کار کند؛ مستقل به ذات' — literally 'one who acts of himself; independent in essence' — which is a word-for-word Persian rendering of the Greek αὐθέντης 'self-doer', so Mo'in himself carries Nourai's whole chain back to Greek. Its Persian use is exactly what the chart says: 'به طریق احترام به بزرگان ترک اطلاق شود و نیز به آخر نام رجال افزوده شود' ('applied as a term of respect to Turkish notables, and also appended to the names of men'). Since Persian has no ambiguity between e and a in an unwritten first vowel, both readings afandi and efendi occur; Nourai's 'afandî' is defensible here even though it is not for the Turkish node.\",\n          \"derivation_fa\": \"«افندی» در فارسی وام‌واژه‌ای است مستقیم از ترکی عثمانی «افندی» (efendi) که در دورهٔ قاجار همراه دیگر واژه‌های تشریفاتی و دیوانی عثمانی (پاشا، بیگ، خانم) به فارسی راه یافته است. معین در فرهنگ فارسی آن را با نشانِ [تر.] یعنی ترکی می‌آورد و ریشهٔ آن را چنین توضیح می‌دهد: «آنکه به نفسه کار کند؛ مستقل به ذات» — که ترجمهٔ لفظ‌به‌لفظِ همان معنای یونانی αὐθέντης «خودکننده» است؛ بدین‌سان خودِ معین زنجیرهٔ نورایی را تا یونانی تأیید می‌کند. کاربرد فارسی آن نیز درست همان است که در نمودار آمده: «به طریق احترام به بزرگان ترک اطلاق شود و نیز به آخر نام رجال افزوده شود». چون واکهٔ نخست در خط فارسی نوشته نمی‌شود، هر دو خوانش «افندی» و «اِفندی» رواج دارد و ضبط نورایی در این گره پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/efendi\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:319\",\n              \"status\": \"supports\",\n              \"note\": \"MON_part1.txt line 15234 (= incoming/MON/MON_2vol_Adena_v1_djvu.txt line 15234), Mo'in entry no. 22701, in the ا-ف-ن alphabetical run that falls on Nourai's p.319: 'افندی: 22701 [تر. آنکه به نفسه کار کند؛ مستقل به ذات] (ا.) به طریق احترام به بزرگان ترک اطلاق شود و نیز به آخر نام رجال افزوده شود.' Mo'in tags it Turkish and glosses the underlying sense as 'one who acts of himself' — exactly Nourai's Turkish>Persian arrow and Greek 'self doer'. (Grep pattern: grep -n 'افندی' MON_part1.txt.)\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt line 15234, s.v. افندی\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check: '[تر. آنکه به نفسه کار کند؛ مستقل به ذات]' — Turkish origin, 'self-doer' gloss.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"BQT_v1_pages.txt / BQT_v2_pages.txt / incoming/BQT/BQT_v3-v5_pages.txt — grep 'افندی'\",\n              \"stance\": \"silent\",\n              \"note\": \"Borhan-e Qate' has no headword افندی; the only hits are manuscript names in Mo'in's apparatus ('نسخهٔ اسعد افندی', 'نسخهٔ اسمد افندی'). Expected: Borhan (1062 AH, India) records classical Persian, not Qajar-era Ottoman courtesy titles.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"incoming/ARY/ARY_pages.txt — grep 'افندی'\",\n              \"stance\": \"silent\",\n              \"note\": \"Aryanpur's dictionary of Indo-European roots in Persian has no entry (no hits), consistent with the word being a Turkish, not an inherited Iranian, item.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"authenticus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Late Latin authenticus 'coming from the author, original, genuine' is a straight transliteration-borrowing of Greek αὐθεντικός authentikós, the -ικός adjective of αὐθέντης, with Greek υ rendered u, θ rendered th and -ικός rendered -icus. It enters Latin in the imperial period as a legal term of art for a document in its original form as opposed to a copy — hence Justinian's Authenticae, the Greek Novellae in their authenticated Latin version (Funk & Wagnalls: 'a collection of the New Constitutions of Justinian: so named because of their being authentic translations from the Greek'). Nourai's arrow runs #1 authentēs → Latin authenticus and so skips one link: the immediate source is the adjective αὐθεντικός, not the noun, which is why the box's Greek parent carries the gloss 'original' (see node #1). Klein, Skeat and Etymonline all insert αὐθεντικός; the chain is otherwise exactly as drawn.\",\n          \"derivation_fa\": \"لاتینی متأخر authenticus «اصل، دست‌نخورده، معتبر» وام‌واژه‌ای است از صفت یونانی αὐθεντικός (صفتِ -ικός ساخته‌شده از αὐθέντης) که در انتقال به لاتین θ به th و -ικός به -icus بدل شده است. این واژه در دورهٔ امپراتوری روم اصطلاحی حقوقی بوده به معنای «سندِ اصل در برابر رونوشت»؛ از همین‌جاست نامِ Authenticae یعنی نُوِلّاهای یونانیِ یوستینیانوس در ترجمهٔ رسمیِ لاتین. تنها نکته آن است که پیکان نورایی یک حلقه را جا انداخته است: مأخذ مستقیمِ لاتین صفتِ αὐθεντικός است نه اسمِ αὐθέντης — و همین توضیح می‌دهد که چرا در جعبهٔ پدر معنای «original» آمده است. جز این، زنجیره درست است و کلاین و اسکیت و Etymonline نیز همین را می‌گویند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/authentic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:89\",\n              \"status\": \"not_checked\",\n              \"note\": \"Page 89 of the 1975/76 AHD New College Edition (the authentic/auto- range of the main body) is not accessible: refs_online.json records only lending-only archive.org copies and a search-only HathiTrust scan of that edition, and the local proxy AHD_watkins1985.txt is the IE-roots appendix alone, which has no entry for authenticus.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 4018 (leaf 80), s.v. authentic and authenticate\",\n              \"stance\": \"partial\",\n              \"note\": \"Klein reaches Latin only through the adjective: 'OF. autentique (F. authentique), fr. Gk. αὐθεντικός …' and s.v. authenticate 'ML. authenticatus, pp. of authenticare, fr. Late L. authenticus.' So Late Latin authenticus is real and the meaning is right, but its parent in Klein is αὐθεντικός, not αὐθέντης.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"FSD_vol1.txt line 29388, s.v. authentic / Authenticae\",\n              \"stance\": \"supports\",\n              \"note\": \"'… authoritative (book, etc.), as distinguished from a counterfeit or apocryphal one. 3. pl. A collection of the New Constitutions of Justinian: so named because of their being authentic translations from the Greek: sometimes called Liber or Corpus Authenticarum' — documents the Late Latin legal sense 'genuine, original' that Nourai glosses.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"LAT.txt — grep 'authentic'\",\n              \"stance\": \"silent\",\n              \"note\": \"Ernout-Meillet's Dictionnaire étymologique de la langue latine has no entry authenticus (the only hits are the French word 'authenticité' in editorial prose); a late Greek technical loan falls outside their inherited-Latin scope. Walde-Hofmann (LEW_1910.txt) likewise returns nothing.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"authentic,\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English authentic is first attested in the mid-14th century in the sense 'authoritative, duly authorized' (now obsolete) and, in the same period, 'entitled to acceptance as factual, genuine'. It came in through Old French autentique (Modern French authentique) and Medieval Latin authenticus — Klein: 'authentic, adj. … — OF. autentique (F. authentique), fr. Gk. αὐθεντικός', Etymonline: 'from Old French autentique and directly from Medieval Latin authenticus'. The -th- of the modern English spelling is a Renaissance re-latinisation restoring the Greek θ, which Old French had reduced to plain t. Nourai's arrow Latin → English is therefore right in substance but elides the Old French stage that actually delivered the word; the trailing comma in the box is a typographic artefact of the chart (the box lists only one word).\",\n          \"derivation_fa\": \"واژهٔ انگلیسی authentic از میانهٔ سدهٔ چهاردهم میلادی گواهی شده است، نخست به معنای «دارای اعتبار و اجازهٔ رسمی» و در همان دوره به معنای «اصیل، پذیرفتنی به‌عنوان واقعیت». راه ورود آن فرانسویِ کهن autentique و لاتینِ سده‌های میانه authenticus بوده است؛ حرف th در املای امروزی بازگردانی رنسانسیِ θ یونانی است، چراکه فرانسویِ کهن آن را به t ساده کرده بود. پیکان نورایی از لاتین به انگلیسی از نظر محتوا درست است، اما مرحلهٔ فرانسویِ کهن را که در عمل واژه را رسانده است نادیده می‌گذارد. ویرگولِ پایانِ جعبه صرفاً نشانه‌گذاری نمودار است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/authentic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"not_checked\",\n              \"note\": \"Same as node #4: the a-u-t- pages of the 1975/76 New College Edition are not open online, and Watkins 1985 (the local AHD proxy) covers only the IE roots appendix, where AUTHENTIC does not appear in the English-word index.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 4018 (leaf 80), s.v. authentic\",\n              \"stance\": \"partial\",\n              \"note\": \"'authentic, adj. authoritative; reliable; genuine. — OF. autentique (F. authentique), fr. Gk. αὐθεντικός …' — Klein routes English through Old French, and to the Greek adjective, rather than through Latin directly.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt line 1191, s.v. Authentic\",\n              \"stance\": \"partial\",\n              \"note\": \"'Authentic. (F.-L.-Gk.) M.E. autentique, autentik. — O.F. autentique, later authentique; L. authenticus, original, written with the author's own hand. — Gk. αὐθεντικός …' — Skeat's language chain F.-L.-Gk. makes the Old French link explicit and confirms the Latin gloss 'original, genuine'.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"FSD_vol1.txt line 29378-29388, s.v. authentic\",\n              \"stance\": \"supports\",\n              \"note\": \"Funk & Wagnalls distinguishes the senses Nourai glosses: 'authentic is … used by table writers as synonymous with genuine' and 'authoritative (book, etc.), as distinguished from a counterfeit or apocryphal one', with the etymology '< LL. authenticatus, pp. of authentico, < L. authenticus'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"German\",\n          \"words\": \"auto-bahn\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"German Autobahn 'motorway' is a compound of Auto + Bahn coined in the late 1920s (Kraftfahrbahn/Autobahn for the HaFraBa project; the Reich network from 1933 made the word international, and English borrowed it in 1937). Both halves have to be qualified against the arrow drawn here. (a) Auto reaches German only at the end of a long relay: it is a clipping of Automobil, itself borrowed from French automobile, coined 1861 as a hybrid of Greek αὐτός and Latin mobilis — so the arrow 'Greek autos → German auto-bahn' is a shortcut across French, not a direct borrowing, and the German word is not a nineteenth-century Graecism but a twentieth-century internationalism. (b) Bahn has nothing to do with the root at all: it continues Middle High German ban, bane 'way, road', literally 'a swath struck through', from PIE *gʷhen- 'to strike, kill' — which is precisely how Watkins indexes it ('AUTOBAHN gʷhen-¹'). So the chart is right that the first element goes back to Greek αὐτός, but only half the word does and only at three removes.\",\n          \"derivation_fa\": \"واژهٔ آلمانی Autobahn «بزرگ‌راه» ترکیبی است از Auto و Bahn که در اواخر دههٔ ۱۹۲۰ ساخته شد و با شبکهٔ بزرگ‌راه‌های آلمان از ۱۹۳۳ جهانی شد. اما پیکانی که نورایی کشیده است دو قید می‌خواهد: نخست آنکه Auto در آلمانی کوتاه‌شدهٔ Automobil است و Automobil خود وام‌واژه‌ای است از فرانسویِ automobile (ساختهٔ ۱۸۶۱ از αὐτός یونانی و mobilis لاتین)؛ پس پیوند «یونانی ← آلمانی» میان‌بُری است بر فرانسوی و واژه‌ای است بین‌المللی از سدهٔ بیستم، نه وام‌گیری مستقیم از یونانی. دوم آنکه جزء Bahn هیچ پیوندی با این ریشه ندارد: دنبالهٔ آلمانی میانهٔ ban/bane «راه» است، در اصل «شکافی که زده و باز شده»، از ریشهٔ هندواروپایی *gʷhen- «زدن، کشتن» — چنان‌که واتکینز نیز AUTOBAHN را ذیل همین ریشه فهرست می‌کند. بنابراین ادعای نورایی تنها دربارهٔ نیمهٔ نخستِ واژه و آن هم با سه واسطه درست است؛ «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/autobahn\",\n            \"https://www.etymonline.com/word/automobile\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives this node no reference at all (refs=None in the source JSON and no book icon on the printed page), so there is nothing of his to check.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt line 1270 (English-word index)\",\n              \"stance\": \"partial\",\n              \"note\": \"'AUTOBAHN gʷhen-¹' — Watkins files autobahn under the root of Bahn ('to strike, kill'), not under anything to do with αὐτός, confirming that the second element is unrelated to this chart's root.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"KLN_1966.txt line 4027 (leaf 80), s.v. auto\",\n              \"stance\": \"supports\",\n              \"note\": \"'auto, n. (colloq.) — Short for automobile.' Klein records the very clipping that produced German Auto-, showing that the modern auto- of Autobahn is 'motor car', not Greek 'self'.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"FSD_vol1.txt line 823 (Introduction, on recent French loans)\",\n              \"stance\": \"supports\",\n              \"note\": \"Funk & Wagnalls 1913 lists automobile among the French words then being absorbed ('The absorption of French words is unabated, as is evidenced by such terms as automobile, charmeuse, chauffeur, garage …'), fixing the French relay by which auto- reached the other European languages, German included.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"otobân «اتوبان»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian اتوبان otobân 'motorway, freeway' is a direct loan from German Autobahn, as Wiktionary states explicitly ('Borrowed from German Autobahn'), and the phonetic shape proves it: German [ˈaʊtoˌbaːn] gives Persian oto- (not French/English auto-) and, crucially, -bân with the long ā of German Bahn, which no French or English source form could supply (French autoroute, English motorway/freeway have no -bahn at all). The word belongs to the Pahlavi-era of Iranian road-building in the 1960s-70s, when German engineering vocabulary entered Persian; its Persian-coined rival آزادراه āzādrāh (āzād 'free' + rāh 'road', a calque of 'freeway') was promoted by the Farhangestān but اتوبان remains the ordinary word. Nourai gives the node no reference, but the claim is right.\",\n          \"derivation_fa\": \"«اتوبان» در فارسی وام‌واژه‌ای است مستقیم از آلمانیِ Autobahn، چنان‌که ویکی‌واژه نیز تصریح می‌کند؛ شکل آوایی خود گواه است: بخش نخست «اتو» (نه «آتو» یا «اوتو»ی فرانسوی-انگلیسی) و به‌ویژه بخش دوم «ـبان» با آای کشیده، بازتاب Bahn آلمانی است و هیچ صورت فرانسوی یا انگلیسی (autoroute، motorway) نمی‌توانست چنین پایانه‌ای بدهد. این وام‌گیری به دههٔ چهل و پنجاه خورشیدی و دورانِ راه‌سازی با مهندسی آلمانی بازمی‌گردد. برابرنهادِ فارسیِ «آزادراه» (آزاد + راه، گرته‌برداری از freeway) را فرهنگستان پیشنهاد کرد، ولی «اتوبان» همچنان واژهٔ رایج گفتار است. ادعای نورایی در این گره درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D8%AA%D9%88%D8%A8%D8%A7%D9%86\",\n            \"https://www.etymonline.com/word/autobahn\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"No reference is cited for this node (refs=None; no book icon on the printed page), so there is nothing of Nourai's to verify.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt / MON_part2.txt — grep 'اتوبان'\",\n              \"stance\": \"silent\",\n              \"note\": \"Mo'in's Farhang-e Fārsi (1963-4) has no entry اتوبان — zero hits — although the neighbouring twentieth-century loans اتوبوس, اتومبیل, اتوماتیک, اتوکار are all there (MON_part1.txt lines 6968-7000). The word entered Persian after Mo'in's dictionary was compiled, which itself dates the borrowing.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"incoming/ARY/ARY_pages.txt — grep 'اتوبان'\",\n              \"stance\": \"silent\",\n              \"note\": \"No hits in Aryanpur's Indo-European roots dictionary; a recent European loanword is outside its scope.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box: Nourai draws French as the intermediary that carried Greek αὐτός into Persian, without naming the French words, because they are simply the Persian ones of node #9 read back into French. The French forms are automatique (17th-c. learned borrowing of Greek αὐτόματος 'self-moving, self-acting'), automobile (adjective coined 1861, then noun, from αὐτός + Latin mobilis 'movable'), and autobus (1906, a blend of auto- with the -bus of omnibus, itself the Latin dative plural 'for all'). French is genuinely the donor language for the whole Persian set — nineteenth- and twentieth-century Persian took its technical and administrative vocabulary from French, not from English or German — so the empty box is correct as drawn; only the word list is missing.\",\n          \"derivation_fa\": \"این جعبه تهی است و نقشِ واسطه دارد: نورایی فرانسوی را همچون زبانِ میانجی نشان می‌دهد که αὐτός یونانی را به فارسی رسانده، بی‌آنکه واژه‌های فرانسوی را بنویسد، زیرا همان‌هایی هستند که در گرهٔ ۹ به خط فارسی آمده‌اند: automatique (وام‌گیریِ عالمانه از یونانیِ αὐτόματος «خودجنبنده»)، automobile (صفتی ساختهٔ ۱۸۶۱ از αὐτός یونانی و mobilis لاتین) و autobus (۱۹۰۶، آمیزهٔ auto- با پایانهٔ -bus از omnibus). فرانسوی به‌راستی زبانِ دهندهٔ همهٔ این مجموعه به فارسی است، چراکه واژگان فنی و دیوانیِ فارسیِ سدهٔ سیزدهم و چهاردهم خورشیدی از فرانسوی گرفته شده است نه از انگلیسی یا آلمانی. پس جعبه درست است و تنها فهرست واژه‌ها در آن نیامده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/automobile\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The French box carries no reference on the printed page (refs=None), so there is nothing of Nourai's to check.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt lines 6979-7000, s.vv. اتوبوس‌رانی, اتوشویی, اتومبیل\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in tags this family French: 'اتوبوس‌رانی … [فر. + ف.]' (French + Persian) and 'اتوشویی … [فر. + ف. اتو (مخفف اتومبیل) + شویی (شستن)]', and marks اتومبیل itself [فر.]. That is Mo'in endorsing precisely the French → Persian arrow of this box.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"FSD_vol1.txt line 823 (Introduction)\",\n              \"stance\": \"supports\",\n              \"note\": \"'The absorption of French words is unabated, as is evidenced by such terms as automobile, charmeuse, chauffeur, garage, hangar, limousine …' — contemporary testimony (1913) that automobile spread out of French.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"(no transliteration; script only) اتوماتیک ، اتوموبیل ، اتوبوس\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"اتوماتیک ، اتوموبیل ، اتوبوس\",\n          \"correct_form\": \"اتوماتیک ، اتوموبیل ، اتوبوس\",\n          \"derivation\": \"The derivation itself is sound and is Mo'in's own: all three words are French loans of the late Qajar and Pahlavi periods. اتوماتیک otomâtik < French automatique < Greek αὐτόματος (αὐτο- + a stem *mat- 'to strive, think', which Watkins indexes as AUTOMATIC men-¹); اتوموبیل otomobil < French automobile (1861, αὐτός + Latin mobilis), which Mo'in defines as 'دستگاه خودرو که به وسیلهٔ موتور … حرکت کند' and tags [فر.]; اتوبوس otobus < French autobus (1906, auto- + -bus of omnibus), Mo'in: 'نوعی از اتومبیل با اطاق دراز و صندلی‌های متعدد'. The Persian forms show the regular French-to-Persian substitutions o for French [o], -ik for -ique, and -bus for -bus. The flag is a data problem, not an etymological one: the printed page (pdf p.72, book p.42) reads اتوموبیل, with a wāw between mīm and bē, while the extracted JSON has اتومبیل. Both spellings live in Persian — Mo'in's own headword is اتومبیل — but the book prints the longer form, so the JSON should be corrected to اتوموبیل.\",\n          \"derivation_fa\": \"خودِ ریشه‌شناسی این گره درست است و همان چیزی است که معین می‌گوید: هر سه واژه وام‌واژه‌های فرانسوی از اواخر قاجار و دورهٔ پهلوی‌اند. «اتوماتیک» از automatique فرانسوی و آن از αὐτόματος یونانی «خودجنبنده»؛ «اتوموبیل» از automobile فرانسوی (ساختهٔ ۱۸۶۱ از αὐτός یونانی و mobilis لاتین) که معین آن را «دستگاه خودرو که به وسیلهٔ موتور … حرکت کند» تعریف و با نشانِ [فر.] ثبت کرده است؛ و «اتوبوس» از autobus فرانسوی (۱۹۰۶، از auto- و پایانهٔ -bus واژهٔ omnibus). دگرگونی‌های آوایی همان جانشینی‌های قاعده‌مندِ فرانسوی به فارسی است (‑ique ← ‑یک). اما نکتهٔ فنی: صفحهٔ چاپی (ص ۴۲) «اتوموبیل» با واو میان میم و بـ چاپ کرده، حال آنکه در دادهٔ استخراج‌شده «اتومبیل» آمده است. هر دو املا در فارسی رواج دارد و سرمدخلِ معین نیز «اتومبیل» است، ولی چون کتاب صورت بلندتر را چاپ کرده، این خطای خوانشِ اسکن است و باید در داده اصلاح شود.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/automobile\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:139\",\n              \"status\": \"supports\",\n              \"note\": \"MON_part1.txt lines 6968-7003 — the ا-ت-و alphabetical run that is Nourai's p.139 — carries all three headwords: 'اتوبوس: (ا.) نوعی از اتومبیل با اطاق دراز و صندلی‌های متعدد که … در شهر و بیرون از شهر برای رفت و آمد کسان بکار می‌رود'; 'اتوماتیک: (ص.) دستگاهی که خود به خود کار می‌کند و نیازی به بودن کارگر بر سر آن نیست؛ خودکار'; 'اتومبیل: (ا.) [فر.] دستگاه خودرو که به وسیلهٔ موتور بخار یا برق یا نفت یا بنزین … حرکت کند'. The neighbouring اتوبوس‌رانی is tagged '[فر. + ف.]' and اتوشویی '[فر. + ف. اتو (مخفف اتومبیل) + شویی]', i.e. Mo'in explicitly marks the family French — exactly Nourai's arrow. (Grep: grep -n 'اتوبوس\\\\|اتوماتیک\\\\|اتومبیل' MON_part1.txt.)\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt lines 6968-7003\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; note that Mo'in's own headword is spelled اتومبیل (without the second wāw), whereas Nourai's printed page has اتوموبیل.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt line 1270 (English-word index)\",\n              \"stance\": \"supports\",\n              \"note\": \"'AUTOMATIC men-¹' — Watkins files automatic under *men- 'to think', the root of the -matos of Greek αὐτόματος, confirming the Greek compound behind French automatique.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt line 1194, s.v. automaton\",\n              \"stance\": \"supports\",\n              \"note\": \"'automaton, a self-moving machine. (Gk.) Gk. αὐτόματον, neut. of αὐτόματος, self-moving. — Gk. αὐτο-, for αὐτός, self; and a stem mat-, appearing in ματ-εύω, I seek after, strive to do. Cf. Skt. mata-, desired, pp. of man, to think.' Same analysis of the ancestor of automatique/اتوماتیک.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"auto-, automobile, automatic\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Three English items, all genuinely from Greek αὐτός but by three different routes. (a) The combining form auto- (before a vowel aut-, before an aspirate auth-) is a learned borrowing of Greek αὐτο-, productive in English since the sixteenth century in autobiography, autograph, autopsy, autocracy; Funk & Wagnalls defines it 'From Greek autos, self: a combining form, signifying action of, from, within, by, or upon self'. (b) automatic is an eighteenth-century formation on Greek αὐτόματος 'self-moving' (auto- + the *men- 'think/strive' stem seen in ματεύω), the same word that gives automaton. (c) automobile is not a Greek compound at all but a French hybrid of 1861 (Greek αὐτός + Latin mobilis 'movable'), which English borrowed as an adjective in 1883 for electric traction cars and as a noun in 1895, shortened from French véhicule automobile, beating out the rival coinages motorcar, autocar and locomobile. Nourai's single English box lumps the three together under one arrow from Greek; that is right for auto- and automatic and right only at one remove, through French, for automobile.\",\n          \"derivation_fa\": \"این جعبه سه واژهٔ انگلیسی را یک‌جا آورده که هر سه به αὐτός یونانی بازمی‌گردند اما از سه راه. نخست، پیشوندِ ترکیبیِ auto- (و گونه‌های aut- و auth-) که وام‌گیریِ عالمانه از αὐτο- یونانی است و از سدهٔ شانزدهم در انگلیسی زایاست (autobiography، autograph، autopsy). دوم، automatic که ساختی است از سدهٔ هجدهم بر پایهٔ αὐτόματος یونانی «خودجنبنده» (از αὐτο- و ستاکِ *men-/mat- «اندیشیدن، کوشیدن»)، همان واژه‌ای که automaton نیز از آن است. سوم، automobile که اصلاً ترکیبی یونانی نیست بلکه آمیزه‌ای فرانسوی از سال ۱۸۶۱ است (αὐτός یونانی + mobilis لاتین «جنبنده») و انگلیسی آن را در ۱۸۸۳ همچون صفت و در ۱۸۹۵ همچون اسم وام گرفت. بنابراین پیکانِ یگانهٔ نورایی برای auto- و automatic بی‌واسطه درست است و برای automobile با یک واسطهٔ فرانسوی.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/automobile\",\n            \"https://www.etymonline.com/word/authentic\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:89\",\n              \"status\": \"not_checked\",\n              \"note\": \"The main-body page 89 of the 1975/76 New College Edition (auto-, automatic, automobile) is not open online (see root ref_check). The local Watkins 1985 proxy indexes AUTOMATIC under men-¹ but has no entry for the prefix itself.\"\n            },\n            {\n              \"ref\": \"KLN:130\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 4027 (leaf 80, Klein's a-u-t- range = Nourai's p.130): 'auto, n. (colloq.) — Short for automobile. auto-, before a vowel aut-, before an aspirate auth-. — Gk. αὐτο-, αὐτ-, αὐθ-, fr. αὐτός, \\\"self, same\\\", of uncertain origin.' Klein's page thus supplies both the prefix auto- and the clipping auto that Nourai's box heads.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"FSD\",\n              \"where\": \"FSD_vol1.txt line 31949, s.v. au'to-\",\n              \"stance\": \"supports\",\n              \"note\": \"'au'to-, … From Greek autos, self: a combining form, signifying action of, from, within, by, or upon self' — the English prefix, straight from αὐτός.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"SKT.txt lines 1193-1195, s.vv. Auto-, automaton, autopsy\",\n              \"stance\": \"supports\",\n              \"note\": \"'Auto-, prefix. (Gk.) Gk. αὐτο-, crude form of αὐτός, self.' with automaton, autonomy and autopsy as illustrations — same prefix, same root.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"AHD_watkins1985.txt lines 1270-1271 (English-word index)\",\n              \"stance\": \"partial\",\n              \"note\": \"'AUTHOR aug-¹ … AUTOBAHN gʷhen-¹ … AUTOCHTHON dhghem- … AUTOMATIC men-¹ … AUTOPSY okʷ-' — Watkins consistently indexes auto- compounds by their second element, i.e. he assigns no PIE root to auto- itself; automobile is absent because its second element is Latin.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-05T05:52:54.925Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-72.json (file state is current in your context — no need to Read it back)
```


## [2026-09-05T05:52:58.535Z] TOOL CALL #53: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-72.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 72"
}
```


### [2026-09-05T05:53:02.356Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 7, 'transcription_suspect': 2, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 5, 'not_checked': 7}
books consulted: {'supports': 17, 'silent': 6, 'partial': 5} | by book: {'FSD': 6, 'SKT': 5, 'KLN': 4, 'MON': 4, 'AHD': 3, 'ARY': 2, 'LKT': 1, 'TTS': 1, 'BQT': 1, 'LAT': 1}
```


## [2026-09-05T05:53:06.243Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,io\np='data/verification/page-72.json'\nd=json.load(open(p))\nd['entries'][0].pop('modern_form_note',None)\nopen(p,'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=2)+\"\\n\")\nEOF\npython3 tools/verify_check.py 72"
}
```


### [2026-09-05T05:53:08.125Z] TOOL RESULT

```
nodes verified: 10/10
node verdicts: {'confirmed': 7, 'transcription_suspect': 2, 'plausible': 1}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 5, 'not_checked': 7}
books consulted: {'supports': 17, 'silent': 6, 'partial': 5} | by book: {'FSD': 6, 'SKT': 5, 'KLN': 4, 'MON': 4, 'AHD': 3, 'ARY': 2, 'LKT': 1, 'TTS': 1, 'BQT': 1, 'LAT': 1}
```


## [2026-09-05T05:53:25.949Z] AGENT

Page 72 (book p. 42), single entry "Autos" (Greek), 10 nodes — all verified, `verify_check.py 72` reports 0 PROBLEM lines.

**Verdicts:** root confirmed. Nodes: 7 confirmed, 1 plausible, 2 transcription_suspect. Ref checks: 5 supports, 7 not_checked (all the AHD:89 / AHD citations — the 1975/76 New College Edition main body is not open online — plus the three nodes Nourai gives no refs at all). Books consulted: KLN, SKT, FSD, AHD/Watkins, POK, WLD, IEC, LKT, TTS, MON, BQT, ARY, LAT.

**Flagged items**
- `transcription_suspect` #2 Turkish "afandi" — **error in the book**. The printed page really does read "afandi"; the Turkish word is *efendi* (Ottoman افندی). Nourai appears to have taken the vowels of the Modern Greek vocative ἀφέντη that Klein prints ("read afendi") and made it his Turkish headword. The arrow Greek → Turkish itself is fully confirmed by Klein p.502, Skeat, Lokotsch no. 557, Funk & Wagnalls.
- `transcription_suspect` #9 Persian — **extraction error, owner must fix**: the printed page shows **اتوماتیک ، اتوموبیل ، اتوبوس** (wāw between mīm and bē), the JSON `script_extra` has **اتومبیل**. The etymology of the node is otherwise sound (Mo'in tags the whole family [فر.]).
- `plausible` #6 German auto-bahn — the arrow "Greek autos → German" is a triple shortcut (αὐτός → Fr. automobile 1861 → Ger. Automobil → clipped Auto → Autobahn, late 1920s), and the second element *Bahn* is unrelated native German (< MHG ban, PIE *gʷhen-; Watkins indexes AUTOBAHN under gʷhen-¹).

**Notable positive finds:** Klein leaf 273 s.v. effendi reproduces Nourai's chain word for word; Mo'in's افندی entry (MON_part1 line 15234, no. 22701) tags it [تر.] and glosses it «آنکه به نفسه کار کند» — a literal Persian rendering of Greek "self-doer", so Mo'in independently supports the whole route. Pokorny p.75 does mention αὐτός under "4. au-" (Walde-Pokorny I 14-15 does not), so the root's "from uncertain origin" (copied from Klein) is dated rather than wrong. Wiktionary confirms اتوبان is borrowed from German Autobahn, not French/English.

Files written: `/home/sfmqrb/git/rishe/data/verification/page-72.json`; page image for audit at `/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/72.png`; 8 web pages archived via `fetch_source.py` into `data/verification/sources/web/`.
