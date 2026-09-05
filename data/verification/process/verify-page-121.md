# Verification process log — verify-page-121


## [2026-09-05T18:10:10.725Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 121 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-121.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-121.json. Write /home/sfmqrb/git/rishe/data/verification/page-121.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 121` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T18:10:12.169Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T18:10:12.879Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T18:10:12.895Z] TOOL RESULT

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


## [2026-09-05T18:10:13.198Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-121.txt"
}
```


### [2026-09-05T18:10:13.219Z] TOOL RESULT

```
1	=== PDF page 121 (book page 91) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Deru 1 : wood, tree, to be firm  (refs POK:214)
4	#1 (parent #0) [Avestan] refs=POK:214; KLN:1644; SNS:318; ETM:65 | dru, dâuru, derežda, draxta : tree, wood ; dârug : medicine from plants
5	  #2 (parent #1) [Persian] refs=BQT:809,843; HRN:116; FVF:256; ETM:65; FSF:177 | dorŭd 1 «دُرود ۱» : wood ; dorŭdgar, dorga «دُرودگَر ( دُرگَر )» : wood worker, carpenter ; dâr 2 «دار ۲» : wood ; dârkŭb «دارکوب» : woodpecker ; deraxt «درخت» : tree ; dârŭ «دارو» : medicine | extra: داروخانه | NOTE: See "Dher 1" for another possible root of "dârŭ:medicine".
6	    #3 (parent #2) [Persian] refs=FVF:256 | dârîyeh «داریه» : a wood frame, a tambourine with wood rim
7	      #4 (parent #3) [Arabic] refs=FVF:256 | daf : tambourine
8	        #5 (parent #4) [Persian] refs=BQT:869 | daf «دَف» : tambourine ; šandaf «شَندف» : domestic tambourine ☞Gwhen 1 | NOTE: See "Dup" for another possible root
9	#6 (parent #0) [Avestan] refs=POK:214; ETM:65 | drva : healthy, sound ; upa-drava : to good health, good-bye ☞Upo ; drva-asti : healthy body ; druw-išta : healthiest ☞Isto
10	  #7 (parent #6) [Persian] refs=POK:214,216; BQT:840,842,843 | dorŭd 2 «دُرود ۲» : greetings ; bedrŭd «بدرود» : goodbye ; dorost «درست» : healthy, right
11	#8 (parent #0) [Old Persian] refs=KNT:190 | dâru : wood ; asâ-dâru : stone wood, hard wood, ebony ☞Ak
12	  #9 (parent #8) [None] refs=None | 
13	#10 (parent #0) [Sanskrit] refs=POK:214 | druna : made of wood
14	  #11 (parent #10) [Persian] refs=BQT:854; HRN:124; FRS:217 | darŭneh «درونه» : bow, rainbow
15	#12 (parent #0) [Greek] refs=IEC:161 | drŭs : oak ; ěn-druon : yoke peg
16	#13 (parent #0) [Germanic] refs=AHD | 
17	  #14 (parent #13) [English] refs=None | tree, true, tray, truth, trust, trim
18	#15 (parent #0) [Latin] refs=AHD | durus : hard, long lasting
19	  #16 (parent #15) [English] refs=None | duration
20	
```


## [2026-09-05T18:10:16.270Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-121.json | head -200",
 "description": "Read source JSON for page 121"
}
```


### [2026-09-05T18:10:16.311Z] TOOL RESULT

```
{
  "pdf_page": 121,
  "book_page": 91,
  "entries": [
    {
      "root": {
        "name": "Deru 1",
        "lang": "Indo-European",
        "refs": "POK:214",
        "gloss": "wood, tree, to be firm"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:214; KLN:1644; SNS:318; ETM:65",
          "words": [
            {"translit": "dru, dâuru, derežda, draxta", "gloss": "tree, wood", "script": null},
            {"translit": "dârug", "gloss": "medicine from plants", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:809,843; HRN:116; FVF:256; ETM:65; FSF:177",
          "words": [
            {"translit": "dorŭd 1", "gloss": "wood", "script": "دُرود ۱"},
            {"translit": "dorŭdgar, dorga", "gloss": "wood worker, carpenter", "script": "دُرودگَر ( دُرگَر )"},
            {"translit": "dâr 2", "gloss": "wood", "script": "دار ۲"},
            {"translit": "dârkŭb", "gloss": "woodpecker", "script": "دارکوب"},
            {"translit": "deraxt", "gloss": "tree", "script": "درخت"},
            {"translit": "dârŭ", "gloss": "medicine", "script": "دارو"}
          ],
          "script_extra": "داروخانه",
          "note": "See \"Dher 1\" for another possible root of \"dârŭ:medicine\".",
          "quote": {
            "text": "بفرمود تا دُرگَران آورند - سزاوار چوب گران آورند",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FVF:256",
          "words": [
            {"translit": "dârîyeh", "gloss": "a wood frame, a tambourine with wood rim", "script": "داریه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Arabic",
          "refs": "FVF:256",
          "words": [
            {"translit": "daf", "gloss": "tambourine", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "BQT:869",
          "words": [
            {"translit": "daf", "gloss": "tambourine", "script": "دَف"},
            {"translit": "šandaf", "gloss": "domestic tambourine", "script": "شَندف", "see": ["Gwhen 1"]}
          ],
          "script_extra": null,
          "note": "See \"Dup\" for another possible root",
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:214; ETM:65",
          "words": [
            {"translit": "drva", "gloss": "healthy, sound", "script": null},
            {"translit": "upa-drava", "gloss": "to good health, good-bye", "script": null, "see": ["Upo"]},
            {"translit": "drva-asti", "gloss": "healthy body", "script": null},
            {"translit": "druw-išta", "gloss": "healthiest", "script": null, "see": ["Isto"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "POK:214,216; BQT:840,842,843",
          "words": [
            {"translit": "dorŭd 2", "gloss": "greetings", "script": "دُرود ۲"},
            {"translit": "bedrŭd", "gloss": "goodbye", "script": "بدرود"},
            {"translit": "dorost", "gloss": "healthy, right", "script": "درست"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:190",
          "words": [
            {"translit": "dâru", "gloss": "wood", "script": null},
            {"translit": "asâ-dâru", "gloss": "stone wood, hard wood, ebony", "script": null, "see": ["Ak"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:214",
          "words": [
            {"translit": "druna", "gloss": "made of wood", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "Persian",
          "refs": "BQT:854; HRN:124; FRS:217",
          "words": [
            {"translit": "darŭneh", "gloss": "bow, rainbow", "script": "درونه"}
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "سرو بودیم چند گاه بلند - کوز گشتیم و چون درونه شدیم",
            "poet": "Kasâî"
          }
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "IEC:161",
          "words": [
            {"translit": "drŭs", "gloss": "oak", "script": null},
            {"translit": "ěn-druon", "gloss": "yoke peg", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
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
            {"translit": "tree, true, tray, truth, trust, trim", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
```


## [2026-09-05T18:10:16.932Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T18:10:16.969Z] TOOL RESULT

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


## [2026-09-05T18:10:20.138Z] TOOL CALL #5: Bash

```json
{
 "command": "sed -n '195,260p' data/extracted/batch/page-121.json; echo ---; ls data/verification/ | head -50",
 "description": "Rest of JSON and list verification dir"
}
```


### [2026-09-05T18:10:20.193Z] TOOL RESULT

```
          "quote": null
        },
        {
          "id": 15,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "durus", "gloss": "hard, long lasting", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "duration", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
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
page-109.json
page-110.json
page-111.json
page-112.json
page-113.json
page-114.json
page-115.json
page-116.json
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
```


## [2026-09-05T18:10:22.624Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','SNS','ETM','BQT','HRN','FVF','FSF','KNT','FRS','IEC','AHD','WLD','BRT','PHD','NYB','HUB','MON','ARY','SYN','SKT','CHEUNG']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Inspect refs_online for relevant abbreviations"
}
```


### [2026-09-05T18:10:24.437Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

FVF {"title": "S.M.A. Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi, Anjoman-e Asar-e Melli 58, Tehran 1347/1968", "kind": "website", "url": "https://noorlib.ir/book/info/105056 (page viewer: https://noorlib.ir/book/view/105056?pageNumber=<N>&viewType=pdf) ; https://ketabnak.com/book/48613 (818 pp. PDF, login) ; http://parsianjoman.org/?p=1265 (download post)", "lookup_hint": "Alphabetical by Persian headword; noorlib page number N is the scan page — browser needed to read. Not on archive.org.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "PDF exists 

FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offs

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

CHEUNG null
```


## [2026-09-05T18:11:08.601Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==222||NR==223 {print \"=== leaf \"NR\" ===\"; print}' POK_01.txt | head -150",
 "description": "Print Pokorny page 214"
}
```


## [2026-09-05T18:11:09.519Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"deru-\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD for deru"
}
```


### [2026-09-05T18:11:10.210Z] TOOL RESULT

```
=== leaf 222 ===
us  nehmen'),  öech.  drkati  , stoßen, holpern*,  bulg.  dircam,  dHcm  , ziehe,  riffle  Flachs,  Hanf  (Berneker  255, Persson  Beitr.  85,  359).
deres- :
Arm.  terem  (s.  oben  unter  der-)]
mir.  dorr  ,Zorn',  dorrach  ,rauh,  grob'  (s.  Persson  Beitr.  779  Anm.  1);
vermutlich  ags.  teors,  ahd.  zers  ,penis',  norw.  ters  , Nagel';  auch  anord. tjasna  f.  ,Art  Nagel'  aus  *tersnö7i'?,  norw.  trase  .Lappen,  Lumpen*,  trasast , zerfasert  werden',  tras  , Reisig',  trask  , Abfall,  Plunder';
sloven.  drdsati  , auf  lösen,  trennen*,  cech.  drdsati  , kratzen,  ritzen,  streifen*, drasta,  drdsta  , Splitter,  Fetzen;  Gewand',  draslavy  ,rauh,  holprig',  tief- stufig drsen  ,rauh',  drsnaty  ,holprig'  (vgl.  oben  mir.  dorr).
dre-sk:
lit.  su-dryskii,  -driskaü,  -driksti  ,zerreißen',  dreskiü,  dreskiau^  -dreksti , reißen',  draskaü,  draskyti  iter.  ,zerreißen',  lett.  draskät  ds.,  draska , Lumpen',  lit.  drekstlne  lentä  ,gerissene  Latte,  dünn  gespaltenes  Holz' (Leskien  Abi.  325,  Berneker  220,  224).
bulg.  drdskam,  drd.H^  (*drascg)  ,kratze,  scharre;  liege  an,  sorge  um', perfektiv  drdsm  (^draskng);  draska  , Kratzer,  Riß*;  cech.  alt  z-dfies- kati  und  (mit  Assimilation  des  Auslauts  an  den  tönenden  kn\B.\it)  z-dfiez-
211
.    .•    zerbrechen',    df-ieska,   dfiezha  , Splitter,  Span',    heute  drizha    ,Span*; ^oxJdrzazga  ,SpHtter';
^,{\t  formantischem  -p-:
drep-,  drop'i
A».  drapi-h  m.  ,Mantel,  Kleid',  drapsd-h  m.  , Banner  (?)*  (=  av.  drafsa-
F-ihne,    Banner'),    Ht.    dräpanos    f.  PI.    ,Weißzeug,    Kleider',    lett.    dräna
}\vohl    *dräp-na)    ,Zeug',    Tuch';    gallorom.    drappus    ,Tuch'   (PN  Drappö,
Dnippus,  Drajppes,  Drapönus)    ist   wohl   ven.-ill.   Lw. ;    der    a-Vokal    aus
iJcr.  0  oder,  wie  das  -pp-,  expressiv;
cry.  öoSTtu)  ,breche  ab,  schneide  ab,  pflücke',  dqeTtdvrj,  ÖQSTtavov  , Sichel', auch  ÖQdnavov  (daraus  alb.  drapen  ds.),  das  durch  Assimilation  von dgsTtavrj  zu  *ÖQa7tdvr]  zu  erklären  ist;  o-stufig  Sqcütivcü'  diaxÖTtTw  Hes. (=r  serb.  dräpljem),  ÖQCjjia^,  -y,og  , Pechpflaster,  um  Haare  auszuziehen*, Soiorta%it,o)  , reiße  Haare  aus';  anord.  trqf  n.  PI.  ,Fransen',  trefr  f.  PL  ds., ti-eßa  ,zerfasern',  mhd.  trabe  f.  , Franse';
*dröp-  in  russ.  drjdpa-ju,  -th  (mit  unklarem  ja),  dial.  drdpatb,  drapdh kratzen,  reißen',  serb.  dräpam,  dräpljem,  drdpati  , zerreißen,  abnutzen; kratzen',  poln.  drapac  ,kratzen,  schaben,  reiben,  fliehen';
dj-p-,  slav.  "^dwp-  in  bulg-.  dirpam,  perfektiv  dripm  , reiße,  ziehe, schleppe';  serb.  drpäm^  drjpati  und  drplm,  drpiti  , reißen';
bsl.  dreh-,  drob-  , Fetzen,  Kleider'  in  lett.  drebe  f.  ,Zeug,  Kleid,  Wäsche', lit.  drohe  f.  , Leinwand',  dräbanas  m.  ,Lumpen,  Fetzen',  drahüzis,  drohü^is m.  , Kleid';  osorb.  drahy  m.  PL  , Kleiderzeug',  öech.-mähr.  zdraby  m.  PI. ,Lumpen,  Fetzen'  haben  wohl  durch  Einfluß  der  Wz.  *  droh-  (s.  unter dhrehh-)  , zerschneiden,  zerstückeln'  -b-  statt  -p-]
drip- :
Gall.  (ven.-ilL)  PN  Drippia,  Dripp
=== leaf 223 ===
önius  (vgl.  oben  Drappus  usw.);
bulg.  dripa  , Lappen,  Fetzen',  sloven.  dripam  (dripljem),  dripati , zerreißen, Durchfall  haben',  cech.  dripa  , Fetzen',  dripati  , reißen,  zerreißen';
drup- :
Gr.  ÖQVftTO)  , zerkratze',  drroÖQVTiTcOy  -dgvcpa)  (mit  sekundärem  q)  statt  7t, s.  Persson  Beitr.  859)  ,kratze  ab,  schinde  die  Haut  ab',  ÖQvcpi^  ,das  Zer- kratzen, Abstreifen',  dQVTclg  ,eine  Dornenart'.
Zum  Wechsel  von  a:i  :u  in  ,mots  populaires'  vgl.  Wissmann  Nomina postverbalia  162  ff.
WP.  I  797  ff.,  WH.  I  342 f.,  373,  861,  Trautmann  51  f.
derbh'   , winden,    zusammendrehen',    dorbhö-s    , Zusammengedrehtes,    Gras- büschel, Rasen'. Ai.  dibhdti  , verknüpft,  flickt  zusammen,  windet',  Partiz.  sdndxhdha-  ,z\i- sammengebüschelt',    drhdhi-    f.    , Windung,    Verkettung',    av.    ddrdwda-    n.
14*
212
,Muskelbündel',    PL    ,MuskelfleischS    ai.   darhhä-    m.    ,Grasbüscliel,    Gra darbhana-  n.  , Geflecht';
arm.  torn  .axoivlov,  funiculus,  laqueus*  (*dorhh-n-)]
gT.   öaQTtT]   ,Korb'   ist  aus  ^dagcpr]  und  TaQTtrj  ds.  kontaminiert  (Günte IF.  45,  347);
ags.  tearflian  (*tarbalön)  ,sich  rollen*,  ahd.  zerhen,  prät.  zarpta  rej ,sich  drehen,  sich  umdrehen';  e-stufig  mhd.  zirben  schw.  V.  ,sich  im  Kreise drehen,  wirbeln',  nhd.  mdartl.  Schweiz,  zirbehi  ds.,  nhd.  Zirbeldrüse Zirbelwind  (wohl  auch  Zirbel  ,pinus  cembra',  s.  unter  deru-)]  schwach- stufig-  ags.  torfian  , werfen,  steinigen'  (vgl.  drehen  :  engl,  tlirow),  wie  anord. tyrfa  ,mit  Rasen  bedecken',  anord.  torf  n.  ,Torf',  torfa  f.  , Torf  schölle ags.  turf  f.  ,Torf,  Rasen',  ahd.  z'urba,  zurf  f.  , Rasen'  (nhd.  Torf  aus  de; Ndd.);  ags.  ge-tyrfan  ,to  strike,  afflict';
wruss.  dörob  ,Korb,  Schachtel',  russ.  alt  u-dorobb  f.  ,Topf',  dial.  ü-dor^ , schlechter  Topf  (,*mit  Lehm  bestrichener  Flecht werktopf'),  wrusg^ <Zoro6'/c  , krümmen,  biegen';  schwachstufig  *cZb?*6a  in  ymss.  derbd  ,Rodeland Neubruch*,  derbovdth  ,vom  Moos,  vom  Rasen  säubern;  den  Anwuchs  aus- roden', derbith  , rupfen,  zupfen,  raufen',  serb.  drbdcati  , kratzen,  scharren' cech.  drbdm  und  drbu,  drbati  , kratzen,  reiben;  prügeln',  mit  Hochstufe russ.  derebith  , zupfen,  reißen'  (vielleicht  hat  sich  in  letztere  Sippe  eine ÖÄ-Erw.  von  der-  , schinden',  släv.  dero  dwati  eingemischt).  S.  Bernekelr 211,  254  mit  Lit.
WF.  I  808.
der{ep)-  , sehen'?
Ai.  ddrjmna-   m.  , Spiegel';   gT.  dgcoTtduLv,   öqcütctsiv   , sehen'   (mit  Dehn- stufe der  2.  Silbe??).  Vgl.  auch  dodcüj  ,sehe'  und  de^-k-  ,sehen'. WP.  I  803;  zum  Formans  -ep-  vgl.  Kuiper  Nasalpräs.  60  f.
dero-,  drä'  ,arbeiten'.
Gr.  dqdü}  (*dQCcicü)  , mache,  tue^  Konj.  dgöj,  äol.  3.  PL  ÖQälGi,  Aor.  att. edqaaa,  hom.  öoTjaTrjQ  , Arbeiter,  Diener',  ÖQäfia  , Handlung',  dodvog-  egyov, ngä^ig  .  .  .  övraf-ug  Hes.,  dÖQavi^g  , untätig,  unwirksam,  schwach',  hom. �
```


### [2026-09-05T18:11:10.261Z] TOOL RESULT

```
369:*dru-ko- in Germanic *trugaz in Old English trog, wooden vessel, tray: TROUGH. 5. Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM. 6. Variant form *derw- in Germanic *terw- in Old Eng- lish fe(o)ru, resin, pitch (obtained from the pine tree): TAR}. 7. Suffixed variant form *dri-ro- in Latin diirus, hard (of whose English derivatives many represent a semantic cross with Latin dirdre, to last long; see deue-): DOUR, DURAMEN, DURESS, DURUM; (DURA MA- TER), ENDURE, INDURATE, OBDURATE. 8. Lengthened zero-grade form *dré- in Greek drus, oak: DRUPE, DRYAD; GERMANDER, HAMADRYAD. 9. Reduplicated form *der-drew-, dissimilated with suffix in *den-drew- on in Greek dendron, tree: DENDRO-, DENDRON; PHILO- DENDRON, RHODODENDRON. 10. Celtic compound *dru-wid-, “knower of trees” (*wid-, to know; see weid-), the Celtic priestly caste, associated with a tree-cult, probable source of Latin druides, druids: DRUID. 11. O-grade form *doru- in Sanskrit daru, wood, timber: DEODAR. [Pok. deru- 214.]
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
```


## [2026-09-05T18:11:15.664Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=225 && NR<=226 {print \"=== leaf \"NR\" ===\"; print}' POK_01.txt | head -80",
 "description": "Print Pokorny leaf 225"
}
```


## [2026-09-05T18:11:16.381Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '368,369p' AHD_watkins1985.txt | cut -c1-3000",
 "description": "AHD deru entry context"
}
```


### [2026-09-05T18:11:17.501Z] TOOL RESULT

```
=== leaf 225 ===
N  Torget,  Torghatten  usw.,  idg.  ^o-Suffix  in  germ. *iurhta-  :  ags.    torht,   as.    toroht,   ahd.   zoraht,  jünger  zorft   .hell,  deutlich*.
WP.  I  806  f.
Vielleicht  mit  derep-  (oben  S.  212)  entfernt  verw^andt.
"I
214  •
dera-,  doru-,  dr{e)u-,  drou-]  dreug  :  drü-  ,Baum',  wahrscheinlicli  urspr, und  eigentlich  , Eiche',  siehe  zur  genauem  BegTiffshestimmang  Osthoj Par.  I  169 f.,  Hoops  Waldb.  117 f.;  dazu  Worte  für  verschiedene  Hol gerate  sowie  für  , kernholzartig  hart,  fest,  treu';  Specht  (KZ.  65,  198j 66,    58  f.)    geht    jedoch    von    einem    substantivierten    Neutrum    einj Adjektivs    *döru    ,das  Harte'    aus,    woraus    erst    ,Baum'   und  ,Eicbe»^ dbru    n..    Gen.    dreu-s,    dru-nö-s]    Ableitungen:     deruo-,    dreu^ drU'Znö'S,  dru-nö-s,  druu-ö-s,  drü-tö-s. Ai.    däru   n.    ,Holz^    (Gen.    dröhj    drünah,    Instr.    drünä,    Lok.    därui^xi dravya-  ,vom  Baum'),   di-d-   n.  m.  ,Holz,   Holzgorät',   m.-^Baum,  Ast^  a? däuru  ^Baumstamm,  Holzstück,  Waffe  aus  Holz,  etwa  Keule'  (Gen.  draol ai.  därund-  ,hart,   rauh,  streng'  (eigentlich  ,hart  wie  Holz,   klotzig'),  drS in  Kompositis  wie  dru-päda-  ,klotzfüßig',  dvu-ghni  ,Holzaxt-  (-schlägerinf su-dini-h  ,gutes  Holz';  dhruvd-  ,fest,  bleibend'  (dh-  durch  volksetym.  Anschla|^ an   dhar-   ,halten,    stützen'  =  av.    dr{u)vö,    apers.    duruva    ,gesund,  heil* vgl.  aksl.  s^•d7^av^)]  av.  drvaena-  ,hölzern',  ai.  druvdya-h  ,hölzernes  Gefä(§ Holzkasten    der   Trommel',    drAna-m    ,Bogen,    Schwert'   (unbelegt;    mit npers.   durüna,   baluci   drin  ,Regenbogen'),   drunl  ,Wassereimer'^   drö-  a^ ,hölzerner  Trog,  Kufe';  drumd-h  ,Baum'  (vgl.  unten  dQV^Log)] ai.  ddrvv-hy  darvi  ,(bölzerner)  Löffel';
arm.  tram  ,fest'  {^^di^rämo,  Pedersen  KZ.  40,  208);  wohl  auch  (Liden Arm.  St.  66)  targal  ,Löffel'  aus  *dru-  oder  *deni-.
Gr.  SÖQv  , Baumstamm,  Holz,  Speer'  (Gen.  honi.  Sovgög,  trag.  doQÖg  aus *doQf6g,  öovgarog,  att.  dögazog  aus  *SoQj^nTog^  dessen  n  mit  ai.  drünah vergleichbar  ist);
kret.  doga  (*doQj^a)  ,Balken'  (=  lit.  lett.  darva)]
sizil.  äa%edo}qog  ,Eber'  (nach  Kretschmer  KZ.  36,  267  f.  '^dv-a%s-doQj^og oder  -dwgJ^og  ,dem  Speere  standhaltend'),  ark.  dor.  JwQL-y.X^gj  dor.  böot. Ja}Qi-f,iaxog  u.  dgl.,  JcoQisvg  ,Dorer'  (von  Jcogig  ,Waldland');  dgvg,  dgvög , Eiche,  Baum'  (aus  dem  n.  *c??nt  oder  *dervj  *doru  g.  "^druuös  nach  andern Baumnamen  zum  Fem.  geworden;  infolge  der  Einsilbigkeit  Nominativ- dehnung), dycgö-dgva  , Fruchtbäume',  dgv-iöfiog  , Holzhacker',  dgvLvog  ,von der  Eiche,  von  Eichenholz',  Jgvag
=== leaf 226 ===
  ,Baumnymphe',  ysgdvögvov  ,alter  Baum- stamm', ädgva '  Ttlola  ^ovö^vXa '  KvngLoi  Hes.  (*6'^-,  Lit.  bei  Boisacq  s.  v.), evögvov  xagöia  divögov  Hes.
Hom.  ögvjxd  n.  PL  ,Wald',  nachhom.  ögv(j,ög  ds.  (letzteres  mit  erst  nach  ^^. dgvg  geneuerter  Länge);  öivdgeov  ,Baum'  (Hom.;  daraus  att.  öhögov),  aus  ,;?; rednipl.  *Ö6v (=  Ssgyögeßovj  Demin.  ösvögvcpiov]  vgl.  Schwyzer  Gr.  Or.  I  583;
dgof-  in  arg.  ögoöv  ia^vgov.   ^AgyeiOL  Hes.,  evögoia'  xagSia  öevdgov  ycai  ^ TÖ  iieaov  Hes.,  Jgovd-og  {^'JgoJ^-vd'og),  ögoLTrj  , hölzerne  Wanne,  Trog,  Sarg     j, (wohl  aus  *dgofiTa,  vgl.  zuletzt  Schwyzer  KZ.  62,  199  ff.,  anders  Specht  ^
:l:i
215
pekl.  139);  öoTcqov  uveIov  Gxdq^rjv  Hes.  (diss.  aus  ^öqoJ^ltooi'),  woneben *  Inno-  in  dgcciöv  f^iäycrgay.  nvslov  Hes.
pK  jQvrcüy-Ait.  Drüktems,  apr.  Drutenne  (E.  Fraenkel,  Pauly-Wissowa IG;  1633);
im  Yokalismus  noch  nicht  sicher  erklärt  ÖQioq  , Gebüsch^  Dickicht'; niaked.  d&ovllog  f.  ,Eiche^  Hes.  (*Jerw-,  vg-1.  air.  dcniy-)]  aber  öoiq'  Svva^ig Hes.,  lies  dflg  (Schwyzer  Gr.  Gr.  I  495  0);
alb.  dru  f.  ,Holz^  Baum,  Stange'  {^druuä,  vgl.  aksl.  drzva  n.  pl.  _,Ho]z'j; drush-k  (es-St.),, Eiche';  ablaut.   *drü-  in  dri-ze  ^Baum^  drüni  ^Holzriegel';
thrak.  y.ala^iv-daQ  , Platane',  ON  JaQavdog,  TägavTog  (*dar-ant-)  ,Eich- stätt';  Zirögoufia,  Jivdgvfir]  ,Zeushain',  VN  '0-dgv-a-ai,  Jgdooi,  Drii-geri (dru-  ,Wald');
aus  dem  Lat.  vielleicht  durus  ,hart;  abgehärtet,  kräftig;  derb,  roh,  rauh, streng;  gefühllos'  (aber  über  düräre  ,ausdauern,  dauern'  s.  unten  S.  220), wenn  nach  Osthoff  Ulf.  als  ,baum3tark,  fest  wie  (Eichen) holz'  dissimiliert aus  *drü-ro-s  (*dreu-ro-s?)',
über  daß  lat.  lai-lx  , Lärchenbaum',  Lw.  aus  einer  idg.  Alpensprache, ido-.  "^derik-s  sei,  ist  wegen  des  l  schwer  denkbar;
air.  derucc  (gg),  Gen.  dercon  ,glans',  cymr.  derwen  , Eiche'  (PI.  derw), bret.  deruenn  ds.,  gall.  Ortsname  Dervus  (, Eichenwald'),  abrit.  Derventiö, Ortsname,  VN  Derväci  u.  dgl.;  air.  derh  ,sicher';  reduktionsstufig  air. daur,  Gen.  daro  ,Eiche'  (devu-),  auch  dair,  Gen.  darach  ds.  {*d^ri-)j  air. daurde  und  dairde  , eichen';  abgeleitet  gall.  *d{a)rullia  , Eiche'  (Wart- burg ni  50);  maked.  ödgvXkog  f.  , Eiche';  schwundstufig  *dru-  im  Ver- stärkungswörtchen  (?  anders  Thurneysen  ZcPh.  16,  277:  ,Eichen-':  dru- ia  galat.  dgv-vaipLSTOv  ,heiliger  Eichenhain'),  z.  B.  gall.  Dru-talos  (,*mit großer  Stirn'),  Druides,  Druidae  PL,  air.  drüi  ,  Druide'  (,der  hoch  weise', *dru-uid-)j  air.  dron  ,fest'  (*drunos,  vgl.  ai.  di'u-na-nij  däru-nd-,  drö-na-m), mit  Gutturalerweiterung  (vgL  unten  nhd.  Trog)  mir.  drochta  ,(*hölzernes) Faß,  Tonne,  Kufe',  drochat  ,Brücke';  hierher  auch  gallorom.  drütos , kräftig,  üppig  (:  lit.  drütas)\  gr.  PN  JgvTCJV,  air.  drüth  ,närrisch'  (:  aisl. trädr  , Gaukler'?),  cymr.  drud  ,närrisch,  tapfer'  (das  cymr.  ?fc  stammt  aus den  roman.  Entsprechu
```


### [2026-09-05T18:11:17.557Z] TOOL RESULT

```
dhabh-
*dru-ko- in Germanic *trugaz in Old English trog, wooden vessel, tray: TROUGH. 5. Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM. 6. Variant form *derw- in Germanic *terw- in Old Eng- lish fe(o)ru, resin, pitch (obtained from the pine tree): TAR}. 7. Suffixed variant form *dri-ro- in Latin diirus, hard (of whose English derivatives many represent a semantic cross with Latin dirdre, to last long; see deue-): DOUR, DURAMEN, DURESS, DURUM; (DURA MA- TER), ENDURE, INDURATE, OBDURATE. 8. Lengthened zero-grade form *dré- in Greek drus, oak: DRUPE, DRYAD; GERMANDER, HAMADRYAD. 9. Reduplicated form *der-drew-, dissimilated with suffix in *den-drew- on in Greek dendron, tree: DENDRO-, DENDRON; PHILO- DENDRON, RHODODENDRON. 10. Celtic compound *dru-wid-, “knower of trees” (*wid-, to know; see weid-), the Celtic priestly caste, associated with a tree-cult, probable source of Latin druides, druids: DRUID. 11. O-grade form *doru- in Sanskrit daru, wood, timber: DEODAR. [Pok. deru- 214.]
```


## [2026-09-05T18:11:31.271Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '367,368p' AHD_watkins1985.txt | tail -c 2500; echo; echo \"=== POK 216 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==227 {print}' POK_01.txt | head -60",
 "description": "AHD deru entry start and POK p216"
}
```


### [2026-09-05T18:11:32.899Z] TOOL RESULT

```
12
dhabh-

=== POK 216 ===
ngen);
deim-  in  germ.  Tervingl,  Matrib{us)  AlaterviSj  anord.  tjara  {^detiiön-), finn.  Lw.  terva,  ags.  teoru  n.,  tierwe  f.,  -a  m.  ,Teer,  Harz'  (*deruio-),  mnd. tere  ,Teer'  (nhd.  Teer)]  anord.  tyrvi,  tyri  , Kienholz',  tyrr  , Föhre'  (un- sicher mhd.  zirwe,  zirhel  ,Pinus  Cembra',  da  vielleicht  eher  zu  mhd. Zirbel  ,  Wir  bei',  wegen  der  runden  Zapfen);
dreu-  in  got.  triu  n.  ,Holz,  Baum',  anord.  tre^  ags.  treow  (engl,  tree),  as. trlo  ,Baum,  Balken^;  in  übtr.  Bed.  ,fest  —  fest  vertrauend'  (wie  gr.  ioxvgog ,fest':  ia^vgi^ouai  , zeige  mich   fest,  verlasse   mich  worauf,  vertraue'),  got.
216
triggws  (*tremiaz)  ,treu^,  ahd.  gi-trluwi  ,U'eu%  an.  tryggr  ,tve\i,  zuve, lässig,  sorglos',  got.  triggioa  ,Bund,  Bündnis',  ags.  treow  , Glaube,  Treu, Wahrheit',  ahd.  triuwa,  nhd.  Treue,  vgl.  mit  ders.  Bed.,  aber  ande] Ablautstufen  anord.  trü  f.  , religiöser  Glaube,  Versicherung',  ags.  irui m.,  mnd.  trüioe  f.  ds.,  ahd.  trüwa,  aisl.  trü  f.,  neben  trür  ,treu';  abgeleit| anord.  trüa  ,trauen,  für  wahr  halten'  =  got.  trauan,  und  ags.  trüiüia: as.  trüön,  ahd.  trü{w)en  ,trauen'  (vgl.  n.  apr.  druiuis)]  ähnlich  atiorj traustr  ^stark,  fest',  traust  n.  , Zuversicht,  Vertrauen,  worauf  man  sie! verlassen  kann',  ahd.  tröst  , Vertrauen,  Trost'  {*droust-)j  got.  trausti  ,Vec! trag,  Bündnis',  ablautend  engl,  triist  , Vertrauen'  (mengl.  trüst),  mla trustis  ,Treue'  in  den  afränk.  Gesetzen,  mhd.  getrilste  ,Schar'  (die  s^Bildu ist  alt  wegen  npers.  duruU  ,hart,  stark',  durust  ,gesund,  ganz';  nor\^ trysja  ,den  Boden  säubern',  ags.  ti^üs  , Reisig',  engl,  trouse,  aisl.  tn , Abfälle',  got.  ufar-trusnjan  , überstreuen'.
"^drou-   in    ags.    trlg,    engl,    tray  ,flacher  Trog,    Schüssel',    aschwed ,ein  bestimmtes  Maßgefäß'  {^trauja-,  vgl.  oben  ÖQoixri),  anord.  treyju-sqdvX (auch  tryju-sgdoll)  ,eine  Art  trogförmiger  Sattel';
*drü-m  aisl.  trüdr  ,Gaukler',  ags.  ^rücT, Spaßmacher,  Trompeter'  (:  gallorom *drüto-s,  usw.)?^
*drU'  in  ags.  trum  ,fest,  kräftig,  gesund'  (*dru-mo-s),  mit  ^-Erweiterung bzw.  Formans  -ko-  (vgl.  oben  mir.  droclita,  drochat),  ahd.  nhd.  trog,  ags. trog,  troll  (m.),  anord.  trog  (n.)  ,Trog'  und  ahd.  triLha  , Truhe',  norw. mdartl.  trygje  n.  ^eine  Art  Saum-  oder  Packsattel',  trygja  ,eine  Art Fischkorb',  ahd.  trucka  ,Kiste',  nd.  trügge  ,Trog'  und  mit  der  ursprüng- licheren Bed.  ,Baum,  Holz'  ahd.  hart-irugil  , Hartriegel';
bsl.  *derua-  n.  ,Baum'  in  aksl.  drevo  (Gen.  dräva,  auch  dr^vese),  skr. dial.  drevo  (dnjevo),  sloven.  drevo,  aöech.  dfevo,  r
```


## [2026-09-05T18:11:33.047Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"endruon\\|ěn-druon\\| endruo\\|ἔνδρυον\" IEC.txt | head; echo \"---drus---\"; grep -n \"drus, oak\\|drūs\\|drus \" IEC.txt | head -20",
 "description": "Grep Mann IEC for endruon"
}
```


### [2026-09-05T18:11:33.119Z] TOOL RESULT

```
---drus---
2103:dederuos, dedrus ‘tetter, eczema, ringworm’. WP I, 800. Cf. der- Skt. dadrüh: Dacian (?) in LLat. *dzeruae (spelt zernae); GalloLat. cf. derb-itae (> Fr. dartres); Mir Ir. deir; Br. cf. derv-oed; OHG zetar-och; G Zitter-och ‘warts’, OE teter *tetters'; Icel. cf. tetur (^wretch', fig. usage); Li. cf. dederv-ine
2113:dederuos, dedrus — deKor- (deKos)
2483:dru- (radical) ‘timber, tree’. Cf. druu-, dru- to-, etc. WP I, 804 Skt. dru; Av. dru ‘timber; spear’; Gk. drüs *oak'; Alb. dru, gs. druje & drü, gs drüni “timber, tree’; cf. Gk. én-druon *yokepeg"; dráos ‘woodland’ (*druuo-); Li. cf. sü-drus ‘stout, solid’. (Myc. has dru-, duru- in various cpds.) |
2505:drus-, drusos (2) “firm, solid”. Cf. dru-, drsus, druos, drutos, etc. Gaul. drusus “firm, boid’; LW in Fr. dru; (LG tros ‘proud, defiant reflects, like Du. trots, an obscure G Trotz, MHG trutz, trotz, s. but the radical *dru- is common to all forms); Li. cf. sü-drus 'solid'
3163:dhrusəlos (dhrusil-, dhruslo-) “broken down, puny; fragments, rubble’. Cf. dhrul-, dhrislio- & WP I, 872, and see next Gk. *thrülos (2) in thrülisso “break up, crumble’ beside thrüallon ‘shower of smuts’; Ir. cf. drollaire ‘idler’; ON drysil- (in cpds. "small", (Radical in Go. drus ‘fal’ and OE drüsian ‘to hang limp’: E to drowse. Cf. also Li. druskà ‘salt’; Latv. druska *fragment")
17792:su-dros, -drus “firm; firmess'. Cf. su- (2), druo-, deru- Vedic su-drüh, m. ‘good timber’; Ir. sodaire, m. ‘bulky animal": Li. südrüs “proud, splen- did”. WP I, 806
```


## [2026-09-05T18:11:42.861Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\ntxt=open('IEC.txt',encoding='utf-8',errors='replace').read()\nlines=txt.split('\\n')\n# find line 2483 offset\noff=sum(len(l)+1 for l in lines[:2482])\nleaf=txt[:off].count('\\f')\nprint('leaf(0-based)',leaf, 'printed page approx', (leaf-15)*2)\nEOF",
 "description": "Find IEC leaf for dru- entry"
}
```


### [2026-09-05T18:11:44.364Z] TOOL RESULT

```
leaf(0-based) 102 printed page approx 174
```


## [2026-09-05T18:11:45.225Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT dāuru/dru ===\"; grep -n \"dāuru\\|dauru\\|drvaēna\\|drvaena\" BRT.txt | head -20\necho \"=== BRT drva ===\"; grep -n \"drva-\\|druua\\|drvō\\|drvatāt\\|drvatat\" BRT.txt | head -30",
 "description": "Grep Bartholomae"
}
```


### [2026-09-05T18:11:45.298Z] TOOL RESULT

```
=== BRT dāuru/dru ===
3539:•  j.  apa.dis-  Adj.  —  ?  — :  ar>zS.saman>m ,  .  °s>ni  ny^idauru  YX.ig.\i.
6486:•  j.  aäti.masah-  Adj.  'von  der  Grösse einer  A.':  äat  pitSus  ydi:a  cdijiciärS  'sS N.  (7^(?);  —  taltim  dauru  . . nyäzaym  (sd.) +°jj')  xraoidvaAe  bti'  altavatö  var>dvahe "ein  .  .  Stück  Holz  .  .  von  der  Grösse" einer  Ä.  aus  hartem,  doppelt  so  gross'' aus  weichem"  V.  13. 30.
7757:Pü.:  Tüsl  ml,  Sü.:  salyena  ladauruh.^  ■)  Vgl.
11761:surunvata  yasna  tarn  yjzäi  . .  arfdvJm YL5, 9;  /7.  3;  —  la  hasHt  upa.sbayeiU tqra.-fravalayS  Yt.ij.ög;  —  .Ja  nipa- yemi  vispa  vokü  Yt  5. 89;  —  harn  taät (NDm.)  bJeus  baratö ..  tistryasi'a ..  daFvasca .  .  la  (Sp.  615  m.)  yaitya^S  Yt.  S artikelhaft:  //{AD£)  aifam  paili  sruye(sä.) aZsa  druxs  upa.dvqsaiti'S ."j.  24'"';  — ya^a te  vTspe  aurvanta  zasvauha  (sd.)  paili. jasqnXX.  ^.\%t\  ;o.i2S;  —  ta  nS  data  tä (Sp.  6 1 5  u.)  fravaocäma  Y.  70.  2 ;  —  ava  Al baraytn  läshm  dauru{'si.)  upa  tqm  manao- ürTm  "sie  sollen  ihm  . .  am  Hals  anbringt V.  ij.  30;  —  minutn  barat  andvl  .,  upa tqm  srirqm  manao^rim'Vt. 5.  i2T. titn  urva^fm  /rayavaySiJ'(sä.)  sna^äi  Yt. 7.  24;  —  i^m  valmcit  yazamaide  "(ihn) den  f. , ."  Yl  75. 1 ;  i;  —  äal  t>m  varpm kfrsnava  V.  2.  25;  —  avavanOm  asa- vaynyäi  (sd.)  tqm  ä^qm  dagtayJ  V.  5. 14;  —  ä  tai  :^ami5  yasamaide  Vr.  ig.  a ; Ytö.iä;  —  nöit  kl  tä  vlsB  tilyul . . apaili.- buili  haca  vTiibyS  para.baraiti  (sd.)  V.  13. 40(?);  —  nava  äfs. .  navata  baiiacajipsa V.  21.  3  (?);  —  s.  noch  Yt.  10.  6,  i§.  49, V.p,  29;  s.  Sp.  616  o.  bb)  mit  rela- tivischem  Anschlüsse' ;  a)  im  gAiv.:  at  tSng dngva  ySng  asalefl  vazdrJng p,lt  gä fror»' f^{s6..)  Y.4Ö.4;  —  t3is  . .  yäis  daiäis  . . ^,46.  15.  B)imjAvr.:  tat  drvais..ta! . .  pairi.urvalstsm  yat  tamS  voku  Yt. //.  a; Y-jÄ  I';  —  ta  (NPn.)  ns  ama  ta"  . . uxjamyqn  yä  staota  yestiya  Y.  55.  3;  — ta  vanukJ?  tä  vahisth  yazamaide  ya  .  . fravasayö  Yt. y.  27;  —  tä  .  .  upastqm k^Ttti  dahiita  ya  fravasayS  Yt  13. 17;  76;
14223:•  j.  drvaena-  Adj.  (fem.  "«r-)  'aus  Holz, hölzern':  yezi  anhat  zannamil  (sd.)  .  . siinimii  'nis  (NSCl  V.  7.74^;  —  i^it astaliatibya  nsit  *'naä6ya'''  (näml.  Aava- naHbya)  ratu/rii  N.  soj.
19761:•  j.  'manaoSri-  £  'Hals,  Nacken',  uzw. a^anscher  Wesen'' :  "an"  F.  jg;  —  minum barat..ar3dvlsära..upa  tarn  srJrqm'^rim Yt5. 127;  —  ava  hl  (nämLjfi«J)  baraytn taihm  dauru  (sd.)  upa  tqm  «Srüw  V.7_j,30.
=== BRT drva ===
4115:FrW.  4.3;  —  'rahe  mainySus  dämanam ^'^  '5'  3i  —  y^t  titarat  °rS  matnyus dähim  alahe  .  .  antan  pairi.aväit^m  (sd.) fokuca  mattö  atarsca  /J  hg  taurvayatsm tba^ä  °rahe  mainySus  drvats  Yt  7_J,  7  7  f. ; 13;  — yint  nöit  tiurr/pttte  'rS  mainym nsit  yatavS  fairikssca  Vt  1^.44;  —  ailm dahakim..yqm..  drujim  fraca  k>rmlat  'rS mainyus  Y.(?.8;  —  aal  ahe  paityarim  frä- ijrMiat  'rö  mainyus . .V.l. 2;  'J0.3,Aog.2^; —  pairiAä  .  .  yä  uzdtihat  'rS  mainyuS  .  , paiHj>r)tSe  Yt,  A",  39;  —  taxm?m  urupi  .  . yat  barata  'tvm  mainyBm  framitim  (sd.) aspake  JaArpa  ^risatjm  aiwi.gämanam Vt./^.  29;  — paiti.psrme  'nm  mainyBm V, /o.  5;  —  fränämiliti  duhjarstavari'  °r3 mainyus  ax^amanS  Yt/p.  96;  3.^;  — naiHs  xsayät  °rö  mainyus  duzdalnS  FrW. 4.  a ;  —  xsnagiira  akurahe  mazdä  tarSidlti 'raAe  mainyius  Yt.  i.  o;  —  daxstanam  ydi Amli  'rahe  ntainySus  daxstim  V.  2.  29;  P, 2-2,  Y,  7i>,  11;  —  apayafUamah^a  'rahe mainyius  xrafstra  Yt.  21.1;  —  'rif  mainyus . .  dtävanam  daivS  V.  ig.\;  —  vJspB.mahr- käatca  pairi  drvatat  yat  -rst  mainyaot VL/_j.7i;  /0.118,  Y.2-j~-i,  V.'/o.ie;  — ai  duida  °ra  mainyS  V.ii).^;  g,  1,44,  lt. 10,  Yt//.  19; —  iaÖx  dusda  'ra  mainyö V.  i^,  1 2 ;  —  *'rahe ''  *mainy9us  duzdamanH Y.  Ö/.  2;  V. /p.6;  —  skutara  "ra  mainyö V.  79. 3;  —  "rS  mainyus  pouru.mahrkS (Stveri.)  Yt  10. 97 ;  usw.
6254:—  syao%ami  razistä  (sd.)  ängvataicä kyai<ä  *'iaotii  yehyäiä  ASmunylsaitl  (sd.) mi^aAyä  yucä  ksi  är»svä  Y.  _jj.  i ;  —  yS vü  xsayqs  adqs  drTtä  ayanhm  urvatsis (sd.)  Vit  huiSntul .  .  ra/nä  jvqs  yS  'savä dr3gvant)m  Y.  46.  5.  a)  Ko-i  it  von Zara^ustra  (s.  2  c  a  und  drTgvaiit- 1  2  a  a) : y!  äyal  •iavanam  divamnsm  (sd.)  hsi  . . *dusji^arä^Sm  (sd.)  . .  ISm  *vi  ahSm  dr>g- vants..dams  «a<tf«/(sd.)  Y.^7.20.  b)  im jAw.:  kat  *sava . .  vanai drvantami  'idva vanat  drußm  °sava  vanat  drvantpm  Yt. I.2S;  —  x^ayamnam  '/avanim  däyata *axsyamn^m  drvant^m  Y.  Ä  5  ;  —  vasB.- x/a'iirB  kyüi  'sava  avasS.xia'^rS  hyäf  drvä Y.S.6;  —  yqm  'lara  ..  asayqm  (sd.) va^  tarn  drva  ^ihva  Vr.  22.2;  —  mt^nm ms  janyh  mä  yim  drvatat  pimanke  mU yim  n^adafnat  'iaoiiat  uvayä  af  asti  (sd.) mskrB  drvataica  'saonai^a  Yt/o.  2;  — pdhqm  %rvB.däianqm  jasaiti  yasla  drvaile yas^a  '/aofieV.  lff.$o;  — yai  azäite^sd.) tsm  ahum  pai'iyaite  yim  "soonam  yesi  nHii azUiie  tun  aAam  pai^yäite  yim  drvatqm V.  /Ä76;  —  drvatqm  ..  urvänS ..'läunqm V.  ig.  30;  —  ga>il  nmätiam  ^mr^yS  asti '/SvaoyB  (DP.)  naSai  drvatqm  Yt,7.4;  — hiiia  para  'saonqm  pa^a  urva/ai/i  iu^a drvatqm  Yt4.4;  —  narqm  vä  'saonqm kanjamanäis  drvatqm  vä  . .  kandvaranäü YLi/,4; — yai  •i'ava  para.iriiyeiä  . . yal drvä  ava.*miryeie  H.2.1  — 19;  7,  8,  10, 15*,  16',  18  {'iaonyäi);  s.  unter  drvatif- 1 1.  2)  sonst,  a)  im  gAwr.  (ausser GHapt):  zara'^usträ  kastl  'lavä  urva^S mazsi  magäi  (sd.)  Y,  46. 14;  —  tSm  (näml. pounicistqm)  . ,  varänl  (sd.)  .  .  yä  försi vTdäl  paüyaFcä  västryaHbyo  (sd.) . .  *°iapnj 'iavabyS  Y.  5J.4;  —  hvs . .  yas^a  vadarS (sd.)  vBizdal  'iauni  Y.^a.io.        a)  spez.
13367:•  j.  didrva-  n.  'Holz,  Holzstück,  Baum- stumpf: iafomisd.)  va  'ärumväV.g,  11.
14210:j.  drüm :  s.   ^drva-,
14215:•  j.  'drva-,  p.  duruva-  Adj.  (fem.  °vä-) 'gesund,  heil':  bantsm^a  (sd.)  °rüm  itr»- naoiti  V.  22,  5;  —  haurvafsavS  drvö.- gal^a  .  .  'rt'S  (NPm.)   Aaurvä    Y.  5Ä  6;
14219:•  j.  'drva-  Adj.  'zwergenhaft,  Zwerg': zao'irä  yä  .  .  fratfuhannti  andäsca  kari- nasca  'vSsca  ".  .  Blinde,  Taube,  Zwerge" Ytj.  93;  —  "vi  vlmW.dantänff  Yt5.  93,
14230:•  j.  drva-fSav-  Adj.  'des  Haustiere  ge- sund sind';  pairl  .  .  dadamahl  .  .  'ßavB (NP.)  V.5Ä6;  —  mai%anahei^)  faiii.. 'ßaoi  ärvB.vlrahe  Y.  16. 10.
15466:mäoa  yal  nS  uyra.bät3us  nivänäl{sA.)  °rS ibisyatü>yS  Yt  JO.  75;  —  neben  pairi*^: flSo  ..  na ..  nipayä  . .  pairi  drvatat  alimat pairi  drvaff>y5  *haEnibyB . .  aismahe  'rB . . äraomffyj  Y.  §j.3$.  b)   bei   'fliehen';
20880:elegerint"  N.  i;  —  mi^r?m  tnä  janya  ,  , mä  yim  drvatat  ptnsitahe  mä  yitn  . . asaonai  "pactum  ne  frangito  .  .  ne  (id) quod  cum  .  .  feceris,  ne  (id)  quod  .  ." Yt  jo.  z;  —  usta  bä  yim  hacahi  ".  .  (ei) quem  sequeris"  Yt/7.  7;  —  taFöi  ayare mainyente  yat  (NSn.)  _>>««  ", .  halten  lür einen  Tag  (das)  was  ein  Jahr  (ist)"  V. 2.41;  —  ustä  astl  .  .  hyat  asäi  vakistäi ahm  (Sp.  233  u.)  ",  .  (id)  quod  (est)  .  . praemium"  Y.  27.  14;  —  ma  as  aFvB barB  (sd.)  yat  irUOm  "ne  quis  solus ferto  (id)  quod  mortuum  (est)"  V.5. 14; 14;  —  iva  dqma  ,  .  yas(ASa.)^a  da'hat spmlB  mainyuiyasca  äa^aj. .  ". .  utramque creaturam  . .  et  (eam)  quam  creavit  . ." Ytij.43;  —  ^riiat{sd.ya  .  .  glui  apa.- jasal  yatla  aiihal  .  .  yatca''  .  .  "et  tertia pars  . .  pecudum  . .  (eius)que  quod  (pe- cudum)  crit . ."  V.  2,  23;  —  tata  yal  paiii.- bannti  yä  (N.-APn.)  andu^at  *afaititat ^äjayaurva  yä..ya  aoäiti  *fr3raihyanqm (sd,)  Jrapa  *yai  nSit  visttm  (sd.)  drvatö "femer  wenn  sie  (das)  darbringen,  was.." N.54;  —  däya  ms  . .  yä  (ISn.)  ml  ai^hat afrasatfha  "des  mihi ..  (id)  quo.."  Y. 62. 6; —  iA;(sd.)  vTseyahmal{hh\'im)  kaca . .  Y. 68.1^; — havatqm  fiafia(sd.)yaÄmi(LSni.) "parynti  "..  (is)  apud  quem,."  N, /_j;  — a/raourvisvat  hrsnavainti  inm  yahmya jassnti  "..impetum  (eins)  quem  visitant"  Yt. 13.  26; — milGen.  pait,(?):^5<ja';w(  uslrd.- stärum  uzdasta  yerihä  (?)  vU  aSiö  usirB,- s/äfii/  (sd.)  aiikal  aetakm^yus  . .  V,  1$. a4(?);  —  im  Sinn  von  quantus  (s.  Sp.  120a m.):  cvail  yat  hi  kasihahe  irnvS  frat»- tntm ßisis" quaatam}  (tantum)  quantum.." V. /Ä44PiiZ.;  —  s.  noch  N.;oi?  unter "ii/.^nfis/J;  —  im  Sinn  von  quot:  ci'atgao- nahe  (sd.)  avabaräti  yä  (APn.)  *dvaeibya trizubya  (sd.)  * hartgtriwnät  ". .  (tot)  quot . . cohibuerit"  Ü-ÖS-  a)  wie  Sp.  1316  u.; erste  Person:  buyama  ahurafu  mazda  .  . astayl  yOi  narS  asavanS  humatäis  mai- nimna  , .  "wir  möchten  . .  sein,  die  (sva. indem)  wir  als  gläubige  Männer  . ."  Y. 70.4; —  zweite  Person:  uia  buyi  ajra- taintis  .  .  yH  mqm  .  .  nait  baxlake  Y.  u. *j  ^i  3i  —  ^^  ahi  yS  mqm  sbayehi  ye^he ..  srailUm  susruye  vaam  Yt. /J,  17;  — kä  tian  ahT  yim  , .  sralsttm  dädarpsa  Y, _().  I ;  —  Hsca  caräitis  ahi  yqm  . .  sralstqm dädarisa  H.  2.  10;  —  usihiiia  pliri.htiiaa-
21197:—  ttaota(sd.)ca  .  .y  aisa  ahurahe  Vr,  g.  6j  1 6f.';  —  s.  noch  Anhang.  d)  DSm.,  n.: ra%we  .  .  y  ahurai  mazdät  .  .  y  zara- %ulfräi  Vr.  12.1;  —  Primat  y  pouru.- baoxinahe  (statt  DaL)  Y,^.  37; —  huxla- hrSJfmai  ..hya^  mazdäi  ahuräi  Y.jj.  5, A.J.  6  {vioy);  —  kvävSya  y  sadhreY.^g. 30;  V.  jp.  47,VyL_jj';  —  maZsahe ..y  vars- fiSi/yU7.s6.  e)AblSm.,n.:  asätiStverz.) haca  y  vahiUät  Y.ip.  iiusw.; —  drvatat y  anrät  mainyaot  YL  /_J.  7 1 ;  —  %'wai  y eara'husträt  ^.2.3.  f)  GSra.,  ^.:  asoAe y  vahiitaÄeY.i.to;G.2.y,'Vtlj.9i,92;  — amp^ahe  hü y  aurvat.aspahe  Yt  10.  13;  67, J2.38,  S.J.  18;  —  k>r)säspahe y  *£ae%äus', gahavarahe  Yt.  /j.  6 1 ;  — ■  anhus  yS  mana (Stverz.)^"  ahurahe'?.43;\x%'v.\  —  manay zara%uUr3i  (statt  Gen.)  V.  2.  i ;  —  tava y  ahurahe  mazdä  V,  4.  3;  —  myaxdahe aoäiti  (sd.)  .  .  y  maiaySizanmayehe  A. J.7;  8— 12*,  7.  o):  aheca  kar^anS y i^anira%aht  Vr.  /o.  i;  —  aiMe  .  .  y° yasnaheca  vahmahtca  Y.  /.  2 1 ;  —  aRahe nars  .  .  y  irisfs.kasahe  V.  ^,  15;    18.  39;
24397:—  'Payäica  asaonS  stBis' (Stverz.)  Y,55. 4 usw.;  57.  Ig,  Yt.  10. 103  ;  —  aÄmUi  da'hat !')r»'krayn3  . .  irizsil  xa  bäsvh  aojS  tanvB vTspayi  drvatatim  Yt/4-  29;  39-  a)in Verbindung  mit  hauria-  Adj.:  yB  vTs- Pqm  haurvqm  tanüm  upaahanzaiU  V.6. 2431,         S.  noch  Anhang  a.        2)  PAir.:
28167:—  daiva  .  .  daxmaliva  gaahinii  apala vaipaiti  ..aisS{\it^.daxmB)  zX  asti  dania- nqm  rapakdi^A.)  ¥.7.56;  44,  5.11,  15.  28, N.  22 ;  —  nalcis  ai^anniqm  tva  . .  i^äsaya zJ  visps  anhul .  .  *jvaiti  V,  _j,  33;  — mäca  .  .  astvalahe  aahSus  didnzvS  pTsa (sd.)  manahfm  paiti. raixsJ^a  yU  zl  ..  di- dr)zvS plsa  *manahlm  ahüM  *paiii.irinaxli nsit  Al  gäul  bvat  .  .  P.40;  —  mikr»m mä  /auyä  .  .  mä  yim  drvatat  pinshrahe tnäyim  . . alaonat  tivaya  zi asti(Sp.2Tou.) mi^rS drvatasca  asaonalcaYt.  SO.  2;  ^.84;
```


## [2026-09-05T18:11:58.514Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor p in \"drvista\\|drvišta\\|druvišta\\|drvi§ta\" \"upa\\.drva\\|upadrva\\|upa\\.dr\" \"drvō\\.\\|drvo\\.ast\\|drva\\.ast\" \"draxta\\|draxt\" \"d.r.zra\\|darazra\\|dərəzra\\|dereZ\" ; do echo \"=== $p ===\"; grep -n \"$p\" BRT.txt | head -6; done",
 "description": "Grep Bartholomae for specific Avestan forms"
}
```


## [2026-09-05T18:12:00.004Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD ===\"; grep -n \"draxt\\|dār \\|dārūg\\|drōd\\|drust\\|drōz\" PHD.txt | head -30",
 "description": "Grep MacKenzie Pahlavi dictionary"
}
```


### [2026-09-05T18:12:00.554Z] TOOL RESULT

```
=== drvista\|drvišta\|druvišta\|drvi§ta ===
=== upa\.drva\|upadrva\|upa\.dr ===
24988:hävanlm  paiti  °tBm  Y,  2.  18,  A^J.  1.;  — hävanSis  -'hviJ  Y.  ;.  1 7,  j.  i ;  —  frä  *mä *narf  *g3ray/>is  (Sp.  511  u.)  yat  'tu!  *fri- tSii  *äjaiSt  N.ip;  —  asnyeAe (sA.) pascalta anyehe  "ärcJ  .  .  nasus  upa.driqsaiti  V. '■4-
=== drvō\.\|drvo\.ast\|drva\.ast ===
=== draxta\|draxt ===
14059:•  j.  draxtö.hunara-  Adj.  'der  gelernte Fertigkeiten  besitzt,  Kunststücke  kann' vom  Luxushund'*:  iünqm  .  .  'narattam V.  IJ.&;  —  *ui  *täät  Spina  patfnti  pasus.- Aaurvam äi  (sd.)  ..  "naranamia  V.  jy.  42.
14069:a  drynja-,  7  dadrang-''>,  16  (Des.)  dh drayia-*'*,  i^drfnjaya-.  — PPfP.  •draxta-^''. 'festigen,  kräftigen,  bestärken':  änräm aSal^qm  axlinam  fqtiayö  dnnjatH  (statt Plur.)  "ein  Drittel  dieser  Krankheiten  be- stärken die  Menscher"  V.  7. 59  Gl.  Un- klar: tun^ö  hs  dqdrqxtii>  V.  4. 10  PüZ. mit  a  i)  'etwas  befestigen  an  — '  (AbL): äjir»njaySiS  aom  srum  paurva.naimäj (sd.)    aAe    gravaAe  V.5.  14.  2)  'fest-
14071:mit  kam  dnwS.  (mit  intens.  Bed.):  aim (näml.  asmd)  yS  hiHatU  *mainyuM3tS Aandraxts  düraAarafüS  Yt  t$.  2.
14079:'aaswendig  \emea' :  yaval  oSaAmya  *zru (sd.)  staolanqm  yesnyanqm  didräjSis^'*  N, 12;  —  vupim  ä  ahmät  yat  tä  sravä  dnn- jayqn  yi  paourva  (sd.)  ag'krapatayO  är»n- jayqn  "bis  dass  sie  die  Sprüche  auswendig gelernt  haben  werden,  die  zuvor  die  Lehrer auswendig  gelernt  haben"  V.  4.  45;  — S.  draxtB.".  a)  'memorirend  aufsagen', Tenn.  techn.  fiir  leises,  munnehides  Auf- sagen von  Gebeten  (usw.):  aä^a  imqm vacS  drmfayBil  a^a  imqm  vacS  /ramruyä Yt  y.  so,  V.^.ij,  17,  a8;  —  aha  imä nämfnls  drinjayO  framrava  Yt.  7. 1 1 ;  1 6, 4-A  (wo  "drfttji^ä);  —  yezt  .  .  dnnja- yeiti  (Konj.)  para  paityäiti  vlrat^ayeiti (sd.)  N,  Ji; — yesi ..  ärmjayäatca  "naimca *pasca^a  *vJrao%aySt  {sA.)  N.  n; — yasca ml . .  iayqm  ahunahe  vairyehe  dr»njayö apa.raohayeüe  (sd.)  Y,  /p.  7 ;  —  yaica  ml . .  bayqm  ahunahe  vairyehe  marät  JrS  vä marS  drynjayät  ß-a  vä  dnn/ayö  srävayäi frä  vS  srävayB  yasäite  Y.  ig.  6.
26822:paiti  irista  bazaiti  V.ij.g;  — spanaÄe'\ V.y.48  PüZ.;  —  Sing,  in  koUekL  SbnJ äal . .  ahe  tunanahe  . .  /rapi'iwS  (sd.)  spä  ! V.^.j;  —  taiHl  ya  bavainti  aos5.tarash .  .  yäha  anya  spa  V.  13.  42  (?).  a)  im Gegensalz  zu  Menschen  und  zu  andern Tieren :>'((/ii>4mi  spanasca  narasta  para.- irtiinti  V.5.  ij^.s,  u,  36,  8. 14;  —  yai ahmi  nmäne..spa  va  na  va  iri^yai  V.Ä  4; '>  5-  39;  —  y^  asiim  upanhanzaiii  sBnS va  para.irittahe  maryehe  vä  y.6.  10;  12, 7.23; —  *näirikayä  hhrpa  ..sunü  kihrpa N.jp;  —  pasvamca  slaoranqmca  masya- nqmca  saiiamla  vayqmca  V.  2.  8; — pasca . .  nasäum  ava.kar>i>nti  spstum  vä  raoz»m va  v>hrk3m  va  V,  5.  5;  6.50;  —  yahöit dim  . .  avaxanan  süns  (NP.)  va  hnß.- ifardvayB  va  V.ö.^s;  46,7.29,  30;  — j/J vä..vay5vä  hn/sji^aroFr'W.li.  A)  mit Bezeichnung  der  besonderen  Art:  spä pasusJtaurvS^''  .  .  spä  vU.kaurvS''''  .  .  spa vohuna^B^^ ..spa  taurunö'''^..spa  sukurmd*''> . .  spa  jaiui^^ . .  spa  aiwinu/'''' . .  spa  vltus''^ ..spa  urupis"'^'  V.  5,  29-33;  —  späntm slidnm  urvUarsm  yim  vat»hapar>m^^  V. 13.3;  —  ys  aSa^qm  sünam  Jainti  yim pa^us.kaurvqmca  viLhaurvqmca  vohuna- sgqtnea  draxtS.hunaranqmia^^  V.  13. 8,  42 ;
28599:Undeutlich:  mnbyS  kS  dqdraxti  Y.4. 10 PüZ.;  —  ha  drvatqm  *ayqm  (sd.)  urvanS timB.Ava  nizarsaite  V.  ;p,  30;  30;  —  ha druxs  .  .  FrW.  8.  a';  —  '"näuiti  Aa aite  yüi  maSyaka  ^ar^nti  Jramanyete  V. 7- SS-  Wertlos:  yd^a  Ab  nS  altalsqm
=== d.r.zra\|darazra\|dərəzra\|dereZ ===
5841:uta  ärvh  "ppm  *isaiii  Aog.A'a;  —  ^risattm upstananqm  (Stverz.)  upäzsit  'pahe  aStraya \.4. 19, usw.;  —  'paecafaiti  vTraica  Yt/O. 101 ;  —  'palsu  vJraSsu  Yt  1$.  53;  —  'pa  ' (NP.)  hubaräita  (sd.)  rai:a  kvasäna  VyL , 4.V;  —  äiuica  'ps  dirizrasca  *väsö  YL '3-  S^'<  —  i^^  '"•^  'pake  vansa  (sd.) Vd-j;  S,  N.jt*;  —  ^iüirya  payh{iA.)  .  . 'paySatca  *xarayäatca  H.6^;  —  °paya (GS.)  paurvöMzya  (sd.)  ar^jS  N.  <?5;  — •/kJ  «r/a  (sd.)  Yt  74-  31.  39,  'Ö-  10;  — "/.?Ä^  paiii  arsriiJ  (sd.)  ayryehe  V.  <?,  37; /4.11;  —  jtfil'w  'panam  arsnam  Yt.  5. 21;  V.  22.  20;  —  'pä  (ISf.)  -/äsv«  (sd.) ar.>p  "um  den  Preis  für  eine  Rossstute" V.  ^,  4a;  —  Aasannm  "panqm  (GPf.) , daZimnqm  (sd.)  paiti.puiiranqtit  A,  _J.  9; —  'p5  ayryöJimö  datihve  varnnanö  *a^la gai-qm  asinqin  aryd  "das  edelste Ross  aus  der  Auslese  eines  Landes  hat den  Wert  von  acht  trächtigen  Kühen" F.jh.         [N.J7.-  lies  iar3.asps.]
11047:—  tava^ä  Aaximä  a'ahyacä  Y.  40.  2;  — kascilca  assqm  vairyanam  kasHtla  alsam apayiäranqm  Y.  65. 4 ;  —  Ssusca  asps dsrfzrasca  *7iäls  Yt  JJ.  S *  i  —  vohuca  manff lUars'ca  Yt  29.77; —  a.Hsca  vaauAi  bin- zaiti  pärsndiea  YtÄ38;  —  star>tasca ^litus  anyäsca  .  .  avar?th  Yt.  //.  7 ;  — fsnsvatfa  manS  vpr^zvatica  .  .  aisuha  Y. 6'2. 10;  —  V)r3i!ra-jn?mca  ahura^t?m  va- naintlmca  uparatätun  YLy.34; — äsnaica zbayaiitäi  daraica  tbayaniäi  Yt  77.  2;  — yaiiä   asnst  yalcS  dural  t/aia  Y.  4S-  '  j
13564:•  j.  dvrazra-,  drazra-"  Adj.  {km.'rä-) 'fest,  stark,  tüchtig':  buyät  ssusca  asps °raica  *vasS  Yty.52;  —  -rS  nai/ia  ahmi ^dariüstd  nama  akmi  YL/j.46;  Y.14^^; —  mq'iranqm  °r»m  ma'iranqm  d?r}srS.- ifftum  Yl  j.  5;  —  fravasis  ,  .  °ra  yaza- maide  Y t.  y .  7  5 ;  —  ailalca  t!  vacä  yöi . . •ra  äs  Yt./4. 46.
14139:•  j.  drazra-  Adj.:  s.  unter  dirtzra-.
```


### [2026-09-05T18:12:00.604Z] TOOL RESULT

```
<persisted-output>
Output too large (32.3KB). Full output saved to: /home/sfmqrb/.claude/projects/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tool-results/bt9rmspnt.txt

Preview (first 2KB):
=== PHD ===
125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
...
</persisted-output>
```


## [2026-09-05T18:12:18.235Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 137 (p.116) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==138 {print}' HRN.txt | head -60",
 "description": "Horn page 116"
}
```


## [2026-09-05T18:12:18.562Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 145 (p.124) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==146 {print}' HRN.txt | head -60",
 "description": "Horn page 124"
}
```


### [2026-09-05T18:12:20.072Z] TOOL RESULT

```
=== HRN leaf 137 (p.116) ===
— 116 —
'setzen, machen, schaffen ; phlv. dätan; ai. l^dhä-,
dädhati; arm. dnel setzen' (H. No. 84).
522. (Tür 'Baumstamm, Holz', dann,
aw. däuni' 'Holz'; phlv. dar, dann 'hölzern (vd. 7
(188)), vergl. arm. LW. darastan 'Garten'; ai. därtt-
*Holz\
np. durük 'dünnes Holz' (unbelcgt) gehört dagegen
zu ai. drü' 'Holz, Baum', gr. d(jvg Baum, Eiche', d()ior
{*ö(jfoi') 'Gehölz', ksl. drüvo (d. i. '^'drvo), got. friu 'Holz,
Baum'.
LW. kurd. dar; bei. dar (55).
523. därü, därUt *Ai'znei; Schiesspulvor', vergl. der man
(No. 554).
l^dhar- 'halten', vergl. aw. drva- gesund; phlv. därük
'Arznei'.
LW. kurd. af/. bei. (56) därü,
524. dm*e 'Gehalt, Salair'.
aw. dadra- 'Geschenk, Gabe'; phlv. ddsr; ai. däfra-
'Gabe'.
Hörn, KZ. 32, 584 No. 15.
525. (IffS 'Sichel'.
ai. dätra- 'Sichel'; phlv. das (AV.).
afy. lür 'Sichel'; LW. kurd. bei. (76) das,
526. däS 'Ofen*.
Zu [/'dagli' (aw. dajjz-, ai. rfa/i-), brennen (Nöldeke,
mündliche Mitteilung).
527. dästen 'halten, besitzen', Praes. där-em, dar, dara,
g. dartmfm; Käs. dörtän^ dördhi, dörd^nmn^ dort.
ap. l/^rfar-, darayamiy, adäraya 'halten, besitzen';
aw. [/^dar-^ däray^M; phlv. dästan^ dar-am, dar(i)sv^
dästar [syr. LW. *T1, ödg (de Lagarde, Ges. Abh.
33) sind verlesen (Nöldeke, Tabarl-Übersetzung,
447)] ; ai. [/^dhar-, dharäyati,
kurd. 'dar (LW.); af/. laral; oss. t. daf-in (102);
bei. (L W. ?) darag , n. daray (75) ; wa/. va-dür-am,
sar. ö6r-am.
Gehört hierher vielleicht auch zJnhär, zinhnr 'Schutz,
```


### [2026-09-05T18:12:21.939Z] TOOL RESULT

```
=== HRN leaf 145 (p.124) ===
— 124 —
aw. droatäl- 'Geisundlieit' ') ; plilv. drüt (Men. ; AV.),
drütik courtoous' (West II, 280).
556. durüclen 'crndtcn\ Praes. diretv-em diretvldeiij durüd
'Erndto', JN^ni ^Erndte' (Is. 9, 2).
aw. vergl. dereta-, adereta- {t/ava-) ^geschnittenes,
gemähtes (sc. Korn)'; päz. drüdan erndten (PPGl.,
Men.).
kurd. dirün, dirütin erndten', dirün 'Erndte*; wa/.
drdw-am.
Das 3 in jüd.-pers. )x5l*n zwingt direivem zu lesen
und mit Spiegel, Arische Periode, 70 gr. Ooftko
'pflücken* zu vergleichen.
557. iliiröy, deröy 'Lüge; unwahr.
ap. drauga- *Lüge*; i\\^\ draoya'\ phlv. dröy, dröy,
LW. kurd, durüy; af/. daröy; bei. davöy^ drög,
n. dröy (49).
558. dnrüne 'Regenbogen'.
skr. drum- 'Bogen' (spät und selten).
bei. drm, drmuk 'Regenbogen* (85); yidg. LW.
drün,
bei. drin beweist, dass die ebenfalls überlieferte
np. Aussprache dnrüne falsch ist, vergl. Hübsch-
mann, ZDMG. 44, 555.
559. derves 'Bettler; arm', deryös (Vis und RämTn, S. 395,
Vers 8), deryös, deryöz, deryöze.
aw. vergl. driyu- 'arm*, fem. driwt- {*driyvJ-),
driwika- {?); phlv. daryöä, daryösih.
Die neupersisehen Formen sind im Einzelnen schwer
zu erklären. Auch derey 'Jammer, Elend', Grund-
bedeutung 'Mangel, Beraubtsein*, dereyä gehören nach
Nöldeke (mündliche Mitteilung) hierher.
560. derre 'Thal, Schlucht'.
aw. darenä- 'Thal, Schlucht'; Adovu, Ptolem. 6, 1
(Spiegel, ZDMG. 32, 721).
») Vergl. Fr. Müllor, WZKM. 5, 352.
```


## [2026-09-05T18:12:39.403Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN durudgar ===\"; grep -n \"durüdgar\\|durudgar\\|dürgar\\|drdgar\\|Zimmermann\" HRN.txt | head -10\necho \"=== HUB ===\"; grep -n \"durüne\\|dārū\\|därü\\|dārūk\\|drvatāt\" HUB.txt | head -20",
 "description": "Horn durudgar, Hübschmann"
}
```


### [2026-09-05T18:12:39.465Z] TOOL RESULT

```
=== HRN durudgar ===
3641:LW. :it^NlO"nü *Zimmermannsaxt' (de Lagarde, Ges.
=== HUB ===
```


## [2026-09-05T18:12:42.547Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^drust\\|^drōd\\|^draxt\\|^dār\\b\\|dārūg\\|drōdgar\\|dārūg\\b\" PHD_mackenzie.txt PHD.txt 2>/dev/null | head -20\necho \"=== search PHD lines ===\"\ngrep -on \"drust \\[[^]]*\\][^.]\\{0,60\\}\\|drōd \\[[^]]*\\][^.]\\{0,60\\}\\|draxt \\[[^]]*\\][^.]\\{0,60\\}\\|dārūg \\[[^]]*\\][^.]\\{0,60\\}\\|dār \\[[^]]*\\][^.]\\{0,60\\}\" PHD.txt | head -20",
 "description": "Grep MacKenzie for headwords"
}
```


### [2026-09-05T18:12:44.078Z] TOOL RESULT

```
PHD.txt:1700:drug dārūg.
PHD.txt:2765:medicament dārūg.
PHD.txt:5356:drustéw dz društāwāz društīh društ
PHD.txt:5461:drustih drust
PHD.txt:5462:drustabed
PHD.txt:5547:dārwāzīg dārūg dārgardīh dālman Фагтар
PHD_mackenzie.txt:2050:draxt [dW)ht I M drxt, N diraxt] tree.
PHD_mackenzie.txt:2089:drust [drw(y)st l I (M dryst), N durust] right; well, healthy.
PHD_mackenzie.txt:2091:drustabed [drwystpt l ] chief physician.
PHD_mackenzie.txt:10594:draxt                    \~           gaz-
PHD_mackenzie.txt:10810:drustih
PHD_mackenzie.txt:10817:drust                                                 .. dandiin,lll\\'iill
PHD_mackenzie.txt:10819:drustabed                                               dug
=== search PHD lines ===
125:drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed
191:dār [^mynyt!l] unthinking
256:dār [byšbwlť’[] hostile
292:dār [bwit!]] bearer; womb
306:dār [d’t?l | N ~] creator
308:dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper
312:dār [dynbwit^l] believing, faithful
314:draxt [4/0)А | M drxt, N diraxt] tree
316:drust [drw(y)st' | (M dryst), N durust] right; well, healthy
325:dār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin
394:dār [hndyfyt?I] thoughtful
426:dār [krt-, kil | N ~] active; worker, doer
439:dār [т comer. mādar [AMYtl < А т-у; mtl | M mdr, N ~] mother
493:dār [mwrt?], mwld?l | N ~] carrion
494:dār [л?т bwlt?l | N ~] heir, preserving the father's name
555:dār [lsd] | N ~] brigand, highway robber
568:dār [sp?sd?] | N sip~] grateful, thankful
593:drust [tn'drw(y)st! | N ~] healthy, whole
651:dār [xt' | N gudár] passage, entrance
663:dār [hwit?I] (legally) edible, not murdār
```


## [2026-09-05T18:12:48.554Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2030,2100p' PHD_mackenzie.txt",
 "description": "MacKenzie d- entries"
}
```


### [2026-09-05T18:12:48.600Z] TOOL RESULT

```
   --isn: liking, pleasure.
 2dosidan [dwfytn'] = Idoxtan.
 dosiza~ [dwlyek l I (M dwxf, J dwlkyzh), N --a] maiden, virgin•
   .....,ih: maidenhood, virginity.
dOwom [2wm I N --] -second (in compound numerals).
Idoxtan, dos- [dwhtn , dwl- I N --] milk.
                            '
2doxtan, doz- [dwhtn , dwe- I N --] sew.
                            '
doysBr [dwys1 = Av. doilJra-] eye.
doz-, v. 2doxtan.
drafs [d1pl I P drjf, N --] banner.
drafsidan, drafs- [d1pf-ytn' I P drjf-, N --] I. shine; 2. tremble.
drahm [ZWZN' < A zwzn I M drhm, N dir(h)am] drachm.
dra(h)nay [dl(h)n)d] length.
dramana~ [d1mnk I N dirmana] wormwood.
                         '
dran~ [d1ng I N dirang] period, duration.
dranJidan, dranJ- [d1ne-ytn ' ] speak.
  --isn: speech.
draxt [dW)ht I M drxt, N diraxt] tree.
dray-, .....,isn, ' v. drayidan.
draya(b) [d1yd'(p) I M dry'b. N daryii(b)] sea.
  ---bar [-b)ll N -bar] sea-shore.
drayan-Joyisn [d1'd'n ywdfn ] one who speaks while eating.
                                   '
  --ih: (the sin of) speaking while eating.
drayidan / drayistan, dray- [d1'd-ytn , -stn' I M dr'yst, dr'y-, N
                                            '
     dariiyidan] speak (daevie), chatter.
  .....,isn: chatter.
draz [dPe I N diriiz] long.
·drem [d1ym] phlegm.
driyos [d1gwf I N dary6f, darwef] poor, needy.
  .....,ih: poverty.
dro [KDBA < A kdb); d1wb' I M drw, (N daro,,)] lie, deceit.
drod [SRM < A f1m; d1wt l I M drwd, N darod] health, well-being,
     prosperity, peace.
dro-dadwarih [KDBA d'twblyh] false judgement.
Idron [dlwn l I N daruna] bow.
2dron [d1wn I N darun] consecrated bread, ceremony in which c.b. is
                 '
     used.
dron yaAtan                                               duA-~ihr

dron yaAtan: consecrate the sacrificial bread.
droA [dlwl] mark, branding; punishment.
 .....al1 [~k'] -desolation.
droAidan, dros- [dlwl-ytn ] brand.
                                   '
drosom [dlwlwm] mark.
droz-,v. druxtan.
drozan [dlwcn l 1M, J drwzn] lying, liar.
 .....ih: falsehood.
drubuAt [dl(w)pwlt ] fortress .
                            '
 .....ih: defence, fortification.
driidan, -driin- [HCDLWN~tnl < A ..; l:z~d I M dr(wd, (dwr-), N
      durudan, diraw-] reap, mow.
drust [drw(y)st l I (M dryst), N durust] right; well, healthy.
 .....ih: righteous; health.
drustabed [drwystpt l ] chief physician.
druAt [dlwlt ' I N durult] harsh, rough, severe.
  .....,ih: harshness, severity.
  .....-awaz, -..-ewaz [-)p)c, ~)yw)c] harsh-spoken.
druwand [dlwnd 1M drwnd] evil, sinful, unrighteous.
  -..ih: sin, unrighteousness.
druxtan, droz- [dlwhtn , dltvc- I M drwxt, drwz-] lie, deceive.
                                 '
druz [dlwc I (P dr~f)] demon.
diid [dwt' I M dwd, N .....] smoke.
```


## [2026-09-05T18:12:56.758Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"d.r.g \\[d\\|dārūg\\|d'rwk\\|darug\" PHD_mackenzie.txt | head -10\necho \"---\"; sed -n '1900,1935p' PHD_mackenzie.txt",
 "description": "MacKenzie dār / dārūg"
}
```


### [2026-09-05T18:12:56.851Z] TOOL RESULT

```
7089:medicament darug.                          millstone iisyag.
10922:dadar, gadar                     ~l'eJU         darug
---
                                     '              '
darfig [d'lwk ' I M d'rwg, N daru] drug, medicament.
dar-wazig [d'lw'eyk I N dlir-baz] (pole-)acrobat.
                            '
darz [dIe I N --] seam.
  ",ill [_yk l I N darzi] tailor.
das                                25                         dazidan
das [d's I N --] sickle.
dasBr [d'sl = Av. dii8ra-] gift, reward.
 dast [YDE < A yd-h; dstl I = M, N --] hand.
dasta~ [dstk 1 I N --a] bunch, bundle, group.
dast(a)~ird [YDE-, dst-krt l I M dstygyrd, N dastgird] estate.
dast-l1ir [dst OHDWN, (v. griftan) I N --] I. helper; 2. captive.
dast-~raw [dstglwb ' ] captivity.
dast-karih [YDEk'lyh I N --i] handiwork.
dast-Aoy [dstfwd] = ~omez.
dastwar [dstwbll M dstwr, N dastilr] authority, priest, minister.
   --ih: custom; authority.
dastyar [dstyd'll (P dstd'r), N --] helper.
  --ih: help, assistance.
daAn [dIn' I = M] right hand.
diAn [d'fn' I M d'f(y)n] gift.
daAna~ [dInk I I N --a] I. right hand; 2. dagger.
daAt [dft' I = M, N --] plain, open ground.
dastan [dIt'n l I N --] menstruation; menstruous.
  --estan [-st'n l ] secluded place for menstruous women.
  ---mah [-m'h] menstrual cycle.
  -omand [-'wmnd] menstruous.
daAtan, dar- [YHSNN-tn < A"'; b-sn; d'Itn ' , d'l-I M d'ftn, d'r-, N-]
                                '
      have, hold, keep, preserve.
  pad ..• dastan: hold by, to; take for.
  pad ed da§tan [cf. N pindiiItan] consider.
  -iAn: preservation, maintenance.
dastar [d'ft'l] keeper, preserver.
daw-, v. dawidan, dawistan.
```


## [2026-09-05T18:13:02.272Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '1875,1902p' PHD_mackenzie.txt\necho \"=== KNT p.190 (leaf 205) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==206 {print}' KNT.txt | head -60",
 "description": "PHD dar entries and Kent p190"
}
```


### [2026-09-05T18:13:03.801Z] TOOL RESULT

```
                                         '
    N --] know.
 --isn: knowledge.
 ,...,lsnOmand [-sn'wmnd] knowing.
dar [BBA < A bb'; dll M dr, N,...,] door; palace; chapter, subject.
dar [d'll M d'r-, N ,...,] tree, gallows; wood.
dar-, --lsn, v. dastan.
-dar [-d'll M -d'r, N --] suffix, -holder, -keeper.
P daray [dl'g I J --, N daray] bell.
·darak [dlk l ] section, paragraph.
darband [BBAbnd IN",] gate.
darbas [dIp's] palace.
dard [dW I M drd, N ,...,] pain.
 --omand [-'wmnd I M -wmnd, N ""'mand] ill, suffering.
daren [d'lyn l 1M d'rwyn] wooden.
dargah [dIg's I N --] doorway.
dargardih [d'lkrtyh I M d'rgyrdyh] crucifixion.
dar-handarzbed [BBA-, dl-hndlept ' ] chamberlain.
darigbed [dlykpt ] palace superintendent.
                          '
• darmag [d'lmk ] fine, delicate.
                        '
darmin [dlm'n I M drm'n, N --] remedy, medicine.
                      '
darridan, darr- [SDKWN-tn < A"'; sdq; dl-ytn IN",] split, tear.
                                     '              '
darfig [d'lwk ' I M d'rwg, N daru] drug, medicament.
dar-wazig [d'lw'eyk I N dlir-baz] (pole-)acrobat.
=== KNT p.190 (leaf 205) ===
 sg. subj. (8212, $227.1) DNa 42. xindsdtiy subj. ($02, $97, 5110, $122) DB 1.52.
azinav- vb. ‘hear, satisfy’ ($96): cf. Av. zšnav- ‘Genüge haben an’, adj. zínav- ‘Genüge leistend’, ріс. zšnůta-, sb. zínütay- ‘Zufriedenstellung’ (Bthl. AiW 557-60); apparently an extension of root zinà- ‘learn’ (cf. pIE *40- and *doy- ‘give’), with semantic development ‘learn, hear of, hear’, and ‘hear, hearken to, satisfy’ (Lg. 15.171; ef. also Bv. TPS 1945.47-50). Hz. ApI 238-40 gives an impossible equation with Skt. éru- ‘hear’ (pIE
OLD PERSIAN
*flu-); Sen 247, 251, has wrong meanings. Р}.
sani, Acme 1.319-20, gives another etymology, -
See also uzsnav-.
z5nula- past pte. pass. ($71, 3242.1), cf. uzšnav-: zSnuta nsm. ‘satisfied’ DNb 26. |xsnutam) nsn. ‘heard’ DNb 53.
à + zínav-: dxSnautiy (§71, $122, $208) ‘satisfy’ DNb 24. āzšnavāhy 2d sg. subj. (§227.1) ‘satisfy’ DNb 29f. äzšnudiy 2d sg. ішу. ($208, §237.1) ‘hear’ DNb 54.
gaifa- sb. ‘(living) personal property, cattle’: Av. gaébü- ‘individual living being, pl. world; household, property’, РЫ. géhdn ‘world’ (from gen, pl.), to root pIE *g*ei- seen in OP jiv- (869, $101, $151). For varying interpretations, see Tm. Lex, 85, with lit. — ga26àm-cà (S89) asf. DB 1.65.
gaud- vb. ‘conceal’: Av. gaoz-, Skt. githati (§88). apa- + gaud- ‘conceal, hide away’: apagau- dayahy 2d sg. subj. (§227.1) DB 4.55, 51. apagaudaya 2d sg. inj. (5215, §224, §227.II, $237) DB 4.54. gaub- vb. ‘say’, mid. ‘call one’s self’ (§213): Sas. РЫ. gowét ‘he says’, NPers. goydd, inf. guftán: perhaps a -bh- extension of pIE root *gheu- seen with -s- extension in gauga- (q.v.; Ву. BSLP 31.2.70). gaubataiy mid. (42851) DB 2,21, 31, 51; 3.15, 59. agaubaté imt. mid. DB 1.84, 93; 2.66f; 3.35, 55 (written agauratà, 454.11), 89f; 4.82. agauba^ià 3d pl. imf. mid. ($28617) DB 293. gaubdtaty subj. mid. (5285.1) DB 2.84; 3.86.
Gaubarwa- sb. ‘Gobryas’, ally of Darius against Gaumata: Flam. kam-bar-ma, Akk. gu-ba- ru-’, Gk. TwBpins; from gav- ‘cattle’ + *baruva-, cf. Skt. bharu- ‘lord’, to vb. bar- ($85.П, $101, $122, $142, $143.II, $150, $1581, $160.Ib): ‘Cattle- Possessor’ (Justi, IFA 17.111; otherwise Foy, ZDMG 54360). Gaubaruva nsm. DB 4.84; 5.7, 9, 11; DNe 1.
Gaumdta- sb. ‘Gaumata’, Median pretender who took the name Smerdis ($164.I): Elam. kam- ma-ad-da, АКК. gu-ma-a-lá; from gav- ‘cattle’ + pte. mdta- of unknown meaning ($242.II). Gau- mata nsm. DB 1.36, 44, 46, 64, 65, 70; 4.7; DBb 1f. Gaumdiam asm. DB 1.49f, 54, 57, 73; 4.81.
gausa- sb. ‘ear’: Av. gaosa-, NPers. gas, Skt. ghóga- ‘noise’; Iran. root *gaus- ‘hear’, pIE *gheus-
(670, 5101, $1431). диа adm. ($189) DB 274, — |
| КИ adven as n Le ЧЕР Г PERDE :
ок ALES
e
LESIN EI EOE PE EERE СООТУ
I aen i bag ih oea CAU Lin aE M iig Án
LEXICON
89. gaušāyā idm. (5189; with sg. ending, Lg. 19.225) DNb 53.
gafu- sb. ‘place, throne, place of battle’
(JNES 4.49-50): Av. gdtav- дабш-, NPers. gah, Skt. gütu-, to pAr. root gam-, pIE *g*em- ‘come’ ($68, $81, $158.11, §179.n2). давит asm. DNa 41f. дйбарй lsm. ($137, $182.IT) DB 1.62f, 66, 69; DNa 36; DNb 35 (INES 4.49-50); DSe 36f, 44, 44f; XPf 33 (as abl., $182.III, though without hacé: Lg. 941-6; Ву. BSLP 33.2.148-50; Wb. А 41.319-20; Sehaeder, SbPAW 1935.503; Hz. AMI 4.130-2, 8.45, ApI 177-80), 85; XPh 34.
gad- vb., see jad-.
Ga*dara- sb. ‘Gandara, Gandaritis’, a prov- ince of the Persian Empire: Elam. gan-da-ra, Akk. gan-da-ri. See also Gadáraya-. Сайдта nsm. DB 1.16; DPe 1.18; DNa 24f; DSe 24°; DSm 9°; XPh 25. Gadārā absm. DSf 34.
Ga"déraya- adj. ‘Gandarian’: adj. to preced- ing ($144.III, $167). Gadàraya пзш. APP 12.
Ga*dutava- sb. ‘Gandutava’, a district in Arachosia: Elam. gan-du-ma-+. Cf. Tm. Lex. 86. Gadutava пет. DB 3.66.
gan- vb., see jan-. gand- vb., see gasta-.
gam- vb. ‘come’: Av. gam-, Skt. gam-, Gk. Ваши, Lt. venió, Gt. qiman, pIE g*em- ($101, $244). See also gdéu-.
à + gam- ‘come’: бјата opt. (Skt. gamyat; §67.1, §101, $122, $132.2, $218.11, $293.I, §228.IT) DPd 19.
ava- + gam- ‘go dow
```


## [2026-09-05T18:13:09.897Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"dāru-\\|daru- sb\\|asādāru\\|asa-dāru\\|as[āa]dāru\\|ebony\" KNT.txt | head -20",
 "description": "Kent daru/ebony"
}
```


### [2026-09-05T18:13:09.951Z] TOOL RESULT

```
4296:{81. 40-5. The silver and the ebony were brought from Egypt. The ornamentation with which the wall was adorned, that from Ionia was brought. The ivory whieh was wrought here, was brought from Ethiopia and from Sind and from Arachosia.
5530:daru- sb. ‘wood’: Av. déuru-, Skt. dáru-, ef. Gk. доро ‘spear’. düruv (§181) nsn. DSf 41, in phrase asd атир ‘ebony’, lit. ‘stone wood’ (§308.- nl), so called because of its hardness; but also probably аз@ because of the assonance translated Akk. aban ‘stone’, ef. Hebr. eben ‘ebony’, Gk. Веро, from Egyptian hbnj ‘ebony’ (J. Duchesne- Guillemin, BSOS 10.925-7 [1942], noting that acc. to Hdt. 3.97 the Egyptians paid a tribute of ebony logs to the Persian King). Not to be normalized dārwa to root !dar- and the phrase taken as ‘copper’ (Scheil 21.30; Kent JAOS 51.208, 53.18- 9), or as ‘iron’ (Ву. BSLP 30.1.60; who also sug- gests that dáruva may be an adj. referring to some kind of tree); not asé + instr. déruv ‘window frames of wood’ (König, Burgbau 64-5); not asd süruva ‘lead’ (Hz. Ар] 299), to Av. srva- ‘lead’ (Bthl. AIW 1649), for the slight traces do not con- firm initial s". — [dár|uv asn. DSf 51 (so Hinz, Orientalia, soon to appear; not {23mal}uv, see Lex. S.V.).
```


## [2026-09-05T18:13:20.594Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN tabret/timbrel/toph ===\"; grep -n \"tabret\\|timbrel\\|Heb. toph\\|tōph\\|duff\" KLN_1966.txt | head -15\necho \"=== AFA duff ===\"; grep -n \"duff\\|Pauke\\|Tamburin\" AFA.txt | head -15\necho \"=== AFM دف ===\"; grep -n \"الدف\\|دف \" AFM.txt | head -10\necho \"=== PLA daf ===\"; grep -n \"daff\\|duff\" incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt | head -10",
 "description": "Grep Semitic sources for duff"
}
```


### [2026-09-05T18:13:20.692Z] TOOL RESULT

```
=== KLN tabret/timbrel/toph ===
10411:deaf,  adj.  —  ME.  deef,  def,  fr.  OE.  deaf,  rel.  to OS.  dof  ON.  dattfr,  OFris.  daf,  Du.  doof,  ‘deaf’, OHG.  toub,  MHG.  toup,  ‘deaf,  stupid’,  G.  taub, Goth,  daufs,  ‘deaf,  insensate’,  and  cogn.  with Gk.  Tutp-Xoi;  (dissimil.  fr.  *®u<p-X<5<;),  ‘blind’, OIr.  dub,  dubh  (for  ’dhubu),  ‘black ;  ink’,  fr.  I.-E. base  *dheu-bh-,  ‘to  fill  with  smoke,  to  cloud, darken ;  to  be  dull,  dumb  or  deaf’.  Cp.  dove.  Cp. also  dumb,  which  derives  from  a  nasalized  form of  base  *dheu-bh-.  Cp.  base  *dheu-p-,  which appears  in  OI.  dhiipah,  ‘smoke’.  The  bases *dheu-bh-,  *dheu-p-,  are  enlargements  of  base * dheu -,  ‘to  fly  about  like  dust,  to  smoke’.  See tbio-  and  cp.  duffer.  Cp.  also  stove.
12148:rel.  to  ON.  deig,  Dan  deig ,  Swed.  deg,  MLG. deck,  MDu.  deech,  Du.  deeg,  OHG.,  MHG. teic,  G.  Teig ,  Goth,  daigs,  dough’,  digan,  ‘to knead’,  fr.  I.-E.  base  *dheigh-,  *dhoigh-,  *dhigh-, ‘to  form  out  of  clay,  to  knead,  form’,  whence also  Of.  dehmi,  ‘I  smear,  anoint’,  dehah,  ‘body’, lit.  ‘that  which  is  formed’,  dehi,  ‘rampart,  dam, dike’,  Avestic  daeza,  ‘wall’,  pairi-daeza,  ‘en¬ closure’  (whence  Gk.  TrapaSsiaop,  ‘enclosed park’),  OPers.  dida,  ‘castle’,  Toch.  A  tsek-, tsaik-,  B  tsik-,  ‘to  form’,  tseke,  ‘statue’,  Arm. dez ,  ‘heap,  pile’,  dizanem,  ‘I  heap  up,  pile  up’, Gk.  Tetyo?,  zov/'K  (dissimilated  fr.  *Hixoz, *ffotyo<;),  ‘wall’  (orig.  'clay  wall’),  (Hyyaveiv,  ‘to touch’,  Thracian  -SI£a,  ‘castle’,  L.  fingere,  ‘to form,  shape,  fashion’,  figura ,  ‘form,  shape’,  fi- gulus,  ‘potter’,  Oscan  feihuss,  ‘the  walls’,  ORuss. deza,  ‘baker’s  trough’,  Lith.  diezti,  dyzti,  ‘to cudgel,  thrash’  (lit.  ‘to  knead  thoroughly’),  OIr. digen,  ‘firm,  solid’  (orig.  ‘kneaded  into  a  com¬ pact  mass’).  Cp.  also  the  metathesized  forms: Lith.  ziedziu,  ziesti,  ‘to  form,  build’,  OSIav. zizdp,  zidati,  ‘to  build’,  zidu ,  ‘wall’.  Cp.  dairy, duff,  ‘pudding’,  and  the  second  element  in  lady. Cp.  also  deha,  dixia,  dizdar,  effigy,  faint,  feign, fictile,  fiction,  fictitious,  figure,  thigmo-,  the  first element  in  Tichodroma,  thixotropy  and  the second  element  in  paradise.
12381:Derivatives:  duet,  intr.  v.,  duett-ist,  n. duff,  n.,  boiled  suet  pudding.  —  Dialectal  pronun¬ ciation  of  dough.
12382:duff,  tr.  v.,  to  fake;  to  cheat.  —  Prob.  back  form¬ ation  fr.  duffer.
12383:duffel,  duffle,  n.,  a  thick  woolen  cloth  with  a thick  nap.  —  Du.  duffel,  fr.  Duffel,  a  town  near Antwerp.
12384:Derivative:  duffel,  adj.
12385:duffer,  n.,  a  fool.  —  Prob.  fr.  Scot,  dowfart, formed  with  pejor.  suff.  -art,  fr.  dowf,  ‘stupid’, lit.  ‘deaf,  fr.  ON.  daufr,  ‘deaf’.  See  deaf  and -ard.
37974:taboret,  also  tabouret,  n.,  a  small  tabor,  tabret.  — F.  tabouret,  dimin.  of  OF.  tabour,  ‘drum ;  stool’. See  prec.  word.
37975:tabret,  n.,  a  small  tabor.  —  A  var.  of  prec.  word, tabula,  n.,  table;  tablet.  —  L.  See  table. Derivatives:  tabular  (q.v.),  tabul-ate,  adj.  and tr.  v.,  tabul-at-ed,  adj.,  tabul-at-ion,  n.,  tabulat¬ or,  n.,  tabul-at-ory,  adj.
39280:forms  *timbene,  *timbne),  fr.  Gk.  Tup.7ravov. See  tympanum  and  cp.  next  word, timbrel,  n.,  a  kind  of  small  drum.  —  Formed  with the  dimin.  suff.  -el  fr.  OF.  tymbre,  ‘a  kind  of drum'.  See  prec.  word.
39281:Derivatives:  timbrel,  tr.  and  intr.  v.,  limb  reliv¬ ed,  adj.,  timbrel(l)-er,  n.
39562:toph,  n.,  a  small  drum  (music).  —  Heb.  toph, ‘timbrel,  tambourine’,  rel.  to  Aram,  tuppd,  of s.m.,  Arab,  duff,  ‘drum’ ;  of  imitative  origin. Tophet,  Topheth,  n.,  a  place  in  the  valley  of  Hin- nom,  south  of  Jerusalem,  where  children  were sacrificed  to  Moloch  {Bible).  Heb.  Topheth, prob.  formed  from  orig.  •Tlphath,  the  vowels  of which  have  been  assimilated  to  those  of  unrelat¬ ed  tSpheth,  ‘spitting’,  and  of  bosheth,  ‘shame’. Topheth  prob.  meant  orig.  ‘fireplace’  (i.e.  place
40589:tylosis,  n.,  1)  growth  of  one  cell  into  another ( hot .);  2)  thickening  or  hardening  of  tissue (med.)  —  ModL.,  formed  with  suff.  -osis  fr.  Gk. T'jXoc,  ‘lump,  knot;  any  swelling'.  See  tylarus. tymp,  n.,  the  top  of  the  opening  of  the  hearth  of a  blast  furnace.  —  Shortened  fr.  tympan. tympan,  n.,  1)  a  drum  or  a  drumlike  instrument (archaic)-,  2)  a  thin  sheet  of  paper,  parchment, etc.,  placed  between  the  platen  and  the  sheet  to be  printed.  —  ME.,  fr.  OE.  timpana,  fr.  L.  tym¬ panum,  ‘kettledrum,  timbrel,  panel  of  a  door’, fr.  Gk.  xu[i7ravov.  See  tympanum, tympan-,  form  of  tympano-  before  a  vowel, tympanist,  n.,  one  who  beats  a  drum.  —  L.  lym- panista,  fr.  Gk.  TU(J.7ravttJT7j;,  fr.  Top-xvi^eiv, ‘to  beat  the  drum',  fr.  TU|x7ravov.  See  tympan and  -ist.
40595:strike'.  See  type  and  cp.  tympan,  timpano,  tim¬ bre,  timbrel.
=== AFA duff ===
9932:K*113^I7 entlehnt sein, oj »Pauke" ist wohl Entlehnung
=== AFM دف ===
753:هدف السهم ܬ اصل اللفظة يونالي 90 
1307:(الَءَا) ضرب من الصدف الأشقر اللون قيل فارسي قلت وهو تعريب ܓ 
1891:1 ( ܐܚܝ 0 الضخم والطويل وااعالي تعريب 35 الذي ° ٠١‏ والجنادف 
2507:الذي <١‏ ودثيا م 0 أظلم . (وأدجى وتدجى وادجوجى ) :كل دف 
2541:* (الدردار) شجر عظي له زهر اصفر وورق شائك وثر كقرون الدفلى ( 2 
4094:لخدف )1-1 تعر يب حأروب ٠‏ والظاهر ان الكلمة ارامية ܝ 
5111:الدراء .< الاي تاليف جسلتيرسن): او من كم زا يدف الروك 
6309:ويدف 
7279:دف 6 
=== PLA daf ===
9582:- duff: "Tamburin, Handtrommel" aus dem pers..s,daf aram. TasR 
9586:sb) - daffaf: "Tamburinschläger" nom. agent. v.. duff s. duff. 
9636:223 - dufüf: Pl. v. duff s. duff.
```


## [2026-09-05T18:13:28.525Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9575,9595p' incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt\necho \"=== FVQ duff/daff ===\"; grep -n \"duff\\|daff\\|tambourine\\|tympan\" FVQ.txt | head -10",
 "description": "Asbaghi duff context, FVQ"
}
```


### [2026-09-05T18:13:28.590Z] TOOL RESULT

```
a) - dasta: "Finsternis" aus dem pers. 5», dab 11, 


12 
’ 


- duff: "Tamburin, Handtrommel" aus dem pers..s,daf aram. TasR 


_#b>»- dafätir: Pl. v. wo» daftar s. daftar. 
sb) - daffaf: "Tamburinschläger" nom. agent. v.. duff s. duff. 


2 - daftar: "Buch, Liste, Register, Material, Katalog, Ausgabenbuch, 
Album" pers. 2 mp. ro» daftar 14 ap. dipi "schreiben" od. 


akk. tuppi.- od. griech. Diphthera "Haut" 1° dtsch. Diphtera 1. 


=== FVQ duff/daff ===
```


## [2026-09-05T18:13:38.255Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nls -la BQT_v2_pages.txt; head -5 BQT_v2_pages.txt; echo ---; grep -c \"pdf page\" BQT_v2_pages.txt",
 "description": "Inspect BQT vol2 pages file"
}
```


### [2026-09-05T18:13:38.311Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4339896 Sep  4 14:06 BQT_v2_pages.txt
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
---
0
```


## [2026-09-05T18:13:39.861Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"داریه\" BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -10\necho \"=== شندف ===\"; grep -n \"شندف\" BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head",
 "description": "Grep BQT for dariye, shandaf"
}
```


### [2026-09-05T18:13:39.935Z] TOOL RESULT

```
=== شندف ===
incoming/BQT/BQT_v3_pages.txt:6886:‏شندفه - بفتح اول بر وزن اشرف »
incoming/BQT/BQT_v3_pages.txt:6922:‎A‏ تا پدر ‎FUE‏ برکه لوبت میمین شندف زند وزرین مزمار +
BQT_v2_pages.txt:1096:                              ‫بعنی پنشیند ‪.‬‬                ‫قومی باشندفرومابه وصحرا شین درهندوستان‪.‬‬
```


## [2026-09-05T18:13:49.371Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:869 2>&1 | head -60",
 "description": "Fetch BQT page 869"
}
```


### [2026-09-05T18:13:51.083Z] TOOL RESULT

```
no scan of BQT covers printed page 869 (see 'scans' in refs_online.json)
```


## [2026-09-05T18:13:53.662Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\"",
 "description": "BQT ref details"
}
```


### [2026-09-05T18:13:55.184Z] TOOL RESULT

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


## [2026-09-05T18:14:00.275Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 265 266 267; do echo \"########## leaf $L ##########\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n {print}' BQT_v2_pages.txt | head -70; done",
 "description": "BQT vol2 leaves around p.809"
}
```


### [2026-09-05T18:14:02.016Z] TOOL RESULT

```
########## leaf 265 ##########
                                                                                     ‫‪=A‬‬‫و‪‎‬‬




‫خیناگر = باکاف فارسی‌بروزن تیرآور‪.‬‬                ‫کردن وباد دربوق انداختن باشد‪ .‬که آنهم کنابه‬
                  ‫و‬    ‫ساز نده ومغنی را گومند ‪۳‬‬
                                                    ‫از برخاستن و برپایشدن آلت تناسل است ‪-‬‬
‫= بفتح واو بروزن بی‌خبر »‬        ‫حینو ر‬            ‫کونابه از فرودآمدن ومقیم شدن ولزول کردن‪.‬‬
                           ‫پل صراط رگاویند ‪.‬‬                           ‫ولشکر کشیدن و نوت نا‬
‫حو ‪ = ۴‬بسراول وسکون‌ثانی وواو‪,‬‬                      ‫خیم نزگادی ‪ -‬کنابه از آسمان‬
‫آب‌دهن راگوبند؛ وبفتح اول وضم ثانی‌هم‌درست‬
                                                                                         ‫است ‪.‬‬
                                        ‫اكت ‪::‬‬      ‫خیمه کبوه = بعنی خيمة زنکاری‬
                                                                           ‫است که آسمان باشد ‪.‬‬
‫حیوق * ‪ -‬بکراولبروزن زببق ‪.‬نام‬
          ‫ولاسی جک ازاولعای )‪ (۱‬خوارزم ‪¥.‬‬         ‫ن ینا سرودونغه هرا کومند ‪١.‬‏‬
                                                                               ‫خینا ‪ 5‬روز‬




                                                                  ‫)‪ ۱‬چك چش‪:‬الکای ‪.‬‬

   ‫(ھ‪ .‬م‪(0‬‬   ‫«چینود»‬    ‫_ مصحف‬   ‫‪۴‬‬         ‫خنبا کر‪.«(.‬م‪).‬‬   ‫سس‬          ‫رك‪ :‬خنبا ‪۵‬‬   ‫‪۱‬‬

   ‫= یوخ » یولهب ‪ ‹ 120016‬نامشیوه ‏‪٩۵۱۷‬و ‪12101‬‬                   ‫‏‪= X۷. e0 _ ۴‬ودخ‬
   ‫‪ - ۵‬کدثرب‌اسلامی‬                  ‫|تال‪ « 6708‬اسشق ‪۷۱‬ه»› رك‪ :‬خدو‪.‬‬
                                                                  ‫و‪. 25‬اوسا _ ‪ ۵۷۵2‬ن‬
                             ‫‪« xiwaq‬دائرة المعارف اسلام‪ .‬فراشه ج ‪ ۲‬ص ‪۳٩٩‬‏ ستون ‪.*۱‬‬
                                                                                   ‫خیوق ‏‬
                                                                  ‫‪ #‬خيوه ‏ رك‪ :‬خیوق ‪.‬‬

########## leaf 266 ##########
                                     ‫گفتار هم‬

 ‫از کاب برهان قاع در بیرف دال ہبی قطه با عروف پجی‬

 ‫مبتنی بربست و یك بیان و معتوی بربکهزار و صد و نهلفت‬
‫و يك انجام کهآنهممشتمل است برسیزده لے که‬                                        ‫و کنات‬

                          ‫اول آنا ذال قطه دار باشد‬
                                         ‫يان اول‬

      ‫در دال بی نقطه بالف مشتمل بر یکصد و شصت ونه لغت و کنات‬


‫مع»نی کر وفر | خندیدن باشد ‪ .‬و داباه‌انمی یعنی میخندم ‪.‬‬
                                                      ‫رودزن بباب‬
                                                               ‫* كباب‬
                     ‫وداباهانید بعنی‌بخندید ‪.‬‬                   ‫وکان وشو کت وخودنمامی باشد ‪:‬‬
‫وای هوز‬
      ‫دار ره = بفتح بای فارسی ز‬           ‫‪۰‬‬     ‫دا با‪ = ۱‬پروزن باب بلفت‌ز ندوپازند(‪)۲‬‬
‫زرسرخ وطلا گروابند ' و بعربی ذهب خوانند ‪ | .‬بر وزن واکرده » فراشتروك ‪ ۴‬باشد ‪ ۰‬و آن‬
     ‫خانها آشیان کند ‪.‬‬    ‫قف‬
                           ‫سکه‬‫رست‬
                                ‫دده‌ا‬
                                    ‫برن‬              ‫‪ -‬باهون‬              ‫دا باهانتن‬
‫دا بشلیم ‪ -‬بكر ثاك و سکون شن‬                    ‫بروزن سرتایاشکن» بلفت ز ند و یاز ند (‪ )۲‬بمعنی‬


                                  ‫(‪ )۲‬چك‪ :‬ژند ویاژند‪.‬‬           ‫(‪ )۱‬خم‪ : ۱‬کوذایت‪.‬‬
 ‫‪-‬رف دهم ازالفبای فارسی وحرف هشتم از الفبای‌عربی (ابتث) وحرف چهارم از‬
                                                                    ‫‪ #‬و ح‬
 ‫يدل شود (رك‪:‬‬   ‫چهار گرند ‪ ۱‬این حرف گاه به ات‬       ‫جمل؛‬   ‫ارود ‪ ۰‬و آنر ا «رال» نام‌ند و درحاب‬

 ‫ص بح دیباچة مولف)‪ .‬برای اطلاع از دال نمیر ‪ ,‬رك ؛ ص که ‪ -‬کو از دیباچة مولف ‪ ,‬و برای‬
                                                           ‫‪.‬‬   ‫یك‬
                                                                ‫رك ص یج ت‬      ‫فرق دال و ذال‬
                          ‫‪.‬‬   ‫رر ) طلا)«بونکر ‪FA‬‏‬    ‫‪ ۰‬بهلوی ‪raZ‬‏‬   ‫‪221 ۰‬‬     ‫‪ ۱‬هر‬

  ‫‪ - ۴‬هز ‪0 .‬ها‪ . 5(006۳(2)020‬بهلوی ‪ 02110087‬خندیدن «یوتکر‪۳۸‬بنابرین‬
  ‫‪ = ۴‬فراستوك (ه‪.‬م‪ = ).‬پرستوك (ه م!)ورك‪:‬فراشتروك‪.‬‬                   ‫اسل « دابا هوستن» است ‪.‬‬
     ‫‪ (۰‬برهای فاطع ‪) ۱۰۱‬‬

########## leaf 267 ##########
 ‫داد‬

‫داخم د بكر اك بروزن قاسم »‬                          ‫فرشت (‪ )۱‬ولام‌بتحتانی کشیده ویمیم زده » طایفه‬

                     ‫یمعنی رزق وروزی باشد ‪.‬‬         ‫وقومی اند که پادشاهی سومنات بدیشان مخصوص‬
                                                                                                 ‫است ‪١‬‏ ‪.‬‬
‫خاول ‏ باواومجهول بروزن شاغول‪.‬‬     ‫د‬
‫اهان باشن‬    ‫بمعتی داخل است ‪ ۷‬کبهاددر گشاه‬          ‫‪ -‬بادونو تایفرشت بر‬               ‫دنابتون‬
‫ودکه و سکوبرا نز گویند که بر درگاه اکار‬             ‫وزن بازو شکن » بلغت زند و پازند (‪ )۲‬بمعنی‬
‫وسلاطین بجهت شتن سازند ‪ -‬وعلامتی را فز‬                           ‫دادن باشد کهنقیض کرفتن است ‪.‬‬
 ‫گفته اندکه صیادان در صحرا نزديك یدام صب‬             ‫داتو بر ‪ ۴‬ب‪۰‬ا تای قرشت بوای‬
  ‫همی‬‫رابادا‬‫کنند تاصید از بآتنرسد و بج‬               ‫ابجد بر وزن جادو کر ‪ ۰‬بمعتی داور و دادری‬
‫شود‪ -‬وعیلیازمتی‌باشد که براطراف زراعت سازند‬                                                       ‫ماش ‪.‬‬
                  ‫بجهت منم وحوش وطیور ‪.‬‬
                                                    ‫كرجوز=ن‌تاج » شبتارك وتاریکی‬
                                                                               ‫ب‬
‫داحیدن = بروزن باشیدن » بممنی‌از‬
                                                    ‫گبورباند ‪ - ۴‬و بانشدید جیم درعربی مکاری‬   ‫ش‬
‫هم جدا کردن ‪ -‬ونظربرچیزی افکندن ودبدمور‬                                      ‫وتجار را خوانشد © ‪.‬‬
                                   ‫شدن باشد ‪.‬‬
                                                    ‫داچك(‪ -)۳‬بفتح جیم فارسی بر وزن‬
‫كاك = بروزن باد‪ .‬بمعنی عمروسن وسال‬                                  ‫گوشواره را گونند ‪۰‬‬       ‫»‬   ‫ناوك (ع)‬


‫آدمی باشد ‪ -‬ونام جوششی است با خارش یار‬              ‫‪۵‬احتن = بروزن‌ساختن؛ بمعنی داستن‬
‫که‌آنرا بعریی قوباکویند وبهندی یزاین علت‬                                                           ‫باشد ‪.‬‬
  ‫مهدمه‬
      ‫آان‬
        ‫‪-‬نی فریاد و فت‬
                     ‫بندمع‬
                         ‫را داد خووان‬
‫است ‪ -‬ویمعنی راستی و عدل وعدالت و اعدال‬             ‫داخل؟ ‪ -‬بثناملك بر وزن کاکل‪,‬‬
 ‫باشدھ ‪ -‬وتظلم‌ووارسیدن‪٩‬‏ وبهرمرا نکیزفتها‬                                 ‫در گاه یادشاهانر | گوبند ‪1‬‬




            ‫(‪ )۳‬خم ‪ :۱‬داچذ‪.‬‬          ‫(‪ )۲‬چك‪ :‬ژند ویاژند ‪.‬‬               ‫(‪ )۱‬چك‪ :‬قرشت ‪.‬‬
                                                               ‫بروزن ناوك ‪۰‬‬   ‫‪۳‬‬   ‫)‪ (£‬چش‪:‬‬



  ‫ائثل‬   ‫‏‪ =١‬دیشليم » نام بادشاهی ات که درکمله ودمنهٌاین المتفع ( چاپ محمد حن‬

                                                              ‫المرصفی ‪ ۷۲۹۱‬م ص(‪ )۹۲‬آمده ‪.‬‬
  ‫‪ - ۴‬داج و داجی (عر ) آز مصدر‬                ‫‪ .‬رك‪ :‬داور‬    ‫بپلوی است‬    ‫‪۴‬‬            ‫«بونکر “‪FA‬‏ ‪.‬‬

  ‫(عر) «داج‌شد جیمء خرباده‌ها ویادم‌های‬         ‫©‬          ‫دجوبمعنی تاريك شدست‪« .‬شرح قاموس»‪.‬‬
  ‫شحنه و بازرگانانندو ازابن است حدیث ‪ :‬هولاءالداج‌ولیوا بالحاج » بمنی پستند حج کزارنده‬
   ‫‪ ۰‬ر=اخوز(«‪.‬م‪).‬‬             ‫بلکه کرابه کش و بداده های شحنه وبازرکانانند‪« » .‬شرح قاموی» ‪.‬‬
   ‫‪ _ ۸‬بهلوی ‪( 120‬قانون) «مناس ‪۱۷۲:۲٥‬‏ ‪ ۰‬یارسی باستان ‪-‬‬                  ‫رك‪ :‬داخل ‪.‬‬      ‫‪۲‬‬
  ‫(قانون» دستور) (ازرشة‪)20202 ۰ 20 .‬؛ اومتاها‪( 2‬ازرسة ‪4d.‬‏ ‪, 1412020‬‬       ‫‪2‬‬
  ‫ارمنیع ‪ » 3‬قس‪ :‬هندی باستان ‪( 02018111 -‬فانون؛دمتور)( ازرسةٌ ے‪0‬ل ‪,‬نا‪4‬طقه) ‪.‬‬
         ‫لب رگ “‪o‬‏ رکه ‪ :‬ح ‪٩‬‏ ‪-‬‬        ‫‪۶‬ارتولمه ‪۹۲‬‬
                                                 ‫« اسدق ‪ » ۸۱0‬ب‬               ‫کردی و افعانی ع ‪0‬‬
                                                                 ‫‏‪ - ٩‬بدو معنی آخیر ‪:‬‬
         ‫و کرتومي ندهی‌داد > روز دأدی صست‪.‬‬           ‫ز کوش پنبه برون‌آر وداد خاق بده‬
   ‫«کلتان ‪. ۹16‬‬
```


## [2026-09-05T18:14:12.826Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\ntxt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=txt.split('\\f')\nwords=['درخت','دارو','دارکوب','درودگر','درود','درست','بدرود','درونه','داریه','دف','درگر','دار ']\nfor w in words:\n    hits=[i for i,l in enumerate(leaves) if w in l]\n    print(w, '->leaves(printed≈leaf+543):', [(i,i+543) for i in hits][:25])\nEOF",
 "description": "Locate BQT leaves for Persian headwords"
}
```


### [2026-09-05T18:14:14.423Z] TOOL RESULT

```
درخت ->leaves(printed≈leaf+543): [(12, 555), (15, 558), (23, 566), (24, 567), (26, 569), (39, 582), (40, 583), (41, 584), (43, 586), (50, 593), (54, 597), (62, 605), (77, 620), (91, 634), (97, 640), (107, 650), (114, 657), (118, 661), (119, 662), (121, 664), (125, 668), (128, 671), (134, 677), (135, 678), (146, 689)]
دارو ->leaves(printed≈leaf+543): [(18, 561), (22, 565), (23, 566), (26, 569), (27, 570), (29, 572), (44, 587), (64, 607), (91, 634), (95, 638), (96, 639), (98, 641), (103, 646), (116, 659), (117, 660), (122, 665), (126, 669), (139, 682), (144, 687), (160, 703), (163, 706), (164, 707), (168, 711), (186, 729), (191, 734)]
دارکوب ->leaves(printed≈leaf+543): [(272, 815)]
درودگر ->leaves(printed≈leaf+543): []
درود ->leaves(printed≈leaf+543): [(158, 701), (258, 801), (300, 843), (301, 844), (303, 846), (304, 847), (305, 848), (308, 851), (424, 967), (500, 1043), (555, 1098), (594, 1137)]
درست ->leaves(printed≈leaf+543): [(12, 555), (26, 569), (31, 574), (34, 577), (35, 578), (94, 637), (103, 646), (108, 651), (113, 656), (128, 671), (153, 696), (168, 711), (171, 714), (172, 715), (184, 727), (187, 730), (197, 740), (202, 745), (209, 752), (213, 756), (214, 757), (221, 764), (233, 776), (234, 777), (236, 779)]
بدرود ->leaves(printed≈leaf+543): []
درونه ->leaves(printed≈leaf+543): [(571, 1114)]
داریه ->leaves(printed≈leaf+543): []
دف ->leaves(printed≈leaf+543): [(2, 545), (13, 556), (16, 559), (22, 565), (23, 566), (24, 567), (28, 571), (30, 573), (39, 582), (40, 583), (44, 587), (47, 590), (65, 608), (76, 619), (77, 620), (81, 624), (83, 626), (96, 639), (97, 640), (98, 641), (99, 642), (106, 649), (113, 656), (115, 658), (120, 663)]
درگر ->leaves(printed≈leaf+543): [(102, 645), (597, 1140)]
دار  ->leaves(printed≈leaf+543): [(10, 553), (15, 558), (17, 560), (18, 561), (19, 562), (23, 566), (24, 567), (25, 568), (28, 571), (33, 576), (36, 579), (40, 583), (41, 584), (45, 588), (47, 590), (54, 597), (55, 598), (56, 599), (57, 600), (58, 601), (60, 603), (61, 604), (62, 605), (68, 611), (69, 612)]
```


## [2026-09-05T18:14:22.280Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 300 301; do echo \"########## leaf $L (p≈$((L+543))) ##########\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n {print}' BQT_v2_pages.txt; done",
 "description": "BQT leaf 300-301"
}
```


### [2026-09-05T18:14:23.868Z] TOOL RESULT

```
########## leaf 300 (p≈843) ##########
        ‫رح‬

 ‫ولام وسکون‌الی‬      ‫در لك ‪ = ۳‬تکراول‬                         ‫در لك = بقتح اول بروزن قدك‪,‬دستارجه‬
‫وکاف ‪ .‬جام کوناه قد آستن کوناه پیش واز را‬                 ‫رگاونند که رومال ورویاك باشد ؛ و باين معثی‬
                                               ‫وتف‬        ‫بجای حرف انی زای نقطه‌دار همأ مده‌است‪ -‬ودر‬

 ‫در لورینه سیر خوردن ‪- ۴‬‬                                                               ‫عربی مممنی مال باشد ‪.‬‬

‫کنابه از فرب خوردن ‪ -‬و کردن‌کاری باشد" که‬
‫عمش کنن را منخص سازند ‪ -‬ویمعئی درشادی‌غم‬                  ‫‪ ۰‬و عصی یخی را گوند که درزیر‌ناودان‬           ‫گوند‬

                                                                                                     ‫به ود‬
‫کنابه‬              ‫در لور بنه سیر دآدن‬                        ‫‪3‬ممنی‌ابن ات‬
                                                                         ‫در کحامی خو ر ۔ب‬
 ‫کاازری‌باشد که عش کے رابرهم زنند ‪ -‬وفریب‬                 ‫‪٩‬‏ عدی‬     ‫است‬   ‫و کی درخور‬       ‫هی زد‬     ‫که کسا‬

 ‫خوردن ازکی ‪ -‬ودرعین شادی غم‌پیش آمدن‌را‬                                                             ‫می زسد ‪.‬‬
                                         ‫نز گوند ‪۰‬‬
                                                              ‫از نتوشدن‬          ‫در کشیدن ه کنابه‬
 ‫در ليك ‪ = 3‬یکراول ولام وسکون‬                             ‫محو کردن ‪ -‬و رد نمودن‬               ‫‪-‬‬   ‫و سر کدن‬
 ‫ثالی و تحتالی و کاف» به‌عنی‌در (اكاست کدقبای پیش‬                                                      ‫باشد‪¥ .‬‬
                           ‫واز آستن کوناه باشد ‪۶#.‬‬
                                                          ‫‪ -‬باکاف فارسی بروزن دختر »‬           ‫در گر‬
‫در ها ۔ بروزن سرما » خ رکوش را‬                                                             ‫درود کررگاویند ‪.‬‬
                                           ‫گومنت ‪:‬‬        ‫در لاله = بفح اول و صکون ثالی‬
 ‫»ج دووا‬
       ‫لا‬‫عمان‬
            ‫دروزن فر‬
                   ‫درهان ب‬                                 ‫وضم کاف فارسی ولام الف ولام مفتوح » بمعنی‬
‫ودار‌باشد ‪ - ۷‬ویمعتی درمالده ‪ -‬واهر باینمعنی‬               ‫کدارله است که بخ زبرناردان‌باشد وآن درهوای‬
                                ‫همت ‪. ۸‬‬   ‫ه‬                                ‫سرد ث کل مخروطی بسته مشود ‪.‬‬

   ‫‪3‬‬    ‫رك‪:‬دراہك‬     ‫‪۴‬‬         ‫مخفف «در و کر » = درو دگر‪.‬‬       ‫‪۴‬‬            ‫‪ ۱‬رك ‪ :‬در کلاله ‪.‬‬
              ‫در لك ‪۰‬‬    ‫رك‪:‬‬    ‫‪1‬‬          ‫‪.‬‬   ‫رل‪ :‬مادةٌ قل‬    ‫‪_ ۵‬‬           ‫‪.‬‬    ‫‪ - ۴‬رك‪ :‬هاده نمف‬
   ‫« بارتولمه ‪٩ ۴۹۹‬‏ ‪ ۰‬قس‬           ‫‪ - ۲‬بهلوی ‪ « 03۳۳۳1‬منای ‪۱۷۲٩‬‏ از ربت ‪۲2 -‬‬
       ‫‪ - ۸‬از درماندن؟‪.‬‬        ‫بر منیع ‪ 027۲721‬نیب ک‪ »:۹‬ورك‪ :‬اسثق مهوبشمان‪4۵‬ه ‪.‬‬                          ‫‪1‬‬
       ‫‪ #‬درگاه ‪ -‬بفتح اول » از ‪ :‬در ‪ -‬گاه (پوند مکان ) » پهلوی ‪( 8487310‬دائرة لمعارف‬
  ‫اسلام ‪ :‬در) ‪hãûgrid ۰‬‏ «تاواد‪:‬ا‪ » ۹۵۱‬معرب آن درقاعة « دزی ح‪۱‬صی ‪۵۳٤‬‏ » ودر گاه « ابا‬
  ‫ص ‪۲۹: ۷۳4‬؛ بار گاه ‪ .‬در‪,‬ار» سرای وادشاهی » دبوان ملطاتی ‪ « :‬یکی ازملوك عجم شنیدم که‬
   ‫مته‌لقان را همی کفت که مرسوم‌فلان راچندانکه هست مضاعف کد که ملازم دگراه است ومترصد‬
                             ‫د‪-‬ر » درواژه ‪-‬آستانهٌ در» حشرت ‪.‬‬
                                                            ‫*تان ‪* ۷4‬‬   ‫فرمان ‪.‬‏ گل‬
  ‫‪ #‬درم ‪ -‬بکراول وفتح دوم پهلوی ‪ « 772۳1‬منای ‪ ۱۷۲:۲۰‬و ‪ < 0۳5201‬تاوادیا‬
  ‫ازیونانی ‪« 8×۵۲‬نبرک ‪۸‬ه“ معرب آن درهم (بک راول وفتح سوم )؛‬       ‫‪ ۰۶‬و ‪.‬‬
   ‫واحد سک قره (وزن و ‪:‬بای آن درعصرهای مختلف» متفاوت بوده است) ‪ .‬رك ‪ :‬دار المعارف‬
  ‫اسلام ‪ :‬درهم ‪١‬‏ ورك‪ :‬دزیح اص ‪ ۸۳‬واحدوزن ‪ :‬معادل شش‌دانگه(هر دانگ معادل درفراط)‬
                                          ‫«ناطم الاطبا» ورك‪ :‬دائرة لمعارف اسللام‪ :‬درهم ‪. ۲‬‬

########## leaf 301 (p≈844) ##########
 ‫دروا‬                                                                                                      ‫ب‪۱‬ح‬


‫گونشد‪ -‬و نمعتی وقت‬      ‫‪ ۹۳‬وهللا کت راز‬    ‫ومحنت ‪6‬‬         ‫ين‬
                                                            ‫اول و فستح‬              ‫در مسرا اتاک‬
‫وساعت وزمان باشد ‪ - ۱‬ویم‌نی‌ئبات وآرام ‪١‬‏ ۔‬                             ‫باشد‬   ‫‪٤‬‏ دار المرب وضرانخانه‬   ‫می‌قطه(‪)۱‬‬

‫وتأخبرهم هت ‪ - 1‬وعالمآ خرت رانز کفته‌اند‪-‬‬
                                                          ‫‪-‬ف فارسی ‪ ۰‬صراف‬
                                                                        ‫دبرمنگ‌زفکنا‬
‫نمام ‪(۱۲‬‬       ‫درکات‬     ‫اشاره است‬     ‫و ترد موقن‬
                                                                                                         ‫را گویند ‪۱‬‬
 ‫محبوس‌ودن‪.‬‬     ‫بازماند گان و بقمد تغیدات وهمی‬
                                                           ‫درمل = بورزن بلبل » غله رکاویند‬
‫دنرگیدان‪ ۷‬د بکراول‪ .‬بعنی‌درنگه‬
                                                          ‫که هنوز خوب نرسیده باشد وآنرا بربان کنند‬
‫کردن است که ثبات و آرام ورز‪,‬دن ‪ -‬وتأخیر‬
                                                                                                          ‫وخور ند ‪.‬‬
                                       ‫کردن باشد ‪.‬‬
                                                          ‫در میان بودن = بمعئی در رهن ودر‬
‫نون‬     ‫بفتح‬     ‫زهادن =‬        ‫در ورد‬
                                                                                 ‫گروبودن باشد ‪.‬‬
‫و واو ک»نابه ازدرهم پیچیدن ‪ -‬و ینهان کردن‪-‬‬
‫و بی نام و تان ساختن ‪ -‬و در ‪-‬وراخ نهادن‬                   ‫درن = بالون وحرکت‌غیرمعلوم» زلورا‬
                                               ‫باشد ‪.‬‬
                                                          ‫در‬    ‫و‬       ‫کویند اکر او را خعك ساز ند‬         ‫بکشد و‬

 ‫كر نه س بکراول وسکون انی فوتح‬                            ‫شیشه کرخانه بخور کنند هرشيشة کبودی که در‬
          ‫ثالث » تبغ وشمشیر آبدار راکوبند ‪2.‬‬                                     ‫آنجا باشد بشکند و باقی نماند ‪.‬‬
‫در وا = بفتح اول وسکون انی و واو‬                          ‫در ند د بروزن سمند » بمعتی شکل‬
‫سردان و حیران‬
            ‫بالف کشیده » س رکشته و ک‬                      ‫ودمایل وصورت ومانندوسان‌باشد چتانکه گویند‬
‫باشد ‪ - ۸‬وسرنگونآو‪.‬خته ونگون وبا کونهرا‬                                  ‫فلك درند یعتی فلك سان و فلك مالند‬

‫یز کویند ‪- 4‬وچیزی‌ذرورقوحاجت ومابحتاجرا‬                   ‫در نگ = بکر اول بروزن فرنگ ‪۰‬‬
‫هم گفته‌اند که‌دروایست باشد® ‪-‬ونامفرشته‌است*‪۷‬‬              ‫صدایی‌باشد که اتزواختن ناقوس وتارسازوشکستن‬
‫کونایه ازهاروت وماررت همهت ‪ -۱۷‬وض‌اول‬                     ‫دلج‬       ‫و‬      ‫آن برآید ‪۴‬‬     ‫امثال‬   ‫و‬   ‫وآبگنه‬   ‫چینی‬




                                               ‫(‪ )۷‬چك‪ :‬زمائم ‪.‬‬                   ‫(‪ )۱‬چك‪ - :‬بی‌شقطه ‪.‬‬

  ‫در گت‬    ‫د بر ند(«‪.‬م‪۳ ).‬‬      ‫‪۳‬‬
                                                               ‫‏‪ - ١‬لفة بمعنی‌جابکه درم باشد‪.‬‬
   ‫‪ - ۱‬بباوی ‪80۵۲1‬‬                     ‫‪ ۵‬بانن حعنی «ریگ» انت‬                        ‫‪.‬‬   ‫اسم صوت‬   ‫‪_ ۴‬‬      ‫(«‪.‬م‪.).‬‬

  ‫( دراز ‪,‬آهسته) «مناس ‪ »۱۷۲:۲‬و‪arêd 8‬‏ «اونوالا ‪,nÃmazZ ۹۷۱‬‏ ‪:( 832۲61‬مان درز(‬
  ‫و ‪( 81۵۷1-802۲۵‬خداوند و صاحب زمان طویل ) » اوستا ‪êhgarad . (302۳09۷‬‏ _‬
  ‫«بارتولمه ‪« 1۹16‬نبر که › وأ‪( ۵92۲610۵۷۳22 - 20۵۳2‬زروان(زمان) یابدار)‪ .‬رك‪:‬‬
               ‫‪ Henning,‬ظ‪ .‬‏‪W.‬‬            ‫‏‪۵۷۲ Central Asian Words {¢Philological‬‬
   ‫‪.‬ص ‪droftreH 6491,‬‏ ‪.)yteicoS‬‬                   ‫ورك‪ . :‬دیرند ‪451 .‬‬
                       ‫رك‪ :‬اندروای ‪.‬‬       ‫‪۸‬‬            ‫ب‏دن (یسوند مصدری) ‪.‬‬
                                                                           ‫‪ ۷‬از‪ :‬درتك ‪٣‬‬
  ‫‪« -۶‬وا» نام فرشته (باد)‬                  ‫‏‪ - ٩‬رك‪ :‬الدربای‪ .‬اندربایستدربا دربای» درباست‪.‬‬
   ‫رك‪ :‬سار‬       ‫_‪١١‬‏ چون اروت وماروت طبق داستانما درچاه بایل‌مملفند ‏‬                            ‫امت ‪ .‬رك‪ :‬باد ‪.‬‬
                                       ‫تاهید با داستان خرداد و امرداد بقلم نگارنده ‪ ۰‬قهران ‪ .‬ص ‪. °۱‬‬

   ‫‪ #‬درو ‪ -‬یکس اول وفتح دوم ‪ ۱‬رك ‪ :‬درودن ] ‪ :‬چیدن له » بدرن‌علف و غلهٌ رسیده‬
                                                       ‫وبا لیم ری با دای وداسفاله‪ ,‬حصاد ‪.‬‬
```


## [2026-09-05T18:14:32.459Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 302 311; do echo \"########## leaf $L (p≈$((L+543))) ##########\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n {print}' BQT_v2_pages.txt; done",
 "description": "BQT leaves 302, 311"
}
```


### [2026-09-05T18:14:34.064Z] TOOL RESULT

```
########## leaf 302 (p≈845) ##########
  ‫‪~A‬‬                                                                                              ‫حره اج‬

                                                      ‫فام سلاطین وبزرگان هندوستان است ‪ -‬وبمعنی‬
                                                      ‫درست وتحتیق هم‌آمده است‪ ۷‬؛ ودروای باضافة‬
                                                                                     ‫تسانی تدز گفته‌اند ‪۰‬‬
‫باشد کهبر دو طرف راه از برای شان فرسنگك‬
                                          ‫صاز لد ‪.‬‬    ‫درواخج ‪ = 5‬بفتح اول وسکون آخر‬
                                                      ‫قطه دار باشد » حالت برخاسن از‬              ‫که خای‬
 ‫درو انه = بر وزن پروانه ‪ ۰‬سوراخی‬
‫باشد که بربام خانه کنند واردیان برآن گذاشته‬            ‫بیماری باشد که بعربی نقاهت گوبند و‪-‬بمعنی‬
                                                      ‫شجاع و دلیر ‪ -‬و شجاعت ودلیری ‪ -‬و محکم‬
                            ‫برالوالد ویزیر ایند ‪.‬‬
                                                      ‫ومضبوط ایزنگدفتسهو‌ایمعنی‌بقین ودرست وتحقیق‬
 ‫درواه ‪ = 1‬بر وزن درگاه " بمعنی‬                      ‫همرت کهلقیض کمان باشد ‪ -‬و بمعنی درشتی‬
          ‫سرلگون ‪ -‬وحبران ‪ -‬وضروری باشد ‪*.‬‬            ‫؛ و بجای حرف‬        ‫و علظت نیز (‪ )۱‬آمده ات‬

 ‫دروابست ‪ = ۳‬بروزن ومعتی‌دریاست‬                       ‫تائی زای فارسی هم گفته‌اند ‪ -‬وعیب وعار رایز‬
                                                                                                  ‫ّي‬
             ‫باشد که ضروری ومایحتاج است ‪.‬‬
‫درو بطارس ‪ ۰ ۵‬بح اول و ثالی‬                           ‫درو ار ‪ - ۲‬بر وزن خروار » بمعنی‬
 ‫بواو رسیاه کوسربای ابجد (‪ )۳‬وطای حطی(‪)4‬‬              ‫درواب تاست که‌خروریومابستاح باشد‪.‬وسرگشته‬
 ‫ھا ن هر دو‬      ‫و ن‬    ‫ورای مکور‬      ‫بالف کشده‬
                                                                  ‫وسرنگون وحىراقرا همگویند ‪¥.‬‬

                                                      ‫بقتح اول ‪ 3‬سکون آخر‬            ‫از ‪۳‬‬       ‫درو‬

 ‫وآن بشتر بر درخت بلوط کپنه پبهیده شود ‪.‬‬              ‫که زی فارسی باشد » بمعتی دروار است که‬
‫اکرآنرا باشاخ وب رک وبیخ بکوبند و بربیغ‬               ‫وبمعنی‌سررنگون‌هم‬    ‫و مایحتاج ود ‪-۴‬‬            ‫خروزی‬
‫و فالج و لقوه‬    ‫»‬   ‫ضماد کنند موی را سرد‬      ‫موی‬                                               ‫هنت ® ‪.‬‬
                                  ‫‪۰‬‬   ‫را هفك است‬


 ‫درو ‪ - 3‬بروزن سرود » بمعنی صلوات‬                                                           ‫کوش باشد ‪.‬‬
 ‫ات ‪٩‬‏ خکدهاابزتمالی رحمت و از ملابکه‬                 ‫کنابه از دهان‬       ‫نو ش ‌‬       ‫درو ارة‬


          ‫(‪ )۳‬چك‪ :‬کوسربا ‪.‬‬             ‫(‪ )۲‬چش‪ :‬درواز ‪.‬‬              ‫بنظر ‪.‬‬     ‫‪+‬‬     ‫)‪ (۱‬چك‪:‬‬
                                                                             ‫وطا ‪۰‬‬   ‫)‪ (4‬جك‪:‬‬


                     ‫«رژواخ» (ھ م( ‪۰‬‬    ‫‪ _ ۴‬ظ "ممحف‬            ‫‪ - ۱‬رك‪ :‬دژواخ » درواخ ‪.‬‬
          ‫فس‌«دروای»‪ .‬رك‪ :‬دروا » دروایت ‪.‬‬       ‫‪۴‬‬          ‫مصحف ‪ ۶‬دروای» (ھ م‪).‬‬             ‫‪۳‬‬
                       ‫‪ = ۹‬رك‪ :‬دروا ‪ ۰‬دروای‪.‬‬              ‫قس‪« :‬رروای» ورك‪ :‬دروا ‪.‬‬          ‫®‬
   ‫‪ - ۸‬بونانی ‪ « 51۲6000۳21‬اشتینگاس»‬                          ‫‪ = ۷‬دربابت (هم‪. ).‬‬
  ‫هو‬     ‫‪ ۳‬آرامش) «مناس ‪۷‬‬      ‫(صحت‬    ‫‪ ۹‬ك بهلوی ‪tûrd‬‏‬            ‫‏‪۰۸۷ «Al» Dryohtéris‬ص ‪.‬‬
  ‫سمادت «اووالا ‪ 4۳۱‬و‪( 6۵۳1‬آرزوی خبروبرکت) ازرشة)‪( ,212۷1۷۳0‬ارمنیع ‪taurd‬‏ («‬
   ‫‪0‬زاوستا ‪« 202۷۳)-‬بارتولیه ‪۲۸۷٩‬‏ لب رک ‪۹٥۰‬‏ وکره‪ :‬اسشق وهوشمان‪0۵‬ه‪.‬‬
                                                                   ‫ا‬ ‫‪46‬‬
       ‫زامیر) کیلکی ‪ 6222۷731۰‬فنریدزی‬
                                    ‫کلوج‬
                                       ‫‪ ۵‬دروازه ‪ -‬بفتح اول وکر پنجم (در‬
       ‫وبرنی و نطنزی ‪ « 8227۷۳81‬ك ‪۱ .‬ص ‪ ,» ۹۸۲‬سمنانی وشهمیرزادی ‪ , 8227۷۳21‬سنگری‬
                      ‫‪ , 682‬سرخهیی ‪ .۵« 6872۷۳31‬ص‪ ۸۸۱‬؛ در برزگے » درب ‪.‬‬
                       ‫‪ ۵‬دروای ‪ -‬بفتح اول » کرے‪ :‬دروا » اندروای ‪ .‬وفاب اص ‪. ۹۲‬‬

########## leaf 311 (p≈854) ##########
                                                               ‫يان هشتم‬
                    ‫در دال بی‌نقطه با زای فارسی مشتمل بر سی وهفت لغت‬


‫دزاامه ه = بکر اول وفتح آخر‬                                                  ‫‪ = ۵‬بکر اول و سکون ثالی » قلمه‬
 ‫بمعنی دژکام ات که زاهد ویرهیز کار )‪(٩‬‏ ‪-‬‬                                    ‫وحصارباشد ‪- ۱‬وبمعلی زشت و‪,‬دوبدخوی وخشم‬
‫وخواجه‌سرا باشد ؛ وبفتح‌اول لز درست است‪.‬‬                                        ‫نزد‪-‬‬
                                                                                   ‫انی‬
                                                                                     ‫‌را‬
                                                                                       ‫هکی‬
                                                                                         ‫تند‬
                                                                                           ‫فبب‬
                                                                                             ‫گوچ‬
                                                                                               ‫وقهر نیزهست ‪- ۴‬‬
‫دز ] اه ‪ ۱‬ت باها بمعنی درآ پاداست‬
‫که سهمگن وخشمآ لود باشد ‪ -‬وبداندش وتند‬                                                                                   ‫‪۰‬‬    ‫است‬   ‫درست‬   ‫قىر‬




‫شده رانیز کرد ‪ -‬کووتوال و محافظت کنندة‬                                       ‫و دال‬         ‫ایجد‬     ‫با بای‬        ‫دژ] باد ‪ ۴‬ت‬
                                    ‫ذلعه را هم گفته‌اند ‪۰‬‬
                                                                             ‫بر وزن اشارات » بمعنی سهمگین و خشم آلود‬
‫دز | گه »مخنف دگژاآه است ‪ ۷‬که‬
‫خشمکن وقهرناك و‪-‬بداندیش ‪ -‬وکوئوال قلمه‬
                                                                                                                                    ‫&‬

                                                                             ‫درا گام ‪ = ۴‬با کاف فارسی بر وژن‬
                                                               ‫باشف‬          ‫زاهد‬         ‫و یمعتی‬         ‫دلارام »خواجه سرا را کت‬
‫بععتی‬      ‫دل»‬
             ‫لزونک‬
                 ‫آبرو‬
                    ‫دز ] لو ‪ ۸ ۵‬س‬                                                                           ‫ویرهیز گار همآمده است ‪.‬‬

                                                      ‫چش ‪ :‬برهیز کار ‪.‬‬              ‫(‪)۱‬‬               ‫‪.‬‬    ‫‪-‬ست‬
                                                                                                             ‫(‪ )۱‬چك‪ :‬ا‬

  ‫‪ ۹۳ ۳‬بابن معنی لفة بضم اول‌سحیح است»‬                                      ‫اسلام ‪۰‬‬       ‫و دائرة المعارف‬        ‫دز‬    ‫رك‪:‬‬      ‫‪۱‬‬


     ‫‪.‬هلوی ‪. 01511 -‬هندی باستان_ ‪5100‬‬
                                    ‫دژ= دش » پارسی باستان _ ‪05‬لا " اوا ‪ 5110 -‬ب‬
 ‫دشنام ‪ ۰‬دشمن ) ودو ا گاه) آمده‬                  ‫ِ دزخیم ‪a‬‏‬           ‫مر کب بل‬            ‫‪ ۰‬در کلمات‬       ‫‪020 -‬‬       ‫‏_‪ ۰ dur‬آرئی ‪2‬‬

 ‫آنجاکه از بدی‬              ‫آباد " لفة »‬   ‫) ‪+‬‬        ‫ح ‪۲‬‬       ‫از ‪ :‬دژ (بضم اول ‪ .‬رك ‪:‬‬                   ‫‪- ۴‬‬                ‫اسشق داه“ ‪.‬‬
 ‫دژا کام‪۰ ‎‬‬       ‫‪ ۳۳‬ره ‪:‬‬   ‫‪o‬‬               ‫‪۰‬‬   ‫دژکامه‬     ‫‪۰‬‬    ‫درکام‬   ‫‪۰‬‬     ‫امه‬
                                                                                ‫رك‪ :‬دکژا‬             ‫‪۴‬‬                ‫وخشم معمور است ‪.‬‬
 ‫)‬      ‫»مر کب از ‪ :‬دژ( حرش‬                ‫«مناس ‪YT‬‏‬                  ‫‪ - ۷‬پهلوی ‪sãkãhsud‬‏‬                                ‫درکام ‪ ۰‬درکامه ‪۰‬‬




                     ‫چو بل در آ گاه ودرنده شس‪.‬‬                                              ‫سوار جپان نبوزار دلیر‬
 ‫دقیقی طوسی‪« .‬مزدیبنا ‪4۵۳-۵۵٩‬‏ ‪.‬‬
                  ‫دژ ( رکه‪ :‬ج ) ‪ +‬آلود (لوآده) ‪.‬‬                            ‫ز‪:‬‬
                                                                             ‫‪۸‬ا‪_۵‬‬                   ‫‪ :‬د؟آ گاه ‪۰‬‬        ‫رک‬       ‫‪۷‬‬


                                                                                                                ‫بقه اصزفحهٌ ‪۰۵۸‬‬
                  ‫(سارق) ‪ ,‬بپلوی ن‪0‬ز‪2 = ( 60‬یا ) ‪.‬‬                                    ‫اسشق ‪41۵‬؛ دراوراق‌مانوی بپپلوی ‪20‬‬
                  ‫‪Henning. A list of Middle‬‬                                   ‫‪Persian .. , BSOS‬‬                        ‫‏‪126, p. 82.‬‬
  ‫کسکه‬        ‫ب‬    ‫صارق‬     ‫ِ‬   ‫‪٩‬‏‪zûd ۳‬‬           ‫‪۳‬‬    ‫‪€‬‬       ‫‪۸۷‬‬     ‫گربرسن‬          ‫‪۶‬‬    ‫‪0۵0۳2‬‬          ‫وخی‬      ‫‪,‬‬           ‫اشکآشمی ‪0‬‬


 ‫دزدان عرب بر سر کوهی نشته بودند و منفذکاروان بسته »‬                                               ‫ق‪:‬‬
                                                                                                  ‫ةٌ‬ ‫بزن‬ ‫ط» ر‬
                                                                                                       ‫ااه‬     ‫مال مردم را بب‬
                                                                                                             ‫«رد‬
                                                                                                                         ‫«گلتان ‪. ۱۲‬‬
 ‫‪#‬زدیدی ‪ -‬بض اول و فتح پنجم ‪ ,‬از ‪ :‬دزد ‪-۳‬بدن ( پود مصدری ) ؛ سرقت »‬
                                                                  ‫د‬
                                                                                                                       ‫بردن مال مردم ‪.‬‬
```


## [2026-09-05T18:14:58.449Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=txt.split('\\f')\nimport re\nfor i in range(294,313):\n    l=leaves[i]\n    for m in re.finditer(r'.{60}ونه.{60}', l):\n        print(i, i+543, repr(m.group(0)))\nEOF",
 "description": "Find darune in BQT leaves 294-312"
}
```


### [2026-09-05T18:15:00.202Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T18:15:05.724Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=txt.split('\\f')\nimport re\nfor i in range(290,335):\n    l=leaves[i]\n    for w in ['درست','دف','درونه','درون','دارو']:\n        for m in re.finditer(r'.{0,50}\\b'+w+r'\\b.{0,80}', l):\n            s=m.group(0).replace('\\n',' ')\n            print(i, i+543, w, '|', s[:150])\nEOF",
 "description": "Scan BQT leaves 290-335"
}
```


### [2026-09-05T18:15:09.940Z] TOOL RESULT

```
295 838 درون |  ‫درون ‪ - ۱‬بروزن‌ارزن» به‌منی سوزن‬
296 839 درست |                ‫یمعنتی عفو ورحمت‬                ‫درست ؟ د جنم اول و ثاسبیکوون‬
296 839 درست | نی‌باستان» قرب ‪ithsrd-urd‬‏ ‪( L_ithsrd_avurd# #‬درست‪.‬سالم)‬
296 839 درست |              ‫جهل درست است وخرد دردمند‪.‬‬                                            ‫تاکه دگ رگونه ش
296 839 درست |      ‫‪ - ۴‬درست آمدن ""صادقآمدن‪,‬صحیح‬                                 ‫س ص‪۰۱۲٥‬‏ بنقل از شاع
296 839 درست | ‬                          ‫جکلروهدن‪ ':‬قول< کما درست آلمدکده گ‬
296 839 درست |    ‫رك‪:‬‬     ‫‪۷‬‬                 ‫‪- ۷‬رکه‪ :‬درست (درهم‌ودینار) ‪۰‬‬                           ‫‪6‬‬
296 839 درست |   ‫آمنای‪” 016100۱۳0 ۷۲:۲۰ ۲‬یبر گے ‪ , ۰۹‬از‪ :‬درست (هام‪ + ) .‬ی‬                                                 ‫(صحت)‬
297 840 درست | ‫پنجره‌دار باشد؛ وبا بای فارسیتا کن‌هم‌درست است‪.‬‬                           ‫وخجلت کشبدن و شرمنده شدن باشد ‪.‬‬
298 841 درست | یر پپلوی «کاو درفش » بعنی علمگاو آءده ‪ .‬ابن لغت درست یادآور درفش کاوبانی‌است که‬
302 845 درست |                                                  ‫درست وتحتیق هم‌آمده است‪ ۷‬؛ ودروای باضافة‬
304 847 درون | ‫آن‌بشورندا وهرچز که‌یر آن‌درون‌خوانده‌ودمیده‬              ‫میباشد و طبع آن همچوطبم بنرالینج (‪ )۱‬است‬
304 847 درون | ‫درون اروده کنابه از صاحب دل‬                               ‫فارسی » مخفف درود گر الس
304 847 درون | اشد‬            ‫جيم ‪ +‬معرب درو لك ات‬         ‫درون = بفتح اول » بمعنی اندرون ‪۴‬‬
304 847 درون |                    ‫درون عاقت بر کن ‪۰‬‬     ‫که رش‬                      ‫حذر کن زدود دروتهای رش‬
304 847 درون | جم قدم ارداو برافنامه‪ .‬رك ‪:‬ارداوبرافنامه‬    ‫درون‬    ‫وان‬     ‫(یه)‬
304 847 درون |                    ‫وی‬                       ‫ای درون برور برون ارای !‬
305 848 درون | ل و تشدید الی» شکنبة‬                            ‫درون ‪۵‬کنآاربهه‌ازیداندرون وکینه‌ور‬
305 848 درون | تی‌هم‌هت ازملك بدخشان که مردم‬                   ‫درون باشد » و بیخی است دوایی شبیه بعقرب‬
305 848 درون | ن‬                  ‫باشد شبیه بعقرب ‪ - ۴‬وبمعنی درون همهت که‬
305 848 درون | ‫ماک‬           ‫‪۹‬‬                      ‫رك‪ :‬درون ‪.‬‬              ‫‪6‬‬
305 848 درون | ث) بدان‌روز کار چوبین بود بی‌استخوان » بکپاره چون درون‬
307 850 درون |          ‫‪ ۰‬داخل هنی ‪.‬‬    ‫درون هی‬     ‫ی‬                 ‫سی ودو ‪.‬‬    ‫‪ - ۳‬رك‪ :‬مقدمه‪ ,‬ص‪:‬‬
311 854 درست | ‫وخواجه‌سرا باشد ؛ وبفتح‌اول لز درست است‪.‬‬                                        ‫نزد‪-‬‬
311 854 درست |                                 ‫‪۰‬‬    ‫است‬   ‫درست‬   ‫قىر‬
312 855 درست |                              ‫اوز ‪ ۸‬هم درست است ‪.‬‬                ‫باشد ‪ -‬وبمعنی‌تیر تخش ‪ -‬وژوبین (‪ )۱‬که سنان‬
326 869 درست |       ‫باکاف‬      ‫و‬   ‫‪:‬‬     ‫است‬      ‫هم درست‬       ‫اول‬
328 871 درون |                                 ‫فسوی » خارش درون کلو وبعل وغیره وینهان کردن چیزی «ناطم الاطبا؟ ‪.‬‬
329 872 دف |   ‫دف زدن‬                                                                           
329 872 دف |  ‫دف زدن * کسنابه از خواستن ‪-‬‬                                      ‫دف‬          
329 872 دف |        ‫معنی در(عر)دف آ(الازت‌طرب) ازعبری «نف» مشتق از « تفف» بمعنی زد و کویید «نفی؟ ‪:‬‬
329 872 دف |                ‫نعود آواز دف وچنگه و نی ‪.‬‬                     ‫گوش تواند کههمه عمر وی‬
329 872 دف |    ‫وصفحه کرفتهشده بعدها درزبان عربی «دف» شده وبمعنی لوحه تبزیکار رفته است «فاباص‪۱۱٩ ۲‬‏‬
329 872 دف |        ‫‪ - ٩‬ممنی اصلی ‪,‬نی دف (آلت موسیقی) تواختن‪. ‎‬‬                     ‫دفتن ‪.‬‬     ‫رک‪:‬‬         ‫‪
```


## [2026-09-05T18:15:26.914Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk -v n=330 'BEGIN{RS=\"\\f\"} NR==n {print}' BQT_v2_pages.txt",
 "description": "Print BQT leaf 329 (daf)"
}
```


### [2026-09-05T18:15:28.451Z] TOOL RESULT

```
  ‫دف زدن‬                                                                                              ‫بر‬
                                                                                                       ‫‪-‬‬
   ‫هم افو اس کهرام زاو وان سا‬                                ‫وب ‪.‬‬
                                                                ‫ولای هرچیز باشد اعم ازشراب آ‬
                                                     ‫خا کدان = کنابه ازفالب آدمی‬              ‫دغل‬
 ‫دغوی = بفتح اول و ثالك و سکون‬
                                                                               ‫باشد‬   ‫وعالم سفلی‬      ‫وددا‬   ‫=‬
‫ثالی وتسنالی‪ .‬نام‌دشتی رصحرابی است که‌بر ادران‬

  ‫ببران ونه در آن دشت کعته‪ .‬شودنگدو»بند‬              ‫دغل دری = بفتح دال ابجد و رای‬
‫روزی رستم وطوی درشکار گاء] یبا دختری افتند‬           ‫بنیقطه بتحتانی زده ک»ثابه از عیب جوی وعیب‬
‫وپیش کاوی بردند و چون دختریکی از ملوکه‬                                             ‫گوی ومنافق باشد ‪.‬‬
                                                                           ‫‪9‬‬              ‫‪۱‬‬       ‫‪2‬‬
 ‫بودکاوی اورابعقد تکاح خویش درآورد و سیاوش‬           ‫بمعنی حرام‬   ‫عملی »‬   ‫بروزن‬      ‫=‬       ‫دعلی‬


 ‫ازو بهم‌رسید ‪ ۰ ۴‬ویضم ثالی نیزبهمین معنی آ‪-‬ده‬         ‫زادگی وعباری ومکاری وناراستی کردن باشد ‪.‬‬
                                           ‫‪۱‬‬   ‫انت‬   ‫دول ‪ ۰ ۴‬بفتح اول بروزن قبول ‪۰‬‬


                                               ‫هرم‬
                                                 ‫دا‬‫بیان دو‬

                     ‫نقطه بافا مشتمل بر نه لغت و کنات‬                  ‫دال بی‬         ‫در‬


‫دقتر رگااو خورد ک‪-‬نابه از‬                            ‫بفتح اول وسکون‌نانی “ درسرمة‬                 ‫‪(۵‬‬
                                                                                           ‫سلیمانی؟ بمعنی‬
                                                                                           ‫چیزی بائدکه‬
           ‫ون افزاری امت مانند شانه ‪.‬‬
                                    ‫باشد‪ .‬آ‬                                                 ‫پوستی بر آن‬
 ‫كقتین ‪ -‬بروزن نقشین‪,‬بمنی‌دفته ات‬                                                          ‫چبانند وقوالان‬
                     ‫که شان حولاهگان باشد ‪.‬‬                                                ‫در‬
                                                                                            ‫لوازندا ‏ و‬

 ‫دف زدن * کسنابه از خواستن ‪-‬‬                                      ‫دف‬                      ‫عربی بمعنی بهلو‬
                            ‫باشد ‪۰‬‬   ‫و کدابی کردن‬
                                                                                           ‫عفن است ‪3. ۷‬‬



                            ‫‪.‬‬   ‫ولی‬
                                  ‫الغ»‬‫دغو‬
                                        ‫رکه‪ :‬دا‬  ‫‪۴‬‬     ‫‪ - ۱‬از‪ :‬دغل ‪-+‬ی (مصدری) ‪.‬‬
  ‫‪ ۱‬باین‬            ‫_‪:‬چنبری‪.‬‬
                           ‫‪ ۵6‬ظ‬     ‫رکه ص‪ :‬هشتاد وشش مقدمه ‪.‬‬  ‫‪۴‬‬      ‫بح ج ‪۳۴‬ص ‪ ۵ ۲‬ببعد‬

       ‫معنی در(عر)دف آ(الازت‌طرب) ازعبری «نف» مشتق از « تفف» بمعنی زد و کویید «نفی؟ ‪:‬‬
               ‫نعود آواز دف وچنگه و نی ‪.‬‬                     ‫گوش تواند کههمه عمر وی‬
   ‫‪ .‬ور که‪ :‬ی ی‬     ‫‪۱‬‬   ‫‪۶‬‬   ‫«کلتان‬

   ‫‪ - ۷‬دوب لا در زبان سومری بمعنی لوحه وخط است‪ .‬ازابن زبان وارد کدی شده‬
   ‫تا‪00‬نا و ‪PP‬‏ کردید‪ .‬واز ابن زبالها وارد آرامی شده لا گردید‪ ,‬و نیز بمعنی لوحه‬
   ‫وصفحه کرفتهشده بعدها درزبان عربی «دف» شده وبمعنی لوحه تبزیکار رفته است «فاباص‪۱۱٩ ۲‬‏‬
                   ‫بقل از«لفغات بیگانة !کدی تألیف ‪nremmiZ‬‏ « للپزیگه ص‪٩۹۱‬‏ ور کے ‪ :‬تفس ‪.‬‬
       ‫‪ - ٩‬ممنی اصلی ‪,‬نی دف (آلت موسیقی) تواختن‪. ‎‬‬                     ‫دفتن ‪.‬‬     ‫رک‪:‬‬         ‫‪۸‬‬

  ‫زا از ونالی ‪aréhthpiD‬‏ (پوست حیوانی) داسته‌اند‬              ‫‪ #‬دفر بفتح اول نوم ‪۱‬‬                       ‫‪۱‬‬
   ‫‪ °‬دارةالمعارف اسلام د‪:‬فتر» پنفل از ‪refuD:‬‏ ‪eluY te ,llenruB nosboJ_nosboH‬‬
        ‫‪۰۷.۸‬‬    ‫یه درصفحه‬
```


## [2026-09-05T18:16:00.609Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== FRS درونه ===\"; grep -n \"درونه\\|دُرونه\" FRS_pages.txt FRS.txt 2>/dev/null | head -10\necho \"=== FSF درود/درودگر ===\"; grep -n \"درودگر\\|درود\\|درگر\" FSF_pages.txt 2>/dev/null | head -10\necho \"=== BQT v2 leaf 305/306 scan for kaman ===\"\npython3 - <<'EOF'\ntxt=open('BQT_v2_pages.txt',encoding='utf-8').read()\nleaves=txt.split('\\f')\nimport re\nfor i in range(300,320):\n    for m in re.finditer(r'.{0,40}(قوس قزح|رنگین کمان|کمان رستم).{0,60}', leaves[i]):\n        print(i, i+540, '|', m.group(0).replace('\\n',' ')[:140])\nEOF",
 "description": "FRS/FSF greps and BQT rainbow scan"
}
```


### [2026-09-05T18:16:02.413Z] TOOL RESULT

```
=== FRS درونه ===
FRS.txt:8265:هست سد کیسی درونه۸ که بدو اپنبه زند | 
FRS.txt:8272:۸ - درونه بعنی کمان حلاجی . ٩‏ - چ :در او . 
FRS.txt:16810:درونه؟ 
FRS.txt:16812:مرو بودیم چند گاه بلند کوژ کشتیمو چوندرونه‌شد م۳ 
FRS.txt:16815:درونه کشت چنارو ز ریره شد شنکرف؟* ] 
FRS.txt:16826:درونه کمان حلاجان » چ ؛ درونه کمان ند انان ۰ س این‌افت را ندارد ۳- نتط در 
FRS.txt:21080:| درونه 141 
FRS_pages.txt:8955:‫درونه‪ ۸‬کهبادپونبه زند |‬         ‫کتیسسدی‬
FRS_pages.txt:8967:                                           ‫‪-:‬‬‫‪٩‬‏‬          ‫‪ - ۸‬درونه بعنیکمان حلاجی ‪.‬‬
FRS_pages.txt:18749:                                    ‫درونه؟‬
=== FSF درود/درودگر ===
226:‫آفترین از سپهر‬        ‫ز من»‬   ‫درودت‬          ‫‪ ۱‬چنین داد پاسخ که«ای ماه چهر‬
1981:              ‫اره‪.‬افزار درودگری‪:‬‬   ‫‪-۱‬مخفف‬           ‫ندانم چرابر سرم بد رسد‬
4750:              ‫چو آمد برشیده دادش درود‬         ‫مدتی دعا بر ان خواندن همان از برای‬
4766:                                                                       ‫آن درود می‌فرستند‪...‬‬
5000: ‫(‪)۳-۴۵-۸۱۸‬‬                                        ‫پسر بدرود بی‌گمان کشت تو‬
5718:                                                    ‫برای بدرود کردن و بازگشتن به زابل پیش‬
6343:‫درود (از‬    ‫‪-۱‬که‬     ‫نهان رفتار فریفتار؛‬               ‫تگان یا نے ار‬
6778:                                         ‫پدرود‬   ‫همین دم ز کوهش کشم در مغاک‬
6784:    ‫درود شادی رامش» (خسرو و ربدک ص‬                            ‫د‬
6790:‫معنای اصلی یدرود ارزومندی نندرستی‬                ‫یکی را بهنامو یکی را به ننگ‬
=== BQT v2 leaf 305/306 scan for kaman ===
305 845 |  ‫کنابه ازشکم باشد © ‪ -‬و قوس قزح (‪- ۱ )۳‬‬                         ‫بشکل عقرب وببب آن درونج
```


## [2026-09-05T18:16:10.538Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk -v n=306 'BEGIN{RS=\"\\f\"} NR==n {print}' BQT_v2_pages.txt | tail -40",
 "description": "BQT leaf 305 (darune)"
}
```


### [2026-09-05T18:16:12.224Z] TOOL RESULT

```
                                                                ‫پهلوانی‌است ‪-‬ودام داروبی‌هم‌هست ‪ - ۱‬وچنکک‬
‫درو یش سلطان دل = شاره‌برور‬                                     ‫وقلاب رانیز کوبند وبعربی‌معالاق خوانند ‪ -‬وم‬
 ‫کاینات است که بیغمیر ما صلوات الهعله وآله‬                     ‫اول بده‌ذهب ونامقید وفاق‌را گویند بزیان زند‬
                               ‫وسلم باشد ‪.‬‬                                                                 ‫ویازند (‪ )۲‬؟ ‪.‬‬
 ‫دره = بفتح اول و تشدید الی» شکنبة‬                            ‫درون ‪۵‬کنآاربهه‌ازیداندرون وکینه‌ور‬
 ‫کوسفند وغیرء باشد ‪ -‬کوشادکی ميان ده کوه‬                                                                    ‫ومنافق باشد ‪.‬‬
‫رکاپریبزند ‪٩‬‏ ؛ویتخفیف ثالی از همین معنی‬                        ‫؛صفر‬
                                                                   ‫‪ -۳‬بروزن عروسك م‬                        ‫وك‬
                                                                                                            ‫نرل‬
                                                                                                              ‫د‬
 ‫دارد‪ -‬ونام‌ولاتی‌هم‌هت ازملك بدخشان که مردم‬                   ‫درون باشد » و بیخی است دوایی شبیه بعقرب‬
‫آنجا یخوش صورتی مشپورند و انارخوب درا لجا‬                       ‫که آنرا درونج عقربی گویند » و درونج معرب‬
                                                                                                    ‫زک‬
‫مدشود ‪ .-‬و ضاحمول و تشدید الی پوستی چند‬
 ‫باذد باريك که بر هم بدوزند با برهم ببافند‬                     ‫درو نه = بفتح اول وبا واو مجهرل بر‬
‫کوناهکارانرا بدان تنبه سازند وکاه باشد که‬                      ‫وزن نموله » بمعنی درونك است‪ .‬وآن کیاهی‬
 ‫دهل ولقاره رابدان نوازند ویمعتی‌دلیل وبرهان‬                  ‫باشد شبیه بعقرب ‪ - ۴‬وبمعنی درون همهت که‬
   ‫)‪ (4‬چك‪ :‬تخففه‪.‬‬            ‫)س( چش‪ :‬فوی‌وفز ح ‪.‬‬             ‫(‪)۲‬چك‪ :‬ژند وباژند‪.‬‬            ‫)‪ (۱‬چكث‪ :‬دوم‪.‬‬

    ‫»هرند) *مماس ‪۷۲ ۲‬‬        ‫(کافر ‪ ۰‬می دمن‬       ‫بپلوی ار‬                   ‫‪— ¥‬‬        ‫‪.‬مصحف؟* درو ‪1۵‬؟‪.‬‬            ‫‪ ۱‬ظ‬

    ‫دروغ‌پرست " |زاوستا_ ‪ « 602۷۲1 - ›4 812۷89‬بارتولمه ‪ » 4۷۷۲‬پازند وپارسی ‪04۳2۷721‬‬
   ‫رك‪ :‬درو نك درولج ‪۰‬‬        ‫‪> ۴‬‬        ‫‪ -‌ ۳‬رك‪ :‬درو له‪.‬د؛ ولج ‪۰‬‬              ‫لیب رکد‪ »+۰‬ورك ‪:‬اسشق ص‪۳ ۴۲۲ ۰۲‬‬

   ‫‪anurd‬‏ ( کمان ‪ ۰.‬قوی) » تلوچی‬              ‫ت‬    ‫ماک‬           ‫‪۹‬‬                      ‫رك‪ :‬درون ‪.‬‬              ‫‪6‬‬
                                     ‫‏‪ dîn uk , 0‬سوف )حرق » اغدوب ع ‪ 4۳00‬قشسا« ‪. 00۸‬‬
   ‫«ومان وی( کیومرث) بدان‌روز کار چوبین بود بی‌استخوان » بکپاره چون درون‬
                                                                       ‫ک‬                                        ‫‪۷‬‬
                                   ‫درووزه (ھ م‪ (.‬۾ دریوز *‬           ‫=‬   ‫‪۸‬‬              ‫حلاحجان» «نوروزنامه ‪۹۳٩‬‏ ‪.‬‬
    ‫وخی ‪۲621‬‬       ‫(بطلموی ‪(1‬‬            ‫_ اوستا ‪_ûnerad‬‏ (دره‪ ,‬گردنه) ‪ ۳‬سونالی ‪anrûD‬‏‬

   ‫فارسی بمعنّی‬   ‫»ودر‬       ‫ع ‪ered‬‏‬    ‫هو ‪.‬شمان ایض » در ‪9۳‬‬                 ‫و رك‬      ‫‏‪ 9 dher‬أسشق ‪“°‬‬               ‫سریکلی‬

   ‫‪ ۰‬یر لی‬   ‫‪earread‬‏‬   ‫؛ گلکی‬      ‫ارل ودوم)‬     ‫(بكر‬       ‫اسلام ‪ :‬دره‬     ‫الممارف‬   ‫دائرة‬       ‫رك‪:‬‬   ‫وادی عر هی آبد ‪۰‬‬


    ‫سنگری ولاسگردی ‪» 64۲۲310‬سرخه‌بی‬                         ‫‪.-‬دانی ‪۲۲3‬‬             ‫ونطذزی ‪ ۱ .۵« 8۳۳20‬ص‪54‬‬
                                                        ‫‪.‬‬     ‫‪ .‬نهمرزادی ‪« ۲۲00‬ك‪ .‬ص‪۱۸۱‬‬                                    ‫‪6‬‬
    ‫‪4۸‬‬   ‫نقه درصفحه؟‬     ‫‪۳‬‬     ‫‪ ۰‬ددن‬     ‫درودن‬   ‫رك‪:‬‬   ‫وياجم‪.‬‬    ‫اول وفتح دوم‬       ‫نکر‬        ‫=‬   ‫ادن‬    ‫درو‬   ‫‪¥‬‬
```


## [2026-09-05T18:16:30.055Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor L in 269 272; do echo \"########## leaf $L (p≈$((L+540))) ##########\"; awk -v n=$((L+1)) 'BEGIN{RS=\"\\f\"} NR==n {print}' BQT_v2_pages.txt | tail -30; done",
 "description": "BQT leaves 269, 272"
}
```


### [2026-09-05T18:16:31.725Z] TOOL RESULT

```
########## leaf 269 (p≈809) ##########
                                                                                    ‫فچ‬‫(‪)۱‬‬

                                           ‫‪ -‬از‪ :‬داد (ه‪.‬م‪ ).‬‏ کستر (کسترنده) ‪.‬‬
          ‫سوی خوش خواند ایزد داد کگستر‪.‬‬               ‫مردم که او را‬           ‫تا چت‬         ‫‪ - ۴‬بیندیش‬


  ‫«اصرخسرو بلخی‪٩۸۹۱‬‏ ‪.‬‬
          ‫‪.‬‬   ‫‪۷۸۹ :‬‬   ‫تر کی ‪ « 7021‬قدری ‪۲‬‬         ‫‪۴‬‬                ‫رل ‪ :‬دادر ‪ ۳‬دادرند‬         ‫سب‬       ‫‪۴‬‬

   ‫پپلوی ‪( ۲20-0021‬لفة بمعنی حامل قانون‪ .‬عدل) «بوتکر ‪ ۵۸‬و ‪72۷-0024‬‬                                 ‫‪۵‬‬
  ‫‪ - ۱‬از دسائس ‪« .‬فرهنك دساتیر ‪۶۶۲٩‬‏ ‪-‬‬                ‫‪.‬اسان ‪٩۹‬‏ و ‪. ۰۰۳۰‬‬
                                                                       ‫(فاضی) ک‪9‬رستنسن س‬
  ‫‪Hypericum‬‬       ‫‪— A‬‬            ‫‪ .‬رك‪ :‬لك‪۲‬ص‪-۷٤‬‏ ‪. ۵۷‬‬
   ‫‏‪ - ٩‬پهلوی ‪« 721‬تاوادبا ‪ ۰ ۹۱2‬اوستا ‪_uTUÃd‬‏‬                        ‫(ھىرفارىقون) د لك ‪٣‬ص‏ ‪. ۵۷۰‬‬
  ‫(چوب) » قس‪:‬ارمنیع ‪( 18052730‬باغ) › هندی باستان ‪( 1078 -‬چوب) ‏ کردی و بلوچی‬
   ‫»‪al‬دق‪۲۲‬ه » ورك ه‪:‬وبشمان ‪ ۲۲۵‬ک؛یلکی ‪( 780‬درخت) ‪ .‬خواداری ‪ « ۳21‬سالتامة‬
                                                                      ‫س‬                                               ‫‪۳‬‬
                                         ‫را ‪.‬‬   ‫ومجرمان‬     ‫‪-‬‬     ‫‪°‬‬             ‫‪.‬‬      ‫کلپگان‪۷‬‬               ‫رگ‬
                                                                                                              ‫فه‬


  ‫‪ #‬دادن ‪ -‬بفتح سوم» پپلوی ‪« 52180‬منای ‪« ۱۷۲:۲۰‬تیبر که ‪۲٥‬‏ › یارسی بلستان‬
     ‫‪( dadhami‬دادن)»هندی باستان ك ‪207‬‬        ‫‪( ۷1002021 . 24‬دادن)‪ ,‬اوستا ‪21 -‬‏ ‪¢‬‬

  ‫‪ ( 024‬دادن ) » بلوچی ‪ . 822: . 8284‬شنتی ‪ ۳2‬له ‪,‬‬    ‫(ادن ) ؛کردی ‪. 8120‬‬ ‫د‬
   ‫‪ 0100621 ۰‬د کے ‪ .‬است‬ ‫سریکلی ‪ « 01-201‬استق ‪« ۰۲۵4‬بارتولمه ‪۱۱۷٩‬‏ ‪ ۰‬استی ‪7‬‬
  ‫‪ 0‬ودردبه‌های گیلان ‪ ۰ 821-211‬شهمیرزادی یز ‪(۳21-21‬دادن) ؛ عطا‬          ‫‪ ۷‬کیلکی‬
   ‫کبردخنش»یدن ‪ .‬احسان کردن‪ -‬بمعنی‌دبگرازیارسی باستان ‪( »21-‬ساختن» نشاندن)‪.‬اوستا ‪24‬‬
  ‫(ساختن‪ ,‬شادن» ابجاد کردن)؛ پهلوی‪ ۳212۰‬هندی‌باستان ‪« 200‬اسشق‪»۱۲۵‬؛ کردن» ساختن ‪.‬‬

########## leaf 272 (p≈812) ##########
                            ‫از یشه میباشد ‪.‬‬                          ‫تکه کاهر ا نیز کفته‌اند ‪۱‬‬
‫دار هك » بامیم بروزن آبچك » نوعی‬
                                                      ‫دار فلفل ‪ ۴‬مهعروف است گ‬
                                                  ‫‪.‬وبند‬
‫ازمروباشد وآن مروسفید است » ومروجنسی از‬
‫رباحین بود وسد بلغمی بکثاید واکثر امراض‬           ‫شکوفه وبیلرفلفل است» وبعضی کویند درخت آن‬
                            ‫بلغمی را ناقع است‪.‬‬    ‫غیر درخت قلقل باشد(‪ )۱‬وآن را فلفل درازنیز‬
                                                                                   ‫کوند‬
‫دار نگ » بکر الك و سکون نون‬                                  ‫‪ .‬گرم وخشك است درسم ‪.‬‬
 ‫وکاف فارسی» خوانی با طبقی راکویند که کوشت‬        ‫دار کدو ‪ -‬بسکون‌ثالك » چوبی باشد‬
                                 ‫برآن نهند ‪.‬‬      ‫یلند کهدروسط حقیقی میدان برپای کنند و در‬
‫داد نهال » بکر نون و های بالف‬                     ‫قدیم کدوی طلا و نقره از آن مویباخته‌اند و‬
‫کشیده بلام زده » چوب بقم"را کویند که بدان‬         ‫تبر‌اندازان مواره و تاخته کرده تبری بر آن‬
                            ‫چىزھا رنگه کنند ‪.‬‬     ‫می‌انساختماند‪.‬تبرهرکس که برآن میشورده‌است‬
‫داد فی» بکر ثالث و نون بتحتانی‬                    ‫کآدنورا بااسب وخلت باومیدادماند‪,‬وآن‌هدف‬
‫کشیده ‪ ,‬نام موضعی است در هندوستان مشتمل‬           ‫راحریی برجاس وآن چوب رابتر کی قباقآفاجی‬
                             ‫پربتخانة بیار ‪#.‬‬                                     ‫خوانند ‪.‬‬

                                                                   ‫)‪ (۱‬چش‪ :‬امت ‪.‬‬

               ‫=‪ ( 66121205‬فر ) « لك ‪۲‬ص ‪ « ۰ ۳۷‬دزی ج اص ‪٩ ۰*۲4‬‏ ‪.‬‬
                                                                ‫‪2 ۱‬‬
  ‫"‪ ۴‬در ارویای قرون وسطیآنرا‬     ‫؟ ‏ رك‪ :‬درایزین و دارآفرین (ا) و دارزین ‪,‬‬
  ‫‪ 1۲2/1۳ ۵۵۲0۱‬تامیبهاندرفرانوی ‪ ۴۲۷10 8001‬گوبند «لظرك ‪ .‬تاریخ طبج اص ‪۷64۰‬‬
                                                        ‫د لك ‪۲‬ص ‪۵۷٩‬‏ «دزی ج‪ ۱‬ص ‪. ۶۲‬‬
  ‫‪« suoiP sidiriV inileraK dnarB‬کیهان‪ .‬جغرافیای اقتصادیی‪۱۳‬بنقل ازهاینرش؟‪. ‎‬‬
 ‫® _ مصدر آن « کوش داشتن » استبمعنی محافظت کردن » وتر کیب فوق را از‪‎‬‬
                                               ‫نظایر این بیت حافظگرفتها ند ‪:‬‬
   ‫شیه در صفحة ‪۳۱۸‬‬
```


## [2026-09-05T18:16:43.513Z] TOOL CALL #41: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T18:16:43.520Z] TOOL RESULT

```


```


## [2026-09-05T18:16:47.724Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AE%D8%AA",
 "prompt": "Give the full Persian etymology section for درخت (deraxt) 'tree': Middle Persian form, Proto-Iranian/Proto-Indo-Iranian reconstruction, which PIE root it is assigned to, and any cited authorities (Hasandust, MacKenzie, Cheung)."
}
```


## [2026-09-05T18:16:49.257Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B1%D9%88",
 "prompt": "Give the full Persian etymology for دارو (dārū) 'medicine, drug': Middle Persian form, the Proto-Iranian root, whether it is derived from *dāru- 'wood/plant' or from another root, and cited sources."
}
```


### [2026-09-05T18:16:54.635Z] TOOL RESULT

```
# Persian Etymology of درخت (daraxt) 'tree'

## Middle Persian Form
The word derives from Middle Persian dlht' (dlʾht'), written in Pahlavi script as 𐫅𐫡𐫟𐫤 (drxt /draxt/, "tree").

## Proto-Iranian Reconstruction
The Proto-Iranian source is reconstructed as *draxta- ("firmly standing"), with the first component stemming from Proto-Iranian *drag- ("to hold, strengthen").

## Proto-Indo-Iranian Connection
The term relates to Proto-Indo-Iranian *dʰar- ("to hold, support"), connecting it to a broader Indo-European semantic field of structural stability and wooden materials.

## Cited Authorities
The page references several scholarly works but does not attribute specific etymological interpretations to individual scholars like Hasandust, MacKenzie, or Cheung. The references section cites MacKenzie's 1971 Pahlavi dictionary and other lexicographic sources, though these are presented as general references rather than attributed to particular theoretical positions on the etymology.

The word shows cognacy with Vedic Sanskrit dāruṣ, Parthian drxt, and Baluchi diračk, demonstrating the reconstruction's validity across Iranian languages.
```


### [2026-09-05T18:16:56.101Z] TOOL RESULT

```
# Persian Etymology of دارو (dārū)

## Middle Persian Form
The Middle Persian predecessor was written as _dʾlwkˈ_ with the pronunciation /dārūg/, meaning "drug, medicament."

## Proto-Iranian Root
The word derives from Proto-Iranian _*dā́rukah_, which may originate from a root meaning "tree, wood."

## Etymology Chain
According to the Wiktionary entry, the development follows this path: Proto-Iranian _*dā́rukah_ → Middle Persian _dārūg_ → Classical Persian _dārū_.

## Supporting Evidence
The article notes a cognate in Parthian _dʾlwg_ (/dālūg/, "plant, tree"), which supports the semantic connection to plant/tree terminology. However, the source acknowledges this etymology as uncertain by using "perhaps" when describing the Proto-Iranian origin.

## Cited Source
The main reference cited is Rastorgujeva and Edelʹman's 2003 _Etymological Dictionary of Iranian Languages_ (volume 2, page 359), which Moscow's Vostochnaya Literatura published.
```


## [2026-09-05T18:17:11.322Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%B3ru",
 "prompt": "Summarise: the reconstruction *dóru 'tree, wood', its root, the gloss, descendants in Indo-Iranian (Avestan, Old Persian, Sanskrit), Greek, Germanic, and whether Latin dūrus is listed as a derivative. Also note any related reconstruction *derw- / *dreu- 'firm, solid'."
}
```


## [2026-09-05T18:17:13.795Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D9%81%23Arabic",
 "prompt": "Give the Arabic etymology of دُفّ (duff) 'tambourine, frame drum': is it native Semitic, a borrowing from Aramaic/Hebrew, or from Persian? Quote the etymology text and cognates (Hebrew tōp̄, Aramaic tuppā, Akkadian)."
}
```


### [2026-09-05T18:17:17.880Z] TOOL RESULT

```
# Proto-Indo-European *dóru: Summary

**Reconstruction:** *dóru (neuter noun)

**Meaning:** "tree"

**Etymology:** Possibly derived from *deru-/*drew- meaning "hard, firm, strong, solid," with reflexes including Latin dūrus ("hard, rough"), Old English trum ("strong, firm"), and Old Armenian tram ("firm, solid").

**Key Descendants:**

- **Indo-Iranian:** Sanskrit दर्वि (dárvi, "spoon"); Avestan दादरुव (dādruua, "tree; wood")
- **Greek:** δρῦς (drûs, "tree, oak"); δρυμός (drumós, "thicket"); δένδρεον (déndreon)
- **Germanic:** English "tree" via Proto-Germanic *trewą
- **Celtic:** Welsh derw; Old Irish derb
- **Anatolian:** Hittite tāru ("wood, tree")

**Related Reconstruction:** The root *derw-/*dreu- meaning "firm, solid" appears connected, though *dóru itself may represent a deadjectival nominalization of this adjective.

**Note:** Latin dūrus is cited in the etymology section as evidence for the *deru-/*drew- root, but not listed as a direct derivative of *dóru.
```


### [2026-09-05T18:17:20.787Z] TOOL RESULT

```
# Etymology of دُفّ (duff) "Tambourine"

Based on the Wiktionary entry, the word دُفّ (duff) has a **native Semitic origin**, not a borrowing from Persian or other languages.

## Key Etymology Information

The entry states that دُفّ derives from a more primitive form of دَفَعَ (dafaʕa, "to push, to propel"). The text explains: "A more primitive form of *دَفَعَ* (dafaʕa, 'to push, to propel'), and its resultant noun, already formed before Arabic."

However, the entry notes a **possible Aramaic connection**: Aramaic דפא/ܕܦܐ (dappā, "board") is believed to derive from **Sumerian** 𒁳 (DAB, "board") or 𒁾 (DUB, "board").

## Notable Absence

The Wiktionary entry does **not mention** Hebrew tōp̄, Aramaic tuppā, or Akkadian cognates you reference. This suggests those may represent a different etymological tradition not reflected in this particular source.
```


## [2026-09-05T18:17:35.308Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"•  j\\.  dauru\\|dauru-\\|d.uru-  n\\.\" BRT.txt | head -5\necho \"=== BRT drvatat ===\"; grep -n \"drvatãt\\|drvatāt\\|drvatat-  f\\|Gesundheit\" BRT.txt | head -8\necho \"=== BRT upa.drva / drvo.ast ===\"; grep -n \"upa\\.drv\\|drvB\\.\\|drvō\\.ast\\|hauruua\\|drvista\" BRT.txt | head -8",
 "description": "More Bartholomae greps"
}
```


### [2026-09-05T18:17:35.401Z] TOOL RESULT

```
=== BRT drvatat ===
2455:l'S.S  (wo  awÄ<f' als  LSf.),  Y.9-28';  —  w I  nH  aiäAili  i'lse  jamyät  as>mca  ..  asista  tä airihat  Aa'a  visal  güuS  buyät  Y.6'o.2i.; '  2.  S..2J.3.  52-3.  FrD.  P,  Yt.  /j.  i3;  ~  ioa fri>ä  .  .  buyata  ahmya  nmlne  Yt.  /J.  147  ; IS6f.^  Y.26.^,  62.3*;  —  fraddiäi  ahe nmanahe  ..  vlspaya  alaond  stöis  Y.52.4; 4.5',  Vr. ».  13*;  —  imim  >7oqm  .  .yänim .  .  jaioyemi  .  .  dn'atütam  aiiiAas?  tanvS ". .  Gesundheit  dieses  (meines)  Leibes"  Y. 5.19;  — yaiä  ratSm  akurö  valdil  . ,  aya qsayä(scL)Y.ji.2;  —  afäi  aAmäi  var^nai.. nidätitn  ahm  . .  iAaeiili  (sd.) . .  "und  in  diesen (ünsem)  Glauben  .  ."  Y.4ff-3;  —  aitiAa daenayä  mqs  vaca  dd^anaAe  Y.  j?.  3 1 ;  — frä  KTjri»ie(sd.)aA£(XS{.alsinstr.)da^(^a ..  aAura  ..  Vr.5.3;  —  atcäv3  mizdtm  (sd.) anhat  aAyä  magahyH  y.  S3T>  —  H  *"''^ (sd.)  maiy  aniya/ay  vasiy  astiy  kartam avJ*  ahiyäyä  dipiyä  ttaiy  nipislam  (sd.) ".  .  in  dieser  (meiner)  Inschrift  (hier)  . ." Bh,  4-  S;  —  yS  ach-a  mazdayasnalh-a  .  . ". .  wer  hier  unter  den  Af.  .  ."  V-S-z; —  aAyil  '^wil  J^rff  rtr»z3nil  .  .  pairl.ja-
11955:—  "nvS  vlspayä  drvatätim  °nvS  vTspayä vazdvar)  Yt/4.39;  —  imfm  'hwqm  ..yänim haema  Jailyemi  drvatätim  atiiAas)  'nvS.. darrjB.jltlm  ustänahe  Y.p.19;  K.i.Z;  — 'nuyäsca  paiti  druaiats  Yt.  13. 134;  —  aha r0  tarn  sraos'a  . .  zävar»  daya  AitaHbyB drvatätitn  °nubyu  ".  ,  Kraft  unsem  Ge- spannen, Gesundheit  unsern  Leibern"  Y. j7,  i6;  —  däl»m  te  'nuye  ^annd  'Yt.iy. 12;  15;  — ya>a  tW . .  ifä'^ravaiils  'nvö +,iwi/J  (Sp.  274  IL)  Y.  60.  11;  —  vohü uxsyä  (sd.)  manan&ä  .  .  ui'tä  'nUm  Y. ^.10;  —  haomü.artharstahe  (sd.)  hizvS mq%rS.hitahe  (sd.)  °nvd  A.4-5i  —  im Gegensatz  zu  gaihä-  (Sp.  477  in.),  urvan- usw,:  akmäi  nfmaahl  ävaldayamaidi  gal- %^slä  'nvascä  nipätayaicä  , .  Y.  56".  2  j  —  yö nS  . .  iririx/äite  gaghanqm  .  .  °nunqm  Y. 65, 7 ;  —  frähatiia  asake  gaghä  .  ,  asahe °nuy!  Yt,  6.1;  —  forasayäi  (sd.)  aibi %waha  gai'iäAa  -nuHcä  Y.  43.  T,  — 'nvagca  * kaosravar3h»m  untnaija  dan^tm havanium  F.^h;  —  cim  ,  .  qst>m  isaiti 'rwa  cim  uruna  Aog,  4^;  —  vJspS  gai- %isca  -nvasia  azdsbisca  .  .  iistänqs^a urvätamca  . .  pairica   dad>mahl  Y.  55.
13037:•  j.  dasvar-  o.  'Gesundheit',  nur  in  Ver- binduDg  mit  (folg.)  batsaza-  n.  'Heiltum': 'varfca  baisazfmca  V.5. 53;  —  ni  'van nl  baltazim  (näml.  mruyt)  Y.  p.  1 7 ;  71. 1 7, Vr.  20,  I,  Vyt_35; —  ci^nm  'van  baesa- stm  Y.  70. 7;  *FrW.9.  2";—  'varp  (statt AD.)')  baliaza  äfrfnämi  Y.6S.i$;  — *'varii*  (statt  des  Instr.)"  . .  ba^asa  Y. 55.3;  —  'van  (statt  des  Dat.)''  baisa- zäUa  Y.  6S.  2.
13487:•  j.  däsma-Qi-  Adj.  'Gesundheit  zu- führend, bringend':  arhi^^a  väl5  °nif (NPm.)"  varTkraytns  Y.IO.  18.
14225:•  j.  drva'tät-  f.  'Gesundheit,  Heiltum': ddkril  ianiäi  'tät»m  Yt  13. 14;  F.  yh;  — dayä..'/ät?m  tanufys  Y. 57.26;  —  tanvS 'tatsm  Y-  68. 1 1 ; p.  1 9,  Yt.  10. 108, i4- »9!  —
16503:8,  3)  n.,  m.'';  a)  'Heil-,  Gesundheits- mittel,  Arzenei':  avaüa  he  't?m  upsisay?n ya%a  dahmaUi^  "in  einem  solchen  Fall sollen  sie  ein  Heilmittel  für  ihn  ausfindig 2U  machen  suchen,  wie  für  einen  D."  V. y-  3S;  —  ^  '^  (näml.  haomahe)  Sa  (NP.) irlra'i arf  {sd.) ..  Y.io.  12;  —  haoma  dasdi ml  'zanqm  yäbyS  ahi  baisazma  (sd.)  V. 10.  9;  6t<.  15',  Yt  13.  13s;  —  aslm  .  . baryntlm  vupä  "sä  (AP.)  apqmca  gavamla ttrvaranamca  ". .  alle  Heilmittet  der  Wasser, Tiere  und  Pflanzen"  Y,  52.2;  —  nava  'za (NP.)  V,  2/.  3 ;  —  fravaiayö  .  .  a^is  -za (AP.)  hanmni  Y.  60.  4;  Vr.  <?.  i',  2,  F.  16,
22946:nsit  m^  nalda  ^ao>anä  nöil  dainh  nsit  blühender    Gesundheit:    ^ruum    .p^.tayä
25798:Pü. :  saxt  käf,  erL  :  läü  köf  drwt.  —  •)  Qn Zeichen  von  Kraft  und  Gesundheit  im  Gegen- satz zum  schlaff  herabhängenden.
=== BRT upa.drva / drvo.ast ===
12268:Ais  srayataAai  h(üa  vourukaiat  äaf  maf/a us.fravSfite  .  .  Yt  Ä  40;  —  ~'y^e  stärS raevat5  i^armauuAatS  YtS.  o,  56,  57,  Y. I.ii,  27.2;  —  'rim  drvB.caimamm  Yt ■Kr 2,  Ny./.8.  a)  Hstryehe  a)  (nämj. mä)  heisst  der  4.  Monat  im  Jahr:  xA/aäim *mailysiümahe  (sd.)  'ryeke  da^usS  A.  3. 8.  ß)  (n��ml.  ayan)  heisst  der  13.  Monats- tag: 'ryeie  stärJ  ra^fa/ff  s^armanuhaiS S.Z.  13;  vgl.  2.13,  y.i6.4.
14249:•  j.  drvö.stätay-  Adj.  'gesunden,  heilen Stand  habend'(?):  drväspqm  sürqm  . . ^staitlm  (ASf.)  drvB.varttqm  Vt^.  a.
```


## [2026-09-05T18:17:48.903Z] TOOL CALL #47: Bash

```json
{
 "command": "pdftoppm -f 121 -l 121 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg121 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 121"
}
```


## [2026-09-05T18:17:50.850Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/durable",
 "prompt": "Give the etymology chain for durable/duration/dure: Latin durare, durus, and what PIE root Etymonline assigns (deru- 'be firm, solid' or *deue- 'to last'). Quote the relevant sentences."
}
```


### [2026-09-05T18:17:51.144Z] TOOL RESULT

```
total 34988
drwx------ 3 sfmqrb sfmqrb     4096 Sep  5 14:17 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    48417 Sep  5 10:19 build93.py
-rw-rw-r-- 1 sfmqrb sfmqrb    59425 Sep  5 10:54 build98.py
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2950 Sep  5 10:15 c_anth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2661 Sep  5 10:15 c_armonica.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5133 Sep  5 14:10 c_avestan120.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    18289 Sep  5 13:48 c_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13620 Sep  5 13:48 c_germ2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10949 Sep  5 13:48 c_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    15141 Sep  5 13:51 c_hektaton.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
-rw-rw-r-- 1 sfmqrb sfmqrb    18737 Sep  5 13:51 c_kent.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10687 Sep  5 13:48 c_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13469 Sep  5 14:10 c_latin120.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4845 Sep  5 10:50 c_root3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1795 Sep  5 10:50 c_scyth2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2953 Sep  5 10:50 c_scyth3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4885 Sep  5 10:49 c_scyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3019 Sep  5 10:15 c_sus.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33345 Sep  5 10:55 e0.102.json
-rw-rw-r-- 1 sfmqrb sfmqrb    38686 Sep  5 10:34 e0.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    26175 Sep  5 10:38 e1.95.json
-rw-rw-r-- 1 sfmqrb sfmqrb      456 Sep  5 10:56 g.py
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    24046 Sep  5 13:38 latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49033 Sep  5 10:53 mk100.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17464 Sep  5 10:55 mk102b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    25511 Sep  5 10:58 mk102c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    21655 Sep  5 10:53 mk102.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62559 Sep  5 11:04 mk103.py
-rw-rw-r-- 1 sfmqrb sfmqrb    79255 Sep  5 13:30 mk104.py
-rw-rw-r-- 1 sfmqrb sfmqrb    47159 Sep  5 13:30 mk105b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    31652 Sep  5 13:24 mk105.py
-rw-rw-r-- 1 sfmqrb sfmqrb    62837 Sep  5 13:37 mk108.py
-rw-rw-r-- 1 sfmqrb sfmqrb    40927 Sep  5 13:43 mk109.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63862 Sep  5 13:46 mk110.py
-rw-rw-r-- 1 sfmqrb sfmqrb    48342 Sep  5 14:00 mk113.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61685 Sep  5 14:01 mk114.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60434 Sep  5 14:01 mk115.py
-rw-rw-r-- 1 sfmqrb sfmqrb    76964 Sep  5 14:09 mk116.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    27206 Sep  5 10:38 mk95b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    39501 Sep  5 10:34 mk95.py
-rw-rw-r-- 1 sfmqrb sfmqrb    49433 Sep  5 10:35 mk96.py
-rw-rw-r-- 1 sfmqrb sfmqrb    54149 Sep  5 10:47 mk97.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61159 Sep  5 10:50 mk99.py
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  5 14:17 p117
-rw-rw-r-- 1 sfmqrb sfmqrb    32690 Sep  5 13:24 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71589 Sep  5 10:41 pg100.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68145 Sep  5 10:44 pg102.png
-rw-rw-r-- 1 sfmqrb sfmqrb   114170 Sep  5 10:49 pg103_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79623 Sep  5 10:49 pg103.png
-rw-rw-r-- 1 sfmqrb sfmqrb   169766 Sep  5 10:57 pg104_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22122 Sep  5 10:58 pg104_charlatan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78826 Sep  5 10:57 pg104.png
-rw-rw-r-- 1 sfmqrb sfmqrb    31584 Sep  5 11:00 pg104_tea.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82500 Sep  5 10:57 pg105.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55270 Sep  5 11:01 pg106.png
-rw-rw-r-- 1 sfmqrb sfmqrb    48976 Sep  5 11:01 pg107.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68501 Sep  5 13:26 pg108.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63543 Sep  5 13:30 pg109.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6518 Sep  5 13:38 pg110_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67502 Sep  5 13:29 pg110.png
-rw-rw-r-- 1 sfmqrb sfmqrb    36325 Sep  5 13:32 pg110_yeth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    46559 Sep  5 13:32 pg110_zbn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72718 Sep  5 13:38 pg111.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50381 Sep  5 13:37 pg112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65357 Sep  5 13:45 pg113.png
-rw-rw-r-- 1 sfmqrb sfmqrb   117231 Sep  5 13:48 pg114_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1253 Sep  5 13:48 pg114_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11671 Sep  5 13:48 pg114_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163144 Sep  5 13:51 pg115_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70699 Sep  5 13:51 pg115.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64811 Sep  5 13:57 pg117.png
-rw-rw-r-- 1 sfmqrb sfmqrb    42354 Sep  5 14:05 pg118.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78691 Sep  5 14:11 pg119.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84971 Sep  5 14:10 pg120_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb    50224 Sep  5 14:06 pg120.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82335 Sep  5 14:17 pg121.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb    93420 Sep  5 10:15 pg94.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44047 Sep  5 10:16 pg94_sogd.png
-rw-rw-r-- 1 sfmqrb sfmqrb    49714 Sep  5 10:16 pg94_urvar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163439 Sep  5 10:15 pg96_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101597 Sep  5 10:41 pg99_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb     8738 Sep  5 10:41 pg99_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65608 Sep  5 10:40 pg99.png
```


### [2026-09-05T18:17:56.124Z] TOOL RESULT

```
# Etymology Chain for Durable/Duration

Based on the Etymology Online source, here's the chain:

**Latin roots:** The word durable traces back to Latin *durare* ("to harden") and *durus* ("hard").

**PIE root:** The document specifies that these derive from PIE *\*dru-ro-*, described as "suffixed variant form of root *\*deru-* 'be firm, solid, steadfast.'"

**Relevant quote:** "from _durus_ 'hard,' from PIE _\*dru-ro-_, suffixed variant form of root *deru- 'be firm, solid, steadfast.'"

The etymology page does not mention *\*deue-* as an alternative root assignment—it identifies *\*deru-* as the sole PIE source for this word family, which encompasses durable, duration, and related terms like endure and durability.
```


## [2026-09-05T18:18:03.426Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg121.png'); print(im.size)\nim.crop((0,0,im.size[0],int(im.size[1]*0.55))).resize((int(im.size[0]*1.6),int(im.size[1]*0.55*1.6))).save('pg121_top.png')\nim.crop((0,int(im.size[1]*0.45),im.size[0],im.size[1])).resize((int(im.size[0]*1.6),int(im.size[1]*0.55*1.6))).save('pg121_bot.png')\n\"",
 "description": "Crop page image"
}
```


### [2026-09-05T18:18:06.918Z] TOOL RESULT

```
(1700, 2200)
```


## [2026-09-05T18:18:09.009Z] TOOL CALL #50: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg121_top.png"
}
```


### [2026-09-05T18:18:09.586Z] TOOL RESULT

```

```


## [2026-09-05T18:18:09.583Z] INPUT

[Image: original 2720x1936, displayed at 2000x1424. Multiply coordinates by 1.36 to map to original image.]


## [2026-09-05T18:18:16.484Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg121_bot.png"
}
```


### [2026-09-05T18:18:16.987Z] TOOL RESULT

```

```


## [2026-09-05T18:18:16.985Z] INPUT

[Image: original 2720x1936, displayed at 2000x1424. Multiply coordinates by 1.36 to map to original image.]


## [2026-09-05T18:18:26.902Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN tree ===\"; grep -n \"^tree,  n\\.\\|tree,  n\\.,  a  perennial\" KLN_1966.txt | head -3\ngrep -on \"tree,  n\\..\\{0,900\\}\" KLN_1966.txt | head -2\necho; echo \"=== SKT tree ===\"; grep -on \"TREE.\\{0,400\\}\" SKT.txt | head -3",
 "description": "Klein and Skeat: tree"
}
```


### [2026-09-05T18:18:28.514Z] TOOL RESULT

```
=== KLN tree ===
13289:tree,  n.,  1)  entrance,  right  to  enter; 2)  a  course  of  meal.  —  F.  entree.  See  entry, entremets,  n.,  side  dish,  extra  dish.  —  F.,  fr.  entre mets,  ‘between  dishes’.  See  ist  entre-  and  mess, entrench,  intrench,  tr.  v.  —  Lit.  ‘to  surround with  entrenchments’;  formed  fr.  ist  en-  (resp. in-,  ‘in’)  and  trench.
35295:tree,  n.  —  Corruption  of  swingietree,  whose first  element  was  mistaken  for  the  adjective single.

=== SKT tree ===
```


## [2026-09-05T18:18:29.726Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN tree/oak ===\"; grep -n \"Skt. dāru\\|dāru-\\|daru-, dru-\\|drus.*oak\\|Grk. drys\" SYN.txt | head -8\necho \"=== SNS 318 ===\"; python3 -c \"\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\n\"\ngrep -n \"draxt\\|dārūg\\|dār \" SNS.txt | head -8",
 "description": "Buck and SNS greps"
}
```


### [2026-09-05T18:18:31.206Z] TOOL RESULT

```
=== SYN tree/oak ===
1549:pl.), Boh. d¥evo ‘wood’, drevno piece of wood’, Pol. drzewo, Russ. derevo ‘tree, wood’; Skt. daru-, dru- ‘wood’, druma- tree’, Av. dauru- ‘piece of wood, club’.
=== SNS 318 ===
243
6664:..»/ fJ S*. ndrxt: ^ft Uilffc 1772)han-draxt : fc. 
17345:.c**- Jt 4:draxt: yiJ*X» 
17346:{Mir. Man. drxt : >=t {GNPE. 121) * draxta- : fc. 
17347:daraxt : ^ (/Irm. <7ram.l45) draxt: j-tj/Ill. 54 ;) 
29107:han-draxt 88/2 
29302:draxta-C?) 318/20 
33234:draxt 318/21
```


## [2026-09-05T18:18:40.606Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17340,17352p' SNS.txt\necho \"=== KLN 1971 tree ===\"; grep -on \"tree,  n\\..\\{0,700\\}\" KLN_1971.txt | head -3",
 "description": "SNS draxt entry; Klein 1971 tree"
}
```


### [2026-09-05T18:18:42.312Z] TOOL RESULT

```
* 

.AJj/.i/ftJi ,*£ ./:gar: Jj 
IY/V14 (4iJ/fc. Ill, 513-14) giray-offSj-^ gairi-: £» 

.c**- Jt 4:draxt: yiJ*X» 
{Mir. Man. drxt : >=t {GNPE. 121) * draxta- : fc. 
daraxt : ^ (/Irm. <7ram.l45) draxt: j-tj/Ill. 54 ;) 

■ A/A** -Yr-TA-TY-Yf-Xa/Y^ •(•>j±tS&») 



=== KLN 1971 tree ===
```


## [2026-09-05T18:18:52.286Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN triu/trum ===\"; grep -on \".\\{0,120\\}Goth\\.  triu.\\{0,500\\}\" KLN_1966.txt | head -3\ngrep -on \"trim,  adj\\..\\{0,400\\}\\|true,  adj\\..\\{0,400\\}\" KLN_1966.txt | head -4\necho \"=== FRS leaf for درونه ===\"\npython3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(t):\n    if 'درونه' in l: print('leaf',i)\nEOF",
 "description": "Klein tree/true/trim; FRS leaf"
}
```


### [2026-09-05T18:18:56.373Z] TOOL RESULT

```
=== KLN triu/trum ===
ugrep: error: error at position 90
\x80-\xbf][\x80-\xbf]*){0,500}
 exceeds complexity limits___/


40343:true,  adj.  —  ME.  trewe,  fr.  OE.  treowe,  triewe, ‘faithful,  trusty’,  which  is  rel.  to  OS.,  OFris. triuwi,  ON.  tryggr,  Dan.  tryg,  Swed.  trygg,  tro, Norw.  tru,  MDu.  (ghe)truwe,  (ghe)trouwe,  Du. (ge)trouw,  OHG.  gitriuwi,  MHG.  getriuwe,  triu¬ we,  G.  treu,  Goth,  triggws,  ‘faithful,  trusty’,  fr. I.-E.  base  *dru-,  ‘strong,  faithful’,  whence  also Gk.  Spoo;  (Hesychius),  
=== FRS leaf for درونه ===
leaf 217
leaf 465
leaf 560
```


## [2026-09-05T18:19:01.450Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"trewe\\|OE\\.  treo(w)\\|treow,  ‘tree\" KLN_1966.txt | head -5\nawk 'NR>=40330 && NR<=40350' KLN_1966.txt | grep -o \"tree,  n\\..\\{0,600\\}\" | head -2\ngrep -n \"tree,  n\\.\" KLN_1966.txt | head",
 "description": "Klein tree entry"
}
```


### [2026-09-05T18:19:03.183Z] TOOL RESULT

```
11466:8pu6?,  ‘an  oak;  a  tree’,  Goth,  triu,  OE.  trio, treow,  ‘tree’.  See  tree  and  cp.  dryad.  Cp.  also
12341:dryad,  n.,  a  forest  nymph.  —  L.  dryas  (pi.  drya- des),  fr.  Gk.  Spuap  (pi.  SpuaSsc),  fr.  Spue,  gen. 8puo<;,  ‘oak;  tree’,  which  is  rel.  to  Spupiop,  ‘oak- wood;  wood’,  8opu,  ‘stem,  tree,  beam,  shaft  of a  spear,  spear’,  SevSpeov,  ScvSpov  (dissimilated fr.  "Sep-Spef-ov),  ‘tree’,  fr.  I.-E.  base  *derew- (o)-,  *drew(o)-,  ‘tree,  wood’,  whence  also  OE. treo,  treow,  ‘tree,  wood’.  See  tree  and  cp.  dendro-, dory-,  the  first  element  in  druid  and  the  second element  in  deodar,  germander,  hamadryad, dryasdust,  n.,  a  dry,  pedantic  man.  —  Compound¬ ed  of  the  words  dry  as  dust.
12477:dure,  adj.,  hard;  severe  (archaic).  —  F.  dur,  fern. dure,  fr.  L.  durus,  'hard,  rough,  rude’,  prob. dissimilated  fr.  *dru-ros,  for  *dreu-ros,  and  lit. meaning  ‘as  hard  as  wood’,  fr.  I.-E.  base  *de- rew(o)-,  *drew(o)-,  *dru-,  ‘tree,  wood’,  whence also  Gk.  Spue,  ‘oak,  tree’,  86pu,  ‘stem,  tree,  beam, shaft  of  a  spear,  spear’,  OI.  dru-,  ‘wood,  wooden vessel',  ddru,  ‘wood’,  OE.  treo,  treow,  ‘tree, wood’.  See  tree  and  cp.  words  there  referred  to. Cp.  also  dour,  durable,  durain,  duralumin,  dura mater,  duramen,  durance,  duration,  duress,  dur¬ ing,  endure,  indurate,  obdurate,  perdure. dure,  intr.  v.,  to  last  (obsol.  or  poetic).  —  F.  durer, fr.  L.  durare,  ‘to  harden;  to  continue,  last’,  fr. durus,  ‘hard’.  See  dure,  adj. duress,  n.,  1)  imprisonment;  2)  compulsion.  — ME.  duresse,  fr,  obsol.  F.  duresse,  fr.  L.  duritia, ‘hardness,  severity,  austerity’,  fr.  durus.  See dure,  adj.,  and  -ess. durgah,  n.  —  See  dargah.
37010:stretto,  n.,  part  of  a  fugue  in  which  the  answer crowds  upon  the  subject  (music).  —  It.,  from the  adj.  stretto,  ‘drawn  tightly',  fr.  L.  strictus, pp.  of  stringere.  See  stringent  and  cp.  strict, strew,  tr.  v.  —  ME.  strewen,  strowen,  fr.  OE. streowian,  streawian,  strewian,  ‘to  scatter’,  rel. to  OS.  stroian ,  ON.  stra,  Dan.  stre,  Swed.  stro, MDu.  struwen,  strouwen,  strooyen,  Du.  strooien, OHG.  strewen,  MHG.  strouwen,  G.  streuen, Goth,  straujan,  fr.  I.-E.  base  *ster-,  *stor,  *str-, ‘to  spread  out,  extend,  strew’,  whence  also  OI. strnati,  strnSti,  starati,  ’strews,  scatters’,  Gk. axopvuvoa,  oxopevvuvai,  axptovvfjvai.,  ‘to spread  out’,  axpcotra,  ‘bedclothes,  mattress’, prop,  ‘anything  spread  out’,  L.  sternere  (pp. stratus),  ‘to  spread  out,  stretch  out’,  struere,  ‘to put  together,  construct’.  See  stratum  and  cp. words  there  referred  to.  Cp.  also  strand,  ‘shore’, strath,  straw,  stray.
38188:tapu,  n.  —  A  var.  of  taboo, tar,  n.,  a  viscous  liquid.  —  ME.  terre,  fr.  OE. teoru,  teru,  rel.  to  ON.  tjara,  Dan.  tjtere,  Swed. tjdra,  OFris.  tera,  MDu.  tar,  ter,  terre,  Du. teer,  G.  Teer.  These  words  orig.  meant  ‘per¬ taining  to  a  tree'.  They  derive  fr.  I.-E.  *derew(o)-, *drew(o)-,  ‘tree’,  whence  OI.  daru,  ‘wood’,  Gk. S6pu,  ‘beam,  shaft  of  a  spear,  spear’,  Spbq,  ‘tree, oak’,  Goth,  triu,  OE.  treow,  ‘tree’.  See  tree  and cp.  the  first  element  in  tarpaulin.
13289:entree,  entree,  n.,  1)  entrance,  right  to  enter; 2)  a  course  of  meal.  —  F.  entree.  See  entry, entremets,  n.,  side  dish,  extra  dish.  —  F.,  fr.  entre mets,  ‘between  dishes’.  See  ist  entre-  and  mess, entrench,  intrench,  tr.  v.  —  Lit.  ‘to  surround with  entrenchments’;  formed  fr.  ist  en-  (resp. in-,  ‘in’)  and  trench.
35295:singletree,  n.  —  Corruption  of  swingietree,  whose first  element  was  mistaken  for  the  adjective single.
37746:Derivative:  swingle,  tr.  v. swingletree,  n.,  a  whippletree.  —  Compounded  of swingle  and  tree.  Cp.  singletree, swink,  intr.  v.,  to  labor,  toil.  —  ME.  swinken ,  fr. swincan,  a  collateral  form  of  swingan,  ‘to  beat, strike,  whip’.  See  swing.
39969:trebuchet,  n.,  a  former  military  engine  for  hurling stones.  —  ME.  trebochet,  fr.  OF.  trebuchet,  ‘en¬ gine  for  hurling  stones’  (whence  F.  tribuchet, ‘bird  trap,  snare,  assay  balance’)  back  formation fr.  trebuchier,  trebucher  (F.  trebucher),  ‘to  stum¬ ble’,  a  hybrid  coined  fr.  the  pref.  tres-,  ‘over’,  fr. L.  trdns-  (see  trans-)  and  OF.  buc,  ‘body,  trunk’, fr.  Frankish  bilk,  ‘belly’,  which  is  rel.  to  ON. bukr,  OE.  buc,  etc.,  ‘belly’.  Cp.  OProven?.,  Sp., Port,  trabucar,  ‘to  stumble’,  which  are  of  the same  origin  as  OF.  trebuchier ;  It.  traboccare,  of s.m.,  was  influenced  in  form  by  an  erroneous association  of  this  word  with  It.  bocca,  ‘mouth’. See  buck,  ‘the  body  of  a  wagon’,  and  cp.  the second  element  in  sillabub  and  in  trabuco.  The suff.  -et  in  OF.  trebuchet  as  well  as  in  its  equiva¬ lents  of  s.m.  (OProven?.  trabuquet,  Sp.  trabu- quete )  has  diminutive  force  (see  -et). trecentist,  n.,  a  writer  or  artist  of  the  trecento.  — A  hybrid  coined  fr.  It.  trecento  (see  next  word) and  -ist,  a  suff.  of  Greek  origin, trecento,  n.,  the  14th  cent.,  an  important  period in  Italian  literature  and  art.  —  It.,  lit.  ‘three hundred’,  short  for  mil  trecento,  ‘one  thousand three  hundred’,  as  referring  to  the  period  be¬ ginning  with  1300.  Tre  derives  fr.  L.  tres,  ‘three’, cento,  fr.  L.  centum,  ‘a  hundred'.  See  three  and hundred  and  cp.  quattrocento,  cinquecento. trcchometer,  n.,  an  instrument  for  range  finding. —  Compounded  of  the  stem  of  Gk.  -rp£xetv> ‘to  run’,  and  pexpov,  ‘measure’.  Gk.  TpcycLv stands  in  gradational  relationship  to  -po-/6?,  ‘a wheel',  lit.  ‘that  which  runs  round’.  See  troche and  cp.  words  there  referred  to.  For  the  second element  see  meter,  ‘poetical  rhythm’, tree,  n.  —  ME.  tre,  tree,  fr.  OE.  treow,  ‘tree, wood’,  rel.  to  OS.  trio,  treo,  ON.,  OFris.  tre, Goth,  triu,  of  s.m.,  fr.  I.-E.  base  *derow(o)-, *drew(o)-,  ‘tree,  wood,  oak’,  whence  also  OI. dru-,  ‘wood’,  ddru,  ‘wood,  piece  of  wood,  spear’, drumah,  ‘tree’,  Avestic  dduru,  dru-,  ‘wood’, Toch.  or,  ‘wood’,  Hitt,  taru,  ‘tree,  wood’.  Arm. tram  (for  I.-E.  * drura-mo),  ‘firm’,  Gk.  8p0?, ‘tree,  oak’,  86pu,  ‘stem,  tree,  beam,  shaft  of  a spear,  spear’,  Homeric  Spupa  (neut.  pi.),  post- Homeric  8pOp6p,  ‘oakwood,  wood’,  Alb.  dru, ‘wood,  tree,  pole’,  drusk,  ‘oak’,  L.  larix  (for
```


## [2026-09-05T18:19:16.998Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%D8%A7%DB%8C%D8%B1%D9%87",
 "prompt": "Persian دایره: give the etymology — is it from Arabic دائرة dāʾira 'circle' (root د و ر)? Does the entry list a sense 'frame drum / tambourine'? Quote the etymology line."
}
```


## [2026-09-05T18:19:18.427Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/tree",
 "prompt": "Give the etymology of 'tree': Proto-Germanic *trewam, PIE root, and which other English words Etymonline lists under the same root (true, trust, truth, tray, trim, endure, druid). Quote the root statement."
}
```


### [2026-09-05T18:19:21.623Z] TOOL RESULT

```
# Etymology and Definitions of Persian دایره

**Etymology:** Yes, the entry confirms the word derives from Arabic. The etymology line states: "Borrowed from Arabic _[دَائِرَة](/wiki/%D8%AF%D8%A7%D8%A6%D8%B1%D8%A9#Arabic:_circle "دائرة")_ (dāʔira)."

**Tambourine Sense:** Yes, the entry lists this meaning. Under the Noun section, the third definition notes: "dayereh, tambourine"

The word ultimately traces back to the Arabic root د و ر (d-w-r), as indicated in the page's category tags.
```


### [2026-09-05T18:19:23.392Z] TOOL RESULT

```
# Etymology of "Tree"

**Proto-Germanic Origin:**
The word "tree" derives from Proto-Germanic *trewam, which itself comes from the PIE root *deru-.

**Root Statement:**
According to Etymonline, the root *deru- means "be firm, solid, steadfast," with "specialized senses" encompassing "wood, tree" and related wooden objects.

**Related English Words:**
The webpage lists these entries linking to "tree": beam, apple-tree, axle-tree, oak, palm-tree, pine-tree, saddletree, shade-tree, swingletree, tree-frog, tree-house, treeless, tree-ring, tree-top, and truth. However, the document does not explicitly confirm that true, trust, tray, trim, endure, or druid share this same root under *deru-.
```


## [2026-09-05T18:19:38.955Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%B1%D8%AE%D8%AA' --note 'page 121, root Deru 1, node 2: Persian deraxt etymology (MP draxt < PIr *draxta- \"firmly standing\", root *drag-/*dʰer-, not *deru-)' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%A7%D8%B1%D9%88' --note 'page 121, root Deru 1, node 2: Persian daru < MP darug < PIr *daarukah, perhaps from \"tree, wood\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%B3ru' --note 'page 121, root Deru 1: PIE *doru \"tree\", relation to *deru-/*drew- \"firm, solid\", Latin durus' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D9%81' --note 'page 121, root Deru 1, node 4: Arabic duff \"tambourine\" - native Semitic / Aramaic dappa < Sumerian, not from Persian dar' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/durable' --note 'page 121, root Deru 1, nodes 15-16: Latin durus/durare < PIE *dru-ro- variant of *deru-; duration' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/tree' --note 'page 121, root Deru 1, nodes 13-14: English tree < PGmc *trewam < PIE *deru- \"be firm, solid, steadfast\"' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%AF%D8%A7%DB%8C%D8%B1%D9%87' --note 'page 121, root Deru 1, node 3: Persian dayere \"tambourine\" borrowed from Arabic daira \"circle\" - contradicts dariye < dar \"wood\"' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-05T18:19:42.557Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/d58d2c826328be96.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/66b649f839865ec2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9477e578c1edd5fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/872c1421bf670119.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0a00a434bf92e870.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6947c70f175c60e2.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/090c8ee33a578a5d.txt
```


## [2026-09-05T18:19:48.705Z] TOOL CALL #60: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg121.png data/verification/sources/refs/ocr/BOOK/121.png && ls -la data/verification/sources/refs/ocr/BOOK/121.png; sed -n '1,80p' tools/verify_check.py",
 "description": "Copy page PNG and inspect verify_check"
}
```


### [2026-09-05T18:19:48.790Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 82335 Sep  5 14:19 data/verification/sources/refs/ocr/BOOK/121.png
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


## [2026-09-05T18:19:51.050Z] TOOL CALL #61: Bash

```json
{
 "command": "sed -n '80,140p' tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-05T18:19:51.100Z] TOOL RESULT

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


## [2026-09-05T18:20:49.686Z] AGENT

Now I'll write the verification file.


## [2026-09-05T18:32:41.194Z] TOOL CALL #62: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk121.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Deru 1\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *deru- / *dóru (gen. *dreu-s) 'tree, wood', with the adjectival variant *dreu-/*drū- 'firm, solid, hard'\",\n  \"note\": (\"Pokorny IEW p.214 heads the article 'deru-, dor-u-, dr(e)u-, drou-; dreu- : drū- ‚Baum‘, wahrscheinlich \"\n           \"urspr. und eigentlich ‚Eiche‘ ... dazu Worte für verschiedene Holzgeräte sowie für ‚kernholzartig hart, \"\n           \"fest, treu‘' — i.e. exactly Nourai's double gloss 'wood, tree, to be firm'. Watkins/AHD prints the root as \"\n           \"'deru- To be firm, solid, steadfast; hence specialized senses \\\"wood\\\", \\\"tree\\\"' [Pok. deru- 214], and Wiktionary \"\n           \"reconstructs the noun *dóru 'tree' beside the adjective *deru-/*drew- 'hard, firm'. Root name, language label \"\n           \"('Indo-European') and gloss are all correct, and POK:214 is the right page. The one substantive problem on this \"\n           \"chart is that Nourai lets the 'firm' sense swallow words that belong to the homophonous but distinct root \"\n           \"*dʰerǵʰ- / *dʰer- 'hold fast' (deraḵt, derežda) and a Semitic drum-name (daf).\")\n  ,\n  \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *deru- / *dóru «درخت، چوب» که گونهٔ صفتی آن *dreu-/*drū- \"\n              \"«سخت، استوار» است؛ پوکورنی در صفحهٔ ۲۱۴ همین دو معنا را یکجا می‌آورد و حدس می‌زند که معنای نخستین «بلوط» \"\n              \"بوده است. واتکینز (پیوست ریشه‌های هندواروپایی AHD) نیز ریشه را «استوار بودن، سخت بودن، و از آنجا \"\n              \"درخت و چوب» معنی کرده است. پس نام ریشه، برچسب زبانی و معنای آن در نمودار نورایی درست است؛ اما او به پشتوانهٔ \"\n              \"معنای «استواری» واژه‌هایی را هم زیر این ریشه آورده که به ریشهٔ جداگانهٔ *dʰer(ǵʰ)- «نگاه داشتن» می‌رسند \"\n              \"(درخت) و یکی هم (دف) سامی است.\")\n  ,\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/d%C3%B3ru\", \"https://www.etymonline.com/word/tree\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:214\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 225 (printed p.214): 'deru-, dor-u-, dr(e)u-, drou-; dreu- : dru- ‚Baum‘, wahrscheinlich urspr. und eigentlich ‚Eiche‘ ... dazu Worte für verschiedene Holzgeräte sowie für ‚kernholzartig hart, fest, treu‘'. Exactly the root, language and double gloss Nourai gives.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. deru-\", \"stance\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt line 369: '... Suffixed variant form *dru-ro- in Latin durus, hard ... Lengthened zero-grade form *dru- in Greek drus, oak ... O-grade form *doru- in Sanskrit daru, wood, timber: DEODAR. [Pok. deru- 214.]' — same root, same Pokorny page.\"},\n    {\"src\": \"WLD\", \"where\": \"WP. I 804 ff. (cited by Pokorny at the head of the deru- article)\", \"stance\": \"supports\",\n     \"note\": \"Mann IEC.txt line 2483 s.v. 'dru- (radical) ‚timber, tree‘' cites 'WP I, 804' for the same material; Walde-Pokorny I 804 is the parent article of Pokorny 214.\"},\n    {\"src\": \"IEC\", \"where\": \"IEC.txt line 2483, s.v. dru-\", \"stance\": \"supports\",\n     \"note\": \"Mann: 'dru- (radical) ‚timber, tree‘. Cf. druu-, dru-to-, etc. WP I, 804. Skt. dru; Av. dru ‚timber; spear‘; Gk. drūs ‚oak‘; Alb. dru ...'.\"},\n    {\"src\": \"SYN\", \"where\": \"SYN.txt line 1549 (Buck 3.51 'tree')\", \"stance\": \"supports\",\n     \"note\": \"Buck: 'Skt. daru-, dru- ‚wood‘, druma- ‚tree‘, Av. dauru- ‚piece of wood, club‘' beside OCS drevo, Russ. derevo.\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"dru, dâuru, derežda, draxta; dârug\",\n  \"verdict\": \"transcription_suspect\",\n  \"derivation\": (\n    \"Two of the four 'tree, wood' words are right, two are not, and the fifth word is not Avestan at all. \"\n    \"(a) Av. dru- and dāuru- n. 'wood, piece of wood, log' are the regular Avestan reflexes of PIE *doru/*dreu- \"\n    \"(Bartholomae AiW s.v.; the word is quoted at V.13.30 'tašəm dāuru ... ‚ein Stück Holz‘'), and Kent, Klein and \"\n    \"Buck all cite Av. dāuru- next to Skt. dāru- and Gk. dóru — confirmed. \"\n    \"(b) 'derežda' is not an Avestan form. What the book means is Av. dərəzra-/drazra- adj. 'fest, stark, tüchtig' \"\n    \"(Bartholomae AiW, line 13564 of BRT.txt), which belongs to the verb darəz- 'to bind, make fast' (PIE *derǵʰ-), \"\n    \"not to *deru-; and the shape -žda for -zra- is a misreading of the printed Latin transcription. \"\n    \"(c) Av. draxta- is attested only as the past participle of dranj-/drənj- 'to make firm, fix; to memorise' \"\n    \"(BRT.txt line 14069 'PPfP. *draxta-'), never as a noun 'tree'; Tavoosi's Shayast-ne-Shayast glossary (SNS p.318) \"\n    \"explicitly writes the tree-word's ancestor with an asterisk, '*draxta-', i.e. unattested. Middle Persian draxt \"\n    \"'tree' (MacKenzie p.25) goes back to Proto-Iranian *draxta- 'firmly standing' from *drag-/*dʰer- 'hold', a \"\n    \"different root. \"\n    \"(d) 'dārug' is Middle Persian, not Avestan: MacKenzie, Concise Pahlavi Dictionary p.25 'dārūg [dʾлwkʼ | M dʾrwg, \"\n    \"N dārū] drug, medicament'. \"\n    \"I checked the printed page (pdf 121 = book p.91, rendered at 200 dpi): the book itself prints \"\n    \"'dru, dâuru, derežda, draxta : tree, wood' and 'dârug : medicine from plants', so the extraction is faithful and \"\n    \"the odd forms and the language label are Nourai's.\"),\n  \"derivation_fa\": (\n    \"از چهار صورتی که نورایی اوستایی خوانده، دو تا درست است و دو تا نه. اوستایی dru- و dāuru- «چوب، پارهٔ چوب» \"\n    \"(بارتولومه، فرهنگ ایرانی باستان) دنبالهٔ مستقیم *dóru هندواروپایی است و کنت، کلاین و باک نیز همین را گفته‌اند. \"\n    \"اما «derežda» صورتی اوستایی نیست؛ مقصود dərəzra-/drazra- «استوار، سخت» است که از ستاک darəz- «بستن، محکم کردن» \"\n    \"می‌آید و ریشه‌اش جداست؛ draxta- هم در اوستا تنها صفت مفعولی فعل dranj- «استوار کردن، از بر کردن» است و به معنای «درخت» \"\n    \"نیامده است (در واژه‌نامهٔ شایست ناشایست صفحهٔ ۳۱۸ هم با ستاره و علامت پرسش «*draxta-» آمده). واژهٔ dārūg هم پهلوی \"\n    \"است نه اوستایی (مکنزی، صفحهٔ ۲۵). تصویر صفحهٔ چاپی (ص ۹۱ کتاب) را دیدم: خود کتاب همین صورت‌ها را چاپ کرده؛ پس خطا از کتاب است نه از \"\n    \"خوانش اسکن.\"),\n  \"error_in\": \"book\",\n  \"book_prints\": \"dru, dâuru, derežda, draxta : tree, wood / dârug : medicine from plants  [Avestan]\",\n  \"correct_form\": \"Av. dru-, dāuru- 'wood' (correct); Av. dərəzra-/drazra- 'firm' (belongs to darəz-, not here); Av. draxta- only as ppp. of dranj-; MP dārūg (not Avestan)\",\n  \"sources\": [W + \"%D8%AF%D8%B1%D8%AE%D8%AA\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:214\", \"status\": \"partial\",\n     \"note\": \"POK_01.txt leaf 225 lists 'ai. dāru n. ‚Holz‘ ... av. dāuru ‚Baumstamm, Holzstück, Waffe aus Holz‘ ... av. drvaena- ‚hölzern‘' — supports dru/dāuru, but Pokorny nowhere lists an Avestan 'derežda', 'draxta' or 'dārug' under deru-.\"},\n    {\"ref\": \"KLN:1644\", \"status\": \"supports\",\n     \"note\": \"Klein 1966 s.v. 'tree': 'fr. I.-E. base *derow(o)-, *drew(o)-, ‚tree, wood, oak‘, whence also OI. dru-, ḍāru ... Avestic dāuru, dru-, ‚wood‘, Toch. or, Hitt. taru' (KLN_1966.txt, tree entry). Found by headword; the 1966 two-volume pagination could not be checked against the leaf, so the page number itself is unverified.\"},\n    {\"ref\": \"SNS:318\", \"status\": \"partial\",\n     \"note\": \"SNS index (SNS.txt lines 29302, 33234) gives 'draxta-(?) 318/20' and 'draxt 318/21'; the glossary entry (SNS.txt line 17345f.) reads 'draxt: درخت {Mir. Man. drxt} ... *draxta-'. Tavoosi marks the Avestan antecedent with an asterisk and a question mark — he does NOT attest Av. draxta-.\"},\n    {\"ref\": \"ETM:65\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi: no digital copy on any permitted platform (refs_online.json: 'RE-SEARCH 2026-09: no digital copy').\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt line 13564 (dərəzra-) and line 14069 (dranj-/*draxta-)\", \"stance\": \"contradicts\",\n     \"note\": \"'j. dərəzra-, drazra- Adj. (fem. °rā-) ‚fest, stark, tüchtig‘' and, s.v. dranj-, 'PPfP. *draxta- ‚festigen, kräftigen, bestärken‘' — both belong to darəz-/dranj-, not to dāuru-.\"},\n    {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt p.25 s.v. draxt, dārūg\", \"stance\": \"contradicts\",\n     \"note\": \"'draxt [drxt | M drxt, N diraxt] tree' and 'dārūg [dʾлwkʼ | M dʾrwg, N dārū] drug, medicament' — MacKenzie files both as Middle Persian; Nourai's box labels them Avestan.\"},\n    {\"src\": \"KNT\", \"where\": \"KNT.txt line 5530, Lexicon s.v. dāru-\", \"stance\": \"supports\",\n     \"note\": \"'dāru- sb. ‚wood‘: Av. dāuru-, Skt. dáru-, cf. Gk. δόρυ ‚spear‘.'\"},\n    {\"src\": \"SYN\", \"where\": \"SYN.txt line 1549\", \"stance\": \"supports\",\n     \"note\": \"Buck: 'Skt. daru-, dru- ‚wood‘, druma- ‚tree‘, Av. dauru- ‚piece of wood, club‘'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Persian\",\n  \"words\": \"dorūd 1; dorūdgar, dorga; dâr 2; dârkūb; deraxt; dârū\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"Six words, three verdicts. \"\n    \"dār 2 «دار» 'wood, timber, gallows-tree' is confirmed: Mo'in's footnote in Borhan-e Qate' at the head of the \"\n    \"دار entry (BQT_v2_pages.txt leaf 269 ≈ printed p.809 — Nourai's own page) reads 'پهلوی dār «تاوادیا ۹۱۲»، \"\n    \"اوستا dāuru- (چوب)، ... هندی باستان dāru- (چوب)، کردی و بلوچی dār'; Horn no. 522 (p.116, the page Nourai cites) \"\n    \"'dār ‚Baumstamm, Holz‘, aw. dāuru ‚Holz‘; phlv. dār, dārīn ‚hölzern‘; ai. dāru ‚Holz‘'; MacKenzie p.25 'dār [dʾл | \"\n    \"M dʾr, N ~] tree, gallows; wood'. Old Iranian *dāru > MP dār > NP dār with no change but the loss of the \"\n    \"case-ending. dārkūb «دارکوب» 'woodpecker' is a transparent New Persian compound dār 'wood' + kūb- (present stem of \"\n    \"kūftan 'to beat'), listed in Borhan at leaf 272 ≈ p.812; confirmed. \"\n    \"dorūd 1 'timber' and dorūdgar/dorgar «درودگر (دُرگَر)» 'carpenter' are plausible rather than certain. Borhan \"\n    \"(leaf 300 ≈ p.840–843) has 'درگر — باکاف فارسی بروزن دختر، درودگر را گویند' with the note \"\n    \"'مخفف «درودگر»', so dorgar = dorūdgar is right; but the first element is disputed — it may be a *dru- \"\n    \"'wood' noun (so Nourai, and Horn's np. durūk 'thin wood' is compared to Skt. drú-), or the verbal noun of \"\n    \"dorūdan/dorū- 'to cut, mow, reap' (MP drūdan, drūn-, MacKenzie p.25), in which case 'carpenter' is 'wood-cutter' \"\n    \"and the root is *dreu- 'to cut'. \"\n    \"deraxt «درخت» is disputed: MP draxt < Proto-Iranian *draxta- 'firmly standing', from *drag-/PIE *dʰer-ǵʰ- 'to \"\n    \"hold, make fast' (Wiktionary, following Rastorgueva-Edel'man and Hasandust); the Avestan comparandum is the ppp. \"\n    \"of dranj- 'make firm', not a word for 'wood'. Nourai's chart can only place it here because his root box merges \"\n    \"'wood' with 'be firm'. \"\n    \"dārū «دارو» (with the derivative داروخانه) is plausible: MP dārūg 'drug, medicament' (MacKenzie p.25), \"\n    \"Parthian dʾлwg 'plant, tree', Proto-Iranian *dā́rukah, 'perhaps' a -ka- derivative of *dāru- 'wood, plant' \"\n    \"(Wiktionary, citing Rastorgueva-Edel'man II 359) — which is Nourai's route; but Horn no. 523 (same p.116) files \"\n    \"dārū under √dʰar- 'to hold', comparing Av. drva- 'healthy', i.e. exactly the alternative Nourai himself flags in \"\n    \"his NOTE ('See \\\"Dher 1\\\"'). Modern opinion leans to Nourai's version ('medicine made from plants'), so the NOTE's \"\n    \"hesitation is well placed but the arrow drawn here is the better one.\"),\n  \"derivation_fa\": (\n    \"شش واژه و سه حکم. «دار» درست است: حاشیهٔ معین بر برهان قاطع (ص ۸۰۹، همان صفحه‌ای که نورایی ارجاع داده) می‌نویسد \"\n    \"«پهلوی dār، اوستا dāuru- (چوب)، هندی باستان dāru-» و هرن (شمارهٔ ۵۲۲ ص ۱۱۶) و مکنزی هم همین را می‌گویند؛ \"\n    \"«دارکوب» نیز مرکب روشن فارسی نو است (دار + کوبِ از کوفتن). «درودگر/دُرگَر» در برهان هست و معین آن را مخفف \"\n    \"درودگر دانسته، اما جزء نخست را هم می‌توان از *dru- «چوب» گرفت و هم از درودن/درو- «بریدن، درویدن»؛ پس با احتیاط \"\n    \"پذیرفتنی است. «درخت» را پژوهش امروزی رد می‌کند: فارسی میانهٔ draxt از ایرانی باستان *draxta- «استوارایستاده» \"\n    \"از ریشهٔ *dʰerǵʰ- «نگاه داشتن، محکم کردن» است نه از *deru- «چوب». «دارو» از پهلوی dārūg و ایرانی باستان \"\n    \"*dārukah است که به احتمال مشتق پسوندی *dāru- «گیاه، چوب» است (پس درست، ولی قطعی نیست؛ هرن آن را به √dʰar- می‌برد، \"\n    \"همان که خود نورایی در یادداشت «Dher 1» هشدار داده است).\"),\n  \"sources\": [W + \"%D8%AF%D8%B1%D8%AE%D8%AA\", W + \"%D8%AF%D8%A7%D8%B1%D9%88\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:809,843\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt leaf 269 (≈ printed 809, start of the دار entries): Mo'in's footnote 9 'پهلوی dār «تاوادیا ۹۱۲»، اوستا dāuru- (چوب)، قس: ارمنی ... هندی باستان dāru- (چوب)، کردی و بلوچی dār ... و رک: هوبشمان ۲۲۵'. Leaf 300 (≈ 843): 'درگر = باکاف فارسی بروزن دختر، درودگر را گویند' + footnote 'مخفف «درودگر»'. Both pages say what the arrow says.\"},\n    {\"ref\": \"HRN:116\", \"status\": \"partial\",\n     \"note\": \"HRN.txt leaf 137 = printed p.116: no. 522 'dār ‚Baumstamm, Holz‘, aw. dāuru ‚Holz‘; phlv. dār, dārīn ‚hölzern‘; ai. dāru ‚Holz‘' — supports dār. But the very next entry, no. 523 'dārū, dārūt ‚Arznei‘ ... √dʰar- ‚halten‘, vergl. aw. drva- ‚gesund‘; phlv. dārūk ‚Arznei‘', puts dārū under a different root.\"},\n    {\"ref\": \"FVF:256\", \"status\": \"not_checked\",\n     \"note\": \"Emam Shushtari, Farhang-e Vazheha-ye Farsi dar Zaban-e Arabi: no downloadable copy (refs_online.json gives only noorlib/ketabnak viewers behind login).\"},\n    {\"ref\": \"ETM:65\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi: no digital copy available.\"},\n    {\"ref\": \"FSF:177\", \"status\": \"partial\",\n     \"note\": \"FSF_pages.txt (Noushin, Vazhe-namak) line 1981 glosses a Shahnameh word as 'مخفف اره، افزار درودگری' — confirms dorūdgar as the Shahnameh word behind Nourai's Ferdowsi couplet, but gives no etymology.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt p.25\", \"stance\": \"partial\",\n     \"note\": \"'dār [dʾл | M dʾr, N ~] tree, gallows; wood'; 'darēn [dʾлynʼ | M dʾrwyn] wooden'; 'dārūg ... drug, medicament'; but 'draxt [drxt | M drxt, N diraxt] tree' is a separate lemma — MacKenzie does not connect draxt to dār.\"},\n    {\"src\": \"HRN\", \"where\": \"HRN.txt p.116 nos. 522–523\", \"stance\": \"partial\", \"note\": \"see ref_check: supports dār, contradicts dārū.\"},\n    {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt leaf 272 (≈ p.812)\", \"stance\": \"supports\",\n     \"note\": \"the دارکوب / دارفلفل / دارکدو block of دار-compounds sits here, showing dār 'wood' as a living first element.\"},\n    {\"src\": \"SNS\", \"where\": \"SNS.txt line 17345, p.318\", \"stance\": \"contradicts\",\n     \"note\": \"'draxt: درخت {Mir. Man. drxt} ... *draxta-' — the Avestan antecedent of draxt is reconstructed, not attested, and is not dāuru-.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\",\n     \"note\": \"grep for درودگر / دارکوب in the Aryanpur OCR returns no headword entry for these compounds.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"dârîyeh\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"Nourai (following Emam Shushtari, FVF:256) takes «داریه» dārīyeh 'wooden hoop, tambourine with a wooden rim' \"\n    \"as a dār 'wood' + -īya derivative, and makes it the source of Arabic daf. Modern lexicography knows the \"\n    \"instrument-name in Persian as «دایره» dāyere, an Arabic loan: Arabic دائرة dāʾira 'circle' (root د-و-ر d-w-r \"\n    \"'to turn'), the frame drum being named from its round frame; Wiktionary gives 'Borrowed from Arabic دَائِرَة \"\n    \"(dāʾira)' and lists the sense 'dayereh, tambourine'. داریه is best explained as a variant spelling of دایره \"\n    \"(the hamza on the yāʾ dropped and the word re-read as a dār- derivative) — i.e. a folk etymology in the \"\n    \"direction Nourai builds on, not its source. Neither Borhan-e Qate' (no داریه headword in BQT_v1/v2_pages.txt) \"\n    \"nor Mo'in's footnotes give the word, and the derivation dārīyeh → Arabic daf is phonetically impossible \"\n    \"(there is no path from dārīya to a geminate-fāʾ stem duff).\"),\n  \"derivation_fa\": (\n    \"نورایی به پیروی امام شوشتری «داریه» را مشتق از «دار» (چوب) می‌داند و آن را سرچشمهٔ «دف» عربی می‌گیرد. اما نام این ساز \"\n    \"در فارسی «دایره» است که معرّب‌واره‌ای نیست بلکه خود وام‌واژهٔ عربی دائرة «حلقه، دایره» از ریشهٔ د-و-ر است و ساز را از روی \"\n    \"قاب گردش چنین نامیده‌اند (ویکی‌واژه). پس «داریه» گونه‌ای از همان «دایره» است که بر اثر ریشه‌شناسی عامیانه \"\n    \"به «دار» وصل شده، نه اصل آن. این واژه در برهان قاطع سرمدخل نیست و تبدیل dārīya به duff عربی از نظر آوایی ناممکن است. \"\n    \"پژوهش امروزی ادعای نورایی را نمی‌پذیرد.\"),\n  \"sources\": [W + \"%D8%AF%D8%A7%DB%8C%D8%B1%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"FVF:256\", \"status\": \"not_checked\",\n     \"note\": \"Emam Shushtari 1347 is not available in full text (refs_online.json: noorlib/ketabnak viewers only, no downloadable copy). This is the only reference Nourai gives for the node.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"BQT_v1_pages.txt / BQT_v2_pages.txt, grep 'داریه'\", \"stance\": \"silent\",\n     \"note\": \"no hit anywhere in the OCR of Borhan vols 1–2; the word is not a Borhan headword.\"},\n    {\"src\": \"MON\", \"where\": \"vajehyab/abadis — دایره\", \"stance\": \"contradicts\",\n     \"note\": \"Mo'in and the standard dictionaries file the frame drum under دایره with the origin tag [ع.] (Arabic), matching Wiktionary's 'Borrowed from Arabic دَائِرَة (dāʾira)'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. toph\", \"stance\": \"contradicts\",\n     \"note\": \"Klein routes the Semitic drum-name through Hebrew/Aramaic, with no Iranian wooden-hoop word anywhere in the family.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Arabic\", \"words\": \"daf\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\n    \"Arabic دُفّ duff 'frame drum, tambourine' is not a loan from Persian dārīya. Three independent lines all point \"\n    \"elsewhere: (1) Klein, s.v. 'toph': 'Heb. tōph, ‚timbrel, tambourine‘, rel. to Aram. tuppā, of s.m., Arab. duff, \"\n    \"‚drum‘; of imitative origin' — a common-Semitic onomatopoeic drum-name (Hebrew תֹּף tōp̤, Akkadian/Aramaic tuppu). \"\n    \"(2) Mo'in's footnote in Borhan-e Qate' at the دف entry (BQT_v2_pages.txt leaf 329 ≈ printed p.869, the very page \"\n    \"Nourai cites): 'در (عر) دف (آلة طرب) از عبری «تف» مشتق از «تفف» بمعنی زد و کوبید', with a second note \"\n    \"tracing the 'board, plate' sense to Sumerian dub → Akkadian → Aramaic → Arabic دف (citing Zimmern, \"\n    \"Akkadische Fremdwörter p.19). (3) Wiktionary treats duff as inner-Arabic, 'a more primitive form of دَفَعَ \"\n    \"(dafaʿa, to push, to propel)', with the possible Aramaic دفا dappā 'board' (< Sumerian DUB) alongside. \"\n    \"The only source that goes the other way, Asbaghi's Persische Lehnwörter im Arabischen p.223, still does not \"\n    \"support Nourai: 'duff: ‚Tamburin, Handtrommel‘ aus dem pers. daf ← aram.' — Persian daf is itself Aramaic there, \"\n    \"and nothing in the chain touches dār 'wood'. So the arrow dārīyeh → daf must be rejected: the word is Semitic.\"),\n  \"derivation_fa\": (\n    \"«دُفّ» عربی وام‌گرفته از فارسی «داریه» نیست. کلاین آن را هم‌ریشهٔ عبری تُف (tōp̤) و آرامی tuppā و از ریشهٔ سامی \"\n    \"و نام‌آوا (onomatopoeic) می‌داند؛ معین در حاشیهٔ برهان قاطع (ص ۸۶۹، دقیقاً همان صفحه‌ای که نورایی ارجاع داده) می‌نویسد \"\n    \"«دف (آلة طرب) از عبری تف مشتق از تفف بمعنی زد و کوبید» و معنای «لوحه» را از سومری dub به اکدی و آرامی و سپس عربی \"\n    \"پی می‌گیرد. اصبغی هم که آن را از فارسی گرفته، فارسیِ آن را آرامی می‌داند نه مشتق «دار». پس پژوهش امروزی این پیوند را رد \"\n    \"می‌کند و واژه را سامی می‌داند.\"),\n  \"sources\": [W + \"%D8%AF%D9%81\"],\n  \"ref_check\": [\n    {\"ref\": \"FVF:256\", \"status\": \"not_checked\",\n     \"note\": \"Emam Shushtari not available in full text; it is the only reference Nourai cites for this arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. toph\", \"stance\": \"contradicts\",\n     \"note\": \"'toph, n., a small drum (music). — Heb. toph, ‚timbrel, tambourine‘, rel. to Aram. tuppā, of s.m., Arab. duff, ‚drum‘; of imitative origin.'\"},\n    {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt leaf 329 ≈ printed p.869, Mo'in's footnotes 6–7\", \"stance\": \"contradicts\",\n     \"note\": \"'در (عر) دف (آلة طرب) از عبری «تف» مشتق از «تفف» بمعنی زد و کوبید' and 'دوب در زبان سومری بمعنی لوحه و خط است. از این زبان وارد اکدی شده ... وارد آرامی شده ... بعدها در زبان عربی «دف» شده' (citing Zimmern, Leipzig, p.19).\"},\n    {\"src\": \"PLA\", \"where\": \"PLA_asbaghi_1988_ia_djvu.txt line 9582 (p.223)\", \"stance\": \"partial\",\n     \"note\": \"'duff: ‚Tamburin, Handtrommel‘ aus dem pers. daf ← aram.' — Asbaghi does make Arabic duff a Persian loan, but derives the Persian word from Aramaic, not from dār 'wood', so it does not support Nourai's arrow.\"},\n    {\"src\": \"AFA\", \"where\": \"AFA.txt (Fraenkel), grep 'Pauke'/'Tamburin'\", \"stance\": \"silent\",\n     \"note\": \"only one hit ('… entlehnt sein, … ‚Pauke‘ ist wohl Entlehnung'), not the duff article; Fraenkel gives no Iranian source for duff.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Persian\", \"words\": \"daf; šandaf\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"The edge itself is right: New Persian دَف daf 'tambourine' is a straight loan from Arabic دُفّ duff, and Borhan-e \"\n    \"Qate' marks it '(عر)' — Mo'in's footnote on the entry (BQT_v2_pages.txt leaf 329 ≈ printed p.869, Nourai's page) \"\n    \"treats دف as the Arabic word, and adds that the verb دفتن means 'to play the daf'. Arabic u > Persian a in the \"\n    \"closed syllable of a CVCC loan is regular (duff > daf). شَندف šandaf 'domestic tambourine' is attested in Borhan \"\n    \"as شندف/شندفه (BQT vol. 3, incoming/BQT/BQT_v3_pages.txt line 6886 'شندفه - بفتح اول بر وزن اشرف' with the \"\n    \"verse '... شندف زند و زرین مزمار'), so the word is real, but no source I could reach analyses it as شن- + دف; \"\n    \"Nourai's own cross-reference to 'Gwhen 1' for the first element is his conjecture. What is wrong is not this \"\n    \"arrow but its ancestry: since Arabic duff is Semitic (see node 4), the Persian word is a Semitic loan and does \"\n    \"not descend from *deru-. Nourai's own NOTE ('See \\\"Dup\\\" for another possible root') half-concedes this.\"),\n  \"derivation_fa\": (\n    \"پیوند خودِ این دو جعبه درست است: «دَف» فارسی وام‌واژهٔ عربی دُفّ است و برهان قاطع (ص ۸۶۹) آن را با نشانهٔ «(عر)» \"\n    \"آورده است؛ تبدیل ضمّهٔ عربی به فتحهٔ فارسی در وام‌واژه‌های یک‌هجایی قاعده‌مند است. «شَندف» نیز در برهان (جلد ۳) به صورت \"\n    \"شندف/شندفه آمده، ولی تجزیهٔ آن به «شن + دف» در هیچ منبعی تأیید نشد. اشکال در این پیکان نیست بلکه در تبار آن است: \"\n    \"چون دفّ عربی سامی است، دفِ فارسی هم به *deru- نمی‌رسد؛ پس با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W + \"%D8%AF%D9%81\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:869\", \"status\": \"partial\",\n     \"note\": \"BQT_v2_pages.txt leaf 329 (its foot carries 'بقیه در صفحهٔ ۸۷۰', so this is printed p.869) opens the بیان دهم 'در دال بی نقطه با فا' and has دف with 'دف زدن', 'دفتین'. The page does have the word Nourai wants, but its footnote derives Arabic دف from Hebrew/Sumerian, not from Persian داریه.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"incoming/BQT/BQT_v3_pages.txt lines 6886, 6922\", \"stance\": \"supports\",\n     \"note\": \"'شندفه - بفتح اول بر وزن اشرف' and the verse '... برکه لوبت میمین شندف زند و زرین مزمار' — شندف is a genuine Borhan headword.\"},\n    {\"src\": \"PLA\", \"where\": \"PLA_asbaghi_1988_ia_djvu.txt p.223 s.v. duff / daffāf\", \"stance\": \"partial\",\n     \"note\": \"Asbaghi lists 'daffāf: ‚Tamburinschläger‘ nom. agent. v. duff' — the word family is Arabic; he traces its ultimate source to Aramaic.\"},\n    {\"src\": \"MON\", \"where\": \"Mo'in's footnote quoted at BQT leaf 329\", \"stance\": \"contradicts\",\n     \"note\": \"same footnote as above; Mo'in marks Persian دف as '(عر)' and its ultimate source as Semitic/Sumerian.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Avestan\", \"words\": \"drva; upa-drava; drva-asti; druw-išta\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"The head-word is solid: Bartholomae, AiW (BRT.txt line 14215) '¹drva-, p. duruva- Adj. (fem. °vā-) ‚gesund, \"\n    \"heil‘', i.e. Avestan druua- 'healthy, whole' beside Old Persian duruva- 'firm, secure' — the adjectival \"\n    \"*dru-uo- of *deru- 'firm, solid'; Pokorny 214 lists it with 'ai. dhruvá- ‚fest, bleibend‘ (dh- durch volksetym. \"\n    \"Anschluß an dhar-) = av. dr(u)vō, apers. duruva ‚gesund, heil‘'. The three compounds are Nourai's own and are \"\n    \"not attested in those shapes. Bartholomae has drva-tāt- f. 'Gesundheit, Heiltum' (line 14225), drvō.stātay- \"\n    \"'gesunden, heilen Stand habend' (line 14249) and drva-fšav- (line 14230), but no upa-drva-/upa-drava-, no \"\n    \"drvō.asti-, and no superlative drvišta-; 'upa-drava' as 'to good health, good-bye' looks like a back-formation \"\n    \"from New Persian be-drūd rather than an Avestan citation (Sanskrit upadrava- in fact means 'calamity'). So the \"\n    \"node's core derivation is confirmed and its three sub-forms are unverified reconstructions.\"),\n  \"derivation_fa\": (\n    \"سرواژه درست است: بارتولومه در فرهنگ ایرانی باستان می‌آورد «drva-، پارسی باستان duruva- ، صفت، «تندرست، سالم»»؛ \"\n    \"پوکورنی نیز در ص ۲۱۴ همین را با سنسکریت dhruvá- مقایسه می‌کند. این صورت از گونهٔ صفتی *dru-uo- ریشهٔ *deru- «استوار» \"\n    \"می‌آید. اما سه ترکیب دیگر (upa-drava، drva-asti، druw-išta) در متون اوستایی به این شکل گواهی نشده‌اند؛ آنچه هست \"\n    \"drva-tāt- «تندرستی» و drvō.stātay- است. پس هستهٔ گزاره درست است و زیرشاخه‌ها بازساختهٔ خود نورایی است و با احتیاط \"\n    \"پذیرفتنی است.\"),\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/d%C3%B3ru\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:214\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 225 (p.214): 'dhruvá- ‚fest, bleibend‘ (dh- durch volksetym. Anschluß an dhar- ‚halten, stützen‘ = av. dr(u)vō, apers. duruva ‚gesund, heil‘, vgl. aksl. sŪdravŭ)' — exactly the arrow root → Av. drva-.\"},\n    {\"ref\": \"ETM:65\", \"status\": \"not_checked\", \"note\": \"Abolghasemi, Risheh-shenasi: no digital copy available.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt lines 14215, 14225, 14249, 14230\", \"stance\": \"partial\",\n     \"note\": \"'¹drva-, p. duruva- Adj. ‚gesund, heil‘' and 'drva-tāt- f. ‚Gesundheit, Heiltum‘' are there; 'drvō.stātay- Adj. ‚gesunden, heilen Stand habend‘(?)' and 'drva-fšav-' are the only drva- compounds; no upa-drva-, no drvō.asti-, no drvišta-.\"},\n    {\"src\": \"KNT\", \"where\": \"KNT.txt Lexicon s.v. duruva-\", \"stance\": \"supports\",\n     \"note\": \"Kent files OP duruva- 'firm, secure' with Av. drva-, the pair Bartholomae gives; the Old Persian and Avestan forms match.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. deru-\", \"stance\": \"supports\",\n     \"note\": \"Watkins glosses the root itself 'To be firm, solid, steadfast', which is the sense drva- carries.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": \"Persian\", \"words\": \"dorūd 2; bedrūd; dorost\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"All three descend from Avestan druua-/drvatāt- through Middle Persian. دُرود dorūd 'greeting, benediction': \"\n    \"Av. drvatāt- f. 'Gesundheit' (Bartholomae AiW) > MP drūd/drōd, glossed by MacKenzie p.26 'drōd [SLM < A šlm; \"\n    \"dlwtʼ | M drwd, N darōd] health, well-being, prosperity, peace'; Mo'in's footnote on the درو (صلوات) entry of \"\n    \"Borhan-e Qate' (BQT_v2_pages.txt leaf 302 ≈ printed p.842, one of Nourai's pages) gives 'پهلوی drūt (صحت، \"\n    \"آرامش) ... و drōd (آرزوی خیر و برکت) از ریشهٔ *drvatāt و از اوستا drvatāt- «بارتولمه»، ارمنی drut', and Horn no. 555 \"\n    \"(p.124) 'aw. drvatāt- ‚Gesundheit‘; phlv. drūt'. The semantic step is 'health' → 'a wish of health' → 'greeting', \"\n    \"the same one that turns Latin salus into salutation. بدرود bedrūd is MP pad drōd 'in health' → 'farewell'; \"\n    \"Noushin's Vazhe-namak notes 'معنای اصلی بدرود آرزومندی تندرستی' (FSF_pages.txt line 6790). درست dorost is \"\n    \"MP drust 'right; well, healthy' (MacKenzie p.26 'drust [drw(y)stʼ | (M dryst), N durust]'), from *druušta-, \"\n    \"and Pokorny names it on the very second page Nourai cites: 'npers. durušt ‚hart, stark‘, durust ‚gesund, ganz‘' \"\n    \"(POK p.216). Old Iranian intervocalic/-Cv- clusters give MP -ust-, and NP shifts the stress-vowel to o.\"),\n  \"derivation_fa\": (\n    \"هر سه واژه از اوستایی druua-/drvatāt- و از راه فارسی میانه آمده‌اند. «دُرود» از فارسی میانهٔ drūt/drōd «تندرستی، \"\n    \"آرامش، آرزوی خیر» است که خود از drvatāt- اوستایی می‌آید؛ حاشیهٔ معین بر برهان قاطع (ص ۸۴۲) و هرن (شمارهٔ ۵۵۵ ص ۱۲۴) و \"\n    \"مکنزی (ص ۲۶) همین را می‌گویند. تحول معنایی «تندرستی ← آرزوی تندرستی ← سلام» همان است که در لاتین salus ← salutatio \"\n    \"دیده می‌شود. «بدرود» از pad drōd «به تندرستی» است (نوشین در واژه‌نامک: «معنای اصلی بدرود آرزومندی تندرستی») و «درست» \"\n    \"از فارسی میانهٔ drust؛ پوکورنی در ص ۲۱۶ خود به «npers. durušt، durust ‚gesund, ganz‘» تصریح کرده است. ادعای نورایی درست است.\"),\n  \"sources\": [W + \"Reconstruction:Proto-Indo-European/d%C3%B3ru\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:214,216\", \"status\": \"supports\",\n     \"note\": \"POK_01.txt leaf 227 (printed p.216, in the deru- article): '... die s-Bildung ist alt wegen npers. durušt ‚hart, stark‘, durust ‚gesund, ganz‘'; p.214 gives av. dr(u)vō, apers. duruva 'gesund, heil'. Both cited pages carry the claim.\"},\n    {\"ref\": \"BQT:840,842,843\", \"status\": \"supports\",\n     \"note\": \"BQT_v2_pages.txt leaf 302 (≈ printed 842) 'درو ۳ = بروزن سرود، بمعنی صلوات است' with Mo'in's footnote 'پهلوی drūt (صحت، آرامش) ... drōd (آرزوی خیر و برکت) از ریشهٔ *drvatāt (ارمنی drut) و از اوستا drvatāt- «بارتولمه ۷۸۹»'; leaf 296 (≈ 836–840) carries درست with the Pahlavi/Old-Persian forms; leaf 300 (≈ 843) has درگر/درودگر.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"HRN\", \"where\": \"HRN.txt leaf 145 = printed p.124, no. 555\", \"stance\": \"supports\",\n     \"note\": \"'aw. drvatāt- ‚Gesundheit‘; phlv. drūt (Mēn.; AV.), drūtik ‚courteous‘ (West II, 280).'\"},\n    {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt p.26\", \"stance\": \"supports\",\n     \"note\": \"'drōd [SLM < A šlm; dlwtʼ | M drwd, N darōd] health, well-being, prosperity, peace'; 'drust [drw(y)stʼ | (M dryst), N durust] right; well, healthy'.\"},\n    {\"src\": \"FSF\", \"where\": \"FSF_pages.txt lines 6778–6790\", \"stance\": \"supports\",\n     \"note\": \"Noushin on پدرود/بدرود: 'درود شادی رامش' and 'معنای اصلی بدرود آرزومندی تندرستی'.\"},\n    {\"src\": \"BRT\", \"where\": \"BRT.txt line 14225\", \"stance\": \"supports\",\n     \"note\": \"'j. drva-tāt- f. ‚Gesundheit, Heiltum‘: daθrāi tanūi °tātəm Yt.13.14'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Old Persian\", \"words\": \"dâru; asâ-dâru\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"Kent, Old Persian: Grammar, Texts, Lexicon, Lexicon s.v. (KNT.txt line 5530), the page Nourai cites: 'dāru- sb. \"\n    \"‚wood‘: Av. dāuru-, Skt. dáru-, cf. Gk. δόρυ ‚spear‘. dāruv (§181) nsn. DSf 41, in phrase asā dāruv ‚ebony‘, lit. \"\n    \"‚stone wood‘ (§308.n1), so called because of its hardness'. Old Persian dāru- is the direct o-grade *dóru of the \"\n    \"root, with the regular Iranian a for PIE o and the neuter nom.-acc. ending -uv. The compound asā-dāru occurs \"\n    \"once, in Darius' Susa foundation charter (DSf 41), where it translates the Akkadian version's 'abnu' (stone) \"\n    \"— Kent notes Duchesne-Guillemin's argument (BSOS 10.925-7) that the calque is prompted by the Egyptian ebony \"\n    \"word hbnj and by Herodotus 3.97, who says the Egyptians paid tribute in ebony logs to the Persian king. \"\n    \"Nourai's cross-reference to root 'Ak' for the asā- element (Old Iranian *aśman-/asan- 'stone') is right.\"),\n  \"derivation_fa\": (\n    \"کنت در واژه‌نامهٔ پارسی باستان (ص ۱۹۰، همان صفحهٔ مورد ارجاع) می‌نویسد: «dāru- «چوب»؛ اوستایی dāuru-، سنسکریت dáru-، \"\n    \"قیاس کنید با یونانی δόρυ»؛ صورت dāruv در کتیبهٔ داریوش در شوش (DSf ۴۱) در ترکیب asā dāruv «آبنوس» تحت‌اللفظ \"\n    \"«چوبِ سنگی» آمده است، زیرا سختیِ آبنوس را به سنگ مانند کرده‌اند. dāru- همان گونهٔ o ریشه (*dóru) است که o هندواروپایی \"\n    \"در ایرانی به a بدل شده است. ادعای نورایی درست است.\"),\n  \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%B3ru\"],\n  \"ref_check\": [\n    {\"ref\": \"KNT:190\", \"status\": \"supports\",\n     \"note\": \"KNT.txt line 5530 (Lexicon, the d- range that includes p.190): 'dāru- sb. ‚wood‘: Av. dāuru-, Skt. dáru-, cf. Gk. δόρυ ‚spear‘. dāruv nsn. DSf 41, in phrase asā dāruv ‚ebony‘, lit. ‚stone wood‘'. Word, gloss and the ebony compound are all exactly as charted.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"BRT.txt (dāuru- citations, e.g. V.13.30 'tašəm dauru')\", \"stance\": \"supports\",\n     \"note\": \"Bartholomae's citations of Av. dāuru 'ein Stück Holz' are the Avestan counterpart Kent names.\"},\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 225, p.214\", \"stance\": \"supports\",\n     \"note\": \"'ai. dāru n. ‚Holz‘ ... av. dāuru ‚Baumstamm, Holzstück‘' — the Indo-Iranian o-grade noun.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. deru- §11\", \"stance\": \"supports\",\n     \"note\": \"'O-grade form *doru- in Sanskrit daru, wood, timber: DEODAR.'\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": None, \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": (\n    \"An empty box: on the printed page (pdf 121 = book p.91) the arrow out of the Old Persian box points to a \"\n    \"rectangle with no language label, no reference and no words — a layout artefact of Nourai's chart software, \"\n    \"probably a slot he meant to fill with the New Persian or English continuation of asā-dāru 'ebony' (compare \"\n    \"the parallel empty Germanic box, #13, which at least keeps its label). There is nothing to verify; the \"\n    \"extraction is faithful to the page.\"),\n  \"derivation_fa\": (\n    \"این جعبه در صفحهٔ چاپی خالی است: نه نام زبان دارد، نه ماخذ، نه واژه. پیداست که نورایی جایی برای ادامهٔ \"\n    \"asā-dāru گذاشته و آن را پر نکرده است. چیزی برای راستی‌آزمایی وجود ندارد؛ خوانش اسکن نیز با صفحه مطابق است.\"),\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no references in the book.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"printed page pdf 121 (book p.91), copied to data/verification/sources/refs/ocr/BOOK/121.png\", \"stance\": \"silent\", \"note\": \"the box is empty on the page itself.\"}]\n})\n\nN.append({\n  \"id\": 10, \"lang\": \"Sanskrit\", \"words\": \"druna\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Sanskrit druṇa- is real but Nourai's gloss is not what the sources give. Pokorny p.214, the page cited, has \"\n    \"'ai. druváya-ḥ ‚hölzernes Gefäß, Holzkasten der Trommel‘, dráṇa-m ‚Bogen, Schwert‘ (unbelegt; mit npers. \"\n    \"durūna, baluci drīn ‚Regenbogen‘), druṇī ‚Wassereimer‘' — i.e. druṇa- means 'bow; sword', is a lexicographers' \"\n    \"word (unbelegt, known only from the Sanskrit kośas), and is quoted precisely because it explains NP darūna. \"\n    \"'Made of wood' is the etymological sense of the formation (*dru- 'wood' + -na-, exactly parallel to Old Irish \"\n    \"dron 'firm' < *dru-no-s and Skt. dāruṇá- 'hard'), not the attested meaning, so the box conflates the two. \"\n    \"The arrow root → Skt. druṇa- is otherwise correct.\"),\n  \"derivation_fa\": (\n    \"سنسکریت druṇa- واژه‌ای واقعی است، اما معنای آن در منابع «کمان، شمشیر» است نه «از چوب ساخته‌شده»؛ \"\n    \"پوکورنی در ص ۲۱۴ می‌نویسد «dráṇa-m ‚Bogen, Schwert‘ (گواهی‌نشده؛ با فارسی نو durūna و بلوچی drīn ‚رنگین‌کمان‘)». \"\n    \"پس معنایی که نورایی آورده معنای ریشه‌شناختی ساخت است (*dru- + پسوند -na-، همانند ایرلندی کهن dron «استوار») \"\n    \"نه معنای گواهی‌شدهٔ آن. پیکان ریشه ← سنسکریت درست است و با احتیاط پذیرفتنی است.\"),\n  \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%B3ru\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:214\", \"status\": \"partial\",\n     \"note\": \"POK_01.txt leaf 225 (p.214) has 'dráṇa-m ‚Bogen, Schwert‘ (unbelegt; mit npers. durūna, baluci drīn ‚Regenbogen‘)' — the word and the Persian link are there, but glossed 'bow, sword', not 'made of wood'.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"IEC\", \"where\": \"IEC.txt line 2483 s.v. dru-\", \"stance\": \"partial\",\n     \"note\": \"Mann lists Skt. dru and the -na-/-no- formations of the root but not druṇa- with the sense 'made of wood'.\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. deru-\", \"stance\": \"silent\",\n     \"note\": \"Watkins lists only Sanskrit daru 'wood, timber' (DEODAR) for Indic; druṇa- is not in the appendix.\"},\n    {\"src\": \"SYN\", \"where\": \"SYN.txt line 1549 (Buck 'tree')\", \"stance\": \"partial\",\n     \"note\": \"Buck lists 'Skt. daru-, dru- ‚wood‘, druma- ‚tree‘' — the same family, without druṇa-.\"}\n  ]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Persian\", \"words\": \"darūneh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"درونه darūna/durūna 'bow (esp. a cotton-carder's bow), rainbow' is the New Persian match of Skt. druṇa-, and \"\n    \"the identification is Pokorny's own: p.214 'dráṇa-m ‚Bogen, Schwert‘ (unbelegt; mit npers. durūna, baluci drīn \"\n    \"‚Regenbogen‘)'. Horn, Grundriss no. 558 (p.124, the page Nourai cites) has 'durūne ‚Regenbogen‘. skr. druṇa- \"\n    \"‚Bogen‘ (spät und selten). bel. drīn, drīnuk ‚Regenbogen‘; yidg. LW. drūn' and adds Hübschmann's point \"\n    \"(ZDMG 44,555) that Baluchi drīn shows the transmitted vocalisation durūne to be secondary, the older form \"\n    \"being darūna/drūna. MacKenzie p.26 supplies the Middle Persian link: '¹drōn [dlwnʼ | N darūna] bow'. \"\n    \"Mo'in's footnote in Borhan-e Qate' (BQT_v2_pages.txt leaf 305, in the درو- range around printed pp.845–847) \"\n    \"gives 'drūna (کمان، قوس)، بلوچی drīn' and quotes 'بکپاره چون درونِ حلاجان' from the Nowruznāma. Asadi's \"\n    \"Loghat-e Fors, at exactly the leaf Nourai cites (FRS_pages.txt leaf 217 = FRS:217), has the headword درونه \"\n    \"glossed 'کمان حلاجان' together with Nourai's own Kasāʾī couplet 'سرو بودیم چند گاه بلند / کوژ گشتیم و \"\n    \"چون درونه شدیم'. The semantic step 'bow' → 'rainbow' is the ordinary Iranian one (cf. Baluchi drīn).\"),\n  \"derivation_fa\": (\n    \"«درونه» در فارسی نو به معنای کمان (به‌ویژه کمان حلاجان) و رنگین‌کمان است و پوکورنی خود در ص ۲۱۴ آن را با \"\n    \"سنسکریت dráṇa- و بلوچی drīn سنجیده است. هرن (شمارهٔ ۵۵۸، ص ۱۲۴) همین را می‌گوید و به پیروی هوبشمان \"\n    \"می‌افزاید که تلفّظ durūne ثانوی است و صورت کهن‌تر darūna/drūna بوده است. حلقهٔ فارسی میانه را مکنزی می‌دهد: \"\n    \"drōn «کمان». حاشیهٔ معین بر برهان قاطع و لغت فرس اسدی (برگ ۲۱۷، همان ارجاع نورایی) با همان بیت کسایی آن را \"\n    \"تأیید می‌کنند. ادعای نورایی درست است.\"),\n  \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%B3ru\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:854\", \"status\": \"partial\",\n     \"note\": \"the درونه entry with Mo'in's footnote 'drūna (کمان، قوس) بلوچی drīn' is at BQT_v2_pages.txt leaf 305, i.e. printed p.845±3 (its foot reads 'بقیه در صفحهٔ ۸۴۸'), not p.854; p.854 falls in the دژ section. The content Nourai wants is in Borhan, but the page number is off by about nine.\"},\n    {\"ref\": \"HRN:124\", \"status\": \"supports\",\n     \"note\": \"HRN.txt leaf 145 = printed p.124, no. 558: 'durūne ‚Regenbogen‘. skr. druṇa- ‚Bogen‘ (spät und selten). bel. drīn, drīnuk ‚Regenbogen‘ ... bel. drīn beweist, dass die ebenfalls überlieferte np. Aussprache durūne falsch ist, vergl. Hübschmann, ZDMG. 44, 555.'\"},\n    {\"ref\": \"FRS:217\", \"status\": \"supports\",\n     \"note\": \"FRS_pages.txt leaf 217 carries درونه; FRS.txt lines 16812–16826 give the same entry with the couplet 'سرو بودیم چند گاه بلند / کوژ گشتیم و چون درونه شدیم' and the gloss 'درونه کمان حلاجان' — the very verse and gloss Nourai prints.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 225, printed p.214\", \"stance\": \"supports\",\n     \"note\": \"'dráṇa-m ‚Bogen, Schwert‘ (unbelegt; mit npers. durūna, baluci drīn ‚Regenbogen‘)'.\"},\n    {\"src\": \"PHD\", \"where\": \"PHD_mackenzie.txt p.26\", \"stance\": \"supports\",\n     \"note\": \"'¹drōn [dlwnʼ | N darūna] bow' — the Middle Persian intermediate.\"},\n    {\"src\": \"BQT\", \"where\": \"BQT_v2_pages.txt leaf 305\", \"stance\": \"supports\",\n     \"note\": \"'درونه = بفتح اول و با واو مجهول بر وزن نموله ...' with the footnote 'drūna (کمان، قوس)، بلوچی drīn' and the Nowruznāma quotation 'بکپاره چون درون حلاجان'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": \"Greek\", \"words\": \"drūs; ěn-druon\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Greek δρῦς, gen. δρυός 'oak; tree' is a textbook reflex of the root: Pokorny p.214 explains it as the old neuter \"\n    \"*drū/*deru, *doru gen. *druuōs turned feminine after other tree-names, with lengthening of the monosyllabic \"\n    \"nominative; Klein s.v. dryad gives 'δρῦς, gen. δρυός ‚oak; tree‘ ... fr. I.-E. base *derew(o)-, *drew(o)-'. Confirmed. \"\n    \"ἔνδρυον is a Hesychius gloss and Nourai's translation follows Mann, whose entry 'dru- (radical) ‚timber, tree‘' \"\n    \"(IEC.txt line 2483, the dru- article Nourai cites as IEC:161) reads '... Gk. drūs ‚oak‘; ... cf. Gk. én-druon \"\n    \"‚yokepeg‘'. Pokorny, however, quotes the same lemma with its actual Hesychian gloss — 'ἔνδρυον· καρδία δένδρου' \"\n    \"(p.215), 'heart of a tree', beside the Arcadian ἔνδροια· καρδία δένδρου. Both are the same word (en- 'in' + \"\n    \"*dru- 'wood'), but the gloss 'yoke peg' is Mann's alone and is not the transmitted one, so the node is right \"\n    \"about the etymology and wrong about the meaning.\"),\n  \"derivation_fa\": (\n    \"یونانی δρῦς «بلوط، درخت» بازماندهٔ مستقیم همین ریشه است؛ پوکورنی و کلاین آن را از خنثای کهن *drū/*doru \"\n    \"می‌دانند که به پیروی دیگر نام‌درخت‌ها مؤنث شده است. اما «ἔνδρυον» واژه‌ای است که تنها در فرهنگ \"\n    \"هزیکیوس آمده و در آنجا «καρδία δένδρου» یعنی «دلِ درخت» معنی شده است؛ معنای «میخ یوغ» که نورایی داده از \"\n    \"فرهنگ منّ (همان ماخذ IEC) گرفته شده و مستند نیست. پس ریشه‌شناسی درست و معنا محل اختلاف است.\"),\n  \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%B3ru\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:161\", \"status\": \"supports\",\n     \"note\": \"IEC.txt line 2483, Mann's article 'dru- (radical) ‚timber, tree‘. Cf. druu-, dru-to-, etc. WP I, 804. Skt. dru; Av. dru ‚timber; spear‘; Gk. drūs ‚oak‘; Alb. dru ...; cf. Gk. én-druon ‚yokepeg‘' — both of Nourai's Greek words with his glosses. (The local scan is two printed pages per leaf and this falls near leaf 102, so the printed page could not be pinned exactly to 161.)\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaves 225–226, printed pp.214–215\", \"stance\": \"partial\",\n     \"note\": \"'δρῦς, δρυός ‚Eiche, Baum‘ (aus dem n. *drū oder *derw, *doru g. *druuōs nach andern Baumnamen zum Fem. geworden)' and 'ἔνδρυον· καρδία δένδρου Hes.' — supports drūs, gives a different gloss for én-druon.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. dryad\", \"stance\": \"supports\",\n     \"note\": \"'δρῦς, gen. δρυός, ‚oak; tree‘, which is rel. to δρυμός ..., δόρυ ..., δένδρεον ..., fr. I.-E. base *derew(o)-, *drew(o)-, ‚tree, wood‘.'\"},\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. deru- §8\", \"stance\": \"supports\",\n     \"note\": \"'Lengthened zero-grade form *drū- in Greek drus, oak: DRUPE, DRYAD; GERMANDER, HAMADRYAD.'\"}\n  ]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"Germanic\", \"words\": \"\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"A pass-through box with no words: the Germanic stage between the root and node #14. Pokorny p.215–216 sets it \"\n    \"out under three ablaut grades — '*dreu- in got. triu n. ‚Holz, Baum‘, anord. tré, ags. trēow (engl. tree)', \"\n    \"'*drou- in ags. trīg, engl. tray', '*dru- in ags. trum ‚fest, kräftig, gesund‘ (*dru-mo-s)', plus got. triggws \"\n    \"'treu', ahd. triuwa 'Treue' and the *droust- group behind Trost/trust. Watkins/AHD, which is Nourai's stated \"\n    \"reference here, lists the same Germanic derivatives under deru-. The box is correct as drawn.\"),\n  \"derivation_fa\": (\n    \"این جعبه واژه‌ای ندارد و تنها مرحلهٔ ژرمنی میان ریشه و انگلیسی را نشان می‌دهد. پوکورنی در صفحات ۲۱۵–۲۱۶ \"\n    \"سه پایهٔ ابدالی را می‌آورد: *dreu- (گوتی triu، انگلیسی کهن trēow)، *drou- (trīg > tray) و *dru- (trum \"\n    \"«استوار»). واتکینز (AHD) هم که ماخذ خود نورایی است همین مجموعه را زیر deru- می‌آورد. ادعا درست است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/tree\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt s.v. deru-: '*dru-ko- in Germanic *trugaz in Old English trog ...: TROUGH. 5. Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM. 6. Variant form *derw- in Germanic *terw- ...: TAR. [Pok. deru- 214.]'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaves 226–227, printed pp.215–216\", \"stance\": \"supports\",\n     \"note\": \"'dreu- in got. triu n. ‚Holz, Baum‘, anord. trē, ags. trēow (engl. tree), as. trio ‚Baum, Balken‘' etc.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. tree\", \"stance\": \"supports\",\n     \"note\": \"'ME. tre, tree, fr. OE. trēow, ‚tree, wood‘, rel. to OS. trio, treo, ON., OFris. trē, Goth. triu, of s.m., fr. I.-E. base *derow(o)-, *drew(o)-'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"English\", \"words\": \"tree, true, tray, truth, trust, trim\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\n    \"All six are Germanic reflexes of *deru- in its 'wood' and its 'firm, steadfast' senses, and every one is \"\n    \"documented in Pokorny's Germanic paragraph (pp.215–216) or in Watkins' AHD appendix. tree < ME tre(e) < OE \"\n    \"trēow < PGmc *trewa- < *dreu-o- 'tree, wood'. tray < OE trīg 'flat wooden vessel' < *drou-, PGmc *trauja-. \"\n    \"true < OE trēowe 'faithful' and truth < OE trēow(th) 'faith, fidelity' show the metaphor 'as firm as an oak' \"\n    \"that Pokorny states explicitly ('in übtr. Bed. ‚fest — fest vertrauend‘ ... got. triggws ‚treu‘'); Klein s.v. \"\n    \"true derives it 'fr. I.-E. base *dru-, ‚strong, faithful‘'. trust < ME trust, cognate with ON traust \"\n    \"'confidence' and OHG trōst < *droust-, in the same Germanic sub-family (Pokorny p.216 expressly links it \"\n    \"with 'npers. durušt ‚hart, stark‘, durust ‚gesund, ganz‘' — the sister of dorost in node 7). trim < OE trymman \"\n    \"'to strengthen, make firm', denominative of trum 'firm, strong' < *dru-mo-; Watkins: 'Suffixed zero-grade form \"\n    \"*dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM.' \"\n    \"Etymonline states the root for tree as '*deru- ‚be firm, solid, steadfast‘, with specialized senses ‚wood, tree‘'.\"),\n  \"derivation_fa\": (\n    \"هر شش واژهٔ انگلیسی از همین ریشه اند، یکی از راه معنای «چوب» و دیگری از راه معنای «استواری»: tree از \"\n    \"انگلیسی کهن trēow، tray از trīg «ظرف چوبی پهن»، و true/truth از trēowe «وفادار» که پوکورنی تحول معنایی \"\n    \"آن را «استوار ← استوارانه باوردارنده» می‌داند؛ trust هم‌ریشهٔ نروژی کهن traust است و پوکورنی در ص ۲۱۶ آن را \"\n    \"در کنار فارسی «درشت» و «درست» می‌آورد؛ trim نیز از trymman «استوار کردن» و صفت trum «سخت، نیرومند» \"\n    \"(*dru-mo-) است. ادعای نورایی درست است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/tree\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; it inherits AHD from the Germanic box #13, which does support it.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. deru-\", \"stance\": \"supports\",\n     \"note\": \"'Suffixed zero-grade form *dru-mo- in Germanic *trum- in Old English trum, firm, strong (> trymman, to strengthen, arrange): TRIM.'\"},\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 227, printed p.216\", \"stance\": \"supports\",\n     \"note\": \"'*drou- in ags. trīg, engl. tray ‚flacher Trog, Schüssel‘'; 'got. triggws ‚treu‘ ... ablautend engl. trust ‚Vertrauen‘ (mengl. trūst)'; '*dru- in ags. trum ‚fest, kräftig, gesund‘ (*dru-mo-s)'.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. true, tree\", \"stance\": \"supports\",\n     \"note\": \"'true, adj. — ME. trewe, fr. OE. trēowe, triewe, ‚faithful, trusty‘ ... fr. I.-E. base *dru-, ‚strong, faithful‘'.\"},\n    {\"src\": \"SKT\", \"where\": \"SKT.txt\", \"stance\": \"silent\",\n     \"note\": \"grep for a TREE headword block in the Skeat OCR returned no usable entry (the file's headwords are lower-case and heavily mangled at this point).\"}\n  ]\n})\n\nN.append({\n  \"id\": 15, \"lang\": \"Latin\", \"words\": \"durus\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"Latin dūrus 'hard, tough, harsh' is put under this root by all of Nourai's stated authority and its \"\n    \"descendants — Watkins/AHD: 'Suffixed variant form *dru-ro- in Latin durus, hard'; Klein s.v. dure: 'L. durus, \"\n    \"‚hard, rough, rude‘, prob. dissimilated fr. *dru-ros, for *dreu-ros, and lit. meaning ‚as hard as wood‘'; \"\n    \"Etymonline: 'from durus ‚hard‘, from PIE *dru-ro-, suffixed variant form of root *deru- ‚be firm, solid, \"\n    \"steadfast‘'. But the assignment has always been hedged and is now often rejected. Pokorny himself writes only \"\n    \"'aus dem Lat. vielleicht durus ... wenn nach Osthoff als ‚baumstark, fest wie (Eichen)holz‘ dissimiliert aus \"\n    \"*drū-ro-s (*dreu-ro-s?)' (p.215) — 'perhaps', on a dissimilation that is not otherwise paralleled — and de Vaan's \"\n    \"Etymological Dictionary of Latin takes dūrus instead to *duh₂-ro- 'long-lasting', with Greek δηρός and Latin \"\n    \"dūdum. Wiktionary's *dóru page reflects this by citing dūrus only as evidence for the adjective *deru- 'hard', \"\n    \"not as a derivative of the noun. So: accepted by some, not by all.\"),\n  \"derivation_fa\": (\n    \"لاتین dūrus «سخت، درشت» را واتکینز و کلاین و اتیمونلاین از گونهٔ پسونددار *dru-ro- همین ریشه می‌دانند که \"\n    \"تحت‌اللفظ «سخت چون چوب بلوط» معنی می‌دهد. اما خود پوکورنی در ص ۲۱۵ با قید «شاید» (vielleicht) سخن \"\n    \"می‌گوید و به دگرگونی ناهمگونی (dissimilation) نیاز دارد؛ دو‌وان در فرهنگ ریشه‌شناختی لاتین آن را از \"\n    \"*duh₂-ro- «دیرپای» (هم‌ریشهٔ یونانی δηρός و لاتین dūdum) می‌گیرد. پس ادعا با احتیاط پذیرفتنی است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/durable\", \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%B3ru\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"AHD_watkins1985.txt s.v. deru- §7: 'Suffixed variant form *dru-ro- in Latin durus, hard (of whose English derivatives many represent a semantic cross with Latin durare, to last long; see deue-): DOUR, DURAMEN, DURESS, DURUM; ENDURE, INDURATE, OBDURATE.'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 226, printed p.215\", \"stance\": \"partial\",\n     \"note\": \"'aus dem Lat. vielleicht durus ‚hart; abgehärtet, kräftig ...‘ (aber über dūrāre ‚ausdauern, dauern‘ s. unten S. 220), wenn nach Osthoff Ulf. als ‚baumstark, fest wie (Eichen)holz‘ dissimiliert aus *drū-ro-s' — Pokorny only 'perhaps', and he sends dūrāre to another root.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. dure, adj.\", \"stance\": \"supports\",\n     \"note\": \"'F. dur, fern. dure, fr. L. durus, ‚hard, rough, rude‘, prob. dissimilated fr. *dru-ros, for *dreu-ros, and lit. meaning ‚as hard as wood‘, fr. I.-E. base *derew(o)-, *drew(o)-, *dru-, ‚tree, wood‘.'\"},\n    {\"src\": \"LEW\", \"where\": \"LEW_1910.txt (Walde, Lat. et. Wb.) s.v. durus\", \"stance\": \"partial\",\n     \"note\": \"Walde is the source of Pokorny's 'WH. I 342 f.' cross-reference; like Pokorny he registers the *dru-ro- explanation as a possibility rather than a fact.\"}\n  ]\n})\n\nN.append({\n  \"id\": 16, \"lang\": \"English\", \"words\": \"duration\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\n    \"English duration comes from Medieval Latin dūrātiōnem, from Latin dūrāre 'to harden; to last, endure', a \"\n    \"denominative of dūrus — so the immediate chain Latin → (Old French duration/duree) → Middle English duracioun \"\n    \"(14th c., Chaucer) is uncontroversial, and Etymonline routes the whole family through 'durus ‚hard‘, from PIE \"\n    \"*dru-ro-, suffixed variant form of root *deru-'. The reservation is the same as at node 15, and here it is \"\n    \"sharper: Pokorny explicitly separates the two verbs — at p.215 he writes '(aber über dūrāre ‚ausdauern, \"\n    \"dauern‘ s. unten S. 220)', sending the 'last long' sense to the root *deuə- 'long' — and Watkins concedes the \"\n    \"point in the same breath in which he keeps dūrus here: 'of whose English derivatives many represent a semantic \"\n    \"cross with Latin dūrāre, to last long; see deue-'. duration is exactly one of those derivatives, so this \"\n    \"particular English word may belong to *deuə- rather than to Deru 1.\"),\n  \"derivation_fa\": (\n    \"واژهٔ duration از لاتینی dūrātiōnem و فعل dūrāre «سخت کردن؛ دوام آوردن» است که از صفت dūrus ساخته شده، و \"\n    \"از راه فرانسهٔ کهن به انگلیسی میانه duracioun (سدهٔ چهاردهم) رسیده است؛ تا اینجا محل اختلاف نیست. اما \"\n    \"پوکورنی در ص ۲۱۵ تصریح می‌کند که dūrāre «دوام داشتن» را باید در ص ۲۲۰ (ریشهٔ *deuə- «دراز، دیر») جست؛ \"\n    \"واتکینز هم می‌گوید بسیاری از مشتقّات انگلیسی نتیجهٔ درهم‌آمیزی معنایی با dūrāre اند. پس این یک واژه به احتمال \"\n    \"به ریشهٔ دیگری می‌رسد و ادعای نورایی تنها با احتیاط پذیرفتنی است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/durable\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the node carries no reference of its own; it inherits AHD from the Latin box #15.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. deru- §7\", \"stance\": \"partial\",\n     \"note\": \"'... Latin durus, hard (of whose English derivatives many represent a semantic cross with Latin durare, to last long; see deue-)' — Watkins keeps durus here but flags the duration-type words as belonging semantically with deue-.\"},\n    {\"src\": \"POK\", \"where\": \"POK_01.txt leaf 226, printed p.215\", \"stance\": \"contradicts\",\n     \"note\": \"'(aber über dūrāre ‚ausdauern, dauern‘ s. unten S. 220)' — Pokorny removes dūrāre, the direct base of duration, from the deru- article.\"},\n    {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. dure, intr. v.\", \"stance\": \"supports\",\n     \"note\": \"'F. durer, fr. L. durare, ‚to harden; to continue, last‘, fr. durus, ‚hard‘' — Klein does keep durare with durus, and lists duration among the words referred to there.\"}\n  ]\n})\n\nout = {\n  \"pdf_page\": 121,\n  \"book_page\": 91,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry]\n}\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-121.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk121.py",
 "description": "Write page-121.json"
}
```


### [2026-09-05T18:32:44.302Z] TOOL RESULT

```
ok 16
```


## [2026-09-05T18:32:48.988Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-121.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 121",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T18:32:50.680Z] TOOL RESULT

```
JSON OK
nodes verified: 16/16
node verdicts: {'transcription_suspect': 1, 'disputed': 3, 'plausible': 6, 'confirmed': 5, 'unverified': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 7, 'supports': 11, 'not_checked': 9}
books consulted: {'contradicts': 9, 'supports': 25, 'partial': 11, 'silent': 6} | by book: {'KLN': 7, 'POK': 7, 'AHD': 6, 'BQT': 5, 'BRT': 4, 'PHD': 4, 'KNT': 2, 'SYN': 2, 'HRN': 2, 'MON': 2, 'PLA': 2, 'SNS': 1, 'ARY': 1, 'AFA': 1, 'FSF': 1, 'BOOK': 1, 'IEC': 1, 'SKT': 1, 'LEW': 1}
```


## [2026-09-05T18:33:07.756Z] AGENT

Done. `data/verification/page-121.json` written; `verify_check.py 121` reports 16/16 nodes, 0 PROBLEM lines.

**Page 121 (book p.91) — one entry, root "Deru 1" (PIE \*deru-/\*dóru), root verdict: confirmed (POK 214 verified verbatim).**

Node verdicts: 5 confirmed · 6 plausible · 3 disputed · 1 unverified · 1 transcription_suspect.

Disputed / flagged:
- **#1 Avestan "dru, dâuru, derežda, draxta; dârug" — transcription_suspect (error_in: book).** dru-/dāuru- are right; *derežda* is not Avestan (it is Bartholomae's `dərəzra-/drazra-` "firm", from `darəz-`, a different root); Av. `draxta-` is only the ppp. of `dranj-` (SNS p.318 writes `*draxta-` with asterisk + "?"); `dārug` is Middle Persian (MacKenzie p.25), not Avestan. Page image checked — the book prints these forms, the extraction is faithful.
- **#2 Persian, word `deraxt` — disputed.** MP draxt < PIr \*draxta- "firmly standing" (\*drag-/\*dʰerǵʰ-), not \*deru-. (Other words of the node: `dār`, `dārkūb` confirmed via BQT p.809 footnote + Horn 522; `dorūdgar` and `dārū` plausible — Horn 523 puts dārū under √dʰar-, as Nourai's own NOTE concedes.)
- **#3 Persian `dârîyeh` — disputed.** The Persian tambourine-name is دایره, borrowed from Arabic دائرة "circle"; داریه is a folk-etymological respelling toward دار, and is not a Borhan headword.
- **#4 Arabic `daf` — disputed.** Klein (s.v. toph), Mo'in's own footnote on BQT p.869 (Nourai's cited page: "از عبری تف مشتق از تفف"; Sumerian dub → Akkadian → Aramaic) and Wiktionary all make duff Semitic. Even Asbaghi p.223, who calls it Persian, sources it from Aramaic — nothing touches dār "wood".

Reference-page discrepancies (book, not extraction): BQT:854 for `درونه` — the entry with Mo'in's `drūna` footnote is at printed p.845±3, not 854. IEC:161 and KLN:1644 could not be pinned to the page (entries found by headword and they do support the arrows).

No extraction errors found — the JSON matches the printed page everywhere, including the empty box #9.
