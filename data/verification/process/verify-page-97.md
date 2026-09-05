# Verification process log — verify-page-97


## [2026-09-05T14:20:51.484Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 97 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-97.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-97.json. Write /home/sfmqrb/git/rishe/data/verification/page-97.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 97` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:20:52.609Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:20:53.313Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:20:53.332Z] TOOL RESULT

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


## [2026-09-05T14:20:53.865Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-97.txt"
}
```


### [2026-09-05T14:20:53.887Z] TOOL RESULT

```
1	=== PDF page 97 (book page 67) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhôi : to fear  (refs POK:161)
4	#1 (parent #0) [Avestan] refs=POK:161,162 | bay : fear ; bhâyaka : fear
5	  #2 (parent #1) [Persian] refs=POK:162; HRN:39,59; BQT:340 | bîm «بیم» : fear ; bâk «باک» : fear
6	#3 (parent #0) [Sanskrit] refs=AEF:320 | bhay : to fear ; bhî-ma : dreadful
7	  #4 (parent #3) [Persian] refs=MON:633 | bîmeh «بیمه» : insurance | NOTE: IEC:723,1562 links this word to root "Weid, Woid: to see"
8	--- entry 1 ---
9	ROOT Bhombhos -> redirect to Bamb
10	--- entry 2 ---
11	ROOT [Indo-European] Bhôu, Bheu : joy, satisfaction  (refs IEC:98)
12	#1 (parent #0) [Persian] refs=IEC:98; MON:607 | bŭyeh «بوی ۲ ، بویه» : desire, hope
13	#2 (parent #0) [Sanskrit] refs=IEC:98 | bhâvita : well arranged
14	--- entry 3 ---
15	ROOT Bhrâ-tar -> redirect to Bher 1
16	--- entry 4 ---
17	ROOT Bhrâ-ter -> redirect to Bher 1
18	--- entry 5 ---
19	ROOT Bhra-ter -> redirect to Ter 3
20	--- entry 6 ---
21	ROOT Bhreg -> redirect to Bhereg
22	--- entry 7 ---
23	ROOT Bhrei -> redirect to Bher 3
24	--- entry 8 ---
25	ROOT Bhreu -> redirect to Bher 5
26	--- entry 9 ---
27	ROOT [Indo-European] Bhru 1 : eyebrow, beam, log  (refs POK:172)
28	#1 (parent #0) [Avestan] refs=POK | brvat : brow
29	  #2 (parent #1) [Pahlavi] refs=BQT:80 | brŭk
30	    #3 (parent #2) [Persian] refs=POK:172; BQT:80; FSF:81 | abrŭ, borŭ «ابرو ، بُرو» : eyebrow
31	#4 (parent #0) [Germanic] refs=AHD | brus : eyebrow
32	  #5 (parent #4) [English] refs=None | brow, eyebrow
33	#6 (parent #0) [Germanic] refs=AHD | brugjô : wooden bridge
34	  #7 (parent #6) [English] refs=None | bridge
35	
```


## [2026-09-05T14:20:55.455Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-05T14:20:56.865Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-97.json | head -200",
 "description": "Read page 97 source JSON"
}
```


## [2026-09-05T14:20:57.293Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T14:20:58.731Z] TOOL RESULT

```
{
    "pdf_page": 97,
    "book_page": 67,
    "entries": [
        {
            "root": {
                "name": "Bh\u00f4i",
                "lang": "Indo-European",
                "refs": "POK:161",
                "gloss": "to fear"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:161,162",
                    "words": [
                        {
                            "translit": "bay",
                            "gloss": "fear",
                            "script": null
                        },
                        {
                            "translit": "bh\u00e2yaka",
                            "gloss": "fear",
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
                    "refs": "POK:162; HRN:39,59; BQT:340",
                    "words": [
                        {
                            "translit": "b\u00eem",
                            "gloss": "fear",
                            "script": "\u0628\u06cc\u0645"
                        },
                        {
                            "translit": "b\u00e2k",
                            "gloss": "fear",
                            "script": "\u0628\u0627\u06a9"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "AEF:320",
                    "words": [
                        {
                            "translit": "bhay",
                            "gloss": "to fear",
                            "script": null
                        },
                        {
                            "translit": "bh\u00ee-ma",
                            "gloss": "dreadful",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 4,
                    "parent": 3,
                    "lang": "Persian",
                    "refs": "MON:633",
                    "words": [
                        {
                            "translit": "b\u00eemeh",
                            "gloss": "insurance",
                            "script": "\u0628\u06cc\u0645\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": "IEC:723,1562 links this word to root \"Weid, Woid: to see\"",
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Bhombhos",
                "redirect": "Bamb"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bh\u00f4u, Bheu",
                "lang": "Indo-European",
                "refs": "IEC:98",
                "gloss": "joy, satisfaction"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Persian",
                    "refs": "IEC:98; MON:607",
                    "words": [
                        {
                            "translit": "b\u016dyeh",
                            "gloss": "desire, hope",
                            "script": "\u0628\u0648\u06cc \u06f2 \u060c \u0628\u0648\u06cc\u0647"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0686\u0647 \u062c\u0648\u0631\u0647\u0627 \u06a9\u0647 \u06a9\u0634\u06cc\u062f\u0646\u062f \u0628\u0644\u0628\u0644\u0627\u0646 \u0627\u0632 \u0648\u06cc - \u0628\u0628\u0648\u06cc \u0622\u0646\u06a9\u0647 \u062f\u06af\u0631 \u0646\u0648\u0628\u0647\u0627\u0631 \u0628\u0627\u0632 \u0622\u06cc\u062f",
                        "poet": "H\u00e2fez"
                    }
                },
                {
                    "id": 2,
                    "parent": 0,
                    "lang": "Sanskrit",
                    "refs": "IEC:98",
                    "words": [
                        {
                            "translit": "bh\u00e2vita",
                            "gloss": "well arranged",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                }
            ]
        },
        {
            "root": {
                "name": "Bhr\u00e2-tar",
                "redirect": "Bher 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhr\u00e2-ter",
                "redirect": "Bher 1"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhra-ter",
                "redirect": "Ter 3"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhreg",
                "redirect": "Bhereg"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhrei",
                "redirect": "Bher 3"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhreu",
                "redirect": "Bher 5"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhru 1",
                "lang": "Indo-European",
                "refs": "POK:172",
                "gloss": "eyebrow, beam, log"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK",
```


### [2026-09-05T14:20:58.759Z] TOOL RESULT

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


## [2026-09-05T14:21:03.614Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-97.json'))\nprint(json.dumps(d['entries'][9],ensure_ascii=False,indent=1))\n\"",
 "description": "Print entry 9"
}
```


### [2026-09-05T14:21:05.374Z] TOOL RESULT

```
{
 "root": {
  "name": "Bhru 1",
  "lang": "Indo-European",
  "refs": "POK:172",
  "gloss": "eyebrow, beam, log"
 },
 "nodes": [
  {
   "id": 1,
   "parent": 0,
   "lang": "Avestan",
   "refs": "POK",
   "words": [
    {
     "translit": "brvat",
     "gloss": "brow",
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
   "refs": "BQT:80",
   "words": [
    {
     "translit": "brŭk",
     "gloss": null,
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
   "refs": "POK:172; BQT:80; FSF:81",
   "words": [
    {
     "translit": "abrŭ, borŭ",
     "gloss": "eyebrow",
     "script": "ابرو ، بُرو"
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": {
    "text": "سیاوش زگفت گروی زره - بُروکرد پرچین ، رخان پرگره",
    "poet": "Ferdowsî"
   }
  },
  {
   "id": 4,
   "parent": 0,
   "lang": "Germanic",
   "refs": "AHD",
   "words": [
    {
     "translit": "brus",
     "gloss": "eyebrow",
     "script": null
    }
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
    {
     "translit": "brow, eyebrow",
     "gloss": null,
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 6,
   "parent": 0,
   "lang": "Germanic",
   "refs": "AHD",
   "words": [
    {
     "translit": "brugjô",
     "gloss": "wooden bridge",
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  },
  {
   "id": 7,
   "parent": 6,
   "lang": "English",
   "refs": null,
   "words": [
    {
     "translit": "bridge",
     "gloss": null,
     "script": null
    }
   ],
   "script_extra": null,
   "note": null,
   "quote": null
  }
 ]
}
```


## [2026-09-05T14:21:05.998Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','AEF','MON','BQT','HRN','FSF','AHD','WLD','SYN','BRT','PHD','NYB','HUB','ARY','KLN','SKT','IRN']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:400] if v else 'MISSING')\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-05T14:21:08.435Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I

AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158

IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/n
```


## [2026-09-05T14:21:14.041Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','IEC','FSF','BQT','AHD','ARY','WLD']:\n    print(k, json.dumps(d[k],ensure_ascii=False,indent=1))\n    print()\n\"",
 "description": "Full ref info for key sources"
}
```


## [2026-09-05T14:21:14.378Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls data/verification/page-9*.json data/verification/page-6*.json 2>/dev/null | head -20",
 "description": "List existing verification pages"
}
```


### [2026-09-05T14:21:15.558Z] TOOL RESULT

```
POK {
 "title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)",
 "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/indogermanisches01pokouoft",
 "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
 "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\\data\\ie\\pokorny&root=config",
 "notes": "Nourai's page numbers are Band I 1959 pages, which match these scans. Band II (1969 index) is at pokorny-indogermanisches-etymologisches-worterbuch-band-ii-1969 (djvu 200). local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt (pp. 1-348), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt (pp. 349-770), /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt (pp. 771-1183); /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt (unpaginated database text with 'Page(s): N' per root)",
 "local_files": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_02.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_03.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_full.txt"
 ],
 "cites": "page number of Pokorny, Indogermanisches etymologisches Wörterbuch, Band I (1959)"
}

IEC {
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

FSF {
 "title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/20220809_20220809_1444",
 "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"
 ],
 "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking",
 "covers_etymology": false,
 "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."
}

BQT {
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

ARY {
 "title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.",
 "kind": "local_scan_ocr",
 "url": "",
 "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"
 ],
 "page_offset": "printed page = pdf page + 1",
 "scans": [
  {
   "file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf",
   "first_printed": 1,
   "last_printed": 546,
   "pdf_offset": -1,
   "lang": "fas+eng",
   "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt"
  }
 ],
 "notes": "Image-only PDF provided by the owner (2026-09-04). Use as an additional modern source alongside Wiktionary/Cheung/Hasandust when judging Persian arrows; cite as ARY:<page>. | full OCR text fas+eng (headwords in Persian and Latin caps), printed = pdf+1 | Latin-only OCR (cleaner for transliterated headwords, root names, Pokorny numbers)"
}

WLD {
 "title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32",
 "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)",
 "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_text.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt"
 ],
 "page_offset": "Band 3: leaf = printed + 6. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> || Band I (WLD_Bd1_pages.txt, 887 leaves): printed = leaf(1-based) − 9 (leaf 801 = p.792). Band II (WLD_Bd2_pages.txt, 720 leaves): printed = leaf − 5 (leaf 701 = p.696).",
 "lookup_hint": "Band 3 is the index (Wortregister by language) - it maps a word to 'Band, page' in vols 1-2, so it can at least confirm that a word is treated at the cited WP volume/page. For the actual entry text, use Pokorny 1959 (POK), whose entries cite 'WP. I 177' etc. and are essentially a revision of WP.",
 "notes": "Tried IA (several queries), Google Books API (quota exceeded / not full view), HathiTrust (blocks automated access, 403). Band 2 (1927) is US public domain; Band 1 (1930) became US PD in 2026, so HathiTrust full view may exist - check manually at https://catalog.hathitrust.org/Search/Home?lookfor=walde+pokorny+vergleichendes. || UPDATE 2026-09: Bände I and II obtained in full from the Digital Library of India scans on archive.org (open, OCR layer in the _text.pdf).",
 "cites": "volume (WLD1 / WLD2) and page of Walde–Pokorny"
}
```


### [2026-09-05T14:21:15.598Z] TOOL RESULT

```
data/verification/page-60.json
data/verification/page-61.json
data/verification/page-62.json
data/verification/page-63.json
data/verification/page-64.json
data/verification/page-65.json
data/verification/page-66.json
data/verification/page-67.json
data/verification/page-68.json
data/verification/page-69.json
data/verification/page-90.json
data/verification/page-91.json
data/verification/page-93.json
```


## [2026-09-05T14:21:19.378Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T14:21:19.415Z] TOOL RESULT

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


## [2026-09-05T14:21:24.122Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"lemma: bh\" POK_full.txt | head -60",
 "description": "Grep POK_full bh- lemmas"
}
```


### [2026-09-05T14:21:24.173Z] TOOL RESULT

```
10238:The assumption of a duplicated Root/ lemma: bhabf^a (b^a-bha) seems to be wrong. 
10965:Root / lemma: bhedh_/(bhedh-i > *b^e6^-r) 
11116:Root / lemma: bheigr"- 
11748:Root / lemma: bhe/-2( > *bhel-(e)-n-) 
14778:Root/ lemma: bh/e-(*bh|ehi-) 
15408:Root / lemma: bhren-to-s
```


## [2026-09-05T14:21:27.497Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 168 169 170 171; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -60; done",
 "description": "Print POK leaves around p.161"
}
```


### [2026-09-05T14:21:29.398Z] TOOL RESULT

```
=== leaf 168 ===
len,    strotzen,    überwallen, fließen',  Erw.  von  bhel-  , (aufblasen),  aufschwellen'.
Gr.  q)Xe{/)(x)  , strotze,  bin   übervoll',    ^Isvg  (*0X7]vg,   dehnstufig),   ephes. 0X€cog  {*Olrjfog)  Beiname  des  Dionysos  als  Vegetationsgottes;  vermutlich^ von  der  Üppigkeit  des  Wuchses  auch  att.  (pXscjq,  jon.  (pXovq  , Schilfgewächs*; q)loLü)    (*cplofia))    , schwelle,    strotze,    bin    in    Blüte',    vft€Qq)XoLog    ,üppig^ wachsend'  oder  ,überaus  saftig',  OXoTog,  OXola  ,Beiname  des  Dionysos  und- der  Köre  als  Vegetationsgottheiten',  wohl  auch  cpXoiög,  (pX6og  , Rinde,  Hülse*  j":
ablautend  cpXvu)   , walle  über,  sprudle,   schwatze;    bin  fruchtreich',    äno- cpXvsiv'  äTtsQsvysad-ai  Hes.  cpXvog  m.  , Geschwätz*,  q)XväS  , Geschwätz,  Possen;' Possenreißer' ;
lit.  blidujuy  bliöviauj  bliduti  , brüllen,  blöken',  bliiivauti  ,brüllen',  lett. blaünu,  bVdvu,  blaut  ds.;  aksl.  bl'ujq,  bthvati  , speien,  erbrechen'  (beruht auf  altem  Präteritalstamm,  vgl.  lit.  bliüvo  aus  idg.  *bhluuä-)]  dazu  viel- leicht auch  apr.  bleushy  , Schilf  (würde  in  der  Bed.  zu  gr.  (pXiwg  stimmenl).
Mit  einer  s-Erw.  nd.  Mustern  , heftig  blasen,  stürmen,  schnauben',  engl. bluster  ,brausen,  lärmen*  und  skr.  bljuzgati  ,mit  Geräusch  strömen,  dummes Zeug  schwatzen';  auch  skr.  blihati  usw.?  (s.  unter  bhlei-s-).
Mit  dentalen  Formantien:  mhd.  blödern  , plaudern'?  (eher  junges Schallwort;  vgl.  Kluge ^^  unter  plaudern)-,  eher  Schweiz,  blöder  ,große Blase  usw.',  blödem  , sprudeln,  wallen',  nhd.  Pluderhosen-,  vielleicht  skr. blütiti  jUngereimt,  unpassend  sprechen',  Berneker  62;  über  ahd.  blät{t)ara ,Blase^  {Hle-drö-)  s.  S.  121;
159
mit  'd'  (ursprgl.  Präsens  bildend?):  g)XvSatü  ,fließe  über,  zerfließe,  werde weich',   q)lvdccQ6g   ,niatschig',   iy,cpXvvdaveiv  ,aufbrechen,   von   Geschwüren*.
£--Er Weiterung  hhleug^-  (vgl.  die  Wzform  hhlegu-):
o-r.  oivö-cpXv^  , weintrunken';  cpXvt.w  , aufwallen,  überwallen,  auch  mit Worten';  cplvytvLg,  cplv-Azaiva  , Blase';  aber  nofi-cpölv^  , Brandblase,  Schild- buckel' bleibt  fern;
lat.  fluö,  -ere,  flüxi,  flüctum,  jünger  flüxum  , fließen,  strömen',  flücUis, •üs  , Strömung,  Woge',  flümen  (*fleugsmen)  , strömendes  Wasser,  Fluß', conflüges
=== leaf 169 ===
  alat.  , Zusammenfluß  zweier  Gewässer',  fluvius  ,Fluß'  (vom  Präs. jluö  aus),  flustra  Nom.  PI.  , Meeresstille'  (*flugstro7n)'
ob  hierher  (mit  Nasalierung)  cjmr.  blyngu  , zornig  werden',  blwng  , zornig',, bret.  blouhi  , tadeln'?
WP.  II  213 f.,  WH.  I  519 f.,  Trautmann  35;  anders  EM.  372.
1.  bhlea-  :  bhlQU- :  bhlü-  ,glänzen',  auch  von  weißem  Hautausschlage  Narben^
Schinn  usw.  Ableitungen  zu  1.  bhel-.
Russ.  blju-sc  ,Efeu'  (Specht  Dekl.  117);  poln.  biysk  (Hhlü-sk-)  ,Blitz'; sorb.  blu-znd  ^Narbe^^  wruss.  blu-znd  ^Webefehler';  lett.  blau-zgaSj  blau-znas,. lit.  blü-zganos  ^Schinn^^  lett.  blü-zga  ^die  sich  ablösende  Haut',  blu-zga ,kleine  Teilchen^  Bohrmehl'  usw.
Specht  Dekl.  117.
Vgl.  die  Parallelbildungen  unter  1.  bhlei-.
2,  bhlea-  :  bblou-  :  bhlü-  ^schwach,  elend'  (wohl  aus  ,geschlagen').
Gr.  g)lavQog,  cpavXog  (beide  dissimil.  aus  *(pXavXog)  ^geringfügige  schlecht'*
got.  blaupian  _,abschaffen'  (eigentl.  ^schwach  machen'),  aisl.  blaudr  ^furcht- sam',  ags.  blead  ,blödee  scheu',  ,mit  jo-Suffix  as.  blödi  , schamhaft',  ahd. blödij  mhd.  bloede  ^zerbrechlich,  zaghaft',  nhd.  blöde;
neben  idg.  *bhl9u-to-  steht  eine  d-Erweiterung  in  aisl.  blautr  ,weichlich,. furchtsam',  ags.  bleat  ,arm,  elend',  mndd.  blöt,  mhd.  blöz  ,bloß',  nhd.  bloß (ahd.  bloß  mit  merkwürdiger  Bedeutung  ,stolz');
Hochstufe  bhleu-  in  ags.  un-bleoh  ,furclitlos'  (Suffix  -ho-),  mit  gramm. Wechsel;  aisl.  bljügr  ,verzagt',  blygd  ,Scham'  {*bleugipo),  ablautend  ahd. blügo  K^Y.,  mhd.  blüc,  5Ziwc  , schüchtern',  ahd.  blügisön,  blüchisön  ,zwei- feln',  ags.  blycgan  (*blugjan)  ,erschrecken'  (trans.);  vgl.  lit.  blükstu,  -äti ,schlaff  werden'.
bh[e)leu-  ist  offenbar  Parallelbildung  zu  5ÄeZew-  , schlagen'.
WP.  n  208  f.,  Hirt  Idg.  Gr.  II  150,  Feist  99,  Specht  Dekl.  133.
bhleu'{k)-,  (-S-)  ,brennen'.  Erw.  von  bhel-  ,glänzen'.
*bhleu-s-  in  gr.  7tSQL-nscpXevaf.i€7'og  nvql  ,vom  Feuer  umlodert',  ircicpXevüe, n^QicpXio)  ,versenge  ringsum';  aisl.  blys  n.  , Flamme',  ags.  blysa  m.  ,Flamme,. Fackel',  mnd.  blüs  , Fackel',  ags.  blyscon  , erröten',  engl,  blush.
160  '
*bhleu-k-  m  mlid.  hliehen  , brennend  leuchten*,  ahd.  hluhhen.
Die  westslaY.  Formen  wie  cech.  hlysUti  , schimmern',  hlyskati  ,glänzeai (neben  aksl.  hhUati  usw.,  s.  u.  *bhleig-)  sind  dagegen  wohl  Umbildun» nach  *lyskati,  poln.  iyskac  , blitzen,  glänzen'  usw.  —  Der  Bed.  nicht  uu« mittelbar  entsprechend,  bzw.  nur  aus  einer  Urb
=== leaf 170 ===
ed.  , glänzen*  zu  recht, fertigen,  vergleicht  Trautmann  GGA.  1911,  245  mit  mhd.  bliehen:  \[^^ hlunkü,  blükti  ,fahl  werden,  die  Farbe  verlieren*.
WP.  II  214.
bble-uo-s  von  lichten  Farben  ,blau,  gelb,  blond',  auch  bbl-uo-s,  bhle-ro-s bblö-rO'S,  Ableitungen  von  der  Wz.  1.  bhel-j  bheh-.
Lat.  flävus  ^goldgelb,  rotgelb,  blond^,  osk.  Flavües  G.  Sg.  ,Flävil^  (aus idg.  *bhl'),  daneben  fulvxis  ,rotgelb,  braungelV  aus  *bhl-uo-s]  flörus  ^flävus^ auch  PN,  aus  *bhlöros  =  gall.  *bläros  (Wartburg),  mir.  blär  ,mit  weißem Stirnfleck,  Fleck,  Feld^,  cymr.  blawr  ,grau^,  daneben  *bhle-ro-  in  mnd. bläre  ,Blässe,  blessige  Kuh^
Ahd.  bläo,  nhd.  blau  (mhd.  blä  auch  ,gelb^),  ags.  *bläw  oder  ^blxw^ aisl.  blär  ,blau^  aus  *bhle-uo-S]   s.  auch  S.  155;
air.  blä  ,gelblich?*^  ist  spätes  ags.  Lw.?  Über  germ.  *bliwa-  ,Blei^ s.  unter  1.  bhlei-.
Lit.  blävaSj  lett.  blävs  ,bläulich,  gelb^  sind  germ.  Lw.
WP.  II  212,  WH.  I  513  f.,  anders  EM  367.
bhleus-  etwa  , schlaff'?
Schwed.   mdartl.   bloslin   , schwächlich*,   norweg.   blyr   ,mild,  lau*,  bleyra , Schwächling,    Feigling',    nhd.    schwäb.    blüsclie{n)    , langsam,    träge*:    lit. apsi-blausti  , verzagen,  traurig  werden*. Vielleicht  zu  bheleu-. WP.  II214.
bhlQido-s   ,licht,   blaß^,   zu   bhlei-  ,glänzen^,  von  einer  erw.  Wzf.  *bhlei-d-.  ■^.
Aksl.   bled^  ,bleich,  blaß^  ==  ags.  blät  ,bleich,  bleifarben^;    ahd.  bleizza  ^'" ,Blässe^    Vielleicht  lit.  blaivas  ,nüchtern^  (wenn  aus  '^blaid-vas]   oder  von der  unerw.  Wz.  bhlei- j  s.  d.),   blaivaüs,  -ytis  ,nüchtern  werden;  sich  auf-   ;%, klären,  vom    Himmelt    Alb.    bZerönj  ,grüne^   von    einem   Adj.    *bTere  aus    £ Hled-re  (e  =  idg.  ai  oder  oi),  bUhure  ,blaß,  bleicht  |
Dazu  wohl  der  illyr.  PN  Blaedarus,
WP.  II  217,  Trautmann  34,  Specht  Dekl.  197.
bhlig-  (:  *bbleig')    ,schlagen,    schmeißen^,    auch    bbligu-    (gr.   kelt.),  aus    # einem  wo-Präsens  *bhllg-uö  zu  deuten.
161
"Vol.  ion.  (pUßu  ^drücke;  quetsche^  
=== leaf 171 ===
(über  d-Ußoj  s.  unter  dhlas-  ^quetschen^); vmr.  hilf  m.  ;,catapult^  pallista'^,  hlifaldcl  ^schnell^;  lat.ßigö,  -ere  ^schlagen, iiscblagen,   zu  Boden   schlagen^   (*bhligö,   oder   allenfalls  mit  durch  fllxi^
ßictun^
veranlaßtem  w- Verlust  aus  *fllguo)]
lett.    hlaizit    ^quetschen,    schmettern,    schlagen^,   6^162^   ^schlagen^;    aksl. blizh    b^^^T>  Adv.  ,nahe^  (eigentl.  ^anstoßend^). ;yp.  II  217,  WH.  I  517,  EM.  369.    Über  russ.  hliznd  s.  unter  1.  bhlM-.
bblök-  ;Woll-  oder  Wergflocke,  Gewebe^?
Lat.  floccus  ^Wollfaser,  Flocke*  (^flöcos)  zu  ahd.  hlaha  f.  ^grobes  Lein- tuch (bes.  zu  Decken  oder  Unterlagen)',  nhd.  Blähe,  Blachej  alt.  dän.  hlaa "\yero*,  Hede^;  jetzt  hlaar  (eig.  PL),  schwed.  blänor,  hlär  ds.,  aschwed. blan    hla  ds.  (germ.  *hlahioö-),  an.  hlceja  {^hlahjön-)  ,Laken,  Bettuch^
WP.  11  217,  WH.  517  f.,  866.
bblos-q-;  -g-  in  Schallworten.
Ir,  blosc,  Gen.  bloisc  ,Lärm^  (bhlosko-)]  vgl.  auch  h'osc  ds.  unter  *bhres-] lit.  blqzgu,  -eti  intr.  ,klappern^,  blqzglnti  ^klappern,  rasselnd WP.  II  218.
bbog-  ^fließendes  Wasser,  Bach'.
Mir.  büal  f.  ,fließendes  Wasser'  (*bhoglä),  büar  m.  ,diarrhoea'  (^bhogro-)] urgerm.  *baJä-,  ahd.  bah,  nhd.  Bach,  neben  Hakja-  in  aisl.  bekkr,  ags. becc  m.  ds.
Mit  Hinblick  auf  ai.  bhatdgd-h,  lit.  bangd  ,Welle'  könnte  an  die  Wz.  bheg- ,zerschlagen,  zerbrechen'^  angeknüpft  werden.
WP.  II  149  f.,  187.
bhtgh'  oder  hhagh-  ,Schlamm,  Sumpft
Mnl.  bagger  m.  ,Schlamm',  daraus  nhd.  baggern  ,den  Schlamm  aus- schöpfen'; russ.  bagnö  ,niedrige,  sumpfige  Stelle',  Öech.  bahno  , Sumpf, Morast',  poln.  bagno  ds.
WP.  II  187,  Petersson  Heterokl.  123  f.
bhöi- :  bhQi'  :  bhi-  (bhiid-)  ,sich  fürchten';  bhoidho-s  ,fürchterlich,  abscheu- lich'. Ai.  bhdyate  ,fürchtet  sich'  (aus  Hhdietai  =  slav.  bojet^),  av.  bayente, byente  ,sie  setzen  in  Furcht',  mpers.  besänd  ,sie  sind  in  Angst'  (uriran. *bai-sk-)',  ai.  bibhki  ,fürchtet  sich',  sek.  zum  ursprünglichen  Perf.  m. Präsensbed.  bibhäya  ,bin  in  Furcht'  (bibhiyät,  bibhltana,  abibhet,  Partiz. bibhlvän  =  av.  biwivä  ,sich  fürchtend');  ai.  bhiyand-h  ,sich  fürchtend'; bhi-h  f.,  bhUi-h  f.  (:  lett.  Inf.  bities)  ,Furcht',  bhlmd-h,  ,furchtbar',  bhitd-h
162
,sich  fürchtend^  erschrocken^^  hhlo-u-h  ,furchtsam^  schüchtern,  feige*^  (wei r  =  idg.   l,  ablautend    mit  lit.    hdiUj   bailüs)-,    npers.    bäk   ,Furcht^  (a^ *bhdyaka-)'j   mit   idg.  Vereinfachung  von  äi   zu  ä  vor  Kons,   hierher  aj^ bhäma-h  etwa  ,Grimm,  Wut',  bhämitd-h  ,grimmig^
Gr.  jtid-TjTiogj  Ttid^cjv  m.  ,Affe
```


## [2026-09-05T14:21:37.699Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==172' POK_01.txt | head -80",
 "description": "Print POK leaf 171 (rest of p.162)"
}
```


## [2026-09-05T14:21:38.508Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 179 180 181; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -70; done",
 "description": "Print POK leaves around p.172"
}
```


### [2026-09-05T14:21:39.137Z] TOOL RESULT

```
(über  d-Ußoj  s.  unter  dhlas-  ^quetschen^); vmr.  hilf  m.  ;,catapult^  pallista'^,  hlifaldcl  ^schnell^;  lat.ßigö,  -ere  ^schlagen, iiscblagen,   zu  Boden   schlagen^   (*bhligö,   oder   allenfalls  mit  durch  fllxi^
ßictun^
veranlaßtem  w- Verlust  aus  *fllguo)]
lett.    hlaizit    ^quetschen,    schmettern,    schlagen^,   6^162^   ^schlagen^;    aksl. blizh    b^^^T>  Adv.  ,nahe^  (eigentl.  ^anstoßend^). ;yp.  II  217,  WH.  I  517,  EM.  369.    Über  russ.  hliznd  s.  unter  1.  bhlM-.
bblök-  ;Woll-  oder  Wergflocke,  Gewebe^?
Lat.  floccus  ^Wollfaser,  Flocke*  (^flöcos)  zu  ahd.  hlaha  f.  ^grobes  Lein- tuch (bes.  zu  Decken  oder  Unterlagen)',  nhd.  Blähe,  Blachej  alt.  dän.  hlaa "\yero*,  Hede^;  jetzt  hlaar  (eig.  PL),  schwed.  blänor,  hlär  ds.,  aschwed. blan    hla  ds.  (germ.  *hlahioö-),  an.  hlceja  {^hlahjön-)  ,Laken,  Bettuch^
WP.  11  217,  WH.  517  f.,  866.
bblos-q-;  -g-  in  Schallworten.
Ir,  blosc,  Gen.  bloisc  ,Lärm^  (bhlosko-)]  vgl.  auch  h'osc  ds.  unter  *bhres-] lit.  blqzgu,  -eti  intr.  ,klappern^,  blqzglnti  ^klappern,  rasselnd WP.  II  218.
bbog-  ^fließendes  Wasser,  Bach'.
Mir.  büal  f.  ,fließendes  Wasser'  (*bhoglä),  büar  m.  ,diarrhoea'  (^bhogro-)] urgerm.  *baJä-,  ahd.  bah,  nhd.  Bach,  neben  Hakja-  in  aisl.  bekkr,  ags. becc  m.  ds.
Mit  Hinblick  auf  ai.  bhatdgd-h,  lit.  bangd  ,Welle'  könnte  an  die  Wz.  bheg- ,zerschlagen,  zerbrechen'^  angeknüpft  werden.
WP.  II  149  f.,  187.
bhtgh'  oder  hhagh-  ,Schlamm,  Sumpft
Mnl.  bagger  m.  ,Schlamm',  daraus  nhd.  baggern  ,den  Schlamm  aus- schöpfen'; russ.  bagnö  ,niedrige,  sumpfige  Stelle',  Öech.  bahno  , Sumpf, Morast',  poln.  bagno  ds.
WP.  II  187,  Petersson  Heterokl.  123  f.
bhöi- :  bhQi'  :  bhi-  (bhiid-)  ,sich  fürchten';  bhoidho-s  ,fürchterlich,  abscheu- lich'. Ai.  bhdyate  ,fürchtet  sich'  (aus  Hhdietai  =  slav.  bojet^),  av.  bayente, byente  ,sie  setzen  in  Furcht',  mpers.  besänd  ,sie  sind  in  Angst'  (uriran. *bai-sk-)',  ai.  bibhki  ,fürchtet  sich',  sek.  zum  ursprünglichen  Perf.  m. Präsensbed.  bibhäya  ,bin  in  Furcht'  (bibhiyät,  bibhltana,  abibhet,  Partiz. bibhlvän  =  av.  biwivä  ,sich  fürchtend');  ai.  bhiyand-h  ,sich  fürchtend'; bhi-h  f.,  bhUi-h  f.  (:  lett.  Inf.  bities)  ,Furcht',  bhlmd-h,  ,furchtbar',  bhitd-h
162
,sich  fürchtend^  erschrocken^^  hhlo-u-h  ,furchtsam^  schüchtern,  feige*^  (wei r  =  idg.   l,  ablautend    mit  lit.    hdiUj   bailüs)-,    npers.    bäk   ,Furcht^  (a^ *bhdyaka-)'j   mit   idg.  Vereinfachung  von  äi   zu  ä  vor  Kons,   hierher  aj^ bhäma-h  etwa  ,Grimm,  Wut',  bhämitd-h  ,grimmig^
Gr.  jtid-TjTiogj  Ttid^cjv  m.  ,Affe
```


### [2026-09-05T14:21:41.402Z] TOOL RESULT

```
=== leaf 179 ===
reu-,  bhreu-d-  m.  ,sprießen,  schwellend
Lat.  friitex,  -icis  m.  ,Staude,  Strauch,  Gesträuch^  beruht  wohl  auf  einem Partiz.  *bhrütös  ,hervorgesprossen^ ;  air.  broth  ,Granne,  Haar^;  hierher das  (Z-Präsens:  mhd.  briezen,  bröz  ,knospen,  schwellen^,  ahd.  mhd.  broz ,Knospe,  Sprosset  Vgl.  1.  bJireu-s-  ,schwellen''',  bhriigJino-  , Zweigt
WP.  II  195,  WH.  I  554.
I»  bbreu-,  bbru-  Erw.  von  bher-  ,mit  scharfem  Werkzeug  schneiden,  ab- schaben usw.',  bes.  germ.  ,zerschlagen,  brechen';  bbrü-no-  (bhrou-no-) ,die  beim  Auskriechen  abgestoßene  Hauf^.
Ai.  bhrü7id-m  ,Embryo'  (nach  der  gesprengten  Eihaut  benannt):
mhd.  briune,  brüne  ,Unterleib,  weibliche  Scham';  ahd.  brödi  ,zerbrech- lich'  (^bhrou-tio-),  aisl.  broma  ,Bruchstück'  (*bhrumön) ;  ein  f-Präsens  in ags.  breodan  ,zerbrechen';  wohl  auf  einem  c^-Präsens  beruht  die  germ. Sippe  von  ags.  breotan  ,zerbrechen',  aisl.  hnöta  ,brechen',  broti  m.  ,Haufen gefällter  Bäume,  Verhau',  braut  f.  ,Weg'  (vgl.  nhd.  Bahn  brechen,  frz. route  aus  rupta),  breyta  (*braiUjan)  ,ändern',  breyskr  ,zerbrechlich,  spröde'; ahd.  bruzi,  bruzzi  , Gebrechlichkeit' ;  aisl.  brytia  =  ags.  bryttian  ,teilen, austeilen';  aisl.  bryti  m.  ,Vorschneider,  d.  i.  der  vornehmste  der  Knechte; Art  Gutsverwalter'  =  agsl.  brytta  m.  , Austeiler'.
Zu  germ.  *breuta7i  vielleicht  auch  air.  fris-brudi  ,weist  zurück'.
Lett.  brauna,  braüna  ,Schorf,  Schuppe,  die  beim  Häuten  oder  Aus- kriechen aus  Hüllen  nachgelassene  Haut,  Eingeweide'  (Grundbed.  ,Ab- schabsel',  vgl.  slav.  bnsngti  ,schaben,  streifen'  unter  bhreu-k-)-^
öech.   brn-ka  (*bhrtin-)  ,Nachgeburt'.    S.  die  Erw.  bhreu-k-,    2.  bhreu-s-.
WP.  n  195 f.,  W.  Schulze  KZ.  50,  259  =  Kl.  Sehr.  216.
170  •
2.  hhreu-,  hhrü-  ^Kante^  scharfer  Rand^
Air.  hrü  ^Rand^  Ufer^^  bruach  ds.  (*brü-öko-); aisl,  brün  ^Kante'^;  wovon   brijna  ;,wetzen%  brfni  ,Wetzstein^:  ags.  mh^l brän  ^scharf ^  (von  Waffen).
Lit.  briaunä  ^Kante^   Rand,   Gesims^  {*bhreuna)j  ablaut.  mit   aisl.  brnri^ Die  Gruppe  ist  von  bher-  ^emporstehen;  Kante^  erweitert. WP.  II  196  f.,  W.  Schulze  KZ.  50,  259  =  Kl.  Sehr.  216.
bhreu-k'  (-k-)  ^streichen,  streifen^;  nur  balto-slav.,  wohl  Erweiterung  voi 1.  blirtu-.    Zum  -k-  vgl.  oben  S.  18  Anm.
Lit.  braukiü  braukiau  braukti  ^wischen,  streichen;  sich  langsam  bew^ gen*;  lett.  bräucu  bräucu  bräukt  ^fahren^;  ablaut.  lit.  brukü  brukaü  briiktt ^Flachs  schwingen,  einzwängen^,  lett.  brukt  ,abbröckeln^,  brucindt  ,ab- reiben,  die  Sense  streichen^;  Iterat.  lit.  braukytij  lett.  braucüt
=== leaf 180 ===
  ,streichen^ (mit  unursprüngl.  Intonation)  und  lit.  brükis  m.  ^Streifen,  Strich*,  lett. brüce  f.  ,Schramme,  Narbe^,  dazu  lit.  brukne^  brukms  f.,  lett.  briiklem f.  , Preiselbeere^;
slav.  Hrusg  *brusiti  (ursprgl.  Iterativ)  in  bulg.  brüsja  (briurtch)  ,ab-^ schütteln,  abschlagen^,  skr.  brusim  brüsltl  , wetzen^,  cech.  brousiti  ds. ' dazu  aksl.  ubrxLST>  ,Schweißtuch'^,  skr.  brüs  (Gen.  brüsa)^  russ.  brus  (Gen. brusa]  meist  brusök)  ,Schleifstein^;  russ.  usw.  brusnika  ,Preiselbeere' (,leicht  abstreifbar^);  ablaut.  r.-ksl.  bnsmiti  ,schaben,  rasieren^,  russ.  brosdU (dial.  brokdt'b),  brösith  .werfen^,  brösnuth  ,Flachs  riffeln^,  bros  ,AbfalF  usw. im  Ablaut  zu  bulg.  briH  ,reibe  ab^  Mit  m  der  Iterativstufe:  aksl.  sirbrysati ,abschaben'^,  brysalo  ,penicillus^
Vielleicht  hierher  skr.-ksl.  bruU  ,Nagel',  bulg.  brut  ds.  als  *brukh,  vgl. zur  Bed.  lit.  brükti  ,mit  Gewalt  hineinstecken^,  zur  Form  lett.  braukts ,Messer  zum  Flachsreinigen*.
Vielleicht  hierher  der  illyr.  VN  Breuci,  PN  Breucus  und  der  gall.  ON Bgsvxö-^ayogy  heute  Brnmath  (Elsaß);  dazu  stellt  Krähe  (Gl.  17,  159)  den illyr.  VN  Bq£vvol  :  Breones  (aus  '^Breuones).
Über  russ.   brykdth  ,ausschlagen^  usw.  s.  Berneker  93.
WP.  II  197,    Trautmann  36  f.,   Pokorny  Urillyrier  119.
J.  hhreu'S'  ,scliwellen;  sprießen*  (vgl.  oben  blireu-).
Air.  brü  f.,  Gen.  bronn  ,Bauch,  Leib^  {Hliriis-ö[n\  :  -?i-os),  bt-üach  ,veu- triosus'  (Hrusäkos),  cymr.  bru  m.  ,venter,  uterus'  (Hhreuso-)',  air.  briiinne ,Brust^  (Hhrusnio-),  acymr.  ncymr.  bronn  f.  ,Brust^,  bret.  bronn,  bron  ds. (Hhrusnä)  in  Ortsnamen  auch  ,runder  HügeP,  mcymr.  brynn,  ncymr. bryn  m.  (Hhrusnio-)  ,Hügel^  (aus  dem  Kelt.  stammt  got.  brunjö  f.  ,(Brust)-
171
üaiize^'S  ahd.  briinja,  hriinna  ^Briinne^);  air.  brollach  ^Busen'^  (^bhi-us-lo- ^it  Formans  -äko-);  mir.  brüasach  ,mit  starker,  breiter  Brust'  (von *hhreus-to-  =  as.  briost).
Mhd.  briustern  _,aufschwellen^;  aisl.  ä-brystur  f.  PI.  ^Biestmilch^  (auch Iroddr  ds.  aus  '^bruz-da-z),  Schweiz,  briescht  ds.  (daneben  briesch  ds.  aus *bhreus-ko-):  as
=== leaf 181 ===
.  bi-iost  N.  PL,  ag's.  breost,  aisl.  5?'ios^  ^Brusf^,  schwund- stufig' go^-  brusts  f.  PL,  ahd.  6?*?<5^,  nhd.  Bmist]  as.  brustian  ^knospen^ (slav.  ^bTbsU  Jvnospe^),  nhd.  Brös-chen  (aus  dem  md.)  , Brustdrüse  des Rindes';  schwäb.  Brüste,  bair.  Brilsel,  Briesel,  Bries  ds.,  dän.  brissei, scliwed.  halfbräss,  mit  Ä:-Suffix  dän.  bryske,  engL  brisket  ^Brust  der  Tiere^
AisL  briösk  ^Knorpel^,  mhd.  h-üsche,  nhd.  Brausche  ^Beule^^  nhd.  diaL hrausche,  brauschig  ^turgidus^  wulstig^^  brauscJien  ,aufschwellen^
Russ.  brjücho  ^Unterleib,  Bauch,  Wanst^,  diaL  brjüchnuth  , weichen, quellen,  anschwellen^,  cech.  alt.  brück,  bfucho,  heute  brich,  bficho  ,Bauch* usw.  {*bhreuso-s,  -m);
hierher  auch  klr.  brost'  f.  dial.  brost  m.  ,Knospe',  hulg-.  b')i,s(t)  m. jjüngere  Sprossen'^,  skr.  brst  m.  ds.,  bi'stina  ,Laub^
WP.  II  197 f.,  Feist  107  f.,  108  f.
2.  bhreu-s-  ,zerbrechen,  zerschlagen^  zerkrümeln  u.  dgV,  Erw.  von  1.  bhrmi-.
Alb.  breshen,  bresher  ,HageP,  wenn  eig-.  ,Kürnchen,  mica^  (^  =  i^^o-  ^'0? lat.  frustum  ,ein  Brocken,  Stückchen,  Bissen^  (aus  *bhrus-to-)'^
air.  brau  , zerschmettere,  zerschlage^  {*bhrüsiö,  gall.  brus-,  frz.  bruiser),  mir. brüire,  brüile  , Bruchstück^,  bruan  ds.,  bruar  ,Bruchstücke^,  brosna  (*brus- tonio-)  ,Reisig'bündeF,  galL  *bruskiä  ,Gestrüpp',  afrz.  broce  ds.,  mir.  brusc ,Krümchen*  usw.;  air.  bronnaim  ,schädig"e^  (*bhrusnämi)  (Subjunktiv  robria von  *bris-  ,brechen^  entlehnt,  s.  unter  bhrei-)]  mcymr.  breu,  ncymr.  brau jgebrechlich^,  mcorn.  bre^o  ,g*ebrochen^  (*bhrönso-)]  mbret.  briisun  ,Krüm- chen^  (*brous-t-)]
ags.  briesan  (^brausjan),  brysan  (*brüsjan)  ,zerbrechen  trans.,  zerschlagen^, engl,  bruise  ,quetschen^,  wahrscheinlich  auch  ahd.  brösma,  mhd.  brösem, bröseme,   brösme  ,Brosame,  Krume,  Bröckchen^;   ags.   brosnian   ,zerfallen^
WP.  II  198  f.,  WH.  I  553.
3.  bhreus-,  bhrüs-  ,brausen,  wallen,  rauschen,  hervorquellen  oder  -sprießen,
sich  bauschen,  Büschel,  Gestrüpp  u.  dgl.^,  besonders  in  germ.  Worten;
vielleicht  zu  1.  bhreu-s-]  auch  eine  jüngere  Schallvorstellung  (ähnlich
skr.  brüjim,  brujiti  ,summen,  von  einer  Menge  Bienen^,  Berneker  89)
kann  mitgewirkt  haben. Mhd.  briisen  , brausen',  brüs  ,das  Brausen^  ndd.  brüsen,  ,brausen,  sieden; eihg    sein    (von    Menschen);    sich   ausbreiten,   neue   Triebe   machen   (von Pflanzen);   besprengen,  bespritzen'    (vgl.  nhd.  Brause)  (daraus   dän.  bruse
172  9
ds.),  ndl.  bruisen,  früher  bruischen  ,scliäumen^  brausen',
```


## [2026-09-05T14:21:49.006Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"bhrü-\\|bhru-\\|brvat\\|Braue\\|hhrü\" POK_01.txt | sed -n 1,40p",
 "description": "Grep POK for bhru root"
}
```


### [2026-09-05T14:21:49.063Z] TOOL RESULT

```
1858:Specht  will  auch  (Dekl.  148),  mit  i-  und  it-Formans,  ags.  bri-d,  birci ,junger  Vogel',  germ.  brü-tis  ,Frau,  Braut',  ai.  bhimnd-  , Embryo',  lett. braüna,  Öech.  brnka  {*bhru-nka)  ,Nachgeburt'  hierherstellen.  S.  aber  unter bh(e)reu-  , quellen'.
1916:5.  bher-  ^glänzend,  hellbraun^:  bhero-s,  bberu-s,  vielfach  von  brauneu Tieren;  redupl.  bhe-btru-s,  bhe-bhro-s  ,braun;  Biber^;  flo-Bildun- gen :  bhre-no-,  bhro-no-  und  (*bheru-s :)  bhrou-no-,  bhrü-no. ,braun^.
1920:ai.  babhrü-h  ^rotbraun;  große  Ichneumonart',  av.  baivra-,  baicri-  ,Biber'; lat.  fiber,  fibrl  ,Biber'  (auch  feber  s.  WH.  I  491;  wohl  i  geneuert  für  e, wie  auch)  kelt.  (nur  in  Namen):  *bibros,  *bibrus  in  gall.  ON  und FIN  Bibracte,  abrit.  VN  Bibroci^  mir.  VN  Bibraige  (*bibru-rigion),  PN Bibar  {*Bibrus)  neben  *bebros  in  gall.  FIN  *Bebrä,  frz.  Bievre]  Bebromiäj frz.  Beuvo'onne,  Brevenne  usw. ;  ahd.  bibar j  ags.  beofor  (ältest  bebr),  mnd. bever,  aisl.  biörr  ds.  (urg.  *SeSrw-);  vgl.  auch  nhd.  FIN  Bever,  alt  Biverna-,
1999:mit  Formans  -uo-  got.  brafv  in  in  braJva  augins  ^iv  Qiit^  dq)&aXfiov,  im Augenblick'  (vgl.  aisl.  augnabragd  n.  , Augenblick,  Zwinkern  mit  den Augen')  und  dehnstufiges  *brihwa,  *bre^wä  in  aisl.  brä  f.  , Wimper',  agg^ bräewj  breaw,  breg  m.  , Augenlid',  as.  bräha  , Augenbraue',  slegi-bräwa , Augenlid',  ahd.  bräwa  f.  ,Braue',  loint-präwa  ,Wimper'  (die  Bed.  , Braue' von  *bra-  , Braue',  idg.  *bhra-,  bezogen);  daß  trotz  Schwyzer  Gr.  Gr.  I. 350,  463^  und  Specht  Dekl.  83,  162  ahd.  bräwa  nicht  auf  Hhreuä  zurück- gehen kann,  wird  durch  den  grammat.  Wechsel  im  Ags.  bewiesen,  der eine  Form  mit  -ku-  voraussetzt  (Sievers-Brunner  200).
2033:bh{e)reu-  :  bh(e)rU-,  Erw.  von  2.  bher-  ,sich  heftig  bewegen,  wallen,  bes.  vom Aufbrausen  beim  Gären,  Brauen,  Kochen  usw.' A.  Ablautstufen  bheru-  (bheru-),  bhr^-:
2464:2.  hhreu-,  hhrü-  ^Kante^  scharfer  Rand^
2501:Ai.  bh'ü-h  f.,  Akk.  bhrüv-am  ,Braue',  aA^  brvat-  f.  (Du.)  ,Brauene  npers.  T ehm,  brü  ds.  (Hübschmann  lA.   10,  24);
2502:gr.  öq)Qvg,  -vog  f.  ,Braue',  übertragen  .erhöhter  Rand,  Hügelrand*  (nach  | Meillet  BSL  27,  129 f.  mit  griech.  Vokalprothese?);
2503:maked.  dßQOvreg  ,dcpQveg'  (von  Kretschmer  Einl.  287  in  äßqovfeg  geän- dert; von  Meillet,  s.  Boisacq  733  Anm.  3,  wegen  der  anderweitig  bezeugten Form  äßqoxeg  und  wegen  av.  brvat-  festgehalten);
2504:mir.  brüad  Gen.   Du.,  bräi,  bröi  Nom.  Du.  f.  ,Brauen'  (zum  Diphthong  W s.  Thurneysen  Grammar  199),  air.  forbru  Akk.  PL  (*bhrüns  :  Akk.  ö(pQvg)f  M fm^brü  Gen.  PL  ,supercilia';    unklar  sind  mir.  PL   abrait  (*abrant-es  oder  -^' *abranti)  , Augenlider,    Brauen',   desgleichen    mbr.    abrant   ,Braue',    cjmr.    ^ amrant  ,Augenlid',  die  Specht  (Dekl.  83,  162)  zu  lat.  fröns  ,Stirn'  stellen möchte;  aber  Vokalismus  und  Bedeutung  weichen  ab;
2507:lit.  hruvis  m.  ,Braue^,  zem.  auch  h-unes  PL,  apr.  xüiihri  f.  ,Wimper^  (scheint Umstellung  aus  Hruiui);
2508:^\)cr,  bnvh  (ursprünglicher  Nom.  *bry,  wie  kry  :  kr^v^)^  skr.-ksl.  obvhiih, skr.  obwa  usw.  ^Braue^
2512:2.  hhrü'f  bhreu-  ,Balken,  Prügel^;*  auch  als  Übergang  über  ein  Gewässer: ,Brücke^
2516:Unklar  ist  der  Guttural  in  den  germ.  Formen:  *brugi-  aus  Hruui-, oder  k-  Suffix?  S.  Kluge^i  unter  ^Brücke'  und  Specht  Dekl.  2113  f^^  ^er Zusammenhang  mit  1.  bhrü-  annimmt.
```


## [2026-09-05T14:21:52.069Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 2495,2525p POK_01.txt",
 "description": "Print POK bhru entry context"
}
```


### [2026-09-05T14:21:52.116Z] TOOL RESULT

```
Mit  germ.  Hruska-z  ,GestrüppS  Hruskan  ,knistern'  {-sk-  kann  idg.  z^ sein)  vergleicht  man  die  baltoslav.  Gruppen  lit.  bruzgai  PI.  ,Gestrüppf briauzgä  ,Schwätzer',  bruzgii,  4ti  ,rascheln',  russ.  brjuzgdju,  -dth  ,murmeln< brjuzzdth  ,brummen,  murren,  knurren'  usw.;  doch  sind  die  Verba  vielleichj eine  erst  baltoslav.  Schallbildung.  Wegen  der  germ.  Bed.  ,spritzen'  is vielleicht  andererseits  russ.  bryzgaju,  -ath  ,spritzen,  sprühen'  usw.  zu' vergleichen.
WP.  II  199  f.,  Trautmann  38.
bbroisqo-,  bhrisqo-  ,herb  von  Geschmack'.
Russ.-ksl.  obrezgnuti,  obrhzgnuti  ,sauer  werden',  cech.  bresk  ,herber  Ge-^^ schmack',  poln.  brzazg  ,unangenehmer,  herber  Geschmack;  üble  LauneVgl^ russ.  brezgdth  (alt  brezgati)  ,sich  ekeln' ;  zunächst  zu  norw.  bj^isk  ,bitterer  ^^: Geschmack',  brisken  ,bitter,  herbe';  wohl  zu  bhrei-  ,schneiden'  (wie  mndl.  Ji; brine  ,Salzwasser').  V.
WP.  II  206.
j.  bhrü'  , Augenbraue',  z.  T.  mit  anlautendem  Vokal,  idg.  o-  oder  a-  (vollere  v Wurzelform?);  nach  Persson  Beitr.  17  liegt  ein  verdunkeltes  Kompo-J^; sitionsglied  "^oku-  ,Auge'  (mit  Kons.-Assimilation)  vor.  y'
Ai.  bh'ü-h  f.,  Akk.  bhrüv-am  ,Braue',  aA^  brvat-  f.  (Du.)  ,Brauene  npers.  T ehm,  brü  ds.  (Hübschmann  lA.   10,  24);
gr.  öq)Qvg,  -vog  f.  ,Braue',  übertragen  .erhöhter  Rand,  Hügelrand*  (nach  | Meillet  BSL  27,  129 f.  mit  griech.  Vokalprothese?);
maked.  dßQOvreg  ,dcpQveg'  (von  Kretschmer  Einl.  287  in  äßqovfeg  geän- dert; von  Meillet,  s.  Boisacq  733  Anm.  3,  wegen  der  anderweitig  bezeugten Form  äßqoxeg  und  wegen  av.  brvat-  festgehalten);
mir.  brüad  Gen.   Du.,  bräi,  bröi  Nom.  Du.  f.  ,Brauen'  (zum  Diphthong  W s.  Thurneysen  Grammar  199),  air.  forbru  Akk.  PL  (*bhrüns  :  Akk.  ö(pQvg)f  M fm^brü  Gen.  PL  ,supercilia';    unklar  sind  mir.  PL   abrait  (*abrant-es  oder  -^' *abranti)  , Augenlider,    Brauen',   desgleichen    mbr.    abrant   ,Braue',    cjmr.    ^ amrant  ,Augenlid',  die  Specht  (Dekl.  83,  162)  zu  lat.  fröns  ,Stirn'  stellen möchte;  aber  Vokalismus  und  Bedeutung  weichen  ab;
173
^trs.  hrü,  aisl.  hrürij  PL  brynn  ^B^-aue^  (kons.  St.,  aus  *brutoün-,  vgl. *ULiuiün,  tungo,  kontrahiert  und  dadurch  zur  flexivischen  Sonderentwicklung geUaügt).
lit.  hruvis  m.  ,Braue^,  zem.  auch  h-unes  PL,  apr.  xüiihri  f.  ,Wimper^  (scheint Umstellung  aus  Hruiui);
^\)cr,  bnvh  (ursprünglicher  Nom.  *bry,  wie  kry  :  kr^v^)^  skr.-ksl.  obvhiih, skr.  obwa  usw.  ^Braue^
Kine  e-Abl.  bkriie-  mit  silbisch  gewordenem  r  sieht  Trautmann  KZ.  44, 223  in  lit.  birwe  =  bruvis.
Toch.  A  'pärwän-j  B  pämoäne  (Dual)  ^Augenbrauen^
WP.  11  206  f.,  Trautmann  38.
2.  hhrü'f  bhreu-  ,Balken,  Prügel^;*  auch  als  Übergang  über  ein  Gewässer: ,Brücke^
Aisl.  &rü  f.  ^rücke*;  aisl.  bryggia  , Landungsplatz,  Hafendamm^  ndd. brügge  ds.,  ahd.  brucca^  as.  -bruggia,  ags.  brycg  ,Brücke^,  bair.  Bruch ,Bretterbank  am  Of  en^  ags.  brycgian  ,pflastern^  (ursprgl.  mit  Holzprügeln), Schweiz,  brügi  (ahd.  *brugi)  ,Holzgerüst^,  brügel  ,Holzscheit^,  mhd.  brügel ,Knüttel^,  nhd.  Prügel  (,Brücke^  ist  also  ,Balken;  Knüppelweg^) ;
gall.  briva  ,Brücke^  (Hhreua)]
abg.  br^v^no  ,Balken^,  skr.  brv  f.  ,Balken^  Stegbrücke^  (usw.,  s.  über  die slav.  Formen  Berneker  92).
Unklar  ist  der  Guttural  in  den  germ.  Formen:  *brugi-  aus  Hruui-, oder  k-  Suffix?  S.  Kluge^i  unter  ^Brücke'  und  Specht  Dekl.  2113  f^^  ^er Zusammenhang  mit  1.  bhrü-  annimmt.
WP.  II  207.
bhrüg-  ,Frucht;   genießen,  gebrauchen^,  vielleicht  ältest  ,sich  Früchte  zum
Genüsse  abbrechen  oder  abstreifen^  und  dann  zu  *bhreu-   ,schneiden'
(vgl.  dort  zur  Bed.  ai.  bhdrvati  ,kaut,  verzehrt^,   auch  bsl.   *bhreu-q-,
-k-  ^darüberstreifen,  abbröckeln').
Lat.  früx,  -gis  f.  ,Fruchf  ==  umbr.  Akk.  PL  frif^fri  ,fragesS  \^i.  frügl
(Dat.  *,zum  Gebrauche^  =)  ,tauglich^,  fruorj  -i,  früctus  und  fruitus  siim
.genieße'^   (aus  *früguor,   das  für  *frügor   eingetreten   ist?),  früniscor  _,ge-
nieße'  {^früg-nlscoi^,  frümentum  ^Getreide',  osk.  fruktatiuf  (^frügetätiöns)
```


## [2026-09-05T14:22:37.906Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD bhru ===\"; grep -n -A12 \"^bhru-\\|^bhrū-\\|bhru- *$\" AHD_watkins1985.txt | head -40; echo \"=== AHD bhei / bheia ===\"; grep -n -B2 -A10 \"BOGY\\|bhoi-\\|bheia-\\|bhei-\" AHD_watkins1985.txt | head -60",
 "description": "Grep AHD Watkins for bhru and bhei"
}
```


### [2026-09-05T14:22:40.598Z] TOOL RESULT

```
=== AHD bhru ===
=== AHD bhei / bheia ===
146-XX
147-LING (storo-), and, at least in some dialects, the SPARROW (sper-’), FINCH (sping-), and woodpecker ((s)peik-). The generic term for “bird” was awi- (Latin avis), and from this was derived the well-represented word for egg, *dOwyo-.
148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic lan- guages have innovated, perhaps from a taboo on speaking the name while gathering wild honey; the common Germanic English word HONEY is from an old color adjective for “yellow,” k(e)neko-.
149-The Indo-Europeans were clearly also troubled by more “personal” insect pests. A root sker-' is the base of a word “kori-, attested in different languages as either “bedbug” or “moth.” English nit faithfully continues Indo-European knid-, “louse, louse egg,” attested in many branches of the fam- ily. And lds-, “louse,” has rhymed with mus-, “mouse,” since Indo-European times.
150-Man and Society. For man himself, a number of terms were employed, with differ- ent nuances of meaning. The general terms for “man” and “woman” are wi-ro- (VIRILE) and *g”end- from g’en- (GYNECOLOGY). For man as a human being, the oldest word was apparently *manu- (man-'), as preserved in English MAN and in Slavic and Sanskrit. In other dialects we find interesting metaphori- cal expressions, which attest a set of religious concepts opposing the gods as immortal and celestial to mankind as mortal and terres- trial. Man is either *mortos, “mortal” (mer-2, “to die’), or *dhghomyo-, ‘“‘earthling”’ (dhghem-, “earth”).
151-The parts of the body belong to the basic layer of vocabulary and are for the most part faithfully preserved in Indo-European lan- guages. Such are ker-', “head” (also kaput in dialects, doubtless a more colloquial word), genu-?, “chin, jaw,” dent-, “tooth,” ok"-, “to see,” whence “eye,” ous-, “ear,” nas-, “nose,” leb-?, “lip,” bhrd-, “brow,” 6s-, “mouth,”
152-dngha, “tongue,” and mon-, “neck.” The word for “foot”? is attested everywhere (ped-'), while that for the hand differs ac- cording to dialect.
153-Internal organs were also named in Indo- European times, including the womb (g“elbh-), gall (ghel-?), brain (mregh-mno-, confined to Low German and Greek), spleen (spelgh-), and liver (yekr). The male sexual organs, pes- and ergh-, are common patri- mony, as is ors-, “backside.”
154-A large number of kinship terms have been reconstructed. They are agreed in pointing to a society that was patriarchal, patrilocal (the bride leaving her household to join that of her husband’s family), and patrilineal (de- scent reckoned by the male line). “Father” and “head of the household” are one: peter-, with his spouse, the mater-. These terms are ultimately derived from the baby-talk sylla- bles pa(pa) and ma(ma), but they had a socio- logical significance in the Indo-European family over and above this, which is marked by the kinship-term suffix -ter-. Related terms are found for the grandfather (awo-) and the maternal uncle (*awon-), and corre- spondingly the term nepét- (feminine *nepti-) applied to both grandson (perhaps originally daughter’s son) and nephew (sis- ter’s son). English soON and DAUGHTER clearly reflect Indo-European *siénu- (from seue-') and dhughater-.
155-Male blood relations were designated as bhrater- (BROTHER), which doubtless ex- tended beyond those with a common father or mother; the Greek cognate means “fellow member of a clan-like group.” The female counterpart was swesor- (SISTER), probably literally “the female member of the kin group,” with a feminine suffix *-sor- and the root s(w)e-, designating the self, one’s own group.
156-While there exist many special terms for relatives by marriage on the husband’s side, like daiwer-, “husband’s brother,” fewer cor- responding terms on the wife’s side can be reconstructed for the protolanguage. The terms vary from dialect to dialect, providing good evidence for the patrilocal character of marriage.
157-The root deme-' denoted both the house (Latin domus) and the household as a social unit. The father of the family (Latin pater familias) was the “master of the house” (Greek despotes) or simply “he of the house” (Latin dominus). A larger unit was the vil- lage, designated by the word weik-'. The
158-Xxi
--
323-outlaw”), in: a. Old English bannan, to summon, pro- claim, and Old Norse banna, to prohibit, curse: BAN}; b. Old French ban, feudal jurisdiction, summons to military service, proclamation, Old French bandon, power, and Old English gebann, proclamation: BANAL, BANNS; ABANDON; C. Old French banir, to banish: BAN- ISH; d. Late Latin bannus, bannum, proclamation: Ccon- TRABAND; @. Italian bandire, to muster, band together (< “to have been summoned”): BANDIT. 4. Suffixed form *bha-ni in Germanic *b6dni- in Old Norse b6n, prayer, request: BOON!. 5. Suffixed form *bhd-ma in: a. Latin fama, talk, reputation, fame: FAME, FAMOUS; DEFAME, INFAMOUS; b. Greek phémé, saying, speech: EUPHEMISM. 6. Suffixed o-grade form *bhd-nd in Greek phéné, voice, sound, and phénein, to speak: PHONE, -PHONE, PHO- NEME, PHONETIC, PHONO-, -PHONY; ANTHEM, (ANTI- PHON), APHONIA, CACOPHONOUS, EUPHONY, SYMPHONY. 7. Suffixed zero-grade form *bha-to- in Latin fatéri, to acknowledge, admit: CONFESS, PROFESS. 8. Greek blas- phémos, evil-speaking, blasphemous (first element ob- scure): (BLAME), (BLASPHEME), BLASPHEMOUS. [Pok. 2. bha- 105.] bha-bha-. Broad bean. 1. Latin faba, broad bean: FAVA BEAN. 2. Variant form *bha-un- in Germanic *bauné in Old English béan, broad bean, bean of any kind: BEAN. [Pok. bhabhé 106.] bhad-. Good. 1. Germanic (comparative) *batiz6 in Old English betera, better: BETTER. 2. Germanic (superla- tive) *batistaz in Old English bet(e)st, best: BEST. 3. Ger- manic noun *b6¢6 in Old English bét, remedy, aid: BooT?. 4. Germanic verb *batnan, to become better, in Old Norse batna, to improve: BATTEN!. [Pok. bhdd- 106.] bhag-'. To share out, apportion, also to get a share. 1. Greek phagein, to eat (< “to have a share of food”): -PHAGE, -PHAGIA, PHAGO-, -PHAGOUS. 2. Extended form *bhags- in Avestan bakhsh- in Persian bakhshidan, to give: BAKSHEESH, (BUCKSHEE). [Pok. 1. bhag- 107.] bhag-. Sharp. Suffixed form *bhag-ro- in Greek phag- ros, whetstone, also a name for the sea bream: PORGY. [Pok. 2. bhag- 107.] bhaghu-. Arm. Germanic *bdguz in Old English bdg, boh, bough: BouGu. [Pok. bhdghii-s 108.] bhago-. Beech tree. 1. Germanic *b6k6, beech, also “beech staff for carving runes on” (an early Germanic graphic device), in: a. Old English bdc, written docu- ment, composition: BOOK; b. Middle Dutch boek, beech: BUCKWHEAT. 2. Germanic *bdkjdn- in Old English béce, beech: BEECH. [Pok. bhdgo-s 107.] bhar-. Also bhor-. Projection, bristle, point. 1. Suffixed o-grade form *bhor-so- in Germanic *barsaz in Old English bzrs, perch, bass (a fish that has a spiny dorsal fin): BASs!. 2. Suffixed zero-grade form *bhAr-sti- in Germanic *bursti- in Old English byrst (> Middle Eng- lish bristel), bristle: BRISTLE. 3. Extended zero-grade form *bhrs- in: a. Germanic *bur- in Swedish borre, bur, perhaps akin to the Scandinavian source of Middle English burre, bur: BUR}; b. suffixed form *bhrs-dh- in Germanic *bruzd-, point, needle, in Old Norse broddr, spike: BRAD; C. suffixed form *bhrs-ti- in Latin fastig- ium, summit, top, extremity: FASTIGIATE, FASTIGIUM; d. possibly suffixed form *bhrs-tu- in Latin fastus, fasti- dium, disdain (from the notion of prickliness): FASTIDI- ous; e. suffixed form *bhrs-tio- in Russian borshch, cow parsley: BORSCHT. [Pok. bhar- 108.] bhardha. Beard. Possibly related to bhar-. 1. Germanic *bardaz in Old English beard, beard: BEARD. 2. Ger- manic *bard6, beard, also hatchet, broadax (the associ- ation of beard and ax is attested elsewhere in the Indo-European family; both were symbols of patriarchal authority), in Old High German barta, beard, ax: HAL- BERD. 3. Latin barba, beard: BARB!, BARBEL, BARBEL- LATE, BARBER, BARBETTE, BARBICEL, BARBULE; REBARBATIVE. [Pok. bhardhé 110.] bhares-. Also bhars-. Barley. 1. Germanic *barz- in Old
324-bhasko-
325:English bere, bere, berlic, barley: BARLEY; BARN. 2. Latin far (stem farr-), spelt, grain: FARINA, (FARINA- CEOUS), FARRAGINOUS, FARRAGO. [Pok. bhares- 111.] bhasko-. Band, bundle. 1. Latin fascis, bundle (as of rods, twigs, or straw), also crowd of people: FASCES, FASCICLE, FASCINE, FASCISM. 2. Latin fascia, band, fillet, bandage: FASCIA, FESS. 3. Probably Latin fascinum, fascinus, an amulet in the shape of a phallus, hence a bewitching: FASCINATE. [Pok. bhasko- 111.] bhau-. To strike. 1. Germanic *bautan in: a. Old English béatan, to beat: BEAT; b. German bosseln, to do odd jobs: BUSHEL?. 2. Germanic *bautilaz, hammer, in Old English bietel, hammer, mallet: BEETLE’. 3. Germanic “bitaz in Old English diminutive buttuc, end, strip of land: BUTTOCK. 4. Germanic *butt-, name for a flatfish, in Middle Dutch butte, flatfish: HALIBUT. 5. Germanic *buttan in Old French bo(u)ter, to strike, push (> French bouton, button): BOUTON, BUTT!, BUTTON, BUTTRESS; ABUT, REBUT, SACKBUT. 6. Variant form *bhit- in: a. Latin confiitdre, to check, suppress, restrain (com-, intensive prefix; see kom): CONFUTE; b. Latin refiitdre, to drive back, rebut (re-, back; see re-): REFUTE. [Pok. 1. bhau- 112.] bhé-. To warm. Contracted from *bheo. 1. Suffixed zero-grade form *bha-to- in Germanic *batham in Old English beth, a bath, and its denominative bathian, to bathe: BATH!, BATHE. 2. Suffixed zero-grade form *bha-g- in: a. Germanic *bakan in Old English bacan, to bake: BAKE; b. Germanic *bakkan in German backen, to bake: ZWIEBACK. [Pok. bhé- 113.] bhedh-. To dig. 1. Germanic *badjam, garden plot, also sleeping place, in Old English bed(d), bed: BED. 2. O-grade form *bhodh- in: a. Latin fodere, to dig: FOSSA, (FOSSE), FOSSIL, FOSSORIAL; b. perhaps Greek bothros, pit: BOTHRIUM. [Pok. 1. bhedh- 113.] bheg-. To break. Akin to bhreg-. Possibly in various Germanic forms. 1. Germanic nasalized form *bang- in: a. Old Norse banga, a hammering, akin to the probable Scandinavian source of English BANG!; b. Swedish dia- lectal bangla, to work inefficiently, akin to the possible Scandinavian source of English BUNGLE. 2. Possibly Germanic nasalized forms *bankiz and *bank6én-, bank of earth (possibly < “feature where the contour of the ground is broken,” escarpment, riverbank, possibly also associated with “manmade earthwork’’), later also bench, table, in: a. Old English benc, bench: BENCH; b. Old Danish banke, sandbank, akin to the Scandinavian source of BANK}; c. Old High German banc, bank, bench, moneychanger’s table (> Italian banca): BANK?, BANT- LING, BUNCO; BANKRUPT; d. Old French banc, bench: BANK, BANQUET; @. Provencal banca, bench: BAN- QUETTE. [Pok. bheg- 115.] bhegr-. To run away. 1. Germanic *bakjaz, a stream, in Old Norse bekkr, a stream: BECK?. 2. Greek phebesthai, to flee in terror, forming phobos, panic, flight, fear: -PHOBE, -PHOBIA. [Pok. bhegy- 116.] bhei-'. A bee. Germanic suffixed form *bidn- in Old English 6é0, a bee: BEE}. [Pok. bhei- 116.] bhei-2. To strike. 1. Germanic suffixed form *bili- in Old English bile, bird’s beak: BILL?. 2. Germanic suffixed form *bilja- in Old English bil), sharp weapon: BILL’. [Pok. bhei(a)- 117.] bheid-. To split; with Germanic derivatives referring to biting (hence also to eating and to hunting) and wood- working. 1. Germanic *bitan in Old English *bitan, to bite: BEETLE!, BITE. 2. Zero-grade form *bhid- in: a. Ger- manic *bitiz in Old English bite, a bite, sting: B1T?; b. Germanic *bitén- in Old English bita, a piece bitten off, morsel: BIT!; c. Suffixed form *bhid-ro- in Old English bit(tjer, ‘‘biting,’’ sharp, bitter: BITTER. 3. O-grade form *bhoid- in Germanic *baitjan in: a. Old Norse beita (verb), to hunt with dogs, and beita (noun), pasture, food: BAIT!; b. Old French beter, to harass with dogs: ABET. 4. Germanic *bait-, a boat (< “dugout
326-bhel-?
327-canoe” or “split planking”), in Old English baz, boat, and Old Norse bdtr, boat: BATEAU, BOAT; (BOATSWAIN). 5. Nasalized zero-grade form *bhi-n-d- in Latin findere (past participle fissus), to split: -FID, FISSI-, (FISSILE), FISSION, (FISSURE). [Pok. bheid- 116.]
328-bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheidh- 117.] bheig-. To shine. An uncertain but plausible root. Greek phoibos, shining: PHOEBE, PHOEBUS. [Pok. bheigz- 118.] bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English blen- can, to deceive: BLENCH!; b. Old French blanc, white: BLANCH, BLANK, BLANKET; BLANCMANGE. 7. *blisk-, to shine, burn, in Old English blyscan, to glow red: BLUSH. IV. Extended form *bhleg-, to shine, flash, burn. 1. Ger- manic *blakaz, burned, in Old English blxc, black: BLACK. 2. Zero-grade form *bhig- in: a. Latin fulgére, to flash, shine: FULGENT, FULGURATE; EFFULGENT, FOU- DROYANT, REFULGENT; b. Latin fulmen (< “fulg-men), lightning, thunderbolt: FULMINATE. 3. a. Latin flagrdre, to blaze: FLAGRANT; CONFLAGRANT, CONFLAGRATION, DEFLAGRATE; b. Latin flamma (< *flag-ma), a flame: FLAMBE, FLAMBEAU, FLAMBOYANT, FLAME, FLAMINGO, FLAMMABLE; INFLAME. 4. Greek phiegein, to burn: PHLEGM, PHLEGMATIC, PHLEGETHON. 5. Greek phlox, a flame, also a wallflower: PHLOGISTON, PHLOX; PHLOGO- PITE. [Pok. 1. bhel- 118, bheleg- 124, bhleu-(k)- 159.] bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC.
329-bhel-*
330-3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
331-bherag-
332-grade form *bhndh- in Germanic *bund- in: a. Middle High German bunt, league: BUND?; b. Middle Dutch bondel, sheaf of papers, bundle: BUNDLE. 4. Suffixed form *bhendh-na-, “tied structure” (as of wicker), in Celtic *benna, manger, in Old English binn(e), manger: BIN. 5. Persian band, band, bandage, also a river levee: BUND!; CUMMERBUND. 6. Sanskrit badhndti (Sanskrit root bandh-), he ties: BANDANNA. [Pok. bhendh- 127.] bhengh-. Thick, fat. Extended zero-grade form *bhnghu- in Greek pakhus, thick, fat: PACHYDERM, PACHYSANDRA. [Pok. bhengh- 127.]
333-bher-1. To carry; also to bear children. 1. a. Germanic *beran in (i) Old English beran, to carry: BEAR! (ii) Old English forberan, to bear, endure (for-, for-; see per’): FORBEAR; b. Germanic *bérd in Old English bér, ber, bier: BIER; c. Germanic *bér- in Old Norse bdra, wave, billow: BORE’. 2. a. Germanic *barnam in Old English bearn, child: BAIRN; b. Germanic *barwdn- in Old Eng- lish bearwe, basket, wheelbarrow: BARROW!, 3. a. Ger- manic *burthinja in Old English byrthen, burden: BURDEN}; b. Germanic *burthiz in Old Norse burdhr, birth, akin to the source of BIRTH; C. Germanic *burja- perhaps in Old Norse byrr, favorable wind: BIRR}. 4. Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; AFFERENT, CONFER, DEFER!, DEFER®, DIFFER, EFFERENT, INFER, OFFER, PREFER, PROFFER, REFER, SUFFER, TRANSFER, VOCIFERATE. 6. Latin pro- brum, a reproach (< “pro-bhr-o-, “something brought before one”; pro-, before; see per'): OPPROBRIUM. 7. Lengthened o-grade form *bhor- probably in Latin far, thief: FERRET!, FURTIVE, FURUNCLE; (FURUNCULOSIS). 8. Greek pherein, to carry: -PHORE, -PHORESIS, -PHO- ROUS; AMPHORA, ANAPHORA, DIAPHORESIS, EUPHORIA, METAPHOR, PERIPHERY, PHEROMONE, TELPHER, TOCOPH- EROL. 9. Greek pherné, dowry (“something brought by a bride”): PARAPHERNALIA. [Pok. 1. bher- 128.]
334-bher-2. To cut, pierce, bore. 1. Germanic *bordn in Old English borian, to bore: BORE}. 2. Germanic *baru-ga-, castrated pig, in Old English bearg, barg, castrated pig: BARROW’. 3. Germanic *bor-, perhaps in French burin, burin: BURIN. 4. O-grade form *bhor-d- in Latin fordre, to pierce, bore: FORAMEN; BIFORATE, PERFORATE. 5. Per- haps Greek pharunx, throat (< “a cutting, cleft, pas- sage”): PHARYNX. 6. Slavic *bor- in Russian borot’, to overcome: DUKHOBOR. See extension bhreu-'. [Pok. 3. bher- 133.]
335-bher-3. Bright, brown. 1. Suffixed variant form *bhri-no- in Germanic *briinaz in: a. Old English briin, brown: BROWN; b. Middle Dutch bruun (> Dutch bruin), brown: BRUIN; Cc. Old French brun, shining, brown: BRUNET, BURNET, BURNISH. 2. Reduplicated form *bhibhru-, *bhebhru-, “the brown animal,” beaver, in Germanic *bebruz in Old English be(o)for, beaver: BEAVER!. 3. Ger- manic *ber6, “the brown animal,” bear, in Old English bera, bear: BEAR?. 4. Germanic *bernuz in Old Norse bjérn (stem ber-), bear: BERSERKER. [Pok. 5. bher- 136.] bher-4. To cook, bake. Extended root form *bhrig- in Latin frigere, to roast, fry: FRY}. [Pok. 6. bher- 137.] bherdh-. To cut. 1. Zero-grade form *bhrdh- in Germanic *burd-, plank, board, table, in: a. Old English bord, board: BOARD; STARBOARD; b. Old Norse bordh (> Swedish bord), board, table: SMORGASBORD; c. Old French borde, hut, and bort, border: BORDELLO, BORDER. 2. Possibly Latin forfex, a pair of scissors: FORFICATE. [Pok. bheredh- 138.]
--
1279-BAYy3 badyo- BAY‘ bat- BAYADERE gWele-1 BE bheue-
1280-BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1281:BEE! bhei-1
1282-BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1283-BELFRY bhergh-? BELIE leugh- BELIEF feubh- BELIEVE leubh- BELL! bhel-4 BELL? bhel-4 BELLADONNA deu-2 BELLE deu-? BELLICOSE duellum
1284-BELLIGERENT duellum, gerere
1285-BELLONA duellum BELLOW bhel-4 BELLOWS bhelgh- BELLY bhelgh- BELONEPHOBIA gvel-! BELUGA bhel-1 BELVEDERE deu-2, weid- BEMA gWa-
1286-BEMOAN mei-no- BEN! en
1287-BENCH bheg-
1288-BEND! bhendh- BEND? bhendh- BENEATH ni BENEDICTION deik-
1289-BENEFACTION deu-2, dhé-1
1290-BENEFACTOR deu-2 BENEFIC deu-2, dhé-1 BENEFICE dhé-1
1291-BENEFICENCE deu-2, dhé-1
--
1297-BIER bher-1 BIFORATE bher-2 BIGEMINAL yem- BIGHT bheug-3
1298-BILANDER ambhi, lendh-2
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1300-BIONT es-
1301-BIOTA g¥ei- BIOTIC gWei- BIPARTITE pere-2 BIRCH bhereg- BIREME ere-!
1302-BIREME
1303-BIRR!
1304-BIRR! bher-1 BIRTH bher-1
1305-BIS dwo-
1306-BISCUIT dwo-, pekw- BISHOP spek- BISHOPRIC reg-! BISON weis-
1307-BIT! bheid-
1308-BIT? bheid-
1309-BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
```


## [2026-09-05T14:22:46.672Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"BROW bhr\\|BRIDGE bhr\\|BROW \\|BRIDGE \" AHD_watkins1985.txt | head; echo \"---root---\"; grep -n \"Eyebrow\" AHD_watkins1985.txt | head",
 "description": "Grep AHD for BROW/BRIDGE"
}
```


### [2026-09-05T14:22:46.736Z] TOOL RESULT

```
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
---root---
344:bly Latin fridre, to crumble: FRIABLE. 3. In the Celtic source of Vulgar Latin *brisdre, the source of Old French brisier and French briser, to break: BRISANCE; DEBRIS. [Pok. bhréi- 166.] bhrekv-. To cram together. 1. Probably Latin frequens, frequent, crowded: FREQUENT. 2. Suffixed zero-grade form *bhrk~-yo- in: a. Latin farcire, to cram, stuff: FARCE, FARCI, FARCY; INFARCT; b. Greek phrassein, to fence in, enclose, block up: DIAPHRAGM. [Pok. bhareky- 110.] bhrem-'. To growl. 1. Latin fremere, to growl, roar: FREMITUS. 2. Perhaps variant *brem- in Greek bronté, thunder: BRONTOSAUR. [Pok. 2. bherem- 142.] bhrem-2, To project; a point, spike; an edge. 1. Germanic *bréma-, name of prickly shrubs, in: a. Old English brém, broom: BRooM; b. Old English diminutive bremel, brém- bel, bramble: BRAMBLE. 2. Germanic *berm-, *brem-, in: a. Middle English brimme, edge: BRIM; b. Middle Dutch berme, barm, edge of a dike: BERM. [Pok. 1. bherem- 142.] bhres-. To burst. Germanic “brest- in Old English ber- stan, to burst: BURST. [Pok. bhres- 169.] bhreu-'. To cut, break up. Extension of bher-2. 1. Suf- fixed form *bhreu-d- in Germanic *breutan, to break up, in Middle English britel, brittle: BRITTLE. 2. Suffixed form *bhreu-t- in Germanic *breuthan, to be broken up, in Old English bréothan, to deteriorate: BROTHEL. [Pok. 1. bhreu- 169.] bhreu-?. To boil, bubble, effervesce, burn; with deriva- tives referring to cooking and brewing. I. 1. Germanic *breuwan, to brew, in Old English bréowan, to brew: BREW. 2. Germanic *braudam, (cooked) food, (leavened) bread, in Old English bréad, piece of food, bread: BREAD. 3. Germanic *brudam, broth, in: a. Old English broth, broth: BROTH; b. Old French breu, broth (diminutive brouet): BREWIS; IMBRUE. II. Variant form *bhré- in Germanic *brédan, to warm, with derivatives. 1. *bréd-6, “a warming,” hatching, rearing of young, in: a. Old English br��d, offspring, brood: BROOD; b. denominative *brodjan, to rear young, in Old English brédan, to beget or cherish offspring, breed: BREED. 2. Germanic *bré- d6n-, roast flesh, in: a. Old High German brat, brdto (> German Braten), roast meat: BRATWURST, SAUERBRA- TEN; b. Old French braon, meat: BRAWN. 3. Perhaps distantly related is the Germanic source of Old French brese, burning coal, ember (> French braise): BRAISE, BRAZE?, BRAZIER?, BREEZE2, III. Reduced form “bher-, especially in derivatives referring to fermentation. 1. Suf- fixed form *bher-men-, yeast, in: a. Germanic *bermén- in Old English beorma, yeast: BARM, (BARMY); b. further suffixed form *bhermen-to- in Latin fermentum, yeast: FERMENT. 2. Extended form *bherw- in Latin fervére, to be boiling or fermenting: FERVENT, FERVID, (FERVOR); DEFERVESCENCE, EFFERVESCE. IV. As a very archaic word for a spring. 1. Suffixed zero-grade form *bhru- n(e)n- in Germanic *brunnon- in Old English burn, burna, spring, stream: BOURN!, BURN?. 2. Suffixed form *bhréw-r in Greek phrear, spring: PHREATIC. [Pok. bh(e)reu- 143, 2. bher- 132.] bhreus-'. To swell. 1. Suffixed form *bhreus-t- in Ger- manic *breustam, “swelling,” breast, in Old English bréost, breast: BREAST. 2. Suffixed zero-grade form *bhrus-t- in Germanic *brust-, bud, shoot, in Old French broust, brost, shoot, twig: BROWSE. [Pok. 1. bhreu-s- 170.] bhreus-2, To break. 1. Germanic *briisjan, to crush, in Old English brysan, to crush, pound: BRUISE. 2. Suffixed zero-grade form *bhrus-to-, fragment, in Latin frustum, piece: FRUSTULE, FRUSTUM. [Pok. 2. bhreu-s- 171.] bhri-. Eyebrow. Contracted from *bhrua-. 1. Germanic *bris in Old English bri, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugj6 (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE}, [Pok. 1. bhrii- 172, 2. bhrii- 173.] bhrig-. Agricultural produce; also to enjoy (results,
```


## [2026-09-05T14:22:54.640Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT brvat ===\"; grep -n \"brvat\\|bruuat\\|brvaṱ\" BRT.txt | head -20; echo \"=== BRT bay 'fürchten' ===\"; grep -n \"byeinti\\|bayente\\|byente\\|baya-\\|bay-\" BRT.txt | head -30",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T14:22:54.706Z] TOOL RESULT

```
=== BRT brvat ===
17469:•  j.  brvat-  f.  'Augenbraue',  Du.:  antarot,  KompA.;  Ableit  —  S,  auch/r^  und /reif.— naimaj  -valbyam  V.S.  41,  42,  q.  15,  16.  '  ,  <"■  t^°'  np./'"'-  —  Pü.:  fräc,  fra';  auch n_  i.  I,^a-„ni.-'  vgl.  dazu  S  tS2,  314,  S97-  —  A**'''  f'^'  """*  "f^'-  ~  ''  ^"^  *■*  Pr^CT., f..  np.  abrü,  barü  {tt'Ant.  /O.  "''""  '"'"  ''^^  lugehörigen  Form  gctrennl -  Pü.:  brük.
29957:•  j.  aal  ^^  drux!  ya  natuS  paitisa  Ml "hö.nä  antaräi  nafmät  brvatJyqm  upa.- dvqsaili  V.^.  15;  16,  '?.4i,  41.
=== BRT bay 'fürchten' ===
10436:•  j-,  g.,  p.  'grab-  V.  'greifen'.  Praes. i  grab-,  11%  g^rminä'^,  15  girißa-*'"'^ , 23  garb.tya-,  gSun'aya-'^,  24  gSurvaya-'^, <)-^  24 ^3r?mbaya-'^,2T g)r3bya-,gpr)uya-^'>; Perf  I  jagaurv-*^,  jayaurv-^^,  ftgaurv-^^, 2  jag»r»b-.  —  PPf P.  g^r^ta-'');  Inf.  gfnbqm.
12671:•  j.,g.'dab-V, 'betrügen'.  Praes.2  dava-^'', lob  dibmav-'^,  iddiivia-^'"^^  24davaya-''>, 26  (Pass.)  iytf(yii-'>,  30  (Iter.)  däbaya-.  —
16638:"   g.   baga-,  j.  "baya-  n.  'Anteil,   Los':
16715:927  bay-  —  bav-  2  928
16728:•  j-,  g.  bay- V.  'erschrecken'.  Praes.  2  !  J/^"'"  ■■  "^''i  ^ß'"*'  ^'^^'^  vanhaot  mana- baya-,\  bya-;  Perf.  i  btwt-.  1«"*«-'   ■  ■    "■  ■  "E^^^oref    iK    .  ."    Vr.  //.
16730:setzen':  aisam  asfanhd  bayente'^  "ihre '  <lem  Dasein  treten,  aufhören  zu  exisüren^ Rosse  enegen  Schrecken"  Ytrj.iz;  13;  aussterben':  I  uin/aiy  tauma  mä  bTyir —  isU  ti  nh  iyaökanaU  bymtl '\  .  %^XiffR  (Opt.)  "und  dein  Geschlecht  soll  (auf- sie  uns  in  Furcht"  Y.J4. 8.  a)  intrans. '  hören  zu  sein  sva.)  aussterben"  Bh.4.11, 'in   Furcht,    Angst    sein    vor  -';    a)    mit!  i?-  2)  'etwas,   zu  etwas  (Nom.)  wer-
17415:ai.  bhyas-  V.  'sich  fürchlen'.  —  Vgl.  bay-.  —
19209:*nizbaya-
19244:•  j,  *m-zbaya-  m.  'Anrufung':  mal  °yeke
23654:reicher Angriff,  Sieg':  aojasca  'rpmla  ifary- nasia  zavanca  Y.  yi.  8,  Yt.  /.  22;  — tanvB  vazdvan  .  ,  tativS  °r»m  Y,  Q8.  11; '(f*)'*;  —  fravasayB  .  .  ya  d3%rJl zbayente  Yt.  13.  2^;  —  anairyanqm tat  dahyunqm  'rsi  uz/asaiti  N,  6^;  Yt. to.zd,  A.  j.  8;  —  tfm  hacät  'nm  vlspO.- ayärfm  (sd.)  Ytij.  54;  —  atäril  'ra  Aa- ^aiie  Yt  14-  44;  5-  69,  ig.  54*;  —  'ra  v»r^ %ra7-ast>möYK.ig.Tq;  11.3,  i4.ii  —  *'ra F.S'K
26459:•  j.  skamb-  'stemmen',  nur  mit  Praev. Praes.  9+24  sambaya-^^.  —  Inf.  'scapta- yalca;  Absol.  'skamhm.
27716:•  j.  zamb-  V.,  nur  mit  harn  'zermal- men'.    Piaes.  30  (Iter.)  zimbaya-.
27719:—  Vgl,  vha/iiia-.  —  Pü.;  hamäk  hac  aivz'\r i  tö  valdenän  rSi  iiaslak  afe  kunc.  —  ')  Vgl. die  Var.,  bes.  E  I.  NA.  hat  kqm  ;^nva  tim- bay-  mit  Mf3;  s,  aber  Pu.
27736:1)  'Jemanden,  etwas  (Akk.)  lufen,  an- rufen, aufrufen':  t!ng  sbayä  vanhiu^ uxhäis manankö  "die  will  ich  rufen  mit  den SpTÜchen  des  guten  Smns"  Y.4&.  14;  — thsla  mZ  nqma  sbaya^a  ¥1,75.49;  4.2 {^baySit);  —  urväkamcif  ibayemi  avi  imal vars  Yt.  12. 3i}).  '  a)  bes.  Gottheiten; yd  Ali  (näTai./ravasayi})  yazänS . .  ibayäti Yt  13.  24;  —  asäunqm  ..framaiayS  staomi tbayemi^  ufyemi  yazamaide^  nmänyi  .  . Y.ij.iS;  —  vUpalca  aSe  . .  ga^sfyd(ais IP.) . . tbayemi'^ yatamadal^a^  Y. 7/.  1 1 ; 1 1 ; —  tpm  vairnüi  tbayamaAiVt i5.i;j2.$,Si — yasß  vTspS.matislfm  ssraohm  £baya{iS.) avanAani{sA.)  Y.33.S; — ks  ahi  yü  mqm (näml.  ai^«)  tbayeki  yeiihe  aum  frayd{&6..) tbayiftiqm  sraislim  susruye  vsäm  Yt iy.17;  —  fravasayB  .  .  yi  äährJs  v>r?- %nm  tbayente  Yt.  ;_j.  24;  Y.  20.  3;  — nli£  yasfutnai  . .  Jathyantai  . .  zbayan- tat''''  .  .  äa%at  .  .  ayapfym  Yt  /f.  21 ;  — kal  iöi  asä  tbayentl  avarths zart^uHrai kat  tsi  voha  mananhs  "was  für  Hilfe  hast du,  o  Aia,  was  du,  o  VM.,  fiir  mich,  den Zara&uiira,  der  ich  rufe?"  Y.  4^.12;  — sara%ustra  (sd.)  tarn  aki  pouruiaspahe pukrB  barüryät  Itaca  gapi/i( jSs-AoiH.)^^ "..  von  deiner  Mutter  ward  ich  angerufen" V.  ig.  6;  —  airyamantm  . .  yS  up?mS  (sd.) yS  mähmlS  .  .  zaotlzuye  (3SPM.)*'  G.  /. 6.  a)  mitinf.:  maibyS  z^ya(_iS.)  ai^tn vaishuyä  ait  *gai.tl{sA.)  Y.  j/.  10;  —  bes. mit  avatahe^^:  tä  (Tä.r(A./ravafayll)  mazdä sbayat  *avaähe  Yt/^.  28;  jo.  S^f.*;  — /ravalqyö  ,  .  yä  *ava  *zbayat^^1  avaAke vyqsca  vyänas/aYt  13.3s;  —  "'''  hläsaatca sbayani3i*^  därasia  zbayaniai'"'  Jasaiti avaahe  Yt  ly.  2.  2)    'rufen    nach  -'
30323:anäar  Im  rawäi  i^ät;    im  GrB.  scheint    lu  '  1-  hu-baya-   Adj.  (fem.  •Ja-)    'gutes  EhC;
```


## [2026-09-05T14:23:10.192Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 60 80; do echo \"=== HRN leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -40; done",
 "description": "Print Horn pp.39,59"
}
```


### [2026-09-05T14:23:11.868Z] TOOL RESULT

```
=== HRN leaf 60 ===
- ^^9 —
aw. uhdaena- 'gewebt*; skr. vergl. ürna^vdbhi^
'Spinne* ^).
aty. üdal, ödal 'weben ; oss. vafpi (75) ; bei. gvapag,
n. ^vafay (134); wa;^. vufam, sar. väfam.
Arische (bezw. indogermanische) Doppelformen vaph-
und vahh-, vergl. Bartholomae, ZDMG. 44, 552,
Hübschmann, ib. 557.
' 169. bäy *6arten*.
Wohl aw. bäga- Xoos' (y. 51, 1); ai. hhägd- 'Teil,
Eigentum*; phlv. häg (PPGl.).
de Lagarde's Bemerkung bezüglich Nathans aus
Rom (Semitica I, 52) vermag ich nicht zu kontroliren.
170. häk 'Furcht*.
ar. '^bhäyaka-, von V^hhay' 'erschrecken, sich fürchten'
(aw. Jay-, ai. hhay-),
171. hälä *hoch\
aw. haresiah' 'Höhe'; phlv. bälä^ baldig bal(i)st (aw.
harezista-, z. B. vd. 2 (75)).
bei. baläd, n. bäläd 'Höhe ; empor, auf* (81) ; kurd.
LW. bälä. /
172. bäliS, bälist 'Kissen, bälfn,
g. bälist; Kä§. böUsm, böliSt
aw. barezis' 'Decke, Matte*; phlv. bäl(i)sn (bälln be-
deutet im Phlv. nur 'Höhe, Gipfel', es steht für
aw. bareSnU'j; ai. barhis- 'Opferstreu'; arm. barj
ngooxfcpdXaiop (H. No. 53).
LW. kurd. bäliät, bälisne^ böl%w^ bälge (H.-Sch.);
oss. t. baz 'Kissen* (50); wa/. baleß^ sar. baldjc.
173. hallden 'wachsen, zunehmen* (Sahn. I, S. 3 Vers 49),
bäliä 'Wachstum*-'); vergl. guvöllden (No. 939).
*) Die indogermanische Wurzel vehh'^ veph', vtra'rtü. wthen^ zuerst
Aufrecht KZ. 4, 282, fehlt auch in der neuesten Auflage von Fick*8
indogermanischem Wörterbuch, erster Theil.
') FR citirt als Beleg einen wortspielreichen Vers Senäl's
(Metr. Xeflf):
tä kl hhisesf /^äjS der bcUis
hälei ämed zt näz^ der hälis
=== HRN leaf 80 ===
- 59 "-
)6. bese 'Wald, Dickicht', jüd.-pers. |NnDn:r^2 (Is. 2, 13).
Käs. Visa; mäz. täl. vtsi.
aw. varesa- *Wald'; phlv. vesaJc; ai. tjksd- *Bauin';
dazu gr. älaog (Bartholomae, briefl. Mitteilung),
kurd. vise (H.-Sch.).
37. bei ^Grabscheit* ^).
Käs. 6ör, böl, bäl^ berd.
Zu aw. [/^bray- schneiden' (de Lagarde, Ges. Abh.
297).
np. bei statt bäl beruht auf Imäla.
kurd. bal^ btel 'Spaten' (H.-Sch.); wa;r. bil, sar. bSil
*Spaten'.
58. blni 'Furcht'.
[bhay^ ' erschrecken , sich fürchten (aw. bai/-y ai.
bhay-), *bhänia7i- ; phlv. 6fm, blmkln,
39. bimär 'krank^^ bimürJ.
aw. v% ■-\;- v^war-) (vergl. vJ-merencalt^); phlv.
vimär, vlmärlh (Men.), virnärinltan (y. 30, 6 nach
Darmesteter's Correctur, Et. ir. II, 138).
Die Etymologie ist gewiss falsch, da altes vi- im
Neupersischen consequent zu gu- wird, und selbst bei
Annahme eines Ausnahmefalles (z. B. biüer^ No. 218)
das i völlig unerklärt bliebe. Dass das erste Glied
np. be- *ohne' sei, könnte man nach sar. LW. bhnar
(d. i. bemar) vermuten; doch erhält man bei dieser
Ableitung keinen guten Sinn. Bartholomae schlägt
mir die Etymologie upai (s. No. 247) + mära-y also
*am Tode' vor, aber dafür spricht nicht das phlv. v
(oder auch w),
30. bin *sehend', hin-em^ binä^ bmis,
ap. vainähiy Conj. (Venn) du siehst'; aw. vaenämi
*ich sehe'; phlv. ven-am, ven(i)sn^ venäk^ venastan (päz.
vm-), vergl. üben (vd. 19 (43)).
af/. vm-am; oss. d. mmin, t. ünin (82); wa;^. §iyn.
viti-am, sar. veln-am.
*) Gul. (Sprenger) S. 26 Zeile 8 reimt es ausnahmsweise auf piL
```


## [2026-09-05T14:26:31.488Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB bim/bak/abru ===\"; grep -n \"bīm\\|blm '\\|bäk\\|abrū\\|abrü\\|barü\" HUB.txt | head -20",
 "description": "Grep Hübschmann"
}
```


## [2026-09-05T14:26:31.488Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /ابرو/ {print NR\": \"substr($0,1,200)}' BQT_v1_pages.txt | sed -n 1,25p",
 "description": "Find abru in BQT v1"
}
```


### [2026-09-05T14:26:31.544Z] TOOL RESULT

```
=== HUB bim/bak/abru ===
5471:(belegt vainahy, avaina); blm 'Nase = paz. vlni Shk. 273;
```


### [2026-09-05T14:26:33.240Z] TOOL RESULT

```
111: مقدمه ۱ ۱ صد ودو
۳ نویسان بعدازجهانگیری - ازجمله حسین خلف موّلف برهان
ق قاطع - لفات مز بوررا ازفرهنگ وی استخراج �
116: صد وهشت لپجه‌های ایرانی در برهان
نش (ذیل : شنگ )» جارشاخ ۱ ( یل : سکر)» چرخ ریسو ۴ ( فیل :
چرخ ریسك)» دانگانه ۴ ( ذیل : 
139: مقدمه صد وسی
و تثری‌تا لیف کند ده‌ها سال تتبم وتحقیق واستغراجلغات ازمتون نظم و نثر
فارسی که درمدت هز ار سال نو
291: و نگذارد که جراحت ورم کند . وااگر بلس رکه
بردمل. وخيارك نهند ب رکرداند ۱ » وابرک کیاپ "
یز بنض آمده است که در آخرش 
292: اول و فتح ثانی حوبرء را کویند و آن پرنده
ایست که بمربی « حباری » گوبند ۴ و کی
«تفدری» خوانند و بکسر اول ميو# نوری 
320: سس سا
مشهور که افلاطون وضع (۱) کرده است ؛» و
ی گونند .ارغنون
ترجبة مزامیر است
بعنی جمیم ساز های
»؛ وبسنی دیگر
کرن�
488: سای هس
و بفتح او وسکون ائی‌نام ماه - و ستارمشتری
باشد ۱ - و بفتح اول و ضم ثانی ابرو را گونند
```


## [2026-09-05T14:26:37.972Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 289 290 291; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt; done 2>/dev/null | head -120",
 "description": "Print BQT v1 leaves 289-291"
}
```


### [2026-09-05T14:26:39.543Z] TOOL RESULT

```
=== leaf 289 ===
- ۷ - ایکا کبا
و سکون الث و ها و رای قرشت ؛ نام اصلی
نیشابور است و ممدن فیروزه آلجاست ٩‏ .
ابر قباك ع من فان . نام ولایتی است
از توابم اره جان ۱ که میان اهواز و فاری
واقم است و آباد کرد قباد شهربار است ؛ و با
زای قطه دار هم کفته اند ۲ . #
ا پر کاد - باکاف‌بروزن‌اتکبار » بمعنی
متحیر و حیران و س رکردان باند ۸ .
ایکا کیا هیفتح اول وانی‌و کسرکاف
دوم تحتانی بال فکشیده , ننیده و تارعنکبوت را
کویند. اکر بر جراحت نهند خون را باز دارد
انت و بمربی «سحاب» گود ٩‏ - و بمعنی هرد
(۱) هم آمده است که دره‌قابل زن‌باشد, و بفنح
ثانی‌بلفت زند ویازید (۲)لت تناسل را گوید ۳
- و «بر » را نیز گفته الد که بمرمی « علی »
خوانند ۴ و بمعنی بر و آغوش هم هت  .‏
آ برش ع بنتح اول و تال ۰ بر وزن
مهوش ؛رنگه سرخ و سفید در هم امیخته را
گوبند . - و اسبی که نقطه های مخالف رنگه
او پر او باشد ۴  .‏
] پر ش خور شیف کنابه‌ازآسمانت.
ابر شهر - فتح اول و انی و رابع
(۱) چك : مردم ! )۱( چك : ژند و باژند ..
۱ - انسکرت 2080۴4 (با 200068 مرکب از0۳۵ - ۵0 بمعنی برنده وحامل
آب ) « وبلیامز ۳:۷۹ > اومتا 3072 بارتولمه ۹۵ بهلوی 27 « دهارله ۱۷۹ » « عنلی
۶ > ۸ نب رک ٩۱‏ . اففانی ۵۲2 . بلوچی 8۷1۲ (باران) « بارتولمه ۹۵ » , کردی ]اقلا .
اورامانی ۷۴۲ : 4 . اورآمان ۱۲۲ * .گلکی ۳9 دزفولی ۳۷ . ۳ 32602۲
حزواری است بمعنی ره » آلت رجولیت « بندهش ۱۱۲ ۰ ۶ یوستی » بندهش ص۵۱ * . اشتباه
نشود ا.« ابر » که در عربی بمعنی نره و فرزند فررینه است و 26779)2(8 هزوارش پمعنی آلت
رجولت « بوتکر ٩۳‏ ۰ . ۴ - اوتا ۱۳۵17 و ۱۳02۲ بمعنی بالا ۰ عالی»
سال‌کریت ۱1۳8۲1 « بارتولمه ۳۹۶ - ٩۵‏ ۰. پهاوی 8087 < منای ۲۹۹ < اونوالا ۳۳۵ ۰
«نب رکه ن 9
۴ - از آن ایرش وبور وختگك وسیاه که دیده است ه رکز زآ هن سیاء
فردوسی * لت تامه » رك : نوروزنامه س ۱۱۰ . ۵ - ۸52۲5۳229۲ , در ارمنی
01 ۸۳8۲, اینکه‌یسی آنرا بمعنی شهربالا بادکرده‌اند درست نیست. بلکه بمعنی شهر
( 8۳27001 بونانی ) برجته‌ترین قبیله ازسه قبلهٌ داعد28102] که دوت‌بارنی
( شاید : اپارنی » ایرنی ) را تأسیی کردند « مار کوارت . شهرستانهای ابران صس ۵۲ بافوت‌این
نام را جفتح اول وسکون دوم وفتح راء وشن معجمه آورده و کوید سکزی آنرا بی‌مهمله روایت
کرده است, رآن معرب است واصل عجمی‌است زبرا «شهر» بفارسی بمعنی بلداست و «ابر» بمعنی
«غیم». ابرشهر تیشابور است و کاه همزه ر) قاط کنند و 3 برشهر ٩‏ گونشد .۰« ممجم‌البلدان »
« کرستنن . سلطنت فاد ترجمه فارسی ص ۰۳۵ . 1 - ارجان . ۲ - بافوت
هم < ابز قباد * بفتح اول وانی و سکون زاء وضم قاف ر باه موحده و الف و زال مجمه آورده
گوبد : بپمین وجه بزاء بخط چند تن از اهل علم دبدهام وقباد بن‌فیروز یکی ازپادشاهان ابران
ویدر انوشیروان عادل است و نام این موضم در فتوح (اسلام) با « مذار » باد شده و گویا ابر قباد
مجاور «میسان» و «دستمیان» باشد وهلال‌ین محن گوید: ابزقباد. (بازاء) ازطسوح‌های مذار.یین
=== leaf 290 ===
و نگذارد که جراحت ورم کند . وااگر بلس رکه
بردمل. وخيارك نهند ب رکرداند ۱ » وابرک کیاپ "
یز بنض آمده است که در آخرش بای ابجد
باشد . ٩‏
ابر که ین کاف » نم شهزیست از
عراق عجم . و چون‌آن شهر بر زمیتی که درته
آن کوه است واقم شده باين نام موسوم ماختند
ومعوب آن ابر قوه است ۴ حرایین زمان بتعریب
ار هر گنه - بکر ثاك و خم میم »
بمعنی ابی‌کپن است که اسفنج الب باشد ۴ .
ابر نجن - بفتح جیم‌بروزن ب رکندن»
حلقه ای باشد از طلا و نقره و امثال آن که
زان در دست و بای (۱) کنند ۴ و آنه در(۷)
دست کنند دست ابر نج و آنراکه در (۲) بای
کنند پای ابرنجن خوانند .
اتتهار دارد . ابر ن<سن - بر وزن فروردین ؛ بمعنی
اب رگن - بکس تاك و انوم ابر‌تجن است . وان حلقه‌ای باشد از طلا و نقره
که در (۲) دست و پای کنند ۴ .
ایرو ددن - کتابه از دا دادن
واشاره کردن باشد ۵ .
ها و سکون نون . چیزی است مانند مد کرم
خورده » چون بی آب گذارند اب را بخود کشد
واسفنج الیسر حمانت ۴ .
۱ - دلیل توایری است یوشای حق بیستی است همچون ابرکا کبا
لطيفي پنقل شموری. ومحتاح اید شواهد است «افت‌نامه».
۳ < ابرفوه » , حبط ابوسمد وبضی دیکر ۶ اپرقوبه » نوشته اند واحل فاري آن را
« ورکوه » نامند ومعنی آن « بالای کوه » است. و آن شهرست مشهور بارس از کورة اسطضر
ترديك بزد. « ممجم‌البلدان »؛ ساب ناحیه‌ای آباد ومهم‌بوده. وهوای آنکرمیرواراضی‌حاصلخیز
وقابل زراعت دارد . درخت سرو بیار کهنی درآنجا هست , اراضی آن از قنواتی حشروب میشود
که.بستی از آنها بیار طوبل است . محصول عمد آن تربالك وینبه وتتبا کو وقلات » شتجی ۱
بافنن کربای . کلردگ ورونای درآن بسیار بعمل آبد ۰« کبهان . جفرافبای سیاسی*44*.
۴ . رك : اسفنج . ۴ - آورنجن , خلخال . ٩9‏ رضا نمودن با اشارت
ابرو . دستوری دادن با اشارت ابود » و لیز بمعنی اشاره کردن ابرو برای دلال آمده استء
۶ لت نامه * .
۵ ابر گون - نوعی اسپ « نوروزنامه ۵۳ : ۱۲ و۱٩‏ *.
* ابرو - اوستا0۲۷34 . ماسکرت 8 , پهلوی ۰« ابرلندی قدیم
4 . فارسی ابرو و برو « بارنولمه 4۷۳ ۰ « اوتوالا 4۰۱ > موخی ۷۳۵۵ ۰ اشکاشمی
۷۲2 ۰ منگلجی ۷۵۲۵0 , شفنی ۷۲۷/8« گربرسن ۲۱۰۱ ؛ طبری 96718 , مازندزانی
کنونی ؟1د « واژه نامه ۱۰۷ » ؛ مجموع هوی روییده برظاهر توا قوسی شکل بالایکاسة
چشم بزیر میشانی . حاجب . مضففآن برو .
یه از سفحهٌ ۷۹
جمره و واسط است . ابنالفقیه و دمگران کفته اند : ايز قباد کوره بست از ارجان بین اهواز
وفاری . «ممجم‌البلدان» . ۸ - از لفات دساتیر است . «فرهنکه دساتیر ۲۳۲.
۰ الراهیم ‏ رك : اپرهام . زا ابرقو , ایرقوه , امرقویه رک : اب کوه -
( برهان فاطع ۱۵ )
=== leaf 291 ===
اول و فتح ثانی حوبرء را کویند و آن پرنده
ایست که بمربی « حباری » گوبند ۴ و کی
«تفدری» خوانند و بکسر اول ميو# نوری و و
باوه باشد ۴ .
ا یر هام » باها بروزن شفق فلم . بمعنی
طسمت باشد؛ گویند فرشته ات که تدی سکننده
عالم است - و تام ییفمبری هم هست ۵ .
ار هه - بنتح اول و ثالث و رابع » تام
پرنده ایست بمیار حقیر ۷ - و نام سر کروء(4)
اصحاب فیل هم هست . کوبند وفتیکه بخراب
کردن که معظمه می آمد ؛ در راه بجپنم
واصل شد و هو که قبر اورا می بیند بی اختیار
ارو د فك - ینی اداره کند -
ورشادهد - _,
اپرو فراخی ‏ کنابه از خوشدلی
و خوش منشی و کشاده روبی و اژه دوی -
وهمت و سضاوت باشد (۱) .
ابرو لقن -با نون و تای فرشت » بی
ون پهلو شکن . بزبان زند و باژند (۲) بمعنی
مردن باخد که در مقابل زستن است ِ.
ابر وی دالزد س کنابه از ماه نو
باتد که بعربی هلال گویند .
ابر ه « بفتح اول و سکون انی » دوی
کلاه وروی قبا و امثال آن بائد ۴ -و بضم
۹ وارش ۵ بپهلوی ( مردن ) ۷6۲01010180 است « براهامیان ٩٩‏ *.
۴ - لرماند پیکی‌سف رگث‌دیبا آمتردیبةٌ زرد , ایرآن حمرا «منوچهری۱۹۱.
```


## [2026-09-05T14:26:54.465Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for L in 558 559 560 561 562; do echo \"=== leaf $L ===\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | tail -25; done 2>/dev/null",
 "description": "Print BQT v1 leaves ~560"
}
```


### [2026-09-05T14:26:56.216Z] TOOL RESULT

```
=== leaf 558 ===
خوانند .
یضهای ددلین و ینهای‌زری که
بیضجر خ کنابه از[ فتاب است.
بیضه دد آب » بینه‌ای تکههنوز
بچه درآن متکون شده باشد .
بیضه زد - ويضة زریی ۰ کنایه از
خورشمد عالم آراست 8
لیا" ه بفتح اول و سکون انی و غین
نخطه دار بالف کشیده ۰ نام مرغیست که از
هندوستان آورند و بعلوطی اشتهار دارد. وآنرا
طوطك یز کوبند .
۱ - پدین‌ممنی‌درپهلوی 065 «منای ۲۹٩‏ : ۲ *. در اوستا» ۷۷5/2 بمعنی‌زهر است .
در عفة حکیم مژمن آمده: «بیش: بهندی بش نامند» واوبیخی است مثبت او بلاد چین وکوهی .
که حلاهل نامند و لهذا زهر هلاعل عبارت ازوست » واوسرم نفوذتر ازسم افعیاست وقلیل اقسام
ار کمتر از دوساعت فانل است و در بلاد هند نیزاقام‌اومیباشد . » ۶ بشت ۲۷۵۱ ح* : معرب
آن نیز «یش» است «نفس » . - در اصطلاح احکام جوم بیش‌فارسی پممنی ترح وآفت عربی است.
< کاءشماری ص۳۳۷ ». ۴ اوستا ۷۵125198 (جنگل ) » سااسکرت ۷۳۴5۲18 (درخت)
«اسفا ۱: ۲ ص۸۸ ۰ پهلوی ۷151216 < بندهش 6۱۸۹ . سفدی ۷151021 «کوتبو ۱۱۸ » طبری
ما سرانی کنونی ۷1502 د« واژه نامه ۷۹۹ » اورامانی ۷۵58 « .اورامان ۱۲۷
۴ مصحف : بیفا. درعردی ببغاء بفتح‌اول‌وسکون دوم‌وفیز فتح اول ودوم‌مضفف رهم بفتح‌اول
ودوم مشدد». طوطی ست:
* یطار -بفتح اول, از بونانی ۳۳1۵/۳05] م رکب از1۳۳05 بممنی اسب و 180۳05
پزشك ( 134718 مداوا) ؛ جمماً بمعنی ستور پزخكو 1120184۳6 درفراضه بمعنی درمانکننده
اسپ‌از خمین ریده است «تفس». همرب‌آنهم بیطار وییطر بفتح و کسر اول (هردو) , رك : دائرة -
المعارف اسلام -
=== leaf 559 ===
لیل- بانانی مجهول
بر وزن فیل » آلنی باشد
آهنی(۱) که باغبانانو امثال
ابشان زمین بدان کنند ۴
- وپاروبیرا(۲) نیز گویند
که کشتی‌بانان بجهت‌راندن
غراب‌سازند و نام‌میوه‌است
اقعام یل
عرای- وبلفت زند و یازند(۳) بمعنی چاه‌باشده 5
مطافاً که بعربی بیر خوانند - و سبدس رگین
کشی ر کگاسیرا نیز گوبند .
ببلای۱ عم با اول بای رسیده و ثالث
بالف کشیده و بتحتانی زده» بلات زندویازند(۳)
چاه باشد مطلعاً که‌عربان مرخوانتد .
لبلسته . با انی مجهول مر وژن می
دسثه , انگشتان دست راگوبند - و نوعی‌از کل
هم هست .
در حندوستان شبیه به هی
(۳) چك : ژند و اژند.
0 مر ۳ ۴ راد :
فرهشگ» روستابی ص ٩٩۷‏ .
۱ - هز . (2/0ا0 : پهلوی
روسای سیاه ۰ «داثرءالممارف اسلام*.
.» ۲
۶ دار ةالمعار ۳
=== leaf 560 ===
یماد سان ۸ بعثی‌سمارهانشد.چسان
بمعتی مانند هم آمده است - و بیمارستانرا نیز
کون که بعر نی دارالشقاء خوانند ِِ‌#
پیمااد غشج - بیمار معلوم» وفتح ین
نقطه دار و سکون نون و جیم . بمعنی بیمارناك
و دردمند است یمنی بیشتر اوقات بیمار ورنجوز
باشد- و کسی رائیز گویند که ببه‌اری او از روی
لاز و غمزه باشد .
بی‌محابا بلنگ ه کنابه از دیا
وروز کاراست - و کنابه ازمی که وهوت‌هم هست.
لیهیر ع بر وزن دییگر؛ بمعئی بیشمار
وییحد و حساب وبیار باشد. چه مربیعنی شمار
هم آمده ات
لیهاز ع کنابه ازمردم سبك‌وبی‌تمکین
مهو ری حم ثالث بروزن بی‌نوری؛
بمعنی مهابت و صلابت باشد*۱.
یف ۷اه بکسر اول بر وزن میتاء بمعنی
دیده ور باشد - و بلفت زند و پازند (۱) بمعنی
۴ - یلفان. شهرست تزديك
۴ -ر: یله. ۴ ر:
شهمیرزادی؟01۳18 < . ۲ص ۱۷
هی کب از امین هی
*- فرهنگ دسانیر ۲۳۷ .
«اسفا ۱ : ۲ ص ۱۸۱ ۰ .
معرب آن یمارستان و مارستان «شی». "
=== leaf 561 ===
پیواد - با نانی مجهولبر وزن دیوار,
عدد ده هزار را هنشت و باین حمثی. محذف الف
پیواده » با تالی مجهول بر وزن
بیجاره ؛ بیکس و غریب وتنها -- وبی‌قدروهرتبه
وبی اعتبار را گویند - و چویکه بدان كلولة
خمیر انرا تنك سازند .
یو اد با نانی مجهول بروزن شیراز »
شیره باشد که آنرا مرغ عیسی گونشد و بعر بی
خفاش خوانند - و بمعنی اجابت و فبولهم آعده
است. و پاسخ وجوابرانیز کویند*۱» وباین معنی
بجای حرف الی لون هم‌بنظرآمده است»وبمعنی
اول بجای حرف اول بای فارسی هم آعده است
پیو بادیدن » بکس ارل و اك
مجهول بر وزن فرو باریدن, ناجاویده فرو ,بردترا
کون که بمربی بلم خوانند ؛ و بفتح انی حم
آمده است که بر وزن شکم خاربدن باشد واین
اصح است . چه در اصل این لفت باوبارسن
بوده است همزه را ببایدل کرده اند بیوباربدن
؟ از:یا. ۳ بی(حاصل
۴ ۳ آسم فاعل ازددن
۷ باین معنی « بيوك » هم آمدهءو در
۸ اظ م مصحف: _ (هم).
بتواچث رد جواب ۴ سحیح ی
سرخه 1 ۷50 ۳ شهمیرزادی از «ء ۰ ی اه جزء ۲ عموداً
ی مشاتی و دهان فرار دارد و قو شامه در جوف آنت .
=== leaf 562 ===
یو سیفن - بر وزن‌خموشیدن» بمعنی
امید داشتن و امیدوار گردیدن وطمم کردن-
و چاپلوسی نمودن باشده .
واو وکاف فارسی » بمعنی عروس است ونم اول
وبای فارسی ح آمده است*٩.‏
یو گانی » با کاف فارسی بر وزن
جیوشانی » عروی را کوند چه بوک بمعنی
عروی باشد و در موبدالفضلا» بجای حرف ثانی
تونآورده است
یو گندن پکر اول و فتح لا
چه در لغت بواز 1 می‌باید٩۱.‏
لبون » بفتح اول بروزن زبون؛ ترباك
وافیونرا کویند؟۱- وبعربی‌چاههای عمیق‌وسیم‌را
؟ - بپلوی 98۷۵۲
کجا سور از پهلوالی شمار
۴ رك؛ باورد و اییورد.
پیوسی بعنی انتظار بهی و خویی :
افموی که دور به‌بیوسی بگذشت
۷ رگ : بوسیدن .
تن ۱ص ۲۵۱>»:
بود در زبان دری ده‌هزار . فردوسی‌طوسی.
٩‏ - و به
تین کت از ۱
0- ره : او کندن و او فکندن .
۴ مخفف ابیون » رك : افیون .
```


## [2026-09-05T14:27:09.522Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk -v n=561 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt",
 "description": "Full leaf 560"
}
```


### [2026-09-05T14:27:11.243Z] TOOL RESULT

```
بنم ثانث مر وزث میگفت اه
ستارژ زهره را گوبند .
بیلقان ‏ بنتح اول و و
بر وزن نهروان ۰ شپرست از ولات اران مابین
شروان و آذربایجان؟ . ۱
پادشانعان - و قبالة خانه و باغ و امثال آنرا
کونند؟ - و تبربرا دز کنته اند که ییکان آن
دو شاخ باشد - و بکر اول وئانی مجهول‌نوعی
از پیکان باشد کهآ ترا مانندهگیل کوچکی سازند
و آنرا پیکان شکاری کر ۵
9
یله - با انی مجپول بر وزل حیله,
خشکی و جزبر؛ میان دربا و رودخانه باشد -
و نوعی از دوابی هم هت - و طبله و خرطهُ
عطار را هم گفته‌اند ومنشور یادشاهان؟ - وقبالة
خانه و باغ را نیز کویند ۴ - و بمعنی رخاره
و پهلو نیز آهده است- ویاروب کشثیبانان که‌بدان
غراب رانند - ویبکانی که مانندیل سازند» -
و چرل و ریمی که از زخم آید - و بمعنی له
ابریشم هم بنظر آمده است - و بت رکی بمعنی
همچنین باشد .
(۱) چك : ژد و بازند .
مك . نت وق <
دیب رک ۰۳۹ 1 : اس ۲۹.
«اونوالا+۲* ازریشابرانی باستان۲02۲3 -
کیلکی ۲1۳2۲ .
۸۵ ره : اسفا
ک ۳۰ ۳
لبم ٩‏ ت بروزن‌میم؛ تری‌وواهمعرا گوند.
دیمار ۷ بروزن دیوار, ناتوان وختهرا
کگویند وامربه نرسیدن هم هست متی بتری.
یماد سان ۸ بعثی‌سمارهانشد.چسان
بمعتی مانند هم آمده است - و بیمارستانرا نیز
کون که بعر نی دارالشقاء خوانند ِِ‌#
پیمااد غشج - بیمار معلوم» وفتح ین
نقطه دار و سکون نون و جیم . بمعنی بیمارناك
و دردمند است یمنی بیشتر اوقات بیمار ورنجوز
باشد- و کسی رائیز گویند که ببه‌اری او از روی
لاز و غمزه باشد .
بی‌محابا بلنگ ه کنابه از دیا
وروز کاراست - و کنابه ازمی که وهوت‌هم هست.
لیهیر ع بر وزن دییگر؛ بمعئی بیشمار
وییحد و حساب وبیار باشد. چه مربیعنی شمار
هم آمده ات
لیهاز ع کنابه ازمردم سبك‌وبی‌تمکین
مهو ری حم ثالث بروزن بی‌نوری؛
بمعنی مهابت و صلابت باشد*۱.
یف ۷اه بکسر اول بر وزن میتاء بمعنی
دیده ور باشد - و بلفت زند و پازند (۱) بمعنی
۴ - یلفان. شهرست تزديك
۴ -ر: یله. ۴ ر:
شهمیرزادی؟01۳18 < . ۲ص ۱۷
هی کب از امین هی
*- فرهنگ دسانیر ۲۳۷ .
«اسفا ۱ : ۲ ص ۱۸۱ ۰ .
معرب آن یمارستان و مارستان «شی». "
```


## [2026-09-05T14:27:29.485Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"بیم\" BQT_alt_v1.txt | head -20; echo \"=== dli ===\"; grep -c \"\" BQT_dli_part1.txt; grep -n \"بیم\\b\" BQT_dli_part1.txt | head -5",
 "description": "Check alternative BQT OCRs"
}
```


### [2026-09-05T14:27:29.573Z] TOOL RESULT

```
217:گذشته ازهم نگسته‌وخویشاوندی[نها بیمدیگر پیدا و آشکار است . 
1447:« گوزهندی» است. بیمین مناسبت برخی از محققان معاصر «پارسيك» را 
2254:حروف الفباست از < عين »> حرف اول عدل ممدوح یعنی از بیم عدل او 
2959:قلمرو زبان دری بوده‌اند از ناصر خسرو می‌پرسیده و بیمین‌جهة کتاب لفتی 
3736:عد از سلاطین بیمنی در بار »ای از ملك 
4181:بیم آنکه کتاب وی بسیار حجیم و ضغیم گردد آنپا را حذف کرده است » 
4221:طبیمت باید.( ظ, پابد< باود )» برهان جمله راغلط خواندء بخطا تعبیر کوده است. م.م. 
5208:2 بست ۱ >راگویند و«یوز» صد را و «منک» ببیم مکسور ونون سا کن 
5490:در «یوماللا من‌شهرر بیم‌النانی ۱۲۲۷ باتمام و سیده. 
6245:هه ارو نامه. د کتر احمده پارسا. از نشریات موزءة علوم طبیمی . 
6603:ومجلد دوم (مقالات بز بانپای اروپایی) بیمت انجمن ايران لیگ . ۱۹۵۰ 
7253:بیمنی قاطر 
7835:کردن «می‌افروزد»" واز فروختن به‌منی‌بیم کردن « میفروشد »وازدوختن 
9294:۰ .۴ - بیمتی‌شت » خادمی که مأمور تهیةٌ مشرویات است؛ صاحب رنبه ای که موظف‌است 
9414:و مستراح را گوبند - و بیمنی دلو آب کشی 
9453:ازآن . باس‌پوشی سوراخ دار که اطبا بیمارانرا 
9454:در آن خواباند با بتثاننه » و سر بیمار را اژ 
9625:] بشتنشگاه » بیمنی آبششگاه است که 
9668:و امثال آن بمقدار قامت آدمی که طبیبان بیمار 
9740:هطه » بیمنی آب طریست. که شراب انگوری 
=== dli ===
7
```


## [2026-09-05T14:27:30.505Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /^.*باک/ {print NR\": \"substr($0,1,120)}' BQT_v1_pages.txt | head -20",
 "description": "Find bak in BQT v1"
}
```


### [2026-09-05T14:27:32.236Z] TOOL RESULT

```
33: مقدمه بت و چپار
برای آن بر نگز یده‌اند ۱ . بدیپی است که تحقبقات آین�
71: مقدمه شصت و دو
پس از مدت‌ها صخح وزیر ورو کردن این کتاب‌متوجه شدم ک
243: ]دی ح بکر الث و رايع و سکون
تحتانی ۰ بمعنی ممنوی باشد که در مقابل لف�
256: ی آشنا کر
خابة سک آنی است ۷ . خالهرا نیز گویند چنانکه گوبند «اين عما
264: کپ هن اف ودک از
فارسی 9 کویند و آن کرداکرد اندرون
دهان است
قلاب را ک�
265: و بکرکاف فارسی محکم بتهراگویند ۱ .
] گففت - بنتح کاف نک
وغای فرشت شت �
266: و شین فرشت » بممنی در آوجخته باشد چه اندر
آکیشید پمنی الدر آوشت - و �
273: آموده ۰ 7۳۳
و آ یخته‌شدن - وساختن و ساخته گردانبدن٩‏ ۹
و پر کردن و م
```


## [2026-09-05T14:27:38.982Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD bem/brug ===\"; grep -n \"bēm\\|bem \\|brūg\\|brwg\\|abrūg\\|byhm\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"bēm\\|brūg\\|brūk\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep MacKenzie and Nyberg"
}
```


### [2026-09-05T14:27:39.112Z] TOOL RESULT

```
=== PHD bem/brug ===
PHD.txt:292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
PHD.txt:649:waxšwar [whiwl | N waxtür] prophet. ~th: prophethood. P wāxtan, wāž- (w’hin', wc- | P wxtn, и?с-] say, speak. lway [wd = Av. way-] bird. *way [wd = Av. wayu- | P шуш] air, atmosphere. ~ í wattar: a demon. ~ i weh: a divinity. way [wd | M wy, N ~] woe. lway- [w*d- | M w’y-] fly. ~endag [-(y)ndk! | J w|B' ynd?] bird. wüyidan, *way- [w'd-ytn'] blow (of wind). wayodagàn [wydwtk’n! | M *wywdg'n, N bayēgān(ī)] nuptials, marriage feast. waz-, -išn(-īg), у. wazidan. waz [wc | = M, (N bāj)] word, speech; ‘grace’ (before meals). ~ griftan: say ‘grace’. 1, *wüz-, ~iSn, v. b *wāzīdan. P wāž-, v. wāxtan. wāzag [w’ck'] utterance, saying. wazay [wzy| N ~, bazay] frog. wāzār [w’c?l | M w?c'r-, N bázár] market. wāzāraģān [wlkn! | M wergn, N bázárgàán] merchant. ~ih: trade. wazidan, waz- [wc-ytn! P wz-, N ~] move, blow (of wind). ~išn: movement. ~i$nig : mobile. Iwāzīdan, wāz- [wc-ytn'] move, carry away; fly. ~išn: flight. *wazidan, w4z- [w'c-ytn! | N bāzīdan) play. wāzīģ [w'cyk! | N Бахт] game, play. wazr [wel] = *warz. wéd [wyt' | N bed] willow. weh [SPYL < А #руғ; wyh | M why, wyh, N bih] better, good. ~ih: goodness. «-dēn [-dyn' | N bih-din] of the good (Mazdean) religion. wēhm [*wyyhm | M wyhm] large, wide, broad. ~ih: width, breadth. wém [шут | = P] rock. wēmār [wyml | M wym’r, N bēmār] ill, sick. «Ih: illness. wén [wyn'] breath. wén-, ~i5n(-ig), v. didan. wēnāb [wyn’p | N binàb] vision. ~dag [-d’h', -t*k!] visible. wënäe [wyr?k! | M wyn!g, N bind] seeing. ~īh: seeing, sight.
PHD.txt:3937:tasteless abēmizag.
PHD.txt:5159:nibēm
PHD.txt:5444:gurgānīg gursagih gursag durgar jorda jorda 1-2gurdih gurd gurdwar gurdag dum, 1021 joma jomā gumānīh gumānīgīh gumānīg gumān gumāngar gumār- gumārdan gumārdag jumb- dumbēmand jumbāgīh jumbīh-
PHD_mackenzie.txt:1639:bru~ [blwk I M brwg, N abru] (eye)brow.
PHD_mackenzie.txt:3729:nibem [npdm I (P nbdm-)] lying, prostrate.
=== NYB ===
```


## [2026-09-05T14:27:40.459Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC bhau/bheu joy ===\"; grep -n \"^bhāu\\|^bheu\\|^bhōu\\|bhāvita\\|bhavita\" IEC.txt | head -30",
 "description": "Grep Mann IEC"
}
```


### [2026-09-05T14:27:40.513Z] TOOL RESULT

```
=== IEC bhau/bheu joy ===
1266:bheudhó ‘prompt, arouse, exhort; be awake’. Cf. bhudh-. WP II, 147 Skt. bódhami; Gk. peüthomai (lit. “be prompted', hence ‘hear of); Go. cf. ana-, faür-biudan; OHG biotan; OE beodan 'de- clare; order": ON bjóða ‘offer’; OFris. biada; OCS bljudo, bljusti ‘guard’
1267:bheudhos ‘offertory, bowl, platter’. Cf. bheudho Phryg. (in Gk.) beüdos “a coloured garment’; Go. biups ‘table’; OE beod ‘table, dish, bowl’; MHG biute ‘kneading-trough’; ON bjóð ‘table, bowl’; OCS bljudü “dish?
1268:bheugo (bhoug-) ‘flee’. WP II, 144
1277:bheuros, see bheuəros
1278:bheuən-, bheun- ‘dwelling’. Cf. bhou-, bheuó Skt. (ambig.) bhavan; Alb. bun “mountain- hut’; cf. MHG biu-lich
1279:bheuəros, bheur- ‘awful, enormous’. Cf. bhour-, bhur- Av. baevaro ‘10,000; LW in Arm. biwr, wd: Oss. bīrä, beurä, berä ‘many’; W bur (i-st. ‘rage’); OCS cf. (o-gde) burja ‘storm’; Li. biaurùs ‘nasty, boorish’
1280:bheuð (bhou- bhü-) ‘be’. Cf. bhou-, bhū- as separate entries Skt. bhávàmi; Av. bavai(mi) beside buye, mp.; Arm. cf. bovem ‘wait, expect’; Alb. buj ‘lodge, spend the night; W cf. bu ‘he was; MHG biuwen, bouwen, büwen ‘dwel; Go. cf. (o-grade) bauan, id.
1286:bhəu- ‘please’. Cf. bhou- (3) Skt. cf. bhavilah ‘good; lecher’ beside (*ou) bhavitah *elated'; Per. cf. büye (s. “hope, de- sire"); (for Lat. faveo, ere, which is ambig.,
```


## [2026-09-05T14:27:48.296Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 1284,1296p IEC.txt; echo \"=== bhou 3 ===\"; grep -n \"^bhou-\\|^bhou\" IEC.txt | head -20",
 "description": "IEC context"
}
```


### [2026-09-05T14:27:48.357Z] TOOL RESULT

```
bhors- (2) «rough, violent Br. bar 'attack', cf. barrad-, cpds. “attack; storm’. W bâr, pl. baroedd ‘fury, trouble’; G barsch ‘harsh, tart'; Du. baars ‘raw’
bhətis, os ‘speech, declaration; speaking, spoken, declared". WP II, 123. Cf. bhaio, bhāmi Arm. baj, Let ‘verb’; Gk. phásis beside á- phatos ‘ineffable’; Lat. cf. in-fit (2) (quoth'. Plautus); in-fitiae ‘denial
bhəu- ‘please’. Cf. bhou- (3) Skt. cf. bhavilah ‘good; lecher’ beside (*ou) bhavitah *elated'; Per. cf. büye (s. “hope, de- sire"); (for Lat. faveo, ere, which is ambig.,
TI
cf. guhau-); Ir. babhaim ‘sweeten’; OE (*-ouio-) bywan ‘polish, adorn’. Cf. also Arm. bav e ‘suffices’ beside bavem ‘suffice’ and Cou) Pol. bawić, Cz. baviti se “amuse oneself. Cf. bhóu- (3)
bhouont-, bhount-, see bheuo, bhou (1) and bhü- Skt. bhavat “being; (an honorific title); OS -buandi ‘dweller’; ON büande, bonde *pea- sant?
bhoueot-, see bhóuot-
bhouos ‘construction, working, homestead’. WP II, 140. Cf. bheuo Skt. bhaváh; Arm. bov ‘furnace, forge, stove’, bovk, u-st. ‘mine’; Lat. favus ‘honeycomb, cell of h^; cf. also (?) favissae ‘basements’; MHG bou, gs. bouwes ‘homestead, building, cultivation, product; Du. bouw *construc- tion, culture'
bhi- (radical) ‘be’. WP II, 143 Per. bid (2pl. imperative "bel: Gk. cf. phi- tuo “produce, propagate'; OLat. fi! fite! (*be- .come'! Plaut.) (Lat. fio usually interpreted as if fr. *bhui-); OIr. bíu “am”; Ir. cf. bí-odh Tet him be"; OBr. bi! id.; MW bit! W bid! id.; OCS bimí, bi, bi (condit. ‘should be); OLi. bit, biti (3s. "was
bhi- (2). See bhiio (2); bhi- (3) see bhiió (1)
bhi, -bhi (3) ‘by, at”, instr. and (sometimes) loc. indicator as an inflexn. Vedic bhi-, px. (in bhi-sákmi *heal); Hind. bhi ‘also’; Tokh. A.B. pi, -pi “and, indeed, so’; Arm. -b, -v (instr. inflexion); Hitt. -pi (in kwa-pi any. where’, sanna-pi ‘in one place); Gk. -phi, Myc. -pi (in óresphi, thürephi, biejphi, dakru- óphi, iphi, etc.); Go. bi; MHG bi; OE bi, be (and comm. Gmc.)
bhíbhér-mi, bhíbhre-. See bheró Sk. bíbharmi; Hom. *píphr&mi (implied in es- phreso “shall introduce?)
bhid- (bhind-) ‘split’. WP II, 138 Skt. bhinádmi, v. beside bhida ‘cleavage’; Av. bid- (ambig. cf. *duid-); Arm. bit ‘spur of bird”; Lat. cf. findo, ére beside bi-fídus; Go. beitan (and comm. Gmc. *bite); MHG bizen beside biz “bite, wound, bit of horse: LG bitt, Du. bit; ON bit *bite, edge, bit, tiebeam' beside biti *bit, eyetooth'
=== bhou 3 ===
1289:bhouont-, bhount-, see bheuo, bhou (1) and bhü- Skt. bhavat “being; (an honorific title); OS -buandi ‘dweller’; ON büande, bonde *pea- sant?
1290:bhoueot-, see bhóuot-
1291:bhouos ‘construction, working, homestead’. WP II, 140. Cf. bheuo Skt. bhaváh; Arm. bov ‘furnace, forge, stove’, bovk, u-st. ‘mine’; Lat. favus ‘honeycomb, cell of h^; cf. also (?) favissae ‘basements’; MHG bou, gs. bouwes ‘homestead, building, cultivation, product; Du. bouw *construc- tion, culture'
1541:bhoudos, à, is ‘good, benefit, gain’. Cf. WP II, 186 Tokh. A pot-, B paut-, v. “honour, flatter beside Tokh. B (queried) pau$ye ‘tribute’; Mir. büad, búaid, Ir. buaidh “victory, success, virtue, glory; OBr. bud “profit; W budd,
1551:bhoudhos ‘awake; awakening’. Cf. bheudhó, bhudh- Skt. bodháh ‘awake, aware; awakening’; Cz. bud, id.
1552:bhoughos (?) “turn, bend, coil, ring; bent. Cf. WP II, 146 Skt. cf. (variant) bhogáh ‘curve, coil; Go. cf. us-baugjan, v. (sweep out', w. semantics of G aus-kehren); OHG boug, OE beag, ON bougr “ring, armlet; LW in OCS bugü, d: Latv. (?) bauga “weight on fishing-net
1553:bhoukətos ‘uproar’. WP II, 113. Cf. bhuk- W bugad ‘tumult’; Cz. (ambig.) bukot *bellow- ing'. See bhonk-
1554:bhoulos, ios, io “ball, lump’. Cf. bhaul- and bhül- Arm. (ambig.) bujlK, gp bulic ( ‘company; Pleiades’. See bhül-); W bul (i-st. *seed-ves- sel, bol); Cor. büly, pl.-yow ‘pebble’. The Gmc. and Sl. evidence is ambig., cf. Go. uf- bauljan ‘puff up’: Srb. buljiti (oči) “make big eyes; Slovene bula 'tumour; Cz. boule ‘Jump’; Pol. dim. bulka ‘blister’, etc.
1555:bhouquos (?) ‘buzzing insect. Cf. WP II, 113 Lat. cf. fücus ‘drone’; OE beaw ‘gadfly’
1556:bhouros (1) ‘raging, violent; violence’. Cf. bheuor- (bheur-), bhur- W (ambig.) bur, pl. -ion ‘violence’; OCS burja ‘storm’. Comm. Sl; Ukr. burytysja ‘clatter’; Late baurot ‘roar’
1557:bhouros (2), (bhur-) *dark, dun, brown, fal- low’. See bhur- Oss. būr, bor ‘dun, fawn, fallow’ (a substrate Eurasian wd. for Abaev); Kurd. bor ‘brown’; Gk. cf. porphurós, porphurá (adj. s. ‘purple’, fr. *bhur-bhur-, cf. Gk. mormúro, tolúpē, tonthorüzo for the dissimilation); It. (Gallo- Latin?) buro ‘dark’; Pol. bury ‘grey’; R buryj, Slovak bury ‘brown’
1558:bhoust- “lump, clump, bump, bulge’. WP II, 117 Lat. füstis ‘cudgel’; Olr. búas, Ir. buas ‘paunch, pouch’; W bus "Ip": QGallo-Lat. in) It. busto “bust”; ON beysti “ham. Variant in Cz. buchta ( bun, fr. *bhouksta?)
1561:bhou- (2), bhou- “heat, cook. Per. cf. bavarée (‘cook’, si: Arm. bov "fur, nace’; Hitt. cf. (queried) pawwanc ‘baked’; Arm. LW in Romani bov ‘stove’, but cf. bhouo-
1563:bhouon- (bhuuon-) ‘dwelling’. Cf. bheu-, bhóuont-, bhóu-, bhouos- Skt. bhavanam ���dwelling, existence’ beside bhuvanam ‘creature, being, world"; Arm. bujn, gs. buno ‘dwelling; nest; Alb. banë, f. ‘dwelling’; MIr. and Ir. buan ‘lasting’; Go. bauan, inf. ‘dwell’ beside bauains ‘dwelling’; OE bone ‘cultivated, occupied’; Cz. buné ‘cell’. Cf. WP II, 140
```


## [2026-09-05T14:27:49.601Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index of line 1286\nidx=sum(len(l)+1 for l in lines[:1285])\nprint('formfeeds before:', t[:idx].count('\\f'))\nprint('total ff', t.count('\\f'))\nEOF",
 "description": "Find IEC leaf for line 1286"
}
```


### [2026-09-05T14:27:51.592Z] TOOL RESULT

```
formfeeds before: 56
total ff 857
```


## [2026-09-05T14:28:03.904Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (54,55,56,57):\n    L=leaves[i]\n    print('=== leaf',i,'len',len(L))\n    print(L[:300].replace('\\n',' | '))\n    print('...TAIL:', L[-200:].replace('\\n',' | '))\nEOF",
 "description": "Inspect IEC leaves 54-57"
}
```


### [2026-09-05T14:28:06.128Z] TOOL RESULT

```
=== leaf 54 len 3443
bieluń; Cz. blín, id. | bhelguh- (?) Um b. cf. felsva (Cbursary' or sim.); LLat. fellus (a measure); MHG béáélgen ‘swell | bhelĝ- ‘rampage, play the fool; befool’. Cf. ble&ho Hes. cf. phelgünó ‘play the fool’; Rum. substr. bleg "limp; silly; E to bilk ‘cheat; Latv. belZu, belzt “buffet, bang'. O-grade i
...TAIL:  WP II, 172 Skt. barhe “cover (zero-grade in brhami 'strengthen"); Oss. cf. ám-bürzín (‘cover’, fr. *som-bherghio); OHG bergan, OE beorgan; Du. bergen; ON bjarga beside birgja; Sw. ber- ga sig “manage
=== leaf 55 len 3473
; refrain’; OCS brégo, brěšti *care for, protect | bherghos 'strong place' (identified in Gmc. with bhergh- and bhréh-, q.v.) W cf. bre “hill, top? (fr. *bhregh-); MHG berc, -ges ‘bulwark, enclosure’; OE beorg *protec- tion, refuge’; ON cf. birgr (*well-provided', fr. *-ghio-); OCS brégü (*shore, bank
...TAIL: bhártum, inf.; Gk. phertós ‘bearable’; Lat. fertus; MIr. bert, Ir. beart ‘burden’; OBr. cf. aperth (for *at-berth “sacrifice'): W ad- ferth ‘comfort’; OHG bérd ‘progeny’: OE cf. beorbor, n. -es- st. �
=== leaf 56 len 3455
��childbirth; newborn child" | bherulà (bherlà) ‘stick, staff. Cf. bhero Lat. ferula; Cz. berla ‘crutch’. (A semantic link with bherió is also possible) | bheruàá “edible herb’. Cf. bheruo Skt. cf. sü-bharvah *well-fed'; bharvami "eat": Lat. cf. conferva (comfrey'. Calque on Gk. sum-phüton), beside dial
...TAIL: es’ beside bavem ‘suffice’ and Cou) Pol. bawić, Cz. baviti se “amuse oneself. Cf. bhóu- (3) | bhouont-, bhount-, see bheuo, bhou (1) and bhü- Skt. bhavat “being; (an honorific title); OS -buandi ‘dwelle
=== leaf 57 len 3393
r’; ON büande, bonde *pea- sant? | bhoueot-, see bhóuot- | bhouos ‘construction, working, homestead’. WP II, 140. Cf. bheuo Skt. bhaváh; Arm. bov ‘furnace, forge, stove’, bovk, u-st. ‘mine’; Lat. favus ‘honeycomb, cell of h^; cf. also (?) favissae ‘basements’; MHG bou, gs. bouwes ‘homestead, building, c
...TAIL: . Variant (*bhigol-) in MHG bickel *pickaxe': Latvian bigulis “poker? | bhig- ‘speck, point Arm. bic 'spot, stain, crumb'; Du. bik 'stone chip’; G cf. Bickel ‘pimple’ | bhiio ‘fear’. Cf. bhïið (2) Skt. bh
```


## [2026-09-05T14:28:35.756Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=1200 && NR<=1600 && length($0)<8 {print NR\": [\"$0\"]\"}' IEC.txt | head -40",
 "description": "Find short lines (page numbers) in IEC"
}
```


### [2026-09-05T14:28:39.001Z] TOOL RESULT

```
1216: [10]
1217: [20]
1218: [25]
1219: [30]
1220: [35]
1221: [40]
1222: [45]
1223: [72]
1241: [20]
1242: [25]
1243: [30]
1244: [35]
1245: [40]
1246: [45]
1256: [" bhero]
1269: [20]
1270: [25]
1271: [30]
1272: [35]
1273: [40]
1274: [45]
1275: [76]
1287: [TI]
1297: [place,]
1299: [15]
1300: [20]
1301: [25]
1302: [30]
1303: [35]
1304: [40]
1305: [45]
1306: [78]
1328: [10]
1329: [20]
1330: [25]
1331: [30]
1332: [35]
1333: [40]
1334: [45]
1353: [10]
```


## [2026-09-05T14:28:46.332Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=1200 && NR<=2200 && $0 ~ /^(9[0-9]|10[0-5])$/ {print NR\": \"$0}' IEC.txt",
 "description": "Locate page 90-105 markers in IEC"
}
```


### [2026-09-05T14:28:47.797Z] TOOL RESULT

```
1480: 90
1549: 96
1559: 97
1606: 100
1616: 101
1634: 102
1645: 103
1666: 104
1677: 105
```


## [2026-09-05T14:28:50.093Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 1559,1606p IEC.txt",
 "description": "IEC pages 98-99"
}
```


### [2026-09-05T14:28:50.144Z] TOOL RESULT

```
97
bhóu- (1) “being, place, dwelling’. See bhauos Skt. bhavah; W bu ‘being’; cf. Srb. baviti se; Cz. bavit; Pol. bawić (2) ‘tarry’; Hitt. (queried) paww- (odge', cf. bhau-)
bhou- (2), bhou- “heat, cook. Per. cf. bavarée (‘cook’, si: Arm. bov "fur, nace’; Hitt. cf. (queried) pawwanc ‘baked’; Arm. LW in Romani bov ‘stove’, but cf. bhouo-
bhóu- (3), bhou- “joy, satisfaction’. See bhou- Skt. cf. bhàvitah *well-disposed'; Arm. cf. bav ‘enough’; bavem beside bovem, bujem "eut. fice’; Per. büya, s. “hope, desire’; Pol. ba- wić, Cz. bavit 'amuse'; Cz. zá-bava famuse- ment’; vy-bava 'endowment; Srb. u-bav “handsome. (For bhou- cf. also Ir. babhaim ‘sweeten’; OE bywan for *beawian ‘adorn’. For Lat. faveo, favor see guhau-)
bhouon- (bhuuon-) ‘dwelling’. Cf. bheu-, bhóuont-, bhóu-, bhouos- Skt. bhavanam ���dwelling, existence’ beside bhuvanam ‘creature, being, world"; Arm. bujn, gs. buno ‘dwelling; nest; Alb. banë, f. ‘dwelling’; MIr. and Ir. buan ‘lasting’; Go. bauan, inf. ‘dwell’ beside bauains ‘dwelling’; OE bone ‘cultivated, occupied’; Cz. buné ‘cell’. Cf. WP II, 140
bhóuont- “master, lord’. See next Skt. bhavan, bhavat- (a title); ON büandi, bóandi, bóndi “master”
bhõuət- (bhouot, bhuót-) ‘being’. Cf. bhü-, bhüt-, bhouos Skt. bhávithab, bhavat, bhàvatabh, bhautah; Gk. phós, gs photós, gp. photón "human being.. Cf. the variant in MHG ge-buode, buode, snf. “building; hut; LW in Finn. puoti “shop? (*-o-) All three variants are present in the Gmc. vbs. Go. bauan, OSw. bo, boa, MHG bouwen, and MHG büwen, ON büa
bhrado, io ‘clamour, din, revel, chatter’. Cf. brad- Gk. phrázo, aor. éphradon ‘declare’; Upper G prassen ‘revel’; cf. Scots brattle “dash, rush’; MLG braten (‘chatter’, if not HG)
bhragio *bleat, bray’ (?). Evidence uncertain.
10
15
20
25
30
35
40
45
bhóu- — bhragð ið 98
Cf. bragið G (LG) braken ‘scold’; Sw. bräcka ‘bleat
bhrāgos, å ‘mess, mash, swill, mire” Hes. (Thrac. or Phryg.) brágos ‘marsh’; MHG bruoch ‘marsh’; LW in It. brago, id. & Fr. brai, id. (Gallo-Lat.?); EMDu. broek ‘marsh’; R brága ‘barley and millet brew’; Ukr. braha ‘mash’; LW in Rum. bragă ‘drink of mille? beside brahă (id. and ‘malt, sediment’); Li. brogà ‘dregs, barm’; Latv. brāga “lees, swill. Cf. bhrak- & bhraK-
bhrag- ‘break; breaking; breaker. WP II, 193. Cf. bhrago, bhraĝmn-, etc. Skt. bhraj, adj.; Lat. cf. nau-fragium; W brai ‘outbreak’; Br. braé *flax-breaker'; Go. brakja ‘struggle’; MHG brach ‘din’; Ger. Brack “lack; rubbish; breech; brackish water’; adj. *thickset beside Brach ‘fallow land’; Brake ‘flax-breaker’; LG brak, id.; OE bræc ‘fallow- land; din’; EME brack ‘vice, fault’; Du brak ‘brat’: adj. ‘brackish’; ON brak ‘creak, crack’; Sw. brak ‘bang’
bhrāĝ- (long-grade variant of bhraĝ-) Sw. brokig ‘motley’; Latv. braZu, brazt “blast, bluster’ beside brāzma ‘gust, bang’
bhragaio (denom. cf. bhra&-, bhrago) Lat. cf. nau-fragó, are; OS brakon ‘crash’
bhra£&ol- Lat. cf. fragílis; W bral ‘rag, shred’; OE cf. braeclian ‘crackle’
bhra$mn- (1) “break, break-up, breakdown'. See bhra$o, ið k Alb. brâm “lees of wax’; Lat. fragmen ‘scrap’; (LLat. also *breakage, refraction, broken speech’); Br. cf. di-framm ‘rupture, breach?
bhragmn- (2), (bhragimn-) ‘noise’ (semantic extn. of (D) ` Alb. brazém, id. (fr. *bhragimn-); Br. bramm, Cor. bram ‘fart; W bram ‘puff; Ir. cf. bra- maim (v. ‘fart) beside MIr. braigim, id.; (-à-): Latv. brāzma ‘bang, bluster’. See next
bhra$no- ‘broken; fragment’. Cf. bhrag- Mir & Ir. bran ‘chaff, bran’; Br. brein, W braen ‘rotten’; OBr. cf. ar-ci-brenou, adj. pl. ‘rotten’; ON brakan ‘creak, crack’; Ger. cf. Brack ‘rubbish’. Gallo-Lat. substrate in Fr. bran ‘bran’
bhra$ó, ið “break? (verbal forms. Cf. bhrag-
99 bhrags- — bhrédho
and derivs.). WP IT, 193 Lat. cf. frango beside OLat. frago; Mir braigim ‘fart’; Br. braéa ‘bruise’; G brachen “break up (a fallow)'; G fr. LG braken ‘break (flax)'; Icel. braka ‘creak’; Sw. braka ‘bang’
bhrags- (extn. of bhra£-, q.v.) Alb. brash ‘tiny’; G Brachse ‘chopper’; EME brash ‘bout, fit’; adj. ‘brittle’; Du. cf. bras- sen ‘live riotousiy’; Li. brakšiù, et ‘crunch, crackle’; Latv. brakstēt, brakšķēt ‘rumble, crash’
bhraĝtos, bhraktos (variant: bhragst-) (1). See bhrag- Lat. fractus; Mir bracht ‘breaking, reaping’; W brath “stab, bite, sting; MHG braht, breht ‘uproar’; Icel. brattur, Norw. bratt, adj. ‘steep’; OS cf. brahtom, OE breahtm ('din', fr. *bhragtomo-)
bhragtos, bhraktos (2) “anger” Ir bracht, id.; Ger. Brast “sorrow, anger (fr. *bhragst-)
bhráió (?). See bhrõið ‘seethe’
bhràák- ‘stir, cloud, muddle’. Cf. bhrakK- Ir. brácaim (3) "maul R brak (2) ‘trash’; Li. brokëtu & broskiu, inf. brokšti ‘churn ` up; grow dim’; Srb. cf. brace “lees of grape- skins’ (fr. *bhráktio). (Isophonic are Ir. brá- caim ‘hack’: Latv. brāķēt)
bhrakt- ‘sap, dye’ Ir. bracht ‘sap’; OCS brosSti ‘red dye’. (Chance likeness w. Gk. brótos ‘gore’ is of no sig- nificance. Gallo-Lat. bractea, brattea, f. *metal-foil' appears to be unrelated)
bhraKos, is “lees, mash, waste’. Cf. bhràgos. WP I, 856 & II, 282 Lat. fracés, pl.; Gallo-Lat. braces, bracis ‘malt’;
Olr. brach, Mlr. braich, mraich, Ir. braich, .
id. beside MIr. braches (mash, pigfood', fr. *bhrakist-); W brag, Cor. brag *malt'; OBr. cf. brac-aut (a fermented drink: W bragod, id.); OR bros *hemp-waste, flax-bolls' beside R ot-bros “refuse, rubbish'. Verbal forms in- clude Lat. fraceo ‘ro? and R bro$ü, brósit "throw, reject? (cf. Lat. fracés in sense of *rubbish") bhrális (pet-form of bhrater-, q.v.)
Romani phral (ambig. Perh.: R brat); Sard. frale; Li. brólis; Latv. bralis, id.
10
20
25
30
35
40
45
100
```


## [2026-09-05T14:29:16.191Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la MON_part1.txt MON_part2.txt incoming/MON/ 2>/dev/null | head; echo \"=== search بویه ===\"; grep -n \"بویه\" MON_part1.txt | head -10; echo \"=== bimeh ===\"; grep -n \"بیمه\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Grep Mo'in for buyeh/bimeh"
}
```


### [2026-09-05T14:29:16.296Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt

incoming/MON/:
total 48684
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
=== search بویه ===
264:۲ - بسرگزید؛ نثر فارسی شمار؛ اول (دوره‌های سامانیان و آل‌بویه) 
282:سامانیان و آل‌بویه). چاپ اول ۱ ۰۱۳۳ چاپ دوم ۰۱۳۳۴ 
2458:آذریسو ت«- (- آذربویه] (امر.) (گیا.) 
24744:بلال: [۵۱2 ۱ - بلار ! (آ.) (کیا.) آذربویه 
26242:بویه: (05۷0) (.) آرزومندی. 
69641:ریسحانی» نازبویه. رزق» روزی. رحمت. 
95681:آورند. عرق بادرنجبویه: (پز.) مایعی که از 
95682:تقطیر جوشاندة بادرنجبویه در آب حاصل 
=== bimeh ===
MON_part1.txt:27258:صورتی که موضوع بیمه گذاشته به نحوی از 
MON_part1.txt:27260:خسارت برآید. بیمه شامل موارد ذیل 
MON_part1.txt:27262:حریق» بیمةً سرقت و غیره. شرکت بیمه: 
MON_part1.txt:27264:را در مقابل خطر ها و حوادث بیمه کند. 
MON_part1.txt:27265:بیمه کننده: (6-)100۵002-.۵ [هند. ف.] (افا. 
MON_part1.txt:27268:حوادث بیمه کند. 
MON_part1.txt:27270:بیمه گذار: 9-۲ [- یمه گذار نده] (افا.) 
MON_part1.txt:27272:موّسسه یا شرکت بیمه» بیمه کند. 
MON_part1.txt:47949:بیوفایی» بیمهر ی.
```


## [2026-09-05T14:29:19.231Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 27248,27275p MON_part1.txt; echo \"=== buyeh ===\"; sed -n 26236,26252p MON_part1.txt",
 "description": "Mo'in entries for bimeh and buyeh"
}
```


### [2026-09-05T14:29:19.300Z] TOOL RESULT

```
بیمر: 27[ (ص‌مر.) بیشمار» بی حد» 
۱ 

سیمناک: ۹( (ص‌مر.) تر سنده» 
بیم‌دارنده. ترسناکک» ترس آور. 


یمه (0-)۱۵آ۵ [اردو وهند. < سیماه 
ضمانت] (.) عملی است که اشخاص با 
پرداخت وجهی قراردادی منعقد کنند که در 
صورتی که موضوع بیمه گذاشته به نحوی از 
انحاء در مخاطره افتد» شرکت سمه از عهدة 
خسارت برآید. بیمه شامل موارد ذیل 
می‌شود: بیمةً عمر) بيمةٌ اعضای بدن؛ بيمة 
حریق» بیمةً سرقت و غیره. شرکت بیمه: 
شرکتی که اشخاص و موّسسات و اموال آنها 
را در مقابل خطر ها و حوادث بیمه کند. 
بیمه کننده: (6-)100۵002-.۵ [هند. ف.] (افا. 
اس) شرکت یا بنگاهی که اشخاص و 
مسسات و اموال آنها را در مقابل خطرها و 
حوادث بیمه کند. 

بیمه گذار: 9-۲ [- یمه گذار نده] (افا.) 
کسی که سرمایه با کالا يا جان خود را نزد 
موّسسه یا شرکت بیمه» بیمه کند. 

بین: (۷«)۵د9 [ع.] (امص.) جدایی. (.) 
میان» وسط. فاصلة دو چیز. 
=== buyeh ===
دارای رایبحه» بابوی. (امر.) سگ شکاری» 
توی بر ب: 

بو یدان: 00-27 (امسر.) ظرفیکه در آن 
چیزهای معطر نهند. ۱ 
بوی‌سوز: 0.902 (امر.) مجمرء آتشدان. 
بویه: (05۷0) (.) آرزومندی. 


بوییدن 


فر هنک فارسی معین 


۳۹۵
```


## [2026-09-05T14:29:40.199Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=1 && $0 ~ /^(72[0-9])$/ {print NR\": \"$0}' IEC.txt | head; echo \"---\"; awk '$0 ~ /^(156[0-9])$/ {print NR\": \"$0}' IEC.txt | head",
 "description": "Locate IEC pages 723 and 1562"
}
```


### [2026-09-05T14:29:41.953Z] TOOL RESULT

```
10183: 720
10194: 721
10223: 723
10235: 724
10256: 726
10263: 727
10281: 728
10550: 721
---
```


## [2026-09-05T14:29:45.469Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 10195,10235p IEC.txt | grep -n \"uid\\|ueid\\|weid\\|uoid\" ; echo \"=== raw ===\"; sed -n 10210,10236p IEC.txt | cut -c1-260",
 "description": "IEC page 723 content"
}
```


### [2026-09-05T14:29:45.536Z] TOOL RESULT

```
32:-mà (formative suffix of nouns derived from verbal roots) Skt. bhi-maà ‘fear’; Per. bi-me ('insurance', fr. *uid-ma?); Gk. fé-me, f. ‘rumour’; Lat. fa-ma, id.; Alb. fry-m& ‘breath’; å-më (Cscent': Gk. os-mé, od-mé, cf. Latv. os-ma ‘smell’, fr. *ods- ma); Go. hliu-ma, f. ‘fame’; ON i-ma ‘strife’; Sw. fet-ma 'fattiness'; Cz. R kos-ma, kosmà ‘tress’; Fris. great-me 'big-ness'; Li. važ-mà ‘freight’; Latv. draus-ma “threat, fear’; dzies- ma ‘song’, etc. etc. Cf. WP II, 123
=== raw ===
lutos, om (2) ‘mud’
Lat. lutum ‘mud’; MIr. Ir. toth, m. id.; Alb. cf. [uc&, f. id. (fr. *lutio)
lütos, om, à ‘tawny; tawniness, yellowness; tawny creature’.
Skt. luta ((2) “a skin-disease; (?) leprosy’); Lat. lūtum ‘yellow dye’; ON lúða, f. ‘halibut’; Li. liútas, m. “lion?
(lutros, radical extn. of type leuto, leutos,
q. v.) G Luder, n. ‘carcase; abomination’; OE loper, m. ‘rake, scatterbrain’; loprung ‘delusion’; Du. lodder, m. ‘rake, debauchee’. Cf. also Ger. lüderlich (dial. form of liederlich ‘wanton’)
luuð (1) “strike, destroy’. Cf. leuis (2)
Lat. cf. luēs, gs -is, f. ‘plague’; ON lýja, pp.. lüinn ‘beat, bruise’; mod. lýja, v. ‘tire’; túi, m. ‘fatigue’; Li. liüvis, gs -io, m. “break, pause, stoppage'. (Irish evidence ambig. cf. lobhaim, v. ‘putrefy’; but lot, m. ‘harm,
luuó (2), see léuio (2)
lks- (Isk-) (?) Cf. Isus Vedic rksáh ‘harmful’; Skt. “bare, bald; cut, pierced; G. cf. erloschen ‘extinguished’. (Iso- phone: Latv. ilkss 'sled-runner')
Imos, cf. elim-, əlim- ‘elm’. Cf. WP I, 152 Lat. ulmus, f., id.; OE ulm-treow, id.; G Ulme, id. (OFr. Fr. orme suggests a non-European origin, with -r- for -l-, cf. Basque zarika A Lat. salicem)
Isus ‘sluggish, tired; sluggishness'
Gk. álus, gs áluos, m. f. (2) ‘boredom’; Li. ilsüs, alsüs “boring, trying; feeble’
723
-m, suffix of direction Skt. cf. kama-m "at will; Gk. dómo-n beside dómonde; Lat. domu-m; OHG inna-n *in- ward’; Sw. utan ‘from outside; without’; frá-n "away": EMLi. namó-n ‘homeward’; aikstë-n ‘outward’; akrüta-n ‘to the ship’. (For S
má (a sentence-particle: “indeed, do, so, yet, but, if). WP II, 685. Cf. man, mar, men (2) Oss ma (*do', as reinforcement to verb); Hitt. -ma, suff. “yet, but; mà-, px. ‘if; Thess. má ‘but’; Gk. mà “yea, nay, indeed’; Mir má "if; Br. ma, id
-mà (formative suffix of nouns derived from verbal roots) Skt. bhi-maà ‘fear’; Per. bi-me ('insurance', fr. *uid-ma?); Gk. fé-me, f. ‘rumour’; Lat. fa-ma, id.; Alb. fry-m& ‘breath’; å-më (Cscent': Gk. os-mé, od-mé, cf. Latv. os-ma ‘smell�
mad- (1) “feed; food". WP II, 232, 262-70, 689 Gk. cf. máza, Doric mádda, f. ‘cake’; Alb. cf. maj, pp: majmë “feed, fatten’ beside gur-máz, -mac, m. ('throat, jaws’, if. fr. *gur-, cf. guer-, and *madio-); Go. mats, Let, m. “food, meal’; ME
mad- (2) 'cut, break
-m — máàdh-
15
20
25
30
40
724
Ir. maidhim, archaic p.t. meamaidh, v. ‘break’; OHG mezzo, wm. ‘stonemason’; MHG metz, metze, sn. ‘knife’; cf. OE mattuc, m. ‘mattock’
```


## [2026-09-05T14:29:57.572Z] TOOL CALL #39: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-05T14:29:57.582Z] TOOL RESULT

```


```


## [2026-09-05T14:30:02.336Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eyh%E2%82%82-",
 "prompt": "Give the reconstructed root, its meaning, and all listed derivatives/descendants, especially Indo-Iranian (Sanskrit bhayate, bhima), Iranian (Avestan bay-, Persian bim, bak), and any note on Proto-Iranian *baiHmah."
}
```


## [2026-09-05T14:30:03.675Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85",
 "prompt": "Persian بیم: give the full etymology section (Middle Persian form, Proto-Iranian, PIE, cognates) verbatim as far as possible."
}
```


### [2026-09-05T14:30:09.327Z] TOOL RESULT

```
# Proto-Indo-European Root *bʰeyh₂-

## Reconstructed Root and Meaning

The root **\*bʰeyh₂-** has two primary etymologies:

1. **"To shake, tremble"** or **"to fear, be afraid"**
2. **"To strike, hit"** or **"to hew, cut"**

## Listed Indo-Iranian Descendants

The page documents these descendants:

**Proto-Indo-Iranian forms:**
- \*bʰáyHatay (mediopassive root present)
- \*bʰiHmás (forming adjective derivatives)
- \*bʰiHtás (forming adjective derivatives)

**Sanskrit attestations mentioned:**
The page notes Sanskrit भेम (bhema) as a "1pl.inj.act." form, though it doesn't explicitly list the modern Sanskrit forms you mentioned (bhayate, bhima).

## Key Derived Terms

The etymology traces descendants through Proto-Balto-Slavic, Proto-Celtic, Proto-Italic, and Proto-Germanic branches, with Latin *foedus* and various Slavic forms (*biti* "to beat") representing major reflexes of the "strike" sense.

**Note:** The page does not specifically address Persian *bim*, *bak*, or Proto-Iranian *baiHmah as you requested.
```


### [2026-09-05T14:30:10.543Z] TOOL RESULT

```
# Etymology of Persian بیم (bīm)

The word بیم derives from **Middle Persian** bym (/⁠bīm⁠/, "fear, fright, dread"), tracing back through several ancestral language stages.

**Proto-Iranian ancestry:** The Middle Persian form comes from Proto-Iranian *biHmáh, which itself descended from Proto-Indo-Iranian *bʰiHmás.

**Proto-Indo-European root:** The ultimate source is Proto-Indo-European *bʰeyh₂- meaning "to fear."

**Cognate languages:** The word shares common ancestry with:
- Avestan b(a)ii- ("to fear")
- Sanskrit बिभेति (bibheti, "to fear") and भीम (bhīmá, "fearful")
- Old Church Slavonic боꙗти (bojati, "to fear"), related to Russian бояться (bojatʹsja)
- Old English bifian ("to shiver")

This linguistic family demonstrates how the concept of fear was expressed across ancient Indo-European languages.
```


## [2026-09-05T14:30:16.628Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%DA%A9",
 "prompt": "Persian باک (bāk): give the etymology section in full — Middle Persian, Proto-Iranian, PIE root, and any cited authority (Horn, Cheung, Hasandust)."
}
```


## [2026-09-05T14:30:18.246Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1%D9%88",
 "prompt": "Persian ابرو (abru) 'eyebrow': give the etymology in full — Middle Persian form, Proto-Iranian, Avestan, PIE reconstruction, and the variant برو (borū)."
}
```


### [2026-09-05T14:30:23.056Z] TOOL RESULT

```
# Etymology of Persian باک (bāk)

## Etymology 1: Fear/Dread

**Middle Persian Origin:**
From Middle Persian /⁠wāk⁠/ or /⁠wāg⁠/, with "further etymology unknown."

**Proto-Iranian Development:**
Derived from Proto-Iranian *bā(ia)-ka-, itself originating from Proto-Iranian *baiH- ("to fear").

**Proto-Indo-European Root:**
Traces back to PIE *bʰeyh₂- ("to fear, be afraid").

**Comparative Evidence:**
The entry notes a cognate in Old Armenian վախեմ (vaxem).

**Cited Authorities:**
- Cheung, Johnny (2007) - *Etymological Dictionary of the Iranian Verb* - provides the PIE and Proto-Iranian reconstructions
- Rastorgujeva, V. S. and Edelʹman, D. I. (2003) - *Etimologičeskij slovarʹ iranskix jazykov* [Etymological Dictionary of Iranian Languages]

## Etymology 2: Gas Tank

Borrowed from Russian бак (bak), representing a modern loanword usage in Persian.
```


### [2026-09-05T14:30:24.375Z] TOOL RESULT

```
# Etymology of Persian ابرو (abru) - "eyebrow"

## Full Etymology Chain

**Middle Persian:** The word derives from Middle Persian *brūg* (written as blwk').

**Proto-Iranian:** This comes from Proto-Iranian *\*HbrúHs*, which represents an earlier stage of the language family.

**Proto-Indo-Iranian:** Further back, the form appears as *\*HbʰrúHs* in Proto-Indo-Iranian.

**Proto-Indo-European:** The ultimate root is reconstructed as PIE *\*h₃bʰrúHs*, representing the deepest recoverable ancestral form.

## Variant Form

An archaic and poetic alternative exists: **برو** (baru/borū), though the modern standard form remains ابرو.

## Cognates Across Languages

The etymological connection extends widely: Northern Kurdish *birû*, Ossetian *ærfyg*, Sanskrit *bhrū*, Old English *brū* (modern English "brow"), Ancient Greek *ophrús*, and Slavic cognates all trace to this same root, demonstrating the word's ancient Indo-European pedigree.
```


## [2026-09-05T14:30:32.553Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85%D9%87",
 "prompt": "Persian بیمه (bime) 'insurance': give the etymology in full (is it from Persian بیم + ه, or a loan from Hindi/Urdu बीमा / بیمہ?). Also any Hindi/Urdu entry etymology if shown."
}
```


## [2026-09-05T14:30:34.843Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs",
 "prompt": "Give the reconstruction, meaning, and descendants list (Indo-Iranian, Iranian, Germanic, Greek, Slavic, Baltic). Does the page connect it to 'bridge' / a 'log, beam' word?"
}
```


### [2026-09-05T14:30:39.566Z] TOOL RESULT

```
# Etymology of بیمه (bime)

The Persian word for "insurance" has a **complex, debated origin**:

## Primary Theory
The word may derive from Persian **بیم** (bim, meaning "fear"), with the suffix **ه** (-e) added.

## Alternative Theory
Given its documented use in the Mughal empire from at least the 1650s, it may originate from an **Indo-Aryan language** rather than Persian. The Sanskrit term **भीम** (bhīma, "fearful, frightening") presents a plausible parallel.

## Ultimate Source
Both Persian and Sanskrit terms trace back to **Proto-Indo-European** *bʰeyh₂- ("to fear"), suggesting a shared ancient root regardless of which immediate language source is correct.

The word traveled from South Asia throughout the Persianate world, with the first Iranian-authored attestation appearing in a memoir from 1801 about the author's time in India.

---

**Note:** The Wiktionary entry does not provide a separate Hindi/Urdu etymology section; these languages are listed as descendants of the Persian term rather than sources for it.
```


### [2026-09-05T14:30:41.313Z] TOOL RESULT

```
# Proto-Indo-European *h₃bʰrúHs - Reconstruction Summary

**Reconstruction:** *h₃bʰrúHs (feminine noun)

**Meaning:** Eyebrow

**Key Descendants:**
- **Indo-Iranian:** *HbʰrúHs
- **Iranian:** (covered under Indo-Iranian)
- **Germanic:** *brēwō and *brūwō
- **Greek:** *opʰrū́s (Ancient Greek ὀφρύς)
- **Slavic/Baltic:** *brū́ˀs (Proto-Balto-Slavic)

**Bridge/Beam Connection:** Yes, the page discusses a possible connection. It notes that "Proto-Germanic *brugjǭ ("bridge")" may derive from *h₃bʰruH-íh₂-s, suggesting the eyebrow root could relate to bridge terminology, though this remains uncertain. The etymology section indicates "if Gaulish brīuā ("bridge") is related... it would require the root to be *(h₃)bʰreh₁w-."

The connection appears speculative rather than definitively established, with the page marking the etymology as incomplete.
```


## [2026-09-05T14:30:46.447Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%DB%8C%D9%87",
 "prompt": "Persian بویه: is there an entry? Give its definition and etymology (relation to بوی 'smell' or to a root meaning 'desire')."
}
```


## [2026-09-05T14:30:48.389Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%DB%8C",
 "prompt": "Persian بوی: give all etymologies and senses. Does any sense mean 'hope, desire, expectation' (as in به بوی آنکه)? What is the etymology of بوی 'smell' (Middle Persian, Proto-Iranian, PIE root)?"
}
```


### [2026-09-05T14:30:54.749Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T14:31:00.049Z] TOOL RESULT

```
# Persian بوی: Etymology and Senses

## Senses

According to the Wiktionary entry, Persian **بوی** (buy) has one documented sense:

- **"smell, scent"**

The entry does not list any sense meaning 'hope, desire, or expectation'. The phrase you mention (به بوی آنکه) may use this word metaphorically, but that figurative usage isn't included in this dictionary source.

## Etymology

The documented etymology traces back through Middle Persian:

"Inherited from Middle Persian 𐫁𐫇𐫏 (bwy /⁠bōy⁠/, 'smell, scent; incense'). Akin to Old Armenian բոյր (boyr), an Iranian borrowing."

The entry does not provide information about Proto-Iranian or Proto-Indo-European roots. To trace the etymology further back beyond Middle Persian would require consulting historical linguistic resources not included in this Wiktionary page.
```


## [2026-09-05T14:31:06.978Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; echo \"=== ابرو ===\"; grep -n \"ابرو\" ARY_pages.txt | head -5; echo \"=== بیم ===\"; grep -n \"^بیم\\|بیم \" ARY_pages.txt | head -8; echo \"=== باک ===\"; grep -n \"باک\" ARY_pages.txt | head -5; echo \"=== بویه ===\"; grep -n \"بویه\" ARY_pages.txt | head -5; echo \"=== latin index BHRU/BHEI ===\"; grep -n -i \"BHRU\\|BHEI\\|BHOI\\|BHEU\" ARY_latin_index_pages.txt | head -20",
 "description": "Grep Aryanpur"
}
```


### [2026-09-05T14:31:07.082Z] TOOL RESULT

```
=== ابرو ===
=== بیم ===
4165:۴۳ ا/ بیم (به چم "ترس *باک")
=== باک ===
1599:هب ۸255 باکه امه
2772:اسپانیایی (8۸(7/3): اد ان انگلیسی (باکلنا8(/0): 3
3075:ْ باک (به چم "ترس" بیم") / ۱۸۷
4165:۴۳ ا/ بیم (به چم "ترس *باک")
4194:بازگشت به: باک
=== بویه ===
=== latin index BHRU/BHEI ===
2139:OYENBRYN NORWEGIAN) 559 3 BHROH, BHRUS :(SANSKRIT) <2 Sie
3017:BUCK: | 1183-1185 BIBHEITI
3159:BOBOR SLOVAK) Si jL1 BABHRUS (SANSKRIT) ny Sade
3265:sco ¢.lu 5 BHOIDH
3902:B23 gta Coad 661" 5 "pat slay pi 4) *BHEUDH: 64 aly bt rly cal obj dll et
4034:SKEAT:  (BHEUDH) 752, (BID) 59 BIOTAN, BITTEN
4041:aSp POKORNY J cul ols (ly 9b 41, *BHEUDH ,*BHEDH sla |) BARNHART ~
```


## [2026-09-05T14:31:10.456Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; awk 'BEGIN{RS=\"\\f\"} /باک \\(به چم/ {print \"LEAF:\"NR; print}' ARY_pages.txt | head -60",
 "description": "ARY bak entry"
}
```


## [2026-09-05T14:31:11.128Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n 4160,4200p ARY_pages.txt; echo \"=== OYENBRYN line ===\"; sed -n 2135,2145p ARY_latin_index_pages.txt",
 "description": "ARY bim entry + brow index"
}
```


### [2026-09-05T14:31:12.012Z] TOOL RESULT

```
LEAF:106
[pdf page 106]
یی
ْ باک (به چم "ترس" بیم") / ۱۸۷
هلندی (007۶). راد ید نا پسگشت‌ها شرا ان ۲
ایرلندی کهن (للولقا صا0): 0 84 208020
ولزی (/65((): اد دزان 5 (۷۷8۸۷5) تلا دا
آلبائی [ ی ۷ 40 (715558) :م02
0 (۷۲۴۸7۴) 28
4090 ما8
7 (۷۲8۸۷۴) :071078
5 (۷۲۳۸۷8) +57
-۷/11 :245 دم تم
فرهنگ معین + ۴۳۶
یادداشت:
چم این واژه در زبان لاتین: پارچه
اوستایی (/4۲23740):
۸ ,898075 ,8۸5075 پسگشت‌ها 5
پهلوی (۷1هاتزهه): 8112۸6۸ 1 11 0001 ۳ ۳
سانسکر یت (8۸79/7): لد ۷ ۱۱:۳۹ 7 (۲)8۸3083) دتل رلز م۳۳
۱2۱زا 1153186 . 0
چ آلمانی کهن (/0574۸ ۲/07 صان): برهان قاطع + ۳۳
1 3100228۸ ,81380 لفت‌نامه دهغدا: ۳۳۴
پروسی کهن (۸835140 قا0): 81۸7۷۷81 ۱
یادداشت. ۱
واژه‌ی یم نیز از همین ريشه است. ٍ
```


### [2026-09-05T14:31:12.067Z] TOOL RESULT

```
1 فریزی کهن (/0ا9ل۶۸ ۵۱۵): ۰ 1۲۲1۳1105 2 ۲۳8۳۵) م0 لیم
الما ی کهن 0870400 قبط صا۵): 7 (۲۳8۲۲۷) :(4ا2نام 77
ی برهان قاطع : ۳۳۶
اوستایی (4۳57/۷): ۰ بف۷1811۸ پهلری (471ا۸7): 57 ,85813
[pdf page 143]
۴۳ ا/ بیم (به چم "ترس *باک")

۱ ساسکربت (64(8/7): -78 ,۷18۸ پسگشت‌ها شش دنت
ارمنی (470481014۷): 3
برنانی 072510): 05 بقد 0018090 ۲ ار عاقه با
لاتین (7100همل): اد ان لغت‌نامه دهخدا: ۱ ۰ 0۲۲۵ یم
ایرلندی میانه (18/31 2ا4100): 7 برهان قاطع + ۳

فرهنگ معین ‎ :‏ - ۶۳۷
یادداشت.
چم این واژه در زبان ارملی؛ لاش) جمد.
[ 26
ارستایی (۸۲2574): ,3۸3588۳7 ,-۸11 8۷ لهستانی (0/7370): 150۸
۸ ,3380715 روسی (75314/۷): 50
پارسی باستان (۲8۲۵914/۷ ط01): 81287/871 صربی (۵07ا828): 807۸743
پهلری (1هالل۸ه): ,16 ,ااآظ برهمی (807784149۷): ید۱1۷۸
رال ند لیترانی (/77740۷4/): ,ات8۸ ,8۸126
سانسکریت (4۷58/7): ۰ 813171 ]811 وله ,21703
8 ,8181187 ,3111۸ 271۸۸ لترنی (لتی) (/147714): ,8۸715
برنانی (072870)(شاید) ‏ ۳1001 ,۳1008 58 ,8170085 2178
لاتین (14710)(شاید) را دی
ایسلندی کهن ((010۸۷24نف5 طا): پسگشت‌ها گرد رن
۸ ب818۸ 1 ۶002
۱ آلمانی کهن (/(0570/۸ ۱/017 صا0): 7 (8۸1(08۵)) :تا (ماط0
7 ,)8186 8 (8130) 2
انگلیسی کهن (37ا8۸۷0 012): 85077۸0 1153 8
اسلاوی کهن (۷72ما5 بل#تابن صال): برهان قاطع + ۱ ۳۴۰
0 8۸7۸7 807۸1 ,85055 :
یادداشت:
بازگشت به: باک
[pdf page 144]
نج
بینی / ۱۴۵
یکره دض
اوستایی (/4887۸4۸): ۷۸۲۰ ,۷۸5۸ نروژی (/۸/07775014): 5(
پارسی باستان (۲8۴۶۶4۸۷ ۰)010 ۰ ۲۸7۸۵۲ هلدی (017۳[4): ناد لا
=== OYENBRYN line ===
. sel ole
ub tt WA get
OJENBRYN DANISH) jails BRAVAT HAVESTAN) glrs\
OGONBRYN (SWEDISH) (5.8 yp BRUG, BRUK (PAHLAVI) 5 hy
OYENBRYN NORWEGIAN) 559 3 BHROH, BHRUS :(SANSKRIT) <2 Sie
OLD CHURCH SLAVIC) oS 59%! OPaRYS GREEK) gliy
BRUVI OLD SCANDINAVIAN) 2455-he!
BRWI POLISH) long) BRUN, BRA
BROV RUSSIAN) .g3 {OLD HIGH GERMAN) oS giell
oBotr CZECH) Sy BRUs, BRAWAs 7
OBRVA SERBIAN) «ype AUGENBRAVE, ° (GERMAN) st
```


## [2026-09-05T14:31:21.463Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; sed -n 2118,2160p ARY_latin_index_pages.txt; echo \"=== pdf page tags near ===\"; awk 'NR>=2050 && NR<=2160 && /pdf page/' ARY_latin_index_pages.txt",
 "description": "ARY abru entry context"
}
```


### [2026-09-05T14:31:23.090Z] TOOL RESULT

```
AMBER ENGLISH) gud AMB, AMP ARMENIAN) gal
OLD CHURCH SLAVIC) 55 53%! APHROS, OMBROS — (GREEK) (gly
OBLAKU IMBER, IMBRIS ALATIN) 3
OBLOK POLISH) ging) OMBRE (FRENCH) Wil},
[pdf page 76]
oa
WI szssyzl
: OBLAKO ARUSSIAN) «5+,
REFERENCES beth OBLAK (CZECH) Sx
= =
BARNHART: (NEBULA) 697 OBLAK SLOVAK) Sle
MACKENZIE: (CLOUD) 167 AMBRIA, CELTIC) ( gS) gh
BUCK: 3s AMBRA (GAULISH) iS
v4 igbi ob, AMIR, AMYR- WELSH) 69
ethos
Ge Desks Shabs 2 Js ctl eet
BY (A pel slay, pe Uae aly ol Gd9d Es hey AS y BUT hak 22-1
. sel ole
ub tt WA get
OJENBRYN DANISH) jails BRAVAT HAVESTAN) glrs\
OGONBRYN (SWEDISH) (5.8 yp BRUG, BRUK (PAHLAVI) 5 hy
OYENBRYN NORWEGIAN) 559 3 BHROH, BHRUS :(SANSKRIT) <2 Sie
OLD CHURCH SLAVIC) oS 59%! OPaRYS GREEK) gliy
BRUVI OLD SCANDINAVIAN) 2455-he!
BRWI POLISH) long) BRUN, BRA
BROV RUSSIAN) .g3 {OLD HIGH GERMAN) oS giell
oBotr CZECH) Sy BRUs, BRAWAs 7
OBRVA SERBIAN) «ype AUGENBRAVE, ° (GERMAN) st
OBRY (BOHEMIAN) goa BRAVE
oBoct SLOVAK) S11 BRU, {OLD ENGLISH) 46S:
BRUVIS LITHUANIAN) gi s-3 OFARBRU-
BRAUD (OLD IRISH) pS 5) EYEBROW, BROW :(ENGLISH) Si
[pdf page 77]
nt va
BUCK: 219 REFERENCES bantu
ONIONS: (BROW) 121 POKORNY = s—=<CS~*~‘S~™~*~«sD
SKEAT: . * GROW) 76 BARNHART: (BROW) 120-121
of be? % igbG oly DELAMARRE: (SOURCIL) 97
‘MACKENZIE: 20, (BROW) 105
Jeetloal
bal es alaal ste Shab; Sy 2 Sly ot!
RAD :(DUTCH) goska RATHO, RATHA —:(AVESTAN) (gl 3!
ROTHAS (LITHUANIAN) gly RH PAHLAVI) 6 gh
=== pdf page tags near ===
[pdf page 74]
[pdf page 75]
[pdf page 76]
[pdf page 77]
```


## [2026-09-05T14:31:37.126Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SKT brow ===\"; grep -n \"^Brow\\|Brow, the\\|Brow\\.\" SKT.txt | head -5; echo \"=== SKT bridge ===\"; grep -n \"^Bridge\" SKT.txt | head -5; echo \"=== KLN brow ===\"; grep -n -o \"brow, n\\..\\{0,600\\}\" KLN_1966.txt | head -3; echo \"=== KLN bridge ===\"; grep -n -o \"bridge, n\\..\\{0,600\\}\" KLN_1966.txt | head -3",
 "description": "Grep Skeat and Klein for brow/bridge"
}
```


### [2026-09-05T14:31:39.538Z] TOOL RESULT

```
=== SKT brow ===
1678:Boer.  (E)  M.  E  Arw.  A.  S.  *«fr-.+Du. and  G.  i^/>r;  I  eel.  bjdrr.  Probably  con- nected wiih  Brow.
2370:Browse.  (F..-M.  H.  G.)  A  corruption of  broust.^O.T.  brouster  (F-  brouttr').  to nibble  off  young  shoeti.  — O.  F.  bnniit  (F. br»tu),  a  sprig,  slioot,  bud.-*M.  H.  G  ^rvi« a  bnd  ;  Bavar.  brossi,  bress^  a  bud ,  tee Brash.
7143:Frond,  a  branch.  (L.)  L.  froHd-^  ttcm oi/'rvns,  a  leafy  lininch. Front.  (F.-L.)  M.  E. /n»«/,  forehead. —  O.  F.  frvHt,  forehead,  brow.  —  L.  /rvnt- tm,  ace  of  yVr/tr,  forehead,  btow.  Allied to  Brow.
=== SKT bridge ===
=== KLN brow ===
=== KLN bridge ===
```


## [2026-09-05T14:31:43.504Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"Brow\\.\\s*(E\\.)\\|Brow,  the\\|^Brow\" SKT.txt | head; echo \"---\"; grep -n \"ofr«s\\|bhrus\\|bhrü\\|OPHRYS\\|ophrus\\|ophrûs\" SKT.txt KLN_1966.txt KLN_1971.txt | head -20",
 "description": "Search Skeat/Klein for eyebrow root"
}
```


### [2026-09-05T14:31:43.601Z] TOOL RESULT

```
2370:Browse.  (F..-M.  H.  G.)  A  corruption of  broust.^O.T.  brouster  (F-  brouttr').  to nibble  off  young  shoeti.  — O.  F.  bnniit  (F. br»tu),  a  sprig,  slioot,  bud.-*M.  H.  G  ^rvi« a  bnd  ;  Bavar.  brossi,  bress^  a  bud ,  tee Brash.
22876:brown — bruin.
---
KLN_1966.txt:5585:bruasach,  ‘having  a  broad,  strong  breast’,  OIr. bruinne  (for  *bhrusnio-),  ‘breast’,  hr  it  (for *bhrusd-),  ‘abdomen,  belly’;  fr.  I.-E.  base *bhreus-,  ‘to  swell’.  Cp.  brisket,  browse. Derivatives:  breast,  tr.  and  intr.  v.,  breast-ed, adj.,  breast-er,  n.,  breast-ing,  n. breastsummer,  n.,  a  large  beam.  —  Compounded of  breast  and  summer,  ‘beam’, breath,  n.  —  ME.  breeth,  breth,  fr.  OE.  brxp,brep, ‘odor,  scent,  breath’,  rel.  to  OHG.,  brddam, MHG.  bradem,  G.  Brodem,  ‘breath,  steam’,  fr. I.-E.  base  bher-,  ‘to  boil’.  See  brew  and  cp. words  there  referred  to.
KLN_1966.txt:5734:bruin,  n.,  name  of  the  bear  in  fairy  tales.  —  Du. bruin,  ‘brown’.  See  brown.  For  sense  develop¬ ment  see  bear,  the  animal, bruise,  tr.  and  intr.  v.  —  ME.  brisen,  brusen,  a blend  of  OE.  brysan,  ‘to  crush,  bruise’,  and  OF. bruisier,  ‘to  break’.  Both  OE.  brysan  and  OF. bruisier  derive  fr.  I.-E.  base  *bhreus-,  *bhres-, ‘to  break,  crush,  crumble’,  whence  also  OIr. bronnaim  (for  *bhrusnami),  ‘I  wrong,  hurt’,  bris- sim,  ‘I  break’,  brisc,  ‘brittle’,  Bret,  bresk,  of s.m.,  brezel,  ‘war’,  VL.  brisare,  ‘to  break’,  a word  of  Celtic  origin  (whence  F.  briser,  of  s.m.), Mir.  brtiim,  ‘I  crush’,  OE.  berstan,  OS.,  OHG. brestan,  etc.,  ‘to  burst’,  and  prob.  also  L.  frus¬ tum  (fr.  *bhrus-to-),  ‘piece’,  Alb.  bresen,  ‘hail’. Cp.  I.-E.  *bhrousmen,  whence  OS.  brosma, OHG.  brosama,  brosma,  MHG.  broseme,  bros- me,  G.  Brosam,  Brosame,  ‘crumb’.  Cp.  debris, debruise.  Cp.  also  burst.  Cp.  also  frustum. Derivatives :  bruise,  n.,  bruis-er,  n.,  bruis-ing,  n. bruit,  n.,  noise;  rumor  (archaic).  —  F.  ‘noise’, orig.  pp.  of  bruire,  ‘to  rustle,  rumble’,  used  as  a noun.  F.  bruire  derives  fr.  VL.  *brugere,  which is  a  blend  of  L.  rugire,  ‘to  roar’,  with  VL.  *bra- gere,  ‘to  whine,  cry’  (whence  F.  braire,  ‘to  bray’ (see  bray,  ‘to  cry’).  L.  rugire  (whence  VL.  *ru- gere),  ‘to  roar’,  is  cogn.  with  Gk.  Epuystv,  ‘to bellow,  roar',  opufraySog,  ‘a  loud  noise’,  pu£etv (for  *p(>Yi£iv),  ‘to  growl,  snarl’,  OSlav.  rykati, ryknQti,  ‘to  roar,  bellow’,  OE.  ryn  (for  *ruhjan), OHG.  rohon,  of  s.m.
KLN_1966.txt:15482:frustum,  n.,  the  lower  part  of  a  solid  figure  formed when  the  top  of  a  cone  is  cut  off  parallel  to  the base.  —  L.,  ‘piece’,  fr.  I.-E.  *bhrus-to-,  fr.  base *bhreus-,  ‘to  break,  crush,  crumble’,  whence also  OE.  brysan,  ‘to  bruise’.  See  bruise, frutescent,  adj.,  shrubby.  —  Incorrectly  formed for  *fruticescent,  fr.  L.  frutex,  gen.  fruticis,  ‘a bush’.  See  next  word  and  -escent. frutex,  n.,  a  shrub.  —  L.,  ‘shrub,  bush’;  of  un¬ certain  origin.  Cp.  frutescent,  fruticose.  L.  Frutis, name  of  Venus,  is  not  related  to  L.  frutex  (see bride).
KLN_1971.txt:33429:bruinne (for *bhrusnio~), ‘breast’, bru (for 
KLN_1971.txt:33430:*bhruso~), ‘abdomen, belly’ ; fr. I.-E. base 
KLN_1971.txt:34494:bronnaim (for *bhrusnami\ ‘I wrong, hurt’, bris- 
KLN_1971.txt:34500:tum (fr. *bhrus-to-), ‘piece’. Alb. bresen , ‘hail’. 
KLN_1971.txt:98091:base. — L., ‘piece*, fr. I.-E. *bhrus-to-, fr. base
```


## [2026-09-05T14:31:48.522Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \".\\{0,200\\}brvat.\\{0,700\\}\" KLN_1966.txt KLN_1971.txt SKT.txt FSD_vol1.txt WEB_vol1.txt 2>/dev/null | head -8",
 "description": "Search English dicts for Avestan brvat"
}
```


### [2026-09-05T14:31:52.203Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:31:55.325Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"brow,  n\\..\\{0,700\\}\\|brow,  n\\..\\{0,700\\}\\|bridge,  n\\..\\{0,700\\}\" KLN_1966.txt | head -4; echo \"== try 1971 ==\"; grep -n \"^brow\\|^bridge\" KLN_1971.txt | head -10",
 "description": "Klein brow/bridge entries"
}
```


### [2026-09-05T14:31:56.829Z] TOOL RESULT

```
5629:bridge,  n.,  structure  spanning  a  river,  etc.  —  ME. brigge,  brig,  etc.,  fr.  OE.  brycg,  brieg,  rel.  to OS.  bruggia,  ON.  bryggja,  bru,  Dan.  bro,  Swed. brygga,  OFris.  brigge,  bregge,  Du.  brug,  OHG. brucca,  G.  Briicke;  prob.  orig.  ‘bridge  of  beams’, and  derived  fr.  I.-E.  base  *bhru-,  *bhreu-,  ‘beam, log’,  whence  also  Gaulish  briva,  ‘bridge’,  OSlav. bruvuno,  ‘beam’,  Serb,  brv,  ‘footbridge’. Derivatives:  bridge,  tr.  v.,  bridg-ed,  adj.,  bridg¬ ing,  n.
5630:bridge,  n.,  a  card  game  resembling  whist.  —  First mentioned  as  Biritch  or  Russian  Whist;  of  un¬ known  origin.
5731:brow,  n.  —  ME.  browe,  fr.  OE.  bru,  rel.  to  ON. brim,  ‘brow’,  and  cogn.  with  OI.  bhrtih,  Toch. A  pdrwdm  (dual),  Avestic  brvat-,  ModPers.  abrit, bru ,  Gk.  otppup,  OSlav.  bruvi,  Lith.  bruvis, ‘brow’,  OPruss.  wubri  (metathesis  fr.  *brwi), OIr.  bru,  ‘edge’,  Mir.  bruad,  ‘brow’.  OE.  brxw, ‘eyelid’,  is  not  related  to  brow  (see  brae), brown,  adj.  —  ME.  broun ,  fr.  OE.  brim,  rel.  to ON.  bninn,  Dan.,  Swed.  brun.  OS.,  OFris., OHG.,  MHG.  brim,  MDu.  bruun.  Du.  bruin, G.  braun,  ‘brown’,  and  cogn.  with  Russ,  bron, ‘white,  variegated’,  Gk.  (ppOvop,  ippuvT),  ‘toad’, (prop,  ‘the  brown  animal').  These  words  have been  enlarged — with 
== try 1971 ==
27438:brown. 
32918:brow’, Goth, brahaugins , ‘moment’, fr. I.-E. 
33756:bridge, n., structure spanning a river, etc. — ME. 
33767:bridge, n., a card game resembling whist. — First 
34433:brow, n. — ME. browe, fr. OE. bru, rel. to ON. 
34440:brown, adj. — ME. broun , fr. OE. brun , rel. to 
34454:brownie (q.v.), brown-ish , adj. 
34455:brownie, n., a good-natured goblin. — Formed 
34461:browse, tr. and intr. v., to feed on; to graze. — 
47304:bridge. — F. cintre , ‘curve, bend’, fr. cintrer, ‘to.
```


## [2026-09-05T14:32:09.662Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==173' POK_01.txt | head -20",
 "description": "POK next leaf for WP ref of bhoi-"
}
```


## [2026-09-05T14:32:10.825Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN eyebrow ===\"; grep -n -o \".\\{0,80\\}EYEBROW.\\{0,900\\}\" SYN.txt | head -3; echo \"=== SYN fear ===\"; grep -n -o \"FEAR.\\{0,400\\}\" SYN.txt | head -3",
 "description": "Buck synonyms eyebrow/fear"
}
```


### [2026-09-05T14:32:11.615Z] TOOL RESULT

```
*^  (von  "^Tiid-og  ,häßlich^,  schwundstuf.  *bhidh^
Lat.  foedus  (*bhoidhos)  ^häßlich,  abscheulich,  schändliche  v
Ahd.  biberiy  as.  bibön,  ags.  beofian,  aisl.  bifa,  -ada  und  bifra  (dies  i; Ausgang  nach  *titrön  ,zittern^  gerichtet)  zu  urg.  *bibai-mi',  *bibön  Jj wohl  erst  nach  dem  sonstigen  Nebeneinander  von  -ön-  und  -ew-Ver sekundär  neben  ein  aus  der  Perfektform  entwickeltes  *biben  getreten.
Bsl.  ursprgl.  Präsens  *bhdiö-y  Prät.-St.  *bhiiä-j  Inf.  *bhltei]  apr.  biät ,fürchten^,  kausat.  pobaiint  ,strafen^;  lit.  bijaus,  bijötis  (auch  nicht  reflexiv' ,sich  fürchten^,  lett.  bistuos,  bijuds,  bities  und  bijäjuos,  bijäties  ,sich  fürchten' lit.   baijils  ,furchtbar,  schrecklich,  abscheulich^;   baidaü,   -yti  ,scheuchen'^ lett.    baXdUj    baXdyt    und    biedet    ,schrecken^,    dazu    lit.    baisä    ,Sch recken' i^baid-s-ä),  baisüs  ,schrecklich,  greulich^,  baisiöti  ,beschmutzen,  beschmie- ren^ (und  aksl.  bäs^  , Teufel^,  *bH-s^)]   lit.  bdime  ,Furcht^;  bdiU  ds.  (bailus ,furchtsam^).
Aksl.  bojg,  bojati  s§  ,sich  fürchtend
Eine  Weiterbildung  *bhil-es-,   *bhis-    in    ai.  bhydsate    ,fürchtet    sicli^, udbhydsa-h  ,sich   fürchtend^,  av.  Perf.  biwivärdha   (d.  i.  biwyaTdha).  ,erregte    * Schrecken,  war  furchtbar^;   ai.  bhlsayate  ,schreckt^,   bhisana-h  ,Schrecken  -'■ erregend^;
ahd.  bisa  ,Nordostwind^,  bisön  ,toll  umherrenuen^,  beo'  ,Eber^  usw.  führen auf  ein  germ.  *6ts-,  *b'tz-  ,aufgeregt  einherstürmen^;  vgl.  Wißmann  Nom. postverb.  78.
WP.  II  124f.,  186,  WH.  I  522f.,  Trautmann  24,  Kluge^i  unter  Biese.
bhok-  ,flammen,  brennen^?
Lat. /oc2<s  , Feuerstätte,  Herd^;  vermutlich  zu  arm.  bosor  ,rot^  (,*feurig^)^| boc  ,Flamme^  (*bhok-s-o-). WP.  II  186,  WH.  I  521.
bholo-  etwa  ,Dunst,  Dampf,  warm  aufsteigender  Geruch'??
Es  vereinigen  sich  vielleicht  air.  bolad,  nir.  boladh  und  baladh  , Geruch' und  lett.  buls,  bula  , dunstige  schwüle  Luft,  Höhenrauch,  Dürre*^;  es  kann^ idg.  bhol-  (irisch)  :  öÄo^  (lett.)  zugrunde  liegen;  vielleicht  ist  mit  obiger; Etymologie  auch  Peterssons  Etym.  Miszellen  34  Verbindung  von  buls  mit- arm, bal  ,caligo'  (wenn  ursprgl.  ,Dunst')  kombinierbar?
WP.  II  189.
163
thorg"^'^  .barsch,  unfreundlich^
Vrin.  baj'k ,hehig,  zornig;  herb,  bitter,  scharf  von  Geschmack^  (Hhrguos)] ir.  borb,  borp  .töricht^;  mir.  borb  {Hurbo-,  idg.  Hhovguo-)  ,roh,  unwissend^, lett   baf-gs  ,streng,  hart,  unfreudlich,  unbarmherzig^;  schwed.  mdartl.  ba^^k ejcreiisinniger  unfreundlicher  Mensch^,  barkun  ,rauh,  barsche
```


### [2026-09-05T14:32:15.603Z] TOOL RESULT

```
=== SYN eyebrow ===
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,900}
                        \___exceeds complexity limits


=== SYN fear ===
29058:FEAR, FRIGHT Goth. agis, faurhtei Lith. baimeé, bailé, i8gqstis rk §to5, oe st ON atti, dgn, hrezla, Lett. bailes ; NG $6805, ai tus, pavor, skelkr ChSl.  strachit, bojaznt ot. timory Dan. frygt, skrak SCr.  strah, bojazan terror iinore;_ spe Sw. fruktan, skraéck Boh. _ strach, bdzer It. paura, d OE ege, egesa, fyrhto Pol. bojazi, strach, trwoga vento ainte, effrot ME fere, eye, frizt Russ. strach, bo
```


## [2026-09-05T14:32:23.213Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 29058,29075p SYN.txt | cut -c1-1500; echo \"=== brow in SYN ===\"; grep -n \"brow\" SYN.txt | head -8",
 "description": "Buck FEAR + eyebrow"
}
```


### [2026-09-05T14:32:23.284Z] TOOL RESULT

```
16.53 FEAR, FRIGHT Goth. agis, faurhtei Lith. baimeé, bailé, i8gqstis rk §to5, oe st ON atti, dgn, hrezla, Lett. bailes ; NG $6805, ai tus, pavor, skelkr ChSl.  strachit, bojaznt ot. timory Dan. frygt, skrak SCr.  strah, bojazan terror iinore;_ spe Sw. fruktan, skraéck Boh. _ strach, bdzer It. paura, d OE ege, egesa, fyrhto Pol. bojazi, strach, trwoga vento ainte, effrot ME fere, eye, frizt Russ. strach, bojazn’ peur ria pavura, NE fear, fright, terror Skt.  bhaya-, bhiti-, bhi-, Sp. pieeee ’ Du. vrees, schrik trasa- oe teamd, spaimd OHG  forhta, egi, egiso Av. Owaésah-, byah-, Rum. Ug ia MHG  vorht(e), ege, eis, tarSti- I ae faitcheas, schreke Nir. age han NHG _ furcht, schrecken
Ww. afm, dy chryn Br. 9M, efreiz
Words for ‘fear’ and the stronger (and in part more sudden) ‘fright, terror’ are mostly based upon those for physical ac- tions expressive of fear, especially ‘trem- ble, shake’, also ‘flee’, ‘be struck’, etc. Insome cases there has been a shift from the objective ‘danger’ to the subjective fear’, as, conversely, words for fear’ are often used objectively for what inspires fear, ‘a horror, a terror, danger’. Anim- portant cognate group is common to Balto-Slavic and Indo-Iranian.
1, Derivs. of IE *bhai-(?), *bhi- in Balto-Slavic and Indo-Iranian words for ‘fear’, prob. (though disputed) the same zit as in OF beofian, OHG bibén, etc. shake, tremble’ (redupl. formation). Walde-P, 2.194 f. Falk-Torp 125. Wei- gand-H, 1.173. Berneker 68. ne lg bailé (also baisa ‘fright’, bail aan tful’, fr. *bai-d-s-), Lett. et, ae ‘4 ~ bailes); ChSl. bojazni, ie peayic; Skt. bhaya-, bhiti-, Bee ae. ane (s-extension) ; vb. forms byents Urighten? » Ay. 8pl. bayente, bijoti(s), an eres brine, Lith. Tati se ete rate » bij at(zes), ChSl.
; , be afraid’.
'. Gr 5 L AS 8 terroy? tie (latter often obj. °F attested ] Vb. del5u (fr. *Be-d¢o10;
a 1 eS SO in Hom. éddecce and
Corinth. Arevias) : Av. dvaééa- ‘threat’ and Skt. dvis- ‘hate’ (cf. 16.41).
Grk. ¢6Bos, orig. ‘flight’ (still the only sense in Hom.), hence ‘panic, fright’ and eventually the most common word for ‘fear’ : PéBouat ‘flee’, Lith. bégit ‘run, flee’, etc. Walde-P. 2.148 f.
Grk. tpéunos ‘a trembling’, esp. with fear, whence NG ‘terror, fright’ : rpéuw, Lat. tremere ‘tremble’, Lith. trimti ‘shake’, IE *trem- beside *tres- in Skt. iras- ‘tremble, be afraid’, Grk. rpew ‘tremble, flee’, Lat. terrére ‘terrify’, terror ‘terror’. Walde-P. 1.785. Er- nout-M. 1054.
3. Lat. timor (> It. timore, Sp. temor, ORum. temoare), with vb. timére (> It. temere, Sp. temer, Rum. teme, whence Rum. sb. teamd), etym. dub. Walde-P. 2.611. Ernout-M. 1040.
Lat. metus (> Sp. miedo), hence me- tuere ‘fear’, etym. dub., possibly : ChSl. motati se ‘be disturbed, moved’, Grk. udb0s ‘battle-din’, ete. Walde-P. 2.269. Wood, Cl. Pl. 5.306.
Lat. pavor, orig. ‘a shaking, quaking’ with emotion, esp. with fear, hence ‘alarm, dread, fear’ (> OFr. paor, Fr. peur; with change of suffix It. paura, Sp. pavura), with vb. pavére ‘be struck with fear, tremble, quake with fear’, prob.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1154
orig. ‘be struck’ : pavire ‘beat, strike’. Ernout-M. 743. REW 6314.
Lat. terror (> It. terrore, Fr. terreur, etc., NE terror), see above under Grk. Tpopos.
=== brow in SYN ===
1185:Ir. bri, bruach (also and orig. ‘edge’) : Lith. briauna ‘edge’, prob. also OF bra ‘brow’, etc. Walde-P. 2.196, 207. Pe- dersen 1.62.
1970:3. Ir. cdo (gen. ciach), NIv. ceo, perh. : Ir. ciar ‘dark brown’, OF har ‘gray’ (NE hoar), ete. Walde-P. 1.360.
3760:Color words underlie some, as ‘brown’ in the Gme. words for ‘bear’ (3.73) and an IE word for ‘beaver’ (NE beaver, etc.); ‘gray’ in Lith. pelé ‘mouse’ (3.63) and prob. a widespread word for ‘hare’
4967:the general Gmc. word : Lith. béras ‘brown’, OE Obriin ‘brown’, ete. Walde-P. 1.166. Falk-Torp 77.
4987:Gme. word, prob. : Skt. puccha- ‘tail’, Walde-P. 2.82. Falk-Torp 281. Feist 144. Cf. Sp. raposa and W. llwynog. ON refr (masc.), Dan. rev, Sw. rdv, perh. as ‘red’: ON jarpr ‘brown ’,OE eorp ‘darkish’, etc. Walde-P. 1.146. Falk-Torp 931. Hellquist 871.
5004:Skt. harina-, deriv. of hari- ‘reddish brown’.
5031:6. Skt. kapi- : kapila- ‘brownish, red- dish’, fr. ‘smoke-colored, Grk. xamvés, etc.? Walde-P. 1.379. Prob. source of Egypt. gephi, Grk. xios, xfBos, etc. Schrader, Reallex. 1.16.
5683:k. éremrov Goth. Lith. kakta a Meee xobredo ON enni Lett. piere Lat. frons Dan. pande ChSl. éelo It. fronte Sw. panna SCr. elo Fr. front OE Sorhéafod _ Boh.  &elo Sp. _ frente ME _forhe(ue)de Pol. _—_czolo Rum. frunte NE forehead (brow) Russ. lob (“elo) Ir. étan, tul Du. voorhoofd Skt. bhala- Nir. clar a éadain OHG - stirna, linna, andi Av. ainika- W. talcen MHG stirn(e), tinne Br. tal NHG  stirn
```


## [2026-09-05T14:32:32.415Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==129' WLD_Bd2_pages.txt | head -30",
 "description": "WLD Bd2 p.124"
}
```


## [2026-09-05T14:32:33.356Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==211' WLD_Bd2_pages.txt | head -40",
 "description": "WLD Bd2 p.206"
}
```


### [2026-09-05T14:32:37.507Z] TOOL RESULT

```
 '                                                                                                           ;




124                                             bhai- : bbai- : bhl-


tJberlieferung'*          (Denom. osk. faamat etwa                              fahula „Rede,            Sage“,
fas eig. „Ausspriich, bes. gottlicher oder richterlicher ; gottliches Eeclit“
(wohl aus [ne]fas est mit infiaitivischem fas „e3 ist [nicht] auszasprechea^,
s.    Vf. LEWb.*          8.    V.   und    —   altes   *fas, nichl:             fordernd          — Bgm. IF
 2,149a, 179, IF. 30, 352; dazu dies fastus „Spruchtag fur den Prator'^,
fasti „da3 Verzeichnis dieser Tage, Kalender“)          als Ableitung von einem
                                                                          ;


Ptc. *bho-t6-s, lafe. fateor, -eri, fassus (in einzelnen Spuren auch fatari)
„bekenaea, zugebea“                   =
                            osk. fatiiim „fari'' (Lit. bei v. PlantaII 272; aber
 die von Zimmer KZ. 24, 209, Pick I* 489, II^ 159 weiter verglichenen air.
doadbat „demonstrat“ usvir. vielmehr zn ueld- „sehen‘‘),
    Aisl. bon, bon „Bitte, Gebet'', ags. ben „d3., Forderung'' {^bha-nl-s    oder                        ;


mlt o-Abtoming wie gr. (pcovijl); ags.             „prahleA^ (llolthausen KZ. 48,
238; wie lat. for aus *fai6r, slav. bijq; zur Abgrenzung gegeniiber dem
unthem. bha-mi             s. Bgm. 11^ 3, 100, 102, 197).

    Aus dem Balt, allenfalls (mit formantischem n, vgl. dieselbe Erw. bei
```


### [2026-09-05T14:32:39.311Z] TOOL RESULT

```
206                               bhres   — bliru-
bhres „bersten, brechen“ und „krachen, prasseln^' (wie beim Brechen).
   Ahd. brestan „bersten, brechen^S unpers. auch „Tnangeln, gebrechen‘‘
(nhd. mit md. nd. Umstellung bersUn), as. brestan^ afries. berstan, ags. berstan
„bersteii, sich brechen (von Wogen), widerhallen“, aisl. bresta „bersten,
krachen“; ahd. brest, bresfo „Gebrechen, Mangel“, nhd. Gebresten^ ahd. mhd.
brust „Bruch, RiS, Ermanglung, Nachteil“, ags. byrst, aisl. bresir ,,Gebrechen,
Mangel^;
  ahd. braston, mhd. brasteln^ ags. brastlian „prasseln, krachen'', aisl. brasta
„larmen, prahlen“; ohne t norw. bras n. „das Prasseln, Knitfcern, Reisholz“,
mit -h brisk „Wacholder“ (wie norw. brake ds. zu %href), sowie mhd.
braschen, mnA.brosken, braschen „krachen, schmettern; schreien, prahlen"';
  lit. braszkii, -Hi „krachen, prasseln, knacken^‘, mit anderer Yokalstellung

bdrszkii^   -Hi „klappern‘'.
  Zur Wz. bhrH gehoren air. brissim „breche“; brisc, bret. bresk „bruchig, zer-
brechlich‘‘ (die bret. Form braucht nicht nachFoy IP. 6, 3231F. Schwund eines
Eons, vor sk erfahren zu haben, so da6 nach Persson Beitr. 330 A. 1 etwa zu
bhreg^ „brechen“ gehoriges bhrg-skos       die Gdf. ware, denn sk bleibt nach
Pedersen KG. I 75f. auch im Brit, vielfach erhalten neben Fallen der
Umstellung zu -ks-, -ch-; ein %rist-ko- oder -sko ware kaum glaubhaft),
corn. breselQ) „Streit'*, mbret. breseJ, nbret. brezel „Krieg'', acymr. Com-bresel
MN., air. Bresal MN. (doch s. dazu Pedersen II 55 und 66S iiber ir. imbresan^
                                                              ;


cymr. ymryssan „rixa, contention, Fick II ^ 184, s. vielmehr Pedersen KG. 11
296, 625). aber ir. brosnae „fragminan zu aisl. brjota „brechenn; desgleichen
mir. brosc „Donner, Schall, Larm^;
   Ygl. Pick I^ 496, II^ 184 f., 186, III^ 280, Falk-Torp u. hriste (Lit.);
Persson Wzerw. 19, 35, 45, 85, 98, 163, Beitr. 329, 555: letzterer verbindet
die Gruppe mit bher-(sy „sch]ieidenn (vielleicht gr. (pagoog), aber wegen
der Bed. nicht mit Recht.

bhroisqo-, bhrisqo- „herb von Geschmackn.
   Russ.-ksl. obrezgnuti, obrhzgmiti „sauer werden“, cech. bresk „herber Ge-
schmackn, poln. brzazg „unangenehmer, herber Geschmack; iible Laune“,
russ. brezgdth (alt brezgati) „sich ekelnn (u. dgl., s. Berneker 85, wo nicht
iiberzeugende etym. Yersuche; -zg- aus -sk- durch Ass. an den tonenden
^V^ortanlaut) nach Wood KZ. 45, 61 zunachst zu norw. brisk „bitterer Ge-
```


## [2026-09-05T14:32:48.645Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; awk 'BEGIN{RS=\"\\f\"} NR==211' WLD_Bd2_pages.txt | tail -30; echo \"########## 212\"; awk 'BEGIN{RS=\"\\f\"} NR==212' WLD_Bd2_pages.txt | head -35",
 "description": "WLD bhru- entry"
}
```


### [2026-09-05T14:32:50.086Z] TOOL RESULT

```
cymr. ymryssan „rixa, contention, Fick II ^ 184, s. vielmehr Pedersen KG. 11
296, 625). aber ir. brosnae „fragminan zu aisl. brjota „brechenn; desgleichen
mir. brosc „Donner, Schall, Larm^;
   Ygl. Pick I^ 496, II^ 184 f., 186, III^ 280, Falk-Torp u. hriste (Lit.);
Persson Wzerw. 19, 35, 45, 85, 98, 163, Beitr. 329, 555: letzterer verbindet
die Gruppe mit bher-(sy „sch]ieidenn (vielleicht gr. (pagoog), aber wegen
der Bed. nicht mit Recht.

bhroisqo-, bhrisqo- „herb von Geschmackn.
   Russ.-ksl. obrezgnuti, obrhzgmiti „sauer werden“, cech. bresk „herber Ge-
schmackn, poln. brzazg „unangenehmer, herber Geschmack; iible Laune“,
russ. brezgdth (alt brezgati) „sich ekelnn (u. dgl., s. Berneker 85, wo nicht
iiberzeugende etym. Yersuche; -zg- aus -sk- durch Ass. an den tonenden
^V^ortanlaut) nach Wood KZ. 45, 61 zunachst zu norw. brisk „bitterer Ge-
schmackn brisken „bitter, herben. Aber nicht nach Wood aaO. als „zu-
sammenziehendn weiter zu mhd. brlsen „schnuren, einschniiren, einfassenn,
brtse „Einschnurung an Kleidungsstiickenn, nhd. elsass. prise „Einfas 3 ung
eines Kleides, Saum; Narbe, Schramme“, nisi, bris „Karben, sondern (in
Modifikation von Petersson IF. 23, 403; 24, 278, Persson Beitr. 930) zu
*bhrH- „schneiden“ (wie mndl. brine „Salzwassern).

1. bhru- „Augenbrauen, z. T. mit anl.     Yokal, wohl idg. o-; darin sehen die
      vollere Wzf. Osthoff MU. 4, 217,  Kretschmer KZ. 31, 336, J. Schmidt
     KZ. 32, 330, Krit 79; auch Solmsen KZ. 34, 549 (aber unter Ansatz
     von idg. a- wegen mak. d^govreg. doch s. u.); dagegen ein ver-
     dunkeltes Zsglied         „Augen mit Kons.-Ass.?) Persson Beitr. 17.
  Ai. hhru-h^ acc. bhruv-am „Braue“, av. brvat- f (du.) „Brauenn, np. abru^
baru ds. (Hubschmann I A. 10, 24); gr. dipgvg, -vog „Brauen, ubertragen „er-

########## 212
                                                                           .




                                                     bhru-, bhreu-                                 207

hohter Rand, Hugelrand“ (wie \^i, supercilium); maked. a^govreg ^dpgveg^^
(von Kretschmer Einl. 287 in d^govj^eg geandert; von Meillet, s. Boisacq
733 Anm. 3, wegen der anderweitig bezeugten Form d^goreg und wegen
av. brvat   air. bruad festgehalten) mir. bruad g. du., braiy brof, br(B n.
                                                             ;



du.        f.   „Brauen‘‘ (Pick II ^ 167, letztere               Formen von Pedersen KGr. 1193
zw. au8 bhroue erklart, doch geniigt ^bliruue als Gdf., das nach gen.
wom^ gebrochen aus ^bruwdm zu brove wurde), air. forbrii a. pi. (^bhruns
:   acc.        dcpgvg) forbrii   g.   pi.   „8upercilia‘‘       (Pedersen aaO.)   ;
                                                                                       ags. hru^   aisl.

6mw, pL brynn „Braue“ (kons. St., aus                    vgl. ^tungun^ ttingOy
kontrahiert und dadurch zur flexivischen Sonderentwicklung gelangt). Uber
ahd. brdwa s. u. bhereJc- „glanzen“) lit. bruvis „Braue‘", apr. tviibri „AVim-
                                                         ;


peP‘ (scheint Umstellung aus %niivi^ s. die Lit. bei Boisacq 734, Berneker
91, Trautmann Apr. XVII 466)        ahg. brzvh (urspriingliches Xom. *bry^ wie
                                                 ;


iry kirbVh)^ skr.-ksl. obr^vh^ skr. bbrva usw. „Braue“
       :
```


## [2026-09-05T14:33:07.861Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C%D9%87/",
 "prompt": "Give the dictionary entries for بویه — Dehkhoda (لغت‌نامه دهخدا), Mo'in (فرهنگ معین), and any etymology note (ریشه). Quote the Persian text."
}
```


## [2026-09-05T14:33:08.198Z] TOOL CALL #63: WebSearch

```json
{
 "query": "ریشه‌شناسی واژه «بویه» آرزو حسن‌دوست بوی هوس"
}
```


### [2026-09-05T14:33:15.986Z] TOOL RESULT

```
# Dictionary Entries for بویه

## Dehkhoda (لغت‌نامه دهخدا)
"بویه. [ ی َ / ی ِ ] ( اِ ) آرزومندی"
The entry defines the word as meaning "desire" or "longing," citing classical Persian poets including Ferdowsi and Asadi.

## Mo'in (فرهنگ معین)
"(یِ ) ( اِ. ) ۱ - آرزومندی . ۲ - آرزو"
This dictionary provides two related meanings: "desiring/yearning" and "desire/wish."

## Etymology
The provided content lacks a dedicated etymology section explaining the word's origin. However, user comments suggest the term derives from local Deilami roots, though the site indicates this remains speculative rather than historically documented.
```


### [2026-09-05T14:33:17.829Z] TOOL RESULT

```
Web search results for query: "ریشه‌شناسی واژه «بویه» آرزو حسن‌دوست بوی هوس"

Links: [{"title":"بوسه - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D8%A8%D9%88%D8%B3%D9%87"},{"title":"بو - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A8%D9%88/"},{"title":"گنجور » رودکی » قصاید و قطعات » شمارهٔ ۱۲۱ - بویِ جویِ مولیان آیَد هَمی","url":"https://ganjoor.net/roodaki/baghimande/sh121/"},{"title":"معنی بویه | لغت‌نامه دهخدا | واژه یاب","url":"https://vajehyab.com/dehkhoda/%D8%A8%D9%88%DB%8C%D9%87"},{"title":"بویه - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C%D9%87/"},{"title":"معنی بویه چیست | لغت یاب","url":"https://logatyab.ir/word/155922/%D8%A8%D9%88%DB%8C%D9%87"},{"title":"معنی بویه - لغت‌نامه دهخدا","url":"https://lamtakam.com/dictionaries/dehkhoda/195673/%D8%A8%D9%88%DB%8C%D9%87"}]

Based on the search results, here's what I found regarding the etymology of the word "بویه" (buyeh):

بویه means desire and wish, expressing a deep sense of longing and hope for obtaining something one desires. 

The etymology of the name "بویه" is possibly derived from local Deilami words such as "بو" or "بیو" meaning "good" or "nice". However, the word also has myriad meanings including desire, yearning, hope, and can also refer to a floating buoy.

It's worth noting that the word appears in Persian poetry with this meaning of desire or longing. The word "بو" (bu) in poetry can mean desire, lust, and aspiration, as seen in poetry where "بوی جوی مولیان" (the desire for the stream of Mulyan) refers to longing and yearning.

The search results indicate that "بویه" has multiple related meanings in Persian, all connected to the concept of desire, yearning, and aspiration, though the specific analysis by Arzoo Hasandoost that you mentioned in your search query was not found in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-05T14:33:37.180Z] TOOL CALL #64: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C/",
 "prompt": "List the Dehkhoda (لغت‌نامه دهخدا) senses of بوی. Does it include a sense 'امید، آرزو، طمع' (hope, desire) with the idiom «به بویِ»? Quote the Persian text of that sense and any example verse."
}
```


## [2026-09-05T14:33:39.927Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FRS بویه ===\"; grep -n \"بویه\" FRS_pages.txt FSF_pages.txt 2>/dev/null | head -10; echo \"=== HRN boi ===\"; grep -n \"böi\\|boi '\\|bòi\\|bü'\\|büi\" HRN.txt | head -10",
 "description": "Grep Loghat-e Fors / Shahnameh glossary / Horn"
}
```


### [2026-09-05T14:33:40.009Z] TOOL RESULT

```
=== FRS بویه ===
FRS_pages.txt:21838:‫‪۱‬ا‪-‬شی؛ٌ ن ‪.‬کز ‏ ‪- ۲‬ل درحاشبه ؛نگایوی بك و بویهرسودوبدن و رفتن‬
FSF_pages.txt:5673:                                               ‫‪1۹‬‬                                         ‫بویه‬
FSF_pages.txt:5702:       ‫خروشان و نوان بابویه جفت‬
FSF_pages.txt:5713:                                      ‫ابخهتر‬                                             ‫بویه‬
FSF_pages.txt:6233:                      ‫(ناصر ‪:)۳۵۳-۴‬‬         ‫هده خحواهی ز من بویهده‌ای»‬    ‫بی‌مهر ی‬
=== HRN boi ===
2444:240. böi, bö 'Geruch*, böytden^ böyämden {Je^. X'är.)^),
2446:aw. baoiöi- *Wohlgeruch' ; phlv. böd, böi, böylnUan;
2456:n. 6ö(J, böz *Balsanistrauch' (46); si/n. böi (LW.), sar.
10257:51. böitan erlösen, retten, befreien', Praes. böjet; höj(i)sn
```


### [2026-09-05T14:33:49.532Z] TOOL RESULT

```
# Analysis of Dehkhoda Dictionary Entry for بوی

Based on the provided content, the Dehkhoda dictionary section does **not** include a sense meaning "hope, desire, or appetite" (امید، آرزو، طمع) with the idiom «به بویِ».

The Dehkhoda entry lists these primary senses:

1. **Fragrance/Aromatics**: "عطریات" (perfumes and aromatic substances)
2. **Pleasant scent**: "بوی خوش" (good smell)
3. **Trace/mark**: "اثر نشان" (sign or remnant)

The entry emphasizes compounds like "خوش‌بوی" (fragrant) and "بدبوی" (foul-smelling), with extensive poetic examples from classical Persian literature.

However, the **synonyms listed at the page header** do mention: "مترادف بوی: آرزو، امل" (Synonyms: hope, aspiration), suggesting this meaning exists in Persian usage, though it does not appear to be documented in the Dehkhoda section quoted here.
```


## [2026-09-05T14:33:57.734Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 5668,5716p FSF_pages.txt; echo \"###### bru in FSF\"; grep -n \"بُرو\\|برو \" FSF_pages.txt | head -10",
 "description": "FSF buyeh and boru"
}
```


### [2026-09-05T14:33:57.791Z] TOOL RESULT

```
 ‫(‪)۳۸۱۲۰۰۷۲۳‬‬                                          ‫بوینده دارای بوی خوش» معطر‪:‬‬

               ‫سوی شهر ایران نهادند روی‬               ‫بیامد بر آن کرسی زر نشست‬
‫سپاهی برآنگونه با رنگ و بوی‬                  ‫پراز خشم بویا ترنجی به دست‬
‫(‪)۲-۷۹۲-۵۶۳۱‬‬                                  ‫(‪)۶-۵۵۲-۳۲۶‬‬
                                               ‫‪1۹‬‬                                         ‫بویه‬


                    ‫منوچهر بهاو می‌گوید‪:‬‬                   ‫کگهوری ندیدم به خوبی چنوی‬
         ‫خاست‬     ‫تو را بویۂ دخت مهراب‬               ‫بدان سرفرازی و آن رنگ و بوی‬
                                                     ‫(‪)۴-۲۱۳-۶۶۱‬‬
 ‫(‪)۱-۴۲۲-۹۱۳۱‬‬
                                                           ‫همان ناممن باز گردد به ننگ‬
‫(یعنی‪ :‬تو آرزوی دیدار رودابه را داری» و‬             ‫نماند ز مندر جهان بوی و رنگ‬
‫دلت در بند و اندیشۀ جان و روان سام که‬                ‫(‪)۶-۷۶۲-۳۲۸‬‬
                   ‫در انتظار تست نیست)‪.‬‬             ‫رستم پس از آنکه در نبرداول بااسفندیار‬
                                                    ‫شکست خورده و زخمی شده است» به‬
    ‫و بی‌معنی است‪:‬‬      ‫آورده‌اند کهنادرست‬                                  ‫زواره گوید‪:‬‬
                                                           ‫بدو گفت رو پیش دستان بگوی‬
 ‫دلت خواهش سام نيرم کحجاست»‬                          ‫کزین دودة سام شد رنگ و بوی‬
                                                     ‫‪۸۲۹۸۵۱۱۳‬‬

 ‫چسنین آرزو را نشاید نسهفت‬                                         ‫‪-۳‬آرایش روی و موی بزک‪:‬‬
 ‫(‪)۴-۲۱۳۰-۹۷۱‬‬
                         ‫(اسدی ‪:)۲۱۲-۸۴‬‬
                                                          ‫پس پرده اندر یکی ماهروی‬
                                                    ‫چو خورشید تابان پر از رنگ و بوی‬
      ‫دلاور نپذرفت ازو هرچه گفت‬
                                                    ‫(‪۲-۲۷۱-۵‬ع‪)6‬‬
‫که بد در دلش بويه روی جفت‬
                                                                           ‫(اسدی ‪:)۲۰۱-۰۳‬‬
                          ‫(ویس ‪:)۵۷۲-۷۲‬‬

                                                           ‫کنون در پس پرده باببوی و رنگ‬
       ‫خروشان و نوان بابویه جفت‬
 ‫ز بی‌صبری و دلتنگی همی گفت‪...‬‬
                                                     ‫نشستی تو بناز و شویت به جنگ‬
                          ‫(ویس ‪:)۸۳۲-۹۷‬‬
                                                     ‫در این بیت از فخر گرگانی معنا روشن‌تر‬
                                                                       ‫است (ویس ‪:)۹۹-۴۳‬‬
        ‫دلبر‬    ‫دیدار‬    ‫بوية‬    ‫فتادش‬

                                                            ‫همه پیراست دایه روی و مویش‬
‫چآوتش در دل و چون تیردربر‬
                                                    ‫همی گسترد بر وی رنگ و بویش‬
                                      ‫ابخهتر‬                                             ‫بویه‬
                                                                                      ‫آرزو‪:‬‬
     ‫ستاره ستاره بخت واقبال]‪ :‬نیکبخت‪:‬‬
                                                     ‫زال کهچندی نزد منوچهر مهمان بود‬
###### bru in FSF
302:    ‫برو بر فگند و برآورد خشم‬                 ‫چشم‬
1478:‫ز من عنبر برو بر سنبلش سای‬                                   ‫‪-۲‬به معنی مجازی‪ :‬شنیدن‪:‬‬
1971: ‫بگسترد و شادان برو ريخت سیم‬
2012:          ‫گر ایدونک هاسترمزازنیان‬          ‫برو کرده صدگونه رنگ و نگار‬
2079:‫اروند می‌باشد و در فارسی «را» به «لام»‬                  ‫زره در برو برسرش بود ترگ‬
2435: ‫برو فسانه مخوان و فسون مدم حافظ‬              ‫خویشتن رابه زه بهمان و احسنت فلان‬
2448:               ‫بشاههی برو آفرین خواندند‬      ‫موسی گفت مبادا آنروز کهمناز افسوس‬
2578:‫گشت بازارگاه‬        ‫برو انجمن‬                    ‫به سوی دهستان نهادند روی‬
2586:               ‫ز هر سو سپه شد برو انجمن‬                    ‫از اسدی ( گرشاسب‌نامه ‪)۳۵۱-۶۱‬‬
2759:        ‫جهان چون برو بر نماند ای پسر‬                                 ‫=رگذشتن‬
```


## [2026-09-05T14:34:06.351Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"پرچین\\|پرگره\\|گروی زره\" FSF_pages.txt | head -10; echo \"--- leaf of headword برو=ابرو ---\"; awk 'BEGIN{RS=\"\\f\"} /پرچین/ {print \"LEAF \"NR}' FSF_pages.txt | head",
 "description": "Find Ferdowsi verse in FSF"
}
```


### [2026-09-05T14:34:08.023Z] TOOL RESULT

```
4986:        ‫ستادیش‌کنان پیش بیژن شدند‬                           ‫سیاوش ز گفت گروی زره‬
4987: ‫چو پيش بت چين بهرمن شدند‬                       ‫برو کرد پرچین‪ ,‬رخان پر گره‬
6887:‫چنین برمی‌آید که شاید پرچین در این‬                                                  ‫پرتاب تیر‬
6908:                      ‫خ‬                                                      ‫پرچین (بهافتوحل)‬
6909: ‫(‪)۱-۷۲۱-۳۹۷‬‬                                      ‫پرچین دیواریست که ازشاخة درخت با‬
6915:                ‫آمده است و نادرست است‪:‬‬                         ‫سراسر همه دشت پرچین نهید‬
19190:            ‫فریدون پیامم بدینگونه داد‬                               ‫گروی زره راگره تاگره‬
--- leaf of headword برو=ابرو ---
LEAF 106
LEAF 144
```


## [2026-09-05T14:34:10.947Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n 4970,4995p FSF_pages.txt; echo \"=== pdf page tag ===\"; awk 'NR<=4990 && /pdf page/' FSF_pages.txt | tail -3",
 "description": "FSF entry containing the verse"
}
```


### [2026-09-05T14:34:12.650Z] TOOL RESULT

```
                          ‫شعر باسکون را)‬                               ‫سواری» سوارکاری‪:‬‬
‫پیشوای کیش برهمایی‪ ,‬در این بیت‌ها‬                           ‫دست‬
                                                              ‫‌شود‬
                                                                 ‫هتا‬
                                                                   ‫ردش‬
                                                                     ‫ی دار‬
                                                                         ‫چهمی‬
                                                                            ‫‪...‬‬
                 ‫کنایه از بت‌پرست است‪_ :‬‬         ‫بیاموزدش خوردن و بسرنشست‬
              ‫دگر باره مهمان دشمن شدی‬            ‫(‪)۳-۱۶۳۱‬‬

 ‫صنم بودی اکنون برهمن شدی‬                                                      ‫لیش)‬
                                                                                  ‫واپ‬
                                                                                    ‫او(ب‬
                                                                                       ‫بر‬
‫(‪)۲-۲۵۱۰-۹۲۲‬‬                                                                 ‫مخثف ابرو‪:‬‬
        ‫ستادیش‌کنان پیش بیژن شدند‬                           ‫سیاوش ز گفت گروی زره‬
 ‫چو پيش بت چين بهرمن شدند‬                       ‫برو کرد پرچین‪ ,‬رخان پر گره‬
‫(‪)۵-۱۳۱-۷۱۸‬‬                                      ‫(‪)۳-۲۲۱۰-۲۸۸۱‬‬
           ‫به شمشیر جان از تنش برکنیم‬                                 ‫(رودکی ‪-‬نفیسی ‪:)۸۷۶‬‬
‫سرش رابه دار برین بر کنیم‬                           ‫بهارچین کن از آن روی بزم خانۀ خویش‬
                                  ‫برین همنشان‬       ‫اگر چه خانة تو نوبهار برهمنست‬
                 ‫بیرنسان بدینسان همچنین‪:‬‬                                    ‫(ناصر ‪:)۴۳۳-۰۸‬‬
               ‫برین همنشان هفت گرد دلیر‬                           ‫بت نشسته در ميان پیرهنت‬
‫کشیدند شمشیر بر سان شیر‬                             ‫تو همی لعنت کنی بر برهمن‬
‫(‪)۲-۶۶۱-۹۹۵‬‬                                                                              ‫برهنه‬
=== pdf page tag ===
```


## [2026-09-05T14:34:54.160Z] TOOL CALL #69: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eyh%E2%82%82-\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%DA%A9\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1%D9%88\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85%D9%87\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\" \\\n \"https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C%D9%87/\" \\\n \"https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C/\" \\\n \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%DB%8C\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"pdf page 97 (book 67), roots Bhoi / Bhou-Bheu / Bhru 1: verification of bim, bak, bimeh, buyeh, abru/boru, brow, bridge\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-05T14:35:00.582Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/b47441504702e7b3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/affc1b4f433ce81e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/13fe1f5bc35cd020.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d54d6cda943d4235.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/902d942e8ce767ab.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1b4899b9782322f7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/55124b59e54ea442.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c4df3eb8299e076e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/96f3a2729db728a1.txt
```


## [2026-09-05T14:35:18.038Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -o \"b[ēe]m [^]]\\{0,60\\}\\|byhm[^]]\\{0,40\\}\\|\\bbim\\b[^]]\\{0,40\\}\" PHD.txt | head -5; echo \"=== PHD fear ===\"; grep -n -o \"[a-zāēīōū]* \\[[^]]*\\] fear[^.]\\{0,40\\}\" PHD.txt | head -10; echo \"=== NYB fear/bim ===\"; grep -n -o \".\\{0,40\\}bīm.\\{0,60\\}\" NYB_vol2_glossary.txt | head -5",
 "description": "MacKenzie/Nyberg for bem 'fear'"
}
```


### [2026-09-05T14:35:21.545Z] TOOL RESULT

```
166:bim [-bym
170:bim [bym
256:bim [bym | = M, N ~
1898:bim, škēh, tars; ahr.
1900:bimémand.
=== PHD fear ===
166:bim [-bym] fearless
170:bim [bym] fearless
256:bim [bym | = M, N ~] fear, terror
256:n [-kn'] fearful, terrible
256:mand [-'wmnd] fearful
593:tars [2/5 | M trs, N ~] fear, respect
593: [tls-ytn' | (M tyrs??dn), N ~] fear, be afraid
=== NYB fear/bim ===
ugrep: error: error at position 80
][\x80-\xbf]*){0,60}
                    \___exceeds complexity limits
```


## [2026-09-05T14:41:25.741Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"== max page markers ==\"; awk '$0 ~ /^[0-9]{3,4}$/ {print $0}' IEC.txt | sort -n | tail -3; echo \"== 1560s ==\"; awk '$0 ~ /^15[5-7][0-9]$/ {print NR\": \"$0}' IEC.txt | head; echo \"== Skeat Bridge/Brow ==\"; grep -n -o \"Bridge\\.\\{0,300\\}\" SKT.txt | head -3; grep -n -o \"Brow,\\{0,1\\}\\.\\{0,250\\}\" SKT.txt | head -3",
 "description": "Check IEC page 1562 and Skeat entries"
}
```


### [2026-09-05T14:41:28.149Z] TOOL RESULT

```
== max page markers ==
997
998
999
== 1560s ==
20448: 1550
20457: 1551
20471: 1552
20479: 1553
20494: 1554
== Skeat Bridge/Brow ==
1678:Brow.
2332:Brow
2370:Brow
```


## [2026-09-05T14:41:32.276Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk '$0 ~ /^15[6][0-9]$/ {print NR\": \"$0}' IEC.txt | head; echo \"--- around 1562 ---\"; sed -n 20494,20560p IEC.txt | grep -n -o \"^15[0-9][0-9]$\\|ueid\\|uid-ma\\|bi-me\\|weid\" | head; echo \"=== Skeat 2332 ===\"; sed -n 2330,2336p SKT.txt",
 "description": "Locate IEC 1562 and Skeat Brow"
}
```


### [2026-09-05T14:41:33.722Z] TOOL RESULT

```
--- around 1562 ---
1:1554
=== Skeat 2332 ===
Broil  (a),  a  tumult.  (F.-Te«t.?)  F. trtmiiUr,  to  jumble,    Cuhuju?.    confound.
BROOK.
Perhaps  related  to  G.  brudeJn,  br^dtM,  to bubble  (whence  to  give  off  steam,  coofose) ; a.  brodel,  broifem,  vapour,  allied  to  E. Breath  (Schclcr).  Cf.  F.  btvuUhrJ,  a mist,  fog.  %  We  also  find  >N.brxKh^  tumult, broiheii.  a  tempest ;  Gael.  brei,^hUadh,  titf- moil.  broigiuk,  noise  (pcrhft[>.s  unrelated). Broker.  <E.)  SceBrooku)- Bronchial.  (Gk.)  Gk.  Bfiyx****  neol. pi.,  the  ramifications  of  the  windpipe.— Gk.  ^p6yxot,  ihe  windpipe  ;  cf.  fipnyx*^-  ' gill.  Allied  to  Gk.  a^x'"*'  ^^  ^<^^-  ^*'* brvrKk't'tis;  (rom  0p6yxof. Bronze.  (F.-ltal.-Teat)  SeeBrown. Brooch.  (F.-L.)  Named  from  the  pin which  fastens  iL  M.  E.  brockr,  a  pin,  yejL brooch.  —  F.  brocht,  a  spit,  point.  —Low  L bnvfa,  a  pointed  stick.  — L.^/vrinttj,  ashaip tooth,  pomt  Cf.  Gael.  bn>ff,  to  goad.^r^, on  awl ;  \V.  procio^  to  stab.
broach.  (F.  -  L.)  M.  E.  settm  m brc(ht  —  \o  set  ft-broafh,  tap  lir^uor.  —  F. mtttn  en  brxMe,  to  tap,  by  piercing  a  bar rel.  —  F.  i^nv A^r,  to  pierce. —  F.  bnkki,  '» broach,  spit.,*  Cot. :  sec  above.
brocade.  (Span.-L.)  Span.  brMain, brocade ;  orig.  embroidered,  the  pp.  of  ■ verb  brotar*-  \no\  u&ed)  an^weiing  to  F btvcMtr,  *  lo  broach,  also,  lo  sLtich  . . .  vilb great  stitches,'  Cot.— Low  L.  brvccm,  U brcccus ;  sec  Broooh.
broccoli.  (Ital.  -  L.)  Ital.  br^ctpHy sprouts ;  pi.  of  broccolc.  a  sprout.  Dlnib ofbroivo,  A  skewer,  a  shoot,  stalk.  — L.  fm* (Hs,  a  i»oint.
brochure,  a  pamphlet  (F.  —  L.)  F. brfffAurt,  a  few  leaves  stitched  together.* F.  brother,  to  stitch :  sec  brocade.
```


## [2026-09-05T14:41:38.945Z] AGENT

Now I'll write the verification file.


## [2026-09-05T14:47:49.025Z] TOOL CALL #73: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk97.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndata = {\n \"pdf_page\": 97,\n \"book_page\": 67,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": []\n}\n\n# ---------------- entry 0 : Bhôi ----------------\ne0 = {\n \"entry\": 0,\n \"root\": \"Bhôi\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *bʰeyh₂- 'to fear, be afraid' (Pokorny: bhōi- : bhəi- : bhī- (bhii̯ə-) 'sich fürchten', IEW 161–162; LIV *bʰeyH-)\",\n \"note\": \"Root name, language label and gloss are all exactly Pokorny's. IEW p.161 heads the article 'bhōi- : bhəi- : bhī- (bhii̯ə-) ,sich fürchten‘; bhoidho-s ,fürchterlich, abscheulich‘', and the article runs onto p.162, closing 'WP. II 124 f., 186'. The modern reconstruction adds a laryngeal (*bʰeyh₂-); Wiktionary notes that this root is sometimes kept apart from a homophonous *bʰeyh₂- 'to strike'. Watkins/AHD has no entry for the 'fear' root at all (no English derivative), so AHD is silent rather than contradicting.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰeyh₂- «ترسیدن، بیم داشتن» است که پوکورنی در فرهنگ ریشه‌شناختی خود (صص ۱۶۱–۱۶۲) به صورت bhōi- : bhəi- : bhī- آورده و همان معنایی را به دست داده که نورایی نقل کرده است. نام ریشه، برچسب زبانی («هندواروپایی») و معنی، هر سه با پوکورنی و پژوهش امروزی می‌خواند؛ تنها تفاوت آن است که بازسازی امروزی حنجره‌ای (*h₂) را نیز در ریشه می‌آورد. ادعای نورایی در این بخش درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0eyh%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:161\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 171 (printed p.161–162): 'bhōi- : bhəi- : bhī- (bhii̯ə-) ,sich fürchten‘; bhoidho-s ,fürchterlich, abscheulich‘. Ai. bhdyate ,fürchtet sich‘ …, av. bayente, byente ,sie setzen in Furcht‘, mpers. besānd ,sie sind in Angst‘ (uriran. *bai-sk-)'. Exactly the root Nourai prints.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.124 (WLD_Bd2_pages.txt leaf 129)\", \"stance\": \"supports\",\n    \"note\": \"Running head of the page reads 'bhai- : bhəi- : bhī-'; this is the WP II 124 f. to which Pokorny's article refers at its close.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.53 'FEAR, FRIGHT'\", \"stance\": \"supports\",\n    \"note\": \"'1. Derivs. of IE *bhai-(?), *bhi- in Balto-Slavic and Indo-Iranian words for \\\"fear\\\" … Walde-P. 2.194 f. … Skt. bhaya-, bhīti-, bhī- … Av. 3pl. bayente \\\"frighten\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, alphabetical run bheg⁠ʷ- … bheid- …\", \"stance\": \"silent\",\n    \"note\": \"Watkins lists bhei-1 'a bee' and bhei-2 'to strike' but no root meaning 'to fear' — the root has no English reflex, so the appendix simply omits it.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"bay; bhâyaka\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Avestan really has a verbal root bay- 'to frighten; to be in fear': Bartholomae, Altiranisches Wörterbuch cols. 927–928, 'j., g. bay- V. \\\"erschrecken\\\"', present stems baya-/bya-, 3pl. bayente (aspąm asnaŋhō bayente 'their horses cause terror', Yt. 5.12), byeintī (Y. 34.8), perfect biwi-; Pokorny 161 quotes the same forms. Nourai's first word is therefore right, though it is a verbal root, not a noun 'fear'. The second word, bhâyaka, is NOT an attested Avestan form: it is the Indo-Iranian preform reconstructed by Horn and repeated by Pokorny for New Persian bāk — POK 162 'npers. bāk \\\"Furcht\\\" (aus *bhāyaka-)', HRN no. 170 'bāk \\\"Furcht\\\". ar. *bhāyaka-, von √bhay- \\\"erschrecken, sich fürchten\\\" (aw. bay-, ai. bhay-)'. The spelling with bh- is Indo-Iranian/IE notation; a real Avestan word would be *bāyaka- (Avestan has no bh). So the node is substantively right but presents a starred reconstruction as an attested Avestan word.\",\n \"derivation_fa\": \"در اوستایی ستاک فعلی bay- «ترساندن، در بیم بودن» به‌راستی گواهی شده است؛ بارتولمه در «فرهنگ ایرانی باستان» (ستون‌های ۹۲۷–۹۲۸) آن را با صیغه‌هایی چون bayente و byeintī آورده و پوکورنی نیز همان‌ها را نقل کرده است. اما صورت دوم، یعنی bhâyaka، واژه‌ای اوستایی نیست بلکه بازسازی هندوایرانی *bhāyaka- است که هرن (شمارهٔ ۱۷۰) و پوکورنی (ص ۱۶۲) برای فارسی «باک» پیشنهاد کرده‌اند؛ در اوستایی «بـهـ» وجود ندارد و صورت اوستایی می‌بایست *bāyaka- باشد. پس ادعای نورایی از نظر محتوایی درست است، ولی یک صورت بازسازی‌شده را به نادرست واژهٔ اوستایی خوانده است — با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0eyh%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:161,162\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 171: 'av. bayente, byente ,sie setzen in Furcht‘' (p.161) and leaf 172 (p.162) 'npers. bāk ,Furcht‘ (aus *bhāyaka-)'. Both of Nourai's words are on the two cited pages.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 927–928 s.v. bay- (BRT.txt line 16728)\", \"stance\": \"supports\",\n    \"note\": \"'j-, g. bay- V. \\\"erschrecken\\\". Praes. 2 baya-, bya-; Perf. 1 biwi-' … 'aspąm asnaŋhō bayente \\\"ihre Rosse erregen Schrecken\\\" Yt.5.12' and 'byeintī … \\\"(so) setzen sie uns in Furcht\\\" Y.34.8'. No noun *bay 'fear' and no Avestan *bhāyaka-.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 170, p.39 (HRN.txt leaf 60)\", \"stance\": \"supports\",\n    \"note\": \"'170. bāk \\\"Furcht\\\". ar. *bhāyaka-, von √bhay- \\\"erschrecken, sich fürchten\\\" (aw. bay-, ai. bhay-)'. Horn is where the starred form Nourai labels 'Avestan' comes from.\"},\n   {\"src\": \"ARY\", \"where\": \"p.143 s.v. بیم (with cross-reference بازگشت به: باک) and p.187 s.v. باک\", \"stance\": \"supports\",\n    \"note\": \"Aryanpur's cognate list for بیم prints 'اوستایی (AVESTAN): BAY-, BHAYATE …' and Pahlavi BIM, Sanskrit BHI/BHIMA/BHITI, i.e. the same Avestan verbal root.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"bîm «بیم»; bâk «باک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"بیم bīm 'fear' descends from Middle Persian bīm [bym] 'fear, terror' (MacKenzie, CPD: 'bīm [bym | = M, N ~] fear, terror', with bīmgēn 'fearful' and abē-bīm 'fearless'), from Old Iranian *biHma- < Proto-Indo-Iranian *bʰiHmás, a -ma- abstract of *bʰeyH-; it is thus the exact formal counterpart of Sanskrit bhīmá-. Horn no. 58 gives precisely this: 'bīm \\\"Furcht\\\". √bhay- \\\"erschrecken, sich fürchten\\\" (aw. bay-, ai. bhay-), *bhāima(n)-; phlv. bīm, bīmkīn'. باک bāk 'fear' goes back to Middle Persian wāk/wāg and to Old Iranian *bā(ya)ka-, a -ka- noun to the same root: intervocalic *-y- was lost with compensatory lengthening of a > ā, giving *bāka- > bāk (Horn no. 170; Pokorny 162 'npers. bāk \\\"Furcht\\\" (aus *bhāyaka-)'; Cheung, EDIV, s.v. *baiH-). Neither word is an Arabic loan; both are inherited Iranian, and both hang from the root box exactly as drawn.\",\n \"derivation_fa\": \"«بیم» از فارسی میانهٔ bīm «ترس، هراس» می‌آید (مکنزی: bīm [bym] fear, terror؛ نیز bīmgēn و abē-bīm)، و آن از ایرانی باستان *biHma- و هندوایرانی آغازین *bʰiHmás، یعنی ساختِ پسوندِ -ma- بر ریشهٔ *bʰeyH-؛ از همین رو «بیم» و «بهیمَ» سنسکریت هم‌ساخت و هم‌ریشه‌اند. هرن (شمارهٔ ۵۸) نیز همین را می‌گوید و صورت *bhāima(n)- را بازسازی می‌کند. «باک» از ایرانی باستان *bā(ya)ka- است: یِ میان‌واکه‌ای افتاده و «ا» کشیده شده و پسوند -ka- به «ک» بدل گشته است (هرن شمارهٔ ۱۷۰؛ پوکورنی ص۱۶۲). هیچ‌یک معرّب یا وام‌واژه نیست. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%A8%DB%8C%D9%85\", W + \"%D8%A8%D8%A7%DA%A9\"],\n \"ref_check\": [\n   {\"ref\": \"POK:162\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 172 (p.162): 'npers. bāk ,Furcht‘ (aus *bhāyaka-)'; the same page lists ai. bhī-ḥ, bhīti-ḥ ,Furcht‘, bhīmá-ḥ ,furchtbar‘.\"},\n   {\"ref\": \"HRN:39,59\", \"status\": \"supports\",\n    \"note\": \"Both pages are right. p.39 = Horn no. 170 'bāk \\\"Furcht\\\". ar. *bhāyaka-, von √bhay-'; p.59 = Horn no. 58 'bīm \\\"Furcht\\\". √bhay- … *bhāima(n)-; phlv. bīm, bīmkīn' (HRN.txt leaves 60 and 80).\"},\n   {\"ref\": \"BQT:340\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 561 (printed ≈ p.340–341) carries the headword 'بیم … بر وزن میم؛ ترس و واهمه را گویند' with Moʿin's etymological footnote (citing Unvala and an Old Iranian preform). Aryanpur independently cites 'برهان قاطع ۳۴۰' for بیم, confirming the page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.18 s.v. bīm (PHD.txt line 256)\", \"stance\": \"supports\",\n    \"note\": \"'bīm [bym | = M, N ~] fear, terror. ~gēn [-kn'] fearful, terrible. ~ōmand fearful'; also 'abēbīm [-bym] fearless'. The Middle Persian link Nourai omits is real.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp.143 (بیم) and 187 (باک)\", \"stance\": \"supports\",\n    \"note\": \"Both headwords are entered, cross-referenced to each other ('بازگشت به: باک'), with Avestan BAY-, Pahlavi BIM, Sanskrit BHI/BHIMA and Balto-Slavic cognates, and with citations to برهان قاطع ۳۴۰ and فرهنگ معین.\"},\n   {\"src\": \"BQT\", \"where\": \"vol.1, printed p.340 (leaf 561)\", \"stance\": \"supports\",\n    \"note\": \"Headword بیم glossed 'ترس و واهمه' with Moʿin's footnote; the sense Nourai gives is Borhān's.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"bhay; bhî-ma\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Sanskrit has the root bhī / bhay- 'to fear': 3sg. mid. bháyate 'he fears' (< *bʰáyHatay), perfect bibhā́ya, present bibhéti; and the vr̥ddhi-less -ma- derivative bhīmá- 'terrible, dreadful, fearful' (< *bʰiH-mó-), which is formally identical with Persian bīm. Pokorny 161–162 prints both: 'Ai. bhdyate ,fürchtet sich‘ (aus *bhōietai = slav. bojetŭ)' and 'bhīmá-ḥ ,furchtbar‘'. Buck 16.53 lists Skt. bhaya-, bhīti-, bhī- among the Indo-Iranian continuants of IE *bhai-/*bhī-. Both words are real, in Sanskrit, with the glosses given, and both descend directly from the root box.\",\n \"derivation_fa\": \"در سنسکریت ریشهٔ bhī / bhay- «ترسیدن» گواهی شده است: bháyate «می‌ترسد»، bibhéti، و ماضی نقلی bibhā́ya؛ و صفت bhīmá- «مهیب، ترسناک» که ساختِ *bʰiH-mó- است و درست هم‌ساخت «بیم» فارسی. پوکورنی (صص ۱۶۱–۱۶۲) هر دو را زیر همین ریشه آورده و باک نیز در فرهنگ واژه‌های هم‌معنی (بند ۱۶٫۵۳) bhaya-، bhīti- و bhī- را در همین خانواده جای داده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0eyh%E2%82%82-\", W + \"%D8%A8%DB%8C%D9%85\"],\n \"ref_check\": [\n   {\"ref\": \"AEF:320\", \"status\": \"not_checked\",\n    \"note\": \"AEF = Khaleqi Motlaq's «اساس اشتقاق فارسی», the Persian translation of Horn's Grundriss with Hübschmann's notes; refs_online.json classes it 'catalog' — no scan online and no local copy, so p.320 could not be opened. The underlying Horn entries (nos. 58, 170), which are on disk, do state 'ai. bhay-', i.e. the claim itself is independently supported.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 161–162 (POK_01.txt leaves 171–172)\", \"stance\": \"supports\",\n    \"note\": \"'Ai. bhdyate ,fürchtet sich‘ … ai. bhiyāná-ḥ ,sich fürchtend‘; bhī-ḥ f., bhīti-ḥ f. ,Furcht‘, bhīmá-ḥ ,furchtbar‘, bhītá-ḥ ,sich fürchtend, erschrocken‘'.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 16.53 FEAR, FRIGHT\", \"stance\": \"supports\",\n    \"note\": \"'Skt. bhaya-, bhīti-, bhī-, trasa-' in the word list, and in the discussion 'Skt. bhaya-, bhīti-, bhīṣā (s-extension)'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur p.143 (بیم)\", \"stance\": \"supports\",\n    \"note\": \"Cognate column 'سانسکریت (SANSKRIT): BHI, BHITI, BHIMA, BHAYATE …' alongside the Avestan and Pahlavi forms.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Persian\", \"words\": \"bîmeh «بیمه»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"بیمه bīme 'insurance' certainly belongs to this root-family, but Nourai's particular arrow (Sanskrit bhay/bhīma → Persian bīme) is only one of two live accounts, and his own cited authority does not say it. Moʿin's entry reads 'بیمه [اردو و هند. < بیماه: ضمانت]', i.e. a loan from Urdu/Hindi bīmā(h) 'guarantee'; the derivatives are labelled '[هند. ف.]' (Hindi + Persian). Wiktionary sets out both possibilities: either an internal Persian formation بیم + ـه, or — because the word is documented in the Mughal empire from the 1650s while the first Iranian attestation is a memoir of 1801 about India — a borrowing from an Indo-Aryan word continuing Sanskrit bhīmá-. Either route ends at PIE *bʰeyh₂-, so the root box is right; what is not established is that the immediate source is Sanskrit rather than Persian bīm itself. The chart's NOTE is accurate to Mann: IEC 723, under the suffix -mā, prints 'Skt. bhi-mā \\\"fear\\\"; Per. bi-me (\\\"insurance\\\", fr. *uid-ma?)', i.e. Mann floats — with a question mark — a derivation from *weid- 'to see'. No modern source follows him; the word is a *bʰeyH- word, and Mann's *uid-mā should be rejected.\",\n \"derivation_fa\": \"«بیمه» بی‌گمان به همین خانوادهٔ *bʰeyh₂- «ترسیدن» می‌پیوندد، اما مسیر دقیقی که نورایی کشیده (سنسکریت → فارسی) قطعی نیست و مرجع خودِ او آن را نمی‌گوید: معین ذیل «بیمه» می‌نویسد «[اردو و هند. < بیماه: ضمانت]»، یعنی وام‌واژه از اردو/هندی. ویکی‌واژه دو احتمال را کنار هم می‌گذارد: یا ساخت درون‌فارسی «بیم + ـه»، یا وام‌گیری از هندی‌آریایی (بازماندهٔ bhīmá- سنسکریت)، چون کهن‌ترین کاربردها از هند دورهٔ گورکانی (سدهٔ ۱۱ ق/۱۷ م) است و نخستین گواه ایرانی سفرنامه‌ای از ۱۸۰۱ م دربارهٔ هند. در هر دو حالت ریشهٔ نهایی یکی است. یادداشت خودِ نمودار درست نقل شده است: مان (IEC ص۷۲۳) ذیل پسوند -mā می‌نویسد «Per. bi-me (insurance, fr. *uid-ma?)» و آن را با تردید به ریشهٔ *weid- «دیدن» می‌بندد؛ پژوهش امروزی این را نمی‌پذیرد. مجموعاً با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D8%A8%DB%8C%D9%85%D9%87\", W + \"%D8%A8%DB%8C%D9%85\"],\n \"ref_check\": [\n   {\"ref\": \"MON:633\", \"status\": \"partial\",\n    \"note\": \"Moʿin has the entry (MON_part1.txt line 27258, 2-vol Adena reprint — its pagination differs from the 6-vol Amir Kabir set Nourai cites, so the page number itself could not be checked): 'بیمه (bime) [اردو و هند. < بیماه ضمانت] (اِ.) عملی است که اشخاص با پرداخت وجهی قراردادی منعقد کنند …'. Moʿin therefore derives the word from Urdu/Hindi, not directly from Sanskrit bhay/bhīma as the arrow does.\"},\n   {\"ref\": \"IEC:723\", \"status\": \"supports\",\n    \"note\": \"Cited only in the chart's NOTE, and it is accurate: IEC.txt line 1223–1234, printed p.723, s.v. the suffix '-mā (formative suffix of nouns derived from verbal roots)': 'Skt. bhi-mā \\\"fear\\\"; Per. bi-me (\\\"insurance\\\", fr. *uid-ma?)'. Mann's *uid-mā is flagged with a question mark by Mann himself.\"},\n   {\"ref\": \"IEC:1562\", \"status\": \"not_found\",\n    \"note\": \"The printed page markers in the local OCR of Mann (IEC.txt) run out at ~p.1554, so the second page cited in the NOTE could not be located; the *weid- claim is however already documented at IEC 723.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Moʿin, Farhang-e Farsi s.v. بیمه\", \"stance\": \"partial\",\n    \"note\": \"'[اردو و هند. < بیماه ضمانت]' — an Indo-Aryan loan, which is compatible with the root but not with a direct Sanskrit-to-Persian arrow.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.723 s.v. -mā\", \"stance\": \"partial\",\n    \"note\": \"Puts Per. bi-me beside Skt. bhi-mā but adds 'fr. *uid-ma?', the alternative Nourai's NOTE reports.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ vol.1 (بیم region, printed p.340)\", \"stance\": \"silent\",\n    \"note\": \"Borhān has بیم but no headword بیمه — the word is a 19th-c. commercial term and post-dates the dictionary (1062/1652).\"}\n ]\n})\n\ndata[\"entries\"].append(e0)\n\n# ---------------- entry 2 : Bhôu, Bheu ----------------\ne2 = {\n \"entry\": 2,\n \"root\": \"Bhôu, Bheu\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Mann, IECD 98: 'bhóu- (3), bhou- \\\"joy, satisfaction\\\"' — a root recognised by Mann alone; the forms he gathers are normally taken as semantic offshoots of PIE *bʰuH- 'to be, become, thrive' (Pokorny bheu- : bheuə- : bhū-, IEW 146–150; Watkins bheuə- 'to be, exist, grow').\",\n \"note\": \"The citation is exact: IEC.txt, printed p.98 (running head 'bhóu- — bhragō 98'), 'bhóu- (3), bhou- \\\"joy, satisfaction\\\". See bhou- | Skt. cf. bhāvitaḥ \\\"well-disposed\\\"; Arm. cf. bav \\\"enough\\\"; bavem beside bovem, bujem \\\"suffice\\\"; Per. būya, s. \\\"hope, desire\\\"; Pol. bawić, Cz. bavit \\\"amuse\\\"; Cz. zá-bava \\\"amusement\\\"; Srb. u-bav \\\"handsome\\\"'. Mann's parallel entry on p.77, 'bhəu- \\\"please\\\"', gives the same material. But no other authority sets up a root 'joy, satisfaction': Pokorny, Walde-Pokorny and Watkins know only bheu- 'to be, grow', and the Armenian/Slavic/Sanskrit words Mann adduces are elsewhere derived from that root or from *gʷʰeh₁w- (Lat. faveō). The root box is therefore faithfully copied from Nourai's source but rests on a single, idiosyncratic authority.\",\n \"note_fa\": \"ارجاع نورایی دقیق است: مان در «فرهنگ تطبیقی هندواروپایی» (ص۹۸) مدخل «bhóu- (3), bhou- \\\"joy, satisfaction\\\"» را دارد و زیر آن سنسکریت bhāvitaḥ، ارمنی bav، فارسی būya و لهستانی bawić را می‌آورد. با این همه، هیچ مرجع دیگری چنین ریشه‌ای را با معنی «شادی، خرسندی» بازسازی نکرده است: پوکورنی، والده-پوکورنی و واتکینز تنها ریشهٔ *bʰeu̯H- «بودن، شدن، بالیدن» را می‌شناسند و واژه‌هایی را که مان گرد آورده یا به همان ریشه یا به ریشه‌های دیگر می‌بندند. پس ریشه‌ای که نورایی آورده وفادارانه از منبعش نقل شده اما تنها بر یک مرجع تک‌رو تکیه دارد؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"%D8%A8%D9%88%DB%8C\", \"https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C%D9%87/\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:98\", \"status\": \"supports\",\n    \"note\": \"IEC.txt lines 1559–1606 (page marker '97' at 1559, running head 'bhóu- — bhragō ið 98'): 'bhóu- (3), bhou- \\\"joy, satisfaction\\\". … Per. būya, s. \\\"hope, desire\\\"; Pol. bawić, Cz. bavit \\\"amuse\\\"'. Nourai's root name, gloss and both daughter words come straight from this page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 146–150 s.v. bheu- : bheuə- : bhū-\", \"stance\": \"silent\",\n    \"note\": \"Pokorny has no root meaning 'joy, satisfaction'; the only bheu-/bhou- root is 'to be, grow, thrive'. Nothing there contradicts Mann outright, but nothing supports him either.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheuə- 'To be, exist, grow'\", \"stance\": \"silent\",\n    \"note\": \"The appendix's index (BE bheue-, BEAM bheue-, BUILD bheue-) shows only the 'be, grow' root; no 'joy' root is listed.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II (bheu- section)\", \"stance\": \"silent\",\n    \"note\": \"Same as Pokorny — WP treats bheu- as 'sein, wachsen, gedeihen' only.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Persian\", \"words\": \"bŭyeh «بوی ۲ ، بویه»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The word is real and the gloss is right: بویه būya 'longing, desire' is attested from the earliest classical poetry — Noushin's Vāže-nāmak s.v. بویه glosses it 'آرزو' and quotes Ferdowsī ('تو را بویهٔ دخت مهراب خاست') and Vīs-o-Rāmīn ('فتادش بویهٔ دیدار دلبر'); Dehkhodā and Moʿin both give only 'آرزومندی، آرزو' and neither offers an etymology. What is not independently supported is the arrow itself. Mann (IEC 98) is the sole authority who attaches بویه/بوی 'hope' to a root 'joy, satisfaction'. Iranian etymology recognises only bōy/bō 'smell, scent' (Horn no. 240: 'bōi, bō \\\"Geruch\\\" … aw. baoδi- \\\"Wohlgeruch\\\"; phlv. bōd, bōi', i.e. Av. baoδi- to baod- 'perceive, smell', PIE *bʰeudʰ-), and the ordinary Persian account of به بویِ آنکه 'in the hope that' is a figurative use of exactly that word ('on the scent of' → 'in hope of'), whence بویه = بوی + ـه. Nourai's Ḥāfeẓ citation ('به بویِ آنکه دگر نوبهار باز آید') is in fact the idiom that account rests on. So: possible, but resting on Mann alone against a straightforward alternative.\",\n \"derivation_fa\": \"خودِ واژه و معنی درست است: «بویه» به معنی «آرزو، آرزومندی» از کهن‌ترین شعر فارسی گواهی دارد — نوشین در «واژه‌نامک» آن را «آرزو» می‌داند و از فردوسی («تو را بویهٔ دخت مهراب خاست») و ویس و رامین شاهد می‌آورد؛ دهخدا و معین نیز تنها «آرزومندی» را ثبت کرده‌اند و هیچ ریشه‌شناسی به دست نمی‌دهند. آنچه پشتوانهٔ مستقل ندارد خودِ پیکان است: تنها مان این واژه را به ریشه‌ای با معنی «شادی» بسته است. ریشه‌شناسی ایرانی فقط bōy/bō «رایحه» را می‌شناسد (هرن شمارهٔ ۲۴۰: از اوستایی baoδi- «بوی خوش»، ستاک baod- «دریافتن، بوییدن»)، و تبیین رایج فارسی آن است که «به بویِ آنکه» کاربرد مجازی همان «بوی» است و «بویه» نیز «بوی + ـه». نکته آنکه شاهد خودِ نورایی از حافظ («به بویِ آنکه دگر نوبهار باز آید») درست همان اصطلاحی است که این تبیین بر آن استوار است. پس ادعای نورایی ممکن است اما تنها بر یک مرجع تکیه دارد؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C%D9%87/\", \"https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C/\", W + \"%D8%A8%D9%88%DB%8C\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:98\", \"status\": \"supports\",\n    \"note\": \"Mann p.98 s.v. bhóu- (3): 'Per. būya, s. \\\"hope, desire\\\"' — literally Nourai's word and gloss.\"},\n   {\"ref\": \"MON:607\", \"status\": \"partial\",\n    \"note\": \"Moʿin does have the headword (MON_part1.txt line 26242: 'بویه: (BUYE) (اِ.) آرزومندی'), so the word and gloss check out; but Moʿin gives no etymology, and the page number could not be verified because the copy on disk is the 2-volume Adena reprint with different pagination (the leaf carries the running number ۳۹۵).\"}\n ],\n \"consulted\": [\n   {\"src\": \"FSF\", \"where\": \"Noushin, Vāže-nāmak s.v. بویه (FSF_pages.txt lines 5668–5713)\", \"stance\": \"supports\",\n    \"note\": \"Headword بویه glossed 'آرزو' with Šāhnāme, Asadī and Vīs-o-Rāmīn attestations — the sense is confirmed for the 4th/10th–5th/11th c.\"},\n   {\"src\": \"HRN\", \"where\": \"no. 240 'bōi, bō \\\"Geruch\\\"' (HRN.txt line 2444)\", \"stance\": \"contradicts\",\n    \"note\": \"'240. bōi, bō \\\"Geruch\\\", bōyīden … aw. baoδi- \\\"Wohlgeruch\\\"; phlv. bōd, bōi, bōyīnītan'. Horn knows only the 'smell' word (root *bʰeudʰ-), not a 'desire' word from a root 'joy'; he has no entry بویه.\"},\n   {\"src\": \"MON\", \"where\": \"Moʿin s.v. بویه; Dehkhodā s.v. بویه (via abadis.ir)\", \"stance\": \"partial\",\n    \"note\": \"Dehkhodā: 'بویه. [ی َ / ی ِ] (اِ) آرزومندی' with Ferdowsī and Asadī shawāhid; Moʿin: '۱ - آرزومندی. ۲ - آرزو'. Meaning confirmed, etymology not addressed by either.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Sanskrit\", \"words\": \"bhâvita\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Sanskrit bhāvita- is a real word: it is the past participle of the causative bhāvayati of the root bhū- 'to be, become' (PIE *bʰuH-), and means 'brought into being, produced; cherished, fostered; purified; pervaded' and, of persons, 'well-disposed, favourably inclined'. Mann's gloss on the cited page is 'well-disposed' (p.98) and on his parallel p.77 entry 'elated'; Nourai's rendering 'well arranged' matches neither exactly and is not a standard gloss of the word. The arrow root→bhāvita is therefore as good as Mann's root itself: the word is genuine and its 'well-disposed, contented' sense fits the gloss 'joy, satisfaction', but morphologically it is simply a causative participle of bhū-, which every other authority assigns to *bʰuH- 'to be, grow'.\",\n \"derivation_fa\": \"واژهٔ سنسکریت bhāvita- واقعی است: اسم مفعولِ ستاک سببیِ bhāvayati از ریشهٔ bhū- «بودن، شدن» (هندواروپایی *bʰuH-) و به معنی «پدیدآورده، پرورده، پالوده، آکنده» و دربارهٔ کسان «خوش‌دل، مایل، خرسند». مان در ص۹۸ آن را «well-disposed» و در مدخل موازیِ ص۷۷ «elated» معنی کرده است؛ برگردانِ نورایی («well arranged» = «سامان‌یافته») با هیچ‌یک نمی‌خواند و معنی متعارف واژه نیست. خودِ واژه و معنیِ «خرسند» با ریشهٔ پیشنهادی مان سازگار است، اما از نظر ساخت صرفاً اسم مفعول سببیِ bhū- است که همهٔ مرجع‌های دیگر آن را زیر *bʰuH- «بودن، بالیدن» می‌آورند. با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0eyh%E2%82%82-\"],\n \"ref_check\": [\n   {\"ref\": \"IEC:98\", \"status\": \"supports\",\n    \"note\": \"IEC p.98 s.v. bhóu- (3) 'joy, satisfaction': 'Skt. cf. bhāvitaḥ \\\"well-disposed\\\"' — the word is there, though glossed 'well-disposed', not 'well arranged'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 146–150 s.v. bheu-, bheuə-, bhū- 'gedeihen, wachsen, werden, sein'\", \"stance\": \"partial\",\n    \"note\": \"Pokorny treats the whole Skt. bhū-/bhāv- family here; bhāvita- is a causative participle of that root, not of a separate 'joy' root.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheuə- 'To be, exist, grow'\", \"stance\": \"partial\",\n    \"note\": \"Same assignment: the Indic bhū-/bhav- forms belong to 'to be, exist, grow'; no 'joy' root exists in the appendix.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.77 s.v. bhəu- 'please'\", \"stance\": \"supports\",\n    \"note\": \"'bhəu- \\\"please\\\". Cf. bhou- (3). Skt. cf. bhavilah \\\"good; lecher\\\" beside bhavitah \\\"elated\\\"; Per. cf. būye (s. \\\"hope, desire\\\")' — Mann's duplicate treatment of the same material.\"}\n ]\n})\n\ndata[\"entries\"].append(e2)\n\n# ---------------- entry 9 : Bhru 1 ----------------\ne9 = {\n \"entry\": 9,\n \"root\": \"Bhru 1\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *h₃bʰruH- (nom. *h₃bʰrúHs) 'eyebrow' (Pokorny '1. bhrū- \\\"Augenbraue\\\"', IEW 172); the 'beam, log, bridge' sense is Pokorny's separate lemma '2. bhrū-, bhreu- \\\"Balken, Prügel; auch als Übergang über ein Gewässer: Brücke\\\"' (IEW 173).\",\n \"note\": \"The page reference is right and the language label and the 'eyebrow' half of the gloss are right. The extra 'beam, log' in the gloss belongs to Pokorny's SECOND lemma on the following page, which Pokorny keeps apart (he only records that Specht assumed a connection). Nourai's single box thus merges IEW 172 and 173. He is following Watkins, who does the same — AHD_watkins1985 s.v. bhrū-: 'Eyebrow. Contracted from *bhruə-. 1. Germanic *brūs in Old English brū … BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugjō (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE. [Pok. 1. bhrū- 172, 2. bhrū- 173.]' — and the wording of Nourai's gloss ('beam, log') is Klein's, s.v. bridge, 'I.-E. base *bhru-, *bhreu-, \\\"beam, log\\\"'. Wiktionary derives Proto-Germanic *brugjǭ from *h₃bʰruH-íh₂-s but marks the etymology uncertain and notes that if Gaulish brīuā 'bridge' belongs here the root would have to be *(h₃)bʰreh₁w-. Verdict: the eyebrow root is confirmed; the merger with 'beam/bridge' is possible but not established.\",\n \"note_fa\": \"شمارهٔ صفحه درست است و برچسب زبانی و نیمهٔ نخست معنی («ابرو») نیز درست‌اند. اما «تیر، کندهٔ چوب» در معنیِ ریشه از مدخل دومِ پوکورنی (ص۱۷۳) می‌آید که او آن را جدا نگاه داشته است؛ نورایی دو مدخل ۱۷۲ و ۱۷۳ را در یک جعبه ادغام کرده است. در این کار پیرو واتکینز است که در پیوستِ ریشه‌های هندواروپاییِ فرهنگ American Heritage همین ادغام را با قید «possibly» انجام داده، و عبارتِ «beam, log» نیز عیناً از کلاین (ذیل bridge) گرفته شده است. ویکی‌واژه *brugjǭ ژرمنی را از *h₃bʰruH-íh₂-s می‌گیرد اما ریشه‌شناسی را ناتمام می‌داند. نتیجه: ریشهٔ «ابرو» تأیید می‌شود، اما یکی‌دانستن آن با «تیر/پل» تنها احتمالی است؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\", W + \"%D8%A7%D8%A8%D8%B1%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"POK:172\", \"status\": \"partial\",\n    \"note\": \"POK_01.txt (printed p.172–173): '1. bhrū- ,Augenbraue‘, z. T. mit anlautendem Vokal, idg. o- oder a- … Ai. bhrū́-ḥ f., Akk. bhrúv-am ,Braue‘, av. brvat- f. (Du.) ,Brauen‘, npers. ebrū, brū ds. (Hübschmann IA. 10, 24)'. The page supports the eyebrow root exactly; but the 'beam, log' gloss comes from the next lemma, '2. bhrū-, bhreu- ,Balken, Prügel‘ … ,Brücke‘', printed on p.173 and kept separate by Pokorny.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhrū- (AHD_watkins1985.txt line 344)\", \"stance\": \"supports\",\n    \"note\": \"'bhrū-. Eyebrow. Contracted from *bhruə-. 1. Germanic *brūs in Old English brū, eyebrow, eyelid, eyelash: BROW. 2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugjō … BRIDGE. [Pok. 1. bhrū- 172, 2. bhrū- 173.]' — Nourai's merged root box, hedged with 'Possibly'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II 206–207 (WLD_Bd2_pages.txt leaves 211–212)\", \"stance\": \"supports\",\n    \"note\": \"Running head 'bhres — bhru-' on p.206 and 'bhru-, bhreu- 207'; '1. bhru- \\\"Augenbrauen\\\" … Ai. bhrūḥ, acc. bhruvam \\\"Braue\\\", av. brvat- f. (du.) \\\"Brauen\\\", np. abrū, barū ds. (Hübschmann IA. 10, 24)'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. bridge and s.v. brow (KLN_1966.txt lines 5629, 5731)\", \"stance\": \"partial\",\n    \"note\": \"Klein keeps the two apart: brow 'fr. OE. brū … cogn. with OI. bhrūḥ, Avestic brvat-, ModPers. abrū, brū, Gk. ὀφρύς'; bridge 'prob. orig. \\\"bridge of beams\\\", and derived fr. I.-E. base *bhru-, *bhreu-, \\\"beam, log\\\"'. Nourai's gloss 'beam, log' is Klein's phrase, but Klein does not identify the two bases.\"}\n ],\n \"nodes\": []\n}\n\ne9[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"brvat\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan brvat- f., attested in the dual brvaṱbyąm 'the two eyebrows' (Vd. 15.16, 9.15–16 — Bartholomae, AiW col. 972 quotes 'antarāt̰ naēmāt̰ brvat̰byąm upa-dvąsaiti'). It continues Proto-Iranian *HbruH-at- / *HbrúHs, from Proto-Indo-Iranian *HbʰrúHs and PIE *h₃bʰrúHs, the u-stem being extended by -at- in Avestan (cf. Skt. bhrū́-ḥ, acc. bhrúvam, without the extension). Pokorny 172 and Walde-Pokorny II 206 both cite the form in exactly this shape and meaning, and Macedonian ἀβροῦτες is kept in the file precisely because of Av. brvat-.\",\n \"derivation_fa\": \"«brvat-» صورتی اوستایی و مؤنث است که در تثنیهٔ brvaṱbyąm «دو ابرو» در وندیداد (۱۵٫۱۶ و ۹٫۱۵–۱۶) گواهی شده و بارتولمه در «فرهنگ ایرانی باستان» (ستون ۹۷۲) آن را با همین شاهدها آورده است. این صورت از ایرانی باستان *HbruH-at- و هندوایرانی آغازین *HbʰrúHs و سرانجام هندواروپایی آغازین *h₃bʰrúHs می‌آید؛ ستاکِ u در اوستایی با پسوند -at- گسترش یافته است، در برابر سنسکریت bhrū́-ḥ و رایی bhrúvam که بی‌پسوند است. پوکورنی (ص۱۷۲) و والده-پوکورنی (ج۲ ص۲۰۶) همین صورت و همین معنی را ثبت کرده‌اند. ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\", W + \"%D8%A7%D8%A8%D8%B1%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"POK\", \"status\": \"supports\",\n    \"note\": \"The node cites POK without a page; the relevant page is IEW 172: 'av. brvat- f. (Du.) ,Brauen‘' (POK_01.txt line 2501).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW col. 972 s.v. brvat- (BRT.txt line 17469)\", \"stance\": \"supports\",\n    \"note\": \"'j. brvat- f. \\\"Augenbraue\\\", Du. … V. 15, 16, 9. 15, 16 … np. abrū, barū … — Pū.: brūk.' — the Avestan word, its Pahlavi and its New Persian continuants in one entry.\"},\n   {\"src\": \"WLD\", \"where\": \"WP II 206\", \"stance\": \"supports\",\n    \"note\": \"'av. brvat- f (du.) \\\"Brauen\\\", np. abrū, baru ds. (Hubschmann IA. 10, 24)'.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp.77–78 (entry ابرو), cognate column\", \"stance\": \"supports\",\n    \"note\": \"'اوستایی (AVESTAN): BRAVAT' beside 'پهلوی (PAHLAVI): BRUG, BRUK' and 'سانسکریت (SANSKRIT): BHROH, BHRUS', with references to Pokorny, MacKenzie (BROW 105) and Buck 219.\"}\n ]\n})\n\ne9[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"brŭk\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The Middle Persian word is written <blwk'> in Book Pahlavi and read brūg by MacKenzie ('brūg [blwk' | M brwg, N abrū] (eye)brow', Concise Pahlavi Dictionary); the older Iranist tradition, which Nourai follows through Borhān, reads the same spelling brūk — Bartholomae ends his brvat- article 'Pū.: brūk', and Moʿin's footnote to ابرو in Borhān-e Qāṭeʿ p.80 prints the Pahlavi form in the same shape. The -k/-g alternation is purely a matter of transliteration convention for Pahlavi final stops, not a different word, so brŭk is not an error. Formally it is Old Iranian *bruH-ka-/*bruH-ah with the productive -ak/-ag suffix, continuing the Avestan-type stem; Manichaean Middle Persian has brwg, confirming the -g.\",\n \"derivation_fa\": \"صورت فارسی میانه در پهلویِ کتابی <blwk'> نوشته می‌شود؛ مکنزی آن را brūg می‌خواند («brūg [blwk' | M brwg, N abrū] (eye)brow») و سنت کهن‌تر ایران‌شناسی — که نورایی از رهگذر حاشیهٔ معین بر برهان قاطع (ص۸۰) دنبال کرده — همان را brūk خوانده است؛ بارتولمه نیز در پایان مدخل brvat- می‌نویسد «Pū.: brūk». پس اختلافِ k/g تنها اختلاف شیوهٔ آوانویسیِ واکه‌های پایانی پهلوی است و صورت brŭk خطا نیست. از نظر ساخت، *bruH-aka- ایرانی باستان با پسوند پرکار -ak/-ag است؛ فارسی میانهٔ مانوی brwg نیز «گ» را تأیید می‌کند. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%A7%D8%A8%D8%B1%D9%88\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:80\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 290 = printed p.80 (the leaf ends 'بقیه از صفحهٔ ۷۹' and carries the signature '( برهان قاطع ۱۵ )'). Moʿin's starred footnote to ابرو reads: '* ابرو - اوستا [brvat], سانسکریت [bhrū], پهلوی [brūk] … فارسی ابرو و برو «بارتولمه» … «اونوالا ۴۰۱»'. Exactly the Pahlavi form Nourai prints, on exactly the cited page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.19 s.v. brūg (PHD.txt line 292; PHD_mackenzie.txt line 1639)\", \"stance\": \"supports\",\n    \"note\": \"'brūg [blwk' | M brwg, N abrū] (eye)brow' — the same word, read with final -g.\"},\n   {\"src\": \"BRT\", \"where\": \"AiW col. 972, end of the brvat- article\", \"stance\": \"supports\",\n    \"note\": \"'— Pū.: brūk' — Bartholomae's Pahlavi form is literally Nourai's brŭk.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp.77–78, cognate column\", \"stance\": \"supports\",\n    \"note\": \"'پهلوی (PAHLAVI): BRUG, BRUK' — Aryanpur records both readings side by side.\"}\n ]\n})\n\ne9[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"abrŭ, borŭ «ابرو ، بُرو»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian ابرو abrū continues Middle Persian brūg: final -g was lost in the passage to New Persian (as in MP dārūg > NP dārū), and an anaptyctic/prothetic a- was added before the initial br- cluster, which New Persian does not tolerate word-initially — hence abrū beside the older, unprothesised بُرو burū/barū, kept as a poetic doublet. Pokorny 172 prints 'npers. ebrū, brū'; Bartholomae and Walde-Pokorny II 206 both print 'np. abrū, barū'; Klein s.v. brow has 'ModPers. abrū, brū'; Wiktionary gives ابرو < MP brūg (blwk') < Proto-Iranian *HbrúHs, with برو (baru/borū) marked archaic and poetic. Ferdowsī uses the short form in the line Nourai quotes: 'سیاوش ز گفت گروی زره / برو کرد پرچین، رخان پر گره'.\",\n \"derivation_fa\": \"«ابرو» دنبالهٔ فارسی میانهٔ brūg است: «گ» پایانی در گذر به فارسی نو افتاده (مانند dārūg > دارو) و چون خوشهٔ آغازینِ br- در فارسی نو روا نیست، واکهٔ آغازینِ «اَ» بدان افزوده شده است؛ از این‌رو «ابرو» در کنار صورت کهن‌ترِ بی‌پیش‌واکهٔ «بُرو» که همچنان صورتی شاعرانه مانده است. پوکورنی (ص۱۷۲) «npers. ebrū, brū» و بارتولمه و والده-پوکورنی «np. abrū, barū» و کلاین «ModPers. abrū, brū» ثبت کرده‌اند؛ ویکی‌واژه نیز ابرو را از brūg فارسی میانه و ایرانی باستان *HbrúHs می‌گیرد و «برو» را کهن و شعری می‌داند. فردوسی همان صورت کوتاه را در بیتی که نورایی آورده به کار برده است. ادعای نورایی درست است.\",\n \"sources\": [W + \"%D8%A7%D8%A8%D8%B1%D9%88\", W + \"Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\"],\n \"ref_check\": [\n   {\"ref\": \"POK:172\", \"status\": \"supports\",\n    \"note\": \"'npers. ebrū, brū ds. (Hübschmann IA. 10, 24)' (POK_01.txt line 2501, printed p.172) — both of Nourai's Persian forms.\"},\n   {\"ref\": \"BQT:80\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt leaf 290 (printed p.80), Moʿin's footnote to ابرو: '… فارسی ابرو و برو «بارتولمه» … مخفف آن برو' — the two forms and the note that برو is the shortened variant.\"},\n   {\"ref\": \"FSF:81\", \"status\": \"supports\",\n    \"note\": \"FSF_pages.txt leaf 106 (≈ printed p.81): headword 'برو (باپیش)' glossed 'مخفف ابرو', illustrated with the very verse Nourai quotes: 'سیاوش ز گفت گروی زره / برو کرد پرچین، رخان پر گره'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. brow (KLN_1966.txt line 5731)\", \"stance\": \"supports\",\n    \"note\": \"'ME. browe, fr. OE. brū … cogn. with OI. bhrūḥ, Toch. A pärwāṃ (dual), Avestic brvat-, ModPers. abrū, brū, Gk. ὀφρύς, OSlav. brŭvĭ, Lith. bruvis'.\"},\n   {\"src\": \"WLD\", \"where\": \"WP II 206\", \"stance\": \"supports\",\n    \"note\": \"'np. abrū, barū ds. (Hubschmann IA. 10, 24)' — note that Walde-Pokorny and Bartholomae vocalise the short form barū, Nourai (with Moʿin) borū; both are recorded readings of «بُرو».\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. brūg\", \"stance\": \"supports\",\n    \"note\": \"'[blwk' | M brwg, N abrū]' — MacKenzie himself names New Persian abrū as the continuant.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur pp.77–78 (ابرو)\", \"stance\": \"supports\",\n    \"note\": \"Entry built on exactly this chain (Avestan BRAVAT → Pahlavi BRUG/BRUK → Persian), citing Pokorny, MacKenzie 105, Onions 121, Skeat 76, Buck 219, Barnhart 120–121.\"}\n ]\n})\n\ne9[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Germanic\", \"words\": \"brus\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Nourai's Germanic *brus is Watkins's exact reconstruction: AHD (Watkins 1985) s.v. bhrū- '1. Germanic *brūs in Old English brū, eyebrow, eyelid, eyelash: BROW'. The form is the inherited root-noun *h₃bʰrúH-s carried into Germanic; Old English brū and Old Norse brún (pl. brýnn) actually continue a consonant stem *brū-w-ōn- (Pokorny 173: 'ags. brū, aisl. brún, Pl. brynn \\\"Braue\\\" (kons. St., aus *brūwōn-)'), so modern handbooks prefer Proto-Germanic *brūwō (beside *brēwō). The gloss 'eyebrow' is right and the descent from the root box is uncontroversial.\",\n \"derivation_fa\": \"صورتِ *brus که نورایی «ژرمنی» خوانده، دقیقاً بازسازی واتکینز است: در پیوستِ ریشه‌های هندواروپاییِ American Heritage ذیل bhrū- آمده «Germanic *brūs in Old English brū … BROW». این همان ستاکِ ریشه‌ایِ *h₃bʰrúH-s است که به ژرمنی رسیده؛ اما انگلیسی کهن brū و ایسلندی کهن brún (جمع brynn) در واقع ستاکِ همخوانیِ *brū-w-ōn- را ادامه می‌دهند (پوکورنی ص۱۷۳) و از این‌رو کتاب‌های امروزی *brūwō (در کنار *brēwō) را ترجیح می‌دهند. معنی «ابرو» و پیوند با ریشه بی‌چون‌وچرا درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 344, s.v. bhrū-: '1. Germanic *brūs in Old English brū, eyebrow, eyelid, eyelash: BROW.' Literally Nourai's form, language label and gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. brow\", \"stance\": \"supports\",\n    \"note\": \"'ME. browe, fr. OE. brū, rel. to ON. brún, \\\"brow\\\"' — the Germanic material, though Klein does not set up a starred Germanic form.\"},\n   {\"src\": \"POK\", \"where\": \"IEW 173\", \"stance\": \"supports\",\n    \"note\": \"'ags. brū, aisl. brún, Pl. brynn \\\"Braue\\\" (kons. St., aus *brūwōn-, vgl. *tungūn, tungō, kontrahiert …)'.\"},\n   {\"src\": \"WLD\", \"where\": \"WP II 207\", \"stance\": \"supports\",\n    \"note\": \"'ags. brū, aisl. brūn, pl. brynn \\\"Braue\\\" (kons. St. …)'.\"}\n ]\n})\n\ne9[\"nodes\"].append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"brow, eyebrow\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old English brū (a consonant-stem feminine, 'eyebrow, eyelid, eyelash') gives Middle English browe and Modern English brow with the regular loss of final -e and the ME long ū > /aʊ/ of the Great Vowel Shift. Eyebrow is a Middle English re-compounding of eye + brow (c.1300), replacing Old English ēag-brū / ēag-bræw. Klein s.v. brow gives the whole chain, and Watkins lists BROW as the English derivative of bhrū-. This is an uncontroversial native Germanic chain.\",\n \"derivation_fa\": \"انگلیسی کهن brū (اسم مؤنثِ ستاک‌همخوانی، به معنی «ابرو، پلک، مژه») به انگلیسی میانهٔ browe و سپس brow امروزی رسیده است؛ «ـه» پایانی افتاده و ū کشیدهٔ انگلیسی میانه در «جابه‌جایی بزرگ واکه‌ها» به /aʊ/ بدل شده است. «eyebrow» ترکیبی است از eye + brow در انگلیسی میانه (نزدیک ۱۳۰۰ م) که جای ēag-brū انگلیسی کهن را گرفت. کلاین همهٔ این زنجیره را آورده و واتکینز نیز BROW را بازماندهٔ انگلیسیِ ریشهٔ bhrū- می‌داند. زنجیره‌ای بومی و بی‌مناقشه است؛ ادعای نورایی درست است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference in the book (refs=None). The link is nevertheless covered by the parent node's AHD citation ('Germanic *brūs in Old English brū … BROW').\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. brow (KLN_1966.txt line 5731)\", \"stance\": \"supports\",\n    \"note\": \"'brow, n. — ME. browe, fr. OE. brū, rel. to ON. brún, \\\"brow\\\" … OE. brǣw, \\\"eyelid\\\", is not related to brow.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. bhrū- and index 'BROW bhrū-'\", \"stance\": \"supports\",\n    \"note\": \"BROW is listed in the English index under bhrū-.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt lines 1678, 7143)\", \"stance\": \"partial\",\n    \"note\": \"The OCR of Skeat's own 'Brow' entry is unrecoverable, but his cross-references confirm his treatment: s.v. Boar 'Probably connected with Brow'; s.v. Front 'O.F. front, forehead, brow … Allied to Brow.'\"}\n ]\n})\n\ne9[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Germanic\", \"words\": \"brugjô\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Proto-Germanic *brugjō 'bridge' is well established (OE brycg, OS bruggia, OFris. brigge, MDu. brug, OHG brucca, ON brú and bryggja 'landing-stage'), and Nourai's form and gloss are Watkins's. What is only probable is the arrow from THIS root: Pokorny files the word under a separate lemma, '2. bhrū-, bhreu- \\\"Balken, Prügel\\\"; auch als Übergang über ein Gewässer: \\\"Brücke\\\"' (IEW 173), together with Gaulish brīva 'bridge', OCS brŭvĭno 'beam' and Serbo-Croat brv 'footbridge', and he adds that the guttural of the Germanic forms is unexplained ('*brugi- aus *bruwi-, oder k-Suffix?'), noting only that Specht assumed a connection with 1. bhrū- 'eyebrow'. Watkins merges the two with 'Possibly'; Wiktionary derives *brugjǭ from *h₃bʰruH-íh₂-s but flags the etymology as incomplete and observes that if Gaulish brīuā belongs here the root would have to be *(h₃)bʰreh₁w-. The semantics ('log' > 'log bridge') are unproblematic; the identity of the two roots is not proven.\",\n \"derivation_fa\": \"صورت ژرمنیِ آغازین *brugjō «پل» به‌خوبی گواهی شده است (انگلیسی کهن brycg، ساکسون کهن bruggia، هلندی میانه brug، آلمانی علیای کهن brucca، ایسلندی کهن brú و bryggja) و صورت و معنایی که نورایی آورده از واتکینز است. آنچه تنها «احتمالی» است پیوند این واژه با ریشهٔ «ابرو» است: پوکورنی آن را زیر مدخل جداگانهٔ «2. bhrū-, bhreu- تیر، چوب‌دست؛ و نیز گذرگاه روی آب: پل» (ص۱۷۳) می‌آورد، همراه با گُلیِ brīva «پل»، اسلاوی کهن brŭvĭno «تیر» و صربی brv «پل باریک»، و می‌افزاید که «گ» صورت‌های ژرمنی توضیح‌ناپذیر است. واتکینز این دو را با قید «possibly» یکی می‌گیرد و ویکی‌واژه نیز ریشه‌شناسی را ناتمام می‌داند. تحول معنایی («کندهٔ چوب» ← «پلِ چوبی») مشکلی ندارد، اما یکی‌بودنِ دو ریشه اثبات نشده است؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 344, s.v. bhrū-: '2. Possibly in the sense of a beam of wood, and perhaps a log bridge, found in Germanic *brugjō (with cognates in Celtic and Slavic) in Old English brycg(e), bridge: BRIDGE.' Nourai's form and gloss ('wooden bridge') are Watkins's, including the hedge Nourai drops.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 173 s.v. 2. bhrū-, bhreu-\", \"stance\": \"partial\",\n    \"note\": \"'2. bhrū-, bhreu- \\\"Balken, Prügel\\\"; auch als Übergang über ein Gewässer: \\\"Brücke\\\". Aisl. brú f. \\\"Brücke\\\" … ahd. brucca, ags. brycg … gall. briva \\\"Brücke\\\" (*bhreua); abg. brŭvŭno \\\"Balken\\\" … Unklar ist der Guttural in den germ. Formen: *brugi- aus *bruui-, oder k-Suffix? … Specht … der Zusammenhang mit 1. bhrū- annimmt.' A separate lemma, with the identification credited to Specht alone.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. bridge (KLN_1966.txt line 5629)\", \"stance\": \"partial\",\n    \"note\": \"'ME. brigge, brig, fr. OE. brycg, bricg … prob. orig. \\\"bridge of beams\\\", and derived fr. I.-E. base *bhru-, *bhreu-, \\\"beam, log\\\", whence also Gaulish briva, \\\"bridge\\\", OSlav. brŭvŭno, \\\"beam\\\", Serb. brv, \\\"footbridge\\\".' Klein confirms the Germanic form and the 'beam, log' base but does not identify it with the 'eyebrow' base.\"},\n   {\"src\": \"WLD\", \"where\": \"WP II 207\", \"stance\": \"supports\",\n    \"note\": \"Continues the '2. bhrū-, bhreu-' article on p.207 with the same Germanic, Gaulish and Slavic material.\"}\n ]\n})\n\ne9[\"nodes\"].append({\n \"id\": 7, \"lang\": \"English\", \"words\": \"bridge\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old English brycg (also bricg) < West Germanic *bruggju < Proto-Germanic *brugjō, with i-umlaut of u > y before the -j- and West Germanic gemination plus palatalisation of -gj- to <cg> /ddʒ/. ME brigge/brugge/brygge gives Modern English bridge; the northern un-palatalised variant survives as Scots brig. Klein s.v. bridge sets out the whole chain, and Watkins lists BRIDGE as the English derivative of the Germanic form of the previous node. The Germanic→English step is entirely regular and uncontroversial (only the deeper attachment to the 'eyebrow' root, judged at node 6, is doubtful).\",\n \"derivation_fa\": \"انگلیسی کهن brycg (و bricg) از ژرمنی غربیِ *bruggju و آن از ژرمنی آغازینِ *brugjō می‌آید: «u» زیر تأثیر -j- به y بدل شده (i-umlaut)، و -gj- در ژرمنی غربی مشدد و سپس کامی شده و به cg /ddʒ/ رسیده است. صورت انگلیسی میانهٔ brigge/brugge به bridge امروزی انجامیده و گونهٔ شمالیِ کامی‌نشده در اسکاتلندی brig بازمانده است. کلاین همهٔ این زنجیره را آورده و واتکینز نیز BRIDGE را بازماندهٔ *brugjō می‌داند. این گام کاملاً قاعده‌مند و بی‌مناقشه است؛ تنها پیوند ژرف‌ترِ آن با ریشهٔ «ابرو» (که در گرهٔ ۶ سنجیده شد) تردیدآمیز است.\",\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The node carries no reference in the book (refs=None); the link is covered by the parent node's AHD citation ('Germanic *brugjō … in Old English brycg(e), bridge: BRIDGE').\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. bridge (KLN_1966.txt line 5629)\", \"stance\": \"supports\",\n    \"note\": \"'bridge, n., structure spanning a river, etc. — ME. brigge, brig, etc., fr. OE. brycg, bricg, rel. to OS. bruggia, ON. bryggja, brú, Dan. bro, Swed. brygga, OFris. brigge, bregge, Du. brug, OHG. brucca, G. Brücke.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. bhrū-; index 'BRIDGE'\", \"stance\": \"supports\",\n    \"note\": \"'… in Old English brycg(e), bridge: BRIDGE.'\"},\n   {\"src\": \"POK\", \"where\": \"IEW 173\", \"stance\": \"supports\",\n    \"note\": \"'ahd. brucca, as. -bruggia, ags. brycg \\\"Brücke\\\" … ags. brycgian \\\"pflastern\\\" (ursprgl. mit Holzprügeln)'.\"}\n ]\n})\n\ndata[\"entries\"].append(e9)\n\nwith io.open(\"data/verification/page-97.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk97.py && python3 -m json.tool data/verification/page-97.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 97",
 "description": "Write and validate page-97.json"
}
```


### [2026-09-05T14:47:51.989Z] TOOL RESULT

```
written
JSON OK
nodes verified: 13/13
node verdicts: {'plausible': 5, 'confirmed': 8}
root verdicts: {'confirmed': 1, 'plausible': 2}
ref checks: {'supports': 14, 'not_checked': 3, 'partial': 2, 'not_found': 1}
books consulted: {'supports': 30, 'partial': 8, 'silent': 1, 'contradicts': 1} | by book: {'ARY': 6, 'POK': 5, 'KLN': 5, 'WLD': 4, 'BRT': 3, 'PHD': 3, 'AHD': 3, 'HRN': 2, 'BQT': 2, 'MON': 2, 'IEC': 2, 'SYN': 1, 'FSF': 1, 'SKT': 1}
```


## [2026-09-05T14:48:18.084Z] AGENT

`verify_check.py 97` reports 0 PROBLEM lines. Written to `/home/sfmqrb/git/rishe/data/verification/page-97.json`.

**Page 97 (book p. 67) — 3 real entries, 13 nodes** (6 redirect entries skipped)
- Node verdicts: 8 confirmed, 5 plausible. Root verdicts: 1 confirmed (Bhôi), 2 plausible (Bhôu/Bheu, Bhru 1).
- Ref checks: 14 supports, 2 partial, 1 not_found, 3 not_checked. 39 `consulted` entries across 14 books (POK, WLD, AHD/Watkins, KLN, BRT, PHD, HRN, HUB-via-POK, BQT, MON, IEC, SYN, FSF, ARY, SKT).

Notable findings (no `disputed`, no `transcription_suspect`, no extraction errors):
- **Bhôi #1 Avestan `bhâyaka`** — plausible: `bay-` is a genuine Avestan verbal root (BRT cols. 927–928), but `bhâyaka` is not Avestan; it is Horn's/Pokorny's reconstructed *\*bhāyaka-* behind NP باک (an Avestan form would be *\*bāyaka-*, Avestan has no bh). Book faithfully extracted; it is Nourai's mislabel of a starred form as attested.
- **Bhôi #4 Persian بیمه** — plausible: his own ref MON:633 says the opposite of the arrow — Moʿin has "[اردو و هند. < بیماه ضمانت]". Wiktionary keeps both routes open (بیم + ـه, or Indo-Aryan from Skt bhīmá-); either way the root box is right. The chart's NOTE is accurate to Mann (IEC 723: "Per. bi-me ('insurance', fr. *\*uid-ma*?)"), but that *\*weid-* idea is rejected by everyone since; IEC:1562 could not be located (the local OCR's page markers stop at ~1554).
- **Bhôu/Bheu (whole entry)** — plausible: IEC:98 is verbatim right ("bhóu- (3) 'joy, satisfaction' … Per. būya"), but Mann is the *only* authority for such a root; Pokorny/WP/Watkins know only bheu- 'to be, grow'. For بویه, Horn (no. 240) knows only bōi 'smell' < Av. baoδi-, and the ordinary Persian account makes به بویِ آنکه (Nourai's own Ḥāfeẓ shāhed) the figurative use of that word.
- **Bhru 1 root** — plausible: POK:172 supports only the 'eyebrow' half; 'beam, log' is Pokorny's *separate* lemma 2. bhrū- on p. 173. Nourai's merger follows Watkins ("Possibly…") and borrows Klein's phrase "beam, log"; Wiktionary flags the bridge link as uncertain. Node #6 (Gmc *brugjô*) marked plausible for the same reason.
- Strong confirmations: HRN:39 (no. 170 bāk) and HRN:59 (no. 58 bīm) are both exactly right; BQT:80 is exactly the ابرو page with Moʿin's footnote giving Pahlavi *brūk*; BQT:340 is the بیم page (independently corroborated — Aryanpur cites "برهان قاطع ۳۴۰" for بیم); FSF:81 is the بُرو entry with the very Ferdowsī verse Nourai quotes.
- AEF:320 not checkable (no scan of Khaleqi Motlaq's translation of Horn anywhere); MON:607/633 pages unverifiable because only the 2-vol Adena reprint is on disk (different pagination) — entries themselves located and quoted.

9 web pages archived via `fetch_source.py` (Wiktionary ×6, abadis ×2, PIE reconstruction pages).
