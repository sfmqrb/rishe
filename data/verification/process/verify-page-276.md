# Verification process log — verify-page-276


## [2026-09-06T21:14:51.619Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 276 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-276.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-276.json. Write /home/sfmqrb/git/rishe/data/verification/page-276.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 276` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:14:53.203Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:14:53.922Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:14:53.940Z] TOOL RESULT

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


## [2026-09-06T21:14:54.056Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-276.txt"
}
```


### [2026-09-06T21:14:54.069Z] TOOL RESULT

```
1	=== PDF page 276 (book page 246) ===
2	--- entry 0 ---
3	ROOT Krep -> redirect to Kwer
4	--- entry 1 ---
5	ROOT Krep-ed-tro -> redirect to Kwer
6	--- entry 2 ---
7	ROOT [Indo-European] Kreu, Qreu, Qreus, Qruwes, Qrus : to be icy, also anything solid, coagulated blood, bloody  (refs POK:621; KLN:252)
8	#1 (parent #0) [Greek] refs=KLN:252 | casos : ice ; kau-casos : shining with ice (mountains) ☞Kŭ 1
9	  #2 (parent #1) [Latin] refs=KLN:252 | caucasus : a very mountainous area between Caspian and Black seas.
10	    #3 (parent #2) [Arabic] refs=None | 
11	      #4 (parent #3) [Persian] refs=MON5:1474 | qafqâz «قفقاز» : Caucasia
12	    #5 (parent #2) [English] refs=KLN:252 | Caucasian
13	#6 (parent #0) [Greek] refs=KLN:252,380 | cros : frost ; crystacus : ice
14	  #7 (parent #6) [Latin] refs=None | crystallum : ice, gloss
15	    #8 (parent #7) [French] refs=None | crystal
16	      #9 (parent #8) [Persian] refs=None | krîstâl «کریستال» : crystal
17	      #10 (parent #8) [English] refs=KLN:380 | crystal
18	  #11 (parent #6) [English] refs=None | cryogenic
19	#12 (parent #0) [Avestan] refs=POK:621; KLN:377 | xrŭ, xrŭm : bloody flesh ; xrŭra : bloody, cruel ; xrŭma, xrŭta, xrus : dreadful ; xrŭždra : heart
20	#13 (parent #0) [Persian] refs=IEC:562; MON:3040 | kolŭx «کلوخ» : dried pieces of mud
21	#14 (parent #0) [Sogdian] refs=SOD:432 | xrwm : earth, soil
22	#15 (parent #0) [Greek] refs=AHD | kreas : flesh ; pan-kreas : all flesh
23	  #16 (parent #15) [French] refs=None | pancreas
24	    #17 (parent #16) [Persian] refs=VOP:108 | pânkrâs «پانکراس» : pancreas
25	  #18 (parent #15) [English] refs=None | pancreas
26	#19 (parent #0) [Latin] refs=KLN:378 | crusta : hardened by freezing ; crŭdus : bloody, raw
27	  #20 (parent #19) [English] refs=None | crust ; crude
28	--- entry 3 ---
29	ROOT Krk -> redirect to Kerk
30	
```


## [2026-09-06T21:14:58.508Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-276.json'))\nprint(json.dumps(d,ensure_ascii=False,indent=1)[:6000])\n\"",
 "description": "Read source JSON for page 276"
}
```


## [2026-09-06T21:14:58.966Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-06T21:15:00.204Z] TOOL RESULT

```
{
 "pdf_page": 276,
 "book_page": 246,
 "entries": [
  {
   "root": {
    "name": "Krep",
    "redirect": "Kwer"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Krep-ed-tro",
    "redirect": "Kwer"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Kreu, Qreu, Qreus, Qruwes, Qrus",
    "lang": "Indo-European",
    "refs": "POK:621; KLN:252",
    "gloss": "to be icy, also anything solid, coagulated blood, bloody"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Greek",
     "refs": "KLN:252",
     "words": [
      {
       "translit": "casos",
       "gloss": "ice",
       "script": null
      },
      {
       "translit": "kau-casos",
       "gloss": "shining with ice (mountains)",
       "script": null,
       "see": [
        "Kŭ 1"
       ]
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 2,
     "parent": 1,
     "lang": "Latin",
     "refs": "KLN:252",
     "words": [
      {
       "translit": "caucasus",
       "gloss": "a very mountainous area between Caspian and Black seas.",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 2,
     "lang": "Arabic",
     "refs": null,
     "words": [],
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Persian",
     "refs": "MON5:1474",
     "words": [
      {
       "translit": "qafqâz",
       "gloss": "Caucasia",
       "script": "قفقاز"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 5,
     "parent": 2,
     "lang": "English",
     "refs": "KLN:252",
     "words": [
      {
       "translit": "Caucasian",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 6,
     "parent": 0,
     "lang": "Greek",
     "refs": "KLN:252,380",
     "words": [
      {
       "translit": "cros",
       "gloss": "frost",
       "script": null
      },
      {
       "translit": "crystacus",
       "gloss": "ice",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 7,
     "parent": 6,
     "lang": "Latin",
     "refs": null,
     "words": [
      {
       "translit": "crystallum",
       "gloss": "ice, gloss",
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
     "refs": null,
     "words": [
      {
       "translit": "crystal",
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
     "refs": null,
     "words": [
      {
       "translit": "krîstâl",
       "gloss": "crystal",
       "script": "کریستال"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 8,
     "lang": "English",
     "refs": "KLN:380",
     "words": [
      {
       "translit": "crystal",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 11,
     "parent": 6,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "cryogenic",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 12,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:621; KLN:377",
     "words": [
      {
       "translit": "xrŭ, xrŭm",
       "gloss": "bloody flesh",
       "script": null
      },
      {
       "translit": "xrŭra",
       "gloss": "bloody, cruel",
       "script": null
      },
      {
       "translit": "xrŭma, xrŭta, xrus",
       "gloss": "dreadful",
       "script": null
      },
      {
       "translit": "xrŭždra",
       "gloss": "heart",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 13,
     "parent": 0,
     "lang": "Persian",
     "refs": "IEC:562; MON:3040",
     "words": [
      {
       "translit": "kolŭx",
       "gloss": "dried pieces of mud",
       "script": "کلوخ"
      }
     ],
     "note": null,
     "quote": {
      "text": "چو کردی با کلوخ انداز پیکار - سر خود را بنادانی شکستی",
      "poet": "Sa`dî"
     }
    },
    {
     "id": 14,
     "parent": 0,
     "lang": "Sogdian",
     "refs": "SOD:432",
     "words": [
      {
       "translit": "xrwm",
       "gloss": "earth, soil",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 15,
     "parent": 0,
     "lang": "Greek",
     "refs": "AHD",
     "words": [
      {
       "translit": "kreas",
       "gloss": "flesh",
       "script": null
      },
      {
       "translit": "pan-kreas",
       "gloss": "all flesh",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 16,
     "parent": 15,
     "lang": "French",
     "refs": null,
     "words": [
      {
       "translit": "pancreas",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 17,
     "parent": 16,
     "lang": "Persian",
     "refs": "VOP:108",
     "words": [
      {
       "translit": "pânkrâs",
       "gloss": "pancreas",
       "script": "پانکراس"
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 18,
     "parent": 15,
     "lang": "English",
     "refs": null,
     "words": [
      {
       "translit": "pancreas",
       "gloss": null,
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
    {
     "id": 19,
     "parent": 0,
     "lang": "Latin",
     "refs": "KLN:378",
     "words": [
      {
       "translit": "crusta",
       "gloss": "hardened by freezing",
       "script": null
      },
      {
       "translit": "crŭdus",
       "gloss": "bloody, raw",
       "script": null
      }
     ],
     "note": null,
     "quote": null
    },
```


### [2026-09-06T21:15:00.236Z] TOOL RESULT

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
```


## [2026-09-06T21:15:31.958Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KLN','IEC','SOD','MON','VOP','AHD','BRT','SYN','WLD','LEW','LAT','SKT','ARY','HRN','HUB','FSD','WEB','PHD']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600])\n    print()\n\"",
 "description": "Check refs_online entries"
}
```


## [2026-09-06T21:15:33.359Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-276.json'))\nprint(json.dumps(d['entries'][2]['nodes'][19:],ensure_ascii=False,indent=1))\nprint(json.dumps(d['entries'][3:],ensure_ascii=False,indent=1))\n\"",
 "description": "Tail of JSON"
}
```


### [2026-09-06T21:15:33.756Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
```


### [2026-09-06T21:15:35.877Z] TOOL RESULT

```
[
 {
  "id": 20,
  "parent": 19,
  "lang": "English",
  "refs": null,
  "words": [
   {
    "translit": "crust",
    "gloss": null,
    "script": null
   },
   {
    "translit": "crude",
    "gloss": null,
    "script": null
   }
  ],
  "note": null,
  "quote": null
 }
]
[
 {
  "root": {
   "name": "Krk",
   "redirect": "Kerk"
  },
  "nodes": []
 }
]
```


## [2026-09-06T21:15:43.054Z] TOOL CALL #7: Bash

```json
{
 "command": "pdftoppm -f 276 -l 276 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg276\" 2>/dev/null || pdftoppm -f 276 -l 276 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg276; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 276"
}
```


## [2026-09-06T21:15:45.638Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==629||NR==630' POK_02.txt 2>/dev/null | head -80; echo \"=== offset check ===\"; grep -n \"page_offset\" -A2 /dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));print(d['POK']['page_offset']);print(d['KLN']['page_offset']);print(d['IEC']['page_offset'])\"",
 "description": "Pokorny page offsets"
}
```


### [2026-09-06T21:15:45.722Z] TOOL RESULT

```
total 19000
drwx------ 2 sfmqrb sfmqrb    4096 Sep  6 17:15 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     352 Sep  6 17:14 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb 5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb 1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb    1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb 8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb   10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb   19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb   12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb   25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb   17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb  105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb  122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb  157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65729 Sep  6 17:10 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76740 Sep  6 17:15 pg276.png
```


### [2026-09-06T21:15:47.551Z] TOOL RESULT

```
=== offset check ===
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


## [2026-09-06T21:15:52.348Z] TOOL CALL #9: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg276.png"
}
```


### [2026-09-06T21:15:53.009Z] TOOL RESULT

```

```


## [2026-09-06T21:15:53.006Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-06T21:16:04.530Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg276.png')\nprint(im.size)\n# crop Greek cros box + Avestan box + empty box\nim.crop((580,980,1200,1180)).resize((1240,400)).save('c_cros.png')\nim.crop((580,1380,1120,1620)).resize((1080,480)).save('c_av.png')\nim.crop((1300,1370,1980,1620)).save('c_empty.png')\n\"",
 "description": "Crop regions of page image"
}
```


### [2026-09-06T21:16:07.185Z] TOOL RESULT

```
(2550, 3300)
```


## [2026-09-06T21:16:09.986Z] TOOL CALL #11: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_cros.png"
}
```


### [2026-09-06T21:16:10.011Z] TOOL RESULT

```

```


## [2026-09-06T21:16:10.205Z] TOOL CALL #12: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_av.png"
}
```


### [2026-09-06T21:16:10.223Z] TOOL RESULT

```

```


## [2026-09-06T21:16:17.953Z] TOOL CALL #13: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_empty.png"
}
```


### [2026-09-06T21:16:17.965Z] TOOL RESULT

```

```


## [2026-09-06T21:16:28.602Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaf for p.621 (leaf=p-344=277 -> NR 278) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR>=277 && NR<=279' POK_02.txt | head -150",
 "description": "Pokorny p.621"
}
```


### [2026-09-06T21:16:30.276Z] TOOL RESULT

```
=== POK_02 leaf for p.621 (leaf=p-344=277 -> NR 278) ===
(überliefert  kragis)  ,HeerS  caryawoytis  Akk.  Sg.  ,Heerschau<;
vd.  auch  oben  1.  kar-  S.  530,  wo  die  bsl.  Beispiele  auch  hierher  ge- hören  können.
WP.  I  353,  462,  Trautmann  118.
kos{e)lo-  ,HaseP.
Lat.  corulus  ,Haselstaude^  colurnus  {*corulinos)  ,aus  Haselholz'; air.  coli,  acymr.  coli  usw.  ,HaseP  (auch  gall.  Coslo- in  EN); ahd.  hasal{a),  ags.  hoBsel,  aisl.  hasl  m.  »HaseP,  ahd.  hesilin,  ags.  toZen, ,aus  Haselholz';
alit.  kasulas  ,  Jäger  spieß*  als  ,Hasler'. WP.  I  464,  WH.  I  280.
kost'  ,Bein,  Knochen'.
Lat.  Costa  i.  ,Rippe';  abg.  kosth  L  ,Knochen'  (skr.  kost  ,Rippe')- Annahme  eines  Ä;-Präfixes  (zu  lat.  os  usw.)  unglaubhaft. WP.  I  464,  WH.  I  281.
krUpo-  (kropo-?)  ,Dach';  nur  germ.  und  slav.
Aisl.  hröf  n.  ,Dach,  Schuppen',  ags.  hröf  ,Dach,  Schiffsverdeck',   engl. roof,  mnd.  röf  ,Schutzdach,  Deckel,  Decke'; abg.  strop^  ,Dach'  (*kräpos). WP.  I  477  f.,  Trautmann  309.
krä-  s.  oben  S.  574  ff.  unter  1.  ker-  und  S.  582  unter  ker9-. krät-  s.  oben  S.  584  unter  ke7^t-.
krä[u]-  :  krou- :  kru-  , aufeinander,  auf  einen  Haufen  legen,  zudecken,  ver- bergen'; krQuo-  jDach',  krüsiä  ,Haufe'.
Air.  crdu,  crö  m.  ,Stall,  Hütte,  Verschlag'  (*Ärawo-),  cymr.  craw  m.  ,Stall', com.  croiü,  bret.  kraou  ds. ;
lit.  krdujuj  kröviau,  krduti  ,aufeinanderlegen,  häufen,  packen,  laden'; lett.  kraünu  (krauju),  krävu,  kraut  ,häufen';  Iter.  lit.  krdustyti,  lett. krausttt  ,häufen',  kravdt  ,zusammenraffen',  krauja,  krava,  kruva  ,Stein- haufen';  lit.  krüvä  (Akk.  krüva)  ,Haufe',  kridute,  krdute  , Bodenraum';
abg.  krov^  ,Dach'  {*krduo-\  ablaut.  kryjg,  kryti  , decken,  hüllen,  ver- bergen' usw. ;
mit  s-Erweiterung:
russ.  krysa  ,Dach',  serb.  krisom  Adv.  ,heimlich'  (usw.,  ebenso:) aisl.  hreysar  PL  f.,  hreysi  n.,  neben  norw.  rüsa,  ndd.  rüse  ,Haufe*;  aisl. Jiraun  n.  ,Steinhaufen,  steinerner  Grund'.
r
617
Auf  krä[u]-  beruht  vielleicht  lett.  kräju,  krdt  ,sammeln,  häufen*,  ahg. (mit  präsensbildendem  d)  kradg,  krasti  ,stehlen'.
Labialerweiterung  (-bh-):  gv.  ycQVfCToj  ,verberge*,  y.Qvcpfj  ,heimlich' u.  dgl.,  y.Qvßd7jv  ds.;
mit  p-Erw.  (vgl.  oben  -^QVTtro))  lett.  krdpju,  krdpu,  krdpt  ,stehlen,  be- trügen*, lit.  kröpti  jStehlen*;  über  got.  hröt  und  ags.  Jiröf  ,Dach*  s.  unter ]cred'  und  krapo-,  auch  Mühlenbach-Endzelin  Lett.-D.  Wb.  II  269;  toch.  B kraup-,  B  krop-  ;Sammeln%-  vgl.  auch  klep-]
für  aisl.  hraukr^  ir.  cruach  ,Haufe*  u.  dgl,  die  an  sich  einer  ic-Erwei- terung  unserer  Wz.  entstammen  könnten,  s.  eine  andere  Deutung  unter sker-,  skereu-  , drehen'.  Im  selben  Sinne  zweifelhaft  ist  anord.  skrüf  n. , aufgestapelter  Haufe*,  skrüfr  m.  , Schopf*,  norw.  dial.  skrauv  , Schaum- gipfel*, 
usw.  (hätten  bewegliches  s-).
Dentalerweiterungen  scheinen:  aisl.  hraud  f.  poet.  ,Brünne*,  ags. hread  f.  , Schmuck*;  aisl.  hrjöda  , decken,  schmücken',  ags.  hreodan  ds. (vgl.  lit.  krdudinu  ,lasse  laden?*)  neben  hyrst  m.  , Schmuck,  Rüstung*, ahd.  hrust  m.  ds.,  ahd.  (h)rusten  , rüsten*.
WP.  I  477,  Trautmann  139,  140.
kre-,  krei-,  kr-  s.  oben  S.  574  ff.  unter  1.  ker-.
kre-  s.  oben  S.  578  unter  4.  ker-,
5.  kreb-  s.  oben  S.  567  ff.  unter  1.  ker-.
krebb-,  krbbb-,  krembb-  ,vertrauen*??
Ai.  srambhate,  Partiz.  srahdha-  (mit  vi-  und  andern  Präp.)  ,vertrauen, sich  worauf  verlassen',  nisrmhhd-  ,sicher  auftretend';
air.  cräbud  ,Frömmigkeit,  Askese*  (*kröbMtu-s)  m. ;  cymr.  crefydd  (jünger creddyf)  , Glaube*  hat  sein  e  von  credu  , glauben*  bezogen.
WP.  I  478,  Kuiper  Nasalpräs.  146.
kred-  ,Gebälk*  (kred-?  s.  unten).
Got.  hröt  n.  ,Dach*,  anord.  hröt  ,Dach,  Dachraum*,  as.  ags.  hröst  , Sparren- werk des  Daches*  (*kröd-s-to-)  =  ndl.  roest  , Hühnerstange,  Hühnerleiter*, mhd.  rä2,  räze  , Scheiterhaufen*  (*kredä',  fem.  Kollektiv  wie  aksl.  krada)] mit  mhd.  räz(e)  ., Scheiterhaufen*  deckt  sich  mhd.  räZj  räze  ,Wabe*,  afr. rata,  mnl.  rate  ,Wabe',  woneben  mit  Ablaut  mnl.  rete  (*hretön-)  und  röte, mdartl.  noch  röte  (*hruti-)  ,Wabe*;
abg.  krada  , Scheiterhaufen,  Holzstoß*  (*kröda).
Als  ,Sparrenwerk,  aus  Latten  iisw.  Gezimmertes'  kann  hierhergehören: lit.  kreslas  ,stattlicher  Stuhl*,  lett.  kr^sls,  apr.  creslan  , Lehnstuhl*,  lit.  kräse
618  f
,Stulil*.  russ.  kreslo,  cech.  kreslo  ,Armstuh?,  sowie  lit.  krösnis^  lett.  krL^ ,Ofen',  ksl.  krosno  ,liciatoriumS  russ.  krösno  »Webstuhl;  Stück  Leinwand^- bulg\  krosno  , Aufzug  beim  Webstuhl;  Torriegel',   krösna  f.   ,Wiege*,  skr! krosna  , Webstuhl',  öech.  krosna,  krüsna  (alt  krösna)  ,TraggestelP. WP.  I  485 f.,  Trautmann  141.
kred-  s.  oben  S.  579  f.  unter  kered-.
1.  kreg-  (und  kerg-?)  ,quälen'?
Ai.  kdrjati  ,quält,  peinigt'  (Dhätup.);
aisl.  hrekja  ,quälen,  belästigen,  verfolgen',  afries.  hreka  , reißen'.
WP.  I  484.
2.  kreg-  ,Schallwort'  s.  oben  S.  569  unter  1.  ker-.
I.  krei-  ,über  etwas  drüberhinstreifen,  berühren*.
Aisl.  hrina  ,wirken',  ags.  asächs.  ahd.  hrinan  ,berühren,  streifen'  (no-  ,7^-- Präs.);  nach  Wissmann  Nom.  postverb.  152 ff.  hierher  ags.  hrenian  ,einen  *^.^ Geruch  ausströmen',  afries.  stark.  V.  hrena  ,einen  Geruch  empfinden' ;  ags»  ^^_ aisl.  hrlniy  mhd.  rim  ,Reif';  |^
lit.  krenä  f.  ,Rahm,  Sahne'  (,was  man  abstreift,  abschöpft'),  lett.  kreju^  V-v^ krhjuj  kriet  ,die  Sahne  von  der  Milch  abschöpfen',  kreims  m.  ,Rahm'  (aus deverbalena  kr'hjums  ,was  man  abstreifen  kann');
  ^'■
daneben  mit  germ.  p:  asächs.  hrlpOj  ahd.  hrlfo  ,Reif'.
WP.  I  478,  Trautmann  141.
2»  krei-f  kreig-,  kreik-  s.  oben  S.  567  ff.  unter  1.  ker-.
krei-  etwa  ,hervorleuchten,  sich  hervortun'.
Ai.   sA-   t   , Schönheit,    Pracht,  Wohlgefallen,   Reichtum,    Herrlichkeit*, av.  srl-  , Schönheit',  ai.  sri-ld-  ,schön,  herrlich',  d-srlra-  ,unschön',  av.  srlra-  '] ,schön',    Kompar.   ai.  ireyas-^   av.  srayah-j   Superl.    ai.   srt^tha-    (srdistha-)^ av.    sraesta-j    ai.    sremdn-    m.    , Auszeichnung,   Vorrang',    av.    srayan-   n. , Schönheit',   Adj.  , schön',  ai.  sriydse  Dat.  n.  ,schön';
hom.  poet.  Tigelcov  ,edel,  fürstlich,  Herrscher'  (siQi)  x^etwv,  v.QBLOvaa)  y^oeatv Pind.  Aisch.,    nachhom.   EN    Koeovaa    (*x^fi[t]-ovr-   Partiz.  , hervorleuch- tend'(?),  steht  vielleicht  für  kqslov-  Komparativ). ■      WP.  I  478,  Schwyzer  Gr.  Gr.  I  526.
I.  krek-  (-k-?)  ,schlagen',  auch  vom  Festschlagen  des  Gewebes,  des  Ein- schlages in  der  Weberei,  daher  auch  ,weben,  Gewebe'. Gr.  x^exw  ,schlage,  klopfe ;  schlage  das  Gewebe  fest',  Tcgöycrj  ,Einschlag- faden,  Gewebe',   xqö^   ds.,  y,Qoy,ovv   ,weben',   xqoy,vq,  -vdog   f.  , Wollflocke';
619
aisl.  hrcdl  (^hrardhüaz)  ,Stab  zum  Festmachen  des  Gewebes*,  ags.  kreol (*hrehulaz)  ,Haspel';  ags.  hroRgl  n.  ,Kleid,  Gewand*,  engl,  rail,  afries.  hreil\ ahd.  Tiregil  n.  ,indumentum,  spolium*;
lett.  kr^kls  ,B[emd*;
wenn  das  lett.  Wort  sein  zweites  k  durch  westidg.  Einfluß  empfangen hat,  kann  auch  folgende  slav.  Sippe  angereiht  werden:  russ.  kresü,  kresdth ^mit  dem  Feuerstahl  Feuer  schlagen',  klr.  kresdty^  kresnüty  ,Feuer  schlagen*, dial.  ,hauen,  schlagen  überhaupt',  skr.  kreserrij  kresati  , Feuer  schlagen; Steine  behauen;  Äste  abschlagen'  (usw.,  s.  Berneker  611).
WP.  I483f.
2.  krek-j  krk-  ,Froschlaich,  Fischlaich,  schleimiges  Zeug  im  Wasser'.
Aisl.  hi'ogn  n.,  ahd.  {h)rogan,  rogen  ,Rogen,  Laich';
lit.  kurkulai  PL  ,Froschlaich',  lett.  kui^kulis  ds.,  lit.  apkurköti  ,sich mit  Wassermoos  beziehen' ;
trotz  lautlicher  Schwierigkeiten  hierher  die  slav.  Sippe  von  serb.  okrijek jWassermoos,  Algen',  slov.  kr^kj  zaho-kr^6ina  ,Froschlaich'  usw.,  ablaut. slov.  kräk  ,Froschlaich ;  grüner  Überzug  an  Pfützen,  Wassermoos',  mit auffälligem  ja :  russ.  krjak  ,Froschlaich',  6ech.  mdartl.  okraky  , Sammel- name für  Wasserpflanzen'?
WP.  I  483,  Berneker  613  f.
j.  krek-  ,Schallwort*  s.  oben  S.  567  ff.  un
```


## [2026-09-06T21:16:34.757Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=280 && NR<=282' POK_02.txt | sed -n '1,200p'",
 "description": "Pokorny p.620-622"
}
```


### [2026-09-06T21:16:36.436Z] TOOL RESULT

```
ter  1.  ker-.
4.  krek-  :  krok-,  mit  -u-  erweitert  ,ragen,  hervorragen'?  und  ,vorspringender Balken  oder  Pflock  u.  dgl.'.
Gr.  ^iQÖaaai  ,Mauerzinnen,  Absätze,  stufenartig  an  der  Mauer  hinauf- geführte Steine'  (*krok{ä)',  dazu  wohl  auch  als  ,vorspringender  Faden' ycQoaaoL  ,hervorragende  Einschlagfäden,  Verbrämung';
air.  crich  f.  (*krekua)  ,Ende,  Grenze,  Furche'  =  cymr.  crib  ,Kamm, Spitze,  Gipfel';
ahd.  *Ära^en,  mhd.  nhd.  ragen,  mhd.  rac  ,steif',  zu  r^Äe,  ahd.  *hräM ,starr,  steif,  ferner  mhd.  nhd.  rc^e/i  ,ragen  machen,  aufrichten';  ags.  ofer- hräegan  ,überragen';
lit.  zem.  kräke  f.  , Stock';
slav.  *kroky,  Gen.  -^ve  in  russ.  krökva  , Stange;  Knebel;  Dachsparren',  6ech. krokva,  alt   krokeVy    Gen.  krokve  , Sparren,   Dachsparren'    (Berneker  621).
WP.  I  482,  Trautmann  139.
krem-  s.  oben  S.  580  f.  unter  kerem-.
620  •
1.  krep-,  kj^p'  ,Leib,  Gestalt'  (oder  k'^erp-?  s.  unten).
Ai.  krpä   Instr.  Sg.  , Gestalt,  SchönheitS    av.  kdrdfi,  kdhrjpdm    ,Gestalt Leibs  mpers.  karp  ,Körper'  (av.  xrafstra-n.  ,Raubtier'  aus  *^^ep  +  *[e](£-<ro!^ zu  ed'  ,essen*?);
vielleicht(?)  alb.  sh-krep,  sh-kep  ,g-leiche  ein  wenig'  (sÄ  =  idg.  sewi,  som^srn.] vgl.  zur  Bed.  ahd.  gi-llh  ,gleich' :  llh  ,Leib') ;
lat.  corpus,  -oris  n.  ,Leib,  Körper*;
mir.  crl  f.  ,Leib*  {^kipes)]
ahd.  {h)ref  m.  ,Leib,  Unterleib,  Mutterleib*,  afries.  href,  hrif  ,Bauch*1 ags.  hrif  n.  ,Mutterleib,  Bauch*  {*Jirefiz-  =  *krepes-\  ags.  mid(h)rif,  afries.^ midref  , Zwerchfell*  (,*in  der  Mitte  der  Leibeshöhle*).
Gr.  TtQaniQ,  meist  PL  -idsg  , Zwerchfell',  das  den  Anlaut  als  k^  erwiese, ist  in  seiner  Zugehörigkeit  fraglich,  da  die  entsprechende  Bedeutung  von ags.  mid{h)rif  wohl  auf  dem  1.  Gliede  des  Kompositums  beruht;  es  müßte denn  Ttqartig  eine  Kurzform  zu  einer  ähnlichen  Zusammensetzung  sein- nach  Ven
dryes  RC  44,  313  ff.,  Specht  KZ.  68,  193  ff.  wäre  idg.  *Ä:^erp! tabuistische  Metathese  zu  ^perk^:.-  ,Leben,  Welt,  Eiche*  (got.  fairhus ,Welt*).
WP.  I  486  f.,  WH.  I  277  f.
2.  krep-  s.  oben  S.  567  ff.  unter  1.  ker-.
1,  krep-  ,stark,  fest*;  nur  germ.  und  slav.
Aisl.  hrcefa  ,ertragen*  (vgl.  russ.  krepithsja  ,ausdauern,  beharren*);  abg. krep^,  kräp^k^  ,f est,  stark* ;
cymr.  craff  ,schnell*  aus  aisl.  krappr  ds.  (=  krappr  ,engS  S.  388). WP.  I  487.
2.  krep-  s.  oben  S.  581  unter  kerdp-,
I.  kret-  , schütteln*  (ob  als  ,stoßen*  mit  kret-  , schlagen*  identisch?  oder  Er- weiterung von  sker-  , drehen,  kreisend  schwingen*?).
Lit.  kreciüj  krSsti  , schütteln,  schüttelnd  streuen*,  Iter.  kratau,  -yti  ds., kretü  kreteti  ,sich  hin  und  her  bewegen,  sich  schütteln,  schlottern*,  lett. krest  ,schütteln*,  Iterat.  kratit,  kr^tulis  ,Art  Sieb*  (lett.  kraitdt  ,taumeln* Entgleisung  von  einem  *krit-  aus) ;
mir.  crothaim  ,schüttle*,  gall.-rom.  '^■crottiäre  ,schütteln* ;
ahd.  redan  ,sieben*,  nhd.  mdartl.  räder,  rädel  ,Sieb*;  aisl.  hradr  ,schnell*, ags.  ArcBjb,  hrcßd  ,schnell,  behend*,  engl,  rather  ,lieber*,  ahd.  hrad,  hrat ,velox,  strenuus* ;  aisl.  hrceda  ,erschrecken  (trans.)*,  hrceddr  ,entsetzt* ;
auch  ags.  ä-hreddan  ,befreien,  retten*,  ahd.  retten  ,bewegen,  treiben; befreien,  retten'  als  ,von  der  Gefahr  wegstoßen*?
WP.  I  484,  Mühlenbach-Endzelin  II  274,  261,  256.
621
jcret'  »schlagen*;  wohl  ursprünglich  mit  1.  Jcret-  identisch.
Qr.  y.QÖTog  ,jedes  durch  Schlagen,  Stampfen,  Klatschen  entstehende Geräusch*;  %Qoreiv  ,klatschen,  klopfen,  schlagen*, x^dra^oi^, Klapper',  yiQÖzacpog ^Schläfe*  (eigentlich  ,*das  Klopfen*);  ,Berghang;  Seite*,  ^qoxacpig  ,Spitz- hammer* ;
dazu  mit  ursprüngl.  wohl  bloß  präsentischer  Nasalierung  aisl.  hrinda, hrattj  ags.  hrindan,  hi^and  ,stoßen*;
vielleicht  die  slav.  Sippe  von  ahg.  krostg^  krotiti  ,zähmen*,  krot^k^  ,sanft, mild,  mäßig*,  wenn  ursprüngl.  , durch  Prügeln  mürbe  machen'?
WP.  I  484  f.,  Berneker  624.
X.  kreu-,  kreuo-ikrü-  1.  ,dickes,  stockendes  Blut,  blutiges,  rohes  Fleisch*, vermutlich  ,g
eronnen  (vom  Blut)*,  dazu  eine  2.  Gruppe  kreus-,  krus- für  ,Eis  (als  erstarrendes),  Kruste  (ursprüngl.  von  Eis  oder  Wund- schorf), Eisscholle,  Erdscholle*  (s.  unten)  und  verbal , frieren,  schaudern (Gänsehaut)*,  kreus-s-  n.  ,rohes  Fleisch*,  krouio-  n.  ,Blut*,  krü-s  f.  ,Blut*.
A.  Ai.  kravis-  n.  ,rohes  Fleisch*  (=  gr.  x^f/ag),  kravyam  n.  ,Blut* (*krouio-  =  apr.  krawian  n.),  krü-rd-  ,blutig,  grausam*  =  av.  xrüra-  ,blutig, grausig,  grausam*  (:  lat.  crüdus?)  im  Kompositum  mit  i-  für  ro-St.,  av. xrvi-dru-  ,der  eine  blutige  Holzwaffe  führt*,  d.  i.  xruvi-dru-,  av.  xrü-  f., xrüm  (=  xruvdm)  Akk.  , Stück  blutiges  Fleisch*,  xt-vant-  (d.  i.  xrüvant-) ,grauenhaft,  grausig*  ( :  lat.  cruentus),  xrvlSyant-  ,blutdürstig,  Grausen  er- regend*, xrüta-  ,grausig,  grausam*,  xrünya-  n.  ,Bluttat,  blutige  Mißhand- lung*, xrüma-  ,grauenhaft,  grausig*;  mit  einer  Bedeutung  ,*geronnen'  = ,dick,  hart*,  ai.  krüddyati  , macht  dick,  fest*,  av.  xrnzdra-  ,hart*  (daneben wieder  mit  i-  statt  ro-St.  im  Kompositum  xru^di-vacah-  ,mit  derber,  lauter Stimme  sprechend*),  xraoidva-  ,hart*;
gr.  yiqeag  n.  ,Fleisch*  (^krmds)]
lat.  cruentus  ,blutig*  (s.  oben),  cruor  m.  ,das  rohe,  dicke  Blut*  (*kreuös)j osk.  krustatar  ,crusta  tegitor*  (Denom.  von  *krus-ta),  lat.  crusta  , Kruste, Rinde,  Schorf*,  ursprüngl.  ,das  fest  gewordene  Blut  auf  einer  Wunde* (*krüs-ta),  crüdus  ,roh,  rauh,  hart*  (*krü-do-),    crüdelis  ,grausam,  herzlos*;
gall.-rom.  crödios  ,hart*  {*kroudios)-
mir.  cru  (j^krüs).  Gen.  crduj  crö  (*kruuos)j  cymr.  craUj  corn.  crow  (^kruua) ,Blut*  (s.  Pedersen  KG.  I  61,  251  f.,  II  97,  Lohmann  ZceltPh.  19,  63  f.),  air. crüaid  (*kroudis)  ,hart,  fest*,  bret.  kriz  (*krüdis)  ,cru,  cruel*  (Pedersen KG.  I  207 ;  nicht  Lw.  aus  lat.  crüdus) ;  das  d  im  Kelt.  und  Lat.  durch Dissimil.  aus  r?
lit.  kraüjas  ,Blut*  (:  ai.  kravya-m),  apr.  crauyo,  krawian  ds.,  lit.  krüvinas ,blutig',  krüvinu  ,mache  blutig*,  Partiz.  krüvintas  ,blutig  gemacht*,  lett. kreve  ,geronnenes  Blut,  Schorf,  Kruste';
622  •
slav.    *kry   (*krüs\    Gen,    *krzve  ,Blut'  in    slov.    krt,    apoln.   kry^  aksL^ krzvh-,    aksl.  ki-bVhm  ,blutig*  (=  lit.  kriimnas)-^  ^
ahd.  (h)rö,  (h)rawer,  as.  Arä,  ags.   hreaw,  aisl.   Ärär  ,roh*  {*hrawa-),
B.  Skyth.  *xrohu-kasi-j  gr.  KavY^aaig  , Kaukasus*  (als  ,eis-glänzend^)  •
gr.  r()  xovog  ,Frost'  (=  *x^?;ö'og?),  y.Qvoraivü)  ,mache  gefrieren',  ^^Qvaialloö  ** ,Eis;  Kristalls  x^vjwdg  ,Frost'  (*x^t'(r^dg),  von  x^vog  abgeleitet  (?)  x^rd^t^  ' »schauerlich*,  'kqvsqöq  »schauerlich,  grausam*;
ai
```


## [2026-09-06T21:16:58.740Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### KLN Caucasian\"; grep -n -i \"Caucasian\" KLN_1966.txt | head -20\necho \"### KLN crystal\"; grep -n -i \"^crystal\\|crystal, n\\|krystallos\" KLN_1966.txt | head -20\necho \"### KLN cruel/crude/crust\"; grep -n -i \"cruentus\\|crudelis\" KLN_1966.txt | head -20",
 "description": "Grep Klein"
}
```


### [2026-09-06T21:16:58.825Z] TOOL RESULT

```
### KLN Caucasian
6830:Caucasian,  adj.  and  n.  —  Formed  with  suff.  -ian fr.  L.  Caucasus,  fr.  Gk.  Kauxaau;,  fr.  Scythian Kpoo-xxcu.?,  ‘Caucasus’,  a  compound  meaning lit.  ‘(the  mountain)  shining  with  ice’;  see  Walde- Hofmann,  LEW.,  I,  pp.  295-96,  s.v.  criista.  The first  element  of  this  compound  is  a  derivative  of I.-E.  base  *qreu-,  ‘to  be  icy’.  For  derivatives  of *qrus-,  an  enlarged  form  of  base  *qreu-  see crust,  crystal.  The  second  element  is  rel.  to  Gk. y.odsiv  (for  "xifieiv),  ‘to  burn’ ;  see  caustic, cauchemar,  n.,  incubus.  —  F.,  a  hybrid  coined from  the  blend  of  OF.  chaucer  and  Picard  cau- quer,  ‘to  trample’  (both  derived  fr.  L.  calcare, of  s.m.,  fr.  calx,  gen.  calcis,' heel'),  and  fr.  MDu. marc,  incubus'.  See  Calceolaria  and  mare,  ‘in¬ cubus',  and  cp.  the  first  element  in  caltrop, caucus,  n.,  private  meeting  of  the  leaders  of  a  poli¬ tical  party.  —  A  word  of  Algonquian  origin,  lit. meaning  ‘counselor’.
6855:Derivative:  causeway,  tr.  v, causey,  n.,  a  causeway  (dial.)  —  ME.  cauce,  fr. ONF.  cauciee,  corresponding  to  F.  chaussee, ‘causeway’,  fr.  VL.  (via)  calctata,  lit.  ‘a  road paved  with  limestone’,  fern.  pp.  of  calciare,  ‘to pave  with  limestone’,  fr.  L.  calx,  gen.  calcis, ‘lime, limestone’.  See  calcareous  and  cp.  chaussee. caustic,  adj.,  burning,  corrosive.  —  F.  caustique, fr.  L.  causticus,  fr.  Gk.  xookttixoc,  ‘capable  of burning,  corrosive’,  fr.  xxocrro?,  ‘burnt’,  verbal adj.  of  xcciEiv,  which  stands  for  *xif-ts'.v,  ‘to burn,  set  on  fire’,  fr.  I.-E.  base  *keu-,  *kii-,  ‘to burn,  heat’,  whence  also  Lith.  kttle,  ‘blight,  mil¬ dew',  kiileti,  ‘to  become  blighted’.  Cp.  caeoma, caliber,  calm,  catacaustic,  Caucasian,  cautery, diacaustic,  encaustic,  holocaust,  hypocaust,  ink, Nausicaa.
9800:crust,  n.  —  ME.,  fr.  OF.  crouste  (F.  croute),  fr. L.  crusta,  ‘the  hard  surface  of  a  body,  rind, crust,  shell’,  which  stands  for  *crus-ta,  and  lit. means  ‘that  which  has  been  hardened  by  freez¬ ing’,  and  is  cogn.  with  Gk.  xpuop  (prob.  for *xp')aoc),  ‘icy  cold,  frost’,  xpusp6c;,  ‘icy,  chilling’, xpu(i6?  (for  *xpua|i6c),  ‘frost’,  xpiiaraXXop,  ‘ice, crystal’,  Toch.  A  kuras,  B  krost,  ’cold’,  Lett. kruvesis,  ‘mud  frozen  in  the  field;  roughness  of the  soil’,  Lith.  at-krusti,  ‘to  revive’  (said  of frozen  people),  OHG.  (h)rosa,  (h)roso,  ‘ice,  crust’, ON.  hriosa,  ‘to  shudder’,  OE.  hruse,  ‘earth, ground’.  All  these  words  derive  fr.  I.-E.  *qreus-, *qrus-,  *qruwes-,  enlarged  forms  of  base  *qreu-, ‘icy,  solid,  coagulated,  congealed’,  whence  also L.  crudus,  ‘raw’.  See  crude  and  cp.  Crustacea, encrust.  Cp.  also  crouton,  crystal,  custard  and the  first  element  in  Caucasian.
23363:Melanochroi,  n.  pi.,  members  of  the  Caucasian race  having  black  hair  and  pale  complexion.  — ModL.,  lit.  ‘black  and  pale’,  compounded  of melan-  and  Gk.  ro^pO?,  ‘pale’.  See  ocher  and  cp. Xantochroi.
24913:nail,  n.,  1)  the  horny  substance  on  the  ends  of  the fingers  and  toes;  2)  a  small  spike  of  metal  or wood.  —  ME.  naile,  neil,  fr.  OE.  nsegl,  ntegel, ‘fingernail;  metal  nail,  peg’,  rel.  to  OS.,  OHG. nagal,  OFris.  neil,  MDu.  naghel,  Du.,  MHG., G.  nagel,  ‘fingernail;  metal  nail’,  ON.  nagl,  ‘fin¬ gernail’,  nagli,  ‘metal  nail’,  Goth,  ganagljan,  ‘to nail’,  fr.  I.-E.  base  *nogho-.  *ngho-,  *ongho-, ‘nail’,  whence  also  OI.  ahghrih,  amhrih,  ‘foot’, Gk.  ovu^,  L.  unguis,  ‘nail,  claw’,  OSlav.  noga, Russ,  noga,  Czech  and  Slovak  noha,  ‘foot’,  Lith. naga,  ‘hoof’,  ndgas,  Lett,  nags,  ‘nail’,  OPruss. nage,  ‘foot’,  OSlav.  nogiiri,  ‘nail,  claw’,  Lith. nagiitis,  OPruss.  nagutis,  ‘fingernail’,  OIr.  ingen, OW.  eguin,  W.,  Co.,  ewin,  Bret,  twin,  ‘nail,  claw’. Cp.  OI.  nakhdft,  Pers.  naxun,  ‘nail,  claw’,  where qh-  (for  gh-)  is  prob.  due  to  Caucasian  influence. —  Cp.  agnail.  Cp.  also  onyx,  ungual. Derivatives:  nail,  v.  (q.v.),  nail-less,  adj.
### KLN crystal
537:crystallogr.
538:crystallography
9833:crystallography,  n.,  the  study  of  the  formation  of crystals.  —  Compounded  of  crystallo-  and  Gk. -yponpla,  fr.  Ypatpeiv,  ‘to  write’.  See  -graphy. crystalloid,  adj.,  resembling  a  crystal.  —  Com¬ pounded  of  crystallo-  and  Gk.  -osiS-fo,  ‘like’, fr.  eXSo?,  'form,  shape’.  See  -oid. crystallomancy,  n.,  divination  by  crystal  gazing. —  Compounded  of  crystallo-  and  Gk.  [xavxeta, ‘oracle,  divination’.  See  -mancy. csardas,  n.,  a  Hungarian  national  dance.  — Hung,  csdrdds.
### KLN cruel/crude/crust
9777:crucify,  tr.  v.  —  OF.  ( =  F.)  crucifier,  fr.  L.  cruci- figere,  orig.  spelled  in  two  words:  cruci  figere, ‘to  fix  to  the  cross’ ;  see  crucifix.  OF.  crucifier  was influenced  in  form  by  the  many  verbs  ending in  -fier,  a  suff.  corresponding  to  L.  -ficare. Derivatives:  crucifi-ed,  adj.,  crucifi-er,  n. crude,  adj.,  1)  raw;  not  refined;  2)  not  finished. —  L.  crudus,  ‘raw,  crude,  not  cooked’,  fit.  ‘trick¬ ling  with  blood,  bleeding’,  rel.  to  cruor,  ‘blood (flowing  from  a  wound)’,  cruentus,  ‘stained with  blood,  bloody’,  fr.  I.-E.  base  *qrewt-, *qreu-,  ‘coagulated,  congealed,  bloody’,  whence also  OI.  kravih ,  ‘raw  flesh’,  kravyam,  ’blood’, krurdh,  ‘raw,  bloody,  cruel’,  Avestic  xrum( acc.), ‘a  piece  of  bloody  flesh’,  xriira-,  ‘bloody,  cruel'.
9781:cruentation,  n.,  oozing  of  blood,  esp.  from  a  dead body  after  incision.  —  L.  cruentatio,  gen.  -dnis, ‘a  staining  with  blood',  fr.  cruentatus,  pp.  of cruentare,  ‘to  stain  with  blood’,  fr.  cruentus, ‘bloody’,  fr.  cruor,  "blood’,  which  is  rel.  to crudus.  See  crude  and  -ation. cruet,  n.,  a  small  glass  bottle  for  vinegar,  oil, etc.  —  AF.,  dimin.  of  OF.  crue,  cruie,  ‘an  earth¬ en  pot’,  fr.  Frankish  *kruka  (whence  also OProven?.  cruga,  and  F.  cruche,  ‘pitcher’),  which is  rel.  to  MHG.  kruche,  ‘pitcher,  jug’,  and  to OHG.  kruog,  of  s.m.  See  crock,  ‘earthen  pot', cruise,  intr.  and  tr.  v.  —  Du.  kruisen ,  ‘to  cross; to  cruise’,  fr.  kruis,  ‘cross’,  fr.  L.  crucem,  acc. of  crux,  ‘cross’.  See  cross,  n.
```


## [2026-09-06T21:17:21.115Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '9825,9835p' KLN_1966.txt\necho \"=== leaf numbers ===\"\npython3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nimport re\nfor target in [6830,9777,9800,9833]:\n    off=sum(len(l)+1 for l in lines[:target-1])\n    leaf=t.count('\\f',0,off)\n    print(target, 'leaf',leaf, 'approx printed p.', 2*(leaf-12), '-', 2*(leaf-12)+1)\nEOF",
 "description": "Klein crystal entry and leaf math"
}
```


### [2026-09-06T21:17:22.884Z] TOOL RESULT

```
Derivative:  cryptorchid-ism,  also  cryptorch-ism, n.
Cryptostegia,  n.,  a  genus  of  woody  vines  of  the milkweed  family  (bot)  —  ModL.,  compounded
Cryptotaenia
380
of  crypto-  and  Gk.  oziyi),  ‘roof’,  which  is  rel.  to (ru-eyo?,  ‘roof’,  fr.  <jx£ye!.v,  ‘to  cover’.  See  ste- gano-.
Cryptotaenia,  n.,  a  genus  of  plants  containing the  honewort  ( bot .)  —  ModL.,  compounded  of crypto-  and  Gk.  xaivtcc,  ‘fillet’.  See  taenia, crystal,  n.  —  ME.  cristal,  fr.  OF.  cristal  (F.  crys¬ tal ),  fr.  L.  crystallum ,  fr.  Gk.  xpiioxaXXo:;,  ‘ice ; crystal’,  which  is  rel.  to  xpuaxalveiv,  ‘to  con¬ geal,  freeze’.  Both  these  words  derive  fr.  xpt)o<; (for  ‘xpuCTop),  ‘frost’,  which  is  cogn.  with  L. crusta,  ‘crust’.  See  crust  and  cp.  words  there referred  to.  Cp.  also  crymodynia,  cryogen, cryolite.
Derivatives:  crystal,  adj.  and  tr.  v.,  crystalline (q.v.),  crystall-ize,  tr.  and  intr.  v.,  crystalliz¬ ation,  n.,  crystalliz-ed ,  adj.,  crystalliz-er,  n. crystall-,  form  of  crystallo-  before  a  vowel, crystalline,  adj.  —  F.  crystallin,  fr.  L.  crystal¬ line,  fr.  Gk.  xpuaxaXXtvo?,  ‘of  crystal’,  fr.  xpu- axaXXo?.  See  crystal  and  -ine  (representing  Gk. -tvos.
Derivatives :  crystalline  n.,  crystallin-ity,  n. crystallo-,  before  a  vowel  crystall-,  combining form  meaning  ‘crystal’.  —  Gk.  xpuaxocXXo-, xpuaxaXX-,  fr.  xp’jaxaXXoc.  See  crystal, crystallographer,  n.  —  See  crystallography  and agential  suff.  -er.
crystallography,  n.,  the  study  of  the  formation  of crystals.  —  Compounded  of  crystallo-  and  Gk. -yponpla,  fr.  Ypatpeiv,  ‘to  write’.  See  -graphy. crystalloid,  adj.,  resembling  a  crystal.  —  Com¬ pounded  of  crystallo-  and  Gk.  -osiS-fo,  ‘like’, fr.  eXSo?,  'form,  shape’.  See  -oid. crystallomancy,  n.,  divination  by  crystal  gazing. —  Compounded  of  crystallo-  and  Gk.  [xavxeta, ‘oracle,  divination’.  See  -mancy. csardas,  n.,  a  Hungarian  national  dance.  — Hung,  csdrdds.
cten-,  form  of  cteno-  before  a  vowel, ctenidium,  n.,  the  gill  of  a  mollusk  ( zool .)  — ModL.,  formed  with  suff.  -idium  fr.  Gk.  xxelp, gen.  xxEvop,  ‘comb’.  See  cteno-. cteno-,  before  a  vowel  cten-,  combining  form meaning  ‘comblike’  (zool.)  —  Gk.  xxevo-,  xxev-, fr.  x-ret?,  gen.  xxevo?,  ‘comb’,  which  stands  for *pkten,  and  is  rel.  to  rrexetv,  ‘to  comb’,  and cogn.  with  L.  pecten,  ‘comb’,  pectere,  ‘to  comb’. See  pecten.
ctenoid,  adj.,  comblike.  —  Compounded  of cten-  and  Gk.  -0Ei8ir]i;,  ‘like’,  fr.  e!8o?,  ‘form, shape’.  See  -oid.
=== leaf numbers ===
6830 leaf 143 approx printed p. 262 - 263
9777 leaf 208 approx printed p. 392 - 393
9800 leaf 209 approx printed p. 394 - 395
9833 leaf 210 approx printed p. 396 - 397
```


## [2026-09-06T21:17:40.787Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SOD xrwm\"; grep -n \"xrwm\\|xrʼwm\\|xrwm(\" SOD.txt | head -20\necho \"### SOD around 432\"; grep -n \"^432\\|\\b432\\b\" SOD_pages.txt | head -5\necho \"### SOD grep zamin/earth soil\"; grep -n \"earth,  *soil\\|earth, soil\" SOD.txt | head -20",
 "description": "Grep Sogdian dictionary"
}
```


### [2026-09-06T21:17:40.856Z] TOOL RESULT

```
### SOD xrwm
37004:xurum   ^xrwm,  Ywrm(h) 
80026:10633  xrwm   M  S\^i^j>j 
80034:10634  xrwmzt*  **  xwrmztyc 
80832:xurm  ^xrwm,  ywrm(h),  ywrwm 
80868:xurmazdic   (xrwmztO 
### SOD around 432
16058:4320 YwVnt B, S                         <c~/j c~-o)o-.lj            Yw*wy , VJ 1093, 1242; 3sg. pres. Yw*t
16066:4321 YwVy B                     (•j>o^'^)«J''j>-
16073:4322 ywVyst => xw'r1, Yw>rn
16075:4323 Yw'rh B, S                                      ^^           GMS 228, 542; VJ 61, 1341; TSP 19.10, 16; inf.
16082:4324 Yw'rnt =* Yw)r'nt                                             gauba =^Ywbc
### SOD grep zamin/earth soil
80029:earth,  soil
```


## [2026-09-06T21:17:42.263Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### MON kolux\"; grep -n \"کلوخ\" MON_part1.txt MON_part2.txt | head -20\necho \"### ARY kolux\"; grep -n \"کلوخ\" incoming/ARY/ARY_pages.txt | head -20",
 "description": "Grep Mo'in and Aryanpur for kolux"
}
```


### [2026-09-06T21:17:42.330Z] TOOL RESULT

```
### MON kolux
MON_part1.txt:12523:است و سنگ و کلوخ بدانجا مالیدن. سنگی 
MON_part1.txt:22123:نتواند شد مانند سنک و کلوخء جماد؛ مة 
MON_part1.txt:22494:به سبب نزدیکك شدن ماه رمضان؛ کلوخ 
MON_part1.txt:24937:سک و کلوخ در آن اندازند. 
MON_part1.txt:35845:پیو: 95 (.) ارة گل خشکث شده, کلوخ. 
MON_part1.txt:39195:که با آن کلوخ يا چیز دیگر کوبند. ساختن؛ ج. تخمیسات. 
MON_part1.txt:46782:سنگک و کلوخ؛ ج. جوامد. ادوية جامد: 
MON_part2.txt:15053:مکعب ستطیل یا کلوخه‌ای که از شکررهای 
MON_part2.txt:15138:کلوخه‌های قند را به اجزاء تقسیم کنند. 
MON_part2.txt:19687:تصفیه شوند؛ کلوخه» سنگ معدنی. کانی‌ها: 
MON_part2.txt:25494:کلوخ: (قد. 15۷ ۷۰ () گل خشک 
MON_part2.txt:25505:بی‌همت. کلوخ راه: کلوخی که در راه مردم 
MON_part2.txt:25506:افتاده باشد. مأنع» حایل. کلوخ بر لب زدن 
MON_part2.txt:25508:داشتن مسطلبی را. کلوخ در آب انکندن: 
MON_part2.txt:25510:کلوخ خاندار: ۲-۸۵52 [ 7 
MON_part2.txt:25511:ی آنکه کلوخ به جانب دیگران پر تاب 
MON_part2.txt:25512:کند. آلتی که کلوخ و مانند آن پرتاب کند؛ 
MON_part2.txt:25518:اواخر ماه شعبان؛ کلوخ‌اندازان. پسر بسر 
MON_part2.txt:25522:و هیثت کلوخباشد. 
MON_part2.txt:42370:زمین شیار کرده بکشند تا کلوخ‌های آن 
### ARY kolux
```


## [2026-09-06T21:17:52.077Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SOD context 10633\"; sed -n '80020,80040p' SOD.txt\necho \"### leaf of that line\"; python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [80026,37004]:\n    off=sum(len(l)+1 for l in lines[:target-1])\n    leaf=t.count('\\f',0,off)\n    print(target,'leaf',leaf,'printed p ~',leaf-66)\nEOF\necho \"### SOD_pages leaf 498\"; grep -n \"pdf page 49[0-9]\" SOD_pages.txt | head",
 "description": "SOD xrwm context"
}
```


## [2026-09-06T21:17:53.312Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### MON kolux context\"; sed -n '25488,25525p' MON_part2.txt\necho \"### qafqaz\"; grep -n \"قفقاز\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Mo'in kolux context"
}
```


### [2026-09-06T21:17:53.867Z] TOOL RESULT

```
### SOD context 10633

GMS  961;  Hen.  JRAS  1945,  153.4,  8;  C2,  60R27; 
CII  1990  F5,  16 

10632  xrtyy  =*  xrtyh 

10633  xrwm   M  S\^i^j>j 
xrum   ©Av.  xruma   ^xwrm,  ywrwm 

earth,  soil 

GMS  415,  482;  Gersh.  JRAS  1942,  101;  AHM 
189 

10634  xrwmzt*  **  xwrmztyc 

10635  xrwnh  S  j^L 
xurwan 

Hulwan(p/ace  name) 
KG  398 
### leaf of that line
80026 leaf 0 printed p ~ -66
37004 leaf 0 printed p ~ -66
### SOD_pages leaf 498
```


### [2026-09-06T21:17:53.931Z] TOOL RESULT

```
### MON kolux context
هم ی ی ی آب 
در آن ریزند و بهم زده مشت مشت و مال دهند تا 
خوب خمیر بعمل آید. سپس آن را در 
ظرفی نهند و دو ساعت به حال خود گذارند 
تا ورآید. 

کلوخ: (قد. 15۷ ۷۰ () گل خشک 


شده. لخت‌های دیوار افتاده و خاک بر هم 


۱۳۸۹ فرهنگ فارسی معیر کلو خ‌انداز 


چسییدة سخت شده. خشت پاره (خام و 
پخته). (کد.) شخص خشک طبیعت و 
بی‌همت. کلوخ راه: کلوخی که در راه مردم 
افتاده باشد. مأنع» حایل. کلوخ بر لب زدن 
(مالیدن): (کد.) مخفی داشتن امری» بنهان 
داشتن مسطلبی را. کلوخ در آب انکندن: 
(کد.) خواهان فتنه و جنگ و آشوب شدن. 
کلوخ خاندار: ۲-۸۵52 [ 7 
ی آنکه کلوخ به جانب دیگران پر تاب 
کند. آلتی که کلوخ و مانند آن پرتاب کند؛ 
فلاخن. سوراخ‌هایی که در زیر کنگره‌های 
دیوار قلعه سازند تا چون دشمن نزدیک 
دیوار قلعه آید» از آن سوراخ‌ها سنگ و 
آتش و خساکستر بسر سسرش ریزند) 
سنکك‌انداز. عیش و عشرت و باده نوشی در 
اواخر ماه شعبان؛ کلوخ‌اندازان. پسر بسر 
فر زند با دختر دختر فرزند» نمبره. 

کلو خه: (۵-)۲۵۱0۵ (۰) هر چیز که به شکل 
و هیثت کلوخباشد. 

کلوز: ۲۵۱02 [- کلوزه] (.) غوزة پنبه که 
شکفته شده و پنبه‌ها از آن بر آمده باشد؛ 
### qafqaz
MON_part2.txt:113:منشاً آن را نواحی غربی آسیا (قفقازیه و 
MON_part2.txt:15779:قفقاز و حتی مسکو به خدمت گرفته 
MON_part2.txt:93297:ایران و قفقاز و چین می‌روید و الب بنام 
MON_part1.txt:10438:آمریکای شمالی و قفقاز و هندوستان فروان
```


## [2026-09-06T21:18:10.395Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SOD_pages xrwm\"; grep -n \"xrwm\" SOD_pages.txt | head; echo \"---\"; grep -n \"10633\" SOD_pages.txt | head\necho \"### IEC leaf 296 (p.562)\"; awk 'BEGIN{RS=\"\\f\"} NR==296' IEC.txt | head -60",
 "description": "SOD page tag and Mann p.562"
}
```


### [2026-09-06T21:18:12.588Z] TOOL RESULT

```
### SOD_pages xrwm
16399:     xurum ^xrwm, Ywrm(h)                                              GMS 817; W-Li 95; Hen. JRAS 1944, 143.20;
34521:10633 xrwm M                               S\^i^j>j
34528:10634 xrwmzt* ** xwrmztyc                                            contentment, satisfaction
34849:       pride, arrogance                                               xurmazdic (xrwmztO
34880:      xurm ^xrwm, ywrm(h), ywrwm                                     STii 6.9; BSTi 318; GMS 893
---
34521:10633 xrwm M                               S\^i^j>j
38102:divinity   2604                       Go)drive on    1461                       10633, 10751, 11217, 11221,
39470:    soil 4438, 10633, 10751                   so unhappy     9790                      0<?)split     4627, 4698, 7922, 8078
### IEC leaf 296 (p.562)
alvor, calvi ‘quibble’; OCS klüno, infl. kleti ‘curse’; R cf. kol-dün ‘sorcerer’; koldovàt, inf. “practise sorcery'
kld- “timber, cut wood’. WP I, 438. Cf. kold- Gk. kládos ‘branch’; MHG holz ‘wood: forest and timber’; OE holt, id. (O-gde in OCS klada “log, beam, stump’: Pol. Kioda Cz. klá- da, R kolóda, id. and Ir. coill, f. ‘wood, copse’. For ON, Norw. holt ‘stony ridge’ etc. see Supt. kld-)
(klà- (1) ‘slip’; (2) ‘clasp, collar”, see Supt. K)
(klk- (1) “bend, knee, hock’, etc. see kələk- (1)
klk- (2) “lump” Cf. klk, id.; Latv. cf. kilkens ‘dumpling’
kluis, à (?) “stick, club’ Skt. cf. krvih (queried: *weaver's sley’); Lat. cf. clava “stick, club?
kluos, à “bald, close-shaven; pate'. WP I, 447. Cf. kaluos. Latin ambig.
klüd- — knabho, io
20
25
30
35
40
516
Lat. calva ‘skull’; calvus ‘shorn, bald’; Skt. cf. áti-külvah, -kürvah beside kulvah, id.; Av. (queried) kaurvo, kaourvo Chald of horse); Per. kal ‘bald’; Fris. holle “head?
km- an adverbial extn. and expletive. Cf. kmt-, Kmt-, kmst- Gk. cf. autí-ka, hení-ka, tení-ka; Dor. ho-ka, állo-ka; Olr. -co, -chon; Go. ni hvas-hun *no- body’, etc. (Lat. -cum is ambig. cf. kom)
kmkKtos, kmstos (?) ‘compact, together, total". Evidence ambig. For *kmkKtos cf. Lat. cunctus, OLat. conctos Call" Speculations in EM/ WH); OCS éestü ‘compact’; Cz. častý 'fre- quent’, and com. Sl.; Li. kimstas ‘compact; Latv. kimsts, id. For *kmst- cf. Gk. hé-kastos each". if for *sem-kmstos 'one-and-all'. Cf. also (?) W cannu, v. 'contain'. Cf. kmt-
kmt- (kmtm, kmto, kmti-) “together, com- bined, total’. Cf. Kmt-, kmKtos Gk. katá “along, from, to’; káto ‘below’; cf. kásis, gs -eos, mf. ‘sibling’; kás-sa ‘concubine’; kas-süo ‘sew together; andrakás ‘man by man’; kas-apai ‘also’ beside Cyp. Arc. ka ‘and’; Lat. cum, -cum (ambig. cf. kom-); Gaul. canta-; Olr. cét, MIr. céite ‘assembly’; MW can, (mutated) gan, cj. "since": W (mutated) gan, prep. ‘by’; Br. gant, gand (“mutated: “by, with"); Cor. gans, id.; OE hyóe, adj. “suitable”; hyðð, -o, f. 'advantage'; ON hund-, px. “very”. (Gk. kai and may represent a form *km + *i, see ei, A Isophones include W caint (2) ‘conflict’, cf. Go. hunps ‘seizure’; MHG hunde ‘booty’; OE hob, f. id. (but cf. Kmt-). E-gde in kem- ‘gather’; o-gde in kom ‘with’, q.v. WP I, 459
(kmt- (2) “conflict, battle’, see kmt- above. Br. kann, pl. u, id.; W caint, pl. ceintiau, id. and cf. Go. hunps 'seizure")
knabo, ið ‘tap, knock, snatch’ Ir. cnabaim (2) ‘beat’; OE hnæppan, id.; LG neppen ‘cheat; ON hneppa (1) ‘dock’; Sw. nappa ‘seize’; cf. näpsa ‘reprimand’
knabhó, ið ‘pick, peck, snip, lop’. WP I, 393. See next Gk. knápto ‘têar’; Ir. cnabaim (1) ‘tug, tousle’; ON hnafa ‘cut off, snap’; Li. knabù, éti ‘peel potatoes? beside knabóti ‘poke out": Latv. cf. (-a-) knābēju ‘peck’ beside knābju, knābt, id.
517
knabhos, à, is “peck, pick, hook, beak, card- ing-comb'. Cf. knabho. WP I, 393 Gk. knáphos “teasel, carding-comb'; Myc. cf. knapeu- ‘fuller’; Alb. krrabé “hook, claw, staff";
Gaul. Cnab- (in a name); OHG Hnabi, OE :
Hnaf (names) W cnaif 'sheep-shearing; fleece; Sw. nåv “long beak’; Li. knabis, m. ‘dibble’ beside knablys ‘beak’; Latv. cf. (-à-) knābis, id.
knàbh- “bite, sting, prick’. (Variant of knabh-, q. v.) Gk. knéphe ‘nettle; itch’; Sw. cf. näv “long beak’; Latv. knābis, s. ‘beak’; cf. knabju, knabt ‘peck’; Li. knóbiu, ti, id.
knad- Gk. cf. knadálló ‘scratch, tickle’; Ir. cf. cnadán, cradán ‘burr’
knadh- ‘scratch, itch, claw". WP I, 392 Gk. knétho, id.; Alb. (ambig.) krodhé (1) scab, eczema’; OCS (and com. Sl.) krado, krasti ‘steal’ (?)
kna
```


## [2026-09-06T21:18:20.097Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC leaf 319 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==319' IEC.txt | head -70",
 "description": "Mann p.562"
}
```


### [2026-09-06T21:18:21.584Z] TOOL RESULT

```
=== IEC leaf 319 ===
uel. Lat. ambig.)
kroupið (kroupeið) ‘rouse, excite, incite’ ON hreyfa, tr. ‘stir, move’; Pol. krupić sig ‘bicker’; Li. kraupiù, kraüpti ‘scare; abuse’. See next
kroupos (kreup-) ‘rough, gritty; roughness; grit, scab’. WP I, 481. See kreup-, krüp- OHG cf. hriuva (for *hriuba ‘scab’ or «leprosy?) (e-gde as also) OE hrēof “rough, scabby’; ON hrjüfr, id.; Latv. kraupis, kraupa ‘scab, mange’; (o-gde in) OCS krupa ('groat, crumb’, and com. Sl.); OCZ. krupy ‘coarse’; cf. Blg. krupen, adj. id.; Li. kraupüs “rough, rugged”; Latv. kraupis & kraupa (beside kr-) ‘scab, mange’; kraupis (2) *toad'; kraupes, pl. ‘wrinkles’
krous- (1) *dash, strike, beat'. Cf. krus- and next. WP I, 479 Gk. kroüo ‘strike, beat’; Umb. cf. krustatar (let him be punched'. WH and E. Vetter otherwise); OE hrieran (‘destroy’. O-gde fac- titive to hréosan 'attack; rush; collapse"); R krusü, krusit' “dash, crash, wreck’; Cz. krusit,
 
339
inf. “crush, crumble’; — se ‘fret’: cf. kruchy ‘crusty, brittle, harg’
krous- (2) ‘collapse, fall, crumble’. (Prob. same root as krous- (1)) ON hreysar, fpl. ‘heap of stones’; hreysi, n. “cairn, cave’; (mod. “hovel'); Sw. rósa, v. ‘pile up’; OCS kruxü ‘crumb’; OCz. kruch “frag- ment’; Blg. krux ‘grain of salt’; Ukr. kruxyj, Cz. kruchý ‘brittle, crumbly’; Pol. kruchy, id.; cf. kruszec, m. ‘ore’. E-gde in OE hrēosan (2) “collapse, sink, fal’; Li. kriauSius (e- or o-gde: “steep bank"). Isophonic: ON hrjósa, sv. 2. (e-gde: “horrify*); see krous- (1). Z-gde in Gk. krüos, n. ‘ice’. See krus-. Extn. in ON hraustr “brave, strong"; hreysti, f. ‘valour’
krout-, see kreut- (1) & (2) R cf. krutój “steep; smart, sudden, severe’; Cz. krutý «cruel; Latv. krauta ‘shore’
krouu-, Gmc. only, in OHG hrao, gs hrawer; OS hrào; OE hréaw; Du. rauw, ON hrár, adj. ‘raw’. Cf. kruu- (2) and kreuos. Isophonic: Latv Kraus, adj. (steep'. Here?)
krüdos “hard, harsh, raw?. Cf. kreud-, krusd-. WP I, 479 I «+, fambig.) crüdus ‘raw; queasy; cruel’; Br. tı z, id.; OE hrüt (queried: ‘dark, livid’), ON cf. hrút-mánaðr (“the dark month’: Dec.-Jan.). E-gde in MIr. crúaid, Ir. cruaidh, as Lat.
krügos, å “crust O: hrúkr, m. ‘scab, crust’; Ukr. kryha “ice- fake, ice-sheet
kruĝ-? ‘cross, thwart; small of back’
^n cf. korcan, adv. ‘backwards’; korcanem, v. ‘overthrow’; OHG hrukki, OE hrycg ‘back, ridge’; cf. OHG hrucki-lingun ‘backwards’;
krükilis (krüklis), ios ‘throat, gorge’ W crigell, m. ‘ravine’; Latv. krūklis ‘larynx’; Li. cf. krūkiu, ti, v. beside kriūkiu, ti ‘grunt’
krukis, ios, iom ‘stick, hook, crook, cross- piece”. WP II, 573 Skt. cf. kruktáh ‘crooked, curved’; Lat. crux, f. ‘gallows, pole, spit, rack’; Gaul. cf. penno- crucium; MIr. Ir. croch, f. ‘cross, gallows, hook’; Br. kruk, krug ‘gallows’; W crwg, pl. crygau, m. “hook, crook’; OCz. kré, Slovak krč ‘log’ (ambig. as also Alb. kércé ‘stump’); cf. OCS krüco, iti ‘twist’; Cz. krčit 'squat'; Ukr. korčyty ‘crook, bend? beside korč
krous- — krunk-
5
20
23
30
40
45
560
‘cramp’; R korta, id.; Li. kriuke ‘snout’. E-gde in R krjuk, m. “hook, crook, hinge’
kruksos, à (kruKs-) ‘crushed grains, powder, granules’. (Sl. evidence ambig. Cf. krüsos). Cf. WP I, 479 *LLat. in It. crusca ‘bran, refuse, dregs’; OCS krüxa “fragment? beside krüso, iti ‘shatter’; R kroxà ‘crumb, grain’; Li. krušà ‘hail’ beside krušùs ‘friable’; kruns$u & krüstu, inf. krusti “crush, pound’; Latv. krusa ‘hail’
krüK- ‘wane; lose; destroy” Arm. korusanem “lose; ruin, destroy’; cf. korust “loss, waste, damage’; Li. krüStu, krüsti & kriüstu, -ti ‘wane, waste away”
krumbilos, à ‘bend, crease, fold, curve, crook’. See next, and cf. krb- & krump- Br. krummel, pl. -u, f. *pot-handle'; OE hrym- pel ‘wrinkle’ beside mod. E rumple, v. (EME also s. *crease"); G cf. (radical form) rümpfen, v. ‘rumple, crease’, and Du. (e-gde) rimpel, m. id. (fr. *krembol-
```


## [2026-09-06T21:18:27.532Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==320' IEC.txt | head -80\necho \"=== grep kolux in IEC ===\"; grep -n -i \"kulúx\\|kulux\\|kolux\\|kulüx\\|kulukh\" IEC.txt | head",
 "description": "Mann p.561-562"
}
```


### [2026-09-06T21:18:29.091Z] TOOL RESULT

```
). Isophone in Du. over- rompelen (‘take by surprise. No certain etym.)
krumbos “bent, crooked; bend, crutch, haunch, joint’. Cf. krmb- Olr. crumb, MIr. cromm, Ir. crom ‘bent, curv- ed, crooked’; Br. krumm; Cor. crom; W crwm, f: crom, adj. id.; MHG rumph, MLG rump, adj. id., cf. MHG rümphen, tr. & intr. erum- ple’; G rümpfen ‘pleat, tuck, crease’; OE cf. hrumpen, pp. oi hrimpan ‘twist, coil (fr. *krmb-). Extns. in Ir. cromán *hipbone; hook; gaff; Cor. cromman ‘sickle’. Cf. Ir. cromtha “bent, crooked'; OCS krotü, id., Pol. krety, id. (*krumbto-: *krmbto-)
krumos ‘bent, lame’. Cf. krumb-, krmb-. WP L 411 & 480 ON hrumr ‘decrepit’; Blg. cf. krámki ‘curls, locks'
krump-, a possible variant of krumb-, q. v. Celtic forms ambig. Explicit are OCS kropü ‘short’; Li. krumplys, m. “joint, knuckle’. Iso- phonic (?) in (ambig.) Latv. krope “dale, swal- let
krunk- (1) ‘croak, caw, rumble, growl'. Cf. krank- Skt. kruñčah (‘curlew’ or sim.); Li. krunkas ‘raven’; Latv. kroka, f. (tea. Ambig. vowel);
crook,
561
OCS cf. krọčina (‘cholera’. Strictly ‘rumbling in the bowels’ and of ambig. vocalism as CZ. krucet, v. See krank-, kronk-, krauk-, the last form being that of Pol. kruczec, as Cz.); Li. krunkiü, ti (caw, crow’, a parallel form of krankiu, id.). (Isophonic are Latvian kroka (2) and krunka fr. Li. «cease, pleat, fold’. See next)
krunk- (2) “bend, fold” Skt. krüficami Chend Pp: kruktáh “bent, crooked'; Go. hrugga ‘stick’; OE hrung ‘crossbar, pole, rung; MHG runge “staff, shaft; G Runge ('side-stay of cart’. LW in Li. rungas ‘side-stay, rib, rung’ and in Latv. runga, f. ‘stick, cudgel’). (LW fr. Eng. in Ir. ronga ‘rung, spar); Latv. kroka (2) and krunka (fr. Li.) ‘crease, pleat, wrinkle’
krüp- (1) “rough”, hard, crusty; roughness, hardness, scab’. Cf. kreup- Alb. kripë ‘salt’; krip, kryp, v. id.; OHG brut, MHG ruf, rufe, s. wf. ‘scurf; leprosy’; G Rufe ‘roughness, scab, crust’; ON hrufa, f. “rough surface’; cf. G rüften ‘get scabby’; (long-gde in) OE hrýfing ‘scabbiness’; Li. (Žemaitē) krüpis, krüpe ‘toad’; Latv. krupis, id.; Li. cf. krumpü, krüpti ‘get scabby’; ON hrufla, v. ‘scratch’; EMDou. rove, f. ‘scab’
krup- (2) *revulsion'. (Same as (1) ?) Alb. krupé, f. ‘loathing’; n. ‘whiff; OCz. krpiti ‘mar, destroy”; Latv. krupis (2) ‘dwarf
krusd- ‘harden, stiffen, encase’. Cf. krusos, krusio, krust-, krüt- Skt. krüdayami, tr. ‘thicken, harden’; Av. xruZda, v. 1sg. ‘grow hard’; Tokh. kro$ce, adj. ‘cold’; Alb. cf. n-grij ('freeze', fr. *en-^) beside sh-krij ((thaw', fr. *eKs-^?); Lat. (ambig.) cf. crüdésco, Gre (‘get raw, become cruel". Phon. as for nidus?). See next
kruselos, kruslos, kruseros “hard, stiff Skt. (ambig.) krüráh “rough, sore’; Gk. kruerós ‘icy’; Icel. hrollur ‘the shudders, the creeps’; hrylla ‘horrify’. See next
krüsió ‘harden, stiffen’. Cf. krusd-, krusos, krust- Alb. gem ‘freeze’; sh-krij ‘thaw’ (fr. *en-, *eKs-krüsio); Li. cf. krüsnis, ies, f. “pile of stones'
krusn-, krusnt-, cf. krous- (2) “fall”, (kreus-). (Variant krüKs-)
krunk- — kruunt-
20
25
30
35
40
45.
562
Arm. cf. korncim ‘perish’; Alb. cf. krunde, f. *coarse bran'; OE cf. hroren-es, f. *downfall, ruin’; hroren-lic ‘perishable’; Ir. cruinne, f. ‘dew’. Radical long-gde in Li. kriustu, kriüsti *wither, fade, pine'
krüsos, à “hard, solid, frozen; frost, ice". WP I, 479. Cf. kruselos, krusio Av. xrüs ‘terrible’; Per. kulüx ‘clod, sod"; Tokh. A kross, Krauss, B krosce, s. ‘cold, chill; Arm. kur (firm, solid, hard’, if same phono- logy as lur: *Klusos); Gk. krüos, n. “chill, frost, ice’; krus-taino, v. tr. ‘freeze’; Olr. (ambig.) crú ‘aw’; W (ambig.) cri ‘hard’; Br. (dial) kri "raw: OHG hrosa, f. ‘frost; OCS krüxükü ‘brittle’. Vari
=== grep kolux in IEC ===
8056:krüsos, à “hard, solid, frozen; frost, ice". WP I, 479. Cf. kruselos, krusio Av. xrüs ‘terrible’; Per. kulüx ‘clod, sod"; Tokh. A kross, Krauss, B krosce, s. ‘cold, chill; Arm. kur (firm, solid, hard’, if same phono- logy as lur: *Klusos); Gk. krüos, n. “chill, frost, ice’; krus-taino, v. tr. ‘freeze’; Olr. (ambig.) crú ‘aw’; W (ambig.) cri ‘hard’; Br. (dial) kri "raw: OHG hrosa, f. ‘frost; OCS krüxükü ‘brittle’. Variant in Li. kriusà "bal": Latv. kru- sa, id. Long-gde in OE hrüse, f. “earth, ground”; short-grade in OE hryre (‘fall, decay’, if here)
```


## [2026-09-06T21:18:38.735Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### BRT xrū\"; grep -n \"xrūra\\|xrura\\|xrūžd\\|xruzd\\|xrūma\\|xruma\\|xrūta\\|xruta\" BRT.txt | head -30\necho \"### HRN kolux\"; grep -n -i \"kul[uūûŭ]x\\|kolux\\|kulukh\" HRN.txt HUB.txt | head -20",
 "description": "Bartholomae Avestan and Horn"
}
```


### [2026-09-06T21:18:38.804Z] TOOL RESULT

```
### BRT xrū
5735:•  j.  a-sarsta'  Adj.  'nicht  gebrochen'  sva. "nicht  gebeugt,  nicht  mutlos  gemacht': taräiuitrlf  'tS  aka  mananha  xruzdya tbaisi.parsiannm  (sd.)  W.ig.\.
10669:•  j.  *xruzdi.vaßah- '*   Adj.  'mit  derber,
10675:•  j.  xruzdra-  Adj.  'hart'  (vom  Holz): 'äidranain  msmanam  ä^re  frabarüts  \ . lg.  24.  a)  sva.  'schwierig'  (zu  beant- worten) :  'uidranam  (näml.  framanam) Yt.5.82  0.
14449:•  ].  ÖTvya^stama-  Adj.  'der  schrecklichste, furchtbarste':  yat^a  anhat  Hgmaihi  ata- tfham  yatca  afihat  banhui^  faiti  gairi- nam  yat^a  Jqfnusva  raonam  paxrumalfu (sd.)  nmanaiiu  "was  an  den  furchtbarsten (der)   Stätten»  ist,    und  was  .  ."  V.2.23.
14845:.  i.  paxruma-  Adj.  fest':   ^m<7/Ä»  (sd.)   ^bl.:    /  mariiya>-         Aauv    *äuviny/ma-
28433:xruma  i'aitayj'''  fraxinte  (Sp.  1700  o.)  Yt.
### HRN kolux
```


## [2026-09-06T21:18:44.824Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '10660,10690p' BRT.txt\necho \"=== search xru- headwords ===\"\ngrep -n \"xru-\\|xrü\\|xrv\\|xrūm\\|'blutig'\\|blutig\" BRT.txt | sed -n '1,40p'",
 "description": "Bartholomae xruzdra context"
}
```


### [2026-09-06T21:18:44.897Z] TOOL RESULT

```
Vgi.  .r^,;»Hm  un<!  xrüra..
•  j.  xrümini  Adv.  'in  grausamer  Weise' xf  gaus  .  .  varai>Tm  (sd.)  fanlam  azaite Ytio.38.
Vgl.  xriima-,  —  Gebildet  wie  ai.  tiipilm.
•  j.,  g.  xrüra-  Adj.  i)  'blutig,  grausig':  'r>m draß^rn  (sd.)  Y.57.  a  5,  Yt.  j.  11 .  2)  'blut- dürstig, grausam':  köi  *dngi'S.dibis  'rät's rämam  (sd.)  dant!  Y.  48. 1 1.
Ko'ropE.  —  ai.  tiäni-  Adj.  —  VrI.  xrü:  — Pü.  {lu  Y.  4X):  ö  d,-.:i,uUn  xiüii/i,  erl.:  rlS; [laYx.  t):  fa  TLxrümb'^,  erl.:/,!  r,-i  koihm  ,
•  j.  xrGzdä-  f  '(Härte  sva.)  Schwierig- keit (zu  beantworten)':  zara>ustrJ  .  . asaril3  aka  maiiai^ha  'dya  (IS.)  IbalsS.- parstanam  (sd.)  V.  iq.  4.
VgL  xnddra:  —  I'ü:.  .xrn-J  ( riansskr.).
j.  xrüid'r  Adj,,  nur  KompA.  1)  'harf. -    2)  'derb   sva.  laut',   von  der  Stimme.
Sva.   xrüidra-;  s.  unter  l/>r>a'.
•  j.  *xruzdi.vaßah- '*   Adj.  'mit  derber,
lauter  Stimme  sprechend':   'iä  (NSm.)  F.
'üzd  (Transskr.)  ffdtvihiihä.   —   D  Hds. 'd.V'.  —  '1  Vgl.  lu  xraoidyah:
•  j.  xrüzdisma-  n.  r)  'harter  Erdboden'; nahyiSi  paitistune  (sd.)  'me  nialy/öi  iiars ■arfdusiiie  V.  A".  8;    —   mayim  ava.kanOis
distitn  'me  vitaslim  rar»dusiiie(&d.)  V.  77, 5.  2)  'Stück  harter  Erde':  saßin  (sd.) vil  .  .  kamcit  vä  "manam  \.g.ii.
Ableit. 'aus  "xriiidi-iam-' Ad'i.  'was  aus  harter Erde  besteht'.  —  Pü. :  saxl  aamJi;  «u  V.  p tu.:  tafii.akij)  I  u  Hl  i.
•  j.  xruzdra-  Adj.  'hart'  (vom  Holz): 'äidranain  msmanam  ä^re  frabarüts  \ . lg.  24.  a)  sva.  'schwierig'  (zu  beant- worten) :  'uidranam  (näml.  framanam) Yt.5.82  0.
Vjjl.  xrao'.diia;  xrfddi',  xrüäij-i  xronSdis/a-, xiairldyah:  —  Pü.:  saxt.  —  »  S.  iSt  V.  /p.4.
•  j.  xrvant-  Adj.  'grauenhaft,  grausig*: 'vantim  äiktvaiibm  urviHnm  pantam  H, 2.17;  —  vairim  . .  yim  'vaiit^m  äi^iva/i- t>m  fi.og.28.
Statt  *xrü'Tiaitl-  geschr. —  Pü.:  vixrün;    s.  tu
■  j.  xrvi-°,  nur  KompA.:  sva.  xrüra-.
D.  i.  xrut'i'.  —  Vgl.  unter  birizf.
•  j.  xrvijTii-  f.  Name  einer  DaSvX:  psniie "/ni  (statt  Akk.)  V.  //.  9.
Fem.  zu  'xni-ffan.  Adj.  "blutig,  grausam  schla- gend, lötend'.  —  Pü.:  fehlt.
•  j.  xrvi-drav-,  xrvi-drav-"  Adj.  'der eine  blutige,  grausige  Holzwaffe  (Keule?) führt',  von  Assma:  aismS  *'vidrus'^  Yt. '!>•  95.;  —  azhmtmca  'vi.dräm  YL  ig. 46;  18.2,  *V.  JO.  13,  ig.AV,  —  aismahe 'vLdrao^  Y.sy.i,  Yt.  Ji.  15,  y.  138,  V. lo.id;  —  aisina  ..  'vI.drvJ''  Y.io.S; —  asima  ..  'vidrvö^''  \t.i-j.$.
Pü. :  xiiidms,  Transskr. ;  Sü. :  Ainii iini/ra i .  — 1)  NA.  hat  auch  x/f7m.dr';  s.  dagegen  Clii. KZ.  jr.  266,  Richter  IF.  5.205.  —  •)  Hds. ,/, vrj-i.  —  3)  LS.  statt  IS.  i  S  -/qT-
•  j.  xrvisyant-  '>  Adj.  (fem.  'yantT-,  'yäli- '') i)  'grausig,  Grauen  erregend':  frai'asay» ,  .  y1    irrpzayeintls    *yanlis  (APf.)   Yt.  IJ.
|33.  2)  'blutdürstig,    grausam':  gaiiahe
\vlvar?zdavatB  yalä  Y.p.30;    —    spaoaA^
dby  Google
54»  xsa-   -
'yantake  Yt  10.  36;  —  i7fi  haSnayä  °ytitis (AP£)  Yt/o.S;  15.49 ■',  /')-54  (wo  "''-O- PPA.,  ans  *xn-is'ya;  den.  Praes.  31.  —  Vgl. ai.  krafi;.  n.  'Aas',  ksl.  Wfol  •Blut'.  —  Vgl. xrii:  —  Pü.  (nach  Dst.):  ifarak  x^äk,  erl.: T/i  iuiiil],);  Sü.!  /liifayili.  ~  ')  Mit  (  Yl.  /J. 33,  /o.  8j  /f,  45  sieht  xriiisy',  %  268.  iz  c —  »)  Gegen  S  /'iJ''  d  «-  —  3)  S.  in  xrüta-. j.  j«cö  F.  zj  b;  lies  xtaosyd.
=== search xru- headwords ===
4403:•  j.  an-äxrviäa.dÖiSxa-"'  Adj.  'des  Augen nicht  —  ?  —  sind':  vayul aurvS  .  .  "re ya'ia anyasäi  xsa'irät  xsayamna  .  .  YL  ij.  54.
4790:der  Richtung:  atcit  dim  aiwyäili'^^  ya dahma . .  ofritis  P.J2.  a)  'begehen,  (einen Weg)  gehen':  mä  dim  psrisS ..yim  xrvan- tim..pantqm  aiwitim^*'''  "frag  den  nicht, .  .  der  den  grausigen  .  .  Weg  gegangen ist"  H.2.17.        S.  noch  No.  26.
5211:—  Hat    ^wä    .  .   m^rrta  .  .   vibaryn  *°oi iiiata..*°oi*y.io.ii;\ti0.iz6{'7'i); — «J tat  3p»n  iincaiti  H'i  yavS/ariltamV.$.^; 16;  —  Oft  um  spay3jlsd.)  I>m9  äia  va?ls.. vupata  'vi  ti/ra  *iumata(sd.)  ^.^^.35; —   ' cataarB  pirsnä  (sA)  v^ärayBis  'vi  pahqm  ' Yt/^44;    —    nanm    «J  (sd.)  'vi    ava.-  '• ginplsm  V. /Äio;  —  aai  ti  ifps  */rasil- vqyää  . .  'vi  hapid.karsvairTi  (IP.  als  AP.) YLÄ9;  —  mit  Gen.  part  statt  Akk.:  yai  , nsit  sünS  . .  aSanham  astqm  'vi  apqmca  \ urvaranqmca    barmtun  (sd.)  frajasqn  V.   ■ 6.  46.  p)    sonst:    un'ä^qmcit  zbayemi '7-i    imat   vard   Yt/2.3;  3J;  —    ahumat raüttnat  (sd.)  vaÄi/fym  vaoiaia  k>mcit  art- h3ui  .  .  °oi  P.  jj;    —    asmamm  .  .  yS  . rtulakiitö   'oi   *5«Vi'a  (sd.)    Yty.  a;    — ya^numca  'vi  sqm^a  V.2J.4;4.  f)  bei  1 Ellipse  des  Verbums :   cim  'oi  yamd  "an  ; wen    (richtet   sich)    das   Gebet?" 2".         b)  'gegen,  contra',  in  feindlichem Sinn:  daiAhupatayS ..  ai'ajasmts  'oi  Aas- nayS  xrvlfyätl/  Yt  10.8;  8;  —  ya^a  yat  < AaOtam    ava^t  .  .  'vi   vTsö  V.  18.  i nSit  .  .  *tyanJm  (sd.)  . .  xit3  mäidayasnls  ).
5737:•  j.  asah-  n.  'Ort,  Stätte,  Platz,  Raum': y8  anyeAe  *'saAya  (LS.)  bansma  */ra- stff^ie^.ioi; — äaire  "saAi  razaaiam(sd.) V.Ä97;  —  atfffi  daoam  °s/f  rämsMäitTm (sd.)  ndil  kuäalJäiim'V.i.i;  iPUZ.,  Vyt. 2'j(?);  —  xrüma  'sl6rs{3is  Subj.)  frasinia danunam  YL  13.  ^S;  —yatca  aakat  %wyqs- brnalrva  'sauham  V.2.23;  —  yäi^a  °sS mai^animca  atmisilSe  äaiära  (sd.)  Yt.  13. 67.  a)  sonst  neben  sSihra-.  paoirlm •sanham^a  Sstiranamca  vakishm  frii' "iwtnspm  .  .  airyatDtn  vaSjB  "als  die  erst- beste der  Stätten  undWohnplätze.."  V.  I.a; Y.  /.  lÖ;  —  hpnti  atiyäscii  °s3sca  sSi^rSsca irirasla..  V.J.  20;  Y.  3.16,  S.  7.28,  2.28; —  äat . .  vazaite  väiS . .  avi  'sä  avi  /gi'irS ai-i  karh'ä  yäis  hapta  Yt  Ä  3  3 ;  —  para  nU ahntät  h<üa  'sarihal^a  ^t^räatca  axslat .,  iia/a  äzätliscaY.g.^y,  —  Adoa..  aktnai •saaAalia  sUrbraläi  paiti.jasata  iii V.  ß.  5  4 ;  55,  57;  —  tä  yai'.yeinti  p>sanahu kavc  'tahi  säi^rafai  Yt.  IJ.  27.
7096:•  j.  ä'xrüra-  m.  EN.  eines  Gläubigen: "rahe  haosravanhalte  asifOHü  "des  A.,  Nach- kommens des  //.  .  ."  Vt.7y.137".
10451:mit  ui  i)  'hochheben,  erheben':  hakal iiigsr.'ptaiibya  aiigustafibya  uzgpr?piaSi- iya  püsriagiiyn  "mit  gleichzeitig  aufge- stemmten Zehen  und  hochgehobenen i'ersen"  Y.S.'jo;  jj; —  *kainSby5  yä  us xrünm    drafhm  gprswnqn   Y.57, 35;  — |
10605:VgÜ  xrütdra-.  —  w.  vgl.  krüjayali laxl.  —  1)  Word,  r  ".  .  nitf  irgend Baum  der  harten  und  weichen".  Pa.  führt als  Beispiel  an:  van  i  väläm  (np.  iädät 'Mandel'>
10646:539  xru-   -
10649:xr3rphayete  spüoaAe  xrvJsyantoAe  Yt.JO.56.
10651:•  j.  xrü-  f.  'blutiges,  rohes  Fleisch':  musti.- masaah»m  xrüm  "ein  fausigrosses  Stück Fleisch""  Yt.  14.  33.  3)  'Grauen,  Graus' (nur  Ableit.)-  a)  Name  eines  Da^'a: psrme  xrB  (statt  AS.)  V.  /;.  9.
10652:Ableit.  —  Vgl.  ii-äla-,  xriinirä;  xrünya-yxriita-, xn^iyaiit-.—  Pii.(iuV.):  fehlt;  Npü.  (lu  Yl.): däaa.  —   ')  Bd.  /p.  31 1  nlas/  masii-  .;'<'jj'. j.  xrüisyeitii  Yl.  /J.  4.9:  %.   unter  xrvlsy'.
10653:•  j.  xrüta-  Adj.  'grausig,  grausam':  z>md .  .  daivS.dätahe  °tahe  ayavaiff  V.  7.  27.
10655:•  g.  xrünarä-  f.  'blutige  Misshandlung, Blutbad':  Auxsa'i räis  ßiipram  (sd.)  'rqmäl ais  dadäta  ,  ,  trata  r/  ävaßö  (sd.)  Y. 55-8.
10657:•  g.  xrünya-  n.  'Bluttat,  blutige '. lung';  u:iii'iysi  (sd.)  Im  ..  'y.i/  \.4S.$.
10658:Vgl.  xrü:  ~  I'ü.:  fixrinii'),  erl.:  lin-aiidU, Su.:  kadarthaaarvam.  —  i)  S.  lu  jrrnw-.
10660:Vgi.  .r^,;»Hm  un<!  xrüra..
10661:•  j.  xrümini  Adv.  'in  grausamer  Weise' xf  gaus  .  .  varai>Tm  (sd.)  fanlam  azaite Ytio.38.
10663:•  j.,  g.  xrüra-  Adj.  i)  'blutig,  grausig':  'r>m draß^rn  (sd.)  Y.57.  a  5,  Yt.  j.  11 .  2)  'blut- dürstig, grausam':  köi  *dngi'S.dibis  'rät's rämam  (sd.)  dant!  Y.  48. 1 1.
10664:Ko'ropE.  —  ai.  tiäni-  Adj.  —  VrI.  xrü:  — Pü.  {lu  Y.  4X):  ö  d,-.:i,uUn  xiüii/i,  erl.:  rlS; [laYx.  t):  fa  TLxrümb'^,  erl.:/,!  r,-i  koihm  ,
10667:j.  xrüid'r  Adj,,  nur  KompA.  1)  'harf. -    2)  'derb   sva.  laut',   von  der  Stimme.
10668:Sva.   xrüidra-;  s.  unter  l/>r>a'.
10672:•  j.  xrüzdisma-  n.  r)  'harter  Erdboden'; nahyiSi  paitistune  (sd.)  'me  nialy/öi  iiars ■arfdusiiie  V.  A".  8;    —   mayim  ava.kanOis
10676:Vjjl.  xrao'.diia;  xrfddi',  xrüäij-i  xronSdis/a-, xiairldyah:  —  Pü.:  saxt.  —  »  S.  iSt  V.  /p.4.
10677:•  j.  xrvant-  Adj.  'grauenhaft,  grausig*: 'vantim  äiktvaiibm  urviHnm  pantam  H, 2.17;  —  vairim  . .  yim  'vaiit^m  äi^iva/i- t>m  fi.og.28.
10678:Statt  *xrü'Tiaitl-  geschr. —  Pü.:  vixrün;    s.  tu
10679:■  j.  xrvi-°,  nur  KompA.:  sva.  xrüra-.
10681:•  j.  xrvijTii-  f.  Name  einer  DaSvX:  psniie "/ni  (statt  Akk.)  V.  //.  9.
10682:Fem.  zu  'xni-ffan.  Adj.  "blutig,  grausam  schla- gend, lötend'.  —  Pü.:  fehlt.
10683:•  j.  xrvi-drav-,  xrvi-drav-"  Adj.  'der eine  blutige,  grausige  Holzwaffe  (Keule?) führt',  von  Assma:  aismS  *'vidrus'^  Yt. '!>•  95.;  —  azhmtmca  'vi.dräm  YL  ig. 46;  18.2,  *V.  JO.  13,  ig.AV,  —  aismahe 'vLdrao^  Y.sy.i,  Yt.  Ji.  15,  y.  138,  V. lo.id;  —  aisina  ..  'vI.drvJ''  Y.io.S; —  asima  ..  'vidrvö^''  \t.i-j.$.
10685:•  j.  xrvisyant-  '>  Adj.  (fem.  'yantT-,  'yäli- '') i)  'grausig,  Grauen  erregend':  frai'asay» ,  .  y1    irrpzayeintls    *yanlis  (APf.)   Yt.  IJ.
10690:'yantake  Yt  10.  36;  —  i7fi  haSnayä  °ytitis (AP£)  Yt/o.S;  15.49 ■',  /')-54  (wo  "''-O- PPA.,  ans  *xn-is'ya;  den.  Praes.  31.  —  Vgl. ai.  krafi;.  n.  'Aas',  ksl.  Wfol  •Blut'.  —  Vgl. xrii:  —  Pü.  (nach  Dst.):  ifarak  x^äk,  erl.: T/i  iuiiil],);  Sü.!  /liifayili.  ~  ')  Mit  (  Yl.  /J. 33,  /o.  8j  /f,  45  sieht  xriiisy',  %  268.  iz  c —  »)  Gegen  S  /'iJ''  d  «-  —  3)  S.  in  xrüta-. j.  j«cö  F.  zj  b;  lies  xtaosyd.
11023:—  ahmäkSng  .  .  urunS  pasukanqmlä  Y. 3().  I ;  —  alä  vohulä  .  .  manatshä  Y.  44. 9,  45.10;  50.3;  —  rasists  i!  asäl  vahis- timca  ahäm  Y.6S.  i^;  —  maifTm  yqm pouruMsaintim  makraheca  paunatat  m  V. 57-  ao;  —  JSmrqm  xrümrqnun  (beide  als I  .Glied ;  Sp.  564  m.)  rSOT^Wi-'tr ..  (A/</J/Ä  Y  j_j. 8.        a)  in  Verbindung  mit  ä  (s.  Sp.300  m.) :
11366:die  Tatsache,  dass  das  Gesi^e  oder  Vor- ausgesetzte auch  hier  gilt,  soU  als  auffällig hingestellt  werden;  sva,  'sogar,  selbst; sogar  schon,  sogar  noch';  b)  im  Aw.: hazaarS.varaySi^A.)  ba^van.väraii^i'W .  21. 2;  —  alsam  amaahqm  .  .  srävt  yimüs- (sd)i^  V.^2.  8;  —  lüpB  . .  ys  tq%ryaslit\ hala  xsa/nS . .  valnaiti  \t.  16. 10, 14. 31  (vgl, 13);  —  kaAriäsB..yS  naomyä{iä..yit  kala dait^haot  musH.masatihfm  xrüm  aiwi.- vaBiaiti  avavallit  yä^a  säkaya  (sd.)  brä- z^m  avavaliit ..  Yt/^.  33; — ysi  pfs?m<!it sär;rm(sd.)  bunfaifiti  usg^npUmHl  snäium ..a/iaji^anvainti {ad.)  Yt  14.  46 -,1:^.40' ;  — tä  ftS  qnahuiit  hats  %rSyaiU  Yt.  13. 146; — yl  narqm  vJgfr^ptä{^di)iit  -baextärsm daoaiH  Vr.  7. 3;  —  kaAmai  ..  Vftvm  x/a- ^rfm  .  .  paiH.da^3ni  , ,  sä^ras^it  AamS.- xsaSirahe  Yt. /0. 109;  iii;  —  ßislaheiti axsnuäaAeisd.)  .  .  manS  rSmaya/i  Yt. /O. 109;  iii;  —  aftäp?n%a  haia  syao>;na.. a^taiit  aÄbyS  *spänhaiti  ".  .  auch  diese (Sünden)  nimmt  sie  ihnen  weg"  V.  j.  39f.;
12519:•  j.  daevya-  Adj.  'rfoAdsch,  teuflisch': arirSi..vairTm  yim  xrvantim  aiktvanttm yim  °vTm  Aog.  2S.
13633:6,  15,  16,  17; — p'iS'iiJ'  aJam  myalii\am  *  j-  dütay-  t  ein  Längenmass*':  mayjm im.im  'pim  iripiitanaiy  -dranf  befahl  ich.  <niJiJncis*'nm'^^  xrüzäiinu-.ltastint  ran- diese  Inschrift   niederzuschreibeo"  X.T.3;  ''i'""'  *sd.)  V./-  5;  —  '/r  F.l^a. 3;  —  «Ttf*    a^iv-J/J    ■/>><!  ^ergänzt.    ««:    -  *'  '~''<'^''   ">  r.Dgertrri.a   ^,V« yo  ^«,-r../ mptttam  Bh.4.8.  ^.J;j^  .teh<t.d.
14061:•  3.  draföa-  m.  'Fahne,  Banner':  mä  . . ya%a  *gaes°i3'^..*vär^ma*caire(sd.)"..v/ie das  Stierbanner •> .."  Y.fo.  14.  a)  sonst von  den  Feldzeichen  der  Feinde  Irans *AainslyS  ya  us  xrünm  -htn  girminqn  Y. 57.25;  —  haiiiayas^a  .  .  xrQr?m  '/»m iarvntayä  Yt  J.  1 1 ;  —  nsii  ihra  airyi daiAhävö  frqi  (sd.)  hySi  hai»ia  .  .  nsii AasnyS  rdhs  nöit  usgprtptö  "so  Yt.  Ä  56; —  kaca  'sayS  (als  Fem.!)  pin\u.usg>r»p- tayä  Yt.4.3.
14679:•fa  dahakS  Yt  $.  39,  15.  19;  ig.  47,  49; —  alJm  dahäktm  •fantm  ^riiairunh^m xrvalailm  Y.p.S;  —  aie  'ßm  (yS.) doAäka Ytig.so.
14775:•  j.  tbaeäö.par^ta-  Adj.  'aus  Feindschaft, in  feindseliger  Absicht  gefragt':  uia  hl fraiha  (sd.)  paiti.mravSne  navaca  navai- tXmla  xruidranqm  °tanqm  yat  mqtn  p»r>- sai ..  "..  auf  die  99  schwierigen,  in  feind- seliger Absicht  gefragten  (Fragen),  wenn  . ." Ytj.  82'';  —  iard^uströ  asaritS  aka manatgka  xrüzdya  'tanqm  ",  .  durch  die Schwierigkeit  der  in  feindseliger  Absicht gefragten  (Fragen)"  V.  ig.  4.
16794:!)'etwas,  Jemanden (Akk.)  tragen;  etwas an,  bei,  in  sich  tragen,  besitzen,  enthalten, führen,  im  Gebrauch  haben':  tmam  zum ya  nä  baraiti  V.  JÄ.  i,  13.  i;  Yt.  JJ.  9;  — mä  eil  barS  aivd  ya}  iristsm  5al  yesi  se baräi  aevö  "nicht  soll  einer  allein  einen Toten  tragen;  wenn  aber  . ."  V.  _y.  14; —  W^adiaram  dldiy  iyaiy  manä  gä'itum bara'tiy  ".  .  (derer,)  die  meinen  Thron tragen"  D.7.4;  —  kaomun  baire..yaka azfin  vanärti  "einen  /faiimastengel  trag ich  bei  mir  (als  Zauber),  damit  ich  .  ." Yt  r-^.  57;  57^;  —  barat  kariUm  "ein Messer  führt  er"  Yt.  i4-'^T,  —  va^jtm vaijS  (sd.)  ,  .  yim  barat  .  .  %raltaonB.  Yt '9-9^',9ZH — haSnäyaica..xrüi»m  ärafhm *barfntya*'>  Yt  /.  11;  —  /ravalayü  .  , hajctä  an>aaiTi  (sä.)  bar^ntls  Yt  ij. ^$;
19316:—  yavBi  vispäi  drüjS  'nät  astayö  Y. 46.  II.  e)  g.  mit  GS.  aciltahyä  manar)hs dnwD.  (vgl  c):  yH  xia%ra  *grshmB  hisa- sai  (sd.)  acislahyä  'nl  mananhä  Y-32. 13,  n)  von  EehausuDgcn,  Ställen  für Tiere:  ^riiai(sd.)ca  . .  gsus  apa.jasai yalca atthat  %wyqst?mal/u  asatahqm  . .  banmus paiti  gairinqm  .  .jqfnusva  raonqtn  paxru- mag/u  (sd.)  'nax/u  V.  2.  23;  —  °n»m  gäva- yamrn  (sd.)  nava.h^nm  navajtgmat^m  . . cvat  yavat  'nsml . .  dvadasa  vltsra  (sd.)  . . V./rf.i4.'
```


## [2026-09-06T21:18:59.659Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'NR<=34521 && /\\[pdf page/ {p=$0} END{}' SOD_pages.txt >/dev/null\ngrep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<34521' | tail -3\necho \"---\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1>34521' | head -2",
 "description": "Find SOD pdf page for xrwm entry"
}
```


### [2026-09-06T21:19:02.145Z] TOOL RESULT

```
---
```


## [2026-09-06T21:19:06.003Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -3 SOD_pages.txt; echo \"...\"; grep -c $'\\f' SOD_pages.txt; grep -n \"page\" SOD_pages.txt | head -3\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\noff=sum(len(l)+1 for l in lines[:34520])\nprint('formfeeds before:', t.count('\\f',0,off))\nprint('total ff', t.count('\\f'))\nEOF",
 "description": "SOD pages structure"
}
```


### [2026-09-06T21:19:07.792Z] TOOL RESULT

```
 SOGDIAN
DICTIONARY
Sogdian - Persian - English
...
642
1946:grammatical identifiers to help differentiate the forms. Adding the references with page
2086:    The English Meaning comprises the next line of           the page and line or paragraph is added. For certain
2986:defective in showing Sogdian vowels in quality and                       The phonemic charts on the following pages give
formfeeds before: 499
total ff 644
```


## [2026-09-06T21:19:12.294Z] TOOL CALL #29: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T21:19:12.302Z] TOOL RESULT

```


```


## [2026-09-06T21:19:16.522Z] TOOL CALL #30: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krewh%E2%82%82-",
 "prompt": "Give the full reconstruction, gloss, descendants (Greek kreas, Latin cruor/crudus/crusta, Avestan xrū-), and any note about the extension *kreus-. Quote key lines."
}
```


## [2026-09-06T21:19:18.717Z] TOOL CALL #31: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D9%84%D9%88%D8%AE",
 "prompt": "What is the etymology given for Persian کلوخ (kolux)? Quote it, including any Middle Persian form and any cited source (Hasandust, Cheung, etc.)."
}
```


### [2026-09-06T21:19:21.123Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T21:19:23.874Z] TOOL RESULT

```
# Proto-Indo-European Root *krewh₂-

**Full Reconstruction:** *krewh₂-

**Gloss:** "blood outside the body (as of a wound)"; by extension, bloody or raw flesh, raw meat; possibly wound or hardened blood/scab

**Key Descendants:**
- Greek: κρέας (kreas, "meat")
- Latin: cruor ("blood"), crudus ("raw"), crusta ("crust")
- Avestan: xrū-
- Old Norse: hræ ("corpse, carcass")
- Old Irish: crúaid ("hard")

**Note on *kreus- Extension:**

The text suggests *kreus- may represent a separate root. According to the article: "these have been argued as from a separate root *krews- ('to freeze, harden')" when discussing semantically related words like Latin crusta and Latvian kreve (coagulated blood). The distinction appears designed to explain the semantic field of "wounding, death, and possibly drying out/hardening of the body."

**Semantic Distinction:**

PIE distinguished this root (outside blood) from *h₁ésh₂r̥ (inside blood), with *krewh₂- associated with aggression, dying, and wound-related imagery in descendant languages.
```


## [2026-09-06T21:19:29.035Z] TOOL CALL #32: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/crystal",
 "prompt": "Quote the full etymology of crystal, and also anything on the entry page about Greek krystallos, kryos, and the PIE root *kreus-."
}
```


## [2026-09-06T21:19:30.371Z] TOOL CALL #33: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Caucasus",
 "prompt": "Quote the etymology section of Caucasus: Greek Kaukasos, Scythian, Pliny, and the analysis of the elements (kroy-khasis 'ice-shining')."
}
```


### [2026-09-06T21:19:34.746Z] TOOL RESULT

```
# Etymology of Crystal

**Full Etymology:**
"Old English _cristal_ 'clear ice; clear, transparent mineral,' from Old French _cristal_ (12c., Modern French _crystal_), from Latin _crystallus_ 'crystal, ice,' from Greek _krystallos_, from _kryos_ 'frost,' from PIE root *_kreus_- 'to begin to freeze, form a crust.'"

**Greek and PIE Root Details:**

The entry explains that the Greek term _krystallos_ derives from _kryos_, meaning "frost." This connects to the Proto-Indo-European root *_kreus_-, which carries the sense "to begin to freeze, form a crust."

The historical understanding is reflected in a medieval quote noting that the ancients "trowe that it is of snowe or yse made harde in space of many yeres" — they regarded crystal as petrified ice, a belief rooted in the semantic connection between the word's origins and the concept of frozen water.
```


### [2026-09-06T21:19:36.537Z] TOOL RESULT

```
# Caucasus Etymology

Based on the Wiktionary content provided, here's what's documented about Caucasus's origins:

**Etymology stated in the article:**
"Via Latin *Caucasus*, from Ancient Greek *Καύκασος* (Kaúkasos)."

The webpage shows the word traveled from Ancient Greek through Latin into English and numerous other languages. However, **the article does not contain information about Scythian origins, Pliny's references, or etymological elements like "kroy-khasis" or interpretations about "ice-shining."**

Your query references etymology details that are not present in this particular Wiktionary entry. Those details may appear in other sources, but I can only report what this specific page actually states.
```


## [2026-09-06T21:19:41.236Z] TOOL CALL #34: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CE%9A%CE%B1%CF%8D%CE%BA%CE%B1%CF%83%CE%BF%CF%82",
 "prompt": "Quote the etymology section for Ancient Greek Καύκασος — any Scythian origin, Pliny's Croucasim, element analysis."
}
```


## [2026-09-06T21:19:42.174Z] TOOL CALL #35: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/pancreas",
 "prompt": "Quote the etymology of pancreas, including Greek pankreas, pan- and kreas 'flesh', and the PIE root."
}
```


### [2026-09-06T21:19:46.037Z] TOOL RESULT

```
# Etymology of Ancient Greek Καύκασος

Based on the Wiktionary article, the etymology section states:

**"Uncertain; perhaps ultimately from Proto-Indo-European *kewk- ("to elevate; height"), or borrowed from Iranian languages, compare Middle Persian *Kaf kōf ("Mount Qaf, Caucasus mountains")."**

The article does not mention:
- Any Scythian origin
- Pliny's "Croucasim"
- Element analysis

The source only presents two theories: a possible Proto-Indo-European root relating to elevation/height, or an Iranian language borrowing connected to Persian Mount Qaf terminology. Both theories remain uncertain according to the entry.
```


### [2026-09-06T21:19:47.055Z] TOOL RESULT

```
# Etymology of Pancreas

The word "pancreas" comes from a Latinized Greek term. According to the Online Etymology Dictionary:

**Greek origins:** The term derives from Greek *pankreas*, literally meaning "entirely flesh," combining *pan-* ("all") and *kreas* ("flesh").

**PIE root:** The *kreas* component traces back to the Proto-Indo-European root *\*kreue-*, meaning "raw flesh."

The anatomical term emerged in English around the 1570s. The name likely refers to "the homogeneous substance of the organ," as the source notes, reflecting how ancient Greeks perceived the gland's uniform composition.
```


## [2026-09-06T21:20:00.920Z] TOOL CALL #36: WebSearch

```json
{
 "query": "حسن‌دوست ریشه‌شناسی کلوخ فارسی kolux etymology clod Persian"
}
```


## [2026-09-06T21:20:02.441Z] TOOL CALL #37: WebFetch

```json
{
 "url": "https://www.vajehyab.com/moein/%D9%82%D9%81%D9%82%D8%A7%D8%B2",
 "prompt": "What does Mo'in (فرهنگ معین) say about قفقاز? Quote the entry."
}
```


### [2026-09-06T21:20:04.516Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T21:20:08.944Z] TOOL RESULT

```
Web search results for query: "حسن‌دوست ریشه‌شناسی کلوخ فارسی kolux etymology clod Persian"

Links: [{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"کلوخ - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%DA%A9%D9%84%D9%88%D8%AE/"},{"title":"محمد حسن‌دوست - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86%E2%80%8C%D8%AF%D9%88%D8%B3%D8%AA"},{"title":"محمد حسن دوست نویسنده کتاب فرهنگ ریشه شناختی زبان فارسی(5جلدی) | ایران کتاب","url":"https://www.iranketab.ir/profile/23034-mohammad-hasandust"},{"title":"کتاب فرهنگ ریشه‌شناختی زبان فارسی (جلد 5)","url":"https://fanuus.org/library/%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-%D8%AC%D9%84%D8%AF-5/"},{"title":"معنی کلوخ - فرهنگ فارسی عمید","url":"https://lamtakam.com/dictionaries/amid/31779/%DA%A9%D9%84%D9%88%D8%AE"}]

I found relevant search results about your query. Here's what I found:

## Mohammad Hasandoost's Etymology Dictionary

Mohammad Hasandoost authored a specialized etymological dictionary of Persian (Farhang-e Risheh-shenāsi-ye Zabān-e Fārsi) which was published in 2014 in five volumes by the Academy of Persian Language and Literature. This dictionary was recognized as a distinguished work in the 33rd session of the Islamic Republic of Iran's Book of the Year award in the category of "Ancient Languages."

## The Word "Kolux" (کلوخ - Clod/Lump)

Regarding the etymology of the Persian word "kolux" (کلوخ), the search results indicate that the word kolux is derived from the roots "kol" and "lakh," referring to pieces or chunks that are dried out or lacking moisture, as the term "kol" or "kal" means dry and waterless.

The search results provide information about this word from various Persian dictionaries and etymological sources, though the specific entry from Hasandoost's dictionary about this particular word wasn't directly displayed in these results. You may want to consult the actual dictionary volumes for more detailed etymological analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T21:20:13.503Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%DA%A9%D9%84%D9%88%D8%AE/",
 "prompt": "Quote the entries for کلوخ from فرهنگ معین, لغت‌نامه دهخدا, and any etymology (ریشه) given, including any Pahlavi form."
}
```


## [2026-09-06T21:20:14.920Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D9%82%D9%81%D9%82%D8%A7%D8%B2/",
 "prompt": "Quote the entries for قفقاز from فرهنگ معین and دهخدا, including any statement about the origin of the name (Arabic, Greek, etc.)."
}
```


### [2026-09-06T21:20:20.018Z] TOOL RESULT

```
# Entries for کلوخ

**فرهنگ معین:**
"(کُ) (اِ.) گل خشک شده و به هم چسبیده"
(Dried earth stuck together)

**لغت‌نامه دهخدا:**
"گل خشک شده" (dried earth), with extended definitions including pieces of dried clay resembling stone, and idiomatic uses such as "کلوخ بر لب زدن" (concealing something obvious).

**Etymology:**
The page presents user-submitted etymological theories suggesting کلوخ derives from "کل" (dry) + "لاخ" (piece), with comparisons to English cognates like *clod*, *clot*, and *clay*—all potentially related to a root meaning adhesiveness or mud.
```


### [2026-09-06T21:20:23.121Z] TOOL RESULT

```
# Caucasus (قفقاز) Entries

## Dehkhoda Dictionary Entry

"نام ناحیه ای است بین دریای سیاه و بحر خزر که در حدود 154250 میل مربع مساحت دارد"

(A region between the Black Sea and the Caspian Sea with an area of approximately 154,250 square miles)

## Moein Dictionary Entry

The Moein dictionary entry provided in the source is briefer, describing it as: "ناحیه ای است واقع بین بحر خزر و بحراسود"

(A region located between the Caspian Sea and the Black Sea)

## Etymology

According to the Dehkhoda dictionary, the name's origin derives from Scythian: "نام قفقاز از نام سکایی kroy - khasis کروی - خاسیس به معنی یخ درخشان، سفید یا برف گرفته شده است"

(The name comes from the Scythian *kroy-khasis*, meaning "shining ice" or "white snow," rendered in Greek as *Kaukasos*)
```


## [2026-09-06T21:20:33.936Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### LEW crusta/crudus\"; grep -n \"crusta\\|crüdus\\|crudus\" LEW_1910.txt | head -10\necho \"### LAT crusta\"; grep -n \"crusta\\|crudus\" LAT.txt | head -10\necho \"### SKT crystal/crude/crust\"; grep -n \"^crystal\\|crystal,\\|crude,\\|crust,\" SKT.txt | head -10\necho \"### SYN kreas\"; grep -n \"kreas\\|xpeas\" SYN.txt | head -5",
 "description": "Latin dicts and Skeat"
}
```


### [2026-09-06T21:20:34.026Z] TOOL RESULT

```
### LEW crusta/crudus
### LAT crusta
9025:cammarus, -I (gam-, gabb-) m.: crustac 4 , 4 crevisse ou crevette,
13810:compose praecox', cf. mdturus} pour le contraire, crudus »
13922:qui recouvre un liquide (=■ crusta ), revetenent de nayonnerie. Le sens
14753:crudelis; crudus; cruentus: v. eruor.crumel( 1 )um
14774:1 ° crudus,-a,-um (cf. herbi-dus, luci-dus) adj . qui marque A la fois
14779:de "cru, non cuit" et crudus a'est opposd a coctus, dont il est devenu
14780:le contre-pied eract, comme le synonyme grec de crudus, <410$, s'oppose
14781:A uemovj de IA le sens de "non digere", cibus crudus (par oppos. a
14787:De crudus "saignant" derivent: crudesco : saigner, qua* magis effuso
14792:le sang, cruel, qui a dans ce sens remplac£ crudus. De IA crudelitas.
### SKT crystal/crude/crust
6840:Flummery,  a  light  food.  (\V,)  W. llymt-u^  llymrwufd,  flunimcry.  sour  oalxneal boiled  and  jellied.  —  W.  Uymrig,  crude, raw ;  Uymus,  sharp,  tart.  —  VV.  Hymu,  lo sharpen;  //y^Mj  sharp.
### SYN kreas
```


## [2026-09-06T21:20:34.773Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/crust",
 "prompt": "Quote the etymology of crust, including Latin crusta, PIE *kreus-, and any note on crude."
}
```


### [2026-09-06T21:20:39.671Z] TOOL RESULT

```
# Etymology of Crust

Based on the Online Etymology Dictionary entry:

The word "crust" originates from early 14c., initially referring to "hard outer part of bread," derived from Old French *crouste* and Latin *crusta* meaning "rind, crust, shell, bark."

The ultimate origin traces to Proto-Indo-European *kreus-, described as a root meaning "to begin to freeze, form a crust." The dictionary notes this PIE root is "suffixed form of root *kreus-" with the definition provided above.

**Note on "crude":** The webpage does not mention or discuss the word "crude" or its etymology, so no information about that connection can be provided from this source.
```


## [2026-09-06T21:20:44.686Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14770,14800p' LAT.txt\necho \"### LAT cruor\"; grep -n \"cruor\" LAT.txt | head -6\necho \"### LAT crystallum\"; grep -n \"crystallum\\|crystallus\" LAT.txt | head -5",
 "description": "Ernout-Meillet crudus/cruor"
}
```


### [2026-09-06T21:20:44.773Z] TOOL RESULT

```
de Varron dans toute la latinite.
D^rivd: cruentus : sanglant, d.' ou iruentS, -as, et incruentus-, non
sanglant (-a u ic tori a). M. L. »343.
A nn mot 'racine *cru- se rattachent:
1 ° crudus,-a,-um (cf. herbi-dus, luci-dus) adj . qui marque A la fois
l'£tat "saignant, sanglant", e.g. Ov., Pont. 1, 3,16, horrent admotas
uolnera cruda «anus, et 1'action "qui fait saigner, couler le sang",
d'ou "cruel, violent" Pl., Tru.643-4, ego faxo dicat me in diebus pqu-
culis/crudum uirum esse. Sur le sens de "saignant" s'est greffd celui
de "cru, non cuit" et crudus a'est opposd a coctus, dont il est devenu
le contre-pied eract, comme le synonyme grec de crudus, <410$, s'oppose
A uemovj de IA le sens de "non digere", cibus crudus (par oppos. a
cibus coctus, concoctus), et "qui ne dig&re pas" (d'ou cruditas "indi-
gestion" et "erudite, chose indigeste", cf. gr. (qiOTiqC, et A basse ^poque
criiditS,-ds; -tdiio, -tio, crudiuus opp. a coctxuus); "vert, non nur"
et "vigoureux" cruda deo uiridisque senectus, Vg., Ae.6,304, etc. - Pan-
roman. M.L.3343; britt. criz.
De crudus "saignant" derivent: crudesco : saigner, qua* magis effuso
crudescunt sanguine pugnae, Vg., Ae.7,788; d'ou incrudesco (Not. Tir.)
et recrudesco", je saigne de nouveau, je me rouvre, qui s'est d'abord
dit des blessures, avant de s'employer au sens figurd.
st crUd&l is (cf. crudesco) i qui sepi ait dans le sang, qui fait couler
le sang, cruel, qui a dans ce sens remplac£ crudus. De IA crudelitas.
M.L.334i,334i a (formes savantes). Sur la forne, v. Benveniste, Orig.de
la formation des noms en- i.-e.,p. 43 .
3° crudarius: arcenti uena in summo reperta crudaria appellatur Plin.
33 > 97 J crudarium: <410X1.vov CGL II 48^,6.
La forne initiale est un non radical qui est conservi dans att.xpea
"viande" (valeur collective) de *xpeFa, av. rru- "chair saignante",
v. polonais kry "sang" (v. sl.ferunt en est 1'ancien accusatif, devenu
nominatif-accusatif)j cf. n.iri.cru (gen.ero) et m.gall. creu "sang
### LAT cruor
1522:Tacite ecrit, A.14,30, captiuo cruore adolere penates. Inversement,
7631:botulus, -I m.: bondin, cf. Tert. Apol. 9 botulos... cruore distensos.
10322:cum ampla, tum casta a cruore ciuili, et absoluraent "exerapt de faute,
14769:sanguis/emicat exultans alte spargitque cruorem, etc. Atteste a partir
### LAT crystallum
```


## [2026-09-06T21:20:54.413Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### AHD kreu\"; grep -n \"kreu\" AHD_watkins1985.txt | head -20\necho \"### MON kristal/pankras\"; grep -n \"کریستال\\|پانکراس\\|پانکرآس\" MON_part1.txt MON_part2.txt | head -10",
 "description": "Watkins kreu- and Mo'in loans"
}
```


### [2026-09-06T21:20:54.481Z] TOOL RESULT

```
### AHD kreu
494:vine, grape: GRAPE; c. Old French grapon, grapnel: GRAPNEL; d. Old French grape, a hook: GRAPPLE; e. Ital- ian dialectal grappa, vine stem, brandy: GRAPPA. 2. Old English crump, crumb, crooked, bent, stooping: CRUM- MIE, CRUMPET, (CRUMPLE). 3. Low German krimpen, to wrinkle: CRIMP!. 4. Middle Dutch crampe, hook, and Frankish *kramp, hook: cramMpP?. 5.Old High German krampfo, a cramp, akin to the Germanic source of Old French crampe, cramp: CRAMP!. 6. Old English crypel, a cripple: CRIPPLE. 7. Germanic *kreupan in Old English créopan, to creep: CREEP. 8. Middle Low German krink, a ring: CRINGLE. 9. Germanic *krengan in Old English cringan, to yield: CRINGE. 10. Middle Dutch crinkelen, akin to Middle English crinkelen, to make kinks in: CRINKLE. 11. Old Norse kriki, a bend, nook: CREEK. 12. Old Norse krékr, a hook: cRooOK. 13. Frankish *krok- (> Old French croc), a hook: CROCHET, (CROCKET), (CROQUET), (CROUCH); ENCROACH. 14. Old English crycc, (bent) staff, crutch: CRUTCH. 15. Old French crosse, crook: CROSIER, LACROSSE. 16. Middle Dutch crulle, curly: CRULLER, CURL. 17. Old English cranc-(stzf), a weaving implement: CRANK}. 18. Norwegian krake, a sickly beast, akin to the source of Middle English crok, an old ewe: cRocK3, 19. Old Norse karpa, to boast: CaRP!, 20. Middle Dutch kroes, curled, akin to the source of Old French grosele, gooseberry: GROSSULARITE. II. Words meaning ‘“‘a rounded mass, collection; a round object, vessel, container.” 1. Old English cruma, a frag- ment: CRUMB. 2. Frankish *kruppa, rump, akin to the Germanic source of Old French croup, rump: CROUP?, (CROUPIER), CRUPPER. 3. Old English cropp, cluster, bunch, ear of corn: crop. 4. Italian gruppo, an assem- blage: Group. 5. Old English crocc, pot: CROCK}. 6, Mid- dle Dutch cruyse, pot: CRUSE. 7. Old English cribb, manger: CRIB. 8. Old English cradel, cradle: CRADLE. 9. Frankish *kripja, cradle, akin to the Germanic source of Old French cre(s)che, crib: CRECHE. 10. Old English creet and Old Norse kartr, wagon: CART. 11. Old English croft, small enclosed field: crort. [Pok. 3. ger- 385.] gerbh-. To scratch. 1. Germanic *kerban in Old English ceorfan, to cut: CARVE. 2. Zero-grade Germanic form *kurbiz in Old English cyrf, a cutting (off): KERF. 3. Variant form *grebh- in: a. Germanic *krab(b)- in Old English crabba, a crab: CRAB}; b. Germanic *krabiz- in Old French crevise, crayfish: CRAYFISH; C. perhaps Ger- manic *krab- in Old Norse krafla, to crawl: CRAWL. 4. Zero-grade form *grbh- in Greek graphein, to scratch, draw, write, and gramma (< *grbh-mn), a picture, writ- ten letter, piece of writing, and grammé, a line: GRAF- FITO, GRAM!, -GRAM, GRAMMAR, GRAPH, -GRAPH, -GRAPHER, GRAPHIC, -GRAPHY; AGRAPHA, AGRAPHIA, DIAGRAM, EPIGRAM, (EPIGRAPH), GRAPHITE, ICONOGRA- PHY, PARAGRAPH, PROGRAM, PSEUDEPIGRAPHA, TETRA- GRAMMATON, TOPOGRAPHY. [Pok. gerebh- 392.] [gerere. To carry, carry on, act, do. Latin verb of un- known origin. Oldest form ges-, past participle gestus. GERENT, GERUND, (GEST), GESTATION, (GESTICULATE), GESTURE, JEST; ARMIGER, BELLIGERENT, (CONGERIES), CONGEST, DIGEST, EGEST, INGEST, REGISTER, SUGGEST, VELIGER.] gere-'. To grow old. 1. Suffixed lengthened-grade form *géro-s- in Greek géras, old age: AGERATUM, CALOYER, GERIATRICS. 2. Suffixed form “gera-ont- in Greek geron (stem geront-), old man: GERONTO-. [Pok. ger- 390.] gere-2. To cry hoarsely; also the name of the crane. I, Words meaning “‘to cry hoarsely”; also words denoting the crow. 1, Germanic *kré- in: a. Old English crawe, a crow: CROW}; b. Old English crdwan, to crow: CROW?; c. Old English cracian, to resound: CRACK; d. Middle Dutch krdken, to crack: CRACKNEL; @. Old Norse kraka, a crow: CRAKE. f. Middle Dutch krdnen, to groan, la- ment: CROON. 2. Possibly (but more likely imitative) Germanic *kur(r)- in Old Norse kurra, to growl, akin to Middle English curre, cur: cur. II. Words denoting a
643:kreus-*
645:kret-2. To beat. O-grade form *krot- in Greek krotein, to strike, beat: DICROTISM, TRICROTIC. [Pok. 2. kret- 621.] kreue='. Raw flesh. 1. Lengthened-grade form *kréw- in Germanic *hréwaz in Old English hréaw, raw: RAW. 2. Suffixed form *krewo-s- in Greek kreas, flesh: CRE- ATINE, CREODONT, CREOSOTE, PANCREAS. 3. Suffixed zero-grade form *krii-do- (< *krua-do-) in: a. Latin cridus, bloody, raw: CRUDE; ECRU, RECRUDESCE; b. Lat- in cridélis, cruel: CRUEL. [Pok. 1. A. kreu- 621.]
646:kreue-2. To push, strike. 1. Germanic *hrewwan in Old
647:kreup-
648:English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
940:*skerb(h)-, *skreb(h)-. 1. Germanic *skarpaz, cutting, sharp, in: a. Old English scearp, sharp: SHARP; b. Gothic skarp6, pointed object, akin to the possible Germanic source of Italian scarpa, embankment: scarp. 2. Ger- manic *skrap- in: a. Old Norse skrap, “pieces,” remains: SCRAP!; b. Old Norse skrapa, to scratch: SCRAPE. 3. Ger- manic skrab- in: a. Middle Dutch schrabben, to scrape: SCRABBLE; b. Middle Dutch schrobben, to scrape: SCRUB!. 4, Germanic *skrub- in Old English scrybb, shrub (< “rough plant”): SHRUB. 5. Latin scrobis, trench, ditch: SCROBICULATE. 6. Latin scrdfa, a sow (< “rooter, digger”): SCREW, SCROFULA. [Pok. 4. sker-, Section I. 938.] sker-2. To leap, jump about. Perhaps same root as sker-3. 1. Extended form “skerd- in Germanic *skert- in Middle High German scherzen, to leap with joy: SCHERZO. 2. O-grade variant form *kor- in Latin coruscdre, to vibrate, glisten, glitter: coRUSCATE. [Pok. 2. (s)ker- 933.] sker-3. Also ker-. To turn, bend. Presumed base of a number of distantly related derivatives. 1. Extended form *(s)kreg- in nasalized form *(s)kre-n-g- in: a. Ger- manic *skrink- in Old English scrincan, to wither, shrivel up: SHRINK; b. variant *kre-n-g- in Germanic *hrunk- in (i) Old Norse hrukka, a crease, fold: RUCK? (ii) Frankish *hrunkjan, to wrinkle (> Old French fronce, pleat): FLOUNCE!, 2, Extended form *(s)kregh- in nasalized form *skre-n-gh- in Germanic *hringaz, something curved, circle, in: a. Old English Aring, a ring: RING!; b. Old French renc, reng, line, row: RANCH, RANGE, RANK}, RINK; ARRANGE, DERANGE; C. Middle Dutch rinc (com- bining form ring-), a ring: RINGHALS. 3. Extended form *kreuk- in Germanic “*hrugjaz in: a. Old English hrycg, spine, ridge: RIDGE; b. Old High German hrukki, back: RUCKSACK. 4. Suffixed variant form *kur-wo- in Latin curvus, bent, curved: CURB, CURVATURE, CURVE, CUR- vET. 5. Suffixed extended form kris-ni- in Latin crinis (< *crisnis), hair: CRINITE; CRINOLINE. 6. Suffixed ex- tended form *kris-td- in Latin crista, tuft, crest: CREST, CRISTA, CRISTATE. 7. Suffixed extended form *krip-so- in Latin crispus (metathesized from *cripsus), curly: CREPE, CRISP, CRISPATE. 8. Extended expressive form *kriss- in Latin crisdre, (of women) to wiggle the hips during copulation: crissuM. 9. Perhaps reduplicated form *ki-kr-o- metathesized into Greek krikos, a ring (> Latin circus, ring, circle): CIRCA, CIRCLE, CIRCUM-, SEARCH; CRICOID. 10. Suffixed o-grade form *kor-6no- in Greek kordnos, curved: (CORONA), CROWN; CORONOID. 11. Suffixed variant form *kur-to- in Greek kurtos, bent: KURTOSIS. [Pok. 3. (s)ker- 935.] sker-4. Excrement, dung. Extension of sek-, “to cut, separate,” hence “to void excrement.” 1. Form *sk-6r- in Greek skdr (genitive skatos < *sk-nt-), dung: SCATO-, SCORIA, SKATOLE. 2. Extended form “skert- in taboo metathesis *sterk-os- in: a. Latin stercus, dung: STERCO- RACEOUsS; b. variant forms *(s)terg-, *(s)treg- in Germanic *threkka- in Middle High German dréc, dung: DRECK. [Pok. sker-d- 947; 8. (s)ter- 1031.] skerbh-. Also skerb-. To turn, bend. Extension of sker-3. 1. Variant form *skreb- in Germanic *skrip- in Old Norse skreppa, to slip, and derivative Old Norse skorpna, to shrink, be shriveled, akin to the probable Scandinavian source of Middle English scorchen, to scorch: SCORCH. 2. Nasalized variant form *(s)kre-m-b- in: a. Germanic *hrimp-, *hrump- in (i) Old English hrympel, wrinkle, fold: RIMPLE (ii) Middle Dutch rom- pelen, to wrinkle: RUMPLE (iii) Old French ramper, to climb, rear up: RAMP?; b. Germanic *skrimp- in (i) Mid- dle Low German schrempen, to shrink, wrinkle, perhaps akin to the possible Low German source of Middle English shrimp, pygmy, shrimp: SHRIMP (ii) Swedish skrympa, to shrink, perhaps akin to the possible Scandi- navian source of SCRIMP. 3. Variant form *kramb- in Greek krambé, cabbage (having wrinkled, shrunken
946:skot-. Dark, shade 1. Suffixed form *skot-wo- in Ger- manic *skadwaz in Old English sceadu, shade: SHADE, SHADOW. 2. Suffixed form *skot-o- in Greek skotos, darkness: scoToMa. [Pok. skot- 957.] skreu-. To cut; cutting tool. Extension of sker-'. 1. Basic form *skreu- in: a. Germanic *skraw- in Old English scréawa, shrew (having a pointed snout): SHREW, (SHREWD); b. Germanic *skraud- in Old English scréade, piece, fragment: SCREED, SHRED; C. Germanic *skrid- in (i) Old English scriid, garment (< “piece of cloth”): SHROUD (ii) Old French escro(uje, scroll: SCROLL (iii) Dutch schrood, a slice, shred: scRop. 2. Extended form “skreut- in Latin scriita, trash, frippery: SCRUTINY. 3. Extended variant form ‘*skraut- in Latin scrétum, scrotum (probably identified with scrautum, leather quiver for arrows): SCROTUM. [Pok. 4. (s)ker-, Section ITI. 947.]
1242:ANA- an! ANABAENA gWa- ANABAPTIST g¥ébh-1 ANABIOSIS gWei- ANACOLUTHON sem-! ANACRUSIS kreue-2 ANADEM dé- ANADIPLOSIS dwo- ANADROMOUS der-1 ANAGLYPH gleubh- ANAGOGE ag- ANALCIME = alek- ANALECTS leg-1 ANALEPTIC (s)lag¥- ANALOGOUS leg-! ANALYSIS leu-1 ANAMNESIS men-1 ANAPEST peu- ANAPHORA bher-? ANARTHROUS ar- ANASARCA twerk- ANASTOMOSIS ste-men- ANASTROPHE  streb(h)- ANATHEMA dhé-1 ANATOMY tem- ANCESTOR ked- ANCHOR ank- ANCHORITE ghé- ANCIENT! ant- ANCILLARY kWel-1 ANCON ank-
1399:CRANIUM ker-1 CRANK! ger-2 CRASH? ker-4 CRATE kert- CRATER kere- CRAW gWere-4 CRAWL! gerbh- CRAYFISH gerbh- CREATE ker-3 CREATINE kreue-1 CRECHE ger-2 CREDENCE kerd-1 CREDIBLE kerd-1 CREDIT kerd-1 CREDO kerd-1 CREDULOUS_ kerd-1 CREEK ger-2 CREEP ger-2 CREMATE ker-4 CREODONT kreue-1 CREOLE ker-3 CREOSOTE kreue-1, teus- CREPE sker-3 CREPITATE ker-2 CRESCENDO ker-3 CRESCENT ker-3 CRESS gras- CREST sker-3 CREVICE ker-2 CREW! ker-3 CRIB ger-2 CRIBRIFORM krei- CRICKET! ker-2 CRICOID  sker-3 CRIME krel- CRIMP! ger-2 CRIMSON k*rmi- CRINGE ger- CRINGLE ger-2 CRINITE sker-3 CRINKLE ger-2 CRINOLINE fino-, sker-3 CRIOSPHINX ker-1 CRIPPLE ger-2 CRISIS krei- CRISP sker-3 CRISPATE sker-3 CRISSUM sker-3 CRISTA sker-3 CRISTATE sker-3 CRITERION krei- CRITIC krei- CROCHET ger-2 CROCIDOLITE krek-1 CROCK! ger-2 GROCK® ger-? CROCKET ger-2 CROFT ger-2 CROMLECH léu-1, skerbh- CRONE sker-1 CROOK ger-2
1401:CROON gere-2 CROP ger-2 CROQUET ger-2 CROSIER ger-2 CROUCH ger-2 CROUP2 ger-2 CROUPIER ger-2 CROUTON kreus- crow! gere-2 cRow2 gere-2 CROWD! greut- CROWD? krut- CROWN sker-3 cRucIFY dhig’- CRUD greut- CRUDE kreue-1 CRUEL kreue-1 CRULLER ger-2 CRUMB ger-2 CRUMMIE ger-2 CRUMPET ger-2 CRUMPLE ger-2 CRUPPER ger-2 CRUSE ger-2 CRUST kreus- CRUSTACEAN kreus- CRUSTACEOUS kreus- CRUSTOSE kreus- CRUTCH ger-2 cRYO- kreus- CRYPT krau-. CRYPTIC krau- CRYPTO- krau- CRYSTAL kreus- CRYSTALLINE kreus- CRYSTALLO- kreus- CTENIDIUM pek-2 CTENOID pek-2 CTENOPHORE pek-2 CUBBY ku-
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1565:GOAD ghei-1 GOAT ghaido- GOD gheu(e)- GODSEND sent- GOFFER webh- GOLD ghel-2 GOLIARD gWel-3 GOMPHOSIS gembh- -GON genu-! GONAD gene- GONFALON gWhen-1 GONIOMETER genu-1 GONIOMETRY genu-! GONION genu-! GONO- gena- coop ghedh- GOOSE! ghans- GORE! ghaiso- GORE? ghaiso- GORGE gWere-4 GORGET gWera-4 GORSE ghers- GOSHAWK ghans- GOSLING ghans- GOSPEL spel-3 GOSSIP s(w)e- GOUACHE akWa- GOWAN ghel-2 GRAB! ghrebh-1 GRABEN ghrebh-2 GRACE gWera-3 GRACKLE gera-2 GRADE ghredh- GRAFFITO gerbh- GRAIN gre-no- GRAM! § gerbh- GRAM? gre-no- -GRAM gerbh- GRAMA gras- GRAMINEOUS_ gras- GRAMMAR gerbh- GRAMPUS_peisk- GRANADILLA gfe-no- GRANARY gre-no- GRANDILOQUENCE tolkw- GRANGE gre-no- GRANITE gr@-no- GRANT kerd-1 GRANULE gre-no- GRAPE ger-2 GRAPH gerbh- -GRAPH gerbh- -GRAPHER gerbh- GRAPHIC gerbh- GRAPHITE gerbh- -GRAPHY gerbh- GRAPNEL ger-2 GRAPPA ger-2 GRAPPLE ger-2 GRASP ghrebh-1 GRAss_ ghré- GRATE! grat- GRATE? kert- GRATEFUL gWere-3 GRATIFY gWere-3 GRATIS gWera-3 GRATITUDE gWero-3 GRATUITY gWera-3 GRAUPEL kreup- GRAVE! ghrebh-2 GRAVE? gwWera-2 GRAVES ghrebh-2 GRAVEL ghréu- GRAVID gWera-2 GRAVURE ghrebh-2 GRAY gher-3 GRAYWACKE wegh-
1570:GRUB ghrebh-2 GRUDGE gru- GRUEL ghréu- GRUESOME ghréu- GRUFF kreup- GRUMBLE ghrem- GRUNION gru- GRUNT gru-
2049:PANACEA yék- PANACHE pet- PANADA pa- PANATELA pa- PANCRATIUM pant- PANCREAS kreue-1, pant- PANDECT dek-1 PANDEMIC da- PANDORE pandoura PANE pan- PANEGYRIC ger-! PANEL pan-
2164:RAW kreue-!
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
2175:RECTUM reg-1 RECUMBENT keu-2 RECUPERATE kap- RECUR kers-2 RED reudh-1 REDE ar- REDEEM em- REDEMPTION em- REDOLENT od-1 REDOUBT deuk- REDOUBTABLE dwo- REDOUND wed-! REDSTART ster-1 REDUCE deuk- REDUNDANT wed-1 REDUVIID eu-! REED kreut- REEF! = rebh-2 REEF? rebh-2 REEK reug- REEL! krek-1 REFECT dhé-1 REFECTORY dhé-1 REFER bher-! REFLUX bhieu- REFRACT bhreg- REFRAIN! ghrendh-
2201:RUBELLA reudh-1 RUBEOLA reudh-1 RUBESCENT reudh-1 RUBICUND reudh-1 RUBIDIUM reudh-1 RUBIGINOUS reudh-! RUBRIC reudh-1 RUBY reudh-1 RUCK? = sker-3 RUCKSACK sker-3 RUDDER ere-1 RUDDLE reudh-1 RUDDOCK reudh-1 RUDDY reudh-! RUE! kreue-2 RUFESCENT reudh-1 RUFFLE! kreup- RUFOUS reudh-1 RUG reu-2
2204:RUNE! riino- RUNE? riino- RUNNEL rei-3 RUPICOLOUS reup- RUPTURE reup- RURAL reue- RUSH? rezg- RUSSET reudh-! RUsT reudh-1 RUSTIC reue- RUT? reu-1 RUTABAGA wrad- RUTH kreue-2 RUTILANT reudh-1 Rx _ kap-
### MON kristal/pankras
MON_part1.txt:22747:کریستال‌هابی است که بی‌رنگ که طعمش 
MON_part1.txt:22852:از جوزالقی استخراج کنند. کریستال‌های آن
```


## [2026-09-06T21:21:06.986Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/crude",
 "prompt": "Quote the etymology of crude: Latin crudus, cruor, PIE root."
}
```


## [2026-09-06T21:21:08.072Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%81%D9%82%D8%A7%D8%B2",
 "prompt": "What do the Persian and Arabic entries for قفقاز say — meaning and any etymology (borrowed from Greek/Latin/Russian)?"
}
```


### [2026-09-06T21:21:12.188Z] TOOL RESULT

```
# Etymology of Crude

Based on the Online Etymology Dictionary, here's the etymology:

**Latin Origin:**
"From Latin _crudus_ 'rough; not cooked, raw, bloody'" (late 14c.)

**Proto-Indo-European Root:**
The word traces back to the PIE root *kreue-, meaning "raw flesh." The dictionary notes it comes from "PIE _\*krue-do-_, from PIE root _\*kreue-_"

**Meaning Evolution:**
Initially describing physical states like uncooked food or untanned hides, the term later acquired figurative senses. "Meaning 'lacking grace, socially unrefined' is attested by 1640s." The modern petroleum term "crude oil" emerged in 1865, referring to oil in its natural, unrefined state.
```


### [2026-09-06T21:21:12.841Z] TOOL RESULT

```
# Response

Based on the Wiktionary content provided, here's what the Persian entry states:

**Meaning:** The word قفقاز (qafqāz) means "Caucasus."

**Etymology:** The term ultimately derives from Middle Persian "*Kaf kōf" which means "Mount Qaf."

**Note:** The page displays only a Persian entry. There is no Arabic entry shown in the provided content, though the page header indicates the term exists in 8 languages total. The etymology does not reference borrowing from Greek, Latin, or Russian—instead, it traces back to a Persian mythological reference to Mount Qaf.
```


## [2026-09-06T21:21:39.440Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krewh%E2%82%82-|page 276 root Kreu: PIE *krewh2- 'blood outside the body, raw flesh' and the *krews- extension\" \\\n \"https://www.etymonline.com/word/crystal|page 276 node 6-10: Gk krystallos < kryos 'frost' < PIE *kreus-\" \\\n \"https://www.etymonline.com/word/crust|page 276 node 19-20: L. crusta < PIE *kreus- 'to begin to freeze, form a crust'\" \\\n \"https://www.etymonline.com/word/crude|page 276 node 19-20: L. crudus < PIE *kreue- 'raw flesh'\" \\\n \"https://www.etymonline.com/word/pancreas|page 276 nodes 15-18: Gk pankreas = pan + kreas 'flesh'\" \\\n \"https://en.wiktionary.org/wiki/Caucasus|page 276 node 2/5: Latin Caucasus < Gk Kaukasos\" \\\n \"https://en.wiktionary.org/wiki/%CE%9A%CE%B1%CF%8D%CE%BA%CE%B1%CF%83%CE%BF%CF%82|page 276 node 1: Gk Kaukasos etymology called uncertain; PIE *kewk- or Iranian Kaf kof\" \\\n \"https://en.wiktionary.org/wiki/%D9%82%D9%81%D9%82%D8%A7%D8%B2|page 276 node 4: Persian qafqaz derived by Wiktionary from MP *Kaf kof, not from Latin via Arabic\" \\\n \"https://abadis.ir/fatofa/%DA%A9%D9%84%D9%88%D8%AE/|page 276 node 13: Moin/Dehkhoda entries for kolux 'dried clod'\" \\\n \"https://abadis.ir/fatofa/%D9%82%D9%81%D9%82%D8%A7%D8%B2/|page 276 node 4: Dehkhoda on qafqaz from Scythian kroy-khasis 'shining ice' via Gk Kaukasos\" \\\n ; do url=\"${u%%|*}\"; note=\"${u##*|}\"; python3 tools/fetch_source.py \"$url\" --note \"$note\" 2>&1 | tail -2; done",
 "description": "Archive web sources"
}
```


### [2026-09-06T21:21:48.064Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/2b1dc9e5df656b59.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b315311df7776bb6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ed85ce0eeda388a9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a795f4094ee2502c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8d09cf3d7be9b0e7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88d176f47f298486.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c1311e39a0d5952d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/88f2eeff74624559.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ccb9d3a6130bf948.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e356e95a9607dced.txt
```


## [2026-09-06T21:21:53.926Z] TOOL CALL #47: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg276.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/276.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3\necho \"=== verify_check tool head ===\"; head -60 /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Copy page PNG and inspect checker"
}
```


### [2026-09-06T21:21:53.993Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
=== verify_check tool head ===
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


## [2026-09-06T21:21:56.444Z] TOOL CALL #48: Bash

```json
{
 "command": "sed -n '60,140p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of checker"
}
```


### [2026-09-06T21:21:56.486Z] TOOL RESULT

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


## [2026-09-06T21:22:34.173Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD Bd1 kreu\"; grep -n \"kreu-\\|kreus-\\|krus-\" incoming/WLD/WLD_Bd1_pages.txt | head -8\necho \"### BQT kolux\"; grep -n \"کلوخ\" BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt 2>/dev/null | head -8\necho \"### ARY pages kolux\"; grep -n \"کلوخ\\|KOLUKH\\|kolux\" incoming/ARY/ARY_pages.txt incoming/ARY/ARY_latin_index_pages.txt 2>/dev/null | head -8\necho \"### HRN/HUB kristall/kulux\"; grep -n -i \"kulūḫ\\|kulûḫ\\|kul.x\" HRN.txt HUB.txt | head -8",
 "description": "Grep WLD, BQT, ARY for root and kolux"
}
```


### [2026-09-06T21:22:34.274Z] TOOL RESULT

```
### WLD Bd1 kreu
46182:krus- „Schienbein, Unterschenkel“.
61677:     ahd. krus-k „furfur“,           ahd. Krii-sch „Kleie‘-                                  (auch Grusch,                                       Griist durch
### BQT kolux
incoming/BQT/BQT_v3_pages.txt:20774:‏آن‌کت کلوخ روخ لقب کرد خو ب کرد
incoming/BQT/BQT_v3_pages.txt:24532:وکلوخ شده * هرمزدنامه س ۳۲ ۶
incoming/BQT/BQT_v3_pages.txt:32005:‏و بعربی عقمق خوانند - وبتر کی بمعن ی کلوخ‎
incoming/BQT/BQT_v3_pages.txt:34903:‏کیتی همه سر بسر کلوخی است
incoming/BQT/BQT_v3_pages.txt:34905:‏قم تو ازآن‌کلوخ کردست .
incoming/BQT/BQT_v3_pages.txt:34917:کلوخ امروه ۱ - نوعی از امرود
incoming/BQT/BQT_v3_pages.txt:34920:کلوخ افداد - -وراخهایی باند که
incoming/BQT/BQT_v3_pages.txt:34926:‎oles‏ کنند وآترا کلوخ الدازان هم میگویند ؛
### ARY pages kolux
### HRN/HUB kristall/kulux
```


## [2026-09-06T21:22:40.326Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '34900,34930p' incoming/BQT/BQT_v3_pages.txt\necho \"=== BQT v3 pdf page tag ===\"; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: '$1<34917' | tail -2",
 "description": "Borhan-e Qate kolux entry"
}
```


### [2026-09-06T21:22:42.578Z] TOOL RESULT

```
‏۴-کردی 61۵6 ( مفرور ؛ قس: 46 فر ) « ژابا س ۳۵۰ *:

‏کیتی همه سر بسر کلوخی است

‏قم تو ازآن‌کلوخ کردست .
‎SE‏ غزبوی س ۰۷۷۰ .
(بر هان ‎(tre ab‏

[pdf page 476]
alae

شده - ولختهای ‎yes‏ افتاده و خاك برهم‌چبیدء
سخت شده باشد و آترا بت کی ‎ALT‏ خوانند -
و خشت ‎Sey‏ خام ويخته را نیز گوبند وکنابه
از مردم خشك طبیمت و کم فطرت و بی همت
باشد .
کلوخ امروه ۱ - نوعی از امرود
‎Sy‏ ناهموار بیمزه باشد .

کلوخ افداد - -وراخهایی باند که
در زس ‎ys SoS‏ قلعه مازند تا چون خسم
تزديك دبوار ‎ali‏ آید از ‎OT‏ سوراخها سنگه
وآتش و خاکتر ‎ten‏ ریزند و آزا سنگه
اندازهم میگوبند ۴ - وسیر و کشت وشرابخوری
و عيش و عشرنی را کوبند که درآخرهای‌ماء(۱)
‎oles‏ کنند وآترا کلوخ الدازان هم میگویند ؛
و بعضی کویندکلوخ اندازنام ‎abe‏ ماه شعبان‌است
- و نبیر؛ فرزدد را 55 کفته‌اند که پسر پسر با
دختر دختر فرزلد باشد - و بمعنی فلاخن عم
آمده است ‎oT,‏ آلتی باشد که شاطران وشبانان
=== BQT v3 pdf page tag ===
34811:[pdf page 475]
34909:[pdf page 476]
```


## [2026-09-06T21:23:03.799Z] AGENT

Now I'll write the verification file.


## [2026-09-06T21:32:12.186Z] TOOL CALL #51: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk276.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nPOK_Q = (\"POK_02 leaf 282 (printed pp. 621-622): \\\"1. kreu-, kreuə-/krū- 1. 'dickes, stockendes Blut, \"\n         \"blutiges, rohes Fleisch', vermutlich 'geronnen (vom Blut)', dazu eine 2. Gruppe kreus-, krus- \"\n         \"für 'Eis (als erstarrendes), Kruste (ursprüngl. von Eis oder Wundschorf), Eisscholle, \"\n         \"Erdscholle' ... und verbal 'frieren, schaudern'\\\"\")\n\nentry = {\n \"entry\": 2,\n \"root\": \"Kreu, Qreu, Qreus, Qruwes, Qrus\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *krewh₂- 'blood outside the body; bloody/raw flesh' (Pokorny 1. kreu-, kreuə-, krū-, p.621) together with its s-extension *krews-/*krus- 'to begin to freeze, form a crust' (Pokorny's group B, same page; Watkins kreus-)\",\n \"note\": (\"Nourai's root name and gloss are lifted almost verbatim from Klein s.v. 'crust' (KLN p.378): \\\"All these words \"\n          \"derive fr. I.-E. *qreus-, *qrus-, *qruwes-, enlarged forms of base *qreu-, 'icy, solid, coagulated, congealed'\\\" — \"\n          \"hence the odd-looking string Qreus/Qruwes/Qrus. Pokorny 621 has exactly the same double root: the 'bloody flesh' \"\n          \"group (A) and the 'ice, crust, clod, to freeze' group (B) under one headword. Watkins (AHD 1985) separates them into \"\n          \"kreuə-1 'raw flesh' [Pok. 1.A. kreu- 621] and kreus- 'to begin to freeze, form a crust' [Pok. 1.B. kreu- 621], but \"\n          \"still refers both to Pokorny 621, so the amalgam in the box is defensible. Modern Wiktionary reconstructs *krewh₂- \"\n          \"and notes that *krews- 'to freeze, harden' \\\"has been argued as from a separate root\\\". Language label (Indo-European) \"\n          \"and glosses are correct; only the implication that 'icy' and 'bloody' are one and the same root is debatable.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *krewh₂- به معنی «خون بیرون‌ریخته، گوشت خام و خونین» است که پوکورنی (صـ ۶۲۱) آن را \"\n             \"با گروه دوم *kreus-/*krus- «یخ بستن، پوسته بستن، کلوخ» زیر یک سرواژه آورده است. نام و معنی ریشه در نمودار نورایی \"\n             \"عیناً از مدخل crust در فرهنگ کلاین (صـ ۳۷۸) گرفته شده است: «*qreus-, *qrus-, *qruwes- صورت‌های گستردهٔ پایهٔ \"\n             \"*qreu- «یخین، سخت، بسته‌شده»». واتکینز در پیوست AHD این دو را جدا می‌کند ولی هر دو را به همان صفحهٔ پوکورنی ارجاع \"\n             \"می‌دهد. بنابراین ادعای نورایی دربارهٔ ریشه و برچسب زبانی درست است؛ تنها یکی‌دانستن دو معنی «یخ» و «خون» را برخی \"\n             \"پژوهشگران امروزی (ویکی‌واژه) با احتیاط دو ریشهٔ جدا می‌شمارند.\"),\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krewh%E2%82%82-\",\n             \"https://www.etymonline.com/word/crust\"],\n \"ref_check\": [\n   {\"ref\": \"POK:621\", \"status\": \"supports\",\n    \"note\": \"Pokorny IEW p.621 (local POK_02.txt, form-feed leaf 282; grep '1. kreu-'). \" + POK_Q + \". The page also carries the Caucasus etymology Nourai uses in node 1.\"},\n   {\"ref\": \"KLN:252\", \"status\": \"partial\",\n    \"note\": \"Klein p.252 s.v. 'Caucasian' (KLN_1966.txt line 6830) gives only \\\"I.-E. base *qreu-, 'to be icy'\\\" — the gloss Nourai copied — while the full string *qreus-/*qrus-/*qruwes- 'icy, solid, coagulated, congealed' is at KLN p.378 s.v. 'crust' (line 9800), which he cites on node 19.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"Bd. I pp. 621-622\", \"stance\": \"supports\", \"note\": POK_Q},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.vv. kreuə-1 and kreus-\", \"stance\": \"supports\",\n    \"note\": \"AHD_watkins1985.txt line 645: \\\"kreue-1. Raw flesh. ... 2. Suffixed form *krewo-s- in Greek kreas, flesh: CREATINE, CREODONT, CREOSOTE, PANCREAS. 3. Suffixed zero-grade form *kru-do- in a. Latin crudus, bloody, raw: CRUDE ... [Pok. 1. A. kreu- 621.]\\\" and line 648: \\\"kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in a. Latin crusta: CRUST ... b. Greek krustallos, ice: CRYSTAL ... 2. *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.]\\\"\"},\n   {\"src\": \"IEC\", \"where\": \"Mann p.562 s.v. krūsos\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt leaf 320 (printed p.562): \\\"krūsos, à 'hard, solid, frozen; frost, ice'. WP I, 479. ... Av. xrūs 'terrible'; Per. kulūx 'clod, sod'; Gk. krūos, n. 'chill, frost, ice'; krus-taino, v. tr. 'freeze' ... OHG hrosa, f. 'frost' ... Long-gde in OE hrūse, f. 'earth, ground'\\\"\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 477-486 (cited by POK)\", \"stance\": \"silent\",\n    \"note\": \"grep of incoming/WLD/WLD_Bd1_pages.txt for 'kreu-', 'kreus-', 'krus-' returns only unrelated hits (line 46182 'krus- „Schienbein“'); the relevant columns are not legible in this OCR, so WP I 477/479 could not be read directly — but both Pokorny and Mann cite them for this root.\"},\n   {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cruor/crudus\", \"stance\": \"supports\",\n    \"note\": \"LAT.txt line ~14798: \\\"La forme initiale est un nom radical qui est conservé dans att. κρέα 'viande' ... de *κρεϜa, av. xru- 'chair saignante', v. polonais kry 'sang'\\\"\"}\n ],\n \"nodes\": []\n}\n\nN = entry[\"nodes\"]\n\ndef node(i, lang, words, verdict, deriv, deriv_fa, sources, refs, cons, **kw):\n    d = {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n         \"derivation\": deriv, \"derivation_fa\": deriv_fa,\n         \"sources\": sources, \"ref_check\": refs, \"consulted\": cons}\n    d.update(kw)\n    N.append(d)\n\n# ---------------- node 1 ----------------\nnode(1, \"Greek\", \"casos; kau-casos\", \"disputed\",\n \"Nourai's box makes 'casos' a Greek word for 'ice' and kau-casos 'shining with ice'. Both the language label and the \"\n \"segmentation are wrong. Greek has no *kasos 'ice'; Καύκασος is a proper name that Greek took over ready-made. \"\n \"Pokorny 622 (group B) gives \\\"Skyth. *xrohu-kasi-, gr. Καύκασος 'Kaukasus' (als 'eis-glänzend')\\\", and Klein p.252 \"\n \"s.v. Caucasian: \\\"fr. Gk. Kaukasos, fr. Scythian Kroukasis ... a compound meaning lit. '(the mountain) shining with ice'. \"\n \"The first element of this compound is a derivative of I.-E. base *qreu-, 'to be icy'. ... The second element is rel. to \"\n \"Gk. kaiein 'to burn'\\\". So it is the FIRST element (Scythian *xrohu-/krou-, from *kreu-) that means 'ice', and the second \"\n \"(-kasi-, cf. Gk. kaiein < *keu-/*ku- 'to burn, shine') that means 'shining' — exactly the reverse of the chart's labels, \"\n \"though Nourai's own cross-reference '☞ Kŭ 1' shows he knew Klein sent the second element to the *keu- 'burn' root. \"\n \"Beyond the mislabelling, the whole Pliny/Scythian etymology (Pliny NH 6.50 'Scythice Croucasim, id est nive candidum') is \"\n \"today regarded as uncertain: Wiktionary's Καύκασος entry offers instead PIE *kewk- 'to elevate, height' or an \"\n \"Iranian source (MP *Kaf kōf 'Mount Qāf'), and does not mention *kreu- at all.\",\n \"نورایی casos را واژه‌ای یونانی به معنی «یخ» می‌گیرد؛ چنین واژه‌ای در یونانی وجود ندارد. \"\n \"پوکورنی (صـ ۶۲۲) و کلاین (صـ ۲۵۲) نام کوه را وام‌واژه‌ای سکایی *xrohu-kasi- می‌دانند که جزء \"\n \"نخستش (از ریشهٔ *kreu-) «یخ» و جزء دومش (هم‌ریشه با kaiein یونانی «سوختن، درخشیدن») «درخشان» است — \"\n \"یعنی دقیقاً واژگونهٔ آنچه در جعبه آمده است. افزون بر این، زبان‌شناسی امروز این ریشه‌شناسی پلینیوسی \"\n \"را قطعی نمی‌داند؛ ویکی‌واژه به‌جای آن *kewk- «بلندی» یا منشأ ایرانی (فارسی میانهٔ *Kaf kōf «کوه قاف») را \"\n \"پیشنهاد می‌کند. پس ادعای نورایی در این گره رد می‌شود.\",\n [\"https://en.wiktionary.org/wiki/%CE%9A%CE%B1%CF%8D%CE%BA%CE%B1%CF%83%CE%BF%CF%82\",\n  \"https://abadis.ir/fatofa/%D9%82%D9%81%D9%82%D8%A7%D8%B2/\"],\n [{\"ref\": \"KLN:252\", \"status\": \"partial\",\n   \"note\": \"KLN_1966.txt line 6830, p.252 s.v. Caucasian: \\\"fr. L. Caucasus, fr. Gk. Kauxasos, fr. Scythian Kroukasis, 'Caucasus', a compound meaning lit. '(the mountain) shining with ice' ... The first element of this compound is a derivative of I.-E. base *qreu-, 'to be icy'. ... The second element is rel. to Gk. kaiein 'to burn'; see caustic.\\\" Klein supports the root but assigns 'ice' to the FIRST element, not to a Greek word 'casos'.\"}],\n [{\"src\": \"POK\", \"where\": \"Bd. I p.622 (group B)\", \"stance\": \"partial\",\n   \"note\": \"POK_02.txt leaf 282: \\\"B. Skyth. *xrohu-kasi-, gr. Καύκασος 'Kaukasus' (als 'eis-glänzend')\\\" — Scythian, not Greek, and the ice element is *xrohu-.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. kreuə-1, kreus-\", \"stance\": \"silent\",\n   \"note\": \"Neither AHD headword lists CAUCASUS/CAUCASIAN among the English derivatives (grep 'kreu' in AHD_watkins1985.txt); Watkins does not endorse the Caucasus etymology.\"},\n  {\"src\": \"WEB-Wiktionary\", \"where\": \"Καύκασος\", \"stance\": \"contradicts\",\n   \"note\": \"\\\"Uncertain; perhaps ultimately from Proto-Indo-European *kewk- ('to elevate; height'), or borrowed from Iranian languages, compare Middle Persian *Kaf kōf ('Mount Qaf, Caucasus mountains')\\\" — no mention of *kreu-.\"}])\n\n# ---------------- node 2 ----------------\nnode(2, \"Latin\", \"caucasus\", \"confirmed\",\n \"Latin Caucasus is the straightforward Latinisation of Greek Καύκασος, taken over by Roman geographers (Pliny, \"\n \"Nat. Hist. 6.50, who reports the local gloss: \\\"Scythice Croucasim, id est nive candidum\\\"), Greek -ος → Latin -us. The \"\n \"gloss in the box ('a very mountainous area between Caspian and Black seas') is the standard geographical sense. The arrow \"\n \"Greek → Latin is uncontroversial; what is doubtful is only the further step back to *kreu- (node 1).\",\n \"لاتینی Caucasus صورت لاتینی‌شدهٔ یونانی Καύκασος است (پایانهٔ -ος یونانی در لاتین به -us بدل می‌شود) و \"\n \"نخست‌بار در جغرافی‌نویسان رومی مانند پلینیوس (تاریخ طبیعی ۶٫۵۰) دیده می‌شود. این پیوند یونانی‌به‌لاتین \"\n \"درست است و مورد اختلاف نیست؛ تنها اتصال آن به ریشهٔ *kreu- محل تردید است.\",\n [\"https://en.wiktionary.org/wiki/Caucasus\"],\n [{\"ref\": \"KLN:252\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt line 6830, p.252: \\\"Caucasian, adj. and n. — Formed with suff. -ian fr. L. Caucasus, fr. Gk. Kauxasos\\\" — the Greek → Latin step is explicit.\"}],\n [{\"src\": \"POK\", \"where\": \"Bd. I p.622\", \"stance\": \"supports\",\n   \"note\": \"POK_02.txt leaf 282 lists \\\"gr. Καύκασος 'Kaukasus'\\\" as the Greek form behind the Latin name.\"},\n  {\"src\": \"WEB-Wiktionary\", \"where\": \"Caucasus (English)\", \"stance\": \"supports\",\n   \"note\": \"\\\"Via Latin Caucasus, from Ancient Greek Καύκασος (Kaúkasos).\\\"\"}])\n\n# ---------------- node 3 ----------------\nnode(3, \"Arabic\", \"\", \"plausible\",\n \"An empty pass-through box: Nourai posits an Arabic intermediary between Latin/Greek Caucasus and Persian qafqāz but \"\n \"prints no Arabic form. The form he must intend is Arabic al-Qawqāz القوقاز (also قبق al-Qabq in the early \"\n \"geographers, e.g. al-Masʿūdī, Ibn Khurradādhbih), which the Muslim geographers took from the Greek/Byzantine name, \"\n \"most likely through Syriac rather than through Latin. The link is credible as a route (Greek → Arabic → Persian) but the \"\n \"chart's parent is Latin, and mediaeval Arabic geography borrowed from Greek/Syriac, not from Latin; and the box is blank, \"\n \"so no Arabic form can be checked as printed.\",\n \"این جعبه خالی است و نورایی هیچ صورت عربی نمی‌آورد؛ مقصود او بی‌گمان عربی القوقاز (و در \"\n \"جغرافی‌نویسان متقدم قبق) است. این وام‌گیری از راه یونانی/سریانی صورت گرفته، نه از لاتینی؛ بنابراین \"\n \"مسیر کلی پذیرفتنی ولی پدرِ نمودار (لاتینی) دقیق نیست. با احتیاط پذیرفتنی است.\",\n [\"https://abadis.ir/fatofa/%D9%82%D9%81%D9%82%D8%A7%D8%B2/\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of Nourai's own (refs=None) and no word.\"}],\n [{\"src\": \"KLN\", \"where\": \"p.252 s.v. Caucasian\", \"stance\": \"silent\",\n   \"note\": \"Klein traces the word only Scythian > Greek > Latin > English; he mentions no Arabic stage (KLN_1966.txt line 6830).\"},\n  {\"src\": \"MON\", \"where\": \"MON_part1/part2 (grep قفقاز)\", \"stance\": \"silent\",\n   \"note\": \"The lexicon volumes of Mo'in on disk mention قفقاز only in passing (MON_part2.txt lines 113, 15779, 93297) as a place name, with no Arabic etymology.\"}])\n\n# ---------------- node 4 ----------------\nnode(4, \"Persian\", \"qafqâz\", \"disputed\",\n \"Persian قفقاز qafqāz 'the Caucasus'. Dehkhoda repeats the classical account, and in the same terms Nourai's root box \"\n \"needs: \\\"نام قفقاز از نام سکایی kroy-khasis به معنی یخ درخشان گرفته شده است\\\" — i.e. Scythian *kroy-khasis \"\n \"'shining ice' → Greek Kaukasos. But the Persian FORM qafqāz, with q- for k- and metathesis of the medial consonants, is not \"\n \"the phonetically expected outcome of a Latin loan; it is the Arabic shape (al-Qawqāz/al-Qabq), and Wiktionary's Persian \"\n \"entry rejects the Graeco-Latin route altogether, deriving قفقاز \\\"ultimately from Middle Persian *Kaf kōf ('Mount Qaf, \"\n \"Caucasus mountains')\\\", i.e. an Iranian name reanalysed as کوه قاف. Since modern scholarship prefers a different immediate \"\n \"origin (Iranian Kaf-kōf, or at best Greek via Arabic — never Latin), the arrow as drawn is disputed.\",\n \"واژهٔ «قفقاز» در فارسی نو. دهخدا ریشه‌شناسی کهن را می‌آورد: «نام قفقاز از نام سکایی kroy-khasis به معنی \"\n \"یخ درخشان گرفته شده است». اما صورتِ فارسی با «ق» و قلب حروف میانی از راه لاتینی توجیه‌پذیر نیست؛ این \"\n \"شکل، شکلِ معرّب (القوقاز/القبق) است، و ویکی‌واژه آن را از فارسی میانهٔ *Kaf kōf «کوه قاف» می‌داند و مسیر یونانی–لاتینی \"\n \"را رد می‌کند. پس زنجیرهٔ «لاتینی ← عربی ← فارسی» به‌صورتی که رسم شده پذیرفتنی نیست.\",\n [\"https://abadis.ir/fatofa/%D9%82%D9%81%D9%82%D8%A7%D8%B2/\",\n  \"https://en.wiktionary.org/wiki/%D9%82%D9%81%D9%82%D8%A7%D8%B2\"],\n [{\"ref\": \"MON5:1474\", \"status\": \"not_checked\",\n   \"note\": \"Mo'in vol. 5 (اعلام) is not among the local OCR files (only the lexicon volumes are). The online Mo'in entry for قفقاز reached through abadis gives only the geographical definition \\\"ناحیه‌ای است واقع بین بحر خزر و بحراسود\\\" with no etymology, so the page reference could be neither confirmed nor refuted.\"}],\n [{\"src\": \"MON\", \"where\": \"فرهنگ معین s.v. قفقاز (via abadis)\", \"stance\": \"partial\",\n   \"note\": \"\\\"ناحیه‌ای است واقع بین بحر خزر و بحراسود\\\" — the meaning matches the chart; no origin given.\"},\n  {\"src\": \"BQT\", \"where\": \"Dehkhoda لغت‌نامه s.v. قفقاز (via abadis)\", \"stance\": \"supports\",\n   \"note\": \"\\\"نام قفقاز از نام سکایی kroy-khasis کروی-خاسیس به معنی یخ درخشان، سفید یا برف گرفته شده است\\\" — supports the ultimate *kreu- origin of the NAME (and, incidentally, confirms that 'ice' is the FIRST element, kroy-).\"},\n  {\"src\": \"WEB-Wiktionary\", \"where\": \"قفقاز (Persian)\", \"stance\": \"contradicts\",\n   \"note\": \"Derives Persian قفقاز \\\"ultimately from Middle Persian *Kaf kōf ('Mount Qaf')\\\", not from Latin/Greek.\"}])\n\n# ---------------- node 5 ----------------\nnode(5, \"English\", \"Caucasian\", \"confirmed\",\n \"English Caucasian is a learned formation of the 17th-18th c.: Latin Caucasus + the suffix -ian; the racial sense was \"\n \"introduced by J. F. Blumenbach in 1795 (De generis humani varietate nativa), who believed the ideal European skull came \"\n \"from the Caucasus. Klein p.252 gives exactly this: \\\"Caucasian, adj. and n. — Formed with suff. -ian fr. L. Caucasus, fr. \"\n \"Gk. Kauxasos\\\". The Latin → English arrow as drawn is correct.\",\n \"واژهٔ انگلیسی Caucasian ساختهٔ عالمانه است: لاتینی Caucasus به‌علاوهٔ پسوند -ian. کلاین (صـ ۲۵۲) همین \"\n \"را می‌گوید. کاربرد نژادی آن را بلومنباخ در ۱۷۹۵ رواج داد. ادعای نورایی در این گره درست است.\",\n [\"https://en.wiktionary.org/wiki/Caucasus\"],\n [{\"ref\": \"KLN:252\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt line 6830: \\\"Caucasian, adj. and n. — Formed with suff. -ian fr. L. Caucasus\\\".\"}],\n [{\"src\": \"KLN\", \"where\": \"p.252\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"},\n  {\"src\": \"WEB-Wiktionary\", \"where\": \"Caucasus (English)\", \"stance\": \"supports\",\n   \"note\": \"\\\"Via Latin Caucasus, from Ancient Greek Καύκασος\\\" — English inherits the Latin form.\"}])\n\n# ---------------- node 6 ----------------\nnode(6, \"Greek\", \"cros; crystacus\", \"transcription_suspect\",\n \"The two Greek words meant are κρύος krýos 'icy cold, frost' (< *krus-es-) and κρύσταλλος krýstallos \"\n \"'ice; rock-crystal' (< *krus-to-), both from the s-extension of *kreu-. Nourai prints them as 'cros' and 'crystacus'. \"\n \"'crystacus' is not a Greek word in any transcription: it is a misprint for crystallus/krýstallos (the -ll- misread or \"\n \"miskeyed as -c-); 'cros' likewise drops the -y- of krýos, though it may just be his loose transcription. I checked the \"\n \"printed page (pdf p.276 = book p.246, PNG copied to data/verification/sources/refs/ocr/BOOK/276.png): the book itself \"\n \"prints \\\"cros : frost\\\" and \\\"crystacus : ice\\\", so the extraction is faithful and the error is Nourai's. The derivation \"\n \"itself is right: Klein p.380 \\\"Gk. krystallos, 'ice; crystal' ... Both these words derive fr. kryos (for *krysos), \"\n \"'frost', which is cogn. with L. crusta\\\"; Watkins puts krustallos under *krus-to-.\",\n \"دو واژهٔ یونانی مورد نظر κρύος (krýos) «سرما، یخ‌بندان» و κρύσταλλος (krýstallos) «یخ؛ بلور» اند، \"\n \"هر دو از گسترشِ s-دارِ ریشهٔ *kreu-. نورایی آن‌ها را crystacus و cros آورده است؛ crystacus در هیچ \"\n \"آوانگاری واژهٔ یونانی نیست و خطای چاپی به‌جای crystallus است. تصویر صفحهٔ چاپی (صـ ۲۴۶ کتاب) بررسی شد: \"\n \"خودِ کتاب همین صورت را چاپ کرده، پس خطای کتاب است نه خطای خوانش اسکن. خودِ اشتقاق درست است (کلاین صـ ۳۸۰).\",\n [\"https://www.etymonline.com/word/crystal\"],\n [{\"ref\": \"KLN:252,380\", \"status\": \"supports\",\n   \"note\": \"KLN p.380 (page marker '380' printed in KLN_1966.txt just above the entry, line ~9830): \\\"crystal, n. — ME. cristal, fr. OF. cristal (F. cristal), fr. L. crystallum, fr. Gk. krystallos, 'ice; crystal', which is rel. to krystainein, 'to congeal, freeze'. Both these words derive fr. kryos (for *krysos), 'frost', which is cogn. with L. crusta.\\\" KLN p.252 (Caucasian) refers the reader to 'crust, crystal' for derivatives of *qrus-.\"}],\n [{\"src\": \"POK\", \"where\": \"Bd. I p.622\", \"stance\": \"supports\",\n   \"note\": \"POK_02.txt leaf 282: \\\"gr. κρύος 'Frost' (= *κρυσος?), κρυσταίνω 'mache gefrieren', κρύσταλλος 'Eis; Kristall', κρυμός 'Frost'\\\" — the correct forms.\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kreus-\", \"stance\": \"supports\",\n   \"note\": \"\\\"1. Suffixed zero-grade form *krus-to- in ... b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-.\\\"\"},\n  {\"src\": \"IEC\", \"where\": \"Mann p.562 s.v. krūsos\", \"stance\": \"supports\",\n   \"note\": \"\\\"Gk. krūos, n. 'chill, frost, ice'; krus-taino, v. tr. 'freeze'\\\".\"}],\n error_in=\"book\", book_prints=\"cros : frost / crystacus : ice\",\n correct_form=\"Gk. κρύος krýos 'frost' ; κρύσταλλος krýstallos 'ice, crystal'\")\n\n# ---------------- node 7 ----------------\nnode(7, \"Latin\", \"crystallum\", \"confirmed\",\n \"Latin crystallum (also crystallus) 'rock-crystal, ice' is a straight borrowing of Greek κρύσταλλος in the classical \"\n \"period (Pliny, Seneca), Greek -ος → Latin -um/-us. Klein p.380: \\\"fr. L. crystallum, fr. Gk. krystallos, 'ice; crystal'\\\". \"\n \"The box's gloss 'ice, gloss' is odd — the printed page really does read 'gloss' (checked on the page image), which looks \"\n \"like Nourai's slip for 'glass' or for the adjectival sense 'glossy, transparent'; the primary Latin senses are 'ice' and \"\n \"'rock crystal'. The arrow Greek → Latin is correct.\",\n \"لاتینی crystallum وام‌واژهٔ مستقیم از یونانی κρύσταλλος است که در دورهٔ کلاسیک (پلینیوس، سنکا) وارد لاتین \"\n \"شده و پایانهٔ -ος به -um/-us بدل شده است. معنیِ داده‌شده در کتاب «ice, gloss» است که به‌گمان لغزش قلم \"\n \"به‌جای glass است. پیوند یونانی–لاتینی درست است.\",\n [\"https://www.etymonline.com/word/crystal\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own (refs=None); the chain is covered by KLN:380 cited on the parent and child nodes.\"}],\n [{\"src\": \"KLN\", \"where\": \"p.380 s.v. crystal\", \"stance\": \"supports\",\n   \"note\": \"\\\"fr. L. crystallum, fr. Gk. krystallos, 'ice; crystal'\\\" (KLN_1966.txt line ~9832).\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet (grep 'crystallum')\", \"stance\": \"silent\",\n   \"note\": \"grep of LAT.txt for 'crystallum'/'crystallus' returns nothing — the Greek loanword has no entry in this OCR.\"},\n  {\"src\": \"WEB-Etymonline\", \"where\": \"crystal\", \"stance\": \"supports\",\n   \"note\": \"\\\"from Latin crystallus 'crystal, ice,' from Greek krystallos, from kryos 'frost,' from PIE root *kreus-\\\".\"}])\n\n# ---------------- node 8 ----------------\nnode(8, \"French\", \"crystal\", \"plausible\",\n \"The French word is cristal (Old French cristal, 12th c.), taken from Latin crystallum with the learned Latin -y- \"\n \"restored only in some English and older French spellings; modern French spells it cristal, never 'crystal'. So the node \"\n \"is real and its parent is right, but the form printed is the English, not the French, spelling. Klein p.380 explicitly: \"\n \"\\\"ME. cristal, fr. OF. cristal (F. cristal), fr. L. crystallum\\\".\",\n \"صورت فرانسوی این واژه cristal است (فرانسوی کهن cristal، سدهٔ دوازدهم) و نه crystal؛ نگارش با y نگارشی \"\n \"انگلیسی/عالمانه است. پس خودِ گره و پدرِ آن (لاتینی) درست است ولی صورتِ چاپ‌شده فرانسوی نیست؛ \"\n \"با احتیاط پذیرفتنی است.\",\n [\"https://www.etymonline.com/word/crystal\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"refs=None on this node.\"}],\n [{\"src\": \"KLN\", \"where\": \"p.380 s.v. crystal\", \"stance\": \"partial\",\n   \"note\": \"\\\"ME. cristal, fr. OF. cristal (F. cristal), fr. L. crystallum\\\" — the French form is cristal.\"},\n  {\"src\": \"WEB-Etymonline\", \"where\": \"crystal\", \"stance\": \"partial\",\n   \"note\": \"\\\"from Old French cristal (12c., Modern French crystal)\\\" — Etymonline's parenthesis is itself a slip; standard modern French is cristal.\"}])\n\n# ---------------- node 9 ----------------\nnode(9, \"Persian\", \"krîstâl\", \"confirmed\",\n \"Persian کریستال kristāl 'crystal, cut glass' is a 19th-20th c. European loan taken through French cristal \"\n \"(Persian technical and luxury-goods vocabulary of the Qajar and Pahlavi periods was overwhelmingly French-mediated: \"\n \"ماژور، آباژور، کریستال). The stressed final -āl and the -ی- for French -i- reflect the French pronunciation \"\n \"[kʁistal] rather than English [ˈkrɪstəl], which would have given *کریستِل. Mo'in's lexicon uses کریستال as an \"\n \"ordinary word in mineralogical definitions (MON_part1.txt lines 22747, 22852), confirming it is naturalised Persian.\",\n \"«کریستال» وام‌واژه‌ای اروپایی است که در دورهٔ قاجار و پهلوی از راه فرانسوی cristal وارد فارسی شده \"\n \"است؛ آوای پایانیِ -آل و امالهٔ «ی» تلفظ فرانسوی را بازمی‌تاباند (از انگلیسی می‌بایست *کریستِل می‌شد). \"\n \"معین خود این واژه را در تعریف‌های کانی‌شناسی به‌کار برده است. ادعای نورایی درست است.\",\n [\"https://www.etymonline.com/word/crystal\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"refs=None on this node.\"}],\n [{\"src\": \"MON\", \"where\": \"MON_part1.txt lines 22747, 22852\", \"stance\": \"supports\",\n   \"note\": \"Mo'in uses کریستال in running definitions (\\\"کریستال‌هایی است که بی‌رنگ که طعمش ...\\\"), i.e. it is current Persian; no headword etymology in the OCR available.\"},\n  {\"src\": \"ARY\", \"where\": \"grep کریستال in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\",\n   \"note\": \"no hit — Aryanpur's IE-root dictionary does not treat modern European loans.\"}])\n\n# ---------------- node 10 ----------------\nnode(10, \"English\", \"crystal\", \"confirmed\",\n \"English crystal descends exactly as the chart draws it, through French: OE cristal / ME cristal was taken from Old French \"\n \"cristal (12th c.) < Latin crystallum < Greek krystallos; the modern spelling with -y- is a Renaissance re-latinisation. \"\n \"Klein p.380: \\\"crystal, n. — ME. cristal, fr. OF. cristal (F. cristal), fr. L. crystallum, fr. Gk. krystallos\\\".\",\n \"انگلیسی crystal دقیقاً همین مسیر را پیموده است: انگلیسی میانه cristal از فرانسوی کهن cristal، آن از \"\n \"لاتینی crystallum و آن از یونانی krystallos. نگارش امروزی با y حاصل لاتینی‌کردنِ دوبارهٔ دورهٔ \"\n \"رنسانس است. کلاین صـ ۳۸۰ همین را می‌گوید؛ ادعای نورایی درست است.\",\n [\"https://www.etymonline.com/word/crystal\"],\n [{\"ref\": \"KLN:380\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt line ~9832 (printed page marker '380' immediately above): \\\"crystal, n. — ME. cristal, fr. OF. cristal (F. cristal), fr. L. crystallum, fr. Gk. krystallos, 'ice; crystal'\\\".\"}],\n [{\"src\": \"KLN\", \"where\": \"p.380\", \"stance\": \"supports\", \"note\": \"as quoted.\"},\n  {\"src\": \"WEB-Etymonline\", \"where\": \"crystal\", \"stance\": \"supports\",\n   \"note\": \"\\\"Old English cristal 'clear ice; clear, transparent mineral,' from Old French cristal (12c.) ... from Latin crystallus\\\".\"},\n  {\"src\": \"SKT\", \"where\": \"Skeat concise (grep 'crystal')\", \"stance\": \"silent\",\n   \"note\": \"no crystal entry retrievable in SKT.txt — the OCR of this concise edition is defective at that point.\"}])\n\n# ---------------- node 11 ----------------\nnode(11, \"English\", \"cryogenic\", \"confirmed\",\n \"cryogenic (first used in the physics of low temperatures c. 1896-1900, on the model of the French/German cryogène of \"\n \"Kamerlingh Onnes' era) is a modern scientific compound of Greek κρύος krýos 'icy cold, frost' + -genes 'producing' + \"\n \"-ic — exactly the node-6 word, so the arrow from that Greek box is correct. Watkins files CRYO- under kreus-, \"\n \"\\\"*krus-es- in Greek kruos, icy cold, frost\\\".\",\n \"واژهٔ علمی cryogenic (از حدود ۱۹۰۰ میلادی در فیزیک دمای بسیار پایین) ساختهٔ نوی از یونانی κρύος \"\n \"«سرما، یخ» به‌علاوهٔ -genēs «پدیدآورنده» است؛ پس پیکانی که آن را از همان جعبهٔ یونانی می‌گیرد \"\n \"درست است. واتکینز نیز CRYO- را ذیل kreus- می‌آورد.\",\n [\"https://www.etymonline.com/word/crystal\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"refs=None on this node.\"}],\n [{\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kreus-\", \"stance\": \"supports\",\n   \"note\": \"\\\"2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-\\\"; the index (line 1401) lists \\\"cRYO- kreus-\\\".\"},\n  {\"src\": \"KLN\", \"where\": \"p.380 s.v. crystal\", \"stance\": \"supports\",\n   \"note\": \"Klein's cross-references at the end of the crystal entry: \\\"Cp. also crymodynia, cryogen, cryolite\\\" — the cryo- family belongs with kryos.\"}])\n\n# ---------------- node 12 ----------------\nnode(12, \"Avestan\", \"xrŭ, xrŭm; xrŭra; xrŭma, xrŭta, xrus; xrŭždra\", \"transcription_suspect\",\n \"All five Avestan forms are genuine and correctly glossed except the last. Bartholomae, AirWb. col. 539: \\\"xrū- f. \"\n \"'blutiges, rohes Fleisch': musti.masaŋhəm xrūm 'ein faustgrosses Stück Fleisch' Yt.14.33\\\" (= 'bloody flesh', with the \"\n \"accusative xrūm); \\\"xrūra- Adj. 1) 'blutig, grausig' 2) 'blutdürstig, grausam'\\\" (= 'bloody, cruel'); \\\"xrūta- Adj. \"\n \"'grausig, grausam'\\\" and Pokorny 621 \\\"xrūma- 'grauenhaft, grausig'\\\" (= 'dreadful'); Mann p.562 has \\\"Av. xrūs \"\n \"'terrible'\\\", the source of Nourai's 'xrus'. But xrūždra- does NOT mean 'heart': Bartholomae has \\\"xruždra- Adj. 'hart' \"\n \"(vom Holz)\\\" and Pokorny 621 \\\"av. xrūždra- 'hart'\\\" — German hart = English HARD. Nourai worked from these German \"\n \"sources and read 'hart' as 'heart'. I checked the printed page (pdf p.276, PNG at data/verification/sources/refs/ocr/\"\n \"BOOK/276.png): the book prints \\\"xrūždra : heart\\\", so the extraction is faithful and the mistake is the author's. \"\n \"(Cf. also Av. xrūždišma- n. 'harter Erdboden' — 'hard ground' — which is the semantic bridge to nodes 13 and 14.) \"\n \"The descent of all these from *kreu- is uncontested.\",\n \"همهٔ صورت‌های اوستایی این جعبه اصیل و درست‌معنایند جز آخری. بارتولومه (فرهنگ ایرانی باستان، \"\n \"ستون ۵۳۹) می‌آورد: xrū- «گوشت خام و خونین»، xrūra- «خونین، بی‌رحم»، xrūta- «هولناک». اما xrūždra- به معنی \"\n \"«دل/قلب» نیست؛ بارتولومه و پوکورنی هر دو آن را به آلمانی hart یعنی «سخت» معنی کرده‌اند. نورایی این \"\n \"hart آلمانی را heart انگلیسی خوانده است. تصویر صفحهٔ چاپی بررسی شد: خطا از خود کتاب است نه از \"\n \"خوانش اسکن. وابستگی این صورت‌ها به ریشهٔ *kreu- مورد اختلاف نیست.\",\n [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krewh%E2%82%82-\"],\n [{\"ref\": \"POK:621\", \"status\": \"supports\",\n   \"note\": \"POK_02.txt leaf 282 (p.621): \\\"av. xrūra- 'blutig, grausig, grausam' ... av. xrū- f., xrūm (= xruvəm) Akk. 'Stück blutiges Fleisch', xrvant- (d.i. xrūvant-) 'grauenhaft, grausig', ... xrūta- 'grausig, grausam', xrūnya- n. 'Bluttat', xrūma- 'grauenhaft, grausig'; mit einer Bedeutung '*geronnen' = 'dick, hart' ... av. xrūždra- 'hart'\\\" — supports every form, and contradicts the gloss 'heart'.\"},\n  {\"ref\": \"KLN:377\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt line 9777, p.377 s.v. crude: \\\"... whence also OI. kravih, 'raw flesh', kravyam, 'blood', kruradh, 'raw, bloody, cruel', Avestic xrum (acc.), 'a piece of bloody flesh', xrura-, 'bloody, cruel'\\\" — exactly the first two lines of Nourai's box.\"}],\n [{\"src\": \"BRT\", \"where\": \"AirWb. col. 539 (BRT.txt lines 10651-10676)\", \"stance\": \"partial\",\n   \"note\": \"\\\"xrū- f. 'blutiges, rohes Fleisch': musti.masaŋhəm xrūm ... Yt.14.33\\\"; \\\"xrūta- Adj. 'grausig, grausam'\\\"; \\\"xrūra- Adj. 1) 'blutig, grausig' 2) 'blutdürstig, grausam'\\\"; \\\"xruždra- Adj. 'hart' (vom Holz)\\\"; \\\"xrūždišma- n. 'harter Erdboden'\\\" — supports all forms but contradicts 'heart' for xrūždra-.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann p.562 s.vv. krūsos, krusd-\", \"stance\": \"supports\",\n   \"note\": \"\\\"Av. xrūs 'terrible'\\\" (s.v. krūsos) is the source of Nourai's 'xrus'; and s.v. krusd-: \\\"Av. xružda, v. 1sg. 'grow hard'\\\" — again 'hard', not 'heart'.\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cruor\", \"stance\": \"supports\",\n   \"note\": \"LAT.txt line ~14798: \\\"av. xru- 'chair saignante'\\\".\"}],\n error_in=\"book\", book_prints=\"xrūždra : heart\",\n correct_form=\"Av. xrūždra- 'hard' (Bartholomae/Pokorny German 'hart')\")\n\n# ---------------- node 13 ----------------\nnode(13, \"Persian\", \"kolŭx\", \"plausible\",\n \"Persian کلوخ kolūx 'a dried clod of earth', with Sa'di's line چو کردی با کلوخ انداز پیکار. Nourai's source is Mann, \"\n \"who lists it under exactly this root: IEC p.562 \\\"krūsos, ā 'hard, solid, frozen; frost, ice' ... Av. xrūs 'terrible'; \"\n \"Per. kulūx 'clod, sod'\\\". The semantic pattern is well attested for the *krus- group (OE hrūse 'earth, ground', Latvian \"\n \"kruvesis 'mud frozen in the field', Pokorny's German gloss 'Erdscholle' = clod, and Av. xrūždišma- 'hard ground'), so a \"\n \"New Persian kolūx < Old Iranian *xru-ša-/*krū-s- 'hardened lump' is phonetically unobjectionable (Ir. xr- > NP kVr- with \"\n \"anaptyctic vowel, as in xratu- > خرد). But no Iranian handbook I could reach states it: Horn and Hübschmann have no \"\n \"entry, Mo'in and Borhan-e Qate' give only the meaning without an origin, and the popular Persian analysis is a native \"\n \"compound کل/کلـ 'dry' + لاخ/-وخ 'piece'. So: compatible but not independently established.\",\n \"«کلوخ» در فارسی نو به معنی گِلِ خشک‌شده و به‌هم‌چسبیده است. مان (فرهنگ تطبیقی هندواروپایی، صـ ۵۶۲) آن را \"\n \"ذیل *krūsos «سخت، منجمد» می‌آورد و همین مأخذ نورایی است. این تحول معنایی (یخ‌زده/سخت ← کلوخ) در همین \"\n \"خانواده نمونه دارد (انگلیسی کهن hrūse «زمین»، اوستایی xrūždišma- «زمین سخت») و از نظر آوایی هم مانعی \"\n \"ندارد؛ اما هرن، هوبشمان، معین و برهان قاطع ریشه‌ای برای آن نمی‌دهند و تحلیل رایج عامیانه آن را \"\n \"«کل (خشک) + لاخ» می‌داند. پس با احتیاط پذیرفتنی است.\",\n [\"https://abadis.ir/fatofa/%DA%A9%D9%84%D9%88%D8%AE/\"],\n [{\"ref\": \"IEC:562\", \"status\": \"supports\",\n   \"note\": \"IEC.txt leaf 320 (printed p.562), s.v. krūsos: \\\"Av. xrūs 'terrible'; Per. kulūx 'clod, sod'\\\" — precisely Nourai's claim, on precisely the page cited.\"},\n  {\"ref\": \"MON:3040\", \"status\": \"partial\",\n   \"note\": \"The 6-vol. Amir Kabir pagination Nourai cites is not the pagination of the local 2-vol. OCR, so p.3040 could not be checked directly; the entry itself is in MON_part2.txt line 25494: \\\"کلوخ: ... گل خشک شده. لخت‌های دیوار افتاده و خاک بر هم چسبیدهٔ سخت شده. خشت پاره\\\" — supports the gloss, gives no etymology.\"}],\n [{\"src\": \"IEC\", \"where\": \"Mann p.562\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check.\"},\n  {\"src\": \"MON\", \"where\": \"MON_part2.txt line 25494\", \"stance\": \"partial\",\n   \"note\": \"\\\"کلوخ: ... گل خشک شده ... خاک بر هم چسبیدهٔ سخت شده\\\" — meaning only, no origin tag.\"},\n  {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' vol. 3, pdf page 476 (incoming/BQT/BQT_v3_pages.txt line 34917 ff.)\", \"stance\": \"partial\",\n   \"note\": \"\\\"[کلوخ] ... شده - و لختهای [دیوار] افتاده و خاک برهم چسبیده سخت شده باشد ... و خشت پاره خام و پخته را نیز گویند\\\" — Mo'in adds no etymological footnote to this headword.\"},\n  {\"src\": \"HRN\", \"where\": \"grep 'kul.x' in HRN.txt\", \"stance\": \"silent\", \"note\": \"no entry for kolūx in Horn's Grundriss.\"},\n  {\"src\": \"HUB\", \"where\": \"grep 'kul.x' in HUB.txt\", \"stance\": \"silent\", \"note\": \"no entry in Hübschmann's Persische Studien.\"},\n  {\"src\": \"ARY\", \"where\": \"grep کلوخ in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no hit.\"}])\n\n# ---------------- node 14 ----------------\nnode(14, \"Sogdian\", \"xrwm\", \"confirmed\",\n \"Sogdian ᵝxrwmᵞ / xurum 'earth, soil' — Gharib's Sogdian Dictionary, entry 10633 (printed p. 432/433): \\\"10633 xrwm M ... \"\n \"xurum ⊙Av. xruma ... earth, soil. GMS 415, 482; Gersh. JRAS 1942, 101; AHM 189\\\". Gharib herself compares the Avestan \"\n \"form, so the parent as drawn (the same *kreu-/*krus- family) is what the standard Sogdian dictionary assumes. The \"\n \"semantics are the 'hardened crust > clod > ground' branch of the root, matching OE hrūse 'earth, ground' (Klein s.v. \"\n \"crust; Mann s.v. krūsos) and Av. xrūždišma- 'hard ground' (Bartholomae). Attested in the Manichaean Sogdian corpus \"\n \"(the 'M' siglum).\",\n \"سغدی xrwm (خوانش xurum) «زمین، خاک»؛ بدرالزمان قریب در فرهنگ سغدی (مدخل ۱۰۶۳۳، صـ ۴۳۲/۴۳۳) آن را با \"\n \"اوستایی xruma مقایسه کرده است. تحول معنایی «پوستهٔ سخت ← کلوخ ← خاک، زمین» در همین ریشه نمونه‌های \"\n \"دیگر دارد (انگلیسی کهن hrūse «زمین»، اوستایی xrūždišma- «زمین سخت»). ادعای نورایی درست است.\",\n [],\n [{\"ref\": \"SOD:432\", \"status\": \"supports\",\n   \"note\": \"SOD.txt line 80026 / SOD_pages.txt line 34521, entry 10633 (form-feed leaf 499 ≈ printed p.433, i.e. the page Nourai cites within the ±1 tolerance of this scan's offset): \\\"10633 xrwm M / xurum ⊙Av. xruma ... earth, soil / GMS 415, 482; Gersh. JRAS 1942, 101; AHM 189\\\".\"}],\n [{\"src\": \"SOD\", \"where\": \"Gharib entry 10633, p.432/433\", \"stance\": \"supports\", \"note\": \"as quoted in ref_check; Gharib's own cross-reference is to Avestan xruma.\"},\n  {\"src\": \"BRT\", \"where\": \"AirWb. col. 539 s.v. xrūždišma-\", \"stance\": \"supports\",\n   \"note\": \"\\\"xrūždišma- n. 1) 'harter Erdboden' ... 2) 'Stück harter Erde'\\\" — the 'hard earth/clod' sense is already Avestan, which makes the Sogdian 'earth, soil' unremarkable.\"},\n  {\"src\": \"IEC\", \"where\": \"Mann p.562 s.v. krūsos\", \"stance\": \"supports\",\n   \"note\": \"\\\"Long-gde in OE hrūse, f. 'earth, ground'\\\" — the same semantic development in Germanic.\"}])\n\n# ---------------- node 15 ----------------\nnode(15, \"Greek\", \"kreas; pan-kreas\", \"confirmed\",\n \"Greek κρέας kréas 'flesh, meat' is the direct s-stem continuation of the root, PIE *krewh₂-s- > *kréwas > Attic \"\n \"κρέας (pl. κρέα < *κρέϜα, with loss of intervocalic digamma), the exact cognate of Sanskrit kraviṣ- and Avestan \"\n \"xrū-. πάγκρεας pánkreas 'sweetbread, pancreas' is a compound of πᾶν 'all' + κρέας, i.e. 'all flesh', coined in \"\n \"the Hellenistic medical tradition (Herophilus of Chalcedon, 3rd c. BCE, then Rufus of Ephesus and Galen) because the \"\n \"gland looks like undifferentiated flesh with no cartilage or fat. Both are on the chart correctly, and Nourai's AHD \"\n \"reference is right.\",\n \"یونانی κρέας (kréas) «گوشت» ادامهٔ مستقیم ستاک s-دار ریشه است: *krewh₂-s- < *kréwas، و هم‌ریشهٔ دقیق \"\n \"سنسکریت kraviṣ- و اوستایی xrū-. πάγκρεας مرکّب از πᾶν «همه» و κρέας است یعنی «همه‌گوشت»، ساختهٔ \"\n \"پزشکان یونانی (هروفیلوس، سدهٔ سوم پیش از میلاد) از آن رو که لوزالمعده همه گوشت می‌نماید. ادعای \"\n \"نورایی درست است.\",\n [\"https://www.etymonline.com/word/pancreas\",\n  \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/krewh%E2%82%82-\"],\n [{\"ref\": \"AHD\", \"status\": \"supports\",\n   \"note\": \"AHD_watkins1985.txt line 645 s.v. kreue-1 'Raw flesh': \\\"2. Suffixed form *krewo-s- in Greek kreas, flesh: CREATINE, CREODONT, CREOSOTE, PANCREAS\\\"; index line 2049: \\\"PANCREAS kreue-1, pant-\\\".\"}],\n [{\"src\": \"POK\", \"where\": \"Bd. I p.621\", \"stance\": \"supports\",\n   \"note\": \"POK_02.txt leaf 282: \\\"gr. κρέας n. 'Fleisch' (*kreųās)\\\", listed beside \\\"Ai. kravis- n. 'rohes Fleisch' (= gr. κρέας)\\\".\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cruor\", \"stance\": \"supports\",\n   \"note\": \"\\\"La forme initiale est un nom radical qui est conservé dans att. κρέα 'viande' (valeur collective) de *κρεϜa, av. xru- 'chair saignante'\\\".\"},\n  {\"src\": \"IEC\", \"where\": \"Mann (grep kreuos/kreas)\", \"stance\": \"partial\",\n   \"note\": \"Mann cross-refers \\\"Cf. kruu- (2) and kreuos\\\" s.v. krouu- (leaf 319, p.559-560); the Greek word belongs to his *kreuos 'blood, flesh' entry.\"}])\n\n# ---------------- node 16 ----------------\nnode(16, \"French\", \"pancreas\", \"confirmed\",\n \"French pancréas (attested from 1541 in Canappe's translations of Galen) is a learned borrowing straight from the Greek \"\n \"medical term πάγκρεας, taken over through the Renaissance Latin form pancreas; French added only the acute accent. \"\n \"The Greek → French arrow is right; the Latin stage is passed over silently by the chart.\",\n \"فرانسوی pancréas (از ۱۵۴۱ میلادی در ترجمهٔ آثار جالینوس) وام‌واژه‌ای عالمانه از اصطلاح پزشکی \"\n \"یونانی πάγκρεας است که از راه لاتینی دورهٔ رنسانس گرفته شده است. پیوند یونانی–فرانسوی درست است.\",\n [\"https://www.etymonline.com/word/pancreas\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"refs=None on this node.\"}],\n [{\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"supports\",\n   \"note\": \"\\\"PANCREAS kreue-1, pant-\\\" — the word is the Greek compound however it reached the modern languages.\"},\n  {\"src\": \"WEB-Etymonline\", \"where\": \"pancreas\", \"stance\": \"supports\",\n   \"note\": \"\\\"from Greek pankreas, literally 'entirely flesh', from pan- 'all' + kreas 'flesh' ... from PIE root *kreue- 'raw flesh'\\\"; English use from 1570s, i.e. contemporaneous with the French.\"}])\n\n# ---------------- node 17 ----------------\nnode(17, \"Persian\", \"pânkrâs\", \"plausible\",\n \"Persian پانکراس pānkrās 'pancreas' is a 20th-c. medical loan. The chart's route (French → Persian) is the likely one, \"\n \"since modern Persian medical terminology was formed on French models (the Dar al-Fonun tradition, and the French-based \"\n \"anatomical nomenclature of the Tehran medical faculty); the long ā in the second syllable reflects French [pɑ̃kʁeas] \"\n \"rather than English [ˈpæŋkriəs]. The word is however marginal in Persian (the usual term is لوزالمعده), and Nourai's \"\n \"only reference for it, VOP (Moshiri, Farhang-e Vāžehā-ye Orūpāyi dar Fārsi), is not obtainable, so the specific claim \"\n \"cannot be checked against a source.\",\n \"«پانکراس» وام‌واژه‌ای پزشکی از سدهٔ بیستم است. مسیری که نمودار می‌دهد (فرانسوی ← فارسی) محتمل‌ترین \"\n \"است، زیرا اصطلاحات پزشکی فارسی از راه فرانسه وارد شده‌اند؛ آلف کشیدهٔ هجای دوم نیز تلفظ فرانسوی \"\n \"را نشان می‌دهد. اما مأخذ نورایی (VOP از مهشید مشیری) در دسترس نیست، پس با احتیاط پذیرفتنی است.\",\n [],\n [{\"ref\": \"VOP:108\", \"status\": \"not_checked\",\n   \"note\": \"refs_online.json entry VOP: \\\"Searched archive.org, ketabnak, noorlib, web: not found ... Purchase second-hand only\\\" — Moshiri's dictionary of European loanwords in Persian has no accessible copy.\"}],\n [{\"src\": \"MON\", \"where\": \"grep پانکراس in MON_part1/part2\", \"stance\": \"silent\",\n   \"note\": \"no hit — Mo'in's lexicon does not carry the loanword (Persian normally uses لوزالمعده).\"},\n  {\"src\": \"ARY\", \"where\": \"grep پانکراس in incoming/ARY/ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"no hit.\"},\n  {\"src\": \"WEB-Etymonline\", \"where\": \"pancreas\", \"stance\": \"partial\",\n   \"note\": \"Confirms the European word's shape and meaning but says nothing about its Persian transmission.\"}])\n\n# ---------------- node 18 ----------------\nnode(18, \"English\", \"pancreas\", \"confirmed\",\n \"English pancreas is first attested in the 1570s, borrowed directly from the Greek medical term (through Modern Latin \"\n \"pancreas) in the anatomical writing of the period; Etymonline: \\\"from Greek pankreas, literally 'entirely flesh', from \"\n \"pan- 'all' + kreas 'flesh'\\\", with Watkins filing PANCREAS under kreuə-1 and pant-. The chart's direct Greek → English \"\n \"arrow is therefore accurate (the intermediary is Neo-Latin, not French).\",\n \"واژهٔ انگلیسی pancreas از دههٔ ۱۵۷۰ میلادی مستقیماً از اصطلاح یونانی (از راه لاتینی نو) وارد شده است: \"\n \"πᾶν «همه» + κρέας «گوشت». پیکان مستقیم یونانی–انگلیسی در نمودار درست است.\",\n [\"https://www.etymonline.com/word/pancreas\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"refs=None on this node; covered by the AHD reference on the parent.\"}],\n [{\"src\": \"AHD\", \"where\": \"Watkins 1985, index and s.v. kreue-1\", \"stance\": \"supports\",\n   \"note\": \"\\\"2. Suffixed form *krewo-s- in Greek kreas, flesh: ... PANCREAS\\\"; index \\\"PANCREAS kreue-1, pant-\\\".\"},\n  {\"src\": \"WEB-Etymonline\", \"where\": \"pancreas\", \"stance\": \"supports\",\n   \"note\": \"\\\"from Greek pankreas, literally 'entirely flesh' ... 1570s ... likely referring to 'the homogeneous substance of the organ'\\\".\"}])\n\n# ---------------- node 19 ----------------\nnode(19, \"Latin\", \"crusta; crŭdus\", \"confirmed\",\n \"Both Latin words are textbook members of the root and Nourai's glosses reproduce his source almost word for word. \"\n \"crusta 'rind, crust, shell' < *krus-ta, i.e. the zero grade of the s-extension + -to-; Klein p.378 s.v. crust: \\\"L. \"\n \"crusta, 'the hard surface of a body, rind, crust, shell', which stands for *crus-ta, and lit. means 'that which has been \"\n \"hardened by freezing'\\\" — exactly the chart's gloss 'hardened by freezing'. crūdus 'raw, bloody' < *krū-do- (Pokorny \"\n \"621; Watkins *krū-do- < *krua-do-), the same formation as crūdēlis 'cruel'; Ernout-Meillet stress that the original \"\n \"sense is 'saignant, sanglant' ('bleeding, bloody') and that 'raw, uncooked' is secondary, opposed to coctus — which is \"\n \"precisely Nourai's order of glosses 'bloody, raw'. Osco-Umbrian krustatar 'crusta tegitor' shows the noun is Italic, not \"\n \"a Greek loan.\",\n \"هر دو واژهٔ لاتینی اعضای شناختهٔ این ریشه‌اند: crusta از *krus-ta (درجهٔ صفرِ گسترش s-دار به‌علاوهٔ \"\n \"پسوند -to-) و معنی نخستینِ آن «آنچه از یخ‌زدگی سخت شده» است (کلاین صـ ۳۷۸)؛ crūdus از *krū-do- که \"\n \"معنی اصلیِ آن در ارنو–مییه «خونین، خون‌ریز» است و «خام، ناپخته» معنی ثانوی است — دقیقاً همان \"\n \"ترتیبی که نورایی آورده است. ادعای نورایی درست است.\",\n [\"https://www.etymonline.com/word/crust\", \"https://www.etymonline.com/word/crude\"],\n [{\"ref\": \"KLN:378\", \"status\": \"supports\",\n   \"note\": \"KLN_1966.txt line 9800, p.378 s.v. crust: \\\"L. crusta ... stands for *crus-ta, and lit. means 'that which has been hardened by freezing' ... All these words derive fr. I.-E. *qreus-, *qrus-, *qruwes-, enlarged forms of base *qreu-, 'icy, solid, coagulated, congealed', whence also L. crudus, 'raw'. See crude\\\" — both words, both glosses, and the root string of Nourai's root box.\"}],\n [{\"src\": \"POK\", \"where\": \"Bd. I p.621\", \"stance\": \"supports\",\n   \"note\": \"POK_02.txt leaf 282: \\\"osk. krustatar 'crusta tegitor' (Denom. von *krus-ta), lat. crusta 'Kruste, Rinde, Schorf', ursprüngl. 'das fest gewordene Blut auf einer Wunde' (*krūs-ta), crūdus 'roh, rauh, hart' (*krū-do-), crūdēlis 'grausam, herzlos'\\\".\"},\n  {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.vv. kreus-, kreue-1\", \"stance\": \"supports\",\n   \"note\": \"\\\"*krus-to- in a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN...\\\"; \\\"*kru-do- in a. Latin crudus, bloody, raw: CRUDE; ECRU, RECRUDESCE; b. Latin crudelis, cruel: CRUEL\\\".\"},\n  {\"src\": \"LAT\", \"where\": \"Ernout-Meillet s.v. cruor / crudus (LAT.txt lines 14753-14795)\", \"stance\": \"supports\",\n   \"note\": \"\\\"crudus, -a, -um ... adj. qui marque à la fois l'état 'saignant, sanglant' ... Sur le sens de 'saignant' s'est greffé celui de 'cru, non cuit' et crudus s'est opposé à coctus\\\".\"},\n  {\"src\": \"LEW\", \"where\": \"Walde-Hofmann I 295-96 (cited by Klein)\", \"stance\": \"silent\",\n   \"note\": \"grep of LEW_1910.txt for 'crusta'/'crudus' returns nothing — the C-section of this 1910 OCR is not searchable; Klein's citation of WH I 295-96 could not be read directly.\"}])\n\n# ---------------- node 20 ----------------\nnode(20, \"English\", \"crust; crude\", \"confirmed\",\n \"crust: Middle English cruste/crouste, borrowed c.1300 from Old French crouste (Modern French croûte) < Latin crusta; \"\n \"the sense narrowed in English to the hard outer part of a loaf before generalising again. crude: taken directly from \"\n \"Latin crudus in the late 14th c. as a learned word (first of undigested food and untanned hides, 'lacking grace, socially \"\n \"unrefined' by the 1640s, 'crude oil' 1865). Both derive from node 19 as drawn, though crust came through Old French while \"\n \"crude is a direct Latinism.\",\n \"crust از انگلیسی میانه crouste، وام‌گرفته از فرانسوی کهن crouste و آن از لاتینی crusta؛ crude در \"\n \"اواخر سدهٔ چهاردهم میلادی مستقیماً از لاتینی crudus به‌عنوان واژه‌ای عالمانه گرفته شده است. \"\n \"هر دو از همان گرهِ لاتینی می‌آیند؛ ادعای نورایی درست است.\",\n [\"https://www.etymonline.com/word/crust\", \"https://www.etymonline.com/word/crude\"],\n [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"refs=None on this node; the parent's KLN:378 covers the chain.\"}],\n [{\"src\": \"KLN\", \"where\": \"pp.377-378 s.vv. crude, crust\", \"stance\": \"supports\",\n   \"note\": \"\\\"crude, adj. ... — L. crudus, 'raw, crude, not cooked', lit. 'trickling with blood, bleeding'\\\" (line 9777); \\\"crust, n. — ME., fr. OF. crouste (F. croûte), fr. L. crusta\\\" (line 9800).\"},\n  {\"src\": \"WEB-Etymonline\", \"where\": \"crust, crude\", \"stance\": \"supports\",\n   \"note\": \"crust: \\\"early 14c., 'hard outer part of bread', from Old French crouste and Latin crusta\\\"; crude: \\\"late 14c., from Latin crudus 'rough; not cooked, raw, bloody'\\\".\"}])\n\nout = {\n \"pdf_page\": 276,\n \"book_page\": 246,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": [entry]\n}\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-276.json','w',encoding='utf-8') as f:\n    json.dump(out, f, ensure_ascii=False, indent=1)\n    f.write(\"\\n\")\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk276.py && python3 -m json.tool data/verification/page-276.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 276",
 "description": "Write and check page-276.json"
}
```


### [2026-09-06T21:32:15.417Z] TOOL RESULT

```
ok 20
JSON OK
nodes verified: 20/20
node verdicts: {'disputed': 2, 'confirmed': 12, 'plausible': 4, 'transcription_suspect': 2}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 2, 'supports': 10, 'not_checked': 10}
books consulted: {'partial': 9, 'silent': 12, 'contradicts': 2, 'supports': 32} | by book: {'KLN': 7, 'WEB-Etymonline': 7, 'AHD': 6, 'POK': 5, 'MON': 5, 'IEC': 5, 'WEB-Wiktionary': 4, 'LAT': 4, 'ARY': 3, 'BQT': 2, 'BRT': 2, 'SKT': 1, 'HRN': 1, 'HUB': 1, 'SOD': 1, 'LEW': 1}
```


## [2026-09-06T21:32:35.164Z] AGENT

Verification of PDF page 276 (book p. 246) complete — `verify_check.py 276` reports **0 PROBLEM lines**, 20/20 nodes.

**Page 276 (root `Kreu, Qreu, Qreus, Qruwes, Qrus`, IE; 2 redirects skipped)**
- Root: **confirmed** (Pokorny 621 §1 kreu- incl. group B kreus-/krus-; root string + gloss copied verbatim from Klein p.378 s.v. *crust*)
- Nodes: confirmed 12 · plausible 4 · disputed 2 · transcription_suspect 2
- Ref checks: 10 supports, 2 partial, 10 not_checked (nodes with `refs=None`, plus MON5:1474 and VOP:108, neither obtainable)

**Disputed**
- #1 Greek `casos ; kau-casos` — no Greek *kasos 'ice'. Pokorny 622 and Klein 252 make Kaukasos a **Scythian** loan *xrohu-kasi-, where the FIRST element is 'ice' and the second (-kasi-, cf. kaiein) is 'shining' — the reverse of Nourai's labels. Wiktionary now calls the whole etymology uncertain (PIE *kewk- 'height', or Iranian).
- #4 Persian `qafqâz` — Wiktionary derives قفقاز from MP *Kaf kōf 'Mount Qāf', not from Latin via Arabic; the q-/metathesis shape is the Arabic one (al-Qawqāz), and Arabic borrowed from Greek/Syriac, never Latin. (Dehkhoda does back the ultimate Scythian *kroy-khasis 'shining ice'.)

**Transcription suspect — both `error_in: "book"` (extraction is faithful; page PNG saved to `data/verification/sources/refs/ocr/BOOK/276.png`)**
- #6 Greek `crystacus : ice` — the book really prints "crystacus"; Nourai's misprint for Gk. κρύσταλλος *krystallos* (`cros` likewise for κρύος *krýos*).
- #12 Avestan `xrŭždra : heart` — book prints "heart", but Bartholomae col. 539 and Pokorny 621 both gloss xrūždra- German **'hart' = HARD**. Nourai misread the German. Correct form: 'hard'.

**Extraction errors for the owner: none.** One cosmetic omission: the printed page has a completely blank, unlabelled box attached to the Avestan node (right of it); the JSON has no node for it — it carries no text, so nothing is lost.

Files written: `data/verification/page-276.json`; 10 web sources archived via `fetch_source.py`; page image at `data/verification/sources/refs/ocr/BOOK/276.png`. Not committed.
