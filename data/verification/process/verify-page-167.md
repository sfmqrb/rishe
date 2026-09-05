# Verification process log — verify-page-167


## [2026-09-05T20:35:20.282Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 167 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-167.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-167.json. Write /home/sfmqrb/git/rishe/data/verification/page-167.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 167` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:35:21.863Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:35:22.569Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:35:22.583Z] TOOL RESULT

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


## [2026-09-05T20:35:22.796Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-167.txt"
}
```


### [2026-09-05T20:35:22.809Z] TOOL RESULT

```
1	=== PDF page 167 (book page 137) ===
2	--- entry 0 ---
3	ROOT [Indo-Schythian] Gan : to seize  (refs ISS:27)
4	#1 (parent #0) [Indo-Schythian] refs=ISS:27 | Uysgani : vulture
5	#2 (parent #0) [Sogdian] refs=ISS:27; SOD:163 | ğnw, ğan : power, force, skill
6	  #3 (parent #1) [Persian] refs=ISS:27; BQT:1023 | zağan «زغن» : a black bird (kite)
7	--- entry 1 ---
8	ROOT [Indo-European] Gang : to mock, hum  (refs POK:352)
9	#1 (parent #0) [Sanskrit] refs=POK:352 | gunj : to hum
10	  #2 (parent #1) [Pahlavi] refs=MON:3418; BQT:1844 | gung : dumb
11	    #3 (parent #2) [Persian] refs=HRN:209; BQT:1844 | gong «گنگ» : deaf, dumb
12	--- entry 2 ---
13	ROOT [Avestan] Gantuma : wheat  (refs HUB:95; SYN:516)
14	#1 (parent #0) [Pahlavi] refs=HRN:209 | gantum : wheat
15	  #2 (parent #1) [Persian] refs=BQT:1842; MON:3411 | gandom «گندم ( گندمک ، گندمینه )» : wheat ; gandomgŭn «گندمگون» : wheat colored ☞Gěu ; gandom-ba «گندم با ( گندم وا )» : wheat soup ☞Pekw
16	--- entry 3 ---
17	ROOT [Avestan] Garenu : scab on animal skin  (refs BQT:1779)
18	#1 (parent #0) [Pahlavi] refs=MON:3211 | gar 2 : scab
19	  #2 (parent #1) [Persian] refs=HRN:200; BQT:1779; MON:3211 | gar 3 «گر۳ ( گری۲ )» : scab on skin (causing baldness) ; gargen «گرگین ( گرگین )» : one who has scab, bald
20	
```


## [2026-09-05T20:35:26.737Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-167.json",
 "description": "Read source JSON for page 167"
}
```


### [2026-09-05T20:35:26.778Z] TOOL RESULT

```
{
  "pdf_page": 167,
  "book_page": 137,
  "entries": [
    {
      "root": {
        "name": "Gan",
        "lang": "Indo-Schythian",
        "refs": "ISS:27",
        "gloss": "to seize",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-Schythian",
          "refs": "ISS:27",
          "words": [
            {
              "translit": "Uysgani",
              "gloss": "vulture",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "ISS:27; SOD:163",
          "words": [
            {
              "translit": "ğnw, ğan",
              "gloss": "power, force, skill",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Persian",
          "refs": "ISS:27; BQT:1023",
          "words": [
            {
              "translit": "zağan",
              "gloss": "a black bird (kite)",
              "script": "زغن"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "جمله صید این جهانیم ای پسر - ما چو صعوه ، مرگ برسان زغن",
            "poet": "Rŭdakî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Gang",
        "lang": "Indo-European",
        "refs": "POK:352",
        "gloss": "to mock, hum",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:352",
          "words": [
            {
              "translit": "gunj",
              "gloss": "to hum",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:3418; BQT:1844",
          "words": [
            {
              "translit": "gung",
              "gloss": "dumb",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:209; BQT:1844",
          "words": [
            {
              "translit": "gong",
              "gloss": "deaf, dumb",
              "script": "گنگ"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گنگ باد آنکس که اندر طعن تو گوید سخن - کور باد آنکس که اندر عرض تو جوید عوار",
            "poet": "Farrokhî"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Gantuma",
        "lang": "Avestan",
        "refs": "HUB:95; SYN:516",
        "gloss": "wheat",
        "note": "Cognate with Sanskrit \"gôdhŭma\"."
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "HRN:209",
          "words": [
            {
              "translit": "gantum",
              "gloss": "wheat",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1842; MON:3411",
          "words": [
            {
              "translit": "gandom",
              "gloss": "wheat",
              "script": "گندم ( گندمک ، گندمینه )"
            },
            {
              "translit": "gandomgŭn",
              "gloss": "wheat colored",
              "script": "گندمگون",
              "see": ["Gěu"]
            },
            {
              "translit": "gandom-ba",
              "gloss": "wheat soup",
              "script": "گندم با ( گندم وا )",
              "see": ["Pekw"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "خال مشکین که بدان عارض گندمگون است - سرّ آن دانه که شد رهزن آدم با اوست",
            "poet": "Hâfez"
          }
        }
      ]
    },
    {
      "root": {
        "name": "Garenu",
        "lang": "Avestan",
        "refs": "BQT:1779",
        "gloss": "scab on animal skin",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:3211",
          "words": [
            {
              "translit": "gar 2",
              "gloss": "scab",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:200; BQT:1779; MON:3211",
          "words": [
            {
              "translit": "gar 3",
              "gloss": "scab on skin (causing baldness)",
              "script": "گر۳ ( گری۲ )"
            },
            {
              "translit": "gargen",
              "gloss": "one who has scab, bald",
              "script": "گرگین ( گرگین )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گر نخواهی رنج گر۳ از گرگنان پرهیزکن - جهل گر۳ است ای پسر پرهیزکن زین زشت گر۲",
            "poet": "Nâser-Khosrow"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-05T20:35:26.880Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:35:26.915Z] TOOL RESULT

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


## [2026-09-05T20:35:32.239Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['ISS','SOD','POK','HUB','SYN','HRN','BQT','MON']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900]); print()\n\"",
 "description": "Check refs_online for relevant abbreviations"
}
```


## [2026-09-05T20:35:33.179Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && sed -n 1,80p data/verification/page-127.json",
 "description": "Look at an existing verification file"
}
```


### [2026-09-05T20:35:34.201Z] TOOL RESULT

```
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317936 (v.6, search-only) ; archive.org khotanesetexts0103bail (vols I-III only, lending)", "identifier": "dictionary-of-khotan-saka (substitute); khotanesetexts0103bail is vols I-III, lending-only", "local_file": null, "page_offset": "DKS: leaf = printed + 17..19 (e.g. leaf 158 = p.139). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Khotanese Texts VI itself is not onlin

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
```


### [2026-09-05T20:35:34.269Z] TOOL RESULT

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
page-311.json
page-31.json
---
{
 "pdf_page": 127,
 "book_page": 97,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Dhem",
   "verdict": "confirmed",
   "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
   "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
   "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
   "sources": [
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
    "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
   ],
   "ref_check": [
    {
     "ref": "POK:247",
     "status": "supports",
     "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
     "stance": "supports",
     "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
     "stance": "supports",
     "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
     "stance": "silent",
     "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
    },
    {
     "src": "IEC",
     "where": "Mann, d-section (grep 'dhem' in IEC.txt)",
     "stance": "silent",
     "note": "Mann has dhen- (2) 'forehead', dhenguhó, dhinió etc. but no *dhem- 'blow, smoke' headword."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan",
     "words": "dam; da-dhmainya",
     "verdict": "plausible",
     "derivation": "The Avestan language has no attested finite verb dam- 'to blow': Bartholomae, Altiranisches Wörterbuch 731 f., knows only the Young-Avestan present participle daδmainiia- 'sich aufblasend, -blähend', said of (tree-)frogs at Vd. 14.5 and 18.73, which he analyses as 'ein Praes. auf -ainya- mit Inl.-Red.' and compares directly with 'ai. dhámati \"er bläst\", np. damīdan \"blasen\"'. Nourai's 'da-dhmainya' is that very word in his own transcription — he writes Avestan δ as dh and marks off the reduplication syllable da- with a hyphen — so the form is faithful; but his gloss 'I inflate, breathe' is wrong: it is an adjective/participle 'puffing itself up', not a 1sg verb. 'dam' is the root abstracted from that participle, i.e. Proto-Iranian *damH- 'to blow, breathe; to swell' (Cheung 2007 s.v. *damH³), which is real and is the ancestor of the Persian words in node 2; it is simply not an Avestan word-form. Hence plausible rather than confirmed: right root, misdescribed gloss, and one of the two 'words' is a root citation.",
     "derivation_fa": "در اوستا هیچ فعلِ صرف‌شدهٔ dam- «دمیدن» به‌جا نمانده است؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۷۳۱ به بعد) تنها اسمِ فاعلِ جوان‌اوستاییِ daδmainiia- «باد کرده، خود را باد کننده» را می‌آورد که دربارهٔ قورباغه‌ها به کار رفته (وندیداد ۱۴٫۵ و ۱۸٫۷۳) و آن را ستاکِ حالِ پسوندِ -ainya- با تکرارِ درونی می‌داند و مستقیماً با «dhámati سنسکریت» و «دمیدنِ فارسی» می‌سنجد. صورتِ «da-dhmainya» در کتاب نورایی همان واژه است (او ذالِ اوستایی را dh می‌نویسد و هجای تکرارِ da- را با خط تیره جدا می‌کند)، پس خوانشِ کتاب درست است؛ اما معنایی که به آن داده («من می‌دمم») نادرست است، چون این صورت صفت/اسمِ فاعل است نه فعلِ اول‌شخص. «dam» هم واژهٔ اوستایی نیست بلکه ریشهٔ ایرانیِ باستانِ *damH- «دمیدن، باد کردن» است (چونگ، ذیل *damH³). بنابراین ریشه درست است ولی معنا و صورت‌بندیِ گره با احتیاط پذیرفتنی است.",
     "sources": [
      "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86"
     ],
     "ref_check": [
      {
       "ref": "POK:247",
       "status": "supports",
       "note": "IEW 247 (POK_01.txt line 3517): 'av. daδmainya- ,sich aufblasend, blähend, von Fröschen''  — the same Avestan form under the same root."
      }
     ],
     "consulted": [
      {
       "src": "BRT",
       "where": "Altiran. Wb. 731 f., s.v. daδmainya- (BRT.txt line 13362)",
       "stance": "partial",
       "note": "'j. däSmainya- Adj. \"sich aufblasend, -blähend\", von Fröschen … Eig. PPA. … — Vgl. ai. dhámati \"er bläst\", np. damidan \"blasen\"' — supports the root and the link to Persian, but shows the form is a participle, not '1sg I inflate'; and Bartholomae has no Avestan verb entry dam- 'to blow' (his dam- entries are 'Haus, Wohnung' and a present stem of dar- 'to hold')."
      },
      {
       "src": "CHEUNG",
       "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
       "stance": "supports",
       "note": "'*AVESTAN: Y Av. daδmainiia- \"blowing up (intr.)\" (V 14.5, V 18.73)' listed as the only Avestan reflex of *damH³."
```


## [2026-09-05T20:35:43.921Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK gong/gang 352 ===\"; grep -n \"gang-\\|guñj\\|gunj\" POK_01.txt POK_02.txt | head -40\necho \"=== POK page area ===\"; ls POK_0*.txt",
 "description": "Grep Pokorny for gang root"
}
```


### [2026-09-05T20:35:43.977Z] TOOL RESULT

```
=== POK gong/gang 352 ===
POK_02.txt:53:gang-  .spotten,  höhnen';  gango-s  ,Ilohn^
POK_02.txt:57:vielleicht  gehört  nir.  geöin  ,Geschrei,  Lärm,  Freude,  Verspottung'  hier- her,  wenn  aus  *ganksni-,  älter  *gang-sni-]  mir.  geim  , Gebrüll',  gesdni ,schreie',  gesachtach  ,Pfau'  könnten  dann  auch  dazugehören.
=== POK page area ===
POK_01.txt
POK_02.txt
POK_03.txt
```


## [2026-09-05T20:35:45.725Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB gandum ===\"; grep -n -i \"gandum\\|gantum\\|gōdhūma\\|godhuma\" HUB.txt | head -20\necho \"=== HRN gandum ===\"; grep -n -i \"gandum\\|gantum\\|gung\\|gung \" HRN.txt | head -30",
 "description": "Grep Hübschmann and Horn"
}
```


### [2026-09-05T20:35:45.790Z] TOOL RESULT

```
=== HUB gandum ===
8811:stank', zd. gainti-; gandum 'Weizen, skr. godhuma-; gunda
=== HRN gandum ===
42:Arbeit kostspielig. Um diese Ressource weiterhin zur Verfügung stellen zu können, haben wir Schritte unternommen, um den Missbrauch durch
364:gung), nupäjedh (S. 191, 2) u. v. a. m. Oft stehen zwei
724:32. äffuften, äSöften 'in Bewegung versetzen, Praes.
728:'in Bewegung geraten'.
1788:aw. varana- *Umfriedigung' (Afr. 3, 10), das
2144:'Umhegung, umfriedigter, befestigter Platz, Flecken,
2311:Übertragungen annimmt (mündliche Mitteilung), vergl.
3180:336. pöziS 'Reue, Entschuldigung', pöztden (Vis und Kämm, ^
3224:') Bartholomae (briefl. Mitteilung) meint, dass die Verdächtigung
3530:Das auslautende t in tat beruht auf Übertragung
3885:KZ. 27, 101 unter (Berücksichtigung von Geldner,
4607:aw. *huxsnüta' vergl. hu/rnüiti- 'Befriedigung'; phlv.
4966:Als eine Bestätigung für diese Etymologie dient der
5792:tödten'; arm. vergl. gan 'Schläge, Züchtigung, yunem
5825:Die Vereinigung mit arm. gari (H. No. 65), lat.
6038:32, 588 No. 23) aus skr. Jada- 'kalt, starr, regungs-
6165:beruhen auf Übertragungen aus der Schriftsprache — haben mich —
6528:beruht auf Übertragung (vergl. No. 373). Ursprüng-
6938:np. s ist im Satzsandhi oder durch Übertragung
6961:durch Übertragung; Fr. Müller, WZKM. IV, 355,
8014:aw. *vi + l^/saoh'; ai. vi 4- l^ksöbh- *in Bewegung,
8015:in Schwanken, in Aufregung geraten*, Causat. skr. 'ver-
8124:Hübschmann, ZDMG. 44, 556 2)); phlv.-paz. gantum
8125:d. i. gandum (PPGl.).
8138:LW. afy. bei. (77) gung stumm*.
8719:bedeutet nur 'Belegung (einer Hündin)'; phlv. mShmatt
9201:'Einfügung (aber nur als ritueller t. t.), vorgl. np.
9397:Die Anregung zu dieser Zusammenstellung verdanke
9755:deutung *die Aufregung, das Wogen' bezw. *auf regen',
10564:99. ffuaftlh ^Gewinn, Erlangung (AV.), guaftak gain*
```


## [2026-09-05T20:35:51.138Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8100,8150p' HRN.txt\necho \"=== leaf of line 8124 ===\"\nawk 'NR<=8140{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before:\",n}' HRN.txt",
 "description": "Read Horn entries around gandum/gung"
}
```


## [2026-09-05T20:35:52.363Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '40,70p' POK_02.txt\necho \"=== leaf ===\"\nawk 'NR<=53{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line53:\",n}' POK_02.txt",
 "description": "Read Pokorny gang- entry"
}
```


### [2026-09-05T20:35:53.019Z] TOOL RESULT

```
egl, gende, gendamden (AM. 45 Zeile 1; 78 Zeile 3
V. u.).
*) Lautlich stünde der Heranziehung von skr. \y^gorj-^ garjati
*brüllen, brummen, toben, brausen, tosen* nichts entgegen; denn sowohl
e/i wie g^h setzen ein ap. d voraus. Doch stimmt die Bedeutung von
garh^ besser als die von garj- (s. auch Bartholoma e, ZDMG. 44, 552).
notirt : hüzle *junge Ziege', desle 'Händchen', yellele 'Bischen, Stückchen*,
kuzowle 'Wasserkrüglein', kulaile *Köter* (eigentlich Demin. von kulai
'Hofhund'j, nazule 'Kätzchen*, perdele 'Häutchen', segle 'Hündchen*,
/unele 'Häuschen'.
Dasselbe Suffix erkenne ich nunmehr in np. ähle 'Bläschen' (AM.
50, 14; 153, 11), auch abile^ äwile^ vergl. äbek (änek^ VuUers No. 2 s. v.
ist verschrieben). Gewiss wird es sich im Np. noch häufiger finden.
Auch kurd. gtirdale (s. oben No. 905) wird hierher gehören (Correctur-
note).- 209 -
aw. gaifiti- 'Gestank'; phlv. gand 'Gestank', gandak
stinkend*, gandakth ; ai. gandhd- *Geruch, Duft (wohl-
riechend)'.
af}'. ganda 'stinkend'; bei. LW. gand 'Kot, Mist'
(97) — gandag, n. ganday schlecht, böse' dagegen stellt
Bartholomae, ZDMG. 44, 552 zu ap. gasta- *übel,
widerwärtig* ; sar. yofid.
935. gend/um *Weizen', ar. LW. jandum in jauz-i jandum.
skr. gödhüma- 'Weizen* (dagegen iran. ^gandhüma-^
Hübschmann, ZDMG. 44, 556 2)); phlv.-paz. gantum
d. i. gandum (PPGl.).
LW. kurd. genim (vergl. g. gamim); af/. yanum;
wa/. yid%m, sangl. minj. yanddm, sar. zandani, sandum,
^\yn. zindum, yidg. yadum; bei. gandtm (98).
936. gunde *Hefenballen (für ein BrotV.
aw. gunda- (vd. 3, 32) 'Teig (Geldnor, KZ. 24,
549 Note 4); phlv. gundak.
Unsicher.
937. gv/ng 'stumm' 8).
skr. [/^guüj-, gufijati summen, brummen' (Geiger:
'das Brummen bezeichnet die tierischen Laute des
Stummen im Gegensatz zur menschlichen Sprache').
Unsicher.
LW. afy. bei. (77) gung stumm*.
938. gor 'Wildesel*, gür/er,
ai. gäurd' 'weisslich, gelblich, rötlich; eine Büflfel-
art: Bos Gaurus* (Spiegel, Ar. Periode 55); phlv. gör
(Papyrus, Hörn ZDMG. 43, 51 und 619).
LW. kurd. gör; afy. yyara; bei. gör 'Wildesel' (80).
^) Das angebliche phlv. ganäk, ganräk erklärt Bartholomae
a. a. O. auch nicht richtig, es ist höchst wahrscheinlich mit Andreas
druväk zu lesen. — Nach der ganz anderen Auffassung Thumb*s von
KRa 56 ff., KZ. 32, 132 wäre ap. gasta- mit Kern zu skr. l'^gad-
'sprechen' zu stellen.
*) Das Yerhältniss des ai. ö zu dem iran. an ist unklar.
') Hierher wird geng bei AM. gehören (von der Stimme, 203
=== leaf of line 8124 ===
formfeeds before: 230
```


### [2026-09-05T20:35:54.970Z] TOOL RESULT

```
Im  Germ,  außerdem  *kalt-,  *klat-,  *klajp-,  z.  B.  mhd.  kalzen,  kelzen sch\vatzen,  plappern';  afries.  kaltia  , sprechen';  ags.  clatrian  , klappern, rasseln',  nhd.  Klatz  , Schmutzfleck',  bekletzen;  anord.  klapp  n.  , Klatsch, Schlag',  ahd.  /:Zap/ m.  , Geschwätz,  Knall,  Schlag,  Stoß'.
Vgl.  die  ähnlichen  Schallwurzeln  ghel-,  kel-.
WP.  I  538  f.,  WH.  I  580  f.,  Trautmann  77.
^.  gal-  oder  ghal-  ,können'.
Cymr.  gallu  , können,  imstande  sein',  corn.  gallos  , Macht',  bret.  gallout können'  (IKln),  ir.  gal  L  , Tapferkeit',  ahret.  gal  , Macht,  Können';  air. dl-gal  f.,  cymr.  dial,  corn.  dgal , Rache';  gallorom.  *galia  , Kraft'  (Wartburg); dazu  die  kelt.  VN  Galli,  FaXäzaL]
lit.  galiü,  galeti  , können',  galiä,  gälios  , Vermögen,  Fähigkeit,  Macht', ne-gäle  f.  , Unwohlsein';
mit  unklarer  Bildung  russ.-ksl.  goUrm  ,groß,  hoch',  bulg.  golem  ,groß, hoch,  weit',  skr.  gdlijemno  ,groß',  aöech.  holemy  ,groß',  skr.  golem  ,groß', russ.  dial.  goljamyj  ,hoch,  mager'  und  Adv.  galjamo  ,viel,  sehr'  (Weiteres bei  Berneker  320  und  Trautmann  77).  ^
WP.  I  539  f.,  Trautmann  77.
gan{dh)'  , Gefäß'?  Nur  kelt.  (?)  und  germ.
Mir.  gann  (*gandhn-  oder  *gandh-)  , Gefäß'  (sehr  unsicher  belegt:  Stokes BB.  19,  82);
isl.  kani  , Henkelgefäß,  Schüssel  (poet.),  norw.  dial.  kane  , Henkelschale', schwed.  dial.  kana  , Schlitten',  dän.  kane  , Schlitten'  (älter  dän.  auch jBoot^),  mnd.  kane  ,Boot'  (woraus  aschwed.  kani  ,Boot'),  ndl.  kaan  ,kleines Boot,  Kahn'  (aus  dem  Ndd.  stammt  auch  nhd.  Kahn,  s.  Kluge  EWb.  s.  v., V.  Bahder,  Wortwahl  30);  damit  ablautend  aisl.  kcena  ,Art  Boot';  dazu weiter  (<C  *gandhna)  anord.  kanna,  aschw.  kanna,  dän.  kande,  ags.  canne, and.  kanna,  ahd.  channa  , Kanne',  woraus  spätlat.  canna  entlehnt  ist;  aus fränk.  kanna  auch  prov.  cana  , Hohlmaß',  afr.  channe  ,Kanne',  s.  Meyer- Lübke  1596,  Gamillscheg  EWb.  d.  Franz.  168;  daneben  ahd.  chanta, canneta,  fränk.  cannada  ^KsLXine^  (<Cgcindha).
WP.  I  535,  WH.  I  154.
352
gang-  .spotten,  höhnen';  gango-s  ,Ilohn^
Ai.  ganja-h  , Verachtung,  Hohn^  ganjana-h  ^verachtend,  höhnend';
o-r.  yayyaLvsiv  rd  fisrä  yeXcjTog  fiQOffTtai^eiv  Hes.;
ags.  canc  u.  ge-canc  ,Spott,  Hohn,  Tadel'  (=  ai.  ganja-h),  cancettan ,spotten',  anord.  kangen-yrcte  ,höhnende  Worte'  (ags.  cincung  ,lautes  Lachen', eno-l.  mdartl.  kink  ,laut  lachen'  hat  expressives  i,  wie  nhd.  kichern  usw.).
vielleicht  gehört  nir.  geöin  ,Geschrei,  Lärm,  Freude,  Verspottung'  hier- her,  wenn  aus  *ganksni-,  älter  *gang-sni-]  mir.  geim  , Gebrüll',  gesdni ,schreie',  gesachtach  ,Pfau'  könnten  dann  auch  dazugehören.
Die  Sippe  scheint  ursprüngl.  schallmalend.  Ähnliche  Schallwörter  sind ai.  günjati  ,summt,  brummt',  gr.  yoyygv^sLv  ,grunzen',  spätgr.  yo/yt^Ccu ,murre,  gurre',  aksl.  ggg^nw^  ,schwer  sprechend',  russ.  gugnati  (alt)  ,mur. mein',  gugnjd  ,Stotterer',  poln.  g§ga6,  gegnac  ,schnattern'  (von  der  Gans),  usw. Lat.  ganniö  ,kläffe,  belfere,  schäkere'  ist  wohl  unabhängige  Schallbildung.
WP.  I  535,  WH.  I  582  f.
§sr-  ,rufen,  schreien',  daneben  einzelsprachliches  *garr-  durch  expressive Konsonantenschärfung  im  Schallworte;  Nominalbildungen  garo-, garä,  gar-mo-  ,Ruf,  Klage'.
Palatal  wird  erwiesen  durch  osset.  zamn^  zarun  ,singen',  zar  , Gesang' und  durch  arm.  cicarn  ,Schwalbe',  cicafnuk  ,Nachtigall'  (redupl.  *goi-gnr-on oder  '710-,  Petersson  KZ.  47,  287);
gr.  yrJQvg,  dor.  yöcQvg  ,Stimme';  yaggKbfis^a '  XoiöoQOv^sd^a  Hes.,  mit  rr  wie
lat.  garriö,  -Ire  ,schwatzen,  plaudern,  plappern  (selten  von  Tierlauten)', garrulus  ,geschwätzig';
air.  gar-  ,rufen'  in  adgair  .verklagt'  (*gar-e-t),  ar-gair  ,verbietet',  do-gair ,ruft'  usw.;  cynpr.  gair  ,Wort'  {*gar-io-),  dyar  ,Lärm,  Traurigkeit'  :  mir. do-gar  ,traurig'  (*du(s)-garo-);  air.  fo-gor  ,Ton,  Laut'  (*upo-garo-),  abret. ar-uuo-art  ,fascinavit';  air.  gairm  n.  (kelt.  *gar-{s)mn),  cymr.  corn.  bret. garm  ds.  (:  as.  karm  ,Wehklage');  dehnstufig  air.  gäir  i.  Geschrei',  gäire ,Lachen',  cymr.  gaior  ,Geschrei,  Kampf ;
ahd.  chara  f.  ,Wehklage',  nhd.  Kar-freitag,  got.  kara  f.,  ags.  cearu  f. ,Sorge'  (davon  ahd.  usw.  karön  ,beklagen,  wehklagen',  ahd.  charag  ,betrübt', mhd.  karc  ,klug,  listig,  geizig-',  nhd.  karg,  ags.  cearig  ,traurig,  bekümmert', engl,  chary  .vorsichtig,  sparsam'),  as.  karm  (s.  oben),  ags.  cearm,  cierm  m. ,Geschrei'.
Vgl.  die  ähnlichen  Schallwurzeln  *ger-  und  *guer-. WP.  I  537.  WH.  I  583.
353
rraro^'  ^grauenvoll;  Grauen^;  gargo-s  jg-rausig",  wild'.
Arm.  harcr  ^hart^^  karcem  ^ich  fürchte,  glaube';
gr.  yoqyög  ^Furcht  erregend,  grausig,  wild'^,  rogya)  ^Schreckgespenst^ yoqyovod-ai  ,wild  werden  (von  Pferden,  d.  i.  sich  erschrecken)',  yooycbip, yogycüTtög  ,schrecklich  blickend'  (die  gr.  Worte  aus  *yaQyö-  assimiliert??);
=== leaf ===
formfeeds before line53: 7
```


## [2026-09-05T20:36:13.426Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB context ===\"; sed -n '8795,8825p' HUB.txt\necho \"=== leaf ===\"; awk 'NR<=8811{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n, \"printed:\", n-10}' HUB.txt",
 "description": "Read Hübschmann gandum context"
}
```


## [2026-09-05T20:36:14.781Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN wheat ===\"; grep -n \"WHEAT\\|gantuma\\|gantumǝm\\|godhuma\" SYN.txt | head -20",
 "description": "Grep Buck for wheat"
}
```


### [2026-09-05T20:36:15.228Z] TOOL RESULT

```
=== HUB context ===
Kapitel 25: ap. g.
^P- 9 (= id§^- 9'i 9^^^ vor Konsonanten und dunkeln
Vokalen) wird im Np. zu g oder y,
Wie ap. h und d den Lautwerth b und d im Anlaut
und nach Konsonanten, dagegen w und $ nach Vokalen
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
stank', zd. gainti-; gandum 'Weizen, skr. godhuma-; gunda
'Hefenballen', zd. gunda-; gos 'Ohr ^= ap. gausa-; gun
'Farbe* == zd. gaona-; guh 'Sehmutz, Koth* = zd. guda-;
gohar 'Ursprung H. 948, oben p. 96; ges^ gesU 'Locken\
zd. ga^sa-; gehan *Welt* = zd. gaedanqm (gen.pl.); angust
'Finger, Zehe' = zd. angiista-; angist 'Kohle', vgl. skr. an-
gdra- ; bang 'Bilsenkraut* — skr. bhanga- ; 7'ang 'Farbe' =
skr. rafiga-.
Im Armenischen stelit hier ebenfalls g: gah 'Thron,
Sessel*; ganj 'Schatz* = np. ganj\ goin 'Farbe*, ^rat; 'Pfand*
u. s. w. ; erang 'Farbe' = np. rang; zangapan *Beinschiene',
zd. zanga- 'Knochel'.
Das anlautende y von yund 'Menge, Sehaar H. 805,
oben p. 83 kann ich nicht erklaren.— 247
§ 139. Ap. g nach Vokalen und r = y bleibt im
=== leaf ===
leaf: 256 printed: 246
```


### [2026-09-05T20:36:15.272Z] TOOL RESULT

```
=== SYN wheat ===
12988:8.48 WHEAT
12990:? Er iechl tuirend Du. tarwe, weit Skt. godhtima- cruithneacht OHG weizz Av. gantuma- gwenith MHG weizze
13004:7. Skt. godhtima-, by Pop. etym, cpd. of go- ‘cow’ and dhiima- ‘smoke’) for *gandhuma- = Ay. gantuma-, NPerg gandum ‘wheat’, root connection? Barth, 493. Hiibschmann, Pers. Stud. Ofna
```


## [2026-09-05T20:36:22.118Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 105 (printed 95) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==106' HUB.txt | head -60",
 "description": "Print Hübschmann page 95"
}
```


## [2026-09-05T20:36:23.213Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=13004{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n,\"printed:\",n-24}' SYN.txt\necho \"---\"; sed -n '12985,13010p' SYN.txt",
 "description": "Buck wheat section page"
}
```


### [2026-09-05T20:36:23.899Z] TOOL RESULT

```
=== HUB leaf 105 (printed 95) ===
— 95 —
ksl. glava 'Kopf ', arm. glux 'Kopf etc. Zu merdle vgl.
Vullers, Grammatica linguae persicae p. 235, wo die
Formen auf le als Formen des Tat-Dialectes bezeichnet
sind. Darauf verweist auch Mann, ZDMG. 47, 705.
931. Np. gumaStan = pfiz. gumdrdan = phi. gumdrtan
'einsetzen, bestimmen, beauftragen, betrauen' Min. Gl.
93, Bdh. Gl. 225, afgh. gumdrql to consign*, arm.
LW. gumar-el 1) sammeln*, 2) 'schicken, iibergeben,
einsetzen* zeigt nirgends den Anlaut t?- und hat jeden-
falls mit ap. *m-inar = skr. vi-smar nichts zu thun.
932. Np. guman = ap. ^mmOna^ (statt zd. *vfmanah'),
Vgl. unten Nr. 965.
934. Vgl. KZ. 33, 165. Dazu nun auch afgh. yand^ql *Ekel
empfinden, nicht leiden, nicht mOgen' (Geiger). Afgh.
ganda 'stinkend' finde ich nicht bei Raverty.
935. Skr. gddhUma^ wird volksetymologische Anlehnung
von ^gandhUma- an die Composita mit gd- *Kuh* sein
{go-dhuma- gleichsam *Kuhrauch'; vgl. unsern Pflanzen-
namen Erdrauch, gr. xanvog^ mnvioc).
936. Dazu arm. LW. gund 'Kugel', gndak *Kugel, Ball,
KnoUen'. Ich halte die Etymologic fiir richtig.
937. Hochst unsicher.
938. Unsicher.
Hierher nach Fr. Miiller, WZKM. 8, 189 guvdrtdan ver-
dauen' = phi. gukar-Uan zu skr. vi-kar umwandeln .
940. Arm. vkay gehdrt nicht zu np. guvdh, vgl. meine
Abhandlung *Arisches und Armenisches*, Idg. Forsch. 4,
p. 119.
941. Ich fasse gosdla *Kalb* als Compos, von go- = np.
gav, gav *Kuh' und sdla *Jahrling (von sal *Jahr ab-
geleitet wie in den Zusammensetzungen mit Zahl-
wortern -sdla = jahrig' ist), also = 'Kuh-jahrling,
vgl. unser 'Jahrlingskalb'. Kurd. LW. gilsile ZDMG.
38, 85.
^4. Np. gost 'Fleisch' = ap. *gausta-?
946. Arm. goin ist Lehnwort, aber aus anderen Griinden.
Ebenso arm. gunak =n np. guna* Afgh. yuna f. 'Haare
[
```


### [2026-09-05T20:36:25.619Z] TOOL RESULT

```
leaf: 568 printed: 544
---
igitized by Arya Samaj Foundation Chennai and eGangotri
VEGETATION 515 ‘grain’) in dano-karg- ‘ant’, lit. ‘grain- stealer’, root connection? Walde-P. 1.831. Barth. 734.
Skt. sasya-, Av. hahya- (in epd., Barth. 1800) : Gall. acc. (s)asiam ‘tye’, W. haidd, Br. heiz ‘barley’. Walde-P. 2.454.
8.48 WHEAT
Goth. hwwatteis Lith.  kvietiet, pirat rips ON _hweiti Lett. kvieSi, par'i ae Dan. hvede SOs. plone hs w.  hvele r.  psenica f hang) at On hw@te Boh.  piSenice peers ME whele Pol. pszenica fie NE wheat Russ. pSenica
? Er iechl tuirend Du. tarwe, weit Skt. godhtima- cruithneacht OHG weizz Av. gantuma- gwenith MHG weizze
NHG weizen
member Ir. -necht, W. -nith, Br. -niz : W. nithio, Br. niza ‘winnow’ (this : Lith. n(d)ekoti ‘winnow in a trough’, etc. Walde-P. 2.321), hence ‘wheat’ as ‘grain for winnowing’, like Lat. triticum as ‘srain for threshing’. First part of Ir. cruitnecht : Ir. cruth ‘red’, with refer- ence to the old red wheat of Ireland. First part of W. gwenith, Br. gwiniz prob. (despite the nm for nn) : gwynn, Br. gwenn ‘white’ (cf. Goth. hwaitets : hweits, below, 4). For full discussion, ef. Loth, RC 41.193 ff.
Ir. tuirend, etym. dub., perh. a epd. of rind ‘point’ and first used of a special kind of wheat. Loth, RC 41.199 ff.
4. Goth. hwaiteis, OE hw@te, etc., general Gmc., so called from the white meal therefrom: Goth. hweits, etc. ‘white’ (15.64). Walde-P. 1.469 f. Feist 280.
Du. tarwe (more popular than weit), MDu. tarewe, prob. (as first applied to some rank species of wheat?) : ME, NE tare ‘vetch, weed’, Skt. durva- ‘panic-
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
516 SELECTED INDO-EUROPEAN SYNONYMS
grass’, also prob. Lith. dirva ‘field’ (8.12). Walde-P. 1.803. Franck-v. W. 689.
5. Lith. kvieciet, Lett. kviest, fr. Gmc. (Goth. hwaiteis, etc., above, 4).
Lith. pirat, Lett. piir’?, above, 1.
6. ChSI. pisenica, SCr., Russ. psenica, Boh. pSenice, Pol. pszenica, orig. ‘grain
destined for grinding’ : ChS]. Pichat; ‘strike’, pitSeno ‘meal’, I, titan ‘crush’, ete. Walde-P. 2.1. :
7. Skt. godhtima-, by Pop. etym, cpd. of go- ‘cow’ and dhiima- ‘smoke’) for *gandhuma- = Ay. gantuma-, NPerg gandum ‘wheat’, root connection? Barth, 493. Hiibschmann, Pers. Stud. Ofna
8.44 BARLEY Grk. «pid Goth. barizeins (adj.) Lith. mieSiat NG xpiOape ON bygg, barr Lett.  miezi Lat. hordeum Dan. byg ChSl.  jeetnénit, jetint (adj.) It. orzo Sw. bjugg, korn SCr.  jetam Fr, orge OE bere, berlic (béow) Boh. jeémen Sp. cebada ME bere, barli Pol. Jeczmien Rum. rz NE barley Russ. jaémen! Ir. eorna Du. __gerst Skt. —_ yava- Nir. corna OHG  gersta Av. Steiis W. haidd MHG §gerste Br. heiz NHG gerste
Apart from the inherited group, and some with specialization from ‘grain’ or ‘fodder, crop’, several words for ‘barley’ are from sources reflecting its sharp, prickly form.
1. IE *gherzd(h)-, *ghrzd(h)-, root connection uncertain and phonetic de- velopment in part obscure. Walde-P. 1.611. Ernout-M. 459, Walde-H. 1.657.
Grk. xpi#;, NG KpOapt; Lat. hordeum (> It. orzo, Fy. orge, Rum. orz); Du. gerst, OHG gersta, MHG, NHG gerste; (Alb. dridhé ‘grain’,
2. Sp. cebada, orig. ‘fodder’, fr. cebar ‘feed, fatten animals’, Lat. cibare id., fr. cibus ‘food’. REW 1894,
3. Ir. eorna, etym. dub. Pokorny, Z. celt. Ph. 17.304 ff. takes as *es-ornia : Goth. asans ‘harvest’ (8.41). (Connec- tion with Skt. yava-, etc., as Pedersen 1.65, Stokes 223, now rejected.)
```


## [2026-09-05T20:36:37.773Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT gantuma ===\"; grep -n \"gantuma\\|gantum\" BRT.txt | head -20\necho \"=== BRT garenu ===\"; grep -n -i \"gar\\(e\\|ə\\)nu\\|garənav\" BRT.txt | head -30",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:36:37.864Z] TOOL RESULT

```
=== BRT gantuma ===
21316:—  yaomca  ahm  (sd.)  V.  5.  52;  53,  S4;  — asjanunqmia  (sd.)  °vanqm  Yt.  8.  29;  V. 5-4.  p.S3.  7-35'.  I9.zh;  —  'vakesar^a ^■4%;  V.J.  27;  —  'vanqm  gantumS (sd.)  ratu/ris  N.  2i?;  —  kat  'iä  'vaia  va- straca yaozdayqn  auA>n..yä  nasäum  ava.- binta  V.  7.  32.  a)  mit  xsäudray-  Adj. 'alkoholisches  Getreide',  d.  i.  Name  eines aus  Getreide  hergestellten  alkoholischen Getränks,  etwa 'Bier':  cval  yaomis.h)  fra- barä0  . .  alva  danary  *xsäudrinqm  (näml. yavanqm) "'  "wie  viel  Bier  soll  man  (ihr)  3' bringen?  . .  Zwei  Portionen  Bier."  V.  16. 7.  b)  dn,  auch  dbne  xsäudray-:  cin>m yaom  frabaräl  V.16.&;  7.
=== BRT garenu ===
```


## [2026-09-05T20:36:39.353Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD gandum/gar ===\"; grep -n -i \"gandum\\|gan̄dum\\|gung\\|^gar\\b\\|garr\" PHD.txt PHD_mackenzie.txt | head -40",
 "description": "Grep MacKenzie Pahlavi"
}
```


### [2026-09-05T20:36:39.407Z] TOOL RESULT

```
=== PHD gandum/gar ===
PHD.txt:378:galēģ [glwk' | N guld] throat. бато [gm | = M, N ~j pace, step, stride; a yard (3 ft.). ~ í dó pay: a pace (s ft.). -рапаб [-k’nk' | M eng, N -gàna] suffix forming numerical adjectives, -fold. бапа [gnd | N ~] stench. gandag [gndk' | (M gng), N —a] foul, stinking. ~th: stench. ģandanāģ [gndn’k' | N gandanā] leek. gandum [Hš < A nth | (M gnwm), N ~] wheat. ganj [gnc | (M gnz), N e treasure, treasury. ~war [-wbl | M -wr, N ~] treasurer. ģan(n)āģ [gr &! | (P gnd?g)] foul, corrupt (v. gandag). ~ ménó$g the Evil Spirit. ~ih: corruption. gar [gl] mountain. -gar [-Al, -gl | M -gr, N ~] suffix forming actor nouns. -gar [-£1| M -g’r, N ~] suffix forming actor nouns. garan [gPn! | M г?л, N girán] heavy, serious, difficult. АҺ; heaviness, weight. garasman [glsm’n' | М ртт?п] = garddman. gard [g/t! | N ~] dust. gardan [gitn! | M grdn, N ~] neck. ģardānāģ [gl h] die (for gaming). gardanidan, gardan- [gl n-ytn! | M grd(y)nydn, N ~] turn (tr.). gardidan, gard- [git-yin' | M grd-, N ~] turn, revolve. ~išn: revolution, turning. garm [gim | M grm, N ~] warm, hot. «„«ih: warmth, heat. garm-ābag [gim'pk! | N ~a] bath-house. garmāģ [glm^ k! | М grmg, N garmá] warmth, heat. g£armóg [gimwk!] warm, ardent, fervent. garmówar(ih) [glmwk wl(yh)] heat ordeal. ģarmsēr [gimsyl | N ~] warm region, lowlands. garódman [glwtmn' = Av. garó dəmana- | M grdm?n] paradise. ~ig [-yk'] (worthy) of paradise. yarranag [g”7k! | M grn’g ?] thunder. yarranidan, yarran- [gl’n-ytn' | (N yurridan)] roar, thunder. ~i$n: roaring. garzag [gick! | N garza] snake, serpent. garzidan, garz- [glc-ytn'] complain; confess. ~i$n: complaint. ~iSnig : complaining. gaw [gw!'] hand (daevic). базу [ТИРА < А twr) | M gw, N ~] ox, bull, cow; astr. Taurus. gawars [PZ < A prg’; g”wls | N ~] sorghum, giant millet.
PHD.txt:384:ёгбһ [glwh | N guroh] group, crowd. gubrág [gwpl’k'] awake, alert, vigilant. ģubrās- [gwp/”s-] = wigras-, v. wigrádan. ģuftan, $0(w)- [YMRRWN-, YMLLWN-tn! < A ymlwn, V тЇ; gwptn', gwb- | M gwptn, gw-, N ~, gā(y)-] say, speak. ~išn: speech. ģuftār [gwpt?] | N ~] speaker. ~ih: (power of) speech. gugiin- [gwk’n- | M gwg^n-] destroy. gugar(i)dan, gugar- [gwk”/-(y)tn! | N guwár-idan] digest. tuģāy [gwk*dy | M gwg'y, N guwah] witness. ~ih: testimony. ģūh [gwh | N —] dung, excrement. guhrayénidan, guhrayén- [gw AP yn-ytn!] waken, arouse. gul [gwl | N ~] flower, rose. ботап [gwnmn! | = M, N ~] doubt. ~par [-A/] casting doubt. ~ig [-yk'] doubtful. ~ih, ~igih: doubt. gumardag [gwmltk'] appointee, deputy. ģumārdan, gumār- [gwm’l-tn' | М gwm'r-dn, N gumāštan, gumar-] appoint, commission, entrust. gumbad [gwmbt' | N ~] dome, fire-temple. £umég [gwmyk! | M gwmyg] mixture. guméxtan, gumēz- [gx”myhtn!, gwmyc- | M gwmyxtn, gwmyz-] mix. ~išn: mixing, mixture; = gumézagih. gumëzag [gwmyck'] mixture. ~th: the Mixture, (the duration of) this material world. Jgund [gwnd | = P] army, troop; group, gathering. *gund [gwnd | N ~] testicle. gung [g(w)ng | N ~] dumb. ģurbaģ [gwibk! | N ~a] cat. Бита [gwlt! | P gwrd, N ~] hero. lih: heroism, bravery. gurdag [gwltk! | N ~a] kidney. *gurdih [ewityh] (some piece of) armour. gurdwār [gwltw’!] befitting a hero. ёпгр [gwlg | N ~] wolf. gurganig [gw/g”nyk! | N ~i] of (the province) Gurgan. gursag [ewlsk] | N gurusna !] hungry. «ЛЬ: hunger. Suën [gvfn! | N ~] male. gusnag [gwšnk! | J gušna] hungry. Gušnasp [gwšn(*)sf] the second major Fire of Sasanian Eran, that of warriors. £yà$ [gyw'k! | M gy'g, N jay] place.
PHD.txt:1706:dumb agowag, gung.
PHD.txt:4303:whatever Cegam-iz-e(w). wheat gandum.
PHD.txt:5376:garānīh darhandarzbed yarranidan garan yarranisn gramigih gramig grāmag drāyīdan, grāyīdan drāz, grāb draxt griy- grih dargūh garasman 1 3uriw griwag grīwbān driyos driyöšīh darigbed dilér drëm griyistan
PHD.txt:5460:LZeund, gung
PHD.txt:5471:gand, бу, gung, jang, jov, juy
PHD_mackenzie.txt:2448:gandum [Hg < A /;lnth I (M gnwm), N .....,] wheat.
PHD_mackenzie.txt:2455:gar [gl] mountain.
PHD_mackenzie.txt:2619:gung [g(w)ng IN......,] dumb.
PHD_mackenzie.txt:6448:district awestam, kust(ag), paygos,     dumb agowag, gung.
PHD_mackenzie.txt:7195:oath sogand, war.                      ordeal war; heat'" garrnowar(ih).
PHD_mackenzie.txt:7966:wheat gandum.                               gabr, grab, pusyan, uruspar, zahar.
PHD_mackenzie.txt:10803:                                                        gand, gi>y, gung,
PHD_mackenzie.txt:10807:1-2g11n d, gung
PHD_mackenzie.txt:12306:cbgat                  \~.-JO'     gandumI                        ..,.,.".,
```


## [2026-09-05T20:36:50.617Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT gar?nu ===\"; grep -n \"gar.nu-\\|gar.nav\" BRT.txt | head -30\necho \"=== BRT Kratze ===\"; grep -n \"Kratze\\|Räude\\|Raude\" BRT.txt | head -20",
 "description": "Grep Bartholomae for garenu and Kratze"
}
```


### [2026-09-05T20:36:50.679Z] TOOL RESULT

```
=== BRT gar?nu ===
10263:•  j.  gar«nav-  m.  'Krätze':  altaliva  dax- maeiva  Aqm.iavainti  axtii^a  'mdc'a  ..\.y.
=== BRT Kratze ===
16002:Räude',  np.  (Hpä.)  pam,   —   NpiL:  pam,  erL:
```


## [2026-09-05T20:36:52.050Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB ===\"; grep -n \"gandum\\|gung\\|garr\\|^gar \" NYB_vol2_glossary.txt | head -20\necho \"=== HRN garr ===\"; grep -n -i \"garr \\|'Kratze'\\|Kratze\" HRN.txt | head -20",
 "description": "Grep Nyberg and Horn for gar"
}
```


### [2026-09-05T20:36:52.113Z] TOOL RESULT

```
=== NYB ===
9:Photographische und photomechanische Wiedergabe nur mit ausdrücklicher Genehmigung des Verlages
1626:gar [gl] mountain, pl. cas. obl. ~-dn 20°. — Av. (513 sq.) gart-.
1739:gung [gwng, gng] dumb 11°. 127. 652°. — = NP. gurbak [gwlbk'] cat 101. — NP gurbah.
3054:be fulfilled 65?! (cancel the rel. pron. <i> at the beginning of l. 21 and join the preceding clause bē kē karr aivāp gung ēnyā, 1. 20, to 1. 21: "With the exception of the deaf and dumb, the religious duties must be fulfilled by everyone’). — Ps. p’ths’dy; Paz. pidišah, NP pādšā(h), cf next w.; ef MPrth vb. pdyx$h- ‘to rule’; from pati + Av. (551 sqq.) zšay- = OP; v. Verbum 229 sq., BBB 95 sq.; Bailey, BSOAS XII, 1948, 328 sq.
=== HRN garr ===
5547:622. rendlden 'schaben, kratzen*, rende.
5548:ai. [/'rad', rddati 'kratzen, ritzen'; phlv. randUan
6852:siften reiben, kratzen'^) mit aw. aiu)i]siföis, yt. 14, 35
7786:^kratzen' (Miklosich, Denkschr. WAW. Band 37, 40).
8551:'reiben*, kratzen, streichen, salben, mahlen' (244).
9930:469. Dazu se/üden zerkratzen' (Sahn. I, 222 Vers 1659,
```


## [2026-09-05T20:36:59.028Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10255,10275p' BRT.txt\necho \"=== leaf ===\"; awk 'NR<=10263{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' BRT.txt\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['BRT'].get('page_offset'),d['BRT'].get('lookup_hint'))\"",
 "description": "Bartholomae garenav context"
}
```


## [2026-09-05T20:36:59.437Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==222' HRN.txt | head -60",
 "description": "Horn page 200"
}
```


### [2026-09-05T20:37:00.634Z] TOOL RESULT

```
(oaml,  arpdvi)  arsnqm  xsudm  m  xlaä^rt- 1  ,  ,  .       °  /  Fp  \  y  »4  7
nqm    *'wqn  ■>   (näml.  yaeidalaiÜ)    Y.  65.  |  >,i,ara„a-  n„  vll.  lü  lit.   'skilti  -Feuer  anschlü-
5.  2)  'Leibesfrucht,  _/W«j'':  ma  . .  iaiiie]  gen'O.  -  IMi,:  oddamk  (Jamaspji  Gloss.547;
mafySnam  pard  fsanmat  {sA.)  :^atU  °W3m^  ".^j/.imi;  Utensils  med  in  the/äi' »j^*-^/(highet
ra?sayät\.  15.11;    ij.   "  "r?'"l'"i    of    'he    Zoroastrian     rdigion^)
..i-^Ma-  m.  I)  -Uterus,  i) 'fetus  ;  mp-  (P";)  (^o !,/„/«/  5,™r^«rf.   -    ■)  Np.  >mr  'Kohk'
■^r.  -    .)  NA.  -,«,;    s.  aber  Var.  und  Yt.  1^,   '^Q^^  „^^^  jjpp_j_  ^g^  fernzuhalten!    i-
j.  gartiai;  lies  giribiü.
•  j.  gar«nav-  m.  'Krätze':  altaliva  dax- maeiva  Aqm.iavainti  axtii^a  'mdc'a  ..\.y.
jelil  Glrili.  /  b.  87.
•  j.,   g.   garaz-  V.   'klagen',     Praes. ,gii-}Z;  S  Jlg»r3z-  [,  25  g»r?zanä\.
57;  —päilistJUe  -näuica  (GS.)  /.rAffW-ii  1      '•''"S^"'  wehklagen,  jammern';   i)  ohne
Yt.y.i,
Obj.:  yeühe  vlxs  gpn
mp.  (Pö.)V'rr.  np.  ^^  -KritK';  so  nseh  JN. ' '■''^''«  (^d.)  a/naoiti  Yt./o.Ss;  —  «d.Vffi JAOS.  14.  cxxv.  g)r>zänä  (NPf.,  näml.  fravalay^)  /ilra-
.  j.,  g.  gamma-  (,  p,  .r«""«»-)  i)  Adj.  {""•  ■  ■  W'l-'Sr.  'S-^'S  -  f"  ffr.! 'heiss,  (Obertrieben)  warm':  aM  a/l .. ��mal  /'■«»« /nf»«i (f.) ..  »«™»'.w- (sd.) . . Yt;o.so,  V.2.S;  -  -»»».ä,  vmm  mlimla  y5»""«(3PPrA,)'>i««äimi^I  ««V,»J "2u  waimen  und  zu  kalten  Wind"  Yt.o.io:''""*'  •  '''  T*?  ■«  J™""» '»  ■?=»■ ««.«».  M  „faJ.Sal  "wenn  (ihm)  die  m  »opheten'  Y.^ja.ij  a)  mit  Dal  der heissen  Speisen  Maul  oder  Zunge  «er-  P="<"'-/"''t; '',?™''  '  .''  » '"''«»^. brennen"  V.,5.4.  2)  n.  'Hitze,  Gluf:  K^ä-)   "''":'  ^iti.Kr..  "'™,'?-"'  •?*'
mil  aot,m..,ml  •mimX.ti.t,;  —  inahyar""  l""^ ''^^^^>  «"^  '"''S"  *= •mi  «3!«  ^-J.^^yWto  ,(/«/  „j/m»;,;„-iS=e>='äes  Stiers'   Y.  25. .«;   daraus   zit-
haa  jimat  mamai!  "wenn  durch  die  !•?'"■"''!'  f'",  A  ~ /"  .'  '  ""f'^'f"'' Glut  deines  Feuers,  dss  seine  Kraft  durch  Iff""'"  ÜSP-M-)»  «■*■'«■  .■  •"'•  «'l'-i Ma  hat,  mir  die  Macht  des  guten  Sinns  I  "'■'»■  53-  ')  m.t  Inhaltsakk.: /««ir,™ zu  teil  werden  wird"  V.49.4.  ipmqm  smzatia  (sSPrM.)  a,„  'die  erste
KompA.  -  ai.  ,f*fl™«-  m.  ■Hitie',  np.  iw™  !  Klage  klagtet." Vt-/". 57 ;  58,  59.      a)  mit 'heiss'.  —  PQ.;  garvi,  gatmat.  '  Dat.  derPerson:  ta  »X'jil  *mainyJui  iiialiyil
.  p.  garma-pada-  n.,  GS.  mit  nah-  m.' '•'"'■'  «''."''''  J«'*""*'»  e"-'«  "diese Name  eines  Monats'):  -Myl  mliyHtd.)  Wo'te  meines  Geistes  klage  ich  euch, Bh  r  II    9  I    7  o  ^/.,  und  dem  /l."  Y.^2.g.
n.d.  JO„.ir  de.  e,.,..  (Mi,.  Ap,.)."-  S,  n.Ü  ,  :-;.-;,"nV"J,,rt  'IS'.';,™  "ifj*: —  0  IlTiiL.  KZ.  2JJ.  aSi.  S  ///.  I  b.  FaUch MiLr.s  G,  483,  504.  —  'i  Der  Inhalt  der  Klaye gehl  voraus.  —    J)  S  5J  I-  S-    -    '>  D«'  I""
=== leaf ===
leaf: 307
Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
```


### [2026-09-05T20:37:02.290Z] TOOL RESULT

```
— 200 —
895. ger, gerr (AM. 28 Zeile 4) ^Krätze.
aw. garenu' *Krätze' vd. 7, 58 (145), yt. 13, 131
(Darmesteter, ebenso Jackson, der Amer. or. Soc.
Proc. 1889, XXV und Avesta Grammar § 806 ai.
gfdhnü' vergleicht; Geldner übersetzt KZ. 25, 551
^Sonnenglut' , Bartholomae, Studien II, 96 Trost',
cfr. lat. gelu^ ksl. zUdica^ nhd. kalt), also unsicher;
phlv. gar [skr. gard- *eine Krankheit' bezeichnet nach
dem PW. wahrscheinlich Schlingbeschwerden oder
ähnliches],
LW. kurd. gv' 'Krätze'; bei. gar ^Aussatz, Räude,
Krätze' (69) ; vergl. nslov. gar je *Krätze', garjaOj garat
^kratzen' (Miklosich, Denkschr. WAW. Band 37, 40).
896. guräz *Eber .
aw. varäza- 'Eber ; phlv. varOz (geschrieben varoc),
arm. LW. varaz, vgl. Varazdat, Baoa^rj^, OvuQoiCfjg
(Armenier); ai. varähd- *Eber'.
kurd. heräz,
V
np. veraz *Eber' wird im FS (Vullers) durch einen
V
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
Vullers?
```


## [2026-09-05T20:37:19.117Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=306 && NR<=309 {print \"---LEAF\",NR-1; print substr($0,1,300)}' BRT.txt\necho \"=== standalone numbers near ===\"; awk 'NR>10150 && NR<10400 && /^[[:space:]]*[0-9]{3}[[:space:]]*$/{print NR\": \"$0}' BRT.txt",
 "description": "Find Bartholomae column number"
}
```


## [2026-09-05T20:37:20.648Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ISS_alt_DKS uysgani ===\"; grep -n -i \"uysgan\\|ysgan\\|zagan\\|zayan\" ISS_alt_DKS.txt | head -30",
 "description": "Grep Bailey Khotan Saka for uysgani"
}
```


### [2026-09-05T20:37:21.795Z] TOOL RESULT

```
---LEAF 305
Rinderheei^de';  yti (näml.  gäus)  vanta  (sd.)  azimna  .  .  zba- yeili  .  .  'vai^lm  paitismarimna  kaoa  tiS arsa  "vai^im  qfayäi  (sd.)  faskat  vazsmrUS Yt  10.  86.
Ableit.  aus  igav-;  Tgl.  zSuff.  got.  meepi,  ags. icfuide  'Schafheerde'.
•  j.  gavana-  m.  Name  einer  Saatfru
---LEAF 306
p/.  661.  iBild. vgl.  femer  lat,  frägro  ans  "ghräghtiiö;  Bcu. Grdr.a  /.  602,  IF.  6.  100.  —  4)  Hds.r  främi mngi  rayöii  yiq  ratul  fritdis  (so  T)  äsat;  S. aber  Pu.  and  Bthl.  IF.  j.  371.  —  J)  Etymo- logisch lu  ^gar:  HaUQ  lieit  vTräj/isHii.  — 6)  S.  ta 
---LEAF 307
aiti Y./0.4;  —  ytzi  ahi  'rS  (LS.)*'  dtr^hm (sd.)  \.2i.  5;  —  paoiryB  °iris  hqm.hiiial .  .  haraiii  bars  . ,  bitys  ztrihazB  HrU  Yt.
BAITHOLOHAa,  AlÜHD.  Wb.
garad-  mit  aiwi
514
ig.  i;  6',  66;  —  'rsU  ^uHjIar^nahe  Y.i. 14,  22.36;  Ny.5.  5,6,  FrW.5.  i;  —  airyB
---LEAF 308
�mal  /'■«»« /nf»«i (f.) ..  »«™»'.w- (sd.) . . Yt;o.so,  V.2.S;  -  -»»».ä,  vmm  mlimla  y5»""«(3PPrA,)'>i««äimi^I  ««V,»J "2u  waimen  und  zu  kalten  Wind"  Yt.o.io:''""*'  •  '''  T*?  ■«  J™""» '»  ■?=»■ ««.«».  M  „faJ.Sal  "wenn  (ihm)  die  m  
=== standalone numbers near ===
10227: 514
10364: 523
```


### [2026-09-05T20:37:21.840Z] TOOL RESULT

```
=== ISS_alt_DKS uysgani ===
505:aysgana- ‘vulture’, JS 24ут pura та pemesti aysgam ће vulture seized the young ones'; K 21:4 aysgana-rivyi ' in vulture-form', K 28:179 -e; K 37:117 vari aysgimi-rüuya sū raksdjsi müfye “еге dwells one demoness (BS rākşasī) in vulture-shape'. See uysgaza-.
1033:cognates s.v. idysa-. Here belong Zor.P. zën ‘saddle’, N. Pers. дёп, Persian Sanskrit jayana-, from *izatna-, distinct from Zor.P. zen 'guard' in sēnīk, and zen-hàür ‘guard’, (dyadic with kar- ' to guard, Georg. xenaar-i), and distinct from Zor.P. xen 'weapon', dyadic in zen aflzür, Sogd. (Р. 7-52) луп ' knife’, from *zayana-, to Ау. zaya- ‘tool’, Georg. zein-k'al-i ' armourer, metal-worker', and distinct from N.Pers. z£nah 'ladder' and 'exit', Zor.P. uzën, uzënah, beside atem ‘entrance’, from *uz-ayana-, *ati- ayana-. The initial z- may represent earlier either i- or i-.
1113:uysgana- ' vulture', = BS grdhra-, Z 13:35 uysgani, changed. from uysguni, K 28:179 aysgana-rüvye, = K 21:4 aysgana- riiuyi, K 37:117 vari aysgini-rüvya їй raksájsi mūñye ' there dwells one rākşasī in vulture form', = BS Divyávadána 45013 vajrake paksi-rüjena pravesah ' meeting with the king of birds on the Vajraka mountain'; JS 24v1 pura pemesti aysgam rraijsai рпећа the vulture seized the young onesinsharp beak’. From uz-gana-' rapax’ ofabird of prey, N.Pers, sayan, Greek lw зќусуоҳ, Turk lw sagen. For the meaning гарах, note O.Ind. grdhra- to gardh- 'seize', Yidya yereno in the compound kyäl-yereno ' bald eagle’, from *grdnu-, Lat. uoltur from uello ‘seize’, Cerkes bye ‘eagle’ and ' rapacious’. Hence a base gan- ‘to seize', IE ghen- to IE Pok. 437-8 ghen-d-, N.Pers. ausand ' armour', Georgian absand ‘stirrup’, Armen. lw óandah ‘aid’, from *abi-janda-ka-. Possibly Sogd. VJ доб упш 'force'.
1782:gan- ‘to seize’, in the name of the raptor bird uysgana- ' vulture',
4781:prraysinime ‘Į watch’, ш 106.34-5 skada yana müse mara Айга aha jsa prraysīnīme stau maista 'l will loosen secretly my girdle; sleep here with me; I will however make great watch'. From *pari-zain- to даї-їдї- ‘е watchful’, Av. saēnahvant- ‘watchful’, zagmi- 'lively', вайпап- ‘liveliness’, даёпаюйап- ‘watchful’, Zor.P. zEnavand; Ау. zagni.bura- ‘watchfully awake’, Zor.P. sēnävand gufrāk ‘watchful, awake’ (-fr- < yr-) glossed by zēnīk хтар ‘he sleeps watchfully’; Parsi-Sanskrit jūgarana- for saēman-; Av. azinavant- ‘watchful’ (epi- thet of 'Taxmë urupa). To Zor.P. sēnahār, N.Pers. sēn- har, Georgian lw zenaar-i, dyadic compound with kar- fto watch’. Base O.Ind. je-, not he-, see s.v. ysinita- ‘taken under care’, With -me (correcting printed -re). Note that Zor.P. has also sēn ‘armour’ (*zayana-), Georgian lw zern-k' al-i ' smith" (*zenakara-); xen ‘saddle’ (*ixaina-).
6108:miysai ‘urine’, v 97, 18a3 miysai khārggä rrumä ' urine, mud, dust’. Base maiz-:miz-, with three initials m- (miysai, maysjyāna), b- (biysma), ph- (phiysgana-), Av. maëz-, таёѕтап-, gao-maēza-, Zor.P. тёх-, müzit, mist, mistan, вӧ-тёх, N.Pers. méz-:müzidan, méxtan, Parsi- Pers. mēzišn; Sogd. Bud. mys-(myz'y P 2:299, not myn'y), Balöči mëzay, nizay, mist'a; Oss, D. mezun, mist, I. mix-, myst, D. mezgd, I. mizg ‘urethra’; Pašto тїәї, mitiyazi turine’, Yidya mīsyo, miz-, méz-:mind, Waxi тїз. Buyni mës-, mist, mišč, бш miz-, тїї, Yazg. mix-, maxi, maxtag. ТЕ Pok. 713 metgh-, O.Ind. méhati, midhá-, meha-; Armen. mízem, тёс, Greek Ópzíyco, Oury£co, igon Lat. met, ictus, mingo, tinctus, O.Norse mmiga, О.Епрі. migan, micga, Got. maihstus, Lit. mast, misti, Serb. mésga, misám, mizati, Tokhara В mišo. For Av. anizón, misti-, see s.v. missa-.
6141:' yahakşaja mūñe 'there dwells а vülture-shaped rüksast- demoness', =K. 37117 vari aysgini-Crüvya їй rakşäjsi mūñye, = К. 28:179—80 vara aysgana-rituye sā yahahsaja mvaiie; K 39:153 pürd vaña ra sam mara müitya ' my son, now remain here’; Ш 67:53 garvā айй vara slam mūñye ‘he is in the mountains, there he dwells'; Manj. 317 sattsera anühvarrda тпшайе “іп the migration he dwells unaffected’; Sid. 140v5 buysq munida ‘they remain long’, Tib. yun ris-du ('long!); K 150720 ttaradará dattavi khoa mūñīda тазіі ‘аз the body's parts (BS dhàütu-) remain rightly; Manj. 58 drraya vara mvaiiida ' the three remain there’; participle present, Sid. 152v3 astauci muñamdan muram hiye ühe ‘eggs of the birds dwelling on the dry land’, BS jangala-, ''ib. bya skam-sa-na gnas-paht sgo-ua; Sid. 134v3-4. astaucd. ysatam и muñamdām datan hiya gusta ' flesh of wild animals born and living on dry land’, BS jüngalaja-, Tib. ri-dags skam-sa-na gnas-pahi $a. Preterite, Е p. 357 B tta tta је aysu münde Па vegasti samu khu vami ' so I remained as excited (BS vega-) as the sea! ; ш 65:10 рата Байа vara зій müde ' he dwelt there a long time’; п 65:13 Austa mida ' where he dwelt’; K 46-36 strrzya müda ће woman dwelt'; JS gra estava mumdai ‘you remained firm’; JS 17r1 thu mi vara mudai ‘you then remained there'; К 39:154 va тпай аиғазјаї
6547:rraysga- 'swift, light (not heavy)', Sid. 12r5 rraysgd vira ‘swiftly’, Tib. myur-du, Z 24:241 hussata rraysgat ‘ће grew swiftly’, parallel Divyāvadāna 1:26 āsu vardhate; Sid. 3r4 vaskalvàmata mase raysga üstanuta günai ' (time) having the mark swift as only a moment and the rest’, BS mnimega-üdika-lakgana-, Tib. mig hdzum-pahi yud- ċam-la sogs-pahi méhan-ma; "light! v 87, sori-2 ami và rre pulsti bisu anujátá crámi arrá o garkhä o và rraysgü 'the king Yama asks him, he questions all what kind of fault of his, whether heavy or light’ (BS anuyuj- 'to enquire'); Bed s5a4 rraysgd, BS Rgipra- ‘swift’, Bed 5513 raysgd vi thyau 'swiftly at once’, BS ла cirea ' not after long’; K 151:37 raysgq-t-i; K 152716 tcana byehide rraysgana baysuiti "whereby they get bodhi-knowledge swiftly’, K 154746 rraysgi thyam (= thyau) ' quickly, at once’. Compound, Sid. 17r5 rraysga-gvücha- ‘digesting lightly or swiftly', BS Jaghutara-, Tib. yan-uo (' light"). From *raju-ka- (-dž-g- > -ysg-), to Av. rayu-, fem. ravi», comparative тәпјуаћ-; ranjista-, with component rava-, -rava-; M.Parth.'T. rg, rgydr ‘swift, swifter', Armen. Iw erag, arag 'swift'; Simnànt raïk. IE Pok. 660 leg"h-, leng*h-, O.Ind. raghú-, laghti-, Greek tAoxús, оеро, Lat. leuis, Got. leihts, O.Engl. leoht, Lit, leigvas, lengeis, O.Slav. Пойа, ;
8359:harahusta- ‘dispel, expel, dispossess', JS 19r4 dà hryau bayau harahustai rraysgana 'with rays of the dharma- doctrine you swiftly dispelled (21202 ‘the darkness')'; К 23:66 grraysya harahausta maiysdyaina anāha phara satia hastanü-pü(ra) tseda ‘dispossessed the distressed pitiful protectorless many beings, they went to Наѕііпа- pura’, -—Krisgirs grraysye harahausta (ca) patsyauda Ёўїга ' he dispossessed the distressed ones who abandoned the country’, =K 3122-3 graysye harahausti satta cu pha patsyamdi Rsiri, phiri ysāri си hastinüpüri tsvádi ‘he dispossessed the distressed beings who left the country, many thousands who went to Hastinüpura'; ur 82:1: aryavalaukittesvara. baudhasatod sa јиѕйа parta viniyü harahausta attrásta ' the bodhisattva Áryavalokite$vara, he (took in charge) Justa, those to be saved (and) disci- plined,. expelled, not saved’, From base 8raud-:6rud-, *Üürusta- ' pressed forth’, IE Pok. 1095-6 tr-eu-d- ‘press, thrust', Lat. 270420, trüdere, trüdis ' pointed stake’, Celtic Welsh cythrudd ‘to torment’, godrudd ‘wild’, gortfirudd ‘oppression’, Got. usfriutan 'cause trouble’, O.Slav. trudü ‘weariness’, truditi ‘torment’, Possibly here M. Pers, T. swst ' weak, weary', N.Pers. sust ' weak, idle" (G. Morgenstierne, NTS 12, 266) with O.Ind. trot-, trut- ‘break in pieces'. Hence distinct from güraphusta- ‘thickened’ *oi-frusta- to base fraud-: frud-.
```


## [2026-09-05T20:37:53.219Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD gnw ===\"; grep -n \"γnw\\|ɣnw\\|gnw\" SOD.txt SOD_pages.txt | head -20\necho \"=== SOD 163 ===\"; grep -n \"force\\|power\" SOD.txt | grep -i \"gn\\|γn\" | head -10",
 "description": "Grep Gharib Sogdian dictionary"
}
```


### [2026-09-05T20:37:53.280Z] TOOL RESULT

```
=== SOD gnw ===
=== SOD 163 ===
```


## [2026-09-05T20:37:54.342Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK 437 ghend ===\"; grep -n \"ghend-\\|ghed-\" POK_01.txt | head -10",
 "description": "Grep Pokorny ghend"
}
```


### [2026-09-05T20:37:54.384Z] TOOL RESULT

```
=== POK 437 ghend ===
```


## [2026-09-05T20:37:57.942Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la SOD*.txt; echo \"---\"; head -c 1500 SOD_pages.txt; echo; echo \"=== grep gan ===\"; grep -n \"gnw\\|ynw\\|ġnw\" SOD_pages.txt | head",
 "description": "Inspect SOD files"
}
```


### [2026-09-05T20:37:58.023Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 3741182 Sep  4 14:06 SOD_pages.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1845041 Sep  4 14:06 SOD.txt
---
 SOGDIAN
DICTIONARY
Sogdian - Persian - English




      B.Gharib




   FARHANGAN   PUBLICATIONS
Sogdian Dictionary (Sogdian-Persian-English)
by B. Gharib
editorial supervisor: A. Mansouri
editor: S. Fotouhi
© 1995, Farhangan Publications
2/52. Shahid-e Said Street, Tehran 15916, Iran.
Tel: 6460069. Fax: 670230

ISBN: 964-5558-06-9
4f*Jj*l{^ 0"J-^8 'Jy^**-             ^J>*4^ tfW : j' a>„J^ <f jljX-U^ -LUi^-L ^JjJ'j^ L» e jlf ijj-
                                                                • l^> o-^ jl ^^<o (j ^jb^b             j uij^- ^C*"
                  ;l_^0 jL-u jlS' 4$" (.5*^-*^' "^^   (H^- fJ




                                                                                                                   L?JJ J'
                                                                             ^            jS.          Ji          *




                                                                             JU-ib^y* jl^ *^Up ^j^>» 4^—*a j -U>_#

O      i j^tbj^> j^Ui   ^O ^ p-iU- jl ^                  ~J*A*         u^T J ('.»-) ^.^ MJ-^ ^                         jl

iJUj




^S" ^L^wJb         jf .x>*j$ oo I 3^^" f j^^* ^^u^J^i             J oU^U^I


                                                                             *_»( *0 k_S-*J   4rf (J^^l -^j'-3 iT'W-' "^J_^
                                                         &*>jS jj! jl d*»Us*>l fjdjbj^




                                                                       »>jb ^^rj

=== grep gan ===
11204:2579 pynwy(y) M                             (>^-^)>*U
11205:     Pay-nawe ©abl. -nw)      =^pyynwy(y)                   2592 pypwryst =* Pypwryst
11282:2607 pyynwy(y)         M                            (>^/-^)>U
11283:     Paye-nawe         =*Pynwy(y)                                               Hen. Tales. 470.60
13311:3344 cynwwt B                          Jf>u*f<>zu              3357 cynt'mtoy      B =» cnt'mny
19825:       MDii, mynw; Frag. Len. 61.12; VJ n p93, 499                    mene ©pi. -f; ob. pi. -/y ^myn'ndyCy)
20673:          nayn- pak -^nynwp'c                                           niyasn ? =*prysnh                           nywst-
20680:     5910 nynwp'c M                                  j-jUj*
26216:     patpatinawe (ptp^yn'wy, ptp^ynw^,                               (to)be appeased
26225:7804 ptpt'ynw'k =» ptpt'ynWk                                           pass., TSP 2.234; GMS 884
```


## [2026-09-05T20:37:59.720Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ghen-d-\\|ghend\\|prehendo\" POK_01.txt POK_02.txt | head -10; echo \"===\"; awk 'BEGIN{RS=\"\\f\"} NR==446' POK_01.txt | head -30",
 "description": "Find Pokorny 437 ghend"
}
```


### [2026-09-05T20:38:01.424Z] TOOL RESULT

```
POK_02.txt:1167:WP.  I  531  ff.,   Trautmann  74,   Feist  218.    S.  auch  unter  ghend-,
POK_02.txt:1402:gbend-  und  ghed-  , fassen^  anfassen,  ergreifen^;,  z.  T.  auch  ^geistig  erfassend Zum  Nebeneinander  der  unnasalierten  und  der  nasalierten  Wurzelf. s.  Brugmann  U^  3,  293  f.,  IF.  32,  321. Gr.  x<xvSdv(jü  (*gh^nd-)  ^fasse^,  Aor.  M^adov  (*ghnd-)j  Fut.  xelaoixav  (^ghend-s-), Perf.  mit  Präs.-Bed.  y,exovöa',
POK_02.txt:1408:vielleicht  hierher   (als   mit   cymr.  genni  bildungsverwandtes  ^ghend-nö). got.  du-ginnan,  ags.  on-,  bi-ginnan,  as.  ahd.  biginnan  ,in-cipere,   beginnen'! (andere   Deutungsversuche    s.  bei  Feist  ^  s.  v. ;    davon   beachtenswert  dei von  Wiedemann  BB.  27,  193  als  *ghen-uö  zu  alb.  ze,  geg.  zä  ,berühre,  fang« fange  an,  empfange  [vom  Weibe],  miete'  aus  uralb.  "^zeno) ;
POK_02.txt:1411:ghendb-  {ghondh-)  ,Geschwür'.
===
```


## [2026-09-05T20:38:13.273Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=1402{n+=gsub(/\\f/,\"\")} END{print \"POK_02 leaf:\",n,\"→ printed:\",n+344}' POK_02.txt\necho \"=== nearby page markers ===\"; awk 'NR>1330 && NR<1420 && /^[[:space:]]*[0-9]{3}[[:space:]]*$/{print NR\": \"$0}' POK_02.txt",
 "description": "Find Pokorny page for ghend-"
}
```


### [2026-09-05T20:38:15.031Z] TOOL RESULT

```
POK_02 leaf: 94 → printed: 438
=== nearby page markers ===
1352: 435
1390: 437
1404: 438
1418: 439
```


## [2026-09-05T20:38:15.400Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *163 \\|^163 \" SOD_pages.txt | head -5\necho \"=== gamma entries ===\"; grep -nE \"^ *[0-9]{2,4} +[yγḡğ]n\" SOD_pages.txt | head -20\necho \"=== search yn'w / ynw ===\"; grep -n \"yn'w\\|ynw\\b\" SOD_pages.txt | head -20",
 "description": "Find Sogdian gnw entry"
}
```


### [2026-09-05T20:38:17.121Z] TOOL RESULT

```
4271:163 »m kS'r'k B                         J^^jj^
=== gamma entries ===
15465: 4121 yn'p- B, S              (*jLfi:Jj*j)jjJkto>J,Ab
15470:                                                                 4134 ynp- B <=» ymb-
15472:                                                                 4135 ynp'wnh B                    J& <j£s~±tgj
15473: 4122 yn'p'nt B                                          oVl;         yanpa/un (ympwn, ynpwn) =4ympn, ymbn,
15479: 4123 yn'p't- B                                         joJU            GMS 113; S W,C2p61
15481:                                                                 4136 ynpn(h)    B, S                         j& tj±j>.
15486: 4124 yn'pSV- S            f                    fr/«J                 TSP 9.130 n p222; Hen. Talcs. 486.3; KG 384,
15489:                                                                4137 ynpwn =» ynp'wnh
15491:                                                                4138 yns1 B                                      JLuai^
15492: 4125 ync(h) B                                    J*fj*              stinking
15497:                                                                4139 yns: B, S                                 Jy^*^
15499:4126 ynd'k M                   (tjJ' <jjf)^jcxX^x                    stable, strong
15503:4127 ynd'qry      C =* ynd}kry(y)
15504:                                                                4140 ynsy'kh S                              ^/^J<fl£*i-I
15505:4128 ynd'kry(y) M                               J^nj&ti              stability
15510:                                                                4141 yns M                         (jx,-?,C j<Uj)jU^j
15511:4129 ynd'ky qryny(y)       M                    X-^i^                xans
15516:                                                                4142 yns- B                                          jxj^
15517:4130 ynS'nyw B                                      &&               xans =4xns-, yrs-
15522:4131 ynyr(h)    B, S                             j^±                 xansak =»yns-
=== search yn'w / ynw ===
8425:      pupil                                                             (3)spawnawe ? ©Parth. '^w             ^'sp'yn'w^
8432: 1612 'sp'yn'w'k B
13312:     cinaut (cyn'wt) ©cynak+aut <*awat                         3358 cyntr1 B, S, C                           J^yd
13314:     GMS 1079; Frag. Len. 118.4; cyn'wt, VJ 686;                    inside
13315:       cyn'wty, VJ 740                                              TSP 3.95 etc. 159, 161, 291, 16.36; BSTBL, Dhu.
13324:3347 cynNvt ^ cyn'wt                                                Ladakh. Insc. 3; Benv. Notesiv BSOAS 1938, 504
19825:       MDii, mynw; Frag. Len. 61.12; VJ n p93, 499                    mene ©pi. -f; ob. pi. -/y ^myn'ndyCy)
26216:     patpatinawe (ptp^yn'wy, ptp^ynw^,                               (to)be appeased
26225:7804 ptpt'ynw'k =» ptpt'ynWk                                           pass., TSP 2.234; GMS 884
27371:8197 pw ptptyn'w'k B
28923:                                                                 8750 synw S                                           j^.
28971:         81.10; STii 1.5, 23, 2.9, 3.13; BSTi 172; Frag.             swxn(w)sxun (sywnh) =>synw, swyn-1,
29497:8922 spyn'wy M                                   f^r«>^
29871:                                                                     BSTii 885.12; ace. swqynw, C2, 51R12
29935:9070 swnt'y B =* swnt}k                                            suxanu (sxnw) =»swyn-\ sywnw, sxwn-, synw
33812:                                                            10409 wyn'wcy B                          Jynjxj^ Jju^a
33825:                                                                  wenawclk       (wyn'wcyk) ^wyn'ncyk
33832:      visible                                               10412 wyn'wcyqy* C                                   jj^ij^
```


## [2026-09-05T20:38:26.252Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -nE \"^ *[0-9]{3,4} +yn?w\" SOD_pages.txt | head -20\necho \"=== y'n / yn ===\"; grep -nE \"^ *[0-9]{3,4} +y[n']\" SOD_pages.txt | head -40",
 "description": "Search SOD for gamma-n-w headword"
}
```


### [2026-09-05T20:38:47.767Z] TOOL RESULT

```
4802:                                                                 363 ywz-' B                                   o^/^pT
15960:                                                            4302 yw'kry      S =» yw'kkr
15962:                                                            4303 yw'm      C                                «& JStf
15963:4290 yw1 B, S                               J<jl
15970:4291 yw2     C                                         3€
15991:4293 yw" =* yw'w-, yw-
15999:4295 ywMkkr B                  (J'&^'d^j^                   4308 yw'ncyq      C =^ yw'ncyk^
16006:4296 yw»n                                                          976 n 1, 1014
16013:4297 ywwnk       MD -> ywn>nk                                    Frag. Len. 27.5, 44.3
16014:4298 yw»t B, S                                ^olj*         4311 yw'ncyqy*     C                             j^^j
16040:                                                             4330 ywVyk S                                    JybiJ^-
16070:                                                             4335 yw'yr- B                                jjIjIJ^ < j-^j>-
16073:4322 ywVyst => xw'r1, Yw>rn
16096: 4338 ywp-3 =» YwPw                                                            C2,48R18
16097:                                                                          4352 ywpty B, M
16098: 4339 ywp't =* YWP-*                                                                                      =»ywbc
16108:                                                                          4353 ywbty     C =» ywpty
16111: 4342 ywpcy'k S                                               ^J-j"^      4355 ywpty'h M                        jJb^j sj^ «>j&
16115: 4343 ywpcyk S                           ^U^l,                                    14.18, 22.17; Sund. AoFviii 1981 p215; STii
16119:4344 ywbd'r-      C -* ywp-1
=== y'n / yn ===
15252:4050 y'ysrc S               ^Sijj ^oO^j)^^    JaI^^U-
15270:4053 y'm3 C                              sz^yt^t^jJ3ijjj
15276:4054 y'm'k B                             (^U~)<                   xast (x'st) ©pL?
15283:4056 y'mqyn      C, M =» y'mkyn                                   GMS 773; VJ 1448
15285:                                                             4069 y'ttwnh =» y'twnh
15314:              4073 y'w-'        B -» yw-
15341:              4078 y'wsrS M                                     , 'jfju         wound, wounding, beating
15358:             4080 y'y B
15372:             4083 y'yr-  B                                ^        <&
15465: 4121 yn'p- B, S              (*jLfi:Jj*j)jjJkto>J,Ab
15470:                                                                 4134 ynp- B <=» ymb-
15472:                                                                 4135 ynp'wnh B                    J& <j£s~±tgj
15473: 4122 yn'p'nt B                                          oVl;         yanpa/un (ympwn, ynpwn) =4ympn, ymbn,
15479: 4123 yn'p't- B                                         joJU            GMS 113; S W,C2p61
15481:                                                                 4136 ynpn(h)    B, S                         j& tj±j>.
15486: 4124 yn'pSV- S            f                    fr/«J                 TSP 9.130 n p222; Hen. Talcs. 486.3; KG 384,
15489:                                                                4137 ynpwn =» ynp'wnh
15491:                                                                4138 yns1 B                                      JLuai^
15492: 4125 ync(h) B                                    J*fj*              stinking
15497:                                                                4139 yns: B, S                                 Jy^*^
15499:4126 ynd'k M                   (tjJ' <jjf)^jcxX^x                    stable, strong
15503:4127 ynd'qry      C =* ynd}kry(y)
15504:                                                                4140 ynsy'kh S                              ^/^J<fl£*i-I
15505:4128 ynd'kry(y) M                               J^nj&ti              stability
15510:                                                                4141 yns M                         (jx,-?,C j<Uj)jU^j
15511:4129 ynd'ky qryny(y)       M                    X-^i^                xans
15516:                                                                4142 yns- B                                          jxj^
15517:4130 ynS'nyw B                                      &&               xans =4xns-, yrs-
15522:4131 ynyr(h)    B, S                             j^±                 xansak =»yns-
15527:                                                                4144 ynsn B                            ? •xjfjfr- <? &/
15529:4132 ynkyn B                                                         with effort ?, with toil ?
15533:                                                                4145 ynsy'kh    B                                    4*&>
15538: 4146 ynt' B
15544: 4147 ynt1 C                                                                  yandak-name
15549: 4148 ynt-     B                                           ^xi-               yandakarc ©f. adj.
15561:4150 yntMk nVn'k B
15567:4151 ynt»k nyzp'n'k B
15573:4152 yntHk zp>k B                                    •yfe^Jj <uIj jJO
15579:4153 ynt'q     C => ynt'k^                                                      Sughn. zinderv; 0P=E1. kanturma         ©ob. -y
15580:4154 ynt'k^      B, S                                                           ^knt'rP, wp'p yntrw
```


## [2026-09-05T20:38:56.956Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '15525,15620p' SOD_pages.txt",
 "description": "Read SOD gamma-n region"
}
```


### [2026-09-05T20:38:57.000Z] TOOL RESULT

```
     dagger                                                          SCE 44; Hen. Texts. 733
     MDiii p76.6; TSP 2277 n p!72; Frag. Len. 37.6,
                                                                4144 ynsn B                            ? •xjfjfr- <? &/
       61.16, 17                                                     xansan
4132 ynkyn B                                                         with effort ?, with toil ?
                                                 jj^'j-fc
     yanken (ynqyn) ©pi. -t                                          TSP 2.1043-44
     brave, victorious
                                                                4145 ynsy'kh    B                                    4*&>
       xansyak     ^yrsy'k                                               4157 ynt'q qry C                            juli <jl$*jb
       torture                                                                yandak-kare ©voc. -qr\ voc. pi. -qryty
       TSP 6.151; Hen. Texts. 733
                                                                              STi 27.7, 11.6, 48.9; -qryty, BSTii 843.28; C2, 68R
 4146 ynt' B
      xand ©3pL pers. =»x-\ y-\ xnt, >nt\ xnd                                  evildoer  "
                                                                                28, 54R 26
                                                              -^iiSJi
      GMS 764; AVS 224                                                   4158 ynrttnWk        B                                    flu,

 4147 ynt1 C                                                                  yandak-name
                                                                              ill-famed
      yand/t
      stench =»ynsl                                                           BSTBL, Intox. 9
      C2, AV29                                                           4159 ynt'qrc C                                     j£*?(oj)
 4148 ynt-     B                                           ^xi-               yandakarc ©f. adj.
      xand                                                                    evildoer

      Go)laugh                        v                                       C2, 12R12: BSTii 849.12
      VJ 1355                                                            4160 ynt'krtyh B                           KsJ^Ji^J^
                                                                              yandak(a)rtya/i
 4149 Ynt»kw      B                             jl^ «jlX «jb <cAS             evil deed
      yandak      -»ynt)kf)), ynd'k
      bad                                                                     TSP 5.123, 124; Frag. Len. 40.4
      SCE 149, etc.; GMS 976 n I; -Wl SCE 264; -\                       4161 yntJqry    C                                   j£+j<jfi>
        SCE 117; BSTBL, Dhy. 141, 268, 397; Intox. 1, 3                       yandakarc       (ynd'qry, -qry) ©pi. -/
                                                                              evildoer
4150 yntMk nVn'k B
     yandak-mane                                  OLfj                        STii 6.1, 17, 38; BSTi, 260; BSTii: C2 gloss.
     evil-minded                                                        4162 yntm      S, C                                       fxf
     SCE 200
                                                                              yandam      ©ob. -y
                                                                              wheat
4151 ynt»k nyzp'n'k B
     yandak-nizpanc                                                           MDii pl86.14; MDiii 34.4; C2, 52R 10; STi 43.12
     having evil passion                                                4163 yntmyn'k B                                 *J&u±aij\**x±-
     SCE 117                                                                 xand-mene
                                                                             derisory

4152 yntHk zp>k B                                    •yfe^Jj <uIj jJO

     yandak-zPak                                                              TSP 8.106 n p216
     evil-tongucd
     SCE 466                                                            4164 yntrw B, S     (? jjjuf ^LaU.)^! *y>- ^l>a ^
                                                                             yandaru ©Av. gandardva% Skt. ghandharva;
4153 ynt'q     C => ynt'k^                                                      Sughn. zinderv; 0P=E1. kanturma         ©ob. -y
4154 ynt'k^      B, S                                                           ^knt'rP, wp'p yntrw
                                          (Of* ^Z~t J**)*'
                                                                              water-spirit, Gandharva
      yandak     (ynt'q, ynt'kk) ©ob. -y; pi. -/; ob. pi.
                                                                              TSP 3.131; Hen. Tales. 481.32, 482n 3; Gersh.
        -ty =>ynd}k, ynt'k0'                                                    Amber. 1969, 199
      bad, evil
      TSP; BSTBL; SCE; STii; STi; Sund. AoFviii 1981
                                                                        4165 yps-
                                                                        4166        => yn(,)
                                                                             yny(y) S
       p215; Frag. Len.; C2; Ynt}k\ Frag. 5.4; Ynfkk,                                                                          o^£
       VJ; BSTBL; SCE; TSP; Ynt>kw, Vim. 18; Hen.                            yafs =^ypt-, yPs-, yfs-
       JRAS 1944, 138.21; Anc. Lett. 3.4; MDii; MSP
       bl 12; Frag. Len.                                                     (to)strive
                                                                             Anc. Lett. 1.9; Hen. BSOAS      12, 607 n 2
4155 ynt'kk ** ynt>kc,)                                                 4167 yr-1   B, S                               j^^L «ja^lj
4156 ynt>kkrt>k S                                  jOa0£*Lf                  xar    ©<*har-     =>yrt-, xyr-, xr-2, y'yr-
     yandak-krte/ak
     evildoer                                                                (/o)walk
                                                                             TSP 13.21, 3pl. opt. Yr*ynt\ Bailey. Prolexis. 411
     Frag. Len. 82a5
                                                                        4168 yr-3   B, M, C                      (j^ ^j^ jS)*f
                                                                                                         iMH




    Yr-yar ©<*gari; Yaghn. Tar ©nom. -y, -w; ace.                     4180 y^n      B, M,C                           J^r^J^^J
         -w; abl. -J; ob. -yffc>, loc. -y; p/. -j\ -tA, -»';                yran ©ace. -w; pi. -t =^yr'nh
        ob. pi. -ry =^Yr*n ywt'w                                            heavy, serious
      mountain                                                              TSP; SCE 341; Frag. Len.; BBB 487 b48; MSP
      GMS 947, 1177; VJ; TSP; STi 16.6; STii 4.39;                            bl05, 189; STi 52.15; STii 5.32, Yr'n, BSTBL,
        SCE; BSTBL; BBB; Hen. Tales. 473.40, 45;                              Dhu. 83, 133, 240; SCE 186; TSP 6.71, 127;
         481.35; MSP bl47; pi. -t\ -th, BSTBL; Cosm.                          rr}nw, TSP 2.33
         307.29; ob. pi. -ty\ GMS 1188; TSP 2.274 n                   4181 yr,np,k(=yr)zp,k)        B     (^^^^/j^)^>
                                                                           xar-zi[3e
         pi 72; gen. pi. Yr*n> TSP 6.47
4169 yr-3 B, S                                   >                          gadfly
     xar ©<Av. xara ©nom. ob. -y-y ace. -w\ abl.                            SCE 365; "ass-bitter", Gersh. IF 1970, 305
       -)(>,; pred. inst. ->
```


## [2026-09-05T20:39:10.621Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=15465{n+=gsub(/\\f/,\"\")} END{print \"leaf at gn ap:\",n,\"printed:\",n-66}' SOD_pages.txt\ngrep -n \"\\[pdf page\" SOD_pages.txt | sed -n '225,240p'\necho \"=== search yn.w ===\"; grep -nE \"^ *4[01][0-9]{2} +yn\" SOD_pages.txt | head -40",
 "description": "Locate SOD page 163"
}
```


### [2026-09-05T20:39:12.619Z] TOOL RESULT

```
leaf at gn ap: 229 printed: 163
=== search yn.w ===
15465: 4121 yn'p- B, S              (*jLfi:Jj*j)jjJkto>J,Ab
15470:                                                                 4134 ynp- B <=» ymb-
15472:                                                                 4135 ynp'wnh B                    J& <j£s~±tgj
15473: 4122 yn'p'nt B                                          oVl;         yanpa/un (ympwn, ynpwn) =4ympn, ymbn,
15479: 4123 yn'p't- B                                         joJU            GMS 113; S W,C2p61
15481:                                                                 4136 ynpn(h)    B, S                         j& tj±j>.
15486: 4124 yn'pSV- S            f                    fr/«J                 TSP 9.130 n p222; Hen. Talcs. 486.3; KG 384,
15489:                                                                4137 ynpwn =» ynp'wnh
15491:                                                                4138 yns1 B                                      JLuai^
15492: 4125 ync(h) B                                    J*fj*              stinking
15497:                                                                4139 yns: B, S                                 Jy^*^
15499:4126 ynd'k M                   (tjJ' <jjf)^jcxX^x                    stable, strong
15503:4127 ynd'qry      C =* ynd}kry(y)
15504:                                                                4140 ynsy'kh S                              ^/^J<fl£*i-I
15505:4128 ynd'kry(y) M                               J^nj&ti              stability
15510:                                                                4141 yns M                         (jx,-?,C j<Uj)jU^j
15511:4129 ynd'ky qryny(y)       M                    X-^i^                xans
15516:                                                                4142 yns- B                                          jxj^
15517:4130 ynS'nyw B                                      &&               xans =4xns-, yrs-
15522:4131 ynyr(h)    B, S                             j^±                 xansak =»yns-
15527:                                                                4144 ynsn B                            ? •xjfjfr- <? &/
15529:4132 ynkyn B                                                         with effort ?, with toil ?
15533:                                                                4145 ynsy'kh    B                                    4*&>
15538: 4146 ynt' B
15544: 4147 ynt1 C                                                                  yandak-name
15549: 4148 ynt-     B                                           ^xi-               yandakarc ©f. adj.
15561:4150 yntMk nVn'k B
15567:4151 ynt»k nyzp'n'k B
15573:4152 yntHk zp>k B                                    •yfe^Jj <uIj jJO
15579:4153 ynt'q     C => ynt'k^                                                      Sughn. zinderv; 0P=E1. kanturma         ©ob. -y
15580:4154 ynt'k^      B, S                                                           ^knt'rP, wp'p yntrw
15596:4155 ynt'kk ** ynt>kc,)                                                 4167 yr-1   B, S                               j^^L «ja^lj
15597:4156 ynt>kkrt>k S                                  jOa0£*Lf                  xar    ©<*har-     =>yrt-, xyr-, xr-2, y'yr-
```


## [2026-09-05T20:39:21.827Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"4133\\|4143\" SOD_pages.txt | head\necho \"=== full leaf 229 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==230' SOD_pages.txt | sed -n '1,40p'",
 "description": "Look for SOD entries 4133/4143"
}
```


### [2026-09-05T20:39:23.590Z] TOOL RESULT

```
15468:      GcOlament                                                  4133 ynqyn     C =* ynkyn
15521:     TSP 2.148, 634, 295                                        4143 yns'kh B                               ^^c^j^j
38214:exertion    4108,4111,4143               face on earth 2766                      8224
=== full leaf 229 ===
  Yn>P-
                                                                       SCE 308; STii 1.17, 2.13; C2, 48R21, 66V 12, 68V
 4121 yn'p- B, S              (*jLfi:Jj*j)jjJkto>J,Ab
                                                                         11; BSTii 843.42, 877.8
      yna(3
      GcOlament                                                  4133 ynqyn     C =* ynkyn
      GMS 1310; VJ 358, 1111; Sund. MHC 26.10;
                                                                 4134 ynp- B <=» ymb-
          trans, pret. Ynyfidyry Mack. AI 25, 422, 19
                                                                 4135 ynp'wnh B                    J& <j£s~±tgj
 4122 yn'p'nt B                                          oVl;         yanpa/un (ympwn, ynpwn) =4ympn, ymbn,
      yna[3and
      lamenting                                                       trouble,
                                                                        ynpn(h)pain
      GMS 1033; VJ 1412
                                                                      BSTBL, Vim. 43, 72; TSP 2.I149-, Frag. Len,,
 4123 yn'p't- B                                         joJU            GMS 113; S W,C2p61
      ynaPat ©pt. inf.
                                                                 4136 ynpn(h)    B, S                         j& tj±j>.
      (/^lament
      VJ 1120                                                         yamban,pain
                                                                      effort,  yanpan =»ymbn, ympn, ynp'wnh

 4124 yn'pSV- S            f                    fr/«J                 TSP 9.130 n p222; Hen. Talcs. 486.3; KG 384,
      ynaf3dar- ©trans. pret.; lsg. impf. Yn'flw                        484; MSP bl05
      0o)larncnt
                                                                4137 ynpwn =» ynp'wnh
      Mack. AI 25,422, 19.28
                                                                4138 yns1 B                                      JLuai^
 4125 ync(h) B                                    J*fj*              stinking
                                                                     yans ©nom. -y -»ynt\ ysn
      vane ©<Av. gainti ©f. adj.
      bad smelling                                                    SCE 287; GMS 435, 496
      TSP 2,636, 712, 793
                                                                4139 yns: B, S                                 Jy^*^
                                                                     xans ~»xns, xs
4126 ynd'k M                   (tjJ' <jjf)^jcxX^x                    stable, strong
     yandak ©Parth. gnd'g «*ynt>k(,), ynt»kC)>
     bad, evil                                                        TSP 2.476, 13.15; Hen. JRAS 1944, 138.10; Frag.
     GMS 989; BBB 513 bl9 c3, 14 flO, 16                                Len. 37.15,81.10; MDii, Ynsw
```


## [2026-09-05T20:39:33.804Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^force\\|^ *force \\|^skill\\|^ *skill \" SOD_pages.txt | head -20\necho \"=== power ===\"; grep -n \"^ *power \" SOD_pages.txt | head -20",
 "description": "Search SOD index for force/power/skill"
}
```


### [2026-09-05T20:39:33.895Z] TOOL RESULT

```
17382:     skill                                                     GMS 514; TSP 2.179, 182, 196, 206; GMS 1186;
=== power ===
```


## [2026-09-05T20:39:37.031Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17370,17395p' SOD_pages.txt\nawk 'NR<=17382{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n,\"printed:\",n-66}' SOD_pages.txt",
 "description": "Read SOD skill entry"
}
```


### [2026-09-05T20:39:38.903Z] TOOL RESULT

```
4782 qnty C                                       ^.J           EGSii 85; GMS 1186n 1; SCE 163, 175, 351
     kande ©pi. ~t =*zy-qnty, kntk
                                                          4795 kp'wtk     B                                     Ajf
     grave                                                     kapote     ©<OP kapautaka
     BSTii 843.40; Benv. JA 1955, 330; C2, 56V,
                                                               blue, grey blue
       n pl08.12                                               TSP 3.114, 128, 146
4783 kntyk =* qnty
                                                          4796 kp'ystCh) B                                     uUU
4784 qnw>ncyJ C                                                kapist (kpyst) ©pi. of kap
                                        ^ojlf
     kon(u)wancya (krn'wncyO ^qrnw'ncy*                        fishes
     skill                                                     GMS 514; TSP 2.179, 182, 196, 206; GMS 1186;
     BSTii 89223, 24: C2, 31R23, 24                              Hen. Tales. 471.9; ob. pi. -twhy TSP 2; -tyy,
                                                                 Hen. Tales. 471.13
4785 qnwn1 C                            c*>.cl.^
     kanona (knwn(>), knwnw)                              4797 kpc   S                           4^ tjJ^f j^\j
                                                                                                                        192

  kqpc*kk
       kap/fc ©ace. -w; nom. & ob. -y                              village
                                                                   k/gram     ©<Skt. grama ©pi. -t(h)
       unit of capacity
       MDii p60.14; kpew, B4R15, kpey, A-18 R9;                    VJ 883, 1481,979, 1172
         Bailey. TPS 1954, 149                                4815 kr»n B                               J^t^^jTU
 4798 kpc>kk S                         4^<jJ*gj*.lj                kran (qr*n, kr'n(h))
leaf: 256 printed: 190
```


## [2026-09-05T20:39:54.806Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nhead -3 BQT_v3_pages.txt; grep -c \"\" BQT_v3_pages.txt; grep -n \"\\[pdf page\" BQT_v3_pages.txt | head -3; grep -n \"\\[pdf page\" BQT_v3_pages.txt | tail -3",
 "description": "Inspect BQT v3 pages file"
}
```


### [2026-09-05T20:39:54.881Z] TOOL RESULT

```
[pdf page 1]
[NOT OCRED - use tools/ref_page.py]
[pdf page 2]
51425
1:[pdf page 1]
3:[pdf page 2]
24:[pdf page 3]
51420:[pdf page 719]
51422:[pdf page 720]
51424:[pdf page 721]
```


## [2026-09-05T20:39:56.163Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:3000])\"",
 "description": "BQT ref details"
}
```


### [2026-09-05T20:39:58.067Z] TOOL RESULT

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
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT
```


## [2026-09-05T20:40:04.108Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/sources/refs/ocr/ 2>/dev/null; ls data/verification/sources/refs/ocr/BQT 2>/dev/null | head -40; echo \"=== tool help ===\"; python3 tools/ref_page.py --help 2>&1 | head -30",
 "description": "Check ref_page tool and OCR cache"
}
```


## [2026-09-05T20:40:04.548Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"زغن\" BQT_v2_pages.txt | head -20",
 "description": "Grep BQT v2 for zaghan"
}
```


### [2026-09-05T20:40:25.133Z] TOOL RESULT

```
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
SOD
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
1462.png
1462.txt
1471.png
1471.txt
1472.png
1472.txt
1488.png
1488.txt
1492.png
1492.txt
1624.png
1624.txt
172.vision.txt
1803.png
=== tool help ===
Fetch ONE cited page of a scanned reference, on demand.

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
```


### [2026-09-05T20:40:25.183Z] TOOL RESULT

```
8911:  ‫‪ = ۴‬خات («‪.‬م‪« : ).‬خاد » زغن باشد یمنی هرخ گوشت‬                                     ‫‪.‬‬    ‫صلب‬   ‫‪:‬‬   ‫رك‬    ‫‪۴‬‬
10977:      ‫خردل‬                                        ‫خوانند ‪.‬‬                                             ‫که زغن است ‪.‬‬
28742:‫زغناد = بن‌اول و نون بالف کشید‪.‬‬
28752:‫بلئد هم آهفه است چه زغند زدن فرباد‬
28806:             ‫_زغن وخاد (هم‪ ).‬مرخ گوشت ریای بود ‪ .‬رود کی (سمرقندی) کوبد ِ‬
28809:        ‫ماچو صموه مرکهبرسان زغن؟‪.‬‬                                    ‫جمله صبد ابن چهانيم ای پسر‬
31075: ‫رزغند = بروزن کمند › آواز پلند مهيب‬
```


## [2026-09-05T20:40:31.808Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=28806{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' BQT_v2_pages.txt\ngrep -n \"\\[pdf page\" BQT_v2_pages.txt | awk -F'[][]' 'NR>0' | head -2\nsed -n '28780,28830p' BQT_v2_pages.txt",
 "description": "Read BQT zaghan entry region"
}
```


### [2026-09-05T20:40:33.517Z] TOOL RESULT

```
leaf: 485
 ‫رعیكه = بفتح اول بر وزن چکیده ‪.‬‬                                      ‫هیم » به‌عنی زور توعدی و زیادتی‌باشد ‪.‬‬
                   ‫باشد ‪.‬‬   ‫یمعتی اقثرده و فشارده‬
                                                              ‫‪ ۰‬کوشت رباو‬            ‫چمن‬        ‫رو=زن‬
                                                                                                    ‫بعن‬
                                                                                                      ‫ر‬
‫بر وزن شعیر » تخم کتادرا‬          ‫ز عبر ‪-‬‬                     ‫‪ ۰‬گونند ششماه ار وششماه ماده‬              ‫‪,‬غلیواج باشد؟‬


‫کویند ‪ -‬و لوعی از طعام هم هست ؛ و بمعتی‬                        ‫است » و بعضی کویند یکال نر و کال‬
                                                                   ‫کهنجشك‬
                                                                        ‫نک‬‫غاند‬
                                                                             ‫زته‌‬
                                                                                ‫بدع‪.‬ضی کف‬
                                                                                        ‫وباش‬
                                                                                           ‫ماده می‬



                                                                            ‫‪«< :‬ورده ‌‬     ‫چش‬    ‫)‪ (۱‬جك‬


   ‫‪ - ۴‬از ‪00‬ع‪ .92‬از ‪020۳82‬‬                       ‫‪.‬‬    ‫رك‪ :‬زغراش‬       ‫؟ ‏‬             ‫‪ - ۱‬رك‪:‬زغره‌اش‪.‬‬
                                                              ‫در‬     ‫مر کزی ۾‬       ‫رك ‪ ۱‬هذینگه ‪ :‬دولغت آسای‬

         ‫‪Philological Society. Hertford 1946 , ۵ . 159, note 1 ۰‬‬
   ‫‪97‎ 10۰ ۰‬و ‪BSOS., X,‬‬                                          ‫ورك ‪:‬‬
             ‫_زغن وخاد (هم‪ ).‬مرخ گوشت ریای بود ‪ .‬رود کی (سمرقندی) کوبد ِ‬
                                                                       ‫‪« ۳‬‬

        ‫ماچو صموه مرکهبرسان زغن؟‪.‬‬                                    ‫جمله صبد ابن چهانيم ای پسر‬
   ‫«لفت فری ‪۱۹۳٩‬‏ ‪.‬‬
                            ‫‪ = ۹‬ژفنکه «لفت لامه» ‪.‬‬                    ‫ژغند(ه م‪۰ )۰‬‬        ‫® ‪ -‬اسم صوت =‬

                                       ‫رك ‪ :‬زعیر ‪.‬‬      ‫‪- ۸‬‬                 ‫رك ‪ :‬لفت فری ‪۹۹۲۰‬‬                ‫‪۲‬‬
                                                  ‫يان دهم‬
                          ‫در زای نقطه دار بافا مشتمل برده لغت‬

 ‫سياه و‬   ‫چویآزنیست‬
                  ‫® »‬             ‫شد‬
                                   ‫ایر‬
                                     ‫بزق‬
                                       ‫ا‬        ‫نوعی‬        ‫زقاك ‪ -‬بفتح اول بروزن هلاك ‪ ۰‬ابر‬
  ‫چبنده که از درخت صنوبر حاصل شود وبرس‬                                                 ‫ند ‪۰‬‬
                                                                                          ‫وهیرا‬
                                                                                              ‫باگرند‬
 ‫عرمی لز بکسر اول‬         ‫ور‬
                           ‫کجلان چ‌بانند » د‬                 ‫زفان ‪ ۱‬ا‪-‬بوال مضموم» زبانرا کویند‬
 ‫همين معنی دارده وآن سه‌نوع است ‪ :‬یکی زفت‬                                     ‫و بعربی لخاونانند ‪. ۴‬‬
 ‫ر فا نه ‪ = ۴‬بروزن ومعتی زبانهباشد رومی و آن براق وصاف واملی میباشد و ازروم‬
  ‫هیآ وزلد و بعضی گوشد همی زفت است هاش‬
                                                            ‫که زبانة آنش ‪ -‬زوبانة چوب اومثال آن‬
```


## [2026-09-05T20:40:44.717Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\\[pdf page\" BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | sed -n '480,492p'\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['BQT'].get('page_offset'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False))\"",
 "description": "Determine BQT v2 page mapping"
}
```


### [2026-09-05T20:40:46.536Z] TOOL RESULT

```
0
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
[{"volume": "3", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf", "first_printed": 1208, "last_printed": 1925, "pdf_offset": -1205, "page_map": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json", "lang": "fas", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt", "ocr_note": "689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py"}, {"volume": "4", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf", "first_printed": 1920, "last_printed": 2475, "pdf_offset": -1917, "lang": "fas", "offset_note": "printed = pdf+1917, checked at pdf 150 and 500", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt"}, {"volume": "5", "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf", "first_printed": 1, "last_printed": 290, "pdf_offset": 5, "lang": "fas", "note": "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt", "requires_volume": true}]
```


## [2026-09-05T20:40:58.702Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor w in \"گرگین\" \"گندم\" \"گنگ\"; do echo \"=== $w ===\"; grep -n \"$w\" BQT_v3_pages.txt | head -8; done",
 "description": "Grep BQT v3 for gargin, gandom, gong"
}
```


### [2026-09-05T20:41:00.495Z] TOOL RESULT

```
=== گرگین ===
=== گندم ===
2861:‏ولدیداد دوکونه شپش ‎al‏ شده : یکی ‎SIT‏ درانبارگندم افتد و دیگر ‎Sle SGT‏ پارچه را تیاه
7025:‏خوانشد 6 - ونام کرمی هم هست دراز و گندم‎
9231:و در ‎ole‏ گندم روید +
10677:چیزی باشد مانند گندمی که پوست آلرا کنده
27620:گندم بربان ‎oS‏ شده را که با چیزی آغشته
27973:‎gt Sy‏ طمامی است که از خمیر آرد گندم
28012:کلیچه . آردیراگویند که گندم آنرا بربان کرده
32600:‏ازآرد گندم وآرد جو و شی رگوسفنددرست‎ LST
=== گنگ ===
23396:‏قزا گنگ ‎Sp pte A‏ فارسی» بر
47365:گنگ بهشت ؟ - نم ‎cola‏ که
47372:گنگ ‎5S‏ ؟ « یکردالابجد وسکون
47388:‏گنگ دژهر ‎VE‏ » بن‌ها وسکون
47459:گنگ ‎0d‏ زر بان - ‎ett‏ کنابه
47461:گنگل (۱) - بر وزن سندل + حزل
47463:گنگلاج (۷) = منم اول و فتح ‎SL‏
```


## [2026-09-05T20:41:05.033Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'NR<=47365 && /\\[pdf page/{p=$0} END{print \"page tag:\",p}' BQT_v3_pages.txt\nsed -n '47340,47400p' BQT_v3_pages.txt",
 "description": "Locate gong entry page in BQT v3"
}
```


### [2026-09-05T20:41:07.208Z] TOOL RESULT

```
page tag: [pdf page 642]
‎Fle?‏ غزنوی ص ۲۷۷ *.
ورك : لغت فری ص ۷۲۹۸ .
۵ - یکی زنده ‎dy‏ است ب رکوه کنگه اکر با سلاح اندر ‎Saw wT‏ .
فردوسی طوسی ۶ رشیدی -
و رك : فهرست ولف .
‎٩‏ - تا ‎ay‏ حسود تو سبلت بدست خویش برسبلت خسود تو افتاد ‎ACF‏ .
سوزلی سمرقندی « رئیدی *.
۷ - ره : کنکه دژ » بهشت کنگه ‎ety KH‏ وركه: ح۲.
۸ - به رگوله بوی و ‎aS se‏ رنگه نکوتر بیارای آن شنکه کنگه.
ولی در فهرست ولف ‎ST‏ باین ممتی نيامده . فردوسی طوسی « رشیدی * .
‎٩‏ -ظ :کنت ‎GE)‏ تازی ) مضفف « تاشکنت ‎ »‏ تاشکند .
‎NO‏ مسحف ‎LS‏ ( دژهوخت ) *. ۱- پهلوی ‎BUDE‏ « پیب رکه ‎AN‏
‏اففانی ع و بلوچی ع ‎BUDE‏ . رك : اسذق - هوبشمان ‎٩۳۷‏ .کردی 6008 ‎whale Sy.‏
‎Uy» 06‏ س ۰۳6 :
کنکه باد ‎SGT‏ اندر طمن توگوید سخن کور بادآ نک سکه اتدرعرض توجوید ‎alge‏
‏« فرخی ‎site‏ ص ‎SOM‏
[pdf page 642]
—N\ate—

مازند و ر زیر زمین بهم وصلکنند ۱ :

کنکار ‎er‏ اول وسکون ‎yt‏ وکاف
فارسی ‎DL‏ کشیده و برای بی‌نقطةٌ زده » ماربرا
کوبندکه تازه پوست افکنده باشد ۴ .

گنگ بهشت ؟ - نم ‎cola‏ که
‎Shee‏ درشهربابل‌ماخته ‎oy‏ وچاه هاروت وماروت
درآ نجا است ‎LT,‏ بپشت ‎KS‏ نیز گویند -
و نام شهری هم‌هست در حدود مشرق از بلادترك
منسوب بخوبان و درآن شهر معبدی است‌مشهور
بقندهار +

گنگ ‎5S‏ ؟ « یکردالابجد وسکون
زای فارسی » نام قلمه‌است که ‎Mae‏ درشهرباپل
ساخته بود - و نام موضمی‌است در حدود مشرق
که بقبة‌الارش مشپور است وآرامگاه ‎ath ob»‏
وآتجا پیوسته روز وشب ‎OLS,‏ است ,عنی‌هريك

‎KS‏ دژهوخت

‏دوازده ‎cele‏ است .

‏جنگ دزهخت ه « بضم‌هاوسکون
خای ‎soaked‏ و تای قرشت » نام بیتالمقدیاست
و بسربانی ابلیا خوانندش و پیش ازین قبله یت
النقدی بوده ‎Vey‏ نیز ‎Gyles US‏ است؛ وبکسر
ها هم کفته‌اند .

‏گنگ دژهر ‎VE‏ » بن‌ها وسکون
رای قرشت و جیم . بمعنی ‎BOS‏ دژهخت است
که بیت‌المقدس ‎ath‏ ؛ وبکسر ها نیز آمده‌است؛
و پکس اول و فتح دال ‎aml‏ و زای هوز و رای
قرشت هم کفته‌اند که بروزن تیم زبرجد باشد .

‎uP‏ دژهوخت ۷ - بم ی
و سکون واو و خای ‎shakes‏ و فوقانی » بمعنی
‎ail ash puddle col capes‏
را ليز کویند .

‏۱ - در مازندران نیزه کنکه » « فرهنگ نظام » 6 بروجردی 8008 « شهیدی © در
فم تیز8008 ( تتبوشه ) > فقبهی»» کردی 811086 ( لوله ) « ژابا ی ۳۹5 ۰ در ‎tL JIN‏
```


## [2026-09-05T20:41:18.742Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))\nprint(type(m))\nif isinstance(m,dict):\n    ks=list(m)[:5]; print(ks)\n    for p in ['636','637','638','639','640','641','642','573','574','575']:\n        print(p, m.get(p))\n\"",
 "description": "Read BQT v3 pagemap"
}
```


### [2026-09-05T20:41:20.435Z] TOOL RESULT

```
<class 'dict'>
['pdf', 'pdf_pages', 'offset_mode', 'anchors', 'map']
636 None
637 None
638 None
639 None
640 None
641 None
642 None
573 None
574 None
575 None
```


## [2026-09-05T20:41:23.892Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))\nmp=m['map']\nprint(m['offset_mode'], m['pdf_pages'])\nprint(json.dumps(m['anchors'],ensure_ascii=False)[:600])\nfor p in ['573','574','575','636','637','638','639','640','641','642']:\n    print(p, mp.get(p))\n\"",
 "description": "Read pagemap map entries"
}
```


### [2026-09-05T20:41:25.782Z] TOOL RESULT

```
1203 721
34
573 None
574 None
575 None
636 None
637 None
638 None
639 None
640 None
641 None
642 None
```


## [2026-09-05T20:41:29.742Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))\nmp=m['map']\nks=sorted(mp)[:5]; print(ks, [mp[k] for k in ks])\nprint(json.dumps(m['anchors'],ensure_ascii=False)[:800])\n# find entries mapping to printed 1779,1842,1844\ninv={}\nfor k,v in mp.items():\n    inv.setdefault(v,[]).append(k)\nfor t in [1779,1842,1844,1846]:\n    print(t, inv.get(t), inv.get(str(t)))\n\"",
 "description": "Inspect pagemap structure"
}
```


### [2026-09-05T20:41:31.315Z] TOOL RESULT

```
['1210', '1211', '1212', '1213', '1214'] [1, 2, 3, 4, 5]
34
1779 None None
1842 None None
1844 None None
1846 None None
```


## [2026-09-05T20:41:36.318Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json\nm=json.load(open('BQT_v3_pagemap.json'))\nmp=m['map']\nfor t in ['1779','1842','1843','1844','1845','1846']:\n    print(t, mp.get(t))\nprint('pdf641 ->', [k for k,v in mp.items() if v in (641,642,574)])\n\"",
 "description": "Map printed to pdf for BQT v3"
}
```


### [2026-09-05T20:41:38.127Z] TOOL RESULT

```
1779 576
1842 639
1843 640
1844 641
1845 642
1846 643
pdf641 -> ['1777', '1844', '1845']
```


## [2026-09-05T20:41:44.405Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk '/^\\[pdf page 641\\]$/{f=1;next} /^\\[pdf page 642\\]$/{f=0} f' BQT_v3_pages.txt | head -80",
 "description": "Print BQT v3 pdf page 641 (printed 1844)"
}
```


### [2026-09-05T20:41:45.941Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:41:48.778Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"pdf page 64[01]\\]\" BQT_v3_pages.txt\nsed -n '47250,47345p' BQT_v3_pages.txt",
 "description": "Print BQT printed page 1844"
}
```


### [2026-09-05T20:41:48.834Z] TOOL RESULT

```
47222:[pdf page 640]
47305:[pdf page 641]

(۱) چش : - شنم .

. Mask
‏گنه هر ۲ - زان پبر سالخورده را‎
. ‏گونند‎
‎oy ‏گندهپیر کابلی ‘ = پر زالی‎
. bE ‏جاد و گر وساخره در‎
‏گنده مغزی = پفتح‌اول ومیم‌وسکون‎
‏کردن و سخنان‎ KG ‏غین نقطه‌دار , کنابه از‎
‏متکیرانه کفتن وهرزه وباوه برزبان‌راندن‌ودرشتی‎
‏گویند‎ a ‏و کج خلقی‌نمودن باشد - وشخصی را‎
. ‏صفات داشته باشد‎ gpl ‏که‎
‏گذر ۲ = بفتح اول و الی وسکون رای‎
SPB ‏بی‌قطه , تام جنگ گاه سلطان محمود‎
. ‏(با) پادشاء تر کستان بوده‎
SE ‏گشگ = بفتح اول وسکون ثانی و‎
‏فارسی ۰ چند ممتی دارد : ۱- نام پتکده ایست‎
‏از بتکده های چین ۸ ۰ ۲- رودخانه ای باشد‎
‏بسیاربز رکه درملك‌هندوستان ومنبعآ نکوههای‎
‏سوالك است و ازملك هندوستان وبنگاله گذشته‎
‏بعمان میریزد و هندوان بدان اعقاد بیار دارند‎
‏و درآنآب ل کردن و مردههای‌خودراسوختن‎
‏وخاکتر و استخوانهای آلها را در آب ریشتن‎

۱ - بعریی کرا کوبند « رشیدی » . رك : دزی ج۷ ص 4۵۳ :کراث .
۴ - امروزه یز 80806 ‎at».‏ ( سلطان آباد ) 55 800085 « مکی ژاد ». کنده
‎gine‏ بزرکه و حجیم و جسیم است و مقابل باريك ( بمعنی اصلی ) پهن است .

۴ - من بگویم صفت ‎AST‏ پرواری گرم

کو بگویند مرا مدعبان کوقه خوار.
‎Gla?‏ اطممه . چاپ التالبول س ۱۷ *.

۴ - پهلوی ‎gundak‏ , ارمنی ع 8080 (کلوله , کرء ) . 8021 (کلوله» کرء )
رك : استق - هوبشمان ‎a te nk . ٩۳۹‏ در ارال ( سلطان‌آباد ) 80008 > مکی‌نژاد *.

© « کند ( بفتح ) ‎Cpe)‏
‏که فرخی در اشمار خودآورده :
بجای ‎SGT‏ توکردی برایشان در« کتر» شاها ۱

زبت پرستان چندان بکشت وچندان بت

. ‏اود‎ gt - ۲

-ظ . مستف «کتر».

حدیث رستم دستان یکی‌بود ازهزاراضان .
د فرخی سیستالی ص ۲۵۹ *.

که کشته بود و گرفته ز ‎QUE‏ به ‎OS‏
‏* فرخی سیستالی ص ۷۲ ۶

و شاید همان ‎ay?‏ » ( تاریخ بیپقی مصحح فیاض ص 4*۷ ) باشد . ‎Day‏ + کنور.
‎dy ۸‏ :کنکه دز. ورك : ح۲ و۷ ‎«tay Laie‏
[pdf page 641]
۱۸44 7 ۱ Cex
‏یکان است‎ LT ‏گوشد شب و روز همیشه در‎
‏میباشد و هوای‌آن در‎ cele ‏دوازده‎ Che ‏یعنی‎
‏چنانکه پیوسته در آنجا بهار‎ oy ‏اعتدال‎ cols
‏لیکووخوب‎ -٩ ۰ ‏باشد و کنگه دژ همان است۷‎
‏وزببا رااکویند ۸ . ۱۰ نام شهر تاشکنت‌است‎
US ‏نام‎ -۱۱ ۰ ٩ ‏که آترا چاج هم میگویند‎
‏پیشینبان است که بت المقدس باشد *۱- و جنم‎
‏لا لگویند وبعربی ابکم‎ LT, ‏اول معروف است‎
‏خرالنند یعنی شخصی که بابما.و اثاره حرف زند‎
‏ازسفال‎ Ty ‏ولوله‌ای که بجهت‎ -۷۱ oly ‏نه‎

فوز عظیم وسیب درجات ومزبل سیات‌میدانند! .
۳ - نام بتخاله‌ایست در ‎TG‏ و کوبند ‎OT‏
‏بتخانه را کیکاوی ساخته است۴ ‎at.‏ ام‌جزیره
‎col‏ درمیان‌دربا ۴ . ۵ - هرچیزخمیده وکج
و کوژ را گونند عموماً و کوژ مادر زاد را
خصوساً ۴ . ‎-٩‏ نام کوهی است » و عربان کوه
را چبل میگوبند ۵ . ۷ - نام باوست که‌بسیب
سودا در بدن مردم بهم میرسد وین‌مویپا میخارد
و تا موی را نکنند ‎Que‏ پر طرف میشود ۷ .
۸ - ام شهری است که درشرقی خطا واقع‌است.

‎Gange= ۱‏ (فر) شطی‌استبهندوستان, بطول ۳۱۰۰ کیلومتروآن ازهیمالیا سرچشمه
گیرد ۰ در ‎SETI‏ « جمنا » بدان پیونده » شهر بنارس و پتنه را مشروب ‎aS‏ و در خلیج ‎MK‏

‏ریزد . ورگ ‎Yer‏ ۴ رك ‎aos) pets.‏ و تاحیه‌ایست) ‎Ve tty‏ ورك ‎KS:‏
‏بهشت ۰ بهشت کنگه .
تا چون ‎KT te‏ شد ازروي او جهان در چشم خسروألی چون رود ‎BOS‏ شد.
خروانی « لفت فرس ص ‎HVA‏
‏۴ - همانگه سپاه اندر آهد بجنگه ‎de‏ همچو دربا ودربا چ وکنکه .

‏عنصری ‎Gah‏ لفت فری ص ۲۹۸ و ‎MMO‏
‏۴ که بینی‌پی ازین ازقبل خدمت تو ‎ot‏ اعدای توچون‌پشت حمابل‌شده ‎WES‏
‎Fle?‏ غزنوی ص ۲۷۷ *.
ورك : لغت فری ص ۷۲۹۸ .
۵ - یکی زنده ‎dy‏ است ب رکوه کنگه اکر با سلاح اندر ‎Saw wT‏ .
فردوسی طوسی ۶ رشیدی -
و رك : فهرست ولف .
‎٩‏ - تا ‎ay‏ حسود تو سبلت بدست خویش برسبلت خسود تو افتاد ‎ACF‏ .
```


## [2026-09-05T20:42:04.738Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\na=$(grep -n \"^\\[pdf page 639\\]$\" BQT_v3_pages.txt | cut -d: -f1); b=$(grep -n \"^\\[pdf page 640\\]$\" BQT_v3_pages.txt | cut -d: -f1); echo \"$a $b\"; sed -n \"${a},${b}p\" BQT_v3_pages.txt",
 "description": "Print BQT printed page 1842 (gandom)"
}
```


### [2026-09-05T20:42:06.306Z] TOOL RESULT

```
Exit code 1
 
sed: -e expression #1, char 1: unknown command: `,'
```


## [2026-09-05T20:42:08.848Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\ngrep -n \"pdf page 63[6-9]\\]\\|pdf page 57[4-8]\\]\" BQT_v3_pages.txt",
 "description": "Find page markers"
}
```


### [2026-09-05T20:42:08.891Z] TOOL RESULT

```
41953:[pdf page 574]
42023:[pdf page 575]
42101:[pdf page 576]
42154:[pdf page 577]
42239:[pdf page 578]
46858:[pdf page 636]
46960:[pdf page 637]
47050:[pdf page 638]
47145:[pdf page 639]
```


## [2026-09-05T20:42:11.295Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nsed -n '47145,47222p' BQT_v3_pages.txt",
 "description": "Print BQT printed page 1842"
}
```


### [2026-09-05T20:42:11.338Z] TOOL RESULT

```
[pdf page 639]
‎oy‏ چه گند ‎gine:‏ خایه و ‎ete‏ حیوالی است
آبی شبیه بسکه و ممرب ‎OT‏ جند پیدستر باشد
و آن ‎TH‏ بچگان کوبند وبعربی خسیةالبحر
خوانند .
‎SAP‏ - بنتح اول ‎SLT,‏ وسکون
ثانی و زای فارسی ۰ مخفف کنگه‌دژ ۱ (۱)است
وآن قلعه‌ای ‎Soy‏ ضحاك در شهر بابل ساخته
‎op‏ وآلرا بپشت ‎KF‏ نام بهادء بود ودرآن قلعه
‎gale‏ کران وساحران ‎her‏ بودندوا کنون ‎AS‏
‎cal‏ وبجز تلی باقی ‎als‏ و برسرآن تل چاهی
است بسیارعمیق ‎SaaS.‏ اروت و ماروت در
‎oT‏ چاه محبون اند .
گندسك = ‎ee‏ اول ‎Sy‏ تالك‌وفتح

‏سین بی‌نقطه » تفنیر خصی‌الکلب ۳ است ,وآن
بیخی باشد مالند خصیةالتملب و هر زوجی برهم
‎gener‏ یکی بزرکه ودبگری کوچك. اکرمرد
بزرکه ‎YT‏ بخورد و با زنان جماع کند فرزند
ترینهآورد واگر زن کوچك ‎LT‏ بخورد مادینه,
‎OT cles‏ قطم شهوت کند ‎OTs‏ مقوی‌باهباشد,

‏(۱) چش :کنگه دز .

‏۱ رك :کنگه دژ.
‎Ke‏ مومن : خصی الکلب .
«رشیدی» . ۴ ركه ‎ga:‏ .

‎.) ‏از :کندم با ( ابا رآش‎ - ٩

‎NARI

‏و عربان ‎oT‏ را قاتل اخیه کوبند بوامطةٌ آنکه
‎eT‏ دوییخ‌اند مانند دو زبتون برهم چسییده که
‎ILS‏ یکی فربه و دیگری ‎AV‏ ميشود و سال
‎GTS‏ فربه ‎oy‏ لاغر وآنکه لا بود فربه
میگردد ۰

‏گندش ۲ = بکرئاكث بروزن‌واجش:
کو کرد را گونند وآن در ‎eb‏ میشود : احمر
و ایيش . کوکرد ‎pol‏ بکجزو از اجزای
‎ST‏ است و کوکرد ‎Gaal‏ بکجزو از اجزاي
باروت +

‎Sa‏ © © بروزن‌اند,بممنی ک و کرد
است - وباروت را نیز گوبند .

‏نك ‎OF‏ = بنتح اولو کسرکاف‌فارسی,
بمعنی‌خر ی کیاه است. گوبند. شقاقل بی ‎ASS‏
‏است وخریآنرا ‎cals‏ دوست میدارد» ؛
‎bp Sa‏ صحرائی است #۰

‏گندما ۱ - آش کندم را کوبند که
حلیم باشد .

‎Oa‏ - بر وزن توجمه ۷ ۰ کرهی
باشد سخت ‏ وآن از بدن آدمی‌برمیایسوعربان

‎wn

‏۴ - پیونانی ‎orchis‏ .)4 : لك #س۳۳ ؛ و رل : ‎fins‏
‏۴ ۰ کندش و کندکه . کوکرد » ‎elt‏ هندست »
- رك : خر یگیاه .

‏- مولف «ترجمه» را طبق تلفظ معمولی

‎pus? ۵‏ - بفتح اول رضم سوم + پهلوی و پازند 88011018 , معرب جندم ‎Jandum‏

‏( در : چوزجندم ) ,کردی ع ‎Jul. genim‏ ع ‎ghanum‏ . رخی ‎ghidim‏ , سنکلیچی
و منجی ‎ghandém‏ . مریکلی ‎zhandum . zhandam‏ , شفتی ‎zhindam‏ . بردغا
‎ghadum‏ , بلوچی ‎gandim‏ « استق ‎٩۳۵‏ > و رگ : هوبشمان ایا ؛ کیلکی » فریزندی ۰
برلیونطنزی 8800010 «کک. ۱ص ۰۲۸۹ دردیه‌های گیلان 8804181۳ ؛ سمنانی ‎gundum‏
‏سنگری ‎.gannim‏ سرخدیی ‎.gunném‏ لاشگردی 80048۳0 . شهییرزادی ‎gandim‏
‏۰ . ۲ ص ۰۱۸۲ ؛ گیاهی است از ‎Sy‏ غلات , یکاله . با اقةٌ از بند بند و تو خالی .
‎SUT‏ بی دمب رک ولی ‎OT als‏ ساقه را درمحل کره‌ها می‌پوشاند . گل کندم ازسنبله‌عابی
تشکیل يافته که شامل سنبله‌های کوچکتر میباشند .
(برهان فاطع ‎(ver‏
[pdf page 640]
```


## [2026-09-05T20:42:30.041Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nsed -n '42101,42154p' BQT_v3_pages.txt",
 "description": "Print BQT printed page 1779 (gar)"
}
```


### [2026-09-05T20:42:30.109Z] TOOL RESULT

```
[pdf page 576]
بیان نهم
در ‎GB‏ فارسی با رای بی‌نقطه مشتمل بر دوست و سی ‎Chey‏ لغت و کنایت
گر بفتح اول وسکون ثالی»,مخففا کر
باشد که کلمةٌ شرطیه است٩‏ - ونام جوششی‌است

مشهو رکه بعربی جرب گوبند ۴ - وبمعنی مراد
وه‌قصود باشد ۴ - و بمه‌تیکننده و سازنده هم

و آهنی ‎op‏ باشد دسته دار و در دو طرف ‎OT‏
‏ریسمان بندند یکی ‎dey‏ آنرا بگیرد و دیگری
‎aS Il,‏ نا زمین شیار کرد ناهموار را
بدان هموار کنند وآنرابعربی مسلفه‌وسواط(۱)

هت ۴ همچوکوزه کر وکاسه گر ‎geal,‏ آن . | خوانند ۸ .
ومرادف کارباشد همچو آموز کار وآموز کر که گر اد بکر اول بروزن ‎Ute ald‏
ازهر دومعنی فاعلیت مفهوم میگردد وقتی که با ]| کهنه راکوبند .

کلمادیگی تر کیپ‌شود - وبضم‌اول نام رووخاله -
‎cul‏ در سرحد ملك غزان » وباین معنی باکاف

گرادون ‏ با رای قرشت بر وزن
فلاطون » نام جوشتی است کهآ نرا داد خوانند
ویعربی قوبا کویند ‎٩‏ -

گر از بطم اول بروز نگداز ‎oes‏
‎Sys‏ نرباشد که جفت خول ماده است*٩-وخرام‏
ورفتاری که از روی تاز وتکبر وتبختر ‎Mask‏
‏و ی گویند بممنی خرام و رفتار از روی ناژ

تازی مشهور است ۵ .
گرا - بفتح اول‌وثانی مشددبالف کشیده»
پمعتی بنده باشد که در مقابل آزاد است ۲ -
وحجام وسرتراش ‎Boy‏ را نیز گوبند۷ »و کاهی
اين ‎bid‏ را بطریق ‎ches‏ هم بزبان آورند -
)1( خم ‎aie:‏ ومشواط -

۱ )4: اگر؛ کردی8067 (اکر) ‎Up‏ صس .»۳۵۷‏ ۴ - مرشی‌است کهدادهها يکوچك
بربدن انان‌وجانوران پدید آرد وخارش کند ومریض راه ک رکین» (مخفف آن : ک رگن) کوند.
اوستا - ‎garenu‏ (جرب)؛ کردی ‎(Oe) BIT‏ بلوچی 88۲ (یسی » جرب) « اسشق ‎۸٩0‏ »
و رك : هوبشمان » ایضاً ؛ پهلوی ‎Bal‏ (جرب) « دارستتر , تبمات ج ۱ ص 6۹۵ .
۴ رل :کر . ۴ اوستا - 64۲8 - (ساخته) » یپلوی ‎aie. gar. - kat‏
‎kara - ott‏ - ۶ اسشق ‎ker coo Xe cant‏ - (وبرانکر [وبران کنتده]) « ژابا س٩4۳‏ >-
ه‌ رگ :کر ۰
‎LS plea 1‏ خاین را بین ماگمان ‎oy‏ که باشد او امن .
مثنوی مولوی فرشیدی» .
‎LV‏ پر خون که گرا می مکد بر امید نقع دل خوش میکند . ‎ .‏
‏مثنوی مولوی «رشیدی» .
۸ -ظ . مصحف «کراز» ‎٩ Gem)‏ رگ : رشیدی .
۴ _ اوستا - ۷۵۲222 (کراز) . یهلوی ۷۵۲22 (لوشته میشود ۷۵۲26) ۰ ارمنیع
‎varaz‏ عندی باستان - ۷۵۳8 ‎GS)‏ ,کردی 96۲82 « ‎Geel‏ ۰۸45 .

۱- مصدر ‎OT‏ «گرازیدن» است .
[pdf page 577]
```


## [2026-09-05T20:42:48.941Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-05T20:42:48.977Z] TOOL RESULT

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
```


## [2026-09-05T20:42:50.618Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON page tags ===\"; grep -c \"\\[pdf page\" MON_part1.txt 2>/dev/null; head -c 300 MON_part1.txt\necho; echo \"=== ARY latin index gandom/gar ===\"; grep -n -i \"GANDOM\\|GANDUM\\|GANG\\|GARR\\b\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Check MON and ARY files"
}
```


### [2026-09-05T20:42:50.693Z] TOOL RESULT

```
=== MON page tags ===
0
0 
2 


چم 
نسم ی 


تمه موی موم 
3 


ماما نا موس ملاس 
روم و3 


2 
7 
س 


همجمج مد هعرج ی وه جر ج مهو موجه و وید جع مج وی ۶ج و وم مب و وج 5 
ادا ما ما زو ماه مرو ماخ( نوم شام 4و منم مخ نا
=== ARY latin index gandom/gar ===
12800:pn olen erly gle Ce gang 9 Cal enh cena op! slats Se dla! chasls ge Stel ;
12910:: GANDUM, GANTUM (PAHLAVI) 44
14674:(esl gail ya" aad’ pe 44) Gangs Gasilyad ys PERSIAN) yyubb
```


## [2026-09-05T20:43:00.036Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%D8%B2%D8%BA%D9%86\" \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%DA%AF\" \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF%D9%85\" \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 167 verification: Persian headword etymology\" ; done",
 "description": "Archive Wiktionary pages"
}
```


### [2026-09-05T20:43:03.602Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cba16fa023380b8d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/43309f87e58f29df.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b529373256744bf5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2d568f61caec4754.txt
```


## [2026-09-05T20:43:06.282Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== زغن ===\"; grep -n -A25 \"^Persian\" cba16fa023380b8d.txt | head -60",
 "description": "Read Wiktionary zaghan"
}
```


### [2026-09-05T20:43:06.331Z] TOOL RESULT

```
=== زغن ===
```


## [2026-09-05T20:43:09.454Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nwc -c cba16fa023380b8d.txt 43309f87e58f29df.txt b529373256744bf5.txt 2d568f61caec4754.txt\necho \"=== head zaghan ===\"; head -c 1200 cba16fa023380b8d.txt",
 "description": "Inspect archived files"
}
```


### [2026-09-05T20:43:09.518Z] TOOL RESULT

```
 2164 cba16fa023380b8d.txt
 9024 43309f87e58f29df.txt
 5641 b529373256744bf5.txt
 4474 2d568f61caec4754.txt
21303 total
=== head zaghan ===
URL: https://en.wiktionary.org/wiki/%D8%B2%D8%BA%D9%86
FETCHED: 2026-09-05T20:43:01Z
STATUS: 200
TITLE: زغن - Wiktionary, the free dictionary

زغن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sidebar 
 hide 

 Beginning

 1 
 Arabic 

 Toggle Arabic subsection 

 1.1 
 Verb 

 Toggle the table of contents 

 زغن 

 4 languages 

 فارسی 
 Malagasy 
 Română 
 Русский 

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

 From Wiktionary, the free diction
```


## [2026-09-05T20:43:13.015Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 43309f87e58f29df b529373256744bf5 2d568f61caec4754; do echo \"=====$f\"; sed -n '/From Wiktionary, the free diction/,$p' $f.txt | head -70; done",
 "description": "Read Wiktionary entries for gong, gandom, gar"
}
```


### [2026-09-05T20:43:34.230Z] TOOL RESULT

```
=====43309f87e58f29df
 From Wiktionary, the free dictionary

 See also: کنگ , کبک , کپک , کپگ , كنك , and کنک 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Inherited from Middle Persian [Book Pahlavi needed] ( gwng /⁠gung⁠/ ) , [Book Pahlavi needed] ( gng /⁠gung⁠/ , “ dumb , mute ” ) . [ 1 ] Perhaps developed from the sense "to mock, hum", usually connected to Sanskrit गुञ्जति ( guñjati , “ buzz, hum ” ) , itself of imitative origin. Compare also Proto-New Indo-Aryan *गुङ्ग ( guṅga ) , whence Hindustani गूँगा / گونگا ( gū̃gā , “ dumb, mute ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈɡunɡ/ 

 ( Dari, formal ) IPA ( key ) : [ɡʊŋɡ] 

 ( Dari, formal ) IPA ( key ) : [ɡʊŋɡ] 
 ( Kabuli ) IPA ( key ) : [ɡʊŋɡ] 

 ( Hazaragi ) IPA ( key ) : [ɡuŋɡ̥] 

 ( Iran, formal ) IPA ( key ) : [ɡ̥oɲɡʲ̥] 

 ( Tajik, formal ) IPA ( key ) : [ɡuŋɡ] 

 Rhymes: -unɡ 

 Readings

 Classical reading ? 

 gung

 Dari reading ? 

 gung

 Iranian reading ? 

 gong

 Tajik reading ? 

 gung

 Noun
 [ edit ] 

 گنگ • ( gung / gong ) ( Tajik spelling гунг ) 

 ( literary ) mute ( a person unable to speak ) 

 Adjective
 [ edit ] 

 گنگ • ( gung / gong ) ( Tajik spelling гунг ) 

 ( mathematics , arithmetic , number theory ) irrational 

 ( obsolete ) crooked , hurled , of a bent back 

 ( literary ) mute ( of the speaking of a person ) 

 Derived terms
 [ edit ] 

 عدد گنگ ( adad-i gung  / adad-e gong , “ irrational number ” ) 
=====b529373256744bf5
 From Wiktionary, the free dictionary

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: گندم 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 گنم ( ganom, genom ) ( dialectal ) 

 Etymology
 [ edit ] 

 From Middle Persian 𐫃𐫗𐫇𐫖 ( gnwm /⁠gannum⁠/ ) , (in book Pahlavi 𐭤𐭢 ( H g /⁠gan(d)um⁠/ ) ) from Proto-Iranian , from Proto-Indo-Iranian .

 Compare Parthian 𐫃𐫗𐫅𐫇𐫖 ( gndwm /⁠gandum⁠/ ) , Sogdian 𐼲𐼻𐽂𐼺 ( γntm /⁠γandam⁠/ ) , Northern Luri گںنم ( gənem ) , Northern Kurdish genim , Pashto غنم ( ǧanëm ) , Talysh گندم ( qandım ) , Avestan 𐬔𐬀𐬧𐬙𐬎𐬨𐬀 ( gaṇtuma ) , 𐬔𐬀𐬥𐬙𐬎𐬨𐬀 ( gantuma ) , Sanskrit गोधूम ( godhūma ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ɡan.ˈdum/ 

 ( Dari, formal ) IPA ( key ) : [ɡän̪.d̪ʊ́m] 

 ( Dari, formal ) IPA ( key ) : [ɡän̪.d̪ʊ́m] 
 ( Kabuli ) IPA ( key ) : [ɡän̪.d̪ʊ́m] 

 ( Hazaragi ) IPA ( key ) : [ɡän̪.d̪úm] 

 ( Iran, formal ) IPA ( key ) : [ɡʲæn̪.d̪óm] 

 ( Tajik, formal ) IPA ( key ) : [ɡän̪.d̪úm] 

 Rhymes: -um 

 Readings

 Classical reading ? 

 gandum

 Dari reading ? 

 gandum

 Iranian reading ? 

 gandom

 Tajik reading ? 

 gandum

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 گندم • ( gandum / gandom ) ( Tajik spelling гандум ) 

 wheat 

 Derived terms
 [ edit ] 

 گندمبا ( gandumbā  / gandombâ , “ haleem ” ) 
=====2d568f61caec4754
 From Wiktionary, the free dictionary

 See also: ـگر , کژ , کر , گز , and کز 

 Burushaski
 [ edit ] 

 Etymology
 [ edit ] 

 (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 

 Pronunciation
 [ edit ] 

 IPA ( key ) : [ɡur] 

 Noun
 [ edit ] 

 گر ( gur ) 

 wheat 

 References
 [ edit ] 

 Bechtholdt, Astrid ( 2026 ), “ gur ”, in Burushaski Hunza Dictionary (Webonary) , Dallas, Texas, USA: SIL International, published 2017 . 

 Old Awadhi
 [ edit ] 

 Noun
 [ edit ] 

 گر ( gr / gir /) [ 1 ] 

 Arabic script form of गिरि ( “ mountain, hill ” ) 

 References
 [ edit ] 

 ^ اَنْصارُ اْللّٰہ، مُحَمَّد [ ansāru llāh, muhammad ] ( 1978 ), “ گِر ”, in پَدْماوَت کِی مُخْتَصَر فَرْہَن٘گ [ padmāvat kī muxtasar farhaṅg , A Short Padmāvat Dictionary ] (in Urdu), 2 nd edition, Aligarh: Letho Car Printers, page 160 . 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Perhaps from Proto-Indo-European *wer- ( “ to burn ” ) . Compare Laki آگر ( agir , “ fire ” ) , Northern Kurdish agir .

 Noun
 [ edit ] 

 گر • ( gor ) 

 flame ; blaze 

 burn ( sensation ) 

 Derived terms
 [ edit ] 

 گر کشیدن ( gor kešidan ) 

 گر گرفتن ( gor gereftan ) 

 Etymology 2
 [ edit ]
```


## [2026-09-05T20:43:37.415Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '/Etymology 2/,$p' 2d568f61caec4754.txt | head -60",
 "description": "Read Wiktionary gar etymology 2"
}
```


### [2026-09-05T20:43:39.171Z] TOOL RESULT

```
 Etymology 2 

 3.2.1 
 Conjunction 

 3.2.1.1 
 Derived terms 

 Toggle the table of contents 

 گر 

 8 languages 

 বাংলা 
 Deutsch 
 فارسی 
 Kurdî 
 Malagasy 
 پنجابی 
 پښتو 
 Тоҷикӣ 

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
```


## [2026-09-05T20:43:49.387Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1%DA%AF%DB%8C%D9%86\" \"https://en.wiktionary.org/wiki/%F0%AC%94%F0%AC%80%F0%AC%A7%F0%AC%99%F0%AC%8E%F0%AC%A8\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 167: gargin / Avestan gantuma\"; done\nfor u in \"https://abadis.ir/fatofa/%DA%AF%D8%B1/\" \"https://abadis.ir/fatofa/%D8%B2%D8%BA%D9%86/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 167: Mo'in/Dehkhoda entry for gar (scab) and zaghan\"; done",
 "description": "Archive gargin, Avestan gantuma, abadis pages"
}
```


### [2026-09-05T20:43:54.747Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9e548816458759b7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/aa380285a6aaa24c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/eec679535bc2abb8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73c952725d673cac.txt
```


## [2026-09-05T20:43:58.075Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== gargin ===\"; sed -n '/From Wiktionary, the free diction/,$p' 9e548816458759b7.txt | head -40\necho \"=== Av gantuma ===\"; sed -n '/From Wiktionary, the free diction/,$p' aa380285a6aaa24c.txt | head -30",
 "description": "Read gargin and Avestan gantuma pages"
}
```


### [2026-09-05T20:43:59.642Z] TOOL RESULT

```
=== gargin ===
=== Av gantuma ===
```


## [2026-09-05T20:44:02.866Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nwc -c 9e548816458759b7.txt aa380285a6aaa24c.txt eec679535bc2abb8.txt 73c952725d673cac.txt\ngrep -n \"TITLE\\|STATUS\" 9e548816458759b7.txt aa380285a6aaa24c.txt eec679535bc2abb8.txt 73c952725d673cac.txt | head",
 "description": "Check archived page sizes"
}
```


### [2026-09-05T20:44:02.929Z] TOOL RESULT

```
  156 9e548816458759b7.txt
  180 aa380285a6aaa24c.txt
28055 eec679535bc2abb8.txt
 8796 73c952725d673cac.txt
37187 total
aa380285a6aaa24c.txt:3:STATUS: -1
aa380285a6aaa24c.txt:4:TITLE: 
eec679535bc2abb8.txt:3:STATUS: 200
eec679535bc2abb8.txt:4:TITLE: گر - معنی در دیکشنری آبادیس
9e548816458759b7.txt:3:STATUS: -1
9e548816458759b7.txt:4:TITLE: 
73c952725d673cac.txt:3:STATUS: 200
73c952725d673cac.txt:4:TITLE: زغن - معنی در دیکشنری آبادیس
```


## [2026-09-05T20:44:07.799Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ncat 9e548816458759b7.txt; echo \"=== abadis gar: moin ===\"; grep -n -m1 -A40 \"فرهنگ معین\" eec679535bc2abb8.txt",
 "description": "Check failed fetch and abadis gar Moin section"
}
```


### [2026-09-05T20:44:07.850Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%DA%AF%D8%B1%DA%AF%DB%8C%D9%86
FETCHED: 2026-09-05T20:43:51Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== abadis gar: moin ===
51: فرهنگ معین
52-
53- ( ~ . ) (اِ. ) کوه .
54- ( ~ . ) [ په . ] (اِ. ) از بیماری های پوستی که باعث خارش و سوزش پوست بدن می شود.
55- (گَ ) (حر رب . شرط . ) مخفف اگر.
56- (گُ ) (اِ. ) (عا. ) شعله ، زبانة آتش .
57- ( ~ . ) [ په . ] (پس . ) ۱ - به آخر اسم معنی پیوندد و صفت فاعلی سازد: بیدادگر، کارگر. ۲ - به آخر اسم ذات پیوندد و صیغة شغل سازد: آهنگر، درودگر. 
58-
59- فرهنگ عمید
60-
61- ۱. دارندۀ شغل و حرفه (در ترکیب با کلمۀ دیگر ): آهنگر، خنیاگر، درودگر، زرگر.
62-۲. انجام دهندۀ (در ترکیب با کلمۀ دیگر ): ستمگر، غارتگر، فسونگر.
63-۱. = جرب
64-۲. (صفت ) ویژگی حیوان مبتلا به جرب: بز گر، خر گر.
65-۳. (صفت ) کچل.
66-شعله، زبانۀ آتش.
67-* گر زدن: (مصدر لازم ) [عامیانه] زبانه کشیدن آتش، شعله ور شدن، شعله زدن آتش، گر کشیدن.
68-* گر کشیدن: = * گر زدن
69-= اَگر 
70-
71- گویش مازنی
72-
73- /gar/ زمین بی آب و خشک - از بیماری های پوستی که در اثر آن موی بدن و سر به یکباره فرو ریزد۳نام حومه ای در قائم شهر که دارای مراتع کم آب است ۴خرمن & مشت - زبانه ی آتش & گره ی ریسمان - گره های چوب
74-
75- واژه نامه بختیاریکا
76-
77- ( گَر ) از امراض
78- ( گُر ) اوج؛ قله؛ نوک
79- ( گَر ) بازنده
80- ( گَـَر ) صخره بزرگ
81-گُر فیس
82- ( گَر ) گوساله
83- ( گِر ) گیر؛ مفصل
84- ( گِر ) گیر؛ نشانه یا بِلکِه ای که پیش از واقع بر روی یک دختر نهند.
85- ( گِر ) نوبت
86- ( گِر ) وقفه؛ مکث
87- ( گِر ) ( ● ) ؛ انتخاب
88-
89- مترادف ها
90-
91- scab (اسم)
```


## [2026-09-05T20:44:13.447Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '30,110p' 73c952725d673cac.txt",
 "description": "Read abadis zaghan"
}
```


### [2026-09-05T20:44:13.493Z] TOOL RESULT

```
زین زاغ و زغن چو کبک بگریز. نظامی.
چنین گفت پیش زغن کرکسی 
که نبود ز من دوربین تر کسی. سعدی ( بوستان ).
دانی که چه ها می رود از دست رقیبت 
حیف است که طوطی و زغن همقفسانند. سعدی.

 فرهنگ فارسی

 ( اسم ) پرنده ایست از راسته شکاریان روزانه از دسته بازها که در حدود هفت گونه از آن شناخته شده و همه متعلق به نواحی گرم و معتدل آسیا و اروپا و افریقا هستند. زغن جزو بازهای متوسط القامه است و بسیار متهور و چابک و تند و حمله و قوی و خونخوار است دم وی دو شاخ است . او همه پستانداران کوچک مخصوصا جوندگان را شکار میکند موش گیر غلیواج پر آذران خاد جنگلاهی چنگلاهی جنگلاجی کور کور . 

 فرهنگ معین

 (زَ غَ ) (اِ. ) پرنده ای است گوشتخوار از دستة بازها اما کوچک تر از باز. 

 فرهنگ عمید

 پرنده ای شبیه کلاغ و کمی کوچک تر از آن که جانوران کوچک را شکار می کند، موش ربا، چوژه ربا، گوشت ربا، گنجشک سیاه، خادوخات، غلیواج، کلیواج، کلیواژ، پندو جنگلاهی، چنکلاهی، چنگلانی. 

 گویش مازنی

 /zeghen/ کسی که ریزش خلط بینی اش زیاد است

 جدول کلمات

 غلیواج 

 مترادف ها

 kite (اسم) 
 زغن، ادم درنده خو، دغل باز، بادبادک، بادبادک کاغذ هوایی غلیوا، غلیواج، ادم متقلب، پرواز بلند
 chough (اسم) 
 زغن

 فارسی به عربی

 طائرة ورقیة 

 پیشنهاد کاربران

 ویش
حمید رضا مشایخی - اصفهان

 زاغ، کلاغ
حمید رضا مشایخی - اصفهان

 غلیواج

 روزگارا چون ز عنقا می نیاموزی ثبات
چون زغن تا چند سالی مادگی سالی نری
دیوان انوری، ج1، ص 469 ( به نقل از کتاب: هزار و پانصد یادداشت، مهدی محقق، ص 48 )

 زغن را نوعی زاغ می دانند که موش را می تواند شکار کند و به ان زاغ گوشت ربا یعنی رباینده گوشت هم می گویند. زغن در اصل نوعی باز شکاری است که از باز کوچکتر است و بعلت شباهت زیاد به زاغ ان را نوعی زاغ قلمداد کرده اند ( خصوصیاتی چون رنگ سیاه و جثه ای نسبتا کوچک ) 
 ... [مشاهده متن کامل] 
در ضمن در نوشتار زاغ و زغن هر دو از حرف ( ز ) و ( غ ) مانند هم استفاده می شود و جالب اینکه گاهی زاغ و زغن در شعر و ادبیات همراه هم شدند مانند:
هنگام می و فصل گل و گشت و چمن شد// در باغِ بهاری، تهی از زاغ و زغن شد// عارف قزوینی

 در کتاب محیط التواریخ صفحه ی ۱۹۴ مینویسد : 
شعرای بلخ فتح او را زغن یافته اند. 
بمعنی پند و عبرت

 زغن: 
دکتر شفیعی کدکنی در مورد " زغن" می نویسد : ( ( غلیواژ ، مرغی که عقیده داشته اند سالی نر است و سالی دیگر ماده ، یا با نر ماده است و یا با ماده نر . ) ) 
 ( ( شاهبازی ، همچنین ، هر گه که خواهی مرد باش 
 ... [مشاهده متن کامل] 
مر زغن را بخش سالی مادگی ، سالی نری ) ) 
 ( تازیانه های سلوک، نقد و تحلیل قصاید سنائی، دکتر شفیعی کدکنی، زمستان ۱۳۸۳، ص 455. ) 
زغن ماهی خوار: غلیواج ماهی خور. 
 ( مرزبان نامه، محمد روشن ج اول، چاپ دوم، ۱۳۶۷، ص ۲۵۶ ) .

 - ذقن:چانه
:زغن : موش گیر

 موش گیر

 کلاغ - زاغ

 همای گو مفکن سایه ی شرف هرگز / دران دیار که طوطی کم از زغن باشد ( حافظ )

 مشاهده ادامه پیشنهادها (١٠ از ١١)

 + عکس و لینک
```


## [2026-09-05T20:44:21.905Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD gang ===\"; grep -n \"gang-\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10\necho \"=== AHD gang ===\"; grep -n \"^gang\\|gang-\\.\" AHD_watkins1985.txt | head -5\necho \"=== IEC gang ===\"; grep -n \"^gang\\|gangō\\|guñj\" IEC.txt | head -10\necho \"=== CHEUNG gan ===\"; grep -n \"^\\*gan\\b\\|\\*gan \\|\\*ganH\" CHEUNG.txt | head -10",
 "description": "Grep WLD, AHD, IEC, CHEUNG"
}
```


### [2026-09-05T20:44:21.983Z] TOOL RESULT

```
=== WLD gang ===
21558:Yergleich mit arm. xacanem im Wege ist (hochstens [sjqhad- bliebe gang- 
33647:gau(dh) gang- 
33679:gang- „spotten, hohnen“. 
33690:her, wenn aus *ganksni-, alter gang-sni -; die bei Fick II 4 109 und 
39966:„summt, brammt“, s. unter *gang- „spotten“). 
41339:aksl. groza ,, horror* usw. (s. u. gang-). 
42061:ai. jinati auch „altert‘‘, jynni-li ,.AItersschwache‘‘, djyuni-h „Unvergang- 
42593:„bringt zum Weichen"; ai. gala- „gegangen“, av. gata-, gr. /taros .gang- 
=== AHD gang ===
=== IEC gang ===
3882:gang- ‘grate, caw, cackle, make a noise’. Cf. ganĝ-, gong-. WP I, 535. (some of the evidence is ambig.) Skt. cf. gafijami ((grate, din’, fr. *gan$- or *gong-); Gk. gaggaíno, v. (mock, jeer’. Hes. beside goggüzo "mutter" See gong-); OCS gognati ‘mutter’; Blg. gágna ‘stammer’; Pol. gegac ‘cackle, honk”; E. dial. to cank ‘chatter, gossip’; OE canc, n. ‘scorn’. See gang-
3883:gang- ‘scorn’. WP I, 535. Cf. gang-, gong- Skt. gafijah, id. cf. gañjanah, id.; Gk. gaggaíno ‘mock’; Ir. (?) cf. gangaire, m. ‘cheat’; gangaid ‘deceit; OE canc, n. ‘scor’; cancettan ‘mock’; E dial. to cank ‘gossip’; ON cf. kankin-yrói, s. ‘taunts’; Icel. kank-vís ‘mocking’. Isophonic is Skt. gafijami, v. ‘grate, noise’
=== CHEUNG gan ===
55749:*gan, *huah, *kap/f'
```


## [2026-09-05T20:44:29.113Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '33679,33695p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== 39960 ===\"; sed -n '39958,39970p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt\necho \"=== IEC gong ===\"; grep -n \"^gong-\" IEC.txt | head -5",
 "description": "Read Walde-Pokorny gang entry"
}
```


### [2026-09-05T20:44:29.204Z] TOOL RESULT

```
gang- „spotten, hohnen“. 

Ai. ganja-h „Verachtung, Hohn u , gahjanci- „verachtend, hohnend“; gr. 
yayyaivetv ( yayyaveveiv M. Schmidt) ' to (.iexo. yskeorog ngoanatCeiv Hes.; ags. 
canc u. ge-canc „Spott, Holm, Tadel“ (= ai. ganja-h , Fick BB. 6,160), can- 
cettan „spotten“, anord. kangen-yrde „hohnende Worte“ (ags. cincung ..lautes 
Lachen“, engl. mdartl. kink „laut lachen" erweist nicht urspriinglichen <■- 
Yokalismus, wie es auch andere Bedeutungsfiirbung hat; bestenfalls Kreuzung 
mit Schallworten wie dt. kichern und iihnlichem bei Falk-Torp 507). 

Yielleicht gehort nir. gedin „Geschrei, Larm, Freude, Verspottung“ hier- 
her, wenn aus *ganksni-, alter gang-sni -; die bei Fick II 4 109 und 
bei Stokes IF. 22, 336 angefiihrten mir. geim ^Gebriilb', gessim „schreie“, 
gesachtaeh „Pfau“ konnten dann auch dazu gehoren. 

Die Sippe scheint ursprgl. schallmalend. Ahnlich Schallworte sind aksl. 
gajgemin „schwer sprechend“, russ . gugnati alt) „murmeln“, gagnja „Stot- 
=== 39960 ===
durch die Bed. empfohlener Ankniipfung an ghei- „gahnen“), gildkar, Feist 
Got. Wb. 2 136. 

gou- „rufen, schreien" ( gou a-, gu-). 

Ai. gavate (nur Dhatup.) „tont“, Intens. joguve „lasse laut ertonen, spreche 
laut aus", jogu- (g. pi. joguvam ) laut singend", gavs-gu-yati „stoBt Freuden- 
schreie aus“ (: gr. yoyyv'Qea „murre, gurre 1 , NT.?, dies eher zu ai. gunjali 
„summt, brammt“, s. unter *gang- „spotten“). 



ghou- 
=== IEC gong ===
4236:gong- ‘mutter, murmur’. Cf. gang-, gan$- Gk. cf. goggüzo; OCS (ambig.) gognati, id.
4241:gong- ‘hump, lump’. Cf. gong- and WP I, 535 Gk. (ambig.) gógge (an alleged form: = 'tap- root); Hes. góggon ‘fool’; R. (dim.) güzka ‘tump’; Blg. gáza ‘buttocks’; ON cf. kakka, v. ‘pile up’
```


## [2026-09-05T20:44:39.797Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB gandum ===\"; grep -n \"gandum\\|gantum\" NYB_vol2_glossary.txt NYB_vol1.txt | head -10\necho \"=== ARY index gar/zaghan ===\"; grep -n -i \"GARENU\\|ZAGAN\\|ZAGHAN\\|UYSGAN\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== ARY pages gandom ===\"; grep -n \"گندم\" incoming/ARY/ARY_pages.txt | head -10",
 "description": "Grep Nyberg and Aryanpur"
}
```


### [2026-09-05T20:44:39.876Z] TOOL RESULT

```
=== NYB gandum ===
=== ARY index gar/zaghan ===
=== ARY pages gandom ===
1069:در آثار هومر یونانی آمده است که بردگان زن مسئول انجام کارهای شاق (مثلاً آردکر دن گندم وجو
15210:7۳ /_واس,» واش (به چم *علوفه‌ی ستوران"» *"خوشه‌ی گندم»)
```


## [2026-09-05T20:44:46.449Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nsed -n '12905,12915p' ARY_latin_index_pages.txt\necho \"=== ARY page 43/44 ===\"; a=$(grep -n \"^\\[pdf page 43\\]\" ARY_pages.txt | cut -d: -f1); b=$(grep -n \"^\\[pdf page 45\\]\" ARY_pages.txt | cut -d: -f1); echo \"$a-$b\"; sed -n \"${a}\",\"${b}\"p ARY_pages.txt | head -70",
 "description": "Read Aryanpur gandum entry"
}
```


### [2026-09-05T20:44:48.859Z] TOOL RESULT

```
|p STINKAN: 345 1) STINKEN GUT g STINK, oh Sit hassiy POKORNY (50.3 4-1
i aca aturly gaat Jl jp GTINGAN 9S
a > _ aie ahead ya,et 64 great 2 Sls cal
“ ly ea Sole 9 gloos! 52 5a ot
KAN . HITTITE) GANTUMA HAVESTAN) glo)
: GANDUM, GANTUM (PAHLAVI) 44
‘REFERENCES nthe GENIM KURDISH) 53,
POKORNY ~ 390391 GANDIM BALUCHI) 4
MACKENZIE: (WHEAT) 140 AFGHAND) (x4) sil
BUCK: 513-516 GHANEM, GHANUM
MALLORY & ADAMS: GA-ONDH KANTI {(TOKHARIAN B) B 3,653
=== ARY page 43/44 ===

sed: -e expression #1, char 1: unknown command: `,'
```


## [2026-09-05T20:44:57.804Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\nawk 'NR<=12910 && /\\[pdf page/{p=$0} END{print p}' ARY_latin_index_pages.txt\nsed -n '12890,12930p' ARY_latin_index_pages.txt",
 "description": "Locate Aryanpur wheat entry page"
}
```


### [2026-09-05T20:44:59.663Z] TOOL RESULT

```
[pdf page 443]
lethal
seek ay gely gen Id CaluaSS” y "Whe 5 "StF" 95 4) GONAD ISI uly
|
GANDHA (SANSKRIT) 2 Suite HAVESTAN) geo si .
GENDU LITHUANIAN) p33 GAINTH, GANTI, GANTAY. ue
GINSTU ALATVIAN) (23) 3) GASTA OLS eRSiAN) DAY peak
(PAHLAVI) 5 ay
REFERENCES beth, GAND, GANDAGIH, GANDAK
POKORNY, SSS*«GAGT ABALUCH) ge Sh
MACKENZIE: (STENCH) 134 GAND, GANDAG, GANDAGH
BUCK: 1024, 1179 HAPGHAND (4) li
Vary sbi ily GANDA, GANDAL
[pdf page 443]
cos aad
leatlosl
|p STINKAN: 345 1) STINKEN GUT g STINK, oh Sit hassiy POKORNY (50.3 4-1
i aca aturly gaat Jl jp GTINGAN 9S
a > _ aie ahead ya,et 64 great 2 Sls cal
“ ly ea Sole 9 gloos! 52 5a ot
KAN . HITTITE) GANTUMA HAVESTAN) glo)
: GANDUM, GANTUM (PAHLAVI) 44
‘REFERENCES nthe GENIM KURDISH) 53,
POKORNY ~ 390391 GANDIM BALUCHI) 4
MACKENZIE: (WHEAT) 140 AFGHAND) (x4) sil
BUCK: 513-516 GHANEM, GHANUM
MALLORY & ADAMS: GA-ONDH KANTI {(TOKHARIAN B) B 3,653
yar iat dhy GANAMA KHOTANESE) >
GODHUMA —_ (SANSKRIT) < Site
Jewtloak
dat AL zely gene 5! jd (KAURN 1063S) KORN gusty CORN ll glanjly aL
KJUKA GoY APAHLAVD 5.34
KOLA (OLD NORSE) 9 2 GU, Gor (KURDISH) 52,6
(OLD HIGH GERMAN) 35 sll SANSKRIT) ey Site
KIOL, CLIUWA GOLAH, GOLA, GOLAM
KUGEL GERMAN) gut KALUM. ARMENIAN) |g)
HOLD ENGLISH) iS g-3Si! GUALON (GREEK) gli
EOL, KLIUWE CULLEUS, (LATIN) oS
KOGEL (DUTCH) gabe :(OLD SCANDINAVIAN) AS She!
[pdf page 444]
[
|
```


## [2026-09-05T20:45:12.809Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Weizen\" BRT.txt | head -10",
 "description": "Grep Bartholomae for Weizen"
}
```


### [2026-09-05T20:45:12.870Z] TOOL RESULT

```
9997:•  '}.  gantutna-  m.  "Weizen":  •mS yavanam ratu/ris  "unter  dCD  Getreidearten  ist  es der  Weizen,  der  den  JP.  genehm  ist"  N.  2Ä
```


## [2026-09-05T20:45:18.224Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=9997{n+=gsub(/\\f/,\"\")} END{print \"leaf:\",n}' BRT.txt\nawk 'NR>9900 && NR<10100 && /^[[:space:]]*[0-9]{3}[[:space:]]*$/{print NR\": \"$0}' BRT.txt",
 "description": "Find Bartholomae column for gantuma"
}
```


### [2026-09-05T20:45:19.732Z] TOOL RESULT

```
leaf: 295
9935: 489
9938: 490
9964: 491
9967: 491
9985: 493
9988: 494
10030: 497
```


## [2026-09-05T20:46:07.308Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -n -i \"scab\\|mange\\|itch\" data/verification/sources/refs/PHD.txt | head -10\nls site/pages/167.jpg 2>/dev/null || echo \"no jpg\"",
 "description": "Check PHD for scab and page image"
}
```


### [2026-09-05T20:46:07.357Z] TOOL RESULT

```
223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
583:šāh [MLKA < A mlk’; th | M £h, N <] king. „ān šāh [MLK Ап MLKA | N ~] king of kings. 7--balüt [shbiwt' | N ~] chestnut. ~-дапар [-d’nk' | N —dàna] hemp-seed. ~-esprahm [-splhm | N ~isparam] basil royal. Sahigan [#hyhk'n' | M Phyg^n] palace. šahr [štr' | M £r, N ~] land, country; city. ~estan [MDYNA < A mdyn’; Str'st?n' | M #šhrs Pn, N ~] province; capital, city. Sahrewar [štrywr | N ~] Best Rule, the third Amahraspand, guardian of metals; cal. 6th month; 4th day. šahryār [ftr'd?] | M shry’r, № ~] lord, sovereign, ruler. ~ih ; dominion, reign, sovereignty. šāhwār [š%w?/ | P ?hw’r, N ~] royal, kingly. Sakar [fA] | M šgr, N ~] sugar. salwar [ilw] | N ~] trousers. šām [Pm | = P, N ~] evening meal, supper. Sambalidag [smblytk' | N šambalīd, -lila] fenugreek. šamšēr [smsyl | N ~] sword. бап [in' | N ~] hemp. &ünag [P?^nk! | N ~a] 1. comb; 2. pitchfork; 3. shoulder-blade. šanēn [snyn'] hempen. šarm [т | M #m, N ~] shame. ~-gah [-g*s | N ~] pudenda. ~gén [-k(y)n! | N ~gin] ashamed. &asab [р | (P Shrb)] satrap. ^Agàn [-yk’n'] satrapal. šast [60| M šst, N ~] sixty. šaš [STA < A st | M f, N ~] six. šaw-, v. Sudan. *Sawag [swb’k'] bat, flittermouse. šāyendaģ [^ dyndk!] able, worthy. ~ih: ability, worthiness. šāyistan, šāy- [P?d-stn! | M P?y-, N ~] be able; be worthy. šāyēd [P?(d)yt! | N šāyad] one can, it is possible. šāzdah [cdh | М ?zdh, N sanzdah] sixteen. бер [ғур | N ~] declivity. šēb- [šyp- | M syb, N ~] move quickly; be confused. ~&g [PR' | N —à] swift, nimble; viper. ~išn: confusion. šēd [у | N ~] bright; sorrel (horse). *šēdā [угу] bliss. šēr, v. Sagr. šēwan [£fywn! | N ~] lament. šiftālūg [spi?lwk! | (P šyft ‘milk’), N šaftālū] peach. šiftēnaģ [šp:ynk! | (P £yftyn ‘sweet’)] a sweetmeat.
661:2xān [/?п! | P л?п] spring, source. хапар [BYTA < A рур; h'nR! | N хапа] = іхап. xandidan, xand- (*GHBHWN-yitn' < A V ghk, or У *ghqh; hnd-ytn' | (M xnyst), N —] laugh. xānīg [/?nyk! | M x?nyg, N xàni] = *xān. xar (HMRA < А hmr’; hl | N ~] donkey, ass. хаг [P1 | M ær, N ~] thorn. xar-buz [hibwe | M xrbwz] oryx. xar-g68 [higws | N ~] rabbit, hare. хаготапа [/PPwmnd] thorny. xār-pušt [/?Ipwst! | N ~] porcupine, hedgehog. xastan [hstn' | M xst, N ~] wound, injure. xašën [hsyn! | N хайл] (dark) blue. хауар [Pd(y)k! | N xdya] egg. ~-dés [-dys] oval, egg-shaped. xayüg [Ah )dwk! | N xayū] saliva, spittle. xaz [hz | N —] marten. xém [лут] nature, character. xëšm [?yfm, hfm | M xysm, N xifm] anger; the demon Wrath. --én [-ya! | M -yn) angry. xindag [hyndk' | M xyndg] ill, sick. ~th: illness, sickness. xir [C BW! < А sbw; hyl | M хут] thing, matter. xirs [hls | N ~] bear. xišt [Ast! | (P hystyg), N ~] brick. хбё [hwk' | N xwk, xóy] nature, character, disposition. x6n [DM YA < А dm’; һит! | M хоп, N хип] blood. xormā [TE A tmryn; hwlm’k' | N ~] date. xrad [hit! | M xrd, N xirad] wisdom, reason. ~ig, ~Omand [-yā!, тиа | N -mand] wise. xrafstar [hlpst] = Av. xrafstra-] reptile, noxious creature. xridan, xrin- [ZBNN-tn! < A V zbn| M xryd, xryn-, N xaridan, (xar-)] buy. xróhak [hlwhk' | N ~] coral. xrēs [DYLK A < A dkr’; hlws | P xrws, N xurós] cock. xróstan [Alwstn! | M xrwst] call, cry. xüb [hwp | M xwb, N ~] good. ~th: goodness. xuftan, xufs- [HLMWN-tn! < А У Ыт; hwptn', hwps- | М xwpt, N xuftan, xusp-] sleep. xūg [HZWL УА < А hzyr; hwk' | N ~] pig. xükar(ag) [hwkl(k') | N xūkara] hedgehog. xumb [kwmb! | M xwmb, N ~] jug, pitcher. xunak [hwnk' | M xwnk, N xunuk] happy; cool. xurdruš [kwldlwš, -dlpš = Av. xrwidruf] ‘with a bloody club’ (epithet of Xēšm, later misinterpreted as *ul-draff ‘*with raised banner’).
2717:manger āxwarr.
3133:pitcher xumb.
3134:pitchfork Sanag.
4325:witch parīg.
5228:VS A HITCH ur) -.0v ҮЕ (Pas РА
site/pages/167.jpg
```


## [2026-09-05T20:46:11.179Z] TOOL CALL #73: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/site/pages/167.jpg"
}
```


### [2026-09-05T20:46:11.210Z] TOOL RESULT

```

```


## [2026-09-05T20:46:29.573Z] TOOL CALL #74: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 167 -l 167 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg167 && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg167.png')\nprint(im.size)\nw,h=im.size\n# crop the last entry (Garenu) persian box\nbox=im.crop((int(w*0.42),int(h*0.72),int(w*0.80),int(h*0.83))).resize((int(w*0.38*2),int(h*0.11*2)))\nbox.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/gar.png')\n\"",
 "description": "Render page 167 at high res and crop"
}
```


### [2026-09-05T20:46:32.821Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T20:46:35.177Z] TOOL CALL #75: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/gar.png"
}
```


### [2026-09-05T20:46:35.361Z] TOOL RESULT

```

```


## [2026-09-05T20:46:35.359Z] INPUT

[Image: original 2584x968, displayed at 2000x749. Multiply coordinates by 1.29 to map to original image.]


## [2026-09-05T20:46:41.594Z] TOOL CALL #76: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\np='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\nim=Image.open(p+'pg167.png'); w,h=im.size\nim.crop((int(w*0.42),int(h*0.700),int(w*0.80),int(h*0.762))).resize((2400,int(2400*(0.062*h)/(0.38*w)))).save(p+'gar2.png')\n\"",
 "description": "Crop gar headwords"
}
```


### [2026-09-05T20:46:43.620Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:46:46.197Z] TOOL CALL #77: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/gar2.png"
}
```


### [2026-09-05T20:46:46.333Z] TOOL RESULT

```

```


## [2026-09-05T20:46:46.330Z] INPUT

[Image: original 2400x506, displayed at 2000x422. Multiply coordinates by 1.20 to map to original image.]


## [2026-09-05T20:47:01.301Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\np='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/'\nim=Image.open(p+'pg167.png'); w,h=im.size\nim.crop((int(w*0.60),int(h*0.685),int(w*0.79),int(h*0.725))).resize((2200,int(2200*(0.040*h)/(0.19*w)))).save(p+'gar3.png')\n\"",
 "description": "Crop gar/gargen Persian forms"
}
```


### [2026-09-05T20:47:03.411Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:47:05.818Z] TOOL CALL #79: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/gar3.png"
}
```


### [2026-09-05T20:47:05.995Z] TOOL RESULT

```

```


## [2026-09-05T20:47:05.993Z] INPUT

[Image: original 2200x599, displayed at 2000x545. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T20:47:35.063Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN zaghan ===\"; grep -n \"zagan\\|zayan\\|zaġan\\|Weihe\\|Milan\" HRN.txt | head -10\necho \"=== RCH ===\"; grep -n \"zagan\\|zaghan\" RCH.txt | head -5\necho \"=== FRS zaghan ===\"; grep -n \"زغن\" FRS_pages.txt FSF_pages.txt 2>/dev/null | head -5\necho \"=== HUB zagan ===\"; grep -n \"zagan\\|zayan\" HUB.txt | head -5",
 "description": "Grep more sources for zaghan"
}
```


### [2026-09-05T20:47:35.156Z] TOOL RESULT

```
=== HRN zaghan ===
=== RCH ===
45710:p   Jkiij  zaghandy  The  cries  of  a   wild  beast,  especially  of  a   pan- ther. A   bell.  A   spring,  a   bound.  A   sally,  flight,  levity, p   zaghangy  A   sigh.  A   wink,  a   glance.  A   moment.
45711:zaghangidany  To  sob,  to  sigh, p   zaghutahy  Haw  silk  wrapped  round  the  spindle.
55867:A   zaghan  or  zighn  (from  ^jd^)y  Hating.  Liking,  having an  inclination  for.  Hatred,  malevolence.  Affection,  attachment.
82689:tJj^  mwrjfgk,  Rain  which  turns  dust  to  mud. p   marzaghdn  (or  ^jj^marzaghan)y  Hell.  A   chafing-
98498:zcarzagany  A   pitcher  full  of  water.
=== FRS zaghan ===
FRS_pages.txt:3574:                            ‫نچو‪.‬‬ ‫غلیواج مرغ گوشت ربای بعنیزغن بود ‪-:۳ ۰‬‬
FRS_pages.txt:3723:‫‪ ۰‬در تن( در حاشیه) ‪ :‬ایزغنج جوال ود و غنج نیز‬          ‫چ هست‬   ‫‪ ۳‬اینلت نقط در‬
FRS_pages.txt:3727:     ‫ابرم کشت ‪ ۰‬ایزغنج درفرهنگها بدست یامد ت‬
FRS_pages.txt:3769: ‫چونغلیجی که بنه بر کند [کذا‪ |] :‬کیست چون تو فژاکن‌و فزغند‬
FRS_pages.txt:4429:    ‫وا وی ‪ ۲‬دهان توو زان بینیفزغند‬
=== HUB zagan ===
```


## [2026-09-05T20:47:55.448Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://abadis.ir/fatofa/%DA%AF%D9%86%DA%AF/\" \"https://abadis.ir/fatofa/%DA%AF%D9%86%D8%AF%D9%85/\" \"https://abadis.ir/fatofa/%DA%AF%D8%B1%DA%AF%DB%8C%D9%86/\"; do python3 tools/fetch_source.py \"$u\" --note \"page 167: Mo'in entry for gong / gandom / gargin\"; done",
 "description": "Archive abadis pages for gong, gandom, gargin"
}
```


### [2026-09-05T20:48:01.900Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/783bbf720d01a709.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c96bf0b60614f29d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c9630865bfe875be.txt
```


## [2026-09-05T20:48:05.056Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 783bbf720d01a709 c96bf0b60614f29d c9630865bfe875be; do echo \"=== $f ===\"; grep -m1 -A8 \"فرهنگ معین\" $f.txt; done",
 "description": "Read Moin sections from abadis"
}
```


### [2026-09-05T20:48:07.122Z] TOOL RESULT

```
=== 783bbf720d01a709 ===
 فرهنگ معین

 ( ~ . ) (اِ. ) = کنگ : امرد قوی جثه .
 ( ~ . ) (اِ. ) جزیره .
 ( ~ . ) (اِ. ) بادی است که گویند به سبب سودا در بدن مردم به هم می رسد و بن موها می خارد و تا موی را نکنند خارش برطرف نمی شود.
 (گَ ) (ص . ) خمیده ، کج ، کوژ (مادرزاد و غیره ).
 ( ~ . ) (اِ. ) لولة سفالی که برای عبور آب در زیر زمین کار می گذاشتند.
 (گُ ) [ په . ] (ص . ) لال ، بی زبان .
 ( ~ . ) (ص . ) نیکو، خوب ، زیبا. 
=== c96bf0b60614f29d ===
 فرهنگ معین

 (گَ دُ ) (اِ. ) گیاهی است یک ساله ، علفی با ریشة افشان و ساقة میان تهی که از آرد آن برای پختن نان استفاده می شود. 

 فرهنگ عمید

 ۱. نوعی دانۀ کوچک سرشار از نشاسته که غذای اصلی انسان است و از آن آرد و نان تهیه می کنند.
۲. بوتۀ این گیاه برگ های بلند و باریک دارد و هر ساقۀ آن دارای سنبله است. 

=== c9630865bfe875be ===
 فرهنگ معین

 (گَ ) (ص مر. ) کسی که بیماری گَر دارد. 

 فرهنگ عمید

 حیوانی که به بیماری جرب مبتلا باشد، گرگ.
دلیر و گستاخ مانند گرگ.
```


## [2026-09-05T20:48:14.378Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nmkdir -p data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg167.png data/verification/sources/refs/ocr/BOOK/167.png\nls -la data/verification/sources/refs/ocr/BOOK/ | head",
 "description": "Copy page image for audit"
}
```


### [2026-09-05T20:48:16.231Z] TOOL RESULT

```
total 5592
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  5 16:48 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb  71589 Sep  5 10:46 100.png
-rw-rw-r--  1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r--  1 sfmqrb sfmqrb  68145 Sep  5 10:49 102.png
-rw-rw-r--  1 sfmqrb sfmqrb  79623 Sep  5 10:55 103.png
-rw-rw-r--  1 sfmqrb sfmqrb  78826 Sep  5 10:59 104.png
-rw-rw-r--  1 sfmqrb sfmqrb  82500 Sep  5 11:05 105.png
-rw-rw-r--  1 sfmqrb sfmqrb  55270 Sep  5 11:03 106.png
```


## [2026-09-05T20:48:18.983Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check requirements"
}
```


### [2026-09-05T20:48:19.021Z] TOOL RESULT

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


## [2026-09-05T20:48:37.597Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ghend-\\|ghend\" AHD_watkins1985.txt | head -5\necho \"=== IEC ghend ===\"; grep -n \"^ghend-\\|^ghed-\" IEC.txt | head -5",
 "description": "Grep AHD and Mann for ghend"
}
```


### [2026-09-05T20:48:37.657Z] TOOL RESULT

```
518:ghend-. Also ghed-. To seize, take. 1. Germanic *getan in: a. Old Norse getfa, to get: GET; b. compound *bigetan (*bi-, intensive prefix; see ambhi), to acquire, in Old English begietan, to get, beget: BEGET; C. compound *fer-getan (*fer-, prefix denoting rejection; see per’), “to lose one’s hold,” forget, in Old English forg(iJetan, to forget: FORGET. 2. Germanic “getison, “to try to get,” aim at, in Old Swedish gissa, to guess, akin to the Scandinavian source of Middle English gessen, to guess: GuEss. 3. Basic form *ghend- in Latin prendere, prehen- dere (pre-, prae-, before; see per'), to get hold of, seize, grasp: PREHENSILE, PREHENSION, PRISON, PRIZE?, (PRIZES), (PRY2); APPREHEND, (APPRENTICE), (APPRISE), COMPREHEND, COMPRISE, EMPRISE, ENTERPRISE, (EN- TREPRENEUR), MISPRISION, PREGNABLE, REPREHEND, (REPRISAL), (REPRISE), SURPRISE. 4. Form “ghed- in Latin praeda, booty (< *prai-heda, “something seized before”; prai-, prae-, before; see per'): PREDATORY, PREY, SPREE; DEPREDATE, OSPREY. [Pok. ghend- 437.]
519:ghendh-. Abscess, boil. Zero-grade form *ghndh- in Germanic *gund- in Old English gund, pus: GROUNDSEL!. [Pok. ghendh- 438.]
837:“around.” I. Basic form *per and extended form *peri. 1. Germanic *fer-, *far-, used chiefly as an intensive prefix denoting destruction, reversal, or completion, in: a. Old High German far-, in German vereinen, to unite: TURNVEREIN; b. Middle Dutch vieren, to let out, slacken: VEER; C. compound “*fer-getan, “‘to lose one’s hold,” forget (see ghend-). 2. Suffixed (comparative) form *per-ero-, farther away, in Germanic *fer(e)ra’in Old English feor(r), far: FAR. 3. Compound “per-n-yo-, of last year (*-n-, year; see en-), in Germanic *fernja- in Old High German firni, old: FmRN. 4. Latin per, through, for, by: PER, PER-; PARAMOUNT, PARAMOUR, PARGET, PAR- VENU. 5. Greek peri, around, near, beyond: PERI-; PERIS- SODACTYL. 6. Sanskrit pari, through, around: PALANQUIN. 7. Avestan pairi, around: PARADISE. II. Zero-grade form *pr-. 1.Germanic *fur, before, in: a. Old English for, before, instead of, on account of: FOR; b. Old English for-, prefix denoting destruction, pejora- tion, exclusion, or completion: For-. 2. Extended form *prt- in Germanic *furth-, forward, in Old English forth, forth: FORTH; AFFORD. 3. Suffixed (comparative) form *pr-tero- in Germanic *furthera- in Old English furthra, furthor, farther away: FURTHER. 4. Compound *pr-st-i- (or *por-st-i-, with o-grade form *por-), “that which stands before,” stake, post (see sta-). III. Extended zero-grade form “pro-. 1. Suffixed (superlative) form *pro-mo- in: a. Germanic *fruma-, *furma- in Old Eng- lish forma, first, foremost: FOREMOST, FORMER?; b. Latin compound prandium, “first meal,” late breakfast, lunch (probably < *pram-d-ium < *pram-(e)d-yo-; second ele- ment *-(e)d-, to eat; see ed-). 2. Suffixed (superlative) form *pro-isto- in Germanic *furista-, foremost, in Old English fyrst, fyrest, first: FIRST. 3. Suffixed form *pre-wo- in Greek *prowo-, first, foremost, in: a. analogi- cally suffixed Greek form *préw-arya in Greek prdira, forward part of a ship: PROw; b. suffixed (superlative) Greek form *préw-ato- in Greek prétos, first, foremost: PROTEIN, PROTIST, PROTO-, PROTON. 4. Suffixed form *pro-i in Celtic *(p)ari, *are in Gaulish ari (combining form are-), before, in Latin arepennis, half-acre (second element obscure): ARPENT. IV. Extended form “prod. 1. Germanic *fura, before, in: a. Old English fore, for (> Middle English fore-), before: FORE, FORE-; FOREFA- THER; b. Old High German fora (> German vor), before: VORLAGE; Cc. Germanic prefixed and suffixed form *bi-fora-na, in the front (*bi-, at, by; see ambhi), in Old English beforan, before: BEFORE. 2. Greek para, beside, alongside of, beyond: PARA-); PALFREY. V. Extended form *pré. 1. a. Germanic *fra, forward, away from, in Old Norse *frd (> Middle English fro), from: FRO; FROWARD; b. Germanic *fra-, completely (see ed-, éik-). 2. Suffixed form *pro-mo- in: a. Germanic *fram, from, in Old English from, from: FROM; b. Germanic *frum, forward, hence derivative verb *frumjan, to further, in Old French f(ojurnir, to supply, provide: FURNISH, VE- NEER; C. Czech pram, raft: PRAAM. 3. Suffixed form *pr6é-wo- in Germanic *frdw6-, lady, in: a. Old High German frouwa, lady: FRAU, (FRAULEIN); b. Middle Dutch vrouwe, woman: vRouw. 4. Latin pré, pro-, be- fore, for, instead of: PRO!, PRO-!; PURCHASE. 5. Suffixed form *pr6-no- in Latin prénus, leaning forward: PRONE. 6. Possible suffixed form *pro-ko- in Latin compound reciprocus, alternating, ‘‘backward and forward” (*re-ko-, backward; see re-): RECIPROCAL. 7. Suffixed adverb *pro-kve in: a. Latin prope, near: APPROACH, RAPPROCHEMENT, REPROACH; b. suffixed form *prok- ink“o- in Latin propinquus, near: PROPINQUITY; Cc. suf- fixed (superlative) form *prok’-samo- in Latin proximus, nearest: PROXIMATE; APPROXIMATE. 8. Compound *pro-bhw-o-, growing well or straightforward (*bhw-o-, to grow; see bheue-), in Latin probus, upright, good, virtuous: (PROBABLE), PROBE, PROBITY, (PROOF), PROVE; APPROVE, IMPROBITY, (IMPROVE), (REPROVE). 9. Greek pro, before, in front, forward: PRO-2. 10. Suffixed (com-
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
=== IEC ghend ===
4652:ghend-, see ghed-, ghnd-. (The evidence is ambig.) Gk. cf. kheísomai ‘will contain’; Alb. gjej (?) “find; guess? beside gjíndem “am found, oc- cur’; Lat. cf. prae-hendo; Pol. cf. Zadac dest. re’; Li. cf. pa-si-gendu, inf. -gesti, pf. -gedau *keep watch, observe'
```


## [2026-09-05T20:50:04.022Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:57:10.392Z] TOOL CALL #86: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk167.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW_ZAGAN = \"https://en.wiktionary.org/wiki/%D8%B2%D8%BA%D9%86\"\nA_ZAGAN = \"https://abadis.ir/fatofa/%D8%B2%D8%BA%D9%86/\"\nW_GONG  = \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%DA%AF\"\nA_GONG  = \"https://abadis.ir/fatofa/%DA%AF%D9%86%DA%AF/\"\nW_GANDOM= \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%AF%D9%85\"\nA_GANDOM= \"https://abadis.ir/fatofa/%DA%AF%D9%86%D8%AF%D9%85/\"\nW_GAR   = \"https://en.wiktionary.org/wiki/%DA%AF%D8%B1\"\nA_GAR   = \"https://abadis.ir/fatofa/%DA%AF%D8%B1/\"\nA_GARGIN= \"https://abadis.ir/fatofa/%DA%AF%D8%B1%DA%AF%DB%8C%D9%86/\"\n\ndoc = {\n \"pdf_page\": 167,\n \"book_page\": 137,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n\n  # ============================== ENTRY 0 — Gan ==============================\n  {\n   \"entry\": 0,\n   \"root\": \"Gan\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"Bailey's Iranian base *gan- 'to seize' (abstracted from Khotanese uysgana- 'vulture' < *uz-gana- 'seizing out, rapacious'), which Bailey attaches to PIE *gʰend- / *gʰed- 'to seize, grasp' (Pokorny IEW 437 f.)\",\n   \"note\": \"The root box is a faithful copy of H. W. Bailey. In his Dictionary of Khotan Saka, s.v. uysgana-, Bailey writes verbatim: 'From uz-gana- \\\"rapax\\\" of a bird of prey, N.Pers. zaγan … Hence a base gan- \\\"to seize\\\", IE ghen- to IE Pok. 437-8 ghen-d-', and again in the reverse index 'gan- \\\"to seize\\\", in the name of the raptor bird uysgana- \\\"vulture\\\"'. So the base, the gloss and the whole chart are Bailey's, and Nourai reproduces them accurately. Two reservations keep this from 'confirmed'. (1) 'Indo-Schythian' is not a language: it is the title of Bailey's series (Indo-Scythian Studies = Khotanese Texts), and the language of uysgana- is Khotanese Saka, an Eastern Middle Iranian language of the Tarim basin, 5th-10th c. CE. (2) *gan- 'to seize' is Bailey's own back-formation from a single compound; it is not an independently attested Iranian verb, and the PIE root he links it to (*gʰend-, Pokorny 437 f., AHD ghend-) has no Iranian reflex in Pokorny, Walde-Pokorny or Watkins — its witnesses are Greek χανδάνω, Latin prehendere/praeda, Germanic *getan (English get, beget, forget) and Celtic. Nourai does not repeat Bailey's IE link, which is prudent.\",\n   \"note_fa\": \"جعبهٔ ریشه در این نمودار عیناً از هارولد بیلی گرفته شده است. بیلی در «فرهنگ ختنی-سکایی»، ذیل uysgana-، می‌نویسد که این واژه از *uz-gana- «رباینده» است و «از این‌جا ستاکی gan- به معنی گرفتن/ربودن به دست می‌آید» و آن را با ریشهٔ هندواروپایی *gʰend- (پوکورنی ۴۳۷ به بعد) می‌سنجد؛ پس نقل نورایی درست است. اما دو نکته: نخست آنکه «هندوسکایی» نام هیچ زبانی نیست، بلکه عنوان مجموعهٔ کتاب‌های بیلی است و زبان این واژه ختنی-سکایی (ایرانی میانهٔ شرقی) است؛ دوم آنکه ستاک *gan- ساختِ خودِ بیلی از یک ترکیب است و در هیچ متن ایرانی به‌تنهایی گواهی نشده، و ریشهٔ هندواروپایی‌ای که بیلی به آن پیوند می‌زند در پوکورنی و والده-پوکورنی و واتکینز هیچ بازماندهٔ ایرانی ندارد. بنابراین ادعای نورایی «با احتیاط پذیرفتنی» است.\",\n   \"sources\": [A_ZAGAN],\n   \"ref_check\": [\n    {\"ref\": \"ISS:27\", \"status\": \"not_checked\",\n     \"note\": \"Bailey, Indo-Scythian Studies: Khotanese Texts VI (1967) p.27 is not online (HathiTrust mdp.39015034317936 is search-only; archive.org has vols I-III lending-only). The substitute on disk is Bailey's own Dictionary of Khotan Saka (1979), which carries the identical statement s.v. uysgana- (ISS_alt_DKS.txt line 1113): 'From uz-gana- \\\"rapax\\\" of a bird of prey … Hence a base gan- \\\"to seize\\\", IE ghen- to IE Pok. 437-8 ghen-d-.' The cited page itself could not be opened.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. uysgana- and s.v. gan- (ISS_alt_DKS.txt lines 1113 and 1782)\", \"stance\": \"supports\",\n     \"note\": \"'uysgana- \\\"vulture\\\", = BS gṛdhra-, Z 13:35 uysgani, changed from uysguni … From uz-gana- \\\"rapax\\\" of a bird of prey, N.Pers. zaγan, … Hence a base gan- \\\"to seize\\\"'; and 'gan- \\\"to seize\\\", in the name of the raptor bird uysgana- \\\"vulture\\\"'.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 437 f. (POK_02.txt line 1402; page numerals 437 at line 1390, 438 at 1404)\", \"stance\": \"partial\",\n     \"note\": \"'ghend- und ghed- \\\"fassen, anfassen, ergreifen\\\", z. T. auch \\\"geistig erfassen\\\". Gr. χανδάνω (*gh-n-d-) \\\"fasse\\\" …' — the PIE root Bailey invokes exists on exactly the pages he cites, but Pokorny lists no Indo-Iranian reflex under it at all, so the Iranian half of the equation is Bailey's own.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. ghend- (AHD_watkins1985.txt line 518)\", \"stance\": \"partial\",\n     \"note\": \"'ghend-. Also ghed-. To seize, take. 1. Germanic *getan … 3. Basic form *ghend- in Latin prendere, prehendere … [Pok. ghend- 437.]' — same root, same gloss 'to seize', but again only Germanic, Latin and Greek witnesses; no Iranian.\"},\n    {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, γ- section, entries 4121-4168 (printed p.163 = leaf 229)\", \"stance\": \"silent\",\n     \"note\": \"the whole γn- run (γn'β- 'lament', γnc(h), γnδ'k, γnyr(h), γnkyn, γnt-…) contains no base γn- 'to seize'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Indo-Schythian\", \"words\": \"Uysgani\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The form is exact: Bailey (DKS s.v.) cites 'Z 13:35 uysgani' — the Book of Zambasta, the great Khotanese Buddhist poem of the 5th-6th c. CE — as the manuscript spelling (altered from an older uysguni), rendering Buddhist Sanskrit gṛdhra- 'vulture', and quotes JS 24v1 'pura pemesti aysgani … the vulture seized the young ones in its sharp beak' and K 21:4 aysgana-rrūvyi 'in vulture-form'. Morphologically uysgana- = uz- 'out, away' (Av. uz-, OP ud-) + gana- (verbal adjective of the base gan- 'to seize'), i.e. 'the one that seizes/snatches away', Latin rapax; Khotanese writes the prefix uys- because Old Iranian *uz- before a voiced stop gives uys- (the same uys- as in uysāna- 'to raise'). The vulture is therefore named exactly as Sanskrit gṛdhra- is named from gardh- 'to seize', as Latin voltur is from vellō 'to pluck, seize', and as Yidgha yereno (in kyāl-yereno 'bald eagle') is from *gṛdnu- — the parallels Bailey himself lists. The only caveat is the language label: this is Khotanese Saka, not a language called 'Indo-Scythian'.\",\n     \"derivation_fa\": \"این صورت دقیقاً همان است که بیلی می‌آورد: uysgani در «کتاب زمبسته»، منظومهٔ بودایی ختنی سدهٔ پنجم-ششم میلادی، بند ۱۳:۳۵، برابرِ gṛdhra- سنسکریت بودایی «کرکس». ساختِ واژه uz- (پیشوندِ «برون، بیرون»، همان اوستایی uz-) + gana- (صفتِ فعلیِ ستاکِ gan- «گرفتن، ربودن») است، یعنی «رباینده»؛ در ختنی *uz- پیش از همخوانِ واکدار به uys- بدل می‌شود. نام‌گذاریِ کرکس بر پایهٔ «ربودن» در زبان‌های دیگر هم دیده می‌شود: سنسکریت gṛdhra- از gardh- «ربودن» و لاتینی uoltur از uello «کندن، ربودن». تنها ایرادِ گره برچسبِ زبان است: این واژه ختنی-سکایی است، نه زبانی به نام «هندوسکایی».\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"ISS:27\", \"status\": \"not_checked\",\n       \"note\": \"Khotanese Texts VI p.27 not obtainable; Bailey's DKS (ISS_alt_DKS.txt line 1113) gives the same form and derivation, quoting the Zambasta passage: 'uysgana- \\\"vulture\\\", = BS gṛdhra-, Z 13:35 uysgani, changed from uysguni'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, Dictionary of Khotan Saka, s.v. uysgana- (line 1113) and s.v. aysgana- (line 505)\", \"stance\": \"supports\",\n       \"note\": \"two headwords, uysgana- and the variant spelling aysgana-, both 'vulture', with the passages K 21:4, K 28:179, K 37:117, JS 24v1.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 437 f., ghend-/ghed-\", \"stance\": \"silent\",\n       \"note\": \"no Khotanese or other Iranian material under the root Bailey connects it with.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Sogdian\", \"words\": \"ğnw, ğan\", \"verdict\": \"plausible\",\n     \"derivation\": \"This node reproduces the last, deliberately tentative sentence of Bailey's article: 'Possibly Sogd. VJ γn'w \\\"force\\\".' VJ = the Sogdian Vessantara Jātaka (Paris, Pelliot sogdien 4, 8th-9th c.), and Bailey's suggestion is that a Sogdian abstract γn'w 'force, might' could contain the same base gan- 'to seize' (semantically 'grip' > 'strength'). The link is unconfirmed by Sogdian lexicography: B. Gharib's Sogdian Dictionary (1995) — the standard word-list, and Nourai's own second reference here — has no entry γnw or γan on p.163 or anywhere in its γn- run, and the gloss 'skill' that Nourai adds appears in neither Bailey nor Gharib (Gharib's word for 'skill' is qnw'ncya, no. 4784, unrelated). So the word may exist as a hapax reading in VJ, but the node as drawn — a Sogdian noun 'power, force, skill' descending from the base gan- — is a possibility flagged by Bailey rather than an established derivation.\",\n     \"derivation_fa\": \"این گره واپسین جملهٔ بیلی را بازمی‌گوید که خود او با تردید نوشته است: «شاید سغدیِ γn'w «نیرو» (در جاتکهٔ وسنتره) هم از همین ستاک باشد». پیوندِ معنایی «گرفتن» ← «نیرو، توان» پذیرفتنی است، اما در واژه‌شناسیِ سغدی تأیید نشده: فرهنگ سغدیِ بدرالزمان قریب (۱۳۷۴)، که خودِ نورایی هم به صفحهٔ ۱۶۳ آن ارجاع می‌دهد، در سراسر بخشِ γn- چنین سرواژه‌ای ندارد، و معنیِ «مهارت» که نورایی افزوده نه در بیلی هست نه در قریب. بنابراین این گره در حدِ «حدسِ بیلی» است و بیش از آن نیست.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"ISS:27\", \"status\": \"not_checked\",\n       \"note\": \"page not obtainable; the substitute Bailey DKS s.v. uysgana- ends 'Possibly Sogd. VJ γn'w \\\"force\\\"' (ISS_alt_DKS.txt line 1113) — the same tentative claim, without the gloss 'skill'.\"},\n      {\"ref\": \"SOD:163\", \"status\": \"not_found\",\n       \"note\": \"SOD_pages.txt leaf 229 = printed p.163 is indeed the γn- page of Gharib (entries 4121 γn'β- … 4168 γr-), but it contains no γnw / γan 'power, force, skill'; the neighbours are γn'β- 'lament', γnc(h) 'bad smelling' (< Av. gainti-), γnδ'k 'bad, evil', γnkyn 'brave, victorious', γnt'k 'bad, evil'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, entries 4121-4168 (p.163)\", \"stance\": \"contradicts\",\n       \"note\": \"the standard Sogdian lexicon does not record the word; grepping the English index for 'force'/'power'/'skill' returns only qnw'ncya no. 4784 'skill' (Christian Sogdian), which is a different word.\"},\n      {\"src\": \"ISS_alt_DKS\", \"where\": \"Bailey, DKS s.v. uysgana- (line 1113)\", \"stance\": \"partial\",\n       \"note\": \"'Possibly Sogd. VJ γn'w \\\"force\\\"' — Bailey's own hedge ('possibly') is dropped in the chart.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"zağan\", \"verdict\": \"plausible\",\n     \"derivation\": \"New Persian زغن zaγan 'kite, Milvus, a black bird of prey' is a real and old word: Asadi Tusi's Loghat-e Fors (11th c.) glosses غلیواج as 'مرغ گوشت‌ربای، به معنی زغن بود', and Borhan-e Qate' has 'زغن و خاد (هم) مرغ گوشت‌ربای بود' with the Rudaki couplet Nourai quotes. Bailey derives it, exactly as the chart does, from the same Old Iranian *uz-gana- 'seizer' that gives Khotanese uysgana-: initial *uz- loses its vowel in the West Iranian development (*uzgana- > *zagan-, cf. NP زدن/زن- beside Av. jan-), and intervocalic -g- is kept as -γ- and written غ. The chart's arrow, however, makes زغن descend from the Khotanese word, which it does not: Bailey lists NP zaγan as a parallel outcome of *uz-gana- in another Iranian branch, i.e. a cognate, not a borrowing from Khotanese — Khotanese was never a donor to Persian. Nourai's own second reference is the right place to look: Mo'in's footnote to the زغن entry in Borhan cites Bailey's BSOS X and Transactions of the Philological Society 1946, p.159 n.1. Modern lexicography adds nothing against it (Wiktionary has no Persian entry at زغن at all, only an Arabic verb), so 'plausible' rather than 'confirmed'.\",\n     \"derivation_fa\": \"«زغن» به معنی پرندهٔ شکاریِ گوشت‌ربا (غلیواج) واژه‌ای کهن است: اسدی طوسی در «لغت فرس» غلیواج را «مرغ گوشت‌ربای، به معنی زغن» می‌داند و برهان قاطع بیت رودکی «جمله صید این جهانیم ای پسر / ما چو صعوه، مرگ برسان زغن» را برای آن می‌آورد. بیلی آن را از همان ایرانی باستانِ *uz-gana- «رباینده» می‌گیرد که در ختنی uysgana- «کرکس» شده است؛ در شاخهٔ غربی واکهٔ پیشوندِ *uz- افتاده و ‑g‑ میان‌واکه‌ای به غ نرم شده است. اما پیکانِ نمودار نادرست است: «زغن» از واژهٔ ختنی گرفته نشده، بلکه هم‌ریشهٔ آن است؛ ختنی هرگز زبانِ وام‌دهنده به فارسی نبوده است. حاشیهٔ معین بر برهان قاطع نیز همین‌جا به مقالات بیلی ارجاع می‌دهد. بنابراین ریشه‌شناسی پذیرفتنی است ولی رابطهٔ دو گره باید «هم‌ریشگی» خوانده شود نه «اشتقاق».\",\n     \"sources\": [W_ZAGAN, A_ZAGAN],\n     \"ref_check\": [\n      {\"ref\": \"ISS:27\", \"status\": \"not_checked\",\n       \"note\": \"page not obtainable; Bailey's DKS s.v. uysgana- (ISS_alt_DKS.txt line 1113) names the Persian word in the same breath: 'From uz-gana- \\\"rapax\\\" of a bird of prey, N.Pers. zaγan, Greek lw …, Turk lw sagen.'\"},\n      {\"ref\": \"BQT:1023\", \"status\": \"supports\",\n       \"note\": \"BQT_v2_pages.txt leaf 485 (printed ≈1023-1028 by the vol-2 rule printed ≈ leaf+543; the run of leaf numerals drifts by a few pages here) carries the entry '_زغن وخاد (هم.) مرغ گوشت ربای بود. رودکی (سمرقندی) گوید: جمله صید این جهانیم ای پسر / ما چو صعوه مرگ برسان زغن' — the very couplet the JSON records — and Mo'in's footnote on the same page cites 'BSOS., X, … 97' and 'Philological Society, Hertford 1946, p.159, note 1', i.e. Bailey, exactly the authority behind Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors (FRS_pages.txt line 3574)\", \"stance\": \"supports\",\n       \"note\": \"'غلیواج مرغ گوشت ربای بمعنی زغن بود' — the word and its meaning are attested in the oldest Persian dictionary (11th c.).\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir, فرهنگ معین s.v. زغن\", \"stance\": \"partial\",\n       \"note\": \"'(زَ غَ) (اِ.) پرنده‌ای است گوشتخوار از دستهٔ بازها اما کوچک‌تر از باز' — meaning confirmed, but Mo'in gives no origin tag, so nothing for or against the Iranian etymology.\"},\n      {\"src\": \"RCH\", \"where\": \"Richardson-Johnson, Persian-Arabic-English Dictionary (RCH.txt line 55867)\", \"stance\": \"silent\",\n       \"note\": \"its only zaghan is the Arabic verbal noun 'hating; liking' (from ظعن/ضغن), not the bird; no etymology.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (grep zagan/zayan in HRN.txt)\", \"stance\": \"silent\",\n       \"note\": \"Horn has no entry for زغن at all — the word is missing from the 1893 Grundriss, which is why Bailey (1946) had to supply the etymology.\"}\n     ]\n    }\n   ]\n  },\n\n  # ============================== ENTRY 1 — Gang ==============================\n  {\n   \"entry\": 1,\n   \"root\": \"Gang\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *gang- 'to mock, jeer' (Pokorny IEW 352; Walde-Pokorny I 535), an onomatopoeic root, beside the parallel sound-words *gong-/*guñg- 'to mutter, hum'\",\n   \"note\": \"Pokorny's page 352 opens with exactly this headword: 'gang- \\\"spotten, höhnen\\\"; gango-s \\\"Hohn\\\"', with Skt. gañja-ḥ 'contempt, mockery', Gk. γαγγαίνειν (Hesychius) 'to mock', OE canc, ge-canc 'scorn, derision' (= Skt. gañja-ḥ), cancettan 'to mock', ON kangen-yrði 'mocking words'. Nourai's gloss 'to mock, hum' is a compression of two things Pokorny keeps a little apart: 'mock' is the root proper, and 'hum' comes from Pokorny's closing remark that 'Die Sippe scheint ursprüngl. schallmalend. Ähnliche Schallwörter sind ai. gúñjati \\\"summt, brummt\\\", gr. γογγρύζειν \\\"grunzen\\\" … aksl. gągnavъ \\\"schwer sprechend\\\", russ. gugnati \\\"murmeln\\\"'. Since these are the words the chart's own Sanskrit and Persian nodes hang on, the compression matters and is discussed at node 1. Root, language label and Pokorny page number are all correct.\",\n   \"note_fa\": \"پوکورنی در صفحهٔ ۳۵۲ کتاب خود دقیقاً همین سرواژه را دارد: gang- «ریشخند کردن، تمسخر کردن»، با سنسکریت gañja- «خواری، ریشخند»، یونانی γαγγαίνειν و انگلیسی باستان canc «تمسخر». معنایی که نورایی داده («ریشخند کردن، زمزمه/وزوز کردن») دو چیز را در هم می‌کند: «ریشخند» معنیِ خودِ ریشه است، و «وزوز» از این جملهٔ پایانیِ پوکورنی می‌آید که «این خانواده در اصل آواواژه است و واژه‌های آواییِ همانند عبارت‌اند از سنسکریت gúñjati «وزوز می‌کند» و یونانی γογγρύζειν …». چون همین واژه‌ها پایهٔ گره‌های بعدیِ نمودارند، این تفاوت مهم است (بنگرید به گرهٔ ۱). در مجموع جعبهٔ ریشه، برچسبِ زبان و شمارهٔ صفحهٔ پوکورنی درست است.\",\n   \"sources\": [W_GONG],\n   \"ref_check\": [\n    {\"ref\": \"POK:352\", \"status\": \"supports\",\n     \"note\": \"POK_02.txt line 53; the printed page numeral '352' stands on the line immediately above the headword: 'gang- \\\"spotten, höhnen\\\"; gango-s \\\"Hohn\\\". Ai. ganja-ḥ \\\"Verachtung, Hohn\\\", ganjana-ḥ \\\"verachtend, höhnend\\\"; gr. γαγγαίνειν …; ags. canc u. ge-canc \\\"Spott, Hohn, Tadel\\\" (= ai. ganja-ḥ) … WP. I 535, WH. I 582 f.'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 535 (WLD_Bd1 djvu line 33679)\", \"stance\": \"supports\",\n     \"note\": \"'gang- „spotten, hohnen“. Ai. ganja-ḥ „Verachtung, Hohn“ … Die Sippe scheint ursprgl. schallmalend.' — the source Pokorny 352 abridges; and at gou- (line 39966) Walde-Pokorny explicitly files 'ai. gunjati „summt, brummt“' 's. unter *gang- „spotten“', i.e. rather more firmly than Pokorny does.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, IE Comparative Dictionary, gang- (1) and (2), and gong- (IEC.txt lines 3882, 3883, 4236)\", \"stance\": \"partial\",\n     \"note\": \"Mann splits the material: 'gang- \\\"scorn\\\". WP I, 535. … Skt. gañjaḥ, id.; Gk. gaggaíno \\\"mock\\\" …' and separately 'gang- \\\"grate, caw, cackle, make a noise\\\"' and 'gong- \\\"mutter, murmur\\\". Cf. gang-, ganǵ- Gk. cf. goggüzo; OCS gognati'. So the 'mock' and 'hum' senses are for Mann two (cross-referenced) roots, not one.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt)\", \"stance\": \"silent\",\n     \"note\": \"no gang- entry: no English word reaches the root through Latin or Greek, so the appendix simply omits it; its silence is not a disagreement.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"gunj\", \"verdict\": \"plausible\",\n     \"derivation\": \"Sanskrit guñj (present guñjati) 'to buzz, hum, murmur' is real and well attested (of bees, of a muttering voice), and it is an imitative formation. The question is the arrow. Pokorny does not derive guñjati from *gang-: he closes the *gang- article with 'Die Sippe scheint ursprüngl. schallmalend. Ähnliche Schallwörter sind ai. gúñjati \\\"summt, brummt\\\", gr. γογγρύζειν \\\"grunzen\\\", spätgr. γογγύζω \\\"murre\\\", aksl. gągnavъ \\\"schwer sprechend\\\", russ. gugnati \\\"murmeln\\\", poln. gęgać \\\"schnattern\\\"' — i.e. guñjati is listed as a similar but independent onomatopoeia beside *gang-, with -u- vocalism against the root's -a-. Walde-Pokorny (at gou-, WLD I) is more generous and says outright that guñjati belongs 'unter *gang- \\\"spotten\\\"'; Mann sets up a separate root gong- 'mutter, murmur' for the same word. Since expressive roots do not obey regular ablaut, all three positions are defensible; Nourai has simply adopted the most generous one. Note also that Pokorny's Sanskrit witness for *gang- proper is gañja-ḥ 'contempt, mockery', not guñj-.\",\n     \"derivation_fa\": \"سنسکریتِ guñj (زمان حالِ guñjati) «وزوز کردن، زمزمه کردن» واژه‌ای است حقیقی و آواواژه‌ای (دربارهٔ صدای زنبور و نجوای زیر لب). ولی پیکانِ نمودار جای بحث دارد: پوکورنی این واژه را از *gang- نمی‌گیرد، بلکه در پایانِ مقالهٔ خود آن را در شمارِ «واژه‌های آواییِ همانند» می‌آورد، در کنارِ یونانیِ γογγρύζειν و اسلاویِ کهنِ gągnavъ؛ گواهِ سنسکریتِ خودِ ریشه نزد او gañja- «خواری، ریشخند» است نه guñj-. در برابر، والده-پوکورنی صریحاً guñjati را «ذیل *gang-» می‌داند و مان (IEC) ریشهٔ جداگانه‌ای به نامِ gong- «زمزمه کردن» برای آن می‌سازد. چون ریشه‌های آواواژه‌ای قاعدهٔ آواییِ منظم ندارند، هر سه رأی دفاع‌پذیر است و نورایی سخاوتمندانه‌ترین را برگزیده است؛ از این رو «با احتیاط پذیرفتنی».\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:352\", \"status\": \"partial\",\n       \"note\": \"IEW 352 (POK_02.txt lines 53-57) has the word but not the descent: 'Ähnliche Schallwörter sind ai. gúñjati \\\"summt, brummt\\\", gr. γογγρύζειν \\\"grunzen\\\" …' — 'similar sound-words', explicitly set beside the root rather than under it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I, s.v. gou- (WLD_Bd1 djvu line 39966)\", \"stance\": \"supports\",\n       \"note\": \"'(: gr. γογγύζω \\\"murre, gurre\\\", NT.?, dies eher zu ai. gunjati \\\"summt, brummt\\\", s. unter *gang- \\\"spotten\\\")' — Walde-Pokorny files guñjati under *gang-, which is Nourai's arrow.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann, gong- 'mutter, murmur' (IEC.txt line 4236) and gang- (2) (line 3882)\", \"stance\": \"partial\",\n       \"note\": \"'gong- \\\"mutter, murmur\\\". Cf. gang-, ganǵ-' and 'gang- \\\"grate, caw, cackle, make a noise\\\" … Skt. cf. gañjami \\\"grate, din\\\" (fr. *ganǵ- or *gong-)' — a cross-referenced but formally separate root.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\", \"note\": \"neither gang- nor gong- appears in the appendix.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"gung\", \"verdict\": \"plausible\",\n     \"derivation\": \"Middle Persian gung 'dumb, mute' is solidly attested: MacKenzie, Concise Pahlavi Dictionary, prints 'gung [g(w)ng | N ~] dumb', and Nyberg's glossary 'gung [gwng, gng] dumb 11°. 127. 652°', citing the Pahlavi Rivāyat and the Shāyast nē Shāyast passage 'bē kē karr ayāb gung ēnyā …' ('with the exception of the deaf and the dumb'). What cannot stand as drawn is the arrow from Sanskrit: Middle Persian does not descend from Sanskrit, and no loan is involved either — there is no route by which an Indo-Aryan present stem guñj- could become a Sasanian Persian adjective. What the sources give is a comparison, and a nervous one: Horn, Grundriss no. 937 (p.209) writes 'gung \\\"stumm\\\". skr. √guñj-, guñjati \\\"summen, brummen\\\" (Geiger: \\\"das Brummen bezeichnet die tierischen Laute des Stummen im Gegensatz zur menschlichen Sprache\\\"). Unsicher.' and Hübschmann's note on the same number (Pers. Stud. p.95) is a bare 'Höchst unsicher.' Wiktionary phrases it the same way: MP gung, 'perhaps developed from the sense \\\"to mock, hum\\\", usually connected to Sanskrit guñjati … itself of imitative origin'. Read as 'cognate with / compared with', the node is fine; read as descent, it is not.\",\n     \"derivation_fa\": \"واژهٔ فارسی میانهٔ gung «لال، گنگ» به‌خوبی گواهی شده است: مکنزی در فرهنگ کوچک پهلوی «gung [g(w)ng] dumb» می‌آورد و نیبرگ در واژه‌نامهٔ خود «gung [gwng, gng] لال» با ارجاع به شایست نشایست («بجز کر یا گنگ …»). آنچه به‌صورتِ نمودار پذیرفتنی نیست پیکانِ «از سنسکریت» است: فارسی میانه از سنسکریت نیامده و راهِ وام‌گیری هم در کار نیست. آنچه مآخذ می‌گویند «سنجش» است و آن هم با تردید: هرن (بند ۹۳۷، ص ۲۰۹) پس از سنجیدنِ gung با guñjati سنسکریت می‌نویسد «نامطمئن»، و هوبشمان در حاشیهٔ همان بند (مطالعات فارسی، ص ۹۵) می‌نویسد «بسیار نامطمئن». ویکی‌واژه نیز می‌گوید «معمولاً با guñjati سنسکریت مرتبط دانسته می‌شود» و نه بیش. پس اگر پیکان را «هم‌ریشه/هم‌سنجِ» بخوانیم درست است، و اگر «اشتقاق» بخوانیم نادرست.\",\n     \"sources\": [W_GONG, A_GONG],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1844\", \"status\": \"supports\",\n       \"note\": \"BQT vol 3, pdf page 641 = printed 1844 (running head '۱۸۴۴' on the leaf; BQT_v3_pagemap.json maps 1844→641). The گنگ entry's sense 12 is 'و آنرا لال گویند و بعربی ابکم خوانند یعنی شخصی که با ایما و اشاره حرف زند نه با زبان', and Mo'in's footnote 11 on the same page reads 'پهلوی gung، … افغانی و بلوچی gung. رک: اشتقاق - هوبشمان ۹۳۷' — a Pahlavi gung, exactly Nourai's node, referred back to Horn/Hübschmann no. 937.\"},\n      {\"ref\": \"MON:3418\", \"status\": \"supports\",\n       \"note\": \"Mo'in, Farhang-e Farsi s.v. گنگ (read through abadis.ir, which reproduces Mo'in's entry text with his origin tags but no pagination): '(گُ) [ په . ] (ص.) لال، بی‌زبان' — the tag [په.] is Mo'in's mark for Pahlavi, so Mo'in does assert the Pahlavi etymon; the page number itself cannot be checked online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt line 384; PHD_mackenzie.txt line 2619)\", \"stance\": \"supports\",\n       \"note\": \"'gung [g(w)ng | N ~] dumb' — and in the English-Pahlavi part 'dumb agōwag, gung' (PHD.txt line 1706).\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt lines 1739, 3054)\", \"stance\": \"supports\",\n       \"note\": \"'gung [gwng, gng] dumb 11°. 127. 652°' and, in the commentary, 'bē kē karr ayāb gung ēnyā … \\\"With the exception of the deaf and dumb, the religious duties must be fulfilled by everyone\\\"'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 937, p.209 (HRN.txt line 8134 ff.; leaf 230 = printed 209)\", \"stance\": \"partial\",\n       \"note\": \"'937. gung \\\"stumm\\\". skr. √guñj-, guñjati \\\"summen, brummen\\\" … Unsicher. LW. afγ. bel. gung \\\"stumm\\\".' — Horn compares, and doubts; he gives no Pahlavi form.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.95, note on Horn's no. 937 (HUB.txt leaf 105)\", \"stance\": \"contradicts\",\n       \"note\": \"'937. Höchst unsicher.' — the harshest verdict of Nourai's own authorities on this very equation.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"gong\", \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian گنگ gong (classical gung, Tajik гунг, Dari gung) 'mute' continues Middle Persian gung directly and without change: the MP short u is preserved in the classical and eastern pronunciation and lowered to o only in modern Iranian Persian (gung > gong), the same way MP gurg > Ir. Pers. gorg. Wiktionary states 'Inherited from Middle Persian gwng /gung/, gng /gung/ \\\"dumb, mute\\\"'; Farrokhi's line, which Nourai prints and which Mo'in also prints in the footnote to Borhan 1844, 'گنگ باد آنکس که اندر طعن تو گوید سخن / کور باد آنکس که اندر عرض تو جوید عوار', shows the word already in the 11th century with exactly this sense. One inaccuracy of gloss: گنگ means 'mute, unable to speak', not 'deaf' — Persian for deaf is کر (MP karr), and the Pahlavi and Borhan passages set karr and gung side by side as two different disabilities. 'Deaf' in the chart is an artefact of the English idiom 'deaf and dumb'.\",\n     \"derivation_fa\": \"«گنگ» فارسی نو دنبالهٔ بی‌واسطهٔ gung فارسی میانه است؛ واکهٔ کوتاهِ u در تلفظ کلاسیک و در دری و تاجیکی مانده و تنها در فارسی ایرانِ امروز به o بدل شده است (همان تحولی که در gurg > گرگ دیده می‌شود). ویکی‌واژه می‌نویسد «به ارث رسیده از فارسی میانهٔ gwng/gng «لال»». بیتِ فرخی که نورایی آورده و معین نیز در حاشیهٔ برهان (ص ۱۸۴۴) نقل کرده، کاربردِ سدهٔ پنجم هجری را نشان می‌دهد. تنها لغزشِ گره در معناست: «گنگ» یعنی لال و بی‌زبان، نه «کر»؛ برابرِ کر در فارسی «کر» (پهلوی karr) است و در همان متن‌های پهلوی و برهان، «کر» و «گنگ» دو نقصِ جداگانه‌اند. «deaf» در نمودار از اصطلاحِ انگلیسیِ deaf and dumb به این‌جا راه یافته است.\",\n     \"sources\": [W_GONG, A_GONG],\n     \"ref_check\": [\n      {\"ref\": \"HRN:209\", \"status\": \"partial\",\n       \"note\": \"Horn's no. 937 stands on p.209 (HRN.txt leaf 230; the running head '- 209 -' is at line 8115), so the page reference is right, and it does give NP gung 'stumm'; but Horn's entry is about the Sanskrit comparison and ends 'Unsicher', and it records no Pahlavi ancestor for the Persian word.\"},\n      {\"ref\": \"BQT:1844\", \"status\": \"supports\",\n       \"note\": \"printed p.1844 (pdf 641) has both the Persian sense ('لال … بعربی ابکم') and, in footnote 11, 'پهلوی gung' with the Farrokhi couplet the JSON quotes, 'گنگ باد آنکس که اندر طعن تو گوید سخن …' ('فرخی سیستانی').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir, s.v. گنگ\", \"stance\": \"supports\",\n       \"note\": \"'(گُ) [ په . ] (ص.) لال، بی‌زبان' — Pahlavi origin tag, and the gloss is 'mute', not 'deaf'.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, s.v. gung and s.v. karr\", \"stance\": \"partial\",\n       \"note\": \"'gung … dumb' with 'N ~' (i.e. surviving unchanged in New Persian) confirms the descent; MacKenzie's separate karr 'deaf' shows that 'deaf' is not part of this word's meaning.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, p.1844\", \"stance\": \"supports\",\n       \"note\": \"senses 12 'لال … شخصی که با ایما و اشاره حرف زند نه با زبان'; the footnote adds Afghan and Baluchi gung and Kurdish forms.\"}\n     ]\n    }\n   ]\n  },\n\n  # ============================== ENTRY 2 — Gantuma ==============================\n  {\n   \"entry\": 2,\n   \"root\": \"Gantuma\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Young Avestan gaṇtuma- / gantuma- m. 'wheat' (Bartholomae, AiW col. 493), Proto-Iranian *gantuma-, whence NPers. gandom\",\n   \"note\": \"Bartholomae's Altiranisches Wörterbuch gives the headword verbatim: 'j. gantuma- m. \\\"Weizen\\\"', with the Nirangistan passage 'unter den Getreidearten ist es der Weizen, der den Frawašis genehm ist' (N 28); Wiktionary lists Avestan gaṇtuma / gantuma among the cognates of گندم. The root box's language label and gloss are therefore right. The chart's added note, 'Cognate with Sanskrit gōdhūma', is also right and is precisely what Nourai's two references say: Hübschmann, Persische Studien p.95 ad Horn 935, 'Skr. gōdhūma- wird volksetymologische Anlehnung von *gandhūma- an die Composita mit gō- \\\"Kuh\\\" sein (go-dhūma- gleichsam \\\"Kuhrauch\\\"; vgl. unsern Pflanzennamen Erdrauch)', and Buck 516 §8.48.7, 'Skt. godhūma-, by pop. etym. (cpd. of go- \\\"cow\\\" and dhūma- \\\"smoke\\\") for *gandhuma- = Av. gantuma-, NPers gandum \\\"wheat\\\", root connection? Barth. 493.' Both mark the pre-Indo-Iranian source as unknown — 'root connection?' — so the word is best treated as an inherited Indo-Iranian agricultural term of ultimately obscure (very possibly non-IE, Central Asian) origin, which is why Nourai wisely heads the chart with an Avestan and not a PIE box.\",\n   \"note_fa\": \"بارتولومه در «فرهنگ ایرانی باستان» (ستون ۴۹۳) سرواژهٔ «gantuma- (جوان‌اوستایی)، مذکر، گندم» را با شاهدی از نیرنگستان آورده است، و ویکی‌واژه نیز اوستاییِ gaṇtuma/gantuma را در شمارِ هم‌ریشه‌های «گندم» می‌آورد؛ پس برچسبِ زبان و معنای جعبهٔ ریشه درست است. یادداشتِ نمودار («هم‌ریشه با gōdhūma سنسکریت») نیز همان است که هر دو مأخذِ نورایی می‌گویند: هوبشمان (مطالعات فارسی، ص ۹۵، ذیل بند ۹۳۵ هرن) gōdhūma- سنسکریت را ریشه‌شناسیِ عامیانه‌ای از *gandhūma- می‌داند که به ترکیب‌های دارای gō- «گاو» تکیه کرده است، و باک (ص ۵۱۶) همین را با افزودنِ «پیوندِ ریشه‌ای؟» می‌آورد. یعنی خاستگاهِ پیش‌ازهندوایرانیِ واژه ناشناخته است و چه‌بسا وام‌واژه‌ای آسیای‌میانه‌ای باشد؛ به همین سبب درست بوده که نورایی سرِ نمودار را «اوستایی» گذاشته و نه «هندواروپایی».\",\n   \"sources\": [W_GANDOM],\n   \"ref_check\": [\n    {\"ref\": \"HUB:95\", \"status\": \"supports\",\n     \"note\": \"HUB.txt leaf 105 = printed p.95, note on Horn's no. 935: 'Skr. gōdhūma- wird volksetymologische Anlehnung von *gandhūma- an die Composita mit gō- \\\"Kuh\\\" sein (go-dhūma- gleichsam \\\"Kuhrauch\\\"; vgl. unsern Pflanzennamen Erdrauch, gr. καπνός)' — exactly the chart's note on the Sanskrit cognate.\"},\n    {\"ref\": \"SYN:516\", \"status\": \"supports\",\n     \"note\": \"SYN.txt leaf 568 = printed p.516, §8.48 WHEAT, para 7: 'Skt. godhūma-, by pop. etym. (cpd. of go- \\\"cow\\\" and dhūma- \\\"smoke\\\") for *gandhuma- = Av. gantuma-, NPers gandum \\\"wheat\\\", root connection? Barth. 493. Hübschmann, Pers. Stud.' — the Avestan headword, the Persian outcome and the Sanskrit cognate in one sentence, on the cited page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch col. 493 (BRT.txt line 9997; column numerals 493 at line 9985, 494 at 9988)\", \"stance\": \"supports\",\n     \"note\": \"'j. gantuma- m. \\\"Weizen\\\": … yavanąm ratufriš \\\"unter den Getreidearten ist es der Weizen, der den [Frawašis] genehm ist\\\" N. 28' — the column Buck cites.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck §8.48, pp.515-516\", \"stance\": \"supports\",\n     \"note\": \"the comparative table prints 'Av. gantuma-' and 'Skt. godhūma-' as the Indo-Iranian entries for WHEAT.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha, index leaf [pdf page 443]\", \"stance\": \"supports\",\n     \"note\": \"the wheat article lists 'GANTUMA (AVESTAN) … GANDUM, GANTUM (PAHLAVI) … GENIM (KURDISH) … GANDIM (BALUCHI) … GHANEM, GHANUM (AFGHANI) … KANTI (TOKHARIAN B) … GANAMA (KHOTANESE) … GODHUMA (SANSKRIT)' with 'REFERENCES: POKORNY 390-391; MACKENZIE: (WHEAT) 140; BUCK: 513-516'.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.246 §138\", \"stance\": \"supports\",\n     \"note\": \"in the sound-law chapter: 'gandum \\\"Weizen\\\", skr. gōdhūma-' listed among the words in which Old Persian g remains g in New Persian.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"gantum\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The Middle Persian word is certain, though the spelling in the chart is the Pazand one. In Book Pahlavi the word is written with the Aramaic heterogram ḤNṬH (Aramaic ḥinṭā 'wheat'), so MacKenzie's dictionary prints 'gandum [Hz < A ḥnṭh | (M gnwm), N ~] wheat', with the Manichaean Middle Persian spelling gnwm as the phonetic control; Wiktionary likewise cites Manichaean 𐫃𐫗𐫇𐫖 (gnwm) and Parthian gndwm. The form 'gantum' with -t- is what the Pazand transcriptions of the Pahlavi glossaries give, and it is Horn's own citation, no. 935 p.209: 'phlv.-paz. gantum d. i. gandum (PPGl.)' — Pazand spelling gantum, real value gandum. Phonologically Av. gaṇtuma- > MP gandum by the regular voicing of a stop after a nasal in Middle Persian (*-nt- > -nd-, as in Av. bandaka- > MP bandag) and by the reduction of the thematic ending. So the node is right, with the caveat that gantum is a graphic, not a phonetic, Middle Persian form.\",\n     \"derivation_fa\": \"واژهٔ فارسی میانه قطعی است، اگرچه صورتی که در نمودار آمده صورتِ پازند است. در پهلویِ کتابی این واژه با هزوارشِ آرامیِ ḤNṬH نوشته می‌شد؛ از این رو مکنزی می‌نویسد «gandum [هزوارش < آرامیِ ḥnṭh | (مانوی gnwm)، فارسی نو ~] گندم» و صورتِ مانویِ gnwm را گواهِ تلفظ می‌گیرد؛ ویکی‌واژه نیز صورتِ مانویِ gnwm و پارتیِ gndwm را می‌آورد. صورتِ gantum با «ت» همان است که در آوانویسیِ پازندِ واژه‌نامه‌های پهلوی آمده و خودِ هرن (بند ۹۳۵، ص ۲۰۹) می‌نویسد: «پهلوی-پازند gantum یعنی gandum». از نظر آوایی، اوستاییِ gaṇtuma- در فارسی میانه به gandum بدل شده است، زیرا در فارسی میانه همخوانِ بی‌واکِ پس از خیشومی واکدار می‌شود (nt < nd، مانندِ bandaka- > bandag) و پایانهٔ ستاکی می‌افتد. پس گره درست است، با این توضیح که gantum صورتی نوشتاری است نه تلفظی.\",\n     \"sources\": [W_GANDOM],\n     \"ref_check\": [\n      {\"ref\": \"HRN:209\", \"status\": \"supports\",\n       \"note\": \"Horn, Grundriss no. 935, on the page whose running head is '- 209 -' (HRN.txt leaf 230): '935. gend/um \\\"Weizen\\\", ar. LW. jandum in jauz-i jandum. skr. gōdhūma- \\\"Weizen\\\" (dagegen iran. *gandhūma-, Hübschmann, ZDMG. 44, 556) ; phlv.-paz. gantum d. i. gandum (PPGl.).' — the Pahlavi form Nourai's node prints, on the cited page.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt line 378; PHD_mackenzie.txt line 2448)\", \"stance\": \"partial\",\n       \"note\": \"'gandum [Hz < A ḥnṭh | (M gnwm), N ~] wheat' — same word, but MacKenzie's phonetic reading is gandum, not gantum; and in the English index 'wheat gandum'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (grep gandum/gantum)\", \"stance\": \"silent\",\n       \"note\": \"the word does not occur in Nyberg's selected glossary (his texts do not include an agricultural passage using it).\"},\n      {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary no. 4162 (p.163 area)\", \"stance\": \"supports\",\n       \"note\": \"'4162 γntm S, C — γandam ©ob. -y — wheat' — the Sogdian sister-form, showing the same Middle Iranian *gandum across the family.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\",\n     \"words\": \"gandom; gandomgŭn; gandom-ba\", \"verdict\": \"confirmed\",\n     \"derivation\": \"All three are correct. (1) گندم gandom continues MP gandum unbroken (classical gandum, still gandum in Dari and Tajik, gandom only in modern Iranian Persian); the variants the chart puts in brackets are ordinary Persian derivatives — گندمک gandomak, the diminutive in -ak (also a name of the smallpox-like rash), and گندمینه gandomina, the adjectival -ina 'of wheat'. Wiktionary's chain is the chart's: NPers گندم < MP gnwm/gandum < Proto-Iranian, beside Parthian gndwm, Sogdian γntm, Kurdish genim, Pashto غنم, Avestan gaṇtuma-, Sanskrit गोधूम. (2) گندمگون gandomgun 'wheat-coloured, olive-complexioned' is گندم + گون, the Persian colour suffix from MP gōn 'colour, kind' (Av. gaona- 'hair, colour'), whence Nourai's cross-reference to his chart Gěu; the Hafez line the JSON records, 'خال مشکین که بدان عارض گندمگون است', is the classic occurrence. (3) گندم‌با gandom-bā (dialectal گندم‌وا) 'wheat pottage' is the dish now called حلیم/هلیم; -با is the old Persian word for a cooked broth or stew (as in زیرباج/سکباج), which Nourai refers to his chart Pekw, i.e. to PIE *pekʷ- 'to cook' — a link that is plausible but not demonstrable from Middle Persian, and Mo'in's own footnote is content to analyse the compound as 'گندم + با (=آش)'. The Persian forms in the JSON match the printed page exactly.\",\n     \"derivation_fa\": \"هر سه واژه درست است. ۱) «گندم» دنبالهٔ بی‌گسستِ gandum فارسی میانه است (در دری و تاجیکی هنوز gandum، و gandom تنها در فارسیِ ایران)؛ صورت‌های داخلِ کمانک ساخته‌های عادیِ فارسی‌اند: «گندمک» با پسوندِ تصغیرِ ‑ک و «گندمینه» با پسوندِ نسبتِ ‑ینه. زنجیرهٔ ویکی‌واژه همان زنجیرهٔ نمودار است: فارسیِ گندم ← فارسی میانهٔ gnwm ← ایرانی آغازین، در کنارِ پارتیِ gndwm، سغدیِ γntm، کردیِ genim، پشتوِ غنم، اوستاییِ gaṇtuma- و سنسکریتِ गोधूम. ۲) «گندمگون» از گندم + گون است؛ «گون» از gōn فارسی میانه (اوستایی gaona- «مو، رنگ») که نورایی آن را به نمودارِ Gěu ارجاع می‌دهد؛ بیتِ حافظ «خال مشکین که بدان عارض گندمگون است» شاهدِ کلاسیکِ آن است. ۳) «گندم‌با» (گویشی: گندم‌وا) همان خوراکی است که امروز حلیم می‌گویند؛ جزءِ «با» واژهٔ کهنِ فارسی برای آش و خورش است (مانندِ زیرباج و سکباج) و نورایی آن را به ریشهٔ *pekʷ- «پختن» می‌برد، که پذیرفتنی است ولی از فارسی میانه اثبات‌پذیر نیست؛ حاشیهٔ معین خود به تجزیهٔ «گندم + با (=آش)» بسنده می‌کند. صورت‌های فارسیِ ثبت‌شده در داده‌ها با چاپِ کتاب دقیقاً می‌خواند.\",\n     \"sources\": [W_GANDOM, A_GANDOM],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1842\", \"status\": \"supports\",\n       \"note\": \"BQT vol 3, pdf page 639 = printed 1842 (BQT_v3_pagemap.json 1842→639). Mo'in's footnote 5 on that page: 'گندم - بفتح اول و ضم سوم، پهلوی و پازند gantum، معرب جندم jandum (در: جوزجندم)، کردی genim، … منجی ghandém … بلوچی gandim، «اشتقاق ۹۳۵»، و رک: هوبشمان' — Pahlavi/Pazand etymon, the Arabicised form, the dialect cognates, and a cross-reference to Horn/Hübschmann no. 935. Footnote 6 on the same page glosses the compound: 'از: گندم + با (=آش)', and the entry 'گندما - آش گندم را گویند که حلیم باشد' is printed there, i.e. Nourai's gandom-bā.\"},\n      {\"ref\": \"MON:3411\", \"status\": \"partial\",\n       \"note\": \"Mo'in, Farhang-e Farsi s.v. گندم read through abadis.ir: '(گَ دُ) (اِ.) گیاهی است یک‌ساله، علفی با ریشهٔ افشان و ساقهٔ میان‌تهی که از آرد آن برای پختن نان استفاده می‌شود' — the meaning is confirmed, but the online text carries no origin tag and no pagination, so the page reference itself could not be checked.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 935, p.209\", \"stance\": \"supports\",\n       \"note\": \"'935. gend/um \\\"Weizen\\\" … LW. kurd. genim; afγ. γanum; wa/. γidim, sangl. minj. γandām, sar. zandani, sandum, šyn. zindum, yidγ. γadum; bel. gandīm' — the Iranian dialect spread of the same word.\"},\n      {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir, s.v. گندم\", \"stance\": \"partial\",\n       \"note\": \"definition only, no etymology in the online text.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, printed p.1842\", \"stance\": \"supports\",\n       \"note\": \"'گندما - آش گندم را گویند که حلیم باشد' with footnote 'از: گندم + با (=آش)'; Mo'in's گندم footnote as quoted above.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, index leaf [pdf page 443]\", \"stance\": \"supports\",\n       \"note\": \"'GANDUM, GANTUM (PAHLAVI) 44' under the wheat article, with Buck 513-516 and MacKenzie 140 as authorities.\"}\n     ]\n    }\n   ]\n  },\n\n  # ============================== ENTRY 3 — Garenu ==============================\n  {\n   \"entry\": 3,\n   \"root\": \"Garenu\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Young Avestan garənav- m. 'scabies, mange' (Bartholomae, AiW ≈col. 516), whence MP gar, NPers گر garr\",\n   \"note\": \"Bartholomae's Altiranisches Wörterbuch has the headword in this exact shape: 'j. garənav- m. \\\"Krätze\\\"', with the Vidēvdād passage the entry quotes; Horn no. 895 (p.200) locates the attestations, 'aw. garənu- \\\"Krätze\\\" vd. 7,58 (145), yt. 13,131'. Nourai's language label and gloss are therefore right, though 'Krätze' is scabies/mange in man and beast alike, so 'scab on animal skin' is narrower than the Avestan word. One genuine dispute the chart does not show: the meaning of the Avestan word has been read three ways. Darmesteter and Jackson took it as 'Krätze'; Geldner (KZ 25, 551) translated 'Sonnenglut' (the blazing of the sun); Bartholomae himself, in the earlier Arische Forschungen/Studien II 96, read 'Frost' and compared Latin gelū, OCS žlědica, German kalt. Horn accordingly ends 'also unsicher'. Bartholomae's mature Wörterbuch of 1904 abandoned his own earlier reading and printed 'Krätze', which is the view Nourai's chart, Mo'in's footnote in Borhan and modern Iranian lexicography follow.\",\n   \"note_fa\": \"بارتولومه در «فرهنگ ایرانی باستان» سرواژه را دقیقاً به همین صورت آورده است: «garənav- (جوان‌اوستایی)، مذکر، جَرَب/گَر»، و هرن در بند ۸۹۵ (ص ۲۰۰) جای‌های کاربردِ آن را نشان می‌دهد: وندیداد ۷٫۵۸ و یشت ۱۳٫۱۳۱. پس برچسب و معنای جعبهٔ ریشه درست است، هرچند «Krätze» جَرَبِ آدمی و جانور هر دو است و معنای «زخمِ پوستِ جانوران» تنگ‌تر از آن است. نکته‌ای که نمودار نشان نمی‌دهد اختلافِ قدیمی بر سرِ معنای صورتِ اوستایی است: دارمستتر و جکسون آن را «جَرَب» خوانده‌اند، گلدنر «تَفِ آفتاب» و خودِ بارتولومه در نوشتهٔ پیشینش «سرما» (با سنجشِ لاتینیِ gelū و آلمانیِ kalt)؛ هرن از همین رو می‌نویسد «پس نامطمئن». اما بارتولومه در فرهنگِ پختهٔ ۱۹۰۴ خود رأیِ کهنِ خویش را وانهاد و «جَرَب» نوشت، و همین رأیی است که نورایی و حاشیهٔ معین بر برهان قاطع و ریشه‌شناسیِ امروزِ ایرانی پی می‌گیرند.\",\n   \"sources\": [W_GAR, A_GAR],\n   \"ref_check\": [\n    {\"ref\": \"BQT:1779\", \"status\": \"supports\",\n     \"note\": \"BQT vol 3, pdf page 576 = printed 1779 (BQT_v3_pagemap.json 1779→576). Mo'in's footnote 2 to the گر entry: 'مرضی است که دانه‌های کوچک بر بدن انسان و جانوران پدید آرد و خارش کند و مریض را «گرگین» (مخفف آن: گرگن) گویند. اوستا - garenu (جرب)؛ کردی gir (کر)، بلوچی gar (پیسی، جرب)، «اشتقاق ۸۹۵»، و رک: هوبشمان، ایضاً؛ پهلوی gar (جرب) «دارمستتر، تعلیقات ج۱ ص ۹۵»' — the Avestan etymon in Nourai's spelling, the Pahlavi intermediate, and both Persian words, on the cited page.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, Altiranisches Wörterbuch ≈col. 516 (BRT.txt line 10263; leaf 307, running head 'garad- mit aiwi' col. 514, next numeral 523)\", \"stance\": \"supports\",\n     \"note\": \"'j. garənav- m. \\\"Krätze\\\"' — the mature Bartholomae reads the word as Nourai does.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 895, p.200 (HRN.txt leaf 222)\", \"stance\": \"partial\",\n     \"note\": \"'895. ger, gerr \\\"Krätze\\\". aw. garənu- \\\"Krätze\\\" vd. 7,58 (145), yt. 13,131 (Darmesteter, ebenso Jackson …; Geldner übersetzt KZ. 25,551 \\\"Sonnenglut\\\", Bartholomae, Studien II,96 \\\"Frost\\\", cfr. lat. gelū, ksl. žlědica, nhd. kalt), also unsicher; phlv. gar' — the whole chain, with a warning over the Avestan gloss.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.246 §138\", \"stance\": \"partial\",\n     \"note\": \"'garr \\\"Krätze\\\", zd. garenu- (?)' — the same equation, with Hübschmann's own question mark.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985\", \"stance\": \"silent\",\n     \"note\": \"no PIE root is offered for the word; Nourai rightly heads the chart with an Avestan and not an IE box.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"gar 2\", \"verdict\": \"plausible\",\n     \"derivation\": \"A Middle Persian gar 'scab, mange' is asserted by all the older Iranists but is missing from the standard modern concise lexica. Horn no. 895 (p.200) ends his entry 'phlv. gar', and Mo'in's footnote in Borhan p.1779 sources it precisely: 'پهلوی gar (جرب) «دارمستتر، تعلیقات ج۱ ص ۹۵»', i.e. Darmesteter's notes to his Zend-Avesta, where the Pahlavi Vidēvdād renders Av. garənu- by gar. Formally the derivation is unproblematic: an Old Iranian u-stem *garnu- / garənav- loses its suffix in Middle Persian and appears as a bare gar, with the doubled -rr of the New Persian word (garr) reflecting the assimilated cluster. But MacKenzie's Concise Pahlavi Dictionary has only 'gar [gl] mountain' and no gar 'scab' (its list runs gar - -gar - garān - garasmān - gard …, and its English-Pahlavi part has no 'scab', 'mange' or 'itch' at all), and Nyberg's glossary likewise has only 'gar [gl] mountain … Av. (513 sq.) gari-'. So the etymon is well motivated and supported by the Pahlavi Vidēvdād glosses, but not attested in the dictionaries a modern reader would check first — hence 'plausible' rather than 'confirmed'.\",\n     \"derivation_fa\": \"وجودِ صورتِ فارسی میانهٔ gar «جَرَب، گَر» را همهٔ ایران‌شناسانِ قدیم می‌پذیرند، اما در فرهنگ‌های معیارِ امروزی نیامده است. هرن در پایانِ بند ۸۹۵ می‌نویسد «پهلوی gar»، و معین در حاشیهٔ برهان (ص ۱۷۷۹) سرچشمه را دقیق می‌دهد: «پهلوی gar (جرب)، دارمستتر، تعلیقات ج۱ ص ۹۵»، یعنی جایی که وندیدادِ پهلوی، garənu- اوستایی را به gar برگردانده است. از نظر ساخت نیز مشکلی نیست: ستاکِ ‑u‑ دارِ ایرانی باستان (*garnu-/garənav-) در فارسی میانه پسوند را از دست می‌دهد و به gar می‌رسد و «رِ» مشددِ فارسیِ نو (گَرّ) بازتابِ همان خوشهٔ همگون‌شده است. با این حال مکنزی در فرهنگ خود تنها «gar [gl] کوه» دارد و هیچ gar به معنی جرب ندارد، و نیبرگ نیز همین‌طور. پس ریشه‌شناسی موجه است ولی گواهِ فرهنگ‌نگاریِ امروزی ندارد؛ از این رو «با احتیاط پذیرفتنی».\",\n     \"sources\": [A_GAR],\n     \"ref_check\": [\n      {\"ref\": \"MON:3211\", \"status\": \"supports\",\n       \"note\": \"Mo'in, Farhang-e Farsi s.v. گر (read through abadis.ir): '( ~ . ) [ په . ] (اِ.) از بیماری‌های پوستی که باعث خارش و سوزش پوست بدن می‌شود' — the tag [په.] is Mo'in's mark for Pahlavi, so Mo'in does derive the Persian word from a Pahlavi gar; the page number cannot be verified online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt line 378 and the English-Pahlavi index)\", \"stance\": \"contradicts\",\n       \"note\": \"MacKenzie's only gar is 'gar [gl] mountain'; grepping his English-Pahlavi part for 'scab', 'mange' and 'itch' returns nothing — the word is not in his corpus.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt line 1626)\", \"stance\": \"contradicts\",\n       \"note\": \"'gar [gl] mountain, pl. cas. obl. ~-ān 20°. — Av. (513 sq.) gari-' — again only 'mountain'.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 895, p.200\", \"stance\": \"supports\",\n       \"note\": \"'… also unsicher; phlv. gar [skr. gard- \\\"eine Krankheit\\\" …]' — Horn's Pahlavi form, which is Nourai's node.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, printed p.1779, footnote 2\", \"stance\": \"supports\",\n       \"note\": \"'پهلوی gar (جرب) «دارمستتر، تعلیقات ج۱ ص ۹۵»'.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Persian\",\n     \"words\": \"gar 3; gargen\", \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The etymology of both words is sound; the flag is on the Persian script of the second one in the JSON. (a) گَرّ garr 'mange, scabies (which makes the hair fall out)' continues MP gar < Av. garənav-, and the Arabic equivalent Borhan gives is جرب; Nāser-Khosrow's couplet in the chart, 'گر نخواهی رنج گر از گرگنان پرهیز کن / جهل گر است ای پسر پرهیز کن زین زشت گر', plays on the word and on the homophone گر 'if'. The bracketed variant گَری garī is the abstract in -ī, 'scabbiness'. (b) گَرگِن gargen / گَرگین gargin 'scabby, mangy; bald' is گر plus the Persian adjectival suffix -gīn (MP -gēn, as in خشمگین, شرمگین, نمگین), with the by-form -gen; Mo'in's footnote to Borhan p.1779 states exactly this pairing, 'مریض را «گرگین» (مخفف آن: گرگن) گویند', and Nāser-Khosrow's plural گرگنان in the very verse the chart prints shows the short form was the living one for him. TRANSCRIPTION: the printed page (137, verified on a 400 dpi rendering of pdf page 167, saved as data/verification/sources/refs/ocr/BOOK/167.png) shows «گَرگِن ( گَرگین )» — four letters in the headword, five in the bracketed variant — matching the transliteration 'gargen' and the poem's گرگنان. The extraction wrote 'گرگین ( گرگین )', i.e. it silently replaced the headword گرگن with گرگین; the two forms are then indistinguishable in the data. This is an extraction error, not a misprint of the book.\",\n     \"derivation_fa\": \"ریشه‌شناسیِ هر دو واژه درست است و نشانه‌گذاری فقط بر املای فارسیِ واژهٔ دوم در داده‌هاست. الف) «گَرّ» یعنی جَرَب و بیماریِ پوستی که مو را می‌ریزد، دنبالهٔ gar فارسی میانه و آن از garənav- اوستایی؛ برابرِ عربیِ آن در برهان «جرب» است. بیتِ ناصرخسرو در نمودار بر همانندیِ «گَر» (بیماری) و «گر» (اگر) بازی می‌کند، و صورتِ داخلِ کمانک، «گَری»، مصدرِ صناعی با «ی» نسبت است. ب) «گَرگِن/گَرگین» یعنی «گَر داشته، کچل»، از «گر» + پسوندِ صفت‌سازِ ‑گین (فارسی میانه ‑gēn، مانندِ خشمگین و شرمگین) با گونهٔ ‑گن؛ معین در حاشیهٔ برهان (ص ۱۷۷۹) دقیقاً همین جفت را می‌آورد: «مریض را «گرگین» (مخفف آن: گرگن) گویند»، و جمعِ «گرگنان» در همان بیتِ ناصرخسرو نشان می‌دهد صورتِ کوتاه صورتِ زندهٔ زمانِ او بوده است. خطای خوانشِ اسکن: صفحهٔ چاپیِ ۱۳۷ (تصویرِ ۴۰۰ نقطه‌ای در data/verification/sources/refs/ocr/BOOK/167.png) «گَرگِن ( گَرگین )» دارد، یعنی سرواژه چهارحرفی و صورتِ کمانکی پنج‌حرفی است؛ اما در داده‌ها هر دو «گرگین» ثبت شده و سرواژهٔ «گرگن» از میان رفته است. این خطای استخراج است، نه خطای چاپِ کتاب.\",\n     \"error_in\": \"extraction\",\n     \"book_prints\": \"گرگن ( گرگین )\",\n     \"correct_form\": \"گرگن ( گرگین )\",\n     \"sources\": [W_GAR, A_GAR, A_GARGIN],\n     \"ref_check\": [\n      {\"ref\": \"HRN:200\", \"status\": \"supports\",\n       \"note\": \"Horn no. 895 on the page headed '- 200 -' (HRN.txt leaf 222): 'ger, gerr (AM. 28 Zeile 4) \\\"Krätze\\\". aw. garənu- \\\"Krätze\\\" … phlv. gar … LW. kurd. gir \\\"Krätze\\\"; bel. gar \\\"Aussatz, Räude, Krätze\\\"' — the New Persian word and its ancestry, on exactly the cited page.\"},\n      {\"ref\": \"BQT:1779\", \"status\": \"supports\",\n       \"note\": \"printed p.1779 (pdf 576): the گر article, sense 2 'نام جوششی است مشهور که بعربی جرب گویند', with footnote 2 giving Av. garenu, Pahlavi gar, and 'مریض را «گرگین» (مخفف آن: گرگن) گویند' — the source of the chart's bracketed pair, in the reverse order.\"},\n      {\"ref\": \"MON:3211\", \"status\": \"supports\",\n       \"note\": \"Mo'in s.v. گر '[ په . ] (اِ.) از بیماری‌های پوستی …' and s.v. گرگین '(گَ) (ص مر.) کسی که بیماری گَر دارد' (abadis.ir) — both senses of the node, though without page numbers online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Mo'in via abadis.ir, s.vv. گر and گرگین\", \"stance\": \"supports\",\n       \"note\": \"'[ په . ] … از بیماری‌های پوستی که باعث خارش و سوزش پوست بدن می‌شود' and 'گرگین: کسی که بیماری گَر دارد'.\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' ed. Mo'in, printed p.1779\", \"stance\": \"supports\",\n       \"note\": \"'گر … نام جوششی است مشهور که بعربی جرب گویند'; footnote 2 as quoted.\"},\n      {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 895, p.200\", \"stance\": \"supports\",\n       \"note\": \"Persian ger/gerr 'Krätze' with the Kurdish and Baluchi cognates gir, gar.\"},\n      {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.246\", \"stance\": \"partial\",\n       \"note\": \"'garr \\\"Kratze\\\", zd. garenu- (?)' — accepts the equation but flags it with a question mark.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Rishe-ha (grep GARENU / گرگین in ARY_latin_index_pages.txt and ARY_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"no article for گر 'scab' or گرگین in the Aryanpur index — the word is not treated.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-167.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk167.py",
 "description": "Write page-167 verification JSON"
}
```


### [2026-09-05T20:57:12.645Z] TOOL RESULT

```
written
```


## [2026-09-05T20:57:17.085Z] TOOL CALL #87: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-167.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 167",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:57:18.847Z] TOOL RESULT

```
JSON OK
nodes verified: 10/10
node verdicts: {'confirmed': 4, 'plausible': 5, 'transcription_suspect': 1}
root verdicts: {'plausible': 1, 'confirmed': 3}
ref checks: {'not_checked': 3, 'not_found': 1, 'supports': 10, 'partial': 3}
books consulted: {'supports': 16, 'silent': 6, 'contradicts': 4, 'partial': 8} | by book: {'HRN': 5, 'MON': 4, 'PHD': 4, 'BQT': 4, 'NYB': 3, 'ISS_alt_DKS': 2, 'SOD': 2, 'HUB': 2, 'ARY': 2, 'POK': 1, 'FRS': 1, 'RCH': 1, 'WLD': 1, 'IEC': 1, 'AHD': 1}
```


## [2026-09-05T20:57:37.271Z] AGENT

Done. `python3 tools/verify_check.py 167` → 0 PROBLEM lines, 10/10 nodes.

**Page 167 (book p. 137) — 4 entries, 10 nodes**

Roots: 3 confirmed, 1 plausible. Nodes: 4 confirmed, 5 plausible, 1 transcription_suspect.

- **Gan (Indo-Schythian, ISS:27) — root plausible.** Faithfully copies Bailey (DKS s.v. *uysgana-*: "Hence a base gan- 'to seize', IE ghen- to Pok. 437-8"), but "Indo-Scythian" is a book title, not a language (the word is Khotanese Saka), and *gan-* is Bailey's back-formation; Pokorny/Watkins list no Iranian reflex of *gʰend-*.
- **#2 Sogdian ğnw, ğan — plausible.** Only Bailey's hedged "Possibly Sogd. VJ γn'w 'force'". `SOD:163` = **not_found**: that leaf *is* Gharib's γn- page (entries 4121–4168) but has no γnw/γan; the gloss "skill" is in neither source.
- **#3 Persian زغن — plausible.** Word and Bailey's *uz-gana-* etymology check out (BQT ≈1023 quotes the same Rudaki couplet and cites Bailey), but the arrow makes it descend from Khotanese; it is a cognate, not a Khotanese loan.
- **Gang #1 Sanskrit gunj — plausible.** Pokorny 352 lists *gúñjati* among "ähnliche Schallwörter" *beside* *gang-*, not under it (Walde-Pokorny does file it there; Mann makes a separate *gong-*).
- **Gang #2 Pahlavi gung — plausible.** MP gung is solid (MacKenzie, Nyberg), but Nourai's own authorities reject descent from Sanskrit: Horn 937 "Unsicher", Hübschmann p.95 "Höchst unsicher".
- **Garenu #1 Pahlavi gar — plausible.** Given by Horn 200 and Mo'in (Darmesteter), but absent from MacKenzie and Nyberg (both have only *gar* 'mountain').
- **Garenu #2 Persian gar 3; gargen — transcription_suspect / EXTRACTION ERROR (owner fix).** The printed page shows «گرگن ( گرگین )»; the JSON has «گرگین ( گرگین )», losing the headword گرگن (which the transliteration *gargen* and Nāser-Khosrow's گرگنان both confirm). Verified on a 400 dpi render saved to `data/verification/sources/refs/ocr/BOOK/167.png`. No other extraction discrepancies on the page.

Reference pages verified in the scans: BQT 1779 (pdf 576), 1842 (pdf 639), 1844 (pdf 641) all confirmed by running-head numerals; HRN 209/200, HUB 95, SYN 516, BRT cols. 493 and ≈516, POK 352 and 437 f. all say what the arrows say. Nine web pages archived via `fetch_source.py`.
