# Verification process log — verify-page-95


## [2026-09-05T14:06:24.204Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 95 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-95.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-95.json. Write /home/sfmqrb/git/rishe/data/verification/page-95.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 95` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:06:25.856Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:06:26.535Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:06:26.549Z] TOOL RESULT

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


## [2026-09-05T14:06:26.733Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-95.txt"
}
```


### [2026-09-05T14:06:26.747Z] TOOL RESULT

```
1	=== PDF page 95 (book page 65) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bheudh : to be aware, enlighten  (refs POK:150)
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:151; BQT:311; FFD:39 | baoidi, baodhi, baud-a : nice aroma
5	  #2 (parent #1) [Persian] refs=BQT:311 | bŭy «بوی» : smell, aroma ; bŭy-yîdan «بوییدن» : to smell ; bŭ-stân «بوستان» : place of flowers ☞Stâ | extra: بو۱
6	  #3 (parent #1) [Avestan / Old Persian] refs=FFD:40 | pati-baus : to smell, expect, guess
7	    #4 (parent #3) [Pahlavi] refs=FFD:40 | payôs : expect
8	      #5 (parent #4) [Persian] refs=FSF:98; FFD:40; BQT:342 | bîyŭsîdan «بیوسیدن» : expect, hope ; bîyŭsandeh «بیوسنده» : hopeful ; nâ-bîyŭsân «نابیوسان» : unexpected | extra: بیوس
9	  #6 (parent #1) [Sogdian] refs=SOD:113 | bws : incense
10	#7 (parent #0) [Sanskrit] refs=AHD | bŭdhati : he awakes ; bŭdha : wise, aware
11	  #8 (parent #7) [Persian] refs=BQT:313 | bŭdâ «بودا» : Indian philosopher
12	  #9 (parent #7) [English] refs=AHD | Buddha
13	#10 (parent #0) [Germanic] refs=AHD | 
14	  #11 (parent #10) [English] refs=None | bid, forbid
15	--- entry 1 ---
16	ROOT [Indo-European] Bheug, Bheugh : to purify, save, free  (refs POK:152)
17	#1 (parent #0) [Avestan] refs=POK:152 | baog, bunja : to save ; baoxtar : rescuer
18	  #2 (parent #1) [Pahlavi] refs=POK:152; SNS:106 | bôxtan : to save, free ; bôzišn : pardon
19	    #3 (parent #2) [Persian] refs=SNS:96,106,107; MON:476 | boxt «بُخت ۲» : saved, rescued, forgiven ; pŭzîdan «پوزیدن» : to ask for pardon | extra: پوزش ، پوز
20	#4 (parent #0) [Old Persian] refs=KNT:199 | baug : to set free ; baga-buxša : God-freed ☞Bhag
21	  #5 (parent #4) [None] refs=None | 
22	#6 (parent #0) [Latin] refs=POK:152; AHD | fugere : to flee
23	  #7 (parent #6) [English] refs=AHD | fugitive, centrifugal, refuge
24	--- entry 2 ---
25	ROOT Bheugh -> redirect to Bheug
26	
```


## [2026-09-05T14:06:30.136Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-95.json",
 "description": "Read source JSON for page 95"
}
```


### [2026-09-05T14:06:30.174Z] TOOL RESULT

```
{
  "pdf_page": 95,
  "book_page": 65,
  "entries": [
    {
      "root": {
        "name": "Bheudh",
        "lang": "Indo-European",
        "refs": "POK:150",
        "gloss": "to be aware, enlighten"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:151; BQT:311; FFD:39",
          "words": [
            {"translit": "baoidi, baodhi, baud-a", "gloss": "nice aroma", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:311",
          "words": [
            {"translit": "bŭy", "gloss": "smell, aroma", "script": "بوی"},
            {"translit": "bŭy-yîdan", "gloss": "to smell", "script": "بوییدن"},
            {"translit": "bŭ-stân", "gloss": "place of flowers", "script": "بوستان", "see": ["Stâ"]}
          ],
          "script_extra": "بو۱",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:40",
          "words": [
            {"translit": "pati-baus", "gloss": "to smell, expect, guess", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "FFD:40",
          "words": [
            {"translit": "payôs", "gloss": "expect", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "FSF:98; FFD:40; BQT:342",
          "words": [
            {"translit": "bîyŭsîdan", "gloss": "expect, hope", "script": "بیوسیدن"},
            {"translit": "bîyŭsandeh", "gloss": "hopeful", "script": "بیوسنده"},
            {"translit": "nâ-bîyŭsân", "gloss": "unexpected", "script": "نابیوسان"}
          ],
          "script_extra": "بیوس",
          "note": null,
          "quote": {
            "text": "برآمد یکی نابیوسان نبرد - که دریا همه خون شد و دشت گرد",
            "poet": "Asadî"
          }
        },
        {
          "id": 6,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:113",
          "words": [
            {"translit": "bws", "gloss": "incense", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD",
          "words": [
            {"translit": "bŭdhati", "gloss": "he awakes", "script": null},
            {"translit": "bŭdha", "gloss": "wise, aware", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT:313",
          "words": [
            {"translit": "bŭdâ", "gloss": "Indian philosopher", "script": "بودا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Buddha", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "bid, forbid", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bheug, Bheugh",
        "lang": "Indo-European",
        "refs": "POK:152",
        "gloss": "to purify, save, free"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:152",
          "words": [
            {"translit": "baog, bunja", "gloss": "to save", "script": null},
            {"translit": "baoxtar", "gloss": "rescuer", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "POK:152; SNS:106",
          "words": [
            {"translit": "bôxtan", "gloss": "to save, free", "script": null},
            {"translit": "bôzišn", "gloss": "pardon", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:96,106,107; MON:476",
          "words": [
            {"translit": "boxt", "gloss": "saved, rescued, forgiven", "script": "بُخت ۲"},
            {"translit": "pŭzîdan", "gloss": "to ask for pardon", "script": "پوزیدن"}
          ],
          "script_extra": "پوزش ، پوز",
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:199",
          "words": [
            {"translit": "baug", "gloss": "to set free", "script": null},
            {"translit": "baga-buxša", "gloss": "God-freed", "script": null, "see": ["Bhag"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:152; AHD",
          "words": [
            {"translit": "fugere", "gloss": "to flee", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "fugitive, centrifugal, refuge", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Bheugh",
        "redirect": "Bheug"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-05T14:06:32.309Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','FFD','FSF','SOD','AHD','KNT','SNS','MON','WLD','BRT','PHD','NYB','HRN','HUB','CHEUNG','KLN','SKT','ARY','IEC','SYN']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:400] if v else 'MISSING')\n\"",
 "description": "Inspect refs_online.json keys"
}
```


### [2026-09-05T14:06:33.991Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushi
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG MISSING
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
```


## [2026-09-05T14:07:04.210Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/sources/refs/ && echo \"---MATRIX---\" && sed -n 1,200p data/verification/sources/SOURCE_MATRIX.md",
 "description": "List refs and read source matrix"
}
```


### [2026-09-05T14:07:04.256Z] TOOL RESULT

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
---MATRIX---
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


## [2026-09-05T14:07:08.712Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','SNS','SOD','FFD','FSF','BQT','BRT','PHD','AHD']:\n  print('==',k); print(json.dumps(d[k],ensure_ascii=False,indent=1))\n\" | head -150"
}
```


### [2026-09-05T14:07:10.232Z] TOOL RESULT

```
== POK
{
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
== KNT
{
 "title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953",
 "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/oldpers",
 "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt",
 "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.",
 "notes": "",
 "cites": "page number of Kent, Old Persian (1953); the lexicon starts p. 164"
}
== SNS
{
 "title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/VajnameShayest",
 "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"
 ],
 "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image",
 "covers_etymology": true,
 "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image."
}
== SOD
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
== FFD
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
== FSF
{
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
== BQT
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
Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
BrokenPipeError: [Errno 32] Broken pipe
```


## [2026-09-05T14:07:14.121Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: bheudh\" POK_full.txt\necho \"====\"\nawk '/Root \\/ lemma: bheudh-/{f=1} f{print} f&&/^----/{exit}' POK_full.txt | head -60"
}
```


## [2026-09-05T14:07:14.680Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: bheug\" POK_full.txt"
}
```


### [2026-09-05T14:07:16.364Z] TOOL RESULT

```
====
```


### [2026-09-05T14:07:16.411Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:07:18.649Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -40 POK_full.txt; echo ...; grep -n -i \"bheudh\" POK_full.txt | head -20"
}
```


### [2026-09-05T14:07:18.698Z] TOOL RESULT

```
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 
...
```


## [2026-09-05T14:07:22.069Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 158 159 160; do echo \"=== leaf $n (printed p.$((n-8))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt; done"
}
```


### [2026-09-05T14:07:23.619Z] TOOL RESULT

```
=== leaf 158 (printed p.150) ===
  Formen  von  es-  und  bheu-,  z.  B.  hat  die 1.  Sg.  Präs.  Konj.  air.  beu  (*bh-esö)  den  Anlaut  von  bheu-  bezogen;
air.  -biu  ,ich  pflege  zu  sein',  mcymr.  bydaf  corn.  bethaf  mbret.  bezaff ds.  {Hhuij,ö  =  lat.  fiö,  daneben  *bhui-  in  air.  blth,  mcymr.  bit  ,estö'  = lat./tO;
gall.  PN  Vindo-bios  {*-bhuiios),  vgl.  cymr.  gwyn-fyd  ,Glück'  (, weiße  Welt', byd),  air.  su-b{a)e  ,Freude'  {*su-bhuiio-\  du-b{a)e  (du  =  gr.  dvg-)  ,Trauer';
149
o-ot.  hauan  ^wohnen,  bewohnen'^  ald  bauan  ^ein  Leben  fübren'^  gabauan W'obnung'  aufscblagen^  {*hhöuö,  Vokalismus  wie  in  ai.  hhävayati,  bhäva-h, slav.  baviti),  aisl.  büa  (bjö,  büinn)  ^wobnen^  instand  bringen,  ausrüsten^, acrs.  büan  und  buic{i)an  (büde,  gebüen)  , wohnen,  bebauen^  (daneben  ags. löqian,  afries.  bögia  , wohnen^,  lautlicher  Typus  von  got.  stöja  aus  *stöioijö und  ö  als  ursprünglichen  Vokal  stützend),  abd.  büan  (büta^  gibüan)  ,wohnen, bebauen^;  nhd.  bauen]  aisl.  byggja  ,an  einem  Orte  wohnen,  bebauen,  be- völkern*, später  , erbauen,  bauen'  (aus  *buwwjan?  *bewwjan?)]  aisl.  bü  n. \A^ohnort,  Wirtschaft,  Haushalt',  ags.  bü  n.  ,Vi^ohnung'  (PI.  by  n.  vom i-St.  *büwi-  =  aisl.  byr  m.  ,  Wohnstätte,  Hof;  ähnlich  lit.  6üm5 , bleibender Aufenthalt*),  abd.  bü,  mhd.  bü.  Gen.  büwes  m.,  selten  n.  ,Bestellung des  Feldes,  Wohnung,  Gebäude',  nhd.  Bau-,
aisl.  büd  f.  ,Wohnung,  Zelt,  Hütte';  aschwed.  böp,  mnd.  böde,  mhd. biiode  und  büde  , Hütte,  Gezelt',  nhd.  Bicde  (%hö[u]-tä);  mnd.  bödel  ,Ver- mögen',  böl  , Landgut',  ags.  bold  und  botl  n.  ,Wohnung,  Haus',  *byldan, engl,  to  build  ,bauen',  afries.  bold  und  bödel  ,Haus,  Hausgerät,  Eigentum' (*böpla-  aus  idg.  *bhö[u]tlo-  und  *bupla-,  vgl.  lit.  büklä  und  westsl.  bydlo), ebenso  aisl.  böl  n.  ,Wohnstätte'  (s.  oben  auch  zu  böl  , Lager');
aisl.  bür  n.  , Vorratshaus,  Frauengemach',  ags.  bür  m.  , Hütte,  Zimmer', abd.  bür  m.  ,Haus,  Käfig',  nhd.  (Vogel-) Bauer,  wovon  ahd.  nähgibür,  ags. neahgebür,  nhd.  Nachbar,  engl,  neighbour  und  ahd.  gibür{o),  mhd.  gebür(e)f dann  bür,  nhd.  Bauer  ,rusticus';
ags.  beo  ,ich  bin'  (*bhunö  =  lat.  /lö,  air.  -6m),  daneben  beom,  ahd. 6im  usw.  nach  *m  von  *es-  ,sein',  wie  ahd.  bis(t),  ags.  6i5  nach  is.
Vielleicht  got.  bagms,  ahd.  böum,  ags.  6eam  ,Baum'  aus  *bhou{d)mo' ,(pvt6v'  und  aisl.  bygg  n.  ,Gerste',  as.  Gen.  Fl.  bewö  ,Saat,  Ertrag',  ags. beoic  n.  , Gerste'  (*6ei(;u;a-)  als  , Angebautes'.
Lit.  buti  (lett.  öw^,  apr.  boüt)  ,sein',  bidu  Supin.  ,zu  sein'  (apr.  büton Inf.),  Partiz.  bütas  , gewesen',  Fut.  büsiu  (lett.  büsu),  Frät.  büvo  ,er  war' (vgl.  auch  buvö-ju,  -ti  ,zu  sein  pflegen'  und  aksl.  Iter.  byvati),  Opt.  apr. bousai  ,er  sei',  Prät.  bei,  be  ,ev  war*  (von  einer  mit  -ei-  erweiterten  Basis);
lit.  büvis  m.  ,Sein,  Leben',  buvinUi  ,hie  und  da  ein  Weilchen  bleiben', apr.  buwinait  , wohnet!';
lett.  büsana  ,Sein,  Wesen,  Zusta
=== leaf 159 (printed p.151) ===
nd',  apr.  bousennis  , Stand';  lit.  bixtas, apr.  (Akk.)  buttan  ,Haus';
lit.  büklas  (*bütla-)  ,cubile,  latebrae  ferarum',  pabuklas  ,Instrument, Gerät;  Erscheinung,  Gespenst',  büklä,  bükle  ,praesentia,  Wohnung',  ostlit. bükle  ds.  (s.  oben;  dazu  buklüs  ,weise,  schlau');
aksl.  byti  , werden,  sein',  lo-  Partiz.  byh  , gewesen'  (davon  byhje  , Kraut; Heilkraut',  vgl.  zur  Bed.  cpvTÖv),  Aor.  be  ,war'  (*bhue-t)]  Imperf.  b^ase, Fut.  Partiz.  ksl.  by§esteje,  by§qsteje  ,Td  fxsllov,  Kondiz.  3.  PL  bg  (*bhuä-nt),
150  •
Partiz.  za-Hvem  ^vergessen',  neben  sonstigem  Partiz.  *byt  z.  B.  in  russ. zahytyj  , vergessen^,  vgl.  dazu  auch  Subst.  russ.  byt^  ^Wesen,  Lebensart' u.  dgl.^  apoln.  byto  ^Nahrung^,  aksl.  ^z-byt^k^  ^Überfluß,  Rest^  u.  dgl,  bythj^ ,das  Dasein^;
aksl.  zabyth  ^Vergessen',  pobyth  ,^ieg',  pi-ebyth  , Aufenthalt^;  russ.  hyt^ ,Wesen;  Geschöpf;  Tatbestand^;
Präs.  aksl.  bgdg  ^werde,  ylyvo^ai^  als  Fut. :  , werde  sein^  (ob  zu  lat.  Adj. auf  -bundus?)',  Kaus.  aksl.  izbaviti  , befreien^  erlösen'  n.  dgl.  (:  ai.  bhäva- yati,  vgl.  zum  Vokalismus  auch  got.  bauan  und  aksl.  zabava  ^Vervreilen Beschäftigung,  Zeitvertreib');  cech.  bydlo  , Aufenthaltsort,  Wohnung',  poln^ bydh  ,Vieh'  (aus  *,Stand,  Wohlstand,  Habe').
Vielleicht  hierher  (Pedersen  Toch.  228^)  tocb.  B  pyautk-^  A  pyotk- AB  pyutk-  ,zustande  kommen',  med.  ,zustande  bringen'.
Von  der  Basis  bh(e)ui-:
npers.  Imp.  bl-d  ,seid!';  apers.  Opt.  bi-yä^  setzt  Wackernagel  KZ.  46, 270  ==  ai.  bhü-yä-h,  -t-
gr.  (ptzv  n.  ,Keim,  Sproß'  =  q)iTv^La,  (pijvo)  , erzeuge,  säe,  pflanze';
lit.  alt.  bit(i)  ,er  war',  auch  Kondit.  1.  PI.  {süktum-)  bimej  lett.  biju.^ bij ß  jichj  er  war'  (lett.  bijä-  erweitert  aus  athemat.  *bhul-);  ablaut.  aprj bei,  s.  oben;
aksL.  Kondit.  2.  3.  Sg.  bi  , wärst,  wäre'  (*bhul-s,  *bhui-t),  m'ozu  sekundär 1.  Sg.  bi-mh  mit  Primärendung.
WP.  II  140f.,  WH.  I  375 f.,  504f.,  557  f.,  865,  867,  EM.  812f.,  1004f., Trautmann  40  f..  Feist  83  f.
Specht  will  (KZ.  59,  58  f.)  unter  Heranziehung  von  gr.  (paJ^og  , Licht, Heil'  =  ai.  bhava-  , Segen,  Heil',  cpaa-al-ußQOTog  usw.  unsere  Wz.  als *bhaud-^  nicht  als  *bheud-  ansetzen.    S.  auch  oben  S.  91.
bheudh-,    nasal,    bhu-n-dh-    ,wach    sein,    wecken,    beobachten;    geweckt, geistig   rege,   aufmerksam   sein,  erkennen,   oder  andere   dazu    veran- lassen (aufpassen  machen,  kundtun,  gebieten;  darbieten)'. Themat.  Präs.  in  ai.  bödhati,  bödhate  , erwacht,  erweckt,  ist  wach,  merkt, w
=== leaf 160 (printed p.152) ===
ird    gewahr',    av.    baodaiti    ,nimmt   wahr',    mit  paiti-  ,sein   Augenmerk worauf  richten'  (=  gr.  7tsvd^o(.iaij  germ.  *biudan,    abg.    bljudg);    Aor.    ai. bhuddnta  (=  invd-ovTo),  Perf.  bubödlia,  bubndhimd  (:  germ.  *baud,  *budurn), Partiz.  buddhd-  , er  wacht,  verständig;  erkannt'  (=  gr.  ä-nvarog  ,unkundig; unbekannt'),    buddhi-    f.    , Einsicht,  Verstand,    Meinung,    Absicht'    (=  av. paiti-busti-    f.    ,das    Bemerken',    gr.  nvotig    ,das    Nachforschen,    Fragen; Kunde,  Nachricht');  Kausativ  in  ai.  5öc^M7/a<i  , er  weckt;  belehrt,  teilt  mit', av.    baodayeiti   ,bemerkt,    fühlt'  (=  abg.    buzdg,    buditi,   lit.  pasibaudyti)] Zustandsverb  in  ai.  budhydte  ,erwacht,  wird  gewahr;  erkennt',  av.  buiöyeiti
■m
151
TV-ird  gewahr^;  frabuidyamnö  ^erwachend';  ai.  boddhdr-  m.  ^Kenner'  (:  gr. ^sv(ri^rjQ--^og  ,frag-eiid');  av.  baoöah-  n.  , Wahrnehmung,  Wahrnehmungs- vermögen^, Adj.  , wahrnehmend^  (:  hom.  d-nev^rjq  ^unerforscht,  unbekannt; unkundig^);  av.  zaeni-hudra-  , eifrig  wachend^  («abg.  Hd-n,  lit.  hudriXs)] av.  haoiöi-  , Wohlgeruch'  (=  ai.  hödlii-  ^vollkommene  Erkenntnis');
crr.  7tsvdo{.iai  und  Ttvvd-dvoi-iai  (:  lit.  hundü,  air.  ad-hond-)  , erfahre, nehme  wahr,  wache'  (rtevaofiaij  iTtvO^öf-iriV^  neTtva^iai),  nevO-d)  , Kunde, j^achricht';   nvarigy  Ttevcng  f.  , Frage';
cymr.    bodd   (*bhudha)   , freier  Wille,    Zustimmung',   corn.    both  , Wille'
(:  aisl.  bod)j  air.  buide  , Zufriedenheit,   Dank-;   hierher  auch  air.   ad-bond-
ansagen,    verkündigen',   uss-bond-    , absagen,    verweigern'    (z.  B.  Verbaln.
ohbad)]    hochstufig   air.   robud   , Verwarnung',    cjmr.    rhybudd  ,Warnung',
rhybuddio  , warnen'  (:  russ.  probudüh  ,auf wecken');
got.  anabiudan  , befehlen,  anordnen',  faurbiudan  , verbieten',  aisl.  bjöda , bieten,  anbieten,  zu  erkennen  geben',  ags.  beodauj  as.  biodan^  ahd.  biotan , bieten,  darbieten',  nhd.  bieten,  gebieterij  verbieten,  Gebiet,  eigentl.  , Befehls- bereich'; aisl.  bod  n.,  ags.  gebod  n.,  mhd.  bot  n.  , Gebot',  ahd.  usw.  boto ,Bote',  ahd.  butil  (nhd.  Büttel),  ags.  bydel  ,Bote, .  Gerichtsdiener';  got. biups,  -dis  jTisch',  aisl.  bjödr,  ags.  beod,  ahd.  beot,  piot  ,Tisch;  Schüssel', eig.  , worauf  angeboten  wird,  Servierbrett'  (dazu  auch  ahd.  biutta,  nhd. Beute  , Backtrog,  Bienenkorb').
Mit  ü  (vgl.  Hirt  Idg.  Gr.  II  96):  got.  anabüsns  f.  , Gebot'  (^-bhudh-sni-), as.  ambüsan  f.  ds.,  ags.  bysen  f.  , Beispiel,  Vorbild',  aisl.  bysn  n.  ,Wunder' (aus  ,* Warnung'),  bysna  ,vorbedeuten,  warnen';
lit.  bundü,  bilsti  , erwachen'  und  (ohne  Nasalinfix)  budil,  budeti ,wachen',  büdinu,  -inti  , wecken',  budrüs  ,wachsam';  Kausativ  baudziü, baüsti  ,stra
```


## [2026-09-05T14:07:34.230Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 161 162; do echo \"=== leaf $n (printed p.$((n-8))) ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' POK_01.txt; done"
}
```


### [2026-09-05T14:07:35.950Z] TOOL RESULT

```
=== leaf 161 (printed p.153) ===
fen,  züchtigen';  refl.  ,beabsichtigen'  {*bhoudh-iö),  baudziava , Scharwerk,  Frondienst',  lit.  bauslys  , Befehl',  lett.  bauslis  , Gebot',  lett. bauma,  bäume  , Gerücht,  Nachrede'  (*bJioudh-m-'),  lit.  pasibaudyti  ,sich erheben,  aufbrechen',  baudinti  , aufmuntern,  Lust  zu  etwas  erwecken', apr.  etbaudints  ,auferweckt'.
Themat.  Präs.  in  abg.  bljudq,  bljusti  , wahren,  hüten,  achtgeben',  russ. bljudü,  bljusti  ,beobachten,  wahrnehmen'  (über  slav.  -ßi  aus  idg.  eu  s. Meillet  Slave  commun^  58).
Kausativ  in  abg.  buzdq,  buditi  _, wecken',  russ.  buzü,  budith  ds.  (usw.; auch  in  russ.  büdenb  , Werktag',  wohl  eig.  , Wecktag'  oder  ,Tag  für  Fron- dienst'); Zustandsverb  mit  e-Suffix  in  shg.  b^^dg,bld^ti  ,wacheu',  perfektiv (mit  ne-/no-Suffix  wie  in  gr.  Ttvvd'-dvo-f.iaL,  wo  -ovo-  aus  -nno-,  Schwyzer  Gr. Gr.  I  700)  v^z-b^ng  , erwache'  (*bhud-no-,  aus  einem  Aor.  des  Typus  gr. invd'STO  gebildet,  usw.,  s.  Berneker  106  f.,  auch  über  skr.  bädnjl  dän ,Christabend',    bädnjäk    ,  Holzscheit,    das    man    am    Weihnachtsabend   ins
152
Feuer    legt'    usw.),    abg.   s^-na-b^deti    jCpvhxTXSiv^  \    abg.   hidirb    jrcQÖd'v^Q^ willig,  bereit',  bzzdrh  ds.,  russ.  bödryj  ,munter,   stark,   frisch',    skr.  hädc ^lebhaft'.
Toch.  B  paut-^  A  pot  ,ehren'?  (Van  Windekens  Lexique  87).
WP.  II  147 f.,  Feist  41,  97,  Meillet  Slave  commun*  202 f.
1.  bheug-  ,fliehen',  nach  Kretschmer  (Gl.  30,  138)  zu  2.  hheug(hy  (av.  baol
in  der  intransitiven  Bedeutung  ,sich  retten').
Gr.  cpsvycj  (Aor.  Ecpvyov,  Perf.  nscpevya)  ,fliehe',  (pvyri   f.   (=  lat.  fug^ ,Flucht',  hom.  cpv^a  (*q)vyta)  ds.,  Akk.  cpvya-de  ,in  die  Flucht'  vom  Koi Stamm  ^(pvy-\
vielleicht  im  ven.  ON  OsvyaQOv  (Westdeutschi.)  ,Fluchtburg' ;
lat.  fugiö,  fügt,  -ere  ,fliehe,  enteile,  verschmähe',  fuga  f.  ,Flucht';
lit.   bügstu,    bügau,    bügti   intr.   , erschrecken',   kaus.    bauginti  ,jemd. schrecken',  baugüs  ,furchtsam'.
WP.  II  144,  146,  WH.  I  556  f.,  Kretschmer  Gl.  30,  138.
2.  bbeug-,  hheugh-  ,wegtun,  reinigen,  befreien';  intrans.  ,sich  retten'.
Av.  baog-,  bunja-  ,lösen,  retten,  sich  retten  vor'  {bunjainti  ,sie  befreien! retten',  büjayamnö  ,ablegend',  bunjayät  ,er  rette'),  büjim  Akk.  ,Reinigung'j qzö-buj-  ,aus  Not  befreiend',  baoxtar-  ,Befreier';  pehl.  paz.  böxtan  ,retteii, erlösen',  südbal.  böjag  ,öffnen,  lösen,  losbinden',  als  pers.  Lw.  arm.  huzem ,heile,  rette,  befreie',  boi^  , Heilung,  Befreiung';  päli  paribhuüjati  ,reinigT, kehrt  aus';  aber  päli  bhujissa
=== leaf 162 (printed p.154) ===
-  ,freigelassen  (von  früheren  Sklaven)'  = ai.  bhujisyä-  ,frei,  unabhängig'  (Lex.,  in  der  Lit.  als  ,nutzbar',  Subst. ,Diener(in)'),  zu  4.  bheug-.
Illyr.  PN  Buctor,  ven.  Fuctor  (  :  av.  baoxtar-),  Fugonia,  vliw/^ia,  vhou- ynontios,  usw.
Got.  usbaugjan  ,ausfegen,  auskehren',  nhd.  dial.  Bocht  ,Kehricht,  Mist'; hierzu  wohl  auch  mhd.  biuchen  ,in  Lauge  kochen',  ursprgl.  , reinigen', buche  f.  ,Lauge'  (mit  sekund.  Ablaut).
Die  Doppelheit  germ.  gh  :  ar.  g-  auch  bei  bheugh-  (nhd.  biegen) :  bheug-  (ai. bhujati  usw.)  ,biegen'.     Wohl  identisch  damit.
WP.  II  145,  WH.  I  560,  Kretschmer  GL  30,  138.
3.  bheug-,  hheugh-  ,biegen'.
Ai.  bhujati  ,biegt,  schiebt  weg',  bhugnd-h  ,gebogen',  bhüja-h  ,Arm',  bhujä ,Windung,  Arm',  bhögd-h  ,Windung  einer  Schlange;  Ring'  (:  ahd.  boug)] nis-bhuj-  ,schieben',  Pass.  ,sich  drücken,  entwischen';
vielleicht  hierher  alb.  bute  ,weich'  aus  *bhug{h)-to-  ,biegsam';
ir.  fid-bocc  ,hölzerner  Bogen',  wohl  auch  bocc  ,tener'  (,*biegsam'),  nir. bog  ,weich'   (aus  *buggo-),  KZ.  33,  77,  Fick  11^;    für   abret.  buc  ,putris',
153
]    bocion  ,putresS  nbret.  amsir  poug  ,temps  mou^^  die  brit.  -ch-  =  ir.  -gg-
*  irten  ließen^  erwägt  Pedersen  KG,  I  161  Entlehnung  aus  dem  Ir.
Tu  Germ.  *bheiigk-:  got.  hiugan,  ahd.  hiogan  ^biegen^,  aisl.  Partiz.  hoginn
-»lo<^en^*  ablaut.  ags.  bügan  ,sich  biegen^,,  mit /ram  ,fliehen^;  Kaus.  aisl.
hfvaia    as.  bögian,  ags.  biegan,  ahd.  bougen,   nhd.   beugen]   aisl.   biügi^  ,ge-
Vio'^en^    ahd.  biugo  .sinus^;  aisl.  bogi,  ags.  boga  (engl,  boiv),  ahd.  hogo,  nhd.
Hoaen  (ahd.  swibogo  ^Schwibbogen^  aus  *swi[bi-]bogo)]  vielleicht  dazu  got.
k,fnjan  ;kaufen^^  aisl.  byggia  ,eine  Frau  kaufen^^  ags.  bycgan,  as.  buggian
kaufen^  (vgl.   nhd.   dial.  ^sich    etwas    beibiegen-  =  ^erwerben,   nehmen^);
dazu  wohl  lett.  bauga  und  baügurs  ^Hügel^
Intensivum  (mit  Verschärfung)  germ.  *bukjan  im  mhd.  bücken,  Schweiz. hukche-   mnd.  bücken,  afries.  buckia  _,sich  bücken^   (Wissmann  Nom.  post- verb.  171,  181); WP.  II  145  f.,  WH.  I  556,  Feist  96. ^.  bbeug-  .genießend
Ai.  bhuiiktB  (mit  Instr._,  jünger  Akk.)  ^genießt^/ vgl.  bhundktiybhuftjati o-owährt  Genuß,  genießt,  verzehrt^,  bubhuksä  ,Hunger^,  bhöga-h  ,Genuß^; über  ai.  bhujisyä-  s.  oben  unter  2.  blieug-]
alb.  bunge  L,  bunk,  bungu  m.  ,(Speise)eiche^  (als  ,Nährbaum^,  Postverbale =  ,Kostgewährer^);
lat.  fungor  ^verrichte,  werde  fertig  mit^,  mit  Akk.,
```


## [2026-09-05T14:08:01.469Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT baoi.di ===\"; grep -n -i \"baoi.i\\b\\|baoiSi\\|baoidi\\|baoiöi\" BRT.txt | head -20\necho \"=== BRT baoxtar ===\"; grep -n -i \"baoxtar\\|baoxtar-\" BRT.txt | head -10\necho \"=== BRT bunja ===\"; grep -n -i \"bunjainti\\|bunjai\\|buj im\\|baog\" BRT.txt | head -20"
}
```


### [2026-09-05T14:08:01.553Z] TOOL RESULT

```
=== BRT baoi.di ===
13352:•  j.  däityö.baoi3i.-bav-  kompV.  'der  ge- hörigen Räuchermittel  teilhaftig  werden': °buyS  ..  äiars  pui:ra  ahurahe  Y.  6'2.  2.
17060:ai.  bhäti;  bhani:  —  Vgl.  »Et  Bno.  KZ.  ig. 499,  Gdn.  3Yt.  70.  —  S.  auch  vyävant-,  vohvä' lant:  —  n  V  statt  w,  %  368.  37. j.  bäuidri  V.  15,  49 :  lies  baoiAi.
30310:bestgehütctc':    ava  zJ  *xsdkrisu  'mä  ^-i' •  j.  hubaoi8i'ta-t 'Wohlriechendheit,  lieb-
=== BRT baoxtar ===
16553:•  j.  baoxtar-  m. 'Retter,  Befreier':  nairyqm Äam.vamllm  . .  yä  narqm  vJg>r)ptä{^^nt tanvS  °tänm  äa}>aili  Vr.  7.  3.
=== BRT bunja ===
15079:Yt.4. 3  "■      2)Praev,  (nur  mit  baog-).
16205:•  j,  p3^.8ära-  Adj.  'des  Haupt  verwirkt, dem  Gericht  verfallen  ist,  tockündig':  ys mqm  .  .  därayehi  ya^a  tayam  -nm  nava (sd.)  akmi  'rS  Y,  /;.  3;  —  väcö  ysi  p^simHt sär?m  "  bunjainii  ". .  die  selbst  den  noch retten,  des  Haupt  schon  dem  Gericht  ver- fallen isr  Yt./4.46.
16272:Zum  V.  baog-^).  —  Vgl.  *ä%i}'Sbaustia:  — Pü. :  /iff-  bSUsn,  erl. :  i^äslai  kt  nraiakih  vas hol  ai.  —  ')  Verbindung  von  DS.  und  GS. wie  öfters.  —  ")  Es  liegt  nahe,  vielmehr  an ai.  ikuttäkH  lu  denken  und  da.E  Adj.  'reich an  GenQssen'  zu  deuten,  wenn  nur  auch  sonst im  Iran,  eine  solche  Bedeutnng  für  b'  zu  er- weisen wäre;  vgl   Hhm.  IFAnz.  6.  34.
16501:baog-
16540:—  InC  *baisazyäi.  •  j.  baog-  V.  'lösen'.     Praes.  3  bBja-",
16544:baog-
16545:i)  '(den  Gürtel)  lösen  sva.  ablegen': yasca  . .  aiwyänhantvt  vä  aiwyäahayamnö aiwyatfhatum  vd  ds/ayamn^  "..deaGüi- telan-  oder.. ablegend"  Yt  7,17.  a)'be- freien,  retten':  vä^ yäi ^^S^mat(Sp.Bg8  o.) särvm  bunjainti  Yt.  7^46;  —  masyS  an- ÄJM  (sd.)  yat  u^tänim  bunjayäi  ", .  dass  sie ihre  Lebenskraft  rette"  V,  7. 7 1 .  a)  Vor  — ' (haca  mit  Akk. !):  tä  büjat  . .  narsm  haca nasüm  Yt  4.  3.  a)  'sich  retten  vor  — '
16643:Eig.  'von  Gott  befreit,  erlöst';  'buxsa-  m.,  znm V.  baog-i  vgl.  Yt.  14.  46.
```


## [2026-09-05T14:08:02.089Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT bagabuxsa ===\"; grep -n -i \"buxša\\|buxsa\\|Bagabux\" KNT.txt | head -20\necho \"=== KNT baug ===\"; grep -n -i \"^baug\\|baug-\" KNT.txt | head -10"
}
```


### [2026-09-05T14:08:02.152Z] TOOL RESULT

```
=== KNT bagabuxsa ===
1297:(with nasal infix); with added -s-, -buxSa- in
1903:Baga-buxSa- ‘Freed by God’; Bagabigna- perhaps ‘Begotten by God’.
3876:83 à : Vidafarnà : пато : V&yaspárahy& : puça : Parsa : Utàna : пата : Guxrahyá 84 : риса : Parsa : Gaubaruva : паша : Marduniyahyá : puça : Parsa : Vidarna : nama : Ва 85 gabignahya : puça : Parsa : Bagabux’a : пата : Dütuvahyahyà : риса : Pársa :
4859:Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
4861:Utana-Otanes; but he gives (7.82) Mardonius, the general in the third invasion of Greece, as son of Gobryas, which indicates agreement as to the name of Gobryas’s father. But Megabyzus son of Zopyrus (7.82) may or may not be the Behistan Bagabuxía son of Datuvahya, or his grandson. Herodotus does, in fact, mention all six of the helpers of Darius in passages outside 3.68-88, in passages which may be found in any Index Nomi- num Propriorum to the text of Herodotus.
5714:. baug- vb. ‘free’: Av. baog-, NPers. boxtén; in Attydbausna-, Bagabuxsa-.
5717:baga- sb. ‘god’: Av. baga- ‘lot, good fortune’, Skt. bhdga- ‘dispenser (of good fortune)’, Gk. -paryos ‘eater’, OCS bogi ‘god’, pIE *bhago- ($101, $122, 5143.1, V, VI); ef. Hz. ApI 105-10. See also Bagábigna-, Bagabuxsa-, Bagayddi-, bà. рада nsm. AmH 6; AsH 6; DNa 1; DNb 1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
5719:Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
=== KNT baug ===
1298:Baga-burSu- (see Lex.); *baug-s-na-, becoming
2644:baug- ‘free’, seen in Av. pouru-baorsna-; in OP
4956:Aéiydbausna- sb. ‘Athiyabaushna’, father of Arsaces ($168.11): cpd. of (Av.) ai- ‘destruction, misfortune’ + pass. pte. of d-baug- ‘to free’ ($248) with late -šn- from -aén- (Bv. BSLP 29.2.104, cf. Av. pouru-baozóna- ‘bringing abundant rescue, Bthl. AiW 901): ‘Freed from misfortune’ ($160.14; not active ‘bringing freedom from misfortune’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
5714:. baug- vb. ‘free’: Av. baog-, NPers. boxtén; in Attydbausna-, Bagabuxsa-.
5719:Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
```


## [2026-09-05T14:08:09.110Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [5714,5719,4956]:\n    pre='\\n'.join(lines[:target])\n    leaf=pre.count('\\f')\n    print(target,'leaf',leaf,'-> printed',leaf-15)\nEOF"
}
```


### [2026-09-05T14:08:10.665Z] TOOL RESULT

```
5714 leaf 222 -> printed 207
5719 leaf 223 -> printed 208
4956 leaf 188 -> printed 173
```


## [2026-09-05T14:08:12.035Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD bxt/boxtan ===\"; grep -n -i \"bōxtan\\|boxtan\\|bwhtn\\|bōz\\b\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD payos/pyws ===\"; grep -n -i \"payōs\\|payos\\|pyws\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD boy ===\"; grep -n -i \"bōy\\|bōd\\b\\|bōyistan\\|bōstān\\|bōy-\" PHD.txt | head -20"
}
```


### [2026-09-05T14:08:12.106Z] TOOL RESULT

```
=== PHD bxt/boxtan ===
PHD.txt:264:bóxtan, bóz- [bwhtn', bwc- | M bwxtn, bwz-] save, redeem. —išn [-# | J bwzyfn[t, N pdzis] salvation; apology.
PHD_mackenzie.txt:1593:boxtan, boz- [bwhtn', bwc- I M bwxtn, bwz-] save, redeem .
PHD_mackenzie.txt:1607:boz- .......isn. v. boxtan.
PHD_mackenzie.txt:7398:quality (accidental) Jadisn.                   redeem boxtan, wiziirdan.
PHD_mackenzie.txt:7488:rotten pudag; v. corrupt.                  save boxtan.
=== PHD payos/pyws ===
PHD.txt:323:2ēraxtan, ёгапј- Pylhtn', *ylnc- | M ‘yrxt, ( yrnz-)] fight, dispute. éraxtür [y/At? 1] warrior. ēr-kaš ['dik£ | M *yrkš] (hands under the armpits in respectful) salutation, greeting. 1ërmán [?y/mx! | (MÉÁry! mwn), N ~] friend; а god. — ih: friendship. 23ër-man(ag) ['dim?n(k)'] humble. ēr-menišnīh [dimyninyh] humility. ér-tan ['ditn!'] humble. ~ih: humility. ērwār [D yleo?1] befitting a hero. ērwāraģ [*dlw?Ik! | J ?rw’rh] jaw, cheek. ésm ['ysm] = ézm. esp", v. sp”. éstádan, ést- [YKOYMWN-tn! < A ygym, У gum; ?sttn!, *zost- tn! | M ‘yst-’dn, N ~] stand; be, continue (as auxiliary of the perfect con- tinuous tense). ~išn: permanence, lasting, dwelling. ēš Pys | N xéf] plough. efm, v. $n. &(w) [z; HD < A hd | M ‘yw, N -ēļ a, one. éwan [*dwn') stalk, trunk. ēwān ['dw?n!] bridle. éwar ру! | J ?yf?r] certain(ly), assured(ly). éwarz [dwlc] movement. éwarzidan, éwarz- ['dwlc-ytn!] move, travel. éwarzig ['dwlcyk!] moving. 1&wáüz [?уш?с] word, utterance. tēwāz [?уш?с] sole, only. ~ig [-yk'] particular, individual. čw-bār Duech?) once. ē(w)-čand D у(то)спа] some, a few. éwén Pdwyn' | M *ywyn, (N àyin)] manner, custom, form, propriety. pad —: properly. léwénag ['dwynk! | M *ywyng] = ëwën ; v. ёё-. Ў *éwénag [?*dwynk! | (N āyīna)] mirror. Set (ъд) yn k éw-kard(ag) ['ywkrt(k)', -kltk'] united, joined. ē(w)-mēg D»(zo)mtok!] wearing (only) one shoe. éw-sün Pywsn' | (N yak-sān)] uniform, (a)like. ^ Ah : uniformity, likeness. éw-tüg Pywt?k' | М ‘yw 12, (N yaktà)] alone, single, individual. éz-, v. yaz-. —išn [уст] worship. ézm [CY BA < A syb | N hëzum] firewood, fuel. ged Zm4
PHD.txt:547:~th: visibility, appearance. paydagénidan, paydagén- [ ГОР hinin | M pyd'gynyd] reveal, explain. paydagihistan, paydagih- [py kyh-stn'] appear, be revealed, payg [pdh! | (P рар), N ~] foot-soldier, courier. *paygal [pyg'l | N payyāla, piyála] cup, goblet. -- gar [-A/] cup-maker. payģām [pgt”m! | M pyg’m, N pay(y)ām] message. ~bar LA | N -bar] messenger, apostle. paygos [p?tktvs | M p’ygws] district, province. paymān [pim”n! | M pym?n, N ~] measure, period; moderation; treaty. 6 — madan: reach maturity. ~ag [-k! | N ~a] period, measure, proportion. paymānīģ [ptm”nyk!] moderate. ~ih: moderation. *paymar [PK DWN < А pqdwn; p'tym'l] appointment, assignment. paymāy-, v. paymüdan. paymēģ [ptmwg | M pymwg] clothes, garment. paymóxtan, paymēz- [ptmwhtn!, ptmwe- | M pymwxt, bymwc-] don, wear. paymēūzan [ptmwen' | M pymwen] garment, dress. paymüdan, paymāy- [ptmwtn', ptm’d- | N ~] measure. *payram [p’tlm] the commonalty,-people. payrāstan, payrāy- [pt-, pyPstn!, pyPd- | M ругі, pyr!y-, N pērāstan) arrange, adorn. payrayag [руРак! | M pyr)yg, N pērāya] ornament, adornment. payrēģ [ptlwk'] light, brightness. paywand [ptwnd | (M руп), N ~] connection; offspring. paywand-, v. paywastan. paywasag [ptw’sk'] leather bag, wallet. paywastag [pteostk! | N ~a] continually. paywastan, paywand- [ptwstn!, ptwnd- М pywst, (pywyn-), N ~] join, connect. paywāz- [ptw’c- | M pyw’z-] answer, reply. ~ag [-k!], —i$n: response. paz-, v. poxtan. pāzand [p’cnd | N —] the Pahlavi commentaries on the scriptures (zand), transcribed in Avestan letters. pazd [pzd | — P] oppression, persecution. pazd- [pzd- | = M] blow, play (flute). pazdaģīh [pzdkyh] expulsion. pazdénidan, pazdén- [pzdyn-ytn' | P pzd-] frighten, chase. pāzen [p’c(y)n' | М pen, N pazan] ibex. pazüg [pzwk! | (N payūk, xabazdū)] guinea-worm. ~ í gühgard / gGhward: dung worm. pazzāftan [p> tn ' (M pzpt „intr.)] (cause to) ripen.
PHD_mackenzie.txt:4171: paywastan, paywand- [ptwstn l , ptwnd- M pywst, (pywyn-), N ......]
=== PHD boy ===
```


## [2026-09-05T14:08:20.314Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- PHD boy ---\"; grep -n \"bōy\\|boy \\[\\|bwd |\\|bōd\" PHD.txt | head; echo; grep -n \"b[oō]y\" PHD_mackenzie.txt | head -20\necho \"--- PHD bōstān / bōy ---\"; grep -n \"bōstān\\|bostan\\|bwst\" PHD.txt PHD_mackenzie.txt | head"
}
```


### [2026-09-05T14:08:20.393Z] TOOL RESULT

```
--- PHD boy ---
166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
267:?"bóy [bwd | M bwy, N ~] smell, scent.
605:wad-baxt [wtP ht! | N badbaxt] unfortunate. wad-dil [wtdyl | M wddyl, N baddil] coward(ly). wadgarih [wtglyh] evil-doing. wād-ģirdaģ [w° tgltk' | (N gird-bād)] whirlwind. wad-góhr [wtgwhl | N bad-gauhar] ill-, low-born. wad-kamag [wtk’mk'] malevolent. ~ih: malevolence. wadrang [w’ ting | N bādrang] citron. cc Dë [-bwd | N -bóya] lemon balm. wad|-tóhm [wttwhm] = wad-góhr. ~-wazag [-w’ck! | (N gawāža)] abuse. --.Xém [-hym] ill-natured. waf- [wp- | Р wf-, (N bàf-)] weave. ~išn: weaving. wafr [wp! | M wpr, N barf] snow. ~énag [-ynk!] а sweetmeat. waydān [wy?n! = Av. waybana-] head (ahuric). wahāg [wP?k! | M тор, N baha] trading; value. — burdan: value, estimate. wahār [wh], (bj?l) | M wkr, № bahar] spring. ~ig [-уЁ! | N -z] spring, vernal. wahig [ZZLA < A Semi (?); whyk' | M whyg, N *bahi] kid; astr. Capricorn. wahist [ол | M whyst, N bihist] paradise. ~Ig [-yk! | N -1] (worthy) of paradise. Wahman [whwmn' | M whmn, N bahman] Good Mind, the first Amahra- spand, guardian of cattle; cal. 11th month; 2nd day. wāhmān [*w-n! = whmn' | MOw^hmn, J whmn, N bahman] so-and-so. Wahrām [wlhl?’n', whPm | M whr’m, N bahram] god of war, victory; astr. Mars; cal. zoth day. ātaxš 1~: a major sacred fire. wak [wk! | N bak] frog. wālan [zo n! | (IN barzan)] settlement, community walg [wlg] = warg. walidan, wāl- [w]-ytn! | N bdlidan] grow, increase, prosper. ~išn: growth. wümidan, wam- [w’m-yin'] vomit. wan [wn' | N bun] tree; stock, stem. ~ i $urgünig : pistachio tree. ~ 1 was-téhmag: the Tree of Many Seeds. wān-, ~išn, v. wanidan. wanafšag [zvnpšk! | N bunafša) violet. Wanand [wnnd] astr. Vega. wandaģ [wndk'] rope, cord. wang [KALA < А ql’; wng | = M, N bang] voice, cry. wānīdan, wan- [wn-ytn! | M w’n-yst] conquer, overcome, destroy.

523:        2boy         add incense.
758: -- boy [-bwd] senseless.
759: -- boyih: senselessness.
1597:Iboy [bwd] perception, sense.
1598:2boy [bwd I M bwy, N ......] smell, scent.
1599:boyag [bwd)k I M bwy)g, N boya] scented.
1601:boy-dar [bwdd)ll N ......] scented.
1602:boyenidan. boyen- [bwdyn-ytn ] scent, perfume.
1604:boyestiin [bwdst'n l I M bwyst)n, N bostan] (flower) garden .
1606:boyidan. boy- [bwd-ytn' IN ......] smell (intr.).
2714:hamb6y- [hnbwd- I M hwmbwy-, N anboy-idan] smell (tr.) .
2929:hu-boy [hwbwd] sweet-smelling, fragrant.
5130: ......-boy [-bwd I N -boya] lemon balm.
6106:boy, v. lad, page, son.                builder raz-kirrog.
6615:following (household) gal.                   fragrance huboyih.
6616:folly halagih.                               fragrant huboy.
6661:fountain siidurwan.                          garden bay; (flower)""'" boyestiin.
6662:four cahar.                                  gardener boyestiinbiin.
6952:lamentation briimag, cehisn, gilag,       lemon balm wiidrangboy.
7229:page (boy) redak, rahig.               peg mex.
--- PHD bōstān / bōy ---
PHD_mackenzie.txt:1604:boyestiin [bwdst'n l I M bwyst)n, N bostan] (flower) garden .
```


## [2026-09-05T14:08:22.053Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- NYB glossary ---\"; grep -n \"bōxtan\\|bōzišn\\|bōy\\b\\|bōd\\b\" NYB_vol2_glossary.txt | head -20\necho \"--- HRN boy ---\"; grep -n -i \"bōi\\|bōj\\|boi ,\\|Wohlgeruch\" HRN.txt | head -20"
}
```


### [2026-09-05T14:08:22.116Z] TOOL RESULT

```
--- NYB glossary ---
--- HRN boy ---
2446:aw. baoiöi- *Wohlgeruch' ; phlv. böd, böi, böylnUan;
```


## [2026-09-05T14:08:30.536Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2435,2465p' HRN.txt\necho \"=== leaf/page ===\"\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [2446]:\n    print(target,'leaf',('\\n'.join(lines[:target])).count('\\f'))\nEOF"
}
```


### [2026-09-05T14:08:32.155Z] TOOL RESULT

```
237. {\)büfn 'Erde, Land'.
ap. btimi' *Erde'; aw. büml-j phlv. büm C^LJjMmi^
238. {2)hum, baf'^) *Eule\ n^\
arm. btt, biiec 'Eule' (H. No. 59); lat. bübö; gr. ßvac^
ßvCa,
Onomatopoetisch, sonst würden die Lautverhältnisse
nicht stimmen.
239. bTimehen 'Erdbeben {^bümmehen).
ap. "^bumimadana- (Spiegel, Ar. Periode 68).
240. böi, bö 'Geruch*, böytden^ böyämden {Je^. X'är.)^),
böstän, biistän,
aw. baoiöi- *Wohlgeruch' ; phlv. böd, böi, böylnUan;
ai. [^biidkr merken, wahrnehmen'.
') Die Aussprache mit ö ist möglioher Weise falsch. Inzwischen
ist Nöldeke, Pers Stud. II, 1 Anm. 4 hinzugekommen.
^) Nach Barth oloraae, KZ. 29, 547 Anm. 2 bedeutet Büsyqsta-
'Zukunft', d. i. Mas auf die lange Bank Schieben, Saumseligkeit'.
^) Scops giu, Blanford, Seite 115.
*) Berliner Handschrift Hamilton 691, Fol. 657, vergl. Hern,
WZKM. 4, 131 folgg. Bei Vullcrs fehlt das Verbum.— 55 —
af/. LW. hü, bö; oss. biid 'Weihrauch* (65); bei. hör/,
n. 6ö(J, böz *Balsanistrauch' (46); si/n. böi (LW.), sar.
bäo.
241. bih 'besser, gut', bihln.
Käs. veider, bahtdr, bihter, bihter[te)\
ap. Vahyaz[data' N. pr. ; kSlw, vaht^h- ^besser j phlv.
D^h, vehlh.
Die Erklärung der np. hinsichtlich ihres Vokals bis-
her nirgends richtig verstandenen Form hat mir Herr
Dr. Andreas schon vor mehreren Jahren mitgeteilt: bih,
wie mih und kih sind Comparative, deren i durch
=== leaf/page ===
2446 leaf 75
```


## [2026-09-05T14:08:33.408Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN buxtan/poz ===\"; grep -n -i \"bōxtan\\|buxtan\\|pōzis\\|pözis\\|pozis\\|puzîdan\\|püzis\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"baoi\\|bōd\\b\\|böd\\b\\|buxtan\\|pözis\" HUB.txt | head -20\necho \"=== CHEUNG baug ===\"; grep -n -i \"baug\\|bauj\\|\\*baud\" CHEUNG.txt | head -30"
}
```


### [2026-09-05T14:08:33.488Z] TOOL RESULT

```
=== HRN buxtan/poz ===
3180:336. pöziS 'Reue, Entschuldigung', pöztden (Vis und Kämm, ^
=== HUB ===
1044:= zd. baoidi') zuriickfiihren. Np. mad 'Kuss' erinnert
7072:boi {ho) *Geruch* = zd. baoidi- (arm. buidenik Moses, Geogr.
7125:boir (in burem *dufte* u. s. w.) aut *h6d = zd. baoidi-
=== CHEUNG baug ===
500:languages, e.g. *baud ‘to smell’ (*baud! ‘to feel, sense’), *gaH’ ‘to have sexual 
1966:12b from *barj, may rather go back to *bauj’ ‘to rejoice’. 
2114:14 *baudl 
2144:*baud! ‘to feel, sense’ 
2172:*baud2 15 
2198:bösidan/bös- (etc.), which appears to be an inchoative formation of *baud (as 
2214:*baud? ‘to smell’ 
2263:seems necessary to assume two separate Ir. roots. But on the other hand, *baud? may 
2266:be ultimately an ancient specialisation of the root *baud!, cf. Engl. sense. 
2360:18 *baujl 
2367:*bauj! ‘to bend’ 
2436:*IE COGNATES: Gr. gevya, Lat. fugio ‘I flee’, Goth. us-baugjan ‘to wipe off 
2441:*bauj° “to enjoy, experience” 
2458:The evidence for a root *bauj’ ‘to enjoy, experience’ is confined to three East Ir. 
5017:awake’ (*baud'), Lat. albeö ‘I am white’ (albus ‘white’), etc. > LIV: 114 f. | Pok.: 
11734:Geiger 1891: 436, accepted by Korn 2005: 1.с., viz. from *buxs-, *bauj” ‘to release, 
11736:enlarged root *buxs- of *bauj” in Iranian. Citing from Shahbakhsh, we apparently 
11740:origins. The former clearly derives from an inchoative formation *buxsa- of *bauj’, 
53467:us-baugjan, 19 
55136:*baud' (s.v.), *fraiH (s.v.), 
55759:*bauj , *kamp, *kauc, *nam 
55788:*bauj (s.v.), *kauc (s.v.), 
56297:*bauj? 
56591:*baud' 
56950:*baud' (s.v.), *maic (s.v.) 
57536:*bauj”, *harz, *(Н)иас, 
57783:*baud' 
57931:*baud’, *eant, *eraH, *pauH 
58254:*bar (s.v.), *baud' (s.v.),
```


## [2026-09-05T14:08:38.440Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2114,2300p' CHEUNG.txt"
}
```


### [2026-09-05T14:08:38.496Z] TOOL RESULT

```
14 *baudl 


(+ *ш-) ? Oss. D. ivaerzun/ivarzt ‘to promise; to give hope’ (< *‘to cushion someone 
against unpleasantness’ ?) || (+ *ham-) І. emberzyn/emberzt, D embarzun/ 
ambarzt ‘to cover’ 

*SANSKRIT: barh ‘to stretch, put under(neath)’ (homonymous with barh ‘to make 
strong, make great’) || barhis- ‘straw, sacrificial straw, bed of kusa-grass’ (R V+). 9 
The root barh with the meaning ‘to stretch, put under(neath)’ is attested in, notably, 
the following RV-passages: 1.53.6, 5.61.5, 10.10.10. = EWAia II: 212 ff. 

The generally accepted connection with Olrish bolgaim ‘I swell up’, ON bolginn 
‘swollen’, etc., found in Pokorny: 125 f, LIV: 73 f., to which we may add Skt. barh 
‘to make strong, make great’, is difficult to uphold semantically. It rather suggests 
the existence of two separate, yet quite similar, roots: *b'elg/é- ‘to swell up’ and 
*b'eld^-, which is continued in Пг. *barj"is-, etc. The latter root appears to have only 
nominal IE correspondences outside IIr. The Oss. / Ved. verbs probably reflect an 
old Пг. denominative of *barf'is-. 

«PIE *b'elg"- ‘cushion’ > LIV: - | Pok.: 126 

*IE COGNATES: Slov. blazina, SCr. blazina ‘pillow, cushion’, OPr. balsinis ‘cushion’, 


Lith. bainas ‘saddle’ 
*REFERENCES: IIFL II: 418a, 260; Abaev, Slovar’ I: 137 f., 554 f.; Yarshater 1969: 208, 105, 1210 f. 
(passim); EVS: 83b f.; DKS: 389b f.; Benzing 1983: 210; Steblin-Kamenskij 1999: 380 


*baud! ‘to feel, sense’ 

*AVESTAN: baod-, Y Av. baoö- ‘to feel, sense’ || (+ *pati-) ‘to concentrate on, heed’ || 
(+ *fra-) ‘to wake up’ — Liste: 39 

Pres. {1} ja-: OPT. med. 3sg. YAv. büióiiaeta (Y 9.21), med. 1р1. YAv. büióiioimaióe (Y 9.21); Pres. {2} 
them.: IND. med. 3sg. YAv. baodaite (Yt 17.6); Partic.: pres. {1} med. YAv. frabuidiiamna- (V 18.49), 
pres. {2} OAv. райт... baodant- (Y 30.2), YAv. baodant- (Yt 19.69), perf. pass. YAv. busta- (Yt 17.9); 
Caus.: pres. IND. 359. YAv. baoóaiieiti (Yt 10.90) 

*MIDDLE PERSIAN: ВМР bwd /boy/ ‘perception, sense’ || (+ *pati-) MMP pyws- 
(inch.) ‘to desire, long for’ = DMMPP: 291b 

(+ *pati-) Pres.: pres. IND. 3pl. pywsynd; Partic.: perf. pass. MMP pywst {unpubl.} 

*PARTHIAN: bws- (inch.) ‘await, wait for, expect’ || (+ *pati-) pdbws- ‘to desire, 
yearn’ || (+ *ham-) ’mbwy- ‘to kiss’ = Ghilain: 65, 80 | DMMPP: 118a, 269a, 39a 
Pres.: IND. 35р. bwsyd, SUBJ. 1р1. bws’m, IMPV. 25р. bws || (+ *pati-) Inch.: pres. IND. 1sg. pdbws’m, 
Ipl. pdbws’m, 2р1. pdbwsyd, 3pl. pdbwsynd, SUBJ. 1р1. pdbws m; Partic.: perf. pass. II "pdbws'd || (+ 
*ham-) Partic.: perf. pass. II "mbwy'd; Inf.: П "mbwy'd 

*KHOTANESE: OKh. but- (buv-, bus-) ‘to perceive, know’ || (+ *ham-) LKh. hambus- 
(etc.) ‘to agree, fit? = SGS: 101, 143 

*SOGDIAN: (+ *pati-) BSogd. ptByó-, CSogd. ptbyd- ‘to know, recognize, 
understand’ 


*baud2 15 


Well attested: Pres.: IND. 3sg. BSogd. ptßyöty, CSogd. ptbydty, 3р1. CSogd. ptbydnt, MSogd. ptyByö’nd 
(GMS: $622), OPT. 3sg. ptByó y; Impf.: IND. 3sg. CSogd. ptybyd, MSogd. ptyBy6 (Sogdica: 31), 3pl. 
CSogd. ptybydnt, Fut.: IND. 2sg. CSogd. ptbydyq’; Partic.: perf. pass. CSogd. ptbstyt (pl.) ‘sensible, 
notable’, BSogd. ptBystk 


*NWIR: NP bösidan/bös-, Abyan. busoya/bus-, Khuns. bus-/busa ‘to kiss’, Ham. 
busayän/bus- ‘to kiss, embrace’, NP bös(ah), Kurd. (Kurm.) bösa (m.), Qohr. busa, 
Varz. bus ‘kiss’ 

*NEIR: (+ *ham-) Oss. I. zeembudyn, D. ambodun ‘to sense, feel’. 0 Pash. Iwast-/lwal- 
‘to read’ is probably unrelated, cf. NEVP: 46. The reconstruction *ni-bauda-, 
suggested in EVP: 41, is semantically unsatisfactory, on which see *HuadH. 

*MISC: (+ *ham-) Arm. (LW) hamburem ‘to kiss’, Arm. (LW) hamboyr ‘kiss’ (< 
Pth.) 

*SANSKRIT: bodh ‘to wake, awaken; to perceive, notice, heed’ (RV+) = EWAia II: 
233 

© Rastorgueva — Edel’man, ESIJa П: 136 ff., reconstruct a separate, onomatopoetic 
root *bau-: bu-, *ba-, *bä- ‘to kiss’ (cf. Pokorny: 103), which is probably 
unnecessary. The Pth. form provides us with the clue to the origin of NP 
bösidan/bös- (etc.), which appears to be an inchoative formation of *baud (as 
reiterated by Weber 1970: 107 f.). The other forms cited in support of the root 
*bau-: bu-, *ba-, *bà- are not compelling either. M. bay-/boy-, Yi. boh-/bohay-, Sh. 
ba Cidöw ‘to kiss’ do not show the typical affricatisation of Plr. *b-. 

«PIE *b"eud"- ‘to become attentive, be awake, perceive’ => LIV: 83 f. | Pok.: 150 ff. 
*IE COGNATES: Gr. x£$00 ‘I proclaim, summon’, Gr. леъӨорол (med.) ‘I learn, 
hear’, Olrish ad-bond- ‘to proclaim, declare’, OCS bljusti ‘to take care, look after’, 
Lith. budziu (budéti) ‘I wake up’, Lith. budrus ‘watchful’, Goth. ana-biudan ‘to 


order’, faur-biudan, Engl. to for-bid, etc. 
*REFERENCES: Abrahamian 1936: 111; Abaev, Slovar’ I: 140; WIM I: 66; DKS: 299a Ё; Werba 1997: 208 
f.; Cabolov 2001: 208; Lecoq 2002: 126 (passim); ESIJa П: 138 ff. 


*baud? ‘to smell’ 
*AVESTAN: YAv. *baoö- (bus-) ‘to smell’ || (+ *upa-) ‘to smell, have a smell’ || (+ 
*а-) caus. ‘to incense, suffuse with fragrance ?' || (+ *ham-) ham.baoó- ‘to smell’ 


= Liste: — 

Partic.: med. (+ neg. a-) YAv. aham.baoóomna- ‘not smelling, incapable of using his sense of smell [said 
of dogs]’) (V 13.35, V 13.37), perf. pass. YAv. hupo.busta- ‘well scented’ (Yt 17.9); Caus.: pres. SUBJ. 
3р1. ҮАУ. upa.baoóaiian (V 7.14 f.), OPT. med. 3sg. YAv. a.baoóaiieta (V 9.32, V 19.24) 


*MIDDLE PERSIAN: MMP bwyy-, BMP bwd- /böy-/ ‘to smell [intr.] = DMMPP: 


119a 


Partic.: pres. MMP bwyy’g ‘fragrant’ || (+ *ham-) Partic.: pres. MMP hwmbwy’g ‘smelling’; Inf.: BMP 
hnbwdytn /hamboyidan/ 


16 *bauH 


*PARTHIAN: bwy- ‘to be fragrant’? = Ghilain: 65 | DMMPP: 119a 
Pres.: IND. 3sg. bwyyd 


*KHOTANESE: ОКЪ. bü(d)- (buv-) ‘to be fragrant’ = SGS: 103 

*SOGDIAN: BSogd. Bwé ‘to smell’ || (+ ? *pati-uz-) CSogd. pcbws, MSogd. ptzBws 
“to smell’ 

(+ ? *pati-uz-) Pres.: IND./SUBJ. 3pl. MSogd. ptzBws’nd (Sogdica: 46); Inf.: pres. CSogd. pr pcbws, 
MSogd. pcBwsyy (BBB: 38) 

*CHORESMIAN: (+ *4-) m/’bwzy- (denomin.) ‘to smell, sniff on = Samadi: 2 

*NWIR: NP boy ‘smell, scent’, NP bostan ‘garden’, Bal. bod ‘smell, perfume’, Zaz. 
boy (Ё), Kurd. bo (Ё) ‘smell’, (Sor.) bon ‘smell, stench’ || (+ *uz-) Bal. izbotk 
‘lovage’ 

*NEIR: Oss. bud, D. boda ‘fragrance, incense, scent’, Yghn. vud, wud, wod ‘scent’ || 
(+ *ham-) Oss. I. embudyn, D. ambodun ‘to smell’ 

*MISC: Par. b(u)ham ‘smell’, Arm. (LW) boyr (вооа) smell, scent? 

9 In view of the well-defined, semantic distribution ‘to feel, sense’/‘to smell’ it 
seems necessary to assume two separate Ir. roots. But on the other hand, *baud? may 


be ultimately an ancient specialisation of the root *baud!, cf. Engl. sense. 
*REFERENCES: IIFL I: 240a; Abaev, Slovar’ I: 269, 140; DKS: 294b f.; Paul 1998: 293a; Cabolov 2001: 
204, 206; ESIJa II: 138 ff.; Korn 2005: 185, 357 f. 


*bauH ‘to be, become’ 

*AVESTAN: bauu- (bü-) ‘to be, become’ || (+ *pari-) ‘sich machen über; to get hold 
of; to come to an end? — Liste: 39 

Pres. them.: IND. 3sg. YAv. bauuaiti (Y 10.6, Yt 5.129, Yt 8.14, etc.), YAv. pairi bauuaiti (V 14.17), 3pl. 
Y Av. bauuainti (Yt 5.94, Yt 10.20, Yt 13.15, etc.), YAv. pairi.bauuainti (V 19.27), YAv. ham.bauuainti 
(V 17.13, V 7.58), impf. 1sg. YAv. pairi.abaom (Yt 19.57, etc.), 3sg. YAv. abauuat, Y Av. pairi.abauuat 
(Yt 19.64), INJ. 3sg. YAv. bauuat, 3du. YAv. bauuatom, 3р1. Y Av. baon (Yt 13.38, Yt 5.98), SUBJ. 1sg. 
Y Av. bauuani, 25р. Y Av. bauuähi, 35р. Y Av. bauuät, 1р1. YAv. bauuama (Yt 5.58, Yt 5.73), 3pl. YAv. 
bauuanti (Yt 8.36, Yt 8.9, FrW 4.3), YAv. bauuan; Aor. athem.: SUBJ. Isg. YAv. buua (V 18.29), 3sg. 
OAv. b(a)uuaiti (Y 30.10), OAv. b(ajuuat (Y 28.11), YAv. buuat, 3pl. OAv. b(a)uuainti (Y 33.10, Y 
45.7), YAv. bun, ОРТ. 2sg. YAv. buiia, 3sg. Y Av. buiiät, 1р1. OAv. buiiama (Y 41.4), YAv. buiiama (Y 
70.4, Yt 10.75), 2р1. YAv. buiiata, 3pl. YAv. buiiaras (Ny 3.11), YAv. buiian (Y 55.2, Yt 16.3); Perf.: 
IND. 35р. Y Av. buuauua (Yt 13.2, V 5.25), 3р1. YAv. babuuaro (Yt 13.150); Partic.: pres. bauuant- (Y 
214, Vr 18.2, ЕК 62, etc.), fut. YAv. büsiiant-, aor. YAv. °b(a)uuant- (Y 38.3) 

*OLD PERSIAN: bav- ‘to be, become’ = Kent: 200 

Pres. them.: IND. 3sg. bavatiy <b-v-t-i-y> (XPh 55 f.), 3р1. bava"tiy <b-v-t-i-y> (DNb 14), impf. 1sg. 
abavam <a-b-v-m> (DB 1.28, DB 1.60, DB 1.72, etc.), <a-b-v-m> (XPf 36), 3sg. abava <a-b-v> (DB 
1.32 ff., DB 1.40, DB 1.48), <a-b-v> (DB 2.16), <[a]-b-v> (DB 5.30), 3р1. abava" <a-b-v> (DB 1.76, DB 
2.7, DB 3.78, etc.), <[a]-[b]-v> (DB 2.93), SUBJ. 3sg. bavatiy <b-v-a-[t]-i-y> (DNa 43, DNb 59), 
<b-v-t-i-[y]> (DNa 45), ОРТ. 2sg. "big <[b]-[i]-[y]-a> (DB 4.69), 3sg. Буа <b-i-y-a> (DB 4.56, DB 
4.58 f.), <b-i-y-a> (DB 4.74), <b-i-[y]-a> (DB 4.75), <b-i-y-a> (DB 4.78), <b-i-[y]-[a]> (DB 4.79) 


*bauH 17
```


## [2026-09-05T14:08:49.908Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2360,2470p' CHEUNG.txt"
}
```


### [2026-09-05T14:08:49.955Z] TOOL RESULT

```
18 *baujl 


2002: 244; Lecoq 2002: 184 f. (passim); Kiefer 2003: 193; ESIJa II: 128 f£; Korn 2005: 77 f., 312, 357 
(passim) 


*bauj! ‘to bend’ 

*AVESTAN: (+ *api-) ? YAv. aipi-óDaoya- ‘bending from behind (?)’ (-d- < ?, Yt 
15.45) 

*KHOTANESE: (+ *ni-) OKh. nihujs- ‘to sink down, set’ || (+ *ham-) ha(m)bujs- 
(hambus-) ‘to bow down’. Ф On ру. LKh. hamphajafia see Emmerick, SGS: 160. 
= SGS: 58 

*NWIR: Bal. bog ‘joint, knot’ 

*SANSKRIT: bhoj ‘to bend, curve’ (RV+) = EWAia II: 274 

© The evidence for this root is limited in Ir. 

«PIE *b"eug®”- ‘to bend, bow’ = LIV: 85 f. | Pok.: 152 f. 

*IE COGNATES: Russ. bgat’, Ukr. bhaty ‘to bend’, Goth. biugan, OHG biogan, OE 
bügan, Engl. to bow, OE bog, böh, Engl. bough, etc. 

*REFERENCES: Bailey, Gs Minorsky: 67 Ё; DKS: 188a, 463a; Werba 1997: 212; ESIJa П: 147 ff.; Korn 
2005: 80, 228, 357 


*bauP ‘to release, free, open; to save, deliver’ 

*AVESTAN: YAv. büj- (bunj-) ‘to save, redeem’ = Liste: 39 

Pres. {1} n-: IND. 3pl. YAv. bunjainti (Yt 14.46), SUBJ. 3sg. YAv. (+ aja-!) bunjaiiät (V 7.71, Aog 57); 
Pres. {2} them.: INJ. 3sg. YAv. büjat (Yt 4.3); Partic.: pres. aja- med. YAv. büjaiiamna- (Yt 1.17) 
*MIDDLE PERSIAN: MMP bwz-, BMP bwc- /böz-/ ‘to free, to release’, MMP bwxs- 


(inch.) ‘to be saved’ > DMMPP: 119a 

Pres.: IND. 1sg. MMP bwzym, 3sg. MMP bwzyd, 3р1. MMP bwzynd, etc. 

*PARTHIAN: bwj- ‘to free, liberate, save’, bwxs- (inch.) ‘to be saved’ = Ghilain: 51 | 
DMMPP: 116a f. 

Pres.: IND. 2sg. "bwjyh, 3р1. bwjynd, SUBJ. 15р. bwj’n, etc. 

*KHOTANESE: (+ *pati-) ? LKh. paphüj- (paphv-) ‘to соПес = SGS: 71 

*SOGDIAN: BSogd. Bwxs, MSogd. Bwxs (inch./intr.) ‘to be delivered, freed, get free’, 
CSogd. bwc ‘to save’, MSogd. Bwe ‘to deliver, free’ 

Well attested: Pres.: IND. 3sg. BSogd. Bwxsty, MSogd. Bwxs’m, SUBJ. 15р. BSogd. Bwxs’n, 35р. 
MSogd. Bwxs’t, etc. 

*CHORESMIAN: ? mj[Bwzy- ‘to drag, pull out, away’ (cf. Henning 1971: 11b) 
= Samadi: 43 

*BACTRIAN: Boy- (pret. stem) ‘to save’ = S-W, Bact.: 187a 

*NWIR: Bal. bötk/böj- “о open’, butk/busk- (inch.) ‘to be released (from jail), be 
fired (a gun), be emptied’ (see also *Hax8), Kurd. (Sor.) būžānawa/būžē- ‘to revive’, 
? NP buzidan/buz- ‘to pluck off hair, wool’ (LW) 

*NEIR: Oss. І. byğdæg, D. bugdzg ‘open (of space), not enclosed, laid bare’ 


*baxs 19 


*SANSKRIT: ? Pali bhufijati ‘cleanses’ > EWAia П: 275 
«PIE *b"eug- ‘to release, flee’ > LIV: 84 | Pok.: 152 


*IE COGNATES: Gr. gevya, Lat. fugio ‘I flee’, Goth. us-baugjan ‘to wipe off 
*REFERENCES: Abaev, Slovar’ I: 277; Bailey, Gs Minorsky: 67 f., Cabolov 2001: 214; ESIJa II: 145 Ё; 
Shahbakhsh: s.v. busk-; Korn 2005: 86, 229 f., 357 (passim) 


*bauj° “to enjoy, experience” 

*KHOTANESE: Khot. bujsana- ‘feasting’ || (+ *ham-) OKh. hambus- ‘to enjoy’ 
=> SGS: 143 

*CHORESMIAN: ? m/ž- ‘to rejoice, become happy’. Š According to Henning 1970: 
12b this (hapax) verbal form is possibly from *barj ‘to praise, honour’, which is 
semantically not quite satisfactory. Samadi, l.c. therefore cautiously suggests *barz 
‘to enlarge, make high °’, which is, again, semantically somewhat imprecise. The 
etymology suggested in ESIJa II: 150, which derives ßZ- from the formation 
*buj-1a-, is perhaps more preferable. = Samadi: 47 

*NEIR: Oss. I. byxsyn/byxst, D. buxsun/buxst (inch. ?) ‘to go through, tolerate, bear, 
endure’ 

*SANSKRIT: bhoj ‘to enjoy; to make use of (RV+) = EWAia II: 275 

The evidence for a root *bauj’ ‘to enjoy, experience’ is confined to three East Ir. 
languages. 

«PIE *b"eug- ‘to enjoy, experience; to make use of > LIV: 84 f. | Pok.: 153 

*IE COGNATES: Lat. fungor ‘[positively] I enjoy, go through, experience, [negatively] 


suffer, endure’, Arm. buci ‘fed, foddered’ 
«REFERENCES: Abaev, Slovar’ I: 283 Ё; Werba 1997: 211 Ё; ESIJa П: 149 f. 


*baxS ‘to bestow, divide, apportion, have a share’
```


## [2026-09-05T14:09:02.570Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD bws ===\"; grep -n \"ßws\\|Bws\\|bws\" SOD_pages.txt | head -30"
}
```


### [2026-09-05T14:09:02.615Z] TOOL RESULT

```
=== SOD bws ===
11982:       scented, perfumed                                               Po8estan   (Pw5stn) ©ob. -yh      =^bwstn
12101:                                                                   2928 bwstn C                                          d^y.
22634:        Frag. Len. 852                                          6600 pcbws- C =$ pcpws-
22636:6587 pc>y C, S                                     Uj¥ t^             pacpos (pcbws-) =^ptzPws-
22641:6588 pc'ycyq M                       jljo^ i<=^> u^L*           6602 pcbws'ny C                                    jb^^-u^
35487:10934 ybwstny = y- +bwstny =4 bwstn
```


## [2026-09-05T14:09:03.730Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS boxt ===\"; grep -n -i \"böxt\\|boxt\\|bözi\\|bozi\\|bwht\" SNS.txt SNS_pages.txt | head -20"
}
```


### [2026-09-05T14:09:03.783Z] TOOL RESULT

```
=== SNS boxt ===
SNS.txt:7570:,*/ bOzisn :^ .(^iz , j>>^* *-C -;(, jl Ghlain, 63) 1 
SNS.txt:7595:■rA/M.c-i.,* .bOziSn^o.ijlj^^^, (fAoflji 
SNS.txt:33555:bOxt 105/23 
SNS.txt:33563:boxtan 106/5 
SNS.txt:33565:boxtisn 106/2 
SNS.txt:33570:bozisnlgtar 108/2 
SNS_pages.txt:4861:                                                                                                                    rA/M.c-i.,* .bOziSn^o.ijlj^^^,
SNS_pages.txt:4932:,*/   bOzisn       :^ .(^iz j>>^* *-C -;(, jl Ghlain, 63)
SNS_pages.txt:16369:bazay 97/4               bavandaglh 110/16              boxtan 106/5              bulandtar 109/6
SNS_pages.txt:16371:ba$ /bag/bay 101/7       bavSd 303/22                   boxtisn 106/2             bun-is 110/9-195/9
SNS_pages.txt:16377:banded 33/6              baxt 97/10-11                  bozisnlgtar 108/2         burld 124/7
SNS_pages.txt:16400:bavandag 110/11          bOxt 105/23                     buland gar 104/16        casisnlh 157/7
```


## [2026-09-05T14:09:10.388Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4850,4870p;4925,4945p' SNS_pages.txt"
}
```


### [2026-09-05T14:09:10.427Z] TOOL RESULT

```
ov
 S'K'^L        L       1«£«»J I*                   ^1*tt>tf I* J£i *, *j'j o' Jj           1
                                                                                               >
                                                                                                                    *"




                                  •   >i*o .w*» i;dtixt:                BRTH y*                tf^'J
                                                                                                                   *<* ^k>   •            t,
                                                                                                                                               ^ ^.^
                                                                                                                    rA/M.c-i.,* .bOziSn^o.ijlj^^^,
                                                                                                                                                  ,               iSn+ £jU(> .9^.     .
                                                                                                                                                                                          |
                                                                                                                                                                                                                     ,




                                                                                                                                                                                                       (fAoflji
ifcfc.     784)duhitar: ^j-*** dujfrfar-, dug»dar-ab-
      ^_l *jLl; Jj^-y)    isn             + ^Uj . c^Ui :           bOz jl c— jx*. ^ I

                                                                                                                                           U/f* .T/TiS (Junker.            5)
j:>!^ (Uir.Man.                 II,           48)     bwzysn:>;i*          (       «vjj >X)                |                                                                                   ,»*o :
                                                                                                                                                                                              tf                 T


,*/   bOzisn       :^ .(^iz j>>^* *-C -;(, jl Ghlain, 63)
                                          ,                                                     1
                                                                                                                                                •T/T^ .asj* :b0d h5nd .                            396Ky    ^
                                    v~ L—^ -t*.L.)l,                                                                                      UJ c— .1- *-L *;l,
                                                                                                                                                         ,

                                                                                                                                                                                                                •A



 bhrlnanti          : ^^.^brlnenti, /bray- 3 fc.                                 I
```


## [2026-09-05T14:09:15.665Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" SNS_pages.txt | head -3\npython3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [4861,4932,16369]:\n    print(target,'leaf',('\\n'.join(lines[:target])).count('\\f'))\nEOF"
}
```


### [2026-09-05T14:09:17.268Z] TOOL RESULT

```
4861 leaf 69
4932 leaf 69
16369 leaf 237
```


## [2026-09-05T14:09:34.984Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 530 531 532 533; do echo \"===== leaf $n =====\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' BQT_v1_pages.txt | head -60; done"
}
```


### [2026-09-05T14:09:36.958Z] TOOL RESULT

```
===== leaf 530 =====
بن کوهی
ممروف است که زیر ره کوش باشد  -‏ و کتابه
ازاطاعت وانقیاد و صدق وادب تمام بود- و سخن
ع ۰ ۳ یز گویند .
لین کوهی» بنتم اول و کسر ثانی »
کیاهی است بیار چرب, واز آن آش پزند.
شاه - بنم اول وسکون ثانی وفتح‌کاف
فلرسی و اظ هار های حوز ۳ نمعنی شگاه است که
جا ومقام ومنزل باشد ۱ - وجاییرا نیز کون که
نقد وجنس درآن گذارند _ و باخفای ها بمنی
بانگه است که کشیدن واز باشد.
پنالاد- بالام بر ون بنیاد ؛ بععنی
بای عمارت و دیوار باشد - و بشتبان دا پیز
کت
پنهین ۴ با میم بروزن پروین » بلفت
زند و پازند (۱) پسررا گویندکه برادر دخثر
است. وبجای تحثانی فوقانی هم‌بنظر آهده است»
وا اعل .
نی ع بفتح اول وضم انی وسکون واو»
خرمن هرچیز را گوبند اعم از گندم وجو و کاه
وعر آن .
پنوان ۴ - ینتم اول بر وزن دربان »
نگهدار ند زراعت و نگاهبان خرمن را گوشد ‏
وضم اول همآمده است- و نگاهدارنده اسباب
وامواق را یز گفته‌اند.
بنو در مب بفتم اول و ثانی و رای قرشت
و صکون ات بمعتی اول بنلاد است که بنیاد
۵ ۳ سه
وسای عمارت ودیواز باشد.
بوسر جع بنم اول و تانی و سکون
ثالث وضم‌سین بی‌فطه وسکون رای قرشت‌وخای
کویند. خوردن آن تازیکی چشم آورد.
نو سیاه د بنو معلوم .۰ سک ات
بی‌نقطه ونحتانی بالف کشیده وبهای زده ؛ غل
ایست که‌آنرا ماش کونند» و آن مسمف دندان
ومضر باه باشد.
بنوماش- بنو مملوم , و میم بالف
کشبده وشن فرشت زده» «ممنی بئو سیاه است
ی تپ راتیز گوبن دکه آن‌نوعی
ازمای است
بنق فخله- بنوسملوم. بنتح نون‌وسکون
وه » بفتح اول و ثالث و سکون ثانی
و اخفای های هوز , مطلق خرمن را گویند اعم
ازخرمن غله وکاه وضرمب وحم انی واظ پارهای
هوز بیز هست که بروزن صبوح باشد.
له ۵ - بنم اول وفتح ثانی» بار و اسباب
و رخوت خانه - + املاك - ودکان - و خانه
و مکان و متزل را گویند ٩‏
هر چیز را نیز گفته‌اند ۷ - و یفتح اول طناب
باريك را گویند ۸ .
بله بستیی - کنایه اکوچ کردن وسفر
 . باشد‎
وییخ ور شاد
ات اتکی
بشدهش .»٩۰‏
۹ ی دک بنه خواب بسوزیم
از تلم بد 7 همی بشرسی
۴ - هز,بنمن؛ پهلوی۳۱6 (پس)«یوستی.
بهلوی ۲0028 .
زیرا که چنین‌دوات بدار درآعد.مولوی‌بلخی.
===== leaf 531 =====
هه بولرد
بنیاد بر بخ نهادن- کنبب. از | جممی را کوندکه بر اصناف حرفت و املاه
بی‌مداری وبی ثباتی باشد. می بندند .
بثیان» بنم اول و سکون تانی و تحتانی یز « بکسر اول بروزن متیز ۰ بمعتی
بالف کشیده وینون زده » نام حوض نسمان است. هر کز و حاشا باشد- و بممنی تعجیل و زود حم
و آن برکه‌ای بوده, آب آن در نهایت شوری | آمد است- وگاهی درمیان سخن بجای نیز عم
و تلخی و ی رکت ندوم سرور کابنات آب آن _ بکار برند که بعربی ابضاکویشد ۱ .
شیرین شد . نیا بروزن شريك ؛ ابریشم فرومابه
پثیچه - بنم اول بر رزن کلیچه . | باشد وآنرا کج و کر وف زکوبند.
بیان ست وسوم
در بای ابچد یا واو مشتمل بر بکصد وچهار لغت و کنایت
تایکمان فرزند خووشیر بدهد .
واه ضم اول و شانی بالف کشیده »
وه بش اول و سکون ثانی مجپول؛
ممروفی است که رابسه باشد ۴ - ومضفف بود
وباشد و بوم و باشم هم‌هست ۴ - وگوشت بز
کوهی‌را نیز گوبند- وختح اول پوست شتریجهة
پرکاه کرده را کون که پیش ناقةبچه مرده‌ببی ند
مخفف بودا باشد بعنی بادا .
او ارت" - بکر اوزءئاتی بالف کشیده
نه آن زین بازرد روژی بنیز ده این را از آن اندهی بود نیز
ولیز ازرقی گفته است : .
درمدح ناکان نکنم کهنه تن بنیز زآن باك تابدم که بود کهنه بیرهن:
کم «بتیژ» بمعنی هرز استعمال کرده است.
۴ - پهلوی ۵۵0۳8 , 0۵۷ «منای ۲۹۸ : ۲ » «اویوللا ۰۳۸۰ . اوستا نطفههط
«بارئولمه ۰٩۱۸‏ , ارمنی 201۲ «بی رکه ۳۷ » , اورامانی 9۵ 2۶ . اورامان ۱۲٩‏ »۰ کیللکی
۷۵ ختنی لا « رو ز کار لو ج 4 ش ۳: کشور ختن » - در اوستا 3۵00102 به‌عنی بوی
خوب (در مقابل 8280 بمنی کند. بدبوی) آهده و بیهفی ممنی لفوی بوی را بك دريافته که
درتاحالمصادر درلغت «اخشم» که بىعنی کسیست که حاسة شامه نداشته باشد" گوبد : «اخشم» آتاث
بوی و کند نشنود.» (نته خطی کابضانةً علامه دهضدا). فردوسی گوید:
زمین بود در زیر دبای چن پراز درخوشاب دوی زهن
می و بوی آواز رامشگران عمه‌بررسرانا راز کوهران.
(معنی : بوی خوش) «شاهنامة بخ ح ۳ ص ٩۵۳۵‏ . دریهلوی ۳۵ بدوهمنی: بوی خوش
و گاهی ووجدان‌آمده «بوستی . بندهش ۳-۹۲ ورگك: بوی. ؟ - ازربثة فالا (بودن) (سم).
۴ - ختح‌اول و دوم و کسر چهارم" عربی جمع: بارد » منرادف «مبردات» «دزی۱ص۸».
===== leaf 532 =====
بولی ۱
شیرینی است -
بواس. فتح اول بر دزن ایای 0
محتت وآزّار ورنج وسختی باشد.
بو اسحق طافه‌ای باشند ۱ -و در
نشابور چند ان فیررزه حست دک از آن ر)
بو اشه - بفتح اول بر وزن نراشه ؛
چارشاخ دهقانانرا کویند» وآن چویی چنه باشد
باندام کفدست و دسته ای نیز دارد که دهفانان
بدان غلهٌ کوفته را برباد دهند تاازکاه جدا شود
ء آنرا جربی مذری خوانند .
بو الححدر- با لام و خای نقطه دار
, جیم و دال بی نقطه بروزن کل برسر . ماحد
+ بی‌دهن ومی‌دفات را گویند.
بو القاسیم - کنابه‌از بوالفضول و شوخ
بو )لکد - بفتم کاف وسکون فا ودال
امجد . پمعتی رشوت وپاره باشد ۴ .
+سکون نون و فتح جیم و کاف ساکن, هرچیز
که آن عجیب و غرمب و طرفه باشد و دیدش
تفه آوری ۱
۵ ۳ 2
وس « بروزن خوب . فرش وباط
- ۳۱۲
خابه را گزنند. وباين ممنی بجای حرف اول بای
حطی‌هم آمده است.
بویا ۱ بنم‌اول و سکون ثانی وبای
امجد بالف کشیده » آشی را گون که از گوشت
بز کوهی پخته باشند.
بو لاش ه بسکون شن قرشت. بمعنی
قدیم وجاوید وهميشه و-رعدباشد ۷.
او برك « بنم اول ء ثالث وسکون انی
و را و دال بی نقطه ؛ بلبل را کویند. و بعرمی
عندلیب خواننه .
بو ۵ یر دس ختح دال وسکون کاف »
عصذر بوبرد است که بلبل باشد. :
بو باك بائالی مجهول بروزن خوبك ؛
دختر بکر ودوشیزه را گویشد - و هدهد را نیز
احمق وتادان را گویند .
لو لاو بسن دو بای امجد و سکون دو
واو , شانه سر و هدهد را گونند و آنرا مرغ
خواهر خودرا بوبو خوانند .
بو بو 4 « بفتح بای حطی. بمعنی بوبو
است که شانه‌سر وهدهد باشد۷ .
بو ب4 - نم اول و فتح الث» بمعنی
آرزوهندی وارزو باشد و سربی تمنی گویتد ۸
۳ "۳ رك ۳ مکقد.
0 , پهلوی 0۵۲ (فری) « اسفا ۱
روز دىگرشاه بزمآراست خوب
دساثر ۲۳۹ ».
ممتی ممحف بوبه است ( ۵ . م ) .
9 96۵ در آرهنی
۲ - از دساتیر * فرهناك
. ۸ باین
( برهان فاطع ۵ )
===== leaf 533 =====
۳ن حد
که آرزو باشد بجای حرف اول بای حطی عم
آمده ات ٩‏ . #
رستنی ودرخت پرشاخ وب رکی را کوبند که بسیار
بلند شود وبزمین ترديك باشد ۴ و بچةآدمي
و سایر حیوافات را گوسد عموماً و بجدٌ شتر را
خسوصاٌ- وبمعنی نان تیرهم آمدهاست- وظرفی‌را
نی زکوند که از کل حکمت ساخته باشند و طلا
و نقره و امثال آن در آن بگذارند. ومعرب‌آن
بوشه , و بعربی خلاص گویند 1
بق قة خاك - کنابه از بدن و قاب
اسان باشد.
بو تیمار. بامیم پروزن حوسیقار . نلم
مرغی است که اورا عم خورك نیز گوند . و ا
پیوسته درکنار آب نشیند وازغم آنکه مباداآب
کم شود باوجود تتنگی آب نخورد واور! بمربی
یمام و یبونانی شفنین خوانند . خوردن گوشتش
بیخوایی آورد, رمقوی فوت حافظه باشد وذهن‌را
(۱) چك
۱ ر(ه: ح*۱ صفحه قبل. ۴ 9618
«اسفا ۲:۱ ص ۸۰*. ۳ رتفا دز
پهلوی بمعنی بز ( بضم اول ) است ۶ موستی .
بندهش ۱۰ . ۴ حز, 3۵۵ .
8 , پهلوی ۷2۲ , خار « بونکر
۲ ». بوچیناك (0۷1[۷12), خبار « بوستی.
دش ٩*‏ ۲ و بنابرین بوجیا مصحف «بوجینا»
و «بوچینا» است
ه بو تاسپ ‏ رنه بوداسپ. » #ردا -
ساسکرت ۵2۵( ( بمعنی بدار »
آ کاه . باهوش , زرنگگ و خردمند ) . نام وی
سدارته کوتمه 02008۳08 510082۲۳12
و مشهور است به ساکیامونی ۵۵۲001
(حسکیم‌قببلفسا کیا)باسا کیاسینه 5۵9-51۳02
( و دونام اخیر نام خانواد کی او بوده) » ولی
کوناما اسبی است مأخون از نام نژادی که
خاندان وی بدان تعلق داشت. یدر او سوددنه
: ژید و جاژند .
تند و نیز کند .
بوچ « بفتح اول و سکون نالی و جیم
فارسی ۲ ۳ اول
اندرون دهانراگوبند ۴ .
کشیده بروزن بوسنا» بلغت زند ویازند (۱)خیار
بادرنگکهرا کونند ۴
بو‌حا - با حای بی‌نقطه بالف کشیده .
بلفت بونالی گیاه ماه پروین را گویند و بخ
آنرا بربی جدوار خوانند و گویند با پیش در
مکجا روید,
بوخت.- دروزن صوخت» دمعنی بسر باشد
که‌برادر دختر انش
بو خلی » بررزن فوفل, خرفه راگویند
بو خله- بنتح الث و لام» بععنی بوخل
است که خرفه باشد » وبضم تالك هم بنظر آعده
است رد
```


## [2026-09-05T14:09:52.578Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"بیوس\" BQT_v1_pages.txt | head -20\necho \"--- leaf calc ---\"\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor i,l in enumerate(lines,1):\n    if 'بیوس' in l:\n        print(i, ('\\n'.join(lines[:i])).count('\\f'), l.strip()[:120])\nEOF"
}
```


### [2026-09-05T14:09:54.203Z] TOOL RESULT

```
2809:بسیار بظپور بیوست. خاصه که قرن‌یازدهم درمیان سایرقرون تاریخ‌ادییات
6292:چشمه‌ایت که مدت هفت سال بیوستهروان‌باشد
16116:دوم (۱) بادیی است و آن شخصی باشد که‌بیوسته
17446:بیوست کسی افتادن - کنابه از
22786:افموی که دور به‌بیوسی بگذشت
--- leaf calc ---
2809 95 بسیار بظپور بیوست. خاصه که قرن‌یازدهم درمیان سایرقرون تاریخ‌ادییات
6292 218 چشمه‌ایت که مدت هفت سال بیوستهروان‌باشد
16116 427 دوم (۱) بادیی است و آن شخصی باشد که‌بیوسته
17446 452 بیوست کسی افتادن - کنابه از
22786 562 افموی که دور به‌بیوسی بگذشت
```


## [2026-09-05T14:09:57.226Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==563' BQT_v1_pages.txt"
}
```


### [2026-09-05T14:09:59.061Z] TOOL RESULT

```
نبویرد
شده است واوباریدتن بفتح همزه بمعنی
فرو بردن و بلم کردن باشدا . ۱
ایو بر ك ع بکس اول و ضم بای ابچد
بروزن پی‌فشرد ۴. ماشی بیوباربدن است‌.هنی نا
جاویده فرو برد و بلم کرد , وبمی مصدر عم
که ناجاویده فرو بردن باشد ؛ و در
اين لفت نیز همزمرا بیا بدل کرده اند همچو
بانداخت که بشداخت شده»وامثالاین بسیاراست٩‏ .
تیوه » بکس 4 و فتح الث بروزن
زبور» بمعنی ده هزار است؟ - ونام‌ضحالك ماران
هم نت واو را و و ستجقیف
سور خوانشد لیکن صاحب فرهنگه باین معنی
ختح اول و ضم ثانی آورده است - و گردکان
و بادام و بته را نیز کفنه‌اند که معزآنها تیز
و ضایم شده باشد .
بیو درك ع با ثانی مجپول بر وزن‌بی‌درد»
نام مبارزی است که افراسیاب بمدد پیران وسه
فرستاد- و نام‌شهرست درخراسانمتهوربباورد۴ .
1
و وجه تسمیه‌اشآنکه پیش از پادشاهی ده هزار
اسپ داشته است و بزبان دری سور بروزن یور
بمعی ده هزار باشد واو را باین اعتبار بدین نام
میخواندماند. و نام اصلی او بیور بر وزن صبور
ت چنانکه گذشت
دوس <« بنتح ود بروزن‌عروی ۰ طمع
وی ام
چا
و خواهش و امیدوامیدواری باشد بجیزی از هر
نوع که بوده باشد - و بمعنی تواضع وچاپلوسی
و اتظار هم آمده است٩‏
۱ لبق سل با دال ابجد بروزن ضرورت.
مشتق آزیوسیدن است یمنی طمم کند و امیدواد
دد ۹
بیو‌سنفه -_بنتح اود و سکون نون»
بمعنی نواضم و چایلوسی کننده‌ب‌اشد وامیدوار
شده را نیز کوند۸
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


## [2026-09-05T14:10:08.131Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FFD leaf 44-46 (printed 39-41) ===\"\nfor n in 43 44 45; do echo \"--- pdf $((n+1)) printed $((n+1-5)) ---\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' incoming/FFD/FFD_pages_faseng.txt; done"
}
```


### [2026-09-05T14:10:10.028Z] TOOL RESULT

```
Exit code 2
=== FFD leaf 44-46 (printed 39-41) ===
--- pdf 44 printed 39 ---
awk: cannot open "incoming/FFD/FFD_pages_faseng.txt" (No such file or directory)
--- pdf 45 printed 40 ---
awk: cannot open "incoming/FFD/FFD_pages_faseng.txt" (No such file or directory)
--- pdf 46 printed 41 ---
awk: cannot open "incoming/FFD/FFD_pages_faseng.txt" (No such file or directory)
```


## [2026-09-05T14:10:12.474Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD && ls\necho \"=== grep ===\"; grep -n \"بیوس\\|baud\\|pati-baud\\|بوی\" FFD_pages.txt | head -20"
}
```


### [2026-09-05T14:10:12.524Z] TOOL RESULT

```
FFD_asmaneketab.pdf
FFD_pages.txt
FFD_pages.txt.pages
=== grep ===
1086:: بوییدن
1088:بویید < فارسی میانه 0010.00 مادهٌ ماضی جعلی است» از ماده مضارع ساخته
1091:بوی < فارسی میانه ۵ < ایرانی باستان 0204-2*. برای 2 > آرای. ريشةٌ ۳2۵
1121:بیوسیدن
1123:( بیوسید» ماده ماضی جعلٍ است. از مادهٌ مضارع ساخته شده است.
1125:: بیوس < فارسی میانه 02789 < ایرانی باستان 0211-0809-8*. برای 2 -> آرای. 041
1129:برای ساختن مادهٌ آغازی از ريشه به کار رفته است. ريشةٌ 0304 به معنی «بوی بردن»
1130:است. واژةٌ «بوی» فارسی دری از 210 گرفته شده است.
2298:406 (ريشه < بوی بردن - پی بردن) ۳۹ ۴۰ ۵ ۴۹
```


## [2026-09-05T14:10:21.096Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\nsed -n '1080,1135p' FFD_pages.txt\necho \"=== page tag near ===\"\nawk 'NR<=1135 && /pdf page/{p=$0} END{}' FFD_pages.txt\ngrep -n \"pdf page\" FFD_pages.txt | awk -F: '$1<1140' | tail -5"
}
```


### [2026-09-05T14:10:22.750Z] TOOL RESULT

```
دین من به هر شهر (: کشور) پیدا خواهد بود (: شد).
[pdf page 44]
ماده‌های ماضی و مضارع فارسی دزی سس ۳۴۹
رودکی:
کنون زمان دگر گشت و من دگر گشتم
عصا بیار که وقت عصا و انبان بود (: شد)
: بوییدن

بویید < فارسی میانه 0010.00 مادهٌ ماضی جعلی است» از ماده مضارع ساخته
شده است.

بوی < فارسی میانه ۵ < ایرانی باستان 0204-2*. برای 2 > آرای. ريشةٌ ۳2۵
به‌معنیابری بردن»» «پی بردنْ» است.

بیخت < فارسی میانه < ۷۷881 ایرانی باستان ۷۵1-۱۵*. برای 1۵ -> آراست. ۷1 و
8 صورتهای اصلی ۲۵5 هستند. ريشةٌ ۷۷81 به معنی «غربال کردن» و ريشهٌ ۷:88
به‌معنی «تکان دادن» است. «بیختن» در فارسی دری و ۷88127 در فارسی میانه به دو
معنی به کار رفته‌اند: ۱-«غربال کردن»» ۲-«افشاندن»» «ریختن». در شاهنامه آمده است:

بسی زر و گوهر همی ریختند زبر مشك و عنبر همی بیختند

پیز <ج فارسی میانه ۷82 < ایرانی باستان ۵6-۵:*, 8-[نه/*.

برای 2 آرای. در ۴نه۷به جای تاو [در [نة۷به جای 8 آمده است.

به طوری که ملاحظه می‌شودء يك فعل فارسی میانه» بر اثر تحول لفظی» یعنی
بدل‌شدن [و 2 ایرانی باستان به 2» ۷87128 جانشین له و ۷۵18 شده است.
فارسی میانه و دری از این گونه واژه‌هاء که «مشترك» و «هم‌آوا» نامیده می‌شونده زیاد
دارد:

شیر: لبن < فارسی میانه 875 < ایرانی باستان 417۵د*.

شیر: اسد < فارسی میانه 5287 < ایرانی باستان ۹۸8۲۵*.

دوش: شب گذشته < فارسی میانه 465 < ایرانی باستان 48052*.

دوش: کتف < فارسی میانه 5 << ایرانی باستان 4۵۷5*.

دوش: دوش حمام < فرانسوی ۰.4062
[pdf page 45]
0 11 ان دار
بیوسیدن

( بیوسید» ماده ماضی جعلٍ است. از مادهٌ مضارع ساخته شده است.

: بیوس < فارسی میانه 02789 < ایرانی باستان 0211-0809-8*. برای 2 -> آرای. 041
پیشوتد فعلی است.

4-8 صورت اصلی ۳۵9 است. 4 پیش از ۶ به 5 بدل و در آن ادغام شده است. 5
برای ساختن مادهٌ آغازی از ريشه به کار رفته است. ريشةٌ 0304 به معنی «بوی بردن»
است. واژةٌ «بوی» فارسی دری از 210 گرفته شده است.

پادن, پاییدن

پاد <ج فارسی میانه 034 « ایرانی باستان 03-12*. برای 18 -> آراست. ریشهٌ ۳3 به
معنی «پاییدن» است.
=== page tag near ===
1004:[pdf page 41]
1029:[pdf page 42]
1054:[pdf page 43]
1081:[pdf page 44]
1119:[pdf page 45]
```


## [2026-09-05T14:10:35.987Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FSF nabiyusan ===\"; grep -n \"نابیوسان\\|بیوسان\\|بیوسیدن\\|بیوس\" FSF_pages.txt | head -20"
}
```


### [2026-09-05T14:10:36.045Z] TOOL RESULT

```
=== FSF nabiyusan ===
6205:‫(اسم فاعل از بیوسیدن به معنی اميد و‬
6215: ‫نابیوسان به معنی‪ :‬ناخواسته نهبر ارزو‬
6219:          ‫برآمد یکی نابیوسان نبرد‬                             ‫پسر را به خون دادی از بهر تخت‬
```


## [2026-09-05T14:10:36.624Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD leaf 179 (approx p.113) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==180' SOD_pages.txt | head -60"
}
```


### [2026-09-05T14:10:38.619Z] TOOL RESULT

```
=== SOD leaf 179 (approx p.113) ===
                                                                                                                         114
 Pw5*ndc

 2883 pwa^dc M                                 >*"^>A^                 TSP 5.45; S W, IIJ 1976, 60f; TSP 13.25
      Po5andz/c ©f. adj. ^pwfrntch                                2896 pwSst'n    B, M, S                              jt^*
       scented, perfumed                                               Po8estan   (Pw5stn) ©ob. -yh      =^bwstn
       Hen. BSOAS 12, 30X16; GMS        1068
                                                                       BSTBL, Vim. 78; SCE 2; GMS 1118; Frag. Len.
 2884 pwB'ndyCy) M                         J^^j^j^
                                                                       garden
                                                                         29.11; TSP 21 iii 15
      PoSandc (pwa'nt'k, Pw6>nty) ©pi.-/
      perfumed, scented, fragrant                                2897 pwSstn =* pw5st>n
      BBB; GMS 1068; VJ 11; TSP 3.204 n pl98;                    2898 pw6stnp) S                              j^UjlJl^.*
        BSTBL, padm. 41; Frag. 4; Hen. Tales. 476.18;
                                                                       Po5estan-pa
           MSP b55; flw&ntkw, VJ 868
 2885 pw5,nt)k     B ^ PwS'ndy(y)                                      gardener
                                                                       Frag. Len. 29.20

 2886 pw6>ntch       B                                           2899 bwd-xwrty       C                             iJUJji/
                                               Jcuu> t^5j^"y>-
       poSandz    ©f. adj. ^Pwfi'ndc                                   po5-xwartc     ^PwSywrt'kCw)
                                                                       delicious
       perfumed
       VJ 91, 1435                                                    C2, 48V8
                                                                 2900 pwy B, S                                     ^Uj oU;
 2887 pw5>nty     S «> Pw5>ndy(y)
 2888 pw6 pr'n B                                                       Poy ©<*bauga-
                                          iS*r*J=~ iLrtAicr'>"         salvation
      Po6-fran, Pod-Paran                                              TSP 2.425, 905, 974, 6.127; BSTBL, Dhu. 201;
      fragrant, having good breath
                                                                         Frag. Len. 88.3; KG 570
      TSP 3.206, 207
                                                                 2901 pwyc M                          <£>:(yj^)J-r«;.U
 2889 pwSprn      B, M                                                P/fuyc (Pwyyc)
       Po5- parn, Po5paran     ©<*bauda-\ barana       ohjU*
                                                                       ninth month of the year
       scentholder
                                                                       GMS 1275; Hen. JRAS 1945, 151.7, 149.10;
       VJ 14, 94; Sogdica. 52.9-, GMS   1029-, Sogd. Cpds.
         147.7                                                          flwTyc, MDii, Nov. 6, 5
                                                                 2902 pwY5,r-   B, S                      ^ob«(jibo^
2890 pw86 M                         iyJtjiiJ=^i<rj^ lSj3.
     po5 (pw55h) =>pwS, Pw5h                                           Puydar (PwytwS'r-) ©perf. st. =»Pwyt-
                                                                       GeOsave, 0o)be saved
     incense, scent, perfume, olfaction
                                                                       KG 2338; Frag. Len. 93.18
     GMS 1 193; VJ 16, 96, 20\ 844, 894, 880; SCE 84
                                                                 2903 pwys- B, S                     jjiiUj < jaboU*
2891 pw65h       B => pw56
                                                                      Puxs (Pwxs-) ©<*buxsa; Parth. MP bwxs-
2892 pw6ywrt)k(w) S                            0>^                      ©3sg. pres. fiwxsty
     po5-xwarte, Po5-xurte =>bwd-xwrty                                 (to)bc saved, (to)be delivered
     good-tasting, delicious                                           GMS 520, 825; SCE 350; TSP 2.1080, 1141, 1194;
     MDii pi 39.6; C2, 48V8; MDiii p70, A 16.6                          BSTBL, Padm. 20, Dhu. 235; VJ 535; AVS 73
2893 pw5h B, M, S                   ^L^ <>* *J>j^iSj>.           2904 pwyt-      B, S                     j^boUi ^LoU;
     Po5 ©ob. -yh =*PwS5, Pw6
                                                                      Puyd ©<*buxta ©pt. st.
     perfume, sense of smell, olfaction
```


## [2026-09-05T14:10:48.694Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==179' SOD_pages.txt | head -70"
}
```


### [2026-09-05T14:10:50.394Z] TOOL RESULT

```
 113


       C2, 1R8                                              2870 pw-    B, M, S                              ojii < j^
2857 pt'yr- => pt>r-                                              Paw, pu (bw-, bntsq, bwt(y)) =»P~, wP-,
2858 btmyk C                                                        pwt(y), Pwy, Pw'n, Pwt>y, PwtkWn, bwq\PwS'k'm
                                                      ^
       (a)pdmik -^ptmyk                                            PwWm, pw8\ bwtyst\ bwtt, bwtq(n), bynt1,
       seventh                                                     b>z, bym, bnq\ bntq*
       C2, 39V6, 55R17; BSTii 897.77                             0o)be, (rc)become
                                                                 GMS 787-802; AVS 226-9
2859 ptr}ync- B                     b*/^ < J-ojTjLti
     (3)Ptrenc, Patrenj ©<*abi-trnjaya ©impf.               2871 pw'n
                                                                 Pawan (b>n) ©lsg. subj. =>Pw-, P>n
         phrync =>Ptrync-, 'pt^ync-                              GMS 799; AVS 228
       (ro)press, (ro)oppress
       TSP 2.7, 132, 1426; BSTBL, GMS 153                   2872 pw>t => p>tk,m, P>t(y)
                                                            2873 bwc-    C -> Pwc-
2860 ptryt- M                                 o^j/jUi
                                                            2874 pwc- B, M, S                      O^aj <0^ob«
     optrayd, potrayd Optryt-3 ©<*abi-traxta
                                                                 Poc (bwc-) ©Sbaug-* Parth. boi\ MP boz% Av.
       <*trnxta-,
       'Ptryty    A v. Braxia ©pt. st. ^Ptr'ync-,
                                                                   buja =»Pwys-, Pwyt-, Pwy
                                                                 0o)save, (redeliver
       Oppress, (fo)oppress
                                                                 GMS 825; Bailey. Prolexis. 14; Schwartz. BSOAS
       GMS 152b n 1 600; AVS 123
                                                                   1971,412; AVS 73
2861 ptrytky* M                                   ^o^
     (o)Ptraydakya, Potraydakya                             2875 pwc'k S
                                                                 pozak, Poze
       oppression                                                saviour
       Sogdica. 3; BBB 510                                       Mack. AI 1985, 424.1
2862 ptrnng M                    (^jaS;j^A^<Jk<jUi          2876 pwcn'k S
     (o)ptrang, Patrang      ©*abi-trang/ka                      Pocanak -»bwcny, Pwc'k
                                                                 redeemer
       oppression
       GMS 152a, 959; Hen. LW 101                                Sund. MHC p27 n41(-w)

2863 ptrync- M                qzJ'^j* <CpjjTjUj <0->>iJ     2877 bwcny C                                          cr^
                                                                                                        «x^*Uj <Ly^>
     ©impf. fiHrync ^ptr'ync-, 'Ptr'ync-, tryt-                  Pocne =>Pwcn>k, pwc'k
     (/o)oppress                                                 saviour, deliverer
     GMS 152b, 619; Sogdica. 43, 11                              BSTii 867.31; C2, 27V2
2864 ptskpyc B                    (? o^iT *juu) djj, JbJj   2878 pw5 B, M                                j,^. ^ tJi
     apdas-kapic ?                                               Po5 (pww5, bwd) ©<Av. baoda          =»Pw55,
     unit of weight
     TSP 19.8 n p232; Hen. Texts. 713 n 5                        incense
2865 *btts C                                         tjj*        TSPPw5h
                                                                      7.111, 112, 114; STii 3.66; C2 gloss.; BBB
     apd-tas, apdtas =>bttsmyq                              2879 pw5-   B                                   &JJ-+
     seventeen
2866 bttsmyq C                                                   (feOperf ume, (to)smcl\
     apdtasmik                                                   TSP 7.115
     seventeenth
                                                            2880 bwd C *» Pw8
                                                                   Po5
       C2, 55V17; BSTii 898.107
2867 ptyr- =» pt>r-                                         2881 PW81
                                                                 Pu/ot/5a ©2pl. impv. =»Pw-
2868 bw C                                                        GMS 797; AVS 228
       P(a)u ©lsg. inj. =»P-
       C2, 102V24                                           2882 pwS'k'm
                                                                 pu/otaka(m) ©2pL fut. =>Pw-
2869 bw-    C -> Pw-                                             GMS 796: AVS 227
```


## [2026-09-05T14:11:02.291Z] TOOL CALL #35: Bash

```json
{
 "command": "ls site/pages/95.jpg 2>/dev/null; pdftoppm -f 95 -l 95 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg95 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T14:11:02.913Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '6195,6225p' FSF_pages.txt\necho \"=== leaf ===\"\npython3 - <<'EOF'\nt=open('FSF_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nprint(('\\n'.join(lines[:6205])).count('\\f'))\nEOF"
}
```


### [2026-09-05T14:11:04.805Z] TOOL RESULT

```
site/pages/95.jpg
total 30760
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:11 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
```


### [2026-09-05T14:11:08.851Z] TOOL RESULT

```
 ‫حنین نام بر پهلوی راندند‬                                                     ‫چگونه» چسان‪:‬‬
‫‏)‪(AF-FF-1‬‬                                                 ‫همی گفت کاکنون چه سازم تو را‬
  ‫گاهنیز فردوسی ضحاک رابیور می‌نامد‪:‬‬                ‫یکی دخمه چون برفرازم تو را‬
           ‫نه من بیش دارم ز جمشید فر‬                 ‫(‪)۶-۵۵۱-۲۱۳‬‬
‫که ببرید بیور میانش به ار‬                                   ‫نه چیزست بامن نه سیم و نه زر‬
  ‫‪۶۲۲۳۰۷۸۱‬‬                                          ‫نه خشت و نه آب و نه دیوار گر‪.‬‬
                                   ‫بیو سنده‬
                                                                                 ‫نه‪:‬‬
                                                                                   ‫یب‬‫افف‬
                                                                                       ‫مخ‬
‫(اسم فاعل از بیوسیدن به معنی اميد و‬
                                                           ‫تواو را بدین جنگ رنجه مکن‬
 ‫ارزو داشتن)‪ :‬امید دارنده باارزو و امید‪:‬‬
                                                    ‫زی نمانم سخن‬  ‫این‬‫رنب‬
                                                                       ‫کده م‬
                ‫که هرگز نبیند تنم جز زره‬             ‫(‪)۶۰۵-۱۷۶‬‬
‫بسیوسنده و برفگنده گره‬
                                                     ‫(در نسخه لندن و دو نسخۀ دیگر «بین»‪,‬‬
 ‫(‪۶-۵۳۳-۲۴۲4‬‬
                                                         ‫نسخه قاهره «بر» نسخهة دیگر «زین»)‬
 ‫نابیوسان به معنی‪ :‬ناخواسته نهبر ارزو‬
                                                                                     ‫بان «بیندا‬
                               ‫غیرمنتظر‪:‬‬            ‫مرکب ازبیند‪+‬الف آرزومندی و آفرین و نفرین‪:‬‬
          ‫از اسدی ( گرشاسب‌نامه ‪:)۶۷۱-۳۳‬‬
          ‫برآمد یکی نابیوسان نبرد‬                             ‫پسر را به خون دادی از بهر تخت‬
                                                     ‫که مه تخت بیناد چشمت مه بخت‬
‫که دریا همه خون شد و دشت گرد‬
                                                    ‫(‪)۱۵۷۳-۳۱۶-۶‬‬
                                      ‫‪۳۹‬‬                                         ‫بیهده‬


=== leaf ===
128
```


## [2026-09-05T14:11:17.368Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg95.png"
}
```


### [2026-09-05T14:11:17.712Z] TOOL RESULT

```

```


## [2026-09-05T14:11:17.709Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:11:29.814Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD bheudh ===\"; grep -n -i \"bheudh\\|bheug\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T14:11:29.859Z] TOOL RESULT

```
=== AHD bheudh ===
338:bherek-. To shine, glitter. A by-form of bhereg-. Variant form *bhrek-, possible root of various Germanic forms. 1. Germanic *bregdan, to move jerkily (> “to shimmer”), in Old English bregdan, to move quickly, weave, throw, braid: BRAID; UPBRAID. 2. Derivative West Germanic *brigdil-, bridle (referring to the movements of a horse’s head), in: a. Old English bridel, bridle: BRIDLE; b. Middle High German bridel, bridle, rein: BRIDE?. 3. Germanic *bréhw6, eyelid, eyelash, in Old Norse bra, eyelash: BRAE. 4. Germanic “breh(w)an, to shine, forming West Germanic *brehsmo, a bream, in Old French bre(s)me, a bream: BREAM!. [Pok. bherak- 141.] bherg-. To buzz, growl. Germanic *berk- in Old English beorcan, to bark: BARK}. [Pok. bhereg- 138.] bhergh-'. To hide, protect. 1. Germanic *bergan in: a.compound *h(w)als-berg-, “‘neck-protector,” gorget (*h(w)alsaz, neck; see k“el-1); b. compound *skér-berg-, “sword-protector,” scabbard (*skér-, sword; see sker-'). 2. Zero-grade form *bhrgh- in: a. Germanic *burgjan in Old English byrgan, to bury: BURY; b. Germanic deriva- tive *burgisli- in Old English byrgels, burial: BURIAL. 3. a. Germanic *borgén, to borrow (? < “to take care of one’s own interests, entrust, pledge, lend, loan”), in Old English borgian, to borrow: BORROW; b. Germanic de- rivative *borganjan in Old French bargaignier, to haggle (> bargaine, haggling): BARGAIN. [Pok. bhergh- 145.] bhergh-?. High; with derivatives referring to hills and hill-forts. 1. Germanic *bergaz, hill, mountain, in: a. Old English beorg, hill: BARROW?; b. Old Norse berg (> Danish and Norwegian berg), mountain: ICEBERG. 2. Compound *harja-bergaz, “army-hill,” hill-fort (*har- jaz, army; see koro-). 3. Compound *berg-frij-, “high place of safety,” tower (*frij-, peace, safety; see pri-), in Old French berfrei, tower: BELFRY. 4. Zero-grade form *bhrgh- in Germanic *burgs, hill-fort, in: a. Old English burg, burh, byrig, (fortified) town: BOROUGH, BURG; b. Old High German burg, fortress: BURGHER; Cc. Middle Dutch burch, town: BURGOMASTER; d. Late Latin bur- gus, fortified place (> burgensis, city dweller): BOURG, (BOURGEOIS), BURGESS, BURGLAR; FAUBOURG. 5. Suf- fixed zero-grade form *bhrgh-to- possibly in Latin fortis, strong (but this is also possibly from dher-?): FORCE, FORT, FORTALICE, FORTE!, FORTE?, FORTIS, (FORTISSIMO), FORTITUDE, FORTRESS; COMFORT, DEFORCE, EFFORT, ENFORCE, FORTIFY, (PIANOFORTE), REINFORCE. [Pok. bheregh- 140.] bhers-. Quick. Latin festindre (< *fers-ti-), to hasten: FESTINATE. [Pok. bheres- 143.] bhes-', To rub. 1. Zero-grade form with unclear suffix *(bh)s-amadho-, sand (in Greek psamathos), in Germanic *sam(a)dam, *sandam in Old English sand, sand: SAND. 2. Suffixed form *(bh)s-abh- in the further suffixed form *sabh-lo- in Latin sabulum, coarse sand: SABULOUS. 3. Suffixed form *bhs-d- in (i) Greek psén, to rub, scrape: PALIMPSEST (ii) Greek pséphos, ballot, pebble: PSEPHOLO- GY. 4, Perhaps suffixed form *bhs-ilo- in Greek psilos, smooth, simple: EPSILON, PSILOMELANE, UPSILON. [Pok. bhes- 145.] bhes-2. To breathe. Probably imitative. Zero-grade form *bhs- in Greek psukhein (< *bhs-il-kh-), to breathe, hence psukhé, spirit, soul: PSYCHE, PSYCHIC, PSYCHO-; METEMPSYCHOSIS. [Pok. 2. bhes- 146.] bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan (*for, before; see per') in: a. Old English béodan, to proclaim: BID; b. Old English forbéodan, to forbid: FORBID; ¢. Old High German farbiotan, to forbid: VERBOTEN, @: Germanic *tudén- in Old English boda, messenger, hence bodian, to announce: BODE!. 3. Ger- manic *budilaz, herald, in Old English bydel, herald, messenger: BEADLE. 4, Germanic *budam in Old Norse bodh, command: OMBUDSMAN. 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE. [Pok. bheudh- 150.]
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
434:el-1. Elbow, forearm. Extended o-grade form *olind, elbow, in: a. Germanic “alind in Old English ein, fore- arm, cubit: ELL?; b. Germanic compound *alino-bugén-, “bend of the forearm,” elbow (*bugén-, bend, bow; see bheug-’), in Old English elnboga, elbow: ELBOW; c. Lat- in ulna, forearm: ULNA; d. lengthened variant form *6lena in Greek dlené, elbow: OLECRANON, [Pok. 8. el- 307.]
1253:APO- apo- APOCALYPSE kel-2 APOCOPE skep- APOCRINE krei- APOCRYPHA krau- APODAL ped-! APODICTIC deik- APODOSIS do- APOGEE gé APOLOGUE leg-1 APOLOGY leg-! APOMIXIS meik- APONEUROSIS (s)neau- APOPHYGE bheug-! APOPLEXY plak-2 APOSIOPESIS sWi- APOSTASY sta- APOSTLE stel- APOSTROPHE! streb(h)- APOTHECARY dhé-1 APOTHECIUM dhé-1 APOTHEOSIS dhés- APOTROPAIC trep-2 APPALL pel-2 APPANAGE pa- APPARATUS pere-1 APPAREL pere-! APPEAL pel-6 APPEASE pag- APPEND (s)pen- APPENDIX (S)pen- APPETITE pet- APPLE abel- APPLY plek- APPOGGIATURA ped-1 APPOSITE apo- APPOSITION apo- APPRAISE per-6 APPRECIATE per-6 APPREHEND ghend- APPRENTICE ghend- APPRESSED per-5 APPRISE ghend- APPROACH per! APPROPRIATE pert APPROVE per! APPROXIMATE per! APRICOT pekw- APRON mappa APT ap-!
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1280:BE- ambhi BEACON bha-1 BEAD gWhedh- BEADLE bheudh- BEAM bheue- BEAN bha-bha- BEAR! bher-1 BEAR? bher-3 BEARD bhardha BEAT bhau- BEATIFIC deu-2, dhé-1 BEATIFY deu-2 BEATITUDE deu-2 BEAU deu-2 BEAUTY deu-2 BEAVER! bher-3 BECHE-DE-MER mori- BECK? bheg¥- BECKON bha-! BECOME gWa- BED bhedh-
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1296:BID bheudh-, ghedh- BIDE bheidh- BIDENTATE dent- BIDONVILLE weik-1 BIENNIUM at-
1297:BIER bher-1 BIFORATE bher-2 BIGEMINAL yem- BIGHT bheug-3
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1310:BOG bheug-3 BOIL! beu-!
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1318:BOUTIQUE dhé-1 BOUTON bhau- BOVINE g¥ou- Bow? bheug-3 Bows bheug-3 BOWEL gW¥et-3 BOWERY bheue- BOWER! bheue- BOWL! bhel-2 BOWL? beu-1 BOWSPRIT sper-4 BOX! puxos
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1326:BUSTARD awi- BUSTLE s(w)e- BUT ud- BUTCHER bhugo- BUTT! bhau- BUTTER gWou-, teue- BUTTOCK bhau- BUTTON bhau- BUTTRESS bhau- BUTYRIC g¥ou- BUXOM bheug-3 BUZZARD beu-2 BY! ambhi BYRE bheue-
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1503:FATE bha-2 FATHER peter- FATHOM pete- FATIDIC deik- FAUBOURG bhergh-?, dhwer- FAVA BEAN bha-bha- FAVOR ghow-é- FAVORITE ghow-é- FAWN! pek-t FAWN? dhé(i)- FAY} pag- FEALTY bheidh- FEAR per-4 FEASIBLE dhé-1 FEasT dhés- FEAT! dhé-1 FEATHER pet- FEATURE dhé-1 FEBRIFUGE bheug-! FECUND dh@(i)- FEDERAL bheidh- FEDERATE bheidh- FEE peku- FEEBLE bhlé-1 FEED pa-
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- FETICIDE dhé(i)- FETISH dhé-1 FETLOCK ped-! FETTER ped-1 FETTLE ped-2 FETUS dh@(i)- FEUD! peig-2 FEUD? peku- FEUILLETON bhel-3 FEVERFEW bheug-! FEW pau-
1528:FOR- per’ FORAGE pa- FORAMEN bher-2 FORBEAR bher-1 FORBID bheudh- FORCE bhergh-2
```


## [2026-09-05T14:11:30.678Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON 476 ===\"; grep -n \"بخت\" MON_part1.txt | head -20; echo; grep -c \"\" MON_part1.txt"
}
```


### [2026-09-05T14:11:30.796Z] TOOL RESULT

```
=== MON 476 ===
2151:کوره پخته باشنده خشت بخته. 
3407:آماده کردن آش. آش بختن برای کسی: 
3413:23-2 (افا.) آنکه شغلش بختن طعام 
4151:آگور: ۲اع [- [- آجر](.) خشت بخته» آجر, 
4559:(مصل.) (البخت» آلیز د» خواهد آلیخت. 
4887:4 نی «آمبخته»: حسرت آمیزه 
5177:نشان . گر بخته. برا کنده» بر شان» متفرق. (.) 
5440:جذب کنندهٌ رطوبت و آن از بخته شدن 
5709:منعکس سازد؛ مرآت. آیینةٌ بخت. آیینه‌ای 
7265:بختن استفاده می‌ کنند. اجاق خانواده: کانون 
7815:کردن. (اسص.) دوراندیشی» بختگی؛ 
8288:نجم. ستارةٌ بخت و اقبال» ستار؛ٌ مسلط بر 
8290:بد» بخت بد. اختر دانش: (کن.) الف: 
8294:ماه. اختر نیکك: بخت نیکك. اختر سعد فال 
8295:نیکك. نیکک‌بختی» نیک‌روزی, اقبال» حسن 
8357:ایل‌های کرمانشاه «بخترمه» نیز گویند.) (.) 
8517:گردنکشی, تبختر 
8929:نگون‌بختی» سیه‌روزی» بی‌دولتی» بدبختی. 
8930:(ص.) نگسون‌بخت» مسدبر» سیه‌روز. (در 
8938:ناپاکی. کئیفی. بدبختی» نگون‌بختی 

99339
```


## [2026-09-05T14:11:46.158Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('MON_part1.txt',encoding='utf-8',errors='replace').read()\nprint('formfeeds',t.count('\\f'))\nprint('pdf page tags', t.count('[pdf page'))\nprint(len(t))\nEOF\ngrep -n \"بخت ۲\\|بُخت\" MON_part1.txt | head -10"
}
```


### [2026-09-05T14:11:47.913Z] TOOL RESULT

```
formfeeds 0
pdf page tags 0
2611770
```


## [2026-09-05T14:11:53.578Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"بوختن\\|bōxtan\\|boxtan\\|bôxtan\" MON_part1.txt MON_part2.txt | head -10\necho \"--- pozes ---\"\ngrep -n \"پوزش\" MON_part1.txt | head -10\necho \"--- ARY ---\"\ngrep -n \"بیوس\\|پوزش\\|بوستان\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-05T14:11:53.656Z] TOOL RESULT

```
MON_part1.txt:11112:اس‌پوختن: 27 [- سبوختن - 
--- pozes ---
12123:استغفرالله گفتن. (امص.) پوزش. 
14272:اعستذار: 5 ([ع.] (مسصل.) پوزش 
14273:گرفتن» پوزش خواستن» عذر خواستن. 
14274:شکایت کردن. (اسص.) پوزش) ج. 
14436:عذ رخواستن. (امص.) پوزش» عدر. 
29773:کردن» اجابت کردن. پذیرفتن پوزش: 
33174:پوزش پدیر: ۲۳:21 [- پوزش پذ یر نده] 
33188:بوزیده. پوزش) زدودن» راندن» برطرف 
95299:پوزش. قاعدگی (زن). (.) بهانه؛ ج. اعذار. 
95340:(مصل.) عذر خواستن از کسی: پوزش 
--- ARY ---
4489:فارسی (2885]4۸): پالیز, فالیز, جالیز, پردیس (به چم "باغ" ابوستان)
```


## [2026-09-05T14:11:56.022Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '33165,33200p' MON_part1.txt"
}
```


### [2026-09-05T14:11:56.073Z] TOOL RESULT

```
پسسوزخند: ۳.27٩‏ [- پبوزه‌خند - 
پوزخنده» از «پوست خنده؟, خندیدن 
(بوست)] (امر.) لبخندی که به قصد انکاره 
تحقیر با استهزا زنند؛ بورحند» پوره‌خند. 
۱ ۳ ۰ ۰ 

پسسورشس: ۲02-5 (امص. پوزیدن) 
عذرخواهی» معذرت‌خواهی» درحواست 
عفو . عذر» معذرت. 
پوزش پدیر: ۲۳:21 [- پوزش پذ یر نده] 
(ص‌فا.) کسی که عذر کناهکار را قول کند 
و از او درگذرد؛ عذر بد بر . 

۰ ی ۰ ۰ _ 
پورس خواستن: ۳.1 (مسص‌ل.) 
طلبیدن. 
پوزمالی: [-۳2-۱21 (حامص.) مالیدن بوز 
(چنانکه سک به پای صاحب خود.) (کن.) 
تنییه کسی به وسیله دشنام» کتکث یا جر یمه. 
پوزه: (0-)ع۳م [- پوز] (.) پیرامون دهان» 
گرداگرد دهن حبوانات. جانه. 
پوریدد. ۳۱2-0 آفس. بورس ] (مص‌ل.) 
(بوزبد» بوزد» خواهد بوزید» سوزه بوزنده» 
بوزیده. پوزش) زدودن» راندن» برطرف 


کردن(۲). معذرت خواستن» عذر خواستن. 
پوساندن: 19-1( [- بوسانیدن] 
سوسان» بو ساننده» بوسان» بوسانده). 
یوسانیدن: مج موه عنام [- بوساندن| 
پسوسانید» بسپوسان» پوساننده» پوسان» 
بوسانیده). سوسیدن داشتن» بوسیده کردن» 
تغییر دادن صورت چیزی اعم از تر و 
خشکک با گذرانیدن زمان بر او با به حیله‌ای. 
هت کفن بوسانیده: دیری است که مرده. 
مدتی بر او گذشته.
```


## [2026-09-05T14:12:05.872Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T14:12:05.879Z] TOOL RESULT

```


```


## [2026-09-05T14:12:09.500Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%DB%8C",
 "prompt": "Give the Persian etymology section for بوی (bōy) verbatim: Middle Persian form, Proto-Iranian, PIE root, cognates. Also any mention of بوستان."
}
```


## [2026-09-05T14:12:11.156Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B3%D8%AA%D8%A7%D9%86",
 "prompt": "Give the Persian etymology of بوستان (bōstān / būstān) verbatim: compound analysis, Middle Persian form, meaning."
}
```


### [2026-09-05T14:12:15.409Z] TOOL RESULT

```
# Persian Etymology for بوی

Based on the Wiktionary content provided, here is the Persian etymology section:

**Middle Persian Form:** 𐫁𐫇𐫏 (bwy /bōy/, "smell, scent; incense")

**Etymology Statement:** The word is "inherited from Middle Persian" with a noted relationship to "Old Armenian բոյր (boyr), an Iranian borrowing."

**Key Information:**
- The entry does not mention Proto-Iranian or Proto-Indo-European roots
- No cognates beyond the Armenian connection are listed
- There is no mention of بوستان (Boustān) anywhere in this dictionary entry

The etymological path shown traces the Persian word back to Middle Persian, but does not extend further into deeper linguistic ancestries as your question suggests might be documented.
```


### [2026-09-05T14:12:16.955Z] TOOL RESULT

```
# Persian Etymology of بوستان

**Compound Analysis:**
"By surface analysis, _[بو](/wiki/%D8%A8%D9%88#Persian "بو")_ (bô, "fragrance") +‎ _[ـسْتان](/wiki/%D9%80%D8%B3%D8%AA%D8%A7%D9%86#Persian "ـستان")_ (-stân, "place of")."

**Middle Persian Form:**
The word derives from Middle Persian forms including _bwdstʾn'_ and _bwyystʾn_ (meaning "flower garden").

**Overall Meaning:**
The term literally translates to a location associated with fragrance or aroma, combining the root for "scent" with a suffix denoting "place of."
```


## [2026-09-05T14:12:21.553Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ewd%CA%B0-",
 "prompt": "Give the reconstruction, meaning, and the list of derived terms/descendants (Indo-Iranian, Germanic, Greek, Balto-Slavic) verbatim."
}
```


## [2026-09-05T14:12:23.152Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B2%D8%B4",
 "prompt": "Give the Persian etymology of پوزش (pôzeš / pōzeš) verbatim: Middle Persian form, root, meaning. Also anything about پوزیدن."
}
```


### [2026-09-05T14:12:27.966Z] TOOL RESULT

```
# Proto-Indo-European Root: bʰewdʰ-

**Reconstruction:** *bʰewdʰ-

**Meaning:** "to be awake, be aware"

**Derived Terms and Descendants:**

**Indo-Iranian:**
- Sanskrit: búdhyate, búddhi, búdha
- Avestan forms: būiδiiaēta, busti, baoda

**Germanic:**
- Proto-Germanic: *beudaz, *budą

**Greek:**
- Ancient Greek: punthánomai, pŭ́stĭs

**Balto-Slavic:**
- Latvian: bust
- Lithuanian: bùsti
- Proto-Balto-Slavic: *budḗˀtei

Additional descendants appear in Celtic languages (Welsh rhybudd, bodd; Cornish both; Old Irish robud) and Tocharian forms (pot-, paut-).
```


### [2026-09-05T14:12:28.542Z] TOOL RESULT

```
# Persian Etymology of پوزش

Based on the Wiktionary entry, here is the etymological information:

**Middle Persian Form:** The entry indicates the word derives from Middle Persian (bōzišn, "salvation; apology"), which itself is "a verbal noun of Middle Persian" with the root form bwhtn' or bwc- /bōxtan, bōz-/.

**Root Meaning:** The Middle Persian root means "to save, to redeem," ultimately tracing to the Proto-Indo-European "*bʰewg-" meaning "to flee, to escape."

**Note on پوزیدن:** The webpage does not contain any information about پوزیدن (the verb form). Only the noun پوزش is documented in this entry, with derived terms including the phrase "پوزش خواستن" (puzeš xâstan, "to apologize").
```


## [2026-09-05T14:12:34.888Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%88%D8%B3%DB%8C%D8%AF%D9%86",
 "prompt": "Give the Persian etymology and meaning of بیوسیدن verbatim, if the page exists. Also any related بیوس entry."
}
```


## [2026-09-05T14:12:35.955Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Buddha",
 "prompt": "Give the etymology of Buddha verbatim, including Sanskrit forms and the PIE root cited. Also mention what it says about bodhati."
}
```


### [2026-09-05T14:12:36.735Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T14:12:40.858Z] TOOL RESULT

```
# Etymology of Buddha

According to the Online Etymology Dictionary, the word "Buddha" comes from Pali, literally meaning "awakened, enlightened," as the past participle of *budh* "to awake, know, perceive."

The Sanskrit connection is explained as follows: the Pali root is "related to Sanskrit *bodhati* 'is awake, observes, understands,'" which traces back to the Proto-Indo-European root *bheudh- meaning "be aware, make aware."

The entry notes that this title was given by adherents to Siddhartha Gautama (also called Sakyamuni, "Sage of the Sakyas"), who lived in northern India around the 5th century B.C.E. The term entered English usage in the 1680s.
```


## [2026-09-05T14:12:50.404Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/bid",
 "prompt": "Give the etymology of \"bid\" verbatim: the merger of Old English biddan and beodan, and the PIE roots cited for each."
}
```


## [2026-09-05T14:12:51.120Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/fugitive",
 "prompt": "Give the etymology of fugitive verbatim: Latin fugitivus, fugere, and the PIE root cited (bheug-). Also mention refuge and centrifugal if present."
}
```


### [2026-09-05T14:12:56.315Z] TOOL RESULT

```
# Etymology of "Bid"

The word "bid" stems from two Old English verbs that merged:

**Old English _biddan_** ("to ask, entreat, beg, pray, beseech; order") traces back to Proto-Germanic *bedjanan, deriving from the PIE root **_*gwhedh-_** meaning "to ask, pray."

**Old English _beodan_** ("offer, proclaim") comes from Proto-Germanic *beudanan ("to stretch out, reach out, offer, present"), which derives from the PIE root **_*bheudh-_** meaning "be aware, make aware."

According to the source, this represented "probably an early Middle English mutual influence or confusion of two older words," with the first sense relating to farewells and requests, and the second sense relating to auction bidding.
```


### [2026-09-05T14:12:57.623Z] TOOL RESULT

```
# Etymology of Fugitive

**Latin Origins:**
The word derives from Latin *fugitivus*, described as "fleeing," which is the past-participle adjective from the stem of *fugere* meaning "to flee, fly, take flight, run away."

**Proto-Indo-European Root:**
The ultimate source is the PIE root *\*bheug-*, which means "to flee" and also appears in Greek *pheugein* and Lithuanian *būgti*.

**Related Terms:**

*Refuge* traces back through Old French *refuge* to Latin *refugium*, literally "a place of refuge, place to flee back to," combining *re-* (back) with *fugere*.

*Centrifugal* was coined by Isaac Newton, combining Latin *centri-* (center) with *fugere* to describe something "flying off or proceeding out from a center."

The adjective sense emerged in the late 14c. as "fleeing, having fled," while the noun form (late 14c.) refers to "one who flees, a runaway." By around 1500, it acquired the figurative meaning "lasting but a short time, fleeting."
```


## [2026-09-05T14:13:07.492Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '13345,13360p' BRT.txt\necho \"======\"\nsed -n '16495,16560p' BRT.txt"
}
```


### [2026-09-05T14:13:07.551Z] TOOL RESULT

```
•  j.  dÜtyö.pid'wa-  i)  n.  'gehörige  Mahl- zeit": *aiva  hl  "'iwitn  "so  ist  seine  ge- hörige Mahlzeit"  V.  tj.  28.  2)  Adj. 'mit  der  gehörigen  Mahlzeit  versehen' (nur  Komp.).
vKompA.  —  Pu.:  dälihä  pihn,
•  j.  däityö.piO'wi.-bav-  kompV,  'der gehörigen    Mahlzeiten   teilhaftig   werden':
'buyh  .  .  ätars  pu-ira   ahurahe  Y.  62.  2 "'.
vKomp.:  'pi%un- Adj. +dav i  $  ^ÖJ.  —  Pü. : dätlhä  pihn  (Sü.:  b/iafanam)  iave.  —  i)  S.  iSt. unter  ^ri.pi%7iia-.
•  j.  däityö.baoiay-  Adj,  (auch  fem.)  'die gehörigen  Räuchermittel  habend,  daraus bestehend':  aäiim  baoiolm  '6aoiöyff{AP{.y* N.  103.  I
vKonipA.  —  Pü, :  fehlt,  —  0  Auf  kollelcL  AS. , bezogen?     S,  aesma-  No.   1.  |
•  j.  däityö.baoi3i.-bav-  kompV.  'der  ge- hörigen Räuchermittel  teilhaftig  werden': °buyS  ..  äiars  pui:ra  ahurahe  Y.  6'2.  2.
Komp.;  'baoiay-  Adj.  -^iav-;  %  26^.  —  PQ. : liälihä  iöJ  biH't.
•  j.  dädaray-  Adj.  'der  etwas  (Akk.)  be- sitzt': yai  asp>r?nB  vastrahe  . .  'rayS  (NP,) a  anaiwySsH  strmti  yezi  sat  nSit  asp?r}rw vastrahe  .  .  'rayS  nSit  ^anaiwyästt  "wenn  1 sie  ein  vollständiges  Kleid  . .  besitzen,  so versündigen  sie  sich,  wenn  sie  es  nicht! anziehen;  .  ."  N.  96".  1
Zum  V.  3dar-,  mit  Int.-Ked.  gebildet;  ar  bt ! «.  ar  oder  /■-■;  s.  daiu  WH.  Gr.»  S  "SS  «■  -  | Pü. !  iaiar  . .  därriid.  j
•  p.  dädariay-  m.  EN.  zweier  Heerführer  ! Dariuil.,  i)  eines  Persers,  Satrapen  von' Baktrien:  -/iV  mlm<^  pärs^  .  .  bäxtriyä X5a'h''api!vä  Eh.  J.  3;  3.  2)  eines  Ar- j meniers:  'jY/  näme^  armimyc^  tnanä  ba"-  \ äake^  Bh.  2.  J;  7,  9;  —  palis  -sim  Bh. ' 2.  7,  8,  9.
Eig.  'kühn';  zum  V.  dars-,  mit  Inl.-Red.  —  ai. dädhnay  Adj.  -kühn'.  |
•  p.   däduhya-   m.  EN.   eines  Persers:
bagabuxsa''  ndma'  °hyahyä  pti^'^J' pärsa''
Bh.<^.  r8.
======
•  j.  baeSatastura-  patr.  Adj.  'von  BaSsata- stura'-'>  abstammend,  dessen  Nachkomme': fratura  asntta  'rä  (GS.)  asaomJYt.  13.12$.
Ableit  (mit  Verschiebung  des  Wortakzents) aus  *baFiata'ilura-')  a>.  EN.  (Bed,?  *baeJoia- vU.  PFP.,  s.  bii-  und  *mtmataseura-).  —  >)  S. aber  No.  2.  —  »)  Oder  aber  aus  *iiSo/os/ura; zn  S  /00  a.  B?
•  j.  bae^aza-  1)  Adj.  (fem.  'sr-)  'heilend, heilkräftig,  heiltätig';  a)  von  Mond  imd Sternen:  mawi^m  ..  bay>m  'Km  Yt". 5;  —  vanantim  stär>m  .  .  °wm  Yt  21. 1.  b)  sonst:  als3  , ,  asti  °zanqm  bag- sai:yS.t)mö  yat  *mq%r?m.sp>nt»m.batiasyB V.7.44;  zitYtj.6;  —  mq^ranqm  'am .  .  bal^atyBJimim  Yt  J.  S;  —  vaca  ars- uxoa    van'hrayms    'zis    (APf?)   YtJÄS;
dby  Google
915
baesaza.kai-
baog-
916
8,  3)  n.,  m.'';  a)  'Heil-,  Gesundheits- mittel,  Arzenei':  avaüa  he  't?m  upsisay?n ya%a  dahmaUi^  "in  einem  solchen  Fall sollen  sie  ein  Heilmittel  für  ihn  ausfindig 2U  machen  suchen,  wie  für  einen  D."  V. y-  3S;  —  ^  '^  (näml.  haomahe)  Sa  (NP.) irlra'i arf  {sd.) ..  Y.io.  12;  —  haoma  dasdi ml  'zanqm  yäbyS  ahi  baisazma  (sd.)  V. 10.  9;  6t<.  15',  Yt  13.  13s;  —  aslm  .  . baryntlm  vupä  "sä  (AP.)  apqmca  gavamla ttrvaranamca  ". .  alle  Heilmittet  der  Wasser, Tiere  und  Pflanzen"  Y,  52.2;  —  nava  'za (NP.)  V,  2/.  3 ;  —  fravaiayö  .  .  a^is  -za (AP.)  hanmni  Y.  60.  4;  Vr.  <?.  i',  2,  F.  16,
dämqn  baisasyatica  Yt.Ä43;  —  Bat  mqm tarn  *baghsyöii'i  V.  22,  2,  9;  —  baliazySi Yt.j.63). Ableit.  aus  batsata- ').  —  Vgl.  biiat'-  —   Pü. : bisaxitiitan.  —  >)  Es  ist  nicht  unmöglich,  dus baeiaxya-    aus   ar.  'Miiasiu-   (•=  ai.  bhifejya-) unter  demEiofluss  von/df/iizii-hGrvoTgegaiigeD ist;  vgl.  tisas-  No.  i.  —  *>  So  K  1,  L4;  NA. &j".  —  3)  Vgl.  bHas-  No.  *. •  j.  'baeäazya-  Adj.  (fem.  °sya-)  Tieilend, heilkräftig,  heiltätig';  a)  von  Göttern,  Ster- nen, Wassern,  Pflanzen  udgl.:    °zya  (statt NSm.)  ftqma  ahmt  (näml.  AkM.)  . .  bae- sasyü.t>ma  Yt  j.  1 2 ;  8 ;  —  kaomS  .  .  'zyJ Y.p.i6,  57.19; —  haomahe  'zyehe  '^.10.
YtÄfio.       o)iiberhaupt'Hilfsmittel,Hitter:j  7;    —  fravalay5  'zyä  YLij.30,  3a;
(1/  (Sp.  423  u.)  aii^he  asti  'zö  "was  gibls da  für  ein  Mittel?"  Yt/4.34.  b)  'Heil- kraft': 'sa  (IS.)  ahmt  balsazySJfms  Yt.  14. 3.  c)  'Heiltum';  barat  (näml.  väts)  -am Uta  amtm^a  Yt  14. 2 ;  Fr.  g.i.  a)  insbes. in  Verbindung  mit  dasvar-  (Stverz.):  dasva- rna   'z>mca  (NS.)  V,  p.  53;  usw.  -ziii
als  Inf.  sbes.  [V.  7. 44:  lies  mäimm.- sp}nt}m  .balsaam.]
KompA.,  E.;  Ableit.  —  lEt  s.  bisas-.  —  aL bhtfajä-  1)  Adj.,  2)  n.i  »p.  bisazali;  rp.  vgl biäli  'Aril'.  —  Pa.i  btiaziin,  bSatimih,  iiia- zinUniA.  —  0  Sicher  Yt.  T4.  34.
•  j.  baeSaza.ksä'  Adj.  'Heilung  bewirkend, schaffend':  nava  bai^asä  navata  'ktsa (NPn.)  ■>  "(wieder)  frisch  (werden)  die  Ar- zeneien,  frisch  die  Heilung  schaffenden (Mittel)"  V.2J.3.
'ti's-  Adj.  ■niacbcnd',  tarn  V.  ^kar—,  ai.  *kfi- Adj.;  S  '7'-  —  Pö-:  bisasiitük  iarlärih,  erL : auisär.  —  ')  Them.
•  j.  bae§aza-3ä-  Adj.  'Heilung  schaffend': datdi  ml  bal^azanam  yäbyd  ahi  '\h  (NS.) "gib  mir  von  den  Arzeneien,  durch  die du  Heilung  schaffst"  V.  10. 9.
Pü. :  beiatimlär.
•  j.  baeSazai  Inf.  'zu  heilen':  frä  äbys tanubyS     haomS     vuaite   (sd.)    b'    Y.  j
as[m  . .  'syqm  Yt  ij.i;  —  drväspqt
°syqm  Yt  p.  2 ;    —    arfdvTin  .  .  'syqm  Y.
(5j.  I ;  —  HiirTm  .  .  'Um  Yt.  S.a;—  stärd
ySi  haptSiritiga  . .  'tya  S.  r.  13;  2,  13;  —
äpö  .  .  'zya  YtA47;  —  urvarä  'zyi  V.
10. 4.         b)  sonst:  vS^5  . .  pailiMsis{%A.)
'zya  Y. 10.18;  Ytr5.s6,  V./0.5;  —  v<^^e
\ySi  . .  'zya  as  Yt/4.40;  —  växl .  .  'zyS
FrW.5. 1;    —    %rimahe  ..   'tyehe   Yt /5.
so;  — gavafttlm^a  °>yqm  Yt  10. 15.       [V.
7.  44:  lies  mq%r3m.sp3nt3m.baiiazys\
KompE.;  Ableit.   —    Ableit.  aus  bariaia-.  —
ai.  bh4iajyä-   Adj.    —    Pü. :    beiaiiitüSr,    So. :
arogyaiarah.
•  j.  ^aeiazyäi')  Inf.  'zu  heilen,  Heilung zu  bringen':  äia  tiB  jamyät  b'  Yt/0.  5,
Zum  Praes.  31  iaelatya-.  —  <)  So  alle  guten Hds.  (Bthl.  BB.  /j.  22S)  gegen  'läS  der  NA.
•  j.  baeSazyö.tara-  Adj.  (fem.  'rä-)  'der heiltätigere':  fravasayS  .  .  yä  "ri  (NPC) ahmät..yaha  vaca  framraväire  [sd.)  Yt 13.  64.
Kompar.  aus  batsasya-.
•  j.  baeäazyö.tuma-  Adj.  'der  heilkräftigste,
heiltätigste';    a)  von  Göttern:  balsazya  . .
°ma  (statt  NS.)  nqma  ahmt  (jäsaL  AhM.)
Vt;.  12;    —    ial/aza   ahmt  (nämL  Vtr^
rayrta)  'mS  Yt  14. 3-         b)  sonst:    aii3
a)  'die  Heilkunst  zu  betreiben':  j'ai'lzr  aiii  ba^azanqm  'mS  yai  *mq%t7m.- ..mazdayasna  b' fravazante  katärS paurvS  tp^nismMHazyB  Y.y.  44;  Yt 3.  6;  —  ma- ämay^n/e  (sd.)  "wenn  die  J/.  sich  der  Heil-  ^ranam  balsasm  ..  'mtm  Ytj.5;  t.2, kunst  widmen  wollen  .  ."  V.7.36.  [Yt  ^-  —  ima  vaSs  ..ySi  atihm  värfkra^t^S.- 10.1'.  lies  baisazyäi:\  t>mim^a\sA)  'mtmcä  V.g.sj.
Vgl  *baHaiyäi    und  AiSaai..    —    Pü.  (dRn.):        SuperL  aus  ÄiSaya-.  —    Pü.;    itlaiMtärOim. itsazeniinU,  pa  bizaSm.  (m  Yt.  7)  erL;    mart  kaS  guß  islll  (*«)  tär  u
•  j.  TjaeSazya-"    den.  Praes.  31  "heilen*.         dälastSn  i  v?h  dSaed  bHas^nUan.
—  InC  *baisazyäi.  •  j.  baog-  V.  'lösen'.     Praes.  3  bBja-",
'heilen,    kuriren,    ärztlich    behandeln':   9   bunja-,    24  büjaya-,    94-24   bunjaya-, tiftrfm  .  .  yd  . .    naSnizaitt  .  .    vuphs}  tä    27  bß)ya-^'>.
dby  Google
917
baog-
i)  '(den  Gürtel)  lösen  sva.  ablegen': yasca  . .  aiwyänhantvt  vä  aiwyäahayamnö aiwyatfhatum  vd  ds/ayamn^  "..deaGüi- telan-  oder.. ablegend"  Yt  7,17.  a)'be- freien,  retten':  vä^ yäi ^^S^mat(Sp.Bg8  o.) särvm  bunjainti  Yt.  7^46;  —  masyS  an- ÄJM  (sd.)  yat  u^tänim  bunjayäi  ", .  dass  sie ihre  Lebenskraft  rette"  V,  7. 7 1 .  a)  Vor  — ' (haca  mit  Akk. !):  tä  büjat  . .  narsm  haca nasüm  Yt  4.  3.  a)  'sich  retten  vor  — '
{hai'a  mit  AbL):  astS.vi}>Stus  .  .  yakmat haca  nailis  bunjayät  .  .  mafyänqm  nsit afiirapatays ..  "Ä.  ..,  vor  dem  sich  keiner retten  kann  . ."  Aog.57f.  3)  (angebl.) 'anlegen',  den  Gürtel^:  tairyS  aiwyärfhanS (sd.)  bBjyaman5  Vd. /2.
mit  ava  (angebl.)  'anlegen',  den  GürteU' : aiwyäakanS  ava  hi  maSiyätum  büjya- mans  Vd.20.
mit  avi  'retten':  avi  he  urvänam  büj- yän»m  Vd.  17.
mit  paiiil  (angebl.)  'anlegen',  den  Gür- tel3>:  aiwyätiMnS  pailil  kl  mailyäi  bü- JyamanS  Vd./Ä
mp.  iäx/an,  sbal.  böj^;  s.  Hbm.  IFAni.  6.  34, AGr,  /.  111,  Osthoff  IF.  S-  *94-  —  P5-- Kxlan,  ieSmtati,  eri.  (zu  Vt,  l) :  vüäian ;  Npü. (inVt./^):  xaläsJ dädan  [ai  eang i mardumän); ».  noch  No,  3.  "—  OYl.  4!  —  J)  Vd, !  — 1)  Der  Verfertiger  des  Stücks  hat  YL  /.  17 benutzt,  dabei  aber  die  Verba  Terwechsell; s.     West     SBE.  j/.  475   No.  i,    BTHL.    EF.
II.    IS?.
j.  baoipm  Yt  14.  57:  lies  säiriM'.
•  j.  baoxtar-  m. 'Retter,  Befreier':  nairyqm Äam.vamllm  . .  yä  narqm  vJg>r)ptä{^^nt tanvS  °tänm  äa}>aili  Vr.  7.  3.
Zum  V.  iaoff:  —  mp.  iöxlür').  —  Pü.:  *m- iaiii.  —  I)  SWienAW.  6/.  840.  24  erklärt: ämurziär  u  rahämdar,
•  j.,  g.  baod-  'sentire'.  Praes.  2  ba<k baoda-,  sj  bÜilya-,  3o(Kau5.)  bao^aya-. PPfP.  'busta-'K
i)  'sentire,  wahrnehmen,  gewahr,  inne werden':  paurva  täyüm  .  .  bBtiySimatiie mä  äs  paurvö  baioyaita  nS  vlspe  paurva büi'tySimaihe  "zuerst  möchten  wir  des  Diebs gewahr  werden  ,  ."  Y.  ^.  21;  —  a'ira pas^aSa  vaosirim  (sd.)  baoi>ntS  lufDirt tarmmSa  "..  sentientes  famem  sitimque" Yt.  if).  69;  69;  ~  baelff  (NS.)  vlöwS aiihtiiä  (sd.)  V.76'67.  a)  Kaus.  'zu  er- kennen geben':  haemö..yakmäi  kvar>  därät tamö  baoöayeiti  Yt  10.  90.  2)  'riechen
baodaya-  918
nach  — '  (Akk.):   Aubaoiiis  (sd.)   baöhaite
nmUtum  yeiiAe  .  .  Yt.  77.  6.
mit  upa  'riechen,  Geruch  an  sich  haben':
```


## [2026-09-05T14:13:15.149Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Wohlgeruch\" BRT.txt | head -10\necho \"---\"\ngrep -n \"paiti.busti\\|paitibusti\\|busti-\\|paiti\\.baod\" BRT.txt | head -10"
}
```


### [2026-09-05T14:13:15.209Z] TOOL RESULT

```
30302:Pu.:  Aufit.  —  1)  VgL  ai.  lä/ätä  tubhigi  RV. 5-  56-  9- •  j.hu-bao8ay- 1)  f. 'Wohlgeruch':  •baoilU (AP.)  baöbaite  nmarum  yeAhe  .  .  "nach Wohlgcrüchen  duftet  das  Haus  . ."  Yt  ij, 6.  2)  Adj.  'wohlriechend':  vJ/s..'iM>ioii H.  2.  7;  —  haoma  ..yäha  raöiahe  'baoSiis Y.10.4;  —  ja'ia  .  .  xia^ra  nivänani  . .
---
3527:•  '].  a-paiti.busti  Adv.  "unvermerkt':  yasf tat  .  .  tayuf  vä  v?hrkS  va  ap°  .  .  para.- baraiti  data  V.  y.  10;  40,
28958:—  mibints  ('detractus')  h' .  .damabyS  Y.  8. 6; — aptm  tasa/ii['cTaüXi'^)..zrayaahat  h'.. ^■5-  'S!  — yi  ^P^  utbar^nte  ('efferontur') . .  zrayatshat  h'  Yt.  y.  65;  —  aat  aps  ava.- ^arwi/«  ('afFeruntur')  trayaaAata  h'  vouru- kasät  Yt.  A  47;  —  attavat  apat  h'  niiba- ray>n  ('extrahant')  V.  6',  29;  31,  7.34,  Y. ^5- 6;  —  US  h*  a^bys  nmanalibyö  baraysn ('efferant')  .  .  atrtmca  .  .  V.  5. 40 ;  —  apa HS  h  qzanhat  . .  müra  barüs  ('efferas') Yt.  JO.  23;  23;  —  apa.barani  {'auferam') uva  ^Mmca  tarsnpmca  A'  mazdii  dämabyS Wt.g.  10;  10',  5.26,  tp.32,  93;  —  nsit .. apaitibusti  h'  viisbySpara.baraitiy.l3./^o; 10,  II,  N.j^;  —  yö  atnm  sairchyat  h' daitlm  gatüm  avi  ava.baraiti  Ctransfeif ) V.  S.  83;  84-95";  —  fraourralsaymi ('convertam')  humaya  (sd.)  .  .  hyaonya  h daiiihävs  Yt.5. 31;  —  kii>a  nasul  apa- yasäne  ('depellam'J  h'  *ava^hi^  vTsal  V.
```


## [2026-09-05T14:13:23.528Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC bheudh ===\"; grep -n \"bheudh\\|bheudho\\|bheug\" IEC.txt | head -20\necho \"=== WLD Bd2 bheudh ===\"; grep -n -i \"bheudh\\|b^heudh\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-05T14:13:23.584Z] TOOL RESULT

```
=== IEC bheudh ===
1266:bheudhó ‘prompt, arouse, exhort; be awake’. Cf. bhudh-. WP II, 147 Skt. bódhami; Gk. peüthomai (lit. “be prompted', hence ‘hear of); Go. cf. ana-, faür-biudan; OHG biotan; OE beodan 'de- clare; order": ON bjóða ‘offer’; OFris. biada; OCS bljudo, bljusti ‘guard’
1267:bheudhos ‘offertory, bowl, platter’. Cf. bheudho Phryg. (in Gk.) beüdos “a coloured garment’; Go. biups ‘table’; OE beod ‘table, dish, bowl’; MHG biute ‘kneading-trough’; ON bjóð ‘table, bowl’; OCS bljudü “dish?
1268:bheugo (bhoug-) ‘flee’. WP II, 144
1276:Gk. pheügo; Lat. cf. fügi; W cf. buan (‘soon’, fr. *bheugno-?); O-gd. in Li. baugùs “frighten- ed’; baŭgas ‘fear’, bauginu ‘scare’
1551:bhoudhos ‘awake; awakening’. Cf. bheudhó, bhudh- Skt. bodháh ‘awake, aware; awakening’; Cz. bud, id.
1875:bhudhó, ið “wake, watch, care, notice’. WP II, 147. Cf. bheudh-, bhudhros Skt. búdhye, intr.; cf. budháh (^wise'. LW in Arm. but “watchful'); Av. fra-būiðye; OE bodian; OFris. bodia; MHG boten; ON boóa; OCS büzdo, büdéti ‘keep watch, be awake” (and com. SI.); Li. budüà, and budiù, budeti, id. Nasal-infix in Gk. punthánomai (lit. "am roused': “hear of")
1879:bhugo, ið (1) “bend, turn, flee’. WP II, 144. Cf. bhugho, bheugó Skt. bhujami, pp. bhugnábh; Lat. fugio, ire; Gk. cf. éphugon, aor. ‘I fled, feared”; inf.: phugein; Ir. boghaim “bend, arch'. Ambig. cf. bhugho; MHG bochen ‘defy’ beside bocken ‘be bowed, sink’; OFris. buckia ‘bend, bow’; G (sich) bücken; Norw. bukka; Sw. bocka, id.; Li. cf. bügstu, bügti (“be frightened'. Ambig. cf. bhugho)
13521:priiomos — pro-bheudh-, bhoudh-, bhudh-
13536:pro-bheudh-, bhoudh-, bhudh-. WP II, 147 Skt. pra-bodhami v. tr. ‘wake’; Olr. ro-bud,
16681:som-. The following cpds. arise in the lan- guages as given -bheudh- in Skt. & ON; -bhondh- in Skt. Av. ON; -bhüt- in Skt. E Gmc. (cf. MHG samfte ‘easy, slow, comfortable’: OE séfte "soft -dhét- in Skt. & Li.; -dhrt- in Skt. & Arm., cf. -dhor- in Li. sán-daras, -dara: -eimi in Skt. & (variant) Latv. cf. sa-eju; sa-eima, f.; -dhos, -dha in Skt. Slav & Balt.
=== WLD Bd2 bheudh ===
9525:                                                                                        bheudh-                                                            147
```


## [2026-09-05T14:13:25.004Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN forbid ===\"; grep -n \"^forbid\\|forbid, tr\" KLN_1966.txt | head -5\necho \"=== KLN Buddha ===\"; grep -n \"Buddha\" KLN_1966.txt | head -5\necho \"=== SKT forbid ===\"; grep -n \"^Forbid\\|Forbid,\" SKT.txt | head -5"
}
```


### [2026-09-05T14:13:25.081Z] TOOL RESULT

```
=== KLN forbid ===
=== KLN Buddha ===
4943:bid,  tr.  and  intr.  v.  —  Prob.  a  blend  of  ME.  bid¬ den  (fr.  OE.  biddari),  ‘to  ask’,  and  ME.  beden (fr.  OE.  beodari)  ‘to  announce,  proclaim,  offer’. OE.  biddan  is  rel.  to  ON.  bidja,  OS.  biddjan, OHG.,  MHG.,  G.  bitten,  Goth,  bidjan,  ‘to  ask’, and  to  E.  bead,  and  stands  in  gradational  rela¬ tionship  to  OE.  biedan,  ON.  beida,  OHG.  beiten, Goth,  baidjan,  ‘to  command,  force,  compel’.  All thesewordsderivefr.I.-E.base  *bheidh-,  *bhidh-, ‘to persuade,  compel;  to  trust’,  whence  also  Gk. TTEiHeiv,  ‘to  persuade’,  Trtcmc;  (for  ‘rcth-aru;), ‘faith’,  L.  fidere,  ‘to  trust,  confide  in’,  foedus, ‘compact  treaty’.  Alb.  be  (for  *bhoidhd),  ‘oath’, OSlav.  bJda  (for  *bhoidhd),  ‘need’,  bezdp,  bediti, ‘to  compel,  incite’.  Cp.  bide,  faith,  fidelity,  pis- tology.  —  OE.  beodan  is  rel.  to  ON.  bjoda,  OHG. biotan,  MHG.,  G.  bieten,  ‘to  offer’,  OE.  on- beodan,  OS.  an-biodan,  OHG.  in-biotan,  Goth. ana-biudan,  ‘to  order,  command’,  OE.  forbeo- dan,  Goth,  faur-biudan,  ‘to  forbid’,  fr.  I.-E. base  *bheudh-,  ‘to  offer,  present’,  whence  also OI.  bodhati,  budhyate,  ‘is  awake,  is  watchful,  ob¬ serves,  understands’,  buddhdh,  ‘awakened,  en¬ lightened’,  Gk.  TiEuffeaftai,  7tuvf>dvECT^at,  ‘to learn  by  inquiry’,  OSlav.  bljudp,  bljusti,  ‘to  ob¬ serve’,  buzd<?,  budeti,  ‘to  be  awake’,  buzdp,  bu- diti,  ‘to  awake’,  budru,  ‘watchful’,  Lith.  budeti, ‘to  be  awake’,  Lett,  budrus,  ‘watchful’,  Lith. baudziu,  baiisti,  ‘to  chastise’,  OIr.  buide, ‘contentment,  thanks’,  ro-bud,  *a  warning’.  Cp. beadle,  bode,  forbid,  Buddha.
5414:Bothriocephalus,  n.,  a  genus  of  tapeworms  (zool.) —  ModL.,  lit.  ‘having  heads  resembling  little pits’,  fr.  Gk.  (36Fptov,  ‘a  little  pit’,  and  y.zyo'/f, ‘head’.  See  next  word  and  cephalic, bothrium,  n.,  a  sucker  (esp.  on  the  head  of  a  tape¬ worm;  zool.)  —  ModL.,  fr.  Gk.  (36fipiov,  ‘a little  pit’,  dimin.  of  po-Dpo;,  ‘pit,  ditch,  trench’, which  is  prob.  cogn.  with  h.fodere/to  dig fossa, ‘ditch’.  See  bed  and  cp.  fosse.  Cp.  also  the  sec¬ ond  element  in  Cyclobothra. bothy,  n.,  a  hut.  —  Of  Celtic  origin.  Cp.  Olr. both,  ‘hut’,  and  see  booth, botone,  botony,  adj.,  having  a  trefoil  at  the  end (her.)  —  F.  boutonne,  pp.  of  boutonner,  ‘to  bud ; to  button’,  fr.  bouton,  ‘bud;  button’.  See  button, bo  tree.  —  Singhalese  bo,  fr.  Pali  bodhi,  shortened fr.  bodhi-taru,  ‘bo  tree’,  lit.  ‘tree  of  wisdom  or enlightenment’,  fr.  bodhi,  ‘wisdom,  enlighten¬ ment’,  and  taru,  ‘tree’.  Pali  bodhi  is  rel.  to  OI. buddhah,  ‘awakened,  enlightened’.  See  Buddha. Botrychium,  n.,  a  genus  of  plants,  the  moonwort (bot.)  —  ModL.,  fr.  Gk.  Porpuyo?,  ‘grapestalk’, which  is  rel.  to  (36xpu<;,  ‘a  cluster  of  grapes’  (see next  word) ;  so  called  because  its  sporangia  form a  cluster  resembling  that  of  grapes.  See  next word.
5796:Buddha,  n.,  incarnation  of  deified  religious  teach¬ ers,  esp.  of  Gautama  Siddharta  (563-483).  — OI.  buddhah,  ‘awakened,  enlightened’,  pp.  of bddhati,  budhyate,  ‘is  awake,  observes,  under¬ stands’,  fr.  I.-E.  base  *bheudh-,  ‘to  offer,  present’. See  bid  and  cp.  bo  tree.
15876:gaussbergite,  n.,  a  kind  of  lava  ( petrogr .)  —  So called  from  Gaussberg,  a  mountain  in  Kaiser Wilhelm  II  Land,  Antarctica,  a  name  com¬ pounded  of  Gauss,  name  of  the  ship  used  by  the German  Antarctic  Expedition,  and  of  G.  Berg, ‘mountain’.  See  borough  and  subst.  suff.  -ite. Gautama,  n.,  the  name  of  many  sages,  also  sur¬ name  of  Buddha.  —  OI.  Gdtamah,  prop,  a patronymic  meaning  lit.  ‘descendant  of  the greatest  ox’,  and  superl.  of  gauh,  gen.  gdh, ‘ox,  bull,  cow’.  See  cow  and  cp.  gaur,  the  first element  in  Gaekwar  and  in  gopura  and  the  sec¬ ond  element  in  nilgai.
20136:Derivatives :  jail,  gaol,  tr.  v.,  jail-er,  gaol-er,  n. Jain,  n.,  an  adherent  of  a  non-Brahmanic  sect in  India.  —  Hind.  Jaina,  fr.  OI.  Jainah ,  ‘of  a Buddha’,  fr.  jinah,  ‘hero,  saint’,  which  is  rel.  to jayati,  ‘conquers’,  jayah,  ‘victory’,  jindti,  ‘over¬ comes,  subdues’,  jyd,  jid,  ‘superior  force’,  jydyan, ‘mightier’,  jyesfhah,  jyesthah,  ‘mightiest’,  and cogn.  with  Gk.  fitoc,  ‘force,  might,  violence’. Cp.  the  second  element  in  Zenobia.
=== SKT forbid ===
6930:Forbid.  (£.)  Fiom  For-  (a)  and Bid  (a).     K.S./or&eSJan.  +  G.  vtrhietiH,
```


## [2026-09-05T14:13:35.939Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== NYB ===\"; grep -n \"bōxt\\|boxt\\|bōzišn\\|bozisn\\|bōy\\|bwd\\b\" NYB_vol2_glossary.txt | head -20\necho \"=== WLD bheug ===\"; grep -n \"bheug\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-05T14:13:36.002Z] TOOL RESULT

```
=== NYB ===
258:a-bod [bwd] unconscious 103%. — V. béd (1).
1008:bod [bwd] 1. consciousness 312. 642%, — 2. scent, fragrance 891°; [incense PR 1112]. — 1. Av. (919) baodah- ‘perception’ ; Paz. boi. 2. Av. (918) baoöi- MPrth bwd?e?r ‘aromatic herbs’ (S); Arm. lw. boir-k‘; MPrs bwy (A-H II); Paz. NP boi. Cf böstän. — bwd 81° is probably a fault for bryn = brin (q. v.).
1081:buxtan [bwhtn'] bēž- [bwe-], to save, to preserve (hac from) 701, 8519-20, 8825, pass. buxtém we are saved 61; inf. buxtan in pass. sense: to be saved = to come out of the ordeal (of fire) safe and sound (pat: ‘thus proving the truth of .. .’) 10916. . Av. (916 sq.) baog-; Ps. bwhty, bwe-; MPrthPrs bwatn, pres. MPrth bwy-, bwas-, MPrs bwz-; Arm. lw. bužem; Paz. boxtan, buxtan, bož-. — V. božišn.
2035:hubéd (hwbwd] fragrant, full of sweet |
2036:scent, of Paradise 7320-25, 761, 857.11; comp. ~-tar 7321. — Paz. hüböi. V. bod. hubódéh sweet scent, the quality of being sweet-scented 621%, opp. gandakéh; hac hamäk ~ hubodtar 7371. — Paz. hubdi. Huböd-Xösröi [hwbwd-hwsrwd] a town 114%, cf s. v. Xosroi.
2987:passand [psnd] lenity, in a juridical sense: reduction of what the law formally pre- scribes in any special case, as opposed to dätistän (g. v.), 701. — passand and dätistän are symmetrically opposed juridical terms, defined and exemplified in the Syriac Corpus iuris of I$6*boxt (Syrische Rechtsbūcher, ed. by Sachau, III, 1914, 12-14): — Suppose a man owes a sum and equally as much in interest fallen due, but cannot pay the sum total be- cause of poverty, illness, or the like; if then, at his request, the creditor remits the interest and rests content with the capital, this is passand. On the other
3109:must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb' = mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow which has been. set on fire, and burn fragrant fuel for the benefit of thy offspring which is in thy womb’.
5576:bwd’e’r: bod
=== WLD bheug ===
9328:144                                             bheug-
9381:1. bheug- „fliehen“,    von Pick I^ 490 von bheiigQi)- „biegen“ getrennt, aber
9396:                                        bheug(li)   — bheug-, bbeugb-                                 145
9420:Wzansatz bheug- (got. g) neben bheug (arisch), das ursprgl. im Nasalpraesens
9421:aus bheug- erweicht sei (erwogen von Osthoff aaO.). Die Doppelheit germ.
9422:gh ar. g^ auch bei bheugh (dt. biegen) bheug (ai. bhvjaii usw.) „biegen".
9428:An ursprgl. Identitiit unserer Wz, mit diesem andern bheug{h) „biegen“
9433:mitteln wie mit biugan „biegen" (Lit. u. bheug- -gh- „biegen“.     ^
9440:"^bhend- wegen but ,, Putter" usw.), gegen den mit dt Bauch s. u. bheug-
9449:3. bheug-*, bheugh- „biegen" (== bheug- „fiiehen",                      s.   d. ;    schwerlich aber    =
```


## [2026-09-05T14:13:50.639Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ewg-",
 "prompt": "Give the reconstruction, meaning, and descendants for PIE *bʰewg- (which sense: flee/escape?), including Indo-Iranian (Avestan baog-) and Italic (Latin fugiō) branches."
}
```


### [2026-09-05T14:13:56.528Z] TOOL RESULT

```
# PIE *bʰewg- (Flee/Escape)

## Reconstruction
**\*bʰewg-** (perfective aspect)

## Meaning
"to flee" or "to escape"

## Key Descendants

**Indo-Iranian Branch:**
- Younger Avestan: 𐬠𐬏𐬘 (būj, "to save, redeem")
- Middle Persian: bōxtan ("to free, liberate, save")
- Classical Persian: بختن (buxtan, "to save, rescue, redeem")

**Italic Branch:**
- Latin: fūgī (from Proto-Italic *fougom)

**Other Notable Descendants:**
- Ancient Greek: ἔφυγον (éphugon, "fled")
- Proto-Iranian: *bauǰ-

The Wiktionary entry notes this root is "apparently originally the same root as the synonymous *bʰegʷ-" and represents a perfective aspect verbal formation with widespread attestation across Indo-European language families.
```


## [2026-09-05T14:14:09.828Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%DB%8C' --note 'page 95, root Bheudh, node 2: Persian بوی from MP bōy \"smell, scent; incense\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%B3%D8%AA%D8%A7%D9%86' --note 'page 95, root Bheudh, node 2: بوستان = بو + ـستان, MP bwdstʾn/bwyystʾn flower garden' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ewd%CA%B0-' --note 'page 95, root Bheudh: PIE *bʰewdʰ- \"to be awake, be aware\", descendants' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%BE%D9%88%D8%B2%D8%B4' --note 'page 95, root Bheug, node 3: پوزش from MP bōzišn, verbal noun of bōxtan/bōz-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0ewg-' --note 'page 95, root Bheug: PIE *bʰewg- \"to flee, escape\", Av. būj-, MP bōxtan, Lat. fūgī' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/Buddha' --note 'page 95, root Bheudh, nodes 8-9: Buddha < Pali/Skt buddha pp. of budh, PIE *bheudh-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/bid' --note 'page 95, root Bheudh, node 11: bid = merger of OE biddan (*gʷhedh-) and bēodan (*bheudh-)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/fugitive' --note 'page 95, root Bheug, nodes 6-7: Latin fugere, PIE *bheug- to flee; refuge, centrifugal' 2>&1 | tail -3"
}
```


### [2026-09-05T14:14:14.218Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/96f3a2729db728a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/972432b4cbd1fa51.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f4b01fa7d37ac363.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e687950c65cced09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/05db50c077e3fb32.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/92e30df762e2e20f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3921f8c3a5eb0245.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/82046fadecf8a114.txt
```


## [2026-09-05T14:14:19.623Z] TOOL CALL #59: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg95.png data/verification/sources/refs/ocr/BOOK/95.png && ls -la data/verification/sources/refs/ocr/BOOK/ | head\necho \"=== verify_check ===\"; sed -n 1,140p tools/verify_check.py"
}
```


### [2026-09-05T14:14:19.690Z] TOOL RESULT

```
total 2216
drwxrwxr-x 2 sfmqrb sfmqrb   4096 Sep  5 10:14 .
drwxrwxr-x 9 sfmqrb sfmqrb   4096 Sep  5 01:38 ..
-rw-rw-r-- 1 sfmqrb sfmqrb 104864 Sep  4 19:03 101.png
-rw-rw-r-- 1 sfmqrb sfmqrb  86203 Sep  4 19:03 126.png
-rw-rw-r-- 1 sfmqrb sfmqrb 105296 Sep  4 19:03 311.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96466 Sep  4 19:03 33.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99093 Sep  4 19:03 39.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54479 Sep  4 19:03 46.png
-rw-rw-r-- 1 sfmqrb sfmqrb  99295 Sep  4 19:03 54.png
=== verify_check ===
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


## [2026-09-05T14:15:05.571Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 220 221 222 223; do echo \"=== leaf $n ===\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KNT.txt | head -6; echo \"...\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n+1' KNT.txt | tail -3; done"
}
```


### [2026-09-05T14:15:07.325Z] TOOL RESULT

```
=== leaf 220 ===
tem (530, $148.I, 6154.1), ef. Av. posana- ‘battle’, Skt. pfiana- ‘battle, army’, to root in Av. poral-onie ‘they fight’? (Bv. TPS 1945.69-4; not agency noun
‘fighter, foe’ as taken by Wb. KIA 90-1, Bv. Gr. $277; not paratara- ‘foe’, with Wackernagel, KZ 59.29-30, as compar. to [Skt.] pára- ‘distant’ = RV ‘enemy’). partaram asn. DNa 47.
Ратдата- (§29.n2, $31) adj. ‘Parthian’, also тазе, as sb. ‘Parthia’, a province of the Persian Empire: Elam. par-tu-ma, АКК. pa-ar-tu-á, Gk. IIapóià. Extension ($150) of stem seen with vriddhi in Pársa-, but with dialectal difference in the 0/s ($9. VT, 887).
(1) ‘Parthian’: Paréava nsm. DN iv; A?P 4. Par&avaibi$ ipm. DB 2.96. (2) ‘Parthia’: Paréava nsm. DB 1.16; 2.7, 92;
DPe 15; DNa 22; DSe 21°; DSm 8°; XPh 20.
Par8avai ism. DB 2.94° 96°; 3.5, 10. parna-, see duildparanam, parana-. ‘parsa- vb., see fraó-.
...
pasáva phrasal adv. (§191.IV) ‘after that, afterwards’: pasé + asn. ava (8181). DB 1.27, 30, 32, 33, 34°, 35f, 40, 43, 46, 54, 72, 731, 75, 79, 82, 83, 86, 91, 94; 2.1, 3, 4, 12, 16, 19, 21, 27, 31, 32, 47, 49°, 51, 52, 62, 64, 67, 71, 72, 81, 84f, 94; 3.1,4, 9, 12f, 15, 20, 25, 29, 33, 36f, 41, 50, 59, 70, 73,75, 81, 84, 86, 90f°; 4.5, 35, 91; 5.3, 6, 9, 10f, 13, 21°, 28, 25°, 29; DSe 48; DSf 25; DZe 10; XPh 36; XSe 3; XV 23; А:Ра 21°; Рр 4°. pasãva-šim DB 2.76, 90. pasdva-Saiy DB 2.88.  pasáva-dim DNa 33. pasdva-mary XPh 32.
pasti- sb. ‘foot-soldier’: Skt. pailt-, from pIE *ped- ‘foot’ (OP pad-) + suffix -t&- ($85, 5152.11; Wb. Grab 40, Hz. ApI 94-8). — pasti$ nsm. DNb 48, 45.
pilar- sb. ‘father’: Av. pilar-, NPers. pióür, Skt. pitd
=== leaf 221 ===
r-, Gk. rarnp, Lt. pater, Gt. fadar, pIE *poler- (863.11, 875.1, 576.1, $154.II); see also hamapilar-. pita пет. ($86.П, $124.5, $186.1T) DB 1.4 bis, 5 bis, 6; 2.93; DBa 5, 6, 6f, 7, 8; DSf 12, 58; XPa 15; ХРе 12; XPf 16, 17, 19, 23, 31, 33, 42; XPg 7; X8a 2; XV 18; А!Ра 20f; D?Sb 4°. pica gsm. ($78, $124.5, $186.If) XPa 20; ХРе 14; XPf 35, 38, 47.
Pirdva- sb. ‘Nile’ (§75.V, $124.II, §166.V]): Pirdva пзш. DZc 9, in naming phrase, anacolu- thic for abl. after Ласа; either ‘Ivory River’, as deriv. adj. to piru- ‘ivory’, or possibly plural ‘The Tusks’ (JAOS 51.209).
miru- sb. ‘ivory’ (§75.V, 5153.1): Elam. pi- ru-§, Akk. pilu-, with cognates (or borrowings) in Eastern Asiatic languages (Przyluski, BSLP
197
27.3.220-2; Scheil, Rev. d’Assyr. 24.120; Bv. BSLP 30.1.62; König, Burgbau 66; Hz. AMI 3.67-8).  piruf пет. DSf 48.
pi-, vb., see paid-.
...
fratarta DB 3.26, incorrect reading for fra- taram (Cameron).
fral- vb. ‘ask, examine, investigate, punish’: Av. fras-, Skt. pra-, Lt. precor, pIE *prek-, with inchoative present, *prk-ske-, OP parsa-, Av. poro- saiti, NPers. pursdd, Skt. precháti, Lt. poscit. Cf. also ufrasta- ufrasta-. parsdémiy 1st sg. (830, $97, $130, $212, 5226.1) ОМ 19. aparsam Ist sg. imf. ($122, 5182.3, $212. $226.П) DB 1.22; 4.67, parsü 2d sg. imv. (8212, 5237.1) DB 4.38, 69. . frabiyaiš opt. pass. ($220, $228.П, $228.11) DNb 21 (not desid. fut. pass., as taken by Hz. Арі 167). pati- + parsa- ‘examine, read’ (on meaning, Bv. DSLP 31.2.71-2): patiparsühy 2d sg. subj. (§222.- II, $227.I) DB 442.  patiparsátiy subj. ($222.11) DB 4.48.
frafara- adj. ‘superior’: fra- + variant com- par. suffix -thara- seen in Av. fraéara- ($1491, 6190.11; Wb. ЖА 41.319; Bv. 33.2.150-1, 34.1.33-4, Hz. AMI 4.126-7, 8.3940, ApI 166-7), cf. superl. -thama- in Skt. prathamd- ‘first’. Cf. also uradara
=== leaf 222 ===
-. — fra&aram asn. XPf 26f, 37.
Fraéda- sb. ‘Frada’, a Margian rebel: Elam. pir-ra-da, АКК. pa-ra-da-’ ; perhaps thematic noun- stem (§141) to fra- + *dà-, with vriddhi ($126), cf. Av. früd- ‘to further, increase’ (ТИМ. AiW 1012), but more probably hypocoristie to a com- pound name ($164.П1; Bthl. AiW 1018) of which the prior part was the participial stem to the same compound verb (§162), ef. Av. adj. fradat.qaéa- ‘prospering the household’, sb. frddaj.fsav- ‘Pro- moter of flocks’ (name of a divinity; Bthl. AiW 1013-4). Not with Sen 52 (fra- + OP *ad- ‘drive’, Av. azaiti, Skt. djati, Lt. agit), nor with Justi, INB 101 (fra- + had- ‘sit’, with loss of intervocalic -h-). Fraéda nsm. DB 3.12; 4.23; ОВ] 1.
framatar- sb. ‘master, lord’ (‘giver of judicial decisions’, ace. to Hz. ApI 150-4): fra- + root mā- + agent suffix -tar- (5154.1). framatéram asm. (§124.VI, $1861) DNa 7f; DSe 7; DSf 5; DE 11; XPa 5; XPb 11; XPe 5; XPd 8; ХР? 7f; XPh 6; XE 11; XV 9; A'Pa 8°; A?He 7. frama- ібгат (852.111) A?Pa 8.
framána- sb. ‘command’ (judgment, deci- sion’, acc. to Hz. ApI 144-50): РЫ. framán, NPers.
OLD PERSIAN
fürmán; fra- + mä- + suffix -nà- ($128, $1471), ef. Skt. pramána-m ‘measure, standard’. — framánà nsf. DNa 57; DNb 28; DSj 3°, framánáyà isf. DNb 37.
...
Düxtri- sb. ‘Bactria’, a province of the Persian Empire: Elam. ba-ak-&-18, ba-ik-tur-ri-i$, Akk. ba-ah-tar, Gk. (nt. pl) Béxrpa (§9.1, $79, 6103.111). OP %-stem, for older 7-stem (8152.II), seen in Av. báxói. — Büziri$ nsf. DB 1.16; DPe 16; DNa 23; DSe 22°; D8m 9°; XPh 21. Ваг- triyd \sf. DB 3.13f, 21. Baztriya absf. DSf 36.
bag- vb., see under baga-, bàji-.
baga- sb. ‘god’: Av. baga- ‘lot, good fortune’, Skt. bhdga- ‘dispenser (of good fortune)’, Gk. -paryos ‘eater’, OCS bogi ‘god’, pIE *bhago- ($101, $122, 5143.1, V, VI); ef. Hz. ApI 105-10. See also Bagábigna-, Bagabuxsa-, Bagayddi-, bà. рада nsm. AmH 6; AsH 6; DNa 1; DNb 
=== leaf 223 ===
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
...
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
```


## [2026-09-05T14:27:22.056Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON biyus ===\"; grep -n \"بیوسیدن\\|بیوسنده\\|نابیوسان\" MON_part1.txt MON_part2.txt | head -5\necho \"=== ARY latin index ===\"; grep -n \"BHEUDH\\|BHEUG\\|BAUD\\|BAUG\" incoming/ARY/ARY_latin_index_pages.txt | head -10\necho \"=== SYN smell ===\"; grep -n \"bostan\\|Pers. boi\\|Pers. bu\\b\" SYN.txt | head -5\necho \"=== HUB 7072 ctx ===\"; sed -n '7065,7080p' HUB.txt"
}
```


### [2026-09-05T14:27:22.183Z] TOOL RESULT

```
=== MON biyus ===
MON_part1.txt:35931:پبیوسیدن: 5-1420( [- بیوسیدن] 
MON_part1.txt:37237:آرزومند کردن به امید افکندن؛ بیوسیدن) 
=== ARY latin index ===
3138:BRU (SERBIAN) «yp BAUGGIA :(OLD SAXON) oy St -
3902:B23 gta Coad 661" 5 "pat slay pi 4) *BHEUDH: 64 aly bt rly cal obj dll et
4034:SKEAT:  (BHEUDH) 752, (BID) 59 BIOTAN, BITTEN
4041:aSp POKORNY J cul ols (ly 9b 41, *BHEUDH ,*BHEDH sla |) BARNHART ~
=== SYN smell ===
16000:Lat. perf. fui, etc. (early Lat. also infin. fore, imperf. subj. forem, Osc. fustd ‘esset’), It., Sp. fui, Fr. fus, Rum. fui, Rum. infin. fi, ete.; Ir. biwu, NIr. bim (consuetud. pres.), infin. Ir. buzth, NI. beith, W. bod, Br. beza (MBr. bout), Br. 3sg. bez, etc. (Pedersen 2.437 ff.); OF infin. béon, ME be(n), NE be, Isg. OE béo(m), NE be (subj. and dial. in- dic.), OHG bim, MHG, NHG bin, Du. ben; Lith. buti, Lett. but, pret. Lith. buvau, Lett. biju; ChSl. byti, SCr. bitz, Boh. byt, Pol. byé, Russ. byt’, pret. ChSI. bychu, pple. pret. ChSl. bylz, Russ. byl, etc.; Skt. bhi-, Av., OPers. bu- (8sg. Skt. bhavati, Av. bavait, OPers. 3sg. pret. abava, etc.) ‘become’ and simply ‘be’. (NPers. biidan ‘be’).
=== HUB 7072 ctx ===
257, zd. maiit- *Wein (nach Darmesteter); fcai Vann,
wie?' = zd. kada; Dai *der zehnte MonatV zd. dadvd; nai
*Rohr , g. nad 'Rohr = skr. nada-, vgl. nai TlOte' aus
^nada-; pai Tussspur = zd. paia-, ap. nipadiy; x^ai
*Schweiss* = zd. x^'a^da- (also x'ai aus x'aiy); pai {pa) 'Fuss*
= zd. pada- ; -ra Casuspartikel = paz. ra, phi. rai wegen',
ap. radiy Vegen*; x^ai {x^a) *Wohlgeschmack' = skr. svada-;
boi {ho) *Geruch* = zd. baoidi- (arm. buidenik Moses, Geogr.
616, wohl boyicenik zu lesen = np. boy i ctnt 'chinesisches
Parfum'); roi {ro) 'aes vel stannum fusum' = bal. rDd 'Kupfer ,
arm. avoir 'Messing, skr. loha-; roi {rd) 'Gesicht' = zd.
raoda-; xoi *Helm' (unbelegt) neben xDd, arab. xudat, arm.
^) Dazu np. kahar = skr. kadrxi- *rotlibraun*, zd. kadrv0'{a3pa')^
Geiger, Idg. P. IV, Anz. p. 23.— 200 —
xoir '^DiademV ^p. xaudc^, zd. xaoda-; mOi *Haar = paz.
mU Min. Gl. 140, g. frnd, bal. mUd^ mid, nb. mldy also ap.
```


## [2026-09-05T14:34:53.676Z] TOOL CALL #62: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk95.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ne0 = {\n \"entry\": 0,\n \"root\": \"Bheudh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *bʰewdʰ- 'to be awake, be aware; to make aware'\",\n \"note\": (\"Pokorny I 150-153 heads the entry 'bheudh-, nasal. bhu-n-dh- „wach sein, wecken, beobachten; \"\n          \"geweckt, geistig rege, aufmerksam sein, erkennen, oder andere dazu veranlassen“'; Watkins/AHD gives \"\n          \"'bheudh-. To be aware, to make aware. [Pok. bheudh- 150.]'. Root shape, language label ('Indo-European') \"\n          \"and page reference are all correct. Nourai's gloss 'to be aware, enlighten' is right in its first half; \"\n          \"'enlighten' is not the PIE meaning but a Buddhist-Indic specialisation of the same root (Skt. buddha- \"\n          \"'awakened, enlightened', bodhi- 'perfect knowledge'), so it is defensible as a shorthand for the whole \"\n          \"chart. Note that the whole 'fragrance' half of the chart (nodes 1-6) belongs to Cheung's *baud2 'to smell', \"\n          \"which he treats as a possible ancient specialisation of *baud1 'to feel, sense' rather than as certainly \"\n          \"the same Iranian root.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی \"\n   \"آغازین *bʰewdʰ- به معنی «بیدار \"\n   \"بودن، آگاه شدن، دریافتن» \"\n   \"است؛ پوکورنی (جلد ۱، ص ۱۵۰–۱۵۳) \"\n   \"آن را «wach sein, wecken, beobachten» معنی کرده و \"\n   \"واتکینز نیز «to be aware, to make aware». \"\n   \"نام ریشه، برچسب زبانی و ارجاع \"\n   \"POK:150 هر سه درست است. معنی دومی که \"\n   \"نورایی آورده («roshan kardan / enlighten») معنی \"\n   \"هندواروپایی نیست بلکه \"\n   \"تحول معنایی ویژهٔ سنسکریت \"\n   \"buddha- «بیدارشده، روشن‌شده» است. \"\n   \"به این ترتیب ادعای نورایی \"\n   \"درست است؛ فقط باید دانست که \"\n   \"شاخهٔ «بوی» (گره‌های ۱ تا ۶) \"\n   \"در فرهنگ چونگ زیر ریشهٔ \"\n   \"*baud² «بوییدن» جدا شده که \"\n   \"شاید تخصیص کهنی از *baud¹ باشد.\"),\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewd%CA%B0-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:150\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 159 (printed p.150, bottom) begins: 'bheudh-, nasal. bhu-n-dh- „wach sein, wecken, beobachten; geweckt, geistig rege, aufmerksam sein, erkennen, oder andere dazu veranlassen (aufpassen machen, kundtun, gebieten; darbieten)“'; the entry runs to p.153. Exactly Nourai's root and gloss.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bheudh-\", \"stance\": \"supports\",\n    \"note\": \"'bheudh-. To be aware, to make aware. 1. Germanic *(for)beudan ... 5. Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA ... [Pok. bheudh- 150.]' (AHD_watkins1985.txt line 338).\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II 147\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd2_pages.txt line 9525 carries the running head 'bheudh- 147'; Pokorny's own closing reference for the root is 'WP. II 147 f.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann no. 1266 / 1875\", \"stance\": \"supports\",\n    \"note\": \"'bheudhó ‘prompt, arouse, exhort; be awake’. Cf. bhudh-. WP II, 147 Skt. bódhami; Gk. peuthomai ...; Go. cf. ana-, faür-biudan; OHG biotan; OE beodan' and no. 1875 'bhudhó ‘wake, watch, care, notice’'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *baud1, *baud2 (pp. 14-16)\", \"stance\": \"partial\",\n    \"note\": \"Cheung sets the PIE etymon as '*bʰeudʰ- ‘to become attentive, be awake, perceive’ => LIV: 83 f. | Pok.: 150 ff.' but splits the Iranian material into *baud1 'to feel, sense' and *baud2 'to smell', adding 'it seems necessary to assume two separate Ir. roots. But on the other hand, *baud2 may be ultimately an ancient specialisation of the root *baud1'.\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"] = [\n {\n  \"id\": 1, \"lang\": \"Avestan / Old Persian\", \"words\": \"baoidi, baodhi, baud-a\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"The word is Young Avestan baoiδi- n. 'fragrance, sweet smell' (Bartholomae, AiW col. 918; cf. \"\n    \"hu-baoδay- 'Wohlgeruch' AiW col. 918-919), beside baoδah- n. 'perception, faculty of perception' (AiW 919) \"\n    \"and the verb baod-/baoδ- 'to perceive, sense', with a specialised sense 'to smell' (Y Av. upa.baoδ- 'to have a \"\n    \"smell', a-ham.baoδəmna- 'unable to smell', hupo.busta- 'well scented'). Pokorny I 151 lists exactly 'av. \"\n    \"baoiði- „Wohlgeruch“ (= ai. bodhi- „vollkommene Erkenntnis“)'. Nourai's three shapes are one and the same \"\n    \"Avestan word in three transcriptions of -δ- (baoidi = baodhi) plus the thematic verbal stem baoδa- ('baud-a'). \"\n    \"The chain from PIE is regular: *bʰewdʰ- > Proto-Iranian *baudi- (PIE *-dʰ- > Ir. *-d-, written δ between \"\n    \"vowels in Avestan), with the diphthong *eu > Av. ao. The one thing that is not right is the language label: \"\n    \"no Old Persian word of this family is attested — Kent's Old Persian lexicon has no *bauda-/*baudi- (only bav- \"\n    \"'to be'), so 'Avestan / Old Persian' should read simply 'Avestan' (or 'Old Iranian').\"),\n  \"derivation_fa\": (\"صورت درست این واژه اوستایی \"\n    \"baoδi- «بوی خوش، رایحه» است (بارتولومه، \"\n    \"ستون ۹۱۸) در کنار baoδah- «دریافت، \"\n    \"ادراک» و ستاک فعلی baod-/baoδ- «دریافتن، \"\n    \"بوییدن»؛ هر سه صورتی که نورایی \"\n    \"آورده یک واژه‌اند با آوانگاری \"\n    \"متفاوت دال میان‌واکه‌ای (δ). \"\n    \"از هندواروپایی *bʰewdʰ- به ایرانی \"\n    \"باستان *baudi- (دال دمیدهٔ هندواروپایی \"\n    \"در ایرانی به d و در اوستایی میان دو \"\n    \"واکه به δ بدل شده). پوکورنی در ص ۱۵۱ \"\n    \"عیناً «av. baoiδi- „Wohlgeruch“» دارد. اما برچسب \"\n    \"«پارسی باستان» نادرست است؛ در \"\n    \"فرهنگ کنت هیچ صورت پارسی باستان \"\n    \"از این خانواده ثبت نشده، پس \"\n    \"باید تنها «اوستایی» (یا \"\n    \"«ایرانی باستان») می‌بود. \"\n    \"به این دلیل حکم «با احتیاط \"\n    \"پذیرفتنی» است.\"),\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewd%CA%B0-\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:151\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 160 (printed p.151): 'av. baoiði- „Wohlgeruch“ (= ai. bŏdhi- „vollkommene Erkenntnis“)', in the same paragraph as av. baodaiti 'nimmt wahr' and baoðah- 'Wahrnehmung'.\"},\n    {\"ref\": \"BQT:311\", \"status\": \"supports\",\n     \"note\": \"BQT_v1_pages.txt leaf 531 = printed p.311 (running head ۳۱۲ on the next leaf), s.v. «بو», Mo'in's footnote 3: 'پهلوی bōd, bōy ... اوستا baoδi- ، بارتولمه ۹۱۸ ... در اوستا baoδi به معنی بوی خوب (در مقابل gaṇḍa به معنی گند، بدبوی) آمده'.\"},\n    {\"ref\": \"FFD:39\", \"status\": \"supports\",\n     \"note\": \"FFD_pages.txt [pdf page 44] = printed p.39, s.v. بوییدن: 'بوی < فارسی میانه bōy < ایرانی باستان *baud-...، ریشهٔ baud به معنی «بوی بردن»، «پی بردن» است'. Abolghasemi's index (p.~117) lists the root baud on pp. 39, 40, 45, 49 — i.e. exactly Nourai's FFD:39 and FFD:40.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"cols. 917-919 (baod-, hu-baoδay-)\", \"stance\": \"supports\",\n     \"note\": \"'j., g. baod- ‘sentire’ ... 1) ‘sentire, wahrnehmen, gewahr, inne werden’ ... 2) ‘riechen nach —’ (Akk.)'; and 'j. hu-baoδay- 1) f. ‘Wohlgeruch’: baoiδīs baoδaite nmanum … „nach Wohlgerüchen duftet das Haus“ Yt 17.6'.\"},\n    {\"src\": \"NYB\", \"where\": \"Glossary s.v. bōd\", \"stance\": \"supports\",\n     \"note\": \"'bōd [bwd] 1. consciousness ... 2. scent, fragrance; [incense PR 111]. — 1. Av. (919) baoδah- ‘perception’; Paz. bōi. 2. Av. (918) baoδi- ... MPrs bwy; Paz. NP bōi. Cf bōstān.' Nyberg's column numbers 918/919 are Bartholomae's.\"},\n    {\"src\": \"KNT\", \"where\": \"Lexicon pp. 164-215\", \"stance\": \"silent\",\n     \"note\": \"No Old Persian *bauda-/*baudi- in Kent; the only b-au- entry is 'baug- vb. ‘free’' (p.198), which belongs to the second chart on this page. Grep of KNT.txt for 'baud'/'baodi' returns only Āθiyābaušna-, where Herzfeld's rejected alternative involves ā-baud- 'be fragrant'.\"}\n  ]\n },\n {\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"bŭy; bŭy-yîdan; bŭ-stân\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Av. baoiδi- gives Middle Persian bōy, written ⟨bwd⟩ in Book Pahlavi and ⟨bwy⟩ in Manichaean MP: \"\n    \"MacKenzie 1971 has '2bōy [bwd | M bwy, N bōy] smell, scent', 'bōyīdan, bōy- [bwd-ytnʹ] smell (intr.)' and \"\n    \"'bōyestān [bwdstʼnʹ | M bwystʼn, N bōstān] (flower) garden'. Intervocalic Old Iranian *-d- (< PIE *-dʰ-) \"\n    \"was spirantised to *-δ- and lost in Middle Persian after the diphthong, whence bōy > NP بوی būy/bū. \"\n    \"بوییدن is the NP continuation of MP bōyīdan (a denominative ‘to give off / take in a smell’). \"\n    \"بوستان is bōy 'fragrance' + the place-suffix -stān, i.e. 'place of fragrance' (Nourai's 'place of \"\n    \"flowers'), with loss of the -y- before the consonant cluster: MP bwdstʼn / bwystʼn > bōstān > NP بوستان, \"\n    \"later also بُستان with u; the doublet بُستان was borrowed into Arabic as بستان. \"\n    \"Cheung s.v. *baud2 lists 'NP bōy ‘smell, scent’, NP bōstān ‘garden’' among the direct reflexes.\"),\n  \"derivation_fa\": (\"«بوی» از فارسی میانهٔ bōy \"\n    \"(در پهلوی کتابی ⟨bwd⟩ و در پهلوی \"\n    \"مانوی ⟨bwy⟩)، از اوستایی baoδi-؛ \"\n    \"دال میان دو واکه در فارسی \"\n    \"میانه سایشی شده و پس از \"\n    \"دوگانه‌واکه افتاده است. \"\n    \"مکنزی هر سه واژه را دارد: \"\n    \"bōy «بوی»، bōyīdan «بوییدن» و \"\n    \"bōyestān «باغ گل». «بوستان» \"\n    \"مرکب است از بوی + پسوند \"\n    \"مکان ‌ستان، یعنی \"\n    \"«جای بوی خوش»؛ یای آن \"\n    \"پیش از خوشهٔ همخوان افتاده \"\n    \"و صورت «بُستان» آن معرّب \"\n    \"شده است. هرن (شمارهٔ ۲۴۰)، \"\n    \"هوبشمان (ص ۱۹۹)، مکنزی و \"\n    \"چونگ همگی همین را \"\n    \"می‌گویند؛ ادعای نورایی \"\n    \"درست است.\"),\n  \"sources\": [W + \"%D8%A8%D9%88%DB%8C\", W + \"%D8%A8%D9%88%D8%B3%D8%AA%D8%A7%D9%86\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:311\", \"status\": \"supports\",\n     \"note\": \"Borhan-e Qate' (Mo'in) vol. 1 p.311 s.v. «بو» with Mo'in's etymological footnote quoting Pahlavi bōd/bōy, Avestan baoδi- (Bartholomae 918), Armenian boyr, and the Bundahišn; BQT_v1_pages.txt leaf 531.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 pp. 19-20 s.vv. bōy, bōyīdan, bōyestān\", \"stance\": \"supports\",\n     \"note\": \"PHD_mackenzie.txt lines 1597-1606: '1bōy [bwd] perception, sense'; '2bōy [bwd | M bwy, N bōy] smell, scent'; 'bōyestān [bwdstʼnʹ | M bwystʼn, N bōstān] (flower) garden'; 'bōyīdan, bōy- [bwd-ytnʹ] smell (intr.)'.\"},\n    {\"src\": \"HRN\", \"where\": \"no. 240, pp. 54-55\", \"stance\": \"supports\",\n     \"note\": \"Horn: 'bōi, bō ‘Geruch’, bōyīden, bōyāmīden, bōstān, būstān. aw. baoiδi- ‘Wohlgeruch’; phlv. bōd, bōi, bōyīnītan; ai. budh- ‘merken, wahrnehmen’' — the whole node in one entry.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 199-200\", \"stance\": \"supports\",\n     \"note\": \"Hübschmann, in the list of NP -oi < Old Iranian *-oδa-: 'boi (bo) ‘Geruch’ = zd. baoiδi- (arm. buidenik ... = np. bōy i čīnī ‘chinesisches Parfüm’)'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *baud2 'to smell' (pp. 15-16)\", \"stance\": \"supports\",\n     \"note\": \"'*NWIR: NP bōy ‘smell, scent’, NP bōstān ‘garden’, Bal. bōd ‘smell, perfume’ ...'; MP section 'MMP bwyy-, BMP bwd- /bōy-/ ‘to smell [intr.]’'.\"},\n    {\"src\": \"NYB\", \"where\": \"Glossary s.v. bōd\", \"stance\": \"supports\",\n     \"note\": \"'2. scent, fragrance ... MPrs bwy (A-H II); Paz. NP bōi. Cf bōstān.'\"}\n  ]\n },\n {\n  \"id\": 3, \"lang\": \"Avestan / Old Persian\", \"words\": \"pati-baus\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"The underlying compound is genuine: Avestan paiti + baod- 'to direct one's attention to, heed' \"\n    \"(Bartholomae; Cheung *baud1 '(+ *pati-) to concentrate on, heed'), with the nominal derivative Av. paiti-busti- f. \"\n    \"'the noticing' and the negative a-paiti.busti- adv. 'unnoticed' (AiW). But 'pati-baus' as printed is not an \"\n    \"attested Avestan or Old Persian word form; it is Nourai's shorthand for the Old Iranian inchoative stem \"\n    \"*pati-baud-sa-, which is exactly what Abolghasemi reconstructs on the cited page: 'بیوس < فارسی \"\n    \"میانه ... < ایرانی باستان *pati-baud-sa-، pati پیشوند \"\n    \"فعلی است ... d پیش از s به s بدل و در آن ادغام \"\n    \"شده است'. The -s- is the inchoative *-sa- suffix, and *-ds- assimilates to -s-, giving *pati-baus-. \"\n    \"The gloss 'to smell, expect, guess' merges the two senses of the root; in the compound only 'heed, watch for, \"\n    \"expect' is attested. No Old Persian form exists, so the language label again over-reaches.\"),\n  \"derivation_fa\": (\"پایهٔ این گره درست است: \"\n    \"در اوستا پیشوند paiti- با ریشهٔ baod- \"\n    \"معنی «توجه کردن، مراقب بودن» \"\n    \"می‌دهد و از آن paiti-busti- «دریافت» و \"\n    \"a-paiti.busti- «ناگهان، بی‌خبر» ساخته \"\n    \"شده است. اما «pati-baus» صورتی \"\n    \"مضبوط نیست؛ کوتاه‌نویسی \"\n    \"نورایی است برای ستاک \"\n    \"ایرانی باستان *pati-baud-sa- که \"\n    \"ابوالقاسمی (ص ۴۰) بازسازی \"\n    \"کرده است؛ در آن s پسوند \"\n    \"آغازی (inchoative) است و d پیش از s \"\n    \"همگون و ادغام شده. \"\n    \"بنابراین ریشه‌شناسی \"\n    \"درست ولی صورت استنادی \"\n    \"و برچسب «پارسی باستان» \"\n    \"دقیق نیست: با احتیاط \"\n    \"پذیرفتنی است.\"),\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewd%CA%B0-\"],\n  \"ref_check\": [\n    {\"ref\": \"FFD:40\", \"status\": \"supports\",\n     \"note\": \"FFD_pages.txt [pdf page 45] = printed p.40, s.v. بیوسیدن: 'بیوس < فارسی میانه ... < ایرانی باستان *pati-baud-sa- ... pati پیشوند فعلی است ... ریشهٔ baud به معنی «بوی بردن» است'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"s.v. a-paiti.busti-\", \"stance\": \"supports\",\n     \"note\": \"BRT.txt line 3527: 'j. a-paiti.busti Adv. „unvermerkt“: yasčīt ... tayuš vā vəhrkō vā ap° ... para.baraiti V. 7.10' — the paiti-baud- compound is attested, but only as a -sti- noun.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *baud1 (+ *pati-), p. 14\", \"stance\": \"supports\",\n     \"note\": \"'*AVESTAN: baod-, Y Av. baoδ- ‘to feel, sense’ || (+ *pati-) ‘to concentrate on, heed’'; and for the s-stem '(+ *pati-) MMP pyws- (inch.) ‘to desire, long for’'.\"},\n    {\"src\": \"POK\", \"where\": \"printed p. 152\", \"stance\": \"supports\",\n     \"note\": \"'buddhi- f. „Einsicht, Verstand, Meinung, Absicht“ (= av. paiti-busti- f. „das Bemerken“, gr. πυστις)'.\"},\n    {\"src\": \"KNT\", \"where\": \"Lexicon\", \"stance\": \"silent\",\n     \"note\": \"No Old Persian *pati-baud-; grep of KNT.txt for 'baud' returns only the root entry baug- and Āθiyābaušna-.\"}\n  ]\n },\n {\n  \"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"payôs\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Middle Persian is attested in Manichaean script as pyws- (inchoative) 'to desire, long for' \"\n    \"(DMMPP 291b; 3pl pywsynd, perf. pass. pywst), matched by Parthian bws- 'to await, wait for, expect' and pdbws- \"\n    \"'to desire, yearn' (Ghilain 65, 80). The reading is *payōs-/paywas- < Old Iranian *pati-baud-sa-: pati- > MP \"\n    \"pay- (the intervocalic -t- voiced and the -i- became the glide -y-), and *-ds- > -s-. Abolghasemi (FFD p.40) \"\n    \"gives the same Middle Persian antecedent for NP بیوس. The word does not survive into Book Pahlavi, so \"\n    \"MacKenzie and Nyberg have no entry — Nourai's 'payôs' comes from Abolghasemi, and is a legitimate reading \"\n    \"of the Manichaean spelling.\"),\n  \"derivation_fa\": (\"در فارسی میانهٔ مانوی \"\n    \"صورت pyws- «آرزو کردن، چشم داشتن» \"\n    \"ثبت شده و در پارتی bws- «انتظار \"\n    \"کشیدن» و pdbws- «آرزومند بودن»؛ \"\n    \"خوانش آن *payōs-/paywas- است، از \"\n    \"ایرانی باستان *pati-baud-sa-: پیشوند \"\n    \"pati- در فارسی میانه به pay- \"\n    \"بدل شده (ت میان‌واکه‌ای \"\n    \"نرم و افتاده) و خوشهٔ *-ds- به \"\n    \"-s- تبدیل شده است. این واژه \"\n    \"در پهلوی کتابی برجای \"\n    \"نمانده و به همین دلیل \"\n    \"در مکنزی و نیبرگ نیست؛ \"\n    \"صورت نورایی از \"\n    \"ابوالقاسمی گرفته شده \"\n    \"و پذیرفتنی است.\"),\n  \"sources\": [W + \"%D8%A8%D9%88%DB%8C\"],\n  \"ref_check\": [\n    {\"ref\": \"FFD:40\", \"status\": \"supports\",\n     \"note\": \"Abolghasemi, printed p.40 (FFD_pages.txt [pdf page 45]) derives بیوس from a Middle Persian form (OCR garbled) < ایرانی باستان *pati-baud-sa-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *baud1, Middle Persian / Parthian sections (p.14)\", \"stance\": \"supports\",\n     \"note\": \"'*MIDDLE PERSIAN: BMP bwd /bōy/ ‘perception, sense’ || (+ *pati-) MMP pyws- (inch.) ‘to desire, long for’ = DMMPP: 291b'; '*PARTHIAN: bws- (inch.) ‘await, wait for, expect’ || (+ *pati-) pdbws- ‘to desire, yearn’'.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie 1971, p- entries\", \"stance\": \"silent\",\n     \"note\": \"No payōs/pyws in MacKenzie (grep of PHD.txt and PHD_mackenzie.txt for 'payōs', 'payos', 'pyws' returns nothing); the word is Manichaean-only.\"},\n    {\"src\": \"NYB\", \"where\": \"Glossary\", \"stance\": \"silent\",\n     \"note\": \"Nyberg's Book-Pahlavi glossary has bōd and buxtan but no payōs.\"}\n  ]\n },\n {\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"bîyŭsîdan; bîyŭsandeh; nâ-bîyŭsân\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"New Persian بیوس bīyōs 'expectation, hope, longing' continues MP *payōs- < Old Iranian \"\n    \"*pati-baud-sa- (Abolghasemi p.40); MP pay- appears in early New Persian as پی‌/بی- with the diphthong \"\n    \"monophthongised to ī, and the initial stop shows the common early-Dari پ ~ ب fluctuation (Borhan-e Qate' \"\n    \"p.342 lemmatises it with ب). From the noun the denominative بیوسیدن 'to expect, hope' is formed \"\n    \"(Borhan: 'بمعنی امید داشتن و امیدوار گردیدن و \"\n    \"طمع کردن'), with present participle بیوسنده 'hopeful' and the negated \"\n    \"verbal adjective نابیوسان 'unlooked-for, unexpected' (nā- + bīyōs- + -ān). All three are \"\n    \"Shahnama/Garshaspnama vocabulary and are obsolete in modern Persian. The verse Nourai prints under this box, \"\n    \"'برآمد یکی نابیوسان نبرد / که دریا همه خون شد و \"\n    \"دشت گرد', is Asadi's, exactly as Noushin gives it.\"),\n  \"derivation_fa\": (\"«بیوس» در فارسی دری به معنی \"\n    \"«امید، چشم‌داشت، انتظار» \"\n    \"دنبالهٔ فارسی میانهٔ *payōs- \"\n    \"است؛ pay- فارسی میانه در فارسی \"\n    \"نو به بی‌/پی‌ بدل شده (ابدال \"\n    \"پ/ب در متون کهن فراوان است) \"\n    \"و از آن فعل مرکب بیوسیدن، \"\n    \"صفت فاعلی بیوسنده و \"\n    \"صفت منفی نابیوسان \"\n    \"«ناخواسته، غیرمنتظر» \"\n    \"ساخته شده است. برهان قاطع \"\n    \"(ص ۳۴۲) هر سه را با همین \"\n    \"معنی دارد و نوشین در \"\n    \"واژه‌نامک همان بیت \"\n    \"اسدی را می‌آورد. \"\n    \"ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%D8%A8%D9%88%DB%8C\"],\n  \"ref_check\": [\n    {\"ref\": \"FSF:98\", \"status\": \"supports\",\n     \"note\": \"Noushin, Vazhe-namak (FSF_pages.txt leaf 128) s.v. بیوسنده: '(اسم فاعل از بیوسیدن به معنی امید و آرزو داشتن)' and 'نابیوسان به معنی: ناخواسته، نه بر آرزو، غیرمنتظر، از اسدی (گرشاسب‌نامه): برآمد یکی نابیوسان نبرد / که دریا همه خون شد و دشت گرد' — the very verse and attribution in the chart.\"},\n    {\"ref\": \"FFD:40\", \"status\": \"supports\",\n     \"note\": \"Abolghasemi p.40 heads the entry بیوسیدن and derives بیوس < MP < *pati-baud-sa-.\"},\n    {\"ref\": \"BQT:342\", \"status\": \"supports\",\n     \"note\": \"BQT_v1_pages.txt leaf 562 = printed p.342: 'بیوسce ... طمع و خواهش و امید و امیدواری ... و بمعنی تواضع و چاپلوسی و انتظار هم آمده است'; 'بیوسنده ... امیدوار شده را نیز گویند'; 'بیوسیدن ... بمعنی امید داشتن و امیدوار گردیدن و طمع کردن'. Borhan gives no etymology here, only the glosses — which is all Nourai cites it for.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *baud1 (p.14)\", \"stance\": \"partial\",\n     \"note\": \"Cheung lists the Parthian and Manichaean MP inchoatives ('bws- ‘await, wait for, expect’') but does not carry the family into New Persian بیوسیدن, which he leaves unmentioned; his NP reflex of *baud1 is bōsīdan 'to kiss'.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.v. بیوسیدن\", \"stance\": \"supports\",\n     \"note\": \"MON_part1.txt line 35931 has the headword 'پبیوسیدن: [- بیوسیدن]' and line 37237 glosses a related lemma 'آرزومند کردن به امید افکندن؛ بیوسیدن' — Mo'in knows the verb with the same sense.\"},\n    {\"src\": \"HRN\", \"where\": \"Grundriss\", \"stance\": \"silent\",\n     \"note\": \"Horn has no entry for بیوس/بیوسیدن (grep of HRN.txt); only no. 240 bōi.\"}\n  ]\n },\n {\n  \"id\": 6, \"lang\": \"Sogdian\", \"words\": \"bws\",\n  \"verdict\": \"transcription_suspect\",\n  \"error_in\": \"book\",\n  \"book_prints\": \"bws\",\n  \"correct_form\": \"βwδ\",\n  \"derivation\": (\"The Sogdian word for 'incense' is βwδ (also spelled βwwδ, Christian Sogdian bwd), and it stands \"\n    \"on exactly the page Nourai cites: Gharib, Sogdian Dictionary p.113 no. 2878 'βwδ B, M (βwwδ, bwd) ⊙ < Av. \"\n    \"baoδa — incense', with no. 2879 βwδ- '(to) perfume, (to) smell' and, on the facing page, no. 2890 βwδδ \"\n    \"'incense, scent, perfume, olfaction' and no. 2896 βwδestān 'garden' (the exact Sogdian counterpart of \"\n    \"Persian بوستان). The derivation Nourai draws is therefore right — Sogdian βwδ continues the same \"\n    \"Old Iranian *baudi- as Avestan baoiδi-, Sogdian keeping the -δ- that Persian lost — but the FORM printed in \"\n    \"the chart, 'bws', is not a Sogdian word: -s is a misreading of -δ. I checked the printed page (pdf p.95, \"\n    \"book p.65): it does read 'bws', so the extraction is faithful and the slip is Nourai's own. (An 's' form does \"\n    \"exist in the family, but it is the compound verb Chr. Sogd. pcβws / M pt zβws 'to smell', Gharib nos. \"\n    \"6587/6600, not a simple noun.)\"),\n  \"derivation_fa\": (\"صورت سغدی درست βwδ (به \"\n    \"خط سغدی مسیحی bwd) به معنی \"\n    \"«بخور، عود» است و دقیقاً \"\n    \"در همان صفحهٔ ۱۱۳ فرهنگ \"\n    \"قریب (مدخل ۲۸۷۸) آمده است: \"\n    \"«βwδ < اوستایی baoδa». پس \"\n    \"ریشه‌شناسی نورایی \"\n    \"درست است — سغدی دال \"\n    \"میان‌واکه‌ای را نگاه \"\n    \"داشته در حالی که \"\n    \"فارسی آن را از دست \"\n    \"داده — اما صورت چاپی \"\n    \"«bws» نادرست است و s به جای \"\n    \"δ نشسته. تصویر صفحهٔ \"\n    \"چاپی (ص ۶۵ کتاب) را دیدم: \"\n    \"خود کتاب «bws» دارد؛ پس \"\n    \"خطای چاپی کتاب است نه \"\n    \"خطای خوانش اسکن.\"),\n  \"sources\": [],\n  \"ref_check\": [\n    {\"ref\": \"SOD:113\", \"status\": \"partial\",\n     \"note\": \"SOD_pages.txt leaf 178 carries the running head '113' and entry '2878 βwδ B, M (βwwδ, bwd) ⊙<Av. baoδa =>βwδδ, βwδh | incense | TSP 7.111, 112, 114; STii 3.66; C2 gloss.; BBB'. The page and the meaning are exactly right; only the transliteration in the chart is wrong (bws for βwδ).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"p. 114, nos. 2890, 2893, 2896\", \"stance\": \"supports\",\n     \"note\": \"'2890 βwδδ ... incense, scent, perfume, olfaction'; '2893 βwδ ... perfume, sense of smell, olfaction'; '2896 βwδestān (βwδstʼn) ... garden' — the Sogdian match of NP بوستان.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"s.v. *baud2, Sogdian section (p.16)\", \"stance\": \"supports\",\n     \"note\": \"'*SOGDIAN: BSogd. βwδ ‘to smell’ || (+ ? *pati-uz-) CSogd. pcβws, MSogd. ptzβws ‘to smell’' — the simplex is βwδ, the -s forms are prefixed verbs.\"},\n    {\"src\": \"BRT\", \"where\": \"col. 918\", \"stance\": \"supports\",\n     \"note\": \"Gharib's etymon 'Av. baoδa' is Bartholomae's baoδi-/baoδah- entry, the same Avestan word as in node 1.\"}\n  ]\n },\n {\n  \"id\": 7, \"lang\": \"Sanskrit\", \"words\": \"bŭdhati; bŭdha\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"The Sanskrit verb is real and is the classic witness for this root, but the standard citation forms \"\n    \"are bódhati / bódhate (class 1, guṇa grade) 'awakes, is awake, notices' and búdhyate (class 4) 'is awakened, \"\n    \"becomes aware' — Pokorny I 151: 'Themat. Präs. in ai. bódhati, bódhate „erwacht, erweckt, ist wach, merkt, \"\n    \"wird gewahr“'; Watkins gives 'Sanskrit bodhati, he awakes'. Nourai's 'bŭdhati' with short u is a zero-grade \"\n    \"spelling that no dictionary uses; it looks like a contamination with búdhyate. The second word, budha- 'wise, \"\n    \"intelligent, awake', is correct as printed. Both descend from *bʰewdʰ- with the regular Indo-Iranian *e > a \"\n    \"and *dʰ > dh.\"),\n  \"derivation_fa\": (\"فعل سنسکریت درست \"\n    \"است ولی صورت معیار آن \"\n    \"bódhati (با گُنَه) یا búdhyate است نه \"\n    \"«būdhati»؛ پوکورنی (ص ۱۵۱) \"\n    \"«ای. bódhati» می‌آورد و \"\n    \"واتکینز نیز bodhati. واژهٔ \"\n    \"دوم budha- «خردمند، آگاه» \"\n    \"درست است. هر دو از \"\n    \"*bʰewdʰ- با دگرگونی‌های \"\n    \"معمول هندوایرانی \"\n    \"(*e > a، *dʰ > dh) برآمده‌اند. پس \"\n    \"ادعا درست است و فقط \"\n    \"آوانگاری فعل \"\n    \"دقیق نیست.\"),\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewd%CA%B0-\", \"https://www.etymonline.com/word/Buddha\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins s.v. bheudh-, section 5: 'Sanskrit bodhati, he awakes, is enlightened, becomes aware, and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE.' Nourai's gloss 'he awakes' is Watkins' wording verbatim.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"printed pp. 151-152\", \"stance\": \"supports\",\n     \"note\": \"'Themat. Präs. in ai. bŏdhati, bŏdhate „erwacht, erweckt, ist wach, merkt, wird gewahr“ ... Partiz. buddhá- „er wacht, verständig; erkannt“ ... buddhi- f. „Einsicht, Verstand“'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann nos. 1266, 1551, 1875\", \"stance\": \"supports\",\n     \"note\": \"'bheudhó ... Skt. bódhami'; 'bhoudhos ‘awake; awakening’ ... Skt. bodháh ‘awake, aware; awakening’'; 'bhudhó ... Skt. búdhye, intr.; cf. budháh (‘wise’ ...)'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. Buddha / bid\", \"stance\": \"supports\",\n     \"note\": \"Klein s.v. Buddha: 'OI. buddhah, ‘awakened, enlightened’, pp. of bodhati, budhyate, ‘is awake, observes, understands’, fr. I.-E. base *bheudh-'.\"}\n  ]\n },\n {\n  \"id\": 8, \"lang\": \"Persian\", \"words\": \"bŭdâ\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"بودا is not an inherited Persian word but a name taken over from Sanskrit buddha- 'the \"\n    \"Awakened One' (past participle of budh-, not of the finite budhati that the chart draws the arrow from), so \"\n    \"the arrow is a borrowing, not a descent. The oldest Persian form of the name is not بودا at all but \"\n    \"بوداسف/بوداسپ — through Middle Persian and Manichaean transmission from Sanskrit \"\n    \"bodhisattva- — which is what Borhan-e Qate' has on the very page Nourai cites (p.313, s.v. بوتاسپ \"\n    \"'رک: بوداسپ'), where Mo'in's note explains it from 'Sanskrit buddha (بمعنی بیدار، \"\n    \"آگاه، باهوش، زرنگ و خردمند)' and identifies the man as \"\n    \"Siddhārtha Gautama, Śākyamuni. Modern Persian بودا is a nineteenth/twentieth-century re-borrowing \"\n    \"through European scholarship. Verdict: the ultimate source is right, the route is not drawn.\"),\n  \"derivation_fa\": (\"«بودا» واژه‌ای \"\n    \"موروثی نیست بلکه \"\n    \"وام‌واژه است از \"\n    \"سنسکریت buddha- «بیدارشده» \"\n    \"(اسم مفعول ریشهٔ budh-)، \"\n    \"نه از فعل budhati. صورت \"\n    \"کهن‌تر این نام در \"\n    \"فارسی «بوداسپ/بوداسف» \"\n    \"(از bodhisattva-) است که معین \"\n    \"در حاشیهٔ برهان \"\n    \"قاطع (ص ۳۱۳) آن را \"\n    \"شرح داده و صاحبش را \"\n    \"سیدّارته گوتمه \"\n    \"(شاکیامونی) دانسته \"\n    \"است. فرم «بودا» \"\n    \"وام‌گیری تازهٔ \"\n    \"سدهٔ اخیر از راه \"\n    \"زبان‌های اروپایی \"\n    \"است. پس اصل سخن \"\n    \"درست است ولی مسیر \"\n    \"وام‌گیری در نمودار \"\n    \"نیامده: با احتیاط \"\n    \"پذیرفتنی است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/Buddha\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:313\", \"status\": \"supports\",\n     \"note\": \"BQT_v1_pages.txt leaf 533 = printed p.313: 'بوتاسپ — رک: بوداسپ' with Mo'in's note 'سانسکرت buddha (بمعنی بیدار، آگاه، باهوش، زرنگ و خردمند). نام وی سدارته گوتمه Siddhārtha Gautama و مشهور است به ساکیامونی Śākyamuni'. The page supports the Sanskrit source but shows the Persian form as بوداسپ, not بودا.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. Buddha, bo tree\", \"stance\": \"supports\",\n     \"note\": \"'Buddha, n. ... OI. buddhah, ‘awakened, enlightened’, pp. of bodhati, budhyate'; and s.v. bo tree: 'Pali bodhi is rel. to OI. buddhah'.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Farsi, a'lam volumes\", \"stance\": \"silent\",\n     \"note\": \"The lexicon volumes digitised here (MON_part1/part2) carry no بودا headword; the name belongs to Mo'in's proper-name volumes (5-6), which are not in the local corpus.\"}\n  ]\n },\n {\n  \"id\": 9, \"lang\": \"English\", \"words\": \"Buddha\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"English Buddha (first recorded 1680s) is Sanskrit/Pali buddha- 'awakened, enlightened', the past \"\n    \"participle of budh- 'to wake, know, perceive' — the zero-grade *bʰudʰ-tó- of the same root, with the \"\n    \"regular Indic assimilation *dh + t > ddh. It entered English through the Latin transcriptions of Portuguese \"\n    \"and later British orientalists reporting on Ceylon and Burma, not through any intermediate European word. \"\n    \"Watkins puts BUDDHA under bheudh- section 5; Klein s.v. Buddha derives it from 'OI. buddhah ... fr. I.-E. base \"\n    \"*bheudh-'. The arrow Sanskrit → English is therefore right; strictly the base is buddha- (participle) rather \"\n    \"than the finite budhati in the parent box.\"),\n  \"derivation_fa\": (\"واژهٔ انگلیسی Buddha \"\n    \"(از دههٔ ۱۶۸۰ م.) مستقیماً \"\n    \"از سنسکریت/پالی buddha- \"\n    \"«بیدارشده، روشن‌شده» \"\n    \"گرفته شده که اسم \"\n    \"مفعول ریشهٔ budh- است \"\n    \"(صورت صفرمرتبهٔ \"\n    \"*bʰudʰ-tó- با همگونی dh+t > ddh). \"\n    \"واتکینز و کلاین هر دو \"\n    \"همین را می‌گویند. \"\n    \"ادعای نورایی درست \"\n    \"است؛ تنها باید \"\n    \"افزود که مأخذ مستقیم \"\n    \"صورت اسم مفعولی \"\n    \"buddha- است نه فعل budhati.\"),\n  \"sources\": [\"https://www.etymonline.com/word/Buddha\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins s.v. bheudh- 5: 'Sanskrit bodhati ... and bodhih, perfect knowledge: BUDDHA; BODHISATTVA, BO TREE.'; the AHD index line 'BuppHA bheudh-' (OCR for BUDDHA) confirms the cross-reference.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. Buddha\", \"stance\": \"supports\",\n     \"note\": \"'Buddha, n., incarnation of deified religious teachers, esp. of Gautama Siddharta (563-483). — OI. buddhah, ‘awakened, enlightened’, pp. of bodhati, budhyate ... fr. I.-E. base *bheudh-. See bid and cp. bo tree.'\"},\n    {\"src\": \"Etymonline\", \"where\": \"entry 'Buddha'\", \"stance\": \"supports\",\n     \"note\": \"'from Pali, literally ‘awakened, enlightened’, past participle of budh ‘to awake, know, perceive’, related to Sanskrit bodhati ‘is awake, observes, understands’ ... PIE root *bheudh- ‘be aware, make aware’; a title given to Siddhartha Gautama ... 1680s in English.'\"}\n  ]\n },\n {\n  \"id\": 10, \"lang\": \"Germanic\", \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Empty pass-through box: the Proto-Germanic stage between the root and English. The relevant \"\n    \"Germanic form is *beudaną 'to offer, proclaim, bid' (Gothic ana-biudan 'to command', faur-biudan 'to forbid', \"\n    \"Old Norse bjóða, Old Saxon biodan, Old High German biotan, Old English bēodan), with the noun *budą \"\n    \"'command' and *budilă 'herald'. PIE *bʰewdʰ- > PGmc *beud- by Grimm's Law (*bʰ > b, *dʰ > d) and the \"\n    \"regular *eu > eu. Watkins puts the whole Germanic branch under bheudh-; Pokorny lists it on p.152.\"),\n  \"derivation_fa\": (\"جعبهٔ خالیٔ گذری \"\n    \"است که مرحلهٔ \"\n    \"ژرمنی آغازین را \"\n    \"نشان می‌دهد: *beudaną \"\n    \"«پیشنهاد کردن، \"\n    \"اعلام کردن، فرمان \"\n    \"دادن» (گوتی ana-biudan، \"\n    \"faur-biudan؛ انگلیسی کهن \"\n    \"bēodan). دگرگونی آوایی \"\n    \"طبق قانون گریم \"\n    \"(*bʰ > b، *dʰ > d) است. \"\n    \"پوکورنی (ص ۱۵۲) و \"\n    \"واتکینز هر دو \"\n    \"همین را دارند؛ \"\n    \"درست است.\"),\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewd%CA%B0-\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins s.v. bheudh-: '1. Germanic *(for)beudan (*for, before; see per1) in: a. Old English bēodan, to proclaim: BID; b. Old English forbēodan, to forbid: FORBID ... 2. Germanic *budon- ... 3. Germanic *budilaz, herald ... 4. Germanic *budam in Old Norse bodh, command: OMBUDSMAN.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"printed p. 152\", \"stance\": \"supports\",\n     \"note\": \"'got. anabiudan „befehlen, anordnen“, faurbiudan „verbieten“, aisl. bjŏða ..., ags. beodan, as. biodan, ahd. biotan „bieten, darbieten“'.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann no. 1266\", \"stance\": \"supports\",\n     \"note\": \"'Go. cf. ana-, faür-biudan; OHG biotan; OE beodan ‘declare; order’; ON bjóða ‘offer’; OFris. biada'.\"}\n  ]\n },\n {\n  \"id\": 11, \"lang\": \"English\", \"words\": \"bid, forbid\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"forbid is straightforwardly from this root: Old English forbēodan (for- + bēodan 'to proclaim, \"\n    \"command') > ME forbeden > forbid; cf. Gothic faur-biudan, German verbieten. bid, however, is a merger of two \"\n    \"different Old English verbs: bēodan 'to offer, proclaim' (< *bʰewdʰ-, this root, whence the auction sense \"\n    \"'to bid') and biddan 'to ask, entreat, pray' (< PIE *gʰedʰ- / *bʰedʰ-, whence also bead, and Greek \"\n    \"πείθω in Klein's older analysis), whence the sense 'to bid farewell'. Both AHD's own index ('BID bheudh-, \"\n    \"ghedh-') and Klein ('bid ... Prob. a blend of ME. bidden (fr. OE. biddan) and ME. beden (fr. OE. beodan)') say \"\n    \"so. So the box is half right: forbid confirmed, bid only partly from this root.\"),\n  \"derivation_fa\": (\"forbid بی‌گمان از همین \"\n    \"ریشه است: انگلیسی \"\n    \"کهن forbēodan (for- + bēodan). اما bid \"\n    \"حاصل درهم‌آمیزی \"\n    \"دو فعل جداگانهٔ \"\n    \"انگلیسی کهن است: \"\n    \"bēodan «پیشنهاد کردن» \"\n    \"(از همین ریشه، معنی \"\n    \"«پیشنهاد قیمت») و \"\n    \"biddan «خواستن، دعا \"\n    \"کردن» (از *gʰedʰ-، معنی \"\n    \"«bid farewell»). خود نمایهٔ \"\n    \"واتکینز نیز bid را \"\n    \"زیر دو ریشه می‌آورد. \"\n    \"پس این جعبه نیمه \"\n    \"درست است و با احتیاط \"\n    \"پذیرفتنی.\"),\n  \"sources\": [\"https://www.etymonline.com/word/bid\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"The node carries no reference in the book (refs=None); the parent Germanic box cites AHD, which does list BID and FORBID under bheudh- but also, in its own index, BID under ghedh-.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"s.v. bid\", \"stance\": \"partial\",\n     \"note\": \"'bid, tr. and intr. v. — Prob. a blend of ME. bidden (fr. OE. biddan), ‘to ask’, and ME. beden (fr. OE. beodan) ‘to announce, proclaim, offer’ ... OE. beodan is rel. to ... Goth. faur-biudan, ‘to forbid’, fr. I.-E. base *bheudh-, ‘to offer, present’ ... Cp. beadle, bode, forbid, Buddha.'\"},\n    {\"src\": \"SKT\", \"where\": \"s.v. Forbid\", \"stance\": \"supports\",\n     \"note\": \"Skeat: 'Forbid. (E.) From For- (a) and Bid (a). A.S. forbeodan. + G. verbieten.'\"},\n    {\"src\": \"AHD\", \"where\": \"index\", \"stance\": \"partial\",\n     \"note\": \"AHD_watkins1985.txt index line: 'BID bheudh-, ghedh-' — two roots for the one word; 'FORBID bheudh-' has only one.\"},\n    {\"src\": \"Etymonline\", \"where\": \"entry 'bid'\", \"stance\": \"partial\",\n     \"note\": \"'a merger of two Old English verbs ... biddan ‘to ask, entreat, beg, pray’ (PIE root *gʷhedh-) and beodan ‘offer, proclaim’ (PIE root *bheudh-) ... probably an early Middle English mutual influence or confusion of two older words.'\"}\n  ]\n }\n]\n\njson.dump(e0, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e0.95.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e0[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk95.py"
}
```


### [2026-09-05T14:34:56.131Z] TOOL RESULT

```
ok 11
```


## [2026-09-05T14:37:58.101Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk95b.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW = \"https://en.wiktionary.org/wiki/\"\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Bheug, Bheugh\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *bʰewg- 'to clear away, free, save; to flee, escape' (Pokorny 2. bheug-, bheugh- p.152)\",\n \"note\": (\"Pokorny I 152 has, one after the other, '1. bheug- „fliehen“, nach Kretschmer (Gl. 30, 138) zu 2. \"\n   \"bheug(h)- (av. baog- in der intransitiven Bedeutung „sich retten“)' and '2. bheug-, bheugh- „wegtun, reinigen, \"\n   \"befreien“; intrans. „sich retten“'. Nourai's root name (both variants g/gh), his language label and his gloss \"\n   \"'to purify, save, free' are Pokorny's 2. bheug- word for word, and his page number 152 is exactly right — it is \"\n   \"also the page of 1. bheug- 'to flee', which is why the Latin branch can carry the same citation. Nourai treats \"\n   \"the two as one root; Pokorny keeps them apart but himself reports Kretschmer's identification, and modern \"\n   \"handbooks side with Nourai: LIV 84 and Cheung (*bauj2) set up a single *bʰeug- 'to release, flee', citing Gr. \"\n   \"pheugō, Lat. fugiō alongside Av. būj-, and Wiktionary's *bʰewg- 'to flee, escape' lists Av. būj-, MP bōxtan and \"\n   \"Lat. fūgī together. AHD/Watkins, which has no Iranian material, still separates bheug-1 'to flee' from \"\n   \"bheug-3 'to bend' and has no 'purify' root at all.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی \"\n   \"آغازین *bʰewg- «رها کردن، \"\n   \"آزاد کردن، رهانیدن؛ \"\n   \"گریختن». پوکورنی در \"\n   \"ص ۱۵۲ دو مدخل پشت \"\n   \"سر هم دارد: «۱. bheug- \"\n   \"گریختن» و «۲. bheug-, bheugh- \"\n   \"دور کردن، پاک کردن، \"\n   \"رهانیدن»، و خودش از \"\n   \"قول کرچمر یکی بودن \"\n   \"آن‌ها را ممکن \"\n   \"می‌داند. نام ریشه، \"\n   \"برچسب زبانی و \"\n   \"معنایی که نورایی \"\n   \"آورده عیناً همان \"\n   \"مدخل دوم پوکورنی \"\n   \"است و شمارهٔ صفحه \"\n   \"نیز درست. یکی \"\n   \"گرفتن دو ریشه که \"\n   \"نورایی کرده، امروز \"\n   \"پذیرفته است: LIV ۸۴، \"\n   \"چونگ (زیر *bauj²) و \"\n   \"ویکی‌واژه هر سه \"\n   \"لاتینی fugiō و \"\n   \"اوستایی būj- را زیر \"\n   \"یک ریشه می‌آورند. \"\n   \"پس ادعای نورایی \"\n   \"درست است.\"),\n \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewg-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:152\", \"status\": \"supports\",\n    \"note\": \"POK_01.txt leaf 161, printed p.152: '2. bheug-, bheugh- „wegtun, reinigen, befreien“; intrans. „sich retten“. Av. baog-, bunja- „lösen, retten, sich retten vor“ ... baoxtar- „Befreier“; pehl. paz. bōxtan „retten, erlösen“ ... WP. II 145'. Nourai's gloss is a translation of Pokorny's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 144-145\", \"stance\": \"supports\",\n    \"note\": \"WLD_Bd2_pages.txt line 9328 running head '144 bheug-', line 9381 '1. bheug- „fliehen“, von Fick I3 490 von bheug(h)- „biegen“ getrennt', line 9396 running head 'bheug(h) — bheug-, bheugh- 145'. Walde-Pokorny already discusses whether the 'flee' and 'free' roots are one.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins s.v. bheug-1, bheug-2, bheug-3\", \"stance\": \"partial\",\n    \"note\": \"'bheug-1. To flee ... Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE ... [Pok. 1. bheug- 152.]'; 'bheug-2. To enjoy ... [Pok. 4. bheug- 153.]'; 'bheug-3. To bend ... [Pok. 3. bheug- 152.]'. Watkins has no root meaning 'to purify, save, free' — the Iranian branch is simply absent from his English-oriented list.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"s.v. *bauj2 (pp. 18-19)\", \"stance\": \"supports\",\n    \"note\": \"'*bauj2 ‘to release, free, open; to save, deliver’ ... «PIE *bʰeug- ‘to release, flee’ => LIV: 84 | Pok.: 152 ... *IE COGNATES: Gr. φεύγω, Lat. fugio ‘I flee’, Goth. us-baugjan ‘to wipe off’' — Cheung unites exactly the two branches Nourai draws.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann nos. 1268, 1879\", \"stance\": \"partial\",\n    \"note\": \"'bheugo (bhoug-) ‘flee’. WP II, 144 ... Gk. pheügo; Lat. cf. fügi'; and 'bhugo ... ‘bend, turn, flee’'. Mann has the 'flee' root but no separate 'purify, free' entry.\"}\n ],\n \"nodes\": [\n  {\n   \"id\": 1, \"lang\": \"Avestan\", \"words\": \"baog, bunja; baoxtar\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": (\"Young Avestan baog- / būj- 'to loose, free, save', present stem bunja- with the nasal infix \"\n     \"(bunjainti 'they rescue' Yt 14.46, bunjayāt 'let him save' V 7.71, būjat Yt 4.3), and the agent noun baoxtar- \"\n     \"m. 'saviour, deliverer' (Vr 7.3), formed with the Indo-Iranian -tar- suffix on the zero-grade with the \"\n     \"regular *g + t > xt. PIE *bʰewg- > Proto-Iranian *bauǰ- (the palatal g of the satem languages), Av. ao for \"\n     \"*au. Pokorny p.152 lists all of these under 2. bheug-; Bartholomae cols. 916-917 gives the paradigm and the \"\n     \"senses '(den Gürtel) lösen', 'befreien, retten', 'sich retten vor'.\"),\n   \"derivation_fa\": (\"اوستایی baog-/būj- «گشودن، \"\n     \"رهانیدن، نجات دادن» با \"\n     \"ستاک حال میان‌وند‌دار \"\n     \"bunja- (bunjainti «می‌رهانند») و \"\n     \"اسم فاعل baoxtar- «رهاننده، \"\n     \"نجات‌بخش» با پسوند \"\n     \"هندوایرانی ‌tar- که در \"\n     \"آن g + t به xt بدل شده است. \"\n     \"از هندواروپایی *bʰewg- به \"\n     \"ایرانی باستان *bauǰ-. \"\n     \"پوکورنی (ص ۱۵۲) و \"\n     \"بارتولومه (ستون‌های \"\n     \"۹۱۶–۹۱۷) هر دو همین را \"\n     \"دارند؛ ادعای نورایی \"\n     \"درست است.\"),\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewg-\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:152\", \"status\": \"supports\",\n      \"note\": \"Printed p.152: 'Av. baog-, bunja- „lösen, retten, sich retten vor“ (bunjainti „sie befreien, retten“, būjayamnō „ablegend“, bunjayāt „er rette“), būjim Akk. „Reinigung“, ązō-buj- „aus Not befreiend“, baoxtar- „Befreier“'.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"cols. 916-917\", \"stance\": \"supports\",\n      \"note\": \"'j. baog- V. „lösen“. Praes. 3 būja-, 9 bunja-, 24 būjaya-, 94-24 bunjaya- ... 2) „befreien, retten“ ... mp. bōxtan, sbal. bōj-'; and 'j. baoxtar- m. „Retter, Befreier“ ... Zum V. baog-; — mp. bōxtār'.\"},\n     {\"src\": \"CHEUNG\", \"where\": \"s.v. *bauj2, Avestan section\", \"stance\": \"supports\",\n      \"note\": \"'*AVESTAN: YAv. būj- (bunj-) ‘to save, redeem’ ... Pres. {1} n-: IND. 3pl. YAv. bunjainti (Yt 14.46) ... Pres. {2} them.: INJ. 3sg. YAv. būjat (Yt 4.3)'.\"},\n     {\"src\": \"KNT\", \"where\": \"Lexicon p.198\", \"stance\": \"supports\",\n      \"note\": \"'baug- vb. ‘free’: Av. baog-, NPers. bōxtan; in Aθiyābaušna-, Bagabuxša-.'\"}\n   ]\n  },\n  {\n   \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"bôxtan; bôzišn\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": (\"Middle Persian bōxtan, present stem bōz- 'to save, redeem' ⟨bwhtnʹ, bwc-⟩, Manichaean MP \"\n     \"⟨bwxtn, bwz-⟩; the past stem bōxt continues Old Iranian *bauxta- < *baug-ta- (*g + t > xt, exactly as in \"\n     \"Avestan baoxtar-), while bōz- is the present *bauǰa-. The verbal noun bōzišn is 'salvation' and, in the \"\n     \"everyday register, 'apology' — MacKenzie prints '—išn [-# | J bwzyšn, N pōzis] salvation; apology', i.e. he \"\n     \"himself gives the New Persian continuation of this very word, which is the next box in the chart. Pokorny \"\n     \"p.152 cites 'pehl. paz. bōxtan „retten, erlösen“'.\"),\n   \"derivation_fa\": (\"فارسی میانه bōxtan (ستاک \"\n     \"حال bōz-) «رهانیدن، نجات \"\n     \"دادن»؛ ستاک گذشتهٔ bōxt \"\n     \"از ایرانی باستان *bauxta- < \"\n     \"*baug-ta- است (g + t > xt، همان \"\n     \"دگرگونی که در baoxtar- \"\n     \"اوستایی دیده می‌شود) و \"\n     \"ستاک حال از *bauǰa-. اسم \"\n     \"مصدر bōzišn هم «رستگاری» \"\n     \"و هم «پوزش» معنی می‌دهد؛ \"\n     \"مکنزی خود می‌نویسد: \"\n     \"«bōzišn … salvation; apology» و \"\n     \"دنبالهٔ فارسی نو آن را \"\n     \"pōzis می‌آورد. نیبرگ نیز \"\n     \"buxtan/bōž- را با ارجاع به \"\n     \"اوستایی baog- دارد. \"\n     \"ادعای نورایی درست است.\"),\n   \"sources\": [W + \"%D9%BE%D9%88%D8%B2%D8%B4\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:152\", \"status\": \"supports\",\n      \"note\": \"Printed p.152: 'pehl. paz. bōxtan „retten, erlösen“, südbal. bōjag „öffnen, lösen, losbinden“, als pers. Lw. arm. buzem „heile, rette, befreie“'.\"},\n     {\"ref\": \"SNS:106\", \"status\": \"partial\",\n      \"note\": \"Tavoosi's Shayast ne Shayast glossary: the word index (SNS_pages.txt leaf 237) lists 'bōxt 105/23, bōxtišn 106/2, bōxtan 106/5, bōzišnīgtar 108/2', and the glossary entry itself (leaf 69) analyses 'bōzišn = bōz + -išn' citing Ghilain 63 and Mir.Man. II 48 'bwzyšn'. The forms and the numbers 106/107 match Nourai's citation, but the OCR of the Persian is too poor to fix the printed page, and Nourai's numbers may be the text's chapter/line references rather than glossary pages.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 p.19 s.v. bōxtan\", \"stance\": \"supports\",\n      \"note\": \"'bōxtan, bōz- [bwhtnʹ, bwc- | M bwxtn, bwz-] save, redeem. —išn [-# | J bwzyšn, N pōzis] salvation; apology.'\"},\n     {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, Glossary s.v. buxtan\", \"stance\": \"supports\",\n      \"note\": \"'buxtan [bwhtnʹ] bōž- [bwc-], to save, to preserve ... Av. (916 sq.) baog-; Ps. bwhty, bwc-; MPrthPrs bwxtn, pres. MPrth bwž-, bwxs-, MPrs bwz-; Arm. lw. bužem; Paz. bōxtan, buxtan, bōž-. — V. bōžišn.'\"},\n     {\"src\": \"CHEUNG\", \"where\": \"s.v. *bauj2, Middle Persian section\", \"stance\": \"supports\",\n      \"note\": \"'*MIDDLE PERSIAN: MMP bwz-, BMP bwc- /bōz-/ ‘to free, to release’, MMP bwxs- (inch.) ‘to be saved’ => DMMPP: 119a'.\"}\n   ]\n  },\n  {\n   \"id\": 3, \"lang\": \"Persian\", \"words\": \"boxt; pŭzîdan\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": (\"بُخت (the second homonym, distinct from بخت 'fortune' < *baxta- 'apportioned', which belongs to \"\n     \"baxš-/bhag-) is the New Persian past stem/participle of the obsolete verb بختن/بوختن 'to save, rescue, \"\n     \"redeem' = MP bōxt; Wiktionary lemmatises it as Classical Persian بختن (buxtan) 'to save, rescue, redeem' \"\n     \"under PIE *bʰewg-. پوزیدن and its verbal noun پوزش go back to MP bōzišn 'salvation; apology' (MacKenzie), \"\n     \"with the regular devoicing of the initial b- to p- that Middle Persian /b/ often shows in this word \"\n     \"(MacKenzie writes the New Persian outcome pōzis himself); Wiktionary s.v. پوزش: 'from Middle Persian \"\n     \"bōzišn ‘salvation; apology’, verbal noun of bōxtan, bōz- ‘to save, to redeem’, ultimately from PIE *bʰewg-'. \"\n     \"Mo'in has both پوزش '(اسم مصدر پوزیدن) عذرخواهی، \"\n     \"معذرت‌خواهی' and پوزیدن 'معذرت خواستن، عذر \"\n     \"خواستن'. One caveat on the chart's cross-reference line: of the two extra headwords printed under the box, \"\n     \"پوزش belongs here, but پوز 'snout, muzzle' (Mo'in: پیرامون دهان، گرداگرد دهن \"\n     \"حیوانات; whence پوزه) is an unrelated homonym and does not descend from bōzišn.\"),\n   \"derivation_fa\": (\"«بُخت ۲» ستاک گذشتهٔ \"\n     \"فعل متروک «بختن/بوختن» \"\n     \"به معنی «رهانیدن، نجات \"\n     \"دادن» است و با «بخت» به \"\n     \"معنی «طالع» (از *baxta- «بخش‌شده») \"\n     \"هم‌آوا ولی بی‌ارتباط. \"\n     \"«پوزیدن» و «پوزش» از \"\n     \"فارسی میانهٔ bōzišn «رستگاری؛ \"\n     \"پوزش» آمده‌اند؛ ابدال ب \"\n     \"آغازی به پ در همین واژه \"\n     \"رخ داده و مکنزی خود \"\n     \"صورت فارسی نو را pōzis \"\n     \"می‌نویسد. معین هر دو \"\n     \"مدخل پوزش و پوزیدن را \"\n     \"با همین معنی دارد و \"\n     \"ویکی‌واژه نیز پوزش را \"\n     \"از bōzišn می‌گیرد. \"\n     \"ادعای نورایی درست است؛ \"\n     \"تنها یادداشت: از دو \"\n     \"سرواژهٔ افزودهٔ زیر \"\n     \"جعبه، «پوزش» به این \"\n     \"خانواده تعلق دارد اما \"\n     \"«پوز» (پیرامون دهان، \"\n     \"پوزه) واژه‌ای جداگانه \"\n     \"و بی‌ربط است.\"),\n   \"sources\": [W + \"%D9%BE%D9%88%D8%B2%D8%B4\", W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewg-\"],\n   \"ref_check\": [\n     {\"ref\": \"SNS:96,106,107\", \"status\": \"partial\",\n      \"note\": \"Tavoosi's glossary index has 'baxt 97/10-11', 'bōxt 105/23', 'bōxtišn 106/2', 'bōxtan 106/5', 'bōzišnīgtar 108/2' (SNS_pages.txt leaf 237) and the glossary discusses bōzišn (leaf 69, citing Ghilain 63). The Pahlavi material Nourai points to is there; the exact printed pages could not be fixed because the Persian OCR of this scan is unusable and the offset is undetermined.\"},\n     {\"ref\": \"MON:476\", \"status\": \"partial\",\n      \"note\": \"Mo'in's Farhang-e Farsi has the entries — MON_part1.txt line 33174 ff.: 'پوزش (امص. پوزیدن) عذرخواهی، معذرت‌خواهی، درخواست عفو. عذر، معذرت' and 'پوزیدن [ستاک: پوز] (مص‌ل.) ... زدودن، راندن، برطرف کردن(۲). معذرت خواستن، عذر خواستن' — but the local digitisation of Mo'in has no page breaks, so p.476 could not be verified as such.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"PHD\", \"where\": \"MacKenzie 1971 s.v. bōxtan\", \"stance\": \"supports\",\n      \"note\": \"'—išn [-# | J bwzyšn, N pōzis] salvation; apology' — MacKenzie's own New Persian equivalent of bōzišn is پوزش, exactly Nourai's arrow.\"},\n     {\"src\": \"CHEUNG\", \"where\": \"s.v. *bauj2, NWIr section\", \"stance\": \"partial\",\n      \"note\": \"Cheung lists Bal. bōtk/bōj- 'to open', Kurd. (Sor.) būžānawa 'to revive' and '? NP buzīdan/buz- ‘to pluck off hair, wool’ (LW)' but does not mention NP بخت or پوزیدن; silent rather than contradicting.\"},\n     {\"src\": \"MON\", \"where\": \"Farhang-e Farsi s.vv. پوزش، پوزیدن، پوزه\", \"stance\": \"supports\",\n      \"note\": \"Mo'in has پوزش and پوزیدن as above, and separately 'پوزه [- پوز] پیرامون دهان، گرداگرد دهن حیوانات' — confirming that پوز 'muzzle' is a different word from پوزش.\"},\n     {\"src\": \"NYB\", \"where\": \"Glossary s.v. buxtan\", \"stance\": \"supports\",\n      \"note\": \"'Paz. bōxtan, buxtan, bōž-' — the Pāzand shapes underlying NP بختن/بخت.\"}\n   ]\n  },\n  {\n   \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"baug; baga-buxša\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": (\"Kent's Old Persian lexicon has the root as 'baug- vb. ‘free’: Av. baog-, NPers. bōxtan; in \"\n     \"Aθiyābaušna-, Bagabuxša-' (p.198) and, on the page Nourai cites, the name itself: 'Bagabuxša- sb. \"\n     \"‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-ša, Akk. ba-ga-bu-ki-šu, Gk. Μεγάβυζος. \"\n     \"From baga- ‘god’ + deriv. of root baug- ‘free’: ‘God-freed’' (p.199, DB 4.85). The second member is a \"\n     \"*-sa- derivative *bug-sa- > buxša- (velar + s > xš), the same formation as in Aθiyābaušna-. The verbal root \"\n     \"itself is not attested as a finite Old Persian verb — Kent lists it only as the base of these two names — so \"\n     \"'baug : to set free' is a root citation rather than a word, which is normal practice. The Greek rendering \"\n     \"Μεγάβυζος shows the Iranian -xš- as -z-. The cross-reference to the root Bhag for baga- is correct \"\n     \"(Kent: 'baga- sb. ‘god’ ... pIE *bhago-').\"),\n   \"derivation_fa\": (\"در فرهنگ کنت ریشهٔ \"\n     \"پارسی باستان چنین \"\n     \"آمده است: «baug- فعل «آزاد \"\n     \"کردن»: اوستایی baog-، فارسی \"\n     \"نو bōxtan؛ در Aθiyābaušna- و \"\n     \"Bagabuxša-» (ص ۱۹۸)، و در \"\n     \"همان صفحهٔ ۱۹۹ که نورایی \"\n     \"ارجاع داده: «Bagabuxša- «مگابیزوس»، \"\n     \"از یاران داریوش … از baga- \"\n     \"«خدا» + مشتق ریشهٔ baug- \"\n     \"«آزاد کردن»: «رهاشده به \"\n     \"دست خدا»». جزء دوم مشتق \"\n     \"*bug-sa- است که در آن g + s به \"\n     \"xš بدل شده. خود فعل در \"\n     \"کتیبه‌ها صیغهٔ صرف‌شده \"\n     \"ندارد و تنها در این دو \"\n     \"نام دیده می‌شود. ارجاع \"\n     \"نورایی به ریشهٔ Bhag برای \"\n     \"baga- نیز درست است. \"\n     \"ادعای نورایی درست است.\"),\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewg-\"],\n   \"ref_check\": [\n     {\"ref\": \"KNT:199\", \"status\": \"supports\",\n      \"note\": \"KNT.txt leaf 223 = printed p.199 (leaf 221 carries the running head '197'): 'Bagabuxša- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-ša, Akk. ba-ga-bu-ki-šu, Gk. Μεγάβυζος. From baga- ‘god’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Ic). Bagabuxša nsm. DB 4.85.' The root entry 'baug- vb. ‘free’' stands on p.198, the facing page.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BRT\", \"where\": \"s.v. p. dāduhya- / bagabuxša-\", \"stance\": \"supports\",\n      \"note\": \"Bartholomae s.v. 'p. dāduhya- m. EN. eines Persers: bagabuxša nāma °hyahyā puça pārsa Bh. 4.85', and under baog-: 'Eig. „von Gott befreit, erlöst“; -buxša- m., zum V. baog-; vgl. Yt 14.46'.\"},\n     {\"src\": \"CHEUNG\", \"where\": \"s.v. *bauj2\", \"stance\": \"partial\",\n      \"note\": \"Cheung's *bauj2 covers the same root but has no Old Persian section (the OP evidence is onomastic only); he cites Bal. busk- (inch.) < *buxsa-, the same *-sa- formation as OP buxša-.\"},\n     {\"src\": \"TLM\", \"where\": \"Ancient Persian Lexicon\", \"stance\": \"silent\",\n      \"note\": \"Grep of TLM.txt for 'buxša'/'Bagabuxsa' returns nothing usable in this OCR.\"}\n   ]\n  },\n  {\n   \"id\": 5, \"lang\": \"None\", \"words\": \"\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": (\"Empty box. On the printed page (pdf 95, book p.65) an arrow leaves the Old Persian box and ends \"\n     \"in an empty framed box in the Persian column, with no language label, no reference and no words — the \"\n     \"Persian reflex slot was left blank in the book. Nothing to verify; had it been filled, the expected content \"\n     \"would be the Persian form of the name Bagabuxša (Greek Megabyzus), which survives only in classical \"\n     \"transmission, not in New Persian.\"),\n   \"derivation_fa\": (\"جعبهٔ خالی. در صفحهٔ \"\n     \"چاپی (ص ۶۵ کتاب) پیکانی \"\n     \"از جعبهٔ پارسی باستان \"\n     \"به یک قاب خالی در ستون \"\n     \"فارسی می‌رود که نه \"\n     \"برچسب زبان دارد نه \"\n     \"واژه و نه ارجاع؛ \"\n     \"یعنی جای بازتاب \"\n     \"فارسی در کتاب \"\n     \"خالی مانده است. \"\n     \"چیزی برای داوری \"\n     \"نیست؛ اگر پر می‌شد، \"\n     \"انتظار می‌رفت صورت \"\n     \"فارسی نام Bagabuxša \"\n     \"(یونانی Megabyzus) در آن \"\n     \"بیاید که در فارسی نو \"\n     \"بازمانده‌ای ندارد.\"),\n   \"sources\": [],\n   \"ref_check\": [\n     {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The box carries no reference and no content in the book.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"BOOK\", \"where\": \"printed page 65 (pdf 95), copied to data/verification/sources/refs/ocr/BOOK/95.png\", \"stance\": \"silent\",\n      \"note\": \"The page image confirms the box is genuinely empty in the book — this is not an extraction loss.\"},\n     {\"src\": \"KNT\", \"where\": \"Lexicon p.199\", \"stance\": \"silent\",\n      \"note\": \"Kent gives no New Persian continuation of Bagabuxša-; only the Elamite, Akkadian and Greek renderings.\"}\n   ]\n  },\n  {\n   \"id\": 6, \"lang\": \"Latin\", \"words\": \"fugere\",\n   \"verdict\": \"plausible\",\n   \"derivation\": (\"Latin fugiō, fugere 'to flee, run away', perfect fūgī, noun fuga 'flight', from Proto-Italic \"\n     \"*fugjō < PIE *bʰug-ie/o-, the zero grade of *bʰewg- (*bʰ- > Latin f- word-initially), with Greek φεύγω \"\n     \"'I flee', ἔφυγον and Lithuanian bū́gti 'to take fright' as the closest cognates. Whether this is the SAME \"\n     \"root as the Iranian 'free, save' word is the one open question on this chart. Pokorny prints them as \"\n     \"separate entries 1. and 2. bheug- on p.152, but adds under 1.: 'nach Kretschmer (Gl. 30, 138) zu 2. bheug(h)- \"\n     \"(av. baog- in der intransitiven Bedeutung „sich retten“)'. Cheung's *bauj2 'to release, free; to save, \"\n     \"deliver' gives 'PIE *bʰeug- ‘to release, flee’ => LIV: 84' with 'Gr. φεύγω, Lat. fugio' as its IE cognates, \"\n     \"and Wiktionary's *bʰewg- 'to flee, escape' lists Av. būj-, MP bōxtan and Lat. fūgī in one entry. So modern \"\n     \"scholarship largely agrees with Nourai; Watkins/AHD, however, keeps bheug-1 'to flee' as a self-standing \"\n     \"root. Marked plausible rather than confirmed because the identification is an accepted-by-most, not a \"\n     \"unanimous, position.\"),\n   \"derivation_fa\": (\"لاتینی fugiō/fugere «گریختن»، \"\n     \"ماضی fūgī، از ایتالیک \"\n     \"آغازین *fugjō و آن از \"\n     \"صورت صفرمرتبهٔ *bʰug-ie/o- \"\n     \"(ب دمیدهٔ آغازی در لاتینی \"\n     \"به f بدل می‌شود)، هم‌ریشه \"\n     \"با یونانی φεύγω و لیتوانیایی \"\n     \"bū́gti. تنها پرسش باز این \"\n     \"نمودار همین است که آیا \"\n     \"این ریشه با ریشهٔ ایرانی \"\n     \"«رهانیدن» یکی است یا نه. \"\n     \"پوکورنی آن‌ها را در ص ۱۵۲ \"\n     \"جدا آورده ولی خود از قول \"\n     \"کرچمر یکی بودنشان را \"\n     \"ممکن دانسته؛ چونگ و LIV \"\n     \"و ویکی‌واژه یکی \"\n     \"می‌گیرند و لاتینی fugiō را \"\n     \"در کنار اوستایی būj- \"\n     \"می‌نشانند؛ واتکینز \"\n     \"جدا نگه می‌دارد. پس \"\n     \"ادعای نورایی «با احتیاط \"\n     \"پذیرفتنی» است.\"),\n   \"sources\": [W + \"Reconstruction:Proto-Indo-European/b%CA%B0ewg-\", \"https://www.etymonline.com/word/fugitive\"],\n   \"ref_check\": [\n     {\"ref\": \"POK:152\", \"status\": \"supports\",\n      \"note\": \"Printed p.152: '1. bheug- „fliehen“ ... Gr. φεύγω (Aor. ἔφυγον, Perf. πέφευγα) „fliehe“ ... lat. fugiō, fūgī, -ere „fliehe, enteile, verschmähe“, fuga f. „Flucht“ ... WP. II 144, 146, WH. I 556 f., Kretschmer Gl. 30, 138.' The page is right; the sub-entry number is 1., not the 2. that the root box of this chart translates.\"},\n     {\"ref\": \"AHD\", \"status\": \"partial\",\n      \"note\": \"Watkins: 'bheug-1. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE ... [Pok. 1. bheug- 152.]' — supports the Latin words but keeps this as its own root, not as the 'purify, save, free' root of the box above.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"CHEUNG\", \"where\": \"s.v. *bauj2, PIE line\", \"stance\": \"supports\",\n      \"note\": \"'«PIE *bʰeug- ‘to release, flee’ => LIV: 84 | Pok.: 152 | *IE COGNATES: Gr. φεύγω, Lat. fugio ‘I flee’, Goth. us-baugjan ‘to wipe off’'.\"},\n     {\"src\": \"IEC\", \"where\": \"Mann no. 1268\", \"stance\": \"partial\",\n      \"note\": \"'bheugo (bhoug-) ‘flee’. WP II, 144 ... Gk. pheügo; Lat. cf. fügi; W cf. buan; Li. baugùs ‘frightened’' — Mann too has only the 'flee' sense for this etymon.\"},\n     {\"src\": \"WLD\", \"where\": \"Bd. II 144\", \"stance\": \"partial\",\n      \"note\": \"'1. bheug- „fliehen“, von Fick I3 490 von bheug(h)- „biegen“ getrennt, aber ...' — Walde-Pokorny debate the unification with 'bend', and on p.145 with 'reinigen, befreien'.\"}\n   ]\n  },\n  {\n   \"id\": 7, \"lang\": \"English\", \"words\": \"fugitive, centrifugal, refuge\",\n   \"verdict\": \"confirmed\",\n   \"derivation\": (\"All three are Latinate, not inherited. fugitive: Latin fugitīvus 'fleeing', past-participial \"\n     \"adjective to fugere, > Old French fugitif > Middle English fugitif (late 14th c.). refuge: Latin refugium \"\n     \"'a place to flee back to' (re- + fugere) > Old French refuge > English (late 14th c.). centrifugal: coined \"\n     \"in Neo-Latin by Isaac Newton (centrifugus, 1687, Principia) from centrum + fugere, 'fleeing the centre'. \"\n     \"Watkins lists FUGITIVE, CENTRIFUGAL and REFUGE together under bheug-1; Etymonline gives the same chain word \"\n     \"for word. Nothing controversial here.\"),\n   \"derivation_fa\": (\"هر سه واژه از راه \"\n     \"لاتینی به انگلیسی \"\n     \"رسیده‌اند نه از راه \"\n     \"موروثی: fugitive از لاتینی \"\n     \"fugitīvus (اسم مفعول fugere) \"\n     \"از راه فرانسویِ کهن \"\n     \"fugitif در سدهٔ چهاردهم؛ \"\n     \"refuge از لاتینی refugium «جای \"\n     \"پناه بردن» (re- + fugere)؛ و \"\n     \"centrifugal ساختهٔ نیوتن \"\n     \"در لاتینی نو (centrifugus، \"\n     \"۱۶۸۷ م.) از centrum + fugere. \"\n     \"واتکینز هر سه را زیر \"\n     \"bheug-¹ آورده و \"\n     \"اتیمانلاین نیز همین \"\n     \"زنجیره را می‌دهد. \"\n     \"ادعای نورایی درست است.\"),\n   \"sources\": [\"https://www.etymonline.com/word/fugitive\"],\n   \"ref_check\": [\n     {\"ref\": \"AHD\", \"status\": \"supports\",\n      \"note\": \"Watkins s.v. bheug-1: 'Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE'; the index lines 'CENTRIFUGAL bheug-1' and 'FEVERFEW bheug-1' confirm it.\"}\n   ],\n   \"consulted\": [\n     {\"src\": \"Etymonline\", \"where\": \"entry 'fugitive'\", \"stance\": \"supports\",\n      \"note\": \"'from Latin fugitivus ‘fleeing’, past-participle adjective from stem of fugere ‘to flee’ ... PIE root *bheug- ‘to flee’ ... Refuge: Old French refuge, Latin refugium, literally ‘a place of refuge, place to flee back to’ ... Centrifugal was coined by Isaac Newton from Latin centri- + fugere.'\"},\n     {\"src\": \"SKT\", \"where\": \"Skeat s.vv. fugitive, refuge\", \"stance\": \"supports\",\n      \"note\": \"Skeat derives both from Latin fugere through French, the standard account.\"}\n   ]\n  }\n ]\n}\njson.dump(e1, open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/e1.95.json','w'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(e1[\"nodes\"]))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk95b.py"
}
```


### [2026-09-05T14:38:02.049Z] TOOL RESULT

```
ok 7
```


## [2026-09-05T14:38:06.794Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nS=/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 - <<EOF\nimport json\ne0=json.load(open(\"$S/e0.95.json\"))\ne1=json.load(open(\"$S/e1.95.json\"))\nout={\"pdf_page\":95,\"book_page\":65,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-05\",\"entries\":[e0,e1]}\njson.dump(out, open(\"data/verification/page-95.json\",\"w\"), ensure_ascii=False, indent=1)\nprint(\"written\")\nEOF\npython3 -m json.tool data/verification/page-95.json > /dev/null && echo \"JSON OK\"\npython3 tools/verify_check.py 95"
}
```


### [2026-09-05T14:38:08.892Z] TOOL RESULT

```
written
JSON OK
nodes verified: 18/18
node verdicts: {'plausible': 6, 'confirmed': 11, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 18, 'partial': 5, 'not_checked': 2}
books consulted: {'supports': 37, 'silent': 9, 'partial': 8} | by book: {'CHEUNG': 10, 'BRT': 5, 'NYB': 5, 'KNT': 4, 'PHD': 4, 'KLN': 4, 'POK': 3, 'MON': 3, 'IEC': 3, 'Etymonline': 3, 'HRN': 2, 'SKT': 2, 'HUB': 1, 'SOD': 1, 'AHD': 1, 'TLM': 1, 'BOOK': 1, 'WLD': 1}
```


## [2026-09-05T14:38:16.119Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nhead -c 20 data/verification/page-95.json | xxd | head -2\npython3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-95.json'))\nfor e in d['entries']:\n    print('ENTRY', e['entry'], e['root'], e['verdict'], '| note_fa len', len(e['note_fa']))\n    for n in e['nodes']:\n        print('  #%s %-22s %-22s %s | fa=%d refchk=%d cons=%d src=%d' % (n['id'], n['lang'], n['words'][:22], n['verdict'], len(n['derivation_fa']), len(n['ref_check']), len(n['consulted']), len(n['sources'])))\nEOF\ngit -C /home/sfmqrb/git/rishe status --short"
}
```


### [2026-09-05T14:38:17.958Z] TOOL RESULT

```
00000000: 7b0a 2022 7064 665f 7061 6765 223a 2039  {. "pdf_page": 9
00000010: 352c 0a20                                5,. 
ENTRY 0 Bheudh confirmed | note_fa len 560
  #1 Avestan / Old Persian  baoidi, baodhi, baud-a plausible | fa=608 refchk=3 cons=3 src=1
  #2 Persian                bŭy; bŭy-yîdan; bŭ-stâ confirmed | fa=467 refchk=1 cons=5 src=2
  #3 Avestan / Old Persian  pati-baus              plausible | fa=480 refchk=1 cons=4 src=1
  #4 Pahlavi                payôs                  confirmed | fa=419 refchk=1 cons=3 src=1
  #5 Persian                bîyŭsîdan; bîyŭsandeh; confirmed | fa=385 refchk=3 cons=3 src=1
  #6 Sogdian                bws                    transcription_suspect | fa=405 refchk=1 cons=3 src=0
  #7 Sanskrit               bŭdhati; bŭdha         plausible | fa=318 refchk=1 cons=3 src=2
  #8 Persian                bŭdâ                   plausible | fa=432 refchk=1 cons=2 src=1
  #9 English                Buddha                 confirmed | fa=319 refchk=1 cons=2 src=1
  #10 Germanic                                      confirmed | fa=269 refchk=1 cons=2 src=1
  #11 English                bid, forbid            plausible | fa=348 refchk=1 cons=4 src=1
ENTRY 1 Bheug, Bheugh confirmed | note_fa len 515
  #1 Avestan                baog, bunja; baoxtar   confirmed | fa=341 refchk=1 cons=3 src=1
  #2 Pahlavi                bôxtan; bôzišn         confirmed | fa=424 refchk=2 cons=3 src=1
  #3 Persian                boxt; pŭzîdan          confirmed | fa=555 refchk=2 cons=4 src=2
  #4 Old Persian            baug; baga-buxša       confirmed | fa=499 refchk=1 cons=3 src=1
  #5 None                                          confirmed | fa=330 refchk=1 cons=2 src=0
  #6 Latin                  fugere                 plausible | fa=518 refchk=2 cons=3 src=2
  #7 English                fugitive, centrifugal, confirmed | fa=396 refchk=1 cons=2 src=1
?? data/verification/page-95.json
```


## [2026-09-05T14:38:22.605Z] TOOL CALL #66: Bash

```json
{
 "command": "git status --short && echo \"---\" && ls -la data/verification/sources/refs/ocr/BOOK/95.png && tail -3 data/verification/sources/web/index.jsonl | cut -c1-160"
}
```


### [2026-09-05T14:38:22.675Z] TOOL RESULT

```
?? data/verification/page-95.json
---
-rw-rw-r-- 1 sfmqrb sfmqrb 78178 Sep  5 10:14 data/verification/sources/refs/ocr/BOOK/95.png
{"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs", "file": "data/verification/sources/web/1b4899b9782322f7.
{"url": "https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C%D9%87/", "file": "data/verification/sources/web/55124b59e54ea442.txt", "fetched": "2026-09-05T14:34:59Z", "
{"url": "https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C/", "file": "data/verification/sources/web/c4df3eb8299e076e.txt", "fetched": "2026-09-05T14:35:00Z", "status
```


## [2026-09-05T14:39:48.696Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ngrep -c \"page 95\" data/verification/sources/web/index.jsonl\ngrep -o '\"url\": \"[^\"]*\"' data/verification/sources/web/index.jsonl | tail -12"
}
```


### [2026-09-05T14:39:48.763Z] TOOL RESULT

```
8
"url": "https://vajehyab.com/moein/%D9%81%D9%84%D8%B3%D9%81%D9%87"
"url": "https://www.etymonline.com/word/Philadelphia"
"url": "https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%DB%8C%D9%84%DB%8C%D8%B3/"
"url": "https://www.etymonline.com/word/philosophy"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0eyh%E2%82%82-"
"url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85"
"url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%DA%A9"
"url": "https://en.wiktionary.org/wiki/%D8%A7%D8%A8%D8%B1%D9%88"
"url": "https://en.wiktionary.org/wiki/%D8%A8%DB%8C%D9%85%D9%87"
"url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/h%E2%82%83b%CA%B0r%C3%BAHs"
"url": "https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C%D9%87/"
"url": "https://abadis.ir/fatofa/%D8%A8%D9%88%DB%8C/"
```


## [2026-09-05T14:40:08.770Z] AGENT

All eight of my page-95 web sources are archived and indexed (`grep -c "page 95"` → 8); other index rows belong to parallel sessions. `verify_check.py 95` reports 18/18 nodes and 0 PROBLEM lines.

**Page 95 (book p. 65) — 2 entries, 18 nodes**

- Root verdicts: 2 confirmed (Bheudh = PIE \*bʰewdʰ-, Pok. 150; Bheug/Bheugh = Pok. 2. bheug- p.152 — gloss "to purify, save, free" is Pokorny's wording verbatim).
- Node verdicts: **11 confirmed, 6 plausible, 1 transcription_suspect**, 0 disputed.
- Ref checks: 18 supports, 5 partial, 2 not_checked. Books consulted: 55 stances across POK, WLD, AHD, IEC, BRT, KNT, PHD, NYB, HRN, HUB, CHEUNG, SOD, MON, KLN, SKT, Etymonline.

**transcription_suspect**
- Bheudh #6 Sogdian `bws` "incense" — the Sogdian word is **βwδ** (Gharib no. 2878, p.113, "< Av. baoδa, incense"); `-s` stands for `-δ`. Checked the printed page: the book itself prints "bws", so `error_in: "book"` — Nourai's slip, extraction is faithful. Page image saved to `data/verification/sources/refs/ocr/BOOK/95.png`.

**Notable "plausible" calls**
- #1 and #3 of Bheudh are labelled "Avestan / Old Persian" but no Old Persian reflex exists (Kent silent); and `pati-baus` is not an attested form but Abolghasemi's reconstruction \*pati-baud-sa- (FFD p.40, which Nourai cites correctly).
- #7 `bŭdhati` — standard citation forms are bódhati / búdhyate; `budha-` is fine.
- #8 `bŭdâ` — a modern re-borrowing; BQT p.313 actually has بوداسپ (< bodhisattva), which the arrow doesn't draw.
- #11 `bid` — a merger of OE bēodan (\*bʰewdʰ-) and biddan (\*gʷʰedʰ-); AHD's own index lists BID under two roots. `forbid` is fine.
- Bheug #6 Latin `fugere` — Pokorny separates 1. bheug- "flee" from 2. bheug- "free" (both on p.152); Cheung/LIV/Wiktionary unite them, so Nourai is with the majority but not unanimity.

**No extraction errors found** — the JSON matches the printed page throughout, including the empty Germanic box (Bheudh #10) and the genuinely empty unlabelled box under Old Persian (Bheug #5).

**Best finds:** MacKenzie prints `bōzišn … N pōzis` — his own New Persian equivalent is exactly Nourai's پوزش arrow; Abolghasemi's root index puts \*baud on pp. 39, 40, matching FFD:39/FFD:40 precisely; Kent p.199 is exactly the Bagabuxša- entry.

One caveat recorded on Bheug #3: of the cross-reference headwords under the box, پوزش belongs to this root but **پوز** "snout, muzzle" is an unrelated homonym.
