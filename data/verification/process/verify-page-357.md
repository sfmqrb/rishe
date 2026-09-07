# Verification process log — verify-page-357


## [2026-09-07T18:18:03.475Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 357 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-357.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-357.json. Write /home/sfmqrb/git/rishe/data/verification/page-357.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 357` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T18:18:05.353Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T18:18:05.970Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T18:18:05.988Z] TOOL RESULT

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


## [2026-09-07T18:18:06.848Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-357.txt"
}
```


### [2026-09-07T18:18:06.867Z] TOOL RESULT

```
1	=== PDF page 357 (book page 327) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Nek 1 : to destroy  (refs POK:762)
4	#1 (parent #0) [Sanskrit] refs=POK:762; BQT:1471; HRN:285 | nâša : to disappear ; pra-nača : to be finished ; pra-nač : absent, absent minded
5	  #2 (parent #1) [Persian] refs=HRN:182; BQT:1471 | farnâs «فَرناس» : dumb, crazy
6	#3 (parent #0) [Avestan] refs=POK:762; KLN:1059; SYN:290; KNT:192 | nasayeti, nashta : disappear ; nasu, nas 1 : corpse, decayed body ; nasu-pâka : corpse burner ☞Pekw
7	  #4 (parent #3) [Pahlavi] refs=SNS:272 | nasâ, nasây : corpse
8	    #5 (parent #4) [Persian] refs=BQT:2136; MON:4714 | nasâ «نَسا» : corpse, corruption
9	#6 (parent #0) [Old Persian] refs=KNT:192,193 | nath : perish ; vi-nath : injure, harm ☞Wi
10	  #7 (parent #6) [Pahlavi] refs=BQT:1836; SNS:282; MAG:186 | vinâs, vinâh, gunâh : destruction, sin
11	    #8 (parent #7) [Persian] refs=BQT:1836 | gonâh «گناه» : sin
12	    #9 (parent #7) [Arabic] refs=VDQ:38; MAG:186 | jonâh : sin
13	      #10 (parent #9) [Persian] refs=MON:1243,1245 | jonâh «جناح ( جنحه )» : sin
14	#11 (parent #0) [Latin] refs=AHD | nocĕre 2 : to harm ; noxa : injury
15	  #12 (parent #11) [English] refs=None | nuisance, innocent ; noxious, obnoxious
16	#13 (parent #0) [Greek] refs=AHD | nek-tar : death overcoming drink ☞Ter 1
17	  #14 (parent #13) [English] refs=None | nectar, nectarine
18	--- entry 1 ---
19	ROOT Nek 2 -> redirect to Neku
20	--- entry 2 ---
21	ROOT [Sanskrit] Někš : to pierce  (refs HRN:238)
22	#1 (parent #0) [Pahlavi] refs=BQT:2228; HUB:104 | něš : sting ; něš-tar : a sharp, pointed tool ☞Der 1
23	  #2 (parent #1) [Persian] refs=BQT:2228; SYN:565 | nîš «نیش» : sting ; nîštar «نیشتر ، نشتر ، نیشدر» : a sharp tool, tooth
24	
```


## [2026-09-07T18:18:10.407Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-357.json",
 "description": "Read source JSON page 357"
}
```


### [2026-09-07T18:18:10.444Z] TOOL RESULT

```
{
  "pdf_page": 357,
  "book_page": 327,
  "entries": [
    {
      "root": {
        "name": "Nek 1",
        "lang": "Indo-European",
        "refs": "POK:762",
        "gloss": "to destroy"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:762; BQT:1471; HRN:285",
          "words": [
            {"translit": "nâša", "gloss": "to disappear", "script": null},
            {"translit": "pra-nača", "gloss": "to be finished", "script": null},
            {"translit": "pra-nač", "gloss": "absent, absent minded", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HRN:182; BQT:1471",
          "words": [
            {"translit": "farnâs", "gloss": "dumb, crazy", "script": "فَرناس"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "گفت نقّاش چونکه نشناسم - که نه دیوانه و نه فرناسم",
            "poet": "Onsorî Balxî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:762; KLN:1059; SYN:290; KNT:192",
          "words": [
            {"translit": "nasayeti, nashta", "gloss": "disappear", "script": null},
            {"translit": "nasu, nas 1", "gloss": "corpse, decayed body", "script": null},
            {"translit": "nasu-pâka", "gloss": "corpse burner", "script": null, "see": ["Pekw"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "SNS:272",
          "words": [
            {"translit": "nasâ, nasây", "gloss": "corpse", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:2136; MON:4714",
          "words": [
            {"translit": "nasâ", "gloss": "corpse, corruption", "script": "نَسا"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "نَسا و پلیدی بدانجا برند - که مردم بران راه برنگذرند",
            "poet": "Zartosht-Nâmeh"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:192,193",
          "words": [
            {"translit": "nath", "gloss": "perish", "script": null},
            {"translit": "vi-nath", "gloss": "injure, harm", "script": null, "see": ["Wi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Pahlavi",
          "refs": "BQT:1836; SNS:282; MAG:186",
          "words": [
            {"translit": "vinâs, vinâh, gunâh", "gloss": "destruction, sin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "BQT:1836",
          "words": [
            {"translit": "gonâh", "gloss": "sin", "script": "گناه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "Arabic",
          "refs": "VDQ:38; MAG:186",
          "words": [
            {"translit": "jonâh", "gloss": "sin", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:1243,1245",
          "words": [
            {"translit": "jonâh", "gloss": "sin", "script": "جناح ( جنحه )"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "nocĕre 2", "gloss": "to harm", "script": null},
            {"translit": "noxa", "gloss": "injury", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "nuisance, innocent", "gloss": null, "script": null},
            {"translit": "noxious, obnoxious", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "nek-tar", "gloss": "death overcoming drink", "script": null, "see": ["Ter 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "nectar, nectarine", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Nek 2",
        "redirect": "Neku"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Někš",
        "lang": "Sanskrit",
        "refs": "HRN:238",
        "gloss": "to pierce"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT:2228; HUB:104",
          "words": [
            {"translit": "něš", "gloss": "sting", "script": null},
            {"translit": "něš-tar", "gloss": "a sharp, pointed tool", "script": null, "see": ["Der 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:2228; SYN:565",
          "words": [
            {"translit": "nîš", "gloss": "sting", "script": "نیش"},
            {"translit": "nîštar", "gloss": "a sharp tool, tooth", "script": "نیشتر ، نشتر ، نیشدر"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "سرو دارد و نیشتر چون گراز - نیارد شدن پیل پیشش فراز",
            "poet": "Ferdowsî"
          }
        }
      ]
    }
  ]
}
```


## [2026-09-07T18:18:10.627Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T18:18:10.665Z] TOOL RESULT

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


## [2026-09-07T18:18:17.071Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','HRN','KLN','SYN','KNT','SNS','MON','VDQ','MAG','AHD','HUB']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:700])\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-07T18:18:18.497Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-312.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\"",
 "description": "Look at existing verification example"
}
```


### [2026-09-07T18:18:19.040Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archiv

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — 

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

VDQ {"title": "Fereydun Badreh'i (tr.), Vazheha-ye Dakhil dar Qor'an-e Majid (Persian translation of Jeffery FVQ with notes), Toos 1372/1993", "kind": "website", "url": "https://noorlib.ir/book/view/12868?pageNumber=<N>&viewType=pdf (page images; viewType=html also exists) ; info: https://noorlib.ir/book/info/12868 ; ketabnak.com/book/51136 (download blocked)", "lookup_hint": "noorlib viewer is JavaScript-rendered (WebFetch/curl get only the site chrome); needs a browser. Since it is a translation of FVQ, verify the substance via FVQ (same entry order); page numbers differ.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "Not on archive.org. Also on ghaemiyeh (ghboo

MAG {"title": "G. Widengren, Muhammad, the Apostle of God, and his Ascension (King and Saviour V), Uppsala 1955, ch. VIII 'Iranian elements in the Kuranic vocabulary'", "edition_found": null, "kind": "archive_restricted", "url": "https://archive.org/details/muhammadapostled0000geow (1955, lending) ; HathiTrust pst.000011130420 search-only", "identifier": null, "local_file": null, "page_offset": null, "lookup_hint": "HathiTrust has it search-only (limited view); Google Books ids -r4rAAAAIAAJ / h20wAAAAYAAJ are snippet view.", "notes": "RE-SEARCH 2026-09: borrowable only; not in DiVA; Google no view."}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
```


### [2026-09-07T18:18:20.437Z] TOOL RESULT

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
{
 "entry": 2,
 "root": "Leuk, Leuqos",
 "verdict": "confirmed",
 "modern_form": "PIE *leuk- (Pokorny leuk̂-) 'light, brightness; to shine, to see', with the thematic *leuk-o-s (Gk. leukós) that Nourai calls 'Leuqos'",
 "note": "Root, language label, gloss and page reference are all right. Pokorny, IEW 687-690, lemma leuk̂- (leuk-), Meaning 'bright, to shine; to see' (References: WP. II 408 ff.), listing exactly the material of this chart: Av. raocah-, OP raucah-, Av. raoxšna-, Lat. lūx/lūmen/lūna/lūstrum/lūstrāre, Goth. liuhaþ / OHG lioht / OE lēoht, Skt. loka-. Watkins/AHD: \"leuk-. Light, brightness. ... [Pok. leuk- 687.]\" — so POK:687 is the exact page. Kent (KNT:205), Nourai's second reference, gives the same root in the older notation pIE *leugos s.v. raucah-. 'Leuqos' is Nourai's spelling of the *leuk-o-s form (Gk. leukós 'white, bright', Skt. loka- 'open bright space, world', Lat. lūcus 'grove'); it is not a separate root. Cross-cutting remarks: (1) the chart's strongest link, Persian rūz/rōšan/afrūxtan and the Arabic loan rizq, is fully confirmed; (2) two Persian items in the Persian box (آرش, درفش ۱) and one Avestan item (a-raxša, plus the unattested raoč-xšaema) are not supported by modern sources; (3) the Sogdian box mixes an inherited word (rwxšn) with a Sanskrit loanword (δwk' < Skt. loka); (4) the Germanic box misprints the reconstruction (liuhtam for *leuhtam); (5) on the printed page the Old Persian box has an arrow into an empty, unlabelled box that the JSON does not record.",
 "note_fa": "ریشه، برچسبِ زبان، معنی و شمارهٔ صفحه هر چهار درست است: پوکورنی در «فرهنگ ریشه‌شناسیِ هندواروپایی» صفحه‌های ۶۸۷ تا ۶۹۰ ریشهٔ leuk̂- را با معنای «روشن، درخشیدن؛ دیدن» می‌آورد و همان داده‌های این نمودار را برمی‌شمارد: اوستایی raocah- و raoxšna-، پارسی باستان raucah-، لاتین lūx و lūmen و lūna و lūstrum، گوتیک liuhaþ و انگلیسی کهن lēoht، و سنسکریت loka-. واتکینز نیز ذیل leuk- همین ارجاع «پوکورنی ۶۸۷» را دارد. «Leuqos» صورتِ ستاک‌دارِ *leuk-o-s است (یونانی leukós، سنسکریت loka-، لاتین lūcus) و ریشهٔ جداگانه‌ای نیست. به‌طور کلی: پیوندِ فارسی «روز، روشن، افروختن» و وام‌واژهٔ عربیِ «رزق» کاملاً تأیید می‌شود؛ اما «آرش» و «درفش ۱» در جعبهٔ فارسی و «a-raxša» و «raoč-xšaema» در جعبهٔ اوستایی پشتوانهٔ امروزی ندارند؛ جعبهٔ سغدی یک واژهٔ میراثی (rwxšn) را با یک وام‌واژهٔ سانسکریت (δwk' از loka) درآمیخته؛ و در جعبهٔ ژرمنی صورتِ بازسازی‌شده غلط چاپ شده است (liuhtam به‌جای *leuhtam).",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/lewk-",
  "https://en.wiktionary.org/wiki/%D8%B1%D9%88%D8%B2"
 ],
 "ref_check": [
  {
   "ref": "POK:687",
   "status": "supports",
   "note": "POK_full.txt, block 'Root / lemma: lehuk- (*lehugh-)', Meaning 'bright, to shine; to see', Page(s): 687-690 — with \"rocas-, rocis-, Avestan raocah-, ap. raucah- n. 'light, radiance, esp. of heaven', Avestan raoxšna- 'gleaming'\", \"Latin lūmen 'light' from *leuk-s-men; lūna 'moon goddess' (*leuksna)\", \"lustrum ... lūstro, -are 'to light up, illuminate'\
```


## [2026-09-07T18:18:40.077Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 76[0-9]\" POK_full.txt | head -20",
 "description": "Find POK page 762 lemma"
}
```


### [2026-09-07T18:18:40.123Z] TOOL RESULT

```
62131:Page(s): 760 
62152:Page(s): 760 
62174:Page(s): 761 
62205:Page(s): 761 
62237:Page(s): 761 
62255:Page(s): 760 
62275:Page(s): 760 
62282:Page(s): 760 
62331:Page(s): 762 
62398:Page(s): 762-763 
62573:Page(s): 763-764 
62598:Page(s): 764 
62645:Page(s): 764 
62732:Page(s): 765 
62749:Page(s): 765-766 
62779:Page(s): 766 
62818:Page(s): 766-767 
62833:Page(s): 768 
62861:Page(s): 768 
62890:Page(s): 768-769
```


## [2026-09-07T18:18:41.002Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *238\\. \\|^ *182\\. \\|^ *285\\. \" HRN.txt | head",
 "description": "Find Horn entries 182, 238, 285"
}
```


### [2026-09-07T18:18:41.053Z] TOOL RESULT

```
2437:238. {2)hum, baf'^) *Eule\ n^\
2795:285. pulten 'kochen, Praes. pez-em^ pezamden,
10736:182. ftiaslnitan (aw. [/^maet- , mi^naitl entsprechend ;
11010:182. spaxff *verleumderisch', spazgth 'Verleumdung' (Men.,
11364:238. ^and 'Gau, zandpat (AW.-Komm.).
```


## [2026-09-07T18:18:45.789Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62290,62400p' POK_full.txt",
 "description": "Read POK 762 lemma"
}
```


### [2026-09-07T18:18:45.846Z] TOOL RESULT

```
Material: Old Indie nasyati, nasati^ gets lost, disappears, passes away ', nasayat/" makes 

disappear, ruin' (lengthened grade compared with Latin noceo^ harm'), Avestan nasye/t/' 

disappears ', participle Old Indie nasta-' lost ', Avestan nasta- ds. (= Latin e-nectus), 

nasista- " most perishable ', nas- f. 'need, misfortune' (= Latin nex, gr. vsK-rap, veke^; Old 

Indie -nasM].), nasu- 'corpse, carrion ' (= gr. v£ku(;, Latin nequ-alia; compare *nRu-\v\ Old 

Irish ecetc), lengthened grade Old Indie nasa-m. ' das Zuniehtewerden '; gr. v£K£(; vcKpoi 

Hes. (therefrom vekqc; ' heap of corpses ', example bzmc,), vekO^, v£Kp6(; 'corpse', vwKap 

n. ' sluggishness, Todesschlaf '; about vsvrap 'drinkof the gods ' s. Kretschmer Anz. Osterr. 

Akad. 1947, Nr. 4 (to Tocharian B /75/r/'god'?) and Thieme Studien 5 ff. (' uber den Tod 

hinwegrettend '?); Latin nex, nec/st 'death, murder', therefrom denicales feriae^ de nece 

purgantes ', need, -are^ kill/murder; put to death; suppress! destroy; kill (plant); quench/drown (fire) ', 

e-/7ec/^5 'exhausted', whereof enectare' kill, torment, smite'; pernicies^ ruin; disaster; pest| 

bane; curse; destruction! calamity; mischief, internecies, -nec/um ds.; noceo^Uarvnl hurt; injure 

■ 
(with DAT) ', s-Konj. nox/t, noxai. 'hurt! injury; crime; punishment! harm '; nequalia^ detrlmenta ' 

(due to stem neRu-)\ Old Irish ec, bret. ankou, corn, ancow, cymr. 5/7^e^ 'death' {*nRu-)\ 

bret. (Vannes) nege/n^s\ay', Old Icelandic Nagl-far^ Totenschiff '; Tocharian A nak-^ die, 

wilt, wither ', B 'destroy', IVIed. ' die, wilt, wither '; about Latin necesse^ necessary! essential; 

unavoidable! compulsory! inevitable; a natural law; true ' see below sed-. 

References: WP. II 326, WH. I 153 ff.; 

See also: s. also ank-1 above S. 45. 

Page(s): 762 

Root / lemma: nelc-fl-), nolc-t-s {* hounk'*-(t-}) 

Meaning: night 

Grammatical information: stem nok'i-i. (originally neutr.??), nok'ii-, nok'iu-i., nok'i(e)ru. 

Note: about ablaut forms see below 

Root/ lemma: nek^-ft-), nok^-t-si* hounk''-(t-))\ night' derived from zero grade of Root/ 

lemma: ong^-Ao anoint, dark ointment' : Old Indie akta- [f] 'night' (RV 01 .062.08) {2}; aktu- 

[m] 'flowing; ointment; (light or dark) color; (final part of the) night' (RV+) {3}. 

Material: Old Indie nak{*nakt) Nom. 'night' {nagjihTte), naktai. Du., naktam My. solidified 

Akk. ' at night ', Instr. PI. naktabhih 6s. (imitation from ahabhih), Akk. PI. naktJh^ nights '; 



gr. vu^, vukt6(; f. "night', in compound vukti-, vukto-, vuktojp Adv. " at night, by night ' 
(*Akk. shaped as u5u)p), vuKT£p6(;, vuKT£piv6(; " nocturnal ' (: Latin nocturnus); unclear are 
vuxa vuKTOjp Hes., horn. £ivavux£<; " nine nights through ', £vvuxo(; " nocturnal ', navvuxiO(; " 
lasting the whole night ', auTOvuxi "in the same night'; 

alb. nate, /7e/e PI. "night'; 

Maybe alb. per-nate^ every night' : mcymr. peu-noeth^e^ch night'. 

Latin nox, /70c//5 "night' (Gen. PI. noct/um /-stem, but distinct conservative stem in Adv. 
nox' at night, by night ' from Gen. *nokt-es, -os)\ nocturnus " nocturnal ' (: vuKT£piv6(;, 
vuKTOjp); of stem *noktu-. Latin noctu^by night', noctua^ a night-owl, an owl '; 

Old Irish i-nnochV hac nocte ', mcymr. peu-noeth' each night ', trannoeth^ during the 
following day ', acymr. henoid, cymr. he-no^ hac nocte ', corn, haneth. Middle Breton 
henoz6s.\ cymr. corn, nos, bret. /7c»z "night', probably from *nokf-s u- cymr. neithiwyr, 
neithwyr{cov\{a\v\s /7tyj//' "evening') "last night', corn. /7e/7^es Middle Breton neyzor, nbr. 
neizeur(is.\ 

Gothic naMs {Dat. PI. nahtam after dagam). Old Icelandic nott, natt. Old High German 
Old Saxon naht. Old English neaht, /7//7/"night' (conservative stem). Old English nihterne^ 
nocturnal '; 

Lithuanian /7a/r//s (conservative Gen. PI. naktu), Latvian nakts. Old Prussian nakt/'n {Akk. 
Sg.) "night', nakftjv-yne ^n\ghthosie\', nakftjvot/ ^\odge, stay ovevnight' , nakv/nas' accommodate 
for the night'. Old Bulgarian /7c»s/i. "night', russ. netopyr Nachtschmetterling, bat'; 

Hittite neku-' dawn'; Gen. ne-ku-uz {nekuz) "night'; Tocharian A n[a]ktim^ nocturnal ', B 
nekciye " the evening, during the early nighttime hours '; 

zero grade: Old Indie 5/r/a"night' (perhaps /7-stem), aktu-m. " darkness, night, light, ray' 
(actually "dawn, twilight'), compare in latter meaning Gothic uhtwd{: Latin noctu etc.), Old 
Icelandic ofta. Old High German Ohta{uohta), Middle High German uhte{uohte). Old 
Saxon uthai.. Old English uth(a)xr\. " early morning time ', Gothic uhteigs' early '; 

another ablaut grade *onk"t- seems Lithuanian anksti " early, matutinal ', is anksto " from 
early on ', ankstus M]. "early, matutinal'. Old Prussian angstainai, angsteina Mn . " early in 
the morning '. 



References: WP. II 337 ff., WH. II 181 ff., Trautmann 9, 193, Specht Indo Germanic Dekl. 

11. 

Page(s): 762-763 

Root / lemma: ne1, ne, nei{*houn)
```


## [2026-09-07T18:18:50.408Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '62276,62292p' POK_full.txt",
 "description": "Read POK lemma header for nek-"
}
```


### [2026-09-07T18:18:50.458Z] TOOL RESULT

```
Root / lemma: ne/-3, ni- {*houn-) 



See also: see above S. 312 f. {en-). 
Page(s): 760 



Root / lemma: neR- {*hounR-) 

Meaning: death, dying; dead person 

Material: Old Indie nasyati, nasati^ gets lost, disappears, passes away ', nasayat/" makes 

disappear, ruin' (lengthened grade compared with Latin noceo^ harm'), Avestan nasye/t/'
```


## [2026-09-07T18:19:03.584Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD nek-1 ===\" && grep -n -A12 \"^nek-\" AHD_watkins1985.txt | head -60",
 "description": "Grep Watkins AHD for nek-"
}
```


### [2026-09-07T18:19:03.634Z] TOOL RESULT

```
=== AHD nek-1 ===
```


## [2026-09-07T18:19:05.112Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT nasu ===\" && grep -n \"nasu-\\|nasāv\\|nasu\\b\" BRT.txt | head -30 && echo \"=== BRT nas- corpse ===\" && grep -n \"nas-p\\|nasupāka\\|nasu-pāka\\|nasupaka\" BRT.txt | head",
 "description": "Grep Bartholomae for nasu"
}
```


### [2026-09-07T18:19:05.216Z] TOOL RESULT

```
=== BRT nasu ===
7829:mit  /r>l,  frB  i)  'erreichen,  treffen':  nsit gdüahe  .  .  tbalxB  frqstißna  (sd.)  fräsnu- y,lt  Yti/.  s;  —  cvat  antar?  *rurSus  aisa druxs  yä  nasu/  ax/i^a  .  .  fräsnaotti  V. J.27;  28;  —  ye%i  nsii  Aarv^rvm  baraiti aztaöa  hi  vfspä  hSirÜTl  fräsnaotti  ".  .  so trifft  er  damit  alle  Weiber"  (?)  V. />  19; —  nSit  ahyä  mä  ahris  (sd.)  syad^anäis frösyaii*    Y.46.8.  2)    'herzu-,    hinzu-
10301:—  II  adam  käram  *»:;(«'.?  (LS.)*>  avasiäyain "ich  stellte  das  Volk  (wieder)  an  seinen richtigen  Platz"  Bh. /.  14;  14'; —  .\ismim ..  adamsim  *°^avä'''>  tnyasädayam  ",  .  ich stellte  sie  (die  Erde)  wieder  an  ihren richtigen  Platz"  Q.6.^.  a)  mit  däitya- Adj.:  *zaotars  (sd.)  duityS  'tus  mawinya nmänahe  N.  ;<?;  J^J;  —  ys  ätnm  nasu- piihin  däitim    -tum   avi  ava.baraiti  V.S.
11762:—  /?  . .  aogazdastima  bavainti  ySi  nasu.- kirfta  V,  7.  26f.J;  —  tä  avil yi  rJtayJ V.36;  Y.  60.  3;  —  haomS  t»mäiyim  hr>- s3nTftt  apaxsa'hnm  (^A.)  nHähayalY.g.z^;
11943:zasta  ..hl..  frasttdhay?n  . .  ap»r3ttayBkahe ahe  (Sp. 6  m.)  havayhss  'nvB  V.  16.T,  —  im Gegensatz  lu  i'awj«-:  malsnta  yalibyS  alte I  nasu.kasa  frasnylnte  var^säsla  'nümca ". .  Leib(sva.Hau  t  J  und  Haare"  V.&  1 1 ;  Vd.4 ;
14883:—  mä  tg  nr«(sd.)  ume  'ti  Y.  10. 17;  — Jtva..tanBm..nidaiama?..iar»zistaisva[ca] 'ti  gatusva  V.  d).  44  f. ;  —  S  ritlm  gäma  (sd.) frabarat ../warnte  'ti  ntäatai tüirfm gäma frabarat  .  .  atiayralsva  raocshva  itidaiät' H.2.15'";  IS',  V.(5.si,  Ä76;  —  ^avä-\ dasii  usmaya{sA)patiy^^  akunavam  Bh. J.8;  14,  2.  13,  14.  b)  auf  die  Frage wo?:  rätayd  Vtspäku  'ti  banzaku  vispahu va^anayaku  spasS atjhsireYx.io.i,^,'*';  — haoma  raüsaisd.)  gara  'tiY.10.4;  — yaiA^ nmän>m  .  .  v^t^m  barvzi/ie  °ti  banzahi Aarai'^yö paiti  (Sp.  824  m.)  barpzayä  Y.57, a  I ;  1 9 ; — yim  yaz?nte  ra%aistärB  baniassu *ti  aspanqm  Yt.  10.11;  —  l?m  yazata  . . akurö  .  .  xaranasu  -ti  fraspaiti  Yt  J5.  2 ;  i 2 ;  —  tarn  yazata  .  .  frarfrase  kankaine °ti  *aaAä  s>mö  Yt5.  41;  —  nars  asaonS urva  urvarahuca  'ti  . .  sa^ayäti  H.  2.  7 ; 'S;  —  drp/ya(sd.}  'ti  zöaraAi  nmänahe.. V.ig.4;  11;  —  .  .  tnasyatahB  al^a  (sd.) *yBi  *aparaya  'ti  *mastrrjnya  (sd.)  F. je;  c.  a)  Die  räumUche  Vorstellung tritt  zurück:  mihr»m  . .  *yahmi  'ti  /ihrrm
15109:•  j.  paitis.x''araoa- "  n.  'der  obere  Teil des  Gesichts',  Stirn  und  Ohren  umfassend: yaica  apd .  .  *pasca.vay6anjm  fiaiti.jasaiti .  .  paitisa  'mm  .  .  äruxs  yä  nasu^  upa.- dvqsaiti  V.  8.  43;  44,  g.  16';  —  upa  vä iiasui  rat^wat  . .  'naöa  V._j.  14'^
18783:Sü.:  nirgaminyak  (NP,).  —  0  Das  ä  »om  NS, •«i/j  E.  dageg.  lat.  «ö-.  —  >)  Gdn.  KZ.  sÄ  si  i. •  j.  nasav-  f.,  m.  'Leiche,  Leichnam'  (von Menschen  und  Tieren);  'Leichenteil':  nSii spsMrjtS  nsit  . .  °su/  nanm  nötl  *astara- yäti  yaica  alte  °jai^  ('Leichenteile')  ^5  sps.- birslaca . .  'tus  nanm  *3stärayantfm  äahäi Uar^Jtäitya  .  .  visps  anhul . .  p^/SJanu/ frSria  ankam  °sunqm  ('Leichen')  ys  paiti äya  zima  irfnhar^V.j.if.; — jaica  aste 'sävS  fri^yeilica  puyäica  Y.6.28;  —  iat iä  nara  yaoidayqn  anhm  .  .  yä  'säum ava.h>Tvta  ssnS  vä  paraAristahe  tnasyeke vä  V.iV.3S;  33,  97,  5.42;  — >aÄ<i  narim alavarum  .  .  'sui  (AP.)  aoi  ava  *%ravTt (Sp.8o2U.)P.2y;  — yai  aesa  'sus  anaiwi.- ynixta  sanS  vS  ..  V.J. 2^;  30; — yt . . matdayasna  ,  .  taci.apaya  (sd.)  's3um^^ frajasqn  .  .  aS^a  S/s  ayaoidya  .  .  yavat azsa  'sus  niibpnla;  us  haca  'savö  (GS.) altavat  apat  Aaca  niiläraym  (Sp.  939  o.) ,  .  pasia  'savs  (GS,)  niüjn^i  .  .  a/i yaoidya  bavaiti  V.  6.  26—32;  —  pasi'a  ., 'Säum  avaJian^mtiisA.)  sps/um  vä  raoitm vä  vfhrkim  wa  V.  5.  J;  —  nara  .  .  yä 'Säum  matgu^qtn  äp»m  ä  vä  älnm  ä  vä ,  .  frabarmti  V.  7.  25;  —  yat  .  .  mazda- yasna  . .  ätnm  nasu.paktm  /ra/asan  'sBm hqmpa^qn  'sUm  /i<lvayqn{sA.)  V.ff.j^;  — «äV  vatihs  ..  iyaöimm  v^myeiti  ydOBii^ puhrake  .  .  frä  nast>m  (sd.)  'sam  pacät  \ V.  76. 1 7 ;  —  nara  . .  yä  'säum  fraauharät  I sünS  vä  .  .  masyefu  vä  V.  7.23;  —  visp^m  j ä  ahmäi  'sunqmca  aiwi.varsianqm  (sd.)  j V.  5, 14;  —  apim  zazämi  aztm  yS  akurS\ mazdä  . .  avi  "ssm  (in  koll.  Sinn)  vazämi  1 . .  tä  ha%ra  frafrävayämi  avi  zrayn  päi- 1 Hifm  (sd.)  V.  5. 1 7  f. ;  1 5  f.  A)  Name  der  \ Leichenhexe*':  ial  .  .  'sus  upa.dvqsaitii ..  i^ari  pasca  para.iristlm  ..  us  haca  6ao%S ayät  .  .  'SUS  upa.dvqsaiti  apäx^raiibyS naHnaeibyB  *maxsi.hhrpa  arrjaitya  V.  7. I  £;  —  yat  aSe  yä  sps.jataca  .  .  coatit>m pascaüa  srvätum  .  .  'sus'  upa.dvqsaitii  .  . asnyehe  (sd.)  pascaita  anyehe  ra^ws  .  . 'SUS  upa.dvqsaiti  V,  7. 3  f. ;  —  kuha  a!tat •sus  (statt  Aide.)  '>  pirTttäne  yä  haca  irista upa  jvanifm  upa-rag^waiti  (sd.)  V.  jo.  i, *9-A1^^;  —  "/"  vä  'sui  ra/hwät  (sd.) nänAanat  Aaia  V._J.  14;  p.  40;  —  /rä  el dvqsaiti  . ,  'sui  yai  dastmim  /räihaoiÜ naum»m  paiti.rathwayHH  (sd.)  V.5.  28; 27-32",  8.  41",  70,  71,  g.  15-24  (oft);
18791:•  j.  nasu-kaäa'  m.  'Leichenwärter' *>:  alte
18800:V,  7, 26.  •  J-  nasu-spa-  Adj.  'Leichen  ein-,  ver-
18806:nasa>palca-    Adj.    'Leichen(teile)      Bedcatet  nasu-ifi-   tH   cig.  ■Leichen  : kodiend':  ava  tut?m  *k^m  JanaOa    V.S.       werfend'?  VgL  die  SteDe  ait  pahis^^äiay..  ~ 74.  a)  vom  Feaer  'zmn  Kochen  von       ^-  **""  *"*''"'^
18819:•  j.  nasu-spaeya- '1  Adj.  im  Kochen  vonjnngen;  s.  Gdn.  GIrPh.  a.  17. Leichen(teilen)  bestehend';  caxr>m  . .  atu      *najta-  m.,  s.  .)  (eig.  wohl  'Bündel',  vgl.  alt. ake  paityänm  yräktntaat  anrO  ntamyul  ? .       noiäm  ich  binde',  «air 'Ring')  ■> ;  mp.  naJ*>)
18864:•  j.  "yaAmi  gashe  k^sa  vasta  Aaoa  nara faha  mara  Ada  nä.tanasuä"  Yt.  i3. 8:  -?-■>.
19555:•  j.  maxäi.b3r«ta-  Adj.  'von  Riegen  ver- tragen, fortgeschleppt':  '0  nasu/  Y.S-i; j.  14  PüZ.;  —  aite  nasävö  ya  .  .  'taca nasui  V.  5. 4,
20787:..yafsam'*>  *ya/>iwa/a  urvqnS  ..  Yt /J. 148;  148;  —  ftWfJ  äfys  dö^räbyS  yä ahurahe  mazdä  Y.  68.  2a;  —  änhqm  nasu- nqm  ..ya ..iriri^ar?  V.5.4;  —  avi  ankam- cit  yä  vatfuhli  yä  äp5  yäsca  urvarS yäsia  ../ravasayS  ^1.21.  1;  Y.ip.iR;  — aS^qm  uxhanqm  .  .  yäis  (als  Subj.)  yatia /ra'c'a  vaoce  .'.  Y.ii^.io;  «.3;  —  vupe ..  vartuhlf  dämqn  asdonf/ yäis' (ah Obj.) dadä^a  Y,  7/.  10;  —  ärshqm  zao^ranqm ,  .  yä  (APn.  statt  f.)  mavSya  nipärayänti Yt/7.  54;  —  ahmäi  nmanai  .  .  "yahva (statt  LS.)  xsnülä  bavaiti  YL70.28;  — mit  Gen.  pait,:  ahmäi  naimäi  .  .y ahmäi natmanqm  mi^rBJruxi  Yt  10. 19;  —  die Beziehung  ist  ungenau:    haca  ahmät  (Sp.
23641:•  ].  V9hrkö.b9r9ta-  Adj.  'von  Wölfen vertragen,  fortgeschleppt':  'ts . .  nasu/ V. 5.  3J    —    fite  nasavS  ya    .  .    'taca     V,
25492:PQ.:  tUI  kU  niai  iar;  %.  aaiu  V.  3.  14  und DST.  ZA.  2,  3S,  aber  auch  nasu-iasa-.
29517:'schmoren,  rösten':  yal  .  .  Strim  nasu- päk»m  frajasqn  nasBm  Aqmpacqn  natüm hävayqn  "wenn  (sie)  .  .  zu  einem  Feuer kommen,  womit  man  eine  Leiche  kocht  — sie  kochen  eine  Leiche,  sie  schmoren  eine Leiche  — :  .  ."  V.Ä73;  —  mqnaym  aAe ya'ha  ätars  huskim  alsmtm  .  .  aipiJunn- taiti  Aävayeüi  äaiaiti  ".  .  wie  das  Feuer trockenes  Holz  . .  zerstückt,  schmort,  ver- brennt" Y.  71. 8;  —  ya%a  . .  yBim  yHi masyaia  ä^ary^a  :^asta  (sd.)  Auyar>£ (3POA.)'>  gqm^a   ifUstsm  ifaraiti   "wie
=== BRT nas- corpse ===
```


## [2026-09-07T18:19:14.236Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"nek-\\b\" AHD_watkins1985.txt | head -20 && echo \"=== nectar ===\" && grep -n -i \"nectar\" AHD_watkins1985.txt | head",
 "description": "Grep AHD for nek and nectar"
}
```


### [2026-09-07T18:19:14.304Z] TOOL RESULT

```
333:bher-1. To carry; also to bear children. 1. a. Germanic *beran in (i) Old English beran, to carry: BEAR! (ii) Old English forberan, to bear, endure (for-, for-; see per’): FORBEAR; b. Germanic *bérd in Old English bér, ber, bier: BIER; c. Germanic *bér- in Old Norse bdra, wave, billow: BORE’. 2. a. Germanic *barnam in Old English bearn, child: BAIRN; b. Germanic *barwdn- in Old Eng- lish bearwe, basket, wheelbarrow: BARROW!, 3. a. Ger- manic *burthinja in Old English byrthen, burden: BURDEN}; b. Germanic *burthiz in Old Norse burdhr, birth, akin to the source of BIRTH; C. Germanic *burja- perhaps in Old Norse byrr, favorable wind: BIRR}. 4. Compound root *bhrenk-, to bring (< *bher- + *enk-, to reach; see nek-2), in Germanic *brengan in Old English bringan, to bring: BRING. 5. Latin ferre, to carry: -FER, FERTILE; AFFERENT, CONFER, DEFER!, DEFER®, DIFFER, EFFERENT, INFER, OFFER, PREFER, PROFFER, REFER, SUFFER, TRANSFER, VOCIFERATE. 6. Latin pro- brum, a reproach (< “pro-bhr-o-, “something brought before one”; pro-, before; see per'): OPPROBRIUM. 7. Lengthened o-grade form *bhor- probably in Latin far, thief: FERRET!, FURTIVE, FURUNCLE; (FURUNCULOSIS). 8. Greek pherein, to carry: -PHORE, -PHORESIS, -PHO- ROUS; AMPHORA, ANAPHORA, DIAPHORESIS, EUPHORIA, METAPHOR, PERIPHERY, PHEROMONE, TELPHER, TOCOPH- EROL. 9. Greek pherné, dowry (“something brought by a bride”): PARAPHERNALIA. [Pok. 1. bher- 128.]
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
1083:thresh, tread, wear out: TRITE, TRITURATE; ATTRITION, CONTRITE, DETRIMENT; b. Greek teréddn, a kind of biting worm: TEREDO. 2. Suffixed form *ter-et- in Latin teres (stem feret-), rounded, smooth: TERETE. 3. Suffixed form *ter-sko- in Germanic *therskan, *threskan, to thresh, tread, in: a. Old English therscan, to thresh: (THRASH), THRESH; b. Old English therscold, threscold, sill of a door (over which one treads; second element obscure): THRESHOLD. II. O-grade form *tor(a)-. 1. Greek toreus, a boring tool: TOREUTICS. 2. Suffixed form *tor(e)-mo-, hole, in Germanic *tharma in Old High German darm, gut: DERMA2. 3. Suffixed form *tor(g)-no- in Greek tornos, tool for drawing a circle, circle, lathe (> Latin tornus, lathe): TURN; (ATTORN), CONTOUR, (DE- TOUR), (RETURN). III. Zero-grade form *tr- in Germanic *thr- in Dutch drillen, to drill: DRILL’. IV. Variant form *tré-. 1.Germanic *thréw- in Old English thrdwan, to turn, twist: THROW. 2. Greek tréma, perforation: MONO- TREME, TREMATODE. 3. Suffixed form *tré-tu- in Ger- manic *thrédu-, twisted yarn, in Old English thréd, thread: THREAD. V. Extended form tri- (< “trig-). 1. Suf- fixed form *tri-dn-, probably in Latin tid, plow ox: SEPTENTRION. 2. Suffixed form *tri-dhlo- in Latin tribu- lum, a threshing sledge: TRIBULATION. VI. Various ex- tended forms. 1. Forms *tré-, *trau- in Greek trauma, hurt, wound: TRAUMA. 2. Form *tru- in Greek truma, trumé, hole: TRYMA. 3. Form *érib- in Greek tribein, to rub, thresh, pound, wear out (> ¢ripsis, a rubbing): DIATRIBE, TRIBOELECTRICITY, TRIBOLOGY, TRYPSIN. 4. Form *trdg- in Greek trégein, to gnaw: TROGON. 5. Form *¢rup- in Greek trupé, hole (> trupanon, auger): TREPAN!; TRYPANOSOME. 6. Form *trig- possibly in Old French truant, beggar: TRUANT. [Pok. 3. ter- 1071.] tera-2. To cross over, pass through, overcome. Variant *trd-, contracted from “traa-. I. Zero-grade form “*tr()-. 1. Germanic suffixed form *thur-ila- in Old English thyr(e)l, thyrel, a hole (< “a boring through”): THRILL; NOSTRIL. 2. Suffixed form *tra-kve in Germanic *thurh in Old English thurh, thuruh, through: THOROUGH, THROUGH. 3. Greek nek-tar, overcoming death ‘(see nek-'). 4, Zero-grade form *tre- and full-grade form *ter(a)- in Sanskrit tirati, tarati, he crosses over: AVATAR. Il. Variant form ‘*trd-. 1. Latin trans, across, over, be- yond, through (perhaps originally the present participle of a verb *trdre, to cross over): TRANS-, TRANSIENT, (TRANSOM). 2. Suffixed form *trd-yo- in Iranian thrdaya-, to protect, in Middle Persian srdyidhan, to protect, in Persian sardi, inn: CARAVANSARY. III. Extended form *tru-. 1. Suffixed form *tru-k- in Latin trux (stem truc-), savage, fierce, grim (< “overcoming,” “powerful,” “pene- trating”): TRUCULENT. 2. Suffixed nasalized form *tru-n-k-o- in Latin truncus, deprived of branches or limbs, mutilated, hence trunk (? < “overcome, maimed”): TRENCH, TRUNCATE, TRUNK. [Pok. 5. ter- 1075.] terkw-. To twist. Extension of tera-'. 1. Possible variant form *twjerk- in Germanic *thwerh-, twisted, oblique, in Old Norse thverr, transverse: THWART. 2. Suffixed (caus- ative) o-grade form *tork’-eyo- in Latin torquére, to twist: TORCH, TORMENT, TORQUE}, TORQUE?, TORSADE, TORT, TORTUOUS; CONTORT, DISTORT, EXTORT, NASTUR- TIUM, RETORT!, TORTICOLLIS. [Pok. terk- 1077.] terp-. To satisfy oneself. Greek terpein, to delight, cheer: TERPSICHORE. [Pok. terp- 1077.] ters-. To dry. 1. Suffixed zero-grade form *trs-t- in Germanic *thurs- in: a. suffixed form *thurs-tu- in Old English thurst, dryness, thirst: THIRST; b. Old Norse thorskr, cod (< “dried fish”), whence Norwegian torsk, tosk, cod, with dialectal variant tusk, cod, stockfish: cusk. 2. Suffixed form *ters-d- in Latin terra, “dry land,” earth (> French and Old French terre, earth, ground): TERRACE, (TERRAIN), TERRAN, TERRENE, TER- RESTRIAL, TERRIER, TERRITORY, TUREEN; FUMITORY, INTER, MEDITERRANEAN, PARTERRE, SUBTERRANEAN, TERRAQUEOUS, TERREPLEIN, TERRE-VERTE, TERRICO-
1461:ENNEAD newn ENNUI od-2 ENORMOUS gn6- ENOUGH kom, nek-2 ENSEMBLE sem-! ENSIFORM nsi- ENSTATITE sta- ENSUE sekw-1 ENSURE cira
1679:INNATE gene- INNER en INNOCENT nek=! INNOCUOUS_nek-1 INNOVATE newo- INNUENDO neu-2 INOCULATE okw- INORDINATE ar- INOSCULATE 6s- INOSITOL wei-1 INOTROPIC wei- INQUILINE kWel-1
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
1907:NEB _ nabja- NEBULA nebh- NEBULOUS nebh- NECESSARY ked- NECK ken-5 NECRO- nek-1 NECROMANCY negw-ro-, nek-1 NECROPOLIS pele-3 NECROSIS nek-1 NECTAR nek-! NECTARINE nek-1 NEE gene-
1939:NOXIOUS nek-1 NUANCE sneudh- NUB gen-
1944:NUDI- nogW- NUDNIK nau-! NUISANCE nek-1 NULL ne
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
1977:ONAGER agro-, asinus ONCE oi-no- ONCOGENESIS nek-2 ONCOLOGY nek-2 ONE oi-no- ONEIROMANCY oner- ONEROUS en-es- ONOMASTIC no-men- es ONOMATOPOEIA kWej-2, no-men- ONSLAUGHT ant, slak- -ONT es-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
=== nectar ===
740:melit-. Honey. 1. Greek meli, honey: HYDROMEL, MARMA- LADE, MELILOT, OENOMEL. 2. Latin mel (stem meil-), honey: MELLIFEROUS, MELLIFLUOUS, MOLASSES. 3. Ger- manic *melith- in compound *melith-dauwaz (*dauwaz, dew; see dheu-?), honeydew (a substance secreted by aphids on leaves; it was formerly imagined to be distilled from the air like dew), in Old English mildéaw, honey- dew, nectar, later also mildew: MILDEW. [Pok. melit- 723.]
776:sively, very (< *ne-mi-s, “not little”; *mi-, little; see mei-2): NIMIETY. 4. Latin nihilum, nothing (< *nehilum, “not a whit, nothing at all”; hilum, a thing, trifle; origin unknown), contracted to nihil, nil, nothing: NIHILISM, (NIHILITY), NIL; ANNIHILATE. 5. Latin non, not (< *ne-oinom, “not one thing”; *oino-, one; see oi-no-): Non-. 6. Italic *nek, not, in: a. Latin prefix neg-, not: NEGLECT, (NEGLIGEE), NEGOTIATE; b. Latin negdre, to deny: NEGATE; ABNEGATE, DENY, RENEGADE, (RENEGE). 7. Greek né-, not: NEPENTHE. 8. Zero-grade combining form *n- in: a. Germanic *un- in Old English wn-, not: uN-!; b,. Latin in-, not: IN-1; c. Greek a-, an-, not: A-}, (AN-); d. Sanskrit a-, an-, not: AHIMSA, AMRITA. [Pok. ne 756.] nebh-. Cloud. 1. Suffixed form *nebh-lo- in Germanic *nibla- probably in Old Norse nifl-, “mist” or “dark”: NIFLHEIM. 2. Suffixed form *nebh-eld- in: a. Latin nebula, cloud: NEBULA, NEBULOUS; b. Greek nephelé, cloud: NEPHELINE; NEPHELOMETER. 3. Suffixed form *nebh-es- in Greek nephos, cloud: NEPHOLOGY. 4. Nasal- ized form *ne-m-bh- in Latin nimbus, rain, cloud, aura: NIMBUS. See ombhro-. [Pok. (enebh-) 315.] ned-. To bind, tie. 1. O-grade form *nod- in: a. Germanic *nati- in Old English ne¢(t), a net: NET!; b. Germanic *nat-ilo, a nettle (nettles or plants of closely related genera such as hemp were used as a source of fiber), in Old English netel(e), netle, nettle: NETTLE; c. Germanic *nat-sk- in Anglo-Norman nouch, brooch: OUCH?. 2. Lengthened o-grade form *nédo- in Latin nédus, a knot: NODE, NODULE, NODUS; DENOUEMENT. 3. Re-for- mation of the root in Latin nectere (past participle nexus), to tie, bind, connect: NEXUS; (ADNEXA), ANNEX, CONNECT [Pok. 1. ned- 758.] negwh-ro-. Kidney. Greek nephros, kidney: NEPHRO-; MESONEPHROS, METANEPHROS, PERINEPHRIUM, PRO- NEPHROS. [In Pok. eng¥- 319.] negw-ro-. Adjective denoting various colors; with deriva- tives like Greek nebros, “fawn.” Latin niger, black: NEGRO, NIELLO, NIGRESCENCE, NIGRITUDE; DENIGRATE, NECROMANCY, NIGROSINE, [néhw-iz. Near. Germanic root. Old English néah, near: NEAR, NEIGHBOR, NEXT, NIGH.] nei-. To be excited, shine. 1. Suffixed form “nei-to- in Germanic *nitha-, animosity, in Old Norse nidh, scorn (> nidhingr, villain): NIDDERING. 2. Suffixed zero-grade form *ni-to- in Latin nitére, to shine: NEAT!, (NET?). 3. Possibly Persian nil, indigo: ANIL, LILAC. [Pok. 2. nei- 760.) neie-. To lead. Sanskrit nayati, he leads: NAINSOOK. [Pok. 1. nei- 760.] neig’-. To wash. Germanic *nikwiz, *nikuz in Old High German nihhus, river monster, water spirit: NIx!. [Pok. neigt- 761.] nek-', Death. 1. Latin nex (stem nec-), death: PERNI- cious. 2. Latin necdre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. 5. Suffixed full-grade form *nek-ro- in Greek nekros, corpse: NECRO-, NECROSIS; NECROMANCY. 6. Greek nek- tar, the drink of the gods, “overcoming death” (*tar-, overcoming; see ter@-2): NECTAR, (NECTARINE). [Pok. nek- 762.] nek-?. To reach, attain. I. O-grade form *nok- in Ger- manic *ga-nah- (*ga-, intensive prefix; see kom), “satis- fies,” forming *gandga-, sufficient, in Old English gendg, enough: ENOUGH. II. Variant form “enk-. 1. Redupli- cated in Greek enenkein, to carry, whence onkos, a burden, mass, hence a tumor: ONCOGENESIS, ONCOLOGY. 2. Compound root *bhrenk- (see bher-'). [Pok. enek- 316.] nekw-t-. Night. O-grade form *nokv-t-. 1. Germanic *naht- in Old English niht, neaht, night: NIGHT. 2. Latin
1907:NEB _ nabja- NEBULA nebh- NEBULOUS nebh- NECESSARY ked- NECK ken-5 NECRO- nek-1 NECROMANCY negw-ro-, nek-1 NECROPOLIS pele-3 NECROSIS nek-1 NECTAR nek-! NECTARINE nek-1 NEE gene-
```


## [2026-09-07T18:19:14.683Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nasyeiti\\|nasyeili\\|nasta-\" BRT.txt | head -10",
 "description": "Grep BRT for nasyeiti"
}
```


### [2026-09-07T18:19:14.723Z] TOOL RESULT

```
18755:•  j.,  g.  'nas-  V.  'verschwinden'.  Praes. 26  nasya-,  Perf.  1  «Äiir-  :  nas-;  PfPr. nrsa-,  j-Aor.  i  nä/-.  —  PFfP.  nasta-, °n3xsta-''>.        Vgl.  noch  II  viyanattty<^,
28963:'extinguas')  V, Ä75;  —  nasyeiti  ('interif) ,.  aAmai  k°  nmanSi  ahitil  Y.io.T,  — asista  (sd.)  .  .  aiähaf  A'  vlstü  gatti  buyat Y.6o.$;  —  —  yakmat  k'  frattnsinta ('tnetum  habebant')  . .  daeva  Yt.  iQ.  99; 97^,  V.  ig.  33;  —  niwyäH  (Sp.  927  m.; 'est   in    tiraore')  . ,  atars  . .  A*  ya^tibyS
29209:4-  8  * ;  —  •r«  baoianha  N.  5p  (?).  c)  'zu- gleich mit  — ,  gleich  bei  — ':  nasyeiti  'ra fraktnsta  (LS.  statt  IS.)  ahmat  haca nmänst  akttis  svz.  "es  verschwindet,  kaum hervorgebracht, .."  Y.  jo.  7.  [N-/:  'i*s ha%ra;  —  Yty.48,  V.p.56,  y.  SS,  Yt 10,101:  lies  Aa%ra.j\  Atüira.f;  —  N,  100  O: lies  fia%raa/^
```


## [2026-09-07T18:19:23.206Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vinath\\|vinaθ\\|vina0\\|naθ\\|vinathaya\\|vina9\" KNT.txt | head -20",
 "description": "Grep Kent for vinath"
}
```


### [2026-09-07T18:19:23.259Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T18:19:24.225Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==208||NR==209' KNT.txt | grep -n -i \"nas\\|nath\\|vina\" | head -30",
 "description": "Kent leaf for page 192-193"
}
```


### [2026-09-07T18:19:25.485Z] TOOL RESULT

```
7:rebel: Elam. şi-iš-ša-an-tak-ma, Akk. -it-ra-an. — | lah-ma, Gk. Tpravraixuns. From ciga-(§9.n1) + | lazma- ‘brave’ ($9.11): ‘Brave-by-Lineage’ (§160,- Ie); the -zm- is Median ($163.II; Jacobsohn, KZ 54.261; Bv. BSLP 31.2.79). For the nasal end-
```


## [2026-09-07T18:19:38.805Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"injur\" KNT.txt | head -20",
 "description": "Grep Kent for injure"
}
```


### [2026-09-07T18:19:38.854Z] TOOL RESULT

```
1077:drógha- ‘injury’. pIE *dhighé, OP didà ‘wall’, cf. Skt. deha-, Gk.
1150:injures’, Lt. nocet, Skt. ndsdyalt. pIE *mak- in OP тойа ‘greatest’, Av. masista-
1290:‘he injures’, Gk. «revo ‘T kill.
1517:*nek- ‘perish’, in vi-nas-ta- ‘damage’, (Ar.) *пй$- in viy-andéaya ‘he injured’.
3916:who are, because I was not hostile, I was not a Lie- follower, I was not a doer of wrong—neither I nor my family. According to righteousness I con- ducted myself. Neither to the weak nor to the powerful did I do wrong. The man who cooper- ated with my house, him I rewarded well; whoso did injury, him I punished well.
4942:axsata- adj. ‘unhurt, undisturbed’: neg. a- + pte. of xSan- ($102, §242.1), Skt. ksanóti ‘injures’, Gk. ктен, ‘kills’ (otherwise Foy KZ 35.49, Hz. Apl 70-1). azšałā nsf, DPe 23.
5576:dury, Skt. drógha- droha- ‘(malicious) injury’, pIE *dhrougho-, cf. NGm. Trug ‘deceit’, and OP duruj-, draujana-, draujiya- (870, 576.11, $101, $108.IV, $106, $122, $128, 5132.2, 3, $143.I, V). drauga nsm. DB 1.34, 434; DPd 20. draugà absm. DB 437; DPd 17f.
5591:vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
```


## [2026-09-07T18:19:47.295Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport bisect\ndef leaf_of(lineno):\n    pre='\\n'.join(lines[:lineno-1])\n    return pre.count('\\f')\nfor n in (1150,1290,1517,5591,5576):\n    print(n, 'leaf', leaf_of(n))\nEOF",
 "description": "Map KNT line numbers to leaves"
}
```


### [2026-09-07T18:19:48.539Z] TOOL RESULT

```
1150 leaf 47
1290 leaf 51
1517 leaf 57
5591 leaf 216
5576 leaf 215
```


## [2026-09-07T18:19:58.194Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 205 206 207 208 209; do echo \"=== leaf $i ===\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -6; done",
 "description": "Inspect Kent leaves 205-209"
}
```


### [2026-09-07T18:19:59.470Z] TOOL RESULT

```
=== leaf 205 ===
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
=== leaf 206 ===
n, fall down’: [avagmat]a nsf. past pte. ($244) DSe 46f (conj. of Kent, cf. JAOS 54.46).
рата + gam- ‘go forth’: paragmata nsf. past pte. ($101, $103.IV, §122, 8132.2, §244) DNa 44f.
ham- + gam- ‘come together, assemble’: ha"- gmaté npm. past pte. ($101, $1081У, $1322, $140.V, $244) DB 2.32, 38, 43, 52, 58; 3.65. See also Надтаійла-.
gay- vb., see Jiv-. gara- ‘devouring’, see bdtugara-.
garta- sb., either ‘cave’ or ‘wagon’, see Asa- garla-.
Garmapada- adj. ‘Garmapada’, the fourth month, June-July: Elam. kormabadas, АКК. du-
=== leaf 207 ===
3f, 57; XPa 20; XPc 14; XPf 48, alva}m-c* ($521) DB 5.9. Ка&-сїу nsm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. |
Citcizri- sb. ‘Cincikhri’, father of Martiya (§163.V): Elam. st-in-sa-ak-ri-1§, Akk. #-in-Sa- ah-ri-i& Cicizrais gsm. (§179.1V) DB 2.9.
сій adv. ‘so long’, correlative with уйій ‘un- til’: from ci- + suffix seen in Gk. ёте-та ‘then’ (8191.11; wrongly König, RuID 72, and Sen 40). DB 248, 63.
cica- sb. ‘seed, lineage’: Av. &6ra-, NPers. &hr ‘origin’ ($78, $148.IIT). In Ariyaciqa-, Ciça- іахта-.
Ciga"lazma- sb. ‘Cicantakhma’, а Sagartian
OLD PERSIAN
=== leaf 208 ===
 Skt. jū- ‘press for- ward, impel quickly, excite, promote’, pres. jdvate ‘hastens’, caus. javayati. Cf. Ву. BSLP 332.152; Hz. AMI 4.127, 8.37-8, 65-6, ApI 366-7; Wb. МА 41.8320; Bailey, BSOS 7.292-4; Schaeder SbPAW 1935.502; Kent, Lg. 9.43, 231.
abi- + jav- caus. ‘promote, increase, add to’: abiyajüvayam 1st sg. imf. ($215) XPg 9; abijáva- yam (§23.1, $140.IIT) XPf 40.
jtyamna- pte. as adj. ‘growing old’, nt. as sb. ‘end’ ($109, $241): Av. Jyamna-, pte. to root }уй- ‘grow weak’, Skt. jinåti ‘grows old’. jiyamnam asn. DB 2.62.
ji- vb. ‘live’: Av. fait: (gay-, Bthl. AiW 502), Skt. Джай, Lt. vivit, pIE *g*īųeti (§216); see also gaiéd-, jiva-. ajivatam 3d du. imf. ($229) DSf 14; XPf 21. jwà 2d sg. imv. ($2371) DB 4.56, 75.
jiva- ad). ‘living’: Av. fva-, Skt. jivd-, Lt. vivos, pIE *g*iuo-, cf. *g*iuo- in Gk. Blos "life", *g*ig*o- in OEng. cwicu "living, NEng. quick (8101, $114, $150). See also 7й-. Jiva nsm. XPh 48, 54. jva-diy Аза 3 (dubious $22, 555.1; ef. JAOS 51.229, Scheil 21.93, Wb. AfOF 7.45). jivahya gsm. DB 5.19f, 35.
jü- vb., see jav-.
=== leaf 209 ===
it (§76.V, 5148.1). Cf. Gray, AJP 58.67; Hz. Klio 8.51, AMI 2.77; Hinz, ZDMG 95.227. lacaram asm. DPa 6; АР]. dacaram ($494) рва 3.
tanii- sb. ‘body, self’ (8$153.IT) Ау. tand-, Skt. tani-; cf. Debrunner, IF 52.136. Decl., 51831. lanüs nsf. DNb 33. lanüm asf. XPf 31.
| tar- vb. ‘cross over’: Av. tar-, Skt. tdratz, caus. türáyalt, Lt. trans pte. as prep. ‘across’, cf. NEng. through. See also fara. vi- + tar- ‘go across’, caus. ‘put across’: viya- larayam Ist sg. imf. (§215) DB 5.24f. viyatarayd- mā lst pl. imf. (5230.1) DB 1.88.
fara prep. with aec. ‘through’: Av. tarō, NPers. tär, Skt. ards; formed on root tar- (q.v.) similarly to para (q.v.). іста] DZe 12.
Táravà- sb. ‘Tarava’, a town in Persia; Elam. -F-ra-ü-ma, АКК. ta-ar-ma-. Тато nsf. DB 3.22.
larsa- pres. stem. of vb. ‘fear’, with Ласа + abl.: Av. tarasaiti, NPers. térsé5, pIE "is-ske-ti (831, $97, $212), ef. pIE *tres- in Skt. trdsati, Gk. тре, also *trem- *trep- in Lt. tremit ‘trembles (with fear)’, trepidus ‘agitated (with fear). Jarsatiy ($228.1) DPd 11f. iarsa"tiy 3d pl. (§232.1) DSe 38f. alarsa imf. DB 1.50f. atarsa” 3d pl. imf. (5232.0) DB 2.12°; DPe 9. tarsam 1st sg. inj. (8224, 5237) DPe 21.
```


## [2026-09-07T18:20:18.898Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 179 211 212 216; do echo \"=== leaf $i ===\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -4; echo \"... tail:\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | tail -3; done",
 "description": "Inspect Kent leaves for page numbers"
}
```


### [2026-09-07T18:20:20.400Z] TOOL RESULT

```
=== leaf 179 ===
8. This is the Arab. 19. This is the Egyptian. 20. This is the Armenian.
21. This is the Cappadocian. 22. This is the Sardian. 23. This is the Ionian. 24. This is the Scythian across the sea. 25. This is the Skudrian. 26. This is the Petasos-Wearing Ionian. 27. This is the Libyan. 28. This is the Ethiopian. 29. This is the man of Maka. 30. This is the Carian.
A’Pa = ARTAXERXES III, PERSEPOLIS А, B, C, D. 1 Бара : vazraka : Auramazda : hya :' 2 упал : bümàm :adà : һуа :a 8 vam : asmünàm : ada : һуа : marti 4 yam : adi : hya : &yatàm : adi : mart ` 5 ihyà : һуа : mim : Агіахёаса : х$ауз 6 буа, : akunaus : aivam : parüvnàm :
[4
... tail:
9 spahy& : puça : Нах
10 amani&iya
TRANSLATION OF W
=== leaf 211 ===
 word of uncertain meaning, Sb 3.
Sanuvaniya- sb. ‘bowman’: deriv. ($144.IV) of stem in Av. Üanvar/n- ‘bow’, ef. Skt. dhanvan- ‘bow’ (583.11, $114, §155.1V) and Hz. ApI 339.
See also wlanwaniya-.  Ganwaniya.nsm. DNb 42.
188
... tail:
Idà- vb. ‘give’: Av. Skt. dà-, Gk. бош, Lt. dai ‘gives’, dónum ‘gift’, pIE *dó- (862, 576.11). dadátus іту. (§209, $237.II) DPd 28; DNa 55; XPh 60.
*dà- vb. ‘put, make, create’: Av. dá-, Skt.
dhà-, Gk. ri
=== leaf 212 ===
fnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis; XPb 3, 4, 5, 6; ХРе 2 bis, 3 bis; XPd 2, 3, 4 bis; XPf 2, 3 bis, 4; XPh 2 bis, 3 bis; XE 3f, 5, 5f, 6; XV 3, 4 bis, 5; A!P2 2°, 3°, 4°, 4f°; А?Не 2, 3, 4 bis; A?Pa 2, 3, 4 bis.
daiy, see -di-.
dawa- sb. (false) divinity, demon’ (cf. Hz. RHRel. 43:.32-7; AMY 8:74-5, ApI 126-30): Av.
^
... tail:
*dar- vb. ‘be angry’, see daríana-.
daraniya- sb. ‘gold’: Av. zaranya- Ars. Phl.. zarén, NPers. zárr, Skt. htranya-m, pIE *ghj-enio- ($82, $66.П, $88, §126, §144.IV), cf. NEng. gold. See also dáranzyakara-. — daraniyam nsn. DSf 35. darantyam asn. DSf 49f. But Gk. $арекб, a Persian gold coin, is from the name of Darius (Bv. BSLP 30.1.59), and not from a short form of darantya- (as taken by Mt. Gr. $129, Hz. ApI 134-5).
déraniyakara- sb. ‘goldsmith’: NPers. zärgär ‘goldsmith’; daraniya- with vriddhi, + kara- ‘maker’ ($126, §143.V, $160.18; König, Burgbau 65; Hz. AMI 3.73-4; Kent, ЈАО 53.21). dàrami- уакатӣ npm. DSf 49 (on Frag. Theta, Scheil 21, plate 11, see 544; Konig, Burgbau, Tafel 5; Kent, JAOS 53.21, against 51.19
=== leaf 216 ===
e 15; DZe 10. drayahya lsn. ($136, §251A; wrongly taken as gen., Hz. АрІ 141-3) DB 1.15, DPe 14, DSe 28°; drayahiyà ($27) XPh 23.
naiy adv. ‘not’: Av. 207, РЫ. në, Skt. ned; :
from pIE *ne, Skt. na, Lt. ne-scio ‘I don't know’, -+ Эа, asn. of pron. i-, Lt. id, OP id-am, ete. (869, 884, $191.1, $291.11, §292a). DB 1.32, 48, 49 ter, 52, 53, 71, 91°; 221, 24, 31, 51, 84; 3.15, 86; 4.44, 47 bis, 51, 55, 58, 63 bis, 63f, 64°, 65 bis; 5.16°, 31; DPd 11; DNb 7f, 12, 13, 21, 23, 36, 40; DSe 36, 40 bis, 43°; DS} 3; XV 22. nai-maiy (836) DB 4.64. nai-ma DNb 8, 10, 19. nai- pati-mà (8133) ОМ 20. nai-&im DB 4.49. naty- diš ($136) DB 4.73, 78.
naiba- adj. ‘beautiful, (religiously) good’, re- .
... tail:
with lit.; not with Foy, KZ 35.11, 37.505, IF 12.172n, nor with Debrunner, IF 52.153): DB 1.58, 58f; 2.271, 39, 44, 52, 59, 72; 3.11, 23, 61, 66, 12, 19; 54°.
nay- vb. ‘lead’: Av. nayeitt, Skt. náyati. Conj., §213. anaya imf. DB 2.88; 3.88°; 5.12. [ajnaya" 3d pl. imf. ($232.11) DB 5.28. anayatá imf. mid. as pass. ($235.П) DB 1.82, 2.73; 5.26". Some or all of these are possibly ànay-, from à + nay-. | fra- + nay- ‘lead forth, provide’: fránayam Ist sg. imf. ($226.11) DB 1.87.
nar- sb. ‘man’: Av. Skt. nar-, Gk. дир, cf. Lt. Ner-6; i
```


## [2026-09-07T18:20:34.463Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==217' KNT.txt | grep -n \"na[bßþ0θ9]\\|nas-\\|nasta\" | head -20",
 "description": "Find naθ- root entry on Kent leaf 216"
}
```


### [2026-09-07T18:20:35.684Z] TOOL RESULT

```
7:nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
12:vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
16:Nabukudracara- sb. ‘Nebuchadrezzar’, son of Nabonidus; name assumed by the rebels Nidintu- Bel and Arkha: Elam. nab-ku-tur-ra-sir, Akk. nabu-kudurri-ugur (82, 833, §75.V, $128, §163.- VD. Nabukudracara nsm. DB 3.80f, 89; 4.14, 29f; DBd 3f; written Nabukuracara ($52.V) DBi 5f. Nabuk*dracara (822) DB 1.78f, 84, 93.
17:Nabunaita- sb. ‘Nabonidus’, last king of the New Babylonian Empire, 556-39. в.с: Elam. na- bu-ni-da, Akk. nabü-na'id; Gk. Aaßivnros (Hat. 1.74, ete.). Nabunailahyà gsm. DB 1.79. Na- bunaitahya (§36.1Vb) DB 3.81; 4.14, 30; DBd 5f; DBi 7f.
```


## [2026-09-07T18:20:39.794Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==217' KNT.txt | sed -n '7,12p'",
 "description": "Print Kent naθ- entry"
}
```


### [2026-09-07T18:20:40.969Z] TOOL RESULT

```
nab- vb. ‘perish’, causative (8123.2, $215) "in- jure; destroy’: Aw. )nas-) ӨЮ. naé-, Gk. vexus
7 ыйсы аЙ eet NUI ШЕЛ, АМАА а аз an ШО. Дені. Zr é
DD де 5... anes
LEXICON
‘corpse’, Lt. acc. nec-em ‘destruction’, nocet ‘harms’, pIE *nek- (887).
vi- + nab- caus. ‘injure, harm’: vindPayatiy (8215) DNb 17f. viyanatlaya imf. (§122, $1232, $215) DB 4.66. vinátayá"tiy За pl. subj. (8222.1I, §232.1) A’Sa 5°, A?Ha 7° (conj. Kent). vinátayais opt. ($215, $223.II, $228.11) DNb 20, 21. vi- nastahyd gsn. past pte. pass. as sb. ($03, $122, $242.11) DNb 18.
```


## [2026-09-07T18:20:50.899Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD winah ==\" && grep -n \"wināh\\|winah\\|wnʾs\\|wnʾh\" PHD.txt PHD_mackenzie.txt | head -10 && echo \"== PHD nasa ==\" && grep -n \"nasā\\|nasay\\|nasā(y)\\|nsʾ\" PHD.txt PHD_mackenzie.txt | head -10 && echo \"== PHD nes ==\" && grep -n \"nēš\\|nes\\b\" PHD.txt PHD_mackenzie.txt | head -10",
 "description": "Grep MacKenzie"
}
```


### [2026-09-07T18:20:50.994Z] TOOL RESULT

```
== PHD winah ==
PHD.txt:166:~ih: wonder. àb-dàn [^5d?n!] water-holder. abdast ['5dst!] hand-guard. abdom Pfdwm | М ?bdwm] last, final(ly). ~ih: finality, end. abd-sahist [pdshst'] wonderful. abē- [5»(y)- | M ?by-, N bé] without, Jess. ~-bar [-5/] fruitless. ---bé$ [-bys] unharmed. ~-bim [-bym] fearless. ~-bimih: fearlessness. e--boy [-bwd] senseless. ---bēyih : senselessness. —-büd(ih) [-bwt', -bwtyh] deficiency. «=čim [-cym] without reason, cause. abēdān рругп!] of use, wanted. abé-|-guman [-gwmn!] without doubt, certain. —-$umiünih : certainty. ~-mizag [-m(y)ck!] tasteless. ~e must [-mwst'] uncomplaining, content. ~-niyaz [-пуа?с] free from want. ~=-68 [ws] M *by?wš, N béhóf] senseless, unconscious. -~-6Sih : senselessness, unconsciousness. abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be destroyed. —išn(ih): destruction, ruin. abespardan Pžļsp?/tn!) = abespurdan. abespurdan, abespār- [’fspwltn', ?psp'l- | M ?byspwrd, ?byspr-, N sipurdan, sipàr-] commit, entrust, consign. ubestag [5(y)s? k!] Avesta, the Mazdean scriptures, abestām [ēst m] = abestān. abestàn [°25/°п!] refuge, support, trust. ābestan Dóystn! | P ?bystn, N abtstan] = ābustan, abé-süd [yý swt'] profitless. “Аһ: profitlessness. a-bëš Буў] harmless; unharmed, invulnerable. ~ih: harmlessness; invulnerability. abē-|-wināh [-cwz?^s | M?bywr? 1] innocent. ~-wizend [-wznd] harmless, invulnerable, safe. abézag Pfyck! | M ?bycg, (N *oëza)] pure, holy. ~th: purity, holiness, abēzār Pye’, ?Буе?1 | N bézdr] free.
PHD.txt:223:āwēnišnīg : blameworthy. a-wēnišnīģ Pzwynšnyk'] invisible. awérag [”wylk!] = awērān. awērān Pwyln', ?5yPn! | N wērān] desolate, ruined. awestad ['zos??t! | M *zxoyst?d, N ēstād] master (craftsman). awestām [*wst?m | M ?wyst?m] province, district. awestarag [”wstlk! | N ustura] razor. awestardan, awestar- [*xvst/-tn! | P °wystr-, N suturdan] wipe; shave. mišn : wiping. awestwār Pwstwb’l | M ?wystw?r, N ustuwār] firm, reliable. “Аһ: reliability, firmness. awēšān [OLE?n, у. бу | М юу п, N ēšān] they, those. a-wināh Pwrs] innocent. a-winast [”wnst'] unharmed, immaculate. awiš [wbš | M ?wys] to him, it; postposition (= ©) to. awištāb Puwst*5 | M ’wyst?b, N šitāb] oppression. P awištādan, awišt- ['zoft2tn! | P ?wyst!dn] stand. awištāftan, awištāb- ['wi?j-tm | M ?wyšt?b-, N sitāftan, šitāb-] oppress; hasten (tr.). tāwištan, tāwāš- [HTYMWN-tn! < A Мут, V htm; ?wbstn' | M *wyšt] seal. a-wiyabanig Pwyd?f?nyk! | N biyābānī] astr. fixed (star). a-wizirignig Pweylinyk'] unavoidable, inevitable. āwurdan, awar- [YHYTYWN-in' < A hyty, У № | M wrd, "wr-, N ~] bring. āxēzīdan [>лусуѓп!] = āxistan. āxistan, āxēz- Phstn', ?hyc- | М *xyst, ?xyz-] rise, stand up. Axrámidan, āxrām- >А?т-уѓп! | M ?xr’m-, N xiram-idan] stride, strut. axtar [Atl | M *xtr, N ~] star, constellation, sign of the zodiac. axtar(ā)mār [Phil(?)m’/] astrologer. ~th: astrology. laxw Dell being, existence, world. ?axw Phw! | M *xvx] mind, will; vital force. *axw Phu'] lord. a-xwamn [’hwmn'] sleepless. axwān Phw’n'] = захм. a-xwārīh ['Aw'iyh] unhappiness. āxwarr [hwi | N àxur] manger, stable. --Sālār [-srd?I] head groom. a-xwaš [D BS YM] unpleasant; unhappy. ~ih: unhappiness. a-xwēškār [kwyšk'I] undutiful. ay Dy | N —J that is to say. āy-, у. amadan. ayāb [уор | М ik, N уд] or. ayāb- v. ayāftan.
PHD.txt:653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
PHD.txt:1441:crime āgrift, winah.
PHD.txt:1482:damage (n.) wināhišn, zyàn; v. harm.
PHD.txt:1483:damage (v.) wināhidan, zinénidan; v. hurt, injure.
PHD.txt:1581:destroy abesihénidan, (afsénistan), gugān-, kandan, murnjénidan, wanidan, wimuštan, wināhidan, wišuftan.
PHD.txt:1585:destruction abesihign(ih), afsënišn, ānāstīh, kastārīh, tabahih, wānišn, wany(b)ūdīh, wināhišn, wišēbišn.
PHD.txt:2445:innocent awināh, abēwināh.
PHD.txt:3662:sin abārēnih, āstār, bazag(ih), mān- dag, wināh; degrees of — āgrift, anābuhlag, arduš, bāzāzanišnih, framān, ēyrišt, tanápuhl, xwar, yüt; cause to — āstārēnīdan.
== PHD nasa ==
PHD.txt:501:narm [nlm | M nrm, N ~] meek, humble, soft. nasā [ns’y | M n(y)s?h, № ~] corpse, carrion. nask [nsk' | N ~] a division of the Avesta. nasrušt(īh) [xslwšt', -yh] pollution, corruption. nastaran [nstln' | N ~] dog-rose, sweet briar. nawad [90 | N —] ninety.
== PHD nes ==
PHD.txt:599:u- [AP- < А р | M'w-] = ud (when followed by a suffixed pronoun, e.g. u-š). ud [W < А w | M ?wd, N u] and. udrag (^wdlk! = Av. udra-] otter. ul (LALA < А I-*P | M ?wl] up(wards). ~ āmadan: rise, ~ih: upward direction. ul-āmadān [LALA YATWNPn!',*wl?mt?n") astr. ascendant. *ul-drafš, v. xurdrus. ummēd Pwmyt! | N ~] hope. ~war [-w?/ | N ~] hopeful. Urdwahišt Pertwhst'] = Ardwahist. Urišlīm Pwlyštym | N ~] Jerusalem. urmód Pwlmwt! | (N amród)] pear. *uruspar Pwlwspl = Av. uru0Bar-] intestines, womb; core, essence. urwahm(an) [wig hm(n') | M ?wrw’hm-] joyful. ~ЛЬ : joy, pleasure, delight. urwar Pwlwl | M ?wrwr] plant(s), vegetable.
PHD.txt:692:ability čāraggarīb, hunar, šāyendag- ih, tuwānīgih; extent of ones — tuwān-sāmān.
PHD.txt:803:antidote anēš, jud-bëš, pādzahr.
PHD.txt:1417:countless amar(ag), anēšmār, авар.
PHD.txt:1502:death marg(īh), ēš, widerišn(īh), P murd; moment of — gyān kandan; deserving — margarzān; risk —, fight to ~ anēš xwardan.
PHD.txt:1507:deceased anēšagruwān; v. blessed.
PHD.txt:2383:immortal ahēš, amarg, anēš(ag).
PHD.txt:2384:immortality ahēšīh, amargih, anēša- gih.
PHD.txt:2446:innumerable amar, anēšmār, азар.
PHD.txt:2848:mortal anēšxwar, géhanig, marg- ómand, 686mand, sazišnīg,
```


## [2026-09-07T18:21:02.002Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN Stachel/nis ==\" && grep -n \"Stachel\" HRN.txt | head -20",
 "description": "Grep Horn for Stachel (sting)"
}
```


### [2026-09-07T18:21:02.049Z] TOOL RESULT

```
== HRN Stachel/nis ==
6481:744. »ffgtir^ sngvrne, stiyvr 'Stachelschwein'. Si/uL sJ/ttr,
6487:Distrikts VazTrl) snkal); bei. sikun^ n. sl/un \Stachel-
6585:sözan) (Bund.); skr. rüka- '(jetreidegranne , Stachel
9217:1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
9942:602. Ein anderes räz 'Stacheligel' wird zu [/^reg- (s. No. 93j
10180:aw. asträ' ^) ; ai. asträ- Stachel zum Antreiben des
```


## [2026-09-07T18:21:03.117Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HUB nis ==\" && grep -n \"Stachel\\|nes\\b\" HUB.txt | head -20 && echo \"== HUB 104 leaf ==\" && awk 'BEGIN{RS=\"\\f\"} NR==115' HUB.txt | head -30",
 "description": "Grep Hübschmann for nēš"
}
```


### [2026-09-07T18:21:04.459Z] TOOL RESULT

```
== HUB nis ==
9:Usage guidelines
48:und Darmesteter (Etudes iraniennes I, Paris 1883) sprach-
660:*auf Kohlenfeuer gebackenes Brod*, afgh. LW. ndnvde
822:Miiller = Buddha, nach H o r n ~ zd. buiti 'Name eines
1017:das Unterste, Fuss eines Baumes, Wurzel', gr. nv&jLi/jy
1207:haufig) ein phi. *pasaxv anzusetzen, jenes aus *patsaxv,
1256:wegen seines t ein dem Avesta entlehntes Parsenwort.
1834:461. Np. xdr *Dom' (dazu xOrpust Igel' = Stachel-riicken),
1985:in Stiicke*. Das zugehdrige np. xurda *klein, kleines
2043:zd. ha^m als Nom. ntr. eines Themas haya- kann os
2090:gerade Tigranaduxt kommt meines Wissens nicht vor.
2318:'master' Shk. 264 = np. rad (rad) 'Oberhaupt eines
2387:645. Np. »dq *das Junge eines Thieres* (aus *05y) = arm.
2388:^'ag (= dzag) *das Junge eines Vogels' = syr. n:1i
2501:'Galle' so wie so fiir nicht mehr vorhandenes ''^zdr =
2923:805. Arm. gund 'Abtheilung eines Heeres, Corps, Schar'
2996:eines arischen *prauUl ist falsch.
3056:840. Dazu nach Geiger hsA, kdh 'frisches griines Gras,
3202:LW. bal. gatnes^ gvamSs 'Biififer, afgh. gavmes 'a male
3293:eines Berges am Thor der HoUe = phi. grfvak, das
== HUB 104 leaf ==
— 104 -
1062. Lies afgh. nllkq (Raverty nlkceh) und ap. apanyaka-.
1064. Im Paz. stets ntro (Min. und Shk.) geschrieben !
1065. Die Etymologie ist lautlieh unmoglich. Nur ein
urspr. ^aniddid wiirde direct zu np. nl^ fiihren. Vgl.
oben Nr. 457 und Fr. M tiller, WZKM. 5, 67.
1067. Dazu afgh. LW. nes 'the sting of any venomous
animal, puncture, lancet'; nastar und nestar a lancet' ;
arm. LW. n§iirj nstrak Xanzette' (das ein phi. *mstir
voraussetzt). Np. nestar bei Fird. I, 46, 214.
1069. Ist nt/m zu sprechen, vgl. paz. n^m, afgh. LW. nlm,
Hier fehlt np. nlmroz 'Mittag' und n%ma *Halfte' = bal.
nemag 'Richtung, Seite*, phi. nBmak part, direction
etc. Gl. and Ind. 251, afgh. nBmai 'a half.
1070. Ich halte Horn's Ausfuhrungen fur richtig mit Ruck-
sicht auf bal. niyosay *horen, horchen, lauschen' und
afgh. nyvatql (3 pr. nyvaM) 'horchen auf, gehorchen',
die auf iran. *ni-gds zuruckgehen. Vgl. auch bal.
gosay 'horen', osset. yossun^ qustn *h6ren .
1071. Np. u, Uf vor Vocalen v und' {z,B. v-agar), Sale-
mann, Mittelp. Studien 235, Vullers, Fird. I,
Einl. XXVL
1072. Hierzu np. bdj mussitatio magorum' u. s. w. bei
Vullers, alter i^a;? 'Gemurmel, leises Recitiren reli-
gioser Formeln', Noldeke, Tab. p. 353, phi. vac
Gl. and Ind. 228, West, PT. I, Introduction p. 73.
Np. guvaza *Schelten' = skr. vivac- 'streitend, Streit'
(larmend, schreiend, tosend, Wettstreit, Schlacht' bei
Pischel-Geldner, Ved. Stud. I, 37).
1075. Lies Gazophyl. p. 289. Die Form auch bei Vullers.
```


## [2026-09-07T18:21:14.552Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor n in (9217,10736,2795,2437):\n    print(n,'leaf',('\\n'.join(lines[:n-1])).count('\\f'))\nEOF\necho \"=== HRN 1067 context ===\"\nsed -n '9210,9230p' HRN.txt",
 "description": "Locate Horn entry 1067 page"
}
```


### [2026-09-07T18:21:15.932Z] TOOL RESULT

```
9217 leaf 259
10736 leaf 305
2795 leaf 85
2437 leaf 75
=== HRN 1067 context ===
Mel. asiat. IX, 241); phlv. mc (AV.?), päz. nfz.
Das Wort heisst aber nlz (nicht uez), es reimt
auf äz; ebenso hemz, das die Wörterbücher fälsch-
lich mit B sprechen lassen.
1066. ne»t *ist nicht*, vest^^),
päz. nestj nesU,
ap. naiy + asti,
1067. neS 'Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)',
nester 'Lanzette'.
ai. vergl. neksana- spitzer Stab, Spiess', zu [/'neks-,
niksati 'durchbohren' (Hörn).
1068. nek 'schön, gut', nekö, nekt, new 'wacker, Held'
(Sahn, I, 416 Vers 555, HI, 1106 Vers 707, von einer
Frau).
*) Wenn phlv. n{i)käm^ vd. 7 f 192) Gl , wirklich 'matrice' bedeutet
— was ich bezweifle - so müsstc es nCOgüm gelesen werden, um mit
np. niyäm vereinigt werden zu können (Darm est eter, Et. ir. I, 61,
Note 4).
*) Lies *amyadäciih
«J Reimt auf yekesi (Öähn. I, 42 Vers 144; 170 Vors 750). Auch
in Indien spricht man heute nlst.- 239 —
```


## [2026-09-07T18:21:30.475Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== grep farnas HRN ==\" && grep -n -i \"farnas\\|frnas\\|farnās\" HRN.txt | head && echo \"== leaf 203 (p.182) ==\" && awk 'BEGIN{RS=\"\\f\"} NR==204' HRN.txt | head -40",
 "description": "Grep Horn for farnās and print p.182"
}
```


### [2026-09-07T18:21:31.807Z] TOOL RESULT

```
== grep farnas HRN ==
== leaf 203 (p.182) ==
- 182 -
817. fiv'i stallen 'schicken*.
ap. *fra + [^sta-, vergl. a.i. pra -\- l^stho- (Causat.)
'entsenden, entlassen'.
vergl. Sit'/, (ififcwul 'senden'; bei. sastay ^ n. sastay
(363).
818. ferseng 'Parasange', arab. LW. farsax»
ap. 7Taf)f((r(iyy7j; phl. frasang bezw. farsany (Men.,
Bund.).
819. firisfe 'Bote.
phlv. firisfak (Dat. d. 3, 15); chald. LVV. vXpnonp
(das de Lagarde fälschlich = np. pereste setzt) und
NOPIDI.?« (Ezra 4, 9), Hoffmann, Zeitschr. f. Assy-
riologie II, 55 (danach Ezra 5, 6 und 7, 6 zu emen-
diren).
Zu np. ßristäden (No. 817), vergl. skr. prasthita-
aufgebrochen, der sich aufgemacht hat'. Ein aw.
^frcfsfa- (aus ar. *prasth'td', vergl. KZ. 25, 56) ist
etwa als Grundform anzunehmen ^).
^[()bi. ffriste, firzste (AM., d. l ßreste) 'Bote; Engel*.
skr. presita- {pra + |/es-, Causat.) 'gesandt', vergl.
ap. fräisayam, fräisaya ; arm. LW. hresfak 'Engel'.
bei. LW. piristay (202).
Die Etymologie stammt von de Lagarde, zuletzt
Semitica I, 67.
820. fermän 'Befehl'.
ap. framana- 'Befehl'; phlv. farman bezw. framm,
arm. LW. hramcm (davon hramanem), talm. }0*)n.
Allgemein entlehnt.
821. f ermüden 'befehlen', Praes. fermäy-em^ fermayis,
fra -f [/^ma-y vergl. ap. framätar- 'Gebieter ; phlv.
farmütan bezw. framiitan^ framät, framäy(i)sn,
822. fernüs 'töricht, nachlässig, verschlafen; Thorheit'.
ai. pra -f [/^nag- 'verloren gehen, verschwinden'.
*) Justi (Glossay 8. v. asta-) hat die Etymologie fra -|- astO' auf-
gestellt, doch giebt es ein aw. asta- 'Gesandter' nicht, und l/^as- (ai.
ag-, agnöti) heisst nicht 'senden*.
```


## [2026-09-07T18:21:42.776Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\"",
 "description": "BQT offsets and hints"
}
```


### [2026-09-07T18:21:43.973Z] TOOL RESULT

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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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


## [2026-09-07T18:21:49.334Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1471 2>&1 | head -60",
 "description": "Fetch BQT page 1471"
}
```


### [2026-09-07T18:21:50.641Z] TOOL RESULT

```
REF: BQT:1471  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 264  OCR-lang: fas

-۱۱۷۱- فرنجه
فرناس ۱ « بفتح اول بروزن کرپای » | وسکون تالك وکاف , کابوس و عبدالجنهراکوبند .
بمعتی غاعل و نادان باشد - و غفلت و نادانی را | وآن‌گرانی و سنگینیی باش د که درخواب‌برمردم
نیز گفتهاند - و بمعنی نیم خواب و خواب آلود آفند وحکما کونند سبب آن ماد سوداوی است
هم‌آمده است - و خواب اندك را نی زکوبند ۲ و درخواب چنان مینماید ‎٩‏ ؛ و بکسر اول‌وئانی
و بکس اول, در عریی شیر درددء سطبر کردن | هم آمده است؛ و درموبدالفضلا باین معنی‌باقاف
باشد؟۴ . نوشته‌اند .
فرفج - بنم اول و ثانی و سکون نون فر نجمشات ۱ - بنتح اول و شممیم:
وجیم . پیرامون واطراف دهانراکویند۴ -وشاخ | بمعنی افراجمشك است که بالنگوی صحرالی
بزرگیرا نی ز کفته‌اند که چونآترا ببرندشاخهای | باشد وعوام آنرا بالنگوی کنده کوبند و بعریی
کوچك از اطراف‌آن برآید ؛ و بفتح اول وثانی | بقلةالشب خوانند . بواسیررا نافع و مخغفف منی
ویکس اول و ضم نانی هم آمده است. باشد .
فر زج - بتتم اول وثالی وجیم فرنجه ۷ - بنتح اول و ثانی و جیم
۱- هندی باستان -8869 0۳2 ( غایب وناپدید شدن ) » ساسکربت - 80۳88262
( تمام شدن , خاموش شدن ) « اسشق - هوبشمان ۸۲۲ >:
گفت نقاش چونکه نشناسم که ته دبوانه ونه فرناسم. ‏ عنصری بلخی«لغت فرس۱۹۲*.
۳ -<-وق30۲۳ , 50۲08۵ (تهرانی وکیلکی )( خر ویفی که شخص‌خوایده کند).
۴ - (عر) «فرنای » بالکر رئیی ومهتر روستابیان - و شیر سطبرکردن و سخت
دلیر۰» ۸« منتهی‌الارب » . ۴ - « فرنج » پیرامن دهان باشد . رودکی (سمرقندی) کوید :
سر فروبردم میان آبخور از فرنج منش خشم آمد مگر.» « لغت فری ۵۸ >.
« این لفظ را مخغفف « فرهانج > هم نوشته ورشدی مخغف « فرنجك > هم . اما هیچکدام‌شاهد
تیاورده و درصورت صحت درهردو باید بافتح اول ودوم باشد. » « فرهنگه نظام >.
۵ <* فرونجك.قی:فدرنجك,درفنجك, برفنجك. فرهانح؛ وآلرابختك وخرخجیون‌نامند:
فريجك وارشان بگرفته آن دیو که سربانی است نامش خرخجیون .
خاقالی شروانی « فرهنگه نظام >.
‎٩‏ - بفتح اول و دوم وچهارم وضم پنجم . دزی‌آنرا به « مشکه فرانکها [ فرنگیان]»
ترجمه میکند < برنجمعك * فلنجمعك (ه.م.) ۳21116 ۶207 (فی) > 01150000000
«زی‌ج ص۲۹۲ :۲*. فرنجمشك < ۸6118992 ازتیرة نمناعیان 1201668 که بر‌کپای ناهموار
و دندانه‌بی دارد وگلپای آن سفید مایل بزردیت وگلها و برکها و دانه‌های آن متعمل‌است
«دگلگلاب 4۷ . ما کی‌مایرهوف کوید : «این لغت عربی ( فلنجمعك ) ازفارسی ماخوذاست.
و فولری (آ:*۱۱) در مادة « افرنج - مغك ( مشکه فرنگیان ) > و در ماد پلنکه - مشکه
(۳۷۹,۲)( مشکه پلنگه ) [ ببب رنگارنگی وعطرگیاه مزبور ] آنرا شرح داده.21816۳]
فقط وجه اخیر را پذیرفته است « عقار4۷ > موْبد نظر اخيرکلمه پهلوی 02120800501 است.
رك: پلنگشکه. ۷- مخفف «افرنجه» (ه.م.)[ * افرنگه * فرنکه] معرب۲ ۰۳۳۵۵
لانینی 17386015 فرانوی۳720 (قوم ژرمان ی که درقدیم در جوار رود 141118 سکوت‌داشتند)
و بمنلکت فراده نیز اطلاق شود . رك : نضبة الدهر دمدقی فهرست ام 2212۳ .
```


## [2026-09-07T18:22:06.883Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1836 2>&1 | head -55",
 "description": "Fetch BQT 1836"
}
```


### [2026-09-07T18:22:13.876Z] TOOL RESULT

```
REF: BQT:1836  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 633  OCR-lang: fas

کنید -۱۸۳۹-
آن در درون‌آن صدا دهد. اگر درزبرزن‌آبستن | است .
قدری ازآن دودکنند بآمانی بزاید وآ نراعربان گنبد تیزدو - بممنی کنیدآفت‌پذبر
حجرة الولادة وحجرة النسر نیزخواتند .#* است که کنایه از آسمان باشد .
گنید « بضم اول‌وفتح بای ابجدوسکون گنید چار بند - کنابه از آسسان
انی و دال بی‌نقطه » نوعی از عمارت باشدمدور است باعتبار چهار نقطةٌ مشرق و مغرب و جنوب
که ازخفت کل کج وآجر پوشند ۱ - وغنچةٌ و شمال - وکنایه از دنیا «م هست باعتبار چهار
کل را نیز گونند- ونوعی ازآیین بندی باشد که | عنصر ۲ ..
مانندکنید سازند؛ وبعربی قبه کویند - ویمعنی گنید جان‌ستان - بممنی کنبدتیزرو
جتن ‏ خی ز کردن هم‌هست - و مطلق پیاله دا | است (») که کنابه ازآسمان باشد -
نیز که خواء بدان شراب خورند وخواه ‌
نیز ده بدان راب خورند وخو گنبد حراقه رگ -, بمعنی کنید
جیزی اس جان ستان است که کنایه ازآسمان باشد .
نید لته کنابه ازحباب‌است وآن "کنند خد 1
رو مک بل خصر | « بمعنی کنید حرافه
شیشه مانندی باشد که بوقت بارردن باران‌برروی
آن بهم میرسد رنگك است که کنایه از آسمان باشد .
گنید ازدق - کنایه از آسسان گنبد دود گشت (۳) « بممنی کنید
است . خضرا است که کنایه ازآسمان باشد. وآتراکنید
۰ 8 او کفت گفته‌اند که سای دا تن
گنید اعظم «» پنمنر فلك‌اعظم است ط که مک بجای دال درمرئبه
که فلك الافلاك باشد » و عرش اعظم همان ای شت ی ۰
گنبد آفت پذیر - کنایه ازآسمان | دورگشت (4) باشد که کنایه از آسسان است
() چك » چش : گویند . (۲) خم۱: باشد .
(م) چش : دودکشت . (4) چش : دو رکشت .
۹ - پپلوی 81170081 ( کنبد » قبه) « ناوادیا صس ‎ ۲:۱۹۱‏ در تهران واراك (سلطان
آباد ) 808۳22 » معرب « جنیذ »
« ممجمالبلدان درد چنید » « دزی‌ج۱ هشوگ۳ ۳
۷ وفحنیذه» «وزی اسما»؛ ۱ ریات هو ار رد دک
مر راجیای دزی ۳۳۳ تس رت هت هه
از ارامی وسر بانی‌ماخون است«تفی‌زاده. ما دس ای ی :
باد گار 4 ص ۲۷۲ 4: سا اه ی
پرفیاننگیرد مرکهبیاش بد تچ 1 ۵
س ن سیده ب ما اس ۹
تربیت نااهل‌راچون کردکان‌بر کنبداست. ‏ ]427207 و مج رتیه
« کلتان ۲۲ . کنید
۲ - برون جمت ازکنید چاربند . نظامی کنجوی « رشیدی > .
< ناه - پم اول . پپلوی ۷1828 (کناه » خراب کردن) » ابرانی‌باستان-0۷10252
( بانکریت - ۷18292 [ اقراض » زوال ] ) ۰ ارمنی ع ۷888 از ۷1888 » شکل جنوب
غربی - 2۷1881128 . معرب‌آن جناح «تیب رکه ص۲۶۳ + کردی 81820 ۰ بلوچی 810885
اسشق ۹۳۳ ؛ بزه . جرم . خطا , میت » ثم » تقصیر » قصور : غلط .
```


## [2026-09-07T18:22:25.001Z] TOOL CALL #31: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2136 2>&1 | tail -30",
 "description": "Fetch BQT 2136"
}
```


### [2026-09-07T18:22:32.115Z] TOOL RESULT

```
ص ۹۶۶ آعهده است . ۴ -رك : ش وقس :۸ دار » (هم.)

۴ - در اوستا 8881 بمعنی لاشه و مردار و آنچه فاسد و کندیده شده باشد خواه از

اسان و خواه ازجانور . غالباً گونند « دروج نو » وازآن دیو مردار ولاشه اراده میکنند .«سو»
درتضیر پهلوی به 11282۴ گردانیده شده و هنوز هم این کلمه در ادیبات زرتشتیان پشکل «ساء
باقی است و۶ نما سالار > کمی‌است که مرده را از در دخمه بدرون دخمه میگذارد . ر4: پورداود.
بشتها ۱ص ۱۵۳ ح ۰۱ ۴ - دا دراوستا و پارسی باستان 81928 » در یونانی ورومی
48 . در پارسی سا بفتح و کسراول هردوآمده » وآن دراصل بمعنیآباد وآباده بود چنانکه
اکنون نام بسیاری از دیه‌ها مختوم به آباد است ( جعفرآباد . حسن آباد . علیآباد ) درسایق‌نا
بکار برده میشد . اي ن کلمه از دوجزو مشتق است : 81 ( پیشوند بمعمنی فرو » پایین )814 ( در
نهادن» آشستن ۰ آسودن) پی‌دا بمنی‌نشتگاه ۰ فرودگاه ۰ زستگاه ؛آبادیاست . بسیاری ازشهر-
های ابران بدین اسم نامبردار شدند: ۱) - دا واقع میان شهرمرووبلخ ‏ پایتخت تیرداد دومین
پادشاه اشکانی (۲۱۶-۲۶۸م.) شاهنامه دوبارازین‌شهرنام برده . بقول سایکی‌انگلیسی‌این شهردرده
میلی جنوب اسكآباد (عشق] باد حالیه) واقع بوده است . ۲)- نا واقع درماد »که داریوش در
کتیبهٌ بپستان ازآن‌بام میبرد. همین‌شهراست که بداشتن‌اسبان ليك‌نژاد مشپوربوده‌است. ‏ ۳)- دا
دربم .۰ 4) - دا درکرمان . ۰) - دا در فارس که همان شهر بیضا ( عپد اسلامی ) امت .
‎)٩‏ نا در میانه ( ميانك ) ازشهرهای خراسان که مار کوارت آنرا همان شهر « بهودان > که در
قرون وسطی‌نامبرداربوده » میداند وامروزآ ترا میمند گوبند , درحوالی سرحدتر کتان وافغانستان
( از بادداشتهای آقای پور داود ) و رك : فاب ۱ص *۲۸ بیعد .
بقفیه از حاشیهٌ صفحهٌ ۲۱۳۵
هنینگه نوسد : نس 3185 ۶ پیرامن دهان » ( اسدی [چاپ هرن] ص 46 ؛ عبدالقادر ص۲۲۳؛
شمی فخری ص ۵۷ ؛ فولرس ]1 . ص ۱۳۱۰ ) شاید مأٌخون از سغدی 28 « یبنی > باشد. كلمةٌ
مغدی بنظر میرسد 1105 تلفظ میشده. یابا يك حرف مصوت خیشومی 328 . چنانکه از مکل
مغدی بودایی 885 ۳ 2288 برمیاید (80.79, 8016010 ۵0 831 .طع1/1221 ) رل:
(1,0.100 ,26 ,8505.... ۷۵۲۵5 - 1۵۵۵ صقا4ود5 ,و 1160220 ) درسبزوارنیز بمعنی
* بینی» و بوکشیدن است « فرهنگه نظام » - نیز در اراك (سلطان]آ باد) 208 بآلت تتاسل دختر
بچه ها اطلاق شود ۶ مکی نژاد > » در تهرانی نیز 309 .
```


## [2026-09-07T18:22:39.307Z] TOOL CALL #32: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2228 2>&1 | tail -35",
 "description": "Fetch BQT 2228"
}
```


### [2026-09-07T18:22:46.737Z] TOOL RESULT

```
تیحوگ " - بفتح اول بروزن‌سرطوق. ۲
5 8 نیشغابور » بابای ابجد پروزن بیجاپوره
بلفت پونانی میوه‌است کهآ براآ لوچه کوبند. : 1
۰ نام شهری است در خراسان که معدن فیروزه در
نیش - با ای مجپول بر وزن دیش » | حدودآدست ‎٩‏ - و نام قعبه‌ای‌هم هست مشهوریه
لیزی سرهرچیز راکوبند همچولیش‌کارد وخنج | لیشاپورك ۷ .
(۱) خم۱: خار .
۱- در لفت فری خهٌ آقای نفیسی مورخ بسال ۸۷۷ آعده : ۶ لیشو » لیشتر باشد .
ابوالعبلی کوید :
که من ازجور بکی‌سفله براد رکه مراست از بخارا برمیدم چو خران از لیدو .>
رك : لیشو . « لغت فری مصحح اقبال ص 2۱3 *.
۴ -قی : لیشوء لیشه . ۴ - قی:هندی باستان -82668182 ( چوب‌سرتیزه
سیخ) از ريشة داو۲ا58. 1۶624 ( سوراخ کردن ( «اسدق ۰۱*۹۷ اففانی ع (نیش
هرجانور زهردار » بشتر ) ؛ 82880187 و 8851218۲ ( سشتر ) آرمنی‌ع ۲ط55 , 89178۴
( ستر ). ( از يك‌کلمه پپلوی 0819111۳ ناشی شده ) فارسی 38812)27. در فردوسی 1» 4۹ »
4 آمده ۱ هوبشمان ۱۶۹۷ : :
دکر ره کر بداری طاقت نیش ۰ مکن انگشت در سولاج (سوراخ) کردم ۰
- « کلتان ۰.۰۳۹
۴ - مخغف « بیعان » (ه.م.) < شان . 8 - مصحف « بیش > (ه.م.). در نظایس
* نیش مار » همان ممنی اول مراد است . ۹ ۳ شابور* شاپور ۳ نیشاپور ۳ نیساپور
( معرب ) » پپلوی 580882017 - 3786۷ ۶ شهرستانپای ایرانشهر . مار کوارت ۱۲ ۰ ۵۹ »
]316957 « اووالا ۱۷ . بلوشه نود : ۸71169380007 نام شهر نیشابورخراساست
که در زمان شاپور اول پسر اردشیراول درقرن سوم میلادی بنا شده» چنانکه حمزء اصفپانی نقل
میکند ( سنی‌ملوك ص 2۸ ) [چاپ برلن ص ۳۶ م.م.] و نام اصلی آن 5521000۲ 271۷8
[ (شهر) نيك شاپور ] است که در پارسی میانه به « ليك شاء‌پوهر» بدل شده . درهمان زمان که
این‌شهرمشهور بنا شده » شاپور اول شهری راکه حمزء اسفهانی (ابضاً) بنامبیشاپور 815820007
با کند » و در پهلوی 58200057 ۷۵۷ [ (شهر) به شاپور ] نامیده میشد » بنا نهاد .>
آهاد07:6 ",21298 ۷۲۵۲ 11۸743 6ل 0۲0005 ‎٩‏ کع6ا20 کعاواع باعط810
۰ .0 ,38۷21 .8 .0 ۵۲ ۵۵۵۲مط 12۵ کهنا8
این ولایت در مغرب مشهد و دردامنهٌ جنوبی کوه بینالود » درجلگهٌ وسیعی وافع شده است.وآن
دارای ۲*۲ قربه و مرکزش شهر فدیمی نیشابور است. این شهر در ‎۳۹٩‏ درجه و ۱۲ دقیقه عرضش
شمالی و۵۸ درجه و*2 دقیقه طولٍ شرقی درارتفاع ۱۲۲ مترازسطح دربا وافع‌است. نام قدیم‌آن
اپرشهر يا ابرشهراست, ومقبرة عمرخیام درلیم فرسنگی جنوب شرقیآن ومقبر فربدالدین عطار
در حواليآست . ر4 : کیهان. جفرافیای سیاسی ص ۰۱۹۳-۱۹۰ ۷ - ر4 : شاپور .
```


## [2026-09-07T18:23:04.412Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SYN corpse/die ===\" && grep -n \"4\\.75\\|4\\.76\\|CORPSE\" SYN.txt | head -10 && echo \"=== SYN nasu ===\" && grep -n \"nasu\" SYN.txt | head -10 && echo \"=== SYN sting ===\" && grep -n -i \"\\bsting\\b\" SYN.txt | head -10",
 "description": "Grep Buck SYN"
}
```


### [2026-09-07T18:23:04.480Z] TOOL RESULT

```
=== SYN corpse/die ===
5771:be teeth, on ‘fork’, tour OS ’ t of the Jaw in jaw Pol ‘angle�� to tha Bee ae m verbs for ‘chew’ Or wae he modern Polish) seems to have dasa slang term forthe: ‘chauter starte - Several are obscure in their d ection. i a ait words for ew, aHal ‘chin’. Orig. sense Jaw and ultimate connection with ae word for ‘knee’, 1B *genu- (neut.), Gri. yoru, Lat. geni, etc. (4.36), through some com- mon notion like ‘angle’, is probable. Walde-P. 1.587. Ernout-M. 414. -H, 1.589 f. on ‘jaw’ (so always in Hom.) and ‘cheek’, -yéverov ‘chin’ (and ‘beard’) ; Lat. gena ‘cheek’ (mostly in pl.; stem genu- in genutni dentés ‘back teeth’); W. gen ‘jaw, chin’ (Ir. gin, W. geneu, Br. genou ‘mouth’); Goth. kinnus, ON kinn, Dan., Sw. kind ‘cheek’, OE cin, OHG kinni, etc. (all WGmce. words) ‘chin’ (but in early period traces of use for ‘jaw’, as OHG chinne ‘jaws’ Notker, Ps. 31.9, OHG chinnibacho ‘jaw’, OE cinban ‘jaw- bone’); Skt. hanu- ‘jaw’ (h for 7 second- ary), Av. zanu- ‘jaw’ or ‘chin’ (in epd., Barth, 1689) , NPers. zanaz ‘chin’; Toch. Ber oa (dual, SSS, 3, ftn.). Gre ae ae extension *Gon(e)dh-, Ba ease pn ; zandas ‘jaw’, al Mihl.-Endz, 4.759) edi pail # Ok rn al yom vor) istot, =i + Boisacq 862. GROpeRT se ce nr HdBos,. vers NG Hacé\)\a, of frequency.
5862:Lett. zwods, mostly ‘chin’ but in some places ‘jaw’ : Lith. zandas, Grk. yvdbos ‘jaw’ (4.207). Miihl.-Endz. 4.759.
7344:4.75 DIE; DEAD; DEATH
7390:1480 f. Barth. 1146. 4.76 KILL Grk. (ao) xrelvw (éxredvov) Goth. usgiman, -daupjan, Lith. uzmusti, Zudyli NG ss akordvw afslahan Lett. nuokaut, nuon aver Lat. _interficere, occidere, ON deyda, drepa, sla, vega ChSl.  ubiti, umoritz necare Dan. draebe SCr.  ubiti, usmrtjt; It. uccidere, ammazzare Sw. déda (drapa) Boh. —zabiti, usmrlitt Fy. tuer OE cwellan, sléan, (a)dj- Pol. —zabié, uSmiercig Sp. matar dan Russ. ubit’ Rum. omort, ucide ME  sley, culle, quelle Skt. han-, vadh- Ir. marbaim, gonim, or- NE kill (slay) Av. jan-, fra-kus-, maraé., gim Du. dooden etc. NIr. — marbhaim OHG  totan, (ir)slahan W. lladd MHG iaten, (er)slan Br. laza, NHG téten, erschlagen, um-
7401:Av. mahrka- ‘destruction, (NPers. marg ‘death’) : marog- kill’ (4.76), Skt. mrc- ‘hurt, marka- ‘eclipse’, etc.
7413:3, Ir. marbaim, NIr. marbhaim fr. Ir. marb ‘dead’ (4.75).
7424:(4.75),
7432:OE cwellan, ME quelle (NE quell), caus. of OF cwelan ‘die’ (4.75).
7438:Lett. nuonavét, perfect. of navet ‘kill, murder’, fr. nave ‘death’ (4.75).
7440:ChSI. wmoriti caus. to (u)mréti ‘die’, etc. (4.75).
=== SYN nasu ===
5907:ae Dies nas-. Walde-P. 2.318. Emout-M. 653, 659. Falk-Torp 779 f. Lat. nasus (> It. naso, Fr. nez, Rum. nas), also pl. narés ‘nostrils, nose’, late sg, naris (>Sp. nariz); ON sg. ngs nostril’, pl. nasar ‘nostrils, nose’, OE nosu, nasu, OHG nasa, etc., general Gme.; Lith. nosis, OPruss. nozy; ChSl. nosit, etc., general Slavic; Skt. nas-,; nas- (in RV only dual, nom. nasd, gen. nasos), Ay., OPers, nah- (sg. and dual in Av., sg. in OPers.). The meaning ‘nostril’ is implied by the early use of dual or pl. forms, but is not necessarily older than ‘nose’, For it may be abstracted from the latter, and the dual was favored by i ae in the case of ‘eyes’, ‘ears’, 2. Grk. pts, gen. pivds, also pl. pives ostrils, nose’ (like Lat. narés), etym.? . Seng ane either : Pr TAG ES i c, (Boisacq 842) or : with query) i ete. (Walde-P. 1.140
5912:gprs OF T 4.23 NOSE Lith. nosis Goth. .--- pis ON nasar Lett. deguns Gre im Dan. nase Chsl. nosit nasus Sw. nisa SCr. nos naso OE nosu Boh. nos nez ME _~ nose Pol. nos nariz NE nose Russ. os Rum. nas Du. neus Skt. nas-, ghrana- sron OHG nasa Av. nah- sron MHG nase i NHG nase Tl Most of the words for ‘nose’ belong to | then orig. a vulgar epithet, displacing Mo:
7372:3, Lat. nex ‘violent death’ (vs. mors, above, 1), late sometimes also for natural ‘death’: Grk. vexpos, vexus Av. nasu- ‘corpse’ (4.77), Skt. nag-, Av. nas- ‘van- ish, perish’, Ir. éc, etc. (below, 4) ‘death’. Walde-P, 2.326. Ernout-M. 669 f.
7453:Grk. —_vexps, cpa, rrOpa Goth. leik, naus Lith. lavonas NG aT@pa, vexpds ON lik, nar Lett. lik'is, miruonis Lat. cadaver, corpus Dan. lig ChSl.  télo, trupit, navt It. cadavere Sw. lik SCr. — le3, mrtvac Fr. cadavre OE lic Boh. = mrtvola Sp. caddver ME cor(p)s, liche, body Pol. trup, cialo Rum. cadavru, leg NE corpse, body Russ. irup, telo ihe marb, marban Du. = ‘ligk Skt. ¢ava-, ¢arira- Nir. marbham, corp, cor- OHG lih, litamo Av. nasu-, kahrp
7460:1. Grk. vexpés, véxus, Av. nasu- : Skt. nag-, Av. nas- ‘perish, vanish’, Lat. nex ‘violent death’, etc. Walde-P. 2.326.
7478:Av. nasu- : Grk. vexpés, etc., above, 1.
7483:Nir. cuirim, adhlacaim NE bury, inter Av. (nasu-spaya- ‘burial’) W.  claddu, daearu Du. begraven
7534:Av. nasu-spaya-, nasu-spd- ‘burial, burier of corpses’, cpds. of nasu- ‘corpse’ (4.77) and the root of spayeiti, etc. ‘take away, remove’. These words occur only with reference to a sin, a violation of the prescribed Zoroastrian practice of ex- posing the corpse. Cf. Vd. 3.41 daéna mazdayasnis.... spayeiti  nasuspaem ‘“the Mazdayasnian law removes the (sin of) corpse-burial”’. Barth. 1059 f., 1615.
19303:(> It. nuocere, Fr. nuire, etc., REW 5938), caus. of *nek-in Lat. nex ‘violent death, murder’, necdre ‘kill’, Gri. vexis, vexpos ‘corpse’, Av. nasu- ‘corpse’, Skt, nag- ‘perish’, caus. ndcaya- (11.27). Walde-P. 2.326. Ernout-M. 669.
23277:5. Lith. panasus (Lalis, Senn, ete: sl not in Kurschat, and prob. neolog.) : nasus ‘comfortable, fertile’ (of. Ngp S.v.), nesti, panesti ‘carry, bear’.
=== SYN sting ===
6167:Br. dourn = Corn. dorn, W. dwrn, Ir. dorn ‘fist’ : Lett. dire, daris ‘fist’, orig. ‘fist’ in striking, fr. dirt ‘sting, thrust’
6168:(cf. Lat. pugnus ‘fist’ : pungere ‘sting’, orig.
6677:‘Pointed object’. Dan. pik, Sw. pick (Hellquist 760); NE prick (NED Prick, sb. 17); W., Corn. cal, Br. kale’h (: W. col ‘sting’, Ir. colg ‘sword’, Pedersen 1.105); W. Zlost (‘sting, dart, penis’) ; Ir, gae ‘spear’ (20.26) and ‘penis’ (Laws, Gloss. 438) ; OF pintel (NE pintle ‘a kind of pin or bolt’), MLG pint, pitte, Sw. dial. pitt (Falk-Torp 861); OHG zumpfo, MHG zumpfe (prob. : MLG timpe, Du. dial. tump ‘tip, point’, nasalized form of that in NE tip); Russ. chuj perh. : chvoj ‘pine needle’ (Berneker 408); Skt. ¢epa-, gepas- (: Lat. cippus ‘stake, post’, etc., Walde-H. 1.219); Sp. carajo (prob. fr. VLat. *caracium, Grk. Xapaxtoy, dim. of xapak ‘pointed stake’ (REW 1862) ; perh. here W. pidyn, Br. pidenn (Henry 223).
7373:4, Ir, at-balim (e.g. 3 sg. at-bail) = fas--bal- (with infixed pronoun, cf. Thuneysen, Gram. 267), OE cwelan, ME quele : W. aballw ‘fail, perish’, OHG, 08 quelan ‘endure torment’, Lith. geltz ‘sting, cause violent pain’, gelia ‘it hurts, galas ‘end’, OPruss. gallan a ete., IE *g¥el-. Walde-P. 1.690. nine 2.459f. Vendryes, RC ae ‘die’ (forms in Lewis-Pedersen ‘de ah “aes Gram. 461), vbl. n. bas en ic Mir. bath ‘death’, etym. dis- Skt one 'S orig. ‘go (forth)’ : Grk. Byy,
8023:fe H. 1.767 f. ST aectinen, of. Rum. sting ‘left’, OFr.
10260:Grk. Beddvn (replacing pa¢ls in Att.), NG Behova, Bedévt : dBerSs ‘spit’, Lith. gelti ‘sting, ache’, etc. Walde-P. 1.689f. Boisacq 118.
10277:Skt, ard-; ON alr, OE al, eal, al, ME al but mostly aule, oule (in form fr. OF awul fork’, prob. a different word : ON ‘v0 ‘meat-fork’, Lat. aculeus ‘sting, spur’, ete.), whence NE awl; OHG ala, MHG ale, NHG ahle; OHG alansa, fr.
10290:chsl. vigil (0d), jehla, Pol. | grain, sting’, Av. sikd- ‘needle’, with t scr. Russ. 4 la, fabs Berne- | Skt. s for ¢, perh. influenced by the init. yss. ayoun”s ie of siv-, syu- ‘sew’ (6.35). Barth. 1582. Brickner 189, i Wackernagel-Debrunner, KZ 67.174 f. 6.37 AWL 5 Lith. yla reas tae alr Lett. ilens oupht Dan. syl ChSl Silo sibula Sw. syl SCr. Silo Iesina OE al Boh. dlo aléne ME al, aule Pol. szydto Tesna NE awl Russ. Silo Colle Du. els, priem ray ara- sa i OHG dla, alansa, siula Vv. gana athe) MHG dle, pfriem(e) hd NHG _ahle, pfriem
11338:4, Lith. gukos (pl.), fr. suké ‘notch’ beside Lett. suka ‘brush’, perh. : Skt. cuka- ‘beard of grain, sting’, Av. sukd- ‘needle’, and even SCr. éetka ‘brush’, etc. (6.92), but all dub. Walde-P. 1.470 (quite otherwise). Trautmann 309f. Miihl.-Endz. 3.1116 f.
12085:66. Feist 73. NED s.v. bed, sb. ON sting, Dan. seng, Sw. sing (OE
```


## [2026-09-07T18:23:06.418Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== NYB winah ===\" && grep -n \"wināh\\|vinās\\|winās\\|gunāh\" NYB_vol2_glossary.txt | head -10 && echo \"=== NYB nasa ===\" && grep -n \"nasā\\|nasāy\" NYB_vol2_glossary.txt | head -10 && echo \"=== SNS ===\" && grep -n -i \"nasā\\|nasay\\|winah\\|wināh\\|vinah\" SNS.txt SNS_pages.txt | head -15",
 "description": "Grep Nyberg and SNS"
}
```


### [2026-09-07T18:23:06.490Z] TOOL RESULT

```
=== NYB winah ===
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
3788:Pärsikän ... fréstit thou hast been sent by the Persian king 1319-1? (for frēstīt he); cē-šān tö-c kust 27° (for kust he; or perhaps an absolute clause: after thy having been slain by them); but kē tē dat he? by whom hast thou been created? 577-5; eoordinated with another pers. pron.: man u to āzmāyišn kuném 4); to an [LK 'NH] ... barom (for barém) ‘thou and I (we) shall...” 5319-20-24), v. s. v. arža- nikenitan; — 2. dir. obj.: né tčy-ic pat depahr därem 21%; mā ziön . . . to dzanénd 2612, 2912; tài to giram (v. gir-) 35°; etc.; — 3. to, for, against thee: har vat kas to nē tuvan kartan is not able to do thee any harm 6!9-%; tē ce vinās jasi estet? what sin has befallen thee? (v. jastan) 1211, 5317; nē tö u ne héc dam i man ästisn nē būt hah there would have been no permanence for thee, nor for any crea- ture of mine 3515-16; beginning the sentence and taken up later by the independent form of the encl. pron.: töy-ic kë vat hah at tar menčt 331^; — 4. agent: to nē dānā- kihä kart 419-11; to amāh-ic dat hem 39"; tē zat mar 1 Tür 99??; ete.; — 5. gen. a) dam i to 335; b) det. rel. attr.: 6 õi % tē pusar 51%; et i to pus 5218-14-15; eto.; c) tē brat 2211 etc.; to mät 227%; to pus 5116; — 6. with prep.: apar tē, hac tē, 6 to, pat to, tē rād. — 51% ZK-p tw: read an-ip to as a sort of ethic dat.: ‘thou mayest understand’ or the like, with an empha- sizing tē, v. lan B; v. further s. v. -p. — < tava, Av. (787) gen. of (786 sqq.) Owa-, OP 0uva- ; the cas. rect. Av. (661) tvēm < tuvam — OP, which would have develop- ed into *tū in Milr, has been absorbed by to, as far as we can judge. MPrthPrs tw, with -c: twy(y)c; Paz. 0o, Ou, tu (0 has no etymological value); NP tū. Cf -t and at.
4163:vināsēh sinfulness 6812, vināsišn destruction, annihilation 109.
6194:w(y)n’h: vinās
7168:gunāh: vinās
=== NYB nasa ===
2648:nasäi [ns’y] corpse 6021. 727. 942%. — Av. (1057) nasu-, ace. nasāum, pl. nom. na- sāvē; MPrth ns’w; MPrs ns’h (A-H I); NP nasā ‘dead’.
5668:nsw: nasāl
6053:nihuftan nm?e: naīnāc nmwdn, nm’y: nimütan nrm: *a-namr-tom nrysh-yzd: Narsah ns'h: nasāi nw(w)m: nahom nwx: Naxu-Ohurmazd nxwst: naxUist nym: nem nymrwz: nöm-röc nyrwg: nörök nyyšydn, nyyš-: murv- niš nzd: nazd nzdyk: nazdik
=== SNS ===
SNS.txt:3141:ji^^» :^Sj) «bS vinah +rf * ab§ .•b^ :abevinah: ^^mv a 
SNS.txt:3143:.ft/UiS .^Ab^- :abSvinah!h: -o-o-»»*o' 
SNS.txt:5846:..tf : vinah + ^^a ) .L*^ :avinaln .. fl 
SNS.txt:5857::avinahlh: 
SNS.txt:13879:oT ( .Uil4S (J AliS'«4 >H J«liy :raargarzan vinah: <o*\\ ?«^-£ 
SNS.txt:13943:aTpUila^ltf , 4>H J 4 Lr :raargarzan vinah: <>Ml ?e^-£ 
SNS.txt:15167:^o^> •**-**** nasay niganih: -oWi -oM 
SNS.txt:15169:^jb^^a^Ui rnasay x v ardan: tf^i -o*l 
SNS.txt:15172:/T ^ ..^,TUj^,ljl* Jj .4*,l l( « J Jii-^»S rf ij :nasay (x) 
SNS.txt:15250:>u-*»<«*»t«ttl. **(-,) :nasay/nasa: -0»i/-^*i 
SNS.txt:15357:Ijb^jOil L«:nasay: .o^vt ^U-^bAy-nasus: -*o<u I 
SNS.txt:15389:,^.^0^-nasay niganih: *oW ~^> 
SNS.txt:15643:O-utl .^J.jU.^^.ojlp: vinahtarih: -oW<^" 
SNS.txt:15644:invinahtar: Vo-» ^ .^Irf-.vinShtarsV^-* 
SNS.txt:15650:■ TWA/IT'S .j*Kktf :vinah kar tar: VX.**>-«
```


## [2026-09-07T18:23:22.749Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vinās\\b\" NYB_vol2_glossary.txt | head -20",
 "description": "Find Nyberg vinās entry"
}
```


### [2026-09-07T18:23:22.805Z] TOOL RESULT

```
3788:Pärsikän ... fréstit thou hast been sent by the Persian king 1319-1? (for frēstīt he); cē-šān tö-c kust 27° (for kust he; or perhaps an absolute clause: after thy having been slain by them); but kē tē dat he? by whom hast thou been created? 577-5; eoordinated with another pers. pron.: man u to āzmāyišn kuném 4); to an [LK 'NH] ... barom (for barém) ‘thou and I (we) shall...” 5319-20-24), v. s. v. arža- nikenitan; — 2. dir. obj.: né tčy-ic pat depahr därem 21%; mā ziön . . . to dzanénd 2612, 2912; tài to giram (v. gir-) 35°; etc.; — 3. to, for, against thee: har vat kas to nē tuvan kartan is not able to do thee any harm 6!9-%; tē ce vinās jasi estet? what sin has befallen thee? (v. jastan) 1211, 5317; nē tö u ne héc dam i man ästisn nē būt hah there would have been no permanence for thee, nor for any crea- ture of mine 3515-16; beginning the sentence and taken up later by the independent form of the encl. pron.: töy-ic kë vat hah at tar menčt 331^; — 4. agent: to nē dānā- kihä kart 419-11; to amāh-ic dat hem 39"; tē zat mar 1 Tür 99??; ete.; — 5. gen. a) dam i to 335; b) det. rel. attr.: 6 õi % tē pusar 51%; et i to pus 5218-14-15; eto.; c) tē brat 2211 etc.; to mät 227%; to pus 5116; — 6. with prep.: apar tē, hac tē, 6 to, pat to, tē rād. — 51% ZK-p tw: read an-ip to as a sort of ethic dat.: ‘thou mayest understand’ or the like, with an empha- sizing tē, v. lan B; v. further s. v. -p. — < tava, Av. (787) gen. of (786 sqq.) Owa-, OP 0uva- ; the cas. rect. Av. (661) tvēm < tuvam — OP, which would have develop- ed into *tū in Milr, has been absorbed by to, as far as we can judge. MPrthPrs tw, with -c: twy(y)c; Paz. 0o, Ou, tu (0 has no etymological value); NP tū. Cf -t and at.
4163:vināsēh sinfulness 6812, vināsišn destruction, annihilation 109.
6194:w(y)n’h: vinās
7168:gunāh: vinās
```


## [2026-09-07T18:23:24.478Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nfor f,ns in [('SYN.txt',(7344,7453,7460,19303)),]:\n    t=open(f,encoding='utf-8',errors='replace').read().split('\\n')\n    for n in ns:\n        print(f,n,'leaf',('\\n'.join(t[:n-1])).count('\\f'), '-> printed', ('\\n'.join(t[:n-1])).count('\\f')-24)\nEOF",
 "description": "Compute Buck page numbers"
}
```


### [2026-09-07T18:23:25.888Z] TOOL RESULT

```
SYN.txt 7344 leaf 324 -> printed 300
SYN.txt 7453 leaf 329 -> printed 305
SYN.txt 7460 leaf 329 -> printed 305
SYN.txt 19303 leaf 824 -> printed 800
```


## [2026-09-07T18:23:33.797Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4155,4165p' NYB_vol2_glossary.txt",
 "description": "Print Nyberg vinās entry"
}
```


### [2026-09-07T18:23:33.846Z] TOOL RESULT

```
vinaftakéh [wynptkyh] "aberration 80?$. — Paz. vinajtat (Skr. v. dlokanatva must be due to a confusion with venäftak ‘clear, apparent, visible’). West ‘cutting off, dismemberment, disunion, disconnection’ and the like. I derive it from vi + nam-, v.s. v. ayinaftan.
vinärihistan [wyn’lyhstn'] to be arranged, etc., pass of the next vb.; pt. = pret. 3d p. sg. vinärihit (he was) equipped, pre- pared 5516,
vinäristan [wyn'lstn'], vinärtan [wyn’ltn'] pres.: read vindrénd 106%? for virdyénd, to put in order, to arrange, to array, to organize 13?(-2stan)??(-rtam). 85”. 86% (-rt). — MPrth wyn’r’d, wyn'r- (MHC); MPrs wyn'rdn w(y)n’r-; Paz. vinardan, vinärastan, Bailey, JRAS 1953, 106; Henning, TPhS 1954, 175 n. 1. Pass. v. above
vīnārišn arrangement, ordering, manage- ment 8575, 899.12, 9210.12,
www.parsianjoman.org | ool wok
vinartar
vinartar manager, administrator, pl. cas. obl. —-ān 11016,
vinäs [wns] sin, passim; ~ u bazak 68". 7419; ~ 2 andar dast u päd sins in which hand and feet are involved 6519-29; opp. kirpak 6313.24, 7925, 810, — NW form, Arm. lw. vnas; MPrs w(y)n’h (S, A-H I); Paz. NP gunäh; Arab. lw. junäh-.
vināsēh sinfulness 6812, vināsišn destruction, annihilation 109.
vinäsitan to destroy 5029, 7425; menisn i ~ to spoil a p.’s thoughts or intention: to seduce a p. 4817, to put a p. out of countenance 5222. — Av. (1055) Inas- ‘to disappear, to be lost’, (1056) vi-nas- ‘to be subject to destruction’ ; MPrth wnštg ‘destroyed? (MHC); MPrs wn'stn wn'h- ‘to damage, to injure’ (S); Verbum 191. V. also vinastakéh.
vinasitar destroyer, pl. cas. obl. ~-dn 11093,
```


## [2026-09-07T18:23:34.889Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 312 313 314 315; do echo \"== leaf $i ==\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -3; done",
 "description": "Check Buck leaf/page mapping around 290"
}
```


### [2026-09-07T18:23:36.141Z] TOOL RESULT

```
== leaf 312 ==
hing) : MBr. gow- zroncquet ‘bathe’, Ir. fo-thrucud id., Lith. trinkti ‘wash’.
W. piso, with sb. pis, fr. ME pisse, NE piss. Parry-Williams 141.
Br. staota, deriv. of staot, MBr. staut ‘urine’ (esp. of animals, but also of men), loanword fr. Gmce., Dan. stalle, Sw. stalla, MLG, NHG stallen (OFr. estaler), NE stale, all ‘urinate’ (of horses, NHG stallen dial. also of men), these perh. (with special application to horses in-
== leaf 313 ==
ion. In the Gme. group and several of the other words the development is from ‘sepa- Tate’, whence ‘discharge from the body’. The countless euphemistic expressions are mostly ignored, as for example those meaning lit. ‘discharge, empty one’s self, Wythe ne sli doone’sneed’, andespecial- : a eta use of the simple verbs defecate shows eas me Hy au finned fe ecent Specialization of
wt. os Purify’ (Fr. deféquer Lat, défaecare fr. PAC quer, sy.), » Ir. faecés dregs’ ; NED
Th oe oe ae for ‘excrement, dung’ are die ce that ‘ Selection is some- Seciaty € notion is oft alization of ‘filth’, but the dan aige # cen (as in NE dirt), A Ween human excrement
== leaf 314 ==
. saknas (Sturtevant, Hitt. Gloss. 128).
6. Lat. stercus (>It. sterco; Sp. estvércol ‘dung, manure’, back-formation to estercolar fr. Lat. stercordre ‘to dung, manure’), perh.: W. érwnc ‘urine, lye’ (but Br. stronk ‘excrement’ : strinka ‘spurt out’), Lith. terstz ‘to soil, dirty’, also Grk. orepyavos, MHG drec, ete. (be- low, 8), but all doubtful combinations. Walde-P. 2.641 f.
Lat. merda (> It. merda, Fr. merde, Sp. mierda), prob. : Lith. smirdéti, Lett.
== leaf 315 ==
 tune ‘underground room’) : Lith. ae i cover’, danga ‘a cover’, IE i lg -. Development fr. ‘covering’ to
Ung’ as fertilizer, and also (independ- ently or through ‘dung’) to ‘heap Underground room’, Walde-P. 1 854. Falk-Torp yf YS
iJ ee eae 5 " as ertilizer, cf. NE
```


## [2026-09-07T18:23:49.477Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i in range(318,332):\n    m=re.findall(r'\\b(2[6-9]\\d|3[0-1]\\d)\\b', t[i][:400])\n    print(i, t[i].strip().split('\\n')[0][:80],'|nums',m[:5])\nEOF",
 "description": "Look for page numbers in Buck"
}
```


### [2026-09-07T18:23:50.747Z] TOOL RESULT

```
leaves 1545
318 ‘get with child’), NHG beischlafen, Du. bzjslapen, etc., all lit. ‘sleep beside’ |nums []
319 amam.) |nums []
320 ��come’, with development ‘come into the world, be born’, or related to |nums ['282']
321 Dan.  frugtsommelig, svan- SCr. _trudna, breda, nose¢a lat. inciéns | iatoreg: g |nums []
322 load’. |nums []
323 �gather, take’, etc. (cf. above SCr. breda). Berneker 50. |nums []
324 ed preference for it, as against the simple verb forms (as notably in Irish and  |nums []
325 ad; déap, Pol. umiéraé, umrzeé; |nums []
326 ndure torment’, Lith. geltz ‘sting, cause violent pain’, gelia ‘it hurts, galas  |nums []
327 e, quelle Skt. han-, vadh- Ir. marbaim, gonim, or- NE kill (slay) Av. jan-, fra- |nums []
328 (‘strike, kill, injure, hurt’), with a (presumably) Gall. gl. orge ‘oc- cide’ (C |nums []
329 , but cf. NPers. kustan ‘kill’) prob. : Skt. kus- ‘tear, etc,’, further connecti |nums ['278']
330 dation Chennai and eGangotri |nums ['291']
331 e. Some are from the notion of ‘cover, hide’ (12.26, 12.27), and some are deriva |nums []
```


## [2026-09-07T18:24:02.902Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 603 604 605; do echo \"== leaf $i ==\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' SYN.txt | head -8; done",
 "description": "Check Buck p.565 area"
}
```


### [2026-09-07T18:24:04.164Z] TOOL RESULT

```
== leaf 603 ==
a te opr),
; NG xbumos, fr. late Grk. xéuBos ‘roll, and’, perh, : oxapBds Walde-P, 2.539
fe (> Romance words T aroot *ned- Seen in Ir, naidm ‘bon ?
ee Goth. nat; ‘net’, ete. sa 328. Ernout-M., 662 f., 674. - &naidm, NIr. snaidhm, perh. fr,
Digitized by Arya Samaj Foundation Chennai and eGangotri
SCELLANEOUS PHYSICAL ACTS, ETC. 551 wisCE 9.192 KNOT (sb.) : Lith. mazgas aur knutr Lett. mazgs oe Dan. knude ChSl.  (qzlii) sae Sw. knut SCr.  uzao tod OE cnolta Boh. _uzel cud ME knotte Pol. wezel aD NE knot Russ. — uzel 7 Du. knoop Skt. — granthi- snaidm OHG knodo, knoto, knopf Av. pee snaidhm MHG  knode, knote, knopf NHG knoten
some by-form of *sné(z)- in Skt. sndyu- ‘bond, sinew’, Lat. nére ‘spin’, Ir. snathe ‘thread’, etc. Walde-P. 2.329, 694 f.
W. clwm, cwlwm, Corn. colmen, Br. koulm, skoulm, prob. : Ir. colum ‘skin’ and ‘sinew’ (cf. columne gl. nervus), re- flecting the old use of sinews for binding. Loth, RC 41.375 ff.
== leaf 604 ==
bs for strike are derived from the name of the instrument used. Several, mostly of imitative origin, were first used with ref- erence to the sound made by a blow (cf. NE knock, Fr. frapper, NG xruna, be- low). Some are used esp. for ‘strike with a sharp instrument’, and so overlap with ‘cut’. Some are used esp. for ‘strike to death’, and so overlap with ‘kill’. The notion of repeated action is usually, though not always, present in NE beat and pound, and elsewhere may be brought out by the use of cpds. or iteratives.
1. IE *g*hen- in words for ‘strike’, and esp. ‘strike to death, wound, kill’ (4.76). Walde-P. 1.679 ff. Ernout-M. 344, Walde-H. 1.332 f.
Grk. Geivw ‘strike’ (poet.), fut. Oevds, |
aor. @eva, beside aor. éredyoy ‘kill’,
. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar _
gévos ‘murder’, etc.; Lat. dé-fendere ‘ward off’, of-fendere ‘strike against’; Skt. han-, Av. Jan- ‘strike, slay’; Arm, ganem ‘strike’; Hitt. kwen, kun- ‘strike, defeat, kill’: Ir. gonim ‘wound, kill’; Lith. ginti, ChSI. giinati ‘drive’ (fr, ‘strike’), etc.
2. IE *bher-. Walde-P. 2.159f, Er- nout-M. 348. Walde-H. 1.481 f.
Lat. fertre ‘strike, beat, knock, slay’ (> Sp. herir ‘wound, hurt, strike’, Ty. férir ‘strike, smite’, obs.); ON berja ‘strike, beat’, OHG berjen, MHG ber- jen, bern ‘strike, pound’, also ‘knead, mold’; ChSl. borjq, bratz ‘fight’, Av. tizi- bara- ‘with a sharp cutting edge’; prob. also Lat. fordre, ON bora, OE borian, ete. ‘bore’ (9.46).
== leaf 605 ==
wn’ (a bird in hunting), tara GO), colog as Nc: s.v. III) and so reg.
Spr,
leaver’, xomets ‘chis-
5. Lat, percutere
ete ° i perculir), ( percuotere,
cpd. of quatere ‘shake’
earlier sense is ‘stri through’, this from ‘ e is ‘strike
(esp. with a cut- iat, cut, strike to death,
```


## [2026-09-07T18:24:16.745Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"56[3-7]$\\|56[3-7] \\|\\b56[45]\\b\" SYN.txt | grep -i \"MISCEL\\|ACTS\\|SHARP\\|9\\.2\" | head -10; echo \"---\"; grep -n \"9\\.2[0-9] \\|SHARP\" SYN.txt | head -20",
 "description": "Find Buck section near p.565"
}
```


### [2026-09-07T18:24:18.024Z] TOOL RESULT

```
14255:564 SELECTED INDO-EUROPEAN SYNONYMS 9.27 SPLIT (vb. trans.) .  oxltw Goth. 5 Lith.  skelti
26243:ort? (but not ‘sound’ in general), etym. much disputed. Prob. not ax-ove- fr. ax- sharp’ and. ods ‘ear’ (Kretschmer, KZ. 33.565, Falk-Torp 454, etc.), but *a- wo- : Goth. hausjan ‘hear’, and both : Gtk, xoéw ‘perceive, notice’, also ‘hear’, Lat, cavére ‘beware’, ChSl. éuti ‘recog- nize, notice’, po-Cuti ‘perceive’ (15.11), Skt. kavi- ‘wise, a seer’, etc. Walde-P. 1369. Boisacq 37f. Feist 252. Walde- H, 1,186.
---
2255:| CHAPTER 2 MANKIND: SEX, AGE, FAMILY RELATIONSHIP 9.1 Man! (Human Being) 2.47 GRANDMOTHER 9.91 Man? (vs. Woman) 2.48 GRANDSON 2.92 Woman 2.49 GRANDDAUGHTER 2.93 MALE’ 2.51 UNcLE 9.94 TeMALE 2.52 AUNT 9.942 Sex 2.53 NEPHEW | 9.25 Boy 2.54 NIECE 9.26 GIRL 2.55 CousIN | 2.27 CHILD 2.56 ANCESTORS 2.28 INFANT 2.57 DESCENDANTS 231 HUSBAND 2.61 Fatuer-1n-Law ~ 2.32 Wire 2.62 Morser-in-Law 2.33 Marry 2.63 Son-1n-Law 2.34 Marriage; WEDDING 2.64 DauGuHTEr-in-LAw 2.35 FaTHER 2.65 BrotuEr-in-Law 2.36 MoTHER 2.66 SisteR-1n-Law | 2.37 PARENTS 2.71 STEPFATHER 2.41 Son 2.72 STEPMOTHER 2.42 Daucuter 2.73 STEPSoN | 2.43 Cuiup (Son or Daughter) 2.74 STEPDAUGHTER 2.44 BroTuHEr 2.75 ORPHAN 2.45 SISTER 2.76 Wipow 2.452 BrotHEer(s) AND SISTER(s) 2.81 RELATIVES 2.46 GRANDFATHER 2.82 FamiIny 2.1 MAN! (Human Being) oy ae por Goth. manna Lith.  Zmogus, pl. Zmonés iy ae eee s oN maor, gumi Lett. cilveks It. heinb - an. —menneske ChSl. elovékit Tr. iter an menniska SCr. Eoujek Sp. hombre ME man(n), guma Boh. tlovtk Rum. om man Pol. czlowiek Tr. duine NE man Russ. elovek Nir. duine Du. mensch Skt.  manu-, purusa- W. dyn OHG man, mannisco, gomo Av. __masya-, masyaka-, Br. den MHG mensch OPers. martiya- NHG mensch
13490:9.11 9.12 9.13 9.14 9.15 9.16 9.17 9.18 9.19 9.192 9.21 9.22 9.23 9.24. 9.25 9.26 9.27
13926:552 9.21 STRIKE (Hit, Beat) Grk. rixrw, xpobw, xdrTw, Goth. slahan, stautan, blig- Lith. musti, iStiktt, dq ‘ii Gelvw, walw gwan . Lett. sist, dauzit, ner t NG xrur&, Bapd, dépvw ON sld, ljosta, berja, ChSl. biti, udariti, lest; Lat. ferire, percutere, cae- drepa uraziti ' dere, percellere, Dan. slaa SCr. —udariti, biti, Lupin; tundere Sw. sid tuéi Pui, It. colpire, percuotere, OE sléan, béatan, drepan Boh. —_uhoditi, udeFiti, bin; batlere ME  sleye, nae strike, " tlouci ah fr. rapper, batire hitte, bete ol. uderzyé, bié, razz, SEES Le ii NE strike (smite), hit, Russ. bit’, udarit’, orgy Sp. golpear, pegar, batir beat razit! , Rum. _lovi, bate Du. — slaan Skt. han-, tad- Ir. benim, sligim, slai- OHG - slahan, bozan, berjen, Av. Jan-, snad- dim, bialim bliuwan Nir. buailim MHG slon, bozen, bern, bliu- W. taro, curo wen Br. skei, kanna, dourna NHG § schlagen
14031:9.22 CUT (vb.)
14092:9.23 KNIFE
14133:9.24 SCISSORS, SHEARS
14169:MISCELLANEOUS PHYSICAL ACTS, ETC. 561 q 9.25 AX Goth. agizt Lith. kirvis iNex5 agivn ON gx (barda) Lett. cirvis Grk. qoexolpt ° Dan. kse Ch&l. sékyra (brady) NG secitris (bipennts, Sw. yra SCr. —sjekira (bradva) Jat. ascia) OE ex Boh. _ sekera (topor) It gscia, soure ME ax, ex Fo siekiera (topor) ache NE ax uss. lopor Fr. hacha (segur) Du. bil Skt.  paragu-, kuthdra 5p. m. (0p0r secures OHG  acchus, bihal, baria Ay. taga- He * piail, tag. MHG aches, bil, barte Nir. a NHG Beil, axt r wy y bouc’hal For ‘ax’ there is one inherited group, | berg et Saglio s.v.; > OFr. aisse, It.
14203:9.26 BREAK (vb. trans.)
14255:564 SELECTED INDO-EUROPEAN SYNONYMS 9.27 SPLIT (vb. trans.) .  oxltw Goth. 5 Lith.  skelti
14289:9.28 TEAR (vb. trans.)
14334:9.29 FLAY, SKIN
25876:15.78 SHARP
27061:15.78 SHARP (In part differentiated; a, of a Point; b, of an Edge)
32693:19.11 Country (“European Countries”) 19.44 Free (adj.) 19.12 Onn’s Native Country 19.45 Commanp, ORDER (vbs.) 19.13 Country vs. Town 19:46 Osry 19.14 Rucion, TERRITORY 19.47 Ler, Permir 19.15 Curry, Town 19.48 ComPEL 19.16 VILLAGE 19.51 Frrenp 19.17 BounDaRyY 19.52 ENemy 19.21 PropriE (Populace) 19.53 ComPANIon 19.22 A Propize, Nation 19.54 NEIGHBOR 19.23 Tripn, Cxuan, Famity (in Wide | 19.55 Srrancser Sense) 19.56 GuEsT 19.31 RuE (vb.), Govern 19.57 Host 1932 Kane 19.58 Ht, Ar (vbs.) 19.33 QuEEN 19.59 Htiyper, PREVENT 19.34 EMPEROR 19.61 Custom 19.85 PRrIncE 19.352 Note on Other Titles of Nobility 19.62 Srarex, QUARRED 19.36 Noszz (sb.), NoBLEMAN 19.63 Puor, Conspiracy 19.37 CrrizEN 19.64 Common (adj.) 19.38 Susszct (sb.) 19.65 Musr (vb.) 19.41 Master 19.71 Note on Terms for Members of a 19.42 Suave Trade or Profession 19.48 Servant 19.72 Wor, ProstiTuTE 19.11 COUNTRY (“European Countries’’) Gtk.  xépa, yf, x0dv Goth. land Lith.  kraStas, Zemé NG —_x:pa, rémos ON land Lett.  zeme Lat. — finés, terra Dan. land ChSl. strana, zemlja It. paese Sw. land SCr. zemlja Fr. pays OE land Boh.  zemé Sp. pats ME land, contree Pol. _ziemia Rum. ard NE country, land Russ. strana I. ltr, crich Du. land Skt.  dega-, vigaya-, jana- Nir. tir OHG lant pada- W. — gwlad MHG lant Av.  dai#hu-, OPers. dah- Br. bro NHG land yu-
32965:19.21 PEOPLE (POPULACE)
32996:ON Igor, and esp. pl. lgdir, OE léode, ME lede, Du. lieden, OHG liuti, MHG liute, NHG leute, all pl. of OE léod, OHG liut, etc. (see list 19.22 ‘a people, nation’ é OE, OHG also ‘a man’) : Lat. liber,
33009:19.22 A PEOPLE, NATION
33036:19.28 TRIBE, CLAN, FAMILY (in Wide Sense)
```


## [2026-09-07T18:24:29.477Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14289,14300p' SYN.txt | cut -c1-600 && echo \"=== 9.29 ===\" && sed -n '14334,14345p' SYN.txt | cut -c1-600",
 "description": "Read Buck 9.28/9.29"
}
```


### [2026-09-07T18:24:29.543Z] TOOL RESULT

```
9.28 TEAR (vb. trans.)
Grk.  craphoow Goth. tahjan, distairan Lith. plegti, dréksti NG  tecxitw ON rifa, slita Lett. plést, draskat Lat. scindere Dan. rive ChSI.  dtrati It. _stracciare Sw. riva, slita SCr. _ kidati, trgati Fr. déchirer OE teran, slitan Boh. _ irhati, rvati Le rasgar, desgarrar ME lere, rende, ryve Pol. drzeé, rwaé ot ae NE tear (rend) Russ. vat’, drat’ ao ‘ Du. scheuren Skt. dy- v a 8()racaim OHG - slizan, zerran, rizan Av. nis-dar Bn ee MHG slizen, zerren, rizen NHG reissen Words for
‘tear’ are used, part] dis- creished by prefixes, for ie sieves Pleces’ or for ‘tear off? (from the main Tn the latter Sense they overlap Snatch, pluck, ete.’ & ords that may be rendered a eee expression for the €nce’ and do not eet ‘tear’ are not Laas iri a : of the words, though listed » Af€ more Commonly used zerreissen, Russ - ‘tear apart’, Words for ‘tear’ and
‘tear off
1h tgp,
‘flay’ (9.29). Walde-P. 1.797 ff. Feist 120. Berneker 185.
Here as ‘tear’ : Goth. dis-tairan ‘tear, burst’ (leather bottles, where Grk. biyvunt; also ga-tatran ‘destroy, break’), OE teran, ME tere, NE tear, OHG zer- ran, MHG zerren (NHG ‘tear off, pull, tug’; OHG fir-zeran ‘destroy’, NHG verzehren ‘consume’); ChSI. dirati, Pol. drzeé, Russ. drat’, dirat’ (SCr. derati, Boh. drati mostly in secondary uses); Skt. dr- ‘burst, tear’ Av. niSdar- ‘tear out’ (Barth. 689). Cf. also Toch. tsar- ‘separate’ (SSS 483).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
| Digitized by Arya Samaj Foundation Chennai and eGangotri
SELECTED INDO-EUROPEAN SYNONYMS
566
2. Grk. craphoow (orapay- as in ond- payne ‘a piece torn off’, emapaynds ‘a tear- ing, rending’) prob. with connection through ‘noise of tearing’ : Skt. sphiij- ‘rumble, crash’, Lith. spragéli ‘crackle’, etc. (Walde-P. 2.672 ff., but crapacow separated, 2.668). Persson, Beitrige 869.
=== 9.29 ===
9.29 FLAY, SKIN
Goth. Lith. — dirti, bielyti, lupti
CL ae ON fla Lett.  dirat
NG iabere Dan. flaa ChSl.  (dirati)
c pears Sw. jld SCr. — derati, guliti
Ie Pier OE fléan, hyldan Boh.  dfiti
4 . — desollar ME fle(n) _ Pol. —zdzieraé, tupié
male jupui NE flay, skin Russ. _ sdirat’
Ir. fennaim Du. villen Skt. bso
Nir. feannaim OHG scintan, fillen Av. vi-nad-
W. — blingo, digroent MHG _schinden, villen
Br. _—digroc’henna NHG - schinden, hiuten
```


## [2026-09-07T18:24:50.421Z] TOOL CALL #43: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-07T18:24:50.427Z] TOOL RESULT

```


```


## [2026-09-07T18:24:54.494Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne%C7%B5-",
 "prompt": "Give the reconstructed root, its meaning, and all listed derivatives (Sanskrit, Avestan, Greek, Latin) verbatim."
}
```


## [2026-09-07T18:24:55.890Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%A7%D9%87",
 "prompt": "Give the full etymology of Persian گناه verbatim, including Middle Persian and Proto-Iranian forms and any cognates or derived Arabic loans."
}
```


### [2026-09-07T18:24:56.014Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:25:02.004Z] TOOL RESULT

```
# Etymology of Persian گناه

Based on the Wiktionary entry, here is the etymological chain:

**Persian گناه** derives from **Middle Persian wināh** (𐫇𐫏𐫗𐫀𐫍 wynʾh), meaning "sin, crime." The ultimate sources are the **Proto-Iranian preverb *vi-** (from Proto-Indo-European *wí meaning "apart, against") combined with the **root *nas-** ("to disappear; to perish"), itself from Proto-Indo-European *neḱ-.

**Related cognates include:**
- Old Armenian վնաս (vnas)
- Old Georgian უნასი (unasi)
- Baluchi gināsk
- Northern Kurdish binas
- Sanskrit विनाश (vināśa)

**Descendant languages** showing this word's wide influence include Turkish günah, Kurdish variants, Tajik гуноҳ, Hindustani गुनाह/گُناہ, and many others across Central Asian and South Asian languages. The word also entered Arabic as جُنَاح (junāḥ) from Middle Persian.
```


## [2026-09-07T18:25:10.095Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne%C4%B7-",
 "prompt": "Give the reconstructed root, its meaning, and all listed derivatives."
}
```


## [2026-09-07T18:25:11.518Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B4",
 "prompt": "Give the full etymology of Persian نیش verbatim (Middle Persian, Proto-Iranian, Sanskrit comparisons) and of نیشتر if mentioned."
}
```


### [2026-09-07T18:25:11.548Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:25:15.036Z] TOOL RESULT

```
# Etymology of Persian نیش (niš)

According to the Wiktionary entry, the etymology traces back through several language stages:

**Direct lineage:** "From Middle Persian [script needed] (nēš), from Old Median, from Proto-Iranian *náyjam, from Proto-Indo-Iranian *náyȷ́žʰam."

The entry does not provide Sanskrit comparisons or detailed information about نیشتر (ništar) beyond listing it as a related term.
```


## [2026-09-07T18:25:23.527Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne%E1%B8%B1-",
 "prompt": "Give the reconstructed root, its meaning, and all listed derivatives and derived terms verbatim."
}
```


## [2026-09-07T18:25:24.566Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/n%C3%A1yjam",
 "prompt": "Give the reconstruction, meaning, etymology and descendants verbatim."
}
```


### [2026-09-07T18:25:26.342Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-07T18:25:32.701Z] TOOL RESULT

```
# Proto-Indo-European Root *neḱ-

**Reconstructed Root:** *neḱ- (perfective)

**Meaning:** "to perish, disappear"

**Derivatives and Derived Terms:**

- *néḱ-t ~ *n̥ḱ-ént (aorist) – Sanskrit náśanti
- *néḱ-s-t ~ *n̥ḱ-s-ént (innovative s-aorist) – Tocharian A ñakäs, Tocharian B nekasta
- *néḱ-ye-ti (ye-present) – Proto-Indo-Iranian *náćyati
- *néḱ-se-ti (se-present) – Tocharian forms
- *ne-nóḱ-e ~ *ne-nḱ-ḗr (perfect) – Sanskrit ननाश (nanā́śa), Avestan vīnə̄nāsā
- *noḱ-éye-ti (causative)
- *nóḱ-o-s – Sanskrit नाश (nāśa)
- *neḱ-tó-s – Sanskrit नष्ट (naṣṭá), Avestan našta
- *néḱ-s ("death") – Latin nex, necō; Avestan nas
- *neḱ-rós – Ancient Greek νεκρός (nekrós)
- *néḱ-tu-s ~ *n̥ḱ-téw-s – Proto-Celtic *anxtu
- *néḱ-us ~ *n̥ḱ-éw-s
- *néḱ-tr̥h₂ – Ancient Greek νέκταρ (néktar)
- *n̥ḱw-ó – Proto-Tocharian *eṅkwe
```


## [2026-09-07T18:25:43.145Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FVQ junah ==\" && grep -n -i \"junāḥ\\|junah\\|جناح\" FVQ.txt FVQ_pages.txt | head -20 && echo \"== PLA junah ==\" && grep -n -i \"junāḥ\\|junah\\|gunāh\\|wināh\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "Grep Jeffery and Asbaghi for junāh"
}
```


### [2026-09-07T18:25:43.205Z] TOOL RESULT

```
== FVQ junah ==
== PLA junah ==
```


## [2026-09-07T18:25:50.132Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"un[aā][hḥ]\" FVQ.txt | head -20; echo \"--- head of FVQ page 38 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==2' FVQ_pages.txt | head -5",
 "description": "Search FVQ for junah"
}
```


### [2026-09-07T18:25:51.383Z] TOOL RESULT

```
20993:hamgunah 103 
21073:hamgunah 103 
21691:gunah 103 
--- head of FVQ page 38 ---
```


## [2026-09-07T18:25:56.120Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -B3 -A12 \"^gunah 103\" FVQ.txt | head -40; echo \"=== search page 103 area ===\"; grep -n \"gunah\\|junah\\|guna\" FVQ.txt | head",
 "description": "FVQ index gunah p.103"
}
```


### [2026-09-07T18:25:56.194Z] TOOL RESULT

```
21688-Kurdish 
21689-
21690-. . 224 
21691:gunah 103 
21692-
21693-
21694-denarius 133, 134 
21695-gingiber 154 
21696-iungere 155 
21697-palatium 83 
21698-flowa 146 
21699-
21700-
21701-Slavonic 
21702-
21703-s?ama 243 
=== search page 103 area ===
20993:hamgunah 103 
21073:hamgunah 103 
21691:gunah 103
```


## [2026-09-07T18:26:02.187Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 FVQ_pages.txt && python3 -c \"\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,p in enumerate(t):\n    if 'gunah' in p or 'hamgunah' in p:\n        print('LEAF',i, p[:60].replace(chr(10),' '))\n\" | head -20",
 "description": "Find FVQ page with gunah"
}
```


### [2026-09-07T18:26:03.431Z] TOOL RESULT

```
LIJ< OU 158174 >m
> - ;0 73
^ COGAEKWAD*8 ^ORIENTAL SERIES
leaves 335
LEAF 325 308 INDICES Baluchi ganj 251 Old Persian amrtatdh 283 dpi 47
LEAF 328 INDICES 311 tmxa/uoc 18 Soghdian Old Turkish Turkish crroa 1
```


## [2026-09-07T18:26:08.739Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==121' FVQ_pages.txt | head -60",
 "description": "Print FVQ page 103"
}
```


### [2026-09-07T18:26:09.939Z] TOOL RESULT

```
103
they apparently treat it as a genuine Arabic formation. As Hiibsch-
mann showed in 1895 in his Pcrsische Sludien, 162, 212, it is the
Pers. aU j 1 through the Pazend yundh (Shikand, Glossary, 247) from
Phlv. (j*)) vinas* a crime or sin (as is obvious from the Arm.
if^ituiu = afJiapTr/iJia in the old Bible translation), 3 and the fact that
vcndh still occurs in one of the Persian dialects as a direct descendant
from the Phlv. -(j^)), 4 which is related to Skt. t^TTIf w&ara and
is quite a good Indo-European word. In Phlv. the word is used
technically just as in the Qur'an, and we find such combinations as
<t)JJ))*> aviuds sinless (PPGl, 77) ; ^'-u^O-")) vinaskarih ~
sinfulness, iniquity (West, Glossary, 248) ; and iiiAj^yj) vindskdr
a criminal, sinner (PPGl, 225). 5
The word was borrowed in the pre-Islamic period and occurs in
the old poetry, e.g. in the Mu'allaqa of al-Harith, 70, etc., and was
doubtless adopted directly into Arabic from the spoken Persian of tin 1
period, for the word is not found in Syriac.
(Janna).
Of very frequent occurrence. Of. ii, 23, !53, 70, etc.
Garden.
It is used in the Qur'an both of an earthly garden (liii, 10; xxxiv,
14 ; ii, 207, etc.), and particularly as a name for the abode of the
Blessed (Ixix, 22 ; Ixxxviii, 10, etc.).
In the general sense of garden, derived from a more primitive
meaning, enclosure, the word may be a genuine Arabic inheritance
from primitive Semitic stock, for the word is widespread in the
1 Vollers hesitatingly accepts this in ZDMG, 1, 689 (hut see p. 612, where he
quotes it as an instance of sound change), and it is given as a Persian borrowing by
Add ai Sher, 45.
2 Hubschmann, Penisc.he, Studien, 159, and Hang in PPGl, 225. Cf. West,
Glossary, 247, Nybcrg, Glonsar, 243.
3 Hubschmann, Arm. Gramm, i, 248.
4 Horn, Grundriss, 208. Kurdish yundh cannot be quoted in illustration as it is
a borrowing from Mod. Persian.
5 The Pazend has similar combinations, e.g. gundhi, sinful ness ; tfnndhkdr, sinful,
mischievous ; gundhkdri, culpability ; yundh-ndrndnihu, proportionate to the sin ;
ham-gundh (cf, Phlv. 4)**)\H] accomplice (Shikand, Glossary, 247).
```


## [2026-09-07T18:26:23.555Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==120' FVQ_pages.txt | tail -30",
 "description": "Print FVQ page 102"
}
```


### [2026-09-07T18:26:24.838Z] TOOL RESULT

```
(Pflm, 695, 696), was nevertheless borrowed in this sense into
Persian as C*<* J . as Noldeke, Sasaniden, 241, n., points out. 1
On the ground of a word X?X1 in a Minaean text (Glaser, 284, 3)
which may mean tribute, Qrinimc, Z^xxvi, 161, would take \j>- as
a borrowing from S. Arabia, but in the uncertainty of the correct
interpretation of this text, it seems better at present to content our-
selves with Fracnkel, Frcmlw, 283, in holding to an Aramaic origin. 2
j^taj- (Jaldblb).
^
xxxiii, 59.
Wrappers. Plu. of <^uL>-, a large* outer covering worn by women.
It is as an article of women's attire that it is mentioned in tho
Qur'an, though the Lexicons differ considerably as to the exact
meaning (cf. LA, i, 265).
The difficulty of deriving the word from <^- is of course obvious,
and Noldeke, Neue Beitrdge, 5)5, recognized it as the Eth. ^Afl'fl, from
lAflfl to cover or cloak, which is quite common in the oldest texts.
It was apparently an early borrowing, for it occurs in the early poetry,
e.g. Div. Hudh, xc, 12.
A- I S
<T- Ll>- (Jutiali).
v, 94; xxxiii, 5, 51, etc. ; some twenty-two limes.
Sin, wrong, crime.
A favourite Madina word, occuring only in late passages. The
favourite phrase is L T'^T *> an d ^ usec J as a technical term
in Muhammad's religious legislation. 3
The Lexicons give no satisfactory explanation of the word, though
1 Vullcrs, Lex, ii, 999.
2 Cf. Schwally, Jdiotiwn, 17.
3 Horovitz,#7, 62, n.
```


## [2026-09-07T18:26:33.246Z] TOOL CALL #56: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A7%D8%AD",
 "prompt": "List all Arabic etymologies given on this page for جناح: the 'wing' word and the 'sin/misdemeanour' word (junāḥ). Quote the etymology sections verbatim, including any mention of Middle Persian wināh or Persian گناه."
}
```


## [2026-09-07T18:26:33.963Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nectar",
 "prompt": "Quote the full etymology of nectar and nectarine."
}
```


### [2026-09-07T18:26:37.718Z] TOOL RESULT

```
# Arabic Etymologies for جناح

## Etymology 1 (janāḥ - "wing")

"Uncertain; no Semitic cognates exist which are not suspected to be borrowed from Arabic."

The entry notes a possible connection to Egyptian ḏnḥ and the Arabic verb جَنَحَ (janaḥa, meaning "to lean"), both referring to the concept of "side."

## Etymology 2 (junāḥ - "blame/transgression")

"Borrowed from Middle Persian.; compare modern Persian گناه (gonâh)."

This meaning derives from a Middle Persian source, with the modern Persian word گناه serving as a cognate form.
```


### [2026-09-07T18:26:39.122Z] TOOL RESULT

```
# Etymology of Nectar and Nectarine

**Nectar (n.):**
"1550s, from Latin _nectar_, from Greek _nektar_, name of the drink of the gods, which is perhaps an ancient Indo-European poetic compound of _nek-_ 'death'...+ _-tar_ 'overcoming.'" The term expanded to mean any delicious drink by the 1580s and came to describe flower nectar around 1600.

**Nectarine (n.):**
"Type of peach with smooth skin and firmer pulp, 1660s, noun use of adjective meaning 'of or like nectar' (1610s; see nectar + -ine)." The word was likely influenced by the German term _nektarpfirsich_ ("nectar-peach"), and earlier appeared in English as _nectrine_.
```


## [2026-09-07T18:26:45.863Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/nuisance",
 "prompt": "Quote the etymology of nuisance, and also whatever the page says about innocent, noxious, obnoxious if present."
}
```


## [2026-09-07T18:26:46.542Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/noxious",
 "prompt": "Quote the etymology of noxious and of obnoxious and innocent if mentioned."
}
```


### [2026-09-07T18:26:50.345Z] TOOL RESULT

```
# Etymology of Nuisance

**Nuisance** originated "c. 1400, 'injury, hurt, harm,' from Anglo-French _nusaunce_, Old French _nuisance_" deriving from Latin _nocere_ "to hurt." The meaning has softened over centuries—from harm and injury to "anything obnoxious to a community" (1660s), then to "source of annoyance" (1831).

## Related Words

The page mentions that **innocent**, **noxious**, and **obnoxious** all derive from the same Proto-Indo-European root *nek- meaning "death," connected through Latin _nocere_ "to harm, hurt."

However, the page does not provide individual etymologies for these three words—only listing them as related entries linking to the *nek- root entry.
```


### [2026-09-07T18:26:51.825Z] TOOL RESULT

```
# Etymology of Noxious, Obnoxious, and Innocent

**Noxious** (adj., c. 1500): "unwholesome, harmful," derived from Latin *noxius* meaning "hurtful, injurious," which traces back to *noxa* "injury, hurt, damage." The root ultimately connects to the PIE *\*noks-*, stemming from *\*nek-* meaning "death."

**Obnoxious**: The page lists this as one of several words that might form from the Proto-Indo-European root *\*nek-* (1) "death," indicating it shares the same ancient etymological foundation as *noxious*, though the specific definition isn't provided in this excerpt.

**Innocent**: Also listed among words potentially derived from the *\*nek-* root, suggesting a connection to the same proto-language source, though detailed etymology isn't included here.

All three words trace their lineage back to concepts of harm, death, or injury through their connection to ancient Indo-European linguistic roots.
```


## [2026-09-07T18:27:06.368Z] TOOL CALL #60: Bash

```json
{
 "command": "ls site/pages/357.jpg 2>/dev/null; pdftoppm -f 357 -l 357 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg357 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 357"
}
```


### [2026-09-07T18:27:08.078Z] TOOL RESULT

```
site/pages/357.jpg
total 29232
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 14:27 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43713 Sep  7 12:35 331-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   135301 Sep  7 12:35 331-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    52382 Sep  7 12:41 333-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88345 Sep  7 12:41 333-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68568 Sep  7 12:43 335-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   105946 Sep  7 12:43 335-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:57 340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24993 Sep  7 13:57 340-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92337 Sep  7 13:59 342-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92697 Sep  7 13:56 343hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30778 Sep  7 13:56 343-mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:52 346-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1579505 Sep  7 14:24 afm76.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1055262 Sep  7 14:23 afm77.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1011 Sep  7 14:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   153966 Sep  7 13:44 bqt2014_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63319 Sep  7 12:40 build333.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11800 Sep  7 14:19 c355_arab2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7474 Sep  7 14:19 c355_conn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10501 Sep  7 14:19 c355_runik2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7270 Sep  7 14:19 c355_runik.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46690 Sep  7 13:44 crop_av3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40759 Sep  7 13:44 crop_heb.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94819 Sep  7 13:44 crop_pers0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78732 Sep  7 13:40 ffd32.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61328 Sep  7 13:44 ffd82.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63978 Sep  7 12:35 mk330.py
-rw-rw-r-- 1 sfmqrb sfmqrb    64100 Sep  7 12:34 mk331.py
-rw-rw-r-- 1 sfmqrb sfmqrb    90456 Sep  7 12:42 mk332.py
-rw-rw-r-- 1 sfmqrb sfmqrb    99976 Sep  7 12:34 mk334.py
-rw-rw-r-- 1 sfmqrb sfmqrb    57252 Sep  7 12:38 mk337.py
-rw-rw-r-- 1 sfmqrb sfmqrb    83271 Sep  7 13:58 mk338.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74349 Sep  7 13:57 mk340.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59512 Sep  7 13:57 mk341.py
-rw-rw-r-- 1 sfmqrb sfmqrb    82502 Sep  7 13:57 mk342.py
-rw-rw-r-- 1 sfmqrb sfmqrb    66284 Sep  7 13:55 mk343.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58811 Sep  7 13:57 mk344.py
-rw-rw-r-- 1 sfmqrb sfmqrb    36436 Sep  7 13:51 mk348b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    20510 Sep  7 13:47 mk348.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61503 Sep  7 13:42 navak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3021 Sep  7 13:42 navak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1525 Sep  7 13:41 p342_box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1759 Sep  7 13:41 p342_box3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1703 Sep  7 13:41 p342_box.png
-rw-rw-r-- 1 sfmqrb sfmqrb   108903 Sep  7 13:41 p342hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10531 Sep  7 13:39 p343_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30408 Sep  7 13:39 p343_mus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   103027 Sep  7 14:19 p355hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114524 Sep  7 14:19 p358hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    37883 Sep  7 14:20 p358_q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36134 Sep  7 14:20 p358_q3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4274 Sep  7 14:19 p358_quote.png
-rw-rw-r-- 1 sfmqrb sfmqrb    21223 Sep  7 13:47 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65267 Sep  7 13:37 pg338.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63922 Sep  7 13:44 pg339.png
-rw-rw-r-- 1 sfmqrb sfmqrb   111897 Sep  7 13:44 pg340hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64116 Sep  7 13:39 pg341.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75149 Sep  7 13:40 pg342.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64151 Sep  7 13:39 pg343.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60735 Sep  7 13:42 pg344.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168870 Sep  7 13:42 pg346hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76794 Sep  7 13:39 pg346.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70743 Sep  7 14:25 pg350.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86553 Sep  7 14:25 pg351.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69045 Sep  7 14:18 pg355.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78195 Sep  7 14:27 pg357.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49496 Sep  7 14:19 pg358.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 13:36 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3120575 Sep  7 14:24 skeat1882.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  2985742 Sep  7 14:25 skeatdli.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb      341 Sep  7 13:46 s.py
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T18:27:11.574Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg357.png"
}
```


### [2026-09-07T18:27:11.946Z] TOOL RESULT

```

```


## [2026-09-07T18:27:11.943Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-07T18:27:30.512Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN nectar ==\" && grep -n \"nectar\" KLN_1966.txt | head -5 && echo \"== KLN necro ==\" && grep -n \"^necro\\|necro-\\|nekros\" KLN_1966.txt | head -5",
 "description": "Grep Klein for nectar/necro"
}
```


### [2026-09-07T18:27:30.576Z] TOOL RESULT

```
== KLN nectar ==
2444:ambrosia,  n.,  the  food  (sometimes  the  drink)  of the  gods  in  Greek  mythology.  —  Gk.  au[ipoaia, fern,  of  apPpocnoi;,  a  word  generally  explained in  the  sense  of  ‘immortal’  and  regarded  as  a lengthened  form  of  ap.f)poT0<;,  ‘immortal’.  A.  W. Verrall  has  proved,  however,  that  the  true meaning  of  ap.pp6<no:;  is  ‘fragrant’.  (For  the exquisite  smell  of  ambrosia  cp.  Homer,  Odys¬ sey,  1 8,  192-3.)  ’ApiPpoaio?  is  prob.  a  Semitic loan  word,  with  the  original  meaning  ‘as  fra¬ grant  as  ambergris;  pertaining  to  amber',  and d|xPpooia  stands  for  apppoaia  £8<o8y),  ‘amber¬ like  food’.  Cp.  Arab.  * unbar  (pronounced  ‘d/n- bar’),  ‘ambergris’,  and  see  amber.  See  also nectar.
10054:Cyclobothra,  n.,  a  genus  of  plants  of  the  lily family;  called  also  Calochortus  (bol.)  —  Com¬ pounded  of  cyclo-  and  Gk.  |361>poi;,  ‘pit’  (see bothrium);  so  called  in  allusion  to  the  nectar  es. Cycloconium,  n.,  a  genus  of  imperfect  fungi  ( hot .) —  ModL.,  compounded  of  cyclo-  and  Gk. yfmq,  ‘dust’,  which  is  cogn.  with  L.  cinis, ‘ashes’.  See  cinerary  and  cp.  words  there  re¬ ferred  to.
11517:Dipladenia,  n.,  a  genus  of  plants  of  the  dogbane family  (bot.)  —  ModL.,  lit.  ‘having  two  glands’, fr.  dipl-  and  6(87711,  ‘gland’  (see  adenoid);  so  called in  allusion  to  the  two  nectar  glands.  For  the ending  see  2nd  suff.  -ia.
20639:things’, pi.  of kdthibh, ‘(something) written’, pas¬ sive  partic.  of  katabh,  ‘he  wrote’.  See  prec.  word. Keturah,  fem.  PN.  {Bible).  —  Heb.  Qeturdh,  lit. ‘incense’,  from  the  stem  of  qitter,  hiqttr,  ‘he made  sacrifices,  smoke’,  whence  also  qltoreth, ‘sweet  smoke  of  sacrifice,  incense’.  See  nectar, kevalin,  n.,  a  soul  freed  from  matter  {Jainism). — OI.,  fr.  kevalah,  ‘alone,  belonging  exclusively to  a  single  person’,  fr.  I.-E.  base  *qail *qoil-, ‘complete,  sound,  well,  happy’,  whence  also Goth,  hails,  ‘complete,  whole,  well,  sound’,  OE. hdl,  ‘whole,  uninjured,  healthy’.  See  whole  and cp.  words  there  referred  to. kevel,  n.,  a  peg  or  bollard  to  which  certain  ropes are  fastened  {naut.) — ONF.  keville  (correspond¬ ing  to  F.  chevilk),  ‘peg,  pin,  bolt’,  fr.  VL. *cavieu!a,  dissimilated  fr.  Late  L.  clavicula,  ‘a little  key’.  See  clavicle.
23348:lit.  ‘honey  fly’,  (3X<.tto>  (for  *p.Xmc»),  ‘I  cut  out the  comb  of  bees’.  Alb.  mjai,  mjai te,  honey', OIr.  mil,  ‘honey’,  Ir.  mills,  ‘sweet ,  WBret.  mel, ‘honey’,  Goth,  milip,  ‘honey’,  OE.  mild  raw, ‘honeydew,  nectar’,  milisc,  ‘honeyed,  sweet’, OHG.  milsken,  ‘to  sweeten’.  See  mildew  and  cp. melliferous,  mellifluent.  Cp.  also  meliceris,  meli- Ute,  melilot,  Melissa,  molasses,  mulse,  caramel, hydromel,  oenomel.
== KLN necro ==
25107:necklet,  n.,  1)  an  ornament  worn  around  the neck;  2)  a  necklace.  —  Formed  fr.  neck,  ‘part of  the  body’,  with  dim.  suff.  -let. necro-,  before  a  vowel  necr-,  combining  form meaning  ‘death,  dead,  corpse’.  —  Gk.  vexpo-, vexp-,  fr.  vsxpoc,  ‘dead  body,  corpse’,  fr.  I.-E. base  *nek-,  ‘to  destroy ;  to  perish’,  w'hence  also L.  nex,  gen.  necis,  "violent  death,  murder", nocere,  ‘to  harm,  hurt’,  noxius,  ‘harmful,  in¬ jurious’.  See  noxious  and  cp.  words  there  re¬ ferred  to.
25108:necrobiosis,  n.,  physiologic  death  of  body  cells. —  Medical  L.,  compounded  of  necro-  and  Gk. jJloou;,  ‘manner  of  life’,  fr.  pio?,  ‘life’.  See  bio- and  -osis.
25109:necrolatry,  n.,  worship  of  the  dead.  —  Com¬ pounded  of  necro-  and  Gk.  -XocTpela,  -Xarpia
25112:necrology,  n.,  a  register  of  deaths,  obituary.  — ML.  necrologium,  compounded  of  necro-  and Gk.  -Xoyta,  fr.  -Xoyoi;,  ‘one  who  speaks  (in  a certain  manner);  one  who  deals  (with  a  certain topic)’.  See  -logy  and  cp.  eulogy, necromancer,  n.,  one  who  practices  necromancy. —  Formed  from  next  word  with  agential  suff. -er.
25113:necromancy,  n.,  divination  by  communication with  the  dead ;  witchcraft,  sorcery.  —  ME.  nigro- mancie,  nigromaunce,  fr.  OF.  nigromancie,  ni- gromance,  fr.  ML.  nigromantia,  fr.  Late  L.  ne¬ cro  mantia,  fr.  Gk.  v£xpo|X3tvTEta,  ‘necromancy’, which  is  compounded  of  vsxp6c,  ‘dead  body, corpse’,  and  (xavTctoi,  ‘oracle,  divination’;  see -mancy.  The  change  of  Late  L.  necromantia  to ML.  nigromantia  is  due  to  a  confusion  of  Gk. vexpo?,  ‘dead’,  with  L.  niger,  ‘black’  (necro¬ mancy  was  regarded  as  ‘the  black  art’).  F.  ne- cromancie  and  E.  necromancy  were  influenced  in form  by  L.  necromantia.
```


## [2026-09-07T18:27:39.241Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"nectar,  n\\.\\|nectar, n\\.\" KLN_1966.txt KLN_1971.txt | head -5; echo \"---offset---\"; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))['KLN']\nprint(d['page_offset']); print(d.get('lookup_hint'))\"",
 "description": "Find Klein nectar entry and page offset"
}
```


### [2026-09-07T18:27:40.579Z] TOOL RESULT

```
KLN_1971.txt:159700:nectar, n., the drink of the gods (Greek mythol.) 
KLN_1966.txt:25117:necrosis,  n.,  the  death  of  bodily  tissue.  —  Gk. vExpcocic,  ‘a  becoming  dead,  state  of  death’,  fr. vExpouv,  ‘to  make  dead,  to  mortify’,  fr.  vexpoc, ‘dead’.  See  necro-  and  -osis. necrotic,  adj.  —  See  prec.  word  and  -otic, nect-,  form  of  necto-  before  a  vowel, nectar,  n.,  the  drink  of  the  gods  (Greek  mythoi) —  L.,  fr.  Gk.  vEx-rap,  ‘drink  of  the  gods’,  esp. ‘wine’,  which  prob.  derives  fr.  Heb.  (yayin)  niq- tar,  ‘smoked  (wine),  perfumed  (wine)’,  Niph‘al (=  passive  form)  of  the  Sem.  base  q-t-r,  ‘to make  sacrifices,  smoke’;  qitter  and  hiqtir ,  ‘he made  sacrifices,  smoked’,  are  Pi’el  (=  intensive form),  resp.  Hiph‘il  (=  causative  form)  of  the same  base,  whence  also  ql/Oreth,  ‘sweet  smoke of  sacrifice,  incense’,  Talmudic  and  Targumic Aram,  qitra,  ‘(thick)  smoke’,  Ethiop.  qetare.
---offset---
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-07T18:27:47.727Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nfor n in (25107,25117):\n    lf=('\\n'.join(t[:n-1])).count('\\f'); print(n,'leaf',lf,'-> printed pp', 2*(lf-12)-1, 2*(lf-12))\n\"",
 "description": "Compute Klein page for necro-/nectar"
}
```


### [2026-09-07T18:27:48.991Z] TOOL RESULT

```
25107 leaf 554 -> printed pp 1083 1084
25117 leaf 554 -> printed pp 1083 1084
```


## [2026-09-07T18:27:57.661Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 540 541 542; do echo \"== leaf $i ==\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | grep -o \"^[a-zA-Z-]*,  *[a-z]*\\.\" | head -8; done; echo \"=== search Av nasu in Klein ===\"; grep -n \"Avestic  nasu\\|Av\\. nasu\\|nasu-\" KLN_1966.txt | head",
 "description": "Check Klein leaf 541 headwords"
}
```


### [2026-09-07T18:27:58.935Z] TOOL RESULT

```
== leaf 540 ==
Moslem,  n.
mosque,  n.
mosquito,  n.
moss,  n.
most,  adj.
mot,  n.
Motacilla,  n.
Motacillidae,  n.
== leaf 541 ==
moulin,  n.
moult,  v.
mount,  n.
mount,  intr.
mountebank,  n.
mourn,  intr.
mouse,  n.
moutonnee,  adj.
== leaf 542 ==
Mucor,  n.
mucosity,  n.
mucus,  n.
mud,  n.
mudar,  n.
muddle,  tr.
mudir,  n.
mudiria,  n.
=== search Av nasu in Klein ===
25700:Nox,  n.,  the  goddess  of  night  in  Roman  mythol¬ ogy.  —  L.,  lit.  ‘night’.  See  nocti-,  night, noxal,  adj.,  injurious.  - —  L.  noxdlis,  ‘harmful,  in¬ jurious’,  fr.  noxa.  See  next  word, noxious,  adj.,  harmful,  injurious.  —  L.  noxius, ‘harmful,  injurious’,  fr.  noxa,  ‘harm,  injury’, rel.  to  noced,  nocere,  ‘to  hurt,  injure,  harm’,  and to  nex,  gen.  necis,  ‘violent  death,  murder’.  For the  change  of  e  -  o  cp.  memini,  ‘I  remember’, and  moneo,  T  remind,  admonish’  (see  memento and  monition ) ;  decet,  ‘it  is  comely,  it  becomes’, and  doced,  T  teach’  (see  decent  and  docile)  -,  rego, T  guide,  conduct,  direct’,  and  rogo,  ‘I  ask',  lit. ‘I  reach  after’  (see  regent  and  rogation).  L.  noced and  nex  derive  fr.  I.-E.  base  *ne'k-,  ‘to  destroy; to  perish',  whence  also  OI.  nasyati,  ‘disappears, perishes,  disappears’,  Avestic  nasyeiti,  of  s.m., nasu-,  ‘dead  body,  corpse',  Toch.  B.  nak-sentr, ‘they  blame',  Gk.  vsxu?,  vex-poe,  ‘dead  body, corpse’,  OIr.  ec,  Bret,  ankou,  Co.  ancow,  ‘death’. Cp.  obnoxious,  nocent,  innocent,  nocuous,  noxal, nuisance.  Cp.  also  internecine,  Necator,  necro-, noyade,  pernicious.  Cp.  also  ninny.  For  E.  -ous, as  equivalent  to  L.  -us,  see  -ous.
```


## [2026-09-07T18:28:06.253Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nn=25700; lf=('\\n'.join(t[:n-1])).count('\\f'); print('leaf',lf,'-> pp', 2*(lf-12)-1, 2*(lf-12))\n\"; grep -c \"\" /dev/null",
 "description": "Compute Klein noxious page"
}
```


### [2026-09-07T18:28:07.660Z] TOOL RESULT

```
leaf 566 -> pp 1107 1108
0
```


## [2026-09-07T18:28:22.296Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(560,572):\n    m=re.findall(r'\\b1[01]\\d\\d\\b', t[i])\n    hw=re.findall(r'(?m)^([a-zA-Z][a-zA-Z-]*),\\s', t[i])\n    print(i, 'nums',m[:6], 'first/last hw', hw[:1], hw[-1:] if hw else '')\nEOF",
 "description": "Find Klein printed page numbers"
}
```


### [2026-09-07T18:28:23.569Z] TOOL RESULT

```
560 nums [] first/last hw ['nidorous'] ['nilgai']
561 nums [] first/last hw ['Nilotic'] ['nitric']
562 nums [] first/last hw ['nitrogen'] ['nodulous']
563 nums [] first/last hw ['noel'] ['nonagenerian']
564 nums ['1054', '1066'] first/last hw ['nonagon'] ['Norman']
565 nums ['1056', '1057'] first/last hw ['orman-ize'] ['notification']
566 nums ['1058', '1059'] first/last hw ['Notodontidae'] ['nu']
567 nums ['1080', '1060', '1061'] first/last hw ['nub'] ['numeral']
568 nums ['1062', '1063'] first/last hw ['numerary'] ['nuncupative']
569 nums ['1064'] first/last hw ['nunnery'] ['nympho-']
570 nums ['1066'] first/last hw ['Nyssa'] ['obituary']
571 nums ['1067', '1068'] first/last hw ['object'] ['obreption']
```


## [2026-09-07T18:28:40.160Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN leaf 306 (p.285) ==\" && awk 'BEGIN{RS=\"\\f\"} NR==307' HRN.txt | head -25",
 "description": "Check Horn p.285"
}
```


### [2026-09-07T18:28:41.391Z] TOOL RESULT

```
== HRN leaf 306 (p.285) ==
— 285 —
138. mTitrlh^) 'Urin' (ZI'Gl.), mat (P.-Vend.).
aw. müS^ra-; ai. mätra- 'Urin'.
N.
139. näl {nak?) 'Nase, nur vd. 8 (46), 9 (158).
ap. näh'^) 'Nase' ; aw. naonliau', tiäonhä- ; ai. ndsä-.
Das alte Wort ist schon im Fehle vT aufgegeben,
doch verstand es der Conimentator wohl noch, da er
es nicht erklärt.
140. näirlk Trau, nCiirtklh 'Ehe' (aw. miiruiirana'),
aw. näirika- Trau'; ai. vergl. mir!-.
141. nmnriSflk namentlich, mit Namen*.
aw. *fiqmö.cistika-^) etwa 'mit Beachtung des
Namens*, ai. ^nämacittika^.
142. naslh^) *Leichnam, Aas*.
aw. vam- 'Leichnam, Aas'.
np. nesa, visä kommt nur in Pnrsenschriften vor
(Citate aus Behräm Zerätust).
148. nastnttan Vernichten* (Aw.-Komm., auch in Glossen).
aw. [/lias-, nasyfiti Verschwinden', Causat. ver-
schwinden machen'; ai. [/nag-, ndryati 'verschwinden,
verderben'; lat. necäre, gr. r/xiv.
Hierher wird np. nüslden 'abmagern' gehören (oben
No. 1018), vergl. auch np. fernüs (oben No. 822).
144. nemak 'Gegend'.
```


## [2026-09-07T18:28:52.091Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    if 'nasay' in p or 'nasa' in p.lower() and 'nasay' in p.lower():\n        print('NASAY leaf',i)\n    if 'vinah' in p or 'vinās' in p:\n        print('VINAH leaf',i)\nEOF",
 "description": "Locate SNS leaves for nasay/vinah"
}
```


### [2026-09-07T18:28:53.331Z] TOOL RESULT

```
leaves 243
VINAH leaf 29
VINAH leaf 53
VINAH leaf 140
VINAH leaf 141
NASAY leaf 154
NASAY leaf 155
NASAY leaf 156
VINAH leaf 159
VINAH leaf 222
NASAY leaf 229
VINAH leaf 233
VINAH leaf 238
VINAH leaf 239
```


## [2026-09-07T18:29:02.629Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for i in 154 159; do echo \"=== leaf $i ===\"; awk -v n=$((i+1)) 'BEGIN{RS=\"\\f\"} NR==n' SNS_pages.txt | grep -n \"nasay\\|nasa\\|vinah\\|vinās\\|vinas\" | head -8; done",
 "description": "Print SNS leaves 154 and 159"
}
```


### [2026-09-07T18:29:03.960Z] TOOL RESULT

```
=== leaf 154 ===
17:^o^>           •**-**** nasay niganih:
20:^jb^^a^Ui rnasay x v ardan: tf^i -o*l
29:/T   ^ ..^,TUj^,ljl* Jj.4*,l «JJii-^»S rfij :nasay
91:                        s                                        ^'|                                     >u-*»<«*»t«ttl. **(-,)                   :nasay/nasa:                    -0»i/-^*i
95:                    v'^^-j'j'^'j-J'J^tOvistarg:                        ^^»                  I    '>tf>W nasae              : {,       (Mir. Man. IIi,58)ns*w
=== leaf 159 ===
4:O-utl .^J.jU.^^.ojlp: vinahtarih:
15:invinahtar:                        .^Irf-.vinShtarsV^-*                             nabh-         CHSf^Shah tj\ napta-
37:                .j*Kktf :vinah kar tar:
58:                                                    U/A**                           *^: vinah viaardan:
```


## [2026-09-07T18:29:19.415Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON نسا ==\" && grep -c \"نسا\" MON_part1.txt MON_part2.txt 2>/dev/null; echo \"== MON جناح ==\" && grep -n \"جناح\" MON_part1.txt MON_part2.txt 2>/dev/null | head -5; echo \"== files ==\"; ls -la MON_part1.txt MON_part2.txt | head",
 "description": "Grep Mo'in local files"
}
```


### [2026-09-07T18:29:19.514Z] TOOL RESULT

```
== MON نسا ==
MON_part1.txt:397
MON_part2.txt:411
== MON جناح ==
MON_part2.txt:14058:پهلودار (جناحین). عقبدار (موّخره). 
MON_part2.txt:27323:دوش. بال پرنده» جناح. شاخهٌ درخت» شاخ. 
MON_part2.txt:70250:چپ. (نظ.) جانب چپ میدان جنگ» جناح 
MON_part2.txt:86638:خواری» ذلت. فروتنی. . وضع جناح: فرو تنی 
MON_part2.txt:86639:(قس. خفض جناح) (امثال و حکم ده خدا. 
== files ==
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
```


## [2026-09-07T18:29:27.148Z] TOOL CALL #72: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%D8%B3%D8%A7/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for نسا verbatim, including any origin tag such as [په.] or [ع.], and also the Dehkhoda entry if it mentions corpse/مردار."
}
```


## [2026-09-07T18:29:27.756Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AC%D9%86%D8%AD%D9%87/",
 "prompt": "Quote the فرهنگ معین (Mo'in) entry for جنحه verbatim, including origin tags, and the Dehkhoda entry."
}
```


### [2026-09-07T18:29:32.823Z] TOOL RESULT

```
# فرهنگ معین Entry for نسا

According to the Mo'in dictionary, the entry reads:

"(نَ) (اِ.) نک. نسر. (~.) [په.] (اِ.) لاشه، مردار."

This indicates the word has medical/anatomical origins [په.] and means "corpse" or "carrion."

# Dehkhoda Entry

The Dehkhoda lexicon also confirms this meaning, stating that نسا refers to "the flesh and bones of a dead person" (گوشت و استخوان مرده را گویند) in Avestan and Pahlavi origins, with the meaning extending to anything "decayed and putrid."
```


### [2026-09-07T18:29:33.773Z] TOOL RESULT

```
# فرهنگ معین Entry

"(جُ حِ ) [ ع . ] (اِ. ) گناه ، بزه کوچک ."

# Dehkhoda Entry

"( جنحة ) جنحة. [ ج ِ ح َ ] ( ع اِ ) اِثْم. ( محیط المحیط ). گناه ، و این لغتی است عامیانه و در هیچ یک از لغت نامه های معتبرنیست."

The Dehkhoda lexicon notes this is colloquial terminology absent from authoritative dictionaries, while defining it primarily as a sin or transgression.
```


## [2026-09-07T18:29:46.961Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%81%D8%B1%D9%86%D8%A7%D8%B3/",
 "prompt": "Quote the فرهنگ معین and Dehkhoda entries for فرناس verbatim, including any etymological note or origin tag."
}
```


## [2026-09-07T18:29:47.674Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B4%D8%AA%D8%B1/",
 "prompt": "Quote the فرهنگ معین and Dehkhoda entries for نیشتر verbatim, including origin tags and any etymology."
}
```


### [2026-09-07T18:29:52.920Z] TOOL RESULT

```
# Lexicographic Entries for فرناس

**Dehkhoda Entry (Abbreviated):**
"فرناس. [ف َ] (ص) درهندی باستان پر + نچ، درسنسکریت پرناچه. (از حاشیه برهان)"
The entry indicates the word derives from Old Hindi and Sanskrit origins, with meanings including "heedless," "ignorant," and "drowsy."

**Farhang-e Moein Entry:**
"(فَ) (ص.) ۱ - غافل، نادان. ۲ - خواب آلود. (فِ) (اِ.) ۱ - مهتر روستاییان"
This source lists the word with different pronunciations and grammatical forms, defining it as "heedless/ignorant" and "sleepy" in one form, and "village elder" in another.

Both entries demonstrate the word's multiple meanings across Persian lexicographic tradition, with etymological roots traced to ancient Indo-European languages.
```


### [2026-09-07T18:29:52.952Z] TOOL RESULT

```
# نیشتر Dictionary Entries

## فرهنگ معین
"(تَ ) (اِ. ) آلت نوک تیزی که با آن رگ می زدند."

## Dehkhoda (لغت نامه دهخدا)
"نیشتر. \[ ت َ \] ( اِ ) مبضغ. ( دهار ). ابزاری مر جراحان را که بدان رگ می زنند و فصد می کنند و آبله می کوبند"

Both entries describe this as a sharp-pointed medical instrument used by physicians and phlebotomists for bloodletting and surgical procedures.
```


## [2026-09-07T18:30:18.794Z] TOOL CALL #76: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-07T18:30:18.834Z] TOOL RESULT

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


## [2026-09-07T18:30:39.387Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== WLD nek ==\" && grep -n \"nek-\\|nāśáyati\\|nasyati\" WLD_band3.txt incoming/WLD/WLD_Bd2_pages.txt 2>/dev/null | head -8; echo \"== LEW noceo ==\" && grep -n \"noceo\\|noxa\" LEW_1910.txt | head -5; echo \"== LAT noceo ==\" && grep -n \"noceo\\|nocere\" LAT.txt | head -5",
 "description": "Grep Walde-Pokorny and Latin dictionaries"
}
```


### [2026-09-07T18:30:39.463Z] TOOL RESULT

```
== WLD nek ==
incoming/WLD/WLD_Bd2_pages.txt:21241:s.   "^enek- „reichen‘^
incoming/WLD/WLD_Bd2_pages.txt:21561:nek- „umkommen“, neku-s „Toter, Leiche'".
== LEW noceo ==
2846:andegoe II 762 dzowa II 330 anoxadéw I 128 azcohatiwm I 553,
== LAT noceo ==
3807:anxius (cf. noxa, noxius et noceo; alsus, alsius et algeo): sens
9711:de capiS, conparable 1 noxa en face de noceo. 6tynologie obscure.
16115:de noceo. - V. aussi disco et doceo. •
38817:la racine *men- "penser", du type de noceo, foueo, etc., cf. mens,lloneta
41351:Tardifs: nocibilis, nocentia, renoceo.
```


## [2026-09-07T18:30:40.438Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SKT nectar ==\" && grep -n \"^Nectar\\|Nectar,\" SKT.txt | head -5; echo \"== SKT noxious ==\" && grep -n \"^Noxious\\|Noxious,\" SKT.txt | head -5; echo \"== SKT nuisance ==\" && grep -n \"Nuisance\" SKT.txt | head -3",
 "description": "Grep Skeat"
}
```


### [2026-09-07T18:30:40.508Z] TOOL RESULT

```
== SKT nectar ==
== SKT noxious ==
12485:Noxious.  (L.)  L.  noxiui,  hurtful.  * L.  ncxa,  hurt.  —  L.  noftrtt  10  hurt ;  cf.  n^:x, destruction.     (VNAK.)
== SKT nuisance ==
12502:Nuisance ;  see  Noxiooa.
```


## [2026-09-07T18:30:46.992Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '21555,21600p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== page tag ===\"; awk 'NR<=21561 && /\\[pdf page/ {last=$0} END{print last}' incoming/WLD/WLD_Bd2_pages.txt",
 "description": "Read Walde-Pokorny nek- entry"
}
```


### [2026-09-07T18:30:48.337Z] TOOL RESULT

```
langen, Begier“,           ags.   nml    f.   „Wunsch, Sehnsucht,        Eifer^\   Persson Beitr.
223,       Falk-Torp u. nijdelig.             Da6 „wornach       einen   Ruck machen“         die ur-
spriinglicheAnschauung sei, so daB Erw. zu neu- „nicken, einen Ruck
machen'^, woran Brugmann aaO. fiir paniistu denkt, ist ganz fraglich.


nek- „umkommen“, neku-s „Toter, Leiche'".
     Ai.    nagyati,     „geht verloren, verschwindet, vergeht^, nacdijati
                       nacati
.,macht verschwinden,   richtet zugrunde^' (dehnstufig gegeniiber lat. noceo),
av. nasyeiti „verschwindet“, Ptc. ai. na^td- „verlorengegangen“, av. naMa-
ds. (-= lat. e-nechis),          nasiUa- „verderblichst“,        ms- f. „]S'ot, Ungluck“ r= lat.
nex, gr. vex-Tag, vexeg;^ ai. -nag Adj.), 7iasti- „Leichnam, Aas“                   (= gr. vexvg,
lat.      nequ-alia ; vgl.   "^nlcu-   usw), dehnstufig ai. ncica- m. „das
                                        in    air.   ec
Zunichtewerden*^ gr. vExeg' vsxgot Hes. (davon vexdg ,,Haufe Leichen“,
                       ;


Yorbild dexag), vex-jag „GottertraEk^^ („*Tod iiberwindend'^, Prellwitz s. v.),
vexvg, vexgog „Leichnam‘’;   vd)xag „Tragheit, TodesschIaf“; lat. ncx ,,ge-
waltsamer Tod, Mord^^,   davon denicdles fUriae „de nece purgantes^^, neco,
-are „toten^‘ {e-nectus „erschopft^^, wo von e nectar e „urabringen, qualen'^;
scheint aber primare Bildung); pernicies ,,Yerderben, Untergang'*, inter-
necieSy -necinm ds. ; noceo „Schade‘*, 7ie boa noccit (Lucilius
                                                                  1195)^ Ptc.
^noxns vorausgesetzt von noxa „Schaden, Strafe, Schuld'^; neqtialia „de-
trimenta^‘ (auf Grund des St. nehii-^', air. cc, bret. cmhon^ corn. ancoWy
cymr.        „Tod'‘          aisl. (Noreen Ltl. 178) Naglfar „Totenschiff“.
  Ygl. Curtius 162; Pick I ^ 96, 272, 501; Stokes BB. 16, 51, Fick II ^ 32,
Strachan 20, 30, Pedersen KG. 146; gegen Yerkniipfung mit         „Zwang‘*
s.   d.


negh „durchbohren, stechen, stupfen“?
     Aksl.        pro-yiozlti „durchbohren^^, no^h „Messer^'             = lett. nafis Messer",
                                                                                        ,,

aksl. nhzq „stecke hinein“;             ir. ness ,,Wunde‘' {^negh’-so-, -sa; Strachan lA.
4, 103,      FickIIM9l);          vielleicht ai.      „Stange^‘ (Geldner Yed. St.1 136f.;
                                                         net         ne-tr   .   .    na-tr   .   .
                                                                                                                                      327

* 7 i(jh-sit-          nach Johansson IF. 2, 51 f., Wackernagel Ai. Grr. I 10;                                                kaum     zu
o^vg).        — Ganz fraglich aber ahd. nagan, nmg „nagen, reiben*' (Fick BB.
1,    241,        Wb.                                             md, nhd.
=== page tag ===
```


## [2026-09-07T18:31:00.730Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== POK niks ==\" && grep -n -i \"niksati\\|neksana\\|nikṣ\" POK_full.txt | head -8; echo \"== WLD niks ==\" && grep -n -i \"niksati\\|neksana\" incoming/WLD/WLD_Bd1_pages.txt incoming/WLD/WLD_Bd2_pages.txt WLD_band3.txt 2>/dev/null | head -8; echo \"== IEC niks ==\" && grep -n -i \"niksati\\|neksana\\|nekso\" IEC.txt | head -8",
 "description": "Search for Sanskrit nikṣ- root in POK/WLD/IEC"
}
```


### [2026-09-07T18:31:00.832Z] TOOL RESULT

```
== POK niks ==
== WLD niks ==
incoming/WLD/WLD_Bd2_pages.txt:21303:niniksati, necht ,,rein" (nicht zu ^neih- „Getreide schwingen", s. d.)
== IEC niks ==
11604:neksos, us (1) “bond, tie’. Cf. nekstos, naskos & neKsos. Variant: nesk- Tokh. (?) nasu ‘friend’; Lat. nexus, gs: -üs, m. ‘tie, band, bale’; Ir. neasc, m. id. (beside nasc ‘collar’: Br. nask); W nais, pl. neisiau, m. id. beside naith, pl. neithion, m. ((2) “betrothal, fr. *nekt- or *nekst-); G. cf. Nistel, f. 'band- age; buckle-beit; lace; shoestring’ (beside Nestel, id. fr. *nast- or *nakst-); ON nist, nisti, n. "brooch: pin” beside nezla, f. (“button- hole”, i. e. *netsla! perh. fr. *nakstila). (Fr. nasse *fish-basket! is a LW, perh. Gallo-Lat.). Cf. Av. nasko, m. ‘chapter, section’
11605:neksos (nesk-) (2) *pus, wound, furuncle' (?). Cf. niks- (2) Arm. nex, o-st. ‘pus’; Gael. neasg “boil, furun- cle; MIr. ness ‘lesion’, fr. a variant of type *neksts via *nekss); Br. nech, m. “worry”
11606:nekstos (nektos), variants of type neksos (1) above. Cf. neKs- Lat. cf. necto, Ere, pf. nexi, sup. nexum “join; knit; spin; frame’; W nais, pl. neisiau, m. (band, De fr. *nektios) beside naith, pl. nei- thion m. ((2) *betrothal, fr. *nektis); OE cf. nestan, v. (^spin'. Phonol. uncertain); ON nist, nisti, n. "brooch, pin’; cf. G Nistel, f. "band. age, belt, shoestring'. (For the variant Nestel, Du. nestel, see nast-. W ambig.)
11621:neKs- (neK-, neKst-) ‘approaching; near. (Variant: neks-). Cf. WP I, 59; I, 129 & II, 328. Cf. neksos, nekstos Per. cf. naxün (first. LW in Arm. nax first); nuxust, adj. “first, beginning’; Tokh. A nes, B naus, invar. adv. ‘earlier; Vedic cf. násami, Skt. nasSayami, v. “reach, approach’; Av. cf. nãs-, v. (2) ‘reach’; uncertainly to Tokh. A nasu "Trend: variant (*neks-) in Skt. naks-, Av. é-nak&-, v. ‘reach’; Lat. cf. nec-esse "to be necessary’; Osc. cf. nistrus, acc. pl. f. ‘nearer’; nessimas, fpl. (nearest, hence *near); Mir. nessa, mod. neas ‘nearer’; nessam, adj. “near- est; com-nessam, m. ‘neighbour’; W nes, Br. nés, néz, Cor. nes, adj. & adv. “near; nearer; W nesaf, adj. ‘next’. (The connexions of Go. néhw-, G nach, nah, OE neah are uncertain, but do not belong here)
```


## [2026-09-07T18:31:05.967Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^niks-\\|niks- (1)\\|niks- (2)\" IEC.txt | head; echo \"---\"; grep -n \"niks\" IEC.txt | head -10",
 "description": "Grep Mann IEC for niks-"
}
```


### [2026-09-07T18:31:06.032Z] TOOL RESULT

```
11595:neik-, see noik-, nik- (2) “effort, force’. Cf. niks- (1) Gk. neikos, n. ‘strife’; Lat. cf. per-nix, gs: -nicis, adj. (persistent, pressing, quick’; Cz. cf. v-nikat, -niknout, inf. ‘penetrate’; Li. cf. į- ninku, -nikti, v. “tackle, struggle with’; j-nykis, gs: -io, m. ‘gusto’
11605:neksos (nesk-) (2) *pus, wound, furuncle' (?). Cf. niks- (2) Arm. nex, o-st. ‘pus’; Gael. neasg “boil, furun- cle; MIr. ness ‘lesion’, fr. a variant of type *neksts via *nekss); Br. nech, m. “worry”
11677:nesk- (?) ‘rot, pus’. Evidence ambig. See niks- (2) and neks- (2) Arm. nex, o-st. ‘rot, decay’; Gael. neasg "Tur, uncle’; Ir. cf. neascóid, m. id.
11757:nik- (2) ‘thrust, force, penetrate’. Cf. niks- (1) Skt. cf. nicah, m. ‘a perfume’; Lat. cf. for-nix, gs: -nicis, m. Catch, doorway’ fr. *dhuer-?); W nig, pl. -ion, m. ‘squeeze, strait’; nigio, inf. denom. ‘squeeze’; OCS nico, nicati (sic) “bud, sprout’; Srb. ničem and nicim, niknem, inf. nicati, id.; Cz. cf. v-niknout, inf. *pene- trate’; Li. cf. ninku, nikti, v. ‘tackle’; Latv. cf. nikns, adj. ‘evil’. (Isophone in Li. nykis, gs: io, m. *whim'). Cf. Lat. per-nix, gs: -nicis *per- sistent?’
11759:niks- (1) “press, force, pierce, penetrate’. Cf. nik- (2) Skt. níksami, v. ‘pierce’; Lat. nixus, gs: -üs, m. “effort; trend"; Li. cf. ninku, nikti, v. ‘tackle’. (Isophones: Skt. niksanam *stirring-rod'; Li. niksas ‘thimble’, nikstas ‘dislocation, crack in bones”, nykštys, 10, m. ‘thumb; big toe’). Cf. also Lat. per-nix, -nicis ‘persistent
11760:niks- (2) (nisk-, nesk-?) Arm. nex, o-st. (decay, pus; W nych, m. ‘languishing state’; nychu, v. inf. ‘pine’; Br. nech, m. ‘worry’; cf. Gael. neasg, Ir. neasc- óid, m. ‘furuncle, boil
11809:noit- (2), o-gde variant of type *neit-, see nit- (1) Lat. cf. (vowel ambig.) nitor, sup. nisus & nixus (of two separate origins but here in the sense of “strive*); Cz. cf. pod-nét 'enter- prise’; pod-nítit, inf. ‘undertake’. (For sup. nixus, cf. niks- (1) above)
---
11135:beside G mannig — in mannig-faltig *mani- fol)”, id.; Sw. mánge, många, mången, id.; OCS münogo, mnogo, prn., mnogü, adj. id.; Finn. LW moni, id. beside monikko, s. *plu- ral; menekki "a good sale, demand Cf. a variant of type *menighs-, meniks- in Ir. me- nicc ‘frequent’; W mynych, adv. ‘often’. Ver- bal type (monoghið) in Go. managjan “in- crease’: OCS množiti, id.
11595:neik-, see noik-, nik- (2) “effort, force’. Cf. niks- (1) Gk. neikos, n. ‘strife’; Lat. cf. per-nix, gs: -nicis, adj. (persistent, pressing, quick’; Cz. cf. v-nikat, -niknout, inf. ‘penetrate’; Li. cf. į- ninku, -nikti, v. “tackle, struggle with’; j-nykis, gs: -io, m. ‘gusto’
11605:neksos (nesk-) (2) *pus, wound, furuncle' (?). Cf. niks- (2) Arm. nex, o-st. ‘pus’; Gael. neasg “boil, furun- cle; MIr. ness ‘lesion’, fr. a variant of type *neksts via *nekss); Br. nech, m. “worry”
11677:nesk- (?) ‘rot, pus’. Evidence ambig. See niks- (2) and neks- (2) Arm. nex, o-st. ‘rot, decay’; Gael. neasg "Tur, uncle’; Ir. cf. neascóid, m. id.
11757:nik- (2) ‘thrust, force, penetrate’. Cf. niks- (1) Skt. cf. nicah, m. ‘a perfume’; Lat. cf. for-nix, gs: -nicis, m. Catch, doorway’ fr. *dhuer-?); W nig, pl. -ion, m. ‘squeeze, strait’; nigio, inf. denom. ‘squeeze’; OCS nico, nicati (sic) “bud, sprout’; Srb. ničem and nicim, niknem, inf. nicati, id.; Cz. cf. v-niknout, inf. *pene- trate’; Li. cf. ninku, nikti, v. ‘tackle’; Latv. cf. nikns, adj. ‘evil’. (Isophone in Li. nykis, gs: io, m. *whim'). Cf. Lat. per-nix, gs: -nicis *per- sistent?’
11758:nik- (3) “low; down; fall’. Cf. ni-, ni- Skt. nicah “low, base’; nicyami “lie low, be servile'; Per. cf. nigün adj. “bent downward', LW in Arm. nkun ‘abased; base’; OCS nif, OCz. nice ‘prone’; Srb. nik, m. ‘fall, lowering’; R niknuť, inf. ‘stoop’; Ukr. cf. nyknuty, inf. ‘disappear’; Cz. cf. zá-nik ‘downfall, eclipse’; Li. nykstu, nýkti, v. ‘disappear, perish’; nykùs, adj. ‘grim, awful’, cf. also nykulys, gs: -io, m. ‘decline’; Latv. nikstu, nikt, v. ‘languish, per- ish’; Big. nica se, v. ‘crouch’
11759:niks- (1) “press, force, pierce, penetrate’. Cf. nik- (2) Skt. níksami, v. ‘pierce’; Lat. nixus, gs: -üs, m. “effort; trend"; Li. cf. ninku, nikti, v. ‘tackle’. (Isophones: Skt. niksanam *stirring-rod'; Li. niksas ‘thimble’, nikstas ‘dislocation, crack in bones”, nykštys, 10, m. ‘thumb; big toe’). Cf. also Lat. per-nix, -nicis ‘persistent
11760:niks- (2) (nisk-, nesk-?) Arm. nex, o-st. (decay, pus; W nych, m. ‘languishing state’; nychu, v. inf. ‘pine’; Br. nech, m. ‘worry’; cf. Gael. neasg, Ir. neasc- óid, m. ‘furuncle, boil
11809:noit- (2), o-gde variant of type *neit-, see nit- (1) Lat. cf. (vowel ambig.) nitor, sup. nisus & nixus (of two separate origins but here in the sense of “strive*); Cz. cf. pod-nét 'enter- prise’; pod-nítit, inf. ‘undertake’. (For sup. nixus, cf. niks- (1) above)
```


## [2026-09-07T18:31:17.648Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== AFM leaf for p.45 ==\" && python3 -c \"\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,p in enumerate(t):\n    if 'جناح' in p or 'گناه' in p:\n        print('leaf',i,'|', [l for l in p.split(chr(10)) if 'جناح' in l or 'گناه' in l][:3])\n\" 2>&1 | head -20",
 "description": "Grep Addi Shir for junāh"
}
```


### [2026-09-07T18:31:19.226Z] TOOL RESULT

```
== AFM leaf for p.45 ==
leaves 198
```


## [2026-09-07T18:31:19.534Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PLA junah ==\" && grep -n \"جناح\\|gunāh\\|gonāh\\|wināh\" incoming/PLA/PLA_pages.txt | head -10; echo \"== LKT gunah ==\" && grep -n -i \"gunah\\|dschunah\\|junah\" LKT.txt | head -5",
 "description": "Grep Asbaghi and Lokotsch"
}
```


### [2026-09-07T18:31:19.593Z] TOOL RESULT

```
== PLA junah ==
== LKT gunah ==
```


## [2026-09-07T18:31:24.089Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==60' AFM_pages.txt | head -20",
 "description": "Sample AFM page"
}
```


### [2026-09-07T18:31:25.302Z] TOOL RESULT

```
3
( 3 امتلاء في 9 (܇ 6 وهو الرجل القوي الجييل
.1 :
+ ( اند لس ) الناقة الكثيرة اللحم السترخية مشتقّة من 0 ومعناه
المجمرع ܢ /
+ ( االخئذيان) البذي اللسان تعريب :ܪ اي ذو رائحة كر يبة
+ ( 95[ 15 3798[ الحيد 97591 95505 7[
ومعناة الشجيع ورئيس !ܙ والفاضل ,ܬ
+ ( ` وردت في 5 في قصة عبدالله بن عباس وجده الرشيد
قال: « - 6( الابد الّا من المغتين وطبقة ايتاك ين ».
فلت دهي جع سانا ܬܨ
( الور ;31( الدنيا تعريب خنور وهي كئابة عن جيع 53 1
1 ±
فإلترذة ) امغر ارين مد
(5.030 وقسالوا‎ ٠. وان الذي عساء‎ "5 3 (5 <١
ܕܝܕ ܙ خورا أى ضعف‎
* (الخآن) فارسي بجت وهو !ܬ :ܝ وهو موجود في ܬܝ اللغات الغرةة
الدارجة ٠.‏ واصل الكلية اراعيى ܚܢܘܬ ܐ وهو يطلق على الدكان والمخدع والماخور
وهو مشتئق من سمه اي مال 3
.]05 فارسي ܐܨ وهو ااسلطان ܕ ܚܝܢ سلاطين الخطا ܕ ܫܝ
```


## [2026-09-07T18:31:36.527Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN p.208 ==\" && awk 'BEGIN{RS=\"\\f\"} NR==230' HRN.txt | grep -n -i \"gunah\\|gunāh\\|venah\\|vinas\" | head -5; echo \"== HRN grep gunah ==\" && grep -n -i \"gunah\\|gunāh\" HRN.txt | head -8; echo \"== HUB gunah ==\" && grep -n -i \"gunah\\|vinas\\|vnas\" HUB.txt | head -8",
 "description": "Horn/Hübschmann on gunāh"
}
```


### [2026-09-07T18:31:37.784Z] TOOL RESULT

```
== HRN p.208 ==
== HRN grep gunah ==
== HUB gunah ==
5499:mana-'y gunah *Sunde' — phi. v(i)nas, arm. vnas; guvdhdan
5625:'auserwahlt' ? ; vnas 'Schade, Verlust, Unrecht, Schuld* =
5710:es vi vor n (+ Vokal?) zu gu macht, daher gunah *Sunde*
7512:gunah *Sunde* = pfiz. gunah Shk. 247, phi. v(i)nad^ Gl. and
7524:dahekan und akah erscheint, liegt s vor in vnas 'Schade,
7530:gundh ^), arab. jun^ (Koran), phi. v(i)ndd^, 1st arm. vnas
7531:auf ein ap. "^vinasa- (neben ^vinad^a- = paz. np. gunoh ; g.
7565:lehnte np. gunah zu gunas geworden ist.~ 213 —
```


## [2026-09-07T18:31:42.171Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7500,7570p' HUB.txt",
 "description": "Read Hübschmann on gunāh/junāh"
}
```


### [2026-09-07T18:31:42.213Z] TOOL RESULT

```
6, Bdh. Gl. 149, arm. dah-ekan (5. Jhd.) 'dgax/nfj, dtjvdgiov,
ap. *da^a (aber zd. dasa, semn. das ZDMQ. 32, 538u. s.w.);
rdbah 'Fuchs' = phi. rOpad^ Bdh. 30, 18 (aber bal. ropask,
skr. Idpa^a-); nigah *Anblick* = phi. n{i)kad^ Gl. and Ind.
246, ap. ^nikad^a- ; agah *kundig = paz. agah Min. Gl. 29,
phi. akad^ Gl. and Ind. 30, arm. akah (5. Jhd.), ap. *<lifl^a-;
nagdh *pl6tzlich' = paz. anagdh Shk. 228, phi. andkadiha
H. 1021 (aber zd. oka sat 'erblickte', kis. ipt. bikes Shuk.
202, skr. kuQ); guvah 'Zeuge' = phi. guka&^) Gl. and Ind.
281, ap. ^mkdd^a- zu skr. vi -f- kag?; s% *dreissig* aus *sth
= ap. ^^''Id^at- = zd. d^risatem (oben p. 78) ; panjah *funf-
zig* = ap. *panda9^at', zd. pancasatem, skr. pafidagaf-;
gunah *Sunde* = pfiz. gunah Shk. 247, phi. v(i)nad^ Gl. and
Ind. 24:7 ; padaf rah *Vergeltung, Strafe* = pfiz. pddafrdh
Shk. 261, phi. j^a^a/m^, a,ip.*pdtifra9^a', vgl. zd. paitifrasa-;
tih leer*, HhT = phi. tuhtk, vgl. bal. fusay *ausgehen*, skr.
tucchya-; phi. pah *Vieh* Horn p. 287 = zd. pasu-, Vgl.
auch ahan 'Eisen', kurd. hasin u. s. w. (oben p. 10) ; dha
^Gazelle', bal. dsk u. s. w. (oben p. 11). Ueber kdstan, kd-
ham H. 835 und Mh 'Stroh' s. oben p. 86. Also sollte ap.
vi9^- *Haus, Familie = zd. vis- im Np. *bih (= paz. *i?iA,
phi. *yt^) lauten, wie es lautgesetzlich richtig im Balu5i
durch gis *Hausstand' vertretea ist 2).
Wahrend im Armenischen h == mp. np. h fiir ap. ^ in
dahekan und akah erscheint, liegt s vor in vnas 'Schade,
Verlust, Unrecht, Schuld' (5. Jhd.) gegeniiber paz. np.
^) Man miisste fQr ap. *vika&a' im Phi. v{i)kii& erwarten. Siehe
§ 53.
2) Hierher oder zu § 95 np. rahi *Diener' = phi. rank?
14*— 212 —
gundh ^), arab. jun^ (Koran), phi. v(i)ndd^, 1st arm. vnas
auf ein ap. "^vinasa- (neben ^vinad^a- = paz. np. gunoh ; g.
venah) zuriickzufuhren? Vgl. auch arm. patuhas 'Strafe*,
wenn es zu np. yddafrah gehort. Und wie verhalt sicli
np. xur^h *Hahn (belegt von Browne JRAS. 1894, 457) zu
xuros und amas (A. M. 8, 8) 'Geschwulst' zu amah (Horn
p. 106 Anm. 1)? Vgl. den Wechsel von ap. rs und r^
aus rk^ (§ 103) und von ap. z, rz und d, rd (Kap. 20).
§ 101. In einigen Fallen findet sich auch zwischen
Vokalen np. s, wo, nach np. has = ap. vasiy zu urtheilen,
im Ap. s, nicht ^ stand: has viel, genug == ap. vasiy (zu
vas = s\iv, vag Vollen'?); kargas 'Geier = zd. kahrkasa-;
pes *Aussatz, aussatzig JRAS. 1894, 451 = zd. pa^sa-;
ges^ gSsU Locken* = zd. ga^sa-; nivSsam 'ich schreibe' =
ap. *nipaisamiy {niyapisam ist sigm. Aorist ^- idg. ni-e-pik^-
sO'tn); resam *ich. spinne', hah resay; xusur 'Schwiegervater
= zd. x^asura-; rasan *Strick' = skr. ragana-; cis *Muhl-
stein', vgl. zd. asan- *Stein ; btst 'zwanzig aus *visat = zd.
vlsaiti; xuros *Hahn, skr. Wrzl. krog; kus H. 852 (?)
Fur an- und inlaut. i' -= s ist unregelmassig s ein-
getreten in: sdx 'Ttweig =■ skr, gakha- (vgl. Bart hoi omae,
Studien II, 41 flg.); sus Xunge' aus *sus mit Assimilation
des Anlauts an den Auslaut = zd. susi-; as *Bruhe' aus
*{?sa-? H. 29; xuros 'Geschrei*, xurosidan *schreien = phi.
xrdsttan (oben p. 55).
§ 102. Ap. s (= idg. k^) vor p (— idg. v), y, m und
r = phi. paz. np. s: asp *Pferd* = ap. aspa-; aspand
*Raute' = zd. spenta-; siped Veiss' = zd. spaeta-; sipihr
'Himmel* = ap. 2md-Qi-, skr. gvitra-; phi. harvisp jeder=^
ap. haruva- -)- vispa- ; mit Ausfall des p : suvHr *Reiter =
ap. asabara-] astar ^Maulesel' = ap. ^asatara-, skr. agva-
tara-; sa^ Hund', medisch andau, zd. spa; — siyah *schwsirz
•^ zd. syava- (aber kasaf 'Schildkrote' = zd. kasyapa-,
Auifallig ist' auch bal. gunas. Man hat fiir iran. Hinasa- =
ap. *vina9a- im Bal. *gtnas zu erwarten, das vielleicht duroh das ent-
lehnte np. gunah zu gunas geworden ist.~ 213 —
skr. kagyapa-); — dsmdn 'Himmer = ap. asman-am (ace);
— xusru *Schwiegermutter (auch xmfl u. s. w.) = skr.
gvagrU-] Xusrav = arm. Xosrov, zd. husravah-; Sards (der
Engel) ^ zd. sraosa-; suriidan singen, pr. sarayam, zd.
srU'\ sardi *Palast* = ap. "^srada-; surun 'Hinterbacken* =
```


## [2026-09-07T18:31:54.492Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY گناه ==\" && grep -n \"گناه\" incoming/ARY/ARY_pages.txt | head -5; echo \"== ARY نیش ==\" && grep -n \"نیش\\b\\|نیشتر\" incoming/ARY/ARY_pages.txt | head -5; echo \"== ARY نسا ==\" && grep -n \"نسا \" incoming/ARY/ARY_pages.txt | head -3; echo \"== ARY latin index ==\" && grep -n -i \"GUNAH\\|NISH\\|NASA\" incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "Grep Aryanpur"
}
```


### [2026-09-07T18:31:54.594Z] TOOL RESULT

```
== ARY گناه ==
== ARY نیش ==
344:جزیره) ایبری (اسپانیا و پرتغال) سنگك نیشته‌هایی پدست آمده که به یکك زبان غیر هند و اروپایی قبل
1787:اوستایی (/۸۲587۸2): مدا نیش هلندی (۵076[3): اج رکه
15992:برهان قاطع : رما نیشن
== ARY نسا ==
== ARY latin index ==
480:Spanish | Lithuanian | albanian Armenian Tocharian A
700:NASAL oh 5 El Ly ye 5 (VEDAS Io9) alpaca US 3Hy L YsFalHy Soy
1402:(TIL)RADE DANISH) Sails GAREDAN, REDAN (GOTHIC) eng
1452:LOKIEC POLISH) lea’ ARASHNISH (OLD PERSIAN) pleat gy
1469:BUCKL: 237-283 ALBUE DANISH) Salo
```


## [2026-09-07T18:32:05.160Z] TOOL CALL #88: Bash

```json
{
 "command": "for u in \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne%E1%B8%B1-' \\\n 'https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%A7%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B4' \\\n 'https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A7%D8%AD' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 357, roots Nek 1 / Nekš: PIE *neḱ-, Persian gonāh/nīš, Arabic junāḥ' 2>&1 | tail -2; done",
 "description": "Archive Wiktionary sources"
}
```


### [2026-09-07T18:32:07.967Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/c82f1aec53afa359.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/730d3c473dc773a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/675739a7fa13d009.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/430e03e3b0bffd73.txt
```


## [2026-09-07T18:32:13.801Z] TOOL CALL #89: Bash

```json
{
 "command": "for u in \\\n 'https://www.etymonline.com/word/nectar' \\\n 'https://www.etymonline.com/word/nuisance' \\\n 'https://www.etymonline.com/word/noxious' \\\n 'https://abadis.ir/fatofa/%D9%86%D8%B3%D8%A7/' \\\n 'https://abadis.ir/fatofa/%D8%AC%D9%86%D8%AD%D9%87/' \\\n 'https://abadis.ir/fatofa/%D9%81%D8%B1%D9%86%D8%A7%D8%B3/' \\\n 'https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B4%D8%AA%D8%B1/' ; do\n python3 tools/fetch_source.py \"$u\" --note 'pdf page 357, roots Nek 1 / Nekš: nectar/nuisance/noxious chains; Mo`in+Dehkhoda for نسا، جنحه، فرناس، نیشتر' 2>&1 | tail -1; done",
 "description": "Archive Etymonline and abadis sources"
}
```


### [2026-09-07T18:32:21.928Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f3256a34be500420.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7c454dd617c562b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5c1d25b85cd04553.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d2c945f3392ed9a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/4decc77416935eda.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e55eef991cdb303a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3cbbb073212f2683.txt
```


## [2026-09-07T18:32:26.565Z] TOOL CALL #90: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg357.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/357.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/357.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-07T18:32:26.626Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 78195 Sep  7 14:32 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/357.png
```


## [2026-09-07T18:35:06.817Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '41340,41355p' LAT.txt",
 "description": "Read Ernout-Meillet noceo"
}
```


### [2026-09-07T18:35:06.862Z] TOOL RESULT

```
tif), cf. encore Cic., Caec.ai,60, arma alia ad tegendum, alia ad
nocendum, Luc.8,305, uolnera parua nocent ("causent la mort"), et
s1 est affaibli au point de ne plus etre dans la langue courante
que "nuire [a]", le sens de "tuer" ayant £te reserve entre autres
au denominatif de nex, necare. Ancien, usuel et classique dans ce
sens. Panroman, sauf roumain, M.L.5938. nocens "qui nuit a,
coupable": innocens "incapable de nuire, innocent", et nocentia
(Tert.), reforme sans doute sur innocentia qui est classique; nocuus,
innocuus, qui se substitue dans la poesie dactylique a l*ametrique
innocens, et penbtre dans la prose imperiale; M.L. 4444 ; celt.: iri.
ennac.
Tardifs: nocibilis, nocentia, renoceo.
noxa: faute, dommage caus^; cf. la formule du f 4 tial dans T.L.9,10,9,
ob eam rem noxam nocuerunt', et Dig., 5 °>i 6,338 0 3, noxae appellatione
omne delictum continetur. Puis, a 1 'epoque imperiale, le sens de
"faute" ayant 4 t<? reserve a noxia, noxa a designe le "coupable",
```


## [2026-09-07T18:35:10.568Z] AGENT

Now I'll write the verification file.


## [2026-09-07T18:45:45.037Z] AGENT

I have all the research I need. Writing the verification file now.


## [2026-09-07T18:55:54.906Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json, io\n\nR = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ne%E1%B8%B1-\"\nW_GONAH = \"https://en.wiktionary.org/wiki/%DA%AF%D9%86%D8%A7%D9%87\"\nW_NISH = \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%B4\"\nW_JANAH = \"https://en.wiktionary.org/wiki/%D8%AC%D9%86%D8%A7%D8%AD\"\nE_NECTAR = \"https://www.etymonline.com/word/nectar\"\nE_NUIS = \"https://www.etymonline.com/word/nuisance\"\nE_NOX = \"https://www.etymonline.com/word/noxious\"\nA_NASA = \"https://abadis.ir/fatofa/%D9%86%D8%B3%D8%A7/\"\nA_JONHA = \"https://abadis.ir/fatofa/%D8%AC%D9%86%D8%AD%D9%87/\"\nA_FARNAS = \"https://abadis.ir/fatofa/%D9%81%D8%B1%D9%86%D8%A7%D8%B3/\"\nA_NISHTAR = \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%B4%D8%AA%D8%B1/\"\n\ndoc = {\n \"pdf_page\": 357,\n \"book_page\": 327,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-07\",\n \"entries\": [\n  {\n   \"entry\": 0,\n   \"root\": \"Nek 1\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"PIE *neḱ- 'to perish, disappear', causative *noḱ-éye- 'to destroy, harm' (Pokorny 762 neḱ- 'Tod, sterben; Toter')\",\n   \"note\": \"Root, language label, gloss and page reference are all defensible. Pokorny, IEW 762, lemma neḱ- (*hounḱ-), Meaning 'death, dying; dead person', References 'WP. II 326, WH. I 153 ff.' — and its Material is precisely the material of this chart: 'Old Indic nasyati, nasati \\\"gets lost, disappears, passes away\\\", nasayati \\\"makes disappear, ruin\\\" (lengthened grade compared with Latin noceo), Avestan nasyeiti \\\"disappears\\\", participle Old Indic nasta-, Avestan nasta- (= Latin e-nectus), nas- f. \\\"need, misfortune\\\" (= Latin nex, gr. νέκταρ, νέκυς), nasu- \\\"corpse, carrion\\\" (= gr. νέκυς, Latin nequ-alia) … Latin nex, necis \\\"death, murder\\\" … noceo \\\"harm\\\", noxa \\\"hurt, injury\\\"'. Watkins/AHD has 'nek-1. Death. … [Pok. nek- 762.]'. Nourai's gloss 'to destroy' is not Pokorny's headword sense (intransitive 'perish') but is exactly Klein's formulation of the base — 'I.-E. base *nek-, \\\"to destroy; to perish\\\"' (KLN pp.1058-59 s.v. noxious, and again s.v. necro-) — and it is the sense of the causative that gives Skt. nāśáyati and Lat. nocēre, so it is a fair label for the whole family. Cross-cutting remarks on this chart: (1) the Iranian spine (Av. nasu- → MP nasāy → NP نسا; OP vi-naθ- → MP wināh → NP گناه → Arab. junāḥ) is confirmed at every link by MacKenzie, Nyberg, Hübschmann, Kent, Jeffery and Mo'in, and is the strongest part of the page; (2) the Sanskrit box prints impossible forms (nâša, pra-nača) taken over from Mo'in's Persian footnote in Borhān; (3) the second Persian جناح box mixes the genuine Arabic loan جناح with جنحه, which is a different, native-Arabic word; (4) the 'death-overcoming' analysis of Greek νέκταρ is one of three competing views, and Klein — Nourai's own authority elsewhere — rejects the Indo-European etymology of νέκταρ altogether.\",\n   \"note_fa\": \"ریشهٔ هندواروپاییِ آغازینِ *neḱ- «نابود شدن، از میان رفتن؛ مرگ» است و پوکورنی در صفحهٔ ۷۶۲ فرهنگ ریشه‌شناسی خود همین ریشه را با همان داده‌های این نمودار می‌آورد: سنسکریت naśyati «گم می‌شود، از میان می‌رود» و nāśáyati «نابود می‌کند»، اوستایی nasyeiti و nasu- «لاشه»، یونانی nekrós و néktar، لاتین nex و noceō و noxa. برچسبِ «هندواروپایی» و شمارهٔ صفحه درست است؛ معنیِ «نابود کردن» که نورایی می‌دهد معنیِ ستاکِ سببی (*noḱ-éye-) است و همان تعبیری است که کلاین به‌کار می‌برد («to destroy; to perish»)، پس پذیرفتنی است هرچند معنیِ پایهٔ ریشه لازم است، نه متعدی. در مجموع ادعای نورایی درست است: ستون ایرانیِ این نمودار (اوستایی nasu- ← پهلوی nasāy ← «نسا»؛ پارسی باستان vi-naθ- ← پهلوی wināh ← «گناه» ← عربی «جناح») با مکنزی، نیبرگ، هوبشمان، کنت، جفری و حواشی معین یکسر تأیید می‌شود. سه نکتهٔ کاستی: صورت‌های سنسکریتِ جعبهٔ نخست (nâša، pra-nača) در هیچ منبعی چنین نیست، «جنحه» به این خانواده ربطی ندارد، و تحلیلِ néktar به «نوشابهٔ چیره بر مرگ» تنها یکی از سه نظرِ رقیب است.\",\n   \"sources\": [R, E_NECTAR],\n   \"ref_check\": [\n    {\"ref\": \"POK:762\", \"status\": \"supports\", \"note\": \"POK_full.txt block beginning 'Root / lemma: neR- {*hounR-} / Meaning: death, dying; dead person / … Page(s): 762' (lines 62282-62331): 'Old Indic nasyati … Avestan nasyeiti … nasu- \\\"corpse, carrion\\\" … Latin nex, necis \\\"death, murder\\\" … noceo \\\"harm\\\" … noxa \\\"hurt! injury\\\"'. Exactly the page Nourai cites and exactly the family he draws.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 762, lemma neḱ-\", \"stance\": \"supports\", \"note\": \"'Meaning: death, dying; dead person'; the whole chart's material (Skt. nasyati/nāsayati, Av. nasyeiti/nasu-, Gk. νέκυς/νεκρός/νέκταρ, Lat. nex/necāre/noceō/noxa, OIr. ec) stands under this one lemma.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 326-327\", \"stance\": \"supports\", \"note\": \"'nek- \\\"umkommen\\\", neku-s \\\"Toter, Leiche\\\". Ai. naśyati \\\"geht verloren, verschwindet, vergeht\\\", nāśáyati \\\"macht verschwinden, richtet zugrunde\\\" (dehnstufig gegenüber lat. noceo), av. nasyeiti … noceo \\\"schade\\\" … Ptc. *noxus vorausgesetzt von noxa'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nek-1\", \"stance\": \"supports\", \"note\": \"'nek-1. Death. 1. Latin nex (stem nec-), death: PERNICIOUS. 2. Latin necāre, to kill: INTERNECINE. 3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocēre … 4. Suffixed o-grade form *nok-s- in Latin noxa … 5. Suffixed full-grade form *nek-ro- in Greek nekros … 6. Greek nek-tar … [Pok. nek- 762.]'\"},\n    {\"src\": \"KLN\", \"where\": \"1966 ed. pp. 1058-59 s.v. noxious (leaf 566, which carries the printed numerals 1058/1059)\", \"stance\": \"supports\", \"note\": \"'L. noceō and nex derive fr. I.-E. base *neḱ-, \\\"to destroy; to perish\\\", whence also OI. naśyati, \\\"disappears, perishes\\\", Avestic nasyeiti, of s.m., nasu-, \\\"dead body, corpse\\\" … Gk. νέκυς, νεκρός, \\\"dead body, corpse\\\", OIr. ec, Bret. ankou … \\\"death\\\"'. This is the source of Nourai's root gloss.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 4.75 'die; dead; death' (p. 285) and 4.77 'corpse' (p. 290)\", \"stance\": \"supports\", \"note\": \"'Lat. nex \\\"violent death\\\" … : Grk. νεκρός, νέκυς, Av. nasu- \\\"corpse\\\" (4.77), Skt. naś-, Av. nas- \\\"vanish, perish\\\", Ir. éc, etc. \\\"death\\\". Walde-P. 2.326.'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. (n-section)\", \"stance\": \"silent\", \"note\": \"Mann has no *nek- 'death' lemma at the greps tried ('nek- death', 'nekus', 'neksos' return only *neks- 'bind/near/pus' lemmas); he is silent on this root.\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Sanskrit\",\n     \"words\": \"nâša; pra-nača; pra-nač\",\n     \"verdict\": \"transcription_suspect\",\n     \"derivation\": \"The Sanskrit material behind this box is genuine and is the classic witness for *neḱ-: náśyati / náśati 'is lost, disappears, perishes' (< *néḱ-ye-ti), causative nāśáyati 'makes disappear, destroys' (< *noḱ-éye-ti, lengthened grade), the ppl. naṣṭá- 'lost' and the action noun nāśá- m. 'disappearance, destruction, ruin'; with the preverb pra-: pra-naśyati 'vanishes utterly, is lost, comes to an end', whence adjectival uses 'gone, absent'. But none of the three shapes Nourai prints is a Sanskrit form. 'nâša' is the noun nāśá- given a verbal gloss ('to disappear'); 'pra-nača' and 'pra-nač' write the palatal ś as č, which no Sanskritist does — they are taken over from Mo'in's Persian footnote to Borhān-e Qāteʿ (BQT:1471, the very page Nourai cites), where the forms appear in Persian letters, and Dehkhoda quotes that same footnote as 'در هندی باستان پر + نچ، در سنسکریت پرناچه (از حاشیهٔ برهان)'. The printed page 357 shows exactly 'nâša / pra-nača / pra-nač', so the extraction is faithful and the odd letters are the book's, inherited from Borhān. The derivation itself (Skt. naś- from PIE *neḱ-) is confirmed by Pokorny 762, Walde-Pokorny II 326, Klein pp.1058-59 and Horn p.285 no.143.\",\n     \"derivation_fa\": \"مادهٔ سنسکریت در این جعبه اصیل است: naśyati «گم می‌شود، از میان می‌رود»، صورتِ سببیِ nāśáyati «نابود می‌کند»، اسمِ nāśá- «نابودی» و با پیشوندِ pra-: pra-naśyati «به‌کلی از میان می‌رود». اما هیچ‌یک از سه صورتی که نورایی چاپ کرده صورتِ سنسکریت نیست: «nâša» همان اسمِ nāśá- است که معنیِ فعلی گرفته، و «pra-nača / pra-nač» شینِ کامیِ سنسکریت را با č نوشته‌اند. سرچشمهٔ این املا حاشیهٔ معین بر برهان قاطع (همان صفحهٔ ۱۴۷۱) است که صورت‌ها را به خط فارسی «پرناچه» آورده و دهخدا هم آن را همین‌گونه نقل کرده؛ صفحهٔ چاپیِ ۳۵۷ نیز همین سه صورت را دارد، پس خطای خوانش اسکن نیست، خطای خودِ کتاب (به‌پیرویِ برهان) است. ریشه‌شناسی درست است: naś- سنسکریت از *neḱ- هندواروپایی، به گواهیِ پوکورنی ۷۶۲، والده-پوکورنی ۳۲۶/II، کلاین ۱۰۵۸-۵۹ و هرن صفحهٔ ۲۸۵ (شمارهٔ ۱۴۳).\",\n     \"error_in\": \"book\",\n     \"book_prints\": \"nâša : to disappear ; pra-nača : to be finished ; pra-nač : absent, absent minded\",\n     \"correct_form\": \"náśyati / nāśá- ; pra-naśyati ; pra-naṣṭa-\",\n     \"sources\": [R, A_FARNAS],\n     \"ref_check\": [\n      {\"ref\": \"POK:762\", \"status\": \"supports\", \"note\": \"IEW 762: 'Old Indic nasyati, nasati \\\"gets lost, disappears, passes away\\\", nasayati \\\"makes disappear, ruin\\\" (lengthened grade compared with Latin noceo) … participle Old Indic nasta- \\\"lost\\\" … lengthened grade Old Indic nasa- m. \\\"das Zunichtewerden\\\"' — the substance of the box, in correct spellings.\"},\n      {\"ref\": \"BQT:1471\", \"status\": \"partial\", \"note\": \"tools/ref_page.py BQT:1471 (v3 pdf p.264), footnote 1 to فرناس: 'هندی باستان pra-naš (غایب و ناپدید شدن)، سانسکریت pra-naś… (تمام شدن، خاموش شدن) ← اشتقاق: هوبشمان ۸۲۲'. The page supports the pra-naś- etymology but is also the source of the deformed spelling.\"},\n      {\"ref\": \"HRN:285\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 306 (printed '— 285 —'), no. 143 'nastūtan \\\"vernichten\\\" … aw. √nas-, nasyeiti \\\"verschwinden\\\", Causat. \\\"verschwinden machen\\\"; ai. √naś-, náśyati \\\"verschwinden, verderben\\\"; lat. necāre, gr. νέκυν. … vergl. auch np. fernūs (oben No. 822)'. Exactly the page Nourai cites, and it links the Sanskrit root both to Avestan and to farnās.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"WLD\", \"where\": \"Bd. II 326\", \"stance\": \"supports\", \"note\": \"'Ai. naśyati \\\"geht verloren, verschwindet, vergeht\\\", nāśáyati \\\"macht verschwinden, richtet zugrunde\\\" … Ptc. ai. naṣṭá- \\\"verlorengegangen\\\" … dehnstufig ai. nāśá- m. \\\"das Zunichtewerden\\\"'.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. p. 1059 s.v. noxious\", \"stance\": \"supports\", \"note\": \"'whence also OI. naśyati, \\\"disappears, perishes\\\"' — the same Sanskrit verb, correctly spelt.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.75 (p. 285), 4.77 (p. 290) and 11.27 (noceō article)\", \"stance\": \"supports\", \"note\": \"'Skt. naś-, Av. nas- \\\"vanish, perish\\\"'; and in the Latin article 'caus. of *nek- in Lat. nex … Skt. naś- \\\"perish\\\", caus. nāśaya-'.\"},\n      {\"src\": \"MON\", \"where\": \"Dehkhoda s.v. فرناس, quoting حاشیهٔ برهان\", \"stance\": \"partial\", \"note\": \"'فرناس. [فَ] (ص) در هندی باستان پر + نچ، در سنسکریت پرناچه. (از حاشیهٔ برهان)' — confirms that Nourai's 'pra-nača' is Mo'in's Persian-script rendering, not a Sanskritist's form.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"farnâs\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"NP فرناس farnās (Horn reads fernūs; the dictionaries also give فرنوس) 'heedless, stupid, ignorant; drowsy, half asleep' is indeed a *pra/fra + naś- formation, literally 'one whose wits are gone'. Horn, Grundriss no. 822 (p. 182 — the page Nourai cites): 'fernūs \\\"töricht, nachlässig, verschlafen; Thorheit\\\". ai. pra + √naś- \\\"verloren gehen, verschwinden\\\"', and he repeats the comparison at p. 285 no. 143 ('vergl. auch np. fernūs'). Mo'in's footnote at BQT:1471 gives the same etymology and cites Hübschmann/Horn 822; Borhān's gloss is 'بمعنی غافل و نادان … و بمعنی نیم‌خواب و خواب‌آلود'; Mo'in's own dictionary has '(فَ) (ص.) ۱- غافل، نادان. ۲- خواب‌آلود'. The word is first attested in ʿOnsori Balxi (early 11th c.), quoted from Asadi's Loghat-e Fors — the very verse the chart prints. Semantic path: 'lost, vanished' → 'absent-minded, dazed' → 'drowsy' → 'fool'. Why only 'plausible': the arrow is drawn out of the Sanskrit box, but Persian farnās cannot descend from Sanskrit. Its first element is the Iranian preverb fra- (Av./OP fra-, cognate with — not borrowed from — Skt. pra-), so the correct parent is the root itself via Old Iranian *fra-nās-. Nourai's own sources say 'compare' (vergl., قس), not 'from'.\",\n     \"derivation_fa\": \"«فرناس» (هرن آن را fernūs می‌خواند و فرهنگ‌ها «فرنوس» هم دارند) به معنیِ «غافل، نادان؛ نیم‌خواب، خواب‌آلود» است و بی‌گمان ساختی است از پیشوندِ *fra- + ریشهٔ naś- «از میان رفتن، گم شدن»، یعنی «آن‌که هوشش رفته است». هرن در شمارهٔ ۸۲۲ (همان صفحهٔ ۱۸۲) می‌نویسد: «fernūs «نابخرد، بی‌خیال، خواب‌آلود»؛ سنسکریت pra + √naś-»، و در صفحهٔ ۲۸۵ نیز همین قیاس را تکرار می‌کند؛ حاشیهٔ معین بر برهان (ص ۱۴۷۱) همان را می‌آورد. کهن‌ترین گواه، بیتِ عنصری بلخی است که در «لغت فرس» اسدی آمده و همان بیتِ نمودار است، و تحول معنایی «رفته، گم‌شده ← بی‌خبر و مدهوش ← خواب‌آلود ← نادان» است. با این همه ادعای نورایی تنها با احتیاط پذیرفتنی است: پیکان از جعبهٔ سنسکریت کشیده شده، در حالی که «فرناس» وام‌واژهٔ سنسکریت نیست و جزءِ نخستِ آن پیشوندِ ایرانیِ fra- (هم‌ریشه با pra- سنسکریت، نه برگرفته از آن) است؛ خودِ هرن و معین هم واژهٔ «قس/vergl.» به کار برده‌اند، نه «از».\",\n     \"sources\": [A_FARNAS],\n     \"ref_check\": [\n      {\"ref\": \"HRN:182\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 203, which opens with the printed page number '- 182 -': '822. fernūs \\\"töricht, nachlässig, verschlafen; Thorheit\\\". ai. pra + √naś- \\\"verloren gehen, verschwinden\\\".' Exact page, exact claim.\"},\n      {\"ref\": \"BQT:1471\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:1471 (v3 pdf p.264): headword فرناس 'بمعنی غافل و نادان … و بمعنی نیم خواب و خواب آلود'; footnote 1 gives Old Indic pra-naś-/pra-naś(yate) and refers to Horn/Hübschmann no. 822; footnote 2 prints the same ʿOnsori verse the chart quotes, 'گفت نقاش چونکه نشناسم ـ که نه دیوانه و نه فرناسم. عنصری بلخی «لغت فرس ۱۹۲»'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HRN\", \"where\": \"no. 822 (p. 182) and no. 143 (p. 285)\", \"stance\": \"supports\", \"note\": \"'ai. pra + √naś-' at p.182; at p.285 'Hierher wird np. nūsīden \\\"abmagern\\\" gehören …, vergl. auch np. fernūs (oben No. 822)' — Horn groups farnās with the nas- family but by comparison, not descent.\"},\n      {\"src\": \"BQT\", \"where\": \"p. 1471 s.v. فرناس\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote 1 as quoted above; Borhān's own gloss 'غافل و نادان … نیم خواب و خواب آلود' matches Nourai's 'dumb, crazy' loosely (Borhān's fourth sense is the Arabic فرناس 'lion', irrelevant here).\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin s.v. فرناس (via abadis.ir)\", \"stance\": \"supports\", \"note\": \"'(فَ) (ص.) ۱- غافل، نادان. ۲- خواب آلود.' Dehkhoda s.v. adds 'در هندی باستان پر + نچ، در سنسکریت پرناچه (از حاشیهٔ برهان)'.\"},\n      {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt\", \"stance\": \"silent\", \"note\": \"grep 'فرناس' and 'FARNAS' return nothing; Aryanpur's OCR yields no entry.\"}\n     ]\n    },\n    {\n     \"id\": 3,\n     \"lang\": \"Avestan\",\n     \"words\": \"nasayeti, nashta; nasu, nas 1; nasu-pâka\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All three items are real Avestan. (a) The root nas- 'to disappear, be lost' — Bartholomae, AiW 1055: 'j., g. nas- V. \\\"verschwinden\\\". Praes. nasya-, Perf. nāš-; PPP. nasta-, nəxsta-'; the 3sg. present is nasyeiti (Y. 10.7 'nasyeiti ha=ra frakərəsta', V. 19.33), so Nourai's 'nasayeti' is an inexact rendering of nasyeiti (his -ay- looks like a contamination from the causative nāsayeiti), and 'nashta' is simply his sh-spelling of the participle našta- (= Lat. e-nectus). (b) nasu-/nasav- f., m. 'corpse, carrion' of man or beast — AiW 1057: 'j. nasav- f., m. \\\"Leiche, Leichnam\\\" (von Menschen und Tieren); \\\"Leichenteil\\\"', hundreds of Vendidād attestations, and also the name of the corpse-demon druxš yā nasuš. (c) nasu-pāka- 'corpse-cooker/burner' — AiW s.v.: 'nasu-pāka- Adj. \\\"Leichen(teile) kochend\\\"', with V. 8.73 quoted in AiW under pak-: 'yaṯ … ātrəm nasu-pākəm frajasąn, nasūm hąmpacąn, nasūm hāvayąn \\\"when they come to a fire on which a corpse is being cooked\\\"' — burning or cooking a corpse being one of the capital sins of Zoroastrian law, which is exactly why the compound is lexicalised. Its second member pāka- is from PIE *pekʷ- 'to cook', Nourai's cross-reference ☞Pekw. The phonology of the whole node is regular: PIE palatal *ḱ > Proto-Iranian *ć/*s, hence Av. nas- beside Skt. naś- and OP naθ- (node 6).\",\n     \"derivation_fa\": \"هر سه مدخلِ این جعبه اوستاییِ اصیل است. یک: ریشهٔ nas- «ناپدید شدن، از میان رفتن»؛ بارتولومه در فرهنگ ایرانی باستان (ستون ۱۰۵۵) می‌آورد «nas- V. \\\"verschwinden\\\"، حالِ nasya-، اسمِ مفعولِ nasta-»، و صورتِ سومِ شخصِ مفردِ حال nasyeiti است (یسنا ۱۰/۷، وندیداد ۱۹/۳۳)؛ پس «nasayeti» نورایی خوانشِ نادقیقِ nasyeiti است (شاید به‌سببِ آمیختن با صورتِ سببیِ nāsayeiti) و «nashta» همان našta- است. دو: nasu-/nasav- «لاشه، مردار (چه انسان چه جانور)» (بارتولومه ستون ۱۰۵۷) که در وندیداد بسیار آمده و دیوِ مردار هم «دْروخشِ نَسو» خوانده می‌شود. سه: nasu-pāka- «پزندهٔ لاشه» (بارتولومه: «Leichen(teile) kochend») که در وندیداد ۸/۷۳ آمده و از گناهانِ مرگ‌ارزانِ شریعتِ زردشتی بوده است؛ جزءِ دومِ آن pāka- از ریشهٔ *pekʷ- «پختن» است، همان ارجاعِ ☞Pekw. آواشناسیِ کلِ جعبه قاعده‌مند است: کافِ کامیِ هندواروپایی (*ḱ) در ایرانی به s بدل می‌شود، از این‌رو اوستایی nas- در برابرِ سنسکریت naś- و پارسی باستان naθ-. ادعای نورایی درست است.\",\n     \"sources\": [R],\n     \"ref_check\": [\n      {\"ref\": \"POK:762\", \"status\": \"supports\", \"note\": \"IEW 762: 'Avestan nasyeiti \\\"disappears\\\", participle … Avestan nasta- ds. (= Latin e-nectus), nasišta- \\\"most perishable\\\", nas- f. \\\"need, misfortune\\\" …, nasu- \\\"corpse, carrion\\\"'.\"},\n      {\"ref\": \"KLN:1059\", \"status\": \"supports\", \"note\": \"Klein 1966 leaf 566 (printed numerals 1058/1059), s.v. noxious: 'whence also OI. naśyati … Avestic nasyeiti, of s.m., nasu-, \\\"dead body, corpse\\\"'. Nourai's page number is exact.\"},\n      {\"ref\": \"SYN:290\", \"status\": \"supports\", \"note\": \"Buck 4.77 CORPSE, printed p. 290 (SYN.txt leaf 329, with the numeral 291 on the following leaf): 'Grk. νεκρός, νέκυς, Av. nasu- : Skt. naś-, Av. nas- \\\"perish, vanish\\\", Lat. nex \\\"violent death\\\", etc. Walde-P. 2.326'; the same page's list gives 'Av. nasu-, kahrp' for 'corpse'.\"},\n      {\"ref\": \"KNT:192\", \"status\": \"supports\", \"note\": \"Kent's Lexicon s.v. naθ- (leaf 216, running head 'LEXICON', printed p.192-93): 'naθ- vb. \\\"perish\\\", causative \\\"injure; destroy\\\": Av. (nas-), Skt. naś-, Gk. νέκυς \\\"corpse\\\", Lat. acc. nec-em \\\"destruction\\\", nocet \\\"harms\\\", pIE *nek-'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BRT\", \"where\": \"AiW 1055 (nas-), 1057 (nasav-), s.v. nasu-pāka-, and 1615 under pak-\", \"stance\": \"supports\", \"note\": \"'j., g. nas- V. \\\"verschwinden\\\" … PPP. nasta-'; 'j. nasav- f., m. \\\"Leiche, Leichnam\\\" (von Menschen und Tieren)'; 'nasu-pāka- Adj. \\\"Leichen(teile) kochend\\\"'; under pak-: 'ātrəm nasu-pākəm … \\\"ein Feuer, womit man eine Leiche kocht\\\"' (V. 8.73).\"},\n      {\"src\": \"KNT\", \"where\": \"Old Persian Lexicon s.v. naθ- (pp. 192-93)\", \"stance\": \"supports\", \"note\": \"Kent equates OP naθ- with 'Av. (nas-), Skt. naś-' under pIE *nek-, exactly the Avestan-box claim.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 142-143 (p. 285)\", \"stance\": \"supports\", \"note\": \"'142. nasīh \\\"Leichnam, Aas\\\". aw. nasu- \\\"Leichnam, Aas\\\"'; '143. nastūtan \\\"vernichten\\\" … aw. √nas-, nasyeiti \\\"verschwinden\\\", Causat. \\\"verschwinden machen\\\"'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 4.77 (p. 290) and 12.44 'bury' (p. 292, on nasu-spaya-)\", \"stance\": \"supports\", \"note\": \"'Av. nasu-spaya-, nasu-spā- \\\"burial, burier of corpses\\\", cpds. of nasu- \\\"corpse\\\" (4.77) … These words occur only with reference to a sin, a violation of the prescribed Zoroastrian practice of exposing the corpse. Barth. 1059 f., 1615.' — the same lexical family as nasu-pāka-.\"}\n     ]\n    },\n    {\n     \"id\": 4,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"nasâ, nasây\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Middle Persian nasā(y), written ⟨nsʾy⟩ in Book Pahlavi and ⟨nsʾh⟩ in Manichaean script, 'corpse, carrion'. MacKenzie, CPD p. 57: 'nasā [nsʾy | M n(y)sʾh, N ~] corpse, carrion'. Nyberg, Manual II p. 137: 'nasāi [nsʾy] corpse 60.21, 72.7, 94.25 — Av. (1057) nasu-, acc. nasāum, pl. nom. nasāvē; MPrth nsʾw; MPrs nsʾh (A-H I); NP nasā \\\"dead\\\"'. The shape is regular: the Avestan u-stem nasu- was replaced in Middle Iranian by a stem built on the strong oblique nasāv- (acc. nasāum, nom. pl. nasāvē), giving *nasāw > MP nasāy/nasā; Parthian keeps ⟨nsʾw⟩. Mo'in makes the same point in his footnote to Borhān p. 2136: 'در اوستا nasu … «نسو» در تفسیر پهلوی به nasāy گردانیده شده'. The word is a technical term of Zoroastrian purity law, whence the surviving compound nasā-sālār 'corpse-bearer' (the man who carries the dead into the dakhma).\",\n     \"derivation_fa\": \"فارسی میانه nasā(y) (به خطِ پهلویِ کتابی ⟨nsʾy⟩ و به خطِ مانوی ⟨nsʾh⟩) به معنیِ «لاشه، مردار». مکنزی در «فرهنگ کوچک پهلوی» ص ۵۷ می‌آورد: «nasā [nsʾy | مانوی n(y)sʾh، فارسی نو همان] corpse, carrion»، و نیبرگ در بخشِ واژه‌نامهٔ «راهنمای پهلوی» ص ۱۳۷: «nasāi [nsʾy] لاشه … اوستایی nasu-، مفعولیِ nasāum، جمعِ فاعلیِ nasāvē؛ پارتی nsʾw؛ فارسی نو نسا». دگرگونی قاعده‌مند است: ستاکِ u-پایانِ اوستایی nasu- در ایرانیِ میانه جای خود را به ستاکی داد که بر پایهٔ صورت‌های غیرفاعلیِ nasāv- ساخته شده بود، یعنی *nasāw > nasāy/nasā. معین نیز در حاشیهٔ برهان (ص ۲۱۳۶) همین را می‌گوید: «نسو در تفسیر پهلوی به nasāy گردانیده شده». این واژه اصطلاحِ شریعتِ پاکیِ زردشتی است و ترکیبِ «نساسالار» از آن مانده است. ادعای نورایی درست است.\",\n     \"sources\": [A_NASA],\n     \"ref_check\": [\n      {\"ref\": \"SNS:272\", \"status\": \"supports\", \"note\": \"SNS_pages.txt leaf 154 carries the glossary headword 'nasay/nasā' (with sub-entries 'nasay nigānīh', 'nasay xwardan' and a Manichaean reference '(Mir. Man. III, 58) nsʾw'). The scan holds two printed pages per leaf, so printed p. 272 = 2×154 − 36, and the same arithmetic puts vināh (Nourai's SNS:282) on leaf 159, where it duly stands — the two citations calibrate each other. Persian OCR of the leaf is poor, but the Latin headwords are legible.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 57\", \"stance\": \"supports\", \"note\": \"'nasā [nsʾy | M n(y)sʾh, N ~] corpse, carrion'; the same page has nasrušt(īh) 'pollution, corruption'.\"},\n      {\"src\": \"NYB\", \"where\": \"Nyberg, Manual II, Glossary p. 137 s.v. nasāi\", \"stance\": \"supports\", \"note\": \"'nasāi [nsʾy] corpse … — Av. (1057) nasu-, acc. nasāum, pl. nom. nasāvē; MPrth nsʾw; MPrs nsʾh (A-H I); NP nasā \\\"dead\\\"'.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW 1057\", \"stance\": \"supports\", \"note\": \"the oblique forms nasāum, nasāvō that the Middle Persian stem is built on are listed here.\"},\n      {\"src\": \"BQT\", \"where\": \"p. 2136, Mo'in's footnote 4 to نسا\", \"stance\": \"supports\", \"note\": \"'«سو» در تفسیر پهلوی به nasāy گردانیده شده و هنوز هم این کلمه در ادبیات زرتشتیان به شکل «نسا» باقی است و «نساسالار» کسی است که مرده را از در دخمه به درون دخمه می‌گذارد'.\"}\n     ]\n    },\n    {\n     \"id\": 5,\n     \"lang\": \"Persian\",\n     \"words\": \"nasâ\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP نَسا nasā 'corpse, carrion; putrefaction' continues MP nasāy directly, with loss of the final glide (nasāy > nasā); no other change is needed. MacKenzie flags the survival with 'N ~' and Nyberg with 'NP nasā'. It is not a general word of literary Persian but a survival in Zoroastrian and Pahlavi-derived writing, which is exactly what Horn observed at the page Nourai uses for the Sanskrit box: 'np. nesā, visā kommt nur in Parsenschriften vor (Citate aus Behrām Zerātust)' (HRN p. 285 no. 142) — hence the chart's illustrative couplet from the Zartošt-nāma. Mo'in's dictionary tags it Pahlavi and glosses it exactly as the chart does: '(نَ) [په.] (اِ.) لاشه، مردار'; Dehkhoda s.v. gives 'گوشت و استخوان مرده را گویند' and extends it to anything rotten, which covers Nourai's second gloss 'corruption'.\",\n     \"derivation_fa\": \"«نَسا» در فارسی نو دنبالهٔ مستقیمِ nasāy فارسی میانه است و تنها تغییرِ آن افتادنِ «ی» پایانی است (nasāy > nasā). مکنزی با نشانهٔ «N ~» و نیبرگ با «NP nasā» بازماندنِ آن را در فارسیِ نو ثبت کرده‌اند. این واژه از واژگانِ رایجِ ادبِ فارسی نیست، بلکه در نوشته‌های زردشتی و متونِ برگرفته از پهلوی مانده است؛ هرن در همان صفحهٔ ۲۸۵ می‌نویسد «np. nesā، visā تنها در نوشته‌های پارسیان (نقل از بهرام زرتشت) دیده می‌شود» — و از همین‌رو نمودار بیتی از «زرتشت‌نامه» را شاهد آورده است. فرهنگ معین آن را «[په.] لاشه، مردار» می‌آورد و دهخدا «گوشت و استخوان مرده» و سپس هر چیزِ گندیده، که معنیِ دومِ نورایی («فساد») را نیز می‌پوشاند. ادعای نورایی درست است.\",\n     \"sources\": [A_NASA],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2136\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:2136 (v4 pdf p.219), footnote 4: 'در اوستا nasu بمعنی لاشه و مردار و آنچه فاسد و گندیده شده باشد خواه از انسان و خواه از جانور … «سو» در تفسیر پهلوی به nasāy گردانیده شده و هنوز هم این کلمه در ادبیات زرتشتیان به شکل «نسا» باقی است … رک: پورداود، یشتها ۱ ص ۱۵۳ ح ۱' — the full Avestan → Pahlavi → New Persian chain the chart draws, on exactly the cited page.\"},\n      {\"ref\": \"MON:4714\", \"status\": \"partial\", \"note\": \"the content is right — Farhang-e Moʿin s.v. نسا reads '(نَ) [په.] (اِ.) لاشه، مردار' (abadis.ir) — but the page number could not be checked: only the 2-volume Adena reprint is on disk (different pagination) and vajehyab/abadis print no page numbers. Note that p.4714 falls in Mo'in's later volumes, where نسا is also the place-name Nasā (see BQT:2136 n.5, OP nisāya-), so the citation may point at the wrong نسا.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"CPD p. 57\", \"stance\": \"supports\", \"note\": \"'nasā [nsʾy | M n(y)sʾh, N ~]' — the 'N ~' marks New Persian nasā as identical in form.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual II p. 137\", \"stance\": \"supports\", \"note\": \"'NP nasā \\\"dead\\\"'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 142 (p. 285)\", \"stance\": \"supports\", \"note\": \"'np. nesā, visā kommt nur in Parsenschriften vor (Citate aus Behrām Zerātust)' — confirms the word and its restricted Zoroastrian usage.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin and Dehkhoda s.v. نسا (abadis.ir)\", \"stance\": \"supports\", \"note\": \"Moʿin '(نَ) [په.] (اِ.) لاشه، مردار'; Dehkhoda 'گوشت و استخوان مرده را گویند', with Avestan/Pahlavi origin and an extension to 'decayed and putrid'.\"}\n     ]\n    },\n    {\n     \"id\": 6,\n     \"lang\": \"Old Persian\",\n     \"words\": \"nath; vi-nath\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Old Persian naθ- 'to perish', causative 'to injure, destroy' — Kent, Old Persian, Lexicon s.v. (printed pp. 192-93, the exact pages Nourai cites): 'naθ- vb. \\\"perish\\\", causative (§123.2, §215) \\\"injure; destroy\\\": Av. (nas-), Skt. naś-, Gk. νέκυς \\\"corpse\\\", Lat. acc. nec-em \\\"destruction\\\", nocet \\\"harms\\\", pIE *nek- (§87)'; and immediately under it 'vi- + naθ- caus. \\\"injure, harm\\\": vināθayatiy DNb 17f., viyanaθaya (imperfect) DB 4.66, vināθayāntiy A²Sa 5, vināθayaiš (optative) DNb 20, 21, vinastahyā (gen. of the past passive participle used as a noun) DNb 18'. The simple verb is not attested by itself in the inscriptions — Kent lemmatises it from the prefixed forms — so Nourai's bare 'nath' is a root-entry, not a text form. The phonology is the diagnostic one: PIE palatal *ḱ gives Old Persian θ where Avestan has s and Sanskrit ś (cf. Skt. śata-, Av. sata-, OP θata- in θatagu-), so OP naθ- : Av. nas- : Skt. naś- is a regular triplet, and it is the θ of the Persid dialect that produces the -h- of Middle Persian wināh and New Persian گناه (nodes 7-8). '☞Wi' is the preverb vi- 'apart, away, asunder' (OP viy-/vi-, Av. vī-, Skt. vi-), whence the sense 'un-do'.\",\n     \"derivation_fa\": \"پارسی باستان naθ- «نابود شدن» و در ساختِ سببی «آسیب رساندن، تباه کردن»؛ کنت در واژه‌نامهٔ «پارسی باستان» (همان صفحه‌های ۱۹۲ و ۱۹۳) می‌آورد: «naθ- «نابود شدن»، سببی «آسیب زدن؛ نابود کردن»: اوستایی nas-، سنسکریت naś-، یونانی nekus «لاشه»، لاتین necem «نابودی» و nocet «آسیب می‌زند»، هندواروپاییِ *nek-»، و بی‌درنگ زیرِ آن: «vi- + naθ- سببی «آسیب زدن»: vināθayatiy در کتیبهٔ داریوش نقش‌رستم (DNb ۱۷)، viyanaθaya در بیستون ۴/۶۶، vināθayaiš در DNb ۲۰-۲۱ و vinastahyā در DNb ۱۸». صورتِ ساده در کتیبه‌ها به‌تنهایی گواه ندارد و کنت آن را از صورت‌های پیشوندی بازسازی کرده، پس «nath» نورایی مدخلِ ریشه است نه صورتِ متنی. آواشناسی اینجا کلیدی است: کافِ کامیِ هندواروپایی در پارسی باستان θ می‌دهد، جایی که اوستایی s و سنسکریت ś دارد (قس سنسکریت śata-، اوستایی sata-، پارسی باستان θata-)؛ همین θ است که در فارسی میانه به h بدل شده و «وناه/گناه» را ساخته است. «☞Wi» همان پیشوندِ vi- «جدا، وا-» است. ادعای نورایی درست است.\",\n     \"sources\": [W_GONAH],\n     \"ref_check\": [\n      {\"ref\": \"KNT:192,193\", \"status\": \"supports\", \"note\": \"KNT.txt leaf 216 (running head 'LEXICON'; the numeral 188 on leaf 211 fixes the offset, so this leaf is printed pp. 192-93): 'naθ- vb. \\\"perish\\\", causative \\\"injure; destroy\\\": Av. (nas-), Skt. naś-, Gk. νέκυς \\\"corpse\\\", Lat. acc. nec-em \\\"destruction\\\", nocet \\\"harms\\\", pIE *nek-' and 'vi- + naθ- caus. \\\"injure, harm\\\": vināθayatiy DNb 17f. …'. Both of Nourai's words, on both of his pages.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KNT\", \"where\": \"Lexicon pp. 192-93 and the pIE-root list at p. 44\", \"stance\": \"supports\", \"note\": \"in the grammar's root list Kent writes '*nek- \\\"perish\\\", in vi-nas-ta- \\\"damage\\\", (Ar.) *nāš- in viy-anāθaya \\\"he injured\\\"'.\"},\n      {\"src\": \"BRT\", \"where\": \"AiW 1055-56 (nas-, vi-nas-)\", \"stance\": \"supports\", \"note\": \"Bartholomae lists the same prefixed formation in Avestan; Nyberg quotes him for it: 'Av. (1055) nas- \\\"to disappear, to be lost\\\", (1056) vi-nas- \\\"to be subject to destruction\\\"'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §100, pp. 212-13\", \"stance\": \"supports\", \"note\": \"Hübschmann reconstructs precisely this Old Persian ancestor: 'Ist arm. vnas auf ein ap. *vinasa- (neben *vinaθa- = paz. np. gunāh; g. venāh) zurückzuführen?'\"}\n     ]\n    },\n    {\n     \"id\": 7,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"vinâs, vinâh, gunâh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"The Middle Persian word is a nominal *wi-nāθa- 'undoing, destruction, sin' from vi- + the lengthened grade of naθ-/nas-, the exact counterpart of Sanskrit vi-nāśá- 'destruction'. Book Pahlavi writes it ⟨wnʾs⟩, with the historical ⟨s⟩ that stands for -h-; MacKenzie therefore reads it wināh — 'wināh [wnʾs | M wynʾh, N gunāh] sin, crime' (CPD p. 90), and Manichaean Middle Persian, which spells phonetically, has wynʾh. Nyberg reads the same graph vinās and explains why both of Nourai's forms are legitimate: 'vinās [wnʾs] sin, passim … — NW form, Arm. lw. vnas; MPrs w(y)nʾh (S, A-H I); Paz. NP gunāh; Arab. lw. junāh-' (Manual II p. 263, the page Mo'in cites). So -s is the North-West (Parthian/Median) reflex — whence the Old Armenian loan վնաս vnas 'harm, loss, guilt' of the 5th century — and -h the South-West (Persid) reflex of the same Old Iranian *-θ-, precisely the dialect split Hübschmann set out at Persische Studien §100 (pp. 212-13): 'gunāh \\\"Sünde\\\" = pāz. gunāh Shk. 247, phl. v(i)nāθ … liegt s vor in vnas … gegenüber pāz. np. gunāh, arab. junāḥ (Koran), phl. v(i)nāθ'. The third form in Nourai's box, 'gunâh', is not Book Pahlavi at all: it is the Pāzand/New Persian shape (Pāz. gunāh, Shikand Gloss. 247), so the box telescopes late Pahlavi and Pāzand into one line.\",\n     \"derivation_fa\": \"واژهٔ فارسی میانه اسمی است از ساختِ *wi-nāθa- «تباهی، نابودی، گناه»، از پیشوندِ vi- و ستاکِ کشیدهٔ naθ-/nas-، و برابرِ دقیقِ vi-nāśá- سنسکریت («انقراض، زوال»). در پهلویِ کتابی ⟨wnʾs⟩ نوشته می‌شود، با «س»ِ تاریخی که در تلفظ h است؛ از این‌رو مکنزی آن را wināh می‌خواند: «wināh [wnʾs | مانوی wynʾh، فارسی نو گناه] گناه، جرم» (ص ۹۰)، و پهلویِ مانوی که آوانگارانه می‌نویسد wynʾh دارد. نیبرگ همان نویسه را vinās می‌خواند و سببِ درستیِ هر دو صورتِ نورایی را روشن می‌کند: «vinās [wnʾs] گناه … صورتِ شمال‌غربی؛ وام‌واژهٔ ارمنی vnas؛ فارسی میانهٔ جنوب‌غربی w(y)nʾh؛ پازند و فارسی نو گناه؛ وام‌واژهٔ عربی junāh-» (ص ۲۶۳، همان صفحه‌ای که معین به آن ارجاع می‌دهد). پس -s بازتابِ شمال‌غربی (پارتی/مادی) و -h بازتابِ جنوب‌غربی (پارسی) از همان *-θ- ایرانی باستان است؛ هوبشمان در بندِ ۱۰۰ «پژوهش‌های فارسی» (ص ۲۱۲-۲۱۳) همین تقسیمِ گویشی را نشان داده است. سومین صورتِ جعبه، «gunâh»، در حقیقت پهلوی نیست بلکه صورتِ پازند و فارسی نو است. ادعای نورایی درست است.\",\n     \"sources\": [W_GONAH],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1836\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:1836 (v3 pdf p.633), Mo'in's footnote to گناه: 'گناه ـ پهلوی wināh (گناه، خراب کردن)، ایرانی باستان *vi-nāθa- (سانسکریت vi-nāśa- [انقراض، زوال])، ارمنی vnas از vinās، شکل جنوب غربی *vi-nāθana-؛ معرّب آن جناح «نیبرگ ص ۲۶۳»، کردی gunāh، بلوچی gunās' — Nourai's Pahlavi box, its Old Iranian ancestor and its Arabic offshoot, all on the cited page.\"},\n      {\"ref\": \"SNS:282\", \"status\": \"supports\", \"note\": \"SNS_pages.txt leaf 159 (= printed p. 282 on the two-pages-per-leaf mapping calibrated by SNS:272, node 4) carries the vināh entries of Tavoosi's Šāyast-nē-šāyast glossary: 'vinah', 'vinahtar', 'vinahtarīh', 'vinah kartar', 'vinah vižārdan'. Persian OCR of the leaf is poor; the Latin headwords are legible.\"},\n      {\"ref\": \"MAG:186\", \"status\": \"not_checked\", \"note\": \"Widengren, Muhammad the Apostle of God (Uppsala 1955), ch. VIII: archive.org has it lending-only (muhammadapostled0000geow), HathiTrust search-only, Google Books snippet — no accessible copy. The identical claim is however in Nyberg p. 263 (which Mo'in cites for it) and in Jeffery FVQ pp. 102-103.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 90\", \"stance\": \"supports\", \"note\": \"'wināh [wnʾs | M wynʾh, N gunāh] sin, crime', with winahgar 'sinner', wināhīdan 'spoil, damage, destroy'; also 'a-wināh [ʾwnʾs] innocent'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual II p. 263 s.v. vinās (index entries 'w(y)nʾh: vinās', 'gunāh: vinās')\", \"stance\": \"supports\", \"note\": \"'vinās [wnʾs] sin, passim … — NW form, Arm. lw. vnas; MPrs w(y)nʾh (S, A-H I); Paz. NP gunāh; Arab. lw. junāh-'; and s.v. vinasītan 'Av. (1055) nas- \\\"to disappear, to be lost\\\", (1056) vi-nas- \\\"to be subject to destruction\\\"'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §100, pp. 212-13\", \"stance\": \"supports\", \"note\": \"'gunāh \\\"Sünde\\\" = pāz. gunāh Shk. 247, phl. v(i)nāθ Gl. and Ind. 247'; and the s/h dialect doublet with 'arab. junāḥ (Koran)'.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 102-103 s.v. جناح\", \"stance\": \"supports\", \"note\": \"'it is the Pers. گناه through the Pazend gunāh (Shikand, Glossary, 247) from Phlv. ⟨wnʾs⟩ vinās \\\"a crime or sin\\\" (as is obvious from the Arm. վնաս = ἁμάρτημα in the old Bible translation) … which is related to Skt. vināśa and is quite a good Indo-European word. In Phlv. the word is used technically just as in the Qurʾān'.\"}\n     ]\n    },\n    {\n     \"id\": 8,\n     \"lang\": \"Persian\",\n     \"words\": \"gonâh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP گناه gonāh 'sin' is MP wināh with two regular New Persian developments: initial wi- becomes gu- (Hübschmann, PS §98: '…es vi vor n (+ Vokal?) zu gu macht, daher gunāh \\\"Sünde\\\"'; the same change gives wirēxtan > gorīxtan 'flee', wisistan > gosistan 'break', winjišk > gonjišk 'sparrow', all listed side by side in MacKenzie's entries), and the inherited intervocalic -h- (< OP -θ-) is kept, exactly as in the parallel set nigāh (< phl. nikāθ), agāh (< phl. akāθ), panjāh (< OP *panθasat-), padafrāh (< phl. pātafrāθ) that Hübschmann assembles on p. 212. Mo'in's footnote at BQT:1836 gives the whole line — 'پهلوی wināh، ایرانی باستان *vi-nāθa- … کردی gunāh، بلوچی gunās' — and Wiktionary states the same: from Middle Persian wynʾh (wināh), from Proto-Iranian *vi- + *nas-, from PIE *neḱ-, with cognates Old Armenian վնաս, Old Georgian უნასი, Balochi gināsk, Northern Kurdish binas, Sanskrit विनाश, and descendants Turkish günah, Tajik гуноҳ, Hindustani گُناہ.\",\n     \"derivation_fa\": \"«گناه» همان wināh فارسی میانه است با دو دگرگونیِ قاعده‌مندِ فارسی نو: نخست، آغازِ wi- به gu- بدل شده — هوبشمان در بندِ ۹۸ می‌نویسد «vi پیش از n به gu بدل می‌شود، از این‌رو gunāh»؛ همین ابدال در «گریختن» (wirēxtan)، «گسستن» (wisistan) و «گنجشک» (winjišk) هم دیده می‌شود — و دوم، «ه»ِ میانِ دو واکه که بازماندهٔ θ پارسی باستان است بر جای مانده، درست مانندِ «نگاه» (پهلوی nikāθ)، «آگاه» (akāθ)، «پنجاه» (پارسی باستان *panθasat-) و «پادافراه» که هوبشمان در صفحهٔ ۲۱۲ در یک ردیف آورده است. حاشیهٔ معین بر برهان (ص ۱۸۳۶) همین زنجیره را دارد: «پهلوی wināh، ایرانی باستان *vi-nāθa- … کردی gunāh، بلوچی gunās»، و ویکی‌واژه نیز همان را می‌گوید و هم‌ریشه‌هایش را ارمنیِ کهن vnas، بلوچی gināsk، کردی binas و سنسکریت vināśa می‌شمارد. ادعای نورایی درست است.\",\n     \"sources\": [W_GONAH],\n     \"ref_check\": [\n      {\"ref\": \"BQT:1836\", \"status\": \"supports\", \"note\": \"Mo'in's footnote s.v. گناه, quoted in full at node 7: 'گناه ـ بضم اول. پهلوی wināh (گناه، خراب کردن)، ایرانی باستان *vi-nāθa- … معرّب آن جناح «نیبرگ ص ۲۶۳»، کردی gunāh، بلوچی gunās … بزه، جرم، خطا، معصیت، اثم، تقصیر'.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"PHD\", \"where\": \"CPD p. 90\", \"stance\": \"supports\", \"note\": \"'wināh [wnʾs | M wynʾh, N gunāh]' — MacKenzie's 'N gunāh' is the derivation itself.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien §98 and §100, pp. 208-213\", \"stance\": \"supports\", \"note\": \"'…es vi vor n (+ Vokal?) zu gu macht, daher gunāh \\\"Sünde\\\"'; 'gunāh \\\"Sünde\\\" = pāz. gunāh Shk. 247, phl. v(i)nāθ'; footnote on Balochi gunās: 'Man hat für iran. *vinasa- = ap. *vinaθa- im Bal. *ginas zu erwarten, das vielleicht durch das entlehnte np. gunāh zu gunās geworden ist'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual II p. 263\", \"stance\": \"supports\", \"note\": \"'Paz. NP gunāh'.\"},\n      {\"src\": \"MON\", \"where\": \"Wiktionary s.v. گناه (which cites Hasandust and MacKenzie)\", \"stance\": \"supports\", \"note\": \"'From Middle Persian wynʾh (wināh) … Proto-Iranian preverb *vi- + root *nas- \\\"to disappear; to perish\\\", from PIE *neḱ-'; cognates Old Armenian վնաս, Balochi gināsk, N. Kurdish binas, Sanskrit विनाश.\"}\n     ]\n    },\n    {\n     \"id\": 9,\n     \"lang\": \"Arabic\",\n     \"words\": \"jonâh\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Arabic جُنَاح junāḥ 'sin, wrong, crime' — a Qurʾānic word (v. 94; xxxiii. 5, 51 and some twenty-two places in all, always late Medinan, chiefly in the formula لا جُناح عليه 'there is no sin upon him') — is a pre-Islamic borrowing of the Middle Persian word. Jeffery, Foreign Vocabulary of the Qurʾān pp. 102-103, s.v.: 'Sin, wrong, crime. A favourite Madina word … The Lexicons give no satisfactory explanation of the word, though they apparently treat it as a genuine Arabic formation. As Hübschmann showed in 1895 in his Persische Studien, 162, 212, it is the Pers. گناه through the Pazend gunāh from Phlv. ⟨wnʾs⟩ vinās \\\"a crime or sin\\\" … The word was borrowed in the pre-Islamic period and occurs in the old poetry, e.g. in the Muʿallaqa of al-Ḥārith, 70, etc., and was doubtless adopted directly into Arabic from the spoken Persian of the period, for the word is not found in Syriac.' Nyberg states it as a fact in his glossary ('Arab. lw. junāh-'), Mo'in gives 'معرّب آن جناح' citing Nyberg 263, and Wiktionary's Etymology 2 of جناح is simply 'Borrowed from Middle Persian; compare modern Persian گناه'. Mechanics of the loan: MP wināh was heard with initial g/gu (whence Arabic ج, the regular substitute for Persian g), and the final -h was rendered by ح; the resulting shape fitted the Arabic fuʿāl noun pattern, which let the lexicographers attach it secondarily to the native root ج‌ن‌ح janaḥa 'to lean, incline (away from the right course)' — a folk etymology, and the homonymous جَناح 'wing' is a genuinely different Arabic word (Wiktionary's Etymology 1, 'Uncertain; no Semitic cognates … not suspected to be borrowed from Arabic').\",\n     \"derivation_fa\": \"«جُناح» عربی به معنیِ «گناه، بزه» — واژه‌ای قرآنی که نزدیک به بیست‌ودو بار و همه در سوره‌های مدنیِ متأخر آمده، بیشتر در ترکیبِ «لا جُناحَ علیه» — وام‌واژه‌ای است پیش‌از‌اسلام از فارسی میانه. جفری در «واژه‌های دخیل در قرآن» (ص ۱۰۲-۱۰۳) می‌نویسد: «فرهنگ‌های عربی توضیحِ درستی برای این واژه ندارند و آن را ساختی عربی می‌انگارند؛ اما چنان‌که هوبشمان در ۱۸۹۵ در «پژوهش‌های فارسی» (ص ۱۶۲ و ۲۱۲) نشان داد، همان «گناه» فارسی است، از راهِ پازندِ gunāh و از پهلویِ ⟨wnʾs⟩ vinās … این واژه در دورهٔ پیش از اسلام وام گرفته شده و در شعرِ کهن، مثلاً در معلقهٔ حارث بیتِ ۷۰، آمده است و بی‌گمان یکسر از فارسیِ گفتاریِ آن روزگار به عربی راه یافته، چون در سریانی نشانی از آن نیست». نیبرگ نیز آن را «وام‌واژهٔ عربی junāh-» می‌خواند، معین «معرّب آن جناح» می‌نویسد و به نیبرگ ص ۲۶۳ ارجاع می‌دهد، و ویکی‌واژه در ریشه‌شناسیِ دومِ «جناح» می‌گوید «وام‌گرفته از فارسی میانه؛ قس فارسیِ گناه». سازوکارِ وام‌گیری: گافِ فارسی به جیم بدل شده (ابدالِ همیشگیِ g فارسی در معرَّبات) و «ه»ِ پایانی به «ح»؛ صورتِ حاصل در قالبِ «فُعال» جا افتاد و همین سبب شد که لغویانِ عرب آن را به ریشهٔ بومیِ «ج‌ن‌ح» (جَنَحَ «میل کردن، کج شدن») ببندند که ریشه‌شناسیِ عامیانه است. «جَناحِ» هم‌نگاشت به معنیِ «بال» واژهٔ دیگری است و ربطی به این ندارد. ادعای نورایی درست است.\",\n     \"sources\": [W_JANAH, W_GONAH],\n     \"ref_check\": [\n      {\"ref\": \"VDQ:38\", \"status\": \"supports\", \"note\": \"VDQ is Badre'i's Persian translation of Jeffery, and the noorlib viewer is JavaScript-only (WebFetch/curl get the site chrome), so — as refs_online.json advises — I verified the substance in the original FVQ, same entry: FVQ_pages.txt leaves 120-121 = printed pp. 102-103, 'جُناح (Junāḥ) … Sin, wrong, crime … it is the Pers. گناه through the Pazend gunāh from Phlv. ⟨wnʾs⟩ vinās … borrowed in the pre-Islamic period'. The claim of Nourai's arrow is exactly what the entry says.\"},\n      {\"ref\": \"MAG:186\", \"status\": \"not_checked\", \"note\": \"Widengren 1955 is lending-only on archive.org and search-only on HathiTrust; no accessible copy. Its claim is independently attested by Jeffery, Hübschmann and Nyberg.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 102-103 s.v. جناح\", \"stance\": \"supports\", \"note\": \"quoted above, with the notes 'Vollers hesitatingly accepts this in ZDMG, 1, 689 … and it is given as a Persian borrowing by Addi Sher, 45' and 'Hübschmann, Arm. Gramm. i, 248'.\"},\n      {\"src\": \"NYB\", \"where\": \"Manual II p. 263 s.v. vinās\", \"stance\": \"supports\", \"note\": \"'Arab. lw. junāh-'.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 212\", \"stance\": \"supports\", \"note\": \"'gegenüber paz. np. gunāh, arab. junāḥ (Koran), phl. v(i)nāθ' — the Arabic form listed as the loan of the Persian word.\"},\n      {\"src\": \"KLN\", \"where\": \"KLN_1966.txt, greps 'junah', 'gunah'\", \"stance\": \"silent\", \"note\": \"Klein has no entry for the Arabic word (it produced no English derivative).\"},\n      {\"src\": \"AFM\", \"where\": \"AFM_pages.txt, greps 'جناح' and 'گناه'\", \"stance\": \"silent\", \"note\": \"no legible hit; the Arabic/Syriac OCR of Addi Shir is too corrupt for this shape. Jeffery FVQ p.103 n.1 records that 'it is given as a Persian borrowing by Addi Sher, 45'.\"},\n      {\"src\": \"PLA\", \"where\": \"incoming/PLA/PLA_pages.txt, greps 'جناح', 'gunāh', 'wināh'\", \"stance\": \"silent\", \"note\": \"no hit in the OCR of Asbaghi's Persische Lehnwörter im Arabischen.\"},\n      {\"src\": \"LKT\", \"where\": \"LKT.txt, greps 'gunah', 'dschunah', 'junah'\", \"stance\": \"silent\", \"note\": \"Lokotsch has no entry — the word produced no European loan.\"}\n     ]\n    },\n    {\n     \"id\": 10,\n     \"lang\": \"Persian\",\n     \"words\": \"jonâh\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"The first form in this box is right: Persian جناح jonāh 'sin' is the Arabic junāḥ taken back into Persian as a learned, Qurʾānic word (used in tafsīr and fiqh), so گناه ~ جناح is a genuine Persian → Arabic → Persian round trip and a doublet of the inherited word — the sort of loop Nourai's chart is designed to show. The second form, جنحه jonha, does not belong to the chain. Mo'in glosses it '(جُ حِ) [ع.] (اِ.) گناه، بزه کوچک' — 'sin, minor offence' — and tags it merely as Arabic; Dehkhoda is blunter: 'جنحة. [جِ حَ] (ع اِ) اِثْم (محیط المحیط). گناه، و این لغتی است عامیانه و در هیچ یک از لغت‌نامه‌های معتبر نیست.' جنحه is in fact the modern juridical Arabic junḥa 'misdemeanour', a regular fuʿla noun from the native root ج‌ن‌ح janaḥa 'to lean, incline' (the same root as جَناح 'wing' and جانِح 'inclining'), coined for the middle tier of offences (جنایت / جنحه / خلاف) in nineteenth-century penal codes on the model of French délit; it is not the Qurʾānic junāḥ. The two have been contaminated in Persian usage because they look and mean alike, and Nourai's parenthesis repeats that contamination.\",\n     \"derivation_fa\": \"صورتِ نخستِ این جعبه درست است: «جناحِ» فارسی همان «جُناحِ» عربی است که دوباره — این بار به‌عنوان واژه‌ای قرآنی و اهلِ تفسیر و فقه — به فارسی بازگشته؛ پس «گناه ← جناح» یک رفت‌وبرگشتِ فارسی ← عربی ← فارسی و دوگانه‌ای (doublet) در برابرِ واژهٔ میراثی است، و همین‌گونه حلقه‌ها موضوعِ اصلیِ نمودارهای نورایی است. اما صورتِ دومِ جعبه، «جنحه»، به این زنجیره تعلق ندارد. معین آن را «(جُ حِ) [ع.] (اِ.) گناه، بزه کوچک» می‌آورد و تنها برچسبِ عربی می‌زند، و دهخدا صریح‌تر است: «جنحة … گناه، و این لغتی است عامیانه و در هیچ یک از لغت‌نامه‌های معتبر نیست». «جنحه» در حقیقت همان junḥa عربیِ حقوقیِ نو به معنیِ «بزهِ میان‌پایه» است، اسمی بر وزنِ «فُعله» از ریشهٔ بومیِ «ج‌ن‌ح» (جَنَحَ «میل کردن») — هم‌ریشه با «جَناح» و «جانح» — که در قانون‌های جزاییِ سدهٔ نوزدهم برای ردهٔ میانیِ جرم‌ها (جنایت/جنحه/خلاف) به‌قیاسِ délit فرانسوی ساخته شد. پس تنها بخشی از ادعای نورایی پذیرفتنی است: «جناح» آری، «جنحه» نه.\",\n     \"sources\": [A_JONHA, W_JANAH],\n     \"ref_check\": [\n      {\"ref\": \"MON:1243,1245\", \"status\": \"partial\", \"note\": \"the substance is in Mo'in — s.v. جنحه '(جُ حِ) [ع.] (اِ.) گناه، بزه کوچک' (abadis.ir, section فرهنگ معین) — so the words and senses the chart prints exist, but Mo'in tags them only [ع.] 'Arabic' and does not connect جنحه to گناه; and the page numbers could not be verified, since only the 2-volume Adena reprint (different pagination) is on disk and vajehyab/abadis carry no page numbers.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin and Dehkhoda s.v. جنحه (abadis.ir)\", \"stance\": \"partial\", \"note\": \"Moʿin '[ع.] گناه، بزه کوچک'; Dehkhoda 'اِثْم (محیط المحیط). گناه، و این لغتی است عامیانه و در هیچ یک از لغت‌نامه‌های معتبر نیست' — i.e. a late, colloquial word, not the Qurʾānic junāḥ.\"},\n      {\"src\": \"FVQ\", \"where\": \"Jeffery pp. 102-103\", \"stance\": \"supports\", \"note\": \"supports the جناح half of the box: the Arabic word is the Persian one, so its use in Persian is a re-borrowing.\"},\n      {\"src\": \"KLN\", \"where\": \"grep 'junah'/'janah' in KLN_1966.txt\", \"stance\": \"silent\", \"note\": \"no entry.\"},\n      {\"src\": \"BQT\", \"where\": \"p. 1836 (Mo'in's footnote to گناه)\", \"stance\": \"supports\", \"note\": \"'معرّب آن جناح «نیبرگ ص ۲۶۳»' — Mo'in records the Arabicised form جناح, but says nothing of جنحه.\"}\n     ]\n    },\n    {\n     \"id\": 11,\n     \"lang\": \"Latin\",\n     \"words\": \"nocĕre 2; noxa\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"Latin nocēre 'to harm, hurt, injure' is the o-grade causative *noḱ-éye- of *neḱ-, literally 'cause to perish' — Watkins/AHD s.v. nek-1: '3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocēre, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. [Pok. nek- 762.]' — so Nourai's bare 'AHD' citation is exactly on target for both words. Pokorny 762 sets it out the same way ('noceo \\\"I harm; hurt; injure (with DAT)\\\", s-Konj. noxit, noxa f. \\\"hurt! injury; crime; punishment\\\"'), and Walde-Pokorny II 326 adds the morphology: 'noceo \\\"schade\\\" … Ptc. *noxus vorausgesetzt von noxa \\\"Schaden, Strafe, Schuld\\\"', i.e. noxa is built on an s-stem/participial *nok-s-. Ernout-Meillet observe the division of labour inside the family: nocēre weakened to 'nuire' once 'to kill' was taken over by the denominative necāre from nex ('le sens de \\\"tuer\\\" ayant été réservé … au dénominatif de nex, necare'), and they define noxa as 'faute, dommage causé', citing the fetial formula ob eam rem noxam nocuerunt (Livy 9.10.9). Alongside them stand nex, necis 'violent death' (< *néḱ-s), pernicies, internecīnus. The '2' in 'nocĕre 2' is Nourai's own homonym numbering.\",\n     \"derivation_fa\": \"لاتینِ nocēre «آسیب رساندن» صورتِ سببیِ *noḱ-éye- از همان ریشهٔ *neḱ- است، یعنی به‌تحتِ‌اللفظ «سببِ نابودی شدن». واتکینز ذیلِ nek-1 می‌نویسد: «۳. صورتِ سببیِ *nok-eyo- در لاتینِ nocēre «آسیب زدن»: NOCENT، NOCUOUS، NUISANCE؛ INNOCENT، INNOCUOUS. ۴. صورتِ *nok-s- در لاتینِ noxa «آسیب، زیان»: NOXIOUS؛ OBNOXIOUS. [پوکورنی ۷۶۲]» — پس ارجاعِ کوتاهِ «AHD» نورایی برای هر دو واژه درست است. پوکورنی (ص ۷۶۲) و والده-پوکورنی (II/۳۲۶) نیز همین را دارند و دومی ساختِ صرفی را می‌افزاید: «noxa بر پایهٔ اسمِ مفعولِ فرضیِ *noxus». ارنو-مِیه نکته‌ای معنایی می‌افزایند: nocēre تنها پس از آن به «زیان رساندن» تخصیص یافت که معنیِ «کشتن» به necāre (مشتق از nex) واگذار شد، و noxa را «تقصیر، زیانِ وارد‌شده» می‌دانند و صیغهٔ فتیالیِ «ob eam rem noxam nocuerunt» (لیویوس ۹/۱۰/۹) را شاهد می‌آورند. عددِ ۲ در «nocĕre 2» شمارهٔ هم‌نگاشتِ خودِ نورایی است. ادعای نورایی درست است.\",\n     \"sources\": [E_NOX, R],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. nek-1: '3. Suffixed (causative) o-grade form *nok-eyo- in Latin nocére, to injure, harm: NOCENT, NOCUOUS, NUISANCE; INNOCENT, INNOCUOUS. 4. Suffixed o-grade form *nok-s- in Latin noxa, injury, hurt, damage: NOXIOUS; OBNOXIOUS. [Pok. nek- 762.]' — both of Nourai's Latin words with both of his glosses.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nek-1, §§3-4\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 762\", \"stance\": \"supports\", \"note\": \"'noceo \\\"I harm; hurt; injure (with DAT)\\\", s-Konj. noxit, noxa f. \\\"hurt! injury; crime; punishment! harm\\\"'.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 326\", \"stance\": \"supports\", \"note\": \"'noceo \\\"schade\\\", ne boa noccit (Lucilius 1195), Ptc. *noxus vorausgesetzt von noxa \\\"Schaden, Strafe, Schuld\\\"'.\"},\n      {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. noceō / noxa\", \"stance\": \"supports\", \"note\": \"'…le sens de \\\"tuer\\\" ayant été réservé entre autres au dénominatif de nex, necare … nocens \\\"qui nuit à, coupable\\\": innocens \\\"incapable de nuire, innocent\\\"'; 'noxa: faute, dommage causé; cf. la formule du fétial dans T.L. 9,10,9, ob eam rem noxam nocuerunt'.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. pp. 1058-59 s.v. noxious\", \"stance\": \"supports\", \"note\": \"'L. noxius, \\\"harmful, injurious\\\", fr. noxa, \\\"harm, injury\\\", rel. to noceō, nocēre, \\\"to hurt, injure, harm\\\", and to nex, gen. necis … For the change of e > o cp. memini and moneō … L. nocēo and nex derive fr. I.-E. base *neḱ-'.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 11.27 (the nocēre article)\", \"stance\": \"supports\", \"note\": \"'caus. of *nek- in Lat. nex \\\"violent death, murder\\\", necāre \\\"kill\\\", Grk. νέκυς, νεκρός \\\"corpse\\\", Av. nasu- \\\"corpse\\\", Skt. naś- \\\"perish\\\", caus. nāśaya-. Walde-P. 2.326.'\"}\n     ]\n    },\n    {\n     \"id\": 12,\n     \"lang\": \"English\",\n     \"words\": \"nuisance, innocent; noxious, obnoxious\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"All four are Latinate borrowings, not native words, and all four hang on nocēre/noxa, so the arrow Latin → English is right. nuisance: c.1400 'injury, hurt, harm', from Anglo-French nusaunce, Old French nuisance, a verbal noun to nuire < Lat. nocēre; the sense weakened to 'anything obnoxious to a community' (1660s) and to 'source of annoyance' (1831). innocent: 14th c. via Old French from Lat. innocēns, -entis 'not harming, harmless, blameless' (in- 'not' + present participle of nocēre) — Ernout-Meillet: 'innocens \\\"incapable de nuire, innocent\\\"'. noxious: c.1500 'unwholesome, harmful', from Lat. noxius 'hurtful, injurious', from noxa. obnoxious: 1580s, from Lat. obnoxius 'exposed to harm, liable to punishment' (ob- + noxa), first English sense 'subject or liable to', the modern 'offensive, objectionable' arising by association with noxious. Skeat states the group compactly: 'Noxious. (L.) L. noxius, hurtful. — L. noxa, hurt. — L. nocēre to hurt; cf. nex, destruction. (√NAK.)' and 'Nuisance; see Noxious'; Klein ends his noxious article 'Cp. obnoxious, nocent, innocent, nocuous, noxal, nuisance'. The empty refs= on this box is Nourai's normal practice for terminal English boxes, and the chain is uncontroversial.\",\n     \"derivation_fa\": \"هر چهار واژه وام‌واژهٔ لاتینی‌اند، نه انگلیسیِ میراثی، و همه به nocēre/noxa بازمی‌گردند؛ پس پیکانِ لاتین ← انگلیسی درست است. nuisance حدودِ ۱۴۰۰ م. به معنیِ «آسیب، زیان» از انگلونورمنِ nusaunce و فرانسویِ کهنِ nuisance (اسمِ مصدر از nuire < nocēre) به انگلیسی آمد و معنایش رو به سبکی رفت: «چیزِ آزارندهٔ همگانی» (دههٔ ۱۶۶۰) و سپس «مایهٔ دل‌آزاری» (۱۸۳۱). innocent در سدهٔ چهاردهم از راهِ فرانسویِ کهن از لاتینِ innocēns «بی‌آزار، بی‌گناه» (in- منفی‌ساز + اسمِ فاعلِ nocēre)؛ noxious حدودِ ۱۵۰۰ از لاتینِ noxius «زیان‌رسان» از noxa؛ و obnoxious در دههٔ ۱۵۸۰ از لاتینِ obnoxius «در معرضِ آسیب، سزاوارِ کیفر» (ob- + noxa) که نخست «گرفتار، در معرض» معنی می‌داد و سپس به قیاسِ noxious معنیِ «ناخوشایند» گرفت. اسکیت همین را کوتاه می‌گوید: «Noxious از لاتینِ noxius، از noxa، از nocēre؛ قس nex» و «Nuisance: نگاه کن به Noxious». نبودنِ ارجاع در این جعبه شیوهٔ همیشگیِ نورایی در جعبه‌های پایانیِ انگلیسی است و زنجیره جای گفت‌وگو ندارد. ادعای نورایی درست است.\",\n     \"sources\": [E_NUIS, E_NOX],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no citation in the book; the chain was checked against Klein, Skeat, Watkins/AHD and Etymonline instead.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 ed. pp. 1058-59 s.v. noxious\", \"stance\": \"supports\", \"note\": \"'noxious, adj., harmful, injurious. — L. noxius … Cp. obnoxious, nocent, innocent, nocuous, noxal, nuisance. Cp. also internecine, Necator, necro-, noyade, pernicious.'\"},\n      {\"src\": \"SKT\", \"where\": \"Skeat s.v. Noxious and Nuisance\", \"stance\": \"supports\", \"note\": \"'Noxious. (L.) L. noxius, hurtful. — L. noxa, hurt. — L. nocēre to hurt; cf. nex, destruction. (√NAK.)'; 'Nuisance; see Noxious.'\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nek-1 and the word index\", \"stance\": \"supports\", \"note\": \"index lines 'NUISANCE nek-1', 'NOXIOUS nek-1', 'OBNOXIOUS nek-1', 'INNOCENT nek-1', 'INNOCUOUS nek-1'.\"},\n      {\"src\": \"FSD\", \"where\": \"etymonline.com/word/nuisance and /noxious (archived)\", \"stance\": \"supports\", \"note\": \"'nuisance: c. 1400, \\\"injury, hurt, harm\\\", from Anglo-French nusaunce, Old French nuisance … from Latin nocere \\\"to hurt\\\"'; 'noxious (adj., c. 1500) \\\"unwholesome, harmful\\\", from Latin noxius … from noxa \\\"injury, hurt, damage\\\", ultimately from PIE *nek- \\\"death\\\"'.\"}\n     ]\n    },\n    {\n     \"id\": 13,\n     \"lang\": \"Greek\",\n     \"words\": \"nek-tar\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"Greek νέκταρ, the drink of the gods (Homer, Il. 1.598, Od. 5.93), whence Lat. nectar, is certainly connected with *neḱ- 'death' by the tradition Nourai follows, and his analysis 'death overcoming drink' with the cross-reference ☞Ter 1 is verbatim Watkins/AHD: '6. Greek nek-tar, the drink of the gods, \\\"overcoming death\\\" (*tar-, overcoming; see terə-2): NECTAR, (NECTARINE)', repeated under terə-2 ('3. Greek nek-tar, overcoming death (see nek-1)'). The compound analysis goes back to Prellwitz — Walde-Pokorny II 326 records it as such: 'νέκταρ \\\"Göttertrank\\\" (\\\"*Tod überwindend\\\", Prellwitz s.v.)' — and was argued at length by Thieme. But it is only one of three live views, so 'plausible' rather than 'confirmed'. (i) Pokorny, on the very page Nourai cites for the root, declines to take sides: 'about νέκταρ \\\"drink of the gods\\\" s. Kretschmer, Anz. Österr. Akad. 1947, Nr. 4 (to Tocharian B ñäkte \\\"god\\\"?) and Thieme, Studien 5 ff. (\\\"über den Tod hinwegrettend\\\"?)'. (ii) Current Wiktionary treats νέκταρ as a plain suffixed derivative of the root, *néḱ-tr̥h₂, with no second root at all. (iii) Klein — Nourai's own authority in the Avestan box on this page — rejects the Indo-European etymology altogether: 'L., fr. Gk. νέκταρ … which prob. derives fr. Heb. (yayin) niqtar, \\\"smoked (wine), perfumed (wine)\\\", Niphʿal of the Sem. base q-t-r'. Etymonline hedges in the same direction as AHD but with 'perhaps': 'from Greek nektar … which is perhaps an ancient Indo-European poetic compound of nek- \\\"death\\\" + -tar \\\"overcoming\\\"'.\",\n     \"derivation_fa\": \"«néktar» یونانی، نوشابهٔ خدایان (ایلیاد ۱/۵۹۸، اودیسه ۵/۹۳) و سرچشمهٔ nectar لاتین، بی‌گمان در سنتی که نورایی از آن پیروی می‌کند به ریشهٔ *neḱ- «مرگ» بسته شده است، و تحلیلِ او («نوشابهٔ چیره بر مرگ» با ارجاعِ ☞Ter 1) لفظ‌به‌لفظ همان چیزی است که واتکینز می‌گوید: «یونانی nek-tar، نوشابهٔ خدایان، \\\"چیره بر مرگ\\\" (*tar- \\\"چیره‌شدن\\\"، نگاه کن به terə-2)». این تحلیلِ ترکیبی از پرلویتس آغاز شد — والده-پوکورنی (II/۳۲۶) آن را به نامِ او ثبت می‌کند: «néktar \\\"نوشابهٔ خدایان\\\" (\\\"*چیره بر مرگ\\\"، پرلویتس)» — و تیمه آن را گسترش داد. اما این تنها یکی از سه نظرِ زنده است و از این‌رو حکمِ ما «با احتیاط پذیرفتنی» است: نخست، خودِ پوکورنی در همان صفحهٔ ۷۶۲ داوری نمی‌کند و تنها به کرچمر و تیمه ارجاع می‌دهد (با علامتِ پرسش)؛ دوم، ویکی‌واژهٔ امروزی néktar را صرفاً مشتقی پسوندی از همان ریشه (*néḱ-tr̥h₂) می‌داند، بدونِ جزءِ دوم؛ سوم، کلاین — که نورایی در همین صفحه در جعبهٔ اوستایی به او ارجاع داده — ریشه‌شناسیِ هندواروپایی را یکسر رد می‌کند و آن را از عبریِ (yayin) niqtar «شرابِ دودی/عطرآمیز» از ریشهٔ سامیِ q-t-r می‌گیرد.\",\n     \"sources\": [E_NECTAR, R],\n     \"ref_check\": [\n      {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. nek-1: '6. Greek nek-tar, the drink of the gods, \\\"overcoming death\\\" (*tar-, overcoming; see terə-2): NECTAR, (NECTARINE). [Pok. nek- 762.]'; and s.v. terə-2: '3. Greek nek-tar, overcoming death (see nek-1)'. Nourai's gloss and his ☞Ter 1 cross-reference are taken straight from here.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. nek-1 §6 and terə-2 §3\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"WLD\", \"where\": \"Bd. II 326\", \"stance\": \"partial\", \"note\": \"'νέκ-ταρ \\\"Göttertrank\\\" (\\\"*Tod überwindend\\\", Prellwitz s.v.)' — reports the compound analysis, attributing it to Prellwitz rather than asserting it.\"},\n      {\"src\": \"POK\", \"where\": \"IEW 762\", \"stance\": \"partial\", \"note\": \"'about νέκταρ \\\"drink of the gods\\\" s. Kretschmer Anz. Österr. Akad. 1947, Nr. 4 (to Tocharian B ñäkte \\\"god\\\"?) and Thieme Studien 5 ff. (\\\"über den Tod hinwegrettend\\\"?)' — Pokorny lists νέκταρ under the root but leaves the analysis open.\"},\n      {\"src\": \"KLN\", \"where\": \"1966 ed. p. 1035 s.v. nectar (and s.v. ambrosia, Keturah)\", \"stance\": \"contradicts\", \"note\": \"'nectar, n., the drink of the gods (Greek mythol.) — L., fr. Gk. νέκταρ, \\\"drink of the gods\\\", esp. \\\"wine\\\", which prob. derives fr. Heb. (yayin) niqtar, \\\"smoked (wine), perfumed (wine)\\\", Niphʿal … of the Sem. base q-t-r' — Klein denies the IE etymology and derives it from Semitic.\"},\n      {\"src\": \"FSD\", \"where\": \"etymonline.com/word/nectar (archived)\", \"stance\": \"partial\", \"note\": \"'from Greek nektar, name of the drink of the gods, which is perhaps an ancient Indo-European poetic compound of nek- \\\"death\\\" + -tar \\\"overcoming\\\"' — same analysis as AHD, flagged as conjectural.\"}\n     ]\n    },\n    {\n     \"id\": 14,\n     \"lang\": \"English\",\n     \"words\": \"nectar, nectarine\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"English nectar is first attested in the 1550s, from Latin nectar < Greek νέκταρ; it was extended to any delicious drink by the 1580s and to the sugary secretion of flowers about 1600 (whence nectary, nectar-guide). nectarine, however, is not a second borrowing from Greek: it is 1660s, the noun use of an English adjective nectarine 'of or like nectar' formed 1610s from nectar + -ine, applied to the smooth-skinned, firm-fleshed peach, probably encouraged by German Nektarpfirsich 'nectar-peach'; the earlier English form was nectrine. So the Greek → English arrow is exact for nectar and one step short for nectarine, which is an English derivative of the loanword rather than an inherited or borrowed form — a nuance rather than an error, since Nourai's terminal English boxes routinely gather a word with its English derivatives (compare 'nuisance, innocent' in node 12).\",\n     \"derivation_fa\": \"«nectar» انگلیسی نخست در دههٔ ۱۵۵۰ گواه دارد، از لاتینِ nectar و آن از یونانیِ néktar؛ در دههٔ ۱۵۸۰ معنایش به «هر نوشابهٔ گوارا» و نزدیکِ ۱۶۰۰ به «شهدِ گل» گسترش یافت (و از آن nectary «شهدینه» ساخته شد). اما «nectarine» وام‌گیریِ دومی از یونانی نیست: در دههٔ ۱۶۶۰ از کاربردِ اسمیِ صفتِ انگلیسیِ nectarine «شهدآگین، شهدمانند» (دههٔ ۱۶۱۰، از nectar + پسوندِ -ine) پدید آمد و به هلوی پوست‌صافِ سخت‌گوشت (شلیل) داده شد، و احتمالاً واژهٔ آلمانیِ Nektarpfirsich «هلوی شهدین» در آن اثر داشته؛ صورتِ کهن‌ترِ انگلیسی nectrine بوده است. پس پیکانِ یونانی ← انگلیسی برای nectar دقیق است و برای nectarine یک پله ناتمام، چون این دومی مشتقِ انگلیسیِ همان وام‌واژه است؛ این نکته‌ای است در حدِ دقت، نه خطا، زیرا نورایی در جعبه‌های پایانیِ انگلیسی همواره واژه را با مشتق‌هایش یک‌جا می‌آورد (قس «nuisance, innocent» در گرهِ ۱۲).\",\n     \"sources\": [E_NECTAR],\n     \"ref_check\": [\n      {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no citation in the book; verified against Klein, Watkins/AHD and Etymonline.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"KLN\", \"where\": \"1966 ed. p. 1035 s.v. nectar\", \"stance\": \"partial\", \"note\": \"Klein confirms the transmission 'L., fr. Gk. νέκταρ' into English but derives the Greek word from Semitic (see node 13); he gives the English derivatives at the same place.\"},\n      {\"src\": \"AHD\", \"where\": \"Watkins 1985, index\", \"stance\": \"supports\", \"note\": \"'NECTAR nek-1', 'NECTARINE nek-1' — and in the root article nectarine is given in parentheses, Watkins's notation for a secondary derivative.\"},\n      {\"src\": \"FSD\", \"where\": \"etymonline.com/word/nectar (archived)\", \"stance\": \"supports\", \"note\": \"'Nectar (n.): 1550s, from Latin nectar, from Greek nektar … expanded to mean any delicious drink by the 1580s and came to describe flower nectar around 1600'; 'Nectarine (n.): type of peach with smooth skin and firmer pulp, 1660s, noun use of adjective meaning \\\"of or like nectar\\\" (1610s; see nectar + -ine) … likely influenced by the German term nektarpfirsich, and earlier appeared in English as nectrine'.\"},\n      {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'Nectar'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no nectar entry.\"}\n     ]\n    }\n   ]\n  },\n  {\n   \"entry\": 2,\n   \"root\": \"Někš\",\n   \"verdict\": \"confirmed\",\n   \"modern_form\": \"Sanskrit nikṣ- / nekṣ- 'to pierce, prick' (níkṣati, nikṣaṇa- 'pointed stick'), IE base *niks- 'press, force, pierce'\",\n   \"note\": \"Language label, gloss and page reference are all right, and the reference is the source of the entry: Horn, Grundriss der neupersischen Etymologie no. 1067, printed p. 238 — 'neš \\\"Spitze, Stachel; Gift (AM. S. 10 Zeile 5 v. u.)\\\", nešter \\\"Lanzette\\\". ai. vergl. nekṣaṇa- \\\"spitzer Stab, Spiess\\\", zu √nekṣ-, nikṣati \\\"durchbohren\\\" (Horn).' The Sanskrit root is real: Mann, Indo-European Comparative Dictionary, lemma 'niks- (1) \\\"press, force, pierce, penetrate\\\" … Skt. níkṣāmi, v. \\\"pierce\\\" … (Isophones: Skt. nikṣaṇam \\\"stirring-rod\\\")'. Two caveats, which are why the individual nodes are graded lower than the root. First, this root box is a Sanskrit form used as the head of an Iranian family, and Persian nīš cannot be a descendant of Sanskrit; Horn himself writes 'ai. vergl.' ('compare Old Indic'), i.e. a cognate, not a source. Second, current Iranian etymology takes a different route: Wiktionary derives NP نیش from MP nēš, from an Old Median form, from Proto-Iranian *náyjam, Proto-Indo-Iranian *náyȷ́žʰam — an inherited Iranian word, its -š the North-West/Median reflex. Pokorny has no lemma corresponding to this root (grep for nikṣati/nekṣaṇa in POK_full.txt is empty); the nearest thing in Walde-Pokorny is the doubtful 'negh \\\"durchbohren, stechen, stupfen\\\"?' at Bd. II 327, which is a different reconstruction (Slavic nožь 'knife').\",\n   \"note_fa\": \"برچسبِ زبان، معنی و شمارهٔ صفحه هر سه درست است و همان ارجاع، سرچشمهٔ این مدخل است: هرن در «دستورِ ریشه‌شناسیِ فارسی نو»، شمارهٔ ۱۰۶۷، صفحهٔ ۲۳۸ می‌نویسد: «neš \\\"نوک، خار؛ زهر\\\"، nešter \\\"نیشتر\\\". قس سنسکریتِ nekṣaṇa- \\\"چوبِ سرتیز، سیخ\\\"، از ریشهٔ nekṣ-، nikṣati \\\"سوراخ کردن\\\"». ریشهٔ سنسکریت واقعی است؛ مان در «فرهنگ سنجشیِ هندواروپایی» مدخلِ «niks- \\\"فشردن، فروکردن، سوراخ کردن\\\"» را دارد با «سنسکریت níkṣāmi \\\"سوراخ می‌کنم\\\"» و «nikṣaṇam \\\"سیخ\\\"». دو نکتهٔ احتیاط: یک، این جعبه صورتی سنسکریت را سرِ خانواده‌ای ایرانی نشانده، در حالی که «نیش» فارسی نمی‌تواند بازماندهٔ سنسکریت باشد و خودِ هرن هم «قس» نوشته، نه «از». دو، ریشه‌شناسیِ امروزیِ ایرانی راهی دیگر می‌رود: ویکی‌واژه «نیش» را از nēš فارسی میانه و آن را از صورتی مادیِ کهن و ایرانی آغازینِ *náyjam می‌گیرد، یعنی واژه‌ای میراثی که «ش»ِ آن بازتابِ شمال‌غربی/مادی است. پوکورنی چنین ریشه‌ای ندارد و نزدیک‌ترین چیز در والده-پوکورنی (II/۳۲۷) مدخلِ مشکوکِ «negh \\\"سوراخ کردن، خلیدن\\\"؟» است که بازسازیِ دیگری است.\",\n   \"sources\": [W_NISH],\n   \"ref_check\": [\n    {\"ref\": \"HRN:238\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 259, no. 1067 (the leaf ends with the printed catch-number '— 239 —', so it is printed p. 238): 'neš \\\"Spitze, Stachel; Gift\\\", nešter \\\"Lanzette\\\". ai. vergl. nekṣaṇa- \\\"spitzer Stab, Spiess\\\", zu √nekṣ-, nikṣati \\\"durchbohren\\\" (Horn).' Nourai's root name, gloss and page are all taken from here.\"}\n   ],\n   \"consulted\": [\n    {\"src\": \"IEC\", \"where\": \"Mann s.v. niks- (1)\", \"stance\": \"supports\", \"note\": \"'niks- (1) \\\"press, force, pierce, penetrate\\\". Cf. nik- (2). Skt. níkṣāmi, v. \\\"pierce\\\"; Lat. nixus, gs: -ūs, m. \\\"effort; trend\\\"; Li. cf. ninku, nikti, v. \\\"tackle\\\". (Isophones: Skt. nikṣaṇam \\\"stirring-rod\\\"; Li. nikšas \\\"thimble\\\", nikštas \\\"dislocation, crack in bones\\\", nykštys \\\"thumb; big toe\\\").'\"},\n    {\"src\": \"POK\", \"where\": \"POK_full.txt, greps 'niksati', 'neksana'\", \"stance\": \"silent\", \"note\": \"no lemma; Pokorny does not reconstruct this root.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II 327\", \"stance\": \"partial\", \"note\": \"'negh \\\"durchbohren, stechen, stupfen\\\"? Aksl. pro-noziti \\\"durchbohren\\\", nožь \\\"Messer\\\" = lett. nazis \\\"Messer\\\" … ir. ness \\\"Wunde\\\"' — a root of the right meaning but a different reconstruction, and Walde-Pokorny marks it with a question mark; the Sanskrit nikṣ- forms are not listed under it.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p. 104, note to no. 1067\", \"stance\": \"supports\", \"note\": \"Hübschmann accepts Horn's entry and adds the Afghan and Armenian evidence (see node 1).\"}\n   ],\n   \"nodes\": [\n    {\n     \"id\": 1,\n     \"lang\": \"Pahlavi\",\n     \"words\": \"něš; něš-tar\",\n     \"verdict\": \"plausible\",\n     \"derivation\": \"A Middle Persian nēš 'sting, point' and nēštar 'lancet' are not attested in the Book Pahlavi corpus — MacKenzie's Concise Pahlavi Dictionary and Nyberg's glossary both have no such entry (greps for nēš in PHD.txt and NYB_vol2_glossary.txt return only anēš 'immortal', nēzag etc.) — so this box is reconstructed, not documented. The reconstruction is nonetheless well founded, and on exactly the page Nourai cites: Hübschmann, Persische Studien p. 104, note to Horn no. 1067: 'Dazu afgh. LW. neš \\\"the sting of any venomous animal, puncture, lancet\\\"; naštar und neštar \\\"a lancet\\\"; arm. LW. nštr, nstrak \\\"Lanzette\\\" (das ein phl. *nēštir voraussetzt). Np. neštar bei Fird. I, 46, 214.' The argument is the standard one for Middle Persian lexemes lost from the surviving books: an Old Armenian loanword (nštr, nstrak 'lancet', a medical term) can only have been taken from a Middle Persian *nēštir, and Pashto neš/naštar is a further loan from Persian. Mo'in reproduces the whole note in his footnote at BQT:2228, ending '(از یک کلمه پهلوی *nēštir ناشی شده) فارسی neštar. در فردوسی ۱، ۴۶، ۲۱۴ آمده … هوبشمان ۱۰۶۷'. Two reservations: the sources reconstruct the instrument-noun *nēštir as a whole, not Nourai's segmentation nēš + -tar; and Wiktionary's Proto-Iranian *náyjam route (see the root note) would make nēš inherited Iranian rather than a Sanskrit derivative, which does not affect the Pahlavi → Persian step but does affect the box above it.\",\n     \"derivation_fa\": \"صورت‌های nēš «نیش» و nēštar «نیشتر» در متونِ بازماندهٔ پهلویِ کتابی گواه ندارند — نه فرهنگِ مکنزی و نه واژه‌نامهٔ نیبرگ چنین مدخلی ندارند — پس این جعبه بازسازی است، نه ثبتِ متنی؛ با این حال بازسازی استوار است و درست بر همان صفحه‌ای که نورایی ارجاع داده: هوبشمان در «پژوهش‌های فارسی» ص ۱۰۴، در حاشیهٔ شمارهٔ ۱۰۶۷ هرن می‌نویسد: «نیز وام‌واژهٔ افغانیِ neš \\\"نیشِ هر جانورِ زهردار، سوراخ، نیشتر\\\"؛ naštar و neštar \\\"نیشتر\\\"؛ وام‌واژهٔ ارمنیِ nštr و nstrak \\\"نیشتر\\\" (که پهلویِ *nēštir را پیش‌فرض می‌گیرد). نیشترِ فارسی در فردوسی، جلد ۱، ص ۴۶، بیتِ ۲۱۴». استدلال، همان استدلالِ همیشگی برای واژه‌های فارسیِ میانه‌ای است که از متونِ بازمانده افتاده‌اند: وام‌واژهٔ ارمنیِ کهن (که اصطلاحی پزشکی است) جز از یک *nēštir فارسیِ میانه نمی‌توانسته گرفته شود. معین همین حاشیه را در پانوشتِ برهان (ص ۲۲۲۸) بازگفته است. دو نکتهٔ احتیاط: منابع، کلِ اسمِ ابزارِ *nēštir را بازسازی می‌کنند، نه تجزیهٔ nēš + tar را؛ و اگر مسیرِ ایرانیِ آغازینِ *náyjam درست باشد، «نیش» واژه‌ای میراثی است نه برگرفته از سنسکریت.\",\n     \"sources\": [W_NISH],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2228\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:2228 (v4 pdf p.311), Mo'in's footnote 3 to نیش: 'هندی باستان *nekṣaṇa- (چوب سرتیز، سیخ) از ریشهٔ nikṣati/nekṣ- (سوراخ کردن) «اشتقاق ۱۰۶۷»؛ افغانی neš (نیش هر جانور زهردار، نشتر)؛ naštar و neštar (نشتر)، ارمنی nštr, nštrak (نشتر) (از یک کلمه پهلوی *nēštir ناشی شده) فارسی neštar. در فردوسی ۱، ۴۶، ۲۱۴ آمده. «هوبشمان ۱۰۶۷»'.\"},\n      {\"ref\": \"HUB:104\", \"status\": \"supports\", \"note\": \"HUB.txt leaf 115, which opens '— 104 -': '1067. Dazu afgh. LW. neš \\\"the sting of any venomous animal, puncture, lancet\\\"; naštar und neštar \\\"a lancet\\\"; arm. LW. nštr, nstrak \\\"Lanzette\\\" (das ein phl. *nēštir voraussetzt). Np. neštar bei Fird. I, 46, 214.' Exact page, and the source of the Pahlavi box.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 104 (note to Horn 1067)\", \"stance\": \"supports\", \"note\": \"quoted above; the reconstructed form is *nēštir, based on the Armenian loan.\"},\n      {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, greps 'nēš', 'nes'\", \"stance\": \"silent\", \"note\": \"MacKenzie has no nēš or nēštar; the only nē(š)-shapes are anēš 'immortal', anēšmār 'countless'.\"},\n      {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, greps 'nēš', 'nyyš'\", \"stance\": \"silent\", \"note\": \"the glossary has nyyšydn/nyyš- 'murw-niš' but no nēš 'sting'; the word is absent from Nyberg's Pahlavi corpus.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 1067 (p. 238)\", \"stance\": \"supports\", \"note\": \"'neš \\\"Spitze, Stachel; Gift\\\", nešter \\\"Lanzette\\\"' — Horn's entry, from which the box is built.\"},\n      {\"src\": \"BQT\", \"where\": \"p. 2228, Mo'in's footnote 3\", \"stance\": \"supports\", \"note\": \"reproduces Hübschmann's *nēštir reconstruction and the Armenian and Pashto evidence.\"}\n     ]\n    },\n    {\n     \"id\": 2,\n     \"lang\": \"Persian\",\n     \"words\": \"nîš; nîštar\",\n     \"verdict\": \"confirmed\",\n     \"derivation\": \"NP نیش nīš, older nēš, 'sting, point, fang; venom' and نیشتر / نشتر / نیشدر nēštar 'lancet, phlebotome' are both securely attested and continue the Middle Persian forms with the regular raising of MP ē to NP ī (nēš > nīš, as in šēr > šīr, tēr > tīr); the variant نیشدر preserves the -d- of the second element, and نشتر is the shortened form (whence the Armenian and Pashto loans naštar). نیشتر is attested from Ferdowsi onwards — Hübschmann cites Šāhnāma I, 46, 214, and the chart's own verse ('سرو دارد و نیشتر چون گراز') uses it of a boar's tusk, which is why Nourai's gloss adds 'tooth'. Mo'in defines it '(تَ) (اِ.) آلت نوک تیزی که با آن رگ می زدند' and Dehkhoda 'مبضغ (دهار). ابزاری مر جراحان را که بدان رگ می زنند و فصد می کنند و آبله می کوبند' — a surgeon's lancet, exactly Nourai's 'a sharp tool'. On the second element: Nourai's cross-reference ☞Der 1 refers -tar to *der-/*dar- 'to tear, split', and the page he cites for it, Buck 9.28 'tear' (p. 565), is indeed where the relevant material stands — 'Skt. dṛ- \\\"burst, tear\\\", Av. niš-dar- \\\"tear out\\\" (Barth. 689)'. That Avestan compound niš-dar- would in fact yield MP *nēšdar directly and explain the Persian variant نیشدر, though on that reading the first element is the preverb niš- 'out' rather than nēš 'sting'; either way the -tar/-dar goes with dar- 'to tear', which is what the citation is for.\",\n     \"derivation_fa\": \"«نیش» (کهن‌تر nēš) به معنیِ «نوک، خار، دندانِ زهرآگین؛ زهر» و «نیشتر / نشتر / نیشدر» به معنیِ «نیشترِ جراحی و فصد» هر دو گواهِ استوار دارند و دنبالهٔ صورت‌های فارسی میانه‌اند، با ابدالِ قاعده‌مندِ «ای»ِ کشیدهٔ فارسی میانه به «ی» در فارسی نو (nēš > nīš، مانندِ šēr > šīr و tēr > tīr)؛ گونهٔ «نیشدر» دالِ جزءِ دوم را نگه داشته و «نشتر» صورتِ کوتاه‌شده است که وام‌واژه‌های ارمنی و پشتو (naštar) از آن گرفته شده. «نیشتر» از فردوسی به‌بعد گواه دارد — هوبشمان به شاهنامه (ج ۱، ص ۴۶، بیتِ ۲۱۴) ارجاع می‌دهد — و در بیتِ خودِ نمودار («سرو دارد و نیشتر چون گراز») به معنیِ دندانِ گراز است، و همین است سببِ آنکه نورایی «tooth» را هم در معنی آورده. معین آن را «آلت نوک‌تیزی که با آن رگ می‌زدند» و دهخدا «مبضغ … ابزاری مر جراحان را که بدان رگ می‌زنند و فصد می‌کنند» تعریف می‌کند. دربارهٔ جزءِ دوم: ارجاعِ ☞Der 1 آن را به ریشهٔ *dar- «دریدن» می‌بندد و صفحه‌ای که نورایی برای آن آورده (باک، بندِ ۹.۲۸ «دریدن»، ص ۵۶۵) درست همان جایی است که مادهٔ لازم آمده: «سنسکریت dṛ- \\\"دریدن\\\"، اوستایی niš-dar- \\\"برکشیدن، بیرون دریدن\\\" (بارتولومه ۶۸۹)». اگر همان ترکیبِ اوستایی سرچشمه باشد، *nēšdar فارسیِ میانه و گونهٔ «نیشدر» یکسر توضیح می‌یابد، هرچند در آن صورت جزءِ نخست پیشوندِ niš- «بیرون» است نه «نیش». ادعای نورایی درست است.\",\n     \"sources\": [A_NISHTAR, W_NISH],\n     \"ref_check\": [\n      {\"ref\": \"BQT:2228\", \"status\": \"supports\", \"note\": \"tools/ref_page.py BQT:2228 (v4 pdf p.311): the headword نیش is on the page ('نیش ـ با یای مجهول بر وزن دیش، تیزی سر هر چیز را گویند همچو نیش کارد و خنجر'), and Mo'in's footnote 3 gives the etymology and the neštar/naštar forms with the Pahlavi *nēštir and the Ferdowsi citation. Both of Nourai's Persian words on the cited page.\"},\n      {\"ref\": \"SYN:565\", \"status\": \"partial\", \"note\": \"Buck p. 565 = §9.28 TEAR (SYN.txt leaf ~617; the running heads 'MISCELLANEOUS PHYSICAL ACTS, ETC. 561' at 9.25 AX and '564 SELECTED INDO-EUROPEAN SYNONYMS' at 9.27 SPLIT fix the position, and '566' stands at the head of 9.29 FLAY). The page has 'Skt. dṛ- \\\"burst, tear\\\", Av. niš-dar- \\\"tear out\\\" (Barth. 689)' — it supports the -tar element (Nourai's ☞Der 1) but says nothing about nīš itself, so it is a partial rather than a full support for the node.\"}\n     ],\n     \"consulted\": [\n      {\"src\": \"BQT\", \"where\": \"p. 2228 s.v. نیش with Mo'in's footnote 3\", \"stance\": \"supports\", \"note\": \"quoted above.\"},\n      {\"src\": \"MON\", \"where\": \"Farhang-e Moʿin and Dehkhoda s.v. نیشتر (abadis.ir)\", \"stance\": \"supports\", \"note\": \"Moʿin '(تَ) (اِ.) آلت نوک تیزی که با آن رگ می زدند'; Dehkhoda 'مبضغ (دهار). ابزاری مر جراحان را که بدان رگ می زنند و فصد می کنند و آبله می کوبند'.\"},\n      {\"src\": \"HRN\", \"where\": \"no. 1067 (p. 238)\", \"stance\": \"supports\", \"note\": \"'neš \\\"Spitze, Stachel; Gift\\\", nešter \\\"Lanzette\\\"' — both New Persian words, with Horn's Sanskrit comparison.\"},\n      {\"src\": \"HUB\", \"where\": \"Persische Studien p. 104\", \"stance\": \"supports\", \"note\": \"'naštar und neštar \\\"a lancet\\\" … Np. neštar bei Fird. I, 46, 214' — the Ferdowsi attestation behind the chart's verse.\"},\n      {\"src\": \"SYN\", \"where\": \"Buck 9.28 'tear' (p. 565)\", \"stance\": \"partial\", \"note\": \"'Skt. dṛ- \\\"burst, tear\\\" Av. niš-dar- \\\"tear out\\\" (Barth. 689)' — the material for the second element of nīštar/nīšdar.\"}\n     ]\n    }\n   ]\n  }\n ]\n}\n\nwith io.open(\"data/verification/page-357.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 -m json.tool data/verification/page-357.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 357",
 "description": "Write and validate page-357.json"
}
```


### [2026-09-07T18:55:56.777Z] TOOL RESULT

```
written
JSON OK
nodes verified: 16/16
node verdicts: {'transcription_suspect': 1, 'plausible': 4, 'confirmed': 11}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 20, 'partial': 4, 'not_checked': 4}
books consulted: {'supports': 54, 'partial': 7, 'silent': 9, 'contradicts': 1} | by book: {'KLN': 7, 'MON': 6, 'NYB': 6, 'HUB': 6, 'HRN': 5, 'BQT': 5, 'PHD': 5, 'SYN': 4, 'AHD': 4, 'WLD': 3, 'BRT': 3, 'FVQ': 3, 'FSD': 3, 'KNT': 2, 'POK': 2, 'SKT': 2, 'ARY': 1, 'AFM': 1, 'PLA': 1, 'LKT': 1, 'LAT': 1}
```


## [2026-09-07T18:56:20.544Z] AGENT

Page 357 (book p. 327) verified — 0 PROBLEM lines from `verify_check.py`.

**Counts:** 2 entries (entry 1 is the `Nek 2 -> Neku` redirect, skipped), 16/16 nodes.
- Root verdicts: 2 confirmed
- Node verdicts: 11 confirmed, 4 plausible, 1 transcription_suspect
- ref_check: 20 supports, 4 partial, 4 not_checked · consulted: 54 supports, 7 partial, 9 silent, 1 contradicts (21 books)

**Flagged items**
- `transcription_suspect` — Nek 1 #1 [Sanskrit] `nâša / pra-nača / pra-nač`: none is a Sanskrit form (nāśá- is a noun given a verbal gloss; ś written as č). Traced to Mo'in's Persian-script footnote at BQT:1471 ("سانسکریت پرناچه", quoted verbatim by Dehkhoda). `error_in: book` — the printed page 357 shows exactly these forms, so the extraction is faithful. Correct: náśyati / nāśá-, pra-naśyati.
- `plausible` — #2 farnās: etymology (fra + naś-) is Horn no. 822 p. 182 exactly, but the arrow comes out of the Sanskrit box; the parent is Old Iranian *fra-nās-, a cognate not a source.
- `plausible` — #10 Persian «جناح (جنحه)»: جناح is a genuine Persian→Arabic→Persian round trip, but جنحه is modern juridical Arabic *junḥa* 'misdemeanour' from the native root ج‌ن‌ح; Dehkhoda calls it colloquial and absent from the reputable lexica.
- `plausible` — #13 Greek nek-tar: the 'death-overcoming' compound is AHD/Prellwitz/Thieme, but Pokorny 762 leaves it open, Wiktionary takes it as plain *néḱ-tr̥h₂, and Klein (p. 1035) derives νέκταρ from Hebrew *niqtar* — the one `contradicts` on the page.
- `plausible` — Někš #1 [Pahlavi] nēš/nēštar: unattested in MacKenzie and Nyberg (both silent); reconstructed from Armenian nštr, which per Hübschmann p. 104 presupposes phl. *nēštir (the whole instrument noun, not nēš + -tar).

**No extraction errors** — the JSON matches the printed page node for node (image saved to `data/verification/sources/refs/ocr/BOOK/357.png`).

**Reference-page findings worth noting:** all of Nourai's page numbers on this chart check out precisely — POK:762, HRN:182/238/285, HUB:104, KNT:192-193 (Kent's `naθ-` entry), KLN:1059 (Klein s.v. *noxious*, and the source of Nourai's root gloss "to destroy"), SYN:290 (Buck 4.77 CORPSE), BQT:1471/1836/2136/2228, and SNS:272/282 (two pages per leaf, the two citations calibrate each other). `MAG:186` (Widengren 1955) is `not_checked` — lending-only everywhere; `VDQ:38` verified through the original Jeffery FVQ pp. 102-103 (same entry), which supplies the pre-Islamic loan date and the Muʿallaqa attestation for Arabic junāḥ. Two `MON` page numbers could not be checked (only the 2-vol reprint is on disk); MON:4714 may point at the place-name نسا rather than 'corpse'. 11 web pages archived via `fetch_source.py`.
