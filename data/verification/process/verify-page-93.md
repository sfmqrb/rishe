# Verification process log — verify-page-93


## [2026-09-05T14:05:53.677Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 93 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-93.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-93.json. Write /home/sfmqrb/git/rishe/data/verification/page-93.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 93` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:05:55.335Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:05:56.043Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:05:56.062Z] TOOL RESULT

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


## [2026-09-05T14:05:56.069Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-93.txt"
}
```


### [2026-09-05T14:05:56.083Z] TOOL RESULT

```
1	=== PDF page 93 (book page 63) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhergh : high  (refs POK:140)  PART 2
4	#1 (parent #0) [Sanskrit] refs=KLN:194; KNT:201 | brhant : high ; brahman : religious devotion, prayer
5	  #2 (parent #1) [Persian] refs=BQT:269 | brahman «برهمن» : Priest of an old Indian religion | extra: برهمه
6	  #3 (parent #1) [English] refs=KLN:194 | Brahma, Brahman
7	#4 (parent #0) [Germanic] refs=AHD | bergaz : hill ; burgs : hill fort ; harja-bergaz : army hill, harbor ☞Koro
8	  #5 (parent #4) [English] refs=AHD | iceberg, Canterbury, borough, harbor
9	#6 (parent #0) [Latin] refs=AHD:1509 | burgus : fortified place, town
10	  #7 (parent #6) [Old French] refs=AHD:156 | bourg : town ; burgeis : townsmen
11	    #8 (parent #7) [Persian] refs=MON:601 | bŭržŭâ «بورژوا» : townsman
12	    #9 (parent #7) [English] refs=AHD:156 | bourgeois : the middle class
13	  #10 (parent #6) [English] refs=AHD | burg, burglar
14	#11 (parent #0) [Latin] refs=KLN:614; AHD:1509 | horctus : high, good ; forctus, fortis : strong
15	  #12 (parent #11) [English] refs=AHD | fort, force, comfort, effort
16	--- entry 1 ---
17	ROOT Bheru -> redirect to Bher 5
18	--- entry 2 ---
19	ROOT Bheu -> redirect to Bhôu
20	--- entry 3 ---
21	ROOT Bheu 1 -> redirect to Beu 1
22	--- entry 4 ---
23	ROOT Bheu 2 -> redirect to Beu 2
24	
```


## [2026-09-05T14:06:00.431Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-93.json",
 "description": "Read source JSON for page 93"
}
```


### [2026-09-05T14:06:00.468Z] TOOL RESULT

```
{
  "pdf_page": 93,
  "book_page": 63,
  "entries": [
    {
      "root": {
        "name": "Bhergh",
        "lang": "Indo-European",
        "refs": "POK:140",
        "gloss": "high"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "KLN:194; KNT:201",
          "words": [
            {"translit": "brhant", "gloss": "high", "script": null},
            {"translit": "brahman", "gloss": "religious devotion, prayer", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:269",
          "words": [
            {"translit": "brahman", "gloss": "Priest of an old Indian religion", "script": "برهمن"}
          ],
          "script_extra": "برهمه",
          "note": null,
          "quote": {
            "text": "دگر باره مهمان دشمن شدی - صنم بودی اکنون برهمن شدی",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "English",
          "refs": "KLN:194",
          "words": [
            {"translit": "Brahma, Brahman", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "bergaz", "gloss": "hill", "script": null},
            {"translit": "burgs", "gloss": "hill fort", "script": null},
            {"translit": "harja-bergaz", "gloss": "army hill, harbor", "script": null, "see": ["Koro"]}
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
            {"translit": "iceberg, Canterbury, borough, harbor", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1509",
          "words": [
            {"translit": "burgus", "gloss": "fortified place, town", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Old French",
          "refs": "AHD:156",
          "words": [
            {"translit": "bourg", "gloss": "town", "script": null},
            {"translit": "burgeis", "gloss": "townsmen", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:601",
          "words": [
            {"translit": "bŭržŭâ", "gloss": "townsman", "script": "بورژوا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD:156",
          "words": [
            {"translit": "bourgeois", "gloss": "the middle class", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "burg, burglar", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:614; AHD:1509",
          "words": [
            {"translit": "horctus", "gloss": "high, good", "script": null},
            {"translit": "forctus, fortis", "gloss": "strong", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "fort, force, comfort, effort", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bheru",
        "redirect": "Bher 5"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bheu",
        "redirect": "Bhôu"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bheu 1",
        "redirect": "Beu 1"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Bheu 2",
        "redirect": "Beu 2"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T14:06:00.838Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:06:00.880Z] TOOL RESULT

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


## [2026-09-05T14:06:05.414Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo \"---refs_online keys---\" && python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','KNT','AHD','BQT','MON']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:600])\n\"",
 "description": "List verification dir and ref metadata"
}
```


## [2026-09-05T14:06:05.960Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bhereĝh\\|bhergh\\|bherĝh\" POK_full.txt | head -40",
 "description": "Grep Pokorny for bhergh"
}
```


### [2026-09-05T14:06:07.672Z] TOOL RESULT

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
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
---refs_online keys---
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
```


### [2026-09-05T14:06:07.722Z] TOOL RESULT

```
12712:Root / lemma: b^ergh- (*bhergh-)
```


## [2026-09-05T14:06:11.338Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && ls | grep -E \"9[0-9]\" ; echo \"---\"; ls | wc -l"
}
```


### [2026-09-05T14:06:11.463Z] TOOL RESULT

```
page-90.json
page-91.json
---
67
```


## [2026-09-05T14:06:11.907Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12700,12760p' POK_full.txt",
 "description": "Read Pokorny bhergh entry"
}
```


### [2026-09-05T14:06:11.963Z] TOOL RESULT

```
Old High German brawa co\i\6 go not back to *b'^reua, is proved tlirougli tlie grammat. 
variation in Old English, the form with -ku- assumes (Sievers-Brunner 200). 

Here probably a kind offish Old High German brahs{i)a, brahsina. Old Saxon bressemo 
' bream, freshwater bream ', Norwegian brasma, brasmeds., ablaut. Old Icelandic brosma 
"a kind of codfish'. 

Hittite par-ku-is{parkui§) "clean, pure', par-ku-nu-uz-zi {parkunuzi) 'purified, clean'. 

References: WP. 1 11 69, Feist 76 f., 103 f., Couvreur H 327. 
Page(s): 141-142 

Root / lemma: b^ergh- (*bhergh-) 

Meaning: to hide, keep 

Material: Gothic bafrgan^save, store, keep'. Old Icelandic bjarga. Old English beorgan. 

Old High German bergan. Old Saxon gibergan "save, store'; changing through ablaut Old 

English byrgan^buxy', byrgen{*burgiznd), byrgels. 

Old Saxon /?^/ig/s//" burial, funeral' and Old High German borfajgen' spare, look after, 

entrust, borrow'. Old English borg/an'\ook after, watch over, keep, borrow'. 

Note: 

Alb.-lllyrian and celt.- Slavic languages prove that from a zero grade of Root/ lemma: 

b^eregh-: "high; mountain' derived Root/ lemma: b^ergh-: "to hide, keep'. Cognates 

deriving from those two roots mark of wave of IE people who introduced burial mounds in 

Europe. 

Maybe alb. nasalized {*bergo) brenge^ concern, sadness (for a dead person?)', brengos 
"sadden' Slavic loanwords. 

Slavic *bergg\n Old Church Slavic (*bhergMei) bregg, bresf/^care, worry' in nebresti 
"neglect', russ. beregu, berecb "beware, preserve, protect, spare, look after, spare', Serbo- 
Croatian older brzem, br/jec/^guard, watch, preserve, protect, care, worry; hold festivities'; 
changing through ablaut kir. oborfh, gen. Oit'o/'d/?^ "haystack', Czech it'/'a/? "haystack, heap', 
poln. brog^barn, haystack' (out of it Lithuanian bragasds.); zero grade Czech brh^cave, 
cottage, tent'; East Lithuanian b/rg/nt/" spare'. 

Perhaps here gallo-rom. (rhat.-lllyrian) barga ' co\/ered thatched hut ', whether from 
*borga, Tagliavini ZrP. 46, 48 f., Bonfante BSL. 36, 141 f. 

References: WP. II 172, Trautmann 31, Feist 76. 



See also: compare above S. 141 . 
Page(s): 145 



Root / lemma: b^er-1 

Meaning: to bear, carry
```


## [2026-09-05T14:06:56.853Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"b\\^ereĝh\\|b\\^erĝh\\|bhereĝh\\|Page(s): 140\" POK_full.txt | head -20"
}
```


### [2026-09-05T14:06:56.901Z] TOOL RESULT

```
12387:Page(s): 140-141
```


## [2026-09-05T14:06:58.389Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"hoch, erhaben\\|Berg'\\|bergaz\\|burgs\" AHD_watkins1985.txt | head -30; echo \"=== bhergh in AHD ===\"; grep -n -i \"bhergh\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T14:06:58.464Z] TOOL RESULT

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bpbnvs3x7.txt

Preview (first 2KB):
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGH
...
</persisted-output>
```


## [2026-09-05T14:07:01.974Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find('bhergh-?. High;')\nprint(t[i:i+1800])\nEOF"
}
```


## [2026-09-05T14:07:02.138Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12330,12395p' POK_full.txt"
}
```


### [2026-09-05T14:07:03.628Z] TOOL RESULT

```
bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCH
```


### [2026-09-05T14:07:03.674Z] TOOL RESULT

```
Gothic bafrgahei^ mountain range, mountainous region ', Old Icelandic bjarg and berg. 
Old High German Old Saxon it'e/ig "mountain'. Old English beorh, i&eo/ig "height, burial 
mound', engl. barrow'buna\ mound' (compare Armenian -berj, cymr. bera. Old Indie 
barha-); 

Germanic *burgundT{= Old Indie brhatT, Celtic *brigantT, Irish Brigit) in Burgund, oldest 
name of Bornholm {Danish island) (actually " the high-rising ') and name Danish and 
Norwegian islands. Old High German Purgunt women's name, in addition Burgundiones, 
family name. 



Gothic baurgsi. "town, city, tower'. Old High German burg etc "castle' is genuine 
Germanic equivalent of Avestan bsrsz-, Celtic br/g-\N\t\r\ the meaning "fortified height as 
refuge'; With it is coincident though Latin burgus "castle, fort', that is borrowed from gr. 
nupYO(; "tower', an oriental loanword from urart. burgana ^pa\ace, fortress' derives (820 v. 
Chr., s. Adontz REtlE 1, 465), whereof would have also derived Armenian burgn, aram. 
burgin, burgon' tower' etc. after Kretschmer though nupyoq Germanic loanword 

Maybe alb. burgu^pnson' a Latin loanword. 

This contemplates *berghd'save, hide, shelter', originally ostensibly " providing 
sancturay for someone at a refuge ' as retrograde derivative to *b'^ergb- "mountain' (Gl. 22, 
113); s. above S. 145. 

Old Church Slavic bregb'bank, border, shore, slope', Serbo-Croatian br/jeg'\r\'\\\, bank, 
border, shore', russ. beregds., is probably not Germanic loanword, but rather Venetic- 
lllyrian origin; Bruckner KZ. 46, 232, Persson Beitr. 927; 

Maybe alb. bregu'bank, border, shore, slope' is a Slavic loanword not from lllyrian 
Berg/n/um. 

from latter with bregb as genuine Slavic words related kir. o-borfh, Czech it'/'a/? "haystack' 
etc belongs rather to Old Church Slavic bregg'care' (*preserve, save, hide, shelter), as 
stogb : GTsyu). 

Maybe alb. brenge'care, sadness, sorrow', i&/"e/7^c»s "sadden, worry' Slavic loanwords. 

With other vowel gradation *bh/-e^/7- perhaps in Old English brego, breogo^ master, 
mister, ruler, prince, lord'. Old Icelandic bragr^best, most exquisite, most distinguished, 
leader, chief, prince'. Middle High German brogen^ rise, direct upwards, wanton brag'. 

Tocharian AB park- " arise, rise, come up ', A parkant, B pirko " the rising ', A parkar, B 
parkre, parkre "tall'; 

perhaps A prakar, B prakre "tight, firm, solid' (compare Latin fortis); Hittite par-ku-us 
{parkus) "high' (: Armenian barjr). 

Hittite: parku- ' high ', parganu- (I) 'make high', pargatarr\. (r/n) 'height ', parkija-, park- (I) 
'stand up' (Friedrich 160-161) 

References: WP. II 173 f., WH. I 124, 535 f., 853, Feist 75 f., 85 f., Trautmann 30 f.. Van 
Windekens Lexique 90, Couvreur H 178. 



Page(s): 140-141 



Root / lemma: b^erem-1 
Meaning: to stick out; edge, hem 
Material: b'^orm-: 

Old Icelandic tiarmr^edge, hem', ey-barmr^ the edge of an island ', Norwegian dial.
```


## [2026-09-05T14:07:11.429Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12280,12332p' POK_full.txt"
}
```


### [2026-09-05T14:07:11.497Z] TOOL RESULT

```
Meaning: high; mountain 

Note: 

Root/ lemma: b^eregh-: "high; mountain' derived from Root/ lemma: b^erag-, b'^reg-: "to 

shine; white, *ash wood, ashen, birch tree, elm' 

Material: Old Indie Kaus. barhayat/ "\r\creases\ brmhat/" makes iai, obese, strengthens, 
uplifts', presumably barha-s, -m "tail feather, tail of a bird, esp. from a peacock'; brhant- 
"big, large, high, convex, elevated, noble, sublime', also "high, loud (of the voice)', fern. 
brhatT{= Irish Brigit, Germanic Burgund), Avestan bsrszant- {npers. buland), f. berezaitJ 
"high', in compound barazi-{: *bar9zra-), baraz-^b\QW and "height, mountain' (= npers. 
burz6s., Irish brl; the Nom. Avestan barsSubst could contain Aryan -ar-, but also Aryan - 
/-, Bartholomae IF. 9, 261), zero grade Avestan uz-barazayen/"\ shall allow to grow up ' (in 
addition IaTi-pap^avr|<; " improve luck ', Iran. *barzana-), barazan-m. barazah-v\. "height', 
barasnu-m. "elevation, height, sky, heaven, head', barazyah-^\r\\g\r\er', barazista-^ the 
highest, the most suitable '; npers. i?aAa "height' {*barz-), burz{see above); 



Old Indie brhant- stands for also "big, large, vast, grand, thick, massive' and brrhhati 
"makes fat, obese, invigorates, strengthens, increases, furthers', bfhana Mv. "dense, tight, 
firm, strong, proficient; very, absolutely', pa/7Z?/p'/7a-/7 "standing firm, dense, solid'. 

Armenian it'e/y" height' in erkna-, lerna-berj^sky-, mountainous' {*b^erghos), barjr^\\\Q'W 
{*b^rghu-), {ham-)barnam ( *barjnam, Aor. barji) "lift up' etc. 

Berg-\v\ PN the Mediterranean countries: thrak. BspyouAri, maked. Bspya, lllyrian 
^e/y//7/^/77 (Bruttium: Bergae), Ligurian Bergomum, Celto-Ligurian Bergusia, hisp. 
Bergantia eic about yO in klein Old Saxon nspyr), rispyaijoc;, maked. Cretan n£pya[JO(; 
suppositions by Kretschmer Gl. 22, 100 f., Krahe ZNF. 19, 64. 

Formations in i- grade: 

Latin for(c)tis. Old Latin forctus, dial, horctus, horctis^ physically, strong, powerful, 
robust; morally, brave, courageous, steadfast, bold, audacious ' (from *forg-tos, Indo 
Germanic *b'^rgb-tos = Old Indie brdhah). 

Cymr. bera'beap' (= Modern High German Berg), acorn, bret. bernds. (-rgh-n-?s. 
Pedersen KG. I 105), gall. PN Bergusia, zero grade Middle Irish bri, Akk. brig'\\\\\ (see 
above), cymr. i?/y"high, above', fem., cymr. corn. bret. bre^\\\\\ , gall. Litano-briga amouQ 
others PN; gall. Brigantes, BpiYavT£(; people's name (either "the sublime, noble' or " 
troglodyte, cave dweller, cliff dweller '; Old Indie brhant-), BrigantiaPH "Bregenz (western 
Austria)' and name of a feminine divinity. Old Irish Brigit {*b^rghntT} "name of a famous 
saint and generally women's name' (also Old Indie brhaff\s used as woman's name, also 
Old High German Purgunt), cymr. it'/'a//?/" privilege, prerogative' (actually "highness'), pi. 
breiniau, in addition mcymr. breenhin, ncymr. brenin^V\x\<^ , corn, brentyn, bryntynds. 
( *brigantTnos). 

Gothic bafrgahei^ mountain range, mountainous region ', Old Icelandic bjarg and berg. 
Old High German Old Saxon it'e/ig "mountain'. Old English beorh, i&eo/ig "height, burial
```


## [2026-09-05T14:07:13.238Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 1966 Brahman ===\"; grep -n -i \"Brahman\\|Brahma,\" KLN_1966.txt | head -20; echo \"=== KLN forctus/fortis ===\"; grep -n -i \"forctus\\|horctus\" KLN_1966.txt KLN_1971.txt LEW_1910.txt LAT.txt | head -20"
}
```


### [2026-09-05T14:07:13.317Z] TOOL RESULT

```
=== KLN 1966 Brahman ===
5381:borough,  n.  —  ME.  burgh,  burwe,  fr.  OE.  burg, burh,  burg,  rel.  to  OS.,  OFris.,  burg,  ‘castle’, ON.  borg,  ‘wall,  castle’,  MDu.  burch,  borch, borcht,  Du.  burchl,  burg,  OHG.  burg,  burc, buruc,  ‘fortified  place,  citadel’,  MHG.  burc, G.  Burg,  ‘castle’,  Goth,  baurgs,  ‘city’,  OE.  beorg, etc.,  ‘mountain’.  These  words  prob.  derive  fr. I.-E.  base  *bhergh-,  ‘high’,  whence  also  Arm. berj,  ‘high  place',  OSlav.  bregu,  ‘bank  (of  a river)’,  W.  bera,  ‘stack,  pyramid’,  Mir.  bri,  acc. brig,  ‘hill’,  Toch.  A  parkas,  ‘long’,  Hitt,  parkush, ‘high’,  OI.  bfhdnt-,  Avestic  blrlzant-,  ‘high’, OCeltic  Brigantes,  lit.  ‘the  high  ones’  (cp.  Bur¬ gundians,  fr.  Late  L.  Burgundiones,  lit.  ‘high¬ landers’),  prob.  also  OL.  forctus,  ‘good’,  L. fortis  (fr.  OL.  forctis),  ‘strong’,  see  Walde-Hof- mann,  LEW.,  I, pp.  535-36,  s.v. fortis, and  Kluge- Mitzka,  EWDS.,  p.67,  s.v.  Berg.  Cp.  barrow, ‘mountain,  mound’,  bourgeois,  burgage,  burgess, burgh,  burgrave,  Burgundy,  canterbury,  faubourg, gaussbergite,  ghetto,  Hapsburg,  hauberk.  Cp.  al¬ so  Brahma,  fort,  and  the  second  element  in  bar- bicane.  Cp.  also  the  suff.  -bury  in  English  place names,  which  comes  fr.  OE.  byrig,  the  dative sing  of  OE.  burg.  Base  *bhcrgh-  is  prob.  an  en¬ larged  form  of  base  *bher-,  ‘to  carry,  lift’.  See bear,  ‘to  carry’.
5510:Brahma,  Brahaman,  n.,  [)  the  impersonal  world soul;  2)  the  chief  member  of  the  trinity  Brahma, Vishnu  and  Siva  ( Hindu  religion).  —  OI.  brah¬ man-  (neut.),  ‘prayer,  the  universal  soul,  the  Ab¬ solute’  (in  this  last  sense  exceptionally  treated as  masculine),  Brahman  (masc.),  ‘the  chief  god of  Hindu  religion’,  of  uncertain  origin;  possibly related  to  OI.  bphdnt-,  ‘high’,  fr.  I.-E.  base *bhergh-,  ‘high’.  See  borough.
5511:Derivatives:  Brahma-hood,  n.,  Brahma-ic,  adj., Brahman,  n.  (see  next  word)
5512:Brahman,  n.,  a  member  of  the  highest  priestly caste  among  the  Hindus.  —  OI.  brahmana-,  fr. brahman-,  ‘prayer’.  See  prec.  word.
5513:Derivatives:  Brahman ,  adj.,  Brahman-ic,  adj.. Brahman-ism,  n.,  Brahman-ist ,  n.,  Brahman-ist- ic,  Brahman-y,  adjs.
5514:Brahmanee,  Brahmani,  n.,  a  Brahmin  woman.  —
5517:OI.  brahmani,  fern,  of  brahmana-.  See  prec.  word, brahmapootra,  usually  shortened  to  brahma,  n., name  of  a  large  species  of  fowl.  —  From  Brah¬ maputra,  name  of  the  great  river  in  India. Brahmin,  n.  —  A  var.  of  Brahman, braid,  tr.  v.  —  ME.  breiden,  braiden,  fr.  OE.  breg- dan,  ‘to  move  quickly,  brandish;  to  weave’,  rel. to  ON.  bregda,  ‘to  brandish,  turn  about,  braid’, OS.  bregdan,  ‘to  weave’,  Du.  breien,  ‘to  knit’, OHG.  brettan ,  MHG.  bretten,  ‘to  draw,  weave, braid’.  The  orig.  meaning  of  these  words  was ‘to  move  suddenly  to  and  fro’.  They  ult.  derive fr.  I.-E.  base  *bherek-,  ‘to  shine’,  whence  also OI.  bhrdsate,  ‘flames,  blazes,  shines’,  Gk.  cpopxot;, ‘white,  gray’.  Cp.  brae,  bream,  a  fish,  bridle, broider,  upbraid.  Cp.  also  bright  and  words there  referred  to.
20136:Derivatives :  jail,  gaol,  tr.  v.,  jail-er,  gaol-er,  n. Jain,  n.,  an  adherent  of  a  non-Brahmanic  sect in  India.  —  Hind.  Jaina,  fr.  OI.  Jainah ,  ‘of  a Buddha’,  fr.  jinah,  ‘hero,  saint’,  which  is  rel.  to jayati,  ‘conquers’,  jayah,  ‘victory’,  jindti,  ‘over¬ comes,  subdues’,  jyd,  jid,  ‘superior  force’,  jydyan, ‘mightier’,  jyesfhah,  jyesthah,  ‘mightiest’,  and cogn.  with  Gk.  fitoc,  ‘force,  might,  violence’. Cp.  the  second  element  in  Zenobia.
=== KLN forctus/fortis ===
LAT.txt:23828:38). On interpritait generalement forctus (et le dialectal horctus)
LAT.txt:28418:horctus: v. fortis.533
KLN_1971.txt:32014:landers’), prob. also OL. forctus, ‘good’, L. 
KLN_1971.txt:96272:is rel. to OL. forctus, dial, horctus , horctis, 
KLN_1966.txt:5381:borough,  n.  —  ME.  burgh,  burwe,  fr.  OE.  burg, burh,  burg,  rel.  to  OS.,  OFris.,  burg,  ‘castle’, ON.  borg,  ‘wall,  castle’,  MDu.  burch,  borch, borcht,  Du.  burchl,  burg,  OHG.  burg,  burc, buruc,  ‘fortified  place,  citadel’,  MHG.  burc, G.  Burg,  ‘castle’,  Goth,  baurgs,  ‘city’,  OE.  beorg, etc.,  ‘mountain’.  These  words  prob.  derive  fr. I.-E.  base  *bhergh-,  ‘high’,  whence  also  Arm. berj,  ‘high  place',  OSlav.  bregu,  ‘bank  (of  a river)’,  W.  bera,  ‘stack,  pyramid’,  Mir.  bri,  acc. brig,  ‘hill’,  Toch.  A  parkas,  ‘long’,  Hitt,  parkush, ‘high’,  OI.  bfhdnt-,  Avestic  blrlzant-,  ‘high’, OCeltic  Brigantes,  lit.  ‘the  high  ones’  (cp.  Bur¬ gundians,  fr.  Late  L.  Burgundiones,  lit.  ‘high¬ landers’),  prob.  also  OL.  forctus,  ‘good’,  L. fortis  (fr.  OL.  forctis),  ‘strong’,  see  Walde-Hof- mann,  LEW.,  I, pp.  535-36,  s.v. fortis, and  Kluge- Mitzka,  EWDS.,  p.67,  s.v.  Berg.  Cp.  barrow, ‘mountain,  mound’,  bourgeois,  burgage,  burgess, burgh,  burgrave,  Burgundy,  canterbury,  faubourg, gaussbergite,  ghetto,  Hapsburg,  hauberk.  Cp.  al¬ so  Brahma,  fort,  and  the  second  element  in  bar- bicane.  Cp.  also  the  suff.  -bury  in  English  place names,  which  comes  fr.  OE.  byrig,  the  dative sing  of  OE.  burg.  Base  *bhcrgh-  is  prob.  an  en¬ larged  form  of  base  *bher-,  ‘to  carry,  lift’.  See bear,  ‘to  carry’.
KLN_1966.txt:15222:fort,  n,  —  F.  fort ,  ‘stronghold,  fort’,  from  the  ad¬ jective  fort,  ‘strong’,  fr.  L.  fortis ,  ‘strong’,  which is  rel.  to  OL.  forctus,  dial,  horctus ,  horctis, ‘good’ ;  prob.  fr.  I.-E.  base  *bhergh-,  ‘high,  to raise’.  See  borough  and  cp.  words  there  referred to.  Cp.  also  force,  ‘strength’,  fortalice,  forte, fortress,  comfort,  counterfort,  sforzando. fortalice,  n.,  a  small  fort.  —  Orig.  ‘a  fortress’,  fr. OF.  fortelece,  corruption  of  forteresse.  See fortress.
```


## [2026-09-05T14:07:21.368Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['KLN_1966.txt']:\n    lines=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    # find page-ish markers near line 5510\n    for i in range(5460,5520):\n        if re.search(r'\\[pdf page|\\f|^\\s*\\d{2,4}\\s*$', lines[i]):\n            print(f,i,repr(lines[i][:120]))\nEOF\ngrep -c $'\\f' KLN_1966.txt; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\""
}
```


## [2026-09-05T14:07:22.872Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"brhant\\|brhánt\\|bṛhant\" KNT.txt | head -20; echo \"=== KNT baršan/barz ===\"; grep -n \"barsan\\|bard-\\|barz\" KNT.txt | head -20"
}
```


### [2026-09-05T14:07:23.252Z] TOOL RESULT

```
KLN_1966.txt 5463 '193'
KLN_1966.txt 5484 'boyar,  n . ,  a  member  of  an  order  in  Russian  aristo¬ cracy.  —  Russ,  boyarin,  fr.  boji,  ‘struggle’,  in gr'
KLN_1966.txt 5514 '194'
KLN_1966.txt 5515 '195'
902
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
```


### [2026-09-05T14:07:23.305Z] TOOL RESULT

```
5737:bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
=== KNT baršan/barz ===
1774:йр- ‘water’, zíap- ‘night’, xfnau- in u-zfnau- ‘well satisfied’, gau- ‘cow’ in compounds, bard- ‘year’, dwar- ‘door’ in duvara-, nar- ‘man’ in üv-nara-, nàv- ‘ship’, паћ- ‘nose’, pad- ‘foot’ in nipadiy etc., vas- ‘wish’ in adv. vasiy, vib- ‘house’, séd- in upa-stá- ‘aid’, zam- ‘earth’ in u- zma- etc.; perhaps napdl- ‘grandson’, an old pIE word, probably a compound; possibly dà- in ‘wada- as element of Paisiyà-uvüdà-, and vaj- in gen. daha-vaja. $143. Noun AND ApjectivE STEMS WITH THE-
5477:bard- sb. ‘year’: Av. sarad- ‘year’, NPers. säl, Skt. Sardd- ‘autumn’ (§31, 587, $142). For the chronology of the rebellions against Darius, see Hist. App. IV. &ardam asf. DB 5.3. barda gsf. DB 4.4f, 41, 45, 52, 60.
5737:bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
5738:Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
5740:(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
5748:brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
```


## [2026-09-05T14:07:33.588Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# count formfeeds before line 5737 and 5748\nfor target in (5737,5748):\n    n=sum(1 for l in lines[:target] if '\\f' in l)\n    print(target,'formfeeds before:',n)\nEOF"
}
```


## [2026-09-05T14:07:34.732Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW fortis ===\"; grep -n \"fortis\" LEW_1910.txt | head; echo \"=== LAT fortis ===\"; sed -n '23815,23850p' LAT.txt"
}
```


### [2026-09-05T14:07:35.311Z] TOOL RESULT

```
5737 formfeeds before: 220
5748 formfeeds before: 221
```


### [2026-09-05T14:07:35.372Z] TOOL RESULT

```
=== LEW fortis ===
=== LAT fortis ===
aussi *confortidre, M.L.3i38 a .
Dirivis et composta: fortiter-, fortitudo (fortit ia n'existe pas;
fortitds n'est que dans les gloses); forticulus et fortiusculus (tar-
dif et rare); fort&scd,-is (un ex. de Laevius); fortifico,-as (tar-
dif); fortioSus (Virg.gramm.); compose; conforts,-as (-fortio, d'aprbs
confirmo, etc.), utilisi comme synonyme de roborS dans 1 'Itala, et con¬
servi dans les 1 . romanes., M.L.3J-38; praefortis (Tert.). L'explication
de fortasse,-sis par un optatif en -ss- de *forto( non atteste) est
de pure fantaisie.
L'abrigi de Festus a les gloses: horctum et forctum pro bono dice¬
bant, 91,14; forctes (l.-iis?) frugi et bonus siue ualidus, <74,14;
et dans le texte de Festus on lit, 474,36, itaque in III (1,5) cautum
est ut idem iuris esset Sanatibus quam Porctibus, i. e. bonis (cf.436.
38). On interpritait generalement forctus (et le dialectal horctus)
comme un doublet de foretis, ancienne forme de fortis-, mais foretis,
fortus sont peut-etre des noms d'une peuplade latine, cf. Thes. s.u.
II semble qa'il faille partir d'un aneien foretis, donc d'une racine
terminee par gutturale. La racine *dher~, qui figure dans firmus, etc.,
a, d'ailleurs, une autre nuance de sens. D'autre part, le rapproche-
ment avec skr. dfmhati "il affermit", drdhdh "ferne", w.darazayeiti
"il attache fortement", dsrazro "ferme, solide", lit.dififas "courroie"
n'est possible que si l'on separe gr.Spacrcrop/xt, "je saisis", v.b.a.
zarga "cloture" et si l'on pose *dhergh-. Le rapprochement le plus
plausible serait dbs lors avec av. draiaite "il tient", v.sl .druiati
"tenir", gr. Tpecpo(UX 1 "je me coagule" (fut. 0 pev)/O|xa 1,); pour le sens,
cf. gr. xaptpuc "epais", Tp6<jM.<; "gros, bien nourri"; mais il n'y a pas
evidence, tant s'en faut.
forum, -1 n. ( forus m.vulg.): a du designer A 1'origine 1'enclos
qui entoure la maison (cf. fores, forus), 1'enclos devant la tombe ( forum
antiqui appellabant quod nunc uestibulum sepulcri dicari solet, P.F.
74,31; cf. Cic.Leg.3,34,61). Dans la langue rustique, il a le sens tech-
nique de "partie du pressoir oA l r on disposait les grappes ou les
olives a ecraser". Le mot a eu une fortune particulibre dans le sens
de "place de marchi": /. bodrium, olitorium, etc., cf. Varr.L.L.5,i4Ssqq.
qui le distingue de macellum "marchi couvert"; et il .a servi k disigner
nombre de villes: Porum Alieni, P. Appii, P. Aurelium, P. Cornelium, etc.
```


## [2026-09-05T14:07:46.521Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==221{print substr($0,1,600)}' KNT.txt; echo \"-----222-----\"; awk 'BEGIN{RS=\"\\f\"} NR==222{print substr($0,1,400)}' KNT.txt"
}
```


## [2026-09-05T14:07:47.301Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT برهمن ===\"; grep -n \"برهمن\" BQT_v1_pages.txt BQT_v2_pages.txt 2>/dev/null | head -20"
}
```


### [2026-09-05T14:07:48.298Z] TOOL RESULT

```
tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, b
-----222-----
r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 bis, 5 bis, 6; 2.93; DBa 5, 6, 6f, 7, 8; DSf 12, 58; XPa 15; ХРе 12; XPf 16, 17, 19, 23, 31, 33, 42; XPg 7; X8a 2; XV 18; А!Ра 20f; D?Sb 4°. pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; XPf 35, 38, 47.
Pirdva- sb. ‘Nile’ (§75.V, $12
```


### [2026-09-05T14:07:48.345Z] TOOL RESULT

```
=== BQT برهمن ===
BQT_v1_pages.txt:19256:برهمن است ت که پیر ومرشد - وحکیم ودانشمند
BQT_v1_pages.txt:19259:برهمن است که اصیل و نجیب - وحکیم سوپیر
BQT_v1_pages.txt:19270:از براعمه , رك : دائرةالنعارف اسلام : پراحمه . ۴ - صرفی است در برهمن ( شای
BQT_v1_pages.txt:22028:لهای « بروزن مخزن» مختف‌برهمن ۴
BQT_v1_pages.txt:28434:نیز گویند و برگه آنرا زنان برهمن در شکاف
BQT_v1_pages.txt:28437:وبرهمنان کتابهای خودرا ازبر کهآ ندرخث سازند
BQT_v2_pages.txt:3128: ‫ونیزطایفه‌ای باشند ازبرهمنان تکشه‌آمی‌افروزند‬
```


## [2026-09-05T14:07:54.406Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} /brazmaniya/{print \"RECORD\",NR; print substr($0,1,300); print \"...\"}' KNT.txt | head -20"
}
```


## [2026-09-05T14:07:55.016Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '19240,19280p' BQT_v1_pages.txt"
}
```


### [2026-09-05T14:07:56.246Z] TOOL RESULT

```
RECORD 31
padahya, Skt. gharmá-; дата-, Av. sarad-; darga-, Av. daraga-, Skt. dirghd-; baršnā, Av. instr. barasna; martiya, Skt. mártya- .
ardastana- ‘window-frame’, Elam. har-da-i5-da- па.
tarsatiy with Iran. tars- because of NPers. (0708, $ despite Av. drasaiti, from is-, both with IE Ж suffi
...
RECORD 57
ress hu, with vocalic u, the single character u was used, and to express hus for hy (from sy), u was written—the А being omitted in both situations:
Nom. Dàrayava^u&, gen. Darayavahaus. Nom. Hara*uvati&, Skt. sdrasvati.
Loe. pl. aniyd*uy-d, Skt. anyasu.
Mwa- ‘own’, Av. т?а-, Skt. sva-.
^wa
...
RECORD 175
m :
17 patiyaxsayaly : manā : bajim : abaraha : t
18 yašām : пасата : aflahiya : ava : akunava : d
19 абат :tya : mana : avadià : adáraya : Mada
20 : Оја : Harauvatiá : Armina : Zraka : Partava
21 : Haraiva : Baxtn$ : Sugda : Uvarazmi
22 &:Dàbirus : Абша : Oatagus : Sparda
```


### [2026-09-05T14:07:56.291Z] TOOL RESULT

```
کوچك را نیز کفته‌اد - وآریش و زیت رائیز
رازبانج است ۱ .کویند از دوزبکه آقاب‌ببرج
حمل میرود ح رکه هر روز ز يك درهم نخم‌راز بانه
با يك درهم فند سفید سفوف کند و تا سه ماه‌در
خوردن آن مداومت نمابد در نمام سال مریض
نشود ؛ و جمیم گزندکان تخم رازبانه خورند
بجهت روشنایی چشم . و افمی چشم‌خود راببهت
روشنابی و نقوت برآن مالد . #
برههی ؟ » بتح اول و ثالی و حیم
بروزن قلمزن» بمعنی بت‌پرست و زناربند باشد
و حکما و دانثه‌ندان و پیر و مرشد بت‌پرستان
و هندوان و آته تش‌پرستانرا هم میگوند -واصیل
و نجیب هنود را نز برهم نگویند » و بفتح‌اول گویند - و بمعنی کمر گاه و کم رکوه هم بنظر
و سکون انی بوزن کر کدن هم آمده است . آمده است ؛ و بنم اول لبز درستست .
دل ۲ ۰ ۳ . ۱
بر همنك * - بروزن سمرفند ۰ بمعنی بر هو ه » بروزن‌انبوه . صابونراکویند
برهمن است ت که پیر ومرشد - وحکیم ودانشمند
و اصیل و جیب هنود باشد .
بر همه 9 بر وزن طبقجه » مخغف
برهمن است که اصیل و نجیب - وحکیم سوپیر
و مرشد هنود باشد . #
بر هوت؟ » بروزن‌بهوت. دابداروبی(۱)
و آن چیزیست که بدان رخت شویند .
بر هیکت اه بر وزن انگیهت مانی
پرهیشتن است بعی بر کشید و برآوود . :
بر هیختی ۲ - بر وزن انگیختن حطلق
بر کشیدن را گویندت ویمعنی بر آ وردن‌هم است. *
(۱) چنن است درنسخ و صحیح :, وأدیی . ۱
_ ۳60۷ «لك۱ ص۰۲۱ . ۴ - مانسکرت ۵۲21111813 بمعنی‌مطلق
پیشوابان روحانی؛ یکی از سهطبقةٌ مردم درآیین برهمابی «مزدیسنا ۹4*۵» راجم بتصور عسلمانان
از براعمه , رك : دائرةالنعارف اسلام : پراحمه . ۴ - صرفی است در برهمن ( شای
فرهمند ) . ۴ مد ساسکرت 2 (روحانی) دوبلیامز 4۷۲۳۸ ۰ رك : پرهمن.
9 - نیز بلهوت و برهوت » وآن وادبی است در حضرموت .که در جوار آن در دامنة
کوهی آتشفشانی چاه مشهور به‌بثر برهوت واقع‌است «دائر:المماری اسلام». ٩‏ رث: برهیختن.
۷ سم یکب‌از: پیشوند بر -هیخ ( هنکه ‏ 10208 اوستابی ی پسولد
مصدری) «فاب۱ : ۸٩‏ «امنا ۱: ۱ص ۲۷ ۱۳۵,۱.
برهما _ بفتح اول و دوم » ساسکربت ۶۵500۸
( ذات واجب‌الوجود. فادر مطلق ( «ونلامز ۷۳۸ خدای‌بز رکه
حندوان باستان, او مظهر آفربد کار جهان وخدایان و فادرمطلق
است؛» وي با ۷۱51۱۲0۷ ( محافظ ) و۷۵ «مخرب * تلیثی را
تشکیل یدود . در ربگه ودا ۹ حرآغاز « ند رجود بود نه
```


## [2026-09-05T14:08:05.978Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} END{print \"records:\",NR}' KNT.txt; grep -c \"\" KNT.txt; echo \"=== search brazmaniya lines ===\"; grep -n \"brazmaniya-\" KNT.txt | head; echo \"=== nearby page numbers ===\"; sed -n '5700,5760p' KNT.txt | grep -n \"^[0-9]\\{1,3\\}$\\|LEXICON\""
}
```


### [2026-09-05T14:08:07.780Z] TOOL RESULT

```
records: 232
5869
=== search brazmaniya lines ===
1494:pIE gh: brazmaniya-, Uvárazmi-, игта-, züra-, zü- rakara-.
5748:brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
=== nearby page numbers ===
13:LEXICON 199
45:LEXICON
53:201
```


## [2026-09-05T14:08:12.837Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=19270 && /\\[pdf page/{p=$0; n=NR} END{}' BQT_v1_pages.txt; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<19270' | tail -3; echo \"--- after ---\"; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1>19240' | head -3"
}
```


## [2026-09-05T14:08:14.477Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON بورژوا ===\"; grep -n \"بورژوا\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10"
}
```


### [2026-09-05T14:08:14.607Z] TOOL RESULT

```
--- after ---
```


### [2026-09-05T14:08:14.664Z] TOOL RESULT

```
=== MON بورژوا ===
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26041:بورژوا: 5 شهری» شهر نشین ( که در 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:26044:متعلق به بورژوازی. 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:65736:است؛ موافق بورژوازی یا سرمایه‌داری. (.) 
MON_part1.txt:26041:بورژوا: 5 شهری» شهر نشین ( که در 
MON_part1.txt:26044:متعلق به بورژوازی. 
MON_part1.txt:65736:است؛ موافق بورژوازی یا سرمایه‌داری. (.)
```


## [2026-09-05T14:08:19.188Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -5 BQT_v1_pages.txt; echo \"==== grep tag styles ====\"; grep -n -m5 \"pdf page\\|صفحه\" BQT_v1_pages.txt | head; echo \"=== formfeed count ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v1_pages.txt; awk 'BEGIN{RS=\"\\f\"} /برهمن است ت که پیر/{print \"REC\",NR}' BQT_v1_pages.txt"
}
```


## [2026-09-05T14:08:19.270Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26030,26050p' MON_part1.txt"
}
```


### [2026-09-05T14:08:20.883Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
==== grep tag styles ====
133:خ مسیمت مصت ‏ سسسسست خن بت پوت وت بت سسصفحه 7
897:با میکنيم : بقیه در صفحهٌ ۲۵یست وینج زبانهای ایرانی
922:بقبه از صفحهٌ ۲6
1884:۲ - مولف انجمن‌آرا وشته : مه در حاشیه صفحه مدپنجاه ونه دسانیر
1892:بقبه ازصفحهٌ پیش
=== formfeed count ===
777
REC 490
```


### [2026-09-05T14:08:20.927Z] TOOL RESULT

```
بور؛ 05۲ (ص.) سرخ» قرمز رنگ. اسب 
سرخ. دماغ سوخته» هجل» خجل. 

بوران: ۰527 [تر.] (ا.) باران با برفی که با 
باد باشد. باد شدیدی که برف‌های کوه را از 
جایی بجایی منتقل کند. 

بسورانی: آ-۲27 (ص‌نس.. امر.) نان 
خورشی که از اسفناج و کدو و بادنجان با 
ماست و کشک سازند. 

بورژوا: 5 شهری» شهر نشین ( که در 
سابق از حقوق مخصوص برخوردار بود) 
شهر نشین مرفه و روتمند. ارتات» مخدوم. 
متعلق به بورژوازی. 

بسورزوازی: ۱072221(.) طعة 
سر مایه‌داری که با در دست داشتن وسایل 
تولید و سرمایه زندگی مرفه دارد. 

بورس: 0۳ (.) بازاری که داد و ستد و
```


## [2026-09-05T14:08:31.699Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));import sys\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\""
}
```


## [2026-09-05T14:08:32.602Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==489||NR==490||NR==491{print \"=== REC\",NR,\"===\"; print substr($0,1,200)}' BQT_v1_pages.txt"
}
```


### [2026-09-05T14:08:33.280Z] TOOL RESULT

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
```


### [2026-09-05T14:08:35.344Z] TOOL RESULT

```
=== REC 489 ===
بردث
لر ون ه بکراول بروزن فون,»مخنف
بیرون است ٩‏ - و بممنی برای وبجهت هم‌هست
چنانکه کوبند «برون تو؛یمنی برای ن�
=== REC 490 ===
است درحضرموت. کویت. درآنجا چاهی امت که
ارواح کفار و عنافین آنجا جمم شوند .
بر هو 3 - با واومجهول بروزن محموده
چیزی
=== REC 491 ===
و کار بهوده و بیفایده کردن باشد . #
پر ود قلكك - کنابه ازماه است که‌قمر
باشد - و ژحل را نی زگفته‌اند 3
بر لژزن - بکر
```


## [2026-09-05T14:08:51.966Z] TOOL CALL #30: Bash

```json
{
 "command": "head -40 tools/fetch_source.py; echo \"...\"; ls data/verification/sources/web | head"
}
```


### [2026-09-05T14:08:52.021Z] TOOL RESULT

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
...
0013bab04a208776.txt
0070109655be6e11.txt
00738e15ee065d37.txt
008d977afc1818a4.txt
0097c36e54f76601.txt
00b2c829968cc7a8.txt
01326eac7cfcce41.txt
0180d09c6db6728a.txt
018d14b3fe147c94.txt
01a350f2398643fc.txt
```


## [2026-09-05T14:08:59.354Z] TOOL CALL #31: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\" \\\n \"https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A5%8D%E0%A4%B0%E0%A4%B9%E0%A5%8D%E0%A4%AE%E0%A4%A8%E0%A5%8D\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%85%D9%86\" \\\n \"https://en.wiktionary.org/wiki/fortis\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 93, root Bhergh part 2 (Nourai p.63): PIE *bherg'h- 'high', Skt brahman, Pers barhaman, Lat fortis\" ; done 2>&1 | tail -8"
}
```


## [2026-09-05T14:09:01.407Z] TOOL CALL #32: Bash

```json
{
 "command": "for u in \\\n \"https://www.etymonline.com/word/bourgeois\" \\\n \"https://www.etymonline.com/word/burglar\" \\\n \"https://www.etymonline.com/word/borough\" \\\n \"https://www.etymonline.com/word/harbor\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 93, root Bhergh part 2: Latin burgus > OFr bourg/burgeis > English bourgeois, burglar; OE burg/herebeorg\" ; done 2>&1 | tail -8"
}
```


### [2026-09-05T14:09:04.057Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/009ed6a3d0d97ac5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8e2cab5cf4272d09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec3e64fe722f2395.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ded606778185ce0.txt
```


### [2026-09-05T14:09:06.523Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e3b3ff4b309a2e94.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3ae7f25932ee1cd3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8997266b77b21809.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b6723f326757c9c4.txt
```


## [2026-09-05T14:09:09.137Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### PIE bhergh\"; grep -n -i -m40 \"Proto-Indo-European\\|Root\\|high\\|Descend\\|Derived\" 009ed6a3d0d97ac5.txt | head -40; echo; echo \"###### size\"; wc -c 009ed6a3d0d97ac5.txt"
}
```


### [2026-09-05T14:09:09.183Z] TOOL RESULT

```
###### PIE bhergh
1:URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-
4:TITLE: Reconstruction:Proto-Indo-European/bʰerǵʰ- - Wiktionary, the free dictionary
6:Reconstruction:Proto-Indo-European/bʰerǵʰ- - Wiktionary, the free dictionary 
57: Proto-Indo-European 
59: Toggle Proto-Indo-European subsection 
62: Root 
65: Derived terms 
72: Reconstruction:Proto-Indo-European/ bʰerǵʰ- 
126: See also: Reconstruction:Proto-Indo-European/bʰergʰ- 
128: This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.
130: Proto-Indo-European
133: Root
141: to be elevated , up high 
143: Derived terms
146: Terms derived from the Proto-Indo-European root *bʰerǵʰ- (89 c, 0 e) 
148: *bʰérǵʰ-e-ti ( thematic root present ) 
154: *bʰérǵʰ-t ~ *bʰr̥ǵʰ-ént ( root aorist ) 
169: > ? Old Armenian: բառնամ ( baṙnam , “ to lift up, raise ” ) ( see there for further descendants )
197: Proto-Italic: *forktis ( see there for further descendants )
200: > ? Proto-Celtic: *brixtus ( “ magical formula, incantation ” ) ( see there for further descendants )
234: Retrieved from " https://en.wiktionary.org/w/index.php?title=Reconstruction:Proto-Indo-European/bʰerǵʰ-&oldid=92171312 "
236: Categories : Proto-Indo-European lemmas 
237: Proto-Indo-European roots 
238: Proto-Indo-European CeRC-shaped roots 
239: Proto-Indo-European perfective roots 
242: Proto-Indo-European entries with etymon 
276: Reconstruction:Proto-Indo-European/ bʰerǵʰ- 

###### size
6954 009ed6a3d0d97ac5.txt
```


## [2026-09-05T14:09:10.503Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"###### brahman skt\"; sed -n '1,40p' 8e2cab5cf4272d09.txt | head -5; python3 - <<'EOF'\nt=open('8e2cab5cf4272d09.txt',encoding='utf-8').read()\ni=t.find('Etymology')\nprint(t[i:i+2500])\nEOF"
}
```


### [2026-09-05T14:09:13.785Z] TOOL RESULT

```
###### brahman skt
URL: https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A5%8D%E0%A4%B0%E0%A4%B9%E0%A5%8D%E0%A4%AE%E0%A4%A8%E0%A5%8D
FETCHED: 2026-09-05T14:09:03Z
STATUS: 200
TITLE: ब्रह्मन् - Wiktionary, the free dictionary

Etymology 

 2.3 
 Pronunciation 

 2.4 
 Proper noun 

 2.4.1 
 Declension 

 2.5 
 Proper noun 

 2.5.1 
 Declension 

 2.5.2 
 Derived terms 

 2.6 
 Noun 

 2.6.1 
 Declension 

 2.7 
 Noun 

 2.7.1 
 Declension 

 2.8 
 Descendants 

 2.9 
 See also 

 2.10 
 References 

 Toggle the table of contents 

 ब्रह्मन् 

 8 languages 

 Français 
 Magyar 
 Malagasy 
 Polski 
 Русский 
 संस्कृतम् 
 தமிழ் 
 中文 

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

 Pali
 [ edit ] 

 Alternative forms
 [ edit ] 

 Alternative scripts
 brahman ( Latin script ) 
 𑀩𑁆𑀭𑀳𑁆𑀫𑀦𑁆 ( Brahmi script ) 
 ব্রহ্মন্ ( Bengali script ) 
 බ්‍රහ‍්මන් ( Sinhalese script ) 
 ဗြဟ္မန် or ၿြႁ္မၼ် or ၿြႁ်မၼ် ( Burmese script ) 
 พฺรหฺมนฺ or พรัหมัน ( Thai script ) 
 ᨻᩕᩉ᩠ᨾᨶ᩺ ( Tai Tham script ) 
 ພ຺ຣຫ຺ມນ຺ or ພຣັຫມັນ ( Lao script ) 
 ព្រហ្មន៑ ( Khmer script ) 
 𑄝𑄳𑄢𑄦𑄴𑄟𑄚𑄴 ( Chakma script ) 

 Proper noun
 [ edit ] 

 ब्रह्मन्   m 

 Devanagari script form of brahman (“Brahma”)

 Sanskrit
 [ edit ] 

 Alternative scripts
 [ edit ] 

 Alternative scripts
 ব্ৰহ্মন্ ( Assamese script ) 
 ᬩ᭄ᬭᬳ᭄ᬫᬦ᭄ ( Balinese script ) 
 ব্রহ্মন্ ( Bengali script ) 
 𑰤𑰿𑰨𑰮𑰿𑰦𑰡𑰿 ( Bhaiksuki script ) 
 𑀩𑁆𑀭𑀳𑁆𑀫𑀦𑁆 ( Brahmi script ) 
 ဗြဟ္မန် ( Burmese script ) 
 બ્રહ્મન્ ( Gujarati script ) 
 ਬ੍ਰਹ੍ਮਨ੍ ( Gurmukhi script ) 
 𑌬𑍍𑌰𑌹𑍍𑌮𑌨𑍍 ( Grantha script ) 
 ꦧꦿꦲ꧀ꦩꦤ꧀ ( Javanese script ) 
 𑂥𑂹𑂩𑂯𑂹𑂧𑂢𑂹 ( Kaithi script ) 
 ಬ್ರಹ್ಮೝ ( Kannada script ) 
 ព្រហ្មន៑ ( Khmer script ) 
 ພ຺ຣຫ຺ມນ຺ ( Lao script ) 
 ബ്രഹ്മന് ( Malayalam script ) 
 ᠪᡵᠠᡥᠮᠠᠨ ( Manchu script ) 
 𑘤𑘿𑘨𑘮𑘿𑘦𑘡𑘿 ( Modi script ) 
 ᠪᠷᠠᠾᠮᠠᠨ ( Mongolian script ) 
 𑧄𑧠𑧈𑧎𑧠𑧆𑧁𑧠 ( Nandinagari script ) 
 𑐧𑑂𑐬𑐴𑑂𑐩𑐣𑑂 ( Newa script ) 
 ବ୍ରହ୍ମନ୍ ( Odia script ) 
 ꢨ꣄ꢬꢲ꣄ꢪꢥ꣄ ( Saurashtra script ) 
 𑆧𑇀𑆫𑆲𑇀𑆩𑆤𑇀 ( Sharada script ) 
 𑖤𑖿𑖨𑖮𑖿𑖦𑖡𑖿 ( Siddham script ) 
 බ්‍රහ‍්මන් ( Sinhalese script ) 
 𑩲 𑪙𑩼𑪂 𑪙𑩴𑩯 𑪙 ( Soyombo script ) 
 𑚠𑚶𑚤𑚩𑚶𑚢𑚝𑚶 ( Takri script ) 
 ப்³ரஹ்மந் ( Tamil script ) 
 బ్రహ్మౝ ( Telugu script ) 
 พฺรหฺมนฺ ( Thai script ) 
 བྲ་ཧྨ་ན྄ ( Tibetan script ) 
 𑒥𑓂𑒩𑒯𑓂𑒧𑒢𑓂 ( Tirhuta script ) 
 𑨠𑩇𑨫𑨱𑩇𑨢𑨝𑨴 ( Zanabazar Square script ) 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *bʰerǵʰ- de
```


## [2026-09-05T14:09:16.968Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('8e2cab5cf4272d09.txt',encoding='utf-8').read()\ni=t.find('Proto-Indo-European *bʰerǵʰ- de')\nprint(t[i:i+2200])\nEOF"
}
```


### [2026-09-05T14:09:18.543Z] TOOL RESULT

```
Proto-Indo-European *bʰerǵʰ- der. 
 Proto-Indo-Iranian *bʰráȷ́ʰma 
 Proto-Indo-Aryan *bʰráźʰma 
 Sanskrit ब्रह्मन् 

 From Proto-Indo-Aryan *bʰráźʰma , from Proto-Indo-Iranian *bʰráȷ́ʰma , from a Schwebeablaut form of Proto-Indo-European *bʰerǵʰ- ( “ to become high, rise, elevate ” ) + *-mn̥ .
Literally “growth”, “expansion”, “creation”, “development”, “swelling of the spirit or soul”. Cognate with Latin fortis . The Sanskrit root is बृह् ( bṛh , “ to increase ” ) +‎ -मन् ( -man ) , from the same Proto-Indo-European root above.

 Alternatively, Mayrhofer prefers to derive the word from Proto-Indo-European *bʰreǵʰ- and connect it to Old Norse bragr ( “ poetry ” ) , whence Icelandic bragur ( “ poem; character ” ) .

 An older etymology presented the word as an exact cognate of Latin flāmen ( “ priest ” ) ; however, this is commonly considered spurious by modern authors.

 Pronunciation
 [ edit ] 

 ( Vedic ) IPA ( key ) : /bɾɐ́ɦ.mɐn/ 

 ( Vedic ) IPA ( key ) : /bɾɐɦ.mɐ́n/ 

 ( Classical Sanskrit ) IPA ( key ) : /bɾɐɦ.mɐn̪/ 

 Proper noun
 [ edit ] 

 ब्रह्म॑न् • ( bráhman ) stem ,  n 

 Brahman or the one self-existent impersonal Spirit, the one universal Soul, the Self-existent, the Absolute, the Eternal

 Declension
 [ edit ] 

 Neuter an-stem declension of ब्रह्म॑न् 

 singular

 dual

 plural

 nominative

 ब्रह्म॑ ( bráhma ) 

 ब्रह्म॑णी ( bráhmaṇī ) 

 ब्रह्मा॑णि ( bráhmāṇi ) 
 ब्रह्म॑¹ ( bráhma¹ ) 
 ब्रह्मा॑¹ ( bráhmā¹ ) 

 accusative

 ब्रह्म॑ ( bráhma ) 

 ब्रह्म॑णी ( bráhmaṇī ) 

 ब्रह्मा॑णि ( bráhmāṇi ) 
 ब्रह्म॑¹ ( bráhma¹ ) 
 ब्रह्मा॑¹ ( bráhmā¹ ) 

 instrumental

 ब्रह्म॑णा ( bráhmaṇā ) 

 ब्रह्म॑भ्याम् ( bráhmabhyām ) 

 ब्रह्म॑भिः ( bráhmabhiḥ ) 

 dative

 ब्रह्म॑णे ( bráhmaṇe ) 

 ब्रह्म॑भ्याम् ( bráhmabhyām ) 

 ब्रह्म॑भ्यः ( bráhmabhyaḥ ) 

 ablative

 ब्रह्म॑णः ( bráhmaṇaḥ ) 

 ब्रह्म॑भ्याम् ( bráhmabhyām ) 

 ब्रह्म॑भ्यः ( bráhmabhyaḥ ) 

 genitive

 ब्रह्म॑णः ( bráhmaṇaḥ ) 

 ब्रह्म॑णोः ( bráhmaṇoḥ ) 

 ब्रह्म॑णाम् ( bráhmaṇām ) 

 locative

 ब्रह्म॑णि ( bráhmaṇi ) 
 ब्रह्म॑न्¹ ( bráhman¹ ) 

 ब्रह्म॑णोः ( bráhmaṇoḥ ) 

 ब्रह्म॑सु ( bráhmasu ) 

 vocative

 ब्रह्म॑न् ( bráhman ) 
 ब्रह्म॑ ( bráhma ) 

 ब्रह्म॑णी ( bráhmaṇī ) 

 ब्रह्मा॑णि (
```


## [2026-09-05T14:09:18.887Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('009ed6a3d0d97ac5.txt',encoding='utf-8').read()\ni=t.find('Root')\nprint(t[t.find('*bʰerǵʰ-',i)-200: t.find('Retrieved from')])\nEOF"
}
```


### [2026-09-05T14:09:20.385Z] TOOL RESULT

```
rms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *bʰerǵʰ- ( perfective ) [ 1 ] [ 2 ] [ 3 ] 

 to rise up , ascend 
 Synonyms: *skend- , *kelH- 

 to be elevated , up high 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *bʰerǵʰ- (89 c, 0 e) 

 *bʰérǵʰ-e-ti ( thematic root present ) 
 Proto-Tocharian: *pärkatäre ( “ to rise, come up ” ) [ 4 ] 
 Tocharian A: pärkatäre 

 Tocharian B: pärkatäre 

 *bʰérǵʰ-t ~ *bʰr̥ǵʰ-ént ( root aorist ) 

 *bʰe-bʰórǵʰ-e ~ *bʰe-bʰr̥ǵʰ-ḗr ( reduplicated perfect ) 
 Proto-Indo-Iranian: *bʰabʰárȷ́ʰa 
 Proto-Indo-Aryan: *babʰárźʰa 
 Sanskrit: बबृहाण ( babṛhāṇá , med.part. ) 

 *bʰorǵʰ-éye-ti ( eye-causative ) 

 *bʰr̥ǵʰ-yé-ti ( ye-present ) [ 5 ] 
 Proto-Anatolian: 
 Hittite: 𒈦𒆠𒄿𒀀𒊍𒍣 ( pár-ki-ya-az-zi /⁠parkiyazi⁠/ , “ to ascend ” ) 

 *bʰr̥-né-ǵʰ-ti ~ *bʰr̥-n-ǵʰ-énti ( nasal-infix present ) 
 Proto-Armenian: 
 > ? Old Armenian: բառնամ ( baṙnam , “ to lift up, raise ” ) ( see there for further descendants )

 Proto-Indo-Iranian: *bʰr̥nȷ́ʰáti 
 Proto-Indo-Aryan: *bʰr̥nźʰáti 
 > ? Sanskrit: बृंहति ( bṛṃháti , “ to increase, expand ” ) 

 *bʰérǵʰ-mn̥ ~ *bʰr̥ǵʰ-mén-s 
 Proto-Indo-Iranian: *bʰárȷ́ʰma 
 Proto-Iranian: *bárjman 
 Avestan: 𐬠𐬀𐬭𐬆𐬰𐬌𐬨𐬀𐬥𐬄𐬨 ( bar ə zimanąm , gen.pl. ) [ 6 ] 

 *bʰérǵʰ-ont-s ~ *bʰr̥ǵʰ-n̥t-és 

 *bʰérǵʰ-o-s 

 *bʰérǵʰ-ō ~ *bʰr̥ǵʰ-n-és 
 Proto-Indo-Iranian: *bʰr̥ȷ́ʰnás 
 Proto-Iranian: *br̥jnáh 
 Avestan: 𐬠𐬀𐬭𐬆𐬱𐬥𐬀 ( bar ə šna , inst.m.sg. ) 

 Old Persian: 𐎲𐎼𐏁𐎴𐎠 ( b-r-š-n-a /⁠baršnā⁠/ , inst.m.sg. ) 
 Middle Persian: 
 Manichaean script: 𐫁𐫢𐫗 ( bšn /⁠bašn⁠/ ) 
 Book Pahlavi script: [Book Pahlavi needed] ( bšn /⁠bašn⁠/ ) 

 *bʰérǵʰ-s ~ *bʰr̥ǵʰ-és 

 *bʰérǵʰ-ti-s ~ *bʰr̥ǵʰ-téy-s 
 Proto-Italic: *forktis ( see there for further descendants )

 *bʰérǵʰ-tu-s ~ *bʰr̥ǵʰ-téw-s 
 > ? Proto-Celtic: *brixtus ( “ magical formula, incantation ” ) ( see there for further descendants )

 *bʰérǵʰ-u-s ~ *bʰr̥ǵʰ-éws 

 *bʰr̥ǵʰ-ró-s [ 7 ] 
 Proto-Tocharian: *pärkäre ( “ long ” ) [ 7 ] 
 Tocharian A: pärkär 

 Tocharian B: pärkare 

 *sperǵʰ- ( with s-mobile ) [ 8 ] 

 Unsorted formations 
 > ? Sanskrit: ब्रह्मन् ( bráhman ) ( or related to Old Norse bragr ( “ poetry ” ) ) 

 References
 [ edit ] 

 ^ Pokorny, Julius ( 1959 ), “ bhereg̑h- ”, in Indogermanisches etymologisches Wörterbuch [ Indo-European Etymological Dictionary ] (in German), volume 1, Bern, München: Francke Verlag, pages 140-141 

 ^ Rix, Helmut , editor ( 2001 ), “ *bʰerg̑ʰ- ”, in Lexikon der indogermanischen Verben [ Lexicon of Indo-European Verbs ] (in German), 2nd edition, Wiesbaden: Dr. Ludwig Reichert Verlag, →ISBN , pages 78-79 

 ^ Wodtko, Dagmar S.; Irslinger, Britta; Schneider, Carolin ( 2008 ), “ *bʰerg̑ʰ- ”, in Nomina im indogermanischen Lexikon [ Nouns in the Indo-European Lexicon ]‎ [1] (in German), Heidelberg: Universitätsverlag Winter, pages 30-34 

 ^ Adams, Douglas Q. ( 2013 ), “pärk-”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , page 399 

 ^ Kloekhorst, Alwin ( 2008 ), “parkii̯e/a-ᶻⁱ”, in Etymological Dictionary of the Hittite Inherited Lexicon (Leiden Indo-European Etymological Dictionary Series; 5), Leiden, Boston: Brill, →ISBN , pages 736-737 

 ^ Cheung, Johnny ( 2007 ), “ *barz ”, in Etymological Dictionary of the Iranian Verb (Leiden Indo-European Etymological Dictionary Series; 2), Leiden, Boston: Brill, →ISBN , pages 12-13 

 ↑ 7.0 7.1 Adams, Douglas Q. ( 2013 ), “pärkäre*”, in A Dictionary of Tocharian B: Revised and Greatly Enlarged (Leiden Studies in Indo-European; 10 ), Amsterdam, New York: Rodopi, →ISBN , page 399 

 ^ Hackstein, Olav ( 2023 ), “ When words coalesce II: Preverb incorporation in Indo-European ”, in Indo-European Linguistics , volume 11 , number 1, →DOI , →ISSN , page 21 of 1–40
```


## [2026-09-05T14:09:27.081Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nfor f,k in [('ec3e64fe722f2395.txt','Persian barhaman'),('3ded606778185ce0.txt','Latin fortis')]:\n    t=open(f,encoding='utf-8').read()\n    i=t.find('Etymology',3000)\n    print('#####',k, len(t))\n    print(t[i-200:i+1600].replace('\\n\\n','\\n'))\n    print('======')\nEOF"
}
```


### [2026-09-05T14:09:28.576Z] TOOL RESULT

```
##### Persian barhaman 4075

======
##### Latin fortis 8989
tis ( plural fortes ) 
 ( phonetics ) A fortis consonant.
 Derived terms
 [ edit ] 
 pre-fortis 
 See also
 [ edit ] 
 aqua fortis 
 Anagrams
 [ edit ] 
 sit for , Fritos 
 Latin
 [ edit ] 
 Etymology 1
 [ edit ] 
 From Old Latin forctis , from Proto-Italic *forktis , from Proto-Indo-European *bʰerǵʰ- ( “ to rise, high, hill ” ) (> Proto-Indo-European *bʰérǵʰ-ti-s ) or Proto-Indo-European *dʰerǵʰ- ( “ to bind fast, to be firm, strong ” ) ; in the latter case, an earlier Proto-Italic form of the word *θorktis can be reconstructed. [ 1 ] 
 Alternative forms
 [ edit ] 
 forctis , forctus ( Archaic Latin ) 
 Pronunciation
 [ edit ] 
 ( Classical Latin ) IPA ( key ) : [ˈfɔr.tɪs] 
 ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈfɔr.tis] 
 Adjective
 [ edit ] 
 fortis ( neuter forte , comparative fortior , superlative fortissimus , adverb fortiter ) ; third-declension two-termination adjective 
 ( physically ) strong , powerful 
 Synonyms: praevalēns , potis , potēns , validus , strēnuus , ingēns , firmus , compos 
 Antonyms: dēbilis , languidus , aeger , fractus , īnfirmus , tenuis , obnoxius , inops 
 Adeō fortis erat ut arborēs pugnō excīderet. He was so strong that he could cut down trees with his fist. 
 ( figuratively ) firm , resolute , steadfast , stout 
 Synonyms: fīxus , tenāx , inexōrābilis , obstinātus 
 ( figuratively ) courageous , brave 
 Antonym: imbēcillus 
 8 CE , Ovidius , Fasti 1.493–494 : omne solum fortī patria est, ut piscibus aequor,
ut volucrī, vacuō quicquid in orbe patet. Every land is home to the brave , as to fishes the sea,
as to birds for every void whatsoever in the open world. 
 ( figuratively ) manly , mannish ( corresponding to the Greek ἀνδρεῖος ) 
 Declension
 [ edit ] 
 Third-declension two-termination adjectiv
======
```


## [2026-09-05T14:09:32.855Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,60p' ec3e64fe722f2395.txt"
}
```


### [2026-09-05T14:09:32.888Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%85%D9%86
FETCHED: 2026-09-05T14:09:03Z
STATUS: 200
TITLE: برهمن - Wiktionary, the free dictionary

برهمن - Wiktionary, the free dictionary 

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
 Persian 

 Toggle Persian subsection
```


## [2026-09-05T14:09:35.741Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in e3b3ff4b309a2e94 3ae7f25932ee1cd3 8997266b77b21809 b6723f326757c9c4; do echo \"##### $f\"; python3 -c \"\nimport sys;t=open('$f.txt',encoding='utf-8').read()\ni=t.find('TITLE')\nprint(t[i:i+1400])\n\"; done"
}
```


### [2026-09-05T14:09:37.643Z] TOOL RESULT

```
##### e3b3ff4b309a2e94
TITLE: Bourgeois - Etymology, Origin & Meaning

Bourgeois - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App 

 Dark
 Auto
 Light

 Terms of Services Privacy Policy 

 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of bourgeois 

 bourgeois (adj.) 

 1560s, "of or pertaining to the French middle class," from French bourgeois , from Old French burgeis, borjois "town dweller" (as distinct from "peasant"), from borc "town, village," from Frankish *burg "city" (via Germanic from PIE root *bhergh- (2) "high," with derivatives referring to hills and hill-forts).

 The word was later extended to tradespeople or citizens of middle rank in other nations. The sense of "socially or aesthetically conventional; middle-class in manners or taste" is from 1764. Also (from the position of the upper class) "wanting in dignity or refinement, common, not aristocratic." As a nou
##### 3ae7f25932ee1cd3
TITLE: Burglar - Etymology, Origin & Meaning

Burglar - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of burglar 

 burglar (n.) 

 "one who commits robbery by breaking into a house," 1540s, shortened from Anglo-Latin burglator (late 13c.), earlier burgator , from Medieval Latin burgator "burglar," from burgare "to break open, commit burglary," from Latin burgus "fortress, castle," a Germanic loan-word akin to borough .

 The unetymological -l- is perhaps from influence of Latin latro "thief" (see larceny ). Middle English had burgur (c. 1200), from Old French burgeor , burgur , also housbreker (c. 1400). Burglar-alarm is by 1840.
 also from 1540s 

 Entries linking to burglar 

 borough (n.) 

 Old English burg , burh "a dwelling or dwellings within a fortified enclosure," from Proto-Germanic *burgs "hill fort, fortress" (source also of Old Frisian burich "castle, city," Old Norse borg "wall, castle," Old High German burg , buruc "fortified place, citadel," German Burg "castle," Gothic baurgs "city"), which Watkins derives from from PIE root *bhergh- (2) "high," with derivatives referring to hills, hill forts, and fortified elevations.

 In German and Old Norse, chiefly as "fortress, castle
##### 8997266b77b21809
TITLE: Borough - Etymology, Origin & Meaning

Borough - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of borough 

 borough (n.) 

 Old English burg , burh "a dwelling or dwellings within a fortified enclosure," from Proto-Germanic *burgs "hill fort, fortress" (source also of Old Frisian burich "castle, city," Old Norse borg "wall, castle," Old High German burg , buruc "fortified place, citadel," German Burg "castle," Gothic baurgs "city"), which Watkins derives from from PIE root *bhergh- (2) "high," with derivatives referring to hills, hill forts, and fortified elevations.

 In German and Old Norse, chiefly as "fortress, castle;" in Gothic, "town, civic community." The meaning shifted in Old English from "fortress," to "fortified town," then simply "town" (16c., especially one possessing municipal organization or sending representatives to Parliament). In some U.S. states (originally Pennsylvania, 1718) often an incorporated town; in Alaska, however, it is the equivalent of a county. As "one of the five administrative divisions of New York City," it dates from the consolidation of 1898; in London, its use dates from the London Government Act of 1899.

 The Scottish form is burgh . The Old 
##### b6723f326757c9c4
TITLE: Harbor - Etymology, Origin & Meaning

Harbor - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of harbor 

 harbor (n.) 

 "lodging for ships; sheltered recess in a coastline," early 12c., a specialized sense of Middle English herberwe "temporary dwelling place, quarters, lodgings; an inn; the camp of an army in the field," probably from Old English here-beorg (West Saxon), *here-berg (Anglian) "lodgings, quarters," from Proto-Germanic compound *harja-bergaz "shelter, lodgings," from *heri "army, host" (see harry (v.)) + *burzjan- "protection, shelter" (from PIE root *bhergh- (1) "to hide, protect"). Perhaps modeled on Old Norse herbergi "room, lodgings, quarters."
 also from early 12c. 

 harbor (v.) 

 Old English herebeorgian "take up quarters, lodge, shelter oneself" (cognate with Old Norse herbergja , Old High German heribergon , Middle Dutch herbergen ), verbal formation from here-beorg "lodgings, quarters" (see harbor (n.)). Meaning "give shelter to, protect" is from mid-14c. Figuratively, of thoughts, etc., from late 14c. Related: Harbored ; harboring .

 Entries linking to harbor 

 harry (v.) 

 Old English hergian "make war, lay waste, ravage, plunder," the word used in the A
```


## [2026-09-05T14:09:52.272Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('AHD_watkins1985.txt',encoding='utf-8',errors='replace').read()\ni=t.find(\"bhergh-'. To hide, protect\")\nprint(t[i:i+900])\nprint('---- HARBOR occurrences ----')\nimport re\nfor m in re.finditer(r'HARBOR', t):\n    print(repr(t[m.start()-300:m.start()+60]))\n    print()\nEOF"
}
```


### [2026-09-05T14:09:54.077Z] TOOL RESULT

```
bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-berga
---- HARBOR occurrences ----
'army. 1. Old English here, army: HERIOT. 2. Old French herban, a summoning to military service: ARRI- ERE-BAN. 3. Compound *haryja-bergaz, “army hill,” hill- fort, later shelter, lodging, army quarters (*bergaz, hill; see bhergh-?), in: a. Old English herebeorg (> Middle English herberwe), lodging: HARBOR; b. Old French herberge, lodging: HARBINGER. 4. Compo'

'ALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas'
```


## [2026-09-05T14:10:03.639Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT borough/burgess/fort ===\"; grep -n \"^BOROUGH\\|^Borough\\|borough, sb\\|BURGESS\\|^FORT\\|fort, sb\\|Fort, \" SKT.txt | head -10; echo; grep -n -i \"brahmin\\|Brahman\" SKT.txt HJB.txt | head -10"
}
```


### [2026-09-05T14:10:03.700Z] TOOL RESULT

```
=== SKT borough/burgess/fort ===
1217:bustard,  a  bird.  (F.  -  L.)  Fonnerly also  hiuard  (Sherwood).  —  O.  F.  bistarde» '  a  bustard  ; '  Cot.  Mod.  F.  ou/an/^.  —  L. a$iu  larJa.xHovr  bird  (Fliny.  N.  H.x.  33). Cf.  Fort,  abctariiaf  also  SeiarJa,  a  buhtard. ^  Both  O.  F.  Hxtardt  aiid  F.  outarUe  are from  auit  tarda ;  in  the  former  case,  initial 0  is  dropped;  in  the  Utter,  outardt  stands for  an  older  vrntardi^  where  9us  ^  L.  awiV. See  Dirt.
6988:Fort,  Fortaiice;  see  Force  (i).
11122:Marjoram,  a  phnt.  (F.  -  L.  *  Gk.) M.  E.  tNaJoroH  (without  r).  —  F.  mtarjc- laine,  of  which  an  older  form  must  have been  marjoimnt  ♦.  Cf.  Ital.  oiajontnat Span,  mayerana,  Fort,  maicranat  m.irjo ram.  Low  L.  majortua;  variously  cor- rupted from  L.  antaraau.^QV.  u^pairvf, marjoram.
20162:ribute.  sb.    (F.-L.>     ME.  tribut. ^  tribut,  tribute.  *L.  tributitnt,  tribute, a  ibtujj  paid ;  ncul.  of  pp.  of  fribucre, iiv^tfn  10  a  Uibe,   to  assign.  pay.  —  L, !»*-/,  B  ifiLte. ribrach  ;  see  Tri-. ribul&tion;  sec  Trie«. rtbiine.  Tribute :  sec  Tribe, [ioe  1 1 ),  a  bhort  space  of  time.    (Span.) tlie  phr.  in  a  /nVv.  — Span,  en  un  tris, I  Iricc^   to  an   install  ,    from  trt't,  the be   maite    by  llie   cracking   of  glass,   a ikf   an    instant.      So    aUo   Fort,  tn't, 'king  of  glass,  a  crash,  craclc,  instant; Um  trii.  in  a  trice.     Prob.  of  imitative ftn ;  bat  kc  Traah.

SKT.txt:2185:BRAHMAN.
SKT.txt:23630:Sanskrit',  avatar,  banyan,  brahmin  (brah- man), champak,  pundit,  lajnb,  Sanskrit^ nittec,  Veda.
HJB.txt:1210:words.  The  author  had  his  information from  a  Brahman  named  Pftdmanaba {Pcuinuinahha^f  who  knew  Dutch,  and who  gave  him  a  Dutch  translation  of Bhar&ihari's  Satakas,  which  is  printed at  the  end  of  the  book.  It  is  tne  first translation  from  Sanskrit  into  an  Euro- pean language  (A.B.).
HJB.txt:2236:1860. — "  The  Azyan  tribes  in  conquering India,  urged  by  the  Brahmans,  made  war against  uie  Turanian  demon-worship,  but not  always  with  complete  success.  — Dr, J.  Wilton,  in  L^fe,  450.
HJB.txt:2329:[c.  1590.— "In  the  citv  of  Sambal  is  a temple  called  Hari  Mandal  (the  temple  of Vishnu)  belonging  to  a  Brahman,  from among  whose  descendants  the  tenth  avatar will  appear  at  this  spot." — Aln,  tr.  Jarrett,
HJB.txt:2943:1771. — ".  .  .  being  employed  to  con- struct a  militiuy  work  at  the  fort  of  Trip- lasore  (afterwards  called  Marsden's  Bastion) it  was  necessary  to  cut  down  a  baajran-toee which  so  incensed  the  brahmans  of  that place,  that  they  found  means  to  poison nim"  («.«.  Thomas  Marsden  of  the  Madias Engineers).— ifm.  of  W.  Marsden^  7-8.
HJB.txt:2960:"Un  Joumaliste  allemand  a  aocustf  M. Casimir  Delavig^ne  d'avoir  pris  pour  un  arbre une  secte  religieuse  de  I'lnde.  ..."  The German  journalist  was  wrong  here,  but  he might  have  found  plenty  of  matter  for ridicule  in  the  play.  Thus  the  Brahmins (men)  are  Ahbar  (!),  Idamore  {!!),  and Empsael  (!!!);  their  women  NSala  (f),  Zaid« (!),  andAftr2a(!l).
HJB.txt:3973:111         BRAHMIN,  BRAHMAN.
HJB.txt:3998:c.  A.D.  150. — "But  the  evil  stars  have  not forced  the  Brahmina  to  do  evil  and  abomin- able things;  nor  have  the  ^^ood  stars  per- suaded the  rest  of  the  (Indians)  to  abstain from  evil  things." — Bardeganes,  in  CfureUm't Spicilegium,  18.
HJB.txt:4010:BRAHMIN Y  BULL.
```


## [2026-09-05T14:10:05.072Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== IEC bergh ===\"; grep -n \"bhergh\\|b̑ergh\\|bergh-\" IEC.txt | head -15; echo \"=== SYN high/hill ===\"; grep -n \"brhant\\|bṛhánt\\|bərəzant\" SYN.txt IEC.txt | head -10"
}
```


### [2026-09-05T14:10:05.136Z] TOOL RESULT

```
=== IEC bergh ===
1236:bherghó, ið “protect, save, foster. WP II, 172 Skt. barhe “cover (zero-grade in brhami 'strengthen"); Oss. cf. ám-bürzín (‘cover’, fr. *som-bherghio); OHG bergan, OE beorgan; Du. bergen; ON bjarga beside birgja; Sw. ber- ga sig “manage; refrain’; OCS brégo, brěšti *care for, protect
1237:bherghos 'strong place' (identified in Gmc. with bhergh- and bhréh-, q.v.) W cf. bre “hill, top? (fr. *bhregh-); MHG berc, -ges ‘bulwark, enclosure’; OE beorg *protec- tion, refuge’; ON cf. birgr (*well-provided', fr. *-ghio-); OCS brégü (*shore, bank’. LW?); Slovene cf. breg “hill, rise, coast'. Cf. Go. baírgan ‘guard’ and bherghó
1781:bhrghəlos ‘hold, holder’. See next, and cf. bherghö (WP II, 172) Br. bréol “iron hook on cart-axle; MHG bürgel ‘surety’
1782:bhrgho, ið “hold, fasten, enclose’. Cf. bherghó (WP II, 172) | Skt. -brhami ‘strengthen’, beside e-gde barhe ‘cover’ and Oss. åm-bårzin, id.; Tokh. A pär- kàw-, B páürko- ‘gain’; Gk. phrásso beside phárkhma &  phrágma; MHG borgen ‘watch, care for; ON byrgja ‘enclose’. An extended form appears to be OLat. fraxare ‘patrol’ (*r) w. sim. long-zero in Alb. brez *girdle; wall-brace'; Dac. substr. briu, id. in Rumanian. Noun-forms include Go. baürgs *walled city, tower' and com. Gmc.; E borough and burrow; OCz. brh ‘lair, den, camp’; mod. Cz. *hencoop, fowling-net’. (The question of an Anatolian equivalent of type *bhurgh- is discussed in SF: baürgs, cf. the Gk. forms pürgos, and (Hes.) phürkos "wall The Cz. placename suffix -brh is said to mean “hill?). Av. borezis ‘cover’ shows secondary palatalism. See next
1794:bhr&hont- (bhrghnt-, bhrghont-) ‘high; height’. WP II, 172. See bhr£&hus & bhergh- Skt. brhát; Av borezafit; Oss. bárzond, pl. bärzändtä; Per. buland, baland; Tokh. A -párkant (B oärk park, pirko) ‘sunrise’; Lat. frons, gp frontium (Ennius: pl. frundes) (forehead, gravity, severity'. For the seman- tics cf. OCS čelo 'forehead': Li. kéin “to raise); Osc. cf. Frunter (name of a god); Gaul. brigantes 'hillmen'; Olr. bríanda *fa- mous’; OBr. cf. brientin ‘noble’; OW breint, braint, „brein, bryein ‘privilege, state’; W braint, id.; Frankish *burgunds; OE brant: ON brattr (variant: *bhrghond-). See next
1795:bhrghus, os “high; height’. WP II, 172. See bhr&hont-, bhergh-. WP II, 172 Skt. cf. brhát; Av. borozoó; Oss. (o-gde. Am- big. bardz, barz ‘mass, crowd': (?) Arm. bardz (2) “hip, thigh’; Arm. bardzr, gs. bardzu ‘high’; Tokh. A cf. párkár, B parkre long; Hitt. parkus; Olr. brí ‘noble’ beside Ir. brigh ‘virtue, power; Sequanian brig- “high — of winds’; Gaul (ambig.) briga Ch, But cf. bhrgh-); W brí, Cor. bry ‘rank, degree, esteem’; OW bry ‘above’: (?) MHG bor ‘up’. Cf. the e-gde forms in Arm. erkna-berdz ‘high as heaven’, lerna-berdz ‘high as a moun- tain’, and OE brego “ruler”.
=== SYN high/hill ===
SYN.txt:992:Dan. bjerg, Sw. berg, OE beorg (‘moun- tain, hill’ and ‘burial mound’, in former sense replaced by the Fr. forms, in the latter sense NE barrow), OHG, NHG berg, etc., the most widespread Gmce. word for ‘mountain’ (but ON bjarg ‘rock, precipice’; in Goth. only bazrga- het = dpewh ‘hill country’) : Skt. brhant- ‘high, great’, Av. barazant- ‘high’, bara- zah- ‘height, mountain’, Arm. berj ‘height’, Ir. bri, ace. brig, W., Br. bre ‘hill’. Walde-P. 2.172 ff. Falk-Torp 77.
SYN.txt:7598:Lat. fortis (more commonly of mental strength, ‘brave’, but also and orig. used of physical strength and in this sense > It. forte, Fr. fort, Sp. fuerte), fr. forctis (Festus), prob.: Av. dragaite ‘holds’, ChSI. driiZati ‘hold’, guttural ex- tensions of IE *dher- in Skt. dhr- ‘hold, support’, ete. Walde-P. 1.859. Ernout- M. 382f. Otherwise (fr. *bhergh- in Skt. brhant- ‘great, mighty, high’, Ay. barazant- ‘high’, etc.) Walde-H. 1.535 ff.
SYN.txt:21781:Avy. barazant- (also baraz-, baraziman-) : Skt. brhant- ‘high, tall’, but mostly ‘great, strong’, Ir. bri, W. bre ‘hill’, : bjarg, OHG berg ‘mountain’, etc. Walde- P. 2.172.
SYN.txt:26305:“rah Du. luid Skt. —_- ucca-, mahant-, Ir ar Ai ; nt, Ni, ard OHG (hA)lit brhant-, tara- V eine] MHG lut, hel Av. barazant- Br uhel NHG laut
SYN.txt:26317:Fr. haut, Sp. alto (esp. of the voice, speech, etc.); Ir. ardd, NIr. ard, W. uchel, Br. uhel; ON har, Dan. hgj, Sw. hég; Skt. ucca-, and brhant-, Av. bara- zant-.
SYN.txt:32861:4. Goth. baurgs, ON borg (also ‘for- tress, castle’), OF burg, ME burgh (NE borough), OHG burg, MHG burc (also ‘fortress, castle’, as NHG burg), all, ex- cept Goth., in earliest use ‘fortified place’, either as ‘place of refuge’ : OF beorgan, OHG bergan ‘shelter’; or else as ‘height? : OF beorg, OHG berg, etc. ‘mountain’, Skt. brhant-, Av. barazant- ‘high’, etc. Walde-P. 2.173. Feist 85 f. Falk-Torp 94. Weigand-H. 1.308 f. Kluge-G. 87. NED s.v. borough.
SYN.txt:33152:3. W. brenin : W. bry ‘high’, Ir. bri, W. bre ‘hill’, Skt. brhant- ‘great, high’ (cf. fem. brhatt-, Ir. Brigit ‘the exalted one’), Av. barazant- ‘high’, ete. Walde-P. 2.173. Pedersen 1.100.
```


## [2026-09-05T14:10:18.792Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW burgus ===\"; grep -n \"burgus\" LEW_1910.txt LAT.txt | head -10; echo \"=== LEW fortis alt spellings ===\"; grep -n \"forctus\\|fortis,\" LEW_1910.txt | head -5; echo \"=== KLN burgus/bourgeois ===\"; grep -n \"^bourgeois\\|^burgess\\|^bourg,\" KLN_1966.txt | head"
}
```


### [2026-09-05T14:10:18.875Z] TOOL RESULT

```
=== LEW burgus ===
LAT.txt:7964:burgus, -I a.: b.lat., e.g. Vig., Mil.4,10, castellum paruulum que*
LAT.txt:7969:Mot ivideaaent geraanique; la glose TiupyoC haec turris, burgus ,
LAT.txt:7970:CGL II 436,46; 570,94 burgus, turris est un rapprocheaent de lettri.
LAT.txt:7971:V. toutefois E. Penninck, L'origine helldnique de "burgus", Latoaua
=== LEW fortis alt spellings ===
=== KLN burgus/bourgeois ===
5447:bourgeois,  n.,  a  size  of  printer’s  type  (print).  — Named  after  Bourgeois,  a  French  type  founder, bourgeoisie,  n.,  middle  class.  —  F.,  fr.  bourgeois.
```


## [2026-09-05T14:10:19.714Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== RCH برهمن ===\"; grep -n \"برهمن\" RCH.txt | head -5; echo \"=== HJB Brahmin entry ===\"; sed -n '3973,3998p' HJB.txt"
}
```


### [2026-09-05T14:10:19.781Z] TOOL RESULT

```
=== RCH برهمن ===
=== HJB Brahmin entry ===
111         BRAHMIN,  BRAHMAN.
»  bouts  duquel  ae  mettent  5  ou  6  oorteurs a'on  appelle  Bon^"— <SdMit«m^,  I  otyage,  i.
168
a.
1785.— "The  boys  with  Colonel  Law- renoe's  palankeen  having  straggled  a  little ont  of  the  line  of  march,  were  ]ncked  up  b^ the  Morattas." — Carracciolt^  Life  of  Clive,  i. 207.
1804.— "My  palanquin  boys  will  be  laid on  Uie  road  on  JAond&y. ''—Wellington,  iii.
1809.— "My  b(^  were  in  high  spirits, laughing  and  singing  through  the  whole night."— I,rf.  Val^iUia,  i.  326.
1810. — "The  palankeen-bearers  are  called Bhoii,  and  are  remarkable  for  strength  and swiftnees.  "—i/aria  Grukam,  128.
BOYA,  8.  A  buoy.  Sea  H. (Rodmck).  FMr.  Skeat  adds:  "The Malav  word  is  also  boya  or  hai-rop, which  latter  I  cannot  trace."]
CBOYANORE,  BAONOB,  s.  A corr.  of  the  Malayal.  VdUunavar, *  Ruler.'     ,
[1887.— "Somewhere  about  1694-95  .  .  . the  Kadattunad  Baja,  known  to  the  early English  as  the  BoyajLore  or  Baonor  of Baoagara,  was  in  sexni-independent  pcMises- sion  of  Kaduttanad,  that  is,  of  the  territory lying  between  the  Mah^  and  K5tta  rivers." —Logany  Man.  qf  McUaJbatj  i.  345.]
BBAB,  s.  The  Palmyra  Tree  (see PALKTBA)  or  Borassus  Jlabelliformds, The  Portuguese  called  this  Palmeira InaTa  ('wild'  palmX  whence  the English  corruption.  The  term  is  un- known in  Bengal,  where  the  tree  is called  'fan-palm,'  'palmyra,'  or  by  the H.  name  tdl  or  tdr,
1623.— "The  book  is  made  after  the fsahion  of  this  country,  t.e.  not  of  paper whi<^  is  seldom  or  never  used,  but  of  palm leaves,  vis.  of  the  leaves  of  that  which  the Portuguese  call  pdlmnm  brama  (nc),  or  wild vahnT—P.  della  Voile,  ii.  681 ;  [Hak.  Soo. 57291].
c.  1666.— "  Tons  l6s  Malabares  invent comme  nous  de  gauche  k  droit  sur  les feulUes  des  Palmtrtu  Bn,ynM."—Thevenot, V.268.
1673.— "Another  Tree  called  Brabb, bodied  like  the  Oocoe,  but  the  leaves  grow round  like  a  Peacock's  Tail  set  upright."— rryar,  76.
1760.— "Brabb,  so  called  at  Bombav: Pdlmira  on  the  coast ;  and  Tall  at  Bengal." — /«f,  458.
o.  1760. — "There  are  also  here  and  there interspersed  a  few  brab-trees,  or  rather  wild palm-trees  (the  word  brab  being  derived  from Bxabo,  which  in  Portuguese  signifies  wild) .  .  .  tike  chief  profit  from  that  is  the  toddy." — 6^tMe,i.48.
[1808.— See  quotation  under  BANDABEE.]
1809.— "The    Palmyra  .  .  .  here   called
the   brab,    furnishes    the   best   leaves   for
thatching,  and  the  dead  ones  serve  for  fuel."
— Maria  Oraham,  5.
BBAHMIN,  BBAHMAN,  BBA- MIN,  s.  In  some  parts  of  India called  Bahman;  Skt.  Brdhmana. This  word  now  means  a  member  of the  priestly  caste,  but  the  original meamng  and  use  were  different. Haug.  {Brahma  und  die  Brat^momen, pp.  8-11)  traces  the  word  to  the  root &m,  'to  increase,'  and  shows  how  it has  come  to  have  its  present  significa- tion. The  older  English  form  is •Rrfti^htna.iij  which  comes  to  us  through the  Greek  and  Latin  authors.
c.  B.C.  830.—**.  .  ,  tQv  i¥  Ta^CkoLS (ToifMrTiay  Idetv  S6o  ^njffl,  Bpaxf'S^fas  i/t4>0' ripow,  rdv  fikv  irpeap&repw  i^vpnuUvoy,  riot Hk  ycibrepop  KOfiifTrp^,  au^xnipois  3*  axoKov- $€iv  futdTfrds  .  .  .**-- ArisuAultu,  quoted in  Siraho,  xv.  c.  61.
c.  B.C.  800.— "'AXXiyi'  ^  SuUpeaiw  irouU nu  irepl  rCap  <f>iKoff6^iaif  8i^  yiwrf  ipdffKW, Cfif  Tois  fUp  Bpaxf^oipas  KoKel,  roifs  S^ Tapfidi^as  [Zapfikvas^y — From  Megaathcnes^ in  Strabo,  xv.  c.  69.
c.  A.D.  150. — "But  the  evil  stars  have  not forced  the  Brahmina  to  do  evil  and  abomin- able things;  nor  have  the  ^^ood  stars  per- suaded the  rest  of  the  (Indians)  to  abstain from  evil  things." — Bardeganes,  in  CfureUm't Spicilegium,  18.
```


## [2026-09-05T14:10:29.419Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7960,7975p' LAT.txt; echo \"=== KLN burgess/faubourg ===\"; grep -n \"burgess\\|faubourg\\|burgh,\" KLN_1966.txt | head -6"
}
```


### [2026-09-05T14:10:29.484Z] TOOL RESULT

```
cpopTopaoTtxxTrjC ?
Le mot n'apparait que sous 1 'Eapire, et doit etre eaprunti; Burdd,
Burdonus, Burdonianus seabie appartenir i 1 1 onoaastique celtique; d'aa-
tre part la double flexion est aussi en faveur d'une origine celtique.
burgus, -I a.: b.lat., e.g. Vig., Mil.4,10, castellum paruulum que*
burgum uocant} Oros., Hist .7,33,13, crebra per limitem habitacula
constituta burgos uulgo uocant (scii. Burgundiones, qui inde dicti
putantur). M.L.1407. Iri. boree, britt. borc'h, bourch’is.
Dirivi: burgdrius.
Mot ivideaaent geraanique; la glose TiupyoC haec turris, burgus ,
CGL II 436,46; 570,94 burgus, turris est un rapprocheaent de lettri.
V. toutefois E. Penninck, L'origine helldnique de "burgus", Latoaua
IV, p.5 et s.
buricus (-ichus; burricus) -i a.: bourrique, petit cheval; syneny-
ae de mannus. Mot bas lat. et vulg., cf. Porph., Hor. C.3,37,7, manni equi
dicuntur pusilli quos uulgo buric(h)os uocant. On trouve aussi dans
=== KLN burgess/faubourg ===
5381:borough,  n.  —  ME.  burgh,  burwe,  fr.  OE.  burg, burh,  burg,  rel.  to  OS.,  OFris.,  burg,  ‘castle’, ON.  borg,  ‘wall,  castle’,  MDu.  burch,  borch, borcht,  Du.  burchl,  burg,  OHG.  burg,  burc, buruc,  ‘fortified  place,  citadel’,  MHG.  burc, G.  Burg,  ‘castle’,  Goth,  baurgs,  ‘city’,  OE.  beorg, etc.,  ‘mountain’.  These  words  prob.  derive  fr. I.-E.  base  *bhergh-,  ‘high’,  whence  also  Arm. berj,  ‘high  place',  OSlav.  bregu,  ‘bank  (of  a river)’,  W.  bera,  ‘stack,  pyramid’,  Mir.  bri,  acc. brig,  ‘hill’,  Toch.  A  parkas,  ‘long’,  Hitt,  parkush, ‘high’,  OI.  bfhdnt-,  Avestic  blrlzant-,  ‘high’, OCeltic  Brigantes,  lit.  ‘the  high  ones’  (cp.  Bur¬ gundians,  fr.  Late  L.  Burgundiones,  lit.  ‘high¬ landers’),  prob.  also  OL.  forctus,  ‘good’,  L. fortis  (fr.  OL.  forctis),  ‘strong’,  see  Walde-Hof- mann,  LEW.,  I, pp.  535-36,  s.v. fortis, and  Kluge- Mitzka,  EWDS.,  p.67,  s.v.  Berg.  Cp.  barrow, ‘mountain,  mound’,  bourgeois,  burgage,  burgess, burgh,  burgrave,  Burgundy,  canterbury,  faubourg, gaussbergite,  ghetto,  Hapsburg,  hauberk.  Cp.  al¬ so  Brahma,  fort,  and  the  second  element  in  bar- bicane.  Cp.  also  the  suff.  -bury  in  English  place names,  which  comes  fr.  OE.  byrig,  the  dative sing  of  OE.  burg.  Base  *bhcrgh-  is  prob.  an  en¬ larged  form  of  base  *bher-,  ‘to  carry,  lift’.  See bear,  ‘to  carry’.
5446:F. ,  fr.  bourg,  ‘small  town’,  hence  prop,  meaning ‘inhabitant  of  a  bourg’;  of  Teut.  origin.  See borough  and  cp.  burgess.  Cp.  also  burgee.
5897:burgee,  n  ,  a  small  pennon  used  by  yachts  and merchant  vessels  for  identification.  —  Orig. ‘owner’s  pennon’,  fr.  OF.  burgeis  (F.  bourgeois) in  burgeis  (F.  bourgeois)  d’un  navire,  ‘owner  of a  ship’;  see  bourgeois.  In  English,  the  s  of  OF. burgeis  was  mistaken  for  the  plural  suff.  For other  words  similarly  treated  see  pea. burgeon,  n.,  bud.  —  ME.  borjoun,  burjon,  fr.  OF. burjon  (F.  bourgeon),  fr.  VL.  *burribnem,  acc.  of *burrib,  fr.  Late  L.  burra,  ‘flock  of  wool’  (see bureau);  so  called  because  the  buds  of  many trees  have  a  hairy,  shaggy  appearance, burgess,  n.,  citizen  of  a  borough.  —  OF.  burgeis (F.  bourgeois),  fr.  Late  L.  burgensis,  fr.  Teut. *burg,  ‘town’.  See  borough  and  cp.  burgher.  Cp. also  bourgeois.
5898:burgh,  n.,  1)  a  borough;  2)  in  Scotland,  an  in¬ corporated  town.  —  A  var.  of  borough  (q.v.) Derivatives:  burgh-al,  adj.,  burgher  (q.v.) burgher,  n.,  1)  freeman  of  a  burgh;  2)  a  citizen.  — Prob.  fr.  Du.  burger,  ‘citizen’,  fr.  MDu.  burgher, fr.  MHG.  burgzere,  burger  (whence  G.  Burger), fr.  OHG.  burgari ,  fr.  OHG.  burg,  ‘castle,  cit¬ adel,  city’;  influenced  in  form  by  E.  burgh.  See borough  and  agential  suff.  -er. burglar,  n.  —  ML.  burgulator,  burglator,  a hybrid  lit.  meaning  ‘town  thief’.  The  first  ele¬ ment  is  a  Teut.  loan  word  (see  borough),  the second  is  traceable  to  L.  latro,  gen.  -onis,  ‘thief, robber’;  cp.  OF.  ler,  lerre,  acc.  laron  (whence  F. larron),  and  see  larceny.
14451:Derivatives:  fatuous-Iy,  ad v.,  fatuous-ness,  n. faubourg,  n.,  outskirts,  suburb.  —  ME  .faubourg, fabour,  fr.  MF.  faux  bourg  (F.  faubourg),  fr. OF.  forsbourc,  lit.  ‘that  which  is  outside  of  the town",  fr.  OF.  pref.  fors,  ‘outside’  (fr.  L.  forts) and  bourc,  ‘town’;  see  forum  and  borough.  The change  of  OF.  forsbourc  to  F.  faubourg  (MF. faux  bourg),  lit.  ‘a  false  town",  is  due  to  folk etymology;  the  suburb  was  looked  upon  as  a not  genuine  town.
```


## [2026-09-05T14:10:30.342Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON برهمن ===\"; grep -n \"برهمن\" MON_part1.txt MON_part2.txt | head -8"
}
```


### [2026-09-05T14:10:30.394Z] TOOL RESULT

```
=== MON برهمن ===
MON_part1.txt:22918:می‌دهند. ضح.- معرب این کلمه نیز «برهمن»
```


## [2026-09-05T14:10:40.462Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '60,200p' ec3e64fe722f2395.txt"
}
```


### [2026-09-05T14:10:40.499Z] TOOL RESULT

```
 1.1 
 Pronunciation 

 1.2 
 Etymology 1 

 1.2.1 
 Noun 

 1.3 
 Etymology 2 

 1.3.1 
 Proper noun 

 1.4 
 Further reading 

 Toggle the table of contents 

 برهمن 

 3 languages 

 فارسی 
 Malagasy 
 پښتو 

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

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: برهمن 

 Wikipedia fa 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ba.rah.ˈman/ 

 ( Dari, formal ) IPA ( key ) : [bä.ɾäɦ.män] 

 ( Dari, formal ) IPA ( key ) : [bä.ɾäɦ.män] 
 ( Kabuli ) IPA ( key ) : [bä.ɾɑː.män] 

 ( Hazaragi ) IPA ( key ) : [bä.ɾɔː.män] 

 ( Iran, formal ) IPA ( key ) : [bæ.ɹæɦ.mæn] 

 ( Tajik, formal ) IPA ( key ) : [bä.ɾäɦ.män] 

 Rhymes: -an 

 Readings

 Classical reading ? 

 barahman

 Dari reading ? 

 barahman

 Iranian reading ? 

 barahman

 Tajik reading ? 

 barahman

 Etymology 1
 [ edit ] 

 Ultimately from Sanskrit ब्राह्मण ( brāhmaṇa ) .

 Noun
 [ edit ] 

 بَرَهمَن • ( barahman ) ( plural بَرَهمَنان ( barahmanān / barahmanân ) , or بَراهِمه ( barâheme ) , Tajik spelling бараҳман ) 

 brahmin ( member of Hindu priestly caste ) 
 c. 1650 , Čandra Bhān, دیوان برهمن [ The Brahman 's divan ]: برهمن از لب هندی نژادان نکته می‌سنجد، زبان پارسی و ترکی و تازی نمی‌داند. barahman az lab-e hendi nežâdân nokte mi-sanjad, zabân-e pârsi va torki va tâzi ne-mi-dânad. [This] brahman weighs his subtle wits with lips of Hindi lineage; he knows not the Persian nor the Turkish nor the Arabic tongue. 

 Etymology 2
 [ edit ] 

 Ultimately from Sanskrit ब्रह्मन् ( brahman ) .
```


## [2026-09-05T14:10:41.029Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '22910,22925p' MON_part1.txt"
}
```


### [2026-09-05T14:10:41.080Z] TOOL RESULT

```
برهم. 02۲1 (رص‌ مر .) فراهم امده» 
مسسجتمع. . شسوریده» مشوش. بریشان» 
مضطرب. ۳ و برهم: شوریده و مشوش. 
برهمائی: 92:2۸:3 (ص‌نسد.) منسوب 
به برهماء پیرو فرقة برهمایی. 
سس همن: 02721۳0027 (ص. .) بشوای 
روحانی آیین برهمایی و آنان یکی از سه 
طبقهً مردم را در آیین برهمایی تشکیل 
می‌دهند. ضح.- معرب این کلمه نیز «برهمن» 
3ج ان «براهمه» است. 
ببس رهنه: ۶006 (ص.) لخت» عریان. 
بی حجاب؛ نایوشیده. بی‌معاش. 
برهوت: 02۳2۳0 [- بلهوت] (اخ.) وادیی 
است در حضر موت. چاه مشهور به «بثر 
برهوت» در جوار وادی برهوت در دامنهة 
کوهی آتشفشانی واقع است که گویند
```


## [2026-09-05T14:10:58.217Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B1%DA%98%D9%88%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/burg\" \\\n \"https://www.etymonline.com/word/iceberg\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 93, Bhergh part 2: Persian بورژوا < French bourgeois; Gmc *burg; iceberg\" ; done 2>&1 | tail -5"
}
```


## [2026-09-05T14:10:59.788Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD/WEB bourgeois ===\"; grep -n -m3 \"bourgeois,\" FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -6; echo \"=== WEB burgus/borough ===\"; grep -n -m2 \"burgus\" WEB_vol1.txt FSD_vol1.txt | head"
}
```


### [2026-09-05T14:11:05.021Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0c78e031adf264d3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d89c9557ad5064f9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9cd5254aeb883ae7.txt
```


### [2026-09-05T14:11:05.089Z] TOOL RESULT

```
=== FSD/WEB bourgeois ===
WEB_vol1.txt:109512:long prim/@r, a size of type between small pica and bourgeois, 10 point.
=== WEB burgus/borough ===
WEB_vol1.txt:25047:4. the concentration of gomave pareau: u’reau-crat (-rō-), n. [fro: 1. an official ay fp lzom bureaucracy, _ 2. an official who follows and ins} inflexible routine, proper forms ea on an bii-reau-crat’ic, bi-reau-crat/jc-Al es, etc, SSR i es by bureaucracy.’ a. 1, of - Of, like, orc isti s b or bureaucrats. aracteristic of a bureaucrat u-reau-crat/i-cal-ly, adv. in a bure manner. aucratic bi-reauc’ra-tist (-rok’ra-), n. on ee or supports bureaucracy pares n. ay as burrel. u-re’6, n. [Sp., from Fr. bur x Spanish wie court in ETR m ing to the royal household are tried SEE bi-rette’, bi-ret’, n. [Fr., dim. of OFr, by; a eee — buire, to drink.] Te PUs . in chemistry or physic glass tube for ASIE em RE haud or fas: It is pf even bore, stands ven ically, with a small apertu a fitted with a stopcock. perture belom gandia 2. a decorated cruet. biir’fish, vn. a fish found along the Atlantic coast of North America, capable of expand- ing its body, which, being covered with spines, presents the appearance of a chestnut bur, whence the name: called also balloon fish, swell fish, and porcupine fish. birg, 7 (ME. burgh; AS. burh, burg, a fortified town. 1. originally, a fortified town. 2. a city, town, or village. [Colloq.] “borg, a suffix meaning burg or borough, as in Vicksburg: also -burgh, as in Pittsburgh. biir-gade’, n. a bourgade. [Obs.] birg’age, n. [ME. burgage, from burg, a town. in law, a former system of tenure of rea estate, held at a fixed rate of rent payable in money or in services; socage. biir’gall, n. a small sea fish, the cunner, blue perch, or nibbler. [Dial.] bur’sga-mot, n. same as bergamot. biir’ga-net, n. a burgonet. biir’gee, 7. [origin unknown.) _. 1. a sort of small coal for firing furnaces. [Brit.] 3 y 2. an identifying flag on a ship, triangular or swallow-tailed in shape. p biir-geois’ (-jois’), n. same as bourgeots. biir’ge6n, 2. (ME. burgen, burgeon; OFr. ber jon, c bud; O.H.G. burjan, to raise, lift up. a bud; a sprout. r būr’ģeðn, v.i. and v.t. burgeoned, $t. bP burgeoning, ppr. to put forth (buds, etc.); sprout. ra -burg/ér, [from hamburger.] a combining form meaning sandwich of ground meal (and), steakburger, cheeseburger, etc. [Slang. js, 2 būr’ğess, n. [OFr. burgeis; LL. buree TG. citizen; burgus, a borough, town; ~ burc, a fortified town.] h 1. a citizen or freeman of a boroug™ ough, 2. in England, a representative Oe ‘aritish corporate town, Or university 1n the Parliament. ; 3. a magistrate of certain Corpor ar 4. before the American Revolution, #1 tire sentative in the lower house of the cere title of Maryland or Virginia, which bore House of Burgesses. jance wee wate a solemn oath of otlan: formerly taken by the burgesses © of a but- biir’gess:ship, 7. the state OF office i gess. birg/grave, n. a burgrave. 4 biirgh (biirg), n. 1. a boroug [Bae 7. in Scotland, an incorporate
WEB_vol1.txt:25079:peaks, n. [OFr. burg, from LL. burgus, a town, and OFr, lere, from L. latro, a thief.] one who commits burglary. ,
```


## [2026-09-05T14:11:10.978Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nt=open('0c78e031adf264d3.txt',encoding='utf-8').read()\ni=t.find('Persian')\nprint(t[t.find('From Wiktionary'):t.find('From Wiktionary')+1200])\n\""
}
```


## [2026-09-05T14:11:11.940Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nt=open('9cd5254aeb883ae7.txt',encoding='utf-8').read()\ni=t.find('Origin and history')\nprint(t[i:i+900])\n\""
}
```


### [2026-09-05T14:11:13.096Z] TOOL RESULT

```
d
```


### [2026-09-05T14:11:14.829Z] TOOL RESULT

```
Origin and history of iceberg 

 iceberg (n.) 

 1774, "glacier humped like a hill;" 1820 as "detached piece of a glacier or ice pack at sea," partial loan-translation of Dutch ijsberg , literally "ice mountain," from ijs "ice" (see ice (n.)) + berg "mountain" (from PIE root *bhergh- (2) "high," with derivatives referring to hills and hill-forts.). Similar formation in Norwegian isberg , Danish isbjerg .

 Earlier English terms were sea-hill (1690s), island of ice (1610s). Phrase tip of the iceberg in a figurative sense (in allusion to most of it being unseen underwater) first recorded 1962. Iceberg lettuce attested from 1893, apparently originally a trade name.
 also from 1774 

 Entries linking to iceberg 

 ice (n.) 

 Old English is "ice, piece of ice" (also the name of the Anglo-Saxon rune for -i- ), from Proto-Germanic *is- "ice" (source also of Old Norse iss , Old Frisian is , Dut
```


## [2026-09-05T14:11:19.948Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -6 0c78e031adf264d3.txt; wc -c 0c78e031adf264d3.txt; grep -c \"Wiktionary does not yet have\" 0c78e031adf264d3.txt"
}
```


### [2026-09-05T14:11:19.994Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B1%DA%98%D9%88%D8%A7
FETCHED: 2026-09-05T14:11:04Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found162 0c78e031adf264d3.txt
0
```


## [2026-09-05T14:11:22.197Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%A8%D9%88%D8%B1%DA%98%D9%88%D8%A7/\" --note \"page 93 node 8: Mo'in/Dehkhoda entry for بورژوا (French bourgeois)\" 2>&1 | tail -2"
}
```


### [2026-09-05T14:11:27.266Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/adf29ec9eef61ece.txt
```


## [2026-09-05T14:11:29.611Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nt=open('adf29ec9eef61ece.txt',encoding='utf-8').read()\nimport re\ni=t.find('بورژوا',500)\nprint(len(t))\nprint(t[i-200:i+1500])\n\""
}
```


### [2026-09-05T14:11:31.637Z] TOOL RESULT

```
5041
۵ م . ) یکی از مسببان ایجاد جامعه ملل .
شخص متمول، سرمایه دار، ارباب، شهرنشین
۱ - شهری شهرنشین ( که در سابق ازحقوق مخصوص بر خوردار بود ) . ۲ - شهر نشین مرفه و ثروتمند . ۳ - ارباب مخدوم . ۴ - متعلق به بورژوازی . 

 فرهنگ معین

 [ فر. ] (ص . ) ثروتمند، دارندة سرمایه و ابزار تولید. 

 فرهنگ عمید

 ۱. شخص متمول، سرمایه دار.
۲. ارباب.
۳. شهرنشین دارا و مرفه. 

 فرهنگستان زبان و ادب

 {bourgeois} [علوم سیاسی و روابط بین الملل] فرد متعلق به طبقۀ شهرنشین و مالک وسایل تولید 

 پیشنهاد کاربران

 " رای : rāy " در زبانِ اوستاییِ کُهن به چمِ " سرمایه، دارایی، ثروت، تمول " بوده است که برابرِ آن در زبانِ پارسیِ میانه - نو نیز" رای: rāy " بوده است و برابرِ آن در زبانِ آلمانی " Reichtum" می باشد. 
در زبانِ اوستاییِ جوان واژه یِ " رَئیوَنت : raē'vant " به چمِ 
 ... [مشاهده متن کامل] 
1 - " سرمایه دار، دارا ، غنی، ثروتمند، متمول " و برابر با " reich " در زبانِ آلمانی
2 - " باشکوه، مجلل، شکوهمند، شکوهمندانه، فاخر " و برابر با " praechtig " در زبانِ آلمانی
3 - " باشکوه، پُر زرق و برق، زرق و برق دار، شکوهمند " و برابر با " prunkvoll " در زبانِ آلمانی
بوده است. ( برای نمونه بنگرید به یَشت : Yt. 7. 5 - Yt. 8. 32 - Yt. 12. 1 ، وَندیداد: V. 20. 1 ، یَسنا : Y. 12. 1 ، سی روچَگ : S. 2. 9 ) 
برابرِ این واژه در زبانِ پارسیِ میانه "رایومند: rāyōmand " و " ریوَند: rēvand " بوده است. 
همچنین در زبانِ اوستاییِ جوان واژه یِ " رَئیوَ : raē'va " بعنوانِ دگرریختی از واژه یِ " رَئیوَنت " آمده است که برابرِ این واژه نیز در زبانِ پارسیِ میانه " رایومند" بوده است. ( برای نمونه بنگرید به یسنا : Y. 22. 24 ) 
" رایومند" ساختواژه ای بمانندِ " تنومند، هستومند و. . . " دارد که از پسوندِ " - ومند" ساخته شده اند. ( ریختِ دیگرِ این پسوند در زبانِ پارسی " - مَند "می باشد. ) 
نکته : واژه یِ اوستاییِ " رَئیوَنت : raē'vant "
```


## [2026-09-05T14:11:51.653Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor i in range(15180,15240):\n    if re.match(r'^\\s*\\d{2,4}\\s*$', lines[i]):\n        print('pagemark',i,lines[i].strip())\nprint(lines[15222][:80])\nEOF"
}
```


### [2026-09-05T14:11:53.460Z] TOOL RESULT

```
pagemark 15193 613
pagemark 15231 614
forte,  n.,  a  strong  point.  —  F.  fort ,  ‘strong’.  See fort.  For  the  a
```


## [2026-09-05T14:11:53.480Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN barahman ===\"; grep -n -i \"barahman\\|brahman\" HRN.txt HUB.txt | head -5; echo \"=== ARY برهمن ===\"; grep -n \"برهمن\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== ARY BRAHM ===\"; grep -n -i \"BRAHM\\|BHERGH\" incoming/ARY/ARY_latin_index_pages.txt | head -5"
}
```


### [2026-09-05T14:11:53.550Z] TOOL RESULT

```
=== HRN barahman ===
=== ARY برهمن ===
=== ARY BRAHM ===
605:(SUTRA) 117.0 y(BRAHMANS)thilasl yp y(VEDAS) cla yx nape De 5 ts Le
943:VAISYA tlnyy 9 (3L,s& >) KASHATRIVA ih sLisy 9 (3 sly) BRAHMAN
```


## [2026-09-05T14:12:03.572Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"bherefih\\|bhereĝh\\|bheregh\\|bhereg^h\\|brhánt\\|bfhánt\" WLD_Bd2_pages.txt | head -10; echo \"=== find page 173 ===\"; grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -3"
}
```


### [2026-09-05T14:12:03.630Z] TOOL RESULT

```
=== find page 173 ===
```


## [2026-09-05T14:12:05.721Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls -la; head -3 WLD_Bd2_pages.txt; echo \"---\"; grep -n -i \"bhereg\\|bherg\" WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-05T14:12:05.795Z] TOOL RESULT

```
total 146212
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  2993454 Sep  4 14:06 WLD_Bd1_1930_dli_70244_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 42256714 Sep  4 14:06 WLD_Bd1_1930_dli_70244_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4327601 Sep  4 14:06 WLD_Bd1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2417287 Sep  4 14:06 WLD_Bd2_1927_dli_106624_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 94865800 Sep  4 14:06 WLD_Bd2_1927_dli_106624_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2833963 Sep  4 14:06 WLD_Bd2_pages.txt
                ALOIS WALDE


---
8744:mit dfc. Burg, s. u. bhergh- „hoch'') erwiesen. Endlich lett. branhfi „fest
10556:   Ygl. die verwandten Wzformen bhrH (bhrlig, -l\ s, dort aucb iiber bherg),
10618:        vorstehn“,   bhrm „Kante''; bhergh ..hoclr' (bhrendhos ,,Hirsch'‘??).    Vgl.
10945:blier     scheinen bhereg, bhcrek- „glanzen'*, Persson Beitr, 6S9a                              1.
11055:bherek- „glanzen‘‘, gleichwertig mit bhereg- ds.                    (s. d.,   auch wegen doppel-
11057:   ai.   bhrdcafe „flammt, leuchtet^^ (unbelegt:            s.   u. bhereg-);    ob dazu bhr<^a-h
11114:bhereg- „glanzen,                         wozu auch der Birkenname.                      Gleichwertig           rait
11134:se.^'Basis %her9g- eben auf *bhereg- weist, sich als zshangend erweisen.
11178:                                         bhemg-    — bherg-                                                     17J
11187:  Forraen, die fur die Wz. *bhereg- eine leichte Nebenform bliertg- sichern
```


## [2026-09-05T14:12:09.412Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && sed -n '11230,11330p' WLD_Bd2_pages.txt"
}
```


### [2026-09-05T14:12:09.458Z] TOOL RESULT

```
vorliegenden Yokalverschiedenheiten erinnern Ts. d. auch iiber den frag-
wiirdigen Versuch etymologischer Yerkniipfung beider Gruppen     die aus                            ),

Wzvariation oder versch. Schallnachahmung erklart w*erden:
  gr.   (pQvyi/.og ,,ein    kleinerer Yogel*'           (Persson 860          a. 2         erw*agt mit sehr
zw. Rechte Umstellung aus "^fpgiyidMg                   lat.   frig -)
  lat. frigo^ -ere ..quietschen (von kleinen Kindern/*, frigultio, -Ire „zwit 3 chern

(von Yogeln), lispeln**, fringulio^ fringulHo ds.. frigulo -are ..schreien f'von
der Dohle/', fringilla ..Fink. Sperling**:
172                                            bhergh-   — bhergh-
     russ. bcrglez^ „Stieglitz“,             skr, brglijes      „Sitta syriaca“,     cech. brhel „Pirol,
Goldamsel“           mahr. ,,Specht“ ^nicht nach Suolahti Dt Vogeln. 173 aus dt.
Firol),        poln. bargiel ,;Art Meise“ (Niedermann BB. 25, 295, Yf. LEWb.^ s.
YV.,    Berneker 119).
     tiber         ai.   bhrioga-h   s.   u. bJirem-;    lat.   frigo nicht nach Wood IF. 22, 152
zu     lit.    br'eziti      „kratze'^    aisL brik „Brett‘',     lat.   frh,   frico.   Ahnliche, aber
gewiS jiingere Schallworte sind lat. merulus frindlt, lit. (Fickl^ 497) bnz-
geti „bloken, meckern, brunimen“.


tohergh „bergen, yerwahren^.
     Got. bairgan „bergen, verwahren'',                   aisl.   bjarga, ags. beorgan, ahd. bergan,
as.gi-bergan ,,bergen‘^; abl. ags. byrgan „begi'aben‘', byrgels, as. burgisli
„Begrabnis“ und ahd. bor{a)gen ,,sich wovor hiiten, sich woYor in Sicher-
heit bringen, acht worauf haben, schonen, anvertrauen, borgen“, ags. borg 'mn
„behuten, borgen“. (tJber Burg s. u. "^bhergh- „hoch“).       Slav. %crgq (Lit.    —
bei Zup. 9, 177) in aksl. bregq, breHi ,,sorgen“ in nebresti „vernachlassigen“,
russ. beregil,  bere(h ..hiiten, bewahren, schonen, sparen“, skr. alter brzem,
        „bewachen, bewahren, sorgen; feiern^'; abl. (und die Annahme Hirts
PBrB. 23, 332 von Entlehnung des ursl. %ergq aus dem germ, widerlegend)
klr. oboHh, gen. oboroJia ,,Heuschober'', tech, brah „Heuschober, Haufen“,
poln. brog „Scheune, SchobeF' (Berneker 73j; schwundstufig c. brJi „Hohle,
Hiitte, Zelt'^ (Berneker 49 m. Lit.).     Ostlit. birgmti „sparen‘* (Trautmann
Bsl. Wb. 31 nach Buga). Mcht hierher ir. commairge ,,Burgschaft, Biirgen^^
(Stokes KZ. 41, 383 irrig '^'kom-borgia), Meringers IF. 18, 262 Anreihung
von av. hdrdjaya- ,,willkominen heifien, huldigen^' (angeblich aus „*bergen,
in sein Heim aufnehmen^), bdrdyda- „wiilkommen, geschatzt, teuer', be-
ruht auf ebenso unveidaBlicher Konstruktion der av. Gdbed. wie seine
Bedeutungsangabe idg. ^bhergh „H6hle“ (s. Berneker 49 und zu den av.
Worten auch 69, sowie Bthl. Wb. 945, 957).             Sind die av. Worte tat-
sachlich verwandt, so kame man etwa auf eine starker gefiihlsmaBige
Gdbed. ,,mit liebevoller Sorge w^orauf sehen“ (woraus ,,bewillkommnen,
freundlich aufnehmen^’j und konnte selbst die arisebe Gruppe av. bjr^g^
f. „religioser Branch, religiose Form, Eitus^’',
                                                  ai. brJias-ixiti-h m. „Herr dea
Gebets^* Toder: brdhmmi-rj damit zu vermitteln versuchen. Doch ist eine
solche Gdbed. rein konstruiert und rein sinnliches „zudecken, bergen“ das.
durch die europ. Sprachen einzig sicherzustellende.            Fiir av. bdr9jaya-^
borjxda- kommfe iibrigens auch Verwandtschaft mit aksl. blag-o „guk‘' unter
idg. bhelgb- in Betracht fFick       94, s. auch Berneker 69;.


bhergh-      ,,hoch, erhoben“, vielleicht Erw. von blier- (,,tragen) heben’^ (s.
        dort die Gruppe von dt. empor) oder von bher „hervorstehn“, s. Pers-
        son Beitr. 21            A
                        5, 607 A 2.
   Ai. Kaus. barhaya 2. sg. ,,auge!-' vermutlich barha-s, -m
                                                                ,,Schwanzfeder,
Schwanz eines Yogels, bes. beim Pfau“ (Persson Beitr. 926; ahnliche Bed.
in Ai. Biirzel     b^do ..Hiigel’* s. u. bher „hervorstehn*‘)
                         :
                                                              ;
                                                                brhanf-’ ,.gro6,
hoch, erhaben, hehr*, auch ,,hoch, laut, von der Stimme, fern, brhail
                                                                              ir.                  (=
Brigif, germ. Bitrgimd), av. bmzant- (np. bidand),                         f.   bdrdzaiti „hoch-^, in Zs.
bdrazi-       (:   %9r9zra-j, b^r^z- ,,hoch** und ,,H6he, Berg'* (= np. burz ds..                      bri;
                                                                                                 ir.
                                                bhergh-                                             173


der      Nom. av, bars subst. kann ar. -ar-, aber auch ar. -r- enthalten, s. Bthl.
IF. 9, 261), hochstufig av. barozayeni                 ,,ich will   aufw’achsen ]assen“ bardzan-
m. bardzali- n. „Hohe'', bardsnu- m. „Erhebimg, Hohe, Himmel, Kopf', bars-
zyah- „h6her‘‘, bardzlsta- „der hochste, hochstgelegene*':                          np. bCil-a ,,Hohe^‘
i^barz-), biirz        (s. o.).

   Ai. brhant- bedeutet              auch „gro6, gewaitig, dick, massenhaft'' und brm-
Ifiati   ist .,macht feist,                                         brhdna Adv. „dicht,
                                  kraftigt, starkt, vermehrt, fordert**,
fest,    derb, tiichtig; sehr, durchaus^' paribrdJia-h                  ,,feststehend, dicht, solid**,
und zwar nach Fick        493 f. und bes. Solmsen KZ. 37, 575 f. durch Zu-
sammenfliefien mit bhelyh- „schwellen*\     Sollte daher lat. for(c)tis nach
Bgm. BSG\Y. 1897, 21fiF., Persson Beitr. 51 f. unserem ^bheryh- entstammen,
ware es nicht auf Grund dieser ai. Bedeutungen als „gedmngen, stark'* zu
verstehn, sondern als „hochgewachsen, daher robust'': doch s. iiber fortis
wahrscheinlicheres u. ^dher-,              dliereyli-    „halten'\
   Arm. bcrj ,,Hohe" in crlcna-,              Icrna-berj ,,himmeh,           berghoch" {^bherghcs),
barjr ,,hoch" {bhrghiU)^ Qiam-)barnam i^barjnam^ aor. barji) ,,hebe auf usw.
(s. u. bhrenlc- „bringen“, wo gegen Verb, init dt. br ingen), Hiibschmann Arm.

Gr. I, 428, Bthl. Wb. 949 f.:
   lat. foric)tis (?) s. o.

   Cymr. bera „IIaufe'‘ (= dt Berg), acorn,  bret. bern ds. {-rglt-n-l s. Peder-
sen      KG. I   1                schwundstufig mir. bri, Acc. brig ,,Hugel*'
                     05), gall. Bergtisln,
(s. 0 .), cymr. bry ..hoch, oben", fern. cymr. corn. bret. bre „Hugel'', gall.
Admageto-briga, LitanG-briga u. a. OK.. Arcbrigimn OK. (..in monte si turn").
Brigiani Alpenvolk (..monticolae*'); gall. Briganfes, Bolyavreg Yolksname
```


## [2026-09-05T14:12:24.987Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-05T14:12:25.026Z] TOOL RESULT

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


## [2026-09-05T14:12:26.507Z] TOOL CALL #62: Bash

```json
{
 "command": "sed -n '80,160p' tools/verify_check.py"
}
```


### [2026-09-05T14:12:26.570Z] TOOL RESULT

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


## [2026-09-05T14:12:30.586Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-91.json'))\nprint(json.dumps({k:v for k,v in d.items() if k!='entries'},ensure_ascii=False,indent=1))\ne=d['entries'][0]\nprint(json.dumps({k:v for k,v in e.items() if k!='nodes'},ensure_ascii=False,indent=1)[:1500])\nprint(json.dumps(e['nodes'][0],ensure_ascii=False,indent=1)[:1800])\n\""
}
```


### [2026-09-05T14:12:32.427Z] TOOL RESULT

```
{
 "pdf_page": 91,
 "book_page": 61,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05"
}
{
 "entry": 0,
 "root": "Bher 5, Bheru, Bhereu, Bhreu, Bhru 2",
 "verdict": "confirmed",
 "modern_form": "PIE *bʰer- 'to boil, seethe, well up' with its u-extension *bʰrewh₁- / *bʰer(e)u- 'to boil, brew'",
 "note": "Nourai's five variant names correspond exactly to the two Pokorny lemmata he cites: IEW 132-133 '2. bher- etwa \"aufwallen\", von quellendem oder siedendem Wasser (auch vom Aufbrausen beim Gähren, Kochen, sowie vom Feuer) \"sich heftig bewegen\"; oft mit u-Formans', and IEW 143-145 'bh(e)reu- : bh(e)rū-, Erw. von 2. bher-, \"sich heftig bewegen, wallen, bes. vom Aufbrausen beim Gären, Brauen, Kochen usw.\"' — so 'Bher 5' = Pokorny's bher-2, 'Bheru/Bhereu/Bhreu/Bhru 2' = his bh(e)reu- : bh(e)rū-. Watkins (AHD) fuses them into one entry, bhreu-2 'To boil, bubble, effervesce, burn; with derivatives referring to cooking and brewing. [Pok. bh(e)reu- 143, 2. bher- 132]'. Wiktionary reconstructs *bʰrewh₁- 'to boil, to brew', explicitly 'Extension of *bʰer- (to boil)'. Language label (Indo-European) and gloss ('to boil, bubble') are both right; only the numbering is Nourai's own.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *bʰer- «جوشیدن، فوران کردن» و گسترش «واوی» آن *bʰrewh₁- (نوشتار کهن‌تر: bh(e)reu-) «جوشیدن، آبجو پختن». آنچه نورایی زیر پنج نامِ Bher 5، Bheru، Bhereu، Bhreu و Bhru 2 آورده، همان دو مدخل پوکورنی است: bher-2 در صفحهٔ ۱۳۲–۱۳۳ و bh(e)reu- : bh(e)rū- در صفحهٔ ۱۴۳–۱۴۵؛ واتکینز در پیوست فرهنگ American Heritage این دو را در یک مدخل bhreu-2 «جوشیدن، حباب زدن، سوختن
{
 "id": 1,
 "lang": "Persian",
 "words": "balvâ",
 "verdict": "disputed",
 "derivation": "Persian بلوا balvā 'riot, tumult, uproar' is treated by every Persian lexicon as an Arabic loan. Dehkhoda: 'بلوا. [بَلْ] (از ع، اِ) بلوی. زحمت (غیاث اللغات). مشقت' ('from Arabic; = balwā; trouble, hardship'); Mo'in — the very reference Nourai cites — 'بلوا (بَ) [ع. بلوی] (اِ.) ۱- شورش، آشوب. ۲- سرکشی'. The Arabic source is بَلْوَى balwā, a maṣdar of the root ب ل و b-l-w 'to test, try, afflict' (same root as بلاء balāʾ 'trial, affliction'), the sense shifting in Persian from 'ordeal, calamity' to 'disturbance, riot'. Nourai's Indo-European derivation rests solely on Mann, IEC 116, whose parenthetical lemma reads '(bhru-, see bheru-. Z-gde radical in Per. balwà \"tumult\" …)'; Mann is alone in this, and no Iranian etymological dictionary (Horn, Hübschmann, Cheung, Hasandust) knows a Persian verb *balv-/*burv- 'to boil'. Phonetically an inherited zero-grade *bʰru- would not yield NP balv- (cf. the genuine reflexes MP/NP burr-, borr- of *bru-). The chart's own NOTE records the conflict; modern scholarship sides with Mo'in.",
 "derivation_fa": "«بلوا» در فارسی وام‌واژه‌ای عربی است، نه واژه‌ای ایرانی. دهخدا آن را «(از ع، اِ) بلوی. زحمت. مشقت» می‌داند و معین — همان مأخذی که نورایی به آن ارجاع می‌دهد — می‌نویسد: «(بَ) [ع. بلوی] (اِ.) ۱- شورش، آشوب. ۲- سرکشی». اصل آن بَلْوَی عربی از ریشهٔ «ب ل و» به معنی «آزمودن، گرفتار کردن» است (هم‌ریشه با «بلاء»)، و تحول معنایی «گرفتاری، آزمون» ← «آشوب» در فارسی رخ داده است. تنها پشتوانهٔ نورایی مدخل مان (IEC ۱۱۶) است که این واژه را درجهٔ صفر ریشهٔ *bʰreu- «جوشیدن» گرفته؛ این رأی در ریشه‌شناسی ایرانی هواداری ندارد و از نظر آوایی نیز *bʰru- در فارسی «بلو-» نمی‌دهد. پس پژوهش امروزی ادعای نورایی را رد می‌کند.",
 "sources": [
  "https://abadis.ir/fatofa/%D8
```


## [2026-09-05T14:14:02.235Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -4 d89c9557ad5064f9.txt; wc -c d89c9557ad5064f9.txt; python3 -c \"\nt=open('d89c9557ad5064f9.txt',encoding='utf-8').read()\ni=t.find('Etymology')\nprint(t[t.find('Proto-West Germanic',2000):t.find('Proto-West Germanic',2000)+700])\""
}
```


### [2026-09-05T14:14:04.036Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/burg
FETCHED: 2026-09-05T14:11:04Z
STATUS: 200
TITLE: Reconstruction:Proto-West Germanic/burg - Wiktionary, the free dictionary
4585 d89c9557ad5064f9.txt
Proto-West Germanic terms derived from the Proto-Indo-European root *bʰerǵʰ- 
 Proto-West Germanic terms derived from Proto-Germanic 
 Proto-West Germanic terms inherited from Proto-Germanic 
 Proto-West Germanic terms inherited from Proto-Indo-European 
 Proto-West Germanic terms derived from Proto-Indo-European 
 Proto-West Germanic terms derived from the Proto-Indo-European root *bʰergʰ- 
 Proto-West Germanic lemmas 
 Proto-West Germanic nouns 
 Proto-West Germanic feminine nouns 
 gmw-pro:Buildings 
 Proto-West Germanic consonant stem nouns 

 Hidden categories: Pages with etymon 
 Proto-West Germanic entries with etymon 
 Pages with entries 
 Pages with 1 entry 

 This page was last edi
```


## [2026-09-05T14:14:06.947Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 -c \"\nt=open('d89c9557ad5064f9.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+900])\""
}
```


### [2026-09-05T14:14:08.620Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 This Proto-West Germanic entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-West Germanic
 [ edit ] 

 Etymology
 [ edit ] 

 From Proto-Germanic *burgz .

 Noun
 [ edit ] 

 *burg   f [ 1 ] 

 fortification 

 ( fortified ) city 

 Inflection
 [ edit ] 

 Consonant stem

 Singular

 Nominative

 *burg 

 Genitive

 *burgi 

 Singular

 Plural

 Nominative

 *burg 

 *burgi 

 Accusative

 *burgu 

 *burgi 

 Genitive

 *burgi 

 *borgō 

 Dative

 *burgi 

 *burgum 

 Instrumental

 *burgi 

 *burgum 

 Derived terms
 [ edit ] 

 *burgwari 

 *haubidaburg 

 Descendants
 [ edit ] 

 Old English: burg , burh , burug , burhg Middle English: burgh Scots: burch , burgh 
 English: borough , -borough , Brough , boro , bur
```


## [2026-09-05T14:19:46.900Z] TOOL CALL #66: Bash

```json
{
 "command": "mkdir -p \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\" && cat > \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build93.py\" <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_ROOT = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0er%C7%B5%CA%B0-\"\nW_BRAHMAN = \"https://en.wiktionary.org/wiki/%E0%A4%AC%E0%A5%8D%E0%A4%B0%E0%A4%B9%E0%A5%8D%E0%A4%AE%E0%A4%A8%E0%A5%8D\"\nW_BARAHMAN = \"https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D9%87%D9%85%D9%86\"\nW_FORTIS = \"https://en.wiktionary.org/wiki/fortis\"\nW_BURG = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-West_Germanic/burg\"\nE_BOURGEOIS = \"https://www.etymonline.com/word/bourgeois\"\nE_BURGLAR = \"https://www.etymonline.com/word/burglar\"\nE_BOROUGH = \"https://www.etymonline.com/word/borough\"\nE_HARBOR = \"https://www.etymonline.com/word/harbor\"\nE_ICEBERG = \"https://www.etymonline.com/word/iceberg\"\nABADIS = \"https://abadis.ir/fatofa/%D8%A8%D9%88%D8%B1%DA%98%D9%88%D8%A7/\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1,\n \"lang\": \"Sanskrit\",\n \"words\": \"brhant; brahman\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Skt. bṛhánt- 'high, great, lofty' (f. bṛhatī́) is the textbook reflex of *bʰérǵʰ-ont-s: Indo-Iranian *bʰarȷ́ʰant- with the palatal *ǵʰ giving Indo-Aryan h, exactly matching Av. bərəzant- 'high' (> NP boland/بلند) and Hitt. parku- 'high'; the zero grade *bʰr̥ǵʰ- appears in the Sanskrit root bṛh-/bṛṃháti 'to grow, make strong, increase'. That word is secure. bráhman- n. 'sacred formulation, prayer, religious devotion' is the uncertain half: Wiktionary derives it from a Schwebeablaut form of *bʰerǵʰ- + *-mn̥ ('growth, expansion, swelling of the spirit'), which is Nourai's picture and also Kent's (Old Persian brazmaniya- 'prayerful' is built to the pre-Indo-Iranian antecedent of Skt. bráhman-, 'to pIE root *bhergh-', Kent p.201, following Henning TPS 1944.108-18); but Mayrhofer prefers *bʰreǵʰ- with Old Norse bragr 'poetry', Klein calls the word 'of uncertain origin; possibly related to OI. bṛhánt-', and Walde-Pokorny II 173 warns that the Sanskrit bṛh- senses partly reflect a confluence with *bʰelǵʰ- 'to swell' (Fick, Solmsen). The old equation with Latin flāmen is now abandoned. Hence: bṛhant- confirmed, brahman- plausible; the node takes the weaker verdict.\",\n \"derivation_fa\": \"سنسکریت bṛhánt- «بلند، بزرگ، والا» بازماندهٔ بی‌چون‌وچرای *bʰérǵʰ-ont- هندواروپایی آغازین است؛ در دورهٔ هندوایرانی *bʰarȷ́ʰant- شده و «ǵʰ» کامی در هندوآریایی به h بدل گشته، درست همانند اوستایی bərəzant- «بلند» که خودِ «بلند» فارسی از آن است. ستاک درجهٔ صفر *bʰr̥ǵʰ- نیز در ریشهٔ سنسکریت bṛh- «رشد کردن، نیرومند ساختن» دیده می‌شود. اما دربارهٔ bráhman- «وِرد و نیایش مقدس» اختلاف هست: کنت (ص ۲۰۱) و ویکی‌واژه آن را از همین ریشه با پسوند ‎*-mn̥‎ می‌گیرند (پارسی باستان brazmaniya- «نیایشگر» گواه آن است)، ولی مایرهوفر آن را به *bʰreǵʰ- و واژهٔ نورس کهن bragr «شعر» می‌بندد و والده-پوکورنی (ج۲ ص۱۷۳) از آمیختگی معنایی با ریشهٔ *bʰelǵʰ- «آماسیدن» سخن می‌گوید. پس ادعای نورایی دربارهٔ bṛhant- درست و دربارهٔ brahman- با احتیاط پذیرفتنی است.\",\n \"sources\": [W_ROOT, W_BRAHMAN],\n \"ref_check\": [\n   {\"ref\": \"KLN:194\", \"status\": \"supports\", \"note\": \"Klein 1966, leaf carrying pp.193-194 (KLN_1966.txt line 5510) s.v. 'Brahma, Brahman': 'OI. brahman- (neut.), \\\"prayer, the universal soul, the Absolute\\\" ... of uncertain origin; possibly related to OI. bṛhánt-, \\\"high\\\", fr. I.-E. base *bhergh-, \\\"high\\\". See borough.' — Nourai's arrow, but Klein flags it as uncertain.\"},\n   {\"ref\": \"KNT:201\", \"status\": \"supports\", \"note\": \"Kent, Old Persian, Lexicon p.201 (KNT.txt line 5748, between the running heads 'LEXICON 199' and '201'): 'brazmaniya- adj. \\\"prayerful, reverent\\\" ... deriv. to pAr. antecedent of Skt. bráhman- \\\"religious devotion, prayer\\\" ... to pIE root *bhergh- (see OP bard-)'. Nourai's gloss 'religious devotion, prayer' is copied verbatim from this page; p.200/201 s.v. bard- vb. 'be high': 'Av. barəz- \\\"high\\\", NPers. burz \\\"high\\\", Skt. bṛhánt- \\\"lofty\\\", OHG berg \\\"mountain\\\", pIE *bhergh-'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp.140-141 s.v. bʰereĝh-\", \"stance\": \"supports\", \"note\": \"'Old Indic ... brhant- \\\"big, large, high, convex, elevated, noble, sublime\\\" ... fem. brhatī (= Irish Brigit, Germanic Burgund), Avestan bərəzant- (npers. buland)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 172-173 s.v. bhergh- 'hoch, erhoben'\", \"stance\": \"partial\", \"note\": \"'ai. ... brhant- \\\"groß, hoch, erhaben, hehr\\\" ... av. bərəzant- (np. buland)' — supports bṛhant-, but adds that the further senses of bṛhánt-/bṛṃháti arose 'durch Zusammenfließen mit bhelgh- \\\"schwellen\\\"' (Fick, Solmsen KZ 37,575), i.e. the semantics behind brahman- are not purely from this root.\"},\n   {\"src\": \"IEC\", \"where\": \"s.v. bhrǵhont- and bhrǵhus (Mann, IEC.txt lines 1794-1795)\", \"stance\": \"supports\", \"note\": \"'bhr̥ǵhont- (bhrghnt-, bhrghont-) \\\"high; height\\\". WP II, 172 ... Skt. brhát; Av. bərəzant; Oss. bärzond; Per. buland, baland'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 12.31 / 12.53 (SYN.txt lines 992, 21781)\", \"stance\": \"supports\", \"note\": \"'Skt. brhant- \\\"high, great\\\", Av. barəzant- \\\"high\\\", barəzah- \\\"height, mountain\\\", Arm. berj \\\"height\\\", Ir. bri ... Walde-P. 2.172 ff.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 2,\n \"lang\": \"Persian\",\n \"words\": \"brahman «برهمن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP برهمن barahman 'Brahmin, priest of the Indian religion' is a learned Indic loan, not an inherited Iranian word: it comes from Sanskrit brāhmaṇá- 'one belonging to the brahman, member of the priestly class' (the vṛddhi-derivative of bráhman-), with shortening of the long ā of the first syllable, loss of the -a ending and the usual Persian anaptyxis in the r-h cluster (brāhmaṇa > barahman). The plural براهمه barāhema in Persian is the Arabic broken plural of the same word, showing that the term also circulated through Arabic geographical and doxographical literature (al-Bīrūnī, Šahrastānī) beside direct Indo-Persian contact. Ferdowsī's line quoted in the chart (صنم بودی اکنون برهمن شدی) shows it fully naturalised by c. 1000 CE. Borhān-e Qāṭeʿ p.269 defines برهمن 'بت‌پرست و زناربند ... و حکما و دانشمندان و پیر و مرشد بت‌پرستان و هندوان' and gives برهمه (the chart's script_extra) as 'مخفف برهمن'. Nourai's arrow Sanskrit → Persian is right; the precise source form is the derived brāhmaṇá-, not bráhman- itself.\",\n \"derivation_fa\": \"«برهمن» در فارسی وام‌واژه‌ای هندی است، نه واژه‌ای ایرانی‌تبار: از سنسکریت brāhmaṇá- «از طبقهٔ روحانیان، برهمن» که خود ساختِ وریدهی (vṛddhi) از brahman- «وِرد مقدس» است. در فارسی «آ»ی هجای نخست کوتاه شده، پایانهٔ ‎-a‎ افتاده و میان r و h واکهٔ میانجی افزوده شده است (brāhmaṇa ← بَرَهمَن). جمعِ «براهمه» جمع مکسر عربی همین واژه است و نشان می‌دهد که این کلمه از راه نوشته‌های عربی (بیرونی، شهرستانی) نیز رواج یافته است. معین در حاشیهٔ برهان قاطع (ص ۲۶۹) آن را از سنسکریت brāhmaṇa و به نقل از مونیه-ویلیامز می‌داند و «برهمه» را «مخفف برهمن» می‌خواند؛ بیت فردوسی نیز کهنگی کاربرد آن را در سدهٔ چهارم نشان می‌دهد. ادعای نورایی درست است، تنها با این نکته که صورت مأخذ brāhmaṇá- است نه brahman-.\",\n \"sources\": [W_BARAHMAN, W_BRAHMAN],\n \"ref_check\": [\n   {\"ref\": \"BQT:269\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ ed. Moʿin, printed p.269 = leaf 489 of BQT_v1_pages.txt (offset printed ≈ leaf − 220 in this part of vol. 1): headword 'برهمن ... بمعنی بت‌پرست و زناربند باشد و حکما و دانشمندان و پیر و مرشد بت‌پرستان و هندوان'; the neighbouring entry 'برهمه ... مخفف برهمن است که اصیل و نجیب و حکیم و پیر و مرشد هنود باشد'; Moʿin's footnote on the same page: 'سانسکریت brāhmaṇa بمعنی مطلق پیشوایان روحانی؛ یکی از سه طبقهٔ مردم در آیین برهمایی ... راجع به تصور مسلمانان از براهمه رک: دائرةالمعارف اسلام: براهمه' (grep 'برهمن' BQT_v1_pages.txt, lines 19256-19270).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Farhang-e Fārsi s.v. برهمن (MON_part1.txt line 22916)\", \"stance\": \"supports\", \"note\": \"'برهمن: [brāhmaṇa] (ص.) پیشوای روحانی آیین برهمایی و آنان یکی از سه طبقهٔ مردم را در آیین برهمایی تشکیل می‌دهند. ضح.- معرب این کلمه نیز «برهمن» ج آن «براهمه» است.' — same Sanskrit source and the Arabic plural.\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.111 s.v. BRAHMIN, BRAHMAN\", \"stance\": \"supports\", \"note\": \"'In some parts of India called Bahman; Skt. Brāhmaṇa. This word now means a member of the priestly caste ... Haug traces the word to the root brh, \\\"to increase\\\"'.\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss der neupersischen Etymologie\", \"stance\": \"silent\", \"note\": \"grep -i 'brahman|barahman' HRN.txt: no hit — Horn does not treat it, as expected for a late Indic loan.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien\", \"stance\": \"silent\", \"note\": \"grep -i 'brahman' HUB.txt: no hit.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, IE roots of Persian\", \"stance\": \"silent\", \"note\": \"grep 'برهمن' incoming/ARY/ARY_pages.txt: no headword (BRAHMAN appears only in the Latin index, line 943, in a list of the Indian castes).\"}\n ]\n})\n\nnodes.append({\n \"id\": 3,\n \"lang\": \"English\",\n \"words\": \"Brahma, Brahman\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English Brahma (the creator god, Skt. nom. Brahmā of the masc. stem brahman-) and Brahman/Brahmin (the priestly caste, Skt. brāhmaṇá-) are both Sanskrit words in English, but by two routes: the older form Brachman/Brachmanes reached English through the Greek Βραχμᾶνες of Megasthenes and Strabo and its Latin rendering (so Hobson-Jobson: 'The older English form is Brachman, which comes to us through the Greek and Latin authors'), while the modern spellings Brahman, Brahmin, Brahma are 18th-19th c. Anglo-Indian borrowings taken straight from Sanskrit by orientalists. Klein's entry is Nourai's source and says exactly this. No sound change is involved beyond the Latinisation of the ending.\",\n \"derivation_fa\": \"واژه‌های انگلیسی Brahma و Brahman/Brahmin هر دو از سنسکریت‌اند: Brahma از صورت فاعلی Brahmā (ستاک مذکر brahman-) و Brahman/Brahmin از brāhmaṇá-. راه ورود دوگانه است: صورت کهن‌تر Brachman از راه یونانی Βραχμᾶνες (مگاستنس و استرابون) و لاتین به انگلیسی رسیده، ولی املاهای امروزی وام‌گیری مستقیم شرق‌شناسان سدهٔ هجدهم و نوزدهم از سنسکریت است (هابسون-جابسون، ص ۱۱۱). دگرگونی آوایی چشمگیری در کار نیست و ادعای نورایی درست است، تنها با یادآوری واسطهٔ یونانی-لاتین در صورت کهن.\",\n \"sources\": [W_BRAHMAN],\n \"ref_check\": [\n   {\"ref\": \"KLN:194\", \"status\": \"supports\", \"note\": \"Klein s.v. Brahma/Brahman (leaf pp.193-194): 'Brahma, Brahman, n., 1) the impersonal world soul ... — OI. brahman- (neut.) ... Brahman (masc.), \\\"the chief god of Hindu religion\\\"'; and 'Brahman, n., a member of the highest priestly caste among the Hindus. — OI. brahmana-, fr. brahman-, \\\"prayer\\\".'\"}\n ],\n \"consulted\": [\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson p.111\", \"stance\": \"partial\", \"note\": \"'The older English form is Brachman, which comes to us through the Greek and Latin authors' (with the Strabo/Megasthenes citations Βραχμᾶνες) — i.e. Greek/Latin mediation for the earliest English form, which Nourai's direct Sanskrit→English arrow omits.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, list of words from Sanskrit (SKT.txt line 23630)\", \"stance\": \"supports\", \"note\": \"'Sanskrit: avatar, banyan, brahmin (brahman), champak, pundit, ... Veda' — Skeat classes brahmin among the direct Sanskrit borrowings.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4,\n \"lang\": \"Germanic\",\n \"words\": \"bergaz; burgs; harja-bergaz\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Proto-Germanic *bergaz 'mountain, hill' < *bʰérǵʰ-o-s, with Grimm's law *bʰ > b and *ǵʰ > g (OE beorg, OS/OHG berg, ON berg, Goth. bairgahei 'mountainous country'); the zero grade *bʰr̥ǵʰ- gives PGmc *burg-s 'fortified height, hill-fort' (syllabic *r̥ > ur before the velar), whence Goth. baurgs 'city', OE burg/burh/byrig, OHG burg. That much is standard (Watkins bhergh-2 §1 and §4; Klein s.v. borough; Pokorny 140-141: 'Gothic baurgs \\\"town, city, tower\\\", Old High German burg \\\"castle\\\" is the genuine Germanic equivalent of Avestan bərəz-, Celtic brig- with the meaning \\\"fortified height as refuge\\\"'). The third word is the weak link: Watkins does list '*harja-bergaz, \\\"army-hill,\\\" hill-fort' under bhergh-2 §2 (and under koro- 'army', whence Nourai's ☞Koro cross-reference), but the modern consensus (Kroonen, Etymonline) takes the second member of OE here-beorg to be the homophonous root *bʰergʰ- 'to hide, protect' (PGmc *bergan- 'to shelter'), giving 'army-shelter, quarters' rather than 'army-hill'; Buck likewise leaves burgs itself hanging between 'place of refuge' (: OE beorgan 'shelter') and 'height'. Hence plausible.\",\n \"derivation_fa\": \"ژرمنی آغازین *bergaz «کوه، تپه» بازماندهٔ *bʰérǵʰ-o-s است؛ بنابر قانون گریم، *bʰ به b و *ǵʰ به g بدل شده (انگلیسی کهن beorg، آلمانی Berg). درجهٔ صفرِ *bʰr̥ǵʰ- به *burgs «دژِ بلند» انجامیده است، زیرا r هجایی پیش از همخوان نرم‌کامی در ژرمنی به ur تبدیل می‌شود (گوتی baurgs «شهر»، انگلیسی کهن burg، آلمانی Burg). این بخش استوار است. اما واژهٔ سوم، *harja-bergaz، محل بحث است: واتکینز آن را «تپهٔ سپاه» و از همین ریشه می‌داند (و نورایی نیز با ارجاع ☞Koro همان را آورده)، ولی ریشه‌شناسی امروزی (کرونن و اتیمولوژی‌آنلاین) جزء دوم را از ریشهٔ هم‌آوای *bʰergʰ- «پناه دادن، پنهان کردن» می‌گیرد، یعنی «پناهگاه سپاه». پس ادعای نورایی در کل پذیرفتنی است اما در مورد harja-bergaz با احتیاط.\",\n \"sources\": [W_BURG, E_BOROUGH, E_HARBOR],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 (AHD_watkins1985.txt) s.v. 'bhergh-2. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain ... 2. Compound *harja-bergaz, \\\"army-hill,\\\" hill-fort (*harjaz, army; see koro-) ... 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort ... [Pok. bheregh- 140.]' — the three words and the Koro cross-reference are copied from this entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. borough (KLN_1966.txt line 5381, pp.193-194)\", \"stance\": \"supports\", \"note\": \"'OE. burg, burh ... Goth. baurgs, \\\"city\\\", OE. beorg, etc., \\\"mountain\\\". These words prob. derive fr. I.-E. base *bhergh-, \\\"high\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"pp.140-141\", \"stance\": \"supports\", \"note\": \"'Gothic baurgs \\\"town, city, tower\\\", Old High German burg \\\"castle\\\" is genuine Germanic equivalent of Avestan bərəz-, Celtic brig- with the meaning \\\"fortified height as refuge\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 19.15 'city, town' (SYN.txt line 32861)\", \"stance\": \"partial\", \"note\": \"'Goth. baurgs, ON borg ... all, except Goth., in earliest use \\\"fortified place\\\", either as \\\"place of refuge\\\" : OE beorgan, OHG bergan \\\"shelter\\\"; or else as \\\"height\\\" : OE beorg ... Skt. brhant-, Av. barəzant- \\\"high\\\". Walde-P. 2.173' — Buck leaves the root assignment open.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 172 s.v. bhergh- 'bergen, verwahren'\", \"stance\": \"partial\", \"note\": \"'Got. bairgan \\\"bergen, verwahren\\\" ... (Über Burg s. u. *bhergh- \\\"hoch\\\")' — Walde-Pokorny put Burg under the 'high' root but the shelter verb under the homonymous root, which is the fault line for harja-bergaz.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5,\n \"lang\": \"English\",\n \"words\": \"iceberg, Canterbury, borough, harbor\",\n \"verdict\": \"plausible\",\n \"derivation\": \"borough < OE burg/burh 'dwellings within a fortified enclosure' < PGmc *burgs, with the sense drift fortress > fortified town > town (16c.); the English place-name element -bury (Canterbury < OE Cantwaraburg 'the burh of the men of Kent') is the dative singular byrig of the same noun, so Nourai's Canterbury belongs here correctly. iceberg is a later importation, not a native form: attested 1774 'glacier humped like a hill', a partial loan-translation of Dutch ijsberg 'ice mountain' (cf. Norwegian isberg, Danish isbjerg), the -berg being PGmc *bergaz. harbor < ME herberwe < OE here-beorg 'lodgings, quarters' (a compound of here 'army'), whose second element Watkins assigns to *bergaz 'hill' but Etymonline and Kroonen to *bʰergʰ- 'to hide, protect'; the semantic 'lodging, shelter' > 'shelter for ships' (early 12c.) favours the latter. That single word keeps the node at plausible.\",\n \"derivation_fa\": \"انگلیسی borough از burg/burh انگلیسی کهن «خانه‌های درون حصار» است و معنایش از «دژ» به «شهرِ حصاردار» و سپس «شهر» گراییده؛ پسوند مکان‌نام‌های ‎-bury‎ (مانند Canterbury از Cantwaraburg «دژِ مردم کنت») همان واژه در حالت به‌ای byrig است. اما iceberg وام‌واژه‌ای متأخر (۱۷۷۴ م) و گرته‌برداری ناقص از هلندی ijsberg «کوهِ یخ» است. harbor از here-beorg انگلیسی کهن «جایگاه سپاه، منزلگاه» می‌آید که جزء دومش را واتکینز از *bergaz «تپه» و پژوهش امروزی از ریشهٔ هم‌آوای *bʰergʰ- «پناه دادن» می‌گیرد؛ معنای «پناهگاه» به رأی دوم نزدیک‌تر است. پس بخش عمدهٔ گره درست و تنها harbor با احتیاط پذیرفتنی است.\",\n \"sources\": [E_BOROUGH, E_ICEBERG, E_HARBOR],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins bhergh-2 §1b 'Old Norse berg ... mountain: ICEBERG' and §4a 'Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG'; HARBOR is indexed in the same book under koro- (the compound *haryja-bergaz), which is the cross-reference Nourai prints.\"}\n   ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. borough (line 5381)\", \"stance\": \"supports\", \"note\": \"'Cp. ... canterbury ... Cp. also the suff. -bury in English place names, which comes fr. OE. byrig, the dative sing of OE. burg.'\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.vv. borough, iceberg, harbor\", \"stance\": \"partial\", \"note\": \"borough and iceberg are put under 'PIE root *bhergh- (2) \\\"high\\\"', but harbor under 'PIE root *bhergh- (1) \\\"to hide, protect\\\"' ('from Proto-Germanic compound *harja-bergaz \\\"shelter, lodgings\\\", from *heri \\\"army\\\" + *burzjan- \\\"protection, shelter\\\"').\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century s.v. burg (WEB_vol1.txt line 25047)\", \"stance\": \"supports\", \"note\": \"'burg, n. (ME. burgh; AS. burh, burg, a fortified town) 1. originally, a fortified town.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 6,\n \"lang\": \"Latin\",\n \"words\": \"burgus\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Late Latin burgus 'small fort, fortified post' is real and well attested — Vegetius, Mil. 4,10 'castellum paruulum quem burgum uocant', Orosius 7,32,13 'crebra per limitem habitacula constituta burgos uulgo uocant' — but it is not an inherited Latin reflex of the root, and Nourai's arrow drawing it straight from Indo-European is misleading. An inherited *bʰr̥ǵʰ- would give Latin f- (as it does in for(c)tis, node 11), not b-. Latin burgus is a borrowing: from Germanic *burgs (so Ernout-Meillet 'mot évidemment germanique', Watkins, who files it under Germanic *burgs, and Webster), or, on a minority view going back to the CGL gloss πύργος : burgus, from Greek πύργος 'tower' — which Pokorny in fact adopts, adding that πύργος is itself an oriental loan from Urartian burgana 'palace, fortress'. Either way the word entered Latin in the 4th c. CE with the Rhine-Danube limes forts. The root and the meaning are right; the directness of the line is not.\",\n \"derivation_fa\": \"لاتینِ متأخر burgus «دژِ کوچک، پاسگاه مرزی» واژه‌ای واقعی است (وگتیوس، سدهٔ چهارم میلادی: castellum paruulum quem burgum uocant)، اما بازماندهٔ ارثیِ ریشهٔ هندواروپایی در لاتین نیست؛ اگر بود می‌بایست با f- آغاز شود (چنان‌که در for(c)tis)، نه با b-. این واژه وام‌واژه است: ارنو-مه‌یه آن را «آشکارا ژرمنی» می‌خواند و واتکینز نیز آن را ذیل *burgs ژرمنی می‌آورد؛ پوکورنی در برابر، آن را وام از یونانی πύργος «برج» می‌داند که خود از اورارتویی burgana «کاخ، دژ» گرفته شده است. در هر دو صورت ورود واژه به لاتین در سدهٔ چهارم میلادی و در پیوند با دژهای مرزی راین و دانوب بوده است. پس ریشه و معنی درست است، ولی پیکانِ مستقیمِ نورایی از ریشهٔ هندواروپایی به لاتین نادرست است و باید از راه ژرمنی (یا یونانی) کشیده شود.\",\n \"sources\": [E_BURGLAR],\n \"ref_check\": [\n   {\"ref\": \"AHD:1509\", \"status\": \"partial\", \"note\": \"Watkins bhergh-2 §4d: 'Late Latin burgus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG' — but it stands inside §4 'Zero-grade form *bhrgh- in Germanic *burgs', i.e. AHD makes Latin burgus a Germanic loan, not a direct Latin descendant as the chart draws it. (AHD p.1509 is in the New College Edition IE-roots appendix, pp.1505-1550, of which the 1985 Watkins standalone on disk is the same list.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. burgus (LAT.txt line 7964)\", \"stance\": \"partial\", \"note\": \"'burgus, -i m.: b.lat., e.g. Veg., Mil. 4,10, castellum paruulum quem burgum uocant; Oros., Hist. 7,32,13 ... Mot évidemment germanique; la glose πύργος haec turris, burgus, CGL II 436,46 ... est un rapprochement de lettrés. V. toutefois E. Penninck, L'origine hellénique de \\\"burgus\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"pp.140-141\", \"stance\": \"contradicts\", \"note\": \"'With it is coincident though Latin burgus \\\"castle, fort\\\", that is borrowed from gr. πύργος \\\"tower\\\", an oriental loanword from urart. burgana \\\"palace, fortress\\\" ... whereof would have also derived Armenian burgn, aram. burgin' — Pokorny denies any direct inheritance.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's s.v. burgess (WEB_vol1.txt line 25047)\", \"stance\": \"supports\", \"note\": \"'OFr. burgeis; LL. burgensis, citizen; burgus, a borough, town; OHG. burc, a fortified town' — Latin burgus explained from the Germanic word.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7,\n \"lang\": \"Old French\",\n \"words\": \"bourg; burgeis\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"OFr. borc / bourg 'town, village (as opposed to countryside)' continues Late Latin burgus (or, as Etymonline puts it, the Frankish *burg that also fed the Latin word — the two converge in Merovingian Gaul); burgeis 'town dweller' is Late Latin burgēnsis (burgus + the denominal suffix -ēnsis) with regular OFr. treatment of -ēnsis > -eis (as in franceis, marchëis) and the nominative -s. Klein: 'burgess, n., citizen of a borough. — OF. burgeis (F. bourgeois), fr. Late L. burgensis, fr. Teut. *burg, \\\"town\\\"'. The pair bourg/burgeis in one node reproduces AHD's '(> burgensis, city dweller)'.\",\n \"derivation_fa\": \"فرانسویِ کهن borc/bourg «شهرک» دنبالهٔ burgus لاتینِ متأخر است (اتیمولوژی‌آنلاین همان را از *burg فرانکی می‌گیرد؛ این دو در گُلِ دورهٔ مروونژی به هم می‌رسند). burgeis «شهرنشین» از burgēnsis لاتینِ متأخر است، یعنی burgus به‌علاوهٔ پسوند نسبتِ ‎-ēnsis‎ که در فرانسوی کهن قاعدتاً ‎-eis‎ می‌شود (مانند franceis) و ‎-s‎ پایانی نشانهٔ حالت فاعلی است. کلاین همین را می‌گوید. ادعای نورایی درست است.\",\n \"sources\": [E_BOURGEOIS],\n \"ref_check\": [\n   {\"ref\": \"AHD:156\", \"status\": \"not_checked\", \"note\": \"AHD p.156 is a page of the New College Edition main dictionary (s.v. bourg/bourgeois), which is not on disk; only Watkins's IE-roots appendix is, and it lists 'BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG' under bhergh-2 §4d, which is the same claim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. burgess and bourgeoisie (KLN_1966.txt lines 5897, 5446)\", \"stance\": \"supports\", \"note\": \"'burgess, n., citizen of a borough. — OF. burgeis (F. bourgeois), fr. Late L. burgensis, fr. Teut. *burg, \\\"town\\\"'; 'bourgeoisie, n., middle class. — F., fr. bourgeois ... fr. bourg, \\\"small town\\\" ... of Teut. origin'.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's s.v. burgess\", \"stance\": \"supports\", \"note\": \"'OFr. burgeis; LL. burgensis, citizen; burgus, a borough, town'.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. bourgeois\", \"stance\": \"partial\", \"note\": \"'from Old French burgeis, borjois \\\"town dweller\\\" ... from borc \\\"town, village\\\", from Frankish *burg \\\"city\\\" (via Germanic from PIE root *bhergh- (2))' — the Frankish rather than the Latin line.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8,\n \"lang\": \"Persian\",\n \"words\": \"bŭržŭâ «بورژوا»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Persian بورژوا burž(u)vā 'bourgeois, well-to-do townsman' is a twentieth-century loan from MODERN French bourgeois, taken by ear: French [buʁˈʒwa] is rendered بورژوا with ژ for the French j and ‑وا for the -ois /wa/, and the companion بورژوازی renders bourgeoisie. It entered Persian with the political vocabulary of the constitutional and post-constitutional press (alongside پرولتاریا, سوسیالیست), directly from French, with no Arabic mediation. Nourai's arrow from OLD French cannot be right in that form: OFr. burgeis was still pronounced with a diphthong and an audible final -s ([burˈdʒejs]), which would have given Persian *بورژیس, not بورژوا; the -ois > /wa/ development is a French sound change of the 15th-18th centuries, long after Old French. So: right ultimate source, wrong stage of French.\",\n \"derivation_fa\": \"«بورژوا» وام‌واژه‌ای از فرانسویِ نو (bourgeois) است که در سدهٔ چهاردهم خورشیدی و همراه با واژگان سیاسی دورهٔ مشروطه و پس از آن (پرولتاریا، سوسیالیست) و از راه شنیداری به فارسی درآمده است: ژ برابر j فرانسوی و «ـوا» برابر تلفظ ‎-ois‎ /wa/ نشسته است؛ «بورژوازی» نیز برگردان bourgeoisie است. معین آن را با نشانهٔ [فر.] یعنی فرانسوی می‌آورد. پیکان نورایی از «فرانسوی کهن» درست نیست: در فرانسوی کهن این واژه burgeis و با ‎-s‎ پایانی تلفظ می‌شد و اگر در آن دوره وام گرفته شده بود در فارسی «بورژیس» می‌شد؛ تلفظ /wa/ برای ‎-ois‎ دگرگونی آوایی سده‌های پانزدهم تا هجدهم فرانسه است. پس مأخذ نهایی درست ولی مرحلهٔ زبانی نادرست است.\",\n \"sources\": [ABADIS, E_BOURGEOIS],\n \"ref_check\": [\n   {\"ref\": \"MON:601\", \"status\": \"partial\", \"note\": \"The 6-volume Moʿin (where p.601 of vol. 1 would fall in the ب) is not on disk; the 2-volume Adena abridgement is: 'بورژوا: [bourgeois] شهری، شهرنشین (که در سابق از حقوق مخصوص برخوردار بود)، شهرنشین مرفه و ثروتمند، ارباب، مخدوم؛ متعلق به بورژوازی' (MON_part1.txt line 26041), and abadis.ir reproduces Moʿin's own tag '[فر.] (ص.) ثروتمند، دارندهٔ سرمایه و ابزار تولید' — i.e. Moʿin marks the word French (فر.), not Old French, so the reference supports the source language but not the Old French stage Nourai draws.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. بورژوا (MON_part1.txt line 26041) and via abadis.ir\", \"stance\": \"partial\", \"note\": \"Moʿin's origin tag is [فر.] 'French' (modern), and the entry sits beside بورژوازی 'طبقهٔ سرمایه‌داری'.\"},\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. bourgeois\", \"stance\": \"supports\", \"note\": \"'1560s ... from French bourgeois, from Old French burgeis, borjois \\\"town dweller\\\"' — the modern French form is the one all later languages, Persian included, borrowed.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9,\n \"lang\": \"English\",\n \"words\": \"bourgeois\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English bourgeois is a French loan of the 1560s, first 'of or pertaining to the French middle class', from French bourgeois < OFr. burgeis/borjois 'town dweller (as distinct from peasant)'; the sense 'socially or aesthetically conventional, middle-class in taste' is from 1764 and the Marxist sense 'capitalist class' from the 1850s translations. The word was never nativised phonetically (it keeps its French /buːʒˈwɑː/), which is itself the proof of a book-and-salon borrowing rather than an inherited form.\",\n \"derivation_fa\": \"انگلیسی bourgeois وام‌واژه‌ای فرانسوی از دههٔ ۱۵۶۰ م است، نخست به معنی «وابسته به طبقهٔ متوسط فرانسه»، از فرانسوی bourgeois و آن از burgeis فرانسوی کهن «شهرنشین». معنای «متعارف و میان‌مایه» از ۱۷۶۴ م و معنای مارکسیستی «طبقهٔ سرمایه‌دار» از ترجمه‌های سدهٔ نوزدهم است. تلفظ فرانسوی‌مانده و بومی‌نشدهٔ آن گواه وام‌گیری کتابی است. ادعای نورایی درست است.\",\n \"sources\": [E_BOURGEOIS],\n \"ref_check\": [\n   {\"ref\": \"AHD:156\", \"status\": \"not_checked\", \"note\": \"The New College Edition main-dictionary page 156 is not on disk; Watkins's appendix lists BOURGEOIS (in parentheses, i.e. as a derivative) under bhergh-2 §4d, which agrees with the chart.\"}\n ],\n \"consulted\": [\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. bourgeois (adj.)\", \"stance\": \"supports\", \"note\": \"'1560s, \\\"of or pertaining to the French middle class,\\\" from French bourgeois, from Old French burgeis, borjois \\\"town dweller\\\" (as distinct from \\\"peasant\\\"), from borc \\\"town, village\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. bourgeoisie / burgee (lines 5446, 5897)\", \"stance\": \"supports\", \"note\": \"'burgee ... fr. OF. burgeis (F. bourgeois) in burgeis d'un navire, \\\"owner of a ship\\\"; see bourgeois.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 10,\n \"lang\": \"English\",\n \"words\": \"burg, burglar\",\n \"verdict\": \"plausible\",\n \"derivation\": \"burglar (1540s) does belong under Latin burgus: it is shortened from Anglo-Latin burglator (late 13c.), earlier burgator, from Medieval Latin burgātor, to burgāre 'to break open, commit burglary', a verb built on burgus; Klein and Webster analyse the word as a hybrid 'town-thief' — burg- (the Germanic loan) + Latin latrō, latrōnem 'thief' (OFr. lerre, acc. laron), which also explains the unetymological -l-. burg 'town', however, does NOT come through Latin: it is OE burg/burh continued (and in the modern American colloquial use reinforced by German Burg and by place-names in -burg), i.e. it belongs to node 4/5, not under Latin burgus. The node is therefore only half in the right place.\",\n \"derivation_fa\": \"burglar «دزدِ خانه‌شکن» (۱۵۴۰ م) به‌درستی زیر burgus لاتین جای می‌گیرد: کوتاه‌شدهٔ burglator در لاتینِ انگلیسی (سدهٔ سیزدهم) و پیش‌تر burgator، از فعل لاتینِ میانه burgāre «شکستن و درآمدن» که بر burgus ساخته شده است؛ کلاین و وبستر آن را واژه‌ای دورگه می‌دانند: burg (وام ژرمنی) + latrō لاتین «دزد» که ‎-l-‎ بی‌ریشهٔ آن را نیز توضیح می‌دهد. اما burg «شهر» از راه لاتین نیامده است؛ دنبالهٔ burg/burh انگلیسی کهن است (و کاربرد امروزی آمریکایی‌اش از Burg آلمانی و نام‌های مکان با ‎-burg‎ نیرو گرفته). پس جای burglar درست و جای burg در این گره نادرست است.\",\n \"sources\": [E_BURGLAR],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins bhergh-2 §4a lists 'BOROUGH, BURG' under Old English burg (i.e. the Germanic line, not the Latin one) and §4d lists 'BURGLAR' under Late Latin burgus — so AHD itself splits the two words Nourai puts in one Latin node.\"}\n ],\n \"consulted\": [\n   {\"src\": \"ETYMONLINE\", \"where\": \"s.v. burglar\", \"stance\": \"supports\", \"note\": \"'1540s, shortened from Anglo-Latin burglator (late 13c.), earlier burgator, from Medieval Latin burgator \\\"burglar\\\", from burgare \\\"to break open, commit burglary\\\", from Latin burgus \\\"fortress, castle\\\", a Germanic loan-word akin to borough. The unetymological -l- is perhaps from influence of Latin latro \\\"thief\\\"'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. burglar (KLN_1966.txt line 5898)\", \"stance\": \"partial\", \"note\": \"'burglar, n. — ML. burgulator, burglator, a hybrid lit. meaning \\\"town thief\\\". The first element is a Teut. loan word (see borough), the second is traceable to L. latro' — Klein makes the first element Germanic, not Latin.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's s.v. burglar (WEB_vol1.txt line 25079)\", \"stance\": \"supports\", \"note\": \"'[OFr. burg, from LL. burgus, a town, and OFr. lere, from L. latro, a thief] one who commits burglary.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 11,\n \"lang\": \"Latin\",\n \"words\": \"horctus; forctus, fortis\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The forms are genuine and correctly transcribed: Paulus's epitome of Festus preserves 'horctum et forctum pro bono dicebant' (91,14) and 'forctes, frugi et bonus siue ualidus' (74,14), horctus being the rural/Praenestine form with h- for f-, and Old Latin forctis is the direct ancestor of classical fortis 'strong, brave'. Nourai's gloss 'high, good' for horctus mixes Festus's 'bonus' with the root meaning. The derivation itself is the contested part. Brugmann (BSGW 1897, 21ff.) and Persson, followed by Walde-Hofmann I 535f., Pokorny 140 ('Latin for(c)tis, Old Latin forctus, dial. horctus ... from *forg-tos, Indo-European *bhr̥gh-tos = Old Indic bṛdhah'), Klein and Watkins, derive it from the suffixed zero grade *bʰr̥ǵʰ-to- 'grown high, hence robust'. But Walde-Pokorny II 173 itself adds 'doch s. über fortis wahrscheinlicheres u. *dher-, dhereǵh- \\\"halten\\\"'; Ernout-Meillet call the forctus/fortis doublet a lettered conjecture ('foretis, fortus sont peut-être des noms d'une peuplade latine') and prefer Av. drāzaite 'holds', OCS drŭžati; Buck likewise ('prob.: Av. drazaite \\\"holds\\\" ... guttural extensions of IE *dher-'); Wiktionary and de Vaan present both, reconstructing Proto-Italic *θorktis on the *dʰerǵʰ- option; and even AHD hedges, '*bhrgh-to- POSSIBLY in Latin fortis, strong (but this is also possibly from dher-2)'. So the words are real and Nourai's source (AHD/Klein) says what he says, but the etymology is disputed in the wider literature: plausible.\",\n \"derivation_fa\": \"صورت‌های این گره اصیل‌اند: در تلخیص فستوس آمده «horctum et forctum pro bono dicebant» و «forctes، frugi et bonus siue ualidus»؛ horctus گونهٔ گویشی (پرنستی/سابینی) با h به‌جای f است و forctis لاتینِ کهن نیای مستقیم fortis کلاسیک «نیرومند، دلیر». معنای «بلند» که نورایی برای horctus آورده از ریشه گرفته شده، نه از فستوس که تنها «نیک» می‌دهد. اما خودِ ریشه‌شناسی محل اختلاف است: بروگمان و پرسون و پس از آنان والده-هوفمان، پوکورنی (ص ۱۴۰: از *bʰr̥ǵʰ-tos «بلندبالا، از این رو تنومند»)، کلاین و واتکینز آن را از همین ریشهٔ «بلندی» می‌گیرند، ولی والده-پوکورنی (ج۲ ص۱۷۳) خود می‌نویسد که «دربارهٔ fortis رأی محتمل‌تر را ذیل *dher-, dhereǵh- \\\"نگاه داشتن\\\" ببینید»، ارنو-مه‌یه و باک نیز اوستایی drāzaite «نگاه می‌دارد» و اسلاوی کهن drŭžati را ترجیح می‌دهند و ویکی‌واژه هر دو رأی را می‌آورد. حتی خودِ AHD می‌افزاید «شاید هم از dher-». پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_FORTIS, W_ROOT],\n \"ref_check\": [\n   {\"ref\": \"KLN:614\", \"status\": \"supports\", \"note\": \"Klein s.v. fort (KLN_1966.txt line 15222, on the leaf carrying pp.613-614): 'fort, n. — F. fort, \\\"stronghold, fort\\\", from the adjective fort, \\\"strong\\\", fr. L. fortis, \\\"strong\\\", which is rel. to OL. forctus, dial. horctus, horctis, \\\"good\\\"; prob. fr. I.-E. base *bhergh-, \\\"high, to raise\\\". See borough' — Nourai's three forms and their glosses come from this line.\"},\n   {\"ref\": \"AHD:1509\", \"status\": \"partial\", \"note\": \"Watkins bhergh-2 §5: 'Suffixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-2): FORCE, FORT ... COMFORT ... EFFORT' — supports the chart but with an explicit alternative that the chart does not show.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"pp.140-141\", \"stance\": \"supports\", \"note\": \"'Latin for(c)tis, Old Latin forctus, dial. horctus, horctis \\\"physically strong ... brave\\\" (from *forg-tos, Indo-Germanic *bhr̥gh-tos = Old Indic bṛdhah)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 173\", \"stance\": \"partial\", \"note\": \"'Sollte daher lat. for(c)tis nach Bgm. BSGW. 1897, 21ff., Persson Beitr. 51f. unserem *bherǵh- entstammen, wäre es ... als \\\"hochgewachsen, daher robust\\\" zu verstehn: doch s. über fortis wahrscheinlicheres u. *dher-, dhereǵh- \\\"halten\\\".'\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. fortis (LAT.txt lines 23824-23840)\", \"stance\": \"contradicts\", \"note\": \"'On interprétait généralement forctus (et le dialectal horctus) comme un doublet de foretis, ancienne forme de fortis; mais foretis, fortus sont peut-être des noms d'une peuplade latine ... Le rapprochement le plus plausible serait dès lors avec av. drāzaite \\\"il tient\\\", v.sl. drŭžati \\\"tenir\\\"'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 4.81 'strong' (SYN.txt line 7598)\", \"stance\": \"contradicts\", \"note\": \"'Lat. fortis ... fr. forctis (Festus), prob.: Av. drazaite \\\"holds\\\", ChSl. drŭžati \\\"hold\\\", guttural extensions of IE *dher- ... Otherwise (fr. *bhergh- ...) Walde-H. 1.535 ff.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Fort (SKT.txt line 6988)\", \"stance\": \"silent\", \"note\": \"'Fort, Fortalice; see Force (1)' — the concise Skeat gives no IE root.\"}\n ]\n})\n\nnodes.append({\n \"id\": 12,\n \"lang\": \"English\",\n \"words\": \"fort, force, comfort, effort\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All four are Latin fortis through French, and the chain is uncontroversial: fort (15c.) from Middle French fort, substantivised from the adjective fort < Latin fortis; force from OFr. force < Vulgar Latin *fortia, the neuter plural of fortis reinterpreted as a feminine singular; comfort from OFr. conforter < Late Latin confortāre 'to strengthen greatly' (com- intensive + fortis), the sense 'consolation' developing in Old French; effort from OFr. esfort/esforz, verbal noun of esforcier < Vulgar Latin *exfortiāre 'to force out, exert'. Whatever the ultimate Indo-European root of fortis (see node 11), this node's derivations are secure.\",\n \"derivation_fa\": \"هر چهار واژه از fortis لاتین و از راه فرانسوی به انگلیسی رسیده‌اند و در این زنجیره اختلافی نیست: fort از fort فرانسوی میانه (صفت اسم‌شده)؛ force از force فرانسوی کهن و آن از *fortia لاتین عامیانه، یعنی جمع خنثای fortis که مؤنث مفرد پنداشته شده؛ comfort از conforter فرانسوی کهن و آن از confortāre لاتینِ متأخر «سخت نیرو بخشیدن»؛ effort از esforz فرانسوی کهن، اسم مصدرِ esforcier از *exfortiāre. سرنوشت ریشهٔ هندواروپاییِ fortis هرچه باشد (بنگرید به گرهٔ ۱۱)، این حلقه‌ها استوارند و ادعای نورایی درست است.\",\n \"sources\": [W_FORTIS],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins bhergh-2 §5 lists exactly this family: 'FORCE, FORT, FORTALICE, FORTE ... FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. fort and forte (KLN_1966.txt lines 15222-15223)\", \"stance\": \"supports\", \"note\": \"'fort, n. — F. fort, \\\"stronghold, fort\\\", from the adjective fort, \\\"strong\\\", fr. L. fortis ... Cp. also force, \\\"strength\\\", fortalice, forte, fortress, comfort, counterfort, sforzando.'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Fort (SKT.txt line 6988)\", \"stance\": \"supports\", \"note\": \"'Fort, Fortalice; see Force (1)' — Skeat groups the same family under Force < Latin fortis.\"}\n ]\n})\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Bhergh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *bʰerǵʰ- 'to rise, be elevated; high, mountain' (Pokorny bhereg̑h- 140-141; Watkins bhergh-2)\",\n \"note\": \"The root, the language label and the gloss are all right, and the page reference is exact: Pokorny IEW pp.140-141 'Root/lemma: bʰereĝh-, Meaning: high; mountain', with Old Indic bṛhant-, Avestan bərəzant- (npers. buland), Armenian berj, Celtic brig-, Germanic berg/burgs, Hittite parku-. Walde-Pokorny II 172-173 has the same lemma as 'bhergh- \\\"hoch, erhoben\\\"'; Watkins files it as 'bhergh-2. High; with derivatives referring to hills and hill-forts. [Pok. bheregh- 140]', which is where Nourai's part-2 numbering and most of his material come from; Wiktionary reconstructs *bʰerǵʰ- 'to rise up, ascend; to be elevated, up high' citing Pokorny 140-141, LIV2 78-79 and NIL 30-34. The one thing the chart does not show is that Nourai's spelling 'Bhergh' is ambiguous between this palatal root *bʰerǵʰ- 'high' and the homophonous velar *bʰergʰ- 'to hide, protect' (Pokorny 145, Watkins bhergh-1) — a distinction that matters twice on this page (harja-bergaz in node 4/5 and, in the wider literature, Germanic *burgs itself). Cross-cutting observations: (a) Latin burgus (node 6) is a loan, not an inherited Latin form — an inherited *bʰr̥ǵʰ- gives Latin f- as in forctis/fortis; (b) Persian بورژوا (node 8) comes from modern, not Old, French; (c) the derivation of Latin fortis from this root (node 11) is the traditional Brugmann-Walde-Hofmann view but is rejected by Ernout-Meillet, Buck and, in a footnote, by Walde-Pokorny itself in favour of *dʰerǵʰ- 'to hold'.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰerǵʰ- «برآمدن، بلند بودن؛ بلندی، کوه» است و نام ریشه، برچسب زبانی و معنایی که نورایی آورده هر سه درست‌اند؛ ارجاع او نیز دقیق است: پوکورنی، صفحه‌های ۱۴۰–۱۴۱، با شواهد سنسکریت bṛhant-، اوستایی bərəzant- (فارسی «بلند»)، ارمنی berj، ژرمنی berg/burgs و هیتی parku-. والده-پوکورنی (ج۲، ص۱۷۲–۱۷۳) و واتکینز (bhergh-2) نیز همین را دارند و شمارهٔ «بخش ۲» نورایی از واتکینز گرفته شده است. تنها نکتهٔ ناگفته این است که املای «Bhergh» میان دو ریشهٔ هم‌آوا مبهم است: *bʰerǵʰ- «بلند» و *bʰergʰ- «پناه دادن، پنهان کردن» (پوکورنی ص۱۴۵)، و این تفاوت در همین صفحه دوبار اثر می‌گذارد. سه نکتهٔ فراگیر: نخست، burgus لاتین (گرهٔ ۶) وام‌واژه است نه بازماندهٔ ارثی، چون بازماندهٔ ارثی در لاتین با f- آغاز می‌شود؛ دوم، «بورژوا»ی فارسی (گرهٔ ۸) از فرانسوی نو است نه فرانسوی کهن؛ سوم، پیوند fortis لاتین با این ریشه (گرهٔ ۱۱) رأی سنتی بروگمان و والده-هوفمان است ولی ارنو-مه‌یه، باک و حتی پانوشت خودِ والده-پوکورنی ریشهٔ *dʰerǵʰ- «نگاه داشتن» را محتمل‌تر می‌دانند.\",\n \"sources\": [W_ROOT],\n \"ref_check\": [\n   {\"ref\": \"POK:140\", \"status\": \"supports\", \"note\": \"Pokorny IEW, 'Root/lemma: bʰereĝh-, Meaning: high; mountain ... Page(s): 140-141' (POK_full.txt lines 12280-12387). The cited page is exactly where the root stands, and the gloss 'high' is Pokorny's own.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 172-173\", \"stance\": \"supports\", \"note\": \"'bhergh- \\\"hoch, erhoben\\\", vielleicht Erw. von bher- (\\\"tragen, heben\\\") ... Ai. ... brhant- \\\"groß, hoch, erhaben, hehr\\\" ... av. bərəzant- (np. buland)' (incoming/WLD/WLD_Bd2_pages.txt lines 11300-11330).\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhergh-2\", \"stance\": \"supports\", \"note\": \"'bhergh-2. High; with derivatives referring to hills and hill-forts ... [Pok. bheregh- 140.]' — and separately 'bhergh-1. To hide, protect ... [Pok. bhergh- 145]', the homonym Nourai's spelling does not distinguish.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.vv. bhrǵhont-, bhrǵhus\", \"stance\": \"supports\", \"note\": \"'bhrǵhus, os \\\"high; height\\\". WP II, 172 ... Skt. cf. brhát; Av. bərəzō; ... Hitt. parkus; Olr. brí'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 1.22 'mountain, hill' (SYN.txt line 992)\", \"stance\": \"supports\", \"note\": \"'OE beorg ... OHG, NHG berg, etc., the most widespread Gmc. word for \\\"mountain\\\" ... : Skt. brhant- \\\"high, great\\\", Av. barəzant- \\\"high\\\" ... Walde-P. 2.172 ff.'\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 93,\n \"book_page\": 63,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry0]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-93.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write('\\n')\nprint(\"written\")\nPYEOF\npython3 \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build93.py\" && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-93.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 93"
}
```


### [2026-09-05T14:19:49.538Z] TOOL RESULT

```
written
JSON OK
nodes verified: 12/12
node verdicts: {'plausible': 7, 'confirmed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 2}
books consulted: {'supports': 21, 'partial': 10, 'silent': 4, 'contradicts': 3} | by book: {'KLN': 6, 'ETYMONLINE': 5, 'POK': 4, 'WEB': 4, 'WLD': 3, 'SYN': 3, 'SKT': 3, 'MON': 2, 'HJB': 2, 'LAT': 2, 'IEC': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-09-05T14:20:01.324Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 - <<'EOF'\np='data/verification/page-93.json'\ns=open(p,encoding='utf-8').read()\nn=s.count('7,32,13')\ns=s.replace('7,32,13','7,33,13')\nopen(p,'w',encoding='utf-8').write(s)\nprint('replaced',n)\nEOF\npython3 -m json.tool data/verification/page-93.json >/dev/null && echo OK && python3 tools/verify_check.py 93"
}
```


### [2026-09-05T14:20:02.997Z] TOOL RESULT

```
replaced 2
OK
nodes verified: 12/12
node verdicts: {'plausible': 7, 'confirmed': 5}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 9, 'partial': 3, 'not_checked': 2}
books consulted: {'supports': 21, 'partial': 10, 'silent': 4, 'contradicts': 3} | by book: {'KLN': 6, 'ETYMONLINE': 5, 'POK': 4, 'WEB': 4, 'WLD': 3, 'SYN': 3, 'SKT': 3, 'MON': 2, 'HJB': 2, 'LAT': 2, 'IEC': 1, 'HRN': 1, 'HUB': 1, 'ARY': 1}
```


## [2026-09-05T14:20:21.152Z] AGENT

Page 93 done. `data/verification/page-93.json` written; `verify_check.py 93` shows 12/12 nodes, 0 PROBLEM lines.

**Verdicts** — root: 1 confirmed (Bhergh part 2 = PIE \*bʰerǵʰ- "high", POK:140–141 exact). Nodes: 5 confirmed, 7 plausible, 0 disputed / transcription_suspect / unverified. Entries 1–4 are redirects (Bheru, Bheu, Bheu 1, Bheu 2) — skipped.

**Main caveats behind the "plausible" verdicts** (all explained in the file, none is a data error):
- #6 Latin *burgus* — not an inherited Latin form (inherited \*bʰr̥ǵʰ- gives f-, cf. forctis); it is a loan from Germanic \*burgs (Ernout-Meillet "mot évidemment germanique", AHD files it under Germanic) or from Greek πύργος (Pokorny). Nourai draws it straight from the root.
- #11 Latin *horctus/forctus/fortis* — forms genuine (Festus 91,14 and 74,14), but the \*bʰr̥ǵʰ-to- etymology is the Brugmann/Walde-Hofmann/Klein/AHD line only; Walde-Pokorny II 173 itself, Ernout-Meillet and Buck prefer \*dʰerǵʰ- "to hold" (Av. drāzaite), and AHD hedges "also possibly from dher-2".
- #8 Persian بورژوا — from **modern** French bourgeois, not Old French burgeis (the -ois > /wa/ change is post-medieval); Mo'in tags it [فر.].
- #4/#5 \*harja-bergaz / harbor — Nourai follows Watkins ("army-hill", ☞Koro), but Kroonen/Etymonline put the second element under the homonym \*bʰergʰ- "to protect".
- #10 — *burglar* rightly under Latin burgus, but *burg* is native OE burg, not via Latin.
- #1 — bṛhánt- solid; bráhman- uncertain (Mayrhofer prefers \*bʰreǵʰ-; Klein "of uncertain origin").

**Ref checks**: POK:140, KLN:194, KNT:201 (verified on the printed lexicon p.201), BQT:269 (leaf 489 of vol. 1, Mo'in's footnote "سانسکریت brāhmaṇa" plus برهمه "مخفف برهمن"), KLN:614, AHD all support; AHD:1509 and MON:601 partial; AHD:156 not_checked (New College main dictionary not on disk — only Watkins's appendix).

**No extraction errors found** — the JSON matches the chart, including the odd-looking but genuine Old Latin `horctus`. 11 web pages archived via `fetch_source.py` (Wiktionary \*bʰerǵʰ-/ब्रह्मन्/برهمن/fortis/PWGmc \*burg, Etymonline bourgeois/burglar/borough/harbor/iceberg, abadis for بورژوا); one fetch, Wiktionary بورژوا, 404s and is not cited.
