# Verification process log — verify-page-96


## [2026-09-05T14:11:32.053Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 96 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-96.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-96.json. Write /home/sfmqrb/git/rishe/data/verification/page-96.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 96` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T14:11:33.968Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T14:11:34.673Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T14:11:34.690Z] TOOL RESULT

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


## [2026-09-05T14:11:34.870Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-96.txt"
}
```


### [2026-09-05T14:11:34.898Z] TOOL RESULT

```
1	=== PDF page 96 (book page 66) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Bhili, Bhilo : good, friendly, loving  (refs POK:153)
4	#1 (parent #0) [Greek] refs=POK:154 | philos : love
5	  #2 (parent #1) [Greek] refs=AHD; KLN | philo-sophos : fond of wisdom ☞Sophos
6	    #3 (parent #2) [Arabic] refs=TAD:53 | falsafah
7	      #4 (parent #3) [Persian] refs=MON:2567 | falsafeh «فلسفه» : philosophy | extra: فیلسوف ، فلاسفه
8	    #5 (parent #2) [Latin] refs=AHD | 
9	      #6 (parent #5) [French] refs=AHD | 
10	        #7 (parent #6) [English] refs=AHD | philosophy
11	  #8 (parent #1) [Greek] refs=AHD; KLN | philo-armonica : fond of music ☞Ar ; philo-hippos : fond of horses ☞Ekwos ; philo-adelphos : fond of brother ☞Gwelbh
12	    #9 (parent #8) [Latin] refs=None | 
13	      #10 (parent #9) [French] refs=AHD | 
14	        #11 (parent #10) [Persian] refs=VOP:257 |  | extra: فیلارمونیک ، فیلیپ
15	        #12 (parent #10) [English] refs=AHD | Philadelphia ; Philip ; philharmonic
16	          #13 (parent #12) [Persian] refs=MON | Fîlâdelfîyâ «فیلادلفیا»
17	  #14 (parent #1) [Greek] refs=AHD; KLN | sŭs-philos : friend of swine (shepherd's name) ☞Su 2
18	    #15 (parent #14) [Latin] refs=None | 
19	      #16 (parent #15) [French] refs=AHD:1306; KLN:1561 | Syphilis : name of a shepherd in a poem by a physician (1530) who was the victim of a disease that was later named after his poem hero, Syphilis.
20	        #17 (parent #16) [Persian] refs=MON | sîfîlîs «سیفیلیس» ; seflîs «سفلیس»
21	        #18 (parent #16) [English] refs=AHD | syphilis
22	  #19 (parent #1) [Greek] refs=AHD; KLN | philo-anthôpos : fond of people ☞Ner 1 ; philo-logos : fond of reasoning
23	    #20 (parent #19) [Latin] refs=None | 
24	      #21 (parent #20) [French] refs=None | 
25	        #22 (parent #21) [English] refs=None | philanthropy ; philology
26	--- entry 1 ---
27	ROOT Bhilo -> redirect to Bhili
28	--- entry 2 ---
29	ROOT Bhlei -> redirect to Bhel
30	--- entry 3 ---
31	ROOT Bhleu -> redirect to Bhel
32	--- entry 4 ---
33	ROOT Bhleu -> redirect to Bhel
34	--- entry 5 ---
35	ROOT Bho -> redirect to Bhě
36	
```


## [2026-09-05T14:11:39.490Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-96.json | head -200",
 "description": "Read source JSON for page 96"
}
```


## [2026-09-05T14:11:40.510Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-05T14:11:41.104Z] TOOL RESULT

```
{
    "pdf_page": 96,
    "book_page": 66,
    "entries": [
        {
            "root": {
                "name": "Bhili, Bhilo",
                "lang": "Indo-European",
                "refs": "POK:153",
                "gloss": "good, friendly, loving",
                "note": "SYN:1110 claims this is an Anatolian word"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": "POK:154",
                    "words": [
                        {
                            "translit": "philos",
                            "gloss": "love",
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
                    "refs": "AHD; KLN",
                    "words": [
                        {
                            "translit": "philo-sophos",
                            "gloss": "fond of wisdom",
                            "script": null,
                            "see": [
                                "Sophos"
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
                    "lang": "Arabic",
                    "refs": "TAD:53",
                    "words": [
                        {
                            "translit": "falsafah",
                            "gloss": null,
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
                    "lang": "Persian",
                    "refs": "MON:2567",
                    "words": [
                        {
                            "translit": "falsafeh",
                            "gloss": "philosophy",
                            "script": "\u0641\u0644\u0633\u0641\u0647"
                        }
                    ],
                    "script_extra": "\u0641\u06cc\u0644\u0633\u0648\u0641 \u060c \u0641\u0644\u0627\u0633\u0641\u0647",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 5,
                    "parent": 2,
                    "lang": "Latin",
                    "refs": "AHD",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 5,
                    "lang": "French",
                    "refs": "AHD",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 7,
                    "parent": 6,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "philosophy",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 1,
                    "lang": "Greek",
                    "refs": "AHD; KLN",
                    "words": [
                        {
                            "translit": "philo-armonica",
                            "gloss": "fond of music",
                            "script": null,
                            "see": [
                                "Ar"
                            ]
                        },
                        {
                            "translit": "philo-hippos",
                            "gloss": "fond of horses",
                            "script": null,
                            "see": [
                                "Ekwos"
                            ]
                        },
                        {
                            "translit": "philo-adelphos",
                            "gloss": "fond of brother",
                            "script": null,
                            "see": [
                                "Gwelbh"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 8,
                    "lang": "Latin",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "French",
                    "refs": "AHD",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "Persian",
                    "refs": "VOP:257",
                    "words": [],
                    "script_extra": "\u0641\u06cc\u0644\u0627\u0631\u0645\u0648\u0646\u06cc\u06a9 \u060c \u0641\u06cc\u0644\u06cc\u067e",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 12,
                    "parent": 10,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "Philadelphia",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "Philip",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "philharmonic",
                            "gloss": null,
```


### [2026-09-05T14:11:41.137Z] TOOL RESULT

```
agent
page-101.json
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
page-67.json
page-68.json
page-69.json
page-70.json
page-71.json
page-72.json
page-73.json
page-74.json
page-75.json
----
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


## [2026-09-05T14:11:44.898Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-96.json | sed -n '200,400p'",
 "description": "Rest of source JSON"
}
```


## [2026-09-05T14:11:45.623Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/page-9*.json data/verification/page-8*.json 2>/dev/null; echo ---; cat tools/verify_check.py | head -80",
 "description": "Check nearby verified pages and checker"
}
```


### [2026-09-05T14:11:46.535Z] TOOL RESULT

```
                            "gloss": null,
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
                    "lang": "Persian",
                    "refs": "MON",
                    "words": [
                        {
                            "translit": "F\u00eel\u00e2delf\u00eey\u00e2",
                            "gloss": null,
                            "script": "\u0641\u06cc\u0644\u0627\u062f\u0644\u0641\u06cc\u0627"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 1,
                    "lang": "Greek",
                    "refs": "AHD; KLN",
                    "words": [
                        {
                            "translit": "s\u016ds-philos",
                            "gloss": "friend of swine (shepherd's name)",
                            "script": null,
                            "see": [
                                "Su 2"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 14,
                    "lang": "Latin",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 16,
                    "parent": 15,
                    "lang": "French",
                    "refs": "AHD:1306; KLN:1561",
                    "words": [
                        {
                            "translit": "Syphilis",
                            "gloss": "name of a shepherd in a poem by a physician (1530) who was the victim of a disease that was later named after his poem hero, Syphilis.",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 17,
                    "parent": 16,
                    "lang": "Persian",
                    "refs": "MON",
                    "words": [
                        {
                            "translit": "s\u00eef\u00eel\u00ees",
                            "gloss": null,
                            "script": "\u0633\u06cc\u0641\u06cc\u0644\u06cc\u0633"
                        },
                        {
                            "translit": "sefl\u00ees",
                            "gloss": null,
                            "script": "\u0633\u0641\u0644\u06cc\u0633"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 18,
                    "parent": 16,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "syphilis",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 19,
                    "parent": 1,
                    "lang": "Greek",
                    "refs": "AHD; KLN",
                    "words": [
                        {
                            "translit": "philo-anth\u00f4pos",
                            "gloss": "fond of people",
                            "script": null,
                            "see": [
                                "Ner 1"
                            ]
                        },
                        {
                            "translit": "philo-logos",
                            "gloss": "fond of reasoning",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 20,
                    "parent": 19,
                    "lang": "Latin",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 21,
                    "parent": 20,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 22,
                    "parent": 21,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "philanthropy",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "philology",
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
                "name": "Bhilo",
                "redirect": "Bhili"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhlei",
                "redirect": "Bhel"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhleu",
                "redirect": "Bhel"
            },
            "nodes": []
        },
        {
            "root": {
                "name": "Bhleu",
                "redirect": "Bhel"
            },
            "nodes": []
        },
```


### [2026-09-05T14:11:46.569Z] TOOL RESULT

```
data/verification/page-80.json
data/verification/page-81.json
data/verification/page-82.json
data/verification/page-83.json
data/verification/page-84.json
data/verification/page-85.json
data/verification/page-86.json
data/verification/page-87.json
data/verification/page-88.json
data/verification/page-89.json
data/verification/page-90.json
data/verification/page-91.json
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


## [2026-09-05T14:11:49.507Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n '80,200p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check.py"
}
```


### [2026-09-05T14:11:49.542Z] TOOL RESULT

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


## [2026-09-05T14:11:50.388Z] TOOL CALL #8: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-91.json'))\nprint(json.dumps(d['entries'][0], ensure_ascii=False, indent=1)[:4000])\n\"",
 "description": "Sample recent verified page"
}
```


### [2026-09-05T14:11:52.376Z] TOOL RESULT

```
{
 "entry": 0,
 "root": "Bher 5, Bheru, Bhereu, Bhreu, Bhru 2",
 "verdict": "confirmed",
 "modern_form": "PIE *bʰer- 'to boil, seethe, well up' with its u-extension *bʰrewh₁- / *bʰer(e)u- 'to boil, brew'",
 "note": "Nourai's five variant names correspond exactly to the two Pokorny lemmata he cites: IEW 132-133 '2. bher- etwa \"aufwallen\", von quellendem oder siedendem Wasser (auch vom Aufbrausen beim Gähren, Kochen, sowie vom Feuer) \"sich heftig bewegen\"; oft mit u-Formans', and IEW 143-145 'bh(e)reu- : bh(e)rū-, Erw. von 2. bher-, \"sich heftig bewegen, wallen, bes. vom Aufbrausen beim Gären, Brauen, Kochen usw.\"' — so 'Bher 5' = Pokorny's bher-2, 'Bheru/Bhereu/Bhreu/Bhru 2' = his bh(e)reu- : bh(e)rū-. Watkins (AHD) fuses them into one entry, bhreu-2 'To boil, bubble, effervesce, burn; with derivatives referring to cooking and brewing. [Pok. bh(e)reu- 143, 2. bher- 132]'. Wiktionary reconstructs *bʰrewh₁- 'to boil, to brew', explicitly 'Extension of *bʰer- (to boil)'. Language label (Indo-European) and gloss ('to boil, bubble') are both right; only the numbering is Nourai's own.",
 "note_fa": "ریشهٔ هندواروپایی آغازین *bʰer- «جوشیدن، فوران کردن» و گسترش «واوی» آن *bʰrewh₁- (نوشتار کهن‌تر: bh(e)reu-) «جوشیدن، آبجو پختن». آنچه نورایی زیر پنج نامِ Bher 5، Bheru، Bhereu، Bhreu و Bhru 2 آورده، همان دو مدخل پوکورنی است: bher-2 در صفحهٔ ۱۳۲–۱۳۳ و bh(e)reu- : bh(e)rū- در صفحهٔ ۱۴۳–۱۴۵؛ واتکینز در پیوست فرهنگ American Heritage این دو را در یک مدخل bhreu-2 «جوشیدن، حباب زدن، سوختن» یکی کرده است. برچسب زبانی و معنای ریشه هر دو درست است و ادعای نورایی در این حد پذیرفتنی است.",
 "sources": [
  "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/b%CA%B0rewh%E2%82%81-"
 ],
 "ref_check": [
  {
   "ref": "AHD:1510",
   "status": "supports",
   "note": "Content verified in the local Watkins text (AHD_watkins1985.txt) s.v. bhreu-2: 'To boil, bubble, effervesce, burn; with derivatives referring to cooking and brewing … [Pok. bh(e)reu- 143, 2. bher- 132.]' — the same appendix Nourai cites. p.1510 falls inside the 1975 New College appendix range (pp.1505-1550, bh- section); the local copy is the 1985 standalone reprint, so the exact page number itself could not be re-checked."
  },
  {
   "ref": "POK:132",
   "status": "supports",
   "note": "POK_01.txt leaf 140 (= printed p.132-133): '2. bher- etwa \"auf wallen\", von quellendem oder siedendem Wasser … oft mit u-Formans; auch als schwere Basis bhers-'. Exactly Nourai's gloss."
  },
  {
   "ref": "POK:143",
   "status": "supports",
   "note": "POK_01.txt leaf 151-152 (= printed p.143-145): 'bh(e)reu- : bh(e)rū-, Erw. von 2. bher- \"sich heftig bewegen, wallen, bes. vom Aufbrausen beim Gären, Brauen, Kochen usw.\"'"
  },
  {
   "ref": "IEC:116",
   "status": "supports",
   "note": "IEC.txt leaf 78 (= printed p.116) carries the cross-reference lemma '(bhru-, see bheru-. Z-gde radical in Per. balwà \"tumult\"; OE brymm, m. \"surf, sea\", prob. also in MHG brunne \"spring\"; ON brunnr, id.)'. Mann's bheru- is Nourai's 'Bheru'."
  }
 ],
 "consulted": [
  {
   "src": "POK",
   "where": "IEW 132-133 and 143-145",
   "stance": "supports",
   "note": "Both lemmata present, with fermentum, ferveo, brinnan, brauen, Brot, defrutum all gathered under them."
  },
  {
   "src": "WLD",
   "where": "Bd. II p.167-168",
   "stance": "supports",
   "note": "'bhereu- : bheru- : bhreu- : bhru- Erw. von bher- \"sich heftig bewegen, wallen, bes. vom Aufbrausen beim Gahren, Brauen, Kochen usw.\"' — the direct forerunner of Pokorny's article."
  },
  {
   "src": "AHD",
   "where": "Watkins, s.v. bhreu-2",
   "stance": "supports",
   "note": "'bhreu-2. To boil, bubble, effervesce, burn' with sections I (brew/bread/broth), II (*bhrē- brood/breed), III (fermentum/fervēre), IV (spring words)."
  },
  {
   "src": "KLN",
   "where": "s.v. brew, barm",
   "stance": "supports",
   "note": "'fr. I.-E. base *bheru-, *bhreu-, *bhrū-, \"to boil, ferment\"' (brew); 'fr. I.-E. base *bher-, \"to boil, seethe\" … Cp. br
```


## [2026-09-05T14:12:19.161Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','TAD','MON','VOP','SYN','WLD','IEC','LKT','PHN','DEV','SKT','FSD','WEB','LEW','LAT','ARY','PLA','AFM','FVQ','ARB']:\n    v=d.get(k)\n    print('==',k, json.dumps(v, ensure_ascii=False)[:700])\n\"",
 "description": "Look up ref metadata"
}
```


### [2026-09-05T14:12:21.084Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start;
== DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "French headword in caps at line start.", "no
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: le
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/ARB_mo3rb.txt", "/home/sfmqrb/git
```


## [2026-09-05T14:12:25.973Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==162' POK_01.txt | head -60",
 "description": "Print Pokorny p.153"
}
```


## [2026-09-05T14:12:26.344Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bhili\" POK_01.txt POK_full.txt | head -20",
 "description": "Grep bhili in Pokorny"
}
```


### [2026-09-05T14:12:27.813Z] TOOL RESULT

```
fen,  züchtigen';  refl.  ,beabsichtigen'  {*bhoudh-iö),  baudziava , Scharwerk,  Frondienst',  lit.  bauslys  , Befehl',  lett.  bauslis  , Gebot',  lett. bauma,  bäume  , Gerücht,  Nachrede'  (*bJioudh-m-'),  lit.  pasibaudyti  ,sich erheben,  aufbrechen',  baudinti  , aufmuntern,  Lust  zu  etwas  erwecken', apr.  etbaudints  ,auferweckt'.
Themat.  Präs.  in  abg.  bljudq,  bljusti  , wahren,  hüten,  achtgeben',  russ. bljudü,  bljusti  ,beobachten,  wahrnehmen'  (über  slav.  -ßi  aus  idg.  eu  s. Meillet  Slave  commun^  58).
Kausativ  in  abg.  buzdq,  buditi  _, wecken',  russ.  buzü,  budith  ds.  (usw.; auch  in  russ.  büdenb  , Werktag',  wohl  eig.  , Wecktag'  oder  ,Tag  für  Fron- dienst'); Zustandsverb  mit  e-Suffix  in  shg.  b^^dg,bld^ti  ,wacheu',  perfektiv (mit  ne-/no-Suffix  wie  in  gr.  Ttvvd'-dvo-f.iaL,  wo  -ovo-  aus  -nno-,  Schwyzer  Gr. Gr.  I  700)  v^z-b^ng  , erwache'  (*bhud-no-,  aus  einem  Aor.  des  Typus  gr. invd'STO  gebildet,  usw.,  s.  Berneker  106  f.,  auch  über  skr.  bädnjl  dän ,Christabend',    bädnjäk    ,  Holzscheit,    das    man    am    Weihnachtsabend   ins
152
Feuer    legt'    usw.),    abg.   s^-na-b^deti    jCpvhxTXSiv^  \    abg.   hidirb    jrcQÖd'v^Q^ willig,  bereit',  bzzdrh  ds.,  russ.  bödryj  ,munter,   stark,   frisch',    skr.  hädc ^lebhaft'.
Toch.  B  paut-^  A  pot  ,ehren'?  (Van  Windekens  Lexique  87).
WP.  II  147 f.,  Feist  41,  97,  Meillet  Slave  commun*  202 f.
1.  bheug-  ,fliehen',  nach  Kretschmer  (Gl.  30,  138)  zu  2.  hheug(hy  (av.  baol
in  der  intransitiven  Bedeutung  ,sich  retten').
Gr.  cpsvycj  (Aor.  Ecpvyov,  Perf.  nscpevya)  ,fliehe',  (pvyri   f.   (=  lat.  fug^ ,Flucht',  hom.  cpv^a  (*q)vyta)  ds.,  Akk.  cpvya-de  ,in  die  Flucht'  vom  Koi Stamm  ^(pvy-\
vielleicht  im  ven.  ON  OsvyaQOv  (Westdeutschi.)  ,Fluchtburg' ;
lat.  fugiö,  fügt,  -ere  ,fliehe,  enteile,  verschmähe',  fuga  f.  ,Flucht';
lit.   bügstu,    bügau,    bügti   intr.   , erschrecken',   kaus.    bauginti  ,jemd. schrecken',  baugüs  ,furchtsam'.
WP.  II  144,  146,  WH.  I  556  f.,  Kretschmer  Gl.  30,  138.
2.  bbeug-,  hheugh-  ,wegtun,  reinigen,  befreien';  intrans.  ,sich  retten'.
Av.  baog-,  bunja-  ,lösen,  retten,  sich  retten  vor'  {bunjainti  ,sie  befreien! retten',  büjayamnö  ,ablegend',  bunjayät  ,er  rette'),  büjim  Akk.  ,Reinigung'j qzö-buj-  ,aus  Not  befreiend',  baoxtar-  ,Befreier';  pehl.  paz.  böxtan  ,retteii, erlösen',  südbal.  böjag  ,öffnen,  lösen,  losbinden',  als  pers.  Lw.  arm.  huzem ,heile,  rette,  befreie',  boi^  , Heilung,  Befreiung';  päli  paribhuüjati  ,reinigT, kehrt  aus';  aber  päli  bhujissa
```


### [2026-09-05T14:12:27.857Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:12:35.829Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"bhili\\|bhilo\\|billich\\|unbil\\|billīh\\|billih\" POK_full.txt POK_01.txt | head -30; echo \"=== full file page markers?\"; head -c 400 POK_full.txt",
 "description": "Grep Pokorny for bhili root"
}
```


### [2026-09-05T14:12:35.891Z] TOOL RESULT

```
POK_01.txt:2181:Mir.  bil  (*bhi-li-)  ,gut',  gall.  Büi-  in  PN  Blli-catus,  Bilicius  usw.,  ahd. hila-  ,gütig^,  jünger  bili-,  bil-  im  1.  Glied  von  Personennamen;  ags.  bile-wit ,einfach,  unschuldig^  =  mhd.  bilewiz,  bilioiz  ,Kobold^  (eigentl.  ,guter  Geist^); ahd.  bil-Uch  ,geziemend^;  Abstraktum  *bilipö  in  as.  unbilithunga  ,UnfÖrm- lichkeit^,  mhd.  unbilde,  unbilede  n.  ,Unrecht,  das  Unbegreifliche^,  nhd. Unbilde,  zum  Adjektiv  mhd.  unbil  ,ungerecht^,  substantiviert  Schweiz. Unbill.  Über  nhd.  Bild  s.  unter  bliei{d)-  ,schlagen^,  wozu  R.  Loewe  (KZ. 51,  187  ff.)  auch  Unbilde  stellen  will.
POK_01.txt:2184:WP.  II  185,  Kluge  11  unter  Bild,  hillig,  Unbill,  Weichbild.
POK_full.txt:14213:Saxon unbilithunga^ unconventionality ', Middle High German unbilde, unbiledeu. " 
POK_full.txt:14214:wrong; injustice, the incomprehensible ', Modern High German Unbilde, to adjective Middle 
POK_full.txt:14215:High German unbiV unjust; unfair', substantivized Swiss Unbill. About Modern High 
POK_full.txt:14217:Unbilde . 
POK_full.txt:14223:References: WP. II 185, Kluge^i under Bild, billig, Unbill, Weichbild. 
POK_full.txt:26133:ek, Malvi e:k, Bhili e:k, Dogri ik, Kumauni e:k, Garhwali e:k, W Pahari e:k, Khandeshi e:k. 
POK_full.txt:73888:(Lamani) saat, Malvi sa:t, Bhili Aa:t, Dogri sat, Kumauni sa:t, Garhwali sa:t, W Pahari sa:t, 
POK_full.txt:83651:Malvi ch"e:, Bhili so:, Dogri ch'e:, Kumauni ch'ai, Garhwali ch'ai:, W Pahari isho:, 
=== full file page markers?
List of language abbreviations in tlie lED 



Abbreviation Language name 


Aeq. 




Aequian 


Akk. 




Akkadian 


Alan. 




Alanian (=Old Ossetic) 


Alb. 




Albanian 


Anat. 




Anatolian 


Ang. 




Anglian 


AngN 




Anglo-Norman 


Aram.- 


■Iran 


Aramaeo-lranian 


Ash. 




Ashkun 


Ass. 




Assyrian 


Auk. 




Aukshtaitian 


Bactr. 




Bactrian 


Bel. 




Beloruss
```


## [2026-09-05T14:12:39.605Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2170,2190p' POK_01.txt",
 "description": "Context around bhi-li entry"
}
```


### [2026-09-05T14:12:39.644Z] TOOL RESULT

```
Vio'^en^    ahd.  biugo  .sinus^;  aisl.  bogi,  ags.  boga  (engl,  boiv),  ahd.  hogo,  nhd.
Hoaen  (ahd.  swibogo  ^Schwibbogen^  aus  *swi[bi-]bogo)]  vielleicht  dazu  got.
k,fnjan  ;kaufen^^  aisl.  byggia  ,eine  Frau  kaufen^^  ags.  bycgan,  as.  buggian
kaufen^  (vgl.   nhd.   dial.  ^sich    etwas    beibiegen-  =  ^erwerben,   nehmen^);
dazu  wohl  lett.  bauga  und  baügurs  ^Hügel^
Intensivum  (mit  Verschärfung)  germ.  *bukjan  im  mhd.  bücken,  Schweiz. hukche-   mnd.  bücken,  afries.  buckia  _,sich  bücken^   (Wissmann  Nom.  post- verb.  171,  181); WP.  II  145  f.,  WH.  I  556,  Feist  96. ^.  bbeug-  .genießend
Ai.  bhuiiktB  (mit  Instr._,  jünger  Akk.)  ^genießt^/ vgl.  bhundktiybhuftjati o-owährt  Genuß,  genießt,  verzehrt^,  bubhuksä  ,Hunger^,  bhöga-h  ,Genuß^; über  ai.  bhujisyä-  s.  oben  unter  2.  blieug-]
alb.  bunge  L,  bunk,  bungu  m.  ,(Speise)eiche^  (als  ,Nährbaum^,  Postverbale =  ,Kostgewährer^);
lat.  fungor  ^verrichte,  werde  fertig  mit^,  mit  Akk.,  später  Abi.,  defungor ,bringe  zu  Ende,  überstehe^,  perfungor  _,genieße  ganz,  verwalte  zu  Ende^ WH.  I  565  f.,  Wackernagel  Synt.  I  68,  Jokl  L.-k.  Unters.  179. bbidb'  ,Topf,  Kübel,  Faß^
gr.  Ttid-oq  n.  ,Faß,  Weinfaß^,  Tti&dycvrj,  att.  q)Lddy,vr]  ds.,  lat.  fidelia (*fides-Uä)  ,irdenes  Gefäß,  Topf^;  vermutlich  aisl.  bida  f.  ,Milchkübel^, norw.  bide  n.  ,Butterfaß^  (*bidjan-),  bidne  n.  Gefäß.
Da  aus  lat.  fiscus  ,geflochtener  Korb;  Geldkorb,  Kasse^, /scma  ,gefloch- tener  KorV  (aus  *bhidh-sko-)  für  unsere  Sippe  eine  Grundbed.  ,geflochtenes Gefäße   erschlossen   werden    darf,   gehört  sie    wohl   zu   einer  Wz.  bheidh- ,binden,  flechtend WP.  II  185,  WH.  I  492  f.,  506. bbili-,  bbilo-  ,ebenmäßig,  angemessen,  gut,  freundliche
Mir.  bil  (*bhi-li-)  ,gut',  gall.  Büi-  in  PN  Blli-catus,  Bilicius  usw.,  ahd. hila-  ,gütig^,  jünger  bili-,  bil-  im  1.  Glied  von  Personennamen;  ags.  bile-wit ,einfach,  unschuldig^  =  mhd.  bilewiz,  bilioiz  ,Kobold^  (eigentl.  ,guter  Geist^); ahd.  bil-Uch  ,geziemend^;  Abstraktum  *bilipö  in  as.  unbilithunga  ,UnfÖrm- lichkeit^,  mhd.  unbilde,  unbilede  n.  ,Unrecht,  das  Unbegreifliche^,  nhd. Unbilde,  zum  Adjektiv  mhd.  unbil  ,ungerecht^,  substantiviert  Schweiz. Unbill.  Über  nhd.  Bild  s.  unter  bliei{d)-  ,schlagen^,  wozu  R.  Loewe  (KZ. 51,  187  ff.)  auch  Unbilde  stellen  will.
154
Gr.  (piXog  fieh,  wert^  usw.  stellt  Kretschmer  (IF.  45,  267  f.)  als  y] griechisch  zu  Ijd.  bilis  ,seiri^;  dagegen  Loewe  aaO.;,  der  die  Betonung  ^1 ersten  Silbe  aus  dem  Vokativ  erklärt.
WP.  II  185,  Kluge  11  unter  Bild,  hillig,  Unbill,  Weichbild.
hhlag'  ,schlagen^
Lat.  flagvum  ^Geißel,  Peitsche^,  ßagellum  ds.,  mit  Dehnstufe  wal scheinlich  flägitö,  -äre  ^zudringlich  und  mit  Ungestüm  fordern,  dringen} mahnen^  (ursprgl.  wohl  mit  Schlägen  und  Drohungen),  flägitium  ,Schau( tat,  Schändlichkeit,  Schande^  (ursprgl.  ,öffentliche  Züchtigung  und  Ai scheltung^;  conßages  ,loca  in  quae  undique  cönfluunt  venti'  Paul  Fest.  35l scheint  verderbt  für  conflüges)]
aisl.  und  nnorw.  dial.  blaka,  blakra  ,vor  und  zurück  schlagen,  fächeln] flattern^,    aisl.   blak    ,Schlag^,    aisl.    blekkja    (Hlakjan)    ,schlagen^    (non , flackern^),  schwed.    mdartl.    bläkkta   (*blakatjan)j   mndl.   blaken  ,fächel flattern,  schlottern^  (im  Germ,  lautlicher  Zusammenfall  mit  der  Sippe  vo! aisl.  blakra  ,blinken^  usw.,  s.  u.  *bheleg-  ,glänzen^;  so  ist  z.  B.  norw.  blakri sowohl  ,fächeln^  als  ,glänzen^).
Lit.  blaskaü  und  blo§kiü  (-sk-  aus  -g-sq-)  ,hin  und  her,  seitwärts  schleif dern,  hin  und  her  reisen,  umhersausen^
WP.  II  209,  WH.  I  511  f.
bhlagh-men-  ,Zauberpriester^;  ursprgl.  wohl  Neutrum  ,Opferhandlung^
```


## [2026-09-05T14:12:40.144Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '14195,14230p' POK_full.txt",
 "description": "English Pokorny version of the entry"
}
```


### [2026-09-05T14:12:40.190Z] TOOL RESULT

```
{*fides-lia) " earthenware vessel, pot, pan'; presumably Old Icelandic bidai. "milk tub ', 
Norwegian bideu. "butter tub' {*bidjan-), bidneu. "vessel'. 

There from Latin f/scus' a basket; hence a money-bag, purse; the state treasury; under 
the empire, the emperor's privy purse ', fiscina " a small basket ' (from *b^i(ii^-sko-) may be 
reconstructed for its family a basic meaning " twisted vessel ', it belongs probably to a root 
b'^e/dh- "bind, flax, wattle, braid'. 

References: WP. II 185, WH. I 492 f., 506. 
Page(s): 1 53 

Root / lemma: b^ili-, b^ilo- 
Meaning: harmonious, friendly 

Material: Middle Irish b/7{*b^f-/f-) "good', gall. B/7/-\n PN Bili-catus, Bilicius e\.c. Old High 
German bila- "kind, gracious', newer bili-, bit- in 1 . part of people's name; Old English bile- 
M/y/ "simple, just, innocent' = Middle High German bilewiz, bilwiz^iawj demon, ghost' 
(actually "good ghost'); Old High German M-^c/7 "proper'; abstract noun *biliPd\v\ Old 
Saxon unbilithunga^ unconventionality ', Middle High German unbilde, unbiledeu. " 
wrong; injustice, the incomprehensible ', Modern High German Unbilde, to adjective Middle 
High German unbiV unjust; unfair', substantivized Swiss Unbill. About Modern High 
German Bildsee below b^ei(a)-^b\{\ wherefore R. Loewe (KZ. 51, 187 ff.) will place also 
Unbilde . 

Gr. cpiAo(; " dear, friend ' etc places Kretschmer (IF. 45, 267 f.) as pre Greek to Lydian 
bills 'be'; against it Loewe aaO., which explains the stress of the first syllable from the 
vocative. 

References: WP. II 185, Kluge^i under Bild, billig, Unbill, Weichbild. 
Page(s): 153-154 

Root / lemma: b^lagh-men- 

Meaning: priest 

Note:
```


## [2026-09-05T14:12:53.844Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== AHD watkins bhili/philo\"; grep -n -i \"bhili\\|bhilo\" AHD_watkins1985.txt | head; echo \"--- philos in AHD\"; grep -n \"philos\\b\\|philo-\\|philosoph\" AHD_watkins1985.txt | head -20; echo \"=== SYN 1110 leaf 1134\"; awk 'BEGIN{RS=\"\\f\"} NR==1135' SYN.txt | head -40",
 "description": "Check AHD Watkins and Buck 1110"
}
```


### [2026-09-05T14:12:55.512Z] TOOL RESULT

```
=== AHD watkins bhili/philo
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
2043:PALUDISM _pele-1 PALYNOLOGY pel-! PAM bhilo-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
--- philos in AHD
50:Jones was content with the assertion of a common original language, without exploring the details. Others took up the cause, notably the German philosopher Friedrich von Schle- gel, to whom is principally due the popular diffusion of the long-lived misconception that the European languages were in some sense derived from Sanskrit. But it remained for another German, Franz Bopp, to found the new science of comparative grammar, with the publication in 1816 of his work On the conjugational system of the Sanskrit lan- guage, in comparison with that of the Greek, Latin, Persian, and Germanic languages. He was twenty-five when it appeared.
340:bheue-. Also bheu-. To be, exist, grow. I. Extended forms *bhwiy(o)-, *bhwi-. 1. Germanic *biju in Old Eng- lish béon, to be: BE. 2. Latin fieri, to become (third person singular present subjunctive fiat): FIAT. 3. Possi- bly suffixed form *bhwi-lyo- in Latin filius, son; but this is possibly from dhé(i)-. II. Lengthened o-grade form *bhéw- in Germanic *béwan in: a. Old Norse bia, to live, prepare (present participle bondi); BONDAGE, BOUND‘; HUSBAND; b. Middle Dutch bouwen, to cultivate: BOW- ERY; C. Old Danish bdth, dwelling, stall, akin to the Scandinavian source of Middle English bothe, market stall: BooTH. III. Zero-grade form *bhu-. 1. Germanic *buthia in: a. Old English bold, dwelling, house, hence byldan, to build: BUILD; b. alternate Germanic form *béthla in Middle Dutch bédel, riches, property: BOoo- DLE. 2. Greek phuein, to bring forth, make grow, phutos, a plant, and phusis, growth, nature: PHYSIC, PHYSIO-, PHYSIQUE, -PHYTE, PHYTO-, PHYTON; DIAPHYSIS, DIPHY- ODONT, EPIPHYSIS, HYPOPHYSIS, IMP, MONOPHYSITE, NEOPHYTE, PERIPHYTON, SYMPHYSIS, TRACHEOPHYTE. 3. Suffixed form *bhu-td- in Welsh bod, to be: EISTEDD- FOD. 4, Suffixed form *bhu-tu- in Latin futirus, “that is to be,” future: FUTURE. IV. Zero-grade form *bhii- (< *bhua-). 1. Germanic *biiram, dweller, especially farmer, in: a. Old English bir, “dwelling space,” bower, room: BOWER}; b. Old English gebir, dweller (ge-, collective prefix; see kom): NEIGHBOR; Cc. Middle Dutch gheboer, ghebuer, peasant: BorR, Boor. 2. Germanic *birjam, dwelling, in Old English byre, stall, hut: BYRE. 3. Suf- fixed form *bhi-lo- in Greek phulon, tribe, class, race, and phulé, tribe, clan: PHYLE, PHYLETIC, PHYLUM; PHY- LOGENY. V. Suffixal forms in Latin. 1. *du-bhw-io-, “being two,” in Latin dubius, doubtful, and dubitdre, to doubt (see dwo-). 2. *pro-bhw-o-, “growing well or straightforward” (see per'). 3. *super-bhw-o-, “being above,” in Latin superbus, superior, proud (see uper). VI. Possibly Germanic *baumaz (and *bagmaz), tree (? < “growing thing”), in: a. Old English béam, tree, beam: uel b. Middle Dutch boom, tree: BooMm?. [Pok. bheu- 146. bheug-'. To flee. 1. Zero-grade form *bhug- in Latin fugere, to flee: FUGACIOUS, FUGITIVE; CENTRIFUGAL, FEVERFEW, REFUGE, SUBTERFUGE. 2. Extended form *bhuga in: a. Latin fuga, flight (> fugdre, to drive away): -FUGE, FUGUE; FEBRIFUGE; b. Greek phugé, flight: APOPHYGE. [Pok. 1. bheug- 152.] bheug-2. To enjoy. Nasalized zero-grade form *bhu-n-g- in Latin fungi, to discharge, perform: FUNCTION, FUNGI- BLE; DEFUNCT, PERFUNCTORY. [Pok. 4. bheug- 153.] bheug-*. To bend; with derivatives referring to bent, pliable, or curved objects. 1. Germanic *baugaz in: a. Old English béag, a ring: BEE?; b. Old High German boug, a ring: BAGEL. 2. Germanic *bugon- in: a. Old English boga, a bow, arch: Bow’; b. compound *alino- bugén-, “bend of the forearm,” elbow (*alino-, forearm; see el-'), 3. Germanic biégan in Old English bigan, to bend: Bow?, BUXxOM. 4. Germanic causative form *baug- Jan in Old Norse beyla, a swelling, akin to the probable Scandinavian source of Middle English baile, baill, a handle: Barn’. 5. Germanic *buhtiz in Old English byht, a bend, angle: BIGHT. 6. Celtic *buggo-, “flexible, mallea- ble,” in Scottish and Irish Gaelic bog, soft: BoG. [Pok. 3. bheug- 152.] bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153,] bhiad-. To worship. Suffixed form *bhildd-(s)men- in Latin flamen, priest (of a particular deity): FLAMEN. [In Pok. bhlag-men- 154.] bhlag-. To strike. 1. Germanic *blak-, perhaps in the probable Scandinavian source of Middle English bakke, bat: BAT?. 2. Latin flagrum, a whip (> flagellum, little whip): FLAGELLATE, FLAGELLUM, FLAIL, FLOG. 3. Latin
=== SYN 1110 leaf 1134
d-, etc.). Walde-P. 1.237, Pedersen 1.41. Stokes 265.
Ir. gel, NIr. geal : OE geolo, ete. ‘yel- low’ (15.69).
Ir. ban : Skt. bha-, Av. ba- ‘shine’, etc, (15.56).
W. can, Br. kann (‘brilliant white’) : (or loanword fr.) Lat. candidus ‘bright’ (15.57). Walde-P. 1.352. Pedersen 1.199. i
4. Goth. hweits, OE hwit, etc., general Gme. : Skt. cveta-, Av. spaéta- ‘white’, ChSl. své& sb. ‘light’ (1.61), svétiti ‘shine’, etc. (15.56). Walde-P. 1.470. Falk-Torp 439.
5. Lith. balias, Lett. balts (and fr. different grade without suffix) ChSl. bélti, etc., general Slavic : Grk. ¢adés" devxds (Hesych.), ON bal, OF bal ‘flame, funeral pile’, Skt. bhala- ‘fore- head’, fr. IE *bhel- (perh. related to *bha- ‘shine’, cf. above, Ir. ban). Walde- P. 2.175f. Berneker 55f. Trautmann 25, 29 f.
6. Skt. cukra-, gukla- ‘bright, clear, pure’ (15.57), also ‘white’.
Skt. cveta-, Av. spaéta-, above, 4.
Skt. arjuna- : Grk. apyés, above, 1.
Av. auruxa-: Skt. aruga-,” aruna- ‘ruddy’, perh. OHG elo, MHG el (ae ‘tawny, yellow’. Walde-P. 1.159, 2.99.
SENSE PERCEPTION
Digitized by Arya Samaj Foundation Chennai and eGangotri
1055
15.65 BLACK
is Goth. swarts Lith. juodas Grk. pednss prec ON svartr Lett. sates NG pe get Dan. _ sort ChSl. Griintt iat. aler; Sw. svart SCr. crn It nero OE blac, sweart Boh. éerny ir. now 5 ME blak, swart Pol. czarny Sp. ‘wl NE black Russ. ternyj Rum. al Du. zwart Skt.  krgna-, ¢yama- i ane oe suarz Ay. sdma-, sydva- Nir. swarz W. a NHG schwarz r
Words for ‘black’ in part reflect such votions 8 ‘dirty’, ‘smoky’, ‘blackened by fire’(?). Some belong to inherited groups containing words applied to various colors, the primary sense of which is obscure. Some old words for ‘black’ that were replaced by others survived in the sense of ‘ink’ (18.58).
1, Grk. pétas (NG perdu ‘ink’, peda- yos ‘blue-black, livid’) : Lett. melns ‘black, dirty’, Skt. mala- ‘dirt, filth’, malina- ‘dirty’, etc. (15.88).
Grk, xedawds : Skt. kalanka- ‘spot, blemish’, kalana- ‘spot, dirt’, Swiss helm ‘white spot on the forehead of cattle’, ete. Walde-P. 1.440 f. Boisacq 480.
Byz., NG padpos, late Grk. pavpés, for duaupds ‘dim, faint, hardly seen’ (: ON meyrr ‘tender, soft’, Russ. smuryj ‘dark- gtey’, chmuryj ‘overcast, cloudy, sullen’, ete. Walde-P, 2,223).
2. Lat. ater, Umbr. atru, adro ‘atra’, Ss blackened, burned by fire’ : Bee aM fire’, Arm. airem ‘kindle, (3 Bs - vatra ‘fire’, etc. Walde-P. 298 tout-M. 83 f. Walde-H. 1.75f.,
Lat, miger (> Romance words) ?
aed Walde-P. 2.322. Emout-M. 671. Goth : dub, NIr. dubh, W., Br. du: ; cufs, ON daufr, etc. ‘deaf’, Grk. blind, dark’, rS¢os ‘smoke, vapor, » thd ‘smoke, burn slowly’, fr. ~ extension of *dheu- seen also fuscus ‘dark’, etc., 15.68). 1’, here prob. fr. ‘confused,
at,
i lack, da;
dimmed by vapor’ or the like. Walde-P. 1.840. Pedersen 1.116.
4, Goth. swarts, ON svarir, etc., gen- eral Gmc. (NE swart only rhet., poet., or dial.) : Lat. sordés ‘filth’, sordidus ‘dirty’ (15.88), sudswm, a kind of dark color. Walde-P. 2.535. Falk-Torp 1109. Ernout-M. 958, 991.
OE blec, ME blak, NE black (as sb. OE blac, OHG blach, OS blak ‘ink’), etym. disputed, prob. : OHG ODlecchen, MHG blecken ‘be visible, let see’, OHG blanc ‘shining white’, Du. blaken ‘burn, glow’, Lat. flagrdre ‘flame, burn’, Grk. gdéyw ‘burn, blaz
```


## [2026-09-05T14:13:03.610Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for n in 1188 1190 1192; do echo \"===== record $n\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' SYN.txt | grep -n \"^[0-9]\\{3,4\\}$\\|Digitized\" ; done",
 "description": "Locate Buck page 1110"
}
```


### [2026-09-05T14:13:05.083Z] TOOL RESULT

```
===== record 1188
23:Digitized by Arya Samaj Foundation Chennai and eGangotri
===== record 1190
21:Digitized by Arya Samaj Foundation Chennai and eGangotri
===== record 1192
11:Digitized by Arya Samaj Foundation Chennai and eGangotri
```


## [2026-09-05T14:13:07.969Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"φίλος\\|pidos\\|φίλ\" SYN.txt | head; echo \"--- search 'dear' section\"; grep -n \"16.28 DEAR\\|DEAR (beloved)\\|16\\.28\" SYN.txt | head",
 "description": "Find Buck's dear/friend section"
}
```


### [2026-09-05T14:13:08.038Z] TOOL RESULT

```
4207:Umbr. erietu: Grk. épidos ‘kid’, Ir. heirp ‘she-goat’, all prob. fr. IE *er- in words of motion, as Grk. épviy, Skt. r-, etc. (Walde-P. 1.135, 136, without con- necting the two groups). G. §. Lane, Language 7.281 ff.
4470:‘gray’, etc. Walde-P. 1.602f. TFalk- | ssdéi ‘suck’. 3.36 3.37 3.38 GOAT HE-GOAT KID (Generic or feminine) Grk. al (xlpatpa) Tp&yos épidos NG ylét, fem. yida  rpa&yos, rpayl karolxe Lat. capra hircus, caper haedus It. capra becco, capro capretto Fr. chevre, bique bouc chevreau, biquet Sp. cabra, chiva cabrén cabrito Rum. capré lap caprioard Ibe, gabor boce menn(dn) Nir. gabhar boc mionnan W. gafr bweh myn Br. gaor bouc’h gaorig Goth. gaits Sante pueceis | ON get hafr (bukkr) kid | Dan. ged buk kid Sw. get bock kid OE gat bucca, hafor ticcen, hécen ME pote bucke kide NE goat he-goat kid Du. geit bok geitje OHG  geiz, ziga boc zicki(n), kizzt(n) - MHG geiz, zige bock 2ickelin NHG ziege, geiss bock zicklein Lith. oka ozys ozelis, ozkutis Lett. kaza Gzis kazlens ChSl. koza koztlit koztle SCr. koza jarac Jare, kozlié Boh. koza kozel kizle Pol. koza koziot koéle Russ. koza kozel kozlenok Skt. _aja-; fem. aja- aja-, chaga- “a Av. i tlcts biza-
9219:Grk. n\n (Hom.), later pidos ‘mill’ or ‘millstone’, also puvddy ‘mill’ (as the place), NG pbdos ‘mill’.
9992:4. Late ChSI., obs. SCr., Russ. jarina : Grk. épidos ‘kid’, Lat. aries ‘ram’, Lith. éras ‘lamb’. Walde-P. 1.135, Berneker 447.
22837:, 1101 eB. ® (Fxopidos); Lat. Mooutns
--- search 'dear' section
21080:derivatives of It. costo, ete. ‘cost? (11.72), as It., Sp. costoso, OF r. costeus (> ME costouse > W. costus), Fr. cotteux, NE costly, NHG kostbar, etc. 1. Grk. zodvredjs, cpd. of zodb ‘much’ and last member fr. rédos ‘tax, toll, duty’ (11.69). Grk. riptos, fr. riuy ‘price’ (11.87). NG dxpiBés, fr. class. Grk. axpifis ‘exact, precise, accurate’ then (fr. ‘exact in money matters’) ‘parsimonious, stin- gy’ and hence ‘dear’ (as SCr. skup, be- low). 2. Lat. carus (> It., Sp. caro, Fr. cher) ‘dear’ = ‘beloved’ (16.28) and ‘ex- pensive’ (Plaut. in both senses). Rum. scump, fr. Slavic, cf. Bulg. ska- pu, etc. below, 6. 3. Ir. logmar, epd. of log ‘price’ and mar, mor ‘great’.
27434:16.28 Drar
27918:16.28 JOYFUL, GLAD
28053:the adjs. for ‘dear’ are also cognate with the words for ‘love’ and so are included in the discussion here, though listed sepa- rately (16.28).
28077:i a bire . Ww 7 eSpace an fr, the Slavic, cf. ChSl. Ljubiti, ae Rojas ‘love’ with drag ‘dear’, fr, the Slavic, ef. late Chsl. dr agoslt ipreciousness' ChSl. drag ‘precious, modern Slavic also ‘dear’ (16.28). Tik- in 569f., 571. ce rad, NIr. gradh, whence the yb. gradhaim, orig. dub., perh. loanword fr, Lat. gratum ‘favor’ (gratus ‘accept- able, agreeable’) in phrases like gratum facere alicui, Walde-P. 1.601. Walde- H. 1.620. Otherwise (as cognate) Pedersen 1,133.
28110:16.28 DEAR Grk. gles Goth. liufs Lith.  mielas NG &yamnrés (pos) ON ljafr, kerr Lett. mil’ Lat. cdrus Dan. kar, elsket ChSl.  viizljublenii, Ljubi It. caro Sw. kar, alskad SCr. mio, drag Fr. cher OE léof, déore Boh. drahy, mily Sp. caro ME _sleve, dére Pol. luby, mity Rum. drag NE dear Russ. mil, dorog Ir. dil, coim, inmain Du. lief Skt. priya- NIr. — dilis, ionmhain OHG  liob Av. — frya-, frida- W. annwyl, cu, hoff MHG liep Br. _ ker, kaez NHG lieb, tener
28487:Av. asdta-, neg. of $ata- ‘glad’ (16.28).
29970:ON, OE, Du. lof, OHG lob, etc. (Dan., Sw. lov mostly biblical) with vbs. ON lofa, OE lofian, ete. : Goth. liufs, OF léof, etc. ‘dear’ (16.28) and OF lufu, etc. ‘love’ (16.27), with development ° of ‘praise’ (vb.) fr. ‘find pleasing’. Walde- P. 2.419. Falk-Torp 657.
33689:1. Grk. gidos, orig. adj. ‘dear’ (16.28).
33713:Av. frya-, as adj. ‘dear’ (16.28).
```


## [2026-09-05T14:13:12.001Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '28110,28135p' SYN.txt; echo \"=== FRIEND section\"; sed -n '33680,33700p' SYN.txt",
 "description": "Buck 16.28 dear and friend entries"
}
```


### [2026-09-05T14:13:12.055Z] TOOL RESULT

```
16.28 DEAR Grk. gles Goth. liufs Lith.  mielas NG &yamnrés (pos) ON ljafr, kerr Lett. mil’ Lat. cdrus Dan. kar, elsket ChSl.  viizljublenii, Ljubi It. caro Sw. kar, alskad SCr. mio, drag Fr. cher OE léof, déore Boh. drahy, mily Sp. caro ME _sleve, dére Pol. luby, mity Rum. drag NE dear Russ. mil, dorog Ir. dil, coim, inmain Du. lief Skt. priya- NIr. — dilis, ionmhain OHG  liob Av. — frya-, frida- W. annwyl, cu, hoff MHG liep Br. _ ker, kaez NHG lieb, tener
The majority of words for ‘dear’ Se ‘beloved’) are connected with words for ‘love’ and have been included in the dis- cussion of the latter (16.26). The others, including some in which the earlier sense was ‘dear’ = ‘valuable, ex- pensive’ (11.88), are:
Ir. dil, etym. dub., perh. *dwe-li- :
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
*dwe-no- in Lat. bonus, OLat. duenos ‘good’. Vendryes, Miscell. K. Meyer, . 289. < Ir. céim (also ‘handsome, fine’), W. cu, MBr. cuff (NBr. kunv ‘gentle, Be fable’) : Lett. saime ‘family’, OB a OHG heim, ‘home’, etc. Walder. 1.259. Pedersen 1.58.
maniin Nir. jonmhain, perh. y lem fr. the root of menme igi Macbain 218. ee ‘nia dilis, also ‘faithful’, orig. ones ee this sense Olr. diless (cf. W. eae Ptr) epd. of neg. di- and -less ays * , W. llys-fab ‘stepson’ : Ir.
Wy, annwyl, etym.? Morris Jones 160
(but??).
Br. ker, MBr. quer, of Fr. cher. Henry 63. | Br, kaez (MBr. quaez ‘captive, un-
fr. a Norman form
fortunate’) ‘unfortunate, miserable’, Grk,  iAtw, Kuvew Goth. kukjan gid ON kyssa dsculari, savidri, ba- Dan. kysse sidre Sw. kyssa .  baciare OE cyssan .  embrasser, baiser ME kisse .  besar NE kiss Rum. sdruta Du. kussen »  pocaim OHG  kussen Nir, pogaim MHG_kiissen “ cusanie NHG kissen ' _pokat
Kissing, as an expression of affection or love, is unknown among many races, and in the history of mankind seems to - : later substitute for the more primi- i ERE of noses, sniffing, and lick- Zs na © partial agreement among words ele ae m some of the IE languages syllables. on Some common expressive # Lie pe 1S NO conclusive evidence mas late = aes Hnown in IE times. It Debably rea ndia, pad a Slavic group der, Reale ects the ‘lick’ kiss. Schra- Snifr. oe x S.v, Kuss. Hopkins, The B19 an Ancient India, JAOS Orient, Ber, Pal Der Kuss im alten 8s. Akad. 1934. 914 ff.
Digitized by Arya Samaj Foundation Chennai and eGangotri
; TEMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1113
whence by affectionate commiseration ‘dear’ : W. caeth, Ir. cacht ‘slave’, Lat. captus ‘captive’, etc. Henry 57.
OE déore, ME dére, NE dear, also ‘precious, expensive’ (cf. 11.88) in OF and ME often ‘glorious, noble’ : ON dyrr ‘precious, noble’, OHG tiure ‘glori- ous, excellent, valuable’, NHG teuer ‘dear’ (in both senses), outside connec- tion dub. Falk-Torp 172. Weigand-H. 2.1040 fi.
SCr., Bulg. drag (> Rum. drag), Boh. drahy, Russ. dorog, also ‘precious, valu- able’, Pol. drogi, ChSl. drag only in the latter sense (cf. also Lett. dargs id., prob. loanword), etym.? Berneker 213.
16.29 KISS (vb.)
Lith. buéiuoti
Lett.  butuot, skipstit ChSl.  lobiizati, célovati SCr. Ujubitt, cjelivatz Boh.  Libatt (celovatz)
Pol. calowaé
Russ. celovat’
Skt. (cumb-)
Av. :
A distinction between the kiss of affec- tion and that of erotic love is sometimes made as in Latin (cf. Sciendum osculum religionis, savium voluptatis; quamvis quidam osculum filiis dari, uxori basium, scorto savium dicant, Serv. ad Verg.), but even here is not maintained and in general is ignored.
Several of the words for ‘kiss’, as already stated, are of imitative origin. One is from a ‘little mouth’. Some come, through church influence, from the kiss of ‘peace’ or ‘greeting’. In some the feeling of ‘love’ is the antecedent of its expression as ‘kiss’.
=== FRIEND section
Grk. — plos Goth. frijonds Lith. draugas, bitiulis NG pbdos ON vinr Lett. draugs
Lat. amicus 5 Dan. ven ChSl. drugit, prijateljt
It. amico Sw. vén SCr. __ prijatelj
Fr. ami OE fréond, wine Boh.  prttel
Sp. amigo ME frend Pol. przyjaciel
Rum. amic, prieten NE friend Russ. drug, prijatel’
Tr. care : Du. _—vriend Skt. sakhi-, suhrd-, mitra- Nir. cara OHG friunt, wint Av. urvaéa-, haxi-, frya- W. cyfaill MHG ovriunt, win(e) OPers. dauStar-
Br. mignon NHG  freund
Words for ‘friend’ are most commonly Cognate with words for ‘love’ or ‘dear’. Some mean also and more originally ‘companion’. A curious Lith. popular term for ‘friend’ means properly ‘bee- keeper’.
1. Grk. gidos, orig. adj. ‘dear’ (16.28).
2. Lat. amicus (> Romance words,
but Rom. amic neolog.) : amare ‘love’ (16.26).
Rum. prieten, fr. Slavic, ef. ChSl.
prijateljt (below, 6). Tiktin 1252.
3. Ir. care, NIv. cara, orig. pres. pple. (*karant-s) of caratim ‘love’ (16.27). Pedersen 1.244. Thurneysen, Gram.
110, 209.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
| | {
Digitized by Arya Samaj Foundation Chennai and eGangotri
1344 SELECTED INDO-EUROPEAN SYNONYMS
W. cyfaill, old cyfaillt = Ir. com-alta ‘foster-brother’, orig. pres. pple. of *com-alim, cpd. of alim ‘nourish, rear’. Pedersen 2.35.
```


## [2026-09-05T14:13:17.174Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Asianic\\|Kretschmer\" SYN.txt | head -20",
 "description": "Search Buck for Asianic/Kretschmer"
}
```


### [2026-09-05T14:13:17.218Z] TOOL RESULT

```
411:Grimm J. und W. Grimm, Deutsches Wérterbuch. GRM_ Germanisch-romanische Monatschrift. Harper Harper’s Latin Dictionary. Hatzidakis, Einl. G. Hatzidakis, Einleitung in die neugriechische Grammatik. Hatzidakis, Meo. I. Xarfidaxts, Mecawwryixa Kal véa "EAAQUKG. Hellquist E. Hellquist, Svensk etymologisk Ordbog, 2d ed. Henry V. Henry, Lexique étymologique du breton moderne. Hermann, Lit.-deutsches Gesprichsb. E. Hermann, Litauisch-deutsches Gesprichsbiichlein. Hessen Hessen’s Irish Lexicon, a Concise Dictionary of Early Irish. Hesych. Hesychii Alexandrini Lexicon. Hirt, Idg. Gram. H. Hirt, Indogermanische Grammatik. Holthausen F. Holthausen, Altenglisches etymologisches Worterbuch. Horn P. Horn, Grundriss der neupersischen Etymologie. Hiibschmann, Arm. Gram. H. Hiibschmann, Armenische Grammatik, I. Theil. Idg. Anz. Anzeiger fiir indogermanische Sprach- und Altertumskunde. Idg. Jhrb. Indogermanisches Jahrbuch. IF Indogermanische Forschungen. IG Inscriptiones Graecae. ‘Tor. Ack. ‘Ioropixdy Aetixdv ris véas ‘EAAnvexijs. Jagié, Entstehungsgesch. V. Jagié, Entstehungsgeschichte der kirchenslavischen Sprache. JAOS Journal of the American Oriental Society. JEGPh. Journal of English and Germanic Philology. JHS Journal of Hellenic Studies. Kluge-G. F. Kluge, Etymologisches Worterbuch der deutschen Sprache, 11. Aufl., bearbeitet von Alfred Gétze. 4 Kretschmer, Hinl. P. Kretschmer, Hinleitung in die Geschichte der griechischen Sprache. Kretschmer, Wortgeogr. P. Kretschmer, Wortgeographie der hochdeutschen Umgangs- sprache. Kurschat F. Kurschat, Litauisch-deutsches und Deutsch-litauisches Woérterbuch. KZ Kuhn’s Zeitschrift (Zeitschrift fiir vergleichende Sprachforschung). Lalis A. Lalis, A Dictionary of the English and Lithuanian Languages. Language Language (Journal of the Linguistic Society of America). Laws, Gloss. Ancient Laws of Ireland, vol. VI, Glossary, comp. R. Atkinson. Le Gonideec Le Gonidec, Dictionnaire frangais-breton et breton-frangais. Leskien, Ablaut A. Leskien, Der Ablaut der Wurzelsilben im Litauischen. Leskien, Bildung d. Nom. A. Leskien, Die Bildung der Nomina im Litauischen. Leskien, Gram. A. Leskien, Grammatik der altbulgarischen Sprache. Lewis-Pedersen H. Lewis and H. Pedersen, A Concise Comparative Celtic Grammar. Lidén, Arm. Stud. E. Lidén, Armenische Studien. Lidén, Stud. E. Lidén, Studien zur altindischen und vergleichenden Sprachgeschichte. Linde M.S. B. Linde, Slownik jezyka polskiego. Littré HE. Littré, Dictionnaire de la langue francaise. Lokotsch K. Lokotsch, Etymologisches Wérterbuch der europiischen Worter orientalischen Ursprungs. Loth, Mots lat. J. Loth, Les mots latins dans les langues brittaniques. LS Liddell and Scott, Greek-English Lexicon, 9th ed. Lunds Univ. Arssk. Lunds Universitets Arsskrift. Macbain A. Macbain, An Etymological Dictionary of the Gaelic Language. Macdonell-Keith A. Macdonell and A. Keith, Vedic Index of Names and Subjects. McKenna L. McKenna, English-Irish Dictionary.
807:1. IE *Ghem- and *§h®em-, represent- ing the most widespread cognate group, though the precise character of the IE variant form involves a difficult rob- lem. Walde-P. 1.662 f. Ernout-M. 464. Walde-H. 1.664f. The inclusion in this group of Hitt. tekan, Toch. A tkam ‘earth’, and the resulting assumption of IE *dheghom-, *dhghom- (Kretschmer, Glotta 20.66 f.), is rejected by Ben- veniste, Mélanges Ginneken 193 ff. But some ultimate connection is probable.
910:NHG dreck, orig. and still in part ‘excrement’ (4.66), but also the usual word for ‘mud’ in many regions. On the local distribution of dreck vs. kot in this sense, cf. Kretschmer, Wortgeogr.
935:1. Group of words belonging together, but of partly obscure phonetic relations, prob. (init. doublets ps-, s-) fr. the root seen in Grk. Waw ‘rub, crumble’, Widos ‘pebble’, etc. (Skt. bhas-, psa- ‘chew, devour’, fr. ‘crush’). Kretschmer, KZ 31.420. Ernout-M. 881.
1159:cane’, éravyifw ‘rush upon’, Skt. e-, ing- ‘shake’, etc.; further analysis dis- puted, but perh. second part : &\Aouar ‘spring, leap’, hence orig. ‘place upon which the waves dash’. Walde-P. 1.11. Bechtel, Lexilogus 16. Kretschmer, Glotta 27.28 f.
1241:Ir. dobur (rare, but cf. dobur-chu ‘ot- ter’, lit. ‘water dog’), W. dwfr, Br. dour (Celt. *dubro-) : 60Bpis* @4hacoa Schol. Theocer. (prob. Illyr.), Alb. det ‘sea’, and these : W. dwfn, Goth. diups, ete. ‘deep’ (12.67), ChSl. dino ‘bottom’, dibri ‘val- ley’, etc. Pedersen 1.35f. Kretschmer, Glotta 22.216. Pokorny, Z. celt. Ph. 20.513. Otherwise (: Ir. dub ‘black’) Walde-P. 1.840.
1257:2. Grk. @4\acca, the main word at all periods, fr. *@4da-x-1a (ef. dadayxav’ $adhaccay Hesych., presumably a Maced. form) or the like : 94Xapos ‘inner room’, 96dos ‘vaulted room’, ChSI. dolt ‘pit’, Goth, dals ‘valley’, ete. Transition from ‘hollow, deep’, to ‘sea’. Cf. Lk. 5.4 els 70 Babos, OE on dypan ‘into the deep’, NE cross the deep, and the gloss 6bBpis: 94Xacca (prob. Illyr.), with Alb. det ‘sea’ : Goth. diups, ete. ‘deep’ (Kretschmer, Glotta 22.216). There is no need to as- sume, as is generally done, that 64racca is of pre-Greek origin. Buck, Class. Studies Presented to E. Capps 42 ff.
1310:Hence, with peculiar change in form, the international word, NE gulf, etc., the history of which is as follows (cf. Kretschmer, Byz. Z. 10.581 ff.). Late Lat. colphus with spelling ph, then pro- nounced and spelled colfus (cf. rpémavov > Lat. tropaeum, late trophacum > Fr. trophée, NE trophy). This colfus > late Grk. «éd¢os, whence NG pop. xép¢os (with pas in jp9a = 70a; but this form now usual only for ‘bosom’, not for ‘gulf’, which is x6\zos); also (with g for c as in late gummi for cummi = Grk. koupe ‘gum’) It. golfo (> Fr. golfe > ME goulf, NE golf, NHG golf, Rum. golf, etc.), Sp. golfo.
1393:4. Grk. rorapss (NG POp. wordt), fr. root of rimrw ‘fall’, réropat ‘fly’, Skt. pat- ‘fly, fall’, etc. That is, Torayés was at first the ‘falling, plunging, rushing’ stream. Walde-P. 2.19. Persson, Bei- trige 654. Kretschmer, Glotta 27,248 f.
2216:Du. aansteken, cpd. of steken ‘thrust.’ So locally NHG anstecken, Kretschmer, Wortgeogr. 79f.
2245:NHG séreichholz, fr. streichen ‘rub, strike’ and holz ‘wood’. Less commonly ztindholz fr. ziinden ‘light’ (1.86), also schwefelholz, fr. schwefel ‘sulphur’, the old word for the sulphur match (like Dan. svovelstikke, Du. zwavelstok, etc.) still used in some places for the current match, Kretschmer, Wortgeogr. 503 f.
2270:3. Grk. aOpwros, etym. much dis- puted. But the old analysis av§p-wzos ‘man-faced, man-like’, fr. the stem of avip, avipds remains the most probable. Cf. Hesych. dpwp- dvOpwros, and for the semantic relation cf. OHG mannisco fr. man (above, 2). The change of avdp- to avOp- is due to a ‘in the second element (cf. répurmov fr. *Terp-rmov), which does not belong properly to the root é7- but may be due to the influence of dpaw. Kretschmer, Glotta 9.231 f., 27.246.
2563:ly meaningless infantile syllables pa and ma, with suffix added after the analogy of other pairs of contrasted relations, while the simpler forms with or without reduplication, like NE pa, ma, papa, mama, continued in use as pet names. Such infantile syllables or nursery words play a considerable role in the words of relationship. They give rise to pet names of loose application which may become specialized in various directions. A similar use of infantile syllables, es- pecially for ‘father’ and ‘mother’, is ob- served in languages from all over the world. Cf. Kretschmer, HFinleitung 353 ff., and, for Latin, Heraeus, Die Sprache der rémischen Kinderstube, Arch. lat. Lex. 13.149 ff.
2698:Kretschmer F estschrift 289 ff. Otherwise Walde-P.
3546:- Kretschmer, Wortgeogr. 454.
4390:de. 2.512. . Ernout-M. 100 f. Ls 465 Kretschmer, Glotta 3.132 f. ig pan Geudiats (sentence-doublets, not to . separated as in Walde-P.); Lat. sas, Umbr. sif ‘sues’; W. hwch BOW (for- erly generic), Br. houc’h ‘hog’; ON sr, OE su, etc., all the Gme. words for sow : and fr. *swino- (orig. adj. like Lat. suinus) the generic words, Goth. tne, OF swin, etc.; Lett. suvens, sivens pig’; ChSl. svinija, etc., the Slavic words, fr. a fem. deriv. of *swino-; Skt. stkara- (fem. stikart- ‘sow’), Av. hiu-; Alb. tht; Toch. B. suwo.
4538:goire, Etud. Horat. 81f, Byzantion 11.615 (: Grk. xdBados ‘rogue’, orig, ‘porter’ ; rejected by Kretschmer, Glotta 27.232).
4544:For the local distribution of NHG pferd, ross, gaul, cf. Kretschmer, Wort- geogr. 61, 600.
5017:2. Lat. stmia (>It. scimmia, Fr. singe), deriv. of stmus, loanword fr. Grk. otés ‘snub-nosed’. First used as a nickname and prob. based on the name ZYuyuslas, Simia. Kretschmer, KZ 33, 563.
5839:OHG baccho (rare, gl. to mandibula, mala; cf. chinnibahho ‘jaw’), MHG backe, NHG backe or backen, in early period partly ‘jaw’, now the popular word for ‘cheek’ vs. wange, except locally (Kretschmer, Wortgeogr. 100 ff.), etym. dub., perh. : OF bec ‘back’, ete. Walde- P. 2.148. Falk-Torp 41, 44. Or as ‘jaw’ fr. ‘eater’ fr. the root seen in Grk. gayerv ‘eat’, dayov ‘glutton’ and (Hesych.) ‘jaw’? So, after Much, Wei- gand-H. 1.136, Kluge-G. 33. But the sense ‘eat’ in Grk. is secondary.
```


## [2026-09-05T14:13:22.913Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Lyd\\.\" SYN.txt | head -20; echo \"=== 16.26/16.27\"; grep -n \"16\\.26 LOVE\\|16\\.27 \" SYN.txt | head",
 "description": "Search Buck for Lydian and love sections"
}
```


### [2026-09-05T14:13:22.973Z] TOOL RESULT

```
28061:Grk. ¢i\éw ‘love’ (have affection for), gidia ‘friendly love, friendship’, fr. dios ‘dear’, sb. ‘friend’, in Hom. also ‘one’s own’, this perh. the earliest sense and so fr. an Anatolian word represented by Lyd. bilis ‘one’s own’. Kretschmer, IF 45.267 ff.
=== 16.26/16.27
27433:16.27 Love (sb.; vb.)
28050:16.27 LOVE (sb.; vb.)
```


## [2026-09-05T14:13:27.043Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=28040 && NR<=28075' SYN.txt | grep -n \"1[01][0-9][0-9]\" | head; echo \"---\"; sed -n '28045,28062p' SYN.txt | cut -c1-300",
 "description": "Find printed page for Buck love section"
}
```


### [2026-09-05T14:13:28.597Z] TOOL RESULT

```
3:N T{EMPERAMENTAL, MORAL, AESTHETIC NOTIONS 1109
17:1110
32:Lat. venus ‘love, charm’ (but com- mon only in the personified Venus) § Skt. van- ‘seek, desire, gain’, Goth. wens ‘hope’, OF wyn, OHG wunna ea , bliss’, OHG wunscan, OF wyscan, = - ‘wish’ (16.61). Walde-P. 1.2588. ** nout-M. 1037.
---
Lett. ruotalat : ruotat ‘be dexterous, turn, hop’, also ‘loaf about’, refl. ‘tumble about, play’ : rats ‘wheel’, etc. Mliihl.- Endz. 583, 584.
6. ChSl. igratz ‘spring, dance’, later also play and so general modern Slavic (in part refl. in sense ‘play’ as a child), ef. ChSl. igri sb. ‘play’ (Supr.) : Skt. ej- ‘stir, move, quake, tremble’, ing- ‘stir, move’, ON etkenn ‘wild, raging’. Walde-P. 1.11. Berneker 422. Briic
7. Skt. krid-, prob. as *kriz-d- : Goth. -hrisjan, OF hrissan ‘shake’, Ir. cressaim ‘shake, swing’, fr. an extension of the root *(s)ker- in Grk. cxaipw ‘dance, hop, spring’, etc. Or as *kliz-d: Ir. cless
Walde-P. 1.527, 544.
feat, trick’ ?.
16.27 LOVE (sb.; vb.)
Walde-P. 2.572.
tous pila, cropyn; Goth. frijapwa; frijon Lith. meilé; myléti ae japwa; frij ; my ack Ayam de, ON dst, elska; elska, un- Lett. milestiba, miliba; mi- ) STEP nA, frja lét, mil’uot ot puras; dyad Dan. kerlighed, elskov; el- ChSl. Uuby; ljubite ih olga amare, ae aati SCr.  Yjubay; eit amore; amare
the adjs. for ‘dear’ are also cognate with the words for ‘love’ and so are included in the discussion here, though listed sepa- rately (16.28).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1110
Although there are sometimes dis- tinctive words for various aspects of love, especially sexual love vs. that of parents, children, friends, etc. (so most clearly in ancient Greek), it is more gen- erally true that the same word is used, any distinction depending upon the con- text.
1. IE *leubh- in words for ‘love, yearn for’, ‘dear’ (also ‘approve, praise, be- lieve’), etc.). Walde-P. 2.419. Walde- H. 1.793.
Here as the usual words for ‘love’ or ‘dear’. Gme. sbs. OE lufu, ME, NE love, OHG liubt, MHG, NHG liebe, Du. liefde; vbs. OF lufian, ME lovie, NE love, OHG liubon, MHG, NHG lieben; adjs. ‘dear’ Goth. liufs, ON yufr, OF leof, ME leve (NE lief), OHG liob, liub, MHG liep, NHG lieb, Du. lef;
2. Grk. épws, Hom. épos, with vb. Hom. papa, Att. épdw, all usually of sexual love, as likewise NG épwras, with vb. épwrebouar ‘fall in love’, épwyérn ‘sweetheart, mistress’, outside root con- nections dub. Walde-P. 1.144, Boi- sacq 270 f.
Grk. ¢i\éw ‘love’ (have affection for), gidia ‘friendly love, friendship’, fr. dios ‘dear’, sb. ‘friend’, in Hom. also ‘one’s own’, this perh. the earliest sense and so fr. an Anatolian word represented by Lyd. bilis ‘one’s own’. Kretschmer, IF 45.267 ff.
Grk. dyad, ‘love’ as ‘have regard or affection for’, ‘be fond or contented with’, etc., rarely of sexual love. Hence the late back-formation éyérn (first in
```


## [2026-09-05T14:13:32.964Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"syphilis\" KLN_1966.txt KLN_1971.txt | head -10",
 "description": "Grep Klein for syphilis"
}
```


### [2026-09-05T14:13:33.014Z] TOOL RESULT

```
KLN_1971.txt:107372:syphilis. — Medical L., fr. L. gummi. See gum, 
KLN_1971.txt:141039:syphilis. — L. lues, ‘a plague, pestilence’, prop, 
KLN_1971.txt:180645:origin. Cp. philander, Philemon, philter, syphilis. 
KLN_1971.txt:210103:syphilis {med.) — Medical L., fr. Gk. putroi;, 
KLN_1971.txt:211694:remedy against syphilis. — Coined by its inven- 
KLN_1971.txt:224552:pox’, i.e. syphilis. See small and pox. For sense 
KLN_1971.txt:227239:and the first element in sybotic, syphilis, Hyos- 
KLN_1971.txt:239644:syphilis, n., an infectious venereal disease. — 
KLN_1971.txt:239656:for syphilis. — See syphilis, 
KLN_1971.txt:239657:syphilology, n., the study of syphilis. — Com-
```


## [2026-09-05T14:13:34.597Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"philo-, *combining form\\|philo-\\b\" KLN_1971.txt | head -10; echo \"=== philosophy\"; grep -n \"philosophy, n\\.\" KLN_1966.txt KLN_1971.txt | head",
 "description": "Grep Klein for philo- and philosophy"
}
```


### [2026-09-05T14:13:34.664Z] TOOL RESULT

```
=== philosophy
KLN_1971.txt:180747:philosophy, n. — ME. philosophic, fr. OF. philo-
```


## [2026-09-05T14:13:37.195Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '239640,239660p' KLN_1971.txt; echo \"=== philos\"; sed -n '180635,180660p' KLN_1971.txt; echo \"=== philosophy\"; sed -n '180740,180760p' KLN_1971.txt",
 "description": "Read Klein entries syphilis, philo-, philosophy"
}
```


### [2026-09-05T14:13:37.299Z] TOOL RESULT

```
‘that which is stretched’. See tone and -y (repre- 
senting Gk. -ta). 

syphil-, form of sy philo- before a vowel, 
syphilis, n., an infectious venereal disease. — 
ModL., from the title of the work by Girolamo 
Fracastoro, Syphilis sive de morho Gallico {— 
Syphilis, or the French disease’), published at 
Verona in 1530; so named after the hero Syphi - 
lus, a shepherd whose name lit. means ‘friend of 
swine’, fr. Gk. cu? (gen. cuo<;) = tic, (gen. O05), 
‘swine’, and 91X05, ‘friend’. For the first ele- 
ment see sow, n., for the second see philo-. 
Derivatives: syphil-itic, adj., syphil-ize , tr. v., 
syphil-oid, adj., sy philo us (q.v.) 
syphilo-, before a vowel syphil-, combining form 
for syphilis. — See syphilis, 
syphilology, n., the study of syphilis. — Com- 
pounded of syphilo and Gk. -Xoyioc, fr. -Xoyo 5, 
‘one who speaks (in a certain manner) ; one who 
deals (with a certain topic)’. See -logy. 
=== philos
Philister. 

Derivatives: Philistine, adj., Philistin-ism , n. 

philo-, before a vowel phil-, combining form 
meaning ‘loving, fond of, interested in’, as in 
philosopher . — Gk. 91X0-, 91X-, fr. 9IX05, 
‘loved, beloved, dear’, as a noun, ‘friend’; later, 
in poetry, also used in an active sense, ‘loving, 
friendly’, whence 9iXelv, ‘to love’; of uncertain 
origin. Cp. philander, Philemon, philter, syphilis. 

Philoctetes, n., a famous archer, who killed Paris 
in the Trojan war with one of the poisoned ar- 
rows given him by Hercules ( Greek mythol) — 
L. Philoctetes , fr. Gk. <E>iXoxxy)T7)5, lit. ‘he who 
loves to possess’, fr. 9IX05, ‘beloved; lover’, and 



xxaop,at, ‘I get, acquire’. See philo- and check, 
‘sudden, stop’. 

Philodendron, n., a genus of plants of the arum 
family; (not cap.), any plant of the genus Philo- 
dendron (hot.) — ModL., compounded of philo- 
=== philosophy
philosophy and -ism and cp. sophism, 
philosophise n., a sophist. — F. philosophiste , 
formed fr. philosophic with suff. -iste. See phi- 
losophy and -ist and cp. prec. word, 
philosophize, intr. v. — See philosophy and -ize. 

Derivative: philosophiz-ation, n. 
philosophy, n. — ME. philosophic, fr. OF. philo- 
sophic, filosofiq (F .philosophic), fr. L .philosophia, 
fr. Gk. 9iXoao9La, ‘love of wisdom, philoso- 
phy’, fr. 91X600905, ‘lover 06 wisdom, philos- 
opher’. See philosopher and -y (representing Gk. 
Adi). 

Derivatives : philosoph-ize , intr. v., philosoph-iz - 
ation, n., philosoph-iz-er, n. 



-philous, combining form meaning ‘fond of’, as in 
ammophilous, entomophilous. — Gk. -91X05, fr.
```


## [2026-09-05T14:13:50.913Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Fracastoro\" KLN_1966.txt KLN_1971.txt | head; echo \"=== philharmonic\"; grep -n -i \"philharmonic\" KLN_1971.txt SKT.txt | head; echo \"=== Philadelphia\"; grep -n \"Philadelphia\" KLN_1971.txt | head -5; echo \"=== philanthropy/philology\"; grep -n \"philanthropy, n\\|philology, n\" KLN_1971.txt | head",
 "description": "Grep Klein for more entries"
}
```


### [2026-09-05T14:13:51.024Z] TOOL RESULT

```
KLN_1971.txt:239646:Fracastoro, Syphilis sive de morho Gallico {— 
KLN_1966.txt:37911:syphil-,  form  of  syphilo-  before  a  vowel, syphilis,  n.,  an  infectious  venereal  disease.  — ModL.,  from  the  title  of  the  work  by  Girolamo Fracastoro,  Syphilis  sive  de  morbo  Gallico  (  = Syphilis,  or  the  French  disease’),  published  at Verona  in  1530;  so  named  after  the  hero  Syphi- lus,  a  shepherd  whose  name  lit.  means  ‘friend  of swine’,  fr.  Gk.  oup  (gen.  auop)  =  up  (gen.  uop), ‘swine’,  and  tptAop.  ‘friend’.  For  the  first  ele¬ ment  see  sow,  n.,  for  the  second  see  philo-. Derivatives:  syphil-itic,  adj.,  syphil-ize,  tr.  v., syphil-oid,  adj.,  syphilous  (q.v.) syphilo-,  before  a  vowel  syphil-,  combining  form for  syphilis.  —  See  syphilis, syphilology,  n.,  the  study  of  syphilis.  —  Com¬ pounded  of  syphilo  and  Gk.  -Aoyta,  fr.  -Aoyop, ‘one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy.
=== philharmonic
KLN_1971.txt:180585:philharmonic, adj., loving music. — F. philhar- 
=== Philadelphia
26379:Benjamin Smith Barton of Philadelphia (died 
210632:History of Medicine, Philadelphia - Toronto, 
235789:ophy of the Human Voice , 4th ed., Philadelphia, 
267672:1818), professor of anatomy in Philadelphia. 
=== philanthropy/philology
180552:philanthropy, n. — Late L. philanthropia, fr. Gk. 
180676:philology, n. — F. philologie, fr. L. philologia , 
239657:syphilology, n., the study of syphilis. — Com-
```


## [2026-09-05T14:13:56.399Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '180583,180590p' KLN_1971.txt; echo \"=== philanthropy\"; sed -n '180552,180560p' KLN_1971.txt; echo \"=== philology\"; sed -n '180676,180684p' KLN_1971.txt",
 "description": "Klein philharmonic, philanthropy, philology"
}
```


### [2026-09-05T14:13:56.504Z] TOOL RESULT

```
philo-. 

philharmonic, adj., loving music. — F. philhar- 
monique, fr. It. filarmonico , fr. fil -, ‘phil-’, and 
armonico, fr. Gk. (xoc) apjxovixa, ‘theory of 
music’, neut. pi. of appiovixi^, ‘harmonious*. 

See phil- and harmonic. 
=== philanthropy
philanthropy, n. — Late L. philanthropia, fr. Gk. 
<piXav-&pca7rta, ‘love to mankind, humanity, 
benevolence, kind-heartedness’, fr^Xav-Ap 037*05. 
See philanthrope and -y (representing Gk. -la). 

philately, n., collection of stamps. — F. philatelies 
fr. phil- and Gk. ocxsXeia, ‘exemption from 
taxes’, fr. axeX^, Tree from taxes’, which is 
formed fr. a- (see priv. pref. -a) and X6X05, ‘end, 
=== philology
philology, n. — F. philologie, fr. L. philologia , 
‘love of learning, love of letters’, fr. Gk. 91X0- 
X6yla, fr. 9tXoXoyo5, ‘fond of learning’, which 
is compounded of 91X05, ‘beloved, loving’, 
and -Xoyo5, ‘one who speaks (in a certain man- 
ner) ; one who deals (with a certain topic)’. See 
philo- and -logy. 

Derivatives: philolog-er, n., philolog-ian , n.,
```


## [2026-09-05T14:13:57.503Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37890 && NR<=37915' KLN_1966.txt | grep -o \"15[0-9][0-9]\" | head; echo \"--- surrounding page numbers\"; sed -n '37900,37912p' KLN_1966.txt | cut -c1-160",
 "description": "Find KLN 1966 page number near syphilis"
}
```


### [2026-09-05T14:13:59.100Z] TOOL RESULT

```
1530
--- surrounding page numbers
synovia,  n.,  an  albuminous  fluid  secreted  by  cer¬ tain  glands  (anat.)  —  Medical  L.,  coined  by Paracelsus.
Derivative:  synovi-al,  adj. synovitis,  n.,  inflammation  of  the  synovial  mem¬ brane  (med)  —  Medical  L.,  formed  fr.  prec. word  with  suff.  -it
syntactical,  also  syntactic,  adj.,  pertaining  to  syn¬ tax.  —  ModL.  syntacticus,  fr.  Gk.  ouv- xaxxix6p,  ‘putting  together  in  order’,  fr. 
Derivatives:  syntactical-ly,  adv.,  syntactic-ian, n.
syntax,  n.  — -  F.  syntaxe,  fr.  Late  L.  syntaxis,  fr. Gk.  auvxafjip,  ‘a  putting  together,  a  putting  to¬ gether  of  words,  syntax’,  from
auvxaaaetv,  ‘to  put  together  in  order’,  fr.  auv (see  syn-)  and  xaaaetv,  ‘to  order,  arrange’.  See taxis  and  cp.  prec.  word.
synteresis,  n.,  innate  knowledge  of  right  and wrong.  —  ML.  synteresis,  fr.  Gk.  auvxrjpTjatp, ‘preservation’,  fr.  auvx7)peiv,  ‘to  preserv
synthetist,  n.,  a  synthesist.  —  Formed  with  suff. -ist  fr.  Gk.  auvS-Exop,  ‘put  together’.  See  prec. word.
synthetize,  tr.  and  intr.  v.,  to  synthesize.  —  Form¬ ed  with  suff.  -ize  fr.  Gk.  auvflcxop,  ‘put  to¬ gether’.  See  synthetic.
syntonic,  adj.,  pertaining  to,  or  placed  in,  reso¬ nance.  —  See  syntony  and  adj.  suff.  -ic. Derivatives :  syntonic-al,  adj.,  syntonic-al-ly 
Derivatives:  syntoniz-ation,  n.,  syntoniz-er,  n. syntony,  resonance.  —  Gk.  auvxovta,  ‘agreement’ fr.  auvxovop,  ‘in  harmony’,  lit.  ‘str
syphil-,  form  of  syphilo-  before  a  vowel, syphilis,  n.,  an  infectious  venereal  disease.  — ModL.,  from  the  title  of  the  work  by  Girolamo Fr
Derivative:  syphilolog-ist,  n.
```


## [2026-09-05T14:14:23.088Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['TAD'],ensure_ascii=False,indent=1))\"",
 "description": "TAD ref metadata"
}
```


## [2026-09-05T14:14:23.900Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فلسف\" TAD_pages.txt | head -20",
 "description": "Grep TAD for falsafa"
}
```


### [2026-09-05T14:14:24.522Z] TOOL RESULT

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
```


### [2026-09-05T14:14:24.557Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:14:27.229Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && wc -l TAD_pages.txt TAD.txt; grep -c \"\" TAD.txt; echo \"--- sample\"; head -30 TAD_pages.txt; echo \"=== grep loose\"; grep -n \"فلسفه\\|فيلسوف\\|فلسف\" TAD.txt | head",
 "description": "Inspect TAD text"
}
```


### [2026-09-05T14:14:27.294Z] TOOL RESULT

```
  3117 TAD_pages.txt
  3312 TAD.txt
  6429 total
3312
--- sample
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
=== grep loose
2145:فاسفة ل ونانى 11معه1] معناه حب المكة ومنه تقليف وفيلسوف
```


## [2026-09-05T14:14:32.522Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '2140,2150p' TAD.txt; echo \"=== find leaf in pages file\"; python3 - <<'EOF'\nimport re\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pages.txt').read()\nleaves=t.split('\\f')\nfor i,l in enumerate(leaves):\n    if 'فاسفة' in l or 'فلسفة' in l or 'وفيلسوف' in l:\n        print('leaf(0-based)',i, 'len',len(l))\n        print(l[:1500])\n        print('-----')\nEOF",
 "description": "Locate TAD falsafa page"
}
```


### [2026-09-05T14:14:34.305Z] TOOL RESULT

```
البس فى فسق جعتم ما فحق أن تدعى بفسقية 


اصع متت 
فاسفة ل ونانى 11معه1] معناه حب المكة ومنه تقليف وفيلسوف 


عام 5 8 
فلفل- لنظ هنديحيث منشأ هذا البات الذيحبه شديد الحراقة وف اسيفاة 

=== find leaf in pages file
leaf(0-based) 56 len 1967
                                  ‫متت‬    ‫اصع‬




           ‫فاسفة ل ونانى ‪11‬معه‪ ]1‬معناه حب المكةومنه تقليف وفيلسوف‬
       ‫‪8‬‬                                     ‫‪5‬‬                             ‫عام‬
 ‫فلفل‪ -‬لنظ هنديحيث منشأ هذا البات الذيحبه شديد الحراقة اوسفيفاة‬
‫آخر له قرونوف اليونانية ‪:‬مهم وهو فىجميم اللغاتبهذاالاسم‬               ‫‏‪ ْ٠‬تسمه وهونات‬
                                                                             ‫ما‬


 ‫فلين‪ -‬وناني ووااه؛ وهو شجر يثبه الاوط قشره ضخم سميك لين‬
                                                 ‫رخف يصنع منهالسداد والصمام‬


 ‫فليون ‪ -‬ايطالي وأهنوناوة! معناه ان صغير وبراد به عندنا الولد الذي محمله‬
                                                                 ‫االعلرامبعفمىودية‬
 ‫وف‬   ‫منار وبراد به المنارة والمشعل فوقبا وى النونانية ‪521‬‬   ‫تصحيف‬        ‫ذثار‬



  ‫الأطالقة م زفوهان انمد ف اهوخا اللمكورة اتاد وه‬
                                   ‫فى « فارس » وهي جزيرة بقرب الاسكندرية‬
              ‫فنجان ‪ -‬فارسي « فنجان وبتكان » وهو قدح صغير من خزف‬
 ‫فندق ‪ 5-3‬ونانيي متقطاء ‪0‬ل‪0‬هقم معناه يشبل اجميع وهو رك من ‪53‬م أي‬
                                     ‫‪0‬‬           ‫ع‬           ‫‪٠‬‬                       ‫‪1‬‏‬


                          ‫كل و نةصمطعمة أي قل واخذ مرادقه نل وميزل‬

      ‫تلضممانه‬
             ‫يلي‬
               ‫فبرس ‪ -‬فارسي نت ‪ 6‬وهو جدولمواد الكتاب ود‬
    ‫«ور » وهو لفظ فارسي قددم معناه ع‬
                                   ‫فوونت ليود عبراني ف‬
      
-----
```


## [2026-09-05T14:14:41.664Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && ls -la MON_part1.txt MON_part2.txt; echo \"=== falsafeh\"; grep -n \"فلسفه\" MON_part1.txt MON_part2.txt | head -5; echo \"=== syphilis\"; grep -n \"سیفیلیس\\|سفلیس\\|سيفيليس\" MON_part1.txt MON_part2.txt | head -5; echo \"=== philadelphia\"; grep -n \"فیلادلفیا\\|فيلادلفيا\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Grep Mo'in for the Persian words"
}
```


### [2026-09-05T14:14:41.753Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
=== falsafeh
MON_part1.txt:91:رشتة ادبیات و فلسفه و علوم تربیتی وارد گردید و در سال ۱۳۱۳ از این شعب 
MON_part1.txt:12948:قرون وسطی. (فل.) شعبه‌ای است از فلسفه 
MON_part1.txt:13366:حکمت اشراق: فلسفه‌ای که در اسلام مروج 
MON_part1.txt:52012:حادث در فلسفه بر دو معنی اطلاق شده: 
MON_part1.txt:53957:حقایق اشیا به قدر طاقت شری؛ فلسفه. 
=== syphilis
MON_part2.txt:1837:دور خر سیفیلیس و همچنین ضایعات 
MON_part2.txt:13406:علتش سیفیلیس ارثی با یکك عفونت حاد 
MON_part2.txt:33668:سیفیلیس و مدر و معرق و ضد کرم می‌باشد؛ 
MON_part1.txt:35870:سیفیلیس و سل و حصبه. چهارم حملة 
MON_part1.txt:48629:ضایعات سیفیلیسی و امراض عفونی دیگر 
=== philadelphia
```


## [2026-09-05T14:14:48.635Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"فلسفه \\[\\|فلسفه\\[\\|(فلسفه\\|فلسفة \\[\" MON_part1.txt MON_part2.txt | head -10; echo \"=== try 'فیلوسوفیا' / 'فیلسوف'\"; grep -n \"فیلوسوفیا\\|فیلسوف \\[\\|فیلسوف\\.\" MON_part1.txt MON_part2.txt | head -10; echo \"=== سیفیلیس headword\"; grep -n \"سیفیلیس \\[\\|سیفیلیس(\\|سیفیلیس \\.\" MON_part1.txt MON_part2.txt | head",
 "description": "Find Moin headword entries"
}
```


### [2026-09-05T14:14:48.725Z] TOOL RESULT

```
=== try 'فیلوسوفیا' / 'فیلسوف'
=== سیفیلیس headword
```


## [2026-09-05T14:14:51.580Z] TOOL CALL #34: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```


### [2026-09-05T14:14:51.589Z] TOOL RESULT

```


```


## [2026-09-05T14:14:58.043Z] TOOL CALL #35: Bash

```json
{
 "command": "ls site/pages/96.jpg 2>/dev/null; pdftoppm -f 96 -l 96 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg96 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 96"
}
```


## [2026-09-05T14:15:00.539Z] TOOL CALL #36: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%CF%86%CE%AF%CE%BB%CE%BF%CF%82",
 "prompt": "Give the full etymology section for Ancient Greek φίλος: what origin is proposed (Pre-Greek? Anatolian/Lydian bilis? PIE *bʰilo-?), which scholars (Beekes, Chantraine, Pokorny) are cited, and the meanings."
}
```


### [2026-09-05T14:15:00.936Z] TOOL RESULT

```
site/pages/96.jpg
total 30832
drwx------ 2 sfmqrb sfmqrb     4096 Sep  5 10:15 .
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
-rw-rw-r-- 1 sfmqrb sfmqrb     4811 Sep  5 02:00 bulca.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22149 Sep  5 01:51 c_belloth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30227 Sep  5 09:50 crop_ambor.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25024 Sep  5 09:50 crop_berijab_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb    39114 Sep  5 09:50 crop_berijan_ar.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65413 Sep  5 09:50 crop_persian_roast.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23219 Sep  5 01:51 c_schyth.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58057 Sep  5 02:29 e0full.json
-rw-rw-r-- 1 sfmqrb sfmqrb     4446 Sep  5 02:23 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   445959 Sep  5 01:37 hrn126_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1213019 Sep  5 01:37 hrn126.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   456157 Sep  5 01:37 hrn127_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1278807 Sep  5 01:37 hrn127.jpg
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
-rw-rw-r-- 1 sfmqrb sfmqrb 18949704 Sep  5 02:30 mw1872.htm
-rw-rw-r-- 1 sfmqrb sfmqrb     3057 Sep  5 10:05 patch87.py
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
-rw-rw-r-- 1 sfmqrb sfmqrb    78178 Sep  5 10:11 pg95.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72929 Sep  5 10:15 pg96.png
```


### [2026-09-05T14:15:07.401Z] TOOL RESULT

```
# Etymology of Ancient Greek φίλος

Based on the Wiktionary entry, here is what is proposed for the origin:

**Proposed Origin:**
The standard proposal derives φίλος from Proto-Indo-European *bʰil-o-s, composed of *bʰil- plus the athematic suffix *-os.

**Cognates:**
The entry identifies related words in Old Irish *bil* ("good, mild") and Proto-West Germanic *bil(i)* ("kind, gentle; decent, fair"), with descendants including Old English *bile-*, German *billig*, and Dutch *billijk*.

**Alternative View:**
Scholar Beekes presents a competing analysis. According to the text: "Beekes rejects the above etymology based on the original meaning of the Greek word apparently being 'own, accompanying' rather than 'beloved', and leaves the origin open."

**Scholar Citations:**
Only Beekes is explicitly mentioned by name in the etymology section, with a reference to his *Etymological Dictionary of Greek* (2010). Chantraine and Pokorny are not cited in this particular etymological discussion.

**Meanings:**
The adjective means "beloved" or "dear" primarily; less commonly "loving" or "friendly." As a noun, it means "friend."
```


## [2026-09-05T14:15:11.777Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg96.png"
}
```


### [2026-09-05T14:15:12.118Z] TOOL RESULT

```

```


## [2026-09-05T14:15:12.115Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-05T14:15:27.098Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && pdftoppm -f 96 -l 96 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg96_600 && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg96_600.png'); print(im.size)\n# crops based on 600dpi (scale from 200dpi image coords x3)\nim.crop((1200,3300,2200,3620)).save('c_anth.png')\nim.crop((1200,1750,2200,2000)).save('c_armonica.png')\nim.crop((1200,2450,2700,2620)).save('c_sus.png')\n\"",
 "description": "Crop key words at 600dpi"
}
```


### [2026-09-05T14:15:31.496Z] TOOL RESULT

```
(5100, 6600)
```


## [2026-09-05T14:15:38.789Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg96_600.png')\nim.crop((1300,3700,2400,3920)).save('c_anth.png')\nim.crop((1300,2020,2400,2240)).save('c_armonica.png')\nim.crop((1300,2780,2700,2950)).save('c_sus.png')\n\"",
 "description": "Recrop key words"
}
```


### [2026-09-05T14:15:40.788Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-05T14:15:42.483Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_anth.png"
}
```


### [2026-09-05T14:15:42.497Z] TOOL RESULT

```

```


## [2026-09-05T14:15:45.344Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/c_armonica.png"
}
```


### [2026-09-05T14:15:45.360Z] TOOL RESULT

```

```


## [2026-09-05T14:15:55.844Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/syphilis",
 "prompt": "Full etymology entry for syphilis: who coined it, in what language, what year, the shepherd Syphilus, and whether the name is explained as Greek sys 'swine' + philos 'loving' or as an alteration of Sipylus (Ovid)."
}
```


## [2026-09-05T14:15:58.104Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3%D9%81%D8%A9",
 "prompt": "Give the Arabic etymology of فلسفة (falsafa): from which Greek word, via Syriac?, relation to فيلسوف faylasūf, and the root ف ل س ف. Also list the Persian descendant if given."
}
```


### [2026-09-05T14:16:01.508Z] TOOL RESULT

```
# Etymology of Syphilis

The term "syphilis" originated in 1718 as Modern Latin, derived from a 1530 poem titled *"Syphilis, sive Morbus Gallicus"* by Veronese physician Girolamo Fracastoro. The poem tells of a shepherd named Syphilus, presented as the disease's first victim. Fracastoro later used the word generically for the disease in his 1546 medical treatise.

## Uncertain Origin of the Name

The true meaning behind Fracastoro's choice remains unknown. Scholars have proposed two main theories:

1. **Greek derivation**: A Latinized Greek term meaning "pig-lover," combining Latin *sus* (pig) with Greek *philos* (loving)

2. **Mythological reference**: An alteration of Sipylus, a character from Ovid's mythology as the son of Niobe

The etymological source remains speculative, with "the usual conjectures" remaining unresolved according to historical sources.
```


### [2026-09-05T14:16:03.402Z] TOOL RESULT

```
# Arabic Etymology of فلسفة (falsafa)

**Greek Origin:**
The word derives from Ancient Greek φιλοσοφία (philosophía), either directly or through the Arabic فَيْلَسُوف (faylasūf, "philosopher").

**Root:**
The term belongs to the Semitic root ف ل س ف (f l s f), with the word functioning as "the verbal noun of فَلْسَفَ (falsafa, 'to philosophize')."

**Persian Descendant:**
The entry lists Persian descendants including Iranian Persian: فَلْسَفِه (falsafe) and Dari: فَلْسَفَه (falsafa).

The Wiktionary entry does not explicitly mention Syriac as an intermediary language in the transmission chain, though it acknowledges the Greek source and notes the relationship to the فيلسوف form.
```


## [2026-09-05T14:16:26.946Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 bhili\"; grep -n \"bhili\\|bhilo\\|bili-catus\\|Bilicius\\|unbilithunga\" incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt | head -5; echo \"=== IEC bhilo\"; grep -n \"bhilo\\|bhili\" IEC.txt | head -5; echo \"=== SKT philosophy/philanthropy\"; grep -n \"^Philosophy\\|Philosophy,\\|Philanthropy\\|Philology\" SKT.txt | head -6",
 "description": "Grep WLD, Mann, Skeat"
}
```


### [2026-09-05T14:16:27.016Z] TOOL RESULT

```
=== WLD Bd2 bhili
11940:bhilo- etwa „in gutem Sinne ebenmaBig, angemessen, gut, freundlich“. 
=== IEC bhilo
1321:bhilios, io (?) (bhuilio-?). Cf. WP I, 830 Lat. filius, filia; Alb. bilé, bijé “daughter” (Umbr. filiu, feliuf, acc. pl. adj. = “sucking”. Cf. dhel-)
1322:bhilos (1) ‘good, fair, friendly, pleasant’. WP II, 185 Myc. piro- (*philo-); Gk. phílos; Ofr. bil (1) ‘fortunate’, MHG cf. un-bil (unfair, wrong"; also ‘unfairness’: G Unbill) beside MHG bil-lich, -liche “fair, fairness’. Cf. also MHG bil-wiz “household spirit’; OE bilewit *inno- cent, mild, pure'
1323:bhilos (2) ‘space, enclosure, rim’ Olr. bil ‘rim, of shield; W byl ‘brim’; ON bil, ds. bili, n. “interval”
1324:bhilos, us ‘timid’ Skt. bhirah ‘terrifying’; bhirüh ‘timid’; MHG bil “at bay’; cf. ON (*-1-) bila ‘give way, fail’
4185:gnabholos, om (gnabhilo-) ‘twist, strainer, tensile instrument Gk. gnáphalon "lock of hair; OHG knebil *gag'. Cf. gnabh-
=== SKT philosophy/philanthropy
```


## [2026-09-05T14:16:31.848Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11935,11960p' incoming/WLD/WLD_Bd2_1927_dli_106624_djvu.txt",
 "description": "Read WLD bhilo entry"
}
```


### [2026-09-05T14:16:31.895Z] TOOL RESULT

```
(und dann mit Ton verstrichenes und gebranntes) Gefa6“ erschlossen werden 
darf (s. Yf. LEWb.^ s. v.), ist bei deren lautreicher Vieldeutigkeit mindestens 
ganz fraglich. Sicher fern bleibt die europ. Sippe von dfc, Bottich^ s. Lit. 
bei Berneker 166, Yf. LE\Yb.^ 288 f. 

bhilo- etwa „in gutem Sinne ebenmaBig, angemessen, gut, freundlich“. 

Yermutlich gr. q)LXog „lieb, wert usw.‘‘ {cpdeoj „liebe“; liber andere 
Deutungen s. Johansson IF. 2, 7 m. Lit.); 

Ir. bit „gut'", gall. Bit- in vielen EN., wie ahd. bili- im 1. Gliede von Per- 
sonennamen; ahd. bil-lrih „ebenma6ig, angemessen, geziemend^^; mhd. 
bdewiz, btkvk „Kobold“ (eig. „guter Geisf') = ags. bile-wit „einfach, un- 
schuldig"'; Abstraktum in nhd. Unbilde f. (sg. TJnbdl ursprgl. schweiz.), 

mhd. unbilde^ nnbilede n. „Unrecht das Unbegreifliche, Ungeheuerliche, 
\Yunder“, as. unbilitlmnga „Unf6rmlichkeit, ungestaltes Ding‘‘; hieher 
vermutlich, als Ableitung eines Yerbums ^bildn und *biljan „angemessen 
darstellen*® ahd. bilotlii 18. Jhdt., biladi, bilidi, as. bilithi^ ndl. beeld^ nhd. 
Bild (s. fiber die genannten AYorte, sowie iiber dt. Weichbild Detier 
ZfdA. 42, 54. Kluge ® und Weigand-Hirt u. Bild, billig, Unbill, Weichbild ; 
eineWz, germ. *bil- der Bed. „schlagen, spalten, behauen“, die Meringer IF. 
18, 284 ff. fur unsere AYorte vertritt, scheint mir nicht ausreichend gestiitzt). 

Fick IP 175, Zup. G. 31; unannehmbar Fick III^ 269.
```


## [2026-09-05T14:16:38.607Z] TOOL CALL #46: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D9%81%D9%84%D8%B3%D9%81%D9%87",
 "prompt": "Quote Mo'in's (فرهنگ معین) entry for فلسفه verbatim, including any origin tag such as [يو.] (Greek) or [ع.] (Arabic) and the definition."
}
```


## [2026-09-05T14:16:39.941Z] TOOL CALL #47: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%DB%8C%D9%84%DB%8C%D8%B3/",
 "prompt": "Quote the فرهنگ معین (Mo'in) and any other dictionary entry for سیفیلیس, including the origin tag (e.g. [فر.] French) and definition."
}
```


### [2026-09-05T14:16:43.230Z] TOOL RESULT

```
# Mo'in Dictionary Entry for فلسفه

According to Farhang-e Mo'in, the entry for **فلسفه** (falsafa) is:

"(فَ لْ سَ فِ) [ع.] (اِ.) 1 - حکمت ، دانشی که موضوع آن هستی و وجود است . 2 - علت ، دلیل"

**Translation of key content:**
- The word originates from Arabic [ع.]
- **Definition 1:** Wisdom; knowledge whose subject is being and existence
- **Definition 2:** Cause; reason
- Additional note: The phrase "~ بافی" is an idiomatic expression alluding to reasoning that strays from logic
```


### [2026-09-05T14:16:46.641Z] TOOL RESULT

```
I appreciate your request, but I need to be transparent about a limitation: the web page content provided does not include an entry from **فرهنگ معین (Mo'in dictionary)**. 

The page only contains:

1. **A Persian language definition** labeled as "فرهنگ فارسی" (Persian language dictionary):
   - "مرضی عفونی و ساری که به ارث به طور مادرزادی به افراد منتقل میشود..." (an infectious contagious disease that can be transmitted hereditarily...)

2. **Synonyms** from various English sources (pox, lues, syphilis, old joe, pip)

To provide the specific Mo'in dictionary entry you've requested, I would need access to content that actually contains that reference. The current page mentions Mo'in's dictionary as part of Abadis's resources, but doesn't reproduce its entry for سیفیلیس.
```


## [2026-09-05T14:16:51.305Z] TOOL CALL #48: WebFetch

```json
{
 "url": "https://vajehyab.com/moein/%D8%B3%DB%8C%D9%81%DB%8C%D9%84%DB%8C%D8%B3",
 "prompt": "Quote Mo'in's entry for سیفیلیس verbatim, including the origin tag (e.g. [فر.]) and definition. If no Mo'in entry, say so and quote whatever dictionary entry is shown."
}
```


## [2026-09-05T14:16:52.114Z] TOOL CALL #49: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/philharmonic",
 "prompt": "Full etymology of philharmonic: date, French philharmonique, Italian filarmonico, Greek elements. Also anything on Philadelphia and Philip if shown."
}
```


### [2026-09-05T14:16:54.232Z] TOOL RESULT

```
The server returned HTTP 500 Internal Server Error.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-05T14:17:02.278Z] TOOL RESULT

```
# Etymology of "Philharmonic"

**Date of Origin:** 1813, appearing in the name of a London society founded to promote instrumental music.

**Language Journey:**
The word traveled through multiple languages before reaching English:
- **French:** *philharmonique* (1739)
- **Italian:** *filarmonico*
- **Greek roots:** *philos* ("loving") + *ta harmonika* ("theory of harmony, music")

**Meaning:** The term literally translates to "loving harmony or music," combining the Greek prefix for affection with musical concepts.

**Historical Impact:** "The Society name was taken up in the names of many symphony orchestras," establishing philharmonic as a designation for musical organizations.

---

**Regarding Philadelphia and Philip:** The provided content does not include etymological information for these names, though they appear in the alphabetical navigation menu of related dictionary entries.
```


## [2026-09-05T14:17:13.105Z] TOOL CALL #50: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Philadelphia",
 "prompt": "Full etymology of Philadelphia: the ancient Lydian city, Greek philadelphos 'brotherly love' (philos + adelphos), Attalus II Philadelphus, and William Penn's 1682 naming of the Pennsylvania city."
}
```


### [2026-09-05T14:17:17.638Z] TOOL RESULT

```
# Etymology of Philadelphia

The name Philadelphia comes from Greek, meaning "brotherly love." William Penn selected this name when founding the Pennsylvania city, deriving it from *philos* ("loving") and *adelphos* ("brother").

The name also references an ancient city in Lydia, mentioned in the New Testament. That city was named after King Attalos II Philadelphos of Pergamon (2nd century B.C.E.), whose title meant "loving the brethren" or referred to his affection for his brother Eumenes.

**Philadelphia lawyer:** This term, meaning a shrewd attorney, dates to 1788 in London. It reportedly originated from Andrew Hamilton, who secured the famous acquittal of publisher J.P. Zenger on libel charges in 1735.
```


## [2026-09-05T14:17:19.262Z] TOOL CALL #51: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%CF%86%CE%AF%CE%BB%CE%BF%CF%82' --note 'page 96, root Bhili/Bhilo, node #1: Ancient Greek philos etymology (PIE *bhil-o-s vs Beekes Pre-Greek)' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/syphilis' --note 'page 96, node #16/#18: syphilis, Fracastoro 1530, sus+philos vs Sipylus' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3%D9%81%D8%A9' --note 'page 96, node #3/#4: Arabic falsafa < Greek philosophia / faylasuf' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://www.etymonline.com/word/philharmonic' --note 'page 96, node #8/#12: philharmonic < Fr philharmonique < It filarmonico' 2>&1 | tail -3; python3 tools/fetch_source.py 'https://vajehyab.com/moein/%D9%81%D9%84%D8%B3%D9%81%D9%87' --note 'page 96, node #4: Moin entry falsafe [ع.]' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-05T14:17:21.826Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/326312e1306628ec.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/929b3cc8044d4049.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5b2da7c6ca99911b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f9183e473e9f9851.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/650b6f4eb3c32ef7.txt
```


## [2026-09-05T14:17:26.393Z] TOOL CALL #52: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://www.etymonline.com/word/Philadelphia' --note 'page 96, node #12/#13: Philadelphia, Greek philadelphos, Attalus II, William Penn 1682' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%DB%8C%D9%84%DB%8C%D8%B3/' --note 'page 96, node #17: Persian sifilis, Farhang-e Farsi definition' 2>&1 | tail -2; python3 tools/fetch_source.py 'https://www.etymonline.com/word/philosophy' --note 'page 96, node #5-#7: philosophy Latin>Old French>English chain' 2>&1 | tail -2",
 "description": "Archive more sources"
}
```


### [2026-09-05T14:17:29.350Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/51c426790b4568a1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/084bb9a3566b6ce9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2f4eac4bd537b366.txt
```


## [2026-09-05T14:17:32.669Z] TOOL CALL #53: Bash

```json
{
 "command": "head -40 /home/sfmqrb/git/rishe/data/verification/sources/web/2f4eac4bd537b366.txt",
 "description": "Read archived etymonline philosophy"
}
```


### [2026-09-05T14:17:32.710Z] TOOL RESULT

```
URL: https://www.etymonline.com/word/philosophy
FETCHED: 2026-09-05T14:17:29Z
STATUS: 200
TITLE: Philosophy - Etymology, Origin & Meaning

Philosophy - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of philosophy 

 philosophy (n.) 

 c. 1300, philosophie , "knowledge, learning, scholarship, scholarly works, body of knowledge," from Old French filosofie "philosophy, knowledge" (12c., Modern French philosophie ) and directly from Latin philosophia, from Greek philosophia "love of knowledge, pursuit of wisdom; systematic investigation," from philo- "loving" (see philo- ) + sophia "knowledge, wisdom," from sophis "wise, learned;" a word of unknown origin [Beekes]. With many spelling variants in Middle English ( filozofie, phelosophie , etc.).

 From mid-14c. as "the discipline of dealing in rational speculation or contemplation;" from late 14c. as "natural science," also "alchemy, occult knowledge;" in the Middle Ages the word was understood to embrace all speculative sciences. The meaning "system a person forms for conduct of life" is attested from 1771. The modern sense of "the body of highest truth, the science of the most fundamental matters" is from 1794.

 Nec quicquam aliud est philosophia, si interpretari velis, praeter studium sapientiae; sapientia autem est rerum divinarum et humanarum causarumque quibus eae res continentur scientia. [Cicero, 
 "De Officiis" ]

 In 1744 he made an unsuccessful attempt to obtain a professorship at Edinburgh; having failed in this, he became first a tutor to a lunatic and then secretary to a general. Fortified by these credentials, he ventured again into philosophy. [Bertrand Russell, writing of Hume, in "A History of Western Philosophy," 1945]

 [Philosophical problems] are, of course, not empirical problems; but they are solved through an insight into the workings of our language, and that in such a way that these workings are recognized — 
 despite an urge to misunderstand them. The problems are solved, not through the contribution of new knowledge, rather through the arrangement of things long familiar. Philosophy is a struggle against the bewitchment (
 Verhexung ) of our understanding by the resources of our language. [Ludwig Wittgenstein, "Philosophical Investigations," 1953]

 also from c. 1300 

 Entries linking to philosophy
```


## [2026-09-05T14:17:39.755Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== SKT philo\"; grep -n -i \"philosophy\\|philanthropy\\|philology\" SKT.txt | head -5; echo \"=== WEB philadelphia/philharmonic\"; grep -n -i \"philharmonic\" WEB_vol1.txt FSD_vol3.txt 2>/dev/null | head -5; echo \"=== FSD syphilis\"; grep -n -i \"syphilis, n\" FSD_vol4.txt | head -3",
 "description": "Grep Skeat, Webster, Funk&Wagnalls"
}
```


### [2026-09-05T14:17:39.843Z] TOOL RESULT

```
=== SKT philo
13906:philology.  6tudy  of  languages.  (I*  — "[.)  h,  phiiahgia.^Gk..  tptKoKoyia,  love 'ditcoune,  love  of  literature  and  language. »Gk  ^AuAoTOf,  foDd  of  discourse ;  aUo, iftlndcut  of  literaLure  and  langaage.  — Gk. iv't.    fond   of;  A^ai,   di&cour^    from
13908:philosophy,  love  of  wisdom.  (F.— L.
22203:[>Dc  XRfxtt  word  of  wvming  moy  perhaps  suffice.  If  we  wish  to  ondentand  a  suffix, most  employ  comparative  philology,  and  not  consider  English  as  an  absolutely
=== WEB philadelphia/philharmonic
=== FSD syphilis
```


## [2026-09-05T14:17:42.309Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '13900,13915p' SKT.txt; echo \"=== FSD grep syphilis loose\"; grep -n -i \"syphilis\" FSD_vol4.txt | head -5",
 "description": "Skeat philo entries and FSD syphilis"
}
```


### [2026-09-05T14:17:42.376Z] TOOL RESULT

```
Pheasant,  a  bird.  (F.  —  U  «* Formed  wit  h  cxcresccot  /  ( after  m)  bxm /esawt,  a  pheasant  —  O.  F.  ySi phasiana,  a  pheasant ;  put  for auiit  Phasian  bird.  —  G|c. pheasant,  lit.  Phasian,  i,e- the  river  Pkasis  in  t.'olchlt.
Phenlx.     Phoonlx.    (L.  - phatnix.  —  Gk.  ^oTct^.  a  phomta 73).  Perhaps  nametl  frovn  iu  \ like  that  produced  by  the
PHRENOLOGY.
547
Fhenomenon ;  sec  Phantom. Phial,  Vial.  (F.-L.-Gk.)  Formerly vmA  tiaJi,  viol,  ftllered  to  phtal  in  mmtem edidous  of  Shakespeare.  — O.  K. /^iWr,  *a »tol!.*  Cot.  (Mod.  F.  /tf/0 -L-  /^('o/rt. >Ck.  (^<iA.ii,  R  broad,  6at,  shallow  cup  or rl  (now  AppUed  to  «  small  bottle). lanthropy,  love  of  mafikind.  (L.— nk.)  L,  fhiianthr^ia.^OV.  <pt\av€fKitwia, tcPfCTolcDce.  —  Gk.  ^Aa^f^a^rot,  loving kL  »  Gk.  fMX<.  for  ^'A-or,  frieodly. Av4fivwoi,  A  tnan. ihUharmonic,  loving  mnsic.  (Gk.) Gk.  ^/A-of,  frienftly,  fond  of;  and  L. i>4  •  Gk.  Apfioviof  bannony ;  see lony.
^philippic,  a  diKoune  fuU  of  invective. ,-Gk.)     L. Pkilippicum,  pi. Philipfica, to  denote  the  celebrated  orations  of lOKthenesagamst  Philip.  — Gk.^iTiror, ilip ;  lit.  '  a  lovci  of  bones.*  — Gk.  f^A-ot, '  of :  fvvor.  a  horse,
philology.  6tudy  of  languages.  (I*  — "[.)  h,  phiiahgia.^Gk..  tptKoKoyia,  love 'ditcoune,  love  of  literature  and  language. »Gk  ^AuAoTOf,  foDd  of  discourse ;  aUo, iftlndcut  of  literaLure  and  langaage.  — Gk. iv't.    fond   of;  A^ai,   di&cour^    from
to  speak.
philosophy,  love  of  wisdom.  (F.— L.
»Gk.)    M.  E./Ai7ajff/Ai>.  -  Y.philosophu,
»1^  ^i/ofi>/Ab].«-Gk.  ^XoGo^a,   love  of
—  Glc  ^iKiao^.   loving  know*
t.«Gk,  tf>iXo-t,  fond  of;  iro^^Sf,  sJcilltil,
iktU;  tct   Sophlot.      Der.  fAi/o-
by  addiug  r  to  M.  E.  phihsophtt
rrprcMiits  F.  phUaupht^  L.  pAihso-
=== FSD grep syphilis loose
1599:sal-var'san,  1   sal-vur'son,  2   sM'var'san,  n   A   compound Invented  by  Lhrllch  for  the  treatment  of  mlcrobic  diseases caused  by  spirilla,  such  as  syphilis,  recurrent  fe\cr,  fram- bCEsla,  etc  popularly  known  ns  606  Sec  cHEMOTiiERAPr SaV'va-ticr'ra,  1   BQrvo-tyer'ro.  2   sal  va-tylr’ra,  n   A   city In  Guanajuata  state  S   central  Mexico 6aM action,  1   sal-v  '^f.n,2  8   l-va'ahon,  n   1.  The  proc- ess or  state  of  being  saved,  deliverance  or  preservation from  e^'il  or  destruction,  as,  the  saltation  of  a   vessel
10402:A   Scottish  naturalist  and  antiquarian SIb'be-cbal,  1   slb'i-kal  or  slbl-k^'o!,  2   slb'e-cl  orslb'e^ff,  n Bib  2Samxxl,18  Slb'be-calt  (R  V ). slb-ben'dy,n  (E  Ind]  SameassEBUNnr slb'bCDS,  I   sib'enz,  2   sib'ens,  n   1.  [Scot]  A   form  of syphilis  with  skln-eniptlons  resembling  Ae  raspberry, formerly  endemic  to  Scotland  2   (Orkneys  J   The  Itch  (<
13694:—   8   (Slow,  a   Slow  as  a   snail  —   s   (track,  n   Ulcerations that  occur  In  continuous  patches  In  the  throat  In  secondary syphilis  — s   (trefoil,  n   Same  as  snail-clover —s.* wa- ter, n   Water  In  which  calcined  snail-shells  have  been Infused  anciently  used  as  a   remedy  —   s   -wheel,  n   In some  striking  timepieces  a   rotating  piece  with  a   spiral periphery  having  notches  so  arranged  as  to  determine  the number  of  strokes  made  on  the  bell  —   white  s   ,   the  common edible  snail  (Helix  pomalia)  —   snalldlke,  a   A   adv  Like  a snail,  slow, slowly  snalFj:
16169:ease  that  has  a   determinate  course  and  succession  of  phe- nomena, and  Is,  due  to  some  distinct  and  definite  cause,  as syphilis  or  Itch  — s   dut>*  see  duty,  5   —   8.  lien,  same  as particular  lien  — s   magnetic  rotation,  sec  magnetic ROTATION  —   s   name,  the  name  of  a   species  that  pan  of the  scientific  name  of  an  animal  or  plant  which  designates the  species  to  which  It  belongs  It  always  follows  the generic  name,  and  begins  with  a   small  letter  —   s.  refrac* tfve  power,  same  as  specific  REFRAcrn'E  energy- s*
19030:relapsing  fever  [<  spuio- -I- Gr  chaff?,  bristle  1   Spl^ro- cbm'te;  —Splrochaeta  pallida,  tbe  germ  of  syphilis,  now known  as  TrepoftmaraKWum  — spl''ro^ha?-to'sIs,  n   A disease  of  fowls  due  to  splrochata  Sec  plate  of  b   vctcria.— Spl"ro-d^a,s  Bot  AgenusofsmaUfloatlngaqnaticplants of  the  family  Lemnacex  They  have  a   disl  -shaped  thallua with  one  or  more  roots,  very  nidimcntary  Icav  es,  and  a   aao Hke  spathe  5   poljThiza  Is  the  greater  duckweed  [< SPIRO-  -i-  Gr  cWor,  form]  — 8pI"ro-go-nIm'l-uin,  n   Box Same  as  speipogommium
```


## [2026-09-05T14:17:52.032Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"Fracastor\\|syph'i-lis\\|syphl-lis\\|Syphilus\" FSD_vol4.txt WEB_vol1.txt KLN_1966.txt 2>/dev/null | head -5; echo \"=== ARY latin index philos\"; grep -n -i \"PHILOS\\|PHILO\" incoming/ARY/ARY_latin_index_pages.txt | head -5",
 "description": "More greps: FSD, Webster, Aryanpur"
}
```


### [2026-09-05T14:17:52.110Z] TOOL RESULT

```
KLN_1966.txt:37911:syphil-,  form  of  syphilo-  before  a  vowel, syphilis,  n.,  an  infectious  venereal  disease.  — ModL.,  from  the  title  of  the  work  by  Girolamo Fracastoro,  Syphilis  sive  de  morbo  Gallico  (  = Syphilis,  or  the  French  disease’),  published  at Verona  in  1530;  so  named  after  the  hero  Syphi- lus,  a  shepherd  whose  name  lit.  means  ‘friend  of swine’,  fr.  Gk.  oup  (gen.  auop)  =  up  (gen.  uop), ‘swine’,  and  tptAop.  ‘friend’.  For  the  first  ele¬ ment  see  sow,  n.,  for  the  second  see  philo-. Derivatives:  syphil-itic,  adj.,  syphil-ize,  tr.  v., syphil-oid,  adj.,  syphilous  (q.v.) syphilo-,  before  a  vowel  syphil-,  combining  form for  syphilis.  —  See  syphilis, syphilology,  n.,  the  study  of  syphilis.  —  Com¬ pounded  of  syphilo  and  Gk.  -Aoyta,  fr.  -Aoyop, ‘one  who  speaks  (in  a  certain  manner);  one  who deals  (with  a  certain  topic)’.  See  -logy.
FSD_vol4.txt:29316:It  appears  In  three  stages  (1)  primary  syphilis,  the stage  In  which  the  manifestations  are  limited  to  the  part first  Inoculated  and  the  adjacent  glands,  (2)  secondary 8   ,   In  which  It  manifests  Itself  on  the  skin  and  mucous membranes,  and  (3)  tertiary  s   ,   in  which  It  spreads  its corrosive  effects  to  muscles,  bones,  and  brain IF  ,   <   SyphUus,  name  of  a   shepherd  In  "   Syphilus,  slve Morbus  Galllcus  ’*  a   poem  by  Fracastorio,  <   Gr  sys, swine  +   Philos  loving  ]— hereditary  syphilis,  constitu- tional syphllLs  communicated  during  fetal  life  from  parental taint  —   syph"l-IeI-co*sIs,  n   Syphilitic  ulceration  —   sj  ph*-
=== ARY latin index philos
```


## [2026-09-05T14:18:02.455Z] TOOL CALL #57: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'))\nprint(d['KLN']['page_offset']); print(d['KLN'].get('lookup_hint'))\nprint('AHD offset:', d['AHD'].get('page_offset'), d['AHD'].get('lookup_hint'))\n\"",
 "description": "KLN and AHD page offsets"
}
```


### [2026-09-05T14:18:04.459Z] TOOL RESULT

```
KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
AHD offset: 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru-' ; entries list English derivatives in caps. Restricted 1970s AHD scans on IA (lending only, djvu.txt returns 401): americanheritage0000dict (July 1977 printing, 970 leaves - probably the New College Edition), bwb_P9-BHZ-437 (1974), americanheritage00nyde (1970), bwb_W9-CSW-086 (1969, 1610 leaves = original 1969 ed.).
```


## [2026-09-05T14:18:08.115Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nt=open(p).read()\nidx=t.find('Girolamo')\nleaf=t.count('\\f',0,idx)\nprint('leaf(0-based)',leaf,'-> approx printed pages', 2*(leaf-12), 2*(leaf-12)+1)\nEOF",
 "description": "Compute Klein page for syphilis"
}
```


### [2026-09-05T14:18:11.119Z] TOOL RESULT

```
leaf(0-based) 827 -> approx printed pages 1630 1631
```


## [2026-09-05T14:18:19.910Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\np='/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt'\nleaves=open(p).read().split('\\f')\nfor i in (790,792,794,827):\n    l=leaves[i]\n    print('== leaf',i, repr(l[:160]))\nEOF",
 "description": "Inspect Klein leaves near 1561"
}
```


### [2026-09-05T14:18:21.729Z] TOOL RESULT

```
== leaf 790 'ument  for  meas¬ uring  blood  pressure  in  the  arteries.  —  Com¬ pounded  of  sphygmo-  and  manometer, sphygmometer,  n.,  an  instrument  for  measuring '
== leaf 792 '  despite.\nDerivatives:  spite,  tr.  v.,  spite-ful,  adj.,  spite-ful- ly,  adv.,  spite-ful-ness,  n. spittle,  n.  —  ME.  spetil,  fr.  OE.  spxtl,  spatl,'
== leaf 794 'a  with  the  dimin.  suff.  -ala. See  spore  and  -ule.\nspot,  n.  —  ME.  spotte,  spot,  rel.  to  MDu.  spot, spotte,  ‘stain,  blot’,  ON.  spotti,  ‘smal'
== leaf 827 'cogn.  with  L.  dicere,  ‘to  show,  tell’.  See diction  and  words  there  referred  to  and  cp.  esp. dicast.\nDerivatives:  syndic-al,  adj.,  svndi-cal-is'
```


## [2026-09-05T14:18:31.792Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nt=open('KLN_1966.txt').read(); print('leaves', t.count('\\f')+1)\"",
 "description": "Count Klein leaves"
}
```


### [2026-09-05T14:18:34.830Z] TOOL RESULT

```
leaves 903
```


## [2026-09-05T14:19:24.073Z] TOOL CALL #61: Bash

```json
{
 "command": "tail -8 data/verification/sources/web/index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('url'))\n\"; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg96.png data/verification/sources/refs/ocr/BOOK/96.png && ls -la data/verification/sources/refs/ocr/BOOK/ | tail -3",
 "description": "Check archived URLs and copy page PNG"
}
```


### [2026-09-05T14:19:25.790Z] TOOL RESULT

```
https://en.wiktionary.org/wiki/%CF%86%CE%AF%CE%BB%CE%BF%CF%82
https://www.etymonline.com/word/syphilis
https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3%D9%81%D8%A9
https://www.etymonline.com/word/philharmonic
https://vajehyab.com/moein/%D9%81%D9%84%D8%B3%D9%81%D9%87
https://www.etymonline.com/word/Philadelphia
https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%DB%8C%D9%84%DB%8C%D8%B3/
https://www.etymonline.com/word/philosophy
-rw-rw-r-- 1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
```


## [2026-09-05T14:19:28.273Z] AGENT

Now I'll write the verification file.


## [2026-09-05T14:35:28.624Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk96.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_PHILOS = \"https://en.wiktionary.org/wiki/%CF%86%CE%AF%CE%BB%CE%BF%CF%82\"\nE_SYPH   = \"https://www.etymonline.com/word/syphilis\"\nW_FALS   = \"https://en.wiktionary.org/wiki/%D9%81%D9%84%D8%B3%D9%81%D8%A9\"\nE_PHILH  = \"https://www.etymonline.com/word/philharmonic\"\nV_FALS   = \"https://vajehyab.com/moein/%D9%81%D9%84%D8%B3%D9%81%D9%87\"\nE_PHILA  = \"https://www.etymonline.com/word/Philadelphia\"\nA_SIF    = \"https://abadis.ir/fatofa/%D8%B3%DB%8C%D9%81%DB%8C%D9%84%DB%8C%D8%B3/\"\nE_PHILO  = \"https://www.etymonline.com/word/philosophy\"\n\nPOK_SUP = {\"ref\": \"POK:153\", \"status\": \"supports\",\n \"note\": \"POK_01.txt (leaf with the printed page-number 154 immediately after it) s.v. 'bhili-, bhilo-': „bhili-, bhilo- ,ebenmaßig, angemessen, gut, freundlich‘“ — exactly Nourai's root name, language label and gloss. English Pokorny (POK_full.txt, 'Root / lemma: bʰili-, bʰilo-, Meaning: harmonious, friendly, Page(s): 153-154').\"}\n\nnodes = []\n\ndef N(i, lang, words, verdict, deriv, deriv_fa, sources, refs, cons, extra=None):\n    d = {\"id\": i, \"lang\": lang, \"words\": words, \"verdict\": verdict,\n         \"derivation\": deriv, \"derivation_fa\": deriv_fa,\n         \"sources\": sources, \"ref_check\": refs, \"consulted\": cons}\n    if extra:\n        d.update(extra)\n    nodes.append(d)\n\n# ---------------- node 1 ----------------\nN(1, \"Greek\", \"philos\", \"plausible\",\n  \"Greek φίλος 'dear, beloved', as a noun 'friend' (Homeric also 'one's own'), whence φιλέω 'I love' and φιλία 'friendship'; Nourai's gloss 'love' is loose — the word is an adjective/noun, 'love' is φιλία. The derivation from the root is the traditional one (*bʰil-o-s > φίλος with regular IE *bʰ > Gk. φ and thematic *-o-s > -ος, cognate with OIr. bil 'good', OHG bili-/billih 'fitting, fair', NHG billig, Unbill), and Mann even adds Mycenaean pi-ro- = *philo-. But Pokorny himself does NOT list φίλος among the descendants: on p.154 he only reports Kretschmer's rival view (IF 45.267 ff.) that it is an Asianic/Anatolian word matching Lydian bilis 'his own', with Loewe against. Watkins hedges ('Possible source of Greek philos'), Klein calls it 'of uncertain origin', and Beekes rejects the IE etymology altogether because the oldest sense is 'own, accompanying' rather than 'beloved', leaving the origin open. So the arrow is one accepted scholarly option, not consensus.\",\n  \"«فیلوس» (φίλος) در یونانی باستان صفت است به معنی «عزیز، دوست‌داشتنی» و در کاربرد اسمی «دوست»؛ پس معنایی که نورایی آورده («love») دقیق نیست و معادل φιλία است. ریشه‌شناسی سنتی آن را از هندواروپایی آغازین *bʰil-o-s می‌گیرد (ب‌ میان‌دمیدهٔ هندواروپایی در یونانی به ف بدل می‌شود)، هم‌ریشه با ایرلندی میانه bil «خوب» و آلمانی بالای کهن billih. اما خود پوکورنی در صفحهٔ ۱۵۴ این واژه را جزء بازمانده‌های ریشه نیاورده و تنها نظر کرچمر را نقل کرده که آن را وام‌واژه‌ای آسیایی (لیدیایی bilis) می‌داند؛ بیکس نیز ریشهٔ هندواروپایی را رد می‌کند. بنابراین ادعای نورایی با احتیاط پذیرفتنی است.\",\n  [W_PHILOS],\n  [{\"ref\": \"POK:154\", \"status\": \"partial\",\n    \"note\": \"POK_01.txt, page printed '154' at the head of the paragraph: 'Gr. φίλος ,lieb, wert‘ usw. stellt Kretschmer (IF. 45, 267 f.) als [klein]griechisch zu lyd. bilis ,sein‘; dagegen Loewe aaO., der die Betonung [der] ersten Silbe aus dem Vokativ erklärt.' The page Nourai cites therefore records the φίλος question but does NOT assert the derivation from bhili-; it presents the Anatolian alternative.\"}],\n  [{\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. bhilo-\", \"stance\": \"partial\",\n    \"note\": \"'bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153.]' — 'Possible source' is a hedge.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, bhilos (1)\", \"stance\": \"supports\",\n    \"note\": \"IEC.txt: 'bhilos (1) ‘good, fair, friendly, pleasant’. WP II, 185  Myc. piro- (*philo-); Gk. phílos; OIr. bil (1) ‘fortunate’, MHG cf. un-bil … bil-lich' — Mann explicitly puts Greek philos (and Mycenaean pi-ro-) under the root.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. philo-\", \"stance\": \"partial\",\n    \"note\": \"KLN_1971.txt: 'philo-, before a vowel phil- … Gk. φιλο-, φιλ-, fr. φίλος, “loved, beloved, dear”, as a noun, “friend” … of uncertain origin.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck p.1110 (16.27 LOVE)\", \"stance\": \"contradicts\",\n    \"note\": \"'Grk. φιλέω ‘love’ … fr. φίλος ‘dear’, sb. ‘friend’, in Hom. also ‘one’s own’, this perh. the earliest sense and so fr. an Anatolian word represented by Lyd. bilis ‘one’s own’. Kretschmer, IF 45.267 ff.'\"},\n   {\"src\": \"WLD\", \"where\": \"Bd. II p.185\", \"stance\": \"partial\",\n    \"note\": \"'bhilo- etwa „in gutem Sinne ebenmaßig, angemessen, gut, freundlich“. Vermutlich gr. φίλος „lieb, wert usw.“' — 'vermutlich' = presumably, i.e. not certain.\"}])\n\n# ---------------- node 2 ----------------\nN(2, \"Greek\", \"philo-sophos\", \"confirmed\",\n  \"Greek φιλόσοφος 'lover of wisdom' = φίλος + σοφός 'wise, skilled' (a word Beekes calls of unknown origin), an ordinary Greek determinative compound with the linking vowel -o- of the first member; attested from Herodotus (1.30) and Heraclitus onward, and made a technical term by Plato, with the abstract φιλοσοφία. The formation is inner-Greek and uncontroversial.\",\n  \"یونانی φιλόσοφος (philosophos) «دوستدار حکمت» ترکیبی است از philos «دوستدار» و sophos «دانا، فرزانه» با میانوند -o- که در ترکیب‌های یونانی معمول است. این واژه از هرودوت و هراکلیتوس به بعد گواهی شده و افلاطون آن را اصطلاح فلسفی کرد. ساخت واژه درون‌یونانی و بی‌چون‌و‌چرا است؛ ادعای نورایی درست است.\",\n  [E_PHILO],\n  [{\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"KLN_1971.txt s.v. philosophy: 'fr. Gk. φιλοσοφία, “love of wisdom, philosophy”, fr. φιλόσοφος, “lover of wisdom, philosopher”.'\"},\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. bhilo- lists PHILO- among the English reflexes of Greek philos; the compound philosophos is the standard example of the combining form.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philosophy / philo-\", \"stance\": \"supports\",\n    \"note\": \"'philo-, before a vowel phil-, combining form meaning “loving, fond of, interested in”, as in philosopher.'\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philosophy\", \"stance\": \"supports\",\n    \"note\": \"'philosophy, love of wisdom. (F.—L.—Gk.) … Gk. φιλοσοφία, love of … Gk. φιλόσοφος, loving know[ledge] … Gk. φίλος, fond of; σοφός, skilful.'\"}])\n\n# ---------------- node 3 ----------------\nN(3, \"Arabic\", \"falsafah\", \"plausible\",\n  \"Arabic فَلْسَفَة falsafa 'philosophy' entered Arabic in the 3rd/9th-century translation movement, through Syriac ـfilosofā, and was re-analysed on the native quadriliteral pattern faʿlalah, producing a new consonantal root فلسف with the verb فَلْسَفَ / تَفَلْسَفَ and the agent noun فَيْلَسُوف faylasūf (pl. فَلاسِفة falāsifa). Nourai's arrow φιλόσοφος > falsafah is one of the two routes modern sources allow, but the direct model of the ABSTRACT noun is φιλοσοφία: Wiktionary gives 'from Ancient Greek φιλοσοφία, either directly or through فَيْلَسُوف', the latter (< φιλόσοφος) being the form that actually matches Nourai's Greek etymon. Hence plausible rather than exact.\",\n  \"عربی «فلسفه» در جنبش ترجمهٔ سدهٔ سوم هجری، بیشتر از راه سریانی، از یونانی philosophia وام گرفته شده و سپس بر وزن رباعی «فَعْلَلَة» بازتحلیل شده و ریشهٔ ساختگیٔ «ف‌ل‌س‌ف» پدید آورده است با فعل «تفلسف» و اسم فاعل «فیلسوف» (جمع: فلاسفه). نورایی پیکان را از philosophos کشیده است که درست‌تر منشأ «فیلسوف» است، نه «فلسفه»؛ از این‌رو ادعا با احتیاط پذیرفتنی است.\",\n  [W_FALS],\n  [{\"ref\": \"TAD:53\", \"status\": \"supports\",\n    \"note\": \"TAD_pages.txt leaf 56 (0-based; printed page ≈ 51-53, the book's own numeral is not legible in the OCR): 'فلسفة — يوناني Philosophia معناه حب الحكمة ومنه تفلسف وفيلسوف' (OCR: 'فاسفة ل ونانى … معناه حب المكة ومنه تقليف وفيلسوف'). Al-Unaysi thus gives the Greek source and the derived تفلسف/فيلسوف, as Nourai claims; he names philosophia, not philosophos.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philosophy\", \"stance\": \"partial\",\n    \"note\": \"Klein has the Greek chain (φιλοσοφία < φιλόσοφος) but says nothing about the Arabic borrowing.\"},\n   {\"src\": \"FVQ\", \"where\": \"Jeffery, Foreign Vocabulary of the Qur'an\", \"stance\": \"silent\",\n    \"note\": \"grep 'falsaf'/'فلسف' in FVQ_pages.txt: nothing — falsafa is post-Qur'anic, so Jeffery does not treat it.\"},\n   {\"src\": \"ARB\", \"where\": \"al-Jawaliqi, al-Mu'arrab\", \"stance\": \"silent\",\n    \"note\": \"grep 'فلسف' in ARB_mo3rb.txt / ARB_abdulraheem.txt: no headword — al-Jawaliqi records mainly older Persian/Aramaic muʿarrabāt, not the translation-movement Graecisms.\"}])\n\n# ---------------- node 4 ----------------\nN(4, \"Persian\", \"falsafeh «فلسفه»\", \"confirmed\",\n  \"New Persian فلسفه falsafe 'philosophy' is a straight Arabic loan (Arabic فَلْسَفَة), taken over with the Arabic tāʾ marbūṭa written ـه and pronounced -e in Persian, current from the earliest Islamic-Persian philosophical prose onward. The box's extra forms belong to the same Arabic quadriliteral family: فیلسوف faylsūf/filsuf (Ar. فَيْلَسُوف < Gk. φιλόσοφος) and its broken plural فلاسفه falāsefe. Mo'in tags the headword [ع.] = Arabic, confirming the immediate donor language of the chart.\",\n  \"«فلسفه» در فارسی نو وام‌واژهٔ مستقیم از عربی فَلْسَفَة است که تاء مربوطهٔ آن در فارسی به ـه نوشته و -e خوانده می‌شود؛ معین در فرهنگ فارسی آن را با نشانهٔ [ع.] می‌آورد: «(فَ لْ سَ فِ) [ع.] (اِ.) ۱- حکمت، دانشی که موضوع آن هستی و وجود است». واژه‌های افزودهٔ جعبه (فیلسوف، فلاسفه) نیز از همین ریشهٔ رباعی عربی‌اند. ادعای نورایی درست است.\",\n  [V_FALS, W_FALS],\n  [{\"ref\": \"MON:2567\", \"status\": \"partial\",\n    \"note\": \"The Mo'in entry was verified online (vajehyab.com/moein/فلسفه): '(فَ لْ سَ فِ) [ع.] (اِ.) ۱- حکمت، دانشی که موضوع آن هستی و وجود است. ۲- علت، دلیل' — the [ع.] tag is exactly Nourai's Arabic parent. The printed page number 2567 could not be checked: the online Mo'in has no pagination and the local MON_part1/2 files are the 2-volume Adena reprint.\"}],\n  [{\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. فلسفه (vajehyab)\", \"stance\": \"supports\",\n    \"note\": \"'[ع.] (اِ.) ۱- حکمت، دانشی که موضوع آن هستی و وجود است' — marked as an Arabic loan.\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\",\n    \"note\": \"grep 'فلسف' in BQT_v1_pages.txt / BQT_v2_pages.txt: no etymological footnote — Borhan is a dictionary of Persian words, and Mo'in annotates Iranian, not Arabic-Greek, vocabulary.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss\", \"stance\": \"silent\",\n    \"note\": \"Horn treats inherited Iranian vocabulary; falsafa, an Arabic loan, is absent (grep 'falsaf' in HRN.txt: nothing).\"}])\n\n# ---------------- node 5 ----------------\nN(5, \"Latin\", \"\", \"confirmed\",\n  \"Pass-through node: Latin took φιλόσοφος/φιλοσοφία as philosophus, philosophia already in the Republican period (Cicero uses philosophia as a naturalised word and coins Latin equivalents for its terminology), with the regular transliteration Gk. φ > Lat. ph and Gk. -ος/-ία > Lat. -us/-ia. From Latin the word passed into all the Romance languages.\",\n  \"این گره واسطه است: لاتینی philosophus و philosophia را در دوران جمهوری (سیسرون) از یونانی وام گرفته است؛ فای یونانی به ph لاتینی و پایانهٔ -os/-ia به -us/-ia بدل شده است. ادعای نورایی درست است.\",\n  [E_PHILO],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. bhilo- gives PHILO- etc. as English reflexes; the Latin transmission is the standard route assumed by the AHD entries for these words.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philosophy\", \"stance\": \"supports\",\n    \"note\": \"'fr. L. philosophia, fr. Gk. φιλοσοφία.'\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philosophy\", \"stance\": \"supports\",\n    \"note\": \"Skeat's chain label '(F.—L.—Gk.)' has Latin as the middle link.\"}])\n\n# ---------------- node 6 ----------------\nN(6, \"French\", \"\", \"confirmed\",\n  \"Pass-through node: Old French filosofie / philosophie is attested from the 12th century, a learned borrowing from Latin philosophia with the Old French learned ending -ie for Latin -ia. English took the word from this Old French form (and partly re-latinised the spelling).\",\n  \"این گره واسطه است: فرانسهٔ کهن filosofie/philosophie از سدهٔ دوازدهم میلادی گواهی شده و وام‌واژه‌ای عالمانه از لاتینی philosophia است که پایانهٔ -ia در آن به -ie بدل شده است. ادعای نورایی درست است.\",\n  [E_PHILO],\n  [{\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"The 1975/76 AHD appendix page is not open online; the 1985 Watkins reprint has no page-level French detail for this word.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philosophy\", \"stance\": \"supports\",\n    \"note\": \"'ME. philosophie, fr. OF. philosophie, filosofie (F. philosophie), fr. L. philosophia.'\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philosophy\", \"stance\": \"supports\",\n    \"note\": \"'M.E. philosophie. — F. philosophie … L. philosophia.'\"}])\n\n# ---------------- node 7 ----------------\nN(7, \"English\", \"philosophy\", \"confirmed\",\n  \"English philosophy is first attested c.1300 as philosophie 'knowledge, learning, scholarship', from Old French filosofie (12c.) and directly from Latin philosophia; Middle English shows many spellings (filozofie, phelosophie). The sense narrows to 'rational speculation' in the mid-14th c. and to 'the science of the most fundamental matters' by 1794.\",\n  \"انگلیسی philosophy نخست در حدود ۱۳۰۰ میلادی به صورت philosophie به معنی «دانش و دانش‌وری» گواهی شده است، از فرانسهٔ کهن filosofie و مستقیماً از لاتینی philosophia. در انگلیسی میانه املاهای گوناگونی داشته و معنای فنی امروزی آن از سدهٔ هجدهم پدید آمده است. ادعای نورایی درست است.\",\n  [E_PHILO],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. bhilo-: PHILO- and the other phil- words are listed as the English outcome of Greek philos.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philosophy\", \"stance\": \"supports\",\n    \"note\": \"'philosophy, n. — ME. philosophie, fr. OF. philosophie … fr. Gk. φιλοσοφία.'\"},\n   {\"src\": \"SKT\", \"where\": \"p.547\", \"stance\": \"supports\",\n    \"note\": \"'philosophy, love of wisdom. (F.—L.—Gk.) M.E. philosophie.'\"}])\n\n# ---------------- node 8 ----------------\nN(8, \"Greek\", \"philo-armonica; philo-hippos; philo-adelphos\", \"plausible\",\n  \"Two of the three are genuine Greek compounds: φίλιππος 'fond of horses' (φίλος + ἵππος, the Macedonian royal name Philippos) and φιλάδελφος 'loving one's brother/sister' (φίλος + ἀδελφός), the epithet of Attalus II Philadelphus and Ptolemy II. The first item, 'philo-armonica', is NOT a Greek word: the ancestor of philharmonic is Italian filarmonico (from fil- 'phil-' + armonico, itself from Gk. (τὰ) ἁρμονικά 'theory of music'), which gave French philharmonique (1739) and English philharmonic (1813). Nourai's form is a Latino-Italian shape written as if Greek; the Greek elements are right but the compound is a modern one. Node verdict takes the worst of the three.\",\n  \"از سه واژهٔ این جعبه، دو تای آخر ترکیب‌های اصیل یونانی‌اند: φίλιππος «اسب‌دوست» و φιλάδελφος «برادر‌دوست» (لقب آتالوس دوم و بطلمیوس دوم). اما philo-armonica واژه‌ای یونانی نیست؛ این ساخت از ایتالیایی filarmonico برآمده که خود از اجزای یونانی (philos + harmoniká) در دوران جدید ساخته شده است. بنابراین ادعای نورایی دربارهٔ دو واژه درست و دربارهٔ واژهٔ نخست با احتیاط پذیرفتنی است.\",\n  [E_PHILH, E_PHILA],\n  [{\"ref\": \"KLN\", \"status\": \"contradicts\",\n    \"note\": \"KLN_1971.txt s.v. philharmonic: 'philharmonic, adj., loving music. — F. philharmonique, fr. It. filarmonico, fr. fil-, “phil-”, and armonico, fr. Gk. (τὰ) ἁρμονικά, “theory of music”.' Klein gives Italian, not a Greek *philo-armonica.\"},\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins 1985 s.v. bhilo- lists only the phil- prefix words generally; it has no entry for a Greek compound *philarmonikos.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philharmonic\", \"stance\": \"contradicts\",\n    \"note\": \"'F. philharmonique, fr. It. filarmonico' — Italian is the intermediary.\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philharmonic\", \"stance\": \"partial\",\n    \"note\": \"'philharmonic, loving music. (Gk.) Gk. φίλ-ος, friendly, fond of; and L. -icus; Gk. ἁρμονία harmony' — Skeat too treats it as a modern coinage from Greek elements, with a Latin suffix, not as an inherited Greek compound.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"partial\",\n    \"note\": \"The index line 'PHILADELPHIA … -PHILE bhilo- … PHILO- bhilo-' assigns the phil- words to the root; the -armonica part belongs under ar- (harmony), as Nourai's cross-reference ☞ Ar also says.\"}])\n\n# ---------------- node 9 ----------------\nN(9, \"Latin\", \"\", \"plausible\",\n  \"Pass-through node with no refs in the book. It is right for two of the three words above: Latin took over Philippus and the Greek place-name Φιλαδέλφεια (the Lydian city of Revelation 3:7) as Philadelphia, and these Latin forms fed the modern languages. It is not the route of philharmonic, which reached French from Italian filarmonico without a Latin stage.\",\n  \"این گرهٔ واسطه در کتاب بدون ارجاع آمده است. برای دو واژه درست است: لاتینی Philippus و نام شهر Philadelphia را از یونانی گرفته و به زبان‌های اروپایی رسانده است؛ اما راه philharmonique ایتالیایی بوده و از لاتینی نگذشته است. با احتیاط پذیرفتنی است.\",\n  [E_PHILA, E_PHILH],\n  [{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The book gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philharmonic\", \"stance\": \"contradicts\",\n    \"note\": \"Klein routes philharmonic F < It., with no Latin stage.\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philippic\", \"stance\": \"supports\",\n    \"note\": \"'philippic … L. Philippicum, pl. Philippica, to denote the celebrated orations of Demosthenes against Philip. — Gk. Φίλιππος, Philip; lit. “a lover of horses”' — Latin did take the Greek name over.\"}])\n\n# ---------------- node 10 ----------------\nN(10, \"French\", \"\", \"plausible\",\n  \"Pass-through node: French has Philippe (from Latin Philippus), Philadelphie, and philharmonique, first recorded 1739 and borrowed from Italian filarmonico rather than from Latin. French is therefore a real link for Philippe/philharmonique and the donor of the Persian forms below, but for Philadelphia the English and Persian forms show the Latinate -ia, not French -ie.\",\n  \"این گرهٔ واسطه درست است: فرانسه Philippe را از لاتینی و philharmonique را (۱۷۳۹ م.) از ایتالیایی گرفته است و همین زبان وام‌دهندهٔ صورت‌های فارسی پایین است؛ ولی برای «فیلادلفیا» پایانهٔ -ia لاتینی/انگلیسی است نه -ie فرانسوی. با احتیاط پذیرفتنی است.\",\n  [E_PHILH],\n  [{\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"The 1975/76 AHD appendix is not open online; the 1985 Watkins text carries no French detail.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philharmonic\", \"stance\": \"supports\",\n    \"note\": \"'F. philharmonique, fr. It. filarmonico' — French is the immediate donor to English.\"},\n   {\"src\": \"SKT\", \"where\": \"p.547\", \"stance\": \"partial\",\n    \"note\": \"Skeat labels philharmonic simply '(Gk.)', i.e. a learned coinage, without the French stage Klein and Etymonline give.\"}])\n\n# ---------------- node 11 ----------------\nN(11, \"Persian\", \"(no transliterated word; script only: فیلارمونیک ، فیلیپ)\", \"confirmed\",\n  \"The two Persian forms in this box are 20th-century French loans: فیلارمونیک filārmonīk from French philharmonique (French -ique regularly gives Persian -یک, and French ph is heard as f, giving ف‌ی‌ل fil- for phil-), and فیلیپ Fīlīp from French Philippe (final -e is not pronounced, hence فیلیپ and not *فیلیپه). Both entered Persian through the French-mediated European vocabulary of the Qajar and Pahlavi periods, as the whole class of Persian musical and personal-name Gallicisms did.\",\n  \"دو صورت این جعبه وام‌واژه‌های فرانسوی سدهٔ چهاردهم خورشیدی‌اند: «فیلارمونیک» از philharmonique فرانسوی (پایانهٔ -ique در فارسی به -یک و ph به ف بدل می‌شود) و «فیلیپ» از Philippe فرانسوی که هٔ پایانی آن خوانده نمی‌شود. این وام‌گیری‌ها از راه فرانسه در دوران قاجار و پهلوی صورت گرفته است. ادعای نورایی درست است.\",\n  [E_PHILH],\n  [{\"ref\": \"VOP:257\", \"status\": \"not_checked\",\n    \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371) is not available in any scan: refs_online.json records 'RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook.'\"}],\n  [{\"src\": \"MON\", \"where\": \"Farhang-e Mo'in (foreign-word volume)\", \"stance\": \"silent\",\n    \"note\": \"The local MON files are the 2-volume Adena reprint of the lexicon; grep 'فیلارمونیک' returns nothing, so Mo'in's [فر.] tag for this word could not be quoted from disk.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. philharmonic\", \"stance\": \"supports\",\n    \"note\": \"Klein's 'F. philharmonique' is the source form the Persian فیلارمونیک reproduces (fil- + -onīk).\"}])\n\n# ---------------- node 12 ----------------\nN(12, \"English\", \"Philadelphia; Philip; philharmonic\", \"plausible\",\n  \"philharmonic is exactly as drawn: English 1813, in the name of the London society, from French philharmonique (1739) < Italian filarmonico. Philip is Latin Philippus / Old French Philippe < Gk. Φίλιππος, so a French stage is defensible. Philadelphia is not from French: the Pennsylvania city was named by William Penn in 1682 straight from Greek φιλαδελφία 'brotherly love' (with the New-Testament Lydian city, named for Attalus II Philadelphus, in mind), and the English form keeps Greek/Latin -ia rather than French -ie. The node is therefore right in substance but its 'French' parent holds for only two of the three words.\",\n  \"از سه واژه، philharmonic (۱۸۱۳ م، از فرانسه) و Philip (از لاتینی/فرانسهٔ کهن) از راه فرانسه رسیده‌اند، اما Philadelphia را ویلیام پن در ۱۶۸۲ مستقیماً از یونانی «برادردوستی» برگزیده است (با یادآوری شهر لیدیایی مذکور در مکاشفهٔ یوحنا) و پایانهٔ -ia یونانی–لاتینی را نگاه داشته، نه -ie فرانسوی. پس پیکان «از فرانسه» دربارهٔ یکی از سه واژه نادرست است.\",\n  [E_PHILA, E_PHILH],\n  [{\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 index: 'PHILADELPHIA' and the PHIL-/PHILO- words are all referred to bhilo-, which is Nourai's root.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philharmonic\", \"stance\": \"supports\",\n    \"note\": \"'F. philharmonique, fr. It. filarmonico' — confirms the French > English step for philharmonic.\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philippic\", \"stance\": \"supports\",\n    \"note\": \"'Gk. Φίλιππος, Philip; lit. “a lover of horses” — Gk. φίλ-ος, fond of; ἵππος, a horse.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 index line for PHILADELPHIA\", \"stance\": \"partial\",\n    \"note\": \"The index assigns the word to bhilo- but gives no transmission route, so it neither confirms nor denies a French stage.\"}])\n\n# ---------------- node 13 ----------------\nN(13, \"Persian\", \"Fîlâdelfîyâ «فیلادلفیا»\", \"confirmed\",\n  \"Persian فیلادلفیا Fīlādelfīyā is the modern transcription of the American place-name, taken in its English/Latinate shape: the final -ia is rendered ـیا (as in ایتالیا، کالیفرنیا), which excludes a French Philadelphie as the model; ph is heard as f. Mo'in records such names in the aʿlām (proper-name) volumes, which is what the bare 'MON' citation points to.\",\n  \"«فیلادلفیا» آوانویسی نام شهر آمریکایی است و پایانهٔ آن (ـیا در برابر -ia) نشان می‌دهد که از صورت انگلیسی–لاتینی گرفته شده، نه از Philadelphie فرانسوی؛ ph نیز به ف بدل شده است. معین این‌گونه نام‌ها را در جلدهای اعلام فرهنگ فارسی آورده است. ادعای نورایی درست است.\",\n  [E_PHILA],\n  [{\"ref\": \"MON\", \"status\": \"not_checked\",\n    \"note\": \"Nourai cites Mo'in without a page; the aʿlām volumes (MON vols 5-6) are not among the local scans and vajehyab carries only the lexicon volumes (a query for فیلادلفیا returns no Mo'in entry).\"}],\n  [{\"src\": \"MON\", \"where\": \"local MON_part1/2 (2-vol Adena reprint)\", \"stance\": \"silent\",\n    \"note\": \"grep 'فیلادلفیا' in MON_part1.txt and MON_part2.txt: no hit — the proper-name volumes are not in this reprint.\"},\n   {\"src\": \"KLN\", \"where\": \"s.v. philo-, -adelphos\", \"stance\": \"supports\",\n    \"note\": \"Klein's philo- entry supplies the Greek elements; Etymonline supplies the naming by William Penn in 1682 and the Lydian city of Attalus II Philadelphus.\"}])\n\n# ---------------- node 14 ----------------\nN(14, \"Greek\", \"sūs-philos\", \"plausible\",\n  \"No Greek *σῦς-φιλος is attested; the form is the modern back-explanation of the name Syphilus that Fracastoro gave his shepherd in 1530, and the elements are real Greek (ὗς/σῦς, gen. ὑός 'swine' + φίλος 'friend, loving'). Klein and Funk & Wagnalls both give exactly this analysis, so Nourai is following the standard 19th-20th c. dictionaries; but Etymonline notes that Fracastoro's intention is unknown and that the rival conjecture — an alteration of Sipylus, the son of Niobe in Ovid's Metamorphoses — is equally current. Hence plausible, not confirmed.\",\n  \"ترکیب *sūs-philos در یونانی باستان گواهی نشده است؛ این صورت تحلیلی است که فرهنگ‌نویسان برای نام Syphilus (چوپان منظومهٔ فراکاستورو، ۱۵۳۰ م.) ساخته‌اند، از ὗς «خوک» و φίλος «دوست». کلاین و فانک و واگنالز همین تحلیل را می‌آورند، ولی پژوهش امروزی مقصود فراکاستورو را نادانسته می‌داند و احتمال دیگر را دگرگونی Sipylus (پسر نیوبه در اوید) می‌داند. بنابراین با احتیاط پذیرفتنی است.\",\n  [E_SYPH],\n  [{\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"KLN_1966.txt (leaf 827, ≈ printed p.1630) s.v. syphilis: 'so named after the hero Syphilus, a shepherd whose name lit. means “friend of swine”, fr. Gk. σῦς (gen. συός) = ὗς (gen. ὑός), “swine”, and φίλος, “friend”.'\"},\n   {\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"The 1975/76 AHD main dictionary (p.1306) is lending-restricted on archive.org; the 1985 Watkins appendix reprint has no syphilis entry.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. syphilis\", \"stance\": \"supports\",\n    \"note\": \"As quoted above — Klein gives the sūs + philos analysis as fact.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV s.v. syphilis\", \"stance\": \"supports\",\n    \"note\": \"'[F., < Syphilus, name of a shepherd in “Syphilus, sive Morbus Gallicus”, a poem by Fracastorio, < Gr. sys, swine + philos loving]'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat\", \"stance\": \"silent\",\n    \"note\": \"grep 'syphilis' in SKT.txt: no entry — Skeat's concise dictionary omits the word.\"}])\n\n# ---------------- node 15 ----------------\nN(15, \"Latin\", \"\", \"plausible\",\n  \"Pass-through node, unreferenced in the book. It is right in that the coinage really is Latin — but New Latin of 1530, not ancient Latin: Girolamo Fracastoro of Verona wrote the hexameter poem Syphilis sive de morbo Gallico in Latin and there invented both the shepherd's name and, in his 1546 prose treatise De contagione, its use for the disease.\",\n  \"این گرهٔ واسطه در کتاب بدون ارجاع است. زبان وام‌دهنده واقعاً لاتینی است، اما لاتینی نوی سدهٔ دهم هجری/شانزدهم میلادی: جرولامو فراکاستوروی ورونایی در ۱۵۳۰ م. منظومهٔ Syphilis sive de morbo Gallico را به لاتینی سرود و همین نام را ساخت. با احتیاط پذیرفتنی است.\",\n  [E_SYPH],\n  [{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The book gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. syphilis\", \"stance\": \"supports\",\n    \"note\": \"'ModL., from the title of the work by Girolamo Fracastoro, Syphilis sive de morbo Gallico … published at Verona in 1530.'\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV\", \"stance\": \"partial\",\n    \"note\": \"F&W names the same poem but labels the English word's immediate source '[F.]' (French), skipping the Latin stage.\"}])\n\n# ---------------- node 16 ----------------\nN(16, \"French\", \"Syphilis\", \"plausible\",\n  \"The gloss is accurate history: Fracastoro's 1530 poem, the shepherd Syphilus as the disease's first victim, the disease later named from the poem's hero. The language label is the weak point: the word is Modern/New Latin coined in Italy, not French; Klein, Etymonline and the AHD all say ModL/New Latin, and English syphilis is first recorded 1718. Nourai's 'French' is not baseless — Funk & Wagnalls (which he used elsewhere) marks English syphilis '[F.]', i.e. transmitted through French — so French is at most the vehicle to English, never the language of the coinage. One factual slip in the caption: Fracastoro's Syphilus is the FIRST VICTIM in the poem, not a real physician's patient, and it is the poem, not the hero, that gave the disease its name.\",\n  \"متن توضیحی جعبه از نظر تاریخی درست است، اما برچسب زبانی آن نادرست است: واژه لاتینی نو (ModL) است که در ایتالیا ساخته شده، نه فرانسوی؛ کلاین و اتیمانلاین هر دو آن را ModL می‌دانند و نخستین کاربرد انگلیسی آن ۱۷۱۸ م. است. با این همه، فانک و واگنالز منشأ واژهٔ انگلیسی را «فرانسوی» می‌داند؛ پس فرانسه تنها واسطهٔ انتقال بوده است نه زبان سازندهٔ واژه.\",\n  [E_SYPH],\n  [{\"ref\": \"KLN:1561\", \"status\": \"partial\",\n    \"note\": \"Klein's syphilis entry says exactly what Nourai's caption says ('ModL., from the title of the work by Girolamo Fracastoro … published at Verona in 1530; so named after the hero Syphilus, a shepherd'), but it stands at KLN_1966 leaf 827 ≈ printed p.1630, not p.1561: leaf 792 (≈ pp.1560-1561) is in the 'spittle / spot' range. The content supports the arrow; the page number does not match the 1966 two-volume pagination. Klein also calls it Modern Latin, not French.\"},\n   {\"ref\": \"AHD:1306\", \"status\": \"not_checked\",\n    \"note\": \"The 1975/76 AHD New College main dictionary is lending-only on archive.org (americanheritage0000dict etc., djvu.txt returns 401); the current AHD entry online reads 'New Latin syphilis, after Syphilus, a shepherd in Fracastoro's poem'.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. syphilis\", \"stance\": \"contradicts\",\n    \"note\": \"'ModL.' — Modern Latin, not French.\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV s.v. syphilis\", \"stance\": \"supports\",\n    \"note\": \"'[F., < Syphilus, name of a shepherd …]' — F&W does label the English word's source French, which is very likely where Nourai's 'French' box comes from.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch\", \"stance\": \"silent\",\n    \"note\": \"grep 'Syphil' in LKT.txt: nothing — the word is not of oriental origin, so Lokotsch has no entry.\"}])\n\n# ---------------- node 17 ----------------\nN(17, \"Persian\", \"sîfîlîs «سیفیلیس»; seflîs «سفلیس»\", \"confirmed\",\n  \"Persian سیفیلیس sīfīlīs is the medical Gallicism of the Qajar/Pahlavi era, taken from French syphilis with the French pronunciation (final -s pronounced, hence ـس and not a silent ending); the doublet سفلیس seflīs is the colloquial reduction of the same word by loss of the unstressed first ī (sīfīlīs > seflīs), a very ordinary Persian shortening of long European words. Persian dictionaries define it purely as the disease.\",\n  \"«سیفیلیس» وام‌واژه‌ای پزشکی از فرانسه (syphilis) است که در دوران قاجار و پهلوی به فارسی راه یافته و سِین پایانی آن مطابق تلفظ فرانسوی خوانده می‌شود. صورت دوم «سفلیس» گونهٔ کوتاه‌شدهٔ عامیانه است که از افتادن ای نخست پدید آمده (sīfīlīs > seflīs) — دگرگونی آوایی معمول در وام‌واژه‌های بلند اروپایی. ادعای نورایی درست است.\",\n  [A_SIF, E_SYPH],\n  [{\"ref\": \"MON\", \"status\": \"partial\",\n    \"note\": \"Nourai cites Mo'in without a page. The entry was checked on abadis.ir, which reproduces فرهنگ فارسی: 'مرضی عفونی و ساری که به ارث به طور مادرزادی به افراد منتقل می‌شود' — the word and both variants are Persian dictionary entries, but the page and the [فر.] tag could not be quoted from the print edition.\"}],\n  [{\"src\": \"MON\", \"where\": \"abadis.ir فرهنگ فارسی s.v. سیفیلیس\", \"stance\": \"supports\",\n    \"note\": \"The headword exists with the medical definition quoted above; the local MON_part1/2 files also show سیفیلیس in running definitions (e.g. MON_part2.txt line 1837 'دور خر سیفیلیس و همچنین ضایعات').\"},\n   {\"src\": \"BQT\", \"where\": \"Borhan-e Qate'\", \"stance\": \"silent\",\n    \"note\": \"grep 'سیفیلیس'/'سفلیس' in BQT_v1_pages.txt / BQT_v2_pages.txt: nothing — a 17th-century Persian dictionary cannot contain a 19th-century European medical loan.\"}])\n\n# ---------------- node 18 ----------------\nN(18, \"English\", \"syphilis\", \"confirmed\",\n  \"English syphilis is first recorded 1718, taken as Modern Latin (with French as a likely vehicle, per Funk & Wagnalls) from Fracastoro's title; Fracastoro himself had already used the word generically for the disease in De contagione (1546). The English form keeps the Latin nominative -is unchanged.\",\n  \"انگلیسی syphilis نخست در ۱۷۱۸ م. گواهی شده و از لاتینی نوی عنوان منظومهٔ فراکاستورو گرفته شده است (فانک و واگنالز واسطهٔ فرانسه را می‌آورد)؛ خود فراکاستورو در رسالهٔ De contagione (۱۵۴۶) آن را نام عام بیماری کرده بود. ادعای نورایی درست است.\",\n  [E_SYPH],\n  [{\"ref\": \"AHD\", \"status\": \"not_checked\",\n    \"note\": \"The 1975/76 AHD main dictionary is lending-restricted; the modern AHD online reads 'New Latin syphilis, after Syphilus, a shepherd in Fracastoro's poem'.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. syphilis\", \"stance\": \"supports\",\n    \"note\": \"'syphilis, n., an infectious venereal disease. — ModL., from the title of the work by Girolamo Fracastoro …'\"},\n   {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls vol. IV s.v. syphilis\", \"stance\": \"supports\",\n    \"note\": \"Describes the three stages of the disease and gives the etymology '[F., < Syphilus … < Gr. sys, swine + philos loving]'.\"}])\n\n# ---------------- node 19 ----------------\nN(19, \"Greek\", \"philo-anthôpos; philo-logos\", \"transcription_suspect\",\n  \"philo-logos is correct: Greek φιλόλογος 'fond of discourse/learning', whence φιλολογία. But 'philo-anthôpos' is impossible: the Greek word is φιλάνθρωπος phil-ánthrōpos 'loving mankind' (φίλος + ἄνθρωπος 'man'), abstract φιλανθρωπία > Late Latin philanthropia > English philanthropy — the r of ἄνθρωπος is missing. I rendered PDF page 96 at 600 dpi and read the box: the printed page itself shows 'philo-anthôpos', so this is Nourai's own misprint and the JSON extraction is faithful. (Nourai's own cross-reference ☞ Ner 1 is to the root of ἀνήρ/ἄνθρωπος, which shows he meant ἄνθρωπος.)\",\n  \"صورت philo-logos درست است (φιλόλογος «سخن‌دوست، ادب‌دوست»)، اما philo-anthôpos صورتی ناممکن است: واژهٔ یونانی φιλάνθρωπος (از ἄνθρωπος «انسان») است و رای آن افتاده است. تصویر صفحهٔ ۹۶ نسخهٔ پی‌دی‌اف را با تفکیک ۶۰۰ دی‌پی‌آی خواندم: در خود کتاب هم philo-anthôpos چاپ شده؛ پس این خطای چاپی کتاب است و خوانش اسکن درست عمل کرده است.\",\n  [E_PHILO],\n  [{\"ref\": \"KLN\", \"status\": \"supports\",\n    \"note\": \"KLN_1971.txt: 'philanthropy, n. — Late L. philanthropia, fr. Gk. φιλανθρωπία, “love to mankind, humanity, benevolence”, fr. φιλάνθρωπος' — with the r; and 'philology, n. — F. philologie, fr. L. philologia … fr. Gk. φιλόλογος, “fond of learning”'.\"},\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins 1985 index sends PHILANTHROPY to ner-2 (the ἀνήρ root), which is precisely Nourai's ☞ Ner 1 cross-reference — further proof he intended ἄνθρωπος.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philanthropy, philology\", \"stance\": \"supports\",\n    \"note\": \"Both Greek compounds are given in their correct forms φιλάνθρωπος / φιλόλογος.\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philanthropy, philology\", \"stance\": \"supports\",\n    \"note\": \"'philanthropy, love of mankind. (L.—Gk.) L. philanthropia. — Gk. φιλανθρωπία, benevolence. — Gk. φιλάνθρωπος, loving mank[ind] … ἄνθρωπος, a man'; 'philology, study of languages. (L.—Gk.) L. philologia. — Gk. φιλολογία.'\"}],\n  extra={\"error_in\": \"book\",\n         \"book_prints\": \"philo-anthôpos\",\n         \"correct_form\": \"philo-anthrōpos (Gk. φιλάνθρωπος)\",\n         \"page_image\": \"data/verification/sources/refs/ocr/BOOK/96.png\"})\n\n# ---------------- node 20 ----------------\nN(20, \"Latin\", \"\", \"confirmed\",\n  \"Pass-through node, unreferenced. Latin borrowed both compounds as learned words: Late Latin philanthropia (in the Church Fathers, rendering Gk. φιλανθρωπία 'God's love of mankind') and classical Latin philologia (Cicero, of learned study; the title of Martianus Capella's De nuptiis Philologiae et Mercurii).\",\n  \"این گرهٔ واسطه درست است: لاتینی هر دو واژه را وام گرفته است؛ philanthropia در لاتینی متأخر و در متون مسیحی، و philologia از عصر سیسرون. ادعای نورایی درست است.\",\n  [E_PHILO],\n  [{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The book gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philanthropy, philology\", \"stance\": \"supports\",\n    \"note\": \"'Late L. philanthropia'; 'fr. L. philologia, “love of learning, love of letters”'.\"},\n   {\"src\": \"SKT\", \"where\": \"p.547\", \"stance\": \"supports\",\n    \"note\": \"Skeat labels philanthropy '(L.—Gk.)' and philology '(L.—Gk.)', i.e. through Latin.\"}])\n\n# ---------------- node 21 ----------------\nN(21, \"French\", \"\", \"confirmed\",\n  \"Pass-through node, unreferenced. French philanthropie and philologie are the immediate models of the English words; Klein derives English philology directly from French philologie, and Skeat labels philosophy '(F.—L.—Gk.)' for the same chain.\",\n  \"این گرهٔ واسطه درست است: فرانسهٔ philanthropie و philologie الگوی مستقیم صورت‌های انگلیسی‌اند؛ کلاین philology را صریحاً از فرانسه می‌گیرد. ادعای نورایی درست است.\",\n  [E_PHILO],\n  [{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The book gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philology\", \"stance\": \"supports\",\n    \"note\": \"'philology, n. — F. philologie, fr. L. philologia.'\"},\n   {\"src\": \"SKT\", \"where\": \"p.547 s.v. philanthropy\", \"stance\": \"partial\",\n    \"note\": \"Skeat labels philanthropy '(L.—Gk.)' without a French stage, so the French box is Klein's route rather than Skeat's.\"}])\n\n# ---------------- node 22 ----------------\nN(22, \"English\", \"philanthropy; philology\", \"confirmed\",\n  \"English philanthropy (1600s, from Late Latin philanthropia through French) and philology (late 14th c. 'love of learning', from French philologie / Latin philologia) are the regular outcomes of the chain drawn; both preserve the Greek combining form philo-/phil- and the Latin-French -ia > -ie > -y ending.\",\n  \"انگلیسی philanthropy و philology برآیند منظم همین زنجیره‌اند: پایانهٔ لاتینی -ia در فرانسه به -ie و در انگلیسی به -y بدل شده و جزء پیشین philo-/phil- دست‌نخورده مانده است. ادعای نورایی درست است.\",\n  [E_PHILO],\n  [{\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"The book gives no reference for this node.\"}],\n  [{\"src\": \"KLN\", \"where\": \"s.v. philanthropy, philology\", \"stance\": \"supports\",\n    \"note\": \"'philanthropy, n. — Late L. philanthropia …'; 'philology, n. — F. philologie …'\"},\n   {\"src\": \"SKT\", \"where\": \"p.547\", \"stance\": \"supports\",\n    \"note\": \"Both headwords present with the same Greek etyma.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 index\", \"stance\": \"partial\",\n    \"note\": \"'PHILANTHROPY ner-2' — the AHD files philanthropy under the ἀνήρ root, not under bhilo-, but that is only a matter of which member of the compound the index chooses.\"}])\n\nentry0 = {\n  \"entry\": 0,\n  \"root\": \"Bhili, Bhilo\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *bʰili-, *bʰilo- 'harmonious, fitting, good, friendly' (Watkins: bhilo- 'dear, familiar')\",\n  \"note\": \"Pokorny IEW 153-154 has the lemma exactly as Nourai names it: 'bhili-, bhilo- ‚ebenmäßig, angemessen, gut, freundlich‘', with Mir. bil 'good', Gaul. Bili- in names, OHG bila-/bili-, bil-lich, OE bile-wit, MHG unbil, NHG Unbilde. Walde-Pokorny II 185 and Mann (IEC 'bhilos (1) “good, fair, friendly, pleasant”') agree, and Watkins gives 'bhilo-. Dear, familiar.' So the root form, the language label 'Indo-European' and the gloss 'good, friendly, loving' are all correct. The chart's own NOTE, 'SYN:1110 claims this is an Anatolian word', is accurate and important: Buck p.1110 (16.27 LOVE) writes that Greek philos, 'in Hom. also “one's own”, this perh. the earliest sense and so fr. an Anatolian word represented by Lyd. bilis “one's own” (Kretschmer, IF 45.267 ff.)'. That doubt bears only on the Greek branch — i.e. on node #1, and through it on the whole page — not on the Germanic/Celtic root itself, which is secure. Beekes (2010) likewise rejects the IE etymology of philos. The page is otherwise a clean Greek-Latin-French-English fan with two Persian offshoots; the only real error is the misprint philo-anthôpos (node #19) and the Greek label on the modern coinage philo-armonica (node #8).\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *bʰili-/*bʰilo- «متناسب، شایسته، نیک، دوستانه»؛ پوکورنی در صفحات ۱۵۳–۱۵۴ همین مدخل را با همین نام و همین معنا آورده و والده–پوکورنی، مان و واتکینز نیز آن را تأیید می‌کنند؛ پس نام ریشه، برچسب زبانی و معنای آن در کتاب درست است. یادداشت خود نورایی («SYN:1110 آن را واژه‌ای آناتولیایی می‌داند») عیناً درست است: باک در صفحهٔ ۱۱۱۰ می‌نویسد که معنای کهن‌تر φίλος در هومر «از آنِ خود» است و شاید از لیدیایی bilis آمده باشد. این تردید تنها به شاخهٔ یونانی (گرهٔ ۱) مربوط است نه به خود ریشه. در سراسر صفحه تنها دو ایراد جدی هست: غلط چاپی philo-anthôpos و یونانی خواندن ساختهٔ جدید philo-armonica.\",\n  \"sources\": [W_PHILOS],\n  \"ref_check\": [POK_SUP,\n    {\"ref\": \"SYN:1110\", \"status\": \"supports\",\n     \"note\": \"Quoted from the root's own NOTE. SYN.txt, printed page 1110 (the page numeral '1110' stands two lines above): 'Grk. φιλέω “love” (have affection for), φιλία “friendly love, friendship”, fr. φίλος “dear”, sb. “friend”, in Hom. also “one's own”, this perh. the earliest sense and so fr. an Anatolian word represented by Lyd. bilis “one's own”. Kretschmer, IF 45.267 ff.' — exactly what Nourai reports.\"}],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 153-154\", \"stance\": \"supports\",\n     \"note\": \"'bhili-, bhilo- ‚ebenmäßig, angemessen, gut, freundlich‘. Mir. bil (*bhi-li-) ‚gut‘, gall. Bili- in PN Bili-catus, Bilicius usw., ahd. bila- ‚gütig‘ … ahd. bil-lich ‚geziemend‘ … mhd. unbilde … nhd. Unbilde.'\"},\n    {\"src\": \"WLD\", \"where\": \"Bd. II p.185\", \"stance\": \"supports\",\n     \"note\": \"'bhilo- etwa „in gutem Sinne ebenmaßig, angemessen, gut, freundlich“. Vermutlich gr. φίλος „lieb, wert usw.“ … Ir. bil „gut“, gall. Bil- in vielen EN.' — Pokorny's direct forerunner (his own reference 'WP. II 185').\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. bhilo-\", \"stance\": \"supports\",\n     \"note\": \"'bhilo-. Dear, familiar. Possible source of Greek philos, dear, loving (> philein, to love): -PHILE, -PHILIA, PHILO-, -PHILOUS, PHILTER; PAM. [Pok. bhili- 153.]'\"},\n    {\"src\": \"IEC\", \"where\": \"Mann, s.v. bhilos (1)\", \"stance\": \"supports\",\n     \"note\": \"'bhilos (1) “good, fair, friendly, pleasant”. WP II, 185  Myc. piro- (*philo-); Gk. phílos; OIr. bil (1) “fortunate” … MHG bil-lich, -liche “fair, fairness”.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck p.1110 (16.27 LOVE), p.1113 (16.28 DEAR)\", \"stance\": \"partial\",\n     \"note\": \"Buck prefers the Anatolian source for Greek φίλος and does not connect it with the Germanic/Celtic 'billig' family.\"}],\n  \"nodes\": nodes,\n}\n\ndoc = {\n  \"pdf_page\": 96,\n  \"book_page\": 66,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": [entry0],\n}\n\nwith open('/home/sfmqrb/git/rishe/data/verification/page-96.json', 'w', encoding='utf-8') as f:\n    json.dump(doc, f, ensure_ascii=False, indent=1)\n    f.write('\\n')\nprint('written', len(nodes), 'nodes')\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk96.py && python3 -m json.tool /home/sfmqrb/git/rishe/data/verification/page-96.json > /dev/null && echo \"JSON OK\" && python3 /home/sfmqrb/git/rishe/tools/verify_check.py 96",
 "description": "Write and validate page-96.json"
}
```


### [2026-09-05T14:35:31.146Z] TOOL RESULT

```
written 22 nodes
JSON OK
nodes verified: 22/22
node verdicts: {'plausible': 9, 'confirmed': 12, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 6, 'supports': 8, 'not_checked': 12, 'contradicts': 1}
books consulted: {'partial': 11, 'supports': 30, 'contradicts': 4, 'silent': 9} | by book: {'KLN': 20, 'SKT': 13, 'AHD': 4, 'MON': 4, 'FSD': 4, 'BQT': 2, 'IEC': 1, 'SYN': 1, 'WLD': 1, 'FVQ': 1, 'ARB': 1, 'HRN': 1, 'LKT': 1}
```


## [2026-09-05T14:35:52.044Z] AGENT

Page 96 (book page 66) verified — `/home/sfmqrb/git/rishe/data/verification/page-96.json`, `verify_check.py 96` shows 0 PROBLEM lines.

**Counts** — 1 entry (5 redirect stubs skipped), 22 nodes: root confirmed; nodes 12 confirmed, 9 plausible, 1 transcription_suspect. Ref checks: 8 supports, 6 partial, 1 contradicts, 12 not_checked. 55 `consulted` entries across POK, WLD, AHD/Watkins, IEC (Mann), SYN (Buck), KLN, SKT, FSD, MON, BQT, HRN, FVQ, ARB, LKT.

**Root** — Pokorny IEW 153-154 has `bhili-, bhilo- ‚ebenmäßig, angemessen, gut, freundlich‘` verbatim; WLD II 185, Mann and Watkins agree, so root name/label/gloss are right. Nourai's own note ("SYN:1110 claims this is an Anatolian word") checks out word for word against Buck p.1110.

**transcription_suspect**
- #19 `philo-anthôpos` — the Greek word is φιλάνθρωπος; the *r* is missing. Rendered PDF p.96 at 600 dpi: **the printed book itself prints "philo-anthôpos"**, so this is Nourai's misprint, `error_in: "book"`, extraction faithful. Page image copied to `data/verification/sources/refs/ocr/BOOK/96.png`.

**Notable `plausible` calls (no `disputed` on this page)**
- #1 `philos` — Pokorny p.154 (the very page cited) does *not* affirm the derivation; it only reports Kretschmer's Anatolian/Lydian *bilis* alternative. Watkins hedges ("Possible source"), Klein says "of uncertain origin", Beekes rejects it outright. Mann and WLD do include it, so: one accepted option, not consensus.
- #8/#9/#10 `philo-armonica` — not a Greek word. Klein and Etymonline: English philharmonic (1813) < Fr. philharmonique (1739) < It. filarmonico; no Latin stage.
- #12 Philadelphia is not from French — Penn named it from Greek in 1682 (the -ia ending shows it); the French parent holds only for Philip and philharmonic.
- #14/#15/#16 Syphilis — Klein/F&W do give sūs + philos, but Etymonline notes Fracastoro's intent is unknown (rival: alteration of Ovid's Sipylus). The **"French" language box is wrong**: the coinage is New Latin, Verona 1530. Likely source of Nourai's error: Funk & Wagnalls tags English syphilis "[F.]".
- #3 `falsafah` — the direct model of the abstract noun is φιλοσοφία; φιλόσοφος is the model of فيلسوف. TAD's entry (leaf 56 ≈ printed p.51-53) confirms the Greek source.

**Reference-page discrepancy the owner may want to note** (not a data error): `KLN:1561` on node #16 — Klein's syphilis entry is at KLN_1966 leaf 827 ≈ printed p.1630; p.1561 falls in the "spittle/spot" range. Content supports, page number does not.

**Extraction errors found: none.** Every transliteration, gloss, Persian script form and arrow in `data/extracted/batch/page-96.json` matches the printed page.
