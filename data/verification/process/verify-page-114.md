# Verification process log — verify-page-114


## [2026-09-05T17:44:23.360Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 114 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-114.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-114.json. Write /home/sfmqrb/git/rishe/data/verification/page-114.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 114` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T17:44:24.966Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T17:44:25.679Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T17:44:25.705Z] TOOL RESULT

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


## [2026-09-05T17:44:25.779Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-114.txt"
}
```


### [2026-09-05T17:44:25.792Z] TOOL RESULT

```
1	=== PDF page 114 (book page 84) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Dekm : ten  (refs POK:191)  PART 1
4	#1 (parent #0) [Avestan / Old Persian] refs=POK:191; GPL:41 | dasa : ten ; aeva-dasa : eleven ☞I 2 ; tri-dasa : thirteen ☞Trei ; xšvaš-dasa : sixteen ☞Sweks ; nava-dasa : nineteen ☞Newn
5	  #2 (parent #1) [Pahlavi] refs=BQT | dah : ten ; yâcdah : eleven ; sîkdah : thirteen ; šâncdah : sixteen ; navasdah : nineteen
6	    #3 (parent #2) [Persian] refs=BQT | dah «ده ١» : ten ; yâzdah «یازده» : eleven ; sîzdah «سیزده» : thirteen ; šânzdah «شانزده» : sixteen ; nŭzdah «نوزده» : nineteen
7	#4 (parent #0) [Avestan / Old Persian] refs=GPL:41; POK:191 | saiti 1, sat : a suffix meaning ten ; vi-saiti : twenty ☞Wi ; thri-sat : thirty ☞Trei ; čatvare-sat : forty ☞Kwetwer ; pančâ-sat : fifty ☞Penkwe
8	  #5 (parent #4) [Persian] refs=GPL:41; BQT |  | extra: بیست ، سی ، چهل ، پنجاه
9	#6 (parent #0) [Avestan / Old Persian] refs=GPL:41; POK:191 | -iti, -ti : a suffix meaning ten ; xšvaš-ti : sixty ☞Sweks ; hapta-iti : seventy ☞Septm ; ašta-iti : eighty ☞Okto ; nava-iti : ninety ☞Newn
10	  #7 (parent #6) [Persian] refs=GPL:41 |  | extra: شست ، هفتاد ، هشتاد ، نود
11	#8 (parent #0) [Germanic] refs=AHD | tehun, tehan : ten
12	  #9 (parent #8) [English] refs=None | ten, teen
13	#10 (parent #0) [Latin] refs=AHD:352; POK:191 | decem, den : ten ; decimus : tenth ; duo-decem : twelve ☞Dwo
14	  #11 (parent #10) [French] refs=None | deca : ten ; deci : tenth ; douzaine : dozen
15	    #12 (parent #11) [Persian] refs=MON:1572; VOP:167 | dekâ- «دکا ـ (دکامتر)» ; desî- «دسی ـ (دسیمتر)» ; dojîn «دوجین»
16	  #13 (parent #10) [English] refs=None | deci-, decimal, dime, December, dozen
17	#14 (parent #0) [Latin] refs=AHD:352; | děn-ârius : a silver coin worth ten bronze "asses".
18	  #15 (parent #14) [Pahlavi] refs=BQT:916 | denâr : an old monetary unit
19	    #16 (parent #15) [Persian] refs=BQT:916 | dînâr «دینار» : an old monetary unit
20	  #17 (parent #14) [Greek] refs=AHD:370 | děnârion
21	    #18 (parent #17) [Arabic] refs=AHD:370 | dînâr
22	      #19 (parent #18) [English] refs=AHD:370; KLN:450 | Dinar
23	#20 (parent #0) [Greek] refs=AHD | deka : ten
24	  #21 (parent #20) [English] refs=None | deca-, decade
25	
```


## [2026-09-05T17:44:28.753Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-114.json",
 "description": "Read source JSON for page 114"
}
```


### [2026-09-05T17:44:28.794Z] TOOL RESULT

```
{
  "pdf_page": 114,
  "book_page": 84,
  "entries": [
    {
      "root": {
        "name": "Dekm",
        "lang": "Indo-European",
        "refs": "POK:191",
        "gloss": "ten"
      },
      "part": 1,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "POK:191; GPL:41",
          "words": [
            {"translit": "dasa", "gloss": "ten", "script": null},
            {"translit": "aeva-dasa", "gloss": "eleven", "script": null, "see": ["I 2"]},
            {"translit": "tri-dasa", "gloss": "thirteen", "script": null, "see": ["Trei"]},
            {"translit": "xšvaš-dasa", "gloss": "sixteen", "script": null, "see": ["Sweks"]},
            {"translit": "nava-dasa", "gloss": "nineteen", "script": null, "see": ["Newn"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT",
          "words": [
            {"translit": "dah", "gloss": "ten", "script": null},
            {"translit": "yâcdah", "gloss": "eleven", "script": null},
            {"translit": "sîkdah", "gloss": "thirteen", "script": null},
            {"translit": "šâncdah", "gloss": "sixteen", "script": null},
            {"translit": "navasdah", "gloss": "nineteen", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {"translit": "dah", "gloss": "ten", "script": "ده ١"},
            {"translit": "yâzdah", "gloss": "eleven", "script": "یازده"},
            {"translit": "sîzdah", "gloss": "thirteen", "script": "سیزده"},
            {"translit": "šânzdah", "gloss": "sixteen", "script": "شانزده"},
            {"translit": "nŭzdah", "gloss": "nineteen", "script": "نوزده"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "GPL:41; POK:191",
          "words": [
            {"translit": "saiti 1, sat", "gloss": "a suffix meaning ten", "script": null},
            {"translit": "vi-saiti", "gloss": "twenty", "script": null, "see": ["Wi"]},
            {"translit": "thri-sat", "gloss": "thirty", "script": null, "see": ["Trei"]},
            {"translit": "čatvare-sat", "gloss": "forty", "script": null, "see": ["Kwetwer"]},
            {"translit": "pančâ-sat", "gloss": "fifty", "script": null, "see": ["Penkwe"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "GPL:41; BQT",
          "words": [],
          "script_extra": "بیست ، سی ، چهل ، پنجاه",
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "GPL:41; POK:191",
          "words": [
            {"translit": "-iti, -ti", "gloss": "a suffix meaning ten", "script": null},
            {"translit": "xšvaš-ti", "gloss": "sixty", "script": null, "see": ["Sweks"]},
            {"translit": "hapta-iti", "gloss": "seventy", "script": null, "see": ["Septm"]},
            {"translit": "ašta-iti", "gloss": "eighty", "script": null, "see": ["Okto"]},
            {"translit": "nava-iti", "gloss": "ninety", "script": null, "see": ["Newn"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "GPL:41",
          "words": [],
          "script_extra": "شست ، هفتاد ، هشتاد ، نود",
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [
            {"translit": "tehun, tehan", "gloss": "ten", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "ten, teen", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:352; POK:191",
          "words": [
            {"translit": "decem, den", "gloss": "ten", "script": null},
            {"translit": "decimus", "gloss": "tenth", "script": null},
            {"translit": "duo-decem", "gloss": "twelve", "script": null, "see": ["Dwo"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "deca", "gloss": "ten", "script": null},
            {"translit": "deci", "gloss": "tenth", "script": null},
            {"translit": "douzaine", "gloss": "dozen", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Persian",
          "refs": "MON:1572; VOP:167",
          "words": [
            {"translit": "dekâ-", "gloss": null, "script": "دکا ـ (دکامتر)"},
            {"translit": "desî-", "gloss": null, "script": "دسی ـ (دسیمتر)"},
            {"translit": "dojîn", "gloss": null, "script": "دوجین"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "deci-, decimal, dime, December, dozen", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:352;",
          "words": [
            {"translit": "děn-ârius", "gloss": "a silver coin worth ten bronze \"asses\".", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "Pahlavi",
          "refs": "BQT:916",
          "words": [
            {"translit": "denâr", "gloss": "an old monetary unit", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 15,
          "lang": "Persian",
          "refs": "BQT:916",
          "words": [
            {"translit": "dînâr", "gloss": "an old monetary unit", "script": "دینار"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 14,
          "lang": "Greek",
          "refs": "AHD:370",
          "words": [
            {"translit": "děnârion", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 18,
          "parent": 17,
          "lang": "Arabic",
          "refs": "AHD:370",
          "words": [
            {"translit": "dînâr", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 19,
          "parent": 18,
          "lang": "English",
          "refs": "AHD:370; KLN:450",
          "words": [
            {"translit": "Dinar", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 20,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "deka", "gloss": "ten", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 21,
          "parent": 20,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "deca-, decade", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-05T17:44:30.389Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','GPL','BQT','AHD','MON','VOP','KLN','WLD','BRT','KNT','PHD','NYB','HRN','HUB','IEC','SYN','SKT','FSD','WEB','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:400])\n\""
}
```


### [2026-09-05T17:44:32.058Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
GPL {"title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911", "edition_found": "1911", "kind": "archive_djvu", "url": "https://archive.org/details/grammarofpersian0000plat", "identifier": "grammarofpersian0000plat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt", "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09:
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root,
```


## [2026-09-05T17:44:35.765Z] TOOL CALL #5: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && sed -n 1,80p tools/verify_check.py"
}
```


### [2026-09-05T17:44:35.827Z] TOOL RESULT

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
page-60.json
page-61.json
page-62.json
page-63.json
page-64.json
page-65.json
page-66.json
---
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


## [2026-09-05T17:44:36.123Z] TOOL CALL #6: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md | head -120"
}
```


### [2026-09-05T17:44:36.166Z] TOOL RESULT

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


## [2026-09-05T17:44:48.712Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"de-k[mṃ]\" POK_full.txt | head -20; echo \"=== dekm\"; grep -n \"dek̂m\\|deḱm\\|dek̑m\\|dekm̥\\|de-k̂m\" POK_full.txt | head -20"
}
```


### [2026-09-05T17:44:48.767Z] TOOL RESULT

```
=== dekm
```


## [2026-09-05T17:44:49.952Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json,sys\nd=json.load(open('../refs_online.json'))\nfor k in ['POK','GPL','AHD','BQT','MON','KLN']:\n    e=d[k]\n    print('==',k, e.get('local_file'), '| offset:', e.get('page_offset'))\n    print('   hint:', (e.get('lookup_hint') or '')[:600])\n\""
}
```


### [2026-09-05T17:44:51.762Z] TOOL RESULT

```
== POK /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | offset: POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
== GPL /home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt | offset: leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Grammar organised by numbered paragraphs (§); grep the paragraph number or the Persian word in transliteration.
== AHD /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
   hint: Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves 
== BQT ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | offset: vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
   hint: grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=deh
== MON ['/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v1_djvu.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_archive.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/MON/MON_2vol_Adena_v2_djvu.txt'] | offset: None
   hint: Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded a
== KLN /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | offset: KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
   hint: Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
```


## [2026-09-05T17:44:55.673Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"lemma: de\" POK_full.txt | head -40"
}
```


### [2026-09-05T17:44:55.747Z] TOOL RESULT

```
8831:lemma: del-5\ "long': Baltic with unexplained o'-loss (see below): Lithuanian ilgas, f. ilga, 
8851:Root/ lemma: digh-\ "goaf derived from a zero grade of Root/ lemma: dei§h-\ "to prick; 
8853:tick'. From the older root Root/ lemma: deigh-: "to prick; tick' derived Root/ lemma: aig-\ 
8945:languages. The phonetic shift da- > zero'xs a common Baltic. Compare Root/ lemma: del- 
16740:Root / lemma: deigh- 
16762:Root / lemma: deiR- 
16839:Root / lemma: dei-1, deia-, di-, dia-{*sthei- : zdhei-) 
17099:Root / lemma: deia-2{dia- dia- dh) 
17142:Root / lemma: de/c-l 
17247:as Latin dexter, -tra, -trum is a suffixed form of old PIE Root / lemma: deR-1 : "to take'. The 
17258:Root /lemma: deR-2{\ doR-, deR-) 
17312:Root/ lemma: deRn^, deRrp-t, deRu- {* due-RrQ-tj\ ten' is an extended Root/ lemma: dud(u) 
17456:Root / lemma: de/-1 
17499:Root / lemma: del-2 
17534:Root / lemma: del-3{dol^, dela- 
17677:Root / lemma: del-4 
17699:Root / lemma: del-5 
17796:Root / lemma: demel- 
17881:Root / lemma: dem-, dema- 
17966:It is a common trait of alb. and Lithuanian to drop the initial da- as in Root/ lemma: del-5\ 
17987:Root / lemma: dem-, derna-: "to build; house' derived from Root/ lemma: ghei-2. ghi-: 
17999:Root / lemma: denR- 
18005:Root/ lemma: denR-\ "to bite' derived from lllyrian derivative of Root/ lemma: gerrio'^-, 
18047:Root / lemma: dens-1 
18102:Root / lemma: dens-2 
18130:Root / lemma: deph- 
18146:It seems that Root/ lemma: deph-\ "to stamp, push' derived from Root/ lemma: d^ab^^-/, 
18154:Root / lemma: deic!^- 
18198:Root / lemma: der(ep)- 
18204:The Root/ lemma: der(ep)-\ "to see, *mirror' derived from Root/ lemma: deii(-\ "to look'. 
18216:Root / lemma: dera-, dra- 
18239:Root / lemma: dergh- 
18264:Root / lemma: deiic- 
18272:Root / lemma: deii(- : to look derived from Root / lemma: gher-3 und ghere-, ghre- : to 
18323:Root / lemma: der-1{\ dor-, deT-) or dor-: dar- 
18343:Clearly Root/ lemma: der-1{. dor-, deT-) or dor-, dor-: "hand span' derived through Root/ 
18349:derived from truncated ghesor. The source of Root / lemma: der-1 {. dor-, der-) or dor-: 
18377:meaning two hands. That means both Root/ lemma: der-1 {. dor-, der-) or dor-, dor-: 
18476:Alb. proves that from Root / lemma: der-, heavy basis dera-, dre-\ "to cut, split, skin' 
18538:Root / lemma: deru- doru-, dr(e)u-, drou- dreuQ- : dru-
```


## [2026-09-05T17:44:56.295Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==200' POK_01.txt | head -80"
}
```


### [2026-09-05T17:44:57.905Z] TOOL RESULT

```
onön  ^zeichnen^,  got.  taiknjan «oio-enS  3-hd.  zeihinen  ds.
Aus  germ.  *taikna  stammt  finn.  taika-  ^Vorzeichens
Ob  deik-  und  deig-  aus  dei-  ,hell  glänzen'  (auch  ^sehen')  als  ^sehen  lassen, aufblitzen  lassen'  erweitert  sind?
WP.  I  776  f.,  WH.  I  348  f.,  351,  860,  Schwyzer  Gr.  Gr.  I  696  f.,  Feist 204,  472.
X.  dek-   ,nehmen,   aufnehmen',    daher  ,begrüßen,   Ehre   erweisend    Aus  der Bed.   ,annehmen,   gern   aufnehmen'   fließt  die  Bed.  ,gut  passend,  ge- eignet, sich  schicken,  ziemen,  es  jemandem  recht  machen;   als  unan- nehmbar darstellen,  etwas  einem  gut  scheinend  machen,  lehren,  lernen'; dekos-  n.  , Zierde,  Ehre'. Ai.  dasasydti  ,erweist  Ehre,  verehrt  einen  Gott,  ist  gnädig'  (Denomin. von   *dasas-   ==  lat.   decus),   dasä    f.    ,Zustand,   Schicksal';    av.   dasdm   n. ,Habe,  Vermögensstück';  ai.  Desiderat,  dlksate  ,weiht  sich',  dlksä  ,Weihe' (*di-dk-s-  mit   sekund.  i),   ddksati  ,ist  tüchtig,   macht  es  einem   recht,  ist gefällig',  ddksa-h  ,tüchtig,  geschickt'  (aber  av.  dax§-  ,lehren,  unterweisen', npers.  daxs    , Geschäft,   Mühe'    bleiben  wegen   des   Gutturals    fern),  dehn- stufig ai.  däsnötij  dästi,  däsati  ,bringt  Opfer  dar,  erweist  Ehre,  gewährt', däsvds-  ,die  Götter  ehrend,  fromm';  av.  däUa-    ,erhalten,  erlangt'  (Partiz.); nach  Frisk  Etyma  Armen.  25  f.  hierher  arm.  dncay  ,Gabe'  aus  *9nd-tiS' äti-  (urarm.  -tis-  aus  *dek-);  ob  auch  hierzu  tesanem  ,ich  sehe'?  (vgl.  unten doy.sva))',  anders  Meillet  Esquisse  135;
gr.  (ion.  äol.  kret.)  di-AOuai  ,nelime  an',  att.  öexo^iaiy  athemat.  hom.  3.  PI. dexazai  (das  x  nach  *d6x^w,  Infin.  dexd-ai)y  Aor.  dfxro,  Partiz.  dayf-ievog, vgl.  TtQOTiösyf^iaL'  TVQoaöexoficcL  Hes.  (yf.i  statt  zw);  das  x  ist  bewahrt  in öoKÖg  ,[Aüfnahme]  balken',  doKav  dri-Ar^v  Hes.  (daraus  lat.  doga  ,Gefäß'), doY,ävaL'  Ol  GTcclLusg  Hes.,  de^dl^a)  ,besteche',  ö(OQO-S6y.og  ,der  Geschenke nimmt',  ös^af.LBvr]  (Partiz.  Aor.)  ,Wasserbehälter',  ägt-deiycstog  ,ausgezeichnet' {et  metr.  Dehnung);  Nasalpräsens  *(J€txw^/at  (:  3ii.däsnöti)  im  Partiz.  ösluvv- y-^vog  ,huldigend,  grüßend',   zu  dsLytavöcowo   ,sie  begrüßten';    Intensiv   dst-
190
dsxaxai  d.s.,  ösi-diOM(j,ai  ^begrüße^  (für  *d>y-Jf (x)-c7xo/ia^  nach  den  Prj auf  -i(jA(x))\  dsi-  kann  dr}-  (idg.  e)  gelesen  werden,  ösi/.v-  auch  deY,v-,  xi^ dsLv,a-  kann  metr.  Dehnung  für  ösx,a-  sein  (Schwyzer  Gr.  Gr.  I  648,  697j1 Kausativ  doyiso)  (=  lat.  doceö  ,meine,  scheine^,  So-asl  fxoi  ,es  scheint  mij (,ist  mir  annehmbar');  Sö^a  f.  ^Meinung,
```


## [2026-09-05T17:45:04.694Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17305,17420p' POK_full.txt"
}
```


### [2026-09-05T17:45:04.739Z] TOOL RESULT

```
Page(s): 191 

Root / lemma: cfeRrp, deRrp-t, deRu-{*due-Rii^-t^ 
Meaning: ten 

Note: 

Root/ lemma: deRn^, deRrp-t, deRu- {* due-RrQ-tj\ ten' is an extended Root/ lemma: dud(u) 
{*duei-): "two". The subsequent roots * uT-Rn[it-T\ "twenty' and ^/?7/'d/77 "hundred' are mutated 
forms of the root *due-Rnff-t\ "ten'. They both reflect the common lllyrian- bait d- > zero. 

Comments: 

The root number {*Rem-t-d) for 10, 20, 30, 40, 100 derived from the name of deer counted 

by PIE hunters, see Root/ lemma: Rem-2\ hornless, young deer. 

Material: Old Indie dasa, Avestan dasa, Armenian /5S/7 (after Meillet Esquisse 42 from 

*o'e^-, as russ. (tri)dcatb "30' from (tri-)dbseti), gr. 5£Ka, Latin decern {denf per ten' from 

*dek-nor, PN Decius= Oscan Dekis, Gen. Dekkieis), Oscan deketasiuf, Nom. PI. 

degetasius " manager of the tithes ' ( *deken-tasio-), 

Umbrian desen-{duf) " twelve ', Old Irish deich, cymr. deg, corn. bret. dek Gothic tafhun{- 

nas in s/'bun, niun). Old Norse tiu. Old English tien, tyn. Old Saxon tehan. Old High 

German ze/75/7 (a probably from den compounds, Brugmann II 2, 18), 

Tocharian A sak, B sak, Finnish deksan^\^' is after Jokl Pr. ling. Baudouin de Courtenay 

104 borrows from Indo Germanic). 

In the substantive number deRrp-tO), actually "decade', go back: 

Old Indie dasat-, dasati-i. "decade', alb. djete, gr. bzKdc,, -dboq, (to a s. Schwyzer Gr. 
Gr. I 498, 597), Gothic ta/hun-tehund ^\r\ur\6re6' (actually "ten decades '), Old Norse t/undt 
6s., Old Prussian dess/mpts ^ter\', Lithuanian desimt, old desimtis, Latvian old desimt, 
metath. desmit, old 0^5/777/5 (compare desmiterr\. f. " ten '); Old Church Slavic des^tb 
(conservative stem in -/, Meillet Slave comm.2 428); 

ofe^:/- probably in Latin decuria^ a body often men; a class, division, esp. of jurors; a 
party, club' (out of it borrows Modern High German Decheru.. "ten pieces'; late Latin 



*teguria\s assumed through Swiss Ziger^ ten pounds of milk'; probably identical with 
Middle High German z/ge^'curd') = Umbrian dequrier, tekuries^ decuries, feast of 
decuries '; compare Oscan-Umbrian dekv/a-\n Oscan (v/a) Dekkviarim^{ a way) 
appropriate to a decury ', Umbrian tekvias "a way to a decury'; in addition probably 
Germanic *tigu- 'decade' in Gothic fidwor-tigjus "40', Old Icelandic fjdrer-tiger. Old English 
feower-tig. Old High German fior-zug6s. Older explanations by WH. I 327 f. and Feist 150. 
see also under under centur/a under Kluge''"' under Decher. 

Maybe alb. /e/r"odd number' 

Changing through ablaut {d)Rixit- (Dual), (d)R6mt-{P\wr.) in figures often (only 
formations up to 50 are provable as Indo Germanic), e.g. Old Indie trimsaVZ^\ Avestan 
^risqs, Armenian ere-sun, gr. ipiaKovra (from *-K(jL)VTa; further details by Schwyzer Gr. Gr. 
I 592), Latin tri-ginta {\N\\h unexplained g), gallo-Latin Abl. PI. TRICONTIS, Old Irish tncho 
(with /"after frr3'), bret. tregont {* tri-komt-es), acymr. trimuceint(\v\ the ending after uceint 
'20'); s. also under u7-kmff^2Q\ 

ordinals dekemo-s and deRrp-to-s: 

dekemo-s\n Old Indie dasama-h, Avestan dasama-, osset. dasam, Latin decimus, 
therefrom decumanus^ of the tenth. (1) relating to the provincial tax of a tenth; m. as subst. 
the farmer of such a tax. (2) belonging to the tenth legion; m. pi. as subst. its members. (3) 
belonging to the tenth cohort ', later "considerable ', Oscan Dekm-anniufs " *Decumanii^ , 
compare also EN Decumius, out of it entl. etr. tecumnal, latinized back Decumenus, gall. 
decametos. Old Irish dechmad, mcymr. decvet, corn, degves. 

deRrp-to-sxn gr. Sekqtoc; (see also Schwyzer Gr. Gr. I 595); Gothic tafhunda. Old Norse 
tTunda, Old High German zehanto, zehendo. Old English teogeda. Old Prussian dessTmts, 
Lithuanian desimtas, Latvian desmitais, older desimtais. Old Church Slavic des§tb\ 
Tocharian A skant, B skante, 5/r5/7ce (linguistic singles Armenian tasn-erord, alb. i-dhjet^\ 

Note: 

Anatolian languages show a pattern similar to alb. So Lycian aitata {* oktd(u)ta) "eight' : alb. 
/e/s "eight'; Lycian nuntata ' n\ne' : alb. nanda'n\ne'. Therefore alb. 5/7/3/5 "seven' derived 
from a truncated *sa{p)tata^ seven' later Old Indie saptathah, Avestan hapta&a-. Old 
Saxon sivotho. Old English seofoda, Lithuanian septintas, also Old Indie saptatf-, Avestan 
haptaiti-lQ\ in alb. -ta, -teare attribute endings that were solidified in Anatolian and Indie 
cognates. The attribute /a (used in the genitive and adjectives) is unique to alb. language 
alone. 



Therefore alb. teta "eight' is a zero grade of Lycian aitata {*oRtd(u)ta) "eight'. It was initially 
an ordinal number used as an attribute [compare Latin octuag/nta '80']. 

Alb. Tosc nanta, Geg nanda' nine ' derived from Lycian nuntata 'n\ne'. 

Alb. gjashta {seRs-ta) "six' [common alb. s- > gj-] : Old Indie 5^/"six', sastha- "sixth' was 
initially an ordinal number. 

Hence alb. d/e-ta'ten' derived from a proto Romance cognate *d/e+ common alb. -ta 
suffix used in attribute nouns; similarly in: Portuguese dez, Ga//c/an dez, Spanish diez, 
Lad/no d\es, Astur/an d\ez, Aragonese d\ez, Auvergnat6\e, L/mos/n6\e, Rumantsch 
Grischund'\esdr\, Surs/7vand'\esdr\, Vallader desch, Ladin diesc, Italian died, Venetian 
diese etc. 

Here ^/?7/'d/77 "hundred' from *(djkrptdm{\.er\) dekades': 

Old Indie satam, Avestan satem (out of it Finnish sata, Crimean Gothic sada); 

gr. EKarov, Arcadian ekotov (from dissimil. *sem Rmtom'a hundred'? compare Schwyzer 
Gr. Gr. I 592 f.), abbreviated *KaTOv in *T£Tpa-KaTOv etc (in TSTpaKOTioi TSipaKoaioi, 400', " 
four hundred '); 

Note: 

Gr. eKQTOv {*heRaton) < * (d)kn^t6m{\.ex\) dekades' is crucial to crucial for tracing the cause
```


## [2026-09-05T17:45:05.309Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==201' POK_01.txt | head -60"
}
```


### [2026-09-05T17:45:07.687Z] TOOL RESULT

```
Ruhm'  (*dox-ö-ß),  döyi-ia  n.  ^Be Schluß',  ö6yciiJ.og  ,ansehnlich,  erprobt';  Soxevo)  ,beobachte',  TCQoa-doy.d(o  ,ei warte';  über  diddayco)  s.  unter  1.  dens-.
alb.  ndieh  ,sich  befinden'  (*deksk5-?)]  ndesh  ,an treffen'  wohl  slav.  LwJ S.  unter  des-;
lat.  c?ece^,  -ere  ,es  ziemt  sich,  ziert,  paßt  gut',  decus,  -oris  n.  ,Zierd( Würde',  dignus  , würdig'  (aus  *dec-nos,  eigentl.  ,geziert  mit');  umbr.  tigi decef/  (s.  dazu  EM.  257);  Kausativ  doceö,  -ere  ,lehre'  (,lasse  einen  etwj annehmen');  discö,  -ere,  didici  ,lerne'  (aus  *di-dk-skö)]  ;',_^
air.  deck  ,der  beste'  (=  lat.  decus);  auch  in  PN  Ecliuid  (^ekvo-de%-^ Gen.  Echdach,  Lnguid,  Gen.  Luigdech  (urir.  Lugu-deccas  mit  cc  =  k),  falls nicht  e  für  älteres  i  steht;  dann  zu  deik-  ,zeigen',  in  der  Bed.  ,befehlei
Vielleicht  hierher  germ.  *teh-uön  in  ags.  teohhlan,  tiohhian  ,meinen,  b( stimmen',  teohh,  tiohh  ,Schar,  Gesellschaft',  teon  (*tehön)  ,bestimraen^J ahd.  gizehön  ,in  Ordnung  bringen',  mhd.  zeche  , Anordnung,  Zunft,  Zeche, Gesellschaft',  nhd.  Zeche,  mhd.  zesem  (*teksma-)  ,ununterbrochene  Reihe' wozu  vielleicht  mit  Dehnstufe  (*tez-uö)  got.  tewa  ,Ordnung',  gatSwjan  ,an'- ordnen';   s.  darüber   auch   unter   deuä-  ,sich  räumlich  vorwärts   bewegen'
Unsicher   aksl.  desg,  desiti  ,finden',  skr.   de.nm  desiti  ,treffen',    refl.  ,je- mandem  begegnen',  cech.  po-desiti  und  u-desiti  ,einholen,   erwischen'; lautend  russ.-ksl.  dositi  , finden,  begegnen';  s.  auch  unter  des-.
Toch.  A  täk-  ,urteilen,  entscheiden';  zweifelhaft  A  täskmäm  {^täksk-märrif ,ähnlich',  Van  Windekens  Lexique  137;  Pisani  Rc.  R.  Ist.  Lomb.  76,  2,  30.
Zum  es-St.   ai.  dasas(ydti),    lat.  decus  stellen   sich   auch  die  Worte   für; ,rechts'  (Specht  KZ.  62,  218).
deks-  mit  verschiedenen  Suffixen:
Ai.  ddksina-j  daksind-  ,rechts,  südlich,  geschickt',  av.  daHna-  ,rechts', lit.  desinas  diS.,  dekinl  ,die  rechte  Hand',  aksl.  desm  ,rechts';  gr.  de^Liegög =  lat.  dexter,  -tra,  -trum  (Komp.  dexterior,  Superl.  dextimus),  osk.  destrst (abgekürzt  für  *destrust)  ,dextra  est',  umbr.  destrame  ,in  dextram';  gr. ds^tog  ,rechts,  glückverkün*lend,  geschickt,  gewandt'  (von  de^i-  mit  For- mans -fo-j  vgl.  gall.  Dexsiva  dea);  (das  Suffix  -uo-  wohl  nach  HaiuoSy skai-uos  ,links')  air.  dess  ,rechts,  südlich',  cjmr.  deheu  {*deksovo-)  ds.,  got taihswa,  ahd.  zeso  ,rechts',  got.  taihswö-  ahd.  zes{a)wa  ,die  rechte  Hand'; alb.  djathte  ,rechts'  (das  von  G.  Meyer  damit  gleichgesetzte  ksl.  desh  ist wohl  Verderbnis  für  desm,  s.  Berneker  187).
191
^yp  I  782  f.,  WH.  I  330  f.,  346  f.,  Trautmann  53,  54,  Schwyzer  Gr.  Gr. «4^    (378    684^  697,  Wistrand  Instrumentalis  14  ff.
j  ^.  (:dok-,  d
```


## [2026-09-05T17:45:16.599Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '17420,17470p' POK_full.txt | grep -n \"Page(s)\" ; echo \"---- context\"; awk 'NR>=17420 && NR<=17460' POK_full.txt | tail -25"
}
```


## [2026-09-05T17:45:16.732Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==202' POK_01.txt | head -40"
}
```


### [2026-09-05T17:45:18.378Z] TOOL RESULT

```
35:Page(s): 191-192 
---- context



Old Church Slavic etc shfo\s barely Iran, loanword (Meillet Slave commun.2 63); 

Tocharian A kant, B kante. 

Alb. Geg du, Tosc oV'two' hence alb. {*hunt) alb. nje-qind^oue- hundred' [common alb. ij > 
/], hence alb. displays centum characteristics while Rumanian suta'a hundred' displays 
the satem nature of Rumanian 

In addition a /^derivative in Latin centur/at " a division of 100; a company of soldiers; a 
century, a part of the Roman people, as divided by Servius Tullius ' (as decuria). Old 
Norse hundari. Old High German huntariu. 'a division of 100, administrative district'. Old 
Bulgarian sbtor/cads., Lithuanian 5//77/e/7O/0as 'characterized by a hundred', s/mfer-g/s' 
hundred-year-old '. 

References: WP. I 785 f., WH. I 200 f., 327 ff., 859, Feist 150, 471 f., Trautmann 53, 305. 
Page(s): 191-192 

Root / lemma: de/-1 

Meaning: to put by; to count, tell 

Material: Perhaps Armenian to/ "line, row', toiem^ line up ';
```


### [2026-09-05T17:45:19.993Z] TOOL RESULT

```
ek-)  ^reißen,  zerreißen,  zerfasernd ^*  \[  dasä  ;die  am  Ende  eines  Gewebes  hervorragenden  Zettelfäden, r-ansen^;  ir.  dual  ,Locke^  {*doklo-)\  got.  tagl  n.  ,einzelnes  Haar^,  anord. titql  u.  ,die  Haare  im  Pferdeschwanz*^,  ags.  tcegl  (engl,  tau)  m.  _,Sch\vanz^,. alid.  2rt^e^  ,Sclnvanz,  Stachel,  männliches  Glied,  Rute^;  got.  tahjan  ,reißen,. zerren^,  distahjan  ,zerstreuen^,  isl.  tcßeja,  täa  ,karden^,  norw.  dial.  tceja (* tahjan)  und  taa  (*tahön)  ,fasern,  zerreißen^;  anord.  tag,  Fl.  tceger  und lagar  f.  ,Faser^,  mhd.  zäch,  zähe  f.  ,Docht,  Lunte^;  in  anderer  Bed. (zerrend  —  ziehend,  hinausziehend^)  norw.  mdartl.  taag  ,langsam  und andauernd^,  mnd.  tege,  ostfries.  tage  ,zähe^  und  ahd.  zag  ,zögernd,  unent- schlossen, zaghaft^,  wozu  zagen  ,verzagt  und  unentschlossen  sein';
vielleicht  hierher  als  ,woran  man  sich  reißt^  oder  ,abgerissenes,  rissiges StücV,  mhd.  zacke  m.  f.,  nhd.  Zacke,  mengl.  takke  ,fibula^,  engl,  tack Stift,  kleiner  NageF,  mit  anderem  Auslaut  tagg,  tagge  m.  ,hervorragende- Spitze,  Zacke^;  oder  gehört  Zacke  zu  lett.  degums  ,Nase,  Schuhspitze^?
S.  auch  unter  denk-.
WF.  I  785.
dektn,  dekm-t,  deku-  ,zehn',  Ordinale  dekeino-s,  dekmto-s.
Ai.  ddsa^  av.  dasa;  arm.  tasn  (nach  Meillet  Esquisse  42  aus  *djc-j. wie  russ.  (tri)dcath  ,S0'  aus  (tri-)dbseti),  gr.  öixa,  lat.  decem  {denl  ,je  zehn^ aus  *dek-noi]  PN  Decius  =  osk.  Dekis,  Gen.  Dekkieis),  osk.  deketasiüi, Nom.  PI.  degetasiüs  ,curatores  decimarum^  (*deken-täsio-),  umbr.  desen-{duf) ,duo-decim^,  air.  deich,  cymr.  deg,  corn.  bret.  dek,  got.  taihun  {-n  wie  in sihun,  niun),  an.  tiu,  ags.  tien,  tyn,  as.  tehan,  ahd.  zehan  {a  wohl  aus  den Kompositis,  Brugmann  II  2,  18),  toch.  A  säk,  B  &ak-^  finn.  deksan  ,10^ ist  nach  Jokl  Pr.  ling.  Baudouin  de  Courtenay  104  aus  dem  Idg.  entlehnt).
Auf  das  Zahlsubstantiv  dekm-t(i),  eigentl.  , Dekade^,  gehen  zurück:
ai.  dasat-,  dasati-  f.  , Dekade',  alb.  djete,  gr.  ösxdg^  -adog  (zum  a  s.. Schwyzer  Gr.  Gr.  I  498,  597),  got.  tdihun-tehund  , hundert'  (eigentlich jZehn  Dekaden'),  anord.  tiund  f.  ds.,  apreuß.  dessimpts  ,zehn',  lit.  de- Hmt,  alt  deHmtis,  lett.  alt  desimt,  metath.  desmit,  alt  desmits  (vgl.  desmits^ m.  f.  , Zehner');  aksl.  desetb  (kons.  Stamm  auf  -t,  Meillet  Slave  comm.^  "^^8);
deku-  wohl  in  lat.  decuria  , Zehntschaft'  (daraus  entlehnt  nhd.  Decher  m. ;Zehn  Stück';  spätlat.  *teguria  wii-d  durch  Schweiz.  Ziger  ,zehn  Pfund  Milch^ vorausgesetzt;  wohl  mit  mhd.  ziger  , Quark'  identisch)  =  umbr.  dequrier^ tekuries  ,decuriis,  Fest  der  Dekurien';  vgl.  osk.-umbr.  dekvia-  in  osk.  (via} Bekkviarim  ,(viam)  Decurialem',  umbr.  tekvias  ,decuvias';  dazu  wohl  germ..
192
*tig2i-  , Dekade'  in  <^ot.  fidwor-tigjus  ,40,  aisl.  fjörer-tiger,    ags.  ßower-ti^ abd.  fior-zug   ds.     �
```


## [2026-09-05T17:45:26.084Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==54' GPL.txt | head -60"
}
```


## [2026-09-05T17:45:26.580Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"yāzdah\\|yazdah\\|sīzdah\\|sizdah\\|panjāh\\|dawāzdah\" GPL.txt | head -20"
}
```


### [2026-09-05T17:45:28.086Z] TOOL RESULT

```
the adjective precede the substantive the ی‎ or * of indefiniteness must be affixed to the noun; ۰.8. بندی دادی‎ ASS ‘good counsel hast thou given’; tS eB سکی‎ استخوانی می خورد‎ ‘a hungry dog was eating a dry bone’. Similarly, if the substantive is in the plural, it alone takes the زی‎ e.g. مردمانی خوب‎ ‘(some) good men’; بندگانی صادق‎ ‘ true (or loyal) servants’.
§ 39. Adjective used as a Subst. An adjective, whether Persian or Arabic, may be used substantively, and in that case it will be treated in every respect as a substantive; e.g. bls a learned man’; دانایان عصر‎ ‘the learned men of the age’; Jol» ‘an ignorant man’; yw ele ‘ignorant men’ ; بدهای آشعارش‎ ‘the bad things in (lit, of) his poems’,
In the rare cases which occur of a noun in the plural number in construction with what appears to be an adjective also in the plural it is generally considered that the ‘ adjective’ is used substantively in apposition. Such instances are—
Faithful servants بندگان مخلصان‎ Worldlywise sages asin پیران‎ Valiant heroes مردانن دلاوران‎
DEGREES OF COMPARISON §40 a. The comparative degree of adjectives (Persian or Arabic) is formed by adding the suffix ثر‎ tar to the positive, and the superlative by adding ین‎ in to the comparative ; e.g. ده‎ ‘good’, بهتر‎ ‘better’, بهترین‎ ‘best’; wo ‘bad’, بدتر‎ (generally contracted to بثر‎ battar, and often to بتر‎ batar) ‘worse’, بدترین‎ (contrac
```


### [2026-09-05T17:45:28.126Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:45:34.802Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['GPL'],ensure_ascii=False,indent=1))\""
}
```


## [2026-09-05T17:45:35.366Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"numeral\" GPL.txt | head -20"
}
```


### [2026-09-05T17:45:36.606Z] TOOL RESULT

```
{
 "title": "J. T. Platts & G. S. A. Ranking, A Grammar of the Persian Language, Part I: Accidence, Oxford 1911",
 "edition_found": "1911",
 "kind": "archive_djvu",
 "url": "https://archive.org/details/grammarofpersian0000plat",
 "identifier": "grammarofpersian0000plat",
 "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/GPL.txt",
 "page_offset": "leaf = printed + 12 (e.g. leaf 17 = p.5). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",
 "lookup_hint": "Grammar organised by numbered paragraphs (§); grep the paragraph number or the Persian word in transliteration.",
 "notes": ""
}
```


### [2026-09-05T17:45:36.639Z] TOOL RESULT

```
54:NoumERALS, 41. Words used Idiomatically in Numbering, 43. Dis- tributive Numerals, 44. Multiplicative Numerals, 45. Approxi- mate Numbers, 45. Fractional Numbers, 46. Adverbial Numbers, 46. Pronoun, 46. Independent Personal Pronouns, 47. Affixed Personal Pronouns, 50. Reflexive Pronouns, 52. Demonstrative Pronouns, 54. Relative Pronouns, 58. Inter- rogative Pronouns, 62. Indefinite Pronouns and Nouns, 65.
64:DrnominativE Nouns. Noun of Unity, 169. Noun denoting Vessel or Receptacle, 170. The Relative Adjective, 170. The Abstract Noun of Quality, 171. The Diminutive, 172. Formation of Feminines from Masculines, 172. Number, 173. The Dual, 173. Regular Plurals, 173. Broken Plurals, 174. The Plural of the Plural, 180. The Declension of Nouns, 180. The Numerals, 181.
66:Construction of the Numerals, 182. Fractional Numbers, 183. Pronominal Suffixes, 183. The Demonstrative Pronoun, 183.
242:§ 14. The twenty-eight letters of the Arabic alphabet are sometimes used as numerals. Their numerical order, however, differs from that given in the alphabet, being, in fact, the order of the Hebrew or Phoenician alphabet. ‘The letters in this order are grouped into the following eight meaningless words, to serve as a memoria technica, and are briefly called ‘the ۵ * ۶:
449:Rem. The indefinite article, 7 )2( = Phl. é, év ‘one’ (= O.P. aiva). The modern Persian numeral یلق‎ ‘one’, is derived from the Phl. évak (év+ak). In the parent language, 2 év, ‘one, a’, preceded the substantive; in Persian it follows, but as an independent word, not as a suffix.
520:Numerals—The Cardinal Numbers Al
523:IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
550:Note 2. In the language of the present day, the particle تا‎ (v. § 53) is affixed to the numerals to denote the individuals; 6.۵ دو تا‎ ‘two’, تا‎ sw ‘three’, تا‎ so ‘a hundred’, هزار تا‎ ‘a thousand’.
551:§ 48. The cardinals are not inflected. The exceptions to this rule are the numerals هزار‎ and رصد‎ which, as collective nouns, take the plural suffix; e.g. صدها‎ ‘hundreds’ ; Es هزارا‎ and هزارها‎ ‘thousands’.
552:Nor, with the exception of wh ‘ , do the numerals have the ya-t-tankir affixed to them.
553:§ 49. The numeral adjective (51s (اسم‎ usually precedes the substan- tive which denotes ‘the things numbered’ (the ر(معدود‎ which ts always tn the singular; as چهار زن‎ ‘four women’; ده اسب‎ ‘ten horses’ ; و پیست سال‎ do ‘a hundred and twenty years’. But if the sub- stantive is made indefinite by means of the has بای‎ to denote an
555:approximate number (§ 36), it will precede the numeral; e.g. دو‎ dls ‘about two years, a year or tw0’ ; sw روزی دو‎ about two or three days’.
557:Words used idiomatically in numbering. In the enumeration of different sorts of objects some collective numeral or noun (such as ‘head’, ‘brace’, ‘pair’, &c.), applicable to the things numbered, is frequently inserted between the numeral and its .معدود‎ The following are some of the words most commonly so used: خفر‎ ‘individual’ (for human beings) ; ul, “head ’ (for horses); سر‎ ‘head’ (for sheep); زاجیر‎ ‘chain’ (for elephants); قطار‎ or مهار‎ mihar ‘row, string’ (for camels, &c.); طاقه‎ ‘fold, part’ (for shawls, &c.); دست‎ or تاد‎ (for clothes); and sometimes for houses; We ‘volume’ (for books); فرش‎ se ae)
571:C: Disrrisutive NUMERALS § 52. Distributives are formed 1) by the repetition of a simple ~
586:‘about’, &c., in construction with the numeral and its ma‘did; e.g.
589:d) Also by affixing the yee پای‎ to the noun and a it with the numeral; e.g. دیناری پا نصد‎ ۲500 dinars or so”
599:§ 56. Numeral adverbs are formed by adding to the cardinals, 1) the subst. بار‎ (or sb) “time *, or one of the synonymous Arabic words رکره ردفنعه رمرتبه روبت‎ 86 eg. بار‎ oh, or توبت‎ eh, or مرتبه‎ ek ‘once’ (but, more commonly, wb, &c.); دو بار‎ or ردو توبت‎ ۰ ‘twice’; 2) the pronominal adjective چند‎ Or چندان‎ ‘so much’, &c., especially the latter; as دو چندان‎ ‘twice as much, double’. The plural بارها‎ (of (بار‎ = ‘many times, repeatedly, often’. In the multiplication table the word بار‎ is not used: its place is taken by the gl po eg Gas times four’ is expressed by چهار در چهار‎ ‘four into four’, or by using تا‎ e.g. شش تا سی تا‎ eu 5 ۳0 = se
832:It may also be followed by a numeral, used as a substantive; as wks, or احدی‎ 42 ‘any one’, with a following negative, ‘not any . one, no one, none’. The substantive may also have the PES, wb annexed to it to strengthen the pronominal adjective; as عیبی ندارد‎ ۰ ۲۳ ‘it has no ae (or, ‘no defect. whatever’) ; هیچ تاربخی‎ pin any epoch whatever’.
843:Similarly, we have هرچا‎ ‘(in) ey place, every where’ ; Wa ‘(at) any time, whenever’ ; بهرحال‎ ‘ in every case, in any 1 . The distributive ah also precede a numeral; e.g. eh > or هرد یکی‎ ۲ one, each one’; هردو‎ ‘both’; هرسه‎ ‘all three’; هرصد‎ ‘every one of the hundred’ ; ۲ کذام‎ used relatively, as هرکذام‎ * whichever ’.
890:8) Yaki(Yaké). Indefinite noun or numeral adjective oe ‘one, some one, a certain one’; with a following negative, ‘ not one, no one, none’, It is used both adjectively and substantively, and in all the cases; €.g. ینکن مردٍ بیگانه دید‎ ‘he saw a (or some) strange man’; روز داهن بدرد‎ ae ‘one day a leopard will rend him’; یکی‎ yal از‎ سر بر نمیدارد‎ ‘not one of these holds up his head’; یکی دوستی بود‎ ‘a certain one had a friend’,
```


## [2026-09-05T17:45:41.302Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=518 && NR<=550' GPL.txt"
}
```


### [2026-09-05T17:45:43.350Z] TOOL RESULT

```
$45. The adjective of astonishment also belongs distinctly to the class of intensive adjectives. It is formed by adding the suffix تا‎ (sdle (الفب‎ to the simple adjective; as بدا‎ ‘how bad! or very bad’ (is) ; Te ‘how great, very great’ (is); Ly ‘how many’! خوشا‎ ۴ pleasant! how lovely’! In construction it usually precedes the sub- stantive, which often has a redundant |, called کلام‎ oe call ‘alif of ornamentation of speech’, or صوت‎ Se الف‎ ‘alif of extension of sound of the voice’, affixed to it; e.g. بدا سلطانیا که‎ ‘how bad (or very bad) is the king who . a0 1 بزرگا غلطا‎ “how great (is) the error’! خوشا شیرازا‎ ‘how beautiful (is) Shiraz’! ۱
Rem. The alif at the end of the adjective is by some termed ws? will ‘the .alif of astonishment’, and کثرت‎ will ‘the 0/7 of
Numerals—The Cardinal Numbers Al
excess’; while that at the end of the substantive is called زائد‎ Call ‘the redundant alzf’. It is the latter alzf that also occurs in the
word گفتا‎ (= wa) ‘he said’, This use of alifis not found in Phl. or O.P., it has its origin in modern Persian, and is probably derived from the Arabic: cf. the final ali in the Ar. وا زیدا‎ ‘Oh Zaid’ ! وا امیر الوم تن‎ 8 for the Conumander of the Belvo? ! This alif is called 433231 eet, or in Persian .الف ندیه‎
IV. THE NUMERALS (اسمای اعداه)‎ A. Tae دجم‎ NumBers (اسمای اعداد ذاتیه)‎ § 46. The following are the cardinal numbers :—
Units (احاد)‎ 1.1 eb (Phi. gvak; O.P. aiva). 5.0 5%) (O.P. paiicha).
2. ۲ 49 (OP. dea). 6. 4 شش‎ (O.P. khshvash). 3. ۳ sw (O.P. thre). 7. ۷ هفت‎ (O.P. hapta).
4. ۴ چهار‎ or le (O.P. ۲ 8. ۸ هشت‎ (O.P. ashta), 9. 4 35 (O.P. nava).
۱ Tens (عشرات)‎
0 دهد‎ (poet. also) sls (O.P. dasa).
11. ۱۱ یازده‎ (dialec.) 3335, (O.P. aivadasa).
12. ۳ دوانزده . وو دوازده‎ (O.P. dvadasa). 13. ۱۳ وو سیزده:‎ .  هدزنیس‎ (O.P. thridasa).
14. ۱۴ چهارده‎ or چارده‎ ) ۰ chathrudasa).
15. 10 بانزده‎ )0.۳۰ paiichadasa).
16. ۱۰ شانزده‎ )۰ khshvashdasa).
17, ۱۷  هدتفه‎ or هفده‎ (O.P. haptadasa).
18. ۱۸ هزده رهشتده‎ or رتجدة‎ (O.P. ashtadasa).
19. 44 $9353; ,وا زده‎ dialec. نوانزده‎ )۰ navadasa). 20. ۲۰ بیست‎ (Phl. vist; O.P. 0190860
30. r- سی‎ (Phi. sth O.P. thrisat).
40. ۰ 2 Je (Phl. chahal ; O.P. chatvaresata). 50. 0+ Ash (Phi. panchah ; O.P. patichasat).
60. 1. شصت‎ for orig. شست‎ (Phi. shasht; O.P. khshvashti). 70. هفتاد مب‎ (Phi. haftat; O.P. haptaiti).
80. a. هشتاد‎ (Phi. hashtat; O.P. ashtaittt).
90. ۰ - نود‎ (Phi. navat ; O.P. ۵۵۵۸۸(۰
42 A ccidence
Hunpreps (متات)‎ 100. 1.. صد‎ (orig. Jw; Phi. sat; 0:۳, sata), plural les. 200. ۲۰۰ دویست‎ (O.P. duye saite) and to 59. 300 ۳ شیک‎ 500. 6. wah,
THOUSANDS (آلوف)‎ ۱
1000. ۱۰۰۰ هزار‎ (Phi. hazar; O.P. hazanra), plural هزاران‎ or .هزارها‎ 10,000. _\j@ ده‎ or UJ, obs. بیور‎ (Phi. 0200۴ و‎ O.P. baévar).
100,000. 7
500,000. هزار‎ sail ne 1,000,000 = کرور‎ yo.
§ 47. The [0 which indicate numbers compounded of the units and the tens, hundreds, &c., are formed by placing the highest number first, the others following in order, and each being connected with the preceding number by the conjunction و‎ ‘and’; as eh بیست و‎ ‘twenty and one, twenty-one’; sy و نود و‎ do هزار و هشت‎ eh ���one thousand and eight hundred and ninety and three’.
Note 1. The same construction is occasionally employed by some of the older poets in the case of the numbers between 10 and 20; e.g. in the Shahnama we meet with ده و دو‎ and داة و دو‎ ‘ten and two, twelve’, The Turki word تومان‎ taman is also used to express 10,000 ; but only (according to Kazimirski) in such constructions as تومان‎ el ‘chief of 10,000 men’, and as the name of a gold-piece of the value of 10,000 dinars. (1 tu&man = 10 girans = 10,000 dinéirs.) The word ملیون‎ 7:29 ‘a million’, borrowed from Europe, is also used in the language of the present time.
Note 2. In the language of the present day, the particle تا‎ (v. § 53) is affixed to the numerals to denote the individuals; 6.۵ دو تا‎ ‘two’, تا‎ sw ‘three’, تا‎ so ‘a hundred’, هزار تا‎ ‘a thousand’.
```


## [2026-09-05T17:45:58.594Z] TOOL CALL #20: Bash

```json
{
 "command": "pdftoppm -f 114 -l 114 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg114 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T17:45:59.995Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD dah/yazdah\"; grep -n \"^dah\\|yāzdah\\|sēzdah\\|šānzdah\\|nōzdah\\|dwāzdah\\|dēnār\\|dīnār\" PHD.txt PHD_mackenzie.txt | head -30"
}
```


### [2026-09-05T17:46:01.208Z] TOOL RESULT

```
total 33780
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 13:46 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9603 Sep  5 10:50 c_byz2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    11328 Sep  5 10:49 c_byz_persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3138 Sep  5 10:50 c_heb1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4953 Sep  5 10:50 c_heb2.png
-rw-rw-r-- 1 sfmqrb sfmqrb      914 Sep  5 11:04 chicane.html
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
-rw-rw-r-- 1 sfmqrb sfmqrb    83933 Sep  5 13:46 pg114.png
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


### [2026-09-05T17:46:01.248Z] TOOL RESULT

```
== PHD dah/yazdah
PHD.txt:307:dahigan 24 darzig
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:312:débag [dyp’k! | N dēbā] brocade. débahr [dyp?hl | P dybhr] anger. pad — dāštan: banish. dég [dyk' | N ~] cauldron. LU) deh [M TA < A m? | M dyh, N ~] country, land; village. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religious. dénódag [dynwtk'] female, milch. dér, dérand, v. dagr, dagrand. d��s(ag) [dys(k') | M dys] form, appearance. désidan, dēs- (dys-ytn! | M dys-yd] build. déw [SD Y.A < A #02, pl. šydy? | N ~] demon, devil. dēwān [d(p)ywn! | N <] archive, collected writings. déwanag [dyw”nk! | N ~a] demonic, mad. dēwār [dyw?l | M dyw’r, N ~] wall. déw|-ésnih [Š D Y Aysnyh | (M dyw?snyh)] idolatry, devil-worship. ~-ézagih [ŠD Y Ayckyh] = ~-ésnih. dēwēk [dywwk! | № déwuk] leech. dibir [dpy(w)r' | M dbyr, N ~] scribe. ~ih: writing, scribeship. „estān [-st?n! LN ~] school. did [TWB < A twb; dt'] again, then, further. didan, wén- [HZ Y TWN-tn! < A У hzy; dytn', wyn- | M dydn, wyn-, N —, bin-] see. ~išn: sight, seeing. ~i8nig : visible. didar [dyť] | N ~] sight; visible. pad ~ [N padidár] visible. didom [dtwm] second. dil [LB(B)ME < A lb(b)-h; dyl | = M, N ~] heart. dilér [dylywl, dlyl | N ~] brave. diz [KLYTA < A дур; dc | M dyz, N ~] fortress. dē [2, TLYN' < A tryn | M dw, N du] two. ~-ахмапіб [2 !hw)nyk!] relating to both worlds. ~ganag [dwk”nk! | M dwg'ng, N dugāna] double; twin. dok [dwk! | N ~] spindle. dol [del | N —] bucket; astr. Aquarius. dó|-pahikar [dwptkl | N du-paikar] astr. Gemini. ~-pay [2 LGLE, дора | N du-pà] biped, human being. dos [dws | N —] gum; plaster. dē-saxwan [2 shwn'] two-tongued, deceitful. dēsēn [dwsyn'] gummy; plastery; *glazed (pottery). dóst [dwst' | = M, N ~] friend.
PHD.txt:317:duš-ēwāz��h 29 dwāzdahān
PHD.txt:318:^-éwüzih [-yxw'cyk | (M dwšw'cyh)) evil speech, calumny. ~+farrag [-plg | P dwéfr] unfortunate. ~-farragih : misfortune. ~-gowisn [-gwbsn'] of evil speech, ill-spoken. ~-humat [-hwmt'] evil thought. ~-hixt [-Awht' | M dwfxwptyy!] evil speech. ~-kām [-2’m] ill-will, malevolence. ~-kanig [-knyk'] hag. — kar LAT difficult. ~-kuni&n [-kwngn'] of evil behaviour, ill-doing. dušmat [dwfmt! = Av. dufmata- | M dw$mtyy!)] evil thought. dušmen [dwsm(y)n' | = M, N dušman] enemy. ~ih: enmity. „ādīh [dušmntyh | M dwkmny’dyh, J dwfmn'dy] enmity, hostility. duš-|-menišn [dwf-myntn!] of evil thought, ill-thinking. --nàm [->”m | N ~] abuse, insult. dušox [dwshw! | M dtws(w)x] hell. ~ig [-yk'] hellish. duš-pādixšā(y) [dušp*thš*(d)) evil ruler. ~th: evil rule, misrule. dušrām [dwsl())m] unhappy. ~ih: unhappiness. dušwār [2001 | M dwšw”r, № ~] difficult, disagreeable. ~ih: difficulty, trouble, misfortune. du&-|-wir [dws-wyl] evil-minded. ~-wurréyisnih [-wlwdsnyh] heresy. c-.xém [-hym] evil-natured. ~-xwadiayih [-hwt'yh] misrule. ~-xwar Lea! | N ~] = dušwār. dušxwaršt [до оной! | M dwkxw styh!] evil deed. duxt [BRTE < A brt-h; dwht' | M dwxt, N ~] daughter. ~ar [dwhtl | N ~] daughter. duz(d) [GN BA < A gnb’; dwc(t) | M dwz, N duzd] thief. ~th [dwe(d)yh] theft. duzidag [dwcytk'] stolen; intercalary (days). duzidan, duz- [dwe-yin' | N duzdidan] steal. dwārīdan / dwāristan, dwür- [dwP?l-ytn!, -stn! | M dwr-] run, move (daevic). ~išn: abode (of demons), hell. dwāzdah [dw'cdh | M dw'zdh, N duwazdah] twelve. ~ап [-’n'] the zodiac.
PHD.txt:671:yāsaman [y smn! | N ~] Jasmine. yask [ysk! | = M] illness, sickness. yasn [ysn' | = M] adoration, worship. yašt [yst! | = M] prayer, worship. yaštan, yaz- [YDBHWN-tn! < A ydbhwn, V dbh; уйт, yc- | M yz-] worship, celebrate, recite. ~Л&п : worship. yāt [yt! = Av. yáta-] a degree of sin. P yāwēd(ān) [5?*wyt(?*n)! | P y'wyd(?n)] always, eternally. yaz-, ~išn, v. ya&tan. yazd [yzdt! | M yzd, N ~] god, divinity. yāzdah [y'cdh | M y'zdh, N ~] eleven. yazdān [yzd’n'] (pl.) gods, spirits. yējdahr [ywid?sl | М ywjdhr] holy, pure. ~th: holiness, purity. yojdahrgar [ywsd’slkl] purifier. ~ih: purification, sanctification. убх [ywc | N ~] cheetah, hunting leopard.
PHD.txt:1619:dinar dēnār.
PHD.txt:3984:thirteen sēzdah.
PHD.txt:4098:twelve dwāzdah.
PHD.txt:5468:gūhragdānāg gohrag dwāzdahān dwāzdah duxt, Just 1-*dūxtun duxtar ldaw-, gūw- gūwāg 12а} dwàr- dwārīdan dwiristan dwārišn jy)
PHD.txt:5579:dahišn, Jah
PHD_mackenzie.txt:1842:dah [ro, ASL Y A < A (ir' I M dh, N ,...,] ten.
PHD_mackenzie.txt:1845:dahlin [PWME < A p(w)m-h I M dhyn, N dahan] mouth.
PHD_mackenzie.txt:1846:dahlbed [dhywpt I M dhybyd] ruler, lord of the land.
PHD_mackenzie.txt:1849:dahigan [dhywk'n 1 iN dihgan] countryman, farmer.
PHD_mackenzie.txt:1850:dahliz [d'hlye I (M dhryz), N ,...,] portico.
PHD_mackenzie.txt:1851:dahm [d'hm] virtuous, pious; a full member of the Mazdean community,
PHD_mackenzie.txt:1853:dahom [d'hwm I M dhwm, N ,...,] tenth.
PHD_mackenzie.txt:8734:dahlin!                         rG"V          padl , pen
PHD_mackenzie.txt:11038:dah-, Jah-
PHD_mackenzie.txt:11055:dahom                                        xwas l
PHD_mackenzie.txt:11066:dahliz
PHD_mackenzie.txt:11071:dahm                                         bahr
PHD_mackenzie.txt:11087:dah-I                                        hazisn
PHD_mackenzie.txt:11577:dahl
```


## [2026-09-05T17:46:12.587Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -o \"sēzdah[^.]*\\.\\|šānzdah[^.]*\\.\\|nōzdah[^.]*\\.\\|wist[^.]*\\.\\|wīst[^.]*\\.\\|panjāh[^.]*\\.\\|čihil[^.]*\\.\\|šast[^.]*\\.\\|haftād[^.]*\\.\\|haštād[^.]*\\.\\|nawad[^.]*\\.\\|sīh [^.]*\\.\" PHD.txt | head -30"
}
```


### [2026-09-05T17:46:12.682Z] TOOL RESULT

```
sīh [суйру] physics.
wistan.
wistan [LH TWN-stn!, dwstn'] = 1 * dawidan.
šastar [dušstl] west.
nawad [90 | N —] ninety.
šast [nsst! | N ~] association.
šastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit.
wistan, *niwéyénidan [nwykyn-ytn'] = niwistan.
wistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate.
šastar ['wsstl] east.
wist, entwine.
šast [60| M šst, N ~] sixty.
wistan.
wist [20; wyst! | = M, N bist] twenty.
wistan, *wih- [SDYTWN-tn' < A V šdh; wstn'] shoot, throw.
wistar(ag) [wsti(g) | N bistar] bedding, cover.
wistardan, wistar- [wstl-tn! | N gustardan] spread.
wistāx [wst??hw! | M wyst?h, N gustāx, bistāx] confident, bold.
wistan [hwystn'] sweat, perspire.
wistan.
šast.
wistar(ag).
wistāx; v.
wistāxīh.
wistāxīh.
wistāx.
wistan, niwéyénidan.
wistar(ag).
šastan.
panjāh.
```


## [2026-09-05T17:46:13.510Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"denar\\|dēnārius\\|denarius\\|dinar\" AHD_watkins1985.txt KLN_1966.txt | head -20; echo \"=== KLN dinar\"; grep -n \"^Dinar\\|^dinar\" KLN_1966.txt KLN_1971.txt | head"
}
```


### [2026-09-05T17:46:13.585Z] TOOL RESULT

```
AHD_watkins1985.txt:72:For the ending, the final vowels of Sanskrit snusd, Old English snoru, and Slavic sniikha all presuppose earlier -d (*snus-d), which is the ordinary feminine ending of these lan- guages. On the other hand, Latin nurus, Greek nuds, and Armenian nu (stem nuo-) all regularly presuppose the earlier ending *-os (*snus-os). Here is an apparent impasse, but the way out is given by the gender of the forms in Greek and Latin. They are feminine, even though most nouns in Latin -us and Greek -os are masculine.
AHD_watkins1985.txt:73:Feminine nouns in Latin -us and Greek -os, since they are an abnormal type, cannot have been created afresh; they must have been inherited. This suggests that the original Indo-European form was *snusos, of femi- nine gender. On the other hand, the common- place freely formed ending for feminine nouns was *-d. It is reasonable to suggest that the three languages Sanskrit, Germanic, and Slavic replaced the peculiar feminine ending *-os (because the ending was nor- mally masculine) with the normal ordinary feminine ending *-d, and thus that the oldest form of the word was *snusos (feminine).
KLN_1966.txt:3561:Arundinaria,  n.,  a  genus  of  bamboo  grasses  (bot.)
KLN_1966.txt:3913:Derivatives:  attitudin-al,  adj.,  attitudinarian, attitudinarianism,  attitudinize  (qq.v.) attitudinarian,  n.,  one  who  attitudinizes.  —  Form¬ ed  with  suff.  -arian  fr.  It.  attitudine.  See  attitude. Derivative:  attitudinarian-ism,  n. attitudinize,  intr.  v.,  to  strike  an  attitude;  to  pose. —  Formed  fr.  It.  attitudine  (see  attitude)  with suff.  -ize.
KLN_1966.txt:7322:Cheka,  n.,  former  name  of  the  political  branch of  the  Soviet  secret  police.  —  Formed  from  the initial  letters  of  Russ.  Chrezvychainaya  Komis- siya,  ‘Extraordinary  Commission’, chela,  n.,  a  Buddhist  disciple.  —  Hind,  chela, ‘slave,  servant’,  fr.  OI.  cefah,  cetakah,  which  is rel.  to  Marathi  ceda,  ‘son’,  celd,  ‘pupil’,  Prakrit ceda-,  cilia-,  ‘boy’,  Pali  cefo,  ‘servant,  youth’, chela,  n.,  the  pincerlike  claw  of  lobsters,  crabs, etc.  ( zool .)  —  ModL.,  fr.  Gk.  yrjXfj,  ‘fork,  claw’, which  is  rel.  to  ‘a  yawning,  gaping’,
KLN_1966.txt:8029:coarctation,  n.,  tightening  of  the  aorta,  an  ori¬ fice,  etc.  (med.)  —  L.  coarctdtio,  gen.  -onis,  ’a crowding  or  pressing  together’,  fr.  coarctdtus, a  collateral  form  of  coartdtus,  pp.  of  coarctdre, resp.  coartdre,  ‘to  crowd  or  press  together’, fr.  co-  and  aretdre,  artare,  ‘to  press  together’, fr.  art  us,  ‘close,  strait,  narrow,  fitted',  which  is related  to  ars,  gen.  artis,  ‘art’,  anna,  ‘armor’; see  art  and  -ion.  The  form  aretdre  (for  artare) is  due  to  folk  etymology,  which  associated  this word  with  L.  arcere,  ’to  hold  off,  keep  off', coarse,  adj.  —  Earlier  also  course,  of  uncertain origin;  possibly  adjectival  use  of  the  noun course  in  the  term  ‘of  course',  taken  in  the  sense of  ‘common,  ordinary,  rude'.
KLN_1966.txt:8896:consuetudinary,  adj.,  customary.  —  Late  L.  con- suetudinarius,  fr.  L.  consuetudd,  gen.  -tudinis. See  prec.  word  and  adj.  suff.  -ary.
KLN_1966.txt:8897:Derivative:  consuetudinary,  n. consul,  n.  —  L.  consul,  ‘either  of  the  two  chief magistrates  of  the  Roman  state’.  This  word prob.  meant  orig.  ‘convener,  convoker’,  and  is
KLN_1966.txt:10444:debouchment,  n.  —  F.  debouchement,  fr.  debou- cher.  See  prec.  word  and  -ment. debridement,  n.,  the  excision  of  damaged  tissue. —  F.,  lit.  ‘unbridling’,  fr.  debrider,  ‘to  unbridle’, fr.  de-  (see  de-)  and  bride,  ‘bridle’,  fr.  MHG. brtdel.  See  bridle  and  -ment. debris,  debris,  n.,  rubbish.  —  F.  debris,  ‘remains, waste,  rubbish’,  fr.  OF.  debriser,  ‘to  break down,  shatter’,  fr.  de-  (see  de-)  and  briser,  ‘to break’,  fr.  VL.  brisare,  ‘to  break’,  a  word  of Gaulish  origin;  cp.  Ir.  brissim,  ‘I  break’.  See bruise  and  cp.  frustum.  Cp.  also  next  word, debruisc,  tr.  v.,  to  cross  a  charge  with  an  ordinary (her.)  —  OF.  debruisier,  ‘to  shatter'.  See  de-  and bruise  and  cp.  debris.
KLN_1966.txt:10535:decode,  v.,  to  translate  from  a  code  into  ordinary language.  —  See  de-  and  code.
KLN_1966.txt:10675:deification,  n.,  the  act  of  making  a  god ;  the  state of  being  made  a  god.  —  See  deify  and  -ation. deiform,  adj.,  having  the  form  of  a  god.  —  ML. deiformis,  compounded  of  L.  deus,  ‘god’,  and forma,  ‘form,  shape’.  See  deity  and  form,  n. deify,  tr.  v.,  to  make  a  god  of.  —  F.  deifier,  fr. Late  L.  deificare,  which  is  compounded  of  L. deus,  ‘god’,  and  -ficare,  ‘to  make’,  fr.  -ficus,  fr. facere,  ‘to  make,  do’.  See  deity  and  -fy. deign,  intr.  and  tr.  v.,  to  condescend.  —  ME. deinen,  deignen,  fr.  OF.  degnier ,  deignier  (F . daigner),  fr.  VL.  *dignare,  fr.  L.  dignari,  ‘to deem  worthy’,  fr.  dignus,  ‘worthy’.  Cp.  It.  deg- nare,  OProven?.  denhar,  Catal.  denyar,  Sp. denar,  which  all  derive  fr.  VL.  *dignare,  and  see dignity.  Cp.  also  dainty,  condign,  dignify,  dis¬ dain.
KLN_1966.txt:10821:denarius,  n.,  an  ancient  Roman  silver  coin.  — L.  denarius,  short  for  denarius  nummus,  ‘the coin  containing  ten  (asses)’,  from  denarius, ‘containing  ten’,  and  nummus,  ‘coin’.  Denarius derives  fr.  deni,  ‘ten  each’,  which  stands  for *dec-noi,  fr.  decern,  ‘ten’.  (Cp.  sinl,  ‘six  each’, fr.  *sex-noi.)  The  denarius  was  so  called  because
KLN_1966.txt:10822:it  originally  contained  ten  asses.  See  ten  and cp.  decern-,  decimal.  Cp.  also  denary,  denier, dinar.
KLN_1966.txt:10823:denary,  n.,  tenfold.  —  L.  denarius,  ‘containing ten*.  See  prec.  word  and  -ary. denationalize,  tr.  v.  —  F.  denationaliser,  fr.  Re¬ fused  in  the  privative  sense  of  this  prefix)  and nationaliser.  See  de-  and  nationalize.
KLN_1966.txt:10841:denier,  n.,  a  French  coin.  —  F.,  fr.  L.  denarius, whence  also  Olt.  danaio.  It.  dandro,  dendro, Proven?,  denier,  dinier,  Sp.  dinero.  Port,  di- nheiro.  See  denarius.
KLN_1966.txt:11461:dinanderie,  n„  decorated  articles  of  brass.  —  MF. (=  F.)  fr.  OF.  dinandier,  ‘worker  in  brass’, formed  with  -ier,  a  suff.  denoting  trade  or occupation,  fr.  Dinand  (now  Dinant),  a  town  in Belgium,  famous  for  its  brasswork.  For  the  end¬ ing  see  the  suffixes  -ier  and  -ery. dinar,  n.  Arab,  dindr,  fr.  Late  Gk.  Srjvdcpiov,  fr.
KLN_1966.txt:11462:L.  denarius.  See  denarius  and  cp.  denier, dine,  intr.  and  tr.  v.  —  ME.  dinen,  fr.  OF  disner (F.  diner),  ‘to  dine’,  orig.  ‘to  breakfast’,  fr. * desjuner ,  shortened  form  of  desjejuner  (see haplology ),  which  derives  fr.  VL.  *disjejundre, ‘to  break  the  fast’,  fr.  dis-  and  L,  jejunus,  ‘fast¬ ing’.  See  jejune  and  cp.  dinner,  dejeuner. Derivatives:  din-er,  n.,  din-ing,  n. ding,  tr.  v.,  to  beat.  —  ME.  dingen,  dengen,  fr. ON.  dengja,  ‘to  hammer,  beat’,  which  is  rel.  to OHG.  tangol,  ‘hammer’,  MHG.  tengeln,  G.  den- geln,  ‘to  hammer,  beat’;  prob.  of  imitative origin.  Cp.  next  word.  Cp.  also  dangle,  dint, ding,  intr.  and  tr.  v.,  to  sound.  —  Of  imitative origin.
KLN_1966.txt:12448:duodenary,  adj.,  in  twelves;  increasing  by  twelves. —  L.  duodenarius,  ‘containing  twelve’,  fr.  duo- deni,  ‘each  twelve’.  See  duodenum  and  adj.  suff. -ary.
KLN_1966.txt:14217:extraordinary,  adj.  —  L.  extraordinarius,  ‘out  of the  common  order,  extraordinary’,  fr.  extra  or- dinem,  ‘outside  the  (common)  order’,  fr.  extra (see  extra)  and  ordinem,  acc.  of  brdo,  ‘order’. See  ordinary.
KLN_1966.txt:14218:Derivatives:  extraordinari-ly,  adv.,  extraordi- nari-ness,  n.
=== KLN dinar
KLN_1971.txt:67653:dinar. 
KLN_1971.txt:71666:dinar, n. — Arab, dindr , fr. Late Gk. Siqvdpiov, fr.
```


## [2026-09-05T17:46:23.934Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('PHD.txt',encoding='utf-8',errors='replace').read()\nfor w in ['sēzdah','šānzdah','nōzdah','wīst','panjāh','čihil','šast','haftād','haštād','nawad','sīh','dēnār','dah [','dahom','sad [']:\n    for m in re.finditer(re.escape(w),t):\n        s=max(0,m.start()-90); print(w,'>>',t[s:m.start()+140].replace('\\n',' '))\n        break\nEOF"
}
```


### [2026-09-05T17:46:25.824Z] TOOL RESULT

```
sēzdah >> der. third sidig; -seyom; (n.) sri8wadag. thirst tīšn, tišnagīh. thirsty tišnag. thirteen sēzdah. thirtieth sihom. thirty sih. this ëd, ën, im. thorn xàr. thorny xarómand. those awēšān. thou tó. thought handēšišn, menišn; v. con- 
wīst >> nidan, wardēnīdan; ~ ¿nto abaz waštan 6. turning gardišn, wardišn. twelve dwāzdah. twenty wīst. twin dóganag. twinkling mēzišn. ranj, sēj, 138 twist pēčīdan. two do. two-tongued dó-saxwan. Lyrannous sézd(én), statt, tyranny sāstā
panjāh >> bre rēšag. fickle nāzuk, r6zward. field ki$w(an)zàr. fierce sturg. fifteen panzdah. fifty panjāh. jig anjīr. fight (n.) Jang, nibard, pahikafišn; v. battle, combat. fight (v.) éraxtan, nibardidan, pahi- kār-, P rān-; make ~ pahika
šast >> īdan, !doxtan. dēšag [dwsk'] dear, loving. —ih: love. došaram [dwi?m | M dw%’rm] love. dēšastar [dušstl] west. īdēšīdan, 458- [dws-ytn!] like, love. ~ign: liking, pleasure. *došidan [dwsytn'] = *dóxtan. dēšīzap [dwsyck' | (M дох,
haftād >>  rawiánt raftan! saxtag sabz šast” sī haštād* sagēn nawad* sēn sēnag sen murw sezd sézdén haftād* darr-t PAHLAVI KEY — AA Sri 33 süxtarih saxtih saxt saxtan, saxtan süg, sak say- sahigih sahig, sivag sas зап saxwan sahóg sak sárcn
haštād >> sahmgen sahmgenih sāstār sāstārīh rawen-! rawenidan! rawiánt raftan! saxtag sabz šast” sī haštād* sagēn nawad* sēn sēnag sen murw sezd sézdén haftād* darr-t PAHLAVI KEY — AA Sri 33 süxtarih saxtih saxt saxtan, saxtan süg, sak say-
nawad >> (īh) [xslwšt', -yh] pollution, corruption. nastaran [nstln' | N ~] dog-rose, sweet briar. nawad [90 | N —] ninety. nérógómand naxéir [nhcyl | M nhcyhr, Р nxcyr, N ~] game, quarry, chase. naxód [nhwt' | N ~] chick-pea. P naxsag [nh
sīh >> abér [yl] very, much. abē-rāh Payis] e erring. abesar [fysl | M ?bysr, N afsar] crown. abesīhēnīdan, abesihén- [Ashyn-ytn', v. abesihidan] destroy. išn(īh): destruction. abesihidan, abesih- Pžs(y)%-ytn! | M? bysyh-] perish, be des
dēnār >> ge. 0" гу -ģān [МТА-, dh? »'] = dahigàn. dën [dyn' | = M, N din] religion; cal. 24th day. dēnār [4ут/ | N dindr] (gold) dinar. dēn-āstawān [dyn’stwh’n'], dēn-burdār [dynbwit^l] believing, faithful. dénig [dyny&! | N dini] religiou
dah [ >> he second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čamb
dahom >> ] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creatio
sad [ >> greedy. ~ih : greed. sabuk [spwk! | N ~] light, easy. sabz [spz, sbz | N —] green, fresh. sad [roo | M sd, N ~] hundred. Sadwés [stwys | M sdwys] a star (Fomalhaut ?). ваб [KLBA < A klb | N ~] dog. Zeag [sk!] stone. sag [PR | P g]
```


## [2026-09-05T17:46:25.915Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\ni=t.find('dinar,  n.  Arab')\nleaf=t[:i].count('\\f')\nprint('leaf(0-based)=',leaf,'-> printed approx', (leaf-12)*2, (leaf-12)*2+1)\n# print running page numbers nearby\nprint(t[i-200:i+300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T17:46:27.736Z] TOOL RESULT

```
leaf(0-based)= 247 -> printed approx 470 471
rmed  with  -ier,  a  suff.  denoting  trade  or occupation,  fr.  Dinand  (now  Dinant),  a  town  in Belgium,  famous  for  its  brasswork.  For  the  end¬ ing  see  the  suffixes  -ier  and  -ery. dinar,  n.  Arab,  dindr,  fr.  Late  Gk.  Srjvdcpiov,  fr. L.  denarius.  See  denarius  and  cp.  denier, dine,  intr.  and  tr.  v.  —  ME.  dinen,  fr.  OF  disner (F.  diner),  ‘to  dine’,  orig.  ‘to  breakfast’,  fr. * desjuner ,  shortened  form  of  desjejuner  (see haplology ),  which  der
```


## [2026-09-05T17:46:40.686Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('KLN_1971.txt',encoding='utf-8',errors='replace').read()\nprint('leaves',t.count('\\f'))\ni=t.find('dinar, n. — Arab')\nprint('leaf',t[:i].count('\\f'))\nprint(t[i-300:i+200].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T17:46:42.534Z] TOOL RESULT

```
leaves 0
leaf 0
udge’. See Dan, PN.   dinanderie, n., decorated articles of brass. — MF.  (= F.) fr. OF. dinandier , ‘worker in brass’,  formed with -ier, a suff. denoting trade or  occupation, fr. Dinand (now Dinant), a town in  Belgium, famous for its brasswork. For the end-  ing see the suffixes -ier and -ery.  dinar, n. — Arab, dindr , fr. Late Gk. Siqvdpiov, fr.   L. denarius. See denarius and cp. denier,  dine, intr. and tr. v. — ME. dinen, fr. OF disner  (F. diner), ‘to djne’, orig. ‘to breakfast’, fr.
```


## [2026-09-05T17:46:48.631Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^dekm\\|dekm̥\\|dek̥m\\|^deḱm\\|DECEMBER\\|dekm-\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-05T17:46:48.683Z] TOOL RESULT

```
362:DECENT. 2. Suffixed (causative) o-grade form *dok-eye- in: a. Latin docére, to teach (< “to cause to accept”): DOCENT, DOCILE, DOCTOR, DOCTRINE, DOCUMENT; b. Greek dokein, to appear, seem, think (< “to cause to accept or be accepted”): DOGMA, (DOGMATIC); DOCETISM, DOXOLOGY, HETERODOX, ORTHODOX, PARADOX. 3. Suf- fixed form *dek-es- in: a. Latin decus, grace, ornament: (DECOR), DECORATE; b. Latin decor, seemliness, elegance, beauty: DECOROUS. 4. Suffixed form *dek-no- in Latin dignus, worthy, deserving, fitting: DAINTY, DEIGN, DIG- NITY; CONDIGN, DIGNIFY, DISDAIN, INDIGN, INDIGNANT, INDIGNATION. 5. Reduplicated form *di-dk-ske- in Latin discere, to learn: DISCIPLE, (DISCIPLINE). 6. Greek dekh- esthai, to accept: PANDECT, SYNECDOCHE. 7. Greek dok- os, beam, support: DIPLODOCUS. [Pok. 1. dek- 189.] dek-2. Referring to such things as a fringe, lock of hair, horsetail. 1. Suffixed o-grade form *dok-lo- in Germanic *taglaz in Old English teg(e)l, tail: TAIL!. 2. Perhaps Germanic *tag- in: a. Swedish tagg, prickle, akin to the Scandinavian source of Middle English tagge, pendent piece: TAG!; b. Middle High German zacke, nail (> German Zacken, point): SHAKO; Cc. Old French tache, fastening, nail: TACHE, TACK!. [Pok. 2. dek- 191.] dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN; b. Old Norse an, ten (see oktd(u)). 2. Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECI- MAL, OCTODECIMO, SEXTODECIMO. 3. Irregular Latin distributive dani, by tens, ten each (formed by analogy with néni, nine each): (DENARIUS), DENARY, (DENIER?). 4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON. II. Extended form *“dekmt- in Germanic *-tig in Old English -tg, ten (see dwo-). III. Ordinal number *dekmto- in Germanic *te- guntha- in Old English teogotha, téotha, tenth: TENTH, (TITHE). IV. Suffixed zero-grade form *-dkm-ta, reduced to -kmtd, and lengthened o-grade form *-dk6m-ta, re- duced to *-kontd. 1. Latin -gintd, ten times: NONAGE- NARIAN, OCTOGENARIAN, SEPTUAGINT, SEXAGENARY. 2. Greek *-konta, ten times: PENTECOST. V. Suffixed zero-grade form *dkm-tom, hundred, reduced to kmtom. 1. Germanic *hundam, hundred, in Old English hundred, hundred (-red, from Germanic *radam, number; see ar-): HUNDRED. 2. Germanic *thiis-hundi, “swollen hundred,” thousand (see teue-). 3. Latin centum, hundred: CENT, CENTAL, CENTAVO, (CENTENARIAN), CENTENARY, CEN- TESIMAL, CENTI-, CENTIME, (CENTNER), CENTUM, CEN- TURY; CENTENNIAL, PER CENT, QUATROCENTO, SEICENTO, (SEN!), (SEN2), (SENITI), SEXCENTENARY, TRE- CENTO. 4. Greek hekaton, a hundred (? dissimilated from *hem-katon, one hundred; see sem-'): HECATOMB, HECTO-. 5. Avestan satam, hundred: SATEM. See also compound root wikmti. [Pok. dekm 191.] deks-. Right (opposite left); hence, with an eastward orientation, south. Suffixed form *deks(i)-tero- in Latin dexter, right, on the right side: DESTRIER, DEXTER, DEXTERITY, DEXTRO-; AMBIDEXTROUS. Compare ner-'. [In Pok. 1. dek- 189.] del-'. Long. Probably extended and suffixed zero-grade form *dlon-gho-. 1.Germanic *langaz, long, in: a. Old English lang, long, long (comparative lengra): LINGER, LoNG!; b. Old High German lang (> German Jang), long: LANGLAUF; C. Old English denominative langian, to grow longer, yearn for: LONG?; d. Latin compound Lon- gobardus, Langobardus (with Germanic ethnic name *Bardi): LOMBARD. 2. Germanic abstract noun */lang- ithé in: a. Old English lengthu, length: LENGTH; b. West Germanic */angitinaz, lengthening of day, in Old English lengten, lencten, spring, Lent: Lent; ¢. Dutch lenghe, linghe, “long one,” akin to the Low German source of Middle English lenge, ling, ling: LING}. 3. Latin longus (> French long), long: LONGERON, LONGITUDE; ELOIGN, ELONGATE, LONGEVITY, LUNGE, OBLONG, PROLONG, PUR-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
```


## [2026-09-05T17:46:49.382Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"TEN\\.\\|ten\\. \\[\" AHD_watkins1985.txt | head; echo ===; grep -n \"dekm\" AHD_watkins1985.txt | head"
}
```


### [2026-09-05T17:46:49.468Z] TOOL RESULT

```
Exit code 1
512:CICHLID. 3. Greek khelidw6n, khelidén, the swallow: CELANDINE. [Pok. ghel- 428.] ghel-2. To shine; with derivatives referring to colors, bright materials (probably “yellow metal”), and bile or gall. I. Words denoting colors. 1. Suffixed form *ghel-wo- in Germanic *gelwaz in Old English gealu, yellow: YELLOW. 2. Suffixed variant form *ghlé-ro- in Greek khioros, green, greenish yellow: CHLORO-; CHLORITE!. 3. Suffixed variant form *ghlo-wo- in Greek khloos (< *khlo-wo-s), green color: CHLOASMA. 4, O-grade form *ghol- in Russian zola, ashes (from their color): PODZOL. II. Words denoting gold. 1. Suffixed zero-grade form *ghl-to- in Germanic *gultham, gold, in: a. Old English gold, gold: GOLD; b. denominative verb *gulthjan in Old English gyldan, to gild: GILD!; c. Middle Dutch gulden, golden: GUILDER, GULDEN; d. Old Norse gulinn, golden, akin to the possible source of Middle English gollan, yellow flower: GOWAN. 2. Suffixed o-grade form *ghol-to- in Polish zloto, gold: zLoTy. 3. Suffixed full-grade form *ghel-i- in the unknown Iranian source of Syriac zarnikd, orpiment: ARSENIC. III. Words denoting bile. 1. Suffixed o-grade form “ghol-no- in Germanic *gallon-, bile, in Old English gealla, gall: GALL!. 2. Suffixed o-grade form *ghol-& in Greek kholé, bile: CHOLE-, CHOLER, (CHOL- ERA); ACHOLIA, MELANCHOLY. 3. Suffixed full-grade form *ghel-n- in Latin fel, bile: FELON?. IV. A range of Germanic words (where no preforms are given, the words are late creations). 1. Germanic *glaimiz in Old English glém, bright light, gleam: GLEAM. 2. Middle High Ger- man glimsen, to gleam, akin to the source of Middle English glimsen, to glimpse: GLIMPSE. 3. Swedish dialec- tal glinta, to shine, akin to the source of Middle English glent, a glint: GLINT. 4. Swedish glimra, akin to the source of Middle English glimeren, to glimmer: GLIM- MER. 5. Old Norse glitra, to shine: GLITTER. 6. Old English glisnian, to shine: GLISTEN. 7. Middle Dutch glisteren, to shine: GLISTER. 8. Germanic *glasam, glass, in Old English gles, glass: GLASS, GLAZE. 9. Germanic *glaz- in Middle Low German glaren, to glisten, akin to the source of Middle English glaren, to glitter, stare: GLARE!. 10. Icelandic glossi, a spark, perhaps akin to the source of GLoss!. 11. Old High German glanz, bright: GLANCE2. 12. Old Norse gléggr, clear-sighted: GLEG. 13. Germanic *gladaz in Old English gled, shining, joyful: GLAD. 14. Germanic *gleujam in Old English gléo, sport, merriment: GLEE. 15. Old English gléd, ember: GLEED. 16. Germanic *gié- in: a. Old English gléwan, to glow: GLow; b. Norwegian dialectal glora, to gleam, stare, akin to the probable source of Middle English gloren, to gleam, stare: GLOWER; C. Old Norse glotta, to smile (scornfully), perhaps akin to the source of GLOAT. 17. Germanic *glé-m- in Old English glém, twilight: GLOAMING. 18. Possibly distantly related is Germanic *glidan, to glide, in: a. Old English glidan, to slip, glide: GLIDE; b. Old French glier, to glide: GLISSADE; c. Old High German glitan, to glide: GLITCH; d. derivative Germanic “glidén- in Old English glida, kite (< “gliding, hovering bird”): GLEDE. 19. Middle Low German glibbe- rich, slippery, possibly akin to the source of GLrB. [Pok. 1. &hel- 429.] ghel-. To cut. 1. Germanic “galdjan, to castrate, in Old Norse gelda, to castrate, and geldingr, a castrated ani- mal: GELD!, (GELDING). 2. Germanic *gulti- in Old Norse gyltr, a sow (< “castrated pig”): GiLT?. [Pok. 2. ghel- 434.] gheldh-. To pay. Only in Germanic and Slavic. 1. Ger- manic *geldam, payment, in: a. Old English geld, gield, payment, service: GELD?; DANEGELD, WERGELD; b. Old High German gelt, payment, reward: GELT!. 2. Germanic *geldan, to pay, in Old English gieldan, to pay, yield: YIELD. 3. Germanic *geldjam, payment, contribution, hence an association founded on contributions, a crafts- men’s guild, in Old Norse gildi, guild: GuILD. [Pok. ghel-t6 436.] ghelegh-. A metal. Possible root of Greek khalkos,
638:kleu-1, To hear. I. Extended form *kleus- in Germanic *hleuza- in Old English hléor, cheek (< “side of the face” < “ear”): LEER. II. Zero-grade form *klu-. 1. Germanic *hlustjan in Old English Alystan, to listen: LIsT*. 2. Ger- manic *hlusin6én in Old English Alysnan, to listen: LIs- TEN. 3. Suffixed lengthened form *kli-to- in Germanic *hlidaz, “heard,” loud, in: a. Old English Alid, loud: Loup; b. Old High German Aldti, sound: ABLAUT, UM- LauT. III. Suffixed form *klew-yo- in Greek kleiein, to praise, tell: Cio. [Pok. 1. Rleu- 605.]
814:fana, flag, banner, weathercock: VANE; b. compound *gund-fanon-, “battle-flag” (see ghen-'). 2. Extended form *panno- in Latin pannus, piece of cloth, rag: PANE, PANEL. 3. Possibly Greek pénos, web (> Latin pdnus, a swelling): PANICLE. [Pok. pan- 788.] [pandoura. Three-stringed lute. Greek noun of obscure origin. BANDORE, MANDOLIN, PANDORE.] pant-. All. Attested only in Tocharian and Greek. Greek pas (neuter pan, stem pant-), all: PAN-, PAN; DIAPASON, PANCRATIUM, PANCREAS. [In Pok. 1. keu- 592.] pap-'. Teat (sound symbolism). Probably the same word as pap-2. 1. Middle English pap(pje, nipple: Pap}. 2. Latin diminutive papula, pimple (diminutive papilla, nipple): PAPILLA, PAPULE. 3. Variant form *pup(p)- in Latin piipus, boy, and pupa, girl: puPA, PUPIL. [In Pok. barb- 91.] pap-?. Food (baby-talk root). Reduplication of pa-. 1. Germanic nasalized form *pamp- in Flemish frequen- tative pamperen, to cram with food, akin to the source of Middle English pamperen, to pamper: PAMPER. 2. Latin pappa, food (> Middle English pap, soft food): PAP?, POPPYCOCK. [Pok. pap(p)a 789, ba*mb- 94.] papa. A child’s word for “father,” a linguistic near-uni- versal found in many languages. 1. French papa, father: PAPA. 2. Greek pappas, father, and pappos, grandfather: PAPPUS, POPE. [Pok. pap(p)a 789.] paso-. Kinsman by marriage. Latin parri- (for pari-) in compound parri-cida (oldest form paricidas), murderer of a near relation: PARRICIDE. [Pok. pdso-s 787.] past-. Solid, firm. 1. Germanic *fastuz, firm, fast, in: a. Old English fest, fixed, firm: FAST!; STEADFAST; b. Middle Dutch vast, firm, fast: AvAST. 2. Germanic *fastinon, to make firm or fast, in Old English festnian, to fasten, establish: FASTEN. 3. Germanic *fastén, to hold fast, observe abstinence, in: a. Old English festan, to abstain from food: rasT?; b. Old Norse fasta, to abstain from food: BREAKFAST. [Pok. pasto- 789.] pau-. Few, little. I. Adjectival form *pau-, few, little. 1. Germanic *fawaz in Old English féawe, few: FEW. 2. Suffixed form *pau-ko- in Latin paucus, little, few: PAUCITY, POCO. 3. Suffixed form *pau-ro- in metathetical form *par-wo- in Latin parvus, little, small, neuter parvum, becoming parum, little, rarely: PARAFFIN, PAR- vovirus. 4. Compound “pau-paros, producing little, poor (*par-os, producing; see pere-'), in Latin pauper, poor: PAUPER, POOR, POVERTY. II. Suffixed reduced variant form “pu-lo-, young of an animal. 1. Germanic *fulén- in Old English fola, young horse, colt: FOAL. 2. Germanic derivative *fuljé in Old Norse fylja, female colt: FILLY. 3. Latin pullus (probably with expressive gemination), young of an animal, chicken: POLTROON, PONY, POOL?, POULARD, PULLET; CATCHPOLE. III. Basic form *pau- and variant form *pi-, boy, child. 1. Suffixed form *pu-ero- in Latin puer, child: PUERILE, PUERPERAL. 2. Suffixed form “pi-sso- in Latin piisus, boy: PUSIL- LANIMOUS. 3. Suffixed form *paw-id- in Greek pais (stem paid-), child (> paideia, education): PEDO-?; ENCY- CLOPEDIA, ORTHOPEDICS. [Pok. pdu- 842.] paus-. To leave, desert, cease, stop. Greek pauein, to stop (> Latin pausa, a stopping): PAUSE, (PESADE), (POSE!); COMPOSE, DIAPAUSE, (REPOSE!). [Pok. paus- 79.] ped-'. Foot. I. Nominal root. 1. Lengthened o-grade form *pod- in Germanic *fot- in Old English fot, foot: Foor. 2. Suffixed form *ped-ero- in Germanic *feteré in Old English fetor, feter, leg iron, fetter: FETTER. 3. Suffixed form *ped-el- in Germanic *fetel- in Old High German vizzelach, fetlock, akin to the Germanic source of Middle English fitlock, fetlock, fetlock: FETLOCK. 4. Basic form *ped- in Latin pés (stem ped-), foot: PAWN2, -PED, PEDAL, PEDATE, PEDESTRIAN, PEDI-, PEDICEL, PEDUNCLE, (PEON), PES, PIONEER; MILLIPEDE, SESQUIPEDALIAN, TRIPEDAL, TRIVET, VAMP!. 5, Form *ped-yo- in: a. Latin expedire, to free from a snare (ex-, out of; see eghs): EXPEDITE; b. Latin impedire, “to put in fetters, hobble,
1106:upo. Under, up from under, over. 1. Germanic *upp-, up, in: a. Old English up, uppe, up: uP; b. Old English up-, upp-, up=: UP-; C. Middle Dutch op, up: UPROAR. 2. Ger- manic *upanaz, “put or set up,” open, in Old English open, open: OPEN. 3. Germanic *ufana, “on, above,” in Old English bifan, above, over: ABOVE. 4. Possibly suffixed form *up-t- in Germanic *ufta, frequently, in Old English oft, oft: OFT, OFTEN. 5. Extended form *upes- in Germanic *ubasw6, *ubizwé6, vestibule, porch, eaves (< “that which is above or in front’), in: a. Old English efes,
(eval):1: == not found
```


## [2026-09-05T17:47:05.550Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint('nleaves',len(leaves))\nfor i in range(368,382):\n    p=leaves[i]\n    print('=== leaf',i,'approx printed',i+543)\n    print(p[:300].replace('\\n',' '))\nEOF"
}
```


### [2026-09-05T17:47:07.576Z] TOOL RESULT

```
nleaves 684
=== leaf 368 approx printed 911
   ‫سره‬                                                                                                         ‫دبافودا‬  ‫دابا * = بروزن زببا ‪,‬قماشی باشد از‬                                               ‫اول رو ز گذشته را گوند ‪. ۱‬‬  ‫ونابه از دیدارخوبان همهت ‪.‬‬                          ‫حر
=== leaf 369 approx printed 912
   ‫دور‬                                                                                                     ‫سس‬  ‫اس * ‪ -‬برای بیقطه وجیم‬                       ‫جیبر‬                          ‫د‬                              ‫بروزن سودا کر ‪ ۰‬تلم روز هشم است ازهر ماه ‪.‬‬   ‫بالف کشیده و سین مپ
=== leaf 370 approx printed 913
 ‫=‬                                                                                                    ‫دیع‬  ‫دیده بان ‪ ۲‬س بروزنبی‌زبان» همان‬                           ‫یدبدا س بفتح اول بروزن شیدا » بمعنی‬             ‫دیدیان است که بعربی ربیثه خوائند ‪.‬‬                                      ‫
=== leaf 371 approx printed 914
 ‫در ند‬                                                                                                      ‫‪۱۱‬‬ ‫ذیر ننگ س بنتح اول و تایقرشت‬                                         ‫ګلی امت که آنراکاو‬                                                                                       ‫دبد 
=== leaf 372 approx printed 915
 ‫‪n‬‬     ‫‪Sh‬‬                                                                                                  ‫دفر فف‬                                             ‫وطعام فز قف ‪.‬‬           ‫رزننده ‪ ۰‬بمعنی‬                                                                               ‫گبیرو‬
=== leaf 373 approx printed 916
 ‫دطروجاش‬                                                                                  ‫‪4‬‬    ‫سل‬    ‫خرش" د با فا ورای بشیطه‬                        ‫دیف د‬                      ‫حکمای بونان ‪ .‬گوبند نباتات و رحتنی را مسار‬  ‫بروزن فیل مخش ‪ ۰‬نام دوابی است امزوسیقی‪.‬‬                    
=== leaf 374 approx printed 917
 ‫‪-4۱-‬‬                                                                                      ‫دنگ‬                            ‫آهنین باشد ‪٩‬‏ ‪.‬‬       ‫واز بونه برآورند تفلکه در ته بوته مانده باشد‬  ‫د یگ بر دینگ = بکسراولوسکون‬                     ‫مرقشیشاست » وآنرا دیفروجس بحذف الف یز‬       
=== leaf 375 approx printed 918
                                                                                                                       ‫‪--‬ي ‪۱4‬‬   ‫بر وزن ریبوای » نرجمة‬                ‫دیماس ‪1‬‬                        ‫عربی سختی‬        ‫ر‬                                                                      
=== leaf 376 approx printed 919
  ‫‪6‬‬                                                                                                     ‫دیمیاد‬  ‫دلن ‪ - ۴‬بکر اول بروزن سین ‪ ۰‬نام‬                       ‫روشنی وضیا بود ‪ -‬وغله ای را نکیوزیند که با‬ ‫فرشته‌ابست که بمحافظت قلم مأموراست ‪ -‬و نام‬              ‫آب باران حاصل 
=== leaf 377 approx printed 920
                                                                                                            ‫‪۱۷‬‬    ‫دی ره ‪ -‬بضم باوزای‌فارسی وسکون‬                                  ‫است چه باز بسیار بزرکه راباونشبت دهند وباز‬ ‫که نام روز بانزدهم‬                  ‫ها مخفف دين پژوه است ‪۴‬‬     
=== leaf 378 approx printed 921
      ‫اه‬                                                                      ‫دبوار خانه روزن شدن‬  ‫آرا‬   ‫وسکون دوسین و فوقانی ‪ ۰‬دوابی است که ن‬                            ‫از قپر وغضب هم نوشته‌اند ‪.# ۷‬‬ ‫انده قوقو گونند وبرکلف وبهق مالند تبافاعشد »‬         ‫ررنو‌شدن‪ ».‬کناه‬            
=== leaf 379 approx printed 922
  ‫ديو دولت‬                                                                               ‫‪٩۱‬‬ ‫باشد ساء رتگك ‪ .‬چون‬       ‫کفته‌اند » و آن‌کرهی‬        ‫دیو پا ‪ - ۱‬با نانی مجهول وبای فارسی‬                                                       ‫بالف کشیده » عنکیوت‌را کو‌ند و نگایماهی‌هم‬  ‫ه
=== leaf 380 approx printed 923
  ‫‪۳‬‬                                                                                                     ‫ديو دید‬    ‫‪ = °‬بمعتی دیواسیت است‬       ‫د دوست‬                      ‫ت کنانه از دبواله ومحنون‬              ‫دلو د‬                                                                      
=== leaf 381 approx printed 924
  ‫دهیم‬                                                                                            ‫‪۲۱‬‬                 ‫هت که بعربی سنای گوبند ‪.‬‬                  ‫دیو کلو چ ‪ = ۱‬بضم کاف ولام بواو‬  ‫دو مشنگ‪ -‬بفتح میم وشین‌قطه‌دار‬                               ‫ډ‬
```


## [2026-09-05T17:47:16.311Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nimport re\nfor i,p in enumerate(leaves):\n    if 'دینار' in p or 'دينار' in p:\n        print('leaf',i,'printed~',i+543)\n        for line in p.split('\\n'):\n            if 'دینار' in line or 'دينار' in line:\n                print('   ',line.strip()[:250])\nEOF"
}
```


### [2026-09-05T17:47:18.301Z] TOOL RESULT

```
leaf 175 printed~ 718
    ‫درق را بپانزده هزار دینار [ک] بنتدلد درمدتی خجاره»‬                       ‫‪* - ۱‬رباز فروختن او یمی‬
leaf 296 printed~ 839
    ‫در سمی ‪ = ۸‬بذم اول و فتح الث بر‬                   ‫صحیح‌خوانند؟ ‪-‬وبمعنی درهم ودینار وزری‌باشد‬
    ‫‪- ۸‬پپلوی‬               ‫‪.‬‬   ‫» درشته‬    ‫درصه‬     ‫رك‪:‬‬     ‫‪۷‬‬                 ‫‪- ۷‬رکه‪ :‬درست (درهم‌ودینار) ‪۰‬‬                           ‫‪6‬‬
leaf 376 printed~ 919
    ‫‪)۹۰۱‬‬   ‫‪۹۰۱2‬‬   ‫ص‬   ‫ج‪۱‬‬   ‫اسلام؛ و( ارزش دینار و تومان در فرون مختلفه ‪ .‬مقالات کسرری‬
leaf 377 printed~ 920
    ‫دینار اشمر (‪-‬ر دینار شمر سراف‬
    ‫شمرندء ) ‪.‬‬       ‫شمر ( ائمرنده ‏‬          ‫از‪ :‬دینار ‪ +‬اشمر‬         ‫‪۱‬‬
leaf 410 printed~ 953
    ‫وطریق وبآین وچیزیت که بدان دینارها را جلا دهند وته‌فا‪ .‬وآن چربی است کنده که انبارهارا‬
```


## [2026-09-05T17:47:23.667Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nprint(leaves[376])\nEOF"
}
```


### [2026-09-05T17:47:25.559Z] TOOL RESULT

```
  ‫‪6‬‬                                                                                                     ‫دیمیاد‬

‫دلن ‪ - ۴‬بکر اول بروزن سین ‪ ۰‬نام‬                       ‫روشنی وضیا بود ‪ -‬وغله ای را نکیوزیند که با‬
‫فرشته‌ابست که بمحافظت قلم مأموراست ‪ -‬و نام‬              ‫آب باران حاصل مشود ‪ -‬و بمعنی باران وشم‬
 ‫روز بیست وچهارم بود از ماههای شمی ‪ .‬نيك‬                ‫حم آمده ؛ و بعضی گوبند بمعنی باران عربی‬
 ‫است درین روز فرزند بمکتب فرستادن و نکاح‬                                                              ‫‪١‬‏ ‪.‬‬    ‫ات‬
  ‫کیش‬
    ‫کردن ‪ - ۴‬ودر عربی بمعنی راه وروش و‬                 ‫هیا ‪۲-‬با بای حطی بروزن دبوزاد ‪.‬‬
                                                                                     ‫د‬
 ‫وعادت و فرمان برداری وشن وشو کت و مرتبه‬               ‫آنست که‬
                                                             ‫و آ‬             ‫باند‪.‬‬
                                                                                 ‫تکفسو ر‬          ‫غررور‬
                                                                                                      ‫ک‬
 ‫_ومالك ‪ ,‬یادشاه باشد ‪ -‬وبفتح اول هم درعربی‬
                                                        ‫اموال فانِةٌ خسبه را در نظر نیاورد وبربذل أن‬
                            ‫فرض و وام را گویند ‪:‬‬                                                  ‫فادر باشد ‪۱‬‬

 ‫دیا = بورزن بینا * نام خواهر بوسف‬                      ‫دمین = ‪,‬کر اول و انی مجهول بر‬  ‫ی‬
 ‫علیه‌اللام است ‪ -‬ویمه‌نی داور وداوری و فتوی‬             ‫وزن مين » چلك بازیرا گویند وآن دوچوب‬
                       ‫نوشتن حم آمده ات ® ‪.‬‬
                                                        ‫دار سه وجب و دیگری بقدر بك‬
                                                                                 ‫م یقکی‬
                                                                                      ‫ابست‬
‫د ينار ‪ = 1‬بر وزن بیمار » زر سرخ را‬                     ‫قبضه وهردوسر جوب کوچك تيز میباشد واکثر‬
‫همچو تمام‬        ‫همست‬
                    ‫‌تم‬
                      ‫می م‬
                         ‫هعن‬
                           ‫بم‬            ‫ام‬
                                          ‫تدم ‪-‬‬
                                              ‫وبن‬
                                                ‫گو‬     ‫طفلان‌بدان بازی کنند ؛ وبفتح اول هم‌بنظرآمده‬
‫ینجاه نابه نود که چپل باشد ‪ -‬وپرنده بزرکی‬                         ‫‪۰‬‬   ‫هم میگویند‬   ‫وآلرا دیمین جوب‬           ‫است‬




  ‫«دیمه کن اول» بارانی است که همشه میا بد درآراش ی رعد ویرق‌با در نگ‬                          ‫‪۱‬‬
   ‫میکند پنجروز بادش روزباهفت‌روز ‪,‬با روزی وشبی ‪...‬جمع آن ديم بروزن عنب» «شرح‌فاموس؟‪.‬‬
   ‫اوستا ‪ , 20680 -‬پېلوى‬             ‫‪۴‬‬        ‫ظ برساختهُ فرقه آذر کیوان ‪.‬‬           ‫‪۳‬‬             ‫‪۰‬‬   ‫دم‬     ‫رك‪:‬‬


   ‫‪ 0‬بازد‪ .1‬ارمنیم ‪«060‬اسشق ‪ .»۷۹۵‬دلنا ازمصدر اوستابی ڭڭ( شناختن و اندشیدن)‬
   ‫آمده که‌برایر است‌باريشة ‪ 01‬درسانسکریت‪ .‬دگراتپا ودیگر بخشهای اوستا مکرر کلمةٌ «دئنا»‬
   ‫آمده‪ .‬دین گدارتها بمعانی مختلف کیش‪ ,‬خصایص روحی‪ ,‬تخص معنوی ووجدان بکار رفته‪ .‬بمعنی‬
   ‫اخیر؛ دین یکی ازفوای پنجگانة باطن اسان است‪ .‬ویز نام ابزدی است از ابزدان آبین زرنشتی‬
   ‫و تگهبانی روز بیت و چهارم ماه بایزد دين سپرده شده ‪ .‬ابوربحان در فپرست نامهای روزهای‬
        ‫رده ‪:‬‬
            ‫ایرانی نام این روز را ‪۶‬دین ‪٩‬‏ و درسفدی حم ‪ +‬دین ‪ ۴‬و درخوارزمی نیز «دین؟ بکاد‬
               ‫میخور و شادی کن و خرمنشین ‪.‬‬                  ‫يتن‬
                                                              ‫دکف‬
                                                                ‫دن روز ای روی تو ‪ ۰‬آ‬
   ‫“‪06٦٦‬‏ ‪.‬‬    ‫‪« .‬مسعود صعد‬                                   ‫‪۱‬‬

  ‫اما دین در عریی از ره ذخ و ماشو از زبانهای سامی است ‪ .‬تازبان این کلمه را‬
   ‫مح الواسطه از زبان | کدی گرفته‌اند ‪ .‬در زبان اخیرکلمات ‪ 1۷0۵0‬و ‪ 111‬بعنی فانون وحق‬
   ‫وداوری‌است» ‪ 0۷‬بمعنی حکم کردن و "‪ 2120‬بمعنی قاضی است ‪ .‬درعبری و آرامی‬
   ‫‪ 8‬و ‪ 2814‬بمعنی قالون وحق وداوری است‪ 08/121 .‬و ‪ 202120‬بمعنی‌حاکم و قاضی‪.‬‬
    ‫‪۲‬ص ‪ « ۹۵۱-۹۹۱‬روز شماری ‪۵۵-۷۵۲‬‬                  ‫دین و دبان از آرامی وارد زبان عربی شده ‪ « .‬بشتپا‬
   ‫‪ ۵‬هزء ‪ 8014‬پهلوی ‪ » 02056020‬داوری‪,‬‬                     ‫‪ ۴‬رك‪ :‬دى‪.‬‬            ‫ورك‪ :‬داثرة المعارف‌اسلام‪ .‬‏‬
  ‫از‬     ‫‪ - ۱‬پپاوی ‪ « ۲82061‬تاوادیا ‪۰۹۱‬‬                 ‫حکم «بولکر ‪۹۷٩‬‏ ورك‪ :‬دین(درزبانهای سامی)‪.‬‬
   ‫لاتینی ‪ 511180621‬بتقدیر ‪ 510101110‬بمعنی «نقدی برابر ده‌آی» چه در اول وضع آن ازنقره‬
   ‫ومساوی ده‌ای ‪ 88‬بودو آس ازنقود مسین بود» وبعدها دتاربوی بمعنی خودآی استعمال شد «نقود‬
   ‫برای ارزش دبنار ‪ ۰‬رك ‪ ۳‬داگرة المعارف‬        ‫‪€: +‬‬     ‫“معرب آن حمدنار هری ج ص‪۳۱‬‬                      ‫ج‬      ‫ص‬

              ‫‪)۹۰۱‬‬   ‫‪۹۰۱2‬‬   ‫ص‬   ‫ج‪۱‬‬   ‫اسلام؛ و( ارزش دینار و تومان در فرون مختلفه ‪ .‬مقالات کسرری‬
```


## [2026-09-05T17:47:47.376Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt; do echo \"== $f\"; grep -c \"دوجین\" $f 2>/dev/null; grep -o \".\\{80\\}دوجین.\\{120\\}\" $f 2>/dev/null | head -3; done"
}
```


## [2026-09-05T17:47:48.671Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== HRN dah/bist\"; grep -n \"dah 'zehn'\\|zehn\\b\" HRN.txt | head -10; echo \"== HUB\"; grep -n \"zehn\" HUB.txt | head -10"
}
```


### [2026-09-05T17:47:49.260Z] TOOL RESULT

```
== MON_part1.txt
1
== MON_part2.txt
0
== incoming/MON/MON_2vol_Adena_v1_djvu.txt
1
== incoming/MON/MON_2vol_Adena_v2_djvu.txt
0
```


### [2026-09-05T17:47:49.338Z] TOOL RESULT

```
== HRN dah/bist
407:aus G. zu nehmen ist: ^Dem Rustem gab zehn Ammen der Löwe (d. L
2750:280. panzde 'fünfzehn , vergl. pänsed 'fünfhundert'.
2751:aw. paücadasa 'fünfzehn; skr. pdflcada^a; phlv.
5264:587. deh zehn, dehum, )^Dinn (Is. 37, 30)2).
5265:aw. dasa zehn', dasema-; phlv. dahuw; ai. r/ara,
5266:dafamci-; arm. ^as« *zehn' (H. No. 270).
6640:763. si^deh 'dreizehn*.
6700:770. sdnzdeh sechzehn'.
9079:1048. nuväzdeh 'neunzehn*.
9081:ai. ndvadasa 'neunzehn .
== HUB
1150:262. Lies *zehntausend' (statt 'tausend*).
1230:280. Np. pan^dah 'funfzehn' hat doch horbares h (wegen-^ 37 —
1231:dah *zehn), wie auch Vullers angiebt. Vgl. paz.
1232:paMahum *der funfzehnte* (Min. 61. p. 161), jud. tat.
1233:pazdeh *funfzehn' (Miller p. 76).
2753:763. Dazu bal. LW. slBnzdah^) 'dreizehn, paz. sSzdahum 'der
2754:dreizehnte' Min. 61. 184. Also ist die altere np. Form
3640:offenbar von dah zehn erhalten wie hcfst *aeht' sein
4017:mesm gross*, kesin *klein', das *zehn im Dialekt von Semnan
4022:dah zehn; vizunid *ihr wisst*, zunCLdmun 'wissen, heze
```


## [2026-09-05T17:47:54.971Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '5264,5270p;6640,6650p;6700,6710p;9079,9086p' HRN.txt; echo \"=== bist/sad HRN\"; grep -n \"zwanzig\\|dreissig\\|vierzig\\|fünfzig\\|sechzig\\|siebzig\\|achtzig\\|neunzig\" HRN.txt | head -20"
}
```


### [2026-09-05T17:47:55.046Z] TOOL RESULT

```
587. deh zehn, dehum, )^Dinn (Is. 37, 30)2).
aw. dasa zehn', dasema-; phlv. dahuw; ai. r/ara,
dafamci-; arm. ^as« *zehn' (H. No. 270).
kurd. bei. LW. deh, dah; afj'. las; oss. d. t. das,
däsäm (106); wa/. das^ las, sar. dh, sij'n. J7s, te,
ya;ai. sangl. das, minj. LW. daÄ.
588. dih *Dorf*, vergl. dihgän (arab. LW. dihqän, arm.
763. si^deh 'dreizehn*.
aw. dridasa 'dreizehnter'; phlv. sicdahum^) (päz. seS,
sez"); ai. trdyödasa,
kurd. dausCf slzdeh (LW.); afy. dyärlas.
np. sizdeh ist eine Analogiebildung.
764. s~ui% 'Kummet'*).
aw. sima^ vergl. siimiSra- yt. 10, 125 (Geldner,
KZ. 25, 530 Note 200); ai. cdmyä- 'Jochbalken
(nach Geldner; PW. hat 'Zapfen, Holznagel, Keil,
1) Nach Nöldeke bei Hübsohmann, KZ. 23, 402.
^) In E^snadäsa^s Pärasiprakäga aus Akbar^s Zeit findet sich nur
770. sdnzdeh sechzehn'.
aw. /svasjlasa 'sechzehnter ; phlv. säncdahiim ^).
af/. späras ; kurd. LW. säfizdeh,
np. sänzdeh ist durch das ihm vorhergehende pämdeh
beeinflusst.
771. smie 'Kamm'.
Käs. K. yö\sen (?).
phlv. sänak 'Kamm' (AV.); gr. xrf4', icrivinv (Hesych),
indog. he-n (Hübschmann, ZDMG. 44, 560).
bei. sak *Kamm' (445), dagegen LW. sänug 'Pferde-
strieger (866).
1048. nuväzdeh 'neunzehn*.
aw. navadasa- neunzehnter; phlv. naväcdahum^);
ai. ndvadasa 'neunzehn .
^) Vullers s. v. Kaku hat aus dem FS sinnlos benesre,
2) VerKl. Seite 128 Note 6.— 235 —
kurd. LW. nözdeh neben dauneh; af/. nülas, nütias;
o»s. d. nätidäs, t. nudäs (205).
Np. nuväzdeh statt nudeh ist eine Analogiebildung.
=== bist/sad HRN
2585:254. bfst 'zwanzig. /^
2587:aw. vTsaiti- 'zwanzig ; phlv. vist;{ai, vingati-j arm.
3128:329. penjäh 'fünfzig'.
4178:454. rihil, 6ü 'vierzig*.
6621:760. st 'dreissig'.
6622:aw. drisatent 'dreissig; phlv. sih, päz. si\ ai. trincdt.
6786:781. sest, sest 'sechzig*.
6787:aw. yscasti- 'sechzig ; päz. säst (FPGl.); ai. saüi-,
9087:1049. ueved neunzig .
9088:aw. naoaiti' 'neunzig; phlv. uaoat; ai. navatl-,
9477:U()96. heStäd 'achtzig.
9478:aw. astaitl- 'achtzig*; phlv. Iiastät bezw. astclt.
9508:l/llOO. heftäd ^siebzig.
9509:aw. haptäiti' 'siebzig; phlv. haftät; ai. saptati-,
```


## [2026-09-05T17:48:08.131Z] TOOL CALL #35: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg114.png"
}
```


### [2026-09-05T17:48:08.589Z] TOOL RESULT

```

```


## [2026-09-05T17:48:08.586Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T17:48:23.764Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 114 -l 114 -r 400 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg114_400 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg114_400.png'); print(im.size)\n# french box region: in 1700-wide image approx x 670-840, y 935-955 -> scale 400/200=2 from the 200dpi(1700 wide?) \nim.crop((1300,1830,1800,1930)).resize((1000,200)).save('pg114_french.png')\nim.crop((650,1830,1300,1930)).resize((1300,200)).save('pg114_latin.png')\n\""
}
```


### [2026-09-05T17:48:27.437Z] TOOL RESULT

```
(3400, 4400)
```


## [2026-09-05T17:48:29.805Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg114_french.png"
}
```


### [2026-09-05T17:48:29.827Z] TOOL RESULT

```

```


## [2026-09-05T17:48:37.518Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg114_400.png')\nim.crop((780,2040,2000,2110)).resize((2440,140)).save('c_fr.png')\nim.crop((780,1870,1600,1940)).resize((1640,140)).save('c_germ.png')\n\""
}
```


### [2026-09-05T17:48:39.520Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:48:41.909Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_fr.png"
}
```


### [2026-09-05T17:48:41.967Z] TOOL RESULT

```

```


## [2026-09-05T17:48:41.965Z] INPUT

[Image: original 2440x140, displayed at 2000x115. Multiply coordinates by 1.22 to map to original image.]


## [2026-09-05T17:48:48.644Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg114_400.png')\nim.crop((780,2580,1450,2650)).resize((1340,140)).save('c_lat2.png')\nim.crop((780,1880,2600,1960)).resize((2730,120)).save('c_germ2.png')\n\""
}
```


### [2026-09-05T17:48:50.719Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:48:53.100Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_lat2.png"
}
```


### [2026-09-05T17:48:53.112Z] TOOL RESULT

```

```


## [2026-09-05T17:48:56.102Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_germ2.png"
}
```


### [2026-09-05T17:48:56.145Z] TOOL RESULT

```

```


## [2026-09-05T17:48:56.141Z] INPUT

[Image: original 2730x120, displayed at 2000x88. Multiply coordinates by 1.36 to map to original image.]


## [2026-09-05T17:49:09.570Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls | head -80; echo ---; ls incoming 2>/dev/null"
}
```


### [2026-09-05T17:49:09.628Z] TOOL RESULT

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
---
AHD
ARY
BLY
BQT
CEL
FFD
IRN
ISS
KGW
MAG
MFL
MON
OEW
PLA
PRT
_tessdata
TTS
TYL
VIE
WLD
ZAW
فرهنگ ریشه های زبان فارسی (2).pdf
```


## [2026-09-05T17:49:13.328Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== FVQ dinar\"; grep -n -i \"dinar\\|dīnār\" FVQ.txt | head -8; echo \"== LKT\"; grep -n -i \"dinar\" LKT.txt | head -8; echo \"== AFM\"; grep -n \"دینار\" AFM.txt AFM_alt.txt 2>/dev/null | head -5; echo \"== PLA\"; grep -rn \"دینار\" incoming/PLA/*.txt 2>/dev/null | head -5; ls incoming/PLA"
}
```


### [2026-09-05T17:49:13.448Z] TOOL RESULT

```
== FVQ dinar
1040:a thing which would hardly have been likely were they ordinary 
1043:ordinary mortal to encompass all its variety, 2 so it is no wonder if 
1946:the ordinary person. 
2872:was familiar, that the ordinary vernacular was inadequate to, express all these new 
8486:jLlo (Dinar). 
8490:A dinar. 
9365:were built up on it in the ordinary way. 
9973:It is used in the Qur'an both as an ordinary period of time an 
== LKT
== AFM
== PLA
PLA_asbaghi_1988_ia_djvu.txt
PLA_asbaghi_1988_ia.pdf
PLA_pages.txt
```


## [2026-09-05T17:49:14.949Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== IEC\"; grep -n \"dek̂m\\|deḱm\\|dekm\\|dekṃ\" IEC.txt | head -10; echo \"== SYN ten\"; grep -n \"13\\.11\\|13\\. 11\" SYN.txt | head -10"
}
```


### [2026-09-05T17:49:15.019Z] TOOL RESULT

```
== IEC
2128:deKomos ‘tenth’. Cf. de&m, deKmti-, dekm- tós. WP I, 785 Skt. da$amah; Av. dasomo; Oss. dásám; Per. dahum; OLat. decumus; Lat. decimus; Gaul. cf. petru-decam-etus ‘14th?; Ir. cf. deachmh- adh ‘tithe’; Cor. dega ‘tenth’; W cf. degf-ed ‘tenth; tithe’; Li. desimfs ‘decade, tensome'
2133:dekm, dekmti ‘ten’; dekmtis 'tensome, ten- group'. WP I, 785 Sk. da$an; da$at, da$atih; Gk. déka; dekáte; Av. dasa; Per. dah; Oss. dás; Arm. tasn; Ma- ced. cf. Désios ‘June’; Alb. -dhiet ( -teen' hence) dhiet, dhjetë ‘10; Lat. decem; Umb. desen-; Tokh. A cák, B cak; Gaul. -decam-; OBr. dec-; MIr. deich; dechmad; W deg; Cor. dek; Br. dék, dég; Go. taíhun, cpds. -tigun; OE ten; téoóa, teogeóa; OHG zëhan; ON tíu, tí-; tiund; OCS dese Li. dešimt; Latv. desmit; desmits. (Dunbar and others relate dekm to deK- ‘receive’, scil. ‘with both hands). See next
20332:uiKmti (uiKomti, uim) ‘twenty’. Cf. ui-, px. and dui-; dekmti, dekm. WP I, 313 Skt. vimčatí; Av. visaiti; Per. bist; Romani bi$; Arm. Kean: Tokh. A wiki, B ikän; Gk. eí- kosi; Dor. eíkati; Boeot. wikati; Lat. viginti; Mir and Ir. fithche, fiche; OW ugeint; W ugain; Br. ügent; Cor. ægans; Venetic queried vhougonta(h), pl. vhougontnah (?), id.
== SYN ten
23351:13.11 Quantity
23379:13.11 QUANTITY Grk. —_ xoabrns Goth. (managei) Lith. kiekybé
31428:13.11 Vorce (sb.)
```


## [2026-09-05T17:49:22.197Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8480,8510p' FVQ.txt"
}
```


### [2026-09-05T17:49:22.243Z] TOOL RESULT

```
religion, borrowed from the Iranian (Brockelmann, Lexicon Syriacwn, 
1516), giving us the same double usage as in Arabic, makes the 
probabilities seem in favour of the borrowing having been from a 
Christian source. 3 In any case it was an early borrowing for it is found 
not uncommonly in the early poetry. 4 

jLlo (Dinar). 

iii, 68. 

A dinar. 

The name of a coin, the Lat. denarius, Gk. 8r)vdpiov. The Muslim 
authorities knew that it was a loan-word and claim that it came from 
Persian, though they were not unanimous about it. al-Jawaliql, Mu'arrab, 
62, whose authority is accepted by as-Suyut!, 5 gives it as Arabicizcd 

lU 

from the Pors. Lo, but ath-Tha'alibl, Fiqh, 317, places it among the 

' x- 

words which have the same form in both Arabic and Persian. as-Suyuti, 
Muzhir, i, 139, places it among the words about which the philologers 
were in doubt, and Raghib, Mufntddt, 171 , while quoting the theory that 

it is of Pers. origin compounded from JO and jl, 6 yet gives his 

n
```


## [2026-09-05T17:49:23.449Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"دینار\\|دينار\" incoming/PLA/PLA_pages.txt | head -5; echo \"== SYN numerals\"; grep -n \"^13\\.1[0-9]* \\|TWENTY\\|13\\.14\" SYN.txt | head -20"
}
```


### [2026-09-05T17:49:23.505Z] TOOL RESULT

```
== SYN numerals
2563:ly meaningless infantile syllables pa and ma, with suffix added after the analogy of other pairs of contrasted relations, while the simpler forms with or without reduplication, like NE pa, ma, papa, mama, continued in use as pet names. Such infantile syllables or nursery words play a considerable role in the words of relationship. They give rise to pet names of loose application which may become specialized in various directions. A similar use of infantile syllables, es- pecially for ‘father’ and ‘mother’, is ob- served in languages from all over the world. Cf. Kretschmer, HFinleitung 353 ff., and, for Latin, Heraeus, Die Sprache der rémischen Kinderstube, Arch. lat. Lex. 13.149 ff.
23351:13.11 Quantity
23352:13.12 Numper
23353:13.13 WHOLE
23354:13.14 Every; Au (pl.)
23355:13.15 Mucu; Many
23356:13.16 More
23357:13.17 Lirruz (Quantity); Few (Number)
23358:13.18 ENnoucH
23359:13.19 Moxtirupr, Crowp
23360:13.192 Norte on oTHER Wonps ror A CoL- LECTIVE Bopy (of Persons, Ani- mals, or Things)
23379:13.11 QUANTITY Grk. —_ xoabrns Goth. (managei) Lith. kiekybé
23405:13.12 NUMBER
23429:13.13 WHOLE
23478:13.14 EVERY; ALL (pl.)
23511:13.15 MUCH; MANY (Where only one form is entered, this is also used, either in pl. or with pl., for ‘Many’)
23596:13.17 LITTLE (Quantity); FEW (Number) (Where only one form is entered, this is also used, either in pl. or with pl., for ‘Few’)
23612:neb ‘any, none’ = Ir. nech ‘any(one)’, fr *ne-k”os (neg. and pron. stem *k9., of. Ir. cach ‘every’, 13.14). Pedersen 2.212,
23631:13.18 ENOUGH (adj. or adv.)
23681:13.19 MULTITUDE, CROWD
```


## [2026-09-05T17:49:33.496Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FVQ_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if '(Dinar)' in p or 'Dinar).' in p:\n        print('leaf',i); print(p[:200])\nEOF\necho \"== SYN\"; grep -n \"13\\.3 \\|13\\.2 \\|NUMERALS\\|^Ten\\b\" SYN.txt | head -20"
}
```


## [2026-09-05T17:49:35.288Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT dasa\"; grep -n \"dasa- \\[Zahlw\\|dasa-,\\|vïsaiti\\|visaiti\\|xsvasti\\|haptāiti\\|haptaiti\\|astaiti\\|navaiti\" BRT.txt | head -20"
}
```


### [2026-09-05T17:49:35.462Z] TOOL RESULT

```
leaf 150
FOREIGN VOCABULARY OF THE QUR'AN 133
Eth. T with its verbal forms Rf V and f-ftfV (and Amharic
judge ; Tigrina &*! judfl c ) \ into Iranian, where we find the
Phlv. ideogram njy dena judgment, decree,
== SYN
23365:13.31 Norse on THE NUMERALS
23833:13.31. NOTE ON THE NUMERALS
```


### [2026-09-05T17:49:35.519Z] TOOL RESULT

```
== BRT dasa
2478:Stelle  der  kongruenten  Form  steht :  a)  das  i ;  —  iE  äbyö  frSrtt^  fr}r»m-ainti  asaonqm Neutr.  Sing.:  yüzim  .  .  aogS  data  .  .  x/a-  ..frtrvaBbyoYX.13.afi;  —  zugleich  zurück- '^nmcS  .  .  azimcll  ahyä  (statt  Du.)  ..'weisend:  asti'atjntö  ..  atihe  haxayü  frä- %wqm  mPtihi  ..vaSd>m{sA.)Y.2<).ia;  —  \yente  astvatjr?lahe  Yt.i'>.95;  —  dacnnm dva/sing  ..  qstqscä  .  .  yezT  ahyä^^  (statt'.,  atiihi  ..  kavaya  ..  daenayn  V./o.ig. Plur.) /ö/  mal  xsayehTY.44.\\i.; — duye  —  a)  mit  relativischem  Anschluss;  ama- navaiti  astanqm  (sd.)  .  .  däittm  ahmäicil  !'af6yö  acibyö  yazataHbvT'  yat  am»saeibyö harf^r?m  hrmi^ät  V.  74. 17.  b)  das  sp»^aAbyöYi.fj.^;  —  mmö  äbyö  döi'iräbyü
4439:j.  anairitay-  f.  Name  eines  Insekts,  das sich  auf  Hunden  aufhält:  duye  navaiti yaoidai'iTta  stiptibyasca  (sd.)  "riti- byasca  .  .  V.  i4.\T.
9867:•  j.  gao-8urä-  f.  'Reichtum  an  Rindern' (?) : TtrthrtrjnS  avi  imal  nmänpm  •räbyBijiV. als  IP.)  :^ar»nö  pairi.vsnnavaiti  (sd.)  Yt.
9947:■  j.  gaSwa-  m.,  gaSwä-  f.  'Hund,  Hün- din''' i)xa.:di^e  navaiti 'wqm{CiY,) pairi.- yaoidaikUa  stiptibyas£a{^^..'S.i4-  I7;  — bis  hapta  puhrqm  'wqm  (AP.)  uzjämöit (sd.)  V.  r4.  i6;  17;  —'  fra  mi  'wa  (NP. als  AP.)  sasayqn  mzbjnta  (sd.)  V,  8. 37.  2)  f.:  aiia  (näml.  hätrist)  ca%wan.- failißäna ya  'Tva'W .i^.iqGl.; — yaica  aisa toa  uÜrS-itänaisva /rajasät{sA.)  V.  15.23; — yS  °wqm  yqm  apu%Tqm  {sd.) /anaiä  vs ,.pasdaya/i{sd.)  vä  yaica  alsa  "wa  magye .  .  pai'jyäite  V.  Jj.  S ;  —  °wqm  yqm  apu- irqm  "^rayqm  *baesdri  "eine  Hündin,  die kürzlich  geworfen  hat,  . ,"  V.  15.49.
13026:Ableit.  aus  'diuaia-  n.;  mm  ksl.  V.  deii/i finden';  vgL  dasa-,  däsla-,
13926:7. 74  No.  i),  i,yiini  enthaltenen  Basis  idg.  V^|-.   V.  18. 73^  **,   Vd,  6;  —  duye  (Af.)^'  navaiti
15171:—  u^&m  tristem  mdansaynt  kavaMya 'ätalibya'^  V.6'.46;  5.11.  b)  von  Tieren: aal  as?m  tanBm  aguu  a^airi 'ähm^*  gjuf armaYtiy.$$.  c)  von  Dingen  (nur Komp.).  3)  'Versteil,  Vers':  ahunavaitim gahqm  .  .  mal  vayiibyaca  *'at3byasca^'* Yx.14.1.         S,  noch  zu  upasu.
18613:•  j.  ^nava  indekL''  Zw.  'neun':  ya^  Ai  'va (als  Nom.)  xsafna  lacantt  Y.g.  35,  ig.  23; i/i.  10,  1 1 ;  —  'va  (als  Akk.)  ptrüwS . . i^rmuFa  V.2.  ^o;  5.  $1,  ().ii,  ii.jaPüZ., 10.18,  14-14,  17-6',  /^.aiPüZ.,  22.ao', P.g,  Yt4-ö(?>,  /9.41;  —  °^'a  «/«  may^m'^ V.5,  54;  —  -zraÄ  yatkj  navaitisca  °vaca sata  'va^a  hatattra  navasSsea  (sd.)  batvqn y.22.3;  YL/j.  59;  —  'va^a  navaÜTm^a "99"  Yt5. 8a;  —  'va  sala  upäzananqm V.  ^,  15;  15;  —  'va  (als  Instr.)  satäts harta.cnanqni  V,  4.  9;  —  *°va  *sat-lts^^ hazannmla  Ytj.  120;  —  'va  (als  Dat) druJaiH  xsa^raaiyd  V.4.10  PuZ.(?);  —  1 'vaijqm  (Gen.)  aspatiqm  ar/ham  V.  22. , 30;  —  *m?nääidyäi  (sd.) . .  'va  dasmi  Y.
18628:•  j.  navaiti'vant-  Adj.  'neunzigütch':  'ni (näml.  asti  mt^fH)  antar?  inlhra  Yt  10.
18690:39,  79.69;  'Yt4-t,  Vyt.  74^;  —  duye navaiti  narqm  a/aonqm  vasiryaäa g^ . . - V.  74. 1 7 ;  A.  j.  7 ;  —  aü'hwSjgabmq  .  . narqm  aIaunqmY.13.3; — Sing.inkollekt. Sinn:  %rilum  nari  asaonS  frayoAuma- take  . .  apayasaitt  V.  18. 64.  c)'**  kas- na'^^  dtrita  tqmta  . .  avapastBt/ (sd.)  ks apB  . .  ks  .  .   iasnä'^^   "(welcher   Mann
19059:faitiAincaiti  a  dim  (sd.)  «°  apivalaite  dai- nayä  V.p.  52.  zu  V):  ys  mqm  :^ästqm n°  baxsahe  V.  JJ.  i ;  2 ;  —  yD  *'naire  .  .  n' paiti Jivtäiti 'S. 4c\  >t/j,  2p,  V.J. 28';  — ^yj  hs  n-  visaiti  */ramrBite  N.  13;  — yS  . . aiwyanhqm  (sd.)  ff  aiwyasti  nSit  (zu  1) ga^ri  sravayäli  nsit  (zu  I)  sps  .  .  yazaitt V. /Ä9;  —  yat  bs  paiti  .  .  naire  .  .  n' daoäiti  V._j.  35;  7.59,  lÄ  34;  —  ya'^a as>m  n'  /ra.nmane  Ytp.  4;  iü.öj; — yat isamnS  «•  vindaite  V.  i_y,  36;  2.4;  —  yezi ml  ri'  ifahät  spä  . .  V.  13. 49 ;  —  ynoi  sl hvar»  a°  utuxsyeiti  \t.6.y,  8.^2;  —  yeiöi zT  azim  ff  daiiyqm  .  .  asS  . .  V.  j.  i  j  — yaii  xt  mi  n°  daihl^  upastqm  ..Yt.13.12;
19201:•  j.  nivavant-  Adj.  (fem.  'vaitr-)  —?  —, käu  (nämL  kaine)  .  .  spanavaiti  'vaiti pasvaili  . .  V.  iq.  30.
19389:—  yaha  at^m  laurvaymi  vupe  yätavB  ,  . yat  mqm  na^ti taurvayat\x,i.^; —  Rica %wqm  cakana  .  .  htm  mqm  "/aiaaa  H. 2.12;  —  a  mqm  ava%a  vtrytunie  yaha anyasat  arlänS  avt  xhtdrh  xla%riAa hqm.V3r3navaititi  V./Ä.32;35;  —  s.  noch bei  3.  zu  I  b):  uHa  ba ytm  halahi  ula mqm  upatihal^i  Ytl^.j;  ~  mqm  sT mainyae yasaifm  Yt  10. 108 (?).  zu  a): paiti  mqm. .pinsanuAa yim  da%väaAim . . V.  /<?.  7 ;  Yt.  12. 3;  —  zugleich  zu  1  a):  y3 af>m  staoiti  hs  mqm  staetti  yim  aAurtm mazdqm  H. /.  3;?. /jj  —  ax^m  dalqm  .. tis'tnm  . .  av3ni?m  . .  ya%a  mqmcij  yim aAunm  masdqm  Yt  8.  50.  2)  AbL; b)  nur  u)  im  j  Aw.j  mana  als  AbL;  zu  2) :  at^B mana  yat  zardhusträi  V.2.r.  3)  Dat.; Bi)  imgAw.j  ei)«a/4)'a'';zu  i  a):  ääidi .. vikaspai  is^m  maibyäcä  Y.2Ä7;  8,  4g.%;
19592:•  j.  iiiaSav  n.  '(Wein  uzw.)  Beerenwein'  '* : gqm^a  ..yaom?a  . .  ''iula  ansptm  V.5. 52; 53>  54iF.  7/;    —    duye  navaiti  narqm  .
19698:•  j.  matp^rasav-  Adj.  (fem.  'svf-)  'mit den  Fragen  *'  versehen,  sammt  den  Fragen' : yasmm  . .  haptarahaittm  . .  'sUm  Vr.  id.  o; —  gähqm  ahunavaitim  ..  'svTm  Vr.  z^.  i.
19707:•  j.  inat.va£astaätay-  Adj.  'sammt  den StropbeD,  mit  allen  Stiophea':  yastam  . . haptaahäitlm  .  ,  mai.a/smamfn  *flm  Vr. iö.o;  —  ahunavaitim  gä%qm  .  .  mai.- afsmanqm  °tim  Vr.  14.  o  f.
20187:•  j.  mazga'vant-  Adj.  (fem.  •vaitl-)  'mit Mark  versehen':  raoynavaiti  °vaili  (VSf.) frazaintivaiti  V,  21. 7.
21368:•  j.  yaska-  m,  'Krankheit':  iä  'kim  'käi.. mahrkim  mahrkai  darayat  (sd.)  V. p.  5 1 ;  —  paitistliSe  'kahe  .  .  mahrkahe V.20.3;  £/.2;  —  kahmäi  °hmca  makr- i^müa  .  .  baxsäni  Yt  10.  iio,  14.  47;  V. 20.  7,  10;  —  äste  °ka  (als  AP.)  . .  alle makrka  V,  g.  48;  —  fräkirtnaot  anrS mainyus  navaca  'ks  navaitisia  navaüa  saia navaca  kazanra  navasSsca  (sd.)  balvqn ^.22,3-,  —  '£a  apa.dvarata  Yt.j.7
22154:nehmen':  vJsmU  aval  vlssnta^a  *mazyasat . .  fravaiayS  "sie  stellen  sich  dazu,  sie stellen  sich  auch  zu  noch  grösserem  be- reit . ."  YLiy.73;  —  at»m  aita  zaota  vUäi staotanqm  yesnyanam  frasraohnm^a . .  "ich will  es  als  Z.  übernehmen:  das  laute  Auf- sagen . ."  Vr._j.  7.  3)  '(herantreten  um zu  —  sva.)  sich  bereit  stellen,  dran,  drauf aus  gehen  (etwas)  zu  (tun),  es  übernehmen zu  — ,  bereit  sein  zu  — ',  mit  Inf.:  visaraha mi  .  .  mprvis  ifri/a(sd.)ca  dalnayili  V. 2. 3 ;  —  vlsaiti^''  dim  frayrSrayS  nStt frayräyräyätiisä.)  N.  ig;  —  visaiti^  ainyB "usyS  (sd.)  «JiV  ainyB  rviismnS  *llstrydte ava  *vlsaae*l  ^naihaxit  ästryeite  "der  eine zeigt  sich  bereit  zu  . .,  der  andere  nicht; der  sich  weigert,  versündigt  sich.  Sind beide  bereit,  so  geschieht  überhaupt  keine  ; Versündigung"  P.  57;  —  hyat  vUJntä  j (sPPrM.)  ängvant^m  avB  kyatcä  .  .  "weil ' sie  drauf  ausgehen,  dem  Z^ru^läubigen 'Propheten)  zu  helfen,  und  dass  (s.  3  a)  . ." Y.^2.  14;  —  nimahl  usSmahl  tumatihl vjsämaidi  V.  $8. 3.  a)  negirt  mit  Inf. a)  'sich  weigern  (etivas)  zu  (tun)':  yas^a  . . imq  vacS  nsit  *vfsaite''^  framrüile  i&A.)  Y. A4;  —  yS  hl  *ap)r3n3mnäi  (sd.)  nött vUäiti^  ''framrüiU  N.  /J;  —  vgl.  noch 3^Ts>mna-.  ß)  'es  nicht  fertig  bringen, nicht  vermögen  zu  (tun)':  t^it  vjsmte  asäni avasyäi  "nicht  vermögen  Steine  (ihn)  zu treffen"  Yt  /.  1 8  *'.  3  a)  'darauf  ausgehen dass  — '  {hya£):  hyat  vUSntä  dngvantjm "vff  (s.  3)  hyaliä  gäus  Jaidyäi  mraol  Y. ,?2.  14.  vliäi'>'>  FrD.  ö(?).  [vJs^rUi
22272:pars  vay&ibyö^'*  YLjo.88; —  *ao^rab}'B ariuxialibyasca  vSyiibyB^^  vufitn  .  . yazatitn  yasamaide  Y,i6.  i;  Vi.  6.  i,  Ny, J.  1 6;  —  Avamxiaft?m .  .yaxamaide  vacaca ^ao^naca  sao^rabyasca  N.1.16.  5)  Sing. JcaT*  K.  oder  mit  arsuxZa-,  miuxZa-  sva. mq'^ra-  (Sp.  1178  o.),  'das  Wort,  das wahlgesprochene  Wort':  yä^a  lia  väHm Milma  (Sp.  1067  o.)  ya'^a  vä  saoiyatits Y.  70. 4;  —  zara%uitrahe  .  .  yS  paoiryS vacim  aoxta  vldsyum  akurS.tkaistnt  Yt. y.go;  90;  —  ^TKuxlam  vacim  yat  frä- dai^gat^gm  yasamaide  S.  2.  iS'"';  G.  2.  6; —  uita  tl  nsii  pairi.frasa  (sd.)  >rpzuxhm *p?rgsahi  VäHm  Y.g.as.  6)  "Einzel- wort,  (Plur.)  Wörter'  uzw.  der  GiJhäs"'>: tiiranam  haurva.paoiryanqm  (sd.)  häiliSla afsmanäca  vacasca  va^astaslim{sA.)ca  Vr. y.  3;  —  *ey3mcit  .  .  väcitn  gä^anqm asrvUm  (sd.)  N.  103;  — yS  gä^anqm  Byam vScim  afayäiti  alvqnt  v3  vacastaltXm  N. 4s\  42;  — ys  asnitgaoia  v3  ajravaoco  va nBii  Sim  Smm  väcim  *aiwyHs  (Sp.  378  0.)  \ .  .  yezi  äat  Syumpt  *väam  *aiwyas  1 anaiwilfi  (sd.)  astryeite  N.  i4-  Undeut- liche oder  wertlose  Stellen:  sar^yO  vaxs FrW.fj.i;  —'kaityavaca  FrW.5.2; — yS kaca  damayät . .*apastv6it  '^rilvayzibis^'^ ^haktni. .  N. 41 "';  —  xsvas  vayeibis^i N. 6j,  /OJ'J';  —  aAunavaitim  gshqm  .  .yasa- maide..  mal  vay£iby3^Va'*>  *pdübyasca V1.14.1;  YLz,  II,  13  (vacqm).  S.  noch vacim  bes.
```


## [2026-09-05T17:49:41.660Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Zw\\.  *'zehn'\\|Zw\\. 'zehn'\\|Zw\\.  *'zwanzig'\\|'zwanzig'\\|'sechzig'\\|'siebzig'\\|'achtzig'\\|'neunzig'\\|'elf'\\|'dreizehn'\\|'sechzehn'\\|'neunzehn'\" BRT.txt | head -20"
}
```


### [2026-09-05T17:49:41.707Z] TOOL RESULT

```
6471:I»  j.  aätätay-  fem.  Zw.  'achtzig':  'täitim mai',yairyehe  (sd-)  da^u/iJ  T^rüraftiake A.J.  II.         a)    mit    Gen.:    'taitlm.    atrt.-
10969:•  j.  xävaStay-  fem.  Zw.  'sechzig':   °i auiS)ySis»mahe  (sd.)    tistryelie  da%usS    A. J.8.         3)  mit  Gen.  'tlm   ätn^aokanam V.Ä91;  J2.I-
13003:•  j.,  g.  da^  indekL'*  Zw.  'zehn':  'sa  (als Nom.)  aid^ra  matfAs  tayana  V.  j.  3; Vyt_9,  Az.5,  N.  42;  —  'sa  (als  Akk.) iW/:7   arimazains  \.44.i8;  —   'sa  pairi
24358:•  j.  visant-  fem.  Zw,  'zwanzig',  mit  Gen.: 'saiti  (AD.)  upazananqm  YL  70.  122;  V. i'.  95,  72. 13,  17;  —  pancäca  'saiti  dah- manqm  V.  72,  9.  a)  adj.  gebraucht: *°sqs  *ta(li^.)ca'i  imä  nam!nTs"aad  diese (genannten)  zwanzig  Namen"  Yt.  7. 19.
```


## [2026-09-05T17:49:51.444Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Zw\\. *'siebzig'\\|Zw\\. *'neunzig'\\|Zw\\. *'dreissig'\\|Zw\\. *'dreißig'\\|Zw\\. *'vierzig'\\|Zw\\. *'fünfzig'\\|Zw\\.  *'elf'\\|dasa-  *Zw\\|aOvan\\.dasa\\|xsvas\\.dasa\\|Bri.dasa\\|nava\\.dasa\" BRT.txt | head -20; echo \"== offsets\"; python3 -c \"\nimport json;d=json.load(open('../refs_online.json'));print(d['BRT'].get('page_offset'));print(d['BRT'].get('lookup_hint'))\""
}
```


### [2026-09-05T17:49:53.088Z] TOOL RESULT

```
11160:•  j.  ca9-war«-sant-  fem.  Zw.  'vierzig': ^a'^u/arasla  a^a  garayl  .  .  'satimca  (ab Nom.)''  dvai^a  saite  dvai^a  hazaj»re  "es gibt  so  2244  Berge"  Yt./p.?; — paruäla 'sat>mea  maiiysizarmtayehe  (%A^  . .  "45  . ." A.j.  7.  a)  mit  Gen.:  'sat?m  (Alck.)'* aiwigämanqm  V.  2.  41;  5. 93,  /2. 14,  *Y. 65.4»,  ^Vi/p.
15262:j.  pan^-sant- *>  fem.  Zw.  'fünfzig': paitica  hl  anya  dva  vä  nara  anhiti  panca vü  'sahm  (als  Nom.)''  va  V.  5.  27;  — aivam  va  avi  x^apamm  duyS  pJ  'satim (als'Akk.)')  va  YtÄii.  a)  mit  Gen.: ^  pasca  'satitn  sar^qm  V.  7,  48;  —  'sat»m \iitr?.saokanqm  V.S.gx;  4, 19',  6'.  13',  12.9, F. /o.  a)  adjekt  gebraucht:  ha^ra.. ^yazataiibyS  . .  'satblsca  sataista  . .  Vr.  Ä  i, I  KompA. ;  Ableit  —  ai.  fonoiiäl-  f.,  np. /on- I  jäh  i).  —  Pü.  i  SO.  —  »  Mit  fl  lu  F.  und  Vr. —  ')  Vgl.  lu  %titanl:  —  3)  S  ^ro  udW.
18629:KompA.  (1.  aoch  *itaimaya);  Ableit  —  ai. näva  (Gen.  navänani),  PDw.  »au ;  np.  vgL ituAii).  —   Pü.;  nöhO.g.  —  i)  S,  aber  Gen.  |  •   j.  nava.dasa-   Adj.   'der  neunzehnte'
18634:Ableit.  aos  *nava.dasa  indekl.  Zw. '19'.  —  ai. navadaiä-  Adj.;  woss.  vgl.  näudäs  '19'.  — Pü,:  navazäahnm.
29801:Anfang  der  Vers  abschnitte  s.  Bthl.  af.  3.  i  Verdienst  im  Gedächtnis  hast,  O  M.,  du 23.  —  3) Tu.:  ia  iFnin  i  Jrvttm/än.. ei  daiänlvf sisst   CS    durch    den    besten    Sinn"   Y. ^ästär  .  .  atiänik'ik.     Undeutlich.  —  4)  Oder  |_^2.  6;  —  xsvas.dasa   'rmis"  Yt,  I.  8. ■^  larätiay-,    'martnay-   Adj.,   imn   V.  >
== offsets
Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
```


## [2026-09-05T17:50:05.946Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"daθa\\|'ten'\\|ten (numeral)\\|θritīya\\|navama\" KNT.txt | head -20; echo \"== KNT dasa\"; grep -n \"dasa\\b\" KNT.txt | head -10"
}
```


### [2026-09-05T17:50:06.015Z] TOOL RESULT

```
2364:IV. Nine: nsm. navama ‘ninth’ is identical with Skt. navamá-s, and is formed from the ordinal pIE *neyn, Skt. ndva, in imitation of "debemos to *dekm, cf. Skt. daSamd-s to dasa, Lt. decimus to decem. The - in ‘nine’ is seen in the Lt. ordinal nonus, from *nouenos.
2955:With an adverbial expression the present may, as in other languages, indicate time begun in the past and extending into the present, and the im- perfect stmilarly may express time begun їп a re- moter past and extending into a nearer past; the best examples are in DB 1.7 hacd paruviyata ётйй amahy һас paruniyata hya améxam taumā a Sdyahiyd cha ‘from long ago we are (= have been) noble, from long ago our family was (= had been) royal (or kings)’, and 9-11 VIII manā tawmaya tyaiy paruvam xsdyahiyd cha adam navama IX duviláparanam xsdyahiya amahy ‘8 of my family (there were) who were (= had been) kings; I (am) the ninth; 9 in succession we are (= have been) kings’.
3149:0816. Sryzistic Omissions occur in OP, es- pecially of the copula when there is a predicate adjective or phrase; cf. §275, §276. Examples: DB Lf Cišpäãiš pita (sc. cha) Hazàmanis; 1.9 VIII mand іаитӣуӣ (ве. dha") tyaty . . .; 1.10 adam (sc. amiy) navama; 1.13 ima (se. ha*tiy) dahydva tyaty ‚..} 1.15 tyaty drayahyá (ве. ha*tiy; or possibly daraya"tiy, сї. XPh 23f); 1.27 ima (sc. astiy) tya mand kartam (se. astty).
3469:10 : xSayafiyaé : dha : adam : navama : IX : duvitiparanam : vayam : хёйуай
5603:navama- adj. ‘ninth’: Ау. паота-, Skt. navamá-, pAr. navama- remade from pIE neyeno- after pAr. dasama- ‘tenth’ ($14911, $204IV), ef. Lt. nénus.  navama пзш. DB 1.10; DBa 10f.
== KNT dasa
2364:IV. Nine: nsm. navama ‘ninth’ is identical with Skt. navamá-s, and is formed from the ordinal pIE *neyn, Skt. ndva, in imitation of "debemos to *dekm, cf. Skt. daSamd-s to dasa, Lt. decimus to decem. The - in ‘nine’ is seen in the Lt. ordinal nonus, from *nouenos.
3072:I. The enclitic pronouns are attached to the first word of their sentence or clause or phrase, even though this be шй ‘and’: DB 1.25 Aura- mazdü-maty upastém frabara ‘Ahuramazda bore me aid’; РР} 8 tya-mary Auramazdà frübara ‘(the kingdom) which Ahuramazda conferred upon me’; DPh 9f тат Auramazdà pütuy utä-maiy ийат ‘me may Ahuramazda protect, and my royal house’. But the phrase vašnā Auramazdaha does not count in fixing the position of an enclitic: DB 1.13f vaina Auramazdàha адат-&ат х$йуабтуа Gham ‘by the favor of Ahuramazda I was king of them’; except in two partly restored passages, see under IIT. An enclitic in a dependent clause is sometimes attached to wd preceding a conjunc- tion or relative: DB 4.781 utd-tazy yàvà tauma ahatiy ‘and as long as strength shall be unto thee’; XPa 15 ша-тату tya рий akunaus ‘and what my father built’, but also XPa 19f шй tya-maiy pica kartam ‘and what was built by my father’; DNb 28f yabd-maiy tya kartam vatnühy ‘when thou shalt see what was built by me’. An attributive en- clitic genitive normally precedes the word which it modifies (cf. §309); but the meaning sometimes governs the position, as in Аа 3 apan?yüka-ma ‘my grandfather’s grandfather’, A*Sa 4 [n*yd|kama (for -am-ma, §138.1) ‘my grandfather’, both with am for -miy = -maiy (852.D. The abl. -ma is found only in hacd-ma ‘from me’, standing any- where in its clause. These formulations are vio- lated in three heavily restored passages, but the available space and the other versions favor these restorations: DSf 20 [ava исйтатату ( = -am-maty) akunaus} ‘that he made successful for me’; DSf 28 [hacd-cily ditradasa [arjanam-sary abariya) from afar its ornamentation was brought’; DNb 54f tya partalm-taty as]fiy ‘what is eommunicated to thee’ (this restoration is highly conjectural).
5100:avabasta DB 4.72, uncertain word read by KT; perhaps avatása-là, from атада with abl. -ša (8191.II; as in avadasa) + encl. apm. -tā ($188), ‘thenceforward Шеш (= the sculptures)? So Kent, JAOS 62.272-3, after Tolman’s emendation араб : là ‘thus them’, cf. НКЗ атаба Sa ‘thus stand (as І stand over the rebels)’, and Sen's avabäštā adj. apm. 'thus standing".
5101:avadà (ie. avadá) adv. ‘there, then’: LAv. атаба; from 'ava- + suffix seen in OP «dà (319.1). Usually resumptive of an immediately preceding place-phrase, which is thus made locative (so al- ways in DB except 1.85, 88; 2.24; 3.74; 4.81; 5.24, 28). See also avadasa.
5104:avadasa adv. ‘from there, from then’: avadd- + abl. -ša (5191.1; ВЫ, AiW 170, with lit.; against his view, Ву. Gr. §325), always after hacd. (1) ‘from there’: DB 1.37; 342, 80; DSf 47. (2) ‘from then’: DSe 47f.
5562:duradasa adv. ‘from afar’, with preceding hacá: dūra- + adv. -dä asin отада + abl. -ša asin avada&a (§135, 5191.1; ЈАО 54.37).  DSf 23.
```


## [2026-09-05T17:50:15.913Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON دوجین\"; grep -o \".\\{200\\}دوجین.\\{200\\}\" MON_part1.txt; echo; echo \"== MON دسیمتر/دکامتر\"; grep -o \".\\{80\\}دکامتر.\\{120\\}\" MON_part1.txt MON_part2.txt | head -3; grep -o \".\\{80\\}دسیمتر.\\{120\\}\" MON_part1.txt MON_part2.txt | head -3"
}
```


### [2026-09-05T17:50:16.026Z] TOOL RESULT

```
== MON دوجین

== MON دسیمتر/دکامتر
```


## [2026-09-05T17:50:16.953Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== NYB\"; grep -n \"dēnār\\|dyn'l\\|dah 'ten'\\|dah,\\|y'cdh\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-05T17:50:17.011Z] TOOL RESULT

```
== NYB
2095:*hu-vaxm [hww’hm] “of good swing", epithet of the varz ‘mace’ (v. vazr) carried by Keresāspa 100%. — Renders Av. (1832) hu-nwiata- "well swung’, epithet of the vazra- of Mithra (Yt. 65. 10132) and of the vazra- in general (Yt. 10%. 1372); < m + vaeg-, v.s. v. ?vextan. Reading hypothet- ical, no Paz. reading being known to me. I take it as *hu-vexm < "hu-vataman- from *véxtan < vaig- (q. v.), which has been largely confounded with !vextan < vaik-; *huvērm > hu-vaxm (or perhaps better *hu-vahm) cf s. v. mahmän. As to véxtan as a battle term cf 254. — As Bthl (Wb 1832) has given quite misleading information about the Phl. w. I put here the notice he quotes in its correct form. It is found in the Phl Xvaršēt ntyāyišn (= Yt 6) in Zand-i Khürtak Avistäk ed. by Dhabhar, p. 21 $ 15: ké yast Ohur- mazd % amarg api-š yast Mihr 4 fragoyot . . . (l. 14) api-§ yast vazr i *hu- vazm | pat kamär apar i dévan | i Mihr frägöyöt (e: *huvaxméh € ku bāstān eton dàret: mēnēyīhā be šavet, vināskārān pã- tifrās bē kunét, u menöyihä apäc 6 kantir äyet) ‘he who has worshipped Ohurmazd the Immortal... has (at the same time) worshipped Mihr (the god) of wide (l. 14) and he has wor- shipped: the mace of good swing on the skulls of the devs, owned by Mihr of wide pasturages (its being “‘of good swing" means that it constantly behaves in the following manner: spiritually it goes off and punishes the sinners, and spiritually it returns to the quiver [sheath?])? NP v. xub nihädah, Skr. v. su-niyukta (Dhalla, The Nyaishes, 1908, p. 50). l
2518:mazdčsn [Prs inscr. mzdysn], BP maz- désn [m'zdysn', m'zdsn'; commonly in the distorted graphic form given I, 134, 9 A], Prth. inser. mazdézn [mzdyzn]: Maz- dah-worshipper, adherent of the religion of Ahura Mazdah, in Av. terminology: a Mazdayasnian; in the title of the Sas.
2799:Ohurmazd [’whrmzd] 1. the name of the Supreme God, OP Ahuramazdah, passim ;
3868:uzdahikéh [^wedhykyh] exile, the state of being exiled 9!. — Abstr. of uzdehik or uzdahik, derived from uzdéh or uzdah, Av. (412) uz-dahyu- ‘a foreigner’, MPrth ‘zdyh (S); MPrs 'wzdyh, "wzdh (S) 'ex- pelled'; v. deh.
4101:Dhabhar vētvar, without etymology, in the sense of ‘contented, contentment, forbearance, patient, consoling oneself (‘consoling’ already West), resigned to the will of God’ (~ dätan ‘to console’); Hormazdyar with the same etymology as Bailey, but giving the same senses as Dhabhar (‘one who endures grief, en- during, patient, consoling, persevering’). Both lay stress on the close parallelism with a%ansand (x"arsand), of which it sometimes seems to be a mere synonym. However, the original idea underlying it must be looked for from another angle. I read it, with Dhabhar, vēt-var and derive it from OTr *vaiti-bara- ‘the willow- bringer [Av. (1314) vaéti-, NP bed, ’willow’] originally an epithet of Airyaman, the god of healing, and going back to the myth told in Vd. 22: Ahuramazdah, badly wounded and struck with 99999 maladies by Ahriman on his first on- slaught on the heavenly creation, pro- mised 1000 horses, 1000 camels, 1000 heads of cattle, 1000 sheep and “the beautiful Benediction of the Righteous" (dahma äfriti) to the god who could heal him. All declined except Airyama tišyē *Airyaman the desired(?)": he brought (barat) hair from 9 horse stallions, hair from 9 camel stallions, hair from 9 bulls, hair from 9 rams, and brought 9 willow twigs (nava vačtayo barat) and drew 9 furrows — the Phl v. adds: “and made a nirang (g. v.)”, a magic spell intended ‘to heal the wounds and stop the maladies. Apparently the willow twigs played the chief part in this nirang (of whose parti- culars we know of course nothing), thus it was quite natural to form out of it the epithet *vea$-bara- of Airyaman in his quality of the healing and relieving god. Later, Airyaman having faded away, the usage took a wider range and developed secondary nuances, but the original meaning ‘healing’ is still fairly transpar- ent in many passages, e.g. DD 36? (quoted both by Dhabhar and Hormazd-
4409:yükint [y*knt'], yakind [y’knd] the precious stone hyacinth; ~ surr 121? (read swhl, not *dyn'l!!). 1187. — Borrow- ed from Gr ddxtvdog; Arab yāgūt due to a misreading of y’knt as y kut.
```


## [2026-09-05T17:50:25.788Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nfor f in ['MON_part1.txt','MON_part2.txt','incoming/MON/MON_2vol_Adena_v1_djvu.txt','incoming/MON/MON_2vol_Adena_v2_djvu.txt']:\n    t=open(f,encoding='utf-8',errors='replace').read()\n    for w in ['دوجین','دکامتر','دسیمتر','دسی','دکا']:\n        for m in re.finditer(w,t):\n            s=max(0,m.start()-150)\n            print(f,w,'>>',t[s:m.start()+200].replace('\\n',' '))\n            break\nEOF"
}
```


### [2026-09-05T17:50:28.213Z] TOOL RESULT

```
MON_part1.txt دوجین >> ز دو جنس مختلف بوجود آمده  باشد. مولودی که پدر او سیاه و مادرش  سفید باشد با بعکس ؛ دو تبره. حرامزاده»  خشوک.   دونهی: ار (ص‌مر .) لاس آستر  شلد ۵.   دوجین: 11 (ق‌مر.) دوازده عدد از مک  شیم » ستهٌ دوارده تایی.   دوچرحه: (0-)10-272 (امر .) دستگاهی  از وسایل نقلیه که با چرخ‌های دندانه‌دار به  وسبلةٌ گردش زنجری به حرکت آید.  دوجندان: 62001-0-.010 (ق‌م
MON_part1.txt دکامتر >> اصل تار» است در مصادر مختوم به  تن و «دار» است در مصادر مختوم به  سدن,» گفتار؛ دیدار» کر دار.   ار 5 (1.) واحد مقیاس سطح, برابر با ۱۰۰  متر مربع (یکث دکامتر مربع): هکتار - صد  ۳   1 ۶ 28 [ع. ف.  رای‌هاء اند بشه‌ها.  آراسستن: 2251 (مصم.) (آراست»  اراید» خواهد اراست. بباراه اراینده؛  آراسته) زینت دادن» زیور کردن. یت  «آرا ستن» در اصل زینت دادن با افز
MON_part1.txt دسیمتر >> ختمان» خانه» گرمامه؛ ماشین آلات و  غیر ۵. دستگاه جنبش: جهاز محر که. دستگاه  رویش: جهاز نامیه. دستگاه متری: عبارت    است از ۱ سانتیمتر - ۱۰ میلیمتر» ۱ دسیمتر  - ۱۰ سانتیمتر - ۱۰۰ مپلیمتر» ۱ متر -    ۰ دسیمتر - ۱۰۰۰ میلیمتر ۱ دکامتر -  ۰ متر» ۱ هکتومتر - ۰ دکامتر - ۱۰۰  متری ۱ کیلومتر - ۱۰ هکتومتر - ۱۰۰۰  مستر . دستگاه وجود. عالم هستی » جهان  آفرینش.
MON_part1.txt دسی >>  او خویشتن را در  11 سنند. سر تراش» سلمانی» گرای؛ دلا کك»  حجام.   اییله کاری: 137-1-.2 (حامص. امر.) نوعی  کوچک و شاندن انها بر دیوار و سقف»  اشکال هندسی و گل و بته‌های مختلف ایجاد  لاه مجموع آیینه‌های کوچکی که برای  تریین به دیوار و سقف نشانده باشند.   آیینه گون: 2.0 (ص‌مر.) مانند آینه»  رحشند ه» صافی.    ۷۴ فرهنگ فارسی معین ۱    تب    «» و را را 
MON_part1.txt دکا >> ردن  آب با آب‌باش و مانند آن» آبباری کردن.  آب دادن به زهر: آلودن شمشیر و خنجر و  جز آن به زهر تاالتیان نپزيرد. آب دادن  چشم: جاری شدن آب مخصوص از  دیدکان به علت کسالت با سماری. آب دادن  فلز: طللی کر دن آن به فلز گرانبهاتر؛ آب زر  پا سیم دادن. آب دادن کارد و شمشیر و مانند  آن: عملی که شمشیر سازان و کار گران کنند  برای سخت کردن آهن و آن فرو بردن فلز
MON_part2.txt دکامتر >> مکنة مختلف متغیر    بیش از این بوده است. د    انفته ال ادن ۲۱۳۳۴ کر فرع تاه    ون دزی مهن ۰ عشیر و عشبر  ۰ گز است. ج طیق قانون مصوب  ۴ ه.ش یک قفیز یک دکامتر مر  ضح- مع‌هذا هنوز در تقاط مختلف برای  اندازه‌های مختلف استعمال می‌شود: در  حوالی یزد معادل ۱۰۰۰ متر مربع حساب  می‌کنند. در جوشقان معادل ۰ متر مربع  فقط و مترادف است با یک کبله. در گیلان  معاد
MON_part2.txt دسیمتر >> دل بال. لکنت زبان. واحدی است معادل  ربع چارکك. چهار گره یک چارک و چهار  چارکك یک ذرع و هر گره دو بهر است.  صح. طبق قانون مسصوب ۴ ۰ ه.ش  بکك گره - یکك دسیمتر. گُره دریایی: و احد  سرعت و عبارت است از یک میل دریایی  در ساعت. (قالی) واحدی است در قالی‌بافی  و آن جزئی است از «رکت»؛ تقریا معادل ۷  یه میا ۳ ۲ این کله گند. : 0  لی رابگر تعین می‌کند. در هر ک
MON_part2.txt دسی >> تاهتر از حروف  است و معمولا آن را در فواصل بین کلمات  کل   اصله : ۱۱+ [ع. ف. -  فاصله‌سنجنده | (ص‌فا. ا.) (عک.) هرگاه به  وسله لوله‌ای که در داخل آن عدسی  ایژکتیفی نصب شده. شیتی را نگاه کنید:  انتدا موقعی که فاصله عدسی تا چشم میزان  نیست» اظر شیّ را مضاعف می‌بیند. حال  اگر لولةٌ دید از دو قسمت تشکیل شده باشد  که در نتیحه ببجاندن یکی در داخل دایکر: 
MON_part2.txt دکا >>  (عم.) با وجود استفاده باز مدعی  است.   غر تشن: (- فلتیشن - قلتشن ]  (ص.) (عم.) زورگو؛ مستبد به رأی: غرتشن  آقا.   غر تی: [- قرتی] (ص.) (عم.) جلف و  بدکار.   غسرچ‌غرج: ۲06( (اصست.) آواز  ساییدن دندان بهم با فشار.   غرچک: ۱:0۳5- غرچه| (ص.) نادان»  ابله» احمق.   غرچه: (۱::۳)6۵- غرچک - غراچه|  (ص.) نامرد» بی‌حمیت. دیوث. ابله» نادان.  ناتوان در مردی. ز
incoming/MON/MON_2vol_Adena_v1_djvu.txt دوجین >> ز دو جنس مختلف بوجود آمده  باشد. مولودی که پدر او سیاه و مادرش  سفید باشد با بعکس ؛ دو تبره. حرامزاده»  خشوک.   دونهی: ار (ص‌مر .) لاس آستر  شلد ۵.   دوجین: 11 (ق‌مر.) دوازده عدد از مک  شیم » ستهٌ دوارده تایی.   دوچرحه: (0-)10-272 (امر .) دستگاهی  از وسایل نقلیه که با چرخ‌های دندانه‌دار به  وسبلةٌ گردش زنجری به حرکت آید.  دوجندان: 62001-0-.010 (ق‌م
incoming/MON/MON_2vol_Adena_v1_djvu.txt دکامتر >> اصل تار» است در مصادر مختوم به  تن و «دار» است در مصادر مختوم به  سدن,» گفتار؛ دیدار» کر دار.   ار 5 (1.) واحد مقیاس سطح, برابر با ۱۰۰  متر مربع (یکث دکامتر مربع): هکتار - صد  ۳   1 ۶ 28 [ع. ف.  رای‌هاء اند بشه‌ها.  آراسستن: 2251 (مصم.) (آراست»  اراید» خواهد اراست. بباراه اراینده؛  آراسته) زینت دادن» زیور کردن. یت  «آرا ستن» در اصل زینت دادن با افز
incoming/MON/MON_2vol_Adena_v1_djvu.txt دسیمتر >> ختمان» خانه» گرمامه؛ ماشین آلات و  غیر ۵. دستگاه جنبش: جهاز محر که. دستگاه  رویش: جهاز نامیه. دستگاه متری: عبارت    است از ۱ سانتیمتر - ۱۰ میلیمتر» ۱ دسیمتر  - ۱۰ سانتیمتر - ۱۰۰ مپلیمتر» ۱ متر -    ۰ دسیمتر - ۱۰۰۰ میلیمتر ۱ دکامتر -  ۰ متر» ۱ هکتومتر - ۰ دکامتر - ۱۰۰  متری ۱ کیلومتر - ۱۰ هکتومتر - ۱۰۰۰  مستر . دستگاه وجود. عالم هستی » جهان  آفرینش.
incoming/MON/MON_2vol_Adena_v1_djvu.txt دسی >>  او خویشتن را در  11 سنند. سر تراش» سلمانی» گرای؛ دلا کك»  حجام.   اییله کاری: 137-1-.2 (حامص. امر.) نوعی  کوچک و شاندن انها بر دیوار و سقف»  اشکال هندسی و گل و بته‌های مختلف ایجاد  لاه مجموع آیینه‌های کوچکی که برای  تریین به دیوار و سقف نشانده باشند.   آیینه گون: 2.0 (ص‌مر.) مانند آینه»  رحشند ه» صافی.    ۷۴ فرهنگ فارسی معین ۱    تب    «» و را را 
incoming/MON/MON_2vol_Adena_v1_djvu.txt دکا >> ردن  آب با آب‌باش و مانند آن» آبباری کردن.  آب دادن به زهر: آلودن شمشیر و خنجر و  جز آن به زهر تاالتیان نپزيرد. آب دادن  چشم: جاری شدن آب مخصوص از  دیدکان به علت کسالت با سماری. آب دادن  فلز: طللی کر دن آن به فلز گرانبهاتر؛ آب زر  پا سیم دادن. آب دادن کارد و شمشیر و مانند  آن: عملی که شمشیر سازان و کار گران کنند  برای سخت کردن آهن و آن فرو بردن فلز
incoming/MON/MON_2vol_Adena_v2_djvu.txt دکامتر >> مکنة مختلف متغیر    بیش از این بوده است. د    انفته ال ادن ۲۱۳۳۴ کر فرع تاه    ون دزی مهن ۰ عشیر و عشبر  ۰ گز است. ج طیق قانون مصوب  ۴ ه.ش یک قفیز یک دکامتر مر  ضح- مع‌هذا هنوز در تقاط مختلف برای  اندازه‌های مختلف استعمال می‌شود: در  حوالی یزد معادل ۱۰۰۰ متر مربع حساب  می‌کنند. در جوشقان معادل ۰ متر مربع  فقط و مترادف است با یک کبله. در گیلان  معاد
incoming/MON/MON_2vol_Adena_v2_djvu.txt دسیمتر >> دل بال. لکنت زبان. واحدی است معادل  ربع چارکك. چهار گره یک چارک و چهار  چارکك یک ذرع و هر گره دو بهر است.  صح. طبق قانون مسصوب ۴ ۰ ه.ش  بکك گره - یکك دسیمتر. گُره دریایی: و احد  سرعت و عبارت است از یک میل دریایی  در ساعت. (قالی) واحدی است در قالی‌بافی  و آن جزئی است از «رکت»؛ تقریا معادل ۷  یه میا ۳ ۲ این کله گند. : 0  لی رابگر تعین می‌کند. در هر ک
incoming/MON/MON_2vol_Adena_v2_djvu.txt دسی >> تاهتر از حروف  است و معمولا آن را در فواصل بین کلمات  کل   اصله : ۱۱+ [ع. ف. -  فاصله‌سنجنده | (ص‌فا. ا.) (عک.) هرگاه به  وسله لوله‌ای که در داخل آن عدسی  ایژکتیفی نصب شده. شیتی را نگاه کنید:  انتدا موقعی که فاصله عدسی تا چشم میزان  نیست» اظر شیّ را مضاعف می‌بیند. حال  اگر لولةٌ دید از دو قسمت تشکیل شده باشد  که در نتیحه ببجاندن یکی در داخل دایکر: 
incoming/MON/MON_2vol_Adena_v2_djvu.txt دکا >>  (عم.) با وجود استفاده باز مدعی  است.   غر تشن: (- فلتیشن - قلتشن ]  (ص.) (عم.) زورگو؛ مستبد به رأی: غرتشن  آقا.   غر تی: [- قرتی] (ص.) (عم.) جلف و  بدکار.   غسرچ‌غرج: ۲06( (اصست.) آواز  ساییدن دندان بهم با فشار.   غرچک: ۱:0۳5- غرچه| (ص.) نادان»  ابله» احمق.   غرچه: (۱::۳)6۵- غرچک - غراچه|  (ص.) نامرد» بی‌حمیت. دیوث. ابله» نادان.  ناتوان در مردی. ز
```


## [2026-09-05T17:50:39.495Z] TOOL CALL #56: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-05T17:50:39.504Z] TOOL RESULT

```


```


## [2026-09-05T17:50:43.556Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/d%C3%A9%E1%B8%B1m%CC%A5",
 "prompt": "Give the reconstruction, meaning, and the full descendant list (Proto-Indo-Iranian, Proto-Iranian, Avestan, Old Persian, Latin, Greek, Proto-Germanic) for the PIE numeral 'ten'. Quote the exact forms."
}
```


## [2026-09-05T17:50:44.641Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dinar",
 "prompt": "Quote the full etymology entry for 'dinar', and also anything on the page about denarius."
}
```


### [2026-09-05T17:50:49.177Z] TOOL RESULT

```
# PIE Numeral "Ten"

**Reconstruction:** "*déḱm̥" (described as "uninflected, probably")

**Meaning:** "ten"

**Selected Descendants from the page:**

The document provides these exact proto-language forms:
- Proto-Indo-Iranian: "*dáća"
- Proto-Italic: "*dekem"
- Proto-Hellenic: "*dékə"
- Proto-Germanic: "*tehun"

**Note on completeness:** The page does not list separate Proto-Iranian or Avestan descendants. It references Proto-Indo-Iranian descendants, which would eventually develop into Iranian languages including Avestan, but specific descendant forms for those individual languages are not provided in this Wiktionary entry. The document directs readers to "see there for further descendants" at each proto-language link rather than exhaustively listing all modern language reflexes.
```


### [2026-09-05T17:50:51.513Z] TOOL RESULT

```
# Dinar Etymology

**Full Dinar Entry:**
"Middle Eastern unit of currency; generic name of Arab gold coins, 1630s, from Arabic dinar, originally the name of a gold coin issued by the caliphs of Damascus, from late Greek denarion, from Latin denarius."

**Denarius Information:**
The page explains that denarius derives from Latin meaning "containing ten," specifically short for "denarius nummus" (the coin containing ten aces). It originated from "deni-" meaning "by tens," connected to "decem" meaning "ten." In English accounting, this term referred to a penny, as the Roman denarius was the largest silver coin—hence the abbreviation "d" for pence in the old "l.s.d." monetary system.

Both terms trace their etymological roots back through Greek and Latin to the Proto-Indo-European root *dekm-, meaning "ten."
```


## [2026-09-05T17:50:56.907Z] TOOL CALL #59: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DB%8C%D8%A7%D8%B2%D8%AF%D9%87",
 "prompt": "Give the Persian etymology of یازده (yāzdah) 'eleven' — the Middle Persian form, Old Iranian/Avestan antecedent, and any cited sources."
}
```


## [2026-09-05T17:50:58.677Z] TOOL CALL #60: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AF%DB%8C%D9%86%D8%A7%D8%B1",
 "prompt": "Give the etymology sections for Arabic دينار and Persian دینار: what language it is borrowed from and via what route (Middle Persian? Greek? Latin denarius?). Quote the etymology text."
}
```


### [2026-09-05T17:51:02.418Z] TOOL RESULT

```
# Etymology of یازده (yāzdah) 'eleven'

**Middle Persian form:**
"𐫏𐫀𐫉𐫅𐫍 (yʾzdh)" and the Book Pahlavi variant, representing /yāzdah/.

**Old Iranian antecedent:**
The word derives from Old Persian "*aivacadaθa," representing the ancient Iranian root for this numeral.

**Etymological chain:**
The progression moves from the Old Persian form through Middle Persian *yvāzdah, ultimately yielding the modern Persian یازده.

**Cited sources:**
The Wiktionary entry references three major Persian dictionaries: Hayyim's New Persian–English dictionary (1934), the Dehkhoda Dictionary (University of Tehran Press), and Steingass's Comprehensive Persian–English dictionary (1892, Routledge & K. Paul).
```


### [2026-09-05T17:51:04.752Z] TOOL RESULT

```
# Etymology of دینار (Dinar)

Based on the provided content, I can only provide information for **Persian دینار**:

## Persian دینار

**Source language path:** Latin → Ancient Greek → Middle Persian → Persian

**Etymology quote:** "From Middle Persian _dynʾl'_ /⁠dēnār⁠/, "(gold) dinar", from Ancient Greek _δηνάριον_ (dēnárion), from Latin _dēnārius_, perhaps through Aramaic _דֵּינָרָא_ / _ܕܝܢܪܐ_ (dēnārā)."

The word ultimately derives from Latin *denarius*, transmitted through Greek and Middle Persian, with possible Aramaic influence.

---

**Note:** The provided webpage content does not include an entry for Arabic دينار, so I cannot provide its etymology. The page only covers the Persian form.
```


## [2026-09-05T17:51:17.756Z] TOOL CALL #61: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/déḱm̥' --note 'page 114, root Dekm: PIE *deḱm̥ \"ten\", descendants PII *dáća, Italic *dekem, Hellenic *dékə, Germanic *tehun' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/dinar' --note 'page 114, nodes 14-19: dinar < Arabic dīnār < late Greek denarion < Latin denarius' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/یازده' --note 'page 114 node 3: Persian یازده < MP yāzdah < OIr *aiva-ca-dasa' ; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/دینار' --note 'page 114 nodes 15-16: Persian دینار < MP dēnār < Gk dēnárion < Lat dēnārius, perhaps via Aramaic dēnārā' 2>&1 | tail -30"
}
```


### [2026-09-05T17:51:20.685Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e5a97269f3eb4af5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35ec964396753301.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1eba3e32d548acd4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/019b1cbc0e367ffc.txt
```


## [2026-09-05T17:51:24.815Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AF%D9%88%D8%AC%DB%8C%D9%86/",
 "prompt": "What does فرهنگ معین (Mo'in) and دهخدا say about دوجین — its meaning and its origin tag (e.g. [فر.] French douzaine)? Quote the entry text."
}
```


## [2026-09-05T17:51:25.687Z] TOOL CALL #63: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/dozen",
 "prompt": "Quote the etymology of 'dozen' (Old French dozaine/douzaine, Latin duodecim)."
}
```


### [2026-09-05T17:51:31.033Z] TOOL RESULT

```
# دوجین: فرهنگ معین and دهخدا

**فرهنگ معین:**
Origin tag: [فا - فر.] (Persian-French)
Meaning: "(دُ) دوازده عدد از یک شی ء، بستة دوازده تایی"
Translation: twelve units of something; a bundle of twelve items.

**دهخدا:**
Origin tag: (از فرانسوی، اِ) — from French
Meaning: "دوازده تا از چیزی: یک دوجین کبریت. یک دوجین دستمال"
Translation: twelve of something; for example, a dozen matches or a dozen handkerchiefs.

Both sources identify the word as a French loanword (from French *douzaine*) meaning twelve units of any item.
```


### [2026-09-05T17:51:31.678Z] TOOL RESULT

```
# Etymology of "Dozen"

According to the Online Etymology Dictionary, the word "dozen" traces back through multiple linguistic layers:

**Old French origin:** "from Old French _dozaine_ 'a dozen, a number of twelve' in various usages, from _doze_ (12c.) 'twelve'"

**Latin roots:** The Old French term derives from Latin _duodecim_ meaning "twelve," which breaks down as "_duo_ 'two'...+ _decem_ 'ten'"

The entry notes that "The Old French fem. suffix _-aine_ is characteristically added to cardinals to form collectives in a precise sense ('exactly 12,' not 'about 12')."

The resource also documents how this Latin-derived term spread across European languages, including Spanish _docena_, Dutch _dozijn_, German _dutzend_, and Russian _duizhina_.
```


## [2026-09-05T17:51:38.134Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== ARY latin index DEKM\"; grep -n -i \"DEKM\\|DEK'M\\|DEKM̥\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"== ARY persian ده\"; python3 - <<'EOF'\nimport re\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if re.search(r'\\bده\\b',p) and ('dekm' in p.lower() or 'decem' in p.lower() or 'deka' in p.lower()):\n        print('pdfpage',i)\n        print(p[:1500])\n        break\nEOF"
}
```


### [2026-09-05T17:51:40.146Z] TOOL RESULT

```
== ARY latin index DEKM
== ARY persian ده
```


## [2026-09-05T17:51:43.292Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"decem\\|dekm\\|deka\" incoming/ARY/ARY_latin_index_pages.txt | head -10; echo \"=== pers\"; grep -n \"دینار\" incoming/ARY/ARY_pages.txt | head -5; echo \"=== SYN 13.31\"; sed -n '23833,23860p' SYN.txt"
}
```


### [2026-09-05T17:51:43.378Z] TOOL RESULT

```
464:\+ Deich | deg deka decem +] leet
8138:deka ty UY
8422:DESIAT, DESIATE —_ (RUSSIAN) 53, DEKA GREEK) sli
8423:DESET CZECH) Sey DECEM LATIN) 553
14731:HOLD HIGH GERMAN) (4S lt DEKAENNIA AGREEK) gli
=== pers
=== SYN 13.31
13.31. NOTE ON THE NUMERALS
No class of words, not even those de- noting family relationship, has been so persistent as the numerals in retaining the inherited words.
Except for some suffix-variation and actual substitution in the case of ‘one’ (13.32), the IE words for ‘one’ to ‘ten’ have persisted everywhere with only slight changes other than phonetic; like- wise the IE word for ‘hundred’, while for ‘thousand’ there are several different groups.
The ‘teens’ are expressed by cop. epds. of the digits with ‘ten’, with the ex- ception of the Gme. words for ‘eleven’ and ‘twelve’ (Goth. ain-lif, twa-lif) and the whole Lith. series (viento-lika, dvy- lika, try-lika, keturio-lika, etc. for 11-19), which are cpds. with a form of IB *leikv- ‘leave, remain’ (Grk. del, etc., Walde- P. 2.396 f.), hence orig. ‘one over’ (the ten), etc.
For 20-90 certain IE epds., the sec- ond part of which seems to be obscurely related to the numeral for ‘ten’, have been partly retained (for 20 Grk. etkoot, Dor. fikart, Lat. viginit, Skt. viricati-, etc.; for the others Grk. -xovra, Lat,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
— ee
-ginia, Skt. -gat-, etc.), and partly re- placed by more transparent phrases or epds. (as for 20 Goth. twaz tigjus, OB twen-tig, Lith. dvi-deSimt, Rum. doud- zect),
The decimal system, based on count- ing the fingers, prevails. But the in- fluence of a duodecimal or Sexagesimal system is indicated by certain breaks in the type of formation as that between 12 and 13 in Gmc., between 60 and 70 in Grk., Goth., ete.
The ordinals are formed from the cardinals, mostly with a -to- or -mo- suffix. Exceptions are those for ‘first’ (13.33), and many of those for ‘second’, which are literally ‘the other’ (Goth. anpar, OE oper, ChSl. witori, etc.) or ‘the following’ (Lat. secundus : sequi ‘follow’; similarly Grk. debrepos prob. orig. ‘the one after’, cf. Hom. debraros ‘last’).
For detailed discussion of the IE nu- merals, cf. Brugmann, Grd. 2.2.1 ff.
In the following we list and discuss only those for ‘one’ and ‘first’, and for ‘three’ with derivs., choosing these last as con- venient illustrations of the various types.
er ey ge eS tee ae ae ae
igitized by Arya Samaj Foundation Chennai and eGangotri
QUANTITY AND NUMBER 937 13.832 ONE Goth. ains Lith. vienas ds ON einn Lett. viens tyas Dan. en ChSl. jedint anus Sw. en SCr. jedan uno OE an Boh. jeden un ME oon Pol. jeden uno NE one Russ. odin oun Du. een Skt.  eka- gen OHG ein Av. aéva-, OPers. aiva aon MHG ein oun H i f a NHG em . ; 1B *oi-no-, ete-, derivs. of a pro- *oi-wo-. Av. aéva-, OPers. aiva-; cf. Al gi- beside 7- in Lat. zs, etc. | Grk. ofos, Cypr. offos ‘alone’, and Skt. Mt 1101, Ernout-M. 1127 f. eva ‘thus’,
ide-P. : Doe. Gri. olvés, olvy ‘one on the
dice, ace’, but as numeral replaced by ds; OLat. oinos, oenus, Lat. unus (> It., Sp. uno, Fr., Rum. wn); Ir. din, oen, Nir. aon, W. un, Br. unan, eun; Goth. ains, OB Gn, etc., general Gmce.; OPruss. ains, Lith. vienas, Lett. viens (init. v ob- gure); ChSl. ino- in epds., otherwise jdinit (jed-, ed- prefixed pronominal ele- ment), SCr. jedan, Boh., Pol. jeden, Russ. odin; cf. Skt. pron. ena-.
*oi-ko-. Skt. eka-, cf. aika- in Indic text in Hittite records.
2. Grk. els, gen. évés, fr. és (Cret.), *éus, fem. pla fr. *oula; Toch. A sas masc., sim fem., B se : Grk. duds, Skt. sama-, Goth. sama ‘same’, Grk. aya ‘to- gether’, Lat. semel, Skt. sa-krt ‘once’, etc. Walde-P. 2.488 ff. NG pop. #as with new nom. to acc. é&a.
13.33 ALONE, ONLY (adj.; adv.)
Whe , ‘only? i: oa adjectives ‘alone’ and Feed as in NE alone etentiat allein Vs. einzig, ete., the We of ben 18 idiomatic and mainly '0n, predicative vs. attribu-
VS. 0;
bloss
Hoyos; ubvov Goth. ains, ainaha; fatat- Lith. vienas (sau), viena- horaxés, wbvos; évoy nei tinis; tik(tai) solus, tinus, tnicus; ON einn, einga- Lett. viens pats, vienigs; sdlum, tantum, mo- Dan. lene, eneste; alene, vien, tik(at) do kun, blot ChSl. jedinti; jedino solo, unico; solo, sola~ Sw. allena, ende; allenast, SCr. sam, jedini; samo mente, soltanto blott Boh.  sdm, jediny; jen, seul, unique; seule- OE Gna, anga, anlic; an toliko ; ale i ME alone, onely; onely, Pol. sam, jedyny; jeno, Slo, tinico; solo, sola- but tytko Rum, ih sib , ; NE alone, only; only, but Russ. odin, jedinstvennyj; ‘ Gee unie; numat Du. alleen, eenig; alleen, tol’ko ! ne slechts Skt.  eka-, ekaka- ¥ Re aon; amhain OHG  eino, einac; ekkorodo Avy. aéva- ee Bog MHG aleine, einec; m nemel eee; were, niwer » Mep-ken NHG allein, einzig; nur,
tive. In many languages the same word is used in both ways, e.g. Grk. pévos, Lat. solus, Fr. seul, Goth. ains, ete. The underlying notion is an emphatic ‘one’, and it is most commonly expressed by
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
| | | :
Digitized by Arya Samaj Foundation Chennai and eGangotri
```


## [2026-09-05T17:51:51.976Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8415,8430p' incoming/ARY/ARY_latin_index_pages.txt; echo \"=== page tag\"; awk 'NR<=8430 && /\\[pdf page/' incoming/ARY/ARY_latin_index_pages.txt | tail -2"
}
```


## [2026-09-05T17:51:53.453Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"dek̂m\\|dekm\\|de$m\\|dek'm\" incoming/WLD/WLD_Bd1_pages.txt | head -10; echo \"=== WLD band3 index\"; grep -n \"dek̂m\\|dekm\" WLD_band3.txt | head"
}
```


### [2026-09-05T17:51:53.927Z] TOOL RESULT

```
[pdf page 292]
avd pts
TIo (NORWEGIAN) 6353 sAK s(TOKHARIAN A) A 5 oa
TIEN (DUTCH) «gala Sak (TOKHARIAN B)B «5x3
OLD CHURCH SLAVIC) 455 95el (SANSKRIT) oy Sila
DESETI DASA, DACHA, DACA
DZIESIEC HPOLISH) gling) TASN ARMENIAN) «531
DESIAT, DESIATE —_ (RUSSIAN) 53, DEKA GREEK) sli
DESET CZECH) Sey DECEM LATIN) 553
DESAT SLOVAK) 5 al DIX A(FRENCH) suit,
DESHIMT LITHUANIAN) gly DIEZ SPANISH) glilyal
DEICH OLD IRISH) oS sd gh DIECI HUTALIAN) gldts!
DEICH GAULISH) JSF zece (RUMANIAN) gly,
DEG WELSH) 53) DEZ (PORTUGUESE) Jas x
TAIHUN GOTHIC) S38
REFERENCES beth HOLD SCANDINAVIAN) 5.5)
=== page tag
[pdf page 291]
[pdf page 292]
```


### [2026-09-05T17:51:55.694Z] TOOL RESULT

```
53:                                       Vorrede.
54:  Das   vorliegende       Werk laSt        uns erst so reckt empfinden, welch uner-
55:setzlichen Yerlust die Wissenschaft mit              dem Tode Alois Waldes                 (3.   Ok-
56:tober 1924) erlitten hat.       Die letzten zehn Jahre seines Lebens waren der
57:Abfassung dieses    etymologischen Worterbuehes gewidmet, dessen Yoll-
58:endung ihm leider nicht vergonnt war. Zwar lagen die Buchstaben P, Ph,
60:tur versehen vor, aber bei den anderen Buchstaben gab es noch sehr
61:viele Liicken auszufiillen, namentlich bei den Vokalen, T, D, Dh und den
62:G-Lauten. Hier bestanden die Zettel zu etwa einem Dritteil teils nur aus
63:den bloBen Stichworten, ohne jedes Wortmaterial,                       teils   nur aus ungeord-
=== WLD band3 index
```


## [2026-09-05T17:52:03.521Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/ARY/ARY_pages.txt',encoding='utf-8',errors='replace').read()\nimport re\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nfor pg in (291,292,293):\n    print('=== pdf page',pg)\n    print(d.get(pg,'')[:900])\nEOF"
}
```


### [2026-09-05T17:52:05.358Z] TOOL RESULT

```
=== pdf page 291

۸11۸ ,نت0۸ انگلیسی (تکلاه/۵: 10۷۳ ,00۷۲۷
پهلری (1/لالمه): 0 هلندی (070ان 71
کردی (4ل03). 0۸ اسلاوی کهن (ع4ذل5 نان صامم:
بلرچی (ات‌ناستمه: 5 ,ت05 متططاضی
افغانی (پشتو) (۸۳0[7۸21). 13 روسی (/42ا5کتا): 03
تخاری ۸ (۸ ۸(۷ل70727۸7). اد رنه با لیتوانی (۸2(هناب 7 رم).
تخاری 8(8 #۸ 7027۸). اد ادن ره با 56 ما0
سغدی ((56007014): روهار ایرلندی کهن (للكل#ا ضان):
سانسکریت ‎ :)64۸/587/7(‏ 0۸ ,اق0 7 010۸1۸ ,0
برنانی (08881): ۰ 2018108 ,0051۵09 سلتی (کلتی) (ع2/71): 00
لاتین (/712ا): زان ولزی (۴8ل): ,010۸8
ایسلندی‌کهن (010/۸۸7بی5 صاه): آلبانی (1۸2/مقلم: رز
700
تررس کهن (۸0۳8۴ طران): 21۸ پسگشت‌ها ‏ " مد دی
فریزی کهن (00فا5لغ۶ صام): لا 8 و
آلمانی کهن ((0874۸ 04 1لز صا0): 8 (008) امین
۱ لرزد 9 (65شتت» اما
آلمانی (2فههع02). #انآهة 05۰ نم 2 مهد
انگلیسی کهن (ل//8/05 صام): 708 ,لاتآن برهان قاطع : ۹.۰
باهدداشت.
چم‌های برخی از واژه‌های این فهرست: دژ) تهه‌ی شنی» تهه؛ وزیدن» شهر؛ ناحید
جٌم واژه‌ی انگلیسی 1301۷81 ته
=== pdf page 292

م۲۹۳۱
تخاری 4 (۸ [(7072۸7): 8 نروژی (/0/07۷801+ 710
تخاری 8(8 ((ین707): 5۸ هلندی (0ع007): 71
سانسکریت (54(57/7): اسلاوی گهن (ع7/بما5 6۶718614 صا0):
۸۸ 3۸03۸ ,08۸ ندرا
ارمنی (4/(/2//1490): نج لهستانی (۳0(./88): دادما
یونانی (0785): 0۸ روسی ((594): ۰ 0851۸78 ,80581۸7
لاتین (710)ما): ان هن 1۱۱ چکه ((250)): 037
فرانسه (۳5۸70[7): 213 اسلواکی (51.0140): 2۸7
اسپانپایی ([52۸(۷18): 2۳2 لیتوانی (۸0/40ل 731 ): 07
ایتالیایی ((4ال17): 2010 ایرندی کهن (5ل#! (ا0): 2
رومانی ((۵ا(۸/(نا): 2 گالي (37/انا۸ه): ی زر
پرتغائی (ظ۳07001028) 22 ولزی (5(7ا8/(): 26
گرنیکد (0071710): 717
ابسلند یکهن (0101۸۷۸۸/(مع5 صا۵): پسگشت‌ها رد اه ادن ادن ات
7 ۶۵0۷0
ساکسونی کهن (24200/۷ ۰:0۵ #ف۸ا781 4 (08۳ 8/7
فریزی کهن (لفا5ل۲7 ل0): 712 4 (010) :5 مل۸5
آلمانی کهن (07ف652(1 ۱/0۲ ص0): 6 (78) اس
دا 9 ((18) :005
آلمانی ([05701۸): لا ۵ 4 (78) +7 ۰
انگلیسی کهن (8۸۷0/757 010): 7 ل 727
انگلیسی (/52/01/5): 7 7 ((758) ۸407
دانمارکی (0۸۷1
=== pdf page 293

ارستی (08882712): 01 آلمانی (4ف05794): انا نما
افغانی (پشتو) (۸۳0/7۸۸۷1): ۱3 انگلیسی کهن (4ل5ل870 صا0):
تخاری ۸ (۸ 7007۸7۸): 3 ,0007 ,71807۸
هن ۹
تخاری 8(8 [۸ل707۸7): انگلیسی (87/ا8(/0): 1 ۳ :
,86۸0175 هلندی (ع007+ ان زان انا وا
سانسکریت (5۸(/8277): اسلاوی کهن (ع7آشا؟ نات انم
0۸۸1 بکلاه0۸ ۰ : 0
ارمنی (48۸/2/1۸/۷): ۰ 53080-/1۸8 لهستانی (377/ا۳0): وا ند را
پونانی 008610): نا ۱۱۷ لیترانی (1۸0ه۸لا 27 7/):
لاتین (712ها): رد۱۱۱ 48 ,05۳731۸
فرانسه (2ع/۳8۸): اند ۱ ۱۱۱۱ لترنی (لتی) (/لفا7م): 0587117۸75
آسپانیایی (82۸(18): 00 پروسی کهن (۷ل۲8534 2ا0): 0888713175
ایتالپایی (/فانقه7): 00 گالی (#لقلانام0): نردان 1۱ هد
رومانی (#۸۸(/۵۷): ولزی (7] کل 7): این رده ان ۱۱۱
۸ ب۸ بف8ن78۳53 بل۸ گالیک (0/لظ0۸): 1۳0
پر تغالی (۳071017885): 0
گوتیک (0071712): انران‌را ۷۷۹۱ پسگشت‌ها ددرت
ایسلندی‌کهن (/010/۸1۸ یمه صان). 2213 آ 0رق 200
ه0 7 4 (18) :اتمه
آلمانی کهن ((6588/۸ 07اب صا0): 6 ( 057 ات رد هام
: 0 ,7233۸170 9
```


## [2026-09-05T17:52:15.488Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\n# find page containing 'taihun' and 'decem'\nfor pg,txt in d.items():\n    if 'taihun' in txt and 'decem' in txt:\n        print('pdf page',pg)\n        print(txt[:1200])\n        print('---')\nEOF"
}
```


### [2026-09-05T17:52:17.565Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T17:52:22.106Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nparts=re.split(r'\\[pdf page (\\d+)\\]',t)\nd={}\nfor i in range(1,len(parts),2):\n    d[int(parts[i])]=parts[i+1]\nprint('pages',len(d), min(d), max(d))\nhits=[pg for pg,txt in d.items() if re.search(r'ta[iíj]hun',txt,re.I)]\nprint('taihun pages',hits[:20])\nhits2=[pg for pg,txt in d.items() if 'dekm' in txt.lower() or 'de$m' in txt.lower()]\nprint(hits2[:20])\nEOF"
}
```


### [2026-09-05T17:52:23.883Z] TOOL RESULT

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 7, in <module>
ValueError: min() iterable argument is empty
```


## [2026-09-05T17:52:28.209Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -3 incoming/WLD/WLD_Bd1_pages.txt; grep -c \"\" incoming/WLD/WLD_Bd1_pages.txt; grep -o \"\\[pdf page [0-9]*\\]\" incoming/WLD/WLD_Bd1_pages.txt | head -3; echo \"== formfeeds\"; python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\nprint('ff',t.count(chr(12)))\nimport re\npgs=t.split(chr(12))\nfor i,p in enumerate(pgs):\n    if 'taihun' in p and 'decem' in p: print(i, p[:600])\n\""
}
```


### [2026-09-05T17:52:30.012Z] TOOL RESULT

```
            GOVERNMENT OF INDIA
 ARCHEOLOGICAL SURVEY OF INDIA

81975
== formfeeds
ff 894
```


## [2026-09-05T17:52:33.327Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npgs=t.split(chr(12))\nimport re\nfor i,p in enumerate(pgs):\n    if re.search(r'ta[ií]hun',p) and 'zehn' in p:\n        print('leaf',i)\n        print(p[:900]); print('===')\n\" | head -60"
}
```


### [2026-09-05T17:52:35.013Z] TOOL RESULT

```
leaf 793
                                                     ,




                                         dek-, dak-,’ dek
                                              7
                                                                 dekm
                                                                    o                                   785

von *dek- mit *deilc- „zeigen“ (ebenfalls mit ausgestreckter Hand) macht
dieselben Yoraussetznngen.


dek-, dek- oder (wegen des Aind.) dek-                          (:   dole-,        dek-) „reiBen, zerreiBen,
        zerfasern".
  Ai. daga „die am Ende eines Gewebes hervorragenden Zettelfaden,
Fransen"; got. tagl n. „einzelnes Haar“, anord. tagl n. „die Haare im
Pferdeschwanz" ags. tcegl (engl. tail ) „Schwanz“, ahd. sagal „Schwanz,
Stachel, mannliches Glied, Rute“; got. tahjan „reiBen, zerren", distahjan
„zerstreuen“, isl. tceja, tabi „karden“, no
===
```


## [2026-09-05T17:52:38.948Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read()\npgs=t.split(chr(12))\nprint(pgs[793][900:3000])\nprint('%%%%%% NEXT')\nprint(pgs[794][:1500])\n\""
}
```


### [2026-09-05T17:52:40.803Z] TOOL RESULT

```
rw. mdartl. tceja ( *tahjan ) und taa

(*tahdn) „fasem, zerreiBen"; anord. tag , PI. tceger und tagar f. „Faser“,
mhd. zdeh, zahe f. „Docht, Lunte"; in anderer Bed. („zerrend             ziehend,               —
binausziehend") norw. mdartl. taag „langsam und andauernd", mnd. tege,
ostfries. tage         „zahe“       (iiber   ahd. zahi   s.   aber unter *denk- „beiBen“), und
ahd. zag „zogernd, unentsehlossen, zaghaft“,                     wozu zagen „verzagt und un-
entschlossen sein“;
                          „woran man sieh reiBt“ oder „abgerissenes, rissiges
      vielleicbt hierher als
Stiiek“, mhd. zacke m. f., nhd. Zacke mengl. takke „fibula ‘, engl. tack „Stift,
kleiner Nagel", norw. mdartl. tagg, tagge m. „hervorragende Spitze, Zacke"
(von Lewy PBrB. 32, 148 Anm. 4, KZ. 40, 563 Anm. 1 wird Zacke mit lit.
dagys „Distel“ und got. tekan „nehmen“ verbunden; nicht besser; vgl.
Muhlenbach-Endzelin I 429 u. dadzis, wo Lit.).
   S. Zupitza Gntt. 192 m. Lit. (unter anderer Abgrenzung gegenuber *denk-
„bei8en“), Fick II 4 152.
  Ir. dual „Locke“ aua *doklo- ebenfalls hierher (trotz Zupitza aaO).                                    —
S. noch *denk - „boiBen“.


dekm „zehn“.
      Ai. daga, av. dasa, gr. dexa, lat. decern, umbr. desen-{duf)
                                                                 „(duo-)decim",
air.    deich     cymr. deg, corn. bret. dek, got. taihun (entweder fur *taihu
                 n.,

mit nach dem Ordinale aufgefrischtem -w, oder aus idg. *dekm-t), anord.
                                                                             2
tiu, ags. tien, tyn, ahd. zehan, as. tehan, tian (zum -an s. Brugmann II       2,
20 f.) arm. tasn (zum a s. die Lit. bei Brugmann aaO., Boisacq s. v. dexa);
auf das Zahlsubst. dekm-t{{)- gehn zuriick alb. djete (Pedersen KZ. 36, 384),
lit. desimt[is ), lett. desimt, desmit (Muhlenbach-Endzelin I 459), aksl. desgtb,

ferner     ai.   dagat dagati-h „Dekade“, got. taihunt-
                        ,                                                     (:   dexad-) in talhunte-hund
(s.Brugmann II 2 2, 35 f.) „
%%%%%% NEXT
786                                              deg-   — dem-, dema-
dt.Hand wobei de-kmt entweder als „zwei Hande“ oder „Hand“ seiber als
                ,



                       s. z. B. Thurneysen KZ. 26, 310 Anm. t,
*(d)komt aufgefaBt wird,                                          Brug-
mann aaO. 4, Pedersen KZ. 38, 410, Hirt IA. 8, 59 f., Zupitza Gutt. 183,
Stewart BB. 30, 229, v. Blankenstein IP. 21, 109 (auch unter *kom)
   Hierher idg. *k m t 6 m „bundert“ aus ** (d')kmtom ai. eat ant, av. satam,    :




gr. E-xazuv lat. centum air. cet, cymr. cant bret. leant, corn, cans, got. hund,
                     ,                ,                          ,

ahd. hunt „100‘ c anord. hund -rad ,,Gro61mndert“ (120), lit. Simtas, lett. simts
                             ,


(Miihlenbach-Endzelin III 841), aksl. szto (zur Entlebnungsfrage s. Brugmann
41, Einzelheiten ebda. 40    46).            —          —
                                      Dazu eine r-Ableitung in lat. centuria                              ,

anord. hundari , ahd. huntari n. „Hundertschaft, Gau“, aksl. sztorica ,,Hundert-
schaft“,lit. simteriopas „hundertartig“, s. zur Bildung Brugmann Distr. 26 f.,

auch iiber lat. decu-riu, d. abl. semenies, umbr. teqtiries und gegen Schulzes
aaO. Ansatz eines idg. *cleku- fur decu-ria got. tigu- (umbr. tekvias osk.                         ,


dekkviarim ist unklarer Bed., s. zu ersterem Laird Cl. Phil. 1, 334).

deg- „packen“?
      Got. tekan „beriihren“, anord. tak
```


## [2026-09-05T17:53:02.409Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/deca-",
 "prompt": "Quote the etymology of the prefix deca-/dec- and also deci-. Which is from Greek deka and which from Latin decimus, and what does it say about the metric system convention (Greek for multiples, Latin for fractions)?"
}
```


### [2026-09-05T17:53:08.399Z] TOOL RESULT

```
# Etymology of Deca- and Deci-

**Deca-/Dec-:** According to the source, this prefix means "ten" and comes from the "Latinized combining form of Greek _deka_ 'ten.'"

**Deci-:** The page states that in the metric system, "deci- means 'divided by ten.'"

**Metric System Convention:** The source explicitly clarifies the pattern: "In the metric system, 'multiplied by ten;' while _deci-_ means 'divided by ten.'"

However, the document does not specify that deca- derives from Greek while deci- derives from Latin. It only identifies deca- as coming from Greek _deka_. The etymology of deci- as a separate Latin-derived form is not detailed in this particular content.
```


## [2026-09-05T17:54:12.604Z] TOOL CALL #75: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://abadis.ir/fatofa/دوجین/' --note 'page 114 node 12: Mo'\"'\"'in [فا - فر.] and Dehkhoda (از فرانسوی) on دوجین = twelve of a thing' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/dozen' --note 'page 114 nodes 11,13: dozen < OFr dozaine < doze < Lat duodecim' ; python3 tools/fetch_source.py 'https://www.etymonline.com/word/deca-' --note 'page 114 node 11: deca- is the Latinized form of Greek deka; metric multiples use Greek prefixes, fractions Latin (deci-)' ; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg114.png data/verification/sources/refs/ocr/BOOK/114.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3"
}
```


### [2026-09-05T17:54:18.203Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/00ce8741315d1238.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e31540f8c44d34e5.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/29d2d8c9ace98b9f.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r-- 1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-05T17:54:20.734Z] TOOL CALL #76: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/114.png && echo ok"
}
```


### [2026-09-05T17:54:20.772Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/114.png
ok
```


## [2026-09-05T18:01:08.171Z] TOOL CALL #77: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk114.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PIE = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/déḱm̥\"\nE_DINAR = \"https://www.etymonline.com/word/dinar\"\nW_YAZ = \"https://en.wiktionary.org/wiki/یازده\"\nW_DINAR = \"https://en.wiktionary.org/wiki/دینار\"\nAB_DOJIN = \"https://abadis.ir/fatofa/دوجین/\"\nE_DOZEN = \"https://www.etymonline.com/word/dozen\"\nE_DECA = \"https://www.etymonline.com/word/deca-\"\n\nPOK = {\"ref\": \"POK:191\", \"status\": \"supports\",\n       \"note\": \"Pokorny IEW p.191/192 (POK_01.txt leaf 202, printed '191'/'192' visible in the leaf): head-entry 'dekm̥, dekm̥-t, deku- ,zehn', Ordinale dekm̥o-s, dekm̥to-s' — 'Ai. daśa, av. dasa; arm. tasn ...; gr. δέκα, lat. decem (denī ,je zehn' aus *dek-noi) ... got. taihun ..., ags. tien, tyn, as. tehan, ahd. zehan'. Exactly the root, label and gloss of the chart.\"}\n\nnodes = []\n\ndef N(**kw):\n    nodes.append(kw)\n\nN(id=1, lang=\"Avestan / Old Persian\",\n  words=\"dasa; aeva-dasa; tri-dasa; xšvaš-dasa; nava-dasa\",\n  verdict=\"plausible\",\n  derivation=(\n    \"PIE *deḱm̥ 'ten' > Proto-Indo-Iranian *dáća > Avestan dasa, Sanskrit dáśa: the PIE palatal *ḱ became the \"\n    \"satem sibilant ś/s, and the syllabic *m̥ was resolved as -a. The 'teens' are copulative compounds of the unit \"\n    \"with dasa: *aēva-dasa 'eleven' (aēva- 'one'), *θri-dasa 'thirteen', *xšvaš-dasa 'sixteen', *nava-dasa \"\n    \"'nineteen'. Two reservations. (a) All five forms are Avestan; genuine Old Persian numerals above 'nine' are \"\n    \"not attested in the inscriptions (they are written with numeral signs), so Kent's lexicon has only navama- \"\n    \"'ninth' and reconstructs proto-Aryan *dasama- 'tenth' — Nourai takes the 'O.P.' column of Platts's grammar \"\n    \"at face value. (b) In the Avesta the compounds are attested chiefly as ordinals (aēvandasa- 'eleventh', \"\n    \"θridasa- 'thirteenth', xšvaš.dasa-, nava.dasa- 'nineteenth'); Bartholomae accordingly starts them with an \"\n    \"asterisk as cardinals (*nava.dasa indekl. Zw. '19'). Nourai's 'tri-dasa' is a simplification of θri-dasa.\"),\n  derivation_fa=(\n    \"«ده» و اعداد یازده تا نوزده در ایرانی باستان از ریشهٔ هندواروپایی آغازین *deḱm̥ می‌آید: کاف کامی هندواروپایی در \"\n    \"شاخهٔ ساتم به س بدل شده و *m̥ هجایی به «ـه/a» رسیده، پس اوستایی dasa و سنسکریت dáśa. عددهای میانی ترکیب \"\n    \"همپایهٔ یکان با dasa است: *aēva-dasa «یازده»، *θri-dasa «سیزده»، *xšvaš-dasa «شانزده»، *nava-dasa «نوزده». \"\n    \"دو نکته: نخست آنکه این صورت‌ها اوستایی‌اند و در پارسی باستان عدد ده به بالا در سنگ‌نبشته‌ها با نشانهٔ عددی \"\n    \"نوشته می‌شده، از این رو کنت در واژه‌نامهٔ خود تنها navama- «نهم» را ثبت کرده است؛ نورایی برچسب «پارسی باستان» را \"\n    \"از دستور پلاتس گرفته است. دوم آنکه بارتولومه این ترکیب‌ها را بیشتر به‌صورت عدد ترتیبی ثبت کرده و صورت اصلی را \"\n    \"با ستاره آورده است. ادعای نورایی در کل پذیرفتنی است، اما برچسب زبانی آن دقیق نیست.\"),\n  sources=[W_PIE],\n  ref_check=[\n    POK,\n    {\"ref\": \"GPL:41\", \"status\": \"supports\",\n     \"note\": \"Platts–Ranking, Grammar of the Persian Language, printed p.41 (GPL.txt, the leaf headed 'Numerals—The Cardinal Numbers 41', §46) prints the table: '10 ده (O.P. dasa)', '11 یازده (O.P. aivadasa)', '13 سیزده (O.P. thridasa)', '16 شانزده (O.P. khshvashdasa)', '19 نوزده (O.P. navadasa)' — the exact source of Nourai's row.\"}],\n  consulted=[\n    {\"src\": \"BRT\", \"where\": \"s.v. dasa- (AiW col. ~673) and nava.dasa-\", \"stance\": \"supports\",\n     \"note\": \"BRT.txt: 'j., g. dasa indekl. Zw. \\\\'zehn\\\\''; and 'Ableit. aus *nava.dasa indekl. Zw. \\\\'19\\\\'. — ai. navadaśá- Adj.; oss. vgl. näudäs \\\\'19\\\\'. — Pü.: navazdahum'; 'xšvas.dasa' cited from Yt. 1.8.\"},\n    {\"src\": \"KNT\", \"where\": \"§149 IV and lexicon s.v. navama-\", \"stance\": \"partial\",\n     \"note\": \"Kent has only 'navama- adj. \\\\'ninth\\\\': Av. nāuma-, Skt. navamá-, pAr. navama- remade from pIE neu̯eno- after pAr. dasama- \\\\'tenth\\\\''. No Old Persian cardinal 'ten' or 'teen' is attested, so the 'Old Persian' half of the box is reconstruction, not record.\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.785 s.v. dekm̥\", \"stance\": \"supports\",\n     \"note\": \"'dekm̥ \\\\'zehn\\\\'. Ai. daśa, av. dasa, gr. δέκα, lat. decem ... got. taihun ... ags. tien, tyn, ahd. zehan, as. tehan, tian'.\"}])\n\nN(id=2, lang=\"Pahlavi\",\n  words=\"dah; yâcdah; sîkdah; šâncdah; navasdah\",\n  verdict=\"transcription_suspect\",\n  error_in=\"book\", book_prints=\"sîkdah; navasdah\", correct_form=\"sîcdah (sēzdah); navâcdah (navazdah)\",\n  derivation=(\n    \"Middle Persian continues the Old Iranian numerals with the regular loss of final syllables: *dasa > dah \"\n    \"(intervocalic -s- > -h-), and the teens *aēva-dasa, *θri-dasa, *xšvaš-dasa, *nava-dasa > yāzdah, sēzdah, \"\n    \"šānzdah, nōzdah. Nourai's spellings with ⟨c⟩ are Book-Pahlavi transliterations, where ⟨c⟩ stands for /z/: \"\n    \"MacKenzie prints 'yāzdah [y'cdh] eleven' and 'dwāzdah [dw'cdh] twelve', and Horn cites the Pahlavi ordinals \"\n    \"sicdahum, sāncdahum, navācdahum. TWO OF THE FIVE FORMS ARE WRONG IN THE PRINTED BOOK: 'sîkdah' (page image \"\n    \"shows ⟨k⟩) should be sîcdah = sēzdah 'thirteen' (Horn no.763 'phlv. sicdahum'; MacKenzie's English index \"\n    \"'thirteen sēzdah'), and 'navasdah' (⟨s⟩) should be navâcdah = navazdah 'nineteen' (Horn no.1048 'phlv. \"\n    \"navācdahum'; Bartholomae 'Pü.: navazdahum'). The JSON reproduces the page faithfully, so these are Nourai's \"\n    \"own misprints, not extraction errors. dah, yâcdah and šâncdah are correct.\"),\n  derivation_fa=(\n    \"در فارسی میانه (پهلوی) شمارهٔ ده و عددهای میانی از صورت‌های ایرانی باستان با کاهش هجای پایانی و نرم‌شدن س میان \"\n    \"دو واکه به ه پدید آمده است: *dasa > dah؛ و *aēva-dasa > yāzdah، *θri-dasa > sēzdah، *xšvaš-dasa > šānzdah، \"\n    \"*nava-dasa > nōzdah/navazdah. نگارش‌های نورایی با ⟨c⟩ در واقع حرف‌نویسی خط پهلوی است که در آن ⟨c⟩ برابر /z/ \"\n    \"است؛ مکنزی yāzdah را [y'cdh] و dwāzdah را [dw'cdh] آورده و هرن نیز صورت‌های sicdahum و sāncdahum و navācdahum \"\n    \"را ثبت کرده است. اما دو صورت در خودِ چاپ کتاب غلط است: «sîkdah» باید «sîcdah» (= sēzdah) باشد و «navasdah» \"\n    \"باید «navâcdah» (= navazdah). این خطای چاپی کتاب است، نه خطای خوانش اسکن؛ تصویر صفحه همین دو صورت غلط را \"\n    \"نشان می‌دهد. سه صورت دیگر درست‌اند.\"),\n  sources=[W_YAZ],\n  ref_check=[{\"ref\": \"BQT\", \"status\": \"not_checked\",\n              \"note\": \"Nourai cites 'BQT' with no page. Borhān-e Qāṭeʿ is a New Persian dictionary; Moʿin's footnotes give Pahlavi forms only sporadically and none of the five numerals could be located without a page reference.\"}],\n  consulted=[\n    {\"src\": \"PHD\", \"where\": \"s.v. dah, yāzdah, dwāzdah; English index 'thirteen', 'twelve'\", \"stance\": \"supports\",\n     \"note\": \"PHD_mackenzie.txt: 'dah [...| M dh, N ~] ten.'; PHD.txt: 'yāzdah [y'cdh | M y'zdh, N ~] eleven.'; 'dwāzdah [dw'cdh | M dw'zdh, N duwāzdah] twelve.'; index: 'thirteen sēzdah.' — confirms ⟨c⟩ = /z/ and that 'thirteen' is sēzdah, not *sīkdah.\"},\n    {\"src\": \"HRN\", \"where\": \"nos. 587, 763, 770, 1048\", \"stance\": \"partial\",\n     \"note\": \"Horn no.587 'deh zehn ... phlv. dahum'; no.763 'sizdeh \\\\'dreizehn\\\\'. aw. θridasa; phlv. sicdahum'; no.770 'sānzdeh \\\\'sechzehn\\\\'. aw. xšvašdasa; phlv. sāncdahum'; no.1048 'nuvāzdeh \\\\'neunzehn\\\\'. aw. navadasa-; phlv. navācdahum'. Supports the chain but shows sicdahum / navācdahum against the book's 'sîkdah' / 'navasdah'.\"},\n    {\"src\": \"BRT\", \"where\": \"s.v. nava.dasa-\", \"stance\": \"partial\",\n     \"note\": \"'Pü.: navazdahum' — Bartholomae's Pahlavi form for 'nineteenth' is navazdahum, again with z, not s.\"}])\n\nN(id=3, lang=\"Persian\",\n  words=\"dah «ده ١»; yâzdah «یازده»; sîzdah «سیزده»; šânzdah «شانزده»; nŭzdah «نوزده»\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"New Persian inherits the Middle Persian numerals unchanged in substance: dah 'ten' (MP dah < Av. dasa), \"\n    \"yāzdah 'eleven' (MP yāzdah, Wiktionary reconstructing Old Iranian *aiva-ča-daθa), sīzdah 'thirteen' \"\n    \"(MP sēzdah, with MP ē > NP ī), šānzdah 'sixteen' (the nasal spread from the preceding pānzdah 'fifteen' — \"\n    \"Horn no.770 says explicitly 'np. šānzdeh ist durch das ihm vorhergehende pānzdeh beeinflusst'), and \"\n    \"nūzdah/nōzdah 'nineteen' (MP navazdah; Horn no.1048 notes np. nuvāzdeh replaced an expected *nudeh by \"\n    \"analogy). Horn no.763 likewise calls np. sīzdeh 'eine Analogiebildung'. All five words and glosses are correct.\"),\n  derivation_fa=(\n    \"فارسی نو همان شمارگان فارسی میانه را دارد: «ده» از dah، «یازده» از yāzdah، «سیزده» از sēzdah (ای کشیدهٔ فارسی \"\n    \"میانه در فارسی نو به ی بدل شده)، «شانزده» از šānzdah و «نوزده» از navazdah/nōzdah. هرن (شمارهٔ ۷۷۰) تصریح می‌کند \"\n    \"که «ن» در «شانزده» به قیاس «پانزده» پیشین افزوده شده، و (شمارهٔ ۱۰۴۸) «نوزده» به جای صورت منتظَر *نُده ساخت \"\n    \"قیاسی است؛ «سیزده» را هم ساخت قیاسی می‌داند. هر پنج واژه و معنای آن‌ها درست است و ادعای نورایی تأیید می‌شود.\"),\n  sources=[W_YAZ],\n  ref_check=[{\"ref\": \"BQT\", \"status\": \"partial\",\n              \"note\": \"Cited without a page. Borhān-e Qāṭeʿ has the headwords ده / یازده / سیزده etc. as ordinary lemmas but gives no etymology for them; the derivation itself has to be taken from Horn/MacKenzie.\"}],\n  consulted=[\n    {\"src\": \"HRN\", \"where\": \"nos. 587, 763, 770, 1048\", \"stance\": \"supports\",\n     \"note\": \"no.587 'deh zehn ... aw. dasa \\\\'zehn\\\\'; phlv. dahum; ai. daśa; arm. tasn'; no.763 'np. sīzdeh ist eine Analogiebildung'; no.770 'np. šānzdeh ist durch das ihm vorhergehende pānzdeh beeinflusst'; no.1048 'Np. nuvāzdeh statt nudeh ist eine Analogiebildung'.\"},\n    {\"src\": \"PHD\", \"where\": \"s.v. dah, yāzdah; index 'thirteen'\", \"stance\": \"supports\",\n     \"note\": \"MacKenzie gives the New Persian outcome in each entry: 'dah [... | M dh, N ~] ten', 'yāzdah [y'cdh | M y'zdh, N ~] eleven' — 'N ~' meaning New Persian identical.\"},\n    {\"src\": \"HUB\", \"where\": \"no. 280 and note to no. 763\", \"stance\": \"supports\",\n     \"note\": \"Hübschmann, Persische Studien: 'Np. panǰdah \\\\'fünfzehn\\\\' hat doch hörbares h (wegen dah \\\\'zehn\\\\')' and, to Horn 763, 'paz. sēzdahum \\\\'der dreizehnte\\\\' Min. 61.184. Also ist die ältere np. Form ...' — the h of the teens is the h of dah.\"}])\n\nN(id=4, lang=\"Avestan / Old Persian\",\n  words=\"saiti 1, sat : a suffix meaning ten; vi-saiti : twenty; thri-sat : thirty; čatvare-sat : forty; pančâ-sat : fifty\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"The decads 20–50 are built on the zero-grade *-dḱom-t- / *-ḱm̥t- of the same word for 'ten', which after the \"\n    \"loss of the initial d- appears in Indo-Iranian as -śat-/-sat- and in Avestan as -sant-/-saiti-: \"\n    \"vīsaiti 'twenty' (< *wi-ḱm̥t-ī, a dual 'two tens'), θrisant-/θrisas 'thirty', čaθwarə-sant- 'forty', \"\n    \"panča-sant- 'fifty'; compare Greek -κοντα, Latin -gintā, Sanskrit -śat-. Nourai's 'saiti 1, sat' is exactly \"\n    \"these two allomorphs; his spellings 'thri-sat, čatvare-sat, pančâ-sat' follow Platts's transcription.\"),\n  derivation_fa=(\n    \"دهگان‌های بیست تا پنجاه بر پایهٔ صورت بی‌واکهٔ همان واژهٔ «ده» (*-ḱm̥t-) ساخته شده‌اند که پس از افتادن دال آغازین \"\n    \"در هندوایرانی -śat-/-sat- و در اوستایی -sant-/-saiti- شده است: vīsaiti «بیست» (در اصل دوگانِ «دو ده»)، \"\n    \"θrisant- «سی»، čaθwarə-sant- «چهل»، panča-sant- «پنجاه»؛ همتای یونانی آن ‎-κοντα و همتای لاتینی ‎-gintā است. \"\n    \"دو صورت «saiti» و «sat» که نورایی آورده دقیقاً همین دو گونهٔ پسوندند و ادعای او درست است.\"),\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\": \"GPL:41\", \"status\": \"supports\",\n     \"note\": \"Platts p.41: '20 بیست (Phl. vist; O.P. vīsaiti)', '30 سی (Phl. sih; O.P. thrisat)', '40 چهل (Phl. chahal; O.P. chatvaresata)', '50 پنجاه (Phl. panchah; O.P. panchasat)' — Nourai's row verbatim.\"},\n    {\"ref\": \"POK:191\", \"status\": \"supports\",\n     \"note\": \"Pokorny under dekm̥: 'Changing through ablaut (d)ḱm̥t- (Dual), (d)ḱómt- (Plur.) in figures often ... e.g. Old Indic triṃśát, Avestan θrisąs, Armenian ere-sun, gr. τριάκοντα ..., Latin tri-gintā ...; s. also under u̯ī-ḱm̥tī \\\\'20\\\\''.\"}],\n  consulted=[\n    {\"src\": \"BRT\", \"where\": \"s.v. vīsant-, čaθwarə-sant-, panča-sant-\", \"stance\": \"supports\",\n     \"note\": \"'j. vīsant- fem. Zw. \\\\'zwanzig\\\\', mit Gen.: vīsaiti (AD.) upazananąm Yt.10.122'; 'j. čaθ-warə-sant- fem. Zw. \\\\'vierzig\\\\''; 'j. panča-sant- fem. Zw. \\\\'fünfzig\\\\' ... Ableit. — ai. pañcāśát- f., np. panjāh'.\"},\n    {\"src\": \"SYN\", \"where\": \"§13.31 Note on the numerals, p.936\", \"stance\": \"supports\",\n     \"note\": \"Buck: 'For 20-90 certain IE cpds., the second part of which seems to be obscurely related to the numeral for \\\\'ten\\\\', have been partly retained (for 20 Grk. εἴκοσι, Dor. ϝίκατι, Lat. viginti, Skt. viṃśati-, etc.; for the others Grk. -κοντα, Lat. -ginta, Skt. -śat-, etc.)'.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. u̯iḱmti\", \"stance\": \"supports\",\n     \"note\": \"Mann: 'u̯iḱmti (u̯iḱomti, u̯iḱm) \\\\'twenty\\\\'. Cf. u̯i-, px. and dui-; deḱmti, deḱm. WP I,313 Skt. viṃśatí; Av. vīsaiti; Per. bist ...'.\"}])\n\nN(id=5, lang=\"Persian\",\n  words=\"(no transliteration in the box) — بیست ، سی ، چهل ، پنجاه\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"The four Persian decads continue the Avestan -sant-/-saiti- forms through Middle Persian: Av. vīsaiti > MP \"\n    \"wīst > NP bīst 'twenty' (initial w- > b- is the regular New Persian treatment); Av. θrisant- > MP sīh > NP \"\n    \"sī 'thirty' (θr- > s-, the final -h dropped); Av. čaθwarə-sant- > MP čihil > NP čehel 'forty' (with the \"\n    \"haplology of the middle syllables already in Middle Persian); Av. panča-sant- > MP panjāh > NP panjāh \"\n    \"'fifty' (the suffix reduced to -āh). Bartholomae himself gives 'np. panjāh' as the derivative of \"\n    \"panča-sant-, and Mann gives 'Per. bist' under u̯iḱmti.\"),\n  derivation_fa=(\n    \"چهار دهگانِ «بیست، سی، چهل، پنجاه» دنبالهٔ همان ساخت اوستایی‌اند و از راه فارسی میانه به فارسی نو رسیده‌اند: \"\n    \"اوستایی vīsaiti > پهلوی wīst > «بیست» (واو آغازین ایرانی در فارسی نو به ب بدل شده)؛ θrisant- > پهلوی sīh > \"\n    \"«سی»؛ čaθwarə-sant- > پهلوی čihil > «چهل»؛ panča-sant- > پهلوی panjāh > «پنجاه». بارتولومه خودْ np. panjāh را \"\n    \"زیر مدخل panča-sant- آورده و مان (Mann) نیز «bist» فارسی را ذیل *u̯iḱmti ثبت کرده است. ادعای نورایی درست است.\"),\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\": \"GPL:41\", \"status\": \"supports\",\n     \"note\": \"Platts p.41 gives exactly these four with their Pahlavi antecedents: 'بیست (Phl. vist)', 'سی (Phl. sih)', 'چهل (Phl. chahal)', 'پنجاه (Phl. panchah)'.\"},\n    {\"ref\": \"BQT\", \"status\": \"not_checked\",\n     \"note\": \"cited without a page; the Borhān headwords بیست/سی/چهل/پنجاه carry no etymological footnote that could be located without one.\"}],\n  consulted=[\n    {\"src\": \"HRN\", \"where\": \"nos. 254, 760, 454, 329\", \"stance\": \"supports\",\n     \"note\": \"no.254 'bīst \\\\'zwanzig\\\\'. aw. vīsaiti-; phlv. vist'; no.760 'sī \\\\'dreissig\\\\'. aw. θrisatəm; phlv. sih, pāz. sī; ai. triṃśát'; no.454 'čihil, čil \\\\'vierzig\\\\''; no.329 'panjāh \\\\'fünfzig\\\\''.\"},\n    {\"src\": \"PHD\", \"where\": \"s.v. wīst, sīh, čihil, panjāh\", \"stance\": \"supports\",\n     \"note\": \"MacKenzie: 'wīst [20; wyst' | = M, N bist] twenty'; English index 'thirty sih', 'fifty panjāh' — the Middle Persian link Nourai's arrow needs.\"},\n    {\"src\": \"BRT\", \"where\": \"s.v. panča-sant-\", \"stance\": \"supports\",\n     \"note\": \"'Ableit. — ai. pañcāśát- f., np. panjāh' — Bartholomae derives the New Persian word from the Avestan decad himself.\"}])\n\nN(id=6, lang=\"Avestan / Old Persian\",\n  words=\"-iti, -ti : a suffix meaning ten; xšvaš-ti : sixty; hapta-iti : seventy; ašta-iti : eighty; nava-iti : ninety\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"For 60–90 Indo-Iranian used an abstract feminine in *-ti- built on the unit ('a sixtiness'), historically the \"\n    \"same 'ten'-element in a different suffixal dress: Av. xšvašti- 'sixty' (xšvaš 'six'), haptāiti- 'seventy' \"\n    \"(hapta 'seven'), aštāiti-/aštātay- 'eighty' (ašta 'eight'), navaiti- 'ninety' (nava 'nine'); compare Sanskrit \"\n    \"ṣaṣṭí-, saptatí-, aśītí-, navatí-. Pokorny cites 'Old Indic saptatí-, Avestan haptaiti- \\\\'70\\\\'' in the \"\n    \"same article. Nourai's '-iti, -ti' correctly states the two shapes of the suffix (-ti after a consonant, \"\n    \"-āiti after a vowel).\"),\n  derivation_fa=(\n    \"برای شصت تا نود، در هندوایرانی اسم مصدرِ مؤنثِ ساخته‌شده با پسوند *-ti- به کار می‌رفت که در اصل همان عنصر «ده» \"\n    \"با پسوندی دیگر است: اوستایی xšvašti- «شصت» (از xšvaš «شش»)، haptāiti- «هفتاد»، aštāiti-/aštātay- «هشتاد»، \"\n    \"navaiti- «نود»؛ همتای سنسکریت آن‌ها ṣaṣṭí-، saptatí-، aśītí- و navatí- است. پوکورنی نیز در همین مدخل \"\n    \"«saptatí- سنسکریت و haptaiti- اوستایی ‹۷۰›» را آورده است. دو گونهٔ ‎-ti و ‎-iti که نورایی نوشته درست است.\"),\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\": \"GPL:41\", \"status\": \"supports\",\n     \"note\": \"Platts p.41: '60 شصت for orig. شست (Phl. shasht; O.P. khshvashti)', '70 هفتاد (Phl. haftat; O.P. haptaiti)', '80 هشتاد (Phl. hashtat; O.P. ashtaiti)', '90 نود (Phl. navat; O.P. navaiti)'.\"},\n    {\"ref\": \"POK:191\", \"status\": \"supports\",\n     \"note\": \"Pokorny's dekm̥ article: '... also Old Indic saptatí-, Avestan haptaiti- \\\\'70\\\\'' — the -ti decads are treated inside the same root entry, as Nourai's arrow from the root assumes.\"}],\n  consulted=[\n    {\"src\": \"BRT\", \"where\": \"s.v. xšvašti-, aštātay-\", \"stance\": \"supports\",\n     \"note\": \"'j. xšvašti- fem. Zw. \\\\'sechzig\\\\''; 'j. aštātay- fem. Zw. \\\\'achtzig\\\\': aštāitīm maiδyairyehe daŋhuš ... A.3.11'.\"},\n    {\"src\": \"HRN\", \"where\": \"nos. 781, 1096, 1100, 1049\", \"stance\": \"supports\",\n     \"note\": \"no.781 'šest, šast \\\\'sechzig\\\\'. aw. xšvašti- \\\\'sechzig\\\\''; no.1100 'haftād \\\\'siebzig\\\\'. aw. haptāiti-; phlv. haftāt'; no.1096 'heštād \\\\'achtzig\\\\'. aw. aštāiti-; phlv. haštāt bzw. aštāt'; no.1049 'navad \\\\'neunzig\\\\'. aw. navaiti-; phlv. navat'.\"},\n    {\"src\": \"SYN\", \"where\": \"§13.31, p.936\", \"stance\": \"supports\",\n     \"note\": \"Buck notes the break in formation 'between 60 and 70 in Grk., Goth., etc.' — i.e. that the higher decads are formed differently from 20–50, exactly why Nourai gives them a separate box.\"}])\n\nN(id=7, lang=\"Persian\",\n  words=\"(no transliteration in the box) — شست ، هفتاد ، هشتاد ، نود\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Av. xšvašti- > MP šast > NP šast 'sixty' (xšv- > š-); Av. haptāiti- > MP haftād > NP haftād 'seventy'; \"\n    \"Av. aštāiti- > MP haštād > NP haštād 'eighty' (with the prothetic h- taken over from haft/hašt); \"\n    \"Av. navaiti- > MP nawad > NP navad 'ninety'. The Avestan -āiti- regularly gives MP/NP -ād. Nourai's \"\n    \"spelling شست for 'sixty' is not a mistake: it is the etymological spelling, and Platts prints '60 شصت for \"\n    \"orig. شست', the modern ص being a later Arabising re-spelling.\"),\n  derivation_fa=(\n    \"اوستایی xšvašti- > پهلوی šast > «شست/شصت»؛ haptāiti- > پهلوی haftād > «هفتاد»؛ aštāiti- > پهلوی haštād > \"\n    \"«هشتاد» (های آغازین به قیاس «هفت/هشت» افزوده شده)؛ navaiti- > پهلوی nawad > «نود». پسوند ‎-āiti اوستایی در \"\n    \"فارسی به ‎-اد بدل شده است. نگارش «شست» در کتاب غلط نیست؛ همان املای ریشه‌شناختی است و پلاتس نیز می‌نویسد \"\n    \"«شصت که در اصل شست بوده»؛ صاد بعدها به قیاس املای عربی نوشته شده است. ادعای نورایی درست است.\"),\n  sources=[W_PIE],\n  ref_check=[{\"ref\": \"GPL:41\", \"status\": \"supports\",\n              \"note\": \"Platts p.41 lists these four Persian words with their Pahlavi and 'O.P.' antecedents (شصت/شست, هفتاد, هشتاد, نود), including the remark '60 شصت for orig. شست'.\"}],\n  consulted=[\n    {\"src\": \"PHD\", \"where\": \"s.v. šast, nawad; index 'seventy', 'eighty'\", \"stance\": \"supports\",\n     \"note\": \"MacKenzie: 'šast [60 | M šst, N ~] sixty'; 'nawad [90 | N ~] ninety' — the Middle Persian stage of the arrow.\"},\n    {\"src\": \"HRN\", \"where\": \"nos. 781, 1049, 1096, 1100\", \"stance\": \"supports\",\n     \"note\": \"Horn gives each New Persian word with its Avestan and Pahlavi antecedent (šast : aw. xšvašti-; navad : aw. navaiti-, phlv. navat; haštād : phlv. haštāt; haftād : phlv. haftāt).\"}])\n\nN(id=8, lang=\"Germanic\",\n  words=\"tehun, tehan : ten\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"PIE *deḱm̥ > Proto-Germanic *tehun by Grimm's Law (*d > t, *ḱ > h) with the syllabic nasal resolved as -un; \"\n    \"Gothic taihun, Old Norse tíu, Old English tīen/tȳn, Old High German zehan, Old Saxon tehan/tian. Strictly, \"\n    \"*tehun is the Proto-Germanic form while 'tehan' is the Old Saxon/Old High German shape (Walde-Pokorny lists \"\n    \"'as. tehan, tian' and Pokorny explains the -a- of ahd. zehan as carried over from the compounds); Nourai's \"\n    \"box collapses the two but names real forms.\"),\n  derivation_fa=(\n    \"*deḱm̥ هندواروپایی بر پایهٔ قانون گریم (د > ت، کاف کامی > ه) به ژرمنی آغازین *tehun رسیده و *m̥ هجایی به ‎-un \"\n    \"بدل شده است: گوتی taihun، نورس کهن tíu، انگلیسی کهن tīen/tȳn، آلمانی علیای کهن zehan، ساکسون کهن tehan. \"\n    \"به‌دقت، صورت ژرمنی آغازین *tehun است و tehan گونهٔ ساکسون کهن/آلمانی کهن؛ نورایی این دو لایه را یکی گرفته، اما \"\n    \"هر دو صورت واقعی‌اند. ادعای او درست است.\"),\n  sources=[W_PIE],\n  ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\",\n              \"note\": \"Watkins (AHD Indo-European Roots, 1985 ed., s.v. dekm): 'I. Basic form *dekm. 1. Germanic *tehun in: a. Old English tien, ten: TEN' — precisely this node and the next. [Pok. dekm 191.]\"}],\n  consulted=[\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.785\", \"stance\": \"supports\",\n     \"note\": \"'got. taihun (entweder für *taihu mit nach dem Ordinale aufgefrischtem -n, oder aus idg. *dekm̥-t), anord. tíu, ags. tien, tyn, ahd. zehan, as. tehan, tian'.\"},\n    {\"src\": \"POK\", \"where\": \"p.192 (POK_01 leaf 202)\", \"stance\": \"supports\",\n     \"note\": \"'got. taihun (-n wie in sihun, niun), an. tíu, ags. tien, tyn, as. tehan, ahd. zehan (a wohl aus den Kompositis, Brugmann II 2, 18)'.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. dekm, dekmti\", \"stance\": \"supports\",\n     \"note\": \"Mann: 'Go. taíhun, cpds. -tigun; OE ten; téoða, teogeða; OHG zëhan; ON tíu, tí-'.\"}])\n\nN(id=9, lang=\"English\",\n  words=\"ten, teen\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Old English tīen/tȳn > Middle English ten > modern ten. The bound form -teen is Old English -tēne/-tȳne, the \"\n    \"same numeral used as the second member of thirteen…nineteen (OE þrēotīene, etc.); the free noun 'teen(s)' \"\n    \"('the teenage years') is a back-formation from those compounds, first in the 17th century. Both are \"\n    \"unquestionably from Germanic *tehun.\"),\n  derivation_fa=(\n    \"انگلیسی کهن tīen/tȳn به انگلیسی میانه ten و سپس ten امروزی رسیده است. جزء وابستهٔ ‎-teen همان عدد است در \"\n    \"ترکیب‌های سیزده تا نوزده (انگلیسی کهن þrēotīene و مانند آن)، و اسم teens («سال‌های نوجوانی») در سدهٔ هفدهم از \"\n    \"همین ترکیب‌ها بازساخته شده است. هر دو بی‌گمان از ژرمنی *tehun‌اند و ادعای نورایی درست است.\"),\n  sources=[W_PIE],\n  ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\",\n              \"note\": \"The chart gives this box no reference (confirmed on the page image); the claim is covered by the AHD citation of the parent Germanic box.\"}],\n  consulted=[\n    {\"src\": \"AHD\", \"where\": \"s.v. dekm, I.1.a\", \"stance\": \"supports\",\n     \"note\": \"'Germanic *tehun in: a. Old English tien, ten: TEN'; the same article puts 'Extended form *dekmt- in Germanic *-tig in Old English -tig, ten (see dwo-)' for the decad suffix.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. ten / denarius (KLN_1966)\", \"stance\": \"supports\",\n     \"note\": \"Klein's denarius entry cross-refers 'See ten and cp. decem-, decimal' — i.e. English ten belongs to the same root as Latin decem.\"}])\n\nN(id=10, lang=\"Latin\",\n  words=\"decem, den : ten; decimus : tenth; duo-decem : twelve\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"PIE *deḱm̥ > Latin decem (the syllabic *m̥ > -em). 'den' is the distributive dēnī 'ten each', which Klein and \"\n    \"Pokorny both derive from *dek-noi (Pokorny: 'lat. decem (denī \\\\'je zehn\\\\' aus *dek-noi)'); AHD calls it an \"\n    \"'irregular Latin distributive dēnī, by tens, ten each (formed by analogy with nōnī, nine each)'. decimus \"\n    \"'tenth' continues the PIE ordinal *deḱm̥-mo- (Pokorny: 'dekm̥mo-s in Old Indic daśamá-, Avestan dasama-, \"\n    \"Ossetic dæsæm, Latin decimus'). 'duo-decem' is Nourai's analytic spelling of duodecim 'twelve'.\"),\n  derivation_fa=(\n    \"*deḱm̥ هندواروپایی در لاتین decem شده (‎*m̥ هجایی به ‎-em بدل شده). صورت «den» همان dēnī «ده‌ده، هر ده تا» است \"\n    \"که کلاین و پوکورنی هر دو از *dek-noi می‌گیرند، و decimus «دهم» دنبالهٔ عدد ترتیبی هندواروپایی *deḱm̥mo- است \"\n    \"(پوکورنی: سنسکریت daśamá-، اوستایی dasama-، آسی dæsæm، لاتین decimus). «duo-decem» نیز صورت تحلیلی duodecim \"\n    \"«دوازده» است. ادعای نورایی درست است.\"),\n  sources=[W_PIE],\n  ref_check=[\n    {\"ref\": \"AHD:352\", \"status\": \"supports\",\n     \"note\": \"Nourai's AHD page numbers are pages of the 1976 AHD New College Edition body, which is not open online; the same publisher's root list (Watkins 1985, AHD_watkins1985.txt s.v. dekm) says 'Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; DECENARY, DECENNIUM, DECUSSATE, DOZEN, DUODECIMAL ...' and 'Irregular Latin distributive dēnī, by tens, ten each'.\"},\n    POK],\n  consulted=[\n    {\"src\": \"KLN\", \"where\": \"s.v. denarius (KLN_1966, leaf 247 ≈ p.470)\", \"stance\": \"supports\",\n     \"note\": \"'Denarius derives fr. dēnī, \\\\'ten each\\\\', which stands for *dec-noi, fr. decem, \\\\'ten\\\\'. (Cp. sēnī, \\\\'six each\\\\', fr. *sex-noi.)'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.785\", \"stance\": \"supports\",\n     \"note\": \"'lat. decem, umbr. desen-(duf) \\\\'(duo-)decim\\\\'' — Umbrian desen-duf is itself the '12' compound Nourai writes as duo-decem.\"}])\n\nN(id=11, lang=\"French\",\n  words=\"deca : ten; deci : tenth; douzaine : dozen\",\n  verdict=\"plausible\",\n  derivation=(\n    \"douzaine 'dozen' is straightforwardly Latin: duodecim > Old French doze/douze, plus the collective suffix \"\n    \"-aine (< Latin -ēna), 12th c.; the -aine suffix marks an exact, not an approximate, count. déci- is likewise \"\n    \"Latin, taken from decimus when the metric system was legislated in 1795. But déca- is NOT from Latin decem: \"\n    \"the 1795 convention deliberately took Greek prefixes for the multiples (déca-, hecto-, kilo-, myria-) and \"\n    \"Latin ones for the submultiples (déci-, centi-, milli-), and Etymonline accordingly defines deca- as the \"\n    \"'Latinized combining form of Greek deka \\\\'ten\\\\''. So one of the three words in this box hangs from the \"\n    \"wrong parent — it belongs under Nourai's own Greek deka box (#20). NOTE: the printed page gives this box the \"\n    \"reference 'AHD', which the JSON records as null (extraction error).\"),\n  derivation_fa=(\n    \"«douzaine» به‌روشنی لاتینی است: duodecim > فرانسهٔ کهن doze/douze به‌علاوهٔ پسوند جمعیِ ‎-aine (از ‎-ēna لاتینی) در \"\n    \"سدهٔ دوازدهم میلادی. «déci-» نیز لاتینی است و هنگام تصویب نظام متری در ۱۷۹۵ از decimus گرفته شده. اما «déca-» \"\n    \"لاتینی نیست: در همان قانون ۱۷۹۵ آگاهانه پیشوندهای یونانی برای مضرب‌ها (déca-، hecto-، kilo-) و پیشوندهای \"\n    \"لاتینی برای کسرها (déci-، centi-، milli-) برگزیده شد، و اتیمانلاین نیز deca- را «صورت لاتینی‌شدهٔ deka یونانی» \"\n    \"می‌داند. پس یکی از سه واژهٔ این جعبه زیر ریشهٔ نادرست نشسته و باید ذیل جعبهٔ یونانیِ deka (شمارهٔ ۲۰) می‌آمد؛ \"\n    \"ادعای نورایی با این احتیاط پذیرفتنی است.\"),\n  sources=[E_DECA, E_DOZEN],\n  ref_check=[{\"ref\": \"AHD\", \"status\": \"partial\",\n              \"note\": \"The printed box carries 'AHD' (visible on the page image; the JSON has refs=null). Watkins s.v. dekm does list 'DOZEN' and 'DECI-' under Latin decem, but puts 'DECA-, DECADE' under 'Greek deka' — so the reference itself contradicts placing deca under Latin.\"}],\n  consulted=[\n    {\"src\": \"KLN\", \"where\": \"s.v. denier / denarius (KLN_1966)\", \"stance\": \"supports\",\n     \"note\": \"Klein: 'denier, n., a French coin. — F., fr. L. denarius, whence also OIt. danaio, It. danaro, Prov. denier, dinier, Sp. dinero, Port. dinheiro' — the parallel Latin>French line for the same root.\"},\n    {\"src\": \"AHD\", \"where\": \"s.v. dekm, I.2 and I.4\", \"stance\": \"partial\",\n     \"note\": \"'2. Latin decem, ten: ... DECI-, DECIMAL, ... DOZEN, DUODECIMAL' vs '4. Greek deka, ten: DEAN, DECA-, DECADE' — deca- is filed under Greek, not Latin.\"}])\n\nN(id=12, lang=\"Persian\",\n  words=\"dekâ- «دکا ـ (دکامتر)»; desî- «دسی ـ (دسیمتر)»; dojîn «دوجین»\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"All three are modern French loanwords in Persian, taken in the 19th–20th century with the metric system and \"\n    \"European commerce. دکا- (in دکامتر) is French déca-, دسی- (in دسیمتر) is French déci-, and دوجین is French \"\n    \"douzaine 'a dozen', the French -aine ending rendered in Persian as -ین. Moʿin defines دوجین as 'دوازده عدد از \"\n    \"یک شیء، بستهٔ دوازده‌تایی' and tags it [فا. - فر.] (Persian–French); Dehkhodā tags it simply '(از فرانسوی، اِ)'. \"\n    \"Moʿin's own متری table (s.v. دستگاه متری) uses دسیمتر and دکامتر as the standard Persian metric terms. \"\n    \"Nourai's arrow (French → Persian) is exactly right; only the ultimate Latin/Greek split above it is imprecise \"\n    \"(see node 11).\"),\n  derivation_fa=(\n    \"هر سه واژه وام‌واژه‌های نوِ فرانسوی در فارسی‌اند که در سدهٔ سیزدهم و چهاردهم خورشیدی همراه با نظام متری و \"\n    \"بازرگانی اروپایی وارد شده‌اند: «دکا ـ» (در دکامتر) از déca-، «دسی ـ» (در دسیمتر) از déci-، و «دوجین» از \"\n    \"douzaine فرانسوی که پایانهٔ ‎-aine آن در فارسی به ‎-ین بدل شده است. معین «دوجین» را «دوازده عدد از یک شیء، بستهٔ \"\n    \"دوازده‌تایی» معنی کرده و برچسب [فا. ـ فر.] بر آن نهاده، و دهخدا نیز آن را «از فرانسوی» می‌داند. جدول «دستگاه \"\n    \"متری» معین نیز دسیمتر و دکامتر را همین‌گونه به کار برده است. وام‌گیری از فرانسه که نورایی نشان داده درست است.\"),\n  sources=[AB_DOJIN, E_DOZEN, E_DECA],\n  ref_check=[\n    {\"ref\": \"MON:1572\", \"status\": \"partial\",\n     \"note\": \"The 6-volume Moʿin's page numbering is not mappable online and no scan of vol. 2 is available; the entries themselves were found in the 2-vol Adena abridgement (MON_part1.txt): 'دوجین: [فر.] (ق‌مر.) دوازده عدد از یک شیء، ستهٔ دوازده‌تایی' and, s.v. دستگاه متری, '۱ دسیمتر = ۱۰ سانتیمتر ... ۱ دکامتر = ۱۰ متر'. Content supports; the exact page could not be confirmed.\"},\n    {\"ref\": \"VOP:167\", \"status\": \"not_checked\",\n     \"note\": \"Moshiri, Farhang-e Vāžehā-ye Orupāyi dar Fārsi (1371/1992) — refs_online.json records that no copy of this book exists online or on disk (kind: none).\"}],\n  consulted=[\n    {\"src\": \"MON\", \"where\": \"s.v. دوجین; s.v. دستگاه متری (2-vol Adena abridgement)\", \"stance\": \"supports\",\n     \"note\": \"'دوجین: (ق‌مر.) دوازده عدد از یک شیء، ستهٔ دوازده تایی'; the metric table under دستگاه متری uses دسیمتر and دکامتر.\"},\n    {\"src\": \"BQT\", \"where\": \"grep of BQT_v1/v2_pages.txt for دوجین / دکامتر / دسیمتر\", \"stance\": \"silent\",\n     \"note\": \"None of the three occurs in Borhān-e Qāṭeʿ, as expected for 20th-century European loans.\"}])\n\nN(id=13, lang=\"English\",\n  words=\"deci-, decimal, dime, December, dozen\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"All five are Latin decem/decimus words that reached English by different roads: deci- and decimal are \"\n    \"learned formations on decimus (decimal via Medieval Latin decimalis, 17th c.); dime is Old French disme \"\n    \"'a tenth (part), tithe' < Latin decima, adopted for the US ten-cent coin in 1786; December is Latin December, \"\n    \"the tenth month of the old ten-month Roman calendar; dozen is Old French dozaine < doze < Latin duodecim. \"\n    \"Watkins files exactly this set under Latin decem.\"),\n  derivation_fa=(\n    \"هر پنج واژه از decem/decimus لاتینی‌اند اما از راه‌های گوناگون به انگلیسی رسیده‌اند: deci- و decimal ساخت‌های \"\n    \"دانشورانه بر پایهٔ decimus‌اند (decimal از راه لاتینی میانه decimalis در سدهٔ هفدهم)؛ dime از فرانسهٔ کهن disme \"\n    \"«یک‌دهم، عشریه» از decima لاتینی که در ۱۷۸۶ نام سکهٔ ده‌سنتی آمریکا شد؛ December همان December لاتینی، ماه دهمِ \"\n    \"گاهشمار کهن رومی؛ و dozen از dozaine فرانسهٔ کهن از doze از duodecim لاتینی. واتکینز نیز همین مجموعه را ذیل \"\n    \"decem لاتینی آورده است و ادعای نورایی درست است.\"),\n  sources=[E_DOZEN],\n  ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\",\n              \"note\": \"No reference on this box (confirmed on the page image); the parent Latin box's AHD:352 covers it.\"}],\n  consulted=[\n    {\"src\": \"AHD\", \"where\": \"s.v. dekm, I.2\", \"stance\": \"supports\",\n     \"note\": \"'Latin decem, ten: DECEMBER, DECEMVIR, DECI-, DECIMAL, DECIMATE, DECUPLE, DICKER, DIME; (DECENARY), DECENNIUM, DECUSSATE, DOZEN, DUODECIMAL, OCTODECIMO, SEXTODECIMO' — Nourai's list is a subset.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. denarius, denary (KLN_1966)\", \"stance\": \"supports\",\n     \"note\": \"'See ten and cp. decem-, decimal. Cp. also denary, denier, dinar' — Klein's own cross-reference net for this box.\"}])\n\nN(id=14, lang=\"Latin\",\n  words=\"děn-ârius : a silver coin worth ten bronze \\\"asses\\\".\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Latin dēnārius is the adjective 'containing ten' (from the distributive dēnī < *dek-noi < decem), used \"\n    \"elliptically for dēnārius nummus, the silver coin first struck c. 211 BCE at a tariff of ten bronze asses \"\n    \"(later sixteen). Klein states it in exactly these words. The chart's gloss 'a silver coin worth ten bronze \"\n    \"asses' is precisely right, and Moʿin's footnote in Borhān repeats it ('نقدی برابر ده آسی، چه در اول وضع آن از \"\n    \"نقره و مساوی ده آسِ as بود'). The trailing semicolon after 'AHD:352' is in the printed book.\"),\n  derivation_fa=(\n    \"dēnārius لاتینی در اصل صفت است به معنی «دربردارندهٔ ده» (از قید توزیعی dēnī از *dek-noi از decem) و به‌صورت \"\n    \"کوتاه‌شدهٔ dēnārius nummus به کار می‌رفت؛ سکهٔ نقره‌ای که نخستین بار حدود ۲۱۱ پیش از میلاد به ارزش ده «آسِ» \"\n    \"برنزی ضرب شد (بعدها شانزده آس). کلاین همین را می‌گوید و معین در حاشیهٔ برهان قاطع نیز می‌نویسد: «نقدی برابر ده \"\n    \"آسی، چه در اول وضع آن از نقره و مساوی ده آسِ as بود و آس از نقود مسین بود». تعریف نورایی کاملاً درست است.\"),\n  sources=[E_DINAR],\n  ref_check=[{\"ref\": \"AHD:352\", \"status\": \"supports\",\n              \"note\": \"The 1976 AHD body page is not open online; the same house's root list (Watkins 1985 s.v. dekm) has 'Irregular Latin distributive dēnī, by tens, ten each (formed by analogy with nōnī, nine each): (DENARIUS), DENARY, (DENIER)' — the derivation the box asserts.\"}],\n  consulted=[\n    {\"src\": \"KLN\", \"where\": \"s.v. denarius (KLN_1966, leaf 247 ≈ p.470)\", \"stance\": \"supports\",\n     \"note\": \"'denarius, n., an ancient Roman silver coin. — L. denarius, short for denarius nummus, \\\\'the coin containing ten (asses)\\\\', from denarius, \\\\'containing ten\\\\', and nummus, \\\\'coin\\\\'. ... The denarius was so called because it originally contained ten asses.'\"},\n    {\"src\": \"POK\", \"where\": \"p.191\", \"stance\": \"supports\",\n     \"note\": \"'lat. decem (denī \\\\'je zehn\\\\' aus *dek-noi)' — the dēnī from which dēnārius is formed.\"}])\n\nN(id=15, lang=\"Pahlavi\",\n  words=\"denâr : an old monetary unit\",\n  verdict=\"plausible\",\n  derivation=(\n    \"Middle Persian dēnār (Book Pahlavi ⟨dynʾl⟩) is well attested — MacKenzie: 'dēnār [dynʾl | N dīnār] (gold) \"\n    \"dinar' — and the coin-name is certainly the Latin dēnārius. What is disputable is the route Nourai draws, a \"\n    \"direct Latin → Pahlavi arrow. Moʿin's own footnote in Borhān (vol. 2, the دینار page, citing Tavadia p.91) \"\n    \"does say 'پهلوی dēnār ... از لاتینی dēnārius', so Nourai is following his source. Modern scholarship, \"\n    \"however, has the word reach Iran through the eastern Mediterranean koine: Wiktionary derives MP dēnār 'from \"\n    \"Ancient Greek δηνάριον, from Latin dēnārius, perhaps through Aramaic דֵּינָרָא / ܕܝܢܪܐ (dēnārā)', and the \"\n    \"Aramaic/Syriac form is what the Sasanian chancery would have met. Verdict: the Latin origin is certain, the \"\n    \"immediate donor probably Greek/Aramaic rather than Latin itself.\"),\n  derivation_fa=(\n    \"صورت فارسی میانهٔ dēnār (به خط پهلوی ⟨dynʾl⟩) به‌خوبی گواهی شده است — مکنزی: «dēnār [dynʾl | N dīnār] دینارِ \"\n    \"زر» — و بی‌گمان همان dēnārius لاتینی است. آنچه جای گفت‌وگو دارد پیکان مستقیمِ «لاتینی ← پهلوی» است. معین در \"\n    \"حاشیهٔ برهان قاطع (جلد ۲، مدخل دینار، به نقل از تاوادیا ص ۹۱) خود می‌نویسد «پهلوی dēnār ... از لاتینی \"\n    \"dēnārius»، پس نورایی پیرو منبع خویش است. اما پژوهش امروزی وام‌گیری را با میانجی می‌داند: ویکی‌واژه dēnār فارسی \"\n    \"میانه را «از یونانی δηνάριον، از لاتینی dēnārius، شاید از راه آرامی dēnārā» می‌گیرد. پس اصل لاتینی قطعی است، \"\n    \"ولی وام‌دهندهٔ بی‌واسطه به احتمال یونانی یا آرامی بوده است؛ ادعای نورایی با احتیاط پذیرفتنی است.\"),\n  sources=[W_DINAR],\n  ref_check=[{\"ref\": \"BQT:916\", \"status\": \"supports\",\n              \"note\": \"Borhān-e Qāṭeʿ vol. 2, the دینار leaf (BQT_v2_pages.txt leaf 376, printed ≈916–919), footnote 1: '۱ ـ پهلوی dēnār، تاوادیا ۹۱ ... از لاتینی dēnārius بتقدیر dēnārium بمعنی «نقدی برابر ده آسی» چه در اول وضع آن از نقره و مساوی ده آسِ as بود و آس از نقود مسین بود' — Moʿin asserts exactly Nourai's Latin > Pahlavi arrow.\"}],\n  consulted=[\n    {\"src\": \"PHD\", \"where\": \"s.v. dēnār\", \"stance\": \"supports\",\n     \"note\": \"MacKenzie: 'dēnār [dynʾl | N dīnār] (gold) dinar' — the Middle Persian word and its New Persian continuation, though MacKenzie gives no etymology.\"},\n    {\"src\": \"NYB\", \"where\": \"glossary, s.v. yākint (note)\", \"stance\": \"silent\",\n     \"note\": \"Nyberg's Manual of Pahlavi glossary has no dēnār entry; the spelling ⟨dynʾl⟩ appears only incidentally in his note on yākint suxr ('read swhl, not *dynʾl!!'), confirming the graph but saying nothing of the etymology.\"}])\n\nN(id=16, lang=\"Persian\",\n  words=\"dînâr «دینار» : an old monetary unit\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"MP dēnār > NP dīnār, with the regular Middle Persian ē > New Persian ī. In Islamic Iran دینار is the gold \"\n    \"coin (as against the silver درهم), and later a small money of account (10,000 dinars = 1 toman). Borhān \"\n    \"defines it 'زر سرخ را گویند ... همچو تمام' and Moʿin's footnote traces it to Pahlavi dēnār and Latin \"\n    \"dēnārius; Wiktionary's Persian entry gives the same chain, adding a possible Aramaic link. Nourai's arrow is \"\n    \"correct as drawn.\"),\n  derivation_fa=(\n    \"dēnār فارسی میانه با تبدیل قاعده‌مندِ ای کشیدهٔ پهلوی به ی، در فارسی نو «دینار» شده است. در ایرانِ دورهٔ اسلامی \"\n    \"دینار سکهٔ زر است در برابر درهمِ سیم، و بعدها واحد خُردِ محاسباتی شد (هر تومان ده هزار دینار). برهان قاطع آن را \"\n    \"«زر سرخ» تعریف می‌کند و معین در حاشیه آن را به پهلوی dēnār و لاتینی dēnārius بازمی‌گرداند؛ ویکی‌واژه نیز همین \"\n    \"زنجیره را با احتمال میانجی آرامی می‌آورد. ادعای نورایی درست است.\"),\n  sources=[W_DINAR],\n  ref_check=[{\"ref\": \"BQT:916\", \"status\": \"supports\",\n              \"note\": \"Same leaf (BQT_v2_pages.txt leaf 376): headword 'دینار = بر وزن بیمار، زر سرخ را گویند ...' with the etymological footnote quoted at node 15, plus Moʿin's cross-reference 'برای ارزش دینار، رک: دائرة المعارف اسلام؛ و ارزش دینار و تومان در قرون مختلفه، مقالات کسروی ج۱ ص۱۰۹'.\"}],\n  consulted=[\n    {\"src\": \"PHD\", \"where\": \"s.v. dēnār\", \"stance\": \"supports\",\n     \"note\": \"'dēnār [dynʾl | N dīnār] (gold) dinar' — MacKenzie explicitly equates the Middle and New Persian words.\"},\n    {\"src\": \"FVQ\", \"where\": \"p.133 s.v. دينار\", \"stance\": \"partial\",\n     \"note\": \"Jeffery reports that the Muslim philologists thought دينار Persian: 'al-Jawālīqī, Muʿarrab 62 ... gives it as Arabicized from the Pers.; but ath-Thaʿālibī, Fiqh 317, places it among the words which have the same form in both Arabic and Persian' — i.e. Persian and Arabic dīnār are the same borrowed word, not two independent ones.\"}])\n\nN(id=17, lang=\"Greek\",\n  words=\"děnârion\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Koine Greek δηνάριον is a straight Latin loan of the imperial period, the -άριον ending being the ordinary \"\n    \"Greek adaptation of Latin -ārius/-ārium; it is the coin of the Gospel tribute-money passages (Matt. 22:19, \"\n    \"Mark 12:15) and is ubiquitous in the Egyptian papyri, which is why it, and not Latin directly, was the form \"\n    \"the Near East knew. Etymonline: dinar is 'from Arabic dinar ... from late Greek denarion, from Latin \"\n    \"denarius'.\"),\n  derivation_fa=(\n    \"δηνάριον در یونانی کوینه وام‌واژه‌ای مستقیم از لاتینی دورهٔ امپراتوری است؛ پایانهٔ ‎-άριον شکل معمول یونانی‌سازیِ \"\n    \"‎-ārius/-ārium لاتینی است. این همان سکه‌ای است که در انجیل (متی ۲۲:۱۹ و مرقس ۱۲:۱۵) از آن سخن رفته و در \"\n    \"پاپیروس‌های مصری فراوان دیده می‌شود؛ ازاین‌رو خاور نزدیک این واژه را به صورت یونانی آن شناخت، نه یکسره از \"\n    \"لاتینی. اتیمانلاین نیز زنجیرهٔ «لاتینی dēnārius ← یونانی متأخر dēnárion ← عربی دینار» را می‌آورد. ادعای نورایی \"\n    \"درست است.\"),\n  sources=[E_DINAR],\n  ref_check=[{\"ref\": \"AHD:370\", \"status\": \"supports\",\n              \"note\": \"The 1976 AHD body page is not open online, but the AHD entry for 'dinar' quoted by every later edition gives 'Arabic dīnār, from Greek dēnarion, from Latin dēnārius' — the same chain, and Watkins s.v. dekm files DENARIUS/DENARY/DENIER under Latin dēnī.\"}],\n  consulted=[\n    {\"src\": \"KLN\", \"where\": \"s.v. dinar (KLN_1966, leaf 247 ≈ p.470)\", \"stance\": \"supports\",\n     \"note\": \"'dinar, n. — Arab. dīnār, fr. Late Gk. δηνάριον, fr. L. denarius. See denarius and cp. denier.'\"},\n    {\"src\": \"FVQ\", \"where\": \"p.133 s.v. دينار\", \"stance\": \"supports\",\n     \"note\": \"Jeffery: 'The name of a coin, the Lat. denarius, Gk. δηνάριον.'\"}])\n\nN(id=18, lang=\"Arabic\",\n  words=\"dînâr\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"Arabic دينار dīnār is a pre-Islamic borrowing of Greek δηνάριον (probably through Aramaic/Syriac dēnārā, \"\n    \"which is the shape actually current in the Fertile Crescent); it occurs in the Qurʾān at 3:75 and in early \"\n    \"poetry, and became the name of the gold coin of the Umayyad reform of 77 AH/696 CE. The Arab philologists \"\n    \"themselves were unsure: Jeffery records that al-Jawālīqī called it Arabicized from Persian, ath-Thaʿālibī \"\n    \"said it had the same form in both languages, and al-Rāghib repeats a folk etymology compounding it out of \"\n    \"دين + آر. The Latin>Greek>Arabic route Nourai draws is the standard one.\"),\n  derivation_fa=(\n    \"«دینار» عربی وام‌واژه‌ای پیش از اسلام از δηνάριον یونانی است، به احتمال از راه آرامی/سریانی dēnārā که صورت \"\n    \"رایج در هلال حاصلخیز بود؛ در قرآن (آل‌عمران ۷۵) و شعر کهن عربی دیده می‌شود و پس از اصلاح ضرب سکهٔ عبدالملک در \"\n    \"۷۷ هجری نام سکهٔ زر شد. زبان‌شناسان عرب خود در آن تردید داشتند: جفری نقل می‌کند که جوالیقی آن را معرّبِ فارسی \"\n    \"دانسته، ثعالبی گفته در هر دو زبان یک صورت دارد، و راغب ریشه‌شناسی عامیانه‌ای از «دین + آر» آورده است. مسیر \"\n    \"لاتینی ← یونانی ← عربی که نورایی کشیده همان دیدگاه معیار است.\"),\n  sources=[E_DINAR],\n  ref_check=[{\"ref\": \"AHD:370\", \"status\": \"supports\",\n              \"note\": \"Same AHD 'dinar' entry: 'Arabic dīnār, from Greek dēnarion, from Latin dēnārius'; the 1976 page itself is not open online.\"}],\n  consulted=[\n    {\"src\": \"FVQ\", \"where\": \"p.133 (FVQ_pages.txt leaf 150) s.v. دينار\", \"stance\": \"supports\",\n     \"note\": \"Jeffery, Foreign Vocabulary of the Qurʾān, p.133: 'دينار (Dinar). iii,68. A dinar. The name of a coin, the Lat. denarius, Gk. δηνάριον. The Muslim authorities knew that it was a loan-word and claim that it came from Persian, though they were not unanimous about it. al-Jawālīqī, Muʿarrab 62 ... ath-Thaʿālibī, Fiqh 317 ... Rāghib, Mufradāt 171 ... quoting the theory that it is of Pers. origin compounded from دين and آر'.\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. dinar (KLN_1966)\", \"stance\": \"supports\",\n     \"note\": \"'dinar, n. — Arab. dīnār, fr. Late Gk. δηνάριον, fr. L. denarius.'\"},\n    {\"src\": \"LKT\", \"where\": \"grep for 'dinar'\", \"stance\": \"silent\",\n     \"note\": \"Lokotsch's Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs (LKT.txt) returns no hit for dinar in the OCR.\"}])\n\nN(id=19, lang=\"English\",\n  words=\"Dinar\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"English dinar is a 17th-century travellers'/orientalists' borrowing of Arabic dīnār, first recorded in the \"\n    \"1630s as the name of Arab gold coins; it was revived in the 20th century as the official currency name of \"\n    \"Iraq, Jordan, Kuwait, Algeria, Tunisia, Serbia and others. Etymonline: 'Middle Eastern unit of currency; \"\n    \"generic name of Arab gold coins, 1630s, from Arabic dinar, originally the name of a gold coin issued by the \"\n    \"caliphs of Damascus, from late Greek denarion, from Latin denarius.'\"),\n  derivation_fa=(\n    \"«dinar» انگلیسی وام‌واژه‌ای از دینار عربی است که در دههٔ ۱۶۳۰ میلادی از راه سفرنامه‌ها و خاورشناسان به انگلیسی \"\n    \"راه یافت و نام عمومی سکه‌های زرِ عربی بود؛ در سدهٔ بیستم دوباره به‌عنوان نام رسمی پول عراق، اردن، کویت، الجزایر، \"\n    \"تونس و صربستان زنده شد. اتیمانلاین: «۱۶۳۰م، از دینارِ عربی ... از dēnárion یونانی متأخر، از dēnārius لاتینی». \"\n    \"ادعای نورایی درست است.\"),\n  sources=[E_DINAR],\n  ref_check=[\n    {\"ref\": \"AHD:370\", \"status\": \"supports\",\n     \"note\": \"AHD's 'dinar' entry (page of the 1976 edition not open online) gives Arabic > Greek > Latin, exactly this chain.\"},\n    {\"ref\": \"KLN:450\", \"status\": \"supports\",\n     \"note\": \"Klein does have the entry — KLN_1966.txt, leaf 247 (≈ printed p.470 by the file's leaf/page formula, some 20 pages off Nourai's '450'): 'dinar, n. — Arab. dīnār, fr. Late Gk. δηνάριον, fr. L. denarius. See denarius and cp. denier.' The content is exactly what the arrow claims; only the page number is doubtful.\"}],\n  consulted=[\n    {\"src\": \"KLN\", \"where\": \"s.v. dinar, denarius, denier (KLN_1966 leaf 247)\", \"stance\": \"supports\",\n     \"note\": \"The three entries stand together and cross-refer: denarius 'See ten and cp. decem-, decimal. Cp. also denary, denier, dinar.'\"},\n    {\"src\": \"SKT\", \"where\": \"grep for 'dinar'\", \"stance\": \"silent\",\n     \"note\": \"Skeat's Concise Etymological Dictionary has no entry for dinar (it is not a core English word).\"}])\n\nN(id=20, lang=\"Greek\",\n  words=\"deka : ten\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"PIE *deḱm̥ > Proto-Hellenic *dékə > Greek δέκα, with the syllabic *m̥ vocalised as -a; the derived δεκάς, \"\n    \"-άδος 'a group of ten, decade' underlies the English word. Pokorny lists gr. δέκα in the head material of \"\n    \"the entry and δεκάς among the *dekm̥-t(i) formations.\"),\n  derivation_fa=(\n    \"*deḱm̥ هندواروپایی از راه هلنی آغازین *dékə به δέκα یونانی رسیده و *m̥ هجایی به ‎-a بدل شده است؛ مشتق آن \"\n    \"δεκάς، ‎-άδος «دسته‌ای ده‌تایی» است که واژهٔ انگلیسی decade از آن می‌آید. پوکورنی δέκα را در سرآغاز مدخل و \"\n    \"δεκάς را در میان ساخت‌های *dekm̥-t(i) آورده است. ادعای نورایی درست است.\"),\n  sources=[W_PIE],\n  ref_check=[{\"ref\": \"AHD\", \"status\": \"supports\",\n              \"note\": \"Watkins s.v. dekm: '4. Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON.'\"}],\n  consulted=[\n    {\"src\": \"POK\", \"where\": \"p.191/192\", \"stance\": \"supports\",\n     \"note\": \"'gr. δέκα' in the material of dekm̥, and 'gr. δεκάς, -άδος' among the reflexes of the substantive dekm̥-t(i).\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.785\", \"stance\": \"supports\",\n     \"note\": \"'Ai. daśa, av. dasa, gr. δέκα, lat. decem ...'.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. dekm\", \"stance\": \"supports\",\n     \"note\": \"Mann: 'Gk. déka; dekáte'.\"}])\n\nN(id=21, lang=\"English\",\n  words=\"deca-, decade\",\n  verdict=\"confirmed\",\n  derivation=(\n    \"deca- is the combining form of Greek δέκα, latinised and adopted as the metric multiplier prefix in 1795 \"\n    \"(decametre, decalitre). decade comes from Greek δεκάς, -άδος 'group of ten' through Late Latin decas/decad- \"\n    \"and Middle French décade (15th c.); in English it first meant 'a division of ten books' (of Livy) and only \"\n    \"from the 17th century 'a period of ten years'. Watkins files both under 'Greek deka'.\"),\n  derivation_fa=(\n    \"«deca-» صورت ترکیبی δέκα یونانی است که در ۱۷۹۵ به‌عنوان پیشوند مضربِ نظام متری لاتینی‌نویسی و پذیرفته شد \"\n    \"(decametre، decalitre). «decade» از δεκάς، ‎-άδος یونانی «دستهٔ ده‌تایی» از راه لاتینی متأخر decas/decad- و \"\n    \"فرانسهٔ میانهٔ décade (سدهٔ پانزدهم) آمده است؛ در انگلیسی نخست به معنی «بخشِ ده‌کتابیِ» تاریخ لیویوس بود و تنها \"\n    \"از سدهٔ هفدهم معنی «دههٔ ده‌ساله» یافت. واتکینز هر دو را ذیل «deka یونانی» آورده است.\"),\n  sources=[E_DECA],\n  ref_check=[{\"ref\": \"None\", \"status\": \"not_checked\",\n              \"note\": \"No reference on this box (confirmed on the page image); the parent Greek box's 'AHD' covers it.\"}],\n  consulted=[\n    {\"src\": \"AHD\", \"where\": \"s.v. dekm, I.4\", \"stance\": \"supports\",\n     \"note\": \"'Greek deka, ten: DEAN, DECA-, DECADE, (DECANAL), (DOYEN); DECAGON, DODECAGON.'\"},\n    {\"src\": \"KLN\", \"where\": \"s.v. decade/deca- (KLN_1966)\", \"stance\": \"supports\",\n     \"note\": \"Klein's d- section treats deca- as the combining form of Gk. δέκα and decade as fr. Gk. δεκάς, gen. δεκάδος, via L. decas, gen. decadis.\"}])\n\nentry = {\n  \"entry\": 0,\n  \"root\": \"Dekm\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *deḱm̥ 'ten'\",\n  \"note\": (\"Pokorny IEW 191 'dekm̥, dekm̥-t, deku- ,zehn'; Watkins/AHD 'dekm. Ten. [Pok. dekm 191]'; \"\n           \"Walde-Pokorny I 785 'dekm̥ ,zehn''. The reconstruction, the language label ('Indo-European') and the \"\n           \"gloss are all correct; the modern notation is *deḱm̥ (uninflected). The page is a well-built chart: \"\n           \"the three Iranian boxes correctly separate the three ways Iranian expresses 'ten' (the free numeral \"\n           \"dasa in 11-19, the -sat-/-saiti- suffix in 20-50, the -ti-/-āiti- suffix in 60-90), which is exactly \"\n           \"Buck's and Pokorny's analysis. Two problems: (a) node #2 prints two malformed Pahlavi numerals \"\n           \"('sîkdah', 'navasdah' for sîcdah/navâcdah) — the page image shows they are the book's own misprints; \"\n           \"(b) node #11 files French 'deca' under Latin, whereas the metric prefix déca- was deliberately taken \"\n           \"from Greek deka in 1795 and belongs under node #20. One extraction error: the French box (#11) carries \"\n           \"the reference 'AHD' on the printed page but refs=null in the JSON.\"),\n  \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *deḱm̥ «ده»؛ پوکورنی (ص ۱۹۱) آن را «dekm̥, dekm̥-t, deku- ,zehn'» آورده، \"\n              \"واتکینز در فهرست ریشه‌های آمریکن هریتیج «dekm. Ten. [Pok. dekm 191]» و والده-پوکورنی (ج۱ ص۷۸۵) \"\n              \"«dekm̥ ,zehn'». بازسازی، برچسب زبانی و معنا هر سه درست است. ساختار نمودار نیز سنجیده است: سه جعبهٔ \"\n              \"ایرانی به‌درستی سه شیوهٔ بیان «ده» را از هم جدا کرده‌اند — عددِ آزادِ dasa در ۱۱ تا ۱۹، پسوند \"\n              \"‎-sat-/-saiti- در ۲۰ تا ۵۰، و پسوند ‎-ti-/-āiti- در ۶۰ تا ۹۰ — و این همان تحلیل باک و پوکورنی است. \"\n              \"دو ایراد: نخست، در جعبهٔ پهلوی دو صورت «sîkdah» و «navasdah» غلط چاپی خودِ کتاب‌اند (درست: sîcdah و \"\n              \"navâcdah)؛ دوم، «deca» فرانسوی زیر لاتین نشسته حال آنکه پیشوند متریِ déca- در ۱۷۹۵ آگاهانه از deka \"\n              \"یونانی گرفته شده و جای آن ذیل جعبهٔ یونانی است. یک خطای خوانش اسکن نیز هست: جعبهٔ فرانسه در چاپ \"\n              \"ارجاع «AHD» دارد ولی در داده‌ها بی‌ارجاع ثبت شده است.\"),\n  \"sources\": [W_PIE],\n  \"ref_check\": [POK],\n  \"consulted\": [\n    {\"src\": \"WLD\", \"where\": \"Bd. I p.785 (WLD_Bd1_pages.txt, form-feed leaf 793, header '785')\", \"stance\": \"supports\",\n     \"note\": \"'dekm̥ ,zehn'. Ai. daśa, av. dasa, gr. δέκα, lat. decem, umbr. desen-(duf) ,(duo-)decim', air. deich, ... got. taihun ..., ags. tien, tyn, ahd. zehan, as. tehan, tian ... arm. tasn'; and on p.786 'idg. *ḱm̥tóm ,hundert' aus **(d)ḱm̥tom'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. dekm\", \"stance\": \"supports\",\n     \"note\": \"'dekm. Ten. I. Basic form *dekm. 1. Germanic *tehun ... 2. Latin decem ... 4. Greek deka ... [Pok. dekm 191.]' — same root, same page reference to Pokorny that Nourai gives.\"},\n    {\"src\": \"IEC\", \"where\": \"s.v. dekm, dekmti\", \"stance\": \"supports\",\n     \"note\": \"Mann: 'dekm, dekmti \\\\'ten\\\\'; dekmtis \\\\'tensome, ten-group\\\\'. WP I,785 Sk. daśan ...; Gk. déka; Av. dasa; Per. dah; Oss. dás; Arm. tasn; ... Lat. decem ...; Go. taíhun ...; OE ten'.\"},\n    {\"src\": \"SYN\", \"where\": \"§13.31 Note on the numerals, p.936\", \"stance\": \"supports\",\n     \"note\": \"Buck: 'the IE words for \\\\'one\\\\' to \\\\'ten\\\\' have persisted everywhere with only slight changes other than phonetic ... The \\\\'teens\\\\' are expressed by cop. cpds. of the digits with \\\\'ten\\\\'' — the architecture of the whole chart.\"},\n    {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt / ARY_pages.txt pdf page 292 (printed ≈293), entry ده\", \"stance\": \"supports\",\n     \"note\": \"Aryanpur's cognate list for ده: 'DASA, DACHA, DACA (SANSKRIT), TASN (ARMENIAN), DEKA (GREEK), DECEM (LATIN), DIX (FRENCH), TAIHUN (GOTHIC), SAK (TOKHARIAN A/B), DESETI (OLD CHURCH SLAVIC), DEICH (OLD IRISH), DEG (WELSH)' — an independent modern Persian cross-check of the same root.\"}],\n  \"nodes\": nodes,\n}\n\nout = {\n  \"pdf_page\": 114,\n  \"book_page\": 84,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry],\n}\n\nimport io\nwith io.open('/home/sfmqrb/git/rishe/data/verification/page-114.json','w',encoding='utf-8') as f:\n    json.dump(out,f,ensure_ascii=False,indent=2)\n    f.write('\\n')\nprint('written')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk114.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-114.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 114"
}
```


### [2026-09-05T18:01:11.072Z] TOOL RESULT

```
written
JSON OK
nodes verified: 21/21
node verdicts: {'plausible': 3, 'transcription_suspect': 1, 'confirmed': 17}
root verdicts: {'confirmed': 1}
ref checks: {'supports': 19, 'not_checked': 6, 'partial': 3}
books consulted: {'supports': 42, 'partial': 5, 'silent': 4} | by book: {'KLN': 9, 'PHD': 6, 'BRT': 5, 'HRN': 5, 'WLD': 4, 'AHD': 4, 'IEC': 3, 'POK': 3, 'FVQ': 3, 'SYN': 2, 'KNT': 1, 'HUB': 1, 'MON': 1, 'BQT': 1, 'NYB': 1, 'LKT': 1, 'SKT': 1}
```


## [2026-09-05T18:01:17.548Z] TOOL CALL #78: Bash

```json
{
 "command": "file data/verification/page-114.json && head -c 20 data/verification/page-114.json | xxd | head -2 && git status --short | head"
}
```


### [2026-09-05T18:01:19.569Z] TOOL RESULT

```
data/verification/page-114.json: JSON text data
00000000: 7b0a 2020 2270 6466 5f70 6167 6522 3a20  {.  "pdf_page": 
00000010: 3131 342c                                114,
?? data/verification/page-114.json
```


## [2026-09-05T18:01:24.002Z] TOOL CALL #79: Bash

```json
{
 "command": "git status --short"
}
```


### [2026-09-05T18:01:24.058Z] TOOL RESULT

```
?? data/verification/page-114.json
```


## [2026-09-05T18:01:29.705Z] TOOL CALL #80: Bash

```json
{
 "command": "git check-ignore -v data/verification/sources/web/00ce8741315d1238.txt data/verification/sources/refs/ocr/BOOK/114.png 2>&1 | head; git log --oneline -1"
}
```


### [2026-09-05T18:01:31.346Z] TOOL RESULT

```
.gitignore:9:data/verification/sources/refs/	data/verification/sources/refs/ocr/BOOK/114.png
e6b6164 Verify page 113 (Dek/doctor, Deks/dexter, dakhsh)
```


## [2026-09-05T18:01:36.840Z] TOOL CALL #81: Bash

```json
{
 "command": "ls -la data/verification/sources/web/00ce8741315d1238.txt data/verification/sources/web/e5a97269f3eb4af5.txt 2>&1; git check-ignore -v data/verification/sources/web/ | head -2"
}
```


### [2026-09-05T18:01:38.524Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 7407 Sep  5 13:54 data/verification/sources/web/00ce8741315d1238.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 5562 Sep  5 13:51 data/verification/sources/web/e5a97269f3eb4af5.txt
```


## [2026-09-05T18:01:58.634Z] AGENT

Page 114 (book page 84) verified. `/home/sfmqrb/git/rishe/data/verification/page-114.json` written; `verify_check.py 114` reports 21/21 nodes, 0 PROBLEM lines.

**Counts** — root: 1 confirmed. Nodes: 17 confirmed, 3 plausible, 1 transcription_suspect. Ref checks: 19 supports / 3 partial / 6 not_checked. Books consulted: 42 supports / 5 partial / 4 silent (POK, WLD, AHD-Watkins, IEC, SYN, BRT, KNT, HRN, HUB, PHD, NYB, KLN, SKT, FVQ, LKT, BQT, MON, ARY).

**transcription_suspect**
- Dekm, node #2 [Pahlavi] — `sîkdah` "thirteen" and `navasdah` "nineteen". Horn nos. 763/1048 give Phl. *sicdahum* / *navācdahum*, Bartholomae "Pü.: navazdahum", MacKenzie "thirteen sēzdah"; Nourai's ⟨c⟩ = /z/ elsewhere in the box (yâcdah, šâncdah). `error_in: book` — the 300 dpi page image shows the book itself prints sîkdah and navasdah. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/114.png`.

**plausible (no disputed items)**
- #1 [Av./OP] — forms are Avestan; Old Persian cardinals above "nine" are unattested (Kent has only *navama-*), and the teens are attested in the Avesta chiefly as ordinals.
- #11 [French] — `douzaine` and `deci` are correctly from Latin, but metric `déca-` was taken from Greek *deka* in 1795 (AHD itself files DECA- under Greek), so it hangs from the wrong parent; it belongs under node #20.
- #15 [Pahlavi denâr] — Latin origin certain, but modern scholarship (Wiktionary) routes MP *dēnār* via Greek δηνάριον / Aramaic *dēnārā*, not straight from Latin. Nourai follows Moʿin's Borhān footnote, which does assert the direct Latin route.

**Extraction error for the owner to fix**
- Node #11 (French box, `decem`→`deca/deci/douzaine`): the printed page shows the reference **AHD**; `data/extracted/batch/page-114.json` has `"refs": null`. (Node #14's odd `"AHD:352;"` with trailing semicolon is faithful — the book prints it that way.)

Key ref confirmations: POK:191 verified verbatim (POK_01 leaf 202); GPL:41 is exactly Platts's cardinal-numeral table with all the Av./"O.P." and Pahlavi forms Nourai copies; BQT:916 located at BQT_v2 leaf 376 (printed ≈916–919) with Moʿin's footnote "پهلوی dēnār … از لاتینی dēnārius"; KLN:450 content found but at leaf 247 ≈ printed p.470 of the 1966 two-volume edition (~20 pages off Nourai's number). VOP:167 unavailable (no copy exists anywhere); AHD:352/370 are 1976-edition body pages that are not open online, checked against the Watkins 1985 root list instead.
