# Verification process log — verify-page-106


## [2026-09-05T14:55:34.652Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 106 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-106.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-106.json. Write /home/sfmqrb/git/rishe/data/verification/page-106.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 106` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:55:36.179Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:55:36.848Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:55:36.866Z] TOOL RESULT

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


## [2026-09-05T14:55:37.042Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-106.txt"
}
```


### [2026-09-05T14:55:37.055Z] TOOL RESULT

```
1	=== PDF page 106 (book page 76) ===
2	--- entry 0 ---
3	ROOT [Avestan / Old Persian] Čirya, Cirya, Cairya, Carya : brave, quick  (refs BRT:598; BQT:676; SYN:1150)
4	#1 (parent #0) [Pahlavi] refs=BQT:676 | cĕr, čĕrîh : strong, brave, quick, dominating
5	  #2 (parent #1) [Persian] refs=BRT:598; BQT:676 | čîr «چیر» : dominating, victorious | extra: چیره ، چیرگی
6	--- entry 1 ---
7	ROOT Cirya -> redirect to Čirya
8	--- entry 2 ---
9	ROOT [Sanskrit] Čîxâ, Čixâ, Čĕxara : point, tip, any pointed thing, skewer  (refs HRN:168)
10	#1 (parent #0) [Persian] refs=BQT:1203; HRN:168; FVF:383 | sîx «سیخ» : skewer | extra: سیخونک
11	  #2 (parent #1) [Turkish] refs=TAD:38; BQT:1203; MON:2112 | šîš : skewer ; šîšlîk : meat roasted on a skewer ; šîš-kabob : meat roasted on a skewer
12	    #3 (parent #2) [Persian] refs=MON:2112 | šîšlîk «شیشلیک» ; šîškabâb «شیش کباب»
13	    #4 (parent #2) [English] refs=AHD:1196 | shish kebab : pieces of seasoned meat roasted and served on skewers
14	--- entry 3 ---
15	ROOT Čixâ -> redirect to Čîxâ
16	
```


## [2026-09-05T14:55:40.337Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-106.json",
 "description": "Read page 106 source JSON"
}
```


### [2026-09-05T14:55:40.373Z] TOOL RESULT

```
{
  "pdf_page": 106,
  "book_page": 76,
  "entries": [
    {
      "root": {
        "name": "Čirya, Cirya, Cairya, Carya",
        "lang": "Avestan / Old Persian",
        "refs": "BRT:598; BQT:676; SYN:1150",
        "gloss": "brave, quick"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:676",
          "words": [
            {"translit": "cĕr, čĕrîh", "gloss": "strong, brave, quick, dominating", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BRT:598; BQT:676",
          "words": [
            {"translit": "čîr", "gloss": "dominating, victorious", "script": "چیر"}
          ],
          "script_extra": "چیره ، چیرگی",
          "note": null,
          "quote": {
            "text": "همی تا آز باشد بر جهان چیر - نگردد جان مردم از گنه سیر",
            "poet": "Vîs-o-Râmîn"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Cirya",
        "redirect": "Čirya"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Čîxâ, Čixâ, Čĕxara",
        "lang": "Sanskrit",
        "refs": "HRN:168",
        "gloss": "point, tip, any pointed thing, skewer"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "BQT:1203; HRN:168; FVF:383",
          "words": [
            {"translit": "sîx", "gloss": "skewer", "script": "سیخ"}
          ],
          "script_extra": "سیخونک",
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Turkish",
          "refs": "TAD:38; BQT:1203; MON:2112",
          "words": [
            {"translit": "šîš", "gloss": "skewer", "script": null},
            {"translit": "šîšlîk", "gloss": "meat roasted on a skewer", "script": null},
            {"translit": "šîš-kabob", "gloss": "meat roasted on a skewer", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:2112",
          "words": [
            {"translit": "šîšlîk", "gloss": null, "script": "شیشلیک"},
            {"translit": "šîškabâb", "gloss": null, "script": "شیش کباب"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 2,
          "lang": "English",
          "refs": "AHD:1196",
          "words": [
            {"translit": "shish kebab", "gloss": "pieces of seasoned meat roasted and served on skewers", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Čixâ",
        "redirect": "Čîxâ"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T14:55:41.106Z] TOOL CALL #4: Bash

```json
{
 "command": "sed -n '1,200p' data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:55:41.153Z] TOOL RESULT

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


## [2026-09-05T14:55:52.993Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['BRT','BQT','SYN','HRN','FVF','TAD','MON','AHD','PHD','NYB','HUB','CHEUNG','POK']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online entries"
}
```


### [2026-09-05T14:55:54.570Z] TOOL RESULT

```
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists on several Iranian sites (ketabnak/parsianjoman) but could not be fetched here (login/JS)."}
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== CHEUNG MISSING
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
```


## [2026-09-05T14:55:54.587Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"čir\\|cir-ya\\|cirya\\|ĉiθrya\" BRT.txt | head -40",
 "description": "Grep BRT for cirya"
}
```


### [2026-09-05T14:55:54.639Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:56:00.434Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'(?m)^\\s*59[78]\\s*$', p) or re.search(r'\\b597\\b.*\\b598\\b', p):\n        print('---leaf',i)\nEOF",
 "description": "Locate BRT column 598"
}
```


## [2026-09-05T14:56:01.897Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"čīr\\|cer\\b\" PHD.txt | head -30; echo \"=== PHD cer\"; grep -n \"^cē\\|^cer\\|^cīr\\|^če\" PHD.txt | head -40",
 "description": "Grep PHD for cer"
}
```


### [2026-09-05T14:56:02.826Z] TOOL RESULT

```
1041
```


### [2026-09-05T14:56:02.889Z] TOOL RESULT

```
394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
1148:Cancer Karzang.
1207:chase (n.) naxčīr.
2073:game Кадар, wāzīg; (quarry) naxčīr.
2476:introducer handémangar
3305:quarry (prey) naxčīr.
=== PHD cer
1185:ceremonies, religious ~ khamāgdēn, radpassāg.
1186:certain a- | abē-gumān, ēwar, tāštīg.
1187:certainly ēwar.
1188:certainty abēgumānih, tāšt.
```


## [2026-09-05T14:56:07.864Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o -n \".\\{0,160\\}victorious.\\{0,160\\}\" PHD.txt | head -20; echo \"=== PHD_mackenzie\"; grep -o -n \".\\{0,160\\}victorious.\\{0,160\\}\" PHD_mackenzie.txt | head -20",
 "description": "Grep PHD for victorious"
}
```


## [2026-09-05T14:56:08.961Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \".\\{0,200\\}čīr.\\{0,200\\}\" HRN.txt | head -20; echo \"=== HUB\"; grep -n -o \".\\{0,200\\}čīr.\\{0,200\\}\" HUB.txt | head -20",
 "description": "Grep Horn and Hübschmann for čīr"
}
```


### [2026-09-05T14:56:13.615Z] TOOL RESULT

```
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,160}
                            \___exceeds complexity limits


=== PHD_mackenzie
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,160}
                            \___exceeds complexity limits
```


### [2026-09-05T14:56:19.002Z] TOOL RESULT

```
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,200}
                       \___exceeds complexity limits


=== HUB
ugrep: error: error at position 83
bf][\x80-\xbf]*){0,200}
                       \___exceeds complexity limits
```


## [2026-09-05T14:56:25.043Z] TOOL CALL #11: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py <<'EOF'\nimport sys,re\npath=sys.argv[1]; pat=sys.argv[2]\nctx=int(sys.argv[3]) if len(sys.argv)>3 else 180\nmaxn=int(sys.argv[4]) if len(sys.argv)>4 else 12\nt=open(path,encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nn=0\nfor i,p in enumerate(pages):\n    for m in re.finditer(pat,p,re.I):\n        n+=1\n        print(f'[leaf {i}] ...{p[max(0,m.start()-ctx):m.end()+ctx]}...')\n        print('---')\n        if n>=maxn: sys.exit()\nif n==0: print('NO MATCH')\nEOF\necho ok",
 "description": "Create grep helper script"
}
```


### [2026-09-05T14:56:26.461Z] TOOL RESULT

```
ok
```


## [2026-09-05T14:56:29.970Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### PHD victorious\"; python3 $S PHD.txt \"victorious\" 200 8; echo \"### PHD cer/cyl\"; python3 $S PHD.txt \"c[eē]r[ 0-9\\[]\" 150 8",
 "description": "Search PHD for victorious / cer"
}
```


### [2026-09-05T14:56:31.629Z] TOOL RESULT

```
### PHD victorious
[leaf 23] ...y. abarón Pf*/xwn! | N wárün] contrary, wrong, sinful. ~ih: sin. abar-6z PóPeoc] stronger. ~ih: mastery. abar-tan [Pltn'] arrogant. ~th: arrogance. abarwēz Pfltvyc | (M *bruyj, N parwéz)] triumphant, victorious. ~ih: triumph, victory. abarzén, v. zmašk, abaxs [hš] repentant; regret. ~ЛЬ : repentance. abaxšāwand [5hP^wnd] regretful. abaxšāyīdan, abaxšāy- [5APd-ytn! | М ?bxPy-, N baxšūdan, baxšāy-) forgive, h...
---
[leaf 45] ..., v. idan. *téhag [cyhk'] grief. čehel [40 | N chil] forty. Céh-widarag [cyhwtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- |...
---
[leaf 45] ...wtlg] = činwad puhl. čēlān [cy”x! | = M, N ~] dagger. ~gar [-kl, -gl | N ~] swordsmith. Cér [cyl | M cyr, N —] victorious, triumphant, brave. —Ih: bravery. Cérihistan, Cérih- [cylyh-stn'] triumph, be victorious. īčīdan, čīn- [cytn', cyn- | M cyydn, cyn-, N ~] gather, pile up. ~išn: gathering. *čīdan, čēh- [cytn', cyh- | M cy-] mourn, lament, grieve. ~i8n : lamentation. ~i$nig¢ : mournful. ihr [cyhl | M cyhr...
---
[leaf 93] ... M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš...
---
[leaf 93] ... M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [...
---
[leaf 181] ....
vengeful kénig, kénwar.
venom wii, zahr.
venomous wišoūmand.
Venus Anāhīd.
vernal waharig.
vertebra muhrag.
very abēr, saxt, staft, Skeft.
vessel jām(ag), kabārag, takók.
vetch mas,
viceroy bidaxš.
victorious abarwéz, Cér, péroz(gar).
victory abarwézih, pērēz(gar)īh; fina...
---
### PHD cer/cyl
[leaf 65] ... N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handē...
---
[leaf 131] ...róstan, xwandan.
calumny dušēwāzih.
calyx kulāfak.
camel uštar.
camp bunag.
camphor kapür.
can Sayistan, tuwān, P Sah-; v. able.
canapé bazmawurd.
Cancer Karzang.
cane graw, nay.
cane-brake nayestan.
cap kulaf(ak).
capable adüg.
capital šahrestān.
Capricorn Wahig.
captive dastgir, griftar, wardag; v. pr...
---
[leaf 146] ...ertwining hambandišnīh.
intestine(s) ródig, uruspar.
intimate hamdam.
intoxicated mast(og).
intoxication mastēgīh.
introduction handémangarih.
introducer handémangar
inverted nigün.
investigate wizóstan.
investigation wizoh|/yisn.
invisibility abaydāgīh.
invisible abaydāg, awēnišnīg.
invocation azbāyišn...
---
[leaf 202] ...U ISU ves e ©, Pee
1-2čīnag čīnišn čegāmag čegām-iz Cer čēlāngar čēlān Celangar čērīh čērīh- čērīhistan čim čim-gūwāgīh čimīg 1%īdan čand, čang Cand- éandih éandal Čang-srāy čandišn L?griw! éandidan cob
čaw...
---
[leaf 233] ...yād YU g S zāmēn- - e$ zāmēnīdan Wes PAS zadan US zādag \зтеҳЅ zibāl NS S 1-1, zay- -aS zih AUS zi(w)- _ GAR zēnhār Sao «S
zēnāwand ayy e$ zēnabzār ` Cer WS zēndānīg oro S zēndān wo pS zēndānbān i^o "GO u$ mër: 15 S. ` mee Ziwénidan zindagih A$ 43 HS zēnīg, zīndag yr
1-2zën S xrīn-! _1 S
vāyčag zūnūg хо...
---
```


## [2026-09-05T14:56:32.251Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### HRN cir\"; python3 $S HRN.txt \"[čc][iī]r\" 200 10; echo \"### HRN 168 sikh\"; python3 $S HRN.txt \"s[iī][xkh]\" 150 6",
 "description": "Search Horn"
}
```


### [2026-09-05T14:56:33.790Z] TOOL RESULT

```
### HRN cir
[leaf 53] ...rd auch das sog. yäi isäret oder
yäi t'arif zurückgeführt (Salemann-Shukovski,
Neup. Grammatik § 19); doch scheint es mir besser,
dasselbe mit dem e des unbestimmten Artikels (yäi
validet) zu identificiren, wie dies nach mündlicher Mit-
teilung Prof. Nöldeke's schon vor Jahren Ewald
gethan hat.
138. ei 'o!'
aw. äi o!'; phlv. ai (vd. 19 (32); N:n vd. 18 (48));
skr. di.
139. ec jemand, etwas', s. hec (...
---
[leaf 119] ...— 98 —
Auch np. ceh7'e (Wörterbücher jehre) 'Spinnrad' ge-
hört hier; dialectisch (Kasan) lautet das Wort cörd,
cöre, cir d. i. *care. In Vöniäün (Kä§än) bedeutet
car/^ auch ^Wetzstein (s. v. sunhade),
438. cer^n Teil, Haut\
s,w,carema7i' Teil'; phlv. carmm- ledern (vd. 18 (6)
Gl.); ai. cärmaU' 'Fell'.
oss. t. mr, curm,...
---
[leaf 121] ...n Vie?\ cü, cünän {'^)i^^^)t, Is. 10, 11), cünln^), cünkL
phlv. digün *wie?* {ci + aw. gaona-), cigämh, vergl.
np. cigüne (vergl. zeryün aus aw. zairLgaona-, No.661).
451. ci(h), ci (AM.) was?, wie?\ cirä warum?*.
ap. üyakaram, -ciy (enclit.); aw. eis, cit; päz. ci/i
(phlv. no); ai. -6it (enclit.).
af}'. ca 'was?; einige*; oss. d. ci, ci, t. ci 'was, was
für ein, welch?' (322).
Als Encliticon hat Sal...
---
[leaf 181] ...rt*; phlv. sat; ai. gatd-,
kurd. sed; af/. sal, sil; oss. sädä (218); wa;^. sar.
LW. sad.
720. ser 'Kopf; vergl. serapa 'Ehrengewand' ^).
aw. Sarah' 'Kopf; phlv. sar^ asar 'endlos' (aw.
anayra-); ai. ciras- 'Kopf; arm. sar 'Höhe, Gipfel,
Abhang' (H. No. 247).
'J Übertritt in die e-lleihe Ca. bei Feist, No. 531).
^) oiiottnts (llesycb), de Lagarde, Ooa. Abb. 208 (?); vergl.
Miklosiob,' Dcnksobr. WAW. ...
---
[leaf 210] ... 203 Zeile (>), kurg 'nicht mehr
legendes, geiles Huhn *^).
Kas. karg, kerk (s. v. mi(ry).
aw. *kahrka- in kahrkam- *Hühn«»rfresser (OtMor)';
phlv. kark; ai. kfka\mku' 'Hahn'.
kurd. kurk 'Huhn'; afy. cirg; oss. /•«;•/• 'Ih'nno,
Huhn (154); wa;^. kork,
9. kerf/es 'Geier' (Sahn. I, 120 Vers 1013).
aw. ÄraÄrArtZs^- 'Geier; \)h]\\ kahrkäs, kargua (Bund.).
LW. af/. gar gas; bei. kargas, w, Kargaz (127); o...
---
[leaf 210] ...i den Pärsen noch vorkommende np.
karkatas 'Geier scheint nach aw. kahrkatas- repristinirt
zu sein.
*) Auch nuf persischen Inschriften in Indien, vergl. Epigraphia
:ca ir, US Note 25.
*J Diese spezificirte He<ieutung der Wörtorhüclior ist vioUoicht
• küii^tUch «M'soinion....
---
[leaf 240] ...s teter. Et. ir. II, 132).
Ganz unsicher, da die PehlevTform (NB. )XTN oder
JNin) unklar ist; die Verknüpfung mit ap. apadäna-
ist vollständig verfehlt.
977. merg *Tod'.
aw. mahrkor 'Tod*; phlv. marg\cirjan^ marißh 'Tod';
arm. vergl. waÄ, warA 'Tod' (H. No. 185).
kurd. merk 'Tod'; bei. mark; oss. d. t. marg *Gift'
(178 e).
Der Bedeutungswechsel im Ossetischen könnte als
ein Analogen vielleicht auch d...
---
[leaf 245] ...— 224 —
Studien, II, 178, befriedigt nicht, da er müye^ nicht
7nöye, als np. Form ansieht.
Fr. Müller, (WZKM. 5, 65) construirt eine *[/maud-
mit einem ap. "^matida-- als Grundform und identi-
ficirt np. möye mit arm. moir 'Bettelei', eigentlich
Torjammern', moiracik 'bettelnd' ; dazu auch np. mit st
*Klage*, mustmeud,
998. me (geschrieben meh) nicht* (prohibitiv).
ap. aw. ai. ma 'nicht' (fifj);...
---
[leaf 260] ..." gegen ai.
pärsni: Der Übergang von rs in /S ist dem gegenüber nur ein schein-
barer in äia^s aus ätars und Syäva^^ aus Si/ävarsati-; )^h soll hier bloss
eine scharfe oder wahrscheinlich etwas modificirte Aussprache des s
bezeichnen, wie sie in ^^ar^set (vergl. Hörn, Mitteiluiigen, Heft IV,
S. 34) berechtigt war. Diese Aussprache wurde dann weiter über-
tragen, z. B. phlv. Zartux^t (aw. Zara^usfra-)...
---
[leaf 264] ...- 243 -
aw. Vieira- 'Entscheider ; phlv. v(i)öfr 'Entscheidung ;
Entscheider, Richter ; arm. LW. vcir ^Entscheidung.
1085. veng, ving 'leer; arm'.
aw. vergl. wwa- *leer, mangelnd'^); ai. und- Voran
etwas fehlt, unzureichend'; arm. unain *leer' (H.
No. 236); got. van 'Mangel*; gr. bvvi^ ermangelnd'
(z...
---
### HRN 168 sikh
[leaf 50] ...- 29 -
124. engehtn (AM.), enguhln *Honig, vergl. terenguhin,
sikengubi7i, sirkenguhln, gezengubln, gulengubm ; arab.
LW. anjuMn, vergl. /vskanjubm (Ibn Beitär) u. a. m.
phlv. angpen, angumen {e beweist das arm. LW....
---
[leaf 50] ... Falls äyyuQo; babyl. *ahgarti = *agru entspricht,
könnte dies aus annlu (d. i. ^Mensch*) agru (^gemieteter , zum Dienst
gezwungener Mann*) oder abil sihri agru oder asgandu agru ('gemieteter
Bote, zum Dienst gezwungener Bote*) abgekürzt sein. Assyr.-babyl.
agäru 'mieten, zum Dienst zwingen* geht auf h...
---
[leaf 59] ...r ist allgemein entlehnt.
167. häzvL *Arm'.
g. bat (aus *baht), Kas. bot, böht böhu etc.; ""inNZ
(Is. 3, 20).
aw. bäzu' *Ärm'; phlv. bäzüh^). bazak]masih^) (ZPGl.);
ai. bahü-,
kurd. bOsk, bäsik: bei. bozk (35).
LW. arm. bazuk (H. No. 48); oss. d. bäzug (Hübsch-
mann, S. 120, v. Stackeiberg, 3AMSTKA 5)....
---
[leaf 59] ...m'.
g. bat (aus *baht), Kas. bot, böht böhu etc.; ""inNZ
(Is. 3, 20).
aw. bäzu' *Ärm'; phlv. bäzüh^). bazak]masih^) (ZPGl.);
ai. bahü-,
kurd. bOsk, bäsik: bei. bozk (35).
LW. arm. bazuk (H. No. 48); oss. d. bäzug (Hübsch-
mann, S. 120, v. Stackeiberg, 3AMSTKA 5).
Gehört hierher auch np. boz 'Klafter (V...
---
[leaf 83] ..., päkih,
278. pälüden 'reinigen', Praes. pälay-em, päläyiden,
paiti + alüden (s. älüden^ No. 42) ; phlv. pälüt (Bund.),
päz. pälJdan, pälaidan (West, Sik. gum.-Gl.).
bei. LW. palayag^ pälenay 'seihen, worfeln, reinigen'
(292).
^j Vergl. Geldner, Studien I, 16. Bartholomae (briefliche
Mitteilung) verwei...
---
[leaf 102] ..., 57); oss. d, ßti, t. fite Tett, Speck'
(289); bei. pT<j, n. pty (298); wa/. j>7/ 'Biestmilch'
dagegen gehören zu paz. j>^y (lies piy) *Fett' (West,
Sik. gura.-Glossar) , das aus *pivaka' entstanden ist
(vergl. Hörn, KZ. 32, 584 No. 17).
T.
)6. tä *bis; damit*.
phlv. ^öi6(?), Hs. tai oder tag, vd. 3 (...
---
```


## [2026-09-05T14:56:44.043Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\n# find leaves containing numbers near 598 as standalone tokens\nfor i,p in enumerate(pages):\n    toks=re.findall(r'\\b(5[89][0-9]|60[0-9])\\b',p)\n    if toks:\n        print(i, sorted(set(toks))[:8], repr(p[:80]))\nEOF",
 "description": "Find BRT leaf with column 598"
}
```


### [2026-09-05T14:56:46.700Z] TOOL RESULT

```
72 ['583'] "ltä  °ia asimäl  .  .  7-Tmruyff  ya'iä  . .  vydmrvi/J  .  . sarairus/ro  Y.i2."
120 ['580'] 'nalibya  ktivanaiibya  Vf. "    ■    "  "\'        -teht  abseits.  \'  70.2,  *N.'
137 ['583'] "a-  Adj.  'keinen  Kampf  führend, nicht  kämpfend':  'na  F.  7.\nPü.:  apatkär."
191 ['584'] 'ao^a- nanqm  .  .  mazdäi  x/ahr^mcä  -räi  ä  Y. 27. 13.  a)  daneben.^.»!  (sd'
247 ['600'] '9.  19-20,11,  6.21,^.36,4.12,13, Mi  15.  J\'37,  H--i  {dRn.  "50,  70,  90,  2'
263 ['593'] 'a^rrä 7\'ohu!-ä  cöist  manatihs  yi.."..  Idas  Rind) das  er  durch  seinen  A7'
289 ['588'] 'ay-  m.  EN.  eines  Gläubigen: No.  10  f.  —  *)  Hds.  ti-iiaufci;  s.  unten'
294 ['599'] "'' i)xa.:di^e  navaiti 'wqm{CiY,) pairi.- yaoidaikUa  stiptibyas£a{^^..'S.i4-  I"
306 ['602'] 'p/.  661.  iBild. vgl.  femer  lat,  frägro  ans  "ghräghtiiö;  Bcu. Grdr.a  /. '
340 ['580'] "A.  hat  das  Iranische  ät%ru'  nicht  I taluT',  —  4)  Them. ;  dem  ai.  «it"
342 ['583', '584'] "' :  yavai 'ia  *avi.inatn  hariks  hancayJt  V.5.60.\nPO.!  transs'kr.\n•  j.  äa"
343 ['581'] " V.  _j.  14;  —  spUi.dSihra{^A^  °manat kaca  niibannti  V.  7.  24;  —  ts  '"
345 ['588', '589'] "  n.  i)  'Same', im  eig.  Sinn  (nur  Komp.).  2)  'Urspmng, Herkunft,  Abstam"
346 ['591'] "t  10.  84;  —  %wqm  yazSnte  .  .  dai- AAu.paiays  . .  '^wqm  naraHt  ySi  t"
347 ['586', '593', '594'] '(sd.)  brä- z^m  avavaliit ..  Yt/^.  33; — ysi  pfs?m<!it sär;rm(sd.)  bunfaifi'
349 ['595', '596', '597'] " 2.  3)  sva.\n'nicht  einmal,  ne  —  quidem' ;  a)  die  Negation folgt:  yat  "
351 ['599'] 'Herrscher  sollen (über  uns)  herrschen  —  nicht  sollen schlechte  Herrscher '
352 ['602'] '\',  S\'*^;  —  \'vat  antan "vantö  *<iae  qsavö  auhin  N.  loS;   *iurius  .  . '
353 ['604'] "(doch\nvgL  voNBEAnicE  ZDMG.  vo.  355).   —    ')  So\nFl;  NA.  •frülS.\n•  j.  "
354 ['606'] '    Et.?  —    »>  Das  «rsle  «  ist  mit  dem  Zeichen i      Xu.  33  der  Sc'
355 ['608'] '  Wort  beeinllusst  ist.  —  0  An  den entsprechenden  Stellen  des  Mi,  steh'
376 ['585'] '  mraot  "was   dein  Aia,   was  dem  A.         J-  y^"""  \'"\'"  ^-  ^^-  ^-  '
395 ['607'] "ÖHT/ali  'er  rinnt' ;  np.  vgl.  äaiiidan,  — ')  Them.,  wie  ai.  dhanvati. "
423 ['585', '598'] "  (sd.)   Y.  57.  lo.         A)    GS.\n'möis''>  mit  upamana-  m.  (sd.,  auc"
424 ['580'] "  puh'J'  Ao.  7. 2;  —  aria- ■.sah^'ä  °v(^us'^  xsaydhiyt^'^  pu%''a''  Ao.\nE"
436 ['590'] " rtäo  'hfyam'ü.öy,  —  afvqm  vä avi  xsafamm  duye  (Af)-^'  vä  'Hx.S.w;  — a"
439 ['595', '608'] "  ^.■.'  aiwiJruitlnU  aiisät   .  .  YLj.  90.\ndrn£dndtkdatem'>,erL:BiVH™(oder!"
461 ['593'] 'a  drivataÄi\nLeiung  aniicher.  Wohl  Name  eines  Körper- leilSt  vgl  unter  a'
481 ['599'] 'an  fiatü,  erL ;  frärön  latJärlA  röi  ya! alt.  —  4)  Vgl.  ai.  palhas.  n'
505 ['591', '600'] "�)Y.5i.i3.  a)dn. auch  ohne  cinvatB  'die  Brücke'  Kar'  i^,: hrlicit  (Sp.  "
533 ['608'] 'üjiyahyä  Bh.  /.  lo:\n—  kt/\'baßyar   avam    \'yam   avSjJ"  yaks la\'bßßyer  •y'
537 ['582'] "ä  ..'^•Sy. 10; — yat  dim  dämSi^  upamanS  huirixttm  b° irinaxti  Yt/0.  68; "
540 ['592'] ' profetre  pratum  sva.  ..pflegte das  Land  Grasweide  zu  tragen"  V.  2. 24.'
552 ['596'] ' Vorderfüsse  um  eines  Vorderfiisses Länge  hinauspisst"  V.  /<?.  40*\';  —  '
563 ['600'] "eit.   —   Zum  \\'.  'mh-;   vgl.  aL\nfiräj-llay  f.  'Zeugung';  s.  daiu  Bthl"
599 ['592', '595'] " n'^  ..  V.  5.  58;  —  Ab n°  ins  vliyätä  dafaäcinii  (Sp.  595  o.)  Y.  a"
600 ['595'] '  n°  /rasaya  (sd.)  ..  cOxnar^Y. mit  indikativischem  Verbum:  pancartqm>  4'
601 ['595'] "  von ma  'fif;  a)  im  gAw.;  es  folgt  Optativ; zu  i):  ff  daibitim  dus.s"
610 ['593'] 'i-  Adj.  (nyäAtai  NP.).  —  Pö.  (la  V.  7p, YL  //):  nikänSff),  (in  V.  5'
644 ['593'] "a  Sita  (Stverz.) 'ta  asaoni  Yt.  16.  7  usw.;  —  ärväspa  iura Ha  Ytp.  s"
674 ['593'] '4;  —  ma  as  aFvB barB  (sd.)  yat  irUOm  "ne  quis  solus ferto  (id)  quod '
675 ['593'] 'Y.46. 15;  —  gavBi dvai%a    Y._92.  16.  3)    mit    folgendem  ,  ai^(l//{Sp'
684 ['590'] 'Sichhalten  an  — ,  Sich- richten nach  -\':  °t5  (LS.)"  paurmeibya ydia  rdi!'
691 ['593'] 'ü y  aurvat.aspahe  Yt  10.  13;  67, J2.38,  S.J.  18;  —  k>r)säspahe y  *£ae%'
708 ['586'] '  "\'/«  (statt  AP.)\n.  .  vanat  Yt.  2.  1 1 ;  —  frShnntal   atsrS\nmainyul a'
721 ['592'] ' V.^.  44,  5.5, 12,27,45, 57,  6.46,  8.2,  12,  ß.  II,  y.37,  i4. 17. ^5-9. '
726 ['588'] " lu  iraoS-.  —  s>  In  ge- \\     schlossener  Silbe  erscheint  vöi';  %  ag^."
731 ['595'] '  überhaupt  keine  ; Versündigung"  P.  57;  —  hyat  vUJntä  j (sPPrM.)  ängva'
753 ['598'] "rtan; (fflr  virnda-):  varaJn.  —  S.  noch  No.  if.  — ')  Unsicher.  Pü.:  v"
757 ['587'] '  ist,  was  er  (übles)  gedacht,  ge- sagt, geUn  hat"  V.7. 51;  —  vgl.  noc'
758 ['588'] ")  V,22. 19.\nKompA.;  Ab1eit.(?].  —  ai.  vfiiä-  ta.  'Baum' (Bthl.  IF.  p.  "
763 ['600'] "a- yasna  bai^azäi  {%A.)  fravazSnte  V.  7. 36.\nmit  nt  'nach  unten  führen,"
775 ['581', '607'] ' seinem  Wohlgefallen"  Y.^.  a;  —  AS. mit  °a  (vanma)  als  Adv.  sbes.  a) '
783 ['588'] 'dayasnsi! G.  2.  7,         S.  noch  v»r>zyata-  mit  No.  z.\nKompE.  —  Zum  '
787 ['606'] "/ra-  (»  statt  u,  S36S.  l), eig.  'der  gute  Kamele  besilH'.\n•  j.  vohv'a"
789 ['581'] 'zu  Y.  46) :  vifarl,  erl. :  röhiai  an  niart  veh muri.  —  O  Unrichtig  G'
808 ['593'] '  afiyH  vatihsui  mananhö /yaohana  vaocat  girsbqm  (sd.)  huxratui spmtqmca  '
810 ['604'] "nö  *ralcayeiti'''  .  .  mi^rS  Yt  10. 41.         a)  Des.  'dem  Verderben  "
822 ['600'] '  naiHi  däbayätl  {?,A.) "die  von  ihnen  gefällten  Richtersprüche wird  Arm.'
837 ['583'] "ulca  (statt pasvd)  bazda  nuit  'ta  (rrSii)  anazdya  ratufris abanfa  airist"
850 ['600'] 'a  hazanraisca  Vr.  Ä  i.  a)  mit attiib.  Einerzahlen:  hazatanm  narqtn  .  '
852 ['585'] '�ble  Gerüche empfinde"  H.a.  35;  7.  zu  b):  na^.a manyäe  jaynvi  */ia^a.am'
863 ['583'] '  vä  paiti sBinma  unqm  vä  katcil  va  paiH  \'raaam ".  .    oder    sonst   '
864 ['583', '584'] "ifiaif*i.\n•  p.  suguda-,  j.  suj-Sa-  Adj.,  be- zeichnet ein  Volk,  'Sogdian"
869 ['593'] '  den  Wunsch  nach  der  langen  Dauer des  köstlichen  Daseins,  von  dem  ges'
870 ['595'] 't  stuyi{\\%.y^  tüSil  ahmät *ä  *syänlm(sd.)..x/tä  "..gelobe  ich  das: .." Y.'
871 ['597', '598'] '  tma  myasda (näml.  avaioayamahi)  Vi.  11.  3;  —  Aap/a /lanti  fiävaiia  ba'
875 ['584'] 'airi  li  kB  *par»tB.tanuttqm stätahaiti  (3S.)  yahmat  haca  ttm  ava.rao- l>'
876 ['606'] 'erl.;   ke  andar\nxänak  i  piiarän  11  iSi  asf.\n•  p.  (,  j.)  stäna-,  j.  '
880 ['591'] "sein'. Praes.  3  sp^nza-.\nmit  Inf:  y!  ,  .  dtmanakya  xh'i-rsm  .  . asil /"
882 ['585'] " Fidsch  JusTl  NB.  309  a.\n•  j.  spänah-  n.  'Heiligkeit,  sanctitas'; a)  v"
938 ['600'] "tsi  jasaiti  avanhe  Yt.  J7.  2 ;  —  para  ' hl  iris)nts  ralsim  Hkayat  V."
988 ['591'] '.  auch  Sp.  Komm.  2. 47J. g.  hisvi  Y.  4^.  i;  lies  hkvä;  s.  hitM-.\n•  '
1011 ['584'] "a  aita  däman  *dähimaide 'maya  clsmaide  'maya  matnyämaide  *yam da^at  ahur"
```


## [2026-09-05T14:56:57.756Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### cairya\"; python3 $S BRT.txt \"cairya|cirya|carya\" 200 12",
 "description": "Grep BRT for cairya/cirya"
}
```


## [2026-09-05T14:56:58.764Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==190' HRN.txt | head -60",
 "description": "Print Horn leaf 189 (p.168)"
}
```


### [2026-09-05T14:56:59.450Z] TOOL RESULT

```
### cairya
NO MATCH
```


### [2026-09-05T14:57:01.133Z] TOOL RESULT

```
— 168 —
kiird. LW. sl; idy, dre; wa/. tral, sangl. trdl, ya/n.
OeraT, miuj. sardi, sar haröi, si/n. arrai,
760. st 'dreissig'.
aw. drisatent 'dreissig; phlv. sih, päz. si\ ai. trincdt.
kurd. LW. s7; af/. der6\
761. siyah *scliwarz', sit/dhi.
Semn. suah.
aw. st/äva- 'schwarz' in SyävarsCmU'y Syäiaspi-;
phlv. siyak, siyäh (PPGrl.), raand. LW. N"'1N''D ; ai.
Qyävd' 'braun, schwarzbraun'; arm. LW. ^) seao
'schwarz'.
kurd. bei. (348) LW. siyäh 'schwarz ; oss. saa (222);
wa/. sü, sangl. s6L
Als Grundform von . np. siyäh ist *syaoaka' anzu-
setzen.
762. sex (i'^i^iit auf be/^), Sa di, Gul. 46 Zeile 5 v. u., Spr.)
*Bratspiess'.
skr. gikha- 'Spitze (eines Pfeiles etc.)', vergl. cekh-
ara- (?).
kurd. stx^^ si/ü *Lunte* ; bei. slh^ sl *Bratspiess, Lad-
stock' (344).
763. si^deh 'dreizehn*.
aw. dridasa 'dreizehnter'; phlv. sicdahum^) (päz. seS,
sez"); ai. trdyödasa,
kurd. dausCf slzdeh (LW.); afy. dyärlas.
np. sizdeh ist eine Analogiebildung.
764. s~ui% 'Kummet'*).
aw. sima^ vergl. siimiSra- yt. 10, 125 (Geldner,
KZ. 25, 530 Note 200); ai. cdmyä- 'Jochbalken
(nach Geldner; PW. hat 'Zapfen, Holznagel, Keil,
1) Nach Nöldeke bei Hübsohmann, KZ. 23, 402.
^) In E^snadäsa^s Pärasiprakäga aus Akbar^s Zeit findet sich nur
{Mia- (No. 723), wie die heutige indische Aussprache lautet.
*) Vergl. Seite 128 Note 6.
^) Ich vermag mir nach der bei Vullers abgedruckten persischen
Erklärung keine rechte Vorstellung über die Verwendung des sim zu
machen, doch scheint es unserem 'Kummet* nahe zu kommen.
```


## [2026-09-05T14:57:26.975Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['BQT_v2_pages.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    pages=t.split('\\f')\n    print(f,len(pages))\n    for i,p in enumerate(pages[:6]):\n        m=re.search(r'\\[pdf page (\\d+)\\]',p)\n        print(i, m.group(1) if m else None, p[:60].replace('\\n',' '))\nEOF",
 "description": "Inspect BQT v2 pages file"
}
```


### [2026-09-05T14:57:28.717Z] TOOL RESULT

```
BQT_v2_pages.txt 684
0 None 
1 None                                          ‫‪7‬‬              
2 None                    ‫م‬ ‫و‬ ‫نآکو سخنیم بیاموزد مرا‬         
3 None                                                      ‫‪ar‬‬ 
4 None    ‫و‬              ‫فك اا ‪ .‬بخش‌اول (منطق)‬              
5 None ‫‪ . ۱‬فيه ما فيه ‪ .‬مولوی بلخی رومی ‪ ۰‬مسحح بدیم الزمان‌ف
```


## [2026-09-05T14:57:29.668Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### TAD شيش\"; python3 $S TAD_pages.txt \"شيش|شش\" 150 10",
 "description": "Grep TAD for shish"
}
```


### [2026-09-05T14:57:31.496Z] TOOL RESULT

```
### TAD شيش
[leaf 2] ...تلىعر اف موعنااسهتحلال مغزالهاسما فيعصرناهذأ عصر‬       ‫بشوق من برااه‬
‫النور والاجمبهاد فيالفحص عنالاصولبالمعرض والطول متكا قد قله رعالاء‬
 ‫كدانت فششت في الاهة‬
                   ‫المتشوق على إدراك مبتغاه عنيت ‪ 2‬مجمعو ‪١‬‏لاثففلة ق‬
 ‫العربية قدا وحديئًا منسابة البها من اغات مختلفة حينابعدحين وا...
---
[leaf 9] ... » معناه غطاء الرجل وهو داس يلبس في الرجل‬
                        ‫باور ‪. 7‬يطالي عنندمة؟ معناه مخار امدرفه بآخرة‬

‫بواتبم ‪ -‬فارسي « بابونه » وحهشيشة ذات زهر أصفر مكلل بأبيض‬
                                                              ‫يتداوى بها‬
‫بادزص جافاريق عركن من بادأي ضد وزهرأي سم وهو حج...
---
[leaf 11] ...        ‫‪١‬‬             ‫‪8‬‏‬
                        ‫>‪ 2‬معئاه عطية وهد‪.‬ه واحسان‬                           ‫فارمي « محش‬                  ‫مخشيش ”' ‪-‬‬


                                                                       ‫‪ 3‬ك‪ 5‬فارسي ‪ 2‬بت» أي صم‬

                                    ...
---
[leaf 42] ...                        ‫غ‪ 01‬ومعناه حركة مرادفه الصور المتحركة أوالاشباح‬

                                       ‫دش »‬

        ‫شاش ‪ -‬عبراني « شش » معناه نسيج رقيق ممن كتان ثممنقعلن‬

‫شاقوف ‪ -‬اراي « شافوفا » أيالاطاس وهومشتق من (دشقف »أي‬
                     ‫هنمومن ‪9‬ه الشقف» العاميةأي ال...
---
[leaf 43] ...ق‬
                                    ‫ارامي « شوشبينا »‬   ‫شيين واثبين ‪-‬‬

                         ‫شتلة ‏ ارامي « شتلتا » عر بيهغرس وغراصس‬

‫«ششححممايمتا © براد بكتهاب صلوات الكبنة‬
                                      ‫ششححيمة ‏ ارامي و‬
                                                      ...
---
[leaf 43] ...
                         ‫شتلة ‏ ارامي « شتلتا » عر بيهغرس وغراصس‬

‫«ششححممايمتا © براد بكتهاب صلوات الكبنة‬
                                      ‫ششححيمة ‏ ارامي و‬
                                                      ‫و‬
 ‫ومعتاهالاسود لانه فى الاصلكان جلدا مجلد أسود ‪ .‬قال العلامة القرداحي معن...
---
[leaf 44] ...                                         ‫جد‬
                                           ‫من دقاق العبدان وتدخله فتموث فيه‬
                         ‫ششم ‪ -‬دواء لامين ‪--‬فارسي د جثم » معناه عن‬

  ‫ششمه ‏ عابي فارسي «جشمه» معناه عينالماء مرادفه ممستراح ومرحاض‬

                                     ...
---
[leaf 44] ...                                      ‫من دقاق العبدان وتدخله فتموث فيه‬
                         ‫ششم ‪ -‬دواء لامين ‪--‬فارسي د جثم » معناه عن‬

  ‫ششمه ‏ عابي فارسي «جشمه» معناه عينالماء مرادفه ممستراح ومرحاض‬

                                           ‫رىسية « شست »‬
                             ...
---
[leaf 45] ...                      ‫تشيحب عرال الككن‬
                                     ‫شهر ‪ -‬أرامي « هرا » معناه القمر وأيامه‬

                           ‫شيش ”‪ 2‬س عاي ترق (شيش» معناه ‪ 75‬وحور‬
‫ترق فارسي ش«يشه ‪ 6‬معناه قارورة وقنيئة ومنه شيسًا‬                 ‫تند‪9‬أمهاها‬
                           ...
---
[leaf 45] ...  ‫تشيحب عرال الككن‬
                                     ‫شهر ‪ -‬أرامي « هرا » معناه القمر وأيامه‬

                           ‫شيش ”‪ 2‬س عاي ترق (شيش» معناه ‪ 75‬وحور‬
‫ترق فارسي ش«يشه ‪ 6‬معناه قارورة وقنيئة ومنه شيسًا‬                 ‫تند‪9‬أمهاها‬
                                               ...
---
```


## [2026-09-05T14:57:40.048Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==46' TAD_pages.txt | head -60",
 "description": "Print TAD leaf 45"
}
```


### [2026-09-05T14:57:41.833Z] TOOL RESULT

```
                                            ‫ل‬


             ‫فكائه أرلى‪ «:‬شكاما سوا عات الاتبزان القن جام‬
‫العربي ودان الفارسي‬       ‫تمان تهنعاء سادل الشيعة وعيرفت منشمع‬
                                                   ‫لداعل كرت المكان‬
                                                                  ‫وهو اداة‬

                           ‫‪ -‬ترك « جانطه © معناهمحنظة‪005‬‬
                ‫‪7‬‬                                ‫ل‬                       ‫و‬
                                                                            ‫الم‬
                                                                              ‫ص‬

                                     ‫يرمة‬
                                        ‫شوذر ل فارسي « جادر ‪ 6‬معوناهخ س‬
                                           ‫شوب ‪ 53‬أراي « شويا » معناه حر‬
 ‫ارد ‪0‬ق تور امنا الماى وعووبالنارسة مقناة سمل‬                             ‫توزيةك‬
 ‫شوكران دنيات سام لانينى قألاءك ولي اليونانية ‪ 101‬شرب‬

                                                        ‫الآ الحكيمماءهافات‬
                  ‫سول ءاي رق‪:‬وجول ‪#‬ساء قر ويريةوسراة‬
 ‫(وال ) ممناه كيس وعدل ‪ .‬والجوالق‬‫شوال ‪ -‬فارسي « جوال » ش‬
                                                            ‫تشيحب عرال الككن‬
                                     ‫شهر ‪ -‬أرامي « هرا » معناه القمر وأيامه‬

                           ‫شيش ”‪ 2‬س عاي ترق (شيش» معناه ‪ 75‬وحور‬
‫ترق فارسي ش«يشه ‪ 6‬معناه قارورة وقنيئة ومنه شيسًا‬                 ‫تند‪9‬أمهاها‬
                                                                         ‫بالسريانية‬
 ‫‪6‬‬   ‫وأأعامة عون‪‎‬‬     ‫اصل الس لاءقد نوي وان انوى لم اإشعك نواه ‪ 6‬م‪..‬‬
                                                                   ‫للا‬
                                                                     ‫وفقناا‬
                                                                          ‫هو‬‫)‪ (١‬ه‬

 ‫القضيب ءنالحديد وك هه اللحم ليشوى وتنصاحبالهبارودة ويشدمميوانشه‪ .‬وفصيحهالسةعود‪‎‬‬
 ‫للاجتواء‪‎‬‬   ‫الاحم نظمه فاىلسقود‬   ‫شال سقد‬
                                         ‫َّ سقاقد‪٠ ‎‬‬
                                                   ‫وهو حديدة لبعوى علدينا الاحم ج‬
                                                                     ‫ونراد»" العرنم”‬

     ‫أن اثتنبك وسءيها السوريف ( اركية )‬     ‫(؟) يهى عند اهل ‪ 44‬اليف نه‬
```


## [2026-09-05T14:57:42.291Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"pdf page\" BQT_v2_pages.txt; grep -o \"\\[pdf page [0-9]*\\]\" BQT_v2_pages.txt | head -5; echo \"---v1\"; grep -o \"\\[pdf page [0-9]*\\]\" BQT_v1_pages.txt | head -3; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\"",
 "description": "Check BQT page tags and metadata"
}
```


### [2026-09-05T14:57:44.281Z] TOOL RESULT

```
0
---v1
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


## [2026-09-05T14:57:54.948Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 132 133 134; do echo \"===== leaf $n\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -70; done",
 "description": "Print BQT v2 leaves around p.676"
}
```


### [2026-09-05T14:57:56.434Z] TOOL RESULT

```
===== leaf 132
 ‫‪۷‬‬                                                                                                    ‫‪۳‬‬
                               ‫ومضرب وشمال وجنوب ‪.‬‬           ‫و فتح میم » اسب رهواروتبزرو راگوبند ‪٩‬‏ ‪#.‬‬
‫چهار نظم ‪ -‬کناب از چپار عنصر‬                                ‫کنانه ازچپار عنصر‬           ‫کر کی د‬       ‫چهار‬

                                                   ‫باشد‬      ‫‪ ۰‬است ‪ -‬وتخت شداد را نیزکوبند ‪ -‬وبسنی‌تخت‬
                                                                                             ‫کوس رگفاته‌اند ‪. ۳‬‬
                                             ‫باشد ® ‪.‬‬
               ‫‪:‬‬                     ‫‪1‬‬
                                                             ‫کناباز چهارحدجهان‬              ‫چهار گلخن‬
‫چهر ` ‪ -‬بکراولبروزن مهر؛ رویرا‬                                                                   ‫‪ -‬وچھارعنصراست ‪.‬‬
‫‪ -‬و بمعنی اصل‬          ‫اجنهند‬
                            ‫وی و‬
                               ‫خرب‬
                                 ‫گویند که بع‬
                                  ‫ذات‌نیز | مده أست ‪.‬‬       ‫چهار گو شه = هر چیزی که مربع‬
‫جهر اراد ‪ 3‬با زای هوز بر وزن‬
                                                             ‫وچهارجانب ‪ -‬و مربند ‪ -‬وسفرة کوچك را نیز‬
 ‫همن‬   ‫و‬   ‫همن باشد‬      ‫دختر‬     ‫نام همای‬   ‫مهر ا باد ›‬
                                                                              ‫‪2‬‬          ‫کویند ‪. ۴‬٭‪#‬‬
‫جحکم شریمتی که تابع آن بود او را بتکاح خود‬
                    ‫درآ ورد وداراب ازو متولد شد ‪.‬‬
                                                             ‫جهارم منظر كنابه ازفلك چهارم‬
                                                                                        ‫است که فلك آفتاب ‪,‬اشد ‪.‬‬
‫چهرآزاد است که‬         ‫رتمعن‬       ‫راد‬   ‫جهر‬

‫دختر بپمن مادردار اب ناشلت و نام دخشس افراساب‬                ‫چهار منقو طه کنابه ازفلك کرسی‬
                                                             ‫باشد که فلكالبروح است باعتبارچهارقطة مشرق‬

  ‫بمناست آنکه در افاله ها آهده که تخت‬                      ‫‪- ۴‬‬                 ‫‪.‬‬   ‫مه‬    ‫‪ :‬چار‬   ‫رك‬   ‫‪_ 9‬‬

  ‫ور بارء کیکاوس نیز همین‬
                        ‫شداد را بر بال چهار کرکس بتند وشداد برآن نشت و بهوا رفت» د‬
                                                                                                  ‫افانه گفته اند ‪.‬‬
       ‫چهار کوشه ‪.‬‬                ‫ریسدش‬
                                      ‫تا ک‬                        ‫توشه‬   ‫وساخت‬           ‫گوشه نت‬      ‫در‬    ‫‪- ۴‬‬

  ‫«‪+‬کنجنه ‪٩.‬‏‬         ‫نظامی گنجوی‪.‬‬

                                  ‫کشانور اس‬
                                          ‫ش‬                               ‫‪.‬‬             ‫شاه‬
                                                                                          ‫گكو‪ :‬چ‬
                                                                                               ‫ر ر‬
                                                                                                 ‫‪۴‬‬
 ‫‪ - ۱‬پهلوی ‪( ۲1116‬تخم) «یبر گے ‪« »64‬مسینا ‪ 7116 ۷: ۲۳۱:۲۰‬ط(بیمت‪,‬نژاد‪.‬منظر )‬
  ‫«مناس ‪ )۰۷۲:۲‬ازاوستا ‪( 2۳1101‬تخمه؛نژاد)«بارتولمه ‪)۷۸۵‬پارسی باستان ‪( 871101-‬نوع‪.‬اصل)‬
  ‫‪« _ ۲‬خمانی ‪ ...‬ملقب بشهر آزاد»‬                       ‫اسشق و هوبدمان ‪۳‬‬             ‫ور که‬        ‫ص‪۰۷۱‬‬       ‫«اسفا ‪۱:۲‬‬

  ‫«طبری حص‪٠٤۲‬‏ دریپلوی )‪)011]- 262‬دیوستی‪.‬بندهش ‪»۲۲۱‬شاهنامه«چهرزاد» «فهرست ولف»‪:‬‬
           ‫و‪۲٩‬؟‪.‬‏‬    ‫التواریخ والقصص ‪» 6‬ور ‪۳ :‬‬             ‫«یادشاهی همای چهر آزاد سی سال بود“ «محمل‬

  ‫[ك ‪:‬گاه ]‪ .‬توایی از موسیقی ابرانی » معرب آن‬
                                            ‫چ‪#‬هارگاه _ بفتح اول و دوم ر‬
                                                                           ‫‪.‬‬        ‫«حهار گاء» «دزی ج ص‪۲۲‬‬
  ‫کن هفتم ( لپجهٌ مر کزی )‪ .‬بهلوی‬                     ‫چهار شنبه ‪ -‬بفتح اول و دوم و پنجم‬
  ‫‪« ۲2018۰‬منای ‪ , ۰۷۲۰‬کیلکر ‪7286 200۳۲8115‬؛ روز پنجم از ابام‌هفتةٌ ملمانان‪.‬‬                                       ‫‪۸‬‬

  ‫* چهارم ‪ -‬بفتح اول وضم راء از ‪ :‬چپار ‪ +‬ام ( سوند عدد )‪ .‬پهلوی ‪011۲0۵20‬‬
     ‫ما ‪۲٩ : ۱۳۱‬‏ با ‪« 00۵6۲20120‬مدای ‪ ۰۷۲‬؛ عدد ترتیبی برای چهار ‪ ,‬درمرئبةٌ چهار ‪.‬‬
  ‫‪ #‬چهل ‪ -‬بکراول‪ ,‬دوم بهلوی ‪« 100‬مسینا ‪ ۰ ۲۳۱‬دارسی‌باستان‪ ,‬ازلا‪820 )70‬‬
  ‫پارسی بامتان_ ‪ , 1۵00۳۷5۳0120‬اوستا ‪.259۳2۷۷0126,]-‬هندی‌باستانی ]‪ « 891۲2۷020‬اسفا ‪: ۱‬‬
                                 ‫‪۲‬ص ‪۷۵,۳٩۲‬‏ مضفف آن‌چل ؛ عدد اصلی چپار برابر ده ؛سی‌بعلاوه ده ‪.‬‬

===== leaf 133
                                                                                                     ‫‪7-۷‬‬


  ‫چهر ه شدن ‪ -‬کناءه ابزرخاستن‬                                  ‫ووی‬
                                                                 ‫چهر ه ‪ -‬یکسر اول » صورت ر‬
                       ‫بمنازعت باشد ‪3.‬‬                          ‫ضم اول ير سادة امرد‬    ‫و‬   ‫‪-‬‬   ‫‪۱‬‬     ‫باشد‬   ‫اده‌ی‬


                                                             ‫؛ویند باين معنی‬
                                                                           ‫ونو کر وملازم راتیز گفته‌اند گ‬
 ‫جهیل ‪ = ۴‬بروزن‌شهید‪ .‬ماضی‌چکیدن‬
                                                                                               ‫«ندی است ؟‪.‬‬
                                ‫چکید ‪.‬‬         ‫باشد «عنی‬
‫چهیدن ‪ ۰‬بر وزن و معنی چکیدن‬                                  ‫چهره پدرار ‪ -‬سور و مورتگر را‬
                                                   ‫باشد ‪.‬‬                                              ‫‪.‬‬    ‫فل‬




                                              ‫لبان ليست و دو یم (‪)۱‬‬


              ‫لغت و کنات‬            ‫دده‬           ‫در‬   ‫درجم فارسی با بای حطی فطل‬



 ‫چیچست "‪ ۱۰‬بکراول وجیم وسکون‬                                  ‫ثانی» مخفف‬     ‫کلوون‬
                                                                                 ‫سراو‬
                                                                                    ‫جی = بک‬
‫ثانی وسین بی‌نقطه و فوقانی » بلغت زند و پازند‬                 ‫چیز امت کهآنرایعربی شی خوانند‪ - ۴‬وچون‬
                                                              ‫درآخرکلمة ترکی افزایند بمعتی‌صانم وفاعل آن‬
         ‫‏(‪ )٤‬کوه کروابند وبعربی جبل خوانند ‪.‬‬
‫‪١١‬ے‏ «روزن همیخ شخصیرا کوبند‬
                                      ‫خ‬ ‫ی‬ ‫چ‬
                                   ‫که ازچشمهای ا‬
                                                 ‫چیز شودحمچو باشماقچی (‪ ۵ )۲‬بعنی کفش کر‬
                                                                 ‫‪۸‬‬    ‫و بالالحی (‪ ۷ )۳‬سنی دروغ گوی ‪۷‬‬
‫و پبوستهآب وچركآ بد ‪ .‬وباین‬                                   ‫چیپال ‪ -‬بابای فارسی بر وزن قیفال ‪,‬‬
               ‫سبب مکارنهایش ربخته شود ‪.‬‬                                     ‫نام بادشاه لاهور بوده است ‪. 4‬‬


          ‫(‪ )۳‬چش‪ :‬پالالچی‪.‬‬                ‫‪.‬‬      ‫(ب‪)۲‬شچمكا‪:‬قجی‬             ‫)‪ ۱‬خم ‪٩‬‏ چجك‪ :‬دوم ‪.‬‬

                                                                            ‫()چك ‪ :‬ژند وباژند ‪.‬‬

  ‫؟ ‪ -‬در اردو ‪ 2۲06‬مخفف ‪ ( 8276106‬پر ) و درترکی«جپرء»‬                          ‫‪ - ۱‬رك ‪ :‬چهر ‪.‬‬

  ‫چیز ‪.‬‬    ‫رك ‪:‬‬   ‫‪- ۴‬‬       ‫‪.‬‬    ‫یضیدن‬
                                     ‫هما‬
                                       ‫چ‪-‬‬‫‪۴‬‬                    ‫اضم اول) «معنی رندك؛ حوان‪« .‬جفتایی ‪"۰۰‬‬

  ‫‪.‬‬    ‫رك ‪ :‬بالالجی‬   ‫‪- ۱‬‬         ‫>‬           ‫است‪«.‬حفتابی‬   ‫‪ ۰‬درت رکی بمعنی کفش (‪)eladnas‬‏‬         ‫باشماق‬   ‫_‬    ‫‪۵‬‬


  ‫غزنوی معمول گردیدچنانکه‬                ‫رعهد‬
                                            ‫‪ - ۲‬این پسوند نرکی است و دلالت برورزندة کآارنی‌کنددو‬
      ‫دش‬
       ‫عنوان «اميرك سپاهدار» عهدمسمودغزنوی را « خمارچی» «یگفتند ‪ .‬رك‪ :‬تاریخ بیهقیمصحح ک‬
         ‫فاض ‪۷۲۲‬؛ درآخر کلمات غیرتر کی نز آرند همجون درشکه‌چی ‪ .‬ارابه چی » تماشاچی ‪-‬‬
                  ‫‪ - ۸‬در تپرانی و کیلکی بمعنی چه استفهامی استعمال شود ‪ .‬رك ‪ :‬چه ‪.‬‬
      ‫‪ 4‬سانسکرت ‪« 21202۷20‬زاخائو ‪ .‬ماللهند ‪ ۰4۳۰‬؛ « ملك بمده (بعدلکتورمان»‬
  ‫البراهمة سامند کثملوثم بهیم‌ثم‌جییال اثنمندپال» «تحقیق ماللهند بیرونی طبع زاخائو ص‪» ۸۰۲‬‬
                            ‫ورك ص‪ ۵4‬ورك‪ :‬دائرةالممارف اسلام (فرانند) ج ‪ ۱‬ص ‪ ۵۹۱‬ستون ‪. ۱‬‬
      ‫صهف دعرهٌ ‪۹۷٩‬‏‬
                   ‫ی‬

===== leaf 134
‫خیره ‪ ۰‬بمعنی مستولی‬            ‫زن‬
                                ‫رهو=‬
                                   ‫چبیر‬                               ‫*ر ‏ = بر وزن میرهبمعنی‌غالب‬
                                                                                                 ‫چی‬
‫ولاور را‬
       ‫جاع د‬
           ‫ش‪-‬‬‫وئد‬
               ‫شدن و تلط بافتن با‬                                     ‫شدن و ظفر یافتن و مستولی گرددن بردشمنی‬
‫‪ - ۴‬و بهندی دستاری که بر سر‬                            ‫لزیکوبند‬        ‫باشد ‪ -۴‬وشجاع ودلاور را نیز گوبند ‪ -‬وبمعنی‬
                                          ‫يبند © ‪۶ ,‬‬                  ‫حصه وبهره و اصیب هم هت ‪ - ۴‬ونام قریه‌ای‬
               ‫‪۰‬‬     ‫‪۳‬‬     ‫‪۳‬‬          ‫‪۰‬‬        ‫‪۰‬‬                                                        ‫‪۰‬‬                    ‫‪۱‬‬   ‫ازق‬   ‫ماث‬
‫چیز یز ‪ -‬بازای هوزبروزن پیش‌خیرز»‬                                                               ‫باازدفرای بونات ‪۳۱‬‬


  ‫اوسا ‏‪( )2۷۳186( cira‬زرنگک > شجاع) «بارتولمه ‪« ۸4۵‬یبر‪« »444‬منای‪«»۷: ۰۷۷‬اسفا‪:۱‬‬
                                                            ‫‪.‬‬     ‫ورك ‪ :‬چره‬      ‫‪04‬‬   ‫هوبشمان‬   ‫ورك‪ :‬اسشق‪.‬‬                   ‫‪۶۳۰‬‬       ‫ص‬

               ‫‪ - ۴‬بفاعل معین؛ معنی مصدری دارد‪ .‬و بتنهابی بمعنی غالب ومظفر است ‪:‬‬
                   ‫وز ولات خراح بردارد ‪.‬‬                                        ‫گر شود چیرو تاج بردارد‬
          ‫‪.‬‬        ‫نظامی کنجوی‪.‬ه کنجینه ‪1‬‬

                                   ‫باین معنی مصحف*تبر» ‪.‬ا لغتی است از آن ‪ .‬رك تمر ‪.‬‬                              ‫‪- ۴‬‬

  ‫در اردو چیره ‪۵۳‬آ[ (نواری که دور دستار بندند) ‪.‬‬                       ‫‪-‬‬    ‫©‬           ‫رکه ‪ :‬چیر ‪.‬‬                  ‫‪۴‬‬

 ‫اوستا‬   ‫‪YT‬‏‬       ‫ب رگز ‪.‬دن) «منای ‪۰‬‬                    ‫(چدن ‪۰‬‬      ‫جیلان ‪ -‬بقتح سوم » بهلوی ‪natîc‬‏‬

 ‫‪ . ۷ - 8880‬حندی باستانی ‪1C. 1-60‬‏ بلوچی ‪8401C‬‏ اسفا ‪۷ : ۱‬ص ‪۸۲۱۰۲۹۳٤‬‏ گیلکی‬
 ‫‪۶(8‬چیدن) ‏ تپرانی ‪021016‬؛ گرفتن میوه از درخت ‪ -‬گزبدن » انتخاب کردن ‪ -‬دانه از‬
  ‫زمین برداشتن مرغ و فروبردن ‪ -‬زدن شاخه هایکیاه‪ -‬بر بالای هم گذاشتن چیزی ‪ -‬گستردن‬
  ‫باط و متاع ‪ -‬گرفتن ناخن وستردن موی ‪« :‬نگوبی که‌دوبدن و برهنه بودن و ناخن ناچیدن‬
                         ‫قابوسنامه چاپ لقمسی ‪.‌ 6۵۱‬‬                   ‫( درمراسم‌حج) ‪«<¢‬‬     ‫تابیراستن چراست‬                      ‫و موی‬

  ‫)‪ .‬حاصل مصدرچیره‪.‬‬       ‫( مصدری‬          ‫ی‬           ‫بفتح سوم » از ‪ :‬چیرء (چیرکه) ‪+‬‬           ‫¬‬   ‫چیری‬                 ‫‪#‬‬

 ‫؛ غالب شدن ‪,‬طفر‬          ‫بد«ییر کے “‪٤٤‬‏ «مناس ‪ « 012۲66 ,۲۲ :۰۷۲‬میا ‪۲۳۱‬‬                                             ‫بهلوی ‪۷‬‬
                                                                                                    ‫‪۰‬‬           ‫ره‬   ‫عافتن ‪ ۰‬رك‪:‬‬


  ‫‪ #‬چیز ‪ -‬بپلوی ‪« 056‬منای ‪ »۰۷۲:۷‬پ=ارسی باستان ‪( 160516‬شینی) الزا‪.>0)1‬‬
 ‫افغانی ع ‪ « 2‬هوبشمان ‪ »۷۵4‬ورك‪ :‬یبر که ‪ 0‬و اسفا ‪٣ :۱‬ص‏ ‪» ۲۲۱‬گیلکی ‪ 216‬؛ شیشی»‬
 ‫هرچه موجود باشدهربودنی» امور ظاهری وباطنی‪ «:‬وچیزهاء پنهانی والهی همیشه غالب‌تر وقوی‌نر‬
                             ‫بود از چیزهاء طبیمی‌و ظاهری‪ ».‬ک«شف المحجوب سجتالی ‪.*۲۷‬‬

                                                                                                    ‫بقه از صفحهٌ ‪۵۷٩‬‏‬

  ‫حمداله مستوفی درترهة القلوب‌مقالهً‪( ۳‬چاپ لیترانج‪۱۳۳۱‬‬                              ‫نیرگ‪۰٤‬‏ ابوستی‪ .‬مندهش ‪۰‬‬
 ‫ولی‌درشاهنامة فردوسی ناسخان بغلط «خنجت »ر‪ :‬فهر ست ولف»‬                            ‫وة‬    ‫‪۷۸-۱۲- ۸-۵۸‬چصت‬                                ‫ص‬
 ‫ود وآشکده معروف «آز رکشتپ» در کار‬                                ‫ضط کرده‌اند ‪ :‬این در باچه دراظر زرتشتان مقدس‬
   ‫‪ ۰‬مصحف دییخ» («‪.‬م‪).‬‬         ‫ظ‬     ‫‪"۱‬‬            ‫‪.‬‬    ‫اشنکه درمتن بمعنی کوه گرفته ‪ ۰‬خطاس‬                  ‫ِ‬   ‫آن قرار داشت‬


 ‫‪ #‬چهلم ‪ -‬بکراولوضم سوم از‪ :‬اچمه(لب‪۳‬س‪-‬وندعددی)؛ عددتر تببی‌چهل»مر تبفچپل‪.‬‬
                                                                           ‫چهل‌منار ‪ -‬رك ‪ :‬چل مناره ‪۰‬‬                ‫‪+‬‬
```


## [2026-09-05T14:58:19.190Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; python3 $S BRT.txt \"cira-|čira-|cira\\b\" 260 14",
 "description": "Grep BRT for cira"
}
```


## [2026-09-05T14:58:20.269Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 659 660 661; do echo \"===== leaf $n (p~$((n+543)))\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt | head -60; done",
 "description": "Print BQT v2 leaves around p.1203"
}
```


### [2026-09-05T14:58:21.070Z] TOOL RESULT

```
[leaf 350] ...Bromliche Fassung  (r.  B.  bei  Sp.  Keilinachr.»  unter  (»-b-  3) falsch.  —  0  Eig.  'etwas  wenig  zaiilieicbes' ;
•  No.
;  lies  At",  s.  ^tav:
•  j.  dirya-«  Adj.  'tüchtig,  tapfer':  pqsnu^ narS  'yS  taxmS  Aog.  84-
Ob  lum  V.  'iar-y  —  np.  cira.  —  Pü,:  iär7- cärJi,  Sü,:  samgräm'imrmü^ha'i.  —  O  Stall 'hiry'  geschr,  S  268. \a\  vgl.  KZ.  36.  163.
•  j.  (Sista-  Adj.,  PPfP.:  s.  kagh:
•  j.,  g.  '(Sistay-  f.  'Denken;  Erkenntnis, Einsicht':  °ff''  ui§täis  syaokanä  ahm  spsn- vaiia...
---
[leaf 455] ...nd*:  t,l  (asmTng
dby  Google
799
Jhwya-
*raoi-
800
(sd.)   -ra  (IS.)   harS  .  .  vainahl  vUpä  Y.
Au»  ar,  *lifiihra- ').  —  ai.  vgl.  hitfum  cakiuh RV.  5.  8.  6;  s.  Bthl.  IF,  /.  49a,  10.  9.  — Pü.: /a  vimilai.  —    ■)  Das  im  Ai.  'iviccira-
•  j.  Jhvyi-  f.  'Schrecknis,  Gefahr";  avi dli  aim  . .  aihim  baräiti  "yqmÜa  Yt  10. 37 ; —  tum  .  .  ma^anam  avi  3^alpaihy/lsf tanvS  'yam  avaiaraht  Vt  10.  sj.
Zum  V.  %iiiay:
•  ].  ÖTvya^stama-  Adj.  'der  schrecklichste, furchtbarste': ...
---
[leaf 676] ... gä>a)  yä  anya  srävaydit  —  avqm  vanam  yqm  samahe  ..ya  (m\) N.  46.  0  N.-APn.:  irja  anSpirika  vaoce  7'isps.bis  nqma  yqm  (zu  I)  upairi  .. iyadhna  yä  narö.va^aya  V.i.i  i;  12,  16;  Yt.i2.17;    —  fravasim  avqm  yqm  aku-
—  vahilla  cCira..yii  slaoia  yesnyaYt.23.  rake  masda  X.26.z;  — yazaEta  ml  him i;  —  vupäca  diima  .  .  yä  asava.däia  Y.  ..yqm  ar?dflm  Yt5.i.  c)  APm.:^i> 7/.  6.  a.)  ava  bai&aza  .  .  yl  humäyehe  . . /myatät  (&d.)  *aAma  *yq  am.'sS  spmif yäi  .  .  ...
---
[leaf 788] ...A.  -äj»,;  s.  aber F  I,  J  10.  —    »)  S,  iSt  Wkst  SBE.  ^/.  480.
•  j.  tßtn  barasma  aycuaisa  . .  fraHndhwan vidinaOTwar«  .  .  frataraiibyS  (sd.)  raocä Yt/j.  55.         Ob  Adv.?
Geringe  Stelle.     Vgl.  zu  rrahaa%viari.
•  j.,  g.  vi-Cira-  Adj.  (fem.  'r3-)  i)  'ent- scheidend, die  Entscheidung  treffend':  hvS 'rS  ahurS  "er,  Ah.,  hat  die  Entscheidung" Y.  2g.  4;  —  fravasayS  .  .  yä  .  ,  ranmS vivaitTs  °ra  Yt  13.  40.  a)  'der  sich entschieden,  die  tfberzeugung,  Gewissh...
---
[leaf 958] ....tarätay-"  f.  'auf  einmal  ent- stehende Furcht,  plötzlicher  Schreck';  nur LS.  mit  dem  V.  %rak-'^:  mihr>m  . .  'la %rhi3kayeie  >a>aya  aspa.vTraja  YLiO.  loi.
')  NA.  trennt.   —   >)  S.  zVerb.  anter  ka%ra..
•  j.  t>m  pantqm  "hadraysn  h<Cira  .  . Vyt  42.
•  j.  hadra-vata-  n.  'auf  einmal,  auf  einen Schlag  erfolgender  Sieg  über  — '  (Gen.): •tahela  paiti    hamtnä^anqm    Yt  13.  133,
•  j.  haSra-vana-  Adj.  'der  auf  einen Schl^  siegt':  'na  (statt  NS.)  nama  ahmt Yt;5.46.
Zum...
---
```


### [2026-09-05T14:58:22.442Z] TOOL RESULT

```
===== leaf 659 (p~1202)
  ‫صهراب‬                                                                                       ‫‪٩‬‬      ‫‪-‬ي‪‎‬‬


                                                     ‫سه خواهران‪ *۰.‬کنابه‌ازبنات‌باشد‪.‬‬
‫تحتالی‬        ‫ن‬
              ‫وو‬‫کالك‬
                   ‫سفتح‬
                      ‫سشهر =ب‬                       ‫وآن سه ستاره است بهلوی حم از حجملهعت متارء‬
‫ورای فرشت » عمارلی بوده مشتمل‌برسه گنبد که‬           ‫بنات‌النمش که آنرا هفت اورنکه و دبا کبرلیز‬
‫نعمان‌بن منذر بجهت معبد بهرام گور ساخته بود‬                   ‫گوبند » وچهار دیگ رکه‌صور ت کرسی‬
‫و چون بزبان پهلوی کنید را دیرمیگویند آبرا‬                                                           ‫خوانند ‪.‬‬
 ‫بدان سبب سه‌دیرمیگفنه‌اندوعربان معرب ساخته‬          ‫› پمعنی‬   ‫ایجد‬   ‫دال‬
                                                                              ‫سه ذختر ‪ -‬جم‬
                 ‫سه دبر بروزن غدیر ءیخوانند ‪. ۴‬‬     ‫سه خواهران ات که کنابه ازسه سناره باشد از‬
‫وکون ثالی و رای‬
              ‫“هر ت یکر اول س‬                                                                 ‫بثات اللعش ‪.‬‬
‫قرشت کاو را میگوبند و عربان بخقويانند ‪۰‬‬              ‫سه درك = بفتح دال » بروزن ومعنی‬
‫و بعضی کوبند هر ماده کاو است ‪ - ۴‬وبفتح‌اول‬          ‫سه پرك است » وآن خطی باشد که بجهت قمار‬
‫وثالی در عربی بمعتی بیداری است که ور مقابل‬                                       ‫بازی بر زمین کشند‪* .‬‬
                                   ‫باشد ‪.‬‬   ‫خواب‬
                                                     ‫سه دوری ‏ باالت بواورسیده ورای‬
‫بضم اول ل»ام پسر رستم‬        ‫سهر اب ‪۶‬‬               ‫بی‌قطه بتحتالی کشیده ‪ ,‬بمعنی سه‪.‬جله است ‪۱‬‬
‫بهمرسیدہ‬         ‫زال است که از دختر ‪SRE‬‏‬             ‫که طول وعرض وعمق باشد وبعربی‌ابعاد تلله(‪)۱‬‬
                                                                        ‫(‪ )۱‬خم ‪ : ۳‬لت ‪۰‬‬

   ‫‪ - ۴‬جوالیقی کوبد ‪« :‬سدیر» فارسیممرب است واصل ان «سادلی»‬                  ‫‪ :‬سه جاده‪.‬‬   ‫رك‬    ‫‏‪١‬‬

   ‫است سنی ا سه قبهٌ داخلاست ومردم آیرا «سه دلی»خوانند یس معرب شده‪.‬ابویکی آرد ؛‬


   ‫وتشدیدلام مفتوح‬         ‫کور ‪۲‬‬            ‫‪:‬آن «سدلی» ‪۷‬‬

   ‫‪۸‬‬     ‫بارت‪4‬‬
         ‫بهتراست‬   ‫‪ ..‬و گفته اند « سدیره یمعتی‬   ‫‪ ۳‬و و‪eE ۳‬‏ گ*فتند ‪.‬‬                          ‫ا‬‫والف در‬
                                             ‫مرحوم قزوینی در بادداشته‬
   ‫تای خود ببررهان لوشته‌اند ‪« :‬سه‌دله وسدلی »‬                                     ‫«المعرب ‪۷۸۱-۸۸٩‬‏‬
  ‫عمارتی بود دارای سه گنبد » که ییکی دروسط بزرکتر بوده و دو درجتبین آن قدری کوچکتر که‬
   ‫‪ ۴‬ل‪-‬او کاو‬                   ‫د ر )‪.‬‬   ‫بند (صحاح ولان » در‪:‬ی‬              ‫گوشوار »‬     ‫بهاسطلاح ‪ ۶‬دو‬

                                                                                   ‫ف(پرست ولف ) ‪:‬‬
              ‫پیاورد فربه مکی ماده سهر ‪.‬‬                   ‫مهر‬        ‫رد‬
                                                                       ‫تزی‬
                                                                         ‫سه تا‬
                                                                             ‫گرشا‬
                                                                                ‫بب‬‫چو‬
   ‫د شاهنامة بخ ج ‪٩‬ص ‪6۳۷۲٩‬‏ ‪.‬‬
   ‫؛پراب ) اوصل « سکهارو »‬  ‫‪:‬رخ س‬  ‫س‬
    ‫ک(اوسرخ) ‪ ۷‬وصف تت بای ءوصوف لته ‪( « :‬آفربدون) اول خروح بکراو شت تا پادشاهی‬
  ‫نامها برحکم آنك شبالی میکردند ‪ :‬سیدد کاو ‪ ۰‬وصاه گاو ‪ .‬وسهر گاو‬               ‫بروی مقرر شد » وگ‬
  ‫افریدون بیرون آمد سلاح اوکرز بود‬            ‫یعنی سرح کاو و ماننده اين نهادند وازاین جهت چون‬
   ‫بعنی سلاح چویانان چوب بائد چون عصا و مانند آن ‪ ۰‬و سرکرز اگواو ساربود بمثال نامپا ‪» .‬‬
   ‫‪۵۲۱٩ _ ۴‬‏ = سرخاب ‪0۵5۲٩‬‏ («‪.‬م‪ , ).‬از ‪:‬‬                    ‫« فارسنامه ‪ .‬ابن البلخی ‪. ۲۱‬‬
   ‫؛ب‪+‬ممنی دارندةآب ورنگ‌سرخ (چنانکه باقوت‌باشراب )«بوستی ‪.‬‬  ‫ب‪)۰‬‬
                                                               ‫آ‪.‬م‬
                                                                 ‫‪ = ۲‬سرخ (ه‬
   ‫دام نامه ابرانی ص ‪ .»۳۱۳‬درسلله ملو که طبرستان دوتن راسرخاب ویکی راسهراب لوشته الد‬
                                                   ‫«مرزبان نامه ‪ .‬تهران ‪ . ۷۱۳۱‬مقدمه ص ‪2‬؟ ‪.‬‬
                                                   ‫= سدلي رك ‪ :‬سه در ‪.‬‬                 ‫‪¥‬ەدله‬
                                                                                           ‫س‬

===== leaf 660 (p~1203)
 ‫‪-۱۱-‬‬                                                                                                   ‫سه روح‬
‫سه غر هُدهاع = بسنی سه ابوان‬                                                          ‫بود و اورا لدانته کشت‪.‬‬

‫خیال و محل‬        ‫مرحول‬
                      ‫فک‬          ‫حهل‬
                                    ‫مت ک‬
                                       ‫دماغ اس‬             ‫سه روح = بارای قرشت بواو کشیده‬
                                  ‫حافظه باشد © ‪.‬‬           ‫و بحای حطی زده » بمعنی موالید ثلائه است که‬

‫سه غرفه هغز= پنینی سه غرفة‬                                                    ‫حیوان ولبات وحماد باشد ‪.‬‬
  ‫ل‬‫مالحو‬
       ‫دماغ است که محل فکر و محل خی‬                         ‫سه رود = با رای قرشت (‪ )۱‬بواو‬
                                    ‫حااظه باشد ‪. ۷‬‬          ‫رسیده و بدال زده » بمعذی سه‌تار است کهطنبور‬
‫اکل‪-‬ید ثلائه‌است که‌لبات‬
                       ‫زن‬‫سه فمرو‬                           ‫تساهرسته باشد ؛ و بعضی کوبند چنگ و رباب‬
                            ‫جوماد وحیوان باشد ‪.‬‬                                                   ‫و پربط است ‪.‬‬
‫سه ھانه = باکاف فارسی بالف کشیدہ‬                            ‫سهستن ‪ = ۱‬بفتح اول و سکون سین‬
 ‫»نابه از جام و پیالةً شراب خوری‬
                               ‫و فتح لون ک‬                      ‫منیقطه بروزن اهشتن» بتمرعسنیدن‌ورمیدن‌باشد‪.‬‬
                                                ‫باشد ‪.‬‬      ‫سه ستبل ؟ = بنتح سین بی قطه (‪)۷‬‬
  ‫کماف فسارکسیونولام؛‬
                    ‫سه گل ‪ -‬ن‬                               ‫و سکون لون و بای ابجد (‪ )۳‬مضموم‌بلام زده‪,‬‬
 ‫نام درختی است که‌میوءآن چون پخته شودسرخ‬                   ‫بمعنی سوستبر است » و آن سبزیی باشد میان‬
 ‫گردد و بغابت قابض باشد وآنرا بفارسی‌توت‌سه‬                 ‫پودنه و عناع زبرا که چون بودنه رادست نتان‬
 ‫کل و بعربی توث العلیق خوانند چه درخت‬                        ‫که ور شوو و افا یسار نر گونتهه‬
‫آلرا عربان علیق گوبند » وتوث وحشی لیزهمان‬                   ‫سه شاخ ‪ -‬با شن قرعت (‪ )4‬بالف‬
                                 ‫اع ‪: ۷‬‬                         ‫کشنده وبخای نقطه‌دار (ه) زده » بمعنی‌سهروح‬
‫سه "نید ان ‪ -‬عبارت از قلمهةٌ سنگوان‬                         ‫اهبه از موالید ثلائه باثد وآن حیوان‬‫اکستن ک‬
 ‫است که در شبراز بپیدان مشهور است وآن سه‬                                          ‫ولبات وجماد است ‪. ۴‬‬
‫قلمه بوده که در آنجا جمشند ساخته امت ‪ :‬اول‬                 ‫از تاربکی صلب‬           ‫یه‬
                                                                                    ‫به ظکلمنتا‪-‬‬
 ‫استخر ودوم قلعةٌ شکته و سوم قلمه حتگوان‪:‬‬                       ‫پدر و تاریکی شکم و تاریکی زهدان مادراست‬
                                                                            ‫وآ را سه ظلمات هممیگویند ‪۲ ۴‬‬
‫بوزیکصد و چهل ستون برسر پشته برآورده‬
‫شصت گر بنیاد کرده‬
                ‫و کوشکی بطول نکصد و‬                        ‫سه علم کناب ازعلمالهی و طبیعی‬
  ‫بود که! کنون آثارآ ارا چپل ستون خوانند ‪. ۸‬‬                                                      ‫و ریاضی باشد‪.‬‬
                                            ‫‪.‬‬   ‫بى نقطه‬   ‫‪- :‬‬    ‫چك‬   ‫(‪)۲‬‬         ‫(‪ )۱‬چك ‪ :‬بارا ‪.‬‬
                 ‫‪ :‬وبا‪۰ ‎‬‬    ‫چك‬   ‫)‪(e‬‬            ‫(‪ )4‬چك‪ - :‬فرشت ‪.‬‬                  ‫‪ :‬وبا ‪.‬‬   ‫چك‬   ‫(‪)۳‬‬



   ‫‪ - ۱‬يهلرى ‪ 720591135‬به‌عنی بنظر آمدن » ظاهر شدن ‪ .‬هزواری آن (‪2)010221‬‬
  ‫_‪( 69‬امراست‌بممنی بنگرودقت کن)‪.‬‬
                                ‫‏‪* —mûnistan‬بونکر ‪« ۵۱۱‬اوتوالا ‪.»۰۵٩‬درنهرانی‏ ‪0 65‬‬
  ‫آلنی م رکب ازدسته‌ای چو من دارای‌سه شاخه‬                ‫‪ - ۴‬و‬              ‫رکه‪ :‬سی سنیر ‪۰‬‬        ‫‪ ۱‬؟ ‏‬

   ‫‏‪ e‬سرك‪:‬مه‌ابواندماغ»‬        ‫فلزی را کونند که بدان غلدرا بدارهند ‪.‬‏ ‪_ ۴‬رك ‪ :‬طلمات ثلاثه ‪.‬‬
   ‫‪ub‬‏ ‪uR‬‬       ‫‪ = ۷‬تمشك =‬              ‫‪٩‬‏‪ -‬ر‪:‬سه ابوان دماغ » سهغرف دماغ ‪.‬‬                    ‫سرهفةٌ مغز ‪.‬‬
                                                                                                         ‫غ‬
   ‫درمبان هر‬     ‫‪ ۰.‬ومیه‌فلعهساخت‬       ‫اه ماخ" باری رادار الملك ساخت‬        ‫‪(۱- ۸‬جمشد)‬           ‫ی اتی ‪+۰‬‬


  ‫» برفلعةٌ‬   ‫سوم قلمةٌ شکنوان‬      ‫» دوم قلعةٌ ‪EEE‬‏‬            ‫یکی قلعةٌ اصطخر‬   ‫وآ را سهکنبدان نام لهاد ‪:‬‬

  ‫اصطخر خزاله داشتی و بر شکته فراش‌خاله واساب آن * ویر شکنوان زرادخانه‪ (».‬وقارسامه ‪۰‬‬

                                                                            ‫ابن البلخی ‪ ۱۲۱ ۰ ۲۳‬و ‪٩۵۱٩‬‏ ‪.‬‬

===== leaf 661 (p~1204)
                                                                                    ‫‪-۱۱۹۷-‬‬


‫سه لو بت ه کنابه از ابامکود کی وایام‬              ‫گهوهاث ‏ باکان وهای هوز بر‬
                                                                           ‫س‬
 ‫ازنپجدواشراق‬    ‫بوه‬
                   ‫ا‪-‬‬‫ناشد‬
                        ‫کی‌ب‬
                           ‫اانییاوم بدر‬
                                      ‫وزن چه‌خويك » بمعنی خارخسك‌است‪,‬و آن خاری أ جو‬
 ‫همست ‪-‬ولوبت نواختن را لز گویند‬     ‫وچاشت ه‬                                       ‫گهوشه ‪-‬‬
                                                                                        ‫اشد م‬
  ‫نی نقاره زدن چه‌در قدیم سه لوفوتبت‌مینواخته‬
                                ‫راا‬         ‫‪۱‬‬      ‫سهل ‪ -‬بفتح اول و سکون انی ولام »‬
‫منا“صتحجر‬
        ‫وضع درد و در راما‬         ‫قفا و ‪٢‬‏فو‬         ‫ا ا ‪۱٩‬‏‬        ‫‪۱‬‬      ‫زر مان باشد؟‬
            ‫‪1‬‬     ‫‪۱‬‬        ‫‪.‬‬   ‫مر ی‬    ‫است ‪. | - ۲‬‬            ‫ار‬
                                                               ‫وابل‬
                                                                  ‫شمق‬
                                                                    ‫ددر‬
                                                                      ‫بمعنی اسان باشد که‬
         ‫ينج وقت شد وینج لومت شهرت بافت‪.‬‬
                                                                  ‫‪.‬‬      ‫ونام وزیر هامان هسمت ‏‬
  ‫درست‬
     ‫= بر وزن صفی » راست و‬             ‫سی‬
‫راگویند عموما ‪ -‬وهر چیز راست رسته راخوانند‬         ‫تری‬   ‫‪۰‬معنتی‬
                                                              ‫وهم ب‬      ‫سهم = بر وزن‬

‫خصوصا © ‪ -‬و بمعنی ‪:‬زه و لوچه و لوجوان هم‬           ‫یکان دار را‬
                                                             ‫و در عربی تپیر‬        ‫باشد ‪۴‬‬    ‫وم‬
                                   ‫‪۳‬‬   ‫آهده است‬                                         ‫کوبند ‪.‬٭‬
‫د هْنح اول وئانی بتحتانی رسده‬     ‫سیت‬              ‫ه بر وزن سمند ‪ ۰‬کوهی اعت‬         ‫سهنك‬
            ‫عالی را گویند‬   ‫مفوفانی زده ‪ ۰‬عمارت‬    ‫مشپور در ولایت آذرایجان تزدیك بتبریز ‪ ۴‬؛‬


                                       ‫بیان لست و جهارم‬

       ‫ات و‬
      ‫یت‬      ‫درسین بی نقطه بابای حطی مشتمل بریکصد وینجاه وش‬
          ‫کشنلغ‬
‫روایند و بعربی حجر خوانشد ‪ -‬و بکسر اول‬
                                     ‫گ‬               ‫ن»‬
                                                    ‫گك‬ ‫اول وسکون اسنی‬          ‫یت»ح‬
                                                                                  ‫ف‬ ‫س‬

                                         ‫است ‪ .‬رك ‪ :‬منتهی الارب و فاموس ‪.‬‬    ‫‪-‬یی‬
                                                                               ‫عر‬‫‪۱‬‬
  ‫‪ - ۴‬بهلوی ‪ ( 0۳1125‬تریس ‪ ,‬وحشت ) از ‪ 71۵5‬؛‬                 ‫رك ‪ :‬منتهی الارب ‪-‬‬     ‫‪۴‬‬
   ‫پارسی استان ‪ 0210-01122-‬٭ = ایرانی باستان ‪ )8۳217-52۲0-‬٭ ‪ 0735,‬از پارسی‬
  ‫=برانی باستان ‪ = 881۳-0126‬ایرای با‪-‬تان ‪_nam_harbt‬‏ * از‬ ‫باستان ‪aÇ ۳2۱۲‬‏ ٭ ا‬
  ‫‏‪ , th rah -‬یبابرآ ‪ ( -1۳25‬ندبزرل ‪ ,‬ندیسرت ) كر[ ‪] :‬ندسرت كر ‪:‬بینركگ كرو؛‪: ۱۹۹‬‬
  ‫‪ - ۴‬کوه تش فشانی قدیمی در ‪۰٩‬‏ کلومتری دریاچه ارمیه ‪.‬‬                   ‫نا که ‪.‬‬
                                                                               ‫م»‬‫هین‬
                                                                                   ‫سمگ‬
                                                                                     ‫سه‬
   ‫ونوب شرقی برشته‌ای موسوم به‌سهند محدود‬
                                        ‫دهانةٌ آش‌فشالی آن‌کاملا واضح است و ازجنوب ج‬
  ‫میشود که سهقله مرتفع آن در روی خطی ‪ ۰‬تا ‪ ۲۱‬کیلو مثر واقم شده و قلۀ مرکزی آن‬
                     ‫‪-‬‏ ‪.‬‬
                        ‫بارتفاع ‪ ۶۰۷۳‬متر است ‪ .‬رك ‪ :‬جفرافیای طبیعی ‪ .‬کیهان ‪ .‬ص ‪٩ ۸۵‬‬
```


## [2026-09-05T14:58:46.577Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; python3 $S BQT_v2_pages.txt \"سیخ\" 300 12",
 "description": "Grep BQT v2 for سیخ"
}
```


### [2026-09-05T14:58:48.419Z] TOOL RESULT

```
[leaf 68] ...            ‫چار دوال‪ -‬بنتح‌ارل وواوبالف کشید‪.‬‬
                                          ‫‪۰‬‬   ‫هت‬   ‫«م‬
                                                           ‫و بلام زده » چوبی باشد بمقدار بك فبشه که‬
‫چارطاق » باطای حطیبالفکشید‪.‬‬                                 ‫چاروا داران برسرآن سیخی کوچك بقدره‌همیزی‬
‫وبقاف زده » معروف است ‪ - ۷‬ولوعی از خیمةٌ‬                     ‫نصب لمایند وزنجیری با چند حلقه وچهار تمه‬
 ‫چهار کوشه هم هت که آنرا در عراق شروالی‬                     ‫بآرن تعبیه کنند والاغ وچاروا را بدان برانند‪.‬‬


                                                           ...
---
[leaf 114] ...ه‌اند و آن‌باین شکل‌است ‪۳‬‬      ‫ونی بواو‬‫چلو چوب ‪ .‬بفتح اول ا‬
                     ‫و آبرا تر‪-‬ابان اطزلا و نقره‬          ‫بواوی‬
                                                              ‫کشیده و ضم جیم فارسی و سکون وا‬
                     ‫سازند و بجهت تیمن و تبرك‬         ‫ابجد ‪ ,‬سیخ کباب راکوبند ‪ » ۴‬و نم اول هم‬
                     ‫بر گردن آویزند ؛ و بعضی‬                                                ‫گنتهاند ‪.‬‬
      ‫چلیپا‬              ‫کونند سه کوشه ای بداشکه‬        ‫چلو ك ‪ » ۳‬بفتح اول وثانی وواووکاف»‬
                                                            ...
---
[leaf 334] ...زن‌بلیل‪,‬‬
                                  ‫ل‬
                                                                               ‫حزمل باشد دود کنند همه بگریز ند ‪4‬‬
                                                                                                               ‫ا‬
 ‫ءمروف‌است ‪- ۴‬وسیخولرانیز گونند‪ .‬وآن‌نوعی‬
               ‫د‬                        ‫باشد‬           ‫ازخاریدت‬         ‫د لیذ یر= با بای فاری وذال نقطه‌دار‬
                                        ‫ھ ای‬           ‫خار‬   ‫که‬         ‫مروزن بی‌نظیر ؛ بمعنی دلاویز است که مطلوب‬
                                   ...
---
[leaf 335] ...نرسیده باشد عموماً ‪ -‬ونخودخام‬
                           ‫ومحتاله وجامهیشمینه‬      ‫اف باشد ‪ -‬و هرغل ناری که آنرا‬      ‫کغهلدر‬
                           ‫وخرفه ومرفع‌درویشان‬                               ‫يوان کننف خضوضا ‪-‬‬
                           ‫را فيز گوند که از‬        ‫‪۵‬ه ‪ ۲‬سیختح‌اول وثانی وثالك » شهری‬
                                                                                    ‫ل‬
              ‫دله‬           ‫آن پشمپیا آوخته‬         ‫که سدازمابه زدن بسته شود وضم‌اول وسکون‬
‫باشد ‪ -‬وبا ثانی مشدد » بمعنیمکر وحیله وعلر‬          ‫ثانی‌جادوریاست زهردارشبیه بعنکب...
---
[leaf 448] ...عآفتاب‬
                          ‫ی‬                     ‫است درهندوستان شیه بفادق لیکن‬
                                                                              ‫بار درختی‬

                                                 ‫کوچکتر ازآن باشد ‪.‬آنرا درآب کنند و دست‬
 ‫ریخ ‪ = ۲‬بکر اول بر وزن سیخ ‪۰‬‬                    ‫اهب کف کروی ولان رها‬
                          ‫له انان ح‬
‫ویوانات دیگر که روان و آبکی‬                                                 ‫ابرشمینه بدان شویند ‪.‬‬
                                      ‫باشد ‪.‬‬    ‫ر تیانج ‪ ۰ ۴‬باتستالی و جیم بروزن‬
 ‫ر یخی ‪ - ۸‬بروزن ب...
---
[leaf 457] ...                                                         ‫ردم‬
                                                                    ‫بم‬‫راذمر د ‪ = ۴‬با‬
 ‫راد هر یح = کنابه از آهن ات‬                           ‫آزاد مرد است که جوان مرد و کریم‬                                       ‫مخفف‬
 ‫که ازان سیخ ومیخ وزنجیر وامثال آن‌سازند‪.‬‬                                                   ‫باشد ‪.٩‬‏‬           ‫همت‬        ‫صاحب‬
                                                                                                                             ‫و‬
 ‫داد س بروزن لار‪ .‬بمعنی مکان روبیدن‬      ...
---
[leaf 497] ...                                                         ‫زرفج د بفتح اول وسکون الیو جیم‪.‬‬
                                                                   ‫و نخر‬            ‫بمعنی گریه و لوحه کردن است ‪۱‬‬
                                                                   ‫ولاخ رایزکوبند کهرعکسیخ‌باشد ‪ -‬و کرهی‬
                                                                    ‫برمی آید ‪ -‬ویم اول‪,‬چانه‬               ‫که از تنه درخت‬

                                                                   ‫‌بعخربویانند ‪- ۴‬ومطلق‬  ‫نو‬  ‫ذوب‬
                                              ...
---
[leaf 543] ...باشد‬
                  ‫شوم فدم و دامبارك پی باشد‪.‬‬       ‫روشنامی جشم را زیاده کند وه رکه ماخود دارد‬

                                                                           ‫آزچشم زخم ایمن گردد‪.‬‬
‫سبز باع ‪ -‬کنابه از تن و بدن آدمی‬
‫کنابه از آسمان هم‌هست ‪ -‬وبهشت را‬                   ‫سیخ = بکر اون وفتح‌ثالی‌وسگون‌خای‬
                                    ‫باشد ‪ -‬و‬
                                  ‫یگوزبند ‪.‬‬        ‫لبك را گونند مطلقاً خواه درآ دمی‌باشد‬      ‫شطمار‪,‬‬

‫سبز بال ‪ -‬بروزن قحط سال ‪ .‬نام نوعی‬                                                ‫در طعام ‪#.‬‬     ...
---
[leaf 608] ...ند ‪ -‬و شخصی را اکیوزبند که کوش او‬
                     ‫چشم زخم در آتش ریزند ‪.‬‬                  ‫سوراخ باشد ‪ -‬وکنابه از فرمان‌بردار و قبول‬
 ‫بطم اول و ثالی وسکون رای‬              ‫سفر ‪۲‬‬                     ‫‪.‬‬   ‫وغلام هم هست ‪۴‬‬        ‫کننده وه‌طیم وتابع ‪-‬‬

 ‫فرشت (‪ * )۱‬بمعنی سیخول است که خارپشت‬
‫بزرکے باشد ؛ و بفتح الی همگفته‌اند و صاحب‬                    ‫سفتین ‪ = ۴‬بکر اول و فوقالی بروزن‬
‫موبدالفضلا میگوبند که ابن لفت سفر باغین‬
                                                              ‫مسکین » نام ولایتی است از نکرستان منوب‬
                                     ...
---
[leaf 641] ... ریزه‬
           ‫و با واو مجپول هم بنظرآمده است‪.‬‬                       ‫میخورد و بعربی قطة خوالند‪.‬‬
‫سنگر ‪ ۴‬ه بنتحاول وضمثالكوسکون‬                    ‫سنگ خاورج ‪(۱‬ا‪۱‬ج برزن‬
                                                ‫موعنی سنکه خوارك است کاهسفرود باشد ‪,‬‬
‫انی و رای قرشت » بمعتی سیخول است کهخار‬
 ‫بشت تر انداز باشد بعنی خارهای خود را چون‬       ‫و آن جالوری است کوچك و سیاه رنگه برابر‬
                               ‫تبرالدازو ‪5 ۴‬‬    ‫بگنجشك و چند پرمثل شاخی برسردارد وعربان‬
‫سنگ ر آه شدن «کنابه‌ازمادم شدن‬                                                  ‫قطاة گویندش ‪.‬‬
 ...
---
[leaf 667] ...  ‫ی‬                                                                                                ‫ات‪۷‬‬
                                                                                                     ‫‪۳۵‬‬

‫سیخگاه یافقن ‪ -‬مراد از آست که‬                                 ‫مهيا ساختن وترئیب دادن کاری باشد ‪.‬‬
‫کی بداندکه بچه‌چیز شخصی را ازجامیتوان‬                 ‫سیچیده ‪ - ۱‬بروزن پیچیده ‪.‬بمعنی‬
‫درآورد » وآن شخص بچه چیز از جا درمیآید‪.‬‬                                         ‫مدا ساخته وآرامته باش...
---
[leaf 667] ...               ‫مدا ساخته وآرامته باشد‪.‬‬
‫سیتحول ‪ = ۴‬بروزن بی‌پول ‪ ۰‬خاریشت‬                      ‫سیحون ‪ = ۲‬بر وزن جبحون ‪ ۰‬نام‬
‫کلالبرا کوبند که خارهای ابلق دارد ومانشدتیر‬            ‫رودخاله ایست در ماوراء النهر زديك بخجند‪#.‬‬
                                           ‫اندازد ‪.‬‬   ‫سیخ لر = با بای فارسی بروزن بیشتره‬
‫”یر = بکر اول وسکون ثانی مجپول‬                        ‫به جانوران برنده راگونند که هنوز پرایشان‬
                                                      ‫در اظر لماید‬    ‫بر لیامده ‪,‬اشد و مانند خاری‬     ‫خوب‬
‫ورای قرشت )‪ ۰ (۱‬معروفت ‪ ۵‬که‌تقیض کرسنه‬
         ...
---
```


## [2026-09-05T14:58:55.378Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 666 667; do echo \"===== leaf $n\"; awk -v N=$((n+1)) 'BEGIN{RS=\"\\f\"} NR==N' BQT_v2_pages.txt; done",
 "description": "Print BQT leaves 666-667"
}
```


### [2026-09-05T14:58:57.339Z] TOOL RESULT

```
===== leaf 666
   ‫—‬       ‫شا‬                                                                                   ‫سسموبه‬

‫وبتحتالی زده ‪ ۰‬چیزیت از اسرون‌آلات کومفند‬                  ‫ابن لفت هم درمجمع‌الفری سروری‌بمعتی‌اسیفول‬
                      ‫وغیره که با شکنبه میباشد ‪.‬‬                 ‫آمده است وآلرا بعربی بزرفطونا نامند‪.‬‬
‫سيج = بفتح اول وسکون ثانی و جیم »‬                          ‫سیبو له = بفتح بای حطی‪,‬مخفف سیب‬
   ‫‪۳‬‬                         ‫بمعنی مویز استو‬             ‫بوبه أست که بوی سیب باشد ‪ -‬و بفتح واو نام‬
 ‫و بکسر اول پمعنی رنج و محنت و مشقت ‪- ۴‬‬                    ‫‪.‬وبند چون هردورخارة‬
                                                                             ‫فاضلی‌است مشهور ‪ ۱‬گ‬
‫و باجیم فارسی همباین معنی وهم بمعنی ترتیب‬                 ‫ابورنکه و ضیا مانند دو سیب بود نا بر امن‬
  ‫دادن و ساز کردن ومپیا ساختن‌کاری باشد ‪۰ ۵‬‬                ‫ونساموم کشت ‪ ۲‬و بعضی کوبند ایلنفت‬
                                                                                           ‫مین‬
                                                                                             ‫با‬
‫سیحقنه ‪ - ۷‬با اول بثالی رسیده وضم‬                                                            ‫عربی است ‪۰‬‬
 ‫جيم فارسی" وفتح غین لشقطه‌دار (‪ )۲‬ونون ؛یمعنی‬             ‫بای ابجد (‪ )۱‬بر وزن‬     ‫سیییا ه بکر‬
 ‫باشه باشد » وآن یرلده‌امت شکاری ازجنس‌زرد‬                 ‫سرباای نوعی از ماهی باشد ‪۴‬‬        ‫لغ»ت‬
                                                                                                ‫بمیا‬
                                                                                                   ‫کی‬
‫وبمعنی صعوه هم‌آهده است ؛ و بفتح‬            ‫چشم ‪- ۷‬‬        ‫در لاحیةٌ بیت‌المقدس و در بعضی ازسواحل‌مفرب‬
                              ‫م فارسی همگفته‌اند ‪.‬‬
                                                 ‫یم‬‫جی‬                                        ‫یز مت‪.‬‬
 ‫» یمعنی‬    ‫بروزن چهد ود‌ن‬    ‫‌‬   ‫‪۸‬‬   ‫سیجیدن‬               ‫ه با فوقانی بواو کشیده‬         ‫وی‬
                                                                                           ‫سی‬
                                           ‫قطه دار ‪.‬‬     ‫(‪ )۲‬چك‪-:‬‬             ‫(‪ )۱‬چك ‪ :‬بکریا‪.‬‬

    ‫ا‪-‬بوبشر عمرو بن عثمان بن فنبره (با) أبن قنبر فارسی بیضاوی وسپی عرأفی بصری‬
    ‫سیبویه»‬      ‫ا«ب‬
                   ‫ت‪.‬و‬
                     ‫ک‪ ۶‬ه‬
                        ‫بال ‪ ۲۹۱‬وبقولی ‪۸۱‬‬               ‫تزووفی‬
                                                             ‫مرا‬
                                                               ‫متولد دریضاء ازقرای شی‬           ‫ی‬
                                  ‫مشپور به«الکتاب »> درتحو آزوست ‪ ۶‬ممجم المطبوعات ج‪ ۱‬ستون *‪.۷۶۱‬‬
    ‫منه‬     ‫‪۴‬‏ ‪١ -‬سيبوبه لفقابرسی » معناه بالعريية رائحة الفاح و فيل كیانشم‬
   ‫اما‬      ‫رائحة‌الطب بذلك سمی‪ .‬وقیل‪ .‬كان بعتادشم الفاح ‪٩‬‏ « ممجم المطبوعات ح ‪ ۲‬ستون ‪۰۷۰۱۰‬‬
   ‫قلبول نداردو کوید ‪ :‬رهکز این‌ککمه را بداب“ مشدد تلفظ نکرده‌اند‬   ‫‪ ۴.‬اریناقو‬     ‫‪7‬‬
      ‫ش‪8‬د‬ ‫‪0۰ ۶‬‬‫بدا‬‫و پیب مشابپت این نامباعد بسیار از ناءهای ابرالی قدیم ‪ ,‬هجای آخرکلمه باب‬
    ‫وبنابراین باحتمال اقوی موان کت که لفط کلمه ‪ 66588‬ات وآن اصطلاحی محبت آمیز بود‬
                                             ‫بمشی قسیب كوچك» ‪ .‬رك ‪ :‬داثرةالمعارف اسلام ‪ :‬سیجوبهی‪.‬‬
    ‫‪ - ۴‬سیجمند بمعتی دارنده رنج ‪۰‬‬                  ‫‪ ( 600۵5‬فر ) « لك ‪ ۲‬ص ‪۱۱۳٩‬‏ ‪.‬‬          ‫‪= ۴‬‬
                                                                                    ‫‪:‬‬    ‫نوت‬‫حنج‬
                                                                                              ‫مل ر‬
                                                                                                 ‫مح‬
                    ‫که او را پیشه باشد بیوفائی‪.‬‬                     ‫جهان سدجه‌ند ویر انائی‬
         ‫‪۵‬ا*ص‪.‬‬
             ‫زرتشت بهرام «ار‪.‬داوبر افنامه چاپ جاماس اس‬
    ‫‪ - ۱‬فرهنگه نظام بنقل از فرهنکه ت رکی اطفری‬                            ‫‪.‬‬      ‫جكی‪:‬دن‬
                                                                                      ‫س ر‬
                                                                                        ‫‪۵‬‬
                                                       ‫«سجیلفنه» را بمعنی کلنکه آورده کهشکاری نیست‪.‬‬
                ‫از دبدة صحفنه کند دانه مهیا‪.‬‬              ‫ادره عدلی که زاصاف نو نبهو‬     ‫ای‬
                                                                                          ‫‪۷‬‬
         ‫ع«میجد لهوباکنیگ‪.‬یری»‪.‬‬
    ‫؛ بهلوی ‪natîcês‬‏‬          ‫مسدری )‬       ‫ند‬
                                             ‫پنو(‬
                                                ‫=یج ‪ +‬بد‬
                                                       ‫‪۸‬یتچیمدد‪1‬ن از س‪:‬يج س‬
                                                                          ‫س‬
    ‫‪, 6 6*50‬‬
           ‫«وادیا ‪ ۵۹۱4۰‬استاد هئینکه پس از کر « پسیچیدن » و ارتباط آن بساغدی _‬
                                                                             ‫تا‬
   ‫_ ‪ 085620‬از ‪٩ 212025120 -‬‏ کوید ل‪:‬ازم است بادآور شوبم که « سیجیدن » ازنحلیل غلط‬
                                      ‫تلفط خطای سیچ ‪cêsib -‬‏ ناشی شده و درحقیفت وجود نداشته است‬
    ‫‏‪Henning , Sogdian loan - words...,BSOS.,X.1,p.104.‬‬

===== leaf 667
  ‫ی‬                                                                                                ‫ات‪۷‬‬
                                                                                                     ‫‪۳۵‬‬

‫سیخگاه یافقن ‪ -‬مراد از آست که‬                                 ‫مهيا ساختن وترئیب دادن کاری باشد ‪.‬‬
‫کی بداندکه بچه‌چیز شخصی را ازجامیتوان‬                 ‫سیچیده ‪ - ۱‬بروزن پیچیده ‪.‬بمعنی‬
‫درآورد » وآن شخص بچه چیز از جا درمیآید‪.‬‬                                         ‫مدا ساخته وآرامته باشد‪.‬‬
‫سیتحول ‪ = ۴‬بروزن بی‌پول ‪ ۰‬خاریشت‬                      ‫سیحون ‪ = ۲‬بر وزن جبحون ‪ ۰‬نام‬
‫کلالبرا کوبند که خارهای ابلق دارد ومانشدتیر‬            ‫رودخاله ایست در ماوراء النهر زديك بخجند‪#.‬‬
                                           ‫اندازد ‪.‬‬   ‫سیخ لر = با بای فارسی بروزن بیشتره‬
‫”یر = بکر اول وسکون ثانی مجپول‬                        ‫به جانوران برنده راگونند که هنوز پرایشان‬
                                                      ‫در اظر لماید‬    ‫بر لیامده ‪,‬اشد و مانند خاری‬     ‫خوب‬
‫ورای قرشت )‪ ۰ (۱‬معروفت ‪ ۵‬که‌تقیض کرسنه‬
                                                                               ‫است‪».‬‬   ‫گو بشد ی سیخ پرشده‬
‫باشد ‪٩‬‏ ‪ -‬و وزلی هم هست معین ‪ ۷‬و آن در‬
 ‫خراسان پانزده متقال است ‪ - ۸‬و نام شهری‬               ‫چپار قطعه‬   ‫‪,‬‬   ‫بر وزن مخك‬             ‫سخك‬


‫‪ -‬بثاالی معروف «مشهور‬
                    ‫مودینه ای باشد ‪٩‬‏ و‬               ‫کر در سیخ کذیده کباب کنند؟ ‪ ۹‬و مصفر‬


‫است که برادر پیازباشد وبعربی وم خوانند*‪- ۷‬‬                                                         ‫هم‬
                                                                                 ‫(‪ )۱‬چك ‪ :‬ورا‬


          ‫ح‬
          ‫جم‪+‬‬
            ‫رع باج‬
                 ‫‪ ۲‬داتین اس درات‬
  ‫بعث سمرقند «معج‌البلدان ‪.‬‬       ‫‪ ¢‬است که لپری است بز رکه بماور االنهر ترديك خجنده‬                ‫ی صحون‬

                                                                                              ‫سیر دربا ‪۰‬‬

                                            ‫ب کوهی خوش او‬
                                                        ‫زوبم‬
                                                           ‫خك چه بک‬
                                                                  ‫يرح‬
                                                                    ‫‪۴‬س‪ -‬ش‬
              ‫هشبار‪.‬‬   ‫کا‬   ‫من شدم مت و شته استت‬
   ‫)‪.‬‬     ‫ص‬     ‫«دبوان‌بحق اطممه شبرازی‪.‬چاب استالبرل ‪۳‬‬

 ‫زیا کی‬       ‫‪rês‬‏ یبر کت ‪,O‬‏‬     ‫هلوی‬
                                     ‫=‬          ‫‪۵‬‬
                             ‫‪ :‬سصمرشدن‪:‬‬         ‫ك‬
                                                ‫ر‪-‬‬‫‪۱‬‬          ‫( راضی » خشنود ) «گربرسن ‪۹‬‬                ‫‪۲‬‬
          ‫ستآنکه بنزديك تو زشت‌است‬                          ‫ای سیرترا نان جوین خوش تنماید‬
  ‫«کلتان ‪.» ۸۲‬‬
                  ‫‪٩۱‬‏ مثقال احت‬     ‫ان‬
                                     ‫ر در‬
                                        ‫هون‬
                                          ‫ت‪۱‬کن‬
                                             ‫‪-‬‬                        ‫ر‬    ‫‪۵‬‬     ‫و‬      ‫رگ‬    ‫‪۲‬‬


  ‫‪ ۶‬سیر » بفتح اول و دوم تود ریگی بین مدیشه وبدر «معجم‌البلدان» و «سیر)بفتح‬                   ‫‏‪٩‬‬
          ‫در مشرق جرد « معجم‌البلدان» ‪ ۶‬و« سبردربا “ رود صیحون را گوبنی‬                ‫اول » شهری درمن‬

   ‫‪6۰۲۱‬‬       ‫حرةً‬
                 ‫فد‬‫صبه‬
                     ‫مق‬
   ‫‪ ( 2011-‬بوك ‪ ,‬یس ) ‪ .‬کردی ‪075. 1515‬‬   ‫‪6‬‬    ‫بكر اول ر‬   ‫‪#‬یخ‬‫س‬
   ‫() «اشسق ‪ . ۲‬افنانی ×‪« 15‬هوبشمان ‪۲۹۷٩۰‬‏ کیلکی ‪.85‬‬
                                                   ‫سأیخ‬
                                                      ‫(فتبله) ب»لوچی ‪ 5‬و‬
  ‫گوش تت را بدان کشند‬     ‫ودراز که قطعات‬
                                          ‫نیباريك‬
                                            ‫ت‬
                                                        ‫معرب «سیخ؟ ‪ ۰‬تر کی «خبش» «نفی»‪+‬قطن‬
                                                                                  ‫و کیاب کنند » بابزن ‪:‬‬
        ‫زند لشکرباش هزار مرغ بسیخ ‪.‬‬                       ‫بهپنج هیضه که سلطان ستم روا دارد‬
  ‫دلتان ‪٩ ۲4‬‏ ‪.‬‬
              ‫ک‬
              ‫‪-‬طعة چویینی کهبدان دهان‪.‬جوال را محکم کنند ‪ -‬هرجچیز راست وسخت ولوك لیز‪.‬‬
                                                                                   ‫ق‬
```


## [2026-09-05T14:59:12.945Z] TOOL CALL #26: Bash

```json
{
 "command": "ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ | grep -i bqt; echo ---; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null | head -30; echo ---; sed -n '1,60p' /home/sfmqrb/git/rishe/tools/ref_page.py",
 "description": "List BQT files and ref_page tool"
}
```


### [2026-09-05T14:59:13.031Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  2634275 Sep  4 14:06 BQT_alt_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb      139 Sep  4 14:06 BQT_dli_part1.txt
-rw-rw-r--  1 sfmqrb sfmqrb 26399828 Sep  4 14:06 BQT_v1_djvu.xml
-rw-rw-r--  1 sfmqrb sfmqrb  2247721 Sep  4 14:06 BQT_v1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2620060 Sep  4 14:06 BQT_v1.txt
-rw-rw-r--  1 sfmqrb sfmqrb  4339896 Sep  4 14:06 BQT_v2_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2359504 Sep  4 14:06 BQT_v2.txt
---
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
---
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


## [2026-09-05T14:59:24.910Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN leaf 1174 (p.1150)\"; awk 'BEGIN{RS=\"\\f\"} NR==1175' SYN.txt | head -50",
 "description": "Print Buck p.1150"
}
```


### [2026-09-05T14:59:26.582Z] TOOL RESULT

```
=== SYN leaf 1174 (p.1150)
. 619, without notice of Skt. vi-smi-, etc.). Walde-P. 2.686 f.
Lat. stupor ‘numbness’ also ‘astonish- ment’ (> It. stupore ‘astonishment’, as sometimes Fr. stupeur), fr. stupére ‘be struck senseless, stunned, be astonished’ :Grk. rimrw ‘strike’, etc. Walde-P. 2.618 f. Ernout-M. 990.
It. maraviglia (orig. obj. ‘wonder’, like Fr. merveille, NE marvel, but also subj. ‘wonder, astonishment’), fr. Lat. mira- bilia ‘wonders’ : mirus, etc. (above). REW 5601.
Fr. élonnement, fr. vb. étonner ‘as- tonish’, fr. VLat. *extondre, epd. of tonare ‘thunder’. Cf. Lat. attonitus (lit. ‘thundered at’) ‘astonished’, NE thun- derstruck. REW 3092.
Fr. ébahissement, fr. ébahir ‘astonish’, OFr. esbahir, based on the expressive syllable ba. REW 851. Gamillscheg 330. Somewhat otherwise Wartburg 1.285 (: forms derived fr. VLat. batare
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
‘open the mouth’, itself ba REW 988).
Sp. pasmo, also and orig. ‘spasm’ fr late Lat. spasmus, fr. Gri. omit ‘spasm’ : ordw ‘tear, wrench’, zy 8127. ay
Rum. mirare, old infin. of y ‘wonder’, fr. Vat. mirare, (above). REW 5603.
3. Ir. machdad (usual word, both obj. and subj.) : vb. ad-machdur ‘wonder, marvel’, this perh. fr. the same root as OIr. do-for-maig ‘increases’ (: Grk. péyas ‘great’, etc. Walde-P. 2.258). Peder- sen 1.421 (2.573).
Ir. ingantas, NIr. iongantas (now the usual word for subj. ‘wonder, surprise’) ; ingnath (pl. inganta), NIr. tongnadh ‘wonderful’ and, as sb., obj. ‘wonder’, orig. ‘unknown’, neg. cpd. of gnath ‘known’ : Grk. yvwrés, Lat. ndtus, etc, ‘known’. Pedersen 1.45, 48.
W. rhyfeddod, fr. rhyfedd ‘wonderful’, epd. of rhy- ‘beyond’ and -medd ‘meas- ure’ as in dyrn-fedd ‘breadth of the hand’, etc.: Ir. med ‘scales’, atr-med ‘measure’, etc. (IE *med-, Walde-P. 2.259). Loth, RC 40.348.
W. syndod : syn ‘dazed, astonished, astonishing’, synnu ‘look, stare at’, perh. fr. *stunno-, *studno-, fr. *std- in words for ‘fixed, stiff? (ef. NHG staunen, be- low). Loth, RC 44.271 f. '
Br. sowez, prob. fr. some VLat. deriv. of subito ‘suddenly’, like the source of Fr. soudain ‘sudden’. Ernault, Dict. étym. 381, Glossaire 632.
4, Goth. sildaleik (= 64uBos Lk. 5.9); beside adj. sildaleiks ‘wonderful’ = Oo sel(d)lic, syllic id. epds. of leik, lic he form’, first part : OF seldan, OHG ex tan, etc. ‘seldom’, hence lit. ‘of rare
sed on ba;
b. mira Lat. mirary
, -P, 2.4574. Feist 421. form’. Walde-P. 2.45 Li. 438)
af-
Goth. afslaupnan (= 04pBos = infin. afslaupnan ‘be astonished’ :
oC
SespTrmse weg? a3 se
—~
: erplexed’, root con- ‘gnxious, P P. 2.709. Feist 9 f.
saupiP lde- "tio S don OHG wuntar, on un ie except Goth.,etym.? Falk-
en me Weigand: 2.1290. These 332. d orig. the obj. ‘wonder’, ds expressed tion. Thus yor aly #8 condarily emotion. and Sor ‘s wonder’, ME, NE wonder i the emotion (NED s.v. 7); OHG also mostly ‘ wonder’ (rarely subj., Bs wuntar giflang, Otfr. 3.16.5), ry . NHG wunder also of the emoti
```


## [2026-09-05T14:59:28.047Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### HUB six\"; python3 $S HUB.txt \"s[iī]x|762\" 200 8; echo; echo \"### KLN shish\"; python3 $S KLN_1966.txt \"shish\" 250 6; echo \"### KLN71 shish\"; python3 $S KLN_1971.txt \"shish\" 250 6",
 "description": "Grep HUB and Klein"
}
```


### [2026-09-05T14:59:31.177Z] TOOL RESULT

```
### HUB six
[leaf 75] ...osen, Np. Sprachfiihrer p. 26, 39: ddhdnd*Qe-
bissstiick des Ziigels ; afgh. LW. dahana fem. *the bit
of a bridle', kal dehand, dahnd etc.
593. Ich stelle -des, -dis *ahnlich' zu gr. Jaxv/t/'zeige', dsixrjXov
*Ebenbild', skr. dig 'zeigen', subst. dig *Hinweis, Art and
Weise', zd. dis Veisen', osset. dwd%8}n zeigen u. &. w.
Also doeh -dEs = zd. ^da^a-, auch wenn dies nicht
rait daesa- yt. 13, 104 (*Tr...
---
[leaf 88] ...s *saf?a-), oben Nr. 694. In der Form '^sav ist
das Wort in sassanidischer Zeit ins Armenische ge-
drungeu in dem N. pr. arm. Savars = zd. Sydvar-
saw-, phi. Siydvaxs, np. Siydvaxs, SiydvaS, Siydvid.
762. Auch das Afghanische hat six (aber hex == np. Jeir
•Wurzer).
Hierher nach Fr. Miiller, WZKM. 7, 376: np. ser
*satt* = zd. '^sairya-, gr. xo(>o^.
763. Dazu bal. LW. slBnzdah^) 'dreizehn, paz. sSzdahu...
---
[leaf 88] ...er Form '^sav ist
das Wort in sassanidischer Zeit ins Armenische ge-
drungeu in dem N. pr. arm. Savars = zd. Sydvar-
saw-, phi. Siydvaxs, np. Siydvaxs, SiydvaS, Siydvid.
762. Auch das Afghanische hat six (aber hex == np. Jeir
•Wurzer).
Hierher nach Fr. Miiller, WZKM. 7, 376: np. ser
*satt* = zd. '^sairya-, gr. xo(>o^.
763. Dazu bal. LW. slBnzdah^) 'dreizehn, paz. sSzdahum 'der
dreizehnte' Min. 61. 18...
---
[leaf 260] ...Anm. ;
xaytdan *kauen', skr. khad-, xar 'Esel* = zd. xara-, skr.
khara-; xoi, xdd 'Helm' = ap. xauda-, zd. xao^a-, SLvm.xoir;
xum, xunb *irdener Krug' == zd. xutnba-, skr. kumbha- (aus
"^khumbha-?)'^ six *Bratspiess H. 762; sax *Zweig' = skr.
Qakha- ; mex 'Pflock , Nagel' , vgl. skr. mayUkha- ; nOxun
'Nagel*, skr. nakha-, Zu xandaq *Graben' und kandan
graben siehe das oben p. 88, Nr. 869 Bemerkte.
Fi...
---
[leaf 260] ...en', skr. khad-, xar 'Esel* = zd. xara-, skr.
khara-; xoi, xdd 'Helm' = ap. xauda-, zd. xao^a-, SLvm.xoir;
xum, xunb *irdener Krug' == zd. xutnba-, skr. kumbha- (aus
"^khumbha-?)'^ six *Bratspiess H. 762; sax *Zweig' = skr.
Qakha- ; mex 'Pflock , Nagel' , vgl. skr. mayUkha- ; nOxun
'Nagel*, skr. nakha-, Zu xandaq *Graben' und kandan
graben siehe das oben p. 88, Nr. 869 Bemerkte.
Fiir ap. amaxam 'unse...
---

### KLN shish
[leaf 72] ...to  sarpere,  ‘to  cut  off,  lop,  trim’.  See  sarmentum. assart,  tr.  v.  —  OF.  essarter,  ‘to  grub  up  trees’, fr.  essart.  See  assart,  n.
assassin,  n.,  murderer.  —  F.,  fr.  It.  assassino,  fr. Arab,  hashshashln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff. ...
---
[leaf 72] ...to  cut  off,  lop,  trim’.  See  sarmentum. assart,  tr.  v.  —  OF.  essarter,  ‘to  grub  up  trees’, fr.  essart.  See  assart,  n.
assassin,  n.,  murderer.  —  F.,  fr.  It.  assassino,  fr. Arab,  hashshashln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff.  -in  in  assas...
---
[leaf 72] ...’.  See  sarmentum. assart,  tr.  v.  —  OF.  essarter,  ‘to  grub  up  trees’, fr.  essart.  See  assart,  n.
assassin,  n.,  murderer.  —  F.,  fr.  It.  assassino,  fr. Arab,  hashshashln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff.  -in  in  assassin  was mistaken  for  p...
---
[leaf 72] ...ln,  ‘drinkers  of  hashish',  fr. hashish,  ‘hemp’ ;  see  hashish.  The  first  assassins were  the  fanatic  followers  of  the  Shaykh-ul- Jabal  (the  Old  Man  of  the  Mountains),  who committed  their  murders  under  the  intoxication of  hashish.  The  plural  suff.  -in  in  assassin  was mistaken  for  part  of  the  word.  Cp.  Bedouin. Derivatives:  assassin-ate,  tr.  v.,  assassin-at- ion,  n.
assault,  n.  —  ME.  asaut,  fr.  OF.  asaut  (F.  as- saut),  fr.  VL.  *assaltus,  fr.  a...
---
[leaf 85] ...cksheesh,  backshish.  —  Variants  of  baksheesh, backward,  backwards,  adv.  —  Formed  fr.  back, adv.  (see  back,  ‘the  hinder  part  of  the  body’), and  -ward,  resp.  -wards.
Derivative:  backward,  adj. backwardation,  n.,  postponement  of  delivery ( Londo...
---
[leaf 86] ... the  ending  see  subst.  suff.  -ite. baker,  n.  —  ME.  bakere,  fr.  OE.  bazeere,  fr.  bacan, ‘to  bake’.  See  bake  and  agential  suff.  -er  and cp.  baxter.
Derivative:  bak-erv,  n.
baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  mast...
---
### KLN71 shish
[leaf 0] ...goad*. L. sarlre is rel. 
to sarpere, ‘to cut off, lop, trim*. See sarmentum. 
assart, tr. v. — OF. essarter , ‘to grub up trees’, 
fr. essart. See assart, n. 

assassin, n., murderer. — F., fr. It. assassino , fr. 
Arab, hashshdshtn, ‘drinkers of hashish ', fr. 
hashish, ‘hemp’; see hashish. The first assassins 
were the fanatic followers of the Shaykh-ul- 
Jabal (the Old Man of the Mountains), who 
committed their murders under the intoxication 
of hashish. The plural suff. -In in assassin was 
mis...
---
[leaf 0] ... is rel. 
to sarpere, ‘to cut off, lop, trim*. See sarmentum. 
assart, tr. v. — OF. essarter , ‘to grub up trees’, 
fr. essart. See assart, n. 

assassin, n., murderer. — F., fr. It. assassino , fr. 
Arab, hashshdshtn, ‘drinkers of hashish ', fr. 
hashish, ‘hemp’; see hashish. The first assassins 
were the fanatic followers of the Shaykh-ul- 
Jabal (the Old Man of the Mountains), who 
committed their murders under the intoxication 
of hashish. The plural suff. -In in assassin was 
mistaken for part o...
---
[leaf 0] ... ‘to cut off, lop, trim*. See sarmentum. 
assart, tr. v. — OF. essarter , ‘to grub up trees’, 
fr. essart. See assart, n. 

assassin, n., murderer. — F., fr. It. assassino , fr. 
Arab, hashshdshtn, ‘drinkers of hashish ', fr. 
hashish, ‘hemp’; see hashish. The first assassins 
were the fanatic followers of the Shaykh-ul- 
Jabal (the Old Man of the Mountains), who 
committed their murders under the intoxication 
of hashish. The plural suff. -In in assassin was 
mistaken for part of the word. Cp. Bedou...
---
[leaf 0] ...o , fr. 
Arab, hashshdshtn, ‘drinkers of hashish ', fr. 
hashish, ‘hemp’; see hashish. The first assassins 
were the fanatic followers of the Shaykh-ul- 
Jabal (the Old Man of the Mountains), who 
committed their murders under the intoxication 
of hashish. The plural suff. -In in assassin was 
mistaken for part of the word. Cp. Bedouin. 
Derivatives: assassin-ate, tr. v., assassin-at- 
ion, n. 

assault, n. — ME. asaut, fr. OF. asaut (F. as- 
saut ), fr. VL. *assaltus, fr. ad- and L. salt us, 
‘a lea...
---
[leaf 0] ...ined by the English 
lexicographer and linguist Dr. (later, Sir James) 
Murray (1837-1915)- 

backgammon, n. — Prop, a game, in which the 
pieces are put back ; compounded of back, ‘the 
hinder part of the body’, and gammon, ‘game’, 
backsheesh, backshish. — Variants of baksheesh, 
backward, backwards, adv. — Formed fr. back , 
adv. (see back, ‘the hinder part of the body’), 
and -ward, resp. -wards. 

Derivative: backward , adj. 
backwardation, n., postponement of delivery 
{London Stock Exchange). ...
---
[leaf 0] ...Baekeland (1863-1944). 
For the ending see subst. suff. -ite. 
baker, n. — ME. bakere, fr. OE. bxcere, fr. bacan, 
‘to bake’. See bake and agential suff. -er and 
cp. baxter. 

Derivative: bak-ery , n. 

baksheesh, n., a gratuity; a tip. — Pers. bakhshish, 
lit. ‘gift’, a derivative of the verb bakhshidan , ‘to 
give’, fr. I.-E. base *bhag-, ‘to distribute, share 
out’, whence also OI. bhajaii, .‘assigns, allots, 
apportions, enjoys, loves’, bhagafy, ‘allotter, dis- 
tributor, master, lord’, Gk. 9aye...
---
```


## [2026-09-05T14:59:51.473Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; python3 $S SYN.txt \"BOLD, BRAVE|16\\.4[0-9]\" 300 8",
 "description": "Find Buck BOLD BRAVE section"
}
```


### [2026-09-05T14:59:53.211Z] TOOL RESULT

```
[leaf 112] ...eva ‘wife’ (2.32), also ‘woman’.
6. Pol. niewiasta, formerly the com- mon word for ‘woman’ (zona being ‘wife’), orig. ‘bride’: ChSl. nevésta ‘bride’, this a cpd. of neg. prefix ne and fem. of véstii ‘known’, hence the ‘un- known’, that is, the newcomer in the husband’s family. Zubat¥, Arch. sl. Ph. 16.406. Briickner 362.
Pol. kobieta, first appearing as a derogatory epithet and plausibly ex- plained as a blend of kobyla ‘mare’ (this also epithet of a ‘clumsy, stupid woman’, as is also Russ. kobyla) with names like Bieta ...
---
[leaf 297] ...P. 2.312. Ernout-M. 649) ; Lat. mentula (> It. minchia), etym. dub. (Walde-H. 2.72. REW 5513) : It. cazzo (: cazza ‘crucible’?); Rum. puld (Tiktin 1277 f.); Ir. biach (Walde-P. 1.667) ; Ir. bot, NIr. bod : W. both ‘nave of a wheel, boss of a shield’, perh. ChSI. gvozdt ‘nail’ (Pokorny, Z. celt. Ph. 16.405. Walde-H. 1.574); OE teors, ME, NE terse, tarse (NED tarse sb.'), OHG, MHG zers (perh. : OE teran ‘tear,’ etc. Walde-P. 1.802); Lith. bybzs; Pol. kutas (‘tassle’, Berneker 653) : Skt. cigna- (Walde-P. 1.402); Skt. kaprt(h)- (Walde- P. 1.348, 2.49).
4.51 BREATHE; BREATH
Grk,  zvéw; aveDpa, rv07 Got...
---
[leaf 334] ....), fr. *f-oxis, first part : Skt. vi- ‘apart? (or possibly: Zs, *ris, Lat. vis ‘strength’) and the second from the weak grade of IE *segh- in Skt. sah- ‘vanquish, overcome, be able’ (cf. vi-sah- ‘overcome, have in one’s power’), Grk. éxw ‘have, hold’, etc. Walde-P. 2.482. Boisacq 386. Brugmann, IF 16.494.
Grk. xparepés, xaprepos (Hom. also xparts) with sb. xpatos, Kapros ‘strength’, etc. : Goth. hardus, ON hardr, ete. ‘hard’, prob. also Skt. karkara- ‘rough, hard’, etc. Walde-P. 1.354. Boisacq 510 f.
Grk. dvvarés, properly ‘able, powerful’ but also ‘strong’ in body, in NG the
CC-0. In Public Domai...
---
[leaf 654] ...th. vinzs : OPruss. winis ‘peg. bung’; further connections? Trautman, Altpreuss. 462. d
Lett. nagla, fr. MHG nagel : OHG nagal, etc. (above, 4). Mihl.-Endz, 2.687.
6. ChSI. guozdi, guozdijt, Pol. g(w) 64dé Russ. gvozd’, perh. : Ir. bot ‘penis’, W. both ‘nave of a wheel, boss’. Pokorny, Z. celt. Ph. 16.405. Walde-H. 1.574. Otherwise (: Lat. hasta ‘spear’). Berne- ker 365 f., Briickner 166.
SCr. cavao, fr. the Venetian form (ef. Meyer-Liibke, It. Gram. 112) of It, chiavo, a by-form (now only poetic) of chiodo (above, 2). Berneker 138.
Boh. hieb, fr. OHG grebil ‘peg’? So Miklosich 412. Otherwise Gebau...
---
[leaf 821] ...(like OE hdl, ChSI. célti, etc.) are used for ‘safe’ as ‘wwharmed’, but hardly as ‘free from danger’, which might be expressed by a phrase be pavojaus ‘without danger’.
lett. druois, orig, ‘brave, bold’ : Lith.
SION, PROPERTY, COMMERCE
ized by Arya Samaj Foundation Chennai and eGangotri
757
drasus ‘bold, brave’, Lett. dristét, drik- stét, Lith. dristéti ‘dare’. Miuhl.-Endz. 1.508.
6. ChSl. stichranino adv. (renders aopadras Mk. 14.44) : (st)chraniti ‘save, preserve’ (11.24).
ChSl. céli, SCr. cio, Boh. cely, Pol. caly (and ocalony fr. ocalié ‘save’), Russ. celyj, all also ‘whole, entire’, ChSl. also ‘well...
---
[leaf 1163] ...3 JoyrruL, GLAD
16.24 Happy, Happiness
16.25 Laueu (vb.); Size (vb.) 16.26 Puay (vb.)
16.27 Love (sb.; vb.)
16.28 Drar
16.29 Kuss (vb.)
16.31 Pain, SUFFERING
16.32 Grier, Sorrow
16.33 AnxiEeTy
16.384 Recret (vb.), Repent 16.35 Pyrry (sb.)
16.36 Sap
16.37 Cry, WEEP
16.38 Tsar (sb.)
16.39 Groan (vb.)
16.41 Hares (sb.)
16.42 ANGER
In this chapter we need not be con- cerned with such moot questions as the definition and precise character of emo- tions; the differentiation of emotions, passions, moods, etc.; the selection of certain emotions as primary; the divi- sion into pleasant and unpleasant or oth...
---
[leaf 1163] ....24 Happy, Happiness
16.25 Laueu (vb.); Size (vb.) 16.26 Puay (vb.)
16.27 Love (sb.; vb.)
16.28 Drar
16.29 Kuss (vb.)
16.31 Pain, SUFFERING
16.32 Grier, Sorrow
16.33 AnxiEeTy
16.384 Recret (vb.), Repent 16.35 Pyrry (sb.)
16.36 Sap
16.37 Cry, WEEP
16.38 Tsar (sb.)
16.39 Groan (vb.)
16.41 Hares (sb.)
16.42 ANGER
In this chapter we need not be con- cerned with such moot questions as the definition and precise character of emo- tions; the differentiation of emotions, passions, moods, etc.; the selection of certain emotions as primary; the divi- sion into pleasant and unpleasant or other types of classi...
---
[leaf 1163] ...inition and precise character of emo- tions; the differentiation of emotions, passions, moods, etc.; the selection of certain emotions as primary; the divi- sion into pleasant and unpleasant or other types of classification. The rela-
1084
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
16.43 Races, Fory
16.44 Envy, JEALousy
16.45 SHame (sb.)
16.46 Honor (sb.)
16.47 Guiory
16.48 Proup
16.51 Dares
16.52 Brave
16.53 Fear, Fricur
16.54 DancrER
16.55 Timp, Cowarpiy
16.61 Wrz, Wiss (vb.)
16.62 Derstre (vb.)
16.63 Hops (sb.)
16.64 THanxs
16.65 Farrarun
16.66 Tru
16.67 Li (sb.)
16.68 Dercrir
1...
---
```


## [2026-09-05T14:59:59.835Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; python3 $S SYN.txt \"16\\.52\\s+BRAVE|16\\.52 Brave\" 1200 4",
 "description": "Find Buck 16.52 BRAVE section"
}
```


### [2026-09-05T15:00:01.575Z] TOOL RESULT

```
[leaf 1163] ...oundation Chennai and eGangotri
CHAPTER 16
EMOTION (WITH SOME PHYSICAL EXPRESSIONS or EMOTION); TEMPERAMENTAL, MORAL, AND AESTHETIC NOTIONS
16.11 Sovn, Spirit
16.12 Emotion, FEELING 16.13 Passion
16.14 Care (sb.)
16.15 Wonprr, ASTONISHMENT 16.16 Surprise
16.17 Fortune (Good or Bad) 16.18 Goop Fortune
16.19 MuisroRTUNE
16.21 PuasE
16.212 Purassz (in polite phrase) 16.22 Jor
16.23 JoyrruL, GLAD
16.24 Happy, Happiness
16.25 Laueu (vb.); Size (vb.) 16.26 Puay (vb.)
16.27 Love (sb.; vb.)
16.28 Drar
16.29 Kuss (vb.)
16.31 Pain, SUFFERING
16.32 Grier, Sorrow
16.33 AnxiEeTy
16.384 Recret (vb.), Repent 16.35 Pyrry (sb.)
16.36 Sap
16.37 Cry, WEEP
16.38 Tsar (sb.)
16.39 Groan (vb.)
16.41 Hares (sb.)
16.42 ANGER
In this chapter we need not be con- cerned with such moot questions as the definition and precise character of emo- tions; the differentiation of emotions, passions, moods, etc.; the selection of certain emotions as primary; the divi- sion into pleasant and unpleasant or other types of classification. The rela-
1084
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
16.43 Races, Fory
16.44 Envy, JEALousy
16.45 SHame (sb.)
16.46 Honor (sb.)
16.47 Guiory
16.48 Proup
16.51 Dares
16.52 Brave
16.53 Fear, Fricur
16.54 DancrER
16.55 Timp, Cowarpiy
16.61 Wrz, Wiss (vb.)
16.62 Derstre (vb.)
16.63 Hops (sb.)
16.64 THanxs
16.65 Farrarun
16.66 Tru
16.67 Li (sb.)
16.68 Dercrir
16.69 Forcive
16.71...
---
[leaf 1233] ...ches Wtb. 623.
Du. durven, NHG diirfen ‘may’ (9.95), used also for a mild ‘dare’ (much as in NE I dare say).
6. Lith. dristi, Lett. drikstét, above, 1.
7. ChSl. sti-méti (usual for roAyaw in Gospels, Supr., etc.), SCr. smjeti, Boh. smit (now ‘may’, old ‘dare’), Pol. Smieé, Russ. smet’, with adj. ChSl. si- mélit, Russ. smelyj ‘brave’ (hence Russ. osmelivat’sja ‘dare’), etc., prob, : Goth.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1150 SELECTED INDO-EUROPEAN SYNONYms
mops ‘anger’, OE méd, OHG muot ‘spirit, courage’, etc. (16.42). Walde-P. 2.239. Berneker 2.47.
ChSl. driiznqit (mostly for @apcéw, sometimes for rodpaw), Bulg. dritzni, OBoh. drzati, Russ. derzat’, etc., with adj. ChSl. drtizi ‘bold’, etc., prob. through adj. ‘firm’ > ‘bold’ : Skt. drh- ‘make firm’, Av. daraza- ‘firm’, etc. Con-
nection with IE *dhers- (above, 1), Je ing the Slavic z unexplained (except a blend with *dhergh- in Skt. drh-, ete he less likely. Walde-P. 1.859, s64, i neker 257 f. ae SCr. odvaziti, Boh. odvdziti, Pol, (0d) wazyé (all in refl. form), fr. NHG wagen, Briickner 598 f. Miklosich 374. 8. Skt. dhrs-, OPers. dars-, above, 1,
16.52 BRAVE Grk.  Opacts, roAunpés, Goth. *balps Lith. narsu...
---
```


## [2026-09-05T15:00:07.010Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==1235' SYN.txt | head -80",
 "description": "Print Buck p.1151 (16.52 BRAVE)"
}
```


### [2026-09-05T15:00:08.644Z] TOOL RESULT

```
s, drqsus ayabbs ON djarfr, hraustr Lett.  dii8igs, druoks NG dvrpetos, -yevvatos Dan. tapper,modig . ChSl. — driizti, chrabiirt, Lat. fortis, animdsus, au- Sw. tapper, modig SCr. _hrabar, odvaan daz OE beald, céne, médig, Boh. udatny, staletny It. bravo, coraggioso dyrstig Pol. odwazny, waleczny, Fr. brave, courageux ME bold, keene, modi, meiny Sp. bravo, valiente corageus Russ. chrabryj Rum. viteaz, brav, curagios NE brave, courageous Skt. ¢tira-, vira- Ir. dana, essamin (gal Du. dapper, moedig, koen Av. Girya-, dar&i-, dar’yu- sb.) OHG  kuoni, bald Nir. _calma, crodha MHG kriene, balt, ° tiirstic, W. dewr, gwrol muotec Br. kalonek, kadarn NHG tapfer, mutig, kiihn
Some of the words listed are used only in the good sense, as terms of approval, like NE brave, while others are used also, or some of them more usually, in the bad sense, with feeling of reproof, ‘bold, rash’
Several are in origin ‘daring’, cognate with verbs for ‘dare’. Others are de- rived from words for ‘spirit, soul’, ‘mood’, or ‘heart’ through the notion of ‘cour- age’; or as originally ‘manly’ from words for ‘man’; or as ‘fearless’ from ‘fear’. Still others are words for ‘strong, mighty’, ‘firm, steadfast’, ‘skilful’, ‘good’ etc., either used also as common expres- sions for ‘brave’ or definitely specialized in this sense. A few are connected with words for ‘war’, ‘anger’, or ‘blood? (through ‘cruel’).
1. Grk. @pacts (most often in bad sense ‘bold, rash’, but also in good sense ‘brave, bold’ as of Hector and others in
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Hom.) : dapcéw ‘dare’, Odpoos ‘courage’, ete. (16.51).
Grk. rodunpéds (poet. also roApjes), deriv. ‘of 76\ua ‘courage, daring’ : roAuaw ‘dare’ (16.51).
Grk. ayafés ‘good’ (16.71) used also for ‘brave’ (Hom.+), as conversely xaxés ‘bad’ for ‘cowardly’ (16.55).
Grk. davépetos ‘manly’ (fr. avqp, avbpés ‘man’) in NG reg. ‘brave’, with avdpela ‘bravery, courage’.
Grk. yevvatos ‘high-born, noble, ¢x- cellent’ (fr. yévva ‘birth, descent’), NG ‘noble’ but esp. ‘brave’.
2. Lat. fortis ‘strong’ (4.81), and esp., as mentally strong, ‘brave’. oo
Lat. animosus, fr. animus ‘soul, spirit, mind, etc.’ (16.11), and hence ‘spirit, courage’. F
Lat audax (more often ‘bold’ in bad sense) : audére ‘dare’ (16.51).
Sp. bravo, ‘wild’ in OSp., later
‘brave’
sense > It. bravo > Fr. prav), fr. Lat. barbarus orig. ‘foreign, a foreigner’, id. REW 945. Gamill-
1080 teal coraggio (fr. Prov. corat-
ge ‘courage’, derivs. of Fr. tc. ‘heart’. REW 2217. j i Iso It.
nie (and in this sense a 4 a yaillant > ME vailant, NE
yaliant), PP qloir) ‘be wor be good for’. REW 9130.
Rum. viteaz, as sb. ‘hero’, fr. th
```


## [2026-09-05T15:00:15.070Z] TOOL CALL #32: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T15:00:15.077Z] TOOL RESULT

```


```


## [2026-09-05T15:00:19.015Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### MON1 shishlik\"; python3 $S MON_part1.txt \"شیشلیک|شیش\" 200 8; echo \"### MON2\"; python3 $S MON_part2.txt \"شیشلیک|شیش کباب\" 200 8",
 "description": "Grep Mo'in for shishlik"
}
```


### [2026-09-05T15:00:20.627Z] TOOL RESULT

```
### MON1 shishlik
[leaf 0] ... )1( نام ماه پنجم 5 پاز دهم سالماه 
خاص بهودی و سرانی. در اصطلاح 
سریانی رومی ماه آب با ماه ششم اغسطس 
سال ماه ترکان یعنی با ماه اوت یولیانی 
مطایق است. 

آباء: "2 ([ع. ف. آبا) ج. اب. بدران» 
اجداد. کشیشان (مسیحی)» آناء کلیسا» آباء 
کنسه. آباء سبعه: هفت پدران. آباء علوی: 
پدران آسمانی. آباء کلیسا: کشیشان مسیحی؛ 
آناء کتسته. آباء کتسته: آباء کلیسا, 

آب‌آب: 0 20-6 (امر.) آبی که هر موجود 
از آن بوجود آ...
---
[leaf 0] ...س 
سال ماه ترکان یعنی با ماه اوت یولیانی 
مطایق است. 

آباء: "2 ([ع. ف. آبا) ج. اب. بدران» 
اجداد. کشیشان (مسیحی)» آناء کلیسا» آباء 
کنسه. آباء سبعه: هفت پدران. آباء علوی: 
پدران آسمانی. آباء کلیسا: کشیشان مسیحی؛ 
آناء کتسته. آباء کتسته: آباء کلیسا, 

آب‌آب: 0 20-6 (امر.) آبی که هر موجود 
از آن بوجود آبد. (تص.) دات خدا» هو بت 
حصق تعالی. (تص.) رحمت خدا نفس 
0 

آب‌او رده: (6-)2۷2)0(۲۳12-.2 (ام_ف.) آن...
---
[leaf 0] ... شناگر» ضواص 
(فره.) (ور.) به اشخاصی اطلاق می‌شود که 
در چاله حوض حمام حرکات نمایشی انجام 
می‌دهنك. 

اب‌بان: 2.0 (ص‌مر.) مردی که و ظبفه او 
شده به محصول می‌رسد يا نه. 

اب بسسته: (۵)هادهه 2.6 (امر.) شیشه؛ 
آ کم بلور. بح. . ژاله» شبنم. تگرگک. 
آب‌بند: 2.0 (رص. امر .) آنکه که آب 
را بند کند. (عم.) آنکه آب در ظرفی ریزد. 
آنکه ماست و پنیر و سرشیر و خامه سازد. 
آنکه درزهای ظروف فلزی را با موم مذاب 
یا قل...
---
[leaf 0] ...
که شومالان - یعنی آهار دهندگان -بر آب 
زنند و برتانه که به جهت بافتن تر تیب کرده 
باشند» فشانند. گنجایش و ظرفیت حوض یا 
پیمانه‌ای یا مکیالی: آبگیر اين حوض ده کر 
است؛. 

آیگینه: (8-)02]ع- -20 (امر.) شیشه» زجاج. 
پلور. این زجاجی. ظرف شیشه‌یی؛ ظرف 
شرات. الماس. تیغ. تما آیگنه سیمار: 
قاروره» تقسر ۵» بیشیار. آبگینه حلبی: آبنه 
حلبی» اينة فلزی که در شهر حلب 


فرهنگ فارسی معین ۳۱ 


می‌ساختند. آبکینه شا...
---
[leaf 0] ...ر آب 
زنند و برتانه که به جهت بافتن تر تیب کرده 
باشند» فشانند. گنجایش و ظرفیت حوض یا 
پیمانه‌ای یا مکیالی: آبگیر اين حوض ده کر 
است؛. 

آیگینه: (8-)02]ع- -20 (امر.) شیشه» زجاج. 
پلور. این زجاجی. ظرف شیشه‌یی؛ ظرف 
شرات. الماس. تیغ. تما آیگنه سیمار: 
قاروره» تقسر ۵» بیشیار. آبگینه حلبی: آبنه 
حلبی» اينة فلزی که در شهر حلب 


فرهنگ فارسی معین ۳۱ 


می‌ساختند. آبکینه شامی: آبنة شامی» آبنة 
منسوب به شهر ...
---
[leaf 0] ...ب و 
زخم و گرد آمدن آب میان بشره و دمه یعنی 
جلد اصلی. (بز.) مرضی است ساری که 
بصورت تاول‌هایی روی پویست بدن‌ظاهر 
می‌شود و باتب همراه است. در اغلب 
حیوانات مانند گوسفند و گاو و خوک و بز 


مر. امر.) شیشه گر: 


و اسب و پرندگان نیز بروز می‌کند؛ باد آبله. 
عقده‌ای که به سیب راه رفتن بسیار در پا پیدا 
شود. سخال» تسخاله. تکمهٌ بستان سر بستان» 
نوک پستان. آبله از هم گسستن: : بیرون زدن 
آبله. آبله شم: دان...
---
[leaf 0] ...ن عب به علت نامنظم بودن 
قرنیه ( که کروی نباشد) و یا جلیدیه (که 
نامنظم باشد) ایجاد می‌شود. در این صورت 
از آن وال تم تست که توا 
قسمت‌های مختلف یک جسم بر روی نقطة 
زرد کارا بل برای رفع ۱ بسن 
عیب از شیشه‌های استوانه‌بی که آنها راروی 
عنککك قرار می دهند» استفاده می‌شو د. 
استیم: و2 [- استیم ِ اشتیم ِ ستیم ] (1.) 
چرکك زخم» زیم» جراحت. سرمایی که بر 
جراحت زند و جراحت به سب ان اماس 
کت 

استیم: و (.) د...
---
[leaf 0] ...د رسوب 


دهد. نشانةٌ اختصاری آن ۸ است. 
آمپرسنج: ل«ع.ة (ا. امر.) (فز.) آلتی 
است جهت تعبین اندازة شدت جریان 
الکتر یسیته به حسب آمپر. آمپرمتر. (فره.) 
اف ۲ (.) (فز.) آمپرسنح. 
آمپول: ا5رسة (.) (پز.) شیشه کوچکث 
سربسته محتوی داروی تزریقی یا خوراکی. 
امد؛ 0هحوة (مص خم. آمدن) آمدن» ایات: 
وفتاق امد) مق زفتا: دهات: باز کفبتا: 
اقال» روی آوردن بحت) رت ی ) مق. 
نبامد. آمدکار: یتک زا یمن» میمنت. 
آمدن: رد-...
---
### MON2
NO MATCH
```


## [2026-09-05T15:00:26.000Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"=== $f\"; grep -c \"شیشلیک\\|شیشلیگ\\|شیش کباب\\|شیش‌کباب\" \"$f\" 2>/dev/null; done",
 "description": "Count shishlik in Mo'in files"
}
```


### [2026-09-05T15:00:27.821Z] TOOL RESULT

```
Exit code 1
=== MON_part1.txt
1
=== MON_part2.txt
0
=== incoming/MON/MON_2vol_Adena_v1_djvu.txt
1
=== incoming/MON/MON_2vol_Adena_v2_djvu.txt
0
```


## [2026-09-05T15:00:32.383Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; python3 $S MON_part1.txt \"شیشلیک\" 400 3; echo \"=== adena\"; python3 $S incoming/MON/MON_2vol_Adena_v1_djvu.txt \"شیشلیک\" 400 3",
 "description": "Print Mo'in shishlik entry"
}
```


### [2026-09-05T15:00:34.055Z] TOOL RESULT

```
[leaf 0] ...ماد با 
فرستادن شیرینی به منزل عروس منعقد شود. 
شیرینی فروشی: 3-0704-7 (حامص.) 
عمل و شغل شیرینی فروش؛ قنادی. (امر.) 
دکان شیر بن فروش) قنادی. 

شیز: 112 [- معر. شیزی] (ا.) (گیاء) آبنوس 
(گیا.) گردکان؛ درخت گردو. قوس» کمان. 
شیشک: 1339 [- شیشاکک] (.) گوسفند 


یک ساله. 
شیشک: *3132 [- شیشاک] (.) (مس.) 
رباب چهار تار. 


شیشکی: 2821 (.) (عم.) صدایی است 
که در مقام تمسخر و تحقیر از دهن 
بر آورند. 

شیشلیک: »11 [تر. به معنی سیخی] 
(امر.) کباب سیخی» طرز تهیة آن چنین 
است: مقداری گوشت راستةٌ قرمز و به 
اندازهةٌ یکك چهارم آن دنه را قطعه قطعه 
کرده با پیاز خرده شده مخلوط نمایند و 
نصف روز در محل خنکی بگذارند و روی 
آن را سرکه و نمک و فلفل ریزند تا سرد 
شود و سپس چهار قطعه گوشت و یک قطعه 
دنبه به ترتیب به سیخ باریکک و بلند کشیده 
مانند کباب‌های معمولی روی آتش پزند و 
آبدار بردارند و در قاب گذاشته روی آن...
---
=== adena
[leaf 0] ...ماد با 
فرستادن شیرینی به منزل عروس منعقد شود. 
شیرینی فروشی: 3-0704-7 (حامص.) 
عمل و شغل شیرینی فروش؛ قنادی. (امر.) 
دکان شیر بن فروش) قنادی. 

شیز: 112 [- معر. شیزی] (ا.) (گیاء) آبنوس 
(گیا.) گردکان؛ درخت گردو. قوس» کمان. 
شیشک: 1339 [- شیشاکک] (.) گوسفند 


یک ساله. 
شیشک: *3132 [- شیشاک] (.) (مس.) 
رباب چهار تار. 


شیشکی: 2821 (.) (عم.) صدایی است 
که در مقام تمسخر و تحقیر از دهن 
بر آورند. 

شیشلیک: »11 [تر. به معنی سیخی] 
(امر.) کباب سیخی» طرز تهیة آن چنین 
است: مقداری گوشت راستةٌ قرمز و به 
اندازهةٌ یکك چهارم آن دنه را قطعه قطعه 
کرده با پیاز خرده شده مخلوط نمایند و 
نصف روز در محل خنکی بگذارند و روی 
آن را سرکه و نمک و فلفل ریزند تا سرد 
شود و سپس چهار قطعه گوشت و یک قطعه 
دنبه به ترتیب به سیخ باریکک و بلند کشیده 
مانند کباب‌های معمولی روی آتش پزند و 
آبدار بردارند و در قاب گذاشته روی آن...
---
```


## [2026-09-05T15:00:43.136Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%AE",
 "prompt": "Give the full Persian section: etymology of سیخ (sīx) 'skewer', any Middle Persian/Proto-Iranian reconstruction, Sanskrit comparison (śikhā), and cited sources (Hasandust, Horn, etc.). Also any other language sections."
}
```


## [2026-09-05T15:00:44.873Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%C5%9Fi%C5%9F",
 "prompt": "Give the Turkish section for şiş: all etymologies (skewer / swelling), Old Turkic / Proto-Turkic reconstructions, any mention of Persian origin, and derived terms like şişlik / şiş kebap."
}
```


### [2026-09-05T15:00:50.605Z] TOOL RESULT

```
# سیخ (sīx) - Persian Section Analysis

## Etymology 1 (Skewer/Spit)

The Wiktionary entry states the etymology is incomplete. It notes: "Particularly: 'Cognate with Sanskrit शिखा (śikhā)?'" However, no definitive reconstruction or cited sources establishing this connection are provided in the article.

## Etymology 2 (Stiff/Erect - Adjective)

The documented derivation traces to Classical Persian ستیخ (sitēx, "high, firm, erect"), which derives from Middle Persian styk' /stēɣ/ ("erect"). The source indicates this Middle Persian form requires Book Pahlavi script notation, which is not supplied.

## Descendants

The Persian term produced forms across multiple languages:
- Chagatai, Uzbek, Uyghur, Ottoman Turkish, Armenian, and Turkmen varieties

## Source Documentation

The article references no specialized etymological works by scholars like Hasandust or Horn. Instead, it cites general lexicographical resources and notes gaps in the existing etymology section, inviting community contributions to clarify the Sanskrit connection and provide fuller Middle Persian documentation.

**Key limitation**: This Wiktionary entry acknowledges incomplete etymological information rather than presenting established scholarly consensus on the word's ultimate origins.
```


### [2026-09-05T15:00:53.137Z] TOOL RESULT

```
# Turkish Section of şiş

## Etymologies

**Etymology 1 (Swelling):** Derived from Ottoman Turkish شیش (şiş, "swollen"), related to the verb şişmek and cognate with Old Turkic. This sense encompasses medical and physical swelling meanings.

**Etymology 2 (Skewer/Needle):** From Ottoman Turkish شیش (şiş, "skewer; rapier; knitting needle"), tracing back to Proto-Turkic *sīĺ meaning "spit, pointed stick or pole," cognate with Turkmen çiş.

## Reconstructed Forms

The word ultimately derives from Proto-Turkic *sīĺ ("spit, pointed stick or pole"). No Persian origin is mentioned in the entry.

## Derived Terms & Related Concepts

The entry lists several derivatives:
- şişlik (swelling-related)
- şişlemek (to pierce/skewer)
- şiş kebap / şiş kebabı (skewered meat)
- şiş köfte (skewered meatballs)

Additionally, the word has descended into English as "shish" (as in shish kebab).
```


## [2026-09-05T15:00:58.418Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/shish%20kebab",
 "prompt": "Give the full etymology entry for shish kebab (and kebab if shown): date of first English attestation, Turkish şiş 'skewer' and kebap, Arabic kabab, any Persian involvement."
}
```


## [2026-09-05T15:00:59.748Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%DB%8C%D8%B1%D9%87",
 "prompt": "Give the Persian section for چیره (čīra): etymology, Middle Persian čēr, Avestan čirya-, any Proto-Iranian reconstruction, sources cited. Also any entry for چیر."
}
```


### [2026-09-05T15:01:13.820Z] TOOL RESULT

```
# Etymology of Shish Kebab and Kebab

**Shish Kebab (1913):**
"pieces of lamb or other meat grilled on skewers, 1913, from Armenian shish kabab, from Turkish siskebap, from sis 'skewer' + kebap 'roast meat.'"

**Kebab (1783):**
The related term "pieces of meat roasted on a skewer" appeared earlier, documented from 1783.

## Key Information

The webpage traces the English term back to Turkish *siskebap*, which combines *sis* (skewer) and *kebap* (roast meat). The Armenian form *shish kabab* served as an intermediate step into English. However, the source document does not provide information about Persian involvement or Arabic *kabab* origins—only the Turkish and Armenian etymologies are documented here.
```


### [2026-09-05T15:01:16.378Z] TOOL RESULT

```
# Response

Based on the Wiktionary content provided, the Persian section for **چیره** (čīra) does not include etymology, Middle Persian, Avestan, or Proto-Iranian reconstructions.

The page only presents:
- **Pronunciation variants** across Classical Persian, Dari, Iranian, and Tajik dialects
- **Adjective definitions**: prevailing/victorious; brave/strong/powerful; rude/violent
- **A single quotation** from Rumi's Masnavi (c. 1260s) demonstrating usage

No separate entry for **چیر** is mentioned. The references cited are historical dictionaries (Hayyim 1934, Steingass 1892) and a Tajik vocabulary resource, but these source materials themselves are not reproduced with etymological details on this page.
```


## [2026-09-05T15:01:24.708Z] TOOL CALL #40: Bash

```json
{
 "command": "pdftoppm -f 106 -l 106 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg106 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 106"
}
```


## [2026-09-05T15:01:26.531Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### NYB cer\"; python3 $S NYB_vol2_glossary.txt \"c[eē]r\\b|čēr\" 200 8; echo \"### CHEUNG car\"; python3 $S CHEUNG.txt \"čirya|cirya\" 250 6",
 "description": "Grep Nyberg and Cheung"
}
```


### [2026-09-05T15:01:26.759Z] TOOL RESULT

```
total 32780
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


### [2026-09-05T15:01:29.099Z] TOOL RESULT

```
### NYB cer
[leaf 21] ...74. 108?; ~ kartan to inform 10%, 11%; kē hac dén ~ he who is enlightened by Religion 6716; subst. pl. cas. obl. kam ~-Gn the ignorant, the witless 11077. — MPrs .g?
(S); Paz. NP ägäh. Arm. lw. akah, cer-
tainly from Prth, proves that -s in ’k’s is spurious, and only the inverse spelling
www.parsianjoman.org | ool wok
akih
of -h; thus it cannot be connected with dkas (q. v.), which also differs in me...
---
[leaf 54] ...ar-barišneh.
barišnēh det. v. n. of burtan: the act of carrying or bringing: & gobišn ~ this "saying-bringing" = such a message conveyed to me (by a mysterious voice) 3812-18; bahr ~ performance of sacer- dotal ministry 53%, v. aržanikenitan and bahr. ~ V. also apar-barišneh and frot- barišnčh.
barišnihi adv. of barišn: yātangēk ~ when engaging a yätangök (g. v.) 7019. — Wanting in Paz. and Skr. v.
b...
---
[leaf 65] ...ied by the
eigón
Western Zoroastrians with Lake Urmia, v. Sécikan.
eér [cyl] brave, valiant, courageous 3!$. 161%, — Av. (598) cirya-; MPrth comp. <cy>rdr, sup. cyryst, cyyrtwm, Sogd. 3514 sq. ; Paz. cer, Skr. v. balistha (SGV), render- ing Av. (380) ugra-; NP cer.
céréh bravery, courage 2*.
cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921;...
---
[leaf 65] ...ikan.
eér [cyl] brave, valiant, courageous 3!$. 161%, — Av. (598) cirya-; MPrth comp. <cy>rdr, sup. cyryst, cyyrtwm, Sogd. 3514 sq. ; Paz. cer, Skr. v. balistha (SGV), render- ing Av. (380) ugra-; NP cer.
céréh bravery, courage 2*.
cigon [cygwn] adv. and conj. A. interrog. adv. how? 1. direct interrogation: nun ~ kunom ?] 272; asmān ~? 921; exclama- tory: how...! 614. — 2. indirect inter- rogation: ä...
---
[leaf 161] ...irmly, with cer- tainty 1097.
www.parsianjoman.org | ool wok
10 Nyberg
ol oc
68 [?wS] reason, understanding, obser- vation, cas. obl. óseh [’wsyh] 522°; pat ~ *cautiously, warily 482%. 497.21, 5019, of NP adj. hösma...
---
[leaf 169] ...nām i... in the name of; in oaths: by: pat x%arrah t Ohurmazd bag ... sdkand xuarčt (imp.) 2117-18; 5913.29, — 6. with regard to: pat dipireh u asvārēh ... ētēn frahast ku ... 226-27; pat cövegän ... cer u nipartak būt 315-16; drāžtar pat bālai u früx"tar pat pahnai 389-19; ka pat tan ētūn vazurg but hend +... 3229-27; 2 angust pat balas 93; pat nēvakēh apar-arZünik 921-15, — 7. distributive: pat 10 ...
---
[leaf 179] ...) satar ; besides, Arm has the Prth. lw. pašt-pan “protector, defender’ < *parésti- päna- (v.s. v. pušt); NP pustibän, pustvän. — pušt-aspān 1118 is an old misreading (Paz. pustaspän Mx) of pustepän, cer- tainly due to wrong association with asp ‘horse’, as is suggested by the spelling pwšt'sp'n'; moreover, in the BP writing the ligature -yp- is very often formed so as to coincide with -sp-. Read con...
---
[leaf 200] ...— Borrowed from Av. (545) xšadra- vairya-.
šahridar ([Str'yd’l, štr'd'l, Prs inscr. Stldl-] ruler, of Pāpak as the Arsacid sub-regent of Pars 1°; of the emperor of Rome (Byzance) 17°; of the high officer sent by the Indian king to the Sassanid court 118°. 1215; pl. cas. obl. ~-dn of the highest class of the Sassanian society, the governors, or vice-roys HajB:5. — Prth. official language hstrdr-, v. x...
---
### CHEUNG car
NO MATCH
```


## [2026-09-05T15:01:35.863Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg106.png"
}
```


### [2026-09-05T15:01:36.228Z] TOOL RESULT

```

```


## [2026-09-05T15:01:36.223Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T15:01:59.654Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob,re\nhits=[]\nsansk_c=[]\nfor f in sorted(glob.glob('data/extracted/batch/page-*.json')):\n    d=json.load(open(f,encoding='utf-8'))\n    for e in d.get('entries',[]):\n        r=e.get('root',{})\n        if r.get('lang') and 'Sanskrit' in str(r.get('lang')):\n            n=r.get('name','')\n            if re.match(r'^[ČčCc]', n): sansk_c.append((f,n,r.get('gloss')))\n        for nd in e.get('nodes',[]):\n            if nd.get('lang') and 'Sanskrit' in str(nd.get('lang')):\n                for w in nd.get('words',[]):\n                    t=w.get('translit') or ''\n                    if re.match(r'^[Čč]', t): sansk_c.append((f,t,w.get('gloss')))\nprint(len(sansk_c))\nfor h in sansk_c[:80]: print(h)\nEOF",
 "description": "Scan extracted data for Sanskrit č- forms"
}
```


### [2026-09-05T15:02:01.438Z] TOOL RESULT

```
10
('data/extracted/batch/page-106.json', 'Čîxâ, Čixâ, Čĕxara', 'point, tip, any pointed thing, skewer')
('data/extracted/batch/page-234.json', 'čakta', 'strong, hard')
('data/extracted/batch/page-249.json', 'čokah', 'peak, hammer')
('data/extracted/batch/page-271.json', 'črî', 'bind, mix')
('data/extracted/batch/page-284.json', 'čvitra', 'white')
('data/extracted/batch/page-292.json', 'čamati, camati', 'to sip')
('data/extracted/batch/page-452.json', 'čadaiti', 'to cover')
('data/extracted/batch/page-452.json', 'čattra', 'cover, umbrella')
('data/extracted/batch/page-456.json', 'čodatî', 'to hurry, propel')
('data/extracted/batch/page-467.json', 'čârah', 'sparrow')
```


## [2026-09-05T15:02:19.614Z] TOOL CALL #44: Bash

```json
{
 "command": "sed -n '1,200p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read verify_check tool"
}
```


### [2026-09-05T15:02:19.654Z] TOOL RESULT

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


## [2026-09-05T15:02:29.193Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; for f in LKT.txt TTS.txt WEB_vol1.txt FSD_vol4.txt SKT.txt HJB.txt; do echo \"=== $f\"; ls $f >/dev/null 2>&1 && python3 $S $f \"schisch|Schisch|kebab|kabob|kebap\" 200 4 || echo \"(no file)\"; done",
 "description": "Grep Turkic/English books for shish kebab"
}
```


### [2026-09-05T15:02:34.047Z] TOOL RESULT

```
=== LKT.txt
[leaf 42] ...Geschenk'  [vom  Vb.  bühSldän  'schenken' Horn  NpEt  S.  43,  Nr."! 86];  ebenso  tk. baksis.  Hieraus  rum.  ftacgis 'Trinkgeld'; engl,  angloind.  bucksheesh,  huxees;  frz. bakchich;  dtsch.  Bakschisch  'Geschenk, Trinkgeld'.  Bulg.  serb.  bnksis  'dass.'. [Devic  DEt  57.    Bern  SlEtWb  40.
179.  Ar.  bahür:
'Weihrauch,  Wohlgeruch';  hieraus  mit ar.  Art.  pg.  albafar,  albafor  'Parfüm aus ...
---
[leaf 93] ...l des  Flickschusters'.  [Dicc  Gast 34  b.]   [DE  37/38.
839.  Ar.  hasis:
'Gras,  Heu',  später  beng  [s.  hier  Nr.  213] oder  indischer  Hanf,  Cannabis  indica [Über  den  indischen  Hanf  (Haschisch) und  seine  Verwendung  als  narkotisches Genußmittel.  In  Ausland  1863,  Nr.  30  j Ed.  Grimaux,  Du  hachich  ou  chanvre Indien.  Paris  1865];  in  die  europäischen Sprachen  ist  das  Wort ...
---
[leaf 93] ...,  Nr.  30  j Ed.  Grimaux,  Du  hachich  ou  chanvre Indien.  Paris  1865];  in  die  europäischen Sprachen  ist  das  Wort  fast  unverändert übergegangen:  frz.  hachiche,  russ.  gasiSf dtsch.  Haschisch.  —  „In  Syrien  steht der  Hasis,  ein  berauschendes  Hanf-  oder Mohnpräparat,  welches  unvermengt  ge- nossen oder  dem  Tabak  beigemengt wird,  bei  den  niederen  Ständen  in Gunst.  Das  Sc...
---
[leaf 94] ...Keines- wegs ist  das  Laster  des  Haschischrauchens derart  verbreitet  wie  bei  uns  der  Ge- nuß der  Spirituosen.  Weit  mehr  als  in Syrien  und  Mesopotamien  ist  das  Hanf-
67
[Ar.  hass.
rauchen  in  Ägypten  verbreitet.  In Marokko ...
---
=== TTS.txt
(no file)
=== WEB_vol1.txt
[leaf 275] ...see cable (moldin: ). ¢a’ble rail’/way, a street railway on Shieh the
DES eien away.
i [pl.] (a) an Oriental dish, consisting gen-
Toast meat.
ae hee leg of mutton with stuffing of herbs
Also spelled kabob.
Ase, bull, brite, tarn, up; ery, myth; cat, maghine, ace, church, chord; gem, afiger, (Fr.) boñ, as; this, thin; azure
Digitized by Arya Samaj Foundation
cab/6-tage
1. a precious stone cut in such a...
---
=== FSD_vol4.txt
NO MATCH
=== SKT.txt
NO MATCH
=== HJB.txt
[leaf 190] ...et  Herbs  put between  and  stuff  in  them,  and  basted  with Oil  and  Garlick  all  the  while." — Ovington. 397.
1814.— "I  often  partook  with  mv  Arabs of  a  dish  common  in  Arabia  caUedKabob or  Kab-ab,  which  is  meat  cut  into  small pieces  and  placed  on  thin  skewers,  alter- nately between  slices  of  onion  and  green ^nger,  seasoned  with  pepper,  salt,  and &ian,  fried  ...
---
[leaf 190] ...and  green ^nger,  seasoned  with  pepper,  salt,  and &ian,  fried  in  ghee,  to  be  ate  with  rice and  dholl."  -Forbes,  <)r.  Mem.  ii.  480 ; (2nd  od.  ii.  8*2  ;  in  i.  315  he  writes  Kebabs].
[1876. — ".  .  .  kavap  (a  name  which  is naturalised  with  us  as  Gabobs),  small  bits of  meat  roasted  on  a  spit.  .  .  ...
---
[leaf 1049] ...8a
Jwfl^mukhi,  4646, 631a
Jyedad,  4746
Jylibdar,  468a
Jysh  kutcheri,  Jyabe, 475a
Eft&rle,  282a Kabaai,  138a Eab-ab,  138a Kabaya,  1876 Eabel,  1406 Kaber,  176a Kaber-dar,  495a Eabkad,  1596 Kabob,  138a KlEbul,  139a Kach, ...
---
[leaf 1050] ...rah,  497a Eatche,  2866 Kath€,  598a Kattara,497a Rauda,  270a Eaul,  476a Eaulam,  7526,  829a Eaunta,  476a Eauri,  270a Eauas,  480a Eavap,  1386 Kayol,  1406 Eazbegie,  Easbekie,
8896 Ka^,  178a Kebab,  188a Eebulee,  476a,  6086 Kechmiche,   Keck-
mishe,  4d6a,  4856,
246a Keddah,  476a Kedgeree,  4766,  65a:
Pot,  4776 Kedgeree,  477a,  414« Keeledar,  4886 Keemoab,  Keemcob,
485a Keemookbt  818...
---
```


## [2026-09-05T15:02:42.706Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/%C5%9Fi%C5%9F",
 "prompt": "Give the etymology entries for şiş: Old Turkic attestations (Divanü Lugati't-Türk, Kaşgari), the meaning 'skewer/spit', and whether any Persian or other foreign origin is proposed. Also anything on şişkebap / şişlik."
}
```


## [2026-09-05T15:02:44.341Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/s%C4%ABl%CC%B1",
 "prompt": "Give the reconstruction page content for Proto-Turkic *sīĺ: meaning, descendants (Old Turkic, Turkish şiş, Turkmen çiş, etc.), and any note about borrowing from Iranian/Persian."
}
```


### [2026-09-05T15:02:46.825Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T15:02:48.605Z] TOOL RESULT

```
I appreciate your detailed request, but I must be honest: the web page content provided contains only the header, navigation, and footer of the Nişanyan Sözlük (Nişanyan Dictionary) website. It does not include the actual etymology entry for "şiş."

To answer your questions about Old Turkic attestations, the meaning 'skewer/spit', Persian origins, and related terms like şişkebap/şişlik, I would need access to the actual dictionary entry content, which is not present in the material you've shared.

If you can provide the full etymology entry text from the dictionary, I'd be happy to extract and summarize that information within the constraints you've specified.
```


## [2026-09-05T15:02:54.704Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/s%C4%ABl%C4%BA",
 "prompt": "Give the reconstruction page for Proto-Turkic *sīĺ: meaning, descendants (Old Turkic, Turkish şiş, Turkmen çiş, Azerbaijani), sources cited, and any note about borrowing."
}
```


## [2026-09-05T15:02:55.684Z] TOOL CALL #49: WebSearch

```json
{
 "query": "Nişanyan şiş kebap etymology Eski Türkçe \"şiş\" şiş~ Kaşgari Divan"
}
```


### [2026-09-05T15:02:56.459Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T15:03:07.875Z] TOOL RESULT

```
Web search results for query: "Nişanyan şiş kebap etymology Eski Türkçe "şiş" şiş~ Kaşgari Divan"

Links: [{"title":"shish kebab - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/shish_kebab"},{"title":"kebap - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/kebap"},{"title":"shish kebab, n. meanings, etymology and more | Oxford English Dictionary","url":"https://www.oed.com/dictionary/shish-kebab_n"},{"title":"Kebab | Origins, Description, Taste, & Types | Britannica","url":"https://www.britannica.com/topic/kebab"},{"title":"Shish kofta","url":"https://en.wikipedia.org/wiki/Shish_kofta"},{"title":"Kuzu %C5%9Fi%C5%9F","url":"https://en.wikipedia.org/wiki/Kuzu_%C5%9Fi%C5%9F"},{"title":"%C3%87%C3%B6p %C5%9Fi%C5%9F","url":"https://en.wikipedia.org/wiki/%C3%87%C3%B6p_%C5%9Fi%C5%9F"},{"title":"Kebab History | What Is Kebab? | Kebab Maker Machine","url":"https://www.kebabmachine.net/kebab-history/"},{"title":"Shish taouk","url":"https://en.wikipedia.org/wiki/Shish_taouk"}]

I found search results that contain references to Sevan Nişanyan's etymological work, and I can see mentions of the Nişanyan dictionary. However, the search results don't contain detailed information about the specific etymology of "şiş" (skewer) in relation to Old Turkish ("Eski Türkçe") or references to Kaşgari's Divan.

Let me perform another search to find more specific information about the etymology of "şiş":

Links: [{"title":"şiş - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%C5%9Fi%C5%9F"},{"title":"шеш - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D1%88%D0%B5%D1%88"},{"title":"Shish Kebab: Back To The Source Of Turkey's Best-Known Culinary Export","url":"https://worldcrunch.com/food-travel/kebab-history-turkey/"},{"title":"Tureng - skewer - Turkish English Dictionary","url":"https://tureng.com/en/turkish-english/skewer"},{"title":"Esin","url":"https://en.wikipedia.org/wiki/Esin"},{"title":"What is the translation of \"skewer\" in Turkish?","url":"https://en.bab.la/dictionary/english-turkish/skewer"},{"title":"Old Anatolian Turkish","url":"https://en.wikipedia.org/wiki/Old_Anatolian_Turkish"},{"title":"Kebab - Wikipedia","url":"https://en.wikipedia.org/wiki/Kebab"},{"title":"%C3%87%C3%B6p %C5%9Fi%C5%9F","url":"https://en.wikipedia.org/wiki/%C3%87%C3%B6p_%C5%9Fi%C5%9F"},{"title":"Papers by Caşteğin Turgunbayer","url":"https://dicle.academia.edu/JashteginTurgun"}]

Based on my search results, I found relevant information about the etymology of "şiş":

The word "şiş" comes from Ottoman Turkish and is derived from Proto-Turkic *sīĺ ("spit, pointed stick or pole"), with cognates appearing in related Turkic languages like Kyrgyz, Southern Altai, Tuvan, and others.

The word "şiş/shish" (skewer) comes from old Turkish, meaning a stick with a pointy end. Additionally, şiş is a Turkish word meaning "sword" or "skewer".

The search results also reference Sevan Nişanyan as a Turkish etymologist, and the Nişanyan Sözlük (Nişanyan Dictionary) appears in the search results as a source for etymology, though the specific details about his analysis in relation to Kaşgari's Divan were not fully detailed in these search results. The results do show connections to Old Turkish sources, but the detailed etymological analysis you're asking about regarding Kaşgari's Divan would require more specialized Turkish etymological sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T15:03:12.012Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/shish_kebab",
 "prompt": "Give the English etymology of shish kebab: source language (Armenian? Turkish şiş kebap), date of first attestation, components şiş 'skewer' + kebap, and any Persian or Arabic involvement."
}
```


### [2026-09-05T15:03:16.602Z] TOOL RESULT

```
# English Etymology of Shish Kebab

**Source Language:** Turkish

**Components:** The term derives from Turkish *şiş kebap*, where *şiş* means "skewer" and *kebap* means "kebab."

**Date of First Attestation:** Not specified in the provided content.

**Persian or Arabic Involvement:** The dictionary entry does not mention Persian or Arabic origins. It traces the word exclusively to Turkish sources.

**Summary:** According to Wiktionary, shish kebab entered English from Turkish *şiş kebap* as a compound of two Turkish words denoting the cooking method and food type respectively.
```


## [2026-09-05T15:03:26.880Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%AE' --note 'page 106, root Cixa, Persian six \"skewer\": Wiktionary etymology (cognate with Skt sikha?)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%C5%9Fi%C5%9F' --note 'page 106, Turkish sis \"skewer\" < Proto-Turkic *sil, no Persian origin' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/shish_kebab' --note 'page 106, English shish kebab < Turkish sis kebap' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/shish%20kebab' --note 'page 106, English shish kebab 1913 < Armenian shish kabab < Turkish sis kebap' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%86%DB%8C%D8%B1%D9%87' --note 'page 106, Persian cira \"victorious\" (Steingass/Hayyim; no etymology given)' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


## [2026-09-05T15:03:29.499Z] TOOL CALL #52: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg106.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/106.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image to audit folder"
}
```


### [2026-09-05T15:03:30.089Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6e20d0869c10b3b1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d67f16c9f4d4aba3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/69b9b9a37c427dd4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eaa350f0c8b78298.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/11a05704eec6b295.txt
```


### [2026-09-05T15:03:30.145Z] TOOL RESULT

```
total 2900
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 11:03 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r-- 1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
```


## [2026-09-05T15:03:48.325Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### HRN siegreich/cir\"; python3 $S HRN.txt \"siegreich|tapfer\" 200 8",
 "description": "Grep Horn for siegreich/tapfer"
}
```


### [2026-09-05T15:03:49.946Z] TOOL RESULT

```
### HRN siegreich/cir
[leaf 27] .... asi- 'Gier ; phlv. äs, äzmand, äzvar,
19. äzäd *frei', äzöde.
.^^x^^ aw. äzäta- *frei, edel*; phlv. azät, arm. LW. azat,
azatak, vergl. atarrj tXsv&soia sc. napd Ils()(T(ag (Hes.).
kurd. aza *brav, tapfer* (Houtum-Schindler).
20. äzär Xeid*, azärden^ azdris; äzerden^ äzerm^).
aw. a + [/'zar-j azärayeiMi sie peinigen' ; phlv. äzär,
äzartan etc.; ai. [/har- 'zürnen.
21. äzmUden 'erproben, versuchen', Pr...
---
[leaf 89] ...er para) — V^vciz-, 'herum- bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Pleja...
---
[leaf 89] ... bezw. weg-
fliegen , vergl. vazaiti er fliegt*.
306. jyerwerden ernähren, erziehen*, periveris, perwer'tden,
pari -f- y^hhar-; phlv. partoarfan, partvar(i)sn,
307. pervez 'siegreich*.
phlv. aparvej 'siegreich'; wohl zu «r^i, be.ze (No. 253)?
Dann perwez.
308. pervfn 'Plejaden*.
aw. paoiryaeinyas\ca (yt. 8, 12), de Lagarde, Beitr.
z. altb. Lex. 56.
af/. peröne; bei. panvar 'Plejaden (Dam es, 54).
309. perh...
---
[leaf 99] .... patrast,
353. perähen 'Hemd*.
phlv. patrahan *ßock' (Yätkär-T Zarir. 64 Note 53),
perähen (PPGL).
kurd. LW. pirun, perlen 'Hemd'; wa/. parhän, sar.
harhän 'Weiberhemd'.
354. perö^, arab. LW. ß:rüz 'siegreich' ; j^frö^e 'Türkis,
arab. LW. flröze, fairüzaj,
aw. "^paiti.raocah-; iphlv, peröd, peröÖkar, päz. |?eröi.
Vergl. lat. piroses, quod bellorum victor interpretatur
(Ammian. Marc. XIX, 2, 11), arm. Pero...
---
[leaf 157] ...c^ 'glänzend, leuchtend, strahlend' ;
ai. ruksd' 'glänzend'.
oss. d. ro/s^ t. rü/s 'Licht, leuchtend', rü/say (214);
ya;'n. ru/sinie.
Gehört np. ru/ 'Wange' auch zu derselben Wurzel?
611. red 'weise, tapfer' (z. B. Sahn. I, 149 Vers 365; Vis
und Rämin S. 13, V. 5 v. u.).
aw. ratU' 'Herr'; phlv. rat, -rat^),
612. rezm 'Schlacht, Kampf.
aw. vergl. areza- 'Schlacht'; arm. LW. paterazm
'Kampf, auch razm.
An...
---
[leaf 214] ...e zu lesen vorschlägt, der kamer eda- als aus
Vermischung der Wörter ai. kakühh-, kakud-, skr.
kapdla-^ lat. caput und ai. mürdhän- entstanden an-
sieht).
kenär s. keran (No. 846).
868. kund 'stumpf; tapfer*.
skr. (bezw. präkr.) kunfha- 'stumpf.
Vergl. Rückert, ZDMG. 8, 280.
np. ktmdaver hat nach Nöldeke (mündliche Mit-
teilung) im Öähnäme immer die Bedeutung 'stolz'.
»J Nöldeke, Pars. Studien II, 40.
U...
---
[leaf 251] ...230 —
V
1025. neberd "Kampf, newerd, neberde 'tapfer (Sahn. I, 93
Vers 586).
aw. *ni -r l/^parU^ peretente sie kämpfen'; phlv.
n{i)part "Kampf (AV.).
Vergl. np. äwerd "Kampf (Sahn. I, 218 Vers 1506),
äwerdgäh (häufig), äweriden,
1025*»*« nebld, nebtd '...
---
```


## [2026-09-05T15:03:50.203Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### FSD shish\"; for f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do echo \"--$f\"; python3 $S $f \"shish[- ]kebab|shish\" 200 3; done",
 "description": "Grep Funk Wagnalls for shish"
}
```


### [2026-09-05T15:03:54.968Z] TOOL RESULT

```
### FSD shish
--FSD_vol1.txt
[leaf 216] ...be  In- vested with  divine  authority.  Tho  Assassins  became  for- midable during  the  crusades,  but  were  suppressed  by  Bi- bars, sultan  of  Egypt,  In  1272.  [F.,  <   Ar.  Hashshashln,
hashish-eaters,  <   hashish,  hashish.]—  as-sns'sln*bug",  ti. Any  bug  of  the  family  Reduriidx;  the  cannibal  bug. as-sas'sl-nate,  1   n-sas'i-net;  2   ft-sus'i-nut,  r.  [-nat'ed; -nat'ing.]  I. ...
---
[leaf 216] ...divine  authority.  Tho  Assassins  became  for- midable during  the  crusades,  but  were  suppressed  by  Bi- bars, sultan  of  Egypt,  In  1272.  [F.,  <   Ar.  Hashshashln,
hashish-eaters,  <   hashish,  hashish.]—  as-sns'sln*bug",  ti. Any  bug  of  the  family  Reduriidx;  the  cannibal  bug. as-sas'sl-nate,  1   n-sas'i-net;  2   ft-sus'i-nut,  r.  [-nat'ed; -nat'ing.]  I.  t.  1.  To  murder, ...
---
[leaf 216] ...thority.  Tho  Assassins  became  for- midable during  the  crusades,  but  were  suppressed  by  Bi- bars, sultan  of  Egypt,  In  1272.  [F.,  <   Ar.  Hashshashln,
hashish-eaters,  <   hashish,  hashish.]—  as-sns'sln*bug",  ti. Any  bug  of  the  family  Reduriidx;  the  cannibal  bug. as-sas'sl-nate,  1   n-sas'i-net;  2   ft-sus'i-nut,  r.  [-nat'ed; -nat'ing.]  I.  t.  1.  To  murder,  as  treac...
---
--FSD_vol2.txt
[leaf 411] ...Indian hemp,  and  also  the  resinous  matter  exuding  from  them.  3.
An  intoxicating  preparation  of  this  plant,  either  smoked or  drunk  or  taken  in  confections.  See  bhang.  [<  Ar. hashish,  hay.)  hasch'Ischf;  hascfa'lshf;  hash'ashf;
hash'ecshf.  „   ..  .   .   „   iiasi-ena,  pp.  nastenea.
Hs-slii'ya,  X   hn-Shl'ya;  2   ha-shi'ya,  n.  pi.  A   Somail  tribe  of  hast'en-er,  1...
---
[leaf 433] ...—  b. -palm,  n.  The  tall chamierops  (Qhamsearops  excelsa),  a   palm  of  Nepal  and China,  yielding  a   fiber  used  Instead  of  hemp.— h. -resin, n.  The  substance  variously  known  as  hashish,  bhang,  chur- Tus,  etc.,  extracted  from  the  hemp  of  India.— h. -seed,  «. The  seed  of  hemp:  used  as  food  for  oago-birds,  and  valued for  the  oil  expressed  from  it.— h.-strlngt,...
---
[leaf 470] ...  flexible  tube  with  a   mouthpiece the  air  In  the  vessel  Is  exhausted  and  the  smoke  drawn through  the  water.  [   <   Hind,  hugea,  <   Ar.  hugga,  pipe for  smoking.]  hoo'kaht.
Tarshish  ...  is  loss  cUstinBaished  by  its  apes,  ivory,  and  pea- cocks, than  its  hookaht.
Eayabd  Taypor  Lands  of  Ihe  Saracen  p   179  [o.  p.  p.  18S5.1 Hooke,  1   huk;  0   hdbk,  Bobert  ...
---
--FSD_vol3.txt
NO MATCH
--FSD_vol4.txt
[leaf 100] ... ican jurist.  Justice  of  the  Supreme  Court  of  Pennsylvania Sha-m'hen,  X   6h&-rQ'hen,  2   8ha-ru'h6n,  n   Bib  Tosh xix,  6
shas,  1   Shos  2   shas,  «   The  Talmud  an  abbreviation  of Shisha  sedarim  (the  six  orders)  its  rabbinical  name shasht,  n   1   A   sash  2   The  scarf  of  a   turban Slia'shal,  X   ShS'^al,  2   sha'shi,  n   Bib  Ezra  x,  40 Sha'shak,  1   Shg'Shak,  ...
---
[leaf 354] ...s Thar'ra,  1   tbaria,  2   tharia  n   Bib  (Apocrypha)  Esth \U,  1   —   Thar-se'as,  1   fha--sl'as  2   thar-sC'as,  n   Bib (Douai)  — Thar'shlsh,  1   fliari^ih,2thar'flhisb,  n   Same as  Tarshish
Tha'sos,  1   ChS'sos,  2   thfi'sfis,  n   A   Grecian  Island  near  S   E Thrace,  85  sq  m   autonomous  in  government  Tha'- sust  —   Tha'sl-an.o  &n
Thas'pl-um,  1   fhas'pi-um,  2   this'pi...
---
[leaf 635] ... C   *   A/  *   5   TT »,  1,  3, 6.  6,  7,  8.  9,  12,  13,  15,  16.  17,  19,  20,  21,
22,  23,  24*.  25  -har'li-kln*,  C*  Af*  ir  * TTr,  4,  11,  24*  — har'll-kwln,  E   f ,   14,  18
hashish,  haSb'iSh*  C   2   Af'S  Tr  *,  1,  3,  5, 6,  7,  8.  9.  12.  15  16‘.  20,  21,  22,  23  24,  25  — ha-^I^b'*,Tr*  11,16*  — haSb'ISb.A? ,— ho^h- ISb',  Af  *,— haSh-I^h',  TTr haslet,  haa'Ie...
---
```


## [2026-09-05T15:04:05.268Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### ARY چیر\"; python3 $S incoming/ARY/ARY_pages.txt \"چیره|چیر \" 250 5; echo \"### ARY سیخ\"; python3 $S incoming/ARY/ARY_pages.txt \"سیخ\" 250 5",
 "description": "Grep Aryanpur for chir and six"
}
```


### [2026-09-05T15:04:06.873Z] TOOL RESULT

```
### ARY چیر
NO MATCH
### ARY سیخ
NO MATCH
```


## [2026-09-05T15:04:10.719Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la incoming/ARY/ | head; grep -c \"چ\" incoming/ARY/ARY_pages.txt; grep -c \"سیب\\|سیر\" incoming/ARY/ARY_pages.txt",
 "description": "Sanity-check ARY file"
}
```


### [2026-09-05T15:04:10.808Z] TOOL RESULT

```
total 9460
drwxrwxr-x  3 sfmqrb sfmqrb    4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb    4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 8102112 Sep  4 14:06 ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  586473 Sep  4 14:06 ARY_latin_index_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  960497 Sep  4 14:06 ARY_pages.txt
drwxrwxr-x  2 sfmqrb sfmqrb   20480 Sep  4 13:30 ARY_pages.txt.pages
1572
21
```


## [2026-09-05T15:04:19.680Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B6%E0%A4%BF%E0%A4%96%E0%A4%BE",
 "prompt": "Sanskrit शिखा (śikhā): meanings, etymology (from śikhara? any PIE root?), related term शेखर (śekhara), and descendants. Also note whether Mayrhofer or any source is cited."
}
```


## [2026-09-05T15:04:21.240Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && S=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/g.py; echo \"### POK sikha\"; python3 $S POK_full.txt \"çikhā|sikhā|çikha-|sikha-\" 200 6; echo \"### IEC\"; python3 $S IEC.txt \"sikha|skewer\" 200 5",
 "description": "Grep Pokorny and Mann for sikha"
}
```


### [2026-09-05T15:04:26.149Z] TOOL RESULT

```
# शिखा (śikhā) - Sanskrit Etymology and Meanings

## Meanings
According to the Wiktionary entry, Sanskrit शिखा has several definitions:
- "plume, tuft of hair"
- "peacock's crest"
- "ray of light" (with synonym किरण)
- "a part of a verse" (in poetry contexts)

## Etymology
The Sanskrit etymology section states the source material is incomplete: "(This etymology is missing or incomplete. Please add to it...)" The only comparative reference provided is to Persian جیغه (jiġa), with no connection to शिखर (śikhara) or Indo-European roots mentioned in the available content.

## Scholarly References
The document cites two major philological sources:
- Monier Williams' *Sanskrit-English Dictionary* (1899)
- Ralph Lilley Turner's *Comparative Dictionary of the Indo-Aryan Languages* (1969-1985)

Neither Mayrhofer nor specific etymological derivations from शेखर are discussed in this Wiktionary entry.

## Descendants
The word produced descendants in Pali (sikhā) and various Prakrit forms, eventually reaching Sinhalese (සී).
```


### [2026-09-05T15:04:28.425Z] TOOL RESULT

```
### POK sikha
NO MATCH
### IEC
[leaf 77] ...’. Cf. bhraio Alb. birë “hole; OHG bora 'gimlet; OE, MLG bor, id.
bhrkos, à, o(n) (1) ‘spike, splinter ` Lat. (ambig.) furca 'fork, prop, gibbet" beside forco *ploughpoint'; Ir. cf. (either) briogún ‘skewer (or) bráca ‘harrow’, brácaim, v. “har- row’ (*-T-); Srb. Slovene bøk ‘moustache’; Cz. brk ‘quill’; Pol. barki, pl. ‘shoulders’; Lusat. cf. bórkać (‘root up ground": Ir. brá- caim); Li. birka ‘tally-s...
---
[leaf 348] .... n. 'graving- tool; késtra, f. ‘pike’; cf. also (?) ág-kistron, n. “hook, barb’; LW in Lat. cestrum ‘borer, dagger, graving-tool beside caestrum, id. (infl. of caedo); MIr. casar ‘thorn, bodkin,
615
skewer, brooch" Ir. casair, f. id.; W cethr, pl. -i, m. “spike, nail
Ket-
Skt. såtayami, Sataye “cut, divide, destroy’; pp: Satáh & śitáh as adj. ‘sharpened; sharp’; LW in Arm. satakem “kill, destroy; W cid...
---
[leaf 649] ...ol- (4) and skel- (3)
skolos, à, is ‘spike, crag. WP II, 591. Cf. skel-, skol-, etc. Oss. Kala, s. (2) ‘branch’; Gk. skólos, on, mn. ‘stake, thorn, mattock’; Alb. hell, pl. bej, m. ‘spit; awl; sting; skewer; icicle? beside hej, m. ('icicle; stalactite’, fr. *skolio-); OCS (and com. Sl.) skala, f. ‘rock, stone’
skopeið, skopio ‘cut, strike’. Cf. skopos. (Vo- calism of Balto-S1. ambig.) Br. skei, pp: skoe...
---
[leaf 693] ...‘chip’; Du. spijl, f. ‘spike, railing,
spid- — spitolos, a, ios (spitul-)
20
25
30
35
40
45
1258
rod'; E spile ‘peg, spigot, pile of timber, stack’; Norw. spile, s. ‘lath, stay’; Cz. spile, f. ‘spit, skewer’; Pol. $pila, f. id.; Big. spila, f. ‘rock, cliff; Li. spylys, gs: -io, m. ‘spit, prick- le’; spyl...
---
[leaf 700] ...futa, v. (thrust", from speud- or sputio); Du. spuiten, tr. ‘inject; intr. ‘spurt’; ME spouten, v. ‘spout; Sw. sputa, v. id.; Li. spüdZiu, spüdéti, v. (“have stitch in the side: ON spýta, v. inf. ‘to skewer’; mod. ‘to spurt’). Nominal types: Du. spuit, f. ‘squirt, jet, waterspout'; Li. spüdus, adj. ‘tight; spüdis, gs: spüdZio, m. ‘squeeze’
spur- (1) “foul; filth' Gk. cf. spurás, gs: -ádos, f. & spuratho...
---
```


## [2026-09-05T15:05:45.508Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"cirya\\|ciriya\\|tarya\" KNT.txt | head -10; echo \"---(no match above means silent)\"; grep -c \"\" KNT.txt",
 "description": "Grep Kent for cirya"
}
```


### [2026-09-05T15:05:45.578Z] TOOL RESULT

```
707:Perhaps [valrtaryaiy DB 4.44, for vartayaty.
3011:imf. ind., as object of preceding Auramazdüha vartaryary 1 appeal to Ahuramazda’, DB 4.44f.
---(no match above means silent)
5869
```


## [2026-09-05T17:21:27.138Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"cirya\" KNT.txt | head; echo \"--- KNT cirya: none above = silent\"",
 "description": "Confirm Kent silent on cirya"
}
```


### [2026-09-05T17:21:27.202Z] TOOL RESULT

```
--- KNT cirya: none above = silent
```


## [2026-09-05T17:25:47.130Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 - <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\ndata = {\n \"pdf_page\": 106,\n \"book_page\": 76,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Čirya, Cirya, Cairya, Carya\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Young Avestan čirya- 'able, capable, brave' (Bartholomae, AiW col. 598)\",\n   \"note\": \"The Avestan adjective is real and Nourai's gloss is essentially right. Bartholomae, Altiranisches Wörterbuch col. 598 (BRT.txt leaf 350): \\\"j. čirya- Adj. 'tüchtig, tapfer': pąsnuš narš 'yō taxmō Aog. 84. Ob zum V. ²čar-? — np. čīra. — Pü.: čīr, čērīh\\\" — i.e. the word is attested once, in the late Avestan Aogəmadaēčā §84, and Bartholomae himself already connects it with NP čīra and Pahlavi čīr/čērīh, which is exactly the chain Nourai draws. Buck, Dictionary of Selected Synonyms, lists 'Av. čirya-, darši-, darəyu-' in the word-table of §16.52 BRAVE, the section that begins at the foot of p. 1150 — so SYN:1150 is a correct citation. Two things are not right. (a) The language label: there is no Old Persian *čirya-; Kent's Old Persian lexicon has no such entry (grep of KNT.txt: no hit), so the box should read 'Avestan' alone. (b) 'Cirya, Cairya, Carya' are Nourai's own spelling variants of the one Avestan word, not attested by-forms; Mo'in's footnote in Borhan-e Qāṭeʿ (printed p. 677) quotes the stem as čira-, and Bartholomae's only reservation is whether čirya- belongs to the verb ²čar-. The gloss 'quick' is Mo'in's زرنگ rather than Bartholomae's 'tüchtig, tapfer'.\",\n   \"note_fa\": \"ریشهٔ این خانواده صفت اوستایی čirya- «توانا، دلیر» است که بارتولمه در ستون ۵۹۸ فرهنگ ایرانی باستان آورده و خودْ آن را با فارسی نو «چیره» و پهلوی čīr / čērīh پیوند داده است؛ این واژه تنها یک بار در متن اوستایی متأخر «اوگمدَ‌ئیچا» بند ۸۴ به کار رفته است. باک نیز در بخش ۱۶٫۵۲ (BRAVE) صفحهٔ ۱۱۵۰ همین صورت اوستایی را در جدول «دلیر» آورده، پس ارجاع نورایی درست است. اما برچسب زبانی «اوستایی / پارسی باستان» نادرست است: در پارسی باستان چنین واژه‌ای گواهی نشده و در واژه‌نامهٔ کنت نیامده است؛ همچنین صورت‌های Cairya و Carya صورت‌های نویسه‌گردانی خودِ نورایی‌اند نه گونه‌های ضبط‌شده. معنی «تند و چابک» برگرفته از حاشیهٔ معین («زرنگ») است نه از بارتولمه. در مجموع ادعای نورایی با احتیاط پذیرفتنی است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%DA%86%DB%8C%D8%B1%D9%87\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"BRT:598\", \"status\": \"supports\", \"note\": \"Bartholomae AiW col. 598, found in BRT.txt leaf 350 (the OCR leaf order is scrambled; neighbouring leaves 349/351 carry cols 595-597 and 599): \\\"• j. čirya- Adj. 'tüchtig, tapfer': pąsnuš narš 'yō taxmō Aog. 84. Ob zum V. ²čar-? — np. čīra. — Pü.: čīr, čērīh, Sü.: saṃgrāma...\\\". Nyberg independently cites the same place as 'Av. (598) čirya-', which fixes the column number.\"},\n    {\"ref\": \"BQT:676\", \"status\": \"partial\", \"note\": \"The Borhan entry چیر with Mo'in's footnote is at BQT_v2_pages.txt leaf 134, i.e. printed p. 677 by the running offset (leaf+543), one page off Nourai's citation. Footnote: «اوستا čira (زرنگ، شجاع) «بارتولمه ۵۹۸» ... «معین ...»». So Mo'in supports the Avestan connection and the Bartholomae column, but quotes the stem as čira- (not čirya-) and says nothing about Old Persian.\"},\n    {\"ref\": \"SYN:1150\", \"status\": \"supports\", \"note\": \"Buck, Selected Synonyms: §16.52 BRAVE starts at the foot of p. 1150 (SYN.txt leaf 1234 ends '16.52 BRAVE Grk. θρασύς, τολμηρός...'), and the word table on the facing page reads 'Av. čirya-, darši-, darəyu-'. Buck offers no further etymology of the Avestan word.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"col. 598 (BRT.txt leaf 350)\", \"stance\": \"supports\", \"note\": \"\\\"j. čirya- Adj. 'tüchtig, tapfer' ... Aog. 84 ... np. čīra. — Pü.: čīr, čērīh\\\"\"},\n    {\"src\": \"SYN\", \"where\": \"pp. 1150-1151, §16.52 BRAVE\", \"stance\": \"supports\", \"note\": \"table entry 'Av. čirya-, darši-, darəyu-' under BRAVE\"},\n    {\"src\": \"NYB\", \"where\": \"Part II Glossary p. 57 s.v. cēr (NYB_vol2_glossary.txt leaf 65)\", \"stance\": \"supports\", \"note\": \"\\\"cēr [cyl] brave, valiant, courageous 3¹⁸, 161¹⁵. — Av. (598) čirya-; MPrth comp. <cy>rdr, sup. cyryst, cyyrtwm, Sogd. 3514 sq.; Paz. cēr ... NP cēr. cērēh bravery, courage\\\" — Nyberg gives exactly Nourai's Avestan→Pahlavi→NP chain\"},\n    {\"src\": \"KNT\", \"where\": \"Old Persian lexicon, whole file\", \"stance\": \"silent\", \"note\": \"grep -i 'cirya' in KNT.txt returns nothing; Kent knows no Old Persian *čirya-, so the 'Old Persian' half of the language label is unsupported\"},\n    {\"src\": \"BQT\", \"where\": \"printed p. 677 (BQT_v2_pages.txt leaf 134), footnote to چیر\", \"stance\": \"partial\", \"note\": \"«اوستا čira (زرنگ، شجاع) «بارتولمه ۵۹۸»» — Avestan yes, Old Persian no, and the stem quoted as čira-\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"cĕr, čĕrîh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Book Pahlavi čēr [cyl] 'victorious, triumphant, brave' with the abstract čērīh 'bravery, victory' and the denominative čērīhistan 'to triumph' (MacKenzie, Concise Pahlavi Dictionary p. 24). It continues Old Iranian *čirya- (Av. čirya- 'able, brave') by the regular Middle Persian treatment of the sequence -irya-, which contracts to -ēr-, exactly as Av. airya- 'Aryan' > MP ēr (whence ērān) and Av. *bairya- > MP bēr; the yod is absorbed and the preceding i lengthened/lowered to the majhūl ē. Manichaean Middle Persian writes cyr, and Parthian has the same stem with comparative <cy>rdr and superlative cyryst / cyyrtwm (Nyberg, Manual of Pahlavi II p. 57), showing the word was common West Iranian, not a learned Avestanism. čērīh is čēr + the ordinary MP abstract suffix -īh. Nourai's Pahlavi glosses 'strong, brave, quick, dominating' are Mo'in's rendering; the dictionaries give 'victorious, brave'.\",\n     \"derivation_fa\": \"پهلوی čēr (نوشتار: cyl) به معنی «پیروز، غالب، دلیر» و مصدرِ حاصلی آن čērīh «دلیری، پیروزی» و فعل čērīhistan «چیره شدن» (مکنزی، فرهنگ کوچک زبان پهلوی، ص ۲۴). این صورت دنبالهٔ ایرانی باستان *čirya- (اوستایی čirya-) است: خوشهٔ -irya- در فارسی میانه به‌ ـēr بدل می‌شود، درست همان‌گونه که اوستایی airya- «آریایی» در فارسی میانه ēr (و ērān) شده است؛ یعنی «ی» میانجی جذب شده و مصوت پیشین به ای مجهول کشیده گردیده است. در پارسی میانهٔ مانوی cyr و در پارتی همین ستاک با صفت برتر cyrdr و برترین cyryst آمده است (نیبرگ، ج ۲، ص ۵۷)، پس واژه‌ای ایرانی غربی و رایج بوده نه وام‌واژه‌ای اوستایی. پسوند ـīh نیز پسوند معمول اسم‌مصدرساز پهلوی است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"BQT:676\", \"status\": \"supports\", \"note\": \"On the same Borhan page (BQT_v2_pages.txt leaf 134 = printed 677) the footnote to چیری reads «... بهلوی čēr ... čīrīh ... ؛ غالب شدن، ظفر یافتن. رک: چیره» — Mo'in gives precisely the Pahlavi forms Nourai puts in this box, though he writes the abstract čīrīh (Nourai čĕrîh).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 24 s.v. čēr (PHD.txt leaf 45)\", \"stance\": \"supports\", \"note\": \"\\\"čēr [cyl | M cyr, N ~] victorious, triumphant, brave. ~īh: bravery. čērīhistan, čērīh- [cylyh-stn'] triumph, be victorious\\\"; MacKenzie's English index (leaf 181) also lists 'victorious abarwēz, čēr, pērōz(gar)'\"},\n      {\"src\": \"NYB\", \"where\": \"Part II Glossary p. 57 (leaf 65)\", \"stance\": \"supports\", \"note\": \"\\\"cēr [cyl] brave, valiant, courageous ... — Av. (598) čirya-; MPrth comp. <cy>rdr, sup. cyryst, cyyrtwm ... Paz. cēr ... NP cēr. cērēh bravery, courage\\\"\"},\n      {\"src\": \"BQT\", \"where\": \"printed p. 677, footnote to چیری\", \"stance\": \"supports\", \"note\": \"«بهلوی čēr ... čīrīh ... غالب شدن، ظفر یافتن»\"},\n      {\"src\": \"HRN\", \"where\": \"whole dictionary\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no numbered entry for čīr/čīra (searched 'čir', 'siegreich', 'tapfer' in HRN.txt; only pērōz no. 354 and parwēz no. 307 come up for 'siegreich')\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"čîr\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP چیر čīr 'dominant, victorious' is the direct continuant of MP čēr; the Middle Persian majhūl ē is written ی in New Persian and is pronounced ē in Classical/Dari and ī in modern Iranian Persian (the same development as MP šēr > شیر 'lion', MP dēw > دیو). Bartholomae already registers the descendant as 'np. čīra' under Av. čirya- (AiW 598). The chart's extra forms are the ordinary NP derivatives: چیره čīra from MP *čērag with the regular loss of final -g after a, and چیرگی čīragī = چیره + -ī, in which the -g- of the older -ag stem reappears before the suffix (like بنده/بندگی, زنده/زندگی). Borhan-e Qāṭeʿ p. 677 defines چیر as «غالب شدن و ظفر یافتن و مستولی گردیدن بر دشمنی ... و شجاع و دلاور را نیز گویند» and چیره as «مستولی شدن و تسلط یافتن»; the Vīs-o-Rāmīn line Nourai quotes («همی تا آز باشد بر جهان چیر») is a genuine 11th-c. attestation of the predicative use. Modern Persian normally uses چیره; bare چیر survives mainly in poetry.\",\n     \"derivation_fa\": \"«چیر» در فارسی نو بازماندهٔ مستقیم پهلوی čēr است؛ ای مجهولِ فارسی میانه در فارسی نو با «ی» نوشته می‌شود و در فارسی کلاسیک و دری ē و در فارسی امروزِ ایران ī تلفظ می‌گردد (همانند šēr > شیر و dēw > دیو). بارتولمه نیز ذیل čirya- اوستایی صورت «np. čīra» را آورده است. مشتق‌های حاشیهٔ چارت طبیعی‌اند: «چیره» از *čērag پهلوی با افتادن ـگ پایانی، و «چیرگی» از چیره + ی که در آن گافِ ستاک کهنِ ـag پیش از پسوند باز می‌گردد (مانند بنده/بندگی). برهان قاطع (ص ۶۷۷) چیر را «غالب شدن و ظفر یافتن و مستولی گردیدن بر دشمنی ... و شجاع و دلاور» معنی کرده و شاهدِ ویس و رامین که نورایی آورده گواهی اصیل سدهٔ پنجم هجری است. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%86%DB%8C%D8%B1%D9%87\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BRT:598\", \"status\": \"supports\", \"note\": \"AiW col. 598 s.v. čirya- ends '— np. čīra. — Pü.: čīr, čērīh' — Bartholomae himself makes the New Persian word the descendant.\"},\n      {\"ref\": \"BQT:676\", \"status\": \"partial\", \"note\": \"The entry is at printed p. 677 (BQT_v2_pages.txt leaf 134), one page later than the citation: «چیر - بر وزن میر بمعنی غالب شدن و ظفر یافتن و مستولی گردیدن بر دشمنی باشد - و شجاع و دلاور را نیز گویند»; footnote «اوستا čira (زرنگ، شجاع) «بارتولمه ۵۹۸»». Content supports; page number off by one.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"printed p. 677, headwords چیر / چیره / چیری\", \"stance\": \"supports\", \"note\": \"«چیره - بمعنی مستولی شدن و تسلط یافتن ...»; footnote to چیری: «از: چیره (چیرگه) + ی (مصدری). حاصل مصدر چیره» and «پهلوی čēr ... čīrīh»\"},\n      {\"src\": \"BRT\", \"where\": \"col. 598\", \"stance\": \"supports\", \"note\": \"'np. čīra' listed as the descendant of Av. čirya-\"},\n      {\"src\": \"NYB\", \"where\": \"Part II p. 57\", \"stance\": \"supports\", \"note\": \"'NP cēr' given as the modern reflex of Pahlavi cēr\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, whole file\", \"stance\": \"silent\", \"note\": \"Hübschmann has no entry for čīr/čīra (searched the transliterations in HUB.txt)\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no hit for چیر/چیره; the Persian OCR of this scan is very thin (only 21 hits for سیب/سیر in the whole file), so the silence is not evidential\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/چیره\", \"stance\": \"partial\", \"note\": \"confirms the word and its senses 'prevailing, victorious; brave, strong' with a Rumi quotation, citing Steingass 1892 and Hayyim 1934, but gives no etymology section\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Čîxâ, Čixâ, Čĕxara\",\n   \"verdict\": \"transcription_suspect\",\n   \"modern_form\": \"Sanskrit शिखा śikhā- 'tuft, crest, point, tip' and शेखर śekhara- 'crest, peak, diadem'\",\n   \"note\": \"Two separate problems. (1) The form: there is no Sanskrit *čikhā or *čekhara. The words Nourai means are śikhā- (शिखा) 'tuft of hair, crest, point, tip, flame-point' and śekhara- (शेखर) 'crest, peak'. He took them from Horn, Grundriss p. 168 no. 762, who prints them in the 19th-century transliteration as 'çikha-' and 'çekhara-' (ç = ś); Nourai read the cedilla-c as č and consequently filed the whole entry under Č in his alphabet. The printed page 76 does show 'Čîxâ, Čixâ, Čĕxara', so the extraction is faithful and the error is the book's; it is systematic in this dictionary — the same substitution appears in čakta (= śakta 'able'), čvitra (= śvitra 'white'), črî (= śrī) elsewhere in the data. (2) The gloss and the arrow: śikhā never means 'skewer'; that sense belongs only to the Persian word. Horn does not derive NP sīx from Sanskrit — he writes 'skr. çikha- \\\"Spitze (eines Pfeiles etc.)\\\", vergl. çekhara- (?)', i.e. a cognate comparison, and Hübschmann (Persische Studien p. 250) lists sīx 'Bratspiess' among the New Persian words whose x answers Sanskrit kh (sāx 'branch' = skr. śākhā, mēx = skr. mayūkha, nāxun = skr. nakha), which is inherited cognacy from Proto-Indo-Iranian *ćikʰ-, not a loan out of Indic. Neither Pokorny nor Mann has the family (no hit for śikhā), and Wiktionary marks the Sanskrit etymology 'missing or incomplete'; śikhā- has no accepted PIE source.\",\n   \"note_fa\": \"این ریشه دو اشکال دارد. نخست صورت واژه: در سنسکریت *čikhā و *čekhara وجود ندارد؛ واژه‌های مقصود śikhā (شیخا) «کاکل، تارک، نوک» و śekhara «تارک، تاج» هستند. نورایی آن‌ها را از هرن (ص ۱۶۸، شمارهٔ ۷۶۲) گرفته که به شیوهٔ نویسه‌گردانی سدهٔ نوزدهم «çikha-» و «çekhara-» نوشته است؛ نورایی ç را č خوانده و کل مدخل را زیر «چ» جای داده است. تصویر صفحهٔ چاپی ۷۶ نشان می‌دهد که خودِ کتاب «Čîxâ» چاپ کرده است، پس خطای خوانشِ اسکن نیست بلکه خطای خودِ کتاب است و در سراسر این فرهنگ تکرار شده (مانند čakta = śakta و čvitra = śvitra). دوم جهت پیکان: śikhā هرگز به معنی «سیخ» نیست و هرن نیز فارسی «سیخ» را از سنسکریت نگرفته، بلکه آن دو را هم‌ریشه دانسته است؛ هوبشمان (مطالعات فارسی، ص ۲۵۰) «سیخ» را در کنار «شاخ» (= śākhā) و «میخ» و «ناخن» در فهرست واژه‌هایی آورده که «خ» فارسی در برابر kh سنسکریت است، یعنی هم‌ریشگی از هندوایرانی آغازین *ćikʰ- نه وام‌گیری. پوکورنی و مان نیز این خانواده را ندارند و ویکی‌واژه ریشه‌شناسی śikhā را ناتمام می‌داند. پس: خطای چاپی/نویسه‌گردانی کتاب، و افزون بر آن جهت اشتقاق نادرست است.\",\n   \"error_in\": \"book\",\n   \"book_prints\": \"Čîxâ, Čixâ, Čĕxara\",\n   \"correct_form\": \"śikhā- (šikhā), śekhara- (šekhara)\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%AE\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"HRN:168\", \"status\": \"partial\", \"note\": \"Horn, Grundriss p. 168 (HRN.txt leaf 189) no. 762: \\\"sēx (mit i auf be..., Saʿdī, Gul. 46 ...) 'Bratspiess'. skr. çikha- 'Spitze (eines Pfeiles etc.)', vergl. çekhara- (?). kurd. sīx, siyū 'Lunte'; bel. sīh, sī 'Bratspiess, Ladstock'.\\\" The page really is the source of Nourai's two Sanskrit words and of the gloss 'point', but Horn prints ç (= ś), not č, marks çekhara- with a question mark, and offers a comparison, not a derivation.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"p. 168 no. 762\", \"stance\": \"partial\", \"note\": \"\\\"skr. çikha- 'Spitze (eines Pfeiles etc.)', vergl. çekhara- (?)\\\" — comparison only\"},\n    {\"src\": \"HUB\", \"where\": \"p. 250 (HUB.txt leaf 260); also p. 78 (leaf 88) ad Horn 762\", \"stance\": \"contradicts\", \"note\": \"\\\"... sīx 'Bratspiess' H. 762; sāx 'Zweig' = skr. çākhā-; mēx 'Pflock, Nagel', vgl. skr. mayūkha-; nāxun 'Nagel', skr. nakha-\\\" — Hübschmann files sīx among inherited Iranian words that correspond to Sanskrit kh-words, i.e. cognates, not Indic loans; at Horn 762 he adds only 'Auch das Afghanische hat six'\"},\n    {\"src\": \"POK\", \"where\": \"POK_full.txt, whole file\", \"stance\": \"silent\", \"note\": \"no hit for śikhā/çikhā/sikha-; the family has no Pokorny entry\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, whole file\", \"stance\": \"silent\", \"note\": \"no 'sikha' lemma; Mann's 'skewer' glosses belong to unrelated roots (bhrkos, skolos, spid-)\"},\n    {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/शिखा\", \"stance\": \"partial\", \"note\": \"gives śikhā 'plume, tuft of hair; peacock's crest; ray of light', citing Monier-Williams 1899 and Turner CDIAL, with the etymology explicitly flagged 'missing or incomplete'; no 'skewer' sense\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"sîx\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP سیخ sīx 'skewer, spit, iron rod'. The relation to Sanskrit śikhā 'point, tip' is real but is cognacy, not descent: Proto-Indo-Iranian *ć gives Skt ś but Iranian s, and PIIr *kʰ gives Skt kh but Iranian x, so an inherited *ćikʰ- yields Skt śikhā beside Iranian *six-. This is precisely how Hübschmann files the word (Persische Studien p. 250: 'sīx \\\"Bratspiess\\\" H. 762; sāx \\\"Zweig\\\" = skr. çākhā-; mēx ... nāxun ...'), and Horn only writes 'vergl.'. No Middle Persian *sēx is attested (MacKenzie has no entry), and Wiktionary's Persian entry leaves the etymology open with the query 'Cognate with Sanskrit शिखा?', so an unbroken Old→Middle→New Persian line cannot be documented; the word is first securely met in classical New Persian (Horn cites Saʿdī, Golestān 46; Borhan quotes Golestān «هزار مرغ بسیخ»). The chart's extra سیخونک sīxūnak 'goad, prod, a poke' is a New Persian derivative of سیخ with the diminutive/instrumental -ūnak, not an old form. Kurdish sīx / Baluchi sīh, sī (Horn 762) and Pashto six (Hübschmann p. 78) are the Iranian cognates. Verdict plausible: the etymological connection Nourai draws is the one his sources make, but the arrow Sanskrit → Persian misrepresents a sister relation as a borrowing, and the root box's 'skewer' gloss is a back-projection of the Persian meaning.\",\n     \"derivation_fa\": \"«سیخ» در فارسی نو به معنی میلهٔ آهنی نوک‌تیز برای کباب کردن. پیوند آن با سنسکریت śikhā «نوک، تارک» راست است اما پیوندِ هم‌ریشگی است نه اشتقاق: *ć هندوایرانی آغازین در سنسکریت ś و در ایرانی s می‌شود و *kʰ در سنسکریت kh و در ایرانی x؛ پس از *ćikʰ- در هند śikhā و در ایران *six پدید می‌آید. هوبشمان (ص ۲۵۰) دقیقاً همین را می‌گوید و «سیخ» را در کنار «شاخ» (śākhā)، «میخ» و «ناخن» می‌آورد، و هرن هم تنها «vergl.» (بسنجید) نوشته است. در فارسی میانه صورت *sēx گواهی نشده (مکنزی مدخلی ندارد) و ویکی‌واژه نیز ریشه‌شناسی را باز گذاشته است؛ کهن‌ترین گواهی‌ها فارسی دری‌اند (سعدی، گلستان). «سیخونک» نیز مشتق فارسی نو از سیخ با پسوند ـونک است، نه صورتی کهن. هم‌ریشه‌های ایرانی: کردی sīx، بلوچی sīh/sī و پشتوی six. داوری: با احتیاط پذیرفتنی است؛ جهتِ پیکان (سنسکریت ← فارسی) خویشاوندی را به وام‌گیری بدل کرده است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%AE\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1203\", \"status\": \"partial\", \"note\": \"The Borhan headword سیخ with Mo'in's etymological footnote is in BQT_v2_pages.txt at leaf 667, i.e. printed p. ~1210 by the running offset (leaf+543) — about seven pages after Nourai's citation, so the page number cannot be confirmed. The entry itself is there: «سیخ ... معرب «سیخ» ... ترکی «شیش» ... آلتی باریک و دراز که قطعات گوشت را بدان کشند و کباب کنند، بابزن» with the Golestān shāhed «... هزار مرغ بسیخ»; the footnote cites هوبشمان together with Kurdish, Baluchi (فتیله) and Gilaki forms. Mo'in gives no Sanskrit ancestor and no borrowing claim.\"},\n      {\"ref\": \"HRN:168\", \"status\": \"supports\", \"note\": \"Horn no. 762 is exactly the source of this box: 'sēx ... Bratspiess. skr. çikha- Spitze (eines Pfeiles etc.), vergl. çekhara- (?)' — though as a comparison, not a derivation.\"},\n      {\"ref\": \"FVF:383\", \"status\": \"not_checked\", \"note\": \"Emam Shushtari, Farhang-e Vāžehā-ye Fārsi dar Zabān-e ʿArabi — refs_online.json records no accessible copy (noorlib/ketabnak need a browser login); nothing on disk.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"p. 168 no. 762\", \"stance\": \"partial\", \"note\": \"\\\"skr. çikha- 'Spitze (eines Pfeiles etc.)', vergl. çekhara- (?). kurd. sīx, siyū 'Lunte'; bel. sīh, sī 'Bratspiess, Ladstock'\\\"\"},\n      {\"src\": \"HUB\", \"where\": \"p. 250 and p. 78 (ad Horn 762)\", \"stance\": \"contradicts\", \"note\": \"treats sīx as inherited Iranian, cognate (not descended) — 'six \\\"Bratspiess\\\" H. 762; sax \\\"Zweig\\\" = skr. çakha-'; and 'Auch das Afghanische hat six'\"},\n      {\"src\": \"BQT\", \"where\": \"printed p. ~1210 (leaf 667), s.v. سیخ\", \"stance\": \"partial\", \"note\": \"«آلتی باریک و دراز که قطعات گوشت را بدان کشند و کباب کنند، بابزن»; footnote cites هوبشمان + Kurdish/Baluchi/Gilaki, no Sanskrit\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, whole file\", \"stance\": \"silent\", \"note\": \"no Middle Persian *sēx / *sīx entry — the word has no Pahlavi attestation\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no hit for سیخ; this scan's Persian OCR is too sparse for the silence to count\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/سیخ\", \"stance\": \"partial\", \"note\": \"Persian سیخ 'skewer': etymology flagged incomplete, with the editorial query 'Cognate with Sanskrit शिखा (śikhā)?'; the page lists Chagatai, Uzbek, Uyghur, Ottoman Turkish, Armenian and Turkmen borrowings OF the Persian word\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Turkish\",\n     \"words\": \"šîš; šîšlîk; šîš-kabob\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"Turkish şiş 'skewer, spit, knitting needle' is not a borrowing of Persian sīx. It is inherited Turkic, from Proto-Turkic *sīĺ 'spit, pointed stick or pole', whose ĺ gives š in Common Turkic (Turkish şiş) against the l-type reflex in Chuvash, with Turkmen çiş as the cognate; the word is Old Turkic and passed into Ottoman as شیش. Phonetically a Persian sīx could not yield šiš at all: Persian s- does not become Turkish ş-, and Persian -x is regularly kept as -h/-k or dropped in Turkic loans, never turned into -ş. Persian سیخ was in fact borrowed the other way, into Chagatai, Uzbek, Uyghur, Ottoman and Turkmen, as a separate word alongside native şiş. Al-Unaysi, whom Nourai cites, likewise calls Arabic شيش Turkish, not Persian (TAD_pages.txt leaf 45: «شيش ... تركي «شيش»», footnote «القضيب من الحديد ويُشك فيه اللحم ليُشوى ... وفصيحه السَّفُّود»). şişlik is şiş + the Turkic denominal suffix -lIk (in modern Turkish şişlik means 'swelling', from the homophonous şiş 'swollen'; the dish-name şışlıq belongs to Crimean Tatar and Azerbaijani, whence Russian шашлык). şiş kebap is şiş + kebap, the latter from Arabic kabāb 'roast meat'. So the node's words and glosses are right, but the derivation from Persian sīx is disputed.\",\n     \"derivation_fa\": \"«شیش» ترکی به معنی سیخ و میل، وام‌واژه‌ای از فارسی «سیخ» نیست. این واژه ترکی اصیل است و از ترکی آغازین *sīĺ «سیخ، چوب نوک‌تیز» می‌آید؛ ĺ در ترکی مشترک به ش بدل می‌شود (ترکی استانبولی şiş) و در ترکمنی çiş بازتاب یافته است، و صورت آن در ترکی باستان و عثمانی گواهی شده. از نظر آوایی هم اشتقاق از فارسی ممکن نیست: «س» فارسی در ترکی «ش» نمی‌شود و «خ» پایانی هرگز به «ش» بدل نمی‌گردد. برعکس، «سیخ» فارسی خودْ به چغتایی، ازبکی، اویغوری، عثمانی و ترکمنی وام رفته و در کنار şişِ بومی نشسته است. طوبیا العنیسی نیز که نورایی به او استناد کرده، «شيش» عربی را ترکی می‌داند نه فارسی. şişlik از şiş + پسوند ـlIk است (در ترکی امروز به معنی «ورم»؛ نامِ خوراک şışlıq از تاتاری کریمه و آذربایجانی است که از راه روسی شاشلیک گسترش یافته)، و şiş kebap از şiş + kebap (این دومی از عربی «کباب»). پژوهش امروزی پیکانِ فارسی ← ترکی را رد می‌کند.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%C5%9Fi%C5%9F\",\n      \"https://en.wiktionary.org/wiki/%D8%B3%DB%8C%D8%AE\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"TAD:38\", \"status\": \"partial\", \"note\": \"Al-Unaysi, Tafsīr al-alfāẓ al-dakhīla, TAD_pages.txt leaf 45 (printed ≈ p. 40 on the leaf−5 offset, so Nourai's 38 is close but not exactly verifiable): «شيش — ... تركي «شيش» معناه ...» with the footnote «القضيب من الحديد ويُشك فيه اللحم ليُشوى ... وفصيحه السَّفُّود». The reference confirms the word and the meaning but assigns it to Turkish, not to Persian.\"},\n      {\"ref\": \"BQT:1203\", \"status\": \"partial\", \"note\": \"The Borhan footnote to سیخ (leaf 667, printed ≈1210) does mention «ترکی «شیش»» beside the Kurdish/Baluchi/Gilaki forms, but Mo'in only juxtaposes the Turkish word; he does not derive it from Persian.\"},\n      {\"ref\": \"MON:2112\", \"status\": \"partial\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. شیشلیک: «[تر. به معنی سیخی] (امر.) کباب سیخی، طرز تهیهٔ آن چنین است ...» (MON_part1.txt; same text in the Adena 2-vol reprint). Mo'in tags the word Turkish, which supports a Turkish source for the Persian word but says nothing in favour of Persian sīx > Turkish şiş.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/şiş\", \"stance\": \"contradicts\", \"note\": \"Turkish şiş 'skewer; rapier; knitting needle' < Ottoman Turkish شیش < Proto-Turkic *sīĺ 'spit, pointed stick or pole', cognate Turkmen çiş; 'No Persian origin is mentioned'. Derived terms şişlemek, şiş kebap, şiş köfte\"},\n      {\"src\": \"TAD\", \"where\": \"leaf 45 (printed ≈40), s.v. شيش\", \"stance\": \"contradicts\", \"note\": \"«تركي «شيش»» — al-Unaysi's own book of foreign words in Arabic classes it as a Turkish, not a Persian, loan\"},\n      {\"src\": \"MON\", \"where\": \"s.v. شیشلیک\", \"stance\": \"partial\", \"note\": \"«[تر. به معنی سیخی]» — Turkish, glossed 'of the skewer'\"},\n      {\"src\": \"LKT\", \"where\": \"Lokotsch, whole file\", \"stance\": \"silent\", \"note\": \"no entry for schisch/şiş or kebab in LKT.txt (the neighbouring Oriental food and utensil words such as ḥašīš no. 839 and bakhšīš no. 178 are there, so the silence is real)\"},\n      {\"src\": \"BQT\", \"where\": \"printed ≈1210, footnote to سیخ\", \"stance\": \"partial\", \"note\": \"«ترکی «شیش»» quoted alongside, without a direction of borrowing\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"šîšlîk; šîškabâb\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both Persian words are modern Turkic loans, as the chart says. شیشلیک šīšlīk is Turkic şiş + -lIk; Mo'in's dictionary tags it explicitly «[تر. به معنی سیخی]» and defines it «کباب سیخی» with a long recipe (marinated loin and tail-fat threaded four pieces of meat to one of dunbe on a long thin skewer). The suffix is not analysable in Persian, which shows the word was taken over whole; the dish-name entered Persian in the late Qajar/Pahlavi period, most likely through Caucasian-Turkic and Russian usage (Russian шашлык from Crimean Tatar şışlıq), which is why Persian has šīšlīk beside the older native کباب. شیش کباب šīškabāb is Turkish şiş kebap 'skewer roast', the second element itself Arabic kabāb; in Persian it is a transparent tautology beside the native kabāb, and it is the less usual of the two forms. Neither word contains anything Iranian: they are Turkic compounds re-borrowed into Persian, so the arrow Turkish → Persian is right.\",\n     \"derivation_fa\": \"هر دو واژه وام‌واژه‌های نوِ ترکی‌اند و پیکان چارت درست است. «شیشلیک» از şiş ترکی + پسوند ـلیک است؛ معین در فرهنگ فارسی آن را با برچسب «[تر. به معنی سیخی]» آورده و «کباب سیخی» معنی کرده و دستور پخت آن را نیز به تفصیل داده است. پسوند ـلیک در فارسی تحلیل‌پذیر نیست و همین نشان می‌دهد واژه یکپارچه وام گرفته شده است؛ نام این خوراک در اواخر دورهٔ قاجار و دورهٔ پهلوی، به احتمال بسیار از راه کاربرد ترکیِ قفقاز و روسی (روسی шашлык از تاتاری کریمه şışlıq)، وارد فارسی شده است. «شیش کباب» نیز همان şiş kebap ترکی است که جزء دومش خود عربیِ «کباب» است؛ در فارسی کنار «کباب» بومی حشو می‌نماید و کم‌کاربردتر است. هیچ‌یک عنصر ایرانی ندارد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%C5%9Fi%C5%9F\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:2112\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Fārsi s.v. شیشلیک (MON_part1.txt): «شیشلیک: [تر. به معنی سیخی] (امر.) کباب سیخی، طرز تهیهٔ آن چنین است: مقداری گوشت راستهٔ قرمز و به اندازهٔ یک چهارم آن دنبه را قطعه قطعه کرده ...». Exactly Nourai's claim that the Persian word comes from Turkish. (Page 2112 is of Mo'in's 6-vol Amir Kabir edition; only the 2-vol Adena reprint is on disk, so the page itself could not be matched.)\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. شیشلیک (MON_part1.txt and the Adena 2-vol reprint)\", \"stance\": \"supports\", \"note\": \"«[تر. به معنی سیخی] ... کباب سیخی»\"},\n      {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt and BQT_v3/4 OCR\", \"stance\": \"silent\", \"note\": \"Borhan-e Qāṭeʿ (a 17th-c. dictionary) has no شیشلیک / شیش کباب — expected, since the word is a modern loan\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/şiş\", \"stance\": \"supports\", \"note\": \"lists şiş kebap / şiş kebabı among the derived terms of Turkish şiş, and şişlik as a -lik derivative\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"shish kebab\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English shish kebab is first recorded in 1913 and comes, per Etymonline, 'from Armenian shish kabab, from Turkish siskebap, from sis \\\"skewer\\\" + kebap \\\"roast meat\\\"'; Wiktionary gives the same source without the Armenian step. The Armenian mediation is the usual account, the word having reached American English through Armenian and Levantine restaurant usage rather than directly from Ottoman Turkish. kebab itself is older in English (1783) and is Arabic kabāb by way of Persian/Urdu usage in India — Hobson-Jobson p. 138 s.v. Kabob quotes Forbes, Or. Mem. (1814) 'a dish common in Arabia called Kabob ... meat cut into small pieces and placed on thin skewers'. That Funk & Wagnalls (1913 first ed., 1940 printing) has no entry for shish kebab, while it does have kabob, fits the 1913 date exactly. The node is correct as drawn: the English word comes from Turkish, not from Persian.\",\n     \"derivation_fa\": \"«shish kebab» انگلیسی نخستین بار در ۱۹۱۳ ثبت شده و بنا بر اتیمانلاین از ارمنی shish kabab و آن از ترکی şiş kebap («şiş» سیخ + «kebap» کباب) گرفته شده است؛ ویکی‌واژه نیز همان خاستگاه ترکی را می‌دهد بی‌آنکه واسطهٔ ارمنی را بیاورد. راهِ ورودِ واژه به انگلیسی آمریکایی از طریق رستوران‌داران ارمنی و شامی بوده است نه مستقیم از ترکی عثمانی. خودِ kebab پیشتر (۱۷۸۳) در انگلیسی هست و از عربی «کباب» از راه کاربرد فارسی و اردو در هند آمده؛ هابسن‌جابسن (ص ۱۳۸، ذیل Kabob) شاهدی از ۱۸۱۴ می‌آورد: «خوراکی رایج در عربستان به نام کباب ... گوشتِ ریزشده که بر سیخ‌های باریک می‌کشند». نبودِ مدخل shish kebab در فرهنگ فانک و واگنالز (چاپ ۱۹۱۳/۱۹۴۰) با همان تاریخ ۱۹۱۳ می‌خواند. این گره درست است.\",\n     \"sources\": [\n      \"https://www.etymonline.com/word/shish%20kebab\",\n      \"https://en.wiktionary.org/wiki/shish_kebab\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD:1196\", \"status\": \"not_checked\", \"note\": \"AHD:1196 is a page of the main text of the American Heritage Dictionary, New College Edition (1975/76), which is not on disk and is lending-only on archive.org; the local AHD file is Watkins's Indo-European Roots (1985), which by its nature has no shish kebab entry. The gloss Nourai quotes ('pieces of seasoned meat roasted and served on skewers') reads like the AHD definition, and AHD's own etymology is 'Turkish şiş kebap', so the citation is very likely accurate — but it could not be verified here.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"ETYMONLINE\", \"where\": \"etymonline.com/word/shish kebab\", \"stance\": \"supports\", \"note\": \"\\\"pieces of lamb or other meat grilled on skewers, 1913, from Armenian shish kabab, from Turkish siskebap, from sis 'skewer' + kebap 'roast meat'\\\"; kebab itself from 1783\"},\n      {\"src\": \"WIKT\", \"where\": \"en.wiktionary.org/wiki/shish kebab\", \"stance\": \"supports\", \"note\": \"\\\"from Turkish şiş kebap, şiş 'skewer' + kebap 'kebab'\\\"; no Persian or Arabic step for shish\"},\n      {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p. 138 s.v. Kabob / Kab-ab\", \"stance\": \"partial\", \"note\": \"1814, Forbes: 'a dish common in Arabia called Kabob or Kab-ab, which is meat cut into small pieces and placed on thin skewers, alternately between slices of onion and green ginger' — documents kabob in English, not the shish- compound\"},\n      {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls New Standard, all four volumes\", \"stance\": \"silent\", \"note\": \"no 'shish' entry anywhere in FSD_vol1-4 (kabob is present); consistent with a first English attestation only in 1913\"},\n      {\"src\": \"KLN\", \"where\": \"Klein 1966 and 1971 files\", \"stance\": \"silent\", \"note\": \"no 'shish kebab' headword in either printing\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat, Concise\", \"stance\": \"silent\", \"note\": \"no hit for shish/kebab\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1, s.v. kabob\", \"stance\": \"partial\", \"note\": \"'[pl.] (a) an Oriental dish, consisting generally of ... roast meat ... Also spelled kabob' — has kabob but not the shish- compound in the volume on disk\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith open('data/verification/page-106.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 -m json.tool data/verification/page-106.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 106",
 "description": "Write verification file and run check"
}
```


### [2026-09-05T17:25:52.117Z] TOOL RESULT

```
written
JSON OK
nodes verified: 6/6
node verdicts: {'confirmed': 4, 'plausible': 1, 'disputed': 1}
root verdicts: {'plausible': 1, 'transcription_suspect': 1}
ref checks: {'supports': 4, 'partial': 5, 'not_checked': 2}
books consulted: {'supports': 10, 'silent': 10, 'partial': 8, 'contradicts': 3} | by book: {'BQT': 5, 'WIKT': 5, 'PHD': 2, 'NYB': 2, 'HRN': 2, 'HUB': 2, 'ARY': 2, 'MON': 2, 'BRT': 1, 'TAD': 1, 'LKT': 1, 'ETYMONLINE': 1, 'HJB': 1, 'FSD': 1, 'KLN': 1, 'SKT': 1, 'WEB': 1}
```


## [2026-09-05T17:26:15.163Z] AGENT

Done — `data/verification/page-106.json` written, `verify_check.py 106` reports **0 PROBLEM lines** (6/6 nodes).

**Page 106 (book p. 76) — 2 real entries (2 redirects skipped)**

- Node verdicts: confirmed 4, plausible 1, disputed 1
- Root verdicts: plausible 1, transcription_suspect 1
- Ref checks: supports 4, partial 5, not_checked 2 (FVF:383 — no accessible copy; AHD:1196 — main-text page, only Watkins's IE-roots appendix is on disk)

**Flagged items**

- `transcription_suspect` — ROOT **Čîxâ, Čixâ, Čĕxara** [Sanskrit]: no such Sanskrit forms. They are śikhā- (शिखा) and śekhara- (शेखर); Nourai read Horn's 19th-c. "çikha- / çekhara-" (ç = ś) as **č** and filed the entry under Č. `error_in: book` — the printed page 76 does show "Čîxâ" (image saved to `data/verification/sources/refs/ocr/BOOK/106.png`), and the same ś→č substitution recurs elsewhere in the data (čakta = śakta, čvitra = śvitra, črî = śrī). Also the root gloss "skewer" is a back-projection: śikhā never means skewer, and Horn/Hübschmann make Persian sīx a **cognate**, not a descendant.
- `disputed` — #2 [Turkish] **šîš, šîšlîk, šîš-kabob**: Turkish şiş is inherited Turkic, from Proto-Turkic \*sīĺ 'spit' (Turkmen çiş), not from Persian sīx — Persian s- and -x cannot give ş…ş. Persian سیخ was in fact borrowed the *other* way into Chagatai/Uzbek/Uyghur/Ottoman/Turkmen. Nourai's own source al-Unaysi (TAD) calls Arabic شيش Turkish, and Mo'in tags شیشلیک «[تر.]».
- `plausible` — ROOT **Čirya** [Avestan / Old Persian]: the Avestan word is solid (Bartholomae col. 598 "čirya- 'tüchtig, tapfer'", Aog. 84; Buck §16.52 BRAVE at p. 1150; Nyberg II p. 57 cites the same column), but there is **no Old Persian \*čirya-** (Kent silent), so the language label is half wrong; "Cairya, Carya" are Nourai's own spelling variants.
- `plausible` — #1 [Persian] **sîx**: relation to śikhā is genuine but is Indo-Iranian cognacy (\*ćikʰ- → Skt ś/kh vs Ir. s/x, per Hübschmann p. 250 with sāx/mēx/nāxun), not descent from Sanskrit; no Middle Persian attestation.

**Confirmed:** Pahlavi čēr/čērīh (MacKenzie p. 24, Nyberg p. 57), Persian چیر (Bartholomae's own "np. čīra"), Persian شیشلیک/شیش کباب as Turkic loans (Mo'in), English shish kebab (1913, Etymonline/Wiktionary).

**Extraction errors: none.** The JSON matches the printed page exactly (including "cĕr, čĕrîh" with the inconsistent c/č, which is the book's own typography).

Page-number drift worth noting for the owner (book's citations, not extraction): BQT:676 → the چیر entry is on printed p. 677; BQT:1203 → the سیخ entry is at leaf 667 ≈ printed p. 1210; TAD:38 → the شيش entry sits at leaf 45 ≈ printed p. 40.
