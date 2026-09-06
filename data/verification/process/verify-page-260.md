# Verification process log — verify-page-260


## [2026-09-06T16:20:33.166Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 260 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-260.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-260.json. Write /home/sfmqrb/git/rishe/data/verification/page-260.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 260` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:20:34.670Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T16:20:35.363Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:20:35.380Z] TOOL RESULT

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


## [2026-09-06T16:20:35.686Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-260.txt"
}
```


### [2026-09-06T16:20:35.700Z] TOOL RESULT

```
1	=== PDF page 260 (book page 230) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kerk, Kork, Krk : thin, slender  (refs POK:581)
4	#1 (parent #0) [Avestan] refs=POK:581; BQT:1795; KLN:672 | keresa : thin, little ; keresa-vazda : with "little power" ; keresa-aspa : with "lean horses" ☞Ekwos
5	  #2 (parent #1) [Persian] refs=BQT:1795 | Garsîvaz «گرسیوز» : "with little power", a male name ; Garšâsp «گرشاسپ» : "with lean horses", a male name
6	  #3 (parent #1) [Sogdian] refs=SOD:32,195 | `ks, ks : thin, small, weak
7	#4 (parent #0) [Latin] refs=POK:581; KLN:672 | gracilis : slender
8	  #5 (parent #4) [English] refs=AHD:570 | gracile
9	--- entry 1 ---
10	ROOT Kěros -> redirect to Sper
11	--- entry 2 ---
12	ROOT Kers 1 -> redirect to Ker 4
13	--- entry 3 ---
14	ROOT [Indo-European] Kers 2 : black  (refs OEW:182)
15	#1 (parent #0) [Egyptian] refs=AHD:30; OEW:182 | khem : black ; chem : a native word for Egypt due to its black soil at Nile shores
16	  #2 (parent #1) [Greek] refs=AHD:30; KLN:45 | xěma : black land, the former name of Egypt, the art of transmutation practiced by the Egyptians
17	    #3 (parent #2) [Arabic] refs=AHD | al-kimyâ, al-kîmîya : the art of transmutation | NOTE: OEW:124 & FSD:66 say it is possible this word is derived from Greek "xymeia:infusion" from root "Gheu:to pour".  KLN:45, however, does not agree.
18	      #4 (parent #3) [Persian] refs=BQT:1759 | kîmîyâ «کیمیا» : chemistry, any rare substance
19	      #5 (parent #3) [Latin] refs=AHD | alchymia
20	        #6 (parent #5) [French] refs=None | alchemie, chimie : chemistry
21	          #7 (parent #6) [Persian] refs=MON:2115 | šîmî «شیمی» : chemistry
22	          #8 (parent #6) [English] refs=KLN:45 | chemistry, alchemist
23	#9 (parent #0) [Sanskrit] refs=OEW:182 | Krishna : the black one, title of an Indian God
24	  #10 (parent #9) [English] refs=OEW:182 | Krishna
25	    #11 (parent #10) [Persian] refs=MON5:1572 | Krîšnâ «کریشنا» : an old Indian god
26	--- entry 4 ---
27	ROOT Kertâ -> redirect to Ker 5
28	
```


## [2026-09-06T16:20:39.530Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/extracted/batch/page-260.json'))\nprint(json.dumps(d, ensure_ascii=False, indent=1)[:6000])\n\"",
 "description": "Dump page-260 source JSON"
}
```


## [2026-09-06T16:20:40.053Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:20:41.246Z] TOOL RESULT

```
{
 "pdf_page": 260,
 "book_page": 230,
 "entries": [
  {
   "root": {
    "name": "Kerk, Kork, Krk",
    "lang": "Indo-European",
    "refs": "POK:581",
    "gloss": "thin, slender"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Avestan",
     "refs": "POK:581; BQT:1795; KLN:672",
     "words": [
      {
       "translit": "keresa",
       "gloss": "thin, little",
       "script": null
      },
      {
       "translit": "keresa-vazda",
       "gloss": "with \"little power\"",
       "script": null
      },
      {
       "translit": "keresa-aspa",
       "gloss": "with \"lean horses\"",
       "script": null,
       "see": [
        "Ekwos"
       ]
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
     "refs": "BQT:1795",
     "words": [
      {
       "translit": "Garsîvaz",
       "gloss": "\"with little power\", a male name",
       "script": "گرسیوز"
      },
      {
       "translit": "Garšâsp",
       "gloss": "\"with lean horses\", a male name",
       "script": "گرشاسپ"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 3,
     "parent": 1,
     "lang": "Sogdian",
     "refs": "SOD:32,195",
     "words": [
      {
       "translit": "`ks, ks",
       "gloss": "thin, small, weak",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 4,
     "parent": 0,
     "lang": "Latin",
     "refs": "POK:581; KLN:672",
     "words": [
      {
       "translit": "gracilis",
       "gloss": "slender",
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
     "refs": "AHD:570",
     "words": [
      {
       "translit": "gracile",
       "gloss": null,
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
    "name": "Kěros",
    "redirect": "Sper"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Kers 1",
    "redirect": "Ker 4"
   },
   "nodes": []
  },
  {
   "root": {
    "name": "Kers 2",
    "lang": "Indo-European",
    "refs": "OEW:182",
    "gloss": "black"
   },
   "nodes": [
    {
     "id": 1,
     "parent": 0,
     "lang": "Egyptian",
     "refs": "AHD:30; OEW:182",
     "words": [
      {
       "translit": "khem",
       "gloss": "black",
       "script": null
      },
      {
       "translit": "chem",
       "gloss": "a native word for Egypt due to its black soil at Nile shores",
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
     "lang": "Greek",
     "refs": "AHD:30; KLN:45",
     "words": [
      {
       "translit": "xěma",
       "gloss": "black land, the former name of Egypt, the art of transmutation practiced by the Egyptians",
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
     "lang": "Arabic",
     "refs": "AHD",
     "words": [
      {
       "translit": "al-kimyâ, al-kîmîya",
       "gloss": "the art of transmutation",
       "script": null
      }
     ],
     "script_extra": null,
     "note": "OEW:124 & FSD:66 say it is possible this word is derived from Greek \"xymeia:infusion\" from root \"Gheu:to pour\".  KLN:45, however, does not agree.",
     "quote": null
    },
    {
     "id": 4,
     "parent": 3,
     "lang": "Persian",
     "refs": "BQT:1759",
     "words": [
      {
       "translit": "kîmîyâ",
       "gloss": "chemistry, any rare substance",
       "script": "کیمیا"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": {
      "text": "آنان که در مخالفت پادشاه دین - بردند دستبرد به مکر و به کیمیا",
      "poet": "Sŭzanî"
     }
    },
    {
     "id": 5,
     "parent": 3,
     "lang": "Latin",
     "refs": "AHD",
     "words": [
      {
       "translit": "alchymia",
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
     "parent": 5,
     "lang": "French",
     "refs": null,
     "words": [
      {
       "translit": "alchemie, chimie",
       "gloss": "chemistry",
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
     "lang": "Persian",
     "refs": "MON:2115",
     "words": [
      {
       "translit": "šîmî",
       "gloss": "chemistry",
       "script": "شیمی"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 8,
     "parent": 6,
     "lang": "English",
     "refs": "KLN:45",
     "words": [
      {
       "translit": "chemistry, alchemist",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 9,
     "parent": 0,
     "lang": "Sanskrit",
     "refs": "OEW:182",
     "words": [
      {
       "translit": "Krishna",
       "gloss": "the black one, title of an Indian God",
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 10,
     "parent": 9,
     "lang": "English",
     "refs": "OEW:182",
     "words": [
      {
       "translit": "Krishna",
       "gloss": null,
       "script": null
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
    },
    {
     "id": 11,
     "parent": 10,
     "lang": "Persian",
     "refs": "MON5:1572",
     "words": [
      {
       "translit": "Krîšnâ",
       "gloss": "an old Indian god",
       "script": "کریشنا"
      }
     ],
     "script_extra": null,
     "note": null,
     "quote": null
```


### [2026-09-06T16:20:41.280Z] TOOL RESULT

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


## [2026-09-06T16:20:56.083Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','OEW','AHD','KLN','BQT','MON','SOD','FSD','ARY','WLD','IEC','SYN','SKT','WEB','FVQ','PLA','AFM','LKT','HJB','LEW','LAT']:\n    v=d.get(k)\n    print('==',k, json.dumps(v, ensure_ascii=False)[:600])\n\"",
 "description": "Inspect refs_online entries"
}
```


## [2026-09-06T16:20:57.210Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"gracilis\" POK_full.txt | head -20; echo ---; grep -n \"kers-\" POK_full.txt | head -20",
 "description": "Grep Pokorny for gracilis and kers"
}
```


### [2026-09-06T16:20:58.174Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
== OEW {"title": "J. T. Shipley, The Origins of English Words: A Discursive Dictionary of Indo-European Roots, Baltimore 1984", "edition_found": "1984 (lending-only)", "kind": "archive_restricted", "url": "https://archive.org/details/originsofenglish0000ship ; https://archive.org/details/originsofenglish00jose (both JHU 1984, borrowable) ; HathiTrust mdp.49015002910322 search-only ; Google ELSm5zUgP_wC no view", "identifier": "originsofenglish00jose (also originsofenglish0000ship)", "local_file": null, "page_offset": null, "lookup_hint": "Borrow via IA lending (djvu.txt returns 401/403). Entries are 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id=
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
== HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos
```


### [2026-09-06T16:20:58.222Z] TOOL RESULT

```
45963:Latin cracentes, leg. gracentes^ thin, slight, slender, slim, meagre, lean ' to gracilis^ 
79071:^5^/7e/"-Ar-; Armenian /70/'(goi/" tenuis, gracilis' ("*zusammengeschnurt or eingeschrumpft'); 
---
44868:Note: compare also ker-3ax\(i kers-1. 
46328:Note: often extended with -/and -u, s. the extensions kerb(h)-ax\6 kers- 
46432:Root / lemma: kers- 
50244:extension the color root /re/'- (see S. 583 kers-), MiJhlenbach-Endzelin II 383. 
50433:*kers- because of common Italic lllyrian rs- > rr-). 
50661:Kspvai, K£pva PI. 'transverse processes of the vertebrae' {*kern- or *kers-n); Kpayv^v 
50678:cernuus, cernulus^ turning a somersault, stooping forwards, head-foremost ' ( *kers-nouos,
```


## [2026-09-06T16:21:01.606Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '45930,45990p' POK_full.txt; echo \"=====KERS=====\"; sed -n '46420,46500p' POK_full.txt",
 "description": "Read Pokorny gracilis and kers- entries"
}
```


### [2026-09-06T16:21:01.698Z] TOOL RESULT

```
Old Church Slavic krbpa^ a web, texture, rag', is-krbpiti, -atT patch up, mend ', 
Bulgarian kbrpa^raq, kerchief, cloth; patch ', serb. krpa^ patch, shred, piece of canvas, 



fabric'; with tlie meaning " slice ', serb. Arjb^e'sncwshce', pcln. kierpce' kind cf slice ', 
Czech krpec " bast shce '; 

with full grade the 2. syllable Kpr|TTi(;, -T5cq " man's high beet, half-bcct, scldiers' beets, 
sheeshaped cake, groundwork, foundation, basement of a building or altar, walled edge of 
a river or canal, quay, ox-tongue, Helminthia echioides, a bandage ' (Latin loanword 
creplda ' a sandal, sole with straps, half-shoe, Grecian shoe '). 

There kerap-\s probably an extension from (s)ker(e)-^ cui, clip',. 

References: WP. I 425, WH. I 172, Trautmann 146. 
Page(s): 581 

Root / lemma: [kerR-.) korR- : kfR- 

Meaning: to wrinkle, become thin 

Note: (or at most kark- : krk-) 

Material: Old Indie krsa-^ emaciated, lean, weak', krsyati^ peaks, becomes thin ', Avestan 

karasa- " skinny '; 

Maybe alb. {*kerk) kerthi^ young, small', kerthize^ umbilical cord of the baby' (common 

alb. -k > -th). 

Latin cracentes, leg. gracentes^ thin, slight, slender, slim, meagre, lean ' to gracilis^ 
skinny, slim, arid', dissim. from *cracilis. 

Old Icelandic horr{*hurha-) " thinness, leanness '; 

Lithuanian karseti, intensiv karstu, karstT become old ', iskarsqs^ frail before age ', 
karse^ senility ', Latvian nuo-karsV become old, mature, ripe, mellow, become seasoned 



kir. kors^ cleared line of land ', Serbo-Croatian krsljav' be slow in growth ', sloven, k'rs 
m. 'shrub, bush', Czech krs^ dwarf tree ', krs-ati, -nouti^ abate ', poln. dial, karslak^ low, 
crooked tree, firewood'. 

References: WP. I 420 f., WH. I 284, Berneker 670. 
Page(s): 581 

Root/ lemma: ker-1, kor-, kr- 

Meaning: a kind of sound (hoarse shrieking, etc.), *crane 

Note: 



Root / lemma: ker-1, kor-, kr-\ "a kind of sound (hoarse shrieking, etc.), *crane' derived 
from Root/ lemma: ger-2\ "to shriek (in expr. forms), *crane'. 
Note: aniaut mostly k-, rare R- also with moveable s- : (s)ker-. 
=====KERS=====
'. Middle Irish ce/77 "point, edge, angle ' (es liegt die Vorstellung des Knicks am Kinnbacken 
^); 

Slavic *ce/77bin: Old Bulgarian crenovbnaja^ puAai ', r.-Church Slavic crenov-bn-b 
(zubb), crenovftbCb " uuAn ' " den^riolans ', Slovak, c/ie/? "mandible, lower jaw bone ' etc. 

After Buga RFV. 67, 234 to Latvian c§ruo-k(s)lis " grinder, molar tooth ', Old Indie carvati 
"chew'. 

References: WP. I 427, Trautmann 129, Specht Indo Germanic Dekl. 141, 169. 
Page(s): 582 

Root / lemma: kers- 

Meaning: a kind of colour (black) 

Note: and probably also bloftes ker-, compare also kel-4 and ker-6. 

Material: Old Indie krsna-^b\acV! = Old Prussian kirsnands., FIN Kirsnappe= Old 

Bulgarian crbPb, russ. cerenb, Serbo-Croatian crn etc. "black' {*cbrxnb, *cbrsnb)\ without - 

/7o-forms Lithuanian kersas^ mottled, speckled black and white, *tabby', kerse' dappled 

cow', /re/^/s "black dappled ox', kersulis^ Ringeltaube '; karsisi. "Brassen, lead (fish)', 

k/rs/ysm. "ash'; the intonation from kersasi\ts but not to Old Indie; 



Note: 

Old Church Slavic: crbnb'b\ack' : Lithuanian: k/rsnas'b\ack (of a horse)' : Old Prussian: 

kirsnan 'black' : Krishna " Vedic black god ' 

Swedish Norwegian harr^ ash ' {*harzu-)\ Old English heard-hara, heardra-m.. Modern 
High German holl. harder, herder^ sea-asW. 

References: WP. I 428 f., Trautmann 118, 134 f. 
Page(s): 583 

Root / lemma: kert- kerat-, krat- {*kuers-t} 

Meaning: to turn, roll, wind, net 

Root/ lemma: kert-, kerat-, krat- {* kuers-tj\ to turn, roll, wind, net, derived from the suffixed 

with -t- formant of Root/ lemma: kures-, kuers-, kufs-\ wood, trees. 

Note: extension from ker-7, S. 574; see below (s)ker-3. 

Material: Old Irish krnatti^ twists the thread, spins ', karttar- "the spinner ', crtati^ binds, 

fixes together', kata-m. 'netting, mat ' (Middle Indie for *krta-), probably also kutf-, kutTi. 

'cottage' {*krfi), kudya-n. {*krtya-) ' (*geflochtene) Wand ', pali koccha-' wickerwork ' (Old 

Indie *krtsa-)\ Old Indie /r/'/s/7a- 'complete, whole' (compare Latin crassus, Slavic *cbrstvh); 

gr. KapTaA(A)o(; m. 'basket', KpoTwvr) ' excrescence on trees, esp. on the olive, 
fragments of bronchial cartilage ' (*KpaTU)va); with ^/-colored reduced grade KupTO(;, Kuprn 
' a fishing-basket, fish snaring net, cage', Kupria ' wickerwork '; 

Latin cratis' wicker-work, a hurdle ', crates dentatae^ harrow ', cratio, -/?e 'harrow' 
{*kerati-, or *krati-, compare Latvian kratihs, Lithuanian krotai); crassus ^\h\ck, strong, 
coarse'; probably cartilage 'gristle' (probably ker[a]t-, compare paima : naAapn); 

In e-grade: 

alb. kjerthuii^ circle, thread reel, thread coil, windlass ' (: Middle Irish ceirtiesee below); 
Maybe alb. kerthiza ' navel, navel cord ' : sloven, kretica ' knot in the weave ': alb. kurth ' 
trap, (net) '. 

Middle Irish ceirtiet ' ball, tangle, knot ' {*kerteiJ3)\ certi. 'scrap, shred, sundries '; 

Gothic haurds {*krtis) 'door'. Old Norse hurd6s., Old Saxon /7i//Y/7' netting'. Old High 
German hurd, PI. hurdids., Modern High German Hurde^ hurdle ', Old English hyrdeian6 
(old) hyrt^ii^ wickerwork ';
```


## [2026-09-06T16:21:16.473Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== LEW gracilis ===\"; grep -n \"gracilis\" LEW_1910.txt | head; echo \"=== LAT gracilis ===\"; grep -n \"gracilis\" LAT.txt | head; echo \"=== AHD kerk/gracile ===\"; grep -n -i \"gracile\\|kerk-\\|kers-\" AHD_watkins1985.txt | head -20; echo \"=== IEC ===\"; grep -n \"gracilis\" IEC.txt | head -5; echo \"=== BRT karesa ===\"; grep -n \"kar\\?sa-\" BRT.txt | head -20",
 "description": "Grep Latin/AHD/Bartholomae"
}
```


### [2026-09-06T16:21:16.573Z] TOOL RESULT

```
=== LEW gracilis ===
=== LAT gracilis ===
14304:cracentes: v. gracilis.
26571:gracilis, -e (f 4 n .gracila, Luc. ap. Non .489,91; Ter. Eu. 314 d'aprbs
64656:gracilis CGL V 634,30- ,
=== AHD kerk/gracile ===
623:(SCARCE). 3. Greek karpos, fruit: -cARP, CARPEL, CARPO-, -CARPOUS. [In Pok. 4. sker- 938.] kers-'. Dark, dirty. 1. Suffixed form *ker(s)-no- in Rus- sian chérnyi (feminine chérnaya), black: CHERNOZEM. 2. Suffixed zero-grade form *krs-no- in Sanskrit krsna-), black, dark: KrisHNa. [Pok. kers- 583.] kers-2. To run. Zero-grade form *krs-. 1. Latin currere (past participle cursus), to run: CORRIDOR, (CORSAIR), COURANTE, COURIER, COURSE, CURRENT, CURSIVE, CUR- SOR, CURULE; CONCOURSE, CONCUR, DECURRENT, DIS- COURSE, EXCURSION, HUSSAR, INCUR, INTERCOURSE, OCCUR, PERCURRENT, PRECURSOR, RECOURSE, RECUR, succor. 2. Suffixed form *krs-o- in Gaulish carros, a wagon, cart, in: a. Latin carrus, a two-wheeled wagon: CAR, CAREER, CARGO, CARICATURE, CARIOLE, CAROCHE, (CARRY), CHARGE, CHARIOT; b. Latin carpentum, a two- wheeled carriage: CARPENTER. [Pok. 2. fers- 583.] kert-. To turn, entwine. I. Zero-grade form *krt-. 1. Suf- fixed form *krt-i- in Germanic *hurdiz, wickerwork frame, hurdle, in: a. Old English hyrdel, hurdle, frame: HURDLE; b. Old French hourd, fence, hurdle, scaffold: HOARDING. 2. Suffixed form “*krt-sti- in Germanic *hur- sti- in Old High German hurst, thicket: Horst. II. Per- haps suffixed variant form *krot-i- in Latin crdatis, wickerwork hurdle: CRATE, GRATE?, (GRID), GRIDDLE; (GRIDIRON). [Pok. kert- 584.] kes-'. To scratch. 1. Germanic *hezd6 in Old English heordan, coarse parts of flax: HARDS. 2. Extended form *kseu- in Greek xuein, to scrape: XYSTER. 3. Nasalized form *ks-n-eu- in: a. Germanic *snaww- in Old Norse snéggr, “close-cropped,” perhaps akin to the source of snuG!: b. Latin novdcula, razor: NOVACULITE. [Pok. kes- 585.] kes-2. To cut. Variant kas-. 1. Suffixed form *kas-tro- in: a. Latin castrare, to castrate: CASTRATE; b. Latin cas- trum, fortified place, camp (perhaps “separated place”): CASTLE. 2. Suffixed form *kas-to- in Latin castus, chaste, pure (< “cut off from, free of, faults”): CASTE, CHASTE; CASTIGATE, INCEST. 3. Suffixed (stative) form *kas-é- in Latin carére, “to be cut off from,” lack: CARET. 4. Ex- tended geminated form *kasso- in Latin cassus, empty, void: (CASHIER), QUASH. [Pok. hes- 586.] kes-°. To order. Suffixed 0-grade form *kos-mo- in Greek kosmos, order: COSMOS; MACROCOSM, MICROCOSM. keu-' Also ekeu-. To perceive, see, hear. O-grade form *akou-. 1. Extended form *kous- in: a. Germanic *haus- Jan in (i) Old English hieran, to hear: HEAR (ii) Old English he(o)rcnian, to harken: HEARKEN; b. suffixed form *9-kous-yo- in Greek akouein, to hear: ACOUSTIC. 2. Variant *skou- in: a. Germanic *skauwon in (i) Old English scéawian, to look at: SHOW (ii) Flemish scauwen, to look at: SCAVENGER; b. Germanic *skaunjaz in Mid- dle Dutch schoon, beautiful, bright (< “conspicuous, attractive”): SCONE; Cc. Germanic *skauniz in Old Eng- lish sciene, bright, sheen: SHEEN. [Pok. 1. keu- 587.] keu-?. Base of various loosely related derivatives with assumed basic meaning “to bend,” whence “a round or hollow object.” I. Extended forms *keub-, *keup-. 1. Ger- manic *haup- in: a. Old English héap, heap: HEAP; b. Dutch hoop, heap, troop: FORLORN HOPE. 2. Germanic *hupp-, to leap (by first bending the legs), in Old English hoppian, to hop: HoP!. 3. Germanic *Aupiz in Old Eng- lish hype, hip: H1P!. 4. Zero-grade form *kup-, vessel, in: a. suffixed form *kup-s- in Greek kupselé, chest, hollow vessel: CYPSELA; b. long-vowel form *kip- in (i) Ger- manic *Aifi- in Old English hyf, hive: HIVE (ii) suffixed form *kip-a in Latin cupa, tub, vat: CUPOLA, CUPULE; c. expressive form *kupp- in Late Latin cuppa, drinking vessel: cup. 5. Zero-grade form *kub- in: a. Greek kubos, cube: CUBE; b. suffixed form *kub-@- in (i) Latin cubdre, to lie down on (< “to bend down, prostrate”): COUVADE, COVEY, CUBICLE; CONCUBINE, INCUBATE, SUCCUBUS (ii) Latin cubitum, elbow: CUBIT; Cc. nasalized form *ku-m-b- in (i) Latin -cumbere, to lie down, recline: ACCUMBENT,
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1335:-CARPOUS kerp- CARPUS kwerp- CARRION sker-1 CARROT ker-1 CARRY kers-2 CART ger-2 CARUNCLE = sker-1 CARVACROL ak- CARVE gerbh- CASCADE kad- CASCARA kwét- CASE! kad-
1344:CHAP2 caupd CHAPITER kaput CHAPMAN caup6 CHAPTER kaput CHARACIN gher-4 CHARACTER gher-4 CHARD kars- CHARGE kers-2 CHARIOT kers-2 CHARISMA gher-5 CHARITY ka- CHARIVARI ker-1 CHARM! kan- CHARNEL sker-1 CHARY gar-
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1397:COUPLE ap-! COURAGE kerd-1 COURANTE kers-2 COURIER kers-2 COURSE kers-2 COURT gher-1 COURTEOUS gher-1 COURTESAN gher-1 COURTESY gher-' COURTIER gher-1 COUSIN swesor- COUTH gnd- COUTURE syi- COUVADE keu-2 COVE! ku- COVEN gWa- COVENANT gWa- COVER wer-5 COVET kwép- COVEY keu-2 cow! gWou- cow2 ku- COWER ku- COWSLIP gWou-, sleubh- coxa koksa
1404:CUPID kwép- CUPIDITY kwép- CUPOLA keu-2 CUPULE keu-2 CUR gere-2 CURATE cura CURATOR cira CURB sker-3 CURD greut- CURE cira CURETTE cira CURIA wWi-ro- CURIO cira CURIOUS cira CURL ger-2 CURRENT kers-2 CURRIER sker-1, CURSIVE kers-2 CURSOR kers-2 CURT sker-1 CURTAL sker-1 CURTILAGE gher-1 cuRTSY gher-* CURULE kers-2 CURVATURE sker-3 CURVE sker-3 CURVET sker-3 CUSHION koksa
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
1429:DIN dhwen- DINGUS _{enk-1 DINOSAUR dwei- DINOTHERE dwei- DIOCESE weik-! DIOECIOUS weik-1 DIOICOUS_ weik-1 DIOPTER oOkW- Dioscuri_ deiw-, ker-3 pip dheub- DIPHTHERIA deph- DIPHYODONT bheue- DIPLO- dwo- DIPLOCARDIAC kerd-1 DIPLODOCUS dek-1 DIPLOE dwo- DIPLOID pel-3 DIPLOMA dwo- DIPNOAN pneu- DIRE dwei- DIRECT reg-! DIRNDL tek- DISARM ar- DISASTER ster-3 DISBURSE bursa DISCERN krei- DISCIPLE dek-! DISCIPLINE dek-? DISCOMFIT dhé-1 DISCORD kerd-1 DISCOURSE kers-2 DISCRIMINATE krel- DIscuss kwét- DISDAIN dek-1 DISEMBOGUE beu-! DISFIGURE dheigh- DISGUST geus- DISK deik- DISMAL deiw-, mel-5 DISMAY magh-! DISMISS (s)meit(9)- DISPARATE pere-1 DISPATCH ped-! DISPEL pel-6 DISPENSE (s)pen- DISPERSE (s)preg- DISPLAY plek- DISPOSE apo- DISPUTE peu- DISQUISITION quaerere DISRUPT reup- DISSECT sek- DISSEMINATE 6-1 DISSENT sent- DISSERTATE ser-3 DISSIDENT sed-1 DISSILIENT sel-4 DISSIPATE swep-2 DISSOCIATE sekw-1 DISSOLVE leu-! DISSONANT swen- DISSUADE swad- DISTANT sta- DISTEND ten- DISTICH steigh- DISTINGUISH _ steig- DISTORT terkw- DISTRACT tragh- DISTRAIN  streig- DISTURB twer-! DITCH dhigw- DITTO deik- DITTY deik- DIURETIC wers-2 DIURNAL deiw- DIVA deiw- DIVARICATE wa- DIVE dheub- DIVERGE wer-3 DIVERT wer-3 DIvEs_ deiw- DIVIDE weidh- DIVINE! deiw- DIVINE? deiw- DIVULSION wel-4 Dizzy dheu-!
1485:EXAMINE ag- EXAMPLE em- EXANTHEMA andh- EXARCH arkhein EXCALIBUR kal-3 EXCAVATE keue-2 EXCEED ked- EXCEL kel-6 EXCEPT kap- EXCERPT kerp- EXCISE? kae-id- EXCITE kei-3 EXCLAIM kela-2 EXCLUDE kleu-3 EXCORIATE sker-1 EXCREMENT krei- EXCRESCENCE ker-3 EXCURSION kers-2 EXECRATE Sak- EXECUTE sekw-1 EXEDRA sed-1 EXEGESIS sag- EXEMPLARY em- EXEMPLIFY em- EXEMPLUM em- EXEMPT em- EXERCISE arek- EXERGONIC werg- EXERGUE werg- EXERT ser-3 EXFOLIATE bhel-3 EXHAUST aus-2 EXHIBIT ghabh- EXHILARATE sel-2 EXHORT gher-5 EXHUME dhghem- EXIGENT ag-
1658:HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
1682:INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
1722:KNOT! gen- KNOUT gen- KNOW gno- KNUCKLE gen- KNUR gen- KOBOLD ku- KOHLRABI kaul-, rap- KoINE kom KOPECK skep- KRISHNA = kers-*- Kriss KRINGLE gene- KRYPTON krau- KSHATRIYA tké- KUCHEN kak-2 KuDOs_ keue-!
1952:OBEY au-5 OBFUSCATE dheu-1 OBITUARY el-1 OBJECT! yé- OBJURGATE ag-, yewes- OBLAST epi, wal- OBLATE! tele- OBLIGE leig-1 OBLITERATE deph- OBLIVION lel- OBLONG del-1 OBLOQUY tolkw- OBNOXIOUS nek-1 OBOE busk- OBSCURE (s)keu- OBSEQUIOUS sekw-1 OBSERVE ser-! oBsEss sed-1 OBSTACLE sta- OBSTETRIC sta- OBSTINATE sta- OBSTREPEROUS §strep- OBSTRUCT ster-2 OBTAIN ten- OBTECT (s)teg- OBTEST trei- OBTRUDE treud- OBTUND (s)teu- OBVERT wer-3 oBvious wegh- OBVOLUTE wel-3 OCARINA awi- OCCASION kad- occipuT kaput OCCLUDE kleu-3 occuLT kel-2 occupy kap- occur kers-2 OCELLUS okWw- OCHLOCRACY wegh- OCHLOPHOBIA wegh- OCTAD okto(u) OctTans okt6(u) OCTANT oktd(u) OCTAVE okt6d(u) OcTAvO okt6(u) OCTENNIAL at-
2079:PER- pert PERCEIVE kap- PERCENT dekm PERCH? perk-1 PERCOLATE kagh- PERCURRENT kers-2 PERCUSS kwét- PERDITION d6- PERDURABLE deue- PEREGRINE agro- PEREMPTORY em- PERENNIAL at- PERFECT dhé-1 PERFIDY bheidh- PERFORATE bher-2 PERFUME dheu-1 PERFUNCTORY bheug-2 PERFUSE gheu- PERGOLA perg- PERI- per! PERICARDIUM kerd-1 PERICLINE Klei- PERIGEE gé PERIHELION sawel- PERIL per-4 PERIMYSIUM mis- PERINEPHRIUM negWh-ro- PERIOD sed-2 PERIONYCHIUM nogh- PERIOSTEM ost- PERIPATETIC pent- PERIPETEIA pet- PERIPHERY bher-1 PERIPHRASIS gWhren- PERIPHYTON bheue- PERIPTERAL pet- PERISARC  twerk- PERISH ei-1 PERISSODACTYL per! PERISTALSIS | stel- PERISTYLE sta- PERITHECIUM dhé-1 PERITONEUM ten- PERITRICH _ thrix PERIWINKLE! weng- PERJURE yewes- PERMANENT men-3 PERMEATE mei-1 PERMIT (s)meit(a)- PERMUTE mei-1 PERNICIOUS nek-1 PERONEAL per-2 PERORAL 6s- PERORATE 6r- PERPEND (S)pen- PERPENDICULAR (S)pen- PERPETRATE peter- PERPETUAL pet- PERPLEX plek-
2129:PRECINCT kenk-! PRECIOUS per-6 PRECIPITATE kaput PRECISE kae-id- PRECLUDE kleu-3 PRECOCIOUS pekw- PRECURSOR kers-2 PREDATORY ghend- PREDECESSOR ked- PREDICATE delk- pRepicT deik- PREDOMINATE deme-1 PREEMPTION em- PREFACE bha-2 PREFECT dhé-1 PREFER bher-1 PREFIGURE dheigh- PREFIX dhig¥- PREGNABLE ghend- PREGNANT! gene- PREGNANT? per-5 PREHENSILE ghend- PREHENSION ghend- PREJUDICE deik-, yewes- PRELAPSARIAN leb-1 PRELATE telo- PRELECT leg-1 PRELIBATION [éi- PRELUDE leld- PREMATURE ma-1 PREMIER per! PREMISE (s)meit(@)- PREMIUM em- PREMONITION men-1 PREMORSE mer-2 PREMUNITION mel-3 PREPARE pere-! PREPENSE (s)pen- PREPONDERATE (S)pen- PREPOSITION apo- PREPOSTEROUS apo- PREPOTENT _poti- PREPUCE pu-! PREROGATIVE reg-1 PRESAGE sag- PRESBYOPIA per! PRESBYTER pert PRESCIENT skel- PRESCIND  skel- PRESCRIBE skribh- PRESENT! es- PRESENT? es- PRESENTIMENT sent- PRESERVE ser-! PRESIDE sed-! PRESS! per-5 PRESSURE per-5 PRESTIGE streig- PRESUME em- PRETEND ten- PRETERIT el-1!, per? PRETERMIT (s)melt(@)- PRETEXT teks- PRETZEL mregh-u- PREVAIL wal- PREVENIENT gWa- PREVENT gWa- PREVIOUS wegh- PREVISE weld- PREY ghend- PRICE per-6
2174:REBUT bhau- RECALESCENCE kele-! RECANT kan- RECAPITULATE kaput RECEDE ked- RECEIVE kap- RECENSION kens- RECENT ken-3 RECIDIVISM kad- RECIPROCAL pert RECISION kae-id- RECK reg-1 RECKLESS reg-! RECKON reg-1 RECLAIM kele-2 RECLINE klei- RECLUSE kleu-3 RECOGNIZE gnd- RECOIL (s)keu- RECOMMEND man-2 RECONDITE dhé-1 RECORD kerd-1 RECOURSE kers-2 RECOVER kap- RECREANT kerd-1 RECREMENT krei- RECRIMINATE  krei- RECRUDESCE kreud-! RECRUIT ker-3 RECTANGLE reg-1 RECTIFY dhé-1, reg-1 RECTILINEAR reg-1 RECTITUDE reg-!
=== IEC ===
6213:-ilis, adj. extn. of quality Alb. cf. í vogël ((small', fr. *suagilis or *uag(h)-); Lat. cf. qualis, tālis, gracilis, habilis, etc.; OCS cf. koli, tolí “how much, so much’: Latv. cf. svilis (“red pig’, cf. Lat. suile 'sty^)
=== BRT karesa ===
4546:•  j.  ankasa-  m.  EN.  eines  Gläubigen: hvanza  °sayä  (GD.)  asaona  "des  H.  und des  A.  (der  beiden  Brüder) ,,"  Yt.  13. 124.
9422:erblicken'.    Praes.  3  kasa-.  ail"'/-
9456:•  j.  'kasa-  m.  Achselhöhle  :  dastmm  ■  ^L  vgl.  *r7>onii«j.  Adj.  'begehrend',  drao- (bz.  Ajf^/n)  'W/W  V.  Ä  48-50*,  <?.  17,  18^;'  Adj.  'carus'.  —  S.  noch  kima-.—  Pü.  (lu  Y.): —    ;;aV    hts    bardii    nfa    'Um    N.  2.?;  — '      =^ähll.%ü.isamlhau;  (zyi^^^y.tallihinim   -
9459:•  1.  'kasa-  m.  Sichzutunmachen  mit  — "';  .  ,,  ,  ...  „nm  n  j  i»  n ,,.'  ,,1  •  1.  'kala-  Adj.,  PPiP.:  s.  'kan-  und  «a-'J. UartUDg  ')                                           _                           J.        E,  _  v^,'.  u:ua..-  .)  Es  ist  nicht  in
25491:•  j.  iristö.kasa-  m.  Totenwärter':  kva aita/ie   nars   gätus    anhat   yat    'sähe    V,
```


## [2026-09-06T16:21:18.474Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== KLN 672 area gracile ===\"; grep -n \"gracile\" KLN_1966.txt | head -10; echo \"=== KLN alchemy/chemistry ===\"; grep -n -i \"^alchemy\\|alchemy,\" KLN_1966.txt | head -10; grep -n \"chemeia\\|Chemia\\|khemeia\" KLN_1966.txt | head -20",
 "description": "Grep Klein"
}
```


### [2026-09-06T16:21:18.556Z] TOOL RESULT

```
=== KLN 672 area gracile ===
16504:Gracilaria,  n„  a  genus  of  algae  (hot.)  —  ModL., fr.  L.  gracilis,  ‘slender’.  See  gracile. gracile,  adj.,  i)  slender;  2)  gracefully  slender.  — L.  gracilis,  ‘slender,  thin,  slight,  meager’,  dis¬ simulated  fr.  *cracitis,  rel.  to  cracens,  ‘slender’, and  prob.  cogn.  with  OI.  kfsdh,  ‘thin,  weak’, Avestic  klr*sa-,  ‘lean,  meager’,  Lith.  karitu, karSti,  ‘to  be  very  old,  to  age’,  Lett,  karst,  karst, ‘to  grow  old,  ripen’.  Cp.  Gracilaria.  For  the  end¬ ing  of  grac-ilis  cp.  habilis ,  ‘handy,  supple,  suit¬ able’,  fr.  habere,  ‘to  have,  hold’  (see  able).
16505:Derivatives:  gracile-ly,  adv.,  gracile-ness,  n., gracil-ity,  n.
=== KLN alchemy/chemistry ===
2130:Alchemilla,  n.,  a  genus  of  plants  of  the  rose  family ; the  lady’s-mantle  (bot.).  —  ModL.,  fr.  Port. alchimelech,  fr.  Arab,  iklil  al-mdlik,  ‘the  crown of  the  king’.  The  first  element  is  prob.  a  loan word  fr.  Aram.  kelil,  kllild,  ‘crown’.  For  the second  element  see  malik,  Mameluke, alchemy,  n.  medieval  chemistry.  —  OF.  alquemie (13th  cent.),  alchimie  (14th  cent.)  (F.  alchimie), fr.  ML.  alchemia,  fr.  Arab,  al-kimiyd,  fr.  al-, "the’,  and  MGk.  yr(uda,  a,  prop,  ’the  art of  the  black  land  (Egypt)’,  fr.  Gk.  Xrjuta,  ‘Black- land,  Egypt’,  fr.  Egypt,  khem,  khame,  ‘black’. The  derivation  from  Gk.  x'JireiS,  ‘pouring’, from  the  stem  of  y_£e iv,  ‘to  pour’,  is  folk  ety¬ mology.  See  W.  Muss-Amolt,  Transactions  of the  American  Philological  Association,  vol.
```


## [2026-09-06T16:21:27.673Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('alchemy,  n.  medieval')\nprint(repr(t[i-100:i+900]))\nEOF",
 "description": "Klein alchemy context"
}
```


## [2026-09-06T16:21:28.154Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"chemistry,  n\\|chemist,  n\\|chemical,  adj\" KLN_1966.txt | head",
 "description": "Klein chemistry entry"
}
```


### [2026-09-06T16:21:29.745Z] TOOL RESULT

```
' loan word  fr.  Aram.  kelil,  kllild,  ‘crown’.  For  the second  element  see  malik,  Mameluke, alchemy,  n.  medieval  chemistry.  —  OF.  alquemie (13th  cent.),  alchimie  (14th  cent.)  (F.  alchimie), fr.  ML.  alchemia,  fr.  Arab,  al-kimiyd,  fr.  al-, "the’,  and  MGk.  yr(uda,  a,  prop,  ’the  art of  the  black  land  (Egypt)’,  fr.  Gk.  Xrjuta,  ‘Black- land,  Egypt’,  fr.  Egypt,  khem,  khame,  ‘black’. The  derivation  from  Gk.  x\'JireiS,  ‘pouring’, from  the  stem  of  y_£e iv,  ‘to  pour’,  is  folk  ety¬ mology.  See  W.  Muss-Amolt,  Transactions  of the  American  Philological  Association,  vol.\nalcmaeon\naiexipnarmic\nXXIII,  p- 149.  Cp.  chemical,  chemist,  chemistry. Derivatives:  alchem-ic,  alchem-ic-al,  adjs.,  al- chem-ic-al-ly,  adv.\nAlcmaeon,  n„  one  of  the  epigones  ( Greek  mythol.)\n—  L.  Alcmaed(n),  fr.  Gk.  ’AXxpucicov,  prob. meaning  lit.  ‘valiant,  brave’.  Cp.  Gk.  aXxp.oaos (Hesychius),  ‘young  man’,  &Xxp.ap£s  (neut.) (ibidem)'
```


### [2026-09-06T16:21:29.786Z] TOOL RESULT

```
2129:Alcestis,  n.,  wife  of  Admetus,  one  of  the  Argo¬ nauts  ;  she  offered  her  life  for  her  husband  but was  rescued  from  the  lower  world  by  Heracles (Greek  mythol.)  —  L.  Alcestis,  fr.  Gk.  ’'AXxy)<m;, lit.  ‘valiant,  courageous’,  fr.  d Xxtj,  ‘protection, help,  strength,  power,  courage’.  See  Alexander, alchemist,  n.  —  OF.  alqemiste  (F.  alchimiste),  fr. alqemie.  See  alchemy  and  -ist.
5041:bio-,  combining  form  meaning  ‘life’.  —  Gk.  (3io-, fr.  pios,  ‘life’,  dissimilated  fr.  *pi Foq,  fr.  I.-E. *glciwos;  cogn.  with  Goth,  qius,  OE.  cwicu, ‘living’.  See  quick,  and  cp.  vital,  zoo-.  Cp.  also biosis,  biotic,  and  the  second  element  in  aerobic, amphibious,  bathybius,  cenobite,  microbe,  hy¬ giene,  Limnobium,  Lithobius,  macrobiotic,  ne¬ crobiosis,  Rhizobium,  symbion,  symbiosis, biochemistry,  n.,  chemistry  dealing  with  animal and  plant  life.  —  See  bio-  and  chemistry, biogen,  n.,  a  protoplasmic  unit  ( biol .)  —  Coined by  the  German  physiologist  Max  Verwom (1863-1921)  in  1903  fr.  bio-  and  -gen. biogenesis,  n.,  the  theory  that  living  organisms can  only  arise  from  pre-existing  living  matter (biol.)—  Coined  by  the  English  biologist  Thomas Henry  Huxley  (1825-95)  in  1870  fr.  Gk.  pto?, ‘life’,  and  y^veoic,  ‘origin,  source’.  See  bio-  and genesis  and  cp.  abiogenesis. biogenesist,  n.,  one  who  believes  in  the  theory  of biogenesis.  —  See  prec.  word  and  -ist. biogenetic,  biogenetical,  adj.,  pertaining  to  bio¬ genesis.  —  See  biogenesis  and  -etic,  resp.  also  -al. Derivative:  biogenetic-al-ly,  adv. biogeny,  n.,  biogenesis.  —  Compounded  of  bio- and  -geny.
7333:chemist,  n.  —  F.  chimiste,  fr.  chimie,  ‘chemistry’. See  alchemy  and  -ist.  Derivative:  chemist-ry,  n. chemo-,  combining  form  denoting  relation  to chemical  actions  or  chemicals.  —  See  chemic. chemosis,  n.,  swelling  of  the  conjunctiva  (med.)  — Medical  L.,  fr.  Gk.  yfioiaic,  ‘affection  of  the eye  in  which  the  cornea  swells  like  a  cockle¬ shell’,  fr.  yj],u. r],  ‘a  yawning,  gaping:  cockleshell’, which  is  rel.  to  yatvsiv,  ‘to  yawn,  gape’;  fr. I.-E.  base  *ghei-,  *ghi-,  ‘to  gape,  yawn’.  See chaos  and  -osis  and  cp.  chela,  ‘claw’, chemotherapy,  n.,  —  Coined  by  the  Jewish  bac¬ teriologist  and  chemist  Paul  Ehrlich  (1854-1915) fr.  chemo-  and  therapy.
23665:metachemistry,  n.,  higher  chemistry.  —  Formed fr.  meta-  and  chemistry.
23826:microchemistry,  n.,  that  branch  of  chemistry which  deals  with  microscopic  objects  or  quanti¬ ties.  —  Compounded  of  micro-  and  chemistry. ndcrocUne,  n.,  a  kind  of  feldspar  belonging  to  the
31194:pyrochemical,  adj . ,  pertaining  to  chemical  changes caused  by  high  temperature.  —  Compounded of  pyro-  and  chemical.
36738:Derivative:  stereobat-ic,  adj. stereochemistry,  n.,  that  branch  of  chemistry which  treats  of  the  arrangement  of  molecules and  atoms  in  space.  —  Compounded  of  stereo- and  chemistry.
38987:thermochemistry,  n.,  that  branch  of  chemistry which  deals  with  the  relation  between  heat  and chemical  action.  —  Compounded  of  thermo- and  chemistry.
```


## [2026-09-06T16:21:45.954Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SOD ks ===\"; grep -n \"thin, small\\|small, weak\\|ʾks\\|'ks\" SOD_pages.txt | head -20; echo \"=== SOD grep ksy ===\"; grep -n \"ks .*thin\\|thin\" SOD_pages.txt | head -20",
 "description": "Grep Sogdian dictionary"
}
```


### [2026-09-06T16:21:46.017Z] TOOL RESULT

```
=== SOD ks ===
9839:      oxsankawe Oxsnq'wyh) -^ysnkWk                                 axsic   ^'ksyc
15750: 4213 yrp'kstr B                          yJiU<>lfT
15754: 4214 yrb'qstr      C =* yrP'kstr                                  yarfi-xware -^yw'^y
15784:     yarpikistar ^yrP'kstr                                         TSP 2.335 -h
16629:  4511 ywyz'kstr B                             JAj*JksJ           yisp ? «*yysp
17633:       karx-nyatakya     ©f. n. ^k^y                                  -(,)y; pi. >ksth pred. inst. >ks} =*'ks-
18987:5347 mndyrp'kstr M                                                   manpat ©impf. ^npt-, nVpt-
27511:8243 pwt'ks'ytr B                                                 8258 pwtty'kh      S(M) =* pwty>k(h)
28622:8642 rync'kstr S                                   J-&?/             saliva                                                aOf
28645:     rincuk-star =*rystr, ryncwk, rync'kstr                           W-Lii 547.6; BBB pl34; GMS 464, 1241, 1288;
31914:      tewak-(a)skune (tyw'kskwny)
31931:9763 tyw'kskwny =» tyw^skwny                                     as much as, so much
=== SOD grep ksy ===
2010:notes, cross-references, Persian meaning, English          the Buddist corpus and non-Buddhist excerpts within
2054:pronunciation at the beginning of the word or within             Grammatical Notes, beginning with the symbol
2233:Kash) writhin the territorial limits of Soghd. He            that the peoples from Farghane to the frontier of
2373:        far as North Mongolia. This document is evidence of              differences within the written materials are
2424:narrow passage within one of the ruined watch                   assumed to have been closed in the beginning of the
2433:   In 191 1, a tentative reading by A. Cowley28                 25. Some scholars think that the language of Bukhara was
2884:containing Turkish elements)97 which were found in              consonants including allophones. For one thing, it
2992:Sogdian vowels at least qualitatively in some                     shows that the dialectal differences within the
3040:the stress within the word. Thus, heavy stems having
3085:  lee/          *yc          something Av. aeta                              (terror).
3094:  /ostay/       V^y              to place Av. ava-staya-                     etymological written y alternates with nothing
3309:words are transcribed (not borrowed) into the                        Wiliiams. Livsic thinks that the last letter of the
3313:       Some Sogdian loanwords in Persian render by /                 I SI), while Sims- Williams thinks it was used to
3939:                                                                something, anything
3951:     something, anything                                          ->kyK Dhy. 338
3964:                                                                something, anything
4833:    TSP 6.80; BSTBL, Vim. 182; AVS 74                                thing, something
4843:    something                                                           taken
4848:    something
5520:    Hen. Tales. 469, 38, 470 p2                                  what, that, something, why
```


## [2026-09-06T16:21:48.969Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BQT v3 گرسیوز ===\"; grep -n \"گرسیوز\" incoming/BQT/BQT_v3_pages.txt BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head; echo \"=== گرشاسپ ===\"; grep -rn \"گرشاسب\\|گرشاسپ\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head; echo \"=== کیمیا ===\"; grep -n \"کیمیا\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head",
 "description": "Grep Borhan-e Qate volumes"
}
```


### [2026-09-06T16:21:49.067Z] TOOL RESULT

```
=== BQT v3 گرسیوز ===
=== گرشاسپ ===
incoming/BQT/BQT_v4_pages.txt:5810:در گرشاسب‌نامه از « مهراج » یادشاهی معین را در هندوستان آراده کرده :
incoming/BQT/BQT_v4_pages.txt:5813:«گرشاسب نامه ‎٩۳‏ > و رك : فهرست اعلامآ نکتاب .
incoming/BQT/BQT_v4_pages.txt:8619:کلمه دراوستا صفت گرشاسپ جهان پیلوان است ولی بتدریج جورت «لر‌بمان» و نیرم » درآهده.
incoming/BQT/BQT_v4_pages.txt:8621:تربمان صفت ( و لغب ):خود گرشاسپ بوده است . رل : پورداود . بشتها ج ۱ ی ۱۹۹ ؛ قاب
incoming/BQT/BQT_v4_pages.txt:19677:وگرشاسپ باوبخشیده شد. چهارمین پوروشب است که در پاداش پری مثل و- زرتشت - از او
incoming/BQT/BQT_v4_pages.txt:21154:ورك4: اسدی. گرشاسب نامه ص۵۸ «وّلف صحاح الفري آرد: ۶ بعك.. چهار دندان پیشین سباع
incoming/BQT/BQT_v3_pages.txt:43415:گرشاسب جهان پهلوان ابرانی ؛ در شمن می‌وشش یبت آعده »که درتیجه شیروی کشته شدم.
incoming/BQT/BQT_v3_pages.txt:43416:۲ - از گرشاسب پسر زو ( زاب ) ودهمین پادشاه پیشدادی که نه سال پادشاهی کرد , باد ‎wat‏
incoming/BQT/BQT_v3_pages.txt:43417:‎a lela: (‏ ج ۱ ص ۷۸۲ ) . موضوع کرشاسب ‎LU‏ اسدی طوسی همان گرشاسب دختی‌است.
incoming/BQT/BQT_v3_pages.txt:43473:استعمال کرده باشند» وحتی اپوالفدا آنرا « کرشاسف » ضبط کرده‌است . نامهدر گرشاسپ در اوستا
=== کیمیا ===
incoming/BQT/BQT_v4_pages.txt:1430::کنون هرچه مانیده بود از لیا زکین جستن وجنکه و ا زکیمیا...
incoming/BQT/BQT_v4_pages.txt:3211:.وباسطلاح اهل صنمت که کیمیاکران باشندآهن | مجهول کشيده وشین نقطه‌دار مضموم بمیم زده »
incoming/BQT/BQT_v4_pages.txt:3528:سنمت که کیمیا کران باشند آن را طلاکنند. ‏ ۱ بهم تبدیل می‌باید چنانکه در فواید کفته شد۷ .
incoming/BQT/BQT_v4_pages.txt:4550:( خمیر کردن ) ماخوذ است. همن‌لفت عربی «* الملقمه» وارد لاتینی (کیمیاگران ) شده صورت
incoming/BQT/BQT_v4_pages.txt:6601:خوانند۴ - ودرعربی هیمون بمعنی‌مبارك وخجسته | کاربها بکار برند - و بمعتی کیمیا هم:آمده است
incoming/BQT/BQT_v4_pages.txt:6632:چه کیمیا کر را میناگر هم میگویند ۱ - و نام | شحا4 9 #۰
incoming/BQT/BQT_v4_pages.txt:12883:نیم هلال - یک ها , کنایه از لب نیا - بکسر هردو نون بروز ن کیمیا +
incoming/BQT/BQT_v4_pages.txt:18474:«غزالی. کیمیای سعادت چاپ کتابفروشی مر کزی‌تهران ۱۳۱۹ج۲مره۹۳» . «یکی ازوزراه بزرس
incoming/BQT/BQT_v3_pages.txt:3480:‎he‏ است محصوضاً در صنمت کیمیا - و لوشادر
incoming/BQT/BQT_v3_pages.txt:26453:اشاره ‎gle‏ کیمیاست - و در عربی بمعنی ‎SUS‏
```


## [2026-09-06T16:21:54.465Z] TOOL CALL #14: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:1795 2>&1 | head -60",
 "description": "Fetch BQT page 1795"
}
```


### [2026-09-06T16:22:02.050Z] TOOL RESULT

```
(no exact page map; using offset -1205 -> pdf page 590; check the printed number and re-run with --pdf-page if off)
REF: BQT:1795  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 590  OCR-lang: fas

شتمنه کرزن
گر ۱ -«بم اول وسکون نانی وزای کوبند ۴ ؛ و باکاف تازی هم بنظر آمده است.
نقطه دار » عمود : گرد - بنم اول وفتح ثانی و سکون
آعنین راکویند جوا | نات ومیم . برادرایانی‌اسفندباراست واوی دکوبی
اسفندبار پیش گشتاسب کرد و گشتاسب اسفندبار
و چماق چوب را گرز 2 ۱ :
: را بند فرمود 9 .
هم کعته‌اند - و دستهٌ هاون را نیز کوبند - : زما۹. :
وکنایه ازقضیب هم هت که آت تناسل باشد. گرز تن - بفتح اول وثانی و رایع
ی بالف کشیده بروزن فلك‌سان » آسمان را گوبند؛
گرددمن بفتح اول وئانی‌وسکون 1 0 ۰
ی ۹ وبفتح ول وسکون ثانی هم آمده است - وعرش
زای نقطه‌دار وفتح دال بی‌نقطه وکسر میم ونون اعظم را نیز گفته اند که" فلك الافلاك باشد ۷ .
ساکرن. داغت ند وبازند نمعنی‌دشمرن وغنم‌باشد. ۰
نی رد ۳ ی ۳۳ ۱ گردن < بر وزن آرزن » تاج مرصعی
گرد تن - جم اول وفتح ثانی‌ورا بم بوده کیانر! بیار بز رکه وسنگین وآنرا پربالای
وسکون ثالث ونون آخر . بمعنی چاره کردن | تخت‌محاذی سر ایغان‌با زنجیرطلامی آويشته‌اند .
علاج نمودن باشد ۰ کونند درآن صد دانه مروارند بود هريك بقدر
۳ شش ۰.۰ ۰ ۰ ‌
گرردش - بفتح اول و کس ثالث‌بروزن | بيضهٌ کنجشگی وآن بانوشیروان رسیده و عربان
ورزش,تظلم وداد خواهی وتضرع وزاری‌نمودن را | آنرا قنقل بروزن منقل کفتندی و قنقل کیله
۱ - پهلوی ۰۷227 اوستا- ۷2272 ۸ بارتولمه۱۳۹۲*. معرب جرز. ارمنی ع۷272هندی
باستان- ۷8[۲۵ (کرز رعد [ایندرا]) «اسشق ۹۰۹۰ « نیب رکه ص۲۳۷ کردی 8072 « ژابا ص
۵۹ - ۳۹۰ *.ورك :کرزه. ۴ نمهز. ۰887220427328 8۳۵[4038. ۰12۳741322
پهلوی 25۳2۳ ۱ شم ( ای بونگر ص ۱۱۷۲ . ۴ - معسحف «گزردن ئ (ج.م.) -
گزربدن ( رك : گرزیدن ‎٩‏ ) . ۴ - «کرزش, نظلم بود . خسروانی گفت :
بده داد من زان لبانت و کرته سوی خواجه خواهم شد از تو بگرزش.»
آقای دهغخدا کلمهرا مصحف «گزرش » ۳ (کزاری) میدانند . « لغخت فری ۲۱۳ .۰
8 - و نیز یکی از قهرمانان تورانی . رك : فهرست ولف :
‎٩‏ - کلمهٌ پارسی ( مستعمل زرتشتیان ) - فارسی 82721121 ( آسمان ) . این‌کلمه‌در
اوستا 0438282 827۵6 . ۸۳۱288 827۵ پازند 82761۳128 ۰ مغدی ۰8۳27043388
پارتی 82701088 » اوراق مانوی بپارسی‌میانه 8472577128 . وكلمهٌ پارسی- فارسی82۳2128
تلفظ متأخر ومفلوط است بمعنی (آسمان علیین ۰ عرش خدا) با بهمنی وسیمتر (آسمان,بهشت).
رد : (۱57 . 0 . ۷۷۹۵۲۵۵ ۸8128 |621۳8 1۷0 ,ع 1162810 ) ورد :
( ۱,0.82 ,13 , 8505 ب ... ققنوت۳ ۷۵۵۱6 0۶ ۱۶4 ۸ « قصادی۲
ورد : اآسشق ‌- هوبشمان۹۰۹٩‏ (۱9ط)
۷ - ۶ پارسیان کوبند عرش است و شعراکویندآسمان است . دقیقی (طوسی) کوید :
مه وخورشید با برجیس وبهرام زحل با تیر و زهره بر کرزمان
همه حکمی بفرمان تورانند که ایز دمرترا داده است‌فرمان.»
‌ لهخت فری ۹۷ عم
```


## [2026-09-06T16:22:13.091Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سیوز\\|رسیوز\" incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt | head -20; echo \"--- pdf tags near line 43415 in v3 ---\"; awk 'NR>=43380 && NR<=43420' incoming/BQT/BQT_v3_pages.txt | grep -n \"pdf page\" ; grep -n \"\\[pdf page\" incoming/BQT/BQT_v3_pages.txt | awk -F: 'NR%1==0' | sed -n '585,600p'",
 "description": "Search Garsivaz in BQT"
}
```


### [2026-09-06T16:22:15.009Z] TOOL RESULT

```
--- pdf tags near line 43415 in v3 ---
42767:[pdf page 585]
42859:[pdf page 586]
42962:[pdf page 587]
43036:[pdf page 588]
43131:[pdf page 589]
43223:[pdf page 590]
43276:[pdf page 591]
43362:[pdf page 592]
43432:[pdf page 593]
43484:[pdf page 594]
43551:[pdf page 595]
43640:[pdf page 596]
43702:[pdf page 597]
43778:[pdf page 598]
43874:[pdf page 599]
43972:[pdf page 600]
```


## [2026-09-06T16:22:19.872Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=43276 && NR<=43500' incoming/BQT/BQT_v3_pages.txt",
 "description": "Print BQT v3 pdf pages 591-593"
}
```


### [2026-09-06T16:22:21.617Z] TOOL RESULT

```
[pdf page 591]
گرزه
و پیمانه بز رکه را گونند ۱

‎OIF‏ © بنتح اول بروزن هرزه »لوعی
ازمار استء وبعض یکوبند ماری باشد سر بز رکه
و پر خط وخال وزهر او ‎asks‏ از مارهای ‎Kee‏
‏است وهیج ترباقی برزهر او مقاومت نکند ۴ -
ودر بعضی از ولایت دارالمرز ۴ موش راکرزء ۴
‎any‏ - و بضم اول. هم یمعنی اولوهم‌بمعنی
کرز باشدکه عربان‌عمود کویند ۵ .

‏گرد گاو پیکر ۷ » ‎oma‏
‏راگوبند چه آنرا بپیأت سر کاومیش از فولاد
ساخته ‎Woy‏ .

‏گر او چهر ۱ -بس یکره
‎Kash‏ است که کرز فربدون باشد .

‏گرز ق گاف سار ۷ - بممنیکرز: کاو
چهراست که عمود فربدون باشد.

‏گرد ة گاوسر ۱ - ‎WSS gn‏

‎. ‏چش : - وآنرا ... بودند‎ (A)

‎1۷۹4 -

‏سار است ‎IFT‏ فربدون باشد .

‏گرذخ او میش ۱ - بسن ی کرزه
کاوسراست که گرز فربدون باشد ‎a LT,‏
سر کاومیش از فولاد ساخته بودند ‎AN)‏

‏گرزیدن ۷ - بن اول و فتح ‎BE‏
‏بروزن ستجیدن » بعمتی گرزدن باشد که چاره
وعلاح کردن ‎col‏ ۰

‏گردلن ‎a‏ بکراول بروزن‌مسکین:
تاج کیانیرا گوبند و آنرا مرصع ساخته از بالای
تخت محازی‌سرایشان باز اجیر طلاآ ویشته‌بوده‌اند
- ویمعتی زبیل ‎col le‏ - و ‎ps‏ پیکان‌دار
را 5 گفته‌الد ۱

‏گرس . ‎em‏ اول و سکون ‎gt‏ وسین
بی‌نقطه » کرسنگی راکویند که در مقابل سپری
است ‎٩‏ - و ‎gine‏ چرك وزیم جامه و بدن هم
آمده است - وموی پیچیده وموی پیچه را لیز

‏کفته‌اند که موباف زان باشد ‎NO‏

‏۱ -قی :کرزن « دزی ج ۲ ص ‎boo‏ ۰۰ ورگ : هرمزدنامه ص ۸-۳۰۷ ۶ نیم‌تاجی
بود از دیبا بافند بزرو ‎pS‏ مفرق کرده » و کوبند ناجی بود ‎Sg‏ وزین پرجواهر ومئوك ‎PB‏

‏تخت ‎gating Lb,‏ . بوسف عروضی گوید :

‏ار عیر بیکوان جهانت و یکوبی

‏۴ - بدی مار کرزه است » از او دورباش

‏۴ مراد گیلان است.
‎Coa) in ®‏
رك : کرزدن » ۸ - ره :038 .

‏تاجت وسال وماه مر اورا چ وکرزنت .»

‏« لت فری ۰۳0۹ .
که بد بدتر از مار گرزه کزد .
« ناصرخرو بلخی . دبوان ص ۱۱۲ *.

‏۴ - درلاهیجان وحوالی ‎OT‏ 88628 (موش) «میررفتی»

‎. Kas: ‏رك‎ ۱

‏۷ - مسحف «گزربدن »< گزردن
‎٩‏ هه کوری , رگ : گرسنه » کشنه » کاشانی

‎.veshegi , ۷۵۵۳۵ . ۷6:۵۵ .vesh‏ پهلری ‎gursitan .gursakib .gursak‏ ؛ کردی
‎vursigt . vurst‏ . ۷۵52 بلوچی ‎gushnage‏ تننی ‎gushna‏ > استق ۹۰۷ ۰ ۰ شکل
پارسی باستان - 0۷۳58, 0۷۲5۵2«هویشمان ‎٩۰۷‏ > رك : «گرسنه » (هم.) ورك : رشیدی و
فرهنگه نظام . جهانگیری و فرهنگه نظام این بست شاهد آورده‌اند :
کر ازدلم برد نم زلف وخال ‎cays‏ جان باخیال رشته فتاد ازخیال‌دوست. بسحاق اطعمه,
اما در دیوان بحاق چاپ قطنطنیه ص ۳۸ بجای کرس > جوع © وبجای خیال اول در مصراع
دوم > حبال » آمده است . ۰ ر : اسشق - هوبشمان ‎٩۰۸‏ .

‏(برهان فاطهه۴۳)
[pdf page 592]
۱۷۹7

گرست « بفتح اول و ابی و سکون
ثالث و ‎sigh‏ بمعنی سیاه همست باشد وبعریی
طافع گویند ۱ - و بزبان علمی هند فرو بردن
لقمه و امثال ‎OT‏ باشد و عربان ‎ab‏ خوانند.

گرسقن ۴ - بکر اول وانی :مخف
کربستن است که کربه کردن باشد .

گر ستودن ۴ بفتح‌اول وئالی‌بروزن
تیغرودن » بمعنی ‎OS‏ است وآن ترازو مانندی
است که بستها و تنگهای ‎gh‏ را بدان سنجند .

گرستون ۴ © بفتح اول وئالی بروزن
شف ق کون + بمعت ی گرستودن است که ‎methods‏
‏وبه‌عنی کیل ‎Ulan‏ بزر که همآمده است‌ومعرب

گرسنه چشم - بت ول تا ناه
از ‎Ste‏ و ممسك ‎ath‏ - و مردم ‎ad‏ وکدا را
‎e‏ میگویند ۵ - وکنابه از مردمی‌هم هست که
از قحط وغلا برآمده پاشتد .

گرسنه چشمان کنعان - کنایه
از برادران ‎Gey‏ علیه‌اللام است .

گرسیان - با بای ونون وحرکت
غیرمملوم « نوعی‌ازسنگه باشد ‎OT;‏ درهتدوستان
‎re‏ میرسد ودر صثمت کیمیا ‎ale‏ 1

‎Sg F‏ = بتادرستا مود
بروزن بخنی‌پز » نام برادر افراسیاب است ؛ وبا
کاف تازی هم بنظ رآمده است .

‏آن قرسطون ‎Fath‏

‏گر شاسب ۲ = با تین قطمدلر بروزن

‎٩‏ باز رسید مت ما داد قدح بدست ما

‏کر دهدی بدست نو شاد و خوشی و کرمتی -

‏مولوی بلخی رومی «جهانگیری» وبنابرین بیت با اول وسوم مفتوح وسکون دوم است -

‏۴ مخففگرستن: رك: لفت ‎EB‏ ۴ - ظ. مصحف «کرستون*.رثك: کرستون.

‏۴ = کرستون (.م.) < فرسطون. رك: فرسطون ‎ .‏ 8 - وحاصل مصدر(اسم‌ععنی)آن
«گرسته چشمی » است . ۲ = ‎jp‏ ؛ در اوستا ‎Keresavazda‏ ( از دو جزء :
2 لاغر واندك , ۷۵28 فوت » پابداری ) ( بمعنی استقامت و بابداری کم دارندء ) تم
برادر افراسیاب است « پورداود . يشتها ج ۱ ص ‎VV‏ ۷ - در شاهنامه ‎pelt Syl‏
پرميخوريم ‎ :‏ ۱- در برخی ازسخ شاهنامةٌ فردوسی( ‎GLEE‏ بخ ج ۱ ص ‎۱۰٩‏ ح ) اسرعنوان
( ناخت کردن منوچهر برسپاهء‌تور ) داستان بمیدان آمدن شیروی پپلوان نورانی و برزم طلبیدن
گرشاسب جهان پهلوان ابرانی ؛ در شمن می‌وشش یبت آعده »که درتیجه شیروی کشته شدم.
۲ - از گرشاسب پسر زو ( زاب ) ودهمین پادشاه پیشدادی که نه سال پادشاهی کرد , باد ‎wat‏
‎a lela: (‏ ج ۱ ص ۷۸۲ ) . موضوع کرشاسب ‎LU‏ اسدی طوسی همان گرشاسب دختی‌است.
کرشاسب در اوستا صورت 16676585۳2 و درسانسکریت 168528۷8 آمده مر کب از دوجزه:
ارل 66۳658 بیمنیلاغر , جزء دوم 2508 همان اسب فارسی است [ دو ۸ در اوستا تبدیل به 4
شده ] مجموعاً بیمنی ‎tah‏ اسب لاغر ,کی که اسبش لاغر است. بنابرین لفة اصح کرشاسب

‏بقیه در مفعةً ۱۷۹۹

‏گرسته - نم اول وکسر دوم و چپارم ( در ‎bend)‏ مر‌کزی ) و نیز جضم اول و دوم و
فتح چهارم» و در شعر بضرورت ‎pie‏ اول و سکون دوم وفتح سوم و چپارم » پهلوی 80758 .
‎gursakih‏ «استو ‎acy‏ تهرانی ‎glam . Vishta SLO, gushna‏ «کری» ‎aS‏
‏ک ی که محتاج‌بخوردن غذاست ‎SGT.‏ احساس احتیاج بخورد نکند :

‏ب سگرسنه خفت وکس ندانت که کیست بس جان بلب آمدکه بروکس نگرست.

‎2h ۳۵ IT >
[pdf page 593]
کرشاسف ‎wae‏
‏طهماسب ؛ تلویکی از اجداد رستم زال ات واو | سرعست » رستنيی باشد خود روی شبیه باسفناج
پر اترد باشدکه از نباثر جمشید است - و نام | که در غلعزارها و کنارهای جوی آب روید ودر
‎ee ae ees‏ عوض اسفناج درآش وشله کنند .
بادشاه شد وهمان در حیات جنگه اس فد
: وهمان در حیات پدر ‎ND‏ قت * ‎Ge‏ اول و ثا ‘
کشته شد .# ۱ ‎x‏ بکس 7 بی وسکون
گرشاسف ۱ -با فا . بروزن و معنی فا وفوقانی » بمنی‌طعنه است که زدن نیزه‌باشدب
‎aan‏ و سخنیرا نیز گویند که بعنوان سرزش کفته
کرشاسب است که نام پسراترد سونام‌یسرطهماسب ‎a‏ ۱ ۱
‎et‏ . . - | شود" - و بمعنی چرم و چنایت - و غرامت
‎ete 1"‏ وتاوان ومواخنت هم‌آمده است - وماض یکرفتن
‎Jes‏ چم ‎Jal‏ بروزن دلبال " | بهردومشی هم‌هت که کرفتارشدن وستدن‌باشد-
جانوری است که ‎TN‏ شفال ‎rae‏ | و یکه دانتن -رو سالش دادن - و ‎easly)‏
‏وازهر دراصیبی دارد؛ ویضی ‎MATIN AG‏ | ایکفت ودست ‎ath‏ درسازهای ذوی‌الاوتار ‎Las‏

‎Le‏ | تا ‎wl,‏ که از < شغال ‎ss‏ ء جرد
‎wy ad‏ ید د کری و موج‌دار وجوهردار بر گوش‌خورد- وبمعنی‌خوف
‎Sw y‏ الماعلم.

‎GT .‏ هر دو بنظر آمده است که ماه گرفتن
‎ea OF‏ دزن | ‎SPL‏
‎tt‏ وسین ‎thin‏ وبای ‎le Salted‏ | ۸ کم
است که پسر انرد - وم پسر طهماسپ باشد. گر قت کرشن » کنایه‌ازاءراض‌کردن

‏گر غصت ؟ - با ‎go‏ قطمدار بر وزن | باشد - و بمعتی مالش دادن سازهم هست بعنی

‏۱ - کرشامف ‏ کرشاسپ (ه.م.) ‏ ۴ - مخفف «ک رکه شفال » «فرهنگه نظام».

‏۴ - مشفف کرشاسپ ‎(pm)‏ ۴ - مبدل «برشت» ‎Com)‏ و رك : برغستوا .
۵ - مصدر مرخم »و سوم شخص مفرد ماضی از «گرفتن» . رك : کرفتن » گرفته .
‎٩‏ - ا زکرفت من زجان اسپرکنید کرچه اکنون هم ‎LOS‏ منید.

‏مولوی بلخی رومی از فول سلیمان 4 برسولان بلقیس « مثنوی ‎le‏ علاهء‌الدوله ص ۰۳۳4 «چاپ
لیکلسن » دفت چپارم ص ۳۱۸ ‎٩‏ . و ‎Ay‏ :گرفته , گرفته زدن .
گرشاه - رك :گلشاه .

‏بقیه از ‎dais Lisle‏ ۱۷۹۵
‎GEL‏ تازی است وچون در سخ خطی قدیم میان‌کاف (تازی) وکاف (یارسی) در نوشتن امنیازی
نمی‌نهادند , ممکن است که گویند کان باستانی ما هم در عهد خوبش کرشاسب يا کاف ( تازی )
استعمال کرده باشند» وحتی اپوالفدا آنرا « کرشاسف » ضبط کرده‌است . نامهدر گرشاسپ در اوستا
2( < اثرط < اترد | برهان قاطع درمتن‌همین‌صفحه] ) راو بقول‌بندهش پسرسام‌بس‌تو رکه
پسر ‎ble‏ پبر دورشاسپ ‎Sep‏ پسفربدون است» و طبق کرشاسپ ‎bb‏ اسدی کرش اسب
پسن ‎bul‏ پسر شم ( نام ) پسر طو رکه پمر شیدسپ پسرنور پسر جمشید . گرشاسب دراوستا
صفت 10808۷ - ‎ob Maire‏ شده بعنی لرهنش و هرد سرشت و بتعبیر دیگر ‎plo‏ و پپلوان.
همین صفت است که بمرور زمان تبدیل به «نریمان» شده و اسم خاص ‎(de)‏ کردیده + درفارسی
سام کرشاسپ ‎olay‏ . با سام ‎an Solas‏ دراوستا تسکی بنام #سونگرسکه» وجود داشته که
ف کرد ۱۵آن از کرشاسپ مفصلا سخن رانده , متأسفاً اين نك مفقود شده است اما خلاصة آن

‏درناعة پپلوی دینکرت صل4 از کتاب 4آهده است . رك : مزدستا ص 8۱۳ ببمد .

[pdf page 594]
—Avay—

کاری کرد نکه شمه لرزان بگوشآید ‎a.‏
‎of‏ ۱ © بروزن فرشته ۰ بمعنی‌طعنه
است که زدن لیزه - و گفتن‌سخنانبطریق‌سرزش
باشد ۴ - و بمعنی تاوان و غرامت هم هست -
وبمعنیلاف و ‎GIS‏ لیز آمده‌است- واسیر و ‎HIS‏
‏را لیز کویند؟ - ومردم خنیس وبخیل ومسك
را عم گفته‌الد - و هرچی که ‎oly‏ اومسدود ‎oat‏

ک رکه

فارسی » حیوالیر! کوب دکه کر داشته باشد ۵
یعنی‌جرب داشته باشد وآن جوششی‌است باخاری
بسیار - وبضم اول ممروف است ۷ . کوبند اگر
‎SS‏ را به ترديك دهی در زیر ‎NS‏ کنندهیچ
```


## [2026-09-06T16:22:44.986Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\n# find pdf page 554 block\nm=re.search(r'\\[pdf page 554\\](.*?)\\[pdf page 557\\]', t, re.S)\nprint(m.group(1)[:5000] if m else 'nope')\nEOF",
 "description": "Print BQT v3 pdf pages 554-556"
}
```


### [2026-09-06T16:22:46.703Z] TOOL RESULT

```
۷۷ات

‎ML‏ - بنتح اول وسکون ثالی وکاف»
معروف است که‌برادر شیش باشد ‎٩‏ . گوبندعس
‎oly LT‏ برپنج روز لمیشود و عربان برغوث
خواشنش - بکسراول وسکون ‎tt‏ بمعنی‌مردم
است که آدمی ‎Fash‏ - و مردمك چتم؟ راهم
میگوشد ۴ - ‎IgG,‏ وفتح‌ثالیناممیوه‌است
-واسبیرا نیز گوبند کهآبی‌رنگه باشد - وبه‌منی
کربه هم‌آمده است که عربان سنور خوانندش .

‏کیکاوس؟ = بمعتی عادل و ‎Jeol‏
‏ونجیب باشد چه کی بمعنی عادل وکاوس بمعتی
‎Jeol‏ ونجیپ همآمده است- ونام مکی از چهار
پس کیقباد است .

‏کيكدر پاچه افکندن ‎AS,‏
‏در پازه افکندن ر کيك درشلوار
‎cade» el‏ کنابه ازاخطرابوبیطاقتی
وبیقراری کردن ومططرب ساختن باشد .

‏کیکن = ‎GS‏ اولوکاف وسکون‌تانی
ونون ۰ ‎ine‏ تاریکی باش د که درمقابل‌روشنایی
است 9 - ولحیم را نیز کوندوآن چیزیت که

‏(۱) چش : کیکیس .

‏بدان طلا وفره و امثال آنرا بهم پیوندکنند ؛
‎Gy‏ اول وفتح ثالث هم ‎nk‏ معنی وهم‌بمعنی
اول آمده است که تاریکی باشد .

‏کیکیر- ‎oh‏ اول بر وزن زنجیر ۰
بمعنی تره ‎Sad‏ باشد وآن سبزبی‌است خوردلی
وبعربی جرجیر گوبند ‎٩‏ ؛ وباین معنی‌بکراول
وزای ‎abit‏ دار هم بنظر آمده است .

‏کیکیش(۱) = بنتح‌اولابروزن‌دروش,
پمعنی کیکیر است۷ که نره‌تيزك باشد؛ وبکسر
اول ‎e‏ آمده ات

‏کیل- بکر اول و فتح ‎sll‏ وسکون
لام ۰ نام میوء‌یست صحرائی شبیه بآ لوچه وسیب
‎the‏ وآنرا در خراسان علف شیران ز علف
خری کویند وبعریی زعرور ودرخت آنرا شجرء
الدب خوانند ‎A‏ - وکیل سرخ نیز گوبندش »
وبعضی گوبند زعرور بونالی است دعر یی اداعلپ
ویک اول وسکون ثالی: بممنی خمیده و کچ

‏شده باشد ‎٩‏ وآرزومند و صاحب آرزو را لیز

‎-٩* a‏ وکلیم ویلای‌پوش راهم کفتماید.

‏۱ تهرانی کك (بفتح) , کردی ‎(ALS) kee‏ , لری 61 «ژابا ‎Hoty‏ .

‏۴ - ممال ‎Cea) or‏
بروز مع رکه بانکشت کر پدید ‎wT‏

‏۴ - از +کی (هیم.) ‎aE‏ (رك : کاووی) .

‎_f

‏« کیک وکالد » مردمك چشم بود...منجيكکوید:
زخشم (چشم. دهخدا) ب رکندازدو زکیك‌اهریمن.

‎cal ۶‏ فری ۲۵۷ ‎٩‏ .
۵ رك : رشیدی +

‏1 - ور جهانگیری ورشیدی « کیکیز» آمده :

‎slo oS‏ بنفشه بوی له کالوخ

‏کنده دهانی کرفی خای له کیکیز .
سوزلی سمرقندی «جهانگیری» «رشیدی» .

‏وچون مبدل ‎OT‏ * کیکیش» است ؛ میتوان کفت همین وجه صحیح است .

‏۷ -رك ‎“WSS:‏
‏حود کفتة بسحاقکو بگوی‌جواب

‎Com) ‏كيلك < کیلو‎  كلایک‎ A

‏که‌پیش ما کیل وبه بهم نخواهدماند*
«بسحاق اطلعمه . دیوان چاپ استالبول ص۲۹۰ .

‎. ‏تنم بسان خلال آمد از خیال خلیل‎ ee ‏از هوای‎ eT ve ‏دلم‌بسان‎ - ٩

‏بت ی که فدش چون قول عاشق ‎wT‏ راست

‏مهی که‌قولش‌چون پشت عاش قآمد کیل:

‏قطران تبریزی «رشیدی» و فس دیوان قطران چاپ نخجوالی ۰۲۱5

‎. ‏رك : سروری » رشیدی‎ NP
[pdf page 555]
کیلك ۱ ‎Ge‏ اول و قح ثالی
‎GE OK ps els‏ » بسنی اول ‎SASS‏
‏عطف شیران وزعرور باشد .

Wh ‏بررزن یزبان » چوبی‎ OLS
‏ماحل‌دربای خزر يابندکهدربای‎ wy &, he
‏و(۱)‎ wabys : ‏وآن دوفم میباشد‎ AS
wool gil Ko ‏دفع کدودانه و امراض‎ cot
- ‏از کندها هم هست‎ sy

کیلو. بکس ارل وفتح الی ولام‌بواو
کفیده. طف شیران وعلف خرس را کویندوآن
میومایست صحرائی شبیه بیب کوچك و آلوچه
وعربان زعرورخوانندشی؟ - وسکون‌نانی؛استض
وتلاب راگوند ۴ .

کیلواس؟ ‎b>‏ سین ‎thie‏ بر وزن
‎yt‏ , م شهری است که تولد خاکمونی()
که ‎sla‏ کفر# ‎ate‏ ییغمبر صاحب کتاب است

و۷
‎le‏ شده .
کیلوس؟ = بنتح اول بروزن‌مضوی»
ییونانی بمعنی پخته ورسیده باشد وباصطلاح‌اطبا
اولین طبخیرا کوبندکه ‎USE‏ در ممده می‌بابد.
کیله = پروزن حیله ؛ پیمانه ای باشد
که بدان غله وآرد وچیزهای ‎Go‏ پیمایندا -

"وبپندی میوه‌ایست که عربان مو زکوبند .

ote ‏بکس اول بر وزن‎ - SS
‏نواری‌باشد چه نکه‌بربالای‎ of, ‏بالاتنك را کوبند‎
‏بار الاغ واستر کشند ۷ -ونام شهری‌است‌ازدشت‎

قیچاق ۸ - ونام دربایی هم هست - و ‎pile‏ اول

حم ‎onl‏ معنی وهم بمعنی قیماق باش دکصرشیر
‎cel‏ .

‎Sas One Jus‏ » جالوری‌است
که از پوستش پوستین سازند ‎Ol‏ پوست نکبود
‎GB,‏ میباشد ویختر ‎sled‏ شروانآورنب٩‏

‎. ‏خم ۱ : شامکولی‎ (YD

‏۴ کید(هم)
رک ‎Scales‏ این لفط کتابی ‎Gace‏ است. ودر

‏(۱) چش : - و.

‎(pa) SS
. ‏سقی: کولاب «رشیدی»‎ ۴
‏اسل «کیلای» بوزن وسوای است وبشین ممجمه یز صحیح است » وآن لام کوهی است عظیم»‎ .
» lle ‏وباغتفاد يك فرقه از هندوان مسکن « میادیو » فام شخصی است که موکل است برفتای‎
‏تیمن نام شهری بیز کنند لیکن تهبرآن وزن که ساحب‌برها نکفته ؛ ونیز کاری‌به‎ had Ss
Xulds ‏فدارد . «سراجاللفات بنقل فرهنگه نظام ج ه ص م۰ - © - ازیونانی‎ gS
‏عساره ومایم) ودر طب عبارتست ازاستحالةٌ کیموی بعد از‎ pines) ‏و اسکات» «اشتینگاس»‎ Ju
. ‏دیگری شبیه یکشتاب «تفس»‎ Se ‏خروج‌آن ازممده بمعاء دقیق ؛ بجوهر‎
‏(عر) «کیل بالقتح » پیماله ... کیله بالکر پیمایش .» «منتهی الارب» -کیله در‎ - 0
. ‏پیمانه است «فرهنگه نظام*‎ nee ‏فارسی ماخوة از عریی‎
MS ‏دوال‎ Sy ‏کار هش که آهن‎ org ‏در کار و‎ - ۴
. ‏سوزلی سمرقندی #رشیدی»‎
‏آوناحیتی است مشرق‌اوجنسی‌از‎ coat . ‏مخن الدر ناحیت کیماك وشهرهای وی‎ «- ۸
‏ومغرب وی بسنی از خفجاخت و جضی وبرالی‎ SET ‏خرخیزست وجنوب وی رود ارتشست ررود‎
‏شهرست وبس 6 لندرو قبیله‌های بسپارست و مردماش‎ Ch ‏است که ابشادرا‎ tel only ... ‏شمال‎
‏خوار وآب میغزار تابتان وزمستان ...«حدودالمالس۵۳».‎ LS ‏آندر خز کله نشینند و کردهاندیر‎
. ‏ز کیمال وبور‎ « Gilby ‏ز سنجاب‎
‏فردوسی طوسی «رشیدی».‎

‎٩‏ - همه ‎GU‏ مك وموی سمور

‏ورك : فهرست ولف .
[pdf page 556]
-۱۷-

کیمخت ‎Le‏ اول وضم ثالث‌بروزن
مییخت. معروفت وآن‌یوست کفل وسافری‌اسب
وخراست که بنوعی خاص ‎MES cake‏ » وبعضی
گوبند کمخت دانهایی است که
میباشد - و پوست ترفجیده ودرهم کشیده را یز
گویند ۰

کیمخت ماه - بکر فوقانی و میم
بالف کشیده وبپای زده 6 کنابه از آسمان است
ویعربی سما خوانند .

کیمسس = بفتح اول وضم تالت‌وسکون
سین بی‌ق
```


## [2026-09-06T16:22:47.366Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^ *[0-9]\\+ *'ks\\|'ks \" SOD_pages.txt | head -20; echo \"=== try ks ===\"; grep -nE \"\\b(\\\\\\\\?'ks|ks)\\b.*(thin|small|weak)\" SOD_pages.txt | head -20; echo \"=== search 'weak' ===\"; grep -n \"small, weak\\|thin, small\" SOD_pages.txt | head",
 "description": "Grep Sogdian for ks"
}
```


### [2026-09-06T16:22:47.950Z] TOOL RESULT

```
=== try ks ===
=== search 'weak' ===
```


## [2026-09-06T16:22:57.708Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/BQT/BQT_v3_pages.txt',encoding='utf-8',errors='replace').read()\nm=re.search(r'\\[pdf page 556\\](.*?)\\[pdf page 558\\]', t, re.S)\ns=m.group(1)\ni=s.find('کیمیا')\nprint(s[max(0,i-2500):i+2500])\nEOF",
 "description": "Find kimiya entry in BQT"
}
```


## [2026-09-06T16:22:58.889Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -nE \"^\\s*(32|195)\\s\" SOD_pages.txt | head -20; echo \"=== ks entries ===\"; grep -nE \"^\\s*[0-9]{1,4}\\s+.?ks\" SOD_pages.txt | head -20",
 "description": "SOD entries 32 and 195"
}
```


### [2026-09-06T16:22:59.846Z] TOOL RESULT

```
-۱۷-

کیمخت ‎Le‏ اول وضم ثالث‌بروزن
مییخت. معروفت وآن‌یوست کفل وسافری‌اسب
وخراست که بنوعی خاص ‎MES cake‏ » وبعضی
گوبند کمخت دانهایی است که
میباشد - و پوست ترفجیده ودرهم کشیده را یز
گویند ۰

کیمخت ماه - بکر فوقانی و میم
بالف کشیده وبپای زده 6 کنابه از آسمان است
ویعربی سما خوانند .

کیمسس = بفتح اول وضم تالت‌وسکون
سین بی‌قطه » نام مردی بوده *

کیموس؟ = بقتح‌اول بروز نکیلوس»
بلفت ‎Gilly‏ بمعنی دوباره پخنه‌باشدوان دوسین
طبخی است که غذا در ‎So‏ مییابد .

کیهو فستن ۲ ۰ یکی اول و نون
وسکون سین بی‌قطه وفتح فوقالی ونون ساکن»
‎cal‏ زد وپازند بمعنی خواستن وطلبیدن‌باشد.

کیمیا؟ بکر اول و ثاك بر وزن
سیمیا . ‎gine‏ مکر وحیله ‎ath‏ و عملی است
مشهور تزد ‎el‏ صنمت که بسبب امتراج روح
وف اجاد ناقصه را ‎Saye‏ کمال رسانند بعنی
قلعی ومس را نقرء وطلاکنند و چون این عمل

در آن پوست

۱ -صبح ازحمایل فلكآهیخ‌خنجری

کین‌سپاوش

خالی از حیله ومکری بست از اين جهت باین
نام خوانند -ونظر پیر ومرشدکامل‌رانزگوینب
و عشق و عاثقیراکیمیا و کیمیا گری گوبنه -
وارزیزرا ی زکفه‌اند که بعربیرصاص‌خواننده +

‎Gar‏ جان » بکر بای حطی
وجیم بالف کشیده و بنون زدء .کنایه از شراب
انگوری باشد .

‏کین - بکر اول وسکون تحتالی‌ولون»
بمعنی کینه است که عدارت و ‎fats‏ باشد ۷
ومخفف که این هم هت ‎Ty‏ بالفحم لوسند
‎oh‏ صورت «کاین؟ +

‎SES‏ - بروزن ‎IS‏ » مردم شراب
خور وبدست را گوشد.

‎push op STMT
۰ ‏است از سی لسن پارید - ونام تولبی هم‌هست‎

‏کین توز۷ - با تای قرشت بر ‎Oi‏
‎ings‏ » اين لفت مر ‎AS‏ از کین و توز
پمعنی کینه کش و صاحب کینه که تلافی کنندء
بدی باشد چهکین بمعنی کینه و توز بمعنی
کشیدن آمده است .

‏کین‌سیاوش - بکر ‎ah wos‏
یستم است از ‎the‏ سی لحن بارید۰

‏کیمخت کوه ادبم شد ازخنجر زرش.
«خاقالی شروالی ص ۲۲۰.

‎De ‏ودرطب‎ (epee Le ‏ازیونالی 6007165 «لیدل‌راسکات»«اشتیتگاس»(بمعنی‎ - ۴

‏طمام است در معده بمد ‎Fi‏ هم بجوهری دیگ رکه ماده‌ای غلیظ مایل برنگ زرد ‎ath‏ «تفی».

‏۴ مز ‎nastan,kéménistan ,kiménostan‏ — (خواستن) ‎“Ve Gy?‏
ظ . مصحف ‎kamidan = cog kdmastan‏ (خواستن) . رك : باروچا ص۲۹۲.

‎alchimie: 5. «pis ‏«اشتینگای» (بممنی‌اختلاط وامتراج)‎ xémela sb y jl -

‎. (eS!) chemistry « (3) chimie .(5)

‎aS - 6‏ در برهان بمعتی ارزی زکه

‏بعربی رصاص ‎a‏ نیز آورده . واين ‎QE‏ از غرابت ست» > ‎Jay big‏ فرهنکه نظام

‎“puree

‏۱ کینه » اوستا - 68602 «بارتولمه ۷ ۹ پهپلوی ‎SF yas? KED‏

‏ص ‎DOTA‏ منای +۷ * « اسشق ۸۸۱ ۰ کردیع 10 , بلوچی 2080 (دشمنی, کینه)
«اسشق ‎aay‏ ارمنی ع 668 ( کینه , دشمنی ) » افتانی ع 108 ‎2S)‏ ورزی ‏ مداوت )

‎RAN ‏«هویشمان‎

‏- از: کین (ه.م.) + توز (نوزدم) .
[pdf page 557]
‎“Ss‏ « پروزن سینه » بمعئی‌یمپری
و عداوت و آزارکیرا ‎Jo»‏ پوشیده داشتن
باشد .
‎THES‏ - بس یکین ایرج ات
که نام لحن نوزدهم باشد از سی لحن پاربد .

‎is‏ سیاوش ۰ بمنی کین میاوش
است که ‎ob‏ لحن بستم باشد ازسی‌لحن ‎teak‏ .

‏کینه کش؟ = بفتحکاف وسکون شین
قطه دار » تلافی کنندة بدی- باشد - و نام روز
درازدهم است از ماههای ملکی .

‏کینه‌ور ۴ صصاحب کینه‌وصاحب‌عداوت
ویی‌مهر_باشد .

‏کیو بنتم اول بر وزن عدو » بمعنی
کاهو باشد وآن ‎Soules‏ خورند وبعربی‌خس
خوانند ۴ - و بممنی ماده و سبب و علت هم
‎Pos‏ .

‏کیوان ‏ بر وزن ایوان . تام ‎te‏
‏زحل است که در فلك حفتم میباشد ۱ - و فلك

‎Fla) ‏کی‎ ٩

‏وا
‏هقتم را ‎sag ps‏ - ویمعن یکمان هم آمده‌است
که بعربی قوس خوانند ‏

‏کیود! - بر وزن کبود » بمعنی آخر
کیواست که ماده و
```


### [2026-09-06T16:23:01.716Z] TOOL RESULT

```
3960:  32 "cYy B                                       fjLoU
4372:195 Vnc     M                               •U-ffAsiA<ljU              TSP 19.16
=== ks entries ===
4244:143 »ks»k => »k)ys>k
6074:                                                                831 >ks- B                                      *J^./<jy
6090:                                                                834 >ksn    B
6096:                                                                835 >kst-     M, S
12861:3198 ckst»k    B                             v^Hjju^j
12869:3199 ckst'k => ckst'k                                                   GMS 475, 1611; TSP 2.43, 340, 574, 69, 467
12870:3200 ckstwny M                                                           n pl69; MDii 1.1, 20; MSP b88
12877:3201 cksty     M =» ckst»k
17678:4906 ks'k =* »k>ys>k                                                   89526
17679:4907 ks'wrz'k M                        ^jj j ^ <e?jjj^
17694:                                                               4923 kst'yckry' B
17697:4912 ksn1 M                                 J^L^^Ui                 O1 17: Frag. Len. 92.17
17700:                                                               4925 kstr- B, M, S              ^jf ^     ^ <j^r/
17705:4913 ksn2 B                                        fS«JisJ          GMS 1280, 1300; Frag. Len. 44.6; STi 26.3, 13.2;
17712:                                                               4926 kstyc => kst'ych
17724:4916 kst- M, S, B                         j^f <j&f
17732:4918 kst'k B                             t4zj£ iC              4931 kt1 M, B                         (uj> s^ j>)S
28221:8491 rks B                                  jL^&l**--                       107
30386:9233 sks}>pt B                         J^ jy^> *oj&                skawe ? (sqwyy) ©<*(hi)$kuwaka        =»swkc\
30394:9234 sks'pt -* sks'pt
```


## [2026-09-06T16:23:17.250Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=6040 && NR<=6120' SOD_pages.txt; echo \"=== page tag ===\"; grep -n \"\\[pdf page\" SOD_pages.txt | awk -F: '$1<6120' | tail -3",
 "description": "Print Sogdian entries 831-835"
}
```


### [2026-09-06T16:23:18.954Z] TOOL RESULT

```
                                                                        sinner
795 >HRZY *± TRZY, 'XRZY(n)
                                                                        VJ; Frag. Len. 93.9; Hen. Magi. 138.38, ob. pi.
796 JJYyr- *» jYyr-
                                                                          -k*ryty\ GMS 1125; 'krt'nyk'r'y, VJ 758, 994
797 *jmnyh M =» jmnw
                                                                    814 Wnyk'rch S                                  jfj,
798 'jw'nty => jw>ndy(y)
                                                                        (o)krtam-karc ©f. adj, ^qt'nyq'rc, qt'nyq'ry
799 >jwn M                                                              sinner
                                                      !j<JJj
      azon     (*j}wny, 'j'wwny)   =^*jwn                               BBB 101 e22; Hen. Magi. 138.35; GMS 1125



                                                       a-"-
'krt'rzt'k

                                                                                                                            32
 815 'krt'rzt'k B                                     L^.Suir    827 'krty'kh      S                                fluf .xj-*
      Okr^rztk) ^krt'rzt'w                                           (a)krtyak
      absolutely                                                     sin, evil deed
                                                                     Sund. MHC p27.10
      TSP 6.188, 14.14 n p203; Benv. Notesiv 496;
                                                                 828 >krty>kryyh      M
        Mack, n p50, 22 BSTBL
 816 »krt'rzt'w    B                                UiW              (o)krtya-kare                                  15^'lM*

      ^krt'rzt'k                                                     performer
                                                                     Hen. Sogdica. 55.14 p57
      absolutely
      BSTBL, Padm. 61, 67; Dhy. 22(N); TSP 6.28                  829 'krtyh     B, S =» }krty>

 817 'krt'rztk =* ^rl'rzt'k                                     830 'krtyy M => >krty, >krt>y
                                                                831 >ks- B                                      *J^./<jy
 818 'krt'sp's B                              ^LUUij,^!*,            (o)kasc, (o)kos(e)?      Oks}y) ©Av. kdrdsa-, Khwar
     (o)krt-sspas ©Pahl. krtsp*s                                       yks =*ks-    -
     obedient, dutiful
                                                                     small, thin
     BSTBL, Dhy. 7; Gersh. Sogd. Cpds. 140, 147
                                                                     GMS 1201; Benv. VJ n p94, 39d; Inst. >ks\ SCE
819 'krt'wcy B                                ju^" j>ju /un-           76; pi. >kstK VJ 1264; MSP bl58
    certainly
     BSTBL, Dhy. 400                                            832 >ks>y =* >ks-
                                                                833 >qsy C
820 >krt>y B, S                   (jy >^- j;)J^ <X                   a/akasc ?
    (o)krte Okrtyy, >krt'k, *krtkt 'ktyy, }qtyy) ©ace.               overseer
                                                                                                                     ^U* <^U»o
       ykrt\v\ f. >kr0   -^kty*, qty\ >krty, qty2                    BSTii 897.73; STSC 58; C2, 55R13
     action, deed                                                                                                    cJjO^j
                                                                834 >ksn    B
     TSP; Sogdica. 60; KG; MSP; BSTBL; STii 10.28;
       MD                                                            (o)kasn, ksan ? ©Skt. ksana =»ksn2
                                                                     time, moment
821 'krtch B, S                                        u*<jf         TSP 2.121 n pl70
    (o)krtc ©f. adj. ^kr^y
                                                                835 >kst-     M, S
    action, deed
     TSP 8.86-, VJ 1053; MDii; 'jfcrcfc, Frag. 5.10                  (o)kist, kost   =>qs-                           X. iir
822 >krtk => >krt>y                                                 GMS
                                                                    0<?)sow926; MDiii
823 >krtw ** >krt>y                                             836 »ksty(y) M
824 'krtwS'r-    B, S     (0>> >^^ jjJo^^i o^                        (o)kiste, koste
    (o)krtu-6ar OktwS'r-, 'kS'r-, qtJr-) ©perf . st.                 OcOsow, sowing, tilling
      =»>krt-, qG'r-                                                 BBB 570; Tales. 470.55; GMS 926, 931
     (to)do
     GMS 167, 877; BBB 518, 706                                 837 >ksyc M, C                              (£l <^1)J&
                                                                    akasec ? CksMc) ©Av. aka-           ^'xsyc
825 >krty B, S              (j^ ^~> Jj)l»J'ij-*<jf                  hook                                        >krt-.
    (a)krte Okrt'k, 'krtyy) ©ace. >krtw, f. }krt\ inf.              Hen. Sogdica. 30.11a
      >krty =*}kty\ 'krt'y                                      838 >kt- M, C
    action, deed
                                                                    (o)k(o)t Cqt-)        ©pt. st. =*kwn-
    VJ; TSP; BSTBL; SCE 475; STii; MDii; GMS 847;
      BBB 542                                                         krt-, qt-
                                                                                                             ^ ji)d^ to* J*
826 >krty) M, B                                                     0o)do, (r6»)become
                                               l^lo^X               GMS 144, 148, 578, 603
    (o)krtya Okrtyh) ©Skt. karman           ©f. n. =>>kty\
                                                                839 >qt- =¥ >kt-
      qty2, qty>
=== page tag ===
```


## [2026-09-06T16:23:27.685Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=17600 && NR<=17740' SOD_pages.txt | grep -n \"195\\|ks-\\|kasc\\|small\\|thin\" ; echo \"====\"; awk 'NR>=17640 && NR<=17700' SOD_pages.txt",
 "description": "Find SOD ks- entry page 195"
}
```


### [2026-09-06T16:23:29.191Z] TOOL RESULT

```
1: 195
31:     C2, 57R24: BSTii 904, 24; Benv. JA 1959, 133              4900 ks-      B                                     ^u^(>^
34:       karx-nyatakya     ©f. n. ^k^y                                  -(,)y; pi. >ksth pred. inst. >ks} =*'ks-
35:       numbness                                                     thin                                                           t^
105:                                                                    smaller, smallest
111:                                                                      "smaller one"
====
4886 -qry     C =» -k'r'k, Y^t'qry, Yw,nkr'k
                                                               4901 qsqnty C                    (v'>^^)OOiJ
4887 kry> B                             r&*oUj<c^                   kas- kande ©<kat+skand ^ktskn^k
     karya (qryO ©pi. kr*yh suff. ^kry'cyq                          devastated
     time, sequence, in turn
                                                                    STii 1.21; GMS 365 n 1; Hen. BBB p63.5.21
     BSTBL, Dhy.; Benv. Notesii 217, Notesiii 224;
       GMS 1120; MSP p47; STSC 143; Bailey.                    4902 KSP S                               <>»)«> jj' o'-^^
       Prolexis 40                                                  ary ©Idg.
                                                                    sum
4888 qry* M =» kry>
                                                                    Anc. Lett, ii 49, 52
4889 kry>cyq M
          acik =>kry>
     karyly                                      J^y Vu J      4903 KSP> S
     time
                                                                    nakrte ©Idg. ^n'krt'k
                                                                    silver
     n}kry}cyk "untimely" GMS 1014
                                                                    MD, Livsic. Osnovyy II p371
4890qryn> C                                     cXJ^s
     kare/ina ?                                                4904 kstr S
                                                                                                         Jj*^<jr*£ <jrlf
       scripture reading, lesson                                    kastar =»kstr-
       C2, 31V17: BSTii 893.17                                      less, inferior
4891 -kryny     M                                                   GMS 1300n 1; MDii p 126.2, 14
                                                 oXjS* ijtla
       karene (-qryny(y))     ©suff.                           4905 qs- C
       doer, maker
                                                                    ka/os    ©pres. St. =*kst-, qsy\ kyr-2
       GMS 1123; BBB b50; W-Li 36, 95; pi. -f, STii
                                                                    0o)sow
                                                                                                                       196
 ks>k

        3sg. opt. qsy, C2, 52R9 n p96
                                                                     Oo)sow
                                                                     STi 48.22, 47.17; S W, C2, 54R26 n p97; BSTii
4906 ks'k =* »k>ys>k                                                   89526
4907 ks'wrz'k M                        ^jj j ^ <e?jjj^
     ka/asa-warze (q^wrzyCy))                                  4920 kst'ych B                               cJ^iJjz£f
     cultivation, tillage, agriculture                              kasti/ec (qystyc, kstyc) =»kystyc
     BBB p72.570; GMS 147; Sogd. Cpds. 1945, 141h                   field, cultivation
       <*karsaw(a)-warz-, Gersh. AHM 157n                            TSP 3.213, 11.28; loc. -y, TSP 7.141
       <*karsa~warz; Gharib. SI 1994, 131-5                    4921 kst'yckr'k B                   Jjy.<tJj<J&^
4908 qsWzyty) »» k^wrz^                                             kostic- kare (kst'yckr'y) ^kst'ych
                                                                    farmer
4909 qsNvrzy(y) mrtyy M                                j^UlT
     ka/asawarze marti                                               Frag. 2a.8, 17, 21; abl. -\ Frag. 2a.ll; GMS 989;
     cultivator                                                        BBB p72, 570

                                 *                             4922 kst'yckr*y =* kst)yckr»k
        BBB 570                                                                                                 JJ '^JJj
                                                                                                                           ,utT
                                                               4923 kst'yckry' B
4910 qsd'r- =» qst>r-                                               kostic-karya
4911 qsn     M, C => ksn1                                           agriculture, sowing, cultivation, tillage
4912 ksn1 M                                 J^L^^Ui                 O1 17: Frag. Len. 92.17
     ko/asn (qsn) ©<karsn =»krsn
     appearance, shape                                         4924 qstr C =» kstr-              l»s
                                                               4925 kstr- B, M, S              ^jf ^     ^ <j^r/
```


## [2026-09-06T16:23:39.598Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt; do echo \"== $f شیمی ==\"; grep -n \"شیمی\" $f | head -5; echo \"== $f کریشنا ==\"; grep -n \"کریشنا\\|کریشن\" $f | head -5; done",
 "description": "Grep Mo'in for shimi and Krishna"
}
```


## [2026-09-06T16:23:39.987Z] TOOL CALL #24: Bash

```json
{
 "command": "ls data/verification/sources/refs/ | head -60; echo ---; grep -n \"OEW\\|FSD\" data/verification/sources/SOURCE_MATRIX.md | head",
 "description": "List refs dir"
}
```


### [2026-09-06T16:23:41.489Z] TOOL RESULT

```
== MON_part1.txt شیمی ==
750:نشانه آن در شیمی ۵۵است و آن به عقند ه 
837:این محلول نیز خواص شیمیایی آب ژاول را 
2088:مواد شیمیایی برای خاموش کردن حریق. 
2722:شیمیایی» کٌازی است ساده» بی‌ر نگك» بی‌بو 
4472:موجود است. نشانه ان در شیمی ۸۱,0۷ 
== MON_part1.txt کریشنا ==
== MON_part2.txt شیمی ==
7342:فسفریکك هستند و برای کودهای شیمیایی 
8336:شیمیایی سده‌ای است دارای جلای 
8529:شیمیایی میو آن ماده‌ای بنام کاپ‌سیسین یا 
18802:ایسنرو گاهی نام شیمیایی ک‌افئین را 
18840:ترکیب شیمیایی کافور 0۱۰۲۲۱۱0 می‌باشد و 
== MON_part2.txt کریشنا ==
```


### [2026-09-06T16:23:41.539Z] TOOL RESULT

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
---
190:- **FSD** — Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913,
191:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt`
192:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol2.txt`
193:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol3.txt`
194:  `/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol4.txt`
```


## [2026-09-06T16:23:48.183Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== FSD alchemy ===\"; grep -n -i \"alchemy\" FSD_vol1.txt | head -5; echo \"=== LKT alchimie/Chemie ===\"; grep -n -i \"alchimie\\|kimiya\\|kīmiyā\\|Chemie\" LKT.txt | head -10",
 "description": "Grep Funk&Wagnalls and Lokotsch"
}
```


### [2026-09-06T16:23:48.249Z] TOOL RESULT

```
=== FSD alchemy ===
7529:Pathol.  Pain  In  the  glands,  ad^e-nal'gyf. —   Ad^e-nan-  lard.  2.  Fatness.  3.  Alchemy.  X   he  last  ot  any  liquid tbe'ra,  n.  A   genus  of  East-Indlnn  trees  and  shrubs  of  the  to  distil  over.  [L.,  grease.]
11252:to,  or  produced  by  means  of  alchemy.
11256:al'che-mist,  1   al'ki-mist;  2   ftl'ce-mtst,  n.  One  who  was skilled  in  or  who  practised  alchemy.
11258:al'clie-mlst-erf;  al'chy-mlstt.—  a!wcho-inls'tIc,a.  Of  or pertaining  to  alchemy  oralchemlsts;  practlslngalchemy.  al"- che-mls'tl-calt;  al"chy-mls'ticj.  —   al"che-mls'ti-cal- ly,  adr.—  al-chem'Is-try,  n.  Alchemy.  al-chym'Is-tryt.
11266:Some  lexicographers  derive  this  word  from  the  Greek Chemcta,  Egypt  (in  ancient  Egyptian,  IChem-l).  According to  Plutarch,  Egypt  was  thus  called  on  account  of  the  black color  of  its  soil.  But  ns  alchemy  signifies  the  transmuta- tion of  metals  and  the  quest  of  the  Elixir  Vitro,  which  arts were  not  practised  in  ancient  Egypt,  this  word  is  more  prob- ably derived  from  the  same  Egyptian  source  ns  chemistry. Amelia  B.  Edwards  Letter  to  .Standard  DM.  Oct.  23,  1891.
=== LKT alchimie/Chemie ===
2452:Tüttasche,  Aschensalz';  mit  ar.  Art.  in alle  europäischen  Sprachen  als  Fach- ausdruck der  Chemie  übergegangen:  sp. pg.  alcali,  frz.  alcali,  als  alchemistischer Ausdruck  algali  'Salpeter',  dial.  (Süd- frankreich) caliou  'Asche  aus  den  Reb- stöcken', engl,  alhdi,  dtsch.  Alkali  usw. Auch  der  Namen  des  Elementes  Kalium, Calium  gehört  hierhin,  [Devic  DEt  7. Lammens  Rem  7.
2718:Od.  klmt,  kopt.  kemi  'schwarz'  war  die Bezeichnung  des  Landes  Ägypten  [dar- aus auch  der  Name  des  dritten  Nach- kommen Noas,  Harn  'der  Schwarze', hebr.  allerdings  in  'der  Heiße'  umge- deutet] ;  hieraus  entstand  ar.  ktmija' zunächst  zur  Bezeichnung  des  'Steins der  Weisen'  [also  im  Sinne  von  ikslr, s.  hier  Nr.  903,  gebraucht,  vgl.  GILDE- MEISTER in  ZDMG  XXX,  534/538], dann  'Scheidekunst,  Chemie'.  Aus  dem Ar.  kommt:  it.  alchimia  'Goldmacher- kunst' [fast  synonym  zu  inganno  'Be- trug'], alchimia  'ein  aus  Messing,  Kupfer und  Erz  zusammengesetztes  Metall', modern  chimica,  arte  chimica  'Chemie', frz.  alnhimie,  chimie,  sp.  pg.  alqtdmia; dtsch.  Alchimie  [für  Alchimisterei  heißt es  bei  Schuppius  zur  Verspottung  dieser Afterwissenschaft  ungemein  treffend : 'Allkühmisterei',  vgl.  Andresen  DVE  34], Chemie,  ndl.  alchimie,  engl,  alchemy,  al- chimij,  Vb.  to  alchemise,  chimistry.  — [Die  ar.  Lexikographen  leiten  ar.  kimija' vom  Vb.  kamä  'verbergen'  ab,  also  im Sinne  von  'verborgener  Kunst'.]  [POTT in  ZDMG  XXX,  6/20.  Mahn  EtUnt  81/85. Devic  DEt  7.    Kluge  10.
2880:[Über  aram.  kuhlä  vielleicht  aus  ass. guhlu  ZAkkFW"  61]  'Spießglanzpulver (Schwefelblei)  zum  Färben  der  Augen- brauen, Wimpern  und  Lider'  [über  den Gebrauch  und  die  Zusammensetzung  der orientalischen  Augenschminke  vgl.HlLLE in  ZDMG  V,  236/242];  noch  im  16. Jahrhundert  ist  das  hieraus  entstandene Wort  Alcohol  in  der  Alchemie  der  ge- läufige Ausdruck  für  'trockenes,  feines Pulver',  erst  später  wurde  es  zur  Be- zeichnung des  Weingeistes  benutzt.  Die einzelnen  Formen  sind:  sp.  pg.  alquifol, alcofol,  alcofor,  alcohol,  kat.  alcofoll, frz.  alquifoux,  coheul,  alcohol,  it.  alcool, rum.  alcool;  ndl.  alkohol,  engl,  alcohol, dtsch.  Alkohol;  russ.  alkogoV.  —  [Pers. und  tk.  heißt  die  Augenschminke  übrigens sürme,  subst.  Inf.  des  tk.  Vbs.  siirmek 'glätten'  vom  Slamme  seb,  sit<>,  süp  'glatt,
5708:.4?awrtc  St.  75 Albatros  1)88 Alchabor  St.  12 Alchimie  1157 Aldebaran  St.  451 Aleppin  792 Algebar  St.  629 Algebra  631 Algedi  St.  035 Algenib  St.  664 Algomeiza  St.  749 ^Z^^oZ  St.  741 Algorab  St.  754 Alhabor  St.  12 Alhajoth  St.  41 Alhidade  896 Alizarin  116 Alkakandschi  1016 ^ZA-«?i  1029 ^/fro/io?  1227 Alkoran  1250 Alkoven  1221 ^/^«/t  59 Alleluja  793 alligaßr  mhd.  2229 Abnagest  1348 Almanach  1389 Almemor  j.  1461  a Alphard  St.  587 Alpherath  St.  586 Alpheraz  St.  586 Alpheta  St.  574 ^/<«/r  St.  1575
5767:j.  858 Chemie  1157 Cherub(in)  1165 C7««/fon  1893 Chonta  j.  805
6240:alchimie  1157
```


## [2026-09-06T16:23:57.929Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11258,11270p' FSD_vol1.txt",
 "description": "Read FSD alchemy etymology"
}
```


### [2026-09-06T16:23:57.985Z] TOOL RESULT

```
al'clie-mlst-erf;  al'chy-mlstt.—  a!wcho-inls'tIc,a.  Of  or pertaining  to  alchemy  oralchemlsts;  practlslngalchemy.  al"- che-mls'tl-calt;  al"chy-mls'ticj.  —   al"che-mls'ti-cal- ly,  adr.—  al-chem'Is-try,  n.  Alchemy.  al-chym'Is-tryt.
-   —   -   “   *   To
[Sp.]  A   magistrate  in  a   Spanish  or  Spanish- American  - .   . .   .   -
pueblo  or  town,  corresponding  to  a   Justice  of  the  peace;  al'che-mlze,  1   al'ki-maiz;  2   51  ce-miz,  rf.  [Hare.] later,  a   chief  magistrate  or  mayor,  ns  in  California  In  transmute  as  by  alchemic  art.  aPche-mlseJ.
1848-1849.  al-cade'J.—  al-eal'd e-shlp,  n.  Darkly  brown  thy  body  is.  Till  the  aunahine  striking  this,
Civil  and  criminal  justice  was  administered,  in  the  first  in-  Alchemize  its  dullness.  _ etance,  by  the  alcaldes,  or  municipal  judges  of  towns.  E.  Bbownino  To  Flush,  My  Doo  st.  o.
Hallam  Middle  Ages  pt.  ii,  ch.  4,  d.  213.  [n.  1854.1  al'chc-my,  1   al'ki-mi;  2   al'ce-my,  n.  1.  The  immature al"cal-dl'a,  1   fll'kal-dl'a;  2   Ul'cal-dl'a,  n.  [Sp.]  1.  The  office  chemistry  of  the  middle  ages,  characterized  by  the  pur-
suit of  the  transmutation  of  base  metals  into  gold,  and the  search  for  the  alkahest  and  the  panacea.
Some  lexicographers  derive  this  word  from  the  Greek Chemcta,  Egypt  (in  ancient  Egyptian,  IChem-l).  According to  Plutarch,  Egypt  was  thus  called  on  account  of  the  black color  of  its  soil.  But  ns  alchemy  signifies  the  transmuta- tion of  metals  and  the  quest  of  the  Elixir  Vitro,  which  arts were  not  practised  in  ancient  Egypt,  this  word  is  more  prob- ably derived  from  the  same  Egyptian  source  ns  chemistry. Amelia  B.  Edwards  Letter  to  .Standard  DM.  Oct.  23,  1891.
Alchemy  .   .   .   was  generally  confined  to  tho  mystery  all  sought to  penetrate,  the  transmutation  of  metals  into  sold.
Hallam  Lit.  Europe  vo\.  i,  pt.  i,  ch.  2,  p.  110.  Jl.  n.  a   co.  1854.] 2.  Any  cunning,  mysterious,  or  preternatural  process of  changing  the  structure  or  appearance  of  things.
Thero  is  in  cenius  that  alchemy  which  convert-!  nil  metals  into gold,  Carlyle  Essays,  Schiller  in  vol.  ii,  p.  257.  [it.  M.  a   co.l And  e’en  the  spotless  robe  of  white.
Worn  overlong,  grows  dim  and  dun Through  the  strange  alchemy  of  light.
```


## [2026-09-06T16:24:07.169Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"chymeia\\|khymeia\\|chemeia\\|khemeia\" FSD_vol1.txt | head -10; echo \"=== chemistry ===\"; grep -n \"chem'is-try\\|chem'ls-try\" FSD_vol1.txt | head -5",
 "description": "FSD chymeia"
}
```


### [2026-09-06T16:24:07.246Z] TOOL RESULT

```
11274:<   Gr.  chcmeia,  for  chymeia,  infusion,  <   chci >,  pour.] The  variants  below  Include  only  such  as  have  been  used
=== chemistry ===
42048:bI"o-cen'tr!c,  1   bal’o-scn'tnk;  2   bfo-c&n'trlc,  a.  Regarding bi"o-chem'is-try,  1   boro-kem'is-tn;  2   bro-cSm'ls-try,  n. That  branch  or  chemistry  relating  to  vital  processes,  their mode  of  action,  and  their  products.  bI"o-clieni'Icst; bl'o~chem"y$.—  bI"o-chcm'lc,  a.  b   l"o- chem '1- calf.—
```


## [2026-09-06T16:24:14.884Z] TOOL CALL #28: Bash

```json
{
 "command": "head -40 tools/fetch_source.py",
 "description": "Inspect fetch_source.py"
}
```


### [2026-09-06T16:24:14.939Z] TOOL RESULT

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


## [2026-09-06T16:24:19.855Z] TOOL CALL #29: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/alchemy\" \\\n \"https://www.etymonline.com/word/alchemy\" \\\n \"https://en.wiktionary.org/wiki/gracilis\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B9%9Bsn%C3%B3s\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 260 verification: roots Kerk (gracilis) and Kers 2 (black/alchemy)\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-06T16:24:23.284Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/alchemy
/home/sfmqrb/git/rishe/data/verification/sources/web/b8da90ed83325b42.txt
### https://www.etymonline.com/word/alchemy
/home/sfmqrb/git/rishe/data/verification/sources/web/ed0657329df3c84e.txt
### https://en.wiktionary.org/wiki/gracilis
/home/sfmqrb/git/rishe/data/verification/sources/web/7f113cdd7caa3919.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B9%9Bsn%C3%B3s
/home/sfmqrb/git/rishe/data/verification/sources/web/41c36bbd30516b04.txt
```


## [2026-09-06T16:24:26.657Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== alchemy wikt ===\"; grep -n -A4 -i \"Etymology\" b8da90ed83325b42.txt | head -60",
 "description": "Read wiktionary alchemy"
}
```


### [2026-09-06T16:24:26.706Z] TOOL RESULT

```
=== alchemy wikt ===
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
--
183: Etymology
184- [ edit ] 
185-
186: Etymology tree
187-
188- Proto-Indo-European *ǵʰew- 
189-
190- Proto-Indo-European *-mn̥ 
--
457: Douglas Harper ( 2001–2026 ), “ alchemy ”, in Online Etymology Dictionary . 
458-
459- Retrieved from " https://en.wiktionary.org/w/index.php?title=alchemy&oldid=91185466 "
460-
461- Categories : English terms derived from Proto-Hellenic 
--
484: Pages with etymology trees 
485: English entries with etymology trees 
486- Pages using etymon with no ID 
487- Pages with entries 
488- Pages with 1 entry 
489- Quotation templates to be cleaned
```


## [2026-09-06T16:24:27.220Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== etymonline alchemy ===\"; sed -n '1,120p' ed0657329df3c84e.txt | grep -n -i \"alchemy\" -A6 | head -60",
 "description": "Read etymonline alchemy"
}
```


### [2026-09-06T16:24:27.280Z] TOOL RESULT

```
=== etymonline alchemy ===
1:URL: https://www.etymonline.com/word/alchemy
2-FETCHED: 2026-09-04T19:36:31Z
3-STATUS: 200
4:TITLE: Alchemy - Etymology, Origin & Meaning
5-
6:Alchemy - Etymology, Origin & Meaning 
7-
8- Search 
9- Log in 
10-
11- Columns 
12- Forum 
--
21: Origin and history of alchemy 
22-
23: alchemy (n.) 
24-
25: "medieval chemistry; the supposed science of transmutation of base metals into silver or gold" (involving also the quest for the universal solvent, quintessence, etc.), mid-14c., from Old French alchimie (14c.), alquemie (13c.), from Medieval Latin alkimia , from Arabic al-kimiya , from Greek khemeioa (found c.300 C.E. in a decree of Diocletian against "the old writings of the Egyptians"), all meaning "alchemy," and of uncertain origin.
26-
27- Perhaps from an old name for Egypt ( Khemia , literally "land of black earth," found in Plutarch), or from Greek khymatos "that which is poured out," from khein "to pour," from PIE root *gheu- "to pour" [Watkins, but Klein, citing W. Muss-Arnolt, calls this folk etymology]. The word seems to have elements of both origins.
28-
29- Mahn ... concludes, after an elaborate investigation, that Gr. 
30- khymeia was probably the original, being first applied to pharmaceutical chemistry, which was chiefly concerned with juices or infusions of plants; that the pursuits of the Alexandrian alchemists were a subsequent development of chemical study, and that the notoriety of these may have caused the name of the art to be popularly associated with the ancient name of Egypt. [OED]
31-
32: The al- is the Arabic definite article, "the." The art and the name were adopted by the Arabs from Alexandrians and entered Europe via Arabic Spain. Alchemy was the "chemistry" of the Middle Ages and early modern times, involving both occult and natural philosophy and practical chemistry and metallurgy. After c. 1600 the strictly scientific sense went with chemistry , and alchemy was left with the sense "pursuit of the transmutation of baser metals into gold, search for the universal solvent and the panacea."
33-
34- also from mid-14c. 
35-
36: Entries linking to alchemy 
37-
38- chemistry (n.) 
39-
40: c. 1600, "alchemy," from chemist + -ry ; also see chemical (adj.). The meaning "natural physical process" is from 1640s; the sense of "scientific study of the composition of material things and the changes they undergo" is by 1788. Chemistry in the European mind disengaged itself from alchemy in the mid-1600s; The Academy del Cimento was established in Italy in 1657, the Royal Society in London in 1660, and the Academy of Sciences in Paris in 1666.
41-
42- The figurative sense of "instinctual attraction or affinity" is also attested by c. 1600, from the alchemical sense.
43-
44- alchemical (adj.) 
45-
46: "relating to or produced by alchemy," 1580s; see alchemy + -ical . Related: Alchemistical (1550s); alchemically .
47-
48- alchemist 
49- alkahest 
50- chemical 
51- chemist 
52- *gheu- 
--
62: 1630s "dealing with occult science or alchemy," from Latin hermeticus, from Greek Hermes, god of science and art (among other...Hermes Trismegistos "Thrice-Great Hermes," who supposedly invented the process of making a glass tube airtight (a process in alchemy...
63-
64- refrigeration 
65-
66: late 15c., refrigeracion, "act of cooling or freezing," originally in alchemy, from Latin refrigerationem (nominative refrigeratio...
67-
68- quintessence 
69-
70: early 15c., quint-essence, in ancient philosophy and medieval alchemy, "a pure essence latent in all things, and the substance...Its extraction was one of the chief goals of alchemy....
71-
72- rotation 
73-
74: Used earlier in alchemy, "transmutation of the four elements into one another" (late 15c.)....
75-
```


## [2026-09-06T16:24:32.452Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '183,260p' b8da90ed83325b42.txt",
 "description": "Read wiktionary alchemy etymology"
}
```


### [2026-09-06T16:24:32.509Z] TOOL RESULT

```
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *ǵʰew- 

 Proto-Indo-European *-mn̥ 
 Proto-Hellenic *-mə 
 Ancient Greek -μᾰ ( -mă ) 

 Ancient Greek χῠ́μᾰ ( khŭ́mă ) 

 Proto-Indo-European *-h₂ 
 Proto-Indo-European *-éh₂ 
 Proto-Indo-European *-i-eh₂ 
 Proto-Hellenic *-íā 
 Ancient Greek -ία ( -ía ) 

 Ancient Greek χυμείᾱ ( khumeíā ) bor. 
 Arabic الْكِيمِيَاء ( al-kīmiyāʔ ) bor. 
 Medieval Latin alchēmīa bor. 
 Old French alkimie der. 
 English alchemy 

 From Old French alkimie , arquemie ( French alchimie ), from Medieval Latin alchēmia , from Arabic اَلْكِيمِيَاء ( al-kīmiyāʔ ) , from Ancient Greek χυμείᾱ ( khumeíā , “ art of alloying metals ” ) , from χύμα ( khúma , “ ingot, bar ” ) . Compare Spanish alquimia and Italian alchimia .

 Pronunciation
 [ edit ] 

 ( US ) IPA ( key ) : /ˈælkəmi/ 

 Audio ( US ) : ( file ) 

 Noun
 [ edit ] 

 alchemy ( countable and uncountable , plural alchemies ) 

 ( uncountable ) The premodern and early modern study of physical changes , particularly in Europe , Arabia , and China ; and chiefly in pursuit of an elixir of immortality , a universal panacea , and/or a philosopher's stone able to transmute base metals into gold , eventually developing into chemistry .
 1605 , Francis Bacon , The Advancement of Learning ‎ [1] , IV. (11) : And yet surely to alchemy this right is due, that it may be compared to the husbandman whereof Æsop makes the fable; that, when he died, told his sons that he had left unto them gold buried underground in his vineyard; and they digged over all the ground, and gold they found none; but by reason of their stirring and digging the mould about the roots of their vines, they had a great vintage the year following: so assuredly the search and stir to make gold hath brought to light a great number of good and fruitful inventions and experiments, as well for the disclosing of nature as for the use of man’s life. 

 2014 June 21, “Magician’s brain”, in The Economist ‎ [2] , volume 411 , number 8892 , archived from the original on 9 January 2025 : There were also letters to scientists and other scholars, pages of derivations of mathematics and physics formulae, and copious writings on alchemy and religion. [ … ] The [ Isaac ] Newton that emerges from the [ unpublished ] manuscripts is far from the popular image of a rational practitioner of cold and pure reason. The architect of modern science was himself not very modern. He was obsessed with alchemy . 

 The purpose of physical alchemy —as opposed to its various spiritual pursuits—was to treat the supposed leprosity of base metals such as lead , refining and purifying them into gold . 

 ( countable ) The causing of any sort of mysterious sudden transmutation .
 1599 (first performance), William Shakespeare , “ The Tragedie of Iulius Cæsar ”, in Mr. William Shakespeares Comedies, Histories, & Tragedies   [ … ] ( First Folio ), London: [ … ] Isaac Iaggard , and Ed [ ward ] Blount , published 1623 , →OCLC , [ Act I, scene iii ] : O, he sits high in all the people’s hearts:
And that which would appear offence in us,
His countenance, like richest alchemy ,
Will change to virtue and to worthiness. 

 1640 , George Herbert , Jacula Prudentum; or, Outlandish Proverbs, Sentences, etc. , in The Remains of that Sweet Singer of the Temple George Herbert , London: Pickering, 1841, p. 143, [3] 
 No alchymy to saving. 

 1667 , John Milton , “Book II”, in Paradise Lost.   [ … ] , London: [ … ] [ Samuel Simmons ], and are to be sold by Peter Parker   [ … ] ; [ a ] nd by Robert Boulter   [ … ] ; [ a ] nd Matthias Walker,   [ … ] , →OCLC ; republished as Paradise Lost in Ten Books:   [ … ] , London: Basil Montagu Pickering   [ … ] , 1873 , →OCLC : Then of their session ended they bid cry
With trumpet’s regal sound the great result:
Toward the four winds four speedy Cherubim
Put to their mouths the sounding alchemy ,
By herald’s voice explained; the hollow Abyss
Heard far and wide, and all the host of Hell
With deafening shout returned them loud acclaim. 

 1840 , Percy Bysshe Shelley , A Defence of Poetry ‎ [4] : [Poetry] transmutes all that it touches, and every form moving within the radiance of its presence is changed by wondrous sympathy to an incarnation of the spirit which it breathes: its secret alchemy turns to potable gold the poisonous waters which flow from death through life; it strips the veil of familiarity from the world, and lays bare the naked and sleeping beauty, which is the spirit of its forms. 

 2016 , Boris Johnson , (Please provide the book title or journal name) : There is such a rich thesaurus now of things that I have said that have been, one way or another, through what alchemy I do not know, somehow misconstrued, that it would really take me too long to engage in a full global itinerary of apology to all concerned. 

 ( computing , slang , countable ) Any elaborate transformation process or algorithm .

 Hypernyms
 [ edit ] 

 protoscience 
 pseudoscience 

 Derived terms
 [ edit ]
```


## [2026-09-06T16:24:42.408Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"=== gracilis ===\"; grep -n -i -B2 -A12 \"Etymology\" 7f113cdd7caa3919.txt | sed -n '1,80p'",
 "description": "Read wiktionary gracilis"
}
```


### [2026-09-06T16:24:42.501Z] TOOL RESULT

```
=== gracilis ===
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
71- Translations 
72-
73- 1.4 
74- References 
--
83-
84- 2.1 
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Adjective 
92-
93- 2.3.1 
94- Declension 
95-
96- 2.3.2 
97- Synonyms 
--
179- [ edit ] 
180-
181: Etymology
182- [ edit ] 
183-
184- From Latin gracilis ( “ slender ” ) . Doublet of gracile .
185-
186- Pronunciation
187- [ edit ] 
188-
189- ( Received Pronunciation ) IPA ( key ) : /ˈɡras.ɪ.lɪs/ 
190-
191- ( General American ) IPA ( key ) : /ˈɡræs.ə.lɪs/ 
192-
193- Noun
--
230- [ edit ] 
231-
232: Etymology
233- [ edit ] 
234-
235- From an Old Latin verb *graceō or *craceō ( “ to be meager, slim ” ) , from Proto-Indo-European *kerḱ- ( “ to become thin, to wane ” ) , related to Sanskrit कृश ( kṛśa , “ thin, lean ” ) , Lithuanian karštu ( “ to age ” ) , and Avestan 𐬐𐬆𐬭𐬆𐬯𐬀 ( kər ə sa , “ meager, lean ” ) .
236-
237- Also compare cracens ( “ slender ” ) and Proto-Germanic *hurhaz ( “ lean ” ) whence Icelandic hor ( “ emaciation ” ) .
238-
239- Pronunciation
240- [ edit ] 
241-
242- ( Classical Latin ) IPA ( key ) : [ˈɡra.kɪ.lɪs] 
243-
244- ( modern Italianate Ecclesiastical ) IPA ( key ) : [ˈɡraː.t͡ʃi.lis]
```


## [2026-09-06T16:24:43.609Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '1,140p' 41c36bbd30516b04.txt",
 "description": "Read PIE krsnos page"
}
```


### [2026-09-06T16:24:43.662Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B9%9Bsn%C3%B3s
FETCHED: 2026-09-06T16:24:23Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
```


## [2026-09-06T16:24:51.627Z] TOOL CALL #35: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3\" \\\n \"https://en.wiktionary.org/wiki/Krishna\" \\\n \"https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D9%85%DB%8C\" \\\n \"https://en.wiktionary.org/wiki/%D9%83%D9%8A%D9%85%D9%8A%D8%A7%D8%A1\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 260 verification: Kers 2 black -> Krishna; kimiya/shimi\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-06T16:24:55.612Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3
/home/sfmqrb/git/rishe/data/verification/sources/web/afb090ac5fb534f0.txt
### https://en.wiktionary.org/wiki/Krishna
/home/sfmqrb/git/rishe/data/verification/sources/web/ea65b2ead42a81c6.txt
### https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D9%85%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/e5a6f27be725d136.txt
### https://en.wiktionary.org/wiki/%D9%83%D9%8A%D9%85%D9%8A%D8%A7%D8%A1
/home/sfmqrb/git/rishe/data/verification/sources/web/117e4f05f5fdcf4a.txt
```


## [2026-09-06T16:24:58.642Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in afb090ac5fb534f0 ea65b2ead42a81c6 e5a6f27be725d136 117e4f05f5fdcf4a; do echo \"########## $f\"; grep -n -A14 \"^ Etymology$\" $f.txt | head -50; done",
 "description": "Read etymologies from batch 2"
}
```


### [2026-09-06T16:25:00.375Z] TOOL RESULT

```
########## afb090ac5fb534f0
244: Etymology
245- [ edit ] 
246-
247- Learned borrowing from Sanskrit कृष्ण ( kṛṣṇa ) . Doublet of कान्हा ( kānhā ) and किशन ( kiśan ) .
248-
249- Pronunciation
250- [ edit ] 
251-
252- ( Standard Hindi ) IPA ( key ) : /kɾɪʃnᵊ/ , /kɾɪʂɳᵊ/ , [kɾɪʃɳᵊ] , /kɾɪ.ʂəɳ/ , [kɾɪ.ʃɐ̃ɳ] 
253-
254- Adjective
255- [ edit ] 
256-
257- कृष्ण • ( kŕṣṇa ) ( indeclinable , Urdu spelling کرشن ) 
258-
--
314: Etymology
315- [ edit ] 
316-
317- Borrowed from Sanskrit कृष्ण ( kṛṣṇa ) . Doublet of कान्हा ( kānhā ) and कान्हू ( kānhū ) .
318-
319- Pronunciation
320- [ edit ] 
321-
322- IPA ( key ) : /kɾuʂ.ɳə/ 
323-
324- Audio : ( file ) 
325-
326- Hyphenation: कृष्‧ण 
327-
328- Rhymes: -ə 
--
559: Etymology
560- [ edit ] 
561-
562- Etymology tree
563-
564- Proto-Indo-European *(s)ker- 
565- Proto-Indo-European *kers- 
566-
567- Proto-Indo-European *-nós 
568-
569- Proto-Indo-European *kr̥snós 
570- Proto-Indo-Iranian *kr̥šnás 
571- Sanskrit कृष्ण 
572-
573- From Proto-Indo-Iranian *kr̥šnás ( “ black ” ) , from Proto-Indo-European *kr̥snós ( “ black ” ) .
########## ea65b2ead42a81c6
187: Etymology
188- [ edit ] 
189-
190- Etymology tree
191-
192- Proto-Indo-European *(s)ker- 
193- Proto-Indo-European *kers- 
194-
195- Proto-Indo-European *-nós 
196-
197- Proto-Indo-European *kr̥snós 
198- Proto-Indo-Iranian *kr̥šnás 
199- Sanskrit कृष्ण ( kṛṣṇa ) bor. 
200- English Krishna 
201-
########## e5a6f27be725d136
155: Etymology
156- [ edit ] 
157-
158- Etymology tree
159-
160- Proto-Indo-European *ǵʰew- 
161-
162- Proto-Indo-European *-mn̥ 
163- Proto-Hellenic *-mə 
164- Ancient Greek -μᾰ ( -mă ) 
165-
166- Ancient Greek χῠ́μᾰ ( khŭ́mă ) 
167-
168- Proto-Indo-European *-h₂ 
169- Proto-Indo-European *-éh₂ 
########## 117e4f05f5fdcf4a
161: Etymology
162- [ edit ] 
163-
164- Etymology tree
165-
166- Proto-Indo-European *ǵʰew- 
167-
168- Proto-Indo-European *-mn̥ 
169- Proto-Hellenic *-mə 
170- Ancient Greek -μᾰ ( -mă ) 
171-
172- Ancient Greek χῠ́μᾰ ( khŭ́mă ) 
173-
174- Proto-Indo-European *-h₂ 
175- Proto-Indo-European *-éh₂
```


## [2026-09-06T16:25:06.035Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### shimi\"; sed -n '155,215p' e5a6f27be725d136.txt; echo \"### kimiya arabic\"; sed -n '161,225p' 117e4f05f5fdcf4a.txt",
 "description": "Read shimi and kimiya etymologies"
}
```


### [2026-09-06T16:25:06.085Z] TOOL RESULT

```
### shimi
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *ǵʰew- 

 Proto-Indo-European *-mn̥ 
 Proto-Hellenic *-mə 
 Ancient Greek -μᾰ ( -mă ) 

 Ancient Greek χῠ́μᾰ ( khŭ́mă ) 

 Proto-Indo-European *-h₂ 
 Proto-Indo-European *-éh₂ 
 Proto-Indo-European *-i-eh₂ 
 Proto-Hellenic *-íā 
 Ancient Greek -ία ( -ía ) 

 Ancient Greek χυμείᾱ ( khumeíā ) bor. 
 Arabic الْكِيمِيَاء ( al-kīmiyāʔ ) bor. 
 Medieval Latin alchēmia 

 ▲ 

 Ancient Greek χυμείᾱ ( khumeíā ) influ. 

 New Latin chimia bor. 
 Middle French chymie 
 French chimie bor. 
 Persian شیمی 

 Borrowed from French chimie .

 Pronunciation
 [ edit ] 

 ( Iran, formal ) IPA ( key ) : [ʃiː.míː] 

 Readings

 Iranian reading ? 

 šimi

 Noun
 [ edit ] 

 Dari

 کیمیا 

 Iranian Persian

 شیمی 

 Tajik

 кимиё 

 شیمی • ( šimi ) 
### kimiya arabic
 Etymology
 [ edit ] 

 Etymology tree

 Proto-Indo-European *ǵʰew- 

 Proto-Indo-European *-mn̥ 
 Proto-Hellenic *-mə 
 Ancient Greek -μᾰ ( -mă ) 

 Ancient Greek χῠ́μᾰ ( khŭ́mă ) 

 Proto-Indo-European *-h₂ 
 Proto-Indo-European *-éh₂ 
 Proto-Indo-European *-i-eh₂ 
 Proto-Hellenic *-íā 
 Ancient Greek -ία ( -ía ) 

 Ancient Greek χυμείᾱ ( khumeíā ) bor. 
 Arabic كيمياء 

 Borrowed from Ancient Greek χυμείᾱ ( khumeíā ) , from χῠ́μᾰ ( khŭ́mă ) + -ία ( -ía ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /kiː.mi.jaːʔ/ 

 Noun
 [ edit ] 

 كِيمِيَاء • ( kīmiyāʔ )  f 

 chemistry 

 Declension
 [ edit ] 

 Declension of noun كِيمِيَاء ( kīmiyāʔ )

 singular

 basic singular diptote 

 indefinite

 definite

 construct

 informal

 كِيمِيَاء 
 kīmiyāʔ 

 الْكِيمِيَاء 
 al-kīmiyāʔ 

 كِيمِيَاء 
 kīmiyāʔ 

 nominative

 كِيمِيَاءُ
```


## [2026-09-06T16:25:20.893Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== BRT keresa ===\"; grep -n \"k9r9sa\\|kdrdsa\\|kǝrǝsa\\|karasa-\\|kərəsa\" BRT.txt | head -20; echo \"=== BRT Keresaspa ===\"; grep -n -i \"keresaspa\\|k9r9saspa\\|kdrdsdspa\\|Kdrdsaspa\" BRT.txt | head -10; echo \"=== BRT vazdah ===\"; grep -n \"vazdah\\|vazda-\" BRT.txt | head -10",
 "description": "Grep Bartholomae"
}
```


### [2026-09-06T16:25:20.973Z] TOOL RESULT

```
=== BRT keresa ===
9576:•  j.  "karasa-   m.  'Wegelagerer,   Strolch':  |     3i„d'.  —  ai.  krlZva-m.  EN. yat    ajasät  *:sasca''    *^ad5Jüsca    dalvtsca  ^      .  ,    „       ,  ,,  ,  .... ÄWr«,«««^  (sd.)  Yt7/.6;   -   aat  ^^^^ ;•]■  taäa- Adj  'gemacht,  fertig  :  z-^rfr^j.« -ySi  fraiar?nti  -sasca  gao0ins7a  (sd.)    N.   °^  bämmmvä  Yt/J-Mi  ^'tF5,  wo  *j««;
=== BRT Keresaspa ===
=== BRT vazdah ===
6313:•  j.  aSa'vazdah-  m.  £N.  zweier  Gläubiger: i)  t?tn  yazitita  'da  pü^rS  pourui>3xÜBis.. Yt5.72;  —  "danhS  pouruoäxstayana/te asaonö  Yt  y .  112.*'  2)  t^m  yazsnta  .. "dasca  (NS.)'>  %ritai^a  sayuMrSis  pu%ra Yt  5. 7  2 ;  —  'daahd  %ritake  *ssyu\dröU Yty.113.
9589:•  j,  karasa'vazdah-  m.  EN.  eines  Bruders  ,  äat  [mam]  *i'^>  arihsits  aslva0  aismanam
23242:•  g.  'vazdah-  Adj.  "beständig';  'äanhä *av!m  J>-J(sd.)  y.4Q. 10.
23887:•  j.  vohvazdah-  m.  EN.  eines  Gläubigen: ( 'datshs  katJus  asaonS  Yt,  13.  114. I      Statt  vahu-^azd'  geschr.;  S  368.  Iz.    —    Eig.
25196:ravazda-
```


## [2026-09-06T16:25:27.508Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"karasä\\|karasa\\b\\|karasa-\" BRT.txt | head -20; echo \"=== aspa EN ===\"; grep -n \"kar[a3]sa.spa\\|k.rasaspa\" BRT.txt | head; echo \"=== mager ===\"; sed -n '9570,9600p' BRT.txt",
 "description": "BRT karasa context"
}
```


### [2026-09-06T16:25:27.590Z] TOOL RESULT

```
9576:•  j.  "karasa-   m.  'Wegelagerer,   Strolch':  |     3i„d'.  —  ai.  krlZva-m.  EN. yat    ajasät  *:sasca''    *^ad5Jüsca    dalvtsca  ^      .  ,    „       ,  ,,  ,  .... ÄWr«,«««^  (sd.)  Yt7/.6;   -   aat  ^^^^ ;•]■  taäa- Adj  'gemacht,  fertig  :  z-^rfr^j.« -ySi  fraiar?nti  -sasca  gao0ins7a  (sd.)    N.   °^  bämmmvä  Yt/J-Mi  ^'tF5,  wo  *j««;
9589:•  j,  karasa'vazdah-  m.  EN.  eines  Bruders  ,  äat  [mam]  *i'^>  arihsits  aslva0  aismanam
=== aspa EN ===
=== mager ===
Aus    at.  Va«'^'-    (S  ^'^z).    wobei   der   NS. '  Yt.5.37.  ^5-^7, '5'38.44  ;— >'a/ Ä?(nänil.
«i>"/imitwirkie.— Pü.:-tflr/j''Jr.— ')  Anders|  dem    kirilii)  pu>ra   usjiaySHe   urvOxiayS
Dsa.  VglS. /.348.Vgl.V.6.45.  — sjNA.-äram.  j  •^uj^'a    /^flSf^t   anyö  .  ,  äat    anyS    ufarB.-
•  j,  karanavant- Adj.,  PPA.;  s.'kar-Tati\kairy3  yava  gaestis  gaöavarS  Y.g.io;  — No.  S.  kshrptm    .  .  yam   sämake  (sd.)    'pake   Yt
•  j.  kar«ma-  Adj.,  mit  star-  m.  'Stern-  y-6"i  136;  -  nairyain  kam.varAtJm  .. schnuppe"':  pairika  .  .  ya  slürä  -mJ  ^5  a/ffw^aira/ "/^w  YL  75.39;  — /«iW^am (NP.)  ^/tf«ft'  on/fl^j  a^w  asmanmca  "die  .J"?"'  *^q'iaili  (sd.)  upanhacat  ■'psm  V. y.  ...  die  als  Sternschnuppen  zwischen  /.9;"«y"«  aojishm  baväht  ya>a  'p^m Erde  und  Himmel  stürzen"  YLiy.S.  (statt  NS.)  Az.j.
Kg.  Bed.  und  Et.?>).    —    ')  Vgl.  Ggr.  OK.        *'    Er   ist  der  Sohn  ©ntos,    aus  der  Familie 311,  West  SEE.  4?.   161.    Wertlos  D st.  ZA.    der  .Sämn.    Seine  Taten  sind  Y.  9,  ii,  Vt.  5.  38, :;.  417.    —    ')  Angebl.  ' Wurmst erne',    lu  ai.    ^5-  z8,   rg.  38,  44    eriählt.    Weiteres  SBE.  t8. trma}-  m.  'Wurm'.    Zuletzt  GlrPh.  i  b.  297.    309  ""d  JusTt  NB.  l6l. .     „  ,,,,       -  „      ■  ,,         Komp. :  *>.4ii/-«fl-+<uA'-.  eic. 'des  Rosse  macer
•  j.  "karasa-   m.  'Wegelagerer,   Strolch':  |     3i„d'.  —  ai.  krlZva-m.  EN. yat    ajasät  *:sasca''    *^ad5Jüsca    dalvtsca  ^      .  ,    „       ,  ,,  ,  .... ÄWr«,«««^  (sd.)  Yt7/.6;   -   aat  ^^^^ ;•]■  taäa- Adj  'gemacht,  fertig  :  z-^rfr^j.« -ySi  fraiar?nti  -sasca  gao0ins7a  (sd.)    N.   °^  bämmmvä  Yt/J-Mi  ^'tF5,  wo  *j««;
(GP.)  VI  "gdisMnqm  {vä)  N.  2&;  -^«rV^  '     „"™  J:  /";";,  ^  -  Pü""  ^^rT""'  ^     ' ''
kava  haosrava  *t?m  's>tn  upa  tarn  cantam  *  ,  „  .     ,  ,       ,      ,
"dass  K.H.  (Herr  ward)  über  den  Wege- '  '  &  >^'?,  ^^^"-    "1.'^   (vorausgehendem)
lagerer  auf  der  Rennbahn"  Yt/5.77.      ;  Dat.  der  Person- 'zu  Gunsten,  um  -  wdlen,
Et.?    \^.  i>r»5nay--l    -    PÜ.    (lu   Yt.  //):    vff^geri  :   altlyS k' yaifgam  karapH  usixsca
iarsyäi,    (lU  N,  5j);    +iflfj>'jm,   {lu  N,  zfi):  ,  (sd.)   aes»m3i   data   Y.44.20.
*iarsyüiiAä.  —    S.  lU  kirisänay-.    —    ')  J  10  ,       Vgl.  ai.  kam    Praen.    (mit    vorausgeh.    Dat.),
ua.     NA,  falsch  hnc.  ,      ksl.  tu  Praen.  (mit  folg.  Dat.);  Bthu  KZ.  3^.
.  j.  'k»r,sa-  Adj.  'mager'.  '     "V?^"'  ^^^t-''  U^v^^'J";  f  *'"''■  '
KompA.  -  ai.  k^ä.  Adj.  "  ^'"  """^^tige  Et.  KZ.  ^.  497-
•  J.  karasaoxäan-  m.  EN.  eines  Gläu-,»  )■  kamcit  Adv.  j)  'in  irgend  einer bigen:  -inö  asaonS  Yt.l3.\Q\.  .  Weise'  (s.  a-d).  2)  'in  jeder  Weise' (s.  e),
Komp.:  »^kiriia-Aruxsan- ,  eig.  'des  Stiere  Stets  mit  Gen.  part.",  in  auffällig  freier mager  sind'.  syntaktischer  Verwendung'';  a)  als  Subj.:
•  j,  karasa'vazdah-  m.  EN.  eines  Bruders  ,  äat  [mam]  *i'^>  arihsits  aslva0  aismanam
UiaitizedbyVjOOQlC
471
ka,m<Ht  b
paiii.baraüi  "irgend  einer  der  Mensch- heit .."  Y.1S.22; — yaj  k°  vä  laoxmanam paradr^ytiti  .  ,  ainyS.tkaSsa  (sd.)  "wenn sonst  einer  aus  der  Verwandtschaft  stirbt.." V.i2.2i.  b)  2\%0\)\.:  frabaraiti  bari-
ktm  vä  .  ,k°  vä  ..  vrvaranam  V.  75. 1 4 ;  — baröis  safim  (sd.)  vä  .  .  k'  vä  xräidis- manam  ". ,  oder  sonst  irgend  ein  Trumm harte'r  Erde"  V.p.ii;  —  äat  hl  mma fradaihyi  .  .  älrfjlaÄyUm  vä  k'  vä  älr?.- dätahe  (sd.)  nqma  ".  ,  oder  sonst  irgend ein  mit  Ätar  in  Beziehung  gesetztes  Wort als  Namen"  V,  1Ä52.  c)  als  Gen.:  upa aitsm  mnämm  baolayqn  uruämayä  vä  .  . k°  vä  hubaoifjitfmanqm  urvaranqm  "..mit- telst Urv.  .  .  oder  mittelst  sonst  irgend einer  der  wohlriechendsten  Pflanzen"  V, Äs.  d)    als   Lok,:    «päca    kl  gätäm
baraym  (sd.)  *n3m5.vantähva  k'  vä  star»- taisinqm  (sd.)  V.i^.^y,  —  k'  vä  *aip- yanqm  Yt.  4. 5;  5^,  e)  als   Instr, :   äat
ha  druxs  avästryeite  (sd.)  k'  i/J*'  vaca-\ nhqm  ". .  mit  (bei)  jedem  der  Worte"  V.p. , 13,       Undeutlich:  k'  vä  vaxsiSam  N.p^.  1
ASf.(?)  aus  ka:  —  Pü.:  kaiärH  i. '—  O  Und (ausser  V.  iS.  2a,  Yt.  4.  5')  stets  mit  folgen- dem  va;  %.  aber  No.  4.  —  »)  Einigennassen vergleichbar  ist  der  Gebrauch  d«s  nhd.  Ad- verbs  so  als  ErsaW  des  Relativs,  —  3)  So  L  4, K  I ;  NA.  kimiil.  —  *)  Hier  wird  i-J  lu  strei- chen sein;  Pü.  (blos);/a  kat-trü  l  gäwVstt.       |
•  j.  ka,saoya-"  Adj.  (fem.  'yä-)  ^Werayak- 1 n.  oder  ap-  f.  Name  des  Ä7OTfi«-Sees*' : a:^ar}t»m  s^ar^nS  .  ,  yal  upanhacailt  ys\ avizoät  fraxsayäte  yaia  zrayS  yat  'saim'^  ■ haitumahm  ". .  den  (Jeden)***,  der  von dorther  seine  HerrschaJft  entfaltet,  wo  der . vom  Haitutnant[_-'¥\\iss.)  gebildete  See  K.  1 ist"  Yt. /p.66; — yat  astvat.srilS  fraxiläile' haca  apal  "jacjd^  Yt /p.92*"*'; — yahmät^ *us.sayäiti  saosyas  .  .  haca  apat  °saoyät^ V./5.5"".
•)  Vgl.  Stein  IA.  15.  21.  Er  liegt  nach  Bd. /J,  16  pa  saiasIStt  'in  SaisiJn'.  —  •')  Aus  dem An'ischen  Königshaus,  als  dessen  Heimat  das Gebiet  des  A:-Sees  gilt,  Bd.  31.  7.  —  ••*)  Im See  K.  ruht,  von  gg^jgg /ra&awy  bewacht,  der Same  des  Zara%uitra,  aus  dem  dereinst  die Saoiyanl  entstehen  sollen,   vßl.  unter  xsudru-'i. ,
Wohl  Ableit.  aus  'i^iar.-  EN.    —    Pü.:   Sf  i.
```


## [2026-09-06T16:25:45.071Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=9540 && NR<=9600' BRT.txt | grep -nE \"^[0-9]{3}$\"; echo \"--- nearby numeric markers ---\"; grep -nE \"^ *4(6|7)[0-9] *$\" BRT.txt | awk -F: '$1>9400 && $1<9700'",
 "description": "Find Bartholomae column numbers"
}
```


### [2026-09-06T16:25:46.779Z] TOOL RESULT

```
52:471
--- nearby numeric markers ---
9463:463
9533:467
9591:471
9631:473
9634:474
```


## [2026-09-06T16:25:48.116Z] TOOL CALL #41: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/km#Egyptian\" \\\n \"https://www.iranicaonline.org/articles/karsasp\" \\\n \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%85%DB%8C%D8%A7\" \\\n \"https://en.wiktionary.org/wiki/chemistry\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 260: Egyptian km black; Garsasp; kimiya Persian; chemistry\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 3"
}
```


### [2026-09-06T16:25:55.279Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/km#Egyptian
/home/sfmqrb/git/rishe/data/verification/sources/web/fbec95ef82a4cda2.txt
### https://www.iranicaonline.org/articles/karsasp
/home/sfmqrb/git/rishe/data/verification/sources/web/a718649123cd692d.txt
### https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%85%DB%8C%D8%A7
/home/sfmqrb/git/rishe/data/verification/sources/web/3f9f50602eaacca6.txt
### https://en.wiktionary.org/wiki/chemistry
/home/sfmqrb/git/rishe/data/verification/sources/web/78014817590e6aa9.txt
```


## [2026-09-06T16:26:00.823Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### egyptian km\"; grep -n -i -A8 \"Egyptian\" fbec95ef82a4cda2.txt | grep -n -i \"black\\|Etymology\\|Afro\" | head -20; echo; grep -n -B2 -A10 \"Proto-Afroasiatic\\|black\" fbec95ef82a4cda2.txt | head -40",
 "description": "Read Egyptian km"
}
```


### [2026-09-06T16:26:00.885Z] TOOL RESULT

```
### egyptian km
16:99- Etymology 1 
26:347- Etymology 1
71:580- perfective active participle of kmm : black 
118:703: Egyptian terms inherited from Proto-Afroasiatic 
119:704: Egyptian terms derived from Proto-Afroasiatic 

560- [ edit ] 
561-
562: From Proto-Afroasiatic *kum- ( “ to be black ” ) .
563-
564- Pronunciation
565- [ edit ] 
566-
567-   ( reconstructed ) IPA ( key ) : /ˈkuːmaw/ → /ˈkuːmaw/ → /ˈkuːmə/ → /keːm/ 
568-
569- ( Old Egyptian , c. 2350 BCE ) IPA ( key ) : /ˈkuːmaw/ 
570- ( Middle Egyptian , c. 1700 BCE ) IPA ( key ) : /ˈkuːmaw/ 
571- ( Amarna-period Late Egyptian , c. 1350 BCE ) IPA ( key ) : /ˈkuːmə/ 
572- ( Late Egyptian , c. 800 BCE ) IPA ( key ) : /keːm/ 
--
578- [ edit ] 
579-
580: perfective active participle of kmm : black 
581-
582- Inflection
583- [ edit ] 
584-
585- Declension of km (perfective active participle)
586-
587- masculine
588-
589- feminine
590-
--
701- Egyptian transitive verbs 
702- Egyptian terms with quotations 
703: Egyptian terms inherited from Proto-Afroasiatic 
704: Egyptian terms derived from Proto-Afroasiatic 
705- Egyptian adjectives 
706- Egyptian participles 
707- egy:Colors 
708- Indonesian lemmas 
709- Indonesian pronouns 
710- Indonesian text messaging slang 
711- Indonesian abbreviations 
712-
```


## [2026-09-06T16:26:02.299Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -5 a718649123cd692d.txt; echo ---; grep -n -i \"Kərəsāspa\\|Keresaspa\\|lean horse\\|Garšāsp\\|Garsasp\" a718649123cd692d.txt | head -20",
 "description": "Read Iranica Karsasp"
}
```


### [2026-09-06T16:26:02.352Z] TOOL RESULT

```
URL: https://www.iranicaonline.org/articles/karsasp
FETCHED: 2026-09-06T16:25:54Z
STATUS: 200
TITLE: KARSĀSP - Encyclopaedia Iranica

---
57: KARSĀSP , Av. Kərəsāspa, Pahlavi various forms (see below), Pers. Garšāsp (Garšāsb, Arabicized Karšāsf), Avestan dragon-slayer, son of Sāma, and eschatological hero. In the Pahlavi and Zoroastrian Persian traditions, several heroic feats are connected with him. In the Šāh-nāma and early historiography, he is a bleak figure, but then again becomes a hero, to whom Asadi Ṭusī devoted the Garšāsp-nāma , and founder of Sistān.
59: On parallels between the Ferēdūn and Karsāsp myths, see also Wikander, 1941, pp. 161-70. On this and on Wikander’s (1938) attempt to connect Kərəsāspa with the “Aryan band of young men,” see Boyce’s criticism (1975, p. 102, n. 110).
60: Garšāsp has today become a popular Internet figure among Iranians and has given his name to a game.
61: The name . Av. Kərəsāspa probably means “he with meager horses”; cf. Old Indic kṛśvāśva (Mayrhofer, 1977, p. I/60), similar to Jāmāspa, “he with scrawny horses” (cf. Old Indic kṣāma “emaciated”). Pahlavi kars is used in the Zand ī Wahman yasn (3.15, 4.68) together with nizār “weak” as the opposite of frabih “fat” (Tafazzoli, 1990, pp. 56-58).
64: The change from Karsāsp to Garšāsp is problematic, but, conceivably, the name was influenced by Gar-šāh “king of the mountain(s),” epithet of Gayōmard (see GAYŌMART ; later usually understood as Gil-šāh “king of the clay,” i.e., of the earth; see Yarshater, 1983, p. 420). Note the combination of the stories of Garšāsp and Gar-šāh, e.g., in ms. MU29 (ed. JamaspAsa and Navābi, 1976; ed. Mazdāpur, 1378 Š./1999).
66: Descriptions . Kərəsāspa/Karsāsp is described in the Avesta as the strongest of strong men other than Zarathustra ( Yašt 19.38). This may be why Zādspram (35.6) measures him by Zarathustra’s size (compare Dârâb Pâhlan’s Ḵolāṣa-ye din , where God tells Zartošt that he weighed his soul [ ruḥ ] by placing it on one side of the scale and heaven and earth on the other, and it weighed more; text p. 50, paraphrase, pp. 68-69). In the Pahlavi texts, he is said to “have much strength” ( was-ōz [which also characterizes Dahāg]) or “be full of strength” ( purr-ōz ).
68: His standing Avestan epithet is naire.manah from * narya-manah “having a manly/heroic mind.” In the later traditions, Garšāsp, Sām, and Narīmān tend to split into two or three different characters, a development that had probably taken place by the third century, since, in the Manichean Book of Giants , the giant brothers Ohya and Ahya, sons of Šahmīzād, are called in Middle Persian Sām/Sāhm and Narīmān (in the Sogdian version, Sāhm and Pātsāhm; Henning, 1943, pp. 69-70; Skjærvø, 1995, pp. 198-203).
69: In the Avesta , Kərəsāspa had a brother named Uruuāxšaiia, about whom nothing much is said, other than that he was killed by Hitāspa but avenged by Kərəsāspa, who killed Hitāspa and dragged him after his chariot ( Yasna 9.10, Yašt s 15.28, 19.41).
70: Karsāsp’s heroic deeds . Two main narratives are associated with Kərəsāspa in the Avesta : the slaying of the three-horned dragon ( Yasna 9.11, Yašt 19, and elsewhere), on the back of which he cooked his noon meal (see Darmesteter, I, p. 89, for parallels), and various other monsters, and his slaying of Aži Dahāka (see below; see also AŽDAHĀ ). A short list is found in the Mēnōy xrad (26.49-53) in the section on the “benefits” ( sūd ) from various mythological characters (ed. Anklesaria, p. 91). Lists of his deeds are also included in the narrative of his crime against the fire (see below), which was part of the Sūdgar nask . A resumé of it is in the Dēnkard (9.15, ed. Vevaina, pp. 274-75), and the full story in the Pahlavi Rivāyat (chap. 18f). Other versions are found in several Zoroastrian Persian texts, including the Ṣad dar Bondaheš , chap. 20 (ed. Dhabhar, pp. 86-92; tr. in The Persian Rivāyats , ed., Dhabhar, 1932, 516-20; text in the Paris ms. suppl. persan 46, see Blochet, pp. 93, no. LXV; Bartholomae, 1915, p. *40) and the Dinkard-nāma (pp. 204-11); a versified version in the Paris ms. suppl. persan 38 (Blochet, p. 77, no. LI; Bartholomae, 1915, p. *26; reproduced in Spiegel, 1860, pp. 336-48); and a pseudo-Pahlavi version, probably translated from Persian into Pahlavi, in ms. MU 29 in the Meherji Rana Library (ed. Mazdāpur, 1378/1999, pp. 122-51; on the ms. see pp. 11-12 and JamaspAsa and Nawabi, eds., introduction). The list of feats in these late texts only partly overlaps that in Yašt 19.
71: According to Yašt 19, it was when the x v arənah had left Yima (see JAMŠID i. MYTH OF JAMŠID ) for the third time that it came to Kərəsāspa, enabling him to perform his deeds (see, e.g., Hintze, ed., 1994, pp. 212-35; Humbach and Ichaporia, eds., 1998, pp. 115-25). Similarly, according to the Dēnkard (7.1.32; Molé, ed. and tr., 1967, pp. 8-11), Karsāsp’s superior strength came from the “word,” which came to him as his share of the second branch or function ( pēšag ) of the dēn (and its xwarrah ), the warriors ( artēštārīh ), as part of Jam’s xwarrah (see ARTĒŠTĀR , CLASS SYSTEM ).
74: The Pahlavi Rivāyat and the Zoroastrian Persian texts then list his slaying of the (seven in the Ṣad dar ) giant highwaymen ( rāhdār ; 18f.68), which is connected with Yašt 13.136, where Kərəsāspa’s fravashi is invoked for withstanding the enemy army and various kinds of robbers ( gaδa ) and the evil they cause; the passage is cited by Zādspram (32.4), where (as elsewhere) the gaδa , Pahlavi gayg , is associated with the rāhdār . Last comes his pacifying of the fleet wind, which had been deceived by the dēw s to go after Karsāsp, which it did so violently that it threatened to destroy the earth, but Karsāspa persuaded it to do what it had been created to do: uphold heaven and earth (18f.20-23).
75: Karsāsp’s sins . Kərəsāspa is mentioned in the Videvdad (1.9) as being followed by the witch Xnąθaitī, who was fashioned by the Evil Spirit as the adversary of the land Vaēkərəta. The Av. pairikąm yąm xnąθaiti is rendered in the Pahlavi version as “witch-desire” ( parīg-kāmagīh ), interpreted as “idol-worship” ( uzdēs-paristagīh ), and Karsāsp is said to be its first practitioner. This exegesis is cited in the Bundahišn (31.17-18), where the “witch-desire” is said to be the same as Sām’s worship of the dēw s, although another authority says it referred to the sin of not tying the kusti ( wišād-dwārišnīh ).
87: Karsāsp in the eschatological narrative . There are a few references to Kərəsāspa’s eschatological functions in the Avesta . In Yašt 13.61, his body ( kərp ) is said to be guarded by 99,999 fravashis of the “sustainers of (the cosmic) order” ( a ṣ̌ auuan ). Manuščihr cites this passage in the Dādestān ī dēnīg (16.5).
97: Garšāsp in the Šāh-nāma . There are several references in the Šāh-nāma to the descent of Garšāsp from Jamšēd (see JAMŠID ). When Ferēdun answers his sons, who are unhappy about his patronage of Manučehr, he does it in front of his great army commanders, including Sām son of Narimān and Garšāsp son of Jamšēd (ed. Mohl, I, pp. 174-75 l. 721; ed. Khaleghi, I, p. 132, l. 692; tr. Warner and Warner, I, p. 212). Another reference comes much later in the book in the description of Kay Ḵosrow walking in the garden with the pahlavān s, Gudarz, etc., and Barzin, (son) of Garšāsp, of the seed of Jam (ed. Mohl, III, pp. 272-73, ll. 20-21; ed. Khaleghi, III, p. 289, ll. 21-22, where “Barzin and Garšāsp”; tr. Warner and Warner, III, p. 273; see BARZĪN ). Finally, in the episode where Esfandiār  scorns Rostam’s father Zāl  as being the brood of a dēv (see DIV ), Rostam answers that Dastān (i.e., Zāl) is the son of Sām, son of Narimān, son of Karimān, son of Hōšang  or Karšāsb, according to the manuscripts (ed. Mohl, IV, pp. 614-15, ll. 3037-39; ed. Khaleghi, V, p. 346, ll. 649-51 with n. 12; tr. Warner and Warner, V, p. 202), and his descent, Rostam adds, is from the loins of Sām and Jam (ed. Khaleghi, n. 14). Another, less explicit, reference to Karimān occurs after Rostam and Tahmina’s first amorous encounter, when Rostam prophesies that, if she has a boy, he will be as tall as Sām son of Narimān and as manly as Karimān (ed. Mohl, II, pp. 82-83, ll. 124-25; ed. Khaleghi, II, p. 124, ll. 87-88; tr. Warner and Warner, II, p. 125). Note also the episode in which Sām addresses the newly-crowned Manučehr, promising him his support, and cites his forebears “from Garšāšp to Narīmān” (ed. Mohl, I, pp. 214-15, ll. 39-40 [not in ed. Khaleghi, I, p. 164, where the two lines in Mohl are missing between ll. 38 and 39]; tr. Warner and Warner, I, p. 239). The story of Narimān is restricted to that of his death at Mount Sepand, told by Zāl to Rostam, before Rostam sets out to take it and thus appeases Narimān’s soul (ed. Mohl, I, pp. 364-67, ll. 1856-68; pp. 374-75, l. 1957; ed. Khaleghi, I, p. 277 in footnotes ll. 46-58, p. 280 in footnotes l. 147; tr. Warner and Warner, I, p. 329).
98: Another couple of references to Garšāsp are found in descriptions of the great ones of the realm, the pahlavān , in various situations. Those gathered to witness Ferēdun giving the throne to Manučehr include Qāren, Garšāsp, and “the son of Narimān” (= Sām; ed. Mohl, I, pp. 168-69, ll. 638-40; ed. Khaleghi, I, p. 127, l. 610 [with two lines less than Mohl, including the one mentioning Garšāsp]; tr. Warner and Warner, I, p. 207). In the description of Manučehr’s army, Garšāsp is assigned the command of the left flank and Sām and Qobād the right flank (ed. Mohl, I, pp. 182-83, l. 821; ed. Khaleghi, I, p. 138, l. 792; tr. Warner and Warner, I, p. 217).
99: More specific situations include Qāren’s seizure of the fortress of the Ālāns, where he goes along with Garšāsp, and Aḡriraṯ’s advice to his son Pašang after the death of Manučehr not to go for Nawḏar, but for Qāren and Garšāsp in order to please the souls of his ancestors (ed. Mohl, I, pp. 194-95, l. 951 and pp. 392-93, ll. 125-26; ed. Khaleghi, I, p. 146, l. 916 and p. 293, l. 109; tr. Warner and Warner, I, p. 345). In a description of Ferēdun’s court, with the king seated on his throne and Manučehr next to him, Garšāsp is mentioned among his ministers specifically as treasurer ( ganjvar ; ed. Mohl, I, pp. 178-79, l. 771; ed. Khaleghi, I, p. 135, l. 742; tr. Warner and Warner, I, p. 214), which recalls his position as vizier in the Muslim sources (see below).
100: In some manuscripts, a chapter is ostensibly devoted to the reign of Garšāsp, son and successor of Zav, but all that is said about Garšāsp is that he was born and, fifteen lines later, died (ed. Mohl, I, pp. 440-41, ll. 1-2, 15; ed. Khaleghi, I, pp. 329-30 in the footnotes after ll. 33 and 44; tr. Warner and Warner, I, pp. 374-75). The chapter is, in fact devoted to the rise of Rostam. It is fairly clear that the lines devoted to Garšāsp are secondary; note, in particular, that he, anacronistically, puts on the Kayanid crown ( kayāni kolāh ). As Ḵāleqi-Moṭlaq points out, the historians who relied on the Šāh-nāma also do not include Garšāsp’s reign (ed. Khaleghi, Notes , I/1, p. 366).
101: Karsāsp in mythological history and later historiography . In the list of the first four haoma -pressers in Yasna 9, Kərəsāspa’s father Θrita of the Sāmas is listed after the fathers of Yima and Θraētaona (see JAMŠID , FERĒDUN ), before Zarathustra’s father Pourušāspa. In Yašt 13 to the fravashis, Kərəsāspa’s fravashi is invoked after those of Manuš.ciθra and the kauui s (see FRAVAŠI , KAYĀNIĀN) and before that of Āxrūra (see above), son of Haosrauuah. In the Pahlavi texts, there is less consistency. In Dēnkard 7.1.31-33, he is placed between Mānuščihr and Kay Kawād, and, in Bundahišn 36.7, Sām is said to have ruled between (? andar ) Manuščihr and Uzaw and Kawād, but, in Bundahišn 35.32-33, he is listed with his father after Kay Husrōy and before Luhrāsp (see KAYĀNIĀN).
103: The early Muslim historians, approximately contemporary with the final redactions of the Pahlavi texts, also had difficulties fitting him into their chronologies. For instance, Ḥamza states briefly that Karšāsf reigned while Zav reigned (ed. Gottwaldt, p. 35; tr., p. 24), and Ḵᵛārazmi (pp. 99-100) says they shared the reign; Masʿudi ( Moruj II, p. 117) says that Manučehr (spelled Manušehr) was succeeded by Sahm, his great-great-grandson, and alludes to Sahm’s “long wars and reign.” According to Ṭabarī (ed. De Goeje, pp. 532-33; tr., III, pp. 115-16), Karšāsb was Zav’s vizier and the son of Aṯreṭ son of Sahm son of Narimān and descended from Afrēdun (Ferēdun). Ṭabari gives another genealogy, as well, which has him descended from Manučehr. He also stresses that, contrary to what some thought, he did not rule. Balʿami has Dastān son of Sām son of Narimān son of Garšāsp son of Barbeṭ (for Aṯreṭ; ed. Gonābādi, p. 133 [not in tr. Zotenberg, p. 104]) and merely mentions that he was Zav’s vizier and a descendant of Afrēdun (ed., p. 523, tr. Zotenberg, p. 406). Similarly, the Mojmal (p. 25) has Rostam son of Zāl son of Sām son of Narimān (with the daughter of the king of Meṣr) son of Garšāsf/Garšāsp (with the daughter of the king of Rum) son of Aṯreṭ; see also ibid., pp. 41-44, on the exploits of Garšāsp and Sām Narimān under Ferēdun, Manučehr, and Nawḏar.
104: According to Ṯaʿālebi (ed. Zotenberg, pp. 68-69)—who does not mention Garšāsp—Sām, son of Narimān, and father of Dastān/Zāl, was Manučehr’s main support, generalissimo, and guardian of his provinces and was nicknamed yal “hero” and pahlavān-e jahān , which Ṯaʿālebi rendered as “support ( ʿomda ) of the world.” He was governor of Sistan, Zābolestān, and the Indian provinces. Mirḵᵛānd has Sām as Manučehr’s governor of Nēmrōz, Kabul, Zābolestān, and the Indian provinces (ed. Kayānfarr, II, pp. 634-35; tr. Shea, pp. 166-67) and Garšāsb as Zāb’s fraternal nephew, his mother being a daughter of Benjamin, son of Jacob (ed. Kayānfarr, II, p. 658; tr. Shea, p. 205; note that the reign of Manučehr was thought to be contemporaneous with Moses, e.g., Ţabari, ed. De Goeje, p. 434; tr., p. 23; Masʿudi, Moruj II, p. 117). He also points out that, “in most histories,” Garšāsp’s rule marks the end of the Pēšdādiān dynasty.
```


## [2026-09-06T16:26:17.726Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD kars ===\"; grep -n -i \"karsāsp\\|kirsāsp\\|garsēwaz\\|kars \\|kirs \" PHD.txt PHD_mackenzie.txt 2>/dev/null | head; echo \"=== NYB ===\"; grep -n -i \"kirsasp\\|karsasp\\|garsewaz\" NYB_vol2_glossary.txt | head; echo \"=== HUB kimiya ===\"; grep -n -i \"kimia\\|kīmiyā\\|chemie\" HUB.txt HRN.txt | head",
 "description": "Grep Pahlavi dicts and Horn/Hübschmann"
}
```


### [2026-09-06T16:26:17.820Z] TOOL RESULT

```
=== PHD kars ===
=== NYB ===
=== HUB kimiya ===
```


## [2026-09-06T16:26:19.271Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### persian kimia\"; grep -n -A12 \"^ Etymology\" 3f9f50602eaacca6.txt | head -40; echo \"### chemistry\"; grep -n -A10 \"^ Etymology\" 78014817590e6aa9.txt | head -30",
 "description": "Read Persian kimia and chemistry etymologies"
}
```


### [2026-09-06T16:26:19.331Z] TOOL RESULT

```
### persian kimia
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 2 
71- Persian 
72-
73- Toggle Persian subsection 
74-
--
76: Etymology 
77-
78- 2.2 
79- Pronunciation 
80-
81- 2.3 
82- Noun 
83-
84- 2.4 
85- Noun 
86-
87- 2.4.1 
88- Inflection 
--
111: Etymology 
112-
113- 3.2 
114- Pronunciation 
115-
116- 3.3 
117- Noun 
118-
119- 3.3.1 
120- Related terms 
121-
122- Toggle the table of contents 
### chemistry
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Usage notes 
72-
--
224: Etymology
225- [ edit ] 
226-
227: Etymology tree
228-
229- Proto-Indo-European *ǵʰew- 
230-
231- Proto-Indo-European *-mn̥ 
232- Proto-Hellenic *-mə 
233- Ancient Greek -μᾰ ( -mă ) 
234-
235- Ancient Greek χῠ́μᾰ ( khŭ́mă ) 
236-
237- Proto-Indo-European *-h₂
```


## [2026-09-06T16:26:23.051Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('3f9f50602eaacca6.txt',encoding='utf-8').read()\ni=t.find('Persian\\n')\n# find the \"Etymology\\n [ edit ]\" occurrences and print following 12 lines\nimport re\nfor m in re.finditer(r'Etymology\\n \\[ edit \\]', t):\n    print('-----')\n    print(t[m.start():m.start()+700])\nEOF",
 "description": "Read all etymology blocks for kimia"
}
```


### [2026-09-06T16:26:25.139Z] TOOL RESULT

```
-----
Etymology
 [ edit ] 

 From Arabic كِيمِيَاء ( kīmiyāʔ ) , from Ancient Greek χῠμείᾱ ( khŭmeíā ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /ciːmjaː/ 

 Noun
 [ edit ] 

 Northern Kurdish

 kîmya 

 کیمیا ( kîmya ) 

 chemistry 

 Persian
 [ edit ] 

 Persian Wikipedia has an article on: کیمیا 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Borrowed from Arabic كِيمِيَاء ( kīmiyāʔ ) , from Ancient Greek χῠμείᾱ ( khŭmeíā ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /kiː.mi.ˈjaː/ 

 ( Dari, formal ) IPA ( key ) : [kʰiː.mi.jɑː] 

 ( Dari, formal ) IPA ( key ) : [kʰiː.mi.jɑː] 
 ( Kabuli ) IPA ( key ) : [kʰiː.mi.jɑː] 

 ( Hazaragi ) IPA ( key ) : [kʰi.mi.jɔː] 

 ( Iran, formal
-----
Etymology
 [ edit ] 

 Borrowed from Arabic كِيمِيَاء ( kīmiyāʔ ) , from Ancient Greek χῠμείᾱ ( khŭmeíā ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /kiː.mi.ˈjaː/ 

 ( Dari, formal ) IPA ( key ) : [kʰiː.mi.jɑː] 

 ( Dari, formal ) IPA ( key ) : [kʰiː.mi.jɑː] 
 ( Kabuli ) IPA ( key ) : [kʰiː.mi.jɑː] 

 ( Hazaragi ) IPA ( key ) : [kʰi.mi.jɔː] 

 ( Iran, formal ) IPA ( key ) : [kʰʲiː.mi.jɒː] 

 ( Tajik, formal ) IPA ( key ) : [kʰi.mi.jɔ] 

 Rhymes: -aː 

 Readings

 Classical reading ? 

 kīmiyā

 Dari reading ? 

 kīmiyā

 Iranian reading ? 

 kimiyâ

 Tajik reading ? 

 kimiyo

 Noun
 [ edit ] 

 Dari

 الخیمیا , کیمیا 

 Iranian Persian

 کیمیا 

 Tajik

 алхимия 

 ک
-----
Etymology
 [ edit ] 

 Borrowed from Classical Persian کیمیا ( kīmiyā ) , from Arabic كِيمِيَاء ( kīmiyāʔ ) , from Ancient Greek χυμεία ( khumeía ) .

 Pronunciation
 [ edit ] 

 ( Standard Urdu ) IPA ( key ) : /kiː.mɪ.jɑː/ 

 Noun
 [ edit ] 

 کیمیا • ( kīmiyā )  f ( Hindi spelling कीमिया ) 

 chemistry 

 ( historical ) alchemy , elixir 

 Related terms
 [ edit ] 

 کیمیائی ( kīmiyāī ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=کیمیا&oldid=90105648 "

 Categories : Central Kurdish terms borrowed from Arabic 
 Central Kurdish terms derived from Arabic 
 Central Kurdish terms derived from Ancient Greek 
 Central Kurdish terms with IPA pronunciation 
 Central Kurdish lemm
```


## [2026-09-06T16:26:35.592Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -o \"ALCHEMY[^ ]*\" AHD_watkins1985.txt | head; echo \"---\"; grep -n \"ALCHEMY\" AHD_watkins1985.txt | head -3 | cut -c1-400; echo \"=== gheu ===\"; grep -n \"gheu-\" AHD_watkins1985.txt | head -5 | cut -c1-600",
 "description": "AHD Watkins alchemy"
}
```


### [2026-09-06T16:26:35.661Z] TOOL RESULT

```
---
=== gheu ===
523:gheu-
524:gher-’. To shine, glow; gray. Hypothetical base of various Germanic forms. 1. Germanic *gréwaz, gray, in: a. Old English greg, gray: GRAY; b. probably Old English grighund, greyhound: GREYHOUND. 2. Germanic *gris- Jaz, gray, in: a. Old French gris (> French gris), gray: GRISAILLE, (GRISETTE), (GRISON), GRIZZLE; AMBERGRIS; b. Medieval Latin griseus, gray, grayish: GRISEOUS. [Pok. 3. gher- 441.] gher-4. To scrape, scratch. 1. Extended zero-grade form *ghr(e)-k- in: a. Greek kharax, a pointed stake, also a kind of sea bream: CHARACIN; b. Greek kharassein, to sharpen, notch, carve, cut: CHA
526:TRANSFUSE. II. Extended form *gheus-. 1. Germanic zero-grade form *gus- in: a. suffixed form *gustiz in Old Norse gustr, a cold blast of wind: cusT!; b. Icelandic gusa, to gush, perhaps akin to Middle English gushen, to gush: GUSH. 2. Germanic suffixed o-grade form *gausjan in Old Norse geysa, to gush: GEYSER. III. Suffixed form *gheu-ti- in Latin fatilis, “(of a vessel) easily emptied, leaky,” hence untrustworthy, useless: FUTILE. IV. Basic form *gheu- in Greek khein, to pour: CHOANA, CHYLE, (CHYME); CHOANOCYTE, ECCHYMOSIS, PARENCHYMA. [Pok. gheu- 447.] ghéu-. To yawn, gape. Compare 
1218:AEDILE aidh- AEGIS aig- AENEOUS ayes- AEOLIPILE pulé AEPYORNIS OrF- AERIAL wer-2 AERO- wer-2 AEROBE gWei- AERODYNE deu-2 AERONAUT nau-2 AESIR ansu- AESTHETIC au-5 AESTIVAL aidh- AETHER aidh- AFFABLE bha-2 AFFAIR dhé-1 AFFECT! dhé-1 AFFECT? dhé-1 AFFECTION dhé-1 AFFERENT bher-1 AFFIANCE bheidh- AFFIANT bheidh- AFFIDAVIT bheldh- AFFILIATE dhé(i)- AFFIRM dher-2 AFFIX dhigy- AFFLATUS bhié-2 AFFLICT bhiig- AFFLUENT bhleu- AFFORD pert AFFOREST dhwer- AFFRAY  pri- AFFRICATE bhréi- AFFUSION gheu- AFTER apo- AFTERMATH mé-4 AGAIN gagina AGAINST gagina AGALACTIA melg- AGAPANTHUS andh- AGE 
1356:CHIRO- ghesor- CHIRURGEON ghesor- CHISEL kaa-id- CHITTERLINGS ku- CHLOASMA ghel-2 CHLORITE! ghel-2 CHLORO- ghel-2 CHOANA gheu- CHOANOCYTE gheu- CHOICE geus- CHOIR gher-1
```


## [2026-09-06T16:26:43.423Z] TOOL CALL #48: Bash

```json
{
 "command": "for u in \\\n \"https://www.ahdictionary.com/word/search.html?q=alchemy\" \\\n \"https://vajehyab.com/moein/%D8%B4%DB%8C%D9%85%DB%8C\" \\\n \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D9%85%DB%8C/\" \\\n ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 260: AHD alchemy etymology; Moin shimi\" 2>&1 | tail -2; done",
 "description": "Fetch AHD and vajehyab"
}
```


### [2026-09-06T16:26:48.045Z] TOOL RESULT

```
### https://www.ahdictionary.com/word/search.html?q=alchemy
/home/sfmqrb/git/rishe/data/verification/sources/web/78cc85a6608f6b83.txt
### https://vajehyab.com/moein/%D8%B4%DB%8C%D9%85%DB%8C
/home/sfmqrb/git/rishe/data/verification/sources/web/a1bead9b4c213993.txt
### https://abadis.ir/fatofa/%D8%B4%DB%8C%D9%85%DB%8C/
/home/sfmqrb/git/rishe/data/verification/sources/web/3faffb13564b66d5.txt
```


## [2026-09-06T16:26:51.863Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### AHD\"; grep -n -i \"alchemy\\|Khemia\\|kimiya\\|khumeia\" 78cc85a6608f6b83.txt | head -20; echo \"### vajehyab\"; grep -n \"شیمی\" a1bead9b4c213993.txt | head -10; echo \"### abadis\"; grep -n \"شیمی\" 3faffb13564b66d5.txt | head -20",
 "description": "Read AHD and Persian dict pages"
}
```


### [2026-09-06T16:26:51.956Z] TOOL RESULT

```
### AHD
1:URL: https://www.ahdictionary.com/word/search.html?q=alchemy
4:TITLE: American Heritage Dictionary Entry: alchemy
6:American Heritage Dictionary Entry: alchemy 
47: 2. A seemingly magical power or process of transmuting: "He wondered by what alchemy it was changed, so that what sickened him one hour, maddened him with hunger the next" (Marjorie K. Rawlings). 
49: [Middle English alkamie , from Old French alquemie , from Medieval Latin alchymia , from Arabic al-k ī miy ā ' : al- , the + k ī miy ā ' , chemistry (from Late Greek kh ē meia , probably alteration of khumeia , from Greek khein, khu- , to pour; see gheu- in the Appendix of Indo-European roots (influenced, owing to the reputation of Egyptian alchemists, by Greek Kh ē mi ā , Egypt, from Egyptian kmt , Egypt, from feminine of km , black, in reference to the black soil of the Nile valley)).]
### vajehyab
4:TITLE: معنی شیمی | فرهنگ انتشارات معین | واژه یاب
9: معنی شیمی | فرهنگ انتشارات معین | واژه یاب 
17: شیمی
### abadis
4:TITLE: شیمی - معنی در دیکشنری آبادیس
6:شیمی - معنی در دیکشنری آبادیس 
10: شیمی
20: شیمی. ( فرانسوی ، اِ ) ( مأخوذ از کلمه «کیمیا» ) علمی است که در آن از خواص اجسام طبیعی و تغییرات عمیق گوهرها و عناصر بحث می شود. بنابراین علم شیمی وابسته به ساختمان نهایی ماده است و در آن می کوشند تا ماده را به کوچکترین اجزای وی تقسیم کنند و آنرا مورد مطالعه قرار دهند. این اجزا یا عناصر در مواد مختلف وجود دارند و با کمک شیمی معلوم می شود که یک قطعه سنگ آهک از یک فلز درخشان ( کلسیم ) و دو شبه فلز، یکی جامدو سیاه ( کربن ) و دیگری گاز ( اکسیژن ) بوجود آمده است. دانش شیمی تنها محدود به تجزیه کردن مواد نیست بلکه با ترکیب عناصر، اجسام پیچیده تری بوجود می آیند. این ترکیب عناصر یا اجسام را با یکدیگر فعل و انفعال شیمیایی نامند، مانند عنصر کلر که گازیست زرد متمایل به سبز، و آن خودبخود با عنصر فسفر که جامد است ترکیب و به کلرور فسفر تبدیل می گردد. از مجموع عناصر اساسی و مواد اصلی بسیط که تاکنون شناخته شده بیش از 100 عنصر را می توان نام برد. ( از فرهنگ فارسی معین ).
21:- شیمی آلی ؛ بحث ترکیباتی است که بدن گیاهان و جانوران را تشکیل داده اند و چون در ترکیب این اجسام همیشه مقداری کربن وجود دارد، این بخش از شیمی را شیمی ترکیبات کربن نیز می نامند. ( از فرهنگ فارسی معین ).
22:- شیمی معدنی ؛ بحث عناصر و ترکیباتی است که اکثر تشکیلات غیرزنده را بوجود می آورند و در حقیقت ترکیبات معدنی هستند و در ترکیب این مواد امکان دارد کربن نیز وجود نداشته باشد. ( از شیمی معدنی تألیف برّی چ دانشگاه ص 7 ). 
26: ( اسم ) علمی است که از خواص اجسام طبیعی و تغییرات عمیق گوهرها و عناصر بحث می کند بنابراین علم شیمی وابسته به ساختمان نهایی ماده است و در آن سعی میشود ماده را به کوچکترین اجزای وی تقسیم کنند و آن را مورد مطالعه قرار دهد . این اجزا یا عناصر در مواد مختلف وجود دارند . با کمک شیمی معلوم می شود که یک قطعه سنگ آهک از یک فلز درخشان ( کلسیم ) و دو شبه فلز : یکی جامد و سیاه ( کربن ) و دیگری گاز ( اکسیژن ) به وجود آمده است . دانش شیمی محدود به تجزیه کردن مواد نیست بلکه با ترکیب عناصر اجسام پیچیده تری به وجود می آورد . وقتی عناصر با هم ترکیب شوند ترکیبات شیمیایی به وجود می آیند . این ترکیب عناصر یا اجسام را با یکدیگر فعل و انفعال شیمیایی نامند مانند عنصر کلر که گازیست زرد متمایل به سبز و آن خود به خود با عنصر فسفر که جامد است ترکیب و به کلرور فسفرو تبدیل می گردد . از مجموع عناصر اساسی و مواد اصلی بسیط که تا کنون شناخته شده است بیش از ۱٠٠ عنصر را می توان نام برد . یا شیمی آلی . مبحث ترکیبات است که بدن گیاهان و جانوران را تشکیل داده اند و چون در سوختن این اجسام اگر اکسیژن به اندازه کافی نباشد مقداری کربن باقی می ماند این بخش شیمی را شیمی ترکیبات کربن می نامند . 
35:* شیمی آلی: (شیمی ) قسمتی از شیمی که دربارۀ کربن یعنی درمورد مواد اولیۀ حیوانی و گیاهی بحث می کند، شیمی کربن. 
39: شیمی ( در فارسی افغانستان و فارسی تاجیکستان: کیمیا ) ( به فرانسوی: Chimie ) شاخه ای از علم است که به بررسی عناصر، ترکیب های ساخته شده از اتم ها، مولکول ها و یون ها، ساختار شیمیایی، خواص و رفتار مواد و تأثیر مواد برهمدیگر و همچنین تغییراتی که یک ماده در حین انجام یک واکنش با مواد دیگر از خود نشان می دهد، می پردازد. 
40:در نمایی کلی از علم، شیمی در جایی میان رشته فیزیک و زیست شناسی قرار می گیرند. در واقع از شیمی به عنوان یک دانش بنیادی یاد می شود؛ به این خاطر که این علم، مفاهیمی را ارائه می کند که درک سایر زمینه های علمی چه در سطح پایه و چه در سطح کاربردی را ممکن می کند. برای مثال علم شیمی، جنبه های مختلفی از شیمی گیاهی «گیاه شناسی»، چگونگی تشکیل سنگ های آذرین «زمین شناسی»، چگونگی تشکیل ازون در اتمسفر و چگونگی تجزیه آلودگی «محیط زیست»، خواص خاک موجود روی ماه «کیهان شناسی»، چگونگی عملکرد داروها «داروسازی» و چگونگی جمع آوری دی ان ای در صحنه جرم به عنوان مدرک «جرم شناسی» را توضیح می دهد. 
41:علم شیمی به موضوعاتی مانند چگونگی برهم کنش اتم ها و مولکول ها از طریق پیوندهای شیمیایی و تشکیل ترکیبات شیمیایی جدید می پردازد. چهار نوع پیوند شیمیایی وجود دارد که ترکیبات مختلف دارای حداقل یکی از آنها هستند: پیوند کووالانسی، پیوند یونی، پیوند هیدروژنی - واندروالسی و پیوند فلزی. 
42:واژهٔ شیمی از کیمیا در زبان مصری باستان، کیمیا از واژهٔ خامه یا خَمِه به معنای زمینِ سیاه برگرفته شده است. پس از تسلط ایرانیان بر مصر در ۵۲۰ پیش از میلاد، این واژه به صورت کیمیا به شرق آمده است و پس از تسلط یونانیان در ۳۳۰ پیش از میلاد به صورت خومِیا ( به یونانی: χυμεία ) در یونانی نیز وارد گردیده است. در دوران تسلط خلافت اسلامی در خاور میانه، به صورت الکیمیاء درآمده است و با جنگ های صلیبی به صورت الشمی ( به انگلیسی: alchemy ) مجدداً است. در زبان فارسی، شیمی یک ترانویسی از برابر فرانسوی است و نخستین بار در سال ۱۸۳۱ توسط میرزا صالح شیرازی در یک رسالهٔ علوم طبیعی که خود وی مرقوم داشته بود به کار برده شد که بعدها در مدرسهٔ دارالفنون با عنوان «رسالهٔ طبیعیات» تدریس می گردید. 
43:کوشش های نخستین بشر برای فهمیدن طبیعت مواد و بیان چگونگی دگرگونی آن ها ناموفق بود. اندک اندک کوشش ها برای تبدیل مواد کم ارزش، به مواد ارزشمندی چون زر و سیم، منجر به پیدایی دانش «کیمیا» گردید. همچنین از دیگر اهداف علم کیمیا، می توان به ساخت داروی جاودانگی که به آن «اکسیر» می گفتند، اشاره کرد. به همین سبب، به کیمیا، علم اکسیر نیز می گفتند. هر چند در ظاهر دانش کیمیا به خواست اصلی خود نرسید، اما دستاوردهای کیمیاگران در این راه به اندوخته گرانبهایی تبدیل شد که پایه گذار شیمی مدرن گردید. [ ۱] کیمیاگری در بین النهرین، مصر باستان، ایران، هند، چین، یونان، روم، در تمدن اسلامی، و سپس در اروپا تا قرن ۱۹ – به صورت یک شبکه پیچیده از مکاتب و نظام های فلسفی در طول دست کم ۲۵۰۰ سال رواج داشت. [ ۲] 
44: wiki: شیمی 
46: شیمی (دامغان). شیمی یک منطقهٔ مسکونی در ایران است که در دهستان قهاب رستاق واقع شده است. [ ۱] براساس سرشماری مرکز آمار ایران در سال ۱۳۹۵، شیمی ۱۵۶ نفر جمعیت دارد. [ ۲] 
47: wiki: شیمی (دامغان) 
53: شیمی (chemistry)
55:شیمی آلی. شاخه ای از علم شیمی است که به بررسی ترکیبات کربن می پردازد.
56:شیمی معدنی. خواص، واکنش ها، و روش تهیه و توصیف همۀ عناصر و ترکیبات را، جز ترکیبات کربن، در این شاخه از علم شیمی بررسی می کنند.
57:شیمی فیزیک. به شرح کمّی پدیده های شیمیایی، واکنش ها، و اندازه گیری داده های لازم برای این توضیحات می پردازد. شاخۀ اخیر توجه ویژه ای به حرکت مولکول ها و تأثیر دما و فشار، غالباً در مایعات و گازها دارد.
```


## [2026-09-06T16:27:09.712Z] TOOL CALL #50: Bash

```json
{
 "command": "ls site/pages/260.jpg 2>/dev/null; pdftoppm -f 260 -l 260 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg260 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render pdf page 260"
}
```


### [2026-09-06T16:27:11.941Z] TOOL RESULT

```
site/pages/260.jpg
total 11784
drwx------ 7 sfmqrb sfmqrb    4096 Sep  6 12:27 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1332 Sep  6 12:27 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
-rw-rw-r-- 1 sfmqrb sfmqrb  181961 Sep  6 12:11 bqt1688_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb  340758 Sep  6 12:11 bqt1709_fn2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  280452 Sep  6 12:11 bqt1709_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49952 Sep  6 11:57 build234b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   32265 Sep  6 11:51 build234.py
-rw-rw-r-- 1 sfmqrb sfmqrb   24770 Sep  6 12:01 build243.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   15240 Sep  6 11:54 c246_caiique.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36354 Sep  6 12:02 c246_casaque.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84366 Sep  6 11:54 c246_n2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   51690 Sep  6 11:54 c246_n6.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13719 Sep  6 12:02 c248_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   30759 Sep  6 12:02 c248_p4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2750 Sep  6 12:02 c248_persian2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3046 Sep  6 12:02 c248_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4259 Sep  6 12:13 c250_celare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7170 Sep  6 12:13 c250_kolba.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4529 Sep  6 12:13 c250_sarez.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8664 Sep  6 12:19 c255_french2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6147 Sep  6 12:19 c255_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23626 Sep  6 12:19 c255_latin2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18287 Sep  6 12:20 c255_latin3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3398 Sep  6 12:19 c255_latin.png
-rw-rw-r-- 1 sfmqrb sfmqrb   26231 Sep  6 12:18 c258_kars.png
-rw-rw-r-- 1 sfmqrb sfmqrb   53453 Sep  6 12:18 c258_n2.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb  169482 Sep  6 11:58 crop_1648b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45260 Sep  6 11:57 crop_1648.png
-rw-rw-r-- 1 sfmqrb sfmqrb  305924 Sep  6 11:57 crop_1731.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6971 Sep  6 11:03 crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8619 Sep  6 11:03 crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5240 Sep  6 11:03 crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2064 Sep  6 12:21 crop_cheek2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1888 Sep  6 12:21 crop_cheek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3215 Sep  6 12:21 crop_p3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
-rw-rw-r-- 1 sfmqrb sfmqrb     724 Sep  6 12:11 drive.py
-rw-rw-r-- 1 sfmqrb sfmqrb    4491 Sep  6 12:13 fix.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   64267 Sep  6 11:59 mk235.py
-rw-rw-r-- 1 sfmqrb sfmqrb   73422 Sep  6 12:02 mk237.py
-rw-rw-r-- 1 sfmqrb sfmqrb   81037 Sep  6 12:03 mk240.py
-rw-rw-r-- 1 sfmqrb sfmqrb   80347 Sep  6 12:08 mk242.py
-rw-rw-r-- 1 sfmqrb sfmqrb   58802 Sep  6 12:07 mk244.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49868 Sep  6 12:23 mk251.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 p245
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:21 p249
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   30335 Sep  6 12:07 part2.py
-rw-rw-r-- 1 sfmqrb sfmqrb   38036 Sep  6 12:11 part3.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb   81026 Sep  6 12:03 pg239.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83594 Sep  6 12:03 pg239_small.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80947 Sep  6 11:59 pg244.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80632 Sep  6 11:55 pg245.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79253 Sep  6 11:54 pg246.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64208 Sep  6 12:04 pg247.png
-rw-rw-r-- 1 sfmqrb sfmqrb  142780 Sep  6 12:02 pg248hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49887 Sep  6 12:02 pg248.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82530 Sep  6 12:05 pg249.png
-rw-rw-r-- 1 sfmqrb sfmqrb  123419 Sep  6 12:13 pg250hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89076 Sep  6 12:13 pg250.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74772 Sep  6 12:13 pg252.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68850 Sep  6 12:14 pg253.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71025 Sep  6 12:13 pg254.png
-rw-rw-r-- 1 sfmqrb sfmqrb  148813 Sep  6 12:19 pg255hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55906 Sep  6 12:13 pg255.png
-rw-rw-r-- 1 sfmqrb sfmqrb  171848 Sep  6 12:21 pg256_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   83469 Sep  6 12:20 pg256.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81240 Sep  6 12:17 pg258.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66128 Sep  6 12:23 pg259.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79514 Sep  6 12:27 pg260.png
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 12:12 __pycache__
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


## [2026-09-06T16:27:15.271Z] TOOL CALL #51: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg260.png"
}
```


### [2026-09-06T16:27:15.610Z] TOOL RESULT

```

```


## [2026-09-06T16:27:15.608Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:27:41.898Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 kerk/gracilis ===\"; grep -n \"gracilis\" incoming/WLD/WLD_Bd1_pages.txt | head -5; echo \"=== WLD Bd1 krsna ===\"; grep -n \"kr̥ṣṇá\\|krsna\\|kirsnan\" incoming/WLD/WLD_Bd1_pages.txt | head -5; echo \"=== IEC krso ===\"; grep -n \"kr̥sos\\|krsos\\|krsnos\\|kr̥snos\" IEC.txt | head -5; echo \"=== SYN black ===\"; grep -n -i \"krsna-\\|kirsnas\" SYN.txt | head -5; echo \"=== SKT alchemy ===\"; grep -n -i \"alchemy\" SKT.txt | head -3; echo \"=== AFM كيمياء ===\"; grep -n \"كيمياء\\|الكيمياء\" AFM_pages.txt | head -5",
 "description": "Cross-check other reference books"
}
```


### [2026-09-06T16:27:42.013Z] TOOL RESULT

```
=== WLD Bd1 kerk/gracilis ===
3367:geworden, vgl. g radius gracilis, ouaXog similis) ; gr. ayeXg „Herde, Scbar“,
40053:(gloss, cracentes ), gracilis , gracilus „mager, schlank, zierlich",                   Gracchus EN.,
47157:„gracilis“ als „diinner Fladen" durch Wood MLN\ 24, 49, Berneker 389).
56465:sicher lat .gracilis ,,mager, schlank, zierlieh"                             (Wood a x Nr. 467, „*schlank,
=== WLD Bd1 krsna ===
40834:                           apr. kirsnan ds., lett. Kirsna „Name eines FlfiB-
=== IEC krso ===
8090:krksos, ios ‘oblique, awry’. WP II, 590. Var- iant krsos, see krs- (1) Gk. (ambig.) kársios ('oblique”. See krs-); Cz. & Slovak krch, krchy, adj. lefthanded, awk- ward’; Slovene cf. kíSiti ‘transgress; Blg. krás, m. “stile, crossing'; krăxvam, v “lay ath- wart; kráskam ‘go zigzag; krása, kărša (2) ‘wind, zigzag’; cf. krăšnjak ‘backbone’; Li. (?) kiršas ‘peevish, cross’; OPr. kirša “across; Li. cf. kìrkšnys, mpl. ‘lumbar region’; Latv. cirksnis, id. (but cf. krkin-) (the semantics are echoed in Alb. kryqza ‘lumbar region’ in relation to kryq, Lat. LW ‘cross’). An isophone arises in Skt. krsah ‘lean, poor?
8103:krKos ‘dwarfed, lean, sickly’. Cf. krsos (2). WP I, 420 Skt. kr$ah, id.; Av. koroso, id.; Alb. cf. kérthi, gs kérthini ‘weakling’ beside i n-gryth& *with- ered' (fr. *en-krK-); Cz. (ambig.) krs ‘dwarf sapling’, cf. krsek ‘dwarf tree; dwarf, gnome’; Lat. cf. crácens (Clean Fest); Li. kirsüs *bilious, jaundiced’
14256:qurkios, om, is 'tuft, shrub'. Cf. qurst-, quorstis Skt. kürcáh, Am. mn. ‘tuft of grass; beard’; Ir. ere, f., curc, pl. -anna m. ‘crest; cap’; Pol. karcz, m., Cz. krč, m. ‘tree-stump’; Ukr. korč, m. ‘bush, shrub’. (Slav. forms ambig. For a possible initial *k- cf. krKos & krsos (2))
=== SYN black ===
25580:If any division of time intermediate between the month and the day was recognized in the IE period, it was no doubt the most obvious one according to the phases of the moon. The Hindus divided the month into two halves (pak- $a- ‘wing’), that of the crescent moon (piirva- ‘earlier’ or gukla- ‘light’) and the waning moon (apara- ‘later’ or krsna- ‘black’). Cf. Thibaut, Grd. d. indo-ar. Phil. 3.9.12. For the Celts the Calen- dar of Coligny attests an old division of the month into halves (Thurneysen, Z. deutsch. Wortf. 1.191). The times
26642:15.63 DARK (in Color) Grk. —_péAas, xedarvds Goth.~ i... Lith. tamsus NG Babbs, oxodpos ON dékkr Lett. tums Lat. fuscus, pullus Dan. mérk, dunkel ChSl.  timinit It. scuro, cupo Sw. mork, dunkel SCr.  taman Fr. foncé, sombre OE wann. (deorc) Boh. temny Sp. obscuro ME dark, wan, dosc Pol. ciemny Rum. inchis NE dark Russ. temnyj Tr. dorche, temen Du. donker Skt. krsna-, ¢yama-, Nir. dorcha OHG  tunchal tamasa- W. tywyll MHG _ tunkel Av. axSaéna- Br. du NHG dunkel
26675:6. Skt. krsna-, gyama ‘black’ (15.65), also ‘dark’ in color.
26724:6. ChSI. ériint, etc., general Slavic : OPruss. kirsnan, Skt. krsna- ‘black’, fur- ther, Lith. kergas ‘black and white’, kersé ‘spotted cow’, etc., Sw., Norw. harr ‘ashes’. Walde-P. 1.428. Berneker 169 f.
26726:Skt. krsna-, above, 6.
=== SKT alchemy ===
519:Alchemy.  (F.-Arab.- Gk.)  O.F.  a/- chemit.  dtyiu/Nii.  ^  Arab,  a/,  the;  and I'imyA,  alchemy,  — Late  Gk.  xv/"'**.  chemis- try; for  xf^^'o.  «  mingling.  — Gk.  xiuv^  to pour  out,  mix.  (^GKU.)
6826:ior-8p&r.  a  roinenl.  (L.) (Ul.  a  Sovring)  wa»  luniicrl)- ia  alchemy  and  chcmi^ti)-. flow.
8623:hermetic.  ^Gk.)  Low  L.  herffuHcui,  re- lating to  alchemy  ;  coined  from  HtrmUt from  the  notion  that  the  great  kccrets  of alchemy  were  discovered  hyfltmuj  Trismt' ^j/iM.  — Gk. 'Ep/i7t,  Mercury.  ^  Hermeti- cally was  a  tenn  in  alchemy ;  a  glass  bottle was  h^rmttuaUy  scaled  when  the  orifice wns  fused  and  then  do<»cd  ogaioat  any admission  of  air.
=== AFM كيمياء ===
```


## [2026-09-06T16:27:54.671Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for L in 40053 40834; do echo \"-- line $L --\"; awk -v L=$L 'BEGIN{p=\"\"} /\\[pdf page/{p=$0} NR==L{print p; exit}' incoming/WLD/WLD_Bd1_pages.txt; done; echo \"=== context 40053 ===\"; sed -n '40048,40060p' incoming/WLD/WLD_Bd1_pages.txt; echo \"=== context 40834 ===\"; sed -n '40826,40845p' incoming/WLD/WLD_Bd1_pages.txt",
 "description": "WLD page context"
}
```


### [2026-09-06T16:27:56.485Z] TOOL RESULT

```
-- line 40053 --

-- line 40834 --

=== context 40053 ===

alt     zakrsald „Unfruchtbare“, slovak. krsek „Zwerg“, poln. mdartl. karslak
„niedriger,       astiger,       so gekriimmter         Baum, dafi er sich nur als Brennholz
eignet“. — Fraglich wegen der abweichenden Vokalstellung                                   lat. gracentes

(gloss, cracentes ), gracilis , gracilus „mager, schlank, zierlich",                   Gracchus EN.,
auch wenn gr-c- nach Solmsen KZ. 34, 21 Anm. aus cr-c- diss. ist ( cracentes
konnte aber auch alte Orthographic fur gracentes sein; ob dann zu ger-
„drehen“?).
  Lit. bei Yf.          LE Wb 2 u. cracentes        ,
                                                        Berneker aaO.

qert-, qerat- „drehen, zusammendrehen", vielfach vom Biegen und Ver-
=== context 40834 ===
„holzerner Pfahl (meta), Grenzpfahl u. dgl.“, s. Johansson IF. 14, 314 f.,
auch Petersson Stud, zu Fortunatovs Regel 38, 36 (mit Lit. auch fiber die
unannehmbare Verbindung von kudha als „Blickpunkt !< mit ai. caksate „sie
sehen“, gr. xey.uao, aksl. Lazuli „zeigen“).

1.     qers- und wohl auch bloBes qer- in Worten                                    ffir   Farben, bes. dunkle,
         schmutzige.
    Ai. krkna- „schwarz“              =
                           apr. kirsnan ds., lett. Kirsna „Name eines FlfiB-
chens“ (etwa „Schwarzwasser“) = abg. cr~om, russ. ierem skr. crn usw.                             ,

„schwarz“ ( *t brxm *cb rsm; s. Berneker 169 m. Lit.); ohne -wo-Formans
                     :
                             .



lit. kersas „schwarz und weiB gefieckt“, kt'rse „bunte Kuh“, kersis „schwarz-

bunter Ochse“, kermlis „Ringeltaube“; karsts „Brassen. Blei (Fisch)‘ f                                                         ,
```


## [2026-09-06T16:28:03.238Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<40060' | tail -2; echo ---; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | awk -F: '$1<40840' | tail -2; echo \"--- format sample ---\"; grep -n \"\\[pdf page\" incoming/WLD/WLD_Bd1_pages.txt | head -3",
 "description": "WLD page tags"
}
```


### [2026-09-06T16:28:05.157Z] TOOL RESULT

```
---
--- format sample ---
```


## [2026-09-06T16:28:10.973Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nfor needle in ['gracilis , gracilus','apr. kirsnan ds.']:\n    i=t.find(needle)\n    leaf=t.count('\\f',0,i)\n    print(needle,'-> leaf(0-based ff count)=',leaf)\nEOF",
 "description": "WLD leaf index"
}
```


### [2026-09-06T16:28:12.596Z] TOOL RESULT

```
gracilis , gracilus -> leaf(0-based ff count)= 429
apr. kirsnan ds. -> leaf(0-based ff count)= 436
```


## [2026-09-06T16:28:21.953Z] TOOL CALL #56: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/%DA%A9%D8%B1%DB%8C%D8%B4%D9%86%D8%A7/\" \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%B4%D8%A7%D8%B3%D8%A8/\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 260: Moin/Dehkhoda for Krishna and Garshasb\" 2>&1 | tail -1; done",
 "description": "Fetch abadis for Krishna and Garshasb"
}
```


### [2026-09-06T16:28:27.696Z] TOOL RESULT

```
### https://abadis.ir/fatofa/%DA%A9%D8%B1%DB%8C%D8%B4%D9%86%D8%A7/
/home/sfmqrb/git/rishe/data/verification/sources/web/9ae1b0806271146c.txt
### https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%B4%D8%A7%D8%B3%D8%A8/
/home/sfmqrb/git/rishe/data/verification/sources/web/cac53a7ebcdfbb07.txt
```


## [2026-09-06T16:28:31.499Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### krishna\"; sed -n '1,40p' 9ae1b0806271146c.txt | grep -n \"کریشنا\" | head -8; echo; grep -n \"کریشنا\" 9ae1b0806271146c.txt | head -6; echo \"### garshasb\"; grep -n \"گرشاسب\\|کرشاسپ\\|لاغر\" cac53a7ebcdfbb07.txt | head -8",
 "description": "Read abadis results"
}
```


### [2026-09-06T16:28:31.578Z] TOOL RESULT

```
### krishna
4:TITLE: کریشنا - معنی در دیکشنری آبادیس
6:کریشنا - معنی در دیکشنری آبادیس 
10: کریشنا
19: اسم: کریشنا (پسر) (سانسکریت) (تلفظ: kerishna) (فارسی: کِریشنا) (انگلیسی: kerishna) 
29: کریشنا (بازیگر). کریشنا ( انگلیسی: Krishna; ۳۱ مهٔ ۱۹۴۳ – ۱۵ نوامبر ۲۰۲۲ ) [ ۲] [ ۳] بازیگر، تهیه کننده فیلم، و کارگردان فیلم اهل هند بود. 
32: wiki: کریشنا (بازیگر) 
34: کریشنا (فیلم ۱۹۹۶). کریشنا ( به هندی: Krishna ) فیلمی محصول سال ۱۹۹۶ و به کارگردانی دیپاک شیوداسانی است. در این فیلم بازیگرانی همچون سونیل شتی، کاریسما کاپور، اوم پوری، شاکتی کاپور، تینو آناند، کولبوشان کارباندا ایفای نقش کرده اند. 
35: wiki: کریشنا (فیلم ۱۹۹۶) 

4:TITLE: کریشنا - معنی در دیکشنری آبادیس
6:کریشنا - معنی در دیکشنری آبادیس 
10: کریشنا
19: اسم: کریشنا (پسر) (سانسکریت) (تلفظ: kerishna) (فارسی: کِریشنا) (انگلیسی: kerishna) 
29: کریشنا (بازیگر). کریشنا ( انگلیسی: Krishna; ۳۱ مهٔ ۱۹۴۳ – ۱۵ نوامبر ۲۰۲۲ ) [ ۲] [ ۳] بازیگر، تهیه کننده فیلم، و کارگردان فیلم اهل هند بود. 
32: wiki: کریشنا (بازیگر) 
### garshasb
4:TITLE: گرشاسب - معنی در دیکشنری آبادیس
6:گرشاسب - معنی در دیکشنری آبادیس 
10: گرشاسب
17: اسم: گرشاسب (پسر) (فارسی) (تاریخی و کهن) (تلفظ: garšāsb) (فارسی: گَرشاسب) (انگلیسی: garshasb) 
18: معنی: دارنده اسب لاغر، نام جهان پهلوان ایرانی، ( = کرشاسپ و گرشاشپ )، به معنی دارنده ی اسب لاغر، ( اَعلام ) ) ( در شاهنامه ) از پهلوانان ایرانی سپاه منوچهر در جنگ با سلم و تور و خزانه دار منوچهر، گرشاسبنامه سرگذشت اوست، ) آخرین شاه از سلسله ی پیشدادیان و پسر زو که نه سال پادشاهی کرد، ( در اعلام ) جهان پهلوان ایرانی پسر اثرط ( اترد ) پسر سام پسر تورگ پسر سپانیاسپ ( شیدسپ ) پسر دورشاسپ پسر توگ ( تور ) پسر فریدون و نیز پسر زو ( زاب ) دهمین پادشاه پیشدادی که نه سال پادشاهی کرد، از شخصیتهای شاهنامه، نام پدر نریمان جد رستم پهلوان شاهنامه، نیز نام پسر زو، از پادشاهان پیشدادی
23: گرشاسب. [ گ ِ ] ( اِ ) احتلام. ( ناظم الاطباء ). و آن مصحف گوشاسب ( = بوشاسپ ) است. رجوع به گوشاسب و گوشاسپ و بوشاسب و بوشاسپ شود.
24: گرشاسب. [ گ َ ] ( اِخ ) نام یکی از اجداد رستم زال است و او پسر اترد باشد که از نبائر جمشید است. ( جهانگیری ) ( برهان ). معاصر فریدون بود. ترکستان و خطا را مسخر کرده. حکیم اسدی طوسی فتوحات او را منظوم نموده و به گرشاسب نامه موسوم است. ( آنندراج ) : اما بنا کردن سیستان به دست گرشاسب بن اثرت بن شهربن کورنگ بن بیداسب بن توربن جمشیدالملک... ( تاریخ سیستان ص 2 ). نام گرشاسب جهان پهلوان در اوستا بارها یاد شده و او در کتاب مقدس مزدیسنا به منزله رستم در شاهنامه یا هرقل یونانیان است. این نام در اوستا به صورت کرساسپه ، سانسکریت کرساسوه آمده و مرکب است از دو جزء: جزء اول کرسه به معنی لاغر و جزء دوم همان اسب پارسی است و مجموعاً به معنی «دارنده اسب لاغر، کسی که اسبش لاغر است » میباشد. بنابراین اصح آن کرشاسب با کاف تازی است و چون در نسخ خطی قدیم میان کاف ( تازی ) و گاف ( پارسی ) در نوشتن امتیازی نمی نهادند ممکن است که گویندگان باستانی ما هم در عهد خویش کرشاسب با کاف ( تازی ) استعمال کرده باشند و حتی ابوالفدا آن را ( کرشاسف ) ضبط کرده ، از اینرو ممکن است قائل شد که گویندگان ایرانی او را گرشاسپ و نزدیک به لغت اوستایی میخواندند .
25:نسب گرشاسب : نام پدر گرشاسب در اوستا ثریته آمده است ، گاهی به اسم خاندانش سام گرشاسب خوانده شده ( فروردین یشت بندهای 61 و 136 )، حتی در کتب پهلوی هم گاهی فقط به نام خاندانش ( سام ) نامیده شده است. در فرگرد 20 وندیداد، در بندهای اول ودوم چنین آمده است : «زرتشت از اهورمزدا پرسید: کیست در میان پرهیزکاران و دانایان و کامکاران و توانگران و رایومندان و تهمتنان ( دیوان ) و پیشدادیان نخستین مردی که ناخوشی را بازداشت ، مرگ را بازداشت ( زخم )، نیزه پران را بازداشت ، حرارت تب را از تن مردم باز- داشت ؟ اهورامزدا در پاسخ گفت : ای سپنتمان زرتشت ثریته در میان پرهیزکاران و دانایان و کامکاران و توانگران و رایومندان و تهمتنان ( دلیران ) و پیشدادیان ، نخستین مردی است که ناخوشی را بازداشت ، مرگ را بازداشت ،( زخم ) نیزه پران را بازداشت ، حرارت تب را از تن مردم بازداشت ». بنا بر این قول ثریته در اوستا نخستین پزشک نوع بشر و به منزله اسکلپسیوس یونانیان و آسکلابیوس رومیان است. در یسنای 9 بند 10 نیز در طی پرسش و پاسخ زرتشت با ایزدهوم از ثریته نام برده شده است.هوم در پاسخ به زرتشت گوید «سوم کسی که مرا مهیا ساخت ثریته از خاندان سام است که از نیک خواه ترین [مردم ] است و در عوض خداوند به او دو پسر داد: یکی اورواخشیه که زاهد و قانونگزار بوده و دیگری گرشاسب که دلیر و نام آور بود.» اما ثریته اوستا همان است که در گرشاسب نامه اسدی اثرط شده : بیشتر بخوانید ...
```


## [2026-09-06T16:29:19.434Z] TOOL CALL #58: Bash

```json
{
 "command": "sed -n '1,120p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T16:29:19.473Z] TOOL RESULT

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


## [2026-09-06T16:29:20.343Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '26565,26580p' LAT.txt",
 "description": "Ernout-Meillet gracilis"
}
```


### [2026-09-06T16:29:20.390Z] TOOL RESULT

```
(G loss.Philox.). Les gloses le derivent d'na graba "capnt", non antre-
aent atteste, cf. Lindsay ALLG 10,338; aais graba seable nn eaprnnt497
gradus
au slave du sud g lava.
grac(c)it 5 , -Ss, -are: crier (de 1 ' oie). Onomatopde (Anthol.).
M.L. 3 & 49 a.
gracilis, -e (f 4 n .gracila, Luc. ap. Non .489,91; Ter. Eu. 314 d'aprbs
Eugraphius, cf. sublima, sterila): maigre (oppose a pinguis dona Pline,
^4,33), minee, grele; de IA A l'dpoque imperiale "pauvre"; dans la
1 . de la rhetor., "simple, sans ornement", traduisant le gr. l.cr)(VOC,
cf. Geli .7, 14, isqq. - Ancien, usuel. M.L. 3849.
Derives: gracilentus (arch.) et gracilens (Laev. ap. Non. 11G,11) 5
gracilitas = Lo^vorriC, gracilitudo (Acc.)j gracilescS (Aa*.)j compos^:
gracilipes (Pubi. Syr. ap.Petr.55 = lo)(yoaxeXT)<;).
Gracilis semble se rattacher A un verbe *graceo dont on trouve
trace dans la glose de P.F.46,16: cracentes (pour gra-), graciles.
```


## [2026-09-06T16:29:56.837Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \"https://www.ahdictionary.com/word/search.html?q=gracile\" \"https://www.ahdictionary.com/word/search.html?q=chemistry\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 260: AHD gracile / chemistry entries\" 2>&1 | tail -1; done; echo; grep -n -i \"gracile\\|Latin gracilis\" data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1(b'https://www.ahdictionary.com/word/search.html?q=gracile').hexdigest()[:16])\").txt | head -6",
 "description": "Fetch AHD gracile and chemistry"
}
```


### [2026-09-06T16:29:59.405Z] TOOL RESULT

```
### https://www.ahdictionary.com/word/search.html?q=gracile
/home/sfmqrb/git/rishe/data/verification/sources/web/15d2be934a7adc9b.txt
### https://www.ahdictionary.com/word/search.html?q=chemistry
/home/sfmqrb/git/rishe/data/verification/sources/web/7d47d5996d43d3f3.txt

1:URL: https://www.ahdictionary.com/word/search.html?q=gracile
4:TITLE: American Heritage Dictionary Entry: gracile
6:American Heritage Dictionary Entry: gracile 
49: [Latin gracilis .]
```


## [2026-09-06T16:30:04.445Z] TOOL CALL #61: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg260.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/260.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Copy page PNG for audit"
}
```


### [2026-09-06T16:30:04.533Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T16:30:06.525Z] AGENT

Now let me write the verification file.


## [2026-09-06T16:37:59.240Z] TOOL CALL #62: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-260.json",
 "content": "{\n  \"pdf_page\": 260,\n  \"book_page\": 230,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-06\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Kerk, Kork, Krk\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *kerḱ- / *kork- : *kr̥ḱ- 'to become thin, wrinkle, waste away' (Pokorny 581 '[kerk-], kork- : kr̥k-', Meaning: 'to wrinkle, become thin')\",\n      \"note\": \"Nourai's root box is an accurate copy of Pokorny p.581: language label (Indo-European), the three ablaut shapes Kerk / Kork / Krk and the gloss 'thin, slender' all match Pokorny's '[kerk-], kork- : kr̥k-, Meaning: to wrinkle, become thin', whose material is exactly Old Indic kr̥śa- / kr̥śyati, Avestan kərəsa- 'skinny', Latin gracilis (dissim. from *cracilis) and Lith. karšti 'to grow old'. Pokorny himself adds a caution ('Note: or at most kark- : kr̥k-'); Wiktionary and modern handbooks write the root with a palatal, *kerḱ-, since Skt. kr̥śá- and Av. kərəsa- require *ḱ. The AHD/Watkins appendix does not carry this root at all, so Nourai could not have taken it from there. No node of this entry is in conflict with modern scholarship; only the direction of the Avestan→Sogdian arrow is a simplification (see node 3).\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kerḱ- «لاغر شدن، تکیده شدن، چروکیده شدن» است که پوکورنی در صفحهٔ ۵۸۱ فرهنگ ریشه‌شناختی خود با سه گونهٔ ابلاوتی [kerk-]، kork- و kr̥k- آورده و مادّهٔ آن دقیقاً همان است که نورایی نقل کرده: سنسکریت kr̥śá- «لاغر»، اوستایی kərəsa- «لاغر، تکیده»، لاتینی gracilis و لیتوانیایی karšti. برچسب زبانی و معنای «thin, slender» درست است؛ تنها نکته آنکه پژوهش امروزی ریشه را با کام‌کامی *ḱ می‌نویسد (*kerḱ-)، زیرا š سنسکریت و s اوستایی جز از *ḱ پدید نمی‌آید، و خود پوکورنی هم در یادداشتش دربارهٔ شکل دقیق ریشه احتیاط کرده است. در مجموع ادعای نورایی دربارهٔ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/gracilis\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:581\",\n          \"status\": \"supports\",\n          \"note\": \"Local OCR POK_full.txt (grep 'gracilis', line 45963) gives the whole entry: 'Root / lemma: [kerk-,] kork- : kr̥k- | Meaning: to wrinkle, become thin | Note: (or at most kark- : krk-) | Material: Old Indic krsa- \\\"emaciated, lean, weak\\\", krsyati \\\"peaks, becomes thin\\\", Avestan karasa- \\\"skinny\\\"; … Latin cracentes, leg. gracentes \\\"thin, slight, slender\\\" to gracilis \\\"skinny, slim\\\", dissim. from *cracilis … References: WP. I 420 f., WH. I 284 … Page(s): 581'. Exactly Nourai's root box.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"p. 581 s.v. [kerk-], kork- : kr̥k-\",\n          \"stance\": \"supports\",\n          \"note\": \"'Meaning: to wrinkle, become thin … Old Indic krsa-, Avestan karasa- \\\"skinny\\\" … Latin gracilis, dissim. from *cracilis' (POK_full.txt lines 45947-45965).\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Band I p. 420 (local WLD_Bd1_pages.txt, leaf 429)\",\n          \"stance\": \"supports\",\n          \"note\": \"'Fraglich wegen der abweichenden Vokalstellung lat. gracentes (gloss. cracentes), gracilis, gracilus \\\"mager, schlank, zierlich\\\"' — Walde-Pokorny I 420 is the source Pokorny cites for this root; note WP is more hesitant about the Latin form ('fraglich').\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 appendix (AHD_watkins1985.txt)\",\n          \"stance\": \"silent\",\n          \"note\": \"grep 'gracile', 'kerk-' returns nothing; the 1985 IE-root appendix has no *kerk-/*kerḱ- lemma and does not index GRACILE, so Watkins simply omits this root.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, col. under 'krKos' (IEC.txt line 8103)\",\n          \"stance\": \"supports\",\n          \"note\": \"'krKos \\\"dwarfed, lean, sickly\\\". Cf. krsos (2). WP I, 420. Skt. kr̥śaḥ, id.; Av. kərəsō, id.; … Lat. cf. crácens (Clean. Fest); Li. kirsūs' — Mann sets up the same root with the same Indo-Iranian and Latin material.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"keresa; keresa-vazda; keresa-aspa\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Young Avestan kərəsa- is a real adjective 'mager, lean' (Bartholomae, Altiranisches Wörterbuch, col. 469-470: 'j. ¹kərəsa- Adj. \\\"mager\\\". Komp[ositionsglied]. — ai. kr̥śá- Adj.'), the exact cognate of Vedic kr̥śá- and the regular Iranian reflex of PIE *kr̥ḱ-so- (PIE *ḱ > Proto-Iranian *s, and the syllabic *r̥ appears in Avestan as the anaptyctic ərə). Both compounds in the box are bahuvrīhis attested as personal names: kərəsa-vazdah- (AiW col. 470, 'j. kərəsa-vazdah- m. EN. eines Bruders' — the brother of Fraŋrasyan/Afrāsiāb) = kərəsa- 'little' + vazdah- 'firmness, endurance' (AiW col. 1379 'g. ¹vazdah- Adj. \\\"beständig\\\"'), so literally 'whose endurance is scant' — Nourai's gloss 'with little power' is right, though he drops the final -h of the stem; and kərəsāspa- = kərəsa- + aspa- 'horse' with the regular contraction a+a > ā, 'he whose horses are lean' (Encyclopaedia Iranica, KARSĀSP: 'Av. Kərəsāspa probably means \\\"he with meager horses\\\"; cf. Old Indic kr̥śvāśva', citing Mayrhofer 1977 I/60). Nourai's uncontracted spelling 'keresa-aspa' is a morphological analysis, not the attested form Kərəsāspa-.\",\n          \"derivation_fa\": \"واژهٔ اوستایی kərəsa- صفتی است به معنای «لاغر، تکیده» که بارتولومه در «فرهنگ ایرانی باستان» (ستون ۴۶۹) با همین معنی «mager» آورده و آن را هم‌ریشهٔ kr̥śá- سنسکریت دانسته است؛ از دید آواشناسی *ḱ هندواروپایی در ایرانی باستان به s بدل شده و *r̥ هجایی در اوستایی به صورت ərə نمودار گشته است. دو ترکیب دیگرِ این خانه هر دو صفتِ ملکی (بهوریهی) و در اوستا نام خاصّ‌اند: kərəsa-vazdah- (بارتولومه، ستون ۴۷۰: «نام خاصّ برادری») از kərəsa- «اندک» و vazdah- «پایداری، استواری»، یعنی «کم‌پایداری»؛ و kərəsāspa- از kərəsa- + aspa- «اسب» با ادغام a+a > ā، یعنی «دارندهٔ اسبان لاغر» (دانشنامهٔ ایرانیکا، مدخل KARSĀSP، به نقل از مایرهوفر، با مقایسهٔ سنسکریت kr̥śvāśva). خوانشِ نورایی درست است؛ تنها «keresa-vazda» بی‌ـh نوشته شده و «keresa-aspa» صورت تحلیلی و ناادغام‌شدهٔ Kərəsāspa- است.\",\n          \"sources\": [\n            \"https://www.iranicaonline.org/articles/karsasp\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:581\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt p.581: 'Old Indic krsa- \\\"emaciated, lean, weak\\\" … Avestan karasa- \\\"skinny\\\"' — Pokorny lists the Avestan adjective under this root, as the chart's arrow requires.\"\n            },\n            {\n              \"ref\": \"BQT:1795\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in's footnotes to Borhan-e Qate' (local scan incoming/BQT/BQT_v3_pages.txt, pdf page 592 = printed p.1797 of the Ibn Sina reprint; Nourai's 1795 is 2 pages off in this printing) give both names from the same Avestan adjective: fn. 6 'گرسیوز؛ در اوستا Keresavazda (از دو جزء: keresa لاغر و اندك، vazda قوت، پایداری) … نام برادر افراسیاب است' and fn. 7 'کرشاسب در اوستا صورت Keresāspa و در سانسکریت Kr̥śāśva آمده مرکب از دو جزء: اول keresa بمعنی لاغر، جزء دوم aspa همان اسب فارسی است … بمعنی صاحب اسب لاغر'. Nourai's transliterations 'keresa-vazda' and 'keresa-aspa' are copied verbatim from Mo'in.\"\n            },\n            {\n              \"ref\": \"KLN:672\",\n              \"status\": \"supports\",\n              \"note\": \"Klein 1966 s.v. gracile (KLN_1966.txt line 16504): 'L. gracilis … prob. cogn. with OI. kr̥śáḥ, \\\"thin, weak\\\", Avestic kər°sa-, \\\"lean, meager\\\"' — Klein cites the Avestan word with exactly this meaning.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Altiranisches Wörterbuch col. 469-470 (BRT.txt lines 9576-9589)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. ¹kərəsa- Adj. \\\"mager\\\". Komp. — ai. kr̥śá- Adj.'; 'Komp.: *kərəsa-aspa-, eig. \\\"des Rosse mager sind\\\"'; 'j. kərəsa-vazdah- m. EN. eines Bruders'; and separately 'j. kərəsaoxšan- m. EN. … eig. \\\"des Stiere mager sind\\\"'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. krKos (IEC.txt line 8103)\",\n              \"stance\": \"supports\",\n              \"note\": \"'krKos \\\"dwarfed, lean, sickly\\\" … Skt. kr̥śaḥ, id.; Av. kərəsō, id.' — independent confirmation of the Avestan adjective under this root.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Dehkhoda/Mo'in s.v. گرشاسب (abadis.ir)\",\n              \"stance\": \"supports\",\n              \"note\": \"'این نام در اوستا به صورت کرساسپه، سانسکریت کرساسوه آمده و مرکب است از دو جزء: جزء اول کرسه به معنی لاغر و جزء دوم همان اسب پارسی' — the standard Persian handbooks give the same analysis.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"Garsîvaz «گرسیوز»; Garšâsp «گرشاسپ»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both New Persian names continue the Avestan compounds of node 1 through Middle Persian. Av. Kərəsavazdah- → MP Karsēwaz/Garsēwaz → NP گرسیوز Garsivaz, the Turanian, brother of Afrāsiāb in the Šāh-nāma: the stem-final -dah is lost as regularly in MP (cf. Av. vazdah- 'firmness'), and Av. -a- of the second member appears as Persian -ē-/-i-. Av. Kərəsāspa- → MP Kirsāsp/Karsāsp (attested in the Pahlavi books, cf. Iranica: 'Av. Kərəsāspa, Pahlavi various forms, Pers. Garšāsp (Garšāsb, Arabicized Karšāsf)') → NP گرشاسپ Garšāsp, the dragon-slaying hero of Asadi Ṭusi's Garšāsp-nāma. The one irregularity is the initial voicing k- > g-: Skjærvø in Iranica calls the change 'problematic' and conjectures contamination with Gar-šāh 'king of the mountain(s)', the epithet of Gayōmard, while Mo'in and Dehkhoda argue that old manuscripts did not distinguish kāf from gāf in writing, so that Kar-/Gar- is largely an orthographic matter (Abu'l-Fidāʾ still writes کرشاسف). The glosses Nourai gives ('with little power', 'with lean horses') are precisely Mo'in's.\",\n          \"derivation_fa\": \"هر دو نام فارسی نو دنبالهٔ همان ترکیب‌های اوستایی‌اند و از راه فارسی میانه به فارسی دری رسیده‌اند: اوستایی Kərəsavazdah- ← فارسی میانه Karsēwaz/Garsēwaz ← فارسی نو «گرسیوز»، برادر افراسیاب در شاهنامه، که در آن پایانهٔ -dah مانند دیگر ستاک‌های اوستایی در پهلوی افتاده است؛ و اوستایی Kərəsāspa- ← پهلوی Kirsāsp/Karsāsp ← فارسی نو «گرشاسپ»، جهان‌پهلوان و اژدهاکش، که اسدی طوسی گرشاسب‌نامه را دربارهٔ او سروده است. تنها دشواری آوایی، ابدال k آغازین به g است؛ اسکیروو در ایرانیکا آن را «مسئله‌دار» می‌خواند و احتمال می‌دهد از «گرشاه» (لقب گیومرد) اثر پذیرفته باشد، ولی معین و دهخدا می‌گویند در نسخ خطی کهن میان کاف و گاف تمایزی در نوشتن نبوده و ابوالفدا هنوز «کرشاسف» ضبط کرده است. معناهایی که نورایی می‌دهد («کم‌توان»، «دارندهٔ اسب لاغر») همان است که معین در حاشیهٔ برهان قاطع آورده؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.iranicaonline.org/articles/karsasp\",\n            \"https://abadis.ir/fatofa/%DA%AF%D8%B1%D8%B4%D8%A7%D8%B3%D8%A8/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1795\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' with Mo'in's notes, printed p.1797 of the local scan (incoming/BQT/BQT_v3_pages.txt, pdf page 592): headword 'گرسیوز … نام برادر افراسیاب است' with fn. 6 deriving it from Av. Keresavazda (keresa 'لاغر و اندك' + vazda 'قوت، پایداری'), and headword 'گرشاسب' with fn. 7 deriving it from Av. Keresāspa 'صاحب اسب لاغر'. The Persian scripts گرسیوز / گرشاسپ in the JSON match the book.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Dehkhoda + Mo'in s.v. گرشاسب (abadis.ir, archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"'نام گرشاسب جهان پهلوان در اوستا بارها یاد شده … این نام در اوستا به صورت کرساسپه … مرکب است از دو جزء: جزء اول کرسه به معنی لاغر و جزء دوم همان اسب پارسی … بنابراین اصح آن کرشاسب با کاف تازی است.'\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW col. 470\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. kərəsa-vazdah- m. EN. eines Bruders' — Bartholomae's Avestan proper name is the etymon of گرسیوز.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt, PHD_mackenzie.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'karsāsp', 'kirsāsp', 'garsēwaz' finds nothing — MacKenzie's dictionary excludes proper names, so it can neither confirm nor deny the Middle Persian link.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II Glossary (NYB_vol2_glossary.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'karsasp', 'garsewaz' finds nothing; the glossary covers the texts edited in vol. I only.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"`ks, ks\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Both Sogdian forms are real and mean what the chart says. Gharib, Sogdian–Persian–English Dictionary no. 831 (printed p.32): 'ʾks- B, (ə)kasc, (ə)kos(e)? (ʾksʾy), ©Av. kərəsa-, Khwar. ykš … small, thin', and no. 4900 (printed p.195): 'ks- B … pl. ʾksth pred. inst. ʾksʾ ⇒ ʾks- … thin'. The two entries are the same word written with and without the prothetic aleph that Sogdian regularly writes before initial consonant clusters, and both go back to Proto-Iranian *kr̥sa- (*ḱr̥ḱ-so-), with the syllabic *r̥ vocalised as a in Sogdian. What is not quite right is the direction of the arrow: Sogdian ʾks- is not descended from Avestan kərəsa- but is its sister, an independent Middle Iranian continuation of the same Old Iranian etymon — Gharib's own '©Av.' sign means 'compare Avestan', not 'from Avestan'. Read as 'same Old Iranian etymon', the chart is correct.\",\n          \"derivation_fa\": \"هر دو صورت سغدی واقعی‌اند و همان معنایی را دارند که در نمودار آمده است: قریب در «فرهنگ سغدی» شمارهٔ ۸۳۱ (ص ۳۲) می‌آورد «ʾks- (ə)kasc / (ə)kos(e)، مقایسه شود با اوستایی kərəsa- و خوارزمی ykš، به معنی خُرد و باریک» و شمارهٔ ۴۹۰۰ (ص ۱۹۵) «ks- … باریک» با جمع ʾksth؛ این دو یک واژه‌اند، یکی با الف پیشین (پروتتیک) که سغدی پیش از خوشهٔ آغازین می‌نویسد. هر دو از ایرانی باستان *kr̥sa- برخاسته‌اند و r̥ هجایی در سغدی به a بدل شده است. نکتهٔ قابل تصحیح آن است که سغدی فرزند اوستایی نیست بلکه هم‌ریشه و خواهرِ آن است؛ نشانهٔ «©Av.» در فرهنگ قریب نیز به معنی «قیاس شود با اوستایی» است نه «برگرفته از اوستایی». پس پیکان نمودار را باید «هم‌ریشه با همان ستاک ایرانی باستان» خواند و با این قید پذیرفتنی است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"SOD:32,195\",\n              \"status\": \"supports\",\n              \"note\": \"Both numbers are printed PAGES of Gharib, not entry numbers, and both are right. SOD_pages.txt line 6074, on the leaf whose running number is 32: '831 ʾks- B  (ə)kasc, (ə)kos(e)? (ʾksʾy) ©Av. kərəsa-, Khwar. ykš ⇒ ks-  |  small, thin  |  GMS 1201; Benv. VJ n p94; Inst. ʾksʾ, SCE 76; pl. ʾkstʾ, VJ 1264'. SOD_pages.txt line ~17678, leaf numbered 195: '4900 ks- B … pl. ʾksth pred. inst. ʾksʾ ⇒ ʾks-  |  thin'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SOD\",\n              \"where\": \"Gharib nos. 831 (p.32) and 4900 (p.195)\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check; Gharib explicitly cross-references Avestan kərəsa- and Khwarezmian ykš.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"AiW col. 469\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. ¹kərəsa- Adj. \\\"mager\\\"' — the Old Iranian etymon that Gharib compares.\"\n            },\n            {\n              \"src\": \"ISS_alt_DKS\",\n              \"where\": \"Bailey, Dictionary of Khotan Saka (ISS_alt_DKS.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for a Khotanese cognate of kərəsa- ('kīrsa', 'ksa- thin') produced no usable entry; the Khotanese side adds nothing here.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Latin\",\n          \"words\": \"gracilis\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Latin gracilis, -e 'thin, lean, slender' (opposed to pinguis; Ernout–Meillet s.v., p.497) is put under this root by Pokorny 581 and Klein 672. The formation is an -ilis adjective of the habilis type, built on a lost verb *graceō/*craceō 'to be meagre', whose participle survives in the Festus gloss 'cracentes (for gra-), graciles' (Paul. Fest. 46,16); Pokorny takes gracilis to be dissimilated from *cracilis, i.e. the initial g- is secondary (Solmsen KZ 34, 21 explains gr-c- < cr-c- by dissimilation). The root vocalism *kr̥ḱ- gives Latin -ra- as usual for syllabic *r̥. Wiktionary states the chain directly: 'From an Old Latin verb *graceō or *craceō \\\"to be meager, slim\\\", from Proto-Indo-European *kerḱ- \\\"to become thin, to wane\\\", related to Sanskrit कृश (kṛśa), Lithuanian karštu, and Avestan 𐬐𐬆𐬭𐬆𐬯𐬀 (kərəsa)'. Ernout–Meillet are more reserved: they set up only *graceō and do not mention the Indo-Iranian cognates, so the Indo-Iranian connection, while standard, is not universally asserted.\",\n          \"derivation_fa\": \"لاتینی gracilis «لاغر، باریک» (در برابر pinguis «فربه») را پوکورنی (ص ۵۸۱) و کلاین (ص ۶۷۲) زیر همین ریشه می‌آورند. ساخت آن صفتی است با پسوند -ilis (مانند habilis از habēre) بر پایهٔ فعلی از میان‌رفته *graceō/*craceō «لاغر بودن» که تنها نشانش گلوسهٔ فستوس است: «cracentes (به‌جای gra-)، graciles». پوکورنی g آغازین را ثانوی و حاصل ناهمگونی از *cracilis می‌داند، و *r̥ هجایی هندواروپایی در لاتین به -ra- بدل شده است. ویکی‌واژه همین زنجیره را می‌آورد و آن را با kṛśa سنسکریت و kərəsa اوستایی هم‌ریشه می‌داند؛ در مقابل، ارنو و مه‌یه محتاط‌ترند و تنها *graceō را بازسازی می‌کنند و از هم‌ریشه‌های هندوایرانی نامی نمی‌برند. در مجموع ادعای نورایی پذیرفتنی و مطابق نظر رایج است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/gracilis\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:581\",\n              \"status\": \"supports\",\n              \"note\": \"POK_full.txt p.581: 'Latin cracentes, leg. gracentes \\\"thin, slight, slender, slim, meagre, lean\\\" to gracilis \\\"skinny, slim, arid\\\", dissim. from *cracilis.'\"\n            },\n            {\n              \"ref\": \"KLN:672\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt line 16504, s.v. gracile: 'L. gracilis, \\\"slender, thin, slight, meager\\\", dissimilated fr. *cracilis, rel. to cracens, \\\"slender\\\", and prob. cogn. with OI. kr̥śáḥ, \\\"thin, weak\\\", Avestic kər°sa-, \\\"lean, meager\\\", Lith. karštu, karšti … For the ending of grac-ilis cp. habilis.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout–Meillet s.v. gracilis (LAT.txt line 26571, near running head 'gradus', p.497)\",\n              \"stance\": \"partial\",\n              \"note\": \"'gracilis, -e … maigre (opposé à pinguis) … Gracilis semble se rattacher à un verbe *graceō dont on trouve trace dans la glose de P.F. 46,16: cracentes (pour gra-), graciles.' They reconstruct the Latin verb but do not name Skt. kr̥śá- / Av. kərəsa-, i.e. they neither confirm nor deny the IE connection.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 420 (WLD_Bd1_pages.txt leaf 429)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Fraglich wegen der abweichenden Vokalstellung lat. gracentes (gloss. cracentes), gracilis, gracilus \\\"mager, schlank, zierlich\\\" … auch wenn gr-c- nach Solmsen KZ. 34,21 Anm. aus cr-c- diss. ist' — WP admit the Latin word here but flag the vowel placement as a difficulty.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann s.v. krKos (IEC.txt line 8103)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Lat. cf. crácens (Clean. Fest)' listed together with Skt. kr̥śaḥ and Av. kərəsō.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"English\",\n          \"words\": \"gracile\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English gracile is a straight learned borrowing of Latin gracilis, taken into English in the early 17th century (first recorded 1620s) in the sense 'slender, thin'; only later, by contamination with graceful, did it acquire the nuance 'gracefully slender' that Klein records as sense 2. There is no intermediate French or Middle English stage — the -is of the Latin adjective is simply dropped, as in fertile, docile. The American Heritage Dictionary gives the whole etymology as '[Latin gracilis.]', which is exactly the arrow drawn here.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی gracile وام‌واژه‌ای دانشورانه و مستقیم از لاتینی gracilis است که در آغاز سدهٔ هفدهم میلادی (نخستین کاربرد دههٔ ۱۶۲۰) به معنی «باریک، لاغر» وارد انگلیسی شد؛ معنای دوم آن، «باریک و خوش‌اندام»، بعدها و از راه آمیختگی با graceful پدید آمد (کلاین دو معنی را جدا می‌آورد). در این وام‌گیری هیچ واسطهٔ فرانسوی یا انگلیسی میانه در کار نیست و تنها پایانهٔ -is لاتینی افتاده است، همان‌گونه که در fertile و docile. فرهنگ American Heritage نیز ریشه‌شناسی این واژه را تنها «[Latin gracilis]» می‌نویسد، یعنی دقیقاً همان پیکانی که نورایی کشیده است.\",\n          \"sources\": [\n            \"https://www.ahdictionary.com/word/search.html?q=gracile\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:570\",\n              \"status\": \"supports\",\n              \"note\": \"The 1975 New College body page is not on disk (the local AHD file is only Watkins' 1985 IE-root appendix), but the current online AHD entry for gracile, archived at data/verification/sources/web/15d2be934a7adc9b.txt, reads 'gracile … 1. Slender; slim … [Latin gracilis.]' — the claim Nourai attributes to AHD p.570.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. gracile (KLN_1966.txt line 16504)\",\n              \"stance\": \"supports\",\n              \"note\": \"'gracile, adj., 1) slender; 2) gracefully slender. — L. gracilis, \\\"slender, thin, slight, meager\\\" … Derivatives: gracile-ly, adv., gracile-ness, n., gracil-ity, n.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"ahdictionary.com s.v. gracile\",\n              \"stance\": \"supports\",\n              \"note\": \"'[Latin gracilis.]'\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, Concise Etymological Dictionary (SKT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'gracile' returns nothing; Skeat's concise dictionary omits this rare Latinism.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 3,\n      \"root\": \"Kers 2\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *ḱers- 'black, dark' (Pokorny 583 kers- 'a kind of colour (black)'; Watkins kers-¹ 'Dark, dirty'), thematic *ḱr̥s-nós 'black'\",\n      \"note\": \"The root box itself is right: a PIE colour root meaning 'black' is universally reconstructed on the strength of Sanskrit kṛṣṇá-, Old Prussian kirsnan, Lithuanian keršas 'black-and-white spotted', Old Church Slavonic črьnъ (Pokorny 583, Walde-Pokorny I 428, Watkins kers-¹, Buck 15.63/15.65). Nourai cites only OEW:182 (Shipley, The Origins of English Words), which is not accessible; but every standard authority agrees, and the AHD/Watkins appendix explicitly derives KRISHNA from '*krs-no- in Sanskrit krsna-, black, dark. [Pok. kers- 583]'. What is NOT part of this root is the Egyptian branch (node 1) that Nourai hangs on it: Egyptian km 'black' is Afro-Asiatic and has nothing to do with PIE. The entry therefore has one sound half (Sanskrit → Krishna) and one half that modern scholarship rejects (Egyptian → Greek → Arabic alchemy).\",\n      \"note_fa\": \"خودِ ریشه درست است: ریشهٔ رنگی هندواروپایی *ḱers- «سیاه» را همهٔ مراجع بازسازی می‌کنند، بر پایهٔ kṛṣṇá- سنسکریت، kirsnan پروسی باستان، keršas لیتوانیایی «سیاه‌وسپید خال‌دار» و črьnъ اسلاوی کهن کلیسایی (پوکورنی ص ۵۸۳، والده-پوکورنی ج ۱ ص ۴۲۸، واتکینز، باک بند ۱۵.۶۳). نورایی تنها به OEW:182 (شیپلی) ارجاع داده که در دسترس نیست، ولی پیوست ریشه‌های هندواروپایی فرهنگ American Heritage صریحاً «Krishna» را از *kr̥s-no- زیر همین ریشه می‌آورد. آنچه به این ریشه تعلّق ندارد شاخهٔ مصری است (خانهٔ ۱): واژهٔ مصری km «سیاه» آفروآسیایی است و هیچ پیوندی با هندواروپایی ندارد. بنابراین این مدخل یک نیمهٔ درست دارد (سنسکریت ← کریشنا) و یک نیمه که پژوهش امروزی آن را رد می‌کند (مصری ← یونانی ← عربی و کیمیا).\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Krishna\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"OEW:182\",\n          \"status\": \"not_checked\",\n          \"note\": \"Shipley, The Origins of English Words (1984) is lending-only on archive.org (originsofenglish0000ship / originsofenglish00jose; djvu.txt returns 401) and has no local copy — refs_online.json records local_file: null. Could not read p.182.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"p. 583 s.v. kers-\",\n          \"stance\": \"supports\",\n          \"note\": \"'Root / lemma: kers- | Meaning: a kind of colour (black) | Material: Old Indic krsna- \\\"black\\\" = Old Prussian kirsnan, FIN Kirsnappe = Old Bulgarian črьnъ, russ. černь, Serbo-Croatian crn etc. \\\"black\\\" (*čьrxnъ, *čьrsnъ); … Lithuanian keršas \\\"mottled, speckled black and white\\\" … References: WP. I 428 f. … Page(s): 583' (POK_full.txt lines 46432-46460).\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny I 428 (WLD_Bd1_pages.txt leaf 436)\",\n          \"stance\": \"supports\",\n          \"note\": \"'1. qers- und wohl auch bloßes qer- in Worten für Farben, bes. dunkle, schmutzige. Ai. kr̥ṣṇa- \\\"schwarz\\\" = apr. kirsnan ds., lett. Kirsna \\\"Name eines Flüßchens\\\" (etwa \\\"Schwarzwasser\\\") = abg. črьnъ, russ. čerenъ, skr. crn usw. \\\"schwarz\\\".'\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985 appendix s.v. kers-¹ (AHD_watkins1985.txt line 623)\",\n          \"stance\": \"supports\",\n          \"note\": \"'kers-¹. Dark, dirty. 1. Suffixed form *ker(s)-no- in Russian chërnyi, black: CHERNOZEM. 2. Suffixed zero-grade form *kr̥s-no- in Sanskrit kr̥ṣṇa-, black, dark: KRISHNA. [Pok. kers- 583.]' — note that Watkins lists no Egyptian or alchemical derivative under this root.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 15.63/15.65 (SYN.txt lines 26642, 26724)\",\n          \"stance\": \"supports\",\n          \"note\": \"'ChSl. črьnъ, etc., general Slavic : OPruss. kirsnan, Skt. kr̥ṣṇa- \\\"black\\\", further, Lith. keršas \\\"black and white\\\", keršė \\\"spotted cow\\\", etc., Sw., Norw. harr \\\"ashes\\\". Walde-P. 1.428.'\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Egyptian\",\n          \"words\": \"khem; chem\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The Egyptian words are real: km (Old Egyptian *kūmaw, Late Egyptian kēm, Coptic ⲕⲏⲙⲉ kēme) 'black', the perfective active participle of kmm 'to be black', and its feminine kmt 'the Black Land', the native name of Egypt from the black alluvium of the Nile — Nourai's glosses are correct. What is wrong is the arrow: Egyptian belongs to the Afro-Asiatic family, and km goes back to Proto-Afro-Asiatic *kum- 'to be black' (Wiktionary s.v. km, Egyptian, 'From Proto-Afroasiatic *kum- (\\\"to be black\\\")'), not to PIE *ḱers-. The resemblance of Eg. km to PIE *ḱr̥s-nós is chance: the two forms share neither the s nor the r, and no Egyptologist or Indo-Europeanist derives one from the other. Neither of Nourai's own references makes his claim — Watkins' AHD appendix lists no Egyptian material at all under kers-¹, and the current AHD (body, s.v. alchemy) mentions Egyptian kmt only as a later semantic influence on a Greek word, not as an Indo-European descendant.\",\n          \"derivation_fa\": \"واژه‌های مصری واقعی‌اند: km (مصری کهن *kūmaw، مصری متأخر kēm، قبطی ⲕⲏⲙⲉ kēme) «سیاه»، اسم مفعولِ فعل kmm «سیاه بودن»، و مؤنث آن kmt «سرزمین سیاه»، نام بومی مصر به سبب خاک سیاه کرانه‌های نیل؛ پس معنایی که نورایی می‌دهد درست است. آنچه نادرست است پیکان نمودار است: مصری از خانوادهٔ آفروآسیایی است و km به آفروآسیایی آغازین *kum- «سیاه بودن» بازمی‌گردد (ویکی‌واژه، مدخل km مصری)، نه به *ḱers- هندواروپایی. شباهت km مصری با *ḱr̥s-nós هندواروپایی تصادفی است، چراکه نه s دارد و نه r. خود مراجع نورایی هم این ادعا را تأیید نمی‌کنند؛ پیوست واتکینز زیر ریشهٔ kers- هیچ مادّهٔ مصری نمی‌آورد. پژوهش امروزی این پیکان را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/km#Egyptian\",\n            \"https://www.ahdictionary.com/word/search.html?q=alchemy\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:30\",\n              \"status\": \"partial\",\n              \"note\": \"AHD p.30 is the body page with 'alchemy'. The current AHD entry (archived) reads: '[Middle English alkamie, from Old French alquemie, from Medieval Latin alchymia, from Arabic al-kīmiyāʾ … (from Late Greek khēmeia, probably alteration of khumeia, from Greek khein, khu-, to pour; see gheu- in the Appendix … (influenced, owing to the reputation of Egyptian alchemists, by Greek Khēmiā, Egypt, from Egyptian kmt, Egypt, from feminine of km, black, in reference to the black soil of the Nile valley))].' So AHD does give Egyptian km 'black' — but only as a secondary INFLUENCE on a Greek word whose real source is khumeia, and it never places Egyptian km under an Indo-European root.\"\n            },\n            {\n              \"ref\": \"OEW:182\",\n              \"status\": \"not_checked\",\n              \"note\": \"Shipley 1984 p.182 is lending-only on archive.org and not held locally; this is the only reference that could actually be asserting the Egyptian-from-PIE claim.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 appendix s.v. kers-¹ (AHD_watkins1985.txt line 623)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Watkins' full material for kers-¹ is 'Russian chërnyi … Sanskrit kr̥ṣṇa- … [Pok. kers- 583]'; ALCHEMY is not indexed to kers- (nor, in the 1985 appendix, to gheu-, whose English derivatives are listed as CHOANA, CHYLE, CHYME, ECCHYMOSIS, PARENCHYMA). No Egyptian word is admitted to the root.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1157 (LKT.txt line 2718)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Ä[gyptisch] kmt, kopt. kēmi \\\"schwarz\\\" war die Bezeichnung des Landes Ägypten … hieraus entstand ar. kīmijāʾ' — Lokotsch supports the Egyptian ETYMON of kīmiyāʾ, but treats it as an Egyptian (Hamito-Semitic) word, with no Indo-European ancestry.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 583 s.v. kers-\",\n              \"stance\": \"silent\",\n              \"note\": \"Pokorny's material under kers- is exclusively Indo-Iranian, Baltic, Slavic and Germanic; no Egyptian, Semitic or Afro-Asiatic form appears.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Greek\",\n          \"words\": \"xěma\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Two problems. (a) The form: no Greek word *χῆμα/xěma with these meanings exists. What the sources know are Χημία (Khēmía) 'Egypt' (Plutarch, De Iside 33) and the technical noun χημεία / χυμεία (khēmeía / khumeía) 'the art of transmuting metals', first attested c. 300 CE in Diocletian's decree against 'the old writings of the Egyptians'. Nourai's 'xěma' conflates the two; the printed page (PDF p.260, image saved to data/verification/sources/refs/ocr/BOOK/260.png) shows 'xěma' exactly as the JSON has it, so this is the author's own compression, not a scanning error. (b) The derivation: modern scholarship prefers the other of the two competing origins. Wiktionary, Skeat and the current AHD all take the base word to be χυμείᾱ (khumeíā) 'art of alloying metals', from χύμα (khúma) 'ingot, that which is poured' < χέω 'I pour' < PIE *ǵʰew-, with Χημία 'Egypt' acting only as a later influence on the spelling with η (the 'popular association' Mahn describes in the OED). Klein 1966 p.45, whom Nourai follows, calls the khumeia derivation 'folk etymology', but he is now the minority view; Etymonline sums up the present consensus as 'of uncertain origin … the word seems to have elements of both origins'.\",\n          \"derivation_fa\": \"دو اشکال در این خانه هست. نخست صورت واژه: در یونانی واژه‌ای به شکل *χῆμα با این معانی وجود ندارد؛ آنچه منابع می‌شناسند Χημία (Khēmía) «مصر» است (پلوتارک، دربارهٔ ایزیس ۳۳) و اصطلاح χημεία / χυμεία «هنر دگرگون‌کردن فلزات» که نخستین بار نزدیک سال ۳۰۰ میلادی در فرمان دیوکلتیانوس علیه «نوشته‌های کهن مصریان» دیده می‌شود؛ نورایی این دو را در هم آمیخته و صورت «xěma» ساخته است. تصویر صفحهٔ چاپی (پیوست: 260.png) نشان می‌دهد که خود کتاب همین «xěma» را چاپ کرده، پس خطای خوانش اسکن در کار نیست و خطا از کتاب است. دوم ریشه‌شناسی: پژوهش امروزی سوی دیگر این اختلاف را برمی‌گزیند و واژهٔ پایه را χυμείᾱ «هنر آمیختن فلزات» از χύμα «شمش، آنچه ریخته شود» و آن از χέω «می‌ریزم» و ریشهٔ *ǵʰew- می‌داند (ویکی‌واژه، اسکیت، فرهنگ American Heritage)، و Χημία «مصر» را تنها عاملی می‌شمارد که بعدها بر املای واژه با η اثر گذاشته است. کلاین (ص ۴۵) که نورایی از او پیروی کرده، این ریشه‌شناسی را «ریشه‌شناسی عامیانه» می‌خواند، ولی امروز نظر اقلیت است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"xěma\",\n          \"correct_form\": \"Χημία (Khēmía) 'Egypt' / χημεία ~ χυμεία (khēmeía, khumeía) 'the art of transmutation'\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alchemy\",\n            \"https://en.wiktionary.org/wiki/alchemy\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:45\",\n              \"status\": \"supports\",\n              \"note\": \"Klein 1966 s.v. alchemy (KLN_1966.txt line 2130): '…fr. Arab. al-kīmiyā, fr. al-, \\\"the\\\", and MGk. χημεία, prop. \\\"the art of the black land (Egypt)\\\", fr. Gk. Χημία, \\\"Black-land, Egypt\\\", fr. Egypt. khem, khame, \\\"black\\\". The derivation from Gk. χυμεία, \\\"pouring\\\", from the stem of χέειν, \\\"to pour\\\", is folk etymology. See W. Muss-Arnolt, TAPA vol. XXIII, p.149.' Klein does say what Nourai's arrow says — but he prints Χημία, not 'xěma'.\"\n            },\n            {\n              \"ref\": \"AHD:30\",\n              \"status\": \"contradicts\",\n              \"note\": \"The AHD alchemy entry makes khēmeia 'probably alteration of khumeia, from Greek khein, khu-, to pour; see gheu-', with Khēmiā/Egyptian kmt only as an influence — the reverse of Nourai's arrow, which makes the Egyptian word the source.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Alchemy (SKT.txt line 519)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'Alchemy. (F.-Arab.-Gk.) O.F. alchemie … Arab. al, the; and kīmiyā, alchemy. — Late Gk. χυμεία, chemistry; for χυμεία = mingling. — Gk. χέειν, to pour out, mix. (√GHU.)' Skeat gives only the khumeia route, with no Egyptian element.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls vol. I s.v. alchemy (FSD_vol1.txt lines 11266, 11274)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"Etymology line: '< Gr. chemeia, for chymeia, infusion, < cheō, pour.' Its note adds: 'Some lexicographers derive this word from the Greek Chemeia, Egypt (in ancient Egyptian, Khem-) … But as alchemy signifies the transmutation of metals … this word is more probably derived from the same Egyptian source as chemistry.'\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1157 (LKT.txt line 2718)\",\n              \"stance\": \"partial\",\n              \"note\": \"Lokotsch takes the Egyptian side ('Äg. kmt, kopt. kēmi \\\"schwarz\\\" … hieraus entstand ar. kīmijāʾ') but passes directly from Egyptian to Arabic without a Greek intermediate, so he does not support this particular Greek node either.\"\n            },\n            {\n              \"src\": \"WEB\",\n              \"where\": \"Webster's New Twentieth Century Dictionary (WEB local file)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for 'khemeia'/'chymeia' in the local vol. 1 text produced nothing usable (the A-section OCR of this volume is very poor).\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Arabic\",\n          \"words\": \"al-kimyâ, al-kîmîya\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Arabic word is genuine and its role as the transmitter to Europe is beyond doubt: al-kīmiyāʾ (اَلْكِيمِيَاء), with the article al-, 'the art of transmutation', later 'chemistry', is the source of Medieval Latin alchimia/alchymia and of every European reflex. What is only 'plausible' is the parent drawn above it. Wiktionary derives Arabic كيمياء directly 'from Ancient Greek χυμείᾱ (khumeíā)', not from a word for Egypt; the same is true of Skeat and of the AHD. The chart's own NOTE frames the question exactly right — OEW:124 and FSD:66 propose Greek khumeia 'infusion' from the root Gheu 'to pour', while KLN:45 rejects it as folk etymology — and modern scholarship comes down on the OEW/FSD side, though not unanimously: Etymonline (following the OED and Mahn) concludes 'of uncertain origin … The word seems to have elements of both origins', and Lokotsch no.1157 still derives kīmiyāʾ from Egyptian kmt. Nourai's two transliterations render one word (al-kīmiyāʾ); the vowel of the second syllable is long ī, so 'al-kimyâ' is a colloquial short form.\",\n          \"derivation_fa\": \"واژهٔ عربی «الکیمیاء» راستین است و نقش آن در انتقال این دانش به اروپا جای تردید ندارد: از همین صورت است که لاتینی سده‌های میانه alchimia/alchymia و از آن همهٔ صورت‌های اروپایی برآمده‌اند. آنچه تنها «با احتیاط پذیرفتنی» است، پدرِ ترسیم‌شده در بالای آن است. ویکی‌واژه، اسکیت و فرهنگ American Heritage «كيمياء» را مستقیماً وام‌گرفته از یونانی χυμείᾱ (khumeíā) می‌دانند، نه از نام مصر. یادداشت خودِ نمودار این اختلاف را درست بازگو کرده است: OEW و FSD واژه را از χυμεία «آمیختن، دم‌کردن» و ریشهٔ *ǵʰew- «ریختن» می‌گیرند و کلاین آن را «ریشه‌شناسی عامیانه» می‌خواند؛ پژوهش امروزی جانب OEW و FSD را می‌گیرد، هرچند نه به اتفاق: Etymonline به پیروی از OED و مان می‌نویسد «خاستگاهش نامعلوم است … واژه گویا از هر دو خاستگاه عناصری دارد» و لوکوچ هنوز آن را از kmt مصری می‌گیرد. دو آوانگاشتِ نورایی یک واژه‌اند؛ صورت درست al-kīmiyāʾ با ī کشیده است و «al-kimyâ» گونهٔ گفتاری کوتاه‌شده.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%83%D9%8A%D9%85%D9%8A%D8%A7%D8%A1\",\n            \"https://www.etymonline.com/word/alchemy\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"AHD s.v. alchemy: 'from Arabic al-kīmiyāʾ: al-, the + kīmiyāʾ, chemistry (from Late Greek khēmeia, probably alteration of khumeia …)'. AHD confirms the Arabic form, the article al-, and the Greek origin — but makes the Greek source khumeia, not a word for Egypt.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. alchemy (p.45; KLN_1966.txt line 2130)\",\n              \"stance\": \"supports\",\n              \"note\": \"'fr. ML. alchemia, fr. Arab. al-kīmiyā, fr. al-, \\\"the\\\" …' — the Arabic step is exactly as drawn.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1157\",\n              \"stance\": \"supports\",\n              \"note\": \"'ar. kīmijāʾ zunächst zur Bezeichnung des \\\"Steins der Weisen\\\" … dann \\\"Scheidekunst, Chemie\\\". Aus dem Ar. kommt: it. alchimia … frz. alchimie, chimie, sp. pg. alquimia; dtsch. Alchimie, Chemie … engl. alchemy'. He also notes '[Die ar. Lexikographen leiten ar. kīmijāʾ vom Vb. kamā \\\"verbergen\\\" ab, also im Sinne von \\\"verborgener Kunst\\\"]' — the native Arabic folk etymology.\"\n            },\n            {\n              \"src\": \"AFM\",\n              \"where\": \"Addi Shir, al-Alfāẓ al-fārisiyya al-muʿarraba (AFM_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'كيمياء' / 'الكيمياء' returns nothing — as expected, since Addi Shir catalogues Persian words arabised, and kīmiyāʾ is not one of them.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Alchemy (SKT.txt line 519)\",\n              \"stance\": \"partial\",\n              \"note\": \"'Arab. al, the; and kīmiyā, alchemy. — Late Gk. χυμεία' — the Arabic word is confirmed, its Greek parent is khumeia.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"kîmîyâ «کیمیا»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian کیمیا kīmiyā 'alchemy; the philosopher's stone; hence anything exceedingly rare and precious' is a loan from Arabic al-kīmiyāʾ, taken over without the article and with the ʾ (hamza) of the Arabic ending dropped, as regularly in Persian arabisms of the CiCyāʾ shape (cf. کبریا, سیمیا). The Persian development is semantic rather than phonetic: from the technical 'art of transmutation' the word became a byword for the unobtainable, as in Sūzanī's line quoted in the chart, 'آنان که در مخالفت پادشاه دین — بردند دستبرد به مکر و به کیمیا'; this 'rare substance' sense is the second gloss Nourai gives and is the one Borhan-e Qateʿ registers. In Afghan and Tajik Persian کیمیا / кимиё remained the word for chemistry, where Iranian Persian later took شیمی from French (node 7) — the two are doublets of the same Greek etymon.\",\n          \"derivation_fa\": \"«کیمیا» در فارسی نو وام‌واژه‌ای از عربی «الکیمیاء» است که بی‌الف‌ولام و با افتادن همزهٔ پایانی وارد شده، همان‌گونه که در دیگر معرّب‌های هم‌ساخت (کبریا، سیمیا) دیده می‌شود. تحول این واژه در فارسی بیشتر معنایی است تا آوایی: از معنای فنّی «هنر تبدیل فلزات» به معنای «چیز کمیاب و دست‌نیافتنی» رسیده است، چنان‌که در بیت سوزنی که نورایی نقل کرده («آنان که در مخالفت پادشاه دین / بردند دستبرد به مکر و به کیمیا») و در برهان قاطع آمده. در فارسی افغانستان و تاجیکستان «کیمیا / кимиё» همچنان به معنی «شیمی» به کار می‌رود، حال آنکه فارسی ایران بعدها «شیمی» را از فرانسه گرفت؛ این دو دوگانه (doublet) از یک اصل یونانی‌اند. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%85%DB%8C%D8%A7\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:1759\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qateʿ, local scan incoming/BQT/BQT_v3_pages.txt pdf page 556 = printed p.1761 of the Ibn Sina reprint (Nourai's 1759 is the same 2-page offset seen at BQT:1795): headword 'کیمیا … بمعنی مکر و حیله باشد و عملی است مشهور نزد اهل صنعت که بسبب امتزاج روح … اجساد ناقصه را بدرجهٔ کمال رسانند یعنی قلعی و مس را نقره و طلا کنند', with Mo'in's footnote 5: 'از یونانی xēmeia «اشتینگاس» (بمعنی اختلاط و امتزاج)، فرانسه alchimie, chimie، انگلیسی chemistry'. The headword, glosses and the Sūzanī verse of the chart all come from this page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qateʿ printed p.1761 s.v. کیمیا, with Mo'in's fn. 5\",\n              \"stance\": \"partial\",\n              \"note\": \"Mo'in confirms the Greek origin and the French/English cognates but glosses the Greek as 'اختلاط و امتزاج' (mixing, blending) — i.e. he reads it as khumeia, not as the name of Egypt, siding against Nourai's Egyptian branch.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in / Dehkhoda via abadis.ir s.v. شیمی\",\n              \"stance\": \"supports\",\n              \"note\": \"'شیمی. (فرانسوی، اِ) (مأخوذ از کلمهٔ «کیمیا»)' — Mo'in treats کیمیا as the older, Arabic-mediated form beside the French neologism.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e riše-hā-ye hend-o-orupāyi (ARY_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'کیمیا' in the Aryanpur scan finds no headword — the book covers inherited Indo-European vocabulary of Persian, and an Arabic/Greek loan falls outside it.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"alchymia\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"This is Medieval, not Classical, Latin: alchimia / alchymia appears in the Latin translations of Arabic scientific works made in twelfth-century Spain (Robert of Chester's 1144 Liber de compositione alchimiae is the earliest landmark), the Arabic definite article al- having been swallowed into the stem, as in algebra, alcohol, alkali. The spelling with -y- is a Renaissance hellenising respelling after Greek χυμεία / χημεία. From this Medieval Latin form come Old French alquemie (13th c.) and alchimie (14th c.), and hence Italian alchimia, Spanish alquimia and English alchemy. Nourai's box, labelled simply 'Latin', is right in substance but hides the medieval date.\",\n          \"derivation_fa\": \"این صورت لاتینی سده‌های میانه است، نه لاتینی کلاسیک: alchimia/alchymia در ترجمه‌های لاتینی آثار علمی عربی در اسپانیای سدهٔ دوازدهم پدید آمد (کهن‌ترین نشانه، «کتاب ترکیب کیمیا» ترجمهٔ رابرت چستری به سال ۱۱۴۴ میلادی)، و در آن حرف تعریف عربی «ال» جزوِ خودِ ستاک شده است، چنان‌که در algebra و alcohol و alkali. املای آن با y از سر یونانی‌نویسی دورهٔ رنسانس و به قیاس χυμεία/χημεία است. از همین صورت است که فرانسهٔ کهن alquemie (سدهٔ ۱۳) و alchimie (سدهٔ ۱۴) و سپس ایتالیایی alchimia، اسپانیایی alquimia و انگلیسی alchemy برآمده‌اند. خانهٔ نمودار که تنها «Latin» برچسب خورده از نظر محتوا درست است ولی سدهٔ میانه بودن آن را پنهان می‌کند.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alchemy\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"AHD s.v. alchemy: 'Middle English alkamie, from Old French alquemie, from Medieval Latin alchymia, from Arabic al-kīmiyāʾ' — AHD prints exactly the form alchymia that Nourai's box gives, and labels it Medieval Latin.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. alchemy (p.45)\",\n              \"stance\": \"supports\",\n              \"note\": \"'OF. alquemie (13th cent.), alchimie (14th cent.) (F. alchimie), fr. ML. alchemia, fr. Arab. al-kīmiyā' — Klein spells the Medieval Latin alchemia.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1157\",\n              \"stance\": \"supports\",\n              \"note\": \"'Aus dem Ar. kommt: it. alchimia \\\"Goldmacherkunst\\\" … frz. alchimie, chimie, sp. pg. alquimia; dtsch. Alchimie … Chemie' — the Romance forms all presuppose the Medieval Latin.\"\n            },\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout–Meillet (LAT.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'alchimia'/'alchymia' returns nothing: Ernout–Meillet covers Classical Latin only, so the absence is itself evidence that the word is medieval.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"alchemie, chimie\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The first word is right and the second is right in fact but simplified in route. Old French alquemie (13th c.) / alchimie (14th c.), modern French alchimie, is the direct continuation of Medieval Latin alchimia. French chimie, however, is not simply alchimie with the Arabic article stripped off in speech: it is a sixteenth-century learned formation, Middle French chymie, borrowed from New Latin chimia — the term the Paracelsian physicians coined for the practical part of the art — which in turn was formed on Greek χυμεία (Wiktionary's etymology tree for شیمی: 'Ancient Greek χυμείᾱ (khumeíā) influ. → New Latin chimia → Middle French chymie → French chimie'). The two French words are therefore doublets that converge, not a single chain; and it was the new chimie, not alchimie, that carried the modern scientific sense after c. 1600.\",\n          \"derivation_fa\": \"واژهٔ نخست درست است و دومی از نظر واقعیت درست ولی از نظر مسیر ساده‌سازی‌شده. فرانسهٔ کهن alquemie (سدهٔ ۱۳) و alchimie (سدهٔ ۱۴) و فرانسهٔ امروزی alchimie دنبالهٔ مستقیم لاتینی میانهٔ alchimia است. اما chimie فرانسوی صرفاً alchimie بی‌«ال» نیست: صورتی است دانشورانه از سدهٔ شانزدهم، فرانسهٔ میانه chymie، وام‌گرفته از لاتینی نو chimia — اصطلاحی که پزشکان پیرو پاراسلسوس برای بخش عملی این هنر ساختند — و آن خود بر پایهٔ χυμεία یونانی است (چنان‌که درخت ریشه‌شناسی ویکی‌واژه در مدخل «شیمی» نشان می‌دهد). پس این دو واژهٔ فرانسوی دوگانه‌اند و در یک زنجیرهٔ پیوسته نمی‌گنجند؛ و پس از حدود ۱۶۰۰ میلادی این chimie تازه بود، نه alchimie، که معنای علمی امروزین را بر دوش گرفت.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D9%85%DB%8C\",\n            \"https://www.etymonline.com/word/alchemy\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The chart gives no reference for this node; the check was done against Klein, Lokotsch and Wiktionary instead (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.vv. alchemy, chemist (KLN_1966.txt lines 2130, 7333)\",\n              \"stance\": \"supports\",\n              \"note\": \"'OF. alquemie (13th cent.), alchimie (14th cent.) (F. alchimie)'; and 'chemist, n. — F. chimiste, fr. chimie, \\\"chemistry\\\". See alchemy and -ist.' Klein has both French words but, like Nourai, routes chimie through alchemy.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch no. 1157\",\n              \"stance\": \"supports\",\n              \"note\": \"'frz. alchimie, chimie' listed side by side as the French outcomes of Arabic kīmiyāʾ.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls vol. I s.v. alchemy\",\n              \"stance\": \"partial\",\n              \"note\": \"Its etymology '< Gr. chemeia, for chymeia, infusion, < cheō, pour' presupposes the Greek base of chimie rather than a French shortening of alchimie.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"šîmî «شیمی»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Persian شیمی šimi 'chemistry' is a nineteenth-century borrowing straight from French chimie, part of the wave of French scientific vocabulary that entered Persian through the Dār al-Fonūn: the French [ʃ] of chimie is rendered by ش, the nasal-free -ie by -ی, giving šimi. Wiktionary states it flatly: 'شیمی — Borrowed from French chimie.' The Persian Wikipedia article archived with this check dates the first use to Mīrzā Ṣāleḥ Šīrāzī's 1831 treatise on natural science, later taught at the Dār al-Fonūn as رسالهٔ طبیعیات. شیمی is thus a doublet of the older Arabic-mediated کیمیا (node 4) — the same Greek word, once through Arabic in the ninth century and once through French in the nineteenth — and Iranian Persian uses شیمی where Afghan and Tajik Persian kept کیمیا / кимиё.\",\n          \"derivation_fa\": \"«شیمی» وام‌واژه‌ای است از فرانسوی chimie که در سدهٔ نوزدهم میلادی، در موج ورود واژگان علمی فرانسوی از راه دارالفنون، به فارسی راه یافت: [ʃ] فرانسوی به «ش» و پایانهٔ -ie به «ی» بدل شده و صورت šimi پدید آمده است. ویکی‌واژه صریح می‌نویسد: «شیمی، وام‌گرفته از فرانسوی chimie». بنا بر ویکی‌پدیای فارسی (بایگانی‌شده در همین بررسی) نخستین کاربرد آن در رسالهٔ علوم طبیعی میرزا صالح شیرازی به سال ۱۸۳۱ است که بعدها با نام «رسالهٔ طبیعیات» در دارالفنون تدریس می‌شد. پس «شیمی» دوگانهٔ (doublet) واژهٔ کهن‌ترِ «کیمیا» است: یک واژهٔ یونانی که یک بار در سدهٔ سوم هجری از راه عربی و یک بار در سدهٔ سیزدهم از راه فرانسه به فارسی رسیده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B4%DB%8C%D9%85%DB%8C\",\n            \"https://abadis.ir/fatofa/%D8%B4%DB%8C%D9%85%DB%8C/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:2115\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in's Farhang-e Fārsi is not on disk in a page-numbered form (MON_part1/part2 cover only part of the lexicon and have no page markers), but the entry text is served verbatim by abadis.ir: 'شیمی. (فرانسوی، اِ) (مأخوذ از کلمهٔ «کیمیا») علمی است که در آن از خواص اجسام طبیعی و تغییرات عمیق گوهرها و عناصر بحث می‌شود … (از فرهنگ فارسی معین)'. Mo'in's tag (فرانسوی) is exactly the origin Nourai's arrow draws.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Farhang-e Fārsi s.v. شیمی (via abadis.ir, archived)\",\n              \"stance\": \"supports\",\n              \"note\": \"'(فرانسوی، اِ) (مأخوذ از کلمهٔ «کیمیا»)'.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qateʿ p.1761 s.v. کیمیا, Mo'in's fn. 5\",\n              \"stance\": \"supports\",\n              \"note\": \"Mo'in's own footnote already lists 'فرانسه alchimie, chimie، انگلیسی chemistry' as the modern descendants, which is where شیمی comes from.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur (ARY_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'شیمی' finds only compounds in running text, no headword; a modern French loan is outside the scope of a dictionary of Indo-European roots of Persian.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"chemistry, alchemist\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Both English words come through French, as the chart draws. alchemist is Old French alqemiste (modern alchimiste), i.e. alquemie + -iste, borrowed in the fifteenth century (Klein: 'alchemist, n. — OF. alqemiste (F. alchimiste), fr. alqemie. See alchemy and -ist'). chemistry is a two-step English formation: French chimiste gave English chemist (16th c.), and chemist + -ry produced chemistry about 1600 (Klein: 'chemist, n. — F. chimiste, fr. chimie, \\\"chemistry\\\". … Derivative: chemist-ry, n.'). Etymonline dates and glosses it 'c. 1600, \\\"alchemy\\\", from chemist + -ry', with the modern sense 'scientific study of the composition of material things' only by 1788, after chemistry had separated itself from alchemy in the mid-1600s.\",\n          \"derivation_fa\": \"هر دو واژهٔ انگلیسی، چنان‌که در نمودار آمده، از راه فرانسه رسیده‌اند. alchemist از فرانسهٔ کهن alqemiste (امروزی alchimiste)، یعنی alquemie + پسوند -iste، است که در سدهٔ پانزدهم میلادی وام گرفته شد؛ کلاین می‌نویسد: «alchemist — از فرانسهٔ کهن alqemiste، از alqemie». اما chemistry ساختی دومرحله‌ای در خود انگلیسی است: فرانسوی chimiste واژهٔ chemist را در سدهٔ شانزدهم به انگلیسی داد و از chemist + پسوند -ry حدود سال ۱۶۰۰ واژهٔ chemistry ساخته شد (کلاین: «chemist از فرانسوی chimiste از chimie … مشتق: chemistry»). بنا بر Etymonline معنای نخستین آن همان «کیمیاگری» بود و معنای علمی امروزین تا سال ۱۷۸۸ پدید نیامد، پس از آنکه شیمی در میانهٔ سدهٔ هفدهم از کیمیا جدا شد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/alchemy\",\n            \"https://en.wiktionary.org/wiki/chemistry\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:45\",\n              \"status\": \"supports\",\n              \"note\": \"KLN_1966.txt: the alchemy article on p.45 closes 'Cp. chemical, chemist, chemistry'; the neighbouring headword (line 2129) reads 'alchemist, n. — OF. alqemiste (F. alchimiste), fr. alqemie. See alchemy and -ist'; and line 7333 'chemist, n. — F. chimiste, fr. chimie, \\\"chemistry\\\". See alchemy and -ist. Derivative: chemist-ry, n.' All three English words are referred back to p.45, exactly as Nourai's citation implies.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.vv. alchemist, chemist (pp.45, ~285)\",\n              \"stance\": \"supports\",\n              \"note\": \"See ref_check.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat s.v. Alchemy (SKT.txt line 519)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Alchemy. (F.-Arab.-Gk.) O.F. alchemie' — Skeat too routes the English word through Old French.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls vol. I s.v. alchemy / alchemist (FSD_vol1.txt lines 11256-11258)\",\n              \"stance\": \"supports\",\n              \"note\": \"'al'che-mist, n. One who was skilled in or who practised alchemy'; 'al-chem'is-try, n. Alchemy' — the same family, with the same French-Arabic-Greek etymology line.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"Krishna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sanskrit कृष्ण kṛṣṇá- 'black, dark' is the textbook reflex of PIE *ḱr̥s-nós, the thematic -no- derivative of the colour root of this entry: PIE *ḱ > Indo-Iranian ś/š, syllabic *r̥ is kept as r̥ in Sanskrit, and *-sn- gives -ṣṇ- by ruki retroflexion. Wiktionary's tree runs 'PIE *kers- + *-nós → *kr̥snós → Proto-Indo-Iranian *kr̥šnás → Sanskrit कृष्ण'. The exact cognates are Old Prussian kirsnan and Old Church Slavonic črьnъ (Pokorny 583). As a proper name Kṛṣṇa is the dark-complexioned eighth avatāra of Viṣṇu, and the name is simply the adjective used as an epithet — so Nourai's gloss 'the black one, title of an Indian God' is precise.\",\n          \"derivation_fa\": \"سنسکریت कृष्ण (kṛṣṇá-) «سیاه، تیره» بازتاب کلاسیک *ḱr̥s-nós هندواروپایی است، یعنی مشتقّ -no-دار همان ریشهٔ رنگی این مدخل: *ḱ هندواروپایی در هندوایرانی به ś/š بدل شده، *r̥ هجایی در سنسکریت همچنان r̥ مانده، و خوشهٔ *-sn- بر اثر قاعدهٔ «روکی» به -ṣṇ- تبدیل شده است. درخت ریشه‌شناسی ویکی‌واژه چنین است: *kers- + *-nós ← *kr̥snós ← هندوایرانی آغازین *kr̥šnás ← سنسکریت कृष्ण. هم‌ریشه‌های دقیق آن kirsnan پروسی باستان و črьnъ اسلاوی کهن کلیسایی‌اند (پوکورنی ص ۵۸۳). کریشنا در مقام نام خاص، هشتمین اوتارهٔ ویشنو با چهرهٔ تیره است و نام او همان صفت است که لقب شده؛ پس معنایی که نورایی می‌دهد («سیاه، لقب خدایی هندی») دقیق است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E0%A4%95%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A3\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"OEW:182\",\n              \"status\": \"not_checked\",\n              \"note\": \"Shipley 1984 is lending-only on archive.org with no local copy; p.182 could not be read. The claim itself, however, is confirmed by four other authorities (see consulted).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 583 s.v. kers-\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old Indic krsna- \\\"black\\\" = Old Prussian kirsnan … = Old Bulgarian črьnъ, russ. černь, Serbo-Croatian crn etc. \\\"black\\\"'; and the appended Note: 'Old Church Slavic: črьnъ \\\"black\\\" : Lithuanian kirsnas \\\"black (of a horse)\\\" : Old Prussian kirsnan \\\"black\\\" : Krishna \\\"Vedic black god\\\".'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 s.v. kers-¹\",\n              \"stance\": \"supports\",\n              \"note\": \"'2. Suffixed zero-grade form *kr̥s-no- in Sanskrit kr̥ṣṇa-, black, dark: KRISHNA. [Pok. kers- 583.]' — and the index line 'KRISHNA kers-¹' (AHD_watkins1985.txt line 1722).\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny I 428 (leaf 436)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Ai. kr̥ṣṇa- \\\"schwarz\\\" = apr. kirsnan ds. … = abg. črьnъ … \\\"schwarz\\\" (*čьrxnъ : *čьrsnъ; s. Berneker 169).'\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 15.65 (SYN.txt line 26724)\",\n              \"stance\": \"supports\",\n              \"note\": \"'ChSl. črьnъ, etc. … : OPruss. kirsnan, Skt. kr̥ṣṇa- \\\"black\\\" … Walde-P. 1.428.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"Krishna\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English Krishna is a direct transliteration-borrowing of Sanskrit कृष्ण kṛṣṇa- (Wiktionary: 'Sanskrit कृष्ण (kṛṣṇa) bor. → English Krishna'), which entered English in the eighteenth century with the first English accounts and translations of Hindu scripture — Charles Wilkins' Bhagavad-Gita of 1785 fixed the spelling with -sh- for the retroflex ṣ. Earlier and independent English forms of the same name, taken through the Prakrits and the modern vernaculars rather than from Sanskrit, are Kanha and the Anglo-Indian Kistna (the river). This node is thus a learned scholarly borrowing, not an inherited form.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی Krishna آوانگاشتی مستقیم از سنسکریت कृष्ण (kṛṣṇa) است — ویکی‌واژه می‌نویسد «از سنسکریت कृष्ण وام گرفته شده» — و در سدهٔ هجدهم میلادی همراه با نخستین گزارش‌ها و ترجمه‌های انگلیسی از متون هندو وارد انگلیسی شد؛ ترجمهٔ بهگودگیتا به قلم چارلز ویلکینز (۱۷۸۵) املای -sh- را برای ṣ برگشتی (retroflex) تثبیت کرد. صورت‌های کهن‌تر و مستقل همین نام در انگلیسی، مانند Kanha و Kistna (نام رود) که از راه پراکریت‌ها و زبان‌های بومی امروزی رسیده‌اند، نشان می‌دهد که این خانه وام‌گیری دانشورانه است نه صورت موروثی. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Krishna\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"OEW:182\",\n              \"status\": \"not_checked\",\n              \"note\": \"Shipley 1984 p.182 not accessible (lending-only, no local copy).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 index (AHD_watkins1985.txt line 1722)\",\n              \"stance\": \"supports\",\n              \"note\": \"'KRISHNA kers-¹' — the English headword is indexed to the root, i.e. treated as the Sanskrit word taken into English.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 (KLN_1966.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'Krishna' finds no headword; Klein does not treat this proper name.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 583 s.v. kers-, Note\",\n              \"stance\": \"supports\",\n              \"note\": \"'Krishna \\\"Vedic black god\\\"' is listed by the editors of the electronic Pokorny alongside the Baltic and Slavic cognates.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"Persian\",\n          \"words\": \"Krîšnâ «کریشنا»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Persian کریشنا Krišnā, the name of the Hindu god, is certainly a modern borrowing and not an inherited Iranian word — had it been inherited, the PIE root would have given Persian a form with s, not š + n, and with a different vowel. The shape of the Persian form, with the cluster kr- preserved and with š rendering ṣ, points to a written European (English or French) transmission, which is what Nourai's arrow from the English box asserts; the alternative, direct transliteration from Sanskrit or from Hindi कृष्ण by Persian Indologists, would give the same result, so the specific intermediary cannot be proved. The chart is right that this is a loan and right about its ultimate source; only the exact route is unverifiable, hence 'plausible'.\",\n          \"derivation_fa\": \"«کریشنا» در فارسی نام خدای هندو و بی‌گمان وام‌واژه‌ای امروزی است، نه واژه‌ای موروثی؛ اگر موروثی می‌بود، ریشهٔ هندواروپایی در فارسی صورتی با s و آوایی دیگر می‌داد نه š + n. ساخت این صورت فارسی، با نگاه‌داشتِ خوشهٔ آغازین kr- و برگرداندن ṣ به «ش»، نشان می‌دهد که از راه نوشتار اروپایی (انگلیسی یا فرانسوی) رسیده است، و این همان است که پیکان نورایی از خانهٔ انگلیسی ادعا می‌کند؛ ولی آوانویسی مستقیم از سنسکریت یا از हिन्दी به دست هندشناسان ایرانی نیز همین نتیجه را می‌داد، پس واسطهٔ دقیق را نمی‌توان اثبات کرد. نمودار در وام‌واژه بودن و در خاستگاه نهایی درست است و تنها مسیر آن اثبات‌ناپذیر می‌ماند؛ از این رو «با احتیاط پذیرفتنی» است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%DA%A9%D8%B1%DB%8C%D8%B4%D9%86%D8%A7/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON5:1572\",\n              \"status\": \"not_checked\",\n              \"note\": \"Mo'in vol. 5 (the aʿlām / proper-name volumes) is not on disk and vajehyab/abadis serve only the lexicon volumes 1-3; a query for کریشنا on abadis.ir (archived) returns a name-dictionary gloss 'اسم: کریشنا (پسر) (سانسکریت)' and Wikipedia articles, but no text of Mo'in's aʿlām entry, so p.1572 could not be read.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"abadis.ir aggregation of Persian dictionaries s.v. کریشنا (archived)\",\n              \"stance\": \"partial\",\n              \"note\": \"'اسم: کریشنا (پسر) (سانسکریت) (تلفظ: kerishna)' — the Persian name dictionaries label the word a Sanskrit borrowing, which confirms the loan status but not the English intermediary.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 index\",\n              \"stance\": \"supports\",\n              \"note\": \"'KRISHNA kers-¹' confirms the ultimate etymon that the Persian form transmits.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur (ARY_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep 'کریشنا' finds nothing; Aryanpur treats only inherited Indo-European vocabulary of Persian, not modern proper-name loans.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-06T16:37:59.273Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-260.json (file state is current in your context — no need to Read it back)
```


## [2026-09-06T16:37:59.708Z] AGENT

You've hit your session limit · resets 3:40pm (America/Toronto)
