# Verification process log — verify-page-157


## [2026-09-05T20:29:04.208Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 157 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-157.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-157.json. Write /home/sfmqrb/git/rishe/data/verification/page-157.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 157` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:29:05.901Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:29:06.635Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:29:06.650Z] TOOL RESULT

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


## [2026-09-05T20:29:06.940Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-157.txt"
}
```


### [2026-09-05T20:29:06.952Z] TOOL RESULT

```
1	=== PDF page 157 (book page 127) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Er 1, Or : to set in motion, excite  (refs POK:327)  PART 2
4	#1 (parent #0) [Indo-European] refs=POK:339 | Ergh : to excite, tremble
5	  #2 (parent #1) [Avestan] refs=POK:339 | ereğant : angry, evil
6	    #3 (parent #2) [Persian] refs=BQT:32 | arğandeh «ارغنده ، آرغنده ، آرغده» : angry
7	  #4 (parent #1) [Sogdian] refs=SOD:57 | `rğnt : greedy
8	  #5 (parent #1) [Greek] refs=AHD | orğ-eyo, orxeisthai : to dance
9	    #6 (parent #5) [French] refs=None | orchestre
10	      #7 (parent #6) [Persian] refs=MON:205 | orkestr «اركستر» : orchestra
11	    #8 (parent #5) [English] refs=AHD | orchestra
12	--- entry 1 ---
13	ROOT Er 2 -> redirect to Ere 1
14	--- entry 2 ---
15	ROOT Erdh -> redirect to Ered
16	--- entry 3 ---
17	ROOT [Indo-European] Ere 1, Re, Er 2 : to split, loosen  (refs POK:332)
18	#1 (parent #0) [Avestan] refs=POK:332; SYN:863; BRT:193 | areda, aredha : side, half
19	#2 (parent #0) [Latin] refs=AHD | rarus : having intervals between, full of empty spaces, sparse ; rěte, rětis : net
20	  #3 (parent #2) [English] refs=AHD | rare ; retina
21	--- entry 4 ---
22	ROOT Ere 2 -> redirect to Eres 1
23	
```


## [2026-09-05T20:29:10.027Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-157.json",
 "description": "Read source JSON for page 157"
}
```


### [2026-09-05T20:29:10.065Z] TOOL RESULT

```
{
  "pdf_page": 157,
  "book_page": 127,
  "entries": [
    {
      "root": {
        "name": "Er 1, Or",
        "lang": "Indo-European",
        "refs": "POK:327",
        "gloss": "to set in motion, excite"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Indo-European",
          "refs": "POK:339",
          "words": [
            {"translit": "Ergh", "gloss": "to excite, tremble", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Avestan",
          "refs": "POK:339",
          "words": [
            {"translit": "ereğant", "gloss": "angry, evil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT:32",
          "words": [
            {"translit": "arğandeh", "gloss": "angry", "script": "ارغنده ، آرغنده ، آرغده"}
          ],
          "note": null,
          "quote": {"text": "پس آن بی درفش پلید و سترگ - به پیش اندر آید چو ارغنده گرگ", "poet": "Daqîqî"}
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:57",
          "words": [
            {"translit": "`rğnt", "gloss": "greedy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 1,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "orğ-eyo, orxeisthai", "gloss": "to dance", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "orchestre", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON:205",
          "words": [
            {"translit": "orkestr", "gloss": "orchestra", "script": "اركستر"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "orchestra", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Er 2",
        "redirect": "Ere 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Erdh",
        "redirect": "Ered"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ere 1, Re, Er 2",
        "lang": "Indo-European",
        "refs": "POK:332",
        "gloss": "to split, loosen"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:332; SYN:863; BRT:193",
          "words": [
            {"translit": "areda, aredha", "gloss": "side, half", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "rarus", "gloss": "having intervals between, full of empty spaces, sparse", "script": null},
            {"translit": "rěte, rětis", "gloss": "net", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "rare", "gloss": null, "script": null},
            {"translit": "retina", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ere 2",
        "redirect": "Eres 1"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T20:29:10.633Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:29:10.670Z] TOOL RESULT

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


## [2026-09-05T20:29:31.863Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','SOD','MON','AHD','BRT','SYN']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:900]); print()\n\"",
 "description": "Inspect refs_online for keys"
}
```


## [2026-09-05T20:29:32.884Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && head -60 data/verification/page-127.json",
 "description": "List verification dir and sample file"
}
```


### [2026-09-05T20:29:33.787Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "loca

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
```


### [2026-09-05T20:29:33.829Z] TOOL RESULT

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
page-129.json
page-130.json
page-131.json
page-133.json
page-135.json
page-136.json
page-137.json
page-138.json
page-139.json
page-141.json
page-144.json
page-146.json
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
----
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
```


## [2026-09-05T20:29:38.337Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f pages: $(grep -c $'\\f' $f)\"; done",
 "description": "Count POK pages"
}
```


## [2026-09-05T20:29:39.298Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ergh-\" POK_01.txt | head -30",
 "description": "Grep ergh in Pokorny"
}
```


### [2026-09-05T20:29:40.012Z] TOOL RESULT

```
== POK_01.txt pages: 352
== POK_02.txt pages: 420
== POK_03.txt pages: 415
```


### [2026-09-05T20:29:40.054Z] TOOL RESULT

```
1990:Dieser   betrachtet  *berghö   ,berge^,  ursprgl.   angeblich   ,bringe  auf  einer ■    Fluchtburg  unter^  als  retrograde  Ableitung  zu  *b7iergh-  ;Berg^  (Gl.  22,  113); 8.  darüber  S.  145.
3058:dergh-  , fassen'.
3917:Lett.  dragät  ,zerren^  dagegen  vermutlich  zu  mndl.  trecken  ,ziehen',  s. 4.  der-  (dergh-,  dreg-)  ,schinden'  und    Mühlenbach-Endzelin  I  488  m.  Lit.
3967:Idg.  dhreugh-  ist  sehr  wahrscheinlich  verwandt  mit  dhuer-  , durch  Täu5 schung  zu  Falle  bringen',  indem  zur  Schwundstufe  *dhru-gh-  aus  *dhuY't sich  neue  Hochstufen  idg.  *dhreugh',  *dhrough-  einstellten.  Mit  dem  er- weiternden gh  wäre  das  von  nhd.  Zwerg  identisch,  wenn  dieses  Wort' nicht  auf  ein  verschiedenes  idg.  dhuergh- , zwerghaft,  verkrüppelt'  (s.  dort) zurückgeht.
4899:air.  Imper.  eirg  ,geh!'  (^ergh-e),  Fut.  regaid  (*rigäti,  idg.  *rgh-)',  s.  obea gr.  egxofiai]  kelt.  or-  in  mcymr.  cyf-or  m.  ,Truppe',  dy-gyf-or  , Erhebung', ad-orth  ,Erregung,  Hilfe'  {*ati-or-to-),  usw.  (Loth  RC  40,  355);  vgl.  auch Ifor  Williams  RC  43,  271   (über  mir.  or  f.  ,Ufer'  s.  Pedersen  KG.  1  206 f.);
```


## [2026-09-05T20:29:45.054Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 334 335 336; do echo \"=== awkpage $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_01.txt | head -60; done",
 "description": "Print Pokorny leaves around p.327"
}
```


### [2026-09-05T20:29:46.880Z] TOOL RESULT

```
=== awkpage 334 ===
Artikel,  na  ,dann*  (*no-ai,  Meillet  Esquisse^  88),  a-n-d  ,dort' ,  (d  aus  idg.  t]  also  nicht  gleich  air.  and  ,hier*,  oben  S.  37,  wozu  noch kypr.  icvöa'  aVzT],  Schwjzer  Gr.  Gr.  I  613);
gr.  vfjg'  TÖ  evi^Qy  dor.  väg  Hes. ;  vrj  , fürwahr',  Instr.  (=  lat.  ne  ds.), valj  valxi  ds.  (vgl.  al:'^  ,wenn',  daliörj  ,also');
lat.  nam  ,denn,  nämlich'  (Akk.  Sg.  f.),  nem-pe  ,denn  doch*,  nem-ut  ds.; ne  , fürwahr',  Instrumental;
unsicher  ob  slav.  *nä,  Interjektion  russ.  na  ,da  hast  du!*  usw.  hierber gehört.
Unsicher  ist  auch,  ob  die  folgenden  Partikeln  hierher  gehören:
ne  in:
ai.  nd  , gleichsam,  wie' ;
av.  yad-na  ,und  zwar' ;
gr.  thess.  SVa,  toVs,  tavSj  mit  Doppelflexion  Gen.  Sg.  rolveog  usw.  ,o(Jß';
lat.  ego-ne,  tü-ne,  denique  (*de-ne-que),  dönicum^  dönec  (*dö-ne-kuomf vgl.  umbr.  arnipo  ,quoad'  aus  *ad-ne-hkorn)^  quandö-ne,  sin  (*si-ne  ,wenn aber  doch'),  usw.;  auch  -ne  in  der  Frage;
ahd.  (ne  iveist  tu)  na  ,(nescis)-ne' ;  -^
alit.  ne  ,wie*,  lit.  n^,  n^gi,  nbgu  ,als*  (nach  Komparativen),  nei  ,wie* (*ne-i),  lett.  ne  ,als*;
akls.  neze^  skr.  nego  ,als*  nach  Komparativen;  aruss.  ni  ds.,  poln.  ni ,wie*  (*ne-{).
321
ßS  in: —     ai.  ^^'-'^^  ,olme';
av.  ya^<^-'^^^   ,gerade   wie',   cid-d-nä  zur   Einleitung  einer  Frage   (=  lat. quid-ne) ; über  gl'-  «V^''^'  ^^s  ^^^^  ^ya}-vr}  sein  könnte,  s.  unter  e,  ö;  y?}  s.  S.  320; lat.  'i^  , für  wahr'  s.  oben  S.  320; -      crot.  -^ict   in   afta-na  Adv.  ,von   hinten',  hinda-na  Adv.  ,jenseits',   usw.; ^J.  -na  in  oha-na  ,von  oben  her';  anord.  per-na  ,tibimet',  usw.; ^\)cr,  v^-ne  , draußen';
fern  bleibt  wohl  phryg.  vi  ,und'  (in  loq  vi  ,und  wer');  über  toch.  A .ne  in  hus-ne  ,welcher',  vgl.  Couvreur  (Tochaarse  Klank-  en  Vormleer  50) ; 5  auch  Schwyzer  Gr.  Gr.  I  612;
^yp.II  336  f.,   WH.  I  339  f.,  370 f.,  386  f.,  404 f.,   Trautmann  7  f.,   195, Schu-yzer  Gr.  Gr.  1  606,  612,  Specht  Dekl.  306.
tn{o)mn',  (o)nomn,  nomn  ,Name'.
Ai.  närna,  Instr.  Sg.  ndmnä,  av.  näma  ,Name';
arm.  anun,  Gen.  anuan,  nach  Meillet  Esquisse  48  aus  *anuwn,  *onomno-, nach  EM^  675  aus  *onömno-',
g\\  ovoiia  (aus  reduziertem  *eno-  mit  Assimilation  e — o),  dial.  ^vv[ia, *tvvfi(x  in  lak.  ^Ew^iayiccgriöag,  (reduziertes  v  entstand  vor  (j,v  aus  dem  Gen. *hoiivog),  dvcüvv^og,  vcbvv(.ivog  ,namenlos' ;
alb.  geg.  emer,  tosk.  emen  (*enmen-)]
lat.  nömen,  -inis,  n.  umbr.  nome,  Abi.  nomne  ,Name'  und  ,Volk';
air.  ainmm  n-  n.,  PI.  anmann  (^^nmn-)]  acymr.  anu,  PL  enuein,  daraus ncymr.  enw]  corn.  Jianoio,  mbret.  Jianff,  hanu,  bret.  ano;
got.  7iamo  n.,  aisl.  nafn  n.,  ags.  nama,  ahd.  7
=== awkpage 335 ===
iamo  m.  ,Navie^ -^  mit Ö-Stufe  afries.  nömia,  mhd.  he-nuomen  , nennen';
apr.  emnes,  emmens  m.  (*enmen-) ;
slav.  *bme,  daraus  *jhme  in  aksl.  ime,  skr.  ime,  acech.  jm^,  Gen.  jmene, russ.  imja ;
toch.  A  üem,  B  nom;
hitt.  la-a-ma-an  (läman),  mit  Dissimilation  des  Anlauts;
vgl.  finno-ugr.  näm,  nam,  nem,  namma,  magyar.  nev  ,Name*.
WP.  I  132,  Feist  369  f.,  Schwyzer  Gr.  Gr.  I  352,  Hirt  Idg.  Gr.  II  98,  121.
enos'  oder  onos-  n.  ^Last^
Ai.  dnah  n.  ^Lastwagen^  =  lat.  onus,  -eris  ,Last^  {onustus  ,beladen^, oneräre  ^beladen^).
Dazu  vielleicht  gr.  dvla,  äol.  dvla  ^Plage^^^  änog,  tiviägög  ^lästig'  (die dialektische  Verteilung  von   dvla  :  dvla  wie  bei   der  Präp.  dvdiSv)]    nach
21
322
f
Wackernagel    Gl.  14,  54  L   aber    dissimiliert   aus    *a(.aJ^a  =  ai.    dmiva  f , Plage'  (s.  unter  07n9').
WP.  I  132  f. ;  s.  auch  unter  enek-.
enq-,  onq-  Schall wurzel:  ,seufzen,  stöhnen^  (ei^q-),  ^brüllen,  brummen^  ipna,) beide  Vokalisationen  also  mit  verschiedenem  Gefühlswert,  so  daß  v\^j leicht  von  zwei  verschiedenen  Schallnachahmungen  zu  sprechen  wäre.' Daneben  freilich  eine  Wurzelform  auf  Media  eng-,  ong-,  ng-  ^stöhnen  ' seufzen',  ohne  solche  Bedeutungsscheidung  nach  der  Vokalisation. Gr.  dy-Käoiiai  , schreie,  brülle^  (vom  Esel),  oy.vog  ,Rohrdommel^  i*oyy.vog)* alb.  nekönj,  ^Qg.  angöj  ,ächze,  seufze,  klage'  (*enq-)] lat.    uncöy   -äre   ,vom  Naturlaut   des   Bären'.    Aber  cymr.  och  jgemitus* Interjektion  ,ach!',  ist  nicht    aus    *OTdq-   herleitbar   und    avoIiI    sicher   eine junge  interjektioneile  Schöpfung;
slav.  *j^6ati,  russ.-ksl.  jaSu,  jacati  ,seufzen^,  jaklm   ^uoyiXdlog,   aegre loquens',  russ.  mdartl.  jacdth  ,stöhnen,  klagend  rufen'. Mit  Media:
mir.  ong  ,Stöhnen,   Seufzer,  Wehklage',   dazu  wohl  air.  ennach  ,Krähe' (aus  *eng-n-äka)  und  enchache  f.  ,scurrilitas' ;
mnd.  anken  ,stöhnen,  seufzen',  norw.  mdartl.  ank  ,Gewimmer,  Seufzen,  ^,. Kummer,  Keue^,  dän.  ank,  anke  ,Klage,  Beschwerde',  wozu  ablautend  ^J dän.  ynke,  schwed.  ynka  ,bemitleiden,  bedauern,  beklagen',  allenfalls  auch  '*£ nhd.  Ujike  nach  ihrem  kläglichen  Ruf  (doch  mhd.  Schallwort  üche  ,Kröte';  x s.  noch  Kluge  ^^,  der  Kreuzung  dieser  üche  mit  mhd.  ahd.  unc  ,Schlange*  »T; [s.  oben  S.  44]  erwägt).  "^
Ein  Schallwort  ist  lit.  üngti,  üngau  ,wimmern  wie  ein  Hund'.  "?
WP.  I  133.
ent-  (besser  ant-?)  ,anzetteln,  weben'  (??).  '^
Ai.  dtka-h  m.  ,Gewand,  Mantel',  av.  adka-,  atka-  m.  ,Oberkleid,  Mantel, (*nt'ko-s) ;
alb.  enty  int  ,webe,  zettle  das  Gewebe  an'  (*ent-{-  oder  *ni-i-);
gr.  att.  ärro^ai  (*nt-io-)   ,webe',  dia^o^ai    ds.  (vgl.    Deb runner  IF.  21,  >«; 216),  ä(T^a,  ölaa^a   ,Kettenfaden' ;    falls   aber    (Petersson    Heterokl.    262)  jy_^, äv
=== awkpage 336 ===
taQ  ds.,  dvvrJQLog  ds.  dazugehören,  ist  eher  *ant'  als  Wurzel  anzusetzen.   1'^^ Jedoch  besteht  bei  gr.  Kulturwörtern  der  Verdacht  voridg.  Herkunft  und  '^:7'
air.   etid   ,bekleidet',   etiud   , Kleidung^   könnten    sekundär   zu   etach   ds. {*en-togo-)  gebildet  sein;  -^^  -^^
auch   die   Gleichung  ai.  dtka-h  :  gr.  dayf.6g  ,Haut,   Schlauch^  ist  der  Be- deutung wegen  zweifelhaft;  gr.  ^tqlov,  dor.  ßV^iov  , Kettenfaden'  sind  vorgr.  -*^ Herkunft  verdächtig.
WP.  I  134.
"Ä?-'
323
cpero-  ;Eber^
Lat.  aper,  aprl  ,Eber^,  umbr.  Akk.  PL  apruf,  ahrof,  Akk.  Sg.  ahrunu, Akk.  PI.  ahrons  ,Scbweine'  (doch  über  lat.  Aprönius,  mars.-lat.  Aprufclano siehe  Schulze  Eigennamen  lll,124f.);  a  wohl  nach  caper-  abgeleitet  lat. aprugnus  ,vom  Eber^  mit  Suffix  -gno-  zur  Wz.  gen-;  hierher  vielleicht jer  PN  Eprüis]
germ.  *ebura-,  altn.  jgfurr  m.  ,Fürst^  (in  übertragener  Bedeutung, eigentlich  ,Eber'),  ags.  eofor  m.  ,Eber',  mndd.  ever  ahd.  ebur,  nhd.  .EJier.
Mit  (analogischem?)  u-Vorschlag  gehören  asl.  veprt  m.  ,Eber',  skr. vepar  (Gen.  vepra),  poln.  tüieprz  (Gen.  wieprza),  russ.  reprb  (Gen.  veprja) hierher;
lett.  vepW«  ds.  (ON  lit.  Vepriai  Plur.,  und  apr.  Weppren)  ist  nicht  dem Slav.  entlehnt,  sondern  urverwandt;
unklar  ist  thrak.  eßqog  ,Bock^
WP.  I  121,  WH.  I  56,   Trautmann  351.
epi,  opi,  pi  (auch  mit  Hochstufe  -ei,  -oi  in  der  Schlußsilbe)  ,nahe  hinzu, auf — darauf,  auf  — hin',  zeitlich  ,dazu,  darauf,  Örtlich  ,hinter,  nach* (auch  ,bei  etwas  herunter'?  so  z.  T.  die  germ.  Formen);  teilweise  in der  Bedeutung  mit  ebhi,  obhi  zusammengefallen.
Ai.  dpi  ,auch,  dazu'  (Adv.),  selten  ved.  Präposition  m.  Lokativ  ,bei,  in', Präfix  api-,  pi-  ,zu,  bei'  {jpi-  in  pi-dhäna-  n.  ,das  Zudecken,  Decke,  Decket, pi-naliyati  , bindet  an,  zu',  py-ükma-  , Überzug  des  Bogenstabes'  :  gr.  7T.T-vxri , Falte,  Schicht',  wenn  aus  *7ii-vx(3t,  fCTvaacj  ,lege  zusammen,  falte',  pida- yati  ifcie^w,  s.  *sed-)-
av.  aipi,  ap.  apiy,  adnominal  ,über — hin,  bei  (Akk.),  bei  (zeitlich,  Lok.), nach  (zeitlich,  Instr.)',  Adv.  ,dazu  auch,  desgleichen  auch,  besonders; hernach,  später',  Präf.  ,hin*;  mit  höchst.  Schlußsilbe  av.  ape  ,nach'  (m. Akk.),  vgl.  apaya  Adv.  ,hernach,  künftig',  -pe  hervorhebende  Part. ;
arm.  ev  ,und,  auch';  *pi  im  Anlaut  h-  einiger  Verba,  wie  h-aganim ,ziehe  mir  an'?
Gr.  iftl,  h'm  ,auf  zu,  an',  adnominal  mit  Dativ  (=  idg.  Lok.,  Instr., Akk.,  Gen.,  Präfix,  eTiioaov  %d  Vaisgov  yevöiievov  Hes.  (d.i.  wohl  ,Nach- kommenschaft',  ürundf.  *a7ii,-Tio-,  Schulze,  Kl.  Sehr.  70 ff.,  675),  ttl-  Präfix (s.  oben);  opi  in  hom.  OTti-d-siv)  , hinten,  hinterher',  ion.  att.  bnLadsiy) ds.  (-er-  nach  7VQ6ad-e{v),  vgl.  auch  d7iLa((s)(ü  , hinten,  rückwärts';  hernach' {*opi-tiö),  drciazaTog  »hinterster,  letzter';  ÖTt-wQa  , Herbst',  S.  343);  vermut- lich (mit  idg.  Kontraktion  von  *opi-oq**  zu  *oplq**,  zu  *oqu-  , sehen')  örti- nevcü  ,gaffewonach',  Ttagd^svoTtl
```


## [2026-09-05T20:29:53.632Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 340 345 352; do echo \"=== awkpage $n ===\"; awk 'BEGIN{RS=\"\\f\"} NR=='\"$n\"'' POK_01.txt; done",
 "description": "Print Pokorny pages 327, 332, 339"
}
```


### [2026-09-05T20:29:55.624Z] TOOL RESULT

```
=== awkpage 340 ===
  *re-skö  in  apers. rasatiy  .kommt,  gelangt',  np.  rasad  ds. ;
ai.  sam-ard-  m..  sam-drana-  n.  .Kampf.  Wettstreit',  av.  liam-ardna-,  apers. Jiam-arana-  n.  .feindliches  Zusammentreffen.  Kampf,  av.  hamara-  m.  (und mit  th-Forma-ns  hamdvdd-a-  m.)  .Gegner.  Widersacher';  ai.  irya-  ,rührig. kräftig,  energisch'  (kann  zur  z-Basis  gehören),  irin-  .gewaltig,  gewaltsam'. drtha-  n.  m.  .(*wozu  man  gelangt)'  .Angelegenheit.  Sache.  Geschäft;  Gut, Vermögen.  Vorteil',  av.  ard^a-  n.  .Sache.  Angelegenheit.  Obliegenheit. Rechtsstreit' ;
ai.  ft^-,  fti'  f.  .Angriff.  Streit',  av.  -drdti-  .Energie'  (vgl.  abg.  rath)]
ai,  arta-  .betroffen,  versehrt,  bedrängt,  leidend',  ärti-  f.  .Unheil.  Leiden' {^ä-xta-,  -rti-))
ai.  drna-  .wallend,  wogend,  flutend',  m.  ,Woge.  Flut',  dimas-  n.  .wallende Flut'  (formell  =  gr.  eqvog  n. ;  vgl.  S.  328  ahd.  runs)^  arnavd-  .wallend, wogend';  m.  .Flut,  wogende  See'  (wo- Weiterbildung  zu  drna-?  oder  in alter  formantischer  Beziehung  zu  j-nöti?  Letzteres  ist  sicher  für:)  av. ardnu-  m.  .Kampf.  Wettkampf'  ( :  ahd.  ernust  S.  331) ;
von  der  themat.  Wurzelf.  (e)re-  ai.  rdiia-  m.  n.  .Kampf  (versch.  von rana-  m.  .Lust')  =  av.  rdna-  n.  .Treffen.  Kampf.  Streit';  av.  räna-^  rqna-  m. .Streiter.  Kämpfer';
arm.  y-arnem  .erhebe  mich,  stehe  auf;  nach  Pisani  Armen.  4  dazu  ore-ar .Leute'  (s.  unten  lat.  orior)]  mit  -dh-  (vgl.  S.  328  igs-S^w,  igsd^i^ü),  dgo- -^vvoi) :  y-ordor  .pronto'.  yordorem  .ermuntere,  wecke,  reize';  arm  .Wurzel' ( :  ^Qi-iEvog) ;  ordi,  Gen.  ordvoy  .Sohn'  (*ordhno) ;
gr.  ogvV(j,i  .errege,  bewege'  (:  ai.  T'^öti]  vgl.  Schwyzer  Gr.  Gr.  I  696/?; das  0  nach  dgso^ac?),  Aor.  (hgoa,  ^gogov,  h'gGo),  Med.  })gwf.iai^  d)gTO  .erhob sich'.  Fut.  dgov{.iai,  them.  Aor.  djgsTO,  Partiz.  bg^evog^  Perf.  Ugwga  .bin erregt';  mit  og-  als  Iterativvokalismus  ögs-oi-iai,  -ovro  .aufbrechen',  mit er-  noch  egero '  wgurjd^T]  Hes..  egoeo '  ÖLsyslgov  Hes..  sgffr] '  ögfirjcr]  (die  dann durch  öjgsro,  b'gaeo  verdrängten  Formen);  ein  Präs.  *l'QWfiL  (wie  xLgvrji.iL) folgt  aus  dem  kret.  Zevg  "'EnigvvTLog  (Schwyzer  Gr.  Gr.  I  695);  -ogvog in  vsogTÖg  .neugeboren'. d-eogrog  .himmlisch',  usw.;  Kvv-,  ^vY,-6gTag, ^ä-igrrjg] hom.  o-ögog  .günstiger  Fahrwind'  {*ögJ^og,  .das  Schiff  treibend'),  ^gog  m. ;Antrieb';
328
•  ':^
mit  g"22-Erweiterung  eQXO^at  ,komme^  (nur  Präs.),  dgx
=== awkpage 345 ===
nngti  ji^co^slv',  ririQtis^  ,ruere';  aruss.  rint  ,Sand- bank',  klr.  rin  ,Sand,  Flußgeröll'  (vgl.  ai.  renn-);  in  anderer  Bed.  (s.  oben zu  lat.  rlvlnus)  abg.  rbVhm  ,Nebenbuhler'  rhvenije  ,£Qig,  igd^sia^  6ech.  fevniti ,nacheifern',  poln.  rzewnic  ,bewegt  machen'.
Mit  s-Erw.  bsl.  *reistiö  in  abg.  ristq,  ristati  ,laufen',  riskanije  ,cur- sus',  lit.  raistas  (,Laufzeit'  =)  ,Brunstzeit',  lett.  rlests  ds.,  lit.  ristas ,schnell',  ri§ciä  Instr.  Sg.  ,im  Galopp'.
e.  Basis  ereu-]  er-nu-  ,Wettkampf',  or-uo-  ,eilig'.
Ai.  fnöti  (Perf.  ära  aber  idg. ^*öra),  arnavd--^  av.  ardnu-  s.  oben  S.  327;
ai.  drvan-,  drvant-  ,eilend,  Renner',  av.  aurva-,  aurvant-  ,schnell,  tapfer' ; vielleicht  av.  auruna-  ,wild,  grausam,  von  Tieren';  sehr  unsicher  ^\.  rü-rd- jhitzig,  vom  Fieber';
gr.  0Qvv(.u,  odgog  s.  oben;  altes  Kausativ  doovw  ,stürze  mich,  stürme los',  ävoQOVo)  ,springe  auf  (wohl  als  *oqov\<j]o}  zur  s-Erw.,  s.  unten);  vgl. Schwyzer  Gr.  Gr.  I  683;
lat.  ruö,  -ere  ,rennen,  eilen,  einherstürmen';
mir.  rüafhar  {*reu-tro-)  ,Ansturm',  cymr.  rhuthr  ds.,  air.  rü(a)e  ,Held' {*reu-io-)]  hierher  die  gall.-brit.  FIN  *Ai-vä,  engl.  Arroio,  frz.  Erve,  Auve (*fwä);  messap.  FIN  Arvö]
as.  aru,  ags.  earu  ,hurtig,  bereit,  flink',  aisl.  grr  ,rasch,  freigebig^ {*arioa-  =  av.  aui-va-]  hierher  als  ursprüngl.  ,freigebig'  vielleicht  auch got.  arwjö  ,unentgeltlich,  umsonst',  ags.  earwunga,  ahd.  ar{a)wün  ,gratis, frustra',  arod  ^kraftvoll,  flink';  ahd.  ernust  s.  S.  328.
332
f
ag'S.  reow  ,aufgeregt^   stürmisch,   wild,   rauh^,  got.  unmana-rlggics  ,wil(i grausam^  ,  -k;.
Erweiterung  reu-s-:
Ai.  rösatij  rusdti  ,ist  unwirsch^,  rusitd-,  rustd-  ,ergrimmt^;  ..^^
schwed.  rüsa  ,daherstürmen,  eileii'^,  mnd.  rüsen  ,rasen,  toben,  lärmen«  ^ rüsck  ,Rausch^,  aisl.  rosi  ,Sturmbö^,  raust  ,Stimme^,  aschwed.  ruska  ,her-  B vorstürmen,  eilen^;  ^^'
[aber  got.  raus  n.,  mit  gramm.  Wechsel  aisl.  reyrr  m.,  ahd.  röi^  ^Schilf.  - rohr^,  rörea  ,Röhre^  (^rauziön),  mit  Stammbetonung  (wie  got.)  schwed.  I. rysja^  ahd.  rüssa,  rüsa,  riusa  f.  ,Reuse^,  weitergebildet  mit  Ä-Suffix  a^s.  '■^- rysc  f.,  mhd.  rusch(e)  f.  ,Binse^,  bleiben  wohl  fern];  ^
lit.  ruosüs  ,geschäftig,  tätigt,  lett.  ruo§s  ds.,  lit.  rnoHü,  ruosiaü,  rimti ,besorgen^,  reflex.  ,sich  bemühen^;
slav.  "^ruchh  in  russ.  ruch  ,Unruhe,  Bewegung^,  rwcÄww^
=== awkpage 352 ===
1.  ero-,  re-,  er(e)-  , rudern;  Ruder';  ero-ter-  , Ruderer'.
Ai.  ari-tra-  m.  , treibend;  Ruder',  n.  (auch  a?'i7ra-)  , Steuerruder',  aritdr ,Ruderer';
gr.    igs-TTjg    ^Ruderer',    Ersatz    für    *iQSTrjQ   (=  ai.    aritdr-)    wozu   fem 'EgevQicc  ON  erhalten,  egiaaci),  att.  iosTToj  , rudere'  (*€gsT-i(x),  Denominativ)  ,J.- iosTfiög,  PL   igsTf-id    (statt   *6Qfji.iog  =  lat.    remus,    nach    igsTrjg,    Schwyzer  '^ Gr.  Gr.  I  493 2)  , Ruder',   hom.  elgsalrj   (sl-  metr.  Dehnung)  ,das  Rudern'  >''"<' UTTTj^srjyg  , Ruderknecht,  Matrose';   übertragen:  , schwer  arbeitender  Diener' Tievrrjgrjg  ,Fünfdecker';    slyiöa-ogogf   Tgiay-öw-ogogy    ion.   Tgirj-aörT-egog   usw. (die  -o^og-Formen  durch  gr.  Assimihation  von  o  aus  £?);  äh-rjgrjg  ,das  Meer durchrudernd',  dixcp-T^grjg  ,doppelruderig',  Tgirjgrjg  ,Dreidecker';
lat.  remus  , Ruder',  triresmom,  septeresmom  Columna  rostrata  (Gruudf. eher  *re-smo-  als  *ret-smo-) '^
air.  o'ä-  , rudern',  imb-rä-  »rudern,  zu  Schiffe  fahren'  (z.  B.  Impf,  -raad, Perf.  imm-rerae  ,profectus  est',  Verbn.  imram  ,das  Rudern'),  räme  , Ruder';
anord.  röa,  ags.  röivan,  mhd.  rilejen  , rudern';  ahd.  ruodar^  ags.  rödor  n. ,Ruder',  anord.  röpr  (w-St.  *röpru-)  ,das  Rudern';
lit.  iriiXy  irti  , rudern',  irklas  , Ruder',  ablaut.  apr.  arttoes  f.  PL  ,Schiffsreise'.
WP.  I  143  f.,  Trautmann  105.
2.  era-,  re-  , ruhen*;  re-uä,  rö-uä  ,Ruhe'.
Av.  airime  adv.  , still,  ruhig'  {^et^-mo-),  armae-iad,  -Uä  , ruhig  sitzend,  !| still  stehend'  (*e?--mo-  oder  *e7'a-mo-;  bloß  graphisches  -i-  sieht  in  airime  % Meillet  Dial.  indoeur.  Q^) ;  ^^  '
gr.  ^gtori  (7tol€[.iOLo)  »(Kampfes) ruhe',  egwiw  , lasse  ab'  =  anord.  ?'ö,  ags. röw,  ahd.  ruoica^  nhd.  Ruhe  (*röwö),  ablautend  mit  ahd.  räwa  ds. ;  dgd-fisvai' j)avxd^€Lv  Hes.  (?) ;
cymr.  araf  , ruhig,  mild,  langsam'  {*er9-mo-) ;
nach  Rozwadowski  R.  Sl.  6,  58  f.  angeblich  hierher  der  Name  der  Wolga Pä  als  , ruhiges,  stehendes  Wasser'  aus  *Rava  (mordvin.  Ravo)  zu  lit. rova  (=  germ.  *röuö  ,Ruhe'),  lett.  räwa  , stehendes  Wasser',  lit.  FlN Rova  =  slav.  Ravu]  besser  oben  S.  336.
Anreihung  von  gr.  egcjg  , Liebe',  sga^ac  , liebe'  (vgl.  ai.  rdmate  ,ruht, steht  still,   läßt  sich   genügen,  findet  Gefallen,  pflegt  der  Liebe')  ist  eine
339
höchstens  ganz  schwache  Möglichkeit  (s.  Boisacq  m.  Lit.,  Persson  Beitr. 667).
Eine  s-Erw.  *r-e-s-,  r-o-s-  in  got.  rasta  ,Meile'  (,Rast'),  anord.  r^s^  f. ^Wegstrecke',  ahd.  rasta  L  ,Ruhe,  Rast,  Wegstrecke,  Zeitraum',  as.  rasta und  resta  (*rastja)  ,Ruhe,  Lager',  ags.  rcest  und  rest  ,Ruhe,  Ruhelager, Grab';  ablautend  m
```


## [2026-09-05T20:30:05.797Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== awk 353 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==353' POK_01.txt\necho \"=== awk 354 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==354' POK_01.txt | head -40",
 "description": "Print Pokorny p.339-340"
}
```


### [2026-09-05T20:30:07.517Z] TOOL RESULT

```
=== awk 353 ===
nd.  o-uste,  roste  ,Ruhe,  Wegstrecke',  spätmhd.  o-ust ,Ruhe';  got.  razn  n.  ,Haus',  anord.  rann  ds.^  ags.  cern,  ren  n.  ,Haus'  (mit merkwürdiger  Bed.  o^cßsn  n.  ,Planke,  Zimmerdecke'),  afries.  ern  in  ßä-ern ,Vieh-haus';  unsicher  ags.  reord  {^rezdo)  f.,  gereord  n.  , Mahlzeit,  Fest, Futter',  anord.  greddir  , Fütterer,  Sättiger'  {^garazdlz),  grenna  , füttern' {*ga-raznian).
Vgl.  rem-,  das  wie  res-  mit  (e)rd-  zusammengestellt  wird.
WP.  I  144  f.
er(9)d-  {,r{d)d-\  er{9)dh-  ,hoch;  wachsen'.
Av.  drddva-  ,hoch';
lat.  arduus  ,hüch,  steil' ;
gall.  Arduenna  silva,  air.  ard  (*fduo-)  ,hoch,  groß';  cjmr.  hardd  , schön';
aisl.  grdugr  , steil'  setzt  (wie  allenfalls  auch  drddva-)  eine  Parallelform auf  dh-  fort,  indem  verschiedene  Erweiterungen  von  er-  ,(in  Bewegung setzen)   hochbringen'  durch   dh   (vgl.  ÖQodvvcj  ,treibe  an'  usw.)  vorliegen.
Sicher  mit  dh  lat.  ai-hor  ^^-^n^'»  wozu  kurd.  är-  aus  *ard-  ,Baum'  in ärzang  ,die  durch  Wind  und  Wetter  verursachte  dunkle  Färbung  auf  den Bäumen*,  eig.  ,Baumrost' ;
alb.  rit  , wachse',  aus  fd-  oder  fdh-'^
slav.  *orstg,  abg.  rastg,  russ.  rastü,  cech.  rostu  usw.  , wachse*  (*ord-, ordh-to) ;
toch.  A  orto  , empor'.
WP.  I  148  f.,  II  289  f.,  WH.  I  64  f.
ergh'  , schütteln,  erregen,  beben'  od.  dgl.,  wohl  Erweiterung  von  er-  ,in Bewegung  setzen'.
Ai.  2'^Ä^y«^i  »bebt,  tost,  stürmt';
gr.  ÖQXEO)   ,7tall(x),  %Lve(x)\   meist  ÖQxaonai   ,tanze,   hüpfe,  springe,   bebe'.
Wegen  der  in  3.  er-  ebenfalls  vorliegenden  Bed.  ,1'^fg'  u.  dgl.  können  dazu in  Beziehung  stehen:
av.  drdyant-  ,arg,  abscheulich*;
ahd.  ar{a)g  ,feig,  träge,  böse,  arg',  ags.  earg  ds.,  aisl.  argr  und  mit Metathese  ragr  ,unmännlich,  wollüstig,  schlecht' ;
lit.  ariüs  ,lüstern,  sinnlich*.
WP.  I  147  f.
22*
340  9
erk"'  , strahlen;  hell  klingen,  lobpreisen'.
Ai.  drcati  , strahlt;  lobsingt,  begrüßt,  ehrt',  arkd-  m.  ,Strahl,  BlitzstraL)      1 Sonne,    Feuer;   Lied,   Sänger'   (=  arm.  erg),    rc-,    Nom.  Sg.  fÄ  f.  ,GlaiuI Gedicht;  Vers',  j-kvan-  ,lobpreisend,  jubelnd';  *
arm.  erg  ,Lied' ;  . .
air.  erc  , Himmel*,  mir.  suairc  , angenehm,  schön,  strahlend'  (*su-erhiU)* toch.  A  yärk,  B  yarke  »Verehrung'  (Pedersen  REtlE.  3,  18);  V'
hitt.  ar-ku-ua-nu-un  ,ich  betete'  (arkuannn) ;  anders  Hendrikseu  45 und  74.
WP.  I  147,  
=== awk 354 ===
Marstrander  ZceltPh.  7,  360;  vgl.  oben  S.  65.
ers-  :  orsos  , Hinterer,  Schwanz*.
Arm.  or  ,  Hinterer'  (meist  PI.  or-k,  i-St.);
gr.  bggog  m.  , Hinterer'  (dazu  oigd  f.  , Schweif  aus  *ors{a)  =  ^|;*
ahd.  a?'s,  ags.  ears  m.,  aisl.  ars,  rass  ,  Arsch'  =  '  ^
hitt.  a-ar-ra-d§  (arras),  Dat.  ar-ri-i§-äi  (arrisi)]  das  -si  enklit.  Pronomen* e-stufig    air.  err    (*ersa)    f.  , Schwanz,    Ende*    (auch    des    Streitwagens)
davon  eirr  , Wagenkämpfer'  (*ers-et-s),  Gen.  erred]
wird   vielfach   als    »Erhebung,  vorstehender  Körperteil'  zu   3.  er-  (oben
S.  326)  gestellt.  'flf
WP.  I  138,   Couvreur  H  98,  Pedersen  KG.  II  101.  '  '""^^^  -
es-  jSein*,  Kopula  und  Verbum  Substantivum ;  bildet  ursprünglich  nur  ein duratives  Präsens  wird  daher  einzelsprachlich  vielfach  durch  die Wurzel  bheud- :  bhü-  suppliert.
1.  Ai.  dsmi,  dsi,  dsti,  smds,  sthd,  sdnti,  av.  ahmi,  3.  Sg.  asti,  3.  PI.  h9nti, apers.  amiy]
arm.  em,  es,  e;
gr.  hom.  att.  bliil  (=  emi,  äol.  I'^ujut,  dor.  ^^t),  el  (=  ei  aus  *esi,  nur att.,  hom.  dg,  idai),  iati,  Biy,sv  (wie  et^i;  att.  ia^iev  wie  ^are]  dor.  ii^eg), iaze,  aioi  (dor.  ivTi),  Dual  iatöv]
venet.  est,
alb.  jam  (*esmi) ;
lat.  sum  (durch  Einfluß  der  1.  PI.),  es(s),  est  (Inchoat.  escit,  wie  gr. Iffx«),  sumus,  estis,  sunt  (Inchoat.  escu7it)]  osk.  süm,  est  (ist)]  umbr.  est]
air.  (nur  als  Kopula)  am  (*esmi),  a-t,  is,  ammi  (*esmesi),  adi-h,  it  {*sentl, acymr.  hint) ;
got.  im,  IS,  ist,  3.  PI.  sind  {*senti)]  aisl.  ew,  est  (ert),  es  (er)]  ags.  eom (nach  beom),  northumbr.  am  (*os-7n),  eart  (Endung  des  Präteritopräs.);  is] 3.  PI.  northumbr.  aron  (*os-nt),  usw. ;
341
alit.  esml,  (heute  esü,  dial.  esmü)  esl,  esti,  Dual  alt  und  dial.  esvä,  estaü und  estä-,  lett.  esmu  (dial.  esit),  esi  usw.;  apr.  asmai,  assai  (essei),  est  (ast);
aksl.  jesm7>,  jesi,  jesh  {*esti),  jesrm,  jeste,  sqH  {==  lat.  sunt) ;  Dual  jesvl jesta,  jeste,  usw.;
toch.  Präs.  B  3.  Sg.  ste,  star-  (mit  Enklitikon),  3.  PI.  skente,  stare, skentar-  Imperf.  A  1.  Sg.  sem,  2.  Sg.  set  usw.,  B  sai{-),  mit  Optativformans idg.  -Ol-  (nach  Pedersen  Tochar.  161  soll  auch  B  nes-,  A  nas-  ,sein'  die AVurzel  es-  enthalten,  das  Präverb  n-  sei  mit  der  Postposition  B  ne  iden- tisch??);
hitt.  e-es-mi  (esmi),  3.  Sg.  e-es-zi  (eszi),  3.  PI.  a-§a-an-zi  (asanzi ;  das  as durch  Vokalharmonie  aus  *es-?).
2.  Wichtige  Übereinstimmungen:
Imperf.  ai.  äsam^  äs,  äs,  bzw.  Perf.  äsa,  äsitha,  dsa,  PI.  äsma,  ästa, äsan,  Dual,  �
```


## [2026-09-05T20:30:21.872Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"rärus\\|rarus\\|rete\\b\\|rëte\" POK_01.txt | head -20\necho \"---- search Auflösung near er\"\ngrep -n \"aufreißen\\|auflösen\\|Auflösung\" POK_01.txt | sed -n '1,40p'",
 "description": "Grep rarus in Pokorny"
}
```


### [2026-09-05T20:30:21.952Z] TOOL RESULT

```
4966:ganz  unsicher  lat.  rärns  .locker,  nicht  dicht,  selten^  {*er9-rö-s),  eher glaublich  rete  ,Netz,  Garn'  (vgl.  unten  lit.  rMs,  lett.  reta);
4967:lit.  yrii,  zrti  ,sich  auflösen,  trennen,  pairas  ,locker';  rZtis  m.  ,BastsieV (mit  unursprünglichem  Schleifton,  wie  oft  in  i-Stämmen),  lett.  reta,  rete .Narbe',  rem  rudzi  ,undicht  stehender  Roggen';  lit.  eftas  ,weit,  geräumig' (,*auseinanderstehend');  von  der  leichten  Basis  retas  ,dünn,  weitläufig, selten'  (von  der  themat.  Wurzelf.  *(e)r-e-,  wie  auch:)  resvq,s  ,selten,  dünn', paresvis  , spärlich';
---- search Auflösung near er
838:Nach  Specht  KZ.  68,  42  ^  weiterhin  zur  Wz.  *er9-  , zertrennen'  als  ,den Boden  aufreißen'?
2985:Mit  u-Formans  von  der  leichten  (der-eu-)  und  schweren  Basis  {dero-u-, ^dr-u-)  ,zerreißen.  (das  Land)  umbrechen,  aufreißen,  ernten':  doro-uäi df-uä  .Getreideart',  deru-,  de-dru-  usw.  .zerrissene  Haut'.
2989:hicrliei'  anord.  trjöna  t  [*dreu-n-ön-)  , Rüssel  des  Schweins^  (,aufreißend,
3011:/dqsKavov  Name  eines  Vorgebirges  in  Kos  (wie  JgeTtavov  mehrfach  als Name  von  Vorgebirgen,  Bugge  BB.  18,  189),  öög-^ai'  xovldsg,  öeq-kvIIelv olaoTTOtBLv  (eigentlich  ,die  Haut  aufreißen*  Avie  gleichbed.  ösqiivXXblv)  Hes.-
3589:aisl.  draf,  engl,  draff  ,Berme,  Hefe',  mnd.  draf,  ahd.  trebir  PI.  ,Treber', anord.  drafli  m.  , frischer  Käse',  drafna  ,sich  auflösen',  norw.  drevja  ,weiche Masse';  geminiert  nl.  drabbe  ^Berme,  Bodensatz',  ndd.  drabbe  ,Schlamm'; schwed.  dröv  n.  ,Bodensatz'  {*dhräbho-),  ags.  dröf,  ahd.  truobi  ,trübe', got.  dröbjan,  ahd.  truoben  ,trüben,  verwirren',  ags.  drefan  ,auf rühren, trüben'  (dasselbe  Bed.-Verh.  wie  zwischen  gr.  ragdaacj  und  anord.  dreggiar).
3906:Got.  gadrahan  ,aushauen,  karo^sly^j  anord.  draf  n.,  ags.  droef  n.  , Ab- fall', anord.  drafna  ,sich  in  kleine  Teile  auflösen',  blöp-drefjar  m.  ,Blut- flecken';
4967:lit.  yrii,  zrti  ,sich  auflösen,  trennen,  pairas  ,locker';  rZtis  m.  ,BastsieV (mit  unursprünglichem  Schleifton,  wie  oft  in  i-Stämmen),  lett.  reta,  rete .Narbe',  rem  rudzi  ,undicht  stehender  Roggen';  lit.  eftas  ,weit,  geräumig' (,*auseinanderstehend');  von  der  leichten  Basis  retas  ,dünn,  weitläufig, selten'  (von  der  themat.  Wurzelf.  *(e)r-e-,  wie  auch:)  resvq,s  ,selten,  dünn', paresvis  , spärlich';
4968:aksl.  oriti  ,auflösen,  stürzen,  zerstören'  (Kaus.  '"^oreiö  ,mache  auseinander- gehen'), skr.  ohhriti  ,niederwerfen',  dech.  ohofiti  .zerstören',  russ.  razorüh  ds.
5051:2.  ereu'  , aufreißend
5054:s.  auch  unter  2.  reu-  ,aufreißen^,  das  wohl  dazugehört. WP.  II  352,  Holthausen  Altwestn.  Wb.  355.
```


## [2026-09-05T20:30:26.303Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4955,4975p' POK_01.txt\necho \"=== which awk page is line 4966? ===\"\nawk 'NR<=4966{n+=gsub(/\\f/,\"\")} END{print n}' POK_01.txt",
 "description": "Print Pokorny era- entry with rarus"
}
```


### [2026-09-05T20:30:27.929Z] TOOL RESULT

```
Gr.  I'^ä  ,Erde',  e^a-^s  ,zur  Erde'  (vielleicht  davon  iqacjy  s.  unten  S.  336; mit  Zusarümendehnung  wohl  noXvrjQog'  ftoXvaQovQog,  nXovdLog  Hes.);  evegoi, s.  oben  S.  312;  ioeai-[,L€rQ7]'  yewi^sTQiav  Hes.;
germ.  *erpö  in  got.  airpa,  anord.  ^'ortf,  ahd.  (usw.)  erda  ,Erde';
germ.  *e?*ö  in  ahd.  ero  ,Erde';
uo-Erw.  in  anord.  ^'^rvi  (*erioan-)  ,Sand,  Sandbank',  und
cymr.  erw  f.  ,Feld',  PL  erwi,  erwydd,  corn.  erw,  ereu  ds.,  abret.  mbret. eruj  nbret.  ero  ,Furche'  (*erwi-);
vielleicht  arm.  erJcir  ,Erde'  (Pedersen  KZ.  38,  197),  wenn  für  *erg-  (idg. *e7'w-)  nach  erkin  ,Himmel'.
WP.  I  142,  Finzenhagen  Terminol.  6,  Schwyzer  Gr.  Gr.  I  424.
5.  er-,  ers-,  thematisch  (e)r-e-    ,locker,    undicht,    abstehend;    auseinander-
gehen, auftrennen'. Ai.  r^e  mit  Abi.,  Akk.  ,rait  Ausschluß  von,  ohne,  außer'  (Lok.  eines  Partiz. *rta-  ,abgetrennt,  abgesondert'),  nirrti-h  ,AufIösung,  Verwesung,  Verderben'; dr-ma-  PI.  ,Trümmer,  Ruinen',  armakd-  ,trümmerhaft'  oder  n.  ,Trümmer- stätte'  (Bedeutung  etwas  unsicher);  *^rd-  in  Irma-  ,Wunde';  themat.  *(e)r-e- in  virala-  ,auseinanderstehend,  undicht,  selten';
333
gr.  SQfiiiog,  att.  eorjixog  ;,einsam^;
ganz  unsicher  lat.  rärns  .locker,  nicht  dicht,  selten^  {*er9-rö-s),  eher glaublich  rete  ,Netz,  Garn'  (vgl.  unten  lit.  rMs,  lett.  reta);
lit.  yrii,  zrti  ,sich  auflösen,  trennen,  pairas  ,locker';  rZtis  m.  ,BastsieV (mit  unursprünglichem  Schleifton,  wie  oft  in  i-Stämmen),  lett.  reta,  rete .Narbe',  rem  rudzi  ,undicht  stehender  Roggen';  lit.  eftas  ,weit,  geräumig' (,*auseinanderstehend');  von  der  leichten  Basis  retas  ,dünn,  weitläufig, selten'  (von  der  themat.  Wurzelf.  *(e)r-e-,  wie  auch:)  resvq,s  ,selten,  dünn', paresvis  , spärlich';
aksl.  oriti  ,auflösen,  stürzen,  zerstören'  (Kaus.  '"^oreiö  ,mache  auseinander- gehen'), skr.  ohhriti  ,niederwerfen',  dech.  ohofiti  .zerstören',  russ.  razorüh  ds.
er-db- :
ai.  fdhak  ,besonders,  abgesondert',  ärdha-h  ,Teil,  Seite,  Hälfte',  ardhd- ,halb',  n.  ,Teil,  Hälfte';
lit.  ardaü,  -yti  ,trennen,  spalten'  (Kaus.,  wie  ksl.  oriti)-^  erdvas  ,weit,  ge- räumig', lett.  ärdaws,  irdens  ,locker,  mürbe',  trds  ,locker,  bequem  (ge- räumig'), irditj  ifdindt  ,lockern,  trennen',  grzw,  grc?w,  ^rst  ,trennen'.
re-dh- :
aksl.  red^k^  ,selten'  (wohl  stoßtonig,  vgl.  cech.  Hdhy,  sloven.  reddkj trotz  serb.-kroat.  njedki,  ridki);
über  ered-  s.  oben  S.  329  f.,  über  ereu-  unter  besonderem  Artikel  unten S.  337.
Inwieweit  die  von  Persson  Beitr.  666,  773,  839  f.  als  Erweiterungen unseres  *er(9)-  betrachteten  Wurzeln  re-d-  ,scharren',  rei-,  reu-  ,auf reißen' ihr  wirklich  entstammen,  ist  fraglich;  die  bei  *er(a)-  besonders  ausgeprägte Bedeutung  des  lockern,  undichten,  auseinanderstehenden  lassen  sie  ganz vermissen  oder  wenigstens  nicht  als  herrschende  Bedeutung  erkennen.
=== which awk page is line 4966? ===
345
```


## [2026-09-05T20:30:47.700Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD era- ===\"; grep -n \"er[əa]-\\|rarus\\|retina\" AHD_watkins1985.txt | head -20\necho; echo \"=== AHD ergh/orgh ===\"; grep -n \"ergh\\|orgh\\|orchestra\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD Watkins"
}
```


### [2026-09-05T20:30:47.767Z] TOOL RESULT

```
<persisted-output>
Output too large (67KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/brknpkh5r.txt

Preview (first 2KB):
=== AHD era- ===
117:General Terms. It is appropriate to begin with a sampling of basic terms in the lexicon, which have no special cultural value but attest to the richness of the tradition. All are widespread in the family. There are two verbs expressing existence, es- and bheue-, found in English Is, Latin esse, and English BE, Latin fu-turus (FUTURE), respectively. There are verbs “to sit” (sed-'), “to lie” (legh-, kei-'), “to stand” (sta-). There are a number of verbs of motion, like g’a-, “to come,” ei-', “to go,” tera-?, “to cross over,” sek’-', “to follow,“ kei-3, “to set in motion,” and the variants of rolling or turning motion in wel-3, wer-%, k”el-'.
123:A number of qualitative adjectives are at- tested that go back to the protolanguage. Some come in semantic pairs: sen-', “old,” and newo-, “new”; also sen-', “old,” and yeu-, “youthful vigor”; *tenu-, “thin” (under ten-), and tegu-, “thick”; g”era-?, “heavy,” and leg"h-, “light.” There are also the two prefixes su-, “good, well-,” and dus-, “bad, ill-,” in the Greek forms borrowed as EU- and pDys-. But normally adjectives of value judg- ments like good and bad are not widespread in the family and are subject to replacement; English good, Latin bonus, and Greek aga- thos have nothing to do with each other, and each is confined to its own branch of the family.
181:seng’h-, “to prophesy, sing, make incanta- tions,” now secularized in sInG. Another is g“era-*, “to praise aloud,” which in Latin gratia (GRACE) has had a considerable for- tune in Christianity.
...
</persisted-output>
```


## [2026-09-05T20:30:49.508Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT ərəγant ===\"; grep -n \"r.gant\\|arəδa\\|ardδa\" BRT.txt | head -20\necho; echo \"=== BRT col 193 area ===\"; grep -n \"^193\\|  193  \" BRT.txt | head",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T20:30:49.587Z] TOOL RESULT

```
=== BRT ərəγant ===

=== BRT col 193 area ===
5446:193
9130:KompA.;  AUntl.  {s.  k.i.-ya-,  ij:-r\  —  Vgl. tiavay-  EN.  —  ai.  Air-.if-  m.  (IIB.  S.  227).  — P6.!  (kdk,  voM.)  tiiyii-,  s.  iinttt  <.ic-f/.iK- mit No.  —  ">  iKI.  s.  C1.0.  KZ.  fj.  300  und  No.  2, 3,  S-  -  ^)  S  i'"''-  3  ai  vgl.  No.  5.  --  3)  IF. /.  191,  193  No. ;  S  ^<>S.  I  b,  MeILLeT  bei Bgm.  Grdr.'  /.  1091.  —  t)  Doch  s.  auch  Komp. \Ln:i').  —  i>  Stven.  nnter  dem  EN.  —  <•)  -f statt  -va,  S  3Ö1V.  31,  Abi;esehcn  von  11  ftjr -0,  formell  gleieli  /'Jrvyi/j-Äi.
```


## [2026-09-05T20:30:55.794Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5430,5470p' BRT.txt",
 "description": "Print BRT around col 193"
}
```


### [2026-09-05T20:30:55.846Z] TOOL RESULT

```
ya^va^uP^    xsäydiiyä'"^  pu^'i^    A0.1.2;
—     ^a^aiiy     "^ä'^J^)     xsilya'^iya"    Am.;,
3-  3)    Artaxerxes    III,    Sohns    Arta-
xerxes  II:  '^t^atiy  '>ra^  xs.Jy.i^iyO^  Ao.
/.  2,  3,  4;  —  ardaxca^c^O  . .  ^vazarkc^
Ao.  2;    —    t^uri^mazdJ   ,  ,    hyt^    tnjtn
"iä^jS'  xsäyaiiyi^i''  akunau/  Ao.  I.i.
Eig.  "der  dem  heiligen  Rechte  die  llemcbaft
gibt'.  —  ")  So,  mit  %•;  nach  EvETTs  Abschrift
auch   beide  Male  in  Am.  4,  gegen  NA.,    die
•%>-a/iyä  bietet.  — ")  Sollte  GS.  sein.  —  3)  Statt
NS.  —  4)  In  der  Schreibung  gani  verunglückt.
Nach   GGA.  rSS2.  494    steht    auf   der   Vase
'sda*,  nicht  s/a^.  —  i)  Statt  AS.
•  j.  *ar«tay- '''  t  sva.  asay- :  niiri,-a  alaond
dby  Google
193
artavardiya-
x/ruiiiim&i  °r?ittmca''>  ..  *paitlsantayasca<
^•39-
Zum  V.  'ar-.  —  VgL  aUy  und  S  ^Sg.  4  C mit  No.  —  Pü.:  larsäiäsJh.  ~~  0  Hds.  ä  rii-' lim;  5.  aber  Pii,  und  iSt.  Y.  60.  3,  wo  oioö- w^  xsnülasla  asayasra  . ,  paili.uiiilayasfa.
•  p.  arta'vardiya-  m.  ER  eines  Heer- führers Darius  /.;  "rfiya*  nämi^  pärsJ^ tnünä  ba'dakt^  Bh._j.6;  6;  — patii  "diyam Bh.j.6,  7.
Eig.  'das  heilige  Recht  mehrend',  Ableit.  (ohne Änderung  der  Bed.)  aus  *arta-varda-  Adj.;  s. dazu  Wh.  Gr.»  S  1212  c.')  —  ■>  S.  auch  Foy ZDMG.  S4-  358.  l^Z.  j/.  518.
•  j.  aratö.kar^^na-  AdJ,  'wofür  die  Er- füllung der  religiösen  Pflicht  bezeichnend ist',  von  Hamaspa^maedaya  (sd.)":  ha- maspahmaSdaim  "tum  Vr.  2.  z; —  kama- spdimaldayeAe  'nahe  Vr.  1.2;  —  *'%nö F.7'>.
"jfnrjian-  n,  •perfectio',  zum  V.  '^iar-.  —  Pü. (lu  F.);  yaiiin  iarlär,  (sonst):  /a  yaiUn  kar- tärik.  —  ■)  Weil  in  diesen  Tagen  das  beson- ders gefeierte  Fest  der  Fravaiay%  stattfand; S.    unter    kamaspfiimaedaya:    —  '')    Geschr.
•  g-  (t  j)  arad-  V.  'gedeihen  lassen'. Praes.  i   arid-  :  »rjd-.
'gedeihen  lassen,  fördern':  däiä  ar?h3us andat  (Ko.)  vohü  manaahä  Aathyilvar/- tqm  (sd.)  Y.  50. 1 1 ;  —  >r»dat.'.
u.  ardhma,  j-dhyam\  fdhäniah.  —  Pü.:  bcaian- dai  dahänik  (für  arf+da/i).
•  j.  arsSa-,  p.  arda-  i)  Adj.  'halb' (nur  Komp.).  2)  m.  'Seite':  *atitar?m (sd.)  'tijm  mayaAe  V.p.29;  —  antar?m 'fam  nmanaheV.6.i,y,  — dasinim  (vair- yastärtm)  hl  upa  "htm  Yt.  10. 100';  — visps  he  upa  'wun  (lies  -o!)  \tio.ioo; —  äasimm  hl  'Öe..  Aävöya  hl  "%€  "rechts (links)  ihm  zur  Seite", Yt. /o.  ia6;  —  ww- %asö  (sd.)  gairis  parmtarim  °c,5  (AD.) manuiahe  YL/p.i.  [V.  5.19,  5.33,  Yl j".6o:  lies  antar».am>m^
KonipA.,E.  —  «i.aj-aMfl- Adj. 'halb',  m. 'Hälfte', ördha-  m.  'Sei(e';  oss.  ärdäg  'halb,  Hälfte'.  — Vgl.  arilah:  —  Pö. :  kanär  (dat  n  a,  vgl.  dal  r ; bei  Salemann  Porsenhdschr.  öS  II  Z.  5,  6).
•  p.  arda-stina-  m.  'Halbstand">j  bau- licher Kunstausdruck  "',vlL'Fensterkrönung' oder-  '-sims':  "«a*  a'it^gaini^  därayO^- vahaul  vt^iyä  karta''  Q.^.
>)  Falsch  FrMüiler  WZKM.  3. 149,  Fov  KZ. ^j.48  (vgL  or.'fa;*-,  trizräspa-),  JusTlGlrl'h.  2. 4SI  No-  Choch'  wäre  *ariiin/a-).  —  s)  Eü. umschreibt  blot.
p.  ardiixiastix'   Ao.  3:    s.   arlaxsa%''a-   mit No.  4.
•  j.  ara^ah-  n.  'Seite';  dasina  paiti  'lanha N.ÖJ.
Vgl.  ari^a-.  —  Pü. :  hal  kusl  i  ddsin.
•  j.  araduma-  Adj, (?)—?— :  srinm  •m»m
Pü.:  fehlt
•  p.  ardu'manis-  m.  ES.  eines  Persers, Genossen  des  Darius  bei  der  Magophonie: 'nis  (NS.)  nJmo"  *vahaukahy3  pu'^'t/' pärsJ"  Bh.4- 18.
Eg.  'geradsinnig',  vgL  unter  iriiav:  —  Vgl, lEt.  Bthl.  IF.  g.  266;  daiu  noch  JuSTl  NB. a34b.  S3Sb-    (Anders  Justi  NB.  ii.)
•  j.  arvduä-  n.  'Verletzung,  Hieb',  im Strafgesetzbuch  vorsätzliche  Körperver- letzung mittelst  einer  Waffe  ohne  sicht- bare Folge,  nur  mit  Schmerzgefühl  ver- bunden*': yat  dim  (nämL  narfm)  amü.- manaigha  paiti.amaoiti  aitat  Äf'du/"weTiTi er  ihn  mit  der  Absicht  der  Misshaadlung trifft,  so  begeht  er  damit  ein  .^."  ¥.4.17;
—  yü  .  .  *ainim  dahmtm  jasnti  'dus  va airyö.staor»m    vd  ..   ^anm  (sd.)   N.  4j;
```


## [2026-09-05T20:30:56.733Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^er[əa9]-\\|^era-1\\|era-!\\|To be sparse\\|sparse\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD for sparse"
}
```


### [2026-09-05T20:30:56.783Z] TOOL RESULT

```
453:era-'. To row. 1. Variant form *ré- (< *rea-) in: a. Ger- manic *ré- in Old English réwan, to row: ROW?; b. suf- fixed form *ré-thra- in Germanic *réthra, rudder, in Old English réther, steering oar: RUDDER; Cc. suffixed form *ré-smo- in Latin rémus, oar: BIREME, REMEX, TRIREME. 2. Oldest variant form *sres- becoming *eré- in Greek triérés, trireme: TRIERARCH. [Pok. 1. er9- 338.]
749:men-2. To project. 1. Suffixed zero-grade form *mn-to- in a western Indo-European word for a projecting body part, variously “chin, jaw, mouth,” in Germanic *mun- thaz in Old English mith mouth: mouTu. 2. Latin mi- nae, projecting points, threats (> mindri, to threaten): MENACE, MINACIOUS; AMENABLE, DEMEAN!, PROME- NADE. 3. Latin -minére, to project, jut, threaten: EMI- NENT, IMMINENT, PROMINENT. 4. Suffixed o-grade form *mon-ti- in Latin méns (stem mont-), mountain: MONS, (MONTAGNARD), MONTANE, MONTE, MONTICULE, MOUNT!, MOUNT?, MOUNTAIN; AMOUNT, ULTRAMONTANE. [Pok. 1. men- 726, 2. menth- 732.] men-3, To remain. Variant suffixed (stative) form *man-é- in Latin manére, to remain: MANOR, MANSE, MANSION, (MENAGE); IMMANENT, PERMANENT, REMAIN. [Pok. 5. men- 729.] men-‘. Small, isolated. 1. Greek manos, rare, sparse: MANOMETER. 2. Suffixed o-grade form *mon-wo- in Greek monos, alone, only, single, sole: MONAD, MONAS- TERY, MONK, MONO-; PSEUDOMONAD. 3. Possibly also suffixed form *men-i-, a small fish, in Old English myne, mynwe, minnow, perhaps the source of Middle English meneu, a small fish: MINNOW. [Pok. 4. men- 728, meni- 731.] mend-. Physical defect, fault. 1. Latin mendum, menda, defect, fault: MENDICANT; AMEND, EMEND, (MEND). 2. Latin mendax, lying, liar: MENDACIOUS. [Pok. mend(a) 729.) mendh-'. To learn. Zero-grade form *mndh- in Greek manthanein (aorist stem math-), to learn: MATHEMAT- ICAL, (MATHEMATICS); CHRESTOMATHY, POLYMATH. [Pok. mendh- 730.] mendh-?. To chew. 1. Latin mandere, to chew: MANDI- BLE, (MANGE), MANGER. 2. Zero-grade form *mndh- in: a. Greek masasthai (< *math-ya-), to chew: MASSETER; b. Greek mastax, mouth, the model for expressive Greek (Doric) mustax, upper lip, mustache: (MOSTACCIOLI), MUSTACHE; Cc. Greek mastikhan, to grind the teeth: MASTICATE. [Pok. 2. menth- 732.] menegh-. Copious. Germanic *managa- in Old English manig, menig, many: MANY. [Pok. men(e)gh- 730.] meng-. To furbish. 1. Latin mango, furbisher, gem pol- isher, swindler: MONGER. 2. Greek manganon, magic
2354:TENTH dekm TENUOUS ten- TENURE ten- TENUTO ten- TEPID tep- TERATOCARCINOMA kWer-1 TERATOGEN kWer-1 TERATOID kWer-1 TERATOMA kWer-1 TERCEL trei- TERCET trei- TEREDO tera-! TERETE tere-1 TERGIVERSATE wer-3 TERM ter- TERMINATE ter- TERMINUS _ter- TERN? trei- TERPOLYMER trei- TERPSICHORE gher-!, terp-
2361:TERRESTRIAL ters- THRESH tera-! TORTICOLLIS kWel-1, terkw- TRICERATOPS ker-1 TERRE-VERTE ters-, virére THRESHOLD tere-1 TORTUOUS terkw- TRICHINA  thrix TERRIBLE tres- THRICE trei- Tory ret- TRICHO-  thrix TERRICOLOUS ters- THRILL tere-2 TOTAL teuta- TRICHOME _ thrix TERRIER ters- THRONE dher-2 TOUGH denk- TRICHOTOMY _ trei- TERRIFIC tres- THROSTLE trozdo- TOUPEE tap- -TRICHOUS _ thrix TERRIGENOUS §ters- THROUGH tere-2 Tow! deuk- TRICHURIASIS ors- TERRITORY ters- THROW tere-1 Tow? taw- TRICLINIUM klei-, trei- TERROR tres- THRUM?2 ter- TOWN dhino- TRICORN ker-1 TERTIAN trei- THRUSH! trozdo- TOXIC tekw- TRICROTIC  kret-2, trei-
```


## [2026-09-05T20:31:03.445Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '450,460p' AHD_watkins1985.txt",
 "description": "Print AHD lines 450-460"
}
```


### [2026-09-05T20:31:03.515Z] TOOL RESULT

```
appear, be born: ORIENT, ORIGIN, ORIGINAL; ABORT. [Pok. 3. er- 326; ergh- 339.]
er-2, Earth, ground. Extended form “*erf- in Germanic *erthé in: a. Old English eorthe, earth: EARTH; b. Middle Dutch aerde, eerde, earth (> Afrikaans aarde): AARD- VARK, AARDWOLF. [Pok. 4. er- 332.]
er-3. Base of designations of various domestic horned animals. Extended form *eri- in Latin ariés, ram: ARIES. [Pok. 2. er- 326.]
era-'. To row. 1. Variant form *ré- (< *rea-) in: a. Ger- manic *ré- in Old English réwan, to row: ROW?; b. suf- fixed form *ré-thra- in Germanic *réthra, rudder, in Old English réther, steering oar: RUDDER; Cc. suffixed form *ré-smo- in Latin rémus, oar: BIREME, REMEX, TRIREME. 2. Oldest variant form *sres- becoming *eré- in Greek triérés, trireme: TRIERARCH. [Pok. 1. er9- 338.]
ere-2. To separate. Variant *ré-, contracted from *reo-. 1. Suffixed variant form *rd-ro- in Latin rdrus, “having intervals between,” “full of empty spaces,” rare: RARE}, 2. Suffixed zero-grade form *ra-ti- in Latin ratis, raft (< “grating,” “latticework”): RATITE. 3. Suffixed length- ened-grade form *ré-ti- in Latin réte, r��tis, a net: RE- SEAU, RETE, RETIARY, RETICLE, RETICULE, RETINA; RETIFORM. 4. Suffixed form *eré-mo- in Greek erémos, empty, desolate, bereft: EREMITE, HERMIT; EREMURUS. [Pok. 5. er- 332.]
ered-. High. Suffixed zero-grade form red-wo- in Latin arduus, high, steep: ARDUOUS. [Pok. er(e)d- 339.]
ergh-. To mount. 1. Suffixed o-grade form *orgh-i- in Greek orkhus, testicle: ORCHID. 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]
erkv-. To radiate, beam, praise. Sanskrit re, rk, “bright- ness,” praise, poem: Ric-VEDA. [Pok. erke- 340.]
ers-'. To be in motion. 1. Variant form *rés- in Germanic *rés- in Old Norse rds, rushing: RACE?. 2. Form ers-d- in Latin errdre, to wander: ERR, ERRATIC, ERRATUM, ERRO- NEOUS, ERROR; ABERRATION. [Pok. 2. ere-s- 336.]
ers-2. To be wet. Variant form *ros- in Latin rés, dew: ROSEMARY. [Pok. 2. ere-s- 336.]
es-. To be. 1. Athematic first person singular form *es-mi in Germanic *izm/(i) in Old English eam, eom, am: AM. 2. Athematic third person singular form *es-ti in: a. Ger- manic *is#(i) in Old English is, is: 1s; b. Sanskrit asti, is: SWASTIKA. 3. Optative stem *si- in Germanic *sijai- in Old English sie, may it be (so) in gése (géa, yea; see i- + sie), yes: YES. 4. Participial form *sont-, being, existing, hence real, true, in: a. Germanic *santhaz in Old English s6th, true: SOOTH, SOOTHE; b. suffixed (collective) zero-grade form *snt-yd, “that which is,” in Germanic *sun(dj6, sin (< “it is true,” “the sin is real”), in Old English synn, sin: SIN}; c. Sanskrit sat-, sant-, existing, true, virtuous: SUTTEE; BODHISATTVA, SATYAGRAHA. 5. Basic form *es- in Latin esse, to be: ENTITY, ESSENCE; ABSENT, (IMPROVE), INTEREST, PRESENT!, (PRESENT?), PROUD, (QUINTESSENCE), (REPRESENT). 6. Basic form *es- in Greek einai (present participle ont-, being), to be (in pareinai, to be present): -ONT, ONTO-; (BIONT), HOMOIOUSIAN, PAROUSIA, (SCHIZONT). See extension esu-. [Pok. es- 340.]
```


## [2026-09-05T20:31:20.709Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '448,450p' AHD_watkins1985.txt",
 "description": "Print AHD er-1"
}
```


### [2026-09-05T20:31:20.751Z] TOOL RESULT

```
ARE!, ART?. 2, Perhaps in Germanic suffixed form “er- n-os-ti- in Old English eornoste, zealous, serious: EAR- NEsT!. 3. Suffixed form *or-yo- in Latin oriri, to arise,
eu-!
appear, be born: ORIENT, ORIGIN, ORIGINAL; ABORT. [Pok. 3. er- 326; ergh- 339.]
```


## [2026-09-05T20:31:22.217Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt; do echo \"== $f\"; grep -n \"ارغنده\\|آرغنده\\|آرغده\" $f | head -10; done",
 "description": "Grep Borhan for arghandeh"
}
```


### [2026-09-05T20:31:23.918Z] TOOL RESULT

```
== BQT_v1_pages.txt
8630:« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه . رك : آلگونه .
10874:است ؛ و بعضی گویند ارغنده آب است وارغنده
== BQT_v1.txt
15391:« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه . رك : آلگونه . 
20368:است ؛ و بعضی گویند ارغنده آب است وارغنده 
20397:۴ در اوستا 6۲681120 درقارسی ارغند وارغنده وارغده 
20400:وآرغده بمعنی خشمگین . در اوسئا ارغشت صفت برای مگس ودوزخ آمده » ومیتوان آنرا بمعنی 
20401:زشت وتیره و مکروه داتست ۰ بنابراین ارغند و ارغنده را که دد فرهنگهای فارسی بمعنی دلیر 
20404:رشجاع گرفته‌اند , درست لست « فاب۱: ۸ ». رك : آرغده . 
20528:۵ رك: ارغنون. ۷ -رك : ارغنده. ‏ ۲ - ۲ ۸ «لفت نامد»؛ کن۱06۲۲ 1۸۷5۵۵1۵ 
== BQT_alt_v1.txt
11864:آرغده ؟- بضم ثالث ( ۲ ) بر وزن 
14008:« آرغده » . رك : آرغده. 1 -لفتی درآ لگوبه ره : آلگونه . 
18427:است ؛ و بعضی کویند ارغنده آب است وارغنده 
18451:۱ رك : ارغنون . ۴ - در اوستا 6۲6213806 درفارسی ارنند وارغنده وارغده 
18454:وآرغده بمعتی خشمگین . در اوسئا ارغشت سقت برای مگس ودوزخ آعده 0 ومیتوان آرا بمعتی 
18455:زفت وتبره و مکروه دانست » بنابراین ارغند و ارغنده را که در فرهنگهای فارسی یمعنی دلیر 
18458:وشجاع گرفته‌اند , درست نیست « فاب۱: ٩-۱۹۸‏ . رك : آرغده .
```


## [2026-09-05T20:31:31.765Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20360,20410p' BQT_v1.txt",
 "description": "Print BQT context for arghandeh"
}
```


### [2026-09-05T20:31:31.814Z] TOOL RESULT

```
او خن " - بر وزن فرزند » بمعنی 
خسم افنکن و دلیر و شجاع باشد - و خشمکن 
را نیز گویند . 

ار غنداب نام رودخانه ات که 
مابین عراق و آذربایجان کذرد - و تام رورخانة 
قندهار هم هست؛ و معنی ترکیبی آن خشمگین 
آب بافد : چه ارفتد بمعنی خشمگین عم آمده 
است ؛ و بعضی گویند ارغنده آب است وارغنده 
نیز بحعنی خشمگین باشد وها بکثرت استعمال 
افاده است . 

ارغنفه ۲ » بر وزن‌شرمنده » بمعنی 
حرص و خداوند شره.باشد - و مسثی را نیز 
گوبند که طالب و حرص‌شراب‌باشد - وبمعنی 
قهر آلود و غنبناك هم آمده است . 

ار نگ - بر وزن وممنی ارژنگ‌است 
که نکارخانةٌ مانی نقاش باشد . 

ادغنی ؟ « بنتح اول و سکون ثانی 
واكك مفتوح و رابع مضموم بنون زده , عخفف 
ارغنون است . و آن سازی باشد که رومیان 
نوازند و افلاطون واضم ( ۳ 

ارغنون ۴ بی وژن آندرون » سازیست 





(۷) خم ۳ : عشفه ؛ چش : عشق بی جان . 





۴ در اوستا 6۲681120 درقارسی ارغند وارغنده وارغده 


وآرغده بمعنی خشمگین . در اوسئا ارغشت صفت برای مگس ودوزخ آمده » ومیتوان آنرا بمعنی 
زشت وتیره و مکروه داتست ۰ بنابراین ارغند و ارغنده را که دد فرهنگهای فارسی بمعنی دلیر 


رشجاع گرفته‌اند , درست لست « فاب۱: ۸ ». رك : آرغده . 


۴ - از بوانی ۳92900 . 


۴ رك : ارغنون.
```


## [2026-09-05T20:31:37.957Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"آرغده\" BQT_v1_pages.txt | head\necho \"---\"\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | head -3",
 "description": "Locate arghade page in BQT v1"
}
```


### [2026-09-05T20:31:38.023Z] TOOL RESULT

```
8630:« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه . رك : آلگونه .
---
```


## [2026-09-05T20:31:42.518Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -5 BQT_v1_pages.txt; echo \"...\"; grep -n \"page\" BQT_v1_pages.txt | head -5; echo \"--- formfeeds:\"; grep -c $'\\f' BQT_v1_pages.txt\necho \"--- page index of line 8630:\"; awk 'NR<=8630{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt\necho \"--- page index of line 20360 in BQT_v1.txt:\"; awk 'NR<=20360{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1.txt; grep -c $'\\f' BQT_v1.txt",
 "description": "Determine BQT page mapping"
}
```


### [2026-09-05T20:31:43.992Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
...
--- formfeeds:
766
--- page index of line 8630:
267
--- page index of line 20360 in BQT_v1.txt:
0
0
```


## [2026-09-05T20:31:54.727Z] TOOL CALL #24: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:32 2>&1 | head -60",
 "description": "Fetch BQT page 32"
}
```


### [2026-09-05T20:31:56.580Z] TOOL RESULT

```
no scan of BQT covers printed page 32 (see 'scans' in refs_online.json)
```


## [2026-09-05T20:32:01.274Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"رغده\\|رغند\" BQT_v1_pages.txt | head -20",
 "description": "Grep BQT v1 pages for arghade variants"
}
```


### [2026-09-05T20:32:01.325Z] TOOL RESULT

```
8630:« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه . رك : آلگونه .
10874:است ؛ و بعضی گویند ارغنده آب است وارغنده
18731:برغندان - بر وزن د:ندان» جشن
18784:بر فندان ۴ بروزن و «متی‌برغندان
18794:در فارسی نیز : برغندان «اسقا ۱ : ۲ص۸*.‎
29528:کرد . گونند « ترغده شده است » ۰ و بروژن
```


## [2026-09-05T20:32:05.581Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==268' BQT_v1_pages.txt | head -70",
 "description": "Print BQT v1 leaf 268"
}
```


### [2026-09-05T20:32:07.414Z] TOOL RESULT

```
کت ۱ آننک
و امٌال اینها باشد 0.٩‏
۲ لر - بروزن لاغر ۰ کقل و رین را
کوند مطلقا ۴ .
۷ ۷ ۱
بمعنی آلراست ک هکفل وسرین باشد مطلناً ۴ .
] ل‌طمفا - برکون ثالت » مهرودگین |
یادشاهان را گوبنده ویضی کویند اين, لفث ترکی .
است ؟ .
۲ لفده * - باغین قطمداربروزن آزرده,
بمعنی قهرآلود وخشمگین - وجنگه آورباشد .
۲ لو زه رن اه نش فاد
است و آن‌سرخی باش که زنان برروی مالند ۰
] فتن - بافاء بروزن ومعن ی آشفتن باشت.
۲ قشته مه پروژن و معتی آخفته ۱ هت
رردیکی و کی ودروش نامراد را نیز گوء بند.
ای او سار ء بل
الطيب را کویند ودردواها بکار برند ۷ - و مصغر
آهرهت ۸
۲ لگو نه سکاف و بروزن‌وععتی
آلفونه است که غازه و سرخی زنان باشد ٩۳‏ .
] ل معصفر « بکر ثالث ۳ نوعی از
ماهی درم دار ۳ 9 را نیز
نته‌اند .
آ مج - بن تلد وسکون نون وجیم»
آلوچه را کویند و آن میومایست ممروف ‏
آ لگ « بروزن آهنکه . کوی بلشد
که در اطراف قلمه‌حا بجهث محاصره و کرفتن
آ نکنند ومورچال همان است- و بسنی دبولربرا
کوبند که بجهت محافظت خود و حواله کماز
پرای قلمه سازند - وجنمی ازمردم را نیز گویند
که مردم. بیرون قلمه جابجا بواسطهٌ کرفتن قلمه
عصسدی: لشت‌نامه ».
۴ التمفا . اللون نمفا » هر پادشاهان ترث که با م رکب سرخ برفرمانها فش میکردد ۰
اين فرامن را منصوصاً « بارليغ التون تمغا * مینامیدند . «جنتابی ۳۱ *. ه‌ لغتی دد
« آرغدء » . رك : آرغده. ۲ -.لفتی درآ لگونه . رك : آلگونه .
۰ ۷ - از تبانات پست سبز است که دد ته اهر با روی آب شیرین با شور دیده میشود .
با گ نه رشه دارد نه ساقه نه ب رگهه . ته اش دارای « کلور فبل » است و شکهای مختلف دنده
ميشود. طول آن ممکن است مندها متر برسد. ركك : فرهشگه روستابی 4۸ - ۹٩‏ ؛ ورگ : آله.
4,۸ : آل. ٩‏ مرکب از: آل (سرج) + کونه (رنگه ).
۰- آن بناکوی کز ساکویی ‏ " بر کشيده است آلگونه بسيم
1 شهید بلخی . « لغت نامه *.
» آئبالو 6مع۳1ه وناصطظ درخئی است از وتا بادامی ها از تیرژ کل
مرخبان . « کل گلاب ۲۲۳۷>. 4 آلتمغا - را: آل طمفا. » آلنوی - ترکی
بمعنی طلا « کاشنری ] : ۱۰۵ > :
ظای و مثدیل وگل ازآلتون بگیر ۷ بگرمابه دوم ای «ا کززیر
« مثنوی ۳ ص 0۵۱۱ > < نداب ۳ : ۵ ٩‏ س۵ ٩‏
```


## [2026-09-05T20:32:23.448Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'آرزو' in p or 'آرغ' in p or 'آرام' in p:\n        print(i, p[:100].replace('\\n',' | '))\nEOF",
 "description": "Find leaves with A-r section in BQT"
}
```


### [2026-09-05T20:32:25.281Z] TOOL RESULT

```
11 سه ژبا نبای‌ایرانی | نعستین بابتخت هخامنشیان بوده و بو نانیان ثرا 958۳88068( خوانده‌اند. | یس از مر گ کم
13 نج ژبانپای‌ایرانی | در فارسی : | لطف الپی بکنه کار خویش مزدءٌ رحمت برساند سروش » | چز همان نفوذ دینی #خیگر
19 یازده زبانبای‌ایرانی | شدن ]نها در آینده بنیاد بسیاری ازلفتبای فارسی استوازتر گردد . | اينك نامپای برخی 
20 مقك مه دوازده | در سراسرنوشته های پپلوی- چه در سنگنیشتهاوچه | هز و ارش در گزارش بیلوی اوستا (زند) و در ن
28 من» 0 -< (مال) من مبر ۲ 90۲ مر دن» تو"۷) < نو زیر 2۷7۲ < زرده | سیرن 28۲۲۷ زر (طلا) ۱ . ۱ | خط سفدی بدوش
38 مقدمه : کی | وآن منسوب به پایتخت‌است وازبیت لفات‌مردم مشرق‌لفت اهل‌نلخ‌بر آن | غالب است ... »> ۱ ۱ | فرهنگ
80 هفتاد وذو | خلف تبر بزی‌متخلص ببر هان در ۰۰۲ ۱ ۰۷ | ۵ - بپارعجم. ازلاله تيك چند بپار | دی در ۵٩‏ ۱۱ ۰ | - پی
81 هفتاد وسه | ۷- سخن نامه نظامی» ازسعید بن | نصر بن_ نمیم غز نوی. | 9۸ سر اج اللفه»؛ از سراحج الدین | علی‌خان 
107 نود و نه زبانبا و لپجه‌ها در برهان قاطع | د - شامی (لغت اهل شام): ارییان » حبق نبطی » حمحم » درافس ۰ | د
138 مقدمه صد وسی | و تثری‌تا لیف کند ده‌ها سال تتبم وتحقیق واستغراجلغات ازمتون نظم و نثر | فارسی که درمدت هز
139 جد وس و يككث کتاب حاضر | اتوء بطری »رادیو» کتری ؛ ماشین » مونوو وفیره. | ِ ۱ بر ای تکمیل کتاب‌حاضر» برخی
215 ساختن ناشد . | " .ریز - بر وزن خاه ریز . ادبخانه | و مستراح را گویند - و بمعنی دلو آب کشی | هم آمده است - 
238 آرا | آداه بروزن خارا . آرایش. وآرایش | کننده و آراینده را کویند همچو خن آرا | و بزمآرا وامی باینمعتی هم ه
239 ت برایو بی اه آرامی | رة حواشی صفحة .۳ | ۵ آرامی_نام قومی از فبایل بدوی سامی ناد سوربه که درجنوب فلسطین 
240 آرامی - پرایی ۷۲٩‏ س | آرامی بکاربردند. بدبنوجه زبان آرام یکه اززبانهای سامی‌است وآموختنش برای‌هزدم مأ
242 ]دی ح بکر الث و رايع و سکون | تحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی | است ۰ چه آرش بمعنی «معنی» است
244 در دل کسی‌جای کند ؛ وباین معلی بازای نفطه‌دار | هم آمده است . | 11 ۱ مه بسکون زای نقطه داره یمعنی | آرزو و
255 ی آشنا کر | خابة سک آنی است ۷ . خالهرا نیز گویند چنانکه گوبند «اين عمارت سه | آ ش لقن * کنابهازآنت کهکیر
267 کت ۱ آننک | و امٌال اینها باشد 0.٩‏ | ۲ لر - بروزن لاغر ۰ کقل و رین را | کوند مطلقا ۴ . | ۷ ۷ ۱ | بمعنی آلراست
280 ودال ابجد ,کی را گویند که دروغ وید 6 | هودم را فریپ دهد ۷ . | آ هی ؟ س بفتح اك و سکون نون » | ممروفست.- وش
286 آ لین جمشید - یکس نون . فلحن | دیم است از سی‌لحن باربد - و نام نوایی هم‌هست | از موسیقی . | وروش‌زا یز گوی
287 و امد تجرید نوفتر | آای‌افت را با واو جمداز اف که « اوپاشه » باشد ابحد تحرید () نوشتن - | بومن حعنی نز ک
288 ابحل ی | )بحل « بنتح اول و ضم حای بی نفطه و«شتکار» نیز گفته‌اند » لقری را نافع است . | و سکون ثانی و لام
293 پوت | ابنکاد ‏ بر وت شب کون گفق | وزراعت را گونند . | ال - بنتح اول و ضم انی وسکون لام. | دوابی است که بشیرا
300 ست و 4 سب | #احر یض « بکر اول و دای بی نقطه | و سکون ثانی وتحتانی و صاد تقطه دار ء دآروبی | است که کلف را 
318 ارغامونی | ار غامو نی پامیم بر وزن افلاطونی؛ | بلغت بونانی تباتی است | صحرایی و برنگ | تردنك(۱) شقایق‌صمان | ب
320 ار که | واستر بشندند ودرعلف زارها (۱) سردهند تابچرد؛ | و باین معنی نم اول و انی مشهور است | ار کال -بکر او
322 ارمند | زلایتی‌است از کوهستان آنربابجان و مولدشیرین | مشهور آبجا بوده و ابریشم ارمنی منسوب بدانجا | است - 
323 از یا | وجیم. , بمعنی آرنج است ت که بندگاه ساعد | وبازو باشد وبحربی مرفق خوانند . | ار ندان بر وزن‌قلمدان 
388 اندر خور | ا ندز خو در - بنمخای نفطه‌داروسکون | واو ممدو له و رای می‌نقعله 4 ممحنی اج وسزاوار | وزیبا باشد
413 ۱۳ات ایدغ | ایاره گیر ۱ -بر وزن کنار هگیر ». | محاسب و نوبسنده را گویند . | ایاد ۴ ه بر وزن نماز , دام غلا
416 و چون کل آن زرد و سفیدو کبود میباشدبنایر | آن ایرسا نامیده‌اند چه شبیه بقوی‌فزح است . | بیوایی ٩‏ طلق و 
425 ی ۷۰ ‌- | پاخر و بنتحالت وسکون رای‌بی‌هطه | و زای نقطه‌دار , نام فصبهابست در خراسان ونم | کوشه‌نی باشد از 
454 وتیردانی را کوبندک» پر از نبر باشد » ومعنی | تر کیبی آن‌بت ماننداست چه‌بت لِف‌جولامگان | و کیش ماننه را 
458 سه؛: روزة خوارزم که ای آنجا جمع حود و کنابه از دمت صاحب همتان هم هست . | پحردمان مق عمل - یب از | بحری
464 بلیست - بکسر اول و ثالی و سکون | سین بی نقطه و فوقانی» وجب را گوبند و بسربی‌شبر | خوانند ۱ .و فتح اول و 
465 مودن باشث . | بد ندان‌خوش هدن « کنابماز | لذت بافتن و محظوظ شدن باشد . | بو » بنتم اول و ثانی و سکون واو »
487 سای هس | و بفتح او وسکون ائی‌نام ماه - و ستارمشتری | باشد ۱ - و بفتح اول و ضم ثانی ابرو را گونند | بر وار 
496 بزمان ۲ بفتح اول بر وزن افنان . | غسگین و غمخوار و افرده رااگویند » ویضم‌اول | ح‌ آفقه ات | بر هژه ه با زا
509 ۳" ۱ ۱ ۹۳ | بد آث « با دال ابجد بروزن فرهاد .عم ۱ | شهری است. از عراق عرب و اسل آن باغ داد | ازکرمشگی و 
532 بولی ۱ | شیرینی است - | بواس. فتح اول بر دزن ایای 0 | محتت وآزّار ورنج وسختی باشد. | بو اسحق طافه‌ای باشند ۱
533 ۳ن حد | که آرزو باشد بجای حرف اول بای حطی عم | آمده ات ٩‏ . # | رستنی ودرخت پرشاخ وب رکی را کوبند که بسیار
535 مشهور - و بمعنی یار هم هست که امر بآوردن | باشد ٩‏ . * | باشد » و بعضی گویند آشی بفر! است - و بسنی | سنبوس
541 بو همان - بسکون‌ناكث بروزن‌دودمانه | پمعنی رحم است که زهدان و بچه وان باشد - | و از اسمای مبهمة فارسی هم
567 او | نیز گویند . ۱ | پاچیله » بر وزن پانیله . کنش و پا | افزار باشد . | پاخره ‏ بفتح خای نقطه دار و رای | بی ن
604 پردا | پرد بمنی يك لای و دو لای با يك ته و دوثه - | ویمعنی خواب همآمدء است مانند خواب مخمل | و جوی آب بائد
614 پرعدوار | و ثل وار ۱ نتمولنانی‌وسکون | مه بش فب ریز کته که ریخب | ۰ ۵ | بر ندوش ؟- با واومجپول بروزن | کمن وش 
629 حمشوق است. | بی جانشین ۳ ۳ | شخصی ات که چون صاحب دکان برخیزد او | یجای صاحب د کان بنشیند وکالا بقروشد | ی خم
688 تالار | تالاد ۱ «بروزن سالاژ» نختی ما خانه‌ای | باشد که بر بالای چهارستون با یشثر از چوب | و نخنه سازند ۰ | 
695 تبنگه - بفتح اول و ثانی بروزن النگه, | طبله‌ای که نان در آن گذارند- و تنور نان‌پزی‌را | هم گفته اند وظرف
721 مهوت | حطی‌ورای بی نقطه, نره‌ای‌باشدشبیه تبرخون(۱)؛ | لسکن بفایت تلغ‌است . | فر گر ب4 » بادر نجبوبه‌است» و
726 تشت وخایه . ۱ - هه - : | مسهل سودا و بعربی کثیرالارجل و اقب الحجر | آشت و خایه » بومی‌از بلزی باشد. | وآآن
737 9 کین | 0 هیرین نله » با نون بر وزن چرنده ۰ کچ | است٩‏ - و ثلق وزر ورق را ليز گویند » و طلق زبالرا گوشد 
749 زو کت 1 مکلرها | کوچك ومسندی که کم‌بدست آ بده هم آمدماست. لطات و نهایت | آبی دوعی از بلور است در غایت لط
752 شور خانه | مشترك میان فارسی وعربی و ترکی» بمعنی محل | تلو رخاف ع با خای نقطه دار بالف | کشیده و فتح نون »
```


## [2026-09-05T20:32:36.536Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (243,244,245,246,247):\n    print('===== leaf',i,'=====')\n    print(t[i][:2500])\nEOF",
 "description": "Print BQT leaves 243-247"
}
```


### [2026-09-05T20:32:38.156Z] TOOL RESULT

```
===== leaf 243 =====
دوع ۰ با غن نقطه دار سس وزن
فاروق , بادی را گویند که از کلو باسدا برآید ؛
و بجای غن , فاف نیز گفته آند و عوق فافه
کردهاند .
آدون- بر وزن قارون » صفتهای
خوب و نيك را کویند .
| رو ند - بفتح دابع و سکون نون
خاقال آیسیی‌هان ‏ قو کت وق رورا
شف ۷
آدوین - بر وزن پا کدین » تجربه
و اسحان و آزماش راک ند .
ده ه بروزن چاره. بیخ و بن دندان ها
را گویند ؟ «
]رید بر فك - یکی الت و سکون
نحتانی و دال ابسد . این لفت از اباع است
وبمعنی دوائی‌باشد مانندییاز شکافتهوآ ترالزسیتان
آورند وبربواسیر طلا کتند تاقع باشد . وخوردن
آن زنان راخون حیض آورد ؛ وبکر همزه تیز
کگفته‌اند که آزدبرید باشد و
آریغ ۴ - بکر مالك و سکون
نحتانی و غين نقطهدار . کینه و عداوت باشد -و
سردی (۱) و نفرنی را نز گوبندکه از شخصی
(۱) چك : سردئی .
۱ و ایس کت ادا وود ۴ رك : اربدبربد. ۴ دریارسی‌باستان (دکتبة بستون. متون؟
بند ۱۲ ) 2621624 از رشه ۲18 بمعنی دشمن ۳0288,۳6۲61566ععدای۲۲.۲۲ )
(۱25-6 . 5 ,1895 96110160,5)۲255018این لت درفر‌هنگه‌اسدی چاب‌نهران س‌۲۳۸ونیز
موضع‌دیگر برهان بخلط «آزیغ»آعده. خسروانی شاعرکوید : کآربغ زمن بدل کرفته + کتجکاوی
های علمی و ادبی . نشریهٌ دانشگاه تهران شمارء ۸۳ . قطمه .ای از بفستان بقلم نگارنده 4۱
آریا _ اوستا ۰21۲72 پارسی‌ب‌استان 211۷2. سانسکرمت 217338 «بارتولمه ۱۹۸ نام
طایفه‌ای از ند و اروپائیان که در عبدی بسیارکهن با هم میزیستند و مد ها بدو بخش بزر که
تیم شده کروهی بیند و گروه دیگر بابران آعدند . هت کش مولر ۱۷۵116۲ ۳2( آرائی را
مخصوصاً در باره همه زبانهائ ی که پیشتر بعنوان هند و اروپائی با هند و ژرسانی شناخته شده .
استعمال کرده است ونیزآربا را درمورد همه کسانیکه بزبانهای مزبور سخن میگویند. بکاربردموهم
اود رکتاب۸۷۵۹ 1۳6 ۵۲ 1101886 ۱36 200 ۷۷۵۲5 ]0 01087200165 ص۲4 نوسد:
*آربائیان ۸٩۳۷۵5‏ کسانی هستند که بزبانپای آربائی‌نکم میکنند . رنکشان حرجه وخونثان ازهر
نز اد باشد . ما که آنان را آربائی ميثاميم منظوری جز از تظر دستور زبان آنان که آربائی‌است »
نداريم . » اصل و ره آربا هرچه باشد . ابنقدر واضح اس تکه ابکمه بتداعی ء محانی بیلر را
بخاط میا ورد و غللیکه حثعلق ببخش خاوری هند و اروپائیان بودند . خود را بدین تلم عفتخو
میدانتند . « دائرقالممارف بریتانیا » امروزه غالبا این کلمه را بنژاد هند و ابرانم, اطلاقمسکنند
و شب‌النه این اقوام را آربائی گونند . «مزدیننا ۷۶ ح» و رك : بستا ۳۵-۳۳ .
آریا راهته - ۸۲3۷27۵000۵ نلم‌جد داربوش بز رکه پدر آرشلم» مرک از2739
آربائی و ۲۸۳020 عنی رامش ؛ جمعاً رامش‌دهنده آربایان «بارتولمه ۰۱4۹
بقه از صفحهٌ ۳۲
در بند هش فصل ۲ بند ۳ «اروار» آمده . (رك : یادگار زربران چاپ کاىگرص 4ه شمارء ۷۷)
«بناص 2۱۷۹ » خواناری 61۷272 < سالنامة گلپایگان 4۷ > هربك از دوقطمه استخوان که
دنداهای فوفانی وفحتانی برآن جای دارد - توسماً فك « لفت‌نامه» . رل : آره.
===== leaf 244 =====
در دل کسی‌جای کند ؛ وباین معلی بازای نفطه‌دار
هم آمده است .
11 ۱ مه بسکون زای نقطه داره یمعنی
آرزو و خواهش با ابرام و حرص باشد در جمیع
امور - ونام جابی ومقامی ونام شهری و مدینه‌ای
هی سب .
وه مکی زان طرسی. 2 نی
آسودن باشد - وامربآسودن هم هست معنی بیاسا
وأسوده شو .
]راد ؟
در توابع نشجوان (۱) و مردم آنجا سفید پوست
میب‌اشند ؛ و شرابآنملك شهرت عظیمی دارد-
و عطلق بی عیب وا کویند یعنی هر چیز که
آن عیب نداشته باشد ویی‌فقد ومجرد - وخلاس
شدم ونجات‌افته را نیز کویند چنانکه ا کر کسی
بر وزن آباد . نام شهرست
کوید «فلان را آزادکردم» یعنی از فید بندکی
فارخش ساختم و خلاصش کردم - و سوسن سفید
را نیز آزاد گونند بسبب آنکه او از علت کجی و
تکیه بشاغ دیگ رکردن فارفت - و درختی حم
هت ۴ که آنرا در هندوستان «یکاین» میگوبند
سو درخت آرون (۲) و کاوری را هم گویند - و
حرختی را نیز که میوه ندهد ؛ و همانا که سوسن
وسرورا باین اعتبار آزاد خوانند. ونام درخت‌سرو
هم هست . گویند از حکیمی پرسیدنکه‌چندین
درخت امور و پرومند هت چرا هیج يك‌راآزاد
تمگوند مگرسرو راکه هیچ‌تمره وعیوه ندارد؛
کفت: هربك را ضلی‌معین ووقتی معلوم اس تکه
کاهی تازماند و گاهی پژمرده و سرو از این ها
ارت و پیوسته تازه و نیکو باشد پس صفت
آزادگان این است - ونزد محفقن کی اس ت که
از تعلقات ظاهری و باطتی خلاص باید ؟ . 3
" بشت ۲ ص ۲۰۶۵ > :
چنین داد پاس خ که آز و باز
بر نکند وقانع نسازد. ۴
فردوسی
. > ,۳۲۵ اونئوالا‎ ۶ , ٩۹
- یز آزاد یکی از مهمترین مافیان
استخوان دار است و گوشت آن لذیذ است
۲ 6۲00۸۵ ۶921100 نربه‌انی ۱۳۷۲ >,
٩2100 225‏ « فرهنگ روستائی۱۱۲۰ »؛
آزاد ماهی بزر کترین توع ماهی فلی‌دار است
بند ۳۶» تلم بعض افراد ایران باستان « نام نامة
و
===== leaf 245 =====
سب چ ح
آزا۵ذارو- با دال ابجد بالف کشیده
و رای فرشت عضوم بواو زده » نوعي از چفندر
صحرابی است ریخ آنرا «حلیموه کوبند . ضماد
آن قری و مفاصل را نافع است .
آراد درخت « درختی است که
آبرا درک رکان « زهرزمين » و در فاری «درخت
طاق» و «طعك» میگونند وبعربی «علغم» و«شجره
جره>خوانند , وحنظل‌بارومیوءآن درخت است ٩‏
اکر بر که آنرا جهایم بخورند بسیرند » و اگر
سر بدان شویند موی سر را درا زکند ؛ و بسنی
کویند آزاد درخت درخت طاق است و هیزم آن
بهترین همه هیزمپاست چنادکه آش آن مدنی
بماند ؟ . ۴
آراد سوه ‌ سکن حیم ۰ حلوابی
است که از فند ومغز بادام و پسته و تخود مقس
سازند - و ی نخود فندی وبادام فتدی ویته
قتدیرا کویند که برنگهایمختلف ساخته باشند .
آ راد و اه باراو بالف کشیده و بای
فرشت زده . تام صوتی است از موسیقی - و نام
موضمی است از فرای اسفراین. گونند در آنجا
انگور یار خوب میشود ۴ .
آزن
آزاده ؟ پر وژن آملده . سوسن
و سرو را کوبند - و مردم ولی شطر و مردمان
پیر و صلحا - وحلالزاده و اسیل را هم کنتماند
-وباسطلاح محقفین نفی‌باشد که ازتلقات بشری
رسته وفیدش بمرتبهٌ اطلاق پیوسته وقطر# وجودش
عن بحیط هت یکت ۵ .
۲ ا۵هدل - یکر 7۹ ۲۳
فرع بال است - وعردم سالح و حلال زاده را
بیز کویند .
ادادی ٩‏ بروزن آبادی»ممووفست
اه نقیض بند کی‌باشد. وشکر وشک رکناری را
نیز کونند . 4
[ خ - بنتحثاات وسکون خای‌خطهوار,
دانه های سختی را گوند بقدر نشود که از اسام
آدمی برمی آید و درد تمیکند وبعربی «تولول»
خوانند ۸ .
ده و فك
! دخ ه بازای فارسی. بروزن‌ومعتی‌ازخ
ت که تلو باشد ۸ .
]2شن » تج ثاك بر وزن آمدن .
بمعنی خلایدن سوزن وامثال آن وآج هکرمن
باشد - وّبمعتی رنگه کردن‌همآمده است -
حعر بان «زادرخت» دی .
۱ وخصلت آزادان «لت نامه».
رو زکار نو جح 4 شش۳ : کشورختن > .
آزاد . سس بمعتی بلخوی
ختنی . 82618 «ییلی-
« لت نامه » « ولف ۳
۷۲ - شکر گزاری .
و درد نمیکند و امروزه ز گیل گوبند , «
آزار
وارستگي .
تب که ۲۸ », « منای ۲۹۹ »؛ از ره 28۳
«لْفت نامه .
1 آزارش -آزید گن..
===== leaf 246 =====
آزدن
رذن . بازای فارسی » بروزن و معنی
آزدن بلشد که خلانیدن سوزن وامشالآنست .-
و استره زنب واژنه وگ اشفا زدن نزدمك
سکدیگر را کوبند .
]رده بروزن آمدم .یمعئی رنگهکرده
و خلانیدم شده بلشد » اعم از سوزن وغیره .
3 بازای‌ظرسی, بروزننو ععنی‌دوم
آزده است که خلانیده شده و اجده ده شده
باشی اعم ا ]که باسوزن با چبزی یگ اد
1رد یتح لت و وزن سور ز سغنت
آزار است - وامر بآزردن وآزار دادن هم هست-
و ومعنی کج طبع نیز آمده است - ودر عربی‌نام
آیرا اهیم علبه‌اللام است‌چه بدراین هي علیه‌اللام
۰ ترح » تلم داشته است لیکن سد ازفوت تار ی
آزر اورا پرورده است ۷ .
زر واه ۴ هه یابایایجد بروزن‌مادرزاد
تلم بسر عاراسیند است و او موبدی موده از اولاد
ژردشت معاصراردشیر بایکان ودر آن زمان‌حکیمی
مانتد او نبوده است گر اردای بر وبرانی ۳
که اعلم از او بوده است -
]ررخش ۴ س بر وزن تاج بخش ۰
شورش و صاعقه را گوند عتی. سرما ورعدوبرة
رده س بقتح ثاث وسکون رابع وداا.
ایجد » بمعنی رنگ» ولون باشد .
۲ رده پشت «کنابه از پ رکوژیشت
باشد - و چاروایی را نیز گوبند که پشت او ز انم
و جراحت شده باشد .
آ دم * - پتح ثاك و سکون دابع
و حیم» چند معنی دارد : ۱-.حیا" و شوم باشد .
۲ - بزرگی و عزت و حرمت را کوند . ۳ .
تاب و طاقت بود . ۶ب رحم وشفقت ومپروححبت
و نرمی ومردمی وآدمت. 4- غم واندوه وتشگی
وسختی‌والم را گویند. -٩‏ عدل واتصاف و یکدلی
باشد. ۷- طاهر و آشکارا را گویند . ه سلاحتی
وراحت بود ۰ - نگاهداشت وباس خاطر وتحمل
یائد. *۱ - غب و قهر ر خشم را گویند .
۱- بخواری و زاری گذاشتن باشد. ۷۲- تقصیی
و گذاه را کویند. ۱۳ - بمعنی حسامان شدن‌باشد.
6 - دام دختر خسرو پروم است ۰۸ واو چهار
ماه پادشاهی کرد .
]زر میداخت ۰۷ بکی مم و خم
دال , نام دخترخسرو پرویز است ؛ و آوچپازساه
و ببعنی گوبند شش‌عاه پادشاهی کرد- ونام شهری
هم‌هت که او بنا کرده است .
هيچيك از مدارد قدیمه اسن نام برای پدر ابراهیم نیامده و نام حقیقی او تارح با تارج است .
قرتکل126061] بدلابلی«عازر» و«آزرگرا ماود ازکلمه عبری ج و و(
دانته گوید آن تام‌خادم وفادار ابراهیم بود *جفری ۵۴ - ۵*
و رگ : * داش‌قائمعارف ابلام » و او به بت گرویت نراش معروف است : منت جاهلان است که
چون بدلیل از خس قرو مانند سلسلهٌ خصومت جنبانند چون آزر بت تراش‌ که . ۰۰« کلستان »
۶ لت نزمه * . ۴ صحیم آذرباد است . ره : آذرباد . ۴ - ره :
اردا وبراف. ۴ - تحرف «آترخش». . ۵ -بهپلوی222۳۳70 «منای ..»۲۹4‏ * - مراد
ِ صسلددوات است که اعتاهاً آنرا یر ۳ از آزرم ۱ آزرءنبخت ( داستهاند ۵ ره 4 آزرمیدخت.
۴- ۰ آژرمی ۲+ دخت . ج. اول در اوستا 8۰22۳6702 که خود مرکب است
از 2 علامت نی و 22۲6002 حم رد 2211۳102 و 2217188 که هر دو صفت است بمعنی
قرغوت و شکته و 281801 در سانسکریت 2۲201[ بپمن معنی است , 22117۷2 بمعنی پیری
بقه در صفحاٌ ۳۷
===== leaf 247 =====
ده
آ زر نگ - بفتح رأیم بوزن با درنگه .
بمعلی غم سخت و محنت صعب و رنج و هلا کت
باشد - وبمعنی خیارسبز هم پنظ آمده است ٩‏ .
گت یتح الت وسکون خی تقطمدار»
درختان دیگر ببرند و آنرا بعریی * جلمه »
خوانند ؟ .
دوعص
ادع بزای فارسی » پروزن و معنی
آزغ‌است که شاخهای‌درخت بربده‌باشد؟ - ولیف
خرما را فیث گوشد ۰
آز فنداك - بفتح‌فا وسکون نون ودال
اد بالف کشده و یکاف زده 4 قوی قرح را
گویشد . ی
]رز فندا لك « بازای‌فارسی»بروژن‌ومعنی
آزفندالك اس که قوی قرح باشد -
1۳ ۳
] ذ گن « بازای فارسی ساکن وکس
کاف فارسی شوت زده » دری باشد که آ ترا مانتد
پنجره ساخته باشند و از ععب آن وان نگاه
(۱) چب ۲ , چش : آکندن .
آژنگه
کرد . *
] ز هثل » بامیم بروزن پای‌بنده خداوند
حرص داز باشد یمنی حریص وصاحب خواهش »
چهنند بمعنی صاحب وخداوند است . #
| د هون بر وزن واژگون , آزما
و امتحان رااگوینب ۴ ۰
]زر ند - با زای فارسی بر وزن یایند ء
کلی باش که بر روی خشت به نکنند و خشت
دیگر بربالای آنگذارند ‏ وگل و لای‌ته حوض
و جوی را نیز کوبند - و کلابه را هم گفتهاند .
آجیده کردن باشد .
 یتع‎
! ز ثف ین » بروزن‌واخندسن, درمیان
]زر زگ ت‌ بفتح ال وسکون رابع‌وکاف
فارسی , چين و شکنجی را کوین دکه بر روی
و آندام مردم اند خواه از ری و خواه ازروی
بسیاراست ؛ یکی دو مثال که بعض فرهنگها برای آزرنگه با زاه میآورند عن‌بسش شواهد آنرنگه
است و اما معنی خیار سب زکه باين کلمه داده اند پی شك اشتباهی است که ظاهرا تخت صلحب
اداة الفشلاء را دست داده است و مثشاء اشتباه کلمةٌ بادرنگه بوده که برای تعبی وزن آنرنگ دد
سخه ای دیده و آرا معنی‌کلمة آذرنگ صو رکرده است . < لفت نامه 5
۴ ره : آزمایش وآزمودن » درذیل .
ه آزمایش پهلوی صلاوز202ه مرکب از 2 + ۳2 « تب رک ۰۸ صه
ما2۵ < اووالا ۲۳ > رك : آزمودن . ه آزعودی _ ارمتا 217702
م رکب از پیشوند 21 ( < 2ل1 که در پارسی دز» شده) و 118 بمعنی انداز هک فتن ؛ تجربه
کردن » آزما شکردن .
بفیه از صفحةٌ ۳۹
است و در بهلوی نیز 320( بممنی پیری آمده که در ثرهنگهای فارسی هم بمعنی پس
وفرتوت باد شده . فلم ولقب پدر رستم» «زال» و «زر» هر دو از بك ریشه و بيك معتی است ممتی
فرتوت . پس ازرمه بعنی پیر ناشدنی: و فرسوده فا کشتنی و آزدمیدخت لفة یعتی ( دختی ) پیر
نشدنی با دخث همشه جوان « فاب اس ۳۱۷-۳۱۱ ح » ابنکه بسضی آنرا مضفف آزرمین دخت
( دختر شرمگن ) دانته‌اند مبتنی بر فقه ال عامیانه است .
۳ ِِ رك: از غ.
```


## [2026-09-05T20:33:00.146Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nprint(t[242][:3000])\nEOF",
 "description": "Print BQT leaf 242"
}
```


### [2026-09-05T20:33:02.004Z] TOOL RESULT

```
]دی ح بکر الث و رايع و سکون
تحتانی ۰ بمعنی ممنوی باشد که در مقابل لفظی
است ۰ چه آرش بمعنی «معنی» است ٩‏ .
آدع بضم نالث و سکون غین نفطه
دار , مخفف آروغ است . و آن بادی باشد که
با صدا ا زکلو برهیآ مد ۰
]رغاده (۱) - بر وزن مارساده + نام
رودخانه ات .
]دغده ؟- بن الك ( ۲ ) بر وزن
آزرده. بمعنی نخبناك (۳)وخشمگین وقهر آ لود -
و جنگاور باشد - و بفتخ الث حريصي در چپزها
را گویند .
۲۰ ریش «- بنتح اول و ثانی ۰ بر وزت
صم کیش ۷. بوست. بیرخت زرهاباخد وآنرا
دو دازو ها چشم نیزبکار برند .
۱ آآرمان ۴ بر وزن آسمان ۰ بمعنی
جح تب و آرزو - و رنج بردن باشد - و پشیمانی
و آفوی را نیز گویند . *
آمده - بکر میم ۵ . مخفف
وسکون میم بروزن دارنده. بمعنی دریغ‌وافوی
و پشیمانی باشد .
] دهش » بکس میم . مخنف آرامش
)۱ خم ۳ آارغاوه ۰
)4( خم ۳ 0 رنگ دادن.
و
است که ساکن شدن و آساش ‏ فراغت وراحت
کردن باشد .
آدهون - بر وزن ولژگون » زری
را گوند که پیش از کارکردن بکارگر و هزدور
دهند . و معربی «عربون» خواند . 4
| رهیفه » بر وزن نا رسیده . قرار
] دن ه بر وزن فارن . مخفف آرنج
است که بند گاه ساعدوبازو باشد. وبعربی«مرفق»
خوانند ۷ ,
اد نج - بر ون نارنج . بندکگاه
ساعد و بازوست که عرب « مرفق » گوید ۷ - و
بمعنی بازو هم بنظر آعده است که ازمرفق باشد
تا دوش .
]را نگ - باکاف فارسی. بروزن وهعنی
آرنج‌است که مرفی‌داشد - ور نگ ولون (4)را
یز کنته اند - و بمعنی حمانا و پنداری وگمان
بری حم‌آعده است - وونج ومجنت‌را عم گویشدب
و بمعئی مکر و حیله و فررت تیز حستتویمعنی
کونه وروش و طرز حم گفته‌اند چنانکه گویند :
«بدین آرنگ» یعنی بدین (۵) رز و باین دوش
و بدین گونه - و نام میوه‌ای هم مت - وحاکم
ملك را فیز گوشد ِب#
۲۱ ) خم ۳ : غشان.
۳ ت‌ اارغیش
آرمده سکون هیم -
6۵ در اشمار
ه آرمیدن _ ره : آرامدن ۰
براندیشه شد تا چهآ ید بدند
> مزدسنا ۷۹ ۱۹۸ و هی‎ ٩
( قاطع برهان 4 )
```


## [2026-09-05T20:33:17.115Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"rγnt\\|rgnt\\|ryn't\\|greedy\" SOD.txt | head -20\necho \"=== SOD_pages greedy ===\"\ngrep -n \"greedy\" SOD_pages.txt | head -20",
 "description": "Grep Sogdian dictionary"
}
```


### [2026-09-05T20:33:17.180Z] TOOL RESULT

```
9111:(ro)dcsirc,  Ga)be  greedy 
9133:(to)bt  greedy 
10190:greedy 
10197:greedy 
10207:greedy 
10322:(/o)be  greedy 
10361:greedy 
17152:greedy 
87640:(to)be  greedy     245,  248,  429 
90124:greedy     414,  416,  418,  439,  1446 
=== SOD_pages greedy ===
4513:          (ro)dcsirc, Ga)be greedy
4532:         (to)bt greedy                                                    261 »sp'nh ? S                                 ? J>i&<JX
4934:     freewaman, noble                                                          greedy
4942:                                                                               greedy
4956:404 Vy      B                                                                 greedy
5031:        (/o)be greedy
5064:        greedy                                                452 >b»nc =* »b>nc
7949:     greedy
37694:(to)be agitated    8153                (/o)become active       1102            (to)be greedy     245, 248, 429
```


## [2026-09-05T20:33:19.880Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4925,4970p' SOD_pages.txt; echo \"=== ===\"; sed -n '5025,5070p' SOD_pages.txt",
 "description": "Print SOD greedy entries"
}
```


### [2026-09-05T20:33:19.934Z] TOOL RESULT

```
400 Vt-      B                                        ^Ij.jJ^
                                                                               born
     az(a/i)t, azat ? =>*z}y-, \jyt-, Vyt-
     be born, born                                                             TSP 2.612; Hen. BSOAS 11, 70, 16; Frag. Len.
     TSP 2.1199, 1148                                                            92.10; BSTBL, Vaj. 2, 3; Vim. 92

401 Vtch      B, S                           ojljv^d oljT Oj              414 »zpr>k(w)      B
                                                                                                                         *j' <u*ij>-
     azac (»ztch) ©f. adj. =#»zt>k(w)                                          azpare (^zpr'y)
     freewaman, noble                                                          greedy
     VJ 1099; Anc. Lett. 1.3                                                   SCE, 45, 124, 329, 375, 457
                                                                          415 "zpr'y ^ »zpr>k(w)
402 Vtk ** >z»t»qt
                                                                          416 Mzcn M
403 Vwnh       B, S                               xjjoyry                     azcan
     azon
       ''jwn (»zwn)   ©ob. -y; pi. -/; ob. pi. -ty #*zwn,
                                                                               greedy
                                                                               GMS 1020; Tales. 480 n g
     creature, being, child(w/z*c/i has been born or
       reborn)                                                            417 »zh B

     VJ; SCE; TSP; STii; BSTBL; Frag. Len.; Hen.                               az ©ace. -wh; ob. ~yh ^'z1
                                                                                                                           \Ji
         Tales. 486.17; MD; >zwn(h), KG; Vwnn, TSP 2,                                                                  •^J' ^--^
                                                                              TSP; SCE; BSTBL
         576; Hen. Texts. 737 n 2; *z(,W, VJ; SCE;
                                                                          418 Hzmyc
                                                                               greed M
         BSTBL; V'W/z, VJ 1226; KG 565; V'Wy,
         Tales. 486 n 1; MSP; VJ 1168; BSTBL                                  azmec
404 Vy      B                                                                 greedy
                                                     ^Jy
                                                                              BBB p72 b9; GMS 1103
     azay (*zy, "z'y, *zy)
     birth                                                                419 Mznd M
     TSP 2.1174                                                                aza/and ©ob. -yy      =>*zynd, Vnt
                                                                                                                        (U--«J <^jU^|j


405 Vy-     B, S          (j^ ^^ jj>)j>\j 0-^jJ>>                              tale, parable
                                                                               BBB d8                                        -l0ijl
    azay (*zy-, *zy-, Vy-) ©<*d-zaya ^z'yt-,
      *z>t-> *jy-, }zy-                                                   420 »zr B
    Go)be born
                                                                               azar Opw »zr) ^Vyr-1, Vyr-2
=== ===
        Bzty(y)     M =» »zt>k(w)
129
        "zw pr-       B                   o>j<s>j>- O^jT
        azu Par                                                      =>»z>yr-2
                                                                   (to)be  hurt
                                                                   Hen. Tales. 470.50; GMS 548, 713; BBB a 1
        (/o)be greedy
        SCE 322                                               445 wzyt- => *z>yt-, »jyt-
4 V)
        "zwn       B, S => Vwnh, *zwn                         446 »zyt- =» »z>yt-
                                                              447 »zyt>t B                                        0Jj J^
        *zwn      C                     ^S Xj iJwj^3 *>>yry
        azon (*zwn) ©pi. -/ =»>jwn                                 azitat, azotat    ©pi ^z'ytk
        child, existence, life                                     born
        STii 4.1; STi 84.20                                        BSTBL, Vaj. 2
4*:
        •zwncyk B                                             448 »zytk =* Vytk
        azon elk
        childhood                               K&i'iJ'ijf    449 »zyty =* »z>ytk
        Frag. Len. 42.2
433
        *zy =* fz*y
                                                                                           >
4U
        "zy- =» *z*y-
                                                              450 >b C
        "zy =* •z'y
                                                       £JJ,
        *zy- => *z}y-                                              ap/p (»ph) =>>p,»p
4*7     ■xy1 B                                                     water
                                                                   GMS 305; STii 3.26
        i/iya (*zyh) ^"z'y
        birth, existence                                      451 »p> B, S
        SCE 563; GMS 972; TSP 2.130
4 A
                                                                   (o)pa (b>]) ©3sg. impf. =*P-, pw-, p>\ wpjl,
        *zyh =* ,zy)                                                 wP>2, wP-
        *iyh ryjyy      M                                          GMS 798; AVS 227
        3/c-rczc
        greedy                                                452 >b»nc =* »b>nc
        Wdica. 16, 18.12b                                     453 'pc'npS'k 'ysywny =^ Pyy 'ysywny
                                                                                                                   18


^c'npScyk
```


## [2026-09-05T20:33:28.913Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"ryynt\\|rynt\\|rgnt\\|rynd\\|arxand\\|argand\" SOD_pages.txt | head -20\necho \"=== entries 50-70 ===\"\ngrep -n \"^ *5[0-9] \\|^ *6[0-9] \\|^ *7[0-9] \" SOD_pages.txt | head -30",
 "description": "Search Sogdian for arghant"
}
```


### [2026-09-05T20:33:29.000Z] TOOL RESULT

```
=== entries 50-70 ===
3974:                                                                     65 »8yt M                                       t            s
3983:                                                                     66 »8yy      M =» »dy, »8»kw
3985:   50 »8kt*m B                                                       67 »fryn- M                             ■ <- -r
3991:                                                                    68 "fryny M
3992:   51 "SprmGi) B          (j^    -,   ^ >      ,
3997:  52 aoup
4006:  53 »«wh B                                                        70 »frywn M                                                            -
4012:  54 »6wk     B =» »5>wkh                                          71 »y _» V
4013: 55 »8wr»yk     S(C)
4022: 56 »dv S                /■
4023:                                                                   73 »Y»z     B -> »Y'z
4027:                                                                  74 "YlnS B .                                            J^K*.
4033:58 »6yc => »5>yc(w)
4034:                                                                  76 nvV2     R
4035:59 »8yh M =» »dy, »8>kw
4036:60 M8yn»(h) M                                                        step,
4040:                                                                  77 »Y>st- S =» »Yst-'
4044:61 *8yn»k =» »5'yn>k-                                                cover, covering
4045:62 »5yn>y =* »5>yn.k                                                 VJ 961; BSTBL; Gharib. AI 4.249
4047:79 »Y>y8- B                    b^jj^y-icr^y*-                aya5o ©<aTa6aku ?
4359:      54                                                               apene   ©f. ^p'ync r>Ph
15902:        58                                                            BSTii: C2 gloss.; Yrywh, Anc. Lett. 2, 4, 3.3, 4;
16577:          71                                                 4514 ywz- B,S                                      ^^
20402: 58 1 1 n's B, M, C                           jijT <^U «lj               ninth
28226:       52                                                                Hindu priest, ascetic
32610:                                                                                67 VJ 1, 29, 1109; TSP 1127, 15.31;
```


## [2026-09-05T20:33:34.317Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4013,4050p' SOD_pages.txt",
 "description": "Print SOD entries 55-62"
}
```


### [2026-09-05T20:33:34.365Z] TOOL RESULT

```
 55 »8wr»yk     S(C)
    aGOrik                                                         72 Vrt         B                    \■ LT'-i'S'
                                                                                                            . . f jpj^-
                                                                                                                   ... . <~~a*.Jo
     Assyrian                                        ijjj^l
                                                                      indigestible ?
     STSC 67                                                                          ■                                           "
                                                                      axart ?
                                                                      TSP 8.124; Hen. JRAS 1944, 144.3
 56 »dv S                /■
                                                                   73 »Y»z     B -> »Y'z
      » w
    a5e8>k(»5y, »6yy) ©pi. _l; ob. pi. -tyv „,dy(
                                                  )
                                                                  74 "YlnS B .                                            J^K*.
    somebod                                                          axans =*»x>s, 'ny's
         y, anybody                                                   fight, dispute
    GMS 1560 ff, 1580, S W, SGI 1986, 407f                            TSP 9.12, 13ii 7
5" B8y M, S -» »5'y, »dy, 'dy(y),
                                  -yfiyyt                         75 »YV      M -> »yrt>k
58 »6yc => »5>yc(w)
                                                                  76 nvV2     R
59 »8yh M =» »dy, »8>kw
60 M8yn»(h) M                                                        step,
                                                                     ax    pace ar                                                    '
   aoene (»5yny) ©<MP                                                SCE 197; BSTBL, Dhy. 93, 97, EGSii 167
   Irid ay
                                                                  77 »Y>st- S =» »Yst-'
   GMS 49; JRAS 1945; Fasts. 149.12,
     151.6 n 2 pl53                  19, 153.14, 36               78 YwS     B       *        «           ,^             ,.
                                                                     ayofc ©<a-gaud- =»»Ywnd-
61 *8yn»k =» »5'yn>k-                                                cover, covering
62 »5yn>y =* »5>yn.k                                                 VJ 961; BSTBL; Gharib. AI 4.249
Y6-
79 »Y>y8- B                    b^jj^y-icr^y*-                aya5o ©<aTa6aku ?
                                                             wish
   aye5 ©<*a-gadaya- =^*Yy5-
   (to)wish, (fo)demand                                      VJ; EGSii 75; GMS 960; nom. VJ 29d, 650, 1185;
```


## [2026-09-05T20:33:40.905Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8').read().split('\\f')\nprint(len(t))\nfor i in (122,123,124):\n    print('==== leaf',i,'====')\n    print(t[i][:2500])\nEOF",
 "description": "Print SOD leaves 122-124"
}
```


### [2026-09-05T20:33:42.844Z] TOOL RESULT

```
645
==== leaf 122 ====
 51
                                                                                                                  V^stMc
                                                                     from Argi
 1440 »r5wk      M                                  o-lj
      ar5uk      ©<*ardu-ka; OP; Av. ardda-t ardumanls               Sogdica. 8.13, 10.1 13c; Hen. BSOS 9, 564; GMS
         -^rdq, >r5kw, yw>rdq                                          1016.L >rkc*nch; Frag. Len. 44.7
       sincere                                                 1452 »rkh B, S =» >rk
       GMS      154,423                                        1453 'rkr'k S                                        fjf
1441 Mwky'     M                                 coj^^Ij             ark-are     (Wry)   ©<V£-Htr>£   ©pi. -f
                                                                     worker
     arSukya   ^'yw'rSwky*
     sincerity
                                                                     MDii  pl59.13;
                                                                       ark-kare   ? Y/rVy, Sund. MSP p41, "work",
       GMS 423

1442 >rSyf-       M =» Wyp-                                    1454 Vkrwn'y      B                     >'<J><J^^X
                                                                     ark(k)arune    Orkrwny)
1443 'rSyp' «> 'rS'yp*
                                                                     (related fcOwork, effective, effect
1444 *rdyw- C                     o^d^f ijz*J                        BSTBL, STii 8.3, 4 p576
     arSew, or5ew ©*d-drdwaya->a~drawaya;
        Khwar. V<5V ©3sg. prcs. yrdywt                         1455 'rkrwny => >rkrwn}y
      (ro)scducc, (ro)lcad astray                              1456 'rksyntr => nksyntr
      C2, 102R19 pl77; Schwartz. JRAS 1966, 119                1457 Jrqwny C
                                                                    arakune
1445 >ry B, M, S                                   J>jJ*^J
     ary ©<*arga ©ace. -h>; ob. -y                                   madness
     value, price                                                    C2, 111V1
      BSTBL; TSP 2.981, 3.97; Frag. Len, 93, 32; Talcs.        1458 >rm-    C
                                                                                                                   J**
        469.33; GMS 1164; MSP bl09
                                                                     (o)ram (rm) ©gen. -y
                                    
==== leaf 123 ====
  'rp'st'wyh                                                                                                             58


       wealthy, precious, powerful                                     flour
       Karab. Insc. 21.21, -w 16.7; MDii apud. S W, SI                C2, 94 V 21
         cahier 7, 1989, 184                                     1480 >rtJ =* »srwc(yy)

 1465 Yp'st'wyh        S                                 ^3J     1481 Yt'kCw) => >rtk
      arpastawe                                                  1482 'rt't rwc M, S
      wealth                                                                            (W^j^jj^'^"^^                    Jjj
                                                                      artat roc ©<haruvatdt
       Hen. Talcs. 486.12
                                                                       sixth day of the month
 1466 Yp\vy        B                     (^^rj^o)^^                    GMS 86 n 1; Hen. Oricntalia. 8, 94; Magi. 149.10;
       arpux Orp'wx, >rpwx, }rpwy)                                       MDiii
       penetrating, profit
                                                                 1483 'rt'w    B, M, C          ajujf ***/ y <Jfji*y, <^>
       BSTBL, Dhu. 74; Bcnv. Notesii 214; Mack.
                                                                      artaw    ©MP    ahlaw; Parth. Vrf'w; OP artawan;
            BSTBL n p49; Hen. LW     102; S W, BSOAS
                                                                         Av.asavan ©pi. ~t-y ob. pL -ty =>}rtw
            1975, 133, }rp+-wxt < axu                                  faithful, clcctus, righteous
 1467 }rp}wx =* 'rp'wy                                                GMS 91, 1076; TSP; Tales. 469.4, 476; Frag. Lcn.;
 1468 Ypst>k => Yp'st'k                                                 STi 45.14; Sund. AoF 1981 p2l3; C2, 39V6,
                                                                        54R19; BBB; MSP
 1469 Vpsty       C, S                                   \+jf
       arpastc ©pi. -t ^'rp'st'k                                 1484 »rt'w frwrtyy     M         '^jJ)JjYJ<j^      jr-*±
       precious
                                                                                warti
       STii 18,3.41, 5.13; MSP b80                                    artaw-fra
                                                                      first clement
 1470 Ypwy =» *rp*wy
 1471 Ypwx => 'rp'wy                         
==== leaf 124 ====
                                                                                                                   >rw>st>k
 59

                                                                1504 »rtwy'     C                                \ys ^»r
                                            (j^U Ji-u? i^sjX*
       artawya   ^rtwy*                                               arawya     ^rt'wy'Oi)
       righteousness, state of electus                                righteousness
       GMS     1111; BBB b46; MSP b77; STi 31.6                       C2,40V21

 1492 VtSvy^h      B, M          oL^^^y/^^                      1505 Ytxwst M         (,js^ ^l^<f*^ _s<^)jyi^JL4ri>J
                                                                     artxwost, artxust Ortxwwst) ©*rta vahista-,
                                                                       >*artavahist>*artxw9st ^rtywst rwc,
       artawyak   ^rt'wy'Ch)                                           Wwxwst rwc
       community of clccti, righteousness
       TSP 2.617; GMS 1111; KG 586                                    Light(//ie third element, a Manichean god),

 1493 Yt'wy'mync C                         ^>jW^°~-^                    light392, 422; Gersh. Sogd. Cpds. 410; Sogdica.
                                                                      GMS
      artawyamenc
                                                                        27.19; BBB
      righteousness
      Sund. AoFviii 1981, 179,17                                1506 Ytxwwst =*> 'rtxwst

1494 Yt'w zrwsc      B                                          1507 Vty1 M, C          -VrrO" j->)(uy >^    jJ)u~r,*ij-i<j
                                                   ^->jj ^
     artaw zrusc
      righteous Zoroaster                                             orti Orlyy, }rtyh) ©Knot, rro ©in compd. with
      S W, 1IJ 1976, 46, Frag. 4.6                                       pron. ^>ty, »PZY, rty, TRZY, }rt\ Bty(y)
                                                                      and, then
1495 Yt'xwst => >rt>wxwst rwc
                                                                      GMS 3, 307A; BBB; KG; MSP; S W, BSOAS
1496 Vtyw rwc S (^J :^j^)^^ jc^, jjj^jj/J                               1983, 41 n 2, 46; C2, 183, >rtyswfsy, >rtysn
     artxu roc, artixu ©Av. asdis-varjhuya-.
                                                                1508 Yty2 C                                               ^7
       <*rtivahv
```


## [2026-09-05T20:33:53.132Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8').read().split('\\f')\np=t[122]\nprint(len(p))\nprint(p)\nEOF",
 "description": "Print full SOD leaf 122"
}
```


### [2026-09-05T20:33:54.937Z] TOOL RESULT

```
5411
 51
                                                                                                                  V^stMc
                                                                     from Argi
 1440 »r5wk      M                                  o-lj
      ar5uk      ©<*ardu-ka; OP; Av. ardda-t ardumanls               Sogdica. 8.13, 10.1 13c; Hen. BSOS 9, 564; GMS
         -^rdq, >r5kw, yw>rdq                                          1016.L >rkc*nch; Frag. Len. 44.7
       sincere                                                 1452 »rkh B, S =» >rk
       GMS      154,423                                        1453 'rkr'k S                                        fjf
1441 Mwky'     M                                 coj^^Ij             ark-are     (Wry)   ©<V£-Htr>£   ©pi. -f
                                                                     worker
     arSukya   ^'yw'rSwky*
     sincerity
                                                                     MDii  pl59.13;
                                                                       ark-kare   ? Y/rVy, Sund. MSP p41, "work",
       GMS 423

1442 >rSyf-       M =» Wyp-                                    1454 Vkrwn'y      B                     >'<J><J^^X
                                                                     ark(k)arune    Orkrwny)
1443 'rSyp' «> 'rS'yp*
                                                                     (related fcOwork, effective, effect
1444 *rdyw- C                     o^d^f ijz*J                        BSTBL, STii 8.3, 4 p576
     arSew, or5ew ©*d-drdwaya->a~drawaya;
        Khwar. V<5V ©3sg. prcs. yrdywt                         1455 'rkrwny => >rkrwn}y
      (ro)scducc, (ro)lcad astray                              1456 'rksyntr => nksyntr
      C2, 102R19 pl77; Schwartz. JRAS 1966, 119                1457 Jrqwny C
                                                                    arakune
1445 >ry B, M, S                                   J>jJ*^J
     ary ©<*arga ©ace. -h>; ob. -y                                   madness
     value, price                                                    C2, 111V1
      BSTBL; TSP 2.981, 3.97; Frag. Len, 93, 32; Talcs.        1458 >rm-    C
                                                                                                                   J**
        469.33; GMS 1164; MSP bl09
                                                                     (o)ram (rm) ©gen. -y
                                                                     crowd, people                               f>S'f*r
1446 Vy'nt B                                 (xijO^^^jT
                                                                     BSTi 236
     aryand ©Av. drdYant           -^ry'nt
     greedy
                                                               1459 Vmyh B                          otaijjj <o~oj>> <l^_
      TSP 2.235 n pi 72; Hen. Texts. 734; Bailey. Asica.            armc ? © A v. aerime-, Oss. armdst
        5
                                                                    deserted, isolated
1447 Vyw        B *± }ry                                             VJ 1084 n p97; Bailey. Prolexis. 203

1448 Vyw'n B                                                   1460 Vmyn        M                                  j^^J
                                           jtyj
     aryawan ©Akk. argamanu; Aram, argwdnd                          armin
                                                                    Armenia
      purple
      BSTBL, Dhy. 362; BBB 527; Benv. Notesii 237,                  Hen. AM      1952,206.13
        iii 227 n 1; CII 1990, B19
                                                               1461 rn— B           j: ^T j_^y Oj'j j^" < o^jj ' jjoj^'o
1449 >rk M                                        J^<J+*<jf         ar(a)n ? ©*ar/iw; Skt. rnoti
     arsk Orkh, rq) ©Khwar. }rk\ Pahl. harg\ Yaghn.                 (ro)urge, OcOdrive on
        ark                                                         TSP 3.234; BSTBL, Dhy. 23, Dhu. 167
        n>kt>rq©f. n.; ob. -y; pi. -/; ob. pi. -ty =^pw 'rq,
                                                               1462 >rn(h) B                               XoUo^^
      work, action, business                                        arn ©Av. ardna*, Khot. drra
                                                                    fault, wrong
      GMS 526; BBB 567; Tales. 470.54; Sogdica. 16.19,
        29, 7, 9; VJfcA, VJ; TSP; SCE 492; STii 9.4;                VJ 1451; TSP 2.971, 1057, 1104; SCE 33, 465;
        BSTBL; Tales. 466.6; Frag. Len.; KG 333; MDii;                BSTBL, Dhy. 40, 73, 134, 141, 144, Dhu. 83
        MSP; >rq> BSTi 159; STi 65.9; BSTii: C2 gloss.
        Benv. JA 1959, 125                                     1463 >rnq C                                      ? J&>«£j
                                                                    arank ?
1450 »rk*ry =* >rkr>k                                               colour, form ?
                                                                    S W, C2, V7 plOO
1451 >rkcyk      S         <j~JLLJ'jJ>iS^:J'jl)J,j\J*l
                                                               1464 'rp'st'k S                        -^j^^JjU^1^
      ark elk
                                                                    arpaste Orpst'k) =»*rpsty, 'rwstk
```


## [2026-09-05T20:34:10.476Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== HRN argand ==\"; grep -n -i \"argand\\|arġand\\|arghand\" HRN.txt | head\necho \"== HUB ==\"; grep -n -i \"argand\\|ərəγant\\|ereghant\" HUB.txt | head\necho \"== ARY latin index ==\"; grep -n -i \"ARGHANDEH\\|ARGAND\\|ORKESTR\" incoming/ARY/ARY_latin_index_pages.txt | head\necho \"== MON orkestr ==\"; grep -n \"اركستر\\|ارکستر\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head\necho \"== KLN orchestra ==\"; grep -n -i \"orchestra\" KLN_1966.txt KLN_1971.txt | head",
 "description": "Batch grep for arghand and orchestra"
}
```


### [2026-09-05T20:34:10.639Z] TOOL RESULT

```
== HRN argand ==
1084:Geldner, Drei Yasht 27)^); phlv. argand [argimd ist
== HUB ==
1288:295. Np. pardgandan zerstreuen', phi. pargandak 'scat-
== ARY latin index ==
== MON orkestr ==
MON_part2.txt:24527:سازهای ارکستر قرار گرفت. در سال ۱۸۴۳ 
MON_part2.txt:88382:شد و در ارکستر راه یافت» هارپ ارار ۴۷ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:24527:سازهای ارکستر قرار گرفت. در سال ۱۸۴۳ 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:88382:شد و در ارکستر راه یافت» هارپ ارار ۴۷ 
MON_part1.txt:6645:کوچکی که ارکستر آن آهنگ‌های عامبانه و 
MON_part1.txt:10177:ارکستر: 6۲ (.) (مس.) در بونان قدیم 
MON_part1.txt:10181:ارکستر سنفنیکك (مد.) ارکستر بزرگی که 
MON_part1.txt:10183:و غیره بکار برده شود. این ارکستر از 
MON_part1.txt:20872:دارد. از این سازها دستهٌ ارکستری نبز تشکیا 
MON_part1.txt:46692:جاز: 15 (.) (مس.) موسیقی ارکستری 
== KLN orchestra ==
KLN_1971.txt:62706:in orchestras. — ME. cimbal , symbol, fr. OE. 
KLN_1971.txt:168329:orchestra, n., 1) in the Greek theater, the place 
KLN_1971.txt:168332:um, reserved for the musicians. — L. orchestra, 
KLN_1971.txt:168341:rise’. See orient, n. For the suff. -tra in orchestra 
KLN_1971.txt:168345:to write or arrange music for an orchestra, or- 
KLN_1971.txt:168347:music for an orchestra. 
KLN_1971.txt:168350:barrel organ. See orchestra, 
KLN_1971.txt:168741:1st irritate, orchestra, oro-, Ortalis, russud. Cp. 
KLN_1971.txt:171374:cp. orchestra . 
KLN_1966.txt:10083:in  orchestras.  —  ME.  cimbal,  symbol,  fr.  OE. cymbal  and  MF.  (=  F.)  cymbak,  which  both derive  fr.  L.  cymbahtm,  fr.  Gk.  xupipaXov,  fr. x<VPt],  ‘the  hollow  of  a  vessel,  cup,  boat’,  fr. I.-E.  base  *qumb-,  ‘to  bend,  curve’,  whence  also OI.  kumbhdh,  ‘pot,  jar’,  Avestic  xumba,  of s.m.,  Toch.  A  kumpac,  ‘drum’,  W.  cwmm,  ‘val¬ ley’,  Bret,  komb,  ‘small  valley’,  MIr.  comm, ‘vessel’,  cummal,  ‘cup’,  and  E.  hump,  ‘swelling, protuberance’  (q.v.)  Cp.  cymba,  chime,  n.  Cp. also  combe.
```


## [2026-09-05T20:34:14.550Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '168329,168350p' KLN_1971.txt\necho \"=== HRN 1080-1095 ===\"; sed -n '1075,1100p' HRN.txt\necho \"=== MON_part1 10170-10190 ===\"; sed -n '10170,10190p' MON_part1.txt",
 "description": "Print Klein orchestra, Horn argand, Moin orkestr"
}
```


### [2026-09-05T20:34:14.645Z] TOOL RESULT

```
orchestra, n., 1) in the Greek theater, the place 
where the chorus danced ; 2) in the modern the- 
ater, the space between the stage and auditori- 
um, reserved for the musicians. — L. orchestra, 
fr. Gk. opxrjCTTpa, ‘place in the theater in which 
the chorus danced’, lit. ‘place for dancing’, 
formed with -Tpa, a suff. denoting place, from 
the stem of 6px£i<r&ai, ‘to dance’, which is 
cogn, with OI. f ghayati, ‘trembles, rages, raves’, 
fr. I.-E. base *ergh-, which is prob. an enlarge- 
ment of base *er-, *or ‘to set in motion’, 
whence opvuvai ‘to rouse, stir up’, L. orfri, ‘to 
rise’. See orient, n. For the suff. -tra in orchestra 
Cp. palaestra. 

Derivatives: orchestr-al, adj., orchestr-ate, tr. v., 
to write or arrange music for an orchestra, or- 
chestr-ation, n., the writing or arranging of 
music for an orchestra. 

orchestrion, n., a large musical box resembling a 
barrel organ. See orchestra, 
=== HRN 1080-1095 ===
(153).
Vergl. türk. arys, oss. d. ItW.arcin (Hübschmann
S. 120).
71. er esk 'Neid, Eifer, resk.
aw. araska- 'Neid') ^) ; phlv. arsk^ rask, arSktn, arsklh,
bei. hirs (156) ist nach Dames und Hübschmann
(ZDM6. 44, 558) arabisches Lehnwort.
72. eryend, eryende 'zornig, gierig (Sahn., Mohl, V, 122),
aw. ereyunf' 'finster' (Bartholomae, Handbuch 220,
Geldner, Drei Yasht 27)^); phlv. argand [argimd ist
wohl nur verschrieben); ai. vergl. räjas-.
73. evff 'Castell, Citadelle'.
phlv. arkpatj nDp'?&* (Talmud) und weitere Formen
bei de Lagarde, Semitica I, 43; vergl. auch Nöldeke,
Tabari-Ubersetzung, 5, 111.
lat. arx, arceo, vergl. gr. doycew; arm. vergl. argel
'Hinderniss', argelum 'abwehren* (H. No. 38).
74. erm 'Arm' (nicht belegt, nur im BQ).
aw. aremö\suta' 'mit dem Arm geschleudert'; ai. irma-
'Arm, Vorderbug'; got. arms.
wa;^. yurm 'Vorderarm*; arm. armukn 'Ellbogen'
(H. No. 45).
eren *Elle' siehe ären (No. 14).
75. ez von, aus' etc., z% z-,
gel. ju köi {r= ez kujä),
ap. hacä; aw. haca; phlv. aj; ai. sdca,
=== MON_part1 10170-10190 ===
صف آرائی سیاه و و ان ر قدیم» مقدمه 
قلب» میمنه» میسره و ساقه. ارکان حرب: 
(اصطلاح روزگار قاجاریه و آغاز دورة 
بهلوی) ستاد ارتش. ارکان دولت: بزرگان و 
اعیان و مردان نامدار و کارگردانان کارهای 
دولتی. 

ارکستر: 6۲ (.) (مس.) در بونان قدیم 
نوازندگان و خوانندگان در جلو 
صحنه. گر وه نوازندگان با مجموعة سازها که 
با همکاری یک قطعهٌ موسیقی را اجرا کنند. 
ارکستر سنفنیکك (مد.) ارکستر بزرگی که 
برای اجرای سنفنی‌ها» اوور تورهاء کنسر تو ها 
و غیره بکار برده شود. این ارکستر از 
سازهای زهی» بادی و کوبی تشکیل می‌شود. 


ارگ فرهنگ فارسی معیر ۱۳ 


تعداد این سازها به اندازهة معینی است و
```


## [2026-09-05T20:34:31.363Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== PHD argand ==\"; grep -n \"argand\\|arg and\" PHD.txt PHD_mackenzie.txt | head\necho \"== NYB argand ==\"; grep -n \"argand\" NYB_vol2_glossary.txt | head\necho \"== SYN page 863 leaf 887 ==\"; python3 -c \"\nt=open('SYN.txt',encoding='utf-8').read().split('\\f')\nprint(len(t))\nprint(t[887][:1800])\n\"",
 "description": "Grep Pahlavi and Buck"
}
```


### [2026-09-05T20:34:33.075Z] TOOL RESULT

```
== PHD argand ==
PHD.txt:542:~ AZ: free (oneself) from. pargandan, pargan- [plkn-, plgn-dn! | (P pr'gnd, N parāgandan)] scatter, distribute, disperse. pargast [plgst' | N ~] let it not happen! Heaven forbid! pargüd [plgwt' | P prgwdg], ~ az: free, exempt from. parig [plyk' | M pryg, N pari] witch. paristag [pistk! | N pirista] servant. ~th: service; worship. paristar [plsť] | N parastár] maidservant. paristidan, parist- [plst-ytn' | M pryst-, N parastidan] serve, worship. ~išn: service, worship. paristog/k [plstwk' | P prstwg, N piristū(k)] swallow. рагпабап [pinyE?n! | M prng?n, N parniyān] polychrome damask. parr [pl | M pr, N ~] feather, wing. parrag [plk', pig | P prg, N ~a] wing. ~ig [-vk'] winged. parréxtan, parréz- [plyhin', plyc-] remain over, be superfluous. parrón [plwn' | M prwn] hence, away. parrwar [plwl | M prwr] winged. parsig [p’lsyk' | N pārsī] Persian. pars [5/f] spotted, speckled. parwāl [plwl | (P prwrz)] refreshment, nourishment. parwal- [plw���l- | (P prwrz'dn)) foster, nourish, -išn: nourishment. parwanag [phonk! | M prw’ng, N ~a] guide, leader. ^h : guidance, leadership. parwand [plwnd | N —] enclosure, comprehension. parwand-, v. parwastan. P parwānģāh [*plw?ng’s] throne. parwār [plyw?l | N ~] citadel; circumvallation; suburb, surroundings. parwardan, parwar- [plwl-tn' | M prwrdn, N ~) foster, nourish, cherish, educate. ~išn: nourishment, fostering, education. parwast [plwst'] enclosure. parwastan, parwand- [plwstn', plwnd-] surround, enclose, contain, comprise. parwāz [plw’c | N ~] flight. parzin [picyn' | M prcyn, J przyn, (N parčīn)] fence, hedge. pas [AHL < A?hr; BATL < Ab2tr; ps| = M, N ~] then, afterwards, behind. ~ az: after. ~ih: rear. pas [p’s | = M, N ~] guard, watch. ~ dāštan: keep watch, guard. pāsbān [p’sp’n' | M p’sb’n, N ~] guardian, watcher. ~ih: defence, protection.
PHD.txt:1644:disperse pargandan.
PHD.txt:1657:distribute baxtan, pargandan.
PHD.txt:3526:scatter afšāndan, pargandan.
PHD.txt:4671:fragandan, pargandan
PHD.txt:4682:frasang parragig pargan- parwar pargandan pargüd frég, parig frest- fréstadan fréstidan pargast fréstag fréb
PHD_mackenzie.txt:4031: pargandan, pargan- [plkn-, plgn-du'               (P pr'gnd, N paragandan)]
PHD_mackenzie.txt:6432:disperse pargandan.                     draw (pull) kesidan; (picture) nigar-;
PHD_mackenzie.txt:6446:distribute baxtan, pargandan.           dry husk.
PHD_mackenzie.txt:7494:row radag, rastag.                         scatter afSiindan, pargandan.
== NYB argand ==
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
2945:par-bütan [pr-YHWWN-tn'] to shun, to avoid: yuvatak hac 63%. — I maintain the reading of the MSS; J.-A. deleted pr-. From Olr pard (Av. 852 pard) + butan, cf MPrs przyr ‘to abstain from’, prer- ‘to avoid’ <  "para-car-; prgn- (v. pargandak); Verbum 227.
2954:pargandak [plgndk'] scattered, dispersed 1092-10, 1121, — Pt. of para + kan- ‘to throw’ (Verbum 227), v. apakandan; M Prs prgn- (S); NP pargandah (the vb. is here pardgandan).
2955:pargandakéh the state of being scattered 111/5. 1122-8,
2956:pargandakiha [~-yh’] ina scattered state (some parts here and others there) 108%.
6083:prgn-: pargandak, par- butan
7315:pargandah: pargandak
== SYN page 863 leaf 887 ==
1545
n’, etc., fr. Anglo- Fr. purchaser = OF r. purchasser ‘seek to obtain’, epd. of chasser ‘chase’, fr. VLat. *captiare. NED s.v.
6. ‘Sell’ fr. ‘give’.
Grk. aor., dredidunv, fut. aroddcopat, the regular Attic and most widespread terms for ‘sell’ in these tenses, mid. of drodliwur ‘give back, pay’ (11.65).
Lith. parduoti, Lett. parduot, ChSl., SCr., Boh. prodati, Pol. przedaé, Russ. prodat’, all cpds. of verbs for ‘give’ (11.21).
ON selja, OF sellan ‘hand over, give’ and ‘sell’ (both senses also in ME), hence, with specialization to ‘sell’ com- plete, Dan. selge, Sw. sdlga, NE sell (also LG sellen esp. of the small trades- man) : OHG sellen ‘hand over, give UP» Goth. saljan ‘offer’ (sacrifice), caus. of *sel- in Grk. édelv ‘take’, Walde-P. 2.504. Falk-Torp 1231. Feist 408.
7. Miscellaneous. pay
Goth. bugjan ‘buy’, fra-bugjan sell’, OS buggian, OF bycgan, ME bugge, bigg’s NE buy, all ‘buy’, ON byggja ‘buy (a
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Jet out’ (land), d’ (money) Goth. biuga n
dt.+), NG pop. Tovde, is the prevailing view fr. a Ee. jn Lith. pelnas ‘profit’, tpel- see Bee, Sk. mr fqli. (beside feili) “for ‘ onc J i 1 ete. (cf. below). Falk-
Torp 902.
PROPERTY, COMMERCE
Digitized by Arya Samaj Foundation Chennai and eGangotri
819
‘trade’ fr. ‘travel’ (above, 2 and 11.83, 11.84), more prob. a new act. (cf. Cret.
fen! 7 F) eh jon (as W? i ryéw ‘sell’ beside dvéopat ‘buy’) to awdéo- ection 1 121. Feist | wvew se ya y Ee: Falk-TorP pat ‘go and come, frequent’ (Hom.+) : ; é f ’, Lat. colere ‘cultivate’ d for ‘sell’ in | 7éopae become’, uneer, the usual wor Skt. car- ‘move’, etc. Schrader, Reallex.
1.437. NIv. diolaim ‘pay’ and ‘sell’, see 11.65. Skt. pan- ‘bet’ (cf. pana- ‘gaming, a wager’) sometimes also ‘bargain, buy’ (cf. panya ‘wares’, etc.) and v
```


## [2026-09-05T20:34:40.032Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('SYN.txt',encoding='utf-8').read().split('\\f')\nfor i in (930,931,932):\n    print('==== leaf',i,'====')\n    print(t[i][:1600])\n\"",
 "description": "Print Buck around printed p.863"
}
```


### [2026-09-05T20:34:41.820Z] TOOL RESULT

```
==== leaf 930 ====
eside old awg ‘sharpness, eager- ness’ (so Evans, Dict. s.v.; not men- tioned in this group in Walde-P., Peder- sen, or Stokes 5 f.) fr. the d-grade of Lat. Gcer, with aw reg. in monosyllables as brawd ‘brother’.
2. Grk. xpdome5ov, cpd. of xpas = xapa ‘head’ and zédov ‘ground’. Walde- P. 1.405. Boisacq 509.
Grk. xethos, NG xeldc ‘lip’ (4.25), also ‘edge’ as ‘rim, border’.
NG d6épas ‘spike of grain’, ‘edge’ of a knife, etc. (also the ‘choice, best part’), fr. Grk. a6np ‘spike of grain’, ‘barb’ of a weapon, perh. : Lat. ador ‘a kind of grain’. Walde-P. 1.45. Boisacq 18. Walde-H. 1.14.
NG xéyn, fr. xém7w ‘cut’.
Grk. oréua ‘mouth’ (4.24) was some- times used (through ‘front’), for the ‘point’ (Hom.) or for the ‘edge’ (Aesch.), of a weapon, e.g. oréya paxalpas ‘edge of a sword’ in LXX and NT, rendered liter- ally ds gladii in the Vulgate, this again (Lk. 21.24) by OE mip suordes in Lin- disf. vs. swurdes ecg in WSax. versions, likewise OHG mund suertes in Tat. (in Goth. the passage is lacking).
3. Lat. dra (derivs. > It. orlo, Sp. orilla) : Lat. 0s, Skt. ds ‘mouth’, OE or
‘beginning’, dra ‘border, edge’ also under ‘coast’, 1.27). Eton 709, 714. REW 6080. i
Lat. margd (> It., Rum. : etc.) : Goth. marka, OE Sif BAG ‘boundary’. Ernout-M. 593. Walder 2.39 f. ,
It. filo, Fr. fil ‘thread’ and ‘edge’ Sp filo ‘edge’ vs. hilo ‘thread’, fr, Lat. filism ‘thread’ (6.38), with development through the fine line of the edge. Wart- burg 3.532.
It. taglio, Rum. tais, fr. It. tagliare Rum. édia ‘cut’ (9.22).
Fr. tranchant, fr. trancher ‘cut? (9.22),
Fr. bord (Cat. > Sp. borde) fr. Gmc, bord (belo
==== leaf 931 ====
snout, Pp ks Walde-P.
ersen 1.42.
thread’ (6.38), used also for
(semantic borrowing) Fr. fil. barvenn, fr. barv ‘barb’.
a ribl er ‘shore, bank’, but also
Lat. ripula, dim. of
Numerous other
‘edge’, like
a(c)arf, etc. (15.78).
MUHG snide, NHG schneide, fr. sniden
‘out? (9.22),
ON bord, OF bord, OHG bort, etc.,
general Gme. word, in part ‘edge, bor-
der, but esp. ‘ship’s side’, root connec-
tion dub, Walde-P, 2.163, Falk-Torp 94.
eae W. 88. NED s.v. board, sb. nee Fr. bord ‘edge, border’, etc. and,
th : — a Fr. deriv., ME bordure, NE
MLG kant, kante, D Dan,, Sy, kant, NH Be LLG >
i: : G kante), used esp. ae ae edge’ (as of a table, ata.) a fe cant (formerly ‘edge’ or §, all fr. a form of the group It. 1 @te., prob. the OF. on cn eb alk-Torp 499. NED s.v. N mee and, trond, OHG rant, or hi ‘only for the ‘boss of a eld’, but Dan., Sw., Du >)
Digitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 861 NHG rand the most comprehensive word for ‘edge’ as ‘border’, etc., prob. fr. an extension of *rem- in ON rimi ‘strip of land, ridge’, OE rima (mostly in epds.), NE rim, OHG rama ‘support, frame’ (NHG rahmen), etc. Walde-P. 2.372. Falk-Torp 876.
Goth. skaut (reg. for kpdomedov, but always ‘edge’ of a garment) : ON skaut ‘corner of cloth, skirt, bosom’, OE scéat ‘corner, region, lap, cloth’, fr. the root in OE scéotan, OHG sctozan ‘rush, throw, shoot, hit’, ete. Walde-P. 2.554. Feist 431.
OE sné@d ‘bit, slice’ and in Gospels reg. for Vulgate jimbria = xpacomedov, fr. snedan ‘cut off’.
OHG trddo (Otfr., Tat. for NT fim- bria, kpaomebov), prob. fr. the root in OE tera
==== leaf 932 ====
ROPEAN SYNONYMS
8. Skt. agri-, above, 1.
Skt. dhard-, Av. dard- (also Uzi-darg ‘with sharp edge’) : Skt. dhay- ‘ringe polish’? BR s.v. *dhara-. Uhlenbeck 136 f.
Skt. anta-, prdnta- ‘end’ (12.35), also ‘edge’.
Av. karana- ‘end’ (12.35), also ‘edge, shore’. Barth. 451.
12.36 SIDE Grk. — wAevpai Goth. féra Lith. Sonas, pusé NG se pepia ON sida Lett. sans, puse Lat. latus, costa Dan. side ChSl.  (rebra, strana) It. lato, canto Sw. sida SCr. strana, bok Fy. cété Or side Boh. strana, bok Sp. lado, costado ME side Pol. strona, bok Rum. parte NE side Russ.  storona, bok Ir. toib, sliss, leth Du. = zijde Skt. pargva-, paksa-, NIr. _—_taobh, slios, leath OHG - sit(t)a, fiara ardha- W. ystlys, tu MHG ssite Av. araéa- Br. kostez, tu NHG seite
Several of the words for ‘side’ were first used only for the ‘side’ of the body and are connected with words for ‘rib’.
‘ribbed’, Fr. c6té, Sp. costado (It. costato ‘region of the ribs’). REW 2280. It. canto ‘edge, corner’ (12.76), also
Others are from such notions as ‘half’ or freq. ‘side’ (cf. accanto ‘beside’).
‘part, region’; and, in general, words for ‘part’ (besides those included in the list here) are often used in the sense of ‘side’.
1. Grk. mAevpat, pl. of devpd ‘Tib’, used for ‘side’ of the body (Hom.-+), then for ‘side’ in general (wAevpé sg. for ‘side’ of the body in NT and N G); simi- larly w)evpé, pl. of rdeupdy ‘rib’, in nar- row sense (Hom.) and later generic, etym.? Boisacq 794.
Grk. pépos ‘part, portion’ (13.23), late ‘region’, NG Hépos, POP. pepid usual word for ‘side’.
2. Lat. latus (> It. lato, Sp. lado, OFr. lez, Rum. arch.
```


## [2026-09-05T20:34:48.046Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 -c \"\nt=open('SYN.txt',encoding='utf-8').read().split('\\f')\nprint(t[933][:2200])\n\"",
 "description": "Print Buck leaf 933"
}
```


### [2026-09-05T20:34:50.296Z] TOOL RESULT

```
LATIONS:
Walde-P. 2.99. Walde-
fr. OFr. *costed > Fr.
) Henry 77.
_ tnart, region’ and prob. : ath J P kdipara ‘region’ cide’ (re tart of body’, Eph. 4.16, ghso 4? aim af hleidumein ferai
it 020) p02
Ss ss
2. Nahe, OE side, ete., general Gmc.
W. hyd ‘length’, Ir. sir ‘ong eternal’, Lat. sérus date’, ete. Walde-P. 2.462. Falk-Torp 961.
5, Lith. sonas, Lett. sans (‘side’ of body, but extended in sense), perh. (as og. ‘Tib’?) : Russ., Slov. sanz (pl.) ed’, Mihl-Endz. 3.804f. Traut- mann 298.
a the words for ‘middle’ are ther ec ‘ a single IE form. The td ‘han inner part’, ‘heart’, fense of a r A recurring secondary im by eee is ‘means’ (the me- in Fy, a Ich one attains results), as Lotion ig yen, NHG mittel, etc. This
otherwise expressed by a case-
CC-0. In Public Domain.
igitized by Arya Samaj Foundation Chennai and eGangotri
PLACE, FORM, SIZE 863
Lith. pusé, Lett. puse, lit. ‘half’ (13.24), but used commonly for ‘side’ of objects.
6. ChSl. strana (but mostly ‘country, region’), SCr., Boh. strana, Pol. strona, Russ. storona ‘side’: ChSl. pro-stira, -stréti, Lat. sternere, Grk. orépviju, etc. ‘spread out’. Walde-P. 2.639. Briick- ner 519.
Russ.-ChSl. bokii, etc., general Slavic, orig. dub. Walde-P. 2.105. Berneker 68 f.
ChSI. rebra ‘side of the body’ (Gospels, Jn. 14.34, etc.), pl. of rebro ‘rib’ (4.162).
7. Skt. pargva-, fr. parcu- ‘rib’ (4.162).
Skt. paksa-, also ‘wing, shoulder, half’ : Lett. paksis ‘corner of the house’, aiz pakga iet ‘do one’s need’ (lit. ‘go aside’), Russ. pach ‘groin’, ete. Walde- P. 2.3f. Mithl.-Endz. 3.50.
Skt. ardha-, Av. arada-, also ‘half’ (Av. ‘half’? adj. only in epds.), perh. : Lith. ardyti ‘split, divide’, etc. Walde- P. 1.143. Uhlenbeck 14. Barth. 193.
12.37 MIDDLE (adj.)
aK. kaos Goth. midjis Lith. vidurints Htsos, peoatos ON mior, mio- Lett.  vidéjs, vidus- medius Dan.  ‘midlerst, mellemst, ChSl. (sréda sb.) nel mezzo, medio midt- SCr.  srednij au milieu, mi-, Sw. mellerst, mid- Boh. _ stfednt aunt OE  midlest, middel, midd Pol. —Sredni a ME  middel, mid Russ. srednij i” Miflociu NE middle, mid- Skt.  madhya- « _-mid-, medénach Du. = middelste, midden- Av. maisya-, masama- “* meadhonach, meadh- OHG mitt, mittil va Bria MHG mitte,
```


## [2026-09-05T20:34:59.102Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"ergh\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20\necho \"=== locker undicht ===\"\ngrep -n \"locker, undicht\\|undicht, abstehend\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Grep Walde-Pokorny Bd1"
}
```


### [2026-09-05T20:34:59.157Z] TOOL RESULT

```
9530:erk ergh 
9572:ergh- ,,schiitteln, erregen, beben" oder dgl., wohl Erw. von er- ,,in Be- 
11757:ofglii-, rghi- m. ..Hode" (vielleicht auch *erghi-). 
11780:idg. e- St ufe *erghi-s). 
11785:Kaum hierher dt. nrg, s. u. ergh- „schutteln‘\ 
16969:Unsicherer Gdf. ist gr. giov „Berghohe, Vorgebirge“ : Liden Aufsiitze fur 
17293:Muller IF. 37, 201), sowie lat. virga „Rute, Reis" ( *uergha „die biegsame" 
17328:klr. vereslo ( *uergh-s-lo -) ,,Kurbisstengel 44 , eech .povfislo ,,Garbenband, Stroh- 
17810:portam" (hierher wohl auch osk. verehia- ..Gemeinwesen", s. u. *ita *uergh- 
23414:l.aitkos PI. f. „Driisen‘*, kaiikus ,.Kobold, Gnom, zwerghafter Geist* - , apr. 
26505:slov. krs m. „Strauch ‘, krzljdv „verkfimmert, zwerghaft”, cech. krs ,.Zwerg- 
30499:r ,Schlafe“ (eigentlich „*das Klopfen' 1 , Brugmann II 2 1, 390), „Berghang; 
42291:struppiges IIaupthaar“, schwab. Kauderer „Werghiindler“ ; gr. f^evdo; n. 
50882:dergh- — derep- 
50913:dergh- „fassen“, nicht als Erweiterung von *der- „dicke Haut abziehen“ 
51843:u. trceg , doch s. eine andere Moglicbkeit u. dergh- „fassen“), teils dryz-tu, 
54134:und gegen Zuteilung (Berneker aaO.) zu *dergh- „fassen“. 
54151:— s. u. bhergh „hoch“ — hat auch Persson Beitr. 51 f. keine durchschlagenden 
54152:Beweisgriinde beigebracht), sowie firmus „fest“ (als *dhergh-mos, s. Yerf. 
54380:dhergh-, dhregh dberbh- 
=== locker undicht ===
9238:5. er-, als set-Basis ere-, thematisch (e)r-e- „locker, undicht, abstehend;
```


## [2026-09-05T20:35:02.778Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '9236,9280p' WLD_Bd1_1930_dli_70244_djvu.txt\necho \"==========\"\nsed -n '9570,9600p' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Print WLD er- and ergh- entries"
}
```


### [2026-09-05T20:35:02.844Z] TOOL RESULT

```
Beziehung zu *tr- ,, locker, auftrennen 11 CFickl* 364) ist ganz fraglich. 

5. er-, als set-Basis ere-, thematisch (e)r-e- „locker, undicht, abstehend; 
auseinandergehn, auftrennen 11 . 

Ai. rtc in. Loc. ,,mit AussckluG von, ohne, auBer 11 (Loc. eines Ptc. 
„abgetrennt, abgesondert 11 , mrrti-h „Auflosung, Verwesung, Yerderben 1 ; 
ur-tna- pi. „Triimmer, Rumen 11 , armakd- „trummerbaft“ oder n. „Triimmer- 
stiltte 11 (Bed. etwas unsieher); set-Form Irma- „Wunde“ (wegen der Bed. 
ganz fraglich ist Zugehorigkeit von irina-m „Rinnsal, Bach, Rinne, Yer- 
tiefung, Grube im Boden; Wiirfelbrett, kahles, bes. salzhaltiges Land 11 , 
Uhlenbeck AiWb. 25); tliemat. *(e)r-e- in drain- „auseinanderstehend, un- 
diclit, selten 11 . 

Gr. eofj/uog, att. ko>jfiog „einsam“ (aber dgaiog „diinn, schwacb 11 , agaioDjua 
„Liicke“ hat anl. f-, s. Sommer Gr. Lautst. 114, Uhlenbeck PBrB. 30, 261; 
freilich Boisacq 73 stellt es ohne ersichtlichen Grand doch hierher). 

Lat. rdrus „locker, nicht dicht, diinn, diinngesiit, einzelstehend, selten 11 
(* e rv-ro-s), vermutlich auch rite „Netz, Garn“ (vgl. unten lit. rStis, lett. 
reta) 1 ). 


') Reichelt KZ 44, 318 stellt rite dagegen zu ordior usw., Wz. ar- „iugen", deren set- 
Form er nach rite- als "art- beatimmt. Docli sprechen die formed mit rite iiberein- 
stimmenden halt. Worte eher tiir obige Auffassung. j.Netz* dann etwa aus ,Sieb“, das 
ursprgl. aus voneinander abstehenden Stiibchen und emer sie kreuzenden zweiten solchen 
Stabchenlage gebildet gewesen sein mag. 



ere-, er(e)- 


143 


Lit. yrii, irti „sich auflosen, trennen (von aus mehreren Stricken zu- 
sammengesetzten Dingen" wegen des StoBtons zur set -Form der Wz.), 
su-trelis gewissermaBen „einer, der entzweigeht", d. i. „Unentschlossener, 
Verwirrter", pairas „locker“; rUis _.,Bastsieb“, nach Nesselmann auch „Netz- 
beutel" (mit unurspriinglichem Schleif'ton, wie oft in i-Stammen, s. Persson 
Beitr. 637), lett. reta, rete „Narbe“, rent rudzi „undieht stehender Roggen"; 
lit. ertas „weit, geraumig" („*aus einanderstehend“ ; von der anit- Basis 
retas „diinn, weitlaufig, selten“ (von der themat. Wzf. *(e)r-e-, wie auch:) 
==========
Uber gr. agy.ev&oc und die bait. Worte s. u. arqu- ,,Gebogenes“. 

ergh- ,,schiitteln, erregen, beben" oder dgl., wohl Erw. von er- ,,in Be- 
wegung setzen 11 . 

Ai. rghayati „bebt, tost, stiirmt 11 ; gr. dgyjco „jrd).Am, xiveco", meist ogye- 
o/iai „tanze, hiipfe, springe, bebe“. Lit. bei Boisacq s. v. 

Wegen der in er- ebenfalls vorliegenden Bed. ,.egi; u. dgl.“ konnen 
dazu in Beziehung stehen av. droyant- „arg. abscheulich 11 i Hiibsehmann 
Pers. St. 13). 

Ahd. ar(a)g „feig, trag. bose, arg“, ags. eanj ds.. aisl. argr und 
ragr „unmannlich, wolliistig, schlecht 11 (Fick III 4 19); mit der Yokal- 
stellung letzterer Form (idg. cregh-, (e)rogh-t) vielleicht auch lit. rdyana 
„Hexe“. 

ragana nicht nach Noreen Ltl. 69 zu ir. orgim „verwiiste“ (s. perg- 
„schlagen‘‘ II 42) und gr. tgeydeo is. rekp-). Germ, arga- kaum auf Grund 
der Bed. „geil“ zu doyiz, av. anzi- „Hode“, (Fick III 4 19 zw.; in wegen 
des verschiedenen Gutturals unmoglieher Kombination gleichzeitig mit m- 
yant- Falk-Torp u. arg). 

10 * 



14S 


erd- — er(a!d-, er(a dh-
```


## [2026-09-05T20:35:13.316Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"arg and\\|argand\\|ary and\\|aryand\\|arĝand\" HUB.txt | head -10\necho \"--- HUB pages ---\"; grep -c $'\\f' HUB.txt\npython3 -c \"\nt=open('HUB.txt',encoding='utf-8').read().split('\\f')\nfor i in range(10,30):\n    if 'gand' in t[i] or 'gend' in t[i]:\n        print('leaf',i); print(t[i][:1500]); break\n\"",
 "description": "Grep Hübschmann for argand"
}
```


## [2026-09-05T20:35:14.979Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== IEC ergh ==\"; grep -n \"ergh\\|orgheiō\\|orkh\" IEC.txt | head -10\necho \"== IEC rārus ==\"; grep -n \"rārus\\|rarus\\|rēte\" IEC.txt | head -10",
 "description": "Grep Mann IEC"
}
```


### [2026-09-05T20:35:15.122Z] TOOL RESULT

```
8:publisher to a library and finally to you.
345:72. Np. aryand *zornig, gierig kann zu zd. ereyant-
1288:295. Np. pardgandan zerstreuen', phi. pargandak 'scat-
2977:Hier nach Salemann np. faryand res sordida,
10266:aryand 13.
10430:faryand 84.
--- HUB pages ---
291
leaf 11
I. THEIL.
Nachdem die neupersische Orammatik zum ersten Mai
durch V u 1 1 e r 8 (Grammatica linguae persicae, Gissae 1870)
und Darmesteter (Etudes iraniennes I, Paris 1883) sprach-
wissenschaftlich behandelt worden ist, hat jetzt Horn in
seinem Grundriss der neupersischen Etymologie (Strassburg
1893) den ersten Versuch gemacht, das zerstreute etymolo-
gische Material zu sammeln und kritisch zu prtlfen und das
als biauehbar erkannte Ubersichtlieh zusammenzustellen.
Dass eine solehe Arbeit, die den Stand unseres zeitigen
Wissens klar darlegt und zur Basis weiterer Forschung
dient, den Fachgenossen willkommen ware, soUte man von
vorn herein erwarten. Wenn gleichwohl Horn's Grund-
riss das zu erwartende Willkommen bei der competenten
Kritik^) nicht gefunden hat, so hat das darin seinen Grund,
dass die Ausfiihrung der Arbeit den von dieser Kritik ge-
stellten Anforderungen nicht entsprochen hat. Zum Theil
allerdings mit Reeht. Denn es muss zugegeben werden,
dass der vorliegende Grundriss, weil allzu hastig gemaeht,
mit Mangeln und Fehlern behaftet ist, die bei langerer und
sorgfaltigerer Arbeit vermieden werden konnten. Anderer-
seits ist aber auch gegen die Kritik einzuwenden, dass sie
an den Autor nicht immer billige Anforderungen gestellt
hat, und dass sie uberhaupt zu weit geht, wenn sie die
ganze Arbeit ftir verfehlt erklaren mSchte, weil Manches
daran zu tadeln ist.
Vgl. 8 ale m an n, Liter. Centralblatt 1893, Nr. 43, Sp. 1547/8;
Fr. Mil Her, WZKM., ,Bd. 7 -8; Maun, ZDMG. 47
```


### [2026-09-05T20:35:15.179Z] TOOL RESULT

```
== IEC ergh ==
1236:bherghó, ið “protect, save, foster. WP II, 172 Skt. barhe “cover (zero-grade in brhami 'strengthen"); Oss. cf. ám-bürzín (‘cover’, fr. *som-bherghio); OHG bergan, OE beorgan; Du. bergen; ON bjarga beside birgja; Sw. ber- ga sig “manage; refrain’; OCS brégo, brěšti *care for, protect
1237:bherghos 'strong place' (identified in Gmc. with bhergh- and bhréh-, q.v.) W cf. bre “hill, top? (fr. *bhregh-); MHG berc, -ges ‘bulwark, enclosure’; OE beorg *protec- tion, refuge’; ON cf. birgr (*well-provided', fr. *-ghio-); OCS brégü (*shore, bank’. LW?); Slovene cf. breg “hill, rise, coast'. Cf. Go. baírgan ‘guard’ and bherghó
1781:bhrghəlos ‘hold, holder’. See next, and cf. bherghö (WP II, 172) Br. bréol “iron hook on cart-axle; MHG bürgel ‘surety’
1782:bhrgho, ið “hold, fasten, enclose’. Cf. bherghó (WP II, 172) | Skt. -brhami ‘strengthen’, beside e-gde barhe ‘cover’ and Oss. åm-bårzin, id.; Tokh. A pär- kàw-, B páürko- ‘gain’; Gk. phrásso beside phárkhma &  phrágma; MHG borgen ‘watch, care for; ON byrgja ‘enclose’. An extended form appears to be OLat. fraxare ‘patrol’ (*r) w. sim. long-zero in Alb. brez *girdle; wall-brace'; Dac. substr. briu, id. in Rumanian. Noun-forms include Go. baürgs *walled city, tower' and com. Gmc.; E borough and burrow; OCz. brh ‘lair, den, camp’; mod. Cz. *hencoop, fowling-net’. (The question of an Anatolian equivalent of type *bhurgh- is discussed in SF: baürgs, cf. the Gk. forms pürgos, and (Hes.) phürkos "wall The Cz. placename suffix -brh is said to mean “hill?). Av. borezis ‘cover’ shows secondary palatalism. See next
1794:bhr&hont- (bhrghnt-, bhrghont-) ‘high; height’. WP II, 172. See bhr£&hus & bhergh- Skt. brhát; Av borezafit; Oss. bárzond, pl. bärzändtä; Per. buland, baland; Tokh. A -párkant (B oärk park, pirko) ‘sunrise’; Lat. frons, gp frontium (Ennius: pl. frundes) (forehead, gravity, severity'. For the seman- tics cf. OCS čelo 'forehead': Li. kéin “to raise); Osc. cf. Frunter (name of a god); Gaul. brigantes 'hillmen'; Olr. bríanda *fa- mous’; OBr. cf. brientin ‘noble’; OW breint, braint, „brein, bryein ‘privilege, state’; W braint, id.; Frankish *burgunds; OE brant: ON brattr (variant: *bhrghond-). See next
1795:bhrghus, os “high; height’. WP II, 172. See bhr&hont-, bhergh-. WP II, 172 Skt. cf. brhát; Av. borozoó; Oss. (o-gde. Am- big. bardz, barz ‘mass, crowd': (?) Arm. bardz (2) “hip, thigh’; Arm. bardzr, gs. bardzu ‘high’; Tokh. A cf. párkár, B parkre long; Hitt. parkus; Olr. brí ‘noble’ beside Ir. brigh ‘virtue, power; Sequanian brig- “high — of winds’; Gaul (ambig.) briga Ch, But cf. bhrgh-); W brí, Cor. bry ‘rank, degree, esteem’; OW bry ‘above’: (?) MHG bor ‘up’. Cf. the e-gde forms in Arm. erkna-berdz ‘high as heaven’, lerna-berdz ‘high as a moun- tain’, and OE brego “ruler”.
2186:derghó (dorgh-, drgh-) 'hurt, torture'. Cf. WP I, 801. See dhrgh- Alb. (ambig.) dergjem “lie ill, mp: Tokh. tsárk-, B tsark- ‘annoy, worry’; Ir. deargaim (2) “hurt, wound’; OE tregian ‘harass’;. ON trega ‘grieve’; Li. dérgiu, dérgti (2) ‘abuse’; o-gde in OE tergan, tiergan ‘tease’; Du. ter- gen; G zergen, id.; Cz. drázditi, id.; z-gde in R dérgat ‘scour; pill flax’ and Cz. drhnou- ti, id.
2294:dis- “apart, away, un-, dis-. WP I, 821 Arm. z- (in z-erc ‘free’, z-ercanem "release: Gk. di- in di-ékho, -othéo, -zémai, -óko (perh. also in di-pháo (2) 'seek); Alb. z- (in z-vjerdh ‘wean’, fr. *dis-uergh-), z-vesh Cundress", fr. *dis-uesio); Lat. dis-; OBr. Br. W di-; Ir. dí-; Ir. dí-, id. OHG zir-, zer, MHG zer-
2409:dorgheið ‘provoke, irritate, tear up’. WP I, 807. Variants: dergh- drgh- OE tergan, tirgan; G zergen; Sw. targa ‘tear up’; Slovene drážiti; Cz. cf. drážditi; (z-gde in) R dërgať ‘pluck, pull, pil; Cz. drhat, drhnout ‘Scour’
2410:dorghos, à ‘rim, edge, frame’. WP I, 807 Cf. dhr£h (1) OHG zarga, MHG zarge ‘edge, frame, brim’; G Zarge; OE targa or targe *buckler; OCS po-dragü “edge, seam’. (Li. pa-dárgas = ‘tool, utensil, organ of the body’). Gk. cf. dorkheloí ‘vertebrae, mouldings’
== IEC rārus ==
14937:(īsos, ios ‘rare, thin’, more prob. ufsos, ios, q.v. but ambig. for Gk. araiós, L. rarus)
```


## [2026-09-05T20:35:23.493Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '338,360p' HUB.txt\necho \"--- which leaf/page? ---\"\nawk 'NR<=345{n+=gsub(/\\f/,\"\")} END{print \"leaf\",n}' HUB.txt\npython3 -c \"\nt=open('HUB.txt',encoding='utf-8').read().split('\\f')\nimport re\nprint(repr(t[22][:200]))\nprint('...tail:',repr(t[22][-200:]))\n\"",
 "description": "Read Hübschmann entry 72"
}
```


### [2026-09-05T20:35:25.240Z] TOOL RESULT

```
envy' etc.) wie abar zu bar auf etc. und geht laut-
gesetzlich durch paz. arask (Min. 61. p. 16 als Var.),
phi. arask (Gl. and Ind. p. 20: arashih) auf ap. ^araska"
= zd. araska- zuruck, das nach der Tradition, der auch
Darmesteter folgt, *Neid' bedeutet und zu skr. iras-
ydti 'missg5nnen, neiden', irsyd- *Neid, Eifersucht* ge-
horen kann. Ebenso jetzt Fr. Miiller, WZKM. 8,91.
72. Np. aryand *zornig, gierig kann zu zd. ereyant-
gestellt werden, wenn man diesem die Bedeutung zornig,
gierig' beilegt, was moglich ist, da es Beiwort der
Holle und der Fliege ist. Uebersetzt man ereyant- mit
Bartholomae durch *finster', so gehoren die Worter
wegen der Bedeutungsverschiedenheit nicht zusammen.
Sicher steht die Bedeutung von zd. ereyant- jedenfalls
noch nicht. Daher kommt fiir die Etymologic auch
skr. rghay- *beben, toben', rghavant- 'tobend' immer
noch in Betracht.
78. T^p.isparud „ein kleiner Vogel" (vom Sperling unter-
schieden) gehorte nicht zu d. Sperling^ got. sparva etc.,
falls sp aus idg. kh entstanden ware.
79. Was soil hier got. aiAe;a/wwdi *Dornstrauch' ? Das Wort
bedeutet vielleicht'Pferdezahn, aber schwerlich !Pferde-
futter', was auch sonderbar ware.
--- which leaf/page? ---
leaf 23
"~ 12 --\n(Shk. 228), das auch advtnak u. s. w. gelesen werden\nkann, vor. Also auch hier adTnak = adenak zu corri-\ngiren? Fr. Miiller's Gleichung: ayma = phl. aivmak\n(wie gleichfalls gelesen werden kann"
...tail: 'eutung von drstya- fDaumen* oder *Klafter etc. ?)\nVgl. F r e i t a g , arab. Wb. a. v. rasas.\n^) Die Var. dristya- hat G e 1 d n e r nicht in den Text auf-\ngenommen. Ihr wiirde np. *drist entsprechen.'
```


## [2026-09-05T20:35:37.059Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"finster\" BRT.txt | head -20",
 "description": "Grep Bartholomae for finster"
}
```


### [2026-09-05T20:35:37.229Z] TOOL RESULT

```
3716:•  j.  aipLdvipiara-  Adj.  (fem.  'ra-)  "wolkig,  |  (eben)  zur  Nachkommenschaft  gelangt  ist, neblig';  xsaps  va  *tq%Tyh  °rayS  "oder  in|(jüngst)geborenliat', von FrauemnJiWiffm finsterer,  nebliger  Nacbt"  Yt//.4-  \yqm  °ram  .  .  anasaxtqm  (sd.)  V,  J5.8;  —
4155:—  tpm  vä  ahäm  drvantB ,  .  nUirint^ät \aastäi  'Muhe]"*  V.5.62.  4)  mit  a) asaanqm  GP.,  b)  drvatqm  GP.;  'Ort,  Auf- enthalt der  a)  Gläubigen,  b)  Ungläubigen', im  Sinn  von  3  a,  b ;  tfm  'hüm  paihyaite yim  asaonam  .  .  tarn  'hüm  paüyatte yim  drvatqm  timanhaitt^m  .  ,  V.iS.jS; 5.62,  5)  mit  timatiha-  Adj.  'der  finstere Aufenth^t,  Raum',  von  der  Hölle:  bunim -TihSus  tpmanhahe  yat  »rr/ats  daozaauhahe
12199:•  j.  t«nai»ha-  Adj.  'finster':  £>m  aASm ..yim  ..  tsmaahairam  t»masShr>m  'ah»m V.5. 62,   l8.^(>-,  —    aahSml  'ukahe  V.
12202:•  j.  Mmaohaena-  Adj.  (fem.  '«f-)  'aus Finsternis  bestehend,  finster*:  Ism  ähUm.. yim  .  .  •tarn  t?masairjm  t^tnanhim  V.  5. 63,  /(?.  76;    —    drujim  yqm  .  .  'nun  Yt.
12235:•  j.  t^Oxya-  i)  Adj.  (fem.  yä-)  'dunkel, finster':  °fyam  aipi  xsapanim  Yi.  14.  13; —  'ryasäi  (GSf)'>  kala  xsafnS  "auch in  finstrer  Nacht"  Yt.  1^31,  ib'.  10;  — xfapa  vä  *'ryä  (GSf,)"  aipi.dziqnaraya YL//.  4.         3)  n.  'Dunkel'  (nur  Ableit).
19128:•  j.  ni'tama-  Adj.  (fem.  'ms-)  'der  unterste, am  tiefsten  befiadliche'  (nach  Lage,  Grösse, Zahl,  Dauer  usw.):  °ma?hia  gätuha  hasa- t9rS.Umahvaca  "an  den  tiefstgelegenen  und ganz  finsteren  Orten"  Yt  15. 53  {?);  —  'macit avatlqm  stsrqm  (sd.)  ya'ha  .  .  "die  klein- sten .  ."  F.  4  a;  —  cvatbya  nä  'maübya havana^bya  (sd.)  ratufri^  "wie  gross mindestens  . ."  N.  108;  —  fratamim  dat'ä- hSus  nava  Pfriems  (sd.)  .  .  m^»nts . .  'ntü ft'jrJ  V.2.  30;  30'';  —  *äjata  nU  *''ma'^ bansmana  ratu/ris  'Ü.QO;  —  *cvaia  (sd.) nä  *'ma'^  vaca  gahä  srävayS  ratufril "quanta  minima  voce , ."  N.  27;  —  dvadasa Vitara  (sd.)  upima  nava  . .  mäb>ma  xi^a/. . 'ttia  (NPm.)  V.  14.  14;  —  cvat  'mum haslnm  (sd.)  anhat  .  .  N.  J/;  —  'macit *haoma.küiiil  hazatgraynyai  astt  dalvanqm "auch  die  geringfügigste  //! -Kelterung  dient dazu  tausend  D.   zu   töten"    V,  70.  6;  6*;
```


## [2026-09-05T20:35:44.548Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Fliege\" BRT.txt | head -20",
 "description": "Grep Bartholomae for Fliege"
}
```


### [2026-09-05T20:35:44.599Z] TOOL RESULT

```
3027:KompA.;Ableit.—Vgl.rty'ii*-,flA7Äi-,—  np.vgI.    abscheulichen  Gestalt  einer  Fliege,.,  die
3629:•  j.  apa-srayamna-  Adj..,  PPM.:  s.  sray-. m  j.  apa-za<)ah-  Adj.  (auch  fem.)  'den Steiss  ab-,  weghaltend  (nach  oben?)''*, von  der  Fliege:  ^maxsiJiihrpa  prrfaitya frasnaol  °Sawi4ff(GSf.))  * akaramm.driwya (sd.)  V.7.2.
7633:•  j.  araj-ant- Adj.  (fem.  'yaiii-)  'entseulich, abscheulich';  a)  von  der  Hölle:  paosisUmäi yat  °yat  daozaahum  P.  ^o;  —  *bun9m atiksm  t)iHat?hahe  yal  'yatö  dagzanuhahe V. /^.  47;  —  °yata  haca  duzauha  Yt. /<?.44;  —  'fatal  haca  äaozavilt  Yt.  4. 7.  b)  von  Fliegen:  baivarj  maxHnqm 'yaitinam  V.14.6; — *max/i./hArpa  "faitya (ISf.)  V.7.2.
13957:mit  a  'auf-,  mit>J  'fort-',  mit  vi  "hin  '"ai'hs  *maxUJt7hrpa  tr^aitya'K.^owm. und  herflattem':  dva  *alwi>S>n  dva  *vf^B.-  herzugeflogen  von  Norden  her  in  abscheu- i»n  dva  *frd^5i>n  "die  zwei  (Federn)  ^  ""^lier  Fliegengestalt"  V.  7. 2;  —  cvantim sollen  auf,  die  zwei  sollen  hin  und  her, '  ^«J'"''^'*  ^rväiitm  . .  as'a  druxl .  .  upa.- die  zwei  sollen  fortflattem"  Yt  1.^.45.        .dvasaiH  V.7.3;  1,4.  a)   mit  Angabe
18066:•  j.  fra-änav-  Adj.  (auch  fem.)  'dieKniee(?) nach  vom  haltend',  von  der  Fliege ;  *maxH.- kihrpa  irr^aitya  'snai>s(GS(.)  apazi^ataks *akaramm.driwyä  (sd.)  V.  7,  a.
19551:•  j.  maxäl-  f.  'Fliege':  druxs  yä  nasus  .. nivSiryete  mqnaym  ahe  >fl5a  'syä  par^mm (sd.)  M.8.6'9;  23  PüZ.;  —  basvan 'sinam »rrfaitinatn  ava.Janyät  V.  14.  f>;  —  °H F.  II.       '[V.7.2  lies:' maxä.i^Är^a.].
19553:•  j.  *niaxäi.V«hrp-"  f  'Fliegengestalt':  a^a druxs  ya  nasus  upa.dvqtaiti  .  .  'kihrpa srr^aitya  V.  7.  %.
```


## [2026-09-05T20:35:57.784Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=7633 && /^[0-9]{2,4}$/{ln=NR; v=$0} END{print v, ln}' BRT.txt\nsed -n '7600,7640p' BRT.txt | head -50",
 "description": "Find BRT column for arəγant"
}
```


### [2026-09-05T20:35:59.575Z] TOOL RESULT

```
27 4478
•  g.  39ävä  AD.  Pron.  i.  Pers.  'uns  beide'; kost!  voha  manav/ia  p  I  dayat  (sd.)  °vü maritalibyS  Y.sq.j.         S.  zu  vayam.
D.  i.  ä!;l,  s.  iSchr.  S  26S.  6.  —  ai.  vgl,  ,h'd/i. AD.  —  Pü.:  -/fl*J«>).  —  '}  Wie  für  JjJwÄi (e.  3äA-)  und  »Jwr/.  Für  Fü.  war  also  Pi  der Träger  der  Cedeutung.
g.  iiSuhi  V.  i8.   11:  S.  'ik;
g.  ittäiUä:  s.  »«lu-.
•  g.  Jtiitay-  f.:  s.  unter  /«/ay-.
•  g.  äma'vant- Adj,  (fem.  "iia/Vr-):  s.  unter amavanl:
•  j.  spastinis  varamis  sispimnö  f»9mnÖ paoiris  iiöiyti'^  Yt. /^.ö?.  Vom  verstUm- j meltes  PPM.  in  der  Bedeutung  'veran- ' lassend',  NSm.  ,
•  j.  a-varazika-"  Adj.  (fem.  °zikii-)  'nicht wirkend,  faul':  druxi  ojfä^re  'ke  (VSf.) ' V.  /*.3o.  I
Zum  V.  ivifj;..  —  Pü.:  avirzü«,  etl.:  '"'^  i frärSii  ni  Titr~J.  —  ■)  Oder  auch  'zaka- ;  s. Wh.  Gr."  S  ^'^'S'J'  c-
•  j,  »-var«zyant-  Adj.  i)  mit  Akk,  'nicht wirkend,  begehend':  'zinbyd^"^  pascaila araiwya  syaoina  V.J.  40.  2)  ohne Obj.  'sich  nicht  übend  (tn  den  Werken der  Religion)';  yö  saite  haurvqm  tarasca xsapamm  ayazsmns  . .  'zyö  ".  ,  ohne  zu beten  . .  ohne  sich  (im  Guten)  zu  üben" V./&S-
Fa.;  az'srülSr.    —    i)  Statt  'üi-h'  für  «ij
j.  *9-vito.xra'8iy-'*:  °of-  Adj.  'des  Ein- sicht untüchtig  ist':  *janyöii  .  .  mairyaya ''iayd'>  (GSf.)  Y.mis- *v'i-iaxra.  (%  268.  57)  Adj. ;  iBed.  und  El,  s. /axma-.i)  —  Pü.:  fehlt;  Sü.i  paribbraflabiid- dhik.  —  I)  So  K  5  b,  J  a;  KA.  'j:arA'.  — a)  S  sfiiK  11  b.  —  3)  Oder  darf  man  an  mp. laxr,  np.  lalx  'bitter'  denken?
•  j.  a-viSvah-,  g.  a-vidvah-  Adj.  i)iAw. mit  Akk.  'etwas  nicht  kennend,  womit unbekannt':  yam  asava  .  ,  alayqm  (sd.) vai'ia  tarn  ärrä  'ovä  Vr.22.2.  z)  gAw. absoL  'nichtwissend'  sva.  'nicht  im  Besitz des  wahren  Wissens,  in  die  rechte  Lehre  . nicht  eingeweiht':  mi^akvaia  vä  ^»ns.vam (sd.)  vs  vidva  vä  'dvh  va  ". .  ein  wissen- der oder  auch  ein  nichtwissender"  Y.^JJ. 12;  —  vTdvä  vJduil  mraolB  mä  'dva  *aipj.- dsbävayai  (sd.)  Y._j7. 17.
Pü. .  anäkäs ;  zu  Y.  _J/.  1 2  erl. :  ziitäk  mcniii.
•  j.  a-vindan-  Adj.  'nichts  erlangend, bekommend':  späns  ydi  hisimie  ai^arO upa  !^'ar>ttt>m  *tarS  spasUnS  *dättS  "die Hunde,  die  ohne  Essen  beim  Essenden stehen,  von  der  Seite  drauf  hinspähend, aber  nichts  abbekommend"  V.  y,28.
«was  Schlechtes'.
•  j.  »-vis-  Adj.  'der  kein  Hauswesen  hat'; vUäne  akm^i  (näml.  pourum  framraomi) ya%a  'säi''>  "dem  der  ein  Hauswesen  hat, (spreche  ich  einen  höheren  Wert  zu)  als dem,  derkeines  hat"V.4.47.  \?visaiusi'a N.  s6:  lies  pvistaist'a.]
Pü,:  az-s.  —  ">  Them.
•  j.  s-vissmna-  Adj.  'sich  weigernd'  (etwas zu  tun):  *vTsaiU  (sÄ)  anyB  "usyö  (sd.)  nsil ainyS  'nS  *astryeiH  P-57.
PPM,  lum  V.  vaes:  —  Pü.:  afa/IriiriTA.
•  j.  *»-vista-'*  Adj.  'nicht  erhalten,  em- pfangen'; nur  LP.  'so  dass  man  nichts (dafür)  erhält'  sva.  'ohne  En^elt':  _^iwr.7- TayS  ava  däirayim  dim  vaeniil*°tash'a^'> vindatum  nSil  *afayiJ  *vistarh'a  "wenn  er nur  eine  solche  (so  geringe)  Besoldung dafür  bewilligt,  dass  man  ihn  für  einen, der  olme  Entgelt  (Unterricht)  erhält,  an- sieht, nicht  eine  solche,  dass  es  gegen Entgelt  (zu  geschehen  scheint)"  Ü.iO.
Pü-:  /«/  <ti  i  sräyil  an  i  däsi   {ia)  äH  i  mizd
tindisii   däiiel  iv  yut  hac  aiizd  *man  fäU  mä
i      aad  ia   p.iliak    häl   ta    dAnft  kam   h.if   mizd
I      last.    —    Es   handelt  sich  um  die  Frage,   ob
Uiflitized  byVj 00^ IC
«vistay-
•  g.  5-vistay-  f.  'Nichtteilhafltgsein':  yot .  .  ilrmaiirni  .  .  b?nxAam  (sd.)  .  .  duLfyag- ianä  avazatai  varghSuS'tt  mana»hS"6S.t die  ■  ■  Arm. , .  verscheuchen,  weil  sie  des guten  Sinns  ermangeln,  sie  deren  Tun  Übel ist"  Y.^4-9-
Zum  V.  'vaed:  —  ai,  ivUlay-  f.  —  Pü.;  irom- disnih,  SQ. :  asami;rahanam.
•  j.  9'vistö.kaya8a-  Adj.  'der  die  Kayma (sd.)-Sünde  nicht  kennt':  nar^mla  alavaium iistiiya  .  .  vislö/raoriitlm  'laut  Vr.^.  4.
*i-viila-  Adj.;    gr.  namc,  got.  iiinoh.  —  Pü.: a/riepallik  käslirVi,  er!. :  viiiäsiärih  ne/aitji.
•  j.  a-W8p0Ji''afnan-  Adj.  'der  keinen voUkommenen,  d.  i.  tiefen  Schlaf  Jiat': zainauha  'na  (NS.;  DämL:  ist  der  Hund) yaia  vastryS  fsuyas  V.  y.46.
''nan-  Adj.,  Ableit.  aus  *vispS.3^a/na-  in.    — Pü.:  undeutlich;  tuxiäi  iäma/iSii  iu yäi x'a/ct.
•  j.  araj-ant- Adj.  (fem.  'yaiii-)  'entseulich, abscheulich';  a)  von  der  Hölle:  paosisUmäi yat  °yat  daozaahum  P.  ^o;  —  *bun9m atiksm  t)iHat?hahe  yal  'yatö  dagzanuhahe V. /^.  47;  —  °yata  haca  duzauha  Yt. /<?.44;  —  'fatal  haca  äaozavilt  Yt.  4. 7.  b)  von  Fliegen:  baivarj  maxHnqm 'yaitinam  V.14.6; — *max/i./hArpa  "faitya (ISf.)  V.7.2.
Et?     Vgl.  Hbm.  PSt.  13.    —    Va.:irins\    s.  1 üaiu  BTHU  IF.  13.  113.
•  j.  3r9x§a-  a  £N.  eines  berühmten iranischen  Schützen**:  tiyris  . . y'im  anhat °sS  xi-vitui-Uus  xsviwi.iivaiimd  airyanqm airyö^stii:at  haca  garSit  ^anvantain  avi gairim  "der  Pfeil  , .,  den  der  PfeilschUtze if.  schoss,  der  beste  Pfeilschütze  der  Arier, vom  Berg  A.  bis  zum  Berg  X<:"   Vt.ÄÖ.
*>  Der  Schulze  heissl  i^iX£t  Aris  hvätiri'l. Er  »oU  unter  Manüiikr  durch  seinen  Schuss  die  1 Grenze  des  Reiches  gegen  Turan  hin  bestimmt ' haben.     LitL  bei  Bthl.  1F,  12.  103.  1
Et.?    —    Ji-STi  NB.  89    will    (nach  AWeber)  ;
'gliniend'    als    eig.   Bed.    und    vergleicht  ai.  1
fk^ä-  Adj.  'kahl'.  —  ')  Übersetiung  von  xivr.iii.- 1
•  j.  ii  faiti.b»nitim  "«r«£iii£t«m  N.  2.  I Vermutl.  Super].;  \\  mHMm.  S.  noch  weiter unten   {wo  arslis/>m).  —  PQ. :  fehlt.  I
```


## [2026-09-05T20:36:09.123Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=7700 && /^[[:space:]]*[0-9]{3}[[:space:]]*$/{print NR\": \"$0}' BRT.txt | tail -8",
 "description": "Find nearest column marker in BRT"
}
```


### [2026-09-05T20:36:11.367Z] TOOL RESULT

```
7458: 339
7461: 340
7498: 342
7531: 344
7556: 345
7559: 346
7660: 351
7696: 353
```


## [2026-09-05T20:36:17.922Z] TOOL CALL #50: Bash

```json
{
 "command": "head -40 tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-05T20:36:17.958Z] TOOL RESULT

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


## [2026-09-05T20:36:24.211Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/orchestra' --note 'page 157, root Er 1/Ergh, Greek orkheisthai -> orchestra chain'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%BA%D9%86%D8%AF%D9%87' --note 'page 157, Persian arghandeh node 3'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CE%BF%CF%81%CF%87%CE%AD%CE%BF%CE%BC%CE%B1%CE%B9' --note 'page 157, Greek orkheomai node 5'\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/retina' --note 'page 157, root Ere 1, Latin rete -> retina node 3'\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/rare' --note 'page 157, root Ere 1, Latin rarus -> rare node 3'",
 "description": "Archive web sources"
}
```


### [2026-09-05T20:36:28.179Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0b6e06c74b1fb41a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b57677735d478d8d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/47e985fc134f1399.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e82dab4fad46c0e1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d1de31dcceb3ffe.txt
```


## [2026-09-05T20:36:30.950Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 0b6e06c74b1fb41a e82dab4fad46c0e1 8d1de31dcceb3ffe; do echo \"=== $f ===\"; head -c 1800 $f.txt; echo; done",
 "description": "Read etymonline archives"
}
```


### [2026-09-05T20:36:33.137Z] TOOL RESULT

```
=== 0b6e06c74b1fb41a ===
URL: https://www.etymonline.com/word/orchestra
FETCHED: 2026-09-05T20:36:26Z
STATUS: 200
TITLE: Orchestra - Etymology, Origin & Meaning

Orchestra - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of orchestra 

 orchestra (n.) 

 c. 1600, "area in an ancient theater for the chorus," from Latin orchestra , from Greek orkhēstra , semicircular space where the chorus of dancers performed, with suffix -tra denoting place + orkheisthai "to dance," perhaps an intensive of erkhesthai "to go, come," but not all experts accept that (see Beekes).

 In ancient Rome, orchestra referred to the place in the theater reserved for senators and other dignitaries. Meaning "group of musicians performing at a concert, opera, etc." is recorded by 1720, so called because they occupy the position of the orchestra relative to the stage ; that of "part of theater in front of the stage" is from 1768 in English.

 Some related words still retain the "dancing" sense: Orchestic "of or pertaining to dancing" (1712), also orchestric (1740).
 also from c. 1600 

 Entries linking to orchestra 

 karaoke (n.) 

 1979, Japanese, from kara "empty" + oke "orchestra," the latter a shortened form of okesutora , which is English orchestra rendered into Japanese.

 orchestral (adj.) 

 "pertaining to an orchestra; suitable for performance by an orchestra," 1811, from orchestra + -al (1).

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 More to explore

 symphony 

 "It was only after the advent of Haydn that this word began to mean a sonata for full orchestra....Ell
=== e82dab4fad46c0e1 ===
URL: https://www.etymonline.com/word/retina
FETCHED: 2026-09-05T20:36:27Z
STATUS: 200
TITLE: Retina - Etymology, Origin & Meaning

Retina - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of retina 

 retina (n.) 

 late 14c., "membrane enclosing the eyeball;" c. 1400, "innermost coating of the back of the eyeball;" from Medieval Latin retina "the retina," probably from Vulgar Latin (tunica) *retina , literally "net-like tunic," on resemblance to the network of blood vessels at the back of the eye, and ultimately from Latin rete "net" (see rete ).

 The Vulgar Latin phrase might be Gerard of Cremona's 12c. translation of Arabic (tabaqa) shabakiyyah "netlike (layer)," itself probably a translation of Greek amphiblēstroeidēs (khiton) .
 also from late 14c. 

 Entries linking to retina 

 rete (n.) 

 late 14c., "open-work metal plate affixed to an astrolabe," from Latin rete "net," a word of uncertain origin, perhaps related to Lithuanian rėtis "sieve," or perhaps a loan-word from a non-IE language. The main modern sense is anatomical, "vascular network, plexus of blood vessels" (1540s). Plural is retia . Related: Retial .

 retinal (adj.) 

 "pertaining to or relating to the retina," 1798; see retina + -al (1). Related: Retinally .

 retinitis (n.) 

 "inflammation of the retina," 1821, from retina + -itis "inflammation." Retinitis pigmentosa is attested by 1856.

 Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Share retina 

 ‘ cite ’ 
 Page URL :
 https://www.etymonline.com/word/retina Copy 

 HTML Link :
 <a href="ht
=== 8d1de31dcceb3ffe ===
URL: https://www.etymonline.com/word/rare
FETCHED: 2026-09-05T20:36:28Z
STATUS: 200
TITLE: Rare - Etymology, Origin & Meaning

Rare - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of rare 

 rare (adj.1) 

 [thin, few, unusual] late 14c., "thin, airy, porous" (opposed to dense ); mid-15c., "few in number and widely separated, sparsely distributed, seldom found, very infrequent;" from Old French rer , rere "sparse" (14c.) and directly from Latin rarus "thinly sown, having a loose texture; not thick; having intervals between, full of empty spaces" (antonym of densus ). Sometimes reconstructed to be from a PIE root *ere- "to separate; adjoin."

 "Having the particles not close together," hence "few in number," hence, "unusual." Sense of "remarkable from uncommonness," especially "uncommonly good" is from late 15c. (Caxton). Related: Rareness . In chemistry, rare earth is from 1818.

 Rare implies that only few of the kind exist : as, perfect diamonds are rare. 
 Scarce properly implies a previous or usual condition of greater abundance. 
 Rare means that there are much fewer of a kind to be found than may be found where 
 scarce would apply. [Century Dictionary, 1895]
 also from late 14c. 

 rare (adj.2) 

 [undercooked] 1650s, a variant of Middle English rere , from Old English hrere "lightly cooked," probably related to hreran "to stir, move, shake, agitate," from Proto-Germanic *hrorjan , which is reconstructed to be from PIE root *kere- "to mix, confuse; cook" (source also of Greek kera- "to mix," krasis "mixture"). Germanic cognates include Old Frisian hrera "to stir, move," Old Sa
```


## [2026-09-05T20:36:44.917Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== greek ===\"; grep -n -A4 -i \"etymology\" 47e985fc134f1399.txt | head -40\necho \"=== persian arghandeh ===\"; head -c 1500 b57677735d478d8d.txt",
 "description": "Read wiktionary archives"
}
```


### [2026-09-05T20:36:44.974Z] TOOL RESULT

```
=== greek ===
=== persian arghandeh ===
URL: https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%BA%D9%86%D8%AF%D9%87
FETCHED: 2026-09-05T20:36:26Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T20:36:47.278Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nhead -20 47e985fc134f1399.txt",
 "description": "Check greek archive"
}
```


### [2026-09-05T20:36:47.318Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%CE%BF%CF%81%CF%87%CE%AD%CE%BF%CE%BC%CE%B1%CE%B9
FETCHED: 2026-09-05T20:36:27Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T20:36:53.389Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport urllib.parse\nfor w in ['ὀρχέομαι','ارغند','Reconstruction:Proto-Indo-European/h₁ergʰ-','ὀρχήστρα']:\n    print(w, 'https://en.wiktionary.org/wiki/'+urllib.parse.quote(w))\nEOF",
 "description": "Build wiktionary URLs"
}
```


### [2026-09-05T20:36:55.064Z] TOOL RESULT

```
ὀρχέομαι https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CF%87%CE%AD%CE%BF%CE%BC%CE%B1%CE%B9
ارغند https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%BA%D9%86%D8%AF
Reconstruction:Proto-Indo-European/h₁ergʰ- https://en.wiktionary.org/wiki/Reconstruction%3AProto-Indo-European/h%E2%82%81erg%CA%B0-
ὀρχήστρα https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CF%87%CE%AE%CF%83%CF%84%CF%81%CE%B1
```


## [2026-09-05T20:37:00.047Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CF%87%CE%AD%CE%BF%CE%BC%CE%B1%CE%B9' --note 'page 157, Greek orkheomai (node 5) etymology'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%BA%D9%86%D8%AF' --note 'page 157, Persian arghand (node 3)'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/r%C4%93te' --note 'page 157, Latin rete (entry 3 node 2)'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/rarus' --note 'page 157, Latin rarus (entry 3 node 2)'",
 "description": "Fetch more wiktionary pages"
}
```


### [2026-09-05T20:37:04.628Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/442305fdb495ffed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1bd2acd4c3ac70dd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a330f983833d8256.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2bf075de288c3ef5.txt
```


## [2026-09-05T20:37:08.212Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 442305fdb495ffed 1bd2acd4c3ac70dd a330f983833d8256 2bf075de288c3ef5; do echo \"=== $f ===\"; sed -n '1,6p' $f.txt; grep -n -i -A6 \"Etymology\" $f.txt | head -30; echo; done",
 "description": "Read new archives"
}
```


### [2026-09-05T20:37:10.251Z] TOOL RESULT

```
=== 442305fdb495ffed ===
URL: https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CF%87%CE%AD%CE%BF%CE%BC%CE%B1%CE%B9
FETCHED: 2026-09-05T20:37:02Z
STATUS: 200
TITLE: ὀρχέομαι - Wiktionary, the free dictionary

ὀρχέομαι - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
--
153: Etymology
154- [ edit ] 
155-
156- Perhaps from Proto-Indo-European *h₁ergʰ- ( “ to mount ” ) , [ 1 ] whence also perhaps Hittite [script needed] ( arkatta , “ to mount sexually ” ) . [ 2 ] Frisk suggests that term may constitute an iterative-intensive formation from ἔρχομαι ( érkhomai , “ to come, go ” ) , for which see there for more. Watkins posits a connection with ὄρχις ( órkhis , “ testicle ” ) , which appears semantically tenuous. [ 3 ] Alternatively, the Proto-Indo-European is reconstructed as *h₃erǵʰ- ( “ to copulate; ardent ” ) (which appears more plausible based on basic sound correspondences) and is compared with Proto-Germanic *argaz ( “ indecent ” ) . [ 4 ] 
157-
158- Pronunciation
159- [ edit ] 
--
1069: ^ Vladimir Orel ( 2003 ), “*argaz”, in A Handbook of Germanic Etymology ‎ [2] , Leiden, Boston: Brill , →ISBN , page 23 
1070-
1071- Further reading
1072- [ edit ] 
1073-
1074- “ ὀρχέομαι ”, in Liddell & Scott ( 1940 ), A Greek–English Lexicon , Oxford: Clarendon Press 
1075-

=== 1bd2acd4c3ac70dd ===
URL: https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%BA%D9%86%D8%AF
FETCHED: 2026-09-05T20:37:03Z
STATUS: 200
TITLE: ارغند - Wiktionary, the free dictionary

ارغند - Wiktionary, the free dictionary 
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Adjective 
--
151: Etymology
152- [ edit ] 
153-
154- From Middle Persian [Book Pahlavi needed] ( ʾlgnd /⁠arγand⁠/ ) , from Avestan 𐬆𐬭𐬆𐬖𐬀𐬧𐬙 ( ər ə γaṇt , “ tumultuous, uproarious, raging ” ) .
155-
156- Pronunciation
157- [ edit ] 

=== a330f983833d8256 ===
URL: https://en.wiktionary.org/wiki/r%C4%93te
FETCHED: 2026-09-05T20:37:04Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
=== 2bf075de288c3ef5 ===
URL: https://en.wiktionary.org/wiki/rarus
FETCHED: 2026-09-05T20:37:04Z
STATUS: 200
TITLE: rarus - Wiktionary, the free dictionary

rarus - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Adjective 
--
165: Etymology
166- [ edit ] 
167-
168- Uncertain. [ 1 ] Possibly related to Lithuanian i̇̀rti ( “ to dissolve, fall into ruin ” ) and Proto-Slavic *oriti . It has also been compared to Ancient Greek ἐρῆμος ( erêmos , “ lonely ” ) , but this may be phonetically difficult if certain sound laws involving laryngeals and *r are accepted.
169-
170- More information
171-
```


## [2026-09-05T20:37:24.060Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/rete' --note 'page 157, Latin rete (entry 3 node 2/3)'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A7%D8%B1%DA%A9%D8%B3%D8%AA%D8%B1' --note 'page 157, Persian orkestr node 7'\necho \"=== POK 3. er- headword ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==339' data/verification/sources/refs/POK_01.txt | head -25",
 "description": "Fetch rete + print Pokorny er- headword"
}
```


### [2026-09-05T20:37:27.685Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b2cc3784ee98a8e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bd6eddd0dfe470fb.txt
=== POK 3. er- headword ===
  "halt.  Grundform  *ereUa-,  vgl.  lit.  eras,  äras  , Adler'  (ob  alt?)-
abg.  orhh  (*arila-)  ,Adler^,  russ.  orel,  Gen.  orid;
ob  um.  erilaRj  aisl.  jarl,  ags.  eo?'Z,  as.  erl  ,Mann^,  bes.  ;Vornebmer Mann^,  damit  zu  verbinden  sei  nach  Maßgabe  von  aisl.  jqfurr  , Fürst' eigentlich  ,Eber^,  ist  unsicher;
hitt.  ha-a-ra-as  (haras),  Gen.  ha-ra-na-as  (haranas),  n-St.  , Adler',  wie got.  ara.
WP.  I  135,  Trautmann  13,  Pedersen  Hitt.  41,  Specht  Dekl.  47.
2,  er-,  eri-  ,Bock;  Schaf,  Kuh,  Damtier*^;  vielleicht  ursprünglich  ,Horntier'.    "^
Arm.  or-oj  (assimil.  aus  *er-oj)  ,agnus,  agna',  e^nnj  ,d6:ficxXigj  vitula iuvenca,  bos' ;
gr.  €Qiq)og  (*eri-bho-)  m.  f.  ,Böcldein,  junge  Ziege*^;
lat.  ariesj  -etis  ,Widder^  Mauerbrecher'  (a  nach  a'per,  caper);  umbr. erietu  ,arietem';
air.  heirp  (*erbhl-)  f.  ,dama,  capra',  erh(b)  ,Kuh'  (*erhhä),  mir.  (mit  sekun- därem /-)  ferh(b)  ds.,  nir.  earh,  fearb  f.  ,Rotwild,  Kuh',  schott.-gäl.  earh  ■ f.  ,Reh' ;    zu   kelt.  *erhä  :  Igicpog   vgl.   gr.    oiqcpoq  :  oeqLcpog   ,Insekt' ;    nach Kleinhans  (Et.  Gelt.  1,  173)  hierher  mir.  reithe  ,Widder'  aus  *ri-{o-tio-]         .    ■;
in  apr.  eristian  ,Lämmchen',  lit.  {j)erasj  lett.  jers  ,Lamm^,  litt,  mend  ^ , Lammfleisch'  =  russ.-ksl.  jarina  ,Wolle',  usw.,  sind  wohl  bsl.  *eTO': ,Bock'  und  *jörä-  ,Jahr'  (s.  oben  S.  297)  vermischt  worden;
ahd.  irah  ,Bock'  usw.  ist  aus  lat.   hircus  entlehnt.
WP.  I  135  f.,  WH.  I  67,   Trautmann  70.  ^]
5-  er-  :  or- :  r-,  ursprünglich  athematische  Wurzel  mit  terminativem  Aspekt:  M ,sich  in  Bewegung  setzen,  erregen  (auch  seelisch,  ärgern,  reizen);  in  ST, die  Höhe  bringen  (Erhebung,  hochwachsen),  z.  T.  auch  von  Bewegung nach   abwärts';    Basenformen    er-,    ere-,    er3-(?),   erei-,    ereu-  und     •• (unter   besond.    Artikel)   eres-j    eros-   ,Erhebung',   ernos-  ,Empor-     'j geschossenes',  Partiz.  or-meno-,  r-to-. Zusammenfassungen  bei  Persson  Beitr.  281  ff.,  636  ff.,  767ff._,  836  ff. a.  Basis  formen   er-,    ere-   (einschließlich   paradigmatisch    damit    ver-  ■ einigter  i-  und  w-Formen):  ::   ""
Ai.  redupl.  Präs.  iy-ar-ti  ,setzt  in  Bewegung',  Med.  Irte  (*i-,r-);  gthav.  , iratü  ,er  soll  sich  erheben';  ai.  intensives  Präs.  dlarti]  von  ereu-  (s.  unten
327
S.  331)  rnöti  rnvdti  .erhebt  sich,  bewegt  sich^  (ih'Qvv^L),  ärta  (vgl.  Jjqto), ärata  (vgl.  djqexo]  themat.  wie  rante,  ranta),  Perf.  ära :  bg-cuga,  Fut! arisijati,  Partiz.  rtd-  {irnd-  .bewegt,  erregt^  mit  Verschleppung  des  l  aus irta  oder  echte  Form  einer  schweren  Basis);
av.  ar-  .(sich)  in  Bewegung  setzen,  hingelangen'.  Präs.-St.  ar-:dr9-j iyar-:ir-  (wie  ai.  iyarti-.irta),  Kaus.  araya-,  Partiz.  -drdta--,
5Ä:o-Präs.  ai.  fcchdti  .stößt  auf  etwas,  erreicht',  woneben
```


## [2026-09-05T20:37:34.825Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A5 \"^ Etymology$\" b2cc3784ee98a8e2.txt | head -20\necho \"=== orkestr ===\"; sed -n '1,6p' bd6eddd0dfe470fb.txt; grep -n -A5 \"Etymology\" bd6eddd0dfe470fb.txt | head -20",
 "description": "Read rete and orkestr archives"
}
```


### [2026-09-05T20:37:36.545Z] TOOL RESULT

```
408: Etymology
409- [ edit ] 
410-
411- Borrowed from Latin rete .
412-
413- Pronunciation
--
448: Etymology
449- [ edit ] 
450-
451- From Latin rēte .
452-
453- Noun
--
507: Etymology
508- [ edit ] 
509-
510- Borrowed from Sanskrit अर्थ ( artha , “ meaning , wealth ” ) . Doublet of reti .
511-
512- Pronunciation
=== orkestr ===
URL: https://en.wiktionary.org/wiki/%D8%A7%D8%B1%DA%A9%D8%B3%D8%AA%D8%B1
FETCHED: 2026-09-05T20:37:27Z
STATUS: 200
TITLE: ارکستر - Wiktionary, the free dictionary

ارکستر - Wiktionary, the free dictionary 
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
--
142: Etymology
143- [ edit ] 
144-
145- Borrowed from French orchestre .
146-
147- Pronunciation
```


## [2026-09-05T20:37:46.112Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== SKT orchestra ==\"; grep -n -i \"orchestra\" SKT.txt | head -5\necho \"== LEW rarus ==\"; grep -n \"rarus\" LEW_1910.txt | head -5\necho \"== LEW rete ==\"; grep -n \"^rete\\|rete,\" LEW_1910.txt | head -5\necho \"== LAT rarus ==\"; grep -n \"rarus\" LAT.txt | head -5\necho \"== LAT rete ==\"; grep -n \"rete\" LAT.txt | head -8",
 "description": "Grep Skeat and Latin dictionaries"
}
```


### [2026-09-05T20:37:46.223Z] TOOL RESULT

```
== SKT orchestra ==
12841:Gk.  A/>xi^crpa,  an  orchestra;  which,  in  the Attic  tbcfllrCf  was  a  space  on  which  the chorus  danced.  — Uk.  6pxioftai,  I  tlaucc. Orchis,  a  plant.  (L.  — Gk.)  L.  anhis.^ Gk.  opx^f,  a  testicle,  a  plant  with  roots  of testicular  shape.  Dor.  orchid,  a  false form,    since    tne    gen.    caM    of   ^x"  ^
18704:Strophe,  part  of  a  poera  or  dssoc.  (Gk.^ Gk.  (TT/Mx^i^,  a  turning;  the  taming  of thi chorus,  dancing  to  one  side  of  the  orchestra or  the  strain  sung  during  this  erolotivH: the  ttropht,  to  which  tlie  tknfimwpkt  m swerSyaaGk.  arpiipuv,  lo  turn.
== LEW rarus ==
== LEW rete ==
10384:geerzwaluw (nndl.) I 652 gubelen I 649 gullen (andl.) I 639 hal I 137 hee (mndl.) I 129 hinniken I 647 horzel I 283 hut I 177 woor I 389 inghedom I 3 kakelen (nndl.) I 126 kies I 596 cloet (rondl.) I 604 cocke (andl.) I 242 kokkelen I 242 koot (nndl.) I 188 kraut I 290 lak I 759 lemmet I 872 lese (mndl.) I 813 lien (mndl.) I 227 lood II 421 malu(w )e LT, mere (vondl.) JI 132 meuzre (flam.) IT 133 micke (mndl.) II 85 mere (rondl.) J 531 mumeren II 67 misschien I 535 mite (mndl.) LT SO moot II 127 moy (mndl.) IT 127 natte (mndl.) IL 52 nood II 155 oer II 841 oksel I 25 oonen I 23 pal I 327 plapperen (nndl.) I 109 pont II 337 ponte (mndl.) II 337 puilen (nndl.) I 122 rake (mndl.) J 441 rete, reten II 431
13150:retere, rétal’a I 668
== LAT rarus ==
1299:sit rarus inuentu. -Attest 4 depuis Plaute; conservi dans quelques dial.
16320:densus, -a, -im: serr 4 , 4 pais, dense, touffn (oppos 4 k rarus);
24151:frequens, -entis adj. : terme d'agri culture, s'oppose k rarus, et
== LAT rete ==
68:Comme on n'a retenu ici que des rapprochements qu’on
974:abete comme parete de paries, cf.M.L. Einf. 3 , p.137): "sapin"; puis "bois de
2318:adigo : nener, pousser vera; spdcialeaent "aaener 4 preter serment"
2983:landais a le preterit ro ait "il a mange" tandis que le latin a alui.
3412:raison du caractbre poetique de son style. Meme rarete des derives et
3732:trfes rare. "On pourrait interpreter le premier terme anda- comme le
4021:ce mot. M. Dumezil ( Le Festin d'immortal it i , p.133) interprete Anna
4163:antenatus: synonyme vulgaire et tardif de priuignus, interprete
```


## [2026-09-05T20:37:52.105Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"rarus, -a\\|rarus,-a\\|rârus\\|räre-facio\\|raresco\" LAT.txt | head -10\necho \"---\"; sed -n '1290,1320p' LAT.txt\necho \"=== rete headword ===\"; grep -n \"rete, -is\\|rete,-is\\|rëte\\|retia\" LAT.txt | head -10",
 "description": "Find Ernout-Meillet rarus entry"
}
```


### [2026-09-05T20:37:52.209Z] TOOL RESULT

```
---
de raisin (sec); acinosus : en forne de grain. Pour duracinus v. durus.
Sans dtynologie: provient sans doute d'une langue mediterran 4 enne.
acipenser ( acipensis , cf .uomer et uomis, -eris, acci-,acu-), -is m.
(les graphies aquipenser, accipenser ont 4 t 4 ddtermindes par des rappro-
chements avec aqua, ou accipio. La quantit 4 de l'a est inconnuej: poisson
rare et renomm 4 , sans doute 1 'esturgeon. Cf. dans Ath 4 n 4 e, 7,394 la
description de 1 'ooocUTtqcrLOC; et Plin.9,60: apud antiquos piscium nobi¬
lissimus habitus acipenser, unus omnium squamis ad os uersis contra
quam in nando neant* nullo nunc in honore est, quod quidem miror, cum
sit rarus inuentu. -Attest 4 depuis Plaute; conservi dans quelques dial.
italiens, M.L.139. - Sans etymologie sure; sans doute composd dont le
premier terne serait du groupe de acies, acus.
acisculus: v. ac-.
aclassls: tunica ab [h^umeris non consuta. P.F.18,31. Pas d'autre
exemple. Cf. peut-etre CGL II 13,49 aclassi, Aoqj/XTO (-re?).aclys
13
aclys, -ydls f. : petit javelot. Premier ex. dans Vg.Ae.7,730 qui
1 'attribue aux Osques et aux Campaniens. Terme desuet d'aprbs Servius
ad loc.; rare et poetique. Vg. a un nomin.pl. grec aclydes. Du gr. ccyxu-
Xu£, par un intermediaire etrusque (les Etrusques ont manie cette arme)?
acnua, -ae {agnua, agna ) f.?: nom en latin rustique de 1 'actus qua¬
dratus, "mesure de 130 pieds carr6s". Cf .Varr., R.R. I 10,3, is nodus
acnua latine appellatur. Columelle attribue 1 'emploi du mot aux rustici
de la Betique; cf. le gaul. acina (?). Rare et technique. V.Isid., 15,15,
5, et Sofer, p.164.
acredula, -ae (agr- par etymologie populaire) f.: -ae ranae paruulae
in sicco uel agro morantes, unde et nuncupatae, Isid., Or.13,6,59. Desi-
gne aussi un oiseau inconnu, correspondant a 1 1 bXoXuywv des Grecs, cf.
Cic., Diu.1,8,44 et la note de St.Pease, dans son 6dition; pour le double
sens, cf. bufo et bubo. Pour la forme cf .ficedula, monedula, querque¬
dula (-tulaj .
=== rete headword ===
39847:teurs generalement opposee aux retiaires; cf. Festus 350,0, retiario
43883:mitif. Pline 11,«4 (Oo) Araneus orditur telas. Ordiri retia. Les
47630:autem dicit lanistas ex habitu gladiatorum, quia post mortem retiarii
49954:_pr Scius, -a, -um (praecia, pretia): -a uitis, no* d*une sorte
50026:depretiS (tardif), depretiator ; manupretium : prix de la nain-d'oeuvre5
52746:et,Vg.Ae.4,131 rora retia). II s'agirait d'une racine *er»-, rS
53409:rete, -ls n.(souvent au pl .retia,-ium, d'ou un fdm.sg. retia et
53413:les mss. de Pl. ont le pl.n. retia, tan dis que Prisc. atteste retiam;
53418:un collectif neutre pl. retia d'ou proviendrait rete: filet, rfcts.
53421:retis et retia, M.1.7355. Celt.: britt.rwyd.
```


## [2026-09-05T20:37:55.850Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '52735,52760p' LAT.txt\necho \"======\"; sed -n '53405,53430p' LAT.txt",
 "description": "Print Ernout-Meillet rarus and rete"
}
```


### [2026-09-05T20:37:55.921Z] TOOL RESULT

```
rSrus, -a, -um: qui prisente des iatervalles ou des iaterstices
(.r. cribrum); clairsemi, espaci, poreux; et par suite "ipars 11 , d' oh
"iaoli" et "rare". S'oppose k dSnsus, cf. Vg,, G.3,337 rora sit {terra)
an supra morem si densa requiras; Coi. 3,9,6 rara seges; k solidus
(lucr.1,347, etc,). - Anci en (liv. Andr. ), usuel. Panroman (formes en
partis savantes), M.l.7067. Adverbe: rarS et rSre (Pl.Sud.9y5, cf.
Charis.3x7, malgri Aulu-Gelle 3,35,8).
Dirivis et coaposis: rSritSs (class.); raritudo (arch.); rSrescS,
-is; rSrBfaciS (luc.); r 5 renter (adv, arch. saas doute forai sur
frequenter) et rdriter (Gloss.); rdripilus (Coi.).
On a rapprochi rdtis, r&te (cf.Varr., L.1.5,130 rete a raritudine
et,Vg.Ae.4,131 rora retia). II s'agirait d'une racine *er»-, rS
"siparer" qui apparaitrait aussi daas lit.jri, i rti "se dissoudre,
tomberen ruines", drditi "se siparer", o rdjti "siparer", v.sl. oriti
"dissoudre»' ditruire", redikit "rare". Tout cela vague et ne four-
nissant avec les nqts latins aucun rapport qu'on puisse serrer de prbs.
rasis, -is f.: sorte de poix brute (Coi.).
rSster, -trum: v. rffdB.
ratis: v. reor.
ratis, -Is f.: non gaulois d'une sorte de fougbre (Marc.Enp.35) •
ratis, -is f.: asseablage de bois flottants; radeau; puis "ba-
teau k fond piat"; en poisie, substitut de nSuis. Cf.Varr., L.1.7,33:
ratis... ubi plu^es doli a«t asseres < iuncti aqua ducuntur • Bine
nauiculae cum remis ratariae dicuntur>. V. de Saint-Denis, Sens et
ivolution sdmaniique de ratis pn lat. class., Les fit. class. HV, 1948,
p.55 et s. - Anci en (Naev., Ean.). M.l.7088. Dirivis: ratitus, ipithbte
======
lit d' un cours d'eau (Gabius ap. Geli. 11, 17. ,4). De la derive un verbe
rStS,-as; cf.Gabius ibid. et Fest.336,35: retanda locantur Pomptina
fluminea i.e. purganda: retae enim uocantur arbores quae> ap<ud fluuios
eminent aut ex ipsis alueis extanty. Gemi.: holi.rete, reten.
rete, -ls n.(souvent au pl .retia,-ium, d'ou un fdm.sg. retia et
un n. sg. retium), retis, -ls f. et m. d'apros Priscien GLK II 3325,14
qui lit uuidum retem dans Pl.jRu.y425 [les mss. de Pl. ont rete],
984 (5 a rete, CD retem; au v. 985 rete nomin.n. est surj au y. 900
les mss. de Pl. ont le pl.n. retia, tan dis que Prisc. atteste retiam;
on lit dans Varron obiecto rete R.R.3,3,8 mais rete cannabina, ibid.
3,5, 11; Charisius GLK I 15 atteste hi retes (a c<Jt<? de in retes
meas), L' abi. est toujours rete (non reti)-, M.Niedermann suppose que
la flexion ancienne devait @tre retis m.sg. auquel correspondait
un collectif neutre pl. retia d'ou proviendrait rete: filet, rfcts.
Mot technique et populaire, de forme mal fix^e; peut-etre emprunte.
Ancien (Pl.), technique. Panroman, sauf roumain, sous les formesi
retis et retia, M.1.7355. Celt.: britt.rwyd.
Derives: reticulum ( reticulus m. Varr.; la Vulgate emploie retia¬
culum, qui s'est maintenu dans les dial-ectes italiens, M.L.7357,
cf. reteiaclSri, sous iaciB): petit filet (a provisionsj filet pour
les cheveux; cf.Rich, s.u.), M.L.7360; reticulStus : -m opus: mayonnerie
en forme de filet, cf.Rich, s.u.j retiolum (tardif; maintenu en
roman, M.L.7364); rUticirius: gladiateur arm<* du filet, r^tiaire;
circum, in-, ob-retiS,-is,-lui (-ii), -itum, -ire.
Certaines formes romanes supposent peut-etre aussi *retella, *retl-
cma, cf. M.L. s.u.
```


## [2026-09-05T20:38:15.953Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"== KLN rare adj ==\"; grep -n \"rare, adj\" KLN_1971.txt | head -3\necho \"== KLN retina ==\"; grep -n \"^retina, n\" KLN_1971.txt | head -3\necho \"== SKT rare/retina ==\"; grep -n \"Rare,\\|Retina\" SKT.txt | head -5\necho \"== MON arghandeh ==\"; grep -n \"ارغنده\\|ارغند\" MON_part1.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null | head -5",
 "description": "Grep Klein/Skeat/Moin"
}
```


### [2026-09-05T20:38:16.060Z] TOOL RESULT

```
== KLN rare adj ==
200276:rare, adj., thin. — F., fr. L. rarus , ‘thin, loose, 
200293:rare, adj., underdone. — ME. rere (whence also 
== KLN retina ==
205769:retina, n., the sensitive membrane at the back of 
== SKT rare/retina ==
== MON arghandeh ==
incoming/MON/MON_2vol_Adena_v1_djvu.txt:10101:ارغنده: 20220206 [- تِِ (ص.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:10103:آشفته و به خشم آمده» ارغند. 
MON_part1.txt:10101:ارغنده: 20220206 [- تِِ (ص.) 
MON_part1.txt:10103:آشفته و به خشم آمده» ارغند.
```


## [2026-09-05T20:38:19.307Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '200274,200292p' KLN_1971.txt\necho \"======\"; sed -n '205769,205782p' KLN_1971.txt\necho \"== MON ==\"; sed -n '10095,10108p' MON_part1.txt",
 "description": "Print Klein rare/retina and Moin arghandeh"
}
```


### [2026-09-05T20:38:19.408Z] TOOL RESULT

```
rara avis, a rare bird. — L., fr. rara, fern, of rarus, 
‘rare’, and avis, ‘bird’. See rare and aviary, 
rare, adj., thin. — F., fr. L. rarus , ‘thin, loose, 
rare’, which is cogn. with OI. %te, ‘besides, 
except’, nirrtih , ‘dissolution, decomposition’, 
viralah, ‘distant, tight, rare’, OSIav. oriti y ‘to 
dissolve, destroy’, Lith. yru , irti, ‘to dissolve’ 
(intr.), pairas , ‘loose’, OSIav. rediku, ‘rare’, Gk. 
ep7]pt.o<;, ‘solitary, isolated’, OI. ardhah , ‘part, 
side, half*, Lith. ardfti, ‘to cleave, separate’, 
erdvas, ‘wide’. All these words derive fr. I.-E. 
base *er- y *ere-, ‘to loose; to split, separate, be 
rare’. Gk. apai6<;, ‘thin, rare’, originally had 
initial digamma (f — w), hence cannot be cog- 
nate with the above words. L. rarus is possibly 
rel. to L. rete, ‘net’ ; see retiary. Cp. hermit and 
the first element in Ardhanari. 

Derivatives: rare , adv., rare-ly y adv., rare-ness y n. 
======
retina, n., the sensitive membrane at the back of 
the eyeball ( anat .) — Medical L. retina, coined 
by the translator Gerard of Cremona (11147- 
1187) fr. L. rete, ‘net’ (see retiary), as a loan 
translation of Hebrew resheth , ‘net’, used in 
Medieval Hebrew to denote the retina. See 
Joseph Hyrtl, Das Arabische und Hebraische in 
der Anatomie, p. 58, and his Onomatologia 
^\natomica, pp. 452-55. 

Derivative: retin-al, adj. 

retinaculum, n., a retaining band (anat., bot. and 
entomol .) — L. retinaculum , ‘a holdfast, band, 
== MON ==
زن‌ند. آوازی که با سودن انگشتان به 
یکدیگر برآورند سرای نشان دادن 
خوشحالی و شادمانی» بشکن؛ انگشتکك. 


۱۳ 
ارغنده: 20220206 [- تِِ (ص.) 
خشمگین» غضا کك» غضاان؛ - خشم آلود» 
آشفته و به خشم آمده» ارغند. 
ارغنون: 22207 (مسعر.) (ا.) (مس.) 
سازهایی ذوات‌الاوتار و سازهایی که از 
تعداد زیادی لوله تشکیل شده و هوارابا 
واسطه داخل 1 لوله‌ها دمند. سازی است 
که بونانیان و رومیان می‌نواختند» ارگ
```


## [2026-09-05T20:38:29.567Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,200p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T20:38:29.604Z] TOOL RESULT

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


## [2026-09-05T20:38:43.176Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"sich in Bewegung setzen, erregen\\|in Bewegung setzen, erregen\" WLD_Bd1_1930_dli_70244_djvu.txt | head -5\necho \"--- page markers near ---\"\ngrep -n \"^3\\. er-\\|^1\\. er-\\|^2\\. er-\" WLD_Bd1_1930_dli_70244_djvu.txt | head",
 "description": "Find WLD 3. er- entry"
}
```


### [2026-09-05T20:38:43.279Z] TOOL RESULT

```
8837:3. er- „sich in Bewegung setzen, erregen (auch seelisch, argern. reizen); 
--- page markers near ---
8768:1. er-, or- „Adler“ arm. gr. „(gro6erer) Yogel iiberhaupt“. 
8793:2. er- „Bock; Tier aus dem Schaf- oder Ziegengeschlecht 2 * * * * * * * * 11 . 
8837:3. er- „sich in Bewegung setzen, erregen (auch seelisch, argern. reizen);
```


## [2026-09-05T20:38:48.092Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\nsed -n '8837,8845p' WLD_Bd1_1930_dli_70244_djvu.txt\necho \"--- nearest page numbers ---\"\nawk 'NR<=8845 && /^[[:space:]]*1[0-9]{2}[[:space:]]*$/{print NR\": \"$0}' WLD_Bd1_1930_dli_70244_djvu.txt | tail -4\nawk 'NR<=9240 && /^[[:space:]]*1[0-9]{2}[[:space:]]*$/{print NR\": \"$0}' WLD_Bd1_1930_dli_70244_djvu.txt | tail -3\nawk 'NR<=9575 && /^[[:space:]]*1[0-9]{2}[[:space:]]*$/{print NR\": \"$0}' WLD_Bd1_1930_dli_70244_djvu.txt | tail -3",
 "description": "Get WLD page numbers"
}
```


### [2026-09-05T20:38:49.911Z] TOOL RESULT

```
3. er- „sich in Bewegung setzen, erregen (auch seelisch, argern. reizen); 
in die Hohe bringen (Erliebung, hochwachsen), z. T. aber auch von 
Bewegung nach abwarts." Basenformen er-, ere-, /„thematisch"), ere (?), 
erei-, creu-, eras (s. bes.). 

Zusammenfassungen bei Persson Wzerw. 25, 84, 102, 122, 232 und aus- 
fiihrlichst Beitr. 281 ff., 586, 636 ff., 666, 707 ff. 836 ff. 

Basi sformen er-, ere- (einsehlielilich paradigmatisch damit ver- 
--- nearest page numbers ---
8623: 133 
8684: 134 
8751: 135 
8820: 136 
9072: 140 
9136: 141 
9202: 142 
9400: 145 
9467: 146 
9533: 147
```


## [2026-09-05T20:39:05.706Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83er-' --note 'page 157, root Er 1/Or (PIE *h3er- to set in motion)'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81erg%CA%B0-' --note 'page 157, node 1 Ergh'\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C7%9Dr%C7%9Dgant-' --note 'page 157, Avestan ereghant node 2'",
 "description": "Fetch PIE reconstruction pages"
}
```


### [2026-09-05T20:39:08.418Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/74fc390769b5e5e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ab5c485efc00275.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e7cf25d372beabc2.txt
```


## [2026-09-05T20:39:11.273Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 74fc390769b5e5e7 3ab5c485efc00275 e7cf25d372beabc2; do echo \"=== $f ===\"; sed -n '1,6p' $f.txt; done",
 "description": "Check reconstruction archives"
}
```


### [2026-09-05T20:39:12.755Z] TOOL RESULT

```
=== 74fc390769b5e5e7 ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83er-
FETCHED: 2026-09-05T20:33:48Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/h₃er- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/h₃er- - Wiktionary, the free dictionary 
=== 3ab5c485efc00275 ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%81erg%CA%B0-
FETCHED: 2026-09-05T20:39:07Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found=== e7cf25d372beabc2 ===
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/%C7%9Dr%C7%9Dgant-
FETCHED: 2026-09-05T20:39:08Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-05T20:39:15.670Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -n -A8 \"^ Etymology\" 74fc390769b5e5e7.txt | head -25\ngrep -n -i \"root\\b\" 74fc390769b5e5e7.txt | head -8",
 "description": "Read h3er- page"
}
```


### [2026-09-05T20:39:15.729Z] TOOL RESULT

```
62: Root 
143: Root
176: Terms derived from the Proto-Indo-European root *h₃er- (86 c, 0 e) 
178: *h₃r̥tó ~ *h₃rn̥tó ( mediopassive athematic root aorist )
```


## [2026-09-05T20:39:18.469Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '140,175p' 74fc390769b5e5e7.txt",
 "description": "Print h3er- root section"
}
```


### [2026-09-05T20:39:18.511Z] TOOL RESULT

```
 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *h₃er- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 

 to move , to stir 

 to rise , to spring 

 Extensions
 [ edit ] 

 *h₃er-dʰ- 

 *h₃r-ey-H- 

 *h₃r-ew- 

 Descendants
 [ edit ] 

 Proto-Tocharian: *er- ( “ to evoke, bring forth, produce ” ) [ 4 ] 
 Tocharian A: ar- 

 Tocharian B: er- 

 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: ऋ ( ṛ ) , अर् ( ar ) , इर् ( ir ) , ईर् ( īr ) 

 Derived terms
 [ edit ]
```


## [2026-09-05T20:40:29.314Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:50:37.914Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk157.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io, os\n\nW_H3ER = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83er-\"\nW_ORKH = \"https://en.wiktionary.org/wiki/%E1%BD%80%CF%81%CF%87%CE%AD%CE%BF%CE%BC%CE%B1%CE%B9\"\nW_ARG  = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%D8%BA%D9%86%D8%AF\"\nW_ORK  = \"https://en.wiktionary.org/wiki/%D8%A7%D8%B1%DA%A9%D8%B3%D8%AA%D8%B1\"\nW_RARUS= \"https://en.wiktionary.org/wiki/rarus\"\nW_RETE = \"https://en.wiktionary.org/wiki/rete\"\nE_ORCH = \"https://www.etymonline.com/word/orchestra\"\nE_RET  = \"https://www.etymonline.com/word/retina\"\nE_RARE = \"https://www.etymonline.com/word/rare\"\n\ndoc = {\n \"pdf_page\": 157,\n \"book_page\": 127,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Er 1, Or\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₃er- (Pokorny '3. er- : or- : ŕ-') 'to set (oneself) in motion, stir, rouse; raise up'\",\n   \"note\": \"Pokorny IEW 326-332 heads the entry '3. er- : or- : ŕ-, ursprünglich athematische Wurzel mit terminativem Aspekt: „sich in Bewegung setzen, erregen (auch seelisch, ärgern, reizen); in die Höhe bringen (Erhebung, hochwachsen), z. T. auch von Bewegung nach abwärts“', and the page Nourai cites (327) is the second page of that article (the Indo-Iranian material: ai. iyarti, av. ar- 'sich in Bewegung setzen'). So the root name (Er / Or, i.e. the e- and o-grades), the language label and the gloss 'to set in motion, excite' are all an accurate short rendering of Pokorny. Walde-Pokorny I 136 has the identical wording; Watkins/AHD lists 'er-¹. To set in motion' and closes it '[Pok. 3. er- 326; ergh- 339.]', i.e. AHD itself files the Ergh branch of this chart under this same root, exactly as Nourai draws it. Wiktionary reconstructs *h₃er- 'to move, to stir; to rise, to spring'. 'PART 2' marks the continuation of a chart begun on the preceding page.\",\n   \"note_fa\": \"ریشهٔ نمودار همان ریشهٔ هندواروپایی آغازین *h₃er- «به جنبش درآوردن، برانگیختن، برخاستن» است. پوکورنی در صفحات ۳۲۶ـ۳۳۲ آن را «در جنبش آمدن، برانگیختن (و نیز خشمگین کردن)، بالا بردن» معنی کرده و صفحهٔ ۳۲۷ که نورایی بدان ارجاع داده همان صفحهٔ مواد هندوایرانی (سنسکریت iyarti، اوستایی ar-) است. والدهـپوکورنی (جلد ۱، ص ۱۳۶) و واتکینز در پیوست فرهنگ آمریکن هریتیج نیز همین را می‌گویند؛ خود واتکینز شاخهٔ ergh- را زیر همین ریشه می‌آورد، درست همان‌گونه که نورایی رسم کرده است. بنابراین جعبهٔ ریشه، برچسب زبان و معنای آن درست است و ادعای نورایی پذیرفتنی است.\",\n   \"sources\": [W_H3ER],\n   \"ref_check\": [\n    {\"ref\": \"POK:327\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt, form-feed page 339 (printed p. 326-327; grep -n 'in Bewegung setzen, erregen'): '3. er- : or- : ŕ-, ursprünglich athematische Wurzel mit terminativem Aspekt: „sich in Bewegung setzen, erregen (auch seelisch, ärgern, reizen); in die Höhe bringen …“'; p. 327 carries 'av. ar- „(sich) in Bewegung setzen, hingelangen“'. Exactly the root box as drawn.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 136 (WLD_Bd1_1930 djvu line 8837)\", \"stance\": \"supports\",\n     \"note\": \"'3. er- „sich in Bewegung setzen, erregen (auch seelisch, ärgern, reizen); in die Höhe bringen (Erhebung, hochwachsen), z. T. aber auch von Bewegung nach abwärts.“ Basenformen er-, ere-, … erei-, ereu-' — the source Pokorny 326 abridges.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, e-list (AHD_watkins1985.txt line 448-450)\", \"stance\": \"supports\",\n     \"note\": \"'er-¹. To set in motion. … 3. Suffixed form *or-yo- in Latin oriri, to arise, appear, be born: ORIENT, ORIGIN … [Pok. 3. er- 326; ergh- 339.]' — Watkins gives this root the same gloss and expressly attaches ergh- 339 to it.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, e-/o- sections (grep 'ergh', 'oreiO' in IEC.txt)\", \"stance\": \"silent\",\n     \"note\": \"Mann has bhergh-, dergh-, dorgheið etc. but no *er-/*ergh- 'set in motion' headword; his silence is not a disagreement.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Indo-European\", \"words\": \"Ergh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Pokorny IEW 339 has the entry verbatim: 'ergh- „schütteln, erregen, beben“ od. dgl., wohl Erweiterung von er- „in Bewegung setzen“', with Skt. ṛghāyati 'bebt, tost, stürmt' and Gk. ὀρχέομαι as its two certain members. Nourai's arrow Er → Ergh is therefore not his own construction but Pokorny's own statement that *ergh- is the gh-enlargement of *er-, and his gloss 'to excite, tremble' renders 'erregen, beben' exactly. Watkins/AHD keeps the same root label but glosses it 'to mount' because he merges Pokorny's ergh- 339 with Pokorny's orghi- 782 'testicle'; the form and the Pokorny page are unaffected.\",\n     \"derivation_fa\": \"پوکورنی در صفحهٔ ۳۳۹ دقیقاً همین مدخل را دارد: «ergh- „تکان دادن، برانگیختن، لرزیدن“، ظاهراً گسترشی از er- „به جنبش درآوردن“»، با دو گواه قطعی: سنسکریت ṛghāyati «می‌لرزد، می‌خروشد» و یونانی ὀρχέομαι. پس پیکانی که نورایی از Er به Ergh کشیده، سخن خود پوکورنی است و معنای «برانگیختن، لرزیدن» نیز برگردان دقیق همان است. واتکینز همین ریشه را «برآمدن، سوار شدن» معنی کرده، زیرا آن را با ریشهٔ دیگری (orghi- «خایه»، پوکورنی ۷۸۲) یکی گرفته است؛ این اختلاف به درستی صورت و ارجاع آسیبی نمی‌زند. ادعای نورایی درست است.\",\n     \"sources\": [W_ORKH],\n     \"ref_check\": [\n      {\"ref\": \"POK:339\", \"status\": \"supports\",\n       \"note\": \"POK_01.txt, form-feed page 353 (printed p. 339): 'ergh- „schütteln, erregen, beben“ od. dgl., wohl Erweiterung von er- „in Bewegung setzen“. Ai. ṛghāyati „bebt, tost, stürmt“; gr. ὀρχέω „πάλλω, κινέω“, meist ὀρχέομαι „tanze, hüpfe, springe, bebe“.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 147 (WLD_Bd1_1930 djvu line 9572)\", \"stance\": \"supports\",\n       \"note\": \"'ergh- „schütteln, erregen, beben“ oder dgl., wohl Erw. von er- „in Bewegung setzen“. Ai. ṛghayati „bebt, tost, stürmt“; gr. ὀρχέω …' — identical to the Pokorny page Nourai cites.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt line 454)\", \"stance\": \"partial\",\n       \"note\": \"'ergh-. To mount. 1. … *orgh-i- in Greek orkhis, testicle: ORCHID. 2. … *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]' — same root, but glossed 'to mount' because Watkins merges two Pokorny lemmata.\"},\n      {\"src\": \"IEC\", \"where\": \"Mann (grep 'ergh' in IEC.txt)\", \"stance\": \"silent\",\n       \"note\": \"no *ergh- headword in Mann; only bherghos, derghó, dorgheið and the like.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Avestan\", \"words\": \"ereğant\", \"verdict\": \"plausible\",\n     \"derivation\": \"The word is real: Young Avestan ərəγaṇt- (fem. ərəγaiṇtī-), which Bartholomae, Altiranisches Wörterbuch (col. ~350, between the col. 346 and 351 markers of the scan) glosses 'entsetzlich, abscheulich' and cites only as an epithet (a) of hell — 'bunəm aṇku̱m təmaŋhahe yat ərəγatō daŏzaŋhahe' V. 3.7, Yt. 18.44 — and (b) of flies, 'baivařə maxs̃inąm ərəγainēnąm' V. 14.6, 'maxs̃i.kəhrpa ərəγaitya' V. 7.2. Nourai's rendering 'angry, evil' is a fair translation of 'entsetzlich, abscheulich' and matches Pokorny's own 'arg, abscheulich'. What is not certain is the arrow: Pokorny prints the Avestan only under a hedge — 'Wegen der in 3. er- ebenfalls vorliegenden Bed. „arg“ u. dgl. können dazu in Beziehung stehen: av. ərəγant- „arg, abscheulich“' — and Bartholomae himself writes only 'Et.?' and refers the reader to Hübschmann. Hübschmann, Persische Studien 13 (no. 72) states the problem in full: the connection works if ərəγaṇt- means 'zornig, gierig', which is possible since it qualifies hell and the fly, but 'übersetzt man ərəγant- mit Bartholomae durch „finster“, so gehören die Wörter wegen der Bedeutungsverschiedenheit nicht zusammen … sicher steht die Bedeutung von zd. ərəγant- jedenfalls noch nicht'. Hence plausible, not confirmed: right word, right language, defensible gloss, but the link to *ergh- rests on a semantic guess.\",\n     \"derivation_fa\": \"این واژه واقعی است: اوستایی متأخر ərəγaṇt- (مؤنث ərəγaiṇtī-) که بارتولومه در فرهنگ ایرانی باستان (ستون حدود ۳۵۰) آن را «هولناک، زشت و مکروه» معنی کرده و تنها دو کاربرد برایش آورده است: صفت دوزخ (ویدیوداد ۳٫۷، یشت ۱۸٫۴۴) و صفت مگس (ویدیوداد ۷٫۲ و ۱۴٫۶). پس برگردان نورایی («خشمگین، بد») با معنای بارتولومه و پوکورنی می‌خواند. آنچه قطعی نیست خود پیوند این واژه با ریشهٔ *ergh- است: پوکورنی آن را فقط با احتیاط («می‌تواند مربوط باشد») می‌آورد، بارتولومه زیر آن فقط می‌نویسد «ریشه؟» و خواننده را به هوبشمان حواله می‌دهد، و هوبشمان (مطالعات فارسی، ص ۱۳، شمارهٔ ۷۲) صریح می‌گوید اگر معنای واژه «خشمگین، آزمند» باشد پیوند درست است، اما اگر معنای دیگری که خود بارتولومه پیش‌تر داده بود («تاریک») درست باشد، دو واژه به هم نمی‌خورند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_ARG],\n     \"ref_check\": [\n      {\"ref\": \"POK:339\", \"status\": \"partial\",\n       \"note\": \"POK_01.txt page 339 does list 'av. ərəγant- „arg, abscheulich“', but only after the caveat 'Wegen der in 3. er- ebenfalls vorliegenden Bed. „arg“ u. dgl. können dazu in Beziehung stehen' — a possibility, not the flat derivation the chart's arrow asserts.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. ~350 (BRT.txt line 7633)\", \"stance\": \"partial\",\n       \"note\": \"'j. ərəγ-ant- Adj. (fem. °γaiṫī-) „entsetzlich, abscheulich“; a) von der Hölle … b) von Fliegen: baivařə maxs̃inąm °γainēnąm V.14.6 … Et.? Vgl. Hbm. PSt. 13.' — confirms form and gloss, leaves the etymology open.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 13, no. 72 (HUB.txt line 345)\", \"stance\": \"partial\",\n       \"note\": \"'Np. arγand „zornig, gierig“ kann zu zd. ərəγant- gestellt werden, wenn man diesem die Bedeutung „zornig, gierig“ beilegt, was möglich ist, da es Beiwort der Hölle und der Fliege ist. Übersetzt man ərəγant- mit Bartholomae durch „finster“, so gehören die Wörter … nicht zusammen.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 147\", \"stance\": \"partial\",\n       \"note\": \"'Wegen der in er- ebenfalls vorliegenden Bed. „arg“ u. dgl. können dazu in Beziehung stehen av. ərəγant- „arg, abscheulich“ (Hübschmann Pers. St. 13)' — same hedge as Pokorny, with the source named.\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"Persian\", \"words\": \"arğandeh\", \"verdict\": \"confirmed\",\n     \"derivation\": \"NP ارغند arγand / ارغنده arγanda 'wrathful, fierce, warlike' continues Av. ərəγaṇt- through a Middle Persian *arγand: Horn, Grundriss no. 72, gives the chain 'erγend, erγende „zornig, gierig“ (S̃āhn., Mohl V, 122), aw. ərəγant- …; phlv. argand', and Wiktionary spells the Pahlavi out as ʾ lgnd /arγand/. Phonetically the Old Iranian present-participle suffix -aṇt- gives MP/NP -and (cf. MP darē/darwand type), the Avestan cluster γ is kept as Persian غ, and the final -a of ارغنده is the ordinary NP adjectival -a (< MP -ag) added to the participle; the third variant آرغده ārγada shows loss of the nasal plus lengthening of the first vowel. Nourai's own source is right at the point: Borhan-e Qateʿ p. 32 s.v. آرغده 'بمعنی غضبناک و خشمگین و قهرآلود - و جنگاور باشد - و بفتح ثالث حریص در چیزها را گویند' — note that the same entry already carries the 'greedy' sense that reappears in the Sogdian cognate (node 4). The Daqiqi hemistich the chart quotes ('چو ارغنده گرگ', from the Goshtasp section embedded in the Shahnameh) attests the word in the 10th century. Mo'in's etymological footnote in the same volume, at ارغنده, states the derivation and warns that the older Persian dictionaries' gloss 'دلیر و شجاع' is wrong.\",\n     \"derivation_fa\": \"«ارغند / ارغنده / آرغده» دنبالهٔ اوستایی ərəγaṇt- است که از راه فارسی میانهٔ arγand (پهلوی ʾargand، به نوشتهٔ هرن در شمارهٔ ۷۲ و ویکی‌واژه) به فارسی نو رسیده است. پسوند اسم فاعلی ایرانی باستان -aṇt- در فارسی به -ند بدل شده، غـی اوستایی دست‌نخورده مانده، و هــــــ پایانی در «ارغنده» همان پسوند صفتی ـه (< فارسی میانه -ag) است؛ صورت «آرغده» نیز افتادن نون و کشیده شدن واکهٔ نخست را نشان می‌دهد. مأخذی که نورایی آورده دقیقاً بر سر جاست: برهان قاطع ص ۳۲ ذیل «آرغده»: «بمعنی غضبناک و خشمگین و قهرآلود ـ و جنگاور باشد ـ و بفتح ثالث حریص در چیزها را گویند» — همین معنای دوم (حریص) در هم‌ریشهٔ سغدی آن نیز دیده می‌شود. بیت دقیقی («چو ارغنده گرگ») گواهی سدهٔ چهارم است. معین در حاشیهٔ برهان ذیل «ارغنده» همین ریشه را می‌آورد و می‌افزاید که معنای «دلیر و شجاع» که فرهنگ‌های فارسی داده‌اند درست نیست. ادعای نورایی درست است.\",\n     \"sources\": [W_ARG],\n     \"ref_check\": [\n      {\"ref\": \"BQT:32\", \"status\": \"supports\",\n       \"note\": \"Borhan-e Qateʿ vol. 1, printed p. 32 (BQT_v1_pages.txt form-feed leaf 242; the following leaf carries the footnote 'بقیه از صفحهٔ ۳۲'): 'آرغده ـ بضم ثالث بر وزن آزرده، بمعنی غضبناک و خشمگین و قهرآلود - و جنگاور باشد - و بفتح ثالث حریص در چیزها را گویند'. Mo'in's etymological footnote at ارغنده in the same volume (BQT_v1.txt line 20397) reads 'در اوستا ərəγant ، در فارسی ارغند و ارغنده و آرغده بمعنی خشمگین … بنابراین ارغند و ارغنده را که در فرهنگهای فارسی بمعنی دلیر و شجاع گرفته‌اند، درست نیست'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"Grundriss no. 72, p. 22 (HRN.txt line 1084)\", \"stance\": \"supports\",\n       \"note\": \"'72. erγend, erγende „zornig, gierig“ (S̃ahn., Mohl, V, 122), aw. ərəγant- „finster“ (Bartholomae, Handbuch 220, Geldner, Drei Yasht 27); phlv. argand [argund ist wohl nur verschrieben]; ai. vergl. rājas-.' — the Avestan → Pahlavi → NP chain of the chart, with the Middle Persian link added.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. ارغنده (MON_part1.txt line 10101)\", \"stance\": \"supports\",\n       \"note\": \"'ارغنده: […] (ص.) خشمگین، غضبناک، غضبان؛ خشم‌آلود، آشفته و به خشم آمده، ارغند.' — same gloss as the chart, with a bracketed Pahlavi origin tag.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 13, no. 72\", \"stance\": \"partial\",\n       \"note\": \"accepts 'Np. arγand „zornig, gierig“ kann zu zd. ərəγant- gestellt werden' but makes it conditional on the Avestan gloss.\"},\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dict. (grep 'argand')\", \"stance\": \"silent\",\n       \"note\": \"MacKenzie has no argand entry (his p- and a- lists give pargandan, ahlaw etc. but not argand); the Pahlavi form is known from Horn and from the Book-Pahlavi spelling ʾargand cited by Wiktionary, not from MacKenzie.\"}\n     ]\n    },\n    {\n     \"id\": 4, \"lang\": \"Sogdian\", \"words\": \"`rğnt\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Gharib's Sogdian Dictionary entry no. 1446, on printed p. 57, reads 'ʾrynʾt B — arγand ©Av. ərəγant- ⇒ʾryʾnt — greedy — TSP 2.235 n p172; Hen. Texts. 734; Bailey. Asica. 5', i.e. Buddhist Sogdian ʾRΓʾ NT / ʾRΓNT arγand 'greedy', which Gharib herself derives from Av. ərəγant-. Nourai's '`rγnt' is the defective spelling of the same word (aleph for the initial ā/a, no mater for the internal a). Sogdian and Persian are thus two parallel continuations of Old Iranian *arγant-, and the Sogdian sense 'greedy' matches the secondary Persian sense that Borhan-e Qateʿ records for the same word ('بفتح ثالث حریص در چیزها'), and matches Hübschmann's 'zornig, gierig' — which is in fact the best evidence that the Avestan word did mean something like 'raging, greedy' rather than 'dark'. The chart's arrow runs Ergh → Sogdian directly, skipping the Avestan/Old Iranian node, but that is only a drawing shortcut.\",\n     \"derivation_fa\": \"قریب در فرهنگ سغدی، مدخل شمارهٔ ۱۴۴۶ در صفحهٔ ۵۷، می‌آورد: «ʾRΓʾNT (سغدی بودایی) arγand، از اوستایی ərəγant-، به معنای آزمند/حریص» با ارجاع به TSP، هنینگ و بیلی. صورتی که نورایی نوشته (`rγnt) همان املای کوتاه‌نویسی همین واژه است. پس سغدی arγand و فارسی ارغند دو بازماندهٔ موازی از ایرانی باستان *arγant- اند، و معنای سغدی «آزمند» دقیقاً با معنای دومی که برهان قاطع برای آرغده می‌آورد («حریص در چیزها») می‌خواند — و همین بهترین قرینه برای آن است که واژهٔ اوستایی معنای «خشمگین/آزمند» داشته نه «تاریک». ادعای نورایی درست است؛ تنها پیکان نمودار گره ایرانی باستان را نادیده گرفته است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"SOD:57\", \"status\": \"supports\",\n       \"note\": \"Gharib, Sogdian Dictionary, printed p. 57 = SOD_pages.txt form-feed leaf 122 (leaf − 65 = printed page; the neighbouring leaves are marked 58 and 59), entry '1446 ʾryʾnt B — arγand ©Av. ərəγant — greedy — TSP 2.235 n p172; Hen. Texts. 734; Bailey. Asica. 5'. Nourai's page number is a page, not an entry number (entry 57 is ʾδy).\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"SOD\", \"where\": \"no. 1446, p. 57\", \"stance\": \"supports\",\n       \"note\": \"'arγand ©Av. ərəγant — greedy' — the source explicitly gives the Avestan etymon, as the chart does.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 13, no. 72\", \"stance\": \"supports\",\n       \"note\": \"'zornig, gierig' is exactly Hübschmann's gloss for the Iranian word, and he argues the whole family hangs on that sense; the Sogdian 'greedy' bears him out.\"},\n      {\"src\": \"BRT\", \"where\": \"Altiran. Wb. col. ~350\", \"stance\": \"partial\",\n       \"note\": \"gives the Avestan etymon ərəγant- 'entsetzlich, abscheulich' but says nothing about Sogdian (the AiW predates the Sogdian finds).\"}\n     ]\n    },\n    {\n     \"id\": 5, \"lang\": \"Greek\", \"words\": \"orğ-eyo, orxeisthai\", \"verdict\": \"plausible\",\n     \"derivation\": \"Two forms are in one box and only the second is Greek. 'orγ-eyo' is Watkins' reconstruction *orgh-eyo-, the suffixed o-grade of *ergh-, copied straight out of the AHD appendix that Nourai cites: 'ergh-. To mount. … 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA.' The second, ὀρχεῖσθαι (present ὀρχέομαι) 'to dance, leap', is a real Homeric verb, and Pokorny 339 lists it under ergh- beside Skt. ṛghāyati, glossing 'tanze, hüpfe, springe, bebe'; Klein s.v. orchestra repeats the same derivation ('cogn. with OI. ṛghāyati … fr. I.-E. base *ergh-, which is prob. an enlargement of base *er-, *or- “to set in motion”'), which is the whole of Nourai's chart in one sentence. But this is contested: Frisk and Beekes take ὀρχέομαι as an iterative-intensive of ἔρχομαι 'to come, go'; Wiktionary calls Watkins' link with ὄρχις 'testicle' 'semantically tenuous' and offers *h₃erǵʰ- 'to copulate; ardent' (with PGmc *argaz) instead; Etymonline warns 'not all experts accept that (see Beekes)'. Hence plausible: the Greek word and its 'dance' sense are certain, the *ergh- attachment is one of three live options, and the first 'word' in the box is a proto-form, not Greek.\",\n     \"derivation_fa\": \"در این جعبه دو صورت آمده و تنها دومی یونانی است. «orγ-eyo» همان بازسازی *orgh-eyo- واتکینز (صورت پایهٔ o از *ergh-) است که نورایی عیناً از پیوست فرهنگ آمریکن هریتیج برداشته، نه واژه‌ای یونانی. دومی، ὀρχεῖσθαι (حال: ὀρχέομαι) «رقصیدن، جستن»، واژه‌ای هومری و اصیل است و پوکورنی در ص ۳۳۹ آن را در کنار سنسکریت ṛghāyati زیر ergh- می‌آورد؛ کلاین نیز ذیل orchestra همین زنجیره را می‌آورد. اما این ریشه‌شناسی اجماعی نیست: فریسک و بیکس ὀρχέομαι را صورت تکراریـتأکیدی ἔρχομαι «آمدن، رفتن» می‌دانند و ویکی‌واژه پیوند واتکینز با ὄρχις «خایه» را از نظر معنایی سست می‌خواند. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_ORKH, E_ORCH],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 454: 'ergh-. To mount. 1. Suffixed o-grade form *orgh-i- in Greek orkhis, testicle: ORCHID. 2. Suffixed o-grade form *orgh-eyo- in Greek orkheisthai, to dance: ORCHESTRA. [Pok. orghi- 782, ergh- 339.]' — both of Nourai's forms come from this line.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 339 s.v. ergh-\", \"stance\": \"supports\",\n       \"note\": \"'gr. ὀρχέω „πάλλω, κινέω“, meist ὀρχέομαι „tanze, hüpfe, springe, bebe“.'\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. orchestra (KLN_1971.txt line 168329)\", \"stance\": \"supports\",\n       \"note\": \"'… from the stem of ὀρχεῖσθαι, “to dance”, which is cogn. with OI. ṛghāyati, “trembles, rages, raves”, fr. I.-E. base *ergh-, which is prob. an enlargement of base *er-, *or “to set in motion”' — Nourai's whole chart in one sentence.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 147\", \"stance\": \"supports\",\n       \"note\": \"'gr. ὀρχέω … meist ὀρχέομαι „tanze, hüpfe, springe, bebe“. Lit. bei Boisacq s. v.'\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. Orchestra (SKT.txt line 12841)\", \"stance\": \"supports\",\n       \"note\": \"'Gk. ὀρχήστρα, an orchestra; which, in the Attic theatre, was a space on which the chorus danced. — Gk. ὀρχέομαι, I dance.'\"}\n     ]\n    },\n    {\n     \"id\": 6, \"lang\": \"French\", \"words\": \"orchestre\", \"verdict\": \"confirmed\",\n     \"derivation\": \"Pass-through node with no reference in the book. French orchestre is a learned 16th-century borrowing of Latin orchestra, which is Greek ὀρχήστρα, 'the semicircular space where the chorus danced' — formed on the stem of ὀρχεῖσθαι with the place-forming suffix -τρα (Klein: '… formed with -τρα, a suff. denoting place, from the stem of ὀρχεῖσθαι'). In French, as in English, the sense moved from the place in the ancient theatre to the pit in front of the modern stage and then, in the 18th century, by metonymy, to the body of musicians who sit there — the meaning in which the word was re-exported to Persian (node 7). The chart's Greek → French arrow is right in substance but passes silently through Latin.\",\n     \"derivation_fa\": \"این گره در کتاب مأخذی ندارد. فرانسهٔ orchestre وام‌واژه‌ای عالمانه از لاتین orchestra است که خود از یونانی ὀρχήστρα «جایگاه نیم‌دایره‌ای رقص دستهٔ همسرایان» می‌آید؛ ساخته از ستاک ὀρχεῖσθαι و پسوند مکانی -τρα (کلاین). در فرانسه معنا نخست از «جایگاه تالار باستانی» به «گودی پیش صحنه» و سپس در سدهٔ ۱۸م به مجاز، به «گروه نوازندگان» تحول یافت و به همین معنا به فارسی راه یافت. پیکان نمودار درست است، جز آنکه حلقهٔ لاتین را نیاورده است.\",\n     \"sources\": [E_ORCH],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the chart gives no reference for this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. orchestra (KLN_1971.txt line 168329)\", \"stance\": \"supports\",\n       \"note\": \"'L. orchestra, fr. Gk. ὀρχήστρα, “place in the theater in which the chorus danced”, lit. “place for dancing”, formed with -τρα, a suff. denoting place, from the stem of ὀρχεῖσθαι, “to dance”.'\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. Orchestra\", \"stance\": \"supports\",\n       \"note\": \"'Gk. ὀρχήστρα … a space on which the chorus danced' — same route, Greek via Latin into the modern languages.\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/orchestra (archived)\", \"stance\": \"supports\",\n       \"note\": \"'c. 1600, “area in an ancient theater for the chorus,” from Latin orchestra, from Greek orkhēstra … Meaning “group of musicians…” is recorded by 1720'.\"}\n     ]\n    },\n    {\n     \"id\": 7, \"lang\": \"Persian\", \"words\": \"orkestr\", \"verdict\": \"confirmed\",\n     \"derivation\": \"ارکستر orkestr is a 20th-century Persian loan directly from French orchestre, not from English: French -ch- is [k], and the French final -re is dropped, giving the Persian cluster -str, whereas an English source would have yielded *ارکسترا. Mo'in's Farhang-e Farsi marks the headword with the origin tag [فر.] 'French' and defines it 'در یونان قدیم نوازندگان و خوانندگان در جلو صحنه. گروه نوازندگان با مجموعهٔ سازها …', i.e. it records both the ancient-Greek sense and the modern one. Wiktionary: 'ارکستر: Borrowed from French orchestre.' So this is a round-trip of sorts: a Greek word whose root the chart traces back to an Indo-Iranian family that also produced Persian ارغنده (node 3) re-enters Persian 2,500 years later through Paris.\",\n     \"derivation_fa\": \"«ارکستر» وام‌واژه‌ای سدهٔ چهاردهم خورشیدی از فرانسهٔ orchestre است و نه از انگلیسی: در فرانسه ch به صورت [k] خوانده می‌شود و e پایانی خوانده نمی‌شود، پس خوشهٔ پایانی ـستر پدید می‌آید؛ اگر از انگلیسی گرفته شده بود «ارکسترا» می‌شد. معین در فرهنگ فارسی این مدخل را با نشانهٔ [فر.] می‌آورد و هر دو معنای یونانی کهن و امروزین را ثبت کرده است؛ ویکی‌واژه نیز می‌نویسد «وام‌گرفته از فرانسهٔ orchestre». شمارهٔ صفحهٔ معین (۲۰۵) را نمی‌توان از روی نسخهٔ برخط سنجید، اما متن مدخل با ادعای نورایی یکی است. ادعای نورایی درست است.\",\n     \"sources\": [W_ORK],\n     \"ref_check\": [\n      {\"ref\": \"MON:205\", \"status\": \"partial\",\n       \"note\": \"the entry itself is there — MON_part1.txt line 10177: 'ارکستر: [فر.] (ا.) (مس.) در یونان قدیم نوازندگان و خوانندگان در جلو صحنه. گروه نوازندگان با مجموعهٔ سازها …', with the French origin tag — but the page number cannot be checked: the only digitised Mo'in is the 2-volume Adena abridgement, whose pagination differs from the 6-volume Amir Kabir edition Nourai cites, and vajehyab/abadis give no page numbers.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. ارکستر (MON_part1.txt line 10177)\", \"stance\": \"supports\",\n       \"note\": \"'ارکستر: [فر.] … گروه نوازندگان با مجموعهٔ سازها که با همکاری یک قطعهٔ موسیقی را اجرا کنند' — French tag, exactly the chart's route.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ارکستر (archived)\", \"stance\": \"supports\",\n       \"note\": \"'Etymology: Borrowed from French orchestre.'\"}\n     ]\n    },\n    {\n     \"id\": 8, \"lang\": \"English\", \"words\": \"orchestra\", \"verdict\": \"confirmed\",\n     \"derivation\": \"English orchestra is first recorded c. 1600 in the antiquarian sense 'the area in an ancient theatre where the chorus performed', taken from Latin orchestra (which in Rome had meant the block of seats reserved for senators), itself from Greek ὀρχήστρα. The modern sense 'body of instrumental musicians' is 1720, from the part of the theatre they occupy in front of the stage (1768 in English for that space). Watkins/AHD, the reference Nourai cites, lists ORCHESTRA under ergh-, and Klein gives the same chain; Skeat likewise. Nourai's Greek → English arrow is correct in substance, the Latin stage being implicit.\",\n     \"derivation_fa\": \"واژهٔ انگلیسی orchestra نخست در حدود ۱۶۰۰ میلادی به معنای «محل دستهٔ همسرایان در تأتر باستان» به کار رفته، وام‌گرفته از لاتین orchestra و آن از یونانی ὀρχήστρα. معنای امروزین (گروه نوازندگان) از ۱۷۲۰ به مجاز محلیت پدید آمده است. همان مأخذی که نورایی آورده (پیوست واتکینز) ORCHESTRA را زیر ergh- می‌آورد و کلاین و اسکیت نیز همین زنجیره را می‌دهند. ادعای نورایی درست است؛ حلقهٔ لاتین در نمودار مسکوت مانده است.\",\n     \"sources\": [E_ORCH],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 454, ergh- §2: '… in Greek orkheisthai, to dance: ORCHESTRA.' The English headword is listed under this root in Watkins' index.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. orchestra (KLN_1971.txt line 168329)\", \"stance\": \"supports\",\n       \"note\": \"'orchestra, n., 1) in the Greek theater, the place where the chorus danced; 2) in the modern theater, the space between the stage and auditorium, reserved for the musicians. — L. orchestra, fr. Gk. ὀρχήστρα …'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/orchestra (archived)\", \"stance\": \"supports\",\n       \"note\": \"'c. 1600 … from Latin orchestra, from Greek orkhēstra … Meaning “group of musicians performing at a concert, opera, etc.” is recorded by 1720'.\"},\n      {\"src\": \"SKT\", \"where\": \"s.v. Orchestra\", \"stance\": \"supports\",\n       \"note\": \"'Gk. ὀρχήστρα … — Gk. ὀρχέομαι, I dance.'\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 3,\n   \"root\": \"Ere 1, Re, Er 2\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *h₁erh₁- / Pokorny '5. er-, set-Basis erə-, thematisch (e)r-e-' 'loose, sparse, standing apart; to come apart, separate'\",\n   \"note\": \"Pokorny IEW 332-333 heads the entry '5. er-, ers-, thematisch (e)r-e- „locker, undicht, abstehend; auseinandergehen, auftrennen“' — the article begins on p. 332, exactly the page Nourai cites — and Walde-Pokorny I 142 f. has the same wording. Watkins/AHD gives it as 'erə-². To separate. Variant *rē-, contracted from *reə- … [Pok. 5. er- 332.]', which is where Nourai's triple heading 'Ere 1, Re, Er 2' comes from: Ere = erə-, Re = the variant *rē-, Er 2 = Pokorny's numbered 'er-'. His gloss 'to split, loosen' is a fair short rendering of 'auftrennen … locker, undicht'. Klein s.v. rare summarises the same family ('I.-E. base *er-, *ere-, “to loose; to split, separate, be rare”') and, importantly for node 1, includes OI. ardhah 'part, side, half' in it. Root box, language label and gloss are all correct.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است. پوکورنی در صفحات ۳۳۲ـ۳۳۳ مدخلی دارد با عنوان «۵. er-، با پایهٔ کشیدهٔ erə- و صورت (e)r-e-: سست، تنک، از هم جدا؛ از هم گسیختن، گشودن» و آغاز مدخل دقیقاً در همان صفحهٔ ۳۳۲ است که نورایی آورده؛ والدهـپوکورنی جلد ۱ ص ۱۴۲ نیز همین را دارد. نام سه‌گانهٔ «Ere 1, Re, Er 2» از پیوست واتکینز گرفته شده که می‌نویسد «erə-² „جدا کردن“، با گونهٔ *rē-». معنای «شکافتن، سست کردن» برگردان پذیرفتنی همان است. کلاین نیز ذیل rare همین خانواده را می‌آورد و — مهم برای گره ۱ — سنسکریت ardha- «بخش، پهلو، نیمه» را در آن جای می‌دهد. ادعای نورایی درست است.\",\n   \"sources\": [W_RARUS],\n   \"ref_check\": [\n    {\"ref\": \"POK:332\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt, form-feed page 346 (the article opens at the foot of printed p. 332 and runs over p. 333): '5. er-, ers-, thematisch (e)r-e- „locker, undicht, abstehend; auseinandergehen, auftrennen“. Ai. ṛ́te … nirrtiḥ „Auflösung“ … gr. ἐρῆμος „einsam“; ganz unsicher lat. rārus …'\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I 142 f. (WLD_Bd1_1930 djvu line 9238)\", \"stance\": \"supports\",\n     \"note\": \"'5. er-, als set-Basis erə-, thematisch (e)r-e- „locker, undicht, abstehend; auseinandergehn, auftrennen“' — the source Pokorny 332 abridges.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 (AHD_watkins1985.txt line 452)\", \"stance\": \"supports\",\n     \"note\": \"'erə-². To separate. Variant *rē-, contracted from *reə-. 1. Suffixed variant form *rā-ro- in Latin rārus … 3. Suffixed lengthened-grade form *rē-ti- in Latin rēte, rētis, a net … [Pok. 5. er- 332.]' — the source of Nourai's three-part root name and of both Latin glosses.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p. 863, §12.36 SIDE (SYN.txt form-feed leaf 933)\", \"stance\": \"supports\",\n     \"note\": \"'Skt. ardha-, Av. arada-, also “half” … perh. : Lith. ardýti “split, divide”, etc. Walde-P. 1.143. Uhlenbeck 14. Barth. 193.' — the same 'split' semantics for the root and the Avestan word of node 1.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. rare, adj. (KLN_1971.txt line 200276)\", \"stance\": \"supports\",\n     \"note\": \"'All these words derive fr. I.-E. base *er-, *ere-, “to loose; to split, separate, be rare”' — Klein's gloss is almost word for word Nourai's 'to split, loosen'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1, \"lang\": \"Avestan\", \"words\": \"areda, aredha\", \"verdict\": \"confirmed\",\n     \"derivation\": \"The two 'words' are one word in two of Nourai's transcriptions: Avestan arəδa-, whose δ he writes now d, now dh. Bartholomae, Altiranisches Wörterbuch 193, exactly the column Nourai cites, has 'j. arəδa-, p. arda- 1) Adj. „halb“ (nur Komp.). 2) m. „Seite“', with the passages (V. 6.1, Yt. 10.100 'dašinəm hē upa arəδəm … hāvōiia hē arəδe “rechts (links) ihm zur Seite”'), and the comparanda 'ai. ardha- Adj. „halb“, m. „Hälfte“, ārdha- m. „Seite“; oss. ärdäg „halb, Hälfte“'. So both of Nourai's glosses ('side, half') are Bartholomae's, in his order reversed. The link to the root box is Pokorny's er-dh- extension of '5. er-' (IEW 333: 'er-dh-: ai. ṛdhak „besonders, abgesondert“, ārdhaḥ „Teil, Seite, Hälfte“, ardhá- „halb“; lit. ardaii, -yti „trennen, spalten“'), the semantics being 'a half' = 'what has been split off'; Buck p. 863 says the same and cites Bartholomae 193 for the Avestan. The only shortfall is that Pokorny's er-dh- paragraph, on p. 333, cites the Sanskrit alone — the Avestan is supplied by Bartholomae and Buck, both of whom Nourai also cites.\",\n     \"derivation_fa\": \"دو «واژه‌» این گره یک واژه‌اند با دو آوانویسی نورایی: اوستایی arəδa- که ذال آن را گاه d و گاه dh می‌نویسد. بارتولومه در ستون ۱۹۳ — همان که نورایی ارجاع داده — می‌آورد: «اوستایی متأخر arəδa-، پارسی باستان arda-: ۱) صفت „نیم“ (تنها در ترکیب)؛ ۲) اسم مذکر „پهلو“» با شواهد ویدیوداد ۶٫۱ و یشت ۱۰٫۱۰۰، و هم‌ریشه‌های سنسکریت ardha- «نیم، نیمه»، آسی ärdäg. پیوند با ریشه از راه گسترش er-dh- است (پوکورنی ص ۳۳۳) و تحول معنایی آن روشن است: «نیمه» همان «آنچه جدا شده» است. باک نیز در ص ۸۶۳ همین را می‌گوید و به بارتولومه ۱۹۳ ارجاع می‌دهد. تنها نکته آنکه خود پوکورنی ذیل er-dh- فقط صورت سنسکریت را آورده و صورت اوستایی از بارتولومه و باک می‌آید — که هر دو را نورایی خود آورده است. ادعای نورایی درست است.\",\n     \"sources\": [],\n     \"ref_check\": [\n      {\"ref\": \"POK:332\", \"status\": \"partial\",\n       \"note\": \"p. 332-333 has the root and its er-dh- extension, but under er-dh- Pokorny cites only Sanskrit ('ai. ṛdhak „besonders, abgesondert“, ārdhaḥ „Teil, Seite, Hälfte“, ardhá- „halb“') — the Avestan form itself is not on the page.\"},\n      {\"ref\": \"SYN:863\", \"status\": \"supports\",\n       \"note\": \"Buck, Selected Synonyms p. 863, §12.36 SIDE (SYN.txt form-feed leaf 933; the leaf carries the printed number 863): 'Skt. ardha-, Av. arada-, also “half” (Av. “half” adj. only in cpds.), perh. : Lith. ardýti “split, divide”, etc. Walde-P. 1.143. Uhlenbeck 14. Barth. 193.' The word-table on the facing page lists 'Av. araδa-' under SIDE.\"},\n      {\"ref\": \"BRT:193\", \"status\": \"supports\",\n       \"note\": \"Altiran. Wörterbuch col. 193 (BRT.txt line 5446 carries the column number '193'): 'j. arəδa-, p. arda- 1) Adj. „halb“ (nur Komp.). 2) m. „Seite“ … ai. ardha- Adj. „halb“, m. „Hälfte“, ārdha- m. „Seite“; oss. ärdäg „halb, Hälfte“.' Both of the chart's glosses, verbatim.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"col. 193\", \"stance\": \"supports\", \"note\": \"see ref_check; also gives the Old Persian cognate arda-, which the chart does not use.\"},\n      {\"src\": \"SYN\", \"where\": \"p. 863 §12.36\", \"stance\": \"supports\", \"note\": \"'Skt. ardha-, Av. arada-, also “half” … perh. : Lith. ardýti “split, divide” … Barth. 193.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 143\", \"stance\": \"partial\",\n       \"note\": \"the er-dh- paragraph of '5. er-' is on WP I 143 (the page Buck cites for ardha-/araδa-), but WP prints the Indic and Baltic material and no Avestan form.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. rare, adj.\", \"stance\": \"supports\",\n       \"note\": \"Klein lists 'OI. ardhah, “part, side, half”, Lith. ardýti, “to cleave, separate”' among the members of base *er-, *ere- — independent confirmation that this word belongs in this root box.\"}\n     ]\n    },\n    {\n     \"id\": 2, \"lang\": \"Latin\", \"words\": \"rarus; rěte, rětis\", \"verdict\": \"plausible\",\n     \"derivation\": \"Both Latin words and both glosses are copied verbatim from the AHD appendix Nourai cites: 'erə-² … 1. Suffixed variant form *rā-ro- in Latin rārus, “having intervals between,” “full of empty spaces,” rare … 3. Suffixed lengthened-grade form *rē-ti- in Latin rēte, rētis, a net'. The words themselves are of course real (rārus 'thinly sown, of loose texture', antonym of dēnsus, from Livius Andronicus on; rēte / rētis 'net', Plautus on). But the attachment to the root is where every source hedges. Pokorny p. 333 writes 'ganz unsicher lat. rārus „locker, nicht dicht, selten“ (*erə-rō-s), eher glaublich rēte „Netz, Garn“' — i.e. rarus 'quite uncertain'. Ernout-Meillet s.v. rārus report the same comparison and dismiss it: 'Il s'agirait d'une racine *erə-, rē “séparer” … Tout cela vague et ne fournissant avec les mots latins aucun rapport qu'on puisse serrer de près'; s.v. rēte they add 'Mot technique et populaire, de forme mal fixée; peut-être emprunté'. Wiktionary calls rarus 'Uncertain', Etymonline calls rēte 'a word of uncertain origin … perhaps a loan-word from a non-IE language'. The semantic step 'loose-meshed' → 'net' is at least old and native: Varro, L.L. 5.130 already writes 'rete a raritudine'. So: real words, correctly glossed, but the root attachment is Watkins' confident version of what Pokorny and the Latin etymologists call doubtful.\",\n     \"derivation_fa\": \"هر دو واژهٔ لاتین و هر دو معنا عیناً از پیوست واتکینز برداشته شده است: «rārus „دارای فاصله، پر از جاهای تهی“ و rēte, rētis „تور“». خود واژه‌ها اصیل‌اند، اما پیوندشان با این ریشه محل تردید همهٔ منابع است: پوکورنی در ص ۳۳۳ می‌نویسد «بسیار نامطمئن است لاتین rārus …، باورپذیرتر rēte „تور“»؛ ارنوـمیه ذیل rārus همین مقایسه را می‌آورد و رد می‌کند (·«همهٔ این‌ها مبهم است و هیچ رابطهٔ دقیقی با واژه‌های لاتین به دست نمی‌دهد») و rēte را «شاید وام‌واژه» می‌داند؛ ویکی‌واژه نیز rārus را «نامعلوم» می‌خواند. در برابر، تحول معنایی «تنک‌بافت» > «تور» نزد خود رومیان شناخته بود (وارو، دربارهٔ زبان لاتین ۵٫۱۳۰: rete a raritudine). پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n     \"sources\": [W_RARUS, W_RETE],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 452: 'erə-². To separate … 1. Suffixed variant form *rā-ro- in Latin rārus, “having intervals between,” “full of empty spaces,” rare: RARE¹ … 3. Suffixed lengthened-grade form *rē-ti- in Latin rēte, rētis, a net: … RETINA'. Both forms and both glosses come from here word for word.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"POK\", \"where\": \"IEW 333\", \"stance\": \"partial\",\n       \"note\": \"'ganz unsicher lat. rārus „locker, nicht dicht, selten“ (*erə-rō-s), eher glaublich rēte „Netz, Garn“ (vgl. unten lit. rėtis, lett. rēta)' — the root's own author calls rarus 'quite uncertain'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. rārus and rēte (LAT.txt lines 52746, 53409)\", \"stance\": \"contradicts\",\n       \"note\": \"s.v. rārus: 'On a rapproché rātis, rēte … Il s'agirait d'une racine *erə-, rē “séparer” … Tout cela vague et ne fournissant avec les mots latins aucun rapport qu'on puisse serrer de près.' s.v. rēte: 'Mot technique et populaire, de forme mal fixée; peut-être emprunté.'\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. I 142\", \"stance\": \"partial\",\n       \"note\": \"'Lat. rārus „locker, nicht dicht, dünn, dünngesät, einzelstehend, selten“ (*erə-ro-s), vermutlich auch rēte „Netz, Garn“' — 'vermutlich', and a footnote records Reichelt's rival derivation of rēte from ordior, Wz. ar- 'fügen'.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. rare, adj. (KLN_1971.txt line 200276)\", \"stance\": \"partial\",\n       \"note\": \"puts rārus in this family but says of the second word only 'L. rarus is possibly rel. to L. rete, “net”; see retiary.'\"}\n     ]\n    },\n    {\n     \"id\": 3, \"lang\": \"English\", \"words\": \"rare; retina\", \"verdict\": \"plausible\",\n     \"derivation\": \"Both English words do go back to the Latin node, but each needs a stage the chart omits. RARE (adj. 1) is late 14c. 'thin, airy, porous', mid-15c. 'few and widely separated': it entered English from Old French rer/rere 'sparse' as well as directly from Latin rārus — Klein files it flatly as 'F., fr. L. rarus' — so the immediate donor is French, not Latin. RETINA is not a classical Latin word at all: it is Medieval/Medical Latin retina, which Klein (following Hyrtl, Das Arabische und Hebräische in der Anatomie 58) says was coined by the translator Gerard of Cremona (d. 1187) on Latin rēte 'net' as a loan translation of the Hebrew/Arabic anatomical term (Hebrew rešet, Arabic ṭabaqa šabakiyya '(the) net-like (layer)', itself rendering Greek ἀμφιβληστροειδής χιτών), on the resemblance of the vascular network at the back of the eye to a net; it reaches English by the late 14c. So the Arabic-Latin translation movement of 12th-century Toledo is the missing link in this arrow. Add to that the uncertainty inherited from node 2 (rēte may not belong to this root at all) and the node is plausible rather than confirmed; the words themselves and their Latin bases are not in doubt.\",\n     \"derivation_fa\": \"هر دو واژهٔ انگلیسی به گرهٔ لاتین بازمی‌گردند، اما هر دو حلقه‌ای را که نمودار نیاورده لازم دارند. rare در اواخر سدهٔ ۱۴م به معنای «رقیق، متخلخل» پدید می‌آید و کلاین آن را صریحاً «از فرانسه، از لاتین rarus» می‌داند؛ پس وام‌دهندهٔ بی‌واسطه فرانسه است نه لاتین. retina اصلاً واژه‌ای لاتینی کلاسیک نیست، بلکه لاتینی پزشکی است که به نوشتهٔ کلاین گراردوس کرمونایی (درگذشتهٔ ۱۱۸۷) در طلیطله بر پایهٔ rēte «تور» ساخته و ترجمهٔ تحت‌اللفظی اصطلاح عربیـعبری «طبقهٔ شبکیّه» (عبری rešet) است — و آن خود برگردان یونانی ἀμφιβληστροειδής است. پس نهضت ترجمهٔ عربی به لاتین در سدهٔ ۱۲م حلقهٔ گمشدهٔ این پیکان است. با افزودن تردیدی که در گرهٔ پیشین بر خود rēte هست، این گره با احتیاط پذیرفتنی است.\",\n     \"sources\": [E_RARE, E_RET],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\",\n       \"note\": \"AHD_watkins1985.txt line 452 lists RARE¹ under erə-² §1 and RETINA under §3 ('rēte, rētis, a net: RESEAU, RETE, RETIARY, RETICLE, RETICULE, RETINA'), exactly the two English words of this node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. rare, adj. and s.v. retina (KLN_1971.txt lines 200276, 205769)\", \"stance\": \"supports\",\n       \"note\": \"'rare, adj., thin. — F., fr. L. rarus' and 'retina, n. … Medical L. retina, coined by the translator Gerard of Cremona (1114?-1187) fr. L. rete, “net” (see retiary), as a loan translation of Hebrew resheth, “net”, used in Medieval Hebrew to denote the retina. See Joseph Hyrtl …'\"},\n      {\"src\": \"Etymonline\", \"where\": \"etymonline.com/word/rare and /word/retina (archived)\", \"stance\": \"partial\",\n       \"note\": \"rare: 'from Old French rer, rere “sparse” (14c.) and directly from Latin rarus … Sometimes reconstructed to be from a PIE root *ere- “to separate”'; retina: 'from Medieval Latin retina … probably from Vulgar Latin (tunica) *retina … ultimately from Latin rete “net” … The Vulgar Latin phrase might be Gerard of Cremona's 12c. translation of Arabic (tabaqa) shabakiyyah', and s.v. rete 'a word of uncertain origin … perhaps a loan-word from a non-IE language'.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-157.json\"\nwith io.open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"wrote\", out, os.path.getsize(out))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk157.py",
 "description": "Generate page-157.json"
}
```


### [2026-09-05T20:50:40.002Z] TOOL RESULT

```
wrote /home/sfmqrb/git/rishe/data/verification/page-157.json 51148
```


## [2026-09-05T20:50:44.305Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-157.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 157",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:50:46.919Z] TOOL RESULT

```
JSON OK
nodes verified: 11/11
node verdicts: {'confirmed': 7, 'plausible': 4}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 1}
books consulted: {'supports': 21, 'partial': 11, 'silent': 2, 'contradicts': 1} | by book: {'KLN': 6, 'WLD': 5, 'BRT': 3, 'HUB': 3, 'SKT': 3, 'Etymonline': 3, 'MON': 2, 'POK': 2, 'AHD': 1, 'IEC': 1, 'HRN': 1, 'PHD': 1, 'SOD': 1, 'Wiktionary': 1, 'SYN': 1, 'LAT': 1}
```


## [2026-09-05T20:51:03.530Z] AGENT

Page 157 (book p. 127) verified — `data/verification/page-157.json`, 0 PROBLEM lines.

**Counts:** 2 roots confirmed; 11 nodes = 7 confirmed, 4 plausible. Ref checks: 9 supports, 3 partial, 1 not_checked. 3 redirect entries skipped.

**Nothing disputed, nothing transcription_suspect, no extraction errors** — the JSON matches the chart throughout.

Plausible (why):
- **Er 1/Ergh, #2 Avestan `ereğant`** — form and gloss confirmed by Bartholomae (AiW col. ~350: `ərəγaṇt-` "entsetzlich, abscheulich", epithet of hell and of flies), but the arrow from *ergh- is only a hedge in Pokorny 339 ("können dazu in Beziehung stehen"); Bartholomae writes "Et.?" and Hübschmann PSt. 13 no. 72 says the link stands or falls on whether the word means 'angry/greedy' or (his older gloss) 'dark'.
- **Er 1/Ergh, #5 Greek `orğ-eyo, orxeisthai`** — the first form is not Greek but Watkins' PIE *orgh-eyo-, copied from the AHD line Nourai cites; and ὀρχέομαι's attachment to *ergh- is contested (Frisk/Beekes: iterative of ἔρχομαι; Wiktionary calls Watkins' ὄρχις link "semantically tenuous").
- **Ere 1, #2 Latin `rarus; rěte`** — glosses are verbatim AHD, but Pokorny himself says "ganz unsicher lat. rārus", Ernout-Meillet dismiss the comparison ("tout cela vague") and call rēte "peut-être emprunté".
- **Ere 1, #3 English `rare; retina`** — rare came via Old French rer/rere (Klein: "F., fr. L. rarus"), and retina is Medical Latin coined by Gerard of Cremona on rēte as a calque of Arabic *ṭabaqa šabakiyya*; both stages are missing from the chart.

Notable confirmations: BQT:32 is exactly right (Borhan vol. 1 p. 32 s.v. آرغده, with Mo'in's footnote at ارغنده giving Av. `ərəγant-`); SOD:57 is a *page*, not an entry number — Gharib no. 1446 on p. 57, "arγand ©Av. ərəγant — greedy". MON:205 could only be checked for content (entry present with the [فر.] French tag), not for pagination — the digitised Mo'in is the 2-vol abridgement.
