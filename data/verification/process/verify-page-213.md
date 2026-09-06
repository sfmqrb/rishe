# Verification process log — verify-page-213


## [2026-09-06T14:52:03.381Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 213 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-213.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-213.json. Write /home/sfmqrb/git/rishe/data/verification/page-213.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 213` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T14:52:05.245Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T14:52:05.956Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T14:52:05.967Z] TOOL RESULT

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


## [2026-09-06T14:52:06.090Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-213.txt"
}
```


### [2026-09-06T14:52:06.109Z] TOOL RESULT

```
1	=== PDF page 213 (book page 183) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Gwhen 1 : to swell, fill  (refs POK:491)  PART 2
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:491; HRN:194; BRT:583; ZMA:49 | kan 1, xan, gan 1 : to dig dirt out and mound it up ; čât : well
5	  #2 (parent #1) [Pahlavi] refs=HRN:194; BQT:1707; SNS:8,155 | kantan, xandan : to dig ; kandak : a dug-in house ; xânîg : spring, water pond ; čâh : well
6	    #3 (parent #2) [Persian] refs=BQT; HRN:186; FVF:593 | kandan «کندن ( کان )» : to dig ; kandak «کَنَدَک» : places dug out in a house ; kandŭk «کندوک» : grain silo, bee hive | extra: کندوله ، کندوج ، کندو ، کندره ، کندور
7	      #4 (parent #3) [Greek] refs=SKT:217 | konda, kondu : a drinking vessel | NOTE: Derivation from Persian is debated.
8	        #5 (parent #4) [Italian] refs=SKT:217; PRT:260 | gonda, gondola : gondola | NOTE: (due to its shape)
9	          #6 (parent #5) [English] refs=SKT:217 | gondola
10	      #7 (parent #3) [Persian] refs=MON:3102 | kanand «کَنَند» : a tool for tilling earth
11	    #8 (parent #2) [Persian] refs=BQT; SYN:46; MON:1395 | xânî «خانی» : spring, water pond ; čâh «چاه» : water well
12	    #9 (parent #2) [Persian] refs=HRN:194; BQT; ZMA:51; MON | xâneh «خانه» : house ; ğâneh «غانه» : house | extra: خان ، خَن ، گلخن
13	خانگاه ، خانقاه
14	ـ غان ، دامغان
15	      #10 (parent #9) [Persian] refs=MON:465 | bâlâxâneh «بالاخانه» : top room, balcony ☞Bhergh
16	        #11 (parent #10) [Italian] refs=LKT:17 | barbacane, balcone
17	          #12 (parent #11) [French] refs=PHN:55 | balcon
18	            #13 (parent #12) [Persian] refs=MON:467 | bâlkon «بالکن»
19	          #14 (parent #11) [English] refs=KLN:148; LKT:17 | barbican, balcony | NOTE: See AHD for different roots
20	    #15 (parent #2) [Arabic] refs=PLA:113 | xandaq : a dug out trench
21	      #16 (parent #15) [Persian] refs=MON:1443 | xandaq «خندق»
22	
```


## [2026-09-06T14:52:10.370Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-213.json",
 "description": "Read source JSON for page 213"
}
```


### [2026-09-06T14:52:10.415Z] TOOL RESULT

```
{
  "pdf_page": 213,
  "book_page": 183,
  "entries": [
    {
      "root": {
        "name": "Gwhen 1",
        "lang": "Indo-European",
        "refs": "POK:491",
        "gloss": "to swell, fill"
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:491; HRN:194; BRT:583; ZMA:49",
          "words": [
            {"translit": "kan 1, xan, gan 1", "gloss": "to dig dirt out and mound it up", "script": null},
            {"translit": "čât", "gloss": "well", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "HRN:194; BQT:1707; SNS:8,155",
          "words": [
            {"translit": "kantan, xandan", "gloss": "to dig", "script": null},
            {"translit": "kandak", "gloss": "a dug-in house", "script": null},
            {"translit": "xânîg", "gloss": "spring, water pond", "script": null},
            {"translit": "čâh", "gloss": "well", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT; HRN:186; FVF:593",
          "words": [
            {"translit": "kandan", "gloss": "to dig", "script": "کندن ( کان )"},
            {"translit": "kandak", "gloss": "places dug out in a house", "script": "کَنَدَک"},
            {"translit": "kandŭk", "gloss": "grain silo, bee hive", "script": "کندوک"}
          ],
          "script_extra": "کندوله ، کندوج ، کندو ، کندره ، کندور",
          "note": null,
          "quote": {"text": "ده و دو هزار انگبین کندره - به دژ ها کشند آنهمه یکسره", "poet": "Ferdowsî"}
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Greek",
          "refs": "SKT:217",
          "words": [
            {"translit": "konda, kondu", "gloss": "a drinking vessel", "script": null}
          ],
          "script_extra": null,
          "note": "Derivation from Persian is debated.",
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Italian",
          "refs": "SKT:217; PRT:260",
          "words": [
            {"translit": "gonda, gondola", "gloss": "gondola", "script": null}
          ],
          "script_extra": null,
          "note": "(due to its shape)",
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": "SKT:217",
          "words": [
            {"translit": "gondola", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "Persian",
          "refs": "MON:3102",
          "words": [
            {"translit": "kanand", "gloss": "a tool for tilling earth", "script": "کَنَند"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {"text": "بر گیر کَنَند و تبر و تیشه و ناوه - تا ناوه کشی ، خار زنی گرد بیابان", "poet": "Khojasteh"}
        },
        {
          "id": 8,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT; SYN:46; MON:1395",
          "words": [
            {"translit": "xânî", "gloss": "spring, water pond", "script": "خانی"},
            {"translit": "čâh", "gloss": "water well", "script": "چاه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 2,
          "lang": "Persian",
          "refs": "HRN:194; BQT; ZMA:51; MON",
          "words": [
            {"translit": "xâneh", "gloss": "house", "script": "خانه"},
            {"translit": "ğâneh", "gloss": "house", "script": "غانه"}
          ],
          "script_extra": "خان ، خَن ، گلخن\nخانگاه ، خانقاه\nـ غان ، دامغان",
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "Persian",
          "refs": "MON:465",
          "words": [
            {"translit": "bâlâxâneh", "gloss": "top room, balcony", "script": "بالاخانه", "see": ["Bhergh"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Italian",
          "refs": "LKT:17",
          "words": [
            {"translit": "barbacane, balcone", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "French",
          "refs": "PHN:55",
          "words": [
            {"translit": "balcon", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:467",
          "words": [
            {"translit": "bâlkon", "gloss": null, "script": "بالکن"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 11,
          "lang": "English",
          "refs": "KLN:148; LKT:17",
          "words": [
            {"translit": "barbican, balcony", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": "See AHD for different roots",
          "quote": null
        },
        {
          "id": 15,
          "parent": 2,
          "lang": "Arabic",
          "refs": "PLA:113",
          "words": [
            {"translit": "xandaq", "gloss": "a dug out trench", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "MON:1443",
          "words": [
            {"translit": "xandaq", "gloss": null, "script": "خندق"}
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


## [2026-09-06T14:52:11.265Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat tools/verify_check.py | head -80",
 "description": "List verification dir and check tool"
}
```


### [2026-09-06T14:52:11.330Z] TOOL RESULT

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


## [2026-09-06T14:52:16.636Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '80,160p' tools/verify_check.py; echo ====; ls data/verification/page-21*.json data/verification/page-212.json 2>/dev/null",
 "description": "Rest of verify_check and neighbor files"
}
```


### [2026-09-06T14:52:16.686Z] TOOL RESULT

```
Exit code 1
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
(eval):1: === not found
```


## [2026-09-06T14:52:17.352Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-202.json'))\nprint(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:4000])\n\"",
 "description": "Sample recent verification style"
}
```


### [2026-09-06T14:52:20.012Z] TOOL RESULT

```
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
   "note": "'*gam¹ \"to come\" … «PIE *gʷem- “to go; come” = LIV: 209 f. | Pok.: 464 f.»'; and '«PIE *gʷeH₂- “to go, stride” = LIV: 205 | Pok.: 463 f.»'. Cheung's *ga
```


## [2026-09-06T14:52:52.047Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T14:52:52.085Z] TOOL RESULT

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


## [2026-09-06T14:52:53.914Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','HRN','BRT','ZMA','BQT','SNS','FVF','SKT','PRT','MON','LKT','PHN','KLN','PLA','SYN','AHD','WLD','PHD','NYB','HUB','CHEUNG','ARY','IEC']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:400])\n\"",
 "description": "Refs online metadata"
}
```


### [2026-09-06T14:52:55.476Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
ZMA {"title": "Fereydun Jonaydi, Zendegi va Mohajerat-e Aryaian, Bonyad-e Neyshabur 1374/1995", "kind": "purchase", "url": "https://www.gisoom.com / iketab.com listings (Balkh / Bonyad-e Neyshabur, in print)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": false, "notes": "RE-SEARCH 2026-09: purchase only; no open
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php
FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabeti
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
PRT {"title": "E. Partridge, Origins: A Short Etymological Dictionary of Modern English, New York 1958", "edition_found": "1958 (lending-only copies)", "kind": "archive_restricted", "url": "https://archive.org/details/originsshortetym00part (1958 1st ed.) ; originsetymologi0000part_j9t3 (4th ed. 1966) ; originsetymologi0000part (Routledge 2009) — all lending", "identifier": "originsshortetym00part (al
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 =
PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verific
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
CHEUNG null
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
```


## [2026-09-06T14:53:07.592Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls | head -60; echo ====; ls /home/sfmqrb/git/rishe/data/verification/page-212.json 2>/dev/null && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/page-212.json'));print(json.dumps(d['entries'][0].get('note'),ensure_ascii=False)[:1500])\"",
 "description": "List refs dir, check page 212 verification"
}
```


## [2026-09-06T14:53:08.171Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"schwellen, strotzen\" POK_0*.txt POK_full.txt | head -20",
 "description": "Grep Pokorny for gwhen-1"
}
```


### [2026-09-06T14:53:09.301Z] TOOL RESULT

```
Exit code 1
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
(eval):1: === not found
```


### [2026-09-06T14:53:09.353Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:53:12.688Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la POK*; head -40 POK_02.txt",
 "description": "Inspect POK files"
}
```


### [2026-09-06T14:53:12.731Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb  981836 Sep  4 14:06 POK_01.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1137861 Sep  4 14:06 POK_02.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 1170809 Sep  4 14:06 POK_03.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 3971883 Sep  4 14:06 POK_full.txt
H
^-)e7
G,  O.
^äb-  ,schauen^  ausschauen  nach9? ergäbe  sich,  wenn  man  mit  Zupitza  Gutt.  194  aisl.  köpa  (j)p)  ^starren,  gaffen^, ao-s.  ccepan  ^beobachten,  ausschauen  nach,  sorgen  für,  schützen^,  ablautend ags.  capian  up  ,aufblicken^,  asächs.  upcapen  ,eminere^;  mnd.  kapen  ,gaffen, schauen',  mhd.  kaffen  ds.,  ahd.  (mit  Intensivgemination)  kapfen  ,schauen, spähen'  (daraus  rückgebildet  ahd.  kapf  ,Ort,  von  dem  man  ausschaut, Gipfel')  und  ahd.  üfkepfen  ,aufschauen'  zu  russ.  zahota  ,Sorge',  zabotith  ^a ,sich  sorgen  machen,  sich  bekümmern'  stellen  dürfte.
Alles  ganz  unsicher.  Der  Ansatz  einer  Wurzel,  die  mit  unaspirierter Media  an-  und  auslautet,  hat  von  vornherein  wenig  Wahrscheinlichkeit für  sich  (vgl.  Meillet  Introduction^  173  f.).
WP.  I  530.
gag-f  gög-  , etwas  Rundes,  Klumpiges';  Wort  der  Kindersprache.
Isl.  kaka  , Kuchen',  norw.  und  schwed.  kaka  ,kleines,  rundes  und flaches  Brot',  dän.  kage  , Kuchen'  (germ.  *kakan-)j  wozu  das  Deminutiv ags.  cicel,  cycel  , kleiner  Kuchen'  (engl,  cake  ist  nord.  Lehnwort)  und  ab- lautend norw.  kök  , Klumpen',  schwed.  koka  ,Scholle,  Erdscholle',  mnd. koke,  ahd.  kuocJio  (germ.  *k5kan-)  ,rundes  Brot,  Kuchen^,  dazu  die  Demi- nutiva  ags.  cöecil,  cecil  und  ahd.  kuocheliin)  , kleiner  Kuchen';
lit.  guoge  , Kohlkopf,  Kopf,  Dickschädel',  guogmgas  ,mit  Kopf  versehen', guogiöti  , Köpfe  ansetzen  (vom  Kohl)'.
Aus  germ.  *kakan-  stammen  finn.  kakkg,  läpp,  gakko  , Kuchen',  finn. kakkara  , Erdscholle,  Erdklumpen,  Brot';
über  prov.  katal.  coca  , Kuchen'  (ndd.  Lw.)  s.  Mejer-Lübke^  4734.
WP.  I  530  f..  Kluge  1^  333.
I.  gal-  ,kahl,  nackt';    mit   u-Erweiterung:  Adjekt.  galuo-s,  Subst.  galuä.
Ahd.  kalo  (^^kalua-),  flektiert  kaliuer,  mhd.  kal  ,kahl',  ags.  calu,  engl. calloio  ,kahl,  ungefiedert';  ahd.  calua  ,calvitium';
lett.  gäla,  gäle  f.  (dehnstuf.)  , dünne  Eisdecke,  Glatteis',  gäls  ,eisglatt';
akl.  goh  , nackt',  sloven.  gbi,  russ.  göiyi  ,kahl,  nackt',  cech.  holp  ds., holek  , bartloser  Bursche',  holka  ,Mädchen',  usw. ;  dazu  ksl.  golotb  f.  ,Eis', cech.  holoty  russ.  göioh  f.  , Glatteis';
350
$
baltoslav.  *galuä  f.  ,Kopf'  in:
lett.  gatva  L,   lit.  galvä   (Akk.   gdlvq)  f.  ,Kopf'  (substantiviertes  Adj.)^ apr.  gallä,  Akk.  galwan  ds.;  lit.  galüötas  ,köpfig^  (==  skr.  glävat) -^ aksl.  glava  ,Kopf^  skr.  gldva  (Akk.  glävu),  russ.  ^o-?ova  (Akk.  5rJ^ovu)J skr.  glävat  ,oToßköpfig',  cech.  hlavaty  ,köpfig' ;
die  halt,  und  die  slaw.  Intonation  (gdlvq  :  göiovu)  stimmen  nicht  überein. vgl.    Meillet    Slave    commun^   183,   503;    die    balt.    gestoßene    Intonatioa spräche  nach  Trautmann  77  eher  für  Verwandtschaft  mit  arm.  glu-x  ,Kop(< aus  *ghölu-ko-  (Meillet  Esquisse  36);  dann  müßten  aber  die  germ.  Worte, als  lät.  Lw.  (aus  calvus)  angesehen  werden.  s^
WP.  I  537  f.,  WH.  I  143  f.,  Trautmann  77;  anders  Mühlenbach-Endzeliu I  596  f.,  Specht  Dekl.  85,  132.
2.  gal'  ,rufen,  schreien';  gal-so-  ,Ruf^   ^
1.  Cymr.  galw  , rufen,  vorladen',  mbret.  galu  ,appel'  {*gal-uo-)j  mir.  gall ,Ruhm'  {*gal-no-s]  nur  unsicher  belegt),  wohl  auch  gall  , Schwan';
aksl.  glagoljq,  glagolati  i^gal-gal-) , sprechen',  glagoh  ,  Wort',  russ.  gologoliU ,plappern,  scherzen';  vielleicht  ai.  gargara-h  ,ein  bestimintes  Musikinstru- ment' (=  aksl.  glagoh,  wenn  mit  r  aus   idg.  l,  Meillet  Et.  229;    oder  za  Hi- *ger-   oder   *guer-,    was   beim   Nebeneinander    dieser    Schallwurzeln   nicht  '" auszumachen    ist,    vgl.    von    noch    einer    andern    solchen    ai.    ghai^ghara- , rasselnd,  gurgelnd;  m.  Lärm').
2.  gal-so-  in:
osset.  yalas  ,q)a)vrj%  aksl.  glas^,  russ.  gölosi  , Stimme',  lit.  galsas  »Wider- hall', anord.  kall  n.  ,das  Rufen',  wovon  kalla  ,rufen,  singen',  ags.  callian (engl,  call)  ds.,  ahd.  kallön  ,viel  und  laut  sprechen,  schwatzen',  mit  -II-  aus 'Iz-,  woneben  -Is-  in  anoid.  kalls   n.  , Aufreizung'.
Ob  lat.  gallus  ,Hahn'  (erst  nachträglich  an  den  Galliernamen  angelehntes) vorderas.  Lw.,  ebenso  wie  gr.  y,äXXaiov  , Hahnenkamm'?
Dazu  vielleicht  als  Erweiterungen,  aber  eher  selbständige  Schall  wurzeln:
3.  glag-:
gr.  yXdZct)  ,lasse  einen  Gesang  erklingen'  (*yX(xyi(o);
anord.  klaka  , zwitschern',  ags.  clacu  f.  , Beleidigung^,  ferner  mehrfach mit  Anwendung  auf  dröhnenden,  klatschenden  Schlag  mhd.  klac  , Hände- klatschen, Knall,  Krach,  Riß',  Meckert  ,mit  einem  Knalle  treffen,  bersten', engl,  clack  ,klappern,  rasseln,  plaudern',  anord.  klakk-särr  ,schädlich',  und m.  d.  Bed.  , klatschend  anwerfen,  beklecksen'  mhd.  klac  auch  ,Klecks, Fleck',  mnd.  klacken  , Kleckse  machen'  (nhd.  klecksen,  Klecks  =  ndd. klakks),  anord.  klakkr  ,Klecks,  Klumpen,  Wölkchen';
4.  gal-gh-,  g{a)lagh-  ,klagen,  schelten':
ai.  garhatij  -te,  ved.  3.  PI.  grhate   ,klagt,   tadelt',   garhä   ,Tadel',   gM'
351
Bettler^  av.  gdvdzaiti  ;klagt,  jammert',  osset.  yärzun  , stöhnen',  av.  gi^za, npers.  gila  , Klage';
ahd.  klaga  J^lage',  klagön  _,klagen' ;
mir.  gläm  , Geschrei,  Fluch'  (*glagh-smä) ;
5.  nasaliert  glengh-  :  ahd.  klingan  ,klingen,  tönen'  (ohne  näheren  Zu- gj^mmenhang  mit  lat.  clangor,  gr.  -Akayyr]  , Klang'),  wonehen  mit  germ. Tenuis  ahd.  klinkan  ds.,  engl,  clink,  schwed.  klinka  , klimpern'.
Im  Germ,  außerdem  *kalt-,  *klat-,  *klajp-,  z.  B.  mhd.  kalzen,  kelzen sch\vatzen,  plappern';  afries.  kaltia  , sprechen';  ags.  clatrian  , klappern, rasseln',  nhd.  Klatz  , Schmutzfleck',  bekletzen;  anord.  klapp  n.  , Klatsch, Schlag',  ahd.  /:Zap/ m.  , Geschwätz,  Knall,  Schlag,  Stoß'.
```


## [2026-09-06T14:53:14.783Z] TOOL CALL #12: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/page-212.json /home/sfmqrb/git/rishe/data/verification/page-214.json 2>&1; cd /home/sfmqrb/git/rishe; python3 -c \"\nimport json,glob\nfor p in ['212','214','211']:\n    try:\n        d=json.load(open('data/extracted/batch/page-%s.json'%p))\n        print(p,[ (e['root']['name'],e['root'].get('gloss'),e.get('part')) for e in d['entries']])\n    except Exception as ex: print(p,ex)\n\"",
 "description": "Check neighbouring pages roots"
}
```


### [2026-09-06T14:53:16.330Z] TOOL RESULT

```
ls: cannot access '/home/sfmqrb/git/rishe/data/verification/page-212.json': No such file or directory
ls: cannot access '/home/sfmqrb/git/rishe/data/verification/page-214.json': No such file or directory
212 [('Gwhedh', 'to ask, wish, want', None), ('Gwhen 1', 'to swell, fill', 1)]
214 [('Gwhen 1', 'to swell, fill', 3)]
211 [('Gwer 4', 'mountain', None), ('Gwere 1', None, None), ('Gwere 2', None, None), ('Gwes, Zgwes', 'to extinguish', None), ('Gweye', None, None), ('Gwhder', 'to flow, run', None)]
```


## [2026-09-06T14:53:22.380Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^4\\(89\\|90\\|91\\|92\\|93\\)$\" POK_02.txt | head",
 "description": "Find page 491 markers in POK_02"
}
```


### [2026-09-06T14:53:24.063Z] TOOL RESULT

```
2206:489
2245:491
2267:492
2277:493
```


## [2026-09-06T14:53:26.460Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2206,2290p' POK_02.txt",
 "description": "Print Pokorny pages 489-493"
}
```


### [2026-09-06T14:53:26.508Z] TOOL RESULT

```
489
Uimmel,    Feuersbrunst;    Zorn^,    gaXzdras    m.    , Lichtschein    am    Himmel'; ■tvohl  auch  apr.  gaylis  ,weiß*. WP.  I  665,  Trautmann  75.
g^beio-  :  g^hl-  , Ader,  Sehne,  Band' ;  gHbi-slo-  ds. Cymr.  gi-au  PL  ,Nerven,  Sehnen';
lit.  gijä  , Faden  im  Aufzug  eines  Gewebes',  lett.  dzija  , Faden,  PL Garn';
aksL  H-ca  , Sehne',  russ.  diaL  Mca  ,Kammgarn',  skr.  zica  ,Faden,  Draht, Schnur,  Saite';  die  bsl7-Formen  könnten  auch  zu  gVin9-  gehören.
g'ihislO'',
Arm.  jil  , Sehne,  Schnur';
lat.  fllum  , Faden';
lit.  gysla  ,Ader,  Sehne,  Blattrippe',  lett.  dztsla^  dztksla  ,Ader'  (die Nasalierung  in  zemait.  ginsla  ist  sekundär),  apr.  pettegislo  , Rückenader' ; aber  aksl.  züa^  russ.  i2?a,  skr.  zila  usw.  ,Ader,  Sehne'  sind  Neubildun- gen zu  zi-ca,  s.  oben.
WP.  I  670,  694,  WH.  I  497  f.,  Trautmann  87,  90.
g^bel-  ,wollen'.
Gr.  d-slü)j  i-&€lo)  (zum  Präfix  s.  W-,  ö-Part.)  ,will,  wünsche',  ablautend (pakiC^ei '  d'eXei  Hes. ;  ijiL^dg)sXog  ,heftig' ;
anord.  gildra  f. ;  gildri  n.  , Falle',  gilja  ,verlocken',  aschwed.  gicel- skaper  , Unzucht';
aksL  zeleti,  ^elatij  iter.  russ.-ksl.  zalati  ,wünschen',  aksl.  zelja  , Wunsch, Sehnsucht'  (auch  ,trauern'  und  ,Trauer'  durch  Anlehnung  an  ^aU  , Schmerz' von  *^"eZ-  ,stechen').
WP.  I  692.
gbuel-  ,sich  krümmen,  von  der  geraden  Richtung  abbiegen  (auch  geistig und  sittlich)  u.  dgl.';  ghuelo-s  ,gekrümmt'.
Ai.  hvdrate  ,biegt  von  der  geraden  Richtung  ab,  macht  krumme  Wege', hvdlati  ,gerät  auf  Abwege,  strauchelt,  irrt',  juhuränd-h  , mißglückend', vihriUa-h  , schadhaft,  krank',  hrunäti  ,geht  irre',  Partiz.  hrutd-y  geneuert hvftd-',  hürchati  ,geht  schief,  gleitet,  schwankt,  fällt';  hvdras-  n.  ,Krüm- mung',  hvard-  m.  , Schlange',  vihrüt-  f.  ,Art  Schlange  oder  Wurm' ;
av.  zbardmna-  ,krumm  gehend',  zharad-a-  n.  ,Fuß  daevischer  Wesen', zharah-  n.  ,Hügel',   zürah-  n.  ,Unrecht,  Trug',   npers.  zur  , falsch;  Lüge';
gr.  q)aXl7tT€L'  uwqaivei  Hes.,  (paXög  , stammelnd,  töricht'  Hes.  und  wahr- scheinlich (pdXoQ  m.  ,hornartiger  Vorsprung  am  Helm',  vermutlich  g)oAxdg, Beiwort  des  Thersites  B.  217,  etwa  , krummbeinig' ;   vielleicht  auch  dTto-
L
490  •
(fcblLog   ,trügerisch'    (ö-stufig),    q)fjlog    ^betrügerisch^,    q)rjXi^T7jg    ;Betrüger',  v? cprjXötJ  (dor.  cpaXöcü)  betrüge';  ^^';
lat.  fallö,  -ere  ^täuschen,  betrügen;  unwirksam  machen;  sich  entziehen-  ^'-^ unbemerkt  bleiben'  (,*krumme  Wege  machen;   ausbiegen';    *ghujnö,  vgl.  - ai.  hrunäti)'j  '4-  -
lit.  nuozvelnüs  ,abschüssig'j  zvalüs  ^geschickt;  flink,  behend'  (,*sich leicht  biegend');  ablaut.  i^vünas  ,schräg,  schief  {*g'hul-),  pa^il-ti,  -au ,sich  neigen',  ir^/^wo^t  , schaukeln,  schwanken';  prazulnas  (*ghul-)  ,schräge, schief,  paMnus  ds. ;  atiülas,  -us  ,schroff,  hart,  unhöflich,  unbarmherzig' u.  dgl. ;
lett.  zveVu,  zveVu,  zvelt  ,wälzen,  fortbewegen,  umwerfen ;  schlagen',  refl. ,sich  schwerfällig  fortbewegen,  sich  wälzen,  umfallen',  zvalstities  ,wanken, schwanken',  zvatns  ,sch wankend';
aksl.  z^l^  ,böse,  schlimm',  skr.  zäo  (f.  zlä)^  russ.  zoi  (f.  zia)  ds. ;
vielleicht  *ghu-el-  aus  einem  gheu-  ,schief'  erweitert;  vgl.  ^ghu-er-  in lit,  ziirU  ,eine  Rankenpflanze'  (*g^ur-lo-),  gv.  ^egfiog  m.  ,Feigenbohne^ (*guher-mo-).
WP.  I  643 f.,  WH.  I  448,   Trautmann  372  f.
•'^^ ' ghuelg-  ,anblicken'?  ^-^'<
Gr.  d-sXyo}   ,bezaubere,   umschmeichle'   (unwahrscheinlich   oben  S.  247);
lit.  ^velgiüj  zvelgti  ^anblicken',  Iterat.  zvalgaUj  zvalgyti  und  zvilgis  m. , Blick',  ^vUgiu,  ^vilgUi  ,kurz  hinblicken'.
WP.  I  644,  Trautmann  374,  Schwyzer  Gr.  Gr.  I  302.  .v4.^-
^hemh-  , lustig  springen,  hüpfen'??  "^
Gr.  äd-sixßovaa '  äy.oXaaraivovaa  (,ausgelassen')  Hes. ;
mhd.  gampen,  gumpen  , springen',  gampel,  gumpel  , lustiges  mutwilliges Springen,  PossenspieF,  gümpelj  nhd.  Gimpel]  mit  oberdeutscher  Lautver- schiebung mhd.  gampf  m.  ,das  Schwanken';  norw.  dial.  gimpa  , wippen, schaukeln',  gamp  m.  ,großer  schwerfälliger  Kerl,  plumpes  Pferd'.
Eine  kürzere  Wzf.  guhem-  vielleicht  in  aisl.  gaman  n.  ,Freude,  Lustig- keit, Wollust',  ahd.  gaman  n.  ds.,  usw.  "       ^
WP.  I  678  f.  ^^
ghuen-    ,tönen',    ghupno-s    ,Ton':    Erweiterung    von    ghau-,     s.   Persson Beitr.  191. kxm.  jain  (ghuon-ii-),  i-St.  , Stimme'  (mit  t- Epenthese) ; alb.  tosk.  Z6  , Stimme',  geg.  zd  (<  *ghuono-s)'j
russ.-ksl.  zvbnjuj  zvhnki  ,klingen,  tönen',  russ.  zvenith,  acech.  zvnieti, öech.  zniti,  altpoln.  tozniec  ds.,  ablaut.  aksl.  zvom  ,Ton',  sl.  zvqn  , Glocke',
491
hnlg'  zv^n^  ,Klang,  Schall',  zvznecb  , Glocke',  skr.  zvono,  russ.  cech.  zvon, poln.  dzwon  , Schall,  Glocke^
Baltoslav.  Wurzelerweiterung  gbueng-:
lit.  zvengiu,  zvengti  ^wiehern',  su-zvihgu,  -zvingti  ,in  Wiehern  ausbrechen^, zvangüs  ,laut,  schallend',  svdngu,  zvangeti  ,rasseln,  klingen,  klirren',  lett. zviegt  , wiehern';
aksl.  zv^go  ,verkünde',  russ.-ksl.  zvjagu  ,singe,  schwatze',  russ.  dial. zvjagü,  zvjach  ,bellen'.
Slav.  Wurzelerweiterung  gbuenk-:
aksl.  zv^kz  m.  ,Klang',  zveknqti  , tönen',  zvecati  , rufen',  skr.  zvek  ,Klang'^ poln.  zwi^k,  diwiek  , Klang,  Schall';  mit  Ablaut  aksl.  zvok^  ,Klang',  russ. zvuk,  cech.  zvuk  ,Ton,  Laut,  Schall';
Slav.  Wurzelerweiterung  gbuent-:
bulg.  zv^ntja  ,schallen,  klingen'.
WP.  I  642,  Trautmann  374.
f.  g^hen-  ,schwellen,  strotzen.  Fülle';  g^hono-s  ,üppig,  reichlich'.
Ai.  a-hand'  , schwellend,  strotzend,  üppig',  ghand-  , dicht,  dick',  m. ,kompakte  Masse';
npers.  ä-gandan  , anfüllen',  äganis  ,voll';
arm.  yogn  ,multum'  (Präp.  i  +  *o-g^hon-  oder  *o-g^hno-,  im  Präfix  o- dem  ar.  ä-  nächststehend) ;
gr.  sid-svi^g  ,reichlich,  in  Fülle',  Hes.,  edd^svsoj  ,gedeihe',  eid-iveia  , Fülle, blühender  Zustand',  dehnstufig  ion.  svdr]vi^g  , reichlich,  in  Fülle',  ion.  att. sid-rivso)  ,gedeihe,  bin  in  Blüte  und  Kraft',  svd-rjvla  f.  ,Fülle';  o-stufig IloKvcpövrrjg  =  noXvKTT^TTjg;  KXsocpövrrjg^  usw.,  red. -stufig  q)aväv '  d^eksiv Hes.,  wohl  eigentlich  ,geil  sein' ;
lit.  ganä  ,genug',  ganeti  ,genügen',  gandeti  ,genug  haben',  lett.  gana ,genug';
aksl.  gonejetb,  goneti  ,genügen',  Denomin.  von  "^gona  =  lit.  ganä]
ob  hierher  gr.  ^cpavog,  lücpvog  n.  ,reichlicher  Vorrat,  Reichtum',  äcpvsiog , begütert'  {cp  und  der  Vokalvorschlag  aus  der  vokallosen  Form  {a)(fv- oder  *sm-g^h(e)n-'>),  auch  Ttao-divog  , Jungfrau'  (leibliche  Fülle?)?
WP.  I  679,  WH.  I  479 ;  Trautmann  77  f.
2.g^hen-(p)-  ,schlagen'.
Nominalbildungen:  g^höno-s  , Schlagen',  g^hn-to-s  ^geschlagen', g^hn-ti-s  und  g^hn-tia  (?)  , Schlagen',  g"hen-tel-  .Schläger',  g'ihen-tuo-s ,occidendus'.
Ai.  hdn-ti  (jünger  thematisch  hanati)  , schlägt,  trifft,  erschlägt,  tötet', 3.  PL  ghn-dnti,  Im^.  ja- hi,  Opt.  Jian-yät,  ghnlta,  VerL  jaghdna]  jaghanväs.
492
Gen.  jaghn-us-ah,  Pass.  hanyäte,  Partiz.  hatd-  ^geschlagen,  getötet'  (==  ay.*^ jata-j  gr.  -cpatog),  hdntva-h  ;Zu  schlagen,  zu  töten'  ( :  av.  jq^iva-^  aksl  .^ 0gtva)j  vrtra-hdn-,  Gen.  -ghTi-dh  (=  av.  vdrd^ra-jan-,  Gen.  -y-no)  ,<ien  Wider-  S stand  niederschlagend',  ghand-  ^erschlagend,  m.  Knüttel,  Keule'  (==  g^^  „- ävÖQO-q)6vogj  lett.  gans),  sam-hd-t  ,Schicht',  hati-h  ,das  Schlagen,  Schlag^ ^ Multiplikation'  (:  gr.  ÖLcpaai-og,  av.  -jaüi-,  anord.  gudr,  gunnr),  hatyä  (spät) ,Tötung'  (:  ahd.  gundea,  lit.  dial.  ginciä),  hantdr-  ,wer  einen  schlägt  od( tötet'  (=aksl.  z§teljb)',  von  der  schweren  Basis  ai.  hanitum  (spät!)  und^fÄö^ ,tötend',  m.  ,Schlag,  Tötung,  Vernichtung',  ghätayati  ,tötet';
aiv,jain-ti  (=  ai.  hdnti-)  ,er  schlägt,  trifft,  tötet',  Imp.  Jaidi,  1-  Sg.  Met m'-ywe  ,ich  schlage  nieder',  Opt.  paiti-ynUa  (=  ai.  ghnlta)  ,er  möchte^ kämpfen  um',  Partiz.  jata-  (=  ai.  hatd-,  s.  oben),  jqd-wa-  ,occidendu8'J Partiz.  Perf.  Akt.  jaynvä,  npers.  ajanam  ,ich  erschlug  =  besiegte',  3.  SgJ aja^""^'^  av.  Jana-  ,schlagend',  jantar-  ,der  schlägt,  tötet',  Jan^i-  f.  ^( Schlagen,  Erschlagen',  -jaiti-  (als  2.  Kompos.-Glied)  ,das  Schlagen'  (=  affl Äa^i-);    Vdrd&rajan-    ,den  Widerstand   niederschlagend'  =  ai.  Vrtra-hani^^^
arm.  ^an,  Gen.  gani  {*g^he-n)  ,Schläge,  Prügel',  ganem  ,schlage,  prügle'^ jin  ,Stock'  (*gyihen-),  jnem  ,ich  schlage'  (über  *jinem  aus  ^g^henö  =  hdnai lit.   genilj  aksl.   ieng),   jnjem  ,vernichte,    reinige'    (aus   ^g^heniö  =  ^stVöjS lit.  geniü)]
gr.   -^ftVw    (*gVien-iö  =  arm.  Jnjßm  ,töte',   alb.   gjanj   ,jage',   lit.   genii ,ästle  ab')  ,schlage',  d-evu),  e-d-eiva-,  redupl.  i/rfi^yo)' , tötete',  necparaLi  -<p(xr6g\ in   hom.  dcQr]l-q)arog   (=  ai.  hatd-h),   auch   in  dlcparov  öiq)daLOv  Hes.  d. , doppelt'  (,Mal'  =  ,Schlag',  ebenso:)  ÖL-cpaai-og  (:  ai.  hati-  s.  oben);  q)6vog'^ ,Mord'    (=  russ.   gon),    cpovr]    ds.,    g)ovsvg    , Mörder',    dvdgocfövog    ,Männer mordend'  (s.  auch  Boisacq  unter  q)0iv6g)]
alb.  gjanj  ,jage,  verfolge'  (*guhen{o)]
lat.  defendö,  -ere  , abwehren,  verteidigen',  offendere  ,anstoßen,  beleidigen', infensus  (Partiz.  eines  *infendö)  , feindlich';
air.  gonim  ,verwunde,  töte',  Perf.  1.  Sg.  gegon,  3.  Sg.  geguhi]  guin ,Wunde' ;
anord.  gudr,  gunnr  f.  (=  ai.  hati-),  as.  güdea,  ags.  güp  (*gunpjö  =  ai. hatyä  bis  auf  den  Akzent)  , Kampf,  Schlacht',  ahd.  gund-fano  ,Kriegs- fahne';  anord.  gandr  , Stock',  Schweiz,  gunten  ,eine  Art  Keil';  norw.  dial. gana  ,die  Äste  an  Bäumen  abhauen'  wie  lit.  geneti]
lit.  genü  (=  aksl.  zeng,  ai.  hdnati,  arm.  jnem)  giftti  ,treibe  (Vieh  auf die  Weide)',  lett.  dzenu-,  dzit  ds.,  schwere  Basis:  geniü  (==  d-eivo))  gene-ti ,abästeln'  und  ginü,  ginti  ,wehren,  schützen'  (ginti :  gmti,  giütas :  gintas =  ai..  hatd :  ghätd-) ;  zu  genü  Iterat.  ganyti  ,Vieh  (treiben  =)  hüten, weiden';  lit.  gänas,  let.  gans  ,Hirt'  (=  ai.  ghand-),  gani  m.  PI.  ,Weide', dehnstufig   lit.   naktl-gonis   m.   ,Nachtschwärmer' ;    lit.   genys,    lett.   dzenis
493
Specht^,  lit.  dial.  ginöiä  (=  ai.  hatyä),  gificas  , Streit'^  giilklas  m.  , Waffe' {*qintlaSj  vgl.  aksl.  ^lo  aus  *gindla')j  üganüs  ^heilbringend'  (lit.  gdinioti ist  Iterativum  zu  ginti ;  lett.  dzenis  ,das  in  der  Gabel  der  Pflugschar  einge- klemmte Holz',  dzenulis  , Stachel'  (vgl.  zur  Bed.  unten  aksl.  ^^lo  , Stachel') ;
aksl.  zeng,  g^nati  ^treiben'  (wie  lit.  genü),  Iter.  gonjq,  goniti  ^treiben, iao'en',  wovon  wieder  poganjati  ^verfolgen' ;  russ.  usw.  gon  ^Treiben,  Jagd' (=s  q)6vog),  cech.  uhona  , Verletzung,  Schaden',  serb.  prijegon  ,Kampf' (dazu  vielleicht  klr.  honöba  ,Belästigung,  Plage',  sloven.  gonöba  , Schaden, Verderben',  ugonoha  , Vernichtung,  Untergang');
aksl.  ^hnjg,  S^ti  (serb.  zeti,  also  schwere  Basis)  ,ernten',  z§tva  (serb. Btva)  f.  ,Ernte'  ( :  ai.  hdntva-) ;  auch  zdo  (*z§dlo)  n.  ,StacheP,  poln.  zqdio ds.,  russ.  zäh  , Stachel,  Schneide  eines  Messers,  einer  Axt' ;  slav.  *gen-tel- m.  , Schnitter'  in  aksl.  ^eteljh  (=  ai.  han-tdr  ,wer  schlägt,  tötet');
hitt.  ku-en-zi  , tötet'  (=  ai.  hdnti),  3.  PI.  ku-na-an-zi  (kunanzi) ;  vgl.  ai. ghndnti  (*g1thn-enti).
WP.  I  679  ff.,  WH.  I  332  f.,  Trautmann  85  f.
gbuer-  , wildes  Tier'.
Gr.  d^T^Q,  -dg,  m.  spät  f.  (^fJQsg,  &rjQCüv  =  ostlit.  ^veres,  zvery,,  Schwyzer
Gr.  Gr.  I  424),  lesb.  gpij^,  hom.  OfjQSQj  thess.  qjeig  {TiecpeLQ&y.orveg  =  xeS^r]-
gaycöreg,  OiXöcpsiQog)  ,Tier'; lat.  ferus,  -a,  -um  ,wild,  wildwachsend,  -lebend'  {*ghuero-s)\ mit  Überführung  in  die  z-Deklination  (nach  dem  Akk.  Sg.  PL  -t»,  -i  =  m,
J,  -^s)  lit.  Iverxs  m.  f.,  lett.  zmrs  m. ;  apr.  Akk.  PL  siolrins ; aksl.  zv^rb  ,wildes  Tier',  sloven.  zvp,  acech.  zvef  m.  f.,  russ.  zverh; i      Substantiv.  Adjektiv  lit.  Sverienä  f.,  russ.  zverina  , Wildbret',  zu  lat.  carö ferina  ds. WP.  I  642  f.,  WH.  I  487  f.,  Trautmann  374  f.
g^her-    ,heiß,    warm';    Adjektiv    g^hermo-    und    g"hornio-    ,warm'    und Substantiva    g^heros-,    g^boros-  n.,    g"bormo-    n.,   g^hormiiä    f., g^horno-s,  g^hrno-s,  g^hortiiä  und  ^hr^-ns-o-s  ,Hitze,  Wärme, Glut,  Brand',  usw. Ai.   hdras-\  n.   ,Glut'   (=  gr.  d-eoog,  arm.  jer),   ghfnd-   m.  ,Glut,  Hitze' (=  lat.  fornus,   aksl.   g'>^n^),   gh^nöti   ,glüht,   leuchtet',   gkarmd-  m.   ,Glut, Hitze',  av.  gardma-  ,heiß',  n.  , Hitze,  Glut',  apers.  in  garma-pada-  Monats- name,  etwa  ,*Eintritt'  der  Hitze'  (=  lat.  formus,  dt.  luarm ;    apr.  gorme) ; arm.  jer  ,Wärme,  schönes  Wetter ;    warm',  jernum  , wärme  mich',  jerm jWarm'  (=  gr.  -S'SQixög ;  vielleicht  als  *gV:her-mn-os  Ableitung  vom  wew-St.  :) jermn  Gen.  jerman  , Fieber'  (auch  gr.  ^ig^ia   f.  ,Wärme'  ursprünglich  ein Neutrum?);
494
thrako-phryg.   germo-  ,warm^   (in  vielen  ON:   Jokl   Eberts  Reallex.  iQi 142 f.,  13,  285,  292;,  294),  kappadok.  garmia(s)  ,Stadtname  auf  der  Peutinge, sehen  TafeF  {a  =  idg.  o);
```


## [2026-09-06T14:53:44.211Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG kan ===\"; grep -n \"^\\*kan\\|\\*kan[0-9¹²³]\\| kan- \" CHEUNG.txt | head -20",
 "description": "Grep Cheung for kan"
}
```


### [2026-09-06T14:53:44.271Z] TOOL RESULT

```
=== CHEUNG kan ===
15356:*kanl 229 
15413:*kan! ‘to throw, place, put; to destroy’ 
15414:*AVESTAN: (+ *ni-) ? Y Av. ni kan- ‘to bury’ || (+ *ui-) YAv. vikan- ‘to destroy, ruin’ 
15518:232 *kan2 
15521:*kan? ‘to fill’ 
15552:*kanH! ‘to dig’ 
15588:*kanH2 233 
15629:*kanH? ‘to love, take pleasure in’ 
15630:*AVESTAN: kan- ‘to love, take pleasure in’, -cinah- (in cmpds.) ‘desire, love for’ 
16167:*MISC: Par. kas ‘eyebrow’ (kas kan- ‘to pull, stretch, contract’ < NP) 
16277:*kan’). Perhaps, the Chor. form derives from the present stem *ham-krnta- of 
28473:*kanH! would be a present formation (IE *kenH'-) of *xaH, as assumed in LIV: 344 
28543:*MISC: Par. xist kan- ‘to rise, jump’ 
33508:*kan-, 232 
56314:*kan! (s.v.), *marc, *Hrais 
56322:*kanH', *kap/f, *Hrad, *xaH 
56597:*kan’, *parc, *parH' 
58218:*kan', *kauz’, *mai9H’,
```


## [2026-09-06T14:53:44.967Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN page markers 193-195 ===\"; grep -n \"^19[3456]$\" HRN.txt | head",
 "description": "Find Horn page 194"
}
```


### [2026-09-06T14:53:47.574Z] TOOL RESULT

```
=== HRN page markers 193-195 ===
```


## [2026-09-06T14:53:52.367Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '15505,15640p' CHEUNG.txt",
 "description": "Print Cheung kan entries"
}
```


### [2026-09-06T14:53:52.418Z] TOOL RESULT

```
Ó In many Iranian languages the roots *kan' ‘to throw’, *kanH! "o dig’ and *kan? 
‘to fill’ forms are homonymous and therefore often show mutual interference. For 
instance, the prefixed forms in *ni- ‘to bury’ may, alternatively, derive from *kan?. 
*PIE — > LIV: – | Pok.: 

*REFERENCES: Christensen, Contributions I: 58 f., 72; IFL II: 222b f. Lambton 1938: 42b; Abaev, 


Slovar’ П: 225, 366 f., 198, 196 Ё; EVS: 48b; Nyberg П: 111b; DKS: 251a, 307b; WIM II/1: 78; Asatrian 
— Livshits: 86; Cheung 2002: 78, 243; Lecoq 2002: 121 ff., 618, 665 (passim); NEVP: 56 


232 *kan2 


*kan? ‘to fill’ 
*MIDDLE PERSIAN: (+ *pati-) MMP phykn- ‘to fill, enter, penetrate’ || (+ *ham-) 


MMP hnen- ‘to fill in^ = DMMPP: 275a, 181a 

Pres.: SUBJ. 3sg. MMP phykn’d; Partic.: perf. pass. MMP phygqnd, "phyknd || (+ *ham-) Partic.: pres. 
MMP hngn’n, perf. pass. MMP hngnd 

*PARTHIAN: (+ *ä-) ’gn-, "gn- ‘to fill’ = Ghilain: 55 | DMMPP: 29b f. 

Pret.: IND. 3sg. "gnd (M2 II Vii,21(132)); Partic.: perf. pass. "end, end 

*SOGDIAN: (+ *4-) MSogd. "kn ‘to fill’ 

Impf.: IND. 3pl. MSogd. m’k’nd (M118iV.5) 

*CHORESMIAN: (+ *upa-) bkn- ‘to fill, load’, bkny- (intr./pass.) ‘to become full’ 
= Samadi: 20 

*NWIR: (+ *4-) NP agandan/agin- ‘to fill, stuff’, (caus.) NP aganidan/agan- ‘to stuff, 
fill, cram’ 

*NEIR: (+ *abi-) Oss. I. evgenyn/evgeed, D. evganun/zvgad ‘to pour in, fill, out; 
to draw’ 


9 Several Iranian languages point to the existence of a separate root *kan- ‘to fill’. 
*REFERENCES: Abaev, Slovar’ I: 201; Cheung 2002: 166 


*kanH! ‘to dig’ 

*AVESTAN: YAv. °kan- ‘to dig’ || (+ *api-) ‘to fill out by digging, fill (a pit)’ || + 
*aua-) ‘to establish by digging, excavate’ || (+ *us-) ‘to dig out’ || (+ *para-) ‘to dig 
around’ || (+ *ni-) ‘to dig in’ = Liste: 14 

Pres. {1} athem.: IND. 3sg. YAv. uskonti (V 3.12), INJ. med. 3sg. YAv. auuakanta (V 15.39), OPT. 3sg. 
Y Av. aipi.kaniiat (V 14.6); Pres. {2} them.: OPT. 25р. YAv. auua.kanöis (V 17.5, V 17.7); Partic.: perf. 
pass. Y Av. nikanta- (V 7.43, V.3.12) 

*OLD PERSIAN: ka(n)- ‘to dig’ = Kent: 178b 

Partic.: perf. pass. ka(")tam <k-t-m> (DSf 25); Inf.: ka"tanaiy <k-t-n-i-y> (DZc 9, XV 21); Pass.: impf. 
IND. 3sg. akaniya <a-k-n-i-y> (DSf 24, DSf 28, (?) DZc 10) 

*MIDDLE PERSIAN: MMP qn- ‘to dig (up); to raze, destroy’ (partially from *kan'), 
BMP kn- (HPLWN-) /kan-/ ‘to dig (out); engrave’ || (+ *fra-) MMP prgnd’n (ppp., 
pl.) ‘built? > DMMPP: 206a, 278b 

Partic.: perf. pass. MMP qnd; Pass.: pres. IND. 3pl. MMP qnyyhynd 

*PARTHIAN: kn- ‘to dig (up); to raze, destroy’ (partially from *кап!) = Ghilain: 206a 


| DMMPP: 206a 
Partic.: perf. pass. knd 


*KHOTANESE: OKh. kamggan- ‘to dig’ (< old intens.) = SGS: 20 

*SOGDIAN: BSogd. kn- ‘to put out (eye)’, BSogd. kn-, CSogd. qn-, MSogd. kn- ‘to 
dig’, SSogd. knöh, BSogd. knöyh, CSogd. q0(-) ‘town’ || (+ *us-) BSogd. skn- ‘to 
incise, engrave’, BSogd. ’sk’’n ‘line’ (Benveniste, TSP: 197 ad 191-2) || (+ *ш-) ? 
MSogd. укуп ‘to dig ош” or rather ‘to destroy’ (whence *kan!) 


*kanH2 233 


Pres.: IND. 3sg. BSogd. knt’, IMPV. 2sg. CSogd. qn’; Impf.: IND. 3sg. MSogd. kn’skwn ‘he was 
digging’; Inf.: pret. BSogd. knt || (+ *us-) Inf.: BSogd. skn’t|| (+ *ui-) Inf.: ? MSogd. апуу ykynyy (BBB: 
33) 

*CHORESMIAN: kn- ‘to dig; to break out (of teeth)’ || (+ *us-) m/’sk’ny- ‘to carve’ 
c» Samadi: 102, 8 

*BACTRIAN: (+ *ni-) vakav- ‘to dig’ = S-W, Bact.: 207b 

*NWIR: Widely attested: NP kandan/kan-, Kurd. (Sor.) kandin/kan-, Zaz. kendis/ 
kenen-, Awrom. kannäy/kan-, Gz. kän-/känt, Gur. (Kand.) kän-/-kän-, Abyan. 
kanda/kan-, Abz. kända/-ken- (-kon-) Ham. kendän/ken-, Isfah. känän/Kän-, Khuns. 
ken-/kend, kena, Nn. kent/r-kin-, Qohr. kanda/kin-, Siv. kén-, k(y)en-/künd, kend-, 
Tal. kande, Tr. kanda/ken- ‘to dig (out)’, also Tr. kända ‘sheep shelter’ (Lecoq 2002: 
466) || (+ *us-) NP sikinah, iskinah ‘(wood-)chisel’ 

*NEIR: Pash. kan-/kandol, (Waz.) (pret.) wu-kind, Wa. ksın-/kot, Yghn. kan-/kánta, 
Sh. Cán-/Cint, Rosh. &än-/änt, Bart. éan-/Cant, Yzgh. Kan-/Kont ‘to dig’, Oss. I. kaend 
‘building’ || (+ *ni-) Oss. D. nik zd ‘carve, cut’ 

*SANSKRIT: khan’ ‘to dig’ (RV+) > EWAia I: 445 

0 See also *kan!. The IE reconstruction with *-H,- is based on the Skt. and Phrygian 
evidence. The initial kh- of Skt. khan! is odd: contamination with kha- (n.) ‘canal, 
opening, hole’, kha- (f.) ‘source, spring’ is usually assumed (cf. EWAia I: 446, fn.). 
In Iranian there is no evidence of a initial laryngeal. 

«PIE ? *kenH,- ‘to dig’ = LIV: 344 | Pok.: 534 

*IE COGNATES: ? OPhr. keneman ‘a monument or a part of it’ (Lubotsky 1988: 15) 
*REFERENCES: KPF I: 145a; EVP: 32 f.; КРЕП: 218; IIFL II: 526a; Abrahamian 1936: 117, 130; Abaev, 
Slovar’ I: 579; Andreev — Pe&éereva: 270; MacKenzie 1966: 99; Abaev, Slovar’ П: 196 f., 183 Ё; EVS: 


26b, 48b; WIM I: 69; WIM II/1: 78; WIM III: 111; Werba 1997: 281 Ё; Paul 1998: 303a; Steblin- 
Kamenskij 1999: 221; Cabolov 2001: 533, 507; Lecoq 2002: 121, 123, 126, 444 (passim) 


*kanH? ‘to love, take pleasure in’ 
*AVESTAN: kan- ‘to love, take pleasure in’, -cinah- (in cmpds.) ‘desire, love for’ 


= Liste: 14 

Pres. ia-: IND. 15р. ? OAv. Капа (Y 33.6); Perf.: IND. 3sg. YAv. cakana (H 2.11), 3р1. OAv. caxnarə (Y 
44.13). © The interpretation of OAv. kaiiä as pres. (Humbach 1950: 541), being related to Skt. käyamäna-, 
is rejected by Kellens — Pirart 1990: 229, s.v. kan. 


*OLD PERSIAN: aspa-cana <a-s-p-c-n-a> nom. sg. PN lit. ‘loving horses’ (DNd.1)
```


## [2026-09-06T14:54:01.286Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^53[3456]$\" POK_02.txt POK_03.txt | head",
 "description": "Find POK page 534"
}
```


### [2026-09-06T14:54:03.849Z] TOOL RESULT

```
POK_02.txt:2902:533
POK_02.txt:2938:535
```


## [2026-09-06T14:54:06.002Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2902,2940p' POK_02.txt",
 "description": "Print POK 533-535"
}
```


### [2026-09-06T14:54:06.050Z] TOOL RESULT

```
533
Ablautneubildung  und  anlaut.  s-  von  der  Wurzel  sker-  hierher  auch  andd. ofskerran  starkes  Verb  , abkratzen*,  ahd.  scerran,  mhd.  scherren  starkes  Verb kratzen,  schaben*,  Intensivbildung  *skarzön  in  norw.  skarra  ,einen  schar- renden Laut  hervorbringen',  mnd.  mhd.  scharren  , kratzen,  scharren*, schwed.  skorra,  mnd.  schurren  , einen  scharrenden  Laut  geben*.
Der  Wurzelvokal  ist  a ;  der  Intonationsunterschied  zw.  Lit.  und  Slav. bleibt  noch  zu  erklären.
WP.  I  355f.,  WH.  I  173f.,  Trautmann  118f.
kas-,  kas-no-  ,grau*.
Lat.  cänus  (^cas-no-s)  ,grau,  aschgrau*,  pälign.  casnar  ,senex*,  ahd.  hasan ,grau  glänzend,  poliert  fein*;  sabin.-lat.  cas-cus  ,alt*  (ursprüngl.  , altersgrau') ;
anord.  hgss  (^kas-iio-),  ags.  hasu  , graubraun*,  mhd.  heswe  ,bleich,  matt*.
Dazu  die  Benennung  des  Hasen  (vgl.  russ.  särjdk  , grauer  Hase*  :  seryj ,grau*):
ai.  sasd-  m.  (aus  *sasd-),  afghan.  soe,  Pämird.  süi]  cymr.  ceinach (-acÄ- Erweiterung  eines  *cein  =  *kasnl  , Häsin*,  Pedersen  KG.  I  86); ahd.  haso,  mit  gramm.  Wechsel  ags.  hara^  anord.  heri  (eine  Ablautsneu- bildung mit  germ.  e  scheint  norw.  schwed.  mdartl.  jase  =  anord.  *hjasi), apr.  sasins  m.  ,Hase',  sasin-tinklo  , Hasengarn*,  ON  Sassenpile  , Hasenberg'.
Eine  Erweiterung  der  Stämme  *kasen-  (:  kas-n-o-)  und  *kaseu-,  kasou- (:  kas-u-o-)  mit  Formans  -dho-  und  Schwundstufe  der  Wurzelsilbe  wird  in gr.  ^av&oq  , blond,  braun'  aus  "^ks-en-dho-  (falls  ^av-  Verquickung  von  *^ev- und  *Ja-=*?w-)?  und  ^ovd-ög  angeblich  ,goldgelb',  falls  aus  *ks-ou-dho-, angenommen,  aber  sehr  zweifelhaft.
WH.  I  156,  Hofm.  Etym.  Gr.  Wb.  221,  Trautmann  330,  Schwyzer  Gr. Gr.  I  329.
käs-,  k9S'  , zurechtweisen,  anweisen';  nur  arisch  und  armenisch.
Ai.  sästi,  1.  PI.  sismdh  , weist  zurecht,  züchtigt,  herrscht,  befiehlt,  belehrt', Partiz.  Aor.  si$dnt-  , unterweisend*,  sistd-  , zurechtgewiesen,  angewiesen, unterwiesen*  (jünger  sästa-,  wie  av.  sästa-)]  av.  sästi  ,heißt,  lehrt',  Opt. sisöit,  a-slHa-  ,verheißen* ;  ai.  sästdr-  , Bestrafer,  Gebieter*  =  av.  sästar- , Gebieter,  Fürst',  mpers.  sastär  ,Herrscher*,  ai.  iästrd-  n.  , Anweisung, Belehrung,  Lehrbuch',  av.  säx'^an-  n.  , Lehre*,  säsnä  , Lehre,  Gebot*,  ai. sisti-  f.  , Bestrafung,  Befehl*  (jünger  sasti-)^  sisya-  ,zu  unterweisen',  m. ,Schüler' ;
arm.  säst  ,Vorwurf,  Drohung,  Strenge,  Autorität',  sastem  , drohe,  schärfe ein,  gebiete',  sastik  , heftig'  (alles  iran,  Lw.  ?).
WP.  I  358,  WH.  I  179.
534  •
1.  kat-  , flechtend   zusammendrehen,   zu   Ketten,    Stricken,    Hürdengeflecht'.
Lat.  catena  , Kette'  (*cates-nä),  cassis,  -is  ,Jägergarn,  Netz'  (wegen  caUna eher  =  *kat-s-is  als  *kat-ti-s-  vielleicht  auch  casa  ,primitive  Hütte'  (xlt- ^prünglich  aus  leichtem  Geflecht;  wohl  dial.  aus  *catiä,  wie  osk.  Bansae aus  Bantiae))
vielleicht  hierher  caterva  f.  ,Hau£e,  Schar,  Truppe'  (*kates-ouä),  umbr. kateramu,  caterahamo  ,catervamini,  congregamini',  doch  s.  unten  unter  1.  A;e^.
cymr.  cader  ,Festung'  (nur  in  ON),  air.  cathh^  , Stadt';
vielleicht  aisl.  hadda  f.  ,Ring,  Henkel,  Bügel' _(*Äa;>i/)ün  :  catena;  recht unsicher),  wohl  ags.  heador  n.  ,Einschließung,  Gefängnis';
ksl.  kotbCh  ,cella,  Nest',  russ.  koty  PL  ,Fischwehr,  Fischzaun',  skr.  kdt, (dial.)  kbtac  ,kleiner  Stall';  dial.  ,Art  Fischfang'  usw.  und  bulg.  kötara, kötora,  kötor  ,Hürde',  skr.  kotar  ,Zaun',  kotär  , Gebiet,  Grenze'  (,*aus Zäunen'),  sloven.  kotdr  ,Bezirk'  (s.  Berneker  386,  588) ;
WF.  I  338,  WH.  I  175 ff.,  181  f.
2.  kat-  ,Junge  werfen;  Tierjunges'.
Lat.  catulus  ,Tierjunges,  bes.  junger  Hund  oder  Katze',  umbr.  katel^ Gen.  katles  , catulus';
aisl.  hadna  f.  , junge   Ziege',   mhd.    hatele,   nhd. -Schweiz,    haue   , Ziege';
slav.  kotiti  s^  (russ.  kotitbsja  usw.)  , Junge  werfen',  dial.  köthka  ,Lamm', skr.  kot  jBrut',  poln.  wy-kot  , Zicklein'  usw.  (s.  Berneker  589  f.).
WP.  I  338  f.,  WH.  I  183.
kat-  ,kämpfen',  katu-  :  5af (e)ro-  ,Kampf'.
Ai.  sätdyati  ,haut  zusammen,  wirft  nieder';  sdtru-  m.  ,Besieger,  Feind';
gall.  catu-  , Kampf  in  GN  Catu-rlx  , Schlachtenkönig',  air.  cath  , Kampf; Truppe,  Schar',  qymr.  cad  ds.,  corn.  cas  m.  ,Kampf';  cymr.  cadr(*kat-ro-) , stark',  abret.  cadr,  mbret.  kazr^  nbret.  kaer  ,schön';  cymr.  cadarn  , stark', bret.  kadarn  ,tapfer';  dazu  auch  nach  Loth  RC  42,  84  f.  cymr.  cadw  m, , Truppe,  Schar'  (^katuo-),  als  Verb  »bewahren,  schützen';  abrit.  Mars Belatu-cadros  enthält  hingegen  die  Wurzel  kad-  , glänzen' ; ■  aisl.  Jiod  f.  ,Streit'  (=  gall.  catu-),  GN  Hgdr,  got.  MN  Theuda-hatha-8, ags.  headu-,  ahd-  hadu-  , Kampf  in  Namen  wie  Hadu-mär,  Hedwig]  mhd. Jiader  ,Zank,  Streit';
falls  man  hier  slav.  k-  für  k-  annehmen  darf  (vgl.  oben  S.  18^),  abg. kotora,  russ. -ksl.  kotera  , Streit,  Kampf;
möglich   wäre   Heranziehung   des   thrak.  VN   der   IccrgaL,  ^arQO-^evtai]
daß  in  gr.  aarlvrj  , Luxuswagen',  adriXla'  nleiäg  tö  äargov,  die  als  phryg. Worte  mit  arm:  sayl  , Wagen'  (arm.-phryg.  *satilia)  zusammenhängen,  die Bed.  des  , Streitwagens'  die  ursprüngliche  sei,  ist  unerweisbar.
WP.  I  339,  340,  Vendryes  RC.  43,  246,  M.  Leumann  Hermes  68,  359,
1
535
}caU'  ^erniedrigen^  demütigen;  kau-no-s  Schande,  Schämt
Gr.  T^avvöq'  xazög  (ay,Xr]QÖg,  in   letzterer  Bed.  zu  v-alo),  Schulze  KZ.  29
```


## [2026-09-06T14:54:22.809Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification; grep -ho '\"ref\": \"HRN:[0-9]*\"[^}]*' page-1[0-9][0-9].json | head -6; echo ====; grep -ho '\"src\": \"HRN\"[^}]*' page-19*.json page-20*.json | head -6",
 "description": "See how HRN refs were cited before"
}
```


### [2026-09-06T14:54:22.866Z] TOOL RESULT

```
Exit code 1
"ref": "HRN:133",
"ref": "HRN:168",
"ref": "HRN:168",
"ref": "HRN:96",
"ref": "HRN:99", "status": "partial", "note": "Horn, Grundriss p.99 no.448 (HRN.txt leaf 120): '448. čōb \"Holz\". phlv. čōp \"Holz\" (Guj. Ab.); kurd. čō, siw; bal. LW. čōp; wa. čōpk, sar. čūb.' — it supports the word and gloss but labels the ancestor Pahlavi, not Old Persian; and čōgān is no.449 on p.100, not p.99."
"ref": "HRN:99", "status": "partial", "note": "Horn p.99 no.448 'čōb \"Holz\". phlv. čōp \"Holz\"' supports čūb exactly; but čōgān is Horn no.449 on p.100 ('čōgān \"Schläger (im Ballspiel)\"', with the note that the NP variant čōlgān 'in čōbgān zu emendiren ist' — i.e. Horn himself reads the word as čōb-gān), so the citation should be HRN:99-100."
(eval):1: === not found
```


## [2026-09-06T14:54:27.756Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### leaf 215 (p.194)\"; awk 'BEGIN{RS=\"\\f\"} NR==215' HRN.txt; echo \"### leaf 207 (p.186)\"; awk 'BEGIN{RS=\"\\f\"} NR==207' HRN.txt",
 "description": "Print Horn pages 194 and 186"
}
```


### [2026-09-06T14:54:30.283Z] TOOL RESULT

```
### leaf 215 (p.194)
— 193 —
Zu ahd. hulja, hulla 'Kopfbedeckung, also zu got.
htdjan Verhüllen, bedecken, lat. celärCj occulere
(Hörn, KZ. 32, 582 No. 10).
Das Suffix ist spezifisch iranisch (vergl. kurd. ktdäw,
serkuläw, arm. LW. sarßiday 'cucullo dei dottori
Armeni'). Calautica und Verwandtes (siehe de
Lagarde, Mitteilungen II, 4 ffolg.) /gehören nicht
hierher.
864. kulbe, kurbe *Bude', arab. LW. ktirbaj, kurhaq^ kidhat,
N ö 1 d e k e (mündliche Mitteilung) vergleicht ^r.
xaXvßrj *Hütte, Laube. Dies zu yiaXvnro) (6. Meyor,
Griech. Grammatik-, § 197a).
865. kern 'wenig, gering, klein', kemJn,
ap. kamna- Venig*; aw. katmia-; phlv. kaw^ kam(i).^f,
LW. kurd. kirn; afy. bei. (125) kanij n. ßam.
Die Grundform ist ^kanibhua- bezw. *kipbhna'
(Hübschmann, ZDMG. 44, 559, Bartholomae,
Studien H, 101). Kurd. kirn und phlv. kim^ welches
bisweilen vorkommt (z. B. vd. 19 (9)), werden auf den
Comparativ *kamni/ao zurückgehen («-Epenthese).
866. {\)kemer 'Gürtel', kemra^),
aw. kamara- 'Gürtel*; phlv. kamar,
LW. kurd. kemer 'Gürtel*, af/. kamar; oss. LW. d.
kamdri Trauengürtel'.
867. (2)kemer 'Höhe, Berg* etc. (IDD Is. 2, 10).
aw. kamere^a- 'Kopf*; phlv. kamal (wie Bartho-
lomae zu lesen vorschlägt, der kamer eda- als aus
Vermischung der Wörter ai. kakühh-, kakud-, skr.
kapdla-^ lat. caput und ai. mürdhän- entstanden an-
sieht).
kenär s. keran (No. 846).
868. kund 'stumpf; tapfer*.
skr. (bezw. präkr.) kunfha- 'stumpf.
Vergl. Rückert, ZDMG. 8, 280.
np. ktmdaver hat nach Nöldeke (mündliche Mit-
teilung) im Öähnäme immer die Bedeutung 'stolz'.
»J Nöldeke, Pars. Studien II, 40.
U r n , QrundriHB d. noup. Ktyniolog-ie. ] 3
### leaf 207 (p.186)
1 85 —
K.
/,8:J1. (i)kär *Wcrk, Tlmt\
aw. kära- in käravaitl; plilv. kär; skr. -küra- *i:Iand-
limg, That\
Allgemein entlehnt.
832. (2)'kär 'Tliäter , z. B. in sitahkär, destkar,
ai. -kära- '-tuend'; plilv. -kär,
Vergl. np. gär (No. 884).
■ym, kärd 'Messer.
aw. kareta- Messer ; plilv. kürt; ai. vergl. [/kart-,
kfntdti 'schneiden*.
kurd. kir, ktrd (H.-Sch.); oss. d. t. ßa?'d 'Messer,
d. kärdtm, t. Mrdln 'schneiden'; bei. kärc^ kärca^
n. ßarca (195).
834. kär[»är 'Kampf, Schlachtfeld*, vergl. karJ 'Kämpfer.
phlv. kärejar (y. 11 (8)).
vergl. ap. kära- *Heer'; lit, käras 'Krieg'; ksl. kara
'Zank, Streit'; got. harjis 'Heer.
Das Suffix -eflr ist unklar. Im PehlevT lautet es
'jär, was nicht -cär gelesen werden kann; vergl.
dialektisch grl. käljär (Vullers), Kä§. K. kast^jori —
kistzär.
Fr. Müller (WZKM. 5, ;354) will dasselbe kär in
np. karwän 'Karawane' finden; Nöldeke (mündliche
Mitteilung) stellt hierher np. kärdär 'Vezir .
835. kästen Vermindern, verringern', Praes. käh-eni,
^ kahldefiy Icästi,
phlv. kahltan, kähet, kälünltan, käh{i)sn (Men. s. v.
khah"),
Wohl zu demselben Stamm wie aw. kasu-, np. kih
(No. 877).
y'836. kästen (Sahn. 111, 1544 Vers 842), kisten 'säen',
Praes. kär-em, kist,
g. kastmün,
aw. [/kars-f ya{i\lxarsti, vergl. karsosca frakäroyöis;
```


## [2026-09-06T14:54:34.458Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### leaf 216\"; awk 'BEGIN{RS=\"\\f\"} NR==216' HRN.txt; echo \"### leaf 208\"; awk 'BEGIN{RS=\"\\f\"} NR==208' HRN.txt",
 "description": "Print Horn leaves 216 and 208"
}
```


### [2026-09-06T14:54:37.433Z] TOOL RESULT

```
### leaf 216
- 194 —
869. kenden graben', Praes. ken-em,
ap. aw. \/kan- graben'; phlv. kantan (Bund.), kandau
(AV., PPGl.), paz. /andan; ai. l/khan-, khdnati.
kurd. kendn; af/. kandal; oss. t. vergl. nijgänin
'begraben' (Urform "^Mnin^ 203); arm. vergl. akan
diOQvy/iia (H. No. 3).
Auf die mit kh anlautende Form der Wurzel gehen
np. (arab.) yendeq Graben , phlv. xantak, np. /öw«j, /an
'Haus' (No. 405) und /am 'Quelle' (No. 466) zurück;
vergl. auch feryen neu gegrabener Wasserkanal' neben
ferken etc. Auf päz. /andan ist gar nichts zu geben,
vergl. päz. /ähUan^ /m u. a. m.
J. V. Fierlinger erklärt KZ. 27, 335 das ap. aw.
kan- gegenüber ai. khan- durch Analogiebildung nach
der schwachen Wurzelstufe, Bartholomae, ib. 367
Anm. 2 durch solche nach den mit Praefixen kon-
sonantischen Auslauts zusammengesetzten Formen.
870. kentz 'Jungfrau, Mädchen', kenizek,
maz. klja (?) ').
aw. kanyä-^ kaini7i-, kainikä- 'Jungfrau, Mädchen';
phlv. kanik, phlv. päz. kaMöak bezw. kanTjak, kanlzak
(PPGL); ai. kanyä-, kanijd-.
Durch dasselbe Suffix weitergebildet wie dösüe,
nrDirn (Is. 23, 4, 12) 'Jungfrau .
871. kiitäh, küteh 'klein, kurz'; ködek 'Kind, Kleines,
Foetus, Embryo (AM.)'.
aw. kutaka- 'klein'; phlv. kütak bezw. kötak,
bei. künd, n. Jcund 'kurz, nahe' (209); afy. LW. (?)
kötah,
np. küiäh entbehrt auflfälliger Weise der Lautver-
schiebung. Für ködek ist eine Grundform *kvataka-
anzusetzen (wie dö aus dva-, tö aus tvam u. a. m.).
Zum Pronominalstamm kva-, kn-?
872. hüze 'Topf.
aw. /awza- *Topf'; arm. LW. kuz.
Da mir Geldner's Übersetzung (vergl. KZ. 25, 583
^) Dazu auch kurd. kic?
### leaf 208
- 186 -^
plilv. hisUw, kis 'Furcliü (vd. 9 (132)), i/^r/är 'Acker-
land' (vd. 5 (22) Gl.), akist (aw. akarsta-, vd. 3 (79)),
kär 'Besäung' (AV.); ai. 2. [/kars-^ kfsdti 'Furchen
ziehen, pflügen.
af/. karal 'säen'; bei. kisag ^ n. kisay (198); wa;^.
kilr-am, sar. cär-am,
Aufi^ällig ist der Bedeutungsübergang von 'Furchen
ziehen, pflügen' zu 'säen*.
837. kaften ^spalten; graben*, kawlden^ käflden^ keffen,
keflden.
Nüldeke vergleicht gr. vA-ntzoc 'Graben*. Vergl.
unter slkäften (No. 787).
kurd. LW. vekavum 'ich wahrsage*, vek^ft (aus np.
wcl käwlden 'nachforschen') Justi No. 37; sar. käti-am
'gi'aben*.
l 838. krim 'Wunsch, Wille*, käme.
ap. aw. kama- 'Wunsch, Wille*; phlv. kamak,
kämakth , kämitan (y. 4 (12) Gl.), käm(i)stan (Men.),
vielleicht arm. LW. kam-k 'Wille, Wunsch*, kamim
'wollen, wünschen* (Hübschniann, No. 140); ai. iama-,
oss. kom 'Wille* (161).
Ob np. kam 'Gaumen* (af/. kumai) dasselbe Wort ist,
ist unsicher '). Der Vokal würde zu mhd. goume,
ags. görnUy got. ^gömö (dann nicht *gatimö) 'Gaumen*
stimmen, das zweifelnd zu gr. xuvvog 'klaffend*, /dog
(*xdfng) 'Kluft* gestellt wird; aber k und g passen
nicht zusammen. Da von einer np. Aussprache gütn
nichts bekannt ist, so durfte West, Pahl. Texts,
Part. II, 439 nicht ein phlv. gämak 'Gaumen' con-
struiren.
f 839. kän 'Mine'.
Zu ap. l^kan- 'graben*, vergl. kenden (No. 869).
840. krih 'Stroh*, vergl. kährubä^ kehriibä 'Bernstein*.
Nöldeke (mündliche Mitteilung) vergleicht ai. käga-,
ein zu Matten, Dächern und Anderem gebrauchtes
'j Ver^l. ii\)cv Kückert, ZO^IQ. 10, 158,
```


## [2026-09-06T14:54:50.617Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"405\\. \\|466\\. \" HRN.txt | head -20",
 "description": "Find Horn entries 405 and 466"
}
```


### [2026-09-06T14:54:50.662Z] TOOL RESULT

```
1821:1466. bäzär 'Markt', bazargan, hazergän Kaufmann'.
3796:405. teheniy tehm *stark'^).
4256:466. yi^miT 'Quelle, Wasserbassin , x^^ (unbelegt und un-
```


## [2026-09-06T14:54:51.703Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### BRT leaf for col 583\"; grep -n \"^58[23]$\\|^ *583\" BRT.txt | head",
 "description": "Find Bartholomae col 583"
}
```


### [2026-09-06T14:54:53.729Z] TOOL RESULT

```
### BRT leaf for col 583
11250:583
```


## [2026-09-06T14:55:00.959Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"'Haus\" HRN.txt | head -20; echo ====; sed -n '4250,4262p' HRN.txt",
 "description": "Grep Horn for Haus and print entry 466"
}
```


### [2026-09-06T14:55:01.030Z] TOOL RESULT

```
Exit code 1
1648:evän 'Vorhalle, Palast* s. unter np. Iä7i 'Haus*
1907:worden. Dass np. bäm 'Haus' zu bämya- gehören
1911:175. {\)bän 'Haus; vergl. bänü (No. 178)2).
1927:2) Vergl. gr. Sdjuag 'Hausfrau* neben ai. dam- (Schulze, KZ.
1947:^78. bätm 'Herrin', wörtl. 'Hausherrin' (vergl. bän, No. 175) ;
2367:np. bune bedeutet dann auch 1) 'Haus, Heimat*
4251:465. ^Jiän, yßne 'Haus , xänef/T.
4764:580. {\)ääm 'Haustier, zahmes Tier.
7351:844. kedy kede^) 'Haus*, vergl. ked/udd {ket/iidä^)); iltes-
7562:'Haus' (No. 405) und /am 'Quelle' (No. 466) zurück;
8345:^4. man 'Haus'.
8346:ap. maniya- 'Haus' (die elamitische Version be-
8354:'Hausgerät' kann ich für man nicht belegen, auch nicht
8804:1012. niehen 'Haus'.
8809:bei. metag 'Haus, Wohnung' (241).
11313:bei. gis 'Hausstand, Weib und Kind, Hauswesen und
11314:Familie*, n. (ßö]mahisk 'Hausfliege* (108).
(eval):1: === not found
```


## [2026-09-06T14:55:03.274Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '4245,4275p' HRN.txt",
 "description": "Print Horn entries 465-466"
}
```


### [2026-09-06T14:55:03.328Z] TOOL RESULT

```
kurd. xäv; oss. LW. /öm (Hübschniann, S. 133);
afy. öm, um; bei. hämag, n. häniay, liänvcuj (155);
wa/. yüng,
464. yritnös^) ^schweigend, still*, /ämösl.
skr. a + \/^marS' geduldig ertragen' ; vergl. fcrämös
(No. 812).
465. ^Jiän, yßne 'Haus , xänef/T.
phlv. /ßnak, /an, /änaklk (n''Nn"*2, Nöldeke,
ZDMG. 46, 142).
Von i^khan- 'graben'. Vergl. np. (arab.) yendeq
neben kenden,
466. yi^miT 'Quelle, Wasserbassin , x^^ (unbelegt und un-
sicher 2)).
aw. x^fw-, Nom. ;^äo 'Quelle'; phlv. ;fäw, /ßnlk (Bund.) ;
ai. khiin- [khä-),
kurd. känT, kahm,
467. xäwer {/"äwer) 'Herr.
aw. /'äpara- 'gnädig, barmherzig*; phlv. y^äpar
(Darmesteter, Et. ir. I, 60 Note).
468. ^äye 'Ei*.
phlv. xäyak *Ei' (Men.); arm. Jw *Ei' (unsicher; H.
No. 179); lat. öoiim; gr. rJov; ksl. aje^ jaje *Ei*.
kurd. haik, hl, liek; afy. hä; oss. t. aik, d. aißä
(12); bei. haik (159).
») Reimt auf hös Sahn. I, 429 V. 730.
*J Auch an SteUen wie AM. 240 Zeile 4 v. u. wird man nicht
etwa ;^ä»e *eine Quelle*, sondern ^^änl *die Quelle* (allg.) lesen müssen.1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
aw. ''h*'i:t.<t'i'. Yrr^'l. aj'i^f't'. p^hlv. 4/a^ (Gemme
.J».v. Biiti:.h Mu^. Xu. •;:.. ZDMG. 44. •>*)).
```


## [2026-09-06T14:55:18.776Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '11240,11275p' BRT.txt",
 "description": "Print Bartholomae col 583"
}
```


### [2026-09-06T14:55:18.834Z] TOOL RESULT

```
*)  Nach   Pü.  {atpräs  drahnäk)   sva.   ein  ta'ar oder  zwei  hSiiTa.
KompA.  —  Zum  V.  tat-,  eig.  'Rennbahn'; vgl.  ta!ar-  und  Bthl.  1F,  /O.  3.
•  j.  i^axViÄ-  i.  'Lauf-,  Rennbahn':  upa tarn  °tqm  yqm  darsyqm  ^t.  ig.  ^  T, — aiia *•  tarn  ^'>  yqm  darrfqm  YL5.  50.
Z'um  V,  )ak-,  s.  ta/'ar-  und  BTHL.IF. /o.  3. — i>  Hds.  j''a"ftjw;  Tgl.  iiar-  No.  2  und  anya- No.  6;  femer  zu  lanal,caxra-.
•  j.  Öamtu-tära- "  .\dj,  'über  die  Ent- fernung eines  C.  hinausgehend,  weiter  als ein  €.  gehend,  reichend';  °r5  F.  ig.
*lära.  Adj.,  zum  \.lar.;  ai.  Wro- Adj.  —  Pü.: tartarlum.  —  >>  FMÜLLERs  Zusammenstellung des  Worts  mit  arm.  tarlat  ■geschickt'.  WZKM. 8.  361  ist  ohne  Wert.  Das  arm.  LW.  farlar stammt  aus  ir.  *iarlara-,  das  zu  ai.  calara- Adj.   'geschickt'   gehört;   s.   dazu  Wn.  AiOr.
•  j.  farstu.dräjah-  n.  'die  Länge  eines C:  äaf  fym  vanm  k?r7na7ia  'jö  k»mät paiti  ca'hrusanqm  ". ,  eben  (f.  nach  jeder der  vier  Seiten"  V.  2.  25^;  F.  15.
Pü.:  aspräs  drahnäk,  erl:  2  käsr  hal  kuH  3, dazu  die  Bern. ;  asl  ki  har  4  kml  ^'cTpit.
•  j.  (Jaraman-  n.  'Fell,  Leder';  mrätim "ma  "^anjaymte  "sie  ziehen  an  dem  ge- gerbten Leder(strang) "  Yt  17,  12;  — 'manqmca  .  .  *mrätanqm  N.  ^8;  —  'm<i (NP.)"  vatnantö  br3e?nta  {sA.)  frjna  »r^-
dby  Google
583
öazdahvant-
£i£aäana-
584
satim  saranitH  "die  Felle  strahlen  auf  die Beschauer  Silber  und  Gold(glanz)  in  Fülle" Yt.  5.  129;  —  •mqnca  *hiku  N.55.
ai.  cirman-  n.,   mp.  (Pii.),   np,  larm.    —  Vgl.
•Ara«ä-.  — I)  Nach  der  <j*-Dekl.,  vU  <iämiS3
und  dämihu;  %  403.
•  g.  äazdah'vant-  Adj.  'einsichtig,  ver- ständig': yä  manaohrlHaA.)  'äöaghvantsm ar}^ahyS  Y.  44.  5;  —  hyai  urvalsm  (sd.) "dönifkvadtbyS  Y.JI.3.
Ai._*iaai{/.yti.  oder  *m</(A)as-,  Et.?  —  Pü.; vicarJJr.
•  j.  £a§an-  m.  'Lehrer':  a%auruns  .  . 'sanqica  "  aEsqmcil  ratüS  ämrvyl .  .  am;/- sascS  sp?nta  saosyantascä  Y. /j.  3.
'Ableit.  aus  '!aia-  m.  -Lehre",  ium  V.  kai-, vgl,  iBild.  mq%ran-.  —  Pü.:  eäiilärtum,  Sü.r prajhäpakatamah.  —  >)  Them.
•  j.  *caääna-  Adj.,  PPM.:  s.  kos-  (mit No.  a).
•  j.,  g.  caäman-  n.  'Auge':  °ntanh(<jV).) sühnt  Yt  10.  23,  P.  ^4;  —  sonst  Sing,  in kollektSinn:  'manat hata  "vondenAugen her"  V.  _j.  14;  —  spUi.dSihra{^A^  °manat kaca  niibannti  V.  7.  24;  —  ts  'mSng''> ^wisra  härS  aibJ  aiä  aibi.vamahl  vTspä "all  dessen  wirst  du  durch  Äsa  gewahr,  es mit  leuchtendem  Auge  beobachtend"  Y.  j/. 13;  —  hyat  äz£/ä  hsm  'maini'^  ASr^ab»n "als  ich  dich  mit  dem  Auge  erfasste"  Y. 31.  8;  —  nS  BTt  (Sp.  1 54  u.)  'maint'^  vyä- danstm  Y.  4:5. 8;  —  y3cä  voAa  'mqm'^ arp/ai  (sd.)  manavAn  Y.  50. 10.
KompE.  —  li.  Tgl.  cäi/Uf.  n.,  np.  /asm,  — lEt.  s.  unter  ias-  und  ias-,  —  Pü.:  äisin,  [lu Y.  J/.  8);  fa  Aam  eaimiA,  (m  Y.  31.  13);  />a har  2  casm.  —  O  LS.,  aber  syntaktisch  als IS.  gehtauchl,  daber  Y,  31.  13  mit  IS.  des Adj.  verbunden;  s.  Bthl.  IF.  /a  9  (gegen Der.  VglS.  /,  219). g.  iäxnar}-.  s.  ^kan-,
•  j.  cäxsnay-')  m.  EN.  eines  Gläubigen: °nöt^''>  asaonS  Yt.  13. 114"*.
Mit  Int.-Red.  gebildet,  S  i02  II.  4-  Et.?  — ')  Oder  auch  läxinav-,  iJxinafs  nach  J  10;  s. No.  2.  —  »)  Nach  JusTi  NB.  152  (und  And.) identisch  mit  dem  Bd.  jz.  t  genannten  Ur- ahnen Zara%r/stras  Caxinui.
•  j.  dät- f.  'Brunnengrube':  maF^e  vä  cäiti vä  V.13.Z1.
Ableit.  —  Zum  V.  'lan-,  vgl.  xa»-;  %  13.— Vgl.  mp.  (l'Q.),  np.  m  (aus  iran.  *<^-iä%  S  S).
•  j.  cätaya-  Adj.  (fem.  'yä^  'in  einer Brunnengrube  befindlich':  äpö  yat  'tayA uzuitytista  (sd.)  V.  6.  33.
Statt  *läHya-  geschr.,  S  i^S.   11.  —  Ableit.  aas
<S/-.  —  Pü.:  äp  i  cähän.
•  j.  £ärä-  f.  'Mittel,  Hilfsmittel"»:  "ram F.  IQ.
Zum  V,  'kar-.  —  np.,  mp.  (PQ.)  '"o'';  s.  daza Hbm,  PSt.  51,  AGr.  /.  188.  —  ')  Nach  Pü.; unsicher.
•  j.  cöit  Part  1)  einen  Vergleichungssatz
einleitend,  'wie':  aä:ä  aäiä  c°  ahurd  .  . zardkiuitrim  aoax^ayaas  .  .  ahä  a'ia  c* zardi:ultrS  daiväis  sanm  vyämrvTtä  .  , dha  *az?mclt..  "so,  so  wie  Ah. . .  lehrte,  .  . so,  so  wie  Zar.  . .  entsagte,  . .  so  . .  auch ich  ..  Y.  72.  sf.  2)  enklit,  eine  parti- zipiale  Erläuterung  anschliessend:  ya>a  nö äaAqm  ..*vastS{sA.)  urvanB ..vakuts  ar^Aui (näml.  tiS  aigkaiy^  äküsc'  Shüire . . Jassn- tarn  "auf  dass  unsre  Seelen  .  .  seien  .  ., soll  uns  das  Paradies  zu  teil  werden,  in- dem wir  von  der  Offenlegung  weg  zu den  d^urischen  Räumen  gelangen"  \,6o. ii">.         [N.  A4:  lies  nSit\
```


## [2026-09-06T14:55:19.806Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"čäh\\|cäh 'Brunnen\\|'Brunnen\" HRN.txt | head -20",
 "description": "Grep Horn for čāh Brunnen"
}
```


### [2026-09-06T14:55:19.859Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:55:32.371Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for p in PHD.txt PHD_mackenzie.txt; do echo \"=== $p\"; grep -n -i \"^kandan\\|kandan \\[\\|kandag\\|^xān\\b\\|xānag\\|^čāh\\|cāh \\[\\|xandaq\" $p | head -20; done",
 "description": "Grep MacKenzie for kandan, xanag, cah"
}
```


### [2026-09-06T14:55:34.435Z] TOOL RESULT

```
=== PHD.txt
4605:čāh čahār čahārdah
5007:kandan, kardan kardagān kardagār *kardag, kūdak kardespās
=== PHD_mackenzie.txt
3190:kandan, kan- [HE.LWN-tn < A -V IJpr; kn-dn', -tn' 1M knd, N -] dig;
9578:kandan, karuan                  \\lO\S          kurkllm                      ooG'~'S
```


## [2026-09-06T14:55:37.561Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3185,3196p' PHD_mackenzie.txt; echo \"=== xan\"; grep -n \"x[aā]n\" PHD_mackenzie.txt | sed -n '1,60p'",
 "description": "MacKenzie kandan + xan entries"
}
```


### [2026-09-06T14:55:37.639Z] TOOL RESULT

```
 ......ih: weakness.
kan-,v. kandan.
kanar [kn'll N --] side, edge; embrace.
  --a~ [_k' I M kn'rg, N .-"a] edge, limit, boundary.
  ......a~omand [-k'wmnd I M -gfomnd] limited, finite.
kandan, kan- [HE.LWN-tn < A -V IJpr; kn-dn', -tn' 1M knd, N -] dig;
                                      '
       raze, destroy.
kani~ [knyk' I M knyg] girl, maid.
kaniza~ [knyck' I M knycg, N kaniz(ak)] = kanig.
kanti~r [kntgl] quiver.
kapur [k'pwl I Ar. hafur] camphor.
=== xan
979: Aleksandar ['Ikmdll M 'lxsyndr, N Iskandar] Alexander (of Macedon).
1251:astuxan ['sth(w»n' I N ustuxWan] bone.
1661:bun-xan [bwnh)n ] source.
4521:saxwan [MRYA < A mly'; shwn l 1M sxwn, N suxan] word, speech.
5482:wizard - wars                     93                              xan
5531: lxan [h)n' I P x)n, N --] house.
5533:xan                                   94                        xurdruA
5534:2xan [h),,' I P x)n] spring, source.
5535:xanag [B YT A < A byt); h)nh l I N xana] = lxan.
5536:xandidan, xand. [·GHBHWN-ytn' < A "II gM, or "II'*ql;zqlJ,; hnd-ytn' I
5538:xanig [h)nyh 1M x)nyg, N xani] = 2 xan.
6082:bone ast(ag), astuxan.                 bridle ewan, padisar.
6799:high horz, buland; on ,....., balistig.        house kadag, man(d), sray, xan(ag);
6800:higher abar(dar).                                V. lady, master; '"-' and home xan
6971:laugh xandidan.                           lie (v.) druxtan.
7643: source bunxan, casmag, xan(ig),        sprinkling passinJisn.
11082:xand-1                                       bazag, waccag
11085:xandidan1                                    bazakkar
11181:horzwangiha     A()\y """      ~\)       hllnxan
11236:xanagf                                        hilll
11525:                                           V-     astllxan                      \~~
11911:xandidan, xwastan              \\~~        uskarisnih         .A(j~~""
12386:ahog, ahug, xanag                 \ ~ t"O'    rrhid                          \~
12393:axwamn                          \t6~          xanig                         ,~\-'O'
```


## [2026-09-06T14:55:52.119Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD cah\"; grep -n \"^cah\\|cah \\[\\| cah \" PHD_mackenzie.txt | head -10; echo \"=== PLA xandaq\"; grep -n \"handaq\\|hundaq\\|ḫandaq\\|andaq\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -20",
 "description": "PHD cah and Asbaghi xandaq"
}
```


### [2026-09-06T14:55:52.186Z] TOOL RESULT

```
=== PHD cah
8505:cihren-                   -~t;        cah                         "'U'~
11751:cahirI
=== PLA xandaq
11248:O8 - zandag: "sich zum Manichäismus bekennen" pers. c3x, zandaq mp.
```


## [2026-09-06T14:55:55.077Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"\\[pdf page\" incoming/PLA/PLA_pages.txt | sed -n '105,125p'",
 "description": "Locate PLA page 113"
}
```


### [2026-09-06T14:55:55.139Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:55:57.913Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; head -5 incoming/PLA/PLA_pages.txt; wc -l incoming/PLA/PLA_pages.txt; grep -n \"page\" incoming/PLA/PLA_pages.txt | head -5",
 "description": "Inspect PLA_pages.txt format"
}
```


### [2026-09-06T14:55:57.981Z] TOOL RESULT

```
             Asya Asbaghi


Persische Lehnwörter im Arabischen

16026 incoming/PLA/PLA_pages.txt
```


## [2026-09-06T14:56:00.763Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} /kandag|kandak|Graben/ {print NR\": \"substr($0,1,600)}' incoming/PLA/PLA_pages.txt | head -20",
 "description": "Search PLA for kandag/Graben"
}
```


### [2026-09-06T14:56:02.420Z] TOOL RESULT

```
81: birün                                                                       66                                                               bil


©27»       - birün:               eine        Vorstadt          in Choresm,              aus       dem    pers.   ayw      birun       mp.
          .iPoy        berön           1,


Ge             - birüni:               Nisba        v.    os         birun       s.    birün.
          abü-raihän-birüni,                         der       berühmte          iran.        Wissenschaftler,             frz.    aliboron
          "Bezeichnung   
128: hanßar                                                                      113                                                            awäni



DZ          banfa      ı "Kandschar,                     großes          Dolchmesser,                Dolch"       pers.       1,
       Kandschar:                "gebogene              orientalische                  Hiebwaffe"                 pers,       >     er.        .


&sjt    -    albund:             "Herr"           eine       kontrahierte               Form     für       »>1i      bodäwand            3,
```


## [2026-09-06T14:56:06.218Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==128' incoming/PLA/PLA_pages.txt",
 "description": "Print PLA printed page 113"
}
```


### [2026-09-06T14:56:07.848Z] TOOL RESULT

```
hanßar                                                                      113                                                            awäni



DZ          banfa      ı "Kandschar,                     großes          Dolchmesser,                Dolch"       pers.       1,
       Kandschar:                "gebogene              orientalische                  Hiebwaffe"                 pers,       >     er.        .


&sjt    -    albund:             "Herr"           eine       kontrahierte               Form     für       »>1i      bodäwand            3,


Gs>     -    handaris:                 "alter          Wein"       aus      dem       pers.,.s             kandris        4    wahrscheinlich
       aus    dem     pers. «u kuhan "alt".

 ..                                                                                                   >
o>e - handag:                "Festungsgraben"                         aus       dem    pers.     oJ       kande,     pass.         pt.    v.       Verb
       kandan        "graben"                <T mp.          +13      kandag          ec       aw.    / ap.        kan    "graben"            ar.    Lw.
                                                         6
       3» bandag,                  syr.           y2         .


asl,s -      b"ag      : "Herr,                 Meister"           pers.         7     vielleicht           ats     dem    pers.          ap!
       hodäyte.


);>- bawar:                Pl.         v. baur.

wi» - b”ärazm =                           härizm s. härizm.

air          - b”ärazmi:                 Nisba          v. b’ärazm.

                                                                            8
OL>-        biwän:         "Tisch,              Speisetisch"                     aus    dem     pers.       ol>     p"an      MP          re xwän         9
       mand.    kuan             10,


axl> - piwända: dim. v. ai biwän pers. !!.

GLs-         biwänig:              Pl.       v.    oWW. hangah                  "Kloster"        pers.


or          - bawäniqg = hbiwänig s. biwäniq.


1.    Littmann         S.        114
2.    Fremdwörterbuch                     Ss.     v.
3. Muhit
      s. v.
4.    al-MuCarrab                Ss.    Ve
5.    Bharucha         s.        v.,      Nyberg         s.      v.
6.    Brockelmann                s.     v.
7.    Wahrmund         s.        v.
8. TaCälivi figh al-luga S. 198, Muhit s. v.
9.    Mackenzie            Ss.     v.
10.    Macuch        Ss.     V.
11.    Mubit     s.        v.
```


## [2026-09-06T14:56:16.378Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n -i \"gondola\" SKT.txt KLN_1966.txt KLN_1971.txt LKT.txt FSD_vol2.txt WEB_vol1.txt 2>/dev/null | head -20",
 "description": "Grep for gondola in English dictionaries"
}
```


### [2026-09-06T14:56:16.474Z] TOOL RESULT

```
SKT.txt:7783:Gondola.  (Itat.-Gk.)  Ital.  gtm<Ma, dimin.  of  gonda,  a  boftt.  — Gk.  itCvht,  A drinlrinjj  v«MrI  ;  from  ibe  sh.ipe.
SKT.txt:23501:ItaiioH  from  Greek :  arcltipelago,  bai^ lone,  bombast,  catncomb,  gondola,  (copel
KLN_1971.txt:104426:gondola, n., a narrow boat used in the canals of 
KLN_1971.txt:104427:Venice. — It., fr. Friaul. gondola, ‘to waver, 
KLN_1971.txt:104432:Derivative: gondola , intr. v. 
KLN_1971.txt:104433:gondolet, n., a small gondola. — It. gondoletta, 
KLN_1971.txt:104434:dimin. of gondola. See prec. word and -et. 
KLN_1971.txt:104435:gondolier, n., one who rows a gondola. — F., fr. 
KLN_1971.txt:104436:It. gondoliere, fr. gondola. See gondola and -ier. 
KLN_1971.txt:202944:of gondolas starting to race. It. riga is borrowed 
KLN_1971.txt:251139:traghetto, n., gondola station. — It., lit. ‘a cross- 
KLN_1966.txt:16419:gondola,  n.,  a  narrow  boat  used  in  the  canals  of Venice.  —  It.,  fr.  Friaul.  gondola,  ‘to  waver, vacillate’,  which  is  prob.  of  imitative  origin.  It is  not  connected  with  L.  gandeia,  ‘a  kind  of African  ship’.
KLN_1966.txt:16420:Derivative:  gondola,  intr.  v. gondolet,  n.,  a  small  gondola.  —  It.  gondoletta , dimin.  of  gondola.  See  prec.  word  and  -et. gondolier,  n.,  one  who  rows  a  gondola.  —  F.,  fr. It.  gondoliere,  fr.  gondola.  See  gondola  and  -ier. gone,  adj.,  lost;  prop.  pp.  of  go.  —  ME.  gon, fr.  OE.  gan,  pp.  of  OE.  gan,  ‘to  go’.  See  go. Derivatives:  gone-ness,  n.,  goner  (q.v.) goner,  n.,  one  ruined,  lost  (slang).  —  Formed  fr gone  with  suff.  -er.
KLN_1966.txt:32140:regardant,  adj.,  looking  backward  {her.)  —  ME., fr.  MF.  regardant,  pres.  part,  of  MF.  (—  F.) regarder.  See  regard,  v.,  and  -ant. regatta,  n.,  boat  race.  -  It.,  also  rigatta,  fr.  riga, ‘row,  rank’;  so  called  with  reference  to  the  row of  gondolas  starting  to  race.  It.  riga  is  borrowed fr.  OHG.  riga,  ‘row’.  See  row,  ‘series,  rank’, regelate,  intr.  v.,  to  freeze  again.  — -  Formed  fr. re-  and  L.  gelatus,  pp.  of  geldre,  ‘to  freeze’.  See gelid  and  verbal  suff.  -ate. regelation,  n.,  the  process  of  refreezing.  —  Form¬ ed  fr.  re-  and  L.  geldtio,  gen.  -onis,  ‘a  freezing', fr.  gelatus,  pp.  of  geldre.  See  prec.  word  and  -ion. regency,  n.  —  ME.  regencie,  fr.  ML.  regentia,  fr. L.  regens,  gen.  -entis;  see  regent,  n.,  and  -cy.  Cp. F.  regence.
KLN_1966.txt:39780:tragelaphus.  See  prec.  word, traghetto,  n.,  gondola  station.  —  It.,  lit.  ‘a  cross¬ ing  over’,  back  formation  fr.  traghettare,  ‘to  fer¬ ry  across’,  fr.  VL.  *trdjectare,  freq.  of  L.  traicere (less  correctly  trajicere),  (pp.  trajeclus),  ‘to  go over’,  formed  fr.  tra-  and  jaedre,  ‘to  throw’; OProvenc.  trajitar  and  OF.  tresjeter,  ‘to  cross over’,  are  of  the  same  origin.  See  jet,  ‘to  spirt forth’,  and  cp.  trajectory.
WEB_vol1.txt:83034:Gon/di, n. [from Gondi, name of the principal dialect.} 1. a group of Dravidian dialects spoken in central India. 2. the principal dialect of this group. gon/do-la, n. [It., ultimately from Romance base dond-, to rock.] . 1. a long, narrow canalboat with a cabin in the middle and a high, pointed prow and stern, used on the canals Agee it is pro- pelled by a pole or one oar at the stern. 2. a flat-bottomed river barge. 3. a gondola car. 4. a cabin suspended under a dirigible or balloon, for holding the motors, instruments, passengers, etc.
WEB_vol1.txt:83036:GONDOLA
WEB_vol1.txt:83037:gon’dō-lå car, a railroad freight car with low sides and no top. gon’dō-let, n. [It. gondoletta, dim. of gondola, a gondola.] a small gondola. gon-dō-liēr’, n. [It. gondoliere, from gondola, a gondola.] a man who rows or poles a gondola. gone, a. [pp. of go.] . moved away; departed. ruined. lost. dying; dead. faint; weak. used up; consumed. . ago; past. far gone; (a) much advanced; deeply in- volved; (b) very tired. gone on; in love with. [Colloq.] gone’ness, n. a condition of exhaustion or weakness, as resulting from lack of food; faintness. gon/ér, n. a person or thing that has reached a stage beyond recovery, help, or recall. [Colleq.] Gon/ér-il, n. in Shakespeare's King Lear, the elder of Lear's two wicked daughters. gon’fa lon, n. [It. gonfalone; OFr. gonfanon (Fr. gonfalon); LL. gonfano, gunifano, a ban- ner; O.H.G. gundfano, a battle standard; gund, gunt, a battle, and gano, a banner.] a flag or ensign hanging from a crosspiece in- stead of an upright staff and usually ending in streamers; especially, such a standard used by any of the medieval republics of Italy. gon/’fa-lon-iér’, n. [from Fr. or It.; Fr. gonfa- lonier; It. gonfaloniere.] 1. one who bears a gonfalon; a chief stand- ard bearer. 2. the chief magistrate of any of various Italian republics during the Middle Ages. 3. an officer at Rome who bears the Church standard. 4. the chief officer of any of the sixteen Florentine guilds in the Middle Ages. gon’fa-lén-iér/ate, n. the office of a gonfalon- ier, gon/fa-non, n. a gonfalon. [Obs.] gong, n. (AS. ganz, a going, passage, privy.] a privy; an outdoor toilet. [Obs.] gong, n. [Malay gu, a gong.] 1. aslightly convex metallic disk that gives a loud, resonant tone when struck. 2. a saucer-shaped beli with a similar tone. Goñ-gō-resque’ (-resk’), a. pertaining to the Spanii poet Gongora, or resembling his style. Gon’g6-rism, n. 1. the literary style which characterized the writings of the Spanish oet, Gongora y Argote (d. 1627): its chief eatures were affected metaphors and strained conceits. 2. any style like this. £0/ni-a-tite, x. (Gr. gota, a corner, angle, and lithos, stone.] any member of an extinct genus of fossil mollusks, belonging to the dibranch- iate cephalopodous mollusks and family of ammonites. £0/nid, n. same as gonidium. E gon-i-dan’gi-um, 1.; pl. gon-idan’éiá, [Gr. goné, generation, seed, and angeion, a vessel, receptacle.} in botany, a sporangium in which gonidia are formed. £0-nid’i-a, n. plural of gonidium.
WEB_vol1.txt:85500:gun/de-let, 7. a gondola. [Obs.]
FSD_vol2.txt:19130:Words  beBlnnlng  with  this  prmlx  will  be  found  in  alpha- betical place,  either  singly  or  In  groups, fer'ro',  n.  ilt.l  The  iron  prow  of  a   gondola.
```


## [2026-09-06T14:56:31.914Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN barbican\"; grep -n -i \"barbican\\|^balcony\\|balcony, n\" KLN_1966.txt KLN_1971.txt | head -10",
 "description": "Grep Klein for barbican and balcony"
}
```


### [2026-09-06T14:56:31.974Z] TOOL RESULT

```
=== KLN barbican
KLN_1971.txt:25086:balcony, n. — It. bale one, formed with the aug- 
KLN_1971.txt:25953:barbican, n., outer defense of a city or castle. — 
KLN_1971.txt:25954:ME. barbecan , fr. OF. barbacan, barbican (F. 
KLN_1966.txt:4311:balcony,  n.  —  It.  balcone,  formed  with  the  aug¬ mentative  suff.  -one  fr.  balco,  ‘scaffold’,  which is  borrowed  fr.  OHG.  balcho,  ‘beam’  (whence MHG.  balke,  G.  Balken,  ‘beam’).  See  balk, ‘beam’.
KLN_1966.txt:4441:barbette,  n.,  mound  for  mounting  guns  (fort.)  — F.,  dimin.  of  barbe,  ‘beard’  (see  barb,  ‘beard’, and  -ette) ;  so  called  from  a  fanciful  comparison of  the  mounted  guns  with  a  beard, barbican,  n.,  outer  defense  of  a  city  or  castle.  — ME.  barbecan,  fr.  OF.  barbacan,  barbican  (F. barbacane),  which  prob.  derives  ult.  fr.  Pers. bdla-khdna,  ‘upper  chamber,  balcony  on  the  top of  a  house’,  lit.  ‘a  high  house’,  fr.  bala,  ‘high’, and  khdna,  ‘house’.  The  first  element  is  rel.  to Avestic  berezant-,  OI.  brhant-,  ‘high’;  see borough.  The  second  element  derives  fr.  stem khan-,  ‘to  dig’.
```


## [2026-09-06T14:56:45.874Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT balkon\"; grep -n -i \"balcone\\|barbacane\\|balkon\\|bālā-ḫāna\\|bālāḫāna\" LKT.txt | head -20",
 "description": "Grep Lokotsch for balcone/barbacane"
}
```


### [2026-09-06T14:56:45.933Z] TOOL RESULT

```
=== LKT balkon
665:[Aus  pers.  bälä  'hoch'  Horn  NpEt  S.  39, Nr.  171  und  pers.  hänä  'Haus'  ebenda S.  103,  Nr.  465;  also  eigentlich  'Hoch- haus'] 'ein  oberes  Zimmer,  hervorstehen- der Teil  des  Hauses,  Erker,  Balkon'; hieraus  mit  vielfachen  Kontaminationen ähnlich  bedeutender  Wörter  und  unter volksetymologischen  Einflüssen  it.  bar- ■bucane  'Brustwehr  mit  Schießscharten, Stützmauer',  prov.  barbacana,  frz.  bar- bacane  'Schießscharte',  kat.  barbacana ''Fensterdach,  Dachvorsprung',  sp.  bar- bacana und  pg.  barbacäa  'Außen werk
667:einer  Feslunii'.  Wenn  Löbel  EITAP  11 diese  Ableitung  mit  mehr  als  einem Schein  von  Recht  elimologia  indoiosä nennt,  so  sind  die  folgenden  Wörter aus  semantischen  Gründen  unzweifel- haft aus  dem  angegebenen  Grundwort abzuleiten  und  Annahme  eines  ahd. palco  'Balken'  als  Grundwort  abzuleh- nen: it.  balcotie,  frz.  balcon,  rum.  halcon, sp.  balcÖH,  pg.  balcäo;  dtsch.  Balkon, engl,  balconi/;  russ.  bulg.  serb.  poln. balkon,  6ech.  bulkön.  —  Auf  direkterem Wege,  höchstens  über  tat.  bälahane  ist russ.  balagan  'Marktbude  aus  Brettern, Schaubude'  entstanden.  —  Andere  Ab- leitungen s.  DE  60.  Eguilaz  97.  ZfromPh V,  244;  XXX,  557.  [Gorjajew  9  u.  10. ML  890.
1071:[Aus  pers.  cähar  'vier'  s.  hier  Nr.  381, zu  car  verkürzt  wie  schon  in  pers.  Zu- sammensetzungen, und  ar.  fäk  'Bogen (im  architektonischen  Sinne)'],  'Terrasse, die  auf  vier  Pfosten  gestützt  ist',  oder 'kleines  viereckiges  Zimmer',  das  gewöhn- lich auf  dem  flachen  Dache  des  Hauses erbaut  ist  und  in  dem  man  entweder Wäsche  trocknet  oder  die  reine,  frische Luft  genießt.  Häufig  werden  dardak auch  die  kleinen  Sommerwohnungen auf  den  Landgütern,  in  den  Gärten  oder den  Weinbergen  der  Reichen  genannt, die  meist  turmartig  gebaut  sind  und außer  dem  Erdgesciioß  noch  wenigstens ein  Stockwerk  haben.  Hieraus  rum. cerdac,  ceardac  'Balkon',  auf  Pfählen gebauter  'Altan'.  Russ.  cerdak  'Erker, Speicher',  certog  'Saal,  Prunkgemach, Halle',  klruss.  cerdak  'Erker',  serb.  car- dak 'Söller,  Obergemach',  bulg.  cerdak, cardak,  cerdak,  corrfoA- 'Vorhalle'.  [Gor- jajew 410.    Bern  SlEtWb  171.
6352:baragouin  256 I  barbacane  197 I  bardache  afz.  229 ]  barde(au)  228 i  ftarc^of  228 ,  baroque  364 I  barque  2148 i  barracan  250 I  basane(r)  afz.  316 ^  basane  316 I  basanier  316 !  basiUqtie  (vemej  262
6934:balcone  197
6972:barbacane  197
7639:babusza  1625 bachmat(y)  128 bachor  180 bachur  180 baczmag  265 badawja  164 öarfja  159 badjan  162 ftöi-aZie  189 balaban  1607 balagula  145  d bafamucic  199 balamut  199 baldachin  170 balkon  197 balsani  293 Z»af<a  207
```


## [2026-09-06T14:56:46.444Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHN balcon\"; grep -n -i \"balcon\" PHN.txt DEV.txt | head -20",
 "description": "Grep Pihan/Devic for balcon"
}
```


### [2026-09-06T14:56:46.505Z] TOOL RESULT

```
=== PHN balcon
PHN.txt:2109:BALCON, s. m. composé, (p.)
PHN.txt:2116:halcany, le portugais balcâo, l'italien balcone, l'espagnol et le
PHN.txt:2117:français balcon, servant à désigner une galerie avec balustrade
PHN.txt:10273:Balcon, s. ni. compose, (p.) Page 55
```


## [2026-09-06T14:56:58.593Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '655,670p' LKT.txt; echo \"=== which leaf\"; awk 'BEGIN{RS=\"\\f\"} {n+=gsub(/\\n/,\"\\n\"); if(!p && n>=665){print \"block \"NR; print substr($0,1,200); p=1}}' LKT.txt",
 "description": "Lokotsch entry 197 context"
}
```


## [2026-09-06T14:56:58.956Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '2100,2130p' PHN.txt",
 "description": "Pihan balcon entry"
}
```


### [2026-09-06T14:57:00.191Z] TOOL RESULT

```
""Schwatzen' ;  hieraus  angloind.  to  buck ^plappern,  viel  und  anhaltend  schwatzen'. [Hobson-Jobson  117.
193.  Tk.  bakyr:
'Kupfer';  hieraus  serb.  bakar  'dass.', bulg.  bakor  'Kupfer,  Kupfergefäß'.  [Mikl SlEtWb  6.    Bern  SlEtWb  40.
194.  Ar.  balä':
'Unglück',  tk.  ebenso  bela;  hieraus  rum. bela,  belea  'Mißgeschick,  Not',  beläleü 'schwach'.
195.  Mal.  baläcau:
^Vorspeise  aus  gesalzenen  und  dann  ge- stampften und  getrockneten  Fischchen oder  dergl.'  [Pijn  38  a];  hieraus  anglo- ind. balachong,  blachong,  die  charakte- ristische Speise  der  indochinesischen  und malayischen  Völker.  [Dass.  wie  hier Nr.  286.]    [Hobson-Jobson  51.
196.  Ar.  balad:
'Land',  Adj.  dazu  baladl  'ländlich,  ein- heimisch'; hieraus  mit  leicht  verständ- lichem Bedeutungswechsel  sp.  baladi 'wertlos,  gering'.    [DE  202/3.
197.  Pers.  bälähäuä:
[Aus  pers.  bälä  'hoch'  Horn  NpEt  S.  39, Nr.  171  und  pers.  hänä  'Haus'  ebenda S.  103,  Nr.  465;  also  eigentlich  'Hoch- haus'] 'ein  oberes  Zimmer,  hervorstehen- der Teil  des  Hauses,  Erker,  Balkon'; hieraus  mit  vielfachen  Kontaminationen ähnlich  bedeutender  Wörter  und  unter volksetymologischen  Einflüssen  it.  bar- ■bucane  'Brustwehr  mit  Schießscharten, Stützmauer',  prov.  barbacana,  frz.  bar- bacane  'Schießscharte',  kat.  barbacana ''Fensterdach,  Dachvorsprung',  sp.  bar- bacana und  pg.  barbacäa  'Außen werk
Lolcotsch,  Etymolog.  Wörterbuch.
einer  Feslunii'.  Wenn  Löbel  EITAP  11 diese  Ableitung  mit  mehr  als  einem Schein  von  Recht  elimologia  indoiosä nennt,  so  sind  die  folgenden  Wörter aus  semantischen  Gründen  unzweifel- haft aus  dem  angegebenen  Grundwort abzuleiten  und  Annahme  eines  ahd. palco  'Balken'  als  Grundwort  abzuleh- nen: it.  balcotie,  frz.  balcon,  rum.  halcon, sp.  balcÖH,  pg.  balcäo;  dtsch.  Balkon, engl,  balconi/;  russ.  bulg.  serb.  poln. balkon,  6ech.  bulkön.  —  Auf  direkterem Wege,  höchstens  über  tat.  bälahane  ist russ.  balagan  'Marktbude  aus  Brettern, Schaubude'  entstanden.  —  Andere  Ab- leitungen s.  DE  60.  Eguilaz  97.  ZfromPh V,  244;  XXX,  557.  [Gorjajew  9  u.  10. ML  890.
198.  Tat.  balaliiika:
'Laute' ;  hieraus  russ.  halalaika,  klr. balabaika,  serb.  balalajka,  öech.  bala- lajka  'russische  Zither  oder  Laute  mit zwei  oder  drei  Saiten' ;  frz.  la  balale'ika, dtsch.  Balalaika.    [Gorjajew  10.
199.  Mongrol.  balamnt:
=== which leaf
block 44
tammt,  ZDMG  LI,  29.o]; hieraus  sp.  albeitar,  pg.  alveitar  'dass.'. [DE  70.
184  a.  Hebr.  bajiö: 'Haus'  [ar.  bait,  assyr.  bitu];  hieraus gaunerdeulsch  Bais,  Bes,  Bos  'dass.'. Mit
```


### [2026-09-06T14:57:00.231Z] TOOL RESULT

```
BALAIS, adj. m. (p.)
^yu^J^ [balakhch] Sorte de pierre précieuse de couleur d'hya-
cinthe, et tirée d'une montagne du Turkestan, que l'on appelle
j&^Oo [badakhch] ou ^lâb^Oy [badakhchân], — Le premier
mot oriental n'est qu'une variante des deux autres, et l'adjectif
français est ordinairement précédé du substantif rubis : rubis
balais, en persan ^L&^«Xj JoJ [/aV badakhchân j. — Les Italiens
écrivent balascio; les Anglais, baiass; les Espagnols et les Por-
tugais, balax.
BALCON, s. m. composé, (p.)
JbU.^1; [bâlûkhâikeh], composé de l'adjectif ^l? [bâlà] élevé, et
du substantif Xîl^ [&/ran«/i] maison, demeure ou appartement.
Partie supérieure d'une habitation, d'où Ton aperçoit les alen-
toui*s; belvédère. (Voyez le Dictionnaire turc-^français de M. fiian-
ck', Q* édition, page 3 16, col. q, lig. 37.) — De là viennent
t^s-probablement, malgré l'altération d'orthographe, l'anglais
halcany, le portugais balcâo, l'italien balcone, l'espagnol et le
français balcon, servant à désigner une galerie avec balustrade
devant les fenêtres d'une maison.
BALDAQUIN, s. m. (a.)
Cp mot , qui désigne un dais nu-dessus dun lit, d'un trthie, etc..
l56 BAL
est tiré directement de l'italien baldacchino; mais ce dernier
vient lui-même de Baldach, transcription vicieuse du nom de
^l«Xffj [baglidâdz]y adoptée par le célèbre voyageur vénitien
Marco Polo et plusieurs autres auteurs du moyen âge. Il parait,
en effet, que jadis la ville de Bagbdad était renommée pour
ce genre d'ornement. — L'italien baldacchino est donc dérivé
de Baldach ou Baldacco, et veut dire simplement appartenant à
Baghdad, ou provenant de Baghdad. C'est ainsi que Ton se sert,
par exemple, du mot maroquin, en parlant d'un genre de cuir
```


## [2026-09-06T14:57:20.429Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SYN page 46 ===\"; awk 'BEGIN{RS=\"\\f\"} NR>=44 && NR<=50 {print \"----block \"NR; print substr($0,1,400)}' SYN.txt",
 "description": "Locate Buck page 46"
}
```


## [2026-09-06T14:57:21.858Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SNS kan ===\"; grep -n \"kan\\b\\|kandan\\|xandaq\\|xān\" SNS.txt | head -20; echo \"=== SNS pages 8/155\"; awk 'BEGIN{RS=\"\\f\"} NR==8 || NR==155 {print \"---- \"NR; print substr($0,1,700)}' SNS_pages.txt",
 "description": "Grep SNS glossary"
}
```


### [2026-09-06T14:57:22.110Z] TOOL RESULT

```
=== SYN page 46 ===
----block 44
ere, Goth. malan, etc. ‘grind’ (5.56). Walde- P. 2.288. Feist 366.
NHG boden, Du. bodem, etc. ‘bottom’ (12.34) and ‘ground, soil’.
4. Boh. pida ‘bottom, ground, soil’ (Russ. pod ‘bottom of a haycock, hearth’) : Grk. wédov etc. (above, 1). Here also prob. Russ. pocva (the reg. technical term for ‘soil’), fr. *pod(d)sva beside podosva ‘sole’?
1.213 DUST Grk. — xévts G
----block 45
 MHG stoup, NHG staub, MLG, Du. stof (MLG > ODan. stov, now stv with é fr. vb., Sw. stoft), root connection? Falk-Torp 1201. Feist 457. wok Si Obey New, ot duft ‘fragrance’), ON, Nowy th ‘ aie dyst ‘fine meal’) OF oa at US ( an.
’ ust (if % correct =
NHG dunst ‘vapor’), ME, NE dust, all fr. extensions of the root *dheu- seen in Skt. dhi-, dhu- ‘shake’, Grk. dtw ‘Tage, seethe
----block 46
 few are used for both ‘mud’ and ‘clay’.
Where several words are entered for the same language, they may be in part somewhat differentiated in application (‘deep mud, mire’, ‘mud’ such as dredged from the bottom of a river, ‘mud’ in the roads, etc.) or in local preference (cf. NHG kot, dreck, etc.).
1. Grk. rydés, Dor. rads most com- monly potters’ and masons’ ‘clay’ (
----block 47
tc. ‘pour’, like OE gyte ‘pouring, flood’. Hellquist 315.
Dan. sgle (more common in Norw.) : OE, OHG sol ‘mud puddle’, Goth. bi- sauljan, OF sylian ‘defile’. Falk-Torp 1238 f,
ME mudde, NE mud, MLG mudde, MIG, Du. modder (MLG > Dan., Sw. mudder), fr. a root *meu-, *mu- and ex- tensions, seen in many words with a common notion of ‘wet? or ‘dirty’, as Grk. pbdos ‘damp’, pvd
----block 48
de-P. 2.176,
Russ. grjaz’ (cf. Pol. grqz ‘deep mud, bog’) : ChSl. po-greenqti, -grqziti ‘sink’ (10.33). Berneker 350.
7. Skt. panka-: Goth. fanz, ete. (above, 4).
Skt. kardama-, etym. dub. Walde-P-
Briickner 31. 1.428. 1.215 SAND Grk. wWéppos, appos Goth. malma Lith. smelis, smiltis NG &spos ON sandr Lett. smélis, smilts Lat. (h)aréna, sabulum Dan. sand ChSl. pésitkit It. sabbia, ren
----block 49
2 MOUNTAIN; HILL : Bpos; dé cow. Goth. fairguni; hlains Lith. kalnas; kalnelis
or eae eae ON ald Lett. kalns; pakalne NG Bovvd; Bouvaxe Dan. Odjerg, fjeld; bakke ChSl.  gora; chlitmit we Lat. | méns; collis, clivus Sw. berg (fjall); backe SCr. gora; brijeg, brezZuljak It. montagna, monte; col- OE beorg, din, munt; hyll (hum)
lina, colle ME mount, mountain; hill Boh. hora (orch); pahorek, Fr. mon
----block 50
acq 128 f.
2. Lat. mons, montis (> It. monte, etc.), W. mynydd, Corn. meneth, Br. menez ‘mountain’, Av. mati- ‘mountain top’, fr. the root seen in Lat. é-, pré- mineére ‘stand out, project’ (cf. NE eminence, prominence in physical sense), minae ‘projecting points, threats’. Walde-P. 2.263. Ernout-M. 628 f.
Lat. adj. monténus, VLat. *mon- taneus (cf. subterrdneus, etc.), neut. p
```


### [2026-09-06T14:57:24.224Z] TOOL RESULT

```
=== SNS kan ===
2066:j-jt^ (Kent. 178) (o^)o* :kan :v^ ( kh3- :o T ^» 
7999:•O sl *:pakan: **"! 
8565:^W-»>^«0^:pa r ^3akan/palCl3akan: 
8566::parakan: <&»**»» ( SnS W *) parakla : ^ 
12837:nfn : jji- na^an : j-S* • (4>m . Gram 204)nkan: ^j' 
28972:kan 8/13 
31733:parCr:akan/palCl3ak3n 
31963:pakan 117/10 
=== SNS pages 8/155
---- 8
                                                                                                                     »


                                                                                                        jLiS^
                                                                                                                                                                                                                             oU
     i^   ^  m
                 Ij-n 4-t •j^i       u »A o^vr Ki* j j A-** 3 Ub - ***** *         1




^     OJ ^( aj*) *jUjy» ts^it
                                              Jii l* i^     *fr o*i*V Jlfri '**** *-Vj      -*




       
---- 155
                                                                                I




                            i^L^ii^b a-U.^J
                                                                                                                                          ^w«*yum                                               TYT
                                      ?-\ l-**/T*S
M-*A-*fr-M*-*—f 6-T—TA-TY-Tf-T6-TT-T^
       . ^A-U-1Y-^-^?-AA-AT-A—
                                VV-YY-Yf-YT-YT-VT                                                         •T./TT*
.f-1 oT-1                                                                                                                *fi,„»f
```


## [2026-09-06T14:57:39.010Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"1\\.3[0-9] \\|SPRING\\|WELL$\\| WELL \" SYN.txt | head -20; echo \"=== blocks 69-73\"; awk 'BEGIN{RS=\"\\f\"} NR>=69 && NR<=73 {print \"----block \"NR; print substr($0,1,300)}' SYN.txt",
 "description": "Find Buck spring/well section"
}
```


### [2026-09-06T14:57:40.627Z] TOOL RESULT

```
1220:1.31 WATER
1248:36 SELECTED INDO-EUROPEAN SYNONYMS 1.32 SHA
1279:1.33 LAKE
1292:5. The Balto-Slavic word, Lith eZeras (or azeras), OPruss. assaran, Lett. ezers, ChSl. jezero, etc. etym.? Connected with the Greek river name ’Axépwv by Prellwitz, BB 24.106 (cf. also Kretsch- mer, Glotta 14.98); with ChSl. jazu ‘canal, fishweir’, ete. (Berneker 277), Lith. eé ‘pool’, by Meillet, BSL 29. 1.38 ff.
1297:1.34 GULF, BAY
1336:40 1.35 WAVE
1374:1.36 RIVER; STREAM; BROOK
1437:1.37 SPRING; WELL
11476:711 DWELL
12041:DWELL
15436:prob. ‘bronze’ in Rigveda (Zimmer, Altind. Leben 51f. Macdonell-Keith 1.31 f.), later ‘iron’, Av. ayah- ‘bronze’ (as shown by epithets ‘yellow, golden’; cf. Geiger, Ostiran. Kultur 148), later fron’ as NPers. dhan.
15465:Skt. ¢ydma- ‘black’ is used with ayas- or alone for ‘iron’. Macdonell-Keith 1.31 f.
15708:Grk. capyavy (in NT, 2 Cor, 11.33 clearly a ‘rope-basket’; cf. the Goth. rendering 8n67j6; so prob. in the papyri, where the word is frequent beside kopuvos), Att. tapyavn (Hesych., EM), etym.? Walde-P. 1.751. Boisacq 853.
16376:ME aisie, aisy, esy, etc., NE easy, fr. OF’. aisié (Fr. aisé), pple. of atster ‘put at ease’, deriv. of aise ‘comfort, ease, op- portunity’ (> ME eise, etc., NE ease sb.), this fr. Lat. adiacéns ‘lying near, neighboring’, but mainly through ‘what is at hand, convenient’, REW 168. Gamillscheg 23. Wartburg 1.31 ff.
18342:. With few exceptions, the words for ee te to an inherited group. =e rive, of IE *aks-, this prob. fr. piwee drive’ in Skt. a7- I, Gere, et ne » ete, (10.65). Walde-P 1.37 Nout-M. 9 “ties & i Walde-H. 1.89. wy Osu; Lat. axis (> It ; . asse, Sp. aan Si (fr. VLat. *axalis), Tr tte »VLat, ae ; OE eaz, ME ax, singl ; beam’), NE dial. HG. a in New England), Du, pn ahse, NHG achse: Moving ct ass; ChSI. ost, SCr.
18703:11.31 SEEK
18704:11.32 Fix
18705:11.33 Lose
18706:11.34 RELEASE
19373:11.31 SEEK
=== blocks 69-73
----block 69
96), NG dim. puax ‘brook’, also peyarid ‘water-
tourse’ (with or without water); Ir. sruaim, sruth ‘stream, river’ (NIr. ‘river’ in river names), NIr. srutén ‘brook’, W. ffrwd ‘stream’, Br. froud ‘torrent’ (so Pedersen 1.35; fr. *spru-tu- : OE spritan ‘sprout’, etc. 
----block 70
m ‘pool’. Walde-P. 2.612. Peder- sen 1.103,
Ir. glais ‘brook’, perh. : Ir. glass ‘green’. Macbain 196 s.v. glaiseach.
Br. gouer, Corn. gover (OCorn. guuer, gl. rivus) ‘brook’, W. gofer ‘overflow, rill’, Ir. fobar in place names, epd. of
— so Ln public Domain. Gurukul Kangri Col
----block 71
r- ‘flow’ (10.32).
Skt. kulya- ‘brook, canal,’ beside kulya- ‘bone’, both from the notion of of ‘hollow’ : OF hol, etc. ‘hollow’ (12.72). Walde-P. 1.332.
Digitized by Arya Samaj Foundation Chennai and eGangotri r" |
44 SELECTED INDO-EUROPEAN SYNONYMS
1.37 SPRING; WELL
k. opt He d
----block 72
 Eust.) : Bptw ‘be full, swell, gush forth’. :
3. Lat. fons, fontis ‘spring’ : Skt. dhan-, dhanv- ‘run, flow’. Walde-P. 1.852. Ernout-M. 375. Walde-H. 1.525.
Hence It. fonte, Sp. fuente. Deriv. fontana, whence It. fontana, Fr. fontaine (> ME, NE fountain, formerly used for ‘spring’),
----block 73
‘out’ and viréti ‘boil’ (10.31). Fr. the same root also SCr. vrelo ‘spring’. Miklosich 381.
Boh. pramen ‘spring’, also ‘jet, stream, strand’ : ChSl. prament ‘thread’, SCr. pramen ‘tuft of hair’, Pol. promien ‘tay’, fr. *por-men-, deriv. of IE *per- ‘pass through’
```


## [2026-09-06T14:57:46.310Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR>=71 && NR<=76' SYN.txt | grep -n -i \"pers\\|Av\\.\\|cah\\|kan\\|xa\\|Skt\" | head -40",
 "description": "Buck 1.37 Iranian forms"
}
```


### [2026-09-06T14:57:47.777Z] TOOL RESULT

```
2:Skt. kulya- ‘brook, canal,’ beside kulya- ‘bone’, both from the notion of of ‘hollow’ : OF hol, etc. ‘hollow’ (12.72). Walde-P. 1.332.
7:puns NHG quelle; brunnen Skt. utsa-; avata-, kiipa-
12:Ay. xzdn-; Edat- brunno ‘spring’, NHG brunnen mostly ‘well’ or ‘fountain’ : Lat. fervére ‘boil’, Grk. dipw ‘mix’, Skt. bhur- ‘quiver, stir’, etc. (IE *bher-, *bheru-, *bhreu-, etc.). Walde-P. 2.157 ff., 167 ff. Ernout-M. 353.
17:3. Lat. fons, fontis ‘spring’ : Skt. dhan-, dhanv- ‘run, flow’. Walde-P. 1.852. Ernout-M. 375. Walde-H. 1.525.
20:CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
21:: CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
33:NHG quelle ‘spring’ : quellen ‘flow, a Skt. gal- ‘drip’, ete. Walde-P. te a Saltinis ‘spring’ : Saltas, Lett. 108, old’. Leskien, Bildung d. Nom. Walde-P. 1 269 SNe Mae so ii, rel as faved the most primi-
36:Lett. avuots ‘spring’ : Skt. avata- ‘well’, avata- ‘pit’, avani- ‘river, river bed’, perh. Grk. avavpos ‘mountain tor- rent’, Lat. Avernus, etc. Walde-P. 1.254. Mihl.-Endz. 1.233. Walde-H. 1.31f.
37:Lett. aka, dim. acina ‘well’ : Lith. akas ‘hole cut in the ice’, ChSl. oko ‘eye’, Grk. 677 ‘hole’, Arm. akn ‘eye, hole, spring’. Development from ‘eye’ to ‘hole’, then ‘well’. Cf. NPers. casm ‘eye’, Casma ‘spring’. Walde-P. 1.170 ff.
44:Pol. érédlo, Boh. zidlo ‘spring’ : Russ. Zerlo ‘opening, crater’, Pol. gardto ‘throat, gullet’ (*gor-dlo-), Lith. gurklys ‘crop’ (of a bird), Lat. gurges ‘abyss, whirlpool’, Grk. Bapaépoy ‘pit’, ete. fr. IE *gver- in Skt. gr- ‘swallow’, Grk. BiBpwoxw ‘devour’, etc. Development through ‘opening’ (as in Russ.) to ‘spring’. Walde-P. 1.682. Briickner 667.
52:8. Skt. wisa- ‘spring’ : udan- ‘water’. Walde-P. 1.252.
53:Skt. avata- ‘well’ : Lett. avuots ‘spring’, etc. (above, 6).
54:Skt. kiipa- ‘hole, pit, well’ (cf. kupa- jala- ‘well-water’) : Grk. xian ‘hut’, kimeAdov ‘goblet’, Lat. capa ‘tub, vat’, etc., all fr. the notion of ‘bent, hollow’. Walde-P. 1.373.
55:Av. zan- (nom. pl. xd) ‘spring’ : Skt. khan- ‘dig’, kha- ‘hole, opening’, kha- or khan- (acc. sg. khaém) ‘spring, source’. Walde-P. 1.399. Barth. 531.
56:Av. éat- ‘well’, NPers. éah ‘well’ : Av. kan- ‘dig’, parallel form to Skt. khan-, Barth. 583.
65:i. caill, fid, fidbad, ross Du. woud Skt. _ vana-, aranya-, atavi- Nir. coil OHG  wald, holz Av. razura-~
76:CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
83: eam, block’, Skt. kastha- ‘stick, oe a (Gypsy karst, hast 1 it. “keld-d- ‘break off, split’ Walde-P. 1.438 f. Falk Ne ok sv. holt. Accordi : eon p 417. NED the meaning ‘py; ng to this connection, S Plece of wood’ would seem
89:4, ON widr ‘woods, wood’, Dan., Sw. ved ‘wood’ (mostly ‘firewood’), OF widu, wudu ‘woods, wood’, so ME wode, NE wood(s) OHG witu ‘wood’, Ir. fid ‘woods, tree, wood’ (NIv. fiodh esp. in epds. ‘wooded’ or ‘wooden’), W. gwydd ‘woods, trees’, Br. gwez ‘trees’ prob. : Lat. di- videre ‘separate’, Skt. vidhu- ‘solitary’, Lith. vidus ‘inside’, etc., with develop- ment of ‘woods’ through ‘borderland’ (as in ON mork, see foll.). Walde-P. 1.314. Falk-Torp 1357.
93:CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
98:5. Lith. giré, Lett. dzir’a ‘woods’, OPruss. garian ‘tree’ : ChSl. gora, Skt. giri-, etc. ‘mountain’ (1.22).
100:Lett. mezs ‘woods’, OPruss. median ‘woods’, Lith. medis ‘tree, wood’ : ChSIl. mezda, Russ. meza ‘boundary’, Lat. me- dius, Skt. madhya-, Goth. midjis ‘mid’, with development through ‘borderland’ as in ON mork, etc. Walde-P. 2.261. Mihl.-Endz. 2.611.
104:7. Skt. vana- ‘woods, tree, wood’, Av. vana- ‘tree’, etym.? Walde-P. 1.259.
105:Skt. aranya- ‘wilderness, forest’, also ‘distant land’ : arana- ‘distant’.
106:Skt. atavi- ‘forest’, prob : af- ‘wander about, roam’. BR s.v. Uhlenbeck 5.
107:Av. razura- ‘woods’ and ‘pit to catch animals’: Av. razah-, Skt. rahas- ‘re- moteness, loneliness’. The development assumed by Barth:, s.v., namely ‘woods’ from the trees used to cover the pit, is less likely than ‘woods’ from ‘remote- ness’, as in Skt. aranya-.
108:142 TREE Grk.  dé5pov Goth. bagms Lith. medis NG ba Spov ON tré, badmr (poet.) Lett. kuoks Lat. arbor Dan. ire t ChSl. drévo, dqbit It. albero Sw. irdd SCr.  drvo Fr. arbre OE tréow, béam Boh. strom Sp. Grbol ME ttre Pol. drzewo Rum. —arbore, copac NE tree Russ. derevo Ir. crann, fid Du. boom Skt. urkga-, vana-, dru- NIr.  crann OHG boum ma-, etc. W. coeden, pren MHG boum Av. vand- (varasa-?) Br. gwezenn NHG baum
112:CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
122:pl.), Boh. d¥evo ‘wood’, drevno piece of wood’, Pol. drzewo, Russ. derevo ‘tree, wood’; Skt. daru-, dru- ‘wood’, druma- tree’, Av. dauru- ‘piece of wood, club’.
```


## [2026-09-06T14:57:57.356Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"khánati\\|khanati\\|khan-\" WLD_Bd1_1930_dli_70244_djvu.txt | head -20",
 "description": "Grep Walde-Pokorny Bd I for khan-"
}
```


### [2026-09-06T14:57:57.417Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:57:59.919Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"graben\" WLD_Bd1_1930_dli_70244_djvu.txt | head -30",
 "description": "Grep WLD Bd1 for graben"
}
```


### [2026-09-06T14:57:59.965Z] TOOL RESULT

```
3535:Wiedemann BB. 29, 317 s. u. iam- „graben‘ : ; auch Zugehorigkeit zu *em- 
11051:horigkeit von lit. dkas „Wuhne, Loch im Eise", lett. aka „gegrabener 
11067:ist (s. u. qhena x - „graben“). 
12703:iain- (oder iem- : i e m- : iom-) ,graben, autgraben". 
17901:wohl zu *t era- ..graben ’i, auch ..Iliigel oder Bank von Steinen oder Kies, 
18580:Gr. oT'qo g ,.Laufgraben, um Schiffe ins Wasser zu ziehen 1 ' kaum als 
18581:*foooyog (Froekde BB. 20. 221) hier, sondern als *ogyog zu *ereu~ ,.graben“. 
21609:K. H. Meyer IF. 35, 230 besserzu *(s)qap- „graben"), xdcu] „Krippe“, xanavq 
21623:mit *sqnp- „graben“ s. Yf. LEWb. 2 s. v.), capnla „Sch6pfgefaB" (capuldre 
21713:worfener Erdhaufen, dann Haufen iiberhaupt“ zu aksl. kopati „graben“, 
21728:Yereinigung von *qap- „fassen“ mit sqap- „graben“ (Prellwitz u. xdnezo?) 
21838:,,Grube“ usw. zugrunde liegen als „gerodetes und gegrabenes Grundstiick I£ 
21847:Ai. Wb. 303, Berneker 565 zu slav. kopati „graben, auch mit dem FuBe 
21848:aufstampfen“ (siehe *sqap- ,.graben, hacken“), kaum mit Zupitza KZ. 37, 
23498:sqap- „schneiden, graben“). Alb. k’ipi „Haufe“ (Jokl SBAk.AVien 16S, 
24926:s-Erw.: lit. knisu, kn'isti „ wiihlen, graben“, lett. knisis, Inislis „kleine 
25134:qheiuY „graben“. 
25136:Ai. kliunati „grabt“, Inf. khani-tum , Ptc. khiltd- „gegraben“, /.’/id- n. 
25143:„graben“ (Formen bei Bartholomae Airan. Wb. 437 ff., zum ar. Abl. s. auch 
25233:Aber lat. cectoria ,.ein um ein Grundstiick gezogener Grenzgraben“ 
27417:mer KZ. 38, lOOf. auch eine gleichbed. Wz, q'iel- „stecken, graben" an: 
27418:cymr. palu ,. graben", pal, corn. bret. pal „Spaten" (wird von Pedersen 
27424:cladait „8ie graben", cymr. claddu ,. graben", z. B. Pedersen KG. II 492); 
27656:KZ. 33, 77, Pedersen KG. II 492), cymr. claddu, bret. claza „graben“, mir. 
28243:„Kapaun“ usw., Wz. qap-, sqap- ..schneiden, graben") moglich (Brugmann, 
28286:„fortgesetzt gelinde kratzen“, kasit , kasti „umgraben‘ - , lett. kast ,,liarken“, 
35594:,.graben" auch u. *bu fiir dumpfe Schalleindriicke ; 
37863:Schnittling vom Olbaum", yaga-xr^g „das eingegrabene, eingepragte; 
38193:Ganz fraglich gr. ygoptpag .,Sau ‘ (.die wiihlende, grabende ?) als Nasalform 
41169:2. ghrebli- ,, kratzen, scharren, graben'-. -Nicht immer sicker von ghrcbli
```


## [2026-09-06T14:58:04.690Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '25128,25165p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== find page 399 marker\"; sed -n '25100,25135p' WLD_Bd1_1930_dli_70244_djvu.txt | grep -n \"39[0-9]\"",
 "description": "Print Walde-Pokorny qhen- graben entry"
}
```


### [2026-09-06T14:58:04.754Z] TOOL RESULT

```
„streben, trachten, ringen“, chiities „kampfen, ringen, sich bemuhen a , 
censfies „sicb anstrengen, sich bestreben, sich sehnen“ hier angescblossen 
werden. Ygl. aber Miihlenbach-Endzelin Lett.-D. Wb. I 372, 391 u. 392. 

Lat. navns (Persson aaO.) bleibt fern, s. yen- „erkennen l ‘. 

qheiuY „graben“. 

Ai. kliunati „grabt“, Inf. khani-tum , Ptc. khiltd- „gegraben“, /.’/id- n. 
„Hohle, Offnung“ ijunge Bildung wie auch llm- in a-khu- „Maulwurf“, 
s. Charpentier IF. 32, 98, kha- „ Quelle, Brunnen“ = av. xa Nom. Acc. pi., 
xq m. Gen. pi. „Quelle, Brunnen u {xqnya- „fontanus“; xayana- ds. durch 
Reim auf das folgende zrayana -, ds. Bartholomae Airan. Wb. 532); mit Ver- 
lust der Aspiration (in Zs. mit Praef. ns-, ham-, Bartholomae KZ. 27, 367 
Anm. 2, Gdr. d. ir. Ph. I Sf., Wackernagel Ai. Gr. I 121) av. ap. kan 
„graben“ (Formen bei Bartholomae Airan. Wb. 437 ff., zum ar. Abl. s. auch 
Reichelt KZ. 39, 39 f.), kani- „Graben“ = ai. Uiani- „wuhlend“, f. „Mine, 
Fundgrube fiir Edelsteiue 1 ' und (Persson KZ. 33, 290) = lit. kin'ts f. „ein- 
gewiihltes Schweinelager“, kinis m. „ds., auch allgemein Lager“, lett. 
cinis „IIumpel“. Arm. akan „dioQvy[ia u (Hiibschmann Arm. St. 1 16, Solmsen 
KZ. 34, 53) stimmt im anl. Yokal und im k nicht (auch idg. q ware arm. 
£); daB phryg. y.vovyavei „dem Grabe“ (Fick BB. 14, 50, Solmsen aaO.) 
als qno-m„n die Hochstufe II der Wz. enthalte (die Basis ware dann als 
qheno- ansetzbar), ist dagegen denkbar, wenn auch nicht sicher t oi-xevefiav 
„dieses Grab 14 ? = ai. *khaniman- ? Solmsen aaO. 6 Iff ). 

Solange die ar. Aspirata kh- nicht als Neuerung dieses Sprachzweiges 
nachgewiesen ist, ist es vorsichtiger, diese Sippe von yen- ^ratzen 1,1 ge- 
schieden zu halten. 

Anders iiber ai. kha-, khu-, aber nicht iiberzeugend, Bezzenberger BB. 
27, 174 f. (: lit. dkas „Wuhne“ usw., s. u. oqt- „sehen“h 

qene (wohl qSene) „Partikel der Yerallgemeinerung und Unbestimmtheit 4 '. 

Ai. cana ds., av. cinCi ds. (s. Bartholomae Airan. Wb. 594) ; wgerm. nord. 
-i jin in ahd. wer-gin, as. hwergin , ags. hivergen „irgendwo“ (aisl. hvenji 
„nirgendwo“ (nhd. ir-gen-d, mlid. iergen, ahd. io wergin), aschwed. cen-gin, 
=== find page 399 marker
20:399 
31:werden. Ygl. aber Miihlenbach-Endzelin Lett.-D. Wb. I 372, 391 u. 392.
```


## [2026-09-06T14:58:13.925Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gräbt\\|grabt\" POK_0*.txt | head -20",
 "description": "Grep Pokorny for gräbt"
}
```


### [2026-09-06T14:58:13.984Z] TOOL RESULT

```
POK_03.txt:2244:Npers.  käfad,  kävaö  ,gräbt,  spaltet',  käf  , Spalt',  §ikäftan  , spalten';
POK_01.txt:4919:weiter   hierher   oder   zu   5.  er-   ai.   rddati   ,kratzt,    ritzt,   gräbt,   hackt^ vi-radati  , zertrennt,  eröffnet';
POK_02.txt:1699:lit.  grabüs,  grabnüs  ,fingerfertig,  gewandt  im  Stehlen',  grabineti,  graba- liöti,  graboti  , tasten  nach  etwas,  greifen',  grabstyti  ,ergreifen,  packen', dehnstuf,  grebiu,  grebti  , rechen,  ergreifen,  rauben';  altes  Iterativ,  gröbiit, gröbti  ,ergreifen,  an  sich  reißen,  rauben',  gröbis  m.  ,Raub,  Beute';  lett. grebju,  grebt  auch  , greifen',  grabas  f.  PL  , Zusammengerafftes',  greblis Jdeine  Harke',  grdbju,  grabt  ,greifen,  fassen,  harken',  gräbdt  Iterativ dazu  ,um  sich  greifen,  zusammenharken';
POK_02.txt:4661:^  Die  bei  WP.  I  341,  348  f.,  399  angeführten  Wurzeln  khäd-  ,beißen',  khähh-  :  khöbh- jkraftlos',  kherw  ,graben'  sind  nicht  als  idg.  zu  erweisen,  ebensowenig  das  von  Specht (Idg.  Dekl.  263,  Anm.  4)  angesetzte  khä-mo-  , krumm';  die  von  ihm  (S.  256)  angeführten ai.  Beispiele  khalati-,  kharva-f  khara-.  khanda-,  khora-  sind  sämtlich  nicbtidg.  Herkunft. Ai.  khädati  ,zerbeißt,  kaut',  npers.  xäyad  ds.,  könnten  zu  arm.  xacanem  ,beiße'  gehören, aber  auch  mit  sekundärer  expressiver  Aspiration  als  *lmd-  zu  lit.  kdndu  , beiße'  (etwas anders  oben  S.  560).  Zur  gleichen  Wurzel  ken-  (oben  559  ff.)  könnte  ai.  khdnati  , gräbt*, Inf.  khdni-tum,  Partiz.  khätd-  {*khn-to-)  gehören,  samt  den  Neubildungen  khä-  n.  , Höhle', ä-khü-  , Maulwurf,  khä-  .Brunnen'  =  av.  Nom.  Akk.  PL  äcä  ds. ;  ai.  khani-  ,wühlend',  f. , Mauseloch'  =  av.  kani-  , Graben';  av.  apers.  kann-  ,graben'  (k-  aus  kh-  aus  den  Kompo- sitis  mit  us-,  kam-).  Der  Anlaut  von  gr.  xäcpäv,  xrjcpTJv  , Drohne',  xcotpög  »stumpf,  taub' ist  unsicher,  ebenso  der  von  ksl.  chabiti  , verderben',  chabem  ,elend',  wie  auch  der  von ksl.  chomg-tb  , Kummet',  von  Specht  zu  lat.  hämus  {*khä-mo-)  , Haken',  gr.  /«^(i?  .ge- krümmt' (und  Jtfa/3d?  ds.)  gestellt  (anders  oben  S.  555).  Zum  Problem  der  Tenues  Aspi- ratae,  die  z.  T.  gewiß  als  sekundär  expressiv  aufzufassen  sind,  vgl.  Hj.  Frisk,  Göteborgs Högsk  Arsskr.  1936:  2,  S.  38ff.,  Specht  Idg.  Dekl.  251  ff.  Zum  slav.  anlautenden  ch- vgl.  V.  Machek  Slavia  16  (1938),  161  ff.  und  J.  J.  Mikkola  Urslav.  Gramm.  174ff.
```


## [2026-09-06T14:58:22.748Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=4661 && /^[0-9]{3}$/ {p=$0; l=NR} END{}' POK_02.txt; awk 'NR<=4665 && /^[0-9]{2,4}$/ {p=$0;l=NR} END{print \"last page marker:\",p,\"at line\",l}' POK_02.txt",
 "description": "Find Pokorny page of the khan footnote"
}
```


### [2026-09-06T14:58:24.492Z] TOOL RESULT

```
last page marker: 40 at line 4509
```


## [2026-09-06T14:58:28.039Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=4661 && /^ *[0-9]{3} *$/ {p=$0;l=NR} END{print \"page\",p,\"line\",l}' POK_02.txt; sed -n '4640,4662p' POK_02.txt | cut -c1-160",
 "description": "Context of Pokorny khan footnote"
}
```


### [2026-09-06T14:58:29.709Z] TOOL RESULT

```
page 633 line 4643
kuon-,  kun-  ,Hund';  ursprüngl.  Nom.  Sg.  küuo{n),  Gen.  kunös,
Ai.  svä  und  s{u)vä  ,Hund',  Gen.  mnas,  Akk.  svänam,  Akk.  PI.  sünas] av,  spä,  spändm,  Gen.  PI.  sünam,  med.  (Herodot)  a/raxa  {*kun-ko-  
arm.  sww.  Gen.  san  ,Hund' Jmit  unklarem  i);  nicht  gut  vereinbar  mit skund  ,Hündchen',  falls  aus  *kuon-to-,  -tä-,  oder  zu  den  oben  S.  564 
633
mit  fürs  Thrak.-Phryg.  auffälligem  Gutt.  1yd.  Kavöavlvig  ,x^^-^n^sS  thrak. (y^  Kccv-ödüjv  (zum  2.  Glied  s.  dhäu-  ,würgen');
o-r.  -Kvcov,  '/.wog  ,Huiid*  (xvvtsqoq  , hündischer,  d.  i.  unverschämter^  Sup. xvvratog',  zu  Kvvd(xvia  vgl.  lit.  sun-muse  ,Hundsfliege') ;
o-anz  unklar  lat.  canis  ,Hund',  cänes  ursprüngl.  altes  fem.  , Hündin', canlcula  (vgl.  ai.  §unl  f.)  hinsichtlich  des  a;  vielleicht  Einmisch
air.  cü  (Gen.  con  ==  xwdg),  cymr.  ci  (PL  cwn  ==  -/.vveg,  lit.  sünes),  bret. corn.  ki  ,Hund*  aus  *Äwö;
got.  hunds,   aisl.  hundr^   ags.  hund,  ahd.  hunt  ,Hund'  (kun-tö-),  s.  oben ;
lit.  §uö  (Gen.  sufis)  ,Hund*  (zum  i-St.  geworden  in  lit.  dial.  sunis,  lett.  suns, apr.  sunis  ,Hund*) ;  ^Form  lett.  suntana  ,großer  Hund'
toch.  A  kuj  Obl.  korij  B  Nom.  ku.
Die  Bedeutung  von  lat.  canis  als  ,unglücklicher  Wurf  beim  Würfelspiel' kehrt  in  gr.  xvcov  wieder,  sowie  in  ai.  Sva-ghnin-  eigentlich  ,Hunde
WP.  I  465 f.,  WH.  I  152 f.;  Kurylowicz  Accentuation  19;  nach  Specht Idg.  Dekl.  32,  121  f.  Ableitung  von  der  Farbwurzel  2.  keu-,  S.  594.
ktires-,  kuers-,  kurs-  , Gehölz,  Baum'??
Gr.  TtqXvog  , Steineiche',  falls  aus  *Ä;wfs-7io-s(?)  :  ^aX\.  prenne  ,arborem  gran- dem',  cymr.  corn.  bret.  prenn  ,Baum'  (*ku7'es-no-)',  ablaut
WP.  I  524,  Morris- Jones  Welsh  Gr.  128,  Machek  Slavia  16  (1939),  182  f., Mikkola  ürslav.  Gr.  177.  J.  B.  Hofmann  (Etym.  Wb.  des  Gr.  284) 
Kh.'
kba  kha!  Interjektion  des  Lachens;  mit  z.  T.  einzelsprachlicher  Neu- schöpfung.
Ai.  hdkhati  (Gramm.)  ,lacht';  arm.  xaxank  , Gelächter',  gr.  xcr^d^cü (aus  *xax«?w)  flache  laut';  lat.  cachinnö,  -äre  ,hellauf  lachen',  cac
Ähnliche  Schallwurzel  käk-  ^auslachen'  in  gr.  xijxa^w  ,schmähe';  ahd. huohön  , spotten,  höhnen',  as.  höhi-llk  ^lächerlich';  mit  germ.  -k-
WP.  I  336,  WH.  I  126.  Vgl.  oben  S.  497  Jia  ha.
^  Die  bei  WP.  I  341,  348  f.,  399  angeführten  Wurzeln  khäd-  ,beißen',  khähh-  :  khöbh- jkraftlos',  kherw  ,graben'  sind  nicht  als  idg.  z
Zahlreiche  ai.  Wörter  nichtidg.  Herkunft  mit  anlaut.  kh-^  darunter  die  oben  erwähnten, bei  Kuiper,  Proto-Munda  47  ff.
```


## [2026-09-06T14:58:58.347Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; wc -l MON_part1.txt MON_part2.txt; echo ===; grep -c \"\" MON_part1.txt; awk 'BEGIN{RS=\"\\f\"} END{print \"blocks:\",NR}' MON_part1.txt; awk 'BEGIN{RS=\"\\f\"} END{print \"blocks:\",NR}' MON_part2.txt; echo \"=== sample\"; awk 'BEGIN{RS=\"\\f\"} NR==100 {print substr($0,1,300)}' MON_part1.txt",
 "description": "Inspect MON OCR structure"
}
```


### [2026-09-06T14:59:00.085Z] TOOL RESULT

```
Exit code 1
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
(eval):1: == not found
```


## [2026-09-06T14:59:03.543Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} END{print \"part1 blocks:\",NR}' MON_part1.txt; awk 'BEGIN{RS=\"\\f\"} END{print \"part2 blocks:\",NR}' MON_part2.txt; echo \"--- sample block 100 part1\"; awk 'BEGIN{RS=\"\\f\"} NR==100 {print substr($0,1,400)}' MON_part1.txt",
 "description": "MON block counts"
}
```


### [2026-09-06T14:59:05.560Z] TOOL RESULT

```
part1 blocks: 1
part2 blocks: 1
--- sample block 100 part1
```


## [2026-09-06T14:59:08.830Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1,20p' MON_part1.txt; echo \"......\"; grep -n \"بالاخانه\\|بالکن\\|خندق\\|خانی\\|کنند\" MON_part1.txt MON_part2.txt | head -20",
 "description": "Inspect MON text and grep Persian words"
}
```


### [2026-09-06T14:59:08.977Z] TOOL RESULT

```
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

......
MON_part2.txt:90:غادر: (ع.] (افا.) غدر کننده بیوفا؛ 
MON_part2.txt:144:تأثیر می‌کنند و اسید سیانیدر یک و گلوکز و 
MON_part2.txt:149:تهیه می‌کنند که به مصارف داروبی می‌رسد. 
MON_part2.txt:174:غارب: 0 (ع.] (افا.) غروب کننده 
MON_part2.txt:186:مال مردم را به تاراج برد؛ غارت کننده. 
MON_part2.txt:194:غارس: *:8:(ع. (افا.) غرس کننده. 
MON_part2.txt:210:موقع نزاع کنند. 
MON_part2.txt:237:می‌کنند و در زمستان بطرف مرکز اروپا و 
MON_part2.txt:241:۲ کبلو وزن بیدا می‌کنند. نژادهای مختلف 
MON_part2.txt:320:غاش: (5868:(ع.] (افا.) غش کننده. کسی 
MON_part2.txt:344:غصب کننده» گیرنده چیزی به قهر و ظلم؛ 
MON_part2.txt:373:غالب: اهاة« [ع.] (افا.) غلبه کننده؛ چیره» 
MON_part2.txt:399:غلو کننده» از حد درگذرنده. آنکه در حق 
MON_part2.txt:411:سباه که موی را بدان خضاب کنند. 
MON_part2.txt:437:می‌کنند و پس از چند ماه به طریقة خشک 
MON_part2.txt:451:اثر تصفیه کننده خون و تقوبت دهنده 
MON_part2.txt:500:جانوران دیگر کنند؛ غال. 
MON_part2.txt:637:آن تأیید کنند» معامله‌ای که به تقویم مسقوم 
MON_part2.txt:697:صبح تتاول کنند) طعام چاشت شت؛ مق. عشاء. 
MON_part2.txt:760:اگر به خارج راه باز کنند یعنی غده دارای
```


## [2026-09-06T14:59:16.015Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^[0-9]\\{3,4\\} *$\" MON_part1.txt | head -20; echo \"---- tail\"; grep -n \"^[0-9]\\{3,4\\} *$\" MON_part1.txt | tail -5; echo \"---- part2\"; grep -n \"^[0-9]\\{3,4\\} *$\" MON_part2.txt | head -5; grep -n \"^[0-9]\\{3,4\\} *$\" MON_part2.txt | tail -5",
 "description": "Find MON page markers"
}
```


### [2026-09-06T14:59:17.608Z] TOOL RESULT

```
---- tail
---- part2
18075:019 
19307:377 
18075:019 
19307:377
```


## [2026-09-06T14:59:24.289Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for n in 5000 20000 40000 60000 80000 95000; do echo \"--- line $n\"; sed -n \"${n}p\" MON_part1.txt; done",
 "description": "Sample MON_part1 coverage"
}
```


### [2026-09-06T14:59:26.018Z] TOOL RESULT

```
--- line 5000
نوعی آناناس معمولی کوچکتر است؛ 
--- line 20000
بیماران حسن شهرت بافته‌اند. 
--- line 40000
کردن» گراینده کردن. راغب کردن؛ به 
--- line 60000
در: "4 [ع.] (.) شیر لبن. غنیمت. نیکوبی 
--- line 80000
( کیاء) کام. سنجد کرجی: ( کُیا.) کنار. سنجد 
--- line 95000
```


## [2026-09-06T14:59:31.667Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -c \"خند\" MON_part1.txt; grep -n \"خندق\" MON_part1.txt | head; echo \"=== balaxane\"; grep -n \"بالاخانه\\|بالاخانه\\|بالكن\\|بالکن\" MON_part1.txt | head; echo \"=== xane hous\"; grep -n \"^خانه\\|خانه: \" MON_part1.txt | head",
 "description": "Grep MON part1 for Persian headwords"
}
```


### [2026-09-06T14:59:31.821Z] TOOL RESULT

```
112
21295:ابحر. بحر بیکران خندق: (کد.) عالم ملکوت 
28029:منجلات. خندق گونه‌ای که بر گرد شهر 
40079:ترک: (.) خندقی که بر دور حصار و 
47389:جر: 127 [خندق» نهر ] (.) شکاف (عموماً). 
47391:خندق ق کم عرضی که دور با‌ها و مزارع 
55056:برون دیوار قلعه و کنار خندق که در آن 
57559:خندق: 1۸0027 [معر. خندکک - کندگکك - 
=== balaxane
20927:بالکن: (.) ابوان کوچکی که در 
26554:بالاخانه. 
31086:اطراف آن باز باشد؛ بالاخانه» بربار» پرباره؛ 
48947:بالاخانه. 
75616:بالاخانه. صفةً سلندی که سقف آن را بر پنجم: گروهی که در کشوری به ضرر آن 
=== xane hous
1184:ابخانه: ()2.2«2 (امر.) جایی که برای 
1282:آبدارخانه: هسقد.0-.2 (اسر.) جای تهبة 
1933:خانه‌ها است» آنکه کشت را آب دهد 
2021:اتشخانه: (6-)21318-.3 (امر .) جای روشن 
3416:آشپزخانه: (0-)718702-.2 (امر.) آنحا که 
3438:اشخانه: (0-)217302 (امر.) آشپزخانه, 
5748:خانه و کوی با نهادن آیینه‌های بسیار بر 
12895:خانه‌نشین کردن. 
19989:خانه‌ها سازند و رخنه‌ها به اطراف گذارند تا 
20136:بارخانه: (ع-)ممقدةه (امر.) جابی که در
```


## [2026-09-06T14:59:36.946Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"### xandaq\"; sed -n '57555,57570p' MON_part1.txt; echo \"### balkon\"; sed -n '20920,20935p' MON_part1.txt",
 "description": "Print Mo'in xandaq and balkon entries"
}
```


### [2026-09-06T14:59:37.025Z] TOOL RESULT

```
### xandaq

خند‌ستان: «8ا2270-2)0(۶ (امر.) افسوس؛ 
سحر د) لاغ. مسجلس مسخرگی؛ معرکة 
سخرگی. (کد.) لب و دهان معشوق. 
خندق: 1۸0027 [معر. خندکک - کندگکك - 
کنده | (ا.) گودالی که گرد حصار و قلعه و 
لشکرگاه کنند تا مانعم عبور دشمن و سیل 
گردد؛ ج. خنادق. 

حند و تند: 227۱0-0-1870 (امی.) زیر و زیر. 
تاخت و تاراج. پرا کنده و پریشان» تار و مار. 
ند ه: (0-)2:7-2 (امص. .) حالتی در 
انسان که به سب شادی و نشاط ابجاد شود و 
لب‌ها و دهمان گشاده گردند و آوازی 
مخصوص از حلق برآید؛ مق. گریه. خندة 
جام: پرتو شراب. خنده زمسین: 
### balkon

بالکا: قتعل (.) (گیا.) ازملک. 

بالکانه: (و)محعاده [- پالکانه - بالگانه - 
بادگانه] (ا.) پنجره‌ای که از مبله‌های فلز ی 
ماش 

بالکن: (.) ابوان کوچکی که در 
جلوی ساختمان سازند؛ مهتابی. (نم.) طتَة 
فوقانی تماشاخانه با سینما که قسمتی از سالن 
تحتانی را در ز بر کنر گر 

سال‌ماسکه: 6 2 (امر.) مجلس 
رقصی که شرکت‌کنندگان موظفند با تغییر 
تیچ سوه بر آو سرضی 
یابند؛ بال کوستومه.
```


## [2026-09-06T14:59:45.068Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '20700,20790p' MON_part1.txt | grep -n \"بالا\" | head -30",
 "description": "Find Mo'in bālāxāne entry"
}
```


### [2026-09-06T14:59:45.127Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-06T14:59:47.835Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"بالا\" MON_part1.txt | sed -n '1,40p'",
 "description": "Grep bālā in MON"
}
```


### [2026-09-06T14:59:47.904Z] TOOL RESULT

```
1305:از راسته راست‌بالان» از رده حشرات. از 
1598:شیب زیاد» معبر آبی که از بالا به زیر آورده 
1665:سماق‌بالا» بالاون» ترشی بالا. مثل آبکش: 
2229:برافراشتن» بالا بردن: سر تاجشان بر سپهر 
2236:برافراشته» بالا برده» مرفوع. بر دوخته به 
2253:از استخوان بالای سینه و زیر گردن. . 0 
2315:بالان که همشکلی کامل با محبط خود دارد و 
2664:مانند آن را بدان پالایند. آبکش بالاون. 
3092:طبقات بالا روند و با از طبقة بالا به بایین و با 
3093:به زمین فرود آیند؛ بالارو» اسانسر. 
3219:مانند سر پوش بالای سر ما قرار دارد. سقف» 
3220:آسمانه. بالا» جانب علف:. اس اشا, (اخ.) 
3837:دینام بالاتر از ولت باتری گردد یعنی فقط 
4507:(جان.) حشره‌ای از راستةٌ قاب‌بالان که در 
5582:اهیانه: (0)حععرنة (ا.) استخوان بالای مغز 
6133:ایر: ۲ (- بر ) بالا؛ مق. بایین. 
6137:ایر: ۲ [- بر ] (حر. اضد.) بر به. با. بالای؛ 
6207:ظاهر استخوان قوسی شکل بالای کاسة 
6209:ابر وان ايز وها. ایرو بالا انداختن: تیان 
6974:اطاق زیر و بالای آن سوار می‌شوند. 
7178:اثیر: ده [معر .] (ا.) کر 5 آتش که بالای کر و 
7180:طبق عقبده قدما فضای بالای هوای کرة 
9503:(پس. دارندگی و نگهبانی)] (امر.) بالاترین 
9527:برخاستن» بلند شدن» بلنت کم دنل ۵ بالا 
9530:محصول. ارتفاع روز: بالا آمدن روز بالا 
9532:چیزی را. (.) بلندی» بالا؛ اوج. ارتفاع 
9554:اظهار چند چیز بالا برند. ارتفاع صوت: 
9582:رفتن» بربالا رفتن» به بالا برشدن بر رفتن» 
9585:مراتب بالا رود. قانون نشوء و ارتقاء: قانون 
9589:چیزی يا کسی را. انتظار. دیدبانی کردن. بالا 
9985:چوب حرکت می‌کرد و با پایین و بالا رفتن» 
10023:بالا تر بودن. 
10457:روی» بالای» فوق. ضح. این کلمه بدین 
10719:معنی ناز پروردگان و بالانشینان و توانگران 
11185:درجه‌ای است دانشگاهی» بالاتر از دانشیار. 
11215:شاگرد. در اصطلاح کنونیبالاترین درجة 
11239:آموزگاری؛ استاد بودن. بالاترین مقام 
12253:شاعری دیگر را؛ ج. استقبالاات. 
12887:بالاتر از کشیش است؛ ج. اساقفه. 
13358:شدن» فرو نگریستن» از بالا به زیر نگریستن.
```


## [2026-09-06T15:00:04.719Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,60p' tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-06T15:00:04.760Z] TOOL RESULT

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


## [2026-09-06T15:00:13.390Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://en.wiktionary.org/wiki/کندن\" \\\n \"https://en.wiktionary.org/wiki/خانه\" \\\n \"https://en.wiktionary.org/wiki/چاه\" \\\n \"https://en.wiktionary.org/wiki/خندق\" \\\n \"https://en.wiktionary.org/wiki/κόνδυ\" \\\n \"https://www.etymonline.com/word/gondola\" \\\n \"https://www.etymonline.com/word/balcony\" \\\n \"https://www.etymonline.com/word/barbican\" ; do\n echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 213, root Gwhen 1 part 2 (kan- 'to dig'): checking Nourai's chart\" ; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:00:19.455Z] TOOL RESULT

```
== https://en.wiktionary.org/wiki/کندن
/home/sfmqrb/git/rishe/data/verification/sources/web/f6c6b73ccca78760.txt
== https://en.wiktionary.org/wiki/خانه
/home/sfmqrb/git/rishe/data/verification/sources/web/5a1b3917e66efe34.txt
== https://en.wiktionary.org/wiki/چاه
/home/sfmqrb/git/rishe/data/verification/sources/web/38221805933028e8.txt
== https://en.wiktionary.org/wiki/خندق
/home/sfmqrb/git/rishe/data/verification/sources/web/522364dfc1625814.txt
== https://en.wiktionary.org/wiki/κόνδυ
/home/sfmqrb/git/rishe/data/verification/sources/web/b279696d6f969083.txt
== https://www.etymonline.com/word/gondola
/home/sfmqrb/git/rishe/data/verification/sources/web/670b5dd57cec54df.txt
== https://www.etymonline.com/word/balcony
/home/sfmqrb/git/rishe/data/verification/sources/web/fea0a6beeaefa20a.txt
== https://www.etymonline.com/word/barbican
/home/sfmqrb/git/rishe/data/verification/sources/web/8cc8008461c45a61.txt
```


## [2026-09-06T15:00:22.387Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in f6c6b73ccca78760 5a1b3917e66efe34 38221805933028e8 522364dfc1625814; do echo \"########## $f\"; grep -n -A6 -i \"Etymology\" $f.txt | head -60; done",
 "description": "Read Wiktionary etymologies"
}
```


### [2026-09-06T15:00:24.082Z] TOOL RESULT

```
########## f6c6b73ccca78760
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
--
146: Etymology
147- [ edit ] 
148-
149- From Middle Persian kntn' ( kantan , “ to dig ” ) , from Proto-Iranian *kánHati ( “ to dig ” ) .
150-
151- Pronunciation
152- [ edit ] 
########## 5a1b3917e66efe34
62: Etymology 
63-
64- 1.2 
65- Noun 
66-
67- 1.2.1 
68- Declension 
--
88: Etymology 
89-
90- 2.3 
91- Pronunciation 
92-
93- 2.4 
94- Noun 
--
203: Etymology
204- [ edit ] 
205-
206: Etymology tree
207-
208- Proto-Indo-European *h₂wes- 
209- Proto-Indo-Iranian *Hwas- 
210- Proto-Iranian *Hwah- 
211- Proto-Iranian *wāhana 
212- Old Persian *vahanam 
--
597: Etymology
598- [ edit ] 
599-
600: Etymology tree
601-
602- Proto-Indo-European *h₂wes- 
603- Proto-Indo-Iranian *Hwas- 
604- Proto-Iranian *Hwah- 
605- Proto-Iranian *wāhana 
606- Old Persian *vahanam 
--
853: Pages with etymology trees 
854: Ottoman Turkish entries with etymology trees 
855: Ottoman Turkish entries with etymology texts 
856- Pages using etymon with no ID 
857- Pages with entries 
858- Pages with 2 entries 
859- Persian entries with etymon 
860: Persian entries with etymology trees 
861: Persian entries with etymology texts 
862- Bashkir terms with redundant script codes 
863- Requests for native script for Punjabi terms 
864- Punjabi terms with non-redundant manual transliterations 
865- Sindhi terms with redundant transliterations 
866-
867- This page was last edited on 22 August 2026, at 04:28.
########## 38221805933028e8
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
--
157: Etymology
158- [ edit ] 
159-
160- Akin to Sogdian [script needed] ( c’t /⁠čāt⁠/ ) , Avestan 𐬗𐬁𐬝 ( cāt̰ ) , Khotanese [script needed] ( cāta ) , Khwarezmian [script needed] ( ct’ ) , Baluchi چات ( cát ) , etc.
161-
162- Pronunciation
163- [ edit ] 
########## 522364dfc1625814
62: Etymology 1 
63-
64- 1.1.1 
65- Pronunciation 
66-
67- 1.1.2 
68- Verb 
--
74: Etymology 2 
75-
76- 1.2.1 
77- Pronunciation 
78-
79- 1.2.2 
80- Noun 
--
97: Etymology 
98-
99- 2.2 
100- Noun 
101-
102- 2.2.1 
103- Derived terms 
--
126: Etymology 
127-
128- 3.3 
129- Pronunciation 
130-
131- 3.4 
132- Noun 
--
211: Etymology 1
212- [ edit ] 
213-
214- An Iranian borrowing: compare Persian کندک ( kandak ) , کنده ( kanda ) , Old Armenian քանդակ ( kʻandak ) (also from Iranian).
215-
216- Pronunciation
217- [ edit ] 
--
715: Etymology 2
716- [ edit ] 
717-
718- Pronunciation
719- [ edit ] 
720-
721- IPA ( key ) : /xan.daq/ 
--
951: Etymology
952- [ edit ] 
953-
954- Borrowed from Persian خندق ( xandaq ) , itself from Arabic خَنْدَق ( ḵandaq , “ trench, moat ” ) , ultimately from Middle Persian *handag .
955-
956- Noun
957- [ edit ] 
--
1043: Etymology
1044- [ edit ] 
1045-
1046- Borrowed from Arabic خَنْدَق ( ḵandaq ) , from Middle Persian *handag (whence Persian هندک ( handak , “ moat ” ) ).
```


## [2026-09-06T15:00:39.487Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; sed -n '595,660p' 5a1b3917e66efe34.txt",
 "description": "Read Wiktionary xane etymology"
}
```


### [2026-09-06T15:00:39.523Z] TOOL RESULT

```
 خنه ( xana ) ( dialectal , Mashhad ) 

 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₂wes- 
 Proto-Indo-Iranian *Hwas- 
 Proto-Iranian *Hwah- 
 Proto-Iranian *wāhana 
 Old Persian *vahanam 
 Middle Persian 𐭡𐭩𐭲𐭠 ( bytʾ /⁠xānag⁠/ ) 
 Persian خانه 

 Inherited from Middle Persian 𐭡𐭩𐭲𐭠 ( bytʾ /⁠xānag⁠/ ) , from Old Persian *vahanam ( “ house ” ) , from Proto-Iranian *wāhana ( “ habitation ” ) , from *Hwah- , from Proto-Indo-Iranian *Hwas- , from Proto-Indo-European *h₂wes- .

 Compare phonetically and semantically similar کده ( kada , “ house; place of ” ) . Related to دیوان ( divân ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /xaː.ˈna/ 

 ( Dari, formal ) IPA ( key ) : [xɑː.ná] 

 ( Dari, formal ) IPA ( key ) : [xɑː.ná] 
 ( Kabuli ) IPA ( key ) : [xɑː.ná] 

 ( Hazaragi ) IPA ( key ) : [xɔː.ná] 

 ( Iran, formal ) IPA ( key ) : [xɒː.né] 

 ( Iran, formal ) IPA ( key ) : [xɒː.né] 
 ( Tehrani ) IPA ( key ) : [xuː.né] 

 ( Tajik, formal ) IPA ( key ) : [χɔ.ná] 

 Rhymes: -a 

 Readings

 Classical reading ? 

 xāna

 Dari reading ? 

 xāna

 Iranian reading ? 

 xâne

 Tajik reading ? 

 xona

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 خانه • ( xāna / xâne ) ( plural خانه‌ها ( xāna-hā / xâne-hâ ) , Tajik spelling хона ) 

 house
```


## [2026-09-06T15:00:50.707Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HUB xane/kandan\"; grep -n \"hänak\\|/länak\\|kanden\\|kenden\\|hane 'Haus'\\|Haus'\" HUB.txt | head -20; echo \"=== NYB\"; grep -n \"^xānag\\|xānag\\|kandan\\|kantan\\|čāh\" NYB_vol2_glossary.txt | head -20",
 "description": "Grep Hübschmann and Nyberg"
}
```


### [2026-09-06T15:00:50.771Z] TOOL RESULT

```
=== HUB xane/kandan
777:nommene Bedeutung *Haus' (vgl. bal. ban *Haus, Lehm-
785:ban 'Haus' = ap. vahana- (vgl. skr. vasana- 'Wohnen*,
6378:Haus' oben p. 24; banu *Herrin (?) H. 178; but Idol' s. oben
8085:ap. tacara-, arm. tadar 'Tempel, Palast, Haus'; varj 'Grosse,
8943:*Haus' H. 465 ; xam 'Quelle* H. 466 , oben p. 88 Anm. ;
=== NYB
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
477:apa-cand [pend] pt. pass. thrown away daru i jün-—-it thy trunk (body) whose life is thrown away, which is lifeless 267. — Pt. pass. of *apa-can- = apa-kan-, v. apakandan, NP aužand ‘thrown’ = afgand (BQ), whence a den. v. auzandidan (BQ, Steingass). Cf also NP bazandi ‘disap- pointment, helplessness, poverty’ (BQ, Steingass), abstr. of "bažand which may safely be derived from "aBa-žand < apa- cand ‘cast down’. V. also daru.
496:apa-kandan [LMYTN-tn'; Prth RMY-] pt. = pret. pass. 3d p. sg. apakand, written LMYTN without complement HajB:8, books LMYTN-t', Prth RMY-t HajA:7; LMYTN without complement = opt. apakané HajB:15; subju. 2nd p. sg. LMYTN-h = apakanäh 1009; cond. 2nd p. sg. LMYTN-t' HWH'-? = apakand hà 2226: to throw; bē ~ to throw away, with 6 or andar 6 to, into, against 2226 etc. passim; to throw (a bucket into the well) 142°. 151; to drive (a horse) against (6) 1145; to shoot (an arrow) HajA: 7. B: 8.15; - to arouse (fear) 5278; 6 miyān ~ to provoke (enmity) 10715; pat menišn 1... m to suggest to a p.’s mind 3712-13; — pt. apakand fallen, slain 2626. — < Olr *apa-kan- and *upa-kan- (v.s. v. apa-), from kandan, q.v.; MPrthPrs >bgndn; Verbum 172, Ghilain 55; Paz. pt. awagad, pres. awa-gan- (SGV); NP afgan- dan, augandan. V. also apa-cand, frakan- dan, pargandak.
1518:frakandan [plkndn'], pt. = pret. pass. 3d p. sg. frakand to throw : bun ~ to lay the foundations 113%. — Ps. pres. plkn- ‘to build’. Cf Lat. fundamenta iacere. V. kandan.
1731:1936, 225sq. (because of Av. vikaya-, Sogd we’w ‘witness’ cannot be compared). Henning, Weller Vol. p. 297, combines Av. vikaya- with Sogd. wcw, deriving the Av. form from *vikäuya- with assi- milation of -uy- to -yy- and then short- tening of -à- > -d-. However, -uy- is not assimilated in Av.: zaoya-, haoya-, hvay- haoya-, kaoya-, gaoya-, adaoya-, mainyao- ya- (v. m&nó3), kqsaoya-, snāuya-. gukün- [gwk’n-] pres. to destroy 90?6 (Paz. substitutes vdnom, v. vànitan). — Av. (438) vi-?kan- = OP; MPrth w(y)g’- ny$n, Ghilain 71; MPrs pres gwg?n-, v. n. gwg’nysn, Verbum 189. V.s. v. kandan. gukayitan [gwk'dtn'] to bear witness, pt. = pret. pass. 3d p. sg. tgukāyīt ['gwk?dt'] 50%, — Cf Arm. lw. vkay-em.
2159:kāhišn [k'hšn', k'hyšn'] the act or pro- cess of diminishing; the state of being diminished: 68°. 983.5. 1047. — MPrs k’hysn (A-H I); NP kästan käh- ‘to lessen, to diminish’ (Paz. zähidan, cf s. v. kandan). A factitive vb. derived from the stem *ka0-, SW form of kas-, v. s. v. !kas. The form k’hy$n' represents probably a hybrid spelling combining kähisn and [k'dšn' =] "kdyišn (cf xudyišn: audh-), since -i- is as a rule not written in the ending -išn.
2196:kandan [HPLWN-tn', kndn'] kan- 1. to dig, pl. kand engraved 113%. — 2. to destroy 4271, 7114. 9918; to tear up by the root 3316, — 3. bé ~ to throw out, to drive away 34’. — Two different vbs.: 1. Av. OP (437 sg.) 2kan-‘ to dig’, whence also gukān- (g. v.); 2. kan- ‘to throw’, whence also apakandan, frakandan, par- gandan, Morgenstierne, AO I, 249; Ver- bum 172. MPrs and NP ‘to dig’, Paz. cadan, xan- with an initial x- confirmed by the Arab. lw. randag ‘trench’ and Skr khan- (pt. khāta-). V. also kanišn.
2206:kanišn [ĶPLWN-šn'] v. n. of kandan (2): ~ + jän the destruction of the vital spirit, the extinction of life 6419,
2524:mēnišn (mynšn'] thinking, thought, mind: together with gób?sn and kunišn v. göbisn ; Zartuxšt had ~ 4 fräröntar hac hamak gēhān a mind more righteous than (that of) all human beings 54%; ~ i fräröneh the way of thinking of honest people 6414; — ~ nihátan 6 to contemplate, to set one's mind on 5??*; 6 hän i ölsän ~ apar Sut hénd they inspired them 403-4; v. also apakandan, bastan, bastišn, nihä- tan, čpastan, viskaftan, vinäsitan; — pat ~ 4 Pourusäsp bim apakand 481911; pat ~ in my mind, through my inner senses 51%; hàn + či dētsr pat ~ his (spiritual) eye in his mind = his inner intuition 5226-27,
2576:miyàn [myd’n'] 1. the middle, the centre: bun ...miyün... frazdm 81; x"atài 4 ~ i asmān 78; han-tāi 6 ~ van to the middle of the tree 415; andar ~ 4 asmän 865; hac ~ dp from the middle of the water 564; — pat ~ kartan to make manifest to all, splendid 67°; 6 ~ apa- kandan to spread, disseminate 10715, — 2. prep. between: + smäh u oan damik i 30 frasang 8%; vimand i ~ Eran u Türän 4519-311; in the middle of 4815, 865. — Av. (1115 sq.) Tmaiöya-, (116 sq.) matčyčna-; MPrth mdyn; MPrs my; Paz. NP myàn.
2723:nikand [nknd] pt. = pret. 3d p. sg. 92%, uncertain: api-§ góhr  x"arrah be ~ seems to mean: he projected, threw forth, (from his own essence) its (= the earth’s) substance-light, i. e. the heavenly light which forms the substance of the material world, cf BdA p. 11? Ohur- mazd hac han i xvēš xvatēh getäh rošneh uy hac getäh rošneh karp + dāmān i xue$ frac brihénit, where gētāh rošneh seems to be a synonym of göhr xtarrah; nikandan from ni + the root kan- ‘to throw’ which is found in apakandan (g.v.).
2842:oškan [>wškn'] a verbal form used as pt. pass. and as pret. pass. 3d p. sg., to *throw: aš 6 pasēh gav apāc rānēnīt (g. v.) with the gl. kü apāc ~ ‘that is: it (his hand) was flung backward’ 485 -$; 62 gurg zat zanak (g. v.) with the gl. ki dahan évak apäk dit frot ~ ‘that is: his jaws were clasped together (the upper jaw was clasped down against the lower jaw)’ 5067; [(ka) dēn-ākāhēh ~ (when) reli- gious knowledge is overthrown DkM 33379; ātaxš mänäk aparociónik hesme m hàn i xét like a fire which has to be kindled but is thrown into wet fuel, ibid. 411°]. As it stands, this form can only be derived from *avis-kan- (the root *kan- ‘to throw’ found, e. g., in apakan- dan, q.v.), thus originally *avis-kanta- > *ēškand > oškann with assimilation of -nd > -nn, but the form is singular, as only old -nd, as far as we know, under- went this assimilation, not -nd- < -nt-. The inf. of this vb. shows the regular form expected: cé andar én mātagdān 6s- kandan [’wSkn'dn'] apāyišnīk dart druš- take [-k' +1, for -keh] vicārihēt ‘the (trouble-hardness =) troublesome diffi- culties which in this book inevitably
2953:pargän [plg?n'] "wall 935 (read, with Dh.: ... pahnai i damik; pērāmēn Harburz ~ H. is a wall all around it). — < *pari- küna- ‘that which is thrown up all around’ from pari + kan- ‘to throw’, v. apakandan; cf parisp.
2954:pargandak [plgndk'] scattered, dispersed 1092-10, 1121, — Pt. of para + kan- ‘to throw’ (Verbum 227), v. apakandan; M Prs prgn- (S); NP pargandah (the vb. is here pardgandan).
3649:kālpad i gētāhīk 8925-25, 9028-27; pat han + dašn pad frac škast trampled on it with his right foot and crushed it 5311-12; škast was broken, burst 542°; v. also s. v. stur. — Av. (1586 sq.) skand-; MPrs ‘Skn- (Sogd. 31%, 33. 59); Paz. škastan, seldom  škandan, škan-; NP  šikastan šikan-.
5518:’bgndn: apakandan
5720:"bgndn: apa-kandan
6405:awagad, awagan-: apa- kandan
6817:šahar: šahr Saharyàr: šahridar Sav: Sap šayastan: šayistan šēvašn: ščp- šihastan: sahistan šina: ščvan škaft: » škandan y škastan, TA EKOLAN šnavašni: āšnavišnēh šnāxtan, šnās-: ~
6888:xadan, xan-: kandan
```


## [2026-09-06T15:01:02.836Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== NYB xanag\"; grep -n \"x[āa]nak\\|x?nak\\|xānag\" NYB_vol2_glossary.txt | head -10; echo \"=== ARY latin index kan\"; grep -n -i \"^kan\\|khan\\|kand\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Nyberg xanag and Aryanpur index"
}
```


### [2026-09-06T15:01:02.930Z] TOOL RESULT

```
=== NYB xanag
2241:äyet do ye proclaim that every man shall come to King V.’s court 205-6; Dahäk hàn and zaman ‘BYDWN-x, cand ... to D. as long a time will be assigned as (to allow him to...) 997; ristäxez etón kind ka he will determine the Resurrection at the time when ... 3422; atän hàn 4 kart axtäyisneh (q. v.) dahet he will create un- willingness with regard to what is in- stituted by you 451; of the marriage contract: mart u zan évak apäk dit kämak bavēt, räyenend u ‘BY DWN-x, man and woman will fall in love, become engaged (v. räyenitan) and contract marriage 1044-25; zan kartan u patvand i geteh rayénitan to marry a woman and settle his family ties in this world 631%; PLK?... pat čip $ banjak kart éstat the axe was enchanted (dedicated to Hell) by means of banjak (q. v.)-water 2516-17, 284; Sah- puhr ... āpān xānak kart Sh. founded (instituted) a temple for the Waters 10914-15; the same meaning undoubtedly also in the expression šahristčin kart 113— 116; šahristan ... pat Sapistan kart was declared a harem-city 116?4-?5, — Av. (448) 2kar- ‘to recollect, to mention, to com- mend’ [from which in all probability ham + the caus. in the set phrase nivaé- čayemi hankčirayemi ‘I consecrate, I de- dicate’ (not from !kar- as Bthl. has 1t)]. First proposed by Pagliaro, RSO XXIII, 1948, 67-68 (v.s. v. ?kartak); followed up by A. Périkhanian, REA, N.S. V, 1968, 22, VI, 1969, 8, quoting the Arm. lw. &ar [< *éarna-] ‘festival oration, ho- mily’. Of course in BP as we now have it BYDWN- has always been read as kun-, but the original pres. must have been kar-, as the NW pres. of kartan ‘to make'.— V .?kartak, kartäreh (1), hangartan, nikerdi, nikeritan, patkārītan, uskärtan.
2731:nikéritan [nkdlytn'] to look, to watch, to notice; to consider, to reflect: nikér ku nē... take care not to... 45; api-š bé-c nikerit kū ... and she reflected, think- ing (+ dir. speech) 38; apfr rāyēnītan i Zartuxst nikérit he pondered as to how to do away with Z. 501%; — apāc ~ to look up 233-318; — tō an... apar nikéram pat apazonikeh u bavandak-menišneh kū-t pat han xānak nikéram i-t hast as for thee, with (my) heavenly powers and perfect thinking I see through thee, namely, I see thee in that house which is thine [1. e. Hell] 5324-26, cf s. v. aržan- tkénitan. — Paz. nigerīdan, nigaridan ; NP ntgarīdan, -istan. The spelling nkdl is attested by FrP 10. As the spelling -dl- regularly denotes -ér- we have to establish
3109:must go back to *pati-yam- ‘to take hold of’, from Av. (1262sg.) yam-, chiefly with preverbs. I find *pāyam as a v. n. in two passages: 1. DkM 285 aköman ... menisn päyam ‘A. holding Mind in his grasp’; 2. ibd. 501? páyam hešm andar ménisn “Wrath taking Mind in his grasp’ (?). — Zsprm VIII, 4 has a somewhat divergent, perhaps more original version of the story 441-9: ^L ZLWN ‘L y’twk’n, MH-t L>? HWH-nd byšznyt'l, BR’ L'WHL ‘L h'nk' ZLWN, YDH BYN ml PWN "MŠH' ZY TWR’ ZY MDM thé YDLWN-t', hysme bwd wt'p' PWN NPSH-tn' zhk' MNW-t PWN 'škmb' = mà šav o yātūkān, cē-t nē hend bēšazanī- tar, bē apāc 6 xanak šav, dast andar mal pat rógn % gāv i apar ātaxš burt, hésm-ic bod vitāp pat x"ēš-tan zahak ké-t pat aš- kamb ‘do not go to the sorcerers, for they cannot heel thee, but go back home, rub thy hand with ox-tallow which has been. set on fire, and burn fragrant fuel for the benefit of thy offspring which is in thy womb’.
3678:. ziyan u pašēmānēh nč rasēt 682122 (similarly 68—72 passim); hakar-at ham- bun-ic mihr i amäh hast 99; xānak i-t nest . . . i-t hast the house that does not belong to thee ... that belongs to thee 5320-21.25-26. as the logical subj. of an inf. or a v.n.: kü-t ... né apasihenitan that is: it is not up to thee, thou wilt not be able to annihilate 46° gl.; ce-t ne apar tarsišn for thou shalt not be afraid 5821, adak-it én tigr patkafom then I shall shoot off this arrow against thee 100%; — 3. the dir. obj.: kü-t Az dev nē frepet 68%; (kit...) api-t... dev 6 došax" nē kēšānd
=== ARY latin index kan
1834:AKANDAN, AKANDE, AKANESH (u61~ 81 dist oaisl ais) — (PERSIAN) qui
1837:GONEJETE, GANA-, GONETI, ‘AGANDAN,AKANDAN.(PAHLAVI) 5 sy,
6735:BUCK: 809 KHADATI, KHANATI, KHAD-
6739:KANDU (LITHUANIAN) gle}
7061:CHICHTAC POLISH) ling) KHANUEL.KANDA
7600:KAN, KUNNA:(OLD FRISIAN) oS5323 HAVESTAN) «lie 3!
7602:KAN, KUNNA (OLD PERSIAN) ilealy
7603:KAN, KONNEN (GERMAN) giJT ADANA, DAN- :
7606:KANDE, KAN DANISH) Sheil HOSSETIC) guy)
7607:KAN SWEDISH) 555 yo ZONIN, ZONUN, ZONUM.
8987:LUCHI ROKHAN HAFGHAND) (5-4) Ji}
11076:SCITAN :(OLD ENGLISH) A Sl SHIKANDIN _ (KURDISH) 53,5
11969:KHAN., KHANATI KAN- AVESTAN) gle 3)
11971:| KANDAN, KANTAN | :(PAHLAVD) 514
11973:TOKORN St=CS~S*~S~Sa KENAN, CHIKANDIN:(KURDISH) 52,5
11975:AMINDAROV: (DIG) 212 KANDAL, KINDEL
12258:KAN HOLD PRUSSIAN) 5 gop
12909:KAN . HITTITE) GANTUMA HAVESTAN) glo)
```


## [2026-09-06T15:01:11.804Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY; awk 'NR<=11975 && /\\[pdf page/ {p=$0;l=NR} END{print \"near 11969:\",p,\"line\",l}' ARY_latin_index_pages.txt; awk 'NR<=1837 && /\\[pdf page/ {p=$0;l=NR} END{print \"near 1834:\",p,\"line\",l}' ARY_latin_index_pages.txt; sed -n '11960,11985p' ARY_latin_index_pages.txt",
 "description": "Locate ARY index pages"
}
```


### [2026-09-06T15:01:13.971Z] TOOL RESULT

```
near 11969: [pdf page 411] line 11962
near 1834: [pdf page 66] line 1831
| GALVA (LITHUANIAN) gy) HAVED, HAFD
| GALVA LATVIAN) (63) 593 HOLD HIGH GERMAN) yf gllT
[pdf page 411]
es | NY
BUCK 7212-213 ‘REFERENCES ac tKany
ONIONS: « qaeanyan = poKom) SS SsSC=<CS~S
AMINDAROV: gi _ (BEAD) 234 BARNHART: (HEAD) 470
eer i gbli oly DELAMARRE: (TETE) 100
Se any aor at rata
KHAN., KHANATI KAN- AVESTAN) gle 3)
AKAN ARMENIAN). 3} KAN- HOLD PERSIAN) jeoly gs),
| KANDAN, KANTAN | :(PAHLAVD) 514
‘REFERENCES enthey -GANIN HOSSETIC) gins)
TOKORN St=CS~S*~S~Sa KENAN, CHIKANDIN:(KURDISH) 52,5
‘MACKENZIE: (DIG) 110 AFGHAN) (4) gil
AMINDAROV: (DIG) 212 KANDAL, KINDEL
Wey sebloby SANSKRIT) ey Suite
seatlaoy
UgT aaa ss GtKl lojly y KERBEN GGlsT y CARVE plSil sl fly cmd cal ley ~1
ashasT (*GERBH) $9 plo, 9 te Gey erly Gj} ns ot! Tals Jy jh colt
(147:BARNHART)
AYE genie »3 POKORNY ct go Fi -¥
dep JB cents eal SLPS oh aa) a te et zlslt gti gal ila! ge lanjly Gala oT
weedl aby 1S (4) oF
KIDERE, KUDER, KUDA, KUVA AVESTAN) gto)
KUM HAFGHAND) (34) gil KU, KUTHRA, KUDA
```


## [2026-09-06T15:01:29.974Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt; do echo \"--- $f\"; grep -c \"\" $f; sed -n '200,205p' $f; done 2>/dev/null | head -60",
 "description": "Inspect BQT volumes"
}
```


### [2026-09-06T15:01:31.766Z] TOOL RESULT

```
--- BQT_v1_pages.txt
32486
نعستین بابتخت هخامنشیان بوده و بو نانیان ثرا 958۳88068( خوانده‌اند.
یس از مر گ کمبوجیه پسر کورش که داربوش پپادشاهی رسید » سرزمینی که
امروژه تخت جمشید گوبیم » پایگاه هخامنشیان بر گز بده شه .گوبا ساختمان
این بایگاه درسال ۵۱۸ بیش از میلاد مسیح آغاز شده باشد و آنرا نونانیان
8 نامیده‌اند . حمدالله مستوفی در نزهة القلوب که درصال ۷۰
هجری نوشته آنرا چپل منار خوانده و سیاحان بیش نیز ۲نجارا بهمین نام
--- BQT_v2_pages.txt
41071

                                                     ‫قمری م‪.‬طبعة کربلائی محمدحسین طهرانی‬
    ‫لندن ‪ ۸۲۹۱‬میلادی م‪-‬قالة سوم باهتمام گای‌لیسترانج ‪ .‬بربل (لیدن) ‪ ۱۳۳۱‬قمری ‪.‬‬

                                           ‫الکرملی ‪ .‬قاهره ‪ ۸۳۹۱‬میلادی ( = نشوء اللغةا(عرییة)‪.‬‬
‫مصحح د کتر پرویز‬           ‫ور لیجا ‪( .‬نفسیر فارسی سور توسصف)‬                 ‫‪ -. ۳۴‬توسف‬
--- incoming/BQT/BQT_v3_pages.txt
51425
‎ole‏ جمل ‎UT‏ سیصد کیرند . این حرف به «چ» ودی» (رلك: ديباچة مولف ص(یح))بدل‌شود.
برای معانی «ش» ‎SD pt‏ ازديباچة ملف. ش (ضمیر سوم شخضص مفرد) درپپلوی 0ا5-,پارسی
باستان 51081 - «بارتولمه ۱۷۲۱ ۰ رث:. تیب رک ۲۱۲-۲۰۹؛ ‎Certs‏ (بط) ازدیباچة مولف
(ضمایی) .

SLOT gaat ‏(امرازبودن)‎ Ate) GE) ‏شا‎ : Nf . ‏رك: شاباش‎ - ٩
--- incoming/BQT/BQT_v4_pages.txt
22553
نبود. خوانندگان محترم میتوانند به جزوه‌های دستوری که نگارنده تحت
هنوان «طرح دستورز بان فارسی>» به طبم میرساند, رجو ع کنند.
همچنین ابدال حروف به یکدبگر در زبانشناسی تحت قواعدیست
وموقع هرحرف‌درآفاز یا پایان‌کلمه ونوع حرف ماقبل‌وما بمد درتبدیلتأثیر
دارد ذ کراینمباحث - که تا کنون درایران سابقه‌ندارد - طبعاً درین کتاب
نيامده است .
```


## [2026-09-06T15:01:38.711Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== v2 xani/xane\"; grep -n \"خانی\\|غانه\" BQT_v2_pages.txt | head -10; echo \"=== v4 kandu\"; grep -n \"کندو\\b\\|کندوج\\|کندوک\\|کندره\" incoming/BQT/BQT_v4_pages.txt | head -15",
 "description": "Grep Borhan for xani, ghane, kandu"
}
```


### [2026-09-06T15:01:38.813Z] TOOL RESULT

```
=== v2 xani/xane
1148: ‫وبربدن آن بیم حلاکت باشد ویشتی مردم‌فرغانه‬           ‫سردوش ناخنها دارد وخودرا سرنگون از درخت‬
5871:  ‫رك ‪ :‬چکاو ‪.‬‬            ‫‪7‬‬                  ‫‪ :‬چغانه‪.‬‬   ‫رک‬       ‫‪۵‬‬                                    ‫‪.‬‬   ‫‪ :‬چغانان‬                ‫رک‬      ‫‪-‬‬     ‫‪۳‬‬
6039:                                                                       ‫مخفف چغانه است‪.‬وآن چویی باشد میان شکافته‬
8077:                                                            ‫ابلخانی (ابلکانی )که درتبر بزوبقداد‬
9203:                               ‫بودن است ‪٩‬‏ ‪۰‬‬   ‫و متواضع‬         ‫فارسی (‪ )۳‬بمه‌نی تخم هرغ باشد چه خانینه‬
10577:     ‫‪ ,‬اشروسنه ‪ ۰‬سیام » فرغانه و سمرفند ) « معجم‌البلدان »‬             ‫تان‬
12016:                                 ‫© _ رك ‪ :‬خانیدن (خساییدن)‬                    ‫آرا قخاید» آورده ‪.‬رك ‪ :‬خسانیدن‬
22709:                      ‫آنرا بعربی سلسالبول کوبند ‪.‬‬         ‫میداسته اند و مردمان در عبادتغانهای خود‬
23919:    ‫«منوچهری دامخانی ‪ ۸۲۱‬ورك ‪ :‬رز‬
=== v4 kandu
```


## [2026-09-06T15:01:47.683Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== v3 kandu\"; grep -n \"کندو\" incoming/BQT/BQT_v3_pages.txt | head -10; echo \"=== v3 kandan\"; grep -n \"کندن\" incoming/BQT/BQT_v3_pages.txt | head -5; echo \"=== v4 sample letters\"; grep -n \"کندو\\|کندن\\|کنده\" incoming/BQT/BQT_v4_pages.txt | head -10; echo \"=== v4 what letter\"; sed -n '2000,2010p' incoming/BQT/BQT_v4_pages.txt",
 "description": "Find kandu in Borhan v3/v4"
}
```


### [2026-09-06T15:01:47.797Z] TOOL RESULT

```
=== v3 kandu
1682:. ۴ ‏رافرست ددهدتابازی‌دمگ رکندوبازی‌قايم شود‎
2252:میگذارد وبروشنایی ‎aS oT‏ چرا میکندوآبرا
19877:‎ST‏ چیزی صورتی که دارد رها کندوصورت
25170:‎x‏ کايك ۱ ‎eee‏ بای ‎aml‏ بر وزن ‎OT‏ تخم کندوبچه‌بر آرد - و رفیده رانیز گفته‌اند
27178:‏کانور © بروزن کافور ء کندوی غله را
30115:حم از کندم ‎yogi‏ کندوك ‎(GT)‏ وهم‌خالی زنان کرسان.
36624:‏۴ - «کندو» (ه.م.) باین معنی است ودرمتن صحیف شده (سراج‌اللقات بنقل فرهنگه
36751:‏کندوج باشد ۴ - و جنماول هم پاین‌منی وهم
36754:‏کندواله ۴ = ‎ee‏ اول بروزن‌خرد(۱)
36764:‏کندوری
=== v3 kandan
3678:‎yet‏ کندن‌هم آمده است ۴ -و پژمرده شدن‌را
4881:‎shikafti n‏ (شکافتن , جدا کردن ‎(Gary per‏ ,بوانی 838008 (کندن .شکستن).ممنی کندن
6764:کریند وبدیرازی کندنای کوهی خوانند. وبعضی
8854:‏۱ « غیرافکن.ره : اوژن.اوژندیدن , او کندن. ۴ - از:شیر ۳ با ‎Aga) (i=)‏
9690:‎Ge) -‏ «صرع (بالفتح وبکسر) برزمین افکندن ۰ ۰ . و بالفتح بیماربی است که از
=== v4 sample letters
1403:را مجاب ومحکوم کردند وبعنوان خروج ازدین » بزندان افکندند و چندان عذاب دادند تا بدرود
1835:وسین می نقطه » چو ب کنده راکوبند که درپس | کوکب عطارد است .
2337:بمعنی گداخته باعد ؛ و ختح اول هم آمده ] قفل و چوب کنده باشد (۳) که دریس دراندازند
2634:مر۸۵ ۱ - يك شخص واحد را کوبند روزی بمیرد و طریق‌کندن آن چنان است که
2644:مرد ماگ * - بنم ثالك بروزنم رجمك. کنده شود وسگه کن مردم کیاه
2730:زشت کردالیدن - و بدست زدن - و پاره‌ای بر کندن: از خمیر و جزآن .> « منتهی‌الارب >.
3317:است . ومکنده را نیز کوبند که فاعل باشد چه مزیدن
3450:و داز ۱ 1 | کوشت را بد بوی و کنده سازد و کرم در آن
3664:مشاش - بنتح اول و ثانی بالف کشیده بمعنی آنبوه و بسیار وپر و لبریز وسطین وکنده
3838:باشد که‌درست کنده ری وسکون میم در آخر جانوری باشد سیاه رنگه
=== v4 what letter
هچرگ ۱ - بفتح اول و(۱) نانی بر مچه ۴ - بنم اول و فتح نالی مشدد ,
وزن تگر3 . بمعنی‌بیگار(٩)‏ وکار فرمودن بزور | برغت راکویند و آن گیاهی است بهاری مانند
وستم ومی اجرت باشد . اسفناج که درآشپاکنند .
ها مجه‌و۱؟-- اوبالف کشیده
مچفس ؟ - منم از شیدن باه | چه و نم اول وواوبالف کشید
کدس نات آشی‌باشد که ازمچه پزند چه وا بمعنی‌آش است.
رو ی ۳ ومچه گیاهی باشد خود رو وبهاری شبیه پاسفناج
مچك بروزن لچك » بمعنی عدس | که بعربی قنابری خوانند .
باشد وآن غله‌ایست که در آشپا کنند و گاهی مچچیدن - بنتح اول بر وزن رسیدن »
عرسه لیزیزند ؛ وبسی گویند بادا کوهی است | بمعنی خرامیدن و رفتاری باشد از روی داز
وآن تلخ میباشد وآنرا بربان کرده در آش پیمار | و زیبایی ‎٩‏ - ویمعنی دیدن هم‌آمده است ۷ ؛
```


## [2026-09-06T15:01:54.034Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '36735,36775p' incoming/BQT/BQT_v3_pages.txt; echo \"=== pdf page tag\"; awk 'NR<=36775 && /\\[pdf page/ {p=$0;l=NR} END{print p,l}' incoming/BQT/BQT_v3_pages.txt",
 "description": "Read Borhan kandu entries"
}
```


### [2026-09-06T15:01:55.840Z] TOOL RESULT

```
‏- النامی » در معنی سبیخه « کندش»
و5 رك : سروری » غباث‌القات :

‏دولت کشاده رخت ‎OVS pile‏ .
«حافظ . مصحح قزونی‌ص‌قیح».
- از : کند ( کندن ) +-مند

‎)۳۱۸ ‏قاطع‎ olay (
[pdf page 500]
وا
‎ae,‏ باشد ۱ .2

‎IT‏ - بنتح اول و سکون ثانی‌وئالت
بواو کشیده » ظرفیرا گویند ‎ashe‏ خم‌بز رک ی که
آرا از کل سازند و پراز غله کننه و معرب ‎OT‏
‏کندوج باشد ۴ - و جنماول هم پاین‌منی وهم
بمعنی غول بیابای‌آمده است ۴

‏کندواله ۴ = ‎ee‏ اول بروزن‌خرد(۱)
ساله . مرد بل ای وی ‎Ket‏ زا کون -

‏و پسر امرد بدالذام وزشت را 5 گفته‌اند و اورا

‏کرتله هم میگونند .

‏(۱) خم ۰۱ چش : خورد ساله .
‎Sy - ۱‏ 4 شود بوم ما کندمند

‏کندوری

‏کندوده ؟ - بر وزن طتبوره » سفرء
چرمین را گویند - و پیش انداز را یز کنته الد
وآن پارچه‌ای باشد که در پیش سفره و بر روی
زانوی مردم بگترانند نا چیزی از خوردلی بر
زمين و دامن مردم نریژد » و این رسم در مك
روم جاری ‎cal‏

‏کندوری ۱
و دتار خوان چرمی ‎IT‏ و بسنی پیش
انداز ‎ala,‏ یعنی ‎slag yl‏ که در پیش ‎ope‏
=== pdf page tag
[pdf page 500] 36744
```


## [2026-09-06T15:02:09.888Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== v3 ghane\"; grep -n \"غانه\" incoming/BQT/BQT_v3_pages.txt | head -10; echo \"=== v3 damghan\"; grep -n \"دامغان\" incoming/BQT/BQT_v3_pages.txt BQT_v2_pages.txt | head -5; echo \"=== v2 xane headword region\"; grep -n \"خانه\\b\" BQT_v2_pages.txt | sed -n '1,10p'",
 "description": "Grep Borhan for ghaneh and Damghan"
}
```


### [2026-09-06T15:02:10.002Z] TOOL RESULT

```
=== v3 ghane
10644:‎Gye‏ فرغانه ‎GULL.‏ را در مقابل تر ‎OST‏ خرلخیه » صرحدیست که طراز نام دارد و ب رکنار
22688:‏و صرء » و بالق شهری است بفرغانه.» « منتهی‌الارب >. . ‎٩‏ ۳ قباچه («م.)ترشیدی»
36920:وان بیشتر در ولایت جمن و فرغانه رویدوبعریی
=== v3 damghan
incoming/BQT/BQT_v3_pages.txt:1648:‏دامغان وبطام ۵ .۷
incoming/BQT/BQT_v3_pages.txt:2770:«* منوچهری دامغانی ‎VEY‏
incoming/BQT/BQT_v3_pages.txt:7930:‎Yoo‏ ور : شوه. ۴ - جپانگیری برای ‎gl‏ همنی بیت ذبل را از منوچهری دامغانی
incoming/BQT/BQT_v3_pages.txt:22615:نیز گوند (محذف با) . منوچهری ( دامغانی ) کوید :
incoming/BQT/BQT_v3_pages.txt:25076:LOW, ‏منوچپری دامغانی‎ «
=== v2 xane headword region
401: ‫گویندکه انکور را درآن لکد زنشد تا شیر‬           ‫پارسیان شخصی را گوبندکهآنچه شرآ ش‌خانه‬
549:‫جام بر سنگ ردن مهکنایه‌از توبه‬                         ‫ګوبند که در پنجره های خانه و حمام بکار‬
594:‫جامگی؟ سس میم بروزن خانگی»‬                                              ‫آسمانه » آبنه خانه راکوبند » وآن خانه‌است‬
662:‫و خانه‌ای که رخوت پوشیدلی وقیر پوشیدلی در‬        ‫رخوت پوشیدلی وغیر پوشیدلی ودوخته ولادوخته‬
672: ‫‪۶ - ۴‬یس مأمون آن روز (عروسی) جامه خانه‌ها عرض کردن خواست و ازآن‌هزار‬
834:‫‪O‬‬                       ‫است ؟‪ .‬‏‪E‬‬                          ‫جاندا نه= بورزن کارخانه » اپزیش‬
965:‫جای مند = ببامریومزن پای‌بند ‪.‬‬                    ‫جاو یداه ه بر وزن تازنخانه ‪,‬‬
1743:  ‫ولیکن عامیان لو در آوردند ‪ .‬این روز برکاغذ ها نوبند و بدرر خانه آویزند تا اندرو کزند‬
1901:                                                    ‫کج شو و خمکرد ‪ -‬و سقف‌خانه و چوب بندی‪‎‬‬
1950:       ‫رشتن پنبه بردوكپیچیده‌شود ‪ ۴‬؛ وبا جیم‌فارسی‬                     ‫خانه را گونند ‪ -‬و طاق ابوان را همگفته انب‬
```


## [2026-09-06T15:02:21.665Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n \"https://abadis.ir/fatofa/غانه/\" \\\n \"https://abadis.ir/fatofa/کنند/\" \\\n \"https://abadis.ir/fatofa/بالاخانه/\" \\\n \"https://abadis.ir/fatofa/خانی/\" ; do echo \"== $u\"; python3 tools/fetch_source.py \"$u\" --note \"page 213: Dehkhoda/Mo'in check for ghaneh, kanand, balaxaneh, xani\"; done",
 "description": "Fetch abadis entries"
}
```


### [2026-09-06T15:02:29.906Z] TOOL RESULT

```
== https://abadis.ir/fatofa/غانه/
/home/sfmqrb/git/rishe/data/verification/sources/web/08656de7d041e588.txt
== https://abadis.ir/fatofa/کنند/
/home/sfmqrb/git/rishe/data/verification/sources/web/5505f84618f4aefe.txt
== https://abadis.ir/fatofa/بالاخانه/
/home/sfmqrb/git/rishe/data/verification/sources/web/bb448bdcfe2b00ef.txt
== https://abadis.ir/fatofa/خانی/
/home/sfmqrb/git/rishe/data/verification/sources/web/0933150cc574a7cf.txt
```


## [2026-09-06T15:02:32.644Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 08656de7d041e588 bb448bdcfe2b00ef 0933150cc574a7cf 5505f84618f4aefe; do echo \"########## $f\"; head -c 3000 $f.txt | tail -c 2500; echo; done",
 "description": "Read abadis pages"
}
```


### [2026-09-06T15:02:34.408Z] TOOL RESULT

```
########## 08656de7d041e588
ب ).
 غانه. [ ن َ ] ( اِخ ) شهری در کنار فرات. ( آنندراج ) ( انجمن آرا ). شهری است در کنار فرات و صحیح عانه است ، چنانکه صاحب قاموس گوید ( فرهنگ رشیدی ) همین قول صحیح است. رجوع به التفهیم چ همائی ج 4 ص 198 و رجوع به منتهی الارب ( عانه ) شود.
 غانه. [ ن َ ] ( اِخ ) نام شهری است در حدود یمن. گویند خاک آن شهر طلا دارد زیرا که خاکروبه آن رامیشویند سونش طلا برمی آید. ( برهان ) ( انجمن آرا ) ( آنندراج ) : وز زمین یمن آنچ از شهرهای صنعاء جنوبی است ، چون ظفار و حضرموت و عدن و دنقله شهر نوبیان و غانه از شهرهای سپاهان مغرب و آنگاه به دریای محیط رسد به مغرب. ( التفهیم بیرونی ص 198 ). شهری است به مغرب. ( منتهی الارب ). مؤلف نزهة القلوب آرد: مغرب از اقلیم اول است و مملکتی فراوان بی اندازه دارد بلاد بزرگش مدینةالفیل و آن را قطانیه خوانند. شهری بزرگ است و در او کنایس بسیار و عجایب و غانه و قمراطه و قصرالفلوس و دیگر بلاد بزرگ. ( نزهة القلوب چ لندن مقاله ثالثه ص 272 ). و در تاریخ بیهق در ضمن فصل ولایات مشهور و نواحی معمور ربع عالم آرد: اول ولایت زنج است که آن را زنگبار خوانند و شهر معظم آن را سفالةالزنج و قنبله خوانند دوم بلاد سودان است نهایت عمارت اقصای مغرب شهر بزرگتر آن را غانه خوانند. ( تاریخ بیهقی ص 17 ). مؤلف تاریخ ایران باستان آرد: و پس از آن در ازمنه بعد بجایی از افریقا منتشر شد ( تمدن ) که حال موسوم به گینه است. ( تاریخ ایران باستان ص 27 ) و مراد از گینه در این جاهمان غانه سودان است. و در معجم البلدان آرد: کلمةعجمیة لااعرف لها مشارکاً من العربیة و هی مدینة کبیرة فی جنوبی بلاد المغرب متصلة ببلاد السودان یجمع الیها التجار و منها یدخل ف
########## bb448bdcfe2b00ef
م عمارت دوطبقه. اطاقی که بر پشت بام سازند. ( از آنندراج ).اطاقی که فوق اطاق دیگر ساخته شده باشد. ( فرهنگ نظام ). منظر. عمارت فوقانی. ( ناظم الاطباء ). خانه طبقه ٔدوم. ( لغت محلی شوشتر ). خانه روی خانه : 
از هوای قامتش تا پر شده ست 
سینه صدچاک بالاخانه است. میرزاعبدالغنی ( از آنندراج ).
 بالاخانه. [ ن َ ] ( اِخ ) نام قریه ای به باکو دارای معادن نفت بسیار. ( یادداشت مؤلف ).
 بالاخانه. [ ن َ ] ( اِخ ) دهی است از بخش پشت آب شهرستان زابل که در 8 هزارگزی باختری بنجار و 3 هزارگزی راه فرعی ادیمی به زابل در جلگه واقع است. ناحیه ایست دارای آب و هوای گرم معتدل و 1133تن سکنه. آب آنجا از رودخانه هیرمند تأمین میشود. محصول عمده آن غلات ، لبنیات. شغل مردمش زراعت و گله داری و گلیم و کرباس بافی. راه آنجا مالرو است. ( از فرهنگ جغرافیایی ایران ج 8 ). 

 فرهنگ فارسی

 ( اسم ) خانهای که بالای خان. دیگر ساخته شود اطاقی که در طبق. فوقانی ساختمانی قرار دارد .
دهی از زابل 

 فرهنگ معین

 (نِ ) (اِمر. ) ساختمان کوچک با یک یا چند اتاق در قسمت فوقانی خانه و مستقل از آن . ، ~ را اجاره دادن کنایه از: عقل سالم نداشتن ، سخنان پریشان و نامربوط گفتن . 

 فرهنگ عمید

 ۱. خانه ای که بالای خانۀ دیگر ساخته می شود.
۲. اتاقی که در طبقۀ دوم یا سوم یا بالاتر ساخته شده. 

 گویش مازنی

 /baalaa khaane/ طبقه دوم ساختمان

 دانشنامه عمومی

 بالاخانه، روستایی در دهستان ادیمی بخش مرکزی شهرستان نیمروز در استان سیستان و بلوچستان ایران است. 
بر پایه سرشماری عمومی نفوس و مسکن در سال ۱۳۹۵، جمعیت این روستا برابر با ۱٬۲۱۰ نفر ( ۳۴۱ خانوار ) بوده است. [ ۱] 
 wiki: بالاخانه 

 این نوشته برگرفته از س
########## 0933150cc574a7cf
 کنید 

 لغت نامه دهخدا

 خانی. ( اِ ) حوض و چشمه آب را گویند .( برهان قاطع ) ( آنندراج ) ( ناظم الاطباء ) : 
دو خانی پدید آید اندر دو چشم 
از آن روی ناری و زلف دخانی. قطران.
گوید این خاقانی دریامثابت خود منم 
خوانمش خاقانی اما از میان افتاده قا. خاقانی.
صدقه جاریه آنست که پادشاهان مدرسه ها سازند و وقفها کنند و مساجد و خانی و چشمه سارها و کهریزها آورند. ( راحة الصدور راوندی ).
آب کوثر نه آب خانی بود
چشمه آب زندگانی بود. نظامی.
ز شرم آب آن رخشنده خانی 
بظلمت رفته آب زندگانی. نظامی.
اولش گرچه آب خانی داد
آخرش آب زندگانی داد. نظامی.
خانیی آب بود دور از راه 
بود از آن خانی آب آن بنگاه. نظامی.
کوزه پر کرد از آب آن خانی 
تا برد سوی خانه پنهانی. نظامی.
نام خود عاشق نهادی چیست این افسردگیها
عاشقان را سینه آتش خانه باید دیده خانی. اوحدی.
یک روز نمی آیی تا در غم خود بینی 
صدخانه چون دوزخ صد دیده چون خانی. اوحدی.
حاصل ما ز زلف و عارض اوست 
اشک چون خون و چشم چون خانی. اوحدی.
تو ماه و مرا پیکر از دیده ماهی 
تو خان و مرا دیده از گریه خانی. خواجو ( از شرفنامه منیری ).
 || تالاب. باتلاق و از این معنی است «مرداب گاوخانی ». رجوع به حاشیه مرقوم بر «خانی » در همین صفحه شود. || آب صاف. ( ناظم الاطباء ). || زری است رایج در ترکستان . ( برهان قاطع ) ( ناظم الاطباء ) ( آنندراج ) ( غیاث اللغات ) : 
خانی دیگران بیک خانی. ظهوری ( از آنندراج ).
|| زر خالص. ( برهان قاطع ) ( آنندراج )( ناظم الاطباء ). || مزید مؤخر امکنه چون :تیرخانی ، چاخانی ، ( چاه خانی )، سرخانی ، سیاه خانی. || از مبادی گاه شماری چون هجری و یزدگردی و جلالی و غیره : فامّا در عصر مترجم که آن شهور سنه �
########## 5505f84618f4aefe
�رهنگ فارسی معین ). || بیلی را نیزگفته اند که سر آن خمیده باشد و برزیگران کار فرمایند. ( برهان ) ( ناظم الاطباء ) ( فرهنگ فارسی معین ). بیلی که سر آن کج باشد ( خمیده ) و برزگران دارند و ظاهراً کلند است. ( آنندراج ) ( از فرهنگ رشیدی ). بیلی باشد سراندرچفته ، برزگران دارند و به ماوراءالنهر بیشتر بود. ( لغت فرس اسدی چ اقبال ص 90 ). بیلی باشد سرچفته که برزگران دارند و آن را به زبان تازی معول خوانند. ( اوبهی ). کلند. کلنگ. آلتی با سری آهنین و دسته چوبین به سه چهار بزرگی تیشه که بدان زمین کنند و امروز کلنگ گویند. ( یادداشت به خط مرحوم دهخدا ): العزق ؛ شکافتن زمین به کنند. ( تاج المصادر بیهقی ) : 
مرد دینی رفت و آوردش کنند
چون همی مهمان در من خواست کند. رودکی ( از لغت فرس چ اقبال ص 9 ).
وگرت خنده نیاید یکی کنند بیار
و یک دو بیتک از این شعر من بکن به کنند. ابوالعباس ( از لغت فرس ایضاً ).
برگیر کنند و تبر و تیشه و ناوه 
تا ناوه کشی خار زنی گرد بیابان. خجسته ( از لغت فرس ایضاً ).
آنچه ببخشید اگر گنج نهادی زمین 
گشتی تا پشت گاو کنده به روئین کنند. سوزنی.

 فرهنگ فارسی

 ( اسم ) ۱ - افزاری است چاه کنان و گلکاران را که بدان زمین کنند : بر گیر کنند و تبر و تیشه و ناوه تا ناوه کشی خار زنی گرد بیابان . ( خجسته ) ۲ - بیلی که سر آن خمیده است و برزیگران ( مخصوصا در ماورائ النهر ) با آن کار میکردند . 

 فرهنگ معین

 (کَ نَ ) (اِ. )افزاری که چاه کنان و گل کاران با آن زمین را می کنند. 

 فرهنگ عمید

 ۱. بیل.
۲. نوعی تبر یا بیل سرکج که با آن خار از زمین می کندند: برگیر کنند و تبر و تیشه و ناوه / تا ناوه کشی خار زنی گرد بیایان (خجسته: شاعران بی دیوان: ۱۶۱ ). 

 پیشنهاد
```


## [2026-09-06T15:02:47.665Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; echo \"##### kondy\"; grep -n -B3 -A12 \"Etymology\" b279696d6f969083.txt | sed -n '1,60p'",
 "description": "Read Wiktionary kondy"
}
```


### [2026-09-06T15:02:47.712Z] TOOL RESULT

```
##### kondy
59- Toggle Ancient Greek subsection 
60-
61- 1.1 
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
74- Derived terms 
--
140- Ancient Greek
141- [ edit ] 
142-
143: Etymology
144- [ edit ] 
145-
146- Like many words ending in -ῠ ( -ŭ ) , it is a loanword . Furnée compares κοτῠ́λη ( kotŭ́lē , “ cup ” ) , suggesting a Pre-Greek origin, while Szemerényi refers to late Neo-Babylonian 𒃶𒁺 ( kandu , “ vessel ” ) which is considered a West Semitic borrowing from Aramaic כנדא ( kandā , “ vessel, pot; specifically for wine ” ) from Sanskrit कन्दु ( kandu , “ pot ” ) and ultimately Proto-South Dravidian *kiṇṭV- ( “ pot ” ) , found also in the forms כַּד ( kaḏ ) , כדא ( kaddā ) , Biblical Hebrew כַּד ( kad ) , Punic 𐤊𐤃 ( kd ) , Ugaritic 𐎋𐎄 ( kd ) , and Ancient Greek κᾰ́δος ( kắdos ) .
147-
148- Pronunciation
149- [ edit ] 
150-
151- IPA ( key ) : /kón.dy/ → /ˈkon.dy/ → /ˈkon.di/ 
152-
153- ( 5 th BCE Attic ) IPA ( key ) : /kón.dy/ 
154-
155- ( 1 st CE Egyptian ) IPA ( key ) : /ˈkon.dy/
```


## [2026-09-06T15:02:49.843Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in 670b5dd57cec54df fea0a6beeaefa20a 8cc8008461c45a61; do echo \"##### $f\"; grep -n -i -A10 \"^ *\\(gondola\\|balcony\\|barbican\\)\" $f.txt | head -40; done",
 "description": "Read Etymonline entries"
}
```


### [2026-09-06T15:02:51.558Z] TOOL RESULT

```
##### 670b5dd57cec54df
6:Gondola - Etymology, Origin & Meaning 
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
--
23: gondola (n.) 
24-
25- 1540s, "long, narrow flat-bottomed boat used in Venice," from Italian (Venetian) gondola , earlier in English as goundel , from Old Italian gondula , of unknown origin; according to Barnhart, perhaps a diminutive of gonda , a name of a kind of boat. Used of flat, open railway cars by 1871. Meaning "cabin of an airship" is from 1896, though it was used hypothetically in 1881 in a futurism piece titled "300 Years Hence." Of ski-lifts from 1957.
26- also from 1540s 
27-
28- Entries linking to gondola 
29-
30- gondolier (n.) 
31-
32- "man who rows a gondola," c. 1600, from French gondolier and directly from Italian gondoliere , agent noun from gondola (see gondola ).
33-
--
110: gondola 
111- gondolier 
112- Gondwana 
113- gone 
114- goner 
115- gonfalon 
116-
117- Advertisement Close 
118- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
119-
120- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
##### fea0a6beeaefa20a
6:Balcony - Etymology, Origin & Meaning 
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
--
23: balcony (n.) 
24-
25- 1610s, "platform projecting from a wall of a building surrounded by a wall or railing," from Italian balcone , from balco "scaffold," which is from a Germanic source (perhaps Langobardic *balko- "beam"), from Proto-Germanic *balkon- (see balk (n.)). With Italian augmentative suffix -one . From 1718 as "gallery in a theater." Until c. 1825, regularly accented on the second syllable. Related: Balconied .
26- also from 1610s 
27-
28- Entries linking to balcony 
29-
30- balk (n.) 
31-
32- also baulk , Middle English balke , from Old English balca "ridge, bank," from or influenced by Old Norse balkr "ridge of land," especially between two plowed furrows, both from Proto-Germanic *balkon- (source also of Old Saxon balko , Danish bjelke , Old Frisian balka , Old High German balcho , German Balken "beam, rafter"), from PIE root *bhelg- "beam, plank" (source also of Latin fulcire "to prop up, support," fulcrum "bedpost;" Lithuanian balžiena "cross-bar;" and possibly Greek phalanx "trunk, log, line of battle"). Italian balco "a beam" is from Germanic (see balcony ).
33-
--
112: balcony 
113- bald 
114- balderdash 
115- baldhead 
116- balding 
117- baldness 
118-
119- Advertisement Close 
120- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
121-
122- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
##### 8cc8008461c45a61
6:Barbican - Etymology, Origin & Meaning 
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
--
23: barbican (n.) 
24-
25- "outer fortification of a city or castle," mid-13c., from Old French barbacane "exterior fortification" (12c.), a general Romanic word, said to be ultimately from Arabic or Persian (compare bab-khanah "gate-house"); according to Watkins from Old Iranian compound *pari-varaka- , from *pari- "around" (from PIE root *per- (1) "forward," hence "in front of, around") + *varaka- , from PIE root *wer- (4) "to cover."
26- also from mid-13c. 
27-
28- Entries linking to barbican 
29-
30- *per- (1) 
31-
32- Proto-Indo-European root forming prepositions, etc., meaning "forward," and, by extension, "in front of, before, first, chief, toward, near, against," etc.
33-
--
122: barbican 
123- Barbie 
124- barbiturate 
125- Barcelona 
126- bard 
127- bardic 
128-
129- Advertisement Close 
130- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
131-
132- Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.
```


## [2026-09-06T15:03:15.727Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/213.jpg 2>/dev/null; pdftoppm -f 213 -l 213 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$PWD/../../../tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg213\" 2>/dev/null || pdftoppm -f 213 -l 213 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg213; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 213"
}
```


### [2026-09-06T15:03:18.529Z] TOOL RESULT

```
site/pages/213.jpg
total 996
drwx------ 2 sfmqrb sfmqrb   4096 Sep  6 11:03 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    264 Sep  6 10:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb  66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb  54688 Sep  6 10:58 pg201.png
-rw-rw-r-- 1 sfmqrb sfmqrb  70083 Sep  6 10:52 pg204.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77858 Sep  6 10:52 pg206.png
-rw-rw-r-- 1 sfmqrb sfmqrb  67371 Sep  6 10:53 pg207.png
-rw-rw-r-- 1 sfmqrb sfmqrb  59146 Sep  6 10:53 pg208.png
-rw-rw-r-- 1 sfmqrb sfmqrb  53054 Sep  6 11:00 pg209.png
-rw-rw-r-- 1 sfmqrb sfmqrb  74515 Sep  6 11:02 pg211.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75961 Sep  6 11:02 pg212.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83761 Sep  6 11:03 pg213.png
-rw-rw-r-- 1 sfmqrb sfmqrb  83752 Sep  6 11:01 pg214.png
-rw-rw-r-- 1 sfmqrb sfmqrb 117034 Sep  6 10:54 pg215.png
```


## [2026-09-06T15:03:20.806Z] TOOL CALL #78: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg213.png"
}
```


### [2026-09-06T15:03:21.302Z] TOOL RESULT

```

```


## [2026-09-06T15:03:21.288Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:04:01.683Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KNT kan\"; grep -n \"kan- .*dig\\|akaniya\\|kantanaiy\" KNT.txt | head -10",
 "description": "Kent Old Persian kan-"
}
```


### [2026-09-06T15:04:01.734Z] TOOL RESULT

```
=== KNT kan
1265:For OP x from £ before consonants, see $102 and $108. Corresponding to Skt. khdnati ‘he digs’ we have OP akantya ‘it was dug’, Av. kan- ‘dig’, and Av. xà ‘well’, with unexplained variation between aspirate and non-aspirate.
1401:root, kan- ‘dig’ + pass. -ya-, in akaniya ‘was dug’. *duS- ll’ + *yür- ‘year’, in dušiyãram ‘famine’. wamarsiyus nsm. ‘by self-death’, Skt. mriyú-š
2531:$220. Tue Passive-Votce Present STEM of pIE was formed by the addition of the suffix pIE -je-/-4o-, which is accented in Sanskrit; in OP the root regularly has the normal grade, with -a-: imf. 3d sg. and pl. abariya abariya", to root bar-; ayadiya ayadiya", to yad-; akaniya, to root kan- ‘dig’; afahya and afahiya, to Ваћ-; avaniya, to van-; ajantya, to jan-; akariya akariya"la, to kar-; pres. ist pl. &ahyàmahy, to dah-; opt. 3d sg. kariyaiš to kar-, frabiyats to frað-, 3d pl. yadiyaiša” to yad-.
4253:28 : ша : tya : BU : akaniya : fravata : uta : tya : bika :
4406:10 iy : draya : tya : haeá : Рагва : aitiy : pasdva : iyam : yauviya : akaniya : 11 avafá : yaf : adam : niyastàyam : utd : nāva : àyatà : haca : Mudra 12 уй : tara : imam : yauviyim : abiy : Pársam : араба : yatà : mim : Ката : dha
4983:Adukanaisa- adj. ‘Adukanaisha’ , first month, March-April: Elam. ha-du-kan-na-1§, АКК. nisannu: -natsa- on the evidence of the Elam., acc. to MB Or. $96, rather than -nisa- ($117). Cpd. of adu- ^ + kan- ‘dig’, possibly with vriddhi ($126; Adu- ?): "Irrigation-Canal-Cleaning Month’, re- ferring to the cleaning of the underground con- duits for irrigation water, regularly done in the spring (cf. РЕШ. AiW 61). Adukalnaz]Sahya gsm. DB 2.69.
5236:ikan- vb. ‘dig’: Av. kan-, Skt. khan- ($100), . See also Adukanaiía-, kata-. ka*tanaiy ($238; NPers. kándón) inf. DZe 9; XV 21. akaniya imf, pass. ($113, $220) DSf 24, 28 (25, 29 read avaniya: see under van-); DZe 10°.
5238:vi- + kan- ‘dig apart, destroy’: viyakanam 1st sg. imf. XPh 38. viyaka" imf. ($208, §228.11) DB 1.64. vikanàhy 2d sg. subj. (327) DB 4.71, 78; vikandh"-di& (S27, 454.11, $136) DB 4.77.
```


## [2026-09-06T15:04:02.688Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Quelle, Brunnen\\|'Quelle'\" BRT.txt | head -10",
 "description": "Bartholomae xan- spring"
}
```


### [2026-09-06T15:04:02.746Z] TOOL RESULT

```
2755:i^/^-    n.  'BrennhoU',    an.    asa  'Glutasche';  uiroiustriM    \t.l6.iy,    —    sarait^trä 85jl.  8)  +j-,rn-  f.  'Quelle';  eig.  also  „Glut-,   urva^im  ^nitlDm  «öfV  "vom  Freund  soll
18567:mp.  nambilan  'befeuchten',  np,  nam  'feucht',  ai. vgl.  nabkanu  f.  'Quelle''). —  i>  pl  nach  % Sj 11;  doch  s.  No.  z.  —  ")  Eine  andre  Etymo- logie (lu  ap.  wiira«  'Quelle',  lat  nrfilünui)  bei BcM,  Grdr."  I.  726  nach  Wil>ielm  BB.  12. 104.
```


## [2026-09-06T15:04:13.974Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR<=7783 && /^ *2[01][0-9] *$/ {p=$0;l=NR} END{print \"SKT page marker:\",p,\"line\",l}' SKT.txt; awk 'BEGIN{RS=\"\\f\"} {n+=1} END{}' SKT.txt; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf-8',errors='replace').read().split('\\n')\n# find nearest standalone number before line 7783\nfor i in range(7782,7600,-1):\n    s=t[i].strip()\n    if re.fullmatch(r'\\d{2,3}',s):\n        print('nearest number line',i+1,s); break\nEOF",
 "description": "Check Skeat page for gondola"
}
```


### [2026-09-06T15:04:15.736Z] TOOL RESULT

```
SKT page marker:  line
```


## [2026-09-06T15:04:20.431Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} {c++} END{print \"SKT blocks\",c}' SKT.txt; awk 'BEGIN{RS=\"\\f\"} {lines+=1} ' SKT.txt >/dev/null; python3 - <<'EOF'\np=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt',encoding='utf-8',errors='replace').read()\nblocks=p.split('\\f')\n# which block contains line 7783\nn=0\nfor i,b in enumerate(blocks):\n    n2=n+b.count('\\n')+1\n    if n<7783<=n2:\n        print(\"block\",i+1); print(b[:300]); break\n    n=n2\nEOF",
 "description": "Find Skeat block for gondola"
}
```


### [2026-09-06T15:04:22.161Z] TOOL RESULT

```
SKT blocks 656
block 199
 to    F.  gi^iir.   game.     Cf. I,  a  fc7«r»  giztaid. r.  (E.J    M.  E.  giM,  adj.     Formed S  /iddtam,  to  king,  be  merry;  mj «cfac  of  gii/ify  waa  mirthful. gitiit,  gitU,  a    ioog.   poem,
fomw
LftlHed
reialed
;5
a  kinil  of  eagle  (Da.  and T^  ftnt  syllable  is  from  Du.
```


## [2026-09-06T15:04:33.792Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:1707 2>&1 | head -60",
 "description": "Fetch Borhan page 1707"
}
```


### [2026-09-06T15:04:41.311Z] TOOL RESULT

```
REF: BQT:1707  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 500  OCR-lang: fas

۱ کندوری

ريخته باشد ‎٩‏ .3 کندوده* - بر وزن طنبوره . سفرة

کند۵ - بفتح اول و سکون نانی‌وناك | چرمین راگویند - و پیش انداز را نیز گفته اند
بوا و کشیده » ظرفیرا کوبند مانند خم‌بزرک ی که | وآن پارچه‌ای باش د که در پیش سفره و بر روی
آنرا ا زگل سازند و پراز غله کنند و معرب آن | زانوی مردم بگترانند تا چیزی از خوردنی بر
کندوج باشد ۴ - و جم اول هم باین«عنی وهم | زمین و دامن مردم نریزد ». و این ارسم در ملك
بمعنی غول بیابانی آمده است ۴ . روم جاری است .

کندواله ی اس اول بروزن‌خرد(۱) کندوری ۹ ه بروزن رنجوری» سقره
ساله » مرد بلند بالای قوی هیکل را کوبند - | و دستار خوان چرمی را گوند - و بسنی پیش
و پسر امرد بداندام وزشت را نیز گفته‌اند و اورا | انداز راگفته‌اند یعنی پارچه‌ای که در پیش سفره
کرتله م میگوبند . و روی زالو اندازند بوقت چیزی خوردن.

(۱) خم ۰۱ چش : خورد ساله .

۹ - وگرنه شود بوم ماکندمند از اسفندبار آن پل بد بند .
فردوسی طوسی طبق فهرست ولف و شاهنامةٌ بخ اج ٩ص‏ ۱۷۶۲ ح ۱۷ » اما درمتن همین صفحه
«پر کزه» آهده کندومند » هم بهمین معنی آمده . رك : رشیدی .

۲ * کندوك , معرب آن کندوج رك : منتهی‌الارب : ان دج - بهمین مناسبت
نیلگون کندو بمعنی‌آسمان آمده :

زین فاحشه کنده پیر زاینده بنشنه میان لیلگون کندو .

۶ ناصر خسرو بلخی‌س۳۷۹ »

۴ - ر4 :کنده . نیزبمعنی ظرفی با جمبه‌ا ی که برای | اب
نگپداری زنبورهای عل وعل گرفتن از آنها سازند .

۴ - مخفف «کنداواله» : ی 1
چاکرانت بگه رزم وکه بزم بوند پگ لد

کندواله چوتپمتن » چو فلاطو نکندا . ۸ سم
عبدالٌ قامی « جهانگیری >.

9 << کندوری «رشیدی». رك : کندوری . کی و

‎٩‏ * کندوره (<.م.) «کندوری آن آاز . بو د که در ای
سفره بود »,و گروهی سفره کوبند . پوشکور (بلخی) گوید : اس

‏کشاده دزاهر دو آزاده وار انواع کندوی زنیورعصل
مان کوی کندوری‌افکنده خوار.»
«لغت فری‌صس ۵۱۷. فقس : فراخ کندوری در تاریخ بیهقی مصحح دکتر فیاض ی ۹۹۱ ۰

‏< کندن - بفتح اول و سوم ء از: کن+-دن ( پسوند مصدری ) » پهلوی ۳2۳087 ؛
یراق باستان - ۴8 (کندن, <فر کردن ) « بارتولمه 4۳۷ > « نیب رکك ۱۱۹ پارسی باستان,
اوستا - ۴81 » پپلوی نیز 128188 (شدحش) , هندی باستان - ۳188 ۰ ۳1287811 + کردی
0 اففانی 128481 ۰ استی 81[83818 ( دفن کردن ) » قس : ارمنی 3188 « اسشق
‎٩۹‏ ورك : هوبشمان ۸۹۹ -
```


## [2026-09-06T15:04:57.311Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"88081\\|khanak\\|xanak\\|8081\\|هوبشمان\" BQT_v2_pages.txt | head -20",
 "description": "Find Mo'in footnote for xane in Borhan v2"
}
```


### [2026-09-06T15:04:57.378Z] TOOL RESULT

```
730:           ‫‪ - ۴‬بقول هوبشمان ازساد کرت ‪ ( ۵ 2302111‬فک رکردن ) است ‪ .‬بقول‬
735:  ‫« استق ‪ ( > ۳۱‬وجه اشتقاق هرن رماردود دانته اند ) « هوبشمان ‪ » :۳۱‬اورامالی‬          ‫‪2‬‬
3290:   ‫‪« - ۷‬جوکك‪ .‬فروخ مکایان بود‪.‬‬                       ‫‪.‬‬    ‫آهن) دهوبشمان‪ »: ۳۲‬ورك‪ :‬جع ‪ ۰‬بوغ » جوه‪‎‬‬
3424:   ‫کردی ع از ‪ .‬افغانی ‪ . [2۷0‬بلوچی ‪( [۵‬ب‪1‬رو » آبراهه) *اسشق‪ ۱۳46‬ورك" هوبشمان‪۱۳4‬؛‬
3518:                         ‫ص‪« »۳‬اسشق ‪ « ۷۳:6‬هوبشمان ‪ ۷۳4‬رك‪ :‬چهره » چرخ‪.‬‬
3951:  ‫و رکه‪ :‬چار‪:‬‬       ‫‪ ۰ :‬اسشق وهوبشمان‪۲۳4‬‬             ‫رک‬   ‫‪۲ :‬‬       ‫» «منای ‪۰۷‬‬         ‫( واسطه » راه) ‪ ۶‬تبرگك “‪£‬‬
5079:                                                              ‫(رخ ربندکی) « هوبشمان‪.۷۳4‬‬
5574:       ‫‪ ۲‬ص ‪ <4‬رك ‪ :‬اسشق و هوبشمان ‪ › ۰44‬پپلوی ‪ « 0711152‬تاوادیا ‪ ۲1 : ۰۷۲‬اونوالا ‪۰۷۵‬‬
7595:  ‫‪ -- ۴‬بېلوی ‪« 8806066‬نب رک ‪« 028066 04۰‬هوبشمان‬                                             ‫رك‪ :‬چك‬              ‫‪۱‬‬
7599:  ‫«هوبشمان‪»4 4‬معرب آن صولجان " وکمةٌ فرانوی ‪ 611201016‬ازفارسی‌مأخون امت « اسفا ‪۱:۲‬‬
7858:                                                            ‫‪.‬‬     ‫ورك ‪ :‬چره‬      ‫‪04‬‬   ‫هوبشمان‬   ‫ورك‪ :‬اسشق‪.‬‬                   ‫‪۶۳۰‬‬       ‫ص‬
7883: ‫افغانی ع ‪ « 2‬هوبشمان ‪ »۷۵4‬ورك‪ :‬یبر که ‪ 0‬و اسفا ‪٣ :۱‬ص‏ ‪» ۲۲۱‬گیلکی ‪ 216‬؛ شیشی»‬
8947:‫= ارمتی ‪ « ۲۸2‬هوبشمان ایضاً»؛ حر چیز‬                              ‫‪ ۲‬وخاریشت « هوبدمان ‪٤٩٤‬‏ )‪ ۰‬افقانی ع ‪۲‬‬
10268:  ‫بازند ‪« 102۷‬هوبشمانس ‪4۵‬ج » « مسینا ‪. » ۲ : ۹۳۱‬بعضی ابن کلمه را از‬                                 ‫‪007‬‬
11846:   ‫«هوبشمان ‪ « > ۲۸4‬افا ‪ :‬اس ‪ ۱۲۰‬کردی ‪ « 81161‬اسفا اضاً » ‪ ,‬طبری ‪2071711521‬‬
12257:                                           ‫و ‪ . ۷۸۰‬افنانی شاناک‪« ]2‬هوبشمان ‪»۸۸4‬‬
12894:                ‫‪- ۸‬قی » افتانی ‪ ( 252۳21‬بختك » خفتك) «هوبشمان ‪ ۳۸4۰‬ورك ‪:‬خفرنج‪.‬‬
13311:                 ‫آورده ؛ هوبشمان لپذیرفته است « هوبدمان ‪۲٩4‬‏ »‪ .‬بسنی جزو اول « خل ر‬
14289:                         ‫هوشمان مردود مداند « هوبشمان ‪. ۸‬معرب آن خوان (ضم اول) «نفس»‬
14457: ‫*اسفا‪۱:۲‬ص ‪۸1٩‬‏ «هوبشمان ‪.»۵۰۵‬هندی باستان_ ‪ ۵8۷۹‬کردی]‪ ۰ 058.81111‬استی ‪» 6061, 05‬‬
```


## [2026-09-06T15:05:08.570Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '8935,8950p' HUB.txt; echo \"=== p.88 note area\"; grep -n \"kanden\\|kan- 'graben'\\|xane\\|/^ane\" HUB.txt | head -20",
 "description": "Hübschmann on xane"
}
```


### [2026-09-06T15:05:08.645Z] TOOL RESULT

```
HtnnaSdn = Ahmatan = *Hmafatta {ftarnra bei laid or) — ap.
Haymatana-,= arm. Valars = np. BaM, syr. ^Dli^^D i. J. 430, ZDMG.
43, 409 ^ gr. BoXoysaltpopa Tab. 134, Hoffmann, Ausz. 67.
Kapitel 26: ap. x.
Ap. X {== arisch kh und vor Konsonanten = arisch k)
bleibt im Np. als x,
§ 144. Ap. X = arisch kh = np. ic:
xa (?) H. 459, 460; xar *Dorn H. 461; xan, xana
*Haus' H. 465 ; xam 'Quelle* H. 466 , oben p. 88 Anm. ;
xaytdan *kauen', skr. khad-, xar 'Esel* = zd. xara-, skr.
khara-; xoi, xdd 'Helm' = ap. xauda-, zd. xao^a-, SLvm.xoir;
xum, xunb *irdener Krug' == zd. xutnba-, skr. kumbha- (aus
"^khumbha-?)'^ six *Bratspiess H. 762; sax *Zweig' = skr.
Qakha- ; mex 'Pflock , Nagel' , vgl. skr. mayUkha- ; nOxun
'Nagel*, skr. nakha-, Zu xandaq *Graben' und kandan
graben siehe das oben p. 88, Nr. 869 Bemerkte.
=== p.88 note area
```


## [2026-09-06T15:05:14.852Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Nr\\. 869\\|869\\.\" HUB.txt | head; echo ---; grep -n \"H\\. 869\" HUB.txt | head",
 "description": "Find Hübschmann p.88 note on kandan"
}
```


### [2026-09-06T15:05:14.922Z] TOOL RESULT

```
3123:869. Horn bemerkt mit Recht, dass auf paz. xandan
8950:graben siehe das oben p. 88, Nr. 869 Bemerkte.
---
```


## [2026-09-06T15:05:17.395Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '3118,3140p' HUB.txt",
 "description": "Hübschmann note 869"
}
```


### [2026-09-06T15:05:17.473Z] TOOL RESULT

```
kamra 'Gewolbe, Stalf (N 6 1 d e k e , Pers. Stud. H, p. 40)
ist mir unklar.
868. Np. kund *stumpf = bal. kunt *stumpf, grob, einfaltig*
(Geiger) = skr. (prakr.) kunthar- 'stumpf. Davon
kund Vir strenuus* zu trennen, vgl. kunda^ kundavar,
869. Horn bemerkt mit Recht, dass auf paz. xandan
(= kandan) nichts zu geben ist. Das angefiihrte
phi. xantak (wo vorkommend?) kann nur das falsch
ins Pehlevi umschriebene arab. pers. xandaq = arm.
xandak (bei Steph. Asol. und Spateren!) sein, dessen
regulare np. Form kanda^) ist. Afgh. kanql (im Praes.
')>Kdnnte, obwohl nicht mit I geschrieben, doch (naoh Bartho-
1 m ae) katnal gelesen werden und entsprSche dann einem ap. ^kamarda-
= zd. ^hamareSa-,
') Die Nebenform xati' zu Jean 'graben' stUtzt sich im Iranischen
eigentlich nur auf dieses arabisch-pers. xandaq, da die etym. Erkl&rungen
von xana^ xd,n und xanl (Nr. 465, 466) doch nicht als durchaua sic her
gelten konnen.- 89 -
und Impt.) = kandol („in the past tenses'') kann
doch nur LW. sein (np. praes. kanam, perf, handam).
Die Differenz zwischen iran. han- und skr. khan ist
noch nicht befriedigend erklart.
870. Np. kamzak ist durch das Deminutivsuffix ak von
```


## [2026-09-06T15:05:31.756Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"ghenō\\|g\\\"henō\\|ghen-ō\\|khanati\\|khánati\" IEC.txt | head -10; echo \"--- IEC kan\"; grep -n \"^kanō\\|kanmi\\|kan- (to dig)\\|to dig\" IEC.txt | head -10",
 "description": "Grep Mann IEC"
}
```


### [2026-09-06T15:05:31.819Z] TOOL RESULT

```
--- IEC kan
```


## [2026-09-06T15:05:35.203Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"khan\" IEC.txt | head -20; echo \"--- AHD watkins\"; grep -n -i \"gwhen\\|g\\^when\\|to swell.*fill\\|abundance\" AHD_watkins1985.txt | head -20",
 "description": "Grep IEC and Watkins"
}
```


### [2026-09-06T15:05:35.262Z] TOOL RESULT

```
3175:dhrêh- (1) ‘hold’ (Variants: dr&h- & dhrgh-). Cf. dhrêhtos. WP I, 859 Skt. drhyami; Av. dərəzis ‘strong’; dorozà ‘fetter’; cf. dərəzrö ‘firm, strong’; Per. cf. (o- gde) darz ‘seam’; LW in Arm. dardz (i-st. id.); Gk. tarkhéa ‘funeral rites’; Hes. tárkhē ‘con- fession’; tárkhanon ‘mourning’; tarkhánion ‘burial’; cf. also (?) Boeotian thráganon *tongs'?; Alb. (ambig.) n-drydh, sh-trydh, v. (‘squeeze’, but for both forms cf. trud-, en-, eks-); cf. also Alb. drudh, drydh, id.; Norw. & Icel. dorg ‘trailing-line’; ON dyrgja ‘take (fish)
4581:ghan- (ghand-) ‘contain, be ample, suffice". WP I, 589. Cf. ghend-, ghnd- Skt. ghanáh ‘total, whole”: Per. cf. a-gandan, v. “fill, cram" beside ganjidan, v. ‘contain’; a-gin ‘full, a-ganiS, id. (: Skt. a-han-); Oss. cf. gánàn, in cpds. ‘means’; Gk. cf. khandáno “hold, contain’; W gan, pl.-oedd ('capacity'? fr. *ghandos/-es-); OW gannaf, 1sg. Cam con- tained", inf. genni, Mod. ganu); G ganz ‘quite’; OCS goněti ‘suffice’; Li. ganà ‘enough’; ga- DÉI. eti ‘suffice’; Latv. gan, gana “enough?
4762:ghnd- ‘seize, hold, get, retain, contain". WP I, 589. See ghed-, ghend- Skt. gádhyami "be held fast; Ober, yadiyamiy ‘beg’; Per. cf. gadā ‘beggar’; Gk. khandáno, aor. ékhadon *hold, comprise'; kházo 'con- tain’; Lat. (vowel ambig.) prae-hendo, Gre ‘seize’; Olr. cf. ro-geinn, pf. 'Itook'; OW gan- ni, genni, W ganu ‘be contained’; OCS 7eZdo, žędati ‘thirsť beside inf. Zedéti “desire”;
5935:mouth"; khan-dón 'gapingly': ON gana ‘gape’ beside (*-à- in) mod. Icel. góna “to gawp'. See $hiia-, etc.)
8187:ksənő, ið ‘scratch, scrape, dig’. Cf. ksnt-. WP I, 450 Skt. khánami, pp: khatáb ‘dig’; khaníh, f. *dig- ging; mine’; Oss. åxsinin ‘comb’; Gk. ksaíno, fut. ksanó ‘lacerate; card wool’; ksánion ^wool- comb’; long-gde in ksenós “cutting, canal; cf. Lat. sentus ‘overgrown, tattered; nasty”; OCz. (?) chanéti, inf. ‘flatter’. (A variant oc- curs in Skt. kham, n. (1) ‘hole’; Oss. xwm, xwmä ‘plowed field")
8211:ksong- (skong-) 'ambling gait; ambling, limp'. Cf. skengio Skt. khanjah “limping, lame’; cf. khanj-, cpds. ‘restless’; khanjanabh, m. ‘wagtail’; OE cf. scanca, wm. ‘shank’; ON cf. shakkr ‘wry, askew’ beside skakka ‘abet
9821:(ligh-, variant of lig-, q.v. Slav. forms am- big.) Gk. líkhnos, adj. ‘fond of food’; likhanós, adj. ‘licking’; Gk. likhneáo, v. ‘lick’; Skt. rihá- mi, v. id.; Cz. (ambig.) líznu, -nout, v. id.
10244:māgh- (2) ‘contrivance, invention’ Gk. mëkhos, n. & mëkhar, n.id. beside mē- khané ‘device, art’ (Doric: -à-); Latv. māžs, usu. pl. māži ‘fantasies’; māžs, m. (also: “jugg- ler’)
16191:slagh- (slaghono, slaghnio) ‘hack, cut up, téar, chop' Gk. cf. lakhaíno, v. ‘hoe’; lákhana, npl. 'vege- tables’; OLat. cf. lanius, m. ‘butcher’; lanio, laniare, v. *téar up, hack’; cf. also la-pis, gs: -pidis (stone', if for *slagh-peds 'stub-foot"); lammina, lamina (‘metal plate’, if for *slagh- mn-) (but for Lat. laedo, see slad-); Ir. slaigim, v. ‘hew, strike" beside slaige, f. ‘chopping’; OHG slag, s. beside MHG slahan, p.t. sluoc, pp: slagen; despite Go. slahan, OE slëan, v. ('strike', etc. Cons. anomalous); cf. also OHG slahton, v. “slaughter”; OE slæhtan, id.; OHG slahta, f. “slaughter”
16632:sogh- (alternative form of type sogh-, sce segh- and segh-). Cf. songh- Skt. cf. sahyam, n. ‘help’; Av. cf. hazao$o, adj. ‘agreed’, Myc. oko-, m. “holder? beside Gk. ókhma, n. & okhmé, f. id.; ókhanon, okháne ‘handle’; MHG sagge, sacke, wm. (common lang’, lit. holding")
17001:sphàk- (?) Br. foeka, inf. ‘thrust, deal a backhander”; taol-fæk, m. ‘thrust, blow’; Li. spankü, spàkti, v. ‘kick back, Jib”
--- AHD watkins
805:op-'. To work, produce in abundance. 1. Suffixed form *op-es- in Latin opus (stem oper-), work, with its denomi- native verb operari, to work, and secondary noun opera, work: OPERA!, OPERATE, OPEROSE, OPUS; COOPERATE, INURE, MANEUVER, MANURE, OFFICINAL. 2. Latin offi- cium, service, duty, business (< *opi-fici-om, “perform- ance of work”; -fici-, doing; see dhé-1). 3. Suffixed form *op-en-ent- dissimilated in Latin opulentus, rich, wealthy: OPULENT. 4. Suffixed form “*op-ni- in Latin omnis, all (< “abundant’”): OMNI-, OMNIBUS; OMNIUM- GATHERUM. 5, Suffixed (superlative) form *op-tamo- in Latin optimus, best (< ‘‘wealthiest’’): OPTIMUM. 6. Prefixed Latin form *co-op- (co-, collective and inten- sive prefix; see kom) in Latin cdpia, profusion, plenty: COPIOUS, COPY; CORNUCOPIA. [Pok. 1. op- 780.]
832:pel-5. To sell. Lengthened o-grade form *pdl- in Greek p6lein, to sell: BIBLIOPOLE, MONOPOLY. [Pok. 5. pel- 804.] pel-6. To thrust, strike, drive. I. Suffixed form *pel-de-. 1. Germanic “*felt-, *falt-, to beat, in: a. Old English anfilt(e), anfealt, anvil (“something beaten on”): ANVIL; b. Germanic “*feltaz, *filtiz, compressed wool, in (i) Old English felt, felt: FELT! (ii) Medieval Latin filtrum, filter, piece of felt: FILTER. 2. Latin pellere (past participle pulsus), to push, drive, strike: POUSETTE, PULSATE, PULSE!, PUSH; COMPEL, DISPEL, EXPEL, IMPEL, PROPEL, REPEL. 3. Suffixed o-grade form *pol-o-, fuller of cloth, in Latin polire, to make smooth, polish (< “to full cloth”): POLISH. II. Extended form *peb-. 1. Present stem *pelna- in: a. Latin appelldre, “to drive to,” address, entreat, appeal, call (ad-, to; see ad-): APPEAL; b. Latin compellare, to accost, address (com-, intensive prefix; see kom): COMPELLATION; Cc. Latin interpellare, “to thrust between,” interrupt (inter-, between; see en): INTERPEL- LATE. 2. Suffixed zero-grade extended adverbial form *pla-ti, in pre-Greek *pldti in Greek plésios, near (< “pushed toward”): PLESIOSAURUS. [Pok. 2. a. pel- 801.] pel-7. Dish. Suffixed lengthened-grade form *pél-owi- in Latin pélvis, basin: PELVIS. [Pok. 4. pel- 804.] pele-1. 1. To fill; with derivatives referring to abundance and multitude. Variant “*p/é-, contracted from “pleo-. I. Suffixed zero-grade form “pls-no-. 1.Germanic *ful- naz, *fullaz, full, in Old English full, full: FULL’. 2. De- rivative Germanic verb *fulljan, to fill, in Old English fylian, to fill: FILL. 3. Latin root *pldno-, replaced by *pléno- (influenced by Latin verb plére, to fill; see III. 1. below) in Latin plénus, full: PLENARY, PLENITUDE, PLENTY, PLENUM; PLENIPOTENTIARY, REPLENISH, TERREPLEIN. II. Suffixed form *p(e)la-u-. 1. Possibly Latin paliis, marsh (? < “inundated”; but possibly rather from pel-?): PALUDAL, PALUDISM. 2. Obscure compara- tive form (Old Latin p/ous) in Latin plis, more: PIU, PLURAL, PLUS; NONPLUS, PLUPERFECT, SURPLUS. 3. O-grade form *pol()-u- in Greek polus, much, many: POLY-; HOI POLLOI. III. Variant form “p/é-. 1. Latin plére, to fill: (ACCOMPLISH), COMPLETE, COMPLIMENT, COMPLY, EXPLETIVE, IMPLEMENT, REPLETE, SUPPLY. 2. Possibly suffixed form *plé-dhw- in Latin p/lébs, plébés, the people, multitude: PLEBE, PLEBEIAN, PLEBS; PLEBISCITE. 3. Suffixed form *plé-dhwo- in: a. Greek pléthos (Ionic pléthus), great number: ISOPLETH; b. Greek derivative verb pléthein, to be full: PLETHORA; PLETHYSMOGRAPH. 4. Suffixed (comparative) form *plé-i(sjon- in Greek pledn, pleién, more: PLEO-, PLEO- NASM; PLEIOTAXY, PLEIOTROPISM, PLIOCENE. 5. Suffixed (superlative) form *p/é-isto- in Greek pleistos, most: PLEISTOCENE. IV. Possibly Sanskrit piirah, cake (< “that which fills or satisfies”): POORI. [Pok. 1. pel- 798.] pela-2, Flat; to spread. Variant *pld-, contracted from *plaa-. 1. Suffixed form *pel{a)-tu- in Germanic “felthuz, flat land, in Old English feld, open field: FIELD. 2. Suf- fixed form *pel{a)-t-es- (by-form of *pel)-tu-) in Ger- manic *feltha-, flat land, in: a. Old High German feild, field: FELDSPAR; b. Middle Dutch veld, velt, field: VELDT. 3. Variant form “pld- in: a. suffixed form
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1506:FENCE gWhen-! FENNEL dhé@(i)- FENUGREEK dhé(i)- -FER bher-1 FERAL ghwer- FER-DE-LANCE ferrum FERE per-2
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1962:OFFEND g¥hen-! OFFENSE gWhen-1 OFFER bher-1 OFFICE dhé-1 OFFICINAL dhé-1, op-1 OFT upo
```


## [2026-09-06T15:05:44.708Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gWhen-2\\.\" AHD_watkins1985.txt | head -3; grep -n \"BARBICAN\\|GONDOLA\" AHD_watkins1985.txt | head -3; echo \"---\"; awk '/gWhen-2\\. To swell|gWhen-2\\./{print NR\": \"substr($0,1,700)}' AHD_watkins1985.txt | head -5",
 "description": "Watkins gwhen-2 entry"
}
```


### [2026-09-06T15:05:46.477Z] TOOL RESULT

```
---
```


## [2026-09-06T15:05:49.013Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"gWhen\" AHD_watkins1985.txt | head -10",
 "description": "Grep Watkins gwhen"
}
```


### [2026-09-06T15:05:49.057Z] TOOL RESULT

```
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1506:FENCE gWhen-! FENNEL dhé@(i)- FENUGREEK dhé(i)- -FER bher-1 FERAL ghwer- FER-DE-LANCE ferrum FERE per-2
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1962:OFFEND g¥hen-! OFFENSE gWhen-1 OFFER bher-1 OFFICE dhé-1 OFFICINAL dhé-1, op-1 OFT upo
```


## [2026-09-06T15:05:54.737Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"EUTHENICS\\|euthenein\\|euthenes\" AHD_watkins1985.txt | head; echo ---; grep -n \"^g.hen\\|g.hen-2\\|g.hen-1\" AHD_watkins1985.txt | head",
 "description": "Find Watkins gwhen root entries"
}
```


### [2026-09-06T15:05:54.834Z] TOOL RESULT

```
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
---
545:sive reduplicated form *gr-g- in Latin gurges, throat, also gulf, whirlpool: GARGET, GORGE, GORGET, GURGITA- TION; INGURGITATE, REGURGITATE. 4. Extended form *gwr6- (< *geroa-) in Greek br6- in: a. suffixed redupli- cated form bi-bré-sko- in Greek bibréskein, to eat: HELLEBORE; b. nasalized variant form *bro-n-kh- in Greek bronkhos, windpipe, throat: BRONCHO-, BRON- CHUS; C. suffixed form *gvré-mn in Greek bréma, food: THEOBROMINE; d. suffixed form *gvr6-ti- in Greek bro- sis, eating: ABROSIA. [Pok. 1. gver- 474.] gwes-. To extinguish. Suffixed variant form *sgves-nu- in Greek sbennunai, to extinguish: ASBESTOS. [Pok. g¥es- 479.] g”et-'. Resin (?). Only in Germanic and Celtic. Suffixed form *gvet-u- in: a. Germanic *kwithu- in Old English cwudu, cwidu, cudu, resin, mastic gum, “that which is chewed,” cud: CUD, QUID!; b. Celtic *betu-, birch, birch resin, in Latin bitumen, resin (Gaulish loanword): BITU- MEN. [Pok. 1. g¥et- 480.] gwet-2. To say, speak. Germanic *kwithan in Old English cwethan, becwethan, to say, speak: BEQUEATH, BEQUEST, QUOTH. [Pok. 2. g¥et- 480.] gvet-3. Intestine. Suffixed o-grade form *gvot-olo- in Latin botulus, intestine, sausage: BOTULINUM, BOTULISM, BOWEL; (BOTULIN). [Pok. gvet- 481.] ghedh-. To ask, pray. 1. Germanic *bidjan, to entreat, in Old English biddan, to ask, pray: BID. 2. Germanic *bidam, entreaty in Old English gebed (ge-, intensive and collective prefix; see kom), prayer: BEAD. [Pok. gehedh- 488, 2. bhedh- 114.] gvhen-'. To strike, kill. 1. O-grade *gvhon- in Germanic suffixed form *ban-6n- in: a. Old English bana, slayer, cause of ruin or destruction: BANE; b. Middle High German ban, bane (> German Bahn), way, road (? < “path hewn through woods”): AUTOBAHN. 2. Suffixed zero-grade form *ghn-tyd- in Germanic *gundjé, war, battle, in: a. Old Norse gunnr, war: GUN; b. compound *gund-fanon-, “battle flag” (fandn-, flag; see pan-), in Italian gonfalone, standard: GONFALON. 3. Suffixed form *gvhen-do- in: a. Latin défendere, to ward off (dé-, away; see de-): DEFEND, (DEFENSE), (FENCE); b. Latin offen- dere, to strike against, be offensive, offend (ob-, against; see epi): OFFEND, (OFFENSE). 4. Suffixed zero-grade form *gvhn-tro- in Persian zahr, poison: BEZOAR. [Pok. 2. gthen-(2)- 491, bhen- 126.] g”hen-2. To swell, abound. Suffixed form *gvhen-eyo- in Greek euthenein (eu-, well; see esu-), to flourish: EU- THENICS. [Pok. 1. gthen- 491.] g’her-. To heat, warm. 1. Zero-grade *gvhr- with nasal suffix and analogical vocalism in Germanic *brenw-, to burn, forming *brennan (intransitive) and brannjan (transitive) in: a. Old English beornan, byrnan (intransi- tive) and bérnan (transitive), to burn: BURN}; b. late Old English brynstan, “burning mineral,” sulfur (stan, stone; see stei): BRIMSTONE. 2. Germanic *brandaz, a burning,
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1479:EUTECTIC ta- EUTHANASIA dhwene- EUTHENICS gWhen-2 EUTROPHIC threph- EUXENITE xenos EVACUATE eu-2 EVADE wadh-2 EVAGINATE wag- EVANESCE eu-2 EVANGEL angelos EVAPORATE kwép- EVECTION wegh- EVENT gWa- EVENTIDE da- EVER aiw-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1572:GUN gWhen-1 GURGITATION gWere-4 GURU gWera-2 GUSH gheu- Gust! gheu- GusT2 geus- GUSTO geus-
1962:OFFEND g¥hen-! OFFENSE gWhen-1 OFFER bher-1 OFFICE dhé-1 OFFICINAL dhé-1, op-1 OFT upo
```


## [2026-09-06T15:06:48.917Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; grep -n \"strotzen\\|schwellen, strotzen\\|aganis\\|agandan\" WLD_Bd1_1930_dli_70244_djvu.txt | head -10",
 "description": "Walde-Pokorny gwhen- swell entry"
}
```


### [2026-09-06T15:06:48.971Z] TOOL RESULT

```
13219:„in Jugendkraft strotzend" (L. Meyer Hdb.I614, Debrunner GGA. 1910. 
18184:s. auch u. au'dij- . strotzen") : slav. *cersl'~, rorsk- (aus * uerk-sij -, iiork-tq-) 
18313:uer(e)g- „strotzen, schwellen yor Saft und Kraft oder Zorn”. 
18316:kraftigt", urjusvant- „strotzend“ : 
18319:manden u. dgl.), dgydco „von Feuehtigkeit und Saft strotzen, vom Erd- 
18461:KG. I 105 zu ir. ferg usw., s. u.; unrjy- „strotzen“; fiber air. doairci „be- 
35467:„Fett, Schmalz, Uppigkeit, strotzende Fiille". 
42807:1. gKlien- „schwellen, strotzen, Fiille". 
42809:Ai. O-hands „schwellend, strotzend, xippig, geil", ghand- „kompakt, dicht, 
42840:triichtig, voll, strotzend" (Ehrlich KZ. 39, 561, BPhW. 1911, 1573, Brug-
```


## [2026-09-06T15:06:52.269Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD; sed -n '42807,42830p' WLD_Bd1_1930_dli_70244_djvu.txt; echo \"=== page\"; awk 'NR<=42807 && /^ *[0-9]{3} *$/ {p=$0;l=NR} END{print p,l}' WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "Read WLD gwhen- entry"
}
```


### [2026-09-06T15:06:54.796Z] TOOL RESULT

```
1. gKlien- „schwellen, strotzen, Fiille". 

Ai. O-hands „schwellend, strotzend, xippig, geil", ghand- „kompakt, dicht, 
dick", m. „kompakte Masse" (nicht als „fest zusammengesehlagen" = ghand- 
„erschlagend, m. Keule", Uhlenbeck Ai. Wb. 84; s. *cfihen- „schlagen“) ; 

npers. u-gandan „anfiillen“, Ciganis „voll“; gr. evftevyg ■ evrcaftovou, loyvgd 
Hes., ev&eveco „gedeihe, bin in Bliite und Kraft", evdeveta ,, Fiille. blxihen- 
der Zustand", dehnstnfig jon. svdgvgg „reichlich, in Fxille", jon. att. ev'&y- 
veco „gedeihe, bin in Bliite und Kraft", evdgvia „Fiille“ {-!h:v- kaum nach 
Sommer Gr. Ltst. 66 aus -dyv- nacli o&evog), o-stufig KQe\*T\a-cp6vTyg eig. 
„kraftschwellend", HoXvcp6vzr\g = IIoXvYzijzrjg, KXeocfdvzrjg, vielleicht zpovog 
aipazog II. 16, 162 wenn „Hasse“ (doch eher nach Niedermann IA. 29, 33 
fur al/ua <povov „das Blut des getbteten Hirsches"), red.-stufig rpavav &e- 
Xelv Hes., wohl eigentlich ,,geil sein". Lit. guild „genug“, aksl. goncti „ge- 
niigen" (gegen Entlehnung aus got. ganah s. Solmsen Beitr. I 167 Anm. 2. 
Berneker 327). 

Arm. yogn „multum" (Praep. i + *o-g’ihon- oder *o-cfihno im Praelix 
o- dem ar. a- nachststehend, Liden Arm. St. 76 f.) . 

Bezzenberger-Fick BB. 6. 337, Fick BB. 8, 330; 16. 289, Horn Kp. Et. 
10, Grdr. d. iran. Phil. I 2, 62, 130, Johansson IF. 3, 241, Ehrlich KZ. 39, 561. 

=== page
679  42794
```


## [2026-09-06T15:07:03.321Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg213.png data/verification/sources/refs/ocr/BOOK/213.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-06T15:07:05.210Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T15:16:26.429Z] TOOL CALL #96: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build213.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot = {\n \"entry\": 0,\n \"root\": \"Gwhen 1\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *gʷhen- 'to swell, teem, abound' (Pokorny IEW 491, '1. gʷhen- „schwellen, strotzen, Fülle“'; Watkins/AHD gʷhen-2 'to swell, abound')\",\n \"note\": \"The root box itself is exactly right: Pokorny IEW p.491 opens '1. gʷhen- „schwellen, strotzen, Fülle“; gʷhono-s „üppig, reichlich“', with ai. ā-ghaná-, npers. ā-gandan 'anfüllen', āganiš 'voll', gr. euthenḗs / euthenéō, lit. ganà 'genug', aksl. gonĕti; Walde-Pokorny I 679 has the identical entry, and Watkins prints 'gʷhen-2. To swell, abound … [Pok. 1. gʷhen- 491]'. Nourai's numbering follows Pokorny (Watkins numbers the same root 2, reserving gʷhen-1 for 'to strike, kill'), so 'Gwhen 1' with the gloss 'to swell, fill' is correct, and POK:491 is the right page. THE PROBLEM ON THIS PAGE IS NOT THE ROOT BOX BUT WHAT HANGS UNDER IT. Everything in PART 2 descends from the Old Iranian verb kan- 'to dig', and no handbook attaches that verb to *gʷhen-: Walde-Pokorny put it under a separate root 'qhen-¹ „graben“' (WP I 399); Pokorny himself, in the footnote on IEW p.634, writes 'Zur gleichen Wurzel ken- (oben 559 ff.) könnte ai. khánati „gräbt“ … gehören … av. apers. kan- „graben“', and dismisses WP's khen- as 'nicht als idg. zu erweisen'; Cheung (EDIV 232 f.) reconstructs *kanH¹ 'to dig' from '?*kenH₂- = LIV: 344 | Pok.: 534'. The genuine Iranian continuant of *gʷhen- is āgandan 'to fill' (Cheung's separate *kan² 'to fill', Parthian ʾgn-, MMP hngn-), which Nourai evidently treated in PART 1 on p.182. So PART 2's whole tree is hung on the wrong root: the individual Iranian and Persian links inside it are mostly sound, but their common ancestor is *kenH- 'to dig', not *gʷhen- 'to swell'. Nourai's own bridging gloss for node 1, 'to dig dirt out and mound it up', is the semantic device by which he joins 'dig' to 'swell'; no source supports it.\",\n \"note_fa\": \"جعبهٔ ریشه درست است: پوکورنی در صفحهٔ ۴۹۱ فرهنگ خود مدخل «1. gʷhen-» را با معنای «آماسیدن، لبریز بودن، فراوانی» آورده و شواهد آن را «آگندن» و «آگنیش» فارسی، euthenḗs یونانی و ganà لیتوانیایی می‌داند؛ والده‌ـ پوکورنی (جلد ۱ ص ۶۷۹) و واتکینز (پیوست AHD، با شمارهٔ gʷhen-2) نیز همین را می‌گویند. پس نام ریشه، برچسب «هندواروپایی» و معنای «آماسیدن، پر کردن» و ارجاع POK:491 هر سه درست است. اما اشکال اساسی این صفحه در محتوای آن است: تمام شاخه‌های «بخش ۲» از فعل ایرانی باستان kan- «کندن، حفر کردن» می‌آید و هیچ فرهنگ معتبری این فعل را به *gʷhen- نمی‌بندد؛ والده‌ـ پوکورنی آن را ذیل ریشهٔ جداگانهٔ «qhen- graben» (جلد ۱ ص ۳۹۹) آورده، خود پوکورنی در پانوشت صفحهٔ ۶۳۴ آن را به ریشهٔ ken- (ص ۵۵۹ به بعد) پیوند می‌زند، و چونگ در فرهنگ ریشه‌شناختی فعل ایرانی آن را *kanH¹ از هندواروپایی *kenH₂- می‌داند. بازماندهٔ راستین *gʷhen- در ایرانی «آگندن» است نه «کندن». بنابراین درخت این صفحه بر ریشهٔ نادرست سوار شده است، هرچند پیوندهای درونی آن (ایرانی باستان ← پهلوی ← فارسی) در بیشتر موارد درست‌اند.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/g%CA%B7hen-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:491\", \"status\": \"supports\",\n    \"note\": \"POK_02.txt lines 2245-2266 (the leaf whose running number is 491): '1. gʷhen- „schwellen, strotzen, Fülle“; gʷhono-s „üppig, reichlich“. Ai. ā-ghaná- „schwellend, strotzend, üppig“, ghaná- „dicht, dick“ …; npers. ā-gandan „anfüllen“, āganiš „voll“; arm. yogn „multum“; gr. εὐθενής „reichlich, in Fülle“ …; lit. ganà „genug“ …; aksl. goneti „genügen“. WP. I 679'. The page and gloss are exactly as Nourai cites — but the entry contains no Iranian kan- 'to dig'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.679 (WLD_Bd1_1930_dli_70244_djvu.txt line 42807)\", \"stance\": \"supports\",\n    \"note\": \"'1. gʷhen- „schwellen, strotzen, Fülle“. Ai. ā-ghaná- … npers. a-gandan „anfüllen“, āganiš „voll“; gr. euthenḗs … Lit. ganà „genug“, aksl. gonĕti „genügen“.' Identical content to Pokorny 491; again no kan- 'dig'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I p.399 (same file, line 25134)\", \"stance\": \"contradicts\",\n    \"note\": \"The dig-root is a SEPARATE Walde-Pokorny entry: 'qhen-¹ „graben“. Ai. khánati „gräbt“, Inf. khani-tum, Ptc. khātá- … khā- „Quelle, Brunnen“ = av. xā …; mit Verlust der Aspiration … av. ap. kan „graben“ …, kani- „Graben“ … Arm. akan „διώρυγμα“.' So the material of PART 2 belongs here, not to gʷhen-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, g-list (AHD_watkins1985.txt line 545)\", \"stance\": \"supports\",\n    \"note\": \"'gʷhen-2. To swell, abound. Suffixed form *gʷhen-eyo- in Greek euthenein …: EUTHENICS. [Pok. 1. gʷhen- 491.]' — same root, same gloss, same Pokorny page; Watkins simply numbers it 2 (his gʷhen-1 is 'to strike, kill', BANE/DEFEND/GUN). No Iranian 'dig' words under it.\"},\n   {\"src\": \"POK\", \"where\": \"IEW p.634, footnote 1 (POK_02.txt line 4661)\", \"stance\": \"contradicts\",\n    \"note\": \"Pokorny's own footnote: 'Die bei WP. I 341, 348 f., 399 angeführten Wurzeln … khen- „graben“ sind nicht als idg. zu erweisen … Zur gleichen Wurzel ken- (oben 559 ff.) könnte ai. khánati „gräbt“, Inf. kháni-tum, Partiz. khātá- gehören, samt … khā- „Brunnen“ = av. Nom. Akk. Pl. xā́ ds.; ai. khani- „wühlend“ = av. kani- „Graben“; av. apers. kan- „graben“ (k- aus kh- aus den Kompositis mit us-, ham-).' Pokorny thus places the whole PART 2 material 143 pages away from gʷhen-.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann col. s.v. ghan- (IEC.txt line 4581)\", \"stance\": \"partial\",\n    \"note\": \"Mann: 'ghan- (ghand-) „contain, be ample, suffice“. WP I, 589 … Per. cf. a-gandan, v. „fill, cram“ beside ganjidan, v. „contain“; a-gin „full“, a-ganiš … Gk. cf. khandánō „hold, contain“ … OCS goněti „suffice“; Li. ganà „enough“.' Mann keeps the āgandan/ganà material but files it under a plain-velar ghan- with Gk. khandánō, i.e. a compatible but not identical reconstruction; he too has no kan- 'dig' here.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp.232-233, s.v. *kan², *kanH¹ (CHEUNG.txt lines 15521, 15552)\", \"stance\": \"contradicts\",\n    \"note\": \"Cheung separates '*kan² „to fill“ … *NWIR: (+ *ā-) NP āgandan/āgin- „to fill, stuff“ … Several Iranian languages point to the existence of a separate root *kan- „to fill“' from '*kanH¹ „to dig“ … *PIE ? *kenH₂- „to dig“ = LIV: 344 | Pok.: 534'. Only the first is a gʷhen- word; PART 2 draws on the second.\"}\n ],\n \"nodes\": []\n}\n\nN = root[\"nodes\"]\n\nN.append({\n \"id\": 1,\n \"lang\": \"Avestan / Old Persian\",\n \"words\": \"kan 1, xan, gan 1; čât\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The forms are real but the parent link is not. Young Avestan kan- 'to dig' is attested in the Vidēvdād (us-kan- 'dig out' V 3.12, auua-kan- V 15.39, aipi.kan- V 14.6, ni-kanta- V 7.43) and Old Persian ka(n)- appears in Darius' Susa inscription (akaniya 'was dug' DSf 24/28, inf. ka(n)tanaiy DZc 9); Kent, Old Persian p.178b: '¹kan- vb. „dig“: Av. kan-, Skt. khan-; ka(n)tanaiy inf.; akaniya imf. pass.' The aspirated by-form xan- is the one behind Av. xā (nom. pl. xā́) 'spring' and Skt. khánati; Kent p.51 notes the 'unexplained variation between aspirate and non-aspirate'. Avestan čāt- f. 'well-pit' is Bartholomae AiW col. 583 ('j. čāt- f. „Brunnengrube“: maiδe vā čāitē vā V.13.71 … Zum V. ¹kan-, vgl. xan-; vgl. mp. (Pū.), np. čāh'). What is wrong is (a) the ancestry: this verb is *kanH- < PIE *kenH₂- (Cheung, LIV 344; Walde-Pokorny's qhen- 'graben', WP I 399; Pokorny IEW 634 fn.), not *gʷhen- 'to swell'; (b) 'gan 1': no Avestan or Old Persian verb gan- 'to dig' exists. The g-form belongs to the separate stem *gan-/āgan- 'to fill' (Cheung *kan², Parthian ʾgn-, NP āgandan) — which really is the gʷhen- reflex, and which Nourai has silently merged with the dig-verb here; (c) the gloss 'to dig dirt out and mound it up' is Nourai's own bridge to 'swell': no dictionary gives the verb a 'heap up' sense.\",\n \"derivation_fa\": \"صورت‌ها درست‌اند اما نسبت‌دادن آن‌ها به این ریشه نادرست است. kan- اوستایی «کندن» در وندیداد (uskanti در ۳٫۱۲، auuakanta در ۱۵٫۳۹، nikanta- در ۷٫۴۳) و ka(n)- پارسی باستان در سنگ‌نبشتهٔ شوش داریوش (akaniya «کنده شد»، مصدر ka(n)tanaiy) گواهی شده است؛ کنت در فرهنگ پارسی باستان (ص ۱۷۸) همین را می‌آورد و می‌افزاید که «تفاوت میان صورت دمیده و نادمیده هنوز توضیح داده نشده است». گونهٔ دمیدهٔ xan- پشتوانهٔ xā اوستایی «چشمه» و khánati سنسکریت است، و čāt- اوستایی «چاهِ کنده» را بارتولمه (ستون ۵۸۳) صریحاً از همین فعل می‌داند و به mp./np. «چاه» می‌رساند. اما سه ایراد هست: نخست آنکه این فعل در ریشه‌شناسی امروزی *kanH- از هندواروپایی *kenH₂- است نه *gʷhen-؛ دوم آنکه فعلی به صورت gan- «کندن» در اوستایی یا پارسی باستان وجود ندارد و صورت g- در واقع از ستاک جداگانهٔ *gan-/āgan- «پر کردن» (همان که «آگندن» از آن است) می‌آید و نورایی این دو را با هم آمیخته است؛ سوم آنکه معنای «خاک را کندن و روی هم انباشتن» ساختهٔ خود نورایی برای پل‌زدن به معنای «آماسیدن» است و در هیچ فرهنگی نیامده.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BRT:583\", \"status\": \"supports\",\n    \"note\": \"Bartholomae AiW col. 583-584 (BRT.txt line 11250 ff.): 'j. čāt- f. „Brunnengrube“: maiδe vā čāitē vā V.13.71. Ableit. — Zum V. ¹kan-, vgl. xan-; §13. — Vgl. mp. (Pū.), np. čāh (aus iran. *čāϑ-)'; the same column carries 'g. čāxnarə-, s. ¹kan-' and 'j. čātaya- „in einer Brunnengrube befindlich“ … Pū.: āp i čāhān'. So BRT:583 is the right column for čāt- and it does derive it from kan- — but from kan-, not from gʷhen-.\"},\n   {\"ref\": \"POK:491\", \"status\": \"contradicts\",\n    \"note\": \"Pokorny 491 (POK_02.txt line 2245 ff.) lists only ai. ā-ghaná-, npers. ā-gandan, arm. yogn, gr. euthenḗs, lit. ganà, aksl. gonĕti — no Avestan or Old Persian kan-/xan-/čāt-. Pokorny's treatment of kan- is on p.634 fn., under ken-.\"},\n   {\"ref\": \"HRN:194\", \"status\": \"supports\",\n    \"note\": \"Horn, Grundriss no.869 (p.194, HRN.txt leaf 216): 'kenden „graben“, Praes. ken-em, ap. aw. √kan- „graben“; phlv. kantan (Bund.), kandan (AV., PPGl.), paz. xandan; ai. √khan-, khánati … Auf die mit kh anlautende Form der Wurzel gehen np. (arab.) xendeq „Graben“, phlv. xantak, np. xāne, xan „Haus“ (No. 405[=465]) und xān „Quelle“ (No. 466) zurück'. Horn is the direct source of Nourai's whole chart — including kan/xan and the čāh, xānī, xāne, xandaq branches.\"},\n   {\"ref\": \"ZMA:49\", \"status\": \"not_checked\",\n    \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian (Bonyad-e Neyshabur 1374) — refs_online.json marks it 'purchase only; no open copy'; not consultable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian p.178b and §100/p.51 (KNT.txt lines 5236, 1265)\", \"stance\": \"supports\",\n    \"note\": \"'¹kan- vb. „dig“: Av. kan-, Skt. khan- (§100). See also Adukanaiša-, kata-. ka(n)tanaiy (§238; NPers. kandan) inf. DZc 9; XV 21. akaniya imf. pass. DSf 24, 28'; and 'Corresponding to Skt. khánati „he digs“ we have OP akaniya „it was dug“, Av. kan- „dig“, and Av. xā „well“, with unexplained variation between aspirate and non-aspirate.' Exactly Nourai's 'kan / xan' pair — but no gan-.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp.232-233 s.v. *kanH¹ (CHEUNG.txt line 15552 ff.)\", \"stance\": \"contradicts\",\n    \"note\": \"'*kanH¹ „to dig“. *AVESTAN: YAv. °kan- … *OLD PERSIAN: ka(n)- „to dig“ = Kent: 178b … *MIDDLE PERSIAN: BMP kn- /kan-/ „to dig (out); engrave“ … *NWIR: NP kandan/kan- … *PIE ? *kenH₂- „to dig“ = LIV: 344 | Pok.: 534.' Cheung's *kan² „to fill“ (NP āgandan) is a different root — the one that really continues gʷhen-.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 1.37 'SPRING; WELL', p.46 (SYN.txt block 72 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'Av. xan- (nom. pl. xā́) „spring“ : Skt. khan- „dig“, kha- „hole, opening“, khā- … „spring, source“. Walde-P. 1.399. Barth. 531.' and 'Av. čāt- „well“, NPers. čāh „well“ : Av. kan- „dig“, parallel form to Skt. khan-. Barth. 583.' Buck confirms both of Nourai's node-1 items and gives the modern root reference — Walde-P. 1.399, not 1.679.\"}\n ]\n})\n\nN.append({\n \"id\": 2,\n \"lang\": \"Pahlavi\",\n \"words\": \"kantan, xandan; kandak; xânîg; čâh\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Middle Persian kandan / kan- 'to dig; to raze' [Book Pahlavi HPLWN-tn' with the Aramaic heterogram ḥpr 'dig', phonetic kndn'/kntn'] is MacKenzie's headword (CPD p.49) and Nyberg's (Manual II p.114): 'kandan [ḤPLWN-tn', kndn'] kan- 1. to dig, pt. kand „engraved“ … MPrs and NP „to dig“, Paz. xandan, xan-, with an initial x- confirmed by the Arab. lw. xandag „trench“ and Skr khan- (pt. khāta-)'. So Nourai's doublet 'kantan, xandan' is exactly Nyberg's/Horn's kantan ~ Pazand xandan; the -t- of kantan is the Book-Pahlavi spelling kntn', voiced to -d- already in late MP. xānīg 'spring' and čāh 'well' are both in MacKenzie (CPD pp.93-94: '²xān [ẖʾnʾ | P xʾn] spring, source', 'xānīg [ẖʾnyh | M xʾnyg, N xānī] = ²xān'; and bun-xān 'source'), the latter from OIr. *čāta- < the same verb. The weak item is kandak: Middle Persian kandag is not 'a dug-in house' but 'ditch, trench, moat' — it is the past participle kand- + -ag ('the dug thing') and is precisely the form Arabic borrowed as ḵandaq (Asbaghi 113); the 'dug-in house' sense belongs to the New Persian kandak of node 3. Hence plausible, not confirmed.\",\n \"derivation_fa\": \"فعل فارسی میانهٔ kandan / kan- «کندن، ویران کردن» (به خط پهلوی با هزوارش آرامی ḤPLWN و املای آوایی kndn'/kntn') در فرهنگ مکنزی (ص ۴۹) و در واژه‌نامهٔ نیبرگ (بخش دوم ص ۱۱۴) آمده است؛ نیبرگ می‌افزاید: «در پازند xandan، xan- با x آغازین که وام‌واژهٔ عربی xandag „خندق“ و khan- هندی باستان آن را تأیید می‌کند». پس جفت «kantan, xandan» نورایی همان صورت کتابی و صورت پازند است و -t- در kantan املای پهلوی کتابی است که در فارسی نو به -d- نرم شده. xānīg «چشمه» و čāh «چاه» نیز هر دو در مکنزی هست (²xān «چشمه»، xānīg = ²xān، و bun-xān «سرچشمه»). تنها ایراد در kandak است: kandag فارسی میانه معنای «خانهٔ کنده‌شده» ندارد بلکه «خندق، گودال» است — همان صورتی که عربی آن را «خندق» گرفته — و معنای «جای کنده‌شده در خانه» به کندکِ فارسی نو (گرهٔ ۳) مربوط می‌شود. از این رو حکم «با احتیاط پذیرفتنی».\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:1707\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p.1707 (BQT_v3 pdf p.500, fetched with tools/ref_page.py BQT:1707; OCR cached under sources/refs/ocr/BQT/), Mo'in's etymological footnote on کندن: «کندن - بفتح اول و سوم، از: کن + ـدن (پسوند مصدری)، پهلوی kantan؛ ایران باستان kan- (کندن، حفر کردن) «بارتولمه ۴۳۷»، «نیبرگ ۱۱۹»، پارسی باستان، اوستا kan-، پهلوی نیز kandan، هندی باستان khan-, khanati، کردی …، افغانی kandal، اُسّتی nigänin (دفن کردن)، قس: ارمنی akan … رک: هوبشمان ۸۹۹». Mo'in prints exactly Nourai's Pahlavi 'kantan'.\"},\n   {\"ref\": \"HRN:194\", \"status\": \"supports\",\n    \"note\": \"Horn no.869 (p.194): 'phlv. kantan (Bund.), kandan (AV., PPGl.), paz. xandan' — Nourai's two Pahlavi forms verbatim, plus 'phlv. xantak' for the Arabic loan.\"},\n   {\"ref\": \"SNS:8,155\", \"status\": \"partial\",\n    \"note\": \"Tavoosi's Shāyast nē Shāyast glossary does carry the entry (SNS.txt line 2066: ':kan:' with the reference '(Kent 178)' and the Pahlavi heterogram), and the index (line 28972) gives 'kan 8/13'; the Persian OCR of pages 8 and 155 (SNS_pages.txt) is too degraded to read the running text, so the two page numbers could not be checked line by line.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p.49 s.v. kandan and pp.93-94 s.v. xān, xānag, xānīg (PHD_mackenzie.txt lines 3190, 5531-5538)\", \"stance\": \"supports\",\n    \"note\": \"'kandan, kan- [ḤPLWN-tn' < A √ḥpr; kn-dn', -tn' | M knd, N -] dig; raze, destroy'; '¹xān [ẖʾnʾ | P xʾn, N -] house'; '²xān [ẖʾnʾ | P xʾn] spring, source'; 'xānag [BYTA < A byt'; ẖʾnh | N xāna] = ¹xān'; 'xānīg [ẖʾnyh | M xʾnyg, N xānī] = ²xān'; also 'bun-xān [bwnẖʾn] source'. Every Pahlavi form of the node except kandak is here.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. kandan (NYB_vol2_glossary.txt line 2196)\", \"stance\": \"supports\",\n    \"note\": \"'kandan [ḤPLWN-tn', kndn'] kan- 1. to dig, pt. kand engraved … Two different vbs.: 1. Av. OP (437 sq.) ²kan- „to dig“, whence also gukān-; 2. kan- „to throw“, whence also apakandan, frakandan, pargandan … MPrs and NP „to dig“, Paz. xandan, xan- with an initial x- confirmed by the Arab. lw. xandag „trench“ and Skr khan- (pt. khāta-).' Nyberg also warns that the homonymous kan- 'to throw' must be kept apart.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien no.869, pp.88-89 (HUB.txt line 3123)\", \"stance\": \"partial\",\n    \"note\": \"'Horn bemerkt mit Recht, dass auf paz. xandan (= kandan) nichts zu geben ist. Das angeführte phl. xantak (wo vorkommend?) kann nur das falsch ins Pehlevi umschriebene arab. pers. xandaq … sein, dessen reguläre np. Form kanda ist.' Footnote: 'Die Nebenform xan- zu kan- „graben“ stützt sich im Iranischen eigentlich nur auf dieses arabisch-pers. xandaq, da die etym. Erklärungen von xāna, xān und xānī (Nr. 465, 466) doch nicht als durchaus sicher gelten können.' i.e. the very scholar Nourai leans on elsewhere doubts the x-forms.\"}\n ]\n})\n\nN.append({\n \"id\": 3,\n \"lang\": \"Persian\",\n \"words\": \"kandan «کندن ( کان )»; kandak «کَنَدَک»; kandŭk «کندوک»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian کندن kandan / present stem کن kan- continues Middle Persian kantan/kandan without complication (Wiktionary: 'From Middle Persian kntn' (kantan, „to dig“), from Proto-Iranian *kánHati „to dig“'); the parenthetical «کان» in the box is Persian kān 'mine', the deverbal noun Horn treats as no.839 on the very page Nourai cites. کندوک kandūk / کندو kandū 'grain-jar, beehive' and its by-forms are all in Borhan-e Qate' at the page cited for node 2: «کندو … ظرفی را گویند مانند خم بزرگی که آن را از گِل سازند و پر از غله کنند و معرّب آن کندوج باشد»; the printed page also carries کندوله، کندوری، کندوره and Nāser Khosrow's «نیلگون کندو» for the sky — i.e. every extra Persian word in Nourai's box (کندوله، کندوج، کندو، کندره، کندور) sits on Borhan p.1707. The formation is the past stem کند kand- + the diminutive/instrumental suffix -ū(k) < MP -ūg, so kandūk is literally 'the dug-out (vessel)'. کَنَدَک kandak 'a place dug out in a house' is the same stem with -ak. The Ferdowsi hemistich quoted in the box («ده و دو هزار انگبین کندره») is the classical attestation of کندره in the beehive sense.\",\n \"derivation_fa\": \"«کندن» فارسی نو با ستاک حال «کن-» بی هیچ پیچیدگی دنبالهٔ kantan/kandan فارسی میانه است (ویکی‌واژه: از فارسی میانهٔ kantan، از ایرانی آغازین *kánHati)؛ «کان» داخل پرانتز همان اسم مشتق از این فعل است که هرن آن را در شمارهٔ ۸۳۹ (ص ۱۸۶ — همان صفحه‌ای که نورایی ارجاع داده) آورده و می‌نویسد «کان: به ap. √kan- „کندن“، رک: کندن شمارهٔ ۸۶۹». «کندوک/کندو» و همهٔ گونه‌های آن در برهان قاطع ص ۱۷۰۷ آمده است: «کندو … ظرفی را گویند مانند خم بزرگی که آن را از گِل سازند و پر از غله کنند و معرّب آن کندوج باشد»، و در همان صفحه کندوله، کندوری و کندوره نیز هست؛ یعنی تمام واژه‌های افزودهٔ نورایی (کندوله، کندوج، کندو، کندره، کندور) از یک صفحهٔ برهان برداشته شده. ساخت واژه: ستاک گذشتهٔ «کند» + پسوند -و(ک) از -ūg فارسی میانه، پس «کندوک» یعنی «ظرفِ کنده‌شده». ادعای نورایی در این گره درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%A9%D9%86%D8%AF%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:186\", \"status\": \"supports\",\n    \"note\": \"Horn no.839 (p.186, HRN.txt leaf 208): 'kān „Mine“. Zu ap. √kan- „graben“, vergl. kenden (No. 869)' — precisely the «کان» Nourai puts in parentheses beside kandan.\"},\n   {\"ref\": \"BQT\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' p.1707 (BQT_v3 pdf p.500 via tools/ref_page.py): «کندو - بفتح اول و سکون ثانی و ثالث بواو کشیده، ظرفی را گویند مانند خم بزرگی که آن را از گِل سازند و پُر از غله کنند و معرّب آن کندوج باشد»; footnote «کندوک، معرب آن کندوج، رک: منتهی‌الارب»; and «رک: کنده. نیز بمعنی ظرفی با جمبه‌ای که برای نگهداری زنبورهای عسل و عسل گرفتن از آنها سازند» — the beehive sense Nourai glosses.\"},\n   {\"ref\": \"FVF:593\", \"status\": \"not_checked\",\n    \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi — refs_online.json lists it as 'website' only (noorlib/ketabnak, login-walled); no page image obtainable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Borhan p.1707 (Mo'in's footnote on کندن)\", \"stance\": \"supports\",\n    \"note\": \"«کندن … از: کن + ـدن (پسوند مصدری)، پهلوی kantan؛ ایران باستان kan- (کندن، حفر کردن)» — the New Persian verb is derived from the Old Iranian dig-root, exactly the chain of nodes 1→2→3.\"},\n   {\"src\": \"ARY\", \"where\": \"Aryanpur, Persian index of IE roots, pdf p.411 (ARY_latin_index_pages.txt lines 11969-11975)\", \"stance\": \"supports\",\n    \"note\": \"The entry heads 'KHAN., KHANATI, KAN- (AVESTAN) / KAN- (OLD PERSIAN) / KANDAN, KANTAN (PAHLAVI) / KENAN, CHIKANDIN (KURDISH) / KANDAL (AFGHAN)' with 'MACKENZIE: (DIG) 110'; Aryanpur files آگندن separately (pdf p.66: 'AKANDAN, AKANDE, AKANESH … GONEJETE, GANA-, GONETI, ĀGANDAN' — the Pokorny 491 material), i.e. an independent modern Persian source that also keeps کندن and آگندن apart.\"},\n   {\"src\": \"MON\", \"where\": \"Mo'in / Dehkhoda s.v. کندو, کندوج (via abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"The lexica agree with Borhan on کندو 'large earthen grain-jar; beehive' and کندوج 'granary'; no competing etymology is offered for any of them.\"}\n ]\n})\n\nN.append({\n \"id\": 4,\n \"lang\": \"Greek\",\n \"words\": \"konda, kondu\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Ancient Greek κόνδυ (kóndu), n., 'drinking vessel', is real — it is the word Greek writers use for the Persian cup (Xenophon, Ctesias, and it is the vessel of the Septuagint's Joseph story) — but 'konda' is not a Greek word; Nourai has read it out of Skeat, where gonda is the ITALIAN form ('Ital. gondola, dimin. of gonda, a boat'), not a Greek one. As for the etymology, modern scholarship does not take κόνδυ from Persian kandūk: Wiktionary (with Furnée and Szemerényi) writes 'Like many words ending in -ῠ, it is a loanword. Furnée compares κοτύλη „cup“, suggesting a Pre-Greek origin, while Szemerényi refers to late Neo-Babylonian kandu „vessel“ which is … a West Semitic borrowing from Aramaic כנדא kandā „vessel, pot“ from Sanskrit कन्दु kandu „pot“ and ultimately Proto-South Dravidian *kiṇṭV-', in the same family as כד kad, Greek κάδος. So κόνδυ is an oriental Wanderwort whose nearest Indo-Iranian relative is Sanskrit kandu 'pot', not Persian kandūk 'grain silo'; the resemblance to کندو is real but the route runs through Mesopotamia and India, and there is no evidence of an Old Persian intermediary. Nourai's own NOTE ('Derivation from Persian is debated') concedes the point, and modern scholarship comes down against him.\",\n \"derivation_fa\": \"κόνδυ یونانی باستان به معنای «جام، ظرف نوشیدنی» واژه‌ای واقعی است — همان جامی که گزنفون و کتسیاس دربارهٔ ایرانیان به کار می‌برند — اما «konda» در یونانی وجود ندارد؛ نورایی این صورت را از اسکیت برداشته، جایی که gonda صورت ایتالیایی است نه یونانی. دربارهٔ ریشه نیز پژوهش امروزی آن را از «کندو»ی فارسی نمی‌گیرد: ویکی‌واژه (به پیروی از فورنه و سه‌مه‌رنی) می‌نویسد که این واژه مانند بسیاری از واژه‌های پایان‌یافته به -ῠ وام‌واژه است؛ فورنه آن را پیشایونانی می‌داند و سه‌مه‌رنی آن را به kandu بابلی نو می‌رساند که خود از kandā آرامی و آن از kandu سنسکریت «دیگ» و سرانجام از *kiṇṭV- دراویدی جنوبی آغازین است. پس κόνδυ واژه‌ای سرگردان (Wanderwort) از خاور نزدیک است و نزدیک‌ترین خویشاوند هندوایرانی‌اش kandu سنسکریت است نه «کندو»ی فارسی. یادداشت خود نورایی («این اشتقاق محل بحث است») درست است و پژوهش امروزی جانب مخالف را می‌گیرد.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%CE%BA%CF%8C%CE%BD%CE%B4%CF%85\"],\n \"ref_check\": [\n   {\"ref\": \"SKT:217\", \"status\": \"partial\",\n    \"note\": \"Skeat, Concise Etym. Dict. p.217 (SKT.txt block 199): 'Gondola. (Ital.-Gk.) Ital. gondola, dimin. of gonda, a boat. — Gk. κόνδυ, a drinking vessel; from the shape.' Skeat does derive the Italian word from Greek κόνδυ — but he says nothing whatever about Persian, and 'gonda' in his entry is Italian, not Greek. So the reference supports only half of Nourai's arrow, and none of the Persian half.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict. s.v. gondola (KLN_1966.txt line 16419)\", \"stance\": \"contradicts\",\n    \"note\": \"'gondola, n., a narrow boat used in the canals of Venice. — It., fr. Friaul. gondola, „to waver, vacillate“, which is prob. of imitative origin. It is not connected with L. gandeia, „a kind of African ship“.' Klein knows Skeat's Greek etymology and silently discards it.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls / Webster, s.v. gondola (WEB_vol1.txt line 83034)\", \"stance\": \"contradicts\",\n    \"note\": \"Webster's New Twentieth Century: 'gon-do-la, n. [It., ultimately from Romance base dond-, to rock.]' — again a Romance, not a Greek or Persian, origin.\"}\n ]\n})\n\nN.append({\n \"id\": 5,\n \"lang\": \"Italian\",\n \"words\": \"gonda, gondola\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Venetian gondola (earlier gondula) is first recorded in a Venetian document of 1094 and becomes the general Italian word in the 15th-16th c.; gonda is the shorter by-form Barnhart cites. The Italian word is certainly the source of English gondola, but its own origin is unsettled and the Greek κόνδυ etymology Skeat and Nourai use is not held today: Etymonline, 'from Italian (Venetian) gondola, earlier in English as goundel, from Old Italian gondula, of unknown origin; according to Barnhart, perhaps a diminutive of gonda, a name of a kind of boat'; Klein derives it from Friulian gondolà 'to waver, vacillate' (imitative); Webster from a Romance base dond- 'to rock'; a further common proposal is Medieval Greek κοντούρα 'small vessel' (to κοντός 'short'), which is a different Greek word from κόνδυ. The chart's parenthesis '(due to its shape)' reproduces Skeat's 'from the shape', i.e. the boat likened to a cup — a semantic bridge no modern dictionary accepts.\",\n \"derivation_fa\": \"«گوندولا»ی ونیزی (صورت کهن‌تر gondula) نخستین بار در سندی ونیزی از سال ۱۰۹۴ میلادی دیده می‌شود و از سدهٔ پانزدهم به بعد واژهٔ عمومی ایتالیایی است؛ gonda گونهٔ کوتاه‌شده‌ای است که بارنهارت یاد کرده. این واژه بی‌گمان خاستگاه gondola انگلیسی است، اما ریشهٔ خودش روشن نیست و اشتقاق آن از κόνδυ یونانی — که اسکیت و به پیروی او نورایی آورده‌اند — امروز پذیرفته نیست: اتیمآنلاین آن را «از ایتالیایی کهن gondula با خاستگاه ناشناخته» می‌داند و به گفتهٔ بارنهارت شاید مصغّر gonda باشد؛ کلاین آن را از gondolà فریولی «تاب خوردن» می‌گیرد و وبستر از ستاک رومی dond- «جنبیدن». پیشنهاد رایج دیگر κοντούρα یونانی میانه «کشتی کوچک» است که واژه‌ای جدا از κόνδυ است. عبارت «(به سبب شکلش)» در نمودار برگردان «from the shape» اسکیت است، یعنی همانندی قایق به جام — پلی معنایی که هیچ فرهنگ امروزی نمی‌پذیرد.\",\n \"sources\": [\"https://www.etymonline.com/word/gondola\"],\n \"ref_check\": [\n   {\"ref\": \"SKT:217\", \"status\": \"supports\",\n    \"note\": \"Skeat p.217: 'Gondola. (Ital.-Gk.) Ital. gondola, dimin. of gonda, a boat. — Gk. κόνδυ, a drinking vessel; from the shape.' This is verbatim the source of Nourai's Italian box, including both words and the parenthetical motivation.\"},\n   {\"ref\": \"PRT:260\", \"status\": \"not_checked\",\n    \"note\": \"Partridge, Origins (1958) — refs_online.json marks all archive.org copies 'lending only'; not readable.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 16419 s.v. gondola\", \"stance\": \"contradicts\",\n    \"note\": \"'It., fr. Friaul. gondola, „to waver, vacillate“, which is prob. of imitative origin.'\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, s.v. gondola (WEB_vol1.txt line 83034)\", \"stance\": \"contradicts\",\n    \"note\": \"'[It., ultimately from Romance base dond-, to rock.]'\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat's list of 'Italian from Greek' words, p.~? (SKT.txt line 23501)\", \"stance\": \"supports\",\n    \"note\": \"Skeat repeats the classification in his appendix: 'Italian from Greek: archipelago, baldacchino[?], bombast, catacomb, gondola …' — showing the Greek derivation is his settled view, but it is his alone.\"}\n ]\n})\n\nN.append({\n \"id\": 6,\n \"lang\": \"English\",\n \"words\": \"gondola\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English gondola is a straightforward 16th-century borrowing of the Venetian word: Etymonline, 'gondola (n.) 1540s, „long, narrow flat-bottomed boat used in Venice“, from Italian (Venetian) gondola, earlier in English as goundel, from Old Italian gondula'. The later senses (railway gondola car 1871, airship car 1896, ski-lift 1957) are English developments. The Italian→English step is beyond doubt; only the ultimate Greek/Persian ancestry drawn above it is not.\",\n \"derivation_fa\": \"gondola انگلیسی وام‌واژه‌ای است از ایتالیایی (گویش ونیزی) که در دههٔ ۱۵۴۰ به انگلیسی رسیده — صورت کهن‌تر انگلیسی goundel — و معناهای تازه‌ترش (واگن باری ۱۸۷۱، اتاقک کشتی هوایی ۱۸۹۶، کابین تله‌کابین ۱۹۵۷) در خود انگلیسی پدید آمده‌اند. این حلقه (ایتالیایی ← انگلیسی) بی‌چون‌وچرا درست است؛ آنچه محل تردید است حلقه‌های بالاتر (یونانی و فارسی) است.\",\n \"sources\": [\"https://www.etymonline.com/word/gondola\"],\n \"ref_check\": [\n   {\"ref\": \"SKT:217\", \"status\": \"supports\",\n    \"note\": \"Skeat p.217 heads the entry 'Gondola. (Ital.-Gk.)', i.e. English from Italian; the English lemma is the headword itself.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"KLN_1966.txt line 16419\", \"stance\": \"supports\",\n    \"note\": \"'gondola, n., a narrow boat used in the canals of Venice. — It.' — English from Italian, with the derivatives gondoletta, gondolier (F., fr. It. gondoliere).\"},\n   {\"src\": \"WEB\", \"where\": \"WEB_vol1.txt line 83034-83037\", \"stance\": \"supports\",\n    \"note\": \"'gon-do-la, n. [It. …] 1. a long, narrow canalboat … 3. a gondola car. 4. a cabin suspended under a dirigible'; 'gon-do-lier, n. [It. gondoliere, from gondola]'.\"}\n ]\n})\n\nN.append({\n \"id\": 7,\n \"lang\": \"Persian\",\n \"words\": \"kanand «کَنَند»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"کَنَند kanand is a genuine classical Persian noun for a digging tool, formed on the present stem کن kan- of کندن. Dehkhoda: «بیلی را نیز گفته‌اند که سر آن خمیده باشد و برزیگران کار فرمایند … کلند. کلنگ. آلتی با سری آهنین و دستهٔ چوبین … که بدان زمین کنند»; Loghat-e Fors (Asadi, ed. Eqbal p.90) already defines it as «بیلی باشد سر اندر چفته، برزگران دارند و به ماوراءالنهر بیشتر بود», and Mo'in gives «(کَ نَ) (اِ.) افزاری که چاه‌کنان و گل‌کاران با آن زمین را می‌کنند» — Nourai's vocalisation and gloss exactly. The verse quoted in the box, «برگیر کَنَند و تبر و تیشه و ناوه / تا ناوه کشی، خار زنی گرد بیابان», is the Khojasteh line preserved in Loghat-e Fors and reprinted in Dehkhoda and Mo'in under the same headword, poet's name included.\",\n \"derivation_fa\": \"«کَنَند» اسم ابزاری راستین در فارسی کلاسیک است که از ستاک حال «کن-» ساخته شده. دهخدا: «بیلی را نیز گفته‌اند که سر آن خمیده باشد و برزیگران کار فرمایند … کلند، کلنگ، آلتی با سری آهنین و دستهٔ چوبین که بدان زمین کنند»؛ لغت فرس اسدی (چاپ اقبال ص ۹۰) پیش‌تر آورده «بیلی باشد سراندرچفته، برزگران دارند و به ماوراءالنهر بیشتر بود»؛ و معین می‌نویسد «(کَ نَ) (اِ.) افزاری که چاه‌کنان و گل‌کاران با آن زمین را می‌کنند» — همان آوانگاری و همان معنایی که نورایی داده است. بیت داخل جعبه («برگیر کَنَند و تبر و تیشه و ناوه / تا ناوه کشی، خار زنی گرد بیابان») نیز همان بیت خجسته است که در لغت فرس آمده و دهخدا و معین ذیل همین سرواژه با نام همین شاعر نقل کرده‌اند. ادعای نورایی در این گره کاملاً درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%DA%A9%D9%86%D9%86%D8%AF/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:3102\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. کنند (read via abadis.ir, section فرهنگ معین; archived as data/verification/sources/web/5505f84618f4aefe.txt): «(کَ نَ ) (اِ.) افزاری که چاه‌کنان و گل‌کاران با آن زمین را می‌کنند». The page number is consistent with Mo'in's continuous pagination (the ک section falls around pp.3050-3200), though the local OCR of MON carries no page markers to confirm 3102 itself.\"}\n ],\n \"consulted\": [\n   {\"src\": \"ARY\", \"where\": \"Dehkhoda, Loghatnāme s.v. کنند (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"«العزق؛ شکافتن زمین به کنند (تاج المصادر بیهقی)» plus three classical verses — Rudaki, Abu'l-Abbas and Khojasteh — the last being Nourai's quotation word for word: «برگیر کنند و تبر و تیشه و ناوه / تا ناوه کشی خار زنی گرد بیابان. خجسته (از لغت فرس)».\"},\n   {\"src\": \"FRS\", \"where\": \"Asadi Tusi, Loghat-e Fors, ed. Eqbal p.90 (quoted in Dehkhoda s.v.)\", \"stance\": \"supports\",\n    \"note\": \"«بیلی باشد سراندرچفته، برزگران دارند و به ماوراءالنهر بیشتر بود» — the oldest attestation of the word, an 11th-century Persian glossary, which also preserves the Khojasteh verse.\"}\n ]\n})\n\nN.append({\n \"id\": 8,\n \"lang\": \"Persian\",\n \"words\": \"xânî «خانی»; čâh «چاه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both words continue the Pahlavi forms of node 2 regularly. چاه čāh < MP čāh < Old Iranian *čāta- (Av. čāt- 'well-pit', with intervocalic -t- > MP -h as in *brātā > brādar-type lenition of the dental); Wiktionary gives the sister forms 'Sogdian c'ṯ /čāt/, Avestan 𐬗𐬁𐬝 (cāt̰), Khotanese cāta, Khwarezmian ct', Baluchi چات (cát)'. خانی xānī < MP xānīg 'spring' (MacKenzie CPD p.94), with the regular loss of final -g after -ī in New Persian. Buck's Dictionary of Selected Synonyms, in the very section §1.37 'SPRING; WELL' on the page Nourai cites, states both derivations from the dig-verb: 'Av. xan- (nom. pl. xā́) „spring“ : Skt. khan- „dig“ … Barth. 531' and 'Av. čāt- „well“, NPers. čāh „well“ : Av. kan- „dig“, parallel form to Skt. khan-. Barth. 583'. Dehkhoda's entry for خانی («حوض و چشمه آب را گویند — برهان قاطع») matches Nourai's gloss and his BQT reference precisely, and quotes Neẓāmi, Owḥadi, Khāqāni and Qaṭrān for it. The one caveat is the one Hübschmann raised in 1895 (see node 2): the x- of xān/xānī is itself not fully explained.\",\n \"derivation_fa\": \"هر دو واژه دنبالهٔ منظم صورت‌های پهلوی گرهٔ ۲ است. «چاه» از čāh فارسی میانه و آن از ایرانی باستان *čāta- (اوستایی čāt- «گودالِ چاه») با تحول -t- میان‌واکه‌ای به -h در فارسی میانه؛ ویکی‌واژه هم‌ریشه‌های آن را برمی‌شمارد: سغدی čāt، اوستایی cāt̰، ختنی cāta، خوارزمی ct'، بلوچی چات. «خانی» از xānīg فارسی میانه «چشمه» (مکنزی ص ۹۴) با افتادن -g پایانی پس از -ī در فارسی نو. باک در همان بخش ۱٫۳۷ «چشمه؛ چاه» که نورایی ارجاع داده، هر دو را از فعل «کندن» می‌گیرد: «xan- اوستایی (جمع xā́) „چشمه“ : khan- سنسکریت „کندن“ … بارتولمه ۵۳۱» و «čāt- اوستایی „چاه“، čāh فارسی نو : kan- اوستایی „کندن“ … بارتولمه ۵۸۳». دهخدا نیز ذیل «خانی» می‌نویسد «حوض و چشمهٔ آب را گویند (برهان قاطع)» و بیت‌هایی از نظامی، اوحدی، خاقانی و قطران می‌آورد. تنها تردید همان است که هوبشمان در ۱۸۹۵ مطرح کرد: توجیه x آغازین هنوز کامل نیست.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%87\", \"https://abadis.ir/fatofa/%D8%AE%D8%A7%D9%86%DB%8C/\"],\n \"ref_check\": [\n   {\"ref\": \"SYN:46\", \"status\": \"supports\",\n    \"note\": \"Buck §1.37 'SPRING; WELL' (begins p.44; the Indo-Iranian paragraphs, §§7-8, fall on p.46 — SYN.txt blocks 71-76): 'Av. xan- (nom. pl. xā́) „spring“ : Skt. khan- „dig“, kha- „hole, opening“, khā- or khan- „spring, source“. Walde-P. 1.399. Barth. 531.' and 'Av. čāt- „well“, NPers. čāh „well“ : Av. kan- „dig“, parallel form to Skt. khan-. Barth. 583.' The reference supports Nourai's node precisely — while pointing to Walde-Pokorny I 399, not to gʷhen-.\"},\n   {\"ref\": \"BQT\", \"status\": \"supports\",\n    \"note\": \"Borhan-e Qate' s.v. خانی, quoted verbatim in Dehkhoda: «خانی. (اِ) حوض و چشمهٔ آب را گویند. (برهان قاطع) (آنندراج) (ناظم‌الاطباء)» — Nourai's gloss 'spring, water pond' is a literal rendering of Borhan's.\"},\n   {\"ref\": \"MON:1395\", \"status\": \"supports\",\n    \"note\": \"Mo'in's lexicon has خانی in the same sense; the page number is consistent with his continuous pagination (خ falls around pp.1350-1470), though the local MON OCR has no page markers to confirm 1395 exactly.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn nos.465-466, p.104 (HRN.txt line 4251 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'466. xānī „Quelle, Wasserbassin“, xān … aw. xā(n)-, Nom. xā́ „Quelle“; phlv. xān, xānīk (Bund.); ai. khān- (khā-). kurd. kānī, kahnī.' Horn's Kurdish kānī 'spring' with plain k- is the strongest independent evidence that xānī really belongs to the kan- family.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.94 (PHD_mackenzie.txt lines 5534-5538)\", \"stance\": \"supports\",\n    \"note\": \"'²xān [ẖʾnʾ | P xʾn] spring, source'; 'xānīg [ẖʾnyh | M xʾnyg, N xānī] = ²xān' — MacKenzie himself equates the Pahlavi word with New Persian xānī.\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col. 583 (BRT.txt line 11250 ff.)\", \"stance\": \"supports\",\n    \"note\": \"'j. čāt- f. „Brunnengrube“ … Zum V. ¹kan-, vgl. xan- … Vgl. mp. (Pū.), np. čāh' — the Avestan→Middle Persian→New Persian chain for چاه spelled out by Bartholomae.\"}\n ]\n})\n\nN.append({\n \"id\": 9,\n \"lang\": \"Persian\",\n \"words\": \"xâneh «خانه»; ğâneh «غانه»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The form and history of خانه itself are not in doubt (NP xāna < MP xānag [BYTʾ, ẖʾnh], MacKenzie CPD p.94), and the whole 19th-century tradition Nourai follows does derive it from the dig-verb: Horn no.465, 'xān, xāne „Haus“, xānegī; phlv. xānak, xān, xānakīk … Von √khan- „graben“. Vergl. np. (arab.) xendeq neben kenden'; Hübschmann §144 files 'xān, xāna „Haus“ H.465' among the reflexes of Aryan kh-; Klein s.v. barbican repeats it ('khāna „house“ … derives fr. stem khan-, „to dig“'). BUT modern Iranian etymology rejects this. Wiktionary's etymology tree for خانه runs PIE *h₂wes- 'to dwell' > PII *Hwas- > PIr *Hwah- > PIr *wāhana 'habitation' > OP *vahanam > MP xānag > NP خانه, comparing کده kada 'house' — i.e. the word is a *wāhana- 'dwelling' with the regular Middle Persian development of initial *w- before -ā-, and has nothing to do with digging. Hübschmann himself already warned (Pers. Stud. no.869 n.): 'Die Nebenform xan- zu kan- „graben“ stützt sich im Iranischen eigentlich nur auf dieses arabisch-pers. xandaq, da die etym. Erklärungen von xāna, xān und xānī (Nr. 465, 466) doch nicht als durchaus sicher gelten können.' The chart's second word is worse: «غانه» ğāneh 'house' is not a Persian word in that sense at all — Dehkhoda's only entries for غانه are proper names (a town on the Euphrates, 'and the correct form is عانه', and the West African Ghana). The printed page (pdf p.213, copied to data/verification/sources/refs/ocr/BOOK/213.png) really does read «غانه: house» with «ـ غان ، دامغان» beneath it, so the extraction is faithful; the ğ- form is Nourai's own back-formation from place-names in -ğān such as دامغان, whose second element is in any case not securely خانه.\",\n \"derivation_fa\": \"دربارهٔ صورت و تاریخ خودِ «خانه» تردیدی نیست: فارسی نو xāna از xānag فارسی میانه (مکنزی ص ۹۴). سنّت سدهٔ نوزدهم که نورایی از آن پیروی می‌کند آن را از فعل «کندن» می‌گیرد: هرن در شمارهٔ ۴۶۵ می‌نویسد «xān, xāne „خانه“؛ پهلوی xānak, xān … از √khan- „کندن“؛ قس خندق در برابر کندن»؛ هوبشمان نیز در بند ۱۴۴ آن را در شمار بازتاب‌های kh هندوایرانی می‌آورد و کلاین ذیل barbican همین را تکرار می‌کند. اما ریشه‌شناسی امروزی این را نمی‌پذیرد: ویکی‌واژه درخت اشتقاق «خانه» را چنین می‌کشد: هندواروپایی آغازین *h₂wes- «سکونت گزیدن» ← هندوایرانی *Hwas- ← ایرانی آغازین *Hwah- ← *wāhana «مسکن» ← پارسی باستان *vahanam ← فارسی میانه xānag ← «خانه»، و آن را با «کده» می‌سنجد؛ یعنی واژه از ریشهٔ «باشیدن/سکونت» است نه از «کندن». خود هوبشمان هم در پانوشت شمارهٔ ۸۶۹ هشدار داده بود که گونهٔ xan- در ایرانی تنها بر «خندق» عربی‌ـ فارسی تکیه دارد و توضیح‌های ریشه‌شناختی «خانه، خان و خانی» را نمی‌توان کاملاً مطمئن دانست. واژهٔ دوم جعبه بدتر است: «غانه» به معنای «خانه» اصلاً واژهٔ فارسی نیست؛ دهخدا زیر «غانه» تنها دو نام خاص دارد (شهری بر کنارهٔ فرات که «صحیح عانه است» و غانهٔ آفریقا). تصویر صفحهٔ چاپی (که در data/verification/sources/refs/ocr/BOOK/213.png نگهداری شده) نشان می‌دهد کتاب واقعاً «غانه: house» را چاپ کرده است، پس خطای استخراج نیست بلکه ساختهٔ خود مؤلف است، احتمالاً از روی نام‌جای‌هایی مانند «دامغان».\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D8%A7%D9%86%D9%87\", \"https://abadis.ir/fatofa/%D8%BA%D8%A7%D9%86%D9%87/\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:194\", \"status\": \"supports\",\n    \"note\": \"Horn no.869 (p.194): 'Auf die mit kh anlautende Form der Wurzel gehen np. (arab.) xendeq „Graben“, phlv. xantak, np. xāne, xan „Haus“ (No. 465) und xān „Quelle“ (No. 466) zurück' — Horn's page is exactly what Nourai's arrow claims, so the citation is accurate even though the claim itself is now contested.\"},\n   {\"ref\": \"BQT\", \"status\": \"not_found\",\n    \"note\": \"The Borhan-e Qate' volume covering خ (BQT_v2_pages.txt) could not be searched successfully for Mo'in's footnote on خانه: the OCR of that volume is interleaved with bidirectional control characters and the headword did not resolve; no page number is given in the chart to fetch as an image.\"},\n   {\"ref\": \"ZMA:51\", \"status\": \"not_checked\",\n    \"note\": \"Jonaydi, Zendegi va Mohajerat-e Aryaian — purchase-only, no accessible copy (refs_online.json).\"},\n   {\"ref\": \"MON\", \"status\": \"partial\",\n    \"note\": \"Mo'in's lexicon has خانه with the expected senses but the reference is given without a page and his entry offers no etymology that would decide between kan- and *wāhana-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien §144 and no.869 n. (HUB.txt lines 8943, 3123)\", \"stance\": \"partial\",\n    \"note\": \"§144 lists 'xān, xāna „Haus“ H. 465; xān „Quelle“ H. 466' under 'Ap. x = arisch kh'; but the footnote to no.869 says the x-forms rest 'eigentlich nur auf dieses arabisch-pers. xandaq, da die etym. Erklärungen von xāna, xān und xānī (Nr. 465, 466) doch nicht als durchaus sicher gelten können', and closes 'Die Differenz zwischen iran. kan- und skr. khan- ist noch nicht befriedigend erklärt.'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.93-94 (PHD_mackenzie.txt lines 5531-5535)\", \"stance\": \"silent\",\n    \"note\": \"'¹xān [ẖʾnʾ | P xʾn, N -] house'; 'xānag [BYTA < A byt'; ẖʾnh | N xāna] = ¹xān'. MacKenzie records the form and its Aramaic heterogram BYTʾ but gives no etymology, so he neither supports nor contradicts the kan- derivation.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. barbican (KLN_1966.txt line 4441)\", \"stance\": \"supports\",\n    \"note\": \"'… ult. fr. Pers. bāla-khāna, „upper chamber, balcony on the top of a house“, lit. „a high house“ … The second element derives fr. stem khan-, „to dig“.' Klein transmits Horn's etymology into the English tradition — the source of Nourai's confidence.\"}\n ]\n})\n\nN.append({\n \"id\": 10,\n \"lang\": \"Persian\",\n \"words\": \"bâlâxâneh «بالاخانه»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"بالاخانه is a transparent Persian determinative compound, بالا bālā 'high, upper' (< MP bālāy < Av. barəzant- 'high', the *bhergh- root to which Nourai's own cross-reference '☞Bhergh' points) + خانه xāna 'house/room', hence 'upper room'. It is well attested from classical times: Dehkhoda «عمارت دوطبقه؛ اطاقی که بر پشت بام سازند … خانهٔ طبقهٔ دوم؛ خانه روی خانه», Mo'in «(اِمر.) ساختمان کوچک با یک یا چند اتاق در قسمت فوقانی خانه و مستقل از آن», ʿAmid «خانه‌ای که بالای خانهٔ دیگر ساخته می‌شود». Lokotsch no.197 gives the identical analysis, citing Horn for both members: 'Pers. bālāḫāna [aus pers. bālā „hoch“ Horn NpEt S.39 Nr.171 und pers. ḫānā „Haus“ ebenda S.103 Nr.465; also eigentlich „Hochhaus“] „ein oberes Zimmer, hervorstehender Teil des Hauses, Erker, Balkon“'. The word and its formation are certain; only the ancestry claimed for its second element (node 9) is contested.\",\n \"derivation_fa\": \"«بالاخانه» ترکیبی وصفی و کاملاً شفاف در فارسی است: «بالا» (از bālāy فارسی میانه و آن از barəzant- اوستایی «بلند»، همان ریشه‌ای که نورایی با نشانهٔ ☞Bhergh به آن ارجاع داده) + «خانه»، یعنی «اتاق بالایی». کاربردش از دورهٔ کلاسیک گواهی شده است: دهخدا «عمارت دوطبقه؛ اطاقی که بر پشت بام سازند … خانهٔ طبقهٔ دوم؛ خانه روی خانه»، معین «ساختمان کوچک با یک یا چند اتاق در قسمت فوقانی خانه و مستقل از آن»، عمید «خانه‌ای که بالای خانهٔ دیگر ساخته می‌شود». لوکوچ در شمارهٔ ۱۹۷ همین تحلیل را با ارجاع به هرن برای هر دو جزء می‌آورد. ساخت و معنای واژه قطعی است؛ تنها نسبی که برای جزء دومش ادعا شده (گرهٔ ۹) محل بحث است.\",\n \"sources\": [\"https://abadis.ir/fatofa/%D8%A8%D8%A7%D9%84%D8%A7%D8%AE%D8%A7%D9%86%D9%87/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:465\", \"status\": \"supports\",\n    \"note\": \"Mo'in s.v. بالاخانه (read via abadis.ir, section فرهنگ معین, archived as data/verification/sources/web/bb448bdcfe2b00ef.txt): «(نِ) (اِمر.) ساختمان کوچک با یک یا چند اتاق در قسمت فوقانی خانه و مستقل از آن». The page number is consistent with Mo'in's ب section (cf. MON:467 for بالکن two entries later).\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no.197, pp.17-18 (LKT.txt line 665)\", \"stance\": \"supports\",\n    \"note\": \"'197. Pers. bālāḫāna: [Aus pers. bālā „hoch“ Horn NpEt S.39, Nr.171 und pers. ḫānā „Haus“ ebenda S.103, Nr.465; also eigentlich „Hochhaus“] „ein oberes Zimmer, hervorstehender Teil des Hauses, Erker, Balkon“'.\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan p.55 s.v. BALCON (PHN.txt line 2109)\", \"stance\": \"supports\",\n    \"note\": \"'BALCON, s. m. composé, (p.) بالاخانه [bâlâkhâneh], composé de l'adjectif بالا [bâlâ] élevé, et du substantif خانه [khâneh] maison, demeure ou appartement. Partie supérieure d'une habitation, d'où l'on aperçoit les alentours; belvédère.'\"},\n   {\"src\": \"ARY\", \"where\": \"Dehkhoda, Loghatnāme s.v. بالاخانه (abadis.ir)\", \"stance\": \"supports\",\n    \"note\": \"«عمارت دوطبقه. اطاقی که بر پشت بام سازند (از آنندراج). اطاقی که فوق اطاق دیگر ساخته شده باشد (فرهنگ نظام). منظر. عمارت فوقانی (ناظم‌الاطباء). خانهٔ طبقهٔ دوم … خانه روی خانه», with a verse of Mirzā ʿAbdolḡani.\"}\n ]\n})\n\nN.append({\n \"id\": 11,\n \"lang\": \"Italian\",\n \"words\": \"barbacane, balcone\",\n \"verdict\": \"disputed\",\n \"derivation\": \"The two Italian words must be judged separately. barbacane 'battered outer wall, barbican' (also Provençal barbacana, Catalan/Spanish barbacana, Portuguese barbacã) is plausibly oriental: Lokotsch no.197 derives it from Persian bālāḫāna 'mit vielfachen Kontaminationen ähnlich bedeutender Wörter und unter volksetymologischen Einflüssen', and Klein s.v. barbican agrees; Etymonline is more guarded ('a general Romanic word, said to be ultimately from Arabic or Persian (compare bab-khanah „gate-house“); according to Watkins from Old Iranian compound *pari-varaka-'). balcone is a different story: the modern consensus is that it is balco 'scaffold, beam-platform' + the augmentative -one, and balco is a Langobardic/Old High German loan, *balko / balcho 'beam' — Klein: 'It. balcone, formed with the augmentative suff. -one fr. balco, „scaffold“, which is borrowed fr. OHG. balcho, „beam“'; Etymonline the same; Watkins files BALCONY under *bhelg- 'beam, plank' beside BALK. Lokotsch does argue the opposite ('Annahme eines ahd. palco „Balken“ als Grundwort abzulehnen'), and even he notes that Löbel called the derivation an 'etimologia dubbiosa'; but on balcone he is now isolated. Since one of the two words in the node is derived by the whole modern literature from Germanic rather than from Persian, the node as drawn is disputed.\",\n \"derivation_fa\": \"دو واژهٔ ایتالیایی این جعبه را باید جدا سنجید. barbacane «دیوار بیرونی قلعه، باروی پیشین» (و همتاهای پرووانسی، کاتالانی، اسپانیایی و پرتغالی آن) به احتمال خاستگاهی شرقی دارد: لوکوچ در شمارهٔ ۱۹۷ آن را با آمیختگی‌های فراوان و تأثیر ریشه‌شناسی عامیانه از «بالاخانه» فارسی می‌گیرد و کلاین نیز همین را می‌گوید؛ اتیمآنلاین محتاط‌تر است و می‌نویسد «واژه‌ای عمومی در زبان‌های رومی که گفته‌اند سرانجام از عربی یا فارسی است (قس bāb-ḵāna «دروازه‌خانه»)» و از قول واتکینز صورت ایرانی باستان *pari-varaka- را می‌آورد. اما balcone داستان دیگری دارد: اجماع امروزی آن را balco «داربست، تیرپوش» + پسوند بزرگ‌ساز -one می‌داند و balco خود وام‌واژه‌ای لومباردی/آلمانی علیای باستان است از *balko «تیر» — کلاین، اتیمآنلاین و واتکینز (که BALCONY را ذیل *bhelg- «تیر، تخته» در کنار BALK می‌آورد) همگی چنین می‌گویند. لوکوچ خلاف این را استدلال می‌کند، ولی در مورد balcone امروز تنها مانده است. چون یکی از دو واژهٔ این گره در تمام ادبیات جدید از ژرمنی گرفته می‌شود نه از فارسی، حکم گره «رد شده» است.\",\n \"sources\": [\"https://www.etymonline.com/word/balcony\", \"https://www.etymonline.com/word/barbican\"],\n \"ref_check\": [\n   {\"ref\": \"LKT:17\", \"status\": \"supports\",\n    \"note\": \"Lokotsch, Etym. Wb. der europäischen Wörter orientalischen Ursprungs, no.197 (printed pp.17-18; LKT.txt line 665, the entry straddles the page break marked by the signature line 'Lokotsch, Etymolog. Wörterbuch'): '… hieraus mit vielfachen Kontaminationen … it. barbacane „Brustwehr mit Schießscharten, Stützmauer“, prov. barbacana, frz. barbacane … Wenn Löbel EITAP 11 diese Ableitung mit mehr als einem Schein von Recht etimologia dubbiosa nennt, so sind die folgenden Wörter aus semantischen Gründen unzweifelhaft aus dem angegebenen Grundwort abzuleiten und Annahme eines ahd. palco „Balken“ als Grundwort abzulehnen: it. balcone, frz. balcon, rum. balcon, sp. balcón, pg. balcão; dtsch. Balkon, engl. balcony …'. So Nourai's citation is exact — the reference does say what his arrow says. It is Lokotsch who is out of step with modern scholarship.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. balcony and barbican (KLN_1966.txt lines 4311, 4441)\", \"stance\": \"partial\",\n    \"note\": \"'balcony, n. — It. balcone, formed with the augmentative suff. -one fr. balco, „scaffold“, which is borrowed fr. OHG. balcho, „beam“ … See balk, „beam“.' — contradicts Lokotsch on balcone; but 'barbican … prob. derives ult. fr. Pers. bāla-khāna, „upper chamber, balcony on the top of a house“' — supports him on barbacane.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index (AHD_watkins1985.txt line 1276)\", \"stance\": \"contradicts\",\n    \"note\": \"'BALCONY bhelg- … BALK bhelg-' — Watkins files balcony with the Germanic beam-word, which is the 'different roots' Nourai's own note in node 14 points the reader to.\"},\n   {\"src\": \"PHN\", \"where\": \"Pihan p.55 (PHN.txt lines 2109-2118)\", \"stance\": \"supports\",\n    \"note\": \"'De là viennent très-probablement, malgré l'altération d'orthographe, l'anglais balcony, le portugais balcão, l'italien balcone, l'espagnol et le français balcon' — the 19th-century French orientalist tradition on which Lokotsch and Nourai both rest.\"}\n ]\n})\n\nN.append({\n \"id\": 12,\n \"lang\": \"French\",\n \"words\": \"balcon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The step drawn here — Italian balcone > French balcon — is certain and uncontroversial: French borrowed balcon from Italian in the 16th century, along with much other Renaissance architectural vocabulary (cf. English balcony 1610s, also from Italian). Pihan, the reference Nourai cites, treats the French word in exactly this position, and Lokotsch no.197 lists 'frz. balcon' in the same series as it. balcone. What is disputed is not this arrow but the one above it: the Italian balcone is now derived from Germanic balco 'beam', so the French word's ultimate ancestor is not Persian bālāxāne.\",\n \"derivation_fa\": \"این حلقه — از balcone ایتالیایی به balcon فرانسوی — قطعی و بی‌مناقشه است: فرانسوی این واژه را در سدهٔ شانزدهم همراه انبوهی از اصطلاحات معماری رنسانس از ایتالیایی وام گرفت (چنان‌که انگلیسی هم balcony را در دههٔ ۱۶۱۰ از ایتالیایی گرفت). پیهان — همان مرجعی که نورایی آورده — واژهٔ فرانسوی را دقیقاً در همین جایگاه می‌نشاند و لوکوچ نیز «frz. balcon» را در همان رشته با «it. balcone» می‌آورد. آنچه محل بحث است این پیکان نیست بلکه پیکان بالاتر است: balcone ایتالیایی امروز از balco ژرمنی «تیر» گرفته می‌شود، پس نیای نهایی واژهٔ فرانسوی «بالاخانه»ی فارسی نیست.\",\n \"sources\": [\"https://www.etymonline.com/word/balcony\"],\n \"ref_check\": [\n   {\"ref\": \"PHN:55\", \"status\": \"supports\",\n    \"note\": \"Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, p.55 (PHN.txt line 2109; confirmed by the book's own index at line 10273, 'Balcon, s. m. composé, (p.) Page 55'): 'BALCON … بالاخانه [bâlâkhâneh], composé de l'adjectif بالا [bâlâ] élevé, et du substantif خانه [khâneh] maison … De là viennent très-probablement, malgré l'altération d'orthographe, l'anglais balcony, le portugais balcão, l'italien balcone, l'espagnol et le français balcon, servant à désigner une galerie avec balustrade devant les fenêtres d'une maison.'\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no.197 (LKT.txt line 667)\", \"stance\": \"supports\",\n    \"note\": \"'it. balcone, frz. balcon, rum. balcon, sp. balcón, pg. balcão; dtsch. Balkon, engl. balcony; russ. bulg. serb. poln. balkon' — the French form in the same series.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. balcony (KLN_1966.txt line 4311)\", \"stance\": \"partial\",\n    \"note\": \"Klein routes the word the same way as far as Italian ('It. balcone … fr. balco „scaffold“') but takes balco from OHG balcho 'beam', so the French borrowing from Italian stands while the Persian source does not.\"},\n   {\"src\": \"DEV\", \"where\": \"Devic, Dictionnaire étymologique des mots français d'origine orientale (DEV.txt)\", \"stance\": \"silent\",\n    \"note\": \"A grep of DEV.txt for 'balcon' returns nothing: Devic, unlike Pihan, does not list balcon among the French words of oriental origin — a silence that is itself evidence of 19th-century disagreement.\"}\n ]\n})\n\nN.append({\n \"id\": 13,\n \"lang\": \"Persian\",\n \"words\": \"bâlkon «بالکن»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"بالکن bālkon is a modern (late 19th-/20th-century) Persian borrowing of French balcon, one of the large group of French architectural and technical loans that entered Persian through the Dār al-Fonūn period and the press; the -on spelling with ـن reflects French [-ɔ̃], and the word coexists with the native بالاخانه and مهتابی. Mo'in's entry (the reference Nourai cites) glosses it «(اِ.) ایوان کوچکی که در جلوی ساختمان سازند؛ مهتابی. (نم.) طبقهٔ فوقانی تماشاخانه یا سینما که قسمتی از سالن تحتانی را در زیر می‌گیرد» — i.e. both the architectural and the theatre sense of the French word, showing it is a loan and not a continuation of بالاخانه. This makes بالکن a genuine round trip only if the Persian origin of balcone were true; on the modern view it is simply a Germanic-Romance word returning to Persian.\",\n \"derivation_fa\": \"«بالکن» وام‌واژه‌ای نو (اواخر سدهٔ سیزدهم/چهاردهم هجری) از balcon فرانسوی است و از جملهٔ انبوه وام‌واژه‌های معماری و فنی فرانسوی است که از روزگار دارالفنون و مطبوعات به فارسی راه یافت؛ املای «ـن» پایانی بازتاب واکهٔ خیشومی فرانسوی است و واژه در کنار «بالاخانه» و «مهتابی» به کار می‌رود. معین — همان مرجعی که نورایی داده — آن را چنین معنی کرده: «(اِ.) ایوان کوچکی که در جلوی ساختمان سازند؛ مهتابی. (نم.) طبقهٔ فوقانی تماشاخانه یا سینما که قسمتی از سالن تحتانی را در زیر می‌گیرد» — یعنی هر دو معنای فرانسوی، که نشان می‌دهد وام‌واژه است نه دنبالهٔ «بالاخانه». اگر خاستگاه فارسی balcone درست می‌بود، این یک «سفر رفت‌وبرگشت» واقعی بود؛ بنا بر دیدگاه امروزی، واژه‌ای ژرمنی‌ـ رومی است که به فارسی آمده است.\",\n \"sources\": [\"https://www.etymonline.com/word/balcony\"],\n \"ref_check\": [\n   {\"ref\": \"MON:467\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. بالکن (MON_part1.txt line 20927): «بالکن: (اِ.) ایوان کوچکی که در جلوی ساختمان سازند؛ مهتابی. (نم.) طبقهٔ فوقانی تماشاخانه یا سینما که قسمتی از سالن تحتانی را در زیر می‌گیرد». The entry sits two headwords after بالکانه and before بال‌ماسکه, i.e. exactly where p.467 would fall given بالاخانه at p.465.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"MON_part1.txt lines 20920-20930\", \"stance\": \"supports\",\n    \"note\": \"The neighbouring headwords — بالکانه «پنجره‌ای که از میله‌های فلزی…», بال‌ماسکه «مجلس رقصی که شرکت‌کنندگان…» — are themselves European loans, confirming that Mo'in treats بالکن as part of the modern French stratum.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no.197 (LKT.txt line 667)\", \"stance\": \"partial\",\n    \"note\": \"Lokotsch lists the word's spread back east only as far as 'russ. bulg. serb. poln. balkon, čech. balkón' and notes 'Auf direkterem Wege, höchstens über tat. bālāhāne ist russ. balagan „Marktbude aus Brettern“ entstanden'; he does not record a re-borrowing into Persian, which is a 20th-century fact later than his 1927 book.\"}\n ]\n})\n\nN.append({\n \"id\": 14,\n \"lang\": \"English\",\n \"words\": \"barbican, balcony\",\n \"verdict\": \"disputed\",\n \"derivation\": \"barbican (Middle English barbecan, from Old French barbacane, mid-13c.) is the item for which a Persian source has real currency: Klein, 'barbican, n., outer defense of a city or castle. — ME. barbecan, fr. OF. barbacan, barbican (F. barbacane), which prob. derives ult. fr. Pers. bālā-khāna, „upper chamber, balcony on the top of a house“, lit. „a high house“, fr. bālā, „high“, and khāna, „house“ … The second element derives fr. stem khan-, „to dig“' — i.e. Nourai's KLN:148 says precisely what his arrow says. But Etymonline reports the competing accounts ('said to be ultimately from Arabic or Persian (compare bab-khanah „gate-house“); according to Watkins from Old Iranian compound *pari-varaka-, from *pari- „around“ + *varaka-, from PIE root *wer- „to cover“'), so even here the specific bālā-xāna source is one option among three. balcony (1610s), on the other hand, is derived by every modern authority from Italian balcone < balco 'scaffold' < Langobardic *balko 'beam' (Etymonline; Klein; Watkins files BALCONY and BALK together under *bhelg-). Nourai's own note, 'See AHD for different roots', is an honest signal that he knew this; modern scholarship takes the AHD side for balcony and leaves barbican open.\",\n \"derivation_fa\": \"barbican انگلیسی (انگلیسی میانه barbecan، از barbacane فرانسوی کهن، میانهٔ سدهٔ سیزدهم) تنها واژهٔ این جعبه است که خاستگاه فارسی برایش جدی گرفته می‌شود: کلاین می‌نویسد «barbican … احتمالاً سرانجام از bālā-khāna فارسی „اتاق بالایی، بالاخانه“، تحت‌اللفظ „خانهٔ بلند“، از bālā „بلند“ و khāna „خانه“ … جزء دوم از ستاک khan- „کندن“ است» — یعنی ارجاع KLN:148 نورایی دقیقاً همان چیزی را می‌گوید که پیکانش ادعا می‌کند. اما اتیمآنلاین روایت‌های رقیب را هم می‌آورد («گفته‌اند سرانجام از عربی یا فارسی است، قس bāb-ḵāna „دروازه‌خانه“؛ به گفتهٔ واتکینز از ترکیب ایرانی باستان *pari-varaka-»)، پس حتی اینجا هم «بالاخانه» یکی از سه گزینه است. در برابر، balcony (۱۶۱۰م) را همهٔ مراجع امروزی از balcone ایتالیایی و آن را از balco «داربست» و آن را از *balko لومباردی «تیر» می‌گیرند (اتیمآنلاین، کلاین، و واتکینز که BALCONY و BALK را با هم ذیل *bhelg- می‌آورد). یادداشت خود نورایی («برای ریشه‌های دیگر به AHD نگاه کنید») نشان می‌دهد که او از این اختلاف آگاه بوده؛ پژوهش امروزی دربارهٔ balcony جانب AHD را می‌گیرد و دربارهٔ barbican مسئله را باز می‌گذارد.\",\n \"sources\": [\"https://www.etymonline.com/word/barbican\", \"https://www.etymonline.com/word/balcony\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:148\", \"status\": \"supports\",\n    \"note\": \"Klein, s.v. barbican (KLN_1966.txt line 4441; the entry falls in the ba- range that his 1966 two-volume pagination puts around p.148): 'barbican, n., outer defense of a city or castle. — ME. barbecan, fr. OF. barbacan, barbican (F. barbacane), which prob. derives ult. fr. Pers. bāla-khāna, „upper chamber, balcony on the top of a house“, lit. „a high house“, fr. bala, „high“, and khāna, „house“. The first element is rel. to Avestic bərəzant-, OI. bṛhant-, „high“; see borough. The second element derives fr. stem khan-, „to dig“.' Note that Klein's own entry for balcony, a few pages earlier, contradicts the Persian derivation for that word.\"},\n   {\"ref\": \"LKT:17\", \"status\": \"supports\",\n    \"note\": \"Lokotsch no.197 explicitly includes 'engl. balcony' in the list of forms he derives from bālāḫāna while rejecting the OHG palco etymology; the citation is accurate, the doctrine outdated.\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, English index and *bhelg- entry (AHD_watkins1985.txt line 1276)\", \"stance\": \"contradicts\",\n    \"note\": \"'BALCONY bhelg-', beside 'BALK bhelg-' — the Germanic beam-root; this is the 'different roots' Nourai's note refers the reader to.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etym. Dict. (SKT.txt)\", \"stance\": \"silent\",\n    \"note\": \"Skeat's concise edition has no barbican entry retrievable in this scan, and his balcony treatment does not appear in the searched range; no independent English witness for the Persian derivation beyond Klein.\"},\n   {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century (WEB_vol1.txt)\", \"stance\": \"silent\",\n    \"note\": \"Grep of the b-range for 'barbican' in this volume returned no usable entry (OCR gap); could not be used either way.\"}\n ]\n})\n\nN.append({\n \"id\": 15,\n \"lang\": \"Arabic\",\n \"words\": \"xandaq\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Arabic خَنْدَق ḵandaq 'moat, fortification ditch' is one of the best-attested Persian loanwords in Arabic — it is the word of the Battle of the Trench (ġazwat al-ḵandaq, 5 AH/627 CE), when Salmān al-Fārisī is said to have proposed the Persian device of a ditch around Medina, and the sūra al-Aḥzāb episode fixed it in the language. Asbaghi's monograph gives exactly the derivation Nourai draws: from Persian کنده kanda, the past participle of کندن kandan 'to dig', going back to Middle Persian kandag and beyond that to Avestan/Old Persian kan- 'to dig'. The Arabic form shows the regular treatment of the Persian aspirated/velar initial as ḵ- (the same x- Horn and Nyberg posit for Pahlavi xandak/xandag) and the insertion of the Arabic quadriliteral pattern faʿlal, whence the sound plural ḵanādiq. Syriac and Armenian (ḵandak) borrowed the same Iranian word independently.\",\n \"derivation_fa\": \"«خَنْدَق» عربی از شناخته‌شده‌ترین وام‌واژه‌های فارسی در عربی است — همان واژهٔ «غزوهٔ خندق» (سال پنجم هجری) که به روایت سنّت اسلامی سلمان فارسی تدبیر ایرانیِ کندنِ خندق را پیرامون مدینه پیشنهاد کرد و داستان سورهٔ احزاب آن را در زبان تثبیت کرد. آسبقی در «وام‌واژه‌های فارسی در عربی» دقیقاً همان اشتقاقی را می‌دهد که نورایی کشیده است: از «کنده»ی فارسی، اسم مفعول «کندن»، و آن از kandag فارسی میانه و سرانجام از kan- اوستایی/پارسی باستان «کندن». صورت عربی، همخوان آغازین را به «خ» بدل کرده (همان x که هرن و نیبرگ برای پهلوی xandak/xandag فرض می‌کنند) و واژه را در وزن رباعی «فَعْلَل» ریخته که جمعش «خنادق» می‌شود. سریانی و ارمنی (xandak) نیز همین واژهٔ ایرانی را جداگانه وام گرفته‌اند.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%86%D8%AF%D9%82\"],\n \"ref_check\": [\n   {\"ref\": \"PLA:113\", \"status\": \"supports\",\n    \"note\": \"Asbaghi, Persische Lehnwörter im Arabischen, p.113 (incoming/PLA/PLA_pages.txt, form-feed block 128, running heads 'ḫanǧar … 113'): 'ḫandaq: „Festungsgraben“ aus dem pers. کنده kande, pass. pt. v. Verb kandan „graben“ < mp. kandag ← aw./ap. kan „graben“; ar. Lw. > … syr. …' — with references to Bharucha, Nyberg and Brockelmann. This is precisely Nourai's arrow, on precisely the cited page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. kandan (NYB_vol2_glossary.txt line 2196)\", \"stance\": \"supports\",\n    \"note\": \"'Paz. xandan, xan- with an initial x- confirmed by the Arab. lw. xandag „trench“ and Skr khan- (pt. khāta-)' — Nyberg uses the Arabic loan as the proof of the Iranian x-form, the mirror image of Asbaghi's argument.\"},\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Pers. Stud. no.869, p.88 (HUB.txt line 3123)\", \"stance\": \"partial\",\n    \"note\": \"'Das angeführte phl. xantak (wo vorkommend?) kann nur das falsch ins Pehlevi umgeschriebene arab. pers. xandaq = arm. xandak (bei Steph. Asoł. und Späteren!) sein, dessen reguläre np. Form kanda ist.' Hübschmann accepts the Iranian source but denies that a Pahlavi xantak is independently attested — a caution about the Pahlavi node above, not about the Arabic loan itself.\"},\n   {\"src\": \"KLN\", \"where\": \"Wiktionary s.v. خندق, Arabic section (archived)\", \"stance\": \"supports\",\n    \"note\": \"'An Iranian borrowing: compare Persian کندک (kandak), کنده (kanda), Old Armenian քանդակ (kʻandak) (also from Iranian).'\"}\n ]\n})\n\nN.append({\n \"id\": 16,\n \"lang\": \"Persian\",\n \"words\": \"xandaq «خندق»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Modern Persian خندق xandaq is a re-borrowing from Arabic — a classic Persian→Arabic→Persian round trip. Mo'in's dictionary marks it as such in the etymological bracket of the headword: «خندق [معرَّب خندک ـ کندک ـ کنده] (اِ.) گودالی که گرد حصار و قلعه و لشکرگاه کنند تا مانع عبور دشمن و سیل گردد؛ ج. خنادق» — 'Arabicised from xandak / kandak / kanda'. The Arabic broken plural خنادق used in Persian, and the -aq ending alien to native Persian phonotactics, both mark the loan; the inherited Persian form of the same word is کنده kanda (still 'ditch, trench'), which Hübschmann called 'die reguläre np. Form'. Wiktionary states the round trip explicitly: 'Borrowed from Arabic خَنْدَق (ḵandaq), from Middle Persian *ḵandag (whence Persian هندک handak „moat“)'.\",\n \"derivation_fa\": \"«خندق» در فارسی نو وام‌واژه‌ای است که از عربی بازگشته — نمونهٔ روشن سفر رفت‌وبرگشتِ فارسی ← عربی ← فارسی. معین در قلاب ریشه‌شناختی سرواژه همین را می‌گوید: «خندق [معرَّب خندک ـ کندک ـ کنده] (اِ.) گودالی که گرد حصار و قلعه و لشکرگاه کنند تا مانع عبور دشمن و سیل گردد؛ ج. خنادق». جمع مکسّر عربی «خنادق» که در فارسی به کار می‌رود و پایانهٔ ـق که با ساخت آوایی واژه‌های اصیل فارسی نمی‌خواند، هر دو نشانهٔ وام‌گیری‌اند؛ صورت موروثی همین واژه در فارسی «کنده» است که هوبشمان آن را «صورت منظم فارسی نو» خوانده. ویکی‌واژه نیز صریحاً می‌نویسد: «وام‌گرفته از خَنْدَق عربی، خود از *ḵandag فارسی میانه». ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/%D8%AE%D9%86%D8%AF%D9%82\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1443\", \"status\": \"supports\",\n    \"note\": \"Mo'in, Farhang-e Farsi s.v. خندق (MON_part1.txt line 57559): «خندق: [معر. خندکک ـ کندگکك ـ کنده] (ا.) گودالی که گرد حصار و قلعه و لشکرگاه کنند تا مانع عبور دشمن و سیل گردد؛ ج. خنادق» (the doubled letters are OCR noise for خندک / کندک). Mo'in's «معرَّب» tag is exactly Nourai's Arabic→Persian arrow, and the entry's position (between خندستان and خنده) is consistent with p.1443.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Hübschmann, Pers. Stud. no.869 (HUB.txt line 3123)\", \"stance\": \"supports\",\n    \"note\": \"'… arab. pers. xandaq = arm. xandak …, dessen reguläre np. Form kanda ist' — Hübschmann labels the word 'arab. pers.', i.e. an Arabic-mediated Persian form beside the inherited کنده.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi p.113\", \"stance\": \"supports\",\n    \"note\": \"By deriving Arabic ḫandaq from Persian kanda / MP kandag, Asbaghi makes the modern Persian خندق necessarily a re-import, since it cannot be the direct continuation of kandag (which would give *kanda).\"},\n   {\"src\": \"ARY\", \"where\": \"Wiktionary s.v. خندق, Persian section (archived)\", \"stance\": \"supports\",\n    \"note\": \"'Borrowed from Persian خندق (xandaq), itself from Arabic خَنْدَق (ḵandaq, „trench, moat“), ultimately from Middle Persian *ḵandag' (in the entry for the onward Ottoman/Turkish borrowing), and for Persian itself 'Borrowed from Arabic خَنْدَق (ḵandaq), from Middle Persian *ḵandag (whence Persian هندک handak „moat“)'.\"}\n ]\n})\n\nout = {\n \"pdf_page\": 213,\n \"book_page\": 183,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [root]\n}\n\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-213.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\nprint(\"written\", len(N), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build213.py && python3 -m json.tool data/verification/page-213.json > /dev/null && echo JSON_OK && python3 tools/verify_check.py 213",
 "description": "Write and validate page-213.json"
}
```


### [2026-09-06T15:16:28.781Z] TOOL RESULT

```
written 16 nodes
JSON_OK
nodes verified: 16/16
node verdicts: {'disputed': 6, 'plausible': 1, 'confirmed': 9}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 21, 'contradicts': 1, 'not_checked': 4, 'partial': 3, 'not_found': 1}
books consulted: {'supports': 27, 'contradicts': 7, 'partial': 6, 'silent': 4} | by book: {'KLN': 7, 'HUB': 4, 'ARY': 4, 'PHD': 3, 'WEB': 3, 'LKT': 3, 'NYB': 2, 'MON': 2, 'SKT': 2, 'PHN': 2, 'AHD': 2, 'KNT': 1, 'CHEUNG': 1, 'SYN': 1, 'BQT': 1, 'FSD': 1, 'FRS': 1, 'HRN': 1, 'BRT': 1, 'DEV': 1, 'PLA': 1}
```


## [2026-09-06T15:16:52.257Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"کنند\" FRS.txt | head -5; echo \"=== FRS pages\"; grep -n \"کنند\" FRS_pages.txt | head -5",
 "description": "Grep Loghat-e Fors for kanand"
}
```


### [2026-09-06T15:16:52.324Z] TOOL RESULT

```
759:بود که چهاربای درش کنند . ه - چ اضافه‌دارد : :وآرام‌هم ‏ ۰ معنی نابروا فقط در 
917:گ : نوا دستان بودکه بر رودها راست کننده بو سف ی : 
992:سیخی باشد ِ باچیزی بدان بر ان بر بان کنند و بگردانند 
1012:۳ -س : کردنا مر ی باچیزی که بر آ نش بریان کنند ۰ چ ؛ گردنا مر بی بود که 
1014:کنند . مطابق تعر اف ع‌ وان گردنا بمعنی سیخ است که مر غ بدان بربان کنند و 
=== FRS pages
838: ‫بود که چهاربای درش کنند ‪ .‬ه ‪ -‬چ اضافه‌دارد ‪: :‬وآرام‌هم ‏ ‪ ۰‬معنی نابروا فقط در‬
1016:                ‫‪:‬‬        ‫گ ‪ :‬نوا دستان بودکه بر رودها راست کننده بو سف ی‬
1080:‫باچیزی بدان بر ان بر بان کنند و بگردانند‬                  ‫ِ‬‫سیخی باشد‬
1099:‫‪ :‬کردنا مر ی باچیزی که بر آ نش بریان کنند ‪ ۰‬چ ؛ گردنا مر بی بود که‬              ‫‪- ۳‬س‬
1101:‫کنند ‪ .‬مطابق تعر اف ع‌ وان گردنا بمعنی سیخ است که مر غ بدان بربان کنند و‬
```


## [2026-09-06T15:17:17.579Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'PYEOF'\nimport json, io\np='data/verification/page-213.json'\nd=json.load(open(p,encoding='utf-8'))\nnodes={n['id']:n for n in d['entries'][0]['nodes']}\n\n# node 3: third consulted was an unarchived Mo'in/Dehkhoda claim -> replace with archived Wiktionary\nnodes[3]['consulted'][2] = {\"src\":\"WIKT\",\"where\":\"Wiktionary s.v. کندن, Persian section (archived as data/verification/sources/web/f6c6b73ccca78760.txt)\",\"stance\":\"supports\",\"note\":\"'From Middle Persian kntn' (kantan, „to dig“), from Proto-Iranian *kánHati („to dig“)' — an independent modern statement of the node-2 -> node-3 step, with no gʷhen- anywhere in the chain.\"}\n\n# node 4: second consulted mislabelled FSD, the quotation is Webster\nnodes[4]['consulted'][1]['src']='WEB'\nnodes[4]['consulted'][1]['where']=\"Webster's New Twentieth Century Dictionary, s.v. gondola (WEB_vol1.txt line 83034)\"\n\n# node 7: relabel Dehkhoda, and be honest about Loghat-e Fors\nnodes[7]['consulted'][0]['src']='DKH'\nnodes[7]['consulted'][0]['where']=\"Dehkhoda, Loghatnāme s.v. کنند (via abadis.ir; archived as data/verification/sources/web/5505f84618f4aefe.txt)\"\nnodes[7]['consulted'][1]={\"src\":\"FRS\",\"where\":\"Asadi Tusi, Loghat-e Fors — searched FRS.txt / FRS_pages.txt for کنند\",\"stance\":\"partial\",\"note\":\"The local OCR of Loghat-e Fors is too degraded for the headword to be located directly (greps for کنند return only unrelated verb forms); but Dehkhoda quotes the entry from it verbatim — «بیلی باشد سراندرچفته، برزگران دارند و به ماوراءالنهر بیشتر بود. (لغت فرس اسدی چ اقبال ص ۹۰)» — together with the Rudaki, Abu'l-Abbas and Khojasteh verses, so the 11th-century attestation is secured at one remove.\"}\n\n# node 10: relabel Dehkhoda\nnodes[10]['consulted'][2]['src']='DKH'\nnodes[10]['consulted'][2]['where']=\"Dehkhoda, Loghatnāme s.v. بالاخانه (via abadis.ir; archived as data/verification/sources/web/bb448bdcfe2b00ef.txt)\"\n\n# node 15 / 16: Wiktionary entries mislabelled KLN / ARY\nnodes[15]['consulted'][2]['src']='WIKT'\nnodes[15]['consulted'][2]['where']=\"Wiktionary s.v. خندق, Arabic section (archived as data/verification/sources/web/522364dfc1625814.txt)\"\nnodes[16]['consulted'][2]['src']='WIKT'\nnodes[16]['consulted'][2]['where']=\"Wiktionary s.v. خندق, Persian and Ottoman Turkish sections (archived as data/verification/sources/web/522364dfc1625814.txt)\"\n\n# node 8: add the archived Dehkhoda source label for xani already in sources; fine.\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint('patched')\nPYEOF\npython3 -m json.tool data/verification/page-213.json >/dev/null && echo JSON_OK && python3 tools/verify_check.py 213",
 "description": "Patch source labels and re-validate"
}
```


### [2026-09-06T15:17:19.336Z] TOOL RESULT

```
patched
JSON_OK
nodes verified: 16/16
node verdicts: {'disputed': 6, 'plausible': 1, 'confirmed': 9}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 21, 'contradicts': 1, 'not_checked': 4, 'partial': 3, 'not_found': 1}
books consulted: {'supports': 26, 'contradicts': 7, 'partial': 7, 'silent': 4} | by book: {'KLN': 6, 'HUB': 4, 'WEB': 4, 'PHD': 3, 'WIKT': 3, 'LKT': 3, 'NYB': 2, 'SKT': 2, 'DKH': 2, 'PHN': 2, 'AHD': 2, 'KNT': 1, 'CHEUNG': 1, 'SYN': 1, 'BQT': 1, 'ARY': 1, 'FRS': 1, 'HRN': 1, 'BRT': 1, 'DEV': 1, 'MON': 1, 'PLA': 1}
```


## [2026-09-06T15:17:24.747Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls -la data/verification/page-213.json data/verification/sources/refs/ocr/BOOK/213.png; ls data/verification/sources/refs/ocr/BQT/ 2>/dev/null | tail -5; head -c 20 data/verification/page-213.json | xxd | head -2",
 "description": "Final file checks"
}
```


### [2026-09-06T15:17:27.854Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 84832 Sep  6 11:17 data/verification/page-213.json
-rw-rw-r-- 1 sfmqrb sfmqrb 83761 Sep  6 11:07 data/verification/sources/refs/ocr/BOOK/213.png
72.vision.txt
733.png
733.vision.txt
902.png
902.vision.txt
00000000: 7b0a 2022 7064 665f 7061 6765 223a 2032  {. "pdf_page": 2
00000010: 3133 2c0a                                13,.
```


## [2026-09-06T15:17:53.119Z] AGENT

Page 213 (book p. 183), root **Gwhen 1 — PART 2**, 1 entry / 16 nodes. `verify_check.py 213` → 0 PROBLEM lines.

Counts: root confirmed; nodes 9 confirmed, 1 plausible, 6 disputed.

Disputed items:
- **ROOT→#1 (Av./OP kan, xan, gan 1; čāt)** — the words are real (Kent 178b, Bartholomae 583) but the whole PART‑2 tree hangs on the wrong root. Pokorny 491 *gʷhen‑* "swell" contains only āgandan-type words; Walde‑Pokorny put "dig" under a separate *qhen‑* (WP I 399), Pokorny himself under *ken‑* (IEW 634 fn.), Cheung under *kanH¹ < *kenH₂‑ (LIV 344). Also no Av./OP verb **gan‑** "to dig" exists (the g‑form is the "to fill" stem, i.e. the real gʷhen‑ reflex), and the gloss "dig dirt out and mound it up" is Nourai's own bridge.
- **#4 Greek konda, kondu** — κόνδυ is real but is a Near‑Eastern Wanderwort (Neo‑Bab. kandu ← Aram. kandā ← Skt. kandu, or Pre‑Greek per Furnée), not from Persian kandūk; "konda" is not Greek at all — Nourai read Skeat's *Italian* gonda as Greek.
- **#5 Italian gonda, gondola** — Skeat's Greek etymology is rejected: Etymonline "of unknown origin", Klein ← Friulian gondolà, Webster ← Romance dond‑.
- **#9 Persian xāneh, ğāneh** — modern view derives خانه from PIr *wāhana‑ "dwelling" (< *h₂wes‑), not from kan‑; Hübschmann (no. 869 n.) already doubted Horn's kan‑ etymology. Also **غانه "house" is not a Persian word** — Dehkhoda has غانه only as place‑names (a town on the Euphrates, = عانه; and Ghana). The printed page really prints it, so this is Nourai's own coinage, not an extraction error.
- **#11 Italian barbacane, balcone / #14 English barbican, balcony** — barbacane/barbican from bālā‑xāna is defensible (Klein, Lokotsch 197, Pihan 55; Etymonline offers bāb‑ḵāna and Watkins' *pari‑varaka‑ as rivals), but balcone/balcony is universally from balco "scaffold" ← Langobardic *balko "beam" (Watkins *bhelg‑, the "different roots" Nourai's own note points to).

Notable confirmations: #15/#16 خندق — Asbaghi p. 113 gives Nourai's arrow verbatim (Ar. ḫandaq ← pers. kanda / MP kandag ← Av./OP kan‑), Mo'in marks Persian خندق «معرَّب»; #7 کَنَند is exact down to the Khojasteh verse; #3's five extra words (کندوله، کندوج، کندو، کندره، کندور) all sit on Borhan p. 1707, the same page as Mo'in's کندن footnote (Nourai's BQT:1707).

Extraction errors for the owner: **none** — the JSON matches the printed page (image saved to `data/verification/sources/refs/ocr/BOOK/213.png`). One cosmetic point: node #9's `script_extra` merges the two script blocks that the page prints separately under xâneh (خان، خَن، گلخن / خانگاه، خانقاه) and under ğâneh (ـ غان، دامغان).

Unreachable references: ZMA:49/51 (purchase‑only), FVF:593 (login‑walled), PRT:260 (lending‑only), and BQT for خانه (vol. 2 OCR unusable, no page cited).
