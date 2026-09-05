# Verification process log — verify-page-139


## [2026-09-05T20:08:08.418Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 139 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-139.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-139.json. Write /home/sfmqrb/git/rishe/data/verification/page-139.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 139` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:08:10.040Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:08:10.765Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:08:10.779Z] TOOL RESULT

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


## [2026-09-05T20:08:10.887Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-139.txt"
}
```


### [2026-09-05T20:08:10.906Z] TOOL RESULT

```
1	=== PDF page 139 (book page 109) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dô 2 : to give, create  (refs POK:223)
4	#1 (parent #0) [Avestan / Sanskrit] refs=BQT:121; POK:223,225 | dâ 4 : to give ; dâtar : giver, God
5	#2 (parent #0) [Pahlavi] refs=NYB:56; HRN:61,115 | dâtan : to give ; dâdâr : God ; dâhišn : gift ; paiti-dâhišn : reward, given back ☞Per 3
6	  #3 (parent #2) [Persian] refs=BQT:289,815; FSF:169; SNS:295 | dâdan «دادن» : to give ; deh 3 «ده ۳ ( روزی ده )» : giver ; Bağdâd «بغداد» : God-given (city) ☞Bhag ; dâdâr «دادار» : God ; dâšan «داشن ( دهش ، دَشت ۲ )» : gift, tip ; pâdâš «پاداش ( پاداشت ، پاداشن )» : reward | NOTE: TAD:12 derives Baghdâd from Persian "bâğ-e-dâd: garden of justice".
7	#4 (parent #0) [Avestan] refs=BQT:121,907 | dathuš : creator ; spento-dâto : holy creation ☞Kwen
8	  #5 (parent #4) [Persian] refs=MON:1588 | day «دی ۲» : creator, the tenth month in Persian calendar ; Esfandîyâr «اسفندیار» : "holy creation", a male name | NOTE: See root "Ghei 1" for another possible derivation of "day"
9	#6 (parent #0) [Avestan] refs=BQT:2396; HRN:248 | dâta 2 : giver, owner ; ŭši-dâta : gifted with intelligence ☞Ôus 1
10	  #7 (parent #6) [Persian] refs=None | hŭšyâr «هوشیار» : aware, intelligent
11	#8 (parent #0) [Avestan] refs=POK:225 | dâthra : gift
12	  #9 (parent #8) [Pahlavi] refs=SNS:298 | dâsr : gift, kindness
13	#10 (parent #0) [Latin] refs=AHD | dare : to give ; donum : gift
14	  #11 (parent #10) [English] refs=None | add ; data ; edit ; rent ; tradition ; surrender ; date 2 : time ; donate ; pardon
15	#12 (parent #0) [Greek] refs=AHD | didonai : to give ; dôron : gift
16	  #13 (parent #12) [English] refs=None | dose ; Dorothy ; Theodore
17	--- entry 1 ---
18	ROOT [Turkish] Dolmak : to wind, wrap  (refs AHD:389)
19	#1 (parent #0) [Turkish] refs=AHD:389 | dolman : wrapping, cover, coating
20	  #2 (parent #1) [Persian] refs=MON:1554 | dolmeh «دلمه» : food wrapped in vine leaves
21	  #3 (parent #1) [German] refs=AHD:389 | dolman : a kind of cloak
22	    #4 (parent #3) [French] refs=None | 
23	      #5 (parent #4) [English] refs=AHD:389; KLN:473 | dolman : cloak or coat with large sleeves ; dolman sleeve
24	
```


## [2026-09-05T20:08:13.892Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-139.json",
 "description": "Read source JSON for page 139"
}
```


### [2026-09-05T20:08:13.935Z] TOOL RESULT

```
{
  "pdf_page": 139,
  "book_page": 109,
  "entries": [
    {
      "root": {
        "name": "Dô 2",
        "lang": "Indo-European",
        "refs": "POK:223",
        "gloss": "to give, create"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Sanskrit",
          "refs": "BQT:121; POK:223,225",
          "words": [
            {
              "translit": "dâ 4",
              "gloss": "to give",
              "script": null
            },
            {
              "translit": "dâtar",
              "gloss": "giver, God",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "NYB:56; HRN:61,115",
          "words": [
            {
              "translit": "dâtan",
              "gloss": "to give",
              "script": null
            },
            {
              "translit": "dâdâr",
              "gloss": "God",
              "script": null
            },
            {
              "translit": "dâhišn",
              "gloss": "gift",
              "script": null
            },
            {
              "translit": "paiti-dâhišn",
              "gloss": "reward, given back",
              "script": null,
              "see": [
                "Per 3"
              ]
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
          "refs": "BQT:289,815; FSF:169; SNS:295",
          "words": [
            {
              "translit": "dâdan",
              "gloss": "to give",
              "script": "دادن"
            },
            {
              "translit": "deh 3",
              "gloss": "giver",
              "script": "ده ۳ ( روزی ده )"
            },
            {
              "translit": "Bağdâd",
              "gloss": "God-given (city)",
              "script": "بغداد",
              "see": [
                "Bhag"
              ]
            },
            {
              "translit": "dâdâr",
              "gloss": "God",
              "script": "دادار"
            },
            {
              "translit": "dâšan",
              "gloss": "gift, tip",
              "script": "داشن ( دهش ، دَشت ۲ )"
            },
            {
              "translit": "pâdâš",
              "gloss": "reward",
              "script": "پاداش ( پاداشت ، پاداشن )"
            }
          ],
          "script_extra": null,
          "note": "TAD:12 derives Baghdâd from Persian \"bâğ-e-dâd: garden of justice\".",
          "quote": {
            "text": "سبک خنجر اندر دهانش نهاد - زدادار نیکی دهش کرد یاد",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:121,907",
          "words": [
            {
              "translit": "dathuš",
              "gloss": "creator",
              "script": null
            },
            {
              "translit": "spento-dâto",
              "gloss": "holy creation",
              "script": null,
              "see": [
                "Kwen"
              ]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "MON:1588",
          "words": [
            {
              "translit": "day",
              "gloss": "creator, the tenth month in Persian calendar",
              "script": "دی ۲"
            },
            {
              "translit": "Esfandîyâr",
              "gloss": "\"holy creation\", a male name",
              "script": "اسفندیار"
            }
          ],
          "script_extra": null,
          "note": "See root \"Ghei 1\" for another possible derivation of \"day\"",
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:2396; HRN:248",
          "words": [
            {
              "translit": "dâta 2",
              "gloss": "giver, owner",
              "script": null
            },
            {
              "translit": "ŭši-dâta",
              "gloss": "gifted with intelligence",
              "script": null,
              "see": [
                "Ôus 1"
              ]
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
          "refs": null,
          "words": [
            {
              "translit": "hŭšyâr",
              "gloss": "aware, intelligent",
              "script": "هوشیار"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:225",
          "words": [
            {
              "translit": "dâthra",
              "gloss": "gift",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "SNS:298",
          "words": [
            {
              "translit": "dâsr",
              "gloss": "gift, kindness",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "dare",
              "gloss": "to give",
              "script": null
            },
            {
              "translit": "donum",
              "gloss": "gift",
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
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "add",
              "gloss": null,
              "script": null
            },
            {
              "translit": "data",
              "gloss": null,
              "script": null
            },
            {
              "translit": "edit",
              "gloss": null,
              "script": null
            },
            {
              "translit": "rent",
              "gloss": null,
              "script": null
            },
            {
              "translit": "tradition",
              "gloss": null,
              "script": null
            },
            {
              "translit": "surrender",
              "gloss": null,
              "script": null
            },
            {
              "translit": "date 2",
              "gloss": "time",
              "script": null
            },
            {
              "translit": "donate",
              "gloss": null,
              "script": null
            },
            {
              "translit": "pardon",
              "gloss": null,
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {
              "translit": "didonai",
              "gloss": "to give",
              "script": null
            },
            {
              "translit": "dôron",
              "gloss": "gift",
              "script": null
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "dose",
              "gloss": null,
              "script": null
            },
            {
              "translit": "Dorothy",
              "gloss": null,
              "script": null
            },
            {
              "translit": "Theodore",
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
        "name": "Dolmak",
        "lang": "Turkish",
        "refs": "AHD:389",
        "gloss": "to wind, wrap"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Turkish",
          "refs": "AHD:389",
          "words": [
            {
              "translit": "dolman",
              "gloss": "wrapping, cover, coating",
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
          "refs": "MON:1554",
          "words": [
            {
              "translit": "dolmeh",
              "gloss": "food wrapped in vine leaves",
              "script": "دلمه"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "German",
          "refs": "AHD:389",
          "words": [
            {
              "translit": "dolman",
              "gloss": "a kind of cloak",
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
          "lang": "French",
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD:389; KLN:473",
          "words": [
            {
              "translit": "dolman",
              "gloss": "cloak or coat with large sleeves",
              "script": null
            },
            {
              "translit": "dolman sleeve",
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
  ]
}
```


## [2026-09-05T20:08:14.483Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:08:14.518Z] TOOL RESULT

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


## [2026-09-05T20:08:42.700Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','BQT','NYB','HRN','FSF','SNS','MON','AHD','KLN','TAD','BRT','PHD','HUB','ARY','LKT','TTS','SKT','WLD','IEC','SYN','CHEUNG']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:900])\n\""
}
```


## [2026-09-05T20:08:43.646Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && python3 -c \"\nimport json;d=json.load(open('data/verification/page-127.json'));print(json.dumps(d['entries'][0],ensure_ascii=False,indent=1)[:3000])\""
}
```


### [2026-09-05T20:08:44.782Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.c
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Dony
== SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt"], "page_offset": "242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image", "covers_etymology": true, "notes": "OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different paginati
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: lea
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based l
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD.txt"], "page_offset": "86 leaves (small book, ~80 printed pages); offset ≈ leaf − 4..6, verify against the printed numeral on the pa
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN number
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsian
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages. grep the oriental source word in transliteration or the number.", "notes": "", "cites": "entry number of Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (1927)"}
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively (3 citations); the 1878 original is public domain - try IA query 'vambery etymologisches wörterbuch turko-tatarischen' or Google Books.", "notes": "Open full text (public domain). OCR rough (Fraktur +
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-Europea
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept head
== CHEUNG null
```


### [2026-09-05T20:08:46.447Z] TOOL RESULT

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
---
{
 "entry": 0,
 "root": "Dhem",
 "verdict": "confirmed",
 "modern_form": "PIE *dʰemH- (LIV² *dʰmeh₁-) 'to blow, breathe; to smoke, raise dust'",
 "note": "Pokorny IEW 247-248 heads the entry 'dhem-, dhemə- \"stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)\"', so Nourai's language label (Indo-European) and his gloss 'to make vapor, raise dust' are an accurate short rendering of the German. Cheung (Etym. Dict. of the Iranian Verb, *damH³) writes the same root «PIE *dʰmeH- 'to blow' = LIV: 153 | Pok.: 247 f.»; Wiktionary reconstructs *dʰemH-. Watkins/AHD carries no dhem- root (its list goes dhembh- → dhen-¹), simply because no English word reaches it through Latin or Greek, so its silence is not a disagreement. Two weak spots in the chart: the Avestan node's gloss (node 1) and the name Damāvand (node 2), which Nourai's own source BQT:878 derives from a different root.",
 "note_fa": "ریشهٔ نمودار همان ریشهٔ هندواروپاییِ آغازینِ *dʰemH- «دمیدن، فوت کردن؛ دود و بخار برخاستن» است. پوکورنی در صفحهٔ ۲۴۷ کتاب خود آن را با معنای آلمانیِ «stieben, rauchen … wehen, blasen» آورده و برگردانِ کوتاهِ نورایی («بخار ساختن، گرد برانگیختن») با آن می‌خواند؛ چونگ نیز همین ریشه را *dʰmeH- «دمیدن» (LIV ۱۵۳) می‌نویسد. پس جعبهٔ ریشه، برچسبِ زبان و معنای آن درست است و ادعای نورایی در این حد پذیرفتنی است. تنها دو نقطهٔ سست در نمودار هست: معنایی که برای صورتِ اوستایی داده شده (گرهٔ ۱) و نامِ «دماوند» (گرهٔ ۲) که خودِ مأخذِ نورایی، یعنی حاشیهٔ معین بر برهان قاطع ص ۸۷۸، آن را از ریشهٔ دیگری می‌گیرد.",
 "sources": [
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85%DB%8C%D8%AF%D9%86",
  "https://en.wiktionary.org/wiki/%D8%AF%D9%85"
 ],
 "ref_check": [
  {
   "ref": "POK:247",
   "status": "supports",
   "note": "POK_01.txt (grep -n 'dbem-' → line 3513), IEW p.247: 'dbem-, dhemo- ,stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben == düster, dunkel), wehen, blasen (hauchen = riechen)'; the page continues 'Ai. dhámati ,bläst', av. daδmainya- …, npers. damīdan ,blasen, wehen', dam ,Atem, Atemzug''. Exactly the root box as drawn."
  }
 ],
 "consulted": [
  {
   "src": "WLD",
   "where": "Bd. I 851 f. (WLD_Bd1 djvu line 53642)",
   "stance": "supports",
   "note": "'dhem-, dhemə- „stieben, rauchen (Rauch, Dunst, Nebel; nebelgrau, rauchfarben = düster, dunkel), wehen, blasen (hauchen = riechen)“. Bedeutungsumfang wie bei Wz. *dheu- „stieben“.' — the source Pokorny 247 abridges."
  },
  {
   "src": "CHEUNG",
   "where": "s.v. *damH³ (CHEUNG.txt line 4670 ff.)",
   "stance": "supports",
   "note": "'*damH³ \"to blow, breathe; to swell\" … «PIE *dʰmeH- \"to blow\" > LIV: 153 | Pok.: 247 f.»'"
  },
  {
   "src": "AHD",
   "where": "Watkins 1985, d-list (AHD_watkins1985.txt line 377)",
   "stance": "silent",
   "note": "the appendix runs 'dhembh-. To bury. … [Pok. (dhembh-), dhmbh- 248.] dhen-¹. To run, flow.' — no dhem- entry at all, since no English word descends from it via Latin/Greek."
  },
  {
   "src": "IEC",
```


## [2026-09-05T20:08:56.210Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==232||NR==233||NR==234' POK_01.txt | head -160",
 "description": "Print Pokorny p.223-225"
}
```


## [2026-09-05T20:08:57.812Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dō-\\|dō-, də-\\|^dō\\b\" POK_01.txt | head -20; echo \"=== AHD\"; grep -n \"^dō-\\|^do-\\.\\|To give\" AHD_watkins1985.txt | head -20",
 "description": "Locate do- root in Pokorny and AHD"
}
```


### [2026-09-05T20:08:58.054Z] TOOL RESULT

```
nlich  bedeutet  anord.  tjöa  (Heuhön) ,helfen^  (s.  Falk-Torp  1315  f.).  Etwas  andere  geistige  Wendung  zeigt  lat. dücere  als  ,berechnen,  schätzen^,  wobei  z.  B.  aliquem  poena  dignum  dücere ursprüngl.  meinte  ,einen  als  strafwürdig  aus  der  Menge  hervorziehen  und dadurch  als  solchen  darstellend
Alb.  nduk  ,rupfe,  reiße  die  Haare  aus*,  dial.  auch  ,sauge  aus^
Mcymr.  dygaf  ,bringe^  {*dukami)]  über  air.  to-ucc-  {cc  =  gg)  ,bringeir s.  unter  euh.
Lat.  dücö  (altlat.  doucö),  -ere,  düxlj  düctum  ^ziehen,  schleppen;  führen (mit  sich  ziehen)'  =  got.  tiuhanj  ahd.  ziohan,  as.  tiolicin,  ags.  teon  ^ziehen^ (anord.  nur  im  Partiz.  toginii).
Verbale  Komposita:  ab-dücö  =  got.  af-tmhaUj  ad-dücö  =  got.  at-tiuhauy con-dücö  =  got.  ga-Huharij  usw.
Wurzelnomen:  lat.  dux,  ducis  m.  f.  , Führer'  (davon  educäre  , aufziehen, erziehen';  sprachgeschichtlicher  Zusammenhang  mit  dem  formal  gleichen anord.  toga,  ahd.  zogön  ,ziehen'  besteht  nicht),  trädux  ,(herübergeführte) Weinranke'.  Ist  as.  usw.  heritogo,  ahd.  herizogo  , Heerführer',  nhd.  Herzog Nachbildung  von  GTQavrjyög?  Vgl.  Feist  479.
^i-St. :  lat.  ductim  ^ziehend,  in  vollen  Zügen',  spät  ducti-ö  ,Führung* (daneben   tu-^i.  ductus,  -üs  ,Führung,  Leitung')  =  nhd.  Zucht  (s.  unten).
Bes.    reiche    Formenentwicklung    im    Germ.,    so:   Iterativ-Kaus.   anord. teygia  ,ziehen,  hinausziehen'  =  ags.  tiegan  ,ziehen'  {^taugian)]  ahd.  zuckan, ., zucchen,   mhd.  zucken,   zücken  ,schnell  ziehen,  entreißen,  zucken'  (mit  in- tensiver Konsonantendehnung;    davon  mhd.  zuc,  Gen.  zuckes  m.  ,Zucken,
221
«    .1-0"   anord.  tofj  n.  ,clas   Ziehen^   SeiF^   mlid.  ?:oc,    Gen.  zoges  m.  ^Zug'^, von  anord.  ^o^ß;  -«<^^«  ^ziehen^^  ags.  torjian,  engl,  ^ow  ^ziehen^^  alid.  zo^ön,
Id    zo^e»    ;Zielien   (tr.^  intr.);    reißen^   zerren-,   vgl.   oben   lat.  {e)-ducare-^ er-    ti/ge  m.  ?-St.  ;,Ziehen^;  alid.  zug,  nlid.  Zug  (*tugi-)]   ahd.  sw^iZ,  zuhü,
hd.  2«^^^;  ^^^-  ^^'^9^h  anord.  tygill  m.  ^Band,  Riemen^,  ags.  ^i/^eZ  ^Strang';- nord.  ^«^'^  ^'  ^Strick^,  ags.  teag  L  ,Band,  Fessel,  Gehege^  (davon  ags. neocin  ^binden^;,  engl,  tie)]  mit  Tief  stufe  anord.  tog  n.  /fau';  anord.  taumr jn  Seil,  Zügel%  ags.  Uam  m.  ^Gespann  Zugochsen,  Gebären,  Nach- kommenschaft^ (davon  tieman  ,sich  vermehren,  schwanger  sein^,  engl. teeni),  ndl.  toom  ,Brut^,  afries.  täm  ,Nachkommenschaft^,  as.  törn  ,lorum^, ahd.  mhd.  zoum  m.  ,Seil,  Riemen,  ZügeF^  nhd.  ,Zaum^  (germ.  *tauma- aus  *tauz-md-);  ahd.  giziugön  ,bezeugen,  erweisen^  (eigentlich  ,zur  Gerichts- verhandlung gezogen  werden^,  [mhd.  geziugen  , durch  Zeugnis  beweisen^, nhd.  (bejzeugen^ 
 Zeuge,  mnd.  betügen  , bezeugen,  beweisen^,  getUcJi  n.  ,Zeugnis^; forner  mit  der  Bed.  .producere,  großziehen,  erzeugen^  ahd.  giziug  (*teugiz) Zeug,  Gerät,  Ausrüstung^,  nhd.  Zeug,  mnd.  tüch  (-//-)  n.  ;,Zeug,  Gerät^ und  ,Zeugungsglied^,  mhd.  ziugen,  nhd.  zeugen]  got.  ustauhts  ,Vollendung^, ahd.  mhd.  zuht  f.  _,Ziehen,  Zug,  Erziehung,  Zucht,  Nachkommenschaft^, nhd.  Zucht  (=  lat.  ductus  s.  oben);  davon  nhd.  zilclitig,  züchtigen,  ags. tyht  m.  ^Erziehung,  Zuchf^,  afries.  tucht,  tocht  ,Zeugungsfähigkeit^
Bes.  wegen  Zucht  ,Nachkommenschaft^,  bair.  auch  ,Zuchtschwein'^  u.  dgl.
zieht  man   ahd.  zöha,   mnd.   töle  [^töhila),  nhd.  schwäb.    zauche    , Hündin^,
neuisl.    töa    , Füchsin^    zu    unserer  Wz.;    doch    vgl.   mhd.   zü])e    , Hündin^,
'norw.  dial.  tohhe  ,Stute,  kleines  weibliches  Wesen^   und   germ.  "^tikö  und
*titö  ,Hündin^
Eine  einfachere  Wzf.  '^deu-  ,ziehen^  vielleicht  in  anord.  tjödr  n.  (*deu- trom)  ,Spannseil,  BindeseiF  =  mengi.  teder,  tej)er  ds.,  ahd.  zeotar  ,Deich- seP,  nhd.  bair.  Zieter  ,Vorderdeichsel^  (auch  ags.  tüdor,  tuddor  n.  ,Nach- kommenschaft^?);  aber  ai.  dörakam  ,Strick,  Riemen'  ist  dravid.  Lw.  (Kuiper Proto-Munda  131).
WP.I  780  f.,  WH.  I  377  f.,  861.
deup-  (:  kteup-?)  ,dumpfer  Schall,  etwa  wie  von  einem  Schlag*";  Schall- wurzel. Gr.  hom.  dovTtog  ,dumpfes  Geräusch,  Getöse;  Schall  der  Fußtritte'; dovTieu)  jgebe  einen  dumpfen  oder  rasselnden  Ton  von  mir';  der  in  hom.  sydov- TtrjGap,  iglydovTtog  ,laut  donnernd'  ((.KxalyöovTtov  .  . .  ixsyaXörjXOv  Hes.)  zu- tage tretende  ursprüngliche  Anlaut  yö-  ist  vielleicht  mit  xrr/rog  ,Schlag' neben  Tvrrog  parallel  oder  ihm  nachgebildet,  so  daß  über  sein  Alter  keine Sicherheit  zu  erlangen  ist;  nach  Schwyzer  wäre  {y)dov7ieo)  Intensiv  zu schwachstufigem  xtdtt-;  serb.  düplm,  düpiti  ,mit  Getöse  schlagen',  sloven.
222
düpam  (dupljem)  dupati  ,auf  etwas  Hohles  schlagen^  dumpf  rauscher dupotdtij  bulg.  düp'^  ,gebe  einem  Roß  die  Sporen'^  lett.  dupeties  ,dum| schallen'  (bsl.  d-  aus  gd-?  oder  älter  als  gr.  yd-?)]
nach  Van  Windekens  Lexique  138  hierher  toch.  A  täp-  _,ertönen  lassei verkünden*^  (*tup-)  im  Infin.  tpässi,  Partiz.  Pass.  cacpu.
WP.  I  781  f.,  Endzelin  KZ.  44,  58,  Mühlenbach-Endzelin  I  518,  Schwyzer Gr.  Gr.  I  7181
d9gb-mö::s  ,schief'?
Ai.  jihmd-li  ^schräg,  schief'  (urar.  Hizhmd-  assimil.  aus  *dizhmd-)j  gj.^ d6x!^iog,  öox^ög  ^schief  (assimil.  aus  *dax!.i6g)'
Pedersen  KZ.  36,  78,  WP.  I  769.  Andere  Möglichkeiten  s.  unter  geU ,drehen,  biegen'.
digh'  , Ziege'.
Gr.-thrak.  öi^a'  ai^.  ^dyaüveg  {*diglnd),  vgl.  den  thrak.  PN  ^il^a-XEl^iq (wie  ^EßQOv-TBXp,Lg  zu  eßgog'  rodyog  Hes.);  ahd.  ziga  ,Ziege',  mit  hypo- korist.  Konsonantenschärfung  ags.  ticce^ij  ahd.  zicktj  zickln  , Zicklein' (aber  über  nhd.  Zecke  s.  oben  unter  deigh-)]  hierher  vielleicht  norw.  dial. tikka  
,Schaf'  (event.  Kreuzung  von  schwed.  dial.  takka  ,Schaf'  mit  einer nord.  Entsprechung  von  Zicklein)^  tiksa  ,Schaf,  Hündin',  tikla  ^junges Schaf  oder  Kuh',  sowie  anord.  tlk  f.  ,Hündin'  =  mnd.  tlke  ds.
Arm.  tik  ,Schlauch  aus  Tierfell'  wird  von  Liden  (Arm.  Stud.  10  f,^ Don.  nat.  Sjdow  53^)  als  ursprgl.  , Ziegenfell'  hierhergestellt,  müßte  jedoch auf  *dig-  zurückgehen  (tabuistische  Entstellung?).
WP.  I  814,  WH.  I  632,  868.  Nach  Risch  (briefl.)  vielleicht  ursprüngl; Lockruf.
dlp-ro-y  dip-erä  ,Opfertier,  Vieh'.
Arm.  tvar  ,Schafbock,  Herde  von  Großvieh'  (*t{var  <  *dxpera)]  got.  tibrW. ,Opf ergäbe'   (verbessert   aus   aihr),  ahd.  zebar  ,Opfertier',   ags.  tiferj  über ds.,  spätmhd.  ungeztherej  unzTver,  nhd.  Ungeziefer  eig.  ,unreines,  nicht  zum Opfern  taugliches  Tier'.  Afrz.  (ajtoivre  , Zugtier'  stammt  aus  dem  Germ.
iW^r
WP.  I  765,  WH.  I  323,  Feist  19  b,  477  a.  ?.>gf
dlkii-i?)  ,süß'.
Gr.  ylv/,vg,  yXvyiSQog  ,süß',  ylvTCKÖv  yXv%v^  y%vy.y.a'  ij  ylvT^mr^g  Hes.  (-xx- aus  -ku-),  ylevY.og  (spät)  ,Most'  (Ablautneubildung);  yX  aus  dl  wegen  des folg.  x;  -Iv-  aus  -Xa-  nach  dem  folg.  v;  über  späte  devY,og  ,Most',  öev/.rig ,süß'  s.  WH.  I  380;
lat.  dulcis  ,süß,  lieblich,  sanft'  (aus  *dlkui-s).
WP.  I  816,  WH.  I  380.  '   ^  1^1
223
S-bü,  dn^huä  ^Zunge^;  oft  durch  Anlautswechsel  und  Umstellungen umgestaltet.
Vi.  jihvä  f.,  av.  hizvä  ds.  (vorar.  *yighuä.  aus  *-daghuä  mit  i  von  ZiÄ-  ;,lecken^ Qjer  von  _;*ä-  ;ab\värts  wenden^;  iran,  *sizva  wohl  durch  Sonorendissi- uiilation);  daneben  tl-Stamra  in  ai.  juhü  f.  ^Zunge,  Löffel^  (mit  u  nach juhöti  ;,ins  Feuer  gießen^^  anders  Wackernagel-Debrunner  III  192),  av. Jiizü  m.  ds.;  mit  -ön-  für  -ä  apers.  hizhäna-,  mpers.  hvzvän  ds._,  nordar. hiBn  m.  ,Zunge;  Rede^   (*vUhvän  nach  E.  Leumann  Nordar.  Spr.  127  f.);
arm.  le^u,  Gen.  lezvi  setzt  im-Ausgang  das  -ghuä  von  *dnghuä  fort, die  erste  Silbe  wohl  von  leigh-  ,lecken'  beeinflußt;
alat.  dingua,  lat,  lingua  (mit  ^  von  lingere)-  osk.  fangv am  (Vetter  Serta Iloffillenana  153;
air.  teng  («-Stamm)  und  tengae,  Gen.  tengad  mit  t-  nach  tongid  ,schwört^; aber  air.  ligur  ,Zunge^  zu  lat.  Ugurriö;  unklar  ist  mcymr.  tafaiot,  cymr. tafodj  acorn.  tauot^  mbret.  teaut,  bret.  teod,  wozu  com.  tava,  mbret. taffhaff,  bret.  tanva  ,kosten^  (kelt.  '^tamäto-'^)
```


### [2026-09-05T20:08:58.126Z] TOOL RESULT

```
=== AHD
268:ai-1, To give, allot. 1. Suffixed form “ai-t-yd in Greek aitia, cause, responsibility: ETIOLOGY. 2. Suffixed form *ai-td- in Greek diaitan, to decide, lead one’s life: DIET!. [Pok. 3. ai- 10.]
489:*klai-ni-, bright, pure, in: a. Old English cléne, pure, clean: CLEAN; b. Old English clénsian, to purify, cleanse: CLEANSE. 2. Extended and suffixed zero-grade form *glo-nd in Greek gléné, eyeball: EUGLENA. [Pok. gel- 366.] gel-3. Cold; to freeze. 1. Germanic *kaliz, coldness, in Old English c(iJele, chill: CHILL. 2. Germanic *kaldaz, cold, in Old English ceald, cold: COLD. 3. Germanic *kédl-, cool, in: a. Old English cdl, cold, cool: cooL; b. Germanic *koéljan, to cool, in Old English célan, to cool: KEEL’. 4. Suffixed form *gel-d- in Latin geldre, to freeze: GELA- TIN, GELATION, JELLY; CONGEAL. 5. Suffixed form *gel-u- in Latin gelu, frost, cold: GELID. 6. Probably suffixed zero-grade form *gl-k- in Latin glaciés, ice: GLACE, GLACIAL, GLACIATE, GLACIER, GLACIS. [Pok. 3. gel()- 365.] gembh-. Tooth, nail. I. Suffixed o-grade form *gombh-o-. 1. Germanic *kambaz, comb, in: a. Old English camb, comb: COMB, KAME; b. Old High German kamb, comb: CAM; c. Germanic denominative *kambjan, to comb, in Old English cemban, to comb: OAKUM, UNKEMPT. 2. Greek gomphos, tooth, peg, bolt: GoMPHosIS. II. Per- haps Germanic *kimb- in Old English cim-, cimb-, rim (only in compounds): CHIME?. III. Possibly suffixed form *gembh-ma in Latin gemma, bud, hence gem: GEM, GEMMA, GEMMATE, GEMMULE. [Pok. gembh- 369.] geme-. To marry. Suffixed zero-grade form “gmoa-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem/(e)- 369.] gen-. To compress into a ball. Hypothetical Indo-Euro- pean base of a range of Germanic words referring to compact, knobby bodies and projections, sharp blows. 1. Germanic *kn-a-pp- in: a. Old English cnzpp, hilltop: KNAP?; b. Middle Dutch cnoppen, to snap, and Low German knappen, to snap, hence “to have a bite,” akin to Middle English knappen, to strike sharply, snap: KNAP!; KNAPSACK; C. Old English cnop, knob: KNop. 2. Ger- manic *kn-a-k- in Middle High German knacken, to crack; KNACKWURST. 3. Germanic *kn-a-r- in: a. Norwe- gian knart, knot in wood, akin to the source of Middle English knarre, knob: KNAR; b. Middle English knor, a swelling: KNUR. 4. Germanic *kn-u-b- in Middle Low German knobbe, knubbe, knot in wood, knob: KNOB, NuB. 5. Germanic *kn-u-k- in: a. Old English cnocian, to knock: KNOCK; b. Italian gnocco, nocchio, knot in wood: GNOCCHI; c. Middle Low German kndkel, knuckle, akin to Middle English knakel, knuckle: KNUCKLE. 6. Ger- manic *kn-u-l- in: a. Old English cnyllan, to strike: KNELL, KNOLL; b. Old English cnoll, a knoll: KNOLL!. 7. Germanic *kn-u-p- in Middle Dutch cnoppe, knob, bud: KNOBKERRIE. 8. Germanic *kn-u-t- in: a. Old Eng- lish cnytten, to tie in a knot, knit: KNIT; b. Old English cnotta, knot in cord: KNOT!; c. Old Norse kniitr, knot in cord: KNOUT. 9. Germanic *kn-u-th- in Old High German knodo, knob, knot (> French quenelle): QUENELLE 10. Germanic *kn-i-b- in Old English cnif, knife: KNIFE. 11. Germanic *kn-e-th- in Old English cnedan, to knead: KNEAD. [Pok. gen- 370.] gene-. Also gen-. To give birth, beget; with derivatives referring to aspects and results of procreation and to familial and tribal groups. 1. Suffixed zero-grade form *gn-yo- in Germanic *kunjam, family, in: a. Old English cyn(n), race, family, kin: KIN; KINDRED; b. *kuningaz, king (< “son of the royal kin”), in Old English cyning, king: KING. 2. Suffixed zero-grade form *gn-ti- in: a. Ger- manic *kundjaz, family, race, in Old English cynd, gecynd(e), origin, birth, race, family, kind: KIND!; b. Ger- manic*kundiz, natural, native, in Old English gecynde (ge-, collective prefix; see kom), natural, native, fitting: KIND?; c. Germanic variant *kinth- in Old High German kind, child: KINDERGARTEN, KRIss KRINGLE; d. Latin géns (stem gent-), race, clan (> French gens, men): GENS, GENTEEL, GENTILE, GENTLE; GENDARME. 3. Suffixed full-grade form *gen-es- in: a. Latin genus (stem gener-), race, kind: GENDER, GENERAL, GENERATE, (GENERA-
502:ghabh-. Also ghebh-. To give or receive. 1. Form *ghebh- in Germanic *geban in: a. Old English giefan, to give: GIVE; b. compound *far-geban (*far-, away; see per'), to give away, in Old English forgi(e)fan, to give, give up, leave off (anger), remit, forgive: FORGIVE. 2. Suf- fixed form *ghebh-ti-, something given (or received), in Germanic “giftiz in Old Norse gipt, gift, a gift: GIFT. 3. O-grade form “*ghobh- in Germanic *gab-ulam, some- thing paid (or received), in Old English gafol, tribute, tax, debt: GAVEL2. 4. Form *ghabh-é- in: a. Latin habére, to hold, possess, have, handle (> habitdre, to dwell): ABLE, BINNACLE, HABILE, HABIT, HABITABLE, (HABI- TANT), (HABITAT); (COHABIT), EXHIBIT, INHABIT, IN- HIBIT, PREBEND, PROHIBIT, (PROVENDER); b. Latin débére (dé-, away from; see de-; third person plural present passive debentur), to owe: DEBENTURE, (DEBIT), DEBT, DEVOIR, DUE, (DUTY); (ENDEAVOR). Compare kap-. [Pok. ghebh- 407.]
931:seue-', To give birth. Suffixed zero-grade form in deriva- tive noun *su(2)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON. See also su-. [Pok. 2. seu- 913.]
```


## [2026-09-05T20:09:06.309Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"geben'\\|,geben\\|dö-\\|do-  :\" POK_01.txt | sed -n '1,40p'",
 "description": "Find Pokorny do- 'geben'"
}
```


### [2026-09-05T20:09:06.363Z] TOOL RESULT

```
146:Toch.  B  ai-,  A  e-,  Infinitiv  B  aitsi,  A  essi  , geben';  hett.  pa-a-i  ,er  gibt', 3.  PI.  p{(-{ayan-zi  mit  Präverb  pe  ,hin'.
714:Zur  Erklärung  der  6-Form  geht  Johansson  IF.  4^  137  f.  von  dem durch  ^Atzlööjv,  ^Amdavög  sowie  durch  ai.  dbda-h  m.  ^Wolke^  und  den  mit äpah  paradigmatisch  zusammengeschweißten  Instr.  Dat.  PI.  ai.  adhliih, adbhyah  vorausgesetzten  St.  *ap(9)d-  (vielleicht  ^Wasser  gebend'^  mit  zu dö-  ^geben''  gehörigem  2.  Gliede)  aus:  *ahd5(n),  Gen.  *abdnes,  woraus *abnes',  aus  den  obl.  Kasus  entsprang  lat.  amnisj  während  im  keltischen *abdö(n) :  *abnes  zu  *abä  (mir.  ab),  ^abonä  (daher  mir.  abann)  ausgeglichen wurde.
1023:audh'  ^Glück^  Besitz^  Reichtum^*  illyr.  PN  Audarus^  Audata  (:  germ. Audo-herJit),  paion.  PN  Audö-leön  (Kralie  IF.  58^  132),  cymr.  iidd  {^audos) ;Herr^  (anders  Lewis-Pedersen  14)/  bret.  ozach  ^Hausherr^  {*udakkos\ Loth  RC.  41,  234;  as.  ödan^  ags.  eaden,  anord.  audinn  ,vom  Schicksal vergönnt,  g-ewährt^,  anord.  audna  , Schicksal,  Glück^,  aiidr  ,Reichtum^, ags.  ead  ,Besitz,  Reichtum,  Glück^,  as.  öd  ,Besitz,  Wohlstand^,  ahd.  al-öd ,voller  und  freier  Besitz^  (mlat.  all^dium),  mhd.  klein-öt  ,Kleinod'^,  got. audahafts  ,beglückt^,  audags  ,beatus^,  ahd.  ötac  ^glücklich,  reicht
1049:Toch.  B  au-läre,  A  oZar  ^Genosse^;  als  zweifelhaft  B  omaute  ^Sehnsucht^^ w-är(ln)-  ,ersehnen'^  A  lo-aste  .Schutz^  mit  angebl.  Schwundstufe  der  Wz; Eher  hierher  wa-  ,geben^,  A  1.  Sg.  icsä  (Pedersen  Tochar.  186).
1127:h.  aue-d-:  ahd.  wäzan,  wiaz,  mhd.  loäzen  ^wehen^  blasen^^  wäz  ^Wind- stoß^;  lit.  vedinti  ^lüften^  kühlen^;  allenfalls  gr.  äaC,o)  ^hauche^  aus  ^^äfdö-m (eher  aber  gr.  Neuschöpfung  nach  anderen  Verben  auf  -a^w);  vermutlich auch  (aus  *aiid-d-ro-)  lit.  dudi^a  m.  ^Sturm^^  n.  ^Gewitter^;  apr.  wydra yWind^  über  ai.  üdhar  n.  ^Kälte^^  av.  aodard,  aota  ds.  vgl.  Persson  Beitr.  11.
1403:as.  banut  ,föraes' ;  ags.  bönian  , polieren'  (d.  i.  , glänzend  machen'),  ndd, (und  daraus  nhd.)  bönen  , scheuern,  höhnen',  mhd.  biienen  , höhnen'  (ob got.  bandioa,  -wo  , Zeichen',  bandwjan,  aisl.  benda  ,ein  Zeichen  geben' hierher  gehören  —  etwa  als  w-Ableitung  von  einem  Partiz.  bhä-nt-  ,schei- nend'  --,  ist  fraglich.     Lit.  bei  Feist  79  f.);
1422:nis  dieser  Tage,  Kalender';  als  Ableitung  von  einem  Partiz.  Hhd-to-s,  Uj fateovj  -erl,  fassus  , öffentlich  erklären,  zugeben'  =  osk.  fatium  ,färi',  la| Fätuus,  Beiname  des  ,Faunus  väticinäns';
2138:got.  anabiudan  , befehlen,  anordnen',  faurbiudan  , verbieten',  aisl.  bjöda , bieten,  anbieten,  zu  erkennen  geben',  ags.  beodauj  as.  biodan^  ahd.  biotan , bieten,  darbieten',  nhd.  bieten,  gebieterij  verbieten,  Gebiet,  eigentl.  , Befehls- bereich'; aisl.  bod  n.,  ags.  gebod  n.,  mhd.  bot  n.  , Gebot',  ahd.  usw.  boto ,Bote',  ahd.  butil  (nhd.  Büttel),  ags.  bydel  ,Bote, .  Gerichtsdiener';  got. biups,  -dis  jTisch',  aisl.  bjödr,  ags.  beod,  ahd.  beot,  piot  ,Tisch;  Schüssel', eig.  , worauf  angeboten  wird,  Servierbrett'  (dazu  auch  ahd.  biutta,  nhd. Beute  , Backtrog,  Bienenkorb').
2141:Themat.  Präs.  in  abg.  bljudq,  bljusti  , wahren,  hüten,  achtgeben',  russ. bljudü,  bljusti  ,beobachten,  wahrnehmen'  (über  slav.  -ßi  aus  idg.  eu  s. Meillet  Slave  commun^  58).
2622:idg.  *dö  ursprgl.  , herzu*  in  lat.  dö-ni-cum  (altertümlich),  dönec  (^dö-ne-que), seit  Lukrez  auch  dönique  ,so  lange  als,  bis  daß,  bis  endlich',  aber  auch ,dann*  {dö-  gleichbed.  mit  ad-,  ar-  in  umbr.  ar-ni-po  ,quoad*  aus  *ad-ne- qvom)  und  in  quandö  ,wann*  =  umbr.  panupel  ,quandoque';  air.  do,  du, acymr.    di    (=  di)^    corn.    de    ,zu*    aus    *dü   (in   gall.    du-ci   .und'),    Thur-
2649:•  Flechse,  Ader'  (idg.  *dö-lo-).
3198:cfö-  :  d9',  auch  dö-u-  :  dQU-  :  cfu-  ,geben^  (perfektiv),  Aoristwurzel  mit  sekun- därem    Präsens     di-dö-mi,     Nominaibildungen:    do-no-m,    dö-ro-tn^ dö'ti-s,    d9-ti-s    ,Gabe',    dö-ter-    ,Geber^,    Partiz.    dö-to-s,    dQ-to-s, 'd-tos,  Infinitiv  dö-men-ai,  dö-uen-ai. Ai.    dd-dä'ti  (Aor.  d-dä-m,   Opt.   deyäm,   Fut.  däsydti,   Aow  Med.  ddita ==  gr.    eöozo,   Inf.  ddmane  :  gr.  ööjxsvai,   vgl.   lat.  daminl,  falls   ursprüngh Infinitiv)  ^gibt*"  (päli  cZmna  zu  einem  Präs.  "^di-dä-ti),  av.  dadäiti  ds.,  apers. Imp.    dadätuv    ,er    soll   geben';  Wurzelnomen    ai.    dä[s]  dstu  ,dator    estu'; Infin.    dätum    (:lat.    Supin.    cZa^wm);    Partiz.    ditd-h    (unbelegt),    sekundär dattd-h,  schwundstuf,  in  ä-t-td-h,  prd-t-ta-h  ^hingegeben',  ablaut.  in  tvä-däta-h ,von  dir  gegeben',  av.  däta-j  zum  Fut.  ai.  däsyämi  (:  lit.  düosiu)  s.  Schwyzer Gr.  Gr.  I  78811;
3202:ven.  zoto  ,dedit^  =  gr.  eöoTO]  zonasto  ^döiiävit^  vielleicht  aus  *dönä-s-to von  einem  denom.  *dönäiö  (*c?ö?20-m  :  lat.  dömim)]  mess.  pi-do  (*dö-t:^[^ ■a-dät):
3206:redupl.  Präsens  ital.  *di-dö(?)  in  lat.  reddö  {reddidtj  redditum,  reddere) jgebe  zurück'  aus  *re-d(iydö(?)  ist  angeblich  themat.  Umgestaltung  von *di-dö-mi',  andere  Komposita  sind  de-dö,  dl-dö,  e-dö,  prö-dö,  trä-dö  und ven-dö]
3207:Partiz.  lat.  dätus  ^gegeben'  =  falisk.  datu  ,datum^^  vest.  data  ^data', päl.  datas  ^datas^  (- S^^-  doTÖg)j  Supin.  datum  (:ai.  Infin.  dätum)\
3212:lit.  duomi  (heute  sekundär  duodu,  lett.  duodu,  neugebildet  zum  alit. Ipv.  duodi  aus  "^dö-dhi-,  ostlit.  düomu),  2.  Sg.  düosi,  3.  Sg.  düost{i)  ,^\hi', apr.  däst  ds._,  beruhen  nach  Kofinek  Listy  filol.  65^  445  und  Szemerenyi Et.  Slav.  Roum.  1,  7  ff.  (vgl.  E.  Fraenkel  Balt.  Sprachw.  11  f.)  nicht  auf alter  Reduplikation  (angebl.  *dö-dd-mi,  bsl.  "^dödmi,  3.  Sg.  *dö-dd-ü,  bsl. *dödti  >  *dösti),  sondern  auf  unreduplizierter  athemat.  Flexion  (*dömi, PL  *ddmös);  lit.  düosti,  abg.  dast^  sind  Nachahmungen  von  lit.  hti  ,ißt' usw.,  die  neben  lit.  *e(d)mij  abg.  janib  (aus  ^ed-m-)  liegen^,  wo  das  d  der Wurzel  als  suffixal  empfunden  wurde;  zum  Fut.  lit.  duosiii  s.  oben  S.  223.
3214:Infin.  lit.  düoti,  lett.  duot,  apr.  dät  {^dö-tl-)  =  aksl.  dati^  serb.  däti, russ.  dath.  ?
3217:partiz.  *dö-na-  in  Siksl.  pre-dam,  serb.  dän,  cech.  ddn,  klr.  ddnyj  , gegeben' , *dö-tcL-  ds.  in  apr.  däts,  lit.  düotas,  lett,  cZwo^s;  einzelsprachl.  Neuerungen <;iiul  serb.  dial.  dät,  cech.  c^a^^;  dazu  lit.  duotina  ;,mannbar^^  russ.-ksl. jwdatbm,  russ.  poddtnyj  .freigebig^;  Supin.  *dötun  ,zu  geben^  in  apr.  daton (lüfin.);  lit.  c?MO%  aksl.  ohdah,  sloven.  dat,  vgl.  slav.  *datz-H  in  sloven. Jodätek,  poln.  dodatek,  russ.  doddtok  , Zugabe^;
3220:*dö-tel-  in  aksl.  dateljh  (*dö-tel-iu-)  ^Geber*^^  cech.  udatel  ^Angeber^,  russ. ddteh  ^Geber'.
3221:Ai.  *däti'  ^Schenkung,  Gabe^  in  däti-vära-  jgern  verteilend,  freigebig^, havya-däti-  ,die  Opfergabe  besorgend,  das  Darbringen  des  Opfers^,  av. däiti-  , Geben,  Schenken,  Gewährung^,  gr.  ö&xig  Hes.  (und  kons.  St.  *dö-t- in  öd)g)  ,Gabe^,  Jcoai-d-sog,  -q)Q0)v^  lat.  cZös,  -tis  ,Mitgift^,  lit.  Inf.  düoti: slav.  *dath  ,Gabe^  (z.  B.  in  aksl.  hlagodath  ,X(xQig',  russ.  pödath  ,Steuer^), Inf.  dati]  schwachstufig  ai.  diti-h,  gr.  ddaiq  ,Gabe^,  lat.  dati-ö,  -tiönis  (alt *-tlnes)  ,das  Schenken^  (Suffix  wie  in  gr.  öcorivT]  ,Gabe^);  mit  Vokalschwund in  Enklise  ai.  bhdga-tti-  ,Glücksgabe^
3224:ai.  däyd-  ,gebend^,  däyd-  m.  ,Geschenk^,  apreuß.  däian  Akk.  ,Gabe^, serb.  pro-daja  ,Verkauf^  (usw.,  Berneker  176).
3226:do-U'  liegt  vor  in  ai.  dävdne  ,zu  geben^  (auch  Perf.  daddu  ,habe  ge- geben'), av.  dävöi  ,7.\i  geben',  kypr.  övfavoi  ,er  möge  geben^,  Inf.  dofsvai (über  ark.  Partiz.  diTtv-döaq  s.  Schwyzer  Gr.  Gr.  I  745  f.),  kontrahiert hom.-att.  dovvai]
3371:dcazu  wohl  lit.  deviit,  devett  , Kleider  anhaben';  ein  formantisches  u  auch in  gr.  *x^o/axog  und  (assim.)  '■^•d-aJ'ay.og,  vgl.  ^occ^w  ,sitze',  ion.  ^wxog  (hom. ^öcoyiog  für  ^6[J^]ccy,og  geschrieben)  ,Sitz',  d-aßamv  ^ä^ov  )]  S-qovov  Hes., att.  auch  ^äxog  ds.,  hom.  ^adaaco  , sitze',  att.  poet.  d'daao)  ds.  (s.zur  gr.  Gruppe Hechtel  Lexil.  161  f.,  Boisacq  335);  vgl.  auch  thrak.  -dava  , Siedlung'  aus *diieuä  oder  *dh9uä]  wohl  Umbildung  nach  dem  Nebeneinander  *dü-: *dou-  , geben';
3553:geben'),  ufries.  dintje  gleicht  schüttern^  norw.  deise  ^taumelnd  fallen,  gl^Jf (aus:)  ndd.  dei(n)sen  (*dantisöri)  ^zurücktaumeln,  auskneif en^;  ostfries. ,Fall^  (s  aus  -dt-  oder  -c?s-),  anord.  dyntr,  ags.  dynt  m.  (=  anord.  dyi engl,  dint  ,Schlag,  Stoß^;
3767:arm.  de-dev-im  , schwanke,  schaukle'  (vgl.  das  ebenfalls  redupl.  Intensiv dhvajd-h  ai.  dö-dhavUi);
4764:lat.  ego-ne,  tü-ne,  denique  (*de-ne-que),  dönicum^  dönec  (*dö-ne-kuomf vgl.  umbr.  arnipo  ,quoad'  aus  *ad-ne-hkorn)^  quandö-ne,  sin  (*si-ne  ,wenn aber  doch'),  usw.;  auch  -ne  in  der  Frage;
4824:illyr.  PN  Epi-cadus  (vgl.  gr.  '/.e/.cxöfisvog  »prangend') ;  ven.  ON  Opi-tergiu-n^  ' (zu  Tergeste  ,Triest*,  abg.  tr^g^  , Marktplatz');   messap.  pi-dö  (*dö-t)  ,o-a.b«.;'*-
```


## [2026-09-05T20:09:07.544Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==233||NR==234||NR==235' POK_01.txt | grep -n \"\" | sed -n '1,80p'",
 "description": "Print Pokorny leaves 233-235"
}
```


### [2026-09-05T20:09:09.135Z] TOOL RESULT

```
1: Zeuge,  mnd.  betügen  , bezeugen,  beweisen^,  getUcJi  n.  ,Zeugnis^; forner  mit  der  Bed.  .producere,  großziehen,  erzeugen^  ahd.  giziug  (*teugiz) Zeug,  Gerät,  Ausrüstung^,  nhd.  Zeug,  mnd.  tüch  (-//-)  n.  ;,Zeug,  Gerät^ und  ,Zeugungsglied^,  mhd.  ziugen,  nhd.  zeugen]  got.  ustauhts  ,Vollendung^, ahd.  mhd.  zuht  f.  _,Ziehen,  Zug,  Erziehung,  Zucht,  Nachkommenschaft^, nhd.  Zucht  (=  lat.  ductus  s.  oben);  davon  nhd.  zilclitig,  züchtigen,  ags. tyht  m.  ^Erziehung,  Zuchf^,  afries.  tucht,  tocht  ,Zeugungsfähigkeit^
2:Bes.  wegen  Zucht  ,Nachkommenschaft^,  bair.  auch  ,Zuchtschwein'^  u.  dgl.
3:zieht  man   ahd.  zöha,   mnd.   töle  [^töhila),  nhd.  schwäb.    zauche    , Hündin^,
4:neuisl.    töa    , Füchsin^    zu    unserer  Wz.;    doch    vgl.   mhd.   zü])e    , Hündin^,
5:'norw.  dial.  tohhe  ,Stute,  kleines  weibliches  Wesen^   und   germ.  "^tikö  und
6:*titö  ,Hündin^
7:Eine  einfachere  Wzf.  '^deu-  ,ziehen^  vielleicht  in  anord.  tjödr  n.  (*deu- trom)  ,Spannseil,  BindeseiF  =  mengi.  teder,  tej)er  ds.,  ahd.  zeotar  ,Deich- seP,  nhd.  bair.  Zieter  ,Vorderdeichsel^  (auch  ags.  tüdor,  tuddor  n.  ,Nach- kommenschaft^?);  aber  ai.  dörakam  ,Strick,  Riemen'  ist  dravid.  Lw.  (Kuiper Proto-Munda  131).
8:WP.I  780  f.,  WH.  I  377  f.,  861.
9:deup-  (:  kteup-?)  ,dumpfer  Schall,  etwa  wie  von  einem  Schlag*";  Schall- wurzel. Gr.  hom.  dovTtog  ,dumpfes  Geräusch,  Getöse;  Schall  der  Fußtritte'; dovTieu)  jgebe  einen  dumpfen  oder  rasselnden  Ton  von  mir';  der  in  hom.  sydov- TtrjGap,  iglydovTtog  ,laut  donnernd'  ((.KxalyöovTtov  .  . .  ixsyaXörjXOv  Hes.)  zu- tage tretende  ursprüngliche  Anlaut  yö-  ist  vielleicht  mit  xrr/rog  ,Schlag' neben  Tvrrog  parallel  oder  ihm  nachgebildet,  so  daß  über  sein  Alter  keine Sicherheit  zu  erlangen  ist;  nach  Schwyzer  wäre  {y)dov7ieo)  Intensiv  zu schwachstufigem  xtdtt-;  serb.  düplm,  düpiti  ,mit  Getöse  schlagen',  sloven.
10:222
11:düpam  (dupljem)  dupati  ,auf  etwas  Hohles  schlagen^  dumpf  rauscher dupotdtij  bulg.  düp'^  ,gebe  einem  Roß  die  Sporen'^  lett.  dupeties  ,dum| schallen'  (bsl.  d-  aus  gd-?  oder  älter  als  gr.  yd-?)]
12:nach  Van  Windekens  Lexique  138  hierher  toch.  A  täp-  _,ertönen  lassei verkünden*^  (*tup-)  im  Infin.  tpässi,  Partiz.  Pass.  cacpu.
13:WP.  I  781  f.,  Endzelin  KZ.  44,  58,  Mühlenbach-Endzelin  I  518,  Schwyzer Gr.  Gr.  I  7181
14:d9gb-mö::s  ,schief'?
15:Ai.  jihmd-li  ^schräg,  schief'  (urar.  Hizhmd-  assimil.  aus  *dizhmd-)j  gj.^ d6x!^iog,  öox^ög  ^schief  (assimil.  aus  *dax!.i6g)'
16:Pedersen  KZ.  36,  78,  WP.  I  769.  Andere  Möglichkeiten  s.  unter  geU ,drehen,  biegen'.
17:digh'  , Ziege'.
18:Gr.-thrak.  öi^a'  ai^.  ^dyaüveg  {*diglnd),  vgl.  den  thrak.  PN  ^il^a-XEl^iq (wie  ^EßQOv-TBXp,Lg  zu  eßgog'  rodyog  Hes.);  ahd.  ziga  ,Ziege',  mit  hypo- korist.  Konsonantenschärfung  ags.  ticce^ij  ahd.  zicktj  zickln  , Zicklein' (aber  über  nhd.  Zecke  s.  oben  unter  deigh-)]  hierher  vielleicht  norw.  dial. tikka  
19:,Schaf'  (event.  Kreuzung  von  schwed.  dial.  takka  ,Schaf'  mit  einer nord.  Entsprechung  von  Zicklein)^  tiksa  ,Schaf,  Hündin',  tikla  ^junges Schaf  oder  Kuh',  sowie  anord.  tlk  f.  ,Hündin'  =  mnd.  tlke  ds.
20:Arm.  tik  ,Schlauch  aus  Tierfell'  wird  von  Liden  (Arm.  Stud.  10  f,^ Don.  nat.  Sjdow  53^)  als  ursprgl.  , Ziegenfell'  hierhergestellt,  müßte  jedoch auf  *dig-  zurückgehen  (tabuistische  Entstellung?).
21:WP.  I  814,  WH.  I  632,  868.  Nach  Risch  (briefl.)  vielleicht  ursprüngl; Lockruf.
22:dlp-ro-y  dip-erä  ,Opfertier,  Vieh'.
23:Arm.  tvar  ,Schafbock,  Herde  von  Großvieh'  (*t{var  <  *dxpera)]  got.  tibrW. ,Opf ergäbe'   (verbessert   aus   aihr),  ahd.  zebar  ,Opfertier',   ags.  tiferj  über ds.,  spätmhd.  ungeztherej  unzTver,  nhd.  Ungeziefer  eig.  ,unreines,  nicht  zum Opfern  taugliches  Tier'.  Afrz.  (ajtoivre  , Zugtier'  stammt  aus  dem  Germ.
24:iW^r
25:WP.  I  765,  WH.  I  323,  Feist  19  b,  477  a.  ?.>gf
26:dlkii-i?)  ,süß'.
27:Gr.  ylv/,vg,  yXvyiSQog  ,süß',  ylvTCKÖv  yXv%v^  y%vy.y.a'  ij  ylvT^mr^g  Hes.  (-xx- aus  -ku-),  ylevY.og  (spät)  ,Most'  (Ablautneubildung);  yX  aus  dl  wegen  des folg.  x;  -Iv-  aus  -Xa-  nach  dem  folg.  v;  über  späte  devY,og  ,Most',  öev/.rig ,süß'  s.  WH.  I  380;
28:lat.  dulcis  ,süß,  lieblich,  sanft'  (aus  *dlkui-s).
29:WP.  I  816,  WH.  I  380.  '   ^  1^1
30:223
31:S-bü,  dn^huä  ^Zunge^;  oft  durch  Anlautswechsel  und  Umstellungen umgestaltet.
32:Vi.  jihvä  f.,  av.  hizvä  ds.  (vorar.  *yighuä.  aus  *-daghuä  mit  i  von  ZiÄ-  ;,lecken^ Qjer  von  _;*ä-  ;ab\värts  wenden^;  iran,  *sizva  wohl  durch  Sonorendissi- uiilation);  daneben  tl-Stamra  in  ai.  juhü  f.  ^Zunge,  Löffel^  (mit  u  nach juhöti  ;,ins  Feuer  gießen^^  anders  Wackernagel-Debrunner  III  192),  av. Jiizü  m.  ds.;  mit  -ön-  für  -ä  apers.  hizhäna-,  mpers.  hvzvän  ds._,  nordar. hiBn  m.  ,Zunge;  Rede^   (*vUhvän  nach  E.  Leumann  Nordar.  Spr.  127  f.);
33:arm.  le^u,  Gen.  lezvi  setzt  im-Ausgang  das  -ghuä  von  *dnghuä  fort, die  erste  Silbe  wohl  von  leigh-  ,lecken'  beeinflußt;
34:alat.  dingua,  lat,  lingua  (mit  ^  von  lingere)-  osk.  fangv am  (Vetter  Serta Iloffillenana  153;
35:air.  teng  («-Stamm)  und  tengae,  Gen.  tengad  mit  t-  nach  tongid  ,schwört^; aber  air.  ligur  ,Zunge^  zu  lat.  Ugurriö;  unklar  ist  mcymr.  tafaiot,  cymr. tafodj  acorn.  tauot^  mbret.  teaut,  bret.  teod,  wozu  com.  tava,  mbret. taffhaff,  bret.  tanva  ,kosten^  (kelt.  '^tamäto-'^)
36:]
37:o-ot.  tuggö  Ly  an.  as.  tunga^  ags.  tunge,  ahd.  zitnga^  mit  -ön-  statt  -ä; als  Ablautneubildung  vielleicht  hierher  ^nord.  tangi  ,Griffstück  der  Klinge^ rand.  tange  _,Sandrückea  zwischen  zwei  Sümpfen^;
38:bsl.  inzä-  m.  in  apr.  insuwis]  lit.  liezüvis  (nach  liezti  ,lecken');  aksL j§zy-ki,  skr.  jezik,  poln.  jezyk^  russ.  jazyk;  zum  Schwund  des  anlaut.  c^- s.  J.  Schmidt,  Krit.  77;
39:toch.  A  käntu,  Gen.  käntwis,  B  känfwo,  Obl.  käntwa  sa  {^kantwaj  um- gestellt aus  '^tankica,  idg.  *dnghua).
40:WP.  I  1792,  WH.  I  8U6f.,  Trautmann  104,  Specht  Dekl.  83,  Havers Sprachtabu  123  f.
41:cfö-  :  d9',  auch  dö-u-  :  dQU-  :  cfu-  ,geben^  (perfektiv),  Aoristwurzel  mit  sekun- därem    Präsens     di-dö-mi,     Nominaibildungen:    do-no-m,    dö-ro-tn^ dö'ti-s,    d9-ti-s    ,Gabe',    dö-ter-    ,Geber^,    Partiz.    dö-to-s,    dQ-to-s, 'd-tos,  Infinitiv  dö-men-ai,  dö-uen-ai. Ai.    dd-dä'ti  (Aor.  d-dä-m,   Opt.   deyäm,   Fut.  däsydti,   Aow  Med.  ddita ==  gr.    eöozo,   Inf.  ddmane  :  gr.  ööjxsvai,   vgl.   lat.  daminl,  falls   ursprüngh Infinitiv)  ^gibt*"  (päli  cZmna  zu  einem  Präs.  "^di-dä-ti),  av.  dadäiti  ds.,  apers. Imp.    dadätuv    ,er    soll   geben';  Wurzelnomen    ai.    dä[s]  dstu  ,dator    estu'; Infin.    dätum    (:lat.    Supin.    cZa^wm);    Partiz.    ditd-h    (unbelegt),    sekundär dattd-h,  schwundstuf,  in  ä-t-td-h,  prd-t-ta-h  ^hingegeben',  ablaut.  in  tvä-däta-h ,von  dir  gegeben',  av.  däta-j  zum  Fut.  ai.  däsyämi  (:  lit.  düosiu)  s.  Schwyzer Gr.  Gr.  I  78811;
42:arm.  ta-m  ,dö',  ta-m¥  ,damus'  {*dd-ie-mi)j  Aor.  etu  (==  d-dä-m,  idg. *e-c?ö-m);
43:224
44:gr.  öl'dco-^u  ,gebeS  Aor.  edcüVM,  Opt.  öoi7]v  (*donem),  Fut.  dwao),  Aor. Med.  l'JoTO;  Partiz.  doTÖg,  Infin.  hom.  öö^evai  und  hom.  tliess.  usw.  do'^jj, (su  ffixloser  Lokativ) ;
45:ven.  zoto  ,dedit^  =  gr.  eöoTO]  zonasto  ^döiiävit^  vielleicht  aus  *dönä-s-to von  einem  denom.  *dönäiö  (*c?ö?20-m  :  lat.  dömim)]  mess.  pi-do  (*dö-t:^[^ ■a-dät):
46:alb.  da-sh'd  Aor.  ^icli  g'aV  (*dd-S7n)]
47:lat.  döj  das,  dat,  dämus  (*dd-mös),  dätis,  dänt  (sekundär  für  *dent  aus *{di)-dn-ti),  alat.  danunt;  dedl,  dätum,  däre  ;gebe^  gewähre^,  refl.  ^begebe niich^  [das  mit  ä  nach  stä-  für  *c?ö  =  lit.  diid,  düo-h  [Specht  KZ.  55 182],  gr.  hom.  di-öio-d-i)',
48:vest.  di-de-t  ^dat^^,  pal.  cZi-<?a  ,det-,  mixCov.  dir sa,  der sa,  tera  ^det^  (*didät) tePtu,  dirstu,  titii  ^dato^  (*d{-de-töd),  tefte  ,datur^  {*di-da-ter)j  a-tef-a-fnst jCircumtulerit^  (^am-de-da-fos-t)-^  osk.  da\^da]d  ^dedaf^  (*däd(-di)-däd),  dadid ,dederit^  (*däd(-de)-did),
```


## [2026-09-05T20:09:41.997Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==235' POK_01.txt | sed -n '1,40p'",
 "description": "Pokorny p.225 area"
}
```


### [2026-09-05T20:09:43.636Z] TOOL RESULT

```
]
o-ot.  tuggö  Ly  an.  as.  tunga^  ags.  tunge,  ahd.  zitnga^  mit  -ön-  statt  -ä; als  Ablautneubildung  vielleicht  hierher  ^nord.  tangi  ,Griffstück  der  Klinge^ rand.  tange  _,Sandrückea  zwischen  zwei  Sümpfen^;
bsl.  inzä-  m.  in  apr.  insuwis]  lit.  liezüvis  (nach  liezti  ,lecken');  aksL j§zy-ki,  skr.  jezik,  poln.  jezyk^  russ.  jazyk;  zum  Schwund  des  anlaut.  c^- s.  J.  Schmidt,  Krit.  77;
toch.  A  käntu,  Gen.  käntwis,  B  känfwo,  Obl.  käntwa  sa  {^kantwaj  um- gestellt aus  '^tankica,  idg.  *dnghua).
WP.  I  1792,  WH.  I  8U6f.,  Trautmann  104,  Specht  Dekl.  83,  Havers Sprachtabu  123  f.
cfö-  :  d9',  auch  dö-u-  :  dQU-  :  cfu-  ,geben^  (perfektiv),  Aoristwurzel  mit  sekun- därem    Präsens     di-dö-mi,     Nominaibildungen:    do-no-m,    dö-ro-tn^ dö'ti-s,    d9-ti-s    ,Gabe',    dö-ter-    ,Geber^,    Partiz.    dö-to-s,    dQ-to-s, 'd-tos,  Infinitiv  dö-men-ai,  dö-uen-ai. Ai.    dd-dä'ti  (Aor.  d-dä-m,   Opt.   deyäm,   Fut.  däsydti,   Aow  Med.  ddita ==  gr.    eöozo,   Inf.  ddmane  :  gr.  ööjxsvai,   vgl.   lat.  daminl,  falls   ursprüngh Infinitiv)  ^gibt*"  (päli  cZmna  zu  einem  Präs.  "^di-dä-ti),  av.  dadäiti  ds.,  apers. Imp.    dadätuv    ,er    soll   geben';  Wurzelnomen    ai.    dä[s]  dstu  ,dator    estu'; Infin.    dätum    (:lat.    Supin.    cZa^wm);    Partiz.    ditd-h    (unbelegt),    sekundär dattd-h,  schwundstuf,  in  ä-t-td-h,  prd-t-ta-h  ^hingegeben',  ablaut.  in  tvä-däta-h ,von  dir  gegeben',  av.  däta-j  zum  Fut.  ai.  däsyämi  (:  lit.  düosiu)  s.  Schwyzer Gr.  Gr.  I  78811;
arm.  ta-m  ,dö',  ta-m¥  ,damus'  {*dd-ie-mi)j  Aor.  etu  (==  d-dä-m,  idg. *e-c?ö-m);
224
gr.  öl'dco-^u  ,gebeS  Aor.  edcüVM,  Opt.  öoi7]v  (*donem),  Fut.  dwao),  Aor. Med.  l'JoTO;  Partiz.  doTÖg,  Infin.  hom.  öö^evai  und  hom.  tliess.  usw.  do'^jj, (su  ffixloser  Lokativ) ;
ven.  zoto  ,dedit^  =  gr.  eöoTO]  zonasto  ^döiiävit^  vielleicht  aus  *dönä-s-to von  einem  denom.  *dönäiö  (*c?ö?20-m  :  lat.  dömim)]  mess.  pi-do  (*dö-t:^[^ ■a-dät):
alb.  da-sh'd  Aor.  ^icli  g'aV  (*dd-S7n)]
lat.  döj  das,  dat,  dämus  (*dd-mös),  dätis,  dänt  (sekundär  für  *dent  aus *{di)-dn-ti),  alat.  danunt;  dedl,  dätum,  däre  ;gebe^  gewähre^,  refl.  ^begebe niich^  [das  mit  ä  nach  stä-  für  *c?ö  =  lit.  diid,  düo-h  [Specht  KZ.  55 182],  gr.  hom.  di-öio-d-i)',
vest.  di-de-t  ^dat^^,  pal.  cZi-<?a  ,det-,  mixCov.  dir sa,  der sa,  tera  ^det^  (*didät) tePtu,  dirstu,  titii  ^dato^  (*d{-de-töd),  tefte  ,datur^  {*di-da-ter)j  a-tef-a-fnst jCircumtulerit^  (^am-de-da-fos-t)-^  osk.  da\^da]d  ^dedaf^  (*däd(-di)-däd),  dadid ,dederit^  (*däd(-de)-did),
```


## [2026-09-05T20:09:43.911Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== PHD dād\"; grep -n \"^dād\\|^dāšn\\|^dahišn\\|^dādār\\|^pādāšn\\|^hōšyār\\|^dāsr\\|^day\\b\\|^dād-\\|^dahi\" PHD.txt | head -40; echo \"=== PHD mackenzie\"; grep -n \"^dād\\|^dāšn\\|^dahišn\\|^dādār\\|^pādāšn\\|^hōšyār\" PHD_mackenzie.txt | head -40",
 "description": "MacKenzie Pahlavi lookups"
}
```


### [2026-09-05T20:09:43.977Z] TOOL RESULT

```
=== PHD dād
307:dahigan 24 darzig
308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
1497:day rēz; — and night r6z-šaban.
5543:dādwar Sy тех dādwarīh xD у мехо Чачап, gādan 19545 āy-! - ot āmadan! VV Wrens jādūgīh AD SAMA jādūg VS MAT jādag-gūwīh A yr SU jadag-gow — SP 5tex5 jadag (EI EI dādmeh +36 ONS dādestān w^ FO) Per
5579:dahišn, Jah
=== PHD mackenzie
```


## [2026-09-05T20:09:48.688Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dādār\\|dādan\\|dāšn\\|pādāšn\\|dahišn\" PHD.txt | head -30; echo \"=== size\"; wc -l PHD.txt PHD_mackenzie.txt",
 "description": "grep PHD for dādan etc"
}
```


### [2026-09-05T20:09:48.737Z] TOOL RESULT

```
122:/abāz dādan б: 1. attribute, ascribe to; 2. appoint to. br ... add M fr! va-čār add helpless. delete á-distag ... (read ayidtag) add ‚тах |°р1°с | N farāz] acclivity. Afson ... add M ?pswn. Vagar ..., add useless. vāgēš [kw | (M "^ wa, P ?gwc), N aqóš] embrace, armful. add vājištag | gyštk' | P * gyšt, N ayišta] mixed, defiled. add \Ahliswang |*hlygwng] = Ard. delete Khriswang ... for alum ... read „alum |? № | N <] millet. Vāsnūd(ag) ... delete noble. aswür [|PR/LSYA < A pršy';.. āšnāg ... add acquainted with. āštīh ... add concord. ayad ... read |" byd^t' |... for bahr... and bahrag ... read bahr(ag) |b hl(k') | M bhr, N ~(a)] part, portion, share, lot; reason. (az) an bahrag ray : on that account, therefore. for  bahrwar ... read bahr(ag)war [b'hl(k)wl | N bahrawar| partaking, parti- cipator, partner. ~th : participation, advantage. balay add M by. add balgam |[blgm | N balyam] phlegm. baxtan ... add divide. bayaspān [by?sp^n' | = M]... bélür ... for M read P bylwr.
292:*brinj [binc | (M bryng), N birinj] bronze, brass. ~én [-yx!] bronze, brazen. brinómand [blyn’wmnd] delimited. brištan, bréz- [blystn', blyc- | M bryz-, N biristan] roast. brüg [blwk' | M brwg, N abrü] (eye)brow. büdan, b(aw)- [YHWWN-tn! < A yhwwn, У hwh; bwtn', b- | M bwdn, bw-, N büdan] be, become. bawišn: becoming, genesis. büf [bwp | N <), *büg [bwk'] owl. buland [bwind | = M, N ~] high. būm [bwm | N ~] land, earth, country. ~-€andag [-cndk'] earthquake. Ibun [bwn' | = M, N ~] base, foundation, bottom. *bun [bwn! | N ~] = wan. bunag [bznk! | N ~a] baggage; abode, camp. — daštan: dwell, settle. bun-dahišn(īh) [bzundhšn!, -yh] primal creation. bunih [bwnyh] beginning. buništ [bwnyst! | = M] foundation. ~ag [-k'] principle. bun-kadaģ [bwnktk'] original house, home. bun-xān [bwnh?n'] source. bur-, —išn, v. buridan. burāģ [bzoP RU] cutting, sharp. burām-, v. bram-. burd [bwit! | M bwrd] patient. ~ih: patience. burdan, bar- [Y BLWN-tn! < А У ybl; bwltn', bl- | M Бата, br-, N <] carry, bear, take, endure. ~išn: bearing, behaviour. burdār [bwit!]] bearer; womb. ~ih: patience. burd-ešnēhr [bwit! fnwhl | P bwrdyfnwhr] grateful, thankful. burg [bwig | (Ar. burj)] tower. buridan, bur- [bwl-ytn! | M bwr-, N ~] = bridan. —j$n: cutting. Burz [bwic] the god of agriculture. Burzénmihr [bwlcynmtr!] the third major Fire of Sasanian Eran, that of husbandmen. burzidan, burz- [bwlc-ytn'] praise, honour. ~i$n: praise, honour. —iŠnié : praiseworthy. buš [ро | N ~] mane. būšāsp [bwPsp | M bwsy'sp, N ~] sleep, sloth; dream. * but [bwt! | = M, N ~] Buddha; idol. buz [AZ < A ‘z; Бос | N ~] goat.
306:īdabr [dpi] sinner, deceiver. *dabr [dpl] *dark-coloured. dad [dt' | M dd, N ~] wild animal. 1ааа [d't! | M d?d, N ~] law, justice; those scriptures dealing with legal matters. даа [d’t' | N ~] age. зааа [d>1!] tooth. tdād, v. ahlaw-dād. dādan, dah- [YH BWN-tn! < A Vyhb; d*tn!, dh- | M d'dn, (dy-), P dh- N ~, dih-] 1. give; 2. create. —išn [dh(y)sn'] giving, donation; creation. dādār [d’t?l | N ~] creator. -- ih : creatorship. dādestān [DYNA < А dyn; d'ts?n! | M d'(d)ys?n, N dá(de)stan] judgement, justice, law; case, process. dàd-gàh [2^? gs] proper place, fire temple; = daxmag. dādīg [d'tyk'] legal, concerned with the Law. dad-meh (d"tms] adult, elder. dādwar [d?twbl | (M d^ywr, P d'dbr), N da(d)war] judge. ~ih: judgement. daftan, dam- [dptn', dm- | M dm-, N dam-idan] breathe, blow. «dišn: breath. daftar [dptl | N —] register, account-book. dagr [AL YK < А ryk; dgl | M dgr > dur, N dër] long. dagrand [дата | N dërand] long. ~«xwaday [-hwt’y] eternal, of long dominion. daģr|-pattāy [dgl pt'd] long-lasting. -—-zamáàn [-2т?п!] a long time. ^-zi(w)isn [-zywsn'] long-lived. dah [ro, ASLY A < A ә | M dh, N ~] ten. dah-, —išn, v. dádan. Юаһаӣр [dř k' | (N Dahàk)] = Azdahág. dahān [РИМЕ < A p(w)m-h | M dhyn, N даһап] mouth. dahibed [dhywpt! | M dhybyd] ruler, lord of the land.
310:das [d’s | N ~] sickle. dàs?r [d’sl = Av. dātra-) gift, reward. dast [Y DE < A yd-h; dst! | = M, N ~] hand. dastag [dstk! | N —a] bunch, bundle, group. dast(a)gird [Y DE., dst-krt! | M dstygyrd, N dastgird] estate. dast- gir [dst OH DWN, (v. griftan) | N ~] 1. helper; 2. captive. dast-graw [dstglwb!] captivity. dast-kàrih [ҮЛЕ ГУА | N ~7] handiwork. dast-šūy [dstšwd] = ģūmēz. dastwar [dstwbl | М dstwr, N dastür] authority, priest, minister. ~th: custom; authority. dastyar [dstyd?l | (P dstd’r), N ~] helper. ~th: help, assistance. dašn [dšn! | = M] right hand. dāšn [d”$n' | M d’s(y)n] gift. dašnaģ [dsnk' | N ~a] 1. right hand; 2. dagger. dašt [dst! | = M, N —] plain, open ground. daštān [dft?n! | N ~] menstruation; menstruous. „estān [-st?n'] secluded place for menstruous women. -—--màh [-m?h] menstrual cycle. -ūmand [-’wmnd] menstruous. dāštan, dar- [YHSNN-tn! < А V ben: d^ftn', Pl- | M d'An, ar-, N ~] have, hold, keep, preserve. pad . . . dāštan: hold by, to; take for. pad éd dāštan [cf. N pindāštan] consider. --išn: preservation, maintenance. dāštār [4° #1 keeper, preserver. daw-, v. dawidan, dawistan. idawāl [dwb’l | N ~] leather, skin. ždawāl [dwbl | N ~] deceit, trickery. idawīdan, daw- [LH TWN-tn! < A Vrht; dwytn', dwb- | M dw-, N ~] run. *dawidan, daw- [dw-ytn'] speak (daevic). 1, 2 dawistan [LH TWN-stn!, dwstn'] = 1 * dawidan. daxmag [dhmk' | P dxmg, N ~a] tomb, dakhma (a building where corpses are exposed for destruction). „estān [-si?n!] cemetery. dax$ag [dhšk! | M dxsg] mark, sign, characteristic; memory. pad ~ dàštan : remember. az — hištan: forget. ~6mand [-’wmnd] marked. Day [ddw' | M dyy, N ~] Creator; cal. roth month; 8th, 15th, 23rd days. dayag [d^yk! | M d?yg-, N ~aj (wet-)nurse. „ānīh [nyh] | (N dāyagī)] nursing, nurture. dazidan, daz- [dc-ytn'] burn, scorch. --išn : burning.
325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
536:pa(č)čēn [pcgn!] copy. *pa(č)čībāg [pcyp k', PWNe- | N *pajiw] *deceptive. ^h : deceit, hypocrisy. *pa(č)čībāy- [pcyp'd-, PWNc-] deceive. pad [PWN, for *pty | M pd, N pa] to, at, in, on. pad- [pt- | M *pd-) fall. padam [pd”m | (IN pandm)] mask for the mouth, worn by a celebrating priest. !Ipádan, pày- (UIN TLWN-tn! < А V ntr; Ptn, pd- | M pd, p’y-, N páyidan] protect, watch, defend. *pádan, pāy- [N TLWN-tn!, etc.] stand, wait. pādāšn [p?td?fn! | M p’d’syn, N pàdàs] reward, retribution. padēx [ptyhw'] flourishing, prosperous. ~ih: prosperity. padéxénidan, padéxén- [ptyhwyn-ytn'] make flourish, prosper. pādēz [p'tyc | M p'dyz, N pāyēz] autumn. pad-góhr [PW Ngwhl] т. jewelled; 2. of good stock, well-born. padifrah [p’tpl’s | M p'dypr?h, N *pādafrāh] punishment, retribution. padir-, ~išn, v. padiriftan. padirag [ptylk' | M pdyrg, N paóira] towards, against, counter-. (6) — madan: come to mect. ~ih: meeting, opposition.
653:~agig [-yk!] movable; intercalary (year). wihir- [whyl- | (M whwr-)] change. —išn: change. wimand [wymnd | = M] boundary, frontier, limit. ~ig, —6mand [-yk', 2wmnd] bounded, limited. *wiméhgén [wmyhkn! | M wymyh-] *shapely. wimustan [uwymwstn! | M wymrz- (< P)] spoil, destroy. win [wn'] vina, lute. wināh [zs | М zoyz)h, N gunàh] sin, crime. winahgar [wsk] | M wwhg’r, (N gunahhar)] sinner. ~ih: sinfulness. wināhīdan, wināh- [wn’s-ytn' | M wyn’h-] spoil, damage, destroy. ~išn: damage, destruction. winastag [wnstk'] spoilt, corrupt. windādan, wind- [HŠKHWN-tn' < А ME, V skh; wnd'tn! | M wynd'd, wynd-} find, obtain, acquire. ~išn: acquisition, earnings. ~ignig : findable. winjišk [zvxcšk! | N gunjišk, binjišk] sparrow. win(n)ārdan, win(n)àr- [wyx?7-tn' | M wyn’r-dn] order, fix, arrange. ~išn: arrangement. win(n)irdan [wynltn' | M wynyrdn) be arranged, established; stay. iwir [wyl | M wyyr] man, hero. *wir [wyl | M wyr-, N bir] memory, mind. *wir [wyl | N bir] thunderbolt. wirāstan, wirāy-, (P wirāz-) [wyl’stn', wyPd-, (wPc-) | M турі, tyr y-, (P wyr st, wyr!z-)] arrange, prepare, cultivate, restore. —jišn(ih): arrangement, preparation. wirég [wlyk! | N guréy] flight, escape. wiréxtan, wiréz- [OL YKWN-tn! < А У ‘rq; wlyhtn', wlyc- | P wryxt, N guréxtan, guréz-] flee, escape. wirdmandih [wy”wmndyh | M wyrwmndyy] memory. wirózag [*wiwck! | (P wrwe)] lightning. wis [wys | = M] village. wisandan, wisān- [ws’n-dn'] separate. —išn(ih): separation. wisay- (ws'd- | M wys’y-] rest. wisbed [wyspt! | M wysbyd] village headman. wisé [wsydy | (P wsyd), N gusë] despatch. ~ kardan: send, despatch. wisistan, wisin(n)- [wsstn', wsyn- | N gusistan, (gusil-)] break, split. wisp [wsp | M wysp] all, every. wispurdan, *wispar- [wspwltn'] tread, trample. wist [20; wyst! | = M, N bist] twenty. wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw. wistar(ag) [wsti(g) | N bistar] bedding, cover.
860:ascribe to abāz dādan 6.
1436:create af(u)ridan, (frāz) brēhēnīdan, dādan, tāšīdan; (daevic) kirrén- idan.
1437:creation āfurišn, brēhēnišn, (bun-) dahišn; dám.
1679:donation dahišn.
1937:find windādan.
2099:gift āyaft, dāšn, pārag, das?r.
2410:increase (n.) abzón, abzāyišn, fra- dahišnih, mehēnišn.
2961:obtain ayāftan, windādan.
3240:progress (n.) frādahišnīh,
3423:retribution pādāšn, pādifrāh..
3437:reward mizd, pādāšn, dās*r.
4688:frahixtan frahixtag frayádisnig fravādišn frāy frādahišnīh frahist farroxīh farrox lxwah-I xwastant frārāst frārūnīh frārēn frāmēš frūmēš- frāmuštan frahist parrag frch pardāxtan frehbūdīh frehbūd pardāz-
4742:padyabib, ALI 00 t€» о) pādāšn VA My o padirán- ` - My yey a pādīrānēn- -p ry yey a pādīrānēnīdan W3 y ry We pādīrānīdan WS wy veyo pādīrān wey yey os paymar Ne теу o pādēz 23 voy o lpādan Y rero) pādofrāh ау\һе» 0) padzahr NS ve» o» pāygūs ISYA padrozag 15 cP rere pāyram » rey’ о
5200:wināhgārīh d: AS 4431 niwāg aru | wināh- - 35211 winühidan TL 11 wināhišn 1745.29 41 nang Au wind- - 23 windādan Wed 11 niwéy- — 4911 niwéy- e 41) niwēyēn- -P niwčyēnīdan “тёз v 4911 niwē, wandag 155 141 wanigarih «D As" niwēyišnīh Be r^ 4311 niwévisn VU 4) VI windišnīgs Vays | windišn tr 1) wahmān', wan, win Au wanand AW nozdah ap i nog 1311 nógzad res aw nūgzādag sterd 411 nógróz an 53
5542:[66] dāštan nh moo dādār, gādār `> və O dādārīh ANS t€. X5 dādgāh Tr хэ dādīg 155 t$ dad, jad, yat, yazd weno
5554:rasián! rasidan! gāhānbār gāhānīg gāhān -īhistan vāzdah gāwdumb gazar dahišn, dāšn Чах$арбтапа daxzag
5579:dahišn, Jah
=== size
  5578 PHD.txt
 12397 PHD_mackenzie.txt
 17975 total
```


## [2026-09-05T20:09:49.274Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==65' NYB_vol2_glossary.txt | head -60",
 "description": "Nyberg glossary p.56 (leaf 64/65)"
}
```


### [2026-09-05T20:09:51.967Z] TOOL RESULT

```
-14, 441-9. — Bor- rowed from Av. (581) carāttī-.
cäreh |e'lyh] 110°: my emendation *fra- hang — was unfounded; restore the MS reading pl’hw (last w. of a line, cramped hand) c*lyh and v. fràx*-càreh.
earm [clm] skin, hide 3211. — = NP; Av. (582) caraman-; MPrs crm (A-H I).
carp [clp'] mild, gentle 688. — MPrth crb (A-H III); Arm. lw. carp ‘fat’ = Bal. = NP carb; Paz. carv.
earpéh mildness, gentleness 7021,
cāšišn [c”ššn'] teaching 8925. — V. cāštan. cašm [cšm, ’YNH] 1. subst. eye 6?? and passim. — 2. adj. conspicuous, comp. ~-tar 56°. — Av. (583) cašman-; MPrth Prs c&m; = Paz. NP.
cašmak the preceding w. in a compound: kamar i 7- ~ a belt with seven “eyes” (plaques) 1211.
ea$m-kài [cšmk”y] having (all) eyes fastened (on oneself) = exposed to people’s (contemptuous) looks, an object of derision, dishonoured, pl. cas. obl. ~-kayan [-k’d’n'], comp. [c3mk’stl] cašm- kāh-tar (thus K; TD, [ešmk'dtl] cašm- kāi-tar) 1522-28, — MPrs cömg’h in the same sense (SalM III-IV, no. 9b°; Henning, GGN 1932, 223 n. 4, where, however, the pejorative sense is not recognized). The alternation -käh: -kāt is also found in the parallel formation tars-käh (PT 65? -k’s): tars-käi (DkM 4811’) ‘reveren- tial, respectful’, abstr. tars-kāhēh (-k’syh) ibd.1.21, but Cod. K (ad 1.) tars-kčiyeh (-k’dyh). Same formation in MPrs gylg’y (S; Verbum 205) < "gil-kdi ‘lamenting’ ; shyk? = sahik-ka(i) ‘frightened’ (preserv- ed -k- indicates -kk-), v. also mānā(k)-kāt.
www .parsianjoman.org | col wok
casm-käi
— -küi < *käya- ‘regard, look’, cf Skr cäyati, -te ‘to notice, to observe, to be- hold’, käya- ‘goal, aim’ (not to be con- founded with käya- ‘body’); root kä-, v. ākāh, nikäh, and gukäi, in which the same alternations in the final are ob- served. — Neriosengh mistook the last element of —, which he found in the form -käh, for käh- ‘to diminish’, Paz. xäh-, hence his reading casm-xdhisn(itar) ; Skr. v. adarsaniyaltara).
cäStan [c'štn'] to teach, pt. = pret. pass. 3d p. sg. cāšt 911. 9421. — Paz. cāšīd. Av. (461) kaš-, pres. caš-, (583) cašan- 'teach- er’. Skr. v. dsvddayati, subst. āsvāda, is due to confusion with another cāš- ‘to taste’, cf List 82. — V. cašišn.
eatrang [ctlng] chess 315, 118-119 passim. 12111-14, — Borrowed from Skr catur-aūga- ‘having four ranks’ (v. 1198-15); Arab. lw. Sitran).
catrušvitak [ctlwšw'tk'] a fourth, a . quarter, a cubic measure 42%. — Borrowed, and reshaped, from Av. (580) cadrušva-, cf srisvätak.
cê [MH; cyh 12111] 1. interrog. pron. what? 59. 726. 89? ete.; how? 1513, 51?!; with prep. 6 cé, pat cé, hac cē; cé rād? why? 351! ete.; combined with a subst.: ce zaman? 715, cē gah? 722; pat ce āivēnak? how? 76%; cé vinäs? 121, cē vat? 7322, etc. ; apar cē ātvēnak margēnītan i Zartuxst pursit how to kill Z. 4912-25-26, 4813-14 (apar governs the whole clause). — 2. rel. pron. what: či ndmakY ce ... nipištv estet, ce Šahpuhr" . . . framätY nipigstany P 2:3-4; kart" ... ce ... sahät P2:8-9; har ce 61.3218, 86%. 9618; ēt ce ... apāc āvurt 11214715; 361; pat hàn cim rād ce 121". — 3. conj. a) subordinating: because 105); ce ka id. 991. — b) coordination: for 2
```


## [2026-09-05T20:10:13.156Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dātan\\|^dātār\\|^dahišn\\|^dāsr\\|^dās\\|^pātdāšn\\|dāt°r\\|dātār\" NYB_vol2_glossary.txt | head -30",
 "description": "Nyberg glossary d-entries"
}
```


### [2026-09-05T20:10:13.211Z] TOOL RESULT

```
1166:dahišn [dhšn'] 1. creation, the act of creating 3615-16, 4117.18, 1099. — 2. coll. the created things: dám u ~ 3311. 762. 772.18.14.20, 7913. 881.16, 894, 915-9, 923; — created being, pl. cas. obl. —-ān : ast-~- an, v. ast; menöi u getäh —-än the heaven- ly and the earthly created beings 8816; — 621. From dätan; Paz. dahisn(i). Not in MPrthPrs (NP dihiš ‘gift, alms’ is a recent formation). Coincides in writing with dāšn and jahišn, v. these ws.
1230:dātār [d^t?]] the Creator 5711; epithet of Ohurmazd, passim; creative principle 64°. dātārēh 1. the act of giving 704. — 2. the quality of being the Creator 71°.
2802:dātār ~, passim; ~ apazonik (q. v.); ~ + x"atài 1222, 745. 75%. "7922, 85H. 894. 12015; ~ bag 2117. 22%; rēc + ~ the first day of the month 95%. — 2. the star of Jupiter 510-12, 77, — 3. n. pr. of human beings: a) the king ~ son of Shapuhr 165—179. 11618; ~ son of Artaxsér 11617; b) a Mobad 1104. — Av. (285 sqq.) Ahura- Mazdāh- in two separate ws.; inser. Prth 'hwrmzd; Prs ^whrmzdy, but as n. pr. of an ordinary man hwlmzdy (KZ); MPrth Prs ^whrmyzd (*whrmzdbg ‘the primordial man’); Paz. Hormezd (Hurmazda and other forms); NP Hurmuzd, Ormuz(d).
4242:vitirtan [wt'ltn'] 1. caus. of vitartan, to cause to pass: dātār han i Zartuxst zx'"arrah tar mätist ārak 6 Zartuxst vitārt the Creator sent Z.’s x“arrah (g. v.) down
```


## [2026-09-05T20:10:14.434Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for p in 61 115 248; do echo \"=== HRN printed $p (leaf $((p+21)))\"; awk -v n=$((p+21+1)) 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -40; done",
 "description": "Horn pages 61,115,248"
}
```


### [2026-09-05T20:10:16.365Z] TOOL RESULT

```
=== HRN printed 61 (leaf 82)
- 61 -
265^" pädäs, pädes (Vis und Rämin) 'Vergeltung', padast,
pädosn,
phlv. pätdah(i)sn {paiti -f dah(i)sn), päz. pädaisn^
pädaän 'Vergeltung'.
Aus dem Pärsismus übernommenes Wort. Vergl.
np. dasen (No. 528).
266. pädiSäh *König'.
ap. "^pati/Säyadiya-; phlv. päta/sä^ bezw. päta/sah
(übersetzt im Kommentar aw. x^<^y(^^^<^' Vermögend,
erlaubt ; Herrscher) ^).
267. päde 'Heerde'^), padehan.
ap. aw. skr. päta- 'beschützt, bewahrt'.
268. pädyäb, pädyaw rituelle Waschung.
aw. paüyäpa- ; phlv. pätt/äp, pOtyapih,
Rituelles Pärsenwort.
269. pädyävend (i:ixnx5?, Is. 1, 31) 'kräftig'.
phlv. pätyavand 'kräftig'.
paiti + l/^««?-, aw. *paityavanU (Part. Praes.).
270. pär 'das vergangene Jahr', pärsal^ parm.
skr. vergl. panit 'im vergangenen Jahre' ; arm. heru
Vergangenes Jahr' (H. No. 167).
kurd. (LW.) par\ af/. parös-; oss. d. fdi% t/aron
'im vorigen Jahre' (277) ; bei. pari, n. pän (293) ; wa;^.
pardy sar. parvus (vergl. gr. nigvöi).
Ap. paruva- 'früher (aw. paurva-) ist schon im
Pehlevi aufgegeben worden; np. pärav alte Frau' ist
nicht belegt.
*) Zu phlv. pata^sa, np. padisäh als t. t. beim Ehesohluss vergl.
West, Pahlavi Texts» 142 Note 10.
2) FR und F J haben als Beleg folgenden Vers des Ferälädl
(so nach Eth6, Morgenländisohe Forschungen, während FR und die
Strassburger Handschrift des FJ Ferälävl, Salemann, SF Feräläri
schreiben), Metrum: Xeflfi
mäde-gävän-t päde-es her yeh
mh^perver huved cn hirmäyün
=== HRN printed 115 (leaf 136)
- 115 —
Zeile 5, 232 Zeile 6, 7), vergl. ;^Mrfw (Vullers), /udn
(FR) ^). Die Zusammenstellung mit aw. geredi,]/(wa-
ist wohl falsch; das Nebeneinandervorkommen von d
(d) und y weist jedenfalls auf einen ursprünglichen
Dental hin, und so wird man auch im PehlevT besser
/adük, yadti lesen.
D.
518. dad 'Gerechtigkeit, Recht', dadistan,
ap. data- 'Gesetz*, {[/^da-, adadü); aw. data- {l^dä-,
daöäiti); phlv. ddt, dätastän, arm. LW. dat, datastan^
hebr. LW. Dl; ai. vergl. dhäman- 'Gesetz' ([^dha-,
dädhati),
LW. kurd. af^'. däd,
519. dädär 'Schöpfer .
aw. datar- 'Schöpfer ; phlv. dätär, päz. dädar, dadär;
ai. dhätär-,
520. (i) dädeti geben', Praes. dth-em, däd 'Gabe', dthis^
jiid.-pers. r^^m (Qiss. Dan., S. 402 Zeile 10 v. u.).
ap. Krfä-, dadütuv geben' ; aw. l/^rfö-, dadqmi 'geben' ;
phlv. dätan; ai. \^da-^ dddäti 'geben'; arm. tcd 'geben'
(H. No. 269).
kurd. däin^ dän 'geben'; afy. lal; oss. d. dädfun,
t. dänftin (240); bei. deag, n. deay (79); »i/n. J/-a?w,
sar. öä-m,
521. {2)däden machen, setzen, in Zusammensetzungen wie
äväz däden 'rufen', ferämös daden 'vergessen' u. v. a. m.
ap. l/^rfä-, adadä 'machen, setzen'; aw. [/'da-, dadaitl
V
') FJ hat folgende zwei Belege:
ö /üdü zed her rüxe ki rö^yl mäh
sijde äred pes i ö der sijdegäh
Mole vi Ma*iiovI (Mctr. Romel).
ez hed'i cer^-t äsiyä-gerdän
^ifsk^ sud der dehän-t hende -/üdü
Süzciil fMetr. Xeflf)
8*
=== HRN printed 248 (leaf 269)
— 248 —
80, 318), Tüchtigkeit*; ai. sündra-, skr. sundani^)
'schön*: phlv. hunar, arm. LW. hnar.
LW. kurd. huner; af;'. bei. (95) hunar.
1/1109. henffäm *Zeit', Ungarn (AM. 213 Zeile 4 v. u.).
ap. *han(/ama' *Zeit*, vergl. aw. aiwLgäma^ 'Winter ;
phlv. hangäm (päz. ögäm), arm. LW. angam *Cbel,
Unglück'.
^1110. henöz noch* (reimt auf iös, 5ö5, y ö-e bei Firdös i
und im Burzönäme, Macan, 1533 Vers 3 v. u., 1583
Vers 17, 2260 Vers 6, 2212 Vers 1), henüz (reimt
auf äz, teinüz, Sadi, Gulistän, Sprenger, 93 Zeile
1 V. u.; 10, 7; Sahn. I, 135 Vers 118)2), ^^^ (gä^n.
I, 67 Vers 97).
Darmes teter. Et. ir. II, 114, 115 ist durchaus
verfehlt.
Zusammenhang mit arm. hanapaz *immer (WZKM.
5, 355, Fr. Müller) ist schon wegen des Bedeutungs-
y Unterschiedes nicht wahrscheinlich.
^1111. {\)hös, hus * Verstand, Klugheit*, huslwär Verständig*.
aw. tisi die beiden Ohren •^) (J. von Fierlinger,
^^J \ KZ. 27, 335); dor. wg, cofatoc, lat. atiri,% lit. austs,
\ ^v^'t got. cmsö etc.; phlv. hös bezw. ös * Verstand*, arm. LW.
' US ^Gedächtnis, Verstand, Acht* (Hübschmann,
No. 237).
Die abgeleitete Bedeutung * Verstand* aus der ur-
sprünglichen 'Ohr' ist erst mittelpersisch.
1112. {2)Jiö8 *Tod* (Vis und Rämin, Seite 82 Vers 13) 4).
aw. aosah' 'Tod'; phlv. hös, hösömand, ahös 'un-
sterblich (Men.).
Eigentum, das Vullers auf diese Weise seinen Büchern einverleibt hat.
Allerdings ist die Klaue des Löwen an sehr vielen Stellen auch ohne
Citat, dai>- Vullers übrigens gewiss nicht mala fide unterlassen hat,
deutlich zu erkennen. Die Lesung uner verbietet wohl die Etymologie.
M Vergl. Jacobi, KZ. 31, 315.
*) Sämmtliche Belege stammen von Herrn Prof. Nöldeke.
^) Ausführliche Angabe der Literatur pro und contra neuerdings
bei Johansson, BB. 18, 25.
*) Stellen aus dem Öähnärae bei Spiegel, Glossar, 368.
```


## [2026-09-05T20:10:34.872Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== dathra\"; grep -n \"dāθra\\|daθra\\|dathra\\|dābra-\" BRT.txt | head -20; echo \"== dathus\"; grep -n \"dāθuš\\|daθuš\\|dābuš\\|dadvāh\\|dad̥vå\" BRT.txt | head -20; echo \"== spento.data\"; grep -n \"spəntō\\.dāta\\|spentö\\.data\\|spəntō-dāta\\|spentodata\" BRT.txt | head -20",
 "description": "Bartholomae greps"
}
```


### [2026-09-05T20:10:34.963Z] TOOL RESULT

```
== dathra
== dathus
== spento.data
```


## [2026-09-05T20:10:36.836Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== uši\"; grep -n \"ušidā\\|uši-dā\\|usi.da\" BRT.txt | head -20; echo \"== HRN 528\"; grep -n \"528\\. \" HRN.txt | head; echo \"== dasen\"; grep -n \"dašen\\|dasen\" HRN.txt | head -10",
 "description": "More greps"
}
```


### [2026-09-05T20:10:36.906Z] TOOL RESULT

```
== uši
6348:•  j.  aäa.x''ä*i^-"  Adj.  'der  das  Behagen, Glück  des  Ala  gewährt' (?),  von  Bergen: gairlm  usi.darmjin    ..    "rim  Y,  1'.  14;  —
8580:AbleiL  iMui-Yhiniitni-;  vgL  iBed.  ai.  udanlya- Adj,  —  «)  NA.  getrennt  und  mit  i  stall  j; s.  F  I  usv-,  IQ  Aiadav-  and  No.  3.  —  'J  In mp.  Schriften  usind,  usindam  genannt;  vgl. SBE.  47.   160.
8721:•  j.  uäi.dam-,  u§i-dain-  tn.  Name  eines Gcbirgs*':  ahmat  haca  garayS  fraoxiyan '0.1  (NS.)')  usi.äar?nd  {i±)  Yt/^.a;  — gairis  yU  °6<j  Yt/p-66;  —  aom  gairuii.. yim  °dam {fuS.y*  usi.darfmm (sd-)Mt.  1.2S.
== HRN 528
4756:528. danen 'Geschenk, Gabe'.
== dasen
2678:np. dasen (No. 528).
```


## [2026-09-05T20:10:42.532Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Schöpfer\" BRT.txt | head -30",
 "description": "Bartholomae Schöpfer"
}
```


### [2026-09-05T20:10:42.578Z] TOOL RESULT

```
3220:der  Spitze  des  Satz(teü)es  stehend  (s.  No. 5,6);  i)  zeitlich 'dann,  darauf,  da';  ''fra- yaire  ayati  .  .  "oa  apare  ayqn  "am  Vor- mittag . .,  dann  (aber)  am  Nachmittag" Aog.5^;  V.  ii.4,  20.4,  N.5J,  F.7,Vt/9. 48;  —  -da  tala  giul  pir>sat  aspm  "da fragte  der  Schöpfer  des  Rinds  das  A."  Y. 2^.2;  — 'da  sl''  ,.  bavaiti  sk>ndö  spaya- %raAyil  (sd)  Y.jo.io;  —  ya%a  va/i  iäd.) ..*''öai^  aaAö  a/ava'V.yi.16.  a)  hinter yäoi:  yet'A  sT  hvar»  nöit  uzttxlyeiti  °oa  . . "wenn  (erst)  die  Sonne  nicht  mehr  auf- geht, dann  . ."  Yt.  6.3.  b)  "oo  .  .  °cit °'6a  'dann  wenn  .  .  dann':  "aa  syäscif pairipataili  'oa  fraistim  vöiynanqm  (sd.) V.  7.3.         a)  anreihend  'und,  und  auch':
4430:•)  Dez.-Jan.  Elg.  'Mon«t  des  namenlosen', d.  i.  des  höchsten  Gottes  (JusTI  ZDMG.  51. Z4S;.  Aw.  da%uiS  '(Monat  des)  Schöpfers',  mp. daiu   (angebl.  den),    np.  dai.   —   S.  noch  unter
6879:•)  {Vgl.  unter  J'arJ'mazdäh.)  Ah.  Ut  maiiUö yasalanqmtit,  ma%Ul</'  bagänäm  Und  alE  solcher der  Schöpfer  aller  guten  Wesen  und  Dinge, auch  der  AmisaSpata  (sd.*)  und  vj-l.  Y.  /p.  8). Sein  ewiger  Gegner  und  Zw illingsb rüder  (Y.  _jo. 3)  ist  AiiraMaiiiyav.  S.  Js.  GltPh.  2.  632,  wo weitre  Litteralur,  und  die  Stelle  <I(^s  GrBd.  bei DsT.  ZA.  2.  305.  Zu  den  obigen  Bemerkungen über  den  (lebrauch  von  'la-  kot  ii.  und  mit 'mazdäi-  (s.  auch  No.  3,  6)  isl  noch  hinzu  zufügen, dass  der  Gebrauch  von  'maafä/i-  allein  im  jAw. häufig  TOrkomml,  im  gAw.  aber  öfter  bciteugt ist  als  der  von  °ra-  allein.  S.  auch  Tiele  Gods- dienst'  2.  40.
12160:.  j.,  g.  tasan-  m.  'Büdner,  Schöpfer',  nur'*  g-  *^s  ä  adv.-artige  Verb,  'auf  solche
12165:der  Schöpfer  des  Rinds  kund  getan  hat" .  •  j.  täta-  Adj.  (fem.  °iä-)  'fliegend,  fallend',
12168:"dein  war  Arm.,  dein  auch  der  Schöpfer  I  strömen  die  fallenden  Wasser  herab"  Yt.
12647:•  j.  daSa-  Adj.  i)  'gebend,  schenkend': Ab  °ls  as»m  upa.raalaydte  (sd.)  yB  drvaite *dalaiti  P.50.       2)  'schaffend;  Schöpfer"
12655:•  j.  daSvah-  :  dadus-,  da'^us-  Adj.  'der geschaffen   hat,   Schöpfer;    schöpferisch':
13299:•  j.,  g.  dätar-  :  dahr-  m.j  j.  däJhri-  f. i)  'der,  die  gibt,  schenkt',  mit  Akk.  der Sache  und  a)  Dat  der  Person:  lumasp  te gaosp?nta  .  ,  'ärö  baxlim  (sd.)  . .  asaone V.  2J.  1  '>;  —  ava.jasa  aridvJ . .  avaahe  . . aridrai  yazimnäi  jaloyanfäi  '>ri/  (NSf.) äyapfym  VL5. 132;  19;  —  JravaSayB  .  . _>'S  °^rf/  (NPt)  v;irjimm  siayaite..  "^ris tiAmSi  voku  x^annS  yS  .  .  Yt  JJ.  24; 24'.  ß)  Gen,  der  Person:  asi (VSf.)  vohOm  i^annö  assqm  narqm Yt.  i-j.  6  *>.  2)  'der  schaffend  hervorbringt, Schöpfer'  von  jiAM.  und  den  AmSp. a)  mit  Gen.  des  Objekts:  aÄura  matda  .  , °tar>gat&anqin  astvaiiiftqm{Stw^iz.)asaum Yt  1. 1  usw.;  —  ahur)m  mazdqm  . .  °tärim vokunqm  dämanqm  Y.  16. 1 ;  —  azim  yö almrö  masdä  azim  yd  'la  vaithvqm  V. 22.  i;  — p»-3sal  zardhusträ  a/iur?m  maz- dqm: *°tar»*vaiikvqm^''  aAura  mazda  V. ig.iT,  verwendet Vyt. i'O ;  —  atmsä  spuita ..  vokunqm  VdrJ  Y.  65. 12;  Vr.  ;7, 12; aiimanam  spmlanqm  .  .  ysi  funti  Snhqm dämanqm  yal  ahurake  mazdä  'tarasca inanxslarasäi  .  .  Yt  ig.  18;  —  azSm  täii "iwä  fraxsnlisA)  auäml  masda  .  .  vispa- nqm  'tänm  Y.  44. 7 ;  —  'tä  artÄJus  andat .  .  hati^y5var?stqm  (sd.)  Y.  ^o.  1 1'*;  —  'tä xratSu^  .  .  räzSng  .  .  sähli  (sd.)  Y.  S'^- 6'*.  ß)  absolut,  von  AhM.:  taha  dim ahurS  mazda  avqn  (sd.)   'ta  Yt  8.  7
13301:Zum  V.  da-.  —  ai.  (zu  l)  dalar-  m.,  (zu  2) dhätär-  m. ;  np.  dädät  'Schöpfer'.  —  Pü. :  dätär ; s.  noch  No.  l ,  3,  4.  —  ')  Pü. :  it  pa  däsr  u// baxl  ist!  ..  ö  öi  i  ..  aiiav.  —  ')  Vgl.  iSt.  Yt. /J.  24  2.  Sl.  —  3)  Hds.  däl3  vaahjn,  aber FB.:  dälär  i  äpä/ihä.  Vgl.  Yt  1.  8  und  No.  6. —  *)  Pü. :  dahi  am  oj^än,  Sü.;  dadämi;  %. No.  5.  —  5)  Pü.:  daie  am  xrat,  Sü.:  dadämi; s.  No.  4.  —  6)  Vgl.  V.  /g.  17  und  No.  3. Pü.:  dätär  u  x'atäi,  erl.:  däm  man  dät.
13427:•  g.  'dämay-,  g.  d^nay-  Adj.  (auch fem.)  'schaffend,  Schöpfer',  a)  absolut  oder b)  mit  t)  Gen.  obj.,  ß)  Akk.;  von  (lUttem, uzw.  i)  von  Mazdäh:  b  a)  at  ^wä  minghl
13428:. .  stöi  . .  z'avhJus  patarSm  (sd.)  mana»hö .  .  haüim  asahya  'mim  ".  .  dass  du  der wahre  Schöpfer  des  Asa  bist"  Y,  j/.  8"; —  kasnä   vanhSui  mazda  'mii  manatahs
13429:93 ;  —  ipints.datäii  'mqn  asavans  yaza- 1  "wer  ist,  o  M.,  der  Schöpfer  des  VM.T maiäe  Vr.  75.  i;    —    vispaca    'ma  (AP.)  '  ¥.44.4"'.  ß)  mazdai  . . yasta  manta..
13442:•  j.dämLdät-Adj.'dieSchÖpfung  schaffend, der  SchöpfuDg  Schöpfer*,  von  AhM.\  ni- sbayemi  ahurö  mazdit  (statt  AS.)  .  .    'tun
13444:•  j.  dämLdäta-'),  dami-däta-  Adj.  (fem. VJ-)  'vom  Schöpfer  (AhM^  geschaffen'" von  Gottheiten:  aurvant»m  ^ws  (näml. Aaom^m)  °Um  Y.  io.  10';  —  mikrtm  .  . 't^/n  YLJO.61;  —  a/i"  srTi-e  'oatte  (VSf.) Yt./7.6o,  61;  —  gsusca  una  -/jYt  74.54.
14392:•  j.  ÖTvar^xätar-  m.  'Bildner,  Schöpfer':
14434:•  j.,  g.  dTWÖr«ätar-  m.  'Bildner,  Schöpfer'  ■> : al  zi  %wa  fsuyatiit^a  västryaica  'ta  iatalü "denn  es  hat  dich  der  Bildner  für  den Viehzüchter  und  Bauern  geschaffen"  Y. 29.  6".  a)  Du.  in  Verbindung  mit payav-  m.  Du.:  payü  (sd.)  "«ra  (AD.)  yä vTspa  %w)r?sats  dämqn  Y.  57.  2; —  *pä- yBc'a  (sd.)   'iara  Y.  42.  2.
16957:i)  Villkommen  heissen',  mit  Gen.'': /rasa  fraya  vahist>tn  ä  ahüm  hnjayanti y?  . .  *sirSus!a  . .  azpmca  Al  bpnjaim  yö  .  . ahurS .  .  uäa  *äa  ti  nun  "'stracks  gehe weiter  zum  Paradies'  (so)  werden  ihn willkommen  heissen  die  Sterne . .  und  (so) werde  ich  ihn  willkommen  heissen,  ich  der Schöpfer  AAM.,  'nach  Wunsch  geh  es  dir hier,  o  Mami'"  V.  7. 52.  2)  'huldigen', mit  Gen.:  bm/ayai  ahurS  .  .  b>njay>n amisä  spMta  yeAha  (sd.)  IbArpff  huraohaya ". .  des  schöngestaltetem  Leib  huldigte j4AM.  . ."  Yt  10.  90;  —  *fraiaintlmca  .  . ye^hh  peurUsca  iftv/ayqn'^  naicisca  aitiha ydssiti  . .  "und  Nachkommenschaft  , .,  der manch  einer  huldigen  und  der  keiner wünschen  soll  .  ."  Y.6'5. 11.
17571:•  g.  fra-xsnl  Inf.  'kennen  zu  lernen': azSm  täiS  'iiwä  fr°  avämJ  mazda  sptnta mainyu  vTspaiiam  dalärpm  "ich  bestrebe mich  so,  dich,  o  M.,  durch  den  heiligen Geist  als  den  Schöpfer  aller  Dinge  kennen zu  lernen"  \.44.T.
19644:•  j.  maiSyÜrya-  m.  Name  der  Gottheit der  fünften  J^eszeit  und  des  an  deren Ende  gefeierten  fünftägigen  Fests*'  (mit dem  letzten,  80.  als  Haupttag):  yiinm sar^tm  aSavamm  asahe  ratüm  "den  kälte- bringenden  M.  .  ."  Vr.  2.  2;  Y.  2.  9;  — 'ryehe  sariaahe  Vr.  J.  a;  A.^.  3;  —  'ryäi Y.  J,  9;  — Jiuxtaheca  na  myasdahe  a^äiti (sd.)  . .  yat  'ryehe  A,^.  11;  —  altaitlm 'ryehe  da%usS  v»n%ra-^nake  "80  [Tage sinds  bis  zum  (Hauptjtagl  des  M.  [im Monat]  des  Schöpfers  [am  Tage]  des  V." A.J.  II.
19658:•  j.  mai8yöi.zar9maya-')  m,  Name  der Gottheit  der  ersten  Jahreszeit  und  des  an deren  Ende  gefeierten  fünftägigen  Fests*> (mit  dem  letzten,  45.  als  Haupttag):  'maem Payanhim  (sd.)  alavansm  alahe  ratäm  Vr. 2.3;  Y.2.9,  A.^,  3;  —  'mayehe  payaahö Vr.  1.  3;  A.3.  a;  —  'mayäi  Y.  J.  9;  — pagiryeheca  na  myazdahe  a&siti  (sd)  .  .yai •mayehe  A.^.  7;  — pan^^a  ^a%war)iafom •mayehe  alaAe  vaAistahe  da%usö  "45  [Tage sin<^  bis  zum  (Haupt)tag]  des  M.  [im Monat]  AV.  [am  Tag]  des  Schöpfers" A.^.?.
19661:I)  NA.  auch  '5iz: ■  j.  maiSyöi-äam-')  m.  Name  der  Gott- heit der  zweiten  Jahreszeit  und  des  an deren  Ende  gefeierten  fünftägigen  Fests*' (mit  dem  letzten,  60.  als  Haupttag):  "Imtim vSstrSMätainlm  (sd.)  asavanim  asahe  ratüm Vr.  2.  3;  Y.  2. 9;  —  'make  V3strd4a(ainyeh4 Vr.i.3;  A.j.3i  —  'ümäi'^  Y./.9;  — bityeht^a  nä  myaxdahe  (^äiti  (sd.)  . .  yat s'fmahe'^  A._j.  8;  —  xivaltim  's>mahe'''> tistryeke  dai:u^S  "60  [Tage  sinds  bis  zum (Haupt)tag]  des  M.  [tm  Monat]  des  Tiitrya [am  Tag]  des  Schöpfers"  A.  j.  8.
22042:—  yäha  drvä  gaom  *visie  (3SPM.)*'  .  . *viile'  Aog.  S2;  F.  Ä*>;  —  vispä  ta  p?nsqs ya'ha  diät  haSi  gam  vtdat  västryS  "nach all  dem  frag  idi,  ob  durch  A!a  der  Kuh teilhaftig  werden  wird  der  Bauer  . ,"  V. 5'-  S*''j  —  ""^  ^^  ""^  ät^ham  zadhranam (Gen,  ab  Obj.)  vindita  '(3SOM.)»  Yt ^7-  S4i  —  '^it  *^  ^^  asraoyanam  tanu- nqm  alahe  (Gen.  als  Obj.)  .  ,  *vthaiti^'> P.  75;  —  yim  dim  va^tät  *tvistaiha  (sd) *vindän?m  ndit  *'ava  yä  *vistas!va  (sva. 'gegen  Entgelt")  N.  t6;  —  s.  noch  i'ldat.', vKat."  a)  mit  Gen.  (statt  Abi.)  der Person  'von  .  .' :  asanS  sasta  draiimnS  .  . vindimnS  dahufs  akuräi  mazdäi  „Steine .  .  von  dem  Schöpfer  AhM.  (sie)  be- kommend" V./5.4.  3)  'Jemandem  (Dat) etwas  erwirken,  verschaffen,  verleihen':  at.. taibyB  xidhnm  vohB  mananha  (als  Subj.) *»S(i'riÄJjÄ(3SKA.)9'  a^byö  jaj«(sd.)  yBi . . Y.J0.8;  —  s.  noch  vindat.-.  4)  'fertig, zu  Stand  bringen,  bereiten':  aAyä  vohs aosO  vida  (sS.)  mananhä  "ihm  bereite, o  VM.,  den  Untergang"  Y.4g.  i;  —  kva ht  aols  vindäma  V.  ig.  46.
22114:mit  ham  i)  'ansichtig  werden,  zu  schauen bekommen':  äaä^ulB  .  ,  raocSbii  (IP.  als Obj.)*'  kqm.vainSimaidl  "möchten  wir des  Schöpfers  Lichträume  zu  sehen  be- kommen" Y.  3Ä  6.  2)  'den  Blick  richten auf—  (Akk.),  sich  wohin  (Adv.)  wenden': ku\a  (sd.)  .  .  masyäka  Aqm.Tainänle?  .  . narym  aiavamm  (näml.  Aam.v)  V.g.  i  f.
26245:'heissen,  lehren',  mit  dopp.  Akk.:  data xratsul . .  razSng  voAb  säAli  mananAa "(es)  lehre  (mich)  der  Schöpfer  der  Geistes- kraft durch  VM.  (seine)  Satzungen"  Y. $0. 6;  —  y^  nä  )mBs  savatshs  pdhs  slisit "der  uns  die  rechten  Wege  des  Vorteils lehren  könnte"  Y.4J.3;  —  süa  nä  aia
27816:(zu)  hoheitsvoll'.  2ar.  wurde  . .  gewahr: 'Die  .  .  Dafva  verabreden  sich  über mein  Verderben'.  Es  erhob  sich  Zar.^ es  machte  sich  auf  Zar.  ungebeugt  .  . Steine  in  der  Hand  haltend , .  (vom  Schöpfer AhM.  sie  bekommend)  ...  Zu  wissen tat  Ärr.  dem/(j1/,:  'Ich  werde  die  daeva- geschaffene  Schöpüing  schlagen  .  .,  bis dass  der  Heiland  geboren  wird  .  .'■  Ihm antwortete -4 J/".:  'Zerstöre  meine  Schöpfung nicht,  o  heiliger  Zar.  Du  bist  der  Sohn I'ourui'aspas.  Von  deiner  Mutter  ward ich  angerufen.  Schwör  ab  die  . .  mazd. Religion,  um  die  Gunst  zu  erlangen,  die erlangte  Vat.  . .'.  Ihm  erwiderte  der  Spit. Zar.:  'Ich  werde  die  .  .  mazd.  Religion nicht  abschwören  .  .'"  V.  jp.  iff.;  -  - Vok.  sehr  häufig,  oft  nur  zeilenflillend: Y. 51.13,  14,  15,  65.10,  71.1,  14,  IS,  Vr. 21.2,  Yt/.9,  10,  34,  35^,  2.11,  13',  4.9, 5.7,  88,  102,  II.  \,  4,  6, 13.3,  9,  ao,  11^46, V.2.3',  43,  j.4a, 4.46,5- 17,  »1,3s,  (J. 37', 7.53,  5.13,14,  lO.iZ,  11.2,  JJ.39,  /7.4, $,  iS.e^t*,  J().i3£*,  21,  34,  H./.2,  4,  7, P.  27,  2S,  2(j,  43,  46,  4$,  FrW.  I.  3,  S.  3, 10.40,   F.  4e;    s.  noch  unten  bei  a  und
```


## [2026-09-05T20:10:43.387Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '4750,4770p' HRN.txt",
 "description": "Horn no.528 dašen"
}
```


### [2026-09-05T20:10:43.428Z] TOOL RESULT

```
zinhar als Amphimacrus bei FirdüsT zu erklären, die
mir jedenfalls (vergl. Indog. Forsch. II, 185) für
iranischen Ursprung des Wortes zu sprechen scheint
(anders Nöldeke, Pers. Stud. II, 46, dessen Erklärung
aus dem aramäischen *inT, wie er selbst zugiebt,
wegen des t Bedenken erregt).
528. danen 'Geschenk, Gabe'.
g. däsn.
phlv. dah(i)Sn ; vergl. padäsn (No. 265*'^'').
529. däy 'Brandmal*, dey.
aw. daya-\ phlv. däy (vd. 15 (48) Gl.); ai. ddha-
'Brand*, skr. ni]däghd' 'Hitze*, Sommer'; lit. dagä 'heisse
Zeit, Sommer.
LW. kurd. afy. däy; bei. däg, n. day (52).
580. {\)ääm 'Haustier, zahmes Tier.
ai. l/"rfam-, d!(^wyci^i"zähmen, zahm sein'; gr. öujiidATjQ
'Stier; lat. domäre; air. dam 'Ochs, Stier ; got. ga-
tamjan, nhd. zahm,
oss. vergl. domun 'zähmen' (108).
phlv. dam 'Geschöpf (aw. däman-) ist im Np. auf-
gegeben.
```


## [2026-09-05T20:11:45.948Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 600 BQT_v1_pages.txt; echo; echo \"=== grep pdf page tags count\"; grep -c \"pdf page\" BQT_v1_pages.txt; echo \"=== v2\"; head -c 300 BQT_v2_pages.txt",
 "description": "Inspect BQT page files"
}
```


### [2026-09-05T20:11:46.005Z] TOOL RESULT

```
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
م و اس مر هر وه او
7 رین خلت ریز یتایب بره ات
لف‌بال ۶۲ .یرک
ا اند کل داي رشب , رمع
فان تا تا
رن 9 3
کرحم تن
اد شش مرا
مو رم | مر
وک رهب اه نات مج
لش
وان روکد ور
۱ و
طراول ؛ | ع اس
چاپ دوم فروردین ۱۳۴۳
با تجدید نظر کامل
بسرمایه کنابفروشی ابن سینا - تپر اناداره کل دک زون.
شماره ۷9 9 ۳
بر
5
‌ ۰ م�
=== grep pdf page tags count
0
=== v2
                                         ‫‪7‬‬

                          ‫رن‪۳‬‬
    ‫نات‬
      ‫ا م‬
              ‫لض‌بال ‪ ۰ ۲۶‬رک‬
‫‪۱‬‬       ‫اسا تعدولیدیارتم و‬
                                     ‫‪7‬�
```


## [2026-09-05T20:11:46.656Z] TOOL CALL #22: Bash

```json
{
 "command": "python3 tools/ref_page.py --help 2>&1 | head -30",
 "description": "ref_page tool help"
}
```


### [2026-09-05T20:11:48.521Z] TOOL RESULT

```
Fetch ONE cited page of a scanned reference, on demand.

    python3 tools/ref_page.py BQT:918          # printed page 918 of Borhan-e Qate'
    python3 tools/ref_page.py IRN:119 --image  # also print the path of the page image
    python3 tools/ref_page.py BQT:918 --pdf-page 375   # override the offset mapping

Looks up the reference in data/verification/sources/refs_online.json
(`scans`: list of {file, first_printed, last_printed, pdf_offset, lang}), renders the
matching PDF page to PNG (for reading with a vision model), OCRs it with tesseract in
the reference's language(s), caches both under
data/verification/sources/refs/ocr/<ABBR>/<printed page>.{png,txt}, and prints the
OCR text. Only the cited page is ever processed — never the whole book.

`pdf_offset` means: pdf page index (1-based) = printed page + pdf_offset.

If the OCR is too poor and you transcribe the relevant passage(s) from the PNG yourself,
save that transcription as <printed page>.vision.txt next to the .txt; from then on this
tool prints the transcription instead of the OCR, so no page is ever read twice.
```


## [2026-09-05T20:11:53.468Z] TOOL CALL #23: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/ 2>/dev/null; echo ---; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/ 2>/dev/null | head -60; echo \"--- MON\"; ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/MON/ 2>/dev/null | head -40",
 "description": "Check OCR cache"
}
```


### [2026-09-05T20:11:53.539Z] TOOL RESULT

```
ARY
BOOK
BQT
HRN
IRN
PLA
SNS
---
0001.png
0001.txt
0049.png
0049.txt
103.vision.txt
1225.png
1225.txt
1225.vision.txt
1275.png
1275.txt
1339.png
1339.txt
1357.png
1357.txt
1382.png
1382.txt
1385.png
1385.txt
1385.vision.txt
1445.png
1445.txt
1445.vision.txt
1452.png
1452.txt
1455.png
1455.txt
1488.png
1488.txt
1803.png
1803.txt
180.png
180.vision.txt
181.png
181.vision.txt
1878.png
1878.txt
1900.png
1900.txt
1908.png
1908.txt
2143.png
2143.txt
220.vision.txt
2222.png
2222.txt
2246.png
2246.txt
2246.vision.txt
2407.png
2407.txt
31.vision.txt
58.vision.txt
70.vision.txt
72.vision.txt
733.png
733.vision.txt
--- MON
```


## [2026-09-05T20:12:08.265Z] TOOL CALL #24: Bash

```json
{
 "command": "for p in 121 289 815 907 2396; do echo \"########## BQT:$p\"; timeout 300 python3 tools/ref_page.py BQT:$p --image 2>&1 | head -60; done",
 "description": "Fetch BQT cited pages"
}
```


### [2026-09-05T20:12:16.000Z] TOOL RESULT

```
########## BQT:121
no scan of BQT covers printed page 121 (see 'scans' in refs_online.json)
########## BQT:289
no scan of BQT covers printed page 289 (see 'scans' in refs_online.json)
########## BQT:815
no scan of BQT covers printed page 815 (see 'scans' in refs_online.json)
########## BQT:907
no scan of BQT covers printed page 907 (see 'scans' in refs_online.json)
########## BQT:2396
(no exact page map; using offset -1917 -> pdf page 479; check the printed number and re-run with --pdf-page if off)
IMAGE: /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BQT/2396.png
REF: BQT:2396  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 479  OCR-lang: fas

هوشیدن : ۹ ۳۹-
فیض واین راکشف وماهده(۱) کوبند 8 دوائی است که آنرا دازی رومی کویند و آن
هوشیدن!۱ ‌- بروژن جوشیدن, بمعئی حبی باشد سرخ برنگه سماق بغدادی و بحریی
امقل کرون باغد چه هوش ۰« نمی عقل م آمده رمان‌الانپار خوانند. عرق‌الشارا نافع است وبول
است ۰ وحیض براند وآنرا هیوفاربقون‌هم میگوبند که
هوفار پقون؟ - بلنت رومی , دام | بند ازحرف اول پای حطی باشد.
(۱) خم۱: مکاشفه .
۱ - بر ساختهٌ فرقةٌ آذرکیوان « فرهنگه دسانیر ص۲۷۷ > از : هوش (۸.م.) بیدن
(پوند مصدری). ۴ - «هوفاربقون, معرب از اوفاربقون بونالیست. وآن سه قسم میباشد,
وهرسه قسم‌را مر مدّل جو است. قسمی را ساق بقدر شبری و زیاده وبرکش مانند ب رکه سداب
وبیار سرخ وگلش سفید وشبیه بگل شب بوودربوی شبیه ببوی صلوبر وتخمش‌سیاه دراز ومدور
مانند جو ومنبتش زمینهای‌سخت... وصنف دویم بزرکترازاول وبرکش بقدرلمناع وپرشعبه وشیها
مستقیم و ساقش سرخ وکلش زرد و تخمش در غلافی مانند خشخاش و با خطوط و دربوی شبیه
برانیانج ... وصنف دیگر که « دازی رومی » عبارت از اوست لباتش بزرکتر ازاول و کوچکتر از
ثالی وبسیار سرخ وپرشاخش ویر کش مانند بر که داب وکلش زرد ودربوی مانند قسم اول ۰
و موّلف اختیارات بدیمی کوید که هوفاربقون شبیه بسماق است » واین قول مشالف قول جمهور
حذافت وبزد حقیر مراد ازنا کسیر هندی قسم‌اخیراست اکرچه اپن‌خزاز وحکمای هند فاربقون
ودازی رومی را یکی داسته آند. ونا کسیرعبارت ازآن واقام اوفر وکامل‌مراد ایشاست.» «تحفهٌ
حکیم موْمن؟ .
5 هودیار - تلفظ قدیم 305087 « فهرست‌ولف» (درتلفظ کنونی ۵9387۲ ) -
«غیار, پهلوی ۵5127 «منای۲۷۹ بقول‌دارمستتراز: هوش(ه.م.) ۳ بار ( ۳ 4219 اوستایی] »
اوستایی ۱-2 ۶*۶۳ ( که [آبکه| هوش میدهد ) « دارمستتر . تتبعات ج ۱ص ددانه
اوستایی بمعنی داده و آفریده است, پس اگر جزو دوم از ريشة مذ کور باشد ۰ این کلمه بمعنی
هوش داده است ( ر4: هزد سنا ص۳۳۱) هرن پی‌ازنقل قول دارمستتردراشتقاق بختیار» هوشیاره
دامیار, شهربار کوبد: «ولی‌طبيعة ازطریق علم الاصوات این فرض غیرهمکن است » بیشتر احتمال
داده میشود که کلمات مذ کور از - داره 1872 #* اشتقاق پافته باشند» چنانکه کلمة پپلوی
321۳842740 در کتیبه‌های پپلوی آنرا تأیید میکند . اما درخصوص اسفندیار پایدگفت که
آن از شکل قدیمتر - داته ۹4218 آمده ودرفارسی «ر» بجای «د» لشته‌است.» «اسشق 6۱۱۲۱
ور4: تعلیقات چپارمقاله نگارنده‌س۹۳؟ . کردی ۳191213۲ (بیدار)؛ 12190227 (باحزم,محتاط).
۴۳ 866 (عوشیار» بصیر) . کیلکی 1180447 «ژابا س۹ ۸ 4* وایز کیلکی 15287 (بیدار)؛
کی که دارای هوش است. باهوش. صیر» بینا :
سنّوده اباشد سر باد سار برین داستان زد یکی هوشیار...
فردوسی طوسی « شاهنامهٌ بخ ج۳ ص*۸ ۰۹۹
+ هودیاری - بافناقدیم ۵910[8۳1ظ (تلنظ کنوبی 0813[2۲1)؛ از: هوغیار(ه م.)
ی (حاسل مصدر, ام معنی) - هشیواری (<.م.) سا هشیاری («.م.) ؛ زب ر کی » خردی ۰
آگاهی, بیداری .
```


## [2026-09-05T20:12:37.975Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3; awk 'BEGIN{RS=\"\\f\"} END{print NR}' BQT_v1_pages.txt; echo \"--- v1 leaf around 121+?\"; awk 'BEGIN{RS=\"\\f\"} NR==130' BQT_v1_pages.txt | head -25",
 "description": "Inspect BQT v1 OCR quality"
}
```


## [2026-09-05T20:12:38.997Z] TOOL CALL #26: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1))\"",
 "description": "BQT scans config"
}
```


### [2026-09-05T20:12:39.807Z] TOOL RESULT

```
777
--- v1 leaf around 121+?
صد و یست و .ك نسخ خطی برهان قاطع
شمارء اوران ۰.۳۵۷ صفحه‌ایی"۲ سطر .طول۳۰ سانتیمتر. عرض۲۰سانتیمتر.
شمارم کتایغانه (1۷) .
۵ - نسغه بخط نستعلیق » در آخر کتاب‌کاتب نام خود را میرزا بابا
ابن میرزا محمد معرفي کرده وسال کتابت‌را سنهٌ ۱۲۵۲ تعبین کرده است .
جلد تیماجی نیم ضر بی .کاغذ فر نگی. واقف سپپسالار. قطم رحلی.
شبارء اوراق ۳۷۲ . صفحه‌ای۲۹ سطر. طول ۵ر ۳۶ سانتیمتر . عرض ۲۲
سانتیمتر . شمارم کتابغانه (۷) .
1 - نسغه‌ای که بسال ۱۲۸۶ مراد علی قمشه‌یی بنا بخواست میرزا
علی| کبر نام از روی نسخه‌ایکه بسال ۱۸۱۸ میلادی در کلکته چاپ سر یی
شده و نسغه آن بیار کمیاب بوده وهست » بخط نسخ نوشته است .
این نخه بسیار مطبوع و دارای یک سر لوح میباشد . صفحات آن
مجدول بطلا ولاجورد وشنجرف واذات آن‌نیز باشنجرف نگاشته شده‌است.
جلد ضربی .کاغذ فر نگی مپره زده . وافف سپپسالار. قطم رحلی.
شمارءٌ اوران ۳۷۷ . صفحه‌ای۳۱ سطر . طول ۵ر۳۱ سانتبمتر. عرض ۲۲
سانتیمتر.شمارم کتا خانه (356) .
۳ کتابخانة مجلس شورای ملی"
۱- نسته برهان بشمارة41۰ (فهرست). تاریخ کتابت ۱۲۶۵(قمری)
خط نتعلیق ؛ هر صفحه ۱ سطر » دارای سر لوح» حساشية دو صفحه اول
تد یب و رصیع » زمینه لاجوردی » قصع رحلی » طول ۳۰سانتیمتر» عرض
1 صانتیمتر » عدهه اوراق ۰ ۰ 6 (شماره ۱2۹
۲- نخه برهان درزمر 2 کتب‌اهدائی [قای‌سید محمد صادن طباطبائی
بشمار۲۲2 ۱۶ .تار یخ کتا بت‌عشر آخررجب ۱۲۰۳ (قمری)»خط نسخ‌خوب‌خوا|نا.
متن لفات وعنوان ها خط قرمز ؛ دارای ۱۰۰۰ صفحه نمام » هر صفحه ۲۵
سطر. 9 سانتیمتر» عرض ۲۱ سانتیمتر. جلد چرمی ۳ .
```


### [2026-09-05T20:12:41.438Z] TOOL RESULT

```
[
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
]
```


## [2026-09-05T20:12:49.376Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in اسفندیار سپنتوداته بغداد; do echo \"=== $w v1\"; grep -n \"$w\" BQT_v1_pages.txt | head -5; done",
 "description": "grep BQT v1 for headwords"
}
```


## [2026-09-05T20:12:50.905Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for w in دادار داشن دهش پاداش; do echo \"=== $w v2\"; grep -c \"$w\" BQT_v2_pages.txt; done; echo; awk 'BEGIN{RS=\"\\f\"} END{print \"v2 leaves:\",NR}' BQT_v2_pages.txt",
 "description": "grep BQT v2"
}
```


### [2026-09-05T20:12:51.099Z] TOOL RESULT

```
=== اسفندیار v1
11016:نام سثار؛ مشتری است - و نام پسر اسفندیار
12181:اسفندیاره بر وزن و معنی آ-نددار
14867:اسفندیار هم هستِ که بسر بهمن باشد .
20103:فرودن » لام برادر اسفندیار است ۴ - و بمعنی
32020:فردوسی طوسی» گفتار رستم باسفندیار .
=== سپنتوداته v1
=== بغداد v1
475:بغداد را ساخت- باید نوشته شده باشد » زیرا در پایان این کتاب در فقره ۱
2044:مر حوماب| نستاس‌ماریا لکر ملی که‌سالهاسا کن بغداد بوده‌درسالع۱۹۱شروع
3194:رد بغدادی ( لغت مردم شداد) : عصیفره .
4523:البغدادی. قاهره. مطیعةا لعصر یه ۱۹۳۹ میلادی (< نغب) .
11142:محیط - و کر آب - و دجلهةٌ بغداد را یز
```


### [2026-09-05T20:12:52.670Z] TOOL RESULT

```
=== دادار v2
8
=== داشن v2
6
=== دهش v2
54
=== پاداش v2
2

v2 leaves: 683
```


## [2026-09-05T20:12:57.572Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '12160,12215p' BQT_v1_pages.txt",
 "description": "BQT v1 esfandiyar context"
}
```


### [2026-09-05T20:12:57.617Z] TOOL RESULT

```
آسفنح است که آمر مرده باشد
اسقنك ۱ - بکر اول وفتح اك‌وسکون
افی و رأبع و دال اسجد ۲ تام ماه دوآزدهم باشد
از سا شسی ۲ و نام الکه‌است درنیشابور -
1 نام داروبی است که ترا حزاراسفتد نیز گویده
و آن نوعی از سداب کوهی باشد و بعربی‌حرمل
" اسقئدار هف ت بر وزن و معت
اسیندارمذ است که‌نام‌امدوازدهم باشدازسال‌شسی.
و للم روژ پنجم آزهر ماه شمسی ۰ و فارسیان این
که مان ابشان متعارفست که چون نام روز با نام
ماه موافق باشد آنروز را عید باید کرد و مبارك
دانت - و نام فرشته است موکل بر ییشپا و
درعتای بو امیر و صاله ماد ایتدان کی میتی
دارد - و بمعثي زمین هم آمده ! ست که سر بی
ارش خوانند ۴ .
اسفند اسشید یک اول وفای دوم»
خردل سفید است ۳
حب‌الرشاد خوانند .
اسفند مد - نم میم ۴
نقطه دار » نام روژسوم (۷) است
و بوسیرن: ۳
اسفندیاره بر وزن و معنی آ-نددار
است که نم پس کشتاسب باشد و او را روبین تن
میکفتند - و بمعنی قدرت حق و لطف یزدان‌هم
هت ورب ماه امفندار و رب روز اسفندار
اسقیك - بر وزن و معنی اسیهید است
کممطلق سیهسالار باشد۷ - ونامی است مخصوس
ملوك فارسیان ۸ .
اسفهبد خوده. بر وزن و معنی
اسیپبد خوره است که باعتقاد اشرافیان فاری شی
ناطقه باشد که آن قوت متکلمة اسانی‌است ٩‏
اسفیجاب - باجيم بروزن استیعاب .نم
3
و۲
اسفیداج باجیم. عمرب اسفیداب است
که زنان برروی مالند و نقاشان و مصوران هم‌کار
قرمایند» وخوردن آ نکشنده نود تا سفیداب
تر
استبی‌ار ‏ مخفف اسفیددار (۳) است
که درخت یده‌باشد وبعربی غرب خوانند ۰ وبصنی
کویند توعی از یده است ٩*‏
اسفیف دشت « اسفید معلوم » و دا
ایجد عفتوح‌وشین ونای فرشت فت‌سا کن» نام‌قر به‌ایست
از توایع صفاحان .
اسفیوش ع بر وزن و معنیاسپیوش‌است
که بزر قطونا باشد . و عربان بقلةٌ با رکه
هه
)۱( چش : دوم . )۱( چش : سیم . )۳( چش: اسفیدیار .
۸ ملوکک طبرستان . صحیح است
خوره - ۱۰ رکه : اسیمدار .
ب وله : اسیندبار.
اسیپیث .
هی کته ۵ تاو 9 انسوفا ء قاضی ترسابانرا کویند وشخصی‌رانیز گویند
.از ابشان که بجهت رباشت خودرا بزنجیر :بندد.
گود اين لت عربی است
اسقلطسی ب سکن اوله وی کی
```


## [2026-09-05T20:13:18.564Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3226,3260p' POK_01.txt",
 "description": "Pokorny do- continuation p.225"
}
```


### [2026-09-05T20:13:18.597Z] TOOL RESULT

```
do-U'  liegt  vor  in  ai.  dävdne  ,zu  geben^  (auch  Perf.  daddu  ,habe  ge- geben'), av.  dävöi  ,7.\i  geben',  kypr.  övfavoi  ,er  möge  geben^,  Inf.  dofsvai (über  ark.  Partiz.  diTtv-döaq  s.  Schwyzer  Gr.  Gr.  I  745  f.),  kontrahiert hom.-att.  dovvai]
lat.  duim,  duls  usw.  ,dem,  des',  Fut.  II  -duö,  enthalten  einen  Aorist- stamm *du-  aus  *(Zow-;  duim  ist  aus  Optat.  *-c?owlm  in  den  Kompositis entstanden  (prö-duint  aus   *prö-douint,  usw.),  dann  auch   bei   Kompositis
15
226
von  *dhe- :  per-dmm,  usw.  Zum  ital.  Optativ  *doulm  trat  wohl  erst  sekj dar  im  Umbr.  und  Fal.  ein  Präsens  *douiö  in  fal.  doviad  ,möge  gewähx (es  scheint  daher  lat.  duam  usw.  in  Kompositis  geschwächtes  *doviä7n] sein),     umbr.     pur-dovitUj     pur-tuvitu,    -tuetu    ^porricito^^    P'^'^ttivi^ jporricies''^  umhr.  pu^^ditom  (*-d(o)täto7n)  ^iporrectum', pur tiius  {*d(^o)umf\ ^porrexeris',  purtifile  ,*porricibilem^,   aus  synkopiertem  *por-d[o]ui-  x^ Wandel  von  du  zu  d]  in  purdovitu  Imper.  wurde  die  Synkope  durch  de Indik.  *pör-dovU  gehindert;
lit.   daviau   ^ich   gab^^  dovanä  f.  ^Gabe^,   lett.  ddvana  f.  ,Gabe',  Itera^ dävdtj    dävindt  ^anbieten^    schenken^    aksl.    -davati   ,verteilen^    (eine Muster  formen  für  die  Iterative  auf  -vati).
Über  as.  tioitliön  ^gewähren^  usw.  s.  unter  2.  den-  , freundlich  gewähret
WP.  I  814f£.,  WH.  I  266,  360 ff.,  371  f.,  861,  Schwyzer  Gr.  Gr.  I  686 V 722,  741,  794,  806  ff.,  Trautmann  56  ff.
dous-  ,Arm^
Ai.  dös-  n.  (m.).  Gen.  dosndk  ,Vorderarm,  Arm,  unterer  Teil  des  Vorder-  •" fußes  bei  Tieren^,  av.  daos-  m.  ,Oberarm,  Schulter^,  npers.  dös  ,Schulter^» air.  doe    {^dous-nt-s),   Gen.    doat   ,Arm^;    lett.  pa-duse    (tiefstufig)   ,Achsel''-vl höhle;  Busen  des  Kleides^;  sXoyqxi.  päzduha,  päzdiha  neben  päzuha,  päziha  '" ,Achselhöhle^,   und    mit    demselben   c2-Verlust   (ein  Erklärungsversuch  bei Berneker  233  f.)  abg.  usw.  pazucha  ,Y,6l7rog'.
WP.  I  782,  Trautmann  64.
dre-  i.drQ-,  erweitert  dr-^m-  ,schlafen^
Ai.  drdti,  dräya-tij  -te  ,schläft^,  ni-drä  ,Schlaf^;  dazu  tiefstufig  ni-drita-y^ ,schlafend,  eingeschlafen';  '»A;
arm.  tartam  ,langsam,  schläfrig^  {*der-d-,  Pedersen  KZ.  39,  416);       <^'
gr.  hom.  Aor.  edgaO^ov  {*e-dr-dh-om)j  jünger  edaqd-ov  ,schlief^,  sekundär ■naTadaQS-dvcü  ,schlafe  ein^;
lat.  dormiö  ,schlafe,  schlummere^  (*c?2'7m-uö)  ;
slav.  *dremiö  ,schlummere^  in  ksl.  dremlju  drimati  ,schlummern',  serb.-| drijemljem  drijemati  ,Schlaflust  haben^,  usw.
Über   die   formalen  Verhältnisse  s.  EM.  284,  zur  -em-Erweiterung  auch Pedersen  Groupement  22.
WP.  I  821,  WH.  I  372,  Trautmann  60.
dregh-   ,unwillig,  verdrossen^,  oder  vielleicht  ursprünglicher  ,schlaff,  zähe^ sein^?  -^
Got.    trigo   ,Trauer,  Widerwille^,   anord.    tregi    m.    ,Trauer,    Hindernis'/^ tregr  ,un willig,  ungeneigt^,  treginn  ,betrübt^,  ags.  trega  m.  ,Trauer,  Leiden',  _
^s^-
227
treqo  m.  ^Schmerz^,,  tregan  (nur  Inf.)  mit  Dat.  ^leid  sein^,  mndl.  tregen ficu  Hut  verlieren^  auord.  trega  =  ags.  tregian  ,betrüben^;  vgl.  mit  einer '-olil  alten  konkreten  Bed.  ^zähe,  zähe  haftend'  norw.  radartl.  treg  auch au'=;dauernd^  fest^^  trege  ,zähe  Faser^  Sehne^  harte  Haut^,  ischwed.  trägen 'unermüdlich^;  dehnstufig-  ahd.  trägi  ^träge,  langsam,  verdrossen'^  as.  trag 'schlecht'^  ags.  trüg  f.  ,Leiden^  Übel';  as.  ahd.  trägl  f.  ^Trägheit,  Verdruß'; lit.  dryz-tü,  drizau,  drizti  ^matt^  schlaff  werden'  (Büga  Kalba  ir.  s.  219)^ drizinti  ^schlaff  machen';  zum  lit.  ri  vgl.  Hirt  Idg.  Gr.  II  83. Wr.  I  ^21  f.;  Persson  Beitr.  46  f.
dumh-  (-hh?)  ^penis^  Schwanz',  vielleicht  eigentlich  ^Stab'.
Av.  duma-  m.  ^Schwanz',  npers.  durrij  dumb  (*dum(}i)ma-)j  ahd.  zumpfo penis';  mhd.  zum2J>f{e),  zumpfelin  (Sütterlin  IF.  4,  93);  dazu  vielleicht  av. dumna-  n.  ;Hand  (?)'  (*dumbna-),  s.  Scheftelowitz  IF.  33,  142  mit  zahl- reichen Parallelen  für  die  Bed.-Entw.  ^Stange^  Stab  —  penis,  Schwanz' und  ,Stab  —  Arm,  Hand'.  Wohl  zu  mnd.  timpe  ;Spitze_,  Gipfel',  ags. atiinplian  ,mit  Nägeln  versehen',  nasal.  Form  von  germ.  *tippa  ,Zipfel' in  engl,  tip  _,Spitze',  mhd.  zipf[el)]  germ.  *tuppa-  ,Zopf'  in  anord.  toppr ds.,  ags.  topp  m.  ,Gipfel',  mhd.  zopf  ^Zopf,  Ende  eines  Dinges',  mit  bb: mnd.  tobbe,  tubbe  , Zapfen',  vgl.  Xqü.  duba  ,aufgestellte  Garbe';  germ. *tappan  ,Zapfen'  in  ags.  tssppa  m.  (engl,  tap)^  mnd.  tappe  m.,  ahd.  zapho, mhd.  zapfe  m.  Offenbar  ,mot  populaire'  mit  intensiver  Konsonantenschär- fung,  Nasalierung  und  Vokalwechsel  a:i:ii'^  vgl.  oben  S.  221  drop- :  drip- : drup-.    S.  auch  oben  S.  177.
WP.  I  816,  Fick  III  155,  164,  168,  Petersson  Heterokl.  70  f.
cfus-  ,übel,  miß-'  als  1.  Kompositionsglied.
Ai.  dus-,  dur-,  av.  diLS-,  duz-  ,miß-,  übel',  arm.  t-  ,un-',  gr.  ovo-  ,miß-, übel',  lat.  in  difficilis  ,schwierig',  air.  do-j  du-  ds.  (lenierend  nach  dem Vorbild  von  so-,  su-),  got.  tuz-  (in  tuz-werjan  ,zweifeln'),  anord.  ags.  tor-j ahd.  2;wr-  ,un-',  slav.  in  abg-.  d^zdh  {^duz-djus  ^schlechter  Himmel'  ==)  ,Regen', russ.  dozdh,  poln.  deszcz^  aöech.  desc.  Gen.  dsce  und  analogisch  deH4.  Zu- sammenhang mit  deus-  ,ermangeln'  ist  sehr  wahrscheinlich.
Erst  ind.  aus  dus-  entwickelt  ist  düsyati  ,verdirbt,  wird  schlecht', dusta-  ,verdorben,  schlecht',  düsdyati  ,verdirbt,  versehrt'.
WP.  I  816,  E.  Fraenkel  M^  Pedersen  453.
duei-  ,fürchten'.
Av.  dvaed-ä  ,Bedrohung'j
arm.  erkntim  ,ich  fürchte',  erkiul  ,Furcht'  (Anlaut  wie  in  erku  ,zwei' '.*diLöu  Meillet  MSL.  8,  235);
16*
```


## [2026-09-05T20:13:19.569Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS dasr/dasn\"; grep -n \"dās\\|dāšn\\|dahišn\\|dātan\" SNS.txt | head -20; echo \"=== SNS pages\"; grep -n \"dās\\|dāšn\" SNS_pages.txt | head -10",
 "description": "SNS greps"
}
```


### [2026-09-05T20:13:19.773Z] TOOL RESULT

```
=== SNS dasr/dasn
=== SNS pages
```


## [2026-09-05T20:13:28.051Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3208,3226p' POK_01.txt",
 "description": "Pokorny do- middle section"
}
```


### [2026-09-05T20:13:28.101Z] TOOL RESULT

```
hierher    vielleicht   trotz    VYH.  I  193   lat.  ce-dö   .siih    her!^  PL    cette
>xs'
aus
^ce-d9te  (:gr.  Sörs);
lit.  duomi  (heute  sekundär  duodu,  lett.  duodu,  neugebildet  zum  alit. Ipv.  duodi  aus  "^dö-dhi-,  ostlit.  düomu),  2.  Sg.  düosi,  3.  Sg.  düost{i)  ,^\hi', apr.  däst  ds._,  beruhen  nach  Kofinek  Listy  filol.  65^  445  und  Szemerenyi Et.  Slav.  Roum.  1,  7  ff.  (vgl.  E.  Fraenkel  Balt.  Sprachw.  11  f.)  nicht  auf alter  Reduplikation  (angebl.  *dö-dd-mi,  bsl.  "^dödmi,  3.  Sg.  *dö-dd-ü,  bsl. *dödti  >  *dösti),  sondern  auf  unreduplizierter  athemat.  Flexion  (*dömi, PL  *ddmös);  lit.  düosti,  abg.  dast^  sind  Nachahmungen  von  lit.  hti  ,ißt' usw.,  die  neben  lit.  *e(d)mij  abg.  janib  (aus  ^ed-m-)  liegen^,  wo  das  d  der Wurzel  als  suffixal  empfunden  wurde;  zum  Fut.  lit.  duosiii  s.  oben  S.  223.
Dasselbe  würde  gelten  von  aksl.  daim  ,ich  werde  geben*,  3.  PL  dadeti (nach  jadet^  usw.);  aksl.  dazda  ,Gabe^  ist  Analogiebildung  nach  *edja ,Essen',  wo  das  d  wiederum  als  Formans  betrachtet  wurde.
Infin.  lit.  düoti,  lett.  duot,  apr.  dät  {^dö-tl-)  =  aksl.  dati^  serb.  däti, russ.  dath.  ?
Zum  Prät.  lit.  daviaü,  lett.  devu  ,gab^  s.  unten.  '
225
partiz.  *dö-na-  in  Siksl.  pre-dam,  serb.  dän,  cech.  ddn,  klr.  ddnyj  , gegeben' , *dö-tcL-  ds.  in  apr.  däts,  lit.  düotas,  lett,  cZwo^s;  einzelsprachl.  Neuerungen <;iiul  serb.  dial.  dät,  cech.  c^a^^;  dazu  lit.  duotina  ;,mannbar^^  russ.-ksl. jwdatbm,  russ.  poddtnyj  .freigebig^;  Supin.  *dötun  ,zu  geben^  in  apr.  daton (lüfin.);  lit.  c?MO%  aksl.  ohdah,  sloven.  dat,  vgl.  slav.  *datz-H  in  sloven. Jodätek,  poln.  dodatek,  russ.  doddtok  , Zugabe^;
hitt.  c?ä-  ,nehmen^^  1.  Sg.  da-ah-hi  {dahhi),  3.  Sg.  c?a-a-i  (c?äi),  wird  von Pedersen  (Mursilis  68)  und  Kretschmer  (Glotta  19^  207)  hierher  gestellt /treben^  —  :?^ür  sich  geben^  —  ^nehmen^);  dagegen  Couvreur  ^  206 ff.
Xominalbildungen:  ai.  dätar-j  dätdr-  ^Geber^^  gr.  (Jwtw^,  dojTrjo  ds., schwachstufig  (JottJo,  öÖTSiga,  lat.  cZa^o?-,  datrix.  —  Ai.  dätrd-,  av.  dä^ra- ji.  ^Geschenk^.
*dö-tel-  in  aksl.  dateljh  (*dö-tel-iu-)  ^Geber*^^  cech.  udatel  ^Angeber^,  russ. ddteh  ^Geber'.
Ai.  *däti'  ^Schenkung,  Gabe^  in  däti-vära-  jgern  verteilend,  freigebig^, havya-däti-  ,die  Opfergabe  besorgend,  das  Darbringen  des  Opfers^,  av. däiti-  , Geben,  Schenken,  Gewährung^,  gr.  ö&xig  Hes.  (und  kons.  St.  *dö-t- in  öd)g)  ,Gabe^,  Jcoai-d-sog,  -q)Q0)v^  lat.  cZös,  -tis  ,Mitgift^,  lit.  Inf.  düoti: slav.  *dath  ,Gabe^  (z.  B.  in  aksl.  hlagodath  ,X(xQig',  russ.  pödath  ,Steuer^), Inf.  dati]  schwachstufig  ai.  diti-h,  gr.  ddaiq  ,Gabe^,  lat.  dati-ö,  -tiönis  (alt *-tlnes)  ,das  Schenken^  (Suffix  wie  in  gr.  öcorivT]  ,Gabe^);  mit  Vokalschwund in  Enklise  ai.  bhdga-tti-  ,Glücksgabe^
Ai.  däna-  n.  ,Geschenk^  (substantiviertes  -720-Partiz.)  =  lat.  dönum,  osk. usw.  dumim  ds.  (dtiunated  jdönRvit') ;  cymr.  daicn  ds.,  air.  dän  m.  ,donum, ars,  ingenium  (Begabung)',  vgl.  slav.  *dam-ki  in  serb.  ddnak  , Abgabe, Steuer^  usw.  und  den  -m-St.  aksl.  danh  , Abgabe,  ZolF,  lit.  duönis  ,Gabe^; schwachstufig  alb.  dhene  ,gegeben^,  f.  ,Gabe,  Abgabe^,  geg.  dhdne]
gr.  ScüQOv  , Geschenk^  (-ro-  in  pass.  Geltung,  vgl.  z.  B.  clä-ru-s),  aksl. dem  ,Gabe^  (m.  wie  ^damk-h),  arm.  tur  ds.;
ai.  däyd-  ,gebend^,  däyd-  m.  ,Geschenk^,  apreuß.  däian  Akk.  ,Gabe^, serb.  pro-daja  ,Verkauf^  (usw.,  Berneker  176).
Als  2.  Kompositionsglied  ai.  -da-  z.  B.  in  asvada-  ,Rosse  schenkend^, slav.  mit  Überführung  in  die  o-Dekl.,  z.  B.  russ.  dial.  pö-dy  PI.  , Abgaben, Steuern^,  serb.  prt-d  ,Draufgabe  beim  Tausch^;  lit.  priedas  , Zugabe,  Zulage^
do-U'  liegt  vor  in  ai.  dävdne  ,zu  geben^  (auch  Perf.  daddu  ,habe  ge- geben'), av.  dävöi  ,7.\i  geben',  kypr.  övfavoi  ,er  möge  geben^,  Inf.  dofsvai (über  ark.  Partiz.  diTtv-döaq  s.  Schwyzer  Gr.  Gr.  I  745  f.),  kontrahiert hom.-att.  dovvai]
```


## [2026-09-05T20:14:14.812Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SNS sample\"; grep -n \"dāt\\|dās\\|dahi\" SNS.txt | head -10; echo \"=== SNS cache\"; ls ocr/SNS | head; echo \"=== FSF داشن دهش\"; grep -n \"داشن\\|دهش\\|پاداش\" FSF_pages.txt | head -10",
 "description": "SNS and FSF greps"
}
```


### [2026-09-05T20:14:14.883Z] TOOL RESULT

```
=== SNS sample
1134:The Bundahishn, being a Facsimile of the 
5381:\*i*j* jx» j'*£*iL-S:avizIdar dahisnan: v^^O i-i^Cf 
15864:*"" ta, -Vi» T ooH*:vehdahiSnani KHUho^, 
16196:W** 'A/IS* VV^ W«A ^JojIj,^ ; dahisn :»£d»rO 
16197:.yjb^g :be dahisn: njon^ ^), i^ /To ^ if/> Y ^ . Y 
16198:•O^'^^W :nS dahisn: ncoifj^ J^ >r/VT tf .^fc^ 
16316:.^...aiiy.a-J*.*: dahisn Omand: jrf«c- wcu-o 
16698:<unj^-^).j > i^. u li - >T,«d iT,jiftj :dahisn: |*0-»-<t> 
16699:»«V> T (l) :dahisnan: t^tTO'-O \\f\»*S •f\f<S 
16701:£^^j*i v \>>>i»U^o^ T *0 , j^ ,A rf J j ;i :avizldar dahisnan: 
=== SNS cache
14.vision.txt
6.vision.txt
=== FSF داشن دهش
173:‫باد سرد‪-‬نیکی دهش ‪-‬نیکی گمان ‪-‬از در ‪-‬خیره پرتاب _گذشته ز من‪-‬ز توبگذرد‬
1690: ‫(‪)۵-۲۷۲۰-۹۲۶‬‬                                     ‫جز آویختن نیست پاداش این‬
2235:   ‫بند ‪ ۲۱51705۵‬یوستی بندهش ص ‪:)۳۶‬‬                         ‫ازیرا سرت ز آسمان برتر است‬
2840: ‫بر پاداشتن» از جای جنباندن و جهانیدن‪.‬‬           ‫ازینسان که هستی بپنداشتم‬
2883:          ‫نماند برین خاک خونخوار کس‬                             ‫‪( 156‬یوستی بندهش ‪)۰۸‬‬
3357:             ‫بازخواست‪ .‬سزای گناه پاداش‪:‬‬                 ‫(‪)۵-۳۲-۹۴۲‬‬
3371:                       ‫رسستم پس از‬                           ‫بحر و ابرست روز پاداشن‬
3381: ‫(‪)۸۸۱-۷۱۸-‬‬                                     ‫چه پاداش و چه بادافره نمودم‬
4221:                   ‫‪۳‬۔بخشندگی» داد و دهش‪:‬‬      ‫)‪(0-4۷-۸1۲1‬‬
4488:             ‫ز نیکی دهش برتوبادافرین‬                        ‫موبد به اردشیر بابکان گوید‪:‬‬
```


## [2026-09-05T20:14:17.230Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==249' KLN_1966.txt | grep -n -i \"dolman\" ; echo \"=== grep dolman KLN\"; grep -n -i \"dolman\" KLN_1966.txt | head; echo \"=== SKT\"; grep -n -i \"dolman\" SKT.txt | head; echo \"=== LKT\"; grep -n -i \"dolman\\|dolama\\|dolmak\" LKT.txt | head",
 "description": "Klein/Skeat/Lokotsch dolman"
}
```


### [2026-09-05T20:14:19.008Z] TOOL RESULT

```
=== grep dolman KLN
12018:dolman,  n.,  a  long  Turkish  robe;  a  kind  of  jacket worn  by  hussars.  —  F.,  fr.  G.  Dolman,  fr.  Hung. dolmany,  fr.  Turk,  dolaman,  the  red  cloak  of  the Janizaries.
=== SKT
23993:Dolman,  a  monument  of, stones,  with  a  third  across  tli X^andC.)     Bret,  dolmrm^  Kt. Legoiiidcc. » Bret.    1/0/.    al< table  (from  L.  tahuia) ;  and  1
=== LKT
1362:'Roter  Tuchmantel,  den  die  Janitscharen als  Paradeanzug  trugen';  hieraus  rum. dulama  'langes  Unterkleid,  Damenober- kleid',  Abltg.  dulämifä;  bulg.  dolama 'langes  Oberkleid',  serb.  dolama  'langes Unterkleid',  russ.  doloman,  dolman,  kl- russ.  doloman,  poln.  dolman  'kurzer Husarenmantel',  öech.  doloman,  dolman 'ungarischer  Pelzrock';  dtsch.  Dohna)}, frz.  doliman,  dolman  'Husarenjacke'. [Gorjajew  104.  Bern  SlEtAVb  206.  Devic DEt  104.
5769:Dalai-Lama  1302 DriZ/e*-  j.  468 Da//os  j.  468 Damast  476 damaszieren  476 Damesinel  1871 Da?«  504 dawnen  j.  505 St.  482 Denebola  St.  482 Derwisch  496 Dey  460 dibbern  j.  514 D//f<eZ  j.  2068 D/f/(27«/  521 Diwan  526 Doc/j^s  j.  1984 Doto  j.  1984 Dollinger  j.  2002 Dolman  530 Dolmetsch(er)  2078 I>oM/"es  j.  1978
7645:damascena  476 damaszka  476 daraban  490 demeszek  476 dervisz  496 rfiw;  509 dolman  530 rfrrtft  490 draganek  2034 duchan  539 dyma  521 tf2/!<j%Ä:  2076 dziryt  681 dzuma  445
```


## [2026-09-05T20:14:29.147Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1355,1365p' LKT.txt; echo \"=== klein leaf\"; awk 'BEGIN{RS=\"\\f\"}{n++; if (index($0,\"dolman,  n.,  a  long  Turkish\")>0) print \"leaf(1-based):\",n}' KLN_1966.txt",
 "description": "Lokotsch dolaman entry + Klein leaf"
}
```


## [2026-09-05T20:14:30.638Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== MON دلمه\"; grep -n \"دلمه\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt 2>/dev/null | head -10",
 "description": "Mo'in dolme"
}
```


### [2026-09-05T20:14:31.121Z] TOOL RESULT

```
527.  Tk.  dizgiii:
'Zaum,  Zügel'  [vom  Stamme  tir,  tiz,  s. hier  Nr.  522] ;  hieraus  rum.  diaghin, desghin  'Kapriole  (des  Pferdes)',  bulg. serb.  dizgin,  serb.  dizden  'Zügel'.  [Bern SlEtWb  203.
528.  Tk.  dojum:
'Großer  Haufe'  [vom  Stamme  tok,  toj 'dicht,  fest,  volP  Vämbery  TktEtWb S.  179,  Nr.  1931];  hieraus  rum.  duium 'Haufe,  großer  Auflauf.
529.  Pers.  döläb:
'Schrank',  ebenso  ik.dolap;  hieraus  rum. dulap  'Schrank,  Schaukel'  [das  letztere nach  Sain  51],  fig.  'Intrige'  [nach  Löbel EITAP  40],  Abltg.  duläpärie,  duläpior; bulg.  dulap  'Schrank'.
530.  Tk.  dolaina:
'Roter  Tuchmantel,  den  die  Janitscharen als  Paradeanzug  trugen';  hieraus  rum. dulama  'langes  Unterkleid,  Damenober- kleid',  Abltg.  dulämifä;  bulg.  dolama 'langes  Oberkleid',  serb.  dolama  'langes Unterkleid',  russ.  doloman,  dolman,  kl- russ.  doloman,  poln.  dolman  'kurzer Husarenmantel',  öech.  doloman,  dolman 'ungarischer  Pelzrock';  dtsch.  Dohna)}, frz.  doliman,  dolman  'Husarenjacke'. [Gorjajew  104.  Bern  SlEtAVb  206.  Devic DEt  104.
531.  Tk.  doldur-:
Doldurmak  'füllen'  ['voll  machen',  Kau-
43
=== klein leaf
leaf(1-based): 260
```


### [2026-09-05T20:14:31.182Z] TOOL RESULT

```
=== MON دلمه
MON_part2.txt:25256:می‌کننكد. از اين برگ‌ها ترشی و دلمه و غیره 
MON_part2.txt:25330:دلمه (00۱۳20-6-«۱2(امر.) خوراکی 
MON_part2.txt:39096:۳9 لسبتّه ا منعقد» دلمه: لخت خون. 
MON_part2.txt:39109:لخته: (۵-)۱3۱۸ (ص.) سته» منعقد؛ دلمه. 
MON_part2.txt:39305:تهیه کنند و آن چون سرد شود دلمه گردد و 
MON_part2.txt:65258:ممازحت: («ع2)ادلمه۱۵0۱8 [ع. ممازجه ] 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:25256:می‌کننكد. از اين برگ‌ها ترشی و دلمه و غیره 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:25330:دلمه (00۱۳20-6-«۱2(امر.) خوراکی 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:39096:۳9 لسبتّه ا منعقد» دلمه: لخت خون. 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:39109:لخته: (۵-)۱3۱۸ (ص.) سته» منعقد؛ دلمه.
```


## [2026-09-05T20:14:38.076Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25325,25340p' MON_part2.txt",
 "description": "Mo'in dolme entry context"
}
```


### [2026-09-05T20:14:38.124Z] TOOL RESULT

```
کلمچی: 1« [ع. تر. - کلمه + چی] 
(ص‌مر. آمر.) مترجم؛ ترجمان (در تنگسوق 
نامه ایلخانی رشیدالدین فضل‌االه آمده. 
مبنوی مدات ۹:۳ ۱). 

دلمه (00۱۳20-6-«۱2(امر.) خوراکی 
است. طریقةٌ آن -مقداری از میان کلم برگی 
را بیرون آورند و کلم را در دیگک آب 
گذارند چون جوش زند برمی‌دارند و 
گوشت قیمةٌ خرد شده را با جعفری خرد 
کرده بجای مغز کلم که بیرون آورده‌اند» 
می‌ریزند و اطرافش را می‌بندند و در ته 
دیگ پیاز حلقه حلقه و آبگوشت می‌ریزند 
و می پر ند, 
کلمرغ: 1۵1-0 (امر.) (جاد.) نوعی 
کرکس. که سروی پر ندارد.
```


## [2026-09-05T20:14:39.493Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==260' KLN_1966.txt | tr ' ' '\\n' | grep -n \"^4[0-9][0-9]$\\|^5[0-9][0-9]$\" | head",
 "description": "Find printed page numbers on Klein leaf 260"
}
```


### [2026-09-05T20:14:41.082Z] TOOL RESULT

```
611:473
2297:474
2298:475
```


## [2026-09-05T20:14:52.292Z] TOOL CALL #39: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-05T20:14:52.333Z] TOOL RESULT

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


## [2026-09-05T20:15:00.803Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"To give\\.\" AHD_watkins1985.txt | head; echo ===; grep -no \"do-\\. To give[^]]*\\]\" AHD_watkins1985.txt | head -c 4000",
 "description": "AHD Watkins do- root"
}
```


### [2026-09-05T20:15:00.851Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-05T20:15:03.326Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"To give\" AHD_watkins1985.txt | head -10",
 "description": "AHD Watkins To give"
}
```


### [2026-09-05T20:15:03.439Z] TOOL RESULT

```
268:ai-1, To give, allot. 1. Suffixed form “ai-t-yd in Greek aitia, cause, responsibility: ETIOLOGY. 2. Suffixed form *ai-td- in Greek diaitan, to decide, lead one’s life: DIET!. [Pok. 3. ai- 10.]
489:*klai-ni-, bright, pure, in: a. Old English cléne, pure, clean: CLEAN; b. Old English clénsian, to purify, cleanse: CLEANSE. 2. Extended and suffixed zero-grade form *glo-nd in Greek gléné, eyeball: EUGLENA. [Pok. gel- 366.] gel-3. Cold; to freeze. 1. Germanic *kaliz, coldness, in Old English c(iJele, chill: CHILL. 2. Germanic *kaldaz, cold, in Old English ceald, cold: COLD. 3. Germanic *kédl-, cool, in: a. Old English cdl, cold, cool: cooL; b. Germanic *koéljan, to cool, in Old English célan, to cool: KEEL’. 4. Suffixed form *gel-d- in Latin geldre, to freeze: GELA- TIN, GELATION, JELLY; CONGEAL. 5. Suffixed form *gel-u- in Latin gelu, frost, cold: GELID. 6. Probably suffixed zero-grade form *gl-k- in Latin glaciés, ice: GLACE, GLACIAL, GLACIATE, GLACIER, GLACIS. [Pok. 3. gel()- 365.] gembh-. Tooth, nail. I. Suffixed o-grade form *gombh-o-. 1. Germanic *kambaz, comb, in: a. Old English camb, comb: COMB, KAME; b. Old High German kamb, comb: CAM; c. Germanic denominative *kambjan, to comb, in Old English cemban, to comb: OAKUM, UNKEMPT. 2. Greek gomphos, tooth, peg, bolt: GoMPHosIS. II. Per- haps Germanic *kimb- in Old English cim-, cimb-, rim (only in compounds): CHIME?. III. Possibly suffixed form *gembh-ma in Latin gemma, bud, hence gem: GEM, GEMMA, GEMMATE, GEMMULE. [Pok. gembh- 369.] geme-. To marry. Suffixed zero-grade form “gmoa-o- in Greek gamos, marriage: GAMETE, GAMO-, -GAMOUS, -GAMY; GAMOSEPALOUS. [Pok. gem/(e)- 369.] gen-. To compress into a ball. Hypothetical Indo-Euro- pean base of a range of Germanic words referring to compact, knobby bodies and projections, sharp blows. 1. Germanic *kn-a-pp- in: a. Old English cnzpp, hilltop: KNAP?; b. Middle Dutch cnoppen, to snap, and Low German knappen, to snap, hence “to have a bite,” akin to Middle English knappen, to strike sharply, snap: KNAP!; KNAPSACK; C. Old English cnop, knob: KNop. 2. Ger- manic *kn-a-k- in Middle High German knacken, to crack; KNACKWURST. 3. Germanic *kn-a-r- in: a. Norwe- gian knart, knot in wood, akin to the source of Middle English knarre, knob: KNAR; b. Middle English knor, a swelling: KNUR. 4. Germanic *kn-u-b- in Middle Low German knobbe, knubbe, knot in wood, knob: KNOB, NuB. 5. Germanic *kn-u-k- in: a. Old English cnocian, to knock: KNOCK; b. Italian gnocco, nocchio, knot in wood: GNOCCHI; c. Middle Low German kndkel, knuckle, akin to Middle English knakel, knuckle: KNUCKLE. 6. Ger- manic *kn-u-l- in: a. Old English cnyllan, to strike: KNELL, KNOLL; b. Old English cnoll, a knoll: KNOLL!. 7. Germanic *kn-u-p- in Middle Dutch cnoppe, knob, bud: KNOBKERRIE. 8. Germanic *kn-u-t- in: a. Old Eng- lish cnytten, to tie in a knot, knit: KNIT; b. Old English cnotta, knot in cord: KNOT!; c. Old Norse kniitr, knot in cord: KNOUT. 9. Germanic *kn-u-th- in Old High German knodo, knob, knot (> French quenelle): QUENELLE 10. Germanic *kn-i-b- in Old English cnif, knife: KNIFE. 11. Germanic *kn-e-th- in Old English cnedan, to knead: KNEAD. [Pok. gen- 370.] gene-. Also gen-. To give birth, beget; with derivatives referring to aspects and results of procreation and to familial and tribal groups. 1. Suffixed zero-grade form *gn-yo- in Germanic *kunjam, family, in: a. Old English cyn(n), race, family, kin: KIN; KINDRED; b. *kuningaz, king (< “son of the royal kin”), in Old English cyning, king: KING. 2. Suffixed zero-grade form *gn-ti- in: a. Ger- manic *kundjaz, family, race, in Old English cynd, gecynd(e), origin, birth, race, family, kind: KIND!; b. Ger- manic*kundiz, natural, native, in Old English gecynde (ge-, collective prefix; see kom), natural, native, fitting: KIND?; c. Germanic variant *kinth- in Old High German kind, child: KINDERGARTEN, KRIss KRINGLE; d. Latin géns (stem gent-), race, clan (> French gens, men): GENS, GENTEEL, GENTILE, GENTLE; GENDARME. 3. Suffixed full-grade form *gen-es- in: a. Latin genus (stem gener-), race, kind: GENDER, GENERAL, GENERATE, (GENERA-
502:ghabh-. Also ghebh-. To give or receive. 1. Form *ghebh- in Germanic *geban in: a. Old English giefan, to give: GIVE; b. compound *far-geban (*far-, away; see per'), to give away, in Old English forgi(e)fan, to give, give up, leave off (anger), remit, forgive: FORGIVE. 2. Suf- fixed form *ghebh-ti-, something given (or received), in Germanic “giftiz in Old Norse gipt, gift, a gift: GIFT. 3. O-grade form “*ghobh- in Germanic *gab-ulam, some- thing paid (or received), in Old English gafol, tribute, tax, debt: GAVEL2. 4. Form *ghabh-é- in: a. Latin habére, to hold, possess, have, handle (> habitdre, to dwell): ABLE, BINNACLE, HABILE, HABIT, HABITABLE, (HABI- TANT), (HABITAT); (COHABIT), EXHIBIT, INHABIT, IN- HIBIT, PREBEND, PROHIBIT, (PROVENDER); b. Latin débére (dé-, away from; see de-; third person plural present passive debentur), to owe: DEBENTURE, (DEBIT), DEBT, DEVOIR, DUE, (DUTY); (ENDEAVOR). Compare kap-. [Pok. ghebh- 407.]
931:seue-', To give birth. Suffixed zero-grade form in deriva- tive noun *su(2)-nu-, son, in Germanic *sunuz in Old English sunu, son: SON. See also su-. [Pok. 2. seu- 913.]
```


## [2026-09-05T20:15:08.104Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Pok. do-\\|do- 223\\|RENDER, RENT\\|ANECDOTE\" AHD_watkins1985.txt | head -5",
 "description": "Find Watkins do- entry"
}
```


### [2026-09-05T20:15:08.153Z] TOOL RESULT

```
404:d6-. To give. Contracted from *doo-. 1. Zero-grade form *do- in Latin dare, to give: DADO, DATE, DATIVE, DATUM, DIE?; ADD, BETRAY, EDITION, PERDITION, RENDER, (RENT!), (SURRENDER), TRADITION, (TRAITOR), (TREA- SON), VEND. 2. Suffixed form *dé-no- in Latin dénum, gift (> ddndre, to present, forgive): DONATION, DONA- TIVE, DONOR; CONDONE, PARDON. 3. Suffixed form *do-t/i)- in: a. Latin dds (genitive détis), dowry: DOT?, DOWAGER, DOWER, (DOWRY); ENDOW; b. Slavic *datja in Russian dacha, gift: DACHA; C. Russian dat’, to give, in izdat’, to publish: sAMIzDAT. 4. Reduplicated form *di-dé- in Greek didonai, to give: DOSE; ANECDOTE, ANTIDOTE, APODOSIS, EPIDOTE. [Pok. d6- 223.] [dorsum. The back. Latin noun of unknown origin. DORSAL, DORSO-, DORSUM, DOSS, (DOSSAL), DOSSER, DOS- SIER; ENDORSE, INTRADOS, REREDOS.]
1245:-ANDRY ner-2 ANECDOTE d6- ANELE elaia ANEMO- ane- ANEROID newo- ANESTHESIA au-5 ANEURYSM were-! ANFRACTUOUS bhreg- ANGARY angelos ANGEL angelos ANGELIC angelos ANGELICA angelos ANGELUS angelos ANGER angh- ANGINA angh- ANGLE! = ank- ANGLE? §ank- ANGLE ank- ANGST angh- ANGUILLIFORM ang¥hi- ANGUINE ang¥hi- ANGUISH angh- ANHYDROUS wed-! ANIL nei-
```


## [2026-09-05T20:15:19.527Z] TOOL CALL #43: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/دادن\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh₃-\" \\\n \"https://en.wiktionary.org/wiki/هوشیار\" \\\n \"https://en.wiktionary.org/wiki/اسفندیار\" \\\n \"https://en.wiktionary.org/wiki/دلمه\" \\\n \"https://en.wiktionary.org/wiki/dolma\" \\\n \"https://www.etymonline.com/word/dolman\" \\\n \"https://en.wiktionary.org/wiki/پاداش\" ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 139, roots Dô 2 / Dolmak — verification of nodes\" 2>&1 | tail -2; done",
 "description": "Archive web sources batch 1"
}
```


### [2026-09-05T20:15:27.443Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/دادن
/home/sfmqrb/git/rishe/data/verification/sources/web/ce6c8365c487ac7f.txt
### https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh₃-
/home/sfmqrb/git/rishe/data/verification/sources/web/61498ad8dd7f3082.txt
### https://en.wiktionary.org/wiki/هوشیار
/home/sfmqrb/git/rishe/data/verification/sources/web/69cc5680619e70b4.txt
### https://en.wiktionary.org/wiki/اسفندیار
/home/sfmqrb/git/rishe/data/verification/sources/web/e4583050ec4994bb.txt
### https://en.wiktionary.org/wiki/دلمه
/home/sfmqrb/git/rishe/data/verification/sources/web/5672b3c2aca7989c.txt
### https://en.wiktionary.org/wiki/dolma
/home/sfmqrb/git/rishe/data/verification/sources/web/4f6455312b263e85.txt
### https://www.etymonline.com/word/dolman
/home/sfmqrb/git/rishe/data/verification/sources/web/ba1bfe912777979f.txt
### https://en.wiktionary.org/wiki/پاداش
/home/sfmqrb/git/rishe/data/verification/sources/web/117e63eb8f6a7513.txt
```


## [2026-09-05T20:15:30.686Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in ce6c8365c487ac7f 69cc5680619e70b4 e4583050ec4994bb; do echo \"##### $f\"; grep -n -A12 \"Etymology\" $f.txt | head -60; done",
 "description": "Read Wiktionary dadan, hushyar, esfandiyar"
}
```


### [2026-09-05T20:15:32.782Z] TOOL RESULT

```
##### ce6c8365c487ac7f
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Verb 
69-
70- 1.3.1 
71- Conjugation 
72-
73- 1.3.2 
74- Derived terms 
--
164: Etymology
165- [ edit ] 
166-
167: Etymology tree
168-
169- Proto-Indo-European *deh₃- redup. 
170-
171- Proto-Indo-European *-ti 
172-
173- Proto-Indo-European *dédeh₃ti 
174- Proto-Indo-Iranian *dádaHti 
175- Old Persian 𐎭𐎭𐎠𐎬𐎢𐎺 ( d-d-a-tu-u-v /⁠dadātuv⁠/ ) 
176- Persian دادن 
177-
178- Inherited from Old Persian 𐎭𐎭𐎠𐎬𐎢𐎺 ( d-d-a-tu-u-v /⁠dadātuv⁠/ ) , from Proto-Indo-Iranian *dádaHti , from Proto-Indo-European *dédeh₃ti , reduplication of *deh₃- , or from *-ti . Cognates include Avestan 𐬛𐬀𐬛𐬁𐬌𐬙𐬌 ( dadā i ti ) , Polish dać , Ancient Greek δίδωμι ( dídōmi ) , Sanskrit ददाति ( dádāti ) , Latin dare , English data and Latin datum . [ 1 ] 
179-
##### 69cc5680619e70b4
65: Etymology 
66-
67- 1.3 
68- Pronunciation 
69-
70- 1.4 
71- Noun 
72-
73- 1.4.1 
74- Related terms 
75-
76- 1.4.2 
77- Descendants 
--
161: Etymology
162- [ edit ] 
163-
164- From Middle Persian 𐭠𐭥𐭱𐭣𐭠𐭫 ( ōšyār , “ conscious ” ) , a pre-Middle Persian compound equivalent to Middle Persian 𐭠𐭥𐭱 ( ōš , “ consciousness, intellect ” ) + 𐭣𐭠𐭫 (dār, “having”), with a phonetic shift *ušiy-dar > *ušiy-yar > *ušiyar > ōšyār.
165-
166- The first component is from Old Persian [script needed] ( ušiy , “ consciousness, intelligence ” ) , ultimately from Proto-Indo-European *h₂ṓws (compare Northern Kurdish hiş ), while the second component is from Middle Persian , from Old Persian , from Proto-Iranian *dar- , [ 1 ] from Proto-Indo-Iranian *dʰar- ( to hold, carry; to bear, support ) , from Proto-Indo-European *dʰer- ( “ to hold ” ) .
167-
168- Pronunciation
169- [ edit ] 
170-
171- ( Classical Persian ) IPA ( key ) : /hoːʃ.ˈjaːr/ 
172-
173- ( Dari, formal ) IPA ( key ) : [hoːʃ.jɑ́ːɾ] 
##### e4583050ec4994bb
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
69-
70- 2 
71- Urdu 
72-
73- Toggle Urdu subsection 
74-
--
76: Etymology 
77-
78- 2.2 
79- Proper noun 
80-
81- Toggle the table of contents 
82-
83- اسفندیار 
84-
85- 5 languages 
86-
87- বাংলা 
88- فارسی 
--
152: Etymology
153- [ edit ] 
154-
155- From Middle Persian [Term?] ( /⁠spandadāt⁠/ ) , in turn derived from Avestan 𐬯𐬞𐬆𐬥𐬙𐬋𐬜𐬁𐬙𐬀 ( spəntōδāta , literally “ given by Amesha Spenta ” ) .
156-
157- Pronunciation
158- [ edit ] 
159-
160- ( Classical Persian ) IPA ( key ) : /ʔis.fan.di.ˈjaːr/ 
161-
162- ( Dari, formal ) IPA ( key ) : [ʔɪs.fän̪.d̪i.jɑ́ːɾ] 
163-
164- ( Dari, formal ) IPA ( key ) : [ʔɪs.fän̪.d̪i.jɑ́ːɾ] 
--
215: Etymology
216- [ edit ] 
217-
218- Borrowed from Classical Persian اسفندیار ( isfandiyār ) .
219-
220- Proper noun
221- [ edit ] 
222-
223- اسفندیار • ( isfandiyār )  m ( Hindi spelling इस्फ़ंदियार ) 
224-
225- name of the son of Gishtāsb, of the first dynasty of Persian kings.
226-
227- a male given name
```


## [2026-09-05T20:15:45.364Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in 5672b3c2aca7989c 4f6455312b263e85 117e63eb8f6a7513; do echo \"##### $f\"; grep -n -A10 \"^ *Etymology$\" $f.txt | head -50; done; echo \"##### etymonline dolman\"; grep -n -i -B2 -A8 \"dolman\" ba1bfe912777979f.txt | head -60",
 "description": "Read dolme/dolma/padash/etymonline"
}
```


### [2026-09-05T20:15:47.187Z] TOOL RESULT

```
##### 5672b3c2aca7989c
146: Etymology
147- [ edit ] 
148-
149- Borrowed from Turkic , cf. Azerbaijani dolma , Turkish dolma .
150-
151- Pronunciation
152- [ edit ] 
153-
154- ( Classical Persian ) IPA ( key ) : /dul.ˈma/ 
155-
156- ( Dari, formal ) IPA ( key ) : [d̪ʊl.má] 
##### 4f6455312b263e85
255: Etymology
256- [ edit ] 
257-
258- From Greek ντολμάς ( ntolmás ) or its etymon, Turkish dolma , from Ottoman Turkish طولمه ( dolma ) , from طولمق ( dolmak , “ to get full, be filled ” ) . [ 1 ] [ 2 ] Thus, the word literally means “stuffed thing”.
259-
260- Pronunciation
261- [ edit ] 
262-
263- ( General American ) IPA ( key ) : /ˈdoʊlmə/ 
264-
265- Audio ( Southern England ) : ( file ) 
--
372: Etymology
373- [ edit ] 
374-
375- Morphologically from dol +‎ -ma .
376-
377- Pronunciation
378- [ edit ] 
379-
380- IPA ( key ) : [doɫˈmɑ] 
381-
382- Audio ( Baku ) : ( file ) 
--
698: Etymology
699- [ edit ] 
700-
701- From Turkish dolma .
702-
703- Pronunciation
704- [ edit ] 
705-
706- IPA ( key ) : /ˈdolmɑ/ , [ˈdo̞lmɑ̝] 
707-
708- Rhymes: -olmɑ 
--
1387: Etymology
1388- [ edit ] 
1389-
1390- Borrowed from Turkish dolma , from Ottoman Turkish طولمه ( tolma ) .
1391-
1392- Pronunciation
1393- [ edit ] 
1394-
1395- ( Standard Indonesian ) IPA ( key ) : /ˈdolma/ [ˈdol.ma] 
1396-
1397- Rhymes: -olma 
##### 117e63eb8f6a7513
153: Etymology
154- [ edit ] 
155-
156- From Middle Persian pʾtdʾšn' ( pādāšn , “ reward, retribution ” ) . Equivalent to پادـ ( pād-  / pâd- , “ counter-, re- ” ) +‎ دهش ( dahiš  / daheš , “ giving ” ) .
157-
158- Pronunciation
159- [ edit ] 
160-
161- ( Classical Persian ) IPA ( key ) : /paː.ˈdaːʃ/ 
162-
163- ( Dari, formal ) IPA ( key ) : [pʰɑː.d̪ɑ́ːʃ] 
##### etymonline dolman
1:URL: https://www.etymonline.com/word/dolman
2-FETCHED: 2026-09-05T20:15:26Z
3-STATUS: 200
4-TITLE: Etymonline - Online Etymology Dictionary
5-
6-Etymonline - Online Etymology Dictionary 
7-
8- Search 
9- Log in
```


## [2026-09-05T20:16:00.293Z] TOOL CALL #46: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/dolman\" \\\n \"https://en.wiktionary.org/wiki/Baghdad\" \\\n \"https://en.wiktionary.org/wiki/داشن\" \\\n \"https://en.wiktionary.org/wiki/دادار\" \\\n \"https://www.nisanyansozluk.com/kelime/dolamak\" ; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 139, roots Dô 2 / Dolmak — node verification\" 2>&1 | tail -1; done",
 "description": "Archive web sources batch 2"
}
```


### [2026-09-05T20:16:05.569Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/dolman
/home/sfmqrb/git/rishe/data/verification/sources/web/d0dc7bef6d2bd196.txt
### https://en.wiktionary.org/wiki/Baghdad
/home/sfmqrb/git/rishe/data/verification/sources/web/2b72a8d1c7608832.txt
### https://en.wiktionary.org/wiki/داشن
/home/sfmqrb/git/rishe/data/verification/sources/web/c5f3ecacc614760e.txt
### https://en.wiktionary.org/wiki/دادار
/home/sfmqrb/git/rishe/data/verification/sources/web/3f808111b547282a.txt
### https://www.nisanyansozluk.com/kelime/dolamak
/home/sfmqrb/git/rishe/data/verification/sources/web/a2904ddaa7e79d71.txt
```


## [2026-09-05T20:16:09.119Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in d0dc7bef6d2bd196 2b72a8d1c7608832 c5f3ecacc614760e 3f808111b547282a; do echo \"##### $f\"; grep -n -A8 \"^ *Etymology$\" $f.txt | head -40; done; echo \"##### nisanyan\"; wc -c a2904ddaa7e79d71.txt; head -c 1500 a2904ddaa7e79d71.txt",
 "description": "Read batch 2"
}
```


### [2026-09-05T20:16:10.859Z] TOOL RESULT

```
##### d0dc7bef6d2bd196
194: Etymology
195- [ edit ] 
196-
197- Jean Baptiste Vanmour , Portret van Sultan Ahmed III ( Portrait of Sultan Ahmed III , 1703–1717), collection of the Rijksmuseum , Amsterdam , the Netherlands. The Sultan of the Ottoman Empire is depicted wearing a dolman (sense 1) .
198-
199- An 1831 portrait by Georg Philipp Schmitt of Count György Károlyi de Nagykároly, a Hungarian politician, wearing a dolman (sense 2) 
200-
201- An illustration by Laure Noël from an 1871 edition of Harper's Bazaar showing the front and back of a cashmere dolman (sense 3) 
202-
##### 2b72a8d1c7608832
181: Etymology
182- [ edit ] 
183-
184- Borrowed from Arabic بَغْدَاد ( baḡdād ) , from Classical Persian بَغْدَاد ( baġdād ) (see there for more). Doublet of Bhagadatta (derived from Sanskrit भगदत्त ( bhagadatta ) ).
185-
186- Pronunciation
187- [ edit ] 
188-
189- IPA ( key ) : /bæɡˈdæd/ , /ˈbæɡdæd/ 
##### c5f3ecacc614760e
135: Etymology
136- [ edit ] 
137-
138- From Middle Persian dʾšyn .
139-
140- Pronunciation
141- [ edit ] 
142-
143- ( Classical Persian ) IPA ( key ) : /daː.ˈʃan/ 
##### 3f808111b547282a
142: Etymology
143- [ edit ] 
144-
145- Inherited from Middle Persian [script needed] ( dʾtʾl /⁠dādār⁠/ ) , from Proto-Iranian **daHtā́ , from Proto-Indo-Iranian *dʰaHtā́ , from Proto-Indo-European *dʰeh₁-tḗr , from *dʰeh₁- ( “ to do, put, place ” ) .
146-
147- Pronunciation
148- [ edit ] 
149-
150- ( Classical Persian ) IPA ( key ) : /daː.ˈdaːr/ 
##### nisanyan
359 a2904ddaa7e79d71.txt
URL: https://www.nisanyansozluk.com/kelime/dolamak
FETCHED: 2026-09-05T20:16:05Z
STATUS: 200
TITLE: dola- - Nişanyan Sözlük

dola- - Nişanyan Sözlük 

 Nişanyan Sözlük 

 ç ğ ı ö ş ü 
 ileri arama

 Bu sözlük nedir? Kullanım Şartları ·
 Gizlilik Politikası 

 © Sevan Nişanyan 2002-2026
 Alıntılarda kaynak gösterilmesi rica olunur.
```


## [2026-09-05T20:16:20.028Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '200,240p' d0dc7bef6d2bd196.txt",
 "description": "Wiktionary dolman etymology body"
}
```


### [2026-09-05T20:16:20.070Z] TOOL RESULT

```
 An illustration by Laure Noël from an 1871 edition of Harper's Bazaar showing the front and back of a cashmere dolman (sense 3) 

 Apparently from French doliman , dolman (sense 2), ultimately from Ottoman Turkish طولامان , دولامان ( dolaman , “ robe ” ) , from طولامق ( dolamak , “ to wrap around ” ) . Compare German Doliman , Dollman ; Hungarian dolmány .

 Pronunciation
 [ edit ] 

 ( Received Pronunciation ) IPA ( key ) : /ˈdɒlmən/ 
 Audio ( Southern England ) : ( file ) 

 ( General American ) IPA ( key ) : /ˈdoʊlmən/ 

 Homophone : dolmen 

 Hyphenation: dol‧man 

 Noun
 [ edit ] 

 dolman ( plural dolmans ) 

 A long, loose garment with narrow sleeves and an opening in the front, generally worn by Turks .
 1903 , Maurus Jókai , “Three Men”, in R[obert] Nisbet Bain , transl., The Slaves of the Padishah: (“The Turks in Hungary,” being the Sequel to “Midst the Wild Carpathians”): A Romance , 3rd edition, London: Jarrold & Sons , 10 & 11, Warwick Lane, E.C., →OCLC , page 33 : Feriz Beg, on discarding his dolman , rolled up the sleeves of his fine shirt of Turkish linen to his shoulders, and drew from its sheath his fine Damascus scimitar, which was scarce two inches broad, and so flexible that you could have bent it double in every direction like a watch-spring. 

 1938 , The Hungarian Quarterly , volume IV, Budapest; New York, N.Y.: Society of the Hungarian Quarterly, →OCLC , page 292 : [I]n the second half of the century the long Turkish dolman disappears completely and tight, knee-length dolmans and mentes become general. 

 1980 , Katalin Földi-Dózsa, “How the Hungarian National Costume Evolved”, in Polly Cone, editor, The Imperial Style: Fashions of the Hapsburg Era: Based on the Exhibition, Fashions of the Hapsburg Era, Austria-Hungary, at the Metropolitan Museum of Art, December 1979—August 1980 , New York, N.Y.: Metropolitan Museum of Art , →ISBN , page 80 : The quintessentially Hungarian item of men's clothing was the dolman . This flowing garment, open in the front, replaced the waistcoat after the Renaissance. 

 A short, close-fitting , heavily braided military jacket , usually worn under a pelisse , originally by hussars .
 1983 , Roberta Gellis , Fortune's Bride , New York, N.Y.: Dell Publishing , →ISBN : Robert nodded in reply to her question and not only took off his helmet but unhooked his pelisse, threw it on a chair, and unbuttoned the top of his dolman . 

 1998 , Gayle Greeno , Sunderlies Seeking (DAW Book Collectors; no. 1103 ), New York, N.Y.: DAW Books , →ISBN : Sitting on the chair's edge, he shrugged a shoulder until his dolman fell into place, then balanced his helmet on his knee like a pampered pet. 

 2005 , Wilbur [Addison] Smith , The Triumph of the Sun , London: Macmillan Publishers , →ISBN : He wore his dolman slung over one shoulder and clasped at his throat with a gold chain, and carried his Hussar's bearskin busby under his right arm. 

 2015 , “dolman”, in Annette Lynch, Mitchell D. Strauss, editors, Ethnic Dress in the United States: A Cultural Encyclopedia , Lanham, Md.: Rowman & Littlefield , →ISBN , page 103 : The uniform jacket with several rows of buttons and a horizontal braid across the front originally worn by the Hussars was also called a dolman . 

 A woman's garment with wide capelike sleeves.
 1942 , Emily Carr , “A Little Town and a Little Girl: Characters”, in The Book of Small ( Project Gutenberg Australia ; eBook no. 0400201.txt )‎ [1] , Toronto: Oxford University Press , published February 2004 (Project Gutenberg Australia version), →OCLC , archived from the original on 31 March 2016 : She, who never went out, found a bonnet that I had never seen before, put a dolman over her best silk dress, locked the guinea fowl safe in her kitchen and got into a hack with Henry, her smelling-bottle and her cap, in which was a new bunch of everlasting flowers.
```


## [2026-09-05T20:16:21.067Z] TOOL CALL #49: Bash

```json
{
 "command": "for u in \"https://en.wiktionary.org/wiki/dolamak\" \"https://en.wiktionary.org/wiki/dolmak\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 139, Turkish root Dolmak — verifying the root gloss\" 2>&1 | tail -1; done",
 "description": "Fetch Turkish verbs"
}
```


### [2026-09-05T20:16:24.892Z] TOOL RESULT

```
### https://en.wiktionary.org/wiki/dolamak
/home/sfmqrb/git/rishe/data/verification/sources/web/ecfb5936354f8631.txt
### https://en.wiktionary.org/wiki/dolmak
/home/sfmqrb/git/rishe/data/verification/sources/web/7a8cae711c8b079b.txt
```


## [2026-09-05T20:16:28.277Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in ecfb5936354f8631 7a8cae711c8b079b; do echo \"##### $f\"; grep -n -A6 \"^ *Etymology\" $f.txt | head -30; grep -n -i \"to be filled\\|to become full\\|wrap\\|wind\" $f.txt | head -8; done",
 "description": "Turkish dolamak/dolmak etymologies"
}
```


### [2026-09-05T20:16:30.665Z] TOOL RESULT

```
##### ecfb5936354f8631
62: Etymology 
63-
64- 1.2 
65- Verb 
66-
67- 1.2.1 
68- Conjugation 
--
151: Etymology
152- [ edit ] 
153-
154- Inherited from Ottoman Turkish طولامق ( dolamak , “ to twist, wind round about a thing ” ) , from Proto-Turkic *tolga- ( “ to twist, to wrap round ” ) . [ 1 ] 
155-
156- Cognates
157-
154: Inherited from Ottoman Turkish طولامق ( dolamak , “ to twist, wind round about a thing ” ) , from Proto-Turkic *tolga- ( “ to twist, to wrap round ” ) . [ 1 ] 
158: Cognate with Karakhanid [script needed] ( tolɣāmāk , “ to twist, wrap round ” ) , Azerbaijani dolamaq ( “ to spin, wind ” ) , Kazakh толғау ( tolğaw , “ to twirl, rotate ” ) , Kyrgyz толгоо ( tolgoo , “ to twist, rotate ” ) , Southern Altai толгоор ( tolgoor , “ to twist, to rotate ” ) , Turkmen dolamak ( “ to wrap, bind, turn ” ) , Tuvan долгаар ( dolgaar , “ to turn, rotate, twist ” ) , Uzbek toʻlgʻamoq ( “ to turn, twist ” ) .
165: ( transitive ) to wind , wrap , wrap around
166: Atkıyı boynuna dola . Wrap the scarf around your neck. 
168: Bu sadece kollarını güzel bir bayana dolamak için bir bahane. It's just an excuse to wrap your arms around a pretty girl. 
##### 7a8cae711c8b079b
62: Etymology 
63-
64- 1.2 
65- Verb 
66-
67- 1.2.1 
68- Conjugation 
--
154: Etymology
155- [ edit ] 
156-
157- Inherited from Ottoman Turkish طولمق ( “ to fill, become full; swell ” ) , from Proto-Turkic *tōl- ( “ to be full ” ) .
158-
159- Verb
160- [ edit ]
```


## [2026-09-05T20:16:47.237Z] TOOL CALL #51: Bash

```json
{
 "command": "for u in \"https://abadis.ir/fatofa/دلمه/\" \"https://abadis.ir/fatofa/دی/\"; do echo \"### $u\"; timeout 120 python3 tools/fetch_source.py \"$u\" --note \"page 139, Mo'in entries دلمه (MON:1554) and دی (MON:1588)\" 2>&1 | tail -1; done",
 "description": "Fetch Mo'in entries online"
}
```


### [2026-09-05T20:16:53.235Z] TOOL RESULT

```
### https://abadis.ir/fatofa/دلمه/
/home/sfmqrb/git/rishe/data/verification/sources/web/3a8f48d7e79518fc.txt
### https://abadis.ir/fatofa/دی/
/home/sfmqrb/git/rishe/data/verification/sources/web/3c79c76598c2f023.txt
```


## [2026-09-05T20:16:56.859Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### dolme\"; grep -n -A6 \"فرهنگ معین\\|معین\" 3a8f48d7e79518fc.txt | head -30; echo \"### dey\"; grep -n -A8 \"فرهنگ معین\" 3c79c76598c2f023.txt | head -40",
 "description": "Read Mo'in entries"
}
```


### [2026-09-05T20:16:56.917Z] TOOL RESULT

```
### dolme
28: فرهنگ معین
29-
30- (دُ مَ یا مِ ) (اِ. ) نوعی خوراک مرکب از برنج ، گوشت چرخ کرده ، لپه ، سبزی مخصوص و غیره که در برگ مو، برگ کلم و غیره پیچند و پزند.
31- ( ~. ) (اِ. ) کیسة پولی که در جشن عروسی یا اعیاد سال به مهمان و مدعوان دهند. 
32-
33- فرهنگ عمید
34-
--
178:منبع فرهنگ لغت معین
179-فرهنگ کوچک زبان پهلوی
180-فرهنگ واژه های اوستا
181-حرف مفت یک پان ترکیسم همیشه حرف مفت می زنند بدون منابع یا اگر با منابع حرف بزنند منابع هاشون درست نیست همیشه پان ترکیسم بازهم گویم حرف مفت می زنند یک مشت آدم غیرمنطقی هستند شما بدن منابع یا منبع حرف می زنید شماآقا به خدا این یک توهین به هم وطنی های خودتون محسوب میشه. . پان ترکیسم آدم های غیر منطقی هستند تمام.
182-
183- عزیزن جناب عالی دیگه شورشو در آوردی هر کجا میرم به هر کلمه سرچ میکنم که ترکی هست رو برگشتی گفتی پارسیه!!! خودشم بدون درصدی منبع. . . 
184-آقا به خدا این یک توهین به هم وطنی های خودتون محسوب میشه. . 
--
219: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
220-
221- لینک ها 
222-
223- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
224-
225- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
### dey
40: فرهنگ معین
41-
42- (دِ یْ ) (اِ. ) ۱ - دهمین ماه هر سال شمسی . ۲ - نامِ روزهای هشتم ، پانزدهم و بیست و سوم هر ماه شمسی .
43- ( دِ ) [ په . ] (ق . ) ۱ - روز گذشته ، دیروز. ۲ - شب گذشته . 
44-
45- فرهنگ عمید
46-
47- ۱. ماه دهم از سال خورشیدی، ماه اول زمستان که موسم سختی سرما است.
48-۲. [قدیمی] نام روزهای هشتم و پانزدهم و بیست وسوم هر ماه خورشیدی. &delta، چون سه روز از روزهای ماه به نام دی بوده برای امتیاز آن ها نام هر روز را به نام روز بعد افزوده روز هشتم را دیباذر (دی به آذر ) و روز پانزدهم را دی به مهر و روز بیست وسوم را دیبادین (دی به دین ) گفته اند.
--
234: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
235-
236- لینک ها 
237-
238- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
239-
240- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
241-
242- © 2006-2026 abadis.ir
```


## [2026-09-05T20:17:21.013Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"}{n++; if (index($0,\"dahišn [dhšn\\x27]\")>0) print \"dahisn leaf:\",n; if (index($0,\"dātār [d^t?]]\")>0) print \"datar leaf:\",n}' NYB_vol2_glossary.txt; echo \"--- check leaf 65 = printed 56?\"; awk 'BEGIN{RS=\"\\f\"} NR==64' NYB_vol2_glossary.txt | head -3",
 "description": "Nyberg leaf numbers"
}
```


## [2026-09-05T20:17:22.116Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" FSF_pages.txt | head -3; awk 'BEGIN{RS=\"\\f\"} END{print \"FSF leaves:\",NR}' FSF_pages.txt; echo \"--- search داشن\"; grep -n \"داشن\" FSF_pages.txt | head -5",
 "description": "FSF structure"
}
```


### [2026-09-05T20:17:22.716Z] TOOL RESULT

```
dahisn leaf: 68
datar leaf: 72
--- check leaf 65 = printed 56?
s bwatn, pres. MPrth bwy-, bwas-, MPrs bwz-; Arm. lw. bužem; Paz. boxtan, buxtan, bož-. — V. božišn.
buxtarčh [bwht’lyh] salvation 683.
to], amāh-tc, ké-c, ka-c (ka vas-ic v.s. v. ka), bē-c, apar-ic, ö-c(i), pat-ic, peš-ic, hac-ic; hac hàn bē tarsēh-ic 4812; ete.; in
```


### [2026-09-05T20:17:24.593Z] TOOL RESULT

```
FSF leaves: 484
--- search داشن
3371:                       ‫رسستم پس از‬                           ‫بحر و ابرست روز پاداشن‬
6267:‫(سم‪)۳-۳۴۵‬‬                                                    ‫داشن‬
6268:                                                                ‫باداش = پاداشن =‬
6270:  ‫بد و نیک را هر دو پاداشن است‬          ‫(یادداشت‌های گات‌ها ص ‪ )۷۸۲‬مرکب از‬
6280:‫پیغمبر تست روز پاداشن‬                    ‫=رگشت‬
```


## [2026-09-05T20:17:38.166Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dātan\\|dātan \\[\" NYB_vol2_glossary.txt | head -5; echo \"---\"; sed -n '1220,1240p' NYB_vol2_glossary.txt",
 "description": "Nyberg dātan entry"
}
```


### [2026-09-05T20:17:38.278Z] TOOL RESULT

```
---
dāštan [d'štn'] dār- [YHSNN-; d'1- 217. 281. 10014. 10279], imp. sg. with encl. pron. där:om [YHSNN-m] 6t; opt. 2nd p. sg. dārēš 41!?; pt. dašt = pret. pass. 3d p. sg., construed as an act. form 495-5; to keep, to hold, to sustain, to maintain, to have, 8?! and passim; — with an adj. as a complement of the obj.: Sahpuhr kanicak āžarmīk u garamik däst Š. kept the girl honoured and respected 163-4; 225 ete. passim; the complement some- times comes near to an adv., e. g. véh ~ to keep, handle a th. well 5026-27, and may be replaced by an adv.: én zan garämikihä ddr 1024; 6415; — with an obj. and pat + an adj.: to consider a p. or a th. to be ...: pat margaržān ~ to consider a p. guilty of death 1014-19; 6398-9, 8017, 839-19; pat azateh (cas. obl. sg.) där-om! consider me as a free (wom- an) — release me (from slavery)! 64, v. s. v. Gzat; — pat & ~ ku to be of the opinion that, to think, imagine that 2525, 982-3, 3227 sq. 5012-13, ef NP pindāštan < *pa(t) én daštan; pat ce dārēh how do you regard (the case mentioned in the preceding kū- clause)? 105-$; pat depahr, pat nihän
www.parsianjoman.org hek
' dāštan
mw: v. these ws.; — gö& ~, (apar) nikäh ~: v. these ws. — apdc ~ to keep back (hac from), to avert, to repulse 495-9. 702°, 739-10, 8719-20, 9619. 10272; to abjure 19! (cf s. v. rad); — apar ~ to lift up from (hac damik) 3318-19; — bé ~ to take away, to tear off (hac from) 1029; — 6 ham ~ to hold together, *to radiate an unbroken ray (hac õi be starting from him) 5125-27, 525; — peš ~ to sacrifice, to make a sacrifice of 1174; — as a sort of auxiliary vb. denoting the duration of the act: -m pat drinišn däret u drinet he keeps tear- ing me up 1027-5; dašt guft kept saying 1019-20, — Av. (690 sq.) ®dar-; MPrth dyrdn d r-; MPrs d'šin d?r-; Paz. NP dästan dar-.
dāštārēh [d*št*lyh] the act of keeping, maintaining ete. 713-4, 9210.20,
daštik [dštyk] belonging to the steppe 9725, 984,
dat [dt'] wild animal 9725, 984, — Av. (678) daitika-; NP dad(ah).
dat [d?t'] 1. law 6413-19, 6916, 8623, 9811, — 2. age 2?9 (with the gl. hangäm). 31. 10*%. 14°. 165. 622. 104°; cas. obl. dātēh 536-22, — 3. created, pt. of dätan: dēvān ~ created by the devs 1038-10-13, — 1. Av. (726) ddta- NP ddd ‘justice, equity’. — 2. NP dad ‘life, age’. — 3. Av. (671 sq.) daēvē.dāta-. dätan [YHBWN-tn'; d’tn' 119%, 1201] dah- [always YHBWN-], lst p. sg. YHBWN-m = dahom; 3d p. sg. = 2nd p. pl. ~ -yt = dahét; lst p. pl. ~-ym = dahem; 3d p. pl. ~-d = dahénd; subju. 2nd p. sg. —-'h = dahäh 34%; imp. sg. ~ = dah; pt. = pret. pass. 3d p. sg. dāt [YHBWN-t', inser. YHBWN; d>t' 22. 922 etc.] lst sg. dāt hom 57°; 2nd p. sg. dāt h&5'1*-* 3d p. pl. dāt hend '18?, construed as an act. form 18?!; pluperf. 3d p. sg. dat estet 8712, 3d p. pl. ~ ēstēnd 94*4; opt. pass. dāt [HWH-d =] he 2%; A. to give SPrs:15; 238-21 ete. passim; apāc ~ to give back 345-6; — fräc ~ to give away 5016-1’; — v, also dröt, framān, passax", zančh. — B. 1. to put, to place,
datistan
to deposit 922. 10912; — bē ~ to deposit 395.7:22. 402. 4910. 48?2. 4098-9.22-23, 5015, 9427; pat damīk bē ~ to lay (an enemy) in the dust 3329; to take off (clothes) 577; — (bé) 0 . . . — to transfer to . . . 88%. 953. 12016, — 2. to create 397. 577-8, 76 20.22 etc. passim. — to prepare 4216, with the gl. kū sāxt; — to bring about 451, v. ax"àyis- neh; — fräc ~ to put into existence by creation 932, 949. — Av. OP (711 sqq.) lda-; MPrth d?dn dh-; MPrs d'dn dy-, dyy-; Paz. dädan dah- (deh-, dih-); NP dadan dth-.
dātār [d^t?]] the Creator 5711; epithet of Ohurmazd, passim; creative principle 64°. dātārēh 1. the act of giving 704. — 2. the quality of being the Creator 71°.
datavar [d’twbl] judge P2: 2; pl. cas. obl. v-ān 10733, — < Olr. *dāta-bara-, v. dāt (1); KZŠPrth 1. 24 d*ibr; MPrth d?dbr; Ps. @twbl-; MPrs d’ywr; Talm. lw. dw’r, dwwr; Paz. NP davar.
ditavarčh l. judicial decision, judgment 7813. 7515-17, — 2. sg. cas. obl. of datavar: pat — kartan to make a p. one's judge, arbitrator 10314,
datéh [d’tyh] 1. the quality of being created, createdness, ''ereatureness'' 5513. — 2. cas. obl. of dāt (2) (q. v.).
dātihā [d'tyh?] righteously 631. 81?!. — MPrs d'dyh? (S).
datikéh [d’tykyh] the tenets of the third section of the Avesta called dätik ‘relat- ing to the Sacred Law’ 98". V. DkM 6771 sqq.; GrIrPh II, 20 sq., and cf gā- hānīk and hät-mänsr.
dätistän [d'tst'n'; DYN?] decision 451. 68 title. 818. 1054; judgment 7274; as opposed to passand (g. v.): a judgment which exceeds the formal prescriptions of the law, the utmost rigour of the law 70! [in other cases also: favour awarded above the formal prescriptions of the law]; ménóyé ~ the Heavenly Justice (personified) 7712; kar um (as a hendiadys) proper use 41%; lawful, righteous deeds
www .parsianjoman.org | ool sa,
datistan
7014; — affair, inatter 4°; condition, state 523-8.13, 964. — MPrs d’dyst’n; Paz. ddéstq, Skr. v. nyàya; NP dästän ‘a tale, story’. datistanéh [d’tst’nyh]. v. yuvat-~ and cf a-dätistäneh, -ihā.
datistanomandeh [~-’wmndyh] adjudie- ation 541°. — Paz. ddéstanmandi, Skr v. nyāyamattā (SGV XVI, 102).
```


## [2026-09-05T20:17:39.346Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"}{n++; if (index($0,\"داشن\")>0 && index($0,\"پاداشن\")>0) print \"leaf:\",n}' FSF_pages.txt | head; echo \"--- context\"; sed -n '6260,6290p' FSF_pages.txt",
 "description": "FSF dashn leaf and context"
}
```


### [2026-09-05T20:17:41.161Z] TOOL RESULT

```
leaf: 76
leaf: 131
leaf: 132
leaf: 140
leaf: 216
--- context
            ‫هنرا‬
               ‫ا‬ ‫شا‬
                  ‫سو‬‫خمه‬
                      ‫هس‬                     ‫زنج آلت و چارپای‬ ‫پسدادی گ‬
‫که پاداش این آنکه بسی‌جان شود‬           ‫نماندی که پایش برفتی ز جای‬
‫ز بد کسردن خویش پیچان شود‬               ‫(‪)۴-۲۱۴۷۱‬‬

‫(سم‪)۳-۳۴۵‬‬                                                    ‫داشن‬
                                                                ‫باداش = پاداشن =‬
                      ‫(اسدی‪:)۴-۵۲ .‬‬     ‫دهمیشن ‪09510۵0۵۵۳‬‬       ‫پسهلوی‪ :‬پات‬
  ‫بد و نیک را هر دو پاداشن است‬          ‫(یادداشت‌های گات‌ها ص ‪ )۷۸۲‬مرکب از‬
    ‫ست‬
     ‫نخحرد‬
         ‫شش از‬
             ‫و جان‬
                 ‫ر آنک‬
                     ‫خنک‬                ‫=د‪ .‬مخالف‪ .‬برگشت [در‬    ‫=اد ض‬ ‫پات پ‬
                     ‫(ناصر ‪:)۷۷۳-۵۱‬‬    ‫واژه‌های مرکب‪ :‬پادآوا ب=رگشت آواز ‪-‬به‬
         ‫حاکم به میان خصم و آن من‬        ‫=د‬
                                          ‫عربی صداء به فتح اول؛ پادزهر ض‬
‫پیغمبر تست روز پاداشن‬                    ‫=رگشت‬
                                             ‫زهر نوشدارو؛ پات سخون ب‬
                     ‫(ویس‪:)۱۵۱-۷۵ .‬‬     ‫‪+‬ار =ضد‬
                                              ‫=اسخ؛ پتیاره [] = پت ی‬
                                                                   ‫سخن پ‬
                                                                               ‫پادافراه‪ .‬پادافره‬

 ‫(‪)۲-۳۰۱-۹۹۴‬‬                                                  ‫بدین رنج و بدین گفتار نیکو‬
                      ‫(دقبقی ‪:)۶-۳۸-۸۶۲‬‬         ‫تو را داشن دهاد ایزد به مینو‬
              ‫سپهبدش را گفت فردا پگاه‬                                       ‫(مسعود ‪:)۵۲۶‬‬
 ‫بخوان از همه پادشاهی سپاه‬                                    ‫بحر و ابرست روز پاداشن‬
```


## [2026-09-05T20:17:57.656Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dasr\\|dāsr\\|das'r\\|dašn\\|dasn\" SNS.txt | head -10; echo \"--- pages leaves\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' SNS_pages.txt; grep -n \"dahisn\" SNS_pages.txt | head -3",
 "description": "SNS dasr lookup"
}
```


### [2026-09-05T20:17:59.786Z] TOOL RESULT

```
1752:. f/U £ .c*-lj o'j haxt 1 dasn: c^«»W 
4155:dasn + arm 
4159:.»j ,5^1/: arm I dasn: 'Cj.^-ji^ 
6733:lu ^i . .flf b : a-yGsdahr/a-y5sdasr : }a*-«o -*04>* 
6819:,f/n ** .c»-lj ^ : cairn I dasn*-" *^^ 
16393:•j*^'oi^'*tf->A'o l -* , - , dasr: ***-<-> 
16395:bahr : ^^^T dasr: ^ da0ra- : ^h-,l*jl jtf l^ 
16397:• f / IT** • lajii^ < Ia^ja : dasran : ^>^^y 
17246:.(c^-ljc^-.) c^ljidasn: Itroj 
32677:haxt i dasn 2/12 
--- pages leaves
242
3346:                                                                                                      \*i*j* jx» j'*£*iL-S:avizIdar                   dahisnan: v^^O i-i^Cf
11659:                                                                                                                                        W** 'A/IS* VV^ W«A ^JojIj,^ dahisn :»£d»rO                       ;
11665:                                                                                                                         J-«V^^         .yjb^g :be dahisn: njon^ ^),
```


## [2026-09-05T20:18:04.587Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16388,16400p' SNS.txt",
 "description": "SNS dasr entry context"
}
```


### [2026-09-05T20:18:04.634Z] TOOL RESULT

```
■H/IT** •ol*^^vr^' (if iUir:gahanIg: Aj*U>-<*-> 

•j*^'oi^'*tf->A'o l -* , - , dasr: ***-<-> 
.rfA^tfUfa^s^ UiW». 732)datra-: I> *S l5J j. da0ra-:fc. 
bahr : ^^^T dasr: ^ da0ra- : ^h-,l*jl jtf l^ 
-r/ITiS .f«/1 iS UofcwaZ.SnS. p. 137) 
• f / IT** • lajii^ < Ia^ja : dasran : ^>^^y
```


## [2026-09-05T20:18:13.505Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"بغداد\" TAD.txt | head -10; echo \"--- pages\"; grep -n \"بغداد\" TAD_pages.txt | head -5",
 "description": "TAD Baghdad"
}
```


### [2026-09-05T20:18:13.561Z] TOOL RESULT

```
510:بغداد - فارسي مركب من باغ أي بستان وداد أي علال 
--- pages
```


## [2026-09-05T20:18:14.672Z] TOOL CALL #60: Bash

```json
{
 "command": "timeout 120 python3 tools/fetch_source.py \"https://www.ahdictionary.com/word/search.html?q=dolman\" --note \"page 139, AHD:389 dolman entry\" 2>&1 | tail -1",
 "description": "Fetch AHD dolman"
}
```


### [2026-09-05T20:18:16.791Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/619c99d39f5a2bfb.txt
```


## [2026-09-05T20:18:23.097Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i -A4 \"dolman\" 619c99d39f5a2bfb.txt | head -40",
 "description": "Read AHD dolman"
}
```


### [2026-09-05T20:18:23.143Z] TOOL RESULT

```
1:URL: https://www.ahdictionary.com/word/search.html?q=dolman
2-FETCHED: 2026-09-05T20:18:16Z
3-STATUS: 200
4:TITLE: American Heritage Dictionary Entry: dolman
5-
6:American Heritage Dictionary Entry: dolman 
7-
8- HOW TO USE THE DICTIONARY
9- To look up an entry in The American Heritage Dictionary of the English Language, use the search window above. For best results, after typing in the word, click on the “Search” button instead of using the “enter” key.
10- Some compound words (like bus rapid transit, dog whistle, or identity theft ) don’t appear on the drop-down list when you type them in the search bar. For best results with compound words, place a quotation mark before the compound word in the search window.
--
49: adj. Of or relating to a garment having sleeves that taper from a very wide armhole: a dolman sweater. 
50-
51: [Partly from French doliman , woman's loose upper garment, and partly from French dolman , hussar's jacket (both ultimately from Ottoman Turkish dolama , robe, loose cassocklike garment with narrow sleeves worn by janissaries, French dolman , from German Dolman , ultimately, probably via Hungarian dolmany , from Ottoman Turkish dolama ), from Ottoman Turkish dolama , from Ottoman Turkish dolamak , to twist, wind, wrap around; akin to Turkic tolğamaq .] 
52-
53- The American Heritage® Dictionary of the English Language, Fifth Edition copyright ©2022 by HarperCollins Publishers. All rights reserved.
54-
55- Indo-European & Semitic Roots Appendices
```


## [2026-09-05T20:18:38.638Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd1 do-\"; grep -n \"geben' (perfektiv)\\|dö- : də\\|dö-  :  d\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5; echo \"=== WLD grep dätra\"; grep -n \"dä%ra\\|daBra\\|dätra\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5; echo \"=== IEC do-\"; grep -n \"^dō-\\|^do- \\|^dōrom\\|^dōnom\" IEC.txt | head -10; echo \"=== SYN give\"; grep -n \"11\\.21 GIVE\\|GIVE$\" SYN.txt | head -5",
 "description": "WLD/IEC/SYN lookups"
}
```


### [2026-09-05T20:18:40.366Z] TOOL RESULT

```
=== WLD Bd1 do-
=== WLD grep dätra
=== IEC do-
2349:do- (theme of dídomi, dómi, and cf. dotós). Cf. dón-, dotis Venetic cf. doto “I will give’, donasto ‘I have given’; Lat. do, donum, etc.; ON tæja ‘grant, help, avail
=== SYN give
18995:GIVE
29560:16.69 FORGIVE
```


## [2026-09-05T20:18:43.070Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2340,2360p' IEC.txt; echo \"=== SYN GIVE section\"; sed -n '18990,19030p' SYN.txt",
 "description": "Mann and Buck 'give'"
}
```


### [2026-09-05T20:18:43.144Z] TOOL RESULT

```
25
30
35
40
45
132
‘dense’, fr. *dntmno-); Lat. densus
dnts-, dont ‘tooth’. Cf. ednt-. Cf. WP I, 120 Skt. dan, dat, dant-; Av. cf. dantan; Per. dandan, beside dande ‘rib’; Oss. cf. dändäg (dim. type); Gk. cf. datü-sso: Go. cf. tunpus; Lat. cf. dens, -tis, gp dentum (Varro, later dentium); Osc. duntes “by the teeth'; Olr. dét; W dant, pl. daint & dannedd; Br. dant, pl. dent; Cor. dans, pl dyns, danneth; Go. tunpus, cf. also aíhva-tundi (o horsetooth' i. e. *briar); OHG zand (i-st.); Swiss zant, pl. zaent; Du. OS tand; OE top, pl. tep; ON tonn, pl. tenn, tenur & téór; Li. dantis, pl. danty, id.
do ^to, towards. Cf. dé. WP I, 770. Cf. endo, ndo Av. -da; Per. -da, -dā in i-dà ‘here’, ava-dà ‘there’; Hitt. -ta, -da in dame-da ‘elsewhere’; Gk. (?) in do-keúð “watch for, do-enüo, -néo “bend”, etc.; Lat. -do in quan-do; MIr. & Ir. do; OBr. do; Br. da (by WSP); W dy- (cpds.); OS.OE to; OHG zuo; MHG also ze (by WSP); Du. te (by WSP); Fris. to; OCS do (cf. also -da in ko-da ‘where’, fr. do); cf. also OCS da-Ze-do “as far as’; OLI. da- (vb.px); Latv. da-, id.
do- (theme of dídomi, dómi, and cf. dotós). Cf. dón-, dotis Venetic cf. doto “I will give’, donasto ‘I have given’; Lat. do, donum, etc.; ON tæja ‘grant, help, avail
do-ar- (by crasis > dar- ?). Cf. do and ar- (3) Arm. cf. taraj “I brought; W daru (inf. *fin- ish’); Li. (?) daraŭ, inf. daryti ‘do’
dö- (dódmi, dídomi, fut. dosio) ‘give’. WP I, 814 Skt. dádàmi, dadmi, fut. dasyámi; OPer. dā-; Av. daóámi; Per. cf. inf. dàdan; Arm. tam, fut. tac; Gk. dídomi, fut. dóso; Lat. do; W cf. dod (imperatv. *give!); ON cf. tæja ‘grant’; OCS fut. damí; OLi. duomi, fut. duosiu, duosu
dogos, is, ios, (n) ‘spike, tine’. WP I, 785 Hitt. cf. cakkis (of uncertain mng.); MHG zacke, G Zacken 'spike, spur; LG tacken ‘spike, twig’; Du. tak ‘branch’; ME tack; Li. dagys ‘thistie’; Latv. dadzis "bur
dogha “holding, reception’. See de$h- & cf. WP I, 783
153
Gk. dokhé; Li. dagà “harvest? (but in sense of ‘heat’, see dhoguh-)
doiKos, à ‘revelation, vision’. Cf. deiK-, diK-. WP I, 776 Skt. deSáh; Av daeso; Oss. des “wonder”, dis ‘surprise’; (Arm. tes, o-st. is fr. *derK- according to AM); Ir. cf. daochán trage; MHG zeige (oxyt. prototype: indication”); OE tah *teaching'; Cz. dés “terror”
doiuos, ios ‘godlike, heavenly’. WP I, 773. Cf. deiuo-, dieus, diu-, etc. Skt. deváh; Av. cf. daev-, v. *Cheat'; OPer. daiva- ‘demon’; Lat. divus; Li. cf. deive *god- dess’; Finn. LW taivas “heaven?
dõios ‘giving; gift. Cf. do-, dídomi, etc. Skt. dayah; Cz. -daj, -dej (in cpds.)
doK-, doKeið “perception, reception; make perceive, make receive’. See deK-. WP I, 783 Gk. dokéo ‘seem’; cf. dóke (*received *opin- ion"); Lat. doceo; OIr. doich ‘apparent’; OS cf. fra-tah ‘ornament’; fra-tahon ‘adorn’; OCS do3o, dositi “find”
dokt-, doket (?) “shaped; shaper Av. daxsta, om ‘tool’; Lat. doctus (?); LG tacht ‘shaped’
=== SYN GIVE section
4 eit Geto, of donum ‘gift’), perf,
C, ded : ‘dee Umbr. dede ‘dedit’,
a ‘ ete. ; Lith. duoti, Lett. V. gz? Ste, general Slavic; yam. tam; Alb, dhané;
CC-0. In Public Domain.
tain’, as Fr. garder, W. cadw, etc. (and so sometimes NE preserve), and to this group belongs NE keep in which ‘retain’ is now the leading sense. Thus all the words listed belong with those discussed in 11.15 or 11.24.
GIVE
Lith. duott Lett. duot ChSl. dati SCr. dati Boh. ddti Pol. daé Russ. dat’ Skt. da-, ra- Av. da-
Hitt. da- ‘take’ (Sturtevant, Hitt. Gloss. 146 with refs.). Possibly here also W. rhot, rhoddi, Br. rei, fr. *pro-d-, cf. Ir. do-rat ‘gave’ (suppl. verb to do-biur, be- low) fr. *to-pro-d- as also W. dyry im- perat. ‘give!’, etc. Pedersen 2.380, 473.
There are also forms pointing to an extension *ddu-, as OLat. subj. duim, duam, Umbr. purdovitu ‘porricito’, Cypr. opt. dufavor, Lith. dovana ‘gift’, etc.
2. Ir. do-biur ‘give, bring’, NIr. do- bheirim, but commonly dependent ta- bhraim, cpd. of Ir. berim ‘carry, bring’ (10.61).
NIr. tugaim, generalized fr. the pret. 3sg. tug, Ir. duic, tuic, tue ‘brought’, fr.
Gurukul Kangri Collection, Haridwar
FPS SS ++.
Digitized by Arya Samaj Foundation Chennai and eGangotri
750 SELECTED INDO-EUROPEAN SYNONYMS
*to-ucc-, etym. dub. See under Ir. ro- uce-, 10.61.
3. Goth. giban, ete., general Gmc., prob. : Lat. habére ‘have’, Ir. gaibim ‘take, seize’ (11.13), despite the semantic polarity, for which there are some paral- lels. Thus Ir. gaibim ‘take, seize’ and ON fa ‘seize, get’ (11.14) are sometimes used in the sense of ‘give’, likewise ME take (NED s.v. 60), and Hitt. da- ‘take’ = IE *do- ‘give’ (see above, 1). The
relation is perh. explained by th common notion of Stretching oyt the hands, hence ‘take’ or ‘hand 9g ; give’. Walde-P. 1.344. Palk-Tom iv Kretschmer, Glotta, 19.207. See also refs. under Goth. niman ‘take’ (11.13)
4. Skt. ra@- (Av. ra- ‘grant’) : rag ‘goods, riches’, rayi- ‘gift, jewel’, Lat rés ‘thing’ (early also ‘property’), Walde-P. 2.343. Ernout-M. g¢1f.
11.22 GIVE BACK, RETURN
Grk.  arrodlduyr Goth. atgiban
Lith. atiduoti, atgrazinti
NG extatpétw, drodtdw ON gefa apir Lett. atduot
Lat. —_reddere (restituere) Dan. give tilbage ChSl. vit, vitz-, ottt-dati It. restiluire, rendere Sw. giva tilbaka, dtergiva SCr.  vratiti
Fr. rendre, restiluer OE agiefan, edgiefan Boh.  vrdtiti
Sp. restiluir, devolver ME __ gife again, restore Pol. wrécié, oddaé Rum. inapota NE give back, return Russ. _ofdat’, vozvraS¢at’ Tr. aisicim Du. teruggeven Skt. pralt-da-
Nir. tabhraim, aisigim OHG argeban Av. sates
W. rhot MHG widergeben
Br. ret NHG  zuriickgeben
For the most part ‘give back’ is ex- pressed as in English by the words for ‘give’ with prefixes or adverbs meaning ‘again, back, etc.’, or by the terms equiv- alent to the English ‘return’.
1. Words belonging with verbs for ‘give’ (11.21). Grk., arodtéwut (d2ro- ‘from’, but also ‘back again’), NG azo- 6idw; Lat. reddere (whence after prendere ‘take’ VLat. *rendere > It. rendere, Fr. rendre, Sp. rendir); Goth. at-giban, etc., all the native Gme. words and phrases; Lith. atiduoti, Lett. atduot; ChSI. widati, vuizdati, ottidati, Pol. oddaé, Russ. otdat’ ; Skt. prati-da-. In the modern Celtic languages there is usually no distinction between ‘give’ and ‘give back’. So Nit. tabhraim (also with tar n-ais ‘back’), W. rhoi, Br. rei.
2. Words belonging with verbs for ‘turn’ (10.13). NG emtorpepu, yupltw; Sp. devolver; NE return; Lith. algrazinti (: gregti ‘bore’, Lett. griezt ‘turn’); SCr. vratiti, Boh. vrdtiti, Pol. wrécié, Russ. vozvraséot’ (ChSI]. loanword).
3. Lat. restituere ‘replace, restore’ (11.23), also ‘return’, as It. restituire, Fr. restituer, Sp. restituir.
Rum. tnapota, fr. tnapoi ‘back, be- hind’ (fr. apot ‘after, next’).
4. Ir. aisicim, aiscim (K. Meyer, Contrib. 69. Laws, Gloss. 45 f.), Nir. aisigim (McKenna), aiseagaim (Din- neen), deriv. (cpd.?) of ais ‘back’.
5. ME, NE restore, also ‘bring back to a previous (or original) condition, now the usual sense (11.23).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
pOSsESSION, PRO
‘ e’ are from ‘set in
Words if Behe, ‘make firm’, lace, ee erect?, ‘make better’, etc. ‘renew’, ‘raise, erect , ah
1. Grk. anoxabloTnHt, NG ae aie
```


## [2026-09-05T20:18:53.335Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Aoristwurzel\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5; echo \"---\"; grep -n \"dö-u-\\|d9u-\\|dö-  ,geben\\|,geben'  (perfektiv)\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5",
 "description": "Walde-Pokorny do-"
}
```


### [2026-09-05T20:18:53.420Z] TOOL RESULT

```
---
```


## [2026-09-05T20:18:57.674Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt; grep -n \"dádāmi\\|dadämi\\|dädämi\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -5; grep -n \"ddiiwi\\|didomi\\|dfdaifit\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -3",
 "description": "WLD Bd1 search"
}
```


### [2026-09-05T20:18:57.745Z] TOOL RESULT

```
55520
```


## [2026-09-05T20:19:04.420Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Geber\" incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt | head -8",
 "description": "WLD Bd1 Geber"
}
```


### [2026-09-05T20:19:04.466Z] TOOL RESULT

```
51399:ai. datar -, datar- „Geber‘ ; , gr. dcbicog ds., schwachstufig doryg, dorsiga,
```


## [2026-09-05T20:19:06.886Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '51380,51410p' incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt",
 "description": "WLD Bd1 do- entry context"
}
```


### [2026-09-05T20:19:06.936Z] TOOL RESULT

```
do- „geben“. 

Ai. d&duti (fut. dasyati) „er gibt“, av. dadaiti ds., ap. imper. dadcUuv, 
ptc. ditd- (enklit. *d-ta- in d-tta-, deva-tta- wie in lat. Consus , siehe Yf. 
LEWb. 2 s. v.), 3. sg. aor. adita (= gr. edozo ); arm. etu ( *e-dom = ai. a-da-m) 
j ta-mk ,,damus“, tam „do“ (Hiibschmann Arm. St. I 52, Arm. Gr. I 
496); alb. dase (*<fo-) „ich gab“ (G. Meyer BB. 8, 188, Alb. Wb. 83); gr. 
didcogu (Fut. dcoacd) „gebe“, dozog (= ai. ditd -), edozo (s. o.) do/isvai (: ai. 
da mane ); lat. do ,.gebe“ (d3-io, s. zuletzt Kieckers IF. 37, 235), damns, 
ddtis , ptc. datus vest, data „data“ usw. (= ai. ditd-), pf. dedit, alat. osk. 
deded, u. dede, redupl. Praes. (: gr. didco/u) in lat. re-ddo (* re-dido ), vestin. 



didet „dat“, pal. dida „det“, u. dirsa ,,det“ (davon fut. osk. didest „dabit“) ; 
lit. duoti ( duomi , di'iodu ) ,,geben“, lett. duot, apr. dat ds., lit. ptc. pf. act. 
daves ; aksl. dati (darn* aus * dad- mb = lit. duomi , 3. pi. dadgtz) , geben“, im- 
perfektiv dajq, dayati (: ai. ptc. med. a-ddya-mana-) ; 

ai. datar -, datar- „Geber‘ ; , gr. dcbicog ds., schwachstufig doryg, dorsiga, 
lat. dator , datrix. — - Ai. datra -, av. dadra- n. ,.Geschenk“. — Ai. *dati- 
..Schenkung, Gabe“ in dati-vara- ,,gern verteilend, freigebig“, havjyei-dati- 
,,die Opfergabe besorgend, das Darbringen des Opfers“, av. daiti- „Geben, 
Schenken, Gewahrung'', gr. dcozi-vr] (und kons. St. *do-t in dcbg) „Gabe“, 
Acooi-dsog, -<pqcov, lat. dos, -tis „Mitgift !t , lit. duotis ,,Gabe“ (nicht ganz sicber, 
s. Leskien Bild. 554), inf. duoti (s. o.), slav. *datb ,.Gabe“ z. B. in aksl. 
blagodatb „xdgis“, russ. podatb ,,Steuer‘, inf. dati , schwachstufig gr. dooig 
„Gabe“, lat. dati-o ,,das Schenken', mit Yokalschwund in Enklise ai. 
bhaga-tti- .,Gliicksgabe ‘. — 

Ai. dftna- n. „Geschenk ‘ (substantiviertes -wo-Ptc.) = lat. domim, osk.
```


## [2026-09-05T20:19:16.117Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN dose\"; grep -n \"^dose,\" KLN_1966.txt | head -2; echo \"== KLN Theodore\"; grep -n \"Theodore,\" KLN_1966.txt | head -2; echo \"== KLN Dorothy\"; grep -n \"Dorothy\" KLN_1966.txt | head -2; echo \"== KLN date\"; grep -n \"^date,  n\\.,  time\\|date,  n\\.,  a  point\" KLN_1966.txt | head -3",
 "description": "Klein English words"
}
```


### [2026-09-05T20:19:16.220Z] TOOL RESULT

```
== KLN dose
12118:dose,  n.,  amount  of  medicine  taken  at  one  time.
== KLN Theodore
38905:theirs,  possessive  pron.  —  Formed  from  prec. word  with  suff.  -s,  on  analogy  of  his. theism,  n.,  belief  in  a  personal  God.  —  Formed with  suff.  -ism  fr.  Gk.  &e6s,  ‘god’,  which  prob. stands  for  *dhes-os,  and  is  cogn.  with  Arm.  dik', ‘gods’  (which  prob.  stands  for  *dhes-es),  OI. dhisnyah ,  ‘pious,  devoted’,  L.  fanum  (for  *fas- nom),  ‘consecrated  place,  temple',  feriae  (fr.  OL. fesiae),  ‘holy  days,  festivals’,  festus,  ‘festive’;  fr. I.-E.  base  *dhes-  (=  L.  *fes-,  *fas-),  ‘holy’.  Cp. apotheosis,  atheism,  ditheism,  enthusiasm,  heno- theism,  hylotheism,  monotheism,  pantheism,  poly¬ theism,  Thecla,  theo-,  Theodore,  Thespesia, Thespian,  theurgy,  Timothy,  tritheism,  zootheism Cp.  also  fair,  fane,  feast,  Fedora, theism,  n.,  a  morbid  condition  due  to  the  exces¬ sive  use  of  tea.  —  Formed  fr.  Thea,  ’tea’,  with suff.  -ism.  Cp.  theine.
38939:Theodore,  masc.  PN.  —  L.  Theoddrus,  fr.  Gk. ©eoScopo;,  lit.  ‘gift  of  God’,  compounded  of Deo;  (see  theo-)  and  Stop ov,  ‘gift’.  See  donation and  cp.  prec.  word  and  Dorothea.  Cp.  also Fedora.
== KLN Dorothy
12008:Doll,  fern.  PN.  —  A  shortened  form  of  Dorothy.
12090:dopplerite,  n.  —  G.  Dopplerit;  named  in  1849 after  the  German  physicist  Christian  Johann Doppler  (1803-53).  The  G.  stiff,  -it  represents Gk.  -Err)  4;  see  subst.  suff.  -ite. dor,  n.,  a  droning  insect,  the  dorbeetle.  —  ME. dore,  fr.  OE.  dora,  ‘bumblebee’,  rel.  to  MLG. dorte,  ‘drone’,  from  the  I.-E.  imitative  base *dher-,  ‘to  hum,  buzz,  murmur’.  See  drone. Dora,  fem.  PN.  —  A  shortened  form  of  Doro¬ thea,  Dorothy.
== KLN date
```


## [2026-09-05T20:19:18.242Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KNT da-\"; grep -n \"dā- 'give'\\|dā-  'give'\\|give, create\\|dadātuv\" KNT.txt | head -5; echo \"== TTS dolamak\"; grep -n -i \"dolamak\\|tolgamak\\|dolama\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -5; echo \"== HUB hus\"; grep -n \"1111\\.\" HUB.txt | head -3",
 "description": "Kent, Vambery, Hübschmann"
}
```


### [2026-09-05T20:19:18.315Z] TOOL RESULT

```
== KNT da-
== TTS dolamak
10900:gen); <?or<'  =  Wirbelwind;  dolamac  =^Kreis. 
== HUB hus
3749:1111. Zd. usi heisst 1) Verstand, Einsicht, Sinn, 2) 'die
```


## [2026-09-05T20:19:25.937Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3749,3760p' HUB.txt; echo \"=== TTS\"; sed -n '10890,10905p' incoming/TTS/TTS_vambery1878_uoft_djvu.txt",
 "description": "Hübschmann 1111 and Vambery dol-"
}
```


### [2026-09-05T20:19:25.985Z] TOOL RESULT

```
1111. Zd. usi heisst 1) Verstand, Einsicht, Sinn, 2) 'die
beiden Ohren*, letzteres nach § 26 des Nirangistan
bei Darmesteter, Zend-Avesta III, p. 95, 96
Anm. 5.
1113. 1st hum zu sprechen (wegen m). Vgl. den Reim auf
bum bei Vullers.
1116. Ich halte die Etymologie fiir falsch.
1118. Man wird I = paz. i doch an ap. hya, hya an-
kniipfen miissen. Der Stamm ya- liegt altpersisch
nur in Adv. wie yada vor. Im Paz. lautet das Re-
lativum ya- (in ya-m, ya-t, ya-s, ya-sctn) = ap. hya,
hya (da ya- zu ja- geworden ware).
=== TTS
Cirkel,  Versammlung;  fio^awa  ==  Wirbelwind. 

osni.  clolaj  =  Cirkel,  Bereich,  in  Betreff,  wegen,  (menden  do- 
foj=  wegen  meiner;  vgl.  arab.  rfatV  =  wegen  mit  daire  =^ 
Kreis);  dolanmak  =  herumgehen,  umgeben  oder  umi'ingt 
sein;  doiandlrniak  =^hetvügen  (eigentl.  jemand  herumgehen 
lassen);  dolasmalc  =  umhergehen;  dolcmk  =  a,ni  Umwegen, 
krumm. 

az.  dolaj  —  Umgehung ,  Kreis  (dolajini  aZmaÄ=  jemand  umrin- 
gen); <?or<'  =  Wirbelwind;  dolamac  =^Kreis. 

alt.    io^M  =  sich  drehen. 

jak.  tul  =  umgehen;  fu^a  =  Umkreis ,  rundherum;  ^tt/a?«  — um- 
geben, abrunden.
```


## [2026-09-05T20:19:28.005Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dā- 'to give\\|'to give, create'\\|dā-, dadā\" KNT.txt | head -5; grep -n \"dadātuv\\|dadâtuv\" KNT.txt | head -5; grep -n \"^dā-\" KNT.txt | head -5",
 "description": "Kent Old Persian da-"
}
```


### [2026-09-05T20:19:28.069Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T20:19:35.601Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"give, create\\|'give'\" KNT.txt | head -8; echo \"== bagadata\"; grep -n -i \"bagadāta\\|Bagadata\\|baga-dāta\" KNT.txt | head -5",
 "description": "Kent give / Bagadata"
}
```


### [2026-09-05T20:19:35.660Z] TOOL RESULT

```
== bagadata
```


## [2026-09-05T20:19:39.217Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dadātuv\\|dadatuv\\|dadâtuv\\|dadaituv\" KNT.txt | head; echo ---; grep -n \"dā-\" KNT.txt | head -8; wc -l KNT.txt",
 "description": "Kent search 2"
}
```


### [2026-09-05T20:19:39.278Z] TOOL RESULT

```
4105:28 : Katpatuka : Sparda : Yauna : бака : {уау : pa 29 radraya :Skudra : Yauna : takabarà : Рибу 30 à : Каўуя : Maciya : Karka : дану : D 31 drayavaus : xšāyaðiya : Auramazda : ya 32 & : avaina : imàm : bümim : yaudatem : 33 pasávadim : manā : frábara : mam : 28d 34 уадуат :akunaus : adam : x&àyatiya 85 :amiy.:.vasnd : Auramazdahd : a 30 damSim : gafava : niyašādayam : tyašā 37 m : adam : afaham : ava : akunava : yabā : mam: 38 Ката : aha : yadipatiy : maniyáhaty : t 39 ya :ciyakaram.: dha : ava : dahyiva 40 :tyà : Darayavaus : xSayafiya 4] :adáraya : patikarà : didiy : tyaiy : g 42 àfum : baratiy : vadā : xSnasahy : 43 adataiy : azdà : bavatiy : Pārsahyā : 44 martiyahyà : diraiy : artes : pa 45 ràgmatà : adataiy : azdà : bavāti 46 y :Parsa :martiya : dürayapiy : hacà : Pa 47 rsà : partaram : patiyajata : 6itiy : Da 48 rayavauS : xSdyafiya : aita : буа : karta 49 m :ava :visam : vasnà : Auramazdaha : ak 50 unavam : Àuramazdá(ma)iy : upastàm : aba 51 ra : yütà : kartam : akunavam : mém:A 52 uramazdà : pàtuv : аса : gasid : utama 53 iy : vitam : uta : imàm : dahyàum : aita : ada 54 m : Auramazdam : jadiyámiy : aitama 55 iy : Auramazda : dadatuv : 56 martiya : hyà : Auramazdah 57 & : framana : hauvtaty : gas 58 tā : ma : adaya : раб : .. 50 {уаш : ristim : mà 60 : avarada : mà : stabava Nores то DNa: The text of DNa now rests upon the photographs of F. Stolze (Persepolis: Berlin, 1882) and of А. Sevruguin (accessible in Wb. Grab, Plates 2-3). The following readings, which either replace older wrong readings or confirm older doubted readings, are assured by the photographs; the restorations agree with the length of the gaps: ^? framatà- | ram; ™ düraiapty; 9 patiyazsayaty; 9^? aba[ra]- | ha; * adáraiya (for nor- malization, ef. $48); 25 haumavargá ; * akunava; * yadi- patiy : maniy|ühaty : t]- | ya (for -haiy, cf. note on DB 4.39); * {aha} Wb.; “ no space for [mand] before ga6um; £ a[va]dà; **düraiy; 4 dárayapiy; ® Auramazda(ma)ty, with omission of те; 6 ga(sta], see Lex. s.v. (not sero+). Other textual notes: 3° [ра]- | radraya, after other oc- currences, see Lex. s.v.; not [ta]- | radraya. *^* Put- (älyä, after other occurrences, see Lex. svt; not Put[i]yà. 2 yauldatim] ВЕ, sée Lex: ву. yaud-; hardly yaufdinim],
---
1649:avadà but avada-ía, avada-Sim, avada-&S, but avadā-sim DB 3.74.
5617:paié- vb. ‘cut, engrave, adorn’: Av. paésa- ‘adornment’, Skt. pisdtz ‘cuts, adorns’, Gk. токіћоѕ ‘variegated’, OCS pisati ‘to write’, pIE *peik-, cf. Lt. pingit ‘embroiders, paints’ (Wb. AfOF 7.42). Cf. also nipišti-, parsiyd-, Paišiyđwwādā-, pisa-. аріа imf. DSf 54 (§211; cf. Konig, Burgbau 72). [ар #} уа] imf. pass. ($220) DB 4.91 (JAOS 62.268). [pjisia nsf. past pte. pass. ($242.1) DSf 42 (Bv. BSLP 30.1.62; Konig, Burgbau 71; not dista with Hz. Apī 121-5].
5868 KNT.txt
```


## [2026-09-05T20:19:46.583Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vb. ‘give\\|vb. 'give\\|‘give, make\" KNT.txt | head -5",
 "description": "Kent lexicon da- entry"
}
```


### [2026-09-05T20:19:46.637Z] TOOL RESULT

```
5494:Idà- vb. ‘give’: Av. Skt. dà-, Gk. бош, Lt. dai ‘gives’, dónum ‘gift’, pIE *dó- (862, 576.11). dadátus іту. (§209, $237.II) DPd 28; DNa 55; XPh 60.
```


## [2026-09-05T20:19:50.446Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5494,5498p' KNT.txt",
 "description": "Kent da- 1 and 2"
}
```


### [2026-09-05T20:19:50.515Z] TOOL RESULT

```
Idà- vb. ‘give’: Av. Skt. dà-, Gk. бош, Lt. dai ‘gives’, dónum ‘gift’, pIE *dó- (862, 576.11). dadátus іту. (§209, $237.II) DPd 28; DNa 55; XPh 60.
*dà- vb. ‘put, make, create’: Av. dá-, Skt.
dhà-, Gk. rifnu, Lt. јеси ‘made’, NEng. do, deed, pIE *dhe-. See also wadd-, data-,ddna-. айайй imf. (§209, 5228.1) DPd 8; DNb 1, 2; DSe 2°, 3°, 3f, 4. ada aor. ($62, S76.TIT, $122, $218.II, $228.IT) DNa 2, 3 bis, 4; DSf 1f^, 2 bis, 3, 9; DSp 2°; DSt 2°, 3, 3f°, 4°; DZe 1, 2 ter; DE 3, 4, 5, 6; XPa 1f, 2, 3 bis; XPb 3, 4, 5, 6; ХРе 2 bis, 3 bis; XPd 2, 3, 4 bis; XPf 2, 3 bis, 4; XPh 2 bis, 3 bis; XE 3f, 5, 5f, 6; XV 3, 4 bis, 5; A!P2 2°, 3°, 4°, 4f°; А?Не 2, 3, 4 bis; A?Pa 2, 3, 4 bis.
daiy, see -di-.
dawa- sb. (false) divinity, demon’ (cf. Hz. RHRel. 43:.32-7; AMY 8:74-5, ApI 126-30): Av.
```


## [2026-09-05T20:20:17.006Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13280,13300p' BRT.txt | grep -n \"^7[0-9][0-9]$\\|^ *7[0-9][0-9] *$\" ; awk 'NR>=13270 && NR<=13310 && /^[0-9]{3}$/ {print NR\": \"$0}' BRT.txt; echo \"--- daθvah context\"; awk 'NR>=12630 && NR<=12660 && /^[0-9]{3}$/ {print NR\": \"$0}' BRT.txt",
 "description": "Bartholomae column numbers"
}
```


### [2026-09-05T20:20:20.153Z] TOOL RESULT

```
9:727
13288: 727
--- daθvah context
12657: 679
```


## [2026-09-05T20:20:36.657Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -6 61498ad8dd7f3082.txt; grep -n \"to give\" 61498ad8dd7f3082.txt | head -5",
 "description": "Check PIE deh3 page fetched"
}
```


### [2026-09-05T20:20:36.712Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh₃-
FETCHED: 2026-09-05T20:15:24Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/deh₃- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/deh₃- - Wiktionary, the free dictionary 
145: to give
```


## [2026-09-05T20:28:09.969Z] TOOL CALL #78: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build139.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\nroot0 = {\n \"entry\": 0,\n \"root\": \"Dô 2\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *deh₃- (Pokorny 'dō- : də-') 'to give'; the 'create' half of Nourai's gloss belongs to the separate root PIE *dʰeh₁- 'to put, place, make' (Pokorny 235)\",\n \"note\": \"Pokorny IEW 223 heads the article 'dō- : də-, auch dō-u- : dəu- : du- „geben“ (perfektiv), Aoristwurzel mit sekundärem Präsens di-dō-mi, Nominalbildungen: do-no-m, dō-ro-m, dō-ti-s, də-ti-s „Gabe“, dō-ter- „Geber“', so the language label (Indo-European) and the 'to give' half of the gloss are exact, and the page number is right. 'Create' is not part of this root. Kent's Old Persian lexicon separates '1dā- vb. „give“: Av. Skt. dā-, Gk. δίδωμι, Lt. dat „gives“, dōnum „gift“, pIE *dō-' from '2dā- vb. „put, make, create“: Av. dā-, Skt. dhā-, Gk. τίθημι, Lt. fēcī „made“, NEng. do, deed, pIE *dhē-'; Bartholomae's Avestan dātar- likewise has sense 1 'der gibt' = Skt. dātar- and sense 2 'Schöpfer' = Skt. dhātār-. Because Proto-Iranian merged *dʰ into d, Avestan and Middle Persian dā- covers both roots, and Nourai's chart consequently mixes them: nodes 1, 3 (dādan, dāšan, pādāš, Baghdād), 8, 9 and the whole Latin/Greek/English side descend from *deh₃-, whereas dādār 'creator' (node 2), dāθuš/Day (nodes 4–5) belong to *dʰeh₁-. The chart is therefore right about the shape of the root and about most of its arrows, but the root box merges two Indo-European roots that only Iranian merged.\",\n \"note_fa\": \"جعبهٔ ریشه همان ریشهٔ هندواروپایی آغازین *deh₃- «دادن» است؛ پوکورنی در صفحهٔ ۲۲۳ آن را چنین آورده: «dō- : də- ... „geben“ ... dō-ter- „Geber“»، پس برچسب زبان، شمارهٔ صفحه و معنای «دادن» درست است. اما نیمهٔ دوم معنا، یعنی «آفریدن»، از آنِ ریشهٔ دیگری است: *dʰeh₁- «نهادن، ساختن، آفریدن» (پوکورنی ۲۳۵). در سنسکریت این دو از هم جدا مانده‌اند (dádāti در برابر dádhāti) و کنت هم در واژه‌نامهٔ پارسی باستان ¹dā- «دادن» را از ²dā- «نهادن، آفریدن» جدا کرده است؛ ولی در ایرانی باستان *dʰ به d بدل شد و هر دو ریشه در اوستایی و فارسی میانه به dā- رسیدند. از همین رو نورایی ناخواسته دو ریشه را در یک نمودار آورده است: «دادن، داشن، پاداش، بغداد» و شاخهٔ لاتینی و یونانی از *deh₃- اند، ولی «دادار» و «دی» و «دَثوش» از *dʰeh₁-. ادعای نورایی در کلیت پذیرفتنی است، اما با این تفکیک.\",\n \"sources\": [W+\"Reconstruction:Proto-Indo-European/deh₃-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:223\", \"status\": \"supports\", \"note\": \"POK_01.txt line 3198 (leaf 232-235 = IEW pp. 223-226): 'dō- : də-, auch dō-u- : dəu- : du- „geben“ (perfektiv), Aoristwurzel mit sekundärem Präsens di-dō-mi, Nominalbildungen: do-no-m, dō-ro-m, dō-ti-s, də-ti-s „Gabe“, dō-ter- „Geber“ ...' — exactly the root box, except that Pokorny glosses it 'geben' only, never 'schaffen'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I p. 814 f. (WLD_Bd1 djvu line 51380 ff.)\", \"stance\": \"supports\", \"note\": \"'dō- „geben“. Ai. dádāti (fut. dāsyati) „er gibt“, av. dadāiti ds., ap. imper. dadātuv ... gr. δίδωμι ... lat. do „gebe“' — Pokorny 223 is the abridgement of this article; again 'geben' only.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985, d-list (AHD_watkins1985.txt line 404)\", \"stance\": \"supports\", \"note\": \"'dō-. To give. Contracted from *doə-. 1. Zero-grade form *də- in Latin dare, to give ... 2. Suffixed form *dō-no- in Latin dōnum, gift ... 4. Reduplicated form *di-dō- in Greek didonai, to give: DOSE ... [Pok. dō- 223.]' — same root, same page reference, gloss 'To give'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. dō- (IEC.txt line 2349 ff.)\", \"stance\": \"supports\", \"note\": \"'dō- (dṓdmi, dídōmi, fut. dōsiō) „give“. WP I, 814. Skt. dádāmi ...; OPer. dā-; Av. daδāmi; Per. cf. inf. dādan; Arm. tam ...; Gk. dídōmi ...; Lat. do' — Mann puts Persian dādan under the same root.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 11.21 GIVE (SYN.txt line 18995 ff.)\", \"stance\": \"supports\", \"note\": \"Buck's GIVE table lists 'Skt. dā-, Av. dā-' beside Lat. dare, Gk. dídōmi, Lith. duoti, ChSl. dati, and notes 'Hitt. da- „take“ = IE *do- „give“'.\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon s.v. dā- (KNT.txt line 5494-5495)\", \"stance\": \"partial\", \"note\": \"'1dā- vb. „give“: Av. Skt. dā-, Gk. δίδωμι, Lt. dat „gives“, dōnum „gift“, pIE *dō-. dadātuv imv. DPd 28; DNa 55; XPh 60.' followed by '2dā- vb. „put, make, create“: Av. dā-, Skt. dhā- ... pIE *dhē-.' Kent supports the 'give' root but contradicts the 'create' half of the root box, which is a separate PIE root.\"}\n ],\n \"nodes\": []\n}\n\nn = root0[\"nodes\"]\n\nn.append({\n \"id\": 1, \"lang\": \"Avestan / Sanskrit\", \"words\": \"dâ 4; dâtar\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both forms are real and correctly placed. The PIE reduplicated present *dé-deh₃-ti gave Proto-Indo-Iranian *dádaHti, whence Sanskrit dádāti 'gives', Avestan dadāiti and Old Persian imv. dadātuv 'let him give' (Darius, DNa 55: 'aitamaiy Auramazdā dadātuv'); Nourai's citation form 'dā' is the root as Sanskrit and Avestan grammarians cite it. The agent noun *deh₃-tér- 'giver' gave Skt. dātár-, Av. dātar-, Gk. δωτήρ, Lat. dator. The second gloss 'God' is right only through a second layer: Bartholomae's Avestan article dātar- : dāθr- has (1) 'der, die gibt, schenkt' = Skt. dātar-, and (2) 'der schaffend hervorbringt, Schöpfer', used of Ahura Mazdā and equated by him with Skt. dhātār- — i.e. the divine sense comes from the homophonous root *dʰeh₁-, which Iranian could no longer keep apart from *deh₃-.\",\n \"derivation_fa\": \"هر دو صورت درست‌اند. ستاک هندواروپایی *deh₃- با پیشوندِ دوگان‌سازی به *dé-deh₃-ti رسید، در هندوایرانی آغازین *dádaHti شد و از آن سنسکریت dádāti، اوستایی dadāiti و پارسی باستان dadātuv (سنگ‌نبشتهٔ داریوش، DNa سطر ۵۵) پدید آمد؛ صورتِ «dā» که نورایی آورده همان ریشه به شیوهٔ دستورنویسان است. نامِ فاعلیِ *deh₃-tér- «دهنده» در سنسکریت dātár-، در اوستایی dātar- و در یونانی dōtḗr و لاتین dator بازتاب یافته است. اما معنای دومِ «خدا» تنها از راهِ لایه‌ای دیگر درست است: بارتولومه در ستون ۷۲۷ برای dātar- دو معنا آورده، یکی «دهنده» (هم‌ارز سنسکریت dātar-) و دیگری «آفریدگار» که آن را هم‌ارز سنسکریت dhātār- می‌داند، یعنی از ریشهٔ *dʰeh₁- که در ایرانی با *deh₃- یکی شده است. ادعای نورایی درست است، با همین تفکیک.\",\n \"sources\": [W+\"%D8%AF%D8%A7%D8%AF%D9%86\", W+\"Reconstruction:Proto-Indo-European/deh₃-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:223,225\", \"status\": \"supports\", \"note\": \"IEW 223 (POK_01.txt line 3198): 'Ai. dá-dā́ti ... „gibt“, av. dadāiti ds., apers. Imp. dadātuv „er soll geben“'; IEW 225 (line 3216 ff.): 'Nominalbildungen: ai. dātar-, dātā́r- „Geber“, gr. δώτωρ, δωτήρ ds. ... lat. dator, datrix.' Both cited pages carry exactly the forms of this node.\"},\n   {\"ref\": \"BQT:121\", \"status\": \"not_checked\", \"note\": \"Borhan-e Qate' vols 1-2 have no page-mapped local scan (tools/ref_page.py: 'no scan of BQT covers printed page 121'); the vol.-1 OCR (BQT_v1_pages.txt line 12181) does show the headword «اسفندیار» in the region Nourai cites, but Mo'in's Latin-script etymological footnotes are lost in that OCR, so the page could not be read.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 727 f., s.v. dātar- (BRT.txt lines 13288-13301)\", \"stance\": \"supports\", \"note\": \"'j., g. dātar- : dāθr- m., j. dāθrī- f. 1) „der, die gibt, schenkt“ ... 2) „der schaffend hervorbringt, Schöpfer“ von AhM. und den AmSp. ... Zum V. dā-. — ai. (zu 1) dātar- m., (zu 2) dhātār- m.; np. dādār „Schöpfer“. — Pü.: dātār'.\"},\n   {\"src\": \"KNT\", \"where\": \"Lexicon s.v. 1dā- (KNT.txt line 5494); text DNa 55 (line 4105)\", \"stance\": \"supports\", \"note\": \"'1dā- vb. „give“ ... dadātuv imv. DPd 28; DNa 55; XPh 60'; the DNa text itself reads 'aitamaiy Auramazdā dadātuv'.\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. I 814 f. (WLD_Bd1 djvu line 51380, 51399)\", \"stance\": \"supports\", \"note\": \"'Ai. dádāti ... av. dadāiti ds., ap. imper. dadātuv' and 'ai. dātar-, dātā́r- „Geber“; gr. δώτωρ ds. ... lat. dator, datrix.'\"}\n ]\n})\n\nn.append({\n \"id\": 2, \"lang\": \"Pahlavi\", \"words\": \"dâtan; dâdâr; dâhišn; paiti-dâhišn\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"MacKenzie's Concise Pahlavi Dictionary has 'dādan, dah- [YHBWN-tn' < Aram. yhb; d'tn', dh-] 1. give; 2. create. ~išn [dh(y)šn'] giving, donation; creation. dādār [d'tʾl] creator' — i.e. exactly Nourai's dātan, dāhišn, dādār, the Book-Pahlavi infinitive dā-tan (present stem dah- < OIr. *da-da-) written with the Aramaic ideogram YHBWN. Nyberg's glossary adds the semantic split: 'dātan ... A. to give ... B. 1. to put, to place ... 2. to create ... Av. OP dā-; MPrth dʾdn dh-; NP dādan dih-' and 'dātār the Creator, epithet of Ohurmazd'. 'paiti-dāhišn' is the pre-form of MP pādāšn: Horn no. 265 'pādāš, pādes „Vergeltung“ ... phlv. pātdah(i)šn (paiti + dah(i)šn), pāz. pādāišn, pādāšn'. As at node 1, dādan/dahišn 'give' continue *deh₃- while dādār 'creator' continues *dʰeh₁-tḗr (Wiktionary: MP dʾtʾl < Proto-Iranian *daHtā́ < PIE *dʰeh₁-tḗr).\",\n \"derivation_fa\": \"مکنزی در فرهنگ کوچک پهلوی می‌آورد: «dādan, dah- ۱. دادن ۲. آفریدن؛ dahišn دهش، بخشش؛ آفرینش؛ dādār آفریدگار» — یعنی درست همان صورت‌هایی که نورایی آورده است؛ مصدر پهلوی dā-tan با ستاک حالِ dah- (از ایرانی باستان *da-da-) و با هُزوارشِ آرامیِ YHBWN نوشته می‌شد. نیبرگ نیز در واژه‌نامهٔ خود همین دو معنا را جدا کرده («الف: دادن؛ ب: نهادن، آفریدن») و dātār را «آفریدگار، لقب اورمزد» دانسته است. صورت paiti-dāhišn نیای «پاداشن» است؛ هرن در شمارهٔ ۲۶۵ می‌گوید: «pādāš ... پهلوی pātdah(i)šn (paiti + dah(i)šn)». تنها نکته آنکه dādār از ریشهٔ *dʰeh₁-tḗr است نه *deh₃-. ادعای نورایی در این گره درست است.\",\n \"sources\": [W+\"%D8%AF%D8%A7%D8%AF%D8%A7%D8%B1\", W+\"%D9%BE%D8%A7%D8%AF%D8%A7%D8%B4\"],\n \"ref_check\": [\n   {\"ref\": \"HRN:61\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p. 61 no. 265 (HRN.txt leaf 82): 'pādāš, pādes (Vis und Rāmin) „Vergeltung“, pādast, pādošn, phlv. pātdah(i)šn (paiti + dah(i)šn), pāz. pādāišn, pādāšn „Vergeltung“ ... Vergl. np. dašen (No. 528)' — literally Nourai's 'paiti-dâhišn : reward, given back'.\"},\n   {\"ref\": \"HRN:115\", \"status\": \"supports\", \"note\": \"Horn p. 115 (leaf 136) nos. 518-521: '519. dādār „Schöpfer“. aw. dātar- „Schöpfer“; phlv. dātār, pāz. dādar; ai. dhātār-.' and '520. dāden „geben“ ... ap. dā-, dadātuv „geben“; aw. dā-, dadąmi „geben“; phlv. dātan; ai. dā-, dádāti „geben“' — with '521. (2) dāden „machen, setzen“ ... ap. dā- „machen, setzen“' kept apart.\"},\n   {\"ref\": \"NYB:56\", \"status\": \"not_found\", \"note\": \"In the local scan of Nyberg's Manual II (leaf = printed + 8) printed p. 56 is the Pahlavi c- section (cāštan, catrang, cē). The entries Nourai wants — 'dātan ... A. to give ... B. 2. to create ... Av. OP (711 sqq.) 1dā-' and 'dātār the Creator' — stand a few pages later (leaves 68 and 72 = printed ~60 and ~64). The content supports the arrow; only the page number is off by a few pages (or Nourai used a different printing).\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 24 f. s.v. dādan (PHD.txt line 306)\", \"stance\": \"supports\", \"note\": \"'dādan, dah- [YHBWN-tn' < A √yhb; d'tn', dh- | M d'dn, (dy-), P dh-, N ~, dih-] 1. give; 2. create. ~išn [dh(y)šn'] giving, donation; creation. dādār [d'tʾl | N ~] creator.' and, p. 65, 'pādāšn [p'td'šn' | M p'd'šyn, N pādāš] reward, retribution'.\"},\n   {\"src\": \"NYB\", \"where\": \"Manual of Pahlavi II, glossary s.vv. dātan, dātār, dahišn (leaves 68-72)\", \"stance\": \"supports\", \"note\": \"'dātan [YHBWN-tn'; d'tn'] dah- ... A. to give ... B. 1. to put, to place ... 2. to create ... Av. OP (711 sqq.) 1dā-; MPrth d'dn dh-; NP dādan dih-'; 'dahišn [dhšn'] 1. creation, the act of creating ... From dātan'; 'dātār [d'tʾl] the Creator ... epithet of Ohurmazd'.\"}\n ]\n})\n\nn.append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"dâdan «دادن»; deh 3 «ده ۳ ( روزی ده )»; Bağdâd «بغداد»; dâdâr «دادار»; dâšan «داشن ( دهش ، دَشت ۲ )»; pâdâš «پاداش ( پاداشت ، پاداشن )»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"دادن dādan continues MP dādan (present dah-) < OP dadātuv, PIE *dé-deh₃-ti; the New Persian present stem deh- (ده) of that verb is what stands in روزی‌ده rūzī-deh 'giver of daily bread', so Nourai's 'deh 3 : giver' is the bound present stem, not an independent noun. دادار dādār < MP dādār 'creator' (Wiktionary: MP dʾtʾl < PIr. *daHtā́ < PIE *dʰeh₁-tḗr). داشن dāšan 'gift' < MP dāšn [dʾšn'] (Wiktionary: 'From Middle Persian dʾšyn'), beside the parallel formation دهش dahiš < MP dahišn; دشت 2 is the same word with the common NP -šn > -št. پاداش pādāš < MP pādāšn 'reward, retribution' = pād- 'back, counter-' (OIr. *pati-) + dāšn/dahišn 'giving', with the variants پاداشن and پاداشت preserving the older -šn/-št; Horn no. 265 spells the Pahlavi pātdah(i)šn, exactly the parent node. بغداد Baghdād is Middle Persian bag-dād 'god-given' (baga- 'god' + dāta- 'given'), the pre-Islamic village name taken over for al-Manṣūr's round city of 762 CE and thence into Arabic بَغْدَاد; Wiktionary derives English Baghdad 'from Arabic baḡdād, from Classical Persian baġdād', a doublet of Skt. Bhagadatta. The chart's own NOTE reports TAD:12, and al-Unaysi's page really does say 'بغداد - فارسي مركب من باغ أي بستان وداد' ('Persian, compounded of bāgh, i.e. garden, and dād'); that is a mediaeval folk etymology which no modern authority accepts — the name is attested in Babylonian/Aramaic before any Persian 'garden of justice' could be meant.\",\n \"derivation_fa\": \"«دادن» دنبالهٔ فارسی میانهٔ dādan (ستاک حال dah-) است، از پارسی باستان dadātuv و ریشهٔ *dé-deh₃-ti؛ «ده» در «روزی‌ده» همان ستاک حالِ همین فعل است، نه اسمی جداگانه. «دادار» از فارسی میانهٔ dādār «آفریدگار» است که ویکی‌واژه آن را از ایرانی آغازین *daHtā́ و هندواروپایی *dʰeh₁-tḗr می‌گیرد. «داشن» از پهلوی dāšn «بخشش» است و «دهش» صورتِ دیگرِ همان مفهوم از dahišn؛ «دشت ۲» نیز همان واژه با تبدیل ‑شن به ‑شت است. «پاداش» از پهلوی pādāšn است: پیشوندِ pād- «باز، ضدّ» (ایرانی باستان *pati-) + dāšn/dahišn «دهش»؛ گونه‌های «پاداشن» و «پاداشت» صورت کهن‌تر را نگه داشته‌اند و هرن (شمارهٔ ۲۶۵) صورت پهلوی را pātdah(i)šn می‌نویسد — درست همان گرهِ مادر. «بغداد» از فارسی میانهٔ bag-dād «خدای‌داده» است (baga «خدا» + dāta «داده»)، نام دهی پیش از اسلام که منصور عباسی در سال ۷۶۲ میلادی بر شهر گِردِ خود نهاد و از آن‌جا به عربی رفت. یادداشتِ نمودار به نقل از «تفسیر الالفاظ الدخیله» درست نقل شده است (در آن کتاب آمده «بغداد ـ فارسي مركب من باغ أي بستان وداد»)، اما این ریشه‌شناسی عامیانه است و پژوهش امروزی آن را نمی‌پذیرد. رویِ‌هم‌رفته ادعای نورایی در این گره درست است.\",\n \"sources\": [W+\"%D8%AF%D8%A7%D8%AF%D9%86\", W+\"%D8%AF%D8%A7%D8%B4%D9%86\", W+\"%D9%BE%D8%A7%D8%AF%D8%A7%D8%B4\", W+\"Baghdad\"],\n \"ref_check\": [\n   {\"ref\": \"FSF:169\", \"status\": \"partial\", \"note\": \"Noushin's Vazhe-namak really has this cluster: FSF_pages.txt leaf 132 prints 'پاداش = پاداشن = داشن ... پهلوی: پات دهمیشن pātdahišn ... مرکب از پات = ضد، مخالف، برگشت + داشن', with Shahnameh citations ('بد و نیک را هر دو پاداشن است'). The scan's printed-page offset is not established, so the leaf could not be matched to the cited p. 169; the content is exactly Nourai's claim.\"},\n   {\"ref\": \"BQT:289,815\", \"status\": \"not_checked\", \"note\": \"Borhan-e Qate' vols 1-2 have no page-mapped local scan (tools/ref_page.py: 'no scan of BQT covers printed page 289 / 815'), and the archive.org OCR of those volumes drops Mo'in's Latin-script footnotes, so the two cited pages could not be read.\"},\n   {\"ref\": \"SNS:295\", \"status\": \"not_checked\", \"note\": \"The Shāyast nē Shāyast glossary scan is 242 leaves with no established page offset and very poor OCR; a printed p. 295 could not be located. (Its dāsr entry, used at node 9, was found by transliteration search.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"nos. 265 (p. 61), 518-520 (p. 115), 528 (p. 117 f.)\", \"stance\": \"supports\", \"note\": \"'528. dašen „Geschenk, Gabe“. g. dāšn. phlv. dah(i)šn; vergl. padāšn (No. 265)'; '520. (1) dāden „geben“, Praes. dih-em, dād „Gabe“ ... phlv. dātan' — Horn's dih-em is Nourai's 'deh 3'.\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie s.vv. dāšn, pādāšn, dādār\", \"stance\": \"supports\", \"note\": \"'dāšn [d”šn' | M d’s(y)n] gift'; 'pādāšn [p'td'šn' | M p'd'šyn, N pādāš] reward, retribution'; 'dādār [d'tʾl | N ~] creator' — every Persian word of this node has its Middle Persian ancestor here.\"},\n   {\"src\": \"TAD\", \"where\": \"al-Unaysi s.v. بغداد (TAD.txt line 510)\", \"stance\": \"contradicts\", \"note\": \"'بغداد - فارسي مركب من باغ أي بستان وداد' — the chart's NOTE quotes this source correctly, but the derivation itself ('garden of justice') is a folk etymology; modern scholarship keeps bag-dāta 'god-given'.\"}\n ]\n})\n\nn.append({\n \"id\": 4, \"lang\": \"Avestan\", \"words\": \"dathuš; spento-dâto\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Both Avestan forms are real. dāθuš- is the nominative of the perfect participle daθvah- : daduš-/dāθuš- 'der geschaffen hat, Schöpfer; schöpferisch' (Bartholomae col. 679), used of Ahura Mazdā, and it is this word that names the month and the day Day (Bartholomae's note on the month: 'Aw. daθušō „(Monat des) Schöpfers“, mp. daδu, np. dai'). spəntō.dāta- is the personal name 'given/created by the Holy One (Spənta Ārmaiti)', second member dāta- 'given'. The reservation is the same as at the root box: dāθuš- belongs to Avestan dā- 'to create' = PIE *dʰeh₁- (Kent's 2dā-), not to *deh₃- 'to give', while the -dāta of spəntō.dāta- is the participle of the 'give' root; so the two words of this node hang from two different Indo-European roots, and only the second is under the right root box.\",\n \"derivation_fa\": \"هر دو صورتِ اوستایی واقعی‌اند. dāθuš- نهادیِ صفت مفعولیِ کاملِ daθvah- : daduš-/dāθuš- «آنکه آفریده است، آفریدگار» است (بارتولومه، ستون ۶۷۹) و لقبِ اهورامزدا؛ همین واژه است که نام ماه و روزِ «دی» از آن آمده — بارتولومه در حاشیهٔ نام ماه‌ها می‌نویسد: «اوستایی daθušō „(ماهِ) آفریدگار“، پهلوی daδu، فارسی دی». صورت spəntō.dāta- نیز نامِ خاصِ «دادهٔ سپند (سپندارمذ)» است که جزء دومش dāta- «داده» است. تنها ایراد همان ایرادِ جعبهٔ ریشه است: dāθuš- به ریشهٔ اوستاییِ dā- «آفریدن» یعنی *dʰeh₁- بازمی‌گردد (²dā- در واژه‌نامهٔ کنت) نه به *deh₃- «دادن»؛ حال آنکه ‑dāta در spəntō.dāta- از همان ریشهٔ «دادن» است. پس این گره با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%AF%DB%8C%D8%A7%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:121,907\", \"status\": \"not_checked\", \"note\": \"Both pages fall in Borhan-e Qate' vols 1-2, for which there is no page-mapped local scan ('no scan of BQT covers printed page 121 / 907'); the vol.-1 OCR does show Borhan's headword «اسفندیار» (BQT_v1_pages.txt line 12181: 'اسفندیار بر وزن و معنی اسفنددار است که نام پسر گشتاسب باشد') in the cited region, but Mo'in's Latin-script etymological footnote — the part that would carry spəntō.dāta- — is lost in that OCR.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"col. 679 s.v. daθvah- (BRT.txt line 12655); month-name note (line 4430)\", \"stance\": \"supports\", \"note\": \"'j. daθvah- : daduš-, dāθuš- Adj. „der geschaffen hat, Schöpfer; schöpferisch“'; and 'Aw. daθušō „(Monat des) Schöpfers“, mp. daδu (angebl. dēn), np. dai.'\"},\n   {\"src\": \"KNT\", \"where\": \"Kent, Lexicon s.v. 2dā- (KNT.txt line 5495)\", \"stance\": \"partial\", \"note\": \"'2dā- vb. „put, make, create“: Av. dā-, Skt. dhā-, Gk. τίθημι, Lt. fēcī „made“, NEng. do, deed, pIE *dhē-' — the 'creator' words belong to this root, not to Nourai's Dô 2.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"s.v. اسفندیار\", \"stance\": \"supports\", \"note\": \"'From Middle Persian /spandadāt/, in turn derived from Avestan spəntōδāta, literally „given by Amesha Spenta“.'\"}\n ]\n})\n\nn.append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"day «دی ۲»; Esfandîyâr «اسفندیار»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"دی Day is the direct continuation of the Avestan genitive daθušō '(month/day) of the Creator': Av. dāθuš- > MP Day, which MacKenzie glosses 'Day [ddw' | M dyy, N ~] Creator; cal. 10th month; 8th, 15th, 23rd days' — precisely Nourai's 'creator, the tenth month'. The Zoroastrian calendar named the tenth month and the 8th, 15th and 23rd days after Ahura Mazdā under this epithet, which is why Persian still distinguishes دی‌بآذر، دی‌بمهر، دی‌بدین. اسفندیار continues MP Spandadāt < Av. spəntō.dāta- 'given by the Holy One', with the regular Iranian shift of intervocalic -d- of the second member to -y-/-r- in the New Persian name (spandadāt > *spandayār > esfandiyār); Mo'in's footnote in Borhan-e Qate' p. 2396 states this explicitly: 'اما درخصوص اسفندیار باید گفت که آن از شکل قدیم‌تر -dāta آمده و در فارسی «ر» بجای «د» نشسته است'. The chart's NOTE ('see root Ghei 1 for another possible derivation of day') is the alternative that takes دی 'yesterday, past' from *dyew-/*ǰi- — that is a different, homonymous word (Mo'in lists it separately as «دِی [په.] روز گذشته»), so both entries can stand side by side.\",\n \"derivation_fa\": \"«دی» یکسره دنبالهٔ اوستایی daθušō «(ماه/روزِ) آفریدگار» است: اوستایی dāθuš- > پهلوی Day، که مکنزی چنین معنی می‌کند: «Day: آفریدگار؛ ماه دهم گاه‌شمار؛ روزهای هشتم، پانزدهم و بیست‌وسوم» — دقیقاً همان که نورایی آورده است. در گاه‌شمار زردشتی ماه دهم و آن سه روز به همین لقبِ اهورامزدا نامیده شدند و از همین‌جاست «دی‌بآذر، دی‌بمهر، دی‌بدین». «اسفندیار» از فارسی میانهٔ Spandadāt و آن از اوستایی spəntō.dāta- «دادهٔ سپند» است؛ معین در حاشیهٔ برهان قاطع (ص ۲۳۹۶) خود می‌نویسد: «اما درخصوص اسفندیار باید گفت که آن از شکل قدیم‌تر ‑dāta آمده و در فارسی «ر» بجای «د» نشسته است». دربارهٔ یادداشتِ نمودار («ریشهٔ Ghei 1 را برای اشتقاق دیگرِ دی ببینید») باید گفت آن «دی» به معنای «دیروز، گذشته» واژه‌ای جداگانه و هم‌آواست (معین آن را جدا آورده: «دِی [په.] روز گذشته»). پس ادعای نورایی درست است.\",\n \"sources\": [\"https://abadis.ir/fatofa/دی/\", W+\"%D8%A7%D8%B3%D9%81%D9%86%D8%AF%DB%8C%D8%A7%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1588\", \"status\": \"partial\", \"note\": \"Mo'in's Farhang-e Farsi is only available online in the form that drops the print edition's Latin-script etymologies; the entry itself matches ('دی (دِ یْ) (اِ.) ۱- دهمین ماه هر سال شمسی. ۲- نامِ روزهای هشتم، پانزدهم و بیست و سوم هر ماه شمسی', abadis.ir/fatofa/دی), and Mo'in keeps the homonym 'دِی [په.] روز گذشته' apart, but the cited page 1588 of the printed edition could not be verified.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 25 s.v. Day (PHD.txt line 310)\", \"stance\": \"supports\", \"note\": \"'Day [ddw' | M dyy, N ~] Creator; cal. 10th month; 8th, 15th, 23rd days.'\"},\n   {\"src\": \"BRT\", \"where\": \"Bartholomae, month-name note (BRT.txt line 4430)\", \"stance\": \"supports\", \"note\": \"'Dez.-Jan. ... Aw. daθušō „(Monat des) Schöpfers“, mp. daδu (angebl. dēn), np. dai.'\"},\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote in Borhan-e Qate' p. 2396 (ocr/BQT/2396.png)\", \"stance\": \"supports\", \"note\": \"'اما درخصوص اسفندیار باید گفت که آن از شکل قدیمتر ‑داته dāta آمده و درفارسی «ر» بجای «د» نشسته است.'\"}\n ]\n})\n\nn.append({\n \"id\": 6, \"lang\": \"Avestan\", \"words\": \"dâta 2; ŭši-dâta\",\n \"verdict\": \"disputed\",\n \"derivation\": \"Avestan dāta- 'given' (past participle of dā-) is of course real, but the glosses 'giver, owner' are not Bartholomae's, and no Avestan compound uši-dāta- 'gifted with intelligence' is attested — Bartholomae's uši- compounds are uši.dam-/uši.darəna- (a mountain name) and uši.darəna-type formations, not *uši-dāta-. The compound is a reconstruction made by Darmesteter to explain Persian هوشیار, and Nourai's own cited page rejects it: Mo'in's footnote at Borhan-e Qate' 2396 reports Darmesteter's uši + dāta- 'given intelligence' and then quotes Horn: 'ولی طبیعةً از طریق علم‌الاصوات این فرض غیرممکن است، بیشتر احتمال داده می‌شود که کلمات مذکور از *-dāra- اشتقاق یافته باشند' ('but phonetically this assumption is impossible; the words in question are more probably derived from *-dāra-'), the Pahlavi inscriptional forms confirming -dār. Modern scholarship follows Horn: the second member of هوشیار، بختیار، شهریار is OIr. *-dāra- 'holding, possessing' (PIE *dʰer-), not *-dāta- 'given'.\",\n \"derivation_fa\": \"صفت مفعولی اوستایی dāta- «داده» البته واقعی است، اما معناهای «دهنده، دارنده» از بارتولومه نیست، و ترکیب اوستایی *uši-dāta- «برخوردار از هوش» در متون اوستایی گواهی نشده است؛ آنچه بارتولومه دارد uši.dam-/uši.darəna- (نام کوه) است. این ترکیب ساختهٔ دارمستتر برای توضیح «هوشیار» است و خودِ مأخذی که نورایی آورده آن را رد می‌کند: معین در حاشیهٔ برهان قاطع ص ۲۳۹۶ نخست قول دارمستتر را نقل می‌کند و سپس از هرن می‌آورد: «ولی طبیعةً از طریق علم‌الاصوات این فرض غیرممکن است، بیشتر احتمال داده می‌شود که کلمات مذکور از ‑dāra* اشتقاق یافته باشند»، و صورت‌های کتیبه‌ای پهلوی را گواه می‌گیرد. پژوهش امروزی نیز همین را می‌گوید: جزء دومِ «هوشیار، بختیار، شهریار» همان *-dāra- «دارنده» (از ریشهٔ *dʰer-) است نه *-dāta- «داده». پس این گره را باید رد شده دانست.\",\n \"sources\": [W+\"%D9%87%D9%88%D8%B4%DB%8C%D8%A7%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:2396\", \"status\": \"contradicts\", \"note\": \"The cited page is indeed the هوشیار entry (rendered as ocr/BQT/2396.png, BQT vol. 4 pdf p. 479), and Mo'in's footnote gives Darmesteter's uši + dāta- reading only in order to reject it: '... اوستایی dāta- بمعنی داده و آفریده است، پس اگر جزو دوم از ريشة مذکور باشد، این کلمه بمعنی هوش داده است ... هرن پس از نقل قول دارمستتر در اشتقاق بختیار، هوشیار، دامیار، شهریار گوید: «ولی طبيعةً ازطریق علم الاصوات این فرض غیرممکن است، بیشتر احتمال داده میشود که کلمات مذکور از -dāra* اشتقاق یافته باشند»'.\"},\n   {\"ref\": \"HRN:248\", \"status\": \"partial\", \"note\": \"Horn p. 248 (HRN.txt leaf 269) no. 1111: '(1) hōš, huš „Verstand, Klugheit“, hušyār „verständig“. aw. uši „die beiden Ohren“ ... phlv. hōš bezw. ōš „Verstand“ ... Die abgeleitete Bedeutung „Verstand“ aus der ursprünglichen „Ohr“ ist erst mittelpersisch.' Horn supports the uši- element but offers no -dāta-; elsewhere (quoted by Mo'in) he explicitly rejects the -dāta- analysis.\"}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"s.v. uši.dam-, uši.darəna- (BRT.txt lines 6348, 8721)\", \"stance\": \"silent\", \"note\": \"Bartholomae's uši- compounds are 'j. uši.dam-, uši-dam- m. „Name eines Gebirgs“' and 'usi.darəna-'; there is no entry *uši-dāta- 'gifted with intelligence' in the Altiranisches Wörterbuch.\"},\n   {\"src\": \"HUB\", \"where\": \"Persische Studien, note on Horn no. 1111 (HUB.txt line 3749)\", \"stance\": \"partial\", \"note\": \"'1111. Zd. usi heisst 1) Verstand, Einsicht, Sinn, 2) „die beiden Ohren“' — Hübschmann confirms the first element only.\"}\n ]\n})\n\nn.append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"hŭšyâr «هوشیار»\",\n \"verdict\": \"disputed\",\n \"derivation\": \"هوشیار is real and means 'aware, intelligent', but it does not come from a compound with dāta- 'given'. Wiktionary: 'From Middle Persian ōšyār „conscious“, a pre-Middle Persian compound equivalent to Middle Persian ōš „consciousness, intellect“ + dār „having“, with a phonetic shift *ušiy-dar > *ušiy-yar > *ušiyar > ōšyār'; the first element is OP ušiy 'consciousness' (Av. uši, PIE *h₂ows- 'ear'), the second Proto-Iranian *dar- 'to hold' < PIE *dʰer-. This is Horn's analysis, and it is the reason Persian has the same -yār in بختیار 'fortunate' and شهریار 'sovereign' (< *xšaθra-dāra- 'realm-holding'), where 'given' makes no sense. So the word does belong to the chart's first element (uši 'intelligence', root Ôus 1) but not to Dô 2 at all.\",\n \"derivation_fa\": \"«هوشیار» واژه‌ای واقعی و به معنای «آگاه، باهوش» است، اما از ترکیبی با dāta- «داده» نیامده. ویکی‌واژه می‌نویسد: از فارسی میانهٔ ōšyār، ترکیبی پیش از فارسی میانه برابر با ōš «هوش» + dār «دارنده»، با این دگرگونی آوایی: *ušiy-dar > *ušiy-yar > *ušiyar > ōšyār؛ جزء نخست از پارسی باستان ušiy «هوش» (اوستایی uši، هندواروپایی *h₂ows- «گوش») و جزء دوم از ایرانی آغازین *dar- «داشتن» (هندواروپایی *dʰer-). این همان تحلیلِ هرن است و گواهش آنکه همین ‑یار در «بختیار» و «شهریار» (از *xšaθra-dāra- «دارندهٔ شهر/شهریاری») هست که در آن‌ها معنای «داده» بی‌معناست. پس این واژه به جزء نخستِ نمودار (هوش) مربوط است، ولی به ریشهٔ «دادن» هیچ ربطی ندارد؛ پژوهش امروزی ادعای نورایی را رد می‌کند.\",\n \"sources\": [W+\"%D9%87%D9%88%D8%B4%DB%8C%D8%A7%D8%B1\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference of its own; the parent node's BQT:2396 was checked and contradicts the derivation (see node 6).\"}\n ],\n \"consulted\": [\n   {\"src\": \"BQT\", \"where\": \"Mo'in's footnote s.v. هوشیار, Borhan-e Qate' p. 2396 (ocr/BQT/2396.png)\", \"stance\": \"contradicts\", \"note\": \"'هوشیار - تلفظ قدیم hōšyār ... پهلوی hōšyār ... بقول دارمستتر از: هوش + یار ... هرن ... گوید: «ولی طبيعةً ازطریق علم الاصوات این فرض غیرممکن است، بیشتر احتمال داده میشود که کلمات مذکور از -dāra* اشتقاق یافته باشند» چنانکه کلمهٔ پهلوی [شهردار] در کتیبه‌های پهلوی آنرا تأیید میکند.'\"},\n   {\"src\": \"HRN\", \"where\": \"Grundriss p. 248 no. 1111\", \"stance\": \"partial\", \"note\": \"'(1) hōš, huš „Verstand, Klugheit“, hušyār „verständig“. aw. uši ... phlv. hōš bezw. ōš „Verstand“' — Horn files hušyār under hōš, with no 'given' element.\"},\n   {\"src\": \"Wiktionary\", \"where\": \"s.v. هوشیار\", \"stance\": \"contradicts\", \"note\": \"'From Middle Persian ōšyār ... equivalent to ōš „consciousness, intellect“ + dār „having“, with a phonetic shift *ušiy-dar > *ušiy-yar > *ušiyar > ōšyār ... the second component is from Proto-Iranian *dar-, from PIE *dʰer- „to hold“.'\"}\n ]\n})\n\nn.append({\n \"id\": 8, \"lang\": \"Avestan\", \"words\": \"dâthra\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Avestan dāθra- n. 'gift' is the instrument/result noun *deh₃-tro-m of the root, the exact counterpart of Sanskrit dātrá- n. 'gift'; Pokorny prints the pair on the very page Nourai cites: 'Ai. dātrá-, av. dāθra- n. „Geschenk“' (IEW 225). Iranian *-tr- regularly appears as -θr- after a long vowel (cf. Av. puθra- : Skt. putra-). Bartholomae's article (col. 732, as cited by Tavoosi) has the same word.\",\n \"derivation_fa\": \"صورت اوستایی dāθra- «بخشش، دهش» همان نامِ ابزاری/برآیندی *deh₃-tro-m از این ریشه است و هم‌ارزِ دقیقِ سنسکریت dātrá- «بخشش»؛ پوکورنی این جفت را درست در همان صفحه‌ای آورده که نورایی ارجاع داده است: «Ai. dātrá-, av. dāθra- n. „Geschenk“» (IEW ۲۲۵). خوشهٔ *-tr- ایرانی پس از واکهٔ بلند به‑ θr‑ بدل می‌شود (سنجید: اوستایی puθra- در برابر سنسکریت putra-). بارتولومه نیز همین واژه را در ستون ۷۳۲ آورده است. ادعای نورایی درست است.\",\n \"sources\": [\"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/deh₃-\"],\n \"ref_check\": [\n   {\"ref\": \"POK:225\", \"status\": \"supports\", \"note\": \"IEW 225 (POK_01.txt line 3216 ff., the leaf carrying the printed '225'): 'Nominalbildungen: ai. dātar-, dātā́r- „Geber“ ... — Ai. dātrá-, av. dāθra- n. „Geschenk“.' Word, language and gloss as drawn.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. I 814 f. (WLD_Bd1 djvu line 51399)\", \"stance\": \"supports\", \"note\": \"'Ai. dātra-, av. dāθra- n. „Geschenk“.'\"},\n   {\"src\": \"SNS\", \"where\": \"Tavoosi, glossary s.v. dasr (SNS.txt lines 16393-16397)\", \"stance\": \"supports\", \"note\": \"The entry sets 'dasr' beside 'dāθra-' and 'dātra-' with a reference to Bartholomae col. 732 — the Avestan word is the source of the Pahlavi one.\"}\n ]\n})\n\nn.append({\n \"id\": 9, \"lang\": \"Pahlavi\", \"words\": \"dâsr\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Book Pahlavi dās(a)r [d'sl] 'gift, reward' is the regular Middle Persian outcome of Av. dāθra-: intervocalic -θr- yields MP -s(a)r (as in Av. puθra- > MP pus(ar)), the spelling <d'sl> being read dāsr/dāsar. MacKenzie prints the equation himself: 'dās°r [d'sl = Av. dāθra-] gift, reward', and lists it in his English index under both 'gift' and 'reward'. The word is rare and mostly Zoroastrian-literary; it did not survive into New Persian, where the parallel dāšn (داشن) took over.\",\n \"derivation_fa\": \"صورت پهلویِ کتابی dās(a)r با نگارشِ <d'sl> «بخشش، پاداش» برآیندِ قاعده‌مندِ اوستایی dāθra- است: خوشهٔ ‑θr‑ میان‌واکه‌ای در فارسی میانه به ‑s(a)r بدل می‌شود (چنانکه اوستایی puθra- به pus(ar) رسید). مکنزی خودِ این برابری را می‌آورد: «dās°r [d'sl = اوستایی dāθra-] بخشش، پاداش» و در نمایهٔ انگلیسی‌اش نیز آن را زیر «gift» و «reward» آورده است. این واژه کمیاب و بیشتر ادبی‑زردشتی است و به فارسی نو نرسید؛ در فارسی نو صورتِ هم‌ریشهٔ «داشن» جای آن را گرفت. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"SNS:298\", \"status\": \"partial\", \"note\": \"Tavoosi's Shāyast nē Shāyast glossary does carry the entry (SNS.txt lines 16393-16397): 'dasr ... dāθra- ... dātra- (Bartholomae 732) ... bahr ... dasran', i.e. exactly Nourai's Pahlavi word explained from the Avestan one. The scan (242 leaves) has no established printed-page offset, so the cited p. 298 itself could not be located.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie p. 25 s.v. dās°r (PHD.txt line 310); index pp. 'gift', 'reward'\", \"stance\": \"supports\", \"note\": \"'dās°r [d'sl = Av. dāθra-] gift, reward'; index: 'gift āyaft, dāšn, pārag, dās°r' and 'reward mizd, pādāšn, dās°r'.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (d- section, leaves 68-72)\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary of the texts he edits has dahišn, dāšn-related items and dātār but no dāsr entry — the word simply does not occur in his corpus.\"}\n ]\n})\n\nn.append({\n \"id\": 10, \"lang\": \"Latin\", \"words\": \"dare; donum\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Latin dō, dare 'to give' continues the zero-grade *də- of the root (Pokorny: 'lat. dō, das, dat, damus (*də-mos), datis, dant ... dedī, datum, dare „gebe, gewähre“'), with the perfect dedī showing the old reduplication and the participle datus = Skt. ditá-/Gk. δοτός. dōnum 'gift' is the substantivised *dō-no- participle, identical with Skt. dāná- n. 'gift' and Oscan dunum. Watkins files precisely these two forms under dō- and hangs the English words on them.\",\n \"derivation_fa\": \"لاتینِ dō, dare «دادن» دنبالهٔ درجهٔ صفرِ ریشه، یعنی *də-، است؛ پوکورنی می‌آورد: «lat. dō, das, dat, damus (*də-mos), datis, dant ... dedī, datum, dāre „gebe, gewähre“»، که در آن ماضیِ dedī همان دوگان‌سازیِ کهن را نگه داشته و صفت مفعولیِ datus هم‌ارزِ سنسکریت ditá- و یونانی dotós است. واژهٔ dōnum «هدیه» نیز اسم‌شدهٔ صفتِ *dō-no- است و درست برابرِ سنسکریت dāná- و اسکیِ dunum. واتکینز در پیوستِ ریشه‌های هندواروپاییِ فرهنگ امریکن هریتیج همین دو صورت را زیر ریشهٔ dō- آورده است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dō- (AHD_watkins1985.txt line 404): 'dō-. To give ... 1. Zero-grade form *də- in Latin dare, to give ... 2. Suffixed form *dō-no- in Latin dōnum, gift (> dōnāre, to present, forgive) ... [Pok. dō- 223.]' — both Latin words, under this root.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 223-225 (POK_01.txt lines 3207, 3222)\", \"stance\": \"supports\", \"note\": \"'lat. dō, das, dat, dāmus (*də-mōs) ... dedī, dātum, dāre „gebe, gewähre“'; 'Ai. dāna- n. „Geschenk“ (substantiviertes -no-Partiz.) = lat. dōnum, osk. dunum ds.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. do- (IEC.txt line 2349)\", \"stance\": \"supports\", \"note\": \"'do- (theme of dídomi, dómi, and cf. dotós) ... Lat. do, donum, etc.'\"}\n ]\n})\n\nn.append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"add; data; edit; rent; tradition; surrender; date 2 : time; donate; pardon\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Every one of these is a Latin loan built on dare or dōnum, and Watkins's dō- article lists them as such: add < Lat. addere (ad- + dare); data/datum < neuter pl. of datus; edit < ēdere/ēditio 'give out, publish'; rent and surrender < Vulgar Latin *rendere for reddere 'give back' (Old French rendre, sur+rendre); tradition (and traitor, treason) < trādere 'hand over' (trans- + dare); date 'point in time' from the Roman dating formula 'data (epistula) Romae', 'given (letter) at Rome'; donate < dōnāre; pardon < Late Latin perdōnāre 'to grant freely' (Old French pardoner). All come into English through Old French or directly from Latin between the 13th and 17th centuries.\",\n \"derivation_fa\": \"هر یک از این واژه‌ها وام‌واژه‌ای لاتینی است که بر پایهٔ dare یا dōnum ساخته شده و واتکینز همه را زیر ریشهٔ dō- برشمرده است: add از addere (ad- + dare)؛ data/datum جمعِ خنثای datus؛ edit از ēdere «بیرون دادن، نشر کردن»؛ rent و surrender از *rendere لاتینی عامیانه به‌جای reddere «بازدادن» (فرانسهٔ کهن rendre و sur-rendre)؛ tradition از trādere «سپردن» (trans + dare)؛ date «تاریخ» از قالبِ نامه‌نگاری رومی data (epistula) Romae «(نامهٔ) داده‌شده در رم»؛ donate از dōnāre؛ و pardon از perdōnāre لاتینی متأخر (فرانسهٔ کهن pardoner). این واژه‌ها میان سدهٔ سیزدهم تا هفدهم میلادی، یا از راه فرانسهٔ کهن یا یکسره از لاتین، به انگلیسی رسیده‌اند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference; the parent's AHD citation covers it (see consulted).\"}\n ],\n \"consulted\": [\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dō- (AHD_watkins1985.txt line 404)\", \"stance\": \"supports\", \"note\": \"'... in Latin dare, to give: DADO, DATE, DATIVE, DATUM, DIE²; ADD, BETRAY, EDITION, PERDITION, RENDER, (RENT¹), (SURRENDER), TRADITION, (TRAITOR), (TREASON), VEND. 2. ... Latin dōnum, gift (> dōnāre ...): DONATION, DONATIVE, DONOR; CONDONE, PARDON.' — every word of the node except 'data' is named, and DATUM covers that.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein, Comprehensive Etym. Dict., s.vv. add, date, donate, pardon\", \"stance\": \"supports\", \"note\": \"Klein derives them all from Latin dare/dōnāre compounds; e.g. his 'dose' article (p. 473 f.) and the Latin-dare family are cross-referenced under 'donation'.\"}\n ]\n})\n\nn.append({\n \"id\": 12, \"lang\": \"Greek\", \"words\": \"didonai; dôron\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Greek δίδωμι / inf. διδόναι is the inherited reduplicated present *di-deh₃-mi, the exact match of Skt. dádāmi and Av. dadāmi; δῶρον 'gift' is the *dō-ro-m formation with the -ro- suffix in passive value (Pokorny compares Lat. clā-rus), corresponding to Old Church Slavonic darъ and Armenian tur. Both stand in Pokorny's article on the pages Nourai cites for the root.\",\n \"derivation_fa\": \"یونانی dídōmi و مصدرِ didónai همان ستاکِ حالِ دوگان‌شدهٔ موروثی *di-deh₃-mi است و درست برابرِ سنسکریت dádāmi و اوستایی dadāmi؛ واژهٔ dôron «هدیه» نیز ساختِ *dō-ro-m است با پسوندِ ‑ro‑ در معنای مفعولی (پوکورنی آن را با clā-rus لاتینی می‌سنجد) و هم‌ارزِ اسلاوی کهن darъ و ارمنی tur. هر دو صورت در همان صفحه‌های پوکورنی که نورایی برای ریشه ارجاع داده آمده‌اند. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"Watkins 1985 s.v. dō- (line 404): '4. Reduplicated form *di-dō- in Greek didonai, to give: DOSE; ANECDOTE, ANTIDOTE, APODOSIS, EPIDOTE.' (Watkins does not list δῶρον, because no English word reaches it through his corpus; Pokorny does.)\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"IEW 224-225 (POK_01.txt lines 3200, 3222)\", \"stance\": \"supports\", \"note\": \"'gr. δίδωμι „gebe“, Aor. ἔδωκα ... Infin. hom. δόμεναι'; 'gr. δῶρον „Geschenk“ (-ro- in pass. Geltung, vgl. z. B. clā-rus), aksl. darъ „Gabe“ ..., arm. tur ds.'\"},\n   {\"src\": \"IEC\", \"where\": \"Mann s.v. dō- (IEC.txt line 2349 ff.)\", \"stance\": \"supports\", \"note\": \"'dō- (dṓdmi, dídōmi, fut. dōsiō) „give“ ... Gk. dídōmi, fut. dṓsō.'\"}\n ]\n})\n\nn.append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"dose; Dorothy; Theodore\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"dose came through Late Latin dosis from Greek δόσις 'a giving, a portion given (of medicine)', the *də-ti-s noun of the same root, entering English via French dose in the 15th century; Dorothy and Theodore are the two orders of the same Greek compound of θεός 'god' and δῶρον 'gift' — Θεόδωρος 'gift of God' (Lat. Theodōrus) and Δωροθέα 'gift of God' (Lat. Dorothea, whence Dorothy), both spread as Christian saints' names. Klein states this expressly for Theodore.\",\n \"derivation_fa\": \"واژهٔ dose از راهِ لاتینِ متأخرِ dosis از یونانی dósis «دادن، بهرهٔ داده‌شده (از دارو)» آمده که همان اسمِ *də-ti-s از این ریشه است و در سدهٔ پانزدهم از فرانسه به انگلیسی رسید. «دوروتی» و «تئودور» نیز دو صورتِ وارونهٔ یک ترکیبِ یونانی‌اند از theós «خدا» و dôron «هدیه»: Theódōros «هدیهٔ خدا» (لاتین Theodōrus) و Dōrothéa (لاتین Dorothea، از آن Dorothy)، که هر دو همچون نامِ قدیسانِ مسیحی گسترش یافتند. کلاین همین را دربارهٔ Theodore به‌صراحت می‌گوید. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node; Klein and Watkins were consulted instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein s.v. Theodore (KLN_1966.txt line 38939, leaf carrying pp. 1607 f.) and s.v. dose (line 12118)\", \"stance\": \"supports\", \"note\": \"'Theodore, masc. PN. — L. Theodōrus, fr. Gk. Θεόδωρος, lit. „gift of God“, compounded of θεός (see theo-) and δῶρον, „gift“. See donation and cp. ... Dorothea.'; 'dose, n., amount of medicine taken at one time.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dō- (line 404)\", \"stance\": \"supports\", \"note\": \"'Reduplicated form *di-dō- in Greek didonai, to give: DOSE; ANECDOTE, ANTIDOTE ...' — dose is filed under this root.\"}\n ]\n})\n\n# ---------------- entry 1 ----------------\n\ne1 = {\n \"entry\": 1,\n \"root\": \"Dolmak\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Ottoman/Turkish dolamak 'to twist, wind, wrap around' (Proto-Turkic *tolga-), beside the distinct dolmak 'to be filled, become full' (Proto-Turkic *tōl-)\",\n \"note\": \"The root box names the wrong one of two Turkish verbs. Turkish dolmak is intransitive 'to be filled, to become full' (Ottoman طولمق, Proto-Turkic *tōl-); 'to wind, wrap' is dolamak (Ottoman طولامق, Proto-Turkic *tolga-, cf. Karakhanid tolɣāmāk). The two are separate stems in the standard handbooks. That matters for the chart, because its two branches actually hang from the two different verbs: the garment (dolama/dolaman > German Dolman > French > English dolman) is from dolamak 'wind, wrap', exactly as AHD and Klein say, whereas Persian دلمه dolme 'stuffed vine leaves' is Turkish dolma 'stuffed thing', from dolmak 'to be filled'. So Nourai's tree is right in substance for each branch but mislabels the head verb and its meaning, and lets dolme descend from the garment word.\",\n \"note_fa\": \"جعبهٔ ریشه نامِ نادرست را از میان دو فعلِ ترکی برگزیده است. dolmak در ترکی فعلی لازم است به معنای «پر شدن» (ترکی عثمانی طولمق، ترکی آغازین *tōl-)، و آنچه «پیچیدن، دورِ چیزی تاباندن» معنی می‌دهد dolamak است (ترکی عثمانی طولامق، ترکی آغازین *tolga-، سنجید: قراخانی tolɣāmāk). این تفکیک برای نمودار مهم است، چون دو شاخهٔ آن در واقع از دو فعل جدا می‌آیند: نامِ جامه (dolama/dolaman ← آلمانی Dolman ← فرانسه ← انگلیسی dolman) از dolamak «پیچیدن» است — چنانکه فرهنگ امریکن هریتیج و کلاین می‌گویند — ولی «دلمهٔ» فارسی از dolma ترکی «چیزِ پرشده» و آن از dolmak «پر شدن» است. پس ساختار نمودار در هر شاخه درست است، اما نامِ فعلِ سرشاخه و معنای آن جابه‌جا شده و «دلمه» زیرِ نامِ جامه نشسته است؛ ادعای نورایی با این اصلاح پذیرفتنی است.\",\n \"sources\": [W+\"dolamak\", W+\"dolmak\", W+\"dolma\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:389\", \"status\": \"partial\", \"note\": \"AHD's own dolman entry (checked in the current online edition, ahdictionary.com search 'dolman'; the local copy of AHD is only Watkins's IE-roots appendix, which has no Turkic material) reads: '... from Ottoman Turkish dolama, robe ... French dolman, from German Dolman, ultimately, probably via Hungarian dolmány, from Ottoman Turkish dolama, from Ottoman Turkish dolamak, to twist, wind, wrap around; akin to Turkic tolğamaq.' It supports the route but gives dolamak, not dolmak, as the source verb.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"s.vv. dolamak, dolmak\", \"stance\": \"contradicts\", \"note\": \"'dolamak ... Inherited from Ottoman Turkish طولامق (dolamak, „to twist, wind round about a thing“), from Proto-Turkic *tolga-'; 'dolmak ... Inherited from Ottoman Turkish طولمق („to fill, become full; swell“), from Proto-Turkic *tōl-.'\"},\n   {\"src\": \"TTS\", \"where\": \"Vámbéry, Etym. Wb. der turko-tatarischen Sprachen (TTS djvu line 10890 ff.)\", \"stance\": \"supports\", \"note\": \"Vámbéry groups the 'turn/wind' family: 'osm. dolaj = Cirkel, Bereich ... dolanmak = herumgehen, umgeben ... dolašmak = umhergehen ... az. dolamac = Kreis; alt. tolu = sich drehen; jak. tul = umgehen' — i.e. the stem behind dolama(n), separate from 'to fill'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 530 (LKT.txt line 1355 ff.)\", \"stance\": \"supports\", \"note\": \"'530. Tk. dolama: „Roter Tuchmantel, den die Janitscharen als Paradeanzug trugen“; hieraus rum. dulama ... russ. doloman, dolman ... poln. dolman „kurzer Husarenmantel“ ... dtsch. Dolman, frz. doliman, dolman „Husarenjacke“.' Lokotsch's headword is dolama, and his no. 531 is separately 'Tk. doldur-: doldurmak „füllen“'.\"}\n ],\n \"nodes\": []\n}\n\nm = e1[\"nodes\"]\n\nm.append({\n \"id\": 1, \"lang\": \"Turkish\", \"words\": \"dolman\",\n \"verdict\": \"plausible\",\n \"derivation\": \"The Turkish word is dolama (also dolaman) 'a long cassock-like robe with narrow sleeves', the deverbal noun of dolamak 'to wind, wrap around' — literally 'the wrapping'; Nourai's citation form 'dolman' is the European shape of the word, not the Ottoman one. Lokotsch heads his entry 'Tk. dolama „Roter Tuchmantel, den die Janitscharen als Paradeanzug trugen“' and Klein 'Turk. dolaman, the red cloak of the Janizaries'; AHD gives 'Ottoman Turkish dolama, robe, loose cassocklike garment with narrow sleeves worn by janissaries'. The gloss 'wrapping, cover, coating' is thus right in sense, the form is not.\",\n \"derivation_fa\": \"صورت ترکی این واژه dolama (و گونهٔ dolaman) است به معنای «ردایی بلند و آستین‌تنگ»، اسمِ برگرفته از فعلِ dolamak «پیچیدن، دورِ چیزی تاباندن»، یعنی به‌راستی «پیچیده، پوشش». آنچه نورایی نوشته (dolman) صورتِ اروپایی واژه است نه صورتِ عثمانی آن. لوکوچ سرواژهٔ خود را «ترکی dolama: ردای ماهوتی سرخ که ینی‌چری‌ها در رژه می‌پوشیدند» می‌آورد، کلاین «ترکی dolaman، ردای سرخ ینی‌چری‌ها»، و فرهنگ امریکن هریتیج «ترکی عثمانی dolama، ردایی گشاد و آستین‌تنگ». پس معنا درست است ولی صورت واژه نه؛ این گره با احتیاط پذیرفتنی است.\",\n \"sources\": [W+\"dolamak\", W+\"dolman\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:389\", \"status\": \"partial\", \"note\": \"AHD (online 5th ed., checked because the local AHD file is only the IE-roots appendix): '... from Ottoman Turkish dolama, robe, loose cassocklike garment with narrow sleeves worn by janissaries ... from Ottoman Turkish dolamak, to twist, wind, wrap around'. Supports the meaning and the position in the tree; the Turkish form is dolama, not dolman.\"}\n ],\n \"consulted\": [\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 530 (LKT.txt line 1355 ff.)\", \"stance\": \"partial\", \"note\": \"'530. Tk. dolama: „Roter Tuchmantel, den die Janitscharen als Paradeanzug trugen“' — headword dolama.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein p. 473 s.v. dolman (KLN_1966.txt leaf 260, which carries printed pp. 473-475)\", \"stance\": \"partial\", \"note\": \"'dolman ... — F., fr. G. Dolman, fr. Hung. dolmány, fr. Turk. dolaman, the red cloak of the Janizaries.'\"}\n ]\n})\n\nm.append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"dolmeh «دلمه»\",\n \"verdict\": \"plausible\",\n \"derivation\": \"دلمه is indeed a Turkic loan in Persian, but it is Turkish dolma 'stuffed thing' — the deverbal noun of dolmak 'to be filled' — not a derivative of the garment word dolama/dolman: 'From Greek ντολμάς or its etymon, Turkish dolma, from Ottoman Turkish طولمه (dolma), from طولمق (dolmak, „to get full, be filled“) ... the word literally means „stuffed thing“' (Wiktionary s.v. dolma); the Persian entry says 'Borrowed from Turkic, cf. Azerbaijani dolma, Turkish dolma'. The word entered Persian with the Turkic-Azeri cuisine of the Safavid period, and Mo'in defines it exactly as Nourai does ('نوعی خوراک ... که در برگ مو، برگ کلم و غیره پیچند و پزند'). So the node belongs under the root verb dolmak, one step to the side of where the chart puts it.\",\n \"derivation_fa\": \"«دلمه» به‌راستی وام‌واژه‌ای ترکی در فارسی است، اما از dolma «چیزِ پرشده» می‌آید — اسمِ برگرفته از dolmak «پر شدن» — نه از نامِ جامه (dolama/dolman). ویکی‌واژه می‌نویسد: «ترکی dolma، از ترکی عثمانی طولمه، از طولمق „پر شدن“ ... واژه لفظاً یعنی چیزِ پرشده»، و در مدخل فارسی: «وام‌گرفته از ترکی، سنجید: آذربایجانی dolma». این واژه با آشپزی ترکی‑آذری در دورهٔ صفوی به فارسی راه یافت و معین آن را درست همان‌گونه که نورایی آورده تعریف می‌کند: «نوعی خوراک ... که در برگ مو، برگ کلم و غیره پیچند و پزند». پس این گره باید یک پله بالاتر، زیرِ خودِ فعلِ dolmak، بنشیند؛ با این اصلاح پذیرفتنی است.\",\n \"sources\": [W+\"dolma\", W+\"%D8%AF%D9%84%D9%85%D9%87\", \"https://abadis.ir/fatofa/دلمه/\"],\n \"ref_check\": [\n   {\"ref\": \"MON:1554\", \"status\": \"partial\", \"note\": \"Mo'in's entry matches the gloss — '(دُ مَ یا مِ) (اِ.) نوعی خوراک مرکب از برنج، گوشت چرخ کرده، لپه، سبزی مخصوص و غیره که در برگ مو، برگ کلم و غیره پیچند و پزند' (abadis.ir/fatofa/دلمه, section فرهنگ معین) — but the online text of Mo'in omits the print edition's origin tag, and the 6-vol. printed p. 1554 could not be checked; the 2-vol. abridgement (MON_part2.txt line 25330) likewise carries the definition without an etymology.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"s.vv. دلمه, dolma\", \"stance\": \"partial\", \"note\": \"'Borrowed from Turkic, cf. Azerbaijani dolma, Turkish dolma'; 'Turkish dolma, from Ottoman Turkish طولمه (dolma), from طولمق (dolmak, „to get full, be filled“) ... literally „stuffed thing“' — a sibling of dolama, not its child.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch nos. 530-531 (LKT.txt line 1355 ff.)\", \"stance\": \"partial\", \"note\": \"Lokotsch keeps the garment (no. 530 dolama) and the 'fill' verb (no. 531 'Tk. doldur-: doldurmak „füllen“') in separate entries.\"}\n ]\n})\n\nm.append({\n \"id\": 3, \"lang\": \"German\", \"words\": \"dolman\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"German Dolman (also Doliman) 'hussar's braided jacket' was taken over from Ottoman dolama through Hungarian dolmány during the long Habsburg-Ottoman border wars of the 16th-17th centuries; the hussar uniform carried it into every European army. Klein: 'F. dolman, fr. G. Dolman, fr. Hung. dolmány, fr. Turk. dolaman'; AHD: 'French dolman, from German Dolman, ultimately, probably via Hungarian dolmány, from Ottoman Turkish dolama'. Nourai's chart omits the Hungarian link, which both authorities insert.\",\n \"derivation_fa\": \"آلمانی Dolman (و گونهٔ Doliman) «نیم‌تنهٔ قیطان‌دوزیِ سواره‌نظام» در جنگ‌های دراز مرزیِ هابسبورگ و عثمانی در سده‌های شانزدهم و هفدهم، از راهِ مجاری dolmány از dolama عثمانی گرفته شده و با یونیفرمِ هوسارها به همهٔ ارتش‌های اروپایی رفته است. کلاین می‌نویسد: «فرانسه dolman، از آلمانی Dolman، از مجاری dolmány، از ترکی dolaman»؛ و فرهنگ امریکن هریتیج: «فرانسه dolman، از آلمانی Dolman، احتمالاً از راه مجاری dolmány، از ترکی عثمانی dolama». نمودارِ نورایی حلقهٔ مجاری را انداخته است، وگرنه درست است.\",\n \"sources\": [W+\"dolman\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:389\", \"status\": \"supports\", \"note\": \"AHD s.v. dolman (online 5th ed.): '... French dolman, from German Dolman, ultimately, probably via Hungarian dolmány, from Ottoman Turkish dolama ...' — the German link is exactly as drawn, with Hungarian as an additional step.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p. 473 s.v. dolman\", \"stance\": \"supports\", \"note\": \"'— F., fr. G. Dolman, fr. Hung. dolmány, fr. Turk. dolaman, the red cloak of the Janizaries.'\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 530\", \"stance\": \"supports\", \"note\": \"'... poln. dolman „kurzer Husarenmantel“, čech. doloman, dolman „ungarischer Pelzrock“; dtsch. Dolman, frz. doliman, dolman „Husarenjacke“.'\"}\n ]\n})\n\nm.append({\n \"id\": 4, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through node: French doliman / dolman, the immediate source of the English word. French had doliman for the Turkish robe from the 16th century (through travellers' accounts) and dolman for the hussar jacket from the German in the 18th-19th century; English borrowed both strands from French.\",\n \"derivation_fa\": \"گرهِ واسطه و بی‌واژه: فرانسهٔ doliman / dolman، سرچشمهٔ بی‌واسطهٔ واژهٔ انگلیسی. فرانسه از سدهٔ شانزدهم صورت doliman را برای ردای ترکی از سفرنامه‌ها گرفته بود و در سده‌های هجدهم و نوزدهم صورت dolman را برای نیم‌تنهٔ هوسارها از آلمانی؛ انگلیسی هر دو رشته را از فرانسه وام گرفت. این حلقه درست است.\",\n \"sources\": [W+\"dolman\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"No reference on the node; covered by the AHD and Klein citations of the neighbouring nodes.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein p. 473 s.v. dolman\", \"stance\": \"supports\", \"note\": \"'dolman ... — F., fr. G. Dolman' — French is the immediate donor to English.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 530\", \"stance\": \"supports\", \"note\": \"'frz. doliman, dolman „Husarenjacke“.'\"}\n ]\n})\n\nm.append({\n \"id\": 5, \"lang\": \"English\", \"words\": \"dolman; dolman sleeve\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"English dolman is first the Turkish robe (17th c.), then the braided hussar jacket worn under the pelisse (early 19th c.), then a woman's mantle with wide cape-like sleeves (later 19th c.); from that last sense comes dolman sleeve, a sleeve cut in one with the bodice and tapering from a very wide armhole, a fashion term of the 20th century. AHD defines exactly this: 'Of or relating to a garment having sleeves that taper from a very wide armhole: a dolman sweater.' Klein p. 473 gives the same word as 'a long Turkish robe; a kind of jacket worn by hussars'.\",\n \"derivation_fa\": \"در انگلیسی dolman نخست همان ردای ترکی است (سدهٔ هفدهم)، سپس نیم‌تنهٔ قیطان‌دوزیِ هوسارها که زیر شنل می‌پوشیدند (آغاز سدهٔ نوزدهم)، و سرانجام شنلِ زنانه با آستین‌های گشادِ ردامانند (اواخر سدهٔ نوزدهم)؛ از معنای اخیر اصطلاحِ dolman sleeve پدید آمد، یعنی آستینی که یکپارچه با تنهٔ لباس بریده می‌شود و از حلقهٔ آستینِ بسیار گشاد به سوی مچ تنگ می‌شود. فرهنگ امریکن هریتیج همین را می‌گوید: «مربوط به جامه‌ای که آستین‌هایش از حلقه‌آستینی بسیار گشاد باریک می‌شود». کلاین نیز در صفحهٔ ۴۷۳ همان واژه را «ردای بلند ترکی؛ گونه‌ای نیم‌تنهٔ هوسارها» تعریف می‌کند. ادعای نورایی درست است.\",\n \"sources\": [W+\"dolman\"],\n \"ref_check\": [\n   {\"ref\": \"KLN:473\", \"status\": \"supports\", \"note\": \"Verified page: KLN_1966.txt leaf 260 carries the printed page numbers 473-475 and contains 'dolman, n., a long Turkish robe; a kind of jacket worn by hussars. — F., fr. G. Dolman, fr. Hung. dolmány, fr. Turk. dolaman, the red cloak of the Janizaries.'\"},\n   {\"ref\": \"AHD:389\", \"status\": \"supports\", \"note\": \"AHD s.v. dolman (online 5th ed.) has both the garment senses and 'adj. Of or relating to a garment having sleeves that taper from a very wide armhole: a dolman sweater', i.e. Nourai's 'dolman sleeve'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"Wiktionary\", \"where\": \"s.v. dolman\", \"stance\": \"supports\", \"note\": \"'Apparently from French doliman, dolman (sense 2), ultimately from Ottoman Turkish دولامان (dolaman, „robe“), from طولامق (dolamak, „to wrap around“). Compare German Doliman, Dollman; Hungarian dolmány.' Senses: Turkish robe; hussar's jacket; 'a woman's garment with wide capelike sleeves'.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch no. 530\", \"stance\": \"supports\", \"note\": \"The whole European family (Romanian, Bulgarian, Serbian, Russian, Polish, Czech, German, French) is set out under Turkish dolama.\"}\n ]\n})\n\nout = {\n \"pdf_page\": 139,\n \"book_page\": 109,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-05\",\n \"entries\": [root0, e1]\n}\n\nwith open(\"/home/sfmqrb/git/rishe/data/verification/page-139.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(out, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build139.py",
 "description": "Build page-139.json"
}
```


### [2026-09-05T20:28:12.947Z] TOOL RESULT

```
written
```


## [2026-09-05T20:28:17.405Z] TOOL CALL #79: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-139.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 139",
 "description": "Validate and run verify_check"
}
```


### [2026-09-05T20:28:19.376Z] TOOL RESULT

```
JSON OK
nodes verified: 18/18
node verdicts: {'confirmed': 13, 'plausible': 3, 'disputed': 2}
root verdicts: {'plausible': 2}
ref checks: {'supports': 9, 'not_checked': 8, 'not_found': 1, 'partial': 6, 'contradicts': 1}
books consulted: {'supports': 29, 'contradicts': 3, 'partial': 7, 'silent': 2} | by book: {'KLN': 5, 'LKT': 5, 'BRT': 4, 'PHD': 4, 'Wiktionary': 4, 'KNT': 2, 'WLD': 2, 'NYB': 2, 'HRN': 2, 'BQT': 2, 'POK': 2, 'IEC': 2, 'AHD': 2, 'TAD': 1, 'HUB': 1, 'SNS': 1}
```


## [2026-09-05T20:28:32.258Z] TOOL CALL #80: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,urllib.parse\nidx=[json.loads(l) for l in open('data/verification/sources/web/index.jsonl',encoding='utf-8')]\nurls={e['url'] for e in idx}\nd=json.load(open('data/verification/page-139.json',encoding='utf-8'))\nmissing=set()\ndef walk(o):\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources':\n                for u in v:\n                    if u not in urls:\n                        dec=urllib.parse.unquote(u)\n                        if dec in urls: o['sources'][o['sources'].index(u)]=dec\n                        else: missing.add(u)\n            else: walk(v)\n    elif isinstance(o,list):\n        for x in o: walk(x)\nwalk(d)\njson.dump(d,open('data/verification/page-139.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)\nopen('data/verification/page-139.json','a',encoding='utf-8').write('\\n')\nprint(\"still missing:\",missing)\nEOF\npython3 tools/verify_check.py 139 | head -3",
 "description": "Normalize source URLs to archived form"
}
```


### [2026-09-05T20:28:34.198Z] TOOL RESULT

```
still missing: set()
nodes verified: 18/18
node verdicts: {'confirmed': 13, 'plausible': 3, 'disputed': 2}
root verdicts: {'plausible': 2}
```


## [2026-09-05T20:29:00.104Z] AGENT

Page 139 (book p. 109) verified — `/home/sfmqrb/git/rishe/data/verification/page-139.json`, `verify_check.py 139`: 18/18 nodes, 0 PROBLEM lines.

Verdicts: nodes 13 confirmed / 3 plausible / 2 disputed; both roots plausible. Ref checks: 9 supports, 6 partial, 1 contradicts, 1 not_found, 8 not_checked; 41 `consulted` entries across 16 books.

- **disputed — Dô 2, node 6 (Av. "dâta 2 / ŭši-dâta")**: no Avestan *uši-dāta- is attested (Bartholomae has only uši.dam-/uši.darəna-, a mountain); the compound is Darmesteter's conjecture.
- **disputed — Dô 2, node 7 (هوشیار)**: second element is OIr. *-dāra- "holding" (PIE *dʰer-), not *-dāta- "given" — as in بختیار/شهریار. Nourai's own cited page, Mo'in's footnote at BQT:2396, quotes Horn rejecting the -dāta- reading ("از طریق علم‌الاصوات این فرض غیرممکن است"), so his reference contradicts his arrow.
- **plausible — root Dô 2**: gloss "to give, create" merges two PIE roots that only Iranian merged (*deh₃- "give" vs *dʰeh₁- "put, create"; Kent separates ¹dā-/²dā-). Consequence: dādār, dāθuš/Day (nodes 2, 4, 5) descend from *dʰeh₁-, not from this root box.
- **plausible — root Dolmak + nodes 1, 2**: the wrapping sense belongs to *dolamak* (PTk *tolga-), not *dolmak* "to be filled" (PTk *tōl-). The garment branch (dolama > Hung. dolmány > G. Dolman > F. > E. dolman) is right; Persian دلمه is Turkish *dolma* "stuffed thing" from *dolmak*, i.e. a sibling of dolama, not its child. Chart also omits the Hungarian step.
- Chart NOTE on Baghdad checked: TAD really prints "بغداد ـ فارسي مركب من باغ ... وداد"; it is a folk etymology — bag-dāta "god-given" stands.

No extraction errors: the JSON matches the chart text throughout; no node needed a `transcription_suspect` flag. Unreadable references: BQT:121/289/815/907 (vols 1–2 have no page-mapped scan and the OCR drops Mo'in's Latin footnotes), SNS:295, NYB:56 (its d- entries sit at printed ~60–64, content correct). KLN:473 was page-verified; BQT:2396 rendered to `sources/refs/ocr/BQT/2396.png`; 15 web pages archived via fetch_source.py.
