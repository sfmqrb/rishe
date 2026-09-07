# Verification process log — verify-page-327


## [2026-09-07T15:49:31.999Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 327 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-327.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-327.json. Write /home/sfmqrb/git/rishe/data/verification/page-327.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 327` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T15:49:33.978Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T15:49:34.701Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T15:49:34.715Z] TOOL RESULT

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


## [2026-09-07T15:49:35.095Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-327.txt"
}
```


### [2026-09-07T15:49:35.114Z] TOOL RESULT

```
1	=== PDF page 327 (book page 297) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mei 3, Meih; Meigw; Moin : to go; to move, change; common  (refs POK:710,713,715; AHD:1528)
4	#1 (parent #0) [Avestan] refs=POK:710,715; KLN:953 | maëni : punishment ; mithô : false ; mithwara : paired ; mithahya : evil
5	#2 (parent #0) [Latin] refs=KLN:1767 | se-mitita : path
6	  #3 (parent #2) [Arabic] refs=KLN:1767 | samt : way, path, direction ; as-sumut : directions
7	    #4 (parent #3) [Persian] refs=MON:1919 | samt «سمت» : path, direction
8	    #5 (parent #3) [French] refs=None | 
9	      #6 (parent #5) [English] refs=KLN:1767 | zenith, azimuth
10	#7 (parent #0) [Latin] refs=AHD | commŭnis : common ; migâre : change one's place of living
11	  #8 (parent #7) [French] refs=AHD | communisme
12	    #9 (parent #8) [Persian] refs=MON6:1603 |  | extra: کمونیزم ، کمونیسم
13	    #10 (parent #8) [English] refs=AHD | communism, communist ; common, communicate
14	  #11 (parent #7) [English] refs=AHD | migrate, immigration
15	#12 (parent #0) [Germanic] refs=AHD | ga-maid-az : changed for worse (mad) ; missa : in a changed manner, wrongly ; gamainiz : common, ordinary, low value (mean)
16	  #13 (parent #12) [English] refs=AHD | mad ; mis-, mistake, misfortune ; mean 2 : inferior
17	--- entry 1 ---
18	ROOT [Indo-European] Mei 4 : to bind, tie  (refs POK:710)
19	#1 (parent #0) [Avestan / Old Persian] refs=POK:710; KNT:203 | mithra : bond, friendship, kindness, angel of light guarding the truth.
20	  #2 (parent #1) [Persian] refs=BQT:2060; MON5:2056; KNT:203 | mehr «مهر» : angel of light, sun, a month in the Persian calendar | extra: مهربان ، مهرگان ، مهرداد ، میترا
21	  #3 (parent #1) [Greek] refs=KLN:989; AHD:841 | mithras : God of light
22	    #4 (parent #3) [Latin] refs=None | 
23	      #5 (parent #4) [English] refs=None | Mithras : God of light
24	
```


## [2026-09-07T15:49:39.343Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-327.json",
 "description": "Read source JSON page 327"
}
```


### [2026-09-07T15:49:39.382Z] TOOL RESULT

```
{
  "pdf_page": 327,
  "book_page": 297,
  "entries": [
    {
      "root": {
        "name": "Mei 3, Meih; Meigw; Moin",
        "lang": "Indo-European",
        "refs": "POK:710,713,715; AHD:1528",
        "gloss": "to go; to move, change; common"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:710,715; KLN:953",
          "words": [
            {"translit": "maëni", "gloss": "punishment", "script": null},
            {"translit": "mithô", "gloss": "false", "script": null},
            {"translit": "mithwara", "gloss": "paired", "script": null},
            {"translit": "mithahya", "gloss": "evil", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Latin",
          "refs": "KLN:1767",
          "words": [
            {"translit": "se-mitita", "gloss": "path", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Arabic",
          "refs": "KLN:1767",
          "words": [
            {"translit": "samt", "gloss": "way, path, direction", "script": null},
            {"translit": "as-sumut", "gloss": "directions", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:1919",
          "words": [
            {"translit": "samt", "gloss": "path, direction", "script": "سمت"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 3,
          "lang": "French",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:1767",
          "words": [
            {"translit": "zenith, azimuth", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "commŭnis", "gloss": "common", "script": null},
            {"translit": "migâre", "gloss": "change one's place of living", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "French",
          "refs": "AHD",
          "words": [
            {"translit": "communisme", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Persian",
          "refs": "MON6:1603",
          "words": [],
          "script_extra": "کمونیزم ، کمونیسم",
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "communism, communist", "gloss": null, "script": null},
            {"translit": "common, communicate", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "migrate, immigration", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "ga-maid-az", "gloss": "changed for worse (mad)", "script": null},
            {"translit": "missa", "gloss": "in a changed manner, wrongly", "script": null},
            {"translit": "gamainiz", "gloss": "common, ordinary, low value (mean)", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "mad", "gloss": null, "script": null},
            {"translit": "mis-, mistake, misfortune", "gloss": null, "script": null},
            {"translit": "mean 2", "gloss": "inferior", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mei 4",
        "lang": "Indo-European",
        "refs": "POK:710",
        "gloss": "to bind, tie"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:710; KNT:203",
          "words": [
            {"translit": "mithra", "gloss": "bond, friendship, kindness, angel of light guarding the truth.", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2060; MON5:2056; KNT:203",
          "words": [
            {"translit": "mehr", "gloss": "angel of light, sun, a month in the Persian calendar", "script": "مهر"}
          ],
          "script_extra": "مهربان ، مهرگان ، مهرداد ، میترا",
          "note": null,
          "quote": {
            "text": "روز مهر و ماه مهر وجشن فرخ مهرگان - مهر بفزا ای نگار مهر چهر مهربان",
            "poet": "Mas`ŭd Sa`d Salmân"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Greek",
          "refs": "KLN:989; AHD:841",
          "words": [
            {"translit": "mithras", "gloss": "God of light", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "Mithras", "gloss": "God of light", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T15:49:39.631Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T15:49:39.670Z] TOOL RESULT

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


## [2026-09-07T15:50:12.423Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','MON','BQT','KNT','WLD','IEC','SYN','BRT','PHD','NYB','HRN','HUB','LEW','LAT','SKT','ARY','AHM']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600]); print()\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-07T15:50:13.208Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls tools/",
 "description": "List verification dir"
}
```


### [2026-09-07T15:50:13.799Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

AHM {"title": "I. Gershevitch, The Avestan Hymn to Mithra, Cambridge 1959", "edition_found": "1959", "kind": "archive_djvu", "url": "https://archive.org/details/gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "identifier": "gershevitch-ilya-the-avestan-hymn-to-mithra-cambridge-university", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHM.txt", "page_offset": "leaf = printed + 14 (e.g. leaf 18 = p.4). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>"
```


### [2026-09-07T15:50:13.836Z] TOOL RESULT

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
page-134.json
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
page-149.json
---
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-07T15:50:16.630Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T15:50:16.672Z] TOOL RESULT

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


## [2026-09-07T15:50:17.930Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/page-316.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:4000])\n\"",
 "description": "Sample recent verification file"
}
```


### [2026-09-07T15:50:19.300Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Mâ, Mâ-ter",
 "verdict": "plausible",
 "modern_form": "PIE *méh₂tēr 'mother' (Pokorny māter- 700–701; AHD māter-), itself built on the nursery word *mā- / *méh₂- 'mother' (Pokorny mā-3, 694)",
 "note": "Both halves of the root box are real reconstructions and the language label 'Indo-European' is right, but two details of the gloss are Nourai's own. (1) Pokorny's mā-3 (p.694, the page Nourai cites) is glossed 'mother (expr. root)', not 'breast'; the 'breast' sense comes only from the reduplicated derivatives (L. mamma 'mother’s breast, nipple', mamilla), so it is a back-projection. (2) 'Mā-ter: feeder (of the family)' with the cross-reference to Ter 3 analyses -ter- as the agent suffix. Watkins and Walde–Pokorny call it the KINSHIP suffix and offer no such gloss ('Based ultimately on the baby-talk form ma-2, with the kinship term suffix -ter-'); Skeat's older view was '√MĀ to measure', i.e. 'manager of the household'; and Wiktionary reports a minority modern view of a genuine verbal root *méh₂- 'to nurse, to mother' — which is the closest anyone comes to Nourai's 'feeder', but it is not the standard account. Also note the page numbers: 694 is mā-3, while māter- is Pokorny 700–701. Nourai's closing remark about a nursery word becoming the usual term is a paraphrase of Buck 2.36 (SYN:103), which he cites correctly. Everything downstream (Avestan–Pahlavi–Persian; Germanic; Latin; Greek) is sound; the one substantive error on the page is in node #8.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *méh₂tēr «مادر» (پوکورنی ۷۰۰–۷۰۱) و واژهٔ کودکانهٔ *mā- (پوکورنی ۶۹۴) هر دو واقعی اند و برچسب «هندواروپایی» درست است؛ امّا دو نکتهٔ معنایی از خود نورایی است: یکی آنکه پوکورنی در ص ۶۹۴ mā-3 را «مادر» معنی کرده و نه «پستان» — معنای پستان تنها از مشتقّات دوگان‌شده (mamma, mamilla لاتینی) برمی‌آید؛ دوم آنکه تفسیر «mā-ter = خوراک‌دهندهٔ خانواده» پسوند -ter- را پسوند فاعلی گرفته، در حالی که واتکینز و والده‌پوکورنی آن را پسوند واژگان خویشاوندی می‌دانند و چنین معنایی نمی‌دهند (ویکی‌واژه دیدگاهی اقلیتی را گزارش می‌کند که *méh₂- را ریشهٔ فعلی «شیر دادن، مادری کردن» می‌گیرد). در مجموع ریشه با احتیاط پذیرفتنی است و همهٔ شاخه‌های پایین‌دست درست اند؛ تنها خطای جدی این صفحه در گرهٔ ۸ («ممه») است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/m%C3%A9h%E2%82%82t%C4%93r",
  "https://www.etymonline.com/word/mother"
 ],
 "ref_check": [
  {
   "ref": "POK:694",
   "status": "partial",
   "note": "Pokorny 694 is 'mā-3, Meaning: mother (expr. root), Note: redupl. māmā, māmmā ... Material: Old Indic mā ‘mother’ ... npers. mām, māmā, māmī ‘mother’ ... Latin mamma ... mamilla ‘nipple’ ... Page(s): 694' (POK_full.txt l.57758ff, grep 'lemma: mah 3'). It therefore supports the Mā- half of the root box, but glosses it ‘mother’, not ‘breast’; Pokorny's separate lemma 'mahter-, Meaning: mother, Note: based on a babble-word mah-, see there ... Page(s): 700-701' is where Mā-ter belongs, i.e. p.700-701 and not 694."
  },
  {
   "ref": "PRT:386,863",
   "status": "not_checked",
   "note": "Partridge, Origins (1958) — no open copy: all 8 archive.org copies are lending-only per data/verification/sources/refs_online.json (kind 'archive_restricted'), and there is no local OCR."
  },
  {
   "ref": "SYN:103",
   "status": "supports",
   "note": "Buck 2.36 on printed p.103 (SYN.txt l.2813): ‘2.36. ‘Mother’. 1. IE *māter-, prob. ... starting fr. a nursery word of the ma type. Walde-P. 2.229. Here belong the Grk., Lat., Ir., Gme. ... and Indo-Iranian forms’ and ‘2. Nursery words that have become the usual terms. Type mama (above, p. 94, Walde-P. 2.221) in It. mamma ... and W., Br. mam.’ Nourai's own remark (‘probably started as a nursery word and became a usual term’) is a paraphrase of exactly these two headings."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. II 221 (§3 mā) and Bd. II 229 (matēr-)",
   "stance": "supports",
   "note": "WLD_Bd2_pages.txt leaf 225 (printed 221):
```


## [2026-09-07T15:50:26.790Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: mei\" POK_full.txt | head -40",
 "description": "Find mei lemmas in Pokorny"
}
```


### [2026-09-07T15:50:26.838Z] TOOL RESULT

```
58098:Root / lemma: meihgh-, also meihk- 
58135:derived the truncated Root/ lemma: meigh-, also rneik-: "to glimmer, twinkle; mist'. 
58149:Root / lemma: meihgh- 
58198:Root / lemma: meih-g"- 
58257:Root / lemma: meih-1 
58298:Root / lemma: meih-2 
58337:Root / lemma: meih-3 
58368:Root / lemma: meih-4 
58394:Root / lemma: meih-5 mi-neu- 
58439:Root / lemma: meih-6, meihu-, min(u)-, mim(ei)- 
58460:Root / lemma: meih-no- 
58482:Root / lemma: meihs- 
58506:Root / lemma: meiht(h)-1 
58524:Root / lemma: meih-t(h)-2 
59600:ze/77s/a "vengeance, revenge' (common Slavic alb. ze- prefix) see Root/ lemma: mei-t(h)-2 
60696:Root / lemma: mei-7: moi-. mT- 
60806:Root / lemma: meig- (or melag-1) {*melagh-)
```


## [2026-09-07T15:50:27.916Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"^mei-\\|mei-1\\|mei-2\\|mei-3\\|mei-4\" AHD_watkins1985.txt | head -40",
 "description": "Find mei in Watkins"
}
```


### [2026-09-07T15:50:27.966Z] TOOL RESULT

```
733:mei-'
734:mahat-, great: MAHARAJAH, MAHARANI, MAHARISHI, MAHATMA, MAHAYANA, MAHOUT. [Pok. meg(h)- 708.] mei-'. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin medre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE. 2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), “changed (for the worse),” abnormal, in Old English gemdd, insane: MAD; b. Latin mitdre, to change: MEW!, MOLT, MUTATE; COMMUTE, PERMUTE, REMUDA, TRANSMUTE; C. Latin miituus, “done in exchange,” borrowed, reciprocal, mutual: MUTUAL. 3. Suffixed extended zero-grade form *mit-to- in Ger- manic “missa-, “in a changed manner,” abnormally, wrongly, in: a. Old English mis-, mis-: Mis-!; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE; C. Ger- manic *missjan, to go wrong, in Old English missan, to miss: MISs!, 4, Suffixed o-grade form *moi-n- in com- pound adjective *ko-moin-i-, “held in common” (*ko-, together; see kom), in: a. Germanic *gamainiz in Old English geméne, common, public, general: MEAN?; (DE- MEAN?); b. Latin commiinis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). 5. Suffixed o-grade form *moi-nes- in: a. Latin minus, “service performed for the community,” duty, work, “public spectacle paid for by a magistrate,” gift: MUNICI- PAL, MUNIFICENT, REMUNERATE; b. Latin immiinis (in-, negative prefix; see ne), exempt from public service: IMMUNE. 6. Extended form *()meigv- in: a. Greek amei- bein, to change: AMOEBA; b. Latin migrdre, to change one’s place of living: MIGRATE; EMIGRATE. [Pok. 2. mei-, 3. mei- 710, meig¥- 713, 2. meit(h)- 715.] mei-2. Small. 1. Greek meidn, less, lesser: MEIOSIS; MIo- CENE. 2. Latin nimis, too much, very (< *ne-mi-s, “not little’; ne-, negative prefix; see ne). 3. Suffixed zero-grade form *mi-nu- in: a. Latin minuere, to reduce, diminish: MENU, (MINCE), MINUEND, MINUTE2; COMMI- NUTE, DIMINISH; b. Latin minor (influenced by the comparative suffix -or), less, lesser, smaller: MINOR, MINUS, MIS-!; MINUSCULE; GC. further suffixed (superla- tive) form *minu-mo- in Latin minimus, least: MINIMUM; d. Latin minister, an inferior, servant (formed after magister, master; see meg-): MINESTRONE, MINISTER, MINISTRY, MYSTERY?; @. Russian men’she, less: MENSHE- vik. [Pok. 5. mei- 711.] mei-3, To fix; to build fences or fortifications. 1. Suffixed o-grade form *moi-ro- in: a. Germanic *mair-ja- in Old English mére, boundary, border, landmark: MERE®; b. Latin miirus, wall: MURAL, MURAMIC ACID, MURE; IMMURE. 2. Suffixed o-grade form *moi-ni- in Latin miinire, to fortify, protect, strengthen: MUNITION; (AM- MUNITION), PRAEMUNIRE, PREMUNITION. 3. Possibly suffixed lengthened-grade form *méi-t- in Latin méta, boundary stone, limit: METE?. [Pok. 1. mei- 709.] mei-4, To tie. 1. Suffixed zero-grade form *mi-tro-, “con- tract, that which binds,” in: a. Greek mitra, headband, earilier a piece of armor worn around the waist: MITER; b. Old Persian Mithra-, name of a god (< “contract” < “bond”): MiTHRAS; c. Russian mir, commune, joy, peace (possibly borrowed from Iranian): mR. 2. Possibly a suffixed zero-grade form *mi-to- in Greek mitos, a warp thread: MITOSIS; DIMITY, MITOCHONDRION, SAMITE. [Pok. 4. mei- 710.] méGi-. Mild. Contracted from *meoi-. Suffixed zero-grade form *mi-ti- (< *mis-ti-) in Latin mitis, soft: MITIGATE. [Pok. 7. mei- 711.] meigh-. To urinate, 1. Germanic suffixed form *mih-stu-, urine, hence mist, fine rain, in: a. Old English mist, mist: MIST; b. Middle Dutch mieselen, to drizzle, perhaps akin to the source of Middle English misellen, to drizzle: MIZZLE; Cc. Germanic diminutive form *mihst-ila-, mistle- toe (which is propagated through the droppings of the missel thrush), in Old English mistel, mistletoe: (MISSEL THRUSH), MISTLETOE. 2. Suffixed form *migh-tu- in
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1385:coMAl keme- COMB gembh- COMBAT battuere COMBINE dwo- COMBUSTION eus- COME gWa- COMEDO ed- COMEDY wed-2 COMESTIBLE ed- COMFIT dhé-1 COMFORT bhergh-2 COMITIA  ei-1 COMITY smei- COMMA skep- COMMAND man-2 COMMANDO man-2 COMMEMORATE (s)mer-1 COMMENCE ei-1 COMMEND man-? COMMENSURATE mé-2 COMMENT men-! COMMERCE merk-2 COMMINUTE mei-2 COMMISERATE miser COMMIT (s)meit(a)- COMMIX meik- COMMODE med- COMMODIOUS med-
1387:COMMODITY med- COMMON mei-! COMMOTION meue- COMMUNE mei-1 COMMUNICATE mei-1 COMMUNISM mei-1 COMMUTE mei-1 COMPACT! pag- COMPANION pa- COMPANY pa- COMPARE pera-2 COMPART pere-2 COMPASSION pé(i)- COMPEL pel-6 COMPELLATION pel-6 COMPENDIUM (s)pen- COMPENSATE (s)pen- COMPETE pet- COMPLACENT plak-! COMPLAIN plak-2 COMPLECT plek- COMPLETE pele-1 COMPLEX plek- COMPLICATE plek- COMPLICE plek- COMPLIMENT pele-1 COMPLY pele-1 COMPONENT apo- COMPORT per-2 COMPOSE apo-, paus-, COMPOSITE apo- COMPOSITION apo- COMPOUND apo- COMPRADOR pere-1 COMPREHEND ghend- COMPRESS per-5 COMPRISE ghend- COMPROMISE (s)meit(9)- COMPUNCTION peuk- COMPURGATION peue- COMPUTE peu- COMRADE kamer- con! kom
1392:CONFOUND gheu- CONFRERE bhrater- CONFUSE gheu- CONFUTE bhau- CONGE mei-1 CONGEAL gel-3 CONGENER gene- CONGENIAL gene- CONGENITAL gene- CONGERIES gerere CONGEST gerere CONGLOBATE gel-1 CONGLOMERATE gel-1 CONGLUTINATE gel-1 CONGRATULATE gWera-3 CONGREGATE ger-! CONGRESS ghredh- CONGRUENT ghréu- CONIDIUM keni- CONIOSIS keni- CONJECTURE yé- CONJOIN yeug- CONJUGAL yeug- CONJUGATE yeug- CONJUNCT yeug- CONJURE yewes- CONNATE gene- CONNECT ned- CONNIVE kneig’h- CONNOISSEUR gn6- CONNOTE gné- CONNUBIAL sneubh- CONQUER quaerere CONQUIAN kom, kWo- CONSCIENCE skei- CONSCIOUS | skei- CONSCRIPT skribh- CONSECRATE sak- CONSENT sent- CONSEQUENT sekw-1 CONSERVE ser-1 CONSIDER sweid-1 CONSIGN sekw-1 CONSIST sta- CONSOCIATE sekw-1 CONSOLE! sel-2 CONSOLIDATE sol- CONSOLUTE leu-1 CONSONANT swen- CONSORT ser-3 CONSPICUOUS _ spek- CONSPIRE spirare CONSTABLE ei-1 CONSTANT sta- CONSTELLATION  ster-3 CONSTERNATE  ster-2 CONSTIPATE  steip- CONSTITUTE sta- CONSTRAIN | streig- CONSTRUCT  ster-2 CONSUETUDE s(w)e- CONSUME em- CONTACT tag- CONTAIN ten- CONTAMINATE tag- CONTEMPLATE tem- CONTEND ten- CONTEST trei- CONTEXT teks- CONTINUE ten- CONTORT terkw- CONTOUR tera-1 CONTRA- kom CONTRABAND bha-2 CONTRACT tragh- CONTRADICT deik- CONTRARY kom CONTRAST sta- CONTRAVENE gWa- CONTRITE tere-1 CONTRIVE trep-2 CONTROL ret- CONTROVERSY wer-3 CONTUSE (s)teu- CONVALESCE wal- CONVECTION wegh- CONVENE gWa- CONVENIENT gWa- CONVENT gWa- CONVENTICLE gWa- CONVENTION gWa- CONVERGE wer-3 CONVERSE! wer-3 CONVERT wer-3 CONVEX wegh- CONVEY wegh- CONVINCE weik-5 CONVIVIAL gWei- CONVOKE wekw-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1426:DIET? deiw- DIFFER bher-! DIFFICULTY dhé-1 DIFFIDENT bheidh- DIFFRACTION bhreg- DIFFUSE gheu- DIG dhigw- DIGEST gerere DIGIT deik- DIGNIFY dek-1 DIGNITY dek-1 DIGRESS ghredh- DIKE dhig¥- DILATE stela- DILATORY tela- DILIGENT leg-1 DILUTE leu(@)- DIME dekm DIMENSION mé-2 DIMER (s)mer-2 DIMINISH mei-2 DIMITY mei-4
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1690:IRISH peie- IRISITIS _ wei-1 IRON eis-1 IRONY wer-6 IRREMEABLE mei-1 IRRIGATE reg-2 IRRUPT reup-
1790:MAD mei-1
1838:MEAN! mel-no- MEAN? mei-1
1841:MEATUS mei-1 MECHANIC magh-1 MECHANISM magh-! MECHANO- magh-! MECONIUM mak-1 MECOPTERAN miak-, pet- MEDDLE meik- MEDIAL medhyo- MEDIAN medhyo- MEDIASTINUM medhyo- MEDIATE medhyo- MEDICAL med- MEDICATE med- MEDICINE med- MEDICO med- MEDIEVAL alw-, medhyo- MEDIOCRE medhyo- MEDITATE med- MEDITERRANEAN medhyo-, ters- MEDIUM medhyo- MEDLEY meik- MEDULLA (s)mer-3 MEED mizdho-
1846:MELON mélion MELT mel-1 MEMBER méms- MEMBRANE méms- MEMENTO men-! MEMORABLE (S)mer-1 MEMORANDUM (s)mer-1! MEMORY (s)mer-1 MENACE men-2 MENAGE men-3 MENARCHE = arkhein, mé-2 MEND mend- MENDACIOUS mend- MENDICANT mend- MENHIR s6-2 MENINX méms- MENISCUS mé-2 MENOPAUSE mé-2 MENSCH man-! MENSES mé6-2 MENSHEVIK mei-2 MENSTRUAL mé-2 MENSTRUATE mé-2 MENSURAL mé-2 MENTAL men-1 MENTION men-1 MENTOR men-1 MENU mei-2 MERCENARY merk-2 MERCER merk-2 MERCHANT merk-2 MERCURY merk-2 MERCY merk-2 MERE! mer-1 MERE? mori-
1847:MERE’ mei-3
1857:METE2 mei-3 METEMPSYCHOSIS bhes-? METER! mé-2
1862:MEW! mei-1 MEZZO-RELIEVO legh- MI smei-
1869:MICROPYLE pulé MICTURATE meigh- MID! medhyo- MIDDLE medhyo- MipcaRD medhyo- MIDGE mu-2 MIDRIFF krep- MIDWIFE me-2 MIGHT! magh-! MIGRAINE ker-1 MIGRATE mei-1 MIL! gheslo-
1872:MIME mimos MIMESIS mimos MIMIC mimos Mimir (s)mer-1 MINACIOUS men-2 MINCE mei-2
1874:MINE? me-1 MINERVA men-! MINESTRONE mei-2 MINGLE mag- MINIKIN men-1 MINIMUM mei-2 MINISTER mei-2 MINISTRY mei-2 MINIVER wer-! MINNESINGER men-!, sengWh- MINNOW men-4 MINOR mei-2 MINT! men-1 MINUEND mei-2 MINUS mei-2 MINUSCULE mei-2 MINUTE? mei-2 MIOCENE mei-2 MIOSIS mul-
1875:MIR mei-4 MIRACLE smei- MIRAGE smei- MIRE meu- MIRROR smei- MIRTH mregh-u- MIs-1_ mei-1, mei-2 MISADVENTURE gWa- MISANTHROPE ner-2 MISCEGENATION gene-, meik- MISCELLANEOUS meik- MISCHIEF kaput MISCIBLE meik- MISCREANT kerd-1 MISER miser MISERABLE miser MISERICORD kerd-1 MISERY miser MISFEASANCE dhé-1 MISHAP kob- MISNOMER nd-men- MISONEISM newo- MISPRISION ghend-, mei-1 MIss! mei-1 MISSEL THRUSH meigh- MISSILE (s)meit(9)- MISSION (s)meit(a)- MISSIVE (s)meit(e)- MIST meigh- MISTAKE mei-1 MISTER meg- MISTLETOE meigh- MISTRAL meg- MISTRESS meg- MITE! = mai-1
1877:MITER mei-4 MITHRAS mei-4 MITIGATE mé6i-
1879:MITOCHONDRION ghrendh-, mei-4 MITOSIS mei-4 MITTEN medhyo- MITTIMUS (s)meit(a)- MIX meik- MIXTURE meik- MIZZEN medhyo- MIZZLE meigh- MNEMONIC men-! MNEMOSYNE men-1 MOAN mei-no- MOB meue- MOBILE meue- MODAL med- MODE med- MODEL med- MODERATE med- MODERN med- MODEST med- MODICUM med- MODIFY dhé-1, med- MODIOLUS med- MODULATE med- MODULE med- MODULUS med- MOGUL! miik- MOIETY medhyo- MOIL mel-1
1881:MOLE‘ mele- MOLECULE m6- MOLEST mo- MOLLIFY dhé-1, mel-1 MOLLUSK mel-1 MOLT mei-1
1896:MUNICIPAL kap-, mei-1
1897:MUNIFICENT mei-1 MUNITION mei-3 MURAL mel-3 MURAMIC ACID mei-3 MURDER mer-2 MURE mei-3 MURINE mis- MURK mer-1 MURMUR mormor- MURRAIN mer-2 MURREY moro- Musca mu-2 MUSCARINE mu-2 MUSCLE miis- MUSE misum Muse men-1 MUSEUM men-! MUSH2 mu-2 MUSIC men-1! MUSKET mu-2 MusT! med- MUSTS ~=meu- MUSTACHE mendh-2
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2125:POST- apo- POSTBELLUM duellum POSTERIOR apo- POSTICHE apo- POSTMERIDIAN deiw- POST-MORTEM apo-, mer-2 POSTPARTUM _pere-1 POSTSCRIPT skribh- POSTULATE prek- POSTURE apo- POTABLE p0(i)- POTATION pd(i)- POTATORY pd(i)- POTENT poti- POTION po(i)- POTPOURRI pu-2 POUCH beu-! POULARD pau- POULTICE pel-1 POUNCE! peuk- POUNCE? (s)poi-mo- POUNCE3 peuk- POUND! (s)pen- POUNDS bend- POUSETTE pel-6 POUT beu-! POVERTY pau- POWDER pel-1 POWER poti- PRAAM per! PRACTICAL prak- PRACTICE prak- PRAEDIAL wadh-1 PRAEMUNIRE mei-3 PRAENOMEN no-men- PRAETOR ei-1 PRAGMATIC prak- PRAISE per-6 PRANDIAL ed- PRATINCOLE kwel-1 PRAXIS prak-
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2209:SAL sal-1 SALACIOUS  sel-4 SALAD sSal-1 SALAMI sal-1 SALARY Sal-1 SALE sel-3 SALI-  sal-1 SALICIN sal(i)k- SALIENT sel-4 SALINE sal-1 SALLOW! | sal-2 SALLOW? | sal(i)k- SALLY sel-4 SALMON sel-4 SALON sel-1 SALOON sel-1 SALSA Sal-1 SALT sal-1 SALTCELLAR sal-1 SALTPETER petra, sal-1 SALUBRIOUS sol- SALUTARY sol- SALUTE sol- SALVAGE sol- SALVE! selp- SALVO! sol- SAME sem-! SAMITE mei-4 SAMIZDAT d6-, sem-1
2402:TRANSIENT ei-1, tera-2 TRANSIT ei-1 TRANSITIVE ei-1 TRANSLATE tele- TRANSLITERATE deph- TRANSLUCENT leuk- TRANSMIT (s)meit(@)- TRANSMUTE mei-1 TRANSOM tere-2 TRANSPIRE § spirare TRANSPONTINE pent- TRANSPORT per-2 TRANSUDE sweid-2 TRANSVERSE wer-3 TRAP! der-1
```


## [2026-09-07T15:50:35.969Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '58257,58420p' POK_full.txt",
 "description": "Pokorny mei lemmas"
}
```


### [2026-09-07T15:50:36.018Z] TOOL RESULT

```
Root / lemma: meih-1 

Meaning: to strengthen; pole 

Material: Old Indie minotT fastens, founds, builds ', mitf-i. " erection, fundation ', mita- 

"fastens', metar-^ der Aufrichter', mayukha-xx\. "peg, plug, ray', npers. /77ex"peg, plug, 

nail' {*maixa-), sogd. myyk^s.. Old Indie sumeka-^ well founded, tight, firm'; 



Latin PI. moenia^ defensive walls, ramparts, bulwarks, city walls ', munid{ardc\. 
moenio), -Tre^ to wall, defend with a wall, fortify, defend, protect, secure, strengthen '; 
mums, old mo/ros'\Na\\'; 

alb. mur' wall ' a Latin loanword. 

Old Irish -tuidmen {*to-dT-mi-na-t} "fastens', verbal noun tuidme; 

Germanic */775//7/7a- "boundary post, frontier post ', Old English msere, gemsere'\\m\t, 
boundary, region, area'. Old Icelandic /5/70''a-/77^/7" limit, boundary, border land ', etc. 

meih-d(h)-\v\. Middle Irish me{/)derc\. " nape ' {*meih-d-io-)\ Latvian miet^ enclose with 
posts ', maTdtV decorate, ornament, adorn '. 

With /extended me[i]ht-. meiht-. m/t-\n: 

Old Indie methf- m., methTi. (Prakrit medhf-, medhT, medhl) " pillar, jamb ', mft- f. " 
column, jamb ' (perhaps also in Avestan barazi-mita-, if " high column '), Armenian moit'^ 
pillar'; Latin meta^ a cone, pyramid, a conical column at the end of the circus, turning- 
post, goal, a goal, winning-post, mark, an end, period, extremity, boundary, limit '; Middle 
Irish methas^ border land, frontier land ' ( *mitostu-)\ Old Icelandic me/dr'tree, balk, beam, 
shaft, pole'; Lithuanian mietas, Latvian /77/e/5 "picket, pole'; zero grade Lithuanian mita^ 
Stecken zum Netzestricken '; probably also Old Bulgarian mesto, Serbo-Croatian mjesto, 
Czech /77/s/o "place' from * moiPto-ox *me[i]Pto-. 

References: WP. II 239 f., WH. II 30 f., Trautmann 165 f.; 
See also: compare meih-4. 
Page(s): 709 

Root / lemma: meih-2 

Meaning: to change, exchange 

Material: Old Indie /77ay5/e "tauschf, n/-maya-m. "exchange'; Latvian m/ju, /r7/7 "exchange'. 

With /^formant: Latin mun/s' ready to be of service ', mOnus, -en's {arch, moenus) " a 
service, office, post, employment, function, duty, a service, favor, kindness, a present, gift, 
a public show, spectacle, entertainment, exhibition, show of gladiators (given by 
magistrates) ', munia, -/um {o\d moen/a)' duties, functions, official duties ', /mmun/s' not 
bound, free from obligation, disengaged, unemployed ', communis {0\6 Latin comoinfem]) 
" common, general, universal, public ' (= Gothic etc. gamains), Oscan mufnikad^ common, 



general, universal, public ', Umbrian muneklu^ a service, office, post, employment, 
function, duty '; 

Old Irish moin, main^ preciousness, treasure, tribute', cfag-md/n/'goo6 gifts, favors'; 
ablaut, cymr. mwyn^ value, worth ' {*meino-)\ 

Gothic gamains. Old English gemaene. Old High German gimein'r common, shared '; as 
" exchanged = falsified, misrepresented, forged, counterfeit, distorted ' also Old High 
German mein^ incorrect, deceitful' (Modern High German Meineid), Old English man 6s., 
Old Icelandic meinn ' harmful ', mein 'damage, pity, misfortune'; 

Lithuanian ma/has m., Latvian /77a//7s 'exchange', Lithuanian mainau, -yti, Latvian mamft 
'swap, vary, exchange, barter'; Old Bulgarian mena^ variation, change ', izmeniti^ 
Siapsipsiv, 5iaAaTT£iv '. Here also Old Indie menf-i. ' revenge, vengeance ', Avestan 
maeni- ' punishment ' (compare Old Bulgarian mbstb ' revenge ' from the extension root 
form meit-). 

Maybe alb. Geg meni, Tosc meri^ revenge, vengeance '. 

extension root form see below mei-g"-, mei-R-, mei-t(h)-. 

References: WP. II 240 f., WH. I 254 f., II 128, Berneker II 48 f., Trautmann 175 f. 
Page(s):710 

Root / lemma: meih-3 

Meaning: to wander, go 

Material: Latin meo, -are^ to go, pass' (perhaps previous a-verb =) poln. mijam, mijac, 

Czech mfjfm, mfjeti^ pass, elapse, avoid '; on this basis could also be based *meia- na- 

present *mi-nami : Old Bulgarian ming, -gti^ pass, elapse ' (also minujg, minovatT 

TTpopaivsiv ') and mcymr. mynet^Qo"; Old Bulgarian mimo^ over, past, finished '; (compare 

gr. M^MCx;" mummer, performer'?) 

here also the river names gall. Moenus' Main, river in Germany ', Middle Irish A^o//7(in 
Kerry, the county in Ireland), poln. Mien, Mianka, *meihn-\v\ poln. Minia, zero grade m/n-\n 
Lithuanian Minija, poln. Mnina, hispan. M>7/^s(Galicia), Etruria Minio. 

Note: 

Around 1700 BC, a highly sophisticated culture grew up around palace centers on Crete: 
the Minoans. 



The relationship migrare: apsipsiv allows the old resemblance with meih-'s\Nap, vary, 
exchange' as " local change ' seem possible. 

References: WP. II 241, WH. II 73, Trautmann 176, Berneker II 59, Krahe BzfN 1, 256 f. 
Page(s):710 

Root / lemma: meih-4 

Meaning: to bind 

Material: Old Indie mitra-v\. (secondary m.) "friend' (originally " friendship' from 

"*association '), Avestan mi^ra-rw. " friend; pact, covenant; name of a God (personification 

of the covenant) ', Old pers. MiPra-^ God's name '; 



gr. hom. Mirpri 'belt; head fascia, Mitra'; doubtful |jiTO(; " Einschlagfaden '; 



Latvian miemuri, meimuri^ Femerstricke '. 

References: WP. II 241 f., GiJntert Weltkonig 50 f.; 

See also: compare mei-1. 

Page(s):710 



Root / lemma: meih-5 mi-neu- 

Meaning: to lessen, small 

Material: Old Indie minati, minoti^ diminishes, damages, hinders ', mTyate, mJyate' 

diminishes ', participle Perf. mlta-\ manyu-mT-^ the diminishing, destructive rancor'; 

gr. pivuGco ' reduce, lessen ', Adj. *mivu-(; in |jivu-cbpiO(; " short-lived, transitory ', |jivuv6a 
" ein kleines Weilchen, nur kurze Zeits ' (Akk. *|jivuv, extension after 5r|-6a); jjeIcjov, [jeTov ' 
less, fewer, inferior, smaller ', after irAEiajv for *[j£ivu)v that still in apisivwv 'better' = "* not 
less ' has received ( *meih-no-), 

Latin ni-mis^ beyond measure, too much, overmuch, excessively, too ' {*ne-mi-is), 
nimiusM] ( *ne-mi-os) " beyond measure, excessive, too great, too much '; Latin minor, n. 
and Adv. minus^ little, small, petty, puny, inconsiderable ', minimus^ least, smallest, very 
small, minute, trifling, insignificant ' {*minu-mos), minister^ subordinate, servant, that 
serves, ministering ' (after magister, Oscan minstrels " little, small, petty, puny, 
inconsiderable '), minerrimus{ : minus af^er vet-errimus: -us), minuo' to make small, 
lessen, diminish, divide into small pieces ', Oscan menvum' to make small, lessen, 
diminish, divide into small pieces ' (probably with neglectful efor /); 



corn, minow^ reduce, lessen ', Middle Breton mynhuigenn, nbret. minvik^ bread without 
the crusts of bread ';
```


## [2026-09-07T15:50:46.077Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '58198,58256p' POK_full.txt; echo \"=====MEITH2=====\"; sed -n '58524,58600p' POK_full.txt",
 "description": "Pokorny meigw and meith2"
}
```


### [2026-09-07T15:50:46.149Z] TOOL RESULT

```
Root / lemma: meih-g"- 

Meaning: to exchange 

Material: Gr. apsipw " change ', Med. ' reciprocate, repay, reward, retribute, shift, wander', 

a|JOi(36(; ' changing ', apoipn "variation'; Note: common lllyrian g"- > b-. 

Latin migro, -are^ to remove, depart, flit, migrate, to go away, depart, pass over, 
change, turn, to leave, abandon, transgress, violate ', Denom. of *mig"-ros. 

References: WP. II 245, WH. II 86 f. 

See also: extension from /77e/-"swap, vary, exchange'. 

Page(s):713 

Root/ lemma: me/h-R- {and meih-g-7) 

Meaning: to mix, stir 

Grammatical information: also mei- : mi-gR-, m/'-n-gR- Prasensstamme also with -so- -sRo-; 



Material: Old Indie meksayati, mimikse^ stirs, mixes ', misra-^ mixes ', misrayatr mixes '; 
Avestan minasti^ mixes ', misvan-^ containing the composite '; myasaite^ sie mischen 
^1 '; common Old Indie -gh- > -ks- > -s- : Avestan -ks- > -s- -s- 

gr. piYvu|ji (more properly psivvuiJi), psi^u), spsi^a, £m(£)ikto, spilYnv "mix, mingle', (jIgyu) 
ds., (jiya, [^'\yba Adv. ' mixed ', [}\yaq, -a5oc; "mixture' (with unclear y); Miayu) "mix, mingle' 
from *|jiy-aKU), or to mezg-\ common Old Indie -gh- > -ks- : Gr. - lllyrian -gh- > -d-, -z- 

Latin misceo, -ere^ mix, mingle, intermingle, blend ' (extension from mi[k]-skd)\ 

Old Irish mesc^ drunk, intoxicated ', Middle Irish also " baffle '; mesc(a)id^ mixes, 
immerses in a liquid, baffles '; cymr. mysgu^rniy!; 

Old High German miskan. Old English m/sc/an'm\x' (rather Latin loanword); 

Lithuanian miesiu, miesti {*meikid) "mix', Iterat. maisau, maisyti, Latvian maisu, maisTt 
ds.; also " plow for the second time '; compare Old Prussian maysotan' mixed ', i.e. 
"varicolored'; Intransit. sum/su and sum/stu, -misti^ get tangled, make a mess, get 
confused ', Latvian sam/sf6s.; Latvian /77/5e/"mix, make mad'; Lithuanian ma/sfasm. " 
agitation' m/sras' mixed ', Latvian m/strs6s.; 

Maybe alb. Geg meshoj^press, push', /77esoy "learn, teach (mix in one's mind?), *make 
mad ' 

Old Bulgarian mesg, mes/t/etc. "mix', has lost its iterate meaning. 

Here probably Old Indie a-mfksa "curd of milk', osset. misin " buttermilk ', Middle Irish 
medg, cymr. maidd, ncorn. meith, abret. meid, gall. -Latin */77es^a (French megue) "wheys' 
( *misga). Old Icelandic mysa "wheys' ( *mihswdn-). common Old Indie -gh- > -ks- : lllyrian - 
Celt, -gh- > -d-, -th- 

References: WP. II 244 f., WH. II 95 f., Trautmann 175; Kuiper Nasalpras. 50, 123. 
Page(s): 714 

=====MEITH2=====
Root / lemma: meih-t(h)-2 

Meaning: to exchange 

Material: Old Indie methati, mithati^ alternates, quarrels, joins to ', mitha-Mv. 'mutual, 

alterant, changeable, together' = Avestan mi&oMy. " inverted, incorrect '; Old Indie 

mfthus, mfthus, mithuya Mv. ds., Avestan mi&wa(na)-, mi&wara- M]. " paired, coupled'; 

gr. (sizil.) \xo\ioc, 'repayment, gratitude ' (loanword from Italic); 

Latin muto, -are ( *moitaJd) ' Of motion, to move, move away, remove. Of alteration, to 
alter, change, transform, vary, modify. Of style, to vary, change, diversify. Of substitution, 
to change, replace, make a change in. To exchange, barter, sell ', mutuus^ borrowed, lent. 
In return, in exchange, reciprocal, mutual '; 

Old Irish negative prefix mf-, mis(s)-, the full form in m/s-cu/s'\r\ate'; compare under 
Germanic missa-, here also Old Irish /77e5sa'bad'? 

Gothic ma/djan' change, falsify', /n-ma/c/Jan' transform'; Gothic ma/Pms'g\h', Old 
Icelandic PI. f. meidmar. Old English madum. Old Saxon medom^g\% preciousness, 
jewel'; participle *miPto-^ confused, confounded, incorrect ' in Gothic /77/sso 'reciprocal, 
each other, one another ', Old Icelandic (a)miss. Middle Low German to misse^ inverted, 
unfavorable'. Old High German missi^ various', prefix Gothic missa-^ wrong, incorrect ' 
{missa-deds = Modern High German Missetat, missa-leiks 'different', compare Modern 
High German miUfarben^ of different colors, varicolored, ', perhaps also Gothic missa-qiss 
'battle of words'). Old Icelandic /77/5- (seldom missi-). Old Saxon Old English mis-. Old High 
German missa-, missi-. Modern High German miss-, 

somewhat different Old High German Old English missan^ miss, feel absence, miss, 
fail'. Old Icelandic missa^ miss, lose ', Middle High German missei. 'lack'. Old English 
missn. ' loss, defeat; casualty ', Old Icelandic missirm. missai. 'loss, damage', to Old 
High German m/dan'avo\6, miss', refl. ' abstain '; intr. ' stay away, lack, hide ', Old Saxon 
mTtiian, midan ds.. Old English miidan' hide; avoid'; 

Balto-Slavic *meitu-\n Latvian mietusm. 'exchange, variation', in addition mituot and 
mietuot' exchange ', mitet^ change ', refl. 'cease'. Adv. pa-mtsu^ alternately '; 

Old Church Slavic /77//e 'alterant, changeable', russ. -Church Slavic mitusbkdv. ds., etc.; 
in addition Old Church Slavic mbstb etc. ' revenge, vengeance '. 

References: WP. II 247 f., WH. II 137, 140, Trautmann 176 f.; 
See also: see below mei-2. 



Page(s): 715 



Root / lemma: mehk- 

Meaning: to bleat (expr. root) 

Material: Old Indie makamakayate^b\ea\.s\ meka-m. ' he-goat; billy goat '; Armenian mak'/ 

'sheep'; gr. horn. priKoaGai 'grouse, bleat'; Latin miccio, -/?e 'grouse, bleat'; Middle High 

German meckatzen, mechzen. Modern High German meckern. Middle High German 

/77ec/re 'he-goat'; Lithuanian mekenu, -e/?// "grouse, bleat, stammer'; kir. /77e/r5/K 'grouse, 

bleat, bleat', etc. 

Maybe alb. /77e'goat bleat' meksh^ buffalo-calf (diminutive -sh suffix). 

References: WP. II 256, WH. II 85 f., Trautmann 177; 

See also: compare meih-6. 



Page(s): 715-716
```


## [2026-09-07T15:50:55.507Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"semita\\|sēmita\\|se-mita\" KLN_1966.txt | head -20; echo ===; grep -n \"zenith\" KLN_1966.txt | head -20; echo ===AZIMUTH; grep -n -i \"azimuth\" KLN_1966.txt | head -20",
 "description": "Klein zenith/azimuth"
}
```


### [2026-09-07T15:50:55.575Z] TOOL RESULT

```
Exit code 1
(eval):2: == not found
```


## [2026-09-07T15:50:57.018Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"mi0ra\\|mithra\\|mi&ra\" BRT.txt | head -30; echo ===MAENI; grep -n \"maeni\\|mafini\\|maini\" BRT.txt | head -20",
 "description": "Bartholomae mithra/maeni"
}
```


### [2026-09-07T15:50:57.071Z] TOOL RESULT

```
Exit code 1
20537:*)  Eine  utsche  Götterfigur,  ursptüDgticli  eine Sonnengottheit  (Oldenberq  Rel.  d.  V«da  4S,  190. HiLLEBKANDT  Ved.  Mylh.  j.  128).    In  den  ap.  In- schriften erscheint  der  Name  Äf.  erst  TattArta- xirjcfs  11.;    Darios  L    und   Xerxet  1.    erwähnen der   Gottheit   nicht,    auch   im    gAw.    wird    sie nicht  genannt.    Ich  nehme  an,  dass  M.  in  der Etrengiardäifi/rischen  Lehre    als  Gottheit    nicht anerkannt   war,    ebenso  wenig  wie    iB.  Uaoma (sd.).    Da  aber  der  Glaube  an  M.  im  Volke  lu fest  wunelte ,  waren  die  Priester  späterhin  ge- nötigt, seine  Verehrung   zuzulassen.     Bekannt- lich  hat  sich  alsdann  der  ^-Kiilt  bis  weit  ins Abendland  hinüber  verbreitet     Vgl.  WlNDlsCK- MANN  Mithra  (AKM.  /),  Dst.  ZA.  2.  441. KompA.,  E.  (in  Ableit.);  Abieil,  (s.  •ni^ray, •ml%ranya^  —  Et.  ?  Vgl  Uhlenbeck  WAiSpr. 223,  Bgm.  GrGr.3  74_>'o.    —    aL    ruiträ-   m. 1)  'Freund',    2)  ein  Adilya;  np.  Wir 'Sonne'; a.  noch  p.EN.  Mnpalinn,  fl/lr/>ayii?  USW.  —  Vgl. v^umiia:   —  Pü. :  mihr  (geschr.  ralnn  oder mlnnk);    SüErl.    lu    Y.   16%     mailripalih.     — ')   Erst    in   Inschriften    des  4.  Jahrhunderts ; 2mal    ist   w'a-V,    imal   {Am.  4)   m'>r"    ge- schrieben.    iSchr.  mit   %'r'  s.  Bthl.  BB.  9. 131,  Hbu.  KZ.  jfi.  177;    auf  die  Schreibung mit  fir^  irgend  welche  Schlüsse    aufzubauen, wie  KZ.  36.  571   geschieht,  halte  ich  für  ver- fehlt  —  »>  S.  »i'Ja  No.   3.   —  3)  Hds.  Vo.   — 4)  Zweifellos  eine  aus  arischer  Zeit  stammende Verbindung. •  j.  "miSrö.aoJah-   Adj.  'falsche   Rede führend'   oder  'den  Mfyra   betrügend"'; mi^rfm  .  .  ye^Ae  dar/jä^i  bäsava  /ra-
(eval):2: ==MAENI not found
```


## [2026-09-07T15:51:03.171Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- semita\"; grep -n \"semita\\|se-mita\" KLN_1966.txt | head -20\necho \"--- zenith\"; grep -n -i \"zenith\" KLN_1966.txt | head -20\necho \"--- azimuth\"; grep -n -i \"azimuth\" KLN_1966.txt | head -20",
 "description": "Klein zenith/azimuth grep"
}
```


### [2026-09-07T15:51:03.277Z] TOOL RESULT

```
--- semita
--- zenith
4191:azimuth,  n.,  distance  of  a  star  from  the  North  or South  point  of  the  meridian  ( astron .)  —  F.  azi- mut,  fr.  Arab.  as-sumBt,  pi.  of  as-samt,  ‘the  way’, fr.  as-,  assimilated  form  of  al-,  ‘the’,  and  saint, ‘way’.  See  zenith  and  cp.  altazimuth.
24345:E.  -oon).  Cp.  the  word  zenith,  which  owes  its form  to  a  similar  misreading.
24897:nadir,  n.,  the  point  opposite  the  zenith;  the  point directly  under  one’s  feet ;  the  lowest  point.  — ME.,  fr.  OF.  (=  F.),  fr.  Arab,  naqtr  in  the  term naqfr  assamt,  lit.  ‘(the  point)  opposite  to  the  zen¬ ith’,  fr.  ndzara,  ‘he  looked  at ;  he  considered,  ex¬ amined’,  which  is  rel.  to  Heb.  natzar,  ‘he  watch¬ ed  over,  guarded’,  Aram.-Syr.  tftar,  of  s.m., Ethi¬ op.  na}dra,  ‘he  looked  at,  observed’,  Akkad. nafaru,  ‘to  watch  over,  protect’.  Cp.  nazir. nadorite,  n.,  a  lead  chloride  and  stibnite  (mineral.) —  Named  after  Jebel  Nador  in  the  department of  Constantine  in  Algeria.  For  the  ending  see subst.  suff.  -ite. naevus,  n.  —  See  nevus.
34326:Scythian,  adj.  and  n.  —  Formed  with  suff.  -an  fr. L.  Scythia,  fr.  Gk.  SxulKix,  ‘the  country  of  the Scythians',  fr.  2x6&r(?,  ‘a  Scythian’, se-,  pref.  —  L.  se-,  a  collateral  form  of  sed-,  ‘aside, apart’,  rel.  to  the  prep,  sed,  se,  ‘without’,  and to  the  conjunction  sed,  ‘but’,  fr.  I.-E.  reflexive base  *swe-,  *se-,  whence  also  OSlav.  svg-ne, svd-ni,  ‘without’.  See  secret,  sedition,  sedulous, select,  separate,  severus,  solve.  See  also  ebriety, sober,  idio-.  See  also  zenith.  For  an  enlarged form  of  the  above  base  see  sine  and  prep, sunder.
--- azimuth
1125:aba,  n.,  a  form  of  altazimuth  instrument.  —  So called  after  its  inventor  Antoine  Thomson A'Abbadie.
2348:Derivative:  altar-ed,  adj. altazimuth,  n.,  an  instrument  for  observing  the altitude  and  azimuth  of  a  star  (astron.)  —  Com¬ pounded  of  the  abbreviation  of  altitude  and of  azimuth.
4191:azimuth,  n.,  distance  of  a  star  from  the  North  or South  point  of  the  meridian  ( astron .)  —  F.  azi- mut,  fr.  Arab.  as-sumBt,  pi.  of  as-samt,  ‘the  way’, fr.  as-,  assimilated  form  of  al-,  ‘the’,  and  saint, ‘way’.  See  zenith  and  cp.  altazimuth.
```


## [2026-09-07T15:51:08.785Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"samt\" KLN_1966.txt | head -20\necho \"--- tail file\"; wc -l KLN_1966.txt; tail -c 3000 KLN_1966.txt",
 "description": "Klein samt / tail"
}
```


### [2026-09-07T15:51:08.858Z] TOOL RESULT

```
2503:‘a  bowl  in  which  the  blood  of  victims  was caught;  membrane  round  foetus’,  rel.  to  dpaa- 8-ou,  ‘to  draw,  gather’,  dpv],  prop,  ap.ii)  (whence L.  hama),  ‘bucket’,  and  cogn.  with  Lith.  semiu, semli,  ‘to  draw’,  samtis ,  ‘scoop,  ladle’.  These words  prob.  derive  fr.  I.-E.  base  *sem~,  one, together’,  whence  also  Gk.  Spa,  ‘together  with  . See  same  and  cp.  aam.
4191:azimuth,  n.,  distance  of  a  star  from  the  North  or South  point  of  the  meridian  ( astron .)  —  F.  azi- mut,  fr.  Arab.  as-sumBt,  pi.  of  as-samt,  ‘the  way’, fr.  as-,  assimilated  form  of  al-,  ‘the’,  and  saint, ‘way’.  See  zenith  and  cp.  altazimuth.
24897:nadir,  n.,  the  point  opposite  the  zenith;  the  point directly  under  one’s  feet ;  the  lowest  point.  — ME.,  fr.  OF.  (=  F.),  fr.  Arab,  naqtr  in  the  term naqfr  assamt,  lit.  ‘(the  point)  opposite  to  the  zen¬ ith’,  fr.  ndzara,  ‘he  looked  at ;  he  considered,  ex¬ amined’,  which  is  rel.  to  Heb.  natzar,  ‘he  watch¬ ed  over,  guarded’,  Aram.-Syr.  tftar,  of  s.m., Ethi¬ op.  na}dra,  ‘he  looked  at,  observed’,  Akkad. nafaru,  ‘to  watch  over,  protect’.  Cp.  nazir. nadorite,  n.,  a  lead  chloride  and  stibnite  (mineral.) —  Named  after  Jebel  Nador  in  the  department of  Constantine  in  Algeria.  For  the  ending  see subst.  suff.  -ite. naevus,  n.  —  See  nevus.
33624:‘the  same’,  rel.  to  OE.  same,  adv.  (in  same  swa, ‘similarly’,  swa  same  swa,  ‘just  as’),  OS.  sama, samo,  OHG.  sama,  adj.  and  adv.,  Goth,  sama, adj.,  OHG.  samant,  MHG.  sament,  samt, ‘together’,  G.  samt,  ‘together  with’,  Goth. samana,  ‘together’,  OE.  samnian,  OS.  samnon, ON.  samna,  OFris.  samnia,  MLG.,  MDu. samenen,  OHG.  samanon,  MLG.,  MHG.  sa- melen,  G.  sammeln,  Du.  tamelen,  ‘to  collect’, lit.  ‘to  bring  together',  OE.  tosamne,  OS.  te- samne,  OFris.  tosamene,  Du.  tezamen,  OHG.  zi- samane,  MHG.  zesamene,  G.  zusammen, ‘together’,  fr.  I.-E.  base  *sem-,  *sm-,  ‘one, together’,  whence  also  OI.  samah,  ‘even,  level, similar,  equal,  the  same,  identical’,  Avestic hama,  ‘similar,  the  same’,  OI.  samam,  ‘together’, sa-k(t,  Avestic  ha-k^r^t,  ‘at  once,  once’,  OI.  sel¬ dom,  Avestic  ha-da,  ‘always’,  OI.  sa-,  Avestic ha-,  OI.  sam-,  Avestic  ham,  ‘with’,  Toch.  A Soma,  B.  fomo,  ‘the  same,  similar’,  B.  fe-me,  A fas,  ‘one’,  Gk.  &\io,  ‘together  with,  at  the  same time  with’,  ojjio?,  ‘one  and  the  same’,  opoio? (Old  Att.  6p.oio?),  ‘like,  resembling’,  ouou, ‘together’,  6|xaX6q,  ‘even’,  el?  (for  *ep.-?,  I-E. *sem-s),  neut.  (for  *£(*,  I--E-  *sem-),  fern, piia  (for  I.-E.  *sm-iye),  ‘one’,  L.  semel,
33671:sandiver,  n.,  glass  gall.  —  ME.  saundiver,  popular alteration  of  F.  suin  (now  spelled  suint)  de  verre, ‘sandiver’,  lit.  ‘sweating  of  glass”.  F.  suin  is  a derivative  of  suer,  ‘to  sweat,  perspire’,  fr.  L. siiddre;  see  sudation.  F.  de,  ‘of,  from’,  comes fr.  L.  de,  ‘from,  away  from’;  see  de-.  F.  verre derives  fr.  L.  vitrum,  ‘glass’;  see  vitreo-. sandix,  n.,  minion;  bright  red  color.  —  L.  sandix, sandyx,  fr.  Gk.  aavSfiE,  ‘minion,  a  women’s garment  dyed  with  this  color’,  a  Semitic  loan word.  Cp.  Akkad,  samtu,  sandu,  ‘a  red  stone’, sandwich,  n.  —  Named  after  John  Montagu, Fourth  Earl  of  Sandwich  (1718-92),  who  once spent  24  hours  at  the  gaming  table,  using  only this  kind  of  food.  —  The  title  of  the  Earl  of Sandwich  comes  fr.  OE.  Sandwic,  lit.  ‘Sand Village’.  (OE.  wic  is  a  loan  word  fr.  L.  views, ‘village,  hamlet’,  for  which  see  vicinage.) Derivative:  sandwich,  tr.  v. sandy,  adj.,  consisting  of  or  abounding  in  sand. —  ME.,  fr.  OE.  sandig,  fr.  sand.  See  sand  and  -y (representing  OE.  -ig).
34995:shirt,  n.  —  ME.  schirte,  shirte,  sherte,  fr.  OE. scyrte,  ‘skirt,  tunic’,  rel.  to  ON.  skyrta,  Dan. skjorte,  Swed.  skjorta,  ‘shirt,  kirtle’,  MDu. scone,  Du.  schort,  ‘apron’,  MHG.  schurz,  G. Schurz,  Schiirze,  ‘apron’  (whence  schiirzen,  ‘to tuck  up’).  The  original  meaning  of  these  nouns was  ‘a  short  garment',  fr.  OE.  scort,  ‘short’,  resp. its  equivalents  in  the  other  Teut.  languages.  See short  and  cp.  skirt,  which  is  a  doublet  of  shirt. shirty,  adj.,  irritable.  —  Formed  fr.  the  phrase  ‘to have  one’s  shirt  out’.  See  shirt  and  adj.  suff.  -y (representing  ME.  -/,  -y,  - ie ). shittah,  n.,  shittah  tree,  the  tree  of  whose  wood the  Ark  and  the  altars,  tables,  and  bars  of  the Tabernacle  were  made  ( Acacia  nilotica ).  —  Heb. shittdb  (pi.  shittim),  for  *shinta,  prob.  fr.  Egypt. sh-n-f-l  (Late  Egypt,  shonte),  whence  also  Ak¬ kad.  samtu,  Arab,  sant,  ‘acacia’.
--- tail file
41262 KLN_1966.txt
��  Lit.  ‘neigh¬ borhood’,  fr.  ML.  vicinetum,  fr.  L.  vicinus, ‘neighboring,  near’,  fr.  views,  ‘district’;  see vicinage.  Venue  in  this  sense  was  influenced  in form  by  venue,  ‘arrival’.
venule,  n.,  a  small  vein.  —  L.  venttla,  formed  fr.
vena  with  dimin.  suff.  -i da.  See  vein  and  -ule. Venus,  n.  —  L.  Venus,  gen.  Veneris,  ‘the  goddess of  love’.,  fr.  venus,  ‘love,  sexual  desire,  loveliness, attractiveness,  beauty,  charm’,  whence  venerari, ‘to  reverence,  worship,  venerate’.  See  venerate, vera,  n.,  name  of  a  tree,  Bu/nesia  arborea.  —  Am. Sp.,  fr.  Sp.  vera,  ‘border’,  which  derives  fr.  L. ora,  ‘border’  (through  the  intermediate  form *uera\  cp.  Sp.  hueso,  ‘bone’  (fr.  L.  ossum).  L. ora  (for  *osa)  is  a  collective  noun  formed  fr.  os, gen.  -oris,  ‘mouth,  opening,  entrance’.  See  oral, veracious,  adj.,  truthful,  true.  —  Formed  with suff.  -ous  fr.  L.  verax,  gen.  veracis,  ‘truthful, speaking  truly",  fr.  verus.  See  very.
Derivatives:  veracious-ly,  adj.,  veracious-ness,  n. veracity,  n.,  truthfulness,  truth.  —  F.  veracite,  fr. ML.  veracitdtem,  acc.  of  veracitas,  ‘truthfulness’, fr.  L.  verax,  gen.  -acis.  See  prec.  word  and  -ity. veranda,  verandah,  n.  —  Port,  varanda,  ‘balcony’, introduced  into  English  from  India.  Port,  ra- randa  itself  is  of  uncertain  origin.  F.  veranda was  borrowed  from  English.
Derivative:  veranda(h)-ed,  adj. verano,  n.,  the  dry  season  in  tropical  America.  — Sp.,  fr.  L.  ver,  ‘spring’.  See  vernal.
Verbesina
verascope,  n.,  a  small  stereoscopic  camera.  —  A hybrid  coined  fr.  L.  verus,  ���true’,  and  Gk. ruov,  fr.  mtoraiv,  ‘to  look  at,  examine’.  See very  and  -scope.  The  correct  form  would  be alethoscope  (fr.  Gk.  dcXvjffrji;,  ‘true’  and  -rsy.6- mov ) .
veratral,  n.,  the  radical  C9H10O4  (chem.)  —  Form¬ ed  with  adj.  suff.  -al  fr.  L.  verdtrum,  'hellebore’. See  veratrine.
veratric,  adj.,  pertaining  to  a  white  crystalline acid. —  Formed  with  adj.  suff.  -ic  fr.  L.  verdtrum, ‘hellebore’  (see  veratrine) ;  so  called  because  it  is easily  obtained  by  the  decomposition  of  vera¬ trine.  \
veratridine,  also  veratridin,  n.,  an  amorphous  al¬ kaloid  obtained  from  sabadilla  seeds, C36H61OnN  (chem.)  —  Coined  fr.  L.  verdtrum, ‘hellebore’  (see  next  word),  and  the  chem. suffixes  -ide  and  -ine  (resp.  -in), veratrine,  n.,  also  veratrin,  veratrina,  veratria,  a poisonous  mixture  of  alkaloids  obtained  from sabadilla  seeds,  used  in  medicine  in  the  treat¬ ment  of  rheumatism,  neuralgia,  etc.  —  F.  vera¬ trine,  fr.  ModL.  veratrina,  fr.  L.  verdtrum,  ‘helle¬ bore’,  fr.  verare ,  ‘to  tell  the  truth’,  fr.  verus, ‘true’;  so  called  because
```


## [2026-09-07T15:51:13.019Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- 1971 zenith\"; grep -n -i \"zenith\" KLN_1971.txt | head -10\necho \"--- 1971 semita\"; grep -n -i \"semita\" KLN_1971.txt | head -10",
 "description": "Klein 1971 zenith"
}
```


### [2026-09-07T15:51:13.089Z] TOOL RESULT

```
--- 1971 zenith
24325:‘way’. See zenith and cp. altazimuth, 
154562:E. -oon). Cp. the word zenith , which owes its 
158213:nadir, n., the point opposite the zenith; the point 
216242:sober, idio-. See also zenith. For an enlarged 
270434:zenith, n., 1) celestial point vertically over th’e ob- 
270436:point. — Late ME., fr. OF. cenit(h) (F. zenith ), 
270446:Derivative: zenith-al, adj. 
--- 1971 semita
217609:Semite, n. — ModL. Semita , fr. Late L. Sem, fr. 
270442:n<. Cp. azimuth. L. semita prob. stands for *se-
```


## [2026-09-07T15:51:15.329Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '270430,270450p' KLN_1971.txt",
 "description": "Klein zenith entry"
}
```


### [2026-09-07T15:51:15.400Z] TOOL RESULT

```
Zend-Avesta, n., the sacred books of the Parsees. 
— Pers. Avistak va Zend, lit. ‘text and commen- 
tary’. See Zend and Avesta. 
zenith, n., 1) celestial point vertically over th’e ob- 
server; the opposite of nadir; 2) the highest 
point. — Late ME., fr. OF. cenit(h) (F. zenith ), 
fr. Sp. cenit , fr. VArab. semt, corresponding to 
Classical Arab, samt , ‘way, path’ (abbreviation 
of samt-ar-rd' s, ‘way over the head’), fr. L. se- 
-mita, ‘path, way’. VArab. semt became senit, 
zenit , owing to a misreading of the letter m as 
n<. Cp. azimuth. L. semita prob. stands for *se- 
-mita, fr. sed-, se, ‘aside’, and *mita, fr. meare , 
‘to go’. See se- and meatus. 

Derivative: zenith-al, adj. 

Zenobia, n., fem. PN. — L. Zenobia, fr. Gk. 
Zi)vo(3ia, lit. ‘force of Zeus’, compounded of 
Z 7)v, a collateral form of Zeus, ‘Zeus’ (see Zeus
```


## [2026-09-07T15:51:27.404Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- KLN1971 Mithras\"; grep -n -i \"mithras\\|Mithra,\" KLN_1971.txt | head -10\necho \"--- KNT mithra\"; grep -n -i \"mithra\\|Mi0ra\" KNT.txt | head -20",
 "description": "Klein Mithras, Kent Mithra"
}
```


### [2026-09-07T15:51:27.466Z] TOOL RESULT

```
--- KLN1971 Mithras
152790:connected with Avestic Mipra see Mithras. 
152792:Mithraism, n., the worship of Mithras. — See 
152795:Mithras, n., the Persian god of light. — L., fr. 
152872:corresponding to the Persian Mithras. — OI. 
152884:Cp. Mithras. 
--- KNT mithra
3138:Another use of the nominative аз genitive 18 seen in Аа 4 [vasnà : АМ: Analhtta |: ціа : [M @то, ‘by the favor of Ahuramazda, Anaitis, and Mithras’ (so also in A?Ha, restored), where the occurrence of the same forms as nominatives in lines 4f sets а model; though the position of the gaps makes it possible to restore the genitive end- ings in Аа, their insertion would make the line unduly long.
4694:TRANSLATION оғ А9: Saith Artaxerxes the Great King, King of Kings, King of Countries, King in this earth, son of Darius the King, of Darius (who was) son of Artaxerxes the King, of Artaxerxes (who was) son of Xerxes the King, of Xerxes (who was) son of Darius the King, of Darius (who was) son of Hystaspes, an Achaemen- ian: This palace Darius my great-great-grand- father built; later under Artaxerxes my grand- father it was burned; by the favor of Ahuramazda, Anaitis, and Mithras, this palace I built. May Ahuramazda, Anaitis, and Mithras protect me from all evil, and that which I have built may they not shatter nor harm.
4704:3 vasnd : AMhà : imam : hadis : tya : j'vadiy : paradayadàm : adam : akunavam : AM : Anah 4 ita : uta : Mitra : mam : pàtuv : hacd : vispà : gastà : utamaiy : kartam Nores то À'Sd: Text according to the line-divisions of copy da. ‘af... de; ahydya db; ahyd de. ? Hazámanikiya db; Harémaniya da, de. 3 akul... da; аштайт db; akuvanašāša de. *hacá da; lost in db; ha Xà de. * vispá da, de; »*dspa db. * gástà da, db; gastü dc. * uta... da; utamaty db; ufamay de. TRANSLATION ОЕ А284: 61. 1-2. ... (= A’Sa 1), an Achaemenian. $2. 2-4. Saith Artaxerxes the King: By the favor of Ahuramazda this is the palace which T built in my lifetime as a pleasant retreat. May Ahuramazda, Anaitis, and Mithras protect me from all evil, and my building.
4712:TRANSLATION oF Á?Hb: This palace, of stone in its column(s), Artaxerxes the Great King built, the son of Darius the King, an Áchaemenian. May Mithras protect me ...
4752:$4. 23-6. Saith Artaxerxes the King: Me may Ahuramazda and the god Mithras protect, and this country, and what was built by me.
5720:Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
5721:‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
5798:Mié6ra- sb. ‘friend’; as deity, ‘Mithras’: El. т1-14-5а, Akk. mi-i-ri; Av. mibra-, NPers. mihr ‘sun’, Skt. mitrd- ‘friend’ (§9.VI, $33, §49c, $78, 5148.11). Cf. Vaumisa- and probably hamigzya-. Міга} nsm. АНЬ; Mitra (822) A’Sd 4, A?Ha 6; Ма А?а 5, А?Ра 25. Аз gen. ($818.П), M'tra A?Ha 5°, M‘éra A’Sa 4.
```


## [2026-09-07T15:51:29.663Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- PHD mihr\"; grep -n \"mihr\" PHD.txt PHD_mackenzie.txt | head -20\necho \"--- NYB mihr\"; grep -n \"mihr\\|Mihr\" NYB_vol2_glossary.txt | head -15\necho \"--- HRN mihr\"; grep -n -i \"mihr\\|mit̲hra\" HRN.txt | head -15\necho \"--- HUB\"; grep -n -i \"mihr\" HUB.txt | head -15",
 "description": "Pahlavi/Persian mihr"
}
```


### [2026-09-07T15:51:29.752Z] TOOL RESULT

```
--- PHD mihr
PHD.txt:128:delete mezidan ... suck. for ?mēzišn ... read ! meziin ... for mistan, *mēz- read... *mēz-.. mihoxt [mytwht' = Av. midaoxta-| falsehood. *mihr .. add ~ druxtan : break faith. add mizīdan, miz- [myc-ytn' | N mazidan] suck. for *moy-mard ... read mowmard ... mēy ... add M mwy. read nüxun [n^hwn' | P nxwn, N nàxun] (finger) nail. delete nāyīzag ... (read wezag). nek, ~th ... add benefit. nibastan ... delete SKBHWN-tn' < A Vškb; nibastan ... read M nb’st, P nb’y-. nibeg ... add M nbyg. nibištan ... |YKTYBWN-tn'... (not -stn'). nidan, nay- |DB(Y)LWN-tn' < A Ydbr |... nigün, ~sar |-s 1 | (P ngws’r)| downwards. add *nihēb |nyhyp | N ~] fear, terror. for nīšān read nišān...
PHD.txt:292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
PHD.txt:491:méx [myh | P myx, N ~] peg, nail. ~ ī gàh: astr. Polaris, pole star. 1-3méz-, v. mézidan, mëzišn, mistan. mēzd [my()zd | № тёз] offering, meal. „bān [-p’n' | N ~] host. mézidan, 'méz- [myc-ytn!] suck. *mézisn [myckn'] blinking, twinkling. mih [mt!] false, contrary, opposite. mihēxt [mytwht!] falsehood. imihr [mtr! | M myhr, N —] Mithra; sun; cal. 7th month; 16th day. tmihr [mtr!, etc.] contract, bond. šmihr [mtr!, etc.] love, friendship. mihrbān [mtr'p?n! | Р myhrb’n, N ~] friendly, kind. mihr-dróz [mtr'dhwc] = mihródruj. mihródruj [mtr?w-, mtrwk-diwe = Av. mitlyo.drujim] contract-breaker. ~th: breaking faith. mihr-zan [mtr'zn'] = mihródruj. mij(ag) [myc(k') | N muz(a)] eyelid; eyelash. mijüg (myc-, myšwk! | IN mizü] lentil. mir-, v. murdan. mistan, 3mëz- [mstn', myc- | N mézidan] urinate. -i$n(ih): urination. mizag [m(y)ck! | N maza] taste. ~darih [-d’lyh] (sense of) taste. ~ӧтапа [отпа] tasty. mizd [m(y)zd | N muzd] reward, hire, pay. ~war [-wbl | N -àr] hireling. *mizné [m(y)znydy] mist, dew. mög [mwk!] shoe. 5 *moy-mard [mgw-mit', -gGBRA | N muy) magus. mör [mwl | N <) ant. mórd [mwlt! | N ~] myrtle. morwārīd [mwlw'lyt! | M mwrwryd, N ~] pearl. *mowbed [mgwpt' | N móbad] Mazdean priest. móy [mwd | N ~] hair. móya$ [mwdk' | N méya] lamentation. móyen [mwdyn'] (made of) hair. moz [mwe | N ~] banana. mózag [mzvck! | N тоха] shoe. *mūdag [mwtk'} spoilt, destroyed. muy [DKRA < А dgP | N mux] date-palm. muhr [muwdl | M mwhr, N ~] seal. Сар [mwhlk! | P mwhrg, N ~a] bead, vertebra, piece (in backgammon, etc.). *muhrišn [*mwtl$n!] excrement. mulān [mwi?n'] belly (daevic).
PHD.txt:1042:bond band; mihr, pašn, ра& (ар).
PHD.txt:1079:breaking šken(n)išn; ~ faith mihrē- drujīb.
PHD.txt:1379:contract mihr.
PHD.txt:1380:contract-breaker mihrdrēz, druj.
PHD.txt:1425:mihrē-
PHD.txt:1868:faith kēš, xwastügih; breaking ~ mihródrujih.
PHD.txt:1948:fire adur, ātaxš; form of ~ āsrēkerpa; sacred ~ ádarog, Burzénmihr, Farrobág, Gušnasp, ātaxš i Wah- ram.
PHD.txt:2046:friendly ayàrómand, mihrbān.
PHD.txt:2047:friendship ayürih, dēstih, ērmānīh, mihr.
PHD.txt:2524:Rind (a.) mihrbàn.
PHD.txt:2678:love (n.) dóstih, dēšagīh, dēšāram, mihr.
PHD.txt:3889:sun mihr, xwar.
PHD.txt:4823:[140] mastog 19112256 mehtar Vess mastarg > e26 mizagūmand 2061” 406 mizagdārīh AAS 3G mizag 1.5 0G rūynī NINE maškabarzēn NS ey wi? makkizag 1923 556 1-2mašk way deh! ATES dehgiin! uses madār У. о mih мес madan, 1-3mihr мео
PHD.txt:4825:mihrodrufih эс » (el
PHD.txt:4826:mihrodruj
PHD.txt:4827:mihrdrūz ay vives mihrzan To иес mihródruj ay stec mihrēdrujīh ` ^45 ay Auree mihrbān wo vue
PHD_mackenzie.txt:1683:Burzenmihr [bwlcynmtr ] the third major Fire of Sasanian Eran, that
--- NYB mihr
463:Anēšē-zātān [/nw&yc?t?n'] patr. of Anošč- zat, the father (or ancestor) of Mihrak 1322, 1525. — From anos = anēšak + zat (q. v.) ‘Immortal-born’; as to the ending -ë in the composition cf s.v. mēnēt.
763:ütur ['twr'; inser. ’twry] fire, referring to the old Iranian fire cult: ~ yazét god Ātur 25?; ~ farröbäg, gušnasp u burzen mihr the names of the three sacred fires connected with the three classes of the old Iranian society 118, explained 27-9; ~ farröbäg, i -bag 974. 9511; ~ gusnasp 955; ~burzén mihr 95%; ~-dn šāh the head of the sacred fires 1222-23, 131; — sal 58, āturv i Artaxšahr säl 40, āturv Šahpuhr i āturān šāh sal 24 SPrs:1-3 = sar 58, ātarē Artaxéahr sar 40, ātarē Šāhēpuhr ātarūn xšāh sār 24 SPrth:1-3: ‘... of the year 58 (viz.) the year 40 (of =) after the (enthronement) fire of Artax- Sahr, the year 24 (of =) after the (en- thronement) fire of Sahpuhr, the head of the fires’, which means the year 266 A.D., v. Christensen apud Ghirshman, Rev. des arts asiatiques X, 1936, 127—128 (the year 40 reckoned from the coronation of A. in the year 226, the year 24 reckoned from the coronation of S. in the year 242, and the year 58 reckoned from what must have been the epochal year of Sassanid time-reckoning, viz. 208 A. D.). — [~ the name of the 9th day of the month, also of the 9th month of the year; dade (q.v.) pat — the name of the 8th day of the month: FrP 28.] — Av. v.s. v. ätaxs; Prth ätarö (g. v.); MPrthPrs ’dwr; Paz. ädur; NP āčar, ādar. As to the three sacred fires v. Christensen, Sass. 164— 167; cf also de Menasee, Feux (1964); Mary Boyce, BSOAS XXXI, 1968, 52- 68, 270-289.
1049:burzčn [~-yn'] in ätur ~ Mihr, the name of the third of the three great imperial
1151:dadv [ddw'] the name of the tenth month of the year 9715; ~ pat Mihr the name of the 15th day of the month 9715-16, - Av. (678 sq.) dadvah- ‘the Creator’;
1369:druž [dlwc'] all that is false, untrue, wrong, deceptive: 1. the world of Guile and Untruth, conceived as a personal cosmic power, 3822, 9313. — 2. individual manifestations of this power, demons, conceived as feminine supernatural be- ings: sg. 5716-25, 583. 9620-24, 9817-19, 101% (voc.). 1023-14; ~ ; anāštēh 671; ^ 4 spazgeh 6811-12; ~ 7 ahramög 10124-25; pl. cas. rect. ~ 648. 65*. 9721, 9819 (of human beings). 10224-27, 1033; pl cas. obl. —-än in the set phrase devün u ~-dn 75" ete. (voc. 9027). V. also mthr-druz, mihrčin-druž. — Av. (778 sqq.) drug-, nom. druxš, gen. drüjö; MPrs drwaš (S); Paz. drü£.
1370:druzéh falsity, unrighteousness 66°; a troop, band of fiendish beings 986%, V. also mihrdin-družčh.
1754:expressed (nominal sentence as in the Semitic languages): man Sähpuhr hom 154; tē ke he? 737; to rād ke Dugdav he 4721. en rētak ke hast? who is this boy? 1617; Artaxsér ... nē pat giyāk hast 6?" sq.; kë zan-& hac õi hucihrtar nest ‘qua pulchrior non est mulier', who is the most beautiful of all women 259-19; ēzšān amüh hem ke ... we are of those who 5723-24, šmāh ke xtēn het 6111; sagr hend 86%, — 3. in the 3d p., together with a subst. virtually in dat., or with a pron. in cas. obl., it expresses ‘to possess’ xdnak i-t hast the house that belongs to thee 5325-26; fradandan i-5 hast the chil- dren he has 142; with ràd as in NP: Papak rüd pus-é hast 3?. — 4. Together with verbal or other nouns it forms periphrastic verbal expressions, e. g. han- dešitar vicītār hom 125; frēftār hah 3419; matür hom 46’; kartar hom 101?’; brihenäk hend 7777; ke (cas. obl.) vitīrišn nest which is incorruptible 66°; tö hän-ic äkäh he this thou knowest 399; hayyär hend they help 106%; -š hayyaréh hénd they help him 1001-12; pat kamēstārēh + spihr hénd they offer resistance to the. Sphere 8721; ké (cas. obl.) Mihr u Mah pat pust hah which M. and M. protect 317-8, ete. — 5. auxiliary vb. forming compound tenses: būt hom, būt hend I was, they were, eto., v. Grammar; notice: HWH-nd, regularly hend, must stand for the subju. händ 14? (fut.). 335 (cond.). — 6. Wrong use of the ideogr. HWH-: a) HWH-wm for the encl. pron. lst p. sg., added to the pret. pass. in order to emphasize the agent-
1839:hama- (v. ham), cf harvist, — 2. A secon- dary enlargement of MPrs hmys = hamis ‘together with’ (A-H II) or ?c ... hmys (S), < OP *hamica- (hamiciya- ‘rebellious, rebel’), NW *hami@ra-, *-riya-, whence MPrth (BBB) hmyr < *hamihr "in all, all told’. Pagliaro, RSO XIX, 1941, 283 sq., Jackson Vol., 1954, 102-110; Nyberg, Unvala Vol, 1964, 102 sq.
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
2120:*jānakān [HY°-k’n'!] designed for the soul, "place of the soul of a deceased, a sepulchre: Sugud, 1 haft ~ andar but, api-š haft-jänakäneh ēt kū haft x“ataidan andar but Sogdiana, in which seven *soul-places" existed; and its possession of “seven soul-places" is explained by the fact that seven royal tombs (v.s. v. axvatātdān) existed there 1131-14: those of Yam, of Frētēn, of Manūcihr, of Käyös of Kai-Xösröi, of Luhräsp, and of King Vištasp (ll. 15-17; Az Dahāk is a spurious addition). — The reading ET Y?-k?n-handed down by such a careful and competent scribe as Mihrapan should never have been doubted; Jamasp Asana’s ''emen- dations” haft (hwt’d’n =) xtatdydn, haft (hwt’d’nyh =) xatdydnéh (a horrid form!) are sheer corruptions. Mihrapan must be taken seriously. Certainly the idea of a place for the jan is absolutely contrary to the Iranian way of thinking,
2232:2kartak 1. juridical term, according to Pagliaro, RSO XXIII, 1948, 52-68, for- mal, strict law; legal proceedings, cause in court: pat ~ dästan to keep the Law, 6 ~ kartan to bring to court, to prosecute, ~ bavēt ógón apāk ku ... it is accom- panied by a formal declaration to the purport that ..., ete. [add GF IV, 20 (Ahriman speaks to the unsuccessful sorcerer): šav u gartan peš kun mihrdru- Z&h rüd (thus the two Copenh. MSS) ka ~ dārēt be off and turn thy nape forwards (i. e., run backwards, cf 6811-12) because of thy treachery measured by strict law (properly: when one keeps the law)]; this sense probably also in the difficult passage 2617-18 (an alleged order of Viš- täsp’s): han asp ka Zarér kartak bit be 6 Bastvar dahet this horse, since for Z. a legally valid declaration was made (that it should be owned by him), give it to B.!, i.e., give B. this (such and such) horse which is his because it is Z.'s legal pro- perty. — 2. in a religious sense: canonical text 11123; cf Dēn-kart. — From ?kartan.
2277:ke [MNW] with encl. MNW-m = ké-m, MNW- = kē-š ete.; MNW-c = ké-c: A. interrog. pron. who? whom ?: én rētak kē hast? 161”; emphasized kē hàn he? who art thou, say? 561%; as cas. obl.: kē pat panāh kunom? 749; ke ax"eš hom? to whom do I belong? 624; én zanišn ké (ag.) kart? who made this deadly shot? 323; — gen. + ke: En pus + kē hast? whose son is this? 1621; or hàn 4 ke: ruvan... hàn t kē...? whose soul? 31?3; — governed by a prep.: hac ke? nazd ke? tài ke? ete. ; — indirect interrogation may be introduced by ku: gob ku to hac fradandän i ke hah 1517-18; without kū: (én-ic dine) hac pusa- ran...ı man ke zīvēt u kë mīrēt 219-19; nē (Gkah hom) i ke hàn 574. — B. rel. pron. who, which ; with pronominal antecedents : man ke, tē ke, šmāh ke, či ke, čišan ke, -$...ke, han (kas) ke, har (hàn) ke; hec (kas) ke both in a positive (6417-18) and a negative (11817-18) sense; 1. used as cas. rect. and cas. obl: (subj.) asvdr-é nest ke ... ētūn cigon to 1519-316; (dat.) (Kävul) ke Mihr u Mah pat pušt hah K. over which Sun and Moon keep guard 317%; (agens) Krisäsp ke Dahāk vanit K. by whom D. was vanquished 1064-5; — its syntactic function may be marked by an enclitic referring to the antecedent: (hu- nušk + Gana Menoi) kē-š ciš-ic pat poc nest (the progeny of the Evil Spirit) for whom there is nothing to furnish an ex- cuse 1021-?; but dastavar ké-§ guft ku there was a theologian who said 1018, also but ké-§ guft ki someone has said (taught) that 103? ; Gišān kē-šān Yam kirrenit those by whom Y. was cut to pieces 10145; — the gen. is regularly ex-
2343:*kurtīk, pl. cas. obl. kurtīkān [kwltykn!'] villeins, slaves or bondmen employed in different occupations on, an estate: ~ šu- pānān slave shepherds 1°. — I follow the reading of Antiä, whose text reproduces the basic MS of Kn, that of Mihrapan (v. I, p. XII). S. has kurtān ‘Kurds’ (ef kurtān šāh KnS V, 1). Itis of course pos- sible that ~ is ultimately derived from the national name of the Kurds, who were notorius nomad  cattle-breeders (BQ notices kurd in the sense, inter alia, of cūpān(ān) and gēsjand-carān) but it cannot have an ethnie sense here. The narration presupposes that Sasan was a slave within easy reach of Papak, to be summoned. into his presence at any mo-
2377:mah [m’h; BYRH, Prth. YRH?’] 1. the moon, regularly written m’h, 7’. 2025 ete. passim, but BYRH 31” (as a deity). — 2. month, regularly written BYRH, SPrs: 1. P1:1.P2:1. 1929. 2081" ete. passim; Prth YRH? ŠPrth 1. — Common Iranian. The names of the months in Phi are: 1. Fravartin. 2. Urt-vahist (Art- q.v.). 3. Harvadat. 4. Tir. 5. Amurdat. 6. Sahrévar. 7. Mihr. 8. Āpān. 9. Atur. 10. Dadv. 11. Vahuman. 12. Spandarmat.
2381:Mahlāh/Mahlāi [m’hl’s 9522, m’hl’y 96°] and Mahliyānāh [m’hlyd’n’h 95”. 965]; Malhà and Malhiyánài [mlh’ — mlhy?n?y] 951? gl.; Mihréh and Mihriyānēh [mtr'yh — mtr'yd’nyh] 634; Misēh [msyh — no fem.] 471: the first human couple, which arose from the sperm which Gäyömart, the Primeval Man, left on the soil when he was killed by Ahriman. — A great variety of forms: A. 1. Mahlé — Mah- liyānē [mhlyd — mhly’nyd] BdA p. 101°; Arab mhl’ — mhlynh (Mas‘üdi, Tanbih 93); — 2. with metathesis of -hl- > th-: *Malhēh — *Malhānā [mlhyh — mlh’n’] DD ch. 36%; Arab mlhy — mih’ny (Birüni, Chron. 99); of this type is prob- ably also Mari - Māryānah Tab. I. 147;— 3. with -$- instead of -Al-, -Ih-, and lengthening of the preceding a: Mašik — Māšyānē [m?$yk — m'šy'nyd] BdA p. 101!5 sq., *Māšīk - *Māšyānīk ibd. p. 1054; Tab. also m’®#. — B. Mihréh - Mihriyäneh, BdJ 33° Mihr [mtr'] - Mihriyän [mtr'y’n] (in other places Maše — Māšēnē): 1. with -s- for -hr-: Misäi — Mišiyānē [mšy — mšyd'ny] BdA y. 10514-15, Miša ibd. 1059. 1072; mšyh — máyd'wy DD ch. 69. 76 = Cod. K 35
--- HRN mihr
465:äb[mendy Röd]äbe, Suhr]ab^ Mihr\äb^ Ardä VTr\af, af[täb,
8696:1000. mihr *Sonne; Liebe', mihr[ban 'freundlich, wohl-
10082:ger bemihr-i tu myerdäned ztmüne ^) rayträi
11018:ger hude yär-t mihr%än bä men
--- HUB
2533:= Mihrdat (arm. Mihrdat) = ap. *Mi^radata- =
4270:') Beaohte das unten angefiihrte Mllad aus phi. Mihrdat. Da
4272:vorsassanidisohes Mihrdat (nicht *MihridcU oder *Mihradat) voraus,
4301:n, 31) aus "^Mihrddt = arm. Mihrdat, lat. Meherdates, gr.
4622:Vgl. Milad aus Mihrdat § 3.
4798:= Mihrdaty siehe § 3 und 9; hujtr, huzlr, xujir 'schdn,
5207:p. 92), haufig in Personennamen wie Atrvsnasp, Mihrvsnasp
7154:u. 8 w., § 92, b), letzteres da, wo spater d erscheint, yg\. arm. Mihrdat^
7273:mihr 'Sonne, Liebe, paz. mihir Sonne*, N. pr. Mihir-ayar
7275:*Mi9^r, spater Mihr), arm. Mihr, das auch in den Ab-,
7276:leitungen mrhakan (Agath.), mihrakan (Mos. Kalank.)
7277:und in vielen Namen vorliegt: Mihr-Nerseh (Elise), Mihr-
7279:Sapuh, Mihr-Vsnasp'^) (Laz. Pharp.), Merhevandak (Se-
7281:Laz. Pharp.) = Merhnzan, Meruian, Mehuzan; Zarmihr-)
7282:(Laz. Pharp.) ^i= p. Zarmihr Tab. 135; Mihrdat (Pseu-
```


## [2026-09-07T15:51:41.344Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '152788,152800p' KLN_1971.txt\necho \"--- 1966 Mithras\"; grep -n -i \"mithras\" KLN_1966.txt | head",
 "description": "Klein Mithras entry"
}
```


### [2026-09-07T15:51:41.425Z] TOOL RESULT

```
fr. L. mitra, ‘cap, turban’, fr. Gk. [xhrpa, ‘belt, 
headband, turban’, which is prob. a loan word 
connected with Avestic Mipra see Mithras. 
Derivatives: mitr-al, adj., mitrate (q.v.). 
Mithraism, n., the worship of Mithras. — See 
next word and -ism. 

Mithras, n., the Persian god of light. — L., fr. 
Gk. Mi&pa?, fr. Avestic Mipra-, which is rel. 
to OI. Mitrdh. See Mitra and cp. next word, 
mithridate, n., an antidote against poison. — 
ML. mithriddtum, fr. Late L. mithridatium, 
prop. neut. of Mithridatius, ‘pertaining to Mith- 
--- 1966 Mithras
24058:mite,  n.,  a  small  arachnid.  —  ME.,  fr.  OE.  mite, rel.  to  MDu.  mite,  Du.  mijt,  OHG.  Dan. mide,  Norw.  mit,  ‘mite’,  and  prob.  also  to  ON. meita,  etc.,  ‘to  cut’.  See  ant. mite,  n.,  a  very  small  coin.  —  ME.  mite,  fr.  MDu. mite,  ‘a  small  coin’,  which  is  identical  with MDu.  mite,  ‘a  small  arachnid’.  See  prec.  word. Cp.  F.  mite,  ‘mite’  (in  both  senses  of  this  word), which  is  a  MDu.  loan  word.  Cp.  also  mitraille. Mitella,  n.,  a  genus  of  plants,  the  miterwort  (bot.) —  L.  mitella,  ‘headband,  turban’,  dimin.  of mitra  (see  next  word  and  -ella);  so  called  in allusion  to  the  shape  of  the  young  pod. miter,  mitre,  n.,  head  dress,  turban.  —  F.  mitre, fr.  L.  mitra,  ‘cap,  turban’,  fr.  Gk.  jxlrpa,  ‘belt, headband,  turban’,  which  is  prob.  a  loan  .word connected  with  Avestic  Mipra -;  see  Mithras. Derivatives:  mitr-al,  adj.,  mitrate  (q.v.). Mithraism,  n.,  the  worship  of  Mithras.  —  See next  word  and  -ism.
24059:Mithras,  n.,  the  Persian  god  of  light.  —  L.,  fr. Gk.  M 10-pa?,  fr.  Avestic  Mipra-,  which  is  rel. to  OI.  Mitrah.  See  Mitra  and  cp.  next  word, mithridate,  n.,  an  antidote  against  poison.  — ML.  mithriddtum,  fr.  Late  L.  mithridatium, prop.  neut.  of  Mithridatius,  ‘pertaining  to  Mith- ridates’,  fr.  L.  Xfithridates,  fr.  Gk.  MifiptSarv)?; so  called  in  allusion  to  Mithridates,  King  of Pontus,  who  made  himself  poison-proof. Derivatives :  mithridat-ism,  n.,  mithridat-ize,  tr.  v. mitigate,  tr.  v.,  to  alleviate.  —  ME.  mitigaten,  fr. L.  mitigatus,  pp.  of  mitigare,  ‘to  make  soft  or tender,  to  soothe,  mitigate’,  compounded  of mit  is,  ‘soft,  mild,  gentle’,  and  agere,  ‘to  set  in motion,  drive,  lead;  to  do,  act’.  The  first  ele¬ ment  prob.  stands  for  *mi-tis  and  derives  fr, I.-E.  base  *mei-,  *mi-,  ‘soft, mild,  tender,  gentle; peaceful,  lovely',  whence  also  OIr.  moith,  Mir. moeth,  Ir.  maoth,  ‘soft’.  Cp.  also — with  -/-forma¬ tive  element — OSlav.  milu,  ‘charitable’,  Russ. milyj,  Pol.  mily,  Czech  and  Slovak  mily,  Lith. mielas,  mylas,  ‘beloved,  dear’,  Lith.  myliu, myleti,  ‘to  love’,  Lett,  mil's,  OPruss.  mijls,  ‘be¬ loved,  dear’,  Russ,  milovat’,  ‘to  show  mercy’, Pol.  milovac,  Czech  milovati,  Slovak  milovat', etc.,  ‘to  love’,  Russ,  mllost',  ‘mercy’,  Czech milost,  Slovak  milost',  ‘love,  mercy’.  Cp. — with  -r-formalive  element — Alb.  mire,  ‘good’, OSlav.  miru,  Pol.  mir,  Czech  mir,  Slovak  mier, ‘peace’,  Russ,  mir,  ‘peace,  world,  community’; with  -/(-formative  element :  Ir.  min,  ‘soft,  smooth, fine’,  W.  main,  ‘slender,  slim’,  mwyn,  ‘soft, kind’,  OCo.  muin,  moin,  ‘soft,  tender’.  OI. mayah,  ‘enjoyment,  pleasure’,  and  Toch.  B maiwe,  ‘little,  subtle',  prob.  also  derive  fr.  I.-E. base  *mei-,  *mi-.  Cp.  mir  and  the  second  ele¬ ment  in  Casimir.  For  the  second  element  in  L. mitigare  see  agent,  adj.,  and  cp.  words  there referred  to.
24067:Mitra,  n.,  a  Vedic  deity  associated  with  Varuna, corresponding  to  the  Persian  Mithras.  —  OI. Mitrah,  prob.  personification  of  mitram,  ‘con¬ tract,  agreement’,  hence  lit.  meaning  ‘partner  to a  contract’ ;  rel.  to  Avestic  and  OPers.  Mipra-, ‘Mithra’,  mipra-,  ‘contract,  agreement’.  These words  are  prob.  rel.  to  OI.  minoti,  ‘fastens, erects,  builds’.  For  the  connection  of  meaning betw'een  ‘to  fasten’,  and  ‘to  make  a  contract’, cp.  L.  pang  ere,  ‘to  make  firm’,  which  is  rel.  to pacisci,  ‘to  make  a  treaty’,  pax,  ‘peace’  (see pact );  see  Mayrhofer,  A  Concise  Etymological Sanskrit  Dictionary,  II,  pp.  33-34  s.v.  Mitrah. Cp.  Mithras.
```


## [2026-09-07T15:51:43.028Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} /Mi.6ra- sb\\./ {print NR; exit}' KNT.txt\necho \"--- count leaves\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' KNT.txt",
 "description": "Locate Kent Mithra leaf"
}
```


### [2026-09-07T15:51:44.330Z] TOOL RESULT

```
--- count leaves
232
```


## [2026-09-07T15:52:00.398Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'ra- sb.' in p and 'friend' in p:\n        print(\"leaf(0-based)\",i,\"1-based\",i+1)\n        print(p[:200])\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['KNT']['page_offset']); print(d['KLN']['page_offset']); print(d['AHD']['page_offset']); print(d['MON']['page_offset'] if 'page_offset' in d['MON'] else 'n/a'); print(d['BQT'].get('page_offset')); print(d['BQT'].get('scans'))\n\"",
 "description": "Find Kent leaf and offsets"
}
```


### [2026-09-07T15:52:01.914Z] TOOL RESULT

```
leaf(0-based) 212 1-based 213
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis
leaf(0-based) 227 1-based 228
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
EU: ET TORR ON |
INS SEE cals l
leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
None
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
```


## [2026-09-07T15:52:10.814Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\np=t[227]\nimport re\nprint(len(p))\ni=p.find('ra- sb.')\nprint(p[max(0,i-1500):i+900])\nEOF",
 "description": "Print Kent leaf 227"
}
```


### [2026-09-07T15:52:12.127Z] TOOL RESULT

```
3685
арббио; per- haps deriv. to *marduna- ‘vintner’ (§144.IV, 8147. П, $153.1, $164.1V), ef. NPers mul ‘wine’, Skt. mydvikd- ‘grapevine’ (Bthl. AW 1151; otherwise Justi, INB 195), which possibly contains root mard- ‘crush (the grapes in the wine-making)’. Marduniyahya gsm. DB 4.84.
mav- vb. ‘send’: ef. Lt. moved Ч move’. [0т]- арай imf. mid. as pass. ($213, $235.II) DB 4.92 (dubious conj. of Kent, JAOS 62.269).
Mazdàh- adj. ‘wise’ (5156.1, $160.Ia): regu- larly compounded in Auramazdah- (q.v.); both
parts declined, but without an intervening word- divider, in Aurahya Mazdaha (8$185.IV) ХРе 10.
maskd- sb. ‘(inflated) skin’; NPers. mask, АКК. mas-ku-u ‘skin’, Aram. maškā: borrowed from Semitic ($99, $109, §117, §148.IV; see MB Gr. 5101). такаа lpf. (872) DB 1.86.
müha- sb. ‘month’: Skt. mása-, pIE *méso-; extension ($143.II) of pIE *més-, seen in Av. mah-, NPers. mah, Skt. mäs-, cf. also Lt. ménsis, Gk. шу, Gt. тепа, ОНС mano, Lith. ménuo, all mean- ing ‘moon’ or ‘month’. mdhyd gsm. DB 1.371, 42, 56, 89, 96; 2.26, 36, 41, 47, 56, 61f, 69, 98; 3.8, 18, 39, 46f, 08, 68, 88 (for *mahahyé, with con- traction of- ähah- to -ah-, with Gray, AJP 21.13-4; rather than the usual interpretation as ism. to stem mah-; $131, $165.n1, $185.IV).
miðah- sb. ($156.П) ‘evil’, the opposite of rüila-: Av. mibahya- ‘evil’, mi6aoxia- ‘falsely spoken’, Skt. mith- ‘to meet (as friend or antago- nist), engage in altercation’; cf. Hz. ApI 259-61, Kent Lg. 15.169-70, and hamigiya-. тиба asn. DNb 7, 9, 11.
Mié6ra- sb. ‘friend’; as deity, ‘Mithras’: El. т1-14-5а, Akk. mi-i-ri; Av. mibra-, NPers. mihr ‘sun’, Skt. mitrd- ‘friend’ (§9.VI, $33, §49c, $78, 5148.11). Cf. Vaumisa- and probably hamigzya-. Міга} nsm. АНЬ; Mitra (822) A’Sd 4, A?Ha 6; Ма А?а 5, А?Ра 25. Аз gen. ($818.П), M'tra A?Ha 5°, M‘éra A’Sa 4.
mub- vb., see maub-.
M udràya- adj. ‘Egyptian’; pl., al
```


## [2026-09-07T15:52:28.950Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i,p in enumerate(t):\n    if 'LEXICON' in p.upper()[:400]:\n        print(i, repr(p[:150]))\nEOF",
 "description": "Find Kent lexicon start leaf"
}
```


### [2026-09-07T15:52:30.309Z] TOOL RESULT

```
232
2 '� i\nтег. E\nEAD Мут\nOLD PERSIAN\nGRAMMAR TEXTS LEXICON\nBY ROLAND G. KENT\nProfessor Emeritus of Indo-European Linguistics\nUniversity of Pennsyloania\nAMER'
4 'y whose courtesy tt appears here\nFOREWORD\nThis volume has been prepared to meet the need for a comprehensive treatment of the Old Persian inscriptions'
20 'gs and uses; fuller discussion will be found in the phonology and in the Lexicon, s.vv.:\nI. Place-Names:\nAsagarla ‘Sagartia’, a district of Media, wit'
34 'ch problems must be settled by etymological comparison or by comparison with borrowings in other languages; but these are only problems relating to in'
193 't’).\n-\nLEXICON\nч.\nАтах$аса- sb. ‘Artaxerxes’ (Т, son of Xerxes; П, son of Darius II; III, son of Artaxerxes II): Elam. ir-tak-Sa-a8-Sa, Akk; ar-tak-Sa'
227 'ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá'
```


## [2026-09-07T15:52:49.020Z] TOOL CALL #26: Bash

```json
{
 "command": "ls site/pages/327.jpg 2>/dev/null; pdftoppm -f 327 -l 327 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg327 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 327"
}
```


### [2026-09-07T15:52:50.809Z] TOOL RESULT

```
site/pages/327.jpg
total 424
drwx------ 2 sfmqrb sfmqrb  4096 Sep  7 11:52 .
drwx------ 4 sfmqrb sfmqrb  4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   251 Sep  7 11:49 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb 30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb 28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb  4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb 62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb 65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb 73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40 Sep  7 11:49 queue.txt
```


## [2026-09-07T15:52:53.905Z] TOOL CALL #27: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg327.png"
}
```


### [2026-09-07T15:52:54.250Z] TOOL RESULT

```

```


## [2026-09-07T15:52:54.247Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T15:53:10.546Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 327 -l 327 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg327hi\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg327hi.png')\nprint(im.size)\nw,h=im.size\n# se-mitita box ~ y 520/2200 of 200dpi -> fraction\ndef crop(x0,y0,x1,y1,name):\n    im.crop((int(w*x0),int(h*y0),int(w*x1),int(h*y1))).save(name)\ncrop(0.20,0.225,0.46,0.25,'/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c_semita.png')\ncrop(0.20,0.295,0.50,0.345,'/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c_migare.png')\nEOF\nls -la c_*.png",
 "description": "Crop the two Latin boxes"
}
```


### [2026-09-07T15:53:15.605Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb 2639 Sep  7 11:53 c_semita.png
```


## [2026-09-07T15:53:18.967Z] TOOL CALL #29: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c_semita.png"
}
```


### [2026-09-07T15:53:18.980Z] TOOL RESULT

```

```


## [2026-09-07T15:53:23.491Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg327hi.png'); w,h=im.size\nim.crop((int(w*0.20),int(h*0.24),int(w*0.46),int(h*0.265))).resize((int(w*0.26*1.5),int(h*0.025*1.5))).save('c_semita2.png')\nim.crop((int(w*0.20),int(h*0.30),int(w*0.50),int(h*0.35))).save('c_migare2.png')\nEOF\necho ok",
 "description": "Re-crop"
}
```


### [2026-09-07T15:53:25.335Z] TOOL RESULT

```
ok
```


## [2026-09-07T15:53:27.971Z] TOOL CALL #31: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c_semita2.png"
}
```


### [2026-09-07T15:53:27.989Z] TOOL RESULT

```

```


## [2026-09-07T15:53:32.688Z] TOOL CALL #32: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c_migare2.png"
}
```


### [2026-09-07T15:53:32.701Z] TOOL RESULT

```

```


## [2026-09-07T15:53:36.678Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg327hi.png'); w,h=im.size\nim.crop((int(w*0.21),int(h*0.322),int(w*0.46),int(h*0.345))).save('c_migare3.png')\nEOF\necho ok",
 "description": "Crop migare line"
}
```


### [2026-09-07T15:53:38.473Z] TOOL RESULT

```
ok
```


## [2026-09-07T15:53:41.022Z] TOOL CALL #34: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c_migare3.png"
}
```


### [2026-09-07T15:53:41.033Z] TOOL RESULT

```

```


## [2026-09-07T15:53:44.631Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg327hi.png'); w,h=im.size\nim.crop((int(w*0.21),int(h*0.34),int(w*0.46),int(h*0.365))).save('c_migare4.png')\nEOF\necho ok",
 "description": "Crop lower"
}
```


### [2026-09-07T15:53:46.433Z] TOOL RESULT

```
ok
```


## [2026-09-07T15:53:49.689Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c_migare4.png"
}
```


### [2026-09-07T15:53:49.702Z] TOOL RESULT

```

```


## [2026-09-07T15:54:02.343Z] TOOL CALL #37: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['KLN'],ensure_ascii=False,indent=1))\n\"",
 "description": "MON and KLN full ref info"
}
```


### [2026-09-07T15:54:03.807Z] TOOL RESULT

```
{
 "title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)",
 "kind": "website+archive_djvu",
 "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)",
 "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).",
 "local_file": [
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf",
  "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt"
 ],
 "page_offset": null,
 "covers_etymology": true,
 "notes": "covers_etymology = partial: origin-language tag visible online, Latin etyma missing. The a'lam volumes (MON5/MON6 citations, e.g. MON5:528) are NOT online: vajehyab's Mo'in has no proper-name entries (tested افراسیاب — only compounds returned); abadis shows Dehkhoda and 'فرهنگ اسم‌ها' instead, which do give Avestan forms (e.g. Frangrasyan) and can serve as a cross-check. noorlib has no Mo'in 6-vol entry found. The 6-vol edition itself was not found on archive.org, Google Books or HathiTrust full view. || RE-SEARCH 2026-09: still no scan of the 6-vol Amir Kabir edition (incl. vols 5-6 اعلام) on archive.org, Google Books (API quota-limited; WebSearch found no record with preview), HathiTrust (no record surfaced), noorlib, ketabnak (author page persons/6040 lists 34 Mo'in titles, none the 6-vol فرهنگ), tarikhema, picofile, scribd, Commons/Wikisource. Only the 2-vol Adena condensation exists (archive.org, mirrored on ketabnak 65980/65981, picofile, persianpdf, scribd); its image PDFs were downloaded to incoming/MON/ (the _text.pdf variants with OCR layer are at the same archive.org identifiers). The 6-vol set is purchase-only (in print: iketab.com, bookroom.ir/book/97022, 30book.com/Book/32100).",
 "cites": "page number of Mo'in's six-volume Farhang-e Farsi; MON5:… / MON6:… = volume 5 / 6 (proper names)"
}
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


## [2026-09-07T15:54:15.817Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\n# map line numbers to leaf\nleaves=t.split('\\f')\nimport itertools\nline=1; \nfor i,lf in enumerate(leaves):\n    n=lf.count('\\n')\n    for target,name in [(4191,'azimuth'),(24059,'Mithras'),(24067,'Mitra')]:\n        if line<=target<=line+n:\n            print(name,'leaf',i,'-> printed p ~',2*(i-12),'..',2*(i-12)+1)\n    line+=n\nprint('total leaves',len(leaves))\nEOF",
 "description": "Compute Klein printed pages"
}
```


### [2026-09-07T15:54:17.151Z] TOOL RESULT

```
azimuth leaf 83 -> printed p ~ 142 .. 143
Mithras leaf 530 -> printed p ~ 1036 .. 1037
Mithras leaf 531 -> printed p ~ 1038 .. 1039
Mitra leaf 531 -> printed p ~ 1038 .. 1039
total leaves 903
```


## [2026-09-07T15:54:17.551Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- MON samt\"; grep -n \"سمت\" MON_part1.txt | head -5 | cut -c1-600\necho \"--- MON komonism\"; grep -n \"کمونیس\\|کمونیز\" MON_part1.txt MON_part2.txt | head -5 | cut -c1-600\necho \"--- MON mehr\"; grep -n \"مهرگان\" MON_part1.txt MON_part2.txt | head -3 | cut -c1-800",
 "description": "Mo'in 2-vol greps"
}
```


### [2026-09-07T15:54:17.644Z] TOOL RESULT

```
--- MON samt
106:فارسی شد. پس از جندی با حفظ سمت به دبیری دانشکد؛ ادبیات منصوب 
110:دکتر ادبیات فارسی در ايران شناخته شد. از آن پس به سمت ذانشیار و سپس به 
111:سمت استاد کرسی «تحقیق در متون ادبی» در دانشکدهة ادبیات به تدریس مشغول 
119:دانشگاه؛ ریاست سازمان لفت‌نامه به عهدة وی محول گردید. وی این سمت را تا 
199:وصی تعیین کرده بود تا اشعار وی را بررسی کند و قسمت لازم را انتشار دهد و 
--- MON komonism
MON_part1.txt:31963:ممالکك کمونیست مانند روسیهٌ شوروی و 
MON_part1.txt:31964:ممالکك کمونیست اروبای شرفی و چین 
MON_part1.txt:49758:دست چپی» طرفدار سوسیالیسم و کمونیسم. 
--- MON mehr
MON_part1.txt:12851:بی‌مهرگان که تشکیل رده اسفنج‌ها ر 
MON_part2.txt:69290:مهرگان: -(۸,۵)-۱0۵۲ [متعلق به مهر - 
MON_part2.txt:69312:ظاهرا از اسم عید مهرگان اخذ شده چنانکه
```


## [2026-09-07T15:54:30.570Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (505,506,507):\n    print('=== leaf',i, 'p~',2*(i-12))\n    print(t[i][:300].replace('\\n',' '))\nEOF",
 "description": "Check Klein leaf 506"
}
```


### [2026-09-07T15:54:32.151Z] TOOL RESULT

```
=== leaf 505 p~ 986
—  L.  maritalis,  ‘of  mar¬ riage',  fr.  maritus,  ‘a  married  man,  husband’, which  is  of  uncertain  etymology.  It  possibly stands  for  *mari-tos  and  lit.  means  ‘provided with  a  young  wife’,  and  is  cogn.  with  OI. mdryah,  ‘young  man,  lover,  wooer’,  Gk.  p.eipaE, ‘boy,  girl
=== leaf 506 p~ 988
 See  marital  and  marriage. Derivatives:  marri-ed,  adj.,  marri-er,  n. Mars,  n.,  the  Roman  god  of  war.  —  L.  Mars,  of unknown  etymology.  Cp.  March,  Marcia, Marcus,  Mark,  Martin,  martin,  martite.  Gk., (xApvotiiai,  '1  fight’,  is  not  cognate  with  L. Mars  (see  marasmus). 
=== leaf 507 p~ 990
—  Prob.  fr. F.  massue,  ‘club’,  fr.  VL.  *mattiuca,  fr.  *mat- tia,  which  is  rel.  to  L.  mateola,  ‘a  tool  for  dig¬ ging'.  See  mace,  ‘a  staff’,  and  cp.  masse,  mattock, masjid,  n.,  a  mosque.  —  Arab.  See  mosque, mask,  n.  —  MF.  (=  F)  masque,  fr.  ML.  masca, fr.  It.
```


## [2026-09-07T15:54:45.507Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\ndef findword(w):\n    for i,lf in enumerate(leaves):\n        if re.search(r'(?m)^'+w+r',', lf):\n            print(w,'leaf',i,'p~',2*(i-12))\n            m=re.search(r'(?m)^'+w+r',.{0,700}', lf, re.S)\n            print(m.group(0).replace('\\n',' ')[:700]); print('---')\n            return\nfor w in ['mean','migrate','mad','common']:\n    findword(w)\nEOF",
 "description": "Klein mean/migrate/mad/common entries"
}
```


### [2026-09-07T15:54:47.147Z] TOOL RESULT

```
mean leaf 511 p~ 998
mean,  adj.,  intermediate.  —  ME.  mene,  fr.  Or. meien,  moien  (F.  moyen),  ‘middle’,  fr.  Late  L. medidnus,  ‘that  which  is  in  the  middle’,  fr.  L. medius,  ‘middle’.  See  media,  ‘voiced  stop  con¬ sonant’,  and  cp.  median,  mesne,  monial. Derivative:  mean,  n.,  something  intermediate, mean,  adj.,  of  low  rank,  inferior,  base.  —  ME. mene,  ‘common,  mean',  fr.  OE.  (ge)mine,  com¬ mon’,  rel.  to  OS.  gimeni,  OFris.  mene,  OS.  gi- meni,  MLG.  gemeine,  gemene  (whence  Dan.  and Swed.  gemen),  MDu.  ghemene,  Du.  gemeen, OHG.  gimeini,  MHG.,  G.  gemein,  Goth,  ga- mains,  ‘common’,  OE.  man,  ON.,  OHG.  mein, OS.,  OFris.  men,  ‘false’,  OE.  man
---
common leaf 180 p~ 336
common,  adj.  —  ME.  commun,  comun,  fr.  OF. comun  (F.  commun),  fr.  L.  communis  (cp.  the OL.  acc.  comoinem),  ‘common,  universal,  pub¬ lic’,  formed  fr.  co-  and  OL.  moinos,  moemis  (L. munus),  ‘service,  office,  function’,  which  is  rel. to  OL.  moenia,  L.  miinia,  ‘official  duties’,  fr. I.-E.  base  *moin-,  *mein-,  ‘to  change’.  See  mean, ‘of  low  rank’,  and  cp.  commune,  communicate, immune,  municipal,  munificent,  remunerate.  Cp. also  mime,  minimum. Derivatives:  common-er,  n.,  common-ly,  adv., common-ness,  n. common,  n.,  1)  common  land ;  2)  common  people ; 3)  right  to  another’s  land  (law).  —  Fr.  common, adj.  Cp.  discommon. D
---
```


## [2026-09-07T15:55:08.790Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nlf=t[511]\ni=lf.find(\"of  low  rank\")\nprint(lf[i-40:i+2200].replace('\\n',' '))\nEOF",
 "description": "Klein mean entry full"
}
```


### [2026-09-07T15:55:10.115Z] TOOL RESULT

```
 something  intermediate, mean,  adj.,  of  low  rank,  inferior,  base.  —  ME. mene,  ‘common,  mean',  fr.  OE.  (ge)mine,  com¬ mon’,  rel.  to  OS.  gimeni,  OFris.  mene,  OS.  gi- meni,  MLG.  gemeine,  gemene  (whence  Dan.  and Swed.  gemen),  MDu.  ghemene,  Du.  gemeen, OHG.  gimeini,  MHG.,  G.  gemein,  Goth,  ga- mains,  ‘common’,  OE.  man,  ON.,  OHG.  mein, OS.,  OFris.  men,  ‘false’,  OE.  manad,  OE., ON.,  meineidr,  Dan.,  Swed.  mened,  OS., OFris.  meneth,  MDu.  meineet,  Du.  meineed, OHG.  meineid,  MHG.  meineit,  G.  Meineid, ‘perjury’,  lit.  ‘false  oath’,  and  cogn.  with L.  miinus  (OL.  moinos,  moenus),  ‘service,  of¬ fice,  function’,  munia  (OL.  moenia),  ‘official, duties,  functions’,  communis  (OL.  acc.  comoi- nem),  ‘common’,  OSlav.  mdna,  ‘change’,  iz- meniti,  ‘to  change,  exchange’,  Lith.  mainas,  ‘ex¬ change’,  mainyti,  ‘to  exchange’,  OI.  menift,  ‘ven¬ geance’,  Avestic  maeni-,  ‘punishment’.  All  these words  derive  fr.  I.-E.  *mein-,  *moin-,  -n-enlarge- ments  of  base  *mei-,  *moi-,  ‘to  change,  ex¬ change’,  whence  OI.  mdyate,  ‘changes’,  Lett. miju,  mit,  ‘to  change’.  Cp.  common,  adj.,  and words  there  referred  to.  For  I.-E.  *mei-t-, *moi-t-,  -(-enlargements  of  base  *mei-,  *moi-, see  mutable,  mutual.  Base  *mei-,  ‘to  change",  is originally  identical  with  base  *mei-,  ‘to  change one’s  place,  to  go’.  See  meatus,  migrate, meander,  n.,  winding,  as  of  a  river.  —  L.  Maean- der,  fr.  Gk.  MoaavSpcx;,  a  river  in  Caria,  noted for  its  windings. Derivatives:  meander,  intr.  v.,  meander-ing,  n. and  adj.,  meander -ing-ly,  adv. measles,  n.  pi.  —  ME.  maseles,  pi.  of  masel,  lit. ‘spot,  excrescence’,  rel.  to  MDu.  masel,  Du. mazelen,  G.  Maseru,  ‘measles’,  and  to  E.  mazer (q.v.)  E.  measles  was  influenced  both  in  form and  pronunciation  by  a  confusion  with  ME. mesel,  ‘leper’,  which  derives  fr.  OF.  mesel,  fr.  L. misellus,  dimin.  of  miser,  ‘wretched,  unfor¬ tunate,  miserable’. Derivative:  measl-y,  adj. measurable,  adj.  —  ME.  mesurable,  fr.  OF.  (=  F.) mesurable,  fr.  Late  L.  mensurabitis,  fr.  mensu- rare,  fr.  L.  mensura.  S
```


## [2026-09-07T15:55:18.408Z] TOOL CALL #43: Bash

```json
{
 "command": "timeout 600 python3 tools/ref_page.py BQT:2060 --image 2>&1 | tail -60",
 "description": "Fetch Borhan-e Qate page 2060"
}
```


### [2026-09-07T15:55:28.346Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 143; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2060.png
REF: BQT:2060  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 143  OCR-lang: fas

خود. ِ - ۹۰
مهف « بر وزن شهد . بلفت شام بیخی مهد مینا -کنایه از آسمان است .
است که آنرا بفارسی چوبك اشنان خوانند مهد فقس موسي - کنابه‌ازسندوقی
وعربان راحة آلاسد گوبند -ودرعربی‌بمعنی گهواره است که موسی 4 را بعد از ولادت ازخوف و بیم
باشد . ۱ فرعون درآن میان گذاشته دردجله ‎٩‏ انداختند .
مهد ۴ - بنم نات بروزن انجم . پرنده همهد۹۸ « بروزن مرسیه » نام شپرست
است صاحب مغلب ودم او ابلق میباشد و او را | درحدود مغرب زین ۲ .
پرتیزسازند - وکبوتری را نیز کوبند که تمام‌پر مهر ؟ « بکر اول وسکون‌انی ورای
او سیاه و دم او سفید باشد . قرشت » لام فرشته ات موکل بمهر و محبت
سس میا
۱ - بمنی‌رود .۴ مهدیه بفتح‌اول و کسرسوم وفتح چهارم مشدد . دوموضع است :
نخست موضمی‌درافریقا ودریگری موضمی که آنرا عبدالموژمن بن علی نزديك « سلاء بنا نهاد - شهر
اول که درافر بقا بود منسوبست بمهدی, وبین‌آن وقروان دومرحله راه بود . رك : معجم‌البلدان ۰
۴ - در سانسکربت 1311۳8 ۰ اوستا و پارسی باستان 1321111۳8 « بارتولمه ۲۱۱۸۳ »
۰ ۳ 5 « 3۹ ض : : ۹
0 و
بر و ۱ وک هر سر ۳ 5
و ههار
۵ : و ( زا مه 1 7 ی
1 گ ان 0( ند ره بر 2
۹ اجان 1۹ وا ۷ ۳
ِ ۱ چ رت چا / خ : ی 1 ۱
3 ۳ + 9 ۳ یه 7 یت .۲۰ ۳ ۱
و ۰ ۹ ۰۵ ۷1 ظ
1 ار ها کون ۳ 1 ۵
۱ ی مک ۳ ۳
و بخ ۱۱۳ اک ۳ 1
یت.. -حکا ۷ ام هس ۱
7 ۳ ۳ جاگ 90 : مه 1 او ۳ 4 ۰
هس سدع کچ ود
ی ْ وص و ری سح بی یی
جرست ره
۰ اا یت په ها 4:۳۰ کشا رح ۳ 1 ۸
۱۳7۳ 4 0 /
زک مد 3 5 وی ان |۹۷ 1 7 ۲
5 ۳۶ رفن 3 بک وس و 1 مین اد 0
۱ چووه ایسچه و رن یه یر سید ۳ دس : ی
محسمهٌ همپردر کاخ واتیکان ) رم (
شه در حاغیة صذحهٌ ۹۱۹
```


## [2026-09-07T15:55:41.389Z] TOOL CALL #44: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2060.png"
}
```


### [2026-09-07T15:55:41.955Z] TOOL RESULT

```

```


## [2026-09-07T15:55:41.952Z] INPUT

[Image: original 1650x2546, displayed at 1296x2000. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-07T15:56:15.262Z] TOOL CALL #45: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT\ncat > /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2060.vision.txt <<'EOF'\n[BQT vol. 4, printed page ۲۰۶۰ (pdf page 143) — read from the page image by Claude, 2026-09-07]\n\nRunning head (right): مهد\nPrinted page number (top left): - ۲۰۶۰ -\n\nRight column:\nمهد - بر وزن شهد . بلغت شام بیخی است که آنرا بفارسی چوبك اشنان خوانند وعربان راحة الاسد گویند - ودرعربی بمعنی گهواره باشد .\nمهدم - بنم ثالك بروزن انجم ، پرنده ایست صاحب مغلب ودم او ابلق میباشد و او را پرتیزسازند - وکبوتری را نیز گویند که تمام‌پر او سیاه و دم او سفید باشد .\n\nLeft column:\nمهد مینا - کنایه از آسمان است .\nمهد نفس موسی - کنایه از صندوقی است که موسی ۴ را بعد از ولادت ازخوف و بیم فرعون درآن میان گذاشته دردجله ۱ انداختند .\nمهدیه - بروزن مرسیه ، نام شهریست درحدود مغرب زمین ۲ .\nمهر ۳ - بکسر اول وسکون ثانی ورای قرشت ، نام فرشته است موکل بمهر و محبت\n[the entry continues; foot of page: بقیه در حاشیهٔ صفحهٔ ۲۰۶۱]\n\nMo'in's footnotes at the foot of the page:\n۱ - یعنی رود .\n۲ - مهدیه بفتح اول و کسر سوم وفتح چهارم مشدد ، دوموضع است : نخست موضعی درافریقا ودیگری موضعی که آنرا عبدالمؤمن بن علی نزدیك «سلا» بنا نهاد - شهر اول که درافریقا بود منسوبست بمهدی، وبین آن وقیروان دومرحله راه بود . رك : معجم‌البلدان .\n۳ - در سانسکریت mitra ، اوستا و پارسی باستان mithra « بارتولمه ۱۱۸۳ » .\n\nPlate at the foot of the page, caption: مجسمهٔ مهر در کاخ واتیکان ( رم )\nEOF\necho written; ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ | head",
 "description": "Save vision transcript of BQT 2060"
}
```


### [2026-09-07T15:56:15.360Z] TOOL RESULT

```
written
total 46660
drwxrwxr-x  2 sfmqrb sfmqrb   12288 Sep  7 11:56 .
drwxrwxr-x 12 sfmqrb sfmqrb    4096 Sep  6 18:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb  330101 Sep  6 17:59 1092.jpg
-rw-rw-r--  1 sfmqrb sfmqrb    2600 Sep  6 17:59 1092.vision.txt
```


## [2026-09-07T15:56:18.892Z] TOOL CALL #46: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T15:56:18.899Z] TOOL RESULT

```


```


## [2026-09-07T15:56:23.106Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%B3%D9%85%D8%AA",
 "prompt": "Give the Arabic entry سمت verbatim: its etymology (is it from Latin sēmita?), the noun samt and its meanings, and any Persian section for سمت. Quote the etymology text."
}
```


## [2026-09-07T15:56:24.181Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/zenith",
 "prompt": "Quote the full etymology of zenith, and any mention of azimuth, Arabic samt, samt ar-ras, Latin semita, Old French/Spanish forms and dates."
}
```


### [2026-09-07T15:56:28.597Z] TOOL RESULT

```
# Arabic Entry: سمت

## Etymology

The entry states: "From Aramaic סֵימִטָא (sēmiṭā) from Latin sēmĭta, but later reanalysed as deriving from an Arabic root س م ت (s m t)."

Yes, it is traced to Latin *sēmita*, though it came through Aramaic as an intermediary language.

## Noun: samt

**Part of speech:** Masculine noun

**Plural:** سُمُوت (sumūt)

**Meanings:**
1. Road, way
2. Mode or manner of conduct; modus vivendi
3. Gravity, staidness, steadiness, sedateness, calmness
4. Region or quarter towards which a course is directed
5. Compass direction
6. Azimuth

## Persian Section: سمت

**Etymology:** Borrowed from Arabic سَمْت (samt)

**Part of speech:** Noun

**Meanings:**
1. Side, way, hand, direction
2. Position, office
3. Azimuth
```


### [2026-09-07T15:56:30.883Z] TOOL RESULT

```
# Etymology of Zenith

**Full Etymology:**
"Point of the heavens directly overhead at any place," from late 14c. _zineth_, deriving from Old French _cenith_ and Medieval Latin _zyneth_, which were "bungled scribal transliterations of Arabic _samt_ 'road, path,' abbreviation of _samt ar-ras_, literally 'the way over the head.'"

**Related Terms:**

The Medieval Latin form may also connect to classical Latin _semita_ meaning "sidetrack, side path," which shares a conceptual link through the notion of "thing going off to the side."

**Azimuth Connection:**
The related word _azimuth_ (late 14c.) comes "from Arabic _as-sumut_ 'the ways,' plural of _as-samt_ 'the way, direction,'" directly referencing the same Arabic root as zenith.

**Figurative Sense:**
The meaning referring to "highest point or state" emerged around 1600, extending the astronomical term into metaphorical usage.

**Dating:**
- Zenith: late 14c.
- Azimuth: late 14c.

The entry notes these astronomical terms entered English from Romance languages that had adapted Arabic astronomical terminology through medieval scholarly transmission.
```


## [2026-09-07T15:56:40.669Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%B1",
 "prompt": "Give the Persian entries مهر verbatim: the etymology of مهر \"love/sun/Mithra/seventh month\" (Middle Persian forms, Avestan/Old Persian, Proto-Iranian), and separately the etymology of مهر \"seal\" if present. Quote the etymology sections."
}
```


## [2026-09-07T15:56:42.778Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-",
 "prompt": "List all the Proto-Indo-European roots spelled *mey- on this page (or linked from it): their glosses (to change/exchange, to bind, to lessen, to fix/build fences, to go) and which Pokorny page each corresponds to."
}
```


### [2026-09-07T15:56:48.102Z] TOOL RESULT

```
# Persian Entries for مهر

## Etymology 2 (Love/Sun/Mithra)

**Middle Persian origin:** "From [Middle Persian](https://en.wikipedia.org/wiki/Middle_Persian "w:Middle Persian") _[mtr'](/wiki/mtr%27#Middle_Persian "mtr'")_ (Mihr)"

**Avestan/Old Persian:** "from [Avestan](https://en.wikipedia.org/wiki/Avestan "w:Avestan") _[𐬨𐬌𐬚𐬭𐬀](/wiki/%F0%90%AC%A8%F0%90%AC%8C%F0%90%AC%9A%F0%90%AC%AD%F0%90%AC%80#Avestan "𐬨𐬌𐬚𐬭𐬀")_ (miθra, "covenant, contract, oath"), from [Proto-Indo-Iranian](https://en.wikipedia.org/wiki/Proto-Indo-Iranian_language "w:Proto-Indo-Iranian language") _[\*mitra](/wiki/Reconstruction:Proto-Indo-Iranian/mitra "Reconstruction:Proto-Indo-Iranian/mitra")_"

The entry shows this term originally meant "covenant/contract" in Proto-Indo-Iranian, evolved through Old Persian and Avestan, and later acquired meanings related to kindness, love, prosperity, and celestial references (the sun, month names).

## Etymology 2 (Seal) — Not Present

The Persian section does not include a separate entry for مهر meaning "seal." That definition appears only in the Arabic and Ottoman Turkish sections of this Wiktionary article.
```


### [2026-09-07T15:56:49.219Z] TOOL RESULT

```
# Proto-Indo-European *mey- Roots

This Wiktionary page documents three distinct homonymic roots spelled *mey-:

**Root 1: "to attach, bind, strengthen"**
- Pokorny page 709
- Example descendants: Latin *mūrus* (wall), Sanskrit *minóti* (to fix, establish)

**Root 2: "to change, exchange; go past"**
- Pokorny page 710
- Example descendants: Latin *meō* (to traverse), Sanskrit *máyate* (changes), Old Irish *mían* (desire)

**Root 3: "small, little"**
- Pokorny page 711
- Example descendants: Latin *minor* (smaller), *minimus* (smallest); Ancient Greek *meíōn* (less, smaller)

The page notes these are reconstructed terms based on comparative evidence across Indo-European languages rather than directly attested forms. Each root has extensive documented derivations across Celtic, Germanic, Italic, Indo-Iranian, Balto-Slavic, and other language families.
```


## [2026-09-07T15:56:57.165Z] TOOL CALL #51: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mitra",
 "prompt": "Quote the etymology of Proto-Indo-Iranian *mitra: which PIE root is it derived from (*mey- 'to bind' or 'to exchange'?), what suffix, what gloss, and list the descendants (Avestan, Old Persian, Sanskrit, and any Greek/Latin borrowings)."
}
```


## [2026-09-07T15:56:57.908Z] TOOL CALL #52: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Mithras",
 "prompt": "Quote the etymology of Mithras / Mithraism: Latin, Greek, Avestan/Old Persian forms, meaning 'contract', and the date/route of the Roman cult."
}
```


### [2026-09-07T15:57:03.497Z] TOOL RESULT

```
# Etymology of Mithras

**Linguistic Lineage:**
The name traces through multiple ancient languages: "from Latin, from Greek _Mithras_, from Avestan _Mithra-_, from Indo-Iranian _\*mitram_ 'contract.'"

**Meaning:**
The root concept centers on contractual relationships. It likely stems from the PIE root meaning "to change; exchange," developing into the sense of "contractual partner, friend," which was then conceptualized as a divine figure.

**Historical Documentation:**
According to the source, "His name is one of the earliest Indic words we possess, being found in clay tablets from Anatolia dating to about 1500 B.C."

**Roman Adoption:**
The cult gained prominence when "His worship was adopted by the Romans and enjoyed great popularity in the early empire." The word entered English around the 1550s as knowledge of this ancient deity spread through scholarly circles.
```


### [2026-09-07T15:57:03.779Z] TOOL RESULT

```
# Etymology of Proto-Indo-Iranian *mitrás

**PIE Root:** The etymology derives from Proto-Indo-European *\*mi-tró-s*, based on the root *\*mey-*. Pokorny (1959) refined this as meaning **"to bind"** (though Meillet earlier suggested "to exchange").

**Suffix:** The *-tra-* suffix functions as a "tool suffix" meaning **"that which [causes]..."**, similar to Sanskrit *mantra* ("that which causes to think").

**Gloss:** Literally "**that which binds**," with semantic range including covenant, treaty, agreement, promise, or oath.

**Key Descendants:**

- **Avestan:** *miθra* ("covenant")
- **Sanskrit:** *mitrá* (later meaning "friend")
- **Old Persian:** *Miθra/Mitra* (attested in 4th century BCE inscriptions)
- **Greek/Latin:** *Míthras/Mithrās* (nominative form of vocative *Mithra*, adopted into Greco-Roman Mithraism)
- **Middle Persian/Modern Persian:** *myhr/mehr* (meaning "love" or "friendship")
- **Armenian, Kurdish, Uyghur, Uzbek:** Various descendants through Persian

The original "covenant" sense is preserved best in Avestan; the Sanskrit shift to "friend" reflects one aspect of binding and alliance.
```


## [2026-09-07T15:57:13.056Z] TOOL CALL #53: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/communism",
 "prompt": "Quote the etymology of communism and communist: French communisme, date, from commun/Latin communis, and who coined it."
}
```


## [2026-09-07T15:57:15.503Z] TOOL CALL #54: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%D9%85%D8%AA/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for سمت verbatim, including the origin tag in brackets (e.g. [ع.]) and the meanings. Also quote the Dehkhoda entry's opening if present."
}
```


### [2026-09-07T15:57:17.287Z] TOOL RESULT

```
# Etymology of Communism and Communist

**Communism (1843):** "social system based on collective ownership," from French *communisme* (c. 1840), derived from *commun* and the suffix *-isme*.

**Communist (1841):** Noun and adjective from French *communiste*, combining *commun* with *-iste*.

**Root source:** Both terms trace to Latin *communis*, meaning "in common, public, shared by all or many."

**Original coiner:** John Goodwin Barmby (1820-1881), a British Owenite and utopian socialist who founded the London Communist Propaganda Society in 1841, is credited with the first written attestation of "communist."
```


### [2026-09-07T15:57:22.025Z] TOOL RESULT

```
# سمت (Samt)

## Dehkhoda Dictionary Opening

"سمت. [س َ] (ع اِ) طرف. سوی." — meaning "side" or "direction" as the primary definitions.

## Mo'in Dictionary Entry

**(سَ) [ع.]** ۱ - (مص ل.) راهی را در پیش گرفتن. ۲ - به راه درست و میانه راه رفتن. ۳ - (اِ.) راه، روش. ۴ - قصد. ۵ - طرف، جانب.

**(س مَ) [ع.]** ۱ - نشان داغ. ۲ - علامت، نشانه. ۳ - عنوان. ۴ - مقام.

## Core Meanings

The word carries two pronunciations with distinct meanings:
- **Direction/path sense**: choosing a route, proper conduct, intent, side
- **Position/status sense**: mark, sign, title, rank

The term also has specialized astronomical usage denoting azimuth—the angular measurement in celestial coordinate systems.
```


## [2026-09-07T15:57:31.190Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification\npython3 - <<'EOF'\nimport json,glob\nfor f in ['page-316.json','page-312.json','page-313.json']:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e['nodes']:\n            for rc in n.get('ref_check',[]):\n                if rc['ref'].startswith('MON'):\n                    print(f, rc['ref'], rc['status'], rc['note'][:300]); print()\nEOF",
 "description": "See how MON refs were handled"
}
```


### [2026-09-07T15:57:32.426Z] TOOL RESULT

```
page-316.json MON:3716 partial Mo'in's 6-volume pagination cannot be mapped online (refs_online.json: 'Page numbers cannot be mapped online'); the entries themselves were read in the 2-vol Adena OCR: 'مادر' and 'مایه' are present with Pahlavi tags, and the مادر/مایه etymologies Mo'in prints in Borhan-e Qate' (see BQT above) are h

page-316.json MON:3679,3716 partial Mo'in's 6-vol pages are not mappable online, but both entries were read in the 2-vol Adena OCR of Farhang-e Farsi: 'مامان: (ا.) (در زبان کودکان) مادر، والده' with 'مامانی: mamanī [فر. ف.]' (MON_part2.txt ll.43100, 43109) and 'ممه: [تر.] (ا.) (به زبان کودکان) پستان. ممه را لولو برد' (l.65508). Mo'in 

page-312.json MON not_checked no page is given in the book, and the six-volume Farhang-e Farsi is not online; the entry text served by vajehyab/abadis tags رزق as [ع.], consistent with the arrow

page-312.json MON:3650 partial the six-volume Farhang-e Farsi is not online and the page cannot be verified; the entry text served by abadis.ir/vajehyab from Mo'in does carry the tag [فر.] and the 'hanging lamp' definition, exactly as the arrow requires

page-313.json MON:3621 partial Moʿin, Farhang-e Farsi s.v. لگن (read via abadis.ir, section فرهنگ معین): «(لَ گَ) (اِ.) ظرف بزرگ لبه دار» — the headword and gloss 'tub' are confirmed, but the lexicon entry itself gives no etymology (Moʿin's etymology for this word is the Borhan footnote, BQT:1904).
```


## [2026-09-07T15:57:48.654Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT maeni\"; grep -n \"'Strafe'\\|Strafe\" BRT.txt | head -5 | cut -c1-300\necho \"=== BRT mi0o\"; grep -n \"mi9wara\\|mi&wara\\|mi^wara\\|mi9o\\b\" BRT.txt | head -8 | cut -c1-400\necho \"=== LEW semita\"; grep -n \"semita\" LEW_1910.txt | head -5 | cut -c1-500\necho \"=== LEW migro\"; grep -n \"migro\" LEW_1910.txt | head -5 | cut -c1-400\necho \"=== LAT semita\"; grep -n \"semita\" LAT.txt | head -5 | cut -c1-500",
 "description": "Bartholomae + Latin dictionaries"
}
```


### [2026-09-07T15:57:48.755Z] TOOL RESULT

```
=== BRT maeni
2503:(Y.  j2.  15);   oft  wegselassen,  zB.  Vp.  12.  54  Schuld   und   Strafe    aus  der  Verhandlung
2528:i)  'Strafe'  (nur  Ableit.).  a)  Du.  'Schuld  16;  —  U  gaumillc^  . .  xia>^am  . .  agarbä- und  Strafe':  kö  asti  tkaEsü  *visätö  (sd.)  ?  yata  .  .  '/a*  xsdi''am  .  .  Bh.  /.  11  f ;  — yö  'ta  pairi  ar>>rra  frazänaiti  ".  .    vie.t\yäsaDAa..l>aoi'j7m 'tarn  b
2601:Strafe  dessen,   der  sich  mit  Zauberei  be-  >'"'    paoun-a    'pataio    dnnjayan  V.  4.^5:
4812:(mit  Akk,):  yezica  hi  anya  aya  /yao^na /ravarsia paiti fa'^^ i'''  As cii:a  "und  wenn er  andere  Übeltaten  begangen  hat,  so  ist die  Strafe  dafür  beglichen"  V.y.  21;  — *paiiit^m'^^  ^'^  he  manu  ar?kat  *paiti- t>m  vaio  syaoimm  uzvarlt>m  (sd.) . .  "so soll  ihm  beg
4888:•  j.  ayarv.dräjah-  n.  Dauer  eines  Tages': *;irr  vä  äzaili  (sd.)  'jS  vä  vaslryll  (sd.) "(so)  soll  man  ihm  (als  Strafe)  drei  (mit der  Peitsche)  diktiren  oder  einen  Tag  lang Feldarbeit"  N.  42,  *43  '>,  6g,  83,  loff;  6g.
=== BRT mi0o
=== LEW semita
=== LEW migro
=== LAT semita
8744:semita calles-, Serv. Ae.4,405; Isid., Diff. 1,539; Orig. 15,16,10. Puis
57142:Comme premier terme de compose, avec la meme valeur, on a lessemita
57148:semita, -ae f.: cbemin de pieton, sentier, trottoir (= crepido).
65234:An secretum iter et fallentis semita uitae. A 1'^poque de la basse
68189:-aa f.: voie, route, chemin, rue (oppos 4 a semita , sentier, trottoir);
```


## [2026-09-07T15:58:02.186Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '57140,57160p' LAT.txt\necho \"=== LAT meo/migro\"; grep -n \"^meo\\|meo, -are\\|migro, -as\" LAT.txt | head -10 | cut -c1-300",
 "description": "Ernout-Meillet semita"
}
```


### [2026-09-07T15:58:02.248Z] TOOL RESULT

```
45 et Diom.; ces formes sont confirmees par 1 'ombrien semu "medio"
et les 1 . romanes, cf.M.L.7811 semis et semus, 7799 sSmare.
Comme premier terme de compose, avec la meme valeur, on a lessemita
1083 ~
correspondants: gr.r)(i,i,—, v.h. a.sdmi -, skr.samt-. C'est a peine si,
en sanskrit, sani existe a 1'etat de mot isole, et il doit d'ailleurs
avoir £td ddtache de composes. I .-e.*semi- indique ce qui n'a qu'un
cote, et appartient originellement au groupe *sen- de sim-plex, etc.
semita, -ae f.: cbemin de pieton, sentier, trottoir (= crepido).
Ane i en (Enn. ), usuel. Panroman (sauf roum.), M. L. 7813.
Derives rares: sSmitdlis (= evo8 loc), Vg., Cat.8,30; semitdrius, Cat.
37,16; semitdtim, Titin.; semito,-as; -tatus', SemitdtricSs (deae).
Sans ^tymologie.
semper adv.: une fois pour toutes, toujours; chaque fois. De
sen + per , qu'on a de meme dans parum-per, etc.
Derives: sempiternus, formd sur aeternus , d'ou a basse epoque,
sempiternitas. Composes (rares et tardifs): semper-florium,-uiuus
(= aeui^oaoS, —ov, nom de la jdubarbe). tlsitd de tout temps. Panroman
(sauf roum. ), M.L.7814.
Le sem- qui est ici est le mot indo-europ^en pour "un" que con¬
servent gr. ei,S, ev avec le fdminin gr.(Al,a, le ddrivd arm.m i "un"
=== LAT meo/migro
37934:migro, -as, -aui, -atum, - 5 re: changer de residence5 s’ en aller,
79208:meos y. ang., 753.
```


## [2026-09-07T15:58:05.415Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"m[a@]\\{1,2\\}[eéf]ni[-‐]\\{0,1\\}\" BRT.txt | head -20\necho \"=== try mreni\"; grep -n \"mroni\\|mfeni\\|maeni\\|maéni\\|mafni\" BRT.txt | head -10 | cut -c1-200\necho \"=== BRT lines with 'Strafe' + Ableit\"; grep -n \"nur  Ableit\" BRT.txt | head -10 | cut -c1-200",
 "description": "Find Bartholomae maeni"
}
```


### [2026-09-07T15:58:06.781Z] TOOL RESULT

```
4978:maeni
8850:maeni
=== try mreni
4978:masyJ  arfi^m  (sd.)  yat  ustäntm  bunjayät V.  7.  71;  —  aom  (NSn.)  aUike  asti  uz- varxim  yai  iiä  .  .  dahäitt  V.  18. -^t,  — p?r»sä  'val  ya^ä  hrS ,  .  ^wäras  (sd.)
8850:—  iäi/  (ab  NPn.)  he  afsman  .  .  käis pisträis  (als  NPn.)  Y.  19.  i6f.  2)  adjek- tivisch: kä  tim  ahyä  *maenis  (sd.)  anhat paouruye  Y.  44- 19;  —  i'f  ahmäi  aji/ )rm
=== BRT lines with 'Strafe' + Ableit
2528:i)  'Strafe'  (nur  Ableit.).  a)  Du.  'Schuld  16;  —  U  gaumillc^  . .  xia>^am  . .  agarbä- und  Strafe':  kö  asti  tkaEsü  *visätö  (sd.)  ?  yata  .  .  '/a*  xsdi''am  .  .  Bh. 
5487:•  j.,  g.  'araS-a-  n.  'Sache'  usw.  i)  in  altem Sinn  'Rechtsstreit'  (nur  Ableit).  2)  'woran einem  gelegen  ist,  Angelegenheit,  Anliegen': -liJil  vöizdyäi  (sd.)  kamahya  tJm 
6302:•  j.  *asa'vaat-'*  Adj.  i)  'rechtschaffen' (nur  Ableit).  i)  'der  das  (höchste) Anrecht  a)  besitzt':  haurvafsavS  .  .  drvä Maurva  -vantö  (NP.)  Y.jÄiS.  b)  'ver- schafft':  
10651:•  j.  xrü-  f.  'blutiges,  rohes  Fleisch':  musti.- masaah»m  xrüm  "ein  fausigrosses  Stück Fleisch""  Yt.  14.  33.  3)  'Grauen,  Graus' (nur  Ableit.)-  a)  Name  eines  Da^'a: psr
12235:•  j.  t^Oxya-  i)  Adj.  (fem.  yä-)  'dunkel, finster':  °fyam  aipi  xsapanim  Yi.  14.  13; —  'ryasäi  (GSf)'>  kala  xsafnS  "auch in  finstrer  Nacht"  Yt.  1^31,  ib'.  10;  — x
13774:feindselig'   (nur  Ableit.),
14385:"Furcht  erwecken' :  %wyatit-  (nur  Ableit).
15017:•  j.  patti.vak-  1)  Adj.  'antwortend,  er- widernd' (nur  Ableit).  2)  f.  'Ausspruch'; lim  ailaya  'vaca  paifyämraet  (sd.)  Y.  21.4.
17373:Unterseite'  (nur  Ableit).
18723:is  yä  mä  ttxfyei/l  mnfsaitt  %'wal  (sd.) Y.44.%; —  k(ü  mh  mrifsmtii  . .  paiica.- dasa  tnä  n^n/saiti  Ytj.  2;  —  tunfsatä- (nur  Ableit.).
```


## [2026-09-07T15:58:15.440Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '8835,8860p' BRT.txt | cut -c1-400\necho \"=== LAT migro\"; sed -n '37930,37950p' LAT.txt",
 "description": "BRT maeni context, LAT migro"
}
```


### [2026-09-07T15:58:15.501Z] TOOL RESULT

```
•  }■>  S->  P-  It*"  (fem-  kä-),  'kay-  (auch fem.)  Pron.  interrog.  'welcher?,  wer?'; I)  als  eigentliches  Fragewort,  an  der Spitze  desSatzes;  1)  substantivisch  :-i-J  r/iqm
yazäite  kö^  .  .  kahmäi  raisca  s^armasea kahmai . .  dnatät)m  ..  baxsäni . .  kahmai"  . . Yt  i0.io8-iio;  —  kü  nd  stavat  kff*  .  . kahe  nS  i',a  nama  äfairyüt  kakmäi  nö  tat dii>nm  dayiit' yal  ..  Yt./j.So;  5.8-",  A*. 15',  /./.473;  —  k5  'i'Wam  . .  inaoili  ks .  . /iaesayati  \.iX6i;  Y.^.SPUZ.,  V.;.'.4a; —  kasp  "iwqm  paoiryö  . .  masyö . .  hun�
14*
dby  Google
4^3
ka-  I  I  A
ka-  n  I  1
424
S4-J3',  —  *a/  aitahe  paiti  .  .  axaBa  V. JÄ68; — /fl/(ASn.)*'  alsa  nätrika paoifim :^ar»%anam  c^aräl  "was  soll  die  Frau  als erste  Speise  gemessen?"  V.5.S0;  —  Ictm (ASn.)3>  haxa  ha^  "baraiti  (sd.)  Y.tfa.S; 20,4;  —  kJng  ä  vaiihSus  fimat  mananhd /isti/{sd.)  "wer  sind  sie,  bei  denen  . ,"  Y. 4^.11;  —  kahmäi  fradaesayS  damqm  V. 2,1',  i;  —  ^
ayä  kahmäi^^  vananqm  (sd.)  dadh  Y. 4^15.  a)  mit  Gen.  part:  kö  hg  . . ae%rapaitinq7r^cä\  *afraoxti  (sd.)  astryäü N.  75 ;  —  kahmät  mazdayasnanqm  har»- 'hrtm  barät  V./j.  17;  N.  6'/,  G2;  —  kake vS  urva  /räye^ät  "^cuius  vestnim  anima . .  ?" Yt  13. 50;  —  iat  vast  (sd.)  iaj  vä  stBlö kat  Vä  yamahya.  "quid  vis?  quid  laudis  . ." Y.J4.12;  
yäil  pmsäi  (sd)  dngvä  vä  Y.  44.  u; jo.i;  —  ks  kvS  yS  .  ,  \.46.g;  —  koste asavä  urva^sY. 46.14;  —  kat  tSi  räzarS Y.34.\i;  —  kat  tat  dqma  ..  Y.ij.i,  5;
—  iai  hqm.srui.väam^a  ti.24i  —  hat humatPin  Y.ig.ii);  19".  a)  in  Kon- gruenz mit  dem  Praedikat:  kä  hl  asti ä>a  (Stverz.)  kä  he  asti  Spjntis  kat  he asti  yaozdä^rsm  Y.3.%%;  36  usw.;  —  kä (NPn.)  asti  i>yeß  mar/aonJ  (sd.)'V.iS.8;
—  liaya  (NP.)  kanti  vaca  {bisämmta) I kaya*  ..N.34-J6;  —  l*'kaya  hmti  mas- ya/phs  aRai  .  .  I kaya    kasyavhsi  F.jc;
—  icayö  äal  ('quaenam')  aSe  raocä  (sd.) aw/ij«.._f?..  V.2.39;  iMia.  a)  Kopula fehlt:  kai  vS  xsa^rim  kä  T/tls  (sd.)  syao- :^anai  Y.34.5;  —  60  *qst0  *iä  *tarö.- maitiP'>  ti.41;  —  kä  yä' kaine  Y. 14.11;
—  kä  fralaitis  Ii.103;  —  liaya  (NP.) ratavif  "wer  sind  die  Ä.T  Y.  79. 18;  18;
—  iäi/  (ab  NPn.)  he  afsman  .  .  käis pisträis  (als  NPn.)  Y.  19.  i6f.  2)  adjek- tivisch: kä  tim  ahyä  *maenis  (sd.)  anhat paouruye  Y.  44- 19;  —  i'f  ahmäi  aji/ )rmävi  I  Hl  ahmäi  jasal  äyaptim  Y.g.y, H.  f .  6 ;  —  /  Hsca  caräitis  ahi  yqm . .  "und(?) was  fiir  eine  Frau  bist  du,  die  . ."  H.  2. 10;  —  *kqm^'>  npmSi  zqm  ku^rä  n^mPi (s
—  ki  mi  nä  %ratä  vtsts  Y.50.  i;  —  ks urva'^0  (sd.)  .  .  zara'i:uiträi  nä  mazdä Y.5/.11.  U)alslndefinitum">,  l)mit mit  folgendem  cit  'wer  immer,  welcher  es auch  sei',  nur  substantivisch ;  1 )  sva.  'irgend Jemand,  irgend  ein,  quispiam';  mit  Gen. part.:  hs  anhäiti  zazustimS  (sd.)  xlayS kasHt  masyänqm  ". .  welcher  der  Menschen es  auch  sei"  YL  /
dby  Google
4»S
ka-  n  I  I
ka-ns
4'6
(sA)  Jasti  N,/oj; — ^kaAyl^^"^  dahmanqm sao^räoa  (si)  *ratu/rU  N,  40 ;  —  draos (sd.)  z-iJ  paiti  söinma  unam  vä  katcit  vS paiti  sidaranqm  N.  IQO;  —  kahmäicit yanhqm  jasS  Yt  13.  41;  41,  V.  7.  7: —  yahmäl  kahmäiHt  na^nanqtn  va ä'ird  baoiöTm  baraiti  ahmst  kahmätHi naimanam  .  .  paiH.jasalH  ütars welcher  (Seite)  her  nach  irgend Seite  der  W
i'ii  statt  riV 'quisque':  ias(a'''^'^wqm  cakana «i'a(sd.>  mmanaca  "quisque  teamavit.." H.  2. 1 1.  2)  verdoppelt,  auch  mit  eil beim  zweiten  Mal,  dnw.  I ,  nur  substantivisch ; I )  'quispiam',  mit  Gen.  part. :  hakmi  kakmi- nl  Tii  aipyanqm  kahtni  kakmicit  vä ara^yanqm  Yt.11.  5.  a)  'quisque':  kaähe kaähe  apayzäire  nmarum  histaite  "am  Ab- fluss  eines  jeden 
gäiu*saste\t 5. 102.  a)  mit  Gen,  part: hamistayalca  .  ,  kahe  kahyäcU  drvatqm Y.  61. a,.  3)  mit  vorangehendem  Relativ und  folgendem  1)  clt  (hinter  ka-\  2)  ^a (hinter  i kay-)  'Jeder  der..,  quisquis,  qui- cunque',  nur  substantivisch;  1)  nur  gAw.: y3  dalnqm  vokB  *sänsttl  (sd.)  manatthä .  .  kas^l  Y.4p.  5;  —  «ÄJ  ahmäi  yahmai Ulla  (sd.)  iahmäicit  .
amanha  asti  masyd  gfurvaya  hl . .  zUvarp Y.p.28;  —  ai  .  .  mainyßm  zara%uströ v^jtttl  (sd.)  yaste  I  ascil  spSmstd  Y.  43.16; —  ySi  mffi  ahmii  s^rao/^m  dqn  I  cayasla (NP.) "'  upä.jimm  (sd.)  . .  ". .  die  mir  ihm Gehör  schenken,  all  die  .."  Y.415,5;  —  MiSl Spants  mainyti  ,  .  asäunl  cBÜ  (sd.)  yä  3i lelcä  vakistä  .  .  drvgvä  baxhitf  (sd.
=== LAT migro
mlgale: musaraigne. F.mprunt tardif (Mul. Chir.) au gr. p.uyaATj'.
Derivd: migalinus: couleur de musaraigne.
*migdllix: mot de forne et de sens incertains (les mss. palatins
ont micdilia) qu'on lit dans 1 'Ambrosianus de Plaute, Poe, 1033.
migro, -as, -aui, -atum, - 5 re: changer de residence5 s’ en aller,
sortir5 emigrer, se changer. Sens concret et abstrait5 transitif ou
absolu, correspond a (xetapa.tvoo, p,6TOL>ta) comme a imep^oa V005 cf. Geli.
2,29,16, cassita nidum migrauit. Quelquefois "transgresser" (par
oppos. a seruare, conseruare, cf. Cic. Fin.3,30,675 Off. 1,80,31). — An¬
cien (Pl.), usuel, classique. N'est demeurd qu'en provenyal, cf.M.L.
55<>5 •
Ddrives et composes: migratio (Vic .),-tor (Gloss.)5 admigro (Pl.);
com-, de-, e- (M.L.2O61), in-, prae-, re-, trdns-nigro, et leurs
d 6 rivd s.
On interprete ce verbe comme d^riv£ d*un adj ectif *nigro~, ou la
racine, de la forme nig-, serait un dlargissement de la racine *mei-
" changer "5 v. munis et nut 5 , le grec a aussi une forme a dlargissement
dans cqxetpw "j '£change".
miles {niless Plaute, Au.538, de **t le t-s), -i tis m. (le f^minin
n'apparaat que dans Ov., et semble artificiel): soldat, terme g^neriquejmilimindrum
- 7 lG -
```


## [2026-09-07T15:58:28.400Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"44\\.  *19\" BRT.txt | head -20 | cut -c1-250",
 "description": "Find BRT maeni entry via Y.44.19 citation"
}
```


### [2026-09-07T15:58:28.445Z] TOOL RESULT

```
11717:(ASf.)  il  vS  *sp3r3ds  nivarllnl  "die  hier (oämL  die  Braut)  will  ich  .  ."  Y.  S3- 4.  b)  adjektivisch,  nur  b)  im  jAwr.; azfwt  yd  ahurS  maztia  ..yas»  tat  nmätam äkffVfUM  srlrsm  .  .  V.  22.  i ;  —  tUtrtm  .  . y
11741:Korrelat;  a)  substantivisch;  a)  im  gAw.: yaitat  (Sp.öi^m.)  mtzdim  ..  ndil  däifl,  kä tim  (ASm.)  ahyn  *mainis{sd.}  at^fiat  Y.44. 19;  —  ySngstü  masds  .  .  minal  (sd.)  , ., fing  zbaya(s6..)'^.46.  14;  — yqsca  haxsa
13136:(Konj.)  Y.44.  19;  34. 14;  —  yh  dh  asls (sd.)  dr^äiti  asSunal^  Y.4^.  4; — yqm xsnät>m  ränsibyä  da  .  .  mazdä  Y,  5/.  g; 31.  3;  —  Aau/tus{s^) . .  mazdä  dadät  ahurS dagHayai  Y.  53. 4 ;  —  yakmai  uHä  (sd.
14948:KorapE.;  vgl.  auch  pmidiiaya-.  —  Zum  V. 'Jä^y,  vgl.  Ti-p.  paidä,  wozu  Hbm.  PSt.  44. 192.  —  ■)  Ungefähr  sv«.  'oAü-  (sd.).
18697:srz.)  wer.."  Y.44.4;  3"*'; — is  urva'iä (sd.)  tpUamai  saraiuHräi  nä  mazdä  Y. 5/.  11;  —  kS  möi  paiSiii  ks  tnS  na  "i^rStä vistd . .  azää  {iA.)  Y.30.  i;  —  ataf  ahmäi .  .  üiä  (Sp.  134  o.)  ankaitl  .  
19045:—  äat  ma  n'  mafyäka  .  .yazittteYx,  10.^4'  sfnghanXn'  anafsmqmY.4ß.i'}.  zu2): (vgl.  8.  23,  Sp.  1074  m.);  —  es  ist  das  yastal  mlidtm  hanmtt  (sd.)  «°  daiil  Y. Praedikatsnomen  des  vorhergehenden  posi-  44. 19. 
20768:jAiw.;  das  Relativ  ist  a)  substantivisch: yOi  däityayaona  ''car^nta  ..noil  aitaEsqm.. N.52;—  s.  noch  N.55(Sp.  1205  0. j; — mit  Gen.  part:  yatca  aSaliqm  ra%wqm faoiryö  paiti  ä./asät  hävanänim  (sd.)  a^m astayeiti
20818:1300  o.);  zu  3):  iamnil .  .  yS  Tt  aAmai jr;'2«*33(sd.)  nä  däitl'^,44.  19.  b)  im jAw.;  das  Relativ  ist  1)  substantivisch; NSm.:  mi^rvm  ..yB  Ssvnqm  äsui yS  arf- dranqm  arpärö yö'" ..  Ytio.ög;  G./.öJj ahurahe  ma
```


## [2026-09-07T15:58:41.947Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHM mithra bind/exchange\"; grep -n -i \"exchange\\|to bind\\|contract'\" AHM.txt | head -12 | cut -c1-350\necho \"=== AHM maeni\"; grep -n -i \"maeni\\|maēni\" AHM.txt | head -5 | cut -c1-200",
 "description": "Gershevitch on mithra etymology"
}
```


### [2026-09-07T15:58:42.017Z] TOOL RESULT

```
=== AHM mithra bind/exchange
2358:1164, Wi.’s translation of suplisaranga- by ‘Schultermagen = Ge- schwisterkinder’ has been accepted by most interpreters. Da. defined the word more closely as ‘ qui s’appuie contre l’épaule l'un de autre’, and, in his Addenda, ZA, 1, 197, as ‘cousins’, Bth. has ‘Gaugenosse’ without explanation. Nearest to what secms to b
2424:belongs to it’. As simdi3ra- obviously contains sim@-, its relation to the latter is quite likely that of Arm. sameti-2 to sami-k. sameti-k is the strap which passing underneath the neck of the animal connects the twa yoke- pegs. In Hiibschmann’s opinion the word represents *sami-a-ti, -a- being the compound vowel, and #7 belonging to Gr. 
2615:1451. The formula vispanam daliyungm daishupaitim, which also accurs in Ny 1.7, the condensed hymn to Mithra quoted above, p. 263, has been translated ‘ Landesherr aller Lander’ (Wi., Spi., Wo., Lo., Htl.), ‘kSnig aller valker’ (Gdn.), ‘maitre de tous les pays’ (Da.). What exactly these schalars thought was the meaning of the title
=== AHM maeni
```


## [2026-09-07T15:58:44.222Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== LKT\"; grep -n -i \"zenit\\|azimut\" LKT.txt | head -10 | cut -c1-400\necho \"=== AFA semita/samt\"; grep -n -i \"semita\\|sēmiṭā\\|samt\" AFA.txt | head -10 | cut -c1-300\necho \"=== DEV azimut\"; grep -n -i \"azimut\" DEV.txt PHN.txt | head -10 | cut -c1-400\necho \"=== SKT zenith\"; grep -n -i \"^zenith\\|zenith\" SKT.txt | head -5 | cut -c1-400",
 "description": "Lokotsch/Fraenkel/Devic/Skeat"
}
```


### [2026-09-07T15:58:44.349Z] TOOL RESULT

```
=== LKT
3598:'��hnlich,  entgegengesetzt  gelegen',  nazlr as-sanit  'dem  Zenit  entgegengesetzt'; hieraus  kat.  sp.  pg.  frz.  rum.  nadir  'Fuß- punkt'; M.nadiro;  dtsch.  Nadir,  engl.wa- dir  'dem  Zenit  entgegengesetzter  Punkt'. [DE  323.   Eguilaz  462.   Devic  DEt  174.
4120:'Weg,  rechter;  Richtung',  plr.  sumüt, simüt;  hieraus  mit  ar.  Art.  it.  azimut, azimutto,  frz.  azimut;  dtsch.  Azimut [oder  meistens  mit  grundlos  angefügtem h:]  Azimuth,  engl,  azimuth  'Bogen  eines Scheitelkreises'.  —  Aus  samt  ar-ru'üs 'Richtung  der  Köpfe'  oder  kurz  as-samt wurde  mit  Verschreibung  von  m  zu  ni it.  zenit,  frz.  engl.  ndl.  zenith,  dt
4121:nit  oder  Zenith  'Scheitelpunkt'  im  Ge- gensatz zu  Nadir  [s.  hier  Nr.  1565). [Devic  DEt  54.  NALLINO  in  RSO  VIII (1919),  3(19  ff.
5711:ausbaldowern  j.  145 ^yw/c  St.  41 Äzarolapfel  2206 Azimut(h)  18l8 aewr  1311
5891:zager  mhd.  1760 Zamlott  653 Zec/i/M«  1903 Zedrach  140 Zenit(h)  1818
5980:azimuth  1818
6340:aumasor  afz.  1399 aumucelle  afz.  1520 utimusse  afz.  1520 nuqueton  afz.  1272 avarie  138 avicenniie  893 ayan  38 azidarac  140 ««ciT  2180 memine  29 uzeroUe  2206 azimut  1818 rtso^A  2208
6881:azimut(to)  1818
7262:zarcii  siz.  220;") zarda  670 zaro(so)  2186 zamlli  dial.  2209 zecca  1903 zecchino  1903 zenit  1818 zenzero  1930 ztnzovero  1930 rerda  670 ^«•0  1894 zetan(ino)  2188 zettovario  2215 «iirf<o  2173 zibibbo  siz.  2214 zicchineffo  siz.  1904 zigrino  1760 zinefra  1828 3»röo  2030 «iro  2222 aocco  1782 zotico  1927 ^of<«  siz  1875 zübhiu  siz.  2227 zubbu  siz.  2226 zucher
=== AFA semita/samt
62:Den gesamten Buchtext können Sie im Internet unter |http: //books . google .coiril durchsuchen..33. -2^0
2977:Dunkel bleibt auch diis sehr vereinsamte »Lu im Sihuh
=== DEV azimut
DEV.txt:700:AziMUTH.  Terme  d'astronomie  :  arc  du  cercle  de  l'ho- rizon compris  entre  la  méridienne  et  la  trace  d'un  plan vertical.  De  l'arabe  o^cviJi  as-semt,  que  les  astronomes orientaux  emploient  dans  le  même  sens^,  et  qui  est  aussi le  mot  dont  nous  avons  fait  zénith.
PHN.txt:2021:AZIMUT, s. m. (a.)
PHN.txt:2022:(;:a>«wJ| [a«9«m/] la voie droite. On appelle azimut, en astronomie,
PHN.txt:2024:angle droit, et azimut magnétique un arc qui sert à mesurer la
PHN.txt:2026:transcription azimut; mais on pourrait tout aussi bien écrire ce
PHN.txt:10135:aussi par corruption le substantif azimut. Voyez ce mot.
PHN.txt:10262:Azimut, s. m. (a.) 5i
=== SKT zenith
12132:Nadir,  the  point  of  t^- the  Ecnith.  (Arnb.)  .\ nastru*j  ^lamt,  the  riB'  1 1 ing  to  the  zenith.  *■•  Arau corresponding  to  ;  ej'jom/,  1^  ail aHo  tne  renitli.  See  AcimatJi,  A (The  I  is  hoe  the  t;ih  Ictm  of  lb« alphabet.)
21821:[Airicaii :  according  to  Littr^,  the  word  is of  Ethiopian  origin. Zodoary.  an  £.  Indian  root  resembling ginger.  (F.—  Low  L.  —  Per«.)  Y.udoairt, CoU  —  Low  L.  Uitoaria.  —  Pens.  saUzvAr, siVtMir,  zedoary ;  a\io&^\i jtuixtNir.  ^The O.  F.  form  was  citouart,  citoual,  (i/oaJ; whence  M.E.  ufcxva'e, Chancer. C.T.  1 369 1 . Zenith.  U''-  -  ^RQ  -  Arab
23699:French  from  Spanish  from  Arabic,  am* ber,  cotton  (i),  fonfnre,  galingale,  garble, garbage,  genet,  ;ennet  (genact),  lackey Jacquey).  mojJc  (masque),  masquerade, mosque,  ogee  (ogive),  racket  (1)  traquct), realgar,  ream,  »umach,  syrup  (sinip),  tabby, talc,  tare  (3),  tariff,  zenith,
```


## [2026-09-07T15:59:00.515Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN mithra/friend\"; grep -n \"mi9ra\\|mithra\\|mitra\" SYN.txt | head -8 | cut -c1-350\necho \"=== SYN communis\"; grep -n \"communis\" SYN.txt | head -5 | cut -c1-350\necho \"=== IEC mei\"; grep -n \"mei-\\b\\|meigw\\|mitro\" IEC.txt | head -10 | cut -c1-300",
 "description": "Buck and Mann"
}
```


### [2026-09-07T15:59:00.590Z] TOOL RESULT

```
=== SYN mithra/friend
905:ME mudde, NE mud, MLG mudde, MIG, Du. modder (MLG > Dan., Sw. mudder), fr. a root *meu-, *mu- and ex- tensions, seen in many words with a common notion of ‘wet? or ‘dirty’, as Grk. pbdos ‘damp’, pvdéw ‘be dace boos (*nvdc0s) ‘defilement’, Pol. mut ‘Slime’, Skt. mitra- ‘urine’, Av. miéra- excrement, filth’, etc, Here 
7043:4. Ir. miinaim, miunigim, NIr. mi- naim, with Ir. min ‘urine’ : Skt. mitra- id. (whence denom. miitraya-, but usual- ly mitram kr- lit. ‘make urine’), Av. miora- ‘filth, dung’, MLG modder, NE mud, etc., also Lith. maudytt ‘bathe’, ChSI. myéz ‘wash’, fr. [EH *meu-, *meu-d-, etc. Walde-P. 2.249 f.
7049:fluenced by the words for ‘stall, Stable’) . Grk. craddoow ‘drip’. Walde-P, 2.649 Henry 252. Loth, Rom. 19,593, 5. OHG seichan, MHG seichen (NHG dial. id.), LG séken (sbs. OHG seih MUHG seich), fr. IE *seig-, beside *sei. in ChSl. sicati, Boh. scdti, Pol. szcedg Russ. scat’ : OF séon, OHG sthan, NHG sethen ‘strain, filter’, Skt
7131:Av. miléra- : Skt. mitra- ‘urine’, ete, (4.65).
10941:Skt. mekhald-, perh. as me-kha-la- fr. IE *mei- ‘bind, join’(?) in Skt. mitra, Av. mi@ra- ‘friend’, Hom. pirpy ‘metal waist-guard (Hom.), girdle’. Walde-P. 2.241 f.
15200:Pol. mularz, by dissim. fr. murarz, deriv. of mur ‘wall’, fr. Gme., cf. OHG mitra, ete. (above, 4). Briickner 348.
27697:2. Lat. admiratid (‘wonder, surprise’ and esp. ‘admiration’), fr. (ad-)mitrari ‘wonder at’, beside mirus ‘wonderful’, etc. : Skt. sm7- ‘smile’, etc. (16.25). Cf. esp. Skt. vi-smi- ‘be astonished’, vismita- ‘astonished’, vismaya- ‘astonishment’, smaya- ‘astonishment’ and ‘pride, arro- gance’. The develop
33686:Tr. care : Du. _—vriend Skt. sakhi-, suhrd-, mitra- Nir. cara OHG friunt, wint Av. urvaéa-, haxi-, frya- W. cyfaill MHG ovriunt, win(e) OPers. dauStar-
=== SYN communis
19742:3. Ir. mdin, main, cf. dag-mdini ‘good gifts, benefits’: Lat. minus ‘service, office, gift, etc.’, communis, Goth. ga- mains ‘common’, etc. Walde-P. 2.241. Pedersen 1.57. Thurneysen, Gram. 43.
=== IEC mei
17:5. 1985. 613-772 (Keros-mitros
10834:mir- — mitros (mitlos?)
10846:(mitlos, see mitros. Thus only in Ir. miodal, m. “flattery”)
10850:mitros (mitlos?) (?) “mild, gentle”. Cf. moitis and WP II, 241 Av. cf. miOro ‘god of air or light; Skt. mitráh “friend; friendship’; Li. mitrüs ‘lively’; Ir. cf. miodal, m. ‘flattery’ (?)
```


## [2026-09-07T15:59:03.749Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint('leaves',len(pages))\n# find pages containing 'mitra' / 'maeni'\nfor i,p in enumerate(pages):\n    if re.search(r'mi[tþ0θ]ra|maeni|mai\\?ni', p, re.I):\n        print('---leaf',i, p[:80].replace('\\n',' '))\nEOF",
 "description": "Walde-Pokorny Bd2 locate"
}
```


### [2026-09-07T15:59:05.105Z] TOOL RESULT

```
leaves 725
---leaf 241                                                                me-              
---leaf 244 240                                           mei-    maide „Stange“    mdidit ^
```


## [2026-09-07T15:59:16.915Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (244,245,248,249,250,251):\n    p=t[i]\n    print('=========== leaf',i)\n    print(p[:1400])\nEOF",
 "description": "Print Walde-Pokorny leaves"
}
```


### [2026-09-07T15:59:18.233Z] TOOL RESULT

```
=========== leaf 244
240                                           mei-



maide „Stange“    mdidit ^bestecken, bepfahlen"' (mit -d(hy wie ir. mMe)^
maili „Zauiistecken‘'; mir. mlde „Nacken‘‘ {^mei-d-io-^ Pick II ^ 205);
      moenia „Umwallung, Stadtmauern^ („*Umpfahlung“), mUnio (mocnio),
   lat.

    „aufdammen (einenWeg; ursprgl, vom Priigelweg), aufmauern, ver-
-‘Ire

schanzen, durch eine Mauer (ursprgl. ein Pallisadenwerk) befestigen” (ob
mit Scbwundstufe dazu cymr. mynawyd, bret. minaoned^ mir. menad „Ahle                 5


Pfrieme" als „Stockcben“? Liden AfslPh. 28, 38 f.);
  lat. 7nurus, alt moiros „Mauer‘‘,  womit im Formans nachstverwandt
(Franck KZ. 37, 120ff.) germ, ^mairia- „(Grenz)pfahr' in mnl. mere ^Grenz-
pfabl, Grenzzeichen, Grenze; Pfahl, um etwas festzubinden‘‘, ags. mcere^
(jemdre „Grenze, Gebiet“, engl. nm^e „Eain, Grenze, Grenzstein‘", aisl.
landain^ri „Grenze, Grenzland“, abgel. Verbum ndl. mercn „Grenzpfahle
setzen; an einen Pfahl binden, bes. ein Schiff‘.

   Mit t erweitert              oder wohl genauer m           md it - mit - in
                                                                   \        \



   ai. mUhi- m., metht f. (prakritisch             medht^ mcdht^ s. Trautmann
Germ. Ltges. 53) „Pfeiler, Pfosten”, mit- f. „Saule, Pfosten*' (vielleicht
auch in av. borozi-mita-^ wenn „hochsaulig^‘, Bartholomae Arian. Wb. 961):
lat. meta „(*Pfahl) jede kegel- o
=========== leaf 245
                                           mei-                                            241

  air. moln^ main „Kostbarkeit, Schatz“, dag-moini „gute Gaben, Wohltateii“

Fickll^ 11)6; keine Schwundstufe dazu enthalt air.         „sicher‘' = „ohne
Umwechslung''? Pedersen KG. I 174);
     got. gamains^   ags.   geni^e^ ahd. gimeini „gemein(sain)'^;           als „vertauscht
= verfalscbt“ auch ahd. mein „falsch, trugerisch“ (nhd. Meineid)^ ags. man
„Falschheit, Verbrechen, Frevel“, aisl. meimi „schadlich“, mein „Schade,
Beschadigung, Ungluck‘‘ (Schade Ad. Wb. 599; nicht wahrscheinlicher zu
ai. mayU^ s. u. ma- „wiQkea“)       lit. mamas,
                                     ;
                                                 lett. mains „Tausch“, lit. main-
au^ -yti^ lett. mainit „wechseln, tauschen^*; abg. niena „Wechsel, Verande-
rung'', imihiiti „diajue[^eiv, diakdzTeiv''.  Hieher auch ai. mUni- f. ,,Ra'Che“,
av. 7naeni- „Strafe, Bestrafung" (Berneker II 48 f.       Tgl. abg, mhsih „Ii^che'‘
                                                              ;


von der erw. \Yzf. meit-).
  Ygl. Yf. LEWb.2 u. communis m. Lit, (auch gegen Meringers IP. 18,
270 f. Yerb. mit moenia),
  Erw. Wzf. s. unter mei-g^^ meit-, Persson Wzerw. 15, 28, 156. tJber denk-
bare alte Beziehung zu mei- „niindern" s. d.; da6 auch mei- „meare“ als
„Ortsveranderung'‘ (vgl, migrarc: d/uel^co) ursprungsglei
=========== leaf 248
244                                            mei           meit

8. inei-,    ml        weich, sanft, geliiide; erquicklich, liebreich“; als Basis
      setzt Hirt  Abl. 100 *meiW‘, Reichelt KZ. 39, 10 «ig«- (: me- s. u.) an
      (letzteres fiir ai. mdyas, das wobl nicbt *ni9ios ist, schwierig).
   Ai. mdyas n. „Labsal, Preude, Lust“, dazu *m{i)ies dh{e)- in ai. niiyedha-
m. „Opferspeise“, av. myazda- m. „Opfermal'‘ (unmittelbar von der Wz.
als niei-dho- wobl ai. medha- m. „Fettbruhe, kraftiger Trank“, medJias- n.
„Opfer“, 8. auch zu mad- „na6“, Wiedemann BB. 28, 42         iiber ai. mitrd-          ;


„Preund“ s. u. mei ^„binden“).
   Mit ^-Pormantien lat. ntUis „mild, gelind“; air. moith, moeth „tener“,
CO moithaigidir „emolliat“ (Stokes KSB. 5, 114), cymr. mivydo „erweichen,
mwydion „Weichteile“ (wenn die ir. Worte aus dem Brit, entlehnt sind,
ware im Kelt, nur die Ablautshife           nicbt auch *mvit- vh. Pedersen                            ;


KGr. I 184),           lett.          Johansson IP. 2, 41, Zupitza BB. 25.
                               atme'et .;erweichen“     ;


99 (wo Abgrenzung gegen andere Wzln. der Porm meit).
  Mit H-, 1-, r-Pormantien: air. mJn „sanft, glatt, fein, klein“, cymr. mivijn
„clemens, urbanus, comis, lems“, acorn, muin, moin ,,gracibs“, bret. moan
„dunn, winzig“ (kelt. Abl. l-.ei, Pedersen KGr. I 51, 181: von Pick II*
204 nicbt besser z
=========== leaf 249
                                                     meigu        meigh-                                    245

cyinr. mysgu ,inisclieii“; ahd. misTcan^ ags. miscian „iiiischen'‘ (eher lat.
                          5


Lw. als urverwandt: s Brugmann II^ 3, 35 J, Kluge Weigand-Hirl; s. v.;
dt. 3Iaische usw., die, weun verwandt gegen Entlehnung sprechen konnten,
besser zu abg. m^zga^ s. u. meiyhs „harneii^');
  Lit. maiszafc^ -yti „mischen, inengen% lett. mat sit „inischen, mengen;
zum 2. Mai pfliigen^^ apr, may sot an „gemengt (d. i. bunt)^*, lit. malszalas
j,Gemeugsel“ matsztas „Aufrahr“                          (bait, sz    wie    slav.   s*   in abg. m^siti   kann
            -As-, ksh sein),           mesziu^ meszti ds.                   Osten-Sacken IF.
                                                                   (Belege bei       v. d.

33,         233),    sitmisztu^           snmtszti „sich durcheinandermengen, in Yerwirrung
geraten‘‘ (Praet. snmiszaii   aus dem sAo-Praesens ? Brugmann II ^ 3, 352)
lett.miset „misclien, irremachen'^, alit. mischlnmas j^Yermischung*', lit.
miszriu Adv. ,durcheinander“ (vgl. ai. micrd-)^ lett. mistrs „gemi8cbt“;
                              5


abg.mesrf, mesitl „mischen‘‘, nmcsiti chleh^       (usw., s. Berneker Il52f.).
   Ygl. Curtius 334, Fick I ^ 103, 510, 11^216, III^ 321 £, Pedersen IF.
5, 68,  KG. I 76, Brugmann I^ 568, II
=========== leaf 250
246                                             meigh-, meiq-


ahd. mist                        meox ,Kot, Diinger'^, ags. engl, mixen „Mist-
                           ags, miox,                5


haufe'^ as. mehs n.              mnd. mes, afries. mese ds. (anders Kern IF. 4,
lllf.);      wahrscheinlich hieher die Bez. der nur durch den Mist der Vogel
verpflanzten Mistel,                  mistil,    Sig^.misiel,        aisl.               (Fick IIl^ 320,
Falk-Torp u. Mistel);
  lit. rnlzii (Keubildung fur                              m{szH „harnen% m[zalal. {jnyzalaT) PI,
„Harn“, mlfnis „einer, der piBt“,                  lett,     mejmi und                   Prat, mifii. Inf.
mift „harnen'^ (aber lit. meziit^ mezti „den Diinger bearbeiten*' ist nach
Leskien Abl. 279 vielmehr meziu                  =
                                     lett. mejchii,   mvft; liegt ein dehn-
stufiges Wznomen *ine[i]?jh zugrunde?);
     skr. rniz-uin^       -afi   „harnen“   (i    aus dexn Praes. "^mis-jq yerallgemeinert,
Solmsen KZ. 39, 218 Anm.);
      sloven, mdzi^ m9seti „hervordringen                    (von Flussigkeiten)“, nidzina „Moor-
grund'‘.
  Hieher (Berneker II 54) auch slav. mezga {^moigzghu aus "^nio/gh-sqay
,,Baumsaft“ C^„hervortr6pfelnd“) in skr. mezga, cech, mkha, nnza usw und                            ,


(mit aufgefrischter Tenuis des Formans) mhd. meiscJi „Maische^^, mn
=========== leaf 251
                                   meit-, meit(h)-   — meit hj-                            247


   Wzf. meiq-: osorb. mihac .jblinzeln, blinken'^, mih j,Augenblick“; lat. mico,
-are „schimmern: sich zuckend oder zitternd bin und her bewegen, zappeln
(z.   B. digitis);     baluci micac^    npers. rniia     (pehl.   ^micah) „Augenwimper‘^
(Liden ]P. 19, 333 f.,  wo auch gegen andere Deutungen Yon       mkare).

      B. mit der Bed. „dunkel vor den Augen werden, Nebel, Wolke^^
      Ai. meghd- m. „Wolke‘',        mih „]S[ebel, Dunst, wasseriger       Niederschlag'*,
av. maeya- „WoIke'"; arm. meg (Hiibschmann Arm.-Gr. I 474) „Neber'; gr.
ofjLiyXrj (atfc. Sgtykrj)  „Wolke, IfebePS bom. djuix^aXoEOoav „nebelig, Bei-
wort von Lemnos^ (Vokalvorschlag wie bei den gr. Yertretern von meigh-
„harnen“; an ein Praef. d- als „B^’ii®belung‘‘ ist wohl nicht zu denken):
    ndl. miggden „staubregnen‘‘ (aisl. mistr j,trubes Wetter^ usw. vielleicht
zur verw. Wz. mei-s-^ oder als                hieher);
    lit. migid, 7nygJd „^7ebek‘, lett, migla^ ds. (— djuLt'/Xr}    ob auch ndl. mig-
                                                                      ;


gelen auf ders. Gdf. beruht, mit Kons.-Dehnung vor              ist unsicherer) abg.   ;



rmgld                 russ. mga „Staubregen, Schneegestober, kalter feuchter
Nebek', eecb. mha „Nebel“, russ.           „staubregnen, nebeln“ usw.
```


## [2026-09-07T15:59:29.989Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (246,247,252):\n    print('=========== leaf',i)\n    print(t[i][:1300])\nEOF",
 "description": "WLD mei- binden and meit(h)"
}
```


### [2026-09-07T15:59:31.494Z] TOOL RESULT

```
=========== leaf 246
242                                                   mei*


wechBeInd“ zu ai. mithu usw., Wz. mei- „tau8chen'‘ gestellt); lett. niemuri,
meimuri „die Feinerstricke“. Petersson Studier tillegn. Es. Tegn^r (1918),
226f.

5.   mei- „mindern“; mi-neu-^ Adj.
   Ai. minotif mindtl „mindevt, schadigt, hindert'^ mtyate, mlycitt „inindert
sich, vergeht“ (erweist keine set-Basis          Ptc. mltd-, manyu-nu- „den
Groll       mindemd, vernichtend“;
     gr.        „imadere“, KAy*fxivv-g in /iivv-Cf]ov’ oXiyo^iov Hes., juivv-
(oQtog „kurze   Zeit lebend'S juivvv^a „ein kleines Weilchen, nur kurze Zeit“
{Acc. *iLtivvv, erw. nach dr]-&d, Osthoff MU. VI 232ff.); /ueicov^ jueiov ge-                             ,



ringer“, nach nXeicov fur ^jmelvcov eingetreten, das noch in djLieivcov „besser'‘
=   „*nicht minder^ erhalten ist (Osthoff MK. VI 303 ff.; zugninde liegt ein
St. *mei-no-, dessen komp. Sinn nur durch die Wzbed., nicht das Formans
gegeben war, und der erst nachtraglich auch die Flexion der formantisch
gekennzeichneten Komparative ubernahm); lat. ni-7ms („*nicht zu wenig'^ =)
„allzusehr“, nimius adj. C^ne-nmos); nimis dazu wohl nach satis- s. zuletzt
Osthoff MU. VI 250f., lat. mino7\ n. und AAy, minus „kleiner“ (zur Ent-
wicklung aus dem Adj.                  ausfiihrlich Osthoff MU.
=========== leaf 247
                                                                                                                     ;




                              mei-, meju-, xnm(u)-, miin(ei)-          — mei- cJer mai'                          243

6.mei-, nieiu-, min(u)-, mim(ei)- in Schallnachahmungen fiir helle, diinne
     Tone, Schreie.
  Ai. mimati „blokt, briillt, schreit“, mimayat^ dmlmet „brullte, bl6kte“,
may'd-m „das Bloken, Briillen^ (diese in der Bed. naher zu          s. d.);

vermutlich tnaya- m. „Ro6‘‘ (*„wiehernd‘9>            m. ,Pfau‘‘ (*„schreiend‘‘j;      5


min-mina- „undeutlich durch die Nase sprechend^^
  gr.         jjWiehere^^, fiijui^juog „das ^Yiebe^l“, jui/ud^aoa' yQEjuerioaoa’
(pcovijoaoa         Hes   ,
                               jutvvQog        „wiininernd“, juivvQOfiaij             juivvQi^co   „winsle“:      lat.

mitmr(r)io „zwitschere, girre^^Lw. ?), mhHrio^ -ire „pfeifen, piepen, von
                                                    (gr.
der Maiis“ (wohl nach Niedermann Mel. Saussure 52 Anm. 2 aus inimmo
synkopiertes          ^minrio^              woraus ^ndndrio,           minfrio)\        abg.   nl^)uat^,      luhinati
„stammela‘'.
  Fick KZ. 19, 251, Curtins 335, Schulze                               KZ. 27, 425, Pick                    102,
=========== leaf 252
                                  .           ;                                                       ;




248                                                  ineis>



KZ. 44, 62 an diese Worfce auch lett. mesJut'es „spielen, buhlen“ als
an), av. mat'da^         „scliwankend“
                                       (Lw. aus dem Italischen); vermiit-
  gr. (siziL) fioitog „Yergeltung, Dank’‘
lich    juirog,    geraden nnd ungeraden Faden des Aufzugs‘‘ als „die
                  -ot „die
Wecliselnden“ (Prellwitz KZ. 47, 305; kaum zu fxtxQa^ s. u. met- „binden‘‘);
  lat.  muto, -are „andern, yerandern, tauschen“, miituKs „wechselseitig“
kelt.  yermutlich in dem mit germ, missa- (s. u.) vergleichbaren Praefix
air. mi-^ 77iis(s)- (Fick 11^216; die vollere Form in mis~cids „Ha6“, wor-

nach analogisch miss-imhert „foul play'' nach K. Meyer SBprAk. 38, 793 f.
und briefl. Mitteilung; abweichend von PedersenKG.il, 10         lat.        mit   =
-mis angeblieh aus          zu mei- „mindera"; doch ist nhnis eher erst nach
satis zu nimius neugeschaffen);
   got. maidjan „yerandern, verfalschen" (zu scheiden von aisL nielda j,ver-
letzen" usw., s. u. mai- „hauen“), mmaidjan ,,verwandeln“           got. niaipms       ;


„Geschenk“, aisl. pi. meidmar, ags. mapmn, as. methom „Geschenk, Kost-
```


## [2026-09-07T15:59:50.554Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN 1000\"; sed -n '8690,8705p' HRN.txt | cut -c1-300\necho \"=== HUB mihr\"; sed -n '7265,7290p' HUB.txt | cut -c1-300",
 "description": "Horn and Hübschmann mihr context"
}
```


### [2026-09-07T15:59:50.607Z] TOOL RESULT

```
=== HRN 1000
phlv. mas gross, grösser, grössest', masist, mas(i)st,
vergl. 7nas[mayan *Grossmagier (AlbSnlnl), masTh%
mahist, päz. meh (PPGL); arm. vergl. mec gross' (H.
No. 191).
af/. masar 'älter, Herr*.
Vergl. zu bih (No. 241).
1000. mihr *Sonne; Liebe', mihr[ban 'freundlich, wohl-
wollend*.
ap. Mid^ra^, vergl. Vaulmisa-; aw. Mi&ra-, mi&ra^
'Vertrag*; phlv. mür, päz. mihir (vergl. Meherdates,
Tac, MsQfiBQorig^ Proc, skr. LW. mihird- *Sonne');
ai. Mitrd", mitrd- 'Freund*.
minj. mira 'Sonne.
1001. muhr 'Siegel; Siegelring,
skr. mudrd- 'Siegel, Siegelring; phlv. mutrOk d. i.
mudrak 'B,ing'(?), vd. 2 (18) Gl.^), nmdar, muhr 'Siegel'
=== HUB mihr
Hier handelt es sich vielleicht nur um Umsohreibung der Zendworter,
vgl. phi. x^aniras = zd. x^anira&a-, levafeh-ras = zd. maUa&a-, ^
*) Vgl. np. hazar = ap. *hazahra', zd. hazanra', skr. sahasra-
u. 8. w., 8. § 9, d.
•) Aus *pahra gekilrat.— 205 —
pahak *Wachter, pahakapan-K *Wache, Besatzung, syr.
pahragban 'Wache', talmud. KiD^ims *Polizeidirektor' (Hoff-
mann, Auszuge p. 97, Anm. 8G6), zd. paOra- *Schutz*;
mihr 'Sonne, Liebe, paz. mihir Sonne*, N. pr. Mihir-ayar
Shk. 258, phi. M(i)tru (historische Schreibung fiir alt arsac.
*Mi9^r, spater Mihr), arm. Mihr, das auch in den Ab-,
leitungen mrhakan (Agath.), mihrakan (Mos. Kalank.)
und in vielen Namen vorliegt: Mihr-Nerseh (Elise), Mihr-
V
Sapuh, Mihr-Vsnasp'^) (Laz. Pharp.), Merhevandak (Se-
beos 30) = Mehrevandak (Thomas 85), Mehruzan (EliSe,
Laz. Pharp.) = Merhnzan, Meruian, Mehuzan; Zarmihr-)
(Laz. Pharp.) ^i= p. Zarmihr Tab. 135; Mihrdat (Pseu-
docall. 94, 100, Mos. Chor.) = i\^, MUad aus '^Mi(h)rdat,
phi. M(i)trd(a)t(a)n (zu sprechen Mihrdatan) ZDMG, 44, 660,
lat. Meherdates (Tacitus), alter lat. Mithtidates = gr.
Mt^Qiddrtjg, Mi^gaddvfjg, bei Herpdot Mizpa^drrjg (ein
Meder), zd. midra-f ap. tnidra-; sahr 'Stadt*, alter *Land',
paz. sahar 'district, country' Shk. 266, Min. 61. 184, phi.
s{a)tru, chald. phi. xs[a)tr' (historische Schreibung fiir alt-
ars. *xsadr, spater sahr), arm. sahr in sassanidischen Namen
```


## [2026-09-07T15:59:52.724Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON komonism headword\"; grep -n \"^کمونیسم\\|کمونیسم:\" MON_part1.txt MON_part2.txt | head -5 | cut -c1-400\ngrep -n \"کمونیس\" MON_part1.txt | head -8 | cut -c1-300\necho \"=== RCH samt\"; grep -n -i \"samt\" RCH.txt | head -8 | cut -c1-250\necho \"=== SKT mad/mean/migrate\"; grep -n -E \"^(Mad|Mean|Migrate)\" SKT.txt | head -8 | cut -c1-400",
 "description": "Mo'in komonism, Richardson samt, Skeat"
}
```


### [2026-09-07T15:59:52.855Z] TOOL RESULT

```
=== MON komonism headword
31963:ممالکك کمونیست مانند روسیهٌ شوروی و 
31964:ممالکك کمونیست اروبای شرفی و چین 
49758:دست چپی» طرفدار سوسیالیسم و کمونیسم. 
=== RCH samt
5631:A   asamt^  (pi.  of  ism)  Names,  a   A   dependant,  a
28635:O   The  fourth  letter  of  the  Arabic  alphabet  (being  never  used in  words  of  I’ersian  origin).  In  arithmetic  it  expresses  600. The  legitimate  power  of  this  character  appears  to  be  that  of  th in  the  English  word  
33685:which  are  scarcely  ever  free  from  dust.  Husamtyy  Very  hairy.
42073:A   samtm,  Blamed,  blamable.  Bad,  depraved..  Loath- some, unwholesome  water.  Eruptions  on  the  face  frpm  heat.  A pimple  under  the  nose.  Milk  running  from  the  dugs,  or  snot from  the  nose.  A   well  containing  little,  o
49643:A   simdjy  (pi.  of  samjy  samijy  and  samtj)  Rich
49689:A   y^£<w  stetiM,  (pL  samtn)  Fat.  Aa/Mman,  A   seller
49710:ACUvAm*  samt  (from  tju«v4nwi),  Travelling.  Groping  along.  j Guessing  the  way.  A   way,  road,  path  ;   a   part,  tract,  country,  or quarter.  Towards.  The  right  way,  the  path  of  probity,  j
49712:m   Of*  samty  The  azimuth.  ^   ohittna  $am^  ]
=== SKT mad/mean/migrate
10877:Mad.  (E.)  The  vowel  was  formerly long.  M.  E,  maad,  made,  —  A.S.  n^m^J, gg-maad,  tn  a  gloss ;  heocc  rndd-mM.  mad- ness (Grein).  -f-  O.  Sax.  ^-mJd.  foolish  ; O.  H.  G.  •^i-meii,  vain ;  Icel.  meiddr,  pp.  of meitSa,  to  maim,  hurt;  Goth.  jpa-ntaSds, maimed.  The  orif;.  sense  seems  to  be •severely  injured;'  the  prefix  .^e-,  ^-,  gU' is  unes^ntia
10878:Madam,  my  lady.  (F.-L.>  V.  madam/, i.e.  ma  dame,  my  lady. —  L.  w/ra  dffmina^ my  lady;  sec  Dame.
10880:Madder,  a  plant  (E.)  M.K.  mader^ madir.  A.  S.  maderu.  madert.  ^  Icel. mt^ra.  Dp,  ntetd.  Cf.  Ski.  madhtira, ■weet,  tender :  whence  fern,  madkurd,  the Dame  of  several  plants.
10882:Madrepore,  coral.  <F.  —  Ital.»I«  and Gk.)  F.  madn'pon.  —  ItaL  madre/era. The  lit  seaic  it  '  ■wClier<«tooc,'  a  fondful
10885:Madrigal,  a  pastoral  song.  (Ilal.  — L Gk.)  Iial.  madrigaU,  i  short  song, pastoral  ditty  ;  put  for  mandn\fa/i Florio  also  gives  mardfia/i,  mandnan* a  hetdftiuan,  also  a  madrigal.  —  Ital, mandra,  a  herd,  flock.  —  L.  ntandra stall,  stable.- Gk.  ^f?/>a.  a  foM -f  Ski matidura,  stable;  frum  mand,  to  slcef (The  suffix  -ijc^-aU"  1.   MiTix  -ft  a/u.
11312:Meander,  a  winding  course.  (L— Gk.) L.  j(AruW/r.  —  Gk.  Mafai'^wi,  a  winding Ktream  :   Pliny,  v.  39.
11542:Migrate.  (L.)  From  pp.  of  L.  migrartf to  wander ;  allied  to  mean,  to  go.
13034:Meant.  (F.  -  L.)  O.  T.paisant,  an- tr  form  of  O.  F.  paisan,  a  peasant ;  (cf. ^  fauaHff,^{'9n. ptusano,  acom-patiiot). ■mcA  with  sq/Tik  -dn  (L.  -hhuj),  from pmis    (K. /or;),  a  country  (cf.  ItoJ.
```


## [2026-09-07T16:00:09.290Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%85%D9%88%D9%86%DB%8C%D8%B3%D9%85/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for کمونیسم verbatim including any origin tag in brackets such as [فر.] (French), and quote the Dehkhoda entry opening if present. Also say whether the spelling کمونیزم appears."
}
```


### [2026-09-07T16:00:15.321Z] TOOL RESULT

```
# Farhang-e Mo'in Entry for کمونیسم

**Quote from Farhang-e Mo'in:**
"(کُ مُ ) [ فر. ] (اِ. ) مکتبی است که از نظر فلسفی و اقتصادی بر مالکیت عمومی وسایل تولید تکیه می کند"

This entry indicates the term originates from French [فر.].

**Dehkhoda Entry Opening:**
"کمونیسم. [ ک ُ مو / م ُ ] ( فرانسوی، اِ ) رجوع به کمونیزم شود."

The Dehkhoda entry directs readers to refer to the spelling **کمونیزم**, indicating that variant spelling does appear in the dictionary's cross-references.
```


## [2026-09-07T16:00:27.086Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D8%AA|page 327 entry 0 nodes 3-4: Arabic samt < Aramaic sēmiṭā < Latin sēmita; Persian samt < Arabic\" \\\n \"https://www.etymonline.com/word/zenith|page 327 entry 0 nodes 5-6: zenith/azimuth from Arabic samt/as-sumut, Latin semita\" \\\n \"https://www.etymonline.com/word/communism|page 327 entry 0 nodes 8-10: French communisme c.1840 < commun < L. communis\" \\\n \"https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%B1|page 327 entry 1 node 2: Persian mehr < MP mihr < Av. miθra\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-|page 327 roots Mei 3 and Mei 4: the PIE *mey- homonyms and their Pokorny pages\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mitra|page 327 entry 1 root and node 1: *mitra 'that which binds' < *mey- 'to bind' (Pokorny) vs Meillet 'exchange'\" \\\n \"https://www.etymonline.com/word/Mithras|page 327 entry 1 nodes 3-5: Latin < Greek Mithras < Avestan Miθra-\" \\\n \"https://abadis.ir/fatofa/%D8%B3%D9%85%D8%AA/|page 327 entry 0 node 4: Mo'in's سمت entry, tag [ع.] = Arabic\" \\\n \"https://abadis.ir/fatofa/%DA%A9%D9%85%D9%88%D9%86%DB%8C%D8%B3%D9%85/|page 327 entry 0 node 9: Mo'in's کمونیسم entry, tag [فر.] = French\" ; do\n  url=\"${u%%|*}\"; note=\"${u#*|}\"\n  python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-07T16:00:34.211Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/140845579911c711.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/60ecf710d5ca6180.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/287c2c9664cae2d4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/575d3fb94b2360ed.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/caebb6dff6cb9f09.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a3ccc9880b2a6387.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/37efc003651084e4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ada3ebf7dc6b1632.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/854931f1b8f7533c.txt
```


## [2026-09-07T16:01:31.744Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN samt\"; grep -n -i \"samt\" HRN.txt | head -5 | cut -c1-200\necho \"=== HUB samt\"; grep -n -i \"samt\" HUB.txt | head -5 | cut -c1-200\necho \"=== ARY mehr\"; grep -n \"مهر\\b\" incoming/ARY/ARY_pages.txt | head -5 | cut -c1-300\necho \"=== ARY latin index MITHRA\"; grep -n -i \"mithra\\|MEHR\" incoming/ARY/ARY_latin_index_pages.txt | head -8 | cut -c1-200\necho \"=== ARY samt\"; grep -n \"سمت\" incoming/ARY/ARY_pages.txt | head -4 | cut -c1-200",
 "description": "Horn/Hübschmann/Aryanpur checks"
}
```


### [2026-09-07T16:01:31.851Z] TOOL RESULT

```
=== HRN samt
62:Den gesamten Buchtext können Sie im Internet unter |http: //books . google .corül durchsuchen.■ /
=== HUB samt
82:Dialectformen ^) zeigen, die samtlich a haben. Zd.
5379:p. 612), np. yasamtn, phi. ydsmln (Bdh. Gl. 285); yavanak,
=== ARY mehr
13075:ایتالیایی (/(0744): ها00 6 (31380۸5) :23/لعل مهر
14464:۸ / میتراه مهر :
15488:انگلیسی کهن (نتولن2۸/0 صا۵): ۱80۸0۷ 1۲80719 :مه #3متتمهر
=== ARY latin index MITHRA
14200:MITHRA NAVESTAN) «glgh ;
14201:‘REFERENCES - beth MITHRA — (OLD PERSIAN) jj, |
14204:THE AMERICAN HERITAGE MEHR AFGHANI) (24) gail
=== ARY samt
709:وهسانی اقلیمی این سرزمین‌ها با فلات ایران» کوج اقوام ایرانی از مسیر آسیای مرکزی به سمت
4052:۰ ا بهر (به چم "سهم" "قسمت"* و "حصه») .
8247:چم این واژه در همه‌ی زبان‌های اپن فهرست (به جز فارسی امروزی): دست راست یا سمت راست» مهارت» ماهر.
11792:پهلری (الاماتلوم: ز نی (تی) (اسمتاتمم: ‏ 0987 ,۲3830
```


## [2026-09-07T16:01:38.146Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find pdf page tag before line 14200\ntag=None\nfor i,l in enumerate(lines):\n    m=re.search(r'\\[pdf page (\\d+)\\]',l)\n    if m: tag=m.group(1)\n    if 14190<=i+1<=14215:\n        print(i+1, tag, l[:160])\nEOF",
 "description": "ARY entry for MITHRA"
}
```


### [2026-09-07T16:01:39.474Z] TOOL RESULT

```
14190 486 : REFERENCES beth MYGHK * (SOGHDIAN) gt
14191 486 POKORNY, SSSS™S~*~«SOD MAYOKHA = <(ANSKRIT) cy Se
14192 486 MACKENZIE: (NAIL) 124 MOENIA, MOENIUM — (LATIN) fet ,
14193 486 ner soo oby 4OLD $EANDINAVIAN) pS.s.thng
14194 486 Jeelaal
14195 486 . Sorel 2o2V O85 22 05s cal
14196 487 [pdf page 487]
14197 487 MITRA (NAME OF A GOD), KINDNESS, AFFECTION, 31 503) 0 gulS a f
14198 487 AMITY, FRIENDS! HIRX LOVE . ;
14199 487 ye or a |
14200 487 MITHRA NAVESTAN) «glgh ;
14201 487 ‘REFERENCES - beth MITHRA — (OLD PERSIAN) jj, |
14202 487 POKORNY: n0 MITR, MITHR, MIHR:(PAHLAV1) 154 !
14203 487 AMINDAROV: (MIHR) 117 MIHR (KURDISH) 52,5 *]
14204 487 THE AMERICAN HERITAGE MEHR AFGHANI) (24) gail
14205 487 DICTIONARY OF THE ENGLISH SANSKRIT) ey Sila
14206 487 LANGUAGE: (MEI-) 2073 MITRA., MITRAH
14207 487 VoPe-ToPd sbi oly MITRHE GREEK) gli y
14208 487 rrr foe Kad LATVIAN) (5) 3.)
14209 487 MIEMURI, MEIMURI
14210 487 OMIKHEO GREEK) 3h y MEZAITI, MAEZ, AVESTAN) gu)!
14211 487 MICTUM, MINGO, X(LATIN) 3’ =~ MAESMA, MIZ-
14212 487 MINGERE (GO-)MIZ, MISTAN, :(PAHLAVI) 5. hy
14213 487 MEAR (SPANISH) gilt MIZTTAN
14214 487 MATHSTUS GOTHIC) S35 MEZUM, MIZIN —:(OSSETIC) ay!
14215 487 OLD SCANDINAVIAN) She) ‘MIZ, MIZTIN, (KURDISH) 63,5
```


## [2026-09-07T16:01:50.055Z] TOOL CALL #73: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg327.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/327.png\nls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5",
 "description": "Copy page image for audit"
}
```


### [2026-09-07T16:01:50.128Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-07T16:02:07.489Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:10:57.510Z] TOOL CALL #74: Bash

```json
{
 "command": "cat > /home/sfmqrb/git/rishe/data/verification/page-327.json <<'JSONEOF'\n{\n  \"pdf_page\": 327,\n  \"book_page\": 297,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Mei 3, Meih; Meigw; Moin\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *mey- 'to change, exchange; to go, pass' — Pokorny's 2. mei- 'wechseln, tauschen' (p.710), 3. mei- 'wandern, gehen' (p.710), the extension mei-gʷ- 'tauschen' (p.713) and 2. mei-t(h)- 'tauschen' (p.715); Watkins/AHD mei-1 'To change, go, move', with the suffixed o-grade *moi-n- of *ko-moin-i- 'held in common'\",\n      \"note\": \"The root box is accurate to an unusual degree: Nourai's three Pokorny pages (710, 713, 715) are exactly the three references Watkins prints under mei-1 ('[Pok. 2. mei-, 3. mei- 710, meigʷ- 713, 2. meit(h)- 715]'), so 'Mei 3, Meih' = Pokorny's mei-2/mei-3 (change + go), 'Meigw' = mei-gʷ- (migrāre), and 'Moin' = the o-grade -n- extension *moi-n- seen in *ko-moin-i- > Lat. commūnis, Goth. gamains. Two small caveats: (a) 'Moin : common' gives the meaning of the derivative, not of the root, which is still 'exchange' (WP II 241 glosses gamains as 'vertauscht'); (b) fusing 'to go' with 'to change' is a scholarly judgement, not an observed fact — Walde–Pokorny state it as a possibility ('daß auch mei- \\\"meāre\\\" als \\\"Ortsveränderung\\\" ... ursprungsgleich', WP II 241) and Klein asserts it outright ('Base *mei-, \\\"to change\\\", is originally identical with base *mei-, \\\"to change one's place, to go\\\"', KLN:953), and both Wiktionary and Watkins now treat them as one root. Two forms on the page are misprints of the book itself (nodes #2 and #7); everything else in the chart is standard.\",\n      \"note_fa\": \"جعبهٔ ریشه درست است: نورایی سه صفحهٔ پوکورنی (۷۱۰، ۷۱۳، ۷۱۵) را می‌آورد و این همان سه ارجاعی است که واتکینز در ذیل mei-1 «تغییر یافتن، رفتن، جنبیدن» می‌دهد؛ پس «Mei 3, Meih» = mei-2/mei-3 پوکورنی (تبادل + رفتن)، «Meigw» = mei-gʷ- (لاتینی migrāre) و «Moin» = گونهٔ o-دار *moi-n- در *ko-moin-i- «مشترک» که لاتینی commūnis و گوتی gamains از آن است. دو نکته: نخست آنکه معنای «مشترک» معنای مشتق است نه معنای ریشه؛ دوم آنکه یکی‌دانستن دو ریشهٔ «رفتن» و «تبادل کردن» داوری پژوهشگران است — والده‌پوکورنی (جلد ۲ ص ۲۴۱) آن را «ممکن» می‌شمارد و کلاین (ص ۹۵۳) صریحاً یکی می‌داند، و ویکی‌واژه و واتکینز نیز امروز آن‌ها را یک ریشه می‌گیرند. دو صورت روی این صفحه (گره‌های ۲ و ۷) غلط چاپی خودِ کتاب است؛ بقیهٔ نمودار استاندارد است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:710\", \"status\": \"supports\", \"note\": \"POK_full.txt has both lemmas on p.710: 'Root / lemma: meih-2, Meaning: to change, exchange ... Latin mūnus ... communis (old Latin comoinem) ... Gothic gamains, Old English gemaene, Old High German gimeini \\\"common, shared\\\" ... Here also Old Indic menī- \\\"revenge, vengeance\\\", Avestan maēni- \\\"punishment\\\" ... Page(s): 710' (l.58298ff.) and 'Root / lemma: meih-3, Meaning: to wander, go, Material: Latin meo, -are \\\"to go, pass\\\" ... The relationship migrāre : ἀμείβειν allows the old resemblance with mei- \\\"swap, vary, exchange\\\" as \\\"local change\\\" seem possible. Page(s): 710' (l.58337ff.). Exactly Nourai's 'Mei 3, Meih : to go / to move, change'.\"},\n        {\"ref\": \"POK:713\", \"status\": \"supports\", \"note\": \"POK_full.txt l.58198: 'Root / lemma: meih-gʷ-, Meaning: to exchange, Material: Gr. ἀμείβω \\\"change\\\" ... Latin migro, -are \\\"to remove, depart, flit, migrate ... change\\\", Denom. of *migʷ-ros ... See also: extension from mei- \\\"swap, vary, exchange\\\". Page(s): 713' — Nourai's 'Meigw'.\"},\n        {\"ref\": \"POK:715\", \"status\": \"supports\", \"note\": \"POK_full.txt l.58524: 'Root / lemma: meih-t(h)-2, Meaning: to exchange, Material: Old Indic methati, mithati \\\"alternates, quarrels\\\" ... = Avestan miθō Adv. \\\"inverted, incorrect\\\"; ... Avestan miθwa(na)-, miθwara- \\\"paired, coupled\\\" ... prefix Gothic missa- \\\"wrong, incorrect\\\" ... Page(s): 715' — the source of two of the four Avestan words in node #1 and of Germanic missa- in node #12.\"},\n        {\"ref\": \"AHD:1528\", \"status\": \"partial\", \"note\": \"The 1975/76 New College appendix (pp.1505-1550) is not open online, but the same Watkins list in the 1985 standalone edition (AHD_watkins1985.txt l.734) reads: 'mei-1. To change, go, move; with derivatives referring to the exchange of goods and services within a society as regulated by custom or law. 1. Latin meāre, to go, pass ... 2. ... Germanic *ga-maid-az ... \\\"changed (for the worse)\\\" ... 3. ... Germanic *missa-, \\\"in a changed manner\\\" ... 4. Suffixed o-grade form *moi-n- in compound adjective *ko-moin-i-, \\\"held in common\\\" ... a. Germanic *gamainiz ... MEAN2; b. Latin commūnis ... 6. Extended form *(a)meigʷ- in ... b. Latin migrāre ... [Pok. 2. mei-, 3. mei- 710, meigʷ- 713, 2. meit(h)- 715.]'. Content confirmed; only the 1976 page number itself is unverifiable.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"WLD\", \"where\": \"Bd. II 240-241 (leaves 244-245 of WLD_Bd2_pages.txt) and Bd. II 248 (leaf 252)\", \"stance\": \"supports\", \"note\": \"p.241: 'got. gamains, ags. gemǣne, ahd. gimeini \\\"gemein(sam)\\\"; als \\\"vertauscht = verfälscht\\\" auch ahd. mein \\\"falsch, trügerisch\\\" (nhd. Meineid) ... Hieher auch ai. menī- f. \\\"Rache\\\", av. maēni- \\\"Strafe, Bestrafung\\\"' and, at the foot of the same page, 'daß auch mei- \\\"meāre\\\" als \\\"Ortsveränderung\\\" (vgl. migrāre : ἀμείβω) ursprungsgleich...'; p.248 has the meit- lemma with 'lat. muto, -are \\\"ändern\\\" ... got. maidjan \\\"verändern, verfälschen\\\" ... germ. missa-'.\"},\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mei-1 (AHD_watkins1985.txt l.734)\", \"stance\": \"supports\", \"note\": \"see ref_check AHD:1528 — the whole shape of Nourai's entry 0 (Latin, Germanic and Romance branches) is Watkins' mei-1 rearranged.\"},\n        {\"src\": \"KLN\", \"where\": \"p.953 s.v. 'mean, of low rank' and p.336 s.v. 'common' (KLN_1966.txt leaves 511, 180)\", \"stance\": \"supports\", \"note\": \"'mean ... rel. to ... Goth. ga-mains, \\\"common\\\" ... cogn. with L. mūnus (OL. moinos, moenus) ... commūnis (OL. acc. comoinem), \\\"common\\\" ... OI. menīḥ, \\\"vengeance\\\", Avestic maeni-, \\\"punishment\\\". All these words derive fr. I.-E. *mein-, *moin-, -n-enlargements of base *mei-, *moi-, \\\"to change, exchange\\\" ... Base *mei-, \\\"to change\\\", is originally identical with base *mei-, \\\"to change one's place, to go\\\". See meatus, migrate.'\"},\n        {\"src\": \"SYN\", \"where\": \"Buck, SYN.txt l.19742 (§11.x, 'gift/service')\", \"stance\": \"supports\", \"note\": \"'Ir. máin, main, cf. dag-máini \\\"good gifts, benefits\\\": Lat. mūnus \\\"service, office, gift, etc.\\\", commūnis, Goth. gamains \\\"common\\\", etc. Walde-P. 2.241.'\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"maëni; mithô; mithwara; mithahya\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All four are genuine Avestan forms, and all four hang on the *mei- 'exchange' family, though from two different sub-lemmas. (1) maēni- f. 'punishment, retribution' (Y. 44.19 kā tōi ahyā maēniš aŋhat pouruyē 'what will be the punishment of this?') is the -n- extension *moi-n-/*mei-n-, semantically 'requital = what is given in exchange'; Old Indic menī- 'vengeance' is its exact cognate (Pokorny 710; WP II 241; Klein p.953 cites it under 'mean'). (2) miθō adv. 'falsely, wrongly' and (3) miθwara- (also miθwana-) adj. 'paired, coupled' belong to Pokorny's mei-t(h)-2 'to exchange' (p.715) beside Old Indic mithás 'mutually', mithuyā 'falsely' — the semantics run 'interchanged' > 'reciprocal, paired' and 'interchanged' > 'altered' > 'false', the same shift that gives Gothic missa- and English mis-. (4) miθahya- 'evil, false' is the -hya- adjective of miθah- n. 'evil' (Kent: 'miθah- sb. \\\"evil\\\", the opposite of ṛtāva-: Av. miθahya- \\\"evil\\\", miθaoxta- \\\"falsely spoken\\\"', from OP DNb 7,9,11), same root. Nourai's glosses are right; only the transliterations are old-fashioned (maēni, miθō, miθwara, miθahya).\",\n          \"derivation_fa\": \"هر چهار صورت اوستایی اصیل‌اند و همه به خانوادهٔ *mei- «تبادل کردن» می‌رسند، امّا از دو زیرریشهٔ متفاوت. maēni- «کیفر، مکافات» (یسنا ۴۴٫۱۹) از گسترش -n- دار *moi-n- است و از نظر معنایی «آنچه در برابر داده می‌شود» یعنی سزا؛ هم‌ریشهٔ دقیقش سنسکریت menī- «انتقام» است (پوکورنی ۷۱۰، والده‌پوکورنی ۲/۲۴۱، کلاین ۹۵۳). miθō «به دروغ» و miθwara- «جفت، دوگانه» به ریشهٔ mei-t(h)-2 پوکورنی (ص ۷۱۵) تعلق دارند، در کنار سنسکریت mithás «متقابلاً»؛ تحول معنایی «جابه‌جاشده» به «متقابل/جفت» و «جابه‌جاشده» به «دگرگون» و سپس «دروغ» است، همان تحولی که در گوتی missa- و پیشوند -mis انگلیسی دیده می‌شود. miθahya- «بد، دروغ» صفتِ miθah- «بدی» است (کنت ذیل miθah-، در برابر ṛtāva-). ادعای نورایی در این گره درست است؛ تنها آوانگاری‌ها قدیمی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:710\", \"status\": \"supports\", \"note\": \"'Here also Old Indic menī- \\\"revenge, vengeance\\\", Avestan maēni- \\\"punishment\\\"' (POK_full.txt, lemma meih-2, p.710).\"},\n            {\"ref\": \"POK:715\", \"status\": \"supports\", \"note\": \"'Old Indic mitha- Adv. \\\"mutual, alterant, changeable, together\\\" = Avestan miθō Adv. \\\"inverted, incorrect\\\"; Old Indic mithás, mithuyā Adv. ds., Avestan miθwa(na)-, miθwara- Adj. \\\"paired, coupled\\\"' (POK_full.txt, lemma meih-t(h)-2, p.715) — covers Nourai's mithô and mithwara exactly.\"},\n            {\"ref\": \"KLN:953\", \"status\": \"supports\", \"note\": \"Klein s.v. 'mean, adj., of low rank, inferior, base' (KLN_1966.txt leaf 511; with the vol.-II leaf offset this is printed p.~954, i.e. Nourai's 953): '... OI. menīḥ, \\\"vengeance\\\", Avestic maeni-, \\\"punishment\\\". All these words derive fr. I.-E. *mein-, *moin-, -n-enlargements of base *mei-, *moi-, \\\"to change, exchange\\\".'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. maēni- (form quoted in BRT.txt ll.8850 and 11741)\", \"stance\": \"partial\", \"note\": \"the OCR of the headword column is unreadable, but Bartholomae's text quotes the passage twice in the reading Nourai's gloss depends on: 'kā tōi ahyā *maēniš (sd.) aŋhat paouruyē Y. 44.19' (l.8850, under ka-) and '*mainis (sd.)' (l.11741) — i.e. the word is registered as an Avestan noun of Y.44.19.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. miθah- (KNT.txt leaf 227 = printed p.~203)\", \"stance\": \"supports\", \"note\": \"'miθah- sb. (§156.II) \\\"evil\\\", the opposite of ṛtāva-: Av. miθahya- \\\"evil\\\", miθaoxta- \\\"falsely spoken\\\", Skt. mith- \\\"to meet (as friend or antagonist), engage in altercation\\\"' — the direct source for Nourai's 'mithahya : evil'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 241 (leaf 245)\", \"stance\": \"supports\", \"note\": \"'Hieher auch ai. menī- f. \\\"Rache\\\", av. maēni- \\\"Strafe, Bestrafung\\\" (Berneker II 48 f.; vgl. abg. mьstь \\\"Rache\\\" von der erw. Wzf. meit-).'\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Latin\",\n          \"words\": \"se-mitita\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"There is no Latin *se-mitita. The word is sēmita, -ae f. 'footpath, side path, pavement', and the printed page really does show 'se-mitita' — a dittography of -ti- in the book itself, not a misreading by the extraction (see the 600 dpi crop of the page). The etymology Nourai intends is Klein's: 'L. semita prob. stands for *se-mita, fr. sed-, se, \\\"aside\\\", and *mita, fr. meāre, \\\"to go\\\"' (KLN p.1767 s.v. zenith), i.e. sē- 'apart' + the zero-grade *mit- of *mey- 'to go' — 'the way that goes off to the side'. That analysis is Klein's and Watkins' (Latin meāre under mei-1) but is not universally accepted: Ernout–Meillet print sēmita with the bare verdict 'Sans étymologie' (LAT.txt l.57148ff.), and Etymonline says only that the Medieval Latin form 'may also connect to classical Latin semita'. So: the arrow PIE *mey- > Latin sēmita is plausible-to-accepted, but the form as printed is corrupt.\",\n          \"derivation_fa\": \"در لاتینی صورتی به شکل *se-mitita وجود ندارد؛ واژهٔ درست sēmita «راهِ پیاده، کوره‌راه، پیاده‌رو» است. تصویر ۶۰۰ نقطه‌ای صفحهٔ چاپی نشان می‌دهد که خودِ کتاب «se-mitita» چاپ کرده است؛ پس خطای چاپی کتاب است و خوانش اسکن درست بوده. تحلیلی که نورایی در نظر دارد از کلاین است: sēmita از پیشوند sē- «جدا، به کنار» و *mita از ستاک meāre «رفتن»، یعنی «راهی که به کناره می‌رود». این تحلیل پذیرفتهٔ کلاین و واتکینز است ولی همگانی نیست: ارنو–مه‌یه در فرهنگ ریشه‌شناسی لاتینی زیر sēmita تنها می‌نویسند «بی ریشه‌شناسی» و اتیمانلاین هم فقط می‌گوید «شاید» با semita مربوط باشد. کوتاه: پیوند ریشه با *mey- پذیرفتنی است، امّا صورت چاپ‌شده مخدوش است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"se-mitita\",\n          \"correct_form\": \"sēmita (Klein's analysis *se-mita)\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/zenith\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1767\", \"status\": \"supports\", \"note\": \"Klein s.v. zenith (text from KLN_1971.txt l.270434ff., printed p.1767 of the 1966 ed.): '... fr. VArab. semt, corresponding to Classical Arab. samt, \\\"way, path\\\" ... fr. L. se-mita, \\\"path, way\\\". ... L. semita prob. stands for *se-mita, fr. sed-, se, \\\"aside\\\", and *mita, fr. meare, \\\"to go\\\". See se- and meatus.' Klein hyphenates 'se-mita' exactly as Nourai's box tries to; the extra -ti- is the book's slip.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. semita (LAT.txt l.57148)\", \"stance\": \"contradicts\", \"note\": \"'semita, -ae f.: chemin de piéton, sentier, trottoir (= crepido). Ancien (Enn.), usuel. Panroman (sauf roum.), M.L.7813. Dérivés rares: semitalis ... Sans étymologie.' — Ernout–Meillet decline the *sē- + *mit- analysis altogether.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mei-1, §1\", \"stance\": \"partial\", \"note\": \"'1. Latin meāre, to go, pass: MEATUS; CONGE, IRREMEABLE, PERMEATE.' Watkins lists the verb meāre under mei-1 (which is what sēmita would be built on) but does not itself cite sēmita.\"},\n            {\"src\": \"LEW\", \"where\": \"Walde 1910 (LEW_1910.txt), grep 'semita' and 'migro'\", \"stance\": \"silent\", \"note\": \"no hit for either headword in the local OCR of the 2nd edition; the entry could not be reached in this copy.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"samt; as-sumut\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Arabic سَمْت samt 'way, road, direction; azimuth', pl. سُمُوت sumūt (with the article as-sumūt 'the ways'), is real and its astronomical use (samt ar-raʾs 'the way over the head' = zenith, samt al-qadam = nadir) is what carried it into Europe. Nourai's arrow Latin > Arabic follows Klein, who derives samt straight from L. sēmita. Modern treatments are more careful in two ways: Wiktionary routes it through Aramaic — 'From Aramaic סֵימִטָא (sēmiṭā), from Latin sēmĭta, but later reanalysed as deriving from an Arabic root س م ت (s m t)' — which is the normal channel for Latin words in pre-Islamic Arabic, and the native reanalysis explains the wholly Arabic-looking pattern and the derived senses ('gravity, staidness', 'mode of conduct'); Lokotsch (no. 1818) and the Arab lexicographers simply treat samt as Arabic. So the direction of borrowing is accepted, but with an Aramaic intermediary and with a caveat that many Arabists consider samt native to س م ت. Hence 'plausible' rather than 'confirmed'.\",\n          \"derivation_fa\": \"واژهٔ عربی «سَمْت» به معنای «راه، جهت؛ سمت الرأس (اوج)» و جمع آن «سُمُوت» واقعی است، و کاربرد نجومی آن (سمت الرأس «راهِ بالای سر») همان است که واژه را به اروپا برد. نورایی پیکان لاتینی > عربی را از کلاین گرفته که samt را یکسر از sēmita لاتینی می‌گیرد. پژوهش امروزی دو احتیاط می‌افزاید: ویکی‌واژه آن را از راه آرامی می‌داند («از آرامی sēmiṭā، از لاتینی sēmita، که بعدها به ریشهٔ عربی س م ت بازتحلیل شده») — که مسیر معمول وام‌واژه‌های لاتینی در عربی پیش از اسلام است و بازتحلیل عامیانه، وزن کاملاً عربی و معناهای مشتق («وقار»، «روش رفتار») را توضیح می‌دهد؛ و لوکوچ و لغویان عرب samt را بی‌درنگ عربی می‌شمارند. پس جهت وام‌گیری پذیرفته است، امّا با واسطهٔ آرامی و با این تردید که بسیاری آن را عربی اصیل می‌دانند؛ از این رو «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D8%AA\",\n            \"https://www.etymonline.com/word/zenith\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1767\", \"status\": \"supports\", \"note\": \"Klein s.v. zenith: 'fr. VArab. semt, corresponding to Classical Arab. samt, \\\"way, path\\\" (abbreviation of samt-ar-rāʾs, \\\"way over the head\\\"), fr. L. se-mita, \\\"path, way\\\"' — exactly Nourai's Latin > Arabic arrow, and his 'as-sumut' is Klein s.v. azimuth (KLN_1966.txt leaf 83 = printed p.~142): 'F. azimut, fr. Arab. as-sumūt, pl. of as-samt, \\\"the way\\\", fr. as-, assimilated form of al-, \\\"the\\\", and samt, \\\"way\\\". See zenith.'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1818 (LKT.txt ll.4120-4121)\", \"stance\": \"partial\", \"note\": \"'[arab. samt] \\\"Weg, rechter; Richtung\\\", plr. sumūt, simūt; hieraus mit ar. Art. it. azimut, azimutto, frz. azimut; dtsch. Azimut ... engl. azimuth. — Aus samt ar-ruʾūs \\\"Richtung der Köpfe\\\" oder kurz as-samt wurde mit Verschreibung von m zu ni it. zenit, frz. engl. ndl. zenith' — Lokotsch confirms every step downstream but says nothing of a Latin origin for samt: for him the word is Arabic.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic s.v. Azimuth (DEV.txt l.700)\", \"stance\": \"partial\", \"note\": \"'De l'arabe as-semt, que les astronomes orientaux emploient dans le même sens, et qui est aussi le mot dont nous avons fait zénith.' Same: Arabic source assumed, no Latin ancestry.\"},\n            {\"src\": \"AFA\", \"where\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen (AFA.txt), grep 'semita' / 'samt'\", \"stance\": \"silent\", \"note\": \"no entry found for samt in the local OCR, so Fraenkel does not list it among the Aramaic loans — the Aramaic sēmiṭā route rests on Wiktionary's citation, not on Fraenkel.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"samt «سمت»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian سمت samt 'direction, side; (astron.) azimuth; post, office' is a straightforward Arabic loan of the classical period, taken over with the ʿarabī pattern intact; Mo'in marks it [ع.] (= Arabic) and glosses it 'راه، روش ... طرف، جانب' ('way, manner ... side, direction'), and Wiktionary's Persian section says simply 'Borrowed from Arabic سَمْت (samt)'. Because Persian took it from Arabic while Arabic had (per node #3) taken it from Latin through Aramaic, this is a rare Latin > Aramaic > Arabic > Persian chain, not an inherited Iranian word — Nourai draws it correctly as a borrowing from the Arabic box. The second Persian sense 'post, position' (سمت اداری) is a later, purely Arabic-internal development of samt 'mode of conduct'.\",\n          \"derivation_fa\": \"«سمت» در فارسی نو به معنای «جهت، طرف؛ (در نجوم) سمت الرأس؛ مقام و عنوان» وام‌واژه‌ای عربی از دورهٔ کلاسیک است که با همان وزن عربی به فارسی آمده؛ معین آن را با نشانِ [ع.] می‌آورد و «راه، روش … طرف، جانب» معنی می‌کند، و ویکی‌واژه هم می‌گوید «وام‌گرفته از عربی سَمْت». چون عربی خود (بنگرید گرهٔ ۳) آن را از لاتینی به واسطهٔ آرامی گرفته است، این زنجیرهٔ کم‌مانند لاتینی > آرامی > عربی > فارسی است و واژه‌ای ایرانی و ارثی نیست؛ نورایی درست آن را وام‌گیری از جعبهٔ عربی نشان داده است. معنای دوم فارسی («مقام، عنوان») تحولی درون‌عربی از samt «روش رفتار» است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D8%AA\",\n            \"https://abadis.ir/fatofa/%D8%B3%D9%85%D8%AA/\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON:1919\", \"status\": \"partial\", \"note\": \"Mo'in's six-volume Farhang-e Farsi is not scanned and its pagination cannot be checked (refs_online.json: 'Page numbers cannot be mapped online'); the entry text itself, read from abadis.ir section فرهنگ معین, is '(سَ) [ع.] ۱- (مص ل.) راهی را در پیش گرفتن. ۲- به راه درست و میانه راه رفتن. ۳- (اِ.) راه، روش. ۴- قصد. ۵- طرف، جانب' — headword, Arabic tag and the gloss 'path, direction' are exactly what the arrow needs.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"RCH\", \"where\": \"Richardson–Johnson s.v. samt (RCH.txt ll.49710, 49712)\", \"stance\": \"supports\", \"note\": \"'A[rabic] samt ... Travelling. Groping along. Guessing the way. A way, road, path; a part, tract, country, or quarter. Towards. The right way, the path of probity' and, next entry, 'samt: The azimuth' — the word is registered in a Persian–Arabic–English dictionary as Arabic, with both the 'path' and the astronomical sense.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt), grep 'samt'\", \"stance\": \"silent\", \"note\": \"no entry — as expected: Horn treats inherited New Persian etymology and excludes Arabic loans.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien (HUB.txt), grep 'samt'\", \"stance\": \"silent\", \"note\": \"no entry for the Persian word (the only hits are German 'sämtlich' and yāsamīn); Hübschmann likewise covers Iranian material, not Arabisms.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"French\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box for the Romance stage between Arabic and English, and it is justified: French azimut (whence English azimuth, late 14c.) comes directly from Arabic as-sumūt, and French zénith continues Old French cenit(h). The one nuance is that the zenith form was not created in French: Klein has 'Late ME., fr. OF. cenit(h) (F. zénith), fr. Sp. cenit, fr. VArab. semt ... VArab. semt became senit, zenit, owing to a misreading of the letter m as ni', while Lokotsch routes the same misreading through Italian ('mit Verschreibung von m zu ni it. zenit'). So French is the immediate donor to English but is itself a relay from Spanish/Italian scientific translation of the 12th-13th centuries.\",\n          \"derivation_fa\": \"این جعبهٔ تهی، مرحلهٔ رومی (فرانسه) میان عربی و انگلیسی است و بجاست: فرانسوی azimut یکسر از عربی as-sumūt گرفته شده (و از آن انگلیسی azimuth در پایان سدهٔ ۱۴ م.) و فرانسوی zénith ادامهٔ فرانسوی کهن cenit(h) است. تنها نکته این است که صورتِ zenith در خودِ فرانسه ساخته نشده: کلاین می‌گوید انگلیسی میانهٔ متأخر از cenit(h) فرانسوی کهن، آن هم از اسپانیایی cenit، از عربی عامیانهٔ semt که در آن «م» به «نی» بدخوانی شده است؛ لوکوچ همان بدخوانی را از راه ایتالیایی می‌داند. پس فرانسه وام‌دهندهٔ بی‌واسطهٔ انگلیسی است، ولی خود واسطهٔ ترجمه‌های علمی اسپانیا و ایتالیای سده‌های ۱۲–۱۳ است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/zenith\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference of its own; the claim is covered by KLN:1767 cited on the neighbouring boxes (see nodes #3 and #6).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p.1767 s.v. zenith and p.~142 s.v. azimuth\", \"stance\": \"supports\", \"note\": \"'Late ME., fr. OF. cenit(h) (F. zénith), fr. Sp. cenit, fr. VArab. semt' / 'F. azimut, fr. Arab. as-sumūt'.\"},\n            {\"src\": \"PHN\", \"where\": \"Pihan, Dictionnaire étymologique des mots français dérivés de l'arabe (PHN.txt ll.2021-2026)\", \"stance\": \"supports\", \"note\": \"'AZIMUT, s. m. (a.) — [as-samt] la voie droite. On appelle azimut, en astronomie ... la transcription azimut' — a French Arabism, listed as such.\"},\n            {\"src\": \"DEV\", \"where\": \"Devic s.v. Azimuth (DEV.txt l.700)\", \"stance\": \"supports\", \"note\": \"'De l'arabe as-semt ... et qui est aussi le mot dont nous avons fait zénith.'\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"English\",\n          \"words\": \"zenith, azimuth\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both are late-14th-century English borrowings from French, and both go back to the same Arabic noun. Zenith: late ME zineth/cenith from Old French cenit(h) (Medieval Latin zyneth), itself from Spanish/Italian cenit, a scribal mangling of Arabic samt (in samt ar-raʾs 'the way over the head') in which -m- was read as -ni-; the figurative 'highest point' is c.1600. Azimuth: from Old French azimut, from Arabic as-sumūt 'the ways', plural of as-samt, with the Arabic article agglutinated (the same al- that hides in algebra, alcohol). So the pair are doublets — one from the singular, one from the plural, one distorted, one not — which is precisely what Nourai's chart shows by hanging both on the French box under Arabic.\",\n          \"derivation_fa\": \"هر دو واژه در پایان سدهٔ ۱۴ م. از فرانسه به انگلیسی رفته‌اند و هر دو به یک اسم عربی می‌رسند. zenith: انگلیسی میانهٔ متأخر zineth/cenith از فرانسوی کهن cenit(h) (لاتینی میانه zyneth)، خود از اسپانیایی/ایتالیایی cenit که تحریف کاتبانِ عربی samt (در samt ar-raʾs «راهِ بالای سر») است و در آن «م» به «نی» خوانده شده؛ معنای مجازی «اوج» از حدود ۱۶۰۰ م. است. azimuth: از فرانسوی کهن azimut، از عربی as-sumūt «راه‌ها»، جمع as-samt، با حرف تعریفِ چسبیده (همان al- که در algebra و alcohol هم پنهان است). پس این دو واژه دوگانه (doublet) اند: یکی از مفرد و دیگری از جمع، یکی تحریف‌شده و دیگری سالم — و نمودار نورایی درست هر دو را زیر جعبهٔ فرانسه و عربی آورده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/zenith\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1767\", \"status\": \"supports\", \"note\": \"Klein's zenith entry (printed p.1767) gives the whole chain and the misreading — 'VArab. semt became senit, zenit, owing to a misreading of the letter m as ni. Cp. azimuth.' — and his azimuth entry gives 'F. azimut, fr. Arab. as-sumūt, pl. of as-samt'. Both English words on Nourai's box are therefore on the page he cites.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Zenith and the list of 'French from Spanish from Arabic' words (SKT.txt ll.21821, 23699)\", \"stance\": \"supports\", \"note\": \"'Zenith. (F. — Sp. — Arab.)' and zenith appears in Skeat's list of words that came into 'French from Spanish from Arabic'; his Nadir entry names 'nazīr as-samt' as the point opposite the zenith.\"},\n            {\"src\": \"LKT\", \"where\": \"Lokotsch no. 1818\", \"stance\": \"supports\", \"note\": \"'engl. azimuth ... frz. engl. ndl. zenith, dt. Zenit oder Zenith \\\"Scheitelpunkt\\\" im Gegensatz zu Nadir'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Latin\",\n          \"words\": \"commŭnis; migâre\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The branch is right, the printing is not. (1) Latin commūnis 'common, public, shared' is from *ko-moin-i- 'held in common' (co- + Old Latin moinos/moenus 'service, duty, gift', cf. mūnus, mūnia); the quantity is long ū (Klein: 'fr. co- and OL. moinos, moenis (L. munus)'), so the printed breve in 'commŭnis' is wrong. (2) There is no Latin *migâre: the verb is migrāre 'to move one's dwelling, migrate', a denominative of *migʷ-ros, from the extended root *mei-gʷ- beside Greek ἀμείβω 'I exchange'. The 600 dpi crop of the printed page shows that the book itself prints 'migâre' without the r, so the extraction is faithful and the misprint is Nourai's (his own AHD source has 'Latin migrāre, to change one's place of living: MIGRATE; EMIGRATE', which is also where his gloss comes from, word for word).\",\n          \"derivation_fa\": \"شاخه درست است، امّا چاپ آن نه. یکم: لاتینی commūnis «مشترک، همگانی» از *ko-moin-i- «در اشتراک نگاه‌داشته» است (co- + لاتینی کهن moinos/moenus «خدمت، وظیفه، پیشکش»، مقایسه کنید با mūnus و mūnia)؛ کمیت واکه ūی کشیده است، پس علامت کوتاهی روی u در «commŭnis» نادرست است. دوم: در لاتینی صورتی *migâre وجود ندارد؛ فعل migrāre «جای زندگی را عوض کردن» است، مشتق از *migʷ-ros از ریشهٔ گسترش‌یافتهٔ *mei-gʷ- در کنار یونانی ἀμείβω «مبادله می‌کنم». تصویر ۶۰۰ نقطه‌ای صفحه نشان می‌دهد خودِ کتاب «migâre» بی r چاپ کرده است؛ پس خطای چاپی کتاب است نه خطای خوانش اسکن — چنانکه منبع خودِ نورایی (واتکینز) عیناً «Latin migrāre, to change one's place of living» دارد و معنای انگلیسی جعبه هم واژه‌به‌واژه از همان‌جاست.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"commŭnis ; migâre\",\n          \"correct_form\": \"commūnis ; migrāre\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/communism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mei-1: '4. Suffixed o-grade form *moi-n- in compound adjective *ko-moin-i-, \\\"held in common\\\" (*ko-, together; see kom), in: ... b. Latin commūnis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM). ... 6. Extended form *(a)meigʷ- in: a. Greek ameibein, to change: AMOEBA; b. Latin migrāre, to change one's place of living: MIGRATE; EMIGRATE.' Nourai's gloss for the verb is copied from this line; only the spelling of the headword slipped.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. migro (LAT.txt l.37934ff.)\", \"stance\": \"supports\", \"note\": \"'migro, -as, -aui, -atum, -āre: changer de résidence, s'en aller, sortir, émigrer, se changer ... On interprète ce verbe comme dérivé d'un adjectif *migro-, où la racine, de la forme mig-, serait un élargissement de la racine *mei- \\\"changer\\\"; v. munis et muto; le grec a aussi une forme à élargissement dans ἀμείβω \\\"j'échange\\\".' — the *mei-gʷ- analysis of the arrow, and the correct headword spelling.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.713 (lemma meih-gʷ-)\", \"stance\": \"supports\", \"note\": \"'Latin migro, -are ... Denom. of *migʷ-ros' — again migro/migrāre with r.\"},\n            {\"src\": \"KLN\", \"where\": \"p.336 s.v. common (KLN_1966.txt leaf 180)\", \"stance\": \"supports\", \"note\": \"'fr. L. communis (cp. the OL. acc. comoinem), \\\"common, universal, public\\\", formed fr. co- and OL. moinos, moenis (L. munus), \\\"service, office, function\\\" ... fr. I.-E. base *moin-, *mein-, \\\"to change\\\"' — supports both the form commūnis and Nourai's 'Moin' root label.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II 241 (leaf 245)\", \"stance\": \"supports\", \"note\": \"'Vgl. Wf. LEWb.2 u. communis' with 'got. gamains ... ahd. gimeini \\\"gemein(sam)\\\"' listed under mei- 'wechseln, tauschen'.\"}\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"French\",\n          \"words\": \"communisme\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"French communisme is a 19th-century learned formation, not an inherited word: commun (< Latin commūnis) + -isme, coined in the Parisian debates of c.1840 (Étienne Cabet, Théodore Dézamy; English communist 1841 with J. Goodwyn Barmby's 'London Communist Propaganda Society', English communism 1843). Nourai's chart is right to put the French box under Latin commūnis and above both the Persian and the English boxes: for this word French really is the distributing centre from which the term spread to English, German, Russian and — via the constitutional and press vocabulary of the late Qajar/Pahlavi period — to Persian.\",\n          \"derivation_fa\": \"فرانسوی communisme واژه‌ای ساختهٔ سدهٔ نوزدهم است و ارثی نیست: commun (از لاتینی commūnis) + پسوند -isme، برساختهٔ محافل پاریس حدود ۱۸۴۰ م. (کابه، دزامی)؛ در انگلیسی communist از ۱۸۴۱ و communism از ۱۸۴۳ م. ثبت شده است. نمودار نورایی بجا جعبهٔ فرانسه را زیر commūnis لاتینی و بالای دو جعبهٔ فارسی و انگلیسی نشانده است: در مورد این واژه، فرانسه به‌راستی کانون پخش است و اصطلاح از آنجا به انگلیسی، آلمانی، روسی و — از راه واژگان مطبوعات و قانون‌نویسی اواخر قاجار و دورهٔ پهلوی — به فارسی رسیده است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/communism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mei-1 §4b lists '(COMMUNISM)' among the English words from Latin commūnis (the parentheses in Watkins' notation mark a derivative formed later in a modern language), which is what the French box represents.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p.336 s.v. common and its cross-references (commune, communicate)\", \"stance\": \"supports\", \"note\": \"Klein takes the whole common/commune/communicate group from L. communis through French; 'communisme' is the same stem plus the French suffix.\"},\n            {\"src\": \"WEB\", \"where\": \"Etymonline s.v. communism (archived)\", \"stance\": \"supports\", \"note\": \"'from French communisme (c. 1840), derived from commun and the suffix -isme'; communist 1841, first used by John Goodwyn Barmby.\"}\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Persian\",\n          \"words\": \"(no transliteration; script only: کمونیزم ، کمونیسم)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian کمونیسم / کمونیزم is a French loan of the constitutional-and-after period, and the doublet of spellings is itself the proof: کمونیسم keeps the French -isme, while کمونیزم reflects the voiced pronunciation [z] that Persian gives French -isme (as in سوسیالیزم, رئالیزم). Mo'in tags the word [فر.] (= French) and defines it 'مکتبی است که از نظر فلسفی و اقتصادی بر مالکیت عمومی وسایل تولید تکیه می‌کند'; Dehkhoda's headword کمونیسم reads '( فرانسوی، اِ ) رجوع به کمونیزم شود'. So the arrow French > Persian is right and the word did not come through Russian or English, in spite of the politics of the period.\",\n          \"derivation_fa\": \"«کمونیسم / کمونیزم» وام‌واژه‌ای فرانسوی از دورهٔ مشروطه و پس از آن است و همین دوگانگی املا گواه آن است: در «کمونیسم» پسوند فرانسوی -isme نگاه داشته شده و در «کمونیزم» تلفظ واکدارِ [ز] که فارسی به -isme فرانسوی می‌دهد بازتاب یافته است (مانند سوسیالیزم و رئالیزم). معین واژه را با نشانِ [فر.] می‌آورد و چنین معنی می‌کند: «مکتبی است که از نظر فلسفی و اقتصادی بر مالکیت عمومی وسایل تولید تکیه می‌کند»؛ دهخدا نیز زیر «کمونیسم» می‌نویسد «(فرانسوی، اِ) رجوع به کمونیزم شود». پس پیکان فرانسه > فارسی درست است و واژه — به‌رغم سیاست آن روزگار — از راه روسی یا انگلیسی نیامده است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%DA%A9%D9%85%D9%88%D9%86%DB%8C%D8%B3%D9%85/\",\n            \"https://www.etymonline.com/word/communism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"MON6:1603\", \"status\": \"not_checked\", \"note\": \"Mo'in vol. 6 (اعلام) is not scanned anywhere (refs_online.json: 'The a'lam volumes (MON5/MON6 citations) are NOT online'), and the 2-volume Adena condensation on disk has no کمونیسم headword (grep of MON_part1/2.txt returns only the word inside other definitions, e.g. l.49758 'دست چپی، طرفدار سوسیالیسم و کمونیسم'). The claim itself was verified in Mo'in's own text via abadis.ir: '(کُ مُ) [ فر. ] (اِ.) مکتبی است که ... بر مالکیت عمومی وسایل تولید تکیه می‌کند' — French tag exactly as the arrow requires.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. کمونیسم, read via abadis.ir (فرهنگ معین)\", \"stance\": \"supports\", \"note\": \"'(کُ مُ) [ فر. ] (اِ.) مکتبی است که از نظر فلسفی و اقتصادی بر مالکیت عمومی وسایل تولید تکیه می کند' — the [فر.] tag is Mo'in's own statement that the word is French.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha-ye hend-o-orupayi (incoming/ARY), grep کمونیس\", \"stance\": \"silent\", \"note\": \"no entry; Aryanpur's dictionary covers inherited Indo-European material in Persian, not modern European loanwords.\"}\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"communism, communist; common, communicate\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All four words are correctly assigned to the root, but the box conflates two different routes and two different centuries. Communism (1843) and communist (1841) are indeed from French communisme/communiste, so they belong under the French box as drawn. Common and communicate are not: common is Middle English commun, comun from Old French comun (< L. commūnis) in the 13th century, and communicate is a 15th-16th-century Latinism from L. communicāre 'to share' — Watkins lists them straight under Latin commūnis ('COMMON, COMMUNE, COMMUNICATE, (COMMUNISM)'), with only communism marked as the modern derivative. So the arrow French communisme > common/communicate is an artefact of the chart's layout, not a real derivation; hence 'plausible' rather than 'confirmed'.\",\n          \"derivation_fa\": \"هر چهار واژه به‌درستی به همین ریشه بازمی‌گردند، امّا این جعبه دو مسیر و دو دورهٔ متفاوت را در هم آمیخته است. communism (۱۸۴۳ م.) و communist (۱۸۴۱ م.) واقعاً از فرانسوی communisme/communiste اند و جای‌شان همان‌جاست که نورایی گذاشته. ولی common و communicate چنین نیستند: common از انگلیسی میانهٔ commun/comun از فرانسوی کهن comun (از لاتینی commūnis) در سدهٔ ۱۳ م. است و communicate واژه‌ای لاتینی‌مأخذ از سده‌های ۱۵–۱۶ م. از communicāre «شریک کردن»؛ واتکینز هر دو را یکسر زیر commūnis لاتینی می‌آورد و تنها communism را با پرانتز به‌عنوان مشتق نوساخته نشان می‌دهد. پس پیکان «communisme فرانسوی > common/communicate» زادهٔ چیدمان نمودار است نه ریشه‌شناسی؛ از این رو «با احتیاط پذیرفتنی».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/communism\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"Watkins 1985 s.v. mei-1 §4b: 'Latin commūnis, common, public, general: COMMON, COMMUNE, COMMUNICATE, (COMMUNISM).' The four words are all under the root, as Nourai says, but Watkins attaches COMMON and COMMUNICATE directly to Latin and marks only COMMUNISM as a later formation — i.e. the reference supports the words but not the French intermediary drawn for two of them.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"p.336 s.v. common (KLN_1966.txt leaf 180)\", \"stance\": \"partial\", \"note\": \"'common, adj. — ME. commun, comun, fr. OF. comun (F. commun), fr. L. communis ... and cp. commune, communicate, immune, municipal, munificent, remunerate' — Old French comun, not communisme, is the source of English common.\"},\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Common / Communicate\", \"stance\": \"partial\", \"note\": \"Skeat likewise takes common from OF comun < L. communis; his dictionary predates communism as a headword.\"}\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"migrate, immigration\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English migrate (1690s) is taken from Latin migrātus, past participle of migrāre, and immigration from Latin immigrāre 'to move into' (in- + migrāre) via immigrātiōnem — both are learned 17th-18th-century Latinisms, borrowed directly from the written language rather than inherited, which is why the chart's arrow runs from the Latin box. Watkins puts both under mei-1 §6b ('Latin migrāre ... : MIGRATE; EMIGRATE'), and Skeat says shortly 'Migrate. (L.) From pp. of L. migrare, to wander; allied to mean, to go' — 'allied to mean' being exactly Nourai's linking of the 'go/change' and 'common' branches of the same root.\",\n          \"derivation_fa\": \"انگلیسی migrate (دههٔ ۱۶۹۰ م.) از migrātus لاتینی، اسم مفعول migrāre، گرفته شده و immigration از immigrāre لاتینی («به درون کوچیدن»، in- + migrāre) از راه immigrātiōnem؛ هر دو وام‌واژهٔ عالمانهٔ سده‌های ۱۷–۱۸ م. اند و از زبان نوشتاری گرفته شده‌اند نه ارثی، و همین است که پیکان از جعبهٔ لاتینی می‌آید. واتکینز هر دو را زیر mei-1 بند ۶ب می‌آورد و اسکیت کوتاه می‌گوید: «Migrate. (لاتینی) از اسم مفعول migrāre «سرگردان شدن»؛ خویشاوند mean «رفتن»» — و همین «خویشاوندی» درست همان یکی‌دانستن دو شاخهٔ «رفتن/تغییر» و «مشترک» است که نورایی در این صفحه نشان داده.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mei-1 §6b: 'Latin migrāre, to change one's place of living: MIGRATE; EMIGRATE' (and the index of the same book, l.1869, 'MIGRATE mei-1').\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Migrate (SKT.txt l.11542)\", \"stance\": \"supports\", \"note\": \"'Migrate. (L.) From pp. of L. migrare, to wander; allied to mean, to go.'\"},\n            {\"src\": \"LAT\", \"where\": \"Ernout–Meillet s.v. migro (LAT.txt l.37934)\", \"stance\": \"supports\", \"note\": \"'Dérivés et composés: migratio (Vitr.), -tor (Gloss.); admigro (Pl.); com-, de-, e-, in-, prae-, re-, trans-migro, et leurs dérivés' — in-migrāre, the base of immigration, is listed.\"}\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Germanic\",\n          \"words\": \"ga-maid-az; missa; gamainiz\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All three Proto-Germanic reconstructions are Watkins' own, letter for letter. (1) *ga-maid-az '(intensive ga- +) changed for the worse, abnormal' is the o-grade *moi-t- of the root (cf. Gothic maidjan 'to change, falsify', in-maidjan 'to transform', WP II 248), whence Old English gemād 'insane'. (2) *missa- 'in a changed manner, wrongly' is the suffixed zero-grade *mit-to- (participial *miþto- 'confused, wrong'), whence the Gothic prefix missa-, Old Norse mis(s)-, Old English mis-. (3) *gamainiz 'common' is *ko-moin-i- 'held in common', whence Gothic gamains, Old High German gimeini, Old English gemǣne — and the pejorative English sense 'low, inferior' that Nourai notes in brackets is a specifically English development of 'common' (as in 'common' > 'vulgar'), paralleled in Old High German mein 'false, deceitful' (Meineid 'perjury').\",\n          \"derivation_fa\": \"هر سه بازسازی ژرمنی آغازین، واژه‌به‌واژه از واتکینز است. یکم: *ga-maid-az «(با پیشوند تأکیدی ga-) دگرگون‌شده به بدی، نابهنجار» گونهٔ o-دارِ *moi-t- ریشه است (مقایسه کنید با گوتی maidjan «تغییر دادن، تحریف کردن»، والده‌پوکورنی ۲/۲۴۸)، و از آن انگلیسی کهن gemād «دیوانه». دوم: *missa- «به شیوهٔ دگرگون، نادرست» صورت پسوندی درجهٔ صفرِ *mit-to- است (اسم مفعول *miþto- «آشفته، نادرست»)، و از آن پیشوند گوتی missa- و انگلیسی کهن -mis. سوم: *gamainiz «مشترک» همان *ko-moin-i- است و از آن گوتی gamains، آلمانی علیای کهن gimeini و انگلیسی کهن gemǣne — و معنای تحقیرآمیزِ «پست، فرومایه» که نورایی در کمانک آورده، تحولی ویژهٔ انگلیسی از «مشترک» به «عامیانه» است، مانند mein «دروغین» در آلمانی علیای کهن (Meineid «سوگند دروغ»). ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mei-1: '2. Suffixed o-grade form *moi-t- in: a. Germanic *ga-maid-az (*ga-, intensive prefix; see kom), \\\"changed (for the worse),\\\" abnormal, in Old English gemād, insane: MAD ... 3. Suffixed extended zero-grade form *mit-to- in Germanic *missa-, \\\"in a changed manner\\\", abnormally, wrongly ... 4. ... *ko-moin-i-, \\\"held in common\\\" ... a. Germanic *gamainiz in Old English gemǣne, common, public, general: MEAN2' — all three of Nourai's forms and all three glosses.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II 248 (leaf 252) and Bd. II 241 (leaf 245)\", \"stance\": \"supports\", \"note\": \"p.248: 'got. maidjan \\\"verändern, verfälschen\\\" ... in-maidjan \\\"verwandeln\\\" ... germ. missa-'; p.241: 'got. gamains, ags. gemǣne, ahd. gimeini \\\"gemein(sam)\\\"; als \\\"vertauscht = verfälscht\\\" auch ahd. mein \\\"falsch, trügerisch\\\" (nhd. Meineid)'.\"},\n            {\"src\": \"POK\", \"where\": \"Pokorny p.715 (lemma meih-t(h)-2)\", \"stance\": \"supports\", \"note\": \"'Gothic maidjan \\\"change, falsify\\\", in-maidjan \\\"transform\\\" ... participle *miþto- \\\"confused, confounded, incorrect\\\" in Gothic misso \\\"reciprocal\\\" ... prefix Gothic missa- \\\"wrong, incorrect\\\" ... Old High German missa-, missi-, Modern High German miss-.'\"},\n            {\"src\": \"KLN\", \"where\": \"p.953 s.v. 'mean, of low rank'\", \"stance\": \"supports\", \"note\": \"'rel. to ... Goth. ga-mains, \\\"common\\\", OE. mān, ON., OHG. mein, OS., OFris. mēn, \\\"false\\\" ... OHG. meineid ... \\\"perjury\\\", lit. \\\"false oath\\\"'.\"}\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"English\",\n          \"words\": \"mad; mis-, mistake, misfortune; mean 2 : inferior\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Mad continues Old English gemād(d) 'out of one's mind' (from PGmc *ga-maid-az), with loss of the prefix in Middle English mad; the semantic path is 'changed, spoiled' > 'maimed' (cf. Gothic gamaiþs 'crippled') > 'insane', which is why Skeat writes 'The orig. sense seems to be \\\"severely injured\\\"; the prefix ge-, g-, gi- is unessential'. Mis- is the native English reflex of *missa- (Old English mis-); mistake was reinforced by Old Norse mistaka 'to take in error' (the -taka being the same word as English take, itself a Norse loan); misfortune is a hybrid of the same element received through Old French mes- (< Frankish *missi-) plus fortune, so it belongs here through a Romance detour rather than directly. Mean 'inferior, base' is Old English gemǣne 'common' (< *gamainiz), pejorated in Middle English along the line 'shared by all' > 'ordinary' > 'low, base' — Nourai's 'mean 2' correctly separates it from mean 'intermediate' (< Old French meien < L. mediānus) and mean 'to intend' (< OE mænan).\",\n          \"derivation_fa\": \"mad ادامهٔ انگلیسی کهن gemād(d) «از خود بی‌خود، دیوانه» است (از ژرمنی *ga-maid-az) که پیشوندش در انگلیسی میانه افتاده و mad شده؛ راه معنایی چنین است: «دگرگون‌شده، تباه» > «آسیب‌دیده، ناقص» (مقایسه: گوتی gamaiþs «لنگ، معیوب») > «دیوانه»، و از این روست که اسکیت می‌نویسد «معنای اصلی گویا \\\"سخت آسیب‌دیده\\\" است و پیشوند -ge غیرضروری است». پیشوند -mis بازماندهٔ بومی *missa- است (انگلیسی کهن -mis)؛ mistake با نورس کهن mistaka «به خطا گرفتن» تقویت شده؛ و misfortune آمیزه‌ای است از همان عنصر که این بار از راه فرانسوی کهن -mes (از فرانکی *missi-) به‌علاوهٔ fortune آمده است، یعنی با یک چرخِ رومی نه به‌طور مستقیم. mean «فرومایه، پست» همان gemǣne انگلیسی کهن «مشترک» است (از *gamainiz) که در انگلیسی میانه معنای منفی گرفته: «مشترکِ همه» > «عادی» > «پست»؛ و نورایی درست آن را «mean 2» نامیده و از mean «میانه» (از فرانسوی کهن meien از mediānus لاتینی) و mean «قصد کردن» جدا کرده است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. mei-1: '... in Old English gemād, insane: MAD ... a. Old English mis-, mis-: MIS-1; b. Old Norse mis(s), mis(s)-, miss, mis-: AMISS, MISTAKE ... in Old English gemǣne, common, public, general: MEAN2; (DEMEAN2)'; the index of the same volume has 'MAD mei-1' (l.1790), 'MEAN2 mei-1' (l.1838), 'MIS-1 mei-1, mei-2' and 'MISTAKE mei-1' (l.1875).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SKT\", \"where\": \"Skeat s.v. Mad (SKT.txt l.10877)\", \"stance\": \"supports\", \"note\": \"'Mad. (E.) The vowel was formerly long. M.E. maad, made. — A.S. gemǣd, ge-maad, in a gloss; hence mād-mōd, madness (Grein). + O.Sax. gi-mēd, foolish; O.H.G. gi-meit, vain; Icel. meiddr, pp. of meiða, to maim, hurt; Goth. ga-maiþs, maimed. The orig. sense seems to be \\\"severely injured\\\"; the prefix ge-, g-, gi- is unessential.'\"},\n            {\"src\": \"KLN\", \"where\": \"p.953 s.v. 'mean, of low rank' (KLN_1966.txt leaf 511)\", \"stance\": \"supports\", \"note\": \"'mean, adj., of low rank, inferior, base. — ME. mene, \\\"common, mean\\\", fr. OE. (ge)mǣne, \\\"common\\\"' — the pejoration of 'common' to 'base' is documented in the very entry Nourai cites for this branch (KLN:953).\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Mei 4\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *mey- 'to bind' (Pokorny 4. mei- 'binden', p.710; Watkins/AHD mei-4 'To tie'), with the instrument suffix *-tro- in *mi-tro- 'that which binds, contract'\",\n      \"note\": \"Root, language label, gloss and page number are all exactly right: Pokorny's fourth mei- lemma on p.710 is headed 'Meaning: to bind' and its material is precisely 'Old Indic mitra- n. \\\"friend\\\" (originally \\\"friendship\\\" from \\\"*association\\\"), Avestan miθra- m. \\\"friend; pact, covenant; name of a God (personification of the covenant)\\\", Old pers. Miθra- \\\"God's name\\\"; gr. hom. Μίτρη \\\"belt; head fascia\\\"', with the cross-reference 'compare mei-1' (i.e. mei-1 'to strengthen; pole', p.709, Skt. minóti 'fastens'). Two remarks. (1) There is a real and old disagreement about which *mei- underlies mitra-: Meillet, Benveniste and Etymonline derive it from *mei- 'to exchange' ('contract' = reciprocity, whence Skt. mitrá- 'friend'), Pokorny, Wiktionary and Watkins from *mei- 'to bind' ('that which binds'). Wiktionary states the split explicitly ('Pokorny (1959) refined this as meaning \\\"to bind\\\", though Meillet earlier suggested \\\"to exchange\\\"'). Nourai follows Pokorny, which is defensible; but note that his own page 297 thereby separates mitra from the maēni/missa material of entry 0, whereas half the field would join them. (2) A stray dissenting voice: Mann's IEC (l.10850) puts Av. miθro and Skt. mitráḥ under *mitros '(?) mild, gentle' beside Lith. mitrùs — an isolated view, and Walde–Pokorny II 242 already dismissed the equation of mitra with 'mild'.\",\n      \"note_fa\": \"ریشه، برچسب زبان، معنا و شمارهٔ صفحه همه درست است: چهارمین سرواژهٔ mei- در پوکورنی، در همان صفحهٔ ۷۱۰، عنوانش «بستن» است و مادهٔ آن درست همین است: «سنسکریت mitra- \\\"دوست\\\" (در اصل \\\"دوستی\\\" از \\\"پیوند\\\")، اوستایی miθra- \\\"دوست؛ پیمان، عهد؛ نام یک خدا (تشخّصِ عهد)\\\"، پارسی باستان Miθra-، یونانی هومری Μίτρη \\\"کمربند، سربند\\\"»، با ارجاع «مقایسه شود با mei-1» (یعنی mei-1 «استوار کردن؛ ستون»، ص ۷۰۹، سنسکریت minóti «استوار می‌کند»). دو نکته: نخست آنکه اختلافی دیرین بر سر آن است که mitra- از کدام *mei- است — مه‌یه، بنونیست و اتیمانلاین از *mei- «تبادل کردن» می‌گیرند («پیمان» = رفتار متقابل، و از همین‌جا mitrá- «دوست» سنسکریت)، ولی پوکورنی، واتکینز و ویکی‌واژه از *mei- «بستن» («آنچه می‌بندد»). نورایی از پوکورنی پیروی کرده که پذیرفتنی است، هرچند نتیجه‌اش آن است که در همین صفحه «مهر» از maēni و missa جدا می‌افتد، در حالی که نیمی از پژوهشگران آن‌ها را یکی می‌دانند. دوم آنکه مان در فرهنگ تطبیقی خود miθro و mitráḥ را زیر *mitros «نرم، ملایم» آورده است — دیدگاهی تک‌افتاده که والده‌پوکورنی (۲/۲۴۲) پیشتر آن را رد کرده بود.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mitra\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mey-\",\n        \"https://www.etymonline.com/word/Mithras\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:710\", \"status\": \"supports\", \"note\": \"POK_full.txt l.58368: 'Root / lemma: meih-4, Meaning: to bind, Material: Old Indic mitra- n. (secondary m.) \\\"friend\\\" (originally \\\"friendship\\\" from \\\"*association\\\"), Avestan miθra- m. \\\"friend; pact, covenant; name of a God (personification of the covenant)\\\", Old pers. Miθra- \\\"God's name\\\"; gr. hom. Μίτρη \\\"belt; head fascia, Mitra\\\"; doubtful μίτος ... References: WP. II 241 f., Güntert Weltkönig 50 f.; See also: compare mei-1. Page(s): 710.' Nourai's 'Mei 4 : to bind, tie / POK:710' is this lemma verbatim.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. mei-4 (AHD_watkins1985.txt l.734, end)\", \"stance\": \"supports\", \"note\": \"'mei-4. To tie. 1. Suffixed zero-grade form *mi-tro-, \\\"contract, that which binds,\\\" in: a. Greek mitra, headband, earlier a piece of armor worn around the waist: MITER; b. Old Persian Mithra-, name of a god (< \\\"contract\\\" < \\\"bond\\\"): MITHRAS; c. Russian mir, commune, joy, peace (possibly borrowed from Iranian): MIR. ... [Pok. 4. mei- 710.]' — same root, same gloss, same Pokorny page as Nourai.\"},\n        {\"src\": \"SYN\", \"where\": \"Buck 6.x (SYN.txt l.10941)\", \"stance\": \"supports\", \"note\": \"'Skt. mekhalā-, perh. as me-kha-la- fr. IE *mei- \\\"bind, join\\\"(?) in Skt. mitra, Av. miθra- \\\"friend\\\", Hom. μίτρη \\\"metal waist-guard (Hom.), girdle\\\". Walde-P. 2.241 f.'\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II 241 f.-242 (leaves 245-246 of WLD_Bd2_pages.txt)\", \"stance\": \"supports\", \"note\": \"the mei- 'binden' lemma runs onto p.242, whose first lines still discuss it ('... wechselnd zu ai. mithu usw., Wz. mei- \\\"tauschen\\\" gestellt); lett. niemuri, meimuri \\\"die Femerstricke\\\"'), i.e. Walde–Pokorny record both the 'bind' attachment and the rival 'tauschen' one; and on p.244 the mei- 'weich, sanft' lemma refers the reader away: 'über ai. mitrá- \\\"Freund\\\" s. u. mei- \\\"binden\\\"'.\"},\n        {\"src\": \"IEC\", \"where\": \"Mann, IEC.txt l.10850 s.v. mitros\", \"stance\": \"contradicts\", \"note\": \"'mitros (mitlos?) (?) \\\"mild, gentle\\\". Cf. moitis and WP II, 241 Av. cf. miθro \\\"god of air or light\\\"; Skt. mitráḥ \\\"friend; friendship\\\"; Li. mitrùs \\\"lively\\\"' — Mann assigns mitra to a root 'mild', not 'bind'; an isolated position.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"mithra\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Avestan miθra- and Old Persian Miθra- are the same Indo-Iranian word *mitra- (Skt. mitrá-), formed with the instrument suffix *-tra- ('that which does X', as in mantra 'that which makes one think') on *mi- 'bind', so literally 'that which binds' > 'covenant, contract, treaty' > the god who personifies and guards it. All four of Nourai's glosses are attested stages: 'bond' (Av. miθra- n. 'contract'), 'friendship/kindness' (Skt. mitrá- 'friend', later Persian mehr 'love'), and 'angel of light guarding the truth' (the Yašt 10 Mihr Yašt divinity, ahura-like guardian of oaths, associated with the sun's light). Old Persian attests the god only from Artaxerxes II onwards: Bartholomae notes that Darius I and Xerxes do not name him and that the name appears 'erst [bei] Artaxerxes II', which Kent's citations bear out (A²Sd 4, A²Ha 6, A²Sa 5, A²Pa 25 — 'by the favor of Ahuramazda, Anaitis, and Mithras, this palace I built'). The label 'Avestan / Old Persian' for one box is therefore accurate.\",\n          \"derivation_fa\": \"اوستایی miθra- و پارسی باستان Miθra- همان واژهٔ هندوایرانی *mitra- (سنسکریت mitrá-) اند که با پسوند ابزارِ *-tra- («آنچه فلان می‌کند»، مانند mantra «آنچه به اندیشیدن وامی‌دارد») از *mi- «بستن» ساخته شده؛ پس تحت‌اللفظ «آنچه می‌بندد» > «عهد، پیمان» > خدایی که عهد را تشخّص می‌دهد و پاس می‌دارد. هر چهار معنایی که نورایی آورده مرحله‌ای واقعی است: «پیوند/پیمان» (اوستایی miθra-)، «دوستی و مهربانی» (سنسکریت mitrá- «دوست» و سپس «مهر» فارسی)، و «فرشتهٔ روشنایی نگاهبان راستی» (ایزد مهرِ مهریشت، پاسدار سوگند و پیوسته با روشنی خورشید). در پارسی باستان نام این ایزد تنها از اردشیر دوم به بعد گواهی شده است: بارتولمه یادآور می‌شود که داریوش یکم و خشایارشا او را نمی‌خوانند و نام او «تنها [در کتیبه‌های] اردشیر دوم» می‌آید، و شواهد کنت همین را نشان می‌دهد. پس برچسب دوگانهٔ «اوستایی / پارسی باستان» برای یک جعبه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mitra\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"POK:710\", \"status\": \"supports\", \"note\": \"lemma meih-4 'to bind': 'Avestan miθra- m. \\\"friend; pact, covenant; name of a God (personification of the covenant)\\\", Old pers. Miθra- \\\"God's name\\\"' (POK_full.txt l.58368ff.).\"},\n            {\"ref\": \"KNT:203\", \"status\": \"supports\", \"note\": \"Kent's Lexicon s.v. Miθra- (KNT.txt leaf 227, in the printed pp. ~202-209 range of the Lexicon; the OCR gives 'Mié6ra-'): 'Miθra- sb. \\\"friend\\\"; as deity, \\\"Mithras\\\": El. mi-iš-ša, Akk. mi-i-ri; Av. miθra-, NPers. mihr \\\"sun\\\", Skt. mitrá- \\\"friend\\\" (§9.VI, §33, §49c, §78, §148.II). Cf. Vaumisa- and probably hamiçiya-. Miθraḥ nsm. A²Hb; Mitra A²Sd 4, A²Ha 6; Miθra A²Sa 5, A²Pa 25.' Kent also cross-refers under Bagayādi-: 'probably referring to Mithras, since Phl. and NPers. call this month Mihr \\\"(Month of) Mithras\\\" (Justi, ZDMG 51.247; Bthl. AiW 952-3)'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. miθra- (BRT.txt l.20537, col. ~1183)\", \"stance\": \"supports\", \"note\": \"'*) Eine [ari]sche Götterfigur, ursprünglich eine Sonnengottheit ... In den ap. Inschriften erscheint der Name M. erst [bei] Artaxerxes II.; Dareios I. und Xerxes I. erwähnen der Gottheit nicht, auch im gAw. wird sie nicht genannt ... Bekanntlich hat sich alsdann der M.-Kult bis weit ins Abendland hinüber verbreitet ... aI. mitrá- m. 1) \\\"Freund\\\", 2) ein Ādityа; np. mihr \\\"Sonne\\\" ... Ph[lv].: mihr (geschr. mtr' oder mtrk)'. This is the very column (1183) that Mo'in's footnote in Borhan-e Qate' cites for the word.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, texts A²Sd/A²Ha/A²Sa (KNT.txt ll.4694-4752)\", \"stance\": \"supports\", \"note\": \"'by the favor of Ahuramazda, Anaitis, and Mithras, this palace I built. May Ahuramazda, Anaitis, and Mithras protect me from all evil' — the Old Persian attestations behind the box's second language label.\"},\n            {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e rishe-ha, pdf p.487 (printed 488), Latin index\", \"stance\": \"supports\", \"note\": \"the مهر entry lists 'MITRA (NAME OF A GOD), KINDNESS, AFFECTION, AMITY, FRIENDSHIP, LOVE / MITHRA (AVESTAN) / MITHRA (OLD PERSIAN) / MITR, MITHR, MIHR (PAHLAVI) / MIHR (KURDISH) / MEHR (AFGHANI) / MITRA, MITRAH (SANSKRIT) / MITHRE (GREEK)' with references to POKORNY, MACKENZIE, AMINDAROV and 'THE AMERICAN HERITAGE DICTIONARY ... (MEI-)' — an independent modern Persian cross-check of the whole chain, root label included.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"mehr «مهر»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian مهر mehr descends regularly: Avestan/Old Persian miθra- > Middle Persian mihr (written mtr' / MTRʾ, an Aramaic-style historical spelling; Manichaean myhr), with Old Iranian intervocalic -θr- > MP -hr- (the same change as in puθra- > pus(ar), aθra- > *ahr), and MP mihr > NP mehr with the ordinary lowering of MP i to NP e. MacKenzie's dictionary registers all three senses Nourai gives, as three homographs: 'mihr [mtr'] Mithra; sun; cal. 7th month; 16th day', 'mihr contract, bond', 'mihr love, friendship', plus 'mihrbān friendly, kind' — so مهربان, مهرگان (Mihragān, the Mihr festival), مهرداد (< MP Mihrdād, OP *Miθradāta 'given by Mithra', whence Greek Μιθριδάτης) and میترا are all correctly attached. The Masʿud Saʿd Salmān couplet quoted in the box plays on exactly this bundle ('the day of Mihr and the month of Mihr and the blessed feast of Mihragān'). One thing the chart wisely does not do is include مُهر mohr 'seal': that is a different word, from Sanskrit mudrā via MP muhr (Horn no. 1001, right beside mihr at no. 1000).\",\n          \"derivation_fa\": \"«مهر» فارسی نو تحولی قاعده‌مند دارد: اوستایی/پارسی باستان miθra- > فارسی میانه mihr (به خط پهلوی mtr'، املای تاریخی؛ مانوی myhr)، با تبدیل -θr- ایرانی باستان در میان دو واکه به -hr- در فارسی میانه (همان دگرگونی که در puθra- > پسر دیده می‌شود)، و سپس mihr پهلوی > mehr فارسی نو با تبدیل معمول i پهلوی به e. مکنزی هر سه معنایی را که نورایی آورده، به‌صورت سه هم‌نگاشت ثبت کرده است: «mihr مهر (ایزد)؛ خورشید؛ ماه هفتم و روز شانزدهم گاه‌شمار»، «mihr پیمان، عهد»، «mihr مهر و دوستی»، و «mihrbān مهربان». پس «مهربان»، «مهرگان»، «مهرداد» (< پهلوی Mihrdād، پارسی باستان *Miθradāta «دادهٔ مهر»، یونانی Μιθριδάτης) و «میترا» همه به‌جا به این جعبه بسته شده‌اند، و بیت مسعود سعد سلمان نیز با همین دسته‌واژه بازی می‌کند. نکتهٔ درست دیگر آن است که نورایی «مُهر» به معنای نگین و نشان را در این جعبه نیاورده؛ آن واژهٔ دیگری است، از mudrā سنسکریت به واسطهٔ muhr پهلوی (هرن، شمارهٔ ۱۰۰۱، درست کنار mihr در شمارهٔ ۱۰۰۰).\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%85%D9%87%D8%B1\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mitra\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:2060\", \"status\": \"supports\", \"note\": \"Borhan-e Qateʿ vol. 4, printed page ۲۰۶۰ (pdf page 143; image and my transcription saved as data/verification/sources/refs/ocr/BQT/2060.png / 2060.vision.txt): headword 'مهر ۳ - بکسر اول وسکون ثانی ورای قرشت ، نام فرشته است موکل بمهر و محبت' ('the name of the angel charged with love and affection'), with Moʿin's own etymological footnote 3 at the foot of the page: 'در سانسکریت mitra ، اوستا و پارسی باستان mithra « بارتولمه ۱۱۸۳ »' — Sanskrit mitra, Avestan and Old Persian mithra, citing Bartholomae col. 1183. The same page carries a plate captioned 'مجسمهٔ مهر در کاخ واتیکان (رم)'. Exactly Nourai's arrow, page number confirmed by the printed numeral.\"},\n            {\"ref\": \"MON5:2056\", \"status\": \"not_checked\", \"note\": \"Moʿin's volume 5 (اعلام / proper names) is not scanned anywhere and vajehyab/abadis do not serve his a'lam entries (refs_online.json notes this explicitly for MON5/MON6 citations); the 2-volume Adena condensation on disk has no مهر a'lam entry (only مهرگان at MON_part2.txt l.69290 'مهرگان: [متعلق به مهر ...]'). The claim itself is independently confirmed by BQT:2060 and KNT:203 above.\"},\n            {\"ref\": \"KNT:203\", \"status\": \"supports\", \"note\": \"Kent s.v. Miθra- gives the Persian outcome directly: 'Av. miθra-, NPers. mihr \\\"sun\\\"'; and s.v. Bagayādi-: 'Phl. and NPers. call this month Mihr \\\"(Month of) Mithras\\\"' — which is Nourai's third gloss, 'a month in the Persian calendar'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.56 (PHD.txt l.491)\", \"stance\": \"supports\", \"note\": \"'1mihr [mtr' | M myhr, N ~] Mithra; sun; cal. 7th month; 16th day. 2mihr [mtr', etc.] contract, bond. 3mihr [mtr', etc.] love, friendship. mihrbān [mtr'p'n' | P myhrb'n, N ~] friendly, kind.' — the Middle Persian link, and all of Nourai's Persian senses, in one entry; 'N ~' means the New Persian form is identical.\"},\n            {\"src\": \"HRN\", \"where\": \"Horn, Grundriss der neupersischen Etymologie no. 1000 (HRN.txt l.8696)\", \"stance\": \"supports\", \"note\": \"'1000. mihr \\\"Sonne; Liebe\\\", mihr|bān \\\"freundlich, wohlwollend\\\". ap. Miθra-, vergl. Vaumisa-; aw. Miθra-, miθra- \\\"Vertrag\\\"; phlv. mtr, pāz. mihir (vergl. Meherdates, Tac., Μιθριδάτης; skr. LW. mihira- \\\"Sonne\\\"); ai. Mitrá-, mitrá- \\\"Freund\\\". minj. mira \\\"Sonne\\\".' — Horn's next entry, no. 1001, is 'muhr \\\"Siegel\\\"' from Skt. mudrā-, confirming that the seal-word is separate.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.205 (HUB.txt l.7273)\", \"stance\": \"supports\", \"note\": \"'mihr \\\"Sonne, Liebe\\\", pāz. mihir \\\"Sonne\\\", N. pr. Mihir-ayar, phl. M(i)tru (historische Schreibung für alt arsac. *Miθr, später Mihr), arm. Mihr ... Mihrdat (Pseudocall., Mos. Chor.) = Mīlād aus *Mi(h)rdāt, phl. M(i)trd(a)t(a)n ... lat. Meherdates (Tacitus), älter lat. Mithridates = gr. Μιθριδάτης ... zd. miθra-, ap. miθra-' — the historical spelling and the Mihrdād/Mithridates name-family that Nourai's extra words include.\"},\n            {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt ll.2377, 763)\", \"stance\": \"supports\", \"note\": \"the Pahlavi month-list 'Die Namen der Monate in Phl sind: 1. Fravartīn ... 7. Mihr ...' confirms the calendrical sense, and s.v. ātur the third sacred fire 'ātur burzēn mihr' shows mihr in Sasanian religious usage.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin, 2-vol. Adena OCR (MON_part2.txt l.69290)\", \"stance\": \"partial\", \"note\": \"'مهرگان: [متعلق به مهر ...]' — the derivative مهرگان is present and derived from مهر, but this condensation omits the a'lam entry for مهر itself, so it cannot stand in for MON5:2056.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Greek\",\n          \"words\": \"mithras\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Greek Μίθρας (also Μίθρης) is a borrowing, not a cognate development: Greeks heard the Old Persian/Middle Iranian name from the Achaemenid west — the personal names Μιθραδάτης/Μιθροβάτης are already in Herodotus, and the god's own name is current from Xenophon onwards — and reshaped it as a first-declension masculine in -ᾱς (Ionic -ης), the standard Greek treatment of Iranian names in -a (cf. Δαρεῖος, Ὑδάρνης). Nourai's gloss 'God of light' is the Hellenistic-Roman understanding of the god (Mithras as sol invictus), not the Iranian etymological sense 'contract'; the drift is real and is the reason the Roman cult is called Mithraism. The arrow is correctly drawn from the 'Avestan / Old Persian' box, though the immediate donor was Old Persian/Median, not Avestan; Klein prints just this: 'Mithras ... L., fr. Gk. Μίθρας, fr. Avestic Miθra-, which is rel. to OI. Mitráḥ'.\",\n          \"derivation_fa\": \"یونانی Μίθρας (و Μίθρης) وام‌واژه است نه تحولی موروثی: یونانیان این نام را از غربِ هخامنشی شنیدند — نام‌های شخصی Μιθραδάτης و Μιθροβάτης از هرودوت به‌بعد در دست است و نام خودِ ایزد از زمان کسنوفون رایج می‌شود — و آن را مانند دیگر نام‌های ایرانی مختوم به -a به صورت مذکرِ صرف اول با پایانهٔ -ᾱς (در ایونی -ης) درآوردند (مقایسه: Δαρεῖος، Ὑδάρνης). معنای «خدای روشنایی» که نورایی آورده برداشت هلنیستی–رومی از این ایزد است (مهر به‌عنوان sol invictus) نه معنای ریشه‌شناختی ایرانی («پیمان»)؛ این جابه‌جایی معنایی واقعی است و همان است که آیین رومی را «میترائیسم» کرده. پیکان به‌درستی از جعبهٔ «اوستایی/پارسی باستان» کشیده شده، هرچند وام‌دهندهٔ بی‌واسطه پارسی باستان و مادی بود نه اوستایی؛ کلاین نیز همین را می‌نویسد: «Mithras ... لاتینی، از یونانی Μίθρας، از اوستایی Miθra-».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/Mithras\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-Iranian/mitra\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:989\", \"status\": \"supports\", \"note\": \"Klein s.v. Mithras (KLN_1966.txt leaf 530 = printed p.~990, i.e. Nourai's 989; identical text in KLN_1971.txt l.152795): 'Mithras, n., the Persian god of light. — L., fr. Gk. Μίθρας, fr. Avestic Miθra-, which is rel. to OI. Mitráḥ. See Mitra and cp. next word.' Even Nourai's gloss 'God of light' is Klein's wording. Klein's neighbouring entry Mitra adds 'prob. personification of mitram, \\\"contract, agreement\\\", hence lit. meaning \\\"partner to a contract\\\"; rel. to Avestic and OPers. Miθra- ... These words are prob. rel. to OI. minóti, \\\"fastens, erects, builds\\\"' — i.e. Klein too puts the word under the 'bind/fasten' root.\"},\n            {\"ref\": \"AHD:841\", \"status\": \"not_checked\", \"note\": \"the main body of the 1975/76 New College Edition (where p.841 would fall, in the 'mit-' range) is not openly available; the Watkins root appendix in the 1985 edition confirms the substance under mei-4 ('Old Persian Mithra-, name of a god (< \\\"contract\\\" < \\\"bond\\\"): MITHRAS') and its index (AHD_watkins1985.txt l.1877) has 'MITHRAS mei-4'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"Pokorny p.710 (lemma meih-4)\", \"stance\": \"partial\", \"note\": \"Pokorny lists the Greek material of this root as 'gr. hom. Μίτρη \\\"belt; head fascia, Mitra\\\"' — i.e. the common noun mitra, not the god's name; the god's name in Greek is a loan and so falls outside Pokorny's inherited material. Nourai's arrow is therefore a borrowing, correctly drawn but not documented by POK.\"},\n            {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.205\", \"stance\": \"supports\", \"note\": \"'lat. Meherdates (Tacitus), älter lat. Mithridates = gr. Μιθριδάτης, Μιθραδάτης, bei Herodot Μιτραδάτης (ein Meder)' — documents the Greek transmission of the name (through Median/Old Persian) from Herodotus onward.\"},\n            {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. Miθra-\", \"stance\": \"supports\", \"note\": \"'Miθra- sb. \\\"friend\\\"; as deity, \\\"Mithras\\\"' — Kent himself renders the Old Persian deity's name with the Greek-Latin form Mithras.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty relay box, and a necessary one: Latin Mithrās, -ae took the god from Greek, not from Iranian directly, and it was the Latin form that carried him across the empire (the cult is attested at Rome from the late 1st century CE, with hundreds of mithraea from Britain to the Euphrates; Latin inscriptions write Deo Soli Invicto Mithrae, dative Mithrae, first-declension after the Greek -ᾱς). Klein's entry states just this relay: 'Mithras ... — L., fr. Gk. Μίθρας', and Etymonline the same: 'from Latin, from Greek Mithras, from Avestan Mithra-'.\",\n          \"derivation_fa\": \"جعبهٔ تهی و در حکم واسطه است، و بجا: لاتینی Mithrās, -ae این ایزد را از یونانی گرفت نه یکسر از ایرانی، و همین صورت لاتینی بود که او را در سراسر امپراتوری گسترد (آیین مهر در روم از اواخر سدهٔ یکم میلادی گواهی شده و صدها مهرابه از بریتانیا تا فرات یافته‌اند؛ در کتیبه‌های لاتینی Deo Soli Invicto Mithrae می‌نویسند، با حالت مفعولی‌به‌واسطهٔ Mithrae بر وزن صرف اول، به پیروی از -ᾱς یونانی). کلاین همین واسطه را می‌نویسد: «Mithras ... لاتینی، از یونانی Μίθρας»، و اتیمانلاین نیز: «از لاتینی، از یونانی Mithras، از اوستایی Mithra-».\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/Mithras\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference; the Greek > Latin > English relay is covered by KLN:989 cited on the Greek box (see node #3).\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Mithras (printed p.~990)\", \"stance\": \"supports\", \"note\": \"'Mithras, n., the Persian god of light. — L., fr. Gk. Μίθρας' — Latin is explicitly the intermediary.\"},\n            {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW s.v. miθra- (BRT.txt l.20537)\", \"stance\": \"supports\", \"note\": \"'Bekanntlich hat sich alsdann der M[iθra]-Kult bis weit ins Abendland hinüber verbreitet. Vgl. Windischmann, Mithra (AKM. I), Dst. ZA. 2. 441' — the westward spread of the cult that the Latin box represents.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"Mithras\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Mithras is a straight learned borrowing of the Latin nominative, in use from the 1550s as European scholars read the classical accounts of the Persian religion (Mithraism, the name of the Roman cult, is a 19th-century formation on it). It is thus the end of a five-stage chain — Old Iranian miθra- 'contract' > Old Persian Miθra- (the god) > Greek Μίθρας > Latin Mithrās > English Mithras — and one of the very few English words that reached the language from Iranian by way of Greek and Latin rather than through Arabic or Turkish. Nourai's gloss 'God of light' is the received English sense and matches Klein's headword definition.\",\n          \"derivation_fa\": \"انگلیسی Mithras وام‌گیری عالمانهٔ مستقیم از حالت فاعلی لاتینی است و از دههٔ ۱۵۵۰ م. به‌کار می‌رود، هنگامی که دانشوران اروپایی گزارش‌های کلاسیک دربارهٔ دین ایرانیان را می‌خواندند (Mithraism نامِ آیین رومی، ساختی از سدهٔ نوزدهم بر همین واژه است). پس این پایانِ زنجیره‌ای پنج‌مرحله‌ای است: ایرانی باستان miθra- «پیمان» > پارسی باستان Miθra- (ایزد) > یونانی Μίθρας > لاتینی Mithrās > انگلیسی Mithras؛ و از آن اندک واژه‌هایی است که از ایرانی به واسطهٔ یونانی و لاتینی به انگلیسی رسیده، نه از راه عربی یا ترکی. معنای «خدای روشنایی» که نورایی می‌دهد همان معنای پذیرفتهٔ انگلیسی و برابرِ تعریف سرواژهٔ کلاین است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/Mithras\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"no reference on the box; covered by KLN:989 on the Greek box (Klein's headword is the English word Mithras) and by Watkins' index entry 'MITHRAS mei-4'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.v. Mithras, Mithraism, mithridate (printed p.~990)\", \"stance\": \"supports\", \"note\": \"'Mithras, n., the Persian god of light. — L., fr. Gk. Μίθρας ...' and 'Mithraism, n., the worship of Mithras. — See next word and -ism.' — the English lemma and its derivative.\"},\n            {\"src\": \"AHD\", \"where\": \"Watkins 1985, index (AHD_watkins1985.txt l.1877) and s.v. mei-4\", \"stance\": \"supports\", \"note\": \"'MITHRAS mei-4' and 'Old Persian Mithra-, name of a god (< \\\"contract\\\" < \\\"bond\\\"): MITHRAS' — the English word is listed as a reflex of the root, exactly as the chart's bottom row claims.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-327.json > /dev/null && echo \"JSON OK\"",
 "description": "Write and validate verification JSON"
}
```


### [2026-09-07T16:10:59.185Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T16:11:03.673Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 tools/verify_check.py 327",
 "description": "Run verify_check for page 327"
}
```


### [2026-09-07T16:11:04.999Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'confirmed': 14, 'transcription_suspect': 2, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'partial': 2, 'not_checked': 6}
books consulted: {'partial': 8, 'supports': 35, 'contradicts': 1, 'silent': 5} | by book: {'KLN': 8, 'SKT': 4, 'BRT': 3, 'KNT': 3, 'WLD': 3, 'LAT': 3, 'HUB': 3, 'POK': 3, 'AHD': 2, 'LKT': 2, 'DEV': 2, 'HRN': 2, 'MON': 2, 'ARY': 2, 'LEW': 1, 'AFA': 1, 'RCH': 1, 'PHN': 1, 'WEB': 1, 'PHD': 1, 'NYB': 1}
```


## [2026-09-07T16:11:13.406Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json\np='data/verification/page-327.json'\nd=json.load(open(p))\nn=[x for x in d['entries'][0]['nodes'] if x['id']==8][0]\nfor c in n['consulted']:\n    if c['src']=='WEB':\n        c['src']='Etymonline'\n        c['where']='etymonline.com s.v. communism (archived via fetch_source.py)'\njson.dump(d,open(p,'w'),ensure_ascii=False,indent=2)\nopen(p,'a').write('\\n')\nEOF\npython3 -m json.tool data/verification/page-327.json >/dev/null && python3 tools/verify_check.py 327",
 "description": "Relabel Etymonline consult and re-check"
}
```


### [2026-09-07T16:11:14.996Z] TOOL RESULT

```
nodes verified: 18/18
node verdicts: {'confirmed': 14, 'transcription_suspect': 2, 'plausible': 2}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 16, 'partial': 2, 'not_checked': 6}
books consulted: {'partial': 8, 'supports': 35, 'contradicts': 1, 'silent': 5} | by book: {'KLN': 8, 'SKT': 4, 'BRT': 3, 'KNT': 3, 'WLD': 3, 'LAT': 3, 'HUB': 3, 'POK': 3, 'AHD': 2, 'LKT': 2, 'DEV': 2, 'HRN': 2, 'MON': 2, 'ARY': 2, 'LEW': 1, 'AFA': 1, 'RCH': 1, 'PHN': 1, 'Etymonline': 1, 'PHD': 1, 'NYB': 1}
```


## [2026-09-07T16:11:32.098Z] AGENT

Page 327 (book p. 297) verified — `data/verification/page-327.json`, `verify_check.py 327` shows 0 PROBLEM lines.

**Counts:** 18/18 nodes — 14 confirmed, 2 plausible, 2 transcription_suspect; both roots confirmed. Ref checks: 16 supports, 2 partial, 6 not_checked. 21 books consulted (35 supports, 8 partial, 1 contradicts, 5 silent).

**transcription_suspect (both are the book's own misprints — extraction is faithful):**
- Entry 0 #2 Latin `se-mitita` — no such Latin word; = sēmita. The 600 dpi crop confirms the page prints "se-mitita" (dittography). `error_in: book`.
- Entry 0 #7 Latin `migâre` — = migrāre; the page really prints "migâre" without the r (Nourai's own AHD source has migrāre). Same box also prints `commŭnis` with a wrong breve for commūnis. `error_in: book`.

**plausible:**
- Entry 0 #3 Arabic samt < Latin sēmita — Klein's direct route; Wiktionary routes it via Aramaic sēmiṭā with later reanalysis to root س م ت, and Lokotsch/Devic/Arab lexicographers treat samt as native.
- Entry 0 #10 English "common, communicate" hung under French *communisme* — communism/communist are from French, but common (< OF comun) and communicate (< L. communicāre) attach straight to Latin in Watkins/Klein; a layout artefact.

**Notable positives:** Nourai's POK:710/713/715 are precisely Watkins' three references under mei-1; POK:710 mei-4 "to bind" matches Mei 4 verbatim; KLN:953 (s.v. "mean, of low rank") and KLN:989 (s.v. Mithras) both check out once the vol.-II leaf offset of the 1966 scan is corrected (leaf ≈ p/2 + 34, not +12, in vol. II — worth adding to refs_online.json). BQT:2060 confirmed against the printed numeral, including Mo'in's footnote "در سانسکریت mitra، اوستا و پارسی باستان mithra «بارتولمه ۱۱۸۳»" and a Mithra-statue plate; image + my transcription saved to `sources/refs/ocr/BQT/2060.png` / `2060.vision.txt`. Root-level note flags the live Pokorny ("bind") vs Meillet/Benveniste ("exchange") dispute over *mi-tro-, and Mann's isolated *mitros "mild".

**No extraction errors found** — the JSON matches the printed page throughout (page image archived at `sources/refs/ocr/BOOK/327.png`). 9 web pages archived via `fetch_source.py`.
