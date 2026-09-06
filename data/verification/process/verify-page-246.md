# Verification process log — verify-page-246


## [2026-09-06T15:52:34.819Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 246 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-246.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-246.json. Write /home/sfmqrb/git/rishe/data/verification/page-246.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 246` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:52:36.277Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:52:36.983Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:52:36.995Z] TOOL RESULT

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


## [2026-09-06T15:52:37.008Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-246.txt"
}
```


### [2026-09-06T15:52:37.020Z] TOOL RESULT

```
1	=== PDF page 246 (book page 216) ===
2	--- entry 0 ---
3	ROOT [Turkish] Kayik : boat  (refs KLN:220)
4	#1 (parent #0) [Persian] refs=MON:2629; ARK:214 | qâyeq «قایق» : boat
5	#2 (parent #0) [Italian] refs=KLN:220 | caicco
6	  #3 (parent #2) [French] refs=PHN:85 | 
7	    #4 (parent #3) [English] refs=AHD:187; LKT:81; KLN:220; FWE:45 | caiique : a row or sail boat
8	--- entry 1 ---
9	ROOT Kaz -> redirect to Kaž
10	--- entry 2 ---
11	ROOT [Old Persian] Kaž, Kaz : inexpensive silk  (refs None)
12	#1 (parent #0) [Pahlavi] refs=BQT:1637; PLA:218 | kac, kač : an inexpensive silk
13	  #2 (parent #1) [Persian] refs=MON:2963 | kaz «کز» : inexpensive silk ; kazâkand «کزاکند» : silk-filled ☞Gwhen 1 | extra: کژ ، غژ ، غژغاو ؛ کژاکند
14	    #3 (parent #2) [French] refs=AHD:209 | casaqueand, casaque : a kind of silk-filled garment
15	      #4 (parent #3) [English] refs=KLN:246 | cassock : a long garment worn by the clergy
16	    #5 (parent #2) [Arabic] refs=LKT:91; PLA:218; NFI:40 | qaz : a type of cloth
17	      #6 (parent #5) [Persian] refs=MON | qaz «قز» : a kind of cloth | extra: قزاغند
18	      #7 (parent #5) [French] refs=NFI:40 | gaze : a loosely woven cotton fabric | NOTE: AHD and KLN derive this from Gaza in Palestine where the fabric was supposed to be made
19	        #8 (parent #7) [Persian] refs=MON:3166 | gâz «گاز» : a surgical dressing
20	        #9 (parent #7) [English] refs=KLN | gauze
21	--- entry 3 ---
22	ROOT Ke 1 -> redirect to Ak
23	--- entry 4 ---
24	ROOT Ke 2 -> redirect to Ki 2
25	--- entry 5 ---
26	ROOT [Greek] Keanos : lying, siting  (refs KNT:164)
27	#1 (parent #0) [Greek] refs=KNT:164 | o-keanos : lying around, water surrounding the earth | NOTE: FSD:1707 & TAD:5 derive this word from Greek "ôkys:swift". See Root "Ôku:swift".
28	  #2 (parent #1) [Arabic] refs=TAD:5 | oqyânŭs : ocean
29	    #3 (parent #2) [Persian] refs=MON:327 | oqyânŭs «اقیانوس» : ocean
30	  #4 (parent #1) [Latin] refs=AHD:909 | ôceanus : ocean
31	    #5 (parent #4) [English] refs=AHD | ocean
32	
```


## [2026-09-06T15:52:41.050Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-246.json",
 "description": "Read source JSON for page 246"
}
```


### [2026-09-06T15:52:41.085Z] TOOL RESULT

```
{
  "pdf_page": 246,
  "book_page": 216,
  "entries": [
    {
      "root": {
        "name": "Kayik",
        "lang": "Turkish",
        "refs": "KLN:220",
        "gloss": "boat"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "MON:2629; ARK:214",
          "words": [
            {"translit": "qâyeq", "gloss": "boat", "script": "قایق"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Italian",
          "refs": "KLN:220",
          "words": [
            {"translit": "caicco", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "PHN:85",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "AHD:187; LKT:81; KLN:220; FWE:45",
          "words": [
            {"translit": "caiique", "gloss": "a row or sail boat", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kaz",
        "redirect": "Kaž"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Kaž, Kaz",
        "lang": "Old Persian",
        "refs": null,
        "gloss": "inexpensive silk"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:1637; PLA:218",
          "words": [
            {"translit": "kac, kač", "gloss": "an inexpensive silk", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:2963",
          "words": [
            {"translit": "kaz", "gloss": "inexpensive silk", "script": "کز"},
            {"translit": "kazâkand", "gloss": "silk-filled", "script": "کزاکند", "see": ["Gwhen 1"]}
          ],
          "script_extra": "کژ ، غژ ، غژغاو ؛ کژاکند",
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "French",
          "refs": "AHD:209",
          "words": [
            {"translit": "casaqueand, casaque", "gloss": "a kind of silk-filled garment", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:246",
          "words": [
            {"translit": "cassock", "gloss": "a long garment worn by the clergy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 2,
          "lang": "Arabic",
          "refs": "LKT:91; PLA:218; NFI:40",
          "words": [
            {"translit": "qaz", "gloss": "a type of cloth", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Persian",
          "refs": "MON",
          "words": [
            {"translit": "qaz", "gloss": "a kind of cloth", "script": "قز"}
          ],
          "script_extra": "قزاغند",
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 5,
          "lang": "French",
          "refs": "NFI:40",
          "words": [
            {"translit": "gaze", "gloss": "a loosely woven cotton fabric", "script": null}
          ],
          "note": "AHD and KLN derive this from Gaza in Palestine where the fabric was supposed to be made",
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:3166",
          "words": [
            {"translit": "gâz", "gloss": "a surgical dressing", "script": "گاز"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "KLN",
          "words": [
            {"translit": "gauze", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Ke 1",
        "redirect": "Ak"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Ke 2",
        "redirect": "Ki 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Keanos",
        "lang": "Greek",
        "refs": "KNT:164",
        "gloss": "lying, siting"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "KNT:164",
          "words": [
            {"translit": "o-keanos", "gloss": "lying around, water surrounding the earth", "script": null}
          ],
          "note": "FSD:1707 & TAD:5 derive this word from Greek \"ôkys:swift\". See Root \"Ôku:swift\".",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "TAD:5",
          "words": [
            {"translit": "oqyânŭs", "gloss": "ocean", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "MON:327",
          "words": [
            {"translit": "oqyânŭs", "gloss": "ocean", "script": "اقیانوس"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD:909",
          "words": [
            {"translit": "ôceanus", "gloss": "ocean", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "ocean", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-06T15:52:41.103Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:52:41.135Z] TOOL RESULT

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


## [2026-09-06T15:52:47.345Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['KLN','MON','ARK','PHN','AHD','LKT','FWE','BQT','PLA','NFI','KNT','TAD','FSD','TTS','DEV','ARY','PHD','HRN','HUB']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T15:52:47.806Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,60p data/verification/page-202.json && echo ---- && cat tools/verify_check.py | head -60",
 "description": "Inspect prior verification file and checker"
}
```


### [2026-09-06T15:52:49.055Z] TOOL RESULT

```
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== ARK {"title": "M.H. Rokn-zadeh Adamiyyat, Arkan-e Sokhan, Sharq 1347/1968", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand."}
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== FWE {"title": "A. J. Bliss, A Dictionary of Foreign Words and Phrases in Current English, 1966", "edition_found": "1966 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/dictionaryoffore00blis (+8 other lending copies)", "identifier": "dictionaryoffore00blis (also dictionaryoffore0000alan, dictionaryoffore0000ajbl)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<word>.", "notes": "RE-SEARCH 2026-09: borrowable only."}
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== NFI {"title": "F. Jonaydi, Nameh-ye Farhang-e Iran (section 4 translating C.H. Rempis, 'Persische Wörter im Deutschen'), Bonyad-e Neyshabur 1368/1989", "kind": "catalog", "url": null, "lookup_hint": "Not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "none online. || RE-SEARCH 2026-09: nothing digitised on any permitted platform (archive.org, Google Books, Persian libraries/ebook stores). Check opac.nlai.ir manually / buy second-hand. Contact Bonyad-e Neyshabur / parsianjoman for the issue with the Rempis translation."}
== KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively 
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
```


### [2026-09-06T15:52:49.100Z] TOOL RESULT

```
{
 "pdf_page": 202,
 "book_page": 172,
 "verified_by": "claude-opus-5",
 "verified_on": "2026-09-05",
 "entries": [
  {
   "entry": 0,
   "root": "Gwa, Gwâ, Gwen 2",
   "verdict": "confirmed",
   "modern_form": "PIE *gʷem- 'to go, to come' (with the collateral root *gʷeh₂- / *gʷā- 'to step, go'); Pokorny IEW 463-465",
   "note": "Pokorny's entry, which begins on p.463 exactly as Nourai cites, is headed 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“', and it is deliberately a double entry (I. gʷā-, II. gʷem-), which is why Nourai's box carries two names, 'Gwa, Gwâ'. His third name 'Gwen 2' reflects the *gʷem- > *gʷen- variant Pokorny himself notes ('Unthematisch *(e)-gʷem-t (> *e-gʷen-t)', and Latin advenam / veniō with -n- for -m-); it is not a separate root in any modern handbook, so it is Nourai's own labelling convenience rather than an error of substance. Watkins/AHD 1985 heads the same material 'gʷā-. Also gʷem-. To go, come'; Cheung splits it into *gaH¹ (PIE *gʷeh₂-, Pok. 463 f.) and *gam¹ (PIE *gʷem-, Pok. 464 f.). The gloss 'to walk, to step, to come, to go' is an accurate rendering. Two words in the chart do not belong to this root: Avestan 'gâv' in node 6 (a misprint) and 'thamân' in node 12 (an unidentifiable form), and one Persian word, nîyâm (node 3), is derived by modern scholarship from a different root (*ni-dā-, not *ni-gam-). Everything else on the page is standard, well-attested Iranian etymology.",
   "note_fa": "جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۶۳ فرهنگ خود مدخل «gʷā-, gʷem-» را با معنای «رفتن، آمدن؛ به جهان آمدن، زاده شدن» آورده و همان‌جا نام‌های gʷm̥-ti-s و gʷem-tu-s «گام، رفتار» را می‌افزاید؛ پس هر دو صورت «Gwa/Gwâ» و «Gwem» از یک مدخل‌اند و برچسب «هندواروپایی» و معنای «راه رفتن، گام برداشتن، آمدن، رفتن» درست است. نام سوم «Gwen 2» گونهٔ *gʷen- است که خود پوکورنی (در *e-gʷen-t و در veniō لاتین) یاد کرده و در کتاب‌های امروزی ریشهٔ جداگانه‌ای به شمار نمی‌رود؛ این نام‌گذاری از خود نورایی است نه خطای علمی. واتکینز (پیوست AHD) نیز همین ماده را «gʷā-, also gʷem-: رفتن، آمدن» آورده و چونگ آن را به دو ریشهٔ *gaH¹ و *gam¹ بخش کرده است. در سراسر این صفحه تنها سه لغزش هست: صورت «gâv» در گرهٔ ۶ (غلط چاپی)، صورت «thamân» در گرهٔ ۱۲ (صورتی که در هیچ فرهنگی یافت نشد) و واژهٔ «نیام» در گرهٔ ۳ که پژوهش امروزی آن را از ریشهٔ دیگری (*ni-dā-) می‌داند.",
   "sources": [
    "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/gʷem-"
   ],
   "ref_check": [
    {
     "ref": "POK:463",
     "status": "supports",
     "note": "POK_02.txt line 1790 (the leaf whose running numbers are 463-465): 'gʷā-, gʷem- „gehen, kommen; zur Welt kommen, geboren werden“; gʷm̥-ti-s f., gʷem-tu-s m. „Gang, Schritt“, Verbaladjektiv gʷm̥-to-s. I. gʷā-: ... 2. gʷem-: ...'. The same pages carry 'av. gātu-s „Ort, Liegerstatt, Sessel, Thron“, apers. gāθu- ds.', 'av. gā-man- n. „Schritt“', 'av. jantu (*gʷem-tu-)' and 'av. jasaiti „er geht“' — i.e. Pokorny 463 alone underwrites the root box and nodes 1, 2 and 6."
    }
   ],
   "consulted": [
    {
     "src": "WLD",
     "where": "Bd. I 675-677 (WLD_Bd1 djvu line 42665 ff., running head 'gʷem-, gʷā-')",
     "stance": "supports",
     "note": "'gʷem-, gʷā-' … 'ai. gātram „Glied, Körper“; ai. gātu- „Gang, Weg, Raum, Ort“, av. gātu-s „Ort, Platz; Liegerstatt, Sessel, Thron“, ap. gāθu … ai. vi-gāman- n. „Schritt“ … av. gāman- n. „Schritt“'. This is the source Pokorny 463 abridges (Buck cites it as 'Walde-P. 1.675 ff.')."
    },
    {
     "src": "AHD",
     "where": "Watkins 1985, g-list (AHD_watkins1985.txt line ~539)",
     "stance": "supports",
     "note": "'gʷā-. Also gʷem-. To go, come. 1. Germanic *kuman in a. Old English cuman, to come: COME … 3. Suffixed zero-grade form *gʷm̥-yo- in Greek bainein, to go, walk, step, with basis (< *gʷm̥-ti-), a stepping, tread, base'. Same double root, same gloss."
    },
    {
     "src": "CHEUNG",
     "where": "s.v. *gam¹ (CHEUNG.txt lines 7307, 7478) and *gaH¹ (line 7054)",
     "stance": "supports",
     "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *gam¹ article lists, as its New-Persian outcome, exactly Nourai's harvest: 'NP zamān “time” … NP gām “step, pace” … NP āmadan … NP pay(g)ām “message”, NP pay(g)ambar … NP anjuman “company, assembly, club”'."
    },
    {
     "src": "SYN",
     "where": "Buck §10.47/10.48 (SYN.txt line 17514 f.)",
     "stance": "supports",
     "note": "'2. IE *gʷem-, *gʷā-. Walde-P. 1.675 ff. … Skt., Av., OPers. gam- \"go, come\" (Skt. gacchati, Av. jasaiti, sk̑o- presents like Grk. baskō; Av. jam- without prefix mostly \"come\"; also Av., OPers. ā-jam- \"come\", whence NPers. amadan \"come\")'."
    },
    {
     "src": "KLN",
     "where": "p.318 s.v. 'come' (KLN_1966.txt line 8320, page marker 318 at the foot)",
     "stance": "supports",
     "note": "'come … fr. I.-E. base *gʷem-, “to go; to come”, whence also OI. gámati, gacchati … Avestic jamaiti “goes” … Cp. the collateral base *gʷā- in OI. agām (aor.), Gk. ébēn (aor.), “I went”'."
    }
   ],
   "nodes": [
    {
     "id": 1,
     "lang": "Avestan / Old Persian",
     "words": "gam : to come, step; jam, jantu : to go",
----
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
```


## [2026-09-06T15:53:24.052Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN caique ===\"; grep -n -i \"caique\\|caïque\\|caicco\" KLN_1966.txt | head -20\necho \"=== KLN cassock ===\"; grep -n -i \"cassock\\|casaque\\|kazhagand\\|kazagand\" KLN_1966.txt | head -20\necho \"=== KLN gauze ===\"; grep -n -i \"^gauze\\|gauze,\" KLN_1966.txt | head -20\necho \"=== LKT kayik ===\"; grep -n -i \"kajik\\|kayik\\|qajiq\\|kaik\" LKT.txt | head -20\necho \"=== LKT qazz ===\"; grep -n -i \"qazz\\|kazz\\|gaze\\b\" LKT.txt | head -20",
 "description": "Grep Klein and Lokotsch"
}
```


### [2026-09-06T15:53:24.176Z] TOOL RESULT

```
=== KLN caique ===
6107:Deut.  32:6,  Ps.  139:13,  Prov.  8:22),  whence developed  the  meanings  ‘he  got,  acquired;  he bought’.  This  relationship  between  the  name Qdyin  and  the  verb  qandh  accounts  best  for  the fact  that  in  Gen.  4 : 1  Eve  explains  the  name Qdyin  with  the  word  qanithi.  This  word  is  usually translated,  ‘I  have  gotten’,  but  it  is  more  prob¬ able  that  its  sense  here  is  ‘I  have  formed’,  ‘I have  made’.  See  U.  Cassuto,  A  Commentary  on the  Book  of  Genesis,  Part  One,  From  Adam  to Noah,  The  Hebrew  University,  Jerusalem,  1961, pp.  196-202.  Cp.  Elkanah,  kinah. caique,  n.,  a  light  rowing  or  sailing  boat,  used esp.  on  the  Bosporus.  — -  F.,  fr.  It.  caicco,  fr. Turk,  kayik.
6199:Derivatives:  calk,  tr.  v.,  calk-er,  n.,  calk-ing,  n. calk,  caique,  tr.  v.,  to  copy.  —  F.  calquer,  ‘to trace,  make  a  drawing’,  fr.  It.  calcare,  lit.  ‘to trample,  tread’,  fr.  L.  calcare,  ‘to  tread’,  whence also  OF.  cauchier,  chauchier.  Accordingly  calk, ‘to  copy’,  is  derivatively  identical  with  calk,  ‘to stop  up  with  oakum’  (q.v.)
=== KLN cassock ===
6685:cassock,  n„  a  long  ecclesiastical  garment.  —  F. cosaque,  fr.  Pers.  kazagand,  ‘a  kind  of  jacket'. The  ending  -and  of  the  Persian  word  was  mis¬ taken  for  a  suff.,  and  consequently  dropped. Cp.  F.  casaquin,  'jacket',  in  which  the  supposed suff.  -and  was  substituted  by  suff.  -in. Derivative:  cassock,  tr.  v.
7415:Derivatives:  chime,  tr.  and  intr.  v.,  chim-er,  n. chime,  chimb,  n.,  rim  of  a  cask.  —  ME.  chimbe, from  the  stem  of  OE.  cimbing,  ‘joint’,  which  is rel.  to  Du.  kirn,  ‘chime’,  G.  Kimme,  dial.  Swed. kind),  kimbe,  ‘edge’.  These  words  prob.  stand in  gradational  relationship  to  comb.  Cp.  dial. Swed.  kim,  ‘cockscomb’, chimer,  chimere,  n.,  a  robe  worn  by  bishops.  — MF.  chamarre,  samarre,  ‘a  loose  gown’,  fr.  Sp. zamarra,  fr.  Arab,  sammiir,  ‘weasel,  marten’. Cp.  It.  zimarra,  ‘robe;  cassock’,  which  was formed  with  vowel  dissimilation  fr.  Sp.  zamarra. F.  simarre,  ‘robe;  cassock’,  is  a  loan  word  fr.  It. zimarra.  Cp.  cymar,  simar,  zimarra. chimera,  chimaera,  n.,  a  monster  with  lion’s  head, goat’s  body  and  serpent’s  tail  ( Greek  mythol.)  — L.  chimaera,  fr.  Gk.  yluatpa,  ‘a  young  she- goat’,  which  is  rel.  to  xipapap,  ‘a  young  he- goat’,  lit.  ‘one  winter  old’,  fr.  xsip.a,  ‘winter’, which  is  cogn.  with  L.  hie  ms,  ‘winter’,  hibernus, ‘pertaining  to  winter,  wintry’.  See  hibernate  and cp.  chiono-,  the  first  element  in  Chimaphila  and the  second  element  in  Hedychium  and  in  iso- cheime.
36023:soutane,  n.,  a  cassock  worn  by  Roman  Catholic priests.  —  F.,  fr.  earlier  sottane,  fr.  It.  sottana, ‘petticoat’,  lit.  ‘undergarment’,  which  derives  fr. sotto,  ‘under’,  fr.  L.  subtus,  ‘below’,  fr.  sub, ‘under’.  See  sub-.  F.  soutane  (for  sottane)  owes its  form  to  the  influence  of  F.  sous,  ‘under’, souteneur,  pimp;  bully.  — t  F.,  ‘supporter,  pro¬ tector;  bully’,  fr.  soutenir,  ‘to  sustain’,  fr.  VL. *sustenire,  corresponding  to  L.  sustinere.  See sustain  and  cp.  sostenuto. south,  adv.  —  ME.  suth,  south,  fr.  OE.  sud, ‘southward,  in  the  south’,  formed — with  com¬
=== KLN gauze ===
10118:cyphosis,  n.  —  A  var.  spelling  of  kyphosis, cy-pres,  cypres,  adv.  and  adj.,  as  nearly  as  pos¬ sible  in  agreement  with  the  testator’s  intentions (law).  —  F.  si-pris,  ‘so  near,  as  near’,  fr.  VL.  sic presse,  ‘from  so  near’,  fr.  L.  sic,  ‘so’,  and  presse, adv.  of  pressus,  ‘pressed’,  pp.  of  premere ,  ‘to press’.  See  sic  and  press,  v. cypress,  n.  —  ME.  cipres,  cypres,  fr.  OF.  cipres (F.  cypresse),  fr.  Late  L.  cypressus,  fr.  Gk.  xu- 7rapia<jo9,  which  prob.  derives  fr.  Heb.  gipher, name  of  the  tree  of  whose  wood  the  ark  was made  (see  Gen.  6 : 14).  Cp.  gopher  and  see  Hehn- Schrader,  Kulturpflanzen  und  Haustiere  in ihrem  Obergang  aus  Asien  nach  Griechenland und  Italien,  5th  edition,  p.231.  Cp.  Cyprian. Derivatives:  cypress,  adj.,  cypress-ed,  adj. cypress,  n.,  cypress  lawn.  —  ME.  c'pres,  ‘gauze, cloth  of  gold’,  fr.  OF.  Cipre,  Cypre,  ‘the  island of  Cyprus’;  so  called  because  orig.  brought from  Cyprus.
15877:gauze,  n.,  a  very  fine  fabric  of  silk,  cotton  etc.  — F.  gaze,  fr.  Gaza,  a  town  in  Palestine,  famous for  the  very  fine  transparent  tissues  fabricated there.
=== LKT kayik ===
2419:'Boot;  langer,  sehr  spitz  zulaufender  und von  leichtem  Holze  gebauter  pfeilschnel- ler Kahn';  hieraus  bulg.  serb.  kaik  'Kahn für  10  Mann',  poln.  kaik,  klruss.  kajuk 'Flußboot',  russ.  kaik,  kajuk  'Boot,  Last- schiff ;  rum.  caic  'Bai'ke',  caicgiü  'Barkeii- führer',  it.  caicco  'kleine  Barke  als  Ret- tungsboot, Schaluppe',  siz.  caiccu  auch 'Kuppler',  frz.  culq,  ca'ique,  calc\  ndl. kaick,  engl,  ca'ique  'Schaluppe,  Boot  auf dem  Bosporus  und  dem  Schwarzen Meere'. —  [Hobson-Jobson  143  fragt  mit Recht,  ob  das  Wort  zufällig  oder  durch tk.  Sprachverwandtschaft  hmdurch  mit dem  grönländischen  kajak  gleichlautet]. [Gorjajew  158.  Bern  SlEtWb  469.  Gr SVociSic  229.
2462:'Schild'  [Stamm  kal  'anhäufen,  schwel- len; dick'  Vämbery  TktEtWb  S.  67, Nr.  721 ;  vgl.  Cag.  kalkan  'Schirm,  Schild', eigentlich,  was  zur  Abwehr  in  die  Höhe gehalten  wird;  ebenso  kirgis.  kaikam und  kalka  'Wetterdach'];  hieraus  serb. kalkan  'Dach,  Schild',  bulg.  kalkan  'ein- hängiges Dach,  Scholle  (Fisch)',  poln. (alt)  kalkan  'Buckelschild'.  [Bern  Sl EtWb  474.
7653:kabala  977 kaban  975 Ä;a6a^  971 kaczan  1192 Ä:a(ft  984 fcarfy  984 kafenauz  1005 kaftan  Iii. kaik  1014 kalauz  1276 Ä;a/efca  1040 kaleta  828 Ä;afÄ;aw  1034 kalkun(t)  1031 kamcha  1043 kamfora  1100 katnlot  653 kanczug  1042 kanczuk  1042 kanfora  1100 kaparki  978 kapary  978 kapinaz  1005 kapkan  1064 karabacz  1279 karaczan  2027 karafka  689 karawana  1075 karbacz  1279 karhona  1208 karbuz  824 karczma(rz)  825 karczoch  833 kardasz  1089 fcary  1070 Ä:a<MM  1272 ÄsttM^a  1005 kawak  1134 kawiar  851 kawon  1138 kazan  1144 kazna  855 kazmirek  1116
=== LKT qazz ===
1005:'Leichter,  durchsichtiger  Seiden-  oder Leinenstoff,  Gaze'  [aus  tk.  biirun  'Nase' aus  dem  Stamme  bar,  var  'vorwärts gehen,  fortschreiten',  Vämbery  TktEtWb S.  200,  Nr.  210:  also  wohl  eigentlich 'Nasenstoff,  d.  h.  Stoff  für  Schleier]; hieraus  rum.  burungiuc  'Gaze',  borangic 'ungezwirnte  Rohseide'.
1300:'Handtuch'  [aus  däst,  s.  hier  Nr.  498, und  niäl,  Präsensstamm  zu  mälldün 'reiben',  Horn  NpEt  S.  214,  Nr.  962], tk.  zur  Erleichterung  der  Aussprache destimal;  hieraus  vam.  testimal,  testemal 'Kopf-  oder  Halstuch':  Die  verheirateten Frauen  über  30  Jahre  tragen  dieses Tuch;  es  ist  ein  langer  Gaze-  od.  Leinen- schleier, der  den  Kopf  bedeckt  und  hin- ten bis  üher  die  Hüften  herabfällt [Sain  69],
1725:Hebr.  '^Azzäh;  gr.  Vdta,  N.  pr.,  Name der  südlichsten  Stadt  an  der  Küste  Pa- lästinas [vgl.  ZDPV  VII,  1/14];  hiernach soll  die  Gaze,  frz.  gaze,  'ein  durchsich- tiger, feiner  Stoff',  benannt  sein.  Da aber  bis  jetzt  keine  Textilindustrie  in älteren  Zeiten  hier  nachgewiesen  ist, muß  die  Etymologie  als  rein  willkürlich angezweifelt  werden;  die  Ableitung  aus kazz  [s.  hier  Nr.  1147]  ist  unbedingt vorzuziehen.
2696:1147.  Ar.  kazz:
2700:gewebe',  frz.  gaze,  dtsch.  Gaze  'dass.', rum.  hasa  [über  das  Tk.]  'Kaliko'.  — [Die  ältere  Etymologie,  s.  hier  Nr.  702, so  auch  noch  ML  3710].  —  MWiD  94.
3278:'Affe';  hieraus  vielleicht  dtsch.  Meer- katze, Cercopithecus  [als  ob  das  Tier  zu uns  über  das  Meer  gekommen  wäre;  wie die  Katze  hat  es  einen  langen  Schwanz; vergleicht  man  daneben  aber  dtsch. Meerkalb,  Meerschweinchen  sowie  die älteren  Formen  ahd.  merikazza,  mnd. merkatte,  so  scheint  die  Etymologie  doch recht  zweifelhaft].  [MWiD  25/26.  Ander- sen DVEt  6.
5831:merikazza  ahd.  1422
```


## [2026-09-06T15:53:26.163Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHN caique ===\"; grep -n -i \"caique\\|caïque\\|CAIQUE\" PHN.txt | head -20\necho \"=== PHN gaze ===\"; grep -n -i \"^GAZE\\|CASAQUE\" PHN.txt | head -20\necho \"=== KNT p164 area ===\"; awk 'BEGIN{RS=\"\\f\"} NR==179' KNT.txt | head -60",
 "description": "Grep Pihan and Kent"
}
```


### [2026-09-06T15:53:27.893Z] TOOL RESULT

```
=== PHN caique ===
2890:CAÏC ou CAÏQUE, s. m. (t.)
10337:Caîc ou Caïque, s. m. (t.) 85
=== PHN gaze ===
3326:CASAQUE, s. r. (a.)
3330:surtout dans ce dernier sens que le mot casaque est usité en
3340:doute servi d'intermédiaire au français casaque. — Tourner
3341:casaque se dit proverbialement pour changer de parti,
5169:GAZE, s. f. (a.)
5177:gaze sur un discours, c'est voiler ce qu'un récit pourrait con-
5179:GAZELLE, 6. f. (a.)
10377:Casaque, s. f. (a.) — Casaquin, s. m. (p.) 10a
=== KNT p164 area ===
 : hya : Dārayavauš : XS : руё : Haxdmanigiya : Mitra : mam : paluv
Nore то АНЬ: Probably the demonstrative imam stood before apadānam at the beginning, and other
155
phrases of the protective prayer may have stood at the end.
TRANSLATION oF Á?Hb: This palace, of stone in its column(s), Artaxerxes the Great King built, the son of Darius the King, an Áchaemenian. May Mithras protect me ...
A'Hc = Artaxerxes II, HAMADAN C. 1 baga : vazraka : Auramazda :hya : тайа : 2 baganam : һуа :imàm : bümim : ada : 3 һуа : avam : asmánam : ada : hya : martiya 4 m : айа : һуа : &y&tim : ада : martiyahy 5 & : hya : Artaxšaçām : XSm : akunaug : ai 6 vam : parünàm : XSm : aivam : parünàm : 7 framataram : ðātiy : Artaxšaçā : XS : va 8 zraka : XŠ : XSyinim : X8 : DHyünám :XS 9 : ahydya : BUya : adam : Darayavausahy 10 à : XShyà : риса : DarayavauSahya : Artax И Sacahya : XShya : puça : ArtaxSacahy 12 & : XSayarSahy3 : XShya : риса : Хау 13 arsahya : Dàrayavausahyà : XShya : p 14 uça : Dārayavaušahyā : Vištāspahyā : nā 15 ma : puça : Haxämanišiya :ðātiy : Artaxša 16 (à : XS : vagna : Auramazdaha : adam : XS :8 17 hyaya : BUyà : vazrak&yà : düraiy :a 18 piy : amiy : Auramazda : xSagam : manā : frába 19 ra : màm : Auramazda : pátuv : uta : xSaca 20 m : tyamaiy : frábara : матау : vilam TRANSLATION OF A?He: M. 1-7. A great god is Ahuramazda, the great- est of gods, ... (= A!Pa 1-8). 82. 7-15.... (= A'Sa D: I (am) ... (= A'8a 1-2), son of Hystaspes by name, an Achaemenian. §3. 15-20. Saith Artaxerxes the King: By the favor of Ahuramazda I am king in this great carth far and wide; Ahuramazda bestowed the kingdom upon me. Me may Ahuramazda protect, and the kingdom which he bestowed upon me, and my royal house.
A?P = ARTAXERXES ÍT or IIT, PeRSEPOLIS.
: Parsa :
: Мада :
3 iyam : Üvja :
4 iyam : Parfava :
8 iyam : Uvarazmiya 9 iyam : така
10 1yam.: Harauvatiya
1 iyam 2 iyam
156
11 zyam 12 iyam 13 iyam 14 iyam 15 iyam 16 iyam 17 iyam 18 iyam 19 iyam 20 iyam 21 lyam 22 may 28 туат 24 iyam 25 туат 26 1yam 27 iyam 28 туат
80 iyam
: Gataguiya : Gadiraya : : Hiduya
: Зака : haumavargà : : бакё : tigraxauda : : Babirus :
: ABuriya
: Атарӯуа
: Mudráya
: Arminiya
: Katpatuka :
: Spardiya
: Yauna :
: Saka : paradraiya : : Skudra :
: Yauna : takabará : : Putàya :
: KüSiya
20 шат: : Karka :
Maciya
OLD PERSIAN -
Notes то А?Р: 4 @ataguiya Smith, Hz.; if correct, for Galaguviya; or a wrong writing for Satagudaya or 8atagudiya, cf. Gk. Larraybdar, 4 There із an extra verti- cal hasta between the g* and the a in haumavarga. ? imy*, miswritten for илт,
TRANSLATION ОЕ А?Р:
1. This is the Persian. 2. This isthe Меде. 3. This is the Elamite. 4. This is the Parthian. [5-7. This is the Arian, the Bactrian, the Sogdian.] 8. This is the Chorasmian. 9. This is the Drangian. 10. This is the Arachosian. |
11. This is the Sattagydian. 12. This is the
Gandarian. 13. This is the man of Sind. 14, This 15 the Amyrgian Scythian. 15. This is the Pointed- Cap Scythian. 16. This is the Babylonian. 17. This is the Assyrian. 1
```


## [2026-09-06T15:53:38.393Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT 1147 context ===\"; sed -n '2685,2710p' LKT.txt\necho \"=== LKT 702 context ===\"; sed -n '1715,1735p' LKT.txt\necho \"=== LKT kaik context ===\"; sed -n '2405,2425p' LKT.txt",
 "description": "LKT context"
}
```


### [2026-09-06T15:53:38.456Z] TOOL RESULT

```
=== LKT 1147 context ===
1141.  Mal.  käyulängit:
'Ein  Schatten  spendender  Baum,  Ailantus glandulosa  Desf.'  [aus  mal.  käyu  'Baum' Pijn  173  und  längit  'Himmel,  Firma- ment, Baldachin'  Pijn  203];  hieraus unter  Abfall  des  anlautenden  k  [vgl. hier  Nr.  1063]  der  botanische  Name, engl,  ailantus,  ailanthus,  frz.  ailante oder  langit,  ailanthe  [in  europäischen, bes.  französischen  und  deutschen,  sowie amerikanischen  Städten  als  Schattenbaum häufig  gepflanzt].  [JAOS  XVII,  105/180.
1142.  3IaI.  käyupfitih:
Ein  Strauch  aus  der  Familie  der  Myr- taceen,  Melaleuca  leucadendron  [auch schon  mal.  'weißer  Baum',  da  er  wie die  Birke  weiße  Rinde  zeigt] ;  aus  seinen Blättern  und  Zweigen  zieht  man  durch Destillation  ein  flüchtiges  Öl  von  durch- dringendem Gerüche:  frz.  htiile  de  caje- piit,  auch  kurz  cajeput,  pg.  cajeput,  engl. cajeput,  cajuput  'Kajeputöl'.  Es  wird in  der  Medizin  gegen  Wechselfieber  und in  der  Industrie  zur  Herstellung  von Firnis  gebraucht.  [MMM  9.  Devic  DEt 76.    JAOS  XVII,  120/123.
1143.  Tk.  kazak: 'Landstreicher,  Vagabund,  Nomade'  [in diesem  Sinne  veraltet,  vom  Stamme  kaz 'umherirren'  Vambery  TktEtWb  S.  22, Nr.  23 ;  jetzt  nur  noch  in  weicher  Form gezmek  'spazieren  gehen'] ;  hieraus  russ. kazak,  kozak,  bulg.  kazak,  poln.  kosak, dtsch.  Kosak,  Bezeichnung  für  die  süd- russischen Steppen-  und  Reitervölker; engl,  cossack,  angloind.  mit  der  Bedeu- tung 'Freibeuter,  plündernder  Reiter', rum.  cazac  'Kosak',  cazachiu  'russ. Weinhändler,  Kosakenmütze'.  Hieraus auch  die  Kleidernamen:  russ.  kazakin 'Art  Halbrock',  öech.  hazuka  'Mönchs- kutte, Oberkleid,  Decke',  poln.  hazuka 'Frauengewand';  mhd. kasugele,  kusuckel 'Mefjgewand',  kasacke  'kurzer  Reiserock', nhd.  Ä'rtsacfcCjacke  in  der  Damenmode), engl,  cassock  'langer  Priesterrock,  Sou- tane'; nlat.  cazaca,  it.  casacca,  hz.casa- qne,  sp.  pg.  casaca  'lange  Überjacke'. [Gorjajew  127.  Bern  SlEtWb  377  und 496.    Hobson-Jobson  262.
1144.  Tk.  kazau:
'Kessel'  [vom  Stamme  kas,  km  'reiben, scharren,  graben'  Vamberv  TktEtWb S.  20,  Nr.  22  II;  eigentlich  'Vertiefung']; hieraus  russ.  kazan  'dass.,  bes.  Brannt- weinkessel', klruss.  bulg.  serb.  poln.  (dial.) kazan  'Kessel,  Bassin'.  Auch  die  russ. Stadt  Kasan  a.  d.  Wolga  hat  ihren  Na- men wegen  ihrer  Lage  hierher.  Rum. cazan  'Kochkessel',  cäzänärie.
1145.  Tk.  kazma:
'Hacke'  [vom  gleichen  Stamme  wie  hier Nr.  1144];  hieraus  rum.  cazma  'Spaten, Doppelhacke'.
1146.  Tk.  kazyk:
'Pfahl'  [Kelfekian  Kämüs  927,  vom  glei- chen Stamme  wie  Nr.  1144  und  1145, vgl.  öag.  kazik,  kazuk  'Pflock',  eigentlich 'das  Eingegrabene'] ;  hieraus  bulg.  Ä;azU', serb.  kaziik  'Pfahl'.   [Bern  SlEtWb  496.
1147.  Ar.  kazz:
'Robseide,  Flockseide'  [aus  pers.  käz, gäz  ZDMG  L,  640];  hieraus  sp.  gasa 'durchsichtiges  feines  Leinen-  od.  Seiden-
Tk.  keCe.]
92
gewebe',  frz.  gaze,  dtsch.  Gaze  'dass.', rum.  hasa  [über  das  Tk.]  'Kaliko'.  — [Die  ältere  Etymologie,  s.  hier  Nr.  702, so  auch  noch  ML  3710].  —  MWiD  94.
114S.  Tk.  kece: Tilz,  Teppich'  [Kölekian  Kämüs  1015] ; hieraus  serb.  ceca  Tilz',  keca  'wollenes Obergewand  der  Berghirten  zum  Schutze gegen  Regen',  poln.  (dial.)  kieca,  kiecz 'Frauengewand,  Soldatenmantel'  [wohl über  uug.  kecse  'Art  Mantel']  und  an- dere Ableitungen.    [Bern  SlEtWb  498.
1149.  Hebr.  k^d^ui:
'Osten' ;  hieraus  gr.  Kabjuia,  Kobiaei'a  zur Bezeichnung  des  Zinkerzes  [vgl.  Edmun- dus  Ries,  Quae  res  et  vocabula  a  gentis semiticis  in  Graeciam  pervenerint,  quae- stiones  selectae.  Vratislaviae  1890.  S.  6]; mit  Wechsel  von  d  zu  l  [wie  gr.  äbd- |naq  >  ar.  almäs  ZDMG  LI,  295;  gr. bciKpu  >  lat.  lacrima;  lat.  Elisabeth  > sp.  Ysabel]  mlat.  calamina;  Grundwort zu  it.  calaminaria  'kieselhaltiges  Zinkerz', afrz.  chalemme,  nfrz.  calamine,  it.  gella- mina,  sp.  pg.  calamina;  engl,  calaniin, mhd.  kalemine,  dtsch.  Galmei  'Kiesel- zinkspat'. [Romania  XXXIII,  605; XXXVIII,  371.    ML  1453.
1150.  Syr.  kefal:
'Aufdecken,  abdecken,  ziehen';  hieraus wohl  mit  Anlehnung  an  niederdtsch. fillen  'das  Fell  abziehen'  [von  vel  'Fell'] gaunerdtsch.  Kafiller  'Schinder'.  [Seiler DKiL  IV,  490.
1152.  Tk.  kel:
'Kahl;  Flechte,  Grind'  [vom  Stamme  il 'glänzen,  strahlen'  Vämbery  TktEtWb S.  119,  Nr.  126  All];  hieraus  bulg.  kel 'Grind,  Räude',  serb.  cela  'Glatze,  Kahl- kopf; rum.  chel  'kahl',  chelie  'Glatze, Kahlköpfigkeit'  [wegen  chelbas  s.  hier Nr.  1023].    [Bern  SlEtWb  499.
1153.  MaL  kelädi:
'Eine  Art  Aronstab  mit  eßbarer  Wurzel, Colocasia  Vera'  [Pijn  179  a];  hieraus  der botanische  Name  lat.  caladium,  engl. caladiiim,  frz.  caladion,  sp.  caladio 'Pflanze,  die  in  den  feuchten  Land- strichen Südamerikas  wächst'  [Dicc  Gast 418  c].    [Devic  DEt  77.
1154.  Hebr.  kelaf:
=== LKT 702 context ===
Plr.  von  gazlra  'Insel';  N.  pr.,  Name einer  nordafrikanischen  Stadt,  Algier. Dazu  das  Adj.  gazä^irl;  hieraus  it. ghiazzerino  'Panzerhemd'  [ursprünglich in  Algier  hergestellt],  prov.  jazeran, jazerenc,  afrz.  jazerant,  sp.  jazarina, pg.  jazerina,  jazeräo.  —  [Ableitung  aus lat.  *acennus  bei  Körting,  Lateinisch- romanisches Wörterbuch,  oder  *jaco- zarad,  d.  h.  frz.  jaque  und  garad  'Ring' DE  289  sind  unhaltbar.]  [Eguilaz  427. ML  3947.
698.  Ar.  gazal: 'Liebesgedicht',  das  nicht  weniger  als  7 und  nicht  mehr  als  17  oder  18  Verse zählen  darf  [in  letzterem  Falle  liegt  eine Kasida  vor];  hieraus  z.  B.  frz.  gJiazel,
dtsch.  Gasel  (PLATEN).  [Devic  DEt 128.
699.  Ar.  gazäl:
'Gazelle,  Antilope  dorcas  Lieht.';  die  nord- afrikanische Aussprache  hat  Imäla,  also gazel;  hieraus  sp.  gacela,  pg.  gazella, frz.  gazelle,  it.  gazzella,  rum.  gazelä; engl,  gazelle,  ndl.  gazel,  dtsch.  Gazelle, siihviQä.  gasell;  luss.  gazel'.    [DE  5!71.
700.  Ar.  gazära:
'Fülle  von  Milch  und  Wasser;  Stimmen- gewirr'; hieraus  it.  gazzarra  'Lärm', gazzurro  'Freude,  der  man  durcii Kanonenschüsse  oder  militärische  Musik Ausdruck  gibt',  sp.  algazara,  pg.  alga- zarra  'Kampfgeschrei'.
701.  Ar.  gazwa:
'Kriegszug'  gegea  andere  Beduinen- stämme; hieraus  pg.  gazua,  gaziva [Constancio  Dicc  587  b]  'militärische Expedition;  Raub  und  Erpressung',  frz. razzia,  vvma.razzia,  dtsch.  Razzia  'Streif- zug' (z.  B.  der  Polizei).    [DE  275.
702.  Ar.  (iazza:
Hebr.  '^Azzäh;  gr.  Vdta,  N.  pr.,  Name der  südlichsten  Stadt  an  der  Küste  Pa- lästinas [vgl.  ZDPV  VII,  1/14];  hiernach soll  die  Gaze,  frz.  gaze,  'ein  durchsich- tiger, feiner  Stoff',  benannt  sein.  Da aber  bis  jetzt  keine  Textilindustrie  in älteren  Zeiten  hier  nachgewiesen  ist, muß  die  Etymologie  als  rein  willkürlich angezweifelt  werden;  die  Ableitung  aus kazz  [s.  hier  Nr.  1147]  ist  unbedingt vorzuziehen.
703.  Mal.  gedong:
'Großes  Haus,  besonders  der  Europäer; Faktorei,  Warenlager'  [aus  telugu  gi- dahgi,  giddangi;  tamil  kidangu  'ein Platz,  wo  Waren  liegen',  von  hidu  'lie- gen']; hieraus  angloind.  godoivn,  frz. gotidon  'Faktorei'  der  handeltreibenden Völker  Europas  im  malay  ischen  Archipel ; auch  'Warenhaus,  Laden'  in  allen  chi- nesischen Häfen.  In  Japan,  wo  mangels jeder  anderen  Möglichkeit  alles,  was  eine Familie  an  Schätzen  besitzt,  in  einem benachbarten  Hause  aufbewahrt  wird, bedeutet  godown  im  lokalen  Dialekte dieses  feuersichere  mit  Erd-  oder  Lehm- mauern versehene  Lagerhaus.  [Hobson- Jobson  381/382.  Chamb  AllJap  43. MMM  22.
704.  Tk.  gegelik: 'Nachtgewand,  Nachtmütze'  [aus  gege 'Nacht'  vom  Stamme  ket,  kec  'wegziehen, vorübergehen,  spät.  Abend'  Vämbeiy TktEtWb  S.  99/100,  Nr.  10711  und  Suffix •lik  zur  Angabe  des  Kleidungsstückes, s.  z.  B.  hier  Nr.  260] ;  hieraus  mm.  ghi- gilic  'Nachtmütze'.
Hebr.  Gghinnöm.]
56
705.  Hebr.  (jehiiinöin:
Eiijeiitlich  <jc  ben  Hinttöm  'Garten  des Sohnes  Hinnonis',  N.  pr.,  ein  Ort  in  der Nähe  von  Jerusalem,  an  dem  in  einem Tempel  dem  Moloch  Menschenopfer  dar- gebracht wurden.  Diesen  Greueln  machte König  Josias  ein  Ende,  indem  er  den Platz  zu  einer  Abfuhrslätte  für  Schutt und  Müll  machte.  So  wurde  das  übel- riechende Gehinnom  mit  'Hölle'  synonym. Hieraus  gr.  ye^wa,  lat.  gehenna,  frz. geheime,  engl,  gehenna,  dtsch.  Gehenna, russ.  bulg.  geenna  'Höhle',  daneben  in übertragener  Bedeutung  afrz.  gehene 'Folter,  Qual,  Zwang',  frz.  gene  'Qual, Zwang',  Vb.  ghie)-  'belästigen',  dtsch. genieren  'dass.,  stören';  poln.  zena 'Zwang',  Vb.  zenowad 'genieren''.  [Devic DEt  126.  Karlowicz  415.
706.  Jap.  geisa: 'Berufsmäßige  Sängerin  und  Tänzerin ; Tanzmädchen';  hieraus  in  allen  euro- päischen Sprachen  Geischa,  meist  engl. geisha.    [Chamb  AllJap  467/468.
707.  .Mal.  gekok:
Name  einer  Eidechsenart,  vermutlich wegen  ihres  Rufes,  also  onomatopoetisch [Pijn  202j;  hieraus  mit  Abfall  von  fc [vgl.  bruk  >>eugl.  bfuh  'eine  Fapageien- art',  batak  batta]  engl,  gekko,  gecco, gecko,  ndl.  gekko,  dtsch.  Gecko,  frz.  gecko, sp.  geco  'Ascalobotes'.  [Devic  DEt  126. JAOS  XVII,  139/14^2.
=== LKT kaik context ===
'Wie'i",  tk.  fcey/ 'Befinden,  Wohlbefinden', dessen  Betätigung  im  Sinne  des  Orien- talen vor  allem  träumerisches  Nichtstun beim  Rauchen  und  Kaffeeirinken  ist. Hieraus  rum.  chef  'Lustigkeit,  Wohl- behagen', chefliü,  chefo^  'kreuzfidel', bulg.  kejf,  kef  'Lust,  gute  Laune',  serb. Cef,  ceif,  ceip  'Lust',  poln.  kiejf  'Mittags- ruhe'. [Bern  SlEtWb  499.  De  Sacy ChrAr  II,  479.
1008.  Tk.  kajina:
'Saum,  Umsäumung'  [K61ekian  Kämüs 941 :  kajmak  'gleiten'  vom  Stamme  taj 'glatt,  gleiten'  Vämbery  TktEtWb  S.  161, Nr.  175];  hieraus  russ.  kaima  'Kante, Saum',  klruss.  kajma  'Stickereisaum'. [Bern  SlEtWb  469.
1009.  Tk.  kajinak:
'Milch,  Rahm'  [Kölekian  Kämüs  941]; hieraus  rum.  caimac  'Sahne,  Rahm',  cai- maci  'entrahmen',  bulg.  serb.  kajmak *dass.',  russ.  kaimak  'dicke  Sahne'. [Bern  SlEtWb  469.
Lokotscb,  Etymolog.  Wörterbuch.
1010.  Ar.  kä'iiumakäni :
'Orts-  oder  Distriktsvorsteher'  [aus  ar. käHm  part.  praes.  act.  des  Vbs.  käma 'stehen'  und  makäni  'Ort',  also  etwa 'locum  tenens'],  tk.  kajmakam ;  hieraus rum.  caimacam  'Distriktsvorsteher',  sp. caimacän  'Leutnant'  [DE  245].
1011.  Ar.  kaisärija: 'Ladenreihe,  Bazar'  (noch  jetzt  in  Da- maskus und  Beirtit  Bezeichnung  der großen  Karawanserais,  vom  gr.  Adj. Kaiaapeia,  d.  h.  der  'kaiserliche',  sc. Markt,  vgl.  Dozy  Suppl  II,  432] ;  hieraus sp.  alcaiceria,  alcaeceria,  pg.  alcaqarias, kat.  (alt)  alcaceria  'die  Waren,  die  im Bazar  verkauft  werden'  [DE  76].
1012.  Tk.  kaisy:
'Aprikose,  Malum  armeniacum';  hieraus bulg.  kajsij,  serb.  kajcija  'Aprikose,  Apri- kosenbaum'; rum.  cais  'Aprikosenbaum', cai'sa 'Aprikose',  caisiü  'aprikosenfarben'. [Bern  SlEtWb  469.
1013.  Ar.  kajjäd:
'Fessel'  [vom  Vb.  kajjada  'binden,  fes- seln'] ;  hieraus  mit  ar.  Art.  sp.  alcayata 'Wandhaken,  Hakennagel'  [DE  90].
1014.  Tk.  kajyk:
'Boot;  langer,  sehr  spitz  zulaufender  und von  leichtem  Holze  gebauter  pfeilschnel- ler Kahn';  hieraus  bulg.  serb.  kaik  'Kahn für  10  Mann',  poln.  kaik,  klruss.  kajuk 'Flußboot',  russ.  kaik,  kajuk  'Boot,  Last- schiff ;  rum.  caic  'Bai'ke',  caicgiü  'Barkeii- führer',  it.  caicco  'kleine  Barke  als  Ret- tungsboot, Schaluppe',  siz.  caiccu  auch 'Kuppler',  frz.  culq,  ca'ique,  calc\  ndl. kaick,  engl,  ca'ique  'Schaluppe,  Boot  auf dem  Bosporus  und  dem  Schwarzen Meere'. —  [Hobson-Jobson  143  fragt  mit Recht,  ob  das  Wort  zufällig  oder  durch tk.  Sprachverwandtschaft  hmdurch  mit dem  grönländischen  kajak  gleichlautet]. [Gorjajew  158.  Bern  SlEtWb  469.  Gr SVociSic  229.
1015.  Tk.  kajys:
'Schmaler  Riemen'  [Kelekian  Kämüs 940;  vom  Stamme  kaj  'hart,  fest;  Stein, Fels'  Vämbery  TktEtWb  S.  83,  Nr.  87; vgl.  Cag.  kajrak  'Schleifstein'] ;  hieraus bulg.  serb.  kais  'Riemen'.
1016.  Ar.  kakang: 'Nachtschatten'  [wohl  pers.  Ursprungs]; hieraus  sp.  alquequenge,  pg.  alkekengi, frz.  alkekenge,  dtsch.  Alkakandschi  'Ju- denkirsche, Physalis  alkekengi  oder  Ph. pubecsens  L.'.   [DE  147.   Devic  DEt  24.
1017.  Mal.  kakatüiva:
'Ein  Papagei  des  malayischen  Archipels' [entweder  nur  onomatopoetisch  oder  aus kakak  'Bruder,  Schwester',  tuä  'alt',  also 'alte  Schwester,  alte  Dame',  ein  fami- liärer Namen  für  den  Vogel,  ähnlich  wie
6
```


## [2026-09-06T15:53:39.465Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHN CAIQUE ===\"; sed -n '2885,2915p' PHN.txt\necho \"=== PHN CASAQUE ===\"; sed -n '3320,3350p' PHN.txt\necho \"=== PHN GAZE ===\"; sed -n '5165,5185p' PHN.txt",
 "description": "Pihan entries"
}
```


### [2026-09-06T15:53:39.535Z] TOOL RESULT

```
=== PHN CAIQUE ===
cour de Gonstantinople , et il offre beaucoup de ressemblance
avec l'ancienne robe d'investiture qui portait, chez les Arabes,
le nom de iUX^ [khil^at]. — Les lexicographes français qui
écrivent cafetan ont tort de faire trois syllabes d'un mot qui ne
doit en avoir que deux.
CAÏC ou CAÏQUE, s. m. (t.)
à^^ [?%?] ^^^9^> bateau. Esquif d'une forme gracieuse et
légère , en usage sur la Méditerranée et la mer Noire. L'impor-
tance des caîcs employés à Gonstantinople est réglée sur le
nombre de paires de rames dont ils sont garnis. Il y en a qui
portent depuis une paire jusqu'à cinq paires de rames, nombre
qu'aucun particulier ne peut dépasser; ceux qui sont construits
pour l'agrément des ministres de la Porte ottomane et des
ambassadeurs étrangers ont sept paires de rames. — Le ba-
teau qui sert, les jours de marché, à transporter à Gonstan-86 CAl
tinople les habitants des villages du Bosphore et à les ramener
ensuite chez eux, s'appelle en turc iS^^jb^ [bâzâr qâygliy] ou
caîc du marché. — Comparez avec le mot turc l'italien caicco
et le portugais caxque : cette dernière orthographe se rencontre
comme variante de cote dans les dictionnaires français.
CÂÏDouKAID,s. m. (a.)
Osjb [î^y^^] ch^f* gotwemeur, dérivé de àb [qâd] conduire, guider.
Dans les Etats barbaresques, ce titre désigne les gouverneurs
de provinces, de villes, ou les chefs militaires qui commandent
au moins à cinq cents hommes. — Les étymologistes se sont
trompés en donnant à ce mot le sens de jti^e ou cadi, car il
appartient évidemment à une autre racine. Le titre de caid (oii
<>s»UJl alqâydayec l'article), connu en Espagne depuis la domi-
nation des Maures, indique un fonctionnaire chargé de veiller
à la garde et à la défense d'un château, et dont les attribu-
tions, par conséquent, sont différentes de celles de Yakade
=== PHN CASAQUE ===
CARVI, s. m. (à.)
\^j^[karamyâ] Nom d'une plante de la famille des ciiminées,
et dont les graines ont un goût aromatique. — L'origine
arabe du mot carvi est confirmée par l'espagnol alcaravea et le
portugais alcaravia, au moyen de l'article al conservé» dans
l'une et l'autre langue, devant le terme oriental.
CASAQUE, s. r. (a.)
, ^ 0m T^ [khasîdj] petite tente en poil de chameau, k l'usage des
Arabes nomades, et dressée sur deux ou trois piliers; se dit
aussi d'un vêtement de laine grossière, à larges manches. C'est
surtout dans ce dernier sens que le mot casaque est usité en
français; et son diminutif casaqcin désigne un vêtement court
et négligé, à l'usage des paysannes et des femmes du peuple.
— Il existe aussi en persan un mot qui présente beaucoup
d'analogie avec casaquin, sous le double rapport du sens et de
l'orthographe; c'est ^yjSlyi [qazâkend]y qui veut dire : vêtement
fourré de soie et de coton, porté surtout en temps de guerre;
puis, sorte de vêtement à l'usage des femmes, et couverture de clievud.
Je ne le cite, toutefois, que comme un simple rapprochement.
— On peut comparer avec l'arabe l'italien casacca, qui a sans
doute servi d'intermédiaire au français casaque. — Tourner
casaque se dit proverbialement pour changer de parti,
CASBAT, s. f. (a.)
AMû» [^a«'a&{7t] palais, cliâteau, on forteresse qui défend une ville,
selon le sens qu'on donne au mol qas'abat en Afrique. — C'est
dans la casbat d'Alger que.Houssaïn pacha, dernier souverainCAV 103
musulman de la Régence de ce nom, avait renfermé son riche
trésor. Né vers 1 778, il perdit son trône le 5 juillet 1 83o, après
avoir été battu par les Français, et se retira à Alexandrie,
oii il mourut en i838. Son règne avait duré environ douze
ans. — Le terme arabe s'étant introduit dans notre langue
=== PHN GAZE ===
[A;a/fr] infidèle, ingrat, qui méconnaît Dieu, ou du persan jjS
[guebr] adorateur du feu, et aussi infidèle, impie. Épithète donnée
aux membres encore subsistants de la secte de Zoroastre, aux
ignicoles ou adorateurs du feu. — Voyez Guèbre.
GAZE, s. f. (a.)
yi [qazz]soie> De là vient probablement le motg'a^^, qui dé-
signe un tissu très^lair et très-léger, une étoffe de soie transpa-
rente dont ou fait des voiles ou des robes de luxe. — Comparez
l'espagnol gasa et l'anglais gauze. Celui qui fabrique ou vend
ce genre d'étoffe s'appelle gazier en français, etjly [qazzâz] en
arabe. — Au figuré, gaze s'emploie pour adoucissement d'une
expression trop leste ou d'une raillerie mordante. Jeter de la
gaze sur un discours, c'est voiler ce qu'un récit pourrait con-
tenir de trop libre ou de trop piquant.
GAZELLE, 6. f. (a.)
^\^ [ghazâl] antilope, gazelle, féminin âII^ [ghazâlat]. Mam-
mifère ruminant, à cornes creuses, et qui tient le milieu entre
le daim et la chèvre. Les Grecs et les Romains l'appelaient
dorcas. Il est trè^-répanduen Asie et en Afrique; aussi les poètes
orientaux en font-ils le sujet de fréquentes allusions, en par-
lant de jeunes filles timides ou légères dont ils veulent célébrer176 GAZ
```


## [2026-09-06T15:53:58.924Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== find printed 164 in KNT ===\"; awk 'BEGIN{RS=\"\\f\"} /^|/ {n++; if (n>=182 && n<=186) {print \"----CHUNK \"n\"----\"; print substr($0,1,1500)}}' KNT.txt",
 "description": "Find Kent p.164"
}
```


### [2026-09-06T15:54:00.628Z] TOOL RESULT

```
Exit code 2
=== find printed 164 in KNT ===
awk: line 1: regular expression compile failed (missing operand)
^|
```


## [2026-09-06T15:54:00.976Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD oqyanus ===\"; grep -n \"اوقيانوس\\|أوقيانوس\\|اقيانوس\\|قيانوس\" TAD.txt TAD_pages.txt | head -20\necho \"=== TAD qazz ===\"; grep -n \"^قز\\|قزّ\" TAD.txt | head",
 "description": "Grep TAD"
}
```


### [2026-09-06T15:54:01.041Z] TOOL RESULT

```
=== TAD oqyanus ===
=== TAD qazz ===
```


## [2026-09-06T15:54:04.263Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 182 183 184 185 186; do echo \"----CHUNK $n----\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N{print substr($0,1,1200)}' KNT.txt; done",
 "description": "Kent chunks"
}
```


## [2026-09-06T15:54:05.275Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nwc -c TAD.txt TAD_pages.txt; echo ---; head -40 TAD_pages.txt",
 "description": "Inspect TAD files"
}
```


### [2026-09-06T15:54:06.138Z] TOOL RESULT

```
----CHUNK 182----
sed him, him- self becoming now king in Parsua, later called Ратѕа. Arsames, however, was not put to death, but (as the OP inscriptions tell us) lived on until after his grandson Darius got the throne of the Persian Empire. Thus Hystaspes never was king, and is not counted among the nine Achaemenian kings. Cyrus II thereafter conquered Media and added it to his dominions, and then extended his conquests in all directions. But he did belong by ancestry to the Achaemenian line; one can hardly brand him as a rank outsider.
Possibly Ctesias’ story, as repeated by Nicolaus Damascenus, originated in the line of Darius as a means of discrediting the line of Cyrus and of. justifying Darius in his seizure of the imperial power. The particular occasion might well be the unsuccessful revolt of Cyrus the Younger against his brother Artaxerxes IT, whom Ctesias served as personal physieian. Cf. JAOS 66.211 (1946).
IL SMERDIS AND GAUMATA
According to Behistan 510-513, Cambyses son of Cyrus killed his full-brother Smerdis, with such secrecy that his death was not known to the people; he then invaded Egypt. While he was on this expedition, rebellions developed in Persia and in Media and else
----CHUNK 183----
he field of historical romance. See also PW 3A.710-2, s.v. Smerdis.
III. Tae HELPERS or DARIUS
The names of the six Persian noblemen who co- operated with Darius in slaying Gaumata the false Smerdis, are given in Behistan §68 and in Herodotus 3.70; there is agreement in the names of the first five:
Behistan Herodotus Vi"dafarnd son of Vayaspdra —— Intaphernes {Дата son of 8uxra Otanes son of
Pharnaspes
Gaubaruva son of Mardunitya ^ Gobryas Vidarna son of Bagübigna Hydarnes Bagabuxsa son of Détuvahya ^ Megabyzus Ardumamé son of Vahauka Aspathines
Herodotus, it will be seen, differs from the Behistan account in the name of the father of
Utana-Otanes; but he gives (7.82) Mardonius, the general in the third invasion of Greece, as son of Gobryas, which indicates agreement as to the name of Gobryas’s father. But Megabyzus son of Zopyrus (7.82) may or may not be the Behistan Bagabuxía son of Datuvahya, or his grandson. Herodotus does, in fact, mention all six of the helpers of Darius in passages outside 3.68-88, in passages which may be found in any Index Nomi- num Propriorum to the text of Herodotus.
The Behistan inscription mentions Vidarna again in §25, as defeating one
----CHUNK 184----
rnment in Media and Persia, gathered an army of Medes and Persians and marched toward Babylon, passing near Elam. As he passed he sent orders to the Elamites, and in terror they seized Acina and brought him in fetters to Darius, who slew him ($17).
Darius with his army went on toward Babylon against Nidintu-Bel ($18), and in his absence from Media and Persia several rebellions started (§21)— some perhaps started earlier, but news of them did not reach Darius before he had set out against Nidintu-Bel: (a) that of Vahyazdata in Persia, with the adherence of Sattagydia and perhaps of a faction in Arachosia (§45); (b) that of Martiya in Elam; (с) that of Phraortes in Media, with the adherence of Armenia (§26), of Assyria, and of Parthia, including Hyreania (885); (d) that of Frada in Margiana; (e) that of Egypt; (f) that of Skunkha in Seythia (821).
Darius came upon Nidintu-Bel and his army at the Tigris, forced the crossing, and defeated him in IX 26 ($18), and though Nidintu-Bel rallied his forces and took the offensive, again defeated him at Zazana on the Euphrates, X 2 ($19); he pursued him and his few remaining horsemen to Babylon, took that city and Nidintu-Bel with it, and
----CHUNK 185----
I re- ject this interpretation of the series of sculptures, since it would oblige us to set the death of Frada at the very end of the series, dating his defeat not IX 23, 522/1, but IX 28, 521/0, and thus extending the series of events from 13 months 12 days to 14 months 13 days.
OLD PERSIAN
hered to Phraortes, declared himself King in Sagartia, a distriet of northern Media; he claimed to be of the family of Cyaxares. Darius sent а force of Medes and Persians under Takhmaspada, a Median officer, who defeated and captured Cicantakhma, bringing him to Darius. Darius mu- tilated him and put him to death with torture, at Arbela ($33). Thus ended rebellion in Media (884) ; but there was still a strong rebel force in Armenia, against which Darius sent an Armenian officer named Dadarshi. Dadarshi, thrice attacked by the rebels, defeated them successively at Zuzaya on II 8 (§26), at Tigra on II 18 (§27), and at Uyama on III 9, whereafter he waited for Darius to come and make final governmental dispositions (828). This third battle by Dadarshi was only nine days after Vaumisa in а second engagement beat off the other force of Armenian rebels in the dis- trict of Autiyara, on IT 30; afte
----CHUNK 186----
ugh not mentioned in the Behistan inscription, must have followed in the same or the next year.
V. THE ACCESSION OF XERXES.
In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius had a number of sons, but—-as was Ahuramazda’s desire—he made Xerxes (presumably not his eldest son, though this is not stated in the inscription) the ‘greatest after himself; and when Darius ‘went from the throne,’ Xerxes—as was Ahuramazda's desire—became king on the throne of his father.
The account given by Herodotus 7.1-4 agrees with this, but gives more details: After Darius re- ceived the news that his forces had been defeated at Marathon and somewhat later that Egypt had risen in rebellion, he started preparations for one campaign against the Athenians and another against the Egyptians. Àt this time there was a dispute between Artobazanes, eldest son of Darius by his first wife, a daughter of Gobryas, and Xerxes, eldest son of Darius by Atossa, daughter of Cyrus the Great, whom Darius had married
after his accession to the throne, as to which should have the succession. On the advice of Damaratus, exiled king of Sparta, Xerxes went to his father and pressed his
```


### [2026-09-06T15:54:06.183Z] TOOL RESULT

```
151889 TAD.txt
243285 TAD_pages.txt
395174 total
---
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬




       ‫لحتل‬
    ‫‪ -‬اا لدم‬  ‫‪1‬‬             ‫تت‬             ‫‪7‬‬   ‫‪:‬‬
     ‫امون‬
‫ظ‬     ‫‪1‬‬



      ‫هني بنشره وتصحيحه وتعليق <واشيه‬
                            ‫ا‬


           ‫الو مان‬
              ‫دام‬    ‫ده ل‬




                    ‫« طبعة ثانية ‪6‬‬




                    ‫حل '‬
                    ‫ذكرى الذ ممردص‬
 ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬

 ‫وقلبه ؛ الى من حب اطق وشرف الحق ولا نخاف فسيبيل المقلومةلاتم‬
                                  ‫والى الصديق الصادق فىكرم انلساانية‬


                  ‫عابلممل ي بنابت اباظ‬
                         ‫اهدي هذا الكتاب‬
```


## [2026-09-06T15:54:17.390Z] TOOL CALL #15: Bash

```json
{
 "command": "ls site/pages/246.jpg 2>/dev/null; pdftoppm -f 246 -l 246 -r 300 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg246 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 246"
}
```


### [2026-09-06T15:54:19.798Z] TOOL RESULT

```
site/pages/246.jpg
total 7400
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:54 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     968 Sep  6 11:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6504 Sep  6 11:13 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3402 Sep  6 11:22 c224_n10.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4812 Sep  6 11:28 c224_n12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4744 Sep  6 11:22 c224_n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3203 Sep  6 11:28 c224_n7.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:27 c229_bibua.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5308 Sep  6 11:27 c229_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5313 Sep  6 11:27 c229_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9059 Sep  6 11:50 c237_n18.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2389 Sep  6 11:50 c237_n3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4987 Sep  6 11:52 c239_kandid2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4734 Sep  6 11:52 c239_kandid.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12852 Sep  6 11:52 c239_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4087 Sep  6 11:52 c239_sandarus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7793 Sep  6 11:13 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4371 Sep  6 11:13 c_gacele.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3485 Sep  6 11:16 c_harmathan.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12347 Sep  6 11:20 c_hdr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9147 Sep  6 11:16 c_herman2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3841 Sep  6 11:16 c_herman.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12691 Sep  6 11:20 c_ieuo.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2071 Sep  6 11:26 c_ijlak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14654 Sep  6 11:20 c_ijlak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12239 Sep  6 11:20 c_latis.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6280 Sep  6 11:13 c_mag.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83691 Sep  6 11:19 gen215.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2303 Sep  6 11:25 j.json
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 11:06 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb   37376 Sep  6 11:09 mk201.py
-rw-rw-r-- 1 sfmqrb sfmqrb   77132 Sep  6 11:11 mk207.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61121 Sep  6 11:11 mk208.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80041 Sep  6 11:14 mk214.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67513 Sep  6 11:27 mk217.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74459 Sep  6 11:33 mk218b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   17605 Sep  6 11:25 mk218.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50138 Sep  6 11:24 mk222.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78297 Sep  6 11:32 mk223.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47928 Sep  6 11:38 mk224.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53093 Sep  6 11:40 mk226.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51303 Sep  6 11:39 mk228.py
-rw-rw-r-- 1 sfmqrb sfmqrb   29152 Sep  6 11:37 mk229.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47535 Sep  6 11:47 mk230.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  141781 Sep  6 11:03 pg212hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb  194102 Sep  6 11:05 pg215hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  117034 Sep  6 10:54 pg215.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76564 Sep  6 11:13 pg216.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82798 Sep  6 11:16 pg217.png
-rw-rw-r-- 1 sfmqrb sfmqrb  147278 Sep  6 11:13 pg218hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82099 Sep  6 11:13 pg218.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71937 Sep  6 11:19 pg219.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63280 Sep  6 11:18 pg220.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71497 Sep  6 11:18 pg221.png
-rw-rw-r-- 1 sfmqrb sfmqrb  118895 Sep  6 11:16 pg222hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84108 Sep  6 11:16 pg222.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79615 Sep  6 11:18 pg223.png
-rw-rw-r-- 1 sfmqrb sfmqrb   90848 Sep  6 11:22 pg224hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55412 Sep  6 11:15 pg224.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80963 Sep  6 11:32 pg225.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161218 Sep  6 11:26 pg226hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74322 Sep  6 11:19 pg226.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54381 Sep  6 11:31 pg227.png
-rw-rw-r-- 1 sfmqrb sfmqrb   52519 Sep  6 11:25 pg228.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78760 Sep  6 11:27 pg229hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42112 Sep  6 11:26 pg229.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65310 Sep  6 11:32 pg230.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69894 Sep  6 11:34 pg231.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67111 Sep  6 11:35 pg233.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82071 Sep  6 11:44 pg234.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47149 Sep  6 11:44 pg236.png
-rw-rw-r-- 1 sfmqrb sfmqrb  125593 Sep  6 11:50 pg237hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67972 Sep  6 11:50 pg237.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168221 Sep  6 11:52 pg239hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78380 Sep  6 11:51 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:54:22.869Z] TOOL CALL #16: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg246.png"
}
```


### [2026-09-06T15:54:23.446Z] TOOL RESULT

```

```


## [2026-09-06T15:54:23.444Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T15:54:34.270Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg246.png')\nprint(im.size)\n# node2 persian script area: displayed ~ (1130,640)-(1700,730) *1.65\nim.crop((1180,1030,1720,1220)).resize((2160,760)).save('c246_n2.png')\nim.crop((1490,1400,1970,1500)).resize((1920,400)).save('c246_n6.png')\nim.crop((1300,630,1970,700)).resize((2010,210)).save('c246_caiique.png')\n\"",
 "description": "Crop page regions"
}
```


### [2026-09-06T15:54:36.465Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-06T15:54:38.789Z] TOOL CALL #18: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c246_n2.png"
}
```


### [2026-09-06T15:54:38.992Z] TOOL RESULT

```

```


## [2026-09-06T15:54:38.986Z] INPUT

[Image: original 2160x760, displayed at 2000x704. Multiply coordinates by 1.08 to map to original image.]


## [2026-09-06T15:54:45.969Z] TOOL CALL #19: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c246_caiique.png"
}
```


### [2026-09-06T15:54:46.031Z] TOOL RESULT

```

```


## [2026-09-06T15:54:46.029Z] INPUT

[Image: original 2010x210, displayed at 2000x209. Multiply coordinates by 1.00 to map to original image.]


## [2026-09-06T15:55:04.941Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n++; if ($0 ~ /LEXICON/) print n\": \"substr($0,1,200)}' KNT.txt | head -20\necho \"=== search sayana/keanos ===\"; grep -n -i \"keanos\\|okeanos\\|çayana\\|šiyāna\\|sayana\" KNT.txt | head",
 "description": "Locate Kent lexicon"
}
```


### [2026-09-06T15:55:06.763Z] TOOL RESULT

```
3: � i
тег. E
EAD Мут
OLD PERSIAN
GRAMMAR TEXTS LEXICON
BY ROLAND G. KENT
Professor Emeritus of Indo-European Linguistics
University of Pennsyloania
AMERICAN ORIENTAL SOCIETY NEW EAV
13: 2, minor 134; DPa etc. 185, e 136; DNa 137, b 138, minor 140; DSa etc. 141, f 142, g etc. 144, m etc. 145; DZ 146; DE 147; DH 147; XPa 147, b 148, c ete. 149, g ete. 150, 1 ete. 152; XSa ete. 152; XE 
186: ugh not mentioned in the Behistan inscription, must have followed in the same or the next year.
V. THE ACCESSION OF XERXES.
In XPf, Xerxes gives us an account of his sue- cession to the throne: Darius
187: � asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-
189: ’, as taken by ТИМ. Aiw 322-3; otherwise Hz. Ap! 191-2: hadtya- ‘truth’, with late loss of h-, + deriv. of d-baud- ‘be fragrant’, cf. Av. baoót- ‘fra-
OLD PERSIAN
grance’, therefore 
191: . Skt. apa, Gk.
and, Lt. ab, Gt. af, Gm. ab, NEng. оў, off, pIE *apo. Used with vb. gaud- and in sbb. apaddna-, apa- niydka-; with suffix in apalara-, apara-.
=== search sayana/keanos ===
```


## [2026-09-06T15:55:10.886Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==187' KNT.txt | head -80",
 "description": "Kent lexicon first page"
}
```


### [2026-09-06T15:55:12.830Z] TOOL RESULT

```
� asn. DPd 20; DNa 53; XPh 43, 59; XSc 4°. ata- таш DPd 22; DNa 54; XPh 60. aitä apf. XPh 30, 35.
Ainaira- sb. ‘Ainaira’, a Babylonian, father of Nidintu-Bel; Elam. ha-a-na-a-ra, АКК. a-ni-ri-’, Ainaliralhya gsm. DB 1.77f.
atva- adj. ‘one’ ($150; §204.1): Av. aéva- ‘one’, Gk. Hom. olos, Cypr. orros ‘alone’, pIE *ozyos. ашат, asm. DNa 6, 7; DSe 6°, 6f; DSf 4, 5; DE 8f, 10; XPa 4, 5; XPb 8f, 10; XPe 4, 5; XPd 6, 7; XPf 6, 7; XPh 5,6; XE 9, 10; XV 7, 8; A!Pa 6f°, 8°; A?He 5f, 6; А?Ра 6, 7.
aiš- vb. ‘hasten’, caus. azSaya- ‘send’: Av. aes-, caus. aéaya-, Skt. 15-, caus. esayatz (§117).
fra + aiš- caus. ‘send forth’: Av. fraei-, Skt. .
preg-. frdiSayam ist sg. imf. (§24, §72, 6181, §215) DB 1.82; 2.19, 30, 50, 72f, 82; 3.2, 18, 30, 84; 5.7. frütsaya imf. DB 3.55, 60, 71.
Auliyüra- sb. ‘Autiyara’, a district in Ar- menia: Elam. ha-u-ti-ja-ru-i§, АКК. ú-ti-ņa-a-ri. Auliyàra nsm. DB 2.58f.
Aura- (Le. A*ura-) sb. ‘Lord, God’: Av. ahura-, Skt. dsura- ‘demon’, pIE *esuro- (6148.1). Aurahya Mazdaha gsm. ({36.ГУЬ, $44) XPe 10. Аита ism. DPe 24 (otherwise Bv. BSLP 30.1.70-3, Gr. §179, 8889; ‘downward’, isn. of aura-, zero- grade of avara-, comparative of *ava-, cf. Ау. aora ‘down’). Elsewhere always in cpd. Auramazdah-.
Auramazdāł- sb. ‘Wise Lord, Ahuramazda’, supreme deity of the Zoroastrian religion: Av. пет, ahurd mazda, РМ. óhrmazd, NPers. hormizd; Elam.. u-ra-más-da., Akky u-ra-ma-az-da. ü-ri-mt-
=
-
LEXICON
12-00 a-hu-ru-ma-az-da-’ ete., Gk. 'Opouacdys; in Av., always two words, usually separated in the Gathas and often in reverse order (Kent, Or. Stud. Hon. Pavry 200-8), but in OP always one word except ХРе 10 (844; for Ашт alone, see under Aura-). Cpd. of *ahura- (see Aura-) + *ma(n)dzdhà- with s-suffix (another! view by Pisani, ef. $185.n3); this is cpd. of pIE *menth- (or is the full grade pIE *math-?) seen in Gk. ёшабо› ‘I learned’, + pIE *dh&- ‘put’, see “da- (Pisani, Riv. Stud. Or. 81-2, takes prior element as *mns-, zero-grade to pAr. manas-, after Wacker- nagel-Debrunner, Altind. Gram. 3.282-3): for formation, ef. Skt. érad-dhà- ‘trust’, Lt. crédit. 670, $156.I, 5160.11; decl., $185.IV.
Auramazdà nsm. AmH 7, 10; AsH 5f, 12; DB 1.12, 60; 4.35, 55, 62, 74, 76, 79f; 5.15f; DPd 1, 7, 13, 15f, 23; DPh 8, 9; DNa 1, 31, 51f, 55; DNb 1, 46, 49: DSe 1; DSf 1,8, 14, 57; DSp 1; DSs 1^, 6f; DSt 1?, 7; DZe 1; DE 1; DH 6f, 8; XPa 1, 18, 20; XPb 1, 21; XPc 1, 12, 15; XPd 1, 17; XPf 1, 45, 48; XPg 12; XPh 1, 32, 49f, 52, 57, 60; XSc 4f°; XE 1; XV 1, 25; A!Pa 1°, 22°; A?8e 7; А?Не 1,18, 19; A?Pa 1, 24, Auramazdà-maiy DB 1.24f, 25, 55, 87, 94; 2.24, 34, 891, 45, 54, 60, 68, 86, 96; 3.6, 16f, 37, 44f, 61f, 661, 87; 4.60; DNa 50 -dà- iy, With omission of m* (§52.VI); DSf 19; XPh 45. Auramazdd-taiy DB 4.78. Auramazda-lay (852.11) DB 4.58. Auramazdd-|Sém] DB 5.311.
Auramazdàm asm. DB 1.54f (Auramazám, $52. VI); 5.16, 18f, 32, 34; DPd 211; DNa 54; DSf 15f, 18; XPf 211, 29; XPh 40, 50, 53, 59; XSe 4.
Auramazdéha gsm. AmH 7f; AsH 10; DB 111, 14, 18f, 22f, 26, 60, 68, 70, 88, 94f; 2.3, 25, 35, 40, АЎ, 54f, 60, 68, 86f, 97; 3.6f, 17, 38, 45, 62, 67, 87Ї; 44, 6, 41, 44, 46, 52, 60, 88; 5.16f, 32f; DSF 12, 21°; DSfv 55f°; D812f; XPb 26f; XPd 16; XPg 3,8; X881; XV19. | Auramazdáhà DPd 4,9; DPe 6f; DNa 16, 35, 49, 56{; DNb 6, 47f; DSe 15, 35, 42; XPa 12, 16f; А?Не 16. Auramazdahà (852.1II; $131; $185.IV) X Pf 34, 43; XPh 14, 33, 37, 44; A'Pa 18f.
AM nsm. (842) DSe 50°; DSi 3°; DS} 4, 6°; DSk 4; DSn 2^; D'Sa 3; A*Sa 4° (as gen., 5818.1), 4; A’Sd 3; А?На 5° (as gen), 6. АМташ DSk 5; D8m 3. AMm asm. DSk 4. AMha gsm. DSa 4; ligature ($42) DSk 4. AMha DS] 3°, 5; Аа 3. AMha or АМ№ DSd 3°; DSi 4°; DSm 5°; D8o 3°; D’Sb 4°.
165
Akaufaciya- adj. sb. ‘man of Akaufaka’; pl. a province of the Persian Empire: АКК. a-ku-pi-i-1$. Deriv. of * Akaufaka- ‘Kohistan’, prefix à + kaufa- ‘mountain’ + adj. suffix ($113, 814411; ef. Hz. AMI 8.72; Kent, Lg. 13.298-9). Akaufaciyd npm. XPh 27. |
akarta- adj. ‘not made, no
```


## [2026-09-06T15:55:29.913Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"ocean\\|ὠκεαν\\|okeav\\|Qkeav\" KNT.txt | head\necho \"=== end of chunk 186 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==186' KNT.txt | tail -c 1500",
 "description": "Search Kent for ocean"
}
```


### [2026-09-06T15:55:31.877Z] TOOL RESULT

```
4912:а adv. as prefix and prep. ‘to’; Av. Skt. à, prep. with acc. and abl., ‘to, as far as’ (also with other uses and meanings); pIE *à if = Lt. à ‘from’ (Sturtevant, Lg. 15.145-54), or *0 if = Gk. ó- in ó-xeayós ‘(lying round about), ocean’.
=== end of chunk 186 ===
, gam-, grab-, jan-, bar-, mà-, yam-; in verbal nouns dyadana-, dvahana-, and in the second parts of compounds Adiyabaukna-, Ariyáramna-, Bagabigna-, also in Akaufaciya-.
(2) Postposition attached to loc. sg. and pl. ($270.1V) and in conj. yada.
(3) Prep. with abl.: yàtà à ‘as far as’, DPh 6, 7; DH 5, 6.
(4) Prep. with adv.: DSe 48.
! a- neg. prefix before consonants (867, 67.1, 0182.1; an- antevocalie, q.v.): Av. Skt. a-, Gk. a~, Lt. ?n-, Сте. un-, pIE *n-. See akarta-, ax áaina-, axsata-, Anümaka-, ayaumani-.
* a- demonst. ‘this’: Av. a- as in GAv. gsm. ahé, Skt. a- as in gsm. asyd, Gk. lsn. є 40, Lt. nsn. tod in ecce ‘lo’; pIE *e-. See also aciy, ada-. Decl., $199.
anã ism. DPe 8 (not to Av. Skt. ana-, cf. Mt. MSLP 19.49-52); XPa 14 (with Wb. KIA 109, Mt. Gr. $326; translated by АКК. a-ga-’, Elam. hi ‘this’, which refutes interpretation of Bv. Gr. $368,
$388, as prep. w. inst. ‘throughout’, Av. ana with ace. ‘along, on’, Gk. дра 'along. ahyāyā lsf, DB 447; DNa 11; DSd 2°; DSe 10; DSf 7, 15; DSg lf; DSi lf, 4; DS} 1°; D8m 5°; D8s If, 3°; DSy 2; DZb 3; DZc 5f; DE 17; XPa 8f; XPc 7; ХВ 12, 24; XPh 9f; XPj; XV 13; A!Pa 13; РЬ if; Аа 1; Ае 4; A’Sdb 1 (ahyd de, $52.VI) ; A?Ha If; А°Не 9, 16f; А#Ра 11; Wb 6; We 7f; Wd 7. ahiydyd ($27) XPb 17; XPd 12; XPjv; XE 17.
aita- demonst. ‘this’ ($260. IIT, $266): Av. адіа-, Skt. elá, PAr. *айа-. айа nsn. ($202) DB 1.44, 45; DNa 48. aita-maty DNb 31. ай�
```


## [2026-09-06T15:55:50.544Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PLA leaf 233 (p.218) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==233' incoming/PLA/PLA_pages.txt | head -60",
 "description": "Asbaghi p.218"
}
```


### [2026-09-06T15:55:52.511Z] TOOL RESULT

```
=== PLA leaf 233 (p.218) ===
garamfül                                                                        218                                                 gaöniza


Js          -     garamfül              =    garamful              q.     v.,    syr.       r           mand.     garunpul     1


F-         azz:        "rohe           Seide"                    pers.     kal          °   mp. „kat            3, dtsch.     Gaze     a
          mand.        gaz        5
          Gaze:        "durchsichtiges,                           gitterartiges             Gewebe"              pers.     —> ar.     > sp.”
          frz.        6,


„I     - gazzaz:                  "Seidenzüchter"                        nom.    agent.      v.   gaz.

                                                                                                    7
I y - gazkand:                         "Panzer"              pers.,         dtsch.      Kasack          .


22» - gazüz:                    Pl.     v5 gazz                   q. v.

      .                                                                               +
>          - qusband:                  "Schaf"              — pers. si                 Zustand mp.                „ıoop gospand aw.
          gaospanta               8,


(8 - gasni:                      "Zichorie"                 aus    pers.        „Lk käsni         9,

(ed — giämif:                     "Rosinen"                pers.         10 „us       pers. ;,ifkeäme$,            mand.     qgiSmiS
          (pe)                   11,


      öl          aßnif:             "Koriander"                  pers.            um    gasniz             mp.     oru3    kiöniz,

            ar» giäniz                     12,

ers - gaßniza                          = gaönig              a. v.        „ syr.        aall?,



1.    Macuch           s.       v.
2.    Wahrmund              s.       v.,     Doz2y          s.    v.
3. Farawafi                 s. v.
4.    Littmann              S.       94.
5.    Macuch           S.       v.
6.    Fremdwörterbuch                        s.       v.
7. Muhit              s.    v.,        Wahrig              s. v.
8.    Nyberg           Bd.        IIs,.          v.
9.    BQ.        s.    v.
10.       BQ.     s.       v.,       Wahrmund              s.     v.
11.       Macuch           s.     v.
12.       Löw s. v.,                 Mackenzie               s.    v.,     Farawaßi         s. v.
13.       Brockelmann                  s.    v.
```


## [2026-09-06T15:55:53.575Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN kaz ===\"; grep -n -i \"kaž\\|kaz 'roh\\|Flockseide\\|Rohseide\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i \"Flockseide\\|Rohseide\\|kaz\" HUB.txt | head -20\necho \"=== PHD kac ===\"; grep -n -i \"^kac\\|kač\\|kaz \" PHD.txt | head -20\necho \"=== AFM qazz ===\"; grep -n \"القز\\|قز \" AFM.txt | head -20",
 "description": "Grep Horn/Hübschmann/MacKenzie/Addi Shir"
}
```


### [2026-09-06T15:55:53.694Z] TOOL RESULT

```
=== HRN kaz ===
=== HUB ===
=== PHD kac ===
=== AFM qazz ===
651:الفارسي ومعناه الوعاء وشرنقة القز او 55( ومعناه القدح © ¢ كك . 
1160:( البتاست) فاسي حض وهو صمغ بعلم وتركيتة ساقز ثر ܪܟ 
1751:4 (اليترى والتثراء:والقزي والكانزر :والكائر #والنيكافرر) ري كار 
2244:المحبط ) ٠‏ ܡܠ بالاغة السر 2 والربادة وقز 4 23 ]| ܨ »× أو 
2316:08 والكردي مفنكان ؛ماذا مايه ن القز 10 1 بالفارسة ܓܚ 9 
3105:+ (الروضة ) من الرمل والعشب مستتقع الا تكو النضنت مز القز به 11
```


## [2026-09-06T15:56:03.238Z] TOOL CALL #25: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:1637 --image 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 1637"
}
```


### [2026-09-06T15:56:09.903Z] TOOL RESULT

```
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1637.png
REF: BQT:1637  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 430  OCR-lang: fas

-۱۹۳۷- کزار
همرغی باشد سیاه و سفید واسری بزرگه دارد ؛ و ثالث بالف کشیده و بنون زده . بادرنگه پوبه
و بکر اول هم کفته‌اند - وتخمی هم‌هست‌دوائی | را کوبند و آن دوائی است که بفارسی بالشگو
که آنرا بعربی بزر الابخره و قرریصض خوانند . | خوانند . هر که آزب رکه و تخم و بیخ آن‌قدری
کزنی ۱( < بمعنی تر وخشك‌باشد؛ | در خرقه‌ای کند و با آبریشم محکم ببنددوباخود
و بعی بمعنی گل‌تر وخشك آورده‌اند ؛ و بهردو نگاه دارد هر که اورا بیند دوست دارد ومحبوب
ممتی با کاف فارسی هم آمده است . القلوب کردد .
گزو۱؟ - بح اول و سکون نانی کزوع - بفتح اول و نانی بوا وکشیده
و واو بالت کشیده بروزن فردا » نوعی ازریوای | و بفین نقطه‌دار زده . مپرء گردن‌انان‌وحوانات
است وان میوه‌ای باشد کوهی باندام ساق دست. دیگر باشد را
کزوان ی < بکراول و سکون نی
بیان دوازدهم . .
درکاف تازی با زای فارسی مشتّمل برسی‌وپنج لغخت و کنات
کو « بفتح اول: و سکون ثانی » بمعنی کو اب ۷ »با بای ابجد, پروزن‌ومعنی
کج است که نفیض رات باغد 8 - و قسمی از کجاوه است .
ابر یشم فرومایه ‏ و کم قیمت بود که بعربی‌قز کویند؛ کزاته ۸ < بفتح اول و تای قرشت ,
و بعی کفته‌اند که قز معرب کز است؟ - ویضم یله اپزبشم را کویند.
اول بیخ درخت باشد . کزار > بضم اول بروزن دچار»چینه‌دان
() خم۱ : + بروژن قردا ۰ ۱
۱-رك :کزی . ۴ < کربا(هم.) . ۴ - معرب آن نیز کزوان .
( بکراول ) 2611896 , 616۳08026[16 « دزی ج ۲ ص4۹۳ >. کردی ۴12۷8 ( پسته ) .۰
0 ۳290۷40 ( بنه » بطم )«زاباص ۳۳۳
۴ - بزخم یکزوغ ورا خرد کرد چنین حرب سازند مردان مهرد .:
عجدی مروزی « جهانگیری >.
در لغت فری ص [ه مه بیت بفردوسی نسبت داده شده ولی در شاهنامه تیامده . رالد : فهرست ولف.
۵ کج (همم.) در اوراق مانوی (پارتی) [کا (بمعنی خودسر . فاسد). +گلاژ (بمعنی
خودسری, فاد ) (۳6۲9120...,8505,126,1.0.84 ۸110016 0۶ 1191 ۸ بوطزد۲0)
« نپالی که کر رسته باشد » اگر در تقویم او زبادت تکلفی و تکلیفی رود » بشکند .> « ظهیری
سمرقتدی . سندیاد نامه ص 2۹ ۴ ۰ ‎٩‏ کج عغز (در : غژغاو ) ۳ قز ( معرب ) :
پهلوی 6 ناوادیا ۰.۱۹۲ قن :کردی 5026 ( پیلةٌ آبریشم ) « ژابا ۳۶۹ >. رل :کج :
۷ < کجاره (هم.) . ۸ - دررشیدی آمده:۸ کژانه,پیلهٌ اپربشم» واین مر کست
از «کز» که ابریشم است و « آنه »که برای نسبت است چون شبانه ومغانه و بعی بتای قرشت
گفته‌اند . »
```


## [2026-09-06T15:56:23.401Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\npython3 -c \"\nfrom PIL import Image\nim=Image.open('1637.png'); print(im.size)\nw,h=im.size\nim.crop((0,int(h*0.55),w,h)).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1637_fn.png')\nim.crop((0,int(h*0.30),int(w*0.55),int(h*0.62))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1637_kaz.png')\n\"",
 "description": "Crop BQT page"
}
```


### [2026-09-06T15:56:25.426Z] TOOL RESULT

```
(1650, 2546)
```


## [2026-09-06T15:56:27.576Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/bqt1637_fn.png"
}
```


### [2026-09-06T15:56:27.604Z] TOOL RESULT

```

```


## [2026-09-06T15:56:51.093Z] TOOL CALL #28: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT && cat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/1637.vision.txt <<'EOF'\n[BQT p. 1637 (Borhan-e Qate', ed. Mo'in) — read from the page image 2026-09-06, entry «کژ» and its footnote 6]\n\nکژ - بفتح اول و سکون ثانی، بمعنی کج است که نقیض راست باشد؛ و قسمی از ابریشم\nفرومایه و کم قیمت بود که بعربی قز گویند، و بعضی گفته‌اند که قز معرب کژ است؛ و بعضی\nاول بیخ درخت باشد.\n\nکژاته / کژانه - بفتح اول و تای قرشت، پیلهٔ ابریشم را گویند.\n\n[حاشیهٔ معین، پانوشت ۶ ذیل «کژ»:]\n۶ ـ کج = غژ (در: غژغاو) = قز (معرب)، پهلوی kac «تاوادیا ۱۶۲»، قس: کردی kozé\n(پیلهٔ ابریشم) «ژابا ۳۴۹»، رک: کج.\n\n[پانوشت ۸ ذیل کژانه:]\n۸ ـ در رشیدی آمده: «کژانه، پیلهٔ ابریشم» و این مرکبست از «کژ» که ابریشم است و «انه»\nکه برای نسبت است چون شبانه و مغانه، و بعضی بتای قرشت گفته‌اند.\n\n[پانوشت ۵ ذیل کژ (معنی «کج»):]\n۵ ـ کج (هم.) در اوراق مانوی (پارتی) kj (بمعنی خودسر، فاسد)، kjyft (بمعنی خودسری،\nفساد) (Henning, A list of Middle Persian…, BSOS, IX, 1, p. 84).\nEOF\necho saved; ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | head",
 "description": "Save BQT 1637 vision transcript"
}
```


## [2026-09-06T15:56:51.821Z] TOOL CALL #29: Bash

```json
{
 "command": "sed -n 1,40p tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-06T15:56:52.681Z] TOOL RESULT

```
saved
total 28280
drwxrwxr-x  2 sfmqrb sfmqrb   4096 Sep  6 11:56 .
drwxrwxr-x 11 sfmqrb sfmqrb   4096 Sep  5 16:42 ..
-rw-rw-r--  1 sfmqrb sfmqrb 368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb   1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb 534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb   2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb   1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb 393921 Sep  6 11:40 1219.png
-rw-rw-r--  1 sfmqrb sfmqrb   3603 Sep  6 11:40 1219.txt
```


### [2026-09-06T15:56:52.719Z] TOOL RESULT

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


## [2026-09-06T15:56:59.095Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/kay%C4%B1k\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%DB%8C%D9%82\" \\\n \"https://www.etymonline.com/word/caique\" \\\n \"https://en.wiktionary.org/wiki/caique\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 246, root Kayik: Turkish kayık > Persian qâyeq / Italian caicco / French caïque / English caique\" 2>&1 | tail -3\ndone",
 "description": "Archive Kayik sources"
}
```


### [2026-09-06T15:57:03.956Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/931e3ab7f99b6177.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e4c6d9e6c1a38071.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d730c8b6c37e87f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/98e5b5737d121498.txt
```


## [2026-09-06T15:57:07.219Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== kayık ===\"; grep -n -A12 -i \"^Etymology\" 931e3ab7f99b6177.txt | head -50\necho \"=== قایق ===\"; grep -n -B3 -A12 -i \"Etymology\" e4c6d9e6c1a38071.txt | head -60",
 "description": "Read Turkish kayık pages"
}
```


### [2026-09-06T15:57:07.278Z] TOOL RESULT

```
=== kayık ===
=== قایق ===
59- Toggle Ottoman Turkish subsection 
60-
61- 1.1 
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Derived terms 
69-
70- 1.2.2 
71- Descendants 
72-
73- 1.3 
74- Further reading 
--
82- Alternative forms 
83-
84- 2.2 
85: Etymology 
86-
87- 2.3 
88- Pronunciation 
89-
90- 2.4 
91- Noun 
92-
93- Toggle the table of contents 
94-
95- قایق 
96-
97- 14 languages 
--
167- [ edit ] 
168-
169- قایق 
170: Etymology
171- [ edit ] 
172-
173- Inherited from Proto-Turkic *kiayguk ( “ boat; oar ” ) ; cognate with Azerbaijani qayıq , Crimean Tatar qayıq , Kyrgyz кайык ( kayık ) , Southern Altai кайык ( kayïk ) , Turkmen kayık and Uzbek qayiq .
174-
175- Noun
176- [ edit ] 
177-
178- قایق • ( kayık ) ( definite accusative قایغی ( kayığı ) , plural قایقلر ( kayıklar ) ) 
179-
180- boat , a watercraft propelled by oars and used for transportation of goods, fishing, racing, or military use
181- Synonym: ناو ( nav ) 
182-
--
256-
257- قیق ( qayiq ) ( Tajik ) 
258-
259: Etymology
260- [ edit ] 
261-
262- Borrowed from Turkic . Compare Azerbaijani qayıq , Kazakh қайық ( qayıq ) , Turkish kayık , Turkmen gaýyk .
263-
264- Pronunciation
```


## [2026-09-06T15:57:12.047Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== etymonline caique ===\"; grep -n -i -A6 \"caique\" 0d730c8b6c37e87f.txt | head -40\necho \"=== wikt caique ===\"; grep -n -B2 -A8 \"Etymology\" 98e5b5737d121498.txt | sed -n '1,80p'",
 "description": "Read caique sources"
}
```


### [2026-09-06T15:57:12.124Z] TOOL RESULT

```
=== etymonline caique ===
1:URL: https://www.etymonline.com/word/caique
2-FETCHED: 2026-09-06T15:57:03Z
3-STATUS: 200
4-TITLE: Etymonline - Online Etymology Dictionary
5-
6-Etymonline - Online Etymology Dictionary 
7-
=== wikt caique ===
63-
64- 1.2 
65: Etymology 1 
66-
67- 1.2.1 
68- Alternative forms 
69-
70- 1.2.2 
71- Noun 
72-
73- 1.2.2.1 
--
78-
79- 1.3 
80: Etymology 2 
81-
82- 1.3.1 
83- Noun 
84-
85- 1.4 
86- See also 
87-
88- 1.5 
--
168- Rhymes: -iːk 
169-
170: Etymology 1
171- [ edit ] 
172-
173- Borrowed from French caïque , from Italian caicco , from Ottoman Turkish قایق ( kayık ) , [ 1 ] [ 2 ] from Proto-Turkic *kiayguk ( “ boat, oar ” ) . Cognate with modern Turkish kayık .
174-
175- Alternative forms
176- [ edit ] 
177-
178- caïc , caicco , caieque , caïque , kaik , kaiki , kajik , kayik , saique 
--
211- Turkish: kayık   (tr) 
212-
213: Etymology 2
214- [ edit ] 
215-
216- A caique (parrot) 
217- From Spanish caíque or Portuguese caíque .
218-
219- Noun
220- [ edit ] 
221-
```


## [2026-09-06T15:57:19.756Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/cassock\" \\\n \"https://en.wiktionary.org/wiki/gauze\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%DA%98\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 246, root Kaž: Persian kaž 'raw silk' > Arabic qazz > French gaze/casaque > English gauze/cassock\" 2>&1 | tail -2\ndone",
 "description": "Archive Kaz-root sources"
}
```


### [2026-09-06T15:57:25.053Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/999d776d5f5f714e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b9b6ee713ae56797.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d87ed9b9ecf630da.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/209ce2ae8e8cd086.txt
```


## [2026-09-06T15:57:28.164Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== cassock ===\"; awk '/^Etymology$/{f=1} f' 999d776d5f5f714e.txt | head -30\necho; echo \"=== gauze ===\"; awk '/^Etymology$/{f=1} f' b9b6ee713ae56797.txt | head -30",
 "description": "Read cassock and gauze"
}
```


### [2026-09-06T15:57:29.792Z] TOOL RESULT

```
=== cassock ===

=== gauze ===
```


## [2026-09-06T15:57:33.254Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== cassock ===\"; grep -n -A10 \"^ Etymology$\" 999d776d5f5f714e.txt | sed -n '1,60p'\necho; echo \"=== gauze ===\"; grep -n -A10 \"^ Etymology\" b9b6ee713ae56797.txt | sed -n '1,80p'",
 "description": "Read cassock and gauze etymologies"
}
```


### [2026-09-06T15:57:34.834Z] TOOL RESULT

```
=== cassock ===
170: Etymology
171- [ edit ] 
172-
173- From Middle French casaque ( “ cloak ” ) .
174-
175- Pronunciation
176- [ edit ] 
177-
178- ( UK ) IPA ( key ) : /ˈkasək/ 
179-
180- Audio ( Southern England ) : ( file ) 

=== gauze ===
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Derived terms 
75-
--
91: Etymology 
92-
93- 2.2 
94- Verb 
95-
96- Toggle the table of contents 
97-
98- gauze 
99-
100- 25 languages 
101-
--
193: Etymology
194- [ edit ] 
195-
196- Borrowed from French gaze , from Arabic قَزّ ( qazz , “ silk ” ) .
197-
198- Pronunciation
199- [ edit ] 
200-
201- enPR : gôz , IPA ( key ) : /ɡɔːz/ 
202- Audio ( Southern England ) : ( file ) 
203-
--
427: Etymology
428- [ edit ] 
429-
430- Cf. German gauzen .
431-
432- Verb
433- [ edit ] 
434-
435- gauze 
436-
437- to bark
```


## [2026-09-06T15:57:40.228Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== قز ===\"; grep -n -A14 \"^ Etymology\" d87ed9b9ecf630da.txt | sed -n '1,90p'\necho; echo \"=== کژ ===\"; grep -n -A14 \"^ Etymology\" 209ce2ae8e8cd086.txt | sed -n '1,90p'",
 "description": "Read Arabic qazz and Persian kaž"
}
```


### [2026-09-06T15:57:40.300Z] TOOL RESULT

```
=== قز ===
62: Etymology 1 
63-
64- 1.1.1 
65- Alternative forms 
66-
67- 1.1.2 
68- Pronunciation 
69-
70- 1.1.3 
71- Noun 
72-
73- 1.1.3.1 
74- Declension 
75-
76- 1.1.3.2 
--
80: Etymology 2 
81-
82- 1.2.1 
83- Verb 
84-
85- 1.2.1.1 
86- Conjugation 
87-
88- 1.3 
89- References 
90-
91- 2 
92- Gulf Arabic 
93-
94- Toggle Gulf Arabic subsection 
--
97: Etymology 1 
98-
99- 2.1.1 
100- Alternative forms 
101-
102- 2.1.2 
103- Pronunciation 
104-
105- 2.1.3 
106- Noun 
107-
108- 2.2 
109: Etymology 2 
110-
111- 2.2.1 
112- Noun 
113-
114- 2.2.2 
115- Verb 
116-
117- 2.3 
118- References 
119-
120- 3 
121- Najdi Arabic 
122-
123- Toggle Najdi Arabic subsection 
--
126: Etymology 
127-
128- 3.2 
129- Verb 
130-
131- 4 
132- Old Anatolian Turkish 
133-
134- Toggle Old Anatolian Turkish subsection 
135-
136- 4.1 
137- Alternative forms 
138-
139- 4.2 
140: Etymology 
141-
142- 4.3 
143- Noun 
144-
145- 4.3.1 
146- Related terms 
147-
148- 4.3.2 
149- Descendants 
150-
151- 4.4 
152- References 
153-
154- 4.5 
--

=== کژ ===
65: Etymology 1 
66-
67- 1.2.1 
68- Adjective 
69-
70- 1.2.1.1 
71- Derived terms 
72-
73- 1.2.2 
74- References 
75-
76- 1.3 
77: Etymology 2 
78-
79- 1.3.1 
80- Alternative forms 
81-
82- 1.3.2 
83- Noun 
84-
85- 1.3.2.1 
86- Derived terms 
87-
88- 1.3.3 
89- References 
90-
91- Toggle the table of contents 
--
194: Etymology 1
195- [ edit ] 
196-
197- From Middle Persian [script needed] ( kaž, gaz ) , from Proto-Indo-European *kog- , *keg- , *keng- ( “ peg, hook, claw ” ) . Related to چنگ ( čang ) . Cognate with English hook .
198-
199- Adjective
200- [ edit ] 
201-
202- کژ • ( kaž ) ( comparative کژتَر , superlative کژتَرین ) 
203-
204- alternative form of کج ( kaj , “ crooked ” ) 
205- c. 1260s , Jalāl ad-Dīn Mohammad Rūmī , translated by Reynold A. Nicholson , مثنوی معنوی [ Masnavi-ye-Ma'navi ], volume II, verse 317: و آن فسون دیو در دلهای کژ 
206-میرود چون کفش کژ در پای کژ u ān fasūn-i dēw dar dil-hā-i kaž 
207-mē-rawad čōn kafš-i kaž dar pā-i kaž While the spell of the Devil goes into crooked hearts
208-as a crooked shoe on to a crooked foot. 
--
224: Etymology 2
225- [ edit ] 
226-
227- From Middle Persian [script needed] ( kač ) . Akin to Old Armenian կաճ ( kač , “ felt ” ) , Old Georgian ყაჭი ( q̇ač̣i ) , Proto-Nakh *q̇aač̣ , Aramaic קָזָא / קָאזָא ( qāzzā ) , Arabic خَزّ ( ḵazz ) , قَزّ ( qazz , “ silk ” ) , possibly also Sanskrit कोशज ( kośaja , “ coming from the cocoon, silk ” ) and Ancient Greek χάσδιον ( khásdion , “ a kind of silk-cloth ” ) . (This etymology is missing or incomplete. Please add to it, or discuss it at the Etymology scriptorium .) 
228-
229- Alternative forms
230- [ edit ] 
231-
232- کز ( kaz ) , کج ( kaj ) , غژ ( ġaž ) , قز ( qaz ) 
233-
234- Noun
235- [ edit ] 
236-
237- کژ • ( kaž ) 
238-
```


## [2026-09-06T15:57:58.836Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFA qazz ===\"; grep -n -i \"qazz\\|kazz\\|Rohseide\\|Flockseide\" AFA.txt | head\necho \"=== DEV gaze ===\"; grep -n -i \"^GAZE\\|CASAQUE\\|CAIQUE\" DEV.txt | head\necho \"=== SKT gauze/cassock ===\"; grep -n -i \"gauze\\|cassock\" SKT.txt | head\necho \"=== WEB gauze ===\"; grep -n -i \"gauze,\" WEB_vol1.txt | head -3\necho \"=== KLN kaz/qazz elsewhere ===\"; grep -n -i \"kazagand\\|khazz\\|qazz\" KLN_1966.txt | head",
 "description": "More local greps"
}
```


### [2026-09-06T15:57:58.940Z] TOOL RESULT

```
=== AFA qazz ===
=== DEV gaze ===
1389:Gazelle.  Esp.  gaceln,  gacele,  gacel,  autref.  algacel;  por- tug.  gazella,  ital.  gazzeUa.  De  l'arabe  JIji  ghazâl,  même sons.  Buffon  a  donné  le  nom  à^aJgazelle  h  une  espèce  de
1393:gazelle,  qui,  selon  Giivier,  ne  diiïère  pas  de  la  gazelle proprement  dite.
1508:HoQUETON.  Vieux  français  aiiqueton.  On  a  reconnu  de- puis longtemps  l'identité  de  ce  mot  avec  l'espagnol  al-, coton,  algodon,  coton,  représentant  l'arabe  (^^kiJî  al-qoton. Du  nom  de  la  matière,  le  mot  est  passé  à  l'étoffe  qu'on  en fabriquait  et  ensuite  à  un  vêtement  fait  de  cette  étoffe.  Si l'on  ne  connaissait  à  ce  terme  que  le  sens  de  casaque,  on I  omprendrait  malaisément  que  l'auteur  du  Roman  de  Ron- ivaux  en  eût  pu  faire  un  objet  de  comparaison  avec  une barbe  blanche  dans  ce  vers  ^  :
3530:Gazella ,  p^.  voy.  Gazelle.
3531:Gazelle.
=== SKT gauze/cassock ===
23451:Frtfukfrom  Italian  from  IjUim:  alarm {•.lanim),  alert,  apaitnunt,  arcade,  artii>an, nbum,  battalion,  bulletin,  cab  (i),  cabbage ;!>,  cape  (i),  capriole,  carnival,  cascade, ftfique.  cassock,  cavalcade,  cavalier,  cavalry, Hadel,  colonel,  colonnade,  compliment, DiDpoat,  concert,  concordat,  corporal  (,1), inridor,  cortege,  costume,  countertenor, ttiraos.  douclie.  ducal.  e>cort,  esplanade, icade.  florin,  fracas,  fugue, gabion,  gambol, Viproviae,  incatoadiiie,  infantry,  lavender, Itestring,  macaroon  ?,  manage,  manege, ben.  mizcn,  (.mizzcn),  modeU  motet, msket,  niche,  ortolan,  paladi'i,  palette, ftUet  (3),  parapet,  partisan  \\)t  pastel, rruke,  pilaster,  piniiacc,  piston,  pomade ^mmoile),  pontoon,  ix>puUce,  porcelain, D&lillion.  preconcert,  rtpnsal,  revolt,  rocket 1),  aalad,  sallct,  salmagundi,  saveloy  (ccr* pifts),  scamper,  Bentinel?,  sentry  1,  somer- lult    (Somerset),    sonnet,    spinet,    squad.
=== WEB gauze ===
80625:gauze, n. (Fr. gaze, gauze, said to be from Gaza, in Palestine, where it was first made.]
80626:„l. a very thin, light, loosely woven mate- nial, usually of silk or cotton: also applied to other material of similar open texture; as, wire gauze,
80628:gauze, a. made of or like gauze; gauzy.
=== KLN kaz/qazz elsewhere ===
6685:cassock,  n„  a  long  ecclesiastical  garment.  —  F. cosaque,  fr.  Pers.  kazagand,  ‘a  kind  of  jacket'. The  ending  -and  of  the  Persian  word  was  mis¬ taken  for  a  suff.,  and  consequently  dropped. Cp.  F.  casaquin,  'jacket',  in  which  the  supposed suff.  -and  was  substituted  by  suff.  -in. Derivative:  cassock,  tr.  v.
```


## [2026-09-06T15:58:05.417Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT cassock entry ===\"; grep -n -i \"CASSOCK\\.\" SKT.txt | head; grep -n \"Cassock\" SKT.txt | head\necho \"=== SKT gauze entry ===\"; grep -n \"GAUZE\\|Gauze\" SKT.txt | head\necho \"=== FSD 1707 ocean ===\"; grep -n -i \"ocean, n\\|Okeanos\\|okys\" FSD_vol3.txt | head",
 "description": "Skeat and FSD"
}
```


### [2026-09-06T15:58:05.499Z] TOOL RESULT

```
=== SKT cassock entry ===
=== SKT gauze entry ===
=== FSD 1707 ocean ===
2098:Ing Madeira and four others, In the Atlantic ocean, near the
11755:Ma^rennes', 1 maVen , 2 mi rin , «• A town aud commune ocean, near the coast of California, length, JO rn
35995:ft. Gulf of, an inlet of the Atlantic ocean, nearly enrlosed
48523:to the Atlantle ocean, near Cape Mondego.
```


## [2026-09-06T15:58:13.291Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in FSD_vol1.txt FSD_vol2.txt FSD_vol3.txt FSD_vol4.txt; do echo \"== $f\"; grep -n -i \"okeanos\\|ökeanos\\|Okeavos\\|okys\\|akys\" $f | head -5; done",
 "description": "Search FSD for okeanos"
}
```


### [2026-09-06T15:58:15.077Z] TOOL RESULT

```
== FSD_vol1.txt
== FSD_vol2.txt
== FSD_vol3.txt
== FSD_vol4.txt
```


## [2026-09-06T15:58:18.109Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%E1%BD%A8%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82\" \\\n \"https://en.wiktionary.org/wiki/ocean\" \\\n \"https://en.wiktionary.org/wiki/%D8%A3%D9%88%D9%82%D9%8A%D8%A7%D9%86%D9%88%D8%B3\" \\\n \"https://en.wiktionary.org/wiki/casaque\" ; do\n timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 246, roots Keanos and Kaz: Greek Okeanos > Arabic uqyanus > Persian oqyanus; Latin Oceanus > English ocean; French casaque\" 2>&1 | tail -2\ndone",
 "description": "Archive ocean/casaque sources"
}
```


### [2026-09-06T15:58:21.465Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1eb5155215338938.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/81858fed4a7e19c0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee65922e97dce33c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c0b8bf3785419ff2.txt
```


## [2026-09-06T15:58:25.204Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== Ὠκεανός ===\"; grep -n -A16 \"^ Etymology\" 1eb5155215338938.txt | sed -n '1,60p'\necho; echo \"=== ocean ===\"; grep -n -A10 \"^ Etymology\" 81858fed4a7e19c0.txt | grep -v \"^[0-9]*- *$\" | sed -n '1,60p'",
 "description": "Read Greek Okeanos and ocean"
}
```


### [2026-09-06T15:58:26.890Z] TOOL RESULT

```
=== Ὠκεανός ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
69-
70- 1.3.1 
71- Inflection 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
77- Descendants 
78-
--
156: Etymology
157- [ edit ] 
158-
159- Uncertain, though generally acknowledged to be a non-Indo-European substrate loan, with Beekes noting that the concept of a "world-river" is not native to Indo-European mythology. A possible relationship with the Semitic root *ʕ-w-g ( “ to be crooked, tortuous ” ) (whence Arabic عِوَج ( ʕiwaj , “ crookedness ” ) , Hebrew עוּגָה ( ugá , “ cake ” ) ) has been discussed. [ 1 ] Another possibility includes a derivation from unattested Sumerian *A-ki-an(u) (Water of the Land and Heaven). [ 2 ] 
160-
161- Beekes suggests a Pre-Greek form *ūkʲān- . [ 3 ] Michael Janda has reminded the scientific community of an earlier comparison [ 4 ] with the Vedic dragon Vṛtra 's attribute āśáyāna- “lying on [the waters]”, claiming it to be an exact phonetical transposition of the Greek word, both stemming from Proto-Indo-European *ō-ḱey-m̥[h₁]no- ( “ lying on ” ) , related to κεῖμαι ( keîmai , “ to lie ” ) .
162-
163- Pronunciation
164- [ edit ] 
165-
166- IPA ( key ) : /ɔː.ke.a.nós/ → /o.ce.aˈnos/ → /o.ce.aˈnos/ 
167-
168- ( 5 th BCE Attic ) IPA ( key ) : /ɔː.ke.a.nós/ 
169-
170- ( 1 st CE Egyptian ) IPA ( key ) : /o.ke.aˈnos/ 
171-
172- ( 4 th CE Koine ) IPA ( key ) : /o.ce.aˈnos/ 

=== ocean ===
62: Etymology 
64- 1.2 
65- Pronunciation 
67- 1.3 
68- Noun 
70- 1.3.1 
71- Synonyms 
--
97: Etymology 
99- 2.2 
100- Noun 
102- 2.2.1 
103- Declension 
105- 2.2.2 
106- Derived terms 
--
120: Etymology 
122- 3.2 
123- Pronunciation 
125- 3.3 
126- Noun 
128- 3.3.1 
129- Related terms 
--
140: Etymology 
142- 4.2 
143- Pronunciation 
145- 4.3 
146- Noun 
148- 4.3.1 
149- Declension 
--
166: Etymology 
168- 5.2 
169- Pronunciation 
171- 5.3 
172- Noun 
174- 5.3.1 
175- Declension 
--
192: Etymology 
194- 6.3 
195- Pronunciation 
197- 6.4 
198- Noun 
200- 6.4.1 
201- Declension 
--
209: Etymology 
211- 7.2 
212- Pronunciation 
214- 7.3 
215- Noun 
217- 7.3.1 
218- Declension 
--
383: Etymology
384- [ edit ] 
386: Etymology tree
388- Ancient Greek Ὠκεᾰνός ( Ōkeănós ) der.
```


## [2026-09-06T15:58:39.202Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== ocean English section ===\"; sed -n '380,420p' 81858fed4a7e19c0.txt\necho; echo \"=== أوقيانوس ===\"; grep -n -A12 \"^ Etymology\" ee65922e97dce33c.txt | sed -n '1,70p'",
 "description": "Read ocean and Arabic uqyanus"
}
```


### [2026-09-06T15:58:39.268Z] TOOL RESULT

```
=== ocean English section ===
 [ edit ] 

 A map with the Indian Ocean in dark blue 
 Etymology
 [ edit ] 

 Etymology tree

 Ancient Greek Ὠκεᾰνός ( Ōkeănós ) der. 
 Latin Ōceanus der. 
 Old French occean bor. 
 Middle English *ocean, occean, occian, occyan 
 English ocean 

 From Middle English *ocean , occean , occian , occyan , from Old French occean (later reborrowed or reinforced by Middle French ocean ), from Latin Ōceanus , originally from Ancient Greek Ὠκεανός ( Ōkeanós , “ Oceanus ” , a water deity ) . Displaced native Old English gārseċġ . Also commonly referred to as the ocean sea , the sea of ocean (compare Latin mare ōceanum ; Old French mer oceane , occeanne mer ). Compare Saterland Frisian Oceoan ( “ ocean ” ) , West Frisian oseaan ( “ ocean ” ) , Dutch oceaan ( “ ocean ” ) , German Low German Ozeaan ( “ ocean ” ) , German Ozean ( “ ocean ” ) , Danish ocean ( “ ocean ” ) , Swedish ocean ( “ ocean ” ) , French océan ( “ ocean ” ) , Italian oceano ( “ ocean ” ) . Doublet of Oceanus / Okeanos .

 Pronunciation
 [ edit ] 

 ( Received Pronunciation ) IPA ( key ) : /ˈəʊ.ʃən/ 

 ( US ) IPA ( key ) : /ˈoʊ.ʃən/ 
 Audio ( US ) : ( file ) 

 ( Australia ) IPA ( key ) : /ˈəʉ.ʃən/ 

 ( New Zealand ) IPA ( key ) : /ˈɐʉ.ʃən/ 

 ( Scotland ) IPA ( key ) : /ˈo.ʃən/ 

 ( Wales , without the toe – tow merger ) IPA ( key ) : /ˈoːʃən/ 

 Rhymes: -əʊʃən 

 Hyphenation: o‧cean 

 Noun
 [ edit ] 

 ocean ( countable and uncountable , plural oceans ) 


=== أوقيانوس ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Descendants 
--
139: Etymology
140- [ edit ] 
141-
142- Borrowed from Ancient Greek Ὠκεανός ( Ōkeanós ) . Doublet of قَامُوس ( qāmūs ) .
143-
144- Pronunciation
145- [ edit ] 
146-
147- IPA ( key ) : /ʔuːq.jaː.nuːs/ 
148-
149- Noun
150- [ edit ] 
151-
```


## [2026-09-06T15:58:49.710Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '150,185p' ee65922e97dce33c.txt\necho \"=== casaque ===\"; grep -n -A12 \"^ Etymology\" c0b8bf3785419ff2.txt | sed -n '1,60p'",
 "description": "Descendants of uqyanus; casaque"
}
```


### [2026-09-06T15:58:49.794Z] TOOL RESULT

```
 [ edit ] 

 أُوقْيَانُوس • ( ʔūqyānūs )  ? 

 ( archaic ) ocean 

 Declension
 [ edit ] 

 Declension of noun أُوقْيَانُوس ( ʔūqyānūs )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 أُوقْيَانُوس 
 ʔūqyānūs 

 الْأُوقْيَانُوس 
 al-ʔūqyānūs 

 أُوقْيَانُوس 
 ʔūqyānūs 

 nominative

 أُوقْيَانُوسٌ 
 ʔūqyānūsun 
=== casaque ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Derived terms 
72-
73- 1.3.2 
74- Descendants 
--
154: Etymology
155- [ edit ] 
156-
157- Probably from Italian casacca ( “ jacket, coat ” ) .
158-
159- Pronunciation
160- [ edit ] 
161-
162- IPA ( key ) : /ka.zak/ 
163-
164- Audio : ( file ) 
165-
166- Audio ( France ( Toulouse ) ) : ( file )
```


## [2026-09-06T15:59:02.207Z] TOOL CALL #44: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-06T15:59:02.215Z] TOOL RESULT

```


```


## [2026-09-06T15:59:05.931Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/cassock",
 "prompt": "Give the full etymology text for \"cassock\", including any mention of Turkish quzzak/Cossack or Persian kazagand."
}
```


## [2026-09-06T15:59:06.339Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/gauze",
 "prompt": "Give the full etymology text for \"gauze\", including any mention of Gaza and Arabic qazz."
}
```


### [2026-09-06T15:59:11.392Z] TOOL RESULT

```
# Etymology of Cassock

The word "cassock" dates to the 1540s, originating from French *casaque* meaning "long coat," which corresponds to Spanish *casaca* and Italian *casacca*. The source contains two competing theories about its ultimate origin:

**Turkish Theory:** The term may derive from Turkish *quzzak* meaning "nomad, adventurer," which is also the source of the word "Cossack." This connection reflects the typical riding coats worn by these groups.

**Persian Theory:** Alternatively, it may come from Arabic *kazagand*, traceable to Persian *kazhagand* meaning "padded coat," composed of *kazh* (raw silk) and *agand* (stuffed).

Initially used to describe "a long loose gown or outer cloak," the garment served chiefly as a soldier's cloak during the 16th-17th centuries. Its association with clergy emerged later, around the 1660s, establishing its modern ecclesiastical meaning.
```


### [2026-09-06T15:59:12.352Z] TOOL RESULT

```
# Etymology of Gauze

According to the Online Etymology Dictionary, the word "gauze" dates to the 1560s, derived from French *gaze*, whose origin remains uncertain.

The entry notes two competing theories about the source: "It has been conjectured to be from Arabic *gazz* 'raw silk'" or "from Gaza, Palestinian city associated with production of this fabric." However, the dictionary indicates these remain unconfirmed, stating "there has been no evidence for either."

The related entry for Gaza identifies it as the "Arabic form of Hebrew *'az* 'force, strength.'" The connection to gauze production, while historically suggested, lacks documentary support according to this etymological resource.
```


## [2026-09-06T15:59:25.588Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 120 python3 tools/fetch_source.py \"https://www.etymonline.com/word/cassock\" --note \"page 246, node 3/4: cassock — Turkish quzzak vs Persian kazhagand\" 2>&1|tail -1\ntimeout 120 python3 tools/fetch_source.py \"https://www.etymonline.com/word/gauze\" --note \"page 246, node 7/9: gauze — Arabic gazz vs Gaza\" 2>&1|tail -1\ncd data/verification/sources/refs\necho \"=== ARY قایق/کژ/اقیانوس ===\"; grep -n \"قایق\\|کژ\\|اقیانوس\\|قز\" incoming/ARY/ARY_pages.txt | head -20\necho \"=== MON قایق ===\"; grep -n \"قايق\\|قایق\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10",
 "description": "Archive etymonline, grep ARY and MON"
}
```


### [2026-09-06T15:59:28.594Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/fdb88f3af001ee69.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/59bfcfdac2de8a80.txt
=== ARY قایق/کژ/اقیانوس ===
2133:ااسپالیایی (قز/رم2ی): 3 8 (0. 2
4062:تخاری 8 (8 7( 70207۸7): قزی نا 6 (۳۸37) دام ها
7406:سانسکریت (54(/97007): س84 سوئدی (8۲50[54): ا۷تقزه
12740:۲ چم این وُژه در دْقزیان‌های این فهرست: نخ پشمی» ریسمان (از الیاف گیاهی).
12824:پهلری (1(ماتنه): 6۸8/0۵ بلاقزج بونانی (088): 7332385 ,371873105
13783:00 ,3205 | 6قز روزمیم :ال ما02
16023:فریزی کهن ((لول۴ظ 0ا0): ۸ ایرندی کهن (0لفتقز ۰:00 ۸08 ,080
=== MON قایق ===
MON_part1.txt:2521:از شقایق. |- معر. اذریون» آذربونه] (گیا.) 
MON_part1.txt:4278:مشخص است. شقایق» لاله نعمان... آلاله‌ها 
MON_part1.txt:12507:استخراج حقایق و مطالب. 
MON_part1.txt:13115:نص.) معارف؛ حقایق» علوم. اسم حسنی 
MON_part1.txt:24002:قدس روشن باشدو با آن قوه شخص حقایق 
MON_part1.txt:24989:ببلم: ۰ (.) قایق؛ کرجی. زورق 
MON_part1.txt:28048:چوبین که قایق‌رانان بدان آب رود یا دریا 
MON_part1.txt:38231:حقایق جوهری اشیاء آنچه جوهریت جوهر 
MON_part1.txt:40305:شقایق و خشخاش بکار می‌رفته است؛ تریاق 
MON_part1.txt:40580:هذیان گفتن. انکار حقایق کردن» سوفسطایی
```


## [2026-09-06T15:59:34.390Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor w in \"قایق\" \"کژ\" \"قز\" \"گاز\" \"اقیانوس\"; do\n  echo \"########## $w\"\n  timeout 120 python3 tools/fetch_source.py \"https://vajehyab.com/moein/$w\" --note \"page 246: Mo'in (MON) entry for $w\" 2>&1 | tail -1\ndone",
 "description": "Fetch Mo'in entries from vajehyab"
}
```


### [2026-09-06T15:59:38.876Z] TOOL RESULT

```
########## قایق
/home/sfmqrb/git/rishe/data/verification/sources/web/07dfc22a0d033023.txt
########## کژ
/home/sfmqrb/git/rishe/data/verification/sources/web/be3bebc7dd2fab0a.txt
########## قز
/home/sfmqrb/git/rishe/data/verification/sources/web/fefca8c8557219dd.txt
########## گاز
/home/sfmqrb/git/rishe/data/verification/sources/web/81c7e2b650ada5a9.txt
########## اقیانوس
/home/sfmqrb/git/rishe/data/verification/sources/web/9203b380f87dad0d.txt
```


## [2026-09-06T15:59:42.530Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 07dfc22a0d033023 be3bebc7dd2fab0a fefca8c8557219dd 81c7e2b650ada5a9 9203b380f87dad0d; do echo \"##### $f\"; head -c 1200 $f.txt; echo; done",
 "description": "Read vajehyab results"
}
```


### [2026-09-06T15:59:44.634Z] TOOL RESULT

```
##### 07dfc22a0d033023
URL: https://vajehyab.com/moein/قایق
FETCHED: 2026-09-06T15:59:37Z
STATUS: 200
TITLE: معنی قایق | فرهنگ انتشارات معین | واژه یاب

'
 />

 معنی قایق | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 قایق

 فرهنگ انتشارات معین
 (یِ) [ تر. ] (اِ.) کشتی ، زورق .

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
##### be3bebc7dd2fab0a
URL: https://vajehyab.com/moein/کژ
FETCHED: 2026-09-06T15:59:37Z
STATUS: 200
TITLE: معنی کژ | فرهنگ انتشارات معین | واژه یاب

'
 />

 معنی کژ | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 کژ

 فرهنگ انتشارات معین
 (کَ) (اِ.) 1 - نادرست ، کج . 2 - ابریشم کم قیمت .

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
##### fefca8c8557219dd
URL: https://vajehyab.com/moein/قز
FETCHED: 2026-09-06T15:59:37Z
STATUS: 200
TITLE: معنی قز | فرهنگ انتشارات معین | واژه یاب

'
 />

 معنی قز | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 قز

 فرهنگ انتشارات معین
 (قَ زّ) [ معر. ] (اِ.) ابریشم .

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
##### 81c7e2b650ada5a9
URL: https://vajehyab.com/moein/گاز
FETCHED: 2026-09-06T15:59:38Z
STATUS: 200
TITLE: معنی گاز | فرهنگ انتشارات معین | واژه یاب

'
 />

 معنی گاز | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 گاز

 فرهنگ انتشارات معین
 [ فر. ] (اِ.) 1 - تور نازک و لطیف که برای بستن زخم به کار می رود. 2 - پدالی که در جلوی اتومبیل و در پیش پای راننده قرار دارد و با فشار دادن بر آن بنزین بیشتری به کاربراتور می رسد و اتومبیل سرعت بیشتری می گیرد.

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
##### 9203b380f87dad0d
URL: https://vajehyab.com/moein/اقیانوس
FETCHED: 2026-09-06T15:59:38Z
STATUS: 200
TITLE: معنی اقیانوس | فرهنگ انتشارات معین | واژه یاب

'
 />

 معنی اقیانوس | فرهنگ انتشارات معین | واژه یاب 

 26 فرهنگ 

 همه دیکشنری مترادف طیفی آزاد + 

 همه دقیق مشابه آوا متن آغاز قافیه 

 اقیانوس

 فرهنگ انتشارات معین
 ( اُ ) [ معر. ] ( اِ.) مأخوذ از یونانی . دریای بسیار بزرگ .

 خرید اشتراک افزودن واژه افزونه مرورگر تماس درباره
```


## [2026-09-06T16:00:03.017Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN page marker near caique (line 6107) ===\"; awk 'NR>=6090 && NR<=6120' KLN_1966.txt | grep -o \"^ *[0-9]\\{3\\} *$\" | head\nsed -n '6100,6112p' KLN_1966.txt | grep -n \"2[12][0-9]\" | head\necho \"--- context lines only numbers ---\"; awk 'NR>=6080 && NR<=6130 {if ($0 ~ /^[0-9]+$/) print NR\": \"$0}' KLN_1966.txt\necho \"=== KLN page marker near cassock (6685) ===\"; awk 'NR>=6660 && NR<=6710 {if ($0 ~ /^[0-9]+$/) print NR\": \"$0}' KLN_1966.txt\necho \"=== KLN page marker near gauze (15877) ===\"; awk 'NR>=15850 && NR<=15900 {if ($0 ~ /^[0-9]+$/) print NR\": \"$0}' KLN_1966.txt",
 "description": "Find Klein page markers"
}
```


## [2026-09-06T16:00:03.752Z] TOOL CALL #51: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py TAD:5 --image 2>&1 | head -40",
 "description": "Fetch TAD page 5"
}
```


### [2026-09-06T16:00:04.748Z] TOOL RESULT

```
=== KLN page marker near caique (line 6107) ===
7:220  221
--- context lines only numbers ---
=== KLN page marker near cassock (6685) ===
6672: 246
6673: 247
=== KLN page marker near gauze (15877) ===
15880: 644
15892: 646
```


### [2026-09-06T16:00:06.556Z] TOOL RESULT

```
no scan of TAD covers printed page 5 (see 'scans' in refs_online.json)
```


## [2026-09-06T16:00:14.609Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['TAD'];print(json.dumps(d,ensure_ascii=False,indent=1))\"\necho \"=== leaves count ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' data/verification/sources/refs/TAD_pages.txt\necho \"=== search variants ===\"; grep -n \"قيانوس\\|قيانس\\|اوقيان\" data/verification/sources/refs/TAD_pages.txt | head",
 "description": "TAD metadata"
}
```


### [2026-09-06T16:00:16.277Z] TOOL RESULT

```
{
 "title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640",
 "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"
 ],
 "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the page image",
 "covers_etymology": true,
 "notes": "Arabic OCR fair. Nourai's exact edition unknown; the Beirut reprint reproduces the 1932 pagination."
}
=== leaves count ===
86
=== search variants ===
```


## [2026-09-06T16:00:19.214Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 9 10 11 12; do echo \"===== leaf $n =====\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' TAD_pages.txt | head -40; done",
 "description": "Inspect TAD early leaves"
}
```


### [2026-09-06T16:00:20.865Z] TOOL RESULT

```
===== leaf 9 =====
                             ‫|قنوم ارامية ‪ 9 72‬قَدُوما ‪ 4‬معناه الشخص‬
 ‫في الفارسية ل‪2‬نكر» وفىاليونانية اله عرببها المرساة والموجل‬           ‫اجر‬

 ‫جيل يوناني‪#‬وألعههدوع (إوتجيليون )معناه خير بشارة وبشرى فرح‬
‫(نكليس ) عريها الجرى‬
                   ‫نقليسوحتكلس ‪ -‬يوناني ‪59‬ا‪600‬ي» إ‬
                                                               ‫والثلقوالصباور‬
        ‫هنا أراعى « عرب » أايلغرب‬
                                ‫صلةلولك‬
                                      ‫أجتا‬
                                         ‫اوريا ‏ ايطالي ‪#‬مه‬
                                ‫اوضة ‪ -‬ري وله يشارف عدر‬
‫أوقة‪ 5‬في اللددينية ‪3‬ن وفي اليونانية ‪#‬أعاىتاه براد مهاجزاء من|ثنيعشر‬

              ‫معناه مربع وعربية اليحر البط‬      ‫داتع يوناني ‪56‬‬

‫اوكاريستيا واوخاريستيا يوناني ‪2‬ناوذوداءنظا معناه نعمة وشكر أحسن‬
                                                        ‫وبراد به القريان المقكدس‬
                     ‫‪,‬نصاغوجي ‪ -‬يوناني ‪ ©8808351‬معناه مدخل وتوطئة‬

 ‫ارشّونة وقونة ‪ -‬يوناني ‪ ©7001‬معناءصورة وشبه ومثال وكثال أما نصمة في‬


‫ايطالي قجلاعناا‪ 61‬معناه لغة نفوذ وفي الطب هوالبلنمالوبابي‬          ‫إيتفاونسا‬
                                                            ‫برادفه العزلة الصدرية‬

‫إبوان عبس فارمي <ايوان» براد به قاعة الدار ومشارفها ومله الوان كدري‬




                                ‫بعش أحرها التي يشددها اللمدان ويفتحونها ويرتقولما‬

===== leaf 10 =====
                                    ‫‪5‬‬

                                 ‫درن »‪6‬‬

           ‫بايا في اللاتينية همهم وهو تضعيف أب مقلوبا أي بايا‬
‫(كوين‬
    ‫ل الارض ت‬   ‫كسا‬
                  ‫نلل‬‫بأبللى ‏ دعي اسمهابابللان الرب هناك بلب‬
                ‫« بابيلو » أيباالباله‬   ‫ووت‬
                                          ‫نيةحفب‬
                                               ‫مشور‬
                                                  ‫‏‪ 4:١‬أ)مافي الا‬
‫يابج ‏ فارسي « بابوش » معناه غطاء الرجل وهو داس يلبس في الرجل‬
                        ‫باور ‪. 7‬يطالي عنندمة؟ معناه مخار امدرفه بآخرة‬

‫بواتبم ‪ -‬فارسي « بابونه » وحهشيشة ذات زهر أصفر مكلل بأبيض‬
                                                              ‫يتداوى بها‬
‫بادزص جافاريق عركن من بادأي ضد وزهرأي سم وهو حجر نحمله‬
                                                                 ‫الدجالون‬
‫باديجان ‪ -‬في الفارسية « بادينجان »‪ 6‬نقل الى الاسبانية ‪2‬مئمعمه‪ 8‬ومنها‬
‫الى الافر نسية ‪#‬هنعروطناة ثاملى الايطالية ‪5‬ةنهده؛وم ويقال له في الايطالية‬
‫أيضا هسةتدداءه» و «داعنت في اليونانية معناه اسود فنظر بعضيم الى ظاهر لنظه‬
‫ففسره « بيض المان أو ابن الجنينة ‪ 4‬أما أصل هذا النبات فههنودي فيكون‬
                           ‫اسمه هندي أيضا ويقال له في العربية قهقب حدق‬
‫بارجة ‪ -‬ايطالي هنهعه‪ 1:‬وهو اسمطائر ماي سميت تلك السفينة باسمه‬
                                                   ‫وقد بطل الا ن استءالها‬

‫بارنامج‪ 5-‬فأرسي م كبمن يارأي هرة وحمل وتمأنمه أي كتابورسالة‬
                                    ‫بآرة ‪ -‬فارمي « باره ‪ 6‬معناه قطعة‬

‫بارود ‪ -‬ترك « باروت »©وهو م‪6‬أخنوذ‪1‬مدنادم الافرئسية أى غبار وقد‬
           ‫أطلقوه على الغبار الناري ومنه البارودة يتذف مها الرصاص والخردق‬

===== leaf 11 =====
                                 ‫م‬‫ميه‬
                                    ‫م ل‬




‫وممامدم أي قاس وهو‬
                 ‫مكب م‪6‬ن‪ 5008‬أي قل د‬
                                   ‫باروسيرت يوناني ر‬
                                           ‫تستعمل لنرقة قن الوا وطذعاه‬
‫بارون ‪ -‬ايطاني مهن أصله من لغة جرمانيا ااقديمة ةط ومعناه رجل‬
‫حر كان يتولى قدي أراضي الامراء اعا هو الآن لقب شرف دون الكونت‬
                                                       ‫وهوآخر الالقاب‬
           ‫باز وبازي ‪ -‬فارسي عر بيهالصقر والعقاب واللاعة والحياقية‬
                                                 ‫اسايق ب ينا‬
     ‫وني مه لتههطا معناهملكيوهو لقب لعرق في الذراع‬
  ‫جرل ومن شاه أي ماك وسلطان‬
                          ‫باشا‪ -‬فارسي مركب من باأي لدم و‬
  ‫| باشق ‏ فارسي « باشه » وهو طائر أصشر من العقاب مرادفه يؤيو وج‪1‬م‬
‫بال ايطالي دادم معناه رفش وعربيه قملب ‪:‬قلب به الارضللزراعةأما‬
                        ‫رويب ‪ 8:585‬الابطالي وهومجرفة منحلية '‬
                                                            ‫عفه‬
                                                              ‫تمر‬
                                                                ‫ال‬
‫بال وبالة ‏ لاتيني ‪806‬هلده مناه المستحم وفي اليونانية ‪20‬ئهاها وهو‬
     ‫مأخوذ املفنينيقي « بعليم » أي سيداليموى الأزاحاوتورةا‬
‫حيواناليموهوحوتيبلغملولهالى م‪8‬ث؟را ووزنه الى ‪5‬ك‪6‬ا‪٠‬‏وغرام وليس‬
‫الموت تعريب ‪ 5082‬اليونانى لانه معراب من زمان بعيد قبطس وتعل اليونان‬
                                          ‫| من حوت الاراني‬   ‫أخذوا ‪12‬‬


 ‫بألة ‏ ابطالي ‪ 21126‬معناه كيسوعك وعدل ‪ .‬أما إبالة فمناها حزمة حطب‬
                    ‫‪1‬‬        ‫‪1‬‬                          ‫‪1‬‬       ‫‪89‬‬
                                     ‫بالو‪ -‬ايطالى ‪ 01122‬معناه الرقص‬
                 ‫بالون ‏ ايطالى عمهااةم تناه ‪ 53‬قجزةوعربيه المنطاد‬

‫ممئأة ضمة زهر مرادقه طاقة من رمحان وزهر‬      ‫بأقهس افرنسى ‪110‬‬

                                                              ‫وبحو ذلك‬

===== leaf 12 =====
                                                              ‫عت ات‬


 ‫بأميا ‪ -‬نبات له قرون تطبخ أصله من أهريكا الحو ببة واسمه هناك هطتترمع‬
 ‫و ‪40362‬دمع وعرنوه ياميا لويتئوه ‪1‬اناء وأطل! أي غاذق إزجة وهو من قصيلة‬
                                                                                                                          ‫الخعامي‬

                                                        ‫‪-‬مي « بير ب»راد به هعنردي‬    ‫ار‬‫يفبر‬
                                                 ‫بيغاء ‏ أصل هذا الطائر من الهند واسمه هندي‬
                                 ‫موف المفسول‬
                                           ‫من‬‫لم‬
                                              ‫ايج‬
                                                ‫بت ‪ -‬فارسي ‪ 0‬بت © وهو نس‬
               ‫مول ‪ 0‬ايطالي وتامماءم معناه زيت الحجر والنفط يستخرج منه‬

                ‫وبراد بهترميل من حشسب‬                          ‫دن اليونانية نا‬                  ‫ايطالي ‪06‬‬             ‫بثية ب‬


                                                                   ‫نخت ‪ -‬فارسي « مخت ‪ 4‬معناه حظ‬
                                       ‫‪5‬‬           ‫‪5‬‬                              ‫‪5‬‬                 ‫‪1‬‬          ‫‪١‬‬             ‫‪8‬‏‬
                        ‫>‪ 2‬معئاه عطية وهد‪.‬ه واحسان‬                           ‫فارمي « محش‬                  ‫مخشيش ”' ‪-‬‬


                                                                       ‫‪ 3‬ك‪ 5‬فارسي ‪ 2‬بت» أي صم‬

                                                             ‫باذق ‪ -‬فارسي « باده » أي حر ونبيذ‬
‫فارسي نركطنراقن ‪ 005‬العربيةفيكون معناه صدر البعلة‬                                                                  ‫انرابط‬
                                                                                ‫وهو اسمالعود ملنات الطرب‬
 ‫تقال س والعامة تقول برتقان ‏ نقل البرتغالبونشجرةهذا الليمون»نالمين‬
                                                                       ‫الى أوروبا سنة ‪7148١‬‏ وسميت بأسمهم‬
                                                                    ‫معئاه حصن‬                ‫ييونالي ‪5‬‬               ‫ات‬

 ‫‏‪ )١١‬اعلم ان العمرب تجمل لكل عطية اسم ‪ .‬قاسم مايعطلى الشاعر المائزة ‪ .‬واسم مامطىعن‬

 ‫عن تفاوت الجناياتالا رش واءم ما‪.‬مطى الدليل المالة ‪ .‬واسم مايعطى المفي ‪ .‬المقارة ‪ .‬وام‬
‫واعم مايمعطى الفدير الفلا ‪..‬‬               ‫الملوان ‪5‬‬      ‫ما على الدلال‪ ,‬واأستخم‬                ‫وام‬     ‫اراق اللة‪.‬‬          ‫ماصطي‬

‫واعنمم مامسالطساي السلطاننٍ الاانلااثاووة ‪ .‬ووامم مامع مططي ااسلجطنلدنيداىلاولطويظفهو قاهوماممرهدااععططدايلددىادي لحلز يه ‪.‬وهلرهجزرسرا‬
```


## [2026-09-06T16:00:39.147Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"اوق\\|أوق\\|اوك\\|أوك\" TAD.txt | head -20\necho \"---- TAD.txt around alef section ----\"; grep -n \"يوناني\" TAD.txt | head -20",
 "description": "Search TAD.txt for uqyanus"
}
```


### [2026-09-06T16:00:39.214Z] TOOL RESULT

```
80:على أن رد الاخيل إلى أصل لفته قد أمعاني داش أوقالي ولقيت منه عنتا شاقا 
91:دلغل من استعملبا أنهماوقع بيددقط كتاب أورباوي في عل الكياء اوالطنفات 
255:أوقة 5 في اللددينية 3ن وفي اليونانية #أعاىتاه براد مها جزاء من | ثني عشر 
259:اوكاريستيا واوخار يستيا يوناني 2ناوذوداءنظا معناه نعمة وشكر أحسن 
956:اوكا تعد مك 
1532:ا عاءى ايطالي 2:6 #ناءاوقة معناه امن أي جعله في الامن ويقال 
1869:وائما طاولة المزار تسمى م نم ذل*ى حشنة الحزار .32 بقعم ءا بها الاحم وكل ماوقيت به الاحمعن 
1975:ءا من الاوقبة وقد بزن فلسين وني زماننا هو جزء من كيلوغرام أي من 
2461:حبة الخر توب وكل 54 حبة نساوي أأوقية 
2894:وقرع ودق” وهو امم للنشبة تم لحديدة ثم لطاس من محاس ,قرع لاوقات الصلاة 
2919:3 في -- حبثي « نيجومي » معناه ملك ج ناجاستي ماوك ( جيم مصرية ) 
3221:رسائل هن أعاق دون للاوكاروا لد 
---- TAD.txt around alef section ----
112:ابنوس - ف اليونانية ومدعاة وهو خشب اسود شديد الصلابة شجره ينبت 
145:د غن ب يوناني 2800عم:0 معناه عضو وآ له واز له طرب ذات أناييب 
147:ا يوناني غمائه)261-1 معناه فراش وير ومرقد جيد 
163:إستار يوناني 818167 تاد أزانفة وهو لقن فضة كان يساوي فى أثينا 
195:إمفنج - يوناني 5 معناه منعصر وهو حيوان نحري جسمه متخلخل 
197:انيف يوناني وومزمء 5أمء معناه فى الاصل الملاحظ والمدير وفى عرف 
221:يك - في اللائينية دامه وفي اليونانية وامه معناه مائع وهو عصارة 
224:اقة في اليونانية معاعه معناه وزن و تقل 
231:امام يوناني 025هلة معناه غير مروض مرادفه السامور وهو عند 
235:اناصول واناطول - يوناني 614 معناه الشرق 
236:انين في اليونانية 185 -؟اطلضة معنآه قذر . والظاهر ان أصله فينيقي . 
244:اجر في الفارسية 2 لنكر» وفىاليونانية اله عرببها المرساة والموجل 
246:جيل يوناني #وألعههدوع ( إوتجيليون ) معناه خير بشارة وبشرى فرح 
248:نقليس وحتكلس - يوناني 95ا006ي» ( إنكليس ) عريها الجرى 
255:أوقة 5 في اللددينية 3ن وفي اليونانية #أعاىتاه براد مها جزاء من | ثني عشر 
257:داتع يوناني 65 معناه مربع وعربية اليحر البط 
259:اوكاريستيا واوخار يستيا يوناني 2ناوذوداءنظا معناه نعمة وشكر أحسن 
262:,نصاغوجي - يوناني 1538088© معناه مدخل وتوطئة 
264:ارشّونة وقونة - يوناني 1007© معناءصورة وشبه ومثال وكثال أما نصمة في 
297:أيضا هسةتدداءه» و «داعنت في اليونانية معناه اسود فنظر بعضيم الى ظاهر لنظه
```


## [2026-09-06T16:00:57.241Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TTS kajik ===\"; grep -n -i \"kajik\\|kajyk\\|kaik\\|Kahn\" incoming/TTS/TTS_pages.txt | head -10\necho \"=== HJB caique ===\"; grep -n -i \"caique\\|caïque\\|kaik\" HJB.txt | head -10\necho \"=== HJB p143 ===\"; grep -n -i \"kajak\\|kayak\" HJB.txt | head -5",
 "description": "Grep Vambery and Hobson-Jobson"
}
```


### [2026-09-06T16:00:57.320Z] TOOL RESULT

```
=== TTS kajik ===
956:ait, halt, aik, Jiaik, kaicl, kaik, rufen, schreien,
=== HJB caique ===
4766:CAIQUE.
17023:elliptically  for  the  tombs  of  such  pjer- sonages,  the  circumstance  pertaining to  them  which  chiefly  creates  notoriety or  fame  of  sanctity  ;  and  it  may  be remarked  that  wau  (or  Wely  as  it  is often  written),  Imdmzdda,  Skaikhy  and Marahout  (see  ADJUTANTX  are  often used  in  the  same  elliptical  way  in Syria,  Persia,  Egypt,  and  Barbary  re- spectively. We  may  add  that  Nc^ (Prophet)  is  used  in  the  same  fashion.
20647:1787.— "A  Troop  of  Native  Cavalry  on ^ho  praaent  EstaolishmeDt  oonnste  of  1 ^European  Subaltern,  1  European  Sei^jeant, 1  Sobidar,  3  JemacUun,  4  HavUdarSj  4 Caiques  (naik),  1  Trumpeter,  1  Famer, and  68  Privates."  —  i2^n«.  far  the  H<m. Cam.'p.*i  BUuh  Troops  on  the  Coast  qf  Coro- mandelj  kc.,  p.  6.
24372:1426,  278a Caiman,  177a Cainnor,  1576 Caique,  143^/ Cair,  Ckiro,  234a Cais,  886a Caiu,  1686 Caixa,  1676 Caixem  4856 Cajan,  143a Cajava,  140a Caieput,  143a Caiew,  Cajoo,  1686 Caiori,  477a Caius,  1686 Caksen,  14da Calaat,  4836 Calafatte,  149a Calaim,  Calain,  1456 Calauz,  Calaluz,  1436 Calamander      wood,
=== HJB p143 ===
4773:CSAIQUE,  s.  The  small  skiff  used at  OoDStantinople,  Turkish  kdiJt.  Is  it liy  accident,  or  by  a  radical  connection through  Turkish  tribes  on  the  Arctic shores  of  Siberia,  that  the  Oreenlander's kayak  ia  so  closely  identical?  [The Slanf.  Diet,  says  that  the  latter  word is  Esquimaux,  and  recognises  no  con- nection with  the  former.]
```


## [2026-09-06T16:00:58.150Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"=== Persian section of قایق ===\"; sed -n '200,260p' e4c6d9e6c1a38071.txt",
 "description": "Persian qayeq section"
}
```


### [2026-09-06T16:00:58.198Z] TOOL RESULT

```
=== Persian section of قایق ===

 Descendants
 [ edit ] 

 Turkish: kayık 

 → Armenian: խայեխ ( xayex ) , խայըխ ( xayəx ) , կայեղ ( kayeġ ) 

 → Aromanian: căíḱe , căícă 

 → Bulgarian: каи́к ( kaík ) 

 → Greek: καΐκι ( kaḯki ) 
 → Italian: caicco → English: caicco 
 → French: caïque , caïc , caie → English: caique 
 → Portuguese: caique 
 → Spanish: caique 

 → German: Kaik 

 → Hungarian: kaik , kajik 

 → Russian: каи́к ( kaík ) 

 → Serbo-Croatian: 
 Cyrillic script: ка̀ӣк 
 Latin script: kàīk 

 Further reading
 [ edit ] 

 click to expand

 Barbier de Meynard, Charles ( 1886 ), “ قایق ”, in Dictionnaire turc-français , volume II, Paris: E. Leroux, page 482 

 Çağbayır, Yaşar ( 2007 ), “ kayık1 ”, in Ötüken Türkçe Sözlük (in Turkish), volume 1, Istanbul: Ötüken Neşriyat, page 2493 

 Hindoglu, Artin ( 1838 ), “ قایق ”, in Hazine-i lûgat ou dictionnaire abrégé turc-français ‎ [1] , Vienna: F. Beck, page 354b 

 Kélékian, Diran ( 1911 ), “ قایق ”, in Dictionnaire turc-français ‎ [2] (in French), Constantinople: Mihran, page 941 

 Meninski, Franciszek à Mesgnien ( 1687 ), “Cymba”, in Complementum thesauri linguarum orientalium, seu onomasticum latino-turcico-arabico-persicum, simul idem index verborum lexici turcico-arabico-persici, quod latinâ, germanicâ, aliarumque linguarum adjectâ nomenclatione nuper in lucem editum ‎ [3] , Vienna, column 318 

 Meninski, Franciszek à Mesgnien ( 1680 ), “ قایق ”, in Thesaurus linguarum orientalium, Turcicae, Arabicae, Persicae, praecipuas earum opes à Turcis peculiariter usurpatas continens, nimirum Lexicon Turkico-Arabico-Persicum ‎ [4] , Vienna, column 3605 

 Nişanyan, Sevan ( 2002– ), “ kayık ”, in Nişanyan Sözlük 

 Поленаковиќ , Харалампие ( 2007 ), “319. CǍÍЌE sb. f. pl. cǎiќi (Pascu), CǍÍCǍ”, in Зузана Тополињска, Петар Атанасов , editors, Турските елементи во ароманскиот [ Turskite elementi vo aromanskiot ]‎ [5] , put into Macedonian from the author’s Serbo-Croatian Turski elementi u aromunskom dijalektu (1939, unpublished) by Веселинка Лаброска , Скопје : Македонска академија на науките и уметностите [ Makedonska akademija na naukite i umetnostite ], →ISBN , page 97 

 Redhouse, James W. ( 1890 ), “ قایق ”, in A Turkish and English Lexicon ‎ [6] , Constantinople: A. H. Boyajian, page 1428 

 Persian
 [ edit ] 

 Alternative forms
 [ edit ] 

 قیق ( qayiq ) ( Tajik ) 

 Etymology
 [ edit ]
```


## [2026-09-06T16:01:13.412Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD silk ===\"; grep -n -i \"silk\" PHD.txt PHD_mackenzie.txt | head -15\necho \"=== NYB kac ===\"; grep -n -i \"silk\\|kač\\|kac \" NYB_vol2_glossary.txt | head -10\necho \"=== POK kei liegen ===\"; grep -n \"ḱei-\\|k̂ei-\\|k̑ei-\" POK_02.txt | head -10\necho \"=== AHD watkins kei ===\"; grep -n -i \"^kei-\\|kei-1\\|kei-2\\|To lie\" AHD_watkins1985.txt | head -10",
 "description": "Pahlavi silk and PIE kei"
}
```


### [2026-09-06T16:01:13.517Z] TOOL RESULT

```
=== PHD silk ===
PHD.txt:170:abilag 5/4! | N ~a] blister. a-bim [bym] fearless. āb-kāmag [5A mk! | N ~a] a thick, sour soup. abnüs Pžēnws | (N ābnūs)] ebony. a-biy Pbwd] senseless. ~ih: senselessness. à abr РЫ, Séi | N ~] cloud. M bel abrang [ing | N aurang] glory, splendour. abrastan, abraz- [AP stn',SPc- | М ?br?st, N (afráttan), afrdz-] lift, raise. abraz [Pe | N afrāz] acclivity. abrēšom Pflyš(u)m | M? bryfwm, N ~} silk. ~én [-yn!] silken. abróxtan, abróz- ['piwhtn', ?phoc- | M brwxt, ?)brwc-, N afróxtan, afróz-] light, kindle, illuminate, polish. ~i$n(ih): illumination. āb-tazan Pftcn!] watercourse. a-bun [*dwx!] baseless, bottomless. a-burd-framān ['bwltplm^n'] disobedient. ~th: disobedience. aburnāy f(w)lnd, v. purnāy | N burnā] under age, child. ^h : childhood. aburnáyag [?A(w)/n’(d)yk'] child. abus [pws] (woman) having just given birth. “АҺ: childbirth. арив, -tan Pws, -tn! | M ’bwws, v. ábestan] pregnant. „il: pregnancy. abydxtan, abyóz- Phywhtn', ?bywc-] join, mix. āb-zan zn! | N ~] bath. labzar [el pel] M *6c*7, N afzār] instrument, means; spice. *abzar [6271 | M bail skill, power; powerful. „ūmand [-wmnd] skilled, able. abzāy-, —išn, у. abztidan, abzón [?pzwn! | M, J ”*bzwn, N afzün] increase, growth. ~ig [-yk!] increasing, expansive, bountiful. ~igih: bountifulness. abzüdan, abzáy- ['pzwtn!,^?pzd- | M ?bz'y-, N afzüdan, afzāy-] in- crease, grow. ~i$n: increase, growth. a-čār [cI] inevitable, Jee ~ag [-k'] compelled.
PHD.txt:570:Srēš [slw$ | M sros, N surūš] the god Obedience; cal. 17th day. ~ig [-yk'] obedient. srū [slwb' | N suri(n)] horn, nail, prong. srub [s/(w)p | N usrub] lead. ~ën [-yn'] leaden. srüdan, sray- [s/wtn', sPd- | M sry-, № sur~] sing, recite, play (an in- strument). ~i$n(ih): singing, recitation. srüwar [siwbw!] horned. srūwēn [slwbyn'] horny. stabr [stpl | M stbr, N sitabr] big, coarse, strong. 7-ih : coarseness; strength, force. stabrag [stpik! | Ar. istabrag] shot silk. stadan, stán- [YNSBWN-tn' < A ynsbwn, V nsb | M ‘std, *stn-, N sit~] take. staft [stpt! | M ‘stpt] hard, firm; harsh, tyrannous; very. stahm [sthm | N sitam] power, oppression. ~ag [-k'] strong, oppressive. ~(ag)ih: oppression. stambag [sthmbk! (-h- < stahm) | M ‘stmbg, N sitamba] oppressive; obstinate. “АҺ: oppression; obstinacy. stān-, v. stadan. star [sil] = stāraģ. stárag [st?/k! | M ‘st?rg, N sitara] star. stard [st!/t!] stunned, stupefied, confounded. ~ih: stupidity, stupefaction. : star-Ošmār, -6šmur [stProfm?l, 2wfmwl] astrologer. starwan [stlwn' | N sit~] barren, childless. stáyIdan (s? dytn! | M гуд, N sit~] = stüdan. Stéy [styk! | N. sitéy] erect. sténdag [styndk!] standing, erect. stér [styl | N sitēr] stater. Stézag [styck! | M ‘styz-, N sitéza] quarrel, strife. sti [sty(y) = Av. sti-] being, existence. Std [stwh! | (P *stwb, N sutdh)] distressed, defeated. ~wih : distress. stör [stwl | P ‘stwr, N sutór] horse, mount; large cattle. «bān [-p’n' | N -bàn] (head) groom. --ģāh [-g’s] stable. *stēš [stw$] the fourth morning after death. stówénidan, stówén- [stwhyn-yin'] defeat, overcome, Stówih, v. sto. stüdan, stāy- [stwtn', st?d- | M ‘stwd, ‘st?y-~~, N sit—] praise. ~išn: praise. ~išnīg : praiseworthy.
PHD.txt:3654:Silk abrēšom; shot — stabrag; v. damask.
PHD.txt:3655:silken abréSomén.
PHD_mackenzie.txt:817:abre~om ['plyf(w)m I M 'brylwm, N -] silk.
PHD_mackenzie.txt:818: --en [-yn'] silken.
PHD_mackenzie.txt:4658:stabrag [stplh' , Ar. istabraq] shot silk.
PHD_mackenzie.txt:7578:silk abresom; shot -- stabrag; v.             sleep (v.) xuftan, nibastan.
PHD_mackenzie.txt:7580:silken abresomen.                             sleepless axwamn.
=== NYB kac ===
1128:cihčnitan [cyhynytn'] to make known, to teach, to announce; ētšān O$-c rād cihenit ku . they announced about him that ... 37’, with the gl. kū-šān guft; pres. pass. nč be cihiyom [cyhywm]: I am not informed 51°, with the gl. ku né dānēt, cf s. v. apasthistan, — Paz. cthini- dan Skr. v. jūā- (Aog.); from Av. (428) kač0- ‘to teach’.
1950:w. for ‘wine’. V. further s.v. mad. — The ideogr. is borrowed from the homo- nym ‘thas. — Neriosengh had no inkling either of thas or *has; in 7413-14 he omitted the first KZY and rendered the second by kač, translating it in Skr šīghram ‘quickly’. — V. Nyberg, Henning Vol. op. 345.
2157:kad 1. ['YMT] interrog. when? 75, — 2. Prth ['MT] relative adv. and conj. when HajA:5. — 1. MPrs kyy = kay < kad; NP kai. — 2. MPrth kd. — Av. (434) kada, kača. The habit which some Iranists have taken of rendering SW (BP and inscriptions) "MT with kad is wholly re- jectable, v. s. v. ka.
2294:keš [kyš] faith, religion, both of the Zoroastrian religion and of others, 8015-18, 8212, 108%. — Av. (812 sq.) tkačša-; MPrs kyš ‘doctrine, dogma’; NP kčš (Sn).
2633:nām-cišt [n’mc$t'] especially, particularly 18°; pat ~ 8018. — = Paz.; from nām + cist, pt. of Av. (429 sqq.) kačš- ‘to teach, to assign’.
5268:paoiryo.tkačša: pöryöt- kés
=== POK kei liegen ===
=== AHD watkins kei ===
117:General Terms. It is appropriate to begin with a sampling of basic terms in the lexicon, which have no special cultural value but attest to the richness of the tradition. All are widespread in the family. There are two verbs expressing existence, es- and bheue-, found in English Is, Latin esse, and English BE, Latin fu-turus (FUTURE), respectively. There are verbs “to sit” (sed-'), “to lie” (legh-, kei-'), “to stand” (sta-). There are a number of verbs of motion, like g’a-, “to come,” ei-', “to go,” tera-?, “to cross over,” sek’-', “to follow,“ kei-3, “to set in motion,” and the variants of rolling or turning motion in wel-3, wer-%, k”el-'.
582:kei-'
595:kei-'. To lie; bed, couch; beloved, dear. I. Basic form *kei-. 1. Suffixed form *kei-wo- in: a. Germanic *hiwa- in Old English hiwan, members of a household: HIND?;
596:kei-?
599:kei-2, Referring to various adjectives of color. 1. Suffixed o-grade form *koi-ro- in German *hairaz, “gray-haired,” old, venerable, hence master, in: a. Old English har, gray, hoary: HOAR; b. Old High German hér, worthy, exalted: JUNKER; Cc. Middle Dutch here, master, lord: YOUNKER. 2. Suffixed zero-grade form *ki-wo- in Germanic *hiwam in Old English hiw, héo, color, appearance, form: HUE}. [Pok. 2. Rei- 540.]
600:kei-3. To set in motion. I. Possibly extended o-grade form *koid- with suffixed form *koi-d-ti- in Germanic *haissiz in: a. Old English h&s, a command, a bidding: HEST; b. Old English compound beh#s, a vow, promise, com- mand (be-, intensive prefix; see ambhi): BEHEST (but perhaps to be referred to a separate root *kaid-). Il. Zero-grade form *ki-. 1. Form *ki-eyo- in Latin ciére (past participle citus), with its frequentative citdre, to set in motion, summon: CITE; EXCITE, INCITE, OSCITANCY, RESUSCITATE, SOLICITOUS. 2. Suffixed form *ki-neu- in Greek kinein, to move (> kinésis, motion): KINEMATICS, -KINESIS, KINETIC; CINEMATOGRAPH, CINEMATORADIOG- RAPHY, HYPERKINESIA, KINESIOLOGY, KINESTHESIA, KININ, (TELEKINESIS). [Pok. kei- 538.]
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
661:ladh-. To be hidden. 1. Greek léthé, forgetfulness: LETH- ARGY, LETHE. 2. Zero-grade form *ladh- (< *bdh-), with nasalized form *landh-, in Greek lanthanein (aorist lathein), to escape the notice of, with middle anthanes- thai, to forget: LANTHANUM; ALASTOR. 3. Suffixed (sta- tive) variant form */at-é- in Latin latére, to lie hidden: LATENT. [In Pok. 2. /a- 651.] laiwo-. Left. Latin Jaevus, left: LEVO-; (LEVOROTATION), (LEVOROTATORY). [Pok. laiuo- 652.] laks-. Salmon. Suffixed form */aks-o- in Germanic */ahs- az in Old High German Jahs, salmon: Lox}. [Pok. lak- 653.] laku-. Body of water, lake, sea. 1. Latin /acus, lake, pond, basin: LAKE!. 2. Greek lakkos, cistern: LACCOLITH. 3. O-grade form *loku- in Old Irish and Scottish Gaelic loch, lake: LocH, LouGH. [Pok. laku- 653.] lap-. To light, burn. Nasalized shortened form */a-m-p- in Greek lampein, to shine: LAMP, LANTERN; ECLAMPSIA. [Pok. la(i)p- 652.] las-. To be eager, wanton, or unruly. 1. Suffixed Ger- manic zero-grade form *lustuz in: a. Old English Just, lust: Lust; b. Old High German Just (> German Lust), desire: WANDERLUST; Cc. Germanic denominative verb *lustjan in Old English lystan, to please, satisfy a desire: LisT’, 2. Suffixed form */as-ko- in Latin lJascivus, wan- ton, lustful: Lascivious. [Pok. las- 654.] lat-. Wet, moist. Latin latex, liquid: LaTEx. [Pok. Jat- 654.] lau-. Gain, profit. 1. Suffixed form */au-no- in Germanic *Jaunam in Old High German J6n, reward: GUERDON. 2. Suffixed zero-grade form */u-tlo- in Latin lucrum, gain, profit: LUCRATIVE, LUCRE. 3. Suffixed variant form *low-ero- in Irish Gaelic ledr, sufficiency, enough: GA- LORE. [Pok. ldu- 655.] lé-1. To get. Contracted from “lea-. Suffixed zero-grade form *b-tr- in: a. Greek Jatreia, service (for pay), duties, worship: -LATRY; b. Greek Jatron, pay, akin to the Greek source of Latin latré, robber: LARCENY; c. Greek -/latrés, worshiper: IDOLATER. [Pok. 2. /é(i)- 665.] lé-2, To let go, slacken. Contracted from *les-. 1. Ex- tended form */éd- in: a. Germanic */étan in Old English létan, to allow, leave undone: LET!; b. Germanic deriva- tive *léthigaz, freed, in Medieval Latin /étus, litus, serf (< “free man”): LIEGE. 2. Extended zero-grade form */d- in: a. Germanic */ataz in Old English Zt, late, with its comparative lztra, latter, and its superlative Jatost, last: LATE, LATTER, LAST!; b. Germanic */atjan in Old English lettan, to hinder, impede (< “to make late”): LET?; c. suffixed form */od-to- in Latin lassus, tired, weary: LASSITUDE; ALAS. 3. Suffixed reduced form */é-ni- in Latin lénis, soft, gentle: LENIENT, LENIS, LENITIVE, LENITY. [Pok. 3. lé(i)- 666.] leb-'. Base of loosely related derivatives meaning “hang- ing loosely.” I. Variant form *lep- in Germanic */ap- in Old English lzppa, lappa, flap of a garment: Lap’. II. Nasalized form *lemb(h)-, with variant form *slemb(h)-. 1. Germanic *lemp- probably in obsolete English limphalt, lame (halt, lame; see kel-'): LIMP. 2. Germanic */ump- in: a. Dutch lomp, rag, akin to the Low German source of Middle English Jump, lump: LUMP!; b. possibly obsolete English Jump, lumpfish: LUMPFISH; Cc. German Lumpen, rags: LUMPEN. 3. Ger- manic *slimp- in Middle Dutch slim(p), slanting, bad: SLIM. 4, Middle High German slam, mud: SLUMGULLION. 5. Old Norse slambra, to strike at, akin to the Scandina- vian source of SLAM!. 6. Norwegian slumpa, to slump, akin to the Scandinavian source of sLuMpP. III. Variant *(s)lab- in Germanic *s/ab-. 1. Danish slab, mud, akin to the Scandinavian source of SLAB2. 2. Swedish slabb, slime, mud, akin to the Scandinavian source of Irish slab, mud: sLos. IV. Variants *slap-, *slep-. Germanic *slap- in: a. Low German s/app, slap: SLAP; b. Old Norse slafra, to slaver: SLAVER}. V. Variant */ab-. 1. Germanic *lab- in Old French label, ribbon, strip: LABEL. 2. Latin
667:legh-. To lie, lay. 1. Suffixed form *leg-yo- in: a. Ger- manic */igjan in Old English licgan, to lie: LIE!; b. Ger- manic *lagjan in (i) Old English lecgan, to lay: Lay}, LEDGE, (LEDGER) (ii) Old English belecgan, to cover, surround (be-, over; see ambhi): BELAY. 2. Suffixed form *leg-ro- in Germanic *legraz in: a. Old English Jeger, lair: LAIR; b. Dutch /eger, lair, camp: LEAGUER!; BELEA- GUER; c. Old High German Jegar, bed, lair (> German Lager, store, and Afrikaans lager, laager): LAAGER, LAGER; (STALAG). 3. Celtic *leg-yd- in Medieval Latin lia, sediment: LEES. 4. Lengthened-grade form *légh- in Germanic */égaz, “lying flat,” low, in Old Norse Jagr, low: Low!. 5. Suffixed form */egh-to- in Latin lectus, bed: LITTER; WAGON-LIT. 6. Suffixed o-grade form *logh-o- in Germanic */agam in: a. Old Norse *lagu, lag-, law, “that which is set down” (> Old English Jagu, law): LAW; DANELAW; b. Old Norse Jag, a laying down: FELLOW; c. Old Norse lég, law: OUTLAW; d. Old High German laga (> Middle High German lage > German Lage), act of laying: ANLAGE, VORLAGE. 7. Suffixed o-grade form *logh-o- in Greek lokhos, childbirth, place for lying in wait: LOCHIA. [Pok. legh- 658, 2. légh- 660.]
697:leug-2. To break. Suffixed form *Jeug-é- in Latin ligére, to mourn (? < “to break down mentally”): LUGUBRIOUS. [Pok. leug- 686.] leugh-. To tell a lie. 1. Germanic *leugan in: a. Old English /Zogan, to lie: WARLOCK; b. Old English beléog- an, to tell lies about (be-, about; see ambhi): BELIE. 2. Germanic */ugiz in Old English lyge, a lie, falsehood: LIE’. [Pok. leugh- 686.] leuk-. Light, brightness. I. Basic form */euk-. 1. Suffixed form *leuk-to- in Germanic */euhtam in Old English léoht, liht, light: LicHT). 2. Latin lix, light: Lucrna, LUCULENT, LUX; LUCIFER, LUCIFERIN. 3. Suffixed form *leuk-smen- in Latin limen, light, opening: LIMN, LU- MEN, LUMINARY, LUMINOUS; ILLUMINATE, PHILLUMEN- 1st. 4. Suffixed form *leuk-snd- in Latin lina, moon: LUNA, LUNAR, LUNATE, LUNATIC, LUNE, LUNULA; DEMI- LUNE, SUBLUNARY. 5. Suffixed form */euk-stro- in: a. Latin listrum, purification: LUSTER, (LUSTRUM); b. Latin lastrdre, to purify, illuminate: ILLUSTRATE. 6. Suffixed form *leuko-dhro- in Latin licubrdre, to work by lamplight: LUCUBRATE. II. O-grade form *louk-. 1. Suffixed form *louk-o- in Germanic *lauhaz in Old English /éah, meadow (< “place where light shines”): LEA. 2. Suffixed (iterative) form *lowk-eyo- in Latin liicére, to shine (> licidus, shining): LUCENT, LUCID; ELUCIDATE, NOCTILUCA, PELLUCID, RELUCENT, TRANS- LUCENT. III. Zero-grade form *luk-. 1. Suffixed form *luk-sno- in Greek lukhnos, lamp: LINK?, LYCHNIS. 2. At- tributed by some to this root (but more likely of obscure origin) is Greek lunx, lynx (as if from its shining eyes): LYNX, OUNCE? [Pok. leuk- 687.] leup-. To peel off, break off. 1. Germanic *laubaz in Old English Jéaf, leaf: LEAF. 2. Germanic *laubja, “roof made from bark,” shelter, in: a. Old French loge, lodge: LODGE, (LOGE); b. Medieval Latin lobium, lobia, laubia, monas- tic cloister: LOBBY. 3. Attributed by some to this root is Germanic */uftuz, sky (traditionally explained as < “roof of the world,” vault of heaven), but probably a separate Germanic root, in: a. Old Norse opt, air, attic, sky: LOFT; ALOFT; b. Germanic */uftjan, to hold up in the air, in Old Norse /ypta, to lift: Lirt. [Pok. leup- 690.]
```


## [2026-09-06T16:01:22.403Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD kei-1 full ===\"; sed -n '595p' AHD_watkins1985.txt | head -c 2000\necho; echo \"=== POK kei liegen ===\"; grep -n \"keimai\\|κεῖμαι\\|kei- .liegen\\|„liegen, sich lagern\" POK_01.txt POK_02.txt POK_full.txt | head -10\necho \"=== WLD kei ===\"; grep -n -i \"qei- .liegen\\|kei-, .liegen\\|liegen, Lager\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "AHD kei-1, Pokorny, Walde"
}
```


### [2026-09-06T16:01:22.500Z] TOOL RESULT

```
=== AHD kei-1 full ===
kei-'. To lie; bed, couch; beloved, dear. I. Basic form *kei-. 1. Suffixed form *kei-wo- in: a. Germanic *hiwa- in Old English hiwan, members of a household: HIND?;

=== POK kei liegen ===
=== WLD kei ===
```


## [2026-09-06T16:01:25.856Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '595,598p' AHD_watkins1985.txt | head -c 3000\necho; echo \"=== POK 539 search ===\"; grep -n \"ḱei-\\|k'ei-\\|kei-\" POK_full.txt | head -20",
 "description": "More AHD and Pokorny"
}
```


### [2026-09-06T16:01:25.922Z] TOOL RESULT

```
kei-'. To lie; bed, couch; beloved, dear. I. Basic form *kei-. 1. Suffixed form *kei-wo- in: a. Germanic *hiwa- in Old English hiwan, members of a household: HIND?;
kei-?
b. suffixed Germanic form *hiwid6 in Old English higid, hid, a measure of land (< ‘household”): HIDE®. 2. Suf- fixed form *kei-wi- in Latin civis, citizen (< “member of a
- household”): cITy, CIVIC, CIVIL. II. O-grade form *koi-. 1. Suffixed form *koi-nd- in Latin ciinae, a cradle: INCUNABULUM. 2. Suffixed form *koi-m-d- in Greek koiman, to put to sleep: CEMETERY. III. Suffixed zero-grade form *ki-wo- in Sanskrit siva, auspicious, dear: SHIVA. [Pok. 1. kei- 539.]

=== POK 539 search ===
47064:Root / lemma: kei- 
47070:Root/ lemma: kei-\ to move, go, departure, *die, derived from Root/ lemma: Rei-1\ to lie 
49678:Middle Irish cfar^dark brown' {*kei-ro-), cfarannm. "beetle, chafer'; cir{*kiru-). Gen. cera 
52466:To *kei- "move' (above S. 538 f.) belongs ke[i]so-, kepJsaWvne' in: 
74817:See also: s. also (s)k(h)ed-, skei-, sken-, skeu-6. 
76939:Root / lemma: skei-b""-, -p- nasalized sk/'-m-b'^- 
76958:Indo Germanic skei-p-, -b^- extended from skei-, compare *skai-uo-s {*skai-uo-s) "slant, 
76966:Root / lemma: skei- 
76996:gescheitio *skei-t-) in the meaning ' eliminate ' (compare Old Icelandic 5/r/?a under S. 921) 
76997:Middle Irish sce'i'd^ vomits ' {*skei-ie-ti, Indo Germanic *skei-), verbal n. sceithi. (from 
77026:*kdi-ua, *{s)kei-ua, *{s)kdiua). 
77028:II. Dental extensions skei-d-, -t- {d, /partly present formant, partly the nominal forms-/o- 
77127:of skeit- or skei-d- (compare Latin sc/ssus) based on Old High German scesso "cliff, rock'; 
77131:skei-p-: gr. oKoTiToq m. " the basic beams on which the bricks rest; wall-plate of a 
77161:skei-b- Gothic Old Icelandic Old English skipn. "ship, boat' ("* ausgeschnittener, 
77178:The root Root / lemma: skei-\ (to cut, separate) is detrimental for alb. language because 
77179:alb. people chose it to design clear speech: alb. {*skei-b-), shq/p' c\ear speech, separated 
77690:alb. he, /7/e "shadow' {*sk//a), /?/>■" grace ' (= gr. oKipov), (hjona ^ shadow' {*skei-n-?),
```


## [2026-09-06T16:01:29.133Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '47060,47075p' POK_full.txt | head -c 2500",
 "description": "Pokorny kei- entry"
}
```


### [2026-09-06T16:01:29.198Z] TOOL RESULT

```
References: WP. I 379 f., WH. I 312 f., Trautmann 147. 
Page(s): 596-597 

Root / lemma: kei- 

Meaning: to move, go, departure, *die 

Note: 

Root/ lemma: kei-\ to move, go, departure, *die, derived from Root/ lemma: Rei-1\ to lie 

down. 

Note: (: kai-. kT-); e:/-basis (partly with n-\ni'\x) kT-(n-)eu-, heavy basis kia-{. kie-1)
```


## [2026-09-06T16:01:33.443Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"Page(s): 539\" POK_full.txt | head\necho ---\nn=$(grep -n \"Page(s): 539\" POK_full.txt | head -1 | cut -d: -f1); sed -n \"$((n-70)),$((n+2))p\" POK_full.txt | head -c 3000",
 "description": "Pokorny page 539"
}
```


### [2026-09-06T16:01:35.198Z] TOOL RESULT

```
49666:Page(s): 539-540 
---
Old English haeman). Second composition part -ki-o- in nspioaoc;, vsoaooc;, very probably 
Latin cunae, cunabulaP\. " cradle, nest' ( *Roi-na) and Old Norse hTd, hTdiu. " lair of bears ' 
{*Rei-to-)\ 

Hittite Mediopassiv ki-it-ta {kitta) and ki-it-ta-ri {kittari) "lies'; perhaps also Lycian sij^ni 
"lies' (Pedersen, Lykisch under Hittite 17). 

Note: 

Anatolian Albanian /r-.s-allophones before the kentum : satem differentiation. 

With the concept "home, trusted, dear': 

with Asuffix Old Indie slifa-n. " consuetude, character'. Old Irish ce(/)/e "comrade, 
husband ' {*kef-///o-s), with secondary /cymr. c/Zyofa' "comrade', etc.; 

with /7^suffix: 

Note: 

-/77- suffix is of lllyrian Greek origin. 

gr. KOifjau) (see above), K£i|jr|Aiov " preserved blessing' (from *K£Ttja n. " lair'); 
lengthened grade Kcopn f. "village' {*k^i\ma)\ 

Old Irish coim, cdem'6ear', acymr. cum, ncymr. c^etc. "dear' {ko/mo-); 

Gothic haimsi. (/-stem) "village, dot; PI. aypoi'. Old Norse heimrm. "homeland, world', 
Nng-heimr^ 6\e beim Thing anwesende congregation, meeting'. Old English ham. Old 
Saxon hem. Old High German /7e//77 "homeland, house, dwelling' (Old English haeman 
"sleep on, marry', originally " Koipav '); 

Latvian saimei. " house servants, family ', ablaut. Lithuanian seimynai.. Old Prussian 
se/m/hsm. " servants '; 

Old Church Slavic semt/a' servants, slave', sem/hb' belonging to the servants, slave'; 

Lithuanian k/emas' farmstead, /ra//77as "village', Latvian c/e/775 "village, meeting-house'. 
Old Prussian cay/77/5 "village', Lithuanian /ra//77y/7as"Nachbar', ka/mene'\r\er6' are the 
borrowing from Germanic 77a//775z dubious; 



Trautmann (112 f.) takes ablaut. Proto Baltic *kaima-xx\. and *koima\. an (Indo 
Germanic di\ ai); 

with rosuffix: Armenian ser'leaning, tendency, love', s/rem'\ love' {*Reiro-)\ 

with i/o-suffix: Old Indie seva-{= Germanic hTwa-) " trusted, friendly, dear, worth ', siva- 
(= Germanic *hfwa-) 'intimate, dear, healthful '; 

Latin c/V/s "guarantor' = Oscan ceus6s:, the /-inflection after /7c»5//s(M. Leumann 
Gnomon 9, 237); 

Gothic heiwa-frauja^ householder'. Old English /7/"M/-c^/7o'"homey', hTw-rgeden\. 
"housekeeping'. Old High German hT-raf marriage'. Old English hhred6s., agutn. hT-skepr 
" family ', Old Norse /7y-/?j?//Neutr. PI. " house beings ' (besides ablaut. *hJwa- = Old Indie 
s/'va- in Old Norse herad. Old Swedish hse-rat^^ district, region, area ', hae-skaper^ family ' 
from *hewa-)\ the Germanic stem *hTwa- is composition form *hTwan-^ 
Hausgenossen(schaft) ' in Old Norse hju{n), hjon " married couple, servantship, servants ', 
Old English hTwan, hJgan^ housemate, family ', hTwenu. " household ', asachs. sinhTwun' 
husband'. Old High German h\\A/)un^ married couple, servant', hT(w)o^ husband; 
housemate, farmhand', hfwa^wie', asachs. h/wads.; with -ro- extended Old Norse hyrr 
"friendly, kind, gracious'. Old English heore, /7/e/'e "friendly, gentle ', Middle High German 
g/h/ure 'mM, comfortable'. Mode
```


## [2026-09-06T16:01:45.303Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nn=$(grep -n \"Page(s): 539\" POK_full.txt | head -1 | cut -d: -f1); sed -n \"$((n-140)),$((n-120))p\" POK_full.txt\necho \"=== WLD Bd1 kei liegen ===\"; grep -n \"keimai\\|Koijjai\\|civis\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Pokorny kei header and Walde"
}
```


### [2026-09-06T16:01:47.257Z] TOOL RESULT

```
because of the meaning doubtful alb. //7e/re "fringe, tail ', compare after all the same 
meaning from Norwegian heker corner, tail' under *keg-, 

cymr. cainc{*kanku, compare i/-stem of Old Indie sarjku-), PI. cangau, mcymr. canghau 
"bough'. Middle Irish gee, nir. ^ea^" bough' (with secondary voiced-nonaspirated in aniaut), 
with -sk- suffix gallo-rom. *gascar/a {French Jachere) " arid land', actually " arable field ', 
Hubschmied Vox Rom. Ill 123^; Old Irish gescae^bN'\g, branch, bough'; with /-suffix Old 
Irish cec/7/ "plough' (probably as */r5/7/r-/c»- next-related to Old Indie sakti-); 

Gothic /7o/7a "plough' (= Old Indie sakha). Old High German huohili^ a small arable field 
'; nasalized Old Norse har^ oarlock' {*hanha, Finnish loanword), hse//^peg, plug, stick' 
{*hanhila-); 

Lithuanian saAa "bough' (ablaut, with Old Indie sakha), sake^ fork ', saAa/ys "splinter' (: 
Old Indie sakala-), saknis. Old Prussian sagn/st, Latvian sakne \oot'; Lithuanian sakarnis 



' brachiating ', Latvian sakarnis^ Wurzelenoe '; Old Church Slavic *SQkTD " a tender young 
twig, branch, shoot, sprout, sprig '; 

=== WLD Bd1 kei liegen ===
22660:lat. civis „Biirger" = osk. ceus ds. (dagegen ir. da „Mann", Fick II 4 75 
52735:noti, dhuvati) „schiittelt, bewegt hin und her, facht an“, fut. dhcivisyati ,
```


## [2026-09-06T16:01:50.180Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '22610,22665p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Walde-Pokorny kei- entry"
}
```


### [2026-09-06T16:01:50.231Z] TOOL RESULT

```
Alle weitern Anreiliungen (Fick I 4 42, 209, 420, II 4 74) sind aufzugeben: 
liber lat. casttis (angeblich = ai. gistd-) „ziichtig“, castlgare „ziichtigen“, 
Ca(s)mena s. Yf. LEWI). 2 s. v\\; liber ir. coin „Abgabe, Gesetz“, s. Pedersen 
KG. I 193 (aus lat. canon) ; auch got. hasjan. ags . her inn ,,preisen“, ahd. 
huren (s. auch u. qar- „preisen") „rufen, schreien“ haben ihre Bed. kaum 
aus „anhen'schen“ verschoben. 

1. kei- ..liegen''; aus dem Begriff des Lagers entwickelt sich „Heimstatte“, 
daraus „traut, lieb, d. i. derselben Siedlung angehorigA 

Ai. cetc, av. socle (— gr. xeirai ) „liegt : ‘, ai. gayate, -ti „liegt, ruht“, guy a, 
goyyd „Lager’ (ein dehnstufiges ko[i\no-, ai. ga-na- sucht man — unter Yer- 
gleich mit gr. y.m-uy, s. u. — mit ganz zweifelhaftem Rechte in ai. gma- 
rnnn-, von J. Schmidt Krit. 88 Anm. als „Steinlager“, von Cliarpentier 
IF. 28, 157ff. als ,.Leichenlager*', s. u. knn- „bedecken“, iibersetzt); ai. mad- 
hynma-rf- „in der Mitte sich lagernd, liegend“ u. dgl. 

Gr y.ditat „liege“: horn, y.clovr eg „dormiturientes“, seit der Odyssee auch 
xftefitv. y.elco usw. ..schlafen wollen“ (nach ’Wackernagel KZ. 28, 145, Brug- 
mann IF. 33, 335 aus *y.eu idrrtg erwachsen. mit *y.eu als Lok. des "Wz.- 
nomens als Yerbalabstraktum); liom. xeoxeto ,Jy;ao“ nach Fick KZ. 
44, 143 f. falsche Umschrift fur *y.>)oy.rto == *xt(t)£axtTo. Die Deutung von 
(o-y.eavd g als ,.der auliegendo“, ai. a-gdi/dna-h iBenfey GGA. 1800, 222, 
v. Fierlinger KZ. 27, 477, Brugmann Album Kern 29 Anm. 1, Grdr. II 2 
2,817, IF. 29, 241 Anm. lj w 'rd von Bruckner KZ. 45, 110, Brugmann- 
Thumb GrGr. 4 519 Anm. wohl mit Recht aufgegeben. Horn, ogeo-xmog 
..der sein Lager in den Bergen hat“ (wold - y.oiog , ai. prostika , -gat/ a- ..auf 
einem Ses-cl ruhend" u. dgl., zuletzt Bechtel Lex. 25' 1 ; xohrj xonog m. 



„Lager“, dxomg „Gemahlin" (mit jon. Pailose aus *a-xomg), vgl. bret. 
argud „leichter Schlaf" (* are-koito -, Loth Rc. 22, 334) ; xoiuam , bringe zu 
Bett, schlafere ein“ (vgl. got. haims, air. coim, lett. saime, auch lit. iseimyna ; 
ags. Ji&manl). Zweites Zsglied nach Brugmann IF. 17, 351 ff. in 

jiegiaoog, veoooog, "Aurptooa u. dgl. Sehr wahrscheinlich lat. ciinae, cun fi- 
bula PI. „Wiege, Nest" ( *koi-na ; s. Yf. LEWb. 2 s. v.) und anord. hid, hidi 
n. „Lager des Biiren" ( *kei-to - , Bugge BB. 3, 118; nicht besser nach 
Noreen Ltl. 204 zu an. skide „Scheide" als s-lose Yariante). 

Mit dem Begriffe „Heim, traut, lieb": 

mit ro- Suffix: arm. ser „Ycigung, Liebe", sirem „ich liebe" (* keiro 
Bugge KZ. 32, 25, Scheftelowitz BB. 28, 284); 

mit «o-Suffix: ai. geva- (= germ, hlwa ) „traut, freundlich, lieb, wert", 
giva- (= germ. *hiwa-) „vertraut, lieb, heilsam"; 

lat. civis „Biirger" = osk. ceus ds. (dagegen ir. da „Mann", Fick II 4 75 
ist vielmehr = cia „wer, jemand" s. Falk-Torp u. hjon N. mit Lit., Pedersen KG. 
II 209); got. heiiva-frauja „Hausherr“, ags. hlw-cund „heimisch", hliv-rceden 
f. „Haushaltung“, ahd. hi-rat „IIeirat“, ags. hl-red ds., agutn. hi-slcepr 
„Familie“, anord. hy-byli Neutr. pi. „Hauswesen" (daneben abl. *Jnwa- = 
ai. giva- in anord. herad, aschwed. hce-rab „Bezirk“, hce-skaper „Familie“
```


## [2026-09-06T16:02:22.484Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\npython3 -c \"\nfrom PIL import Image\nim=Image.open('pg246.png')\nim.crop((1030,1290,1500,1380)).resize((1880,360)).save('c246_casaque.png')\n\"",
 "description": "Crop French casaque box"
}
```


### [2026-09-06T16:02:24.495Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T16:02:26.940Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c246_casaque.png"
}
```


### [2026-09-06T16:02:26.960Z] TOOL RESULT

```

```


## [2026-09-06T16:02:39.587Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -n 60,200p /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Read rest of verify_check"
}
```


### [2026-09-06T16:02:39.634Z] TOOL RESULT

```
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


## [2026-09-06T16:02:51.650Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR>=2380 && NR<=2440 {if ($0 ~ /^[0-9]{1,3}$/ || $0 ~ /\\] *[0-9]{2,3}$/ || $0 ~ /^[0-9]{2,3} *$/) print NR\": \"$0}' LKT.txt\necho \"---- lines 2408-2420 ----\"; sed -n '2408,2420p' LKT.txt | cut -c1-200",
 "description": "LKT page markers near kajyk"
}
```


### [2026-09-06T16:02:53.337Z] TOOL RESULT

```
2383: 80
2400: 81
2425: 6
2427: 82
---- lines 2408-2420 ----
1009.  Tk.  kajinak:
'Milch,  Rahm'  [Kölekian  Kämüs  941]; hieraus  rum.  caimac  'Sahne,  Rahm',  cai- maci  'entrahmen',  bulg.  serb.  kajmak *dass.',  russ.  kaimak  'dicke  Sahne'. [Bern  SlEtWb  469.
Lokotscb,  Etymolog.  Wörterbuch.
1010.  Ar.  kä'iiumakäni :
'Orts-  oder  Distriktsvorsteher'  [aus  ar. käHm  part.  praes.  act.  des  Vbs.  käma 'stehen'  und  makäni  'Ort',  also  etwa 'locum  tenens'],  tk.  kajmakam ;  hieraus rum.  caimacam  'Distri
1011.  Ar.  kaisärija: 'Ladenreihe,  Bazar'  (noch  jetzt  in  Da- maskus und  Beirtit  Bezeichnung  der großen  Karawanserais,  vom  gr.  Adj. Kaiaapeia,  d.  h.  der  'kaiserliche',  sc. Markt,  v
1012.  Tk.  kaisy:
'Aprikose,  Malum  armeniacum';  hieraus bulg.  kajsij,  serb.  kajcija  'Aprikose,  Apri- kosenbaum'; rum.  cais  'Aprikosenbaum', cai'sa 'Aprikose',  caisiü  'aprikosenfarben'. [Bern  SlEtWb  469.
1013.  Ar.  kajjäd:
'Fessel'  [vom  Vb.  kajjada  'binden,  fes- seln'] ;  hieraus  mit  ar.  Art.  sp.  alcayata 'Wandhaken,  Hakennagel'  [DE  90].
1014.  Tk.  kajyk:
'Boot;  langer,  sehr  spitz  zulaufender  und von  leichtem  Holze  gebauter  pfeilschnel- ler Kahn';  hieraus  bulg.  serb.  kaik  'Kahn für  10  Mann',  poln.  kaik,  klruss.  kajuk 'Flußboot',  
1015.  Tk.  kajys:
```


## [2026-09-06T16:03:03.680Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.ahdictionary.com/word/search.html?q=cassock",
 "prompt": "Quote the etymology given for \"cassock\" verbatim."
}
```


### [2026-09-06T16:03:08.020Z] TOOL RESULT

```
The etymology for "cassock" is:

"French _casaque_, long military coat, from Middle French, probably originally meaning "Cossack coat" and ultimately (probably via Old Russian _kozakŭ_, free man, Cossack) and of Turkic origin; akin to Tatar _qazaq_, free man, adventurer, and Kazakh _qazaq_, Kazakh"
```


## [2026-09-06T16:03:25.715Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\ntimeout 120 python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=cassock\" --note \"page 246 node 3: modern AHD derives cassock/casaque from Turkic qazaq, not Persian kazagand\" 2>&1|tail -1\ncd data/verification/sources/refs\necho \"=== HRN Seide ===\"; grep -n -i \"Rohseide\\|Flockseide\\|kag\\b\\|kaz\\b\" HRN.txt | head -10\necho \"=== HUB Seide ===\"; grep -n -i \"Seide\" HUB.txt | head -10\necho \"=== RCH kaz ===\"; grep -n -i \"raw silk\" RCH.txt | head -10\necho \"=== TTS kajyk stem ===\"; grep -n -i \"Kahn\\|Boot\" incoming/TTS/TTS_pages.txt | head -5",
 "description": "Horn/Hübschmann/Richardson/Vambery greps"
}
```


### [2026-09-06T16:03:28.496Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/287bd5b7a09272d9.txt
=== HRN Seide ===
22507:, vkag 940.
=== HUB Seide ===
305:65. Np. ahreSum *Seide' ^ arm. LW. aprisum, apresum
308:flir *Seide' sind wohl sammtlich aus dem Neupersischen
4173:abresum *Seide', aatar 'Stern', arj, arz *Werth*, arzls 'Zinn,
4876:phi. apuxS(ly(i)Snlk; abr^am *Seide' = abresum, arm. apriSum;
6124:+ rwJ. Ebenso bei abresum = baresum *Seide', arm. apri-
6173:^tistr = zd. ustra- ; vielleicht auch in abr^um *Seide* = phi.
6239:abresum 'Seide', arm. aprisum ; angubm 'Honig , phi. angpeti^
6614:vuxt 'seiden* (AT.), eigentlich golddurchwebt* ? von zarn =
=== RCH kaz ===
75026:p   Iffy  A   loose  cloak,  especially  of  silk.  A   rope  made  of the  fibres  of  palm-trees.  A   fibry  plant,  of  the  stem  of  which  they make  brushes  for  cleaning  combs.  A   Hiinsy  substance,  like  raw silk,  in  which  they  keep  soap  for  washing  the  body.
=== TTS kajyk stem ===
11273:        um das Boot vorwärts zu bringen, Stütze, Lehne.
```


## [2026-09-06T16:03:35.550Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==191' incoming/TTS/TTS_pages.txt | head -40",
 "description": "Vambery p.161"
}
```


### [2026-09-06T16:03:38.082Z] TOOL RESULT

```
                                                  Ißl



                                                 175.


 Talii, taj, tOff, hüll, glatt, eleu, gleiten,                                   ausgleiten,

                       naschen.

  2.     faÄ;   = glatt, eben, durchweg (nur als Verstiirkungssilbe zu
         ///» gebraucht;    so: tah   = ganz gerade); ^oÄ*a = Regel,
                                                tüjz

        Ordnung, Sitte, d. h. glatte, geordnete Zustände, und da-
        von togru = in gerader Richtung, in Ordnung; togrnt-
        »Ka/i;= gerade machen; talcir                   =
                                       dev feste, glatte Lehmboden
        in der Steppe; kahl, glatzköpfig; takrak = taliir; takirla-
        »»aZ;   =kahl oder glatt machen, ebnen; ^«^'waZ- = gleiten,
                 ifaj^aÄ- = schlüpfrig, glatt.
         glitschen;
«ig.       = schlüpfrig.
         taJiJc
alt. tajls = seichte Stelle eines Flusses.
osm. rfoj/rw = gerade aufrichtig (vgl. cag. togru).
                                ,




            t   wird bei tieferm Einl)lick in den Begriffskreis von glatt,
         fest, hart als eine verwandte         Form der Stammsilbe hil-
         = dürr, getrocknet, trocken erscheinen, und es ist die-
         selbe Veränderung des Anlauts, die wir in der Bezeichnung
         des    Begriffs       von       gleiten,       glitschen        auch anderweitig
         wahrnehmen; so:

osm. /iY^maZ;        = gleiten rutschen; Ä'CfJaZ; = schlüpfrig,
```


## [2026-09-06T16:03:49.071Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 931e3ab7f99b6177 98e5b5737d121498 0d730c8b6c37e87f fdb88f3af001ee69 59bfcfdac2de8a80 287bd5b7a09272d9; do echo \"== $f\"; head -4 $f.txt; wc -c $f.txt; done",
 "description": "Check archived file statuses"
}
```


### [2026-09-06T16:03:50.871Z] TOOL RESULT

```
== 931e3ab7f99b6177
URL: https://en.wiktionary.org/wiki/kay%C4%B1k
FETCHED: 2026-09-06T15:57:01Z
STATUS: 200
TITLE: kayık - Wiktionary, the free dictionary
3283 931e3ab7f99b6177.txt
== 98e5b5737d121498
URL: https://en.wiktionary.org/wiki/caique
FETCHED: 2026-09-06T15:57:03Z
STATUS: 200
TITLE: caique - Wiktionary, the free dictionary
4803 98e5b5737d121498.txt
== 0d730c8b6c37e87f
URL: https://www.etymonline.com/word/caique
FETCHED: 2026-09-06T15:57:03Z
STATUS: 200
TITLE: Etymonline - Online Etymology Dictionary
692 0d730c8b6c37e87f.txt
== fdb88f3af001ee69
URL: https://www.etymonline.com/word/cassock
FETCHED: 2026-09-06T15:59:28Z
STATUS: 200
TITLE: Cassock - Etymology, Origin & Meaning
6051 fdb88f3af001ee69.txt
== 59bfcfdac2de8a80
URL: https://www.etymonline.com/word/gauze
FETCHED: 2026-09-06T15:59:28Z
STATUS: 200
TITLE: Gauze - Etymology, Origin & Meaning
4989 59bfcfdac2de8a80.txt
== 287bd5b7a09272d9
URL: https://www.ahdictionary.com/word/search.html?q=cassock
FETCHED: 2026-09-06T16:03:28Z
STATUS: 200
TITLE: American Heritage Dictionary Entry: cassock
4643 287bd5b7a09272d9.txt
```


## [2026-09-06T16:03:55.625Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '5,60p' 931e3ab7f99b6177.txt | tr -s '\\n' ' ' | head -c 1200; echo; echo \"=== etymonline cassock ===\"; grep -n -i \"quzzak\\|kazagand\\|kazhagand\" fdb88f3af001ee69.txt | head",
 "description": "Check kayık and etymonline archives"
}
```


### [2026-09-06T16:03:55.697Z] TOOL RESULT

```
 kayık - Wiktionary, the free dictionary Jump to content Main menu Main menu move to sidebar hide Navigation Main page Community portal Requested entries Recent changes Random entry Help Glossary Contact us Special pages Search Search Appearance Donations Create account Log in Personal tools Donations Create account Log in Contents move to sidebar hide Beginning 1 Turkish Toggle Turkish subsection 
=== etymonline cassock ===
25: 1540s, "long loose gown or outer cloak," from French casaque "long coat" (16c.), corresponding to Spanish casaca , Italian casacca , probably ultimately from Turkish quzzak "nomad, adventurer," (the source of Cossack ), from their typical riding coat. Or perhaps from Arabic kazagand , from Persian kazhagand "padded coat," from kazh "raw silk" + agand "stuffed." Chiefly a soldier's cloak 16c.-17c.; ecclesiastical use is from 1660s.
```


## [2026-09-06T16:05:23.503Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN ocean ===\"; grep -n \"ocean,  n\" KLN_1966.txt | head -3\necho \"=== KLN ocean ctx ===\"; grep -n -o \"ocean,  n[^|]\\{0,320\\}\" KLN_1966.txt | head -3\necho \"=== LAT Oceanus ===\"; grep -n -i \"oceanus\" LAT.txt LEW_1910.txt | head -5\necho \"=== BQT v3 قایق ===\"; grep -n \"قایق\" incoming/BQT/BQT_v3_pages.txt BQT_v2_pages.txt 2>/dev/null | head -5\necho \"=== ARY کژ ===\"; grep -n \"ابریشم\" incoming/ARY/ARY_pages.txt | head -5",
 "description": "Klein ocean, Latin, BQT/ARY greps"
}
```


### [2026-09-06T16:05:25.526Z] TOOL RESULT

```
=== KLN ocean ===
26000:Derivative:  occurrent,  n.,  somethingthat  occurs, ocean,  n.  —  F.  ocean,  fr.  L.  deeanus,  fr.  Gk.  <I>xe- av6?,  ‘the  great  river  encompassing  the  whole
=== KLN ocean ctx ===
26000:ocean,  n.  —  F.  ocean,  fr.  L.  deeanus,  fr.  Gk.  <I>xe- av6?,  ‘the  great  river  encompassing  the  whole
=== LAT Oceanus ===
LAT.txt:24188:fretSlis: fretalis Oceanus (Aan.).
=== BQT v3 قایق ===
incoming/BQT/BQT_v3_pages.txt:4803:شقایق (اعمان)در حاشیه ‎ .‏ ۴ -مقوردیون ‎Cee)‏
incoming/BQT/BQT_v3_pages.txt:4812:‏کلهای ‎OT‏ برنگه سرخ تیره ولکه‌های سیاء است « کل کلاب ۲۷۱۱ - ثقایق ‎(giles) gles‏
incoming/BQT/BQT_v3_pages.txt:4816:آرد:« الثقر والشقایق النسمان ‎WY.‏ اینکه لاله ‎polish‏ را نعمان با تعمانی یا
incoming/BQT/BQT_v3_pages.txt:4821:‏در نام شقایق عمان بخون جوان بیار زیبای ‎(Adonis) Adoni‏ در داستان فینیقی خرس
incoming/BQT/BQT_v3_pages.txt:34458:مثل قایق برروی‌آب رانند ) « ژابا ص۳۰ * . دزفولی 18181 ( بهمین معنی ).
=== ARY کژ ===
```


## [2026-09-06T16:05:31.998Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26000p' KLN_1966.txt | head -c 1200\necho; echo \"=== page markers near 26000 ===\"; awk 'NR>=25980 && NR<=26010 {if ($0 ~ /^[0-9]+ *[0-9]* *$/) print NR\": \"$0}' KLN_1966.txt",
 "description": "Klein ocean full entry"
}
```


### [2026-09-06T16:05:33.639Z] TOOL RESULT

```
Derivative:  occurrent,  n.,  somethingthat  occurs, ocean,  n.  —  F.  ocean,  fr.  L.  deeanus,  fr.  Gk.  <I>xe- av6?,  ‘the  great  river  encompassing  the  whole

=== page markers near 26000 ===
```


## [2026-09-06T16:05:37.317Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26001,26003p' KLN_1966.txt | head -c 1200\necho; echo \"---markers---\"; awk 'NR>=25960 && NR<=26020 {if ($0 ~ /^[0-9]{3}( +[0-9]{3})? *$/) print NR\": [\"$0\"]\"}' KLN_1966.txt",
 "description": "Klein ocean continuation"
}
```


### [2026-09-06T16:05:39.283Z] TOOL RESULT

```
Exit code 100
Oceania
earth’ ;  hence  'the  great  Outward  Sea’  (opposed to  the  Inward  or  Mediterranean),  which  is  of uncertain  etymology.  Derivative:  ocean-ic,  adj.
Oceania,  n.,  collective  name  for  the  Central  and Western  Pacific  and  its  islands.  —  See  prec, word  and  1st  -ia.  Derivative:  Oceani-an,  adj.

---markers---
REcompile() - panic:  values still on machine stack for ^[0-9]{3}( +[0-9]{3})? *$
```


## [2026-09-06T16:05:46.160Z] TOOL CALL #76: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg246.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/246.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/246.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-06T16:05:46.262Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 79253 Sep  6 12:05 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/246.png
```


## [2026-09-06T16:05:48.363Z] AGENT

Now writing the verification file.


## [2026-09-06T16:15:19.472Z] TOOL CALL #77: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-246.json",
 "content": "{\n \"pdf_page\": 246,\n \"book_page\": 216,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Kayik\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Turkish kayık 'boat, skiff' (Ottoman Turkish قایق kayık), from Proto-Turkic *kiayguk 'boat, oar', from a stem *kay- 'to slide, glide'\",\n   \"note\": \"Root, language label and gloss are all right. Klein p.220 s.v. caique: 'F., fr. It. caicco, fr. Turk. kayik'; Lokotsch no. 1014 (printed p.81) 'Tk. kajyk: Boot; langer, sehr spitz zulaufender und von leichtem Holze gebauter pfeilschneller Kahn'; Hobson-Jobson p.143 'CAIQUE, s. The small skiff used at Constantinople, Turkish kāīk'. The only cosmetic point is that Nourai writes the headword 'Kayik' with an ordinary i, whereas modern Turkish orthography has the dotless kayık; that is a transliteration convention, not an error. Nourai does not go behind Turkish, but Wiktionary derives the Ottoman word from Proto-Turkic *kiayguk, so the box is the correct starting point for the European and Persian words hanging from it. Every arrow on this chart is standard and independently attested; the one blemish is the English form printed as 'caiique' (node 4), a typographic slip of the book.\",\n   \"note_fa\": \"جعبهٔ ریشه درست است: «قایق» واژه‌ای ترکی است، صورت عثمانی آن قایق kayık و بنابر ویکی‌واژه از ترکی آغازین *kiayguk «قایق، پارو» از ستاک *kay- «لغزیدن» می‌آید. کلاین (ص ۲۲۰) ذیل caique می‌نویسد که این واژه از فرانسه، آن هم از ایتالیایی caicco و آن از ترکی kayik است؛ لوکوچ (شمارهٔ ۱۰۱۴، ص ۸۱) و هابسن‑جابسن (ص ۱۴۳) نیز همین را می‌گویند. برچسب زبان («ترکی») و معنای «قایق» هر دو درست است و تنها نکته این است که نورایی نشان بی‌نقطهٔ ı ترکی را ننوشته است. ادعای نورایی در این جعبه درست است؛ تنها لغزش این صفحه، صورت چاپی «caiique» در گرهٔ ۴ است که غلط چاپی کتاب است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%DB%8C%D9%82\",\n    \"https://en.wiktionary.org/wiki/caique\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KLN:220\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6107, on the leaf whose printed page numbers are 220/221: 'caique, n., a light rowing or sailing boat, used esp. on the Bosporus. — F., fr. It. caicco, fr. Turk. kayik.' Exactly the root box and the whole chain of nodes 2-4.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"LKT\", \"where\": \"no. 1014, printed p. 81 (LKT.txt line 2419; page markers '81' at line 2400, '82' at line 2427)\", \"stance\": \"supports\", \"note\": \"'1014. Tk. kajyk: Boot; langer, sehr spitz zulaufender und von leichtem Holze gebauter pfeilschneller Kahn; hieraus … rum. caic Barke …, it. caicco kleine Barke als Rettungsboot, Schaluppe, siz. caiccu …, frz. caïq, caïque, caïc, ndl. kaick, engl. caïque Schaluppe, Boot auf dem Bosporus und dem Schwarzen Meere.'\"},\n    {\"src\": \"HJB\", \"where\": \"s.v. CAIQUE, p. 143 (HJB.txt line 4773)\", \"stance\": \"supports\", \"note\": \"'CAIQUE, s. The small skiff used at Constantinople, Turkish kāīk. Is it by accident, or by a radical connection through Turkish tribes on the Arctic shores of Siberia, that the Greenlander's kayak is so closely identical?'\"},\n    {\"src\": \"TTS\", \"where\": \"no. 175, printed p. 161 (TTS_pages.txt leaf 191)\", \"stance\": \"silent\", \"note\": \"Vámbéry has no separate article kajyk; his no. 175 'talii, taj, toj … glatt, eben, gleiten, ausgleiten' is the glide-stem that Lokotsch invokes for kajmak 'gleiten' (Lokotsch no. 1008 cites 'Vámbery TktEtWb S. 161, Nr. 175'), which is the stem Wiktionary continues as Proto-Turkic *kay- 'to slide'. Grep of TTS_pages.txt for kajik/kajyk/kaik returned only an unrelated line.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. قایق (Ottoman Turkish) and s.v. caique\", \"stance\": \"supports\", \"note\": \"'Inherited from Proto-Turkic *kiayguk (\\\"boat; oar\\\")'; the Descendants list gives '→ Italian: caicco → French: caïque, caïc, caie → English: caique', and the Persian section makes Persian قایق 'Borrowed from Turkic'.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Persian\",\n     \"words\": \"qâyeq «قایق» : boat\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian قایق qāyeq is a loan from Ottoman/Azerbaijani Turkish قایق kayık, taken over in the Safavid–Qajar period along with the rest of the Caspian and Ottoman nautical vocabulary; the Turkish dotless ı is rendered in Persian by the yā of قایق and pronounced -e- in the Tehran standard (qāyeq). Mo'in marks the word [ تر. ] i.e. Turkish, and glosses it 'کشتی، زورق' — a boat, a skiff — which is Nourai's gloss. Persian did not pass the word on to any of the European forms: they came independently through Italian (node 2), so Nourai is right to hang Persian and Italian as two separate branches from the Turkish root rather than in a chain.\",\n     \"derivation_fa\": \"«قایق» وام‌واژه‌ای است از ترکی عثمانی/آذربایجانی قایق kayık که در دورهٔ صفوی و قاجار همراه دیگر واژه‌های دریانوردی به فارسی راه یافته است؛ ı بی‌نقطهٔ ترکی در فارسی با «ی» نوشته و در تلفظ معیار تهرانی -ِ- خوانده می‌شود، از این‌رو qāyeq. معین این واژه را با نشان [ تر. ] یعنی ترکی آورده و «کشتی، زورق» معنی کرده است که همان معنای نورایی است. فارسی این واژه را به زبان‌های اروپایی نداده است؛ آن‌ها مستقلاً از راه ایتالیایی گرفته‌اند، پس درست است که نورایی شاخهٔ فارسی و شاخهٔ ایتالیایی را جدا از هم از ریشهٔ ترکی رسم کرده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%D9%82%D8%A7%DB%8C%D9%82\",\n      \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%DB%8C%D9%82\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:2629\", \"status\": \"supports\", \"note\": \"Mo'in's entry, read at vajehyab.com/moein/قایق: 'قایق (یِ) [ تر. ] (اِ.) کشتی ، زورق .' — Turkish origin tag and Nourai's gloss 'boat'. The print page number 2629 cannot be checked online (vajehyab carries no pagination), but the entry is Mo'in's and says what Nourai's arrow says.\"},\n      {\"ref\": \"ARK:214\", \"status\": \"not_checked\", \"note\": \"ARK = Rokn-zadeh Adamiyyat, Arkan-e Sokhan (Sharq 1347/1968); refs_online.json records that no copy is digitised on any accessible platform, so p.214 could not be seen.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. قایق (vajehyab, فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"'قایق (یِ) [ تر. ] (اِ.) کشتی ، زورق .'\"},\n      {\"src\": \"BQT\", \"where\": \"grep of BQT_v2_pages.txt and incoming/BQT/BQT_v3_pages.txt for قایق\", \"stance\": \"silent\", \"note\": \"Borhan-e Qate' (1062/1652) has no article قایق — only شقایق and, at v3 line 34458, a simile 'مثل قایق برروی آب رانند' inside another entry. Consistent with the word being a late Turkish loan that entered Persian after Borhan was compiled.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. قایق, Persian section\", \"stance\": \"supports\", \"note\": \"'Borrowed from Turkic. Compare Azerbaijani qayıq, Kazakh қайық (qayıq), Turkish kayık, Turkmen gaýyk.'\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Italian\",\n     \"words\": \"caicco\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Italian caicco 'small ship's boat, launch' is a 16th-century borrowing of Ottoman Turkish kayık, taken over by Venetian and Genoese seamen in the Levant trade; Turkish -yık was rendered by the Italian geminate -cc- (kayık > ca-icco), giving the stress pattern caìcco. Klein p.220 makes it the direct source of French caïque, and Lokotsch p.81 lists it in the same series as Sicilian caiccu, Romanian caic, Bulgarian/Serbian kaik and Russian kaik — i.e. the whole Mediterranean and Balkan spread of the Turkish word, of which Italian is the westward link.\",\n     \"derivation_fa\": \"ایتالیایی caicco «زورق کوچک کشتی» وام‌گیری سدهٔ شانزدهم از ترکی عثمانی kayık است که ملوانان ونیزی و جنووایی در بازرگانی شام (لِوانت) آن را گرفتند؛ ‑yık ترکی در ایتالیایی به ‑cc‑ مشدد بدل شده و تکیه بر هجای دوم افتاده است (caìcco). کلاین (ص ۲۲۰) همین صورت را سرچشمهٔ caïque فرانسوی می‌داند و لوکوچ (ص ۸۱) آن را در کنار caiccu سیسیلی، caic رومانیایی، kaik بلغاری و صربی و روسی می‌آورد؛ یعنی ایتالیایی حلقهٔ غربی گسترش این واژهٔ ترکی است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/caique\",\n      \"https://en.wiktionary.org/wiki/%D9%82%D8%A7%DB%8C%D9%82\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:220\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6107 (printed pp. 220/221): 'caique … — F., fr. It. caicco, fr. Turk. kayik.' Klein's chain It. caicco < Turk. kayik is Nourai's arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1014, p. 81\", \"stance\": \"supports\", \"note\": \"'… it. caicco kleine Barke als Rettungsboot, Schaluppe, siz. caiccu …'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. قایق, Descendants\", \"stance\": \"supports\", \"note\": \"'→ Italian: caicco → English: caicco / → French: caïque, caïc, caie → English: caique'.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"French\",\n     \"words\": \"\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"An empty pass-through box: the French word intended is caïque (also spelled caïc), attested from the late 16th century for the light Bosporus rowing boat and borrowed from Italian caicco, with the Italian geminate simplified and a diaeresis written to keep the hiatus ca-ï. Pihan pp. 85-86 heads the article 'CAÏC ou CAÏQUE, s. m. (t.)' — the (t.) marking it Turkish — describes the Constantinople caïque and its rating by pairs of oars, and closes 'Comparez avec le mot turc l'italien caicco et le portugais caïque', i.e. the same Turkish > Italian > French line Nourai draws.\",\n     \"derivation_fa\": \"این جعبه تهی است و واژهٔ فرانسوی مقصود caïque (به‌گونهٔ caïc نیز) است: قایق سبک پاروییِ بُسفُر، از اواخر سدهٔ شانزدهم در فرانسه گواهی شده و وام‌گرفته از caicco ایتالیایی، با ساده‌شدن مصوّت مشدد و نشانهٔ دو‑نقطه (tréma) برای نگه‌داشتن دو هجای ca‑ï. پیهان در صص ۸۵ـ۸۶ مدخل «CAÏC ou CAÏQUE, s. m. (t.)» را با نشان (t.) یعنی ترکی آورده، قایق‌های استانبول و رده‌بندی آن‌ها را بر پایهٔ شمار جفت‌پاروها شرح داده و در پایان می‌نویسد: «واژهٔ ترکی را با caicco ایتالیایی و caïque پرتغالی بسنجید» — یعنی همان زنجیرهٔ ترکی ← ایتالیایی ← فرانسوی که نورایی رسم کرده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/caique\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"PHN:85\", \"status\": \"supports\", \"note\": \"PHN.txt line 2890 opens 'CAÏC ou CAÏQUE, s. m. (t.)' and the running head '86 CAI' falls inside the article, so it stands on pp. 85-86 exactly as cited. Text: 'Esquif d'une forme gracieuse et légère, en usage sur la Méditerranée et la mer Noire … Comparez avec le mot turc l'italien caicco et le portugais caïque.'\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1014, p. 81\", \"stance\": \"supports\", \"note\": \"'… frz. caïq, caïque, caïc, ndl. kaick, engl. caïque …' — French listed as the intermediary between Italian and English.\"},\n      {\"src\": \"DEV\", \"where\": \"grep of DEV.txt for CAIQUE/GAZE/CASAQUE\", \"stance\": \"silent\", \"note\": \"Devic's Dictionnaire des mots français d'origine orientale has no article caïque (only Gazelle at p.1389 of the OCR); he restricts himself to Arabic/Persian words and leaves the Turkish ones to Pihan.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. caique, Etymology 1\", \"stance\": \"supports\", \"note\": \"'Borrowed from French caïque, from Italian caicco, from Ottoman Turkish قایق (kayık), from Proto-Turkic *kiayguk (\\\"boat, oar\\\").'\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"caiique : a row or sail boat\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The derivation itself is correct and uncontroversial — English caique (also caïque), 'a light rowing or sailing boat used especially on the Bosporus', from French caïque, from Italian caicco, from Ottoman Turkish kayık — but the form printed in the book, 'caiique' with two i's, is not an English word and appears in no dictionary. It is the book's own typesetting accident: the diaeresis of French caïque was set as a second i (ca-ï-que > caiique). Wiktionary's alternative-form list for caique (caïc, caicco, caieque, caïque, kaik, kaiki, kajik, kayik, saique) does not contain it. I rendered PDF page 246 at 300 dpi and read the English box: the page really does print 'caiique : a row or sail boat', so the JSON extraction is faithful and the error is Nourai's. The page image is filed at data/verification/sources/refs/ocr/BOOK/246.png.\",\n     \"derivation_fa\": \"خودِ اشتقاق درست و بی‌مناقشه است: انگلیسی caique (یا caïque) «قایق سبک پارویی یا بادبانی، به‌ویژه در بسفر» از caïque فرانسوی، از caicco ایتالیایی، از kayık ترکی عثمانی. اما صورتی که در کتاب چاپ شده، «caiique» با دو i، واژهٔ انگلیسی نیست و در هیچ فرهنگی نیامده است؛ فهرست صورت‌های دیگرِ ویکی‌واژه (caïc, caicco, caieque, caïque, kaik, kaiki, kajik, kayik, saique) نیز آن را ندارد. این لغزش از خودِ کتاب است: دو‑نقطهٔ (tréma) واژهٔ فرانسوی در حروف‌چینی به i دوم بدل شده است. صفحهٔ ۲۴۶ را با تفکیک ۳۰۰ نقطه بر اینچ درآوردم و خواندم؛ روی کاغذ هم «caiique» چاپ شده است، پس خطای خوانش اسکن نیست، خطای چاپی کتاب است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"caiique\",\n     \"correct_form\": \"caique (French caïque)\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/caique\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:220\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6107 (pp. 220/221): 'caique, n., a light rowing or sailing boat, used esp. on the Bosporus. — F., fr. It. caicco, fr. Turk. kayik.' Klein spells it caique, not caiique.\"},\n      {\"ref\": \"LKT:81\", \"status\": \"supports\", \"note\": \"LKT.txt line 2419, no. 1014, printed p. 81 (markers 81 at line 2400, 82 at line 2427): '… engl. caïque Schaluppe, Boot auf dem Bosporus und dem Schwarzen Meere.'\"},\n      {\"ref\": \"AHD:187\", \"status\": \"not_checked\", \"note\": \"AHD:187 is a page of the main text of the 1975 American Heritage New College Edition; only Watkins' Indo-European appendix is on disk (AHD_watkins1985.txt), and the New College scans on archive.org are lending-only.\"},\n      {\"ref\": \"FWE:45\", \"status\": \"not_checked\", \"note\": \"FWE = A. J. Bliss, Dictionary of Foreign Words and Phrases in Current English (1966); refs_online.json records it as borrowable-only on archive.org.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 220 s.v. caique\", \"stance\": \"supports\", \"note\": \"'caique, n., a light rowing or sailing boat, used esp. on the Bosporus. — F., fr. It. caicco, fr. Turk. kayik.'\"},\n      {\"src\": \"HJB\", \"where\": \"p. 143 s.v. CAIQUE\", \"stance\": \"supports\", \"note\": \"'CAIQUE, s. The small skiff used at Constantinople, Turkish kāīk.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. caique, Etymology 1 and Alternative forms\", \"stance\": \"partial\", \"note\": \"Confirms the chain F. caïque < It. caicco < Ott. Turk. قایق, and lists the attested spellings 'caïc, caicco, caieque, caïque, kaik, kaiki, kajik, kayik, saique' — 'caiique' is not among them.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Kaž, Kaz\",\n   \"verdict\": \"plausible\",\n   \"modern_form\": \"New Persian کژ / کز kaž, kaz 'floss silk, cheap raw silk' (by-forms کج kaj, غژ ġaž), from Middle Persian kač; not attested in Old Persian\",\n   \"note\": \"The word and the gloss are right, the language label is not. کژ/کز is a Middle- and New-Persian word: Mo'in's own footnote 6 to Borhan-e Qate' p.1637 reads 'کج = غژ (در: غژغاو) = قز (معرب)، پهلوی kac «تاوادیا ۱۶۲»، قس: کردی kozé (پیلهٔ ابریشم) «ژابا ۳۴۹»', and Asbaghi p.218 gives 'pers. kaž, mp. kač'. There is no Achaemenid attestation — Kent's Old Persian lexicon has nothing of the kind — and silk only became an Iranian commodity in the Parthian–Sasanian period, so 'Old Persian' here must be read as Nourai's loose label for 'Old Iranian', and even that is doubtful: Wiktionary treats Persian کژ as merely 'akin to' Aramaic קָזָא qāzzā, Old Armenian կաճ kač 'felt', Old Georgian ყაჭი q̇ač̣i, Arabic خَزّ ḵazz and قَزّ qazz, i.e. a Wanderwort of the silk trade whose ultimate direction of travel is not settled. Everything hanging below the box in Persian, Arabic and Pahlavi is well attested; the two weak arrows are the French ones (nodes 3 and 7), where the modern handbooks prefer other origins. Verdict for the box: plausible — real word, right meaning, wrong (or at best over-precise) language label.\",\n   \"note_fa\": \"واژه و معنا درست است، برچسب زبان نه. «کژ/کز» واژه‌ای فارسی میانه و فارسی نو است: خودِ معین در پانوشت ۶ برهان قاطع (ص ۱۶۳۷) می‌نویسد «کج = غژ (در: غژغاو) = قز (معرب)، پهلوی kac «تاوادیا ۱۶۲»، قس: کردی kozé (پیلهٔ ابریشم) «ژابا ۳۴۹»»، و اصباغی (ص ۲۱۸) نیز «pers. kaž، mp. kač» می‌آورد. هیچ گواهی هخامنشی برای این واژه نیست — در واژه‌نامهٔ پارسی باستانِ کِنت چنین مدخلی وجود ندارد — و ابریشم تنها از دورهٔ اشکانی و ساسانی کالای ایرانی شد؛ پس «پارسی باستان» را باید برچسب سهل‌انگارانهٔ نورایی برای «ایرانی باستان» دانست، و همان هم تردیدآمیز است: ویکی‌واژه «کژ» را تنها «هم‌ریشه» با آرامی qāzzā، ارمنی کهن kač «نمد»، گرجی کهن q̇ač̣i و عربی خَزّ و قَزّ می‌شمارد، یعنی واژه‌ای سرگردان (Wanderwort) از راه بازرگانی ابریشم که سمت‌وسوی وام‌گیری‌اش قطعی نیست. شاخه‌های فارسی، عربی و پهلویِ زیرِ این جعبه همه استوارند؛ دو پیوند سست، دو گرهٔ فرانسوی (۳ و ۷) است که پژوهش امروزی برای آن‌ها خاستگاه دیگری می‌پسندد. حکم دربارهٔ جعبهٔ ریشه: با احتیاط پذیرفتنی است.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%DA%A9%DA%98\",\n    \"https://vajehyab.com/moein/%DA%A9%DA%98\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"(none cited)\", \"status\": \"not_checked\", \"note\": \"The root box carries no reference in the book (refs = None in the extraction, and the printed box on page 216 shows no book icon), so there is nothing of Nourai's own to check at root level; the references on node 1 (BQT:1637; PLA:218) are the ones that actually underwrite the etymon and both were checked and both support it.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"printed p. 1637 (BQT vol. 3 = incoming/BQT/BQT_v3_picofile.pdf page 430; rendered with tools/ref_page.py BQT:1637 --image, transcript saved as sources/refs/ocr/BQT/1637.vision.txt)\", \"stance\": \"supports\", \"note\": \"s.v. کژ: «بفتح اول و سکون ثانی، بمعنی کج است که نقیض راست باشد؛ و قسمی از ابریشم فرومایه و کم قیمت بود که بعربی قز گویند، و بعضی گفته‌اند که قز معرب کژ است». Mo'in's footnote 6: «کج = غژ (در: غژغاو) = قز (معرب)، پهلوی kac ‹تاوادیا ۱۶۲›، قس: کردی kozé (پیلهٔ ابریشم) ‹ژابا ۳۴۹›».\"},\n    {\"src\": \"PLA\", \"where\": \"printed p. 218 (PLA_pages.txt leaf 233, running heads garamfül … gaöniza)\", \"stance\": \"supports\", \"note\": \"'qazz: \\\"rohe Seide\\\" pers. kaž, mp. kač [n.3 Farawaši], dtsch. Gaze'; on the same page 'gaz(a)/Gaze: \\\"durchsichtiges, gitterartiges Gewebe\\\" pers. → ar. → sp., frz.' and 'gazkand: \\\"Panzer\\\" pers., dtsch. Kasack'. Asbaghi's page underwrites nodes 1, 5, 7 and (for the garment) node 3.\"},\n    {\"src\": \"PHD\", \"where\": \"grep of PHD.txt / PHD_mackenzie.txt for kac / kač / silk\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no headword kač; its silk words are 'abrēšom … silk' and 'stabrag [stplk' | Ar. istabraq] shot silk'. Absence from the CPD is not evidence against the word (the CPD is deliberately restricted to the published Book-Pahlavi corpus), but it means the Pahlavi form rests on Farahvashi and Tavadia, as Mo'in and Asbaghi cite them.\"},\n    {\"src\": \"MON\", \"where\": \"s.v. کژ (vajehyab, فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"'کژ (کَ) (اِ.) 1 - نادرست ، کج . 2 - ابریشم کم قیمت .' — meaning 2 is Nourai's 'inexpensive silk' word for word.\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. کژ, Etymology 2\", \"stance\": \"partial\", \"note\": \"'From Middle Persian kač. Akin to Old Armenian կաճ (kač, \\\"felt\\\"), Old Georgian ყაჭი, Proto-Nakh *q̇aač̣, Aramaic קָזָא (qāzzā), Arabic خَزّ (ḵazz), قَزّ (qazz, \\\"silk\\\") …' with alternative forms 'کز (kaz), کج (kaj), غژ (ġaž), قز (qaz)'. Supports the Middle Persian etymon and every Persian by-form Nourai prints, but declines to make Persian the source of the Semitic forms.\"},\n    {\"src\": \"KNT\", \"where\": \"Lexicon pp. 164 ff. (KNT.txt chunks 186-187)\", \"stance\": \"silent\", \"note\": \"Kent's Old Persian lexicon has no word of this shape; there is no Achaemenid attestation to justify the label 'Old Persian' on the box.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"kac, kač : an inexpensive silk\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian kač 'raw/floss silk' is the immediate ancestor of the New Persian word and is recorded by both of Nourai's references: Mo'in's footnote to Borhan-e Qate' p.1637 gives 'پهلوی kac' (citing Tavadia), and Asbaghi p.218 writes 'pers. kaž, mp. kač' (citing Farahvashi). It is the word for the coarse, unreeled silk left over after the fine thread has been drawn off the cocoon — precisely 'inexpensive silk'. The Pahlavi final affricate -č is continued in New Persian both unchanged (کج kaj) and voiced (کژ kaž), with a further de-affricated by-form کز kaz and a dialectal غژ ġaž; Borhan-e Qate' registers all of them on the same page. Wiktionary's Persian article s.v. کژ likewise begins 'From Middle Persian kač'.\",\n     \"derivation_fa\": \"فارسی میانه (پهلوی) kač «ابریشم خام و فرومایه» نیای بی‌واسطهٔ واژهٔ فارسی نو است و هر دو مأخذی که نورایی آورده آن را ثبت کرده‌اند: معین در حاشیهٔ برهان قاطع (ص ۱۶۳۷) «پهلوی kac» می‌نویسد (به نقل از تاوادیا) و اصباغی (ص ۲۱۸) «pers. kaž، mp. kač» می‌آورد (به نقل از فرهوشی). این واژه نام همان ابریشم درشت و نانخ‌کشیده‌ای است که پس از کشیدن نخ نازک از پیله بر جای می‌ماند، یعنی درست همان «ابریشم کم‌قیمت». وَرزِ پایانیِ ‑č پهلوی در فارسی نو هم بی‌تغییر مانده (کج kaj)، هم واک‌دار شده (کژ kaž)، و گونهٔ ساده‌شدهٔ کز kaz و گویشیِ غژ ġaž نیز در همان صفحهٔ برهان آمده است. ویکی‌واژه هم مدخل «کژ» را با «از فارسی میانهٔ kač» آغاز می‌کند. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%A9%DA%98\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1637\", \"status\": \"supports\", \"note\": \"Rendered with tools/ref_page.py BQT:1637 --image (vol. 3 pdf page 430) and read from the image; footnote 6 to کژ: «کج = غژ (در: غژغاو) = قز (معرب)، پهلوی kac ‹تاوادیا ۱۶۲›، قس: کردی kozé (پیلهٔ ابریشم) ‹ژابا ۳۴۹›، رک: کج.» Transcript filed at sources/refs/ocr/BQT/1637.vision.txt.\"},\n      {\"ref\": \"PLA:218\", \"status\": \"supports\", \"note\": \"PLA_pages.txt leaf 233 = printed p. 218: 'qazz: \\\"rohe Seide\\\" pers. kaž, mp. kač, dtsch. Gaze', footnote 3 'Farawaši'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, grep kac / kač / silk\", \"stance\": \"silent\", \"note\": \"No headword kač; MacKenzie's silk words are abrēšom and stabrag 'shot silk'. The form is not in the CPD's corpus, so it rests on Tavadia and Farahvashi as cited by Mo'in and Asbaghi.\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep kač / kac / silk\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary has kač- only in the Avestan verb kaēš-/kač- 'to teach' (s.vv. cihēnītan, nām-čišt) and kad/kača 'when' — nothing for the silk word.\"},\n      {\"src\": \"BQT\", \"where\": \"p. 1637 footnote 6\", \"stance\": \"supports\", \"note\": \"'پهلوی kac' — Mo'in's own Pahlavi form, exactly Nourai's node.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 218 s.v. qazz\", \"stance\": \"supports\", \"note\": \"'pers. kaž, mp. kač'.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"kaz «کز» : inexpensive silk ; kazâkand «کزاکند» : silk-filled (☞Gwhen 1)\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"New Persian کژ/کز kaž, kaz continues Middle Persian kač with the regular voicing/de-affrication of the final affricate; Borhan-e Qate' p.1637 defines it 'قسمی از ابریشم فرومایه و کم قیمت بود که بعربی قز گویند' — a kind of low-grade, cheap silk called qaz in Arabic — and Mo'in's own dictionary keeps the two senses side by side: 'کژ (کَ) (اِ.) ۱- نادرست، کج. ۲- ابریشم کم قیمت'. The compound کژاکند / کزاکند kaž-āgand is kaž 'floss silk' + āgand, the past stem of آگندن āgandan 'to stuff, pad' (Middle Persian āgandan, from Old Iranian *ā-gand-, PIE *gʷhen-), so literally 'silk-stuffed' — the quilted war-jacket padded with waste silk; Nourai's cross-reference '☞ Gwhen 1' for the second element is therefore correct. The printed page shows the by-forms in brackets, کژ، غِژ، غِژغاو beside کَز, and کژاکند beside کزاکند, and Borhan lists کژانه 'silk cocoon' on the same page — the extraction reproduces all of this faithfully.\",\n     \"derivation_fa\": \"فارسی نو «کژ/کز» دنبالهٔ فارسی میانهٔ kač است با واک‌دارشدن و سپس ساده‌شدنِ ورزِ پایانی. برهان قاطع (ص ۱۶۳۷) آن را «قسمی از ابریشم فرومایه و کم قیمت بود که بعربی قز گویند» تعریف می‌کند و خودِ فرهنگ معین هر دو معنا را کنار هم آورده است: «کژ (کَ) (اِ.) ۱- نادرست، کج. ۲- ابریشم کم قیمت». واژهٔ مرکب «کژاکند/کزاکند» از «کژ» (ابریشم فرومایه) و «آگند»، ستاک گذشتهٔ «آگندن» (فارسی میانه āgandan، از ایرانی باستان *ā-gand-، هندواروپایی *gʷhen-) ساخته شده، یعنی «آگنده به ابریشم»: همان جوشن یا نیم‌تنهٔ لایی‌دار جنگی که با پس‌ماندهٔ ابریشم پُر می‌کردند؛ پس ارجاع نورایی به ریشهٔ «Gwhen 1» برای جزء دوم درست است. در صفحهٔ چاپی گونه‌های «کژ، غِژ، غِژغاو» در کمانک کنار «کَز» و «کژاکند» کنار «کزاکند» آمده و برهان در همان صفحه «کژانه» (پیلهٔ ابریشم) را نیز دارد؛ استخراج JSON همهٔ این‌ها را درست ثبت کرده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%DA%A9%DA%98\",\n      \"https://en.wiktionary.org/wiki/%DA%A9%DA%98\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:2963\", \"status\": \"supports\", \"note\": \"Mo'in's entry read at vajehyab.com/moein/کژ: 'کژ (کَ) (اِ.) 1 - نادرست ، کج . 2 - ابریشم کم قیمت .' Sense 2 is Nourai's gloss. The printed page number 2963 cannot be verified — vajehyab reproduces Mo'in's text without pagination and no page-mapped scan of the six-volume Amir Kabir edition is on disk.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"printed p. 1637, s.v. کژ and کژاته/کژانه\", \"stance\": \"supports\", \"note\": \"«… و قسمی از ابریشم فرومایه و کم قیمت بود که بعربی قز گویند، و بعضی گفته‌اند که قز معرب کژ است»; footnote 8: «در رشیدی آمده: کژانه، پیلهٔ ابریشم، و این مرکبست از «کژ» که ابریشم است و «انه» که برای نسبت است».\"},\n      {\"src\": \"MON\", \"where\": \"s.v. کژ (vajehyab)\", \"stance\": \"supports\", \"note\": \"'2 - ابریشم کم قیمت'.\"},\n      {\"src\": \"HRN\", \"where\": \"grep of HRN.txt for kaz / Rohseide / Flockseide\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss has no numbered article for kaž/kaz; he does not treat the silk vocabulary.\"},\n      {\"src\": \"HUB\", \"where\": \"grep of HUB.txt for Seide\", \"stance\": \"silent\", \"note\": \"Hübschmann's Persische Studien discusses only abrēšum 'Seide' (nos. 65, and pp. 4173, 4876, 6239 of the OCR) — nothing on kaž.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. کژ, Etymology 2, Alternative forms\", \"stance\": \"supports\", \"note\": \"Lists exactly Nourai's by-forms: 'کز (kaz), کج (kaj), غژ (ġaž), قز (qaz)'.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"French\",\n     \"words\": \"casaqueand, casaque : a kind of silk-filled garment\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"Two problems, one formal and one substantive. (a) Form: 'casaqueand' is not a French word and never was; I rendered PDF page 246 at 300 dpi and the box really prints 'casaqueand, casaque', so the extraction is faithful and the slip is the book's. It is a garbled fusion of casaque with the Persian ending -and, which comes straight out of Klein's article: 'cassock … — F. casaque, fr. Pers. kazagand, a kind of jacket. The ending -and of the Persian word was mistaken for a suff., and consequently dropped. Cp. F. casaquin, jacket, in which the supposed suff. -and was substituted by suff. -in.' The forms that should stand are casaque (and its diminutive casaquin). (b) Substance: the arrow Persian kaž-āgand > French casaque is a minority view. For it: Klein p.246 (as quoted) and Asbaghi p.218, who lists 'gazkand: \\\"Panzer\\\" pers., dtsch. Kasack'. Against it: the American Heritage Dictionary — the very work Nourai cites here as AHD:209 — now reads 'French casaque, long military coat, from Middle French, probably originally meaning \\\"Cossack coat\\\" and ultimately (probably via Old Russian kozakŭ, free man, Cossack) of Turkic origin; akin to Tatar qazaq'; Lokotsch no. 1143 puts it.casaque, cassock, Kasack and Italian casacca under 'Tk. kazak: Landstreicher, Vagabund, Nomade'; Wiktionary s.v. casaque has only 'Probably from Italian casacca'; and Pihan pp. 102-103 derives casaque from Arabic khasīj and cites Persian قزاکند qazākend only 'comme un simple rapprochement'. Etymonline gives both without deciding. So the word is real and the garment sense is right, but the printed form is impossible and the Persian route is contested.\",\n     \"derivation_fa\": \"دو اشکال، یکی صوری و یکی ماهوی. (الف) صورت: «casaqueand» واژهٔ فرانسوی نیست و هرگز نبوده است؛ صفحهٔ ۲۴۶ را با تفکیک ۳۰۰ نقطه بر اینچ درآوردم و در جعبه به‌روشنی «casaqueand, casaque» چاپ شده است، پس خطای خوانش اسکن نیست بلکه خطای چاپی کتاب است. این صورت آمیزه‌ای مغشوش از casaque با پایانهٔ فارسی ‑and است که مستقیماً از مقالهٔ کلاین آمده: «cassock … از فرانسهٔ casaque، از فارسی kazagand؛ پایانهٔ ‑andِ واژهٔ فارسی را پسوند پنداشتند و از این‌رو انداختند؛ قس فرانسهٔ casaquin که در آن به‌جای پسوند پنداشتهٔ ‑and پسوند ‑in نشسته است.» صورت‌های درست casaque و صورت کوچک‌شدهٔ casaquin است. (ب) ماهیت: پیکانِ «کژاکندِ فارسی ← casaqueِ فرانسوی» نظری اقلیتی است. موافق آن: کلاین (ص ۲۴۶) و اصباغی (ص ۲۱۸) با «gazkand: زره، فارسی، آلمانی Kasack». مخالف آن: خودِ فرهنگ American Heritage — همان مأخذی که نورایی این‌جا با AHD:209 به آن ارجاع می‌دهد — که امروز می‌نویسد casaque از فرانسهٔ میانه و در اصل احتمالاً «قبای قزّاق»، از راه روسی کهن kozakŭ و سرانجام از خاستگاه ترکی، هم‌ریشه با qazaqِ تاتاری؛ لوکوچ (شمارهٔ ۱۱۴۳) casaque و cassock و Kasack و casacca را زیر «ترکی kazak: ولگرد، خانه‌به‌دوش، کوچ‌نشین» می‌آورد؛ ویکی‌واژه ذیل casaque تنها «احتمالاً از ایتالیایی casacca» دارد؛ و پیهان (صص ۱۰۲ـ۱۰۳) casaque را از عربی «خَسیج» می‌گیرد و «قزاکند» فارسی را تنها «به‌عنوان یک هم‌سنجی ساده» یاد می‌کند. اتیمانلاین هر دو را بی‌داوری می‌آورد. پس واژه و معنای «جامهٔ آگنده» درست است، اما صورت چاپی ناممکن و راهِ فارسی مورد مناقشه است.\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"casaqueand, casaque : a kind of silk-filled garment\",\n     \"correct_form\": \"casaque (with the diminutive casaquin); the -and belongs to the Persian etymon kazāgand, not to the French word\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/casaque\",\n      \"https://www.ahdictionary.com/word/search.html?q=cassock\",\n      \"https://www.etymonline.com/word/cassock\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD:209\", \"status\": \"not_checked\", \"note\": \"AHD:209 is a page of the main text of the 1975 American Heritage New College Edition, which is not on disk (only Watkins' IE appendix) and is lending-only on archive.org. The current online AHD entry, however, contradicts the arrow: 'French casaque … probably originally meaning \\\"Cossack coat\\\" and ultimately (probably via Old Russian kozakŭ, free man, Cossack) of Turkic origin; akin to Tatar qazaq, free man, adventurer'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 246 s.v. cassock (KLN_1966.txt line 6685, leaf markers 246/247)\", \"stance\": \"supports\", \"note\": \"'cassock, n., a long ecclesiastical garment. — F. casaque, fr. Pers. kazagand, \\\"a kind of jacket\\\". The ending -and of the Persian word was mistaken for a suff., and consequently dropped. Cp. F. casaquin, \\\"jacket\\\", in which the supposed suff. -and was substituted by suff. -in.'\"},\n      {\"src\": \"PLA\", \"where\": \"p. 218\", \"stance\": \"supports\", \"note\": \"'gazkand: \\\"Panzer\\\" pers., dtsch. Kasack' — Asbaghi derives the European garment name from Persian kaž-kand/kaž-āgand.\"},\n      {\"src\": \"LKT\", \"where\": \"no. 1143, printed p. 92\", \"stance\": \"contradicts\", \"note\": \"'1143. Tk. kazak: Landstreicher, Vagabund, Nomade … Hieraus auch die Kleidernamen: russ. kazakin \\\"Art Halbrock\\\", … nhd. Kasack(jacke in der Damenmode), engl. cassock \\\"langer Priesterrock, Soutane\\\"; nlat. cazaca, it. casacca, frz. casaque, sp. pg. casaca \\\"lange Überjacke\\\".' Lokotsch takes the whole family from Turkish kazak, not from Persian.\"},\n      {\"src\": \"PHN\", \"where\": \"s.v. CASAQUE, pp. 102-103 (PHN.txt line 3326)\", \"stance\": \"partial\", \"note\": \"'CASAQUE, s. f. (a.) خسيج [khasîj] petite tente en poil de chameau … Il existe aussi en persan un mot qui présente beaucoup d'analogie avec casaquin … c'est قزاکند [qazâkend], qui veut dire: vêtement fourré de soie et de coton, porté surtout en temps de guerre … Je ne le cite, toutefois, que comme un simple rapprochement. — On peut comparer avec l'arabe l'italien casacca, qui a sans doute servi d'intermédiaire au français casaque.' Pihan knows Nourai's Persian word and its exact sense, but explicitly declines to make it the etymon.\"},\n      {\"src\": \"AHD-online\", \"where\": \"ahdictionary.com s.v. cassock\", \"stance\": \"contradicts\", \"note\": \"'French casaque, long military coat, from Middle French, probably originally meaning \\\"Cossack coat\\\" and ultimately (probably via Old Russian kozakŭ, free man, Cossack) and of Turkic origin; akin to Tatar qazaq, free man, adventurer, and Kazakh qazaq, Kazakh.'\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. cassock\", \"stance\": \"partial\", \"note\": \"'from French casaque \\\"long coat\\\" (16c.), corresponding to Spanish casaca, Italian casacca, probably ultimately from Turkish quzzak \\\"nomad, adventurer\\\" (the source of Cossack), from their typical riding coat. Or perhaps from Arabic kazagand, from Persian kazhagand \\\"padded coat,\\\" from kazh \\\"raw silk\\\" + agand \\\"stuffed.\\\"'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. casaque (French)\", \"stance\": \"contradicts\", \"note\": \"'Probably from Italian casacca (\\\"jacket, coat\\\").' No Persian element.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"English\",\n     \"words\": \"cassock : a long garment worn by the clergy\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The arrow drawn here — French casaque > English cassock — is not in doubt, whatever the ultimate source of the French word. English cassock is first recorded in the 1540s in the sense 'long loose gown or outer cloak', is a soldier's cloak through the 16th and 17th centuries, and only from the 1660s settles into its present ecclesiastical meaning, which is exactly Nourai's gloss; the French -que was anglicised as -ck. Klein p.246 gives 'cassock, n., a long ecclesiastical garment. — F. casaque', and Wiktionary agrees: 'From Middle French casaque (\\\"cloak\\\")'. Note that Nourai's gloss captures the modern, post-1660s sense, not the 16th-century one that the borrowing actually started from.\",\n     \"derivation_fa\": \"پیکانی که این‌جا کشیده شده — casaqueِ فرانسوی ← cassockِ انگلیسی — بی‌مناقشه است، هرچه خاستگاه نهایی واژهٔ فرانسوی باشد. cassock نخستین‌بار در دههٔ ۱۵۴۰ به معنای «ردای بلند و گشاد یا شنل رویی» در انگلیسی دیده می‌شود، در سده‌های شانزدهم و هفدهم بیشتر شنل سرباز است و تنها از دههٔ ۱۶۶۰ معنای کلیسایی امروزی را می‌گیرد که همان معنای نورایی است؛ ‑que فرانسوی در انگلیسی ‑ck نوشته شده است. کلاین (ص ۲۴۶) می‌نویسد «cassock، جامهٔ بلند کلیسایی، از فرانسهٔ casaque» و ویکی‌واژه نیز «از فرانسهٔ میانهٔ casaque (شنل)» می‌آورد. تنها نکته آنکه معنایی که نورایی داده معنای پس از ۱۶۶۰ است، نه معنای سدهٔ شانزدهمی که وام‌گیری از آن آغاز شد. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/cassock\",\n      \"https://www.etymonline.com/word/cassock\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN:246\", \"status\": \"supports\", \"note\": \"KLN_1966.txt line 6685, on the leaf whose printed page numbers are 246/247: 'cassock, n., a long ecclesiastical garment. — F. casaque, fr. Pers. kazagand …'. Klein's headword, gloss and immediate French source are Nourai's node exactly.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 246 s.v. cassock\", \"stance\": \"supports\", \"note\": \"'a long ecclesiastical garment. — F. casaque'.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. cassock\", \"stance\": \"supports\", \"note\": \"'1540s, \\\"long loose gown or outer cloak,\\\" from French casaque \\\"long coat\\\" (16c.) … Chiefly a soldier's cloak 16c.-17c.; ecclesiastical use is from 1660s.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. cassock\", \"stance\": \"supports\", \"note\": \"'From Middle French casaque (\\\"cloak\\\").'\"},\n      {\"src\": \"LKT\", \"where\": \"no. 1143, p. 92\", \"stance\": \"supports\", \"note\": \"'engl. cassock \\\"langer Priesterrock, Soutane\\\"' listed beside frz. casaque — same immediate route, different ultimate origin.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Arabic\",\n     \"words\": \"qaz : a type of cloth\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic قَزّ qazz 'raw silk, floss silk' (Nourai transliterates it qaz, without the doubled final consonant) is the Arabicised form of Persian kaž: Persian k- regularly answers Arabic q- in borrowings that entered before the Arabic script had a letter for /g/ or /ž/, and the Persian short a is kept. All three of Nourai's traditions say so: Lokotsch no. 1147 (printed p. 91) 'Ar. kazz: Rohseide, Flockseide [aus pers. kāz, gāz]'; Asbaghi p. 218 'qazz: \\\"rohe Seide\\\" pers. kaž, mp. kač'; and Mo'in's footnote to Borhan p.1637 'قز (معرب)', i.e. qaz is the mu'arrab (Arabicised) form, with the body of the Borhan article adding 'بعضی گفته‌اند که قز معرب کژ است'. The derived Arabic occupational noun qazzāz 'silk-rearer, silk-merchant' (Asbaghi p. 218, Pihan p. 176) shows the word fully naturalised. One caveat: Wiktionary treats Arabic قَزّ and خَزّ, Aramaic קָזָא qāzzā and Persian کژ as a set of merely 'akin' forms, so a route through Aramaic rather than direct Persian > Arabic borrowing cannot be excluded.\",\n     \"derivation_fa\": \"عربی «قَزّ» به معنای ابریشم خام (نورایی آن را بدون تشدید qaz آوانویسی کرده) معرّبِ «کژ» فارسی است: «ک» فارسی در وام‌واژه‌هایی که پیش از پیدایش حرف‌های ویژهٔ /گ/ و /ژ/ به عربی رفته‌اند به‌طور منظم «ق» می‌شود و فتحهٔ کوتاه فارسی می‌ماند. هر سه سنتی که نورایی به آن‌ها تکیه دارد همین را می‌گویند: لوکوچ (شمارهٔ ۱۱۴۷، ص ۹۱) «عربی kazz: ابریشم خام و پرک، از فارسی kāz، gāz»؛ اصباغی (ص ۲۱۸) «qazz: ابریشم خام، فارسی kaž، فارسی میانه kač»؛ و معین در حاشیهٔ برهان (ص ۱۶۳۷) «قز (معرب)»، و متن برهان نیز می‌افزاید «بعضی گفته‌اند که قز معرب کژ است». اسم فاعل عربیِ «قزّاز» (ابریشم‌فروش، نوغان‌دار) که اصباغی و پیهان (ص ۱۷۶) آورده‌اند نشان می‌دهد واژه در عربی کاملاً بومی شده است. یک احتیاط: ویکی‌واژه «قَزّ» و «خَزّ» عربی و «qāzzā»ی آرامی و «کژ» فارسی را تنها «هم‌ریشه» می‌شمارد، پس راهِ آرامی به‌جای وام‌گیری مستقیم فارسی ← عربی یکسره منتفی نیست. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%DA%A9%DA%98\",\n      \"https://en.wiktionary.org/wiki/%D9%82%D8%B2\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"LKT:91\", \"status\": \"supports\", \"note\": \"LKT.txt line 2696, entry '1147. Ar. kazz:' — the running head 'Tk. keče.] 92' falls three lines later, so the entry begins on printed p. 91 exactly as cited. Text: \\\"'Rohseide, Flockseide' [aus pers. kāz, gāz ZDMG L, 640]; hieraus sp. gasa 'durchsichtiges feines Leinen- od. Seidengewebe', frz. gaze, dtsch. Gaze 'dass.'\\\"\"},\n      {\"ref\": \"PLA:218\", \"status\": \"supports\", \"note\": \"PLA_pages.txt leaf 233 = printed p. 218: 'qazz: \\\"rohe Seide\\\" pers. kaž, mp. kač, dtsch. Gaze'; also 'gazzaz: \\\"Seidenzüchter\\\" nom. agent. v. gaz.'\"},\n      {\"ref\": \"NFI:40\", \"status\": \"not_checked\", \"note\": \"NFI = F. Jonaydi, Nameh-ye Farhang-e Iran (the translation of Rempis, 'Persische Wörter im Deutschen'); refs_online.json records nothing digitised on any accessible platform.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1147, p. 91\", \"stance\": \"supports\", \"note\": \"'Ar. kazz … [aus pers. kāz, gāz ZDMG L, 640]'.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 218 s.v. qazz\", \"stance\": \"supports\", \"note\": \"'pers. kaž, mp. kač'.\"},\n      {\"src\": \"BQT\", \"where\": \"p. 1637, article کژ and footnote 6\", \"stance\": \"supports\", \"note\": \"«… که بعربی قز گویند، و بعضی گفته‌اند که قز معرب کز است»; footnote 6 'قز (معرب)'.\"},\n      {\"src\": \"AFM\", \"where\": \"grep of AFM.txt for قز / القز\", \"stance\": \"partial\", \"note\": \"Addi Shir has no separate article قز, but uses the word as a known Arabic term inside other entries (e.g. line 651 'شرنقة القز', line 2316 'من القز'), i.e. he treats it as naturalised Arabic without discussing its origin.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. کژ, Etymology 2\", \"stance\": \"partial\", \"note\": \"Groups Arabic قَزّ (qazz) and خَزّ (ḵazz) with Aramaic קָזָא (qāzzā) and Persian کژ as 'akin' forms rather than asserting the direction Persian > Arabic.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Persian\",\n     \"words\": \"qaz «قز» : a kind of cloth\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"A textbook Persian > Arabic > Persian round trip. The native word کژ kaž went into Arabic as قَزّ qazz (node 5) and came back into literary Persian in its Arabic dress as قز qaz, which Mo'in registers with the tag [ معر. ] — mu'arrab, 'Arabicised' — and the gloss ابریشم 'silk': 'قز (قَ زّ) [ معر. ] (اِ.) ابریشم .' The re-borrowed form then generated the Arabic-looking compound قزاغند qazāġand printed in the extra script field, which is simply کژاکند kažāgand rewritten with the returned q- and with the Arabic-Persian ġ for the k of -kand. Persian thus has the same object under a native and a borrowed name side by side — a classic doublet.\",\n     \"derivation_fa\": \"نمونه‌ای کلاسیک از رفت‌وبرگشت فارسی ← عربی ← فارسی. واژهٔ بومی «کژ» به عربی رفت و «قَزّ» شد (گرهٔ ۵) و همان صورت معرّب دوباره به فارسی ادبی بازگشت و «قز» شد؛ معین آن را با نشان [ معر. ] و معنای «ابریشم» ثبت کرده است: «قز (قَ زّ) [ معر. ] (اِ.) ابریشم». صورت بازگشته سپس ترکیب عربی‌نمای «قزاغند» را زایید که در بخش «script extra» چاپ شده و چیزی نیست جز همان «کژاکند» با قافِ بازگشته و «غ» به‌جای «ک». بدین‌سان فارسی یک چیز را هم‌زمان با نام بومی و نام وام‌گرفته دارد؛ یعنی یک دوگانه (doublet) تمام‌عیار. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%D9%82%D8%B2\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON\", \"status\": \"supports\", \"note\": \"Nourai cites MON without a page here. Mo'in's entry, read at vajehyab.com/moein/قز: 'قز (قَ زّ) [ معر. ] (اِ.) ابریشم .' — the [معر.] tag is precisely Nourai's Arabic-to-Persian arrow.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. قز (vajehyab)\", \"stance\": \"supports\", \"note\": \"'قز (قَ زّ) [ معر. ] (اِ.) ابریشم .'\"},\n      {\"src\": \"BQT\", \"where\": \"p. 1637 footnote 6 and the body of the article کژ\", \"stance\": \"supports\", \"note\": \"'قز (معرب)' and «بعضی گفته‌اند که قز معرب کز است» — Mo'in states the Arabicisation, which is what makes the Persian قز a re-borrowing.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 218\", \"stance\": \"supports\", \"note\": \"Asbaghi's whole article is built on the Persian > Arabic direction ('qazz … pers. kaž'), which is the first leg of the round trip.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. کژ, Alternative forms\", \"stance\": \"supports\", \"note\": \"Lists قز (qaz) among the Persian forms of the word, i.e. the re-borrowed spelling is current Persian.\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"French\",\n     \"words\": \"gaze : a loosely woven cotton fabric\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"French gaze, first recorded in the 1560s for a very thin transparent tissue, has two rival etymologies, and the chart's own NOTE states them. (1) From Arabic قَزّ qazz 'raw silk' — with the Arabic q- rendered as g- through Spanish gasa, which is the same word and the likely intermediary of the westward journey. This is Pihan's view (p. 176: 'GAZE, s. f. (a.) قز [qazz] soie. De là vient probablement le mot gaze … Comparez l'espagnol gasa et l'anglais gauze'), Lokotsch's (no. 1147: 'hieraus sp. gasa …, frz. gaze, dtsch. Gaze'), Asbaghi's (p. 218: 'Gaze … pers. → ar. → sp., frz.') and Wiktionary's (s.v. gauze: 'from French gaze, from Arabic قَزّ (qazz, \\\"silk\\\")'). (2) From Gaza in Palestine, where the fabric was supposedly woven — Klein p. 644 ('gauze … — F. gaze, fr. Gaza, a town in Palestine, famous for the very fine transparent tissues fabricated there') and Webster ('said to be from Gaza, in Palestine, where it was first made'). Lokotsch settles the question against Gaza at no. 702: 'Da aber bis jetzt keine Textilindustrie in älteren Zeiten hier nachgewiesen ist, muß die Etymologie als rein willkürlich angezweifelt werden; die Ableitung aus kazz ist unbedingt vorzuziehen.' Etymonline, more cautiously, says 'there has been no evidence for either'. Nourai's arrow is therefore the better-supported of the two but not demonstrated — hence plausible rather than confirmed. His gloss 'a loosely woven cotton fabric' is also slightly off: gaze was originally a silk tissue, cotton and later surgical gauze being secondary.\",\n     \"derivation_fa\": \"«gaze» فرانسوی که نخست در دههٔ ۱۵۶۰ برای پارچه‌ای بسیار نازک و شفاف گواهی شده، دو ریشه‌شناسی رقیب دارد و خودِ یادداشت نمودار هر دو را یاد کرده است. ۱) از عربی «قَزّ» (ابریشم خام)، با تبدیل ق به g از راه اسپانیایی gasa که همان واژه و به احتمال زیاد حلقهٔ میانی سفر غربیِ آن است؛ این دیدگاه پیهان (ص ۱۷۶: «قز یعنی ابریشم؛ واژهٔ gaze احتمالاً از همین است؛ اسپانیایی gasa و انگلیسی gauze را بسنجید»)، لوکوچ (شمارهٔ ۱۱۴۷)، اصباغی (ص ۲۱۸: «فارسی ← عربی ← اسپانیایی، فرانسوی») و ویکی‌واژه است. ۲) از نام شهر غزه در فلسطین که گویا این پارچه را در آن‌جا می‌بافتند؛ این دیدگاه کلاین (ص ۶۴۴) و وبستر است. لوکوچ در شمارهٔ ۷۰۲ خود این نظر را رد می‌کند: «چون تاکنون هیچ صنعت نساجی کهنی در آن‌جا اثبات نشده، باید این ریشه‌شناسی را یکسره دلبخواهی و مشکوک دانست؛ اشتقاق از kazz بی‌تردید ترجیح دارد.» اتیمانلاین محتاط‌تر است و می‌گوید «برای هیچ‌یک شاهدی در دست نیست». پس ادعای نورایی از میان دو نظر، نظر مستندتر است اما اثبات‌شده نیست: با احتیاط پذیرفتنی است. معنایی هم که داده («پارچهٔ نازک پنبه‌ای») اندکی نادرست است؛ gaze در اصل پارچهٔ ابریشمی بود و کاربرد پنبه‌ای و پزشکی آن بعدی است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/gauze\",\n      \"https://www.etymonline.com/word/gauze\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"NFI:40\", \"status\": \"not_checked\", \"note\": \"NFI = Jonaydi's Nameh-ye Farhang-e Iran (Rempis's 'Persische Wörter im Deutschen' in translation); refs_online.json records that no copy is digitised on any accessible platform, so p. 40 could not be read. It is, however, the only reference Nourai gives for this node, so the arrow rests on sources he does not cite (Pihan, Lokotsch, Asbaghi), all of which happen to support it.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"LKT\", \"where\": \"no. 1147 (p. 91) and no. 702 (p. 56)\", \"stance\": \"supports\", \"note\": \"no. 1147: 'Ar. kazz … hieraus sp. gasa …, frz. gaze, dtsch. Gaze'; no. 702, s.v. Ar. Ġazza (the city): 'hiernach soll die Gaze, frz. gaze … benannt sein. Da aber bis jetzt keine Textilindustrie in älteren Zeiten hier nachgewiesen ist, muß die Etymologie als rein willkürlich angezweifelt werden; die Ableitung aus kazz [s. hier Nr. 1147] ist unbedingt vorzuziehen.'\"},\n      {\"src\": \"PHN\", \"where\": \"s.v. GAZE, p. 176 (PHN.txt line 5169)\", \"stance\": \"supports\", \"note\": \"'GAZE, s. f. (a.) قز [qazz] soie. De là vient probablement le mot gaze, qui désigne un tissu très clair et très léger … Comparez l'espagnol gasa et l'anglais gauze. Celui qui fabrique ou vend ce genre d'étoffe s'appelle gazier en français, et قزّاز [qazzâz] en arabe.'\"},\n      {\"src\": \"PLA\", \"where\": \"p. 218\", \"stance\": \"supports\", \"note\": \"'Gaze: \\\"durchsichtiges, gitterartiges Gewebe\\\" pers. → ar. → sp., frz.'\"},\n      {\"src\": \"KLN\", \"where\": \"p. 644 s.v. gauze (KLN_1966.txt line 15877, leaf markers 644/646)\", \"stance\": \"contradicts\", \"note\": \"'gauze, n., a very fine fabric of silk, cotton etc. — F. gaze, fr. Gaza, a town in Palestine, famous for the very fine transparent tissues fabricated there.' This is the rival etymology Nourai's own NOTE attributes to KLN.\"},\n      {\"src\": \"WEB\", \"where\": \"s.v. gauze (WEB_vol1.txt line 80625)\", \"stance\": \"contradicts\", \"note\": \"'gauze, n. [Fr. gaze, gauze, said to be from Gaza, in Palestine, where it was first made.]'\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. gauze\", \"stance\": \"partial\", \"note\": \"'1560s, from French gaze, of unknown origin. It has been conjectured to be from Arabic gazz \\\"raw silk\\\" or from Gaza, Palestinian city … but there has been no evidence for either.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. gauze\", \"stance\": \"supports\", \"note\": \"'Borrowed from French gaze, from Arabic قَزّ (qazz, \\\"silk\\\").'\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Persian\",\n     \"words\": \"gâz «گاز» : a surgical dressing\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Modern Persian گاز gāz 'surgical gauze, the light open-weave bandage cloth' is a twentieth-century loan straight from French gaze, taken over with the rest of the European medical vocabulary; French [gaz] is written گاز with the Persian letter gāf, which the Arabic script of قز could not supply. Mo'in tags it [ فر. ] — Faransavi, French — and gives exactly Nourai's gloss: 'گاز [ فر. ] (اِ.) ۱- تور نازک و لطیف که برای بستن زخم به کار می رود' (the second sense in Mo'in, the accelerator pedal, is the other French گاز, from gaz 'gas', a homonym). This closes the circle: the same Persian word that left the language as kaž re-enters it a third time, now through Arabic and French, as a hospital term.\",\n     \"derivation_fa\": \"«گاز» فارسیِ امروز به معنای تورِ نازکِ زخم‌بندی، وام‌واژه‌ای است از gaze فرانسوی که در سدهٔ بیستم همراه دیگر واژگان پزشکی اروپایی به فارسی آمده؛ تلفظ فرانسوی با «گ» نوشته شده، حرفی که خط عربیِ «قز» آن را نداشت. معین آن را با نشان [ فر. ] یعنی فرانسوی آورده و درست همان معنای نورایی را می‌دهد: «گاز [ فر. ] (اِ.) ۱- تور نازک و لطیف که برای بستن زخم به کار می رود» (معنای دوم در معین، یعنی پدال شتاب‌دهنده، از «گاز»ِ دیگرِ فرانسوی gaz «گاز» است و هم‌آواست نه هم‌ریشه). بدین‌گونه دایره بسته می‌شود: همان واژه‌ای که روزی به‌صورت «کژ» از فارسی بیرون رفت، این‌بار از راه عربی و فرانسوی برای سومین بار به فارسی بازمی‌گردد، اکنون به‌عنوان اصطلاحی بیمارستانی. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%DA%AF%D8%A7%D8%B2\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:3166\", \"status\": \"supports\", \"note\": \"Mo'in's entry read at vajehyab.com/moein/گاز: 'گاز [ فر. ] (اِ.) 1 - تور نازک و لطیف که برای بستن زخم به کار می رود. 2 - پدالی که در جلوی اتومبیل …'. The [فر.] tag and sense 1 are Nourai's arrow and gloss. Page 3166 itself cannot be checked — vajehyab carries no pagination.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. گاز (vajehyab)\", \"stance\": \"supports\", \"note\": \"'گاز [ فر. ] (اِ.) 1 - تور نازک و لطیف که برای بستن زخم به کار می رود.'\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' (1062/1652)\", \"stance\": \"silent\", \"note\": \"Borhan has no article گاز in this sense; the word is a modern European loan and could not be in a seventeenth-century dictionary — which is itself confirmation that Nourai is right to hang it from French rather than from the native کژ.\"},\n      {\"src\": \"PLA\", \"where\": \"p. 218\", \"stance\": \"supports\", \"note\": \"Asbaghi's chain 'Gaze … pers. → ar. → sp., frz.' is the outbound leg whose return into Persian this node records.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"English\",\n     \"words\": \"gauze\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English gauze is attested from the 1560s and is a straightforward borrowing of French gaze, the French -ze being respelled -ze/-se and finally -ze in the modern spelling gauze with the au digraph that English uses for the French open a; the sense travelled from 'thin transparent silk tissue' to the modern open-weave surgical and millinery cloth. Klein p. 644 gives it under gauze without a page in Nourai's citation ('gauze, n., a very fine fabric of silk, cotton etc. — F. gaze'), and Wiktionary has 'Borrowed from French gaze'. Only the ultimate origin of the French word is at issue (see node 7); the French-to-English step drawn here is not in dispute.\",\n     \"derivation_fa\": \"«gauze» انگلیسی از دههٔ ۱۵۶۰ گواهی شده و وام‌گیری ساده‌ای است از «gaze» فرانسوی؛ املای au در انگلیسی همان صورتی است که برای aی باز فرانسوی به کار می‌رود. معنا از «پارچهٔ نازک و شفاف ابریشمی» به تورِ سست‌بافتِ جراحی و کلاه‌دوزی امروزی رسیده است. کلاین (ص ۶۴۴) می‌نویسد «gauze، پارچهٔ بسیار نازک از ابریشم یا پنبه و جز آن، از فرانسهٔ gaze» و ویکی‌واژه نیز «وام‌گرفته از gaze فرانسوی». تنها خاستگاه نهاییِ واژهٔ فرانسوی محل بحث است (نگاه کنید به گرهٔ ۷)؛ خودِ گامِ فرانسوی ← انگلیسی بی‌مناقشه است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/gauze\",\n      \"https://www.etymonline.com/word/gauze\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KLN\", \"status\": \"supports\", \"note\": \"Cited by Nourai without a page. KLN_1966.txt line 15877, on the leaf whose printed markers are 644/646: 'gauze, n., a very fine fabric of silk, cotton etc. — F. gaze, fr. Gaza, a town in Palestine …'. Klein supports the French-to-English step (this node) while contradicting the Arabic origin of the French word (node 7) — which is exactly what Nourai's NOTE says of him.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"p. 644 s.v. gauze\", \"stance\": \"supports\", \"note\": \"'gauze, n., a very fine fabric of silk, cotton etc. — F. gaze'.\"},\n      {\"src\": \"WEB\", \"where\": \"s.v. gauze (WEB_vol1.txt line 80625)\", \"stance\": \"supports\", \"note\": \"'gauze, n. [Fr. gaze …] 1. a very thin, light, loosely woven material, usually of silk or cotton'.\"},\n      {\"src\": \"Etymonline\", \"where\": \"s.v. gauze\", \"stance\": \"supports\", \"note\": \"'1560s, from French gaze'.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. gauze\", \"stance\": \"supports\", \"note\": \"'Borrowed from French gaze'.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 5,\n   \"root\": \"Keanos\",\n   \"verdict\": \"disputed\",\n   \"modern_form\": \"Ancient Greek Ὠκεανός Ōkeanós, of disputed origin: Beekes reconstructs a Pre-Greek *ūkʲān-; the analysis Nourai follows is ō- + a derivative of PIE *ḱey- 'to lie' (Pokorny 1. ḱei- 539-540), i.e. *ō-ḱey-m̥no- 'lying around'\",\n   \"note\": \"There is no Greek word *keanos. What Nourai has boxed as a root is the second half of Ὠκεανός under the segmentation proposed by Benfey (1860) and taken up by Brugmann, who compared the Vedic epithet ā-śáyāna- 'lying upon (the waters)' of the dragon Vṛtra. Nourai's own reference is accurate: Kent, Old Persian, Lexicon p. 164 s.v. ā, writes 'pIE *ā if = Lt. ā \\\"from\\\" (Sturtevant, Lg. 15.145-54), or *ō if = Gk. ó- in ó-κεανός \\\"(lying round about), ocean\\\"'. But the interpretation was abandoned by the very school that produced it: Walde-Pokorny I 358 f., s.v. '1. ḱei- \\\"liegen\\\"', records 'Die Deutung von (ὠ)κεανός als \\\"der aufliegende\\\", ai. ā-śáyāna-ḥ (Benfey GGA. 1860, 222 …, Brugmann …) wird von Brückner KZ. 45,110, Brugmann-Thumb GrGr.⁴ 519 Anm. wohl mit Recht aufgegeben.' Beekes rejects it outright and reconstructs a Pre-Greek form, pointing out that a circumambient world-river is not an Indo-European conception; Klein, s.v. ocean, simply calls the Greek word 'of uncertain etymology'. Only Michael Janda has recently revived the comparison. So the box records a real but minority, largely abandoned nineteenth-century etymology: disputed. Two smaller points: 'siting' in the gloss is a misprint for 'sitting', and the sense wanted is 'lying' alone; and the alternative Nourai flags in the node NOTE (from ὠκύς 'swift', FSD and TAD) is even weaker — no modern handbook entertains it. The Arabic, Persian, Latin and English nodes hanging below are all sound.\",\n   \"note_fa\": \"واژهٔ یونانیِ *keanos وجود ندارد. آنچه نورایی به‌عنوان ریشه در جعبه نهاده، نیمهٔ دومِ Ὠκεανός بر پایهٔ تجزیه‌ای است که بنفی (۱۸۶۰) پیشنهاد کرد و بروگمان پی گرفت و در آن با صفتِ ودایی ā-śáyāna- «خفته بر (آب‌ها)»، لقبِ اژدها وْرْتْره، سنجیده شد. ارجاع خود نورایی دقیق است: کِنت در واژه‌نامهٔ پارسی باستان، ص ۱۶۴ ذیل ā می‌نویسد «هندواروپایی *ā اگر برابر ā لاتین باشد، یا *ō اگر برابر ó- یونانی در ó-κεανός «آنچه گرداگرد خفته است، اقیانوس» باشد». اما همان مکتبی که این تفسیر را پدید آورد، آن را رها کرد: والده‑پوکورنی (جلد یکم، صص ۳۵۸ به بعد، ذیل «1. ḱei- خفتن») می‌نویسد که تفسیر (ὠ)κεανός به معنای «برخفته» در قیاس با ā-śáyāna-ی سنسکریت «به‌درستی رها شده است». بیکس آن را یکسره رد می‌کند و صورتی پیشایونانی *ūkʲān- بازسازی می‌کند و یادآور می‌شود که رودِ جهان‌گردِ گرداگردِ زمین مفهومی هندواروپایی نیست؛ کلاین نیز ذیل ocean واژهٔ یونانی را «با ریشه‌شناسی نامعلوم» می‌خواند. تنها میشائیل یاندا در سال‌های اخیر این سنجش را دوباره زنده کرده است. پس این جعبه ریشه‌شناسیِ واقعی اما اقلیتی و تقریباً متروکِ سدهٔ نوزدهم را ثبت می‌کند: پژوهش امروزی آن را رد می‌کند. دو نکتهٔ کوچک‌تر: «siting» در معنا غلط چاپیِ «sitting» است و معنای درست تنها «خفتن، درازکشیدن» است؛ و بدیلی که نورایی در یادداشت گره آورده (از ὠκύς «تندرو»، به نقل از FSD و TAD) از این هم سست‌تر است و هیچ کتاب مرجع امروزی آن را نمی‌پذیرد. گره‌های عربی، فارسی، لاتین و انگلیسیِ زیر این جعبه همه درست‌اند.\",\n   \"sources\": [\n    \"https://en.wiktionary.org/wiki/%E1%BD%A8%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82\",\n    \"https://en.wiktionary.org/wiki/ocean\"\n   ],\n   \"ref_check\": [\n    {\"ref\": \"KNT:164\", \"status\": \"supports\", \"note\": \"KNT.txt line 4912, in the article ā at the head of Kent's Lexicon (which begins on printed p. 164): 'ā adv. as prefix and prep. \\\"to\\\"; Av. Skt. ā, prep. with acc. and abl., \\\"to, as far as\\\" …; pIE *ā if = Lt. ā \\\"from\\\" (Sturtevant, Lg. 15.145-54), or *ō if = Gk. ó- in ó-κεανός \\\"(lying round about), ocean\\\".' Kent does give exactly the segmentation and gloss Nourai's box asserts — the reference is accurate even though the etymology it reports is no longer accepted.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"1. ḱei- 'liegen, Lager; Heimstätte; traut, lieb', pp. 539-540 (POK_full.txt, 'Page(s): 539-540' at line 49666)\", \"stance\": \"partial\", \"note\": \"Pokorny has the root — 'Old Indic śéte, Av. saēte (= gr. κεῖται) \\\"liegt\\\" … gr. κοιμάω … κειμήλιον', Latin cūnae, Hittite kitta 'lies' — i.e. the material a form *ō-ḱey-m̥no- would be built on, but he does not list ὠκεανός among its derivatives.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I 358 f., '1. ḱei- \\\"liegen\\\"' (WLD_Bd1_1930 djvu lines 22610-22640)\", \"stance\": \"contradicts\", \"note\": \"'Die Deutung von (ὠ)κεανός als \\\"der aufliegende\\\", ai. ā-śáyāna-ḥ (Benfey GGA. 1860, 222, v. Fierlinger KZ. 27, 477, Brugmann Album Kern 29 Anm. 1, Grdr. II² 2,817, IF. 29, 241 Anm. 1) wird von Brückner KZ. 45, 110, Brugmann-Thumb GrGr.⁴ 519 Anm. wohl mit Recht aufgegeben.' Walde-Pokorny explicitly withdraws the etymology Nourai's root box asserts.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kei-¹ (AHD_watkins1985.txt lines 595-598)\", \"stance\": \"partial\", \"note\": \"'kei-¹. To lie; bed, couch; beloved, dear. I. Basic form *kei- … II. O-grade form *koi-. … 2. Suffixed form *koi-m-ā- in Greek koiman, to put to sleep: CEMETERY … [Pok. 1. kei- 539.]' Watkins has the root and its Greek reflexes but does not derive ocean from it; his entry for OCEAN is not attached to any Indo-European root.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. ocean (KLN_1966.txt line 26000-26001)\", \"stance\": \"contradicts\", \"note\": \"'ocean, n. — F. océan, fr. L. ōceanus, fr. Gk. Ὠκεανός, \\\"the great river encompassing the whole earth\\\"; hence \\\"the great Outward Sea\\\" (opposed to the Inward or Mediterranean), which is of uncertain etymology.'\"},\n    {\"src\": \"Wiktionary\", \"where\": \"s.v. Ὠκεανός\", \"stance\": \"contradicts\", \"note\": \"'Uncertain, though generally acknowledged to be a non-Indo-European substrate loan, with Beekes noting that the concept of a \\\"world-river\\\" is not native to Indo-European mythology … Beekes suggests a Pre-Greek form *ūkʲān-. Michael Janda has reminded the scientific community of an earlier comparison with the Vedic dragon Vṛtra's attribute āśáyāna- \\\"lying on [the waters]\\\" … both stemming from Proto-Indo-European *ō-ḱey-m̥[h₁]no- (\\\"lying on\\\"), related to κεῖμαι.'\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Greek\",\n     \"words\": \"o-keanos : lying around, water surrounding the earth\",\n     \"verdict\": \"disputed\",\n     \"derivation\": \"The word is real and the gloss is right — Ὠκεανός is in Homer the great fresh-water river that runs round the rim of the earth and the Titan who personifies it, and only later the outer sea — but the morphological analysis drawn here is not accepted today. Nourai's cut ō- + keanos, 'lying around', with ō- the preverb answering Sanskrit/Avestan ā and the second element from PIE *ḱey- 'to lie' (compare κεῖμαι), is the Benfey-Brugmann etymology built on the Vedic ā-śáyāna- 'lying upon (the waters)'. Kent p. 164 records it, but Walde-Pokorny I 358 f. states that Brückner and Brugmann-Thumb abandoned it 'wohl mit Recht', Beekes reconstructs a Pre-Greek *ūkʲān- and argues that a circumambient world-river is not an Indo-European idea, and Klein calls the Greek word 'of uncertain etymology'; Michael Janda alone has revived the comparison, positing *ō-ḱey-m̥[h₁]no-. The variant the node's NOTE reports from FSD:1707 and TAD:5, deriving it from ὠκύς 'swift' (as though the ocean were 'the swift one'), is a folk-etymological guess of the older Arabic and popular lexicography and is entertained by no modern handbook. Verdict: the word yes, this derivation no.\",\n     \"derivation_fa\": \"واژه واقعی و معنا درست است — Ὠκεανός نزد هومر رودِ بزرگِ شیرینی است که گرداگردِ لبهٔ زمین می‌گردد و نیز تیتانی که آن را تجسم می‌بخشد، و تنها بعدها به معنای دریای بیرونی به کار رفت — اما تجزیهٔ صرفی‌ای که این‌جا رسم شده امروز پذیرفته نیست. برشِ نورایی، یعنی ō- + keanos «گرداگرد خفته»، با ō- همان پیشوندی که برابر ā در سنسکریت و اوستایی است و جزء دوم از ریشهٔ هندواروپایی *ḱey- «خفتن» (قس κεῖμαι)، همان ریشه‌شناسی بنفی‑بروگمان است که بر پایهٔ ā-śáyāna-ی ودایی «خفته بر آب‌ها» ساخته شده. کِنت (ص ۱۶۴) آن را ثبت کرده، اما والده‑پوکورنی (ج۱، ص ۳۵۸ به بعد) می‌گوید بروکنر و بروگمان‑تومب آن را «به‌درستی» رها کردند، بیکس صورتی پیشایونانی *ūkʲān- بازمی‌سازد و استدلال می‌کند که رودِ گرداگردِ جهان مفهومی هندواروپایی نیست، و کلاین واژهٔ یونانی را «با ریشه‌شناسی نامعلوم» می‌خواند؛ تنها یاندا این سنجش را با بازسازی *ō-ḱey-m̥[h₁]no- زنده کرده است. آن گونهٔ دیگری هم که یادداشت این گره از FSD:1707 و TAD:5 نقل می‌کند، یعنی اشتقاق از ὠκύς «تندرو» (چنان‌که گویی اقیانوس «تندرو» باشد)، حدسی از گونهٔ ریشه‌شناسی عامیانه در فرهنگ‌نویسی کهن عربی و عامه است و هیچ کتاب مرجع امروزی آن را نمی‌پذیرد. حکم: واژه آری، این اشتقاق نه.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%E1%BD%A8%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"KNT:164\", \"status\": \"supports\", \"note\": \"KNT.txt line 4912 (Kent's Lexicon, which opens on printed p. 164), s.v. ā: '… pIE *ā if = Lt. ā \\\"from\\\" (Sturtevant, Lg. 15.145-54), or *ō if = Gk. ó- in ó-κεανός \\\"(lying round about), ocean\\\".' Kent supports both the segmentation ō- + κεανός and the gloss 'lying round about'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. I 358 f., '1. ḱei- liegen'\", \"stance\": \"contradicts\", \"note\": \"'Die Deutung von (ὠ)κεανός als \\\"der aufliegende\\\", ai. ā-śáyāna-ḥ … wird von Brückner KZ. 45,110, Brugmann-Thumb GrGr.⁴ 519 Anm. wohl mit Recht aufgegeben.'\"},\n      {\"src\": \"POK\", \"where\": \"1. ḱei- pp. 539-540\", \"stance\": \"silent\", \"note\": \"Pokorny's article on the root lists Greek κεῖται, κοιμάω, κειμήλιον, κώμη, but never ὠκεανός; the compound is simply absent from the root's inventory.\"},\n      {\"src\": \"KLN\", \"where\": \"s.v. ocean\", \"stance\": \"contradicts\", \"note\": \"'… fr. Gk. Ὠκεανός, \\\"the great river encompassing the whole earth\\\"; hence \\\"the great Outward Sea\\\" … which is of uncertain etymology.'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. Ὠκεανός\", \"stance\": \"contradicts\", \"note\": \"'generally acknowledged to be a non-Indo-European substrate loan … Beekes suggests a Pre-Greek form *ūkʲān-.' It records Janda's revival of the *ō-ḱey-m̥[h₁]no- analysis as a minority position, which is Nourai's.\"},\n      {\"src\": \"TAD\", \"where\": \"printed p. 5 (TAD_pages.txt leaf 9)\", \"stance\": \"partial\", \"note\": \"The Arabic entry that stands alphabetically between أوقة and أوكاريستيا reads, in the damaged OCR, 'يوناني … معناه مسرع وعربيه البحر المحيط' — 'Greek …, its meaning \\\"swift\\\", its Arabic equivalent al-baḥr al-muḥīṭ'. That is the ὠκύς 'swift' derivation Nourai's NOTE attributes to TAD:5, so the note reports its source correctly, but the derivation itself is worthless.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Arabic\",\n     \"words\": \"oqyânŭs : ocean\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic أوقيانوس ūqyānūs is a direct loan from Greek Ὠκεανός, taken into Arabic in the ninth-tenth century with the Greek geographical corpus — Ptolemy through the Syriac and Greek translators — and used by al-Khwārizmī, al-Masʿūdī and the later cosmographers for the encircling outer sea; the Greek -ος was fitted with the Arabic nominal ending -ūs and the initial ō- given the prosthetic hamza-alif of أو-. Wiktionary marks it '(archaic) ocean' and 'Borrowed from Ancient Greek Ὠκεανός. Doublet of قَامُوس (qāmūs)' — qāmūs being the same Greek word taken in by another route, later generalised to 'dictionary' after al-Fīrūzābādī's Qāmūs. Nourai's own reference, Tobia al-'Unaysi's dictionary of foreign words in Arabic, has the entry on p. 5, in the alif section, marked يوناني 'Greek'.\",\n     \"derivation_fa\": \"عربی «أوقيانوس» وام‌واژه‌ای است مستقیم از یونانی Ὠκεανός که در سده‌های سوم و چهارم هجری همراه با میراث جغرافیای یونانی — بطلمیوس از راه مترجمان سریانی و یونانی — به عربی راه یافت و خوارزمی و مسعودی و کیهان‌نگاران پسین آن را برای دریای فراگیرِ بیرونی به کار بردند؛ پایانهٔ ‑ος یونانی با پایانهٔ اسمی عربی ‑وس جایگزین شد و ō- آغازین همزهٔ الف گرفت (أو-). ویکی‌واژه آن را «(کهن) اقیانوس» می‌خواند و می‌نویسد «وام‌گرفته از یونانی باستان Ὠκεανός؛ دوگانهٔ قاموس» — و «قاموس» همان واژهٔ یونانی است که از راهی دیگر وارد شده و پس از «القاموس»ِ فیروزآبادی معنای «فرهنگ لغت» گرفته است. مأخذ خود نورایی، فرهنگ واژه‌های دخیل طوبیا العنیسی، این مدخل را در ص ۵ و در بخش الف با نشان «یونانی» آورده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/%D8%A3%D9%88%D9%82%D9%8A%D8%A7%D9%86%D9%88%D8%B3\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"TAD:5\", \"status\": \"supports\", \"note\": \"TAD_pages.txt leaf 9 (= printed p. 5 on the offset recorded in refs_online.json, leaf − 4) is the tail of the alif section, running أوقة … أوكاريستيا … انجيل; between أوقة (TAD.txt line 255) and أوكاريستيا (line 259) stands line 257, the أوقيانوس article, whose OCR reads 'يوناني … معناه مسرع وعربية البحر المحيط' — Greek, glossed 'swift', Arabic equivalent al-baḥr al-muḥīṭ. So al-'Unaysi does place the word on p. 5 and does derive it from Greek (via ὠκύς 'swift'), which is both Nourai's arrow and the alternative his NOTE ascribes to TAD:5. The Greek word itself was lost in the OCR and no page image of TAD is available (tools/ref_page.py reports 'no scan of TAD covers printed page 5').\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. أوقيانوس (Arabic)\", \"stance\": \"supports\", \"note\": \"'Borrowed from Ancient Greek Ὠκεανός (Ōkeanós). Doublet of قَامُوس (qāmūs).' Noun: 'أُوقْيَانُوس (ʔūqyānūs) — (archaic) ocean.'\"},\n      {\"src\": \"TAD\", \"where\": \"p. 5, alif section\", \"stance\": \"supports\", \"note\": \"See ref_check: the article stands between أوقة and أوكاريستيا and is tagged يوناني.\"},\n      {\"src\": \"AFM\", \"where\": \"grep of AFM.txt / AFM_pages.txt for اوقيانوس / قيانوس\", \"stance\": \"silent\", \"note\": \"Addi Shir's Kitab al-Alfaz al-Farisiyya al-Mu'arraba covers only Persian loanwords in Arabic, so a Greek loan like ūqyānūs is outside his scope and does not appear.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Persian\",\n     \"words\": \"oqyânŭs «اقیانوس» : ocean\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Persian اقیانوس oqyānus is the Arabic أوقيانوس taken over into Persian with the initial hamza-alif simplified to a plain alef and the Arabic ū of the first syllable reduced to o- in the Persian pronunciation. Mo'in's entry says so twice over: 'اقیانوس ( اُ ) [ معر. ] ( اِ.) مأخوذ از یونانی . دریای بسیار بزرگ .' — the tag [معر.] marks it an Arabicised (hence Arabic-mediated) word, and 'مأخوذ از یونانی' names Greek as the ultimate source, exactly the two-step route Nourai draws (Greek > Arabic > Persian). The word is a learned geographical term of the classical and modern periods, not an old inherited one.\",\n     \"derivation_fa\": \"«اقیانوس» فارسی همان «أوقيانوس» عربی است که با ساده‌شدن همزهٔ آغازین به الفِ ساده و کوتاه‌شدن ū هجای نخست به o- در تلفظ فارسی وارد شده است. مدخل معین این را دوبار می‌گوید: «اقیانوس ( اُ ) [ معر. ] ( اِ.) مأخوذ از یونانی . دریای بسیار بزرگ .» — نشان [معر.] یعنی معرّب، پس واژه از راه عربی آمده، و «مأخوذ از یونانی» سرچشمهٔ نهایی را نام می‌برد؛ یعنی دقیقاً همان دو گامی که نورایی رسم کرده است (یونانی ← عربی ← فارسی). این واژه اصطلاحی جغرافیایی و کتابی است، نه واژه‌ای موروثی و کهن. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://vajehyab.com/moein/%D8%A7%D9%82%DB%8C%D8%A7%D9%86%D9%88%D8%B3\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"MON:327\", \"status\": \"supports\", \"note\": \"Mo'in's entry read at vajehyab.com/moein/اقیانوس: 'اقیانوس ( اُ ) [ معر. ] ( اِ.) مأخوذ از یونانی . دریای بسیار بزرگ .' Both the Arabic mediation and the Greek ultimate source are Mo'in's own words. Page 327 itself cannot be verified online.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"s.v. اقیانوس (vajehyab)\", \"stance\": \"supports\", \"note\": \"'[ معر. ] … مأخوذ از یونانی . دریای بسیار بزرگ .'\"},\n      {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\", \"note\": \"Borhan is a dictionary of Persian (mostly native) words and has no article اقیانوس; the absence is consistent with the word being a learned Arabic-mediated geographical term rather than a Persian lexical item of the kind Borhan collects.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. أوقيانوس (Arabic)\", \"stance\": \"supports\", \"note\": \"Confirms the Arabic form Persian borrowed and its Greek source.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Latin\",\n     \"words\": \"ôceanus : ocean\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin Ōceanus is a straight borrowing of Greek Ὠκεανός, taken in with the Greek mythological and geographical vocabulary well before the classical period and current in Caesar and Cicero for the outer sea beyond the Pillars of Hercules; Greek ō (eta with the circumflex, ω) is rendered by Latin long ō, and the Greek second-declension -ος by Latin -us. Klein's article s.v. ocean gives precisely this chain — 'F. océan, fr. L. ōceanus, fr. Gk. Ὠκεανός' — and Wiktionary's etymology tree for ocean has 'Ancient Greek Ὠκεᾰνός → Latin Ōceanus'. The arrow is drawn from node 1 rather than from the root, which is correct: Latin took the whole word, not its supposed parts.\",\n     \"derivation_fa\": \"لاتینی Ōceanus وام‌گیری مستقیم از یونانی Ὠκεανός است که همراه با واژگان اساطیری و جغرافیایی یونانی و مدت‌ها پیش از دورهٔ کلاسیک به لاتین رفته و در نوشته‌های کایسار و کیکرو برای دریای بیرونیِ آن‌سوی ستون‌های هرکول به کار می‌رود؛ ō یونانی (اُمگا) با ōی بلندِ لاتین و پایانهٔ ‑ος صرف دومِ یونانی با ‑us لاتین برگردانده شده است. کلاین ذیل ocean همین زنجیره را می‌آورد: «فرانسهٔ océan، از لاتینِ ōceanus، از یونانیِ Ὠκεανός»، و درخت ریشه‌شناسی ویکی‌واژه نیز «یونانی باستان Ὠκεᾰνός ← لاتین Ōceanus» دارد. اینکه این پیکان از گرهٔ ۱ کشیده شده نه از خودِ جعبهٔ ریشه، درست است: لاتین کل واژه را گرفت، نه اجزای فرضی آن را. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/ocean\",\n      \"https://en.wiktionary.org/wiki/%E1%BD%A8%CE%BA%CE%B5%CE%B1%CE%BD%CF%8C%CF%82\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD:909\", \"status\": \"not_checked\", \"note\": \"AHD:909 is a page of the main text of the 1975 American Heritage New College Edition, which is not on disk (only Watkins' Indo-European appendix) and is lending-only on archive.org; the Watkins appendix has no entry that yields OCEAN, consistent with the word having no accepted Indo-European root.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. ocean (KLN_1966.txt lines 26000-26001)\", \"stance\": \"supports\", \"note\": \"'ocean, n. — F. océan, fr. L. ōceanus, fr. Gk. Ὠκεανός, \\\"the great river encompassing the whole earth\\\"; hence \\\"the great Outward Sea\\\" (opposed to the Inward or Mediterranean) …'\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. ocean, etymology tree\", \"stance\": \"supports\", \"note\": \"'Ancient Greek Ὠκεᾰνός (Ōkeănós) der. Latin Ōceanus der. Old French occean bor. Middle English *ocean, occean, occian, occyan → English ocean.'\"},\n      {\"src\": \"LAT\", \"where\": \"grep of LAT.txt / LEW_1910.txt for Oceanus\", \"stance\": \"silent\", \"note\": \"Ernout-Meillet and Walde's Latin dictionary have no article Ōceanus (only the phrase 'fretalis Oceanus' quoted s.v. fretalis) — as expected for a transparent Greek proper-name borrowing that Latin etymological dictionaries do not treat.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"English\",\n     \"words\": \"ocean\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English ocean is Latin ōceanus, but not taken directly as the chart's single arrow suggests: it came through Old French occean (Middle French océan) into Middle English occean, occian, occyan from about 1290, displacing the native Old English gārseċġ 'ocean'. Klein makes the French stage explicit ('ocean, n. — F. océan, fr. L. ōceanus'), and Wiktionary's chain is 'from Middle English *ocean, occean, occian, occyan, from Old French occean (later reborrowed or reinforced by Middle French ocean), from Latin Ōceanus, originally from Ancient Greek Ὠκεανός'. The omission of the Old French link is a simplification of the kind the book makes throughout for well-trodden Latin-to-English chains, not an error of substance; the sense in English is from the start the great outer sea, and the mythological Oceanus survives beside it as a doublet.\",\n     \"derivation_fa\": \"«ocean» انگلیسی همان ōceanusِ لاتین است، اما نه یکسره و بی‌واسطه چنان‌که پیکانِ تنهای نمودار می‌نماید: این واژه از راه occeanِ فرانسهٔ کهن (océanِ فرانسهٔ میانه) و از حدود ۱۲۹۰ میلادی به‌صورت‌های occean، occian، occyan به انگلیسی میانه رسید و جای واژهٔ بومیِ انگلیسی کهن gārseċġ «اقیانوس» را گرفت. کلاین مرحلهٔ فرانسوی را صریح می‌آورد («ocean، از فرانسهٔ océan، از لاتینِ ōceanus») و ویکی‌واژه زنجیره را چنین می‌دهد: «از انگلیسی میانه، از فرانسهٔ کهن occean … از لاتین Ōceanus، در اصل از یونانی باستان Ὠκεανός». افتادن حلقهٔ فرانسهٔ کهن ساده‌سازی‌ای است که این کتاب در زنجیره‌های شناختهٔ لاتین‑به‑انگلیسی همواره می‌کند، نه خطای ماهوی؛ معنای انگلیسی از آغاز همان دریای بزرگ بیرونی است و نام اساطیریِ Oceanus نیز همچنان به‌عنوان دوگانه در کنارش مانده است. ادعای نورایی درست است.\",\n     \"sources\": [\n      \"https://en.wiktionary.org/wiki/ocean\"\n     ],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"not_checked\", \"note\": \"Cited by Nourai without a page (the preceding node cites AHD:909). The 1975 New College Edition is not on disk and is lending-only on archive.org; the only AHD material available locally is Watkins' Indo-European appendix, which has no entry yielding OCEAN.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"s.v. ocean\", \"stance\": \"partial\", \"note\": \"'ocean, n. — F. océan, fr. L. ōceanus, fr. Gk. Ὠκεανός …' — same ultimate chain, but Klein inserts the French stage that Nourai's arrow skips.\"},\n      {\"src\": \"Wiktionary\", \"where\": \"s.v. ocean, English section\", \"stance\": \"partial\", \"note\": \"'From Middle English *ocean, occean, occian, occyan, from Old French occean (later reborrowed or reinforced by Middle French ocean), from Latin Ōceanus, originally from Ancient Greek Ὠκεανός (Ōkeanós, \\\"Oceanus\\\", a water deity). Displaced native Old English gārseċġ. … Doublet of Oceanus / Okeanos.'\"},\n      {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century Dictionary, s.v. ocean\", \"stance\": \"silent\", \"note\": \"Grep of WEB_vol1.txt found only compounds and place-names containing 'ocean'; the headword article falls in the unscanned second volume, so Webster could not be quoted here.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n"
}
```


### [2026-09-06T16:15:19.505Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-246.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:15:24.562Z] TOOL CALL #78: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-246.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 246",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T16:15:30.021Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 14, 'transcription_suspect': 2, 'plausible': 1, 'disputed': 1}
root verdicts: {'confirmed': 1, 'plausible': 1, 'disputed': 1}
ref checks: {'supports': 17, 'not_checked': 8}
books consulted: {'supports': 42, 'silent': 12, 'partial': 9, 'contradicts': 8} | by book: {'Wiktionary': 16, 'KLN': 8, 'BQT': 7, 'LKT': 6, 'PLA': 6, 'MON': 5, 'Etymonline': 4, 'WEB': 3, 'PHN': 2, 'AFM': 2, 'TAD': 2, 'DEV': 1, 'HJB': 1, 'PHD': 1, 'NYB': 1, 'HRN': 1, 'HUB': 1, 'AHD-online': 1, 'WLD': 1, 'POK': 1, 'LAT': 1}
```


## [2026-09-06T16:15:51.540Z] AGENT

Done — `data/verification/page-246.json` written, `python3 tools/verify_check.py 246` reports 18/18 nodes and **0 PROBLEM lines**.

**Page 246 (book p. 216), 3 non-redirect entries, 18 nodes**
- Root verdicts: confirmed 1 (Kayik), plausible 1 (Kaž/Kaz), disputed 1 (Keanos)
- Node verdicts: confirmed 14, transcription_suspect 2, plausible 1, disputed 1
- Ref checks: 17 supports, 8 not_checked (ARK, NFI, FWE and the 1975 AHD main-text pages are not obtainable)

Flagged items:
- **disputed — Keanos (root + node 1, Gk. o-keanos)**: no Greek word *keanos exists; the cut ō- + *ḱey- 'lie' is the Benfey/Brugmann etymology. Kent p.164 does state it (ref accurate), but Walde-Pokorny I 358 f. says it was "wohl mit Recht aufgegeben", Beekes reconstructs Pre-Greek *ūkʲān-, Klein calls the Greek word "of uncertain etymology". Only Janda revives it.
- **transcription_suspect — entry 0 node 4, English "caiique"**: not an English word; book misprint for *caique* (French diaeresis set as a second i). `error_in: book`.
- **transcription_suspect — entry 2 node 3, French "casaqueand, casaque"**: "casaqueand" is impossible French; it fuses *casaque* with the Persian ending *-and* discussed in Klein. `error_in: book`. The derivation is also contested: AHD (incl. the very AHD Nourai cites), Lokotsch no.1143, Wiktionary and TLFi take *casaque* from Italian *casacca* ← Turkic *qazaq*; only Klein and Asbaghi keep Persian *kaž-āgand*.
- **plausible — Kaž/Kaz root**: word and gloss right, but "Old Persian" is unsupportable (nothing in Kent; silk is Parthian/Sasanian); Mo'in (BQT 1637 fn. 6) and Asbaghi give MP *kač*, and Wiktionary treats it as a silk-trade Wanderwort shared with Aramaic *qāzzā*, Armenian *kač*.
- **plausible — entry 2 node 7, French gaze ← Arabic qaz**: the better-supported of two rivals (Pihan, Lokotsch 702/1147, Asbaghi, Wiktionary) but Klein and Webster keep the Gaza etymology and Etymonline says there is evidence for neither. Nourai's own NOTE states the dispute correctly.

**No extraction errors** — I rendered PDF p. 246 at 300 dpi and read the Persian and French boxes; the JSON matches the printed page exactly (including «کَز ( کَژ ، غِژ ، غِژغاو )» / «کَزاکند ( کَژاکند )»). Both odd forms are the book's own misprints. Page image filed at `data/verification/sources/refs/ocr/BOOK/246.png`; a hand-read transcript of Borhan-e Qate' p. 1637 (with Mo'in's footnote giving Pahlavi *kac*) is saved at `data/verification/sources/refs/ocr/BQT/1637.vision.txt`; 17 web pages archived via `fetch_source.py`.
