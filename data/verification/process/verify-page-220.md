# Verification process log — verify-page-220


## [2026-09-06T15:12:14.659Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 220 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-220.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-220.json. Write /home/sfmqrb/git/rishe/data/verification/page-220.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 220` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:12:16.265Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:12:17.009Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


## [2026-09-06T15:12:17.021Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-220.txt"
}
```


### [2026-09-06T15:12:17.036Z] TOOL RESULT

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


### [2026-09-06T15:12:17.040Z] TOOL RESULT

```
1	=== PDF page 220 (book page 190) ===
2	--- entry 0 ---
3	ROOT [Hebrew] Hebhel : breath, vanity, name of the second son of Adam and Eve  (refs KLN:3)
4	#1 (parent #0) [Arabic] refs=None | 
5	  #2 (parent #1) [Persian] refs=AKM:1; MON6:2237 | Hâbîl «هابیل» : the second son of Adam and Eve
6	#3 (parent #0) [Greek] refs=KLN:3 | Abel
7	  #4 (parent #3) [Latin] refs=None | 
8	    #5 (parent #4) [English] refs=KLN:3 | Abel
9	--- entry 1 ---
10	ROOT [Egyptian] Hebni : ebony tree (common in India)  (refs AHD:411)
11	#1 (parent #0) [Greek] refs=AHD:411 | ebnos : ebony tree
12	  #2 (parent #1) [Pahlavi] refs=MON:26 | âwanos
13	    #3 (parent #2) [Persian] refs=KLN:496; BQT:12 | âbnŭs «آبنوس» : ebony
14	  #4 (parent #1) [Latin] refs=AHD | ebeninus : (made of) ebony
15	    #5 (parent #4) [English] refs=None | ebony
16	--- entry 2 ---
17	ROOT [Semitic] H.j.r : to emigrate  (refs KLN:694)
18	#1 (parent #0) [Arabic] refs=KLN:694 | h.j.r : to emigrate
19	  #2 (parent #1) [Persian] refs=FVA:443 | hejrat «هجرت» : departure, departure of Mohammad from Mecca | extra: هجر ، هجری ، هاجر ، مهجور ، هجران ، مهاجر ، مهاجرت
20	#3 (parent #0) [Hebrew] refs=KLN:694; FSD:1101 | Hâğâr : wandering
21	  #4 (parent #3) [English] refs=FSD:1101 | Hagar : a Biblical name, mother of Ishmael
22	
```


## [2026-09-06T15:12:19.563Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-220.json",
 "description": "Read source JSON for page 220"
}
```


### [2026-09-06T15:12:19.598Z] TOOL RESULT

```
{
  "pdf_page": 220,
  "book_page": 190,
  "entries": [
    {
      "root": {
        "name": "Hebhel",
        "lang": "Hebrew",
        "refs": "KLN:3",
        "gloss": "breath, vanity, name of the second son of Adam and Eve"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "AKM:1; MON6:2237",
          "words": [
            {"translit": "Hâbîl", "gloss": "the second son of Adam and Eve", "script": "هابیل"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "عدوت باد چو هاروت و دوست چون زهره - ولیت باد چو هابیل چون خصم چون قابیل",
            "poet": "Qatrân"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:3",
          "words": [
            {"translit": "Abel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "KLN:3",
          "words": [
            {"translit": "Abel", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Hebni",
        "lang": "Egyptian",
        "refs": "AHD:411",
        "gloss": "ebony tree (common in India)"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:411",
          "words": [
            {"translit": "ebnos", "gloss": "ebony tree", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "MON:26",
          "words": [
            {"translit": "âwanos", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "KLN:496; BQT:12",
          "words": [
            {"translit": "âbnŭs", "gloss": "ebony", "script": "آبنوس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "چو روی هوا چون گشت چون آبنوس - نهادند بر کوهۀ پیل کوس",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "ebeninus", "gloss": "(made of) ebony", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ebony", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "H.j.r",
        "lang": "Semitic",
        "refs": "KLN:694",
        "gloss": "to emigrate"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Arabic",
          "refs": "KLN:694",
          "words": [
            {"translit": "h.j.r", "gloss": "to emigrate", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "FVA:443",
          "words": [
            {"translit": "hejrat", "gloss": "departure, departure of Mohammad from Mecca", "script": "هجرت"}
          ],
          "script_extra": "هجر ، هجری ، هاجر ، مهجور ، هجران ، مهاجر ، مهاجرت",
          "note": null,
          "quote": {
            "text": "از پای فتادیم چو آمد غم هجران - در درد بمردیم چو از دست دوا رفت",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Hebrew",
          "refs": "KLN:694; FSD:1101",
          "words": [
            {"translit": "Hâğâr", "gloss": "wandering", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "FSD:1101",
          "words": [
            {"translit": "Hagar", "gloss": "a Biblical name, mother of Ishmael", "script": null}
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


## [2026-09-06T15:12:21.863Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','MON','BQT','FVA','FSD','AKM','POK','WLD','SKT','WEB','AFM','PLA','LKT','HRN','HUB','PHD','NYB','FVQ','IEC','SYN','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-06T15:12:24.017Z] TOOL RESULT

```
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 202
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
AKM {"title": "Amir J. A'lam, Farhang-e A'lam-e Ketab-e Moqaddas (Dictionary of Proper Names in the Bible, English–Persian), Iran University Press 1988", "kind": "purchase", "url": "in print (Niloofar 1388); gisoom/iketab", "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only."}
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_page
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.t
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-06T15:12:30.174Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','AHD','FSD','BQT','MON','AKM','FVA','LKT','AFM','PLA','FVQ','ARY','SKT','WEB','HJB','DOZ','DEV','PHN','LAM','AFA']:\n    v=d.get(k)\n    if not v: print(k,'MISSING'); continue\n    print('==',k, '| kind:',v.get('kind'),'| local:',v.get('local_file'),'| offset:',v.get('page_offset'))\n    print('   hint:', str(v.get('lookup_hint'))[:300])\n\""
}
```


## [2026-09-06T15:12:30.645Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -80 && echo --- && ls data/verification/ | head"
}
```


### [2026-09-06T15:12:31.891Z] TOOL RESULT

```
== KLN | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== AHD | kind: archive_djvu+website+archive_restricted | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== FSD | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt | offset: vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== BQT | kind: archive_djvu+local_scan_ocr | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== MON | kind: website+archive_djvu | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None
   hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbe
== AKM | kind: purchase | local: None | offset: None
   hint: Not found.
== FVA | kind: catalog | local: None | offset: None
   hint: Searched archive.org, ketabnak, noorlib, web: no digital copy found.
== LKT | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt | offset: leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.
== AFM | kind: archive_djvu | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt'] | offset: 198 leaves; page numerals OCR'd unreliably — offset approx leaf − 8 (front matter); confirm on page image
   hint: Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').
== PLA | kind: archive_djvu | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt'] | offset: 301 leaves (pdftotext -layout, \f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).
   hint: HathiTrust search-only; Google Books id q_ErAAAAMAAJ snippet view; DDB has only the table of contents. No full text online. | For pages in a scanned volume use: python3 tools/ref_page.py PLA:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
== FVQ | kind: archive_djvu | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt'] | offset: printed page = leaf − 17 (0-based \f blocks in FVQ_pages.txt; 335 leaves)
   hint: Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).
== ARY | kind: local_scan_ocr | local: ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt'] | offset: printed page = pdf page + 1
   hint: Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY
== SKT | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt | offset: leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.
== WEB | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt | offset: not reliably detected (page_numbers.json sparse); grep headword. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.
== HJB | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt | offset: leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.490, leaf 905 = p.870). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headwords in caps at line start followed by ', s.' etc., e.g. grep -n '^BAZAAR' HJB.txt. Also online at dsal: https://dsal.uchicago.edu/dictionaries/hobsonjobson/ (search box) which shows page numbers.
== DOZ | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DOZ.txt | offset: leaf = printed + 11..13 (e.g. leaf 15 = p.2, leaf 43 = p.32). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Dutch headword in caps at line start.
== DEV | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt | offset: leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: French headword in caps at line start.
== PHN | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt | offset: leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: French headword in caps at line start; Arabic script not OCRed. grep -n '^BAZAR' etc.
== LAM | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/LAM.txt | offset: leaf = printed + 57 (e.g. leaf 59 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: French headword in caps at line start with running heads like '2 ABRI'.
== AFA | kind: archive_djvu | local: /home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt | offset: leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Arabic/Aramaic in script (not OCRed) with German glosses; grep the German meaning or transliteration.
```


### [2026-09-06T15:12:31.934Z] TOOL RESULT

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
```


## [2026-09-06T15:12:41.635Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Abel\" KLN_1966.txt | head -20; echo ---; grep -n \"Hebhel\\|hebhel\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T15:12:41.698Z] TOOL RESULT

```
1150:Abel,  masc.  PN.;  in  the  Bible,  the  second  son  of Adam  and  Eve.  — -  L.,  fr.  Gk.  ’'A(3eX,  fr.  Heb. Hebhel,  lit.  ‘breath,  vanity’, abeie,  n.,  the  white  poplar.  —  Du.  abeel,  fr.  OF. aubel,  albel,  fr.  VL.  *albellus,  ‘whitish’,  dimin. of  albulus,  which  itself  is  dimin.  of  albus, ‘white’.  See  alb.
1151:Abelmoschus,  n.,  a  genus  of  plants  of  the  mallow family  (bot.)  —  ModL.,  fr.  Arab,  habb-al-musk, in  vulgar  pronunciation  habb-el-mosk,  lit.  ‘grain of  musk’.  See  hubba  and  musk, abelmosk,  n„  a  plant  of  the  mallow  family.  — Fr.  prec.  word.
---
1150:Abel,  masc.  PN.;  in  the  Bible,  the  second  son  of Adam  and  Eve.  — -  L.,  fr.  Gk.  ’'A(3eX,  fr.  Heb. Hebhel,  lit.  ‘breath,  vanity’, abeie,  n.,  the  white  poplar.  —  Du.  abeel,  fr.  OF. aubel,  albel,  fr.  VL.  *albellus,  ‘whitish’,  dimin. of  albulus,  which  itself  is  dimin.  of  albus, ‘white’.  See  alb.
6015:cable,  n.  —  ME.  cable,  cabel,  kable,  fr.  F.  cable, fr.  Port,  cable,  which  is  a  blend  of  Arab,  habl, ‘rope,  cable’,  and  VL.  cap(u)lum,  ‘a  halter  for cattle’,  fr.  capid,  capere,  ‘to  catch,  seize,  take, hold’.  Arab,  habl  is  rel.  to  habala,  ‘he  bound’, Heb.  hebhel,  ‘rope,  cord’,  Ethiop.  habal,  ‘rope’, habala,  ‘he  bound’,  Akkad,  nahbalu,  ‘rope, snare’,  Aram,  habhld,  ‘cord,  rope’.  For  the  ety¬ mology  of  L.  capere  see  captive.
31683:Derivatives:  rap-er,  n.,  rap-ist,  n. rape,  n.,  one  of  the  six  divisions  of  Sussex.  — First  mentioned  in  Domesday  Book;  perh.  fr. rape,  an  obsol.  var.  of  rope,  used  in  the  sense  of ‘measure’.  For  sense  development  cp.  Heb. hebhel,  ‘rope;  measure’.
```


## [2026-09-06T15:12:42.482Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^Hegira\\|^hegira\\|Hijrah\\|hijrah\\|Hegira\" KLN_1966.txt | head -20; echo ---HAGAR---; grep -n \"Hagar\" KLN_1966.txt | head -20"
}
```


### [2026-09-06T15:12:42.556Z] TOOL RESULT

```
17444:hegira,  n.,  the  flight  of  Mohammed  from  Mecca (in  622).  —  Arab.  hljrah,  ‘flight’,  fr.  hajara,  ‘he fled,  emigrated’.  Cp.  Hagar. hegumen,  n.,  the  first  official  in  a  monastery  of  an Orthodox  Eastern  Church.  —  ML.  hegumenus, fr.  Gk.  •r)Y°V£V°S>  'it-  ‘leading’,  pres.  part,  of ■fjYEicOai,  ‘to  lead’.  See  hegemony.  For  the  suff. -pevoi;  see  alumnus  and  cp.  words  there  re¬ ferred  to.
---HAGAR---
17025:Hagar,  n.,  Sarah’s  Egyptian  handmaid  (Bible).  — Heb.  Haghdr,  prob.  rel.  to  Arab,  ha  jar  a,  ‘he fled,  emigrated’,  hijra",  ‘flight,  emigration’.  See hegira.
17444:hegira,  n.,  the  flight  of  Mohammed  from  Mecca (in  622).  —  Arab.  hljrah,  ‘flight’,  fr.  hajara,  ‘he fled,  emigrated’.  Cp.  Hagar. hegumen,  n.,  the  first  official  in  a  monastery  of  an Orthodox  Eastern  Church.  —  ML.  hegumenus, fr.  Gk.  •r)Y°V£V°S>  'it-  ‘leading’,  pres.  part,  of ■fjYEicOai,  ‘to  lead’.  See  hegemony.  For  the  suff. -pevoi;  see  alumnus  and  cp.  words  there  re¬ ferred  to.
19959:Ishmael,  n.,  son  of  Abraham  and  Hagar  (Bible); used  in  a  figurative  sense  to  denote  an  outcast (see  Gen.  16:12)  —  Heb.  Yishmafl,  lit.  ‘God hears’.  Heb.  yishmd',  ‘he  will  hear’,  is  imperf. of  shdmd,  ‘he  heard’.  See  Sbema  and  cp.  Simeon, Simon.  For  the  second  element  in  the  name Ishmael  see  El  and  cp.  words  there  referred  to. Derivative:  Ishmael-ite,  n.
```


## [2026-09-06T15:12:50.832Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ndef leaf_of_line(n):\n    return t.count('\\f','',sum(len(l)+1 for l in lines[:n-1]))\n# simpler: index\nfor target in [1150,17025,17444]:\n    off=sum(len(l)+1 for l in lines[:target-1])\n    print(target,'leaf',t.count('\\f',0,off))\nEOF"
}
```


## [2026-09-06T15:12:52.545Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ebony\\|^ebon\\b\\|ebenus\\|ebeninus\\|hbnj\\|Egypt.*ebony\" KLN_1966.txt | head -20; echo ---AHD---; grep -n -i \"ebony\\|ebenus\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T15:12:53.086Z] TOOL RESULT

```
1150 leaf 13
17025 leaf 374
17444 leaf 385
```


### [2026-09-06T15:12:53.150Z] TOOL RESULT

```
12575:Ebenaceae,  n.pl.,  the  ebony  family  (hot.)  — ModL.,  formed  with  suff.  -aceae  fr.  L.  ebenus. See  ebony.
12580:ebony,  n.  —  OF.  ebaine  (F.  ebdne),  fr.  L.  ebenus (whence  also  OHG.,  MHG.  ebenus,  G.  Eben- hoiz),  fr.  Gk.  spevo?  (whence  also  Arabo- Persian  abatis),  fr.  Egypt,  hebni  (whence  also Heb.  pi.  hobhnim,  Ezek.  27:15).
---AHD---
```


## [2026-09-06T15:13:10.131Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [12575,12580]:\n    off=sum(len(l)+1 for l in lines[:target-1])\n    print(target,'leaf',t.count('\\f',0,off))\nEOF\necho ---FSD2---\ngrep -n \"^Hagar\\|Hagar,\" FSD_vol2.txt 2>/dev/null | head -10"
}
```


## [2026-09-06T15:13:10.338Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo ---MON---; grep -n \"آبنوس\" MON_part1.txt | head -10; echo ---BQT1---; grep -n \"آبنوس\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-06T15:13:11.906Z] TOOL RESULT

```
12575 leaf 270
12580 leaf 270
---FSD2---
61894:rsiand.  Janan.  de.sceudant  of  Islim.a6l,  Abraham’s  son  by  Hagar,  and,
```


### [2026-09-06T15:13:11.972Z] TOOL RESULT

```
---MON---
38781:آن. تخت آبنوس (آبنوسی): تختی که از 
38782:چوب آبنوس ساخته باشند. (کد.) شب. 
50126:شکاعی. قر قره. چرخ آبنوس: (کد.) آسمان 
88156:شیز: 112 [- معر. شیزی] (ا.) (گیاء) آبنوس 
---BQT1---
6423:آبنوسی شاخ ) » سوری ()
```


## [2026-09-06T15:13:19.238Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 220 221 222 223 224; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' BQT_v1_pages.txt | head -60; done"
}
```


### [2026-09-06T15:13:22.066Z] TOOL RESULT

```
=== leaf 220 ===
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
آبنوی خوانند . اکر بر آتش نهند مانند عود
بکدازد و بوی خوی دهد . و اکر با آب (ه)
بسابند و در چشم کشند شب کوری را برد
و خوردن آن سنکگ مثانه را بریزاند - و نوعی
از ماهی حم‌هست بسیار لذمف -
آبنوسی شاخ ) » سوری ()
را گوند و آن را شهنای هم خوانند - و نایی
را ی زگویند که از چوب آبنوی ساخته باشند .
]بو « ین ثاك و سکون واو » کل
یلوفر را گویند .
- آب ودد ه بح واد و سکون ثالث
و رای بی هطه و زای قطمدار + شناور و شنا
کننده را گویند.
آ وق بضم بای فارسی و سکون واو
و فاف » آنت که کسی دهان خود را برباد کند
و دیگری چنان دستی بر آن زند که آن باد با
صدا ازدهان او برآید ‏
آب و فد » پروزن پای‌بند ؛ ظرفآب
را گویند » چه ود بلنتی ظرف است مطلفاً -
4۲ - بنتح نالت م دام قربه‌ایست از فرای
ساوه ؟ .
(4) خم ۲ : انگور. (ه) خم ۲ : یاب .
که درخت آن در
=== leaf 221 ===
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
=== leaf 222 ===
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
=== leaf 223 ===
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
=== leaf 224 ===
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
آکش فروذ -ب بسن آش افرز اس
و آن ظرفی باشد بهیأت سر آدمی و سوراخ
گذارند , بغاری از آن موراخ برآید و آش
ملکی بزدجردی - و پر نددای هم حست که آ را
ولام , کنابه از اسپ جلد و"ند وتیز باشد (۳) .
۲ تثك « بفتح الث و راببم و سکون
کاف » بمعنی برق باشد  -‏ وکرم شب تاب را یز
به‌پروانه » و کویند آن روشنی از فسَلةٌ اوست
و سم
۲تشکار- بی وزن آ تشبار مءکنابه از
خشمگن و ز ده و ید کاره باشد . و گلخنی
۵ آتش‌زی - آش‌زنه » چضاق .
۵ آش فارسی - رك : اش پارسی -
( بر های قاطع ۷)
```


## [2026-09-06T15:13:31.738Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==221' BQT_v1_pages.txt | tail -30"
}
```


## [2026-09-06T15:13:32.890Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '38770,38790p' MON_part1.txt; echo \"=== search MON for هابیل ===\"; grep -n \"هابیل\" MON_part1.txt MON_part2.txt | head"
}
```


### [2026-09-06T15:13:33.487Z] TOOL RESULT

```
باشد ٩‏ .
آب نافع - بکسر الث وفا » کنابه
از شراب انگوری باشد .
اب ثتخوردن « کنابه از درنگه با
کردن و توقف تمودق پلشد ۰ _ ۱
آ نوس - بس وزن خاکبوی درختی
باشد سیاه ۴ و مشهور است و آنرا سربی نیز
آبنوی خوانند . اکر بر آتش نهند مانند عود
بکدازد و بوی خوی دهد . و اکر با آب (ه)
بسابند و در چشم کشند شب کوری را برد
و خوردن آن سنکگ مثانه را بریزاند - و نوعی
از ماهی حم‌هست بسیار لذمف -
آبنوسی شاخ ) » سوری ()
را گوند و آن را شهنای هم خوانند - و نایی
را ی زگویند که از چوب آبنوی ساخته باشند .
]بو « ین ثاك و سکون واو » کل
یلوفر را گویند .
- آب ودد ه بح واد و سکون ثالث
و رای بی هطه و زای قطمدار + شناور و شنا
کننده را گویند.
آ وق بضم بای فارسی و سکون واو
و فاف » آنت که کسی دهان خود را برباد کند
و دیگری چنان دستی بر آن زند که آن باد با
صدا ازدهان او برآید ‏
آب و فد » پروزن پای‌بند ؛ ظرفآب
را گویند » چه ود بلنتی ظرف است مطلفاً -
4۲ - بنتح نالت م دام قربه‌ایست از فرای
ساوه ؟ .
(4) خم ۲ : انگور. (ه) خم ۲ : یاب .
که درخت آن در
```


### [2026-09-06T15:13:33.564Z] TOOL RESULT

```
تباهی خرد؛ ناقص عقلی؛ ج. تخبطات. 
تخبیر: للع | (مصم) خبر دادن 
آگاه کردن» آ گاهانیدن. (امص.) آ گاهی؛ ج. 
تحیرات. 
تخت: ۱۵ (ا.) کرسی» نشیمنگاه چوبین با 
آهنین چهار پایه. منبر. اریکةٌ سلطنت؛ 
کرسیی که شاه در روز باروسلام روی آن 
نشند. شهر و مقر سلطنت. هر جای مر تفعی 
از زمین که در روی آن نشینند و خوابند و 
تکه کنند. هر جای مسطح و برابر و هموار. 
(اخ.) عرش خدا. کف کفش» گیوه و مانند 
آن. تخت آبنوس (آبنوسی): تختی که از 
چوب آبنوس ساخته باشند. (کد.) شب. 
تخت حاسب (حاسبان» حساب» محاسب» 
محاسبان): تخته‌ای که محاسبان و منجمان 
خاک نرم بر آن ریزند و با میل آهننین با 
چوبین اعداد و نقوش طالع بر آن نویسند و 
حساب کنند. . تحت حر بر : (کد.) گل. تحت 
سینه: (عم.) وسط سینه. تخت عاج: تختی که 
از عاج (دندان لب ۳-3 
روز. (کد.) سرین» شرمگاه. تخت فبروزه: 
=== search MON for هابیل ===
```


## [2026-09-06T15:13:41.401Z] TOOL CALL #16: Bash

```json
{
 "command": "sed -n '1,60p' tools/fetch_source.py"
}
```


### [2026-09-06T15:13:41.469Z] TOOL RESULT

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
        with urllib.request.urlopen(req, timeout=60) as r:
            status = r.status
            raw = r.read(4_000_000)
            ctype = r.headers.get("Content-Type", "")
            enc = "utf-8"
            m = re.search(r"charset=([\w-]+)", ctype)
            if m: enc = m.group(1)
            body = raw.decode(enc, errors="replace")
            if "html" in ctype or body.lstrip().lower().startswith("<!doctype html") or "<html" in body[:2000].lower():
                mt = re.search(r"(?is)<title>(.*?)</title>", body)
```


## [2026-09-06T15:13:43.010Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ابنوس\" MON_part1.txt | head -5; echo ---AFM---; grep -n \"بنوس\" AFM_pages.txt | head -10; echo ---PLA---; grep -n -i \"abanūs\\|abanus\\|Ebenholz\" incoming/PLA/PLA_pages.txt | head -10"
}
```


### [2026-09-06T15:13:43.093Z] TOOL RESULT

```
---AFM---
2325:آبنوس وغيرهم الشيزى او شجر تعمل ܘܬܘ ܐܢܝܢ ( حيط الحيط ٠)‏ لعل معنى ساسم
2707:5 خشب 731 الا بنوس وهذا صحيح 559 بالفارسيّة معناه
2708:آلا بنوس
---PLA---
```


## [2026-09-06T15:13:48.031Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2695,2720p' AFM_pages.txt; echo \"=== leafnum ===\"; python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [2325,2707]:\n    off=sum(len(l)+1 for l in lines[:target-1])\n    print(target,'leaf',t.count('\\f',0,off))\nEOF"
}
```


### [2026-09-06T15:13:50.131Z] TOOL RESULT

```
١ >‏ الشُوَيل 6 - به وهو كو يلا بالقارسة
( الغاه :فازمى يحت ܙܕ الله
(الشأشكان). موباعفان الوشيقى فارسّة
(شاه بأُوط ) فارسي”
( الشورنيذ والشهني) اللبة السوداء تعريب شُييز
ܫ (الشيء : ) تفريب حي وهو مخف جز بالفارسيّة وهو من موافتات اللغسنات
5 7 5 ܐ 29 0 ܨܝ و6وملاء بالفرنسة
و6053 0 ® و ¢1153 باللائينة ܐ بالتركة ܝܣ }ܨܭ 4 و طننا86
بالروسة
د £ ܨ 9 فارساتة &80
± (الشِيز والشيرزى ) خشب 13638 مله القضاع ܙ مغاط ܐ قو
ܢ<
5 خشب 731 الا بنوس وهذا صحيح 559 بالفارسيّة معناه
آلا بنوس
( الشِيطرَج ) دواء نافع ܝ ܐܬܟܐ والمهق ܨ 06 0 باصل ܢܐܝ
احمر حاد دقيق يقال له بالعربيّة مسواك الراعى وبالتركية سر كله ١‏ البرهان
القاطع) = :
+ 17( 3 .ܨ ܝ “قال في البرهان ܗ عد
ܓ فلوس على ظهره نقط سود يقال له 05512
وبالتركية « ايت بالغى »
(3الغاف ) غنت على وه مارك
ܒ̈ 2 .(م 25م )جرع
ܐܝ الصاد
* ( @ : الثمر )© 693 3
03 مطوخ مركي من الزيت او من الشحم وغيرثما والقلى ٠‏ وهو صابون
0 ® والتركة والكرد نه . 01.97 ® و0215 , 9220 0297 ܕ @$611
=== leafnum ===
2325 leaf 92
2707 leaf 107
```


## [2026-09-06T15:14:01.075Z] TOOL CALL #19: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/ebony\" \\\n\"https://www.etymonline.com/word/ebony\" \\\n\"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D9%86%D9%88%D8%B3\" \\\n\"https://en.wiktionary.org/wiki/%E1%BC%94%CE%B2%CE%B5%CE%BD%CE%BF%CF%82\" \\\n\"https://en.wiktionary.org/wiki/Abel\" \\\n\"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%A8%D9%8A%D9%84\" ; do\npython3 tools/fetch_source.py \"$u\" --note \"page 220 verification (Hebhel/Abel, Hebni/ebony)\"; done"
}
```


## [2026-09-06T15:14:03.925Z] TOOL CALL #20: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/%D9%87%D8%AC%D8%B1%D8%A9\" \\\n\"https://en.wiktionary.org/wiki/%D9%87%D8%AC%D8%B1%D8%AA\" \\\n\"https://en.wiktionary.org/wiki/Hagar\" \\\n\"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%AC%D8%B1\" \\\n\"https://www.etymonline.com/word/hegira\" \\\n\"https://en.wiktionary.org/wiki/%D7%94%D6%B6%D7%91%D6%B6%D7%9C\" ; do\npython3 tools/fetch_source.py \"$u\" --note \"page 220 verification (H.j.r/hejrat/Hagar; Hebhel)\"; done"
}
```


### [2026-09-06T15:14:09.229Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/48fb3cba14fe5c67.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6684c84a7c2cbe0d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b1cacbd820d51863.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55002e68dc315671.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/156592c175c84f7e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/07febddbd06c2abd.txt
```


### [2026-09-06T15:14:14.254Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/32043850e3630e68.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e3e7aa5b50337f78.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/14bd516e0166bcce.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b07cc39f299ed266.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5ad3194268c9a89f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/351d7060db452036.txt
```


## [2026-09-06T15:14:16.842Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 48fb3cba14fe5c67 b1cacbd820d51863 55002e68dc315671; do echo \"########## $f\"; head -c 3000 $f.txt | sed -n '1,200p'; echo; done"
}
```


### [2026-09-06T15:14:18.367Z] TOOL RESULT

```
########## 48fb3cba14fe5c67
URL: https://en.wiktionary.org/wiki/ebony
FETCHED: 2026-09-06T15:14:03Z
STATUS: 200
TITLE: ebony - Wiktionary, the free dictionary

ebony - Wiktionary, the free dictionary 

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
 English 

 Toggle English subsection 

 1.1 
 Etymology 

 1.2 
 Pronunciation 

 1.3 
 Noun 

 1.3.1 
 Derived terms 

 1.3.2 
 Related terms 

 1.3.3 
 Translations 

 1.4 
 Adjective 

 1.4.1 
 Derived terms 

 1.4.2 
 Translations 

 1.5 
 See also 

 1.6 
 Further reading 

 1.7 
 Anagrams 

 Toggle the table of contents 

 ebony 

 39 languages 

 বাংলা 
 Čeština 
 Ελληνικά 
 Esperanto 
 Español 
 Eesti 
 فارسی 
 Suomi 
 Français 
 Galego 
 Magyar 
 Հայերեն 
 Ido 
 Italiano 
 日本語 
 ಕನ್ನಡ 
 한국어 
 Kurdî 
 Malagasy 
 മലയാളം 
 မြန်မာဘာသာ 
 Nederlands 
 Norsk bokmål 
 Oromoo 
 Polski 
 Română 
 Русский 
 Sängö 
 တႆး 
 Simple English 
 Slovenčina 
 Kiswahili 
 தமிழ் 
 తెలుగు 
 Tagalog 
 Türkçe 
 اردو 
 Tiếng Việt 
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

 See also: Ebony 

 English
 [ edit ] 

 WOTD – 12 March 2010 , 12 March 2011 

########## b1cacbd820d51863
URL: https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D9%86%D9%88%D8%B3
FETCHED: 2026-09-06T15:14:05Z
STATUS: 200
TITLE: آبنوس - Wiktionary, the free dictionary

آبنوس - Wiktionary, the free dictionary 

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
 Ottoman Turkish 

 Toggle Ottoman Turkish subsection 

 1.1 
 Noun 

 2 
 Persian 

 Toggle Persian subsection 

 2.1 
 Alternative forms 

 2.2 
 Etymology 

 2.3 
 Pronunciation 

 2.4 
 Noun 

 2.4.1 
 Descendants 

 2.5 
 Further reading 

 Toggle the table of contents 

 آبنوس 

 9 languages 

 Deutsch 
 فارسی 
 Malagasy 
 Polski 
 پنجابی 
 پښتو 
 سرائیکی 
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

 Ottoman Turkish
 [ edit ] 

 Noun
 [ edit ] 

 آبنوس • ( abnûs ) 

 alternative spelling of آبانوز 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: آبنوس 

 Wikipedia fa 

 Alternative forms
 [ edit ] 

 آونوس ( āwnūs  / âvnus ) 

 Etymology
 [ edit ] 

 Inherited from Middle Persian 𐫀𐫛𐫗𐫇𐫘 ( ʾpnws /⁠abnūs⁠/ ) , from Ancient Greek ἔβενος ( ébenos ) , from Egyptian hbnj ( “ ebony ” ) . 

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ʔaːb.ˈnuːs/ 

 ( Dari, formal ) IPA ( key ) : [ʔɑːb.nuːs] 

 ( Dari, formal ) IPA ( key ) : [ʔɑːb.nuːs] 
 ( Kabuli ) IPA ( key ) : [ʔɑːb.nuːs] 

 ( Hazaragi ) IPA ( key ) : [ʔɔːb.nus] 

 ( Iran, formal ) IPA ( key ) : [ʔɒːb.nuːs] 

 ( Tajik, formal ) IPA ( key ) : [ʔɔb.nus] 

 Rhymes: -uːs 

 Readings

########## 55002e68dc315671
URL: https://en.wiktionary.org/wiki/%E1%BC%94%CE%B2%CE%B5%CE%BD%CE%BF%CF%82
FETCHED: 2026-09-06T15:14:05Z
STATUS: 200
TITLE: ἔβενος - Wiktionary, the free dictionary

ἔβενος - Wiktionary, the free dictionary 

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
 Ancient Greek 

 Toggle Ancient Greek subsection 

 1.1 
 Alternative forms 

 1.2 
 Etymology 

 1.3 
 Pronunciation 

 1.4 
 Noun 

 1.4.1 
 Inflection 

 1.4.2 
 Derived terms 

 1.4.3 
 Descendants 

 1.5 
 References 

 Toggle the table of contents 

 ἔβενος 

 9 languages 

 Eesti 
 Français 
 Italiano 
 한국어 
 Kurdî 
 Malagasy 
 Polski 
 Русский 
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

 See also: έβενος 

 Ancient Greek
 [ edit ] 

 Alternative forms
 [ edit ] 

 ἔβελος ( ébelos ) , ἐβένη ( ebénē ) 

 Etymology
 [ edit ] 

 Borrowed from Egyptian hbnj , 

 Pronunciation
 [ edit ] 

 IPA ( key ) : /é.be.nos/ → /ˈe.βe.nos/ → /ˈe.ve.nos/ 

 ( 5 th BCE Attic ) IPA ( key ) : /é.be.nos/ 

 ( 1 st CE Egyptian ) IPA ( key ) : /ˈe.be.nos/ 

 ( 4 th CE Koine ) IPA ( key ) : /ˈe.βe.nos/ 

 ( 10 th CE Byzantine ) IPA ( key ) : /ˈe.ve.nos/ 

 ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈe.ve.nos/ 

 Noun
 [ edit ] 

 ἔβενος • ( ébenos )  f or m ( genitive ἐβένου ) ; second declension 

 ebony tree, wood

 Inflection
 [ edit ] 

 Second declension of ὁ ἔβενος ; τοῦ ἐβένου ( Attic )

 Case / #

 Singular

 Dual
```


## [2026-09-06T15:14:27.411Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== ebony wikt etym ===\"; grep -n -A25 \"^ Etymology$\" 48fb3cba14fe5c67.txt | head -60; echo; echo \"=== etymonline ebony ===\"; grep -n -i -B2 -A20 \"ebony\" 6684c84a7c2cbe0d.txt | sed -n '1,80p'"
}
```


### [2026-09-06T15:14:29.338Z] TOOL RESULT

```
=== ebony wikt etym ===
203: Etymology
204- [ edit ] 
205-
206- Etymology tree
207-
208- Egyptian 
209-
210- ( hbnj ) bor. 
211- Ancient Greek ἕβενος ( hébenos ) bor. 
212- Latin hebenus 
213-
214- Proto-Indo-European *-(i)yós 
215- Proto-Italic *-ijos 
216- Proto-Italic *-ios 
217- Old Latin -ios 
218- Latin -ius 
219-
220- Latin ebenius der. 
221- Middle English ebenif 
222- English heben, hebeny 
223- English ebony 
224-
225-From earlier heben , hebeny , from Middle English ebenif , hebenyf (influenced by Late Latin hebeninus ), from Ecclesiastical Latin ebenius ( “ of ebony ” ) , from Latin hebenus ( “ ebon tree ” ) , from Ancient Greek ἔβενος ( ébenos ) , from Egyptian hbnj , 
226-
227- Pronunciation
228- [ edit ] 

=== etymonline ebony ===
1:URL: https://www.etymonline.com/word/ebony
2-FETCHED: 2026-09-06T15:14:03Z
3-STATUS: 200
4:TITLE: Ebony - Etymology, Origin & Meaning
5-
6:Ebony - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
13- Apps 
14- Premium 
15-
16- Log in 
17-
18- Advertisement Remove Ads 
19- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
20-
21: Origin and history of ebony 
22-
23: ebony (n.) 
24-
25: dark, hard wood favored for carving, musical instruments, etc., 1590s, perhaps an extended form of Middle English ebon , or from hebenyf (late 14c.), perhaps a Middle English misreading of Latin hebeninus "of ebony," from Greek ebeninos , from ebenos "ebony," probably from Egyptian hbnj or another Semitic source. Figurative use to suggest intense blackness is from 1620s. As an adjective, "of ebony, made of ebony," from 1590s; in reference to skin color of Africans, by 1813. French ébène , Old High German ebenus (German Ebenholz ) are from Latin ebenus .
26- also from 1590s 
27-
28: Entries linking to ebony 
29-
30- ebon (n.) 
31-
32: early 15c., "ebony wood, ebony tree," from Old French ebene or directly from Latin ebenus (see ebony ). As an adjective, "made of ebony," from 1590s. Figurative sense of "dark, black" is from 1590s; in some cases a poetic shortening of ebony .
33-
34- Ebonics (n.) 
35-
36: "African-American vernacular English," 1975, as title of a book edited by U.S. professor Robert L. Williams (1930-2020), who is said to have coined the word as a blend of ebony and phonics .
37-
38- Advertisement Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
39-
40- More to explore
41-
42- sable 
43-
44- early 15c., "fur or pelt of the European sable" (Martes zibellina), from Old French sable (also martre sable "sable martin"), in reference to the carnivorous arctic mammal or its highly prized fur, borrowed in French from Germanic (compare Middle Dutch sabel, Middle Low German sa
45-
46- wood 
47-
48- Old English wudu, earlier widu "tree, trees collectively, forest, grove; the substance of which trees are made," from Proto-Germanic *widu- (source also of Old Norse viðr, Danish and Swedish ved "tree, wood," Old High German witu "wood"), from PIE *widhu- "tree, wood" (source als
49-
50- bone 
51-
52- Middle English bon, from Old English ban "bone, tusk, hard animal tissue forming the substance of the skeleton; one of the parts which make up the skeleton," from Proto-Germanic *bainan (source also of Old Frisian and Old Saxon ben, Old Norse bein, Danish ben, German Bein). Absen
53-
54- tree 
55-
56- Old English treo, treow "tree" (also "timber, wood, beam, log, stake"), from Proto-Germanic *trewam (source also of Old Frisian tre, Old Saxon trio, Old Norse tre, Gothic triu "tree"), from PIE *drew-o-, suffixed variant form of root *deru- "be firm, solid, steadfast," with speci
--
80- 1530s, "to windward," from a- (1) "on" + Middle English loof "windward direction," which is probably from Dutch loef (Middle Dutch lof) "the weather side of a ship" (see luff (n.)). Originally in nautical orders to keep the ship's head to the wind, and thus stay clear of a lee-sh
81-
82: Share ebony 
83-
84- ‘ cite ’ 
85- Page URL :
86: https://www.etymonline.com/word/ebony Copy 
87-
88- HTML Link :
89: <a href="https://www.etymonline.com/word/ebony">Etymology of ebony by etymonline</a> Copy 
90-
91- APA Style :
92: Harper, D. (n.d.). Etymology of ebony. Online Etymology Dictionary. Retrieved September 5, 2026, from https://www.etymonline.com/word/ebony Copy 
93-
94- Chicago Style :
95: Harper Douglas, "Etymology of ebony," Online Etymology Dictionary, accessed September 5, 2026, https://www.etymonline.com/word/ebony. Copy 
96-
97- MLA Style :
98: Harper, Douglas. "Etymology of ebony." Online Etymology Dictionary, https://www.etymonline.com/word/ebony. Accessed 5 September, 2026. Copy 
99-
100- IEEE Style :
101: D. Harper. "Etymology of ebony." Online Etymology Dictionary. https://www.etymonline.com/word/ebony (accessed September 5, 2026). Copy 
102-
```


## [2026-09-06T15:14:36.264Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== Abel wikt ===\"; sed -n '/^ Translingual\\|^ English$/,$p' 156592c175c84f7e.txt | grep -n -A12 \"Etymology\" | head -70"
}
```


## [2026-09-06T15:14:37.686Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== هابيل ===\"; grep -n -A14 \"Etymology\" 07febddbd06c2abd.txt | head -60; echo \"=== hevel הבל ===\"; grep -n -A14 \"Etymology\" 351d7060db452036.txt | head -60"
}
```


### [2026-09-06T15:14:37.982Z] TOOL RESULT

```
=== Abel wikt ===
9: Etymology
10- [ edit ] 
11-
12: Etymology tree
13-
14- Biblical Hebrew הָ֑בֶל ( háḇel ) bor. 
15- Ancient Greek Ἅβελ ( Hábel ) bor. 
16- Latin Abē̆l der. 
17- Old English Ābel 
18- Middle English Abel 
19- English Abel 
20-
21- From Middle English Abel , from Old English Ābel , from Latin Abel , from Ancient Greek Ἅβελ ( Hábel ) , from Biblical Hebrew הֶבֶל ( Héḇel , “ Abel ” ) , possibly from the homonymous word הֶבֶל ( heḇel , “ breath, vapor; vanity ” ) or from Akkadian 𒌉𒍑 ( ablu , “ son ” ) .
22-
23- Pronunciation
24- [ edit ] 
--
246: Etymology
247- [ edit ] 
248-
249- From Late Latin Abel , from Ancient Greek Ἅβελ ( Hábel ) , from Hebrew הֶ֫בֶל .
250-
251- Pronunciation
252- [ edit ] 
253-
254- IPA ( key ) : ( Northern ) [əˈβe̞l] 
255-
256- IPA ( key ) : ( Balearic ) [əˈbɛl] 
257-
258- IPA ( key ) : ( Central ) [əˈβɛl] 
--
281: Etymology
282- [ edit ] 
283-
284- Ultimately from Ancient Greek Ἅβελ ( Hábel ) , from Biblical Hebrew הֶבֶל ( hével ) .
285-
286- Pronunciation
287- [ edit ] 
288-
289- IPA ( key ) : /ˈaː.bəl/ 
290-
291- Audio : ( file ) 
292-
293- Hyphenation: Abel 
--
400: Etymology
401- [ edit ] 
402-
403: Etymology tree
404-
405- Biblical Hebrew הָ֑בֶל ( háḇel ) bor. 
406- Ancient Greek Ἅβελ ( Hábel ) bor. 
407- Latin Abē̆l 
408-
409- Borrowed from Ancient Greek Ἅβελ ( Hábel ) , itself from Biblical Hebrew הֶ֫בֶל ( heḇel ) . The vowel, while short by etymology, is shown to be carrying stress by the descended Italian Abele and Spanish Abel .
410-
411- Pronunciation
412- [ edit ] 
413-
414- ( Classical Latin ) IPA ( key ) : [ˈa.beːɫ] , [ˈa.bɛɫ] 
415-
--
470: Etymology
471- [ edit ] 
472-
473- From Latin Abel , from Ancient Greek Ἅβελ ( Hábel ) , from Hebrew הֶ֫בֶל 
474-
475- Proper noun
476- [ edit ] 
477-
```


### [2026-09-06T15:14:38.036Z] TOOL RESULT

```
=== هابيل ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
69-
70- 1.3.1 
71- Declension 
72-
73- Toggle the table of contents 
74-
75- هابيل 
76-
--
144: Etymology
145- [ edit ] 
146-
147- From Classical Syriac ܗܰܒܶܝܠ ( hābēl ) .
148-
149- Pronunciation
150- [ edit ] 
151-
152- IPA ( key ) : /haː.biːl/ 
153-
154- Rhymes: -iːl 
155-
156- Proper noun
157- [ edit ] 
158-
=== hevel הבל ===
```


## [2026-09-06T15:14:47.633Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== هجرة ===\"; grep -n -A16 \"Etymology\" 32043850e3630e68.txt | sed -n '1,60p'; echo \"=== هجرت ===\"; grep -n -A16 \"Etymology\" e3e7aa5b50337f78.txt | sed -n '1,60p'"
}
```


### [2026-09-06T15:14:47.710Z] TOOL RESULT

```
=== هجرة ===
=== هجرت ===
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Descendants 
69-
70- 2 
71- Persian 
72-
73- Toggle Persian subsection 
74-
75- 2.1 
76: Etymology 
77-
78- 2.2 
79- Pronunciation 
80-
81- 2.3 
82- Noun 
83-
84- 2.3.1 
85- Descendants 
86-
87- Toggle the table of contents 
88-
89- هجرت 
90-
91- 6 languages 
92-
--
157: Etymology
158- [ edit ] 
159-
160- From Arabic هِجْرَة ( hijra ) . 
161-
162- Noun
163- [ edit ] 
164-
165- هجرت • ( hicret ) 
166-
167- ( Islam ) Hegira , Hijra 
168-
169- ( Islam ) hegira , hijra 
170-
171- Descendants
172- [ edit ] 
173-
--
183: Etymology
184- [ edit ] 
185-
186- Borrowed from Arabic هِجْرَة ( hijra ) .
187-
188- Pronunciation
189- [ edit ] 
190-
191- ( Classical Persian ) IPA ( key ) : /hid͡ʒ.ˈrat/ 
192-
```


## [2026-09-06T15:14:48.981Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== Hagar wikt ===\"; grep -n -A16 \"Etymology\" 14bd516e0166bcce.txt | sed -n '1,60p'; echo \"=== هاجر ===\"; grep -n -A12 \"Etymology\" b07cc39f299ed266.txt | sed -n '1,60p'"
}
```


### [2026-09-06T15:14:49.049Z] TOOL RESULT

```
=== Hagar wikt ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
69-
70- 1.3.1 
71- Quotations 
72-
73- 1.3.2 
74- Translations 
75-
76- 1.4 
77- Anagrams 
78-
--
178: Etymology
179- [ edit ] 
180-
181- From Hebrew הָגָר ( Hagar , “ stranger ” ) . Compare Arabic هَاجَر ( hājar ) , Tiberian Hebrew הָגָר ( Hāḡār ) .
182-
183- Pronunciation
184- [ edit ] 
185-
186- ( Received Pronunciation ) IPA ( key ) : /ˈheɪɡɑː/ 
187-
188- Audio ( Southern England ) : ( file ) 
189-
190- ( US ) IPA ( key ) : /ˈheɪɡɑːɹ/ 
191-
192- Proper noun
193- [ edit ] 
194-
=== هاجر ===
62: Etymology 1 
63-
64- 1.1.1 
65- Verb 
66-
67- 1.1.1.1 
68- Conjugation 
69-
70- 1.1.2 
71- Noun 
72-
73- 1.1.2.1 
74- Declension 
--
77: Etymology 2 
78-
79- 1.2.1 
80- Pronunciation 
81-
82- 1.2.2 
83- Proper noun 
84-
85- 1.2.2.1 
86- Declension 
87-
88- 2 
89- Iraqi Arabic 
--
94: Etymology 
95-
96- 2.2 
97- Pronunciation 
98-
99- 2.3 
100- Verb 
101-
102- 2.3.1 
103- Conjugation 
104-
105- 3 
106- South Levantine Arabic 
--
111: Etymology 
112-
113- 3.2 
114- Pronunciation 
115-
116- 3.3 
117- Verb 
118-
119- 3.3.1 
120- Conjugation 
121-
122- Toggle the table of contents 
123-
--
193: Etymology 1
194- [ edit ] 
195-
196- Root
```


## [2026-09-06T15:14:53.187Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '190,260p' b07cc39f299ed266.txt; echo \"==== هجرة file empty? ====\"; wc -c 32043850e3630e68.txt; head -20 32043850e3630e68.txt"
}
```


### [2026-09-06T15:14:53.246Z] TOOL RESULT

```
 Arabic
 [ edit ] 

 Etymology 1
 [ edit ] 

 Root 

 ه ج ر ( h j r ) 

 17 terms 

 Verb
 [ edit ] 

 هَاجَرَ • ( hājara ) III ( non-past يُهَاجِرُ ( yuhājiru ) , verbal noun مُهَاجَرَة ( muhājara ) or هِجَار ( hijār ) ) 

 to migrate 

 ( Classical ) to separate from one's own, emigrate from one's tribe

 ( Classical ) to abandon the nomadic life of the desert to live in the city

 Conjugation
 [ edit ] 

 Conjugation of هَاجَرَ (III, sound, full passive, verbal nouns مُهَاجَرَة , هِجَار )

 verbal noun
 الْمَصْدَر 

 مُهَاجَرَة , هِجَار 
 muhājara , hijār 

 active participle
 اِسْم الْفَاعِل 

 مُهَاجِر 
 muhājir 

 passive participle
 اِسْم الْمَفْعُول 

 مُهَاجَر 
 muhājar 

 active voice
 الْفِعْل الْمَعْلُوم 

 singular
 الْمُفْرَد 

 dual
 الْمُثَنَّى 

 plural
 الْجَمْع 

 1 st person
 الْمُتَكَلِّم 

 2 nd person
 الْمُخَاطَب 

 3 rd person
 الْغَائِب 

 2 nd person
 الْمُخَاطَب 

 3 rd person
==== هجرة file empty? ====
3618 32043850e3630e68.txt
URL: https://en.wiktionary.org/wiki/%D9%87%D8%AC%D8%B1%D8%A9
FETCHED: 2026-09-06T15:14:11Z
STATUS: 200
TITLE: هجرة - Wiktionary, the free dictionary

هجرة - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal
```


## [2026-09-06T15:15:02.352Z] TOOL CALL #28: Bash

```json
{
 "command": "for u in \\\n\"https://en.wiktionary.org/wiki/%D9%87%D8%AC%D8%B1\" \\\n\"https://en.wiktionary.org/wiki/%D7%94%D7%92%D7%A8\" \\\n\"https://en.wiktionary.org/wiki/%D9%87_%D8%AC_%D8%B1\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 220 verification: Semitic h-j-r root, hejrat, Hagar\"; done"
}
```


## [2026-09-06T15:15:04.432Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD vol2 Hagar headword ===\"; grep -n \"^Ha  gar\\|^Hagar\\|Ha-gar\\|Ha'gar\" FSD_vol2.txt | head; echo \"=== hegira in FSD2 ===\"; grep -n -i \"he-gi-ra\\|hegira\" FSD_vol2.txt | head"
}
```


### [2026-09-06T15:15:05.340Z] TOOL RESULT

```
Exit code 1
/home/sfmqrb/git/rishe/data/verification/sources/web/57739514a64113a5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8c24c99df6cbbe7d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/bba55168025cce57.txt
```


### [2026-09-06T15:15:05.421Z] TOOL RESULT

```
=== FSD vol2 Hagar headword ===
=== hegira in FSD2 ===
11173:Hindu  era  of  the  deluKo  (3101  or  310’2  B.  G.:  used  lu Hindu  chronology) ;   Mohammedan  era,  Mo.slera  era,  or era  of  the  Hegira  (July  16,  A.  D.  622:  tho  1st  of  Miiharrarn oecurretl  63  days  before  the  Hegira) ;   Olympic  era  (July  13, 776  B.  C.:  ended  A.  D.  390) ;   Persian  era,  Oelalcan  era, Jalalcan  ora,  or  ora  of  Yezdcglrd  (June  16,  A.  Ii.  632: used  by  Par,sce.s  of  India  ami  Persia);  Spanish  era  (Jan. 1,  38  B.  C.:  conquest  of  Spain  by  Augustus,  used  till  14tli century).
11360:0.  1.52:  seiiaratlon  of  Armenian  church  from  Greek  churcli); Augustan  era  (27  B.  O.:  Octavius  Caisar  received  title Augustus) ;   Babylonian  eta  or  era  of  Nabonassar  (Feb. 25,  747  B.  O.:  his  accession  to  throne  of  Babylon,  used  I)y Ptolemy  In  astronomleal  calculations);  Chaldean  era,  era of  Contracts,  era  of  the  Greeks,  era  of  Kings,  era  of the  .Selcucldas  or  Macedonian  era  (October,  :U2  B.  G., or  at  Babylon,  April  2,  lUl  1$.  O.:  used  by  tho  Jews  till  HtU century;  in  Egypt  till  10th  century;  by  the  Arabs  till  lilUi century):  Chine,se  era  or  era  of  Yao  (2277  or  2700  B.  (!.: reign  of  Yao  tho  Great);  Christian  era,  floniinon  era, era  of  the  Incarnation  or  Vulgar  era  (between  2   B.  <;. and  7   B.  C.:  see  CHaistiAN:  also  Uionyiuan  eka  below) : Diocletian  era  or  era  of  Martyns  (Aug.  211,  A.  .D.  2.qi ;   used by  the  Copts  and  AbysslnUms) ;   Dionysian  era  (Marcli  2.5, In  the  year  754  of  the  Roman  era:  date  comimted  by  J   )lon.va- ius  Exlguus  as  beginning  ot  Clirlsi.lan  era:  sees  Chiii.wian): Egyptian  era  (Aug.  29, 20  B.  C.:  Egyptian  calendar  revised by  Augustus):  era  of  Abraham  «,)ct.  I,  2010  B.  C.:  (fen. xll):  era  of  Actlum  (Soph  ;i,  31  B,  O.:  sese  Actium);  era  of Alexander  (Nov.  12,  324  b.  C.:  death  of  Alexamler  the Groat) ;   era  of  foundation  of  Borne,  era  of  Cato,  era  of Varro  or  Koman  era  (April  21, 753  B,  O,;  Vurro's  accepted computation) :   era  of  Liberty  (Jan,  1, 17.S0;  used  In  Franco until  French  Republican  era  was  Introduced) ;   era  of  Mac- cabees (Nov.  2t,  106  B.  (J.;  see  Judah  Maccahku.s)  ;   era of  Tyro  (Oct,  10,  125  B.  O.:  a   mimlsmatlo  era);  eras  of Creation  or  Mundane  eras:  (l)  Alexandrian  (5,500  li.  c.: used  till  time  of  Ploctetlaii),  (2)  Antiochian  (.5400  B. used  by  Christians  of  Syria),  (3)  Constantlnopolltan, Byzantine,  or  Eastern  Church  (.5508  B,  c.:  used  by  the Greek  Chureb),  (4)  Jewish  (Oct.  7,  3701  B,  C,:  used  by  tho Jews  since  16th  century),  (5)  Usher’s  (4004  B.  C.:  com- puted by  Bishop  Usher);  French  Bopnbllcan  era  (Bept. 22,  1792:  used  until  Jan.  1,  1800):  Julian  era  (Jan.  1,  45 B.  0.:  Julian  calendar  lotroducod):  Kali  Yuga  era,  or Hindu  era  of  tho  deluge  (3ioi  or  3102  B.  tJ.:  used  to Hindu  chronology);  Motiainmcdan  era,  Moslem  era,  or era  of  the  Hegira  (July  10.  A.  I>.  022:  tho  1st  of  Muharrani occurred  03  (lay.s  before  tho  Hegira);  Olympic  era  (July  13, 776  B.  o,:  ended  A.  ».  390) :   Persian  era,  Gelaleau  era, Jalalean  era,  or  era  of  Yezdeglrd  (June  10,  A.  U.  032: used  by  Parseea  of  India  and  Persia) ;   Mpanlsh  era  (Jau.
39664:Ua"dlnK',  1   a   'daft';  2   a'dan',  Jane  (w/sslSSfl-  ).  Jeanne Alfredine  Trefouret:  the  professional  name  of  a   French actress;  has  toured  Europe  and  the  United  States. Had'lth,  1   had'i  til :   2   had'lth,  re.  [Ar.]  1.  A   saying  or  tradi- tion. 3.  [had'iths,  or  a-had'ith,  pi.]  Specif.,  the  body  of traditional  law  based  on  the  life  and  teaching  ol  Mohammed, originally  handed  down  orally  and  constituting  the  stinnah or  path.  In  the  3d  century  of  the  Hegira  two  jurists,  Mo- shin  and  Bokhari,  systematized  this  code,  and  the  Uaditiis of  Bokhari  forms  the  legal  norm  for  the  Moslems  of  north- ern  Africa.  Had'lsJ;  Had'i-thaht;  Had'i-thatt. hadj,  1   haj:  2   hadj,  re.  [Ar.]  The  pilgrimage  to  Mekka,  re- quired of  every  free  Mohammedan,  at  least  once  in  his  life, in  the  twelfth  month  of  the  year.
43381:hcj'l-ra,  fl.  Same  as  HEGIRA.  tion  of  Hel.  goddess  of  death.  Turbid  rivers,  full  of  mud,
45589:HIJ  'e-ra,  1   hlj'i-ra;  2.Mj'e-ra,  n.  The  Hegira.  HiJ  'rat. hike*,  1   hoik;  3   hlk,  v.  [Prov.  Eng.  &   Local,  U.  S.]  I.  {.  To jerk  or  toss;  as,  to  hike  a   toad  (to  kill  it  by  jerking  from  a plank).  II.  i.  1.  To  run  or  go  away;  clear  out;  hurry; specif.  (U.  S.  Army],  to  march:  tramp.  2.  (u.  S.]  To hitch:  work  up;  as.  your  collar  hikes,  or  hikes  up. bike**,  0.  [Local,  H.  S.]  I.  f.  1.  To  twitch  or  drag  care- lessly: usually  with  wy.  II.  i.  1.  To  go  about  in  a   dragging or  slouching  way,  3.  To  discharge  suddenly.—  hlk'er,  n. (S.  TJ.  S.l  A   brldle-oheck  that  is  too  tight.  [on  foot,
```


## [2026-09-06T15:15:10.591Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Ishmael\" FSD_vol2.txt | head -20"
}
```


### [2026-09-06T15:15:10.644Z] TOOL RESULT

```
61905:A   person  having  the  character  of  Ishmael,  whosfi  hand  was against  every  man,  etc.  1   Chron.  xxvil,  30. 1.sh*me-eWtet.- IsU"ina-el-lt'lc,  Ibh'ma-el-it"lsh,  a.— Isi»'ma“e!-lt"ism,
64206:XXV,  IS.  A   son  of  Ishmael.
66989:Ke'dar,  I   kl'dar;  2   kS'dar,  ».  Bib.  Gen.  xxv,  13.  A   son of  Ishmael.  [Heb.,  powerful.]  [ture  of  wild  elephants, ked'dab,  1   ked'a;  2   ketl'a, «.  [India.]  A   snare  set  for  the  cap- Ked'c-mah,  l   ked'i-me  or  ki-di'ma;  2   k6d'I-ma  or  ke-dS'ma, n.  Bib.  Gen.  xxv,  IR.  A   son  of  Ishmael.
```


## [2026-09-06T15:15:15.743Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Abraham’s\\|Abraham's\" FSD_vol2.txt | grep -i \"hand\\|bondwoman\\|concubine\\|wife\" | head -10; echo ---; grep -n -i \"flight;\\s*emigration\\|Heb\\., flight\\|Heb\\.,  flight\" FSD_vol2.txt | head"
}
```


### [2026-09-06T15:15:15.852Z] TOOL RESULT

```
---
```


## [2026-09-06T15:15:18.206Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"ha[ '\\\"]*gar\" FSD_vol2.txt | head -20"
}
```


### [2026-09-06T15:15:18.277Z] TOOL RESULT

```
39695:Zool.  A   ticciion  i>t  vene.jraa'.s.  Including  all  tMid-bloodod  Ma'gar,  1   he'gar;  2   ha'gar,  ».  Sib.  Concubine  of  Abrahiim; forms,  a.s!Hluw  an  1   reptiiM.  Hem"a-tof'r}--a;.- haem'-  mmiier  of  I.shmaPl.  h't/j.  svl,  1.  [Heb.,  w-Mulenua.i a-toc'ry-al,  a.  ~   HtBm"a-t(>pii"i-ii'na,  n.  pi.  Mam.  The  Ila'gar-ene,  1   he'gor-ln;  2   hii'gar-fn,  n.  1.  Sib.  A   Saracen Desmn-.iomhle  as  a   primary  division  of  bats.— ha;m"a-  de.ivemiant  of  l,lagar.  2.  pi,  A   peonie  E,  of  the  Jordan. toph"l-Iln'ic,  a.— M.  fjf,  Omitk.  lla'gar-ltest.
61891:P.  I.)  Fish:  a   term  used  by  the  Jt.  ls"ma-e'le,  1   Is'ma-ti'lg,  2   is’nm-e'le;  L.  Ish'- t‘T,' ’V*.*'''  ma-el.  Gm.  xvl,l2.  2.  The8onof.\braUam.andHagar.
61894:rsiand.  Janan.  de.sceudant  of  Islim.a6l,  Abraham’s  son  by  Hagar,  and,
```


## [2026-09-06T15:15:24.639Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nn=t.count('\\f')\nprint('leaves',n)\nfor target in [39695,61891]:\n    off=sum(len(l)+1 for l in lines[:target-1])\n    print(target,'leaf',t.count('\\f',0,off))\nEOF"
}
```


### [2026-09-06T15:15:26.463Z] TOOL RESULT

```
leaves 773
39695 leaf 390
61891 leaf 592
```


## [2026-09-06T15:15:29.965Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==391' FSD_vol2.txt | grep -o \"1[01][0-9][0-9]\" | head -20; echo \"---first lines---\"; awk 'BEGIN{RS=\"\\f\"} NR==391' FSD_vol2.txt | head -8"
}
```


### [2026-09-06T15:15:31.683Z] TOOL RESULT

```
1082
---first lines---
ckle.— hack'ler,  re.  one  who  hackles or  dresses  flax.
hack'le:,  ct.  1.  To  mangle  In cutting.  3.  [Prov.  Eng.,  U.  S.]
To  haggle.  [Var.  ofnAQGLEi,  ®.]
in  forming  the  pluperfect.
Have  is  used  improperly  In  such  expressions  as  “Had  X have  known  it.”  Had,  used  elliptically  for  if  I   had.  Itself carries  the  contingency  back  Into  the  pa.st,  and  there  is  no need  of  an  added  have  to  do  the  same  thing.  “   Had  I   known this,”  “   Had  he  done  that.”  are  conditional  clauses,  each complete  in  itself  as  expressing  past  posslbilit '.  Had better,  had  rather,  are  forms  which  have  been  disputed by  certain  grammatical  critics,  from  the  days  of  Samuel Johnson,  the  critics  Insisting  upon  the  substitution  of  would or  should,  but  these  expressions  are  thoroughly  established as  English  idioms,  having  the  almost  universal  popular  and literary  sanction  of  centuries.  (See  note  under  have,  vt) "I  uwuld  rather  not  go”  Is  undoubtedly  correct  when  the purpose  is  to  emphasize  the  element  of  choice  or  will  in  the matter;  but  in  all  ordinary  cases  "   I   had  rather  not  go”  has the  merit  of  being  Idiomatic  and  easily  and  universally  un- derstood.
I   had  rather  bo  a   doorkeeper  in  the  house  of  my  God  than  to dwell  in  the  touts  of  wickedness.  P«.  Ixxxiv,  10
If  for  “You  had  better  stay  at  home”  we  substitute “You  should  better  stay  at  home,”  an  entirely  different meaning  is  expressed,  the  idea  ol  expediency  giving  place to  that  of  obligation.
Would  rather  may  always  bo  substituted  for  had  rather.  Might rather  would  not  have  the  same  meaning.  Would  and  should  do not  go  well  with  belter.  In  one  instance  can  is  admissible.  ‘   I can  better  afford,’  because  can  is  especially  associated  with afford.  Wo  may  say  might  better,  but  it  has  neither  the  sanction,
```


## [2026-09-06T15:15:41.666Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FSD_vol2.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nimport re\nfor i,p in enumerate(pages):\n    if re.search(r'\\b110[01]\\b',p[:4000]) or re.search(r'\\b110[01]\\b',p[-3000:]):\n        print(i, [w for w in re.findall(r'\\b1[01][0-9][0-9]\\b',p)][:6], p.strip()[:80].replace('\\n',' '))\nEOF"
}
```


### [2026-09-06T15:15:43.396Z] TOOL RESULT

```
59 ['1100'] holes.  Ed"rl- as'ter,  re.  (t.  g.)  (<  Gr.  hedrion,  dim.  of  hedra,  seat
134 ['1100'] iuma  and  mother  of  tho  Charltoa.  2.  A   Bu-.st»''thi-an,  1   yu-ste'thi'
337 ['1096', '1100', '1040', '1053'] n (.Tkryoihorus  grenadensis) God-fearing,  a.  Having  rev- erence lor  God  an
683 ['1000', '1000', '1100', '1150'] lb.torfid.—  lan'guld-ly,  ado.— lan'guld-ness,  n. In  tho  sculptures  of  the
```


## [2026-09-06T15:16:13.151Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT ebony ===\"; grep -n \"^EBONY\\|EBONY\" SKT.txt | head -5; echo \"=== WEB vol1 ebony ===\"; grep -n \"^ebony\\|eb'on-y\\|ebony,\" WEB_vol1.txt | head -5; echo \"=== FSD vol1 ebony ===\"; grep -n -i \"eb'on-y\\|^ebony\" FSD_vol1.txt | head -5; echo \"=== PHD abnus ===\"; grep -n -i \"abnus\\|abnūs\\|ʾpnws\\|ebony\" PHD.txt PHD_mackenzie.txt NYB.txt NYB_vol2_glossary.txt 2>/dev/null | head -10"
}
```


### [2026-09-06T15:16:13.271Z] TOOL RESULT

```
=== SKT ebony ===
=== WEB vol1 ebony ===
36334:cõ'cus-wood, n. a close-grained wood of the West Indies, sometimes known as American ebony, which is used in the manufacture of musical instruments.
61109:1. a hard, heavy, anc durable wood, which takes a fine polish or loss, and is used for urniture and deco- rative woodwork, The usual color is black, but red and green varieties arealso found. The most valuable is the heart- wood of Diospyros eb- enum, which grows in the flat parts of Cey- EBONY (Diospyros ebenum) lon. Other varieties of valuable ebony are obtained from Diospyros ebenaster of the East Indies and Diospyros melanoxylon of the Coromandel coast in Hin- dustan. The green ehony of Jamaica, known also as the West Indian or American ebony, is the wood of the leguminous tree Brya ebenus.
61113:2. like ebony, especially in color; dark;
=== FSD vol1 ebony ===
=== PHD abnus ===
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:1733:ebony abnüs.
PHD_mackenzie.txt:810:abnus [lpnws I (N abniis)] ebony.
PHD_mackenzie.txt:6478:ebonyabnus.                                     complete.
```


## [2026-09-06T15:16:14.625Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HRN ===\"; grep -n -i \"abnūs\\|abnus\\|Ebenholz\" HRN.txt | head -10; echo \"=== HUB ===\"; grep -n -i \"abnūs\\|abnus\\|Ebenholz\" HUB.txt | head -10; echo \"=== ARY ===\"; grep -n \"آبنوس\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== LKT ===\"; grep -n -i \"ebenholz\\|abnus\\|ébène\" LKT.txt | head -10"
}
```


### [2026-09-06T15:16:14.730Z] TOOL RESULT

```
=== HRN ===
=== HUB ===
=== ARY ===
=== LKT ===
224:[Das  selbst  aus  gr.  ^ßevoq,  letzten  Endes phönizischen  Ursprungs  ist]  'Ebenholz'. Hieraus  prov.  avenuts,  sp.  abenuz  'Eben- holzbaum, Diospyrus  ebenus'  [neben unmittelbar  dem  lat.  ebenus  entlehnten e^ano  wie  die  übrigen  romanischen Formen].  Ebenso  rum.  abanos  'Eben- holz', fig.  'kräftig'.  [Sain  46.  DE  31. ML  2816.
```


## [2026-09-06T15:16:23.845Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '215,232p' LKT.txt; echo \"=== leaf ===\"; python3 - <<'EOF'\nt=open('LKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:223])\nprint('leaf',t.count('\\f',0,off))\nEOF"
}
```


### [2026-09-06T15:16:25.480Z] TOOL RESULT

```
Spanisch   235
Syrisch  (nebst  Aramäisch)   241
Tschechisch   241
Etymologisches  Wörterbuch.
1.  Syr.  aßa:
[BrLexSyr  la;  allgemein-semitisch,  vgl. hebr.  rtß,  ar.  abü,  ass.  abu,  Del  HWß  3  a] 'Vater'.  Hieraus  gr.  äßßaq  und  seit  dem 4.  Jahrhundert  im  Kirchenlatein  abbas /abbätem,  dbbätem]  in  der  Bedeutung 'Vater,  Mönch',  woraus  die  Ableitungen abbatia  'Abtei'  und  abbatissa  'Äbtissin'. Die  romanischen  Formen  sind:  it.  abate, abhate;  ahbadia,  hadia,  abaz'm;  (a)ba- dessa;  prov.  abas;  abodia;  abadesa;  kat. ubat;  abadesa;  sp.  abad;  abadesa,  aba- dia;  pg.  abbade;  abbadia;  abbadessa;  frz. abbd;  abbesse;  abbaye.  In  den  germa- nischen Sprachen:  ags.  abbod,  engl.  «6- bot,  ndl.  abt,  dtsch.  Abt,  Abtei,  Äbtis- sin. Daß  das  von  ML  S  aufgeführte sp.  kat.  abadejo,  pg.  badejo  'Stockfisch' hierher  gehört,  darf  doch  wohl  aus semantischen  Gründen  bezweifelt  wer- den. Aus  dem  it.  wurde  russ.  abbat, abbatissa,  abbatstwo;  serb.  abat,  opat, (5ech.  poln.  oimt,  dagegen  cech.  je ptiäka 'Nonne'  aus  dem  mhd.  eppefisse  'Äb- tissin'. [ML  8—10.  Wartbg  FEWb  .S. Kluge  .5.  Gorjajew  1.  Bern  SlEtWb  22.
2.  Av.  'abä':
'Grober,  dicker  Wollstoff'  [vgl.  ZDMG  IV, 392],  'Mantel  daraus'.  Im  Tk.  ebenso und  abagu  'Hersteller  od.  Verkäufer  von solchen  Mänteln'.  Hieraus  rum.  aba 'dicker  Stoff  für  Mönchskutten',  abayiü 'Verkäufer  dieses  Stoffes',  abagerie 'Handel  damit'  und  Ableitungen :  abager, abageresc,  abäioarä,  abälii^ä.  —  Russ. aba  'grobes,  weifäes  Tuch';  bulg.  aba 'dass.',  'Art  Oberkleid  der  Bauern'; serb.  aba  'grobes  Tuch';  poln.  haba, chaba  'dass.'.  [Sain  46.  Gorjajew  1. Bern  SlEtWb  22.
3.  Ar.  abaufis:
[Das  selbst  aus  gr.  ^ßevoq,  letzten  Endes phönizischen  Ursprungs  ist]  'Ebenholz'. Hieraus  prov.  avenuts,  sp.  abenuz  'Eben- holzbaum, Diospyrus  ebenus'  [neben unmittelbar  dem  lat.  ebenus  entlehnten e^ano  wie  die  übrigen  romanischen Formen].  Ebenso  rum.  abanos  'Eben- holz', fig.  'kräftig'.  [Sain  46.  DE  31. ML  2816.
Lokotsch,  Etymolog,  Wörterbuch.
4.  Ar.  'Abbäs:
N.  pr.  Nach  dem  pers.  Schah  'ABBAS  I. [1586 — 1628]  wurde  eine  Münze  mit seinem  Bilde  so  genannt  [vgl.  Napoleon d'or,  Louis  d'or];  hieraus  russ.  «6«^ 'Münze  von  20  Kopeken'.    [Gorjajew  1.
5.  Pers.  abdär:
[Aus  äb  'Wasser'  od.  'Glanz'  Hoi-n  NpEt S.  1,  Nr.  2  und  3,  und  Stamm  där- 'habend,  haltend'  ebda.  S.  116,  Nr.  527] 'wässerig,  hell,  glänzend'  [von  Stahl od.  Waffen  gesagt].  Über  das  tk.  hier- aus rum.  abitir  'besser,  vortrefflicher'; russ.  ob'jar  'Art  Stoff'.
6.  Ar.  abjad :
'Weiß'.  Hieraus  fiz.  abit  'Bleiweiß', alter  chemischer  Terminus.  Aus  dem ar.  Subst.  bajäd  'Weiße'  wurde  mit  ar. Art.  sp.  albayalde  'kohlensaures  Blei- salz', Vb.  albayaldar.    [Devic  DEl  1.
7.  Pers.  äbkärl:
=== leaf ===
leaf 27
```


## [2026-09-06T15:16:36.188Z] TOOL CALL #39: Bash

```json
{
 "command": "for u in \\\n\"https://www.ahdictionary.com/word/search.html?q=ebony\" \\\n\"https://abadis.ir/fatofa/%D8%A2%D8%A8%D9%86%D9%88%D8%B3/\" \\\n\"https://abadis.ir/fatofa/%D9%87%D8%A7%D8%A8%DB%8C%D9%84/\" \\\n\"https://abadis.ir/fatofa/%D9%87%D8%AC%D8%B1%D8%AA/\" ; do python3 tools/fetch_source.py \"$u\" --note \"page 220: ebony/abnus, Habil, hejrat\"; done"
}
```


### [2026-09-06T15:16:44.457Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6ccfc09064a03112.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b079f5d209bb20ee.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/7c7f5d845bdfe028.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac644dd287da8dcf.txt
```


## [2026-09-06T15:16:47.645Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### AHD\"; grep -n -i -A6 \"ebony\" 6ccfc09064a03112.txt | head -40; echo \"### abadis abnus\"; grep -n -B2 -A8 \"معین\\|فرهنگ فارسی\" b079f5d209bb20ee.txt | head -60"
}
```


### [2026-09-06T15:16:47.713Z] TOOL RESULT

```
### AHD
1:URL: https://www.ahdictionary.com/word/search.html?q=ebony
2-FETCHED: 2026-09-06T15:16:38Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: ebony
5-
6:American Heritage Dictionary Entry: ebony 
7-
8- HOW TO USE THE DICTIONARY
9- To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
10- Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
11- guide to the dictionary 
12-
--
51: adj. 1. Made of or suggesting ebony.
52- 2. Black in color.
53-
54: [Probably from Middle English hebenyf , ebony wood, from alteration of Late Latin hebeninus , of ebony, from Greek ebeninos , from ebenos , ebony tree, from Egyptian hbny .]
55-
56- The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
57-
58- Indo-European & Semitic Roots Appendices
59- Thousands of entries in the dictionary include etymologies that trace their origins back to reconstructed proto-languages. You can obtain more information about these forms in our online appendices:
60- Indo-European Roots 
### abadis abnus
54-رخ شید از گرد شد آبنوس. فردوسی.
55-
56: فرهنگ فارسی
57-
58- ( آبنوس ) درختی است از تیر. پروانه واران که در هند و ماداگاسکا و جزیر. موریس روید. چوب آن سیاه سخت سنگین و گرانبهاست . یا آبنوس دروغی درختیاست از تیره پروانه واران شجره النحل قصاص قطیس . یا آبنوس کیانی درختی است از تیر. پروانه واران مخصوص نواحی معتدل . یا آبنوس هندی
59-چوبی سیاه رنگ و سخت و سنگین و گرانبها از درختی بهمین نام ماخوذازکلمه یونانی ابانس، درختی که درهندوحبشه میرویدوثمرش شبیه انگوراست 
60-
61: فرهنگ معین
62-
63- ( آبنوس ) [ په . ] (اِ )درختی است با چوبِ بسیار سخت ، سیاه رنگ و گران بها. 
64-
65- فرهنگ عمید
66-
67- ( آبنوس ) ۱. (زیست شناسی ) درختی گرمسیری با چوب سیاه، و گران قیمت.
68-۲. (زیست شناسی ) چوب این درخت که سخت، سنگین، و با لکه های سیاه است در کنده کاری و نجاری کاربرد دارد.
69-۳. (صفت ) [قدیمی] تیره رنگ، شیز. 
--
167- دیکشنری آبادیس
168-
169: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
170-
171- لینک ها 
172-
173- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
174-
175- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
176-
177- © 2006-2026 abadis.ir
```


## [2026-09-06T15:16:55.676Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### هابیل\"; grep -n -B3 -A6 \"معین\\|دهخدا\" 7c7f5d845bdfe028.txt | head -60"
}
```


### [2026-09-06T15:16:55.731Z] TOOL RESULT

```
### هابیل
20- معنی: عرب از عبری نفس یا بخار، نام پسر آدم ( ع )، ( عبری ) به معنی ' نفس یا بخار '، ( در اعلام ) به نقل از تورات دومین پسر حضرت آدم بوده است که داستان وی و برادرش ( قابیل ) در قرآن سوره ی مائده، آیه آمده است، معرب از عبری نفس یا بخار
21- برچسب ها: اسم ، اسم با ه ، اسم پسر ، اسم عبری ، اسم مذهبی و قرآنی 
22-
23: لغت نامه دهخدا
24-
25- هابیل. ( اِخ ) پسر دومین آدم است . بعضی را گمان چنان است که اسم مسطور ( هابیل = نفس ، بخار ) دلالت بر کوتاهی عمر هابیل است ، ودیگران بر آنند که چون حوّا دید قاین آن نسل موعود نیست این مطلب داعی بر این شد که با خود فکر نماید که زندگانی را چندان اهمیتی نیست و همچنانکه یعقوب ( 4:14 ) میگوید: «حیات شما چیست ؟ مگر بخاری نیستید که اندک زمانی ظاهر است و بعد ناپدید میشود». علی الجمله هابیل شبان بود و از اول زادگان گوسفندان خود از برای خداوند قربانی آورد و خداوند قربانی وی را پذیرفته قربانی قائین را که از محصول ارضی بود رد کرد . در این حال دست حسد سرمه نفرت در دیده قائین کشیده بر برادر خود غضبناک شده او را کشت . و مسیح ، هابیل راهابیل صدیق نامید . ( قاموس کتاب مقدس ). مؤلف مجمل التواریخ آرد: «نخستین کسی که از دنیا بیرون رفت هابیل بود که قابیل بکشتش ، چنانکه حق تعالی در قرآن یاد کرده است و همانجا در کوههای حدود سراندیب قابیل ، هابیل را در زیر خاک کرد .
26-و اندر کتاب دلایل القبله چنان خواندم که روایت کرده است ابن عباس رضی اﷲ عنهما که آن وقت زمین اسفید بود تا آن وقت که قابیل هابیل را بکشت ، پس لونش بگردید و طعم بعضی از میوه ها ناخوش گشت و مضر، و از آن سبب در مرثیت و اندوه هابیل آدم این بیتها یاد کرد و معروف و مشهور است : 
27-تغیرت البلاد و من علیها
28-و وجه الارض مُغْبرّ قبیح 
29-تغیَّرَ کل ذی لون و طعم 
--
89-در آتش عشق همچو هابیل. 
90-اوحدی کرمانی ( از مزدیسنا ص 512 ) . 
91-و رجوع به مجمل التواریخ و القصص ص 89، 182، 430، 431 و 481 و تاریخ گزیده صص 23 - 24 و 65 نزهةالقلوب ج 3 ص 250 و 292 و لباب الالباب ج 1 صص 17 - 18العقد الفرید ج 2 ص 152 و ج 5 ص 59 و الکامل ج 1 و ناسخ التواریخ ج 1 شود. 
92:منبع. لغت نامه دهخدا
93-
94- منبع. عکس فرهنگ ریشه واژگان فارسی دکتر علی نورایی
95-
96- هابیل دومین پسر آدم و حوا بوده و اسم هابیل به معنی نفس
97-
98- به معنی = نفس
--
104-
105- دیکشنری آبادیس
106-
107: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
108-
109- لینک ها 
110-
111- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
112-
113- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است.
```


## [2026-09-06T15:16:57.086Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### هجرت\"; grep -n -B3 -A8 \"فرهنگ معین\\|لغت نامه دهخدا\" ac644dd287da8dcf.txt | head -60"
}
```


### [2026-09-06T15:16:57.141Z] TOOL RESULT

```
### هجرت
22- معنی: از کشور یا زادگاه خود به جای دیگر رفتن، از کشور یا زادگاه خود به جای دیگر رفتن و در آنجا ساکن شدن، ( اَعلام ) مهاجرت پیامبر اسلام ( ص ) و جمعی از یارانش ( مهاجران ) از مکه به یثرب ( مدینه )، که رویدادی ویژه در تاریخ اسلام بود، بعدها مبدأ تاریخ هجری قرار گرفت ( = میلادی )
23- برچسب ها: اسم ، اسم با ه ، اسم دختر ، اسم عربی 
24-
25: لغت نامه دهخدا
26-
27- هجرت. [ هَِ رَ ] ( ع اِمص ) مفارقت. جدایی. ( ناظم الاطباء ) ( آنندراج ) ( منتهی الارب ). دوری. افتراق. فراق. هجر. هجران. || ترک وطن و دوری از خانمان و مفارقت یاران و دوستان. ( ناظم الاطباء ). جدائی از سرای و نشیمن. ( السامی فی الاسامی ). بریدن از وطن. بریدن از خانمان. جدایی از وطن : حرمت هجرت و وسیلت غربت را مایه و ساقه ٔآن گردانیده. ( کلیله و دمنه ). || رحلت. ارتحال. کوچ. مهاجرت : اگر در عاقبت کارها وهجرت سوی گور فکرتی شافی واجب داری حرص و شره این عالم فانی بر تو بسر آید. ( کلیله و دمنه ). || ( مص ) گذاشتن. || جدا شدن از خانمان. ( غیاث ) ( شمس اللغات ). || در اصطلاح مسلمین ، ترک وطن کفار و انتقال به دارالاسلام. ( از تعریفات سید شریف جرجانی ). در مقابل تَعَرﱡب که قبل از فتح مکه به دست پیغمبر به معنی مهاجرت از منطقه اسلامی مدینه به منطقه کفار قریش در مکه و نواحی بود : 
28-آن را که کس به جای پیمبر جز او نخفت 
29-با دشمنان صعب به هنگام هجرتش. ناصرخسرو.
30-ازبهر دین ز خانه براندید مرمرا
31-تا با رسول حق به هجرت سوی شدم. ناصرخسرو.
32-این بس شرف سفر که در عالم 
33-تاریخ ز هجرت پیمبر شد. علی شطرنجی.
--
41-
42- (مصدر ) جداشدن جدایی کردن .۲- رحلت کردن هجرت کردن .۳- (اسم ) جدایی مفارقت . ۴- رحلت مهاجرت . ۵- ترک وطن کفار وانتقال بدارالاسلام ۶- ترک پیغمبراسلام مکه را وحرکت وی بسوی مدینه و آن در ۱۶ ژوئیت سال ۶۲۲ م . صورت گرفت وهمان مبدائ تاریخ مسلمانان قرارگرفته: (( هفتصد وپنجاه وچار ازهجرت خیرالبشر مهر را جوزامکان وماه راخوشه وطن . ) ) ( حافظ ) یا هجرت اولی. مهاجرت گروهی از پیروان پیغمبر اسلام ازمکه به حبشه که براثر آزار قریش بدستور پیغمبربسال پنجم ازبعثت رسول اتفاق افتاد. 
43-
44: فرهنگ معین
45-
46- (هِ رَ ) [ ع . هجرة ] (اِمص . ) ۱ - کوچ کردن ، ترک وطن . ۲ - مبداء تاریخ مسلمانان که زمان هجرت پیامبر است از مکه به مدینه برابر با ۶۲۲ م . 
47-
48- فرهنگ عمید
49-
50- ۱. دوری گزیدن از وطن، کوچ کردن از وطن خود و به جای دیگر رفتن، رفتن از شهری به شهر دیگر و در آنجا وطن کردن.
51-۲. مهاجرت پیامبر اسلام از مکه به مدینه، که مبدٲ تاریخ مسلمانان است. 
52-
--
74-«...وَاهْجُرُوهُنَّ فِی الْمَضَاجِعِ...»؛(سوره نساء/34) در بستر از آنها دوری نمائید.
75-و به پیامبر اکرم صلی الله علیه و آله خطاب می نماید:
76-«وَاصْبِرْ عَلَی مَا یَقُولُونَ وَاهْجُرْهُمْ هَجْرًا جَمِیلاً»؛(سوره مزمل/10) و در برابر آنچه (دشمنان) می گویند: شکیبا باش و به طرزی شایسته از آنان دوری گزین!
77:لغت نامه دهخدا برای هجرت معانیی همچون: مفارقت و جدایی، ترک وطن و دوری از خانمان و مفارقت یاران و دوستان، جدائی از سرای و نشیمن را بیان نموده و به نقل ا زتعریفات سید شریف جرجانی آورده است که: هجرت در اصطلاح مسلمین ، ترک وطن کفار و انتقال به دارالاسلام است.
78-قرآن می فرماید: «وَما کانَ الْمُؤمِنُون لِیَنْفِرُوا کافَّةً فَلَوْلا نَفَر مِنْ کُلِّ فِرْقَةٍ مِنْهُمْ طائِفَةٌ لِیَتَفَقَّهُوا فی الدّین...» ؛؛ شایسته نیست مؤمنان همگی (به سوی میدان جهاد) کوچ کنند؛ چرا از هر گروهی از آنان طایفه ای کوچ نمی کند تا در دین آگاهی یابند و به هنگام بازگشت به سوی قوم خود، آنها را بیم دهند؟ wikiahlb: هجرت 
79-
80- [ویکی شیعه] هجرت (ابهام زدایی). هجرت ممکن است به یکی از عناوین زیر اشاره داشته باشد: wikishia: هجرت_(ابهام زدایی) 
81-
82- دانشنامه آزاد فارسی
83-
84- رجوع شود به:مهاجرت wikijoo: هجرت 
85-
--
92-
93- هجرت. [ هَِ رَ ] ( ع اِمص ) مفارقت. جدایی. ( ناظم الاطباء ) ( آنندراج ) ( منتهی الارب ) . دوری. افتراق. فراق. هجر. هجران. || ترک وطن و دوری از خانمان و مفارقت یاران و دوستان. ( ناظم الاطباء ) . جدائی از سرای و نشیمن. ( السامی فی الاسامی ) . بریدن از وطن. بریدن از خانمان. جدایی از وطن : حرمت هجرت و وسیلت غربت را مایه و ساقه ٔآن گردانیده. ( کلیله و دمنه ) . || رحلت. ارتحال. کوچ. مهاجرت : اگر در عاقبت کارها وهجرت سوی گور فکرتی شافی واجب داری حرص و شره این عالم فانی بر تو بسر آید. ( کلیله و دمنه ) . || ( مص ) گذاشتن. || جدا شدن از خانمان. ( غیاث ) ( شمس اللغات ) . || در اصطلاح مسلمین ، ترک وطن کفار و انتقال به دارالاسلام. ( از تعریفات سید شریف جرجانی ) . در مقابل تَعَرﱡب که قبل از فتح مکه به دست پیغمبر به معنی مهاجرت از منطقه اسلامی مدینه به منطقه کفار قریش در مکه و نواحی بود 
94- ... [مشاهده متن کامل] 
95:منبع. لغت نامه دهخدا
96-
97- رفتن
98-
99- ترک بلاد
100-رحل
101-
102- رفتگی
103-
--
134-
135- دیکشنری آبادیس
136-
137: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
138-
139- لینک ها 
140-
141- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد.
```


## [2026-09-06T15:17:22.017Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 270 374 385 13; do echo \"=== leaf $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | head -3; echo \"  ...tail:\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N+1' KLN_1966.txt | tail -2; done"
}
```


### [2026-09-06T15:17:23.592Z] TOOL RESULT

```
=== leaf 270 ===
,  fr.  OE.  earnian, ‘to  deserve,  earn’,  rel.  to  OHG.  amen,  arnon, ‘to  reap’,  OE.  ern,  OHG.  aran,  arn,  G.  Ernte, ‘harvest’,  Goth,  asans,  ‘harvest,  summer’,  ON. bnn  (for  *aznu),  ‘work  in  the  field’,  and  cogn. with  OSlav.  jeseni,  Russ,  osen’,  OPruss.  assanis, ‘autumn’.
Derivatives:  earn-er,  n.,  earning,  n.  (q.v.) earnest,  n.,  seriousness.  —  ME.  ernest,  fr.  OE. eornost,  rel.  to  OS.,  OHG.,  ernust,  ‘struggle’, MHG.  ernest,  ‘struggle;  earnest’,  G.  Ernst, ‘earnest,  seriousness’,  Goth,  arniba,  ‘safely’,  ON. jama,  ‘fight,  combat’,  ern,  ‘able,  fit,  vigorous', orig.  ‘able  to  fight’.  Cp.  Ernest.
Derivatives:  earnest,  adj.,  earnest-ly,  adv.,  ear- nest-ness,  n.
  ...tail:
Eburna,  n,,  a  genus  of  marine  gastropods,  the ivory  shell.  —  ModL.,  fr.  L.  eburnus,  ‘of  ivory’, fr.  ebur,  ‘ivory’.  See  ivory, eburnated,  adj.,  hard  like  ivory  (med)  —  Formed with  suff.  -ed  fr.  L.  eburnus,  ‘of  ivory’.  See  prec. word.
eburnation,  n.,  an  increase  in  the  density  of  bone, cartilage  or  tooth  (med.)  —  Formed  with  suff. -ation  fr.  L.  eburnus,  ‘of  ivory’.  See  Eburna. eburnean,  adj.,  pertaining  to,  made  of,  or  resem¬ bling,  ivory.  —  Formed  with  suff.  -an  
=== leaf 374 ===
  fr.  MDu.,  hakebusse.  See  harquebus.
hackery,  n.,  an  Indian  bullock  cart  (India).  — Corruption  of  Hind,  chakra,  ‘cart’,  fr.  OI. cakrah,  ‘wheel’ .  See  cycle  and  words  there  referred to  and  cp.  esp.  chukker.
hackle,  n.,  1)  a  comb  for  dressing  flax;  2)  one  of the  long  feathers  on  the  neck  of  a  cock.  —  ME. hekele ,  ‘an  instrument  for  cleansing  and  carding flax  or  hemp’.  See  hatchel,  n.,  and  cp.  heckle. Derivatives:  hackle,  v.,  hackl-er,  n.
  ...tail:
Haggai,  n.,  1)  a  prophet  who  lived  about  500 B.C.E.,  the  tenth  in  the  order  of  the  Twelve Prophets;  2)  the  Book  of  Haggai  (Bible).  — Heb.  Haggay  (whence  Gk.  ’Ayyaio L.  Aggae- us),  lit.  ‘festal,  born  on  a  feast  day’,  fr.  Heb. hagh,  ‘a  festival  gathering,  a  feast’,  from  the  stem of  hdghagh,  ‘he  made  a  pilgrimage,  celebrated  a feast’,  which  is  rel.  to  Syr.  haggi,  ‘he  made  a pilgrimage,  celebrated  a  feast’,  Aram.-Syr. haggd,  ‘a  feast’,  Arab,  hajja,  ‘he  went  on  a  pil¬ grimage’.  Cp.  hadj,  hadji. haggard,  n.,  an  untamed  hawk;  adj.,  hard  to  tame (said  of  a  hawk).  —  MF.  (=  F.)  hagard,  ‘a  hag¬ gard’,  which  is  of  Teut.  origin  and  orig.  meant ‘(a  bird)  of  the  hedge’,  i.e.  ‘a  wild,  untameable (bird)’.  Cp.  ME.  hagger,  ‘wild;  an  untamed hawk,  haggard’,  and  see  hedge  and  -ard.  Cp. also  hag,  ‘witch’.
haggard,  adj.,  harassed.  —  From  prec.  word. The  orig.  meaning  was  ‘wild-looking’. Derivatives:  haggard-ly,  adv.,  haggard-ness,  n. haggis,  n.,  a  Scottish  dish  made  of  the  lungs, heart,  liver,  etc.,  of  a  sheep  or  calf.  —  ME. hagese,  hageys,  hagas,  ‘a  kind  of  pudding’,  prob. fr.  haggen,  ‘to  hew’.  See  hag,  ‘to  hew’, haggle,  tr.  v,  to  mangle;  intr.  v.,  to  bargain  in  a mean  way.  —  Freq.  of  hag,  ‘to  cut’  (q.v.)  For the  ending  see  freq.  suff.  -le.  Cp.  higgle. Derivatives:  haggle,  n„  haggl-er,  n. hagi-,  form  of  hagio-  before  a  vowel, hagiarchy,  n.,  government  by  men  in  holy  orders. —  Compounded  of  hagi-  and  Gk.  -apyix,  ‘rule’, fr.  if/fiz,  ‘leader,  chief,  ruler’.  See  -archy. hagio-,  before  a  vowel  hagi-,  combining  form meaning  ‘holy,  sacred’.  —  Gk.  ayio-,  ayt-,  fr. ayi6g,  ‘holy,  sacred’,  which  is  rel.  to  cPjeaFoci (for  *3yiea8m),  ‘to  stand  in  awe  of,  to  revere’, ayoi;,  ‘sacri
=== leaf 385 ===
 resp.  OFris.  hod,  OHG.  huota,  MHG. huole,  G.  Hut,  ‘protection,  care’,  OE.  hod, ‘hood’.  See  hood.
heed,  n.  —  ME.  hede,  fr.  heden.  See  heed,  v. Derivatives:  heed-ful,  adj.,  heed-ful-ly,  adv., heed-ful-ness,  n.,  heed-less,  adj.,  heed-less-ly, adv.,  heed-less-ness,  n.
heehaw,  n.,  i)  the  bray  of  a  donkey;  2)  a  guffaw; intr.  v.,  1)  to  bray  like  a  donkey;  2)  to  guffaw.  — Imitative.
  ...tail:
heliogravure,  n.,  photoengraving.  —  F.  helio¬ gravure,  a  hybrid  coined  fr.  Gk.  fjXioi;,  ‘sun’, and  gravure,  ‘engraving’,  a  word  of  Teut.  origin. See  Helios  and  gravure.
heliology,  n.,  the  study  of  the  sun.  —  Compound¬ ed  of  helio-  and  Gk.  -Xoyloi,  fr.  -X6yo?,  ‘one who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy, beliometer,  n.,  an  instrument  f
=== leaf 13 ===
  L.  bassus,  ‘thick,  fat, low’.  See  base,  ‘low’,  and  cp.  the  second  element in  bouillabaisse.
Derivatives :  abas-ed ,  adj.,  abas-ed-ly,  adv.,  abas- ed-ness,  n.,  abase- ment,  n. abash,  tr.  v.,to  confuse;  to  put  to  shame.  —  ME. abassen,  abaissen,  abashen,  fr.  OF.  esbahiss-, pres.  part,  stem  of  esbahir,  ‘to  astonish’,  com¬ pounded  of  pref.  es-  (fr.  L.  ex\  see  1st  ex-)  and a  derivative  of  OF.  baer  (F.  bayer ),  ‘to  gape’, the  change  of  conjugation  (-ir  for  -er)  being prob.  due  to  the  influence  of  the  OF.  adj.  batf.
abasia
  ...tail:
Derivative:  abhorrent-ly,  adv. abide,  intr.  and  tr.  v.  —  OE.  abidan ,  formed  fr. intensive  pref.  a-  and  bidan,  ‘to  remain,  await’. See  bide.
Derivatives:  abid-ing,  adj.,  abid-ing-ly,  adv. Abies,  n.,  a  genus  of  trees,  the  true  fir  (bot.)  — L.  abies,  ‘silver  fir’,  cogn.  with  Gk.  fiffiv  (acc.), ‘silver  fir’,  ’Affix)),  name  of  Southern  Russia, lit.  ‘a  region  of  firs’.  Cp.  abeto. abietic,  adj.,  pertaining  to  the  crystalline  acid C20H30O2  (chem.)  —  Formed  with  suff.  -ic  fr. L.  abies,  gen.  abietis,  ‘silver  fir’.  See  prec.  word. Abigail,  fem.  PN. ;  in  the  Bible,  the  wife  of  Nabal, later  of  David.  —  Heb.  Abhigayil,  lit.  ‘my  father is  rejoicing’,  fr.  abh,  ‘father’  and  gil,  ‘to  rejoice’. For  the  first  element  see  Aboth.  The  second  ele¬ ment  is  rel.  to  Arab,  jdla,  ‘he  went  round’  and to  Heb.  galdl,  ‘he  rolled,  unfolded’;  see  gelilah. The  use  of  the  name  in  the  sense  of  ‘waiting maid’  is  due  to  the  passage  ini  Sam.  25 : 35,  where Abigail  calls  herself  a  ‘handmaid’, abigeat,  n.,  cattle  stealing  (civil  law).  —  L.  abi- geatus,  fr.  abigeus,  ‘cattle  stealer’,  fr.  abigere, ‘to  drive  away’,  fr.  ab-  and  agere,  ‘to  drive’ ;  see agent.  The  change  of  Latin  d  (in  agere)  to  f  (in  ab¬ igere)  is  due  to  the  Latin  phonetic  law  according to  which  in  the  unaccented  open  radical  syllable of  the  second  element  of  compounds,  original b  becomes  i.  Cp.  accident,  adhibit,  ambiguous, ancipital,  anticipate,  artifice,  comfit,  conceive, consilient,  constitute,  contiguous,  council,  de¬ ceive,  deciduous,  deficient,  delicious,  delitescent, desipient,  destine,  destitute,  difficulty,  disciple, dissilie
```


## [2026-09-06T15:17:43.670Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"### FVQ Habil\"; grep -n -i \"hābīl\\|Habil\\|Qābīl\" FVQ_pages.txt | head -5; echo \"### FVQ hijra\"; grep -n -i \"hijra\\|hijrah\" FVQ_pages.txt | head -5; echo \"### FSD1 Abel\"; grep -n \"A'bel\\|Abel,\" FSD_vol1.txt | head -5; echo \"### SKT abel/ebony\"; grep -n -i \"^EBON\\|^ABEL\" SKT.txt | head"
}
```


### [2026-09-06T15:17:43.770Z] TOOL RESULT

```
### FVQ Habil
### FVQ hijra
865:3 This was in A.I). 616, and is known as the First Hijra, of. at-Tabarl, Annahn, i,
2108:of the Hijra and so doubtless influenced by Muhammad's usage. They would seem
### FSD1 Abel
4782:Abd"»er*Rah'man,  1   ubd'-er-m'msTr.  2   abd'*?r»rS'man.  n.  ab-dom"I-nn-ves'I-cal,  1   ab-dem'i-no-vesVkal;  2   &b-d6m’-  tropical  shrubs  of  the  honeysuckle  family,  cultivated  as 1.  A   Moslem  (   -788)  who  founded  the  Ommiad  Moslem  I-no-v§s'i-cal,  a.  Of  or  pertaining  to  the  bladder  and  the  flowering  plants.  See  Illus.  below.  [<  Clarke  Abel,  Eng.
4875:fir.'Is.a,  Sab-ilfiin'l-nH'll-a,  n.  pi.  A'bel*,l  0'bel;2fi'b?l,n.  1.  Carlfn/jils.lT-u/nlOOO.a  Ger-  town  In  Carmarthenshire.  Wales.
4891:atafeo-pv*  »4.  Med.  Examination  of  the  abdomen,  as  for  A'bel-bctb  *ma/a-chab,  1   C'bel-  berh-mC'o-ko;  2   o'bfl-  VacyitiK  from,  the  type  ol  its  group;  abnormal;  cxccp- discovering  disease.  [<  Anoouns’  -f  -flcopv.J  he^l’m5,a;ca*  A   city  In  N.  Palestine;  captured  by  tional.  |   <   L.  aberran (t-)*,  ppr. of aberro;  sec  ader»ate.J
### SKT abel/ebony
5653:Ebony,  a  hard  wood.  (F.-U-Gk Hcb  >   Formerly  fAr«.  — O.  F.  eb€nt.t\<^
```


## [2026-09-06T15:17:47.839Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5650,5660p' SKT.txt; python3 - <<'EOF'\nt=open('SKT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:5652])\nprint('leaf',t.count('\\f',0,off))\nEOF"
}
```


### [2026-09-06T15:17:50.084Z] TOOL RESULT

```
orta,  remnants,  leavings.  fE)  M< ortej.  From  A.  S.  er-.  out  (wnat  b  Ici etatt,  to  cat.  Proved  by  O.  Du.  Qrtti piece  left  after  eating,  Swcd.  dial uraU^  refuse  fodder.  The  some  prefix occnr^  in  or-deal ;  for  which  see  DcaL
Eaves,  the  clipped  edge  of  a  thatc^ roof.  \E.^  M.  E  eutu\  pi  tuesu  ( eaveses).  AS.  efese^  a  clipped  edge  J thatch ;  whence  e/etian,  to  sorar.  ^  li N/Ui  Swed.  dial,  uffs,  Goth.  M^itiMi,  a  poi from  (he  prcjectioa  of  the  eaves ;  O.  Hj e/asa.  Urig.  sense  'that  which  profi or  is  over ; '  allied  to  Over.  Dar.  Ml dropper^  one  who  stands  under  droppi from  the  eaves,  a  secret  lisicncr.
Ebb.  (E.)  M.  £.  ehbe.  A.  S.  cM«^ ' of  the  tide.  +  Du.  e^.  ebb*,  sb..  Daa. « sb  and  vb.,  Swed.  ehh,  sb.     Allied  to  Bt
Ebony,  a  hard  wood.  (F.-U-Gk Hcb  >   Formerly  fAr«.  — O.  F.  eb€nt.t\<^
—  L.  hebenus,  ebeHum.^G)L.l&*^at,  ifii
—  Mcb.  Aovtt/m,  p!..  ebony  wood;  (ifol non-Semitic  word.
Ebriety.dninkcnnesi.  (F.^L.^  F^dn
—  L.  ace  ekrietaUtH.^l^  i^riuM,  dnul Der.  tH-edriate,  to  make  dninkea.
sober.  (F.  -  L.)    .M .  E.  j^^e.  -  K.  kJ "L,  jobrium,  ace.  of  sit^'^fM^  sober. -^L
s  je'^  apart,  hence,  not ;  eAn'us^  drvnk.  O scbrietyt  F.  jobrutit  L  ace.  sobri4imitm4
Ebullition;  see  BuU  («),
leaf 152
```


## [2026-09-06T15:18:07.088Z] TOOL CALL #46: Bash

```json
{
 "command": "ls site/pages/220.jpg 2>/dev/null; pdftoppm -f 220 -l 220 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg220 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T15:18:09.365Z] TOOL RESULT

```
site/pages/220.jpg
total 2944
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:18 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    462 Sep  6 11:14 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb 431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb   6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb   9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb  11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb  37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb  77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb  61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb  80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb 141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb  76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb 147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb  63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb 118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55412 Sep  6 11:15 pg224.png
```


## [2026-09-06T15:18:12.306Z] TOOL CALL #47: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg220.png"
}
```


### [2026-09-06T15:18:12.765Z] TOOL RESULT

```

```


## [2026-09-06T15:18:12.762Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:18:24.417Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '1,80p' tools/verify_check.py"
}
```


### [2026-09-06T15:18:24.466Z] TOOL RESULT

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


## [2026-09-06T15:18:26.379Z] TOOL CALL #49: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py"
}
```


### [2026-09-06T15:18:26.420Z] TOOL RESULT

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


## [2026-09-06T15:18:59.974Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### etymonline hegira\"; grep -n -A4 \"hegira (n\" 5ad3194268c9a89f.txt | head -20; echo \"### heb הגר\"; grep -n -A8 \"Etymology\" 8c24c99df6cbbe7d.txt | sed -n '1,40p'; echo \"### root ه ج ر\"; grep -n -A10 \"Root\\b\" bba55168025cce57.txt | sed -n '1,30p'"
}
```


### [2026-09-06T15:19:00.085Z] TOOL RESULT

```
### etymonline hegira
23: hegira (n.) 
24-
25- flight of Muhammad from Mecca to Medina (July 16, 622 C.E.), the event from which the Islamic calendar reckons, 1580s, from Medieval Latin hegira , from Arabic hijrah "departure," from hajara "to depart."
26-
27- Entries linking to hegira 
### heb הגר
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Proper noun 
69-
70- 1.2 
71: Etymology 2 
72-
73- 1.2.1 
74- Verb 
75-
76- 1.2.1.1 
77- Derived terms 
78-
79- 1.3 
80: Etymology 3 
81-
82- 1.3.1 
83- Pronunciation 
84-
85- 1.3.2 
86- Noun 
87-
88- 1.4 
--
97: Etymology 
98-
99- 2.2 
100- Proper noun 
101-
102- Toggle the table of contents 
103-
104- הגר 
105-
--
172: Etymology 1
173- [ edit ] 
### root ه ج ر
```


## [2026-09-06T15:19:02.269Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '170,215p' 8c24c99df6cbbe7d.txt"
}
```


### [2026-09-06T15:19:02.384Z] TOOL RESULT

```
 [ edit ] 

 Etymology 1
 [ edit ] 

 Pronunciation
 [ edit ] 

 ( Modern Israeli ) IPA ( key ) : /haˈɡaʁ/ 

 Audio : ( file ) 

 Proper noun
 [ edit ] 

 הָגָר • ( hagár )  f 

 ( biblical ) Hagar 

 a female given name , Hagar 

 ( Medieval ) Hungary 
 Synonym: ( modern ) הונגריה 

 Etymology 2
 [ edit ] 

 Root 

 ה־ג־ר ( h-g-r ) 

 3 terms 

 Coined by Eliezer Ben-Yehuda based on Arabic هَاجَرَ ( hājara , “ to migrate ” ) and the name הָגָר ( hagár , “ Hagar ” ) above, which he concluded belong to a shared Semitic root. The verb with pa'al construction did not become widely used, but it's action noun הֲגִירָה ( hagirá , “ emigration ” ) and a pi'el verb היגר / הִגֵּר ( higér , “ to emigrate, to immigrate ” ) did.

 Verb
 [ edit ] 

 הָגַר • ( hagár ) ( pa'al construction ) 

 ( rare , obsolete ) to emigrate 
 Synonym: היגר / הִגֵּר 

 Derived terms
 [ edit ]
```


## [2026-09-06T15:19:09.271Z] TOOL CALL #52: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg220.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/220.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/220.png"
}
```


### [2026-09-06T15:19:09.358Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 63280 Sep  6 11:19 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/220.png
```


## [2026-09-06T15:25:22.963Z] TOOL CALL #53: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-220.json",
 "content": "{\n  \"pdf_page\": 220,\n  \"book_page\": 190,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Hebhel\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Biblical Hebrew הֶבֶל heḇel 'breath, vapour, vanity'; also the personal name Heḇel (Abel), Gen. 4\",\n      \"note\": \"Klein s.v. 'Abel' (1966 ed. leaf 13 = pp. 2-3) prints verbatim: 'Abel, masc. PN.; in the Bible, the second son of Adam and Eve. — L., fr. Gk. Ἄβελ, fr. Heb. Hebhel, lit. ‘breath, vanity’.' Nourai's root name, language label and gloss are Klein's own, letter for letter ('Hebhel' = his transliteration of הֶבֶל with spirantised bh = ḇ). Wiktionary adds the one caveat: the personal name is only 'possibly' the homonymous common noun heḇel 'breath, vapour; vanity' (the word of Eccl. 1:2 hăḇēl hăḇālîm) and may instead be Akkadian ablu 'son'; that reservation touches the name, not the Hebrew word, so the root box stands. Note also that Nourai's page numbers for Klein on this page (KLN:496, KLN:694) sit ~4% below the 1966 two-volume pagination (ebony = leaf 270 ≈ p.516; Hagar/hegira = leaves 374/385 ≈ pp.724/746) while KLN:3 is exact — the signature of the compressed 1971 one-volume 'unabridged' reprint, which is evidently the copy he used.\",\n      \"note_fa\": \"ریشهٔ عبری הֶבֶל (heḇel) به معنای «دم، بخار، بیهودگی» است و در سفر پیدایش (باب ۴) نام دومین پسر آدم و حوا نیز هست. کلاین در مدخل Abel (چاپ ۱۹۶۶، برگ ۱۳ ≈ ص ۳) دقیقاً همین را می‌آورد و بنابراین نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است. تنها نکتهٔ احتیاطی آن است که ویکی‌واژه پیوند نامِ خاص «هابیل» را با اسم عامِ heḇel «دم، بخار» تنها «محتمل» می‌داند و احتمال دیگری (اکدی ablu «پسر») را نیز یاد می‌کند. در مجموع ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Abel\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:3\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 1150 (leaf 13 = pp.2-3): 'Abel, masc. PN.; in the Bible, the second son of Adam and Eve. — L., fr. Gk. Ἄβελ, fr. Heb. Hebhel, lit. ‘breath, vanity’.' Exactly the root box (grep -n '^Abel,' KLN_1966.txt).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"1966 leaf 13 (pp. 2-3), s.v. Abel; also line 6015 s.v. cable\", \"stance\": \"supports\", \"note\": \"s.v. 'cable' Klein separately lists 'Heb. hebhel, ‘rope, cord’' as a homonym, confirming that the transliteration Hebhel = הֶבֶל and that Klein keeps the two Hebrew hebhel words apart.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Abel\", \"stance\": \"partial\", \"note\": \"'from Biblical Hebrew הֶבֶל (Héḇel, ‘Abel’), possibly from the homonymous word הֶבֶל (heḇel, ‘breath, vapor; vanity’) or from Akkadian 𒌉𒍑 (ablu, ‘son’)' — same Hebrew etymon, but the 'breath, vanity' sense is flagged as only probable.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through node for Arabic هابيل Hābīl, the traditional Islamic name of Adam's murdered son. Arabic did not take the name straight from Hebrew: Wiktionary derives هابيل from Classical Syriac ܗܰܒܶܝܠ (hābēl), the Peshitta form of Heb. הֶבֶל, which reached Arabic through Syriac-speaking Christian and Jewish transmitters of biblical lore in the 6th-7th c. The Syriac spelling with initial hā- gives Arabic hā- (long ā), and the final -īl is analogical to the many Semitic names in -īl current in Arabic (Ismāʿīl, Jibrīl, Isrāʾīl). The name itself is not in the Qur'an — Q 5:27-31 tells the story of 'the two sons of Adam' without naming them; Hābīl and Qābīl come from the tafsīr and qiṣaṣ al-anbiyāʾ literature.\",\n          \"derivation_fa\": \"این گره واسطهٔ عربی است، یعنی «هابیل» عربی. عربی این نام را نه یکراست از عبری، بلکه به گواهی ویکی‌واژه از سریانی کلاسیک ܗܒܝܠ (hābēl) — صورت پشیطتا از עברי הֶבֶל — وام گرفته است؛ راه انتقال، ادبیات دینی مسیحیان و یهودیان سریانی‌زبان در سده‌های ششم و هفتم میلادی بوده است. الفِ کشیدهٔ آغازی از همان hā- سریانی است و پایانهٔ ‑īl به قیاس نام‌های سامیِ رایج در عربی (اسماعیل، جبریل، اسرائیل) افزوده شده. یادآور می‌شود که این نام در قرآن نیامده است؛ در سورهٔ مائده (آیات ۲۷ تا ۳۱) تنها از «دو پسر آدم» سخن رفته و نام‌های هابیل و قابیل از تفسیر و قصص‌الانبیا آمده‌اند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%A8%D9%8A%D9%84\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference on this pass-through Arabic box; the claim is covered by KLN:3 on the root and by MON6:2237 on the child.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/هابيل (Arabic section)\", \"stance\": \"supports\", \"note\": \"'هابيل … Etymology: From Classical Syriac ܗܰܒܶܝܠ (hābēl).' — an Arabic form of the Hebrew name, mediated by Syriac, exactly as the Hebrew→Arabic arrow requires.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 13 s.v. Abel\", \"stance\": \"silent\", \"note\": \"Klein traces the name only through Greek and Latin to English; he says nothing about the Arabic branch.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"Hâbîl\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian هابیل Hābīl is the Arabic name taken over unchanged after the Islamic conquest, along with the whole cast of the qiṣaṣ al-anbiyāʾ; it is a proper name, not a common noun, and Persian keeps the Arabic vocalisation hā-bī-l. Qatrān of Tabriz (11th c.), quoted by Nourai, already uses it in the fixed antithesis Hābīl/Qābīl. Dehkhoda's entry (via Abadis) states the meaning explicitly: 'هابیل = نفس، بخار' ('Hābīl = breath, vapour'), i.e. the same Hebrew heḇel, and Abadis's name dictionary labels it 'معرب از عبری: نفس یا بخار' ('Arabicised from Hebrew: breath or vapour') — Nourai's chain Hebrew → Arabic → Persian in full.\",\n          \"derivation_fa\": \"«هابیل» در فارسی نو وام‌واژه‌ای عربی است که پس از اسلام همراه با مجموعهٔ قصص‌الانبیا وارد زبان شده و نام خاص است، نه اسم عام؛ آوایش عربی hā-bī-l بی‌دگرگونی حفظ شده است. قطران تبریزی (سدهٔ پنجم هجری) در بیتی که نورایی آورده، آن را در تقابل همیشگی «هابیل / قابیل» به کار برده است. دهخدا نیز می‌نویسد «هابیل = نفس، بخار» و در فرهنگ نام‌ها آمده «معرب از عبری: نفس یا بخار»؛ یعنی همان زنجیرهٔ عبری ← عربی ← فارسی که نورایی ترسیم کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%87%D8%A7%D8%A8%DB%8C%D9%84/\",\n            \"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%A8%D9%8A%D9%84\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AKM:1\", \"status\": \"not_checked\", \"note\": \"A'lam, Farhang-e A'lam-e Ketab-e Moqaddas: refs_online.json marks it 'purchase' only, no digital copy found; nothing on archive.org/noorlib.\"},\n            {\"ref\": \"MON6:2237\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 6 (اعلام) is not digitised: vajehyab/abadis serve only the lexicon volumes 1-3, and the local MON_part1/part2 OCR has no هابیل (grep -n 'هابیل' MON_part*.txt returns nothing). Dehkhoda's parallel entry, however, gives exactly the gloss Mo'in's a'lam volume would ('هابیل = نفس، بخار').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Dehkhoda (via Abadis)\", \"where\": \"abadis.ir/fatofa/هابیل, section لغت نامه دهخدا\", \"stance\": \"supports\", \"note\": \"'هابیل. (اِخ) پسر دومین آدم است… اسم مسطور (هابیل = نفس، بخار)…' — Persian lexicography gives the same Hebrew sense 'breath, vapour' that Klein gives for Hebhel.\"},\n            {\"src\": \"MON (via Abadis)\", \"where\": \"abadis.ir/fatofa/هابیل, name dictionary\", \"stance\": \"supports\", \"note\": \"'معرب از عبری نفس یا بخار… (عبری) به معنی ‘نفس یا بخار’' — the Persian form is explicitly an Arabicised Hebrew name; the Mo'in lexicon volumes have no entry (proper name, vol. 6).\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/هابيل\", \"stance\": \"supports\", \"note\": \"Arabic هابيل < Classical Syriac hābēl — the immediate donor of the Persian form.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"Abel\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Septuagint Greek Ἅβελ (Hábel), indeclinable, the standard LXX rendering of Heb. הֶבֶל in Gen. 4:2-25 and carried into the New Testament (Mt 23:35, Heb 11:4). Greek had no /h/-letter but wrote the Hebrew initial he with the rough breathing, hence Ἅβελ with spiritus asper; Hebrew segholate ḥéḇel/héḇel gives Greek -a-e- because the LXX translators regularly render the Hebrew furtive/segholate vowel with alpha in names. Klein's chain 'L., fr. Gk. Ἄβελ, fr. Heb. Hebhel' is precisely this node.\",\n          \"derivation_fa\": \"صورت یونانی Ἅβελ (Hábel) از ترجمهٔ سبعینیه (سپتواگینت) است و در سفر پیدایش ۴ برابر عبری הֶבֶל نشسته و از آنجا به عهد جدید (متی ۲۳:۳۵ و عبرانیان ۱۱:۴) راه یافته است. یونانی حرفی برای «ه» نداشت و آن را با نشانهٔ دمِ درشت (spiritus asper) نشان می‌داد، از این رو Ἅβελ. مصوت نخست عبری در نام‌های سبعینیه معمولاً با «آلفا» نوشته می‌شود. کلاین نیز همین زنجیره را می‌آورد؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Abel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:3\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 1150: '— L., fr. Gk. Ἄβελ, fr. Heb. Hebhel' — the Hebrew→Greek arrow verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Abel, etymology tree\", \"stance\": \"supports\", \"note\": \"'Biblical Hebrew הָ֑בֶל (háḇel) bor. → Ancient Greek Ἅβελ (Hábel) bor. → Latin Abē̆l' — identical route, with the rough breathing noted in the Greek headword.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 13\", \"stance\": \"supports\", \"note\": \"as above.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Pass-through node for Latin Abel, the Vulgate form, borrowed from Septuagint/NT Greek Ἅβελ; Latin dropped the Greek rough breathing (no h- is written) and kept the name indeclinable in ecclesiastical usage, though a genitive Abelis occurs. Wiktionary's Latin entry: 'Borrowed from Ancient Greek Ἅβελ (Hábel), itself from Biblical Hebrew הֶ֫בֶל… The vowel, while short by etymology, is shown to be carrying stress by the descended Italian Abele and Spanish Abel.'\",\n          \"derivation_fa\": \"این گرهِ واسطه لاتینیِ Abel است، همان صورتِ وولگاتا که از یونانیِ سبعینیه/عهد جدید (Ἅβελ) وام گرفته شده. لاتینی نشانهٔ دمِ درشتِ یونانی را ننوشت و نام در کاربرد کلیسایی بیشتر بدون صرف ماند (هرچند گاه Abelis در حالت اضافی دیده می‌شود). ویکی‌واژه نیز همین وام‌گیری را ثبت کرده و می‌افزاید که تکیه بر هجای نخست، از بازماندگانِ ایتالیایی Abele و اسپانیایی Abel بازسازی می‌شود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Abel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference is printed on this pass-through Latin box; the arrow is covered by KLN:3 on the neighbouring boxes.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Abel, Latin section\", \"stance\": \"supports\", \"note\": \"'Borrowed from Ancient Greek Ἅβελ (Hábel), itself from Biblical Hebrew הֶ֫בֶל (heḇel).'\"},\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 13 s.v. Abel\", \"stance\": \"supports\", \"note\": \"Klein has English Abel '— L., fr. Gk. …', so Latin is the intermediate exactly as drawn.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"Abel\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Abel comes down from Old English Ābel (in Ælfric and the OE Genesis, taken from the Vulgate) through Middle English Abel; it has never been anything but a learned/biblical name, so the form is unchanged apart from the Great Vowel Shift raising ME /aː/ to /eɪ/, giving modern /ˈeɪbəl/. Klein's entry states the whole chain in one line; Wiktionary gives the intermediate stages 'Middle English Abel, from Old English Ābel, from Latin Abel'.\",\n          \"derivation_fa\": \"نامِ انگلیسی Abel از انگلیسی کهن Ābel (در آثار الفریک و «پیدایش» انگلیسی کهن، برگرفته از وولگاتا) و سپس انگلیسی میانه Abel به انگلیسی نو رسیده است. چون همواره نامی کتابی و دینی بوده، صورتش دگرگون نشده و تنها بر اثر «جابه‌جایی بزرگ واکه‌ها» (Great Vowel Shift) مصوت /aː/ انگلیسی میانه به /eɪ/ بدل شده و امروز /ˈeɪbəl/ تلفظ می‌شود. کلاین همین زنجیره را در یک سطر آورده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Abel\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:3\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 1150, s.v. Abel: the headword is the English name and the etymology is '— L., fr. Gk. Ἄβελ, fr. Heb. Hebhel' — the Latin→English arrow.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Abel, English section\", \"stance\": \"supports\", \"note\": \"'From Middle English Abel, from Old English Ābel, from Latin Abel, from Ancient Greek Ἅβελ (Hábel), from Biblical Hebrew הֶבֶל.'\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 1, leaf ~4875 area (A'bel)\", \"stance\": \"partial\", \"note\": \"Funk & Wagnalls has the headword \\\"A'bel\\\" among the biblical proper names but its OCR here is badly broken; it adds nothing beyond the biblical identification.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Hebni\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"Egyptian hbnj (also hbny) 'ebony (wood)'\",\n      \"note\": \"The root box is right in substance: the Egyptian word for ebony, hbnj/hbny, is the accepted ultimate source of Greek ἔβενος and thence of the whole European and Iranian family. AHD (5th ed., online) s.v. ebony: '[Probably from Middle English hebenyf, ebony wood, from alteration of Late Latin hebeninus, of ebony, from Greek ebeninos, from ebenos, ebony tree, from Egyptian hbny.]' — Nourai's AHD:411 is the 1975/76 New College page for this entry. Two reservations, both minor: (a) the gloss 'common in India' is off — Egyptian hbnj denoted the black African heartwood (Dalbergia melanoxylon) shipped up from Nubia and Punt, which is why the word travelled with the trade; the Indian/Ceylonese Diospyros ebenum only later took over the name; (b) Skeat and Lokotsch stop the chain earlier (Skeat at Hebrew hobnīm 'probably a non-Semitic word'; Lokotsch calls the Greek word 'ultimately of Phoenician origin'), but Egyptological evidence has since settled the matter in Nourai's favour — Hebrew הָבְנִים hoḇnīm (Ezek. 27:15) is itself the Egyptian word borrowed.\",\n      \"note_fa\": \"جعبهٔ ریشه در اصل درست است: واژهٔ مصریِ hbnj/hbny «آبنوس» سرچشمهٔ پذیرفته‌شدهٔ ἔβενος یونانی و از آن راه، سرچشمهٔ همهٔ صورت‌های اروپایی و ایرانی این واژه است؛ فرهنگ American Heritage (ویراست پنجم) نیز صریحاً می‌نویسد «from Greek ebenos … from Egyptian hbny». دو نکتهٔ کوچک: نخست آنکه توضیح نورایی («رایج در هند») دقیق نیست، زیرا واژهٔ مصری چوب سیاه آفریقایی (Dalbergia melanoxylon) را می‌نامید که از نوبه و سرزمین پونْت به مصر می‌رسید و تنها بعدها این نام به گونهٔ هندی/سیلانی (Diospyros ebenum) داده شد؛ دوم آنکه اسکیت این زنجیره را تا عبری hoḇnīm و لوکوچ آن را تا «خاستگاه فینیقی» دنبال می‌کنند، ولی مصرشناسی امروز حق را به نورایی می‌دهد و صورت عبری را خود وامی از مصری می‌داند.\",\n      \"sources\": [\n        \"https://www.ahdictionary.com/word/search.html?q=ebony\",\n        \"https://en.wiktionary.org/wiki/%E1%BC%94%CE%B2%CE%B5%CE%BD%CE%BF%CF%82\",\n        \"https://www.etymonline.com/word/ebony\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"AHD:411\", \"status\": \"supports\", \"note\": \"The 1975/76 AHD New College appendix pages are 1505-1550, so AHD:411 is a main-dictionary page — the 'ebony' entry. The current AHD text (ahdictionary.com/word/search.html?q=ebony) reads '…from Greek ebenos, ebony tree, from Egyptian hbny', which is the root box word for word. Watkins's IE-roots list (AHD_watkins1985.txt) is silent, as expected: the word is not Indo-European (grep -i 'ebony\\\\|ebenus' AHD_watkins1985.txt → no hits).\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"KLN\", \"where\": \"1966 leaf 270 (≈ p.516), s.v. ebony\", \"stance\": \"supports\", \"note\": \"'ebony, n. — OF. ebaine (F. ébène), fr. L. ebenus …, fr. Gk. ἔβενος (whence also Arabo-Persian abanūs), fr. Egypt. hebni (whence also Heb. pl. hobhnīm, Ezek. 27:15).' Klein even spells the Egyptian word 'hebni', which is where Nourai's root name comes from.\"},\n        {\"src\": \"SKT\", \"where\": \"leaf 152 (≈ p.132), s.v. Ebony\", \"stance\": \"partial\", \"note\": \"'Ebony, a hard wood. (F.-L.-Gk.-Heb.) Formerly heben. — O.F. ebene … — L. hebenus, ebenum. — Gk. ἔβενος … — Heb. hobnīm, pl., ebony wood; probably a non-Semitic word.' Skeat routes the Greek through Hebrew and only hints at the non-Semitic (i.e. Egyptian) source.\"},\n        {\"src\": \"LKT\", \"where\": \"entry 3 (leaf 27 = p.1), 'Ar. abanūs'\", \"stance\": \"partial\", \"note\": \"'[Das selbst aus gr. ἔβενος, letzten Endes phönizischen Ursprungs ist] ‘Ebenholz’' — Lokotsch has the Greek source but calls it ultimately Phoenician, not Egyptian; superseded.\"},\n        {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ἔβενος\", \"stance\": \"supports\", \"note\": \"'ἔβενος … Etymology: Borrowed from Egyptian hbnj.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Greek\",\n          \"words\": \"ebnos\",\n          \"verdict\": \"transcription_suspect\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"ebnos\",\n          \"correct_form\": \"ebenos (ἔβενος)\",\n          \"derivation\": \"The Greek word is ἔβενος (ébenos) f./m. 'ebony tree, ebony wood', attested from Herodotus 3.97 (Ethiopian tribute of ebony logs to Persia) and Theophrastus; the book's box prints 'ebnos', with the second epsilon dropped. The printed page (rendered at 200 dpi, copy at data/verification/sources/refs/ocr/BOOK/220.png) clearly shows 'ebnos : ebony tree', so the JSON extraction is faithful and the missing vowel is Nourai's own misprint — Klein, whom he otherwise follows here, prints 'Gk. ἔβενος'. With that corrected, the derivation is right: Egyptian hbnj, a wood-name of the Nubian trade, was taken into Greek in the archaic period (probably through Phoenician or Cyrenaic middlemen), Egyptian h- being lost and the consonant cluster broken by an anaptyctic vowel, giving ἔβενος with the initial e- of many Greek loans from Egyptian.\",\n          \"derivation_fa\": \"صورت درست یونانی ἔβενος (ébenos) «درخت و چوب آبنوس» است که از هرودوت (۳٫۹۷، در باب خراج آبنوسِ حبشیان به هخامنشیان) و تئوفراستوس به بعد گواهی دارد؛ اما کتاب «ebnos» چاپ کرده و یک «ه/e» از میان واژه افتاده است. تصویر صفحهٔ چاپی (نگهداری‌شده در data/verification/sources/refs/ocr/BOOK/220.png) به‌روشنی «ebnos» را نشان می‌دهد؛ پس خطا از خوانش اسکن نیست، بلکه خطای چاپی خودِ کتاب است — کلاین که نورایی در همین‌جا از او پیروی می‌کند، ἔβενος نوشته است. با اصلاح این صورت، اشتقاق درست است: واژهٔ مصری hbnj در دورهٔ باستان (احتمالاً به میانجی فینیقی‌ها) به یونانی رفت، «ه» آغازین افتاد و برای شکستن خوشهٔ همخوانی واکه‌ای میانجی افزوده شد.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BC%94%CE%B2%CE%B5%CE%BD%CE%BF%CF%82\",\n            \"https://www.ahdictionary.com/word/search.html?q=ebony\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD:411\", \"status\": \"supports\", \"note\": \"AHD s.v. ebony: '…from Greek ebeninos, from ebenos, ebony tree, from Egyptian hbny' — the Egyptian→Greek arrow, but with the correct spelling ebenos, confirming the book's 'ebnos' is a misprint.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 270, s.v. ebony\", \"stance\": \"supports\", \"note\": \"'fr. Gk. ἔβενος … fr. Egypt. hebni' — same arrow, correct Greek form.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ἔβενος\", \"stance\": \"supports\", \"note\": \"'ἔβενος • (ébenos) f or m … ebony tree, wood', alternative forms ἔβελος, ἐβένη; 'Borrowed from Egyptian hbnj'.\"},\n            {\"src\": \"SKT\", \"where\": \"leaf 152 s.v. Ebony\", \"stance\": \"supports\", \"note\": \"'— Gk. ἔβενος' (OCR garbled but the Greek form is the same).\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"âwanos\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"A Middle Persian form is certainly attested: MacKenzie's Concise Pahlavi Dictionary p.4 lists 'abnūs [ʾpnws | (N ābnūs)] ebony' (PHD.txt line 170; the reverse index PHD.txt line 1733 'ebony abnūs'). The Pahlavi spelling ⟨ʾpnws⟩ is ambiguous: MacKenzie normalises it abnūs, while Nourai (following Mo'in) reads âwanos, taking ⟨p⟩ at its usual intervocalic value /w/ and supplying an anaptyctic vowel. Nourai's reading is not invented — Persian preserves the doublet آونوس āwnūs beside آبنوس ābnūs (Wiktionary lists it under 'Alternative forms'), which presupposes exactly a MP *āw(a)nōs — but the standard normalisation is abnūs, so the node is 'plausible' rather than 'confirmed'. The word entered Middle Persian from Greek ἔβενος in the Sasanian period, most likely through Syriac medical and materia-medica literature (ebony was a drug as well as a luxury wood, cf. the eye-remedy use in Borhān), with Greek e- reinterpreted as the Iranian long ā- of the following syllable.\",\n          \"derivation_fa\": \"وجود صورتی در فارسی میانه قطعی است: مکنزی در «فرهنگ کوچک پهلوی» (ص ۴) می‌آورد «abnūs [ʾpnws | (فارسی نو ābnūs)] آبنوس». اما املای پهلویِ ⟨ʾpnws⟩ دوپهلوست: مکنزی آن را abnūs می‌خواند و نورایی (به پیروی از معین) âwanos، زیرا «پ» در میان دو واکه در پهلوی معمولاً /w/ خوانده می‌شود و واکه‌ای میانجی نیز افزوده‌اند. خوانش نورایی بی‌پایه نیست، چون فارسی صورت دوگانهٔ «آونوس» را در کنار «آبنوس» نگاه داشته است (ویکی‌واژه آن را در «صورت‌های دیگر» آورده) و این خود بر *āw(a)nōs پهلوی دلالت دارد؛ ولی چون خوانشِ معیار abnūs است، این گره «با احتیاط پذیرفتنی» ارزیابی می‌شود. راه ورود واژه از یونانی ἔβενος در دورهٔ ساسانی و به احتمال زیاد از راه ادبیات پزشکی سریانی بوده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D9%86%D9%88%D8%B3\",\n            \"https://abadis.ir/fatofa/%D8%A2%D8%A8%D9%86%D9%88%D8%B3/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:26\", \"status\": \"supports\", \"note\": \"Mo'in vol. 1 p.26 is the آبنوس entry; the online Mo'in text (abadis.ir/fatofa/آبنوس, section فرهنگ معین) reads '(آبنوس) [په.] (اِ) درختی است با چوبِ بسیار سخت، سیاه رنگ و گران بها' — the tag [په.] = پهلوی is exactly Nourai's Pahlavi box. The Latin-script Pahlavi form of the print edition (whence 'âwanos') is not reproduced online.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie p.4, s.v. abnūs (PHD.txt line 170; reverse index line 1733)\", \"stance\": \"partial\", \"note\": \"'abnūs [ʾpnws | (N ābnūs)] ebony' — the Pahlavi word and the New Persian descendant are confirmed, but MacKenzie normalises the spelling as abnūs, not âwanos.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep -i 'abnus\\\\|ebony' NYB.txt / NYB_vol2_glossary.txt returns nothing; the word does not occur in Nyberg's text corpus.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/آبنوس\", \"stance\": \"supports\", \"note\": \"'Inherited from Middle Persian 𐫀𐫛𐫗𐫇𐫘 (ʾpnws /abnūs/), from Ancient Greek ἔβενος (ébenos), from Egyptian hbnj' — and 'Alternative forms: آونوس (āwnūs / âvnus)', which is the doublet behind Nourai's reading.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Persian\",\n          \"words\": \"âbnŭs\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian آبنوس ābnūs 'ebony' is inherited straight from the Middle Persian word (Wiktionary: 'Inherited from Middle Persian ʾpnws /abnūs/'), the initial a- being lengthened to ā- by folk association with آب āb 'water' (the spelling آبنوس with alef madda shows the reanalysis). Ferdowsī's line quoted by Nourai (چو روی هوا چون گشت چون آبنوس) already has the classical form and the transferred sense 'pitch-black'. Borhān-e Qāṭeʿ p.12 (BQT_v1_pages.txt leaf 220, confirmed by the 'continued from p.13/14' catchlines on leaves 221-222) has the entry: 'آبنوس — بر وزن خاک‌بوی، درختی باشد سیاه و مشهور… اگر بر آتش نهند مانند عود بگدازد… و اگر با آب بسایند و در چشم کشند شب‌کوری را ببرد'. The Arabic آبنوس/أبنوس abanūs is the same Greek word taken by a parallel route (Klein: 'whence also Arabo-Persian abanūs'), so Persian ābnūs is not an Arabic loan but a Sasanian-era inheritance.\",\n          \"derivation_fa\": \"«آبنوس» در فارسی نو میراث مستقیم صورت فارسی میانه است (ویکی‌واژه: «برگرفته از فارسی میانهٔ ʾpnws /abnūs/») و «الف» آغازینِ کوتاه بر اثر همانندسازی عامیانه با واژهٔ «آب» کشیده شده است؛ املای «آبنوس» با الف مدّه گواه همین ریشه‌شناسی عامیانه است. بیت فردوسی که نورایی آورده («چو روی هوا چون گشت چون آبنوس…») هم صورت کلاسیک و هم معنای مجازی «سیاهِ تیره» را نشان می‌دهد. برهان قاطع، ص ۱۲، مدخل «آبنوس» را دارد: «بر وزن خاک‌بوی، درختی باشد سیاه و مشهور… اگر بر آتش نهند مانند عود بگدازد… و اگر با آب بسایند و در چشم کشند شب‌کوری را ببرد». «أبنوس» عربی نیز همان واژهٔ یونانی است که از راهی جداگانه وام گرفته شده، پس «آبنوس» فارسی وام‌واژهٔ عربی نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A2%D8%A8%D9%86%D9%88%D8%B3\",\n            \"https://abadis.ir/fatofa/%D8%A2%D8%A8%D9%86%D9%88%D8%B3/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:496\", \"status\": \"supports\", \"note\": \"Klein s.v. ebony (1966 leaf 270; his p.496 is the 1971 one-volume pagination): 'fr. Gk. ἔβενος (whence also Arabo-Persian abanūs)' — Klein explicitly names the Persian form and derives it from Greek.\"},\n            {\"src\": \"BQT:12\", \"ref\": \"BQT:12\", \"status\": \"supports\", \"note\": \"Borhān-e Qāṭeʿ p.12 = BQT_v1_pages.txt leaf 220 (page identified by the 'خه از صفحهٔ ۱۳' / 'در صفحهٔ ۱۴' catchlines on leaves 221-222): 'آبنوس - بر وزن خاک‌بوی، درختی باشد سیاه و مشهور و آن را عربی نیز آبنوس خوانند…' — the headword is exactly where Nourai says it is, though Mo'in adds no etymological footnote to it here.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BQT\", \"where\": \"vol. 1 p.12 (leaf 220), s.v. آبنوس\", \"stance\": \"supports\", \"note\": \"'آبنوس … درختی باشد سیاه و مشهور … و اگر با آب بسایند و در چشم کشند شب کوری را برد' — the word and its medical use; no etymological note attached.\"},\n            {\"src\": \"MON (via Abadis)\", \"where\": \"abadis.ir/fatofa/آبنوس, فرهنگ معین\", \"stance\": \"supports\", \"note\": \"'(آبنوس) [په.] (اِ) درختی است با چوبِ بسیار سخت، سیاه رنگ و گران بها' — Mo'in tags the word Pahlavi, i.e. inherited, not Arabic.\"},\n            {\"src\": \"Dehkhoda (via Abadis)\", \"where\": \"abadis.ir/fatofa/آبنوس, فرهنگ فارسی\", \"stance\": \"supports\", \"note\": \"'ماخوذ از کلمهٔ یونانی ابانس' — 'taken from the Greek word', the same ultimate source.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\", \"note\": \"grep -i 'abnūs\\\\|abnus\\\\|Ebenholz' HRN.txt → no hits; Horn omits the word (it is a culture-loan, not part of his inherited-vocabulary programme).\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien\", \"stance\": \"silent\", \"note\": \"grep -i 'abnūs\\\\|abnus\\\\|Ebenholz' HUB.txt → no hits.\"},\n            {\"src\": \"AFM\", \"where\": \"Addi Shir, s.v. الشيز (AFM_pages.txt leaf 107)\", \"stance\": \"partial\", \"note\": \"'خشب … الأبنوس وهذا صحيح … بالفارسيّة معناه الأبنوس' — Addi Shir treats Arabic شيز (Pers. شیز) as the Persian name of ebony wood; he does not claim أبنوس itself is Persian, which is consistent with Greek being its source.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"ebeninus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin has both the noun (h)ebenus 'ebony tree/wood' (Virgil, Georg. 2.116) and the adjective ebeninus/hebeninus 'made of ebony'. The adjective is not formed inside Latin: it is the Greek adjective ἐβένινος (ebéninos) taken over whole, as AHD says — 'from alteration of Late Latin hebeninus, of ebony, from Greek ebeninos, from ebenos'. So the arrow Greek → Latin is right, with the refinement that ebeninus continues Greek ἐβένινος rather than being derived from ἔβενος on Latin soil. Wiktionary's tree adds the parallel Ecclesiastical Latin ebenius 'of ebony' (Latin -ius), which is the form that actually feeds the English word.\",\n          \"derivation_fa\": \"لاتینی هم اسم (h)ebenus «درخت و چوب آبنوس» را دارد (ویرژیل، گئورگیکا ۲٫۱۱۶) و هم صفت ebeninus/hebeninus «ساخته از آبنوس». این صفت در خودِ لاتینی ساخته نشده، بلکه صفت یونانی ἐβένινος به تمامی وام گرفته شده است؛ فرهنگ American Heritage نیز می‌نویسد «from Late Latin hebeninus, of ebony, from Greek ebeninos». پس پیکان «یونانی ← لاتینی» درست است، با این دقت که ebeninus دنبالهٔ ἐβένινος است نه ساختی لاتینی از ἔβενος. ویکی‌واژه صورت کلیسایی ebenius را نیز می‌افزاید که سرچشمهٔ بی‌واسطهٔ واژهٔ انگلیسی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=ebony\",\n            \"https://en.wiktionary.org/wiki/ebony\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD s.v. ebony: '[Probably from Middle English hebenyf, ebony wood, from alteration of Late Latin hebeninus, of ebony, from Greek ebeninos, from ebenos, ebony tree, from Egyptian hbny.]' — the Latin adjective is exactly Nourai's ebeninus.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 270, s.v. ebony and Ebenaceae\", \"stance\": \"partial\", \"note\": \"Klein routes English through 'L. ebenus' (and s.v. Ebenaceae 'ModL., formed with suff. -aceae fr. L. ebenus'), i.e. he uses the noun rather than the adjective ebeninus.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ebony, etymology tree\", \"stance\": \"supports\", \"note\": \"'Latin hebenus … Latin ebenius der. → Middle English ebenif' and 'influenced by Late Latin hebeninus' — both Latin forms are recorded.\"},\n            {\"src\": \"SKT\", \"where\": \"leaf 152 s.v. Ebony\", \"stance\": \"partial\", \"note\": \"'— L. hebenus, ebenum' — Skeat cites only the noun.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"ebony\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English ebony (1590s in this form) rests on Middle English hebenyf/ebenif (late 14c.), itself from Ecclesiastical Latin ebenius / Late Latin hebeninus; the -y of the modern word is a re-formation of the odd ME ending, helped by the older noun ebon (early 15c., from Old French ebene / Latin ebenus). Etymonline: 'dark, hard wood favored for carving… 1590s, perhaps an extended form of Middle English ebon, or from hebenyf (late 14c.), perhaps a Middle English misreading of Latin hebeninus ‘of ebony’, from Greek ebeninos, from ebenos ‘ebony’, probably from Egyptian hbnj'. The figurative sense 'intensely black' dates from the 1620s, matching Ferdowsī's use of ābnūs in the same metaphor six centuries earlier.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی ebony (به این صورت از دههٔ ۱۵۹۰) بر انگلیسی میانهٔ hebenyf/ebenif (اواخر سدهٔ چهاردهم) استوار است که خود از لاتینی کلیسایی ebenius / لاتینی متأخر hebeninus می‌آید؛ پایانهٔ ‑y صورت بازساختهٔ آن پایانهٔ نامأنوس انگلیسی میانه است و واژهٔ کهن‌ترِ ebon (از فرانسهٔ کهن ebene) نیز در آن اثر داشته. اتیمانلاین همین را می‌آورد و ریشهٔ نهایی را «Egyptian hbnj» می‌داند. معنای مجازی «سیاهِ تیره» در انگلیسی از دههٔ ۱۶۲۰ ثبت شده است — همان استعاره‌ای که فردوسی شش سده پیش‌تر با «آبنوس» به کار برده بود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/ebony\",\n            \"https://en.wiktionary.org/wiki/ebony\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference printed on this box; the arrow is covered by the AHD citation on the parent Latin node, which states the Latin→Middle English→English chain in full.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/ebony\", \"stance\": \"supports\", \"note\": \"'From earlier heben, hebeny, from Middle English ebenif, hebenyf (influenced by Late Latin hebeninus), from Ecclesiastical Latin ebenius (‘of ebony’), from Latin hebenus…'\"},\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 270, s.v. ebony\", \"stance\": \"supports\", \"note\": \"'ebony, n. — OF. ebaine (F. ébène), fr. L. ebenus' — Latin (via French) → English.\"},\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, vol. 1, s.v. ebony (WEB_vol1.txt line 61109)\", \"stance\": \"supports\", \"note\": \"'a hard, heavy and durable wood… The usual color is black… EBONY (Diospyros ebenum)' — confirms the English sense and the botanical identification.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 2,\n      \"root\": \"H.j.r\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Arabic root ه ج ر (h-j-r) 'to separate oneself, emigrate' < Proto-Semitic *h-g-r; the equation with Hebrew הָגָר Hāgār is only probable\",\n      \"note\": \"The Arabic root is real and its meaning is exactly as given. What is only 'probable' is the second half of the chart — that the Hebrew name Hagar belongs to it. Klein, Nourai's own reference, hedges: s.v. Hagar (1966 leaf 374) 'Heb. Hāghār, prob. rel. to Arab. hajara, ‘he fled, emigrated’, hijra’, ‘flight, emigration’. See hegira.' The correspondence is phonologically impeccable (Proto-Semitic *g > Arabic j, stays g in Hebrew, so Heb. h-g-r = Arab. h-j-r), but Biblical Hebrew has no verb h-g-r at all: the modern Hebrew הָגַר 'to emigrate' was coined by Eliezer Ben-Yehuda precisely on the strength of Arabic hājara and the name Hagar, 'which he concluded belong to a shared Semitic root' (Wiktionary). So Nourai's root box states as fact a hypothesis that rests on Arabic alone; Wiktionary's Hagar entry glosses the Hebrew name 'stranger' instead. Verdict: plausible, not confirmed. A second, purely notational point: a Proto-Semitic root would be cited *h-g-r; 'H.j.r' is the Arabic reflex used as the label for the whole family.\",\n      \"note_fa\": \"ریشهٔ عربی «ه ج ر» و معنای آن («دوری گزیدن، هجرت کردن») بی‌گمان درست است؛ آنچه تنها «محتمل» است نیمهٔ دوم نمودار است، یعنی انتساب نام عبری «هاجر» به همین ریشه. کلاین که خودِ مأخذ نورایی است با احتیاط می‌نویسد: «عبری Hāghār، احتمالاً مرتبط با عربی hajara ‘گریخت، هجرت کرد’». تناظر آوایی بی‌عیب است (گِ سامی آغازین در عربی به «ج» و در عبری به «گ» بدل می‌شود)، اما در عبری کتاب مقدس اصلاً فعلی از ریشهٔ h-g-r نیست؛ فعل عبری امروزین הָגַר «مهاجرت کردن» را الیعزر بن‌یهودا بر پایهٔ همین hājara عربی و نام «هاجر» ساخته است (ویکی‌واژه). پس نورایی فرضیه‌ای را که تنها بر شواهد عربی استوار است، همچون واقعیت آورده و ویکی‌واژه معنای نام عبری را «بیگانه» می‌داند. داوری: با احتیاط پذیرفتنی. نکتهٔ صوری آنکه ریشهٔ سامی آغازین را باید *h-g-r نوشت؛ «H.j.r» صورت بازتاب‌یافتهٔ عربی است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Hagar\",\n        \"https://en.wiktionary.org/wiki/%D7%94%D7%92%D7%A8\",\n        \"https://www.etymonline.com/word/hegira\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"KLN:694\", \"status\": \"partial\", \"note\": \"KLN_1966.txt line 17025 (leaf 374): 'Hagar, n., Sarah’s Egyptian handmaid (Bible). — Heb. Haghār, prob. rel. to Arab. hajara, ‘he fled, emigrated’, hijrah, ‘flight, emigration’. See hegira.' and line 17444 (leaf 385) 'hegira … — Arab. hijrah, ‘flight’, fr. hajara, ‘he fled, emigrated’. Cp. Hagar.' Klein supplies the two halves but joins them only with 'prob. rel.', not as a reconstructed Semitic root.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/הגר (Hebrew, Etymology 2)\", \"stance\": \"partial\", \"note\": \"'Coined by Eliezer Ben-Yehuda based on Arabic هَاجَرَ (hājara, ‘to migrate’) and the name הָגָר (hagár, ‘Hagar’), which he concluded belong to a shared Semitic root.' — the Hebrew verb is a modern coinage, so the 'Semitic root' is inferred, not attested on the Hebrew side.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Hagar\", \"stance\": \"partial\", \"note\": \"'From Hebrew הָגָר (Hagar, ‘stranger’). Compare Arabic هَاجَر (hājar)' — the comparison with Arabic is kept, but the gloss is 'stranger', not 'wandering/emigration'.\"},\n        {\"src\": \"FSD\", \"where\": \"vol. 2, leaf 390 (≈ p.1082), s.v. Ha'gar\", \"stance\": \"supports\", \"note\": \"'Ha'gar … n. Bib. Concubine of Abraham; mother of Ishmael. Gen. xvi, 1. [Heb., wandering]' (OCR of the bracketed gloss is damaged: 'w-Mulenua.i'). Funk & Wagnalls is the source of Nourai's gloss 'wandering'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Arabic\",\n          \"words\": \"h.j.r\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Arabic ه ج ر (h-j-r) is a fully attested triliteral: form I hajara 'to leave, forsake, cut oneself off from', form III hājara 'to emigrate, to leave one's tribe/desert life for the town', with the verbal nouns هِجْرَة hijra 'departure, emigration', هِجْران hijrān, and the participle مُهاجِر muhājir 'emigrant'. The specialised sense — the Prophet's departure from Mecca to Yathrib in 622 CE, made the epoch of the Muslim calendar under ʿUmar — grows out of form III, which in pre-Islamic usage meant abandoning nomadic life for the settled town, precisely what the Meccan emigrants did. Klein's entry for hegira gives the same morphology.\",\n          \"derivation_fa\": \"ریشهٔ سه‌حرفی «ه ج ر» در عربی به‌تمامی گواهی‌شده است: باب اوّل «هَجَرَ» (ترک کردن، دوری گزیدن)، باب سوم «هاجَرَ» (کوچیدن، ترک قبیله و بادیه به قصد شهر)، و مصدرهای «هِجْرَة»، «هِجْران» و اسم فاعل «مُهاجِر». معنای ویژهٔ آن، یعنی کوچ پیامبر از مکه به یثرب در سال ۶۲۲ میلادی که در روزگار عمر مبدأ گاه‌شماری مسلمانان شد، از همان باب سوم برآمده است؛ چه در کاربرد پیش از اسلام نیز «هاجَرَ» یعنی رها کردن زندگی بادیه‌نشینی و روی آوردن به شهر — دقیقاً کاری که مهاجران مکه کردند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%87%D8%A7%D8%AC%D8%B1\",\n            \"https://www.etymonline.com/word/hegira\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:694\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 17444 (leaf 385, s.v. hegira): 'Arab. hijrah, ‘flight’, fr. hajara, ‘he fled, emigrated’' — the Arabic root with exactly Nourai's gloss.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/هاجر (Arabic, Etymology 1)\", \"stance\": \"supports\", \"note\": \"'Root ه ج ر (h j r) … هَاجَرَ (hājara) III … to migrate; (Classical) to separate from one’s own, emigrate from one’s tribe; (Classical) to abandon the nomadic life of the desert to live in the city.'\"},\n            {\"src\": \"KLN\", \"where\": \"1966 leaves 374/385, s.vv. Hagar, hegira\", \"stance\": \"supports\", \"note\": \"as quoted above.\"},\n            {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\", \"note\": \"grep -i 'hijra' FVQ_pages.txt gives only incidental datings ('the First Hijra', 'of the Hijra'); Jeffery has no entry, i.e. he treats hijra as native Arabic — consistent with Nourai's chart.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"hejrat\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian هجرت hejrat is Arabic هِجْرَة hijra borrowed after the conquest; Persian renders the Arabic feminine ending -a(t) (tāʾ marbūṭa) as spelled -at, and the Arabic kasra of the first syllable becomes Persian e, giving hejrat. Mo'in marks it '[ع. هجرة]' ('Arabic, hijra'). It carries both the general sense 'leaving one's homeland' (already in Kalīla wa-Dimna: 'حرمت هجرت و وسیلت غربت را…') and the technical one, the Prophet's emigration of 622 CE that founded the hijrī era, whence the adjective هجری. The chart's extra field lists the rest of the family taken over with it — هجر، هجری، هاجر، مهجور، هجران، مهاجر، مهاجرت — all regular Arabic derivatives of the same root (maf'ūl, fa'lān, mufā'il, mufā'ala patterns), borrowed wholesale as Persian nouns; Hafez's غم هجران in the quoted verse shows هجران fully naturalised in classical poetry.\",\n          \"derivation_fa\": \"«هجرت» در فارسی نو وام‌واژه‌ای است از عربی «هِجْرَة» که پس از فتح اسلامی وارد شده؛ «تاء مربوطه» در فارسی به صورت «ت» نوشته و خوانده می‌شود و کسرهٔ هجای نخست به «ـِ» فارسی بدل می‌گردد، پس hijra ← hejrat. معین آن را با نشانهٔ «[ع. هجرة]» ثبت کرده است. این واژه هم معنای عام «ترک وطن» را دارد (چنان‌که در کلیله و دمنه: «حرمت هجرت و وسیلت غربت را…») و هم معنای خاصِ کوچ پیامبر در سال ۶۲۲ م. را که مبدأ تاریخ هجری شد و صفت «هجری» از آن ساخته شده است. واژه‌های افزودهٔ نمودار — هجر، هجری، هاجر، مهجور، هجران، مهاجر، مهاجرت — همگی مشتقات قاعده‌مند همین ریشه در عربی‌اند (بر وزن‌های مفعول، فعلان، مُفاعِل و مُفاعَلة) که یکجا به فارسی راه یافته‌اند؛ «غم هجران» در بیت حافظ نشان می‌دهد که «هجران» در شعر کلاسیک کاملاً فارسی شده بود. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%87%D8%AC%D8%B1%D8%AA\",\n            \"https://abadis.ir/fatofa/%D9%87%D8%AC%D8%B1%D8%AA/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FVA:443\", \"status\": \"not_checked\", \"note\": \"Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi: refs_online.json records 'no digital copy found' (archive.org, ketabnak, noorlib, web all searched); could not be consulted.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON (via Abadis)\", \"where\": \"abadis.ir/fatofa/هجرت, فرهنگ معین\", \"stance\": \"supports\", \"note\": \"'(هِ رَ) [ع. هجرة] (اِمص.) ۱- کوچ کردن، ترک وطن. ۲- مبداء تاریخ مسلمانان که زمان هجرت پیامبر است از مکه به مدینه برابر با ۶۲۲ م.' — Arabic origin and both senses, exactly Nourai's box.\"},\n            {\"src\": \"Dehkhoda (via Abadis)\", \"where\": \"abadis.ir/fatofa/هجرت, لغت نامه دهخدا\", \"stance\": \"supports\", \"note\": \"'هجرت. [هَِ رَ] (ع اِمص) مفارقت. جدایی… || ترک وطن و دوری از خانمان… || در اصطلاح مسلمین، ترک وطن کفار و انتقال به دارالاسلام' — marked (ع) = Arabic.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/هجرت (Persian)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Arabic هِجْرَة (hijra).'\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Hebrew\",\n          \"words\": \"Hâğâr\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Hebrew הָגָר Hāgār, Sarah's Egyptian handmaid and Ishmael's mother (Gen. 16, 21). The link to the Arabic root is phonologically regular — Proto-Semitic *g is kept in Hebrew as ג and shifts to j in Arabic, so Heb. h-g-r : Arab. h-j-r is a textbook correspondence — but it is an inference, not an attestation: Biblical Hebrew has no verb or noun of this root beside the name, and the modern Hebrew verb הָגַר 'to emigrate' was coined by Ben-Yehuda on the basis of the Arabic word plus this very name. Klein therefore writes only 'prob. rel. to Arab. hajara'; Wiktionary glosses the name 'stranger'; others connect it with Arabic hajar 'stone' or leave it as a foreign (Egyptian) name, fitting for a character the text calls 'the Egyptian'. Nourai's gloss 'wandering' is Funk & Wagnalls'. Node accepted as plausible, not confirmed.\",\n          \"derivation_fa\": \"«هاجر» (עברית הָגָר) در سفر پیدایش (باب‌های ۱۶ و ۲۱) کنیزِ مصریِ سارا و مادر اسماعیل است. پیوند این نام با ریشهٔ عربی از نظر آوایی بی‌عیب است — «گ» سامی آغازین در عبری «گ» می‌ماند و در عربی به «ج» بدل می‌شود، پس h-g-r عبری در برابر h-j-r عربی تناظری کاملاً قاعده‌مند است — اما این پیوند استنباط است نه گواهی: در عبری کتاب مقدس جز همین نام، هیچ فعل یا اسمی از این ریشه نیست و فعل عبری امروزین הָגַר را بن‌یهودا بر پایهٔ همان واژهٔ عربی و همین نام ساخته است. از این رو کلاین تنها می‌نویسد «احتمالاً مرتبط با عربی hajara»؛ ویکی‌واژه معنای نام را «بیگانه» می‌دهد و برخی آن را با «هَجَر» عربی (سنگ) یا نامی مصری می‌سنجند — که با «هاجرِ مصری» بودن او در متن سازگار است. معنای «سرگردانی» را نورایی از فرهنگ فانک و واگنالز گرفته است. داوری: با احتیاط پذیرفتنی.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Hagar\",\n            \"https://en.wiktionary.org/wiki/%D7%94%D7%92%D7%A8\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:694\", \"status\": \"partial\", \"note\": \"KLN_1966.txt line 17025: 'Hagar … — Heb. Haghār, prob. rel. to Arab. hajara, ‘he fled, emigrated’, hijrah, ‘flight, emigration’.' Klein connects them, but only as probable, and gives no Hebrew gloss.\"},\n            {\"ref\": \"FSD:1101\", \"status\": \"supports\", \"note\": \"FSD_vol2.txt line 39695 (leaf 390, running head area ≈ p.1082 in the 1913 scan; Nourai's 1940 printing may number it 1101): 'Ha’gar … n. Bib. Concubine of Abraham; mother of Ishmael. Gen. xvi, 1. [Heb., wandering]' — the source of the gloss 'wandering' in the chart.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Hagar\", \"stance\": \"partial\", \"note\": \"'From Hebrew הָגָר (Hagar, ‘stranger’). Compare Arabic هَاجَر (hājar), Tiberian Hebrew הָגָר (Hāḡār).' — different gloss, same Arabic comparison.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/הגר (Hebrew)\", \"stance\": \"partial\", \"note\": \"the Hebrew verb of this root is Ben-Yehuda's coinage 'based on Arabic هَاجَرَ … and the name הָגָר', so no Biblical Hebrew verb supports the derivation.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 374\", \"stance\": \"partial\", \"note\": \"as quoted.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"Hagar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Hagar is the biblical name as spelled in the Latin Vulgate (Agar) and, with the h- restored from the Hebrew, in Tyndale and the King James Version (Gen. 16:1 'Hagar'); it is a purely learned transmission through Greek Ἄγαρ and Latin, with no phonetic development, the modern pronunciation /ˈheɪɡɑːr/ being a spelling pronunciation. Funk & Wagnalls has the entry, together with the derivative Hagarene 'a Saracen, descendant of Hagar' — the medieval European name for the Arabs, itself a witness to the Hagar/Arab connection the chart draws.\",\n          \"derivation_fa\": \"نام انگلیسی Hagar همان نام کتاب مقدسی است که در وولگاتای لاتینی Agar نوشته می‌شد و در ترجمه‌های انگلیسی تیندل و شاه جیمز با «ه» آغازینِ برگرفته از عبری به صورت Hagar درآمد (پیدایش ۱۶:۱). انتقال آن سراسر کتابی و از راه یونانی Ἄγαρ و لاتینی است، بی‌هیچ تحول آوایی، و تلفظ امروزین /ˈheɪɡɑːr/ تلفظِ برخاسته از املا است. فرهنگ فانک و واگنالز افزون بر خودِ نام، مشتق Hagarene «ساراسن، از نسل هاجر» را نیز دارد — نامی که اروپاییان سده‌های میانه به عرب‌ها می‌دادند و خود گواهی است بر همان پیوند هاجر و عرب که نمودار ترسیم کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Hagar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FSD:1101\", \"status\": \"supports\", \"note\": \"FSD_vol2.txt line 39695 (leaf 390): 'Ha’gar, 1 he’gar; 2 ha’gar, n. Bib. Concubine of Abraham; mother of Ishmael. Gen. xvi, 1. [Heb., wandering]', immediately followed by 'Ha’gar-ene … 1. Bib. A Saracen descendant of Hagar. 2. pl. A people E. of the Jordan.' — Nourai's English box and gloss verbatim.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"Wiktionary\", \"where\": \"en.wiktionary.org/wiki/Hagar (English)\", \"stance\": \"supports\", \"note\": \"'From Hebrew הָגָר (Hagar, ‘stranger’)' — the English name is the Hebrew one, as the arrow says.\"},\n            {\"src\": \"KLN\", \"where\": \"1966 leaf 374, s.v. Hagar\", \"stance\": \"supports\", \"note\": \"Klein's headword is the English name, etymology 'Heb. Haghār' — Hebrew → English directly, as drawn.\"},\n            {\"src\": \"FSD\", \"where\": \"vol. 2, leaf 592 s.v. Ishmael\", \"stance\": \"supports\", \"note\": \"'The son of Abraham and Hagar' — corroborates the gloss 'mother of Ishmael'.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T15:25:23.000Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-220.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T15:25:28.677Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport re,io\np='data/verification/page-220.json'\ns=open(p,encoding='utf-8').read()\ns=s.replace('{\"src\": \"BQT:12\", \"ref\": \"BQT:12\", \"status\": \"supports\"','{\"ref\": \"BQT:12\", \"status\": \"supports\"')\nopen(p,'w',encoding='utf-8').write(s)\nEOF\npython3 -m json.tool data/verification/page-220.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 220"
}
```


### [2026-09-06T15:25:31.836Z] TOOL RESULT

```
JSON OK
nodes verified: 14/14
node verdicts: {'confirmed': 11, 'transcription_suspect': 1, 'plausible': 2}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'not_checked': 6, 'supports': 10, 'partial': 1}
books consulted: {'supports': 28, 'silent': 5, 'partial': 8} | by book: {'Wiktionary': 14, 'KLN': 9, 'Dehkhoda (via Abadis)': 3, 'MON (via Abadis)': 3, 'FSD': 2, 'SKT': 2, 'PHD': 1, 'NYB': 1, 'BQT': 1, 'HRN': 1, 'HUB': 1, 'AFM': 1, 'WEB': 1, 'FVQ': 1}
```


## [2026-09-06T15:25:48.962Z] AGENT

0 PROBLEM lines. Page 220 (book p. 190) verified: 3 entries, 14 nodes.

**Verdicts** — nodes: 11 confirmed, 2 plausible, 1 transcription_suspect. Roots: 2 confirmed, 1 plausible. Ref checks: 10 supports, 1 partial, 6 not_checked. 14 books/sources consulted (Klein 1966, MacKenzie, Skeat, Lokotsch, Addi Shir, Funk & Wagnalls, Webster, Borhan-e Qate' v1, Mo'in/Dehkhoda via Abadis, Jeffery, Horn, Hübschmann, Nyberg, AHD online, Wiktionary, Etymonline).

**Flagged items**
- `transcription_suspect` — Hebni, node #1 Greek `ebnos`: the Greek word is ἔβενος *ebenos*. `error_in: book` — the printed page (copied to `data/verification/sources/refs/ocr/BOOK/220.png`) clearly shows "ebnos", so the extraction is faithful and the dropped epsilon is Nourai's own misprint; Klein, whom he follows, prints ἔβενος.
- `plausible` — Hebni, node #2 Pahlavi `âwanos`: MacKenzie p.4 has the word but normalises ⟨ʾpnws⟩ as *abnūs*. Nourai's reading (from Mo'in) is defensible — Persian keeps the doublet آونوس *āwnūs* — but it is not the standard normalisation.
- `plausible` — ROOT `H.j.r` and node #3 Hebrew `Hâğâr`: Klein (Nourai's own ref) only says Heb. Hāgār is "prob. rel." to Arab. *hajara*; Biblical Hebrew has no h-g-r verb at all — the modern Hebrew הָגַר was coined by Ben-Yehuda *from* the Arabic word and this name. Wiktionary glosses Hagar "stranger". So the chart states a hypothesis as fact.

**No extraction errors** — the JSON matches the printed page everywhere (âwanos, âbnŭs, Hâğâr, ebnos all as printed).

**Incidental findings for the owner**
- Nourai's Klein page numbers are the **1971 one-volume** edition, not the 1966 two-volume set on disk: KLN:3 is exact, but KLN:496 (ebony) = 1966 leaf 270 ≈ p.516 and KLN:694 (Hagar/hegira) = leaves 374/385 ≈ pp.724/746, a consistent ~4% compression. Worth noting for future pages.
- BQT:12 confirmed as `BQT_v1_pages.txt` leaf 220 (identified via the "خه از صفحهٔ ۱۳" catchlines on leaves 221–222) — useful anchor for the vol. 1 offset near the start.
- FSD:1101 (Hagar) sits at leaf 390 ≈ p.1082 in the 1913 scan; Nourai's 1940 printing may number it differently.
- Root gloss "ebony tree (common in India)" is inaccurate: Egyptian *hbnj* denoted African ebony (Dalbergia melanoxylon) from Nubia/Punt; noted in the entry `note` but not flagged as a verdict.
