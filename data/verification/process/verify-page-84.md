# Verification process log — verify-page-84


## [2026-09-05T06:20:09.244Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 84 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-84.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-84.json. Write /home/sfmqrb/git/rishe/data/verification/page-84.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 84` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T06:20:10.310Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T06:20:11.170Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T06:20:11.188Z] TOOL RESULT

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


## [2026-09-05T06:20:11.716Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-84.txt"
}
```


### [2026-09-05T06:20:11.737Z] TOOL RESULT

```
1	=== PDF page 84 (book page 54) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhel, Bhelgh, Bhlei, Bhleu : to swell, blow, thrive, grow, bloom, overflow  (refs POK:120,122,125,156,158; AHD; ROE:65,66)  PART 1
4	#1 (parent #0) [Avestan] refs=POK:120; BQT:256 | barez : to grow ; bara-s-man : bundle of twigs
5	  #2 (parent #1) [Pahlavi] refs=BQT:256 | barsum : branches, twigs
6	    #3 (parent #2) [Persian] refs=BQT:256; SNS:103 | barsam «برسم» : a bundle of twigs used in Zoroastrian ceremonies
7	#4 (parent #0) [Avestan] refs=POK:125 | baraziš, barašnav : cushion, pillow
8	  #5 (parent #4) [Pahlavi] refs=SNS:98 | bâlîšn, bâlěn : pillow
9	    #6 (parent #5) [Persian] refs=POK:125; SNS:98 | bâleš «بالش ١» : pillow | extra: بالین
10	#7 (parent #0) [Middle German] refs=AHD | bole : beam, plank ; balle : ball
11	  #8 (parent #7) [French] refs=AHD | boulevard
12	    #9 (parent #8) [Persian] refs=MON:605 | bŭlvâr «بلوار» : boulevard
13	    #10 (parent #8) [English] refs=AHD | boulevard
14	  #11 (parent #7) [Italian] refs=AHD:102 | palla, pallone : ball ; ballotta : a small ball used for voting
15	    #12 (parent #11) [French] refs=AHD:102 | ballon : ball
16	      #13 (parent #12) [Persian] refs=MON:467 | bâlon «بالون» : balloon | extra: بالن ١
17	      #14 (parent #12) [English] refs=AHD:102 | balloon
18	    #15 (parent #11) [English] refs=AHD:102 | ballot
19	#16 (parent #0) [Latin] refs=AHD | ballaena : (spouting) whale ; bulga : leather bag
20	  #17 (parent #16) [Old French] refs=AHD | baleine : whale
21	    #18 (parent #17) [Persian] refs=MON:464,467 | bâlon «بالن ٢» : whale | extra: بال ١
22	    #19 (parent #17) [English] refs=AHD | baleen
23	  #20 (parent #16) [Old French] refs=AHD | bougette : leather bag, budget
24	    #21 (parent #20) [English] refs=AHD; ETM:62 | budget
25	      #22 (parent #21) [French] refs=ETM:62 | budget
26	        #23 (parent #22) [Persian] refs=MON:600 | bŭdjeh «بودجه» : budget
27	#24 (parent #0) [Old Norse] refs=AHD | blôm, blômi : flower ; bulki : rolled up bundle
28	  #25 (parent #24) [English] refs=AHD | bloom, bulk
29	
```


## [2026-09-05T06:20:13.214Z] AGENT

I'll read the source JSON and reference infrastructure.


## [2026-09-05T06:20:14.631Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-84.json | head -200",
 "description": "Read page 84 source JSON"
}
```


## [2026-09-05T06:20:15.174Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T06:20:16.251Z] TOOL RESULT

```
{
    "pdf_page": 84,
    "book_page": 54,
    "entries": [
        {
            "root": {
                "name": "Bhel, Bhelgh, Bhlei, Bhleu",
                "lang": "Indo-European",
                "refs": "POK:120,122,125,156,158; AHD; ROE:65,66",
                "gloss": "to swell, blow, thrive, grow, bloom, overflow"
            },
            "part": 1,
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:120; BQT:256",
                    "words": [
                        {
                            "translit": "barez",
                            "gloss": "to grow",
                            "script": null
                        },
                        {
                            "translit": "bara-s-man",
                            "gloss": "bundle of twigs",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Pahlavi",
                    "refs": "BQT:256",
                    "words": [
                        {
                            "translit": "barsum",
                            "gloss": "branches, twigs",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT:256; SNS:103",
                    "words": [
                        {
                            "translit": "barsam",
                            "gloss": "a bundle of twigs used in Zoroastrian ceremonies",
                            "script": "\u0628\u0631\u0633\u0645"
                        }
                    ],
                    "note": null,
                    "quote": {
                        "text": "\u062c\u0647\u0627\u0646\u062c\u0648\u06cc \u0628\u0627 \u0622\u0646 \u062f\u0648 \u062e\u0633\u0631\u0648 \u067e\u0631\u0633\u062a - \u06af\u0631\u0641\u062a \u0627\u0632 \u067e\u06cc \u0648\u0627\u0698 \u0628\u0631\u0633\u0645 \u0628\u062f\u0633\u062a",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 4,
                    "parent": 0,
                    "lang": "Avestan",
                    "refs": "POK:125",
                    "words": [
                        {
                            "translit": "barazi\u0161, bara\u0161nav",
                            "gloss": "cushion, pillow",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 4,
                    "lang": "Pahlavi",
                    "refs": "SNS:98",
                    "words": [
                        {
                            "translit": "b\u00e2l\u00ee\u0161n, b\u00e2l\u011bn",
                            "gloss": "pillow",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "Persian",
                    "refs": "POK:125; SNS:98",
                    "words": [
                        {
                            "translit": "b\u00e2le\u0161",
                            "gloss": "pillow",
                            "script": "\u0628\u0627\u0644\u0634 \u0661"
                        }
                    ],
                    "script_extra": "\u0628\u0627\u0644\u06cc\u0646",
                    "note": null,
                    "quote": {
                        "text": "\u0633\u067e\u0647\u0631 \u0628\u0644\u0646\u062f \u0627\u0631 \u06a9\u0634\u062f \u0632\u06cc\u0646 \u062a\u0648 - \u0633\u0631\u0627\u0646\u062c\u0627\u0645 \u062e\u0634\u062a\u0633\u062a \u0628\u0627\u0644\u06cc\u0646 \u062a\u0648",
                        "poet": "Ferdows\u00ee"
                    }
                },
                {
                    "id": 7,
                    "parent": 0,
                    "lang": "Middle German",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "bole",
                            "gloss": "beam, plank",
                            "script": null
                        },
                        {
                            "translit": "balle",
                            "gloss": "ball",
                            "script": null
                        }
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
                        {
                            "translit": "boulevard",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "Persian",
                    "refs": "MON:605",
                    "words": [
                        {
                            "translit": "b\u016dlv\u00e2r",
                            "gloss": "boulevard",
                            "script": "\u0628\u0644\u0648\u0627\u0631"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 8,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "boulevard",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 7,
                    "lang": "Italian",
                    "refs": "AHD:102",
                    "words": [
                        {
                            "translit": "palla, pallone",
                            "gloss": "ball",
                            "script": null
                        },
                        {
                            "translit": "ballotta",
                            "gloss": "a small ball used for voting",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
```


### [2026-09-05T06:20:16.293Z] TOOL RESULT

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


## [2026-09-05T06:20:18.924Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-84.json | sed -n '200,500p'",
 "description": "Rest of page 84 JSON"
}
```


## [2026-09-05T06:20:20.381Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','ROE','BQT','SNS','MON','ETM']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:800])\n    print()\n\"",
 "description": "Look up ref metadata"
}
```


### [2026-09-05T06:20:20.491Z] TOOL RESULT

```
                },
                {
                    "id": 12,
                    "parent": 11,
                    "lang": "French",
                    "refs": "AHD:102",
                    "words": [
                        {
                            "translit": "ballon",
                            "gloss": "ball",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 12,
                    "lang": "Persian",
                    "refs": "MON:467",
                    "words": [
                        {
                            "translit": "b\u00e2lon",
                            "gloss": "balloon",
                            "script": "\u0628\u0627\u0644\u0648\u0646"
                        }
                    ],
                    "script_extra": "\u0628\u0627\u0644\u0646 \u0661",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 12,
                    "lang": "English",
                    "refs": "AHD:102",
                    "words": [
                        {
                            "translit": "balloon",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 11,
                    "lang": "English",
                    "refs": "AHD:102",
                    "words": [
                        {
                            "translit": "ballot",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "ballaena",
                            "gloss": "(spouting) whale",
                            "script": null
                        },
                        {
                            "translit": "bulga",
                            "gloss": "leather bag",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 16,
                    "lang": "Old French",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "baleine",
                            "gloss": "whale",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 18,
                    "parent": 17,
                    "lang": "Persian",
                    "refs": "MON:464,467",
                    "words": [
                        {
                            "translit": "b\u00e2lon",
                            "gloss": "whale",
                            "script": "\u0628\u0627\u0644\u0646 \u0662"
                        }
                    ],
                    "script_extra": "\u0628\u0627\u0644 \u0661",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 19,
                    "parent": 17,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "baleen",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 20,
                    "parent": 16,
                    "lang": "Old French",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "bougette",
                            "gloss": "leather bag, budget",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 21,
                    "parent": 20,
                    "lang": "English",
                    "refs": "AHD; ETM:62",
                    "words": [
                        {
                            "translit": "budget",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 22,
                    "parent": 21,
                    "lang": "French",
                    "refs": "ETM:62",
                    "words": [
                        {
                            "translit": "budget",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 23,
                    "parent": 22,
                    "lang": "Persian",
                    "refs": "MON:600",
                    "words": [
                        {
                            "translit": "b\u016ddjeh",
                            "gloss": "budget",
                            "script": "\u0628\u0648\u062f\u062c\u0647"
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 24,
                    "parent": 0,
                    "lang": "Old Norse",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "bl\u00f4m, bl\u00f4mi",
                            "gloss": "flower",
                            "script": null
                        },
                        {
                            "translit": "bulki",
                            "gloss": "rolled up bundle",
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                },
                {
                    "id": 25,
                    "parent": 24,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "bloom, bulk",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "note": null,
                    "quote": null
                }
            ]
        }
    ]
}
```


### [2026-09-05T06:20:22.516Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<lea

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/

ROE {"title": "R. Claiborne, The Roots of English: A Reader's Handbook of Word Origins, New York 1989", "edition_found": "1989 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/rootsofenglish00clai ; rootsofenglishre0000robe (lending)", "identifier": "rootsofenglish00clai (also rootsofenglishre0000robe)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending; in-book search ?q=<root>.", "notes": "RE-SEARCH 2026-09: borrowable only."}

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/82307409

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02

ETM {"title": "Mohsen Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374/1995", "kind": "catalog", "url": "https://ketabnak.com/book/107170/ (no download) ; https://ketab.ir/book/2ebb5f53-ba49-4955-98f4-d419919d0ebc ; purchase: https://adinehbook.com/gp/product/9643110451", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only."}
```


## [2026-09-05T06:20:54.595Z] AGENT

Now let me research. Starting with Pokorny and the Iranian nodes.


## [2026-09-05T06:20:56.324Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 120 122 125 156 158; do\n  L=$((n+8))\n  echo \"===== POK page $n (POK_01 leaf $L) =====\"\n  awk -v n=$L 'BEGIN{RS=\"\\f\"} NR==n' POK_01.txt | head -70\ndone",
 "description": "Print Pokorny cited pages"
}
```


### [2026-09-05T06:20:57.872Z] TOOL RESULT

```
===== POK page 120 (POK_01 leaf 128) =====
 Aderlaßeisen^  (*bhei-tlo-)',  ahd.  bt(h)al  ,Beil^  (*bhei^^ lo-),   daher  wohl  germ.  Hilja-  und   nicht  *bipla-  in   ahd.  ags.  bill  n.,  as! 6i7    ^Schwerte    mhd.    bil,    billes  ^Steinhaue*^,   nhd.  Bille   f.   ^Hacke^    mlid.:; billen  ,(be)hauen,  ahd.  bilötJii,  bilidij  nhd.  Bild\   ahd.  billa  f.  ,Sauerteig^-' mit  Formans  -li-  ags.  bile  m.  ,SchnabeF,  Nebenform  zu  engl,  bill'^  4
aksl.  5i;^  (^V?)  ^*'^^*  ,schlagene  skr.  %*em  lylti,  russ.  &ft;*w  ii^ft  ds.,  davon mit  Formans  -dhlo-:  russ.-ksl.  bilo  n.  ,Läutebrette  skr.  Ulo  ,Querholz  ein Rechens^  Öech.  bidlo  ,Stangee  russ.  bilo  ,SchlägeF;  büva  ,Kampf,  Schi (:  messap.  ßiaßrj),   aksl.   bich  , Geißel^   (aus   dem   Slav.   nhd.    Peitsche)]   ii Ablaut   aksl.  u-bojh  m.  ,Morde   skr.  böj,  Gen.  boja  ,Schlachte   russ.  cec boj  ds.  (:  illyr.  Boii).
WP.  II  137  f.,  WH.  I  503  f.,  506,  Trautmann  33,  Liden  KZ.  61,  12: Karstien  KZ.  65,  154  f.
S.  oben  unter  bheid-.
hheig"^'  ,glänzen^?
Apers.  *bigna-  ,Glanz^?  in  den  PN  Bagä-bigna-,  t^gia-ßLyvrjg; gr.  q)OLßog  ,rein,   glänzen d^   q)Oißd(x),   q)oißa^(x)  ,reinigee  dq>olßavTog  , be- schmutzt^ (*bhoig^-o-)j  c^^txrdg,  dcpiytTQÖg  (*bhigu-)  ,unrein^ Über  OoTßog  l^Ttölliov  vgl.  Kretschmer  Gl.  15,  199. WP.  II  138,  Schwyzer  Gr.  Gr.  I  299.
I.  bhel',    balto-slav.    auch    bbelo-   ,glänzend,  weiß^     auch    von    weißlichen Tieren,  Pflanzen  und  Dingen,  wie  Schuppen,   Haut  usw.;  zu   1.  bJiä- im   selben  Verhältnis  stehend,  wie  stel-  zu  stä-  ,stehene  del-  ,spalten^ zu  *dä(iy  ,teilen^ Ai.  bhälam  n.  ,Glanz,  Stirn^  sam-bhälayaü  ^blickt^  (dehnstufig);  baläkä ,eine  Kranichart^  mit  b-  nach  bakd-h,  ,eine  Reiherart^ ; arm.  bal  ,Blässe,  Bleichheit^;
gr.  q)a}.ög  ,weiß^  Hes.,  q)akvvsL'  laf.i7tQvv€L  Hes.,  (pa'ki{/)6g  ,glänzend; weiß,  weißstirnig^  q)alriq6g,  dor.  -aqog  ds.,  cpaXrjQig^  dor.  -aqig  ,Bläßhuhir , (palaytq6g  ,kahlköpfige  Tca^icpaldo)  ,schaue  schüchtern  umher^;  ßaliog  ,wq\Q, weißgefleckt^  ist  wohl  illyr.  Lw.;
119
illyr.  *halta  ^Sumpf^^^  daraus  lat.  hlatea  f.,  ^Kotklümpchen'^^  adalm.  balta ^umpfsee'^;  ligur.  *bolä  ^SumpF  (M.-L.  1191  b)^  FIN  Duria  Bautica  (aus *Baltica),  vielleicht  hierher  mare  Balticum  (ven.-ill.?)  ^Ostsee^  (Einhard, 9  Jh.);  ^ö^-  ßoiif^"^®  BSL.  37,  7  f. ;
alb.  hale  ^Stirn'^  (=  apr.  hallo  ds.),  baldsh  ^hlässiges  Pferd  oder  Ochse^, halte  Ly  halt  m.  ,Schlamm,  Sumpf,  Ton^;
lat.  fulica  (vgl.  ahd.  helihha)  und  fulix  f.  ,Bläßhuhn^  (*hholik-  mit  diaL ii)'  aber  ob  feles,  -is  f.  ,Katze,  Marder,  lltis^  hierher  gehört,  ist  wegen wSles,  -is  f.  ,Marder,  Dachs^   zweifelhaft;
kelt.  helo-  ,leuchtend,  weiß^  in  
===== POK page 122 (POK_01 leaf 130) =====
d.  bil{{)sa  ist  wohl  keltj Lw.  (vgl.  aprov.  belsa)]
slav.  *belena-,  *belenä  in  r.-ksl.  belem  ra.,  russ.  belend  f.,  slav.  *belm  m| in  slov.  bl^n,  acech.  blen,  tief  stuf.  slav.  *bhlm  in  skr.  bün.
WP.  II  180,  WH.  I  99  f.,  Trautmann  30,  Kretschmer  Gl.  14,  97,  Specht] Dekl.  140.
5.  bhel-,  hhle-  , aufblasen,  aufschwellen,  sprudeln,  strotzend
Ai.  bhända-  n.  ,Topf,  Gefäß'  {*bhäln-da?) ;  nach  Thieme  (ZDMG.  92,  47  f.)1 hierher  av.  bat^-s-man-  ,Bündel  von  Zweigen',  ai.  bdrsva  m.  PL  ,Wulst,f Zahnfleisch'  (Lw.  aus  av.  *barsman  , Polster');    vgl.  unten  ahd.  bilorn.      %
Arm.  beiiin  , fruchtbar'  (:  gr.  cpdXrjg),  bein-aicor  ds.  (:  gr.  cpaXkog),  Adontz,1 Mel.  Boisacq  9.
Gr.  (paXXog,  cpdXrig  ,peüis'  {cpaXXog  aus  *bhlnös  oder  *bhjnös'^  vgl.  air.  ball, nhd.  Bulle)-  dazu  cpdXXaiva  (Bildung  wie  Avxa/m),  q)dXXrj  , Walfisch'  (vgl das  wohl  durch  illyr.  Vermittlung  entlehnte  lat.  ballaena]  auch  mhd. bullich  bezeichnet  große  Fischarten;  identisch  ist  cpdXXaLva  ,Nachtfalter^, über  dcpaXrig  ^^^  Zubehör  s.  oben  Z.  1;  über  ocpsXog  s.  u.  pAe^;  nach  Persson Beitr.  299  auch  cpX6f.iog  {cpXdvog)  ,Königskerze,  Pflanze  mit  dicken  wolligen Blättern,  als  *bh(e)lo-mo-s?
Vermutlich  phryg.  ßd^i-ßaXov,  ßd-ßaXov  .aldoTov'  Hes.,  auch  ßaXXLov ,penis';  thrak.  VN  Tqi-ßaXXoL
Lat.  f Ollis  ,lederner  Schlauch;  Windball,  Ballon;  Blasebalg,  Geldbeutel' (Hhlnis  oder  Hholnis,  vgl.  die  germ.  Worte  mit  -II-  aus  -In-);
cymr.  bdl  f.  ,Erhöhung,  Berggipfel'  {Hhlä)-,
schwundstuf.  air.  ball  m.  ,Glied,  Körperteil',  dann  ,Teil,  Ort,  Fleck' (auch  am  Körper),  daher  vielleicht  auch  cymr.  ball  , Epidemie';  cymr. balleg  ,Sack,  Börse';  ablautendes  bol,  boll  in  cymr.  dyrn-fol  ,Handschuh', arfolli  ,sch wanger  werden',  ffroen-foll  ,mit  geblähten  Nüstern'  (:  cpaXXög)] reduktionsstuf.  mit  Formans  -ko-  und  einer  Bed.  wie  ahd.  bald  (s.  u.):  nir.. balc  ,stark',  cymr.  balch,  bret.  balcli  ,stolz,  anmaßend'.
m-'
121
hbl'  (bhe^')  '^^  ascliwed.  bulin,  bolin  ^aufgeschwollen^,  hulde,  holde,  hyld
\  seh  "Teilung",  Geschwür,;  aisl.  hulr,  holr  m.  ^Baumstamm,  Rumpfe,  mnd.
'id    hole  f.  ,Planke'  (nhd.  Bohle)-^   aisl.  holi  ,Stier^,  ags.  hula  ds.,  hulluc
'  n<^er  Stier^,  engl,  hüll,  mnd.  nhd.  Bulle  (als  *bull-ön  =  gr.  ^cpallcov  von
'*iem   St-  ^hulla-  =  (paU.6-g)'j    hess.    feuZZe   ^vulva';    aisl.   holli   m.  ,Trink-
ijj^le^  (,*ku
===== POK page 125 (POK_01 leaf 133) =====
 ,Ab- teilun*^^'  schwundstuf.  ags.  bolca  m.  ^Laufplanke^;  aber  ahd.  bloh{h),  mhd. hloch  nhd.  (ndd.)  Block  ,Klotz,  Bohle^  enthält  idg-,  u,  also  aus  idg.  *bJduko- oder  falls  mit  germ.  Konsonantenverschärfung,  aus  "^bhlugo-,  zu  mir.  blog Bruchstück',  weiter  vielleicht  zu  got.  bliggivan,  ahd.  bliuwan,  nhd.  bleuen 'schla<^en';  aus  idg.  *bhleu-ono- ;   s.  unter  bheleu-.
Hino-eo"en  gehören  wohl  zu  *bhelgh-  ^schwellen'  von  einer  ßedeutungs- vermittlung  ,dick,  schwellend'  aus:
lit.  balziena  ,Längsbalken  an  der  Egge',  balzienas  ^Querbalken',  lett.  bäl- ziens  belziens  m.  ,Stütze',  ostlett.  bhlgzds  m.  , Stützenverband  am  flachen Holzschlitten',  lett.  pabälsts  m.  ,Stütze,  Griff,  Handhabe  am  Pfluge',  bäl- zitj  pabälstit  , stützen';
russ.  mdartl.  (Gouv.  Olonez)  bölozno  , dickes  Brett',  slov.  blazina  , Dach- balken, Querbaum  des  Schlittens,  Rungstock';  kasub.  bhzno  ,das  die Schlittenkufen  verbindende  Querholz'.
WP.  II  181  f.,  WH.  1  559,  Trautmann  25  f.
6.  bhel'  ,schallen,  reden,  brüllen,  bellen';  Schallwurzel.
Ai.  bhasd-h  , bellend'  (*bhel-s-\  bhäsats  ,redet,  spricht,  plaudert';  bhan- (fate  (Dhatup.)  ,spricht,  höhnt,  tadelt'  {*bhel-n-do),  bhdnati  , redet,  spricht' (*bhel-no)  sind  nach  Kuiper  Proto-Munda  32  f.  nichtidg-.
aisl.  belja  ,brüllen',  mndl.  beleti  ,bellen';  aisl.  hylja^  bulda  , drohen,  dröh- nen', bylr  ,Windstoß',  ags.  bylgan  , brüllen',  mhd.  boln  , schreien,  brüllen';
mit  germ.  II  (Konsonantenschärfung  in  der  Schallwurzel),  ahd.  bellan ,bellen',  ags.  bellau  ,brüllen,  bellen,  grunzen';  ahd.  bullön  ,heulen  (vom Wind),  bellen,  brüllen',  isl.-norw.  bulla  , babbeln,  schwatzen';  aisl.  bjalla, ags.  belle,  engl,  bell,  mnd.  belle  , Schelle,  Glocke',  nhd.  (eigentl.  ndd.)  Bell- hammel , Leithammel  (mijt  Schelle)';
mit  germ.  Id  (wohl  aus  einem  c?Ä-Präs.  und  vielleicht  mit  lit.  bildu  zu vergleichen,  da  letzteres  höchstwahrscheinlich  idg.  dh  enthält)  dän.  baldre, norw.  mdartl.  baldra,  schwed.  mdartl.  ballra  ,lärmen',  mnd.  ndl.  balderen ds.,  dän.  buldre,  schwed.  bullsa,  mnd.  ndl.  bulderen,  bolderen,  mhd. huldern,  nhd.  foltern ;
apr.  billit  , sagen,  sprechen',  lit.  bilstu,  bilau,  btlti  ,zu  reden  anfangen'^ hilu,  biloti  ,reden',  biUju,  -öti  , sagen,  reden',  byl-aü,  -öti  ds.,  hylä  ,Rede, Aussprache,  Unterhaltung',  lett.  bilstu,  bilzu,   bilst  (in  Zs.)  , reden,  anreden'.
124
hÜdet  ,anreden';  lett.  Ulldt  (aus  Hily,a)  ,weiiieii';  mit  Formans  -so-  lit.  Id sas  , Stimme,  Ton';  ■
toch.  Aß  päl-j  päl-  ,loben'  (Van  Windekens  Lexique  89).
Hievon  abgeleitet  Hhle-  ,blöken'.
WP.  II  182,  WH.  I  516,  Trautmann  25.
bh{e)läg-  etwa  ,schlaff,  albern^??
Hhläg-   oder   *bhlög-   in  wruss.  Mdhyj  
===== POK page 156 (POK_01 leaf 164) =====
  später  Abi.,  defungor ,bringe  zu  Ende,  überstehe^,  perfungor  _,genieße  ganz,  verwalte  zu  Ende^ WH.  I  565  f.,  Wackernagel  Synt.  I  68,  Jokl  L.-k.  Unters.  179. bbidb'  ,Topf,  Kübel,  Faß^
gr.  Ttid-oq  n.  ,Faß,  Weinfaß^,  Tti&dycvrj,  att.  q)Lddy,vr]  ds.,  lat.  fidelia (*fides-Uä)  ,irdenes  Gefäß,  Topf^;  vermutlich  aisl.  bida  f.  ,Milchkübel^, norw.  bide  n.  ,Butterfaß^  (*bidjan-),  bidne  n.  Gefäß.
Da  aus  lat.  fiscus  ,geflochtener  Korb;  Geldkorb,  Kasse^, /scma  ,gefloch- tener  KorV  (aus  *bhidh-sko-)  für  unsere  Sippe  eine  Grundbed.  ,geflochtenes Gefäße   erschlossen   werden    darf,   gehört  sie    wohl   zu   einer  Wz.  bheidh- ,binden,  flechtend WP.  II  185,  WH.  I  492  f.,  506. bbili-,  bbilo-  ,ebenmäßig,  angemessen,  gut,  freundliche
Mir.  bil  (*bhi-li-)  ,gut',  gall.  Büi-  in  PN  Blli-catus,  Bilicius  usw.,  ahd. hila-  ,gütig^,  jünger  bili-,  bil-  im  1.  Glied  von  Personennamen;  ags.  bile-wit ,einfach,  unschuldig^  =  mhd.  bilewiz,  bilioiz  ,Kobold^  (eigentl.  ,guter  Geist^); ahd.  bil-Uch  ,geziemend^;  Abstraktum  *bilipö  in  as.  unbilithunga  ,UnfÖrm- lichkeit^,  mhd.  unbilde,  unbilede  n.  ,Unrecht,  das  Unbegreifliche^,  nhd. Unbilde,  zum  Adjektiv  mhd.  unbil  ,ungerecht^,  substantiviert  Schweiz. Unbill.  Über  nhd.  Bild  s.  unter  bliei{d)-  ,schlagen^,  wozu  R.  Loewe  (KZ. 51,  187  ff.)  auch  Unbilde  stellen  will.
154
Gr.  (piXog  fieh,  wert^  usw.  stellt  Kretschmer  (IF.  45,  267  f.)  als  y] griechisch  zu  Ijd.  bilis  ,seiri^;  dagegen  Loewe  aaO.;,  der  die  Betonung  ^1 ersten  Silbe  aus  dem  Vokativ  erklärt.
WP.  II  185,  Kluge  11  unter  Bild,  hillig,  Unbill,  Weichbild.
hhlag'  ,schlagen^
Lat.  flagvum  ^Geißel,  Peitsche^,  ßagellum  ds.,  mit  Dehnstufe  wal scheinlich  flägitö,  -äre  ^zudringlich  und  mit  Ungestüm  fordern,  dringen} mahnen^  (ursprgl.  wohl  mit  Schlägen  und  Drohungen),  flägitium  ,Schau( tat,  Schändlichkeit,  Schande^  (ursprgl.  ,öffentliche  Züchtigung  und  Ai scheltung^;  conßages  ,loca  in  quae  undique  cönfluunt  venti'  Paul  Fest.  35l scheint  verderbt  für  conflüges)]
aisl.  und  nnorw.  dial.  blaka,  blakra  ,vor  und  zurück  schlagen,  fächeln] flattern^,    aisl.   blak    ,Schlag^,    aisl.    blekkja    (Hlakjan)    ,schlagen^    (non , flackern^),  schwed.    mdartl.    bläkkta   (*blakatjan)j   mndl.   blaken  ,fächel flattern,  schlottern^  (im  Germ,  lautlicher  Zusammenfall  mit  der  Sippe  vo! aisl.  blakra  ,blinken^  usw.,  s.  u.  *bheleg-  ,glänzen^;  so  ist  z.  B.  norw.  blakri sowohl  ,fächeln^  als  ,glänzen^).
Lit.  blaskaü  und  blo§kiü  (-sk-  a
===== POK page 158 (POK_01 leaf 166) =====
I  519  f.
I.  bblm-  :  bhlQi-  :  bhli-  ^glänzen',  auch  von  Narben,  Erw.  von  bhel-  ds.
Germ.  *blipia-  (*bhlei-tio-  oder  eher  *bhll-tio-)  ,\ic\\t,  heiter  (vom  Himmel, dann  von  den  Mienen,  der  Stimmung:)  fröhlich^  in  got.  bleips  ,gnädig, mild*^,  aisl.  blldr  ,mild  (vom  Wetter),  freundlich,  angenehm^,  ags.  bhpe ,heiter,  freundlich*^,  ahd.  blldi  ,heiter,  froh,  freundlich^,  as.  bllthön,  ahd. bilden  ,sich  freuend
As.  bll  n.  ,Farbe^,  Adj.  ,farhig',  afries.  bli{e)n  ,Farbe^,  bli  ,schön^,  ags. bleo  n.  ,Farbe,  Erscheinung,  Form*^  (wohl  *bllja-).
Ob  germ.  *bllwa  ,Blei^  (ahd.  blio,  -loes,  as.  bll,  aisl.  bly)  ein  mit  lit. blyvas  ,lila,  veilchenblau*^  sich  deckendes  Farbadj.  mit  Formans  -wo-  von unserer  Wurzel  war  (ein  dem  nhd.  blaih  entsprechendes,  allerdings  unbe- legtes kelt.  *blzuo-  aus  *bhle-uo-  als  Quelle  anzunehmen,  wäre  denkbar), ist  strittig,  aber  doch  das  Wahrscheinlichste.
Hierher  (nach  Specht  Dekl.  117)  russ.  bli-znd  , Fadenbruch  im  Gewebe^, ßech.  poln.  bli-zna  ,Narbe';  wegen  der  Parallelformen  unter  1.  bkleu- kaum  mit  WH.  I  517  zu  bhliy-.
Lit.  blyvas  ,lila,  veilchenblau';  vielleicht  lit.  blawas  ,nüchtern'  (wenn nicht  als  *blaid-vas  zum  verwandten  *bhhido-s),  blaivaüs,  -ytis  ,sich  auf- klären, nüchtern  werden';   vielleicht  lett.  bllnet  ,lauern,  blinzeln'.
156  9
Toch.  A.  plyaskem  ^Meditation^??  (Van  Windekens  Lexique  97).
WP.  II  210.
S.  auch  unter  1.  bhleu-  und  bhhido-s.
2.  bblei-  ^aufblasen,  schwellen^  strotzen^  überfließen'^  Erw.  von  hhel-  ds.
Norw.  dial.  hleime,  aschwed.  hlema  ^Hautbläschen*^  (vgl.  norw.  blcema  ^j unter   bhel-^  bh(e)le-)'^    dän.  blegn(e)  ^Bläschen'   {*blajjinön),   ags.   biegen engl,    blain,    mnd.  bleine,    älter    dän.    blen{e)j    aschwed.    blena    ^Bläscher^ i^blajinön).
Daß   gr.  cpliä  ^Türpfeiler,  Türpfosten'   eig.  _,(*geschwollener  =)  dickS Balken'   sei   (Prellwitz  ^  und   Boisacq   s.  v. ;    Gdf.  *bhll-uä   oder   -sä), dürfte  erst  auswärtiger  Bestätigung;   rä  q)Xi(X€Xia  ^Blutgeschwulst'  ist  ai lat.  flemina  verderbt.
bbleis-:    aisl.   bllstra   ,blasen,    pfeifen'?    (vgl.   got.  -blesan    unter    bheli bh(e)l-e-',    junge    Variation    mit   i  zur   Nachahmung    des   hellen   Tones?)' vielleicht  serb.   blihäm,  blihati   »überschwemmen;    speien;    den    Durchfall] haben';  blihnem,  blihnuti  ^anspritzen',  buig.  blici,  blikm,  blikvam  ^ergieße! mich,    ströme'  (wenn    nicht    als   ursl.  *blychajg    zur    w -Variante   von q)Xv(jü  usw.).
bhleid-  (vermutlich  c?-Präs.  *bhli-d-ö).
Gr.  (plidaco  ^fließe  von  Feuchtigkeit  über,  schwelle  davon  auf,  ecpliö^v diSQQsev  Hes.,  (plidavsc  öiaggeZ  Hes.,  dianecploLÖev'  diay
```


## [2026-09-05T06:21:22.016Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK leaf 134 (p.125-126, bhelgh) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==134' POK_01.txt | head -45\necho \"=== POK leaf 168 (p~158) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==168' POK_01.txt | head -40\necho \"=== grep barzis/barezis in POK ===\"; grep -n -i -E \"bar[əe.]?zis|barzis|barezi|Polster\" POK_01.txt | head -20",
 "description": "Pokorny bhelgh and bhleu pages"
}
```


### [2026-09-05T06:21:23.968Z] TOOL RESULT

```
=== POK leaf 134 (p.125-126, bhelgh) ===
,schlecbt,   bäßlich'  (daraus   lett. blägs,  lit.  blögas  ,kraftlos,  schwach'  entlehnt),  biazic  ,tollen',  grruss.  blag^ ,starrköpfig,   häßlich',    dial.  blainoj  ,dumm',   poln.  biagi   ,schlecht,    nichts wert';  kaum  zu  gr.  cpElyvvei '  davvsTetj  Xr]Qst  Hes.,  da  das  slav.  Wort  auf  i schwere,  das  griech.  auf  leichte  Basis  weist;  s.  unter  phelg-,  |
Hierher  (offenbar  mit  expressiver  Gemination)  aber  lat. /acctts  , schlaffe
WP.  n  183  f.,  680,  WH.  I  507  f.
bheld-  ,pochen,  schlagen',  vielleicht  ursprüngl.  cZ-Präsens  der  Schallwurzel  bhel,   •.
Aus   dem   Germ,  wahrscheinlich   dazu  mnd.  bolte(7i)   ,Bolz,  Pfeil',  ahd. bolzj  nhd.  Bolz,  Bolzen,  ags.  bolt  ,Bolz,  Pfeil',  schwed.  bult  ,Bolz'  (*bhld.\- vielleicht   auch   nhd.  Balz,  Vb.  balzen   und    bolzen,    norw.  mdartl.  bolt  m. ,männlicher   Waldvogel;    Kater',    nhd.  Bolze  ,Kater';   norw.  mdartl.    bolta^^ ,poltern,    vorwärtsstürmen',    älter    dän.  bolte  ,sich    rollen',    schwed.    bidtaj ,klopfen',    schwed.  mdartl.  bultra  ,sich   wälzen,    tummeln',    norw.    mdartlJ bultra  , lärmen,  tummeln',  abl.  norw.  mdartl.  baltra  ,sich  wälzen,  tummeln';
lit.  beldii,  -eti  und  beldziu,  belsti  ,pochen,  klopfen',  ablaut.  bildu,  bildeti jdröhnen,  poltern',  bdldau,  -yti  ,klopfen,  stark  poltern',  baldas  ,StößeP: lett.  beizt  ,schlagen'  (vielleicht  Kontamination  von  *beUu  =  lit.  beldiiu mit  telz-  ,schlagen',  Mühlenbach-Endzelin  Lett.-dt.  Wb.  278).
WP.  II  184,  WH.  I  560 f.
bheleg-  ,glänzen',  Erw.  von  bhel-  ds.
bhelg-:  ai.  bhdrgas-  n.  , strahlender  Glanz'  {*bhelgos)',  Bhfgavah'FL ,mythische  Priester  des  Blitzfeuers';  lett.  balgans  , weißlich';  vielleicht hierher  aksl.  blag^  ,gut',  russ.  (alt  und  mtdarl.)  bölogo  Adv.  ,gut',  eig. ,licht'  (Gegensatz  , dunkel':  ,böse');  toch.  AB  pälk-  , brennen,  leuchten, sich  erhitzen',  A  pälk,  B  pilko  ,Blick',  A  polkämts  , Gestirn'  (:  lit.  balgans), B  empalkaitte  ,nachlässig'  (Negation  -f  *palk-  _,leuchten'  neben  pälk-) ;
bhleg-:  gr.  q)Xeya)  , brenne,  senge,  zünde  an',  (pXeye&oj  ,senge,  setze  in Brand;  intr.  brenne,  stehe  in  Flammen',  cpUyfia  n.  ,Brand;  Entzündung] Schleim',  q)Uyuovr}  f.  , Entzündung;  Leidenschaft;  Brunst',  (pleyvag'  dstdg ^avd-og  Hes.  (Adj.  ,feurig  rot')  ^Ao^,  cpXoyiiög  , Flamme';
\a.t.flagrö,  -äre  , flammen,  lodern,  brennen',  wozu  wohl  flamma  ,Flamme* als    *flagmä,    osk.    Flagiui   etwa  ,Fulgurätöri' ;    neben  fläg-    (red.-stufiges
125
*hhl  cjvö-   *hhlegnid  oder  wegen  (pXoyi.i6g,  (pl6^  eher  Hldogma)  steht  schwund- fio-es  bhlg'y  lat.  fiäg-  in  lat.  fulgö  und  fulgeö,  -ere,  fulsl  ^blitzen,  schim-
ern    leuchten^,  fulgor,  -öris  ^das  Bhtzen,  Schimmer^  GLinz^,  fulgus,  -uris BlitZ;  Schimmer^;  fulmen  (*fulgmen)  ds.; ^    mir.  imhlissiu  ^Augenstern'   (^mhhi-hhlg-s-,  
=== POK leaf 168 (p~158) ===
en'; ,Dämmerung'.
Ai.  bradhnd-h  (*bhlndh-no-)  ,rötlich,  falb';
germ.  *blundaz  (*bhlndh-o)  in  mlat.  blundus,  ital.  biondOj  frz.  blondj woraus  mhd.  bluntj  nhd.  blond -^
got.  blinds  ,blind',  aisl.  blindr  ,blind,  undeutlich',  as.  ags.  blind,  ahd. blint  ,blind',  auch  ,dunkel,  trübe,  nicht  sichtbar';  got.  blandan  sik  ,sich vermischen',  aisl.  blanda  ,mischen'  (blendingr  ,Blendling'),  as.  ags.  blandan, ahd.  blantan,  mhd.  blanden  ,mischen,  trüben'  (nhd.  Blendling  ,Mischling'); zum  germ.  a  vgl.  das  Iterativ-Kausativ:  ahd.  blendan  (*blandjan)  ,ver- dunkeln,  blenden',  ags.  blendan  ,blenden'  (:  blandytis,  aksl.  bladiti)]  aisl. hlunda  ,die  Augen  schließen',  blundr  ,Schlummer',  mengl.  blundren  ,um- rühren,  verwirren',  nengl.  blunder  ,sich  gröbKch  irren,  tappen';
lit.  blendziü,  blesti  ,schlafen;  das  Essen  mit  Mehl  einrühren',  lett.  blendu, bleust  ,mcht  recht  sehen,  kurzsichtig  sein,  schauen';  lit.  blandaüs,  -ytis  ^^iq Augen  niederschlagen,  sich  schämen'.,  lett.  bluodities  ,ds.;  herumschlen- dern', lit.  blaüdas  ,Schläfrigkeit,  trübes  W etter^ j  blandüs  ,bündig,  von  der Suppe    (eingerührt);    trübe;    dunkel';   lit.    blista,   blindo,   blisti  ,dämmrig,
158  •
dunkel  werden;    trübe  werden,  vom  Wasser^,  pryhlinde   (und  prieblandl ^Abenddämmerung*^;  hierher  auch  blinde^  hlendiSj  blünde  ^Salweide^;
aksl.  bledg,  blesti  girren;   noQvsveiv\  bledh  ^Geschwätz,  Possen^,  slov.  hl dem,  blesti  ;,faseln,  phantasieren^,  acech.  blesti  (2.  Sg.  blede§)  ,faseln^;  aks| blgd^  ^Ttogvsla^  poln.  blqd  Jrrtum^,   aksl.  blozdq,  blqdlti  girren,   TtOQvavBii skr.  blüdlmj  bluditi  ,irren,  betrügen^  usw.
WP.  II  216,  218,  Trautmann  34  f.,  Endzelin  KZ.  52,  112,  Specht  Del 58,  117.
Gehört  wohl  zu  1.  bhel-.
hhles-  ,glänzen^,  bisher  nur-im  Germ,  nachweisbare  Erw.  von  bhel-  ,glänzen* Mhd.  blas  ,kahl,  bleich^  (nhd.  blaß)  n.  ,Fackel,  brennende  Kerze^^  a^ bloßse  ,Fackel,  Feuer^,  engl,   blaze  ,Glut;   weißer  Stirnfleck^,  ahd.  blas-n ,Pferde  mit  einer  Blässe^  (lichtem  Fleck  auf  der  Stirn),  mnd.  bles^  blesn (*blasjö)    ,Blässe^,   aisl.    *bles-  in   blesöttr  ,mit  einem  weißen  Fleck,  einer Blässe  gezeichnet^  und  in  Kompos.  auf  -blesi. WP.  II  217.
bhleu-    , aufblasen    (schnauben,    brüllen),    schwel
=== grep barzis/barezis in POK ===
1572:got.  bida  ,Gebet',  ahd.  beta  f.  ,Bitte',  got.  bidjan  (sek.  -bidan)  ,bitten, beten',  aisl.  bidja,  ags.  biddan,  ahd.  bitten,  aisl.  kne-bedr  m.  , Kniepolster', ags.  cneow-gebed  n.  ,Gebet'  (vgl.  a,i.  jfiU'bädh-)]
1671:Ai.  bhända-  n.  ,Topf,  Gefäß'  {*bhäln-da?) ;  nach  Thieme  (ZDMG.  92,  47  f.)1 hierher  av.  bat^-s-man-  ,Bündel  von  Zweigen',  ai.  bdrsva  m.  PL  ,Wulst,f Zahnfleisch'  (Lw.  aus  av.  *barsman  , Polster');    vgl.  unten  ahd.  bilorn.      %
1761:bbelgh'  ,schwellen;    Balg   (aufgeblasene   Tierhaut),    Kissen,  Polster'  (Erw.
1763:Ai.    barhü'   n.   ,Streu,    Opferstreu'  =  av.  bardzis-  n.  ,Polster,    Kissen'
1764:npers.  bälis  , Kissen';   ai.  upa-bdrhana-m,   npa-bdrhanl  f.  , Decke,  Polster';
1769:got.  balgs  ra.  ,Sclilauch',  aisl.  belgi^  m.  ,abgestreifte  Tierhaut,  Balg Bauch',  ahd.  mhd.  balg  ,Balg,  Schlauch,  Blasebalg,  Schwertscheide',  agg, bielg,  byl{i)g  ,Balg,  Beutel',  engl,  belly  ,Bauch',  bellows  ,Blasebalg'  (germ. *balii-  m.,  vgl.  apr.  balsinis]  vielleicht  hat  auch  ai.  barhls-j  av.  barezii, idg.  -i-s-  als  Erw.  dieses  i-St.);  .
1771:aisl.  bylgja  ,Woge',  mnd.  bidge  ds. ;  *bul{h)stra-  in  aisl.  bolstr  m.  ,Kisseii' ags.  bolster  n.  ,Polsteri  Kissen',  ahd.  bolstar  ds.,  ndl.  bolster , Fruchtbalg,  Hülse'
1772:apr.  balsinis  ,Kissen'  (*bholghi-nos),  pobalso  , Pfühl',  lett.  pabälsts ,Kopfkissen'  (und  , Stütze',  s.  oben  S.  123);  slov.  blazina  ,Kissen,  Matratze] Bettpfühl;  Fuß-  oder  Handballen'  (und  , Dachbalken,  Querbaum  des* Schlittens,  Rungstock',  s.  oben  S.  123),  skr.  blazina  , Kopfkissen,  Polster^ti Federbett';  russ.  bolozem,  m.  , Schwiele,  Beule,  Leichdorn,  Hühnerauge^! (aber  russ.  dial.  bölozno  , dickes  Brett').  Hierher  wohl  als  ven.-ill.  Lw.^t apr.  balgnan  n.,  alit.  balgnas,  lit.  balnas  , Sattel'  (wohl  aus  ,Kissen').  Weitere  ' baltoslav.  Formen  s.  oben  S.  123.  -|
```


## [2026-09-05T06:21:31.362Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=1761{n+=gsub(/\\f/,\"\")} END{print \"leaf idx for line1761:\", n+1}' POK_01.txt\necho \"--- bhelgh full ---\"\nsed -n '1758,1780p' POK_01.txt",
 "description": "Locate bhelgh page and print"
}
```


### [2026-09-05T06:21:33.027Z] TOOL RESULT

```
leaf idx for line1761: 135
--- bhelgh full ---
Über  nhd.  Block  usw.  s.  unter  5.  bhel-.
WP.  II  189,  Hirt  Idg.  Gr.  II  150,  Feist  79,  100,  Specht  Dekl.  133.
Daneben  eine  Wzf.  bhleii-  :  bhhu-  :  bJilü-,  s.  dort.
bbelgh'  ,schwellen;    Balg   (aufgeblasene   Tierhaut),    Kissen,  Polster'  (Erw.
von  bhel-  ,aufblasen'  usw.).
Ai.    barhü'   n.   ,Streu,    Opferstreu'  =  av.  bardzis-  n.  ,Polster,    Kissen'
npers.  bälis  , Kissen';   ai.  upa-bdrhana-m,   npa-bdrhanl  f.  , Decke,  Polster';
Ob  mit  Asp.-Diss.  gegen  das  Formans  -ha-  hierher  ai.  bdrjaha-h  , Euter'?
ir.    bolgaim    ,schwelle',    bolg   f.   ,Blase',    bolg  m.   ,Sack,    Bauch,    Hülse,
126  '
,  Hose',  mir.  holgach  f.  ,Beule,  Blase,  Blatter;  Pocken',  bolgamm  ,Schlucl^^ cymr.  hol,  bola,  holy  ,Bauch,  Sack',  hui  ,Sainenhülse'  (PL  von  holy),  bret; holc'h  ,cosse  de  lin',  vann.  pehl-en  (aus  *pehl-)  ds.,  gall.  bulga  ,Ledersac]i< (daraus  ahd.  hulga  ,lederner  Wasserbehälter*);  gall.  Belgae  ,die  Zornigen^
got.  balgs  ra.  ,Sclilauch',  aisl.  belgi^  m.  ,abgestreifte  Tierhaut,  Balg Bauch',  ahd.  mhd.  balg  ,Balg,  Schlauch,  Blasebalg,  Schwertscheide',  agg, bielg,  byl{i)g  ,Balg,  Beutel',  engl,  belly  ,Bauch',  bellows  ,Blasebalg'  (germ. *balii-  m.,  vgl.  apr.  balsinis]  vielleicht  hat  auch  ai.  barhls-j  av.  barezii, idg.  -i-s-  als  Erw.  dieses  i-St.);  .
aisl.  Partiz.  bolginn  ,geschwollen',  Kaus.  belgja  , aufschwellen  machen' as.  ags.  belgan  St.-V.  ,zornig  sein',  ahd.  belgan  ,aufschwellen',  refl.  ,zö^ nen',  afries.  Partiz.  ovirbulgen  ,erzürnt';
aisl.  bylgja  ,Woge',  mnd.  bidge  ds. ;  *bul{h)stra-  in  aisl.  bolstr  m.  ,Kisseii' ags.  bolster  n.  ,Polsteri  Kissen',  ahd.  bolstar  ds.,  ndl.  bolster , Fruchtbalg,  Hülse'
apr.  balsinis  ,Kissen'  (*bholghi-nos),  pobalso  , Pfühl',  lett.  pabälsts ,Kopfkissen'  (und  , Stütze',  s.  oben  S.  123);  slov.  blazina  ,Kissen,  Matratze] Bettpfühl;  Fuß-  oder  Handballen'  (und  , Dachbalken,  Querbaum  des* Schlittens,  Rungstock',  s.  oben  S.  123),  skr.  blazina  , Kopfkissen,  Polster^ti Federbett';  russ.  bolozem,  m.  , Schwiele,  Beule,  Leichdorn,  Hühnerauge^! (aber  russ.  dial.  bölozno  , dickes  Brett').  Hierher  wohl  als  ven.-ill.  Lw.^t apr.  balgnan  n.,  alit.  balgnas,  lit.  balnas  , Sattel'  (wohl  aus  ,Kissen').  Weitere  ' baltoslav.  Formen  s.  oben  S.  123.  -|
WP.  II  182  f.,  WH.  I  122.  Vgl.  über  gr.  nolyog  ,Ledersack'  Vendryes BSL.  41,  134  f.
bhen-  ,schlagen,   verwunden';    auch  von    durch    den   Schlag   böser   Geister bewirkter  Krankheit  (avest.;  vgl.  zu  diesem  Aberglauben  Havers  IF. 25,  380  f.) Av.  bqnaydn  ,sie  machen  krank',  banta-  , erkrankt,  siech'; got.  banja  , Schlag,  Wunde,  Geschwür',  aisl.  ben,  ags.  benn  f.,  as.  beni- tüunda   ,Wunde';    aisl.  bani   m.  ,Tod;    Mörder',   ags.  bana^    ahd.    as.  bano ,Totschläger,  Mörder',  ahd.  bano,  mhd.  hane,  ban  ,Tod,  Verderben';    viel- leicht auch  mhd.  bane,  ban  f.  und  m.  ,Bahn,  Weg'  als  ,*Durchhau  durch einen  Wald'  oder  ,*festgeschlagener  Weg';   mir.  epit  f.  , Hippe'  aus  *ek8- bhen-tl-  corn.  bony  ,Axt';  aber  cymr.  &on-cZws^ , Ohrfeige' enthält  bon  , Stock'. Av.  bata-j  wenn  ,geschrotet,  vom  Getreide',  könnte  als  *bhn-to-  verwandt sein,  ist  aber  wegen  der  unsichern  Bed.  nur  mit  Vorbehalt  zu  nennen. WP.  II  149,  Feist  80.
bbend'  etwa  ,singen,  schön  klingen,  jauchzen'.
Ai.  bhandate  , empfängt  jauchzenden  Zuruf,  wird  gepriesen,  glänzt', bhdndi§tha-h  ,am  lautesten  jauchzend,  gellend,  am  besten  preisend',  bhan-
w
127
. ,  ^,^    jauchzend^,  bhanddnä  , lustiges  Tönen,  Jauchzen^  (die  Bedeutungen T    bezweifelt);    schwundstufig    air.   mir.   bind    , melodisch^,    abret.  bann
canora^ '    WP.  II  151  f.
```


## [2026-09-05T06:21:33.618Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT barzis ===\"; grep -n -E \"bar\\^zi|barezi|barziš|bar.ziš-|barəzi\" BRT.txt | head -20\necho \"=== BRT barsman ===\"; grep -n -i -E \"barəsman|bar.sman|baresman\" BRT.txt | head -20\necho \"=== BRT barsnu ===\"; grep -n -i -E \"bar.šnu|barasnu|barsnu\" BRT.txt | head -10",
 "description": "Bartholomae lookups"
}
```


### [2026-09-05T06:21:33.697Z] TOOL RESULT

```
=== BRT barzis ===
16999:bar^ziäta-
17023:•  j.  bar9zi§-  n.  'Polster,  Kissen':  >?  narS hämS^ätvü  nipaüyeinte  Aqm  vä  paiti  stairis Aqm  vä  paiti  '«/V.J.  27;  —  cvat  alte slairisca  °tisca  aesa  druxs  .  .  fräshaoiti V.  7-9;  —  aitaoa  altahe  aste  (Sp.  340) slairii^a  °zi/^a  hqm.v^rtnattte  V.j.  59;  — ana  'zis  sayamnanqm  (sd.)  V.  lü.  26;  — gätu  *x''aiiii.star»tu  (sd.)  mai  °ziia  V. 7^14.         [Yt5.  loa:  lies  bar^zi/Aav'.]
=== BRT barsman ===
190:Die  angeführten  Texte  bringen  ausserordentlich  zahlreiche  Wiederholungen. Und  zwar  sind  entweder  zwei  oder  mehr  Stellen  einander  völlig  gleich  oder  sie unterscheiden  sich  nur  in  untergeordneten  —  d.  h.  für  das  Wörterbuch  wenigstens untei^e ordneten  —  Stücken.  Als  Beispiel  für  die  erste  Art  von  Wiederholungen mögen  dienen:  Y.  65.  2-5  —  Yt.  3.  2-5;  Yt.  5.  10  =  12,  14,  16,  20  (usw.);  Yt. 5. 19  =  23,  27,  35,  39  (usw.);  Yt.  JO.  98  =  135;  Yt.  j^.  15  (von  hü  bis  taxmahe')  ^ Yt.  10.  70,  127;  Y.  57.  25  (von  akeca  an)  —  Yt.  10.  93  usw.  —  Die  Wiederholungen der  zweiten  Art  zerfallen  in  verschiedene  Gruppen:  Yt io.  103  wiederholt  sich  von yS  hantaia  an  wörtlich  in  Y.57.  isfl,  nur  dass  hier  das  ca  hinter  har>ta  fehlt; irgend  ein  Grund  für  die  Abweichung  ist  nicht  vorhanden.  Yt. /o.  94  (^=  114I und  Y.57. 26  stimmen  völlig  lusammen,  nur  dass  auf  die  Eingangsworte  aäa  nS tum  dort  der  Vokativ  mikira  vouru.gaoyaoite,  hier  aber  traosa  afya  huraöha  folgt; die  Gebetsformel  ist  die  selbe,  aber  die  Adresse  ist  verschieden.  Ähnlich  steht es  mit  den  vier  in  Yljo.  igof.  enthaltenen  Stücken,  die  von  vier  Waffenarten Mihras  durchaus  das  Gleiche  aussagen;  nur  eben  die  Namen  der  Waffe,  sowie deren  Beiwörter  machen  die  Verschiedenheit  der  Stücke  aus.  Besonders  zahlreich findet  sich  diese  Art  der  Wiederholung  im  Viälvdäi  {Vendidad);  z.B.  unterscheiden sich  in  dem  Kapitel  über  die  Verträge  (V.  4)  die  Abschnitte  6  bis  10  und  ander- seits II  bis  16  nur  durch  den  Namen  des  Vertrags  und  der  Zahl  in  der  Buss- bestimmung. Femer  haben  V.p,  53,  54,  55  und  S7  '^'on  üäca  an  den  gleichen Wortlaut,  nur  dass  das  dreimalige  para  von  53  in  54  durch  kaha,  in  55  durch nöü,  in  57  durch  pascalta  ersetzt  ist  In  den  liturgischen  Teilen  des  Yasna  wieder sind  grosse  Stücke  bis  auf  die  Eingangs-  oder  Schlussformel  gleichlautend.  So decken  sich  Y,  i.  3  ff.  und  5.  5  ff.,  4. 8  ff.,  7.  5  ff.  vollständig  bis  auf  die  Eingangs- worte, die  zu  Y.  1:  nivaiöayemi  hankärayemi,  zu  Y.^:  äyese yeSH,  zu  Y.  4:  Hat  dis äva^ayamahl,  zu  Y.  7:  alaya  daöami  lauten,  während  anderseits  Y.  2.  äff.  und 6.\S.  nur  darin  auseinandergehen,  dass  hier  (Y.  6)  jeder  Abschnitt  mit  yatamatde endet,  dort  (Y.  4)  jeder  mit  ahmya  zaohre  bar>smanaica  eingeleitet  und  mit  äyese yeiti  geschlossen  wird.
3987:■  j.  aiwylnhana-  n.  i)  'Gürtel,  Gürtel- schnur'*>:  'n^m  r3  aiwya»hayamnS  'mm bO/ayarnnS  (sd.)  Yti.iT,  —  /rä  i! mazdä  harat  ..  'n^m  ..  vanuhim  daSnqm mäzdayasnlm  "dir  (dem  Haoma)  brachte M.  einen  Gürtel  . .,  (näml.)  die  gute mazday.  Religion"  Y.9. 26'*;  —  yat  alle yö  mazdayasnS  ap^rmäyBks  avi  hs  hapta ■na  /rajasäiti . .  °nö "'  paitis  h!  maiayai bU)yamanS  avi  hlnara pascaili  tamauhmti 'wenn  dem  jungen  Masday.  sieben  Jahre vergangen  sind,  soll  man  ihm  den  Gürtel um  die  Hüften  legen,  worauf  ihn  die Männer  (als  ihresgleichen)  achten"  Vd, 18;  20'; — jairyö  °nö  ißjyamanff  "vieitem legt  man  (dem  Toten)  die  Gürtelschnur um"  Vd. /23),  a)  von  der  Schnur,  mit der  die  Barvsmanzvreigt  in  Bündel  zusam- mengebunden werden"":  a^a  'na  N. ioS(?).  2)  'Gewand,  Kleid';  ^5  iama *°«o"  aiitryia^qyanii  "wenn  zwei  gleiche Kleider  anziehen"  N.p4(?);  — yaii  tarasca 'na  aipi.vancainii'^.gs^); — bilyS  ant?ma 'nH  "zweitens  (soll  man  dem  Toten  mit- geben) das  Untergewand"  Vd./i>3'.
4680:■jpB  k^rinaol  frasa  •iiyil  fralacat  (sd.)  Yt. 5.78.  a)  NS.  mit  folg.  obl.  Kasus  'ein- ander', mit  part.  Gen.:  asa  vi  'nyS  'inim vXvBnghaiR  "einer  von  euch  soll  den  andern an  Gerechtigkeit  zu  Übertreffen  suchen" Y.5J.  s;  —  am>sanqm  sp^ntanqm  ..yaeiqm 'iiiyS  'inyehe  urväntm  ami.vaenaiü  Yt y-84>  —  vgl.  aiiyd.anya:  2)  Du.  in Verbindung  mit  agta-  Du.  'hie  et  alter': yB  . .  amqsia  (sd.)  *x^ar5.a^aya  *alU  'nye (ADn.)'>  ^cikayatB  ". .  hoc  et  alterum  . ." ^'3  c;  —  atitari  *ha>:r>mcit  *<7Ä^(ADn.) 'nya  (ADm.)»>  itpaisat  "innerhalb  eines H.  soll  man  dies  (barfsman-  n.)  und  jenes (alsma-  m.)  suchen"  N.  log.  I  a)  mit
7131:—  y5  "tr^iii  uruzdipäk»tn  däitlm  gätUm avi  avaiaraiti  V.S.Sz;  83—96'*;  —  näi/ faahö  ahmst  ^ad^mm  vtr^nyäti  yaaöit Ptti:rahe  .  .  nasQm  pacät  paiti  '^re  üAfm baräiY.iO.iT; — yd  naiäum  matgü^qm ..'tr^m  ,'l../rabarinH\.y.2^.  a)neben| Wasser,  Rind,  Pflanzen,  Barssman  usw.:' para  asmgm  .  .  äpim  .  .  zqm  .  .  gqm  .  . urrarq/n  . . 'trwi  Y.ig.2;  —  iulia  "tnm , .  .  äpfm  .  .  zqm  .  .  gqm  .  ,  urvarqm  . . yaaidainni  V.ii.j;  3,  $,  9,  10,^.33,  42;
8471:'  'um  "ranqm  uzuxfyenlinam  srlranqm zairi^aoiianqm  vaxsA  (sd.)  apayasaite  V. /Ä63;  Yt. /Ä6;  —  at  aRyäi  (näml.  dem Rind)  mazdä.  'rä  vaxiaj  (sd.)  Y.4S.6;  — avi  racynyq/H  varauhmt  azuitlmca  'ranam Yt.  ^2.3;  —  nima  'vaire  (VS.)  varMhi masdaöäte  asaone'V.  ig.ii;  Vyt.22,  N.7/, f)7.  a)  Plut.,  im  Gegens.  zu  alxa-  Plur., 'pflanzenbewachsener Boden';  ahond  una 'rlhuca  paiti  *baooisca  vTdtnanmnS  saoa- yäti  . .  ärvatS  urva  *aexahuea  (sd.) . .  "der Seele  des  Gläubigen  ist  es  so,  als  ob  sie auf  Wiesengiund  (stehe)  und  Wohlgerüche empfinde,  .."H.  2. 7— 25.  b)  sva, 'Baum', a)  im  Gegens.  zu  var^ä-.  pairi  van>'>iJ- byasca  'räbyas^a  atsmaiibyS  (sd.)  V.  16. s.  ß)  sonst:  v3r»ynahe  . .  yS  .  .  sainif marisat  'ranqm  ". .  der ..  im  Flug  der  Bäume Wipfel  streift'"  Yt./.4.2i''.  c)  'Pflanzen- Stengel,  Reis':  yavat  akmUi  paitinqm •ranqm  aetavat . .  "so  viel  es  ihm  einzelne Reiser  gibt,  (als  ob)  er  so  viel  .  ."  V.  iV. 86,  a)  bes.    der   zum  Barisman    ge-
11486:Bed'.?  —   11  Son^l  i'aiip-  gelesen,   wofür  die  '  — *°J'«/1''  nä  *mt>ma  bartsmana  ratufrisi
14314:\tavaia  hüXimä  asaAyäl^ä  Y.  40.  a;  — hubfrfti  .  .  atari  Sfrinämi  huyesti  1  tnva ahuränt  äfrJnämi  Y.  68. 14;  —  äyese  yeili Aavanaeibya  .  .  tastai  . .  varfsäi  ..  I  tavafa bargsmanS  Vr.  70.  3;  —  avi  apqmla  .  . yasrmn  gsrpömaki..  I  avi  tava  zard^uitra Vr.  27.  if.;   z=.  zu  1  b):  \tava  ätars
14656:*)  Die  Zahl  der  Zweige  war  bei  den  verschie- denen Zeremonien  verschieden;  drei  lum  min- desten; vgL  zu  barisman-.
14690:•  j.  BriS.urvarä-  Adj.  (maslc.  Ta-)  'drei Pflanzenstengel  enthaltend,  daraus  be- stehend': tvat  (lies  cvald)  nä  nit^ma barysmana  ratufrisl  'ra  (ISn.)  "wie  um- fangreich muss  das  B.  zum  mindesten sein,  wenn  man  r.  sein  will?  Drei  Pflanzen- stengel enthaltend."   N.50.
14891:Entgelt)  dafür':  äa^  mqm  tarn  *^aisaxyilii ..  dahäni  tl  aStahe  'ti  V.22.  2f.'3>;  — iat  astahe  'ti  ..  azaeta  (Sp.  2240.)  V. iK  68**;  —  ait»)n>m  ijaoiinanqm  .  . altahe  'ti  .  .  duye  saite  upaeananqm  upä- «3(V  (Sp.  224  m.)  V.  4.  2o'4).  '4)  zur Bezeichnung  der  Ursache  und  Urheber- schaft, sowie  des  Mittels  'per';  i)  mit  Akk.; a)  'mittelst':  frasnatse  .  .  ayryqm  (sd) 'ti  usnäitlm  V,  Ä  98;  —  mi^ra  ahura  .  . yasamaide  .  .  urvarä  'ti  batvsmanyä  Yt. 10. 145  (s.  2a);  —  yasiä  Hl . ,  väHm  °ti tofnis  {sd.)  anhat  V.  7^,  40;  — aitakmllyus 'ti'>^  AirÄ^w  V./5.ai,  43.  b)'wegen, propter':  aitahmSyiti  'ti"'''  varsla  syao^na V.  75. 10.  2)  mit  Lok.;  a)  'mittelst': ahura  mi>ra . ,  urvaräÄu  *ti  bar)smanyähu .  .  äyese  yati  Y.  2,  11  (s.  i  a);  —  */tahmäi tl  aioahmi  'ti  vaSs  . .  /ravaktm  (sd.)  H. /.  I*'; —  handaitim  staotanqm  yesnyanqm yasamaide  apan3J»may3  (sd.)  °tl  va^astaltä Y.sS.S'^-l  b)  'durch':  saräku^lrahe  . . yakmi  'ti  .  ,  *asim.srav3  (sd.)  vTsruyaia Yty.  91.  c)  'wegen,  propter':  nSil.. ahmi  'ti  nairi  dva  *mainyu  r}na  (sd.)  ava.- stäahat  V.  7. 52.  3)  mit  Gen, ;  a)  'mittelst'; yqm  yazata  zarä^uströ  . .  humatahe  °ti manavAlF    Yt.  16.  6;    6'.  b)    'wegen,
16982:barasman-  Noten
16984:•  j.  barasman-  n^  meist  kollekt  Sing., Bezeichnung  eines  beim  Gottesdienst  ge- brauchten ZweigbUndeIs*':*Äa/a  nä  *mbma 'tnana   ratufrisi  %rilurvara  (sd.)  N.fjo;
17003:AbleiL  aus    barisntan-;    vgl.  bar?smanya-  und
17004:vor  %  igS-  —  V^:  I  iatsm. ■  j.  bar^smanya-  Adj.  (fem.  'yä-)  'zum Bansman  gehörig,  gebraucht  (usw.),  Bar»s- man'':  un>araku  paiti  °nyähu  mi^r^m  . . Syese  yeid  Y.  2.  1 1 ;  —  utrarä  paiti  *nyä mi%nm  yasamatde  Yt  10. 145.
17006:•  j.  bar«8mö.st9r«tay-  f.  'Spreituog von  Bargsman':  aivayacit  *alsm5.st»rnti alvayacii  •riiiti  (IS.)  P.  24;  N.  103.
17008:•  j.  barasmö.zasta-  Adj.  (fem.  '/ä-) 'Barvsmanistengel)  in  der  Hand  habend, mit  B.  in  der  Hand'-,  yas^  Sics  . .  Jrä- yaxäile  . .  'iS  Y.  62.  i;  \.  3.1;  —  *yim aiwitö  mazdayama  histmta  'ta  Yt,  5.  98; —  'ta  (NSf.)  .  .  mittum  harat  .  .  ar^ävl sara  Yt5. 127.
17534:•  j.  (fraka-)  Adj,  'vorwärts,  berangewendet*, nur  IS,  und  ASn,  als  Adv,;  i)  IS.  fraka 'vorwärts,  hervor,  von  der  Stelle'  (nur Komp.).  3)  hß,Ti..frak»m  'heran,  herbei', mit  V.  ^bar-  sva^.  fra-öar-:  fraÖ»r>lars  {s,A.) yat..bar>smanca  'ksm  [yCixsA.bar3{)S'^raf^a yasnö.k>rgtaeibys  paiti.bara}  N.  74.
17682:betrauten  Unterpriesters  (ra/av-) :  äat  'iari (GS.,  näml.  kairim)  yal  a%rasca  alvqm hraxiim  yaoida^ai  barismanca  frahm ähralca  yasf0.k»r>taiibyd paiti.barät  "(das Amt)  des  Fr.  (ist),  dass  er  eine  Ecke  (ein Viertel)  des  Feuers  gehörig  in  Stand  setzt und  die  .^.-Stengel  herbei  und  dem  Feuer bei  jedem  yenhi-hStqm-Qi€at'(.  (Brennholz) hinzubringt"  N.  ■]4;  —  ava^a  "ta  *zaohrä frabaröit  N.  68;  —  'lar^  däityS  gätus *haoyqm  upa  %raxiiin  fratarqn  bansmqn "des  Fr.  gehöriger  Platz  (ist)  auf  der linken  Seite  vor  dem  B"  N. 75";  81, *Vyt  15";  —  paoiryS  .  .  kavanämm  (sd.) ..  astayeiti  ..  '^ritlm  'tat>m  N,  i'2;  — 'tänm  ästäya  Vr,^.  i;  G._J.  5;  —  ätra- 7'ax/e  vä  'itre  va  V.5.  $7;  58;  —  Va  N. 7J,  *6yi\ Elg.  'der  herzuträgt'.  —  Vgl.  ax.  fräb/iatiar-  m.
21440:yas3  ('wie  sva.  womit')  hwä  yazata vTstäsps  Yt77.  61;  61,  5.90,  91,  /5- 54, V.  75.  17,  Vyt.20,  3/;  — ka%a  zaota  xsäta apB ..yazäile  Y.ö^.g;  —  tim  yazät surunvata  yasna  sraol»m  . .  zaokrabyB  (DP. statt  IP.)  Y.57.  3;  Yt.>  18,  70.  31 ;  —  yö aHm  yjzäite  zaohräbyB  Yt/7.  2;  2,  8.\, 10.6,  Y.68.10;  —  yatal^a  mqm  zara- ^uära  ..  zaokrräbyS  Yt  /.  9 ;  mangelhaft  zitirt F.4g; — hvanx^aitim ..yazamaide  haomays gava  barismana  .  ,  zaohrabyasca  arsux- öaäbyasca  vayzibyS  (DP.  statt  IP.)  Ny.  7. 1 6 ; —  yazayania  %wqm  mazdayasna  pasubya staoraHbya  vayalibya  pataraialibya  (sd.)  Yt 10. 1  \(j;—ultaiaiiya  (LS.  statt \%.)ca  vTspnn asavamm  .  .yazamaide  Vr.  18, 2.  b)  Akk.; tarn  yazata  kaolyaahü . .  sat)m  aspanqm  . . hazaisr)m  gavqm  "ihr  opferte  ff. . .  hundert Rosse, .."  Yt. 5.  21;  p.  ag;  —  tarn  yaztnta .  .  hunavB  .  .  sat>m  aspanqm  Yt  5.  57; 72.  c)  paiti  mit  Gen.(?);  yqm  yazata zara'huitrS  humatahe  paiti  mananhS  Yt 16.  6.  2)  mit  Angabe  des  wozu?  durch
21673:yäiamtha  V.  JÄ  19;  Y.g.2;  —  zaohra äyese  {iSPM.)  yeiH  Y.2.1;  i»,  a-i8;  — akmya  tao%re  barysmana^a  ratavo  main- yava  äyese  yesH'VT,2.i;  i',  2— 11,  io.it*, Y.  23. 3,  62.  ji;  —  äyese  ydH  *ä  *fravase (statt  AP.)'>  Y.zy.a'.
=== BRT barsnu ===
```


## [2026-09-05T06:21:41.534Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- around 16975-17030 ---\"; sed -n '16975,17030p' BRT.txt\necho \"=== search barzant/hoch ===\"; grep -n -E \"bar\\^z|bar>z|barrf|barez\" BRT.txt | sed -n '1,40p'",
 "description": "Bartholomae context"
}
```


### [2026-09-05T06:21:41.598Z] TOOL RESULT

```
--- around 16975-17030 ---
DsT.  ZA.  2.  608 ;  "marchant  lous  le  fardeau ', Gdn.  3Yt.  118:  "in  brünstiger  Jugendkraft (stehend)".    Ob  *barima-\-'a-ya(ma-t
•  j.  bairya-  n.  1)  'Tragen,  Bringen (usw.)'.         a)  'Empfangen'.
KompE.  —  Zum  V,  ^bar-.
•  j.  baoirya-  Adj.  (fem.  •ys-)  'was  gekaut werden  muss,  fesf,  von  Speisen:  gam -yam  "(die  feste  ">  Nahrung,  die  das  Rmd liefert,  d.  i.)  dasFleisch  des  Rinds"  Y.^.  3  GL, 7- 3  Gl.
Ir.  'iargiia-  (%36S.  44).  PFP.  »um  ai.  V.  Mir* voll  'er  kaul';  vgl,  Haaurva-  und  Bim.  BB. to,  272.  —  mp.  /iV  i  iärt  'fetle  Nahrung* N.  66  (,  6/,  /6);  i.  auch  SO.  —  PQ.j  fehlt, aber  5U.:  gäm  iavaräm  (eine  nngescbickle Wiedergabe  des  inp.  Mr);  Bthl.  IF.  11.  139, —  ')  Im  Gegens.  lu  jfvya:  —  •)  Vgl.  mp. mär  anter  mamvay: ■  j.  haourva-  Adj.  'kauend'.
KompE.  —  Zum  ai.  V.  bhiniati  'er  kaut'.  —
dby  Google
barasman-  Noten
94«
•  j.  barasman-  n^  meist  kollekt  Sing., Bezeichnung  eines  beim  Gottesdienst  ge- brauchten ZweigbUndeIs*':*Äa/a  nä  *mbma 'tnana   ratufrisi  %rilurvara  (sd.)  N.fjo;
—  sraostm  . ,  yS  paoirys  'ma  frastn-mata %ryaxstlli!a  panca.yaxltT^a  Aapta.yaxällca nava.yaxitii^a  ox^nosca  mathydi.patti^tä- nasca  Y.5J.6; — yaj  'ma  a^.dräjS yave.- frä^S  .  .  yat  masyS  aBakmät  °ma  N.  70;
—  'ma  hiusbärayat  alsS.dra.jO  yavS.fi-ä^S V.  19.  19;  —  yB  anu  ailam  (sd.)  'ma *frast3nnte  yäka  .  .jämäspS  */rashr)nalla ratufris  ^.8g;  loi,  102;  —  anyahu  ratu-
frisu  latatarS  *kaAhaiBi  'man  ^frasta- raityS'Ü.  102;  103;  —  tadkrä  hruzbaray^n .  .  -ma  hl  sUrmaypn   Yt  S.  58;  V.  12.  2;
—  tä  (aimi. /ravasays)  el  starsta^  'möhu saoyä  Yt.  y.  a  7 ;  —  ys  'maca  ^frastfrinte gSulca  paitiiaraiti  ti.6o;6o;  —  %risum 'ma  frastjritmyA  paitila  hü  a^wansm  Yt. 12.  3;  —  ys  .  .  rapiUwiftfin  . .  fräyasäite
frashrttat  paiti  'nun  (Abi.)  uidOtät  paiti haomat  raecintäi  paiti  a'^rät  sravayamnät paiti  ahunai  vairyäl  A.4.  5;  Y.57.  i,  Yt JO.137,75. 2,V.9.56;— ÄflSn.eacär^m  haZa.- aiwyäahamm  imai  'ma  asaya  frastartttm Y.  71.  23;  2, 1,  4. 1,  6^2,  9,  Vr.  11.  2,  V.  _j. 15,  8.  14,  15,  Vyt  2^;  —  •manO  afaya frastantaheVr.iO.z; —  'manamca  asaya *frastir3tanqm  Vr.  12. 3;  —  ha^a  'mm (AbL)  frastairyat  V.^j.  16,  17,  16.  4,  17.  4;
—  hazatanm  /rast»r)ianqm  'maine  fra- stairyäi  Y.iS.'ja;  — yS  'man  *frasttr>nte haomqsca  var^Ssca  %anvasca  (sd.)  antar».- dSta  ..yS  ra'^Ssca  pasvanzdssca  *'mainc'> "hqm.varpntay^n/i  N.p7;  ■ —  tum  'ma  aya- jaa'fl., Yt./5.S5; — sadr^m  ahmai ..yahinät saota  anasava  ..  pasca  'ma  frakika  p?r3- nsmla  °ma  staranS  danypm^a  yasmm  ya- zans  ". .  ein  zu  volles  B. ''  spreitend  und  den
K  zu  sehr  in  die  Länge  ziehend"  Yt.  10. 138; —  binstm  baräi  saota  väam  hii'tpmnd pasca  'ma  YLJ7.  61;  —  yö  'ma  *aivah- mat  naimat  hamsrisäiti  hqm  va  dansa- yeili  N.  pp;  —  yat  patri  °ma  hanjasante N.  6"2;  —  tim  yazäi . .  haomayff  {sdi.)  gava 'mana  Ny.  /.  16;  —  aao'ira^  .  .  'ma'  äytse yesti  sao^ra  haoaJar^sma  .  .  'ma  hala.- saehra  äyese  yesti  akmya  sadhre  imai  '""^ .  .  ana  'mana  imqm  zaoirqm  .  .  ha%a.- zao^rfm  imai  '«"^  Syae  ydti  Y.  2.  i;  —
ahmya  saokre  'manas^a  (LS.  als  IS.)^* ahur?m  .  .  äyese  yesti  Y.  2.  2;  3ff.,  Vr.  2. iff.;  —  anahitai  pars  'mm  anahitayai pars  sao%rayäi  Ytio.  88;  —  yS  anyeke . .  'ma  */rastyrmti  (sd.)  frajasaiti  N. 104\  —  'mana  paiH.bfr>ta  .  .  hai/anSi/ .  .  :far»%»m  myasdim  ayese  yesti  Y.j,  i; 22. 1 ;  —  yB  paiti  ape  baraiti  nsit  'maine (DS.)  N.  6g;  6g,  V.  7.  77;  —  yeti  'ma antarat  naimai  .  .  (näml.  asti)  paiti *'manalHt<''>  [/a/ft']  barSit  N.6p;  — yS dim  */ra hinan  *antan  ätarpmla  'maca N.  68;  Yt  J2. 3  {'maia) ;  —  atrtmca  'mala taäaca  kaomala  havanaca  V,  5.  39;  14.8; —  hävanaHbya . .  taÜai . .  varpsäi . .  tavaca 'manS  Vr.  70,  2;  —  haomqsca  myaadqsia zao%rhca  'maca  . ,  gqmü  Y.4.1;  —  *Äava assma  hava  'mana  N.  108;  —  ha' ml  iara aSsmaca  'maca  N.  lo^;  lOj,  71T,  Y. 62, 9; — aat frabmtars  (näml.  lia/n'M  atahai) yai.. 'mqnca  fraksm  (sd.)  a%raeca  paiti.Öaräi N,  74;  —  yat  saota  ahurtm  mazdam  ya- zaiti  *mahmai  'man  (GS.)  paiH.bärHi  N. 70;  jo*^;  —  havanatm{^^)  daityS  gatui .  .  fratarqn  'mqn  (GS.)  aparqm  akrS  N. 79f  79t  —  y^  *""'  *taa/ayeiti  (sd.)  draitf wJ  . .  N.  100.
Undeutlich:  aUai  'ma  yaj  paiti  aptm  . . N.yo;  83,  V.ip.19; — 'manaVp.2j.  [N. gS:  streiche  -iwa.'»]
*>  Über  die  Pflanien,  von  denen  die  Zweige geschnitten  werden  dürfen,  bieten  die  älteren Texte  keine  genaueren  Mitteilungen;  N.  90 PüErl.  (Blatt  16/.  ig)  ist  nicht  recht  deutlich. In  Indien  braucht  man  jetzt  ans  Metall  herge- stellte Zweige.  Die  Mindestzahl  wird  N.  po  auf drei  angegeben;  Y.  57.  6  werden  die  Zahlen 3>  S>  7>  9  genannt.  Als  Höchstzahl  etscheint N.  90  PüErl.  (Blatt  t6S.  1)  551.  Für  gewöhn- lich schwankt  die  Zahl  zwischen  5  und  33,  der Zahl  dcT  ra/rij'ö f airi!,Aä-!i/iHayB  (sd.).  Ober  Grösse und  Stärke  der  Zweige  s.  Y.  J/.  6,  N.  yo,  po, V.  /p.  19.  Die  Zusammenfassung  der  Zweige  zu einem  Bündel  geschieht  mittelst  des  aiwyio- ^nna-'Cürter  (Sp.  98  m.),  wozu  man  heutzutage ein  Datlelblalt  verwendet.  Die  gebündelten Zweige  ruhen  auf  dem  Gerätetisch  (aräVoi^) vor  dem  ZaMar.  Weiteres  bei  Hauo  Essays» 396  f.,  West  SBE.  5.  »84,  '8.  142.  3y-  162. DsT.  ZA.  /.  LXJüiL  Der  Terra,  techn.  für  das Bündeln  des  B.%  ist  ^slar-  'stemere'.  Dies  sowie die  Etymologie  von  b'  weisen  darauf  bin,  das« der  Gebrauch  des  B.  sich  aus  dem  'Spreiten der  Opferstreu'  (ai.  barhifah  slärimä)  entwickelt hat;  %.  datn  OuiENSEiic  Rel.  des  Veda  343.
KompA.,    E.;    AbleiL    —    Aus    ir.   *iartm;
S  2*4;  'gl-  iar>al-.  —  Tä.:  barsm  (Traniskr.).
—  I»  D.h.  der  mehr  Zweige  dazu  verwendet.
dby  Google
bar^ziäta-
95°
als  f&r  den  betrelTenden  Fall  vorgeichriebcD ist;  •-•>.  —  »  Hds.-ma^ae.  —  3)  Them.  — 4)  Hds.  'macil;  vgl.  das  folgende;  faili  afaec^ barSil.  —  s)  An  letiter  Stelle  hds.  'mr.  —  6)  Als Glosse  zu  urvarqrn;  sd.  Sp.  403  U.
•  j.  bansmanay-  Adj.  (auch  fem.)  'zum Barnman  gehörig,  gebraucht  (usw.),  Bam- man°':  imqmca  urvarqm  'nJm  (ASf.)  Y. 22.3-  '    ,
AbleiL  aus    barisntan-;    vgl.  bar?smanya-  und
vor  %  igS-  —  V^:  I  iatsm. ■  j.  bar^smanya-  Adj.  (fem.  'yä-)  'zum Bansman  gehörig,  gebraucht  (usw.),  Bar»s- man'':  un>araku  paiti  °nyähu  mi^r^m  . . Syese  yeid  Y.  2.  1 1 ;  —  utrarä  paiti  *nyä mi%nm  yasamatde  Yt  10. 145.
Ableit.  aus  iarinnaH-;  vgl.  iarjimaitay-  und vor  S  'flS-  —  Pü.;  urvarän  1  barsm.
•  j.  bar«8mö.st9r«tay-  f.  'Spreituog von  Bargsman':  aivayacit  *alsm5.st»rnti alvayacii  •riiiti  (IS.)  P.  24;  N.  103.
Pü. ;  barsm  nistarHnTA.
•  j.  barasmö.zasta-  Adj.  (fem.  '/ä-) 'Barvsmanistengel)  in  der  Hand  habend, mit  B.  in  der  Hand'-,  yas^  Sics  . .  Jrä- yaxäile  . .  'iS  Y.  62.  i;  \.  3.1;  —  *yim aiwitö  mazdayama  histmta  'ta  Yt,  5.  98; —  'ta  (NSf.)  .  .  mittum  harat  .  .  ar^ävl sara  Yt5. 127.
Fü. :  barsiH  äasl.
•  j.  'bar»z-  V,,  nur  mit  us  'in  die  Höhe gehen,  aufwachsen'.  Praes.  30  (Kaus.) batvzaya-.
Kaus.  'aufwachsen   lassen':   kaimät  . .
frataintlm  us  apara  iatvxaymi  Ytio.  108.
ai.  iarAaya^tS.)  'i.uge';  atta.  Aamiar'na/ [Aar.
•batji)  'extDlIere,  elevate'.  —  Vgl.  'bam-  usw.,
•  j.  *bar»Z-  :  b»nz-^'>  i)  Adj.  'hoch,  er- haben': ratüm  Äj/vwm  Vr,  2.  10;  —  ratSuS hmlf{GS.)  Vt.i.%]  —  Hitrlm  . . yahmät haca  binzät^^  haosravanhtm  (sd.)  Vlä 4,  a)  von  Tönen  'hoch,  laut';  yas3  . . bsDBtn  barat  zaota  väHm  Yt.//.  61;  — yat  bsnism  barst  astra  ('die  Peitsche') vaHm  Yt. /o.  113.  2)  'Höhe;  Berg': haraiti  (sd.)  Äar/{NS.))>  Yt.ifj.  i;  —  upa upa.bdi  Aj«ya  (sd.)  i.wvÄ?(GS.)  Ytj?.  3, Jj.  24;  —  talrfincH  harai'hyä  btrpzö  Y. 42. 3;  —  lainm  harai^yä  barisö  (GS.) Ytr2. 15;  —  karai^yS  paiti  bar^zayä (GS.)*>  Y.io.  10,  57. 19,  Vt  10.  50,  90;  — vispkhu  paiti  öanzähu*''  Yt/o.4S.  [FrBy.: lies  °b?nts  als  Komp.]
KompA.  (s.  auch  btr^Bräi-),  E.  —  Zum  V. bam-.  —  np,  burs  "iioch;  Höhe',  bälä  'Höhe'; air.  ifj'Berg",  Km.  rrkna-bcrj  'himmelhoch' S. —  Pü.  (lu  1):  buland,  (lua):  burz.  —  0  Idg. *ihir^h- :  *blinA:  Eriteres  in  np.  bä!-ä  (,  tU. in  arm.  'b(r/]'>1,  letzteres  in  np.  bun  (,  gol. baurg-it,  air.  bri,  brtg).  —  »)  Them.  —  3)  Üg. *bAtrxt  oder*W/-ji  (=  ult. bri);  IF.p.aöi.— 4)  Nach  der  ä-Dekl.  —  s)  Richter  IF.9.  zso nimmt  fälschlich  ai.  ^AitspdliA  aU  (cig.J'Ber- gesherr';  s.  va  bing-.  —  6)  Anders  Hbm.  AGr. /.  4*8.
•  j.  bar^zan-  m.  'Höhe':  kukatrlm  (sd.) banzS . .  yahmat . .  haca  fi-azgmaite  andvl . .  AazavrHi  (statt  GS.)  'nsha  (IS.)  vTranqm YL5.  g6";  —  xiva/paya  (sd.)  vaOtaya 'nSna  Y.  5. 1 1  PüZ.,  Yt  ig.  40.
KompE.  —  Zum  V.  bariz-;  vgl.  bariiiman- und  Bthl.  IF.  7.  59.  —  0  Vgl.  Bd.  12.  6: hukar  i  buland  an  it  äf  i  ardvisür  ha?  ai  frei äyet  1000  mart  bälät.
•  j.  barszah-  n.  'Höhe,  Berg':  *upa *tnaitlm  (sd.)  'zargAam  V.J.  30;  —  mihnm .  .  yS  vlsp)m  aham  .  .  Sdt6aili  haratkyät (sd.)  paiti  'zatakat  Yt  jo.  5 1 ;  —  barniste paiti  'zaÄi  haraihyS  .  .  Y.  ^y.  19;  — AuiaitJm  (sd,)  °zS  Ytj.  96,  12.  24;  —  ya (näml.  arfdvt)  .  .fratacaiti  hukairyät  haca 'zaftkat  Y.  65.  3 ;  Yt  5.  2  5.
KompE.  — ■  Zum  V.  barix-,  vgl.  'banx:  — Fü. :  buland,  (zu  V.):  pa  bälisl,  erl.  ifatari  kif.
•  g.,  j.  baraziman- Adj. 'hoch':  imä  raeüa bartziit^m  •zimanqm  avat  (sd.)  yai  hvarJ avaaY.36.6i  —  Avan  bar7zisi?m  'zima- nqm Vr.  IQ,  2.
'Zum  V.  tarn-.  —  VgL  barizan-  and  Bthl. IF.  p  65.  —  Ptt.  (dRn.);  bäUitä»  bälist,  bälist Aac  bäliilän,
•  j.  bar9zi§-  n.  'Polster,  Kissen':  >?  narS hämS^ätvü  nipaüyeinte  Aqm  vä  paiti  stairis Aqm  vä  paiti  '«/V.J.  27;  —  cvat  alte slairisca  °tisca  aesa  druxs  .  .  fräshaoiti V.  7-9;  —  aitaoa  altahe  aste  (Sp.  340) slairii^a  °zi/^a  hqm.v^rtnattte  V.j.  59;  — ana  'zis  sayamnanqm  (sd.)  V.  lü.  26;  — gätu  *x''aiiii.star»tu  (sd.)  mai  °ziia  V. 7^14.         [Yt5.  loa:  lies  bar^zi/Aav'.]
KompE.;  Ableit.  —  ai.  barAif^n.  'Opferstren', np.  bälis  'Kissen';  vgl.  ai.  ufabärAaria-  n. 'l'olster'.  —  Pü.:  bälisn.
•  ].,  g.  baraziäta-  Adj.  'der  höchste,  hüchst- gelegene':  'te paiti  bantaAi  Aaraiiyg paiti bansayä  Y.  57.  19;  —  'taiibyS  gairibyö V. 2. 22;  —  'laihiaia  paiti  gätuha  V, 6^.45;  —  urvaranqm  .  ■  ysi  hftiii ..  'taca V.  2.  28; —  imä  raoiä  't?m  bar»zimanqm
dby  Google
951
^barfzi&havant-
I
V.^.6;  Yi.ig.2.         a)  'sehr  ticT:   -U
=== search barzant/hoch ===
16999:bar^ziäta-
17015:•  j.  *bar»Z-  :  b»nz-^'>  i)  Adj.  'hoch,  er- haben': ratüm  Äj/vwm  Vr,  2.  10;  —  ratSuS hmlf{GS.)  Vt.i.%]  —  Hitrlm  . . yahmät haca  binzät^^  haosravanhtm  (sd.)  Vlä 4,  a)  von  Tönen  'hoch,  laut';  yas3  . . bsDBtn  barat  zaota  väHm  Yt.//.  61;  — yat  bsnism  barst  astra  ('die  Peitsche') vaHm  Yt. /o.  113.  2)  'Höhe;  Berg': haraiti  (sd.)  Äar/{NS.))>  Yt.ifj.  i;  —  upa upa.bdi  Aj«ya  (sd.)  i.wvÄ?(GS.)  Ytj?.  3, Jj.  24;  —  talrfincH  harai'hyä  btrpzö  Y. 42. 3;  —  lainm  harai^yä  barisö  (GS.) Ytr2. 15;  —  karai^yS  paiti  bar^zayä (GS.)*>  Y.io.  10,  57. 19,  Vt  10.  50,  90;  — vispkhu  paiti  öanzähu*''  Yt/o.4S.  [FrBy.: lies  °b?nts  als  Komp.]
17017:•  j.  bar^zan-  m.  'Höhe':  kukatrlm  (sd.) banzS . .  yahmat . .  haca  fi-azgmaite  andvl . .  AazavrHi  (statt  GS.)  'nsha  (IS.)  vTranqm YL5.  g6";  —  xiva/paya  (sd.)  vaOtaya 'nSna  Y.  5. 1 1  PüZ.,  Yt  ig.  40.
17023:•  j.  bar9zi§-  n.  'Polster,  Kissen':  >?  narS hämS^ätvü  nipaüyeinte  Aqm  vä  paiti  stairis Aqm  vä  paiti  '«/V.J.  27;  —  cvat  alte slairisca  °tisca  aesa  druxs  .  .  fräshaoiti V.  7-9;  —  aitaoa  altahe  aste  (Sp.  340) slairii^a  °zi/^a  hqm.v^rtnattte  V.j.  59;  — ana  'zis  sayamnanqm  (sd.)  V.  lü.  26;  — gätu  *x''aiiii.star»tu  (sd.)  mai  °ziia  V. 7^14.         [Yt5.  loa:  lies  bar^zi/Aav'.]
17228:•  j.  bar^zy-arStay-  m.  EN.  eines  Gläu- bigen: H5ti  aiaonS  Yt  y.  loi.
20833:—  AblSm.,!!,:  vazrpm..yaAmat  /laca/ra- tpnsaili  ar»rS  mainyul  Yt  10.  97;  97J,  7  y. 87,  Aog.  5<¥;  —  hukairjm  bar>zB  yahmat ml  hala  frazgahaife  ar)dvj  Ytf,  96;  — tistrlm  .  .  *yahmat  haca  b}r»zat  haosra- var?h3m  Ytty.4;  —  GSm.,  n.:  mt^nm  .. yeAhe  zim.frdis  maihanim  vllät^m  .  . yeiihe  asia  rätayä . . spasS  at^häire  Yt  70. 44f.;  60,  68,  69,  70,  82,  85,  104,  143, 5.30,  7J.  81,  93\  107,  V. /;.  13J,  Kj. 44;  —  sraosfm  .  .  yeti/ie  ahiinS  vairyB snaihi/  visata  Y.  ^y.  32;  ai,  23;  — yän^m  vO  yäsämi  . .  yeAhe  däiti  paiti vaahs  nisrJta    anaiwi-druxti  (sd.)   Y.  6j.
```


## [2026-09-05T06:22:12.165Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT barsnu ===\"; grep -n -E \"bar.{0,2}šnu|barsnu|barešnu|barasnu|Scheitel\" BRT.txt | head -10\necho \"=== PHD barsom/balisn/balen ===\"; grep -n -i -E \"barsom|bars(u|o)m|bāliš|balisn|bālēn|balen|bāl\\(\" PHD.txt PHD_mackenzie.txt | head -30\necho \"=== HRN balis ===\"; grep -n -i -E \"bāli[sš]|balis|bālīn|balin\" HRN.txt | head -20\necho \"=== HUB ===\"; grep -n -i -E \"bāli|balis|barsom|barsam\" HUB.txt | head -20",
 "description": "MacKenzie, Horn, Hübschmann lookups"
}
```


### [2026-09-05T06:22:14.092Z] TOOL RESULT

```
=== BRT barsnu ===
=== PHD barsom/balisn/balen ===
PHD.txt:226:azbüy- 16 bālēn
PHD.txt:244:ībālēn [P'lyn!] top, peak.
PHD.txt:245:*bālēn [5!Iyn! | N Баби) cushion, pillow.
PHD.txt:249:bāliš [P'Ifn! ! | N ~] cushion, pillow.
PHD.txt:252:bāmdād [6’md’t' | М bmd?d, N ~] dawn, morning. bāmīģ [P myk!] brilliant, glorious. -bān [-??s! | M Aa, N ~] suffix, -keeper, -guard. band [bnd | = Р, N ~] bond, link. band-, v. bastan. bandag [bndk! | P bndg, N ~a] servant. bang [bng | N ~] henbane. bānūg [Pnwk! | N Бапи) lady. bar [b] | N ~] fruit, produce, profit. bar-, —išn, v. burdan. ībār [Pl | N ~] time, occasion. *bār [P1 | N ~] bank, shore. заг [D] | M P?r, N ~] fruit. ‘bar [b] | M br, N ~] load, burden; duty. bāraģ [5/А! | N ~a] mount, horse. barbut [blbwt! | N ~] lyre. bārestān [b/st?n'] patient, resigned. ~ih: patience, resignation. barig/k [b’lyk' | N bārīk (cf. tārīg)) thin, fine, subtle. bar-jamag [bly mk! | N ~a] saddle-bag. barómand [b wmnd | N ~] fruitful, prolific. barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere- mony. baršnūm [b/s2wm] the major purification ritual. bastan, band- [ASLWN-tn! < A Vier bstn', bnd- | M bstn, (bn-), P bnd-, N ~] tie, bind. bāstān [b’st?n' | M PysPn, N ~] always, often. bas [YHWWNS | M P, N ~] be! (imperative of büdan, q.v.) baSkué [bskwe] gryphon. bašn [bén' | = P] top, peak; stature; mane (v. buš). baw-, —i$n, v. büdan. baxš-, —išn, v. baxtan. baxt [b()At! | N ~] fortune, fate. baxtan, baxš- [HLKWN-tn! < А У hig; bC)htn', bhf- | M bxt, bx$-, N baxsidan] apportion, distribute. ~išn: bestowal, distribution. bay [ORHY A < A */h; bk', bg | M by] god, lord. im ~: his Majesty. бу ~: his late Majesty. bayaspān [by’sp’n'] messenger, envoy.
PHD.txt:978:bench bālēngāh.
PHD.txt:3128:pillow balén, bāliš.
PHD.txt:3694:sleep (n.) xwàb, xwamn; büšasp. sleep (v.) xuftan, nibastan, sleeping-platform bālēngāh. sleepless axwamn.
PHD.txt:4032:top bālēn, bašn, sar; v. summit.
PHD_mackenzie.txt:1472:lIbalen [b)lyn l I N biilin] cushion, pillow.
PHD_mackenzie.txt:1507:barsom [blswm I M brswm] the bunch of twigs used in the Yasna cere-
PHD_mackenzie.txt:6039:bed gah, balengah.                          biting (n.) gazisn.
PHD_mackenzie.txt:6063:bench balengah.                             blossom (n.) skofag, wiskOfag.
PHD_mackenzie.txt:6276:contained, be ....., in andar budan.         couch balengah, taxtgah.
PHD_mackenzie.txt:6339: cushion balen. balis.                     deceiver dabr; freftiir.
PHD_mackenzie.txt:7223:owl bUf/g.                             peak balen, basn, cagad, terag.
PHD_mackenzie.txt:7286:pillow balen, balis.                       pond sadurwan.
PHD_mackenzie.txt:11259:balengah              ~~\                 adur                      \\,~
PHD_mackenzie.txt:11261:1-2balen
=== HRN balis ===
=== HUB ===
4612:ap. ^bardah" = zd. barezah^^) *H5he', phi. sup. balist, zd.
4615:balis *Kissen, phi. balisn Gl. and Ind. 76, zd. barezis; phi.
5649:Abalish I, 3 u. s. w.), nirgends mit v^), so dass die Gleichung
5660:64, 8 ; Spiegel, trad. Litt. p. 389 ; Barthelemy, Gujastak Abalish
6167:= zd. baresma (np. barsam ist Parsenwort); hezum 'Brennholz
6376:H. 167; bak Turcht H, 170; baU *hoch* H. 171; balis
6382:H. 198; barsam (Parsenwort) H. 200; biristan *braten' H
8456:Shk. 257 = np. mahist (siehe oben) = ap. madista- ; balist
9311:phi. sup. balist := zd. barezista-; phi. sup. x^alist am
9313:'schmecken' H. 500; balis 'Kissen', zd. barezis-; phi. baltn
```


## [2026-09-05T06:22:24.603Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB context 4605-4620 ===\"; sed -n '4605,4620p' HUB.txt\necho \"=== HUB context 6160,6175 ===\"; sed -n '6160,6175p' HUB.txt\necho \"=== HUB context 9305,9320 ===\"; sed -n '9305,9320p' HUB.txt\necho \"=== HUB 6370,6385 ===\"; sed -n '6370,6385p' HUB.txt",
 "description": "Hübschmann context"
}
```


### [2026-09-05T06:22:24.668Z] TOOL RESULT

```
=== HUB context 4605-4620 ===
navasard etc.), fiir das im urspriinglichen Pehlevi das semi-
tische snat geschrieben wird, zd. eared a-; salar *Anfiihrer
= paz. salar ^ arm. salar (5. Jhd.), phi. sardar; batidan
'wachsen, phi. caus. voUnltan, zd. tared mod. Vachsen,
caus. vareday mehren"; guvaltdan (unbelegt) Vachsen*, zd.
vl^vared ; pal&: *Garten , arm. partSz, hebr. pardBs, zd. pairi-
da^za-; bola 'RQhe, ohen (hal.LW. balOi'RlShe*) aus *6arrf^,
ap. ^bardah" = zd. barezah^^) *H5he', phi. sup. balist, zd.
bareziSta- *h5chst*; phi. sup. a;^flto-) *am schmackhaftesten*,
zd. x^areziSta-, vgl. np. x^aUdan schmecken' (Horn Nr.500)?;
balis *Kissen, phi. balisn Gl. and Ind. 76, zd. barezis; phi.
balln *a summit, the crown of the head* Gl. and Ind. 76,
zd. baresnu- *H5he, Gipfel' (aus *6ar2?«w-, vgl. zd. bqSnu-
*Tiefe* zu bqjsah-); mOlfdan reiben', phi. -^tnarz, zd. marez-;
Mia *Hagel, Reif* aus *iardak (vgl. Horn Nr. 684)?, nol
*Rohr , skr. nada- *Schilfrohr , gr. vdgdog ? ; naltdan *klagen',
=== HUB context 6160,6175 ===
einherschreiten' aus *viraz — skr. vraj zu stammen.
B. Vokaleinschab im Inlant
fand statt zur Vermeidung iiberlanger Silben (auf kurzen
Vokal + drei Eonsonanten oder langen Vokal + zwei
Konsonanten, wenn der letzte Konsonant ein Nasal oder
eine Liquida ist) und zwar ist
§ 64. a) u eingeschoben in : phi. paz. barsum aus *barsm
= zd. baresma (np. barsam ist Parsenwort); hezum 'Brennholz
aus *ezm = ap. *aizma- = zd. a^sma- ; ustur 'Kameel' aus
*) Schon bei Ptolem. liandSarcc^ das trotzdem zu zd. &p. spaSa-
*Heer* gehoren wird.
*) Der Vorsohlag von a vor sx aus X8 (z, B. asx^ *roth' = zd.
xsapta-'y asxarh 'Land' = ap. xsa^^'a-) ist; armenisoh.- 175 -
^tistr = zd. ustra- ; vielleicht auch in abr^um *Seide* = phi.
*apr^utn (s. oben p. 12). Dieser Einschub fand also schon
im Phi. statt.
=== HUB context 9305,9320 ===
§ 157. Ap. rd (= idg. rd, rdh, rg^, rg^h) = np. I:
sal 'Jahr' = arm. sard (in navasard etc.); salar *Anfuhrer,
arm. salar (5. Jhd.) = phi. sardar; balldan 'wachsen', zd.
vared; guvCLlldan Vachsen , zd. m-vared; pflfe^r /Garten',
hebr. pardss, zd. pairida^&a- ; bala *H6he, oben', ap. Hardah-
= zd. barezah- ; buland 'hoch' == ap. *brdanUy zd. berezant- ;
phi. sup. balist := zd. barezista-; phi. sup. x^alist am
schmackhaftesten' = zd. x^arezista- ^ vgl. np. x^alfdan
'schmecken' H. 500; balis 'Kissen', zd. barezis-; phi. baltn
*a summit', zd. bareSnu- (aus ^barz-nu-); mdlldan reiben\
phi. -marz, zd. marez; iola 'Hagel, Reif* aus *kirdak H. 684;
naVRohr, skr. nada-, gr. vdg^og?; Mtlad aus MihlG>d{i^. 189) =
Mihrdat; paz. kala 'verriickt', zd. hareii- (8iehe^§ 9, a); gul
*Rose' aus *!?rd-, vgl. arab. arm. vard; mul 'Wain', skr.
mrdtHka- *Weintraube'; palang 'Leopard*, afgh. pr(ing,[8kv,
prdaku", gr. ndpduhg; dil *Herz* = zd. zered-^ skr. Ard-;
=== HUB 6370,6385 ===
vermuthet und halte es — wie jetzt auch andere Gelehrte
— fiir sicher. Vgl. die Einleitung p. 115.
Ap. 6, w (= idg. hh) wird im Np. zu 6, v und /.
§ 74. a) Ap. h im Anlaut = np. 6:
haj 'Tribut', ap. haji-, skr. Wrzl. hhaj\ bar Last' H.
156; bara 'Pferd' H. 160; bOzYsXkQ, arm. ia-se; bCLzu'kvm
H. 167; bak Turcht H, 170; baU *hoch* H. 171; balis
'Kissen H. 172; bam *Morgen H. 174; bam, ban *Dach,
Haus' oben p. 24; banu *Herrin (?) H. 178; but Idol' s. oben
p. 26; biziSk *Arzt' H. 183; baxt ^Schicksal' H. 185; baxsi-
dan *schenken H. 186; biradar *Bruder H. 192; baraz
Schmuck' H. 193; burdan H. 196; burz *hoch*, buland 'hoch
H. 198; barsam (Parsenwort) H. 200; biristan *braten' H
201; burrfdan *schneiden H. 212; buz 'Ziege, Bock* H. 213
bazm Test' H. 215; baza *Siinde' H. 216; bastan 'binden
band *Band* H. 219; bus 'Mahne H. 220; bun 'Fundament
```


## [2026-09-05T06:22:26.423Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS balisn ===\"; grep -n -i -E \"bali[sš]|bālis|barsom|barsum|balen\" SNS_pages.txt | head -20\necho \"=== SNS pdf page tags near ===\"; grep -n \"pdf page\" SNS_pages.txt | head -5",
 "description": "SNS lookups"
}
```


### [2026-09-05T06:22:26.490Z] TOOL RESULT

```
=== SNS balisn ===
4709:v-.yi^ijljj ** */^ ^jU5U*>-Li « jm*                         :barsam/barsum:                         -6**i>
4719: .(*j*y**)                  barsum      :^                                                  :                                    :
4725:l^t^Vrfc-l^H^.^U-^; barsum-dan:                                                         *^*S!2>                         >J/itic
4728:                 .   •Aii t-r*.ii- f-*s      barsum I apadyab: e^o *****«.£*                             »
4733:e-ij.^-^             U^b *^** f-.*: barsum I 7 tag:                       J-^^___^»--x^» '(
16391:barsum dan 103/7         besaz 112/4                     bristag 103/16
16392:barsum I apadyab 103/9   belazlh 112/7                   bud 106/16-303/8         cabuktar 156/9
16393:barsum I 7 tag 103/11    belazisn 112/9                  budan 107/8-303/4        cah 155/4
=== SNS pdf page tags near ===
```


## [2026-09-05T06:22:45.201Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS around balisn ===\"; grep -n -i -E \"bali[sš]n|balisn|balen|balin\" SNS.txt SNS_pages.txt | head -20\necho \"=== SNS index page 98 ===\"; grep -n -E \"9[0-9]/[0-9]\" SNS_pages.txt | grep -i -E \"bal\" | head -20",
 "description": "SNS balisn lookup"
}
```


### [2026-09-05T06:22:45.260Z] TOOL RESULT

```
=== SNS around balisn ===
=== SNS index page 98 ===
```


## [2026-09-05T06:22:46.011Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD bhel ===\"; grep -n -E \"^bhel|bhel-|bhelgh|bhleu|bhlei\" AHD_watkins1985.txt | head -30",
 "description": "AHD Watkins bhel roots"
}
```


### [2026-09-05T06:22:46.061Z] TOOL RESULT

```
=== AHD bhel ===
326:bhel-?
328:bheidh-. To persuade, compel, confide. 1. Probably Ger- manic *bidan, to await (< “to await trustingly, expect, trust”), in Old English bidan, to wait, stay: BIDE; ABIDE, (ABODE). 2. Latin fidere, to trust, confide, and fidus, faithful: FIANCE, FIDUCIAL, (FIDUCIARY); AFFIANCE, (AFFIANT), (AFFIDAVIT), (CONFIDANT), CONFIDE, (CONFI- DENT), (DEFIANCE), DEFY, DIFFIDENT. 3. Suffixed o-grade form *bhoidh-es- in Latin foedus (stem foeder-), treaty, league: FEDERAL, FEDERATE; CONFEDERATE. 4. Zero-grade form *bhidh- in Latin fidés, faith, trust: FAITH, FEALTY, FIDELITY; INFIDEL, PERFIDY. [Pok. bheidh- 117.] bheig-. To shine. An uncertain but plausible root. Greek phoibos, shining: PHOEBE, PHOEBUS. [Pok. bheigz- 118.] bhel-'. To shine, flash, burn; shining white and various bright colors. I. 1. Russian byelii, white: BELUGA. 2. Greek phalaros, having a white spot (> phalaris, coot): PHALAROPE. II. 1. Suffixed variant form *bhié-wo- in Germanic *bléwaz, blue, in Old French bleu: BLUE. 2. Suffixed zero-grade form *bhb-wo- in Latin flavus, golden or reddish yellow: FLAVESCENT, FLAVO-; (FLAVIN), (FLAVONE), (FLAVOPROTEIN). III. Various ex- tended Germanic forms. 1. *blaikjan, to make white, in Old English blécan, to bleach: BLEACH. 2. *blaikaz, shining, white, in: a. Old Norse bleikr, shining, white: BLEAK}; b. Old English biéc, bright: BLEAK?. 3. Ger- manic *blikkatjan in Old High German blécchazzen, to flash, lighten (> German Blitz, lightning): BLITZKRIEG. 4. *blas-, shining, white, in: a. Old English blxse, torch, bright fire: BLAZE!; b. Middle Dutch bles, white spot: BLESBOK; C. Old French ble(s)mir, to make pale: BLEM- Ish. 5. *blend-, *bland-, to shine, dazzle, blind, confuse, in: a. Old English blind, blind: BLIND; (BLINDFOLD), (PURBLIND); b. Old High German blentan, to blind, deceive: BLENDE; Gc. Old English blandan, to mingle: BLEND; d. Old French blond; blond: BLOND. 6. *blenk-, *blank-, to shine, dazzle, blind, in: a. Old English blen- can, to deceive: BLENCH!; b. Old French blanc, white: BLANCH, BLANK, BLANKET; BLANCMANGE. 7. *blisk-, to shine, burn, in Old English blyscan, to glow red: BLUSH. IV. Extended form *bhleg-, to shine, flash, burn. 1. Ger- manic *blakaz, burned, in Old English blxc, black: BLACK. 2. Zero-grade form *bhig- in: a. Latin fulgére, to flash, shine: FULGENT, FULGURATE; EFFULGENT, FOU- DROYANT, REFULGENT; b. Latin fulmen (< “fulg-men), lightning, thunderbolt: FULMINATE. 3. a. Latin flagrdre, to blaze: FLAGRANT; CONFLAGRANT, CONFLAGRATION, DEFLAGRATE; b. Latin flamma (< *flag-ma), a flame: FLAMBE, FLAMBEAU, FLAMBOYANT, FLAME, FLAMINGO, FLAMMABLE; INFLAME. 4. Greek phiegein, to burn: PHLEGM, PHLEGMATIC, PHLEGETHON. 5. Greek phlox, a flame, also a wallflower: PHLOGISTON, PHLOX; PHLOGO- PITE. [Pok. 1. bhel- 118, bheleg- 124, bhleu-(k)- 159.] bhel-2. To blow, swell; with derivatives referring to various round objects and to the notion of tumescent masculinity. 1. Zero-grade form *bhl- in Germanic *bul- in: a. Old English bolla (> Middle English boll), pot, bowl: BOLL, BOWL!; b. Old Norse bolr, tree trunk: BOLE}; c. Old Norse bulki, cargo (< “rolled-up load”): BULK}; d. Old High German bolla, ball: ROCAMBOLE; e. Middle High German bole, beam, plank: (BOULEVARD), BUL- WARK; f. Middle Dutch bolle, round object: BOLL; g. Middle Dutch bille, buttock: BILTONG; h. Swedish *buller-, “round object,” in bullersten, “rounded stone,” boulder, akin to the Scandinavian source of English BOULDER; i. possibly obsolete Swedish bulde, a swelling (see wer-1). 2. Suffixed zero-grade form *bhl-n- in: a. Germanic *bulJ6n-, bull, in Old Norse boli, bull: BULL); b. Greek phallos, phallus: PHALLUS; ITHYPHALLIC.
329:bhel-*
330:3. O-grade form *bhol- in Germanic *ball- in: a. Old English beallucas, testicles: BOLLIX; b. Old Norse bdllr, ball: BALL; c. Danish bolle, round roll, akin to the probable Scandinavian source of BILBERRY; d. Middle High German baile (> Italian balla, palla), ball: BAL- LOON, BALLOT; PALL-MALL; e. French baile, ball: BAL- LOTTEMENT; f. Old French baie, rolled-up bundle: BALE!. 4. Suffixed o-grade form *bhol-to- possibly in Germanic *balthaz, bold, in: a. Old English bald, beald, bold: BOLD; b. Old High German bald, bold: BAWD. 5. Suffixed o-grade form *bhol-n- in Latin follis, bellows, inflated ball: FOLLICLE, FOOL!; (FOLLICULITIS). 6. Possibly Greek phalaina, whale: BALEEN. 7. Conceivably (but more likely unrelated) Greek phellos, cork, cork oak: PHEL- LEM; PHELLODERM, PHELLOGEN. (The following deriva- tives of this root are entered separately: bhel-?, bhelgh-, bhlei-, bhleu-.) [Pok. 3. bhel- 120.} bhel-3, To thrive, bloom. Possibly from bhel-?. I. Suffixed o-grade form *bhol-yo-, leaf. 1. Latin folium, leaf: ForL?, FOLIAGE, FOLIO, FOLIUM; CINQUEFOIL, DEFOLIATE, EX- FOLIATE, FEUILLETON, FOLICOLOUS, MILFOIL, PORTFO- LIO, TREFOIL. 2. Greek phullon, leaf: (-PHYLL), PHYLLO-, -PHYLLOUS; GILLYFLOWER, PODOPHYLLIN. II. Extended form *bhlé- (< *bhlea-). 1. O-grade form *bhl6- in: a. suffixed form *bhlé-w- in Germanic *bl6-w- in Old English bléwan, to flower: BLOWS; b. Germanic suffixed form *bl6-m6n- in (i) Old Norse blém, blémi, flower, blossom: BLOOM! (ii) Old English bléma, a hammered ingot of iron (semantic development obscure): BLOOM?; c. Germanic suffixed form *bl6-s- in Old English bléstm, bléstma, flower, blossom: BLOssoM; d. Latin flés (stem flor-), flower: FERRET?, (FLORA), FLORA, (FLORAL), FLOR- IATED, FLORID, FLORIN, FLORIST, -FLOROUS, FLOSCULUS, FLOUR, FLOURISH, FLOWER; CAULIFLOWER, DEFLOWER, EFFLORESCE, ENFLEURAGE, FLORIGEN. 2. Germanic suf- fixed form *blé-do- in Medieval Latin bladium, produce of the land: EMBLEMENTS. 3. Suffixed zero-grade form *bhib-to- in Germanic *bladaz in Old English bled, leaf, blade: BLADE. [Pok. 4. bhel- 122.] bhel-4. To cry out, yell. Germanic *bell- in: a. Old English bellan, to bellow, bark, roar: BELL?; b. Old English belle, a bell: BELL!; c, Old English belgan, bylgan, to become enraged: BELLOW; d. perhaps Old English bealcan, *b(iJelcan, to utter, belch forth: BELCH; e. Middle High German buldern, boldern, to make noise: POLTERGEIST; f. Icelandic baula, to low, akin to the Scandinavian source of Middle English baulen, to howl: BAWL. [Pok. 6. bhel- 123.] bheld-. To knock, strike. Zero-grade form *bhid- in Germanic *bult-, missile, in Old English bolt, heavy arrow, bolt: BouT!. [Pok. bheld- 124.] bhelg-. Also bhelk-. A plank, beam. 1. Germanic *balku- in Old English balc(a), ridge: BALK. 2. Germanic *balk6n- in: a. Old French bauch, beam: DEBAUCH; b. Old Italian balcone, scaffold: BALCONY. 3. Suffixed zero-grade form *bhik-yo- in Latin fulcire, to prop up, support: FULCRUM. 4. Possibly Greek phalanx, beam, finger bone, line of battle: PHALANGE, PHALANX. [Pok. 5. bhel- 123.] bhelgh-. To swell. Extension of bhel-2. 1. Germanic *balgiz in Old English bel(ijg, belig, purse, bellows: BELLOWS, BELLY. 2. Germanic *bulgjan in Old Norse bylgja, a wave: BILLOW. 3. Germanic *bolgstraz in Old English bolster, cushion: BOLSTER. 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.) bhelu-. To harm. Germanic *balwaz in Old English bealo, b(e)alu, harm, ruin, bale: BALE?. [Pok. bheleu- 125.] bhendh-. To bind. 1. Germanic *bindan in Old English bindan, to bind: BIND; WOODBINE. 2. O-grade form *bhondh- in Germanic *band- in: a. Old English bend, band, ribbon, akin to the Germanic source of Old French bende, band: BEND?; b. Old English bendan, to bend: BEND!; c. Old Norse band, band, fetter: BAND!, BOND; d. Old French bande, bond, tie, link: BAND!. 3. Zero-
342:flagitdre, to demand importunately: FLacitious. [Pok. bhlag- 154.] bhlagh-men-. Form, ritual form. Sanskrit brahmd, brah- man-, priest, and brahma, bréhman-, prayer: BRAHMA!, BRAHMAN, (BRAHMIN). [Pok. bhlagh-men- 154.] bhlé-1. To howl. Probably imitative. 1. Germanic suffixed form *blé-t- in Old English b/gtan, to bleat: BLEAT. 2. Germanic suffixed form *b/é-r- in Middle English bleren, to roar: BLARE. 3. Latin flére, to weep: FEEBLE. [Pok. bAlé- 154.] bhié-2, Also bhla-. To blow. 1. Germanic suffixed form *blé-w- in Old English blawan, to blow: BLow!. 2. Ger- manic suffixed form *blé-dram, “something blown up,” in: a. Old English blZdre, blister, bladder: BLADDER; b. Old Norse bladhra (noun), bladder, and bladhra (verb), to prattle: BLATHER. 3. Germanic extended form *blés- in: a. Old English b/ést, a blowing, blast: BLAST; b. Middle Dutch blas(e), a bladder: stncLass. 4. Variant form *bhid- in Latin flare, to blow (> flabellum, fan): FLABELLUM, FLATUS, FLAVOR; AFFLATUS, CONFLATE, (DEFLATE), INFLATE, SOUFFLE. [In Pok. 3. bhel- 120.] bhlei-. To blow, swell. Extension of bhel-2. 1. Germanic *blajjinén-, a swelling, in Old English blegen, a boil, blister: BLAIN. 2. Perhaps in the Germanic source of Old French blestre, a blister: BLISTER. [Pok. 2. bhiei- 156.] bhleu-. To swell, well up, overflow. Extension of bhel-?. 1. Possibly Germanic *b/aut- in Old Norse blautr, soft, wet: BLOAT. 2. Extended form bhleug~- in Latin fluere, to flow, and -fluus, flowing: FLUCTUATE, FLUENT, FLUERIC, FLUID, FLUME, FLUOR, (FLUORO-), (FLUSH2), FLUVIAL, FLUX; AFFLUENT, CONFLUENT, EFFLUENT, (EFFLUVIUM), (EFFLUX), (FLUORIDE), FLUVIOMARINE, INFLUENCE, (IN- FLUENZA), MELLIFLUOUS, REFLUX, SUPERFLUOUS. 3. Zero-grade form *bhlu- in Greek phluein, phluzein, to boil over: PHLYCTENA. 4. Possibly Greek phloos, phioios, tree bark (< “swelling with growth”): PHLOEM. [Pok. bhileu- 158.] bhlig-. To strike. Latin fligere, to strike: AFFLICT, CON- FLICT, INFLICT, PROFLIGATE. [Pok. bhlig- 160.] bhoso-. Naked. Germanic *bazaz in: a. Old English bzr, bare: BARE!; b. Old Swedish and Old Danish bar, bare: BALLAST. [Pok. bhoso-s 163.] bhrag-. To smell. 1. Germanic *brak- in Old High Ger- man bracc(h)o, dog that hunts game by scent: BRACH. 2. Suffixed form *bhrag-ro- in Latin fragrdre, to smell: FLAIR, FRAGRANT. [Pok. bhrag- 163.] bhrater-. Brother, male agnate. 1. Germanic *brdthar- in Old English bréthor, brother: BROTHER. 2. Latin frdter, brother: FRA, FRATERNAL, FRIAR; CONFRERE, FRATRI- CIDE. 3. Greek phratér, fellow member of a clan: PHRATRY. 4, Sanskrit bhratd, bhrdatar-, brother: PAL. [Pok. bhrdater- 163.] bhreg-. To break. 1. Germanic *brekan in: a. Old English brecan, to break: BREAK; b. Old English bréc, a break- ing: BREACH; c. Old High German brehhan, to break, akin to the Germanic source of Italian breccia, breccia: BRECCIA; d. Old French breier, to break: BRAY?; e. Old French brier (dialectal) and broyer, to knead: BRIOCHE. 2. Germanic *brak-, bushes (< “that which impedes motion”), in Old Norse *brakni, undergrowth, akin to the probable Scandinavian source of Middle English brake(n), bracken: BRACKEN, BRAKE’, BRAKE‘, 3. Nasal- ized zero-grade form *bhr-n-g- in Latin frangere, to break: (FRACTED), FRACTION, (FRACTIOUS), FRACTURE, FRAGILE, FRAGMENT, FRAIL!, FRANGIBLE; ANFRACTU- OUS, CHAMFER, DIFFRACTION, (INFRACT), INFRANGIBLE, INFRINGE, OSSIFRAGE, REFRACT, (REFRAIN?), (REFRIN- GENT), SAXIFRAGE, SEPTIFRAGAL. 4, Latin suffrdgdri, to vote for (? < “to use a broken piece of tile as a ballot”), hence suffrdgium, the right to vote: SUFFRAGAN, SUF- FRAGE. [Pok. 1. bhreg- 165.] bhréi-. Also bhri-. To cut, break. 1. Possibly Latin fricdre (> French frotier), to rub: FRAY?, FRICATIVE, FRICTION, FROTTAGE; AFFRICATE, DENTIFRICE. 2. Possi-
794:obhel-. Also abhel-. To augment, increase. Greek ophe- los, advantage: ANOPHELES. [Pok. obhel- 772.]
1144:*wn-to- in Germanic *wundaz in Old English wund, a wound: WOUND!. 2. Suffixed o-grade form *won-yo- in Germanic *wanja-, a swelling, in Old English wen(n), wen{n), wen: WENI. [In Pok. 1. ué- 1108.] wendh-. To turn, wind, weave. 1. Germanic *windan, to wind, in: a. Old English windan, to wind: WIND2; b. Old Norse vinda, to wind: WINDLASS. 2. Germanic causative *wandjan in: a. Old English wendan, to turn to: WEND; b. Dutch wenden, to turn: WENTLETRAP. 3. Germanic *wandr6n, to roam about, in: a. Old English wandrian, to wander: WANDER; b. German wandern, to wander: WANDERLUST. 4. Germanic *wanduz in Old Norse véndr, a supple twig: WAND. 5. Germanic *wandljaz, “wan- derer,” perhaps in Latin Vandalus, a Vandal: VANDAL. [Pok. 1. uwendh- 1148.] weng-. To bend, curve. 1. Germanic *wink- in Old Eng- lish wincian, to close the eyes (< “to bend down the eyelids”): WINK. 2. Germanic *winkja in Old English wince, a reel, roller: WINCH. 3. Germanic *winkil- in Old English -wincel, spiral shell: PERIWINKLE!. 4, Germanic *wankil-, *wankul- in: a. Old English wencel, youth, maid (< “inconstant one’): WENCH; b. Old English wancol, inconstant, unsteady: wonky. 5. Germanic *wankj- in: a. Old French gauchir, to turn aside: GAUCHE; b. Anglo-Norman *wencir, to turn aside, avoid (> Middle English wincen, to kick): w1NcE. [Pok. we-n-g- 1148.] wep-. Bad, evil. From earlier *awep-. Suffixed zero-grade form *up-elo- in Germanic *ubilaz, evil, in Old English yfel, evil: EVIL. [wépnam. Weapon. Germanic root. 1. Old English wé- P(e)n, weapon: WEAPON. 2. Old Norse vapn (plural vdpn), weapon: WAPENTAKE.] wer-', High raised spot. 1. Suffixed form *wer-d- in Germanic *wartén- in Old English wearte, wart: WART. 2. Possibly Germanic *war- in obsolete Swedish var- bulde, “pus swelling” (bulde, swelling; see bhel-2), akin to the source of WARBLE2. 3. Latin varius (genitive plural variérum), spotty, speckled, changeable: (VAIR), VARIE- GATE, (VARIETY), VARIOLA, VARIORUM, VARIOUS, VARY; (MINIVER). 4. Latin varix, varicose vein: VARIX. 5. Suf- fixed and extended zero-grade form *wrsu-ko- in Latin verriica, a wart: VERRUCA. [Pok. 2. wer- 1151, 2. ud- 1108.] wer-2. To raise, lift, hold suspended. Earlier form *ower-. 1. Basic form *awer- in Greek aeirein, to raise, and Greek artéria, windpipe, artery: AORTA, ARSIS, ARTERIO-, ARTERIOLE, ARTERY. 2. Possibly referred to this root (obscure basic form *dwer-) is Greek aér (> Latin aer > Italian aria), air: AERIAL AERO-, AIR, ARIA, MALARIA. 3. Related to Greek aér, air, is Greek aura (< zero-grade form *aur-), breath, vapor: AURA. [Pok. 1. wer- 1151.] wer-3, Conventional base of various Indo-European roots; to turn, bend. I. Root *wert-, to turn, wind. 1. Germanic *werth- in: a. Germanic variant *warth- in (i) Old Eng- lish -weard, toward (< “turned toward”): -WARD (ii) Germanic *inwarth, inward (*in, in; see en), in Old English inweard, inward: INWARD; b. perhaps Germanic derivative *werthaz, “toward, opposite,” hence “equiv- alent, worth,” in Old English weorth, worth, valuable, and derivative noun weorth, wierth, value: WORTH}; STALWART. 2. Germanic *werthan, to become (< “to turn into”), in Old English weorthan, to befall: worTH?. 3. Zero-grade form *wrt- in Germanic *wurth- in Old English wyrd, fate, destiny (< “that which befalls one”): WEIRD. 4, Latin vertere, to turn, with its frequentative versare, to turn, and passive versari, to stay, behave (< “to move around a place, frequent”): VERSATILE, VERSE}, VERSION, VERSUS, VERTEBRA, VERTEX, VERTIGO, VOR- TEX; ADVERSE, ANNIVERSARY, AVERT, BOULEVERSE- MENT, CONTROVERSY, (CONVERSE!), CONVERT, DEXTRORSE, DIVERT, EVERT, (EXTROVERSION), EXTRO- VERT, INTRORSE, INTROVERT, INVERT, MALVERSATION, OBVERT, PERVERT, PROSE, RETRORSE, REVERT, SINIS-
1246:ANILE an-! ANILINGUS 4no-, leigh- ANIMA ane ANIMADVERT ane- ANIMAL ane- ANIMATE ane ANIMATO ane- ANIMISM ane- ANIMOSITY ane- ANIMUS ane- ANION ei-1 ANISEIKONIA weik-3 ANKLE ank- ANKYLOSIS ank- ANLAGE an}, legh- ANNALS at- ANNEAL aidh- ANNEX ned- ANNIHILATE ne ANNIVERSARY at-, wer-3 ANNOTATE gno- ANNOUNCE neu-! ANNOY od-2 ANNUAL at ANNUITY at- ANNUL ne ANNULAR 4no- ANNULET 4no- ANNULUS 4no- ANODE sed-2 ANODYNE ed- ANOINT ong¥- ANOMALOUS sem-! ANOMIE nem- ANON ol-no- ANONYMOUS né-men- ANOPHELES obhel- ANORECTIC reg-1 ANOREXIA reg-1 ANORTHITE wrddh- ANOSMIA od-! ANSATE ans- ANSERINE ghans- ANSWER swer-1 ANT mai-1
1276:BABA baba- BABBLE baba- BABE baba- BABKA baba- BABU baba- BABUSHKA baba- BABY baba- BACILLUS bak- BACTERIUM bak- BACULIFORM bak- BAGEL bheug-3 BAGUETTE bak- Bails bheug-3 BAIRN bher-1 BaIT! bheid- BAKE bhé- BAKSHEESH bhag-' BALALAIKA baba- BALCONY bhelg- BALE! bhel-2 BALE? bhelu- BALEEN bhel-2 BALK bhelg- BALL! bhel-2 BALL2 gWele-1 BALLAD gWele-1 BALLAST bhoso-, kla- BALLET gWela-1 BALLISTA gWele-1 BALLOON bhel-2 BALLOT bhel-2 BALLOTTEMENT bhel-2 BAMBINO _baba- BAN! bha-2 BANAL bha-2 BAND! bhendh- BANDANNA bhendh- BANDIT bha-2 BANDOLEER bha-1 BANDORE pandoura BANE gWhen-1 BANG! bheg- BANIAN wen-1 BANISH bha-2 BANK! bheg- BANK? bheg- BANK? bheg- BANKRUPT bheg-, reup- BANNER bha-! BANNERET bha-1 BANNS bha-? BANQUET bheg- BANQUETTE bheg- BANSHEE gWen- BANTLING bheg- Baptist gébh-!
1278:BAPTIZE gWébh-1 BAR? gWere-2 BARB! bhardha BARBARIAN baba- BARBARISM baba- BARBAROUS_ baba- BARBEL bhardha BARBELLATE bhardha BARBER bhardha BARBETTE bhardha BARBICEL bhardha BARBULE bhardha BARD! gWera-3 BARE! bhoso- BARGAIN bhergh-? BARITE gWera-2 BARITONE gWera-2 BARIUM gWera-2 BARK! bherg- BARLEY bhares- BARM_ Dbhreu-2 BARMY bhreu-2 BARN bhares- BARO- gWera-2 BAROUCHE dwo-, ret- BARROW! bher-1 BARROW? bhergh-2 BARROW’ = bher-2 BARYON gWere-2 BARYSPHERE gWere-2 BARYTA gWere-2 BASCULE (s)keu- BASE! gWa- BASE? bassus BASIS gWa- BAS-RELIEF bassus Bass! bhar- Bass? bassus BASSET! bassus BASSO bassus BAT? bhiag- BATE? battuere BATEAU bheid- BATH! bhé- BATHE bhé- BATHOS gWadh- BATHY- gWadh- BATHYSCAPH skep- BATTEN! bhad- BATTERY battuere BATTER! battuere BATTER’ battuere BATTLE battuere BAWD bhel-2 BAWL bhel-4 Bay? bat-
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1283:BELFRY bhergh-? BELIE leugh- BELIEF feubh- BELIEVE leubh- BELL! bhel-4 BELL? bhel-4 BELLADONNA deu-2 BELLE deu-? BELLICOSE duellum
1285:BELLONA duellum BELLOW bhel-4 BELLOWS bhelgh- BELLY bhelgh- BELONEPHOBIA gvel-! BELUGA bhel-1 BELVEDERE deu-2, weid- BEMA gWa-
1299:BILBERRY bhel-2 BILINGUAL dnghi BILIRUBIN reudh-1 BILIVERDIN virére BILL! beu-1 BILL? bhei-2 BILLS = bhei-2 BILLET! beu-1 BILLET-DOUX = dik-u- BILLOW bhelgh- BILTONG bhel-2, dnghi BIMESTRIAL mé-2 BIN bhendh- BINAL dwo- BINARY dwo- BIND bhendh- BINNACLE ghabh- BINOMIAL nem- BIO- gW¥ei-
1309:BITE bheid- BITTER bheid- BITTERN! beu-2 BITUMEN gWet-1 BIVOUAC ambhi, weg-2 BLACK bhel-1 BLACKMAIL méd- BLADDER bhié-2 BLADE bhel-3 BLAIN bhlei- BLAME bha-2 BLANCH bhel-1 BLANCMANGE bhel-1 BLAND mel-1 BLANDISH mel-1 BLANK bhel-1 BLANKET bhel-1 BLARE bhié-1 BLASPHEME bha-2 BLASPHEMOUS bha-2 BLAST bhlé-2 -BLAST melst- BLASTEMA melst- BLASTO- melst- BLASTULA melst- BLATHER bhlé-2 BLAZE! bhel-1 BLEACH bhel-1 BLEAK! bhel-1 BLEAK? bhel-1 BLEAT bhlé-1 BLEMISH bhel-1 BLENCH! bhel-1 BLEND bhel-1 BLENDE bhel-1 BLENNY mel-1 BLESBOK bhel-1, bhugo- BLIND bhel-1 BLINDFOLD bhel-1 BLINI mele- BLINTZ mele- BLISTER bhlei- BLITE mele- BLITZKRIEG bhel-1, gwere-2 BLOAT bhieu- BLOND bhel-1 BLOOM! bhel-3 BLOOM? bhel-3 BLOSSOM bhel-3 BLOW! bhié-2 BLOW3 bhel-3 BLUE bhel-1 BLUNDERBUSS (s)tene- BLUSH bhel-1 BOARD bherdh- BOAST! beu-1 BOAT bheid- BOATSWAIN bheid- BOCACCIO beu-1 BODE! bheudh- BODEGA dhé-1 BODHISATTVA bheudh-, es- BoER bheue-
1313:BOLD bhel-2 BOLE! bhel-2 BOLL bhel-2 BOLLIX bhel-2 BOLOMETER gW¥ele-1 BOLSHEVIK bel- BOLSTER bhelgh- BOLT! bheld- BOMB bamb- BOMBARD bamb- BONANZA deu-2 BONBON deu-2 BOND bhendh- BONDAGE bheue- BONHOMIE deu-2, dhghem- BONITO deu-2 BONNE deu-2 BONNYCLABBER band- BONTEBOK bhugo- BONUS deu-2 BOOBY baba- BOODLE bheue- BOOK bhago-
1314:BOOM? bheue- BOON! pbha-2 BOON2 deu-2 BOOR bheue- BOOT? bhad- BOOTH bheue- BORDELLO bherdh- BORDER bherdh- BORE! bher-2 BORE’ bher-1 Boreas gWero-1 BOROUGH bhergh-2 BORROW bhergh-1 BORSCHT bhar- BOSCAGE busk- BOSOM beu-1 BOTH ambh6o BOTHRIUM bhedh- BO TREE bheudh- BOTTOM bhudh- BOTTOMRY bhudh- BOTULIN gWet-3 BOTULINUM gWet-3 BOTULISM gWet-3 BOUCLE beu-1 BOUGH bhaghu- BOUILLABAISSE beu-! BOUILLON beu-1 BOULDER bhel-2 BOULE! gWele-1 BOULE? beu-! BOULEVARD bhel-2, werg-
1318:BOUTIQUE dhé-1 BOUTON bhau- BOVINE g¥ou- Bow? bheug-3 Bows bheug-3 BOWEL gW¥et-3 BOWERY bheue- BOWER! bheue- BOWL! bhel-2 BOWL? beu-1 BOWSPRIT sper-4 BOX! puxos
1324:BRIO gWere-2 BRIOCHE bhreg- BRISANCE bhréi- BRISTLE bhar- BRITTLE bhreu-1 BRONCHIECTASIS  ten- BRONCHO- gWere-4 BRONCHUS gWere-4 BRONTOSAUR bhrem-! BROOD bhreu-2 BROOK? bhriig- BROOM bhrem-2 BROTH bhreu-2 BROTHEL bhreu-' BROTHER bhrater- BROW bhri- BROWN bher-3 BROWSE bhreus-1 BRUIN bher-3 BRUISE bhreus-2 BRUMAL mregh-u- BRUNET bher-3 BRUT gWere-2 BRUTE gWere-2 BUBO beu-! BUCCAL beu-1 BUCEPHALUS gWou- BUCK! bhugo- BUCKAROO wak- BUCKBOARD beu-! BUCKLE! beu-! BUCKLE? beu-1 BUCKSHEE bhag-' BUCKWHEAT bhago- BUCOLIC gou-, kWel-1 BuppHA bheudh- BUDGET bhelgh- BUDGE! beu-1 BUGLE! gWou- BUGLOss gldgh- BUILD bheue- BULGE bhelgh- BULIMIA gWou-, leia- BULK! bhel-2 BULL! bhel-2 BULL? beu-1 BULLA beu-1 BULLATE beu-1 BULLET beu-! BULLETIN beu-1 BULLION beu-1 BULLY? beu-1 BULWARK bhel-2, werg- BUNCO bheg- BUND! bhendh- BUND? bhendh- BUNDESRAT ar- BUNDLE bhendh- BUNG peuk- BUNGLE bheg- BUPRESTID gWou- BUR! bhar- BURDEN! bher-1 BURG bhergh-2 BURGESS bhergh-2 BURGHER bhergh-2 BURGLAR bhergh-2 BURGOMASTER bhergh-2 BURIAL bhergh-! BURIN bher-2 BURN! gWher- BURN? bhreu-2 BURNET bher-3 BURNISH bher-3 BURSA bursa BURSAR bursa BURSE bursa BURST bhres- BURY bhergh-1 BUSHEL? bhau- BUSK! busk- BUSK? s(w)e-
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1360:CINCH kenk-1 CINCTURE kenk-1 CINDER sendhro- CINEMATOGRAPH kei-3 CINEMATORADIOGRAPHY kei-3 CINERARIUM keni- CINEREOUS_ keni- CINGULUM_ kenk-1 CINQUAIN penkWe CINQUE penkWe CINQUEFOIL bhel-3, penkwe cIRcA sker-3 CIRCADIAN deiw- CIRCLE sker-3 CIRCUIT ei-1 CIRCUM-  sker-3 CIRCUMCISE kae-id- CIRCUMDUCTION deuk- CIRCUMFUSE gheu- CIRCUMLOCUTION  tolkw- CIRCUMSCRIBE skribh- CIRCUMSPECT spek- CIRCUMSTANCE sta- CIRCUMVENT gWa- CIRCUMVOLVE wel-3 cIs- ko-
1390:CONFECT dhé-1 CONFEDERATE bheidh- CONFER bher-1 CONFESS bha-2 CONFETTI dhé-1 CONFIDANT bheidh- CONFIDE bheidh- CONFIDENT bheidh- CONFIGURATION dheigh- CONFIRM dher-2 CONFLAGRANT bhel-1 CONFLAGRATION bhel-1 CONFLATE bhié-2 CONFLICT bhiig- CONFLUENT bhieu- CONFORM merph-
1418:DEEP dheub- DEER dheu-! DEFACE dhé-1 DEFAME bha-2 DEFEASANCE dhé-1 DEFEAT dhé-1 DEFECT dhé-1 DEFEND gWhen-1 DEFENSE gWhen-1 DEFER! bher-1 DEFER? bher-1 DEFERVESCENCE bhreu-2 DEFIANCE bheldh- DEFICIENT _dhé-1 DEFILE! pu-2 DEFILE? gWhi- DEFLAGRATE bhel-1 DEFLATE bhlé-2 DEFLOWER bhel-3 DEFOLIATE bhel-3 DEFORCE bhergh-? DEFORM merph- DEFUNCT bheug-2 DEFY bheidh- DEGAGE wadh-1 DEGENERATE geno- DEGLUTINATE gel-1 DEGLUTITION gWel-3 DEGRADE ghredh- DEGREE ghredh- DEGRESSION ghredh- DEGUST geus- DEHISCE ghal- DEICIDE deiw- DEICTIC deik- DEIFIC delw- DEIGN dek-1 DEISM deiw- DEITY deiw- DEJECT yé- DELAINE wele-1 DELAY slég- DELEGATE leg-1 DELIBERATE [ithra DELINQUENT leikw- DELIQUESCE wileik- DELIRIUM leis-1 DELIVER leudh-2 DELL dhel- DELPHINIUM g¥elbh- DELUDE leid- DELUGE leu(@)- DELVE dhelbh- DEMAGOGUE ag-, da- DEMAND man-2 DEMARCATION merg- DEME da- DEMEAN! men-2 DEMEAN2 mei-1
1442:EDIBLE ed- EpicT deik- EDIFICE aidh-, dhé-1 EDIFY aidh-, dhé-1 EDITION d6- EDUCATE deuk- EDUCE deuk- EFFACE dhé-1 EFFECT dhé-1 EFFEMINATE dhé(i)- EFFERENT bher-1 EFFERVESCE bhreu-2 EFFETE dh@(i)- EFFICACIOUS dhé-1 EFFICIENT dhé-1 EFFIGY dheigh- EFFLORESCE bhel-3 EFFLUENT bhleu- EFFLUVIUM bhieu- EFFLUX bhlieu- EFFORT bhergh-2 EFFULGENT bhel-1 EFFUSE gheu- EFTSOONS apo- EGEST gerere EGG! awi-
1454:ELUANT leu(@)- ELUCIDATE leuk- ELUDE leid- ELUTE leu(a)- ELUVIUM leu(a)- ELYTRON wel-3 EMACIATE mak- EMANATE ma-3 EMANCIPATE man-2 EMASCULATE mas EMBASSAGE ag- EMBASSY ag- EMBELLISH deu-2 EMBER eUS- EMBER DAY ambhi, rei-3 EMBLEM gWele-1 EMBLEMENTS bhel-3 EMBOUCHURE beu-! EMBRACE mregh-u- EMBROCATE mergh- EMEND mend- EMERGE mezg-! EMERITUS (s)mer-2 EMESIS weme- EMETIC weme- EMIGRATE mei-! EMINENT men-2 EMIT (s)meit(9)- EMMET mai-1 EMOLLIENT mel-1 EMOTION meue- EMPEROR pere-! EMPHASIS bha-' EMPHYSEMA pu-! EMPIRIC per-4 EMPLOY plek- EMPORIUM per-2 EMPRISE ghend- EMPTY med- EMPYEMA pu-2 EMPYREAL pil- EMULSION melg- EMUNCTORY meug-2 EN-! en
1459:ENERVATE (s)neeu- ENFILADE gWhi- ENFLEURAGE bhel-3 ENFORCE bhergh-2 ENGAGE wadh-! ENGAGE wadh-! ENGENDER gene- ENGINE gene- ENGRAVE ghrebh-2 ENGROSS gW¥res- ENHANCE al-3 ENIGMA ai-2 ENJOIN yeug- ENJOY gau-
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1507:FERIA dhés- FERMATA dher-2 FERMENT bhreu-? FERN per-2 FEROCIOUS ghwer- FERRET! bher-1 FERRET? bhel-3 FERRI- ferrum FERRO- ferrum FERROUS ferrum FERRUGINOUS ferrum FERRULE wei-1 FERRY per-2 FERTILE bher-1 FERVENT bhreu-2 FERVID bhreu-2 FERVOR bhreu-2 FEss bhasko- -FEsT dhés- FESTAL dhés- FESTINATE bhers- FESTIVAL dhés- FESTIVE dhés- FESTOON dhés- FETAL dhé(i)- FETCH! ped-1 FETE dhés- FETICIDE dhé(i)- FETISH dhé-1 FETLOCK ped-! FETTER ped-1 FETTLE ped-2 FETUS dh@(i)- FEUD! peig-2 FEUD? peku- FEUILLETON bhel-3 FEVERFEW bheug-! FEW pau-
1516:FIx dhigw- FIXATE dhig¥- FIXITY dhigw- FIXTURE dhigw- FIZGIG peis-2 FIZZLE pezd- FJELD pelis- FJORD per-2 FLABELLUM bhié-2 FLAG! = plak-1 FLAGELLATE bhiag- FLAGELLUM _bhiag- FLAGITIOUS bhlag- FLAGRANT bhel-1 FLAIL  bhlag- FLAIR bhrag- FLAKE! plak-1 FLAKE? plak-1 FLAMBE bhel-1 FLAMBEAU bhel-1 FLAMBOYANT bhel-1 FLAME bhel-1 FLAMEN bhilad- FLAMINGO bhel-1 FLAMMABLE bhel-1 FLAN plat- FLANEUR pele-2 FLANK kleng- FLANNEL wele-1 FLAP plab-
1517:FLAT!  plat- FLAT? plat- FLATTER! plat- FLATUS bhié-2 FLAVESCENT bhel-1 FLAVIN bhel-1 FLAVO- bhel-1 FLAVONE bhel-1 FLAVOPROTEIN bhel-1 FLAVOR bhié-2
```


## [2026-09-05T06:23:09.299Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftoppm -f 84 -l 84 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg84 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render page 84"
}
```


### [2026-09-05T06:23:11.414Z] TOOL RESULT

```
total 10004
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 02:23 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 01:20 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    4061 Sep  5 02:00 avestan.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5971 Sep  5 02:13 baga.html
-rw-rw-r-- 1 sfmqrb sfmqrb  189420 Sep  5 02:15 bqt440_bottom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  513902 Sep  5 02:15 bqt440.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  502834 Sep  5 02:02 bqt538_big.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   72705 Sep  5 02:02 bqt538_fn6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24595 Sep  5 02:02 bqt538_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22593 Sep  5 02:02 bqt538_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  207980 Sep  5 02:01 bqt538.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  282104 Sep  5 01:29 bqt733_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  669351 Sep  5 01:29 bqt733.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   17369 Sep  5 01:35 bqtv1_361_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  470042 Sep  5 01:35 bqtv1_361.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  241161 Sep  5 01:36 bqtv1_398_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  482084 Sep  5 01:36 bqtv1_398.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  190109 Sep  5 01:35 bqtv1_399_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53579 Sep  5 01:36 bqtv1_399_head2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1625 Sep  5 01:35 bqtv1_399_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  510341 Sep  5 01:35 bqtv1_399.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   63555 Sep  5 01:43 build71.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5214 Sep  5 02:23 build82a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb  445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1278807 Sep  5 01:37 hrn127.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   40966 Sep  5 01:40 mk67.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58318 Sep  5 01:45 mk70.py
-rw-rw-r-- 1 sfmqrb sfmqrb   78619 Sep  5 02:02 mk73.py
-rw-rw-r-- 1 sfmqrb sfmqrb   68454 Sep  5 02:01 mk75.py
-rw-rw-r-- 1 sfmqrb sfmqrb   79383 Sep  5 02:19 mk78.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52793 Sep  5 02:18 mk79.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55169 Sep  5 01:30 pg67.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57649 Sep  5 01:33 pg69.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50966 Sep  5 01:33 pg69_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77968 Sep  5 01:31 pg70.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75801 Sep  5 01:29 pg71_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71145 Sep  5 01:29 pg71.png
-rw-rw-r-- 1 sfmqrb sfmqrb  134140 Sep  5 01:44 pg72_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2377 Sep  5 01:44 pg72_afandi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11769 Sep  5 01:47 pg72_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2947 Sep  5 01:44 pg72_fr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49860 Sep  5 01:44 pg72.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81180 Sep  5 01:47 pg73.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56073 Sep  5 01:48 pg74.png
-rw-rw-r-- 1 sfmqrb sfmqrb  108877 Sep  5 01:51 pg75_400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   20612 Sep  5 01:51 pg75_greeklatin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75134 Sep  5 01:51 pg75.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66505 Sep  5 01:51 pg76.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65211 Sep  5 02:00 pg77.png
-rw-rw-r-- 1 sfmqrb sfmqrb  155334 Sep  5 02:00 pg78_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63822 Sep  5 01:59 pg78.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59439 Sep  5 02:09 pg79.png
-rw-rw-r-- 1 sfmqrb sfmqrb   58953 Sep  5 02:08 pg80.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99904 Sep  5 02:15 pg81.png
-rw-rw-r-- 1 sfmqrb sfmqrb   29321 Sep  5 02:20 pg82_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74477 Sep  5 02:20 pg82.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56108 Sep  5 02:20 pg82_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82358 Sep  5 02:23 pg84.png
```


## [2026-09-05T06:23:12.667Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN boulevard/bulwark ===\"; grep -n -i -E \"boulevard|bulwark\" KLN_1966.txt KLN_1971.txt SKT.txt | head -12\necho \"=== KLN ballot/balloon ===\"; grep -n -i -E \"^ballot|ballot,|balloon\" KLN_1966.txt KLN_1971.txt SKT.txt | head -12\necho \"=== KLN baleen/whalebone ===\"; grep -n -i -E \"baleen|ballaena|balaena\" KLN_1966.txt KLN_1971.txt SKT.txt | head -12\necho \"=== KLN budget/bougette/bulga ===\"; grep -n -i -E \"budget|bougette|bulga\" KLN_1966.txt KLN_1971.txt SKT.txt | head -12",
 "description": "Klein and Skeat lookups"
}
```


### [2026-09-05T06:23:12.784Z] TOOL RESULT

```
=== KLN boulevard/bulwark ===
SKT.txt:274:sconce  (1),  a  small  fort,  bulwark.  (Du. — 'F —L.)  Also  applied  to  a  hclinct,  and even  to  the  head.  —  O- Du.  sch*iHtst  (Dii. sfhanf').  a  fortrcis.  sconce.  •■  O.  V.  <sc9Hser^ lo  hide,  cover ;  pp.  ttcont.  —  L.  ahsconsus, used  (AS  well  OA  aouoHiiitus)  as  pp.  of  abi- ceHiiifi,  to  hide  tabovci.
SKT.txt:3052:Casemate.  (F.  -  Ital.)     F. loop-bole  in  a  fortiiicd  walL—llaLi maifa,  a  chamber  built  under  a bulwark,  to  hinder  those  who ditch  to  scale  the  wall  of  a  fort. to  mean    'dark  chamber.'  — TtaL case,  house,  cottage,  room ;  and  II fern,  of  ma/fo,  ong.  mad,  but  the rriaUu  means  '  dim.'
KLN_1971.txt:32365:boulevard, n. — F., earlier boloart , boulevert, 
KLN_1971.txt:32367:fication’, fr. MDu. bolwerc . See bulwark, 
KLN_1971.txt:35193:bulwark, n., 1) rampart; 2) protection. — ME. 
KLN_1971.txt:35197:‘trunk of a tree’, and work and cp, boulevard. 
KLN_1971.txt:35198:Derivative: bulwark, tr. v. 
KLN_1971.txt:156790:tify, protect’, fr. moenia , ‘walls, bulwarks’, 
KLN_1971.txt:156857:*moi-ni-), ‘walls, bulwarks’. See muniment and 
KLN_1971.txt:199834:boulevart (now boulevard). 
KLN_1971.txt:215142:sconce, n., cover, fort. — Du. schans , ‘bulwark’. 
KLN_1971.txt:268303:bulwark. Cp. also ergon and words there referred 
=== KLN ballot/balloon ===
SKT.txt:1345:balloon,  a  large  ball.  (F.-U.  U.  G.) Formerly  baU^ti^  a  ball  used  in  a  gam«
SKT.txt:1352:ballot.  (F.-O.  H.G.)  F.  baUoler,  to choose  lots.  >-F.  f>allotte,  a  little  ball  Dsed for  voting ;  dimiii.  of  K.  balU,  a  balL  And see  Bole,  Bov/1.  Bolt,  Bolster.  Boil  (i), Boiled  (under  Bulfffl).
SKT.txt:1356:Balloon,  Ballot;  see  Ball  (3).
SKT.txt:13278:parachute,  an  apparatus  for  breaking «  fall  from  a  balloon.  (F.  —  L.)  F.  pam- thute.  put  for  pat^  ^  ehtU,  lit.  that  which parries  or  guards  against  a  fall.  —  F.  par<r, 10  deck,  U50  to  guard  against;  d.  prep., lo,  against;  thute,  a  fall.  Here  partr  = L  parare;  *)  -  L.  iui\  and  thute  is  allied lo  Ical.  eaduto,  fallen,  from  L.  eadert^  to fall.
SKT.txt:23563:FRENCH  FROM  OLD  HIGH  GER- MAN :  arrange,  await,  award,  baldric,  ball (2),  balloon,  ballot,  banish,  baron,  baste(3), bostile,  blanch  (i)*  blank,  boot  (1),  boss, bottle  (a),  brawn,  bream,  chamberlain, chine,  crayfish  (craw-fish),  dance,  eclat, enamel,  ermine,  eschew,  espy,  fief,  fife,  fil- bert, frank,  franchise,  (rankliD,  freight, furbish,  furnish,  garb(i),  garb  (3),  garden, gimp,  guarantee  (guaranty),  guard,  guise,
KLN_1971.txt:25209:‘bundle*, baleen, balinger, balloon, ballot, bil- 
KLN_1971.txt:25274:balloon*, fr.. ballon . See next word and -et. 
KLN_1971.txt:25275:balloon, n. — F. ballon, fr. It. pallone , which is 
KLN_1971.txt:25282:Derivatives: balloon, tr. and intr. v., and the 
KLN_1971.txt:25283:hybrid noun balloon-ist, n. 
KLN_1971.txt:25284:ballot, n. — F. ballotte, fr. It. ballotta , ‘little ball’, 
KLN_1971.txt:25288:Derivatives: ballot, intr. and tr. v., ballot-age 
=== KLN baleen/whalebone ===
KLN_1971.txt:25007:Balaena, n., a genus of whales, the Greenland 
KLN_1971.txt:25008:whale. — L. ballaena, balaena. See baleen, 
KLN_1971.txt:25160:baleen, n., whalebone. — ME. balene , baleyne, 
KLN_1971.txt:25162:L. ballaena, ‘whale*, which was borrowed fr. Gk. 
KLN_1971.txt:25168:and cp. Balaena, balioger. 
KLN_1971.txt:25175:gier , ‘whaleship’, fr. baleine , ‘whale*. See baleen, 
KLN_1971.txt:25208:‘to swell*. See belly and cp. Balaena, bale, 
KLN_1971.txt:25209:‘bundle*, baleen, balinger, balloon, ballot, bil- 
KLN_1971.txt:35131:baleen, ball, ‘a round body’, bold, bulk, ‘size’, 
KLN_1966.txt:4303:Balaena,  n.,  a  genus  of  whales,  the  Greenland whale.  —  L.  ballaena,  balaena.  See  baleen, balaghat,  balaghaut,  n.,  tableland  above  the  pas¬ ses  (Anglo-Ind.)  —  Formed  fr.  Pers.  bald, ‘above’,  and  Hind,  ghat,  ‘a  pass’, balalaika,  n.,  a  Russian  stringed  instrument  with a  triangular  body.  —  Russ,  balalaika,  which, according  to  Erich  Berneker,  Etymologisches
KLN_1966.txt:4319:bale,  n.,  balefire.  —  OE.  beel.  See  balefire, baleen,  n.,  whalebone.  —  ME.  balene,  baleyne, ‘whale,  whalebone’,  fr.  OF.  baleine,  ofs.m.,  fr. L.  ballaena,  ‘whale’ ,  which  was  borrowed  fr.  Gk. (pdtXXocwa,  of  s.m.,  through  the  medium  of  the Illyrian  language,  a  fact  which  explains  the  tran¬ sition  of  Gk.  9  into  L.  b  (instead  of  p).  Gk. 9<iXXaiva  is  related  to  ipaXXAs,  ‘penis’,  fr.  I.-E.
KLN_1966.txt:4321:base  *bhel-,  ‘to  swell’.  See  ball,  ‘a  round  body’, and  cp.  Balaena,  balinger. balefire,  n.  —  OE.  bielfyr,  ‘funeral  fire’,  com¬ pounded  of  bxl,  ‘a  blazing  fire,  a  funeral  pile’, and  fyr,  ‘fire’.  The  first  element  is  rel.  to  ON.  bdl, ‘a  great  fire’,  fr.  I.-E.  base  *bhel-,  ‘to  shine’;  see bald.  For  the  second  element  see  fire, balinger,  n.,  a  whaleship  ( obsol .)  —  OF.  balen- gier,  ‘whaleship*,  fr.  baleine,  ‘whale’.  See  baleen, balk,  also  baulk,  n.,  ridge  of  land  left  unplowed between  furrows :  a  beam.  —  ME.  balke,  ‘beam’, fr.  OE.  balca,  ‘ridge  between  furrows,  beam, rafter’,  rel.  to  OS.  balko,  ON.  bjalki,  Dan.  bjelke, Swed.  bjdlke,  OFris.  balka,  OHG.  balko,  balcho, MHG.  balke,  G.  Balken,  ‘beam,  rafter’  (cp., with  vowel  gradation,  OE.  bolca,  ‘wooden gangway  of  a  ship’),  ON.  bolr,  ‘trunk  of  a  tree’ ; fr.  I.-E.  base  *bheleg-,  ‘beam,  plank’,  whence also  Gk.  tpaXzy?,  ‘trunk,  log;  line  of  battle, battle  array’,  cpaXtoit;,  ‘beam’,  L.  fulcire,  ‘to prop’,  fulcrum,  ‘bedpost’,  Lith.  balziena,  ‘cross¬ bar’,  Lett,  bdlziens,  ‘prop,  stay’.  Cp.  balcony. Cp.  also  block,  bole,  ‘trunk’,  bulk,  ‘projection’, debauch,  ebauchoir,  fulcrum,  phalange,  phalanx, planch,  planchet,  plancier,  plank.
=== KLN budget/bougette/bulga ===
SKT.txt:21241:Wattle,  a  flexible  rod,  hurdle ;  fleshy part  under  the  throat  of  a  cock  or  turkey. i^E.*)  The  orig^.  sen&e  was  something  twined or  woven  together;  hence  a  hurdle,  a  bag of  woven  stuff,  a  bag  on  a  cock's  neck. M.  E.  watel,  a  ba^ ;  A.  S.  tuafel,  watul,  a hurdle.  Base  WAT;  from  ^W A,  to  bind. wallet,  a  bag,  budget.  (E.)  M.  E. wa/et,  a  comiplion  of  M.  E.  wafeit  a  wat- tle, also  a  bag.  In  P.  Plowman,  C.  xi. 269,  where  some  MSS.  express  '  bag-full ' by  xoatel-ful,  others  have  waUt-ful.  Again, Saakespcare  has  ivaliets  for  bags  of  flesh upon  the  neck  (Temp.  iii.  5.  46),  which  is the  same  as  waffles.  Further,  cf.  O.  Da. wattsa^i,  G.  watiOik,  wnzdaaei,  a  wallet, where  tttf/-  ail  swers  lolhc  base  o(A.S,waf-e/.
SKT.txt:23406:Frtmh  from  Ctilic  {or  Breton) :  attach, attack,  bnggage  (i),  baggage  (a),  bar, barrel,  barrier,  basin,  bnscnct  (basnet), beak,  billet  (a), billiards,  bobbin?,  boudoir  ?, bound  \^i),  bourn  (t),  brail,  branch,  brave, bray  (a),  bribe,  brisket,  bruit,  budge  (a), budget,  car,  carcaiict,  career,  carol,  car- penter, carry,  caul,  cloak  (,cloke),  gafT, Barter,  gobbet,  gobble  {with  E.  su^ix)^ gravel,  grebe,  harness,  hurl  {with  E.  su^ix), nurt.  hurtle  {wiih  £.  shJIx),  javelin,  job (2),  lay  (a),  lias,  lockram,  maim  (a)7, mavis,  mutton  ?.  petty  ?,  pickaxe,  picket,  pip (3)*  pitl^c,  piquet,  pottage,  potUc,  pouch.
KLN_1971.txt:2161:Bulgarian 
KLN_1971.txt:2758:Old Bulgarian 
KLN_1971.txt:28076:boly , ‘belly’, Bret, bolc'h, ‘flax pod’. (L. bulga, 
KLN_1971.txt:31521:and cp. billow, budget, bulge. 
KLN_1971.txt:34925:bulga, ‘leather wallet’. See bulge and cp. budget. 
KLN_1971.txt:34934:budget, n. — F. bougette, ‘a little trunk of wood’, 
KLN_1971.txt:34938:Derivatives: budget , tr. and intr. v., budget-ary, 
KLN_1971.txt:34939:adj., budget-eer, n., budge t-er, n. 
KLN_1971.txt:35012:OF. (= F.) bougre , fr. ML. Bulgarus, ‘a Bul- 
KLN_1971.txt:35013:garian; heretic; sodomite'. See Bulgarian.
```


## [2026-09-05T06:23:18.878Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- boulevard 32360-32372 ---\"; sed -n '32360,32372p' KLN_1971.txt\necho \"--- bulwark 35190,35200 ---\"; sed -n '35190,35200p' KLN_1971.txt\necho \"--- ball/balloon/ballot 25195,25295 ---\"; sed -n '25195,25215p;25270,25292p' KLN_1971.txt\necho \"--- baleen 25155,25172 ---\"; sed -n '25155,25172p' KLN_1971.txt\necho \"--- budget/bulge 34920,34945 ---\"; sed -n '34920,34945p' KLN_1971.txt\necho \"--- bulk 35125,35140 ---\"; sed -n '35125,35142p' KLN_1971.txt",
 "description": "Klein entries in full"
}
```


### [2026-09-05T06:23:19.057Z] TOOL RESULT

```
--- boulevard 32360-32372 ---
see ballistic. See Frisk, GEW., I, pp. 258-59 s.v. 
jlouXo^ai. 

boule, n., a game. — F., ‘ball’, fr. L. bulla , ‘any 
round object, bubble, boss’. See bill, ‘document*, 
boulevard, n. — F., earlier boloart , boulevert, 
balouart, belouart, orig. meaning ‘work of forti- 
fication’, fr. MDu. bolwerc . See bulwark, 
boulter, n., a long line for fishing, with hooks 
attached. — Of unknown origin, 
bounce, intr. and tr. v. — ME. bunsen . Cp. LG. 
bunsen, Du. bonzen , ‘to beat, thump’. Cp. also 
jounce. 
--- bulwark 35190,35200 ---
Derivatives: bully -ing, adj., bully-ing-ly, adv. 
bulrush, n. — ME. bolroysche, bulrysche. See bole, 
‘trunk of a tree’, and rush, the plant, 
bulwark, n., 1) rampart; 2) protection. — ME. 
bulwerk, fr. MLG. (= Du.) bolwerk, which is rel. 
to MHG. bolwerk , G.Bollwerk, Swed. bolverk . 
These words lit. mean ‘bole work’. See bole, 
‘trunk of a tree’, and work and cp, boulevard. 
Derivative: bulwark, tr. v. 

bum, intr. v., to make a humming sound. — Of 
--- ball/balloon/ballot 25195,25295 ---

balk, also baulk, tr. v., to hinder, thwart; intr. 
v., to refuse. — Formed fr. prec. word and lit. 
meaning ‘to put a beam in the way*. Cp. bilk. 

Balkanize, tr. v. — Coined by the English jour- 
nalist and editor James Louis Garvin (1868- 
1947) in allusion to the political condition in the 
Balkans in 1912-13. 

ball, n., a round body; a sphere. — ME. balle, 
fr. ON. bo Ur, which is rel. to OHG. ballo, balla , 
MHG. balle , bal, G. Ball, fr. I.-E. base *bhel -, 
‘to swell*. See belly and cp. Balaena, bale, 
‘bundle*, baleen, balinger, balloon, ballot, bil- 
low, bulk, ‘size*, and the first element in bill- 
berry and in pall-mall. 

Derivatives: ball, tr. y., to form into a ball, 
ball-er , n. 

word and -ics. 

ballonet, n., an auxiliary gas or air bag in a bal- 
loon or airship. — F. ballonnet, lit. ‘a small 
balloon*, fr.. ballon . See next word and -et. 
balloon, n. — F. ballon, fr. It. pallone , which is 
formed with augment, suff. - one fr. pal la, ‘a 
ball’, a word of Teut. origin; see ball, ‘a round 
body*, and -oon. The b in F. ballon (fr. It. pal- 
lone) is due to the influence of F. balle, ‘ball’. 
Cp. pallone. 

Derivatives: balloon, tr. and intr. v., and the 
hybrid noun balloon-ist, n. 
ballot, n. — F. ballotte, fr. It. ballotta , ‘little ball’, 
dimin. of balla , ‘ball’ (see E. ball, ‘a round 
body’); so called in allusion to the small balls 
formerly dropped into the voting urn. 
Derivatives: ballot, intr. and tr. v., ballot-age 
(q.v.) 

Ballota, n., a genus of plants of the mint family 
(bot) — ModL., fr. Gk. paXXon^, ‘the black 
--- baleen 25155,25172 ---

bale, n., bucket, v., to dip water. — See bail, 
‘bucket*. 

bale, n., balefire. — OE. bsel. See balefire, 
baleen, n., whalebone. — ME. balene , baleyne, 
‘whale, whalebone*, fr. OF. baleine , of s.m., fr. 
L. ballaena, ‘whale*, which was borrowed fr. Gk. 
9<IXXaiva, of s.m., through the medium of the 
Illyrian language, a fact which explains the tran- 
sition of Gk. 9 into L. b (instead of p). Gk. 
9<&XXotivflt is related to 9CCXX65, ‘penis’, fr. I.-E. 
base *bhel -, ‘to swell*. See ball, ‘a round body’, 
and cp. Balaena, balioger. 
balefire, n. — OE. bxlfyr, ‘funeral fire*, com- 
pounded of bxl, *a blazing fire, a funeral pile*, 
and fyr, ‘fire*. The first element is rel. to ON. bdl, 
‘a great fire*, fr. I.-E. base *bhel-, ‘to shine’ ; see 
--- budget/bulge 34920,34945 ---
budge’, which are of the same origin as F. 
bouger, and see boil, v. 

budge, n., a kind of fur. — ME. bouge , ‘bagVfr. 
OF. boge, bouge, ‘leather bag, wallet’, fr. L. 
bulga, ‘leather wallet’. See bulge and cp. budget. 
Cp. also belly. 

budgereegah, n., the Australian parakeet. — Na- 
tive Australian. 

budgerow, n., a keelless barge ( Anglo-Ind .) — 
Hind, bajrd. 

budget, n. — F. bougette, ‘a little trunk of wood’, 
dimin. of boge, bouge, ‘leather bag, wallet’. See 
budge, ‘fur’, and -et. 

Derivatives: budget , tr. and intr. v., budget-ary, 
adj., budget-eer, n., budge t-er, n. 
budmash, n., a worthless fellow, rake (Anglo- 
Ind.) — A hybrid coined fr. Pers. bad, ‘evil’, 
and Arab, ma'dsh, ‘means of livelihood’, fr. 
l dsha, ‘he lived’. Cp. the first element in next 
word. 

--- bulk 35125,35140 ---
bole, fr, OE. bula, ‘bull’, rel. to ON. boli, MDu. 
bul(le), Du. bul, G. Bulle, of s.m., OE. bitlluc , 
‘little bull’, bealluc , ‘testicle’, ON. bollr, ‘ball’, 
fr. I.-E. base *bhel- , ‘to swell’, whence also Gk. 
<paXX6c, ‘penis’, tpaXXorxva, <paXXv), ‘whale’, L. 
folds, ‘a pair of bellows’. Cp. bullock. Cp. also 
baleen, ball, ‘a round body’, bold, bulk, ‘size’, 
follicle, phallus. For derivatives of base *bhelgh-, 
an enlargement of base *bhel~, see belly, bud- 
get, bulge. 

Derivative: bull , intr. and tr. v., bull-ish, adj. 
bull, n., an edict of the pope. — ME. bulle, fr. OF. 
bulle, fr. It. bulla, fr. ML. bulla , ‘seal affixed to a 
document, document’, fr. L. bulla, ‘bubble, boss, 
knob’, fr. I.-E. whence also Lith. bule, 

bulls , ‘buttock’, MDu. puyl , ‘bag’, MLG. pull.
```


## [2026-09-05T06:23:30.837Z] TOOL CALL #20: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg84.png"
}
```


### [2026-09-05T06:23:31.187Z] TOOL RESULT

```

```


## [2026-09-05T06:23:31.183Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T06:23:40.899Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 barsam ===\"; grep -n \"برسم\" BQT_v1_pages.txt | head -10\necho \"=== pdf page tags ===\"; grep -c \"pdf page\" BQT_v1_pages.txt",
 "description": "BQT barsam"
}
```


### [2026-09-05T06:23:40.955Z] TOOL RESULT

```
=== BQT v1 barsam ===
15980:پرستندة آذر زردهشت. همی‌رفت باباژ و برسم بمشت . فردوسی‌طوسی «مزدیسنا۲۵۳ببمد»
18597:دس آن هم‌آهن باشد و آنرا برسم چین خوانند
18602:بخوانند . و برسم را با برسم چین ببرندیس‌برسم
18606:مازند » و برسمهارا اسدرون
18619:نسکهای عشهور زند )۱( آست سی و پنج برسم
18621:وچهار برسم, وهنگلم بدن شتن وچیزی خوردن
18622:و عیادت کردن پنج برسم ؛ و چون یکبار
18623:نگ وندیداد خوانده‌شودآن برسمپا باطل گردد؛
18625:شد اختیار دارند ء خواهند با همان برسمها عمل
18626:کنند و خواهند برسم نازه بدست گیرند . و از
=== pdf page tags ===
0
```


## [2026-09-05T06:23:43.315Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== MON بلوار ===\"; grep -n \"بلوار\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON بودجه ===\"; grep -n \"بودجه\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON بالون ===\"; grep -n \"بالون\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON بالن ===\"; grep -n \"بالن\" MON_part1.txt MON_part2.txt | head -5\necho \"=== MON بالش ===\"; grep -n \"بالش\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Mo'in lookups"
}
```


### [2026-09-05T06:23:43.460Z] TOOL RESULT

```
=== MON بلوار ===
MON_part1.txt:26195:محل گردش عموم است. بلوار. 
=== MON بودجه ===
MON_part1.txt:25873:دستورالعمل (بودجه) هر ولایت به خرج 
MON_part1.txt:26017:۰ اسفند ۱۳۱۲ بودجه را چنین تعریف 
MON_part1.txt:64803:تفریغ بودجه موظف است و شامل پنج شعبه 
MON_part2.txt:56459:بودجه) هر ایالت و ولایتی را از روی 
MON_part2.txt:61875:دستورالعمل (بودجهة ابلاغی) و اجازه و 
=== MON بالون ===
MON_part1.txt:20966:بالون: «ماقه (.) (فر.) کره‌ای بزرگک که 
MON_part1.txt:64447:دیریژابل: ا"ت2آءآه (امر.) قسمی بالون که 
MON_part2.txt:23320:کشتی هوایی: بالن (بالون)» سفینة هوایی 
=== MON بالن ===
MON_part2.txt:19582:حفریات عمیق و کندن تونل‌های بالنسه 
MON_part2.txt:19739:بریدگی و زخم در انساج بشود و بالنتیجه 
MON_part2.txt:23320:کشتی هوایی: بالن (بالون)» سفینة هوایی 
MON_part2.txt:27570:فرمول 5:0۲ است که دارای سختی بالنسبه 
MON_part2.txt:35648:هیپ رگلیسمی (ازدیاد قند خون) و بالنتیجه 
=== MON بالش ===
MON_part2.txt:1020:انجام دادن. غربالش کن: ۳ در جواب 
MON_part2.txt:2197:غلاله: (ه‌هاقاهر [ع. غلاله ] (۱.) بالشجه‌ای 
MON_part2.txt:30823:گردبالش: 4عت«. -.ع (امر.) بالشی کو چک و 
MON_part2.txt:31285:تنکك» رغیف. قرص نان. قرص. بالش گرد. 
MON_part2.txt:31297:گرده‌بالش: ۲0-0226 (امر.) متکای گر د؛
```


## [2026-09-05T06:23:56.769Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS index lines with 98/ ===\"; grep -n -E \"98/[0-9]\" SNS_pages.txt | head -20\necho \"=== SNS 'bal' words ===\"; grep -n -o -E \"b[aā]l[a-zšíīē]* [0-9]+/[0-9]+\" SNS_pages.txt | head -30",
 "description": "SNS index for page 98"
}
```


### [2026-09-05T06:23:56.824Z] TOOL RESULT

```
=== SNS index lines with 98/ ===
14854:                              vSsyas- 198/13
14909:                                                               barhis 98/11                nar 164/11
14920: trisata 88/21              298/19
14924:                                                               bhiraa- 67/4-98/19
14937: datra- 298/13          pancadasa 118/3
15043:  daraya, darayamiy- 298/19B
15048:                                     bardhanya- 98/14              haraa   47/1Q
15123: b5ma-, baraya- 98/19      raaretan-, raarata- 308/3               yazata majjra. spgnta-       rasta- 222/13
15151:                                                                   ra9a6- star- 41/15           vahyah- 198/13
15154:raaoiri- 248/5             yaozdaera- 334/11                       rapiewina- 225/18            var-/v3ra- 98/3-261/K
15205:                          paity-apara 116/6                  pixa- 143/16               baxs- 98/1
15213:                                                             pu0ra- 109/12-138/16       baraz- 98/9
15215:                                                             pOtay- 137/14              barazis 98/11
15242:caQwarasat 172/2      zaranya- 162/12                     e                              daffra- 298/13
15248:                      z^rad- 225/7                        er3yO- 183/2                   dalta- 298/17
15403:shr 199/11               why 198/14
15561:d'stn 298/20          dyw*r 190/3                                              J
15724:v6h 198/12-285/23
15725:vfihfln   198/17         vlstura 287/8                   Visp 273/12               v±a/ 279/11
15735:vShlh 198/20             vidaxtag 267/20                 vistarg 273/24            vuzurg 225/2-270/6
=== SNS 'bal' words ===
16508:balay 77/6
```


## [2026-09-05T06:23:57.934Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '26190,26200p' MON_part1.txt; echo \"-----\"; sed -n '20960,20975p' MON_part1.txt; echo \"----- budget\"; sed -n '26010,26022p' MON_part1.txt",
 "description": "Mo'in contexts"
}
```


### [2026-09-05T06:23:58.011Z] TOOL RESULT

```
شاش, ادرار. (مسص‌ل.) گمیز انداختن» 
شاشیدن. 

بولوار: ۰۷27 (.) میدان و خیابانی که 
باغجه‌ها و چمن‌ها و درختان سار دارد و 
محل گردش عموم است. بلوار. 


ترتیب دهند و آن 


-----

بالوس: 5 [- بالوس - بالوش - 
پالوش] (.) کافور مغشوش. 

بالوعه: (ع.] (.) چاهی که در آن 
آب باران و آب‌های فاسد ربخته شود چاه 
بالون: «ماقه (.) (فر.) کره‌ای بزرگک که 
پوشش آن از پارچه‌ای غر قبل نقوذ تدکیل 
شده و داخل آن را از گازهای سک 
صعو د کند. 

باله: (0-)0312 [- بال] (ا.) اندام‌های شنای 
ماهی» اعضای شناوری ماهی. 

بالیدن: 02۱7 [ - بالودن؛ نمو » شوک 
(مص‌ل.) (بالید» بالد» خواهد بالید» تال 
----- budget

نودحجه: 6[ (۱.) مسجموع در آمدها و 
هزینه‌های یکك کشورء یک وزارتخانه؛ 
یک اداره» یک موسسه و با شخص خاص؛ 
صورت برآورد جمع و خسرج یک 
وزار تخانه» یک اداره با یک نگاه. . ضح.- 
مادة اول قانون محاسبات عمومی مصوب 
۰ اسفند ۱۳۱۲ بودجه را چنین تعریف 
کر ده است: رو دجه لانحة پیش‌بینی کلبه 
عواید و مخارج است برای مدت بکسال 
شمسی (سنه مالی) که به تصویب مجلس 
شورای ملی رسیده باشد.»
```


## [2026-09-05T06:24:07.833Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"bar[a9ə]zis|barzis|barhis\" SNS_pages.txt SNS.txt | head\necho \"=== context around SNS body p98 ===\"\ngrep -n -E \"b[aā]l[iíī][sš]\" SNS_pages.txt | head -20",
 "description": "SNS body barazis"
}
```


### [2026-09-05T06:24:07.897Z] TOOL RESULT

```
SNS.txt:7142:"*». 950,barhis:^^ ba^iS-,^ " 
SNS.txt:28515:barhis 98/11 
SNS.txt:29442:barazis 98/11 
SNS_pages.txt:4613:                                                                                                         "*». 950,barhis:^^                 "
SNS_pages.txt:14909:                                                               barhis 98/11                nar 164/11
SNS_pages.txt:15215:                                                             pOtay- 137/14              barazis 98/11
=== context around SNS body p98 ===
```


## [2026-09-05T06:24:10.300Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '4595,4630p' SNS_pages.txt",
 "description": "SNS page 98 body"
}
```


### [2026-09-05T06:24:10.343Z] TOOL RESULT

```
     Y/YT ^   .* d la*j*.j3rfij'j>*<# :bamlgtar:
                                                                  V*r>                                                           *«*»> -A»ttor bar:
                                                                                     I
                                                                                                                                                          \y -»is
                                                                                                                                                 •r-r/viS -r6/r^


        ..i.T^b-jt   haraka   :   ***->^   <   J '*«* tf* 1   * o=j'/j j •**                                                           •^•^'^•i'Lrbaiay;           J^.
                                                                                                   ri/4A .              „




                                                                                                         ,„_            &*-cA«#sbaii5n: «X„
                                                                                                         "*». 950,barhis:^^                 "
                                                                                                                                                                                 .


      .jC****, :^V3 WiM>.1788-1789.}                                -*jMj
                                                                                                                                                   ba^iS-,^
                                                                                                                                       r-Y/r*   i,M.   M   , r/t   j

                                                                                                               MB            '   951) ?Bar
                                                                                                                                          3snQ-barasnav-:t„
                                               .4ii>ai-« r W'oW:bnn<           II

                                                              .Y1-Y*-U/1

                 U/T      ;ioUai


 1   ^\r (J-i)«/;'*S^ T '^-oWtcr-tf :bayyas..                            ,>..,
```


## [2026-09-05T06:24:25.879Z] TOOL CALL #27: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T06:24:25.886Z] TOOL RESULT

```


```


## [2026-09-05T06:24:29.105Z] TOOL CALL #28: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%B1%D8%B3%D9%85",
 "prompt": "Give the Persian entry برسم (barsam): etymology, meaning, and any Middle Persian/Avestan forms cited."
}
```


## [2026-09-05T06:24:31.121Z] TOOL CALL #29: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%D8%B4",
 "prompt": "Give the Persian entry بالش (bāleš) 'pillow': full etymology, Middle Persian, Avestan and Proto-Iranian/PIE forms cited, and any related بالین."
}
```


### [2026-09-05T06:24:33.476Z] TOOL RESULT

```
# Persian Entry: برسم (beresam)

Based on the Wiktionary page provided, here is the available information:

**Meaning:** The entry برسم functions as a verb form rather than a standalone lemma.

**Definition:** It represents the "first-person singular present subjunctive" form of the verb رسیدن (residan).

**Etymology & Historical Forms:** The page does not provide etymological information, Middle Persian cognates, or Avestan forms. Only the connection to the base verb رسیدن is documented.

**Note:** This is a non-lemma form, categorized as a Persian verb conjugation rather than an independent dictionary entry. To find fuller etymological details, one would need to consult the entry for رسیدن (residan) itself.
```


### [2026-09-05T06:24:37.300Z] TOOL RESULT

```
# Persian بالش (bāliš/bâleš) - Etymology & Related Terms

## Full Etymology

Per the Wiktionary entry, بالش derives from Middle Persian 𐭡𐭠𐭫𐭱𐭭 (bʾlšn' /bālišn/), which traces back through Proto-Iranian *barjíš and Proto-Indo-Iranian *bʰarȷ́ʰíš to Proto-Indo-European *bʰelǵʰ-.

## Middle Persian & Historical Forms

The Middle Persian ancestor is recorded as "𐭡𐭠𐭫𐭱𐭭 (bʾlšn' /⁠bālišn⁠/)" in the etymological chain, representing the intermediate stage between Classical Persian and older Indo-European roots.

## Proto-Iranian & PIE Roots

- **Proto-Iranian:** *barjíš
- **Proto-Indo-Iranian:** *bʰarȷ́ʰíš  
- **Proto-Indo-European:** *bʰelǵʰ-

## Related Term: بالین (bālīn)

The entry lists "بالین (bālīn / bâlin)" as a synonym for the Persian word meaning pillow/cushion, though no separate etymology for this variant is provided in the source material.
```


## [2026-09-05T06:24:42.336Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/barəsman",
 "prompt": "Avestan barəsman-: meaning and etymology (which PIE root), and descendants (Middle Persian barsom, Persian barsam)."
}
```


## [2026-09-05T06:24:43.393Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DB%8C%D9%86",
 "prompt": "Persian بالین (bālīn): etymology, Middle Persian and Avestan forms cited."
}
```


### [2026-09-05T06:24:44.162Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:24:49.667Z] TOOL RESULT

```
# بالین (Persian Word)

This Wiktionary entry documents a Persian noun with the following key information:

**Definition**: The term denotes "pillow" in an archaic sense, with modern speakers using the synonym بالش instead.

**Etymology**: The word "inherited from Middle Persian" with the reconstructed form bʾlyn' representing /balēn/, also meaning "cushion; pillow."

**Pronunciation**: Varies across Persian dialects—Classical Persian uses /baː.ˈliːn/, while Iranian formal speech renders it as /bɒː.líːn/. Tajik speakers pronounce it /bɔ.lín/.

**Transliteration**: The standard Persian reading is "bālīn," with Iranian variants written as "bâlin" and Tajik as "bolin" (болин in Cyrillic script).

The entry is categorized as an archaic Persian noun inherited from Middle Persian origins, indicating its historical rather than contemporary usage in modern Persian.
```


## [2026-09-05T06:24:55.956Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.iranicaonline.org/articles/barsom-avestan-baresman",
 "prompt": "Encyclopaedia Iranica article BARSOM: what is it, and what does it say about the etymology of Avestan barəsman- / Middle Persian barsom / Persian barsam?"
}
```


## [2026-09-05T06:24:56.536Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/boulevard",
 "prompt": "Etymology of boulevard, and also any entries shown for bulwark."
}
```


### [2026-09-05T06:24:57.829Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:25:05.162Z] TOOL RESULT

```
# Etymology of Boulevard and Bulwark

## Boulevard

The word "boulevard" entered English in 1769, referring to a "broad street or promenade planted with rows of trees." It derives from French *boulevard*, which originally meant "top surface of a military rampart" (15th century).

The French term came from a garbled adaptation of Middle Dutch *bolwerc* (fortification wall). Since French lacked the letter "w" at that time, the adaptation proved challenging, resulting in variant forms like *boloart* and *bollvercq*.

The semantic shift reflects an urban planning concept: "a promenade atop demolished city walls, which would be wider than the old streets." In the U.S., since 1929, the term has applied to "multi-lane limited-access urban highways."

## Bulwark

"Bulwark" is a doublet of boulevard, dating to the early 15th century. It originally denoted "a fortification outside a city wall or gate; a rampart, barricade," derived from Middle Dutch *bulwerke* or Middle High German *bolwerc*.

The term likely combines *bole* (plank or tree trunk, from Proto-Germanic *\*bul-*) with *werc* (work), creating "bole-work"—a construction of logs. By the mid-15th century, the word acquired figurative meaning: "means of defense or security."
```


## [2026-09-05T06:25:10.618Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/budget",
 "prompt": "Etymology of budget; also anything about the sense 'financial statement' and re-borrowing into French."
}
```


## [2026-09-05T06:25:11.080Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/baleen",
 "prompt": "Etymology of baleen; also balloon and ballot if shown."
}
```


### [2026-09-05T06:25:15.922Z] TOOL RESULT

```
# Etymology of Budget

## Origin and Development

The word "budget" originated in the early 15c. as "bouget," meaning a leather pouch or small bag. It derived from Old French *bougette*, a diminutive of *bouge* (leather bag), ultimately tracing back to Latin *bulga* and a Gaulish root meaning "to swell."

## Financial Meaning

The modern sense referring to fiscal planning emerged around 1733. This shift occurred because "the treasury minister keeping his fiscal plans in a wallet" inspired the metaphorical application to financial statements.

## Broader Usage

Between the late 16c. and 18c., the term also meant "a stock, store, or collection of miscellaneous items," and later developed the sense of "bundle of news"—which led to its adoption as a newspaper title.

## Re-borrowing into French

The source material does not contain information about budget being re-borrowed into French, so I cannot comment on that aspect based on this etymology dictionary entry.
```


### [2026-09-05T06:25:16.998Z] TOOL RESULT

```
# Etymology of Baleen

**Baleen** originates from Old French *balaine* (meaning "whale" or "whalebone") in the early 14th century. This term traces back through Latin *ballaena* to Greek *phallaina*.

The Greek root is thought to derive from *phallos* ("swollen penis"), potentially referencing a whale's body shape, combined with a feminine suffix. This connects to the Proto-Indo-European root *bhel-* meaning "to blow, swell."

Interestingly, the shift from Latin's *ph-* to *b-* suggests the word entered Latin through a third language, with scholars proposing Illyrian as the intermediary.

**Related words** sharing this etymological root include balloon, ballot, bold, bull, and bulge—many relating to round or swollen objects.
```


## [2026-09-05T06:25:21.807Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%AF%D8%AC%D9%87",
 "prompt": "Persian بودجه: etymology (from which language), meaning."
}
```


## [2026-09-05T06:25:22.597Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A8%D9%84%D9%88%D8%A7%D8%B1",
 "prompt": "Persian بلوار: etymology (from which language), meaning."
}
```


### [2026-09-05T06:25:25.011Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T06:25:25.778Z] TOOL RESULT

```
# Persian بودجه (budje)

**Etymology:** The word is "Borrowed from French _budget_."

**Meaning:** According to the Wiktionary entry, بودجه means "budget" — referring to an allocation of money or resources for a specific purpose. The example provided demonstrates usage: "بودجه دولت" (budje-ye dowlat) means "state budget."

The etymological path traces further back through French to English, ultimately deriving from Proto-Indo-European roots through Old French and Latin origins.
```


## [2026-09-05T06:25:34.246Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -E \"بالن|بال:\" MON_part1.txt | head -20\necho \"=== نهنگ context ===\"; grep -n \"نهنگ\" MON_part1.txt | head -10",
 "description": "Mo'in بالن whale"
}
```


### [2026-09-05T06:25:34.323Z] TOOL RESULT

```
1009:ابال: (28 [ع.] (.) ج. ابل» شتران 
10958:اسبال: لام [ع.] (مصل.) باران باریدن» 
12245:استقبال: ۶۱55۱ [ع.] (مصم.) طلب اقبال 
15289:اقبال: انب [ع.] (مص‌م.) روی آوردن؛ 
16986:بالنسبه بزرگ و قرمز رنگ است؛ رمان» 
20555:بماسکت بال: ۱29۲۰-121 [- سک تال ] 
20815:بال: اه (.) (جاد.) هر یک از اندام‌های 
20820:بال: ۰۶ (.) (جان.) یکی از پستانداران 
20827:پبال: !2" ريشة بالیدن و بالش. 
20829:بال: اقا (ع.] (.) حال» خاطر» دل. 
20832:بالا: ۰212 (ص‌فا.) بالنده؛ نمو کننده. (.) 
20876:بالان: «قاجه (ص‌فا. حا.) بالنده. در حال 
20939:بالنگ: 8 |[ - بارنگ ِ بادرنگ ۰ 
20949:بالنکو: مدز (.) (گیا.) گیاهی از تسره 
24762:بلبال: ۱۳2۱" (ع.) (.) شدت اندوه و غم 
24763:بسلبال: :۵" (ع.) (مسصل.) سخت 
26995:پیس بال: ۵5-2۱" (امر.) (ور.) بازیی است 
27492:برابر» همراه» طایق النعل بالنعل. 
28742:(بالید» بالد» خواهد بالید» بیال» بالنده» 
30534:گوشدار» ج. پرستاران. برستاران خبال: 
=== نهنگ context ===
4578:نوعی نهنگ (سوسمار) آمریکایی‌که طول 
20825:«نهنگ» خو انند و اشتاه است. 
21297:که تقاطر کند. بحر نهنگ آثار؛ (کد.) تیغ» 
43566:تمساح را مرادف با نهنگ دانسته‌اند» در 
43567:صورتی که نهنگ اسم عام بستانداران 
78206:ماهی با نهنگ و غیره که بر قبضة شمشیر 
78453:ماهی» سقنقر» نهنگ دشتی» ورل ماهی» 
81239:تمساح‌ها. ضح.- در برخی کتب کلمة نهنگ 
81241:است ولی باید دانست که نهنگ معمولاً
```


## [2026-09-05T06:25:36.923Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20813,20832p' MON_part1.txt",
 "description": "Mo'in بال entries"
}
```


### [2026-09-05T06:25:36.971Z] TOOL RESULT

```
رگم 

بال: اه (.) (جاد.) هر یک از اندام‌های 
قدامی جانوران ذیفقار (خزندگان؛ پرندگان» 
بستانداران) غیر از ماهی‌ها از کتف تا نو کث 
انگشتان؛ بر و بال» جناح. 

بال: ۰۶ (.) (جان.) یکی از پستانداران 
بحری» از راستهً آب‌بازان (شناگران) دارای 
سر حجیم و پهن و شکم صاف. طولش تا 
۰ متر و وزنش تا ۱۵۰/۰۰۰ کیلوگرم 
می‌رسد. ضح.- غالباً این جانور را بنام 
«نهنگ» خو انند و اشتاه است. 

پبال: !2" ريشة بالیدن و بالش. 

بال: اقا (ع.] (.) حال» خاطر» دل. 

پال: ۱" .) مجلس رقص» محل رقص. 
بالا: ۰212 (ص‌فا.) بالنده؛ نمو کننده. (.)
```


## [2026-09-05T06:25:45.900Z] TOOL CALL #40: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:256 2>&1 | head -60",
 "description": "Fetch Borhan-e Qate page 256"
}
```


### [2026-09-05T06:25:47.589Z] TOOL RESULT

```
no scan of BQT covers printed page 256 (see 'scans' in refs_online.json)
```


## [2026-09-05T06:25:52.799Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt; do echo \"== $f: lines=$(wc -l < $f) ff=$(tr -cd '\\f' < $f | wc -c)\"; done\necho \"--- برسم entry context ---\"; sed -n '18590,18615p' BQT_v1_pages.txt",
 "description": "BQT file structure and barsam entry"
}
```


### [2026-09-05T06:25:54.490Z] TOOL RESULT

```
== BQT_v1_pages.txt: lines=32485 ff=776
== BQT_v1.txt: lines=66791 ff=0
== BQT_alt_v1.txt: lines=61533 ff=0
--- برسم entry context ---
میشود . سفوف آنکرم شکم را میکشد و آنرا
بحریی جوزالایهل و ثمرتالمرعر خوانند ۴ .
پر سم ۴ - بروزن‌مرهم » شاخهای‌باريكث
بی که باشد بمقدار یك‌وجب که آنرا از درخت
هوم ببرند ؛ و آن درختی است شبیه بدرخت کز
و اکر هوم نباشد درخت کر و الا درخت انار ء
و رسم بریدن آن چنان است که اول کاردی که
دس آن هم‌آهن باشد و آنرا برسم چین خوانند
(۱) چك : ژند . ۱ "
۳۹ ۱9
مس زمزم نمایند بمتی دهایکه در وقت عبلدت
آش و بدن شستن و چیزی خوردن میخوانشد
بخوانند . و برسم را با برسم چین ببرندیس‌برسم
دانرا قیز آب گفتد و آن
ظرفی باشد مانشد قل‌دان وآنرا
از طلا و نفره و امشال آن
مازند » و برسمهارا اسدرون
آن گذارند » و حرگاه خواعند
بدن بشوبند باچیزی بخورند با
زد (۱) ععنی قسمی از اقسام
کتابهای زند (۱) بخوانند چند
عدد از آن برس که بجهت آن
کار وآن فعل معین است بدست
گیرند, چنانچه بجهت خوادن
سك وندیداد که یکی از
۳ - رگ : بوس .
```


## [2026-09-05T06:26:01.754Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=18597{n+=gsub(/\\f/,\"\")} END{print \"formfeed page idx:\", n+1}' BQT_v1_pages.txt\necho \"--- print that page ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==295' BQT_v1_pages.txt | tail -30",
 "description": "Locate BQT page for barsam"
}
```


### [2026-09-05T06:26:03.471Z] TOOL RESULT

```
formfeed page idx: 477
--- print that page ---
باگد همجنانکه دایا» بمعنیباست » مثل اشکه
و بی حساب .
ابیادی - می وزن پرراری . نوعی اژ :
کبوثر باشد - و جنسی از بافته - و جامةٌ بسیار
تازك حم هست ۵ .
ی
) بو قلمون > بنتم فاف و لام ؛ بمنی
بوقلمونت و آن نوعی از دیبای رومی. باشد که
هر ژمان برنگی تماید - و جاتوری نیز هست
شبیه بچلپامه - و کنابه از مردمی است کدهر
ساعت خود را برنگی بارایند (۳) - و کنابه‌از
دناهم هست - و علم مرغی نیز شده است ۴ -
و اهل مشرق سنکه پشت راکویند .
ایهل ین اول و حای هوز و کون
| فید‌اك ‏ با دال ابجد ‏ بروزن پربزاد
پیتی ظلم و مثم و پیداد پاش ما
الیو - بر وزن دیر » بلفت زند وپازند
(۵). بمعنی پیراهن‌است وبعربی« قمیس»خوانند.
الیژ ه یر وزن تمیز ۰ شرارة آکش دا
۷
)۱( خم ۳ : و. )۱( خم۳ : عبری. (۳) چك : ساراید .
(4) چك , چب : بر. (م) چك : زند وباژند .
۱ - از لاتتی 3۱01۳060 « لفت نامه *. ۴ رگ : بوفلمون .
۴ - مفینه 5۵0102 , نوعی از عرعی و سروکوهی وکو کلانو وری و ارس و آورین
۲7 دلفت‌نامه ». مای موز ۹۵102 101۳6۳۵5[ «نایتی .۱۵٩‏ ۴ - پپلوی
6 با 32۷1 < باروچا ۵۰0 » 206 < اونوالا ۷۷ > :
آبی‌حکم شرع آب خوردن خطاست اگرخون بنتوی بربزی رواست تت:
۵ - و نیز اییاری منسوب باببار است » قربه ای بجزیر؛ بنی صرمیان مصر و اسکندربه
« ممجم‌البلدان >. ۱ - ابیز وآمیزوآیید وایید وایر ویر وآییژدآیر وصوردیگر مصحف
این کلمه‌اند < لفت نامه *.
```


## [2026-09-05T06:26:17.594Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=18597{n+=gsub(/\\f/,\"\")} END{print n}' BQT_v1_pages.txt\npython3 - <<'EOF'\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\n# find chunk containing برسم entry\nfor i,ch in enumerate(data):\n    if 'برسم چین خوانند' in ch:\n        print('chunk',i)\n        print(ch[:3000])\n        break\nEOF",
 "description": "Print BQT chunk with barsam"
}
```


### [2026-09-05T06:26:19.235Z] TOOL RESULT

```
476
chunk 476
" بر‌سان « بنتح اول می وزن نرسان :
دوشاب میاء رنگه خوشبوی را گویند - و مطلق
امت را لیز کفته‌اند از هر پیعمبی که باشد ٩‏ -
وکروه آدمپان را هم - و بکسر اول نیز آمده
است - و بضم اول اژدها را کویند .
پر سر آ هدن - کنابه ازغلبه وافزونی
و زبادئی کردن باشد . ۳
بر ص‌غنچه - نم او و غن‌قلمدار,
تضم سرو کوعی باشد و آن سیاه رنکه و فربه
میشود . سفوف آنکرم شکم را میکشد و آنرا
بحریی جوزالایهل و ثمرتالمرعر خوانند ۴ .
پر سم ۴ - بروزن‌مرهم » شاخهای‌باريكث
بی که باشد بمقدار یك‌وجب که آنرا از درخت
هوم ببرند ؛ و آن درختی است شبیه بدرخت کز
و اکر هوم نباشد درخت کر و الا درخت انار ء
و رسم بریدن آن چنان است که اول کاردی که
دس آن هم‌آهن باشد و آنرا برسم چین خوانند
(۱) چك : ژند . ۱ "
۳۹ ۱9
مس زمزم نمایند بمتی دهایکه در وقت عبلدت
آش و بدن شستن و چیزی خوردن میخوانشد
بخوانند . و برسم را با برسم چین ببرندیس‌برسم
دانرا قیز آب گفتد و آن
ظرفی باشد مانشد قل‌دان وآنرا
از طلا و نفره و امشال آن
مازند » و برسمهارا اسدرون
آن گذارند » و حرگاه خواعند
بدن بشوبند باچیزی بخورند با
زد (۱) ععنی قسمی از اقسام
کتابهای زند (۱) بخوانند چند
عدد از آن برس که بجهت آن
کار وآن فعل معین است بدست
گیرند, چنانچه بجهت خوادن
سك وندیداد که یکی از
۳ - رگ : بوس .
بقه از مضه ۲۵۵
( برهان فاطع ۳۷ )
مسعز
```


## [2026-09-05T06:26:26.018Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nch=data[476]\nprint(ch[3000:8000])\nEOF",
 "description": "Rest of BQT chunk 476 (footnotes)"
}
```


### [2026-09-05T06:26:27.736Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T06:26:30.922Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\ndata=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (477,478,479):\n    print('=== chunk',i,'===')\n    print(data[i][:2500])\nEOF",
 "description": "Next BQT chunks for footnotes"
}
```


### [2026-09-05T06:26:33.688Z] TOOL RESULT

```
=== chunk 477 ===
ده
نسکهای عشهور زند )۱( آست سی و پنج برسم
بدست گیرید ؛ و بجهت نك بشت ٩‏ بیست
وچهار برسم, وهنگلم بدن شتن وچیزی خوردن
و عیادت کردن پنج برسم ؛ و چون یکبار
نگ وندیداد خوانده‌شودآن برسمپا باطل گردد؛
و از جهت :سکهای دیگر و افمالی که مذکور
شد اختیار دارند ء خواهند با همان برسمها عمل
کنند و خواهند برسم نازه بدست گیرند . و از
شروط برسم بدست گرفتن بدن شستن وجامةٌ باله
پوشیدن است . و صاحب فرهنکه جپانگیری
کوید این لفت را از مجوسی که در دین خود
بغامت فاضل ود و آردشیر نام داشت و او را
مجوسان موید میدانستند و درعهدا کیر پادشاه از
کرمان بهندوستاي آمده بود تحفیق نمود » اما
درچند نخه از فرحتگههسروری‌توشته‌اند که‌برسم
ککایی است که آ تش‌پرستان درحین پرستش بردست
گیرند مگر. در يك دخه که کیاهی لوشنه شده
بود واین‌را با آنچه درفرهنگه
جهانگیری نوشته اند فی‌الجمله
تردیکی است وان اعلم .
برسم چین ه باجيم
فارسی بروزن فروردین , کاردی
بود که دستآنهم از آهن باشد
و فارسان بدان برسم از درخت
برند ؟ . #
(۱) چك : ژند .
برشیان دارو:
بر سق له - بروزن مرغوله . قرسی‌باشد
که در آن جوز و پزباز و بنگه و دیگی ادوبه
کر مکنند و خورلد .
بر سیا نا بفتح‌اول وسکون ثانیو کسر
الت و بای حطی وتون‌هردو بالف کشیده .رستنی
باشد که تخم آن‌مانندنخم کرفی‌است۴ .علت‌جرب
را نافع باشد .
بر شان باشین نفطه‌دار بروزن افشان.
+معنی اعت باشدمطلفاً از عرییغمب رکه باشد ۴ .۶
بر شا - با خای قطه‌دار بروزن کرپلاه
نم موضعی است میان ابران وتوران » و باینممنی
یبای خای قطدار چم هم آمده است ٩‏ .
۰ بر شتخحان - بر وزن کهکشان » بمعنی
برشضا است که نام حوضمی باشد میان ابران
وتوران»و باین‌معنی بجای‌خا جیم هم بنظر آهده
اس ۵ .
بر شده (۲) ه بمعنی بالارفته و بلندشده
باشد .
بر شکستی - کنابه از اعراض نمودن
و ترگدادن - و وا گذاشئن - و بر کشئن باشد .
بر شو ۵ - بر وزن موسوم ۰ بلغت احل
نجد نوعی از خرمای خشكث باشد .
بر شیان‌دادو - بکر اك رتتالی
بالف کذینه و نون زده » دارومی است که آرا
۷۵۹-۸ .
15 ویروشنیکان ( . رد ؛برپر‌وشان و برسان.
۴ رك : مزدبنا
۴ - مسحف « برروشنان »
=== chunk 478 ===
می شیر آن" زین نهادن
سرخ‌مرد گوبند و بعربی عصا الراعی خوانندا ۰
بر شیر فرد ین نهادن - کنابه از
تهایت غالب شدن - و افزولی و زبادنی کردن
بر صحر انهادن هه کنانه از آشکار
و غلعر ساختن خاشد *
بر صیصا ‌ مشپور است. 1 او عابدی
بودة در تهامت خدایرستی . عاقبت ازشیطان فرب
خورده کمراه شظ .
بر ظاس - باطای حظی بروزن کربای,
نم شهری است از ولامت تی کستان . گوبندرویاء
آنجا پوست خوب میدارد و پوست آن رویاه را
نیز پرطلی میگونند ؛ و با.بای فارسی هم آمده
لت ۴ .
یراق نهادن » یمنی بمربة اعنی
رساتیدن ‏ و کنابه ازتركگدادن - و فراموش کردن
هم حست 4 :
بر طا نیقی » بکر نون و سکون بای
حطی و قلف بتحتانی‌رسید. ۰ بلفت بوتانی ؟ کلی
کویند تخم بان افروز است .
فرطایل- بکر تحتانی و سکون لام»
ظ‌جزیرماست‌در حتدوستان کهاز یکی ازدرختان
بت ۳۵۸ ‌-
آن جزیره بانگی عظیم و صدایی ههیپ‌می آبذ ,
و بضی کویند کوهی است در آن جزبر هکه‌شبها
از آن کوه صدای طبل و دهل و سنج میآید .
بر طیسقون - بختح اول و سکون ثانی
و اث بتحتاتی دسیده و بین بی‌نفطهٌ زده و ضم
فاف و واو و نون ساکن ؛ بلقت بونالی گل‌سرخ
را کویند و بعربی طی‌الاحمر خوانند » وبهترین
وی آن بودکه از مصر آورند » و آن قایم مقام
گل‌مخنوم است .
یرم ۴ ۰ تم اول و سکون ثامی و غين
نقطمدار ۰ شدی باشد که از چوب و خاشاكوخاله
وگل در پیش آب بندند » و بفتح اول و کسر
ثانی هم کفته‌اند . و بفتح اول و تالی‌هم‌ینآمده
است. و باین معنی بازای‌نقطه‌دار نیز درست‌است.
بر غاب * - بروزن غرقاب » بند آب‌است
یعنی جایبکه پیش آبرا بندند تا آب در آن
جمع شود .
برست ۲ - بر وزن سرمست .کیاهی
جوی‌آب رود و آنرا مج هگونند ویعربی‌قنابری
و عملول و تملول و شجردالبهق خوانند ۰۷
وبعنی گوبن دگیاهی است که کل‌زردی داردو آ ترا
«لكثاص ۰۲۱۵ . ۲ واگ ناس :
دزی ۱ : ۰*۷۳
۴ - بیواانی 9۳60۵1016 «لك ۱ص ۲۰۵»
شّه ازسفحهٌ ۲۵۷
=== chunk 479 ===
-- ۷6 سس
بیشتراوفات‌بخر وکاو دهند» وبخورند وبسنی‌دمگر
گفته‌اند ترمایست بپاری و طعم تیژی دارد » تازهٌ
آنرا بپزند وبخورند و چون‌خشك شودبخر و کاو
دهند - و جل وزغ را نیز کویند و آن چیزی
ماشد سب که بر دوی آبهای استاده می‌استد -
بحانب زراعت بر ند ۰
بر غالا فیفان « بالامبروزن‌خرچرانیدن,
بمعتی برانگیختن و تحریض نمودن شخصی باشد
برغهان » بامیم بروزن همزبان. سار
بز رکه و اژدها را گویند .
برغندان - بر وزن د:ندان» جشن
ونشاطی را گوبند که بسبب‌ترديك شدن ماءرهضان
در آخر های شعبان کنند . و بسنی گوبند نام
روز اخر ماه شمبان است ۰ و باین هعنی بجای
حرف الث قاف هم آمده است .
و عو ‏ منم اول بروزن پرکو » شاخی
باشد مان تهی که درا مانند نضر نوازند .
۰ ‌ ۳
برغوفی ۴ «بانی مثلله بر وزن
سر کوشی ۰ تخمی است که آنرا بفارسی اسفیوش
: مرفره
وبعربی‌بز رقطوها ومشیراژی‌بشکووییوفانی‌فلیون #
خوائند .
برغول س با واومجهول بروزن مرغول»
حلوابی را گوبند که از آرد پزند و آنرا افروشه
نیز خوانند - و کندمی را گون دکه درهم‌شکته
باشند - و هرچیزی که آنرا درهم کوفه باشندد
و آشیکه از کندم دلیده کرده‌پزند ؛ و بدوممنی
آخر بضم اول هم آعده است . #*
بر قاب ۴ هبافا بروزن مهتاب. ممروف
است که آب برف و آب سرد باشد - و کنابه
از آب دهان است که وفت خوردن شخصی‌چیزی
را سیب میل و خواهش طبیمت در دهن‌دیگری
مرگردد و گاه باخد که از دهن یرون آید وی
اختیار بر رد ۰
بر ف آب‌دادن - کنابه از دل سرد
کردن و ناامید ساختن باشد.
رفر « بر وزن صرصر » بیعنی خان
و شوکت و علو در و حنزلت باشد ٩‏ .
بر فر وشان ۱ بروزن برده بوشان.
بمعنی بربروشان است که امت مینمبر باشد .
برفره - بر وزن شه‌تره ۰ بمعنی برقر
باشد که شان و شوکت و عظمت امت ۷ .
۴ . را: برقندان.
۴ - م رکب از : برف + آب .
از ؛: بر فر (فره ‏ خره) .
۲ رکه : برفر .
1 0216» برنی ۷2/۲ , نطنزی ۷۵۲۲
فریزندی بهر دو صورت «کك. ۱ ص ۲۸۵ ۰
سمناتی ۰۷۵۶ ۷۵2۲۵ » سنگری ۷۵۲۲ ۰
۲ 3 شهمیرزادی ]087 دکت, ر۳۵
۶ »: ادکاشمی و نگلجی 2۹ عنجی
2 بودغا ۱۷۲10 « گربرسن ۱۰۱ ؛
```


## [2026-09-05T06:26:53.002Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== WLD Bd2 bhelgh / barzis ===\"; grep -n -i -E \"bhelgh|barezis|barzis|barhis\" incoming/WLD/WLD_Bd2_pages.txt | head -15\necho \"=== IEC ===\"; grep -n -i -E \"bhelgh|barezis|bāliš|balis\" IEC.txt | head -10\necho \"=== SYN pillow ===\"; grep -n -i -E \"^19\\.2|pillow\" SYN.txt | head -10",
 "description": "Walde-Pokorny, Mann, Buck"
}
```


### [2026-09-05T06:26:53.076Z] TOOL RESULT

```
=== WLD Bd2 bhelgh / barzis ===
11798:     bhelgh „schwellen“, ^bhlcg'^ ds.
11912:   Zur Yermittlung der obigen Bedeutungen mit den u. bhelgh- „schwellen'‘
11922:182                                        bhel-    — bhelgh
11970:bhelgh- ..willkommen, gut: bewillkommnen'*?
11975:bhelgh ,,schwellen; Balg (aufgeblasene Tierhaut), Kissen, Bolster' (Erw.
11977:     Ai. barhis- n. ,,Streii, Opferstreu**           = av. barezis- n.        ,,   Bolster, Kissen", np.
11999:+    710- s;     vielleicht            hat auch       ai.    barhis-^     av.    barezis-     idg.       -i-s-     als   Erw.
=== IEC ===
1212:bhelghó ‘roar’ Skt. barhami; MHG er-bëlgen; E bellow, id.
1488:bholghis, io ‘bolster, litter. WP II, 183 Skt. barhís “bed of kusa-grass'; Av. barozis "mat LW in Arm. bardz (i-st. ‘cushion, pad"); Per. balis, balin ‘cushion’; Srb. blàzina *cush- ion, bolster’; OPr. balsinis (for *balzinis *cushion). (For a semantic link w. Cz. blázen
=== SYN pillow ===
6545:: ON koddi ‘pillow’, OE codd ‘bag, pod’ (ME cod rarely ‘belly’ or ‘testicle’), prob. Lat. (fr. Oscan) botulus ‘sausage’, all with common notion of ‘swollen, rounded’ object. Walde-P. 1.671. Falk- Torp 606. Feist 390.
12084:5. Goth. badi, ON bedr (‘bed’ and ‘pillow’; Dan. bed only ‘bed?’ in the gar- den), Sw. bédd, OE bedd, ME, NE, Du. bed, OHG betti, beti, MHG bette, bet, NHG bet, the most widespread Gme. word, best explained as orig. ‘dug-out place, den, lair’ for man and beast : Lat. Jodere ‘dig’, W. bedd ‘grave’, etc. Walde- P. 2.188. Walde-H. 1.542. Falk-Torp
19710:OE codd ‘bag’, NE cod formerly freq. as ‘purse’: Du. kodde ‘testicle’, ON koddi ‘pillow’, etc. Falk-Torp 558. NED s.v. cod sb.!.
32965:19.21 PEOPLE (POPULACE)
33009:19.22 A PEOPLE, NATION
33036:19.28 TRIBE, CLAN, FAMILY (in Wide Sense)
```


## [2026-09-05T06:26:54.358Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index ===\"; grep -n -i -E \"BARSAM|BALESH|BALIS|BALIN|BHELGH|BHEL\" incoming/ARY/ARY_latin_index_pages.txt | head -20",
 "description": "Aryanpur index"
}
```


### [2026-09-05T06:26:54.422Z] TOOL RESULT

```
=== ARY latin index ===
3043:BALESHT AFGHAND) () gil BAREZISH s(AVESTAN) gis 9\
3045:BARHISH, BARISHN BALESHT, BALIN
3046:BULGA (ULEX(GREEK) gly BALISH PAHLAVI) «5 Shy
```


## [2026-09-05T06:27:03.899Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3035,3050p' incoming/ARY/ARY_latin_index_pages.txt\necho \"--- page tag ---\"\nawk 'NR<=3046 && /\\[pdf page/{p=$0} END{print p}' incoming/ARY/ARY_latin_index_pages.txt\necho \"=== ARY persian بالش ===\"; grep -n \"بالش\" incoming/ARY/ARY_pages.txt | head -8",
 "description": "Aryanpur context"
}
```


### [2026-09-05T06:27:05.850Z] TOOL RESULT

```
MACKENZIE: (STATURE) 134, BERG, :(OLD HIGH GERMAN) op gist
(HEIGHT) 117 BURG, BERGAZ,
BUCK: 23, 852 BERG, BURG (GERMAN) lat
TYR VOR ST e+ abl oy BEORG «(OLD ENGLISH) 5, ,-Sil
setlaal
10935405 Sb S 23s onl owe
sel aly gaat jl pt Sy gdb
ip thy CAFU oF
BALESHT AFGHAND) () gil BAREZISH s(AVESTAN) gis 9\
(SANSKRIT) ey Sule OLD PERSIAN) ihuel, go 3h,
BARHISH, BARISHN BALESHT, BALIN
BULGA (ULEX(GREEK) gly BALISH PAHLAVI) «5 Shy
BALGS GOTHIC) Si BAZ AOSSETIC) ga)
we
[pdf page 108]
i!
--- page tag ---
[pdf page 107]
=== ARY persian بالش ===
202:از بررسی زبالشناختی برای یافت گهواره‌ی هندو اروپائیان چه دتایچی گرفته
10076:7۸ اس ند بالشلشت۸ ۳۲1 : 5 ,لنشت[521
11922:7 بالشا پروسی کهن ((۲8-954 ۰:00 18۸
```


## [2026-09-05T06:27:18.567Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -A6 \"^bloom, n\" KLN_1971.txt | head -20\necho \"---\"; grep -n -A6 \"^bulk, n\" KLN_1971.txt | head -25\necho \"--- SKT bole/bloom/bulk ---\"; grep -n -i -E \"^Bloom|^Bulk|bulki\" SKT.txt | head -10",
 "description": "Klein bloom and bulk"
}
```


### [2026-09-05T06:27:18.641Z] TOOL RESULT

```
30922:bloom, n., flower. — ME. blome, fr. ON. blom, 
30923-blomi, which is rel. to OS. blomo, Du. bloem, 
30924-OHG. bluoma (fern.), bluomo (masc.), MHG. 
30925-bluome (masc. and fern.), G.Blume (fem.), Goth. 
30926-bldma, ‘flower, blossom’, OE. blostm, blostma, 
30927-‘blossom’, and cogn. with OIr. blath, ‘bloom, 
30928-flower’, L. fids , ‘flower’, florere, ‘to blossom, 
--
30939:bloom, n., rough mass of wrought iron. — OE. 
30940-bldma , ‘a lump of metal’, of uncertain origin, 
30941-bloomer, n., a costume for women. — Named 
30942-after the inventor Mrs. Amelia Jenks Bloomer of 
30943-New York (in 1851). 
30944-
30945-bloomer, n., a blunder. — Of uncertain origin, 
---
35107:bulk, n., size, volume; cargo of a ship. — ME. 
35108-bulke, prob. a blend of ON. bulki, ‘carge’, and 
35109-OE. biie, ‘body, belly’. ON. bulki, is rel. to ON. 
35110-bollr, ‘a ball’, fr. I.-E. base *bhel-, ‘to swell’; 
35111-see bull, ‘the male of a bovine animal’, and cp. 
35112-ball, ‘a round body’, bold. For the etymology 
35113-of OE. buc see buck, ‘the body of a wagon’. 
--
35115:bulk, n., projection from a shop. — ME. balk , 
35116-bolk , fr. OE. balca, ‘beam’. See balk and cp. 
35117-next word. 
35118-
35119-bulkhead, n. — Compounded of bulk, ‘projection’, 
35120-and head. 
35121-
--- SKT bole/bloom/bulk ---
1337:bulk  (3\  the  stall  of  a  shop.  (Scand.) InSb.  — Iccl.^J/ir,  a  l>eam;  also,  a  inanition ^pronounced  with  d  like  ow  in  e^t/)i  see Balk,  above.  Der.  bulk-kesuiy  a  partition. Ball  (O,  a  dance.  (F.-LowL.)  F./W.- Low  L.  bailarty  lo  dance.  ^Gk.  ^aAAi^''ffU'f to  dance.
1992:bloom,  a  flower.  (Scand.)  M.  E.  bhme ; not  in  A.S.  —  lcel.  bUm^  bldmi,  a  ilowcr; Swed.  bhmma  ;  Dan.  bUmmt.^Vi^^.  btotm  ; Colli.  bloma\  L,.^os;  »ec  Flower.
2415:BULK.
19265:architect.  (F.  ->  L.  «  Gk.)  F.  artkt- tt<tt.  —  L.  architectuj,  the  same  as  anc*> /^r/tfH.  — Gk.  dpxiW«Taft%  a  chief  builder  Of artificer.  —  Gk.  'ip^i-,  chief  vsec  Arolu-); W«ra>f,  a  carpenter,  bulkier.  ^Scc  alsu Text.)
```


## [2026-09-05T06:27:34.381Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%D8%B4' --note 'page 84, root Bhel/Bhelgh, node 6: Persian بالش bāleš < MP bālišn < PIr *barjíš < PIE *bʰelǵʰ-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DB%8C%D9%86' --note 'page 84, node 5/6: Persian بالین bālīn < MP bālēn cushion, pillow' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/boulevard' --note 'page 84, nodes 7-10: boulevard < F boulevard < MDu bolwerc; bulwark = bole+work' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/budget' --note 'page 84, nodes 16,20-23: budget < OF bougette dimin. of bouge < L bulga (Gaulish); financial sense 1733' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://www.etymonline.com/word/baleen' --note 'page 84, nodes 16-19: baleen < OF baleine < L ballaena < Gk phallaina via Illyrian; PIE *bhel-' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%AF%D8%AC%D9%87' --note 'page 84, node 23: Persian بودجه borrowed from French budget' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-05T06:27:37.799Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/6d359aca76cdd63f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d6e35f915815eca0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1cafbbcba9b31d0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/da7ecfec1606b0f3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0e11c6a598d92f1f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/54350504e71712f2.txt
```


## [2026-09-05T06:27:47.907Z] TOOL CALL #51: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-05T06:27:47.943Z] TOOL RESULT

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


## [2026-09-05T06:28:24.023Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==132' POK_01.txt | grep -n -i -E \"bhel|blühen|gedeihen|blóm|blom\" | head -10",
 "description": "Pokorny p.122 bhel- bloom"
}
```


### [2026-09-05T06:28:25.552Z] TOOL RESULT

```
4:Dazu  4.  hhel-  , blühen'  usw.  und  die  Erweiterungen  hhelgh-,  hhUdh^^ bhlegu-,  hhlei-,  bJileu-  ^schwellen'  usw.
6:4.  hhel-   und    bhle-,   bhlö-,   ibJWs-   , Blatt,    Blüte,  blühen;    üppig  sprießen'
8:Gr.  g)vXXov  , Blatt'  {*bhHiom)j  lat.  folium  ds. ;  mir.  bileöc  ,Blättchen'  (aua *6i7e  <  *bhelio-)]  hierzu  wohl  air.  bile  n.  ,Baum';
9:hhle-j  meist  bhlö-  in:  lat.  flös,  -iHs  m.  ,Blume';  flöreö,  -ere  , blühen';  0  k. Fluusai  ,Flörae',  Fluusasiais  ,Flörälibus',  sabin.  Flusare  ,Flöräli'.
10:Mir.  bläth  m.  , Blüte,  Blume',  cymr.  blaivd^  acorn.  blodon  ,Blüte'  (*bhlö  t-\ mbret.  (mit  -wen-Suffix)  bleuzven,  nbret.  bleufi(v)enn  ds.,  mit  ö'-Ableitun^r mhd.  bluost  , Blüte',  nhd.  Blust,  ags.  blöstma,  blösma,  blöstm  ,Blume',  an. blömstv  ds.,  ndl.  blasen  , blühen'  (=  mnd.  blasen  ,erröten',  s.  u.  bhles- ,glänzen') ;
11:got.  blöma  m.,  ahd.  bluomo  m.  ,Blume',  aisl.  blomi  m.  ds.,  blöm  Kollek- tiv ,Blume';
12:ahd.  bluojen,  bluoiven,  as.  blöjan,  ags.  blötoan  ,blühen';  ahd.  bluot  f. ,das  Blühen,  Blüte'  =  ags.  bled  f.  ,Sproß,  Zweig,  Blume,  Frucht';  aber got.  blöp  n.,  aisl.  blöd,  as.  ags.  blöd,  ahd.  bluot  ,Blut'  wohl  zu  *bhel~e- , sprudeln'.
16:5.  bhel-,    meist   mit   -5^- (-£-) Suffix    ,Bohle,   Balken':    bh^lQg-,    bb^lQ-n-g-r
17:bheleg-',  bblk-.
18:Einfaches  bhel-  in  ai.  bhurijäu  Du.  ,Arme,  Deichselarme';  gall.  *balä- kon  ,(Mauer-)Vorsprung',  cymr.  balog  , Zinne'  (M.-L.  890).
```


## [2026-09-05T06:28:59.478Z] AGENT

Now I'll write the verification file.


## [2026-09-05T06:39:03.015Z] TOOL CALL #53: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk84.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_BALESH = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%D8%B4\"\nW_BALIN  = \"https://en.wiktionary.org/wiki/%D8%A8%D8%A7%D9%84%DB%8C%D9%86\"\nE_BOUL   = \"https://www.etymonline.com/word/boulevard\"\nE_BUDG   = \"https://www.etymonline.com/word/budget\"\nE_BALEEN = \"https://www.etymonline.com/word/baleen\"\nW_BUDJE  = \"https://en.wiktionary.org/wiki/%D8%A8%D9%88%D8%AF%D8%AC%D9%87\"\n\nnodes = []\n\nnodes.append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"barez; bara-s-man\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Two different things are packed into one box. (a) Av. barəsman- n. 'bundle of twigs used in the Yasna' is real and well attested (Bartholomae, AiW col. 949 f.); Bartholomae takes it from Iranian *barzman- and expressly connects it with Skt. barhis- 'sacrificial straw' ('die Etymologie von b. weisen darauf hin, dass der Gebrauch des B. sich aus dem Spreiten der Opferstreu (ai. barhisah starima) entwickelt hat'), i.e. with the *bhelgh-/*bhel- 'swell, strew, pad' family, and Pokorny p.120 s.v. '3. bhel-, bhle- aufblasen, aufschwellen' lists it there explicitly, following Thieme ZDMG 92, 47 f.: 'nach Thieme hierher av. bar-s-man- Buendel von Zweigen, ai. barsva Wulst, Zahnfleisch (Lw. aus av. *barsman Polster)'. Nourai's odd hyphenation 'bara-s-man' is copied straight from Pokorny's 'barə-s-man-'. So this word under this root is exactly Pokorny's own analysis. (b) 'barez: to grow' is Av. barəz- (AiW col. 950: '1barəz- V., nur mit us: in die Höhe gehen, aufwachsen'; '2barəz-: bərəz- Adj. hoch, erhaben; Höhe, Berg'), which Bartholomae himself derives from IE *bhereǵh- : *bhrǵh- (whence NP burz, buland, bālā) — Pokorny 140, a DIFFERENT root from *bhel-. Modern handbooks are split on barəsman-: those who follow Thieme/Pokorny keep it with *bhelǵh-, those who follow the older analysis take it from barəz- 'be high'. Either way, Nourai's box conflates the two roots, so the node is compatible with, but not identical to, the standard picture.\",\n \"derivation_fa\": \"در این خانه دو مطلب جداگانه در هم آمیخته است. یکم: «برسمن» اوستایی barəsman- «دستهٔ ترکه‌های آیینی» واژه‌ای است شناخته و بارتولومه (ستون ۹۴۹) آن را از ایرانی باستان *barzman- می‌گیرد و آشکارا با سنسکریت barhiṣ- «کاه قربانی» می‌سنجد؛ پوکورنی نیز در ص ۱۲۰ ذیل ریشهٔ bhel- «باد کردن، آماسیدن» و به پیروی از تیمه همین واژه را آورده است، پس ذکر آن زیر این ریشه درست و برگرفته از خودِ پوکورنی است. دوم: barez «رستن» همان barəz- اوستایی است که بارتولومه (ستون ۹۵۰) آن را از هندواروپایی *bʰerǵʰ- «بلند» می‌داند (خاستگاه «برز»، «بلند» و «بالا» در فارسی نو) و ریشه‌ای جداگانه است. بنابراین ادعای نورایی با احتیاط پذیرفتنی است: برسمن آری، ولی barez به ریشهٔ دیگری تعلق دارد.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:120\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 130 (printed p.120), entry '5.[=3.] bhel-, bhle- aufblasen, aufschwellen, sprudeln, strotzen': 'nach Thieme (ZDMG. 92, 47 f.) hierher av. barə-s-man- ‚Buendel von Zweigen‘, ai. barsva m. Pl. ‚Wulst, Zahnfleisch‘ (Lw. aus av. *barsman ‚Polster‘)'. Nourai's word, gloss and hyphenation come from this line. The page says nothing about 'barez to grow'.\"},\n   {\"ref\": \"BQT:256\", \"status\": \"partial\", \"note\": \"BQT_v1_pages.txt chunk 476 (page bearing 'بقیه از صفحه ٢٥٥' = continued from p.255, so this is printed p.256, signature 'برهان قاطع ٣٧'): the headword 'برسم – بروزن مرهم، شاخهای باریک ... که آنرا از درخت هوم ببرند' is there with the full Zoroastrian description, but Borhan/Mo'in give no Avestan form on the page (Mo'in's footnote only refers to his own مزدیسنا), so it supports the word, not the Avestan etymology.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"cols. 949-950 s.v. barəsman-\", \"stance\": \"partial\", \"note\": \"'j. barasman- n., meist kollekt. Sing., Bezeichnung eines beim Gottesdienst gebrauchten Zweigbuendels'; footnote: 'Der Terminus techn. fuer das Buendeln des B. ist √star- stemere. Dies sowie die Etymologie von b. weisen darauf hin, dass der Gebrauch des B. sich aus dem Spreiten der Opferstreu (ai. barhisah starima) entwickelt hat'; 'Aus ir. *barzman-'. Same column-neighbourhood also has '1barəz- ... in die Hoehe gehen, aufwachsen' and '2barəz- hoch, erhaben ... Idg. *bh(e)rǵh-', i.e. a separate root.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 182-183 (WLD_Bd2_pages.txt l. 11975 ff.)\", \"stance\": \"partial\", \"note\": \"'bhelgh schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster (Erw. ...)' with 'Ai. barhis- n. Streu, Opferstreu = av. barezis- n. Polster, Kissen, np. bālis Kissen' — Walde-Pokorny keep barhis-/barəzis- here but do not list barəsman-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhel-2\", \"stance\": \"silent\", \"note\": \"AHD_watkins1985.txt l.328: bhel-2 lists only Germanic, Greek and Latin reflexes; no Iranian material at all.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §64 (p.174) and §74 (H.200)\", \"stance\": \"supports\", \"note\": \"'phl. paz. barsum aus *barsm = zd. baresma (np. barsam ist Parsenwort)' — Huebschmann derives the Pahlavi/Persian word from Av. barəsman-.\"}\n ]\n})\n\nnodes.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"barsum\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian barsom /barsom/ <blswm>, Manichaean <brswm>, 'the bunch of twigs used in the Yasna ceremony' (MacKenzie, CPD p.18). It continues Av. barəsman- through Old Iranian *barzman-: the cluster -sm- was broken by an anaptyctic -u-, exactly as Hübschmann formulates it (Pers. Stud. §64, 'Vokaleinschub im Inlaut'): 'phl. paz. barsum aus *barsm = zd. barəsma', on the same footing as hēzum 'firewood' < *ēzm = Av. aēsma- and ustur 'camel' < *ustr = Av. uštra-. The variant with -o- (barsom) is the reading MacKenzie prints; Nourai's barsum is the Pāzand/older transcription used by Hübschmann. Nourai's gloss 'branches, twigs' is right.\",\n \"derivation_fa\": \"«برسم» فارسی میانه barsom (نوشتار پهلوی blswm، مانوی brswm) به معنی «دستهٔ ترکه‌هایی که در آیین یسنا به کار می‌رود» (مکنزی، فرهنگ کوچک پهلوی ص ۱۸). این صورت دنبالهٔ barəsman- اوستایی از راه ایرانی باستان *barzman- است؛ در خوشهٔ پایانی ‑sm‑ واکهٔ میانجی u افزوده شده است. هوبشمان (پژوهش‌های فارسی، بند ۶۴) همین را می‌گوید: «phl. paz. barsum از *barsm = زند barəsma»، درست مانند hēzum «هیزم» از *ēzm و ustur «اشتر» از *uštr. پس ادعای نورایی درست است؛ تنها گونهٔ خوانش (barsum در برابر barsom) اختلافی صوری است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:256\", \"status\": \"partial\", \"note\": \"Same page as node 1 (BQT_v1_pages.txt chunk 476, printed p.256). Borhan's برسم entry describes the object and its ritual use but prints no Pahlavi form; the Pahlavi barsum is not on the page.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.18 s.v. barsom\", \"stance\": \"supports\", \"note\": \"PHD.txt l.252: 'barsom [blswm | M brswm] the bunch of twigs used in the Yasna cere-mony.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §64, p.174\", \"stance\": \"supports\", \"note\": \"'§ 64. a) u eingeschoben in: phl. paz. barsum aus *barsm = zd. baresma (np. barsam ist Parsenwort)'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II (glossary)\", \"stance\": \"silent\", \"note\": \"grep -i 'barsom|barsum' over NYB_vol2_glossary.txt returned no usable hit (OCR of the glossary is very noisy in the b- range).\"}\n ]\n})\n\nnodes.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"barsam\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP برسم barsam 'the bundle of twigs (originally of the hōm plant, otherwise tamarisk or pomegranate) held by the priest during the Yasna', continuing MP barsom without further change beyond the regular MP -o- / NP -a- fluctuation in this learned word. Hübschmann (§64) marks it explicitly as a 'Parsenwort', i.e. a term kept alive by the Zoroastrian community and taken over into literary Persian from the priestly tradition rather than inherited through ordinary popular transmission — which is why the -rs- cluster survives unaltered. Ferdowsī's line quoted in the chart (گرفت از پی واژ برسم بدست) shows it in the Shāhnāma; Borhan-e Qāte‘ p.255-256 gives the same ritual description.\",\n \"derivation_fa\": \"«برسم» در فارسی نو همان دستهٔ ترکه است که موبد در آیین یسنا به دست می‌گیرد و برهان قاطع (ص ۲۵۵–۲۵۶) شرح مفصل آن را آورده است. این واژه بی‌واسطه دنبالهٔ barsom فارسی میانه و در نهایت barəsman- اوستایی است؛ اما هوبشمان (بند ۶۴) آن را «واژهٔ پارسیان» (Parsenwort) می‌خواند، یعنی وام‌واژه‌ای از سنت دینی زردشتی در فارسی ادبی، نه واژه‌ای که از راه تحول عادی و مردمی به فارسی رسیده باشد؛ به همین سبب خوشهٔ ‑رس‑ دست‌نخورده مانده است. شاهد فردوسی («گرفت از پی واژ برسم بدست») کاربرد آن را در شاهنامه نشان می‌دهد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:256\", \"status\": \"supports\", \"note\": \"BQT_v1_pages.txt chunk 476 = printed p.256 (it carries 'بقیه از صفحه ٢٥٥' and the signature 'برهان قاطع ٣٧'): 'برسم – بروزن مرهم، شاخهای باریک ... بمقدار یک وجب که آنرا از درخت هوم ببرند' and, on the following column, the rules for holding 35 / 24 / 5 barsam twigs — exactly Nourai's gloss.\"},\n   {\"ref\": \"SNS:103\", \"status\": \"supports\", \"note\": \"SNS_pages.txt index (l.16391 ff.): 'barsum dan 103/7', 'barsum I apadyab 103/9', 'barsum I 7 tag 103/11'; the body entry ':barsam/barsum:' stands at SNS_pages.txt l.4709. Tavoosi's glossary treats the word on exactly the page Nourai cites.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §64 p.174; index H.200\", \"stance\": \"partial\", \"note\": \"'np. barsam ist Parsenwort' — same etymology, but Huebschmann warns that the NP form is a learned/priestly transmission, not an ordinary inherited word.\"},\n   {\"src\": \"BQT\", \"where\": \"vol. 1, printed p.255-256\", \"stance\": \"supports\", \"note\": \"see ref_check; also the neighbouring headword 'برسم چین ... کاردی بود که دسته آن هم از آهن باشد و پارسان بدان برسم از درخت برند'.\"},\n   {\"src\": \"PHD\", \"where\": \"CPD p.18\", \"stance\": \"supports\", \"note\": \"'barsom ... the bunch of twigs used in the Yasna ceremony' — the direct MP antecedent.\"}\n ]\n})\n\nnodes.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"baraziš, barašnav\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The first word is right and is the core of the whole branch: Av. barəziš- n. 'Polster, Kissen' (Bartholomae AiW col. 950, with the Vendīdād passages), = Skt. barhis- 'sacrificial straw, litter', and Bartholomae himself adds 'np. bālis Kissen. — Pü.: bālisn'. Pokorny puts precisely this pair under bhelǵh- at p.125-126: 'bhelgh- schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster (Erw. von bhel- aufblasen usw.). Ai. barhiš n. Streu, Opferstreu = av. barəziš- n. Polster, Kissen, npers. bālis Kissen'. The second word, barašnav, is Av. barəšnav-/barəšnu-, and it does NOT mean 'cushion, pillow': Bartholomae (col. 951) glosses it 'Höhe, Scheitel' ('height, crown of the head'), the word behind the Zoroastrian baršnūm purification (MacKenzie: 'baršnūm, the major purification ritual'). Hübschmann is Nourai's actual source for the pairing: 'bālis Kissen, phl. bālisn ..., zd. barəzis; phl. bālīn a summit, the crown of the head ..., zd. barəšnu- Höhe, Gipfel (aus *barz-nu-)'. So Nourai has silently carried the gloss 'pillow' over from the first word to the second, and *barz-nu- belongs rather with *bherǵh- 'high'. Compatible picture, imprecise gloss — hence 'plausible'.\",\n \"derivation_fa\": \"واژهٔ نخست درست است: barəziš- اوستایی «بالش، تشک» (بارتولومه، ستون ۹۵۰، با شواهد وندیداد)، برابر با barhiṣ- سنسکریت «کاه قربانی»؛ خودِ بارتولومه در پی آن می‌افزاید «np. bālis، پهلوی bālišn». پوکورنی هم در ص ۱۲۵–۱۲۶ ذیل *bʰelǵʰ- «آماسیدن؛ خیک، بالش» همین جفت را آورده است. اما واژهٔ دوم، barašnav، همان barəšnu-/barəšnav- اوستایی است و معنای آن «بلندی، فرقِ سر» است (بارتولومه ستون ۹۵۱)، نه «بالش»؛ همین واژه ریشهٔ آیین برشنوم است. مأخذ نورایی در این‌جا هوبشمان است که می‌نویسد: «bālis «بالش»، پهلوی bālišn، زند barəzis؛ پهلوی bālīn «قله، فرقِ سر»، زند barəšnu- «بلندی» از *barz-nu-». پس نورایی گلوسِ «بالش» را نابه‌جا به واژهٔ دوم نیز تعمیم داده و افزون بر آن *barz-nu- به ریشهٔ *bʰerǵʰ- «بلند» تعلق دارد. ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"POK:125\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 135, entry beginning at printed p.125 and running onto 126: 'bbelgh- schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster (Erw. von bhel- aufblasen usw.). Ai. barhiš n. Streu, Opferstreu = av. barəzis- n. Polster, Kissen, npers. bālis Kissen; ai. upa-barhana-m ... Decke, Polster'. Exactly Nourai's arrow for barəziš-; the page does not mention barəšnu-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AiW cols. 950-951\", \"stance\": \"partial\", \"note\": \"col. 950: 'j. barəziš- n. Polster, Kissen ... ai. barhiš n. Opferstreu, np. bālis Kissen; vgl. ai. upabarhana- n. Polster. — Pü.: bālisn.' — supports the first word; but barəšnu- is entered separately in col. 951 as 'Höhe, Scheitel', not 'cushion'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p. 182-183\", \"stance\": \"supports\", \"note\": \"'bhelgh schwellen; Balg ..., Kissen, Polster. Ai. barhis- n. Streu, Opferstreu = av. barezis- n. Polster, Kissen, np. bālis Kissen' (WLD_Bd2_pages.txt l.11975-11977).\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, s.v. bholghis\", \"stance\": \"supports\", \"note\": \"IEC.txt l.1488: 'bholghís, io bolster, litter. WP II, 183 Skt. barhís bed of kusa-grass; Av. barozis mat, LW in Arm. bardz (cushion, pad); Per. balis, balin cushion; Srb. blàzina cushion, bolster; OPr. balsinis'. Mann even puts NP bālīn here, not with barəšnu-.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. bhelgh-\", \"stance\": \"partial\", \"note\": \"'bhelgh-. To swell. Extension of bhel-2 ... 4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE. [Pok. bhelgh- 125.]' — same root and same Pokorny page, but Watkins prints only the western reflexes.\"}\n ]\n})\n\nnodes.append({\n \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"bâlîšn, bâlěn\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Pahlavi forms are attested and both are Nourai's, not inventions. (a) MP bālišn <bʾlišn / 𐡡𐠠𐡫𐡱𐡭> 'cushion, pillow' < Old Iranian *barǡiš- (= Av. barəziš-): the change is the regular Middle Persian one of *-rǡ- / *-rz- > -l- (Hübschmann §157 'Ap. rd (= idg. rd, rdh, rgʰ, rǵʰ) = np. l', with sāl 'year', bālā 'height', buland, and 'bālis Kissen, zd. barəzis-' in the same list), plus the abstract suffix -išn; MacKenzie's edition prints the shorter bāliš. (b) MP bālēn <bʾlyn'> 'cushion, pillow' and also 'top, peak' (MacKenzie CPD p.17, two entries), from *barz-nu- = Av. barəšnu- 'height, crown of the head', so that bālēn originally denoted what lies under the crown of the head. Both are the direct antecedents of NP بالش and بالین.\",\n \"derivation_fa\": \"هر دو صورت پهلوی واقعی‌اند. یکم: bālišn پهلوی «بالش، متکا» از ایرانی باستان *barźiš- (اوستایی barəziš-)؛ خوشهٔ ‑رز‑ ایرانی باستان در فارسی میانه به ل بدل شده است — همان قاعده‌ای که هوبشمان در بند ۱۵۷ برمی‌شمارد («سال»، «بالا»، «بلند»، «bālis کیسن، زند barəzis-») — و پسوند اسم‌ساز ‑شن بدان افزوده شده. مکنزی صورت کوتاه‌ترِ bāliš را ضبط کرده است. دوم: bālēn پهلوی «بالش» و نیز «قله، فرقِ سر» (مکنزی، ص ۱۷، دو مدخل)، از *barz-nu- برابر با barəšnu- اوستایی «بلندی، فرقِ سر»؛ یعنی آنچه زیرِ فرقِ سر می‌نهند. این دو، سرچشمهٔ مستقیم «بالش» و «بالین» فارسی نو هستند. ادعای نورایی درست است.\",\n \"sources\": [W_BALESH, W_BALIN],\n \"ref_check\": [\n   {\"ref\": \"SNS:98\", \"status\": \"supports\", \"note\": \"SNS_pages.txt: the Avestan index has 'barəzis 98/11', 'barhis 98/11', 'barəz- 98/9' (l.14909, 15213-15215), and the body page (SNS_pages.txt l.4595-4620) shows the Pahlavi headword 'bali5n' [= bālišn] cross-referenced to Bartholomae '950, barhis / barəziš-', immediately followed by '951) ?Barəšnū-barašnav-'. Tavoosi p.98 is thus exactly the page that gives Nourai both bālišn and the form 'barašnav' of node 4.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie CPD p.17 s.v. bālēn, bāliš\", \"stance\": \"supports\", \"note\": \"PHD.txt l.244-249: '1bālēn [bʾlyn'] top, peak.' / '2bālēn [bʾlyn' | N bālīn] cushion, pillow.' / 'bāliš [bʾlišn' | N ~] cushion, pillow.'\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien §157 and the b- list\", \"stance\": \"supports\", \"note\": \"'bālis Kissen, phl. bālisn Gl. and Ind. 76, zd. barəzis; phl. bālīn a summit, the crown of the head, zd. barəšnu- Höhe, Gipfel (aus *barz-nu-)' — Huebschmann has the very form bālišn Nourai prints.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II\", \"stance\": \"silent\", \"note\": \"grep for 'balisn|balen|balis' in NYB_vol2_glossary.txt gave no readable hit; the OCR of Nyberg's glossary is too damaged in this range to judge.\"}\n ]\n})\n\nnodes.append({\n \"id\": 6, \"lang\": \"Persian\", \"words\": \"bâleš\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP بالش bāleš 'pillow' is the straight continuation of MP bālišn, with loss of the final -n of the suffix; Wiktionary gives the chain بالش < MP 𐡡𐠠𐡫𐡱𐡭 (bʾlšn' /bālišn/) < Proto-Iranian *barjíš < Proto-Indo-Iranian *bʰarǵʰíš < PIE *bʰelǵʰ-, i.e. exactly Nourai's route and exactly Pokorny's bhelǵh-. The doublet بالین bālīn (the chart's 'extra'), now archaic and largely poetic, continues MP bālēn. The Ferdowsī line quoted in the chart (سرانجام خشتست بالین تو) shows the bālīn form in the Shāhnāma. Both are thus reflexes of Av. barəziš-/barəšnu- and cognate with Skt. barhis-, Old Prussian balsinis 'cushion', Serbo-Croat blàzina, Gothic balgs 'bag'.\",\n \"derivation_fa\": \"«بالش» فارسی نو دنبالهٔ بی‌واسطهٔ bālišn فارسی میانه است با افتادن ن پایانی؛ ویکی‌واژه همین زنجیره را می‌دهد: بالش ← فارسی میانه bālišn ← ایرانی آغازین *barjíš ← هندوایرانی آغازین *bʰarȷ́ʰíš ← هندواروپایی آغازین *bʰelǵʰ-، یعنی درست همان راهی که نورایی رسم کرده و همان که پوکورنی زیر bhelǵh- آورده است. گونهٔ دوگانهٔ آن «بالین» (که در نمودار به عنوان صورت افزوده آمده) دنبالهٔ bālēn پهلوی است و امروز کهن‌گرا و بیشتر شعری است؛ بیت فردوسی «سرانجام خشتست بالین تو» همان را نشان می‌دهد. هم‌ریشه‌های آن سنسکریت barhiṣ-، پروسی کهن balsinis «بالش» و گوتی balgs «خیک» است. ادعای نورایی درست است.\",\n \"sources\": [W_BALESH, W_BALIN],\n \"ref_check\": [\n   {\"ref\": \"POK:125\", \"status\": \"supports\", \"note\": \"Pokorny p.125-126 s.v. bhelgh- names the Persian outcome directly: 'npers. bālis Kissen' beside 'av. barəzis- n. Polster, Kissen'.\"},\n   {\"ref\": \"SNS:98\", \"status\": \"supports\", \"note\": \"Same page as node 5; Tavoosi's entry bālišn on p.98 is glossed by the Avestan barəziš- with Bartholomae col. 950, which is the etymology Nourai carries down to NP bāleš.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, b- list (H.172) and §157\", \"stance\": \"supports\", \"note\": \"'balis Kissen H. 172' in the list of NP words continuing OP b; and §157 'bālis Kissen, zd. barəzis-; phl. bālīn a summit, zd. barəšnu- (aus *barz-nu-)'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. bholghis\", \"stance\": \"supports\", \"note\": \"'Per. balis, balin cushion' listed among the reflexes of bholghís 'bolster, litter'.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt, pdf page 107-108\", \"stance\": \"supports\", \"note\": \"Aryanpur's Latin index groups exactly this family on one page: 'BAREZISH (AVESTAN) / BARHISH (SANSKRIT) / BALISH (PAHLAVI) / BALESHT, BALIN / BULGA / BALGS (GOTHIC)' with cross-references to MACKENZIE and BUCK.\"},\n   {\"src\": \"PHD\", \"where\": \"CPD p.17\", \"stance\": \"supports\", \"note\": \"'bāliš [bʾlišn' | N ~] cushion, pillow' — MacKenzie explicitly equates the MP word with the New Persian one.\"}\n ]\n})\n\nnodes.append({\n \"id\": 7, \"lang\": \"Middle German\", \"words\": \"bole; balle\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Nourai is transcribing Watkins/AHD verbatim: under bhel-2 'to blow, swell', AHD 1.e has 'Middle High German bole, beam, plank: (BOULEVARD), BULWARK' and 3.d has 'Middle High German balle (> Italian balla, palla), ball: BALLOON, BALLOT; PALL-MALL'. Both words are real MHG (bole 'plank' < Gmc *bul-, o-grade *ball- in balle 'ball'). Two reservations: (i) the book's language label 'Middle German' is loose for 'Middle High German'; (ii) the immediate donor of French boulevard is Middle Dutch/Middle Low German bolwerc, not the MHG word — Klein s.v. bulwark: 'ME. bulwerk, fr. MLG. (= Du.) bolwerk, which is rel. to MHG. bolwerk, G. Bollwerk, Swed. bolverk. These words lit. mean bole work', and Etymonline likewise derives boulevard from Middle Dutch bolwerc. Since the MHG and MDu words are the same compound in two dialects, the arrow is right in substance but not in the detail of the dialect.\",\n \"derivation_fa\": \"نورایی در این‌جا عیناً از واتکینز/AHD نقل می‌کند: زیر ریشهٔ bhel-2 «باد کردن، آماسیدن» آمده است «آلمانی میانهٔ علیا bole «تیر، تخته» ← BOULEVARD, BULWARK» و «آلمانی میانهٔ علیا balle «گوی» (← ایتالیایی balla, palla) ← BALLOON, BALLOT». هر دو واژه در آلمانی میانه واقعی‌اند. دو نکته: نخست آنکه برچسب «آلمانی میانه» به‌جای «آلمانی میانهٔ علیا» بی‌دقت است؛ دوم آنکه سرچشمهٔ بی‌واسطهٔ boulevard فرانسوی، صورت هلندی میانه/آلمانی سفلای میانهٔ bolwerc است نه صورت آلمانی علیا (کلاین ذیل bulwark و اتیمانلاین هر دو چنین می‌گویند). چون این دو در حقیقت یک ترکیب در دو گویش‌اند، جهت اشتقاق درست است ولی جزئیات گویشی دقیق نیست. ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [E_BOUL],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.328/330, s.v. bhel-2: '1.e Middle High German bole, beam, plank: (BOULEVARD), BULWARK' and '3.d Middle High German balle (> Italian balla, palla), ball: BALLOON, BALLOT; PALL-MALL'. Nourai's box is a direct transcript of these two lines.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. bulwark, ball\", \"stance\": \"partial\", \"note\": \"KLN_1971.txt l.35193: 'bulwark ... fr. MLG. (= Du.) bolwerk, which is rel. to MHG. bolwerk ... These words lit. mean bole work'; l.25205: 'ball ... ME. balle, fr. ON. bollr, which is rel. to OHG. ballo, balla, MHG. balle, bal, G. Ball, fr. I.-E. base *bhel-, to swell'.\"},\n   {\"src\": \"POK\", \"where\": \"printed p.120-121\", \"stance\": \"supports\", \"note\": \"under 3. bhel- 'aufblasen, aufschwellen': 'aisl. bulr, bolr m. Baumstamm, Rumpf, mnd. bole f. Planke (nhd. Bohle)'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. Ball (3), Balloon, Ballot\", \"stance\": \"supports\", \"note\": \"SKT.txt l.1356: 'Balloon, Ballot; see Ball (3)'; l.1352 derives F. ballotte from F. balle, listed in Skeat's appendix 'FRENCH FROM OLD HIGH GERMAN: ... ball (2), balloon, ballot ...'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 8, \"lang\": \"French\", \"words\": \"boulevard\",\n \"verdict\": \"plausible\",\n \"derivation\": \"French boulevard, 15th c., earliest forms boloart, bollvercq, boulevert, balouart, originally 'the flat top surface of a rampart'. It is a garbled adaptation of Middle Dutch bolwerc 'bulwark' — garbled because Old French had no /w/, so the Germanic -werc was resolved as -vart/-vard. The modern sense arose in 18th-c. Paris, when the demolished city walls were turned into tree-lined promenades wider than the old streets. Nourai's arrow (from the Germanic 'bole' word) is correct in substance; the strictly correct donor dialect is Middle Dutch (Klein, Etymonline), while AHD, which Nourai is following, cites Middle High German bole and refers boulevard to bhel-2 + werg- 'to do'.\",\n \"derivation_fa\": \"«بولوار» فرانسوی در سدهٔ پانزدهم میلادی با صورت‌های کهن boloart, bollvercq, balouart به معنی «سطح فوقانی بارو» پدیدار شد. این واژه، وام‌گیریِ دگرگون‌شدهٔ bolwerc هلندی میانه («بارو») است؛ چون فرانسوی آن روزگار واج /w/ نداشت، بخش پایانی ‑werc به ‑vart/‑vard بدل شد. معنای امروزی در سدهٔ هجدهم در پاریس پدید آمد، آنگاه که باروهای ویران‌شده به گذرگاه‌های درخت‌کاری‌شده و پهن بدل شدند. جهت اشتقاقی که نورایی رسم کرده در اصل درست است، اما وام‌دهندهٔ دقیق هلندی میانه است نه آلمانی علیا؛ نورایی از AHD پیروی کرده که این واژه را زیر bhel-2 به‌علاوهٔ werg- «کار کردن» آورده است. ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [E_BOUL],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt index l.1314: 'BOULEVARD bhel-2, werg-'; the root entry bhel-2 1.e lists BOULEVARD under Middle High German bole.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. boulevard\", \"stance\": \"partial\", \"note\": \"KLN_1971.txt l.32365: 'boulevard, n. — F., earlier boloart, boulevert, balouart, belouart, orig. meaning work of fortification, fr. MDu. bolwerc. See bulwark.' — Middle Dutch, not Middle German.\"},\n   {\"src\": \"WEB\", \"where\": \"grep of WEB_vol1.txt\", \"stance\": \"silent\", \"note\": \"no usable 'boulevard' entry recovered from the OCR of Webster vol. 1.\"}\n ]\n})\n\nnodes.append({\n \"id\": 9, \"lang\": \"Persian\", \"words\": \"bŭlvâr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP بلوار bolvār (also spelled بولوار) is a 20th-century direct loan from French boulevard, taken in during the Reza Shah period together with the town-planning concept itself (the wide tree-lined avenue). Mo‘in's dictionary enters it as بولوار with the French tag and the definition 'میدان و خیابانی که باغچه‌ها و چمن‌ها و درختان سایه‌دار دارد و محل گردش عموم است', with the cross-reference 'بلوار'. French [bul-] is rendered بولـ/بلـ and the final -vard as -وار, the -d being dropped exactly as in the French pronunciation.\",\n \"derivation_fa\": \"«بلوار» (و به املای دیگر «بولوار») وام‌واژه‌ای است مستقیم از فرانسوی boulevard که در سدهٔ چهاردهم خورشیدی همراه با خودِ مفهوم شهرسازیِ خیابان پهنِ درخت‌کاری‌شده وارد فارسی شد. معین آن را با نشانِ [فر.] و با تعریف «میدان و خیابانی که باغچه‌ها و چمن‌ها و درختان سایه‌دار دارد و محل گردش عموم است» ضبط کرده و صورت «بلوار» را نیز آورده است. آوای فرانسوی [bul‑] به «بول‑/بل‑» و پایانهٔ ‑vard به «‑وار» بدل شده و دالِ پایانی مانند تلفظ فرانسوی نیفتاده بلکه اصلاً تلفظ نمی‌شود. ادعای نورایی درست است.\",\n \"sources\": [E_BOUL],\n \"ref_check\": [\n   {\"ref\": \"MON:605\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi: MON_part1.txt l.26193-26195 'بولوار: boulevard (.) میدان و خیابانی که باغچه‌ها و چمن‌ها و درختان سایه‌دار دارد و محل گردش عموم است. بلوار.' The available OCR is of the 2-vol. abridgement, so the exact page 605 of the 6-vol. edition cannot be verified, but the entry and the French origin are confirmed.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. بولوار\", \"stance\": \"supports\", \"note\": \"see ref_check; the headword carries the Latin-script French lemma 'boulevard'.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"grep of 'بلوار' in Aryanpur's Indo-European root dictionary gives nothing — as expected, since it is a modern European loan, not an inherited word.\"}\n ]\n})\n\nnodes.append({\n \"id\": 10, \"lang\": \"English\", \"words\": \"boulevard\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English boulevard is a straight borrowing of French boulevard, first recorded 1769 in the sense 'broad street or promenade planted with rows of trees'; in the U.S. from 1929 it also covers multi-lane limited-access urban highways. The word is a doublet of the inherited-Germanic bulwark, which came into English in the early 15th c. from Middle Dutch bulwerke / MHG bolwerc.\",\n \"derivation_fa\": \"«boulevard» انگلیسی وام‌واژه‌ای است مستقیم از فرانسوی که نخستین بار در ۱۷۶۹ میلادی به معنی «خیابان پهن یا گذرگاهی که ردیف‌های درخت در آن کاشته‌اند» ثبت شده و در آمریکا از ۱۹۲۹ بر بزرگراه‌های شهری نیز اطلاق می‌شود. این واژه دوگانهٔ (doublet) واژهٔ bulwark است که در آغاز سدهٔ پانزدهم از هلندی میانهٔ bulwerke یا آلمانی میانهٔ علیای bolwerc به انگلیسی راه یافته بود. ادعای نورایی درست است.\",\n \"sources\": [E_BOUL],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt index l.1314 'BOULEVARD bhel-2, werg-'; root entry bhel-2 1.e '(BOULEVARD), BULWARK'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. boulevard, bulwark\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt l.32365 and l.35193; Klein makes boulevard and bulwark the same compound 'bole work'.\"},\n   {\"src\": \"SKT\", \"where\": \"grep of SKT.txt\", \"stance\": \"silent\", \"note\": \"Skeat's Concise has no 'boulevard' headword (only bulwark-related 'sconce' material turned up in the grep).\"}\n ]\n})\n\nnodes.append({\n \"id\": 11, \"lang\": \"Italian\", \"words\": \"palla, pallone; ballotta\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Italian palla / balla 'ball' is a Germanic loan (Langobardic or Frankish *balla, the o-grade *bhol- of the root; AHD prints 'Middle High German balle (> Italian balla, palla)'). Two Italian derivatives matter here: pallone, with the augmentative suffix -one, 'big ball', and ballotta, the diminutive of balla, 'little ball' — so called from the small balls dropped into the urn in Venetian and Genoese voting, whence the political sense. Nourai's glosses ('ball'; 'a small ball used for voting') are exactly Klein's.\",\n \"derivation_fa\": \"واژهٔ ایتالیایی palla/balla «گوی» وام‌واژه‌ای ژرمنی است (لُمباردی یا فرانکیِ *balla، از پایهٔ o‑دارِ ریشه)؛ واتکینز می‌نویسد «آلمانی میانهٔ علیا balle ← ایتالیایی balla, palla». دو مشتق آن در این‌جا اهمیت دارد: pallone با پسوند بزرگ‌ساز ‑one «گویِ بزرگ»، و ballotta مصغّرِ balla «گویچه» که نام گویچه‌های رأی‌گیری در ونیز و جنوا بود و از همین راه معنای سیاسی «رأی» یافت. گلوس‌های نورایی دقیقاً همان‌هایی است که کلاین می‌آورد. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:102\", \"status\": \"supports\", \"note\": \"The root entry (AHD_watkins1985.txt l.330) has '3.d Middle High German balle (> Italian balla, palla), ball: BALLOON, BALLOT'. The page number 102 refers to the A-Z body of the AHD New College Edition (the b-a- range, where BALLOON and BALLOT stand); that volume is lending-only on archive.org and could not be opened, but the root-appendix content is verified here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. balloon, ballot\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt l.25275 'balloon, n. — F. ballon, fr. It. pallone, which is formed with augment. suff. -one fr. palla, a ball, a word of Teut. origin'; l.25284 'ballot, n. — F. ballotte, fr. It. ballotta, little ball, dimin. of balla, ball ...; so called in allusion to the small balls formerly dropped into the voting urn'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. ballot\", \"stance\": \"supports\", \"note\": \"SKT.txt l.1352: 'ballot. (F.-O.H.G.) F. ballotter, to choose lots. — F. ballotte, a little ball used for voting; dimin. of F. balle, a ball.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 12, \"lang\": \"French\", \"words\": \"ballon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"French ballon 'large ball, balloon' is borrowed from Italian pallone; the initial p- was replaced by b- under the influence of the native French balle 'ball' (itself the same Germanic word). Klein states this explicitly. From the 1780s (Montgolfier) the word acquired the aerostatic sense that then travelled on into English and Persian.\",\n \"derivation_fa\": \"«ballon» فرانسوی «گویِ بزرگ، بالون» وام‌گرفته از pallone ایتالیایی است؛ پِ آغازین زیر تأثیر واژهٔ بومیِ فرانسوی balle «گوی» (که خود همان واژهٔ ژرمنی است) به ب بدل شده — کلاین این نکته را صریح می‌آورد. از دههٔ ۱۷۸۰ و آزمایش‌های برادران مونگلفیه، این واژه معنای «بالونِ هوایی» یافت و با همین معنا به انگلیسی و سپس به فارسی رفت. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:102\", \"status\": \"supports\", \"note\": \"AHD index l.1276 'BALLOON bhel-2'; root entry bhel-2 3.d lists BALLOON under MHG balle > It. balla, palla. The dictionary page 102 itself (New College Edition body) is not accessible online.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. balloon\", \"stance\": \"supports\", \"note\": \"'balloon, n. — F. ballon, fr. It. pallone ... The b in F. ballon (fr. It. pallone) is due to the influence of F. balle, ball.'\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. balloon\", \"stance\": \"supports\", \"note\": \"SKT.txt l.1345: 'balloon, a large ball. (F.-Ital.-O.H.G.) Formerly ballon, a ball used in a game'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 13, \"lang\": \"Persian\", \"words\": \"bâlon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP بالون bālon (variant بالن) 'balloon' is a modern loan from French ballon, taken over in the Qājār period with the technology itself. Mo‘in's entry prints the French lemma in Latin script and tags it [فر.] = French: 'بالون: ballon (.) (فر.) کره‌ای بزرگ که پوشش آن از پارچه‌ای غیرقابل نفوذ تشکیل شده و داخل آن را از گازهای سبک ... صعود کند'. French nasal -on is rendered by Persian -ون / -ن, and the chart's numbering 'بالن ١' distinguishes it from the homograph 'بالن ٢' 'whale' of node 18.\",\n \"derivation_fa\": \"«بالون» (و گونهٔ «بالن ۱») وام‌واژه‌ای نو از فرانسوی ballon است که در دورهٔ قاجار همراه با خودِ فناوریِ بالون وارد فارسی شد. معین آن را با صورت لاتینِ ballon و نشانِ [فر.] چنین تعریف می‌کند: «کره‌ای بزرگ که پوشش آن از پارچه‌ای غیرقابل نفوذ تشکیل شده و داخل آن را از گازهای سبک ... صعود کند». واکهٔ خیشومی ‑on فرانسوی در فارسی به «‑ون/‑ن» بدل شده است. شمارهٔ «۱» در نمودار برای جدا کردن آن از هم‌نگارِ «بالن ۲» به معنی «نهنگ» (گرهٔ ۱۸) است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"MON:467\", \"status\": \"supports\", \"note\": \"MON_part1.txt l.20966: 'بالون: ballon (.) (فر.) کره‌ای بزرگک که پوشش آن از پارچه‌ای غر قبل نقوذ تدکیل شده ...' — Mo'in's own [فر.] tag confirms the French origin. Exact page 467 of the 6-vol. edition could not be checked (only the 2-vol. abridgement is on disk).\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. بالون\", \"stance\": \"supports\", \"note\": \"see ref_check; MON_part2.txt l.23320 also has 'کشتی هوایی: بالن (بالون)، سفینهٔ هوایی', showing both spellings side by side.\"},\n   {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no entry for بالون; Aryanpur covers inherited Indo-European vocabulary only.\"}\n ]\n})\n\nnodes.append({\n \"id\": 14, \"lang\": \"English\", \"words\": \"balloon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English balloon (1570s of a ball used in a game, from 1783 of the aerostat) is from French ballon, itself from Italian pallone; Klein and Skeat agree, and Watkins refers it to bhel-2 through Middle High German balle. Nourai's arrow French > English is the standard one.\",\n \"derivation_fa\": \"«balloon» انگلیسی (نخست در دههٔ ۱۵۷۰ به معنی گویی که در بازی به کار می‌رفت و از ۱۷۸۳ به معنی بالونِ هوایی) از ballon فرانسوی و آن از pallone ایتالیایی است؛ کلاین و اسکیت هم‌داستان‌اند و واتکینز آن را از راه balle آلمانی میانهٔ علیا به ریشهٔ bhel-2 بازمی‌گرداند. پیکانِ «فرانسوی ← انگلیسی» که نورایی کشیده همان مسیر متعارف است. ادعای نورایی درست است.\",\n \"sources\": [E_BALEEN],\n \"ref_check\": [\n   {\"ref\": \"AHD:102\", \"status\": \"supports\", \"note\": \"AHD index l.1276 'BALLOON bhel-2'; root entry bhel-2 3.d. The cited dictionary page 102 (New College Edition) is lending-only online and could not be opened directly.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. balloon\", \"stance\": \"supports\", \"note\": \"'balloon, n. — F. ballon, fr. It. pallone, ... a word of Teut. origin; see ball, a round body, and -oon.'\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. balloon\", \"stance\": \"supports\", \"note\": \"SKT.txt l.1345 'balloon, a large ball. (F.-Ital.-O.H.G.)'.\"}\n ]\n})\n\nnodes.append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"ballot\",\n \"verdict\": \"plausible\",\n \"derivation\": \"English ballot (1540s 'small ball used in secret voting', hence 'a vote') does descend from Italian ballotta, but not directly as the chart's arrow implies: the intermediary is French ballotte / the verb ballotter, and Klein and Skeat both route it that way ('ballot, n. — F. ballotte, fr. It. ballotta, little ball, dimin. of balla, ball'). AHD, which Nourai follows, simply lists BALLOT among the English descendants of MHG balle > Italian balla, palla, without spelling out the French step — which is how the direct Italian-to-English arrow arose. Substance right, route abridged.\",\n \"derivation_fa\": \"«ballot» انگلیسی (از دههٔ ۱۵۴۰ به معنی گویچه‌ای که در رأی‌گیری پنهانی به کار می‌رفت و سپس «رأی») از ballotta ایتالیایی است، اما نه بی‌واسطه چنان‌که پیکانِ نمودار می‌نمایاند: میانجی آن ballotte فرانسوی (و فعل ballotter) است و کلاین و اسکیت هر دو همین مسیر را می‌دهند. واتکینز که مأخذ نورایی است تنها BALLOT را در شمار بازماندگان انگلیسیِ balle آلمانی می‌آورد و مرحلهٔ فرانسوی را ذکر نمی‌کند؛ از همین‌جا پیکان مستقیمِ «ایتالیایی ← انگلیسی» پدید آمده است. اصلِ ادعا درست ولی مسیر فشرده شده است؛ با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD:102\", \"status\": \"partial\", \"note\": \"AHD index l.1276 'BALLOT bhel-2'; the root entry lists BALLOT under 'Middle High German balle (> Italian balla, palla)' without naming the French stage, so it supports the root but not the direct Italian>English arrow.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. ballot\", \"stance\": \"partial\", \"note\": \"KLN_1971.txt l.25284: 'ballot, n. — F. ballotte, fr. It. ballotta, little ball, dimin. of balla, ball ... so called in allusion to the small balls formerly dropped into the voting urn.' — French intermediary.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. ballot\", \"stance\": \"partial\", \"note\": \"SKT.txt l.1352: 'ballot. (F.-O.H.G.) F. ballotter, to choose lots. — F. ballotte, a little ball used for voting; dimin. of F. balle, a ball.' — also via French; Skeat lists 'ballot' in his 'French from Old High German' appendix (l.23563).\"}\n ]\n})\n\nnodes.append({\n \"id\": 16, \"lang\": \"Latin\", \"words\": \"ballaena; bulga\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both Latin words really belong to this root family, but neither is an inherited Latin reflex of it — both are loanwords into Latin, which the chart's direct arrow from the root box hides. (a) L. ball(a)ena 'whale' is borrowed from Greek φάλλαινα (rel. to φαλλός 'phallus', from *bhel- 'to swell'), and the initial b- instead of p- shows that it came through a third language, generally taken to be Illyrian; Pokorny p.121 says exactly this: 'φάλλαινα, φάλλη Walfisch (vgl. das wohl durch illyr. Vermittlung entlehnte lat. ballaena)'. (b) L. bulga 'leather bag' is a Gaulish/Celtic loan, from Celtic *bolgā (Old Irish bolg 'sack, belly'), from the extension *bhelǵh-; Pokorny p.126: 'gall. bulga Ledersack (daraus ahd. bulga lederner Wasserbehälter)'; AHD s.v. bhelgh-: '4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE'. Nourai's glosses '(spouting) whale' and 'leather bag' are right.\",\n \"derivation_fa\": \"هر دو واژهٔ لاتینی به‌راستی به همین خانوادهٔ ریشه‌ای تعلق دارند، اما هیچ‌یک بازماندهٔ ارثیِ لاتینیِ آن نیست؛ هر دو وام‌واژه‌اند و پیکانِ مستقیمِ نمودار این نکته را می‌پوشاند. یکم: ballaena لاتینی «نهنگ» وام‌گرفته از یونانی φάλλαινα است (هم‌ریشه با φαλλός)، و بِ آغازین به‌جای پ نشان می‌دهد که واژه از راه زبانی سوم — که معمولاً ایلیری دانسته می‌شود — به لاتین رسیده است؛ پوکورنی در ص ۱۲۱ همین را می‌گوید. دوم: bulga لاتینی «انبان چرمی» وام‌واژه‌ای گَلی/سلتی است از *bolgā سلتی (ایرلندی کهن bolg «کیسه، شکم») از گسترشِ *bʰelǵʰ-؛ پوکورنی ص ۱۲۶ و واتکینز ذیل bhelgh- هر دو چنین می‌گویند. گلوس‌های نورایی درست است ولی نوعِ رابطه (وام‌گیری، نه وراثت) در نمودار نیامده؛ ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [E_BALEEN, E_BUDG],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD_watkins1985.txt s.v. bhelgh- '4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE' — supports bulga, and marks it as Celtic. For the whale, AHD s.v. bhel-2 has only '6. Possibly Greek phalaina, whale: BALEEN', i.e. Watkins routes it through Greek and calls the connection merely 'possible', and does not derive Latin ballaena straight from the root as the chart does.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"printed pp.121 and 126\", \"stance\": \"supports\", \"note\": \"p.121: 'dazu φάλλαινα ..., φάλλη Walfisch (vgl. das wohl durch illyr. Vermittlung entlehnte lat. ballaena)'; p.126: 'gall. bulga Ledersack (daraus ahd. bulga lederner Wasserbehälter)'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. baleen, budge\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l.4319: 'L. ballaena, whale, which was borrowed fr. Gk. φάλλαινα ... through the medium of the Illyrian language, a fact which explains the transition of Gk. φ into L. b (instead of p)'; KLN_1971.txt l.34925: 'OF. boge, bouge, leather bag, wallet, fr. L. bulga, leather wallet'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.182-183\", \"stance\": \"supports\", \"note\": \"the bhelgh- article gathers Celtic bolg-/bulga with Skt barhis-, Av. barezis- and Germanic balgs.\"}\n ]\n})\n\nnodes.append({\n \"id\": 17, \"lang\": \"Old French\", \"words\": \"baleine\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old French baleine 'whale, whalebone' (also balaine, 12th c.) is the regular popular development of Latin ball(a)ena: intervocalic -ll- simplified, and the sequence -aena gave OF -eine as in Latin plēna > OF pleine. It is the ancestor of Modern French baleine and the source of both English baleen and, much later, of the Persian zoological term.\",\n \"derivation_fa\": \"«baleine» فرانسوی کهن «نهنگ، استخوان نهنگ» (نیز balaine در سدهٔ دوازدهم) دنبالهٔ عادی و مردمیِ ballaena لاتینی است: ‑ll‑ میان دو واکه ساده شده و ‑aena به ‑eine بدل شده، درست مانند plēna لاتینی که به pleine فرانسوی کهن رسیده است. همین صورت نیای baleine فرانسوی امروز و سرچشمهٔ baleen انگلیسی و — بسیار دیرتر — اصطلاح جانورشناسیِ فارسی است. ادعای نورایی درست است.\",\n \"sources\": [E_BALEEN],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\", \"note\": \"AHD s.v. bhel-2 '6. Possibly Greek phalaina, whale: BALEEN' — Watkins names only the Greek and the English end-points; the Old French stage is implicit in the AHD body entry for baleen, which is not accessible online.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. baleen, balinger\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l.4319: 'baleen, n., whalebone. — ME. balene, baleyne, whale, whalebone, fr. OF. baleine, of s.m., fr. L. ballaena'; and 'balinger, n., a whaleship (obsol.) — OF. balengier, whaleship, fr. baleine, whale'.\"},\n   {\"src\": \"LEW\", \"where\": \"grep of LEW_1910.txt\", \"stance\": \"silent\", \"note\": \"no usable ballaena entry recovered from the OCR of Walde's Lateinisches etymologisches Woerterbuch.\"}\n ]\n})\n\nnodes.append({\n \"id\": 18, \"lang\": \"Persian\", \"words\": \"bâlon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"The Persian zoological term for the whale, بالن / بال bāl(en), is a modern loan from French baleine, brought in with 19th/20th-century natural history; it is a homograph of بالن ١ 'balloon' (node 13), which is why Nourai numbers them ١ and ٢, and of the inherited بال 'wing'. Mo‘in has the entry as بال: 'یکی از پستانداران بحری، از راستهٔ آب‌بازان (شناگران)، دارای سر حجیم و پهن و شکم صاف ... طولش تا [۳۰] متر و وزنش تا ۱۵۰/۰۰۰ کیلوگرم می‌رسد', and adds the corrective note 'غالباً این جانور را بنام «نهنگ» خوانند و اشتباه است' — i.e. the loanword bāl was introduced precisely to replace the traditional but zoologically inaccurate نهنگ. So the chart's arrow Old French baleine > Persian is right in substance, though the actual donor is Modern French baleine.\",\n \"derivation_fa\": \"اصطلاح جانورشناسیِ «بالن/بال» در فارسی وام‌واژه‌ای نو از فرانسوی baleine است که همراه با تاریخ طبیعیِ سدهٔ نوزدهم و بیستم وارد شد؛ این واژه هم‌نگارِ «بالن ۱» به معنی بالونِ هوایی (گرهٔ ۱۳) است و از همین‌رو نورایی آن دو را با شمارهٔ ۱ و ۲ از هم جدا کرده، و نیز هم‌نگارِ «بالِ» ارثی به معنی پر و بازوست. معین مدخل را چنین می‌آورد: «بال: یکی از پستانداران بحری، از راستهٔ آب‌بازان (شناگران)، دارای سر حجیم و پهن و شکم صاف ... طولش تا سی متر و وزنش تا ۱۵۰٬۰۰۰ کیلوگرم می‌رسد»، و در پی آن هشدار می‌دهد: «غالباً این جانور را بنام «نهنگ» خوانند و اشتباه است». یعنی همین وام‌واژه را برای جانشینی «نهنگِ» سنتی و از نظر جانورشناسی نادرست به کار برده‌اند. ادعای نورایی درست است، جز آنکه وام‌دهنده فرانسوی امروزی است نه فرانسوی کهن.\",\n \"sources\": [E_BALEEN],\n \"ref_check\": [\n   {\"ref\": \"MON:464,467\", \"status\": \"supports\", \"note\": \"MON_part1.txt l.20820-20825, headword 'بال' with the Latin lemma and the tag (جان.) 'zoology': 'یکی از پستانداران بحری، از راستهٔ آب‌بازان (شناگران) ...' with the note 'غالباً این جانور را بنام «نهنگ» خوانند و اشتاه [اشتباه] است'. Only the 2-vol. abridgement is on disk, so the exact pages 464/467 of the 6-vol. edition are unverified, but the entries Nourai points to are confirmed.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. بال (جان.)\", \"stance\": \"supports\", \"note\": \"see ref_check; the neighbouring entries distinguish بال 'wing', بال 'whale', بال 'ریشهٔ بالیدن و بالش' and Arabic بال 'حال، خاطر'.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. baleen\", \"stance\": \"supports\", \"note\": \"confirms the French word baleine 'whale' from which the Persian term is taken.\"}\n ]\n})\n\nnodes.append({\n \"id\": 19, \"lang\": \"English\", \"words\": \"baleen\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English baleen, ME balene/baleyne 'whale, whalebone' (early 14th c.), is from Old French baleine; it narrowed from 'whale' to 'whalebone, the horny plates of the whale's upper jaw', the sense it has today (baleen whales). The chain OF baleine < L ballaena < Gk φάλλαινα < *bhel- 'to swell' is uncontroversial and is given identically by Klein, Watkins and Etymonline.\",\n \"derivation_fa\": \"«baleen» انگلیسی، در انگلیسی میانه balene/baleyne «نهنگ، استخوان نهنگ» (آغاز سدهٔ چهاردهم)، از baleine فرانسوی کهن است؛ معنای آن از «نهنگ» به «تیغه‌های شاخیِ آرواره‌ی بالای نهنگ» تنگ‌تر شده و امروز در «نهنگ‌های بالِن‌دار» به کار می‌رود. زنجیرهٔ baleine فرانسوی کهن ← ballaena لاتینی ← φάλλαινα یونانی ← ریشهٔ *bʰel- «آماسیدن» بی‌مناقشه است و کلاین، واتکینز و اتیمانلاین آن را یکسان می‌آورند. ادعای نورایی درست است.\",\n \"sources\": [E_BALEEN],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD index l.1276 'BALEEN bhel-2'; root entry bhel-2 '6. Possibly Greek phalaina, whale: BALEEN' — Watkins hedges the Greek etymology with 'possibly' but the word is put here.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. baleen\", \"stance\": \"supports\", \"note\": \"KLN_1966.txt l.4319, full chain ME balene < OF baleine < L ballaena < Gk φάλλαινα, 'related to φαλλός, penis, fr. I.-E. base *bhel-, to swell'.\"},\n   {\"src\": \"FSD\", \"where\": \"grep of FSD volumes\", \"stance\": \"silent\", \"note\": \"no clean 'baleen' entry recoverable from the Funk & Wagnalls OCR.\"}\n ]\n})\n\nnodes.append({\n \"id\": 20, \"lang\": \"Old French\", \"words\": \"bougette\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old French bougette is the diminutive (-ette) of boge / bouge 'leather bag, wallet', which continues Latin bulga; the sense is 'a little leather pouch'. Klein s.v. budget: 'F. bougette, a little trunk of wood, dimin. of boge, bouge, leather bag, wallet'. The intervocalic -lg- of bulga gave OF -ug-/-uch- by the normal vocalisation of l before a consonant. Nourai's gloss 'leather bag, budget' telescopes the medieval and the modern sense into one line, but the word is right.\",\n \"derivation_fa\": \"«bougette» فرانسوی کهن مصغّرِ (با پسوند ‑ette) واژهٔ boge/bouge «انبان چرمی، کیسه» است که خود دنبالهٔ bulga لاتینی است؛ معنای آن «کیسهٔ چرمیِ کوچک» است. کلاین ذیل budget می‌نویسد: «فرانسوی bougette، مصغّرِ boge, bouge «انبان چرمی»». لامِ خوشهٔ ‑lg‑ در لاتینی بر پایهٔ قاعدهٔ عادیِ فرانسوی پیش از همخوان به واکه بدل شده و ‑ug‑ داده است. گلوسِ نورایی («انبان چرمی، بودجه») معنای قرون وسطایی و معنای امروزی را در یک سطر در هم فشرده، ولی خودِ واژه درست است. ادعای نورایی درست است.\",\n \"sources\": [E_BUDG],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. bhelgh- '4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE' — Watkins puts BUDGET here; the Old French diminutive is the standard intermediate step given in the AHD body entry.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. budge 'fur', budget\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt l.34925: 'budge, n., a kind of fur. — ME. bouge, bag, fr. OF. boge, bouge, leather bag, wallet, fr. L. bulga, leather wallet'; l.34934: 'budget, n. — F. bougette, ... dimin. of boge, bouge, leather bag, wallet.'\"},\n   {\"src\": \"SKT\", \"where\": \"appendix 'French from Celtic'\", \"stance\": \"supports\", \"note\": \"SKT.txt l.23406 lists 'budge (2), budget' among French words of Celtic (Breton/Gaulish) origin — i.e. Skeat too traces the word to the Celtic bulga.\"}\n ]\n})\n\nnodes.append({\n \"id\": 21, \"lang\": \"English\", \"words\": \"budget\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English budget, ME bouget 'leather pouch, wallet' (early 15th c.) from OF bougette; from the late 16th c. also 'a stock, store, collection of miscellaneous things' and 'a bundle of news'. The financial sense dates from 1733, from the image of the treasury minister 'opening his budget', i.e. the wallet in which he kept his fiscal papers — the famous pamphlet against Walpole, 'The Budget Opened'. This English-made sense is what later travelled back to France and on to Persia.\",\n \"derivation_fa\": \"«budget» انگلیسی، در انگلیسی میانه bouget «انبان چرمی، کیسه» (آغاز سدهٔ پانزدهم)، از bougette فرانسوی کهن است؛ از اواخر سدهٔ شانزدهم معنای «ذخیره، مجموعهٔ چیزهای گوناگون» و «بستهٔ اخبار» نیز یافت. معنای مالی از ۱۷۳۳ پدید آمد، از تصویرِ وزیر خزانه‌داری که «کیسهٔ خود را می‌گشاید»، یعنی کیفی که اوراق مالی در آن بود — اشاره به جزوهٔ مشهورِ ضدِ والپول با عنوان The Budget Opened. همین معنای انگلیسی‌ساخته است که بعدها به فرانسوی بازگشت و از آن‌جا به فارسی رسید. ادعای نورایی درست است.\",\n \"sources\": [E_BUDG],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD index l.1324 'BUDGET bhelgh-'; root entry bhelgh- '4. Celtic *bolg- in Latin bulga, leather sack: BUDGET, BULGE'.\"},\n   {\"ref\": \"ETM:62\", \"status\": \"not_checked\", \"note\": \"ETM = Abolghasemi, Risheh-shenasi (Etimoloji), Qoqnus 1374. refs_online.json records 'RE-SEARCH 2026-09: no digital copy on any permitted platform; catalogue/purchase only' — the book is not available to check.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. budget\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt l.34934: 'budget, n. — F. bougette, a little trunk of wood, dimin. of boge, bouge, leather bag, wallet. See budge, fur, and -et.'\"},\n   {\"src\": \"SKT\", \"where\": \"appendix\", \"stance\": \"partial\", \"note\": \"SKT.txt l.23406 lists 'budget' among 'French from Celtic'; l.21241 s.v. wallet glosses 'wallet, a bag, budget', showing the older English sense.\"}\n ]\n})\n\nnodes.append({\n \"id\": 22, \"lang\": \"French\", \"words\": \"budget\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Modern French budget is a 19th-century re-borrowing from English (attested 1802/1806 in the fiscal sense, in the wake of the British parliamentary vocabulary), not a survival of the medieval bougette; the pronunciation with a final -et and the anglicised spelling betray the round trip. It is therefore a doublet of French bougette, and one of the classic examples of a French word that returned home from England with a new meaning.\",\n \"derivation_fa\": \"«budget» فرانسوی امروز وام‌گیریِ دوبارهٔ سدهٔ نوزدهمی از انگلیسی است (نخستین شواهدِ معنای مالی در ۱۸۰۲ و ۱۸۰۶، در پی رواج واژگان پارلمانی بریتانیا)، نه بازماندهٔ bougette قرون وسطایی؛ املا و تلفظِ انگلیسی‌گونهٔ آن گواه این سفر رفت و برگشت است. پس این واژه دوگانهٔ bougette فرانسوی است و از نمونه‌های کلاسیکِ واژه‌ای فرانسوی که با معنایی تازه از انگلستان به خانه بازگشته است. ادعای نورایی درست است.\",\n \"sources\": [E_BUDG, W_BUDJE],\n \"ref_check\": [\n   {\"ref\": \"ETM:62\", \"status\": \"not_checked\", \"note\": \"Abolghasemi's Risheh-shenasi p.62 is Nourai's authority for the English>French>Persian leg; refs_online.json records that no digital copy exists on any permitted platform, so it could not be consulted.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. budget\", \"stance\": \"partial\", \"note\": \"Klein derives English budget from French bougette but does not discuss the modern French re-borrowing; the modern French financial term is not treated in his English dictionary.\"},\n   {\"src\": \"DEV\", \"where\": \"grep of DEV.txt\", \"stance\": \"silent\", \"note\": \"Devic's dictionary of French words of oriental origin has nothing on budget — correctly, since it is not an orientalism.\"}\n ]\n})\n\nnodes.append({\n \"id\": 23, \"lang\": \"Persian\", \"words\": \"bŭdjeh\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"NP بودجه budje is borrowed from French budget; Wiktionary states plainly 'Borrowed from French budget'. The French final -t is dropped (as in French pronunciation) and the -e is written with the Persian hā-ye bayān ه; the word entered administrative Persian with the constitutional financial legislation. Mo‘in's entry defines it as 'مجموع درآمدها و هزینه‌های یک کشور، یک وزارتخانه ...' and quotes the legal definition from article 1 of the Public Accounts Act of 30 Esfand 1312 (1934). This is thus a Persian > (no) — purely European — loan, the last link of a chain that began with Gaulish bulga.\",\n \"derivation_fa\": \"«بودجه» وام‌واژه‌ای است از فرانسوی budget؛ ویکی‌واژه صریحاً می‌نویسد «وام‌گرفته از فرانسوی budget». تِ پایانیِ فرانسوی — که در تلفظ فرانسوی هم ادا نمی‌شود — افتاده و واکهٔ پایانی با هایِ بیان نوشته شده است. این واژه با قوانین مالیِ پس از مشروطه وارد زبان اداری فارسی شد. معین آن را «مجموع درآمدها و هزینه‌های یک کشور، یک وزارتخانه ...» تعریف می‌کند و تعریف قانونیِ مادهٔ اول قانون محاسبات عمومیِ مصوب ۳۰ اسفند ۱۳۱۲ را نیز نقل می‌کند. بدین‌سان «بودجه» آخرین حلقهٔ زنجیره‌ای است که از bulga گَلی آغاز شده است. ادعای نورایی درست است.\",\n \"sources\": [W_BUDJE, E_BUDG],\n \"ref_check\": [\n   {\"ref\": \"MON:600\", \"status\": \"supports\", \"note\": \"MON_part1.txt l.26010 ff.: 'بودجه: [budget] (ا.) مجموع درآمدها و هزینه‌های یک کشور، یک وزارتخانه، یک اداره ...' followed by the citation of the Public Accounts Act of 30 Esfand 1312. Only the 2-vol. abridgement is on disk, so page 600 of the 6-vol. edition is unverified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"s.v. بودجه\", \"stance\": \"supports\", \"note\": \"see ref_check.\"},\n   {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwoerter im Arabischen\", \"stance\": \"silent\", \"note\": \"not relevant / no entry: بودجه is a European loan into Persian, not a Persian word borrowed by Arabic.\"}\n ]\n})\n\nnodes.append({\n \"id\": 24, \"lang\": \"Old Norse\", \"words\": \"blôm, blômi; bulki\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Two Old Norse words, both correctly placed. (a) ON blóm n. (collective) / blómi m. 'flower, blossom' continues Germanic *blōmōn-, from the extended o-grade *bhlō- of the 'thrive, bloom' branch of the root; Pokorny p.122 s.v. '4. bhel- und bhlē-, bhlō-, bhlə-s- Blatt, Blüte, blühen; üppig sprießen' lists 'got. blōma m., ahd. bluomo m. Blume, aisl. blómi m. ds., blōm Kollektiv Blume', cognate with Latin flōs 'flower'. (b) ON bulki m. 'cargo, a rolled-up load stowed amidships' belongs to the zero-grade *bhl- of the 'swell' branch; AHD s.v. bhel-2 '1.c Old Norse bulki, cargo (< rolled-up load): BULK'. Nourai's glosses are accurate.\",\n \"derivation_fa\": \"دو واژهٔ نورسی کهن، هر دو به‌درستی زیر این ریشه نشسته‌اند. یکم: blóm (اسم جمعِ خنثی) و blómi «گل، شکوفه» دنبالهٔ ژرمنیِ *blōmōn- از پایهٔ گسترده‌ی *bʰlō- در شاخهٔ «رُستن، شکوفیدن» است؛ پوکورنی در ص ۱۲۲ ذیل «۴. bhel- و bhlē-, bhlō-, bhlǝ-s- «برگ، شکوفه، شکوفیدن»» صورت‌های «گوتی blōma، آلمانی علیای باستان bluomo، ایسلندی کهن blómi، blōm» را می‌آورد و همهٔ اینها با flōs لاتینی «گل» هم‌ریشه‌اند. دوم: bulki نورسی «بارِ کشتی، بستهٔ لوله‌شده» به پایهٔ صفرِ *bʰl- در شاخهٔ «آماسیدن» تعلق دارد؛ واتکینز ذیل bhel-2 می‌نویسد «نورسی کهن bulki «بار» (از «بارِ لوله‌شده») ← BULK». گلوس‌های نورایی دقیق‌اند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. bhel-2 '1.c Old Norse bulki, cargo (< “rolled-up load”): BULK1' and s.v. bhel-3 'Germanic suffixed form *blō-mōn- in (i) Old Norse blóm, blómi, flower, blossom: BLOOM1'. Both of Nourai's words with both of his glosses.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"printed p.122\", \"stance\": \"supports\", \"note\": \"POK_01.txt leaf 132: '4. bhel- und bhle-, bhlo-, bhle-s- Blatt, Bluete, bluehen; ueppig spriessen ... got. bloma m., ahd. bluomo m. Blume, aisl. blomi m. ds., blom Kollektiv Blume'; the same page opens 'Dazu 4. bhel- bluehen usw. und die Erweiterungen bhelgh-, bhledh-, bhlegu-, bhlei-, bhleu- schwellen usw.'\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. bloom, bulk\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt l.30922 'bloom, n., flower. — ME. blome, fr. ON. blom, blomi'; l.35107 'bulk, n., size, volume; cargo of a ship. — ME. bulke, prob. a blend of ON. bulki, cargo, and OE. buc, body, belly. ON. bulki is rel. to ON. bollr, a ball, fr. I.-E. base *bhel-, to swell'.\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. bloom\", \"stance\": \"supports\", \"note\": \"SKT.txt l.1992: 'bloom, a flower. (Scand.) M.E. blome; not in A.S. — Icel. blom, blomi, a flower; Swed. blomma; Dan. blomme; Du. bloem; Goth. bloma; L. flos; see Flower.'\"}\n ]\n})\n\nnodes.append({\n \"id\": 25, \"lang\": \"English\", \"words\": \"bloom, bulk\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English bloom 'flower' is a Scandinavian loan of the Viking period (ME blome, not attested in Old English, which used blōstma > blossom), from ON blóm/blómi. English bulk 'size, volume; cargo of a ship' likewise goes back to ON bulki 'cargo'; Klein refines this to 'prob. a blend of ON. bulki, cargo, and OE. buc, body, belly', which explains the -u- and the 'body/mass' sense, but the Norse word remains the main source, as AHD's 'Old Norse bulki, cargo: BULK1' says. (English homonyms bulk 'stall of a shop' and bulk-head belong instead to OE balca 'beam' — a neighbouring but distinct root, Pokorny's 5. bhel- 'Bohle, Balken', p.123.)\",\n \"derivation_fa\": \"«bloom» انگلیسی به معنی «گل، شکوفه» وام‌واژه‌ای اسکاندیناویایی از روزگار وایکینگ‌هاست (انگلیسی میانه blome؛ در انگلیسی باستان نبوده و آن زبان blōstma را به کار می‌برده که «blossom» امروزی است)، از blóm/blómi نورسی. «bulk» نیز به معنی «حجم، تنه، بارِ کشتی» به bulki نورسی «بار» بازمی‌گردد؛ کلاین آن را «احتمالاً آمیزه‌ای از bulki نورسی و būc انگلیسی باستان «تنه، شکم»» می‌داند که واکهٔ u و معنای «تنه/توده» را توضیح می‌دهد، ولی خاستگاه اصلی همان واژهٔ نورسی است، چنان‌که واتکینز می‌گوید. (هم‌نگارِ دیگرِ bulk به معنی «سکوی جلو دکان» از balca انگلیسی باستان «تیر» است که به ریشهٔ همسایه ولی جداگانهٔ «۵. bhel- تخته، تیر» در ص ۱۲۳ پوکورنی تعلق دارد.) ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD index l.1309 'BLOOM1 bhel-3' and l.1324 'BULK1 bhel-2'; the root entries give ON blóm/blómi > BLOOM1 and ON bulki > BULK1.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"s.v. bloom, bulk\", \"stance\": \"partial\", \"note\": \"'bloom, n., flower. — ME. blome, fr. ON. blom, blomi' (supports); 'bulk, n., size, volume; cargo of a ship. — ME. bulke, prob. a blend of ON. bulki, cargo, and OE. buc, body, belly' (a refinement of the simple ON > E arrow).\"},\n   {\"src\": \"SKT\", \"where\": \"s.v. bloom, bulk (3)\", \"stance\": \"partial\", \"note\": \"SKT.txt l.1992 'bloom ... Icel. blom, blomi'; l.1337 'bulk (3), the stall of a shop. (Scand.) — Icel. balkr, a beam ... see Balk' — Skeat separates that homonym from bulk 'size'.\"},\n   {\"src\": \"POK\", \"where\": \"printed p.122 and p.123\", \"stance\": \"supports\", \"note\": \"p.122 has the 'bloom' branch (aisl. blomi, blom); p.123 '5. bhel-, meist mit -g-(-k-) Suffix Bohle, Balken' is the separate root of bulk 'stall, beam'.\"}\n ]\n})\n\nentry = {\n \"entry\": 0,\n \"root\": \"Bhel, Bhelgh, Bhlei, Bhleu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *bʰel- 'to blow, swell' (Pok. 3. bhel- 120) and *bʰel- 'to thrive, bloom' (Pok. 4. bhel- 122), with the extensions *bʰelǵʰ- 'to swell; bag, cushion' (Pok. 125), *bʰlei- (Pok. 156) and *bʰleu- 'to swell, well up, overflow' (Pok. 158)\",\n \"note\": \"Root, language label, gloss and all five page references are correct, and they are correct together: Pokorny opens the article on p.122 with exactly Nourai's grouping — 'Dazu 4. bhel- ‚blühen‘ usw. und die Erweiterungen bhelgh-, bhlēdh-, bhlegu-, bhlei-, bhleu- ‚schwellen‘ usw.' Watkins/AHD has the same set with the same Pokorny page numbers in its brackets (bhel-2 [Pok. 3. bhel- 120]; bhel-3 'to thrive, bloom' [Pok. 4. bhel- 122]; bhelgh- 'to swell, extension of bhel-2' [Pok. bhelgh- 125]; bhlei- 'to blow, swell, extension of bhel-2' [Pok. 2. bhlei- 156]; bhleu- 'to swell, well up, overflow, extension of bhel-2' [Pok. bhleu- 158]), which is plainly where Nourai took the composite headword and the reference string from. The composite gloss 'to swell, blow, thrive, grow, bloom, overflow' is a fair rendering of Pokorny's 'aufblasen, aufschwellen, sprudeln, strotzen' + 'Blatt, Blüte, blühen; üppig spriessen' + 'schwellen, strömen, überfliessen'. Caveats affecting individual arrows, not the root: 'Avestan barez to grow' (node 1) belongs to *bʰerǵʰ- 'high' (Pok. 140), not here; Latin ballaena and bulga (node 16) are loans into Latin (Greek via Illyrian, and Gaulish respectively), not inherited reflexes; and the Persian words بلوار، بالون، بالن، بودجه are modern European loans, whereas برسم and بالش/بالین are genuine Iranian inheritances — the page is in fact a nice demonstration of the same root reaching Persian twice, once down the Avestan line and once round through Paris.\",\n \"note_fa\": \"ریشه، برچسب زبانی، معنا و هر پنج ارجاع درست‌اند و مهم‌تر آنکه با هم درست‌اند: پوکورنی در ص ۱۲۲ دقیقاً همین گروه‌بندی را می‌آورد: «و بدین ریشه تعلق دارد ۴. bhel- «شکوفیدن» و گسترش‌های bhelgh-, bhlēdh-, bhlegu-, bhlei-, bhleu- «آماسیدن»». واتکینز در پیوست ریشه‌های هندواروپایی AHD همین مجموعه را با همین شمارهٔ صفحات پوکورنی در قلاب می‌آورد (۱۲۰، ۱۲۲، ۱۲۵، ۱۵۶، ۱۵۸) و پیداست که نورایی سرواژه و رشتهٔ ارجاعات را از همین جا گرفته است. سه نکتهٔ احتیاطی در سطح پیکان‌ها و نه خود ریشه: barez اوستایی (گره ۱) به ریشهٔ *bʰerǵʰ- «بلند» (پوکورنی ۱۴۰) تعلق دارد؛ ballaena و bulga لاتینی (گره ۱۶) وام‌واژه‌اند (یکی از یونانی از راه ایلیری و دیگری از گَلی) نه بازماندهٔ ارثی؛ و سرانجام واژه‌های «بلوار، بالون، بالن، بودجه» وام‌واژه‌های اروپایی نوین‌اند، حال آنکه «برسم» و «بالش/بالین» میراث اصیل ایرانی‌اند؛ این صفحه نمونهٔ خوبی است از یک ریشه که دو بار به فارسی رسیده است: یک بار از راه اوستا و یک بار از راه پاریس.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"POK:120\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 130 (printed p.120): '5.[read 3.] bhel-, bhle- ‚aufblasen, aufschwellen, sprudeln, strotzen‘' — with gr. φαλλός, φάλλαινα, lat. follis, aisl. bulr/bolr, mnd. bole, and av. barə-s-man-.\"},\n  {\"ref\": \"POK:122\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 132 (printed p.122): '4. bhel- und bhle-, bhlo-, bhle-s- ‚Blatt, Blüte, blühen; üppig sprießen‘' with 'aisl. blomi m., blom Kollektiv Blume'; the same page states 'Dazu 4. bhel- ‚blühen‘ usw. und die Erweiterungen bhelgh-, bhledh-, bhlegu-, bhlei-, bhleu- ‚schwellen‘ usw.'\"},\n  {\"ref\": \"POK:125\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 135, entry beginning at printed p.125: 'bbelgh- ‚schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster‘ (Erw. von bhel- ‚aufblasen‘ usw.)'.\"},\n  {\"ref\": \"POK:156\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 166 (printed p.156): '2. bhlei- ‚aufblasen, schwellen, strotzen, überfließen‘, Erw. von bhel- ds.'\"},\n  {\"ref\": \"POK:158\", \"status\": \"supports\", \"note\": \"POK_01.txt leaf 168 (printed p.158): the article closes with 'bhleu- ‚aufblasen (schnauben, brüllen), schwellen ...‘', matching AHD's '[Pok. bhleu- 158]'.\"},\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt l.328-330 and l.342: bhel-2 [Pok. 3. bhel- 120], bhel-3 'To thrive, bloom' [Pok. 4. bhel- 122], bhelgh- 'To swell. Extension of bhel-2' [Pok. bhelgh- 125], bhlei- 'To blow, swell. Extension of bhel-2' [Pok. 2. bhlei- 156], bhleu- 'To swell, well up, overflow. Extension of bhel-2' [Pok. bhleu- 158] — Nourai's four root names and five page numbers in one place.\"},\n  {\"ref\": \"ROE:65,66\", \"status\": \"not_checked\", \"note\": \"ROE = R. Claiborne, The Roots of English (1989). refs_online.json: 'RE-SEARCH 2026-09: borrowable only' — lending-only on archive.org, not consultable.\"}\n ],\n \"consulted\": [\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny Bd. II pp.182-183\", \"stance\": \"supports\", \"note\": \"WLD_Bd2_pages.txt l.11798 'bhelgh ‚schwellen‘, *bhleg- ds.'; l.11975 'bhelgh ‚schwellen; Balg (aufgeblasene Tierhaut), Kissen, Polster‘ (Erw. ...)'; l.11922 running head '182 bhel- — bhelgh'. The predecessor of Pokorny 1959 has the same architecture.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann, s.v. bholghis\", \"stance\": \"supports\", \"note\": \"IEC.txt l.1488 'bholghís, io ‚bolster, litter‘. WP II, 183 Skt. barhís ...; Av. barozis ...; Per. balis, balin ‚cushion‘' — Mann reconstructs the same *bholgh- noun.\"},\n  {\"src\": \"KLN\", \"where\": \"s.v. ball, bull, baleen\", \"stance\": \"supports\", \"note\": \"KLN_1971.txt l.35110-35114: 'fr. I.-E. base *bhel-, ‚to swell‘, whence also Gk. φαλλός, φάλλαινα, φάλλη ‚whale‘, L. follis ... For derivatives of base *bhelgh-, an enlargement of base *bhel-, see belly, budget, bulge.' Klein groups exactly Nourai's material.\"},\n  {\"src\": \"SYN\", \"where\": \"Buck, Dictionary of Selected Synonyms\", \"stance\": \"silent\", \"note\": \"the 'pillow' and 'whale' sections of Buck (SYN.txt around l.6545, l.19710) discuss ON koddi / OE codd and other words; no bhel-/bhelgh- entry that bears on this chart.\"}\n ],\n \"nodes\": nodes\n}\n\nout = {\n \"pdf_page\": 84,\n \"book_page\": 54,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [entry]\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-84.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\nprint(\"written\", len(nodes), \"nodes\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk84.py",
 "description": "Write page-84.json"
}
```


### [2026-09-05T06:39:06.393Z] TOOL RESULT

```
written 25 nodes
```


## [2026-09-05T06:39:10.553Z] TOOL CALL #54: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-84.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 84",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T06:39:12.144Z] TOOL RESULT

```
JSON OK
nodes verified: 25/25
node verdicts: {'plausible': 6, 'confirmed': 19}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 22, 'partial': 5, 'not_checked': 2}
books consulted: {'partial': 13, 'silent': 11, 'supports': 39} | by book: {'KLN': 16, 'SKT': 10, 'HUB': 5, 'PHD': 4, 'POK': 4, 'MON': 4, 'WLD': 3, 'ARY': 3, 'BRT': 2, 'AHD': 2, 'NYB': 2, 'IEC': 2, 'BQT': 1, 'WEB': 1, 'LEW': 1, 'FSD': 1, 'DEV': 1, 'PLA': 1}
```


## [2026-09-05T06:39:30.122Z] AGENT

Done. `data/verification/page-84.json` written; `verify_check.py 84` reports 25/25 nodes, 0 PROBLEM lines.

**Page 84 (book p. 54) — root "Bhel, Bhelgh, Bhlei, Bhleu", 1 entry, 25 nodes**

- Root: **confirmed** (1). Nodes: **confirmed 19, plausible 6**, no disputed, no transcription_suspect, no unverified.
- Ref checks: supports 22, partial 5, not_checked 2 (ROE:65,66 and ETM:62 — both unavailable in any digital form per `refs_online.json`). 18 books consulted.

Plausible (nothing worse) — the six imprecisions:
- **#1 Av. barez / bara-s-man** — `barəsman-` is genuinely under *bʰel-* (Pokorny p.120 quotes it, following Thieme; Bartholomae ties it to Skt. *barhiṣ-*), but `barez` = Av. *barəz-* 'be high' belongs to *bʰerǵʰ-* (Pok. 140), a different root.
- **#4 Av. baraziš, barašnav** — `barəziš-` 'cushion' is correct; `barašnav` (= Av. *barəšnu-*) means 'height, crown of the head' (Bartholomae col. 951, source of the *baršnūm* ritual), not 'cushion'. Nourai got the pairing from Hübschmann and carried the gloss across.
- **#7/#8 Middle German bole → French boulevard** — verbatim from AHD, but the actual donor of *boulevard* is Middle Dutch *bolwerc* (Klein, Etymonline).
- **#15 English ballot** — drawn straight from Italian; the real route is via French *ballotte*.
- **#16 Latin ballaena, bulga** — both are loans *into* Latin (Greek φάλλαινα via Illyrian; Gaulish *bulga*), not inherited reflexes, which the arrow from the root box hides.

Positive confirmations worth noting: Nourai's Pahlavi **bālišn** is exactly Hübschmann's and Wiktionary's MP form; **SNS:98** turns out to contain both *bālišn* and the very transliteration "barašnav", and **SNS:103** the *barsum* entry — both citations check out precisely. **BQT:256** was located in `BQT_v1_pages.txt` (the page carries "بقیه از صفحه ٢٥٥") and does hold the برسم entry.

**Extraction errors: none.** I rendered PDF p.84 and compared: the JSON is faithful to the printed page throughout, including "barašnav", "Middle German", and the Persian script/numbering (بالن ١ / بالن ٢, بالش ١, بال ١).

6 web sources archived via `fetch_source.py` (Wiktionary بالش/بالین/بودجه, Etymonline boulevard/budget/baleen).
