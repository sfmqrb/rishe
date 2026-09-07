# Verification process log — verify-page-315


## [2026-09-07T01:37:03.655Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 315 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-315.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-315.json. Write /home/sfmqrb/git/rishe/data/verification/page-315.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 315` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T01:37:05.483Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T01:37:06.143Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T01:37:06.159Z] TOOL RESULT

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


## [2026-09-07T01:37:07.016Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-315.txt"
}
```


### [2026-09-07T01:37:07.040Z] TOOL RESULT

```
1	=== PDF page 315 (book page 285) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Lrğ : to tremble  (refs IEC:1640)
4	#1 (parent #0) [Old Iranian] refs=FFD:75 | Rarz : to shake, shiver
5	  #2 (parent #1) [Pahlavi] refs=FFD:75; BQT:1894 | rrz, larz : shiver
6	    #3 (parent #2) [Persian] refs=BQT:1894; FFD:75 | larzîdan «لرزیدن (لرزاندن)» : to shiver ; larzesh «لرزش (لرزه ، زمین لرزه)» : shiver
7	#4 (parent #0) [Middle German] refs=IEC:1640 | lurken, lreken : shiver
8	--- entry 1 ---
9	ROOT Lu -> redirect to Leu
10	--- entry 2 ---
11	ROOT Lup -> redirect to Wel 2
12	
```


## [2026-09-07T01:37:10.629Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-315.json",
 "description": "Read source JSON for page 315"
}
```


### [2026-09-07T01:37:10.670Z] TOOL RESULT

```
{
  "pdf_page": 315,
  "book_page": 285,
  "entries": [
    {
      "root": {
        "name": "Lrğ",
        "lang": "Indo-European",
        "refs": "IEC:1640",
        "gloss": "to tremble"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Old Iranian",
          "refs": "FFD:75",
          "words": [
            {"translit": "Rarz", "gloss": "to shake, shiver", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "FFD:75; BQT:1894",
          "words": [
            {"translit": "rrz, larz", "gloss": "shiver", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:1894; FFD:75",
          "words": [
            {"translit": "larzîdan", "gloss": "to shiver", "script": "لرزیدن (لرزاندن)"},
            {"translit": "larzesh", "gloss": "shiver", "script": "لرزش (لرزه ، زمین لرزه)"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نه چون بید از تهیدستی دراین گلزار میلرزم - که از بیحاصلی میلرزم و بسیار میلرزم",
            "poet": "Sâeb"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Middle German",
          "refs": "IEC:1640",
          "words": [
            {"translit": "lurken, lreken", "gloss": "shiver", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {"name": "Lu", "redirect": "Leu"},
      "nodes": []
    },
    {
      "root": {"name": "Lup", "redirect": "Wel 2"},
      "nodes": []
    }
  ]
}
```


## [2026-09-07T01:37:12.528Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['IEC','FFD','FVD','BQT','POK','WLD','AHD','HRN','HUB','PHD','NYB','MON','ARY','CHEUNG','SYN','KLN','SKT']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\""
}
```


### [2026-09-07T01:37:13.731Z] TOOL RESULT

```
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

FVD null

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

CHEUNG null

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
```


## [2026-09-07T01:37:30.378Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -60; echo ---; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['IEC'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['FFD'],ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-07T01:37:31.629Z] TOOL RESULT

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
{
 "title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87",
 "edition_found": "1984-1987 (complete, cols./pp. 1-1682)",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987",
 "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt",
 "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.",
 "notes": "",
 "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"
}
{
 "title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995",
 "kind": "local_scan_ocr",
 "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)",
 "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"
 ],
 "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).",
 "covers_etymology": true,
 "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Entries: headword, then 'فارسی میانه ... < ایرانی باستان *...' with Latin transliterations (best read in *_pages_faseng.txt or on the page image). | OCR text, printed = pdf-5"
}
```


## [2026-09-07T01:37:32.255Z] TOOL CALL #6: Bash

```json
{
 "command": "pdftoppm -f 315 -l 315 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg315 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T01:37:34.126Z] TOOL RESULT

```
total 64
drwx------ 2 sfmqrb sfmqrb  4096 Sep  6 21:37 .
drwx------ 3 sfmqrb sfmqrb  4096 Sep  6 21:35 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   175 Sep  6 21:37 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 49502 Sep  6 21:37 pg315.png
```


## [2026-09-07T01:37:37.165Z] TOOL CALL #7: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg315.png"
}
```


### [2026-09-07T01:37:37.661Z] TOOL RESULT

```

```


## [2026-09-07T01:37:37.659Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-07T01:37:56.551Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(len(leaves))\n# target printed page 1640 -> leaf ~ 1640/2+15 = 835\nfor n in (833,834,835,836,837):\n    L=leaves[n]\n    print('=== leaf',n, L[:200].replace('\\n',' | '))\nEOF"
}
```


## [2026-09-07T01:37:57.344Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"lurken|lerken|l.rken\" IEC.txt | head -20; echo \"--- larz\"; grep -n -i -E \"larz|lrz\" IEC.txt | head -20"
}
```


### [2026-09-07T01:37:57.773Z] TOOL RESULT

```
858
=== leaf 833 utifully’; Sw. vän, adj. ‘pleasant’; Li. vēnios, fpl. ‘strength’. (Isophonic: Latv. pa- vēnis ‘shade, shadow, shelter’) | uën- (2) “lacking, defective, immature; lack’, etc. Cf. uän-. Gk. ambig. Hom. Cf
=== leaf 834 ) joy’; OE wynn, f. ‘delight’; cf. wyn-sum ‘winsome’. (FK:EWDS untenable: Wonne). See next | 1515 | uénskKó ‘desire’. Cf. uenos, -es-, and uén- (1). WP I, 259 Skt. vafncami, v. id.; Du. wenschen, mod. wen
=== leaf 835 ņemt, v. ‘take heed’; | uer- (3) (uero, ið) ‘speak’. Cf. ueru-, uoru-. WP I, 283 Hitt. weriyami, v. “call, invite’; Gk. eíro, v. “say, speak, tell; éromai, v. "ask | uer- (4) (?) *up, upon' Per. bar, adv.
=== leaf 836 ‘work’; (denom. in) OHG wérkon, w&rchon, v. "work do’; Swiss werchen, id.; Du. werken, id.; OE weorcan, id. beside (z-gde) wyrcan, id.; ON verka, v. ‘work’; Alb. virdhem, v. ‘gain a skill, win sympath
=== leaf 837 nus ‘barrier’; Br. gwern, pl. -iu, f. 'ship's mast’; W gwernen, pl. gwerni, f. id.; Cor. gwern, pl. gwernow, f. id.; ON vorn, f. beside vernd, f. ‘defence’; Sw. värn, n. id.; Finn. (LW) varras, s. ‘sp
```


### [2026-09-07T01:37:57.824Z] TOOL RESULT

```
9688:lergo (?) Per. larzidan, inf. ‘tremble’; larze, s. ‘tremor’; MHG, MLG lérken, lirken ‘stammer’. (Iso- phonic Icel. lerkaóur is ‘bruised, sore. MHG lérc & lirc is "left-hand; lame). Ir. learg is “plain, track, road; slope”, and leirg, f. is “path; reason?)
--- larz
9688:lergo (?) Per. larzidan, inf. ‘tremble’; larze, s. ‘tremor’; MHG, MLG lérken, lirken ‘stammer’. (Iso- phonic Icel. lerkaóur is ‘bruised, sore. MHG lérc & lirc is "left-hand; lame). Ir. learg is “plain, track, road; slope”, and leirg, f. is “path; reason?)
```


## [2026-09-07T01:38:10.584Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 9688\nidx=9687\npre='\\n'.join(lines[:idx+1])\nleaf=pre.count('\\f')\nprint('leaf index of lergo line:',leaf)\nleaves=t.split('\\f')\nL=leaves[leaf]\nprint(repr(L[:3000]))\nEOF"
}
```


### [2026-09-07T01:38:11.911Z] TOOL RESULT

```
leaf index of lergo line: 384
'cf. penplepios \'spurge-laurel, lit. “five leaves\', from its terminal cluster; Ir. leo, m. ‘film, esp. of oil on water’; Slovene f. lepen, m. “leaf”; R cf lépestt, f. “strip; petal; Srb. cf. lepetati, inf. ‘flutter’\nlép- (?) MHG lāb if distinct from là, gs lawes, see leuis (1) “mild, of weather’; Li. lépis, m. *dawdler\'; lepti, inf.; lepstà 1sg. ‘flag, be limp’; cf. Latv. lépot, inf. ‘dawdle’ (with expressive initial ]-)\nlerdos (?) ‘clumsy, awkward’. Cf. lurd-. (Variant: lordos ?) Sp. lerdo ‘ponderous, clumsy, heavy’; MHG lërz “awkward, left-handed\' beside lérzen, v. ‘stammer’. Cf. (?) Gk. lordós “bent?\nlergo (?) Per. larzidan, inf. ‘tremble’; larze, s. ‘tremor’; MHG, MLG lérken, lirken ‘stammer’. (Iso- phonic Icel. lerkaóur is ‘bruised, sore. MHG lérc & lirc is "left-hand; lame). Ir. learg is “plain, track, road; slope”, and leirg, f. is “path; reason?)\nlés- (lesa, ós, ióm) (?) “place, space, area, room” Per. -lax, cpds. “-place\'; OHG cf. gi-lari, n. ‘room, dwelling’; Icel. lár *ditty-box\'; Sw. lår, m. ‘box, drawer’; LW in R lari; Latv. lēsa ‘ayot, mudfiat\'. (Isophonic: ON láss ‘lock; arrow,\n681\nbolt’: Sw. lås, n. ‘lock’)\nleskos (ledskos ?) ‘feeble, limp’. Cf. los-quos (Iks-) Ir. leasc, adj. id.; OW & W llesg ‘feeble, slug- gish’; llesgu, tr. ‘weaken? OHG lëskan, sv A ‘die out; MHG léschen, sv 4, id. (FK: EWDS: lóschen untenable)\nleso, ið ‘peck, pick, gather, read WP II, 440 Skt. rasàmi, rasyāmi (taste, feel, sample’. Ambig.); Go. lisan, sv. 5 “gather”; MHG lésen, sv 5 “gather, choose, read, tell’; OE lesan ‘pick, glean’; ON lesa ‘pick; catch; read”; Li. lesu, lésti ‘peck, pick’; Latv. lešu, lest ‘reckon, count? beside (o-gde) sa-lasit, inf. ‘gather up’; sa-lasas, fpl. ‘scraps, gleanings\'\nletos, is (let-) “free, Easy; ease’ ; Skt. ratáh *bestowed"; ratih ‘generous, favour- able’; Br. līt, lid, pl. -u, m. “fate; joy; caress’; Go. cf. un-léps, -léds “poor, disowned\'; un- ledi, n. ‘poverty’; OE un-ldéd “abandoned, stray’; un-lædu (w. non-historic -u, f. *mis- ery’); OCS læti, phr: — jesti “it is allowed’; lótije, n. ‘facility’; Li. lētas ‘slow, easygoing, soft, quiet, meek’; Latv. lēts ‘cheap’; short vowel in MHG lëdig ‘free’; LW in Finnish: lieto “soft, tender, gentle". (The background of Lat. laetus ‘fortunate’ and lētum ‘death’ is uncertain, as also that of OCS lëto ‘sum- mer’. LLat. laetus ‘liege’, as also OFr. lige, id. is a Gmc. type *leþigas: G ledig). The iso- phone OE Leo n. ‘county division’; ON láð, n. ‘land’; G Lehde, f. ‘upland, high plateau? is reflected in the LLat. LW leta *court-leet". Blg. letăv ‘horizontal’ is without an etym.)\nletros, å ‘piece, strip, skin”; letró, io ‘strip, flay, têar’. WP II, 428 Per. latre ‘part, fragment’; Gk. cf. ko-letráo (‘trample’, if ko- is a px.); Ir. leathar, m. “skin, hide’; W lledr, m. id. (and “leather?); Br. ler, lezr, m. id.; Mir. cf. letraim, v. ‘mangle, téar\'; MHG léder, n.; OE -leóer, leóer-, cpds. ‘eather’; MHG cf. l&deren, lideren, v. ‘tan’\nleubh, leubhi ‘rather, or’. See next Osc. loufi, lo'
```


## [2026-09-07T01:38:25.930Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,L in enumerate(leaves):\n    if re.search(r'(?m)^\\s*1640\\s*$', L) or re.search(r'(?m)^\\s*164[01]\\s*$',L):\n        print('leaf',i)\n        print(L[:1500])\n        print('...')\n        break\n# also which leaf has marker 681\nfor i,L in enumerate(leaves):\n    ms=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',L)\n    if i in (383,384,385):\n        print(i, ms)\nEOF"
}
```


### [2026-09-07T01:38:27.322Z] TOOL RESULT

```
383 ['679', '680']
384 ['681', '682']
385 ['683']
```


## [2026-09-07T01:38:31.985Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i in list(range(835,845))+[855,856,857]:\n    L=leaves[i]\n    ms=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',L)\n    head=L[:80].replace('\\n',' ')\n    print(i, ms, '|', head)\nEOF"
}
```


### [2026-09-07T01:38:33.209Z] TOOL RESULT

```
835 ['1517', '1518'] | ņemt, v. ‘take heed’; uer- (3) (uero, ið) ‘speak’. Cf. ueru-, uoru-. WP I, 283 H
836 ['1519', '1520'] | ‘work’; (denom. in) OHG wérkon, w&rchon, v. "work do’; Swiss werchen, id.; Du. w
837 ['1521'] | nus ‘barrier’; Br. gwern, pl. -iu, f. 'ship's mast’; W gwernen, pl. gwerni, f. i
838 ['1522', '1523'] | ag’; Lat. verro, ére, OLat. vorro ('drag, trail; sweep, brush”, uerpo — uertos 1
839 ['1524', '1525'] | a dike’; G Werd, m. “island, coastal strip’; Ukr. vereta, f. ‘blanket. (Go. wair
840 ['1526', '1527'] | , wasami, wasiyami, wasemi, v. ‘put on — clothes’; Gk. Ion. heimai, 2s: héssai, 
841 ['1528', '1529'] |  id. cf. Li. ve-du, id. ues- (2) “breath, air, breeze, cool, fragrance’. WP I, 2
842 ['1530'] |  Cf. ues- (2). WP I, 222 Skt. vasanam, n. ‘fumigation, scenting'; Gk. cf. á-ëma,
843 ['1531', '1532'] | r-old, annual; yearling'. Cf. uetos. WP I, 251 Skt. vatsáh, m. ‘calf, young anim
844 ['1533', '1534'] | ‘crossbar, bail’ beside LLat. vibra, id.; W gwif, pl. -ion, m. "lever, bar; LG w
855 ['1552', '1553'] | Lat. liquor, gs: -óris, m. ‘fluid’; MIr. & Ir. fliuch *wet'; OBr. gulip & guilp,
856 ['1554'] | bulga is ambig. Skt. várgā ‘sect, class’ seems to be unrelated) (ulio (1) ‘wind,
857 [] | (1) only in Skt. ürnómi, v. ‘envelop’; (2) only in Gmc. cf. Go. wulan and OE wyl
```


## [2026-09-07T01:38:57.660Z] TOOL CALL #13: Bash

```json
{
 "command": "curl -s \"https://ia-petabox.archive.org/services/search/beta/page_production/_search/?q=%22larzidan%22&search_type=inside&identifier=mann-an-indo-european-comparative-dictionary-1984-1987\" -m 60 | head -c 2000; echo; echo \"=== metadata\"; curl -s -m 60 \"https://archive.org/metadata/mann-an-indo-european-comparative-dictionary-1984-1987\" | python3 -c \"\nimport json,sys\nd=json.load(sys.stdin)\nfor f in d.get('files',[]):\n    print(f.get('name'), f.get('size'))\n\" | head -30"
}
```


### [2026-09-07T01:38:59.337Z] TOOL RESULT

```
=== metadata
Mann - An Indo-European Comparative Dictionary (1984-1987).epub 2121286
Mann - An Indo-European Comparative Dictionary (1984-1987).pdf 75622175
Mann - An Indo-European Comparative Dictionary (1984-1987)_chocr.html.gz 51141410
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.txt 3698758
Mann - An Indo-European Comparative Dictionary (1984-1987)_djvu.xml 45262215
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr.html 93307559
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_pageindex.json.gz 10999
Mann - An Indo-European Comparative Dictionary (1984-1987)_hocr_searchtext.txt.gz 1486201
Mann - An Indo-European Comparative Dictionary (1984-1987)_jp2.zip 1165905241
Mann - An Indo-European Comparative Dictionary (1984-1987)_page_numbers.json 171319
Mann - An Indo-European Comparative Dictionary (1984-1987)_scandata.xml 275575
__ia_thumb.jpg 6096
mann-an-indo-european-comparative-dictionary-1984-1987_archive.torrent 31962
mann-an-indo-european-comparative-dictionary-1984-1987_files.xml None
mann-an-indo-european-comparative-dictionary-1984-1987_meta.sqlite 20480
mann-an-indo-european-comparative-dictionary-1984-1987_meta.xml 1446
```


## [2026-09-07T01:39:06.685Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && curl -s -m 120 -o iec_pages.json \"https://archive.org/download/mann-an-indo-european-comparative-dictionary-1984-1987/Mann%20-%20An%20Indo-European%20Comparative%20Dictionary%20%281984-1987%29_page_numbers.json\" && python3 - <<'EOF'\nimport json\nd=json.load(open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/iec_pages.json'))\npages=d.get('pages',d)\nprint(type(pages), len(pages))\nnums=[(p.get('leafNum'),p.get('pageNumber')) for p in pages]\nprint(nums[:5]); print(nums[-8:])\nmx=[n for n in nums if n[1] and str(n[1]).isdigit()]\nprint('max printed', max(int(n[1]) for n in mx))\nfor leaf,pn in nums:\n    if pn and str(pn).isdigit() and 1636<=int(pn)<=1644:\n        print('leaf',leaf,'page',pn)\nEOF"
}
```


### [2026-09-07T01:39:09.007Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/usr/lib/python3.12/json/__init__.py", line 293, in load
    return loads(fp.read(),
           ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```


## [2026-09-07T01:39:11.508Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && head -c 300 iec_pages.json; echo; file iec_pages.json"
}
```


### [2026-09-07T01:39:11.555Z] TOOL RESULT

```
iec_pages.json: empty
```


## [2026-09-07T01:39:39.474Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in CHEUNG.txt PHD.txt NYB_vol2_glossary.txt HRN.txt HUB.txt SYN.txt AHD_watkins1985.txt; do echo \"=== $f\"; grep -n -i -E \"larz|rarz|lrz\" $f | head -12; done"
}
```


### [2026-09-07T01:39:40.689Z] TOOL RESULT

```
=== CHEUNG.txt
3539:*NWIR: NP Candis ‘severe tremor’, Delij. čandeš ‘tremble, larzis’, also borrowed in 
5164:polarz-/palisé-, M. polörz- ‘to wrap up (a bundle) || (+ *ni-) Sh. nióuyj ‘woollen yarn 
12927:9 See also *rarz. 
20456:it is due to the influence of Pers. larzidan ‘to shake, tremble’ (*rarz) ? An IE 
20656:*rarz ‘to shake, tremble’ 
20657:*MIDDLE PERSIAN: BMP llc- /larz-/ ‘to shake, tremble’, MMP mz ‘(fever’s) 
20661:Pres.: IND. 3sg. BMP Ilcyt /larzed/, 3р1. BMP Ilcynd /larzend/ 
20684:*NWIR: NP Jarzidan, Kurd. larzin/larz-, (also Sor.) larzän/larze-, Zaz. lerzäyis/ 
20685:lerzen-, Gz. lärz-/lärzä, Gur. (Kand) -lärüä-, Khuns. lerz-/lerza, Tal. larze ‘to shake, 
35306:llc- /larz-/, 314 
39351:wlrz (C), 314 
41150:larzidan, 311, 315 
=== PHD.txt
432:— h: supplication. lajan [/cn! | N ~] mud, slime. larzidan, larz- [ilc-ytn' | P Irz-, N ~] shiver, tremble. laškar [ISk] | N ~] army.
3633:shiver larzidan.
4064:tremble Candidan, drafšīdan, larz- idan.
4913:rag атат, sīhom” hazārag* larz- larzīdan ram abgan-! abgandan! ramag ras- rascn- rasenidan rahig rasidan rastarih rastan rastag
=== NYB_vol2_glossary.txt
2349:larzitan [lleytn'] to tremble 58%, — MPrthPrs Irz-, MPrs also rrz ‘to shiver with fever’, List 87; NP larzidan.
7251:larzīdan: larzītan
=== HRN.txt
5710:zad 'Geburt' {-zad, mlrzä), zaj^ zaje 'Wöchnerin*,
7864:wa;^. LW. gilrz,
=== HUB.txt
=== SYN.txt
11444:OFr. miradoir, mireor, mirour (> ME mirour, NE mirror), Fr. miroir, fr. *mirdtorium, deriv. of Lat. mirare (mirarz) ‘wonder at’ in the later sense of ‘look’ as in It. mirare, Fr. mirer, etc. (15.52). REW 5603. NED s.v. mirror.
11485:Lat. morart, démorart ‘delay’ (14.24), in VLat. also ‘dwell’ (so mordrz and commorarz in Peregrinatio), whence Sp. morar ‘dwell’, It. dimorare, Fr. demeurer ‘remain’ and ‘dwell’. Wartburg 3.38 f.
13639:3. Lat. opus (sometimes abstr., most- ly coner.), opera (mostly abstr., but concer. in derivs. It., Rum. opera, Fr. @uvre, Sp. obra), whence vb. operarz,
15172:Grk, rherey rd unis os Ne ae es . a ae limrja Lith. murininkas * — (faber steinsmidr Lett. mérnieks ee Cee Dan. murer ChSl. .... g, Macon Sw. —- murare SCr. zidar Rim oat OE _stanwyrhta Boh. zednik ik a. 2idar ME — machun Pol. = mularz Nh, “ir NE mason Russ. kamenStik W, %°r cloiche a metselaar Skt. _ lepaka- saat ony Stn ar pe NHG maurer
15200:Pol. mularz, by dissim. fr. murarz, deriv. of mur ‘wall’, fr. Gme., cf. OHG mitra, ete. (above, 4). Briickner 348.
15907:k twpados ON (skrifari) Lett. gleznuotojs a garyphdos Dan. maler Chsl Fee N t. _ piclor Sw. mdlare SCr. — slikar e " piltore OE métere Boh. mali ir peintre ME peyntour Pol. malarz Sp. pintor NE painter Russ. Zivopisec Rum. piclor Du. schilder Skt. citrakara- jij aro OHG = madlari Ay. ; NIr. Hie MHG madlere a Por, penter NHG = maler
15963:Rum. lucru ‘work, act’ and ‘thing’, fr. Lat. lucrum ‘gain’. Sense of ‘work’ through vb. lucra (Lat. lucrarz) ‘gain’ (by work) > ‘work’, but generic ‘thing’ by Slavic influence. Cf. Bulg. délo and rabota both ‘work’ and ‘thing’. Tiktin 927f. REW 5146.
18411:Grk. —vabrns Goth. .... Lith. jureivis, jurininkas NG vabrns ON skipari, skipamadr, Lett. jurnieks, kug'inieks Lat. nauia sjomaér ChSl.  (morjaninit) It. marinaio, marinaro Dan.  s¢mand, matros SCr. _mornar, brodar Fr. marin, matelot Sw. sjéman, matros Boh. ndmo*ntk, plavec Sp. marinero, marino OE scipmann, scipere, Pol. zeglarz, marynarz, Rum. marinar, matelot s@lipend majtek Tr. noaire, loingseach ME _ schipman, seman, Russ. morjak, matros Nir. mairnéalach mariner Skt.  navika- W. morwr, llongwr NE sailor, seaman (mari- Av. ae Br. merdead, martolod ner)
18448:Pol. zeglarz, fr. NHG segler ‘sailer’, also ‘sailor’ (: segeln ‘sail’). Briickner 660 f.
=== AHD_watkins1985.txt
```


## [2026-09-07T01:39:40.776Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls incoming/FFD/ && echo \"=== fas+eng grep larz\" && grep -n -i -E \"larz|rarz|lrz\" incoming/FFD/FFD_pages_faseng.txt | head -20; echo \"=== fas grep لرز\"; grep -n \"لرز\" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-07T01:39:40.869Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
=== fas+eng grep larz
ugrep: warning: incoming/FFD/FFD_pages_faseng.txt: No such file or directory
=== fas grep لرز
714:بدل شده است. ريشةٌ 35800 به معنی «لرزیدن» است. «آشوفت» زیر نفوذ «آشوب»
1352:«هیجان‌داشتن» و 2۵۵414۵8 به معنی «لرزیدنْ» است.
1869:0 صورت ضعیف ريشهٌ 35200 است. ريشهٌ 5200*به معنی «لرزیدن» است. «آشفتن)
2057:لرزیدن
2058:لرزید < فارسی میانه 1272۵» مادةٌ ماضی جعلی و از مادةٌ مضارع ساخته شده است.
2059:لرز + فارسی میاته 1372 + ایرانی باستان ۲۵۲2-۵*. برای 2 آرای.
2674:۷۳/۵ ناهگه: (ريشه < لرزیدن) ۰۲۶ ۶۹
```


## [2026-09-07T01:39:52.337Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/FFD/FFD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nidx=2056\npre='\\n'.join(lines[:idx+1]); leaf=pre.count('\\f')\nprint('pdf page (leaf+1):', leaf+1, ' printed:', leaf+1-5)\npages=t.split('\\f')\nprint(pages[leaf][:1200])\nEOF"
}
```


## [2026-09-07T01:39:53.549Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '20640,20700p' CHEUNG.txt; echo \"=== ref to 314/311 lines\"; sed -n '12920,12930p' CHEUNG.txt"
}
```


### [2026-09-07T01:39:53.909Z] TOOL RESULT

```
pdf page (leaf+1): 80  printed: 75
[pdf page 80]
ماده‌های ماضی و مضارع فارسی دری وی

گفت < فارسی میانه +801 < ایرانی باستان 80-42 *. برای 12 -> آراست. 6۵0 صورت
اصلی ۶باع است» ۳ پیش از 1 به ؟ بدل شده است. 90ع صورت ضعیف ريشهٌ 8200 به
معنی «گفتن» است.

گوی + فارسی میانه 83۷ < ایرانی باستان 8200-2*. برای ۵ > آرای.

گماردن. گماشتن

گمارد < فارسی میانه ۰8070370 (گماشت) در فارسی دری به قیاس با «کاشت».
«کار» به وجود آمده است.

گمار + فارسی میانه ۰801037

گواردن

گوار + فارسی میانه 6۳837 < ایرانی باستان ۷1-127-۵*. برای 2-> آرای. 137 صورت
بالاندةٌ ريشهٌ ۴۵۲ به معنی «کردنْ» است. ۷۷1 پیشوند فُعلی است.

مادهٌ ماضی در فارسی میانه 8083770 بوده که جعلی است. «گوارد» فارسی دری
بازماندة ۹1-137-1۵* ایرانی باستان است. برای 1۵ -> آراست.

گوالیدن (:بالیدن)

گوال < ایرانی باستان ۷3۲4-2-/۷*. برای ۵ -> آرای. ۷ پیشوند فعلی است. ۷۷374
صورت بالاندةٌ ۷۵7۵ به معنی «بالیدن» است و خود («بالیدن» هم از ۷۵7۵ آمده است >
بالیدن.

لرزیدن
لرزید < فارسی میانه 1272۵» مادةٌ ماضی جعلی و از مادةٌ مضارع ساخته شده است.
لرز + فارسی میاته 1372 + ایرانی باستان ۲۵۲2-۵*. برای 2 آرای.
```


### [2026-09-07T01:39:53.983Z] TOOL RESULT

```
*rap/f ‘to help, assist, support’ 
*AVESTAN: rap- ‘to help, assist’ = Liste: 56 
Pres. them.: ОРТ. Zeg. OAv. rapöis (Y 41.4), IMPV. 25р. OAv. агара (Y 49.1); Partic.: pres. rapant- 


*KHOTANESE: Khot. tcarampha- ‘staff, stick’ || (+ *pati-) parah- (parih-) ‘to be 
established’, LKh. pariph- (caus./tr.) ‘to establish’, paraha- ‘support’? = SGS: 81 f. 
9 Further Ir. cognates are unknown. 


“PIE LIV: - | Pok.: 
*REFERENCES: EVP: 65; IIFL II: 259a, 420a, 549a; Abrahamian 1936: 124, no. 63; EVS: 91a; Puhvel III: 
176 ff.; Steblin-Kamenskij 1999: 398 


*rarz ‘to shake, tremble’ 
*MIDDLE PERSIAN: BMP llc- /larz-/ ‘to shake, tremble’, MMP mz ‘(fever’s) 


shivering, ague’ > DMMPP: 296b 
Pres.: IND. 3sg. BMP Ilcyt /larzed/, 3р1. BMP Ilcynd /larzend/ 


*PARTHIAN: Irz- ‘to tremble’ || (+ *ui-) wirz- ‘to tremble’ = Ghilain: 52 | DMMPP: 


222b, 342b 
Pres.: IND. Isg. Irz’m, 1р1. Irz’m, 3р1. “глупа || (+ *ui-) Partic.: perf. pass. П wirz’d 


*SOGDIAN: (+ *ui-) BSogd. wyr’rz, CSogd. wirz, CSogd. wdrz ‘to tremble, shake’ 


(cf. GMS: §60, fn.) 
Pres.: IND. 3sg. BSogd. wyr’rzt (P2 9 R.411), CSogd. wirzt, 2pl. CSogd. wdrzt’sqn 


*CHORESMIAN: (+ *abi-) Brzyk ‘shaking fever, ague’ 


*raub 315 


*NWIR: NP Jarzidan, Kurd. larzin/larz-, (also Sor.) larzän/larze-, Zaz. lerzäyis/ 
lerzen-, Gz. lärz-/lärzä, Gur. (Kand) -lärüä-, Khuns. lerz-/lerza, Tal. larze ‘to shake, 
tremble’ 

*NEIR: Pash. reZdedol ‘to tremble, quiver’, Sh. réyj-/ryzd ‘to tremble, shiver’, (Baj.) 
rayja ‘trembling, fever, ague’, Yzgh. riwz-/rawzd ‘to tremble, shiver’, Yzgh. riwza, 
Rosh. rawza ‘trembling, fever, ague’, Pash. larye ‘trembling’ 

*SANSKRIT: — = EWAia II: 458 

© This Ir. root may be related to *Hraiz. The initial /- found in the Wir. forms is 


probably the result of dissimilation of two homosyllabic r... r$: 1 ...r$. 
*REFERENCES: EVP: 65; KPF II: 222; Henning 1971: 11а; EVS: 67a; WIM I: 70; WIM ПЛ: 79; Paul 
1998: 304b; Cabolov 2001: 578 f. 

=== ref to 314/311 lines
*NEIR: Oss. I. rizyn/ryzt, D. rezun/rizt ‘to shake’, Pash. reZdedol ‘to shake, tremble’ || 
(+ *aua- or *ui-) ? Yi. uriz-/urizd ‘to spread manure’ || (+ *pati- ?) Sariq. piraxt, 
puraxt ‘cradle’. 0 Yi. uriz-/urizd is assigned a different etymology by Morgenstierne, 
ПЕТ ПП: l.c. 

*SANSKRIT: rej ‘to shake, to tremble’ (RV+) = EWAia II: 458 f. 

9 See also *rarz. 

«PIE *Hileié- ‘to shake’ = LIV: 246 f. | Pok.: 667 f.
```


## [2026-09-07T01:40:12.238Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re,glob\nfor fn in ['POK_01.txt','POK_02.txt','POK_03.txt']:\n    try: t=open(fn,encoding='utf-8',errors='replace').read()\n    except FileNotFoundError: \n        print('missing',fn); continue\n    print(fn, 'leaves', t.count('\\f')+1)\nEOF\nls POK*; echo ---; python3 -c \"\nimport json\nd=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('local_file')); print(d['POK'].get('lookup_hint'))\""
}
```


### [2026-09-07T01:40:13.507Z] TOOL RESULT

```
POK_01.txt leaves 364
POK_02.txt leaves 434
POK_03.txt leaves 430
POK_01.txt
POK_02.txt
POK_03.txt
POK_full.txt
---
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


## [2026-09-07T01:40:16.652Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"lemma: .*(leig|lerg|elǝg|reig)\" POK_full.txt | head -20; echo \"=== page 667\"; grep -n -B3 -A6 \"Page(s): 66[6-9]\" POK_full.txt | head -80"
}
```


### [2026-09-07T01:40:16.731Z] TOOL RESULT

```
14563:Root/ lemma: b'^leig-, b'"ng-{*b^\e\g-) 
47526:Root / lemma: kleg-, klog- klag-, klang- kleg-, klog- kleig- kleik- 
48306:Root / lemma: krei-2, kreig-, kreik- 
54390:Root/ lemma: /ehig-l and /ehik- beiier oleig-/k-{*lehu^ Note: common Proto Germanic -u- 
69863:Root / lemma: reig- or reig- 
69897:Root / lemma: {reig-), reig- 
77999:Root / lemma: (s)leig- 
80594:Root / lemma: sp(h)reig- 
80653:Root / lemma: (s)pleigh- 
80806:Root / lemma: (s)reigh- 
83110:Root / lemma: streig-1 
83132:Root / lemma: streig-2 
83151:Root / lemma: (s)treig-3, streid(h)- 
87122:Root / lemma: treig- 
91860:Root/ lemma: uer-3. I. ur-ei- y) ureig- {* huer-3) 
=== page 667
54366-
54367-See also: see below /e//?-/ "besmear'. 
54368-
54369:Page(s): 666 
54370-
54371-Root/ lemma: leid-{*lehud-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
54372-Meaning: to play, joke 
54373-
54374-Material: Gr. Ai^si rrai^si, Ai^ouai "rrai^ouai Hes. (from *Aiv5ju), compare Aiv5£a9ai 
54375-aiJiAAaoGai Hes.); Aoi5opo(; " scolding ', AoiSopsu) ' abuse, revile, scold ' (compare to 
--
54385-perhaps Middle Irish laidid{*loid-) " stimulates, invigorates, sings '. 
54386-
54387-References: WP. II 402, WH. I 829 f. 
54388:Page(s): 666 
54389-
54390-Root/ lemma: /ehig-l and /ehik- beiier oleig-/k-{*lehu^ Note: common Proto Germanic -u- 
54391-> -U-, -y-, -/-. 
54392-
54393-
54394-
--
54423-
54424-References: WP. II 398, Trautmann 161; 
54425-See also: probably to lei-2. 
54426:Page(s): 667 
54427-
54428-Root/ lemma: lehig-3, lohig-{*lehu^ Note: common Proto Germanic -u- > -u-, -y-, -/-. 
54429-Meaning: to jump; to tremble 
54430-
54431-Material: Old Indie rejati^ makes jump, allows to tremble ', rejate^ jumps, shakes ', rejayati 
54432-" makes tremble, shake '; 
--
54454-Lithuanian /a/gyt/' run around wildly ', verbal noun laigymas. 
54455-
54456-References: WP. II 399, Trautmann 148. 
54457:Page(s): 667-668 
54458-
54459-Root / lemma: lehig-4, lehig-{*lehu^ Note: common Proto Germanic -u- > -u-, -y-, -/-. 
54460-
54461-Meaning: to bind, *vow, make an oath 
54462-
54463-Material: Alb. lith, //dhPass. //c/hem 'b'\nd, bandage, gird ', //dhe, Mhe^band, strap, chain; 
--
54489-
54490-
54491-References: WP. II 400, WH. I 800. 
54492:Page(s): 668 
54493-
54494-
54495-
54496-Root / lemma: lehigh-, slehigh-{*lehugh-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
54497-
54498-Meaning: to lick 
--
54543-
54544-f. 
54545-
54546:Page(s): 668 
54547-
54548-
54549-
54550-Root / lemma: lehik-1 {* lehuK} Note: common Proto Germanic -u- > -u-, -y-, -/-. 
54551-Meaning: to prepare for sale 
54552-
--
54559-assemble ', nuo/Ikums ' pact, covenant'. 
54560-
54561-References: WP. II 395, WH. I 797. 
54562:Page(s): 669 
54563-
54564-Root/ lemma: lehik-2{*lehuK} Note: common Proto Germanic -u- > -u-, -y-, -/-. 
54565-Meaning: to bend 
54566-
54567-Material: S. above S. 309 E {el-8, elehi-, lehi-), wherefore further the Celtic (?) FIN Licus ' 
54568-Lech, River (the name is of Celtic origin), river in the west of Austria, rises south of Rote 
54569-Wand, the highest peak in Vorarlberg ' (Bavaria), Lithuanian FIN /./e/reand Leika, 
54570-Lithuanian //e/r/7a "marshy meadow', Latvian Iiekna6s.; compare lllyrian Ep/-//cus partus, 
54571-FIN Pacco-//cus (Bruttium), mod. FIN Z.//^a(Kroatien). 
54572:Page(s): 669
```


## [2026-09-07T01:40:31.763Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '54428,54458p' POK_full.txt; echo \"=== POK_02 printed 667 -> leaf 667-344=323\"; python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (322,323,324):\n    print('--- leaf',i)\n    print(t[i][:1500])\nEOF"
}
```


### [2026-09-07T01:40:33.064Z] TOOL RESULT

```
Root/ lemma: lehig-3, lohig-{*lehu^ Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to jump; to tremble 

Material: Old Indie rejati^ makes jump, allows to tremble ', rejate^ jumps, shakes ', rejayati 
" makes tremble, shake '; 

npers. alextan^ jump, kick (of the horse) ', Kurdish be-fez/um^ dance', ITzim^ play'; 

gr. eAeAI^u), sAsAi^a " cause to vibrate, whirl round, of an army, cause it to turn and face 
the enemy, rally it, move in coils or spires, of a serpent ', £A£Ai[*Y]-x6u)v " shaking the 
earth, epith. of Poseidon ' (in addition probably also Aiy- " tear off, dash off ' in Aiyaivsi " 
outleap, jump before -, jump forward ', Aiya tqxsux;); 



Old Irish lofgvc\. "calf, bret. dial, /u-eds., A/" blockhead, laughable'; cymr. PI. //o/" 
calves ' (Sg. //o) is Irish loanword; 

Gothic laikan{laflaiK) " jump, spring', bi-laikan^ deride ', laiks^ dance ', Old Norse leika 
{lek) 'join somebody to play, lick (flame), fence ', /e/Ar'game, derision ', Old English lacan 
"be quick, move fast, play, fence ', /ac'game, fight, struggle, booty, gift'. Middle High 
German leichen^ jump, make fun, laugh at ', Old High German leih, /e/ch^game, song, 
melody ', Modern High German dial, /a/ch^ lusus venerius ', Middle Low German /e/r' the 
spawning, spawn ', Modern High German La/ch {from Germanic entl. Old Bulgarian //kb ' 
round dance, peasant dance '); 

Lithuanian /a/gyt/' run around wildly ', verbal noun laigymas. 

References: WP. II 399, Trautmann 148. 
Page(s): 667-668 

=== POK_02 printed 667 -> leaf 667-344=323
--- leaf 322
  ,  t,
lit.  Ullas  jdünn,  schlank'  (aus  Heiras,  zu  gr.  leiQÖg),  lett.  Zie^s  ,groß« (,*schlank*),  mit  anderen  Suffixen  lit.  lelnas,  leXtas  ,schlank',  ablaut.  ldina% ds.;  liehas  , mager,  dünn',  ablaut.  Idibas  ,zart,  dünn,  schlank';
ksl.  lMv^,  libav^,  l^biv^  , mager',  serb.  linjati  , schwinden',  linjati  «^ , mausern',  Denomin.  von  Hein-  (;  lit.  leinas),  slov.  Uliti  ,häuten'  {:  \i^ leiUti  , mager  werden'),  leviti  se  ,sich  häuten'  (:  lit.  IdiUnti  , dünner machen') ;
toch.  A  lalamsk-,  B  lalamske  ,zart'.
b.  s-Erweiterung  leis-,  lois-  in:
gr.  iLagög  ,milde,  lind*  (*lis,ro-s),  loXad'Og  ,der  zurückbleibende,  hinterste, letzte',  loiad'iog  ds.,  vielleicht  aus  HoihioTog,  Superlativ  zu  *loihig
=  germ.  Haisiz  , weniger,  minder*,  ags.  Ixs,  nengl.  less^  as.  les  ds.,  Kompar. ags.  Ixssa  (Haisiza),  afries.  lessa,  Superl.  ags.  läest  und  Irrest,  engl,  hast, afries.  lerest  und  lest,  zu  krimgot.  lista  , wenig' ;  ahd.  llso  Adv.  ,leniter', mhd.    Adj.   und  Adv.    Use,   nhd.  leise]   ags.  ge-Usian   , schlüpfen,    gleiten';
lit.  liesas,  lett.  Hess  , mager';  lit.  Uesti  und  lysti  ,mager  werden',  lett. liest  ds.
WP.  II  387  ff.,  WH.  I  807  f.,  Trautmann  154,  Specht  Idg.  Dekl.  125, Machek  Recherches  75  ff.  Wohl  hierher  1.  leig-  und  leik-,  s.  unten  S.  676.
3,  lei-  , schleimig,   durch  Nässe  glitschiger  Boden,  ausgleiten,   worüber  hin- schlei
--- leaf 323
ehm^  (lajiz-),   leira  [Haizön)
schwach.  Fem.  ,lehmiger  Strand'
und  apr.  layso  f.  {Haisa)  , Letten,  Ton,  Tonerde';  in  ders.  Bed.  von einer  (^-Erw.  apr.  laydis  ,Lehm*  und  alb.  leth  , feuchter  Ton*;
lit.  laistau,  -yti  ,verkleben,  mit  Lehm  oder  Kalk  verschmieren',  vgl. auch  ai.  lindu-  , schleimig,  schlüpfrig'
663
2.  als  Bezeichnung  schleimiger  Fische:
o-r.  hvevg  , Schleimfisch',  ahd.  slio,  ags.  slliv,  sleo  , Schleie',  lit.  lynas, lett.  Unis,  apr.  Unis  , Schleie',  russ.  linb  usw.  ds. ;
3.  als  Bezeichnung  des  , (schleimig)  Glatten'  :  gr.  XeTog  , glatt'  :  lat.  levis (^leiuis)  ,glatt',  gr.  liTÖg  , glatt,  schlicht',  Xiröq  und  Ug,  -xög  ,glattes  Tuch', Uoafi  Tthqa  , glatter  Fels' ;  llaTtog,  att.  llacpog  ,glatt,  gerieben'  sind  unklar ; lat.  li'fna  , Feile'  wohl  aus  *(s)li-mä  oder  *{s)lei-mä  (vgl.  ahd.  sUm  ,Schleim^, slmen  , glatt  machen,  blank  schleifen',  auch  gr.  Xel(.ia^  , Schnecke');
4.  mit  anlautendem  sl-:
kelt.  *sli-m-no-  , glitschig'  in  air.  slemun  ,glatt,  schlüpfrig*,  cymr.  llyfn , glatt,  eben',  acymr.  limnint  ,sie  glätten',  abret.  gur-limun  , glätten',  mbret. di'leffn  ,hart' ;
ags.  aisl.  nfries.  mnd.  mhd.  sllm  , Schleim'  (ahd.  slimen  , glätten');  vgl. aisl.  sly  n.  , schleimige  Wasserpflanzen';
lett.  slienas  f.  PI.  , Speichel'  (^sleinäs),  aksl.  sliny,  serb.  sUne  ,Rotz', russ.  slina  , Speichel';
5.  mit  Ic-Suffix:
gr.  Xel
--- leaf 324
en  ds.,  mhd. eine  hure  sleif  en  ,sie  dem  Erdboden  gleich  machen'.  Intens,  ahd.  slipfen .ausgleiten,  ausschlüpfen',  mhd.  slipfec,  slipferic  , schlüpfrig' ;
daneben  mit  germ.  -hb-:  ndl.  slib,  slibbe  , Schlick,  Schlamm',  slibheren , gleiten',  mnd.  slibber,  -ich  , schlüpfrig'.
{s)leidh-  ,schlüpfrig,  gleiten',  s.  unter  eigenem  Schlagwort.
sleig-  , schleimig,  gleiten,  glätten' :
Gr.  XiyÖTjv  ,die  Oberfläche  streifend',  Xiyöog,   Xiyda  ,Reibstein,  Mörser';
664  f
f.
air.  sligim,  fo-sUgim  ,linö',  adslig  , lockt  an'  (cymr.  llith  , Lockspeise*,  T Uithio  , ködern'  <  *sUg-t-),  vielleicht  —  als  , streichen  =  schlagen'  =  air.  -. sligim  ,schlage',  dazu  slige  ,Straße'(?);  air.  sliachtad  .das  Glätten,  Ebnen*-  " air.  slige  ,Kamm' ;
aisl.  sllkr  , glatt',  sllkisteinn  , Schleifstein',  ahd.  sllhhan  .schleichen' (==  ^gleiten'),  sleihha  , Schleife,  Schlitten',  mnd.  sUk,  slick,  mhd.  slich ,Schhck,  Schlamm';  Partiz.  *sUhta-  ,geglättet'  in  got.  slaihts  »schlicht, eben',  aisl.  slettr  , glatt,  eben,  gerade',  ahd.  sieht  ,gerade,  eben,  schlecht', nhd.  schlicht  und  schlecht,  ags.  sliht,  mengl.  sUght,  sleght  , glatt,  eben';
abg.  shzzkz  ,6lg  ^hoO-ov',  russ.  slizkij  , schlüpfrig',  slizb  , Schleim',  sUzy PL  ,eine  Art  Schleife'.
leip-  ,mit  Fett  beschmieren',  s.  unter  eigenem  Schlagwort.
lei-t-  , darüber  streichen,  sanft  berühren,  streicheln':  wahrscheinlich Xlttj  ,
```


## [2026-09-07T01:40:34.525Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in KLN_1966.txt SKT.txt LKT.txt; do echo \"== $f\"; grep -n -i -E \"lurken|lerken|lirken\" $f | head -5; done; echo \"== ARY index\"; ls incoming/ARY/ 2>/dev/null | head; python3 - <<'EOF'\nimport json,os\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_headwords.json'\nprint(os.path.exists(p))\nif os.path.exists(p):\n    d=json.load(open(p))\n    ks=[k for k in (d if isinstance(d,dict) else []) if 'لرز' in k]\n    print(ks[:20])\n    for k in ks[:5]: print(k, d[k])\nEOF"
}
```


### [2026-09-07T01:40:35.738Z] TOOL RESULT

```
== KLN_1966.txt
21178:Derivatives:  laryngoscop-ic,  laryngoscop-ic-al, adjs.,  laryngoscop-ist,  n.,  laryngoscop-y,  n. larynx,  n.,  the  upper  part  of  the  windpipe  (anat.) —  Medical  L.,  fr.  Gk.  Xdpuyf ,  gen.  Xdpuyyos, ‘throat,  upper  part  of  the  windpipe’,  which  is prob.  a  blend  of  9«puy5,  ‘throat’  (see  pharynx), andXatpLo;,  ‘throat,  gullet’.  See  Frisk,  GEW., II  87  s.v.  Xapuy£  It  is  also  possible,  however, that  Gk.  Xdpuyl  derives  from  the  I.-E  imitative base  *(s)lrg-  ‘to  sip’,  whence  also  MHG.  slurc, ‘gullet,  gorge’,  slurken,  ‘to  sip’,  Swed.  slurca,  ‘to sip  in  big  quaffs’,  and  possibly  also  L.  lured,  lur- care  (also  lurcor,  lurcari),  ‘to  devour’  (fr.  *lurgi- cos,  ‘devouring’);  see  Walde-Hofmann,  LEW., I,  837  s.v.  lured.  If  this  latter  etymology  is correct,  the  form  of  Xapu-/£  is  prob.  due  to  the influence  of  ^dpuy^,  ‘throat’, lascar,  n.,  an  East  Indian  sailor.  —  Pers.  lashkar, ‘army’,  fr.  Arab,  al'askar,  ‘the  army’,  fr.  al-, ‘the’,  and  ‘ Askar ,  ‘army’,  which  prob.  derives  fr. Late  Gk.  i^pxr,Tov,  fr.  L.  exercitus,  ‘army’,  fr. exercere,  ‘to  train,  drill’.  See  exercise  and  cp. askari  and  the  second  clement  in  seraskier.  E. lascar  was  influenced  in  meaning  by  Pers.  lash- kart,  ‘soldier’,  lit.  ‘of  the  army’,  fr.  lashkar. lascivious,  adj.,  wanton,  lustful.  —  Late  L.  lasci- vidsus,  fr.  L.  lasclvia,  ‘wantonness,  playfulness, lustfulness’,  fr.  lascivus,  ‘wanton,  playful,  lust¬ ful’,  fr.  I.-E.  base  *lds-,  ‘greedy,  desirous’, whence  also  OI.  -iafati  (dissimilated  fr.  *lalsati), ‘yearns’,  Idsati,  ‘plays,  frolics’  (also  ‘flashes.
22340:lurk,  intr.  v.,  to  lie  in  wait.  —  ME.  lurken,  formed fr.  ME.  luren,  ‘to  frown,  lurk'  (see  lower,  ‘to frown’),  with  the  intensive  suff.  -k.  The  same suff.  occurs  in  the  verbs  smirk,  stalk,  talk. Derivatives:  lurk,  n.,  lurk-er,  n. lurry,  n.  —  A  var.  of  lorry.
== SKT.txt
== LKT.txt
== ARY index
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
False
```


## [2026-09-07T01:40:48.693Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | grep -i bqt; echo \"=== ARY\"; grep -n \"لرز\" ARY_pages.txt | head -15; echo \"=== ARY latin\"; grep -n -i -E \"larz|rarz\" ARY_latin_index_pages.txt 2>/dev/null | head"
}
```


### [2026-09-07T01:40:48.765Z] TOOL RESULT

```
BQT_alt_v1.txt
BQT_dli_part1.txt
BQT_v1_djvu.xml
BQT_v1_pages.txt
BQT_v1.txt
BQT_v2_pages.txt
BQT_v2.txt
=== ARY
ugrep: warning: ARY_pages.txt: No such file or directory
=== ARY latin
```


## [2026-09-07T01:40:48.785Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1894 --image 2>&1 | tail -40"
}
```


### [2026-09-07T01:40:53.283Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1894.png
REF: BQT:1894  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 691  OCR-lang: fas

کوردین -۱۸۹۵-
لرلر ۱ « بنتح دو لام و سکون دو را ۱ یکی ازنامهای خدای تعالی است جل‌جلاله .
بیان نهم
در لام با زای نقطه دار ۲۷ مشتمل بر دو لت
راکوبند وآن کمان نرمی باشد که کمانداران زر - بر وزن وزس , بمعنی هوشمند
بدان مشق کمان کشیدن کنند ۴ - و در عربی | وعاقل ودانا و بزرکك وپرهیزکار باشد.
بیان دهم
رم ۴ - بنتح اول و ثانی و سکون‌منم. ون ؟ - بر وزن وممنی لجن است که
کل و لای تیره و سیاه راکویند که درته‌حوشها کل سیاء ته حوشها و لای بن تالابها باشد #*
و بن تالابها میباشد وآنرا لجن هم میگویند.
(۱) خم۱ : با زای تازی .
۹ -اين بیت عنصری بلخی را شاهد آوردهء‌اند : ۱
بفرزانگی ساب افمرش همیخواست از حضرت لرلرش.
و ظاهراً این صورت مصحف «کرکر» است « لغت نامه > . رك :گرکر .
۴ - ای ببازوی فوت تو شده مر فلك را کمان کمان لزءم .
۴ لبم - لجن < لزن . ۴ <لجن * لجم * ازم . 1
2 لرز - بفتح اول » در اوراق مانوی ( پهلوی ) 772 ( لرزیدن از تب) ,۳1687188)
( 0.87 وا ,126 ,8505 و ... ۳۳۵۵2 ۸/:۵۵16 ‎٩۲‏ افنا ۸ -کردی 1272 (ب)
« ژابا ص ۳۷۸ > ؛ جنبش با حرکات کوچکه غیر منظم و ارتعاش وترس » لرزبدان .
۰ 7 لرزیدن - بفتح اول و-ینجم » از : لرز (ء.م.) + بدن ( پوند مصدری ) ؛ جنبیدن
و مرتعش شدن با حرکات كوچك غبر منظم » طپیدن .
2 لست - ر4 لفات متفرقهٌ پامان کتاب .
```


## [2026-09-07T01:41:09.194Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && ls; grep -n \"لرز\" ARY_pages.txt | head -15"
}
```


### [2026-09-07T01:41:09.248Z] TOOL RESULT

```
ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf
ARY_latin_index_pages.txt
ARY_pages.txt
ARY_pages.txt.pages
1066:بردگان به سرکردگی اسپارتاکوس 92۸17۸2118 که پایه‌های امپراتوری روم را به لرزه د رآورد»
1951:معنی این واژه در سانسکریت: لرزیدن.
5698:چم این واژه در سانسکریت و لیترانی و لثرنی و یونانی : لرزیدن» به لرزه افتادن
8581:۱ لرزد 9 (65شتت» اما
11095:افغانی (پشتو) (/44(7ا4۳0): لرزقه ان پسگشت‌ها اش ات۲
```


## [2026-09-07T01:41:12.439Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i -E \"^lrz|lrz-|larz\" NYB_vol2_glossary.txt | head; echo \"=== PHD leaf of line 432\"; python3 - <<'EOF'\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:432]); leaf=pre.count('\\f')\nprint('leaf',leaf,'printed p.',leaf-21)\nEOF\necho \"=== NYB leaf\"; python3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\npre='\\n'.join(lines[:2349]); leaf=pre.count('\\f')\nprint('leaf',leaf,'printed p.',leaf-8)\nEOF"
}
```


### [2026-09-07T01:41:13.680Z] TOOL RESULT

```
2349:larzitan [lleytn'] to tremble 58%, — MPrthPrs Irz-, MPrs also rrz ‘to shiver with fever’, List 87; NP larzidan.
7251:larzīdan: larzītan
=== PHD leaf of line 432
leaf 77 printed p. 56
=== NYB leaf
leaf 135 printed p. 127
```


## [2026-09-07T01:41:20.018Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && sed -n '8575,8585p' ARY_pages.txt; echo ---; grep -c \"\" ARY_pages.txt; grep -n \"لرز\" ARY_latin_index_pages.txt | head"
}
```


### [2026-09-07T01:41:20.084Z] TOOL RESULT

```
لاتین (/712ا): زان ولزی (۴8ل): ,010۸8
ایسلندی‌کهن (010/۸۸7بی5 صاه): آلبانی (1۸2/مقلم: رز
700
تررس کهن (۸0۳8۴ طران): 21۸ پسگشت‌ها ‏ " مد دی
فریزی کهن (00فا5لغ۶ صام): لا 8 و
آلمانی کهن ((0874۸ 04 1لز صا0): 8 (008) امین
۱ لرزد 9 (65شتت» اما
آلمانی (2فههع02). #انآهة 05۰ نم 2 مهد
انگلیسی کهن (ل//8/05 صام): 708 ,لاتآن برهان قاطع : ۹.۰
باهدداشت.
چم‌های برخی از واژه‌های این فهرست: دژ) تهه‌ی شنی» تهه؛ وزیدن» شهر؛ ناحید
---
16204
```


## [2026-09-07T01:41:20.456Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T01:41:20.464Z] TOOL RESULT

```


```


## [2026-09-07T01:41:24.350Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86",
 "prompt": "Give the full Persian etymology section for لرزیدن (larzidan): Middle Persian form, Proto-Iranian reconstruction, cognates, cited authorities."
}
```


## [2026-09-07T01:41:25.341Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2",
 "prompt": "Persian لرز (larz) — etymology, Middle Persian and Proto-Iranian forms, meaning."
}
```


### [2026-09-07T01:41:30.685Z] TOOL RESULT

```
# Persian Word: لرز (larz)

This Wiktionary entry documents a Persian noun with multiple related meanings.

## Meaning

The word **لرز (larz)** refers to physical trembling and seismic events. Its definitions include "shaking," "temblor," "quake," and "shivering."

## Etymology

The term descends from an ancient language family. According to the entry, it was "Inherited from Proto-Iranian *rarz-," with cognates appearing in related languages like Zazaki (lerz, meaning "shaking, quake") and Northern Luri.

## Pronunciation

The word is pronounced /ˈlarz/ in Classical Persian, with slight variations across different Persian dialects and related languages like Tajik.

## Related Forms

A derived verb **لرزیدن (larzīdan)** means "to shake, to tremble." The word also traveled into Hindustani languages, appearing as लरज़ (laraz) in Hindi and لَرَز (laraz) in Urdu.
```


### [2026-09-07T01:41:31.141Z] TOOL RESULT

```
# Persian Etymology of لرزیدن (larzidan)

**Middle Persian Origin:**
The word is "inherited from Middle Persian" with the form 𐭫𐭥𐭦𐭩𐭣𐭭 (llc-ytn /⁠larzīdan⁠/).

**Proto-Iranian Root:**
It derives from Proto-Iranian *[\*rarz-](/w/index.php?title=Reconstruction:Proto-Iranian/rarz-&action=edit&redlink=1), establishing the ancient lineage of this verb.

**Cognate Evidence:**
A related form appears in Pashto as رېږدېدل (reẓ̌dedəl), meaning "to tremble," demonstrating linguistic connections across Iranian language branches.

**Lexicographic Authority:**
The Dehkhoda Dictionary Institute provides scholarly documentation of this term, with entries compiled by Ali-Akbar Dehkhoda beginning in 1931.

The verb fundamentally means to shake, tremble, shiver, or shudder—sense preserved across centuries of Persian linguistic development.
```


## [2026-09-07T01:41:35.982Z] TOOL CALL #32: WebSearch

```json
{
 "query": "Mittelhochdeutsch \"lërken\" stammeln Lexer lirken bedeutung"
}
```


## [2026-09-07T01:41:38.434Z] TOOL CALL #33: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86' --note 'page 315, root Lrğ, node 3: Persian larzidan < MP larzidan < Proto-Iranian *rarz-' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2' --note 'page 315, root Lrğ, node 3: Persian larz \"shivering, quake\" < Proto-Iranian *rarz-' 2>&1 | tail -3"
}
```


### [2026-09-07T01:41:42.534Z] TOOL RESULT

```
Web search results for query: "Mittelhochdeutsch "lërken" stammeln Lexer lirken bedeutung"

Links: [{"title":"Mittelhochdeutsches Handwörterbuch Bibliotheksausgabe | S. Hirzel Verlag","url":"https://www.hirzel.de/mittelhochdeutsches-handwoerterbuch-bibliotheksausgabe/9783777626543"},{"title":"lurken - Frühneuhochdeutsches Wörterbuch","url":"https://fwb-online.de/go/lurken.s.3v_1709543983"},{"title":"lurken – Frühneuhochdeutsches Wörterbuch","url":"https://fwb-online.de/lemma/lurken.s.3v"},{"title":"Mittelhochdeutsch lernen","url":"https://www.mittelalter-entdecken.de/mittelhochdeutsch-lernen/"},{"title":"Mittelhochdeutsche Sprache – Wikipedia","url":"https://de.wikipedia.org/wiki/Mittelhochdeutsche_Sprache"},{"title":"Matthias Lexer","url":"https://en.wikipedia.org/wiki/Matthias_Lexer"},{"title":"Hilfsmittel im Netz - Mittelhochdeutsch zum Nachschlagen und Lernen","url":"https://mhd.sawogra.de/thilfsmittel.php"},{"title":"Ad fontes: Ressourcen / Die deutsche Sprache in den Quellen / Lexer: Mittelhochdeutsches Wörterbuch, Kurzdarstellung","url":"https://www.adfontes.uzh.ch/ressourcen/die-deutsche-sprache-in-den-quellen/lexer-mittelhochdeutsches-woerterbuch-kurzdarstellung-pdf"},{"title":"Mittelhochdeutsches Handwörterbuch von Matthias Lexer","url":"https://woerterbuchnetz.de/?sigle=Lexer"}]

Based on the search results, I found relevant information about these Middle High German terms:

The word "lurken" means "stottern, anstoßen, schwer reden" (stutter, stumble in speech, speak with difficulty). Related words include "lallen," "lispeln," "schwapeln," "stammeln," "statzen," "anstossen," "gatzen," "lerzen," "lirken," and "stottern."

The search results show that lirken is mentioned as a related word (Bedeutungsverwandte) to lurken, indicating they are synonymous terms relating to speech impediments and difficulty with clear articulation.

The results also confirm that Matthias Lexer's "Lexer" (mittelhochdeutsches Taschenwörterbuch) is still the standard reference work for translations from Middle High German, which would be the appropriate resource to consult for precise definitions of these terms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-07T01:41:44.624Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0218766017cfcab9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/44316d9d9214f828.txt
```


## [2026-09-07T01:41:52.755Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://fwb-online.de/lemma/lurken.s.3v",
 "prompt": "What does the Early New High German verb \"lurken\" mean, and which related words (Bedeutungsverwandte) are listed? Quote the definition."
}
```


## [2026-09-07T01:41:55.207Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg315.png')\nprint(im.size)\n# crop region of the boxes: x 500-1300, y 440-800 in original 2550x3300\nim.crop((540,440,1300,810)).resize((1520,740)).save('crop_boxes.png')\n\""
}
```


### [2026-09-07T01:41:57.642Z] TOOL RESULT

```
# Early New High German "lurken"

**Definition:** According to the Frühneuhochdeutsches Wörterbuch, "lurken" means "›stottern, anstoßen, schwer reden‹" (to stutter, to stumble in speech, to speak with difficulty).

**Related words (Bedeutungsverwandte)** listed include:
- lallen
- lispeln
- schwapeln
- stammeln
- statzen
- anstossen
- gatzen
- lerzen
- lirken
- stackeln
- stottern

The entry notes this verb is primarily used in Upper German (oberdeutsch) dialects and is ablaut-related to Middle High German *lërcken*.
```


### [2026-09-07T01:41:59.142Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-07T01:42:01.694Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/crop_boxes.png"
}
```


### [2026-09-07T01:42:01.722Z] TOOL RESULT

```

```


## [2026-09-07T01:42:29.467Z] TOOL CALL #37: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T01:42:29.512Z] TOOL RESULT

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


## [2026-09-07T01:42:44.010Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT larz/rarz\"; grep -n -i -E \"larz|rarz|\\brəz\" BRT.txt | head -6; echo \"== KNT\"; grep -n -i -E \"larz|rarz\" KNT.txt | head -3; echo \"== Watkins leig\"; grep -n -i -E \"^leig|leig-|lēig\" AHD_watkins1985.txt | head -10; echo \"== WLD band? \"; ls WLD* 2>/dev/null; echo \"== SYN tremble\"; grep -n -i \"TREMBLE\" SYN.txt | head -5"
}
```


### [2026-09-07T01:42:44.110Z] TOOL RESULT

```
== BRT larz/rarz
== KNT
== Watkins leig
184:Another aspect of the function of sover- eignty is the sphere of the law. There is an old word, yewes-, probably for “religious law,” in Latin jus. Latin léx is also ancient (leg-'), though the details of its etymology are uncertain. In a society that emphasized the principle of exchange and reciprocity, it is scarcely surprising that the notion of con- tractual obligation should be well repre- sented. Several roots specify the notion of “bond”: bhendh-, ned-, leig-', all of which have derivatives with technical legal mean- ings in various languages. The word for “a pledge,” wadh-', exists in western Indo- European, whence the English verb for mak- ing a particular kind of contract, WED. An oath then as now was important: the roots *serk- and oito- are found in Celtic and Ger- manic. The verb k”ei-' meant “to pay com- pensation for an injury.” Its derivative noun, *k“oind, was borrowed from Doric Greek into the most ancient Roman law as Latin poena, punire, whence English PUNISH and a host of legal terms. The Greek word for jus- tice, diké, is derived from the notion of “boundary marker” (deik-; compare also ter-, “termen-).
671:extensions in: a. Old English slim, slime: sLIME; b. Old English slipor, slippery: SLIPPERY; Cc. Old English *slice, smooth (> Middle English slike, smooth): sLick; d. Old English lim, cement, birdlime: LIME; e. Old English lam, loam: LOAM; f. Old Norse s/éttr, smooth, sleek, akin to the probable Scandinavian source of Middle English slight, slender: SLIGHT; g. Middle Dutch and Middle Low German slippen, to slip, slip away, akin to the probable source of Middle English slippen, to slip: sL1P!; h. Middle Low German slépen, to drag: SCHLEP. 2. Suffixed form *lei-mo- in Latin limus, slime: LIMACINE, LIMICOLINE. 3. Suffixed form */ei-w- in Latin oblivisci (ob-, away; see epi), to forget (< “to wipe, let slip from the mind”): OBLIVION, OUBLIETTE. 4. Extended form *(sjleia- in: a. nasalized zero-grade form */i-n-a- in Latin linere, to anoint: LINIMENT; b. Suffixed zero-grade form *li- (< *lig-) in Greek litos, plain, simple: LiToTEs. [Pok. 3. lei- 662.] léi-. Also lei-. To flow. 1. Extended form “/eib- in Latin libdre, to pour out, taste: LIBATION; PRELIBATION. 2. Possibly suffixed extended form */eit-os- in Latin litus, shore: LITTORAL. [Pok. 4. lei- 664.] leid-. To play, jest. Suffixed o-grade form *loid-o- in Latin lidus, game, play, with its derivative lidere, to play (but both words may possibly be from Etruscan): LUDICROUS; ALLUDE, COLLUDE, DELUDE, ELUDE, ILLU- SION, INTERLUDE, PRELUDE, PROLUSION. [Pok. leid- 666.] leie-. To waste away. Zero-grade form “li- (< *lia-) in Greek limos, hunger, famine: BULIMIA. [In Pok. 2. lei- 661.] leig-'. To bind. 1. Germanic */ik- in Middle Low German lik, leech line: LEECH?. 2. Zero-grade form */ig-d- in Latin ligare, to bind: LEAGUE!, LEGATO, LIABLE, LIEN, LIGASE, LIGATE; ALLOY, (ALLY), COLLIGATE, COLLIGATIVE, FURL, OBLIGE, (RALLY), RELY. [Pok. 4. leig- 668.] leig-?. Poor. Perhaps Greek oligos, few, little: OLIGO-. [Pok. 1. leig- 667.] leig-5. To leap, tremble. O-grade form */oig- in Germanic *laik- in: a. Old English -lac, suffix denoting activity: WEDLOCK; b. Old Norse leika, to play: LARK?. [Pok. 3. leig- 667.] leigh-. To lick. 1. Greek leikhein, to lick: ELECTUARY. 2. Zero-grade form *lig- in Germanic *likk6n in: a. Old English liccian, to lick: Lick; b. Old French lechier, to live in debauchery: LECHER. 3. Nasalized zero-grade form *ling- in Latin lingere, to lick: ANILINGUS, CUNNI- LinGus. [Pok. leigh- 668.] leikw-, To leave. 1. Basic form *leikv- in Greek leipein, to leave: ECLIPSE, ELLIPSIS. 2. O-grade form *loikv- in: a. Germanic */aihwnjan in Old English lénan, to lend, give (< “to leave to”): LEND; b. suffixed form *loikv-nes- in Germanic */aihwniz in Old Norse Jan, loan: LOAN. 3. Zero-grade form *likv- in Germanic *-lif-, left, in: a. Germanic *ain-lif-, “one (beyond ten),” in Old English endleofan, eleven (see oi-no-); b. Germanic *twa-lif-, “two left (beyond ten),” in Old English twelf, twelve (see dwo-). 4. Nasalized zero-grade form *li-n-kv- in Latin linquere, to leave: DELINQUENT, DERELICT, RELINQUISH. [Pok. leike- 669.] leip-. To stick, adhere; fat. 1. Germanic *libam in Old English Jif, life (< “continuance”): LIFE, LIVELY. 2. Ger- manic “libén in Old English lifian, libban, to live: LIVE}. 3. Germanic */aibjan in Old English léfan, to leave, have remaining: LEAVE!. 4. Germanic “libro in Old English lifer, liver (formerly believed to be the blood-producing organ): LIVER}. 5. Zero-grade form *lip- in Greek lipos, fat: L1po-. 6. Variant form *aleibh- in Greek aleiphein, to anoint with oil (> aleiphar, unguent): ALIPHATIC; SYNA- LEPHA. [Pok. eip- 670.] leis-'. Track, furrow. 1. O-grade form *lois- in: a. Ger- manic */aist- in Old English Jast, lést, sole, footprint: Last’; b. Germanic */laistjan, “to follow a track,” in Old English /éstan, to continue: LAST?; c. suffixed form *lois-G in Germanic */aiz6 in Old English Jar, learning:
698:[lik-. Body, form; like, same. Germanic root. 1. Old English lic, form, body: LICH GATE. 2. Old English -lic, having the form of: -LyY!}, -Ly?. 3. a. Germanic *galikaz in Old English gelic, similar: ALIKE, LIKE?; b. Germanic phrase *aiwo galikaz, “ever alike” (*aiwo, *aiwi, ever; see aiw-), in Old English #lc, each: EACH. 4. Germanic *is-lik in Old English ilca, the same (see i-). 5. Old Norse likr, like: LIKELY. 6. Middle Dutch -lijc, -ly: FROLIC. 7. Germanic *likjan in Old English lician, to please: LIKE!, 8. Germanic *hwa-lik-, which (see k’o-). [In Pok. 2. leig- 667.]]
1229:ALLEGE ag-, leg-1 ALLEGORY al-!, ger-1 ALLELOMORPH al-1 ALLERGY werg- ALLEVIATE legh- ALLEY! al-2 ALLIGATOR al-1 ALLITERATE deph- ALLITERATION deph- ALLO- al-1 ALLOCUTION tolkw- ALLOMERISM (s)mer-2 ALLOPATRIC  peter- ALLOT kleu-3 ALLOY leig-1 ALLUDE |leid- ALLUVION leu(e)-
1383:COLE kaul- COLEOPTERA kel-2, pet- COLEOPTERAN kel-2 COLEOPTILE kel-2, pet- COLEORHIZA kel-2, wrad- COLESLAW kaul- COLEUS kel-2 COLLABORATE leb-1 COLLAGE koli- COLLAPSE leb-1 COLLAR kwel-1 COLLATE tele- COLLEAGUE leg-1 COLLECT! leg-1 COLLEGIALITY leg-! COLLET kwel-1 COLLIE g(e)u-lo- COLLIER g(e)u-lo- COLLIGATE leig-' COLLIGATIVE |leig-1 COLLO- koli- COLLODION koli- COLLOQUIUM tolkw- COLLOQUY tolkw- COLLUDE leid- COLLUVIUM leu(a)- COLOBOMA kel-1 COLON! | skel-3 COLONEL kel-6 COLONNADE kel-8 COLONY kWel-1 COLOPHON kel-6 COLOR kel-2 -COLoUS kWel-1 COLPITIS kwelp- COLPOSCOPE kwelp- COLPOSCOPY kwelp- COLTER skel-1 CoLuMBA kel-5 COLUMBARIUM kel-5 COLUMBINE kel-5 COLUMN kel-6 COLZA sé-1
1546:FURBISH prep- FURL leig-1 FURLOUGH leubh- FURNACE gWher- FURNISH per! FURROW perk-2 FURTHER per! FURTIVE bher-1 FURUNCLE bher-1 FURUNCULOSIS_ bher-1 FURZE piiro-
1730:LAPS |ab- LAPAROTOMY lep-1 LAPSE leb-1 LAPWING klou- LARCENY [é-1 LARK? leig-3 LASCIVIOUS las- LASSITUDE [é-2 LAST! |@-2
1737:LEAGUE! leig-1
1739:LEAGUER! legh- LEAK leg-2 LEAN! klei- LEAP klou- LEARN leis-1 LEASING leu-! LEAST leis-2 LEATHER letro- LEAVE! leip- LEAVE? §leubh- LEAVEN legWh- LECHER leigh- LECTERN leg-1 LECTION leg-1 LECTURE leg-' LEDGE legh- LEDGER legh- LEE kele-1 LEECH! feg-1 LEECH? leig-1 LEEK leug-! LEER kleu-! LEES legh- LEGACY leg-1 LEGAL leg-1 LEGATE leg-1 LEGATO leig-1 LEGEND leg-1 LEGERDEMAIN leg¥h- LEGIBLE leg-1 LEGION leg-1 LEGISLATOR leg-1, tele- LEGIST leg-1 LEGITIMATE leg-1 LEITMOTIF leit-2 LEMAN leubh- LEMMA! (s)lag¥- LEMMA? lep-t LEMURES_ lem-2 LEND leikw- LENGTH del-1 LENIENT [6-2 LENIS [6-2 LENITIVE |@-2 LENITY 16-2 LENT del-1 LENTO lento-, lep-1. LEPIDO- lep-1 LEPIDOTE lep-1 LEPRECHAUN kWrep-, legwh- -LEPSY (s)lag¥- LEPTO- lep-1 LEPTON! lep-1
1741:LETHAL ol- LETHARGY |adh- LETHE ladh- LETTER deph- LETTUCE melg- LEVEL [ithra LEVER leg’h- LEVIGATE ag-, leg’h- LEVIRATE daiwer- LEVITY leg¥h- LEVo- laiwo- LEVOROTATION laiwo- LEVOROTATORY laiwo- LEX leg-1 LEXICON leg-1 LIABLE leig-1 LIBATION Iéi- LIBERAL leudh-2 LIBERATE leudh-2 LIBERTINE leudh-2 LIBERTY leudh-2 LIBIDO leubh- LIBRA fithra
== WLD band? 
WLD_band3.txt
== SYN tremble
10405:OE wé@fels ‘covering’ and ‘cloak’ (e.g. Mt. 5.40), fr. the root of OE (b:-)w@fan, Goth. bi-waibjan ‘wrap about, clothe’ : ON veifa ‘vibrate’, Skt. vip- ‘tremble’, etc. Walde-P. 1.240. Feist 97.
14545:2. Lat. premere (> It. premere), perf. presst, pple. pressus, with frequent. pressdre (> Fr. presser, Sp. prensar; Rum. presa, fr. Fr.), fr. parallel stems *prem- and *pres- (ef. *trem-, *tres- in words for ‘tremble’), outside connec- tions dub. Walde-P. 2.43. Ernout-M. 807 f. REW 6738, 6741.
14594:MHG schit(t)en, NHG schiitten, in MHG also ‘shake hard, move violently’, in this sense OHG scutan : OE sciidan ‘shake, tremble’, OS scuddian ‘shake’, Lith. kutétz ‘shake up’, etc. Weigand-H. 2.805 f. Walde-P. 2.601.
16682:6. ChSI. dvignati (reg. for xivés and gadebw in Gospels; cf. dvizenije = xtvy- ots), Russ. dvinut’, dvigat’ (the other Slavic cognates mostly ‘raise, lift’), out- side connections dub. Berneker 240 suggests d-vignqti, with prefix d- (zero grade to Lat. ad) and *vignati : Skt. vij- ‘start up, flee from, tremble’, Av. vij- ‘swing, throw’, ON vikja ‘recede, give way’. Doubted by Walde-P. 1.235.
17018:Du. schudden, OHG scut(/)an, MHG schiit(t)en (NHG schiitten), with iter. forms OHG scutilon, MUG schiit(t)eln, NHG._ schiitteln (also NHG schiittern ‘tremble, shiver’ and schaudern ‘shud- der’, NE shudder) : Lith. kutéti ‘rouse’, Lett. kutet ‘tickle’, ON hossa ‘toss’ (a child on the knees). Walde-P. 2.601 f. Weigand-H. 2.806. Franck-v. W. 602 f.
```


## [2026-09-07T01:42:45.768Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://vajehyab.com/?q=%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86&d=moein",
 "prompt": "What does Mo'in's Farhang-e Farsi give for لرزیدن and لرز — meaning and origin tag (e.g. [په.])?"
}
```


### [2026-09-07T01:42:49.625Z] TOOL RESULT

```
Based on the content provided:

**For لرزیدن (larzidan):**
Mo'in's dictionary defines it as: "جنبیدن ، تکان خوردن" (moving; being shaken). The origin tag is (مص ل .), indicating it's a verbal noun (masdar) from a root verb.

**For لرز کردن (larz kardan):**
Mo'in defines it as: "لرزیدن بر اثر سرما یا تب" (trembling due to cold or fever). The origin tag is (مص ل .), also marking it as a verbal noun.

Both entries use the same origin notation, classifying them as verbal nouns derived from the root ل ر ز.
```


## [2026-09-07T01:43:05.285Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD band3\"; grep -n -i -E \"lerg|larz|leig\" WLD_band3.txt | head -8; echo \"== POK_02 leaf 675/676 for 'leig' printed 667\"; python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(320,332):\n    L=t[i]\n    ms=re.findall(r'(?m)^\\s*(\\d{3,4})\\s*$',L)\n    if ms: print(i, ms)\nEOF"
}
```


### [2026-09-07T01:43:06.520Z] TOOL RESULT

```
== WLD band3
2558:61. feleigare lit. (614° set, atlas ik. 048°. stelgit, ‘ately lit. 645%, (040%),
3026:pin} sy = iliiealy sein 2. leige- 307
3062:‘Haar ghait-d 527. dhrigh- S70. S.pek’- 16%. pilo- aia rowmen- 301" (ateifes) 1, te wal Hacke yon My hasken ileig- FOT* Haher kik 451. bleiben Cort =—— ae - wig- 24. haftenbleiben gh yhaie i 528. Hak ow. cy 388. 5: or GOD". hall #imi- 403" | halloh uli 80. Halm Lolame-2 44 stechender) Heyh- O22", pera a. #el- 45], | Hale mono: 2 Hakechmuck mono. J05* halten jem- 207, | dher- Sidi, | wee 451". Hammer dea Donnergotbes moldh- G0". Hand ijhanto- rere 2. mar 213" a Hand 1 an pat , handel 1 feag- Tay". (mit Vorbedaohi ) zz. 705. Handiliche 2. dhen- 353. Ip. 428". Handhabe 3. ger- 412. hang < ty laerd) eyes harken L. ghrebh- 652. Harn ‘ormat: 463 L. meu- 249". harman meigh- 245". I. (ayels G42", harret l. ger 411. hart 3. qar- 34. Harz 2. gtel- 672. poi- Ta*. ol wagon pe HaseinuBatrauch acd. 887%, 2. ad= TAs Pid- 340, Hauch etmen- 118. havehen -3.an- 6.  revea 843 dhem- Sil,
3132:evhow auriicktroten dpeyt- | achlagen Hhelgh= 805, | schlipfrig meny- 250*. sa rv Nel rice pis: 12%, | lerg- a". wuheven =). gei- GOS. H. per- 42°. (aveidlh—T0T" eohiebon igh: isa. = D1". echliirfen quem O14.. ayeubh- 550", aude coil 1, weu- abo = | Khrud. 127°. ha ; a pon bhei- 137". | schidrfond tovken lab. 343°. eqeibh- B48*, | bhen- 149". | Schlutf qalad- Oe. : ee*, bheid- 154*. | achhummorn aneeiY: rensecitincant yr ruta bath 376: Schitund i gvere 682: | irda 480. (ale Ajiadd cd bharug- 170". whielond —kaikas 32 Phos tangio)- 38 i r : ; ; = ; ; = * 0 ae eee beeu- O15". |'Sohmach  ‘Bormo: 463, <ubi- BBG®, | emdg- 685". | achmilhen ono 168i). Schid u- 315°. eek 1. qur- 353. Behildieréte gyner- 200, | sei. TOT". pi oe. ade 63. | Scblatm  H- 163. neid- 322°, o> 320°. 1 Pies 460. | ’ oa aaoe, tj = ail p-h iz ln ln Sot A hia Seale) 7. | soba andtih-tri-} Se SOE STL W Shel. bees pox- 5%. Schmalz aol Se*. ghwag4. 4G, | Schlamumpititse ee 65". | schmatzend lecken (i- 3383" det- 772: achlammig 2’ yel- 473. sthmawinn 2. gee BOT. bAleuth- 216" {dimo- (55°. | schmocken yews G08. tosyed- G20", | Sehlange = wumyu(A)i- 63. mele BOO", 2. (a)plh)et- gape aac aap. 450", 70", schlank at wits S85 | saath Se Rakin . a- 347° Schumer ameru- Go)". aie a¥ A 885%. | tauch (aun Fell) merinone | sohmeicheln Gl. 440, 08" schinniBen  bdfig- 217° dchilecht | elk pskchalene la. TOL.
== POK_02 leaf 675/676 for 'leig' printed 667
320 ['661']
321 ['662']
323 ['663']
325 ['665']
327 ['667']
328 ['669']
329 ['670']
331 ['671']
```


## [2026-09-07T01:43:10.648Z] TOOL CALL #41: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://fwb-online.de/lemma/lurken.s.3v' --note 'page 315, root Lrğ, node 4: ENHG/MHG lurken = \"stottern, anstoßen, schwer reden\" (stammer), synonyms lirken, lerzen; ablaut to MHG lercken — NOT \"shiver\"' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://vajehyab.com/?q=%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86&d=moein' --note 'page 315, node 3: Moin s.v. لرزیدن «جنبیدن، تکان خوردن»' 2>&1 | tail -2; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg315.png data/verification/sources/refs/ocr/BOOK/315.png && ls -la data/verification/sources/refs/ocr/BOOK/315.png"
}
```


### [2026-09-07T01:43:13.232Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/cbf64342e0fb5b3a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4df074b73ef7e599.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 49502 Sep  6 21:43 data/verification/sources/refs/ocr/BOOK/315.png
```


## [2026-09-07T01:43:19.637Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nL=t[327]\ni=L.lower().find('leig')\nprint(L[:2500])\nEOF"
}
```


### [2026-09-07T01:43:20.830Z] TOOL RESULT

```
t.  lüdö,  -ere,  lüsl,  -sum  , spielen,  zum  besten  halten',  lüdus  (alt  loidos) ,Spiel';
vielleicht  mir.  laidid  (*loid-)  ,treibt  an,  besingt'.
WP.  II  402,  WH.  I  829  f.
667
leJg'  ^^^  leik-  besser  oleig-jk-  .dürftige  elend;,;    Krankheit,  schlechtes Ergehend
1.  Gr.  Xoiyög  , Verderben,  Unheil,  Untergang,  Tod^,  lotyiog  , verderblich, tödlichS'  öXlyog  ,klein';
alb.  lig  ,böse,  mager',  lige  ,Bosheit,  ÜbeP;
lit.  ligä  jKrankheit^,  lett.  liga  ,schwerere  Krankheit,  Seuche^,  ablaut.  lit. päliegis  m.  ds.;
2.  arm.  ai/tat  ,arm,  dürftig,  wenig,  knapp';  Subst.  , armer  Bettler^,  aUat- anam  ,bin  oder  werde  arm;  nehme  ab,  werde  schwach'  (*ali]t-  aus  idg. *oUJco- ;  demnach  ist  auch  das  d-  von  gr.  dXlyog  wohl  alt,  die  Wz.  also  als *{o)leig-lk-  anzusetzen);  air.  llach  ,elend,  unglücklich';  apr.  licuts  ,klein'.
WP.  II  398,  Trautmann  161 ;  wohl  zu  2.  lei-.
2.  {l^ig-)f  ^^S-  ;Gestalt;  von  der  Gestalt  jemandes,  ähnlich  oder  gleich'.
Got.  leih  n.  ,Leib,  Fleisch,  Leiche',  aisl.  llk  ,Leib,  Körper,  Leiche', ags.  llc  ds.,  as.  Ukj  ahd.  llh  (Gen.  llhJiij  fem.)  ,Körpergestalt,  Aussehen, Leib,  Leiche';  got.  galeiks  ,gleich',  aisl.  gllki-j  likr  ,gleich,  gleich  gut',  ags. gelle,  as.  gilik,  ahd.  gilih,  nhd.  gleich  (, dieselbe  Gestalt  habend'),  got. hiUiks  ,wie  beschaffen,  welcher'  usw. ;  got.  leikan,  galeikan  ,gefallen', aisl.  lika  ds.,  ags.  lician  (engl,  like  ,gern  haben'),  as.  llkön  ds.,  ahd. liehen  ,ds.,  gleich  sein,  angemessen  sein',  aisl.  llkr  ,passend',  llkna  ,ver- zeihen'  (,sich  vergleichen') ;
lit.  lyg,  lygus  ,gleich',  lygti  ,gleichen',  lett.  llgt  , übereinkommen',  lldzis ,gleich',  apr.  pollgu  Adv.  ,gleich',  llgint  ,richten'  (rechtlich)  =  altlit.  liginti , Gericht  halten',  lit.  lyginti  ,vergleichen,  gleichmachen  (rechtlich)'.
WP.  II  398  f.,  Endzelin  Lett.  Gr.  508  f.
3.  leig-f  loig-  , hüpfen,  beben;  beben  machen'.
Ai.  rijati  ,macht  hüpfen,  läßt  erbeben',  rijate  ,hüpft,  bebt',  rejdyati ,macht  erzittern,  beben';
npers.  älextan  ,springen,  ausschlagen  (vom  Pferde)',  kurd.  be-lezium ,tanze',  llzim  , spiele';
gr.  sXsU^o),  iXsXi^a  ,mache  erzittern,  schwinge',  eX£XL[*y]-x-^(ov  ,Erder- schütterer'  (dazu  wohl  auch  Xiy-  ,worauf  losstürmen'  in  XiyaLvet  ,stürmt los',  Xlya '  Tax^cog) ;
air.  loig  m.  ,Kalb',  bret.  dial.  lu-e  ds..  lu  ,
```


## [2026-09-07T01:44:03.642Z] AGENT

Now I'll write the verification file.


## [2026-09-07T01:46:49.812Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\ndata = {\n \"pdf_page\": 315,\n \"book_page\": 285,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Lrğ\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"no standard PIE root *l(e)rǵ- exists; the family Nourai draws on is Mann's uncertain lemma *lergō (?) 'tremble' (IEC 681), while the accepted IE root of the 'leap/tremble' family is PIE *leyǵ- / *loyǵ- (Pokorny 667 f. '3. leiĝ-, loiĝ- hüpfen, beben; beben machen'; Watkins leig-³ 'to leap, tremble'; LIV 246 f. *Hreiǵ-)\",\n   \"note\": \"The root box is essentially a re-shaping of ONE uncertain entry in Mann: 'lergo (?) Per. larzidan, inf. ‘tremble’; larze, s. ‘tremor’; MHG, MLG lérken, lirken ‘stammer’' — and Mann's own question mark shows he offers it as a guess, built solely on the Persian verb plus two German verbs. Pokorny, Walde-Pokorny and Watkins know no root of the shape *lrǵ-/*lerǵ-; the nearest real root is Pok. 667 f. 3. leiĝ- 'hüpfen, beben' (Skt. rejati 'makes leap, makes tremble', NPers. ālextan 'to leap, kick', Kurd. be-lezim 'I dance', Gk. elelízō 'I make shake'), to which Cheung (2007) links Proto-Iranian *Hraiz, not *rarz. Decisive difference: the Iranian evidence points to initial *r- (*rarz, whence Pashto rēẓ̌d-, Shughni rēyj-, Sogd. wi-r'rz), the l- of Persian larz being an Iranian-internal dissimilation r…r > l…r; an Indo-European root in *l- therefore cannot be demonstrated from this material, and Cheung leaves *rarz without any PIE entry at all (his 'PIE / LIV / Pok.' line is empty). The gloss 'to tremble' is right for the family; the reconstructed shape and the initial l- are Nourai's (after Mann's) and not shared by the standard handbooks. Note also that Nourai's page number is wrong: Mann's entry stands on p. 681, not 1640.\",\n   \"note_fa\": \"ریشه‌ای هندواروپایی به شکل *lrǵ- در پوکورنی، والده‌ـ‌پوکورنی و واتکینز وجود ندارد؛ نورایی آن را از تنها مدخل مان (IEC) گرفته است که خودِ مان با علامت پرسش «lergo (?)» آورده و تنها بر پایهٔ «لرزیدن» فارسی و دو فعل آلمانی میانه ساخته است. نزدیک‌ترین ریشهٔ پذیرفته‌شده *leyǵ-/*loyǵ- «جهیدن، لرزیدن» است (پوکورنی، ص ۶۶۷ به بعد؛ سنسکریت rejati، فارسی «الختن»، کردی be-lezim). نکتهٔ اصلی این است که شاهدهای ایرانی به *rarz با ر آغازین می‌رسند و «ل» فارسی نتیجهٔ ناهمگونی (dissimilation) دو رِ همنشین در درون خودِ ایرانی است (چونگ، ص ۳۱۵)، پس ریشهٔ هندواروپایی با «ل» اثبات‌پذیر نیست؛ چونگ نیز برای *rarz هیچ ریشهٔ هندواروپایی ثبت نکرده است. معنی «لرزیدن» درست است، اما شکل بازسازی‌شده با احتیاط پذیرفتنی است. شمارهٔ صفحهٔ ارجاع هم نادرست است: مدخل مان در ص ۶۸۱ است، نه ۱۶۴۰.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86\",\n    \"https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"IEC:1640\", \"status\": \"partial\",\n     \"note\": \"The claim's real basis is Mann IEC p. 681 (local IEC.txt leaf 384, line 9688): 'lergo (?) Per. larzidan, inf. ‘tremble’; larze, s. ‘tremor’; MHG, MLG lérken, lirken ‘stammer’. (Isophonic Icel. lerkaður is ‘bruised, sore’. MHG lérc & lirc is ‘left-hand; lame’)'. So the content is Mann's, but (a) the page is 681, not 1640 — the l- section of Mann runs pp. ~660-700 (leaf 384 carries the printed markers 681/682) and the local scan of the item stops at printed p. ~1554, so p. 1640 could not be inspected; (b) Mann marks the root '(?)' and reconstructs *lergō, not *lrǵ-, with no ǵ.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Bd. I p. 667 (POK_02.txt leaf 327)\", \"stance\": \"contradicts\",\n     \"note\": \"'3. leig̑-, loig̑- ‘hüpfen, beben; beben machen’. Ai. rijati ‘macht hüpfen, läßt erbeben’ … npers. älextan ‘springen, ausschlagen (vom Pferde)’, kurd. be-lezium ‘tanze’ … gr. eXeXi^o ‘mache erzittern’' — Pokorny's root for 'tremble' is *leiĝ-/*loiĝ- with a diphthong and does NOT include larzīdan; no *lrǵ- anywhere in the l- section (pp. 661-671 checked leaf by leaf).\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. leig-³ (AHD_watkins1985.txt line 671)\", \"stance\": \"contradicts\",\n     \"note\": \"'leig-³. To leap, tremble. O-grade form *loig- in Germanic *laik- … [Pok. 3. leig- 667.]' — same root as Pokorny's, shape *leiǵ-, and only Germanic reflexes (WEDLOCK, LARK²) are listed; no Iranian material, no *lrǵ-.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *rarz, pp. 314-315\", \"stance\": \"partial\",\n     \"note\": \"Cheung's entry '*rarz ‘to shake, tremble’' gives no PIE line at all (unlike neighbouring entries which read 'PIE *… = LIV: … | Pok.: …'), and only remarks '© This Ir. root may be related to *Hraiz' — i.e. modern Iranian etymology declines to attach an IE root of Nourai's shape; *Hraiz itself is referred to 'PIE *Hreiǵ- ‘to shake’ = LIV: 246 f. | Pok.: 667 f.'\"},\n    {\"src\": \"WLD\", \"where\": \"Band 3 (Register), WLD_band3.txt\", \"stance\": \"silent\",\n     \"note\": \"Only the 1932 index volume is on disk; its OCR (lines 3062, 3132) shows index stubs 'leig- …' and 'lerg- …' under the German keywords but is too garbled to read, and Bde I-II (where WP. II 399, Pokorny's own reference for 3. leiĝ-, stands) are not available locally.\"},\n    {\"src\": \"IEC\", \"where\": \"p. 680 s.v. lerdos (?)\", \"stance\": \"partial\",\n     \"note\": \"Directly above 'lergo', Mann has 'lerdos (?) ‘clumsy, awkward’ … MHG lërz ‘awkward, left-handed’ beside lérzen, v. ‘stammer’' — showing that his lérken/lirken belong to a German 'stammer/lame/left-handed' word-family, which weakens the 'tremble' equation with Persian.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Old Iranian\",\n     \"words\": \"Rarz\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Iranian (Proto-Iranian) *rarz- 'to shake, tremble' is exactly the form modern Iranian etymology reconstructs: Cheung, Etymological Dictionary of the Iranian Verb (2007) 314-315 heads the entry '*rarz ‘to shake, tremble’', and Abolqasemi (FFD, Nourai's own reference) p. 75 writes 'لرز ← فارسی میانه larz ← ایرانی باستان *rarz-'. The stem is unattested in Avestan and Old Persian (Bartholomae and Kent have nothing) and is reconstructed backwards from Middle Persian larz-/lrz-, Parthian lrz-, Sogdian (with *wi-) BSogd. wyr'rz / CSogd. wirz, Chorasmian (with *abi-) βrzyk 'shaking fever', and the East Iranian forms that keep r-: Pashto rēẓ̌dedəl, Shughni rēyj-/ryzd, Yazghulami riwz-, Roshani rawza 'ague'. Nourai's capital 'R' (his notation for a verbal stem) is therefore right, and important: the ancestor of Persian larz had initial r-, and the l- of the West Iranian forms arose later, by dissimilation of the two homosyllabic r's (Cheung 315: 'The initial l- found in the WIr. forms is probably the result of dissimilation of two homosyllabic r… rz: l… rz'). The only weak link is the arrow above this node: attaching *rarz to an IE root in *l- is not supported (see the root note).\",\n     \"derivation_fa\": \"«ایرانی باستان *rarz-» با ر آغازین درست بازسازی شده است: چونگ در «فرهنگ ریشه‌شناختی فعل ایرانی» (۲۰۰۷، صص ۳۱۴–۳۱۵) مدخل را «*rarz «لرزیدن، تکان خوردن»» می‌آورد و ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» ص ۷۵ می‌نویسد: «لرز ← فارسی میانه larz ← ایرانی باستان *rarz-». این ستاک در اوستایی و پارسی باستان گواهی ندارد (بارتولومه و کنت خاموش‌اند) و از روی فارسی میانهٔ larz-، پارتی lrz-، سغدی wyr'rz (با پیشوند *wi-)، خوارزمی βrzyk و صورت‌های ایرانی شرقی مانند پشتوِ rēẓ̌dedəl و شغنیِ rēyj- بازسازی شده است. «ل» فارسی نتیجهٔ ناهمگونی دو رِ همنشین (r…rz > l…rz) در ایرانی غربی است. پس این بخش از ادعای نورایی درست است؛ تنها پیوند این ستاک به ریشه‌ای هندواروپایی با «ل» جای تردید دارد.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2\"],\n     \"ref_check\": [\n      {\"ref\": \"FFD:75\", \"status\": \"supports\",\n       \"note\": \"Abolqasemi p. 75 (PDF p. 80 of incoming/FFD/FFD_pages.txt, printed = pdf-5), s.v. لرزیدن: 'لرزید < فارسی میانه larzīd، مادهٔ ماضی جعلی و از مادهٔ مضارع ساخته شده است. / لرز ← فارسی میانه larz ← ایرانی باستان *rarz-.' — exactly the chain root→Pahlavi→Persian that Nourai draws, and with the r-initial reconstruction.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"CHEUNG\", \"where\": \"pp. 314-315 s.v. *rarz\", \"stance\": \"supports\",\n       \"note\": \"'*rarz ‘to shake, tremble’' with MP, Parthian, Sogdian, Chorasmian and NWIr./NEIr. reflexes, and the note on l- < r- by dissimilation; references EVP: 65; KPF II: 222; Henning 1971: 11a; EVS: 67a; Cabolov 2001: 578 f. (grep 'rarz' CHEUNG.txt, lines 20656-20690).\"},\n      {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch, searched whole text\", \"stance\": \"silent\",\n       \"note\": \"grep -iE 'larz|rarz|rəz' BRT.txt returns nothing: no Avestan cognate is attested, which is consistent with Cheung's purely Middle/New Iranian evidence base for *rarz.\"},\n      {\"src\": \"KNT\", \"where\": \"Old Persian, searched whole text\", \"stance\": \"silent\",\n       \"note\": \"grep -iE 'larz|rarz' KNT.txt: no hits; the stem is not attested in the Old Persian corpus, so 'Old Iranian' here can only mean a reconstruction.\"},\n      {\"src\": \"MON\", \"where\": \"vajehyab (Mo'in) s.v. لرزیدن\", \"stance\": \"silent\",\n       \"note\": \"Mo'in's online entry gives only '(مص ل.) جنبیدن، تکان خوردن' with no origin tag and no Old Iranian form; the print edition's Latin-script etyma are not in the online text.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"rrz, larz\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Both Pahlavi forms Nourai prints are real and are precisely the two spellings the handbooks record. Nyberg, Manual of Pahlavi II (glossary) p. 127: 'larzitan [llcytn’] to tremble …, — MPrthPrs lrz-, MPrs also rrz ‘to shiver with fever’, List 87; NP larzidan' — i.e. Middle Persian has both <lrz>/<llc-> = larz- and the older <rrz> still showing inherited r- from *rarz-, the two differing exactly by the dissimilation r…r > l…r. MacKenzie, Concise Pahlavi Dictionary p. 56: 'larzīdan, larz- [llc-ytn’ | P lrz-, N ~] shiver, tremble', with Parthian lrz- beside it; Cheung 314 adds BMP llc- /larz-/, 3sg. llcyt /larzēd/, 3pl. llcynd /larzēnd/ and Manichaean MP mz/lrz '(fever’s) shivering' (DMMPP 296b). Mo'in's own footnote in Borhan-e Qāteʿ at the cited page confirms it from the Manichaean material. The gloss 'shiver' is right; graphically <l> and <r> are one and the same letter in Book Pahlavi script, so 'rrz' is a transliteration choice, not an error.\",\n     \"derivation_fa\": \"هر دو صورتی که نورایی برای پهلوی آورده گواهی‌شده است: نیبرگ در واژه‌نامهٔ «راهنمای پهلوی» (ج ۲، ص ۱۲۷) می‌نویسد «larzitan [llcytn'] لرزیدن … در پارتی و فارسی میانه lrz-، در فارسی میانه نیز rrz «لرزیدن از تب»» و مکنزی (ص ۵۶) «larzīdan, larz- [llc-ytn' | پارتی lrz-]» را ثبت کرده است. صورت rrz همان ریختِ کهن‌ترِ برجای‌مانده از ایرانی باستان *rarz- است و larz صورت ناهمگون‌شدهٔ آن؛ در خط پهلوی نیز «ل» و «ر» یک نشانه‌اند، پس «rrz» خطای چاپی نیست بلکه گزینشِ حرف‌نویسی است. حاشیهٔ معین بر برهان قاطع (ص ۱۸۹۴) هم صورت مانویِ lrz «لرزیدن از تب» را می‌آورد. ادعای نورایی در این گره درست است.\",\n     \"sources\": [\"https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86\"],\n     \"ref_check\": [\n      {\"ref\": \"FFD:75\", \"status\": \"supports\",\n       \"note\": \"Abolqasemi p. 75: 'لرز ← فارسی میانه larz' — the Middle Persian present stem larz is given as the direct source of the New Persian stem, as drawn.\"},\n      {\"ref\": \"BQT:1894\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qāteʿ ed. Moʿin, p. 1894 (rendered from BQT_v3 pdf p. 691 via tools/ref_page.py; the running head on the sheet reads ۱۸۹۵, so the entry sits at the 1894/1895 opening): 'لرز - بفتح اول، در اوراق مانوی (پهلوی) lrz (لرزیدن از تب) … کردی larz … جنبش با حرکات کوچک غیر منظم و ارتعاش و ترس، لرزیدن' — Moʿin's footnote cites exactly the Manichaean Pahlavi lrz.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"p. 56 (PHD.txt leaf 77)\", \"stance\": \"supports\",\n       \"note\": \"MacKenzie: 'larzīdan, larz- [llc-ytn’ | P lrz-, N ~] shiver, tremble' — Pahlavi stem larz-, Parthian lrz-, New Persian identical.\"},\n      {\"src\": \"NYB\", \"where\": \"vol. II glossary p. 127 (leaf 135)\", \"stance\": \"supports\",\n       \"note\": \"'larzitan [llcytn’] to tremble …, — MPrthPrs lrz-, MPrs also rrz ‘to shiver with fever’, List 87; NP larzidan' — the only source that explicitly records Nourai's variant rrz.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 314 s.v. *rarz, Middle Persian section\", \"stance\": \"supports\",\n       \"note\": \"'BMP llc- /larz-/ ‘to shake, tremble’, MMP lrz ‘(fever’s) shivering’ > DMMPP: 296b; Pres.: IND. 3sg. BMP llcyt /larzēd/, 3pl. llcynd /larzēnd/'.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"larzîdan «لرزیدن (لرزاندن)»; larzesh «لرزش (لرزه ، زمین لرزه)»\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian لرزیدن larzīdan continues MP larzīdan <llc-ytn'> without change (Wiktionary, with Dehkhoda; MacKenzie p. 56 'N ~' = New Persian identical). Morphologically the present stem is the inherited one, larz- < MP larz- < OIr. *rarz-, and the past stem larzīd is a secondary (Abolqasemi: 'جعلی') formation on the present stem with -īd, whence the modern infinitive larzīdan; Borhan-e Qāteʿ p. 1894 s.v. لرزیدن analyses it the same way: 'از: لرز (ء.م.) + یدن (پیوند مصدری)'. The bracketed لرزاندن larzāndan is the regular causative in -ān(i)dan of the same stem. larzeš لرزش is present stem larz- + the verbal-noun suffix -eš 'a shivering, tremor'; لرزه larze (Mann's 'larze, s. ‘tremor’') is the same stem with -a(h) < MP -ag, and زمین‌لرزه zamīn-larze 'earthquake' is a compound with زمین 'earth'. All four forms and their glosses are correct; the Sāʾeb couplet Nourai quotes uses می‌لرزم regularly. Cognates outside Persian: Kurd. larzîn/larz-, Zazaki lerzāyiş, Talyshi larze (Cheung 315), and the loans Urdu/Hindi لَرَز/लरज़.\",\n     \"derivation_fa\": \"«لرزیدن» بازماندهٔ بی‌واسطهٔ فارسی میانهٔ larzīdan <llc-ytn'> است؛ ستاک حال larz- میراث ایرانی باستان *rarz- است و ستاک گذشتهٔ «لرزید» جعلی و ساخته‌شده از ستاک حال با پسوند -īd است (ابوالقاسمی، ص ۷۵). برهان قاطع (ص ۱۸۹۴) نیز همین تجزیه را می‌دهد: «از: لرز + یدن (پیوند مصدری)». «لرزاندن» صورت سببیِ همان ستاک با پسوند -ān(i)dan است، «لرزش» از ستاک حال + پسوند اسم‌ساز -ش، و «لرزه» از همان ستاک + -ه (< فارسی میانهٔ -ag) که در ترکیب «زمین‌لرزه» به کار رفته است. هم‌ریشه‌ها: کردی larzîn/larz-، زازاکی lerzāyiş، تالشی larze (چونگ، ص ۳۱۵) و وام‌واژهٔ اردو/هندی «لَرَز». همهٔ صورت‌ها و معناهای این گره درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86\",\n      \"https://en.wiktionary.org/wiki/%D9%84%D8%B1%D8%B2\",\n      \"https://vajehyab.com/?q=%D9%84%D8%B1%D8%B2%DB%8C%D8%AF%D9%86&d=moein\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1894\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qāteʿ p. 1894 (BQT_v3 pdf 691): 'لرزیدن - بفتح اول و پنجم، از: لرز (ء.م.) + یدن (پیوند مصدری)؛ جنبیدن و مرتعش شدن با حرکات کوچک غیر منظم، طپیدن' and s.v. لرز 'جنبش با حرکات کوچک غیر منظم و ارتعاش و ترس' — both of Nourai's Persian words with these glosses.\"},\n      {\"ref\": \"FFD:75\", \"status\": \"supports\",\n       \"note\": \"Abolqasemi p. 75 s.v. لرزیدن: 'لرزید < فارسی میانه larzīd، مادهٔ ماضی جعلی و از مادهٔ مضارع ساخته شده است' — the New Persian infinitive is built on the Middle Persian present stem, as the arrow says.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"vajehyab.com (Farhang-e Moʿin) s.v. لرزیدن / لرز کردن\", \"stance\": \"partial\",\n       \"note\": \"'لرزیدن (مص ل.) جنبیدن، تکان خوردن'; 'لرز کردن: لرزیدن بر اثر سرما یا تب' — confirms the words and glosses but the online text carries no origin tag or older forms, so it is silent on the etymology.\"},\n      {\"src\": \"PHD\", \"where\": \"p. 56\", \"stance\": \"supports\",\n       \"note\": \"'larzīdan, larz- … N ~' — MacKenzie explicitly marks the New Persian form as identical with the Pahlavi one.\"},\n      {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie, whole text\", \"stance\": \"silent\",\n       \"note\": \"grep -iE 'larz|rarz|lrz' HRN.txt gives only unrelated OCR noise (mlrzä at line 5710, gilrz at 7864): Horn has no article on larzīdan.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien, whole text\", \"stance\": \"silent\",\n       \"note\": \"grep -iE 'larz|rarz|lrz' HUB.txt: no hits at all.\"},\n      {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-hā-ye hend-o-orupāyi (ARY_pages.txt)\", \"stance\": \"silent\",\n       \"note\": \"grep 'لرز' finds the word only inside other articles (e.g. 'معنی این واژه در سانسکریت: لرزیدن' l. 1951, 'به لرزه درآورد' l. 1066); there is no headword لرز/لرزیدن, so Aryanpur assigns it no IE root.\"},\n      {\"src\": \"CHEUNG\", \"where\": \"p. 315, NWIR section\", \"stance\": \"supports\",\n       \"note\": \"'*NWIR: NP larzidan, Kurd. larzin/larz-, (also Sor.) larzān/larze-, Zaz. lerzāyiş/lerzen-, … Tal. larze ‘to shake, tremble’'.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Middle German\",\n     \"words\": \"lurken, lreken\",\n     \"verdict\": \"transcription_suspect\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"lurken, lreken\",\n     \"correct_form\": \"lurken, lërken (Mann prints 'MHG, MLG lérken, lirken')\",\n     \"derivation\": \"The printed page (checked at 300 dpi, copy at data/verification/sources/refs/ocr/BOOK/315.png) really does read 'lurken, lreken : shiver', so the extraction is faithful; but 'lreken' is not a German word — it is Nourai's misprint (e/r transposed) of the form in his source. Mann, IEC p. 681, s.v. 'lergo (?)' writes 'MHG, MLG lérken, lirken ‘stammer’' beside 'Per. larzidan … larze'. Two things follow. (1) The form: MHG/MLG lérken ~ lirken, Early New High German lurken, is real — the Frühneuhochdeutsches Wörterbuch s.v. lurken glosses it '‹stottern, anstoßen, schwer reden‹' (Upper German, ablaut-related to MHG lërcken) and lists lirken and lerzen among its synonyms. (2) The meaning: these verbs mean 'to stutter, stammer', NOT 'to shiver'; Nourai has carried the Persian gloss over to the German box. Mann himself flags the whole equation '(?)', and his neighbouring lemma 'lerdos (?) ‘clumsy, awkward’ … MHG lërz ‘awkward, left-handed’ beside lérzen ‘stammer’' shows lérken belongs to a German 'lame/left-handed/stammering' family, not to a 'tremble' root; Pokorny and Watkins list no such Germanic forms under 3. leiĝ- (their Germanic reflexes are Goth. laikan 'to leap', ON leika, OE lācan). Klein's 'lurken' (p. 1180 s.v. lurk) is a different word again: ME lurken from ME luren 'to frown, lurk' + intensive -k. So besides the misprinted form, the derivation Middle German ← IE *Lrğ 'tremble' is unsupported and the gloss 'shiver' is wrong.\",\n     \"derivation_fa\": \"تصویر صفحهٔ چاپی (با ۳۰۰ نقطه بر اینچ بازخوانی شد، رونوشت در data/verification/sources/refs/ocr/BOOK/315.png) به‌روشنی «lurken, lreken : shiver» دارد، پس خطای خوانش اسکن نیست؛ اما «lreken» واژه‌ای آلمانی نیست و خطای چاپی کتاب است: مان در IEC ص ۶۸۱ زیر «lergo (?)» می‌نویسد «MHG, MLG lérken, lirken ‘stammer’». صورت درست پس «lérken/lirken» (و در آلمانی نو آغازین lurken) است. مهم‌تر آنکه معنی این فعل‌ها «لکنت داشتن، به‌سختی سخن گفتن» است، نه «لرزیدن»: فرهنگ آلمانی نو آغازین (FWB) ذیل lurken می‌آورد «stottern, anstoßen, schwer reden» و lirken و lerzen را هم‌معنای آن می‌شمارد. خودِ مان این برابری را با علامت پرسش آورده و مدخل پیشین او (lerdos «ناشی، چپ‌دست») نشان می‌دهد این خانوادهٔ واژگانی آلمانی به معنای «چپ‌دست/لنگ/الکن» است نه «لرزان». پوکورنی و واتکینز نیز ذیل *leyǵ- تنها laikan گوتی و leika نورسی «جهیدن» را می‌آورند. بنابراین هم شکل واژه خطای چاپی است و هم معنی «shiver» و هم پیوند آن با «لرزیدن» فارسی پذیرفتنی نیست.\",\n     \"sources\": [\"https://fwb-online.de/lemma/lurken.s.3v\"],\n     \"ref_check\": [\n      {\"ref\": \"IEC:1640\", \"status\": \"partial\",\n       \"note\": \"The forms come from Mann but from p. 681, not p. 1640 (IEC.txt leaf 384, printed markers 681/682): 'lergo (?) Per. larzidan … MHG, MLG lérken, lirken ‘stammer’'. Mann's spelling is lérken (not 'lreken') and his gloss is 'stammer' (not 'shiver'); the local scan of the archive.org copy ends at printed p. ~1554, so p. 1640 itself could not be examined.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"vol. 2 s.v. lurk (KLN_1966.txt line 22340)\", \"stance\": \"contradicts\",\n       \"note\": \"'lurk, intr. v., to lie in wait. — ME. lurken, formed fr. ME. luren, ‘to frown, lurk’ …, with the intensive suff. -k' — the only Germanic 'lurken' Klein knows has nothing to do with trembling.\"},\n      {\"src\": \"SKT\", \"where\": \"Concise Etymological Dictionary, whole text\", \"stance\": \"silent\",\n       \"note\": \"grep -iE 'lurken|lerken|lirken' SKT.txt: no hits; Skeat has no such entry.\"},\n      {\"src\": \"POK\", \"where\": \"Bd. I p. 667-668, 3. leig̑-\", \"stance\": \"contradicts\",\n       \"note\": \"Pokorny's Germanic material under the 'hüpfen, beben' root is 'got. laikan ‘springen’, aisl. leika, ags. lācan, mhd. leichen, ahd. leih' — no lérken/lirken/lurken, i.e. the German verbs Nourai cites are not part of this family in the standard handbook.\"},\n      {\"src\": \"IEC\", \"where\": \"p. 680 s.v. lerdos (?)\", \"stance\": \"contradicts\",\n       \"note\": \"'lerdos (?) ‘clumsy, awkward’ … Sp. lerdo; MHG lërz ‘awkward, left-handed’ beside lérzen, v. ‘stammer’' — Mann places the lërz/lérzen/lérken words in a 'clumsy/stammer' group, confirming the gloss 'shiver' is wrong.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-315.json','w',encoding='utf-8') as f:\n    json.dump(data,f,ensure_ascii=False,indent=1)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 -m json.tool data/verification/page-315.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 315"
}
```


### [2026-09-07T01:46:51.460Z] TOOL RESULT

```
written
JSON OK
nodes verified: 4/4
node verdicts: {'confirmed': 3, 'transcription_suspect': 1}
root verdicts: {'plausible': 1}
ref checks: {'supports': 5, 'partial': 1}
books consulted: {'supports': 6, 'silent': 7, 'partial': 1, 'contradicts': 3} | by book: {'CHEUNG': 3, 'MON': 2, 'PHD': 2, 'BRT': 1, 'KNT': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1, 'KLN': 1, 'SKT': 1, 'POK': 1, 'IEC': 1}
```


## [2026-09-07T01:47:11.125Z] AGENT

Done. `verify_check.py 315` reports 4/4 nodes, 0 PROBLEM lines.

**Page 315 (book p. 285)** — 1 real entry (`Lrğ`) + 2 redirects (Lu → Leu, Lup → Wel 2, skipped).

- Root verdicts: plausible 1. Node verdicts: confirmed 3, transcription_suspect 1.
- Ref checks: supports 5, partial 1 (node level). Books consulted: CHEUNG, PHD, NYB, BQT, MON, FFD, POK, AHD/Watkins, WLD, IEC, KLN, SKT, BRT, KNT, HRN, HUB, ARY.

Findings:
- ROOT `Lrğ` "to tremble" (**plausible**): no such PIE root in Pokorny/Walde-Pokorny/Watkins. The whole box rests on one uncertain Mann lemma, `lergo (?)` — and that entry stands on **IEC p. 681, not p. 1640** (Nourai's page is wrong; the archive scan also stops at p. ~1554, so 1640 is uninspectable). Standard root for the family is Pok. 667 f. `3. leiĝ-/loiĝ-` "hüpfen, beben" / Watkins `leig-³`; Cheung gives *rarz no PIE root at all. Also the Iranian evidence points to initial *r-, so an IE root in *l- isn't demonstrable.
- #1 Old Iranian `Rarz` (**confirmed**): exactly Cheung 314-315 `*rarz` and Abolqasemi FFD p. 75 «ایرانی باستان *rarz-»; l- of Persian is later dissimilation r…r > l…r. Unattested in Avestan/OP (BRT, KNT silent).
- #2 Pahlavi `rrz, larz` (**confirmed**): Nyberg II p. 127 explicitly has "MPrs also **rrz** 'to shiver with fever'"; MacKenzie p. 56 `larzīdan, larz- [llc-ytn' | P lrz-]`; Moʿin's Borhan footnote (p. 1894) cites Manichaean lrz.
- #3 Persian `larzîdan, larzesh` (**confirmed**): Borhan p. 1894 "از: لرز + یدن"; FFD 75 (past stem secondary); all four words/glosses right.
- #4 Middle German `lurken, lreken` "shiver" (**transcription_suspect**, `error_in: book`): the page really prints "lreken" (extraction faithful) — Nourai's misprint of Mann's **lérken, lirken**, and Mann's gloss is **'stammer'**, not 'shiver' (FWB s.v. *lurken* "stottern, anstoßen, schwer reden"). So the German link is also semantically disputed; Klein's ME *lurken* 'lurk' is a different word.
- No extraction errors: JSON matches the printed page everywhere (page PNG saved to `data/verification/sources/refs/ocr/BOOK/315.png`; BQT:1894 OCR cached; 4 web pages archived via fetch_source.py).
- Minor note for the owner: the sheet rendered as BQT:1894 (BQT_v3 pdf p. 691) carries running head ۱۸۹۵ — the لرز/لرزیدن entries sit at that 1894/1895 opening.
