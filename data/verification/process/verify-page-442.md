# Verification process log — verify-page-442


## [2026-09-14T01:55:48.448Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 442 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-442.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-442.json. Write /home/sfmqrb/git/rishe/data/verification/page-442.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 442` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T01:55:49.490Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T01:55:50.402Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T01:55:50.419Z] TOOL RESULT

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
226	Several agents run at the same time and share the scratchpad and `/tmp`, so every temporary
227	file you create must carry your page number in its name (e.g. `e0-363.json`, `pg363.png`,
228	`draft-363.json`), never a bare `e0.json` or `entry.json` — another agent will overwrite it.
229	
230	```json
231	{
232	  "pdf_page": 126,
233	  "book_page": 96,
234	  "verified_by": "claude-opus-5",
235	  "verified_on": "2026-09-05",
236	  "entries": [
237	    {
238	      "entry": 0,
239	      "root": "Dheigh, Dhigha",
240	      "verdict": "confirmed",
241	      "modern_form": "PIE *dʰeyǵʰ- 'to knead, form (clay)'",
242	      "note": "Pokorny 244 dheiĝh-; AHD dheigh-. Root, language label and gloss all correct.",
243	      "note_fa": "ریشهٔ هندواروپایی آغازین *dʰeyǵʰ- «خمیر کردن، شکل دادن (گِل)» … ادعای نورایی درست است.",
244	      "sources": ["https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/dʰeyǵʰ-"],
245	      "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
246	      "consulted": [{"src": "WLD", "where": "Bd. I 833", "stance": "supports", "note": "…"}],
247	      "nodes": [
248	        {
249	          "id": 6,
250	          "lang": "Avestan",
251	          "words": "pairi-daeza",
252	          "verdict": "confirmed",
253	          "derivation": "Av. pairi-daēza- 'walled enclosure' = pairi 'around' (PIE *per-) + daēza- 'wall' …",
254	          "derivation_fa": "«پردیس» … اوستایی pairi-daēza- «دیوارکشیده، باغِ محصور» از pairi «پیرامون» و daēza- «دیوار» …",
255	          "sources": ["https://en.wiktionary.org/wiki/pairidaēza"],
256	          "ref_check": [{"ref": "POK:244", "status": "supports", "note": "…"}],
257	          "consulted": [{"src": "BRT", "where": "col. 866", "stance": "supports", "note": "…"}]
258	        }
259	      ]
260	    }
261	  ]
262	}
263	```
264	
265	Rules:
266	- Include EVERY node of every non-redirect entry on the page (even empty-word pass-through
267	  nodes like `[Latin] refs=None |` — give them a one-line derivation and a verdict).
268	- `words` = the transliterations of the node joined by "; " (copy from the chart).
269	- `derivation` must be specific: forms, sound changes, dates/eras, texts or peoples,
270	  semantic shifts. 1–5 sentences. No hand-waving like "derived regularly".
271	- Keep `note` on the entry for root-level comments and for anything cross-cutting.
272	- If a node lists several words, cover each word; if they differ in verdict, use the worst
273	  verdict for the node and explain per word in `derivation`.
274	- Where the chart's own NOTE already records a dispute, evaluate it: say which side modern
275	  scholarship takes.
276	- Every node has `ref_check` (array, may contain a single `not_checked` item) AND `consulted`
277	  (array) AND `derivation_fa` (string); every entry has `note_fa`.
278	- Valid JSON only. Test it with `python3 -m json.tool` before finishing, then run
279	  `python3 /home/sfmqrb/git/rishe/tools/verify_check.py <pdf page>` — it must show 0 PROBLEM lines.
280	- When done, reply with a SHORT summary (≤ 15 lines): counts of verdicts per page, and a
281	  bullet per `disputed` / `transcription_suspect` item (root, word, one-line reason), plus
282	  any extraction errors (JSON differs from the printed page) the owner must fix.
283	  Do not paste the JSON back into your reply.
284	
```


## [2026-09-14T01:55:50.901Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-442.txt"
}
```


### [2026-09-14T01:55:50.932Z] TOOL RESULT

```
1	=== PDF page 442 (book page 412) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Sem 1, Sm : None  (refs POK:902,904)  PART 2
4	#1 (parent #0) [Avestan] refs=POK:902-904; HRN:30 | han-jâmana : come together ☞Gwa ; han-jâma : come to end ☞Gwa ; han-gmatana : place to get together ☞Gwa ; han-vaěg : swing together, excite ☞Weik 1
5	  #2 (parent #1) [Persian] refs=BQT:166,167,2368 | anjoman «انجمن» : association ; anjâm «انجام ( سرانجام )» : ending, conclusion ; Ekbâtân «اکباتان ( همدان )» : name of a city ; angîxtan «انگیختن ( انگیزه )» : to excite
6	#3 (parent #0) [Avestan] refs=BQT:172 | han-davatha : depressed ☞Dheu 2 ; han-du : to smear together ☞Dheu 3 ; han-dareza : pull together, fortify, advise ☞Dher 1 ; han-gama : at the same time, during ☞Gwa
7	  #4 (parent #3) [Persian] refs=BQT; MON | andŭh «اندوه» : sorrow ; andŭdan «اندودن» : to smear ; andarz «اندرز» : advice ; hengâm «هنگام» : time
8	#5 (parent #0) [Old Persian] refs=KNT:211,212 | ha 1 : one, with ; ha-dâ : with ; ham : together ; ham-karta : cooperation ☞Kwer
9	#6 (parent #0) [Greek] refs=AHD; KLN:1557; IEC:1246 | homos, homalos : same ; sun : together ; sun-phonos : harmonious sound ☞Bhâ 2 ; sun-ballein : throw together, compare, symbol ☞Gwel 1 ; sun-posion : drink together ☞Pô 2
10	  #7 (parent #6) [French] refs=None | homogene ; symphonie ; symbole ; symposium
11	    #8 (parent #7) [Persian] refs=MON:1921; VOP:372 | homožen «هموژن» ; samfonî «سمفونی» ; sambol «سمبول» ; sampozîyom «سمپوزیوم»
12	    #9 (parent #7) [English] refs=AHD | symphony
13	  #10 (parent #6) [Latin] refs=None | 
14	    #11 (parent #10) [English] refs=None | homogenous, symbol, symposium
15	#12 (parent #0) [Russian] refs=AHD:1148 | samo-war, samo-vari, samo-varitî : self boiler ☞Wer 5
16	  #13 (parent #12) [Persian] refs=MON:1918 | samâvar «ساموار» : "self boiler"
17	#14 (parent #0) [Germanic] refs=AHD | 
18	  #15 (parent #14) [English] refs=None | same, some, seem
19	#16 (parent #0) [Latin] refs=AHD | 
20	  #17 (parent #16) [English] refs=AHD | single, simple, sincere, similar ; simulate, simultaneous, resemble, assemble
21	
```


## [2026-09-14T01:55:53.665Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-442.json",
 "description": "Read source JSON for page 442"
}
```


### [2026-09-14T01:55:53.710Z] TOOL RESULT

```
{
  "pdf_page": 442,
  "book_page": 412,
  "entries": [
    {
      "root": {
        "name": "Sem 1, Sm",
        "lang": "Indo-European",
        "refs": "POK:902,904",
        "gloss": null
      },
      "part": 2,
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:902-904; HRN:30",
          "words": [
            {"translit": "han-jâmana", "gloss": "come together", "script": null, "see": ["Gwa"]},
            {"translit": "han-jâma", "gloss": "come to end", "script": null, "see": ["Gwa"]},
            {"translit": "han-gmatana", "gloss": "place to get together", "script": null, "see": ["Gwa"]},
            {"translit": "han-vaěg", "gloss": "swing together, excite", "script": null, "see": ["Weik 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:166,167,2368",
          "words": [
            {"translit": "anjoman", "gloss": "association", "script": "انجمن"},
            {"translit": "anjâm", "gloss": "ending, conclusion", "script": "انجام ( سرانجام )"},
            {"translit": "Ekbâtân", "gloss": "name of a city", "script": "اکباتان ( همدان )"},
            {"translit": "angîxtan", "gloss": "to excite", "script": "انگیختن ( انگیزه )"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "BQT:172",
          "words": [
            {"translit": "han-davatha", "gloss": "depressed", "script": null, "see": ["Dheu 2"]},
            {"translit": "han-du", "gloss": "to smear together", "script": null, "see": ["Dheu 3"]},
            {"translit": "han-dareza", "gloss": "pull together, fortify, advise", "script": null, "see": ["Dher 1"]},
            {"translit": "han-gama", "gloss": "at the same time, during", "script": null, "see": ["Gwa"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Persian",
          "refs": "BQT; MON",
          "words": [
            {"translit": "andŭh", "gloss": "sorrow", "script": "اندوه"},
            {"translit": "andŭdan", "gloss": "to smear", "script": "اندودن"},
            {"translit": "andarz", "gloss": "advice", "script": "اندرز"},
            {"translit": "hengâm", "gloss": "time", "script": "هنگام"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:211,212",
          "words": [
            {"translit": "ha 1", "gloss": "one, with", "script": null},
            {"translit": "ha-dâ", "gloss": "with", "script": null},
            {"translit": "ham", "gloss": "together", "script": null},
            {"translit": "ham-karta", "gloss": "cooperation", "script": null, "see": ["Kwer"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD; KLN:1557; IEC:1246",
          "words": [
            {"translit": "homos, homalos", "gloss": "same", "script": null},
            {"translit": "sun", "gloss": "together", "script": null},
            {"translit": "sun-phonos", "gloss": "harmonious sound", "script": null, "see": ["Bhâ 2"]},
            {"translit": "sun-ballein", "gloss": "throw together, compare, symbol", "script": null, "see": ["Gwel 1"]},
            {"translit": "sun-posion", "gloss": "drink together", "script": null, "see": ["Pô 2"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "French",
          "refs": null,
          "words": [
            {"translit": "homogene", "gloss": null, "script": null},
            {"translit": "symphonie", "gloss": null, "script": null},
            {"translit": "symbole", "gloss": null, "script": null},
            {"translit": "symposium", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 7,
          "lang": "Persian",
          "refs": "MON:1921; VOP:372",
          "words": [
            {"translit": "homožen", "gloss": null, "script": "هموژن"},
            {"translit": "samfonî", "gloss": null, "script": "سمفونی"},
            {"translit": "sambol", "gloss": null, "script": "سمبول"},
            {"translit": "sampozîyom", "gloss": null, "script": "سمپوزیوم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 7,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "symphony", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 6,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "homogenous, symbol, symposium", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 0,
          "lang": "Russian",
          "refs": "AHD:1148",
          "words": [
            {"translit": "samo-war, samo-vari, samo-varitî", "gloss": "self boiler", "script": null, "see": ["Wer 5"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "Persian",
          "refs": "MON:1918",
          "words": [
            {"translit": "samâvar", "gloss": "\"self boiler\"", "script": "ساموار"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 15,
          "parent": 14,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "same, some, seem", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 16,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 17,
          "parent": 16,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "single, simple, sincere, similar", "gloss": null, "script": null},
            {"translit": "simulate, simultaneous, resemble, assemble", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-14T01:55:54.700Z] TOOL CALL #4: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo ---- && cat data/verification/sources/SOURCE_MATRIX.md | head -80",
 "description": "List verification dir and source matrix"
}
```


### [2026-09-14T01:55:54.774Z] TOOL RESULT

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
```


## [2026-09-14T01:56:00.650Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','KNT','KLN','IEC','AHD','HRN','BQT','MON','VOP','BRT','PHD','NYB','HUB','WLD','SYN','SKT','LEW','ARY','CHEUNG','LKT','TTS','FSD','WEB']:\n    if k in d: print(k, json.dumps(d[k], ensure_ascii=False)[:600]); print()\n\""
}
```


## [2026-09-14T01:56:01.144Z] TOOL CALL #6: Bash

```json
{
 "command": "head -60 data/verification/page-385.json"
}
```


### [2026-09-14T01:56:01.873Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google Books RwdkAAAAMAAJ (Nahid Shahidi 1997, no view). Purchase second-hand only."}

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
```


### [2026-09-14T01:56:01.912Z] TOOL RESULT

```
{
  "pdf_page": 385,
  "book_page": 355,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-07",
  "entries": [
    {
      "entry": 0,
      "root": "Peg",
      "verdict": "plausible",
      "modern_form": "PIE *peg- / *pōg-, *pōk-s- 'armpit, hip, loin, side' (Pokorny 792); Watkins/AHD lists the same root as *peg- 'breast'",
      "note": "Pokorny 792 prints the headword as '(peg-:) pog-: pōg-, pōk-s-' and glosses it 'Achsel, Hufte, Lende, Seite' (armpit, hip, loin, side) — the full-grade *peg- is only a bracketed, inferred variant. Nourai's headword 'Peg' with the gloss 'breast' is copied verbatim from the AHD (Watkins) appendix, which prints 'peg-. Breast.' The 'breast' sense in fact rests only on Latin pectus and Tocharian A pässäṃ / B pāścane 'the two breasts'; Sanskrit pakṣa- and Latvian paksis point to 'side, flank'. Modern scholarship (de Vaan via Wiktionary) further doubts that Lat. pectus and Skt. pakṣa- belong together at all. Root is real and the language label is right; the gloss is a one-sided simplification.",
      "note_fa": "ریشهٔ هندواروپایی آغازین که نورایی آن را Peg با معنای «سینه» آورده، در فرهنگ پوکورنی (ص ۷۹۲) با سرواژهٔ «(peg-:) pog-: pōg-, pōk-s-» و معنای «زیربغل، ران، پهلو» ثبت شده است؛ صورت *peg- تنها گونه‌ای بازسازی‌شده و درون‌کمانک است. معنای «سینه» را نورایی از پیوست ریشه‌های هندواروپایی فرهنگ AHD (واتکینز) گرفته که همان‌جا «Breast» نوشته است، ولی این معنا فقط بر پایهٔ pectus لاتین و pāścane تخاری است، حال آنکه pakṣa- سنسکریت و paksis لتونیایی بر معنای «پهلو، سو» دلالت دارند. افزون بر این، پژوهش امروزی (دِ ڤان، به نقل ویکی‌واژه) در پیوند pectus لاتین با pakṣa- سنسکریت تردید می‌کند. پس: ریشه واقعی است و برچسب زبانی درست، اما معنای داده‌شده یک‌سویه و ساده‌سازانه است — ادعای نورایی با احتیاط پذیرفتنی است.",
      "sources": [
        "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7",
        "https://en.wiktionary.org/wiki/pectus"
      ],
      "ref_check": [
        {
          "ref": "POK:792",
          "status": "partial",
          "note": "Pokorny IEW p.792 (local POK_03.txt, form-feed leaf 25) reads: '(peg-:) pog-: pōg-, pŏk-s- \"Achsel, Hufte, Lende, Seite\". Ai. pákṣa- m. \"Schulter, Flugel\" und \"Seitenpfosten\", pákṣas- n. \"Seite\"; lat. pectus \"Brust\"; lett. paksis \"Hausecke\"; toch. A pässäṃ, B päścane \"die beiden Bruste\" ... WP. II 3 f., WH. II 270.' The page number is exact; the gloss is not 'breast'."
        }
      ],
      "consulted": [
        {
          "src": "AHD",
          "where": "Watkins 1985, s.v. peg-",
          "stance": "supports",
          "note": "'peg-. Breast. 1. Suffixed variant form *pek-tos- in Latin pectus, breast: PECTORAL; EXPECTORATE, PARAPET. 2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA. [Pok. (peg-), pog- 792.]' — this is verbatim Nourai's chart (grep '^peg-' AHD_watkins1985.txt line 820)."
        },
        {
          "src": "WLD",
          "where": "Walde-Pokorny II 3-4 (WLD_Bd2_pages.txt leaf 8)",
          "stance": "partial",
          "note": "Entry headed 'pag-' (their spelling) with 'ai. pajasyá- n. Bauchgegend, Weichen, russ. pachu \"Leistengegend\", pacha \"Achselhohle\" ... ein io-St. *pagio- in cech. paze \"Arm\"' — again 'flank/armpit', no 'breast'."
        },
        {
          "src": "IEC",
          "where": "Mann, alphabetical",
          "stance": "silent",
          "note": "grep of IEC.txt for 'peg-', 'pokso-', 'pektos' returns no headword for this root."
        }
      ],
      "nodes": [
        {
          "id": 1,
          "lang": "Sanskrit",
          "words": "pakša",
          "verdict": "plausible",
          "derivation": "Sanskrit पक्ष (pakṣá-) m. is real and old (RV), but its meanings are 'wing, feather; side, flank; half (of a month); party, faction' — not 'breast'. Monier-Williams and Wiktionary give no 'breast' sense; the chart's 'breast' is imported from Nourai's root gloss. Formally pakṣa- goes back to Proto-Indo-Iranian *pakšás 'side, flank' < PIE *peg-/*pok-s-, with the regular Indo-Aryan treatment of *-ks- > -kṣ-; the Iranian cognate is Ossetic fæxs 'side'. So the arrow root -> Sanskrit is sound; only the gloss 'breast' is wrong.",
          "derivation_fa": "واژهٔ سنسکریت pakṣá- «بال، پر؛ پهلو، سو؛ نیمه (ماه)؛ دسته» از ریگ‌ودا به‌بعد گواهی شده است، اما معنای «سینه» برای آن ثبت نشده و نورایی آن را از معنای ریشه به این گره تسری داده است. از دید آوایی pakṣá- بازماندهٔ هندوایرانی آغازین *pakšás «پهلو، سو» است (خوشهٔ *-ks- در هندوآریایی به -kṣ- بدل می‌شود) و هم‌ریشهٔ آن در ایرانی، fæxs آسی به معنی «پهلو» است. بنابراین پیکان «ریشه ← سنسکریت» درست است و تنها معنای «سینه» نادرست است.",
          "sources": [
            "https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%95%E0%A5%8D%E0%A4%B7"
          ],
          "ref_check": [
            {
              "ref": "AHD",
              "status": "partial",
              "note": "Watkins 1985 s.v. peg-: '2. Possibly suffixed variant form *pek-so- in Sanskrit paksah, wing: PUNKA.' Watkins glosses the Sanskrit word 'wing' only, and marks the connection 'possibly'."
```


## [2026-09-14T01:56:39.685Z] AGENT

Now let me check the local reference library.


## [2026-09-14T01:56:43.114Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; python3 - \"$f\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8',errors='replace').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i,p in enumerate(pages):\n    if re.search(r'\\bsem-\\s*2|sem-\\s*\\n|\\bsemel\\b', p) and 'zusammen' in p:\n        print('LEAF',i, p[:200].replace('\\n',' | '))\nEOF\ndone",
 "description": "Find Pokorny sem- entry"
}
```


## [2026-09-14T01:56:44.492Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^sem-\" AHD_watkins1985.txt | head -20; echo \"----ksun\"; grep -n \"^ksun\" AHD_watkins1985.txt | head",
 "description": "AHD Watkins sem- root"
}
```


### [2026-09-14T01:56:44.746Z] TOOL RESULT

```
== POK_01.txt
364
== POK_02.txt
434
== POK_03.txt
430
LEAF 138 caniom,  sottr dern  volksetymologische  Umgestaltung  von  sicinnium  aus  gr.  aULvvig  ,Ti der  Satyrn*) ; | mit  gh  vermutlich  arm.  ez  ,einer'  (*sem-gho-?  damit  hez  ,mild.  recW schaffen'  a
```


### [2026-09-14T01:56:44.808Z] TOOL RESULT

```
1654:sem-1
----ksun
```


## [2026-09-14T01:56:48.984Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));print(d['POK']['page_offset']);print(d['AHD']['page_offset']);print(d['KNT']['page_offset']);print(d['IEC']['page_offset'])\"",
 "description": "Get page offsets"
}
```


## [2026-09-14T01:56:49.863Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1650,1720p' AHD_watkins1985.txt",
 "description": "Print AHD sem-1 entry"
}
```


### [2026-09-14T01:56:50.119Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.
leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
```


### [2026-09-14T01:56:50.241Z] TOOL RESULT

```
HOUND kwon-
HOUR yér-
HOUSEL kwen- HOUSING? kel-2
How! kWo-
sem-1
HOWL
HOWL ul-
HOYDEN kalto- HUBRIS ud- HUCKSTER keu-2 HUE! kei-2 HUGUENOT neud-, oito- HULL kel-2
HUM kem-3 HUMAN dhghem- HUMANE dhghem- HUMBLE dhghem- HUMECTANT wegw- HUMERUS omeso- HUMID wegw- HUMILIATE dhghem- HUMILITY dhghem- HUMOR wegw- HUMUS dhghem- HUNDRED dekm HUNGER kenk-2 HUNKER keu-2 HURDLE kert- HUSBAND bheue- HUSSAR kers-2 HUSTINGS tenk-1 HUT (s)keu- HYATHODE sed-2 HYDATHODE wed-1 HYDATID wed-1 Hypra_ wed-! HYDRANT wed-! HYDRANTH andh- HYDRAULIC aulo- HYDRO- wed-1 HYDROCEPHALUS ghebh-el- HYDROMEL melit- HYDROUS wed-1 Hyprus_ wed-! HYENA sil- HYGEIA gWei- HYGIENE gWej- HYGRO- wegw- HYLOZOISM _hulé HYMEN  syil- HYMNODY wed-2 HYOSCINE si- HYPER- uper HYPERBOLA gWele-1 HYPERBOLE gWelg-1 HYPERBOREAN gWere-1 HYPERKINESIA kei-3 HYPERPNEA pneu- HYPHA webh- HYPNAGOGIC ag- HYPNO- swep-! Hypnos swep-! HYPNOSIS swep-1 HYPNOTIC swep-1 HYPO- upo HYPOCHONDRIA ghrendh- HYPOCORISM ker-3 HYPOGEAL gé HYPOPHYSIS bheue- HYPOPNEA pneu- HYPOSTASIS sta- HYPOSTYLE sta- HYPOTAXIS tag- HYPOTENUSE ten- HYPOTHERMIA gWher- HYPOTHESIS dhé-1 HYPROCRISY krei- HYPSO- upo HYSTERESIS ud- HYSTERIC udero- HYSTERO- udero- HYSTERON PROTERON per!, ud-
I
I eg
ICE eis-2
ICEBERG bhergh-2 IcH dhgWher- ICHTHYO- dhghi- ICHTHYORNIS  or- ICICLE eis-2, yeg- ICON weik-3
ICONIC weik-3 ICONO- weik-3 ICONOGRAPHY gerbh- ICONOSTASIS  sta- ICOSAHEDRON  wikmti ID I
IDEA weid-
IDEM I-
IDENTICAL j-
IDENTIFY i- IDENTITY i-
IDEO- weid-
IDIO- s(w)e- IDIOM s(w)e- IDIOMORPHIC s(w)e- IDIOPATHY s(w)e- IDIOSYNCRACY kere- IDIOSYNCRASY s(w)e- IDIOT s(w)e- IDOCRASE weid- IDOL weid- IDOLATER [é-1 IDYLL weid-
IF |-
IGNEOUS egni- IGNITE egni- IGNITRON egni- IGNOMINY no-men- IGNORANT gné-
IGNORE gno- ILEUS wel-3 ILK i-
ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
IN-2 en INAMORATA amma INAUGURATE aug-! INCANDESCE kand- INCANTATION kan- INCARCERATE cGarcer INCARNATE sker-1 INCENDIARY kand- INCENSE kand- INCENTIVE kan- INCEPTION kap- INCERTITUDE krei- INCEST kes-2 INCH! i-no- INCHOATE kagh-
94
INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
INERT ar-
INERTIA ar- INEXORABLE 6r- INFAMOUS bha-2 INFANT bha-2 INFANTRY bha-2 INFARCT bhrekw- INFECT dhé-1 INFELICITY dhé&(i)- INFER_ bher-1 INFERIOR ndher- INFERNAL ndher- INFERNO ndher- INFEST dhers- INFEUDATION peku- INFIDEL bheidh- INFIRM dher-2 INFIRMARY dher-2 INFIX dhigw- INFLAME bhel-1 INFLATE bhié-2 INFLICT  bhiig- INFLUENCE bhieu- INFLUENZA bhleu- INFRA- ndher- INFRACT bhreg- INFRANGIBLE bhreg- INFRINGE bhreg- INFUSE gheu- INGENIOUS gene- INGENUOUS gene- INGEST gerere INGRATE gWere-3 INGRATIATE gWere-3 INGRESsS ghredh- INGUINAL engW- INGURGITATE gWere-4 INHABIT ghabh- INHERE ghais- INHERIT ghé- INHIBIT ghabh- INHUME dhghem- INIMICAL amma INITIAL ej-1 INITIATE ei-1 INJECT yé- INJUNCTION yeug- INJURY yewes- INK kéu-
INNATE gene- INNER en INNOCENT nek=! INNOCUOUS_nek-1 INNOVATE newo- INNUENDO neu-2 INOCULATE okw- INORDINATE ar- INOSCULATE 6s- INOSITOL wei-1 INOTROPIC wei- INQUILINE kWel-1
IRE
INQUIRE quaerere INSCRIBE skribh- INSECT sek- INSERT ser-3, s6-1 INSESSORIAL sed-1 INSIGNIA sekw-1 INSIST sta- INSOLATE sawel- INSOMNIA swep-! INSPECT spek- INSPIRE spirare INSTALL | stel- INSTALLMENT! | stel- INSTANT sta- INSTAURATION sta- INSTIGATE | steig- INSTINCT | steig- INSTITUTE sta- INSTRUCT  ster-2 INSULT sel-4 INSURE cura INTACT tag- INTEGER tag- INTEGUMENT (s)teg- INTELLIGENT leg-1 INTEND ten-
INTER en, ters- INTERCALATE kela-2 INTERCEDE ked- INTERCEPT kap- INTERCOSTAL kost- INTERCOURSE kers-2 INTERDICT deik- INTEREST es- INTERIM en INTERIOR en INTERJECT yé- INTERLOCUTION  tolkw- INTERLOPE klou- INTERLUDE leid- INTERMEDIATE medhyo- INTERMIT (S)meit(a)- INTERNAL en INTERNECINE nek-1 INTERPELLATE pel-6 INTERPOSE apo- INTERPRET per-68 INTERREX reg-1 INTERROGATE reg-1 INTERRUPT reup- INTERSECT sek- INTERSPERSE (s)preg- INTERSTICE sta- INTERVAL walso- INTERVENE gWa- INTERVIEW weid- INTESTINE en INTIMA en INTIMATE? en INTINCTION  teng- INTINE en
INTRA- en INTRADOS dorsum, en INTRANSIGENT ag- INTREPID  trep-1 INTRINSIC en, sekw-1 INTRO- en INTRODUCE deuk-, en INTROIT el-1, en INTROMIT en, (s)meit(a)- INTRORSE en, wer-3 INTROSPECT en, spek- INTROVERT wer-3 INTRUDE treud- INTUITION teu- INTUMESCE teue- INTUSSUSCEPTION en, kap- INULIN wel-3 INUNCTION ongw- INUNDATE wed-! INURE op-! INVADE wadh-2 INVAGINATE wag- INVALID! = wal- INVALID2  wal- INVEIGH wegh- INVEIGLE okw- INVENT gWa- INVERT wer-3 INVEST wes-4 INVETERATE wet-2 INVOKE wekw- INVOLVE wel-3 INWARD wer-3 IODOPSIN  okw-
ION eij-1
IRASCIBLE eis-1 IRATE eis-1
TRE eis-1
IRIDACEOUS
IRIDACEOUS wei-1 IRIDIUM wei-1 IRIDO- wei-1 TRIS wei-1
Irts_ wei-1
IRISH peie- IRISITIS _ wei-1 IRON eis-1 IRONY wer-6 IRREMEABLE mei-1 IRRIGATE reg-2 IRRUPT reup-
Is es- ISALLOBAR gWere-2 ISCHEMIA segh- ISINGLASS bhié-2 ISLAND akwa- ISOBAR gWere-2 ISOCLINE klei- ISOGLOss glogh- ISOHEL sawel- ISOHYET seue-2 ISOMER (S)mer-2 ISOMETRIC mé-2 ISOPIESTIC sed-1 ISOPLETH pele-1 ISOSCELES skel-3 IsosTasy sta- ISSUE ei-1
IT ko-
ITEM I-
ITERATE I- ITHYPHALLIC bhel-2 ITINERANT ei-1 ITINERARY el-1 Iwis_ weid-
J
JAIL keue-2
JAIN gWeio-
JAMB kamp- JANITOR ei-1 JANUARY ei-1 Janus ei-1 JAVELIN ghabholo- JEALOUS ya- JELLY gel-3 JEOPARDY yek- JESS yé-
JEST gerere
JET2 yé-
JEWEL yek-
JINX yu-2
JOCOSE yek- JOCULAR yek- JOIN yeug-
JOIST yé-
JOKE yek-
goss deiw- JOURNAL deiw- JOURNEY deiw- JOUST yeug- JovE deiw- JOVIAL deiw- JOWL! gep(h)- JOWL2 gwel-3
JOY gau- JUBILATE yu-2 JUDGE deik-, yewes- JUDICIAL deik- JUGATE yeug- JUGGERNAUT gWa- JUGGLE yek- JUGGLER yek- JUGULAR yeug- JUGUM yeug- JUICE yeue- JULEP ap-2, wrod- JuLY deiw- JUNCTION yeug- JUNCTURE yeug- JUNIOR yeu- JUNKER kei-2, yeu- JUNTA yeug- JUPITER deiw- JURAL yewes- JURIDICAL deik-, yewes- JURISCONSULT yewes- JURISDICTION deik-, yewes- JURISPRUDENCE yewes- JURIST yewes- JURY! yewes- JUSSIVE yeudh- susTl yewes- JusTiFy dhé-1
JUVENILE yeu- JUVENOCRACY yeu- JUXTAPOSE yeug- JUXTAPOSITION yeug-
K
KalILYARD SCHOOL kaul- KAINITE ken-3 KALE kaul- KALEIDOSCOPE kal-2, weid- KaMA kas KAMASUTRA ka-, syii- KAME gembh- KARMA kWer-1 KARYO-  kar-1 KEEL! gWel-3 KEEL? ku-
KEEL’ gel-3 KEELHAUL kele-2 KEELSON ku- KEESHOND kwon- KEN gno- KENNEL! kwon- KENNING gno- KENO penkwe KENOSIS ken-4 KERATIN ker-! KERATO- ker-1 KERCHIEF kaput KERF gerbh- KERMES k*rmi- KERN! kat-2 KERNEL gre-no- KEVEL kleu-3 KEY? kagh-
KILL! gWel-1
KILN pekw-
KILO- gheslo-
KIN gene-
KIND! gene- KIND? gene- KINDERGARTEN gene-, gher-1 KINDRED af-, gene- KINE gWou- KINEMATICS kei-3 KINESIOLOGY kei-3 -KINEsIS_ kei-3 KINESTHESIA kei-3 KINETIC kei-3 KING gene-
KININ kei-3
KIRK keue-2 KIRTLE_ sker-1 KISHKE (8)keu- Kiss kus- KITCHEN pekw- KITH gndé-
KITTLE tit- KLEPTOMANIA klep- KLIPSPRINGER spergh- KLOOF gleubh- KLUTZ gel-! KNACKER ken-5 KNACKWURST gen- KNAP! §gen- KNAP2 gen- KNAPSACK gen- KNAR gen- KNEAD gen- KNEE genu-1 KNEEL genu-! KNELL gen- KNIFE gen-
KNIT gen-
```


## [2026-09-14T01:56:54.524Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^sem-1\\|^sem-2\\|^sem-3\\|^sem-\" AHD_watkins1985.txt | head; echo \"=== ksun/sun\"; grep -n \"ksun\\|xun, with\" AHD_watkins1985.txt | head",
 "description": "Locate AHD sem- entries"
}
```


### [2026-09-14T01:56:54.592Z] TOOL RESULT

```
1654:sem-1
=== ksun/sun
648:English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
2281:SPRINGE spergh- SPRINKLE (8)preg- SPRIT sper-4 SPROUT sper-4 SPRY (s)preg- SPUME (S)poi-mo- SPUR spere- SPURGE peue- SPURN spere- SPURRY (s)preg- SPURT sper-4 SPUTNIK ksun, pent- SPUTTER spyeu- SPUTUM spyeu- SPY spek- SQUAD kWetwer- SQUALENE (8)kWal-o- SQUARE kWetwer- SQUASH2 kwét- SQUAT ag- SQUIRE skei- SQUIRREL ors-, skeoi- STABLE! sta- STABLE? sta- STACK steg- STACTE stag- STADDLE sta- STADHOLDER sta- STAFF! stebh- STAG stegh- STAGE sta- STAGGER steg- STAGNANT stag- STAIN teng-
2331:SWING sweng(w)- SWINGE sweng(w)- SWINGLETREE sweng(w)- SWIRL swer-2 SWITCH swei-2 SWIVEL swei-2 swoop swei-2 SWORD swer-4 SYCAMORE moro- SYCOPHANT bha-! SYLLABLE (s)lag’- SYLLEPSIS (s)lag¥- SYLLOGISM leg-1 SYMBIOSIS gWei- SYMBOL gvele-1 SYMPATHY kWent(h)- SYMPATRIC peter- SYMPHONY bha-2 SYMPHYSIS bheue- SYMPODIUM ped-! SYMPOSIUM pd@(i)- SYMPTOM pet- SYN- ksun SYNAGOGUE ag- SYNALEPHA leip-
```


## [2026-09-14T01:56:56.040Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('POK_03.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(134,146):\n    p=t[i]\n    print('===== LEAF',i)\n    print(p[:3000])\nEOF",
 "description": "Print Pokorny leaves around sem-"
}
```


### [2026-09-14T01:56:57.149Z] TOOL RESULT

```
===== LEAF 134
Hof,  sei  {*salja-)  , Sennhütte^;  got.  saljan  ,einkehren,  bleiben*, salipwös  PI.  ,Einkehr,  Herberge',  ahd.  salida,  as.  selitha,  ags.  seid  ,Woh- nung';  abg.  selo  ,fundus,  Dorf,  selitva  ,Wohnung'  (bildungsähnlich  dem got.  salipwös)]  lit.  salä  f.  ,Dorf'.
WP.  II  502  f.,  Trautmann  248.
2.  sei-,  suel-  ,Balken,  Brett,  aus  Stämmen  oder  Brettern  Verfertigtest
Ags.  selma,  sealma,  as.  selmo  ,Bett',  eig.   ,das  hölzerne  Bettgestell^* suolas  ,Bank',  lit.  slle  ,Trog,  Schweinetrog',  lett.  sile  , Krippe,   Trog';  M gjole  ,Platte,  auf  die  man  Viehsalz  legt'  {*selä).
Mit  Anlaut  su-:  gr.  aeXi-Kx,  -azog  (bei  Hes.  auch  el^ara)   ,Balken,
899
,1,    Gerüst,  bes.  Schiffsverdeck,  Ruderbank^,  hom.  i'ßaasXuog  ,mit  guten -    Ruderbänken  verseben',  GsXlg^  -Idog  ^Planke,  Ruderbank';  ebenso  abd.  swelli, hd.  sioelle  , Balken,  Grundbalken,  Schwelle^  aisl.  svalar  f.   PL,   ascbwed, caU  , Galerie*,   nisl.   svoli  ,Holzklotz^,   e-stufig  aisl.   stvill  f.  ^Grundbalken, g  j^^velleS  schwundstufig  ags.  syll,  aisl.  syll  ds.,   mnd.   sill,   süllßj   sille  ds. AVP.  IlöOSf.
l      gel-  _,nebmen,  ergreifen'.
Qr.  iletv  ,nehmen,  in  die  Gewalt  bekommen',  eXcog  n.,  iXcbgiov  ,Beute, Raub,  Fang';  fraglich  lat.  cönsilium  ,Ratsversammlung,  Entschluß^-  cönsu- l^e  senatum  ,den  Senat  versammeln',  dann  »befragen',  Wurzelnomen  cönsul, Konsul';
dazu  als  -wo-Ableitung  air.  selb  f.,  cymr.  helw  m.  , Besitz',  gall.  (Julia) Luguselva  Frauenname  (,* Eigentum  des  Lugus'),  wozu  air.  ad-selb-  ,bezeu- <ren',  to-ad-selb-  , zuweisen,  vorzeigen',  to-selb  , behalten';  vielleicht  auch  auf Grund  einer  Basis  "^slei-i  ir.  stt-  m  fuil{l)em  , Zinsen'  (*fo-sTt-mo-)j  adroilliu verdiene'  {ad-ro-sVt-)^  -tuillim  ds.  {to-sVt-)'^  cymr.  dyrllydduy  bret.  deleza ,verdienen'  (*to-ro-sli-i-);
als  Kausativ  ,nehmen  machen'  hieher  got/  salj an  ,darbringen,  opfern*, aisl.  selia,  as.  gisellian,  ahd.  seilen^  ags.  sellan  ,übergeben,  verkaufen';  die Nomina  aisl.  sal  n.  , Bezahlung',  sala  f.,  ags.  salu  ,yerkauf'/  ahd.  sala  ,Uber- gabe  eines  Gutes',  sal  m.  ,Gut,  das  laut  Testamentes  zu  übergeben  ist' müssen  postverbal  sein;  hierher  aksl.  s^h 
===== LEAF 135
 ,Bote',  s^lat^  , schicken'.
WP.  II  504  f.,  Trautmann  292.
4.  sei-  jSpringen*.
Ai.  ucchalati  ,schnellt  empor'  (mind.  aus  *ud-salati)]
gr.  ScXXofxccL  ,springe,  hüpfe'  (*Stliö),  ep.  Aor.  älro,  Verbaln.  ^Ifxa  , Sprung', älaig  ,das  Springen' ;
lat.  saliö^  -Ire,  -ui  (-li),  -tum  , springen,  hüpfen',  saltus  , Sprung',  salax jgeil',  saltäre  ,tanzen',  salebra  ,holprige  Stelle  des  Weges'  (gebildet  nach latebra)  ;  wozu  insultäre  ;
mir.  saltraid  ,zertritt',  Yerbalnomen  cymr,  sathru  , Zertreten',  mbret. saotra  , Beschmutzen',  Vannes  sautrein  , Zertreten,  Beschmutzen';
lit.  ätsala  ,Wasserlache',  sdlti  ,fließen',  apr.  salus  ,Regenbach';  über  lit. salä^  lett.  sala  ,Insel'  s.  Mühlenbach-Endzelin  III  664;
eine  p-Erweiterung  in  lit.  salpas  m.  ,Bucht,  Busen*  =  slav.  *solp^  in slov,  släp  jWasserfall,  Woge';  slav.  ^seljpjg,  ^shlpati  ,springe*  in  aksl. 'm>-sUpljq  ds.,  Inf  in.  ksl.  shpati.
WP.  II  505,  WH.  II  468,  Trautmann  256.
57*
900  '
5-  sei-  jSchleiclien,  kriechen*.
Ai.  tsdrati  ,schleicht,  schleicht  heran,  heschleicht*  mit  Präfix  [a]d-^  tsdr^. m.  »schleichendes  Tier*,  av.  srvant-,  sravant-  ,schleichend,  anschleichen^» (Part,  von  ar.  *tsr-au-^  «-Erw.  hzw.  u-Fvä-S.) ;  so  vielleicht  auch  arm.  soK»  \ Aor.  solecay  ,serpo,  repo,  delabor,  trahorS  solun  ,humi  serpens,  repej^ji (*t-sol-  mit  Wandel  von  ts-  zu  s-?);  gr.  eiXlrtoSag  ßovg  (Akk.)  ,schleppfuQju' (eigentlich  ,schleichfüßigS  vgl.:)  €ihTSvr;g  Beiwort  der  Quecke,  ,die  aick' schleichweise  ausdehnende' (metr.  Dehnungen  für  iXc-)]  alb.  sÄ%e  , Schlang« Natter*;  air.  selige^  mir.  seilche  (^selekio-)  , Schildkröte,  Schnecke*;  air *8elid  »schleicht,  kriecht*,  Verbalnomen  sleitli  {*sleth  aus  *slfä)  ,das  Be-"  ^ schleichen  einer  schlafenden  Frau^  intled  f.  »Fallstrick*  (*ind-sleth)i  nifl"^ seilide  »Schnecke'  (air.  *seUt  aus  *sel-nti):  lit.  selü,  seleti  ^schleichen,  leite -^ auftreten*.
WP.  II  505 f.,  Trautmann  255,  M.  O'Brien  Et.  celt.  3,  370 f.;  E.  Schneider WuS.  21,  166  ff.
^.  sei-,  selQ- : slä-  , günstig,  guter  Stimmung;  begütigen^
Lat.  sölor^  -ärl  , trösten,  lindern,  beschwichtigen*;  air.  slän  ,heil,  gesund*?'"  ' germ.  *sßZ-  in  got.  sels  ,gut,  tauglich',  selei  ,Güte',  aisl.  s^ll  , glücklich*, ags.  sWl  m.  f.  , Glück,  Gelegenheit,  Zeit',  gesälig  ,glücklich',  ahd.  as.  sälUH ,glücklich,  selig,  gesegnet*,  ahd.   sälida  ,Güte,   Glück,   Heil*  =  as.  sälda^ ags.  sxld,  anord.  sxld  f.  ,Glück*;  *söl-  in  ags.  selra  (*söUza)  , besser',  Adr, sei  »besser*;
Auf  einer  schweren  Basis  '^s(e)ld-:slä-  beruht  die  griech.  Sippe  von  *fti;fii {*OL-aXr]-fiL)  ,bin  günstig,  gnädig*,  Imp.  hom.  ^iXr]'d^t,  theokr.  'iläd^i  (^al-aXä-di),-' woneben  als  Perf.-Imp.  äol.  eXXa^i  (*ae-oXcc&i)',  unredupl.  Präs.  iXaiutif']^ nach  dem.  redupl.  iXa-  umgefä
===== LEAF 136
 =  \X&si^ bei  Steph.  Byz.)  wie  auch  xXaqög  ,heiter,  froh*  aus  ^kXaqog]  lXaay.O[xaL  (*(Tt- iyXä-üKO(,iaL)  ,mache  mir  jemanden  günstig  gesinnt,  versöhne';  auf  Grund des  Präs  iXrj-j  iXä-  einerseits  lakon.  iX7]J^og,  kret.  ^Xsog,  att.  lAfwg,  ion. Ilfiwg,  andrerseits  hom.  'iXa(J^)og,  arkad.  ^Xaog,  lesb.  ^iXXaog  ,günstig,  gnädigst WP.  II  506  f.,  WH.  II  556.
•selg-  jloslassen,  entsenden,  werfen,  ausgießen*.
Ai.  sj-jdti^  sdrjati  ,entläßt,  schießt,  gießt',  Partiz.  srstd-^  visarjana-m , Ausgießung*  (sdrga-  ,das  Entlassen,  Schießen,  Gießen'  mit  g  durch  Ent- gleisung); av.  hardzaiti,  hdrdzaiti  ,entläßt,  sendet  aus,  schickt  aus',  PartiJ. harsta-j    hardztxna-    n.    ,das    Lassen,   Verlassen;    Durchlassen,    Filtrieren* ;._„
air.  selg  f.  ,Jagd'  (vom.  Loslassen  der  Hunde,  ai.  srjdti  äünah),  sieg  L ,Speer*  (*%ä);  acymr.  in-helcha  ,venando*,  helgha-ti  ,jage!',  mcymr.  hel$, ncymr.  hei,  heia  ,jagen',  heliwr  ,Jäger',  acorn.  hellmr  ds.,  mcorn.  Jielhys^  hellt/9
h^:
901
•^o-t^;    corn.    heißa    ,Jageii*^    bret.    hem-olc'h    ,Jagd';,    di-elc'hat   ,atemlos
iiihd.  seihen  st.  V.  ^tropfend  niederfallen^  sich  senken  (von  Wolken)',  ags. L.sißcan  , entkräften^,  *ä-seolcan  , träge  sein   oder  werden^^  nur  im  Partiz. ij^olceUj  solcen  , träge,  faul'^  engl,  sulky. '  \yp.  II508.
elk-  jziehen';  solko-s  ,Zug^;  vielleicht  mit  uelk-  zu  eines  Ursprung!.  Wz.
^^lelk-  ZU  vereinigen,  s.  zuletzt  Specht  KZ  66,  25  f.
iVrm.  heig  ,langsam,  träge*  (Yo"!-  ^^^^  Bed.  zögern :  ziehen,  ducere  tempiis); (TT.  ^Axw  jziehe',  öXy,r]  f.,  öXxög  m.  ,Zug;  das  Geschleppte  usw.*  =  lat. sülcus  jFurche',  sulcö,  -äre  ^pflügen^,  tiefstufig  ags.  sulh  ^Furche,  Pflügt alb.  helq,  heq  ,ziehe,  reiße  ab*  (*solke{ö) ;
alid.  selahj  ags.  seolh,  anord.  selr  , Seehund,  Robbe*  als  ,sich  mühsam schleppend*?
toch.  B  sälk-  ^herausziehen,  vorführen*.
WP.  II  507  f.,  WH.  II  627,  Frisk  77.
selos-  n.  ;Sumpf,  See*;  selesio-  ^sumpfig*.
AI.  sdras-  n.  jWasserbecken^,  Teich,  See',  Sdrasvati  f.  FIN  und  GN  (zu sdras-vant-  .wasserreich*)  =  av.  Harax^'aitl,  apers.  Hara(h)uvaU ,Ar3iChosiQn^ j ai.  sarasyd-  Adj.  , Teich-,  See-^;  gr.  eXog  n.  ^sumpfige,  bewachsene  Nie- derung*,    sleiog  ,palustris*.
WP.  II  507.
selp-  ,Fett  (Butter,  Schmalz)*.
Ai.  sarpis'  n.  ^Schmelzbutter,  Schmalz*,  sxprd-  , geölt,  glatt,  blank';  gr. elnog  (n.)  *  slaiov,  otscq  Hes.  und  (mit  cp  nach  lileKpa'.Xinog'^)  klcpog' ßovrvQOv.  KvTVOLOi  Hes.,  oXni],  bXrtig,  -löog  f.  ,Ölflasche*;  alb.  gjalp  ,Butter*; ahd.  salba^  as.  salba,  ags.  sealf  , Salbe*,  got.  ahd.  salbön,  as.  salbön^  ags. sealßan  , salben*;
toch.  A  sälyp^  B  salype  ,Fett,  Butter,  Ol'.
WP.  II  508.
i.  sem-  ,schöpfen,  gießen*.
Gr.  df.ido(j,ai  ,sammle*,  ic^rj  f.  ,Wassereimer*  (daraus  lat.  ama  ,Feuereim
===== LEAF 137
e^  nhd.  Ohm  , Flüssigkeitsmaß'),  d^iLg  f.  , Nachttopf*, ä^vLov  n.  ,Opf erschale*,  ä(.iaXXa  f.  , Garbe*  {äiuXXa),  aber  ävxXog^  -ov  , Haufen, Schiffsraum,  Kielwasser*  nach  Benveniste  ßSL.  50,  39  zu  hitt.  han-  ,giessen';
illjr.  FIN  Semnus  (Lucanien);
lat.  sentina  ,Kielwasser,  Schiffsjauche*,  sentlnö  , schöpfe  das  Wasser  aus, habe  meine  Not*:
902  $
air.  sem-  ^ausgießen'  in  to-eks-sem-  ds.,  to-uks-sem-  ,zeugen,  erzeugest Verbalnomen  teistiu  .Ausgießen',  tuistiu  ,Zeugung,  Schöpfung^  (*i!o^ui^ sem-tiö)  usw.;  vgl.  auf  Grund  einer  abstufenden  Flexion  -<^ö(n). :  .^j,^ oben  lat.  sentlna  (ursprüngl.  Adj.,  seil,  aqua);  mit  -d-  weitergebildet,«^ in  abret.  do-uo-hinnom  gl.  ,austum',  cymr.  gwe-hynnu  ,schöpfen,  ausleeren»*
lit.  semiü,  semti  , schöpfen',  sdmtis  ,ScliöpflöffelS  mit  -el-  Weiterbildani lett.  smejuj  smelt  , schöpfen'.
WP.  II  487  f.,  WH.  II  514  f.,  Trautmann  256,  Ifor  Williams  RC  40,  497 Frisk88f.
2.  sem-  ,eins'  und  ,in  eins  zusammen,  einheitlich,  samt,  mit*.
1.  Mit  vorherrschender  Zahlwortbedeutung  ,eins':
Arm.  mi  ,eins'  (*sw-uos);  gr.  slg,  h,  ^la  (*sems,  *sem,  ^^sm-id),  Gen.  k»i^A (für  *eii6g  oder  a^iög  nach  *£Vg,  h)  ,ein*;  ^iww?  , Einhufer'  (%^-wj;rJ).  \^  .-j dlid%ig,  tarent.  äiiaxig  ,einmal*,  Komp.  dor.  Hcbqoq  (att.  ersgog)  ',der  em<L* der   andere  von  zweienV  (=   cymr.   hanner^    corn.    bret.    hanter   ,Hälfte*)»
lat.   sem-per  ,in   einem   fort,   immer'  {*sem  =  gr.   ev,  vgl.   unten  germ.      \ sin-)]   simitu  .zugleich',  Ablat.  von  *si'mitus  <i*sem-eitus  ,das  Zusammen»      1 gehen*,  vgl.  air.  emith  ,tanquam,   quasi',   cymr.   hefyd  ,auch*   aus  "^semitL zu  ai.  sdm-iti- ;  mllle  ,1000'  aus  *swi  ghesll  ,eine  Tausendheit'  (irrig  S.  44( vgl.  das  in  *s7n-gheslom  zerlegte  ai.  sahdsra-m^  av.  hazaidva-  ,eintausend'F air.  cumme  .ähnlich'  aus  *kom-svino-  ,ganz  der  eine,   der  gleiche';  germ, *sin  (d.  i.  idg.  *sem  in  adv.  Erstarrung)  ,*in  einem'  =  , zusammen'  oder^J , immerwährend'  oder  .durchaus,  sehr'  in  as.  ahd.  sin-hiun,  ags.  sin-hxwwk .conjuges,   Ehegatten',   got.   sin-teins   .täglich',    as.    sin-nahti^    ags.   sin-nxki^ .ewige  Nacht',  mhd.  sin-grüene,   ags.   sin-grene^   aisl.   sl-grenn   ,immergrUn* ags.   sin-here  , großes   Heer',   ahd.   sin-fluot   ,große   Flut',   aisl.   si-valr, sine-wealty  and.  sinu-iuel  ,ganz  rund'  usw. ;
toch.  A  sas  m.  (komponiert  sa-),   B  se  (älter  ses  in   ses-ka  .allein')  auff *sem-s]    A   säm  f.   aus   *sem]   Kompos.   Form   A  soma-   (*semo-),  B  somo^ri (*somo-)]  Van  Windekens  Lexique  121.
sm-  als  1.  Kompositionsglied:  ai.  sakrt,  av.    Jia-kdrdt   , einmal'   (über sa-hdsram  s.  oben),  gr.  ä-jta^  , einmal',  ä-nlöog  , einfach',  lat.  sim-pluSj  -pUx^ , einfach',  gr.  §-y,ccTÖv  ,ein-hundert'  aus  *ä-''/.aTÖv  nach  eig  o
===== LEAF 138
caniom,  sottr dern  volksetymologische  Umgestaltung  von  sicinnium  aus  gr.  aULvvig  ,Ti der  Satyrn*) ;
mit  gh  vermutlich  arm.  ez  ,einer'  (*sem-gho-?  damit  hez  ,mild.  recW schaffen'  als  »einfach  von  Sitten'  gleich?   Federsen  KZ.  39,  414);  mit^
903
^  §dsvant-  ,sich  gleichmäßig  erneuernd^  eine  ununterbrochene  Reihe  bildend, •gjef;  ^^''  (a^s  *sa-§vant-,  mit' Formans  -uent-  von  idg.  *6ip,-ko-  etwa  ,in Einern  Zuge,  in  einer  Reihe*);  vielleicht  alb.  gjitli  ^alles^  ganz*  {^sem-Tco- von  einer  und  derselben  Art'?).
j\Iit  i-Suffixen :  gr.  oßOLlöq  , gleich,  eben,  glatt*  (,*in  einer  Art  verlaufend*) ablaut.  lat.  similis  ,ähnlich'  (*semelis  ,von  ein  und  derselben  Art'),  simul^ jilter  semol^  semul  ,zugleich'  apokopiert  aus  ^stmeli,  woneben  nach  bis, *tris(ter)  erweitertes  *semlis  , einmal^  in  semel,  umbr.  sumel  , zugleich*  (mit demselben  o  wie  öi^aXög?  oder  letzteres  erst  nach  6(.i6g  aus  *äij,aX6g  um- o-efärbt?);  mit  Red.-St.  air.  samail  ,Bild,  Gleichnis*  (proklit.  amal  ,wie*), cymr.  usw.  hafal  , ähnlich,  gleich*,  air.  samlith  ,simul*,  cosmail  ,consimilis* ; <rot.  simle  ,(*einmal  =)  einst*,  ags.  $im(b)lej  simleSj  simblon  ,immer*,  ahd. smble(s)^  simblum  ds.,  auf  einem  n.  *semlo-m  ,eine  Zeif  beruhend.
2.  SeTno-  ,einer^  =  , irgendeiner*  (unbetont):
ai.   samd-  , irgendein^,   av.   ap.    hama-  ,jeder  beliebige,   omnis^;
arm.  amen,  amen-ain  ,alle,  omnis* ;
gr.  äf-iö-  , irgend  ein^  in  d^fj,  att.  äfxfj  »irgendwie*,  d(.iöd-£v,  att.  &f.i6&ev ^irgendwoher',  d^ojg,  att.  ä^ög  ,irgendwie^  odd-afiög  ,nicht  einer,  keiner*, ovSajxcög  ,keineswegs';  got.  sums  , irgend  ein,  ein  gewisser*,  PL  , einige, manche',  aisl.  sumr  ,quidam,  nonnuUus*,   as.  ags.  ahd.  sum  ds.
3.  ,*in  eins  =  zusammen,  mit^;
srn-:  ai.  sa-hdj  sadha'^  , gemeinsam,  zusammen*  =  av.  hada^  ap.  hadä ,zusammen',  ai.  saträ  ,zusammen,  ganz  und  gar'  =  av.  Jiad-ra  »zusammen, zugleich,  vereint  mit*,  ai.  sddam,  sddä  ,allzeit,  stets  immer'  =  av.  haöa ,immer*,  ai.  sd-dhrl  Adv.  ,zusammen'  (:  Wz.  ^dher-  ,halten*,  wie  auch:) gr.  d-d-QÖoi,  att.  &-&o6oi  ,im  Verein,  gesamt',  ä-Xoxog  ,consors  tori',  d-delcpog ,couterinus',  d-v.öXovd-og  ,Weggefährte'  (aus  ä~  durch  Aspiratendiss.).  —  Ai. smdt  ,zusammen  mit',  av.  mat  ,ds.;  immer,  immerdar';  gr.  ä^ia,  dor.  &i.iä ,in  einem,  zugleich',  &1.16&L  ,zusammen'.
som-:  ai.  sdm-  ,zusammen,  zugleich  mit',  av.  ap.  ha{m)-  ,mit'  (in  Verbin- dung mit  Verben  und  in  Zs.  mit  Nomina
===== LEAF 139

===== LEAF 140

===== LEAF 141
;  arm.  ham-  ,mit'  wohl  aus  dem Iran.) ;
lit.  sam-,  sq-  (z.  B.  sam-dyti  , dingen',  sdn-dora  , Eintracht',  sq-zine  , Ge- wissen, conscientia'),  apr.  san-,  sen-  (^san-insle  , Gürtel'),  sen  (*sem)  Präp. ,mit'  (idg.  *sem);  aksl.  so-  ,mit'  (sg-sMh  , Nachbar',  vgl.  ai.  sam-sdd-  »Ver- sammlung'), sq-log^  ,consors  tori',  vgl.  ä-Xoxog  usw. ;
mit  aksl.  sg-  ablautend  ist  *s^n-,  s^  (*Som)  z.  B.  in  s^n-iti  ,convenire^, s^-vezati  , zusammenbinden'  sowie  s^  Präp.  ,mit';  falls  lit.  sü  ,mit'  dazu- gehört, könnte  es  samt  aksl.  s^  und  gr.  ^vv,  avv  ,mit'  auf  idg.  *ksu  bzw. Vcsun  zurückgeführt  werden;  vgl.  Schwjzer  Gr.  Gr.  2,  487 ^
904
f
Von  som-  stammt  somo-s:  ai.  samci-  ,ehen,  gleich,  derselbe',  samdm  Adr und  Präp.  ,zusammenS  samdyä  ,m  gleicher  Weise,  mitten  hindurch^  *samal yati  ,ebnet,  bringt  in  Ordnung',  av.  ap.  hama-  .gleich,  derselbe',  arm.  o,„^ ^irgendwer'  (Meillet  Esquisse^  90) ;  über  ai.  simä-  ,selhst*  s.  WackernageU Debrunner  3,  578;
gr.  öuög  .gemeinsam;  ähnlich,  gleich,  eben,  glatt',  öf^ov  Adv.  und  Prip^p .zusammen',  öi-iö-^ev  ,aus  demselben  Ort^  öfiö-as  ,an  denselben  Ort',  6ifio,g'Ü ,gleichwohl'   (ö^ioiog,   natt.   o^oiog  .ähnlich^;   hierher   SjXTjQog  (oben  S.  ^^ ö^aoTSO)  ,begleite'  (zu  *OLiaQTog  aus  *som-r-to-s)j  nach   Szemer^nyi  Gl.  88  : 265  zu  *er-,  oben  S.  327  f. ;  air.  -som  .ipseS  air.  sund   ,hierS   cymr.   hunui' .dieser'  (aus  idg.  *so7ndhe,  welches  zu  sondo-  umgebildet  wurde);  got.  i^;^ sama  .derselbe*,  aisl.  samr^  inn  sami  .derselbe^  samt  Adv.  ,ununterbrochenV ahd.  der  samo  .derselbe',  vgl.  auch  Zs.  wie  got.  sama-kuns,  anord.  samkynU ,von  gleichem   Geschlecht^   gr.   Ofiöynog  ds.,   ai.   sama-jätiya  , gleichartig*,^ anord.   samfedra,  öf.i07i(XTüjQ,   ap.    hamapitar-   .von    demselben  Vater',  aiijj* sammedri,  ofiOfirjTQLog  .von  derselben  Mutter*;
ein  i-Fem.  *somi,  *sml  , Beisammensein,  Vereinigung,  z.  T.  auch  kämp*« fendes   Aneinandergeraten'   in  ai.   sami-kd-  n.   , Kampf,  Schlacht^;  aber  gr. 6'«i-Aog  , Haufe.  Versammlung,  Schlachtgedränge',  bf-älla  ,Umgang,  Verkehr*^ ö^lXso)   .verkehre'   bleiben  wegen   äol.  l)fxiXXog  fern,  ebenso  lat.  miles,  vj Szemerenyi   Arch.    Ling.    6.   41 ;    gr.    Sc^dXa    .Streit,    Kampf,  Wettstreit (*Sem-il-ia)y  ä{.iLXXaadai  .wettkämpfen';
dazu  mit  dem  Begriffe  des  friedlichen  Beisammenseins,  auch  des  Zrf sammenstimmens  aisl.  sama  , passen,  sich  schicken' ;  got.  samjan  .gefallen^ zu  gefallen  suchen',  aisl.  semja  (=  ai.  samayati)  , zusammenstellen,  vereini gen, 
===== LEAF 142
 einig  werden  um,  ordnen,  zustandebringen';  dazu  wohl  germ.  *sampu in  ahd.  semfti  (Adv.  samfto)  ,hequem,  gemächlich,  freundlich',  nhd.  «an/<, as.  safto  Adv.  .leicht',  mnd.  sachte  Adj.  Adv.  , sanft,  mild',  ags.  s^fU (Adv.  softe)  , ruhig,  mild',  vgl.  dazu  bes.  ai.  säntva-  n.  .gute  beschwichti- gende Worte',  säman-  m.   n.  .ds..  Milde,  freundliches  Entgegenkommen*;
germ.  *sampia-  ist  viell.  aus  einem  ^w-St.  *sampu-  umgebildet,  der  mit ai.  säntva-  auf  idg.  *söm-tu-  zurückgehen  kann ;
dagegen  ist  ags.  smede,  smöd^  as.  smödl  ,glatt.  eben,  sanft,  milde'  wegen westfäl.  smgid  aus  *sman]ji  entstanden;  got.  samap  , zusammen',  as.  samad, ags.  samodj  ahd.  samit  (samant  mit  n  nach  saman-),  nhd.  samt;  eine c?- Ableitung  in  ai.  samad-  f.  , Streit,  Kampf,  gr.  d^adog  , Gewühl,  Menschen- menge* ;
dehnstufig  ai.  säman-,  samand- , ruhig',  säma-gir- , freundliche  Worte  redend', säntva-  (s.  o.),  av.  häma-   ,gleich,   derselbe',   np.   hämün  , Ebene',  air.  »aw» - ,Ruhe'   (aus   ,*trauliches    Beisammensein'),   säim   ,ruhig,   mild',   aisl.   söma (*sömen)  ,passen,   geziemen*,   sömi  m.   ,Ehre,  Auszeichnung',   semr  .gezie-
905
lueiid,  passend^  as.  sömi  ds.;  ags.  söm  f.  , Einigkeit,  Versammlung',  ge-söm einmütig,  freundlich^,  mhd.  suome  , angenehm,  lieblich^;  abgel.  aisl.  sema gich  finden  in,  Rücksicht  nehmen  auf,  ehren^,  ags.  seman  , versöhnen' 5 eflo-l.  seem  , ziemen,  scheinen'  ist  nord.  Lw.;
aksl.  saim  ,ipse,  solus,  unus';
mit  i2-Formans:  ai.  säman-,  sämana-  s.  oben;  mit  ö-Stufe  wohl  ai.  sa- mana-  n.  , Zusammenkunft,  Festversammlung',  samanä  Adv.  ,zusammen, crleichzeitig,  ebenmäßig';  got.  samana  ,beisammen',  aisl.  saman  ,zusammen^, ahd.  samaUj  zi  samane,  nhd.  zusammen]  davon  abgeleitet  aisl.  samna,  ahd. savianön,  mhd.  samenen  , sammeln',  dissim.  samelen,  nhd.  sammeln-^  mit Red. -St.  ir.  samain  ,das  Fest  des  1.  Nov.'  (eigentlich  , Zusammenkunft'), hech-samain  ,Bienenschwarm' ;
eine  Dehnstufe  *sem  vielleicht  in  gall.  ao-aiv  , dieses^  und  im  n.  des  air. Artikels  {s)a'\  vortonig  aus  *sin,  dieses  aus  *sem  über  ^^sln]  die  übrigen Formen  sind  durch  Übertragung  der  Endflexion  auf  eine  Adv.-Form  *sinde (aus  ^sem-dhe;  es  läßt  sich  nach  ai.  sa-dha  idg.  *<iÄe,  oder  nach  ir.  suide  aus idg.  *so-de  (^o-Flexion)  =  gr.  8-6e  auch  idg.  *cZe  ansetzen)  entstanden; Demonstr.  ir.  sin,  cymr.  hynn  gehen  auf  den  Stamm  *sindo-  zurück  und stellen  die  enklitische  Form  dar.
WP.  II  488 ff.,  WH.  II  511  f.,  513,  533 ff.,  Trautmann  249 f.;  J.  Gonda Reflections  on  the 
===== LEAF 143
 Numerais.
5.  sem-  , Sommer'  (Gen.  Sein-ös)]  mit  Erweiterung  zum  ä-St.  Semä]  r-St. *Scn2er-. Ai.  sdmä  f.  , Halbjahr,  Jahreszeit,  Jahr*  (=  arm.  am),  äi-sd-mah  ,heuer' (wohl  aus  einem  Lok.  *äi-samäi  umgebildet,  s.  oben  S.  286) ;  av.  ham- ,Sommer';  arm.  am  ,Jahr^  (=  ai.  sdma)^  amafn  , Sommer'  (^Stm^rom)]  air. sam  i^semo-)  und  samrad  {^s^mo-röto-,  oben  S.  866),  cymr.  corn.  haf,  bret. haüv  , Sommer*;  cymr.  hafod  , Sommerhaus^,  bret.  havreg  , Brachfeld',  mir. samad  m.  , Ampfer';  gall.  samon\ios]  , Sommermonat*,  samolus  , Sauerklee', Samara  , Ulmensamen';  fern  bleibt  der  ibero-rom.  Fischname  samauca (Hubschmid  Rom.  Phil.  8,  12  f.);  ahd.  sumar^  ags.  sumor  m.,  aisl.  sumar n.  ,Sommer^;  als  , einjährige  Tiere'  aisl.  simull  ,(einjähriger)  Ochs',  simi, simir  ds.,  norw.  simla  , Renntierkuh'  (idg.  sem-).  schwed.  somel  ,Renntier- kalb'.
WP.  II  492  f.
semi-  ,halb'  als  1.  Kompositionsglied.
Ai.  sämi-  ,halb'  (d-sämi-  Adj.  ,nicht  halb,  vollständig');  gr.  ijjta-  ,halb' (fjfiiGvg    jhalb'   aus   ursprüngl.   f](J.iTvg  m.  ,*Hälfte',  vgl.   kret.   ii^itv-tyLtov,
906
epid.  'fjuirsLtt',  fiidva  ,HälfteO;  lat.  semi-  {semus  späte  Adjektivierung);  ,g^ indekl.'  ,halb,  Hälfte^  wohl  nach  6is;  ahd.   sämi-,   as.   säm--^  vgl.  lat.  ^gnit vivus,  gr.   'fj^d-ßiog,  ahd.  sämi-quecJc,  as.  säm-quick  ,halbtot^ WP.  II  493,  WH.  II  512  f.
sen-,   sene-,   sen{e)u-,   send-   ,hereiteii;   ausarbeiten,  vollenden,  erzielen'^
Ai.  dsanam  ,ich  gewann',  sanima  ,wir  mögen  gewinnen';  saiiöti  ;gewiiin|t' sanukd-  ,beutegierig',  sanitär-  ,Gewinner,  Sieger',  Partiz.  sätd-  ;gewoiinen<* säti-  f.  ,Gewinnung,  Erwerb';  gr.  *ävvfa,  themat.  dvvo),  att.  äpvco  und  hont      ^ ävü)    {*ävJ^(x})   ,vollende';    gr.    ävvrto    ds. ;    davsg-    od    T€Xsad^7]a6f.ievov    He^ iv    ävdTOig'    iv    änoqlaLg    Hes.    {äv-arog    ,unvollendet') ;    hom.    ivveci-BQYQ^ Jgya   dvvajv^',    svagcc    ,die   Rüstung   des   erschlagenen    Gegners'   (*,Kanip. fesbeute');   davon   ivalgco,    Aor.    'ijvaQOv   ,im   Kampfe   toten',   svagllu)  ,dem getöteten  Feinde  die  Rüstung  ausziehen;  im  Kampfe  töten';  lak.  ivagaa^^ Qog  „rä  evaga  cpsgcov"]   evrsa  (Sg.   evrog)  ,Rüstung';   woneben   *ivuig  ,Zu».,. rüstung,  Vollendung'  vorausgesetzt  von  irzva),  iviivco  , mache  fertig,  rüstf^^ zu,  bereite';  neben  tö   evrog  steht  ovv-ivrrig'   avvegyög  Hes.   und  aid^hrn^-^ ,*mit  eigener  Hand  vollbringend:  Mörder;  Herr*;
air.  con-sul  ,sucht  zu  erwerben,  macht  streitig',  cymr.  cynyddu  ,erobemS zu  gewinnen  suchen'  usw. ;
hitt.  §anh-  ,suchen,  erstreben,  fordern';  auch  , fegen'  (,*durchsuchen*).
WP.  II  493,  Pedersen  Hitt.  185.
sendhro-,  -ä  , geronnene,  sich  verdichtende  Flüssigkeit':  nur  germ.  und  slav» Aisl.  sindr  n.  , Metallschlacke'  und  , Hammerschlag'  (dazu  sindra 
===== LEAF 144
rwandt  ist  norw.  dial.i sinkla  ,sich  mit  einer  Eiskruste  beziehen'  als  *si7id-kla-  serb.-ksl.  8ediy\ krhvhnyje,  russ.-ksl.  sjadry  krovnyja  ,geronnene  Blutmassen',  skr.  sl^dra^ , Kalksinter',  cech.  sddra  ,Gips'  (aus  '*sendhrä). WP.  II  497,  Trautmann  256.
seng^-  ,  fallen,  sinken'.
Arm.  ankanim  , falle,  weiche,  nehme  ab';  gr.  sdcp^vj  ,sank'  {dOTiig)]
germ.  *sinkwan  in:  got.  sigqan^  aisl.  sekkva^  ags.  sincan,  as.  ahd.  sinkan^'^
sinken,  Intens,  dän.-norw.  sakka,   ndl.   zakken^   nhd.   sacken  , sinken';   Adj/j:-!^
*sinhti-  in  ags.  sihte  , sumpfig',  mhd.  slht{e),  nhd.   seicht,  alem.  sieht  ,sebr;^''"'^
feucht'  (von  Wiesen).
WP.  II  495  f.
seng^h-   »singen,   mit   singender   Stimme    vortragen';   song^bo-s   , Gesang'»
907
präkr.  samghai  , sagen,  belehren*;  gT.  öf-irfr}  , Stimme,  Prophezeiung* /*sojig^(ihä),  Tcavoucpalog  , Beiname  des  Zeus';  mcymr.   de(h)ongl  , erklären';
o-ot.  siggwan  ^singen,  vorlesen,  rezitieren',  aisl.  syngua,  ags.  ahd.  as. gingan,  singen-^  got.  saggws  , Gesangs  Musik,  Vorlesung',  aisl.  sgngr  , (kirch- licher) Gesang^,  ags.  sang,  song,  ahd.  as.  sang,  Sang  , Gesang,  Lied'.
WP.  n  496,  Bloch  BSL  31,  62,  Vendryes  RC  48,  476;  nach  W.  Wüst (brieil.)  gehört  präkr.  samghai  zu  kens-,  oben  S.  566.
seni-f  senu-,  (seni-),  sn-ter-  ,für  sich,  abgesondert^
Ai.  sanu-tdr  ,abseits  von,  weit  weg^  sdnutara-(?),  sdnutya-  ,verstohlen, unvermerkt'  (*,beiseite'),  av.  hanard  , abseits,  ohne^;  gr.  Ureo  (ion.)  , abseits, ohne'  {^snter)]
as.  sundir  ,ohne'  (=  Uisq),  ahd-.  suntar  »abgesondert'  und  ,aber,  dagegen', nhd.  sondern  (diese  Bed.  aus  jaußer,  ohne'),  ags.  sundor  ,für  sich,  beson- ders', anord.  sicndr  , entzwei',  got.  sundrö  ,für  sich,  abseits,  besonders^, Adj.  mhd.  sundei',  besunder,  nhd.  besonder]
lat.  sine  ,ohne'  (wohl  neutr.  "^seni,  nächststehend  dem  ir.  sain  aus  *5e7w*-);
air.  sain  Adj.  »verschieden,  besonders^  (*V^i-s),  cymr.  o-han-y  a-han-  ,von', gwa-han  , getrennt,  verschieden',  acymr.  han  ,alium' ;  cymr.  hanes  , Er- zählung' =  mir.  Sanas  , Geheimnis,  Lispeln'  (*sani-sta) :  corn.  hanys  ,heim- lich';  toch.  A  sne^  B  snai  {*sanai)  ,ohne*;
Die  Bedeutung  ,abgesondert,  für  sich'  läßt  Verbindung  mit  dem  Reflexiv- stamm *se-,  *s(e)iie-  zu,  vgl.  mit  Anlaut  su-:  aksl.  svSnS  ,außer,  ohne'  und lat.  sed,  se  Präp.  ,sine,  ohne*,  Präf.  ,ohne,  beiseite'.
WP.  II  494f.,  WH.  II  542f.,  H.  Lewis  EC.  1,  322.
senk-  , brennen,  dörren';  nur  germ.  und  slav.
Ags.  sengan,  mnd.  mhd.  sengen  , sengen'  {*sangjan  , brennen  machen'); nd.  sangeren  ,in  der  Haut  prickeln'  (eig.  ,brennen'),  älter  ndl.  sengel  , Funke', mhd.  senge  ,Troc
===== LEAF 145
kenheit,  Dürre',  sine  {-g-)  ,das  Sengen',  sungen,  sunken , anbrennen',  sungeln,  sunkeln  ,knistern',  norw.  dial.  sengra,  sengla  ,brenzlich riechen',  schwed.  dial.  sjängla  ,sengen',  isl.  säng{u)r,  n.  sangt  ,versengt, angebrannt' ;
aksl.  pre-socitl,  isqciti  ,trocknen',  sgcilo  ,Ofen',   russ.   izsjaklyj  , trocken'.
WP.  II  495.
serz(o)-  ,alt';  seno-mäter  , Großmutter'.
Ai.  sdna-^  av.  hana-  ,alt',  ai.  sanakd-  , ehemal  ig,  alt'  (:  lat.  senex,  fränk. Sinigus^  gall.  Seneca),  sanah  ,vor  alters',  sdnä^  sanät,  sandtä  ,von  alters her,  von  jeher,  stets',  sanätdna-  ,ewig,  unvergänglich,  beständig';  arm. hanajpaz  , immer',  hin  ,alt';  gr.  svog  ,alt,  vom  Aderigen  Jahre',  di-evog  ,zwei-
908  •
jährig^  evT;.yMl  via  ,der  Tag  vor  dem  Neumond  und  der  erste  des  beginnen, den  Monats';  lat.  sßnex,  Gen.  senls,  Kompar.  senior  ,alt,  bejahrt';  seneö,  -gre, ,alt,  schwach  sein',  smlscö,  -ere  ,altern,  hinschwinden',  Senium  \Alters. schwäche,  zehrende  GemütsstimmungS  senätus,  -üs  (osk.  Gen.  senattU) , Senat',  senectüs  , Alter',  seneciö  ds. ;  air.  sen  ,^\i',  acjmr.  corn.  bret.  ^en ,senex',  Komp.  air.  siniu,  cymr.  %n;  ir.  sen-mäth{a)ir  (==  lit.  sen-mrfeg) , Großmutter';  gall.  Seno-gnätus  u.  dgl,  Äerieca;  got.  sineigs  „^Qsaßvrr^gU^ sinista  ,ältester',  afränk.  sini-skalkus  ,der  älteste  Hausdiener',  aisl.  sina ,vorjähriges  Gras';  lit.  senas  ,alt',  senis  ,Greis',  seniaX  ,vor  alters,  längst', seneju  , werde  alt'  (=  lat.  seneö).
WP.  II  494,  WH.  II  513  f.,  Trautmann  256.
sent-  ,eine  Richtung  nehmen,  gehen'  {sento-  , Gehen,  Reisen;  Weg')  und im  geistigen  Sinne  ,empfinden,  wahrnehmen'.
A.  im  geistigen  Sinne:  lat.  sentiö,  -Ire,  -si,  -sum  ,fühlen,  empfinden,  wahr« nehmen',  sensus,  -üs  , Gefühl,  Sinn,  Gesinnung,  Meinung',  sententia  (*sen- tientia)  , Meinung  usw.';  ahd.  sin,  -nnes  ,Sinn'  (*sent-no-),  sinnan  ,trachten, begehren',  nhd.  sinnen]  lit.  sinteti  , denken';  aksl.  sesth  ,klug'.
B.  im  eigentlichen  Sinne :  av.  haut-  (Präs.  hl-sasat,  Fut.  ni-sqsya)  ,gelan- gen,  gelangen  lassen';  arm.  dntac  ,Weg,  Gang',  dntanam  ,gehe,  reise,  eile';
air.  set  ,Weg',  cymr.  hynt  ds.,  mbret.  nbret.  hent  ds.  (=  germ.  *sin'pa-)y abret.  Gl.  do-guo-hintiliat  ,inceduus',  acorn.  cam-hinsic  Gl.  ,iniustus*  {cam- , krumm'),  eun-hinsic  Gl.  ,justus'  (eun-  , gerecht');  davon  air.  setig  ,Frau' (, Weggenossin',  l-Fem.  eines  Adj,  *setach)',  cymr.  carrynt  (zu  cai^r  ,Wagea') ,Weg,  Reise',  epynt  (zu  eb-,  *ekuo-)  ,Pferde-Weg',  dyffrynt  ,Tal'  (zu  dtofr ,Wasser');  aus  *sentio-:  mcymr.  hennydd  , Gefährte',  bret.  hantez  , Nachbar', ; corn.   hynsa  ds. ;
got.  sinps  m.  ,Mal',  aisl.  sinn  n.  ,Mal',  sinni  n.  ,Gang,  Reise'  (und  als Nachkomme  eines  *gasinpja-
```


## [2026-09-14T01:57:09.967Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"sem-1\\.\" AHD_watkins1985.txt | head; echo \"---\"; grep -n \"SIMPLE\\b\" AHD_watkins1985.txt | head -3; echo \"--- search body\"; grep -n \"sem-1\" AHD_watkins1985.txt | head -20",
 "description": "Find AHD sem-1 body entry"
}
```


### [2026-09-14T01:57:10.058Z] TOOL RESULT

```
---
916:tive verb *salbén in Middle Dutch salven, to anoint, salve, in obsolete Dutch guacksalver, a quack: QUACK- SALVER. [Pok. selp- 901.] sem-'. One; also adverbially “as one,” together with. I, Full-grade form *sem-. 1. Greek *hem- in: a. Greek heis (< nominative singular masculine *hen-s < *hem-s), one: HENDECASYLLABIC, HENDIADYS, HENOTHEISM; b. Greek he- in hekaton, one hundred (? dissimilated from *hem-katon; see dekm). 2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEM- BLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- (*per, during, for; see per’) in Latin semper, always, ever (< “once for all”): SEMPRE; SEMPITERNAL. II. O-grade form *som-. 1. Sanskrit sam, together: SAMSARA, SAN- DHI, SANSKRIT. 2. Suffixed form *som-o- in: a. Germanic *samaz, same, in Old Norse samr, same: SAME; b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; Cc. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level: HOMOLOGRAPHIC, HO- MOLOSINE PROJECTION. III. Lengthened o-grade form *s6m-. 1. Suffixed form *sém-i- in Germanic *sdmiz in Old Norse scemr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY. 2. Suffixed lengthened o-grade form *sém-o- in Russian sam, samo-, self: SAMIZ- DAT, SAMOVAR. IV. Zero-grade form *sm-. 1. Greek ha-, a-, together, in compound a-kolouthos, accompanying (a- + keleuthos, way, path): ANACOLUTHON. 2. Greek com- pound haplous, simple (-plous, -ploos, -fold; see pel-3): HAPLOID. 3. Suffixed form “smm-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -soME!. 4. Suffixed form *syym-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMI- LATE, RESEMBLE. 5. Compound *sm-kéro-, of one grow- ing (see ker-3). 6. Suffixed form *sm-tero- in Greek heteros (earlier hateros), one of two, other: HETERO-. 7. Compound *srn-plek-, “one-fold,” simple (*plek-, -fold; see plek-), in Latin simplex, simple: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound sym-plo-, “one-fold,” simple (*-plo-, -fold; see pel-3), in Latin simplus, simple: SIMPLE. 9. Extended form *syma in Greek hama, together with, at the same time: HAMADRYAD. 10. Basic form sm- in Old Russian si-, together, in compound siivéti (> Rus- sian sovet), assembly (véti, council; see weite-): SOVIET. [Pok. 2. sem- 902.] sem-2, Also sema-. Summer. Suffixed zero-grade form *sma-aro- in Germanic *sumaraz in Old English sumor, summer: SUMMERI. [Pok. 3. sem- 905.] sémi-. Half. 1. Germanic *sémi- in Old English sdm-, half: SAND-BLIND. 2. Latin sémi-, half: sEmI-. 3. Latin sémis, half: SESQUI-, SESTERCE. 4. Greek hémi-, half: HEMI-. [Pok. sémi- 905.] sen-', Old. 1. Latin senex, old, an elder: SEIGNIOR, SEN- ATE, SENECTITUDE, SENESCENT, SENILE, SENIOR, SENO- PIA, (SIGNORY), (SIR), SIRE, (SURLY). 2. Suffixed form *sen-o- in Germanic *senaz in compound “*sini-skalkaz, old servant (Germanic *skalkaz, servant, slave; see skalkaz), in Medieval Latin siniscalcus, seneschal: SEN- ESCHAL. [Pok. sen(o)- 907.] sen-2. Also seni-. Apart, separated. 1. Suffixed zero-grade form *sn-ter- in: a. Germanic *sundré in Old English sundor, sunder, apart: ASUNDER; b. Germanic denominative *sundrén in Old English syndrian, sun- drian, to put apart: SUNDER; Cc. Germanic derivative adjective *sundriga- in Old English syndrig, apart, separated: SUNDRY. 2. Zero-grade form *snni- in Latin sine, without (< “outside,” “out of’): SANS; SINECURE. [Pok. seni- 907.] sendhro-. Crystalline deposit. Germanic *sendra-, slag, in: a. Old English sinder, iron slag, dross: CINDER; b. Old High: German sintar (> German Sinter), slag: SINTER. [Pok. sendhro- 906.] sengw-. To sink. Germanic *sinkwan in: a. Old English sincan, to sink: SINK; b. Scandinavian intensive form
2259:SILT sal-1 SILURID ors- SILVICOLOUS kWel-1 SIMILAR sem-1 SIMPLE sem-1 SIMPLEX sem-! SIMPLICITY sem-1 SIMULTANEOUS sem-1 SIN] es-
--- search body
1263:ASH? os- ASININE asinus ASK ais- ASPECT spek- ASPEN apsa ASPERSE (s)preg- ASPIRATE spirare Ass? ors- ASSAI? Sa- ASSAIL  sel-4 ASSAY ag- ASSEMBLE sem-! ASSENT sent- ASSERT ser-3 ASSESS sed-1 ASSET sa- ASSEVERATE weéro- assIDUOUS_ sed-1 ASSIGN sekw-1 ASSIMILATE sem-1 ASSIST sta- ASSOCIATE sekw-1 ASSOIL feu-1 ASSONANCE swen- ASSORT ser-3 ASSUAGE swad- ASSUASIVE swad- ASSUME em- ASSURE cira ASTASIA sta- ASTATINE  sta- ASTER  ster-3
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1597:HENCE ko- HENDECASYLLABIC sem-1 HENDIADYS dwo-, sem-1 HENOTHEISM sem-1 HEPARIN yekwr HEPATIC yekwr HEPATITIS yek"r HEPATO- yekwr _ HEPATOGENIC yekr HEPTA- septm HEPTAD septm HeEpPTaTEuCH dheugh- HER ko-
1639:HOMEO- sem-! HOMICIDE dhghem- HOMILY sem-1 HOMINID dhghem- HOMO! dhghem- HOMO- sem-1 HOMOIOUSIAN eS- HOMOLOGOUS leg-1 HOMOLOGRAPHIC sem-1 HOMOLOSINE PROJECTION HOMONYMOUS nO-men- HOMUNCULUS dhghem- HONE! k6-
1654:sem-1
2209:SAL sal-1 SALACIOUS  sel-4 SALAD sSal-1 SALAMI sal-1 SALARY Sal-1 SALE sel-3 SALI-  sal-1 SALICIN sal(i)k- SALIENT sel-4 SALINE sal-1 SALLOW! | sal-2 SALLOW? | sal(i)k- SALLY sel-4 SALMON sel-4 SALON sel-1 SALOON sel-1 SALSA Sal-1 SALT sal-1 SALTCELLAR sal-1 SALTPETER petra, sal-1 SALUBRIOUS sol- SALUTARY sol- SALUTE sol- SALVAGE sol- SALVE! selp- SALVO! sol- SAME sem-! SAMITE mei-4 SAMIZDAT d6-, sem-1
2211:SAMOVAR sem-1, wer-7 SAMPLE em- SAMSARA sem-1, ser-2 SANCTIFY sak- SANCTUM sak- SAND bhes-1 SAND-BLIND sémi- SANDHI dhé-1, sem-1 SANE sano- SANHEDRIN  sed-1 SANITARY sano- SANS sen-2 SANSKRIT k¥er-1, sem-1 SAP! sab-
2241:SEMEME dheie- SEMEN sé-1 SEMESTER mé-2, s(w)yeks SEMI- sémi- SEMINARY sé-1 SEMINATION sé@-1 SEMIOLOGY dheie- SEMIOTIC dheie- SEMPITERNAL aiw-, sem-1 SEMPLICE sem-1 SEMPRE sem-1
2259:SILT sal-1 SILURID ors- SILVICOLOUS kWel-1 SIMILAR sem-1 SIMPLE sem-1 SIMPLEX sem-! SIMPLICITY sem-1 SIMULTANEOUS sem-1 SIN] es-
2261:SING sengh- SINGE senk- SINGLE sem-1 SINGSPIEL sengWh- SINISTRORSE wer-3 SINK seng¥- SINN FEIN s(w)e- SINTER sendhro- SIP seue-2
2276:SoL sdwel- SOLACE sel-2 SOLANINE sAwel- SOLAR sawel- SOLARIUM sawel- SOLE! sel-1 SOLE? s(w)e- SOLEMN sol- SOLICITOUS_ kei-3, sol- SOLID sol- SOLILOQUY s(wW)es, tolkw- SOLIPSISM s(w)e- SOLITARY s(w)e- SOLITUDE s(w)e- SOLO s(w)e- SOLSTICE sawel- SOLUBLE leu-1 SOLUM sel-1 SOLUTE leu-1 SOLVE leu-! SOMA teue- SOMATO- teua- SOME sem-! -SOME! sem-1 -SOME2  teue- SOMERSAULT sel-4, uper SOMNI swep-! SOMNOLENT swep-! SON seue-! SONANT swen- SONATA swen- SONE swen- SONG sengWh- SONIC swen- SONNET swen- SONOROUS swen- sooT sed-1 SOOTH es- SOOTHE es-
```


## [2026-09-14T01:57:11.578Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\n# printed p.211 -> leaf 211+15=226\nfor i in (225,226,227):\n    print('==== leaf',i); print(t[i][:2500])\nEOF",
 "description": "Kent lexicon pages 211-212"
}
```


### [2026-09-14T01:57:12.864Z] TOOL RESULT

```
232
==== leaf 225
BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f.
brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223-9), with braz- rather than barz- (883; cf. Elam. pir-ra-us-man-ni-ia, АКК. bi-ra- 2a-man-ni-1): deriv. (§144.IV) to pAr. antecedent of Skt. bráhman- ‘religious devotion, prayer’, ef. identical Skt. deriv. brahmanyd- ‘religious’, to pIE root *bhergh- (see OP bard-; $75.1II, §95, $120, 5155.11; Henning, TPS 1944.108-18). For other views, see Kent, Lg. 13.301; Hartmann, OLZ 40.145-60; Nyberg, Rel. 367, 478; Hz. AMI 8.69, Apl 116-8 (to Av. barag- ‘to welcome’, barag- ‘rite’, Бәтәгба- ‘beloved’; wrongly, since this would give OP *bragman-); Christensen, Essai sur la démonologie iranienne 40-1; Henning, BSOS 10.506; Abayev, Iranskie Yazyki 1.134; Scherman, JAOS 65.141-3 n.23. Cf. also О. M. Dalton, Treasure of the Oxus 94-5. On form and meaning of РЫ. brahm brahmak, see Henning, TPS 1944. 108-18. brazmaniya nsm. ХР 41, 51, 54 (hardly brazmaniy isn. modifying arid; also not -niy apn. ‘divine’ with Sen 155, nor adn. in elliptic dual with Pisani, see under aria-).
т°, of dubious meaning, Se 1; taken by Justi, IFA 17.112, to be an abbreviation for OP *méraka ‘seal’, NPers. maráh.
та-, stem of ist person pron. in obl. cases of sg.; see adam.
mà conj. ‘not’, in prohibitions ete.: Av. Skt. mà, Gk. шӯ, pIE *mé ($109, §191.1, §292b). With subj.: DNb 55 (mé-taty), 58. With opt.: DB 4.59, 69, 79°; DPd 18, 19 bis, 20; XPh 39. With
201
inj.: DB 4.54; DPe 21; DNa 58, 59, 60; DNb 52 (mà-lay). With imv.: DNb 60. With lost verbs: DNb 57, DSq 4 bis; with restored subj. A'Sa 5^ bis, A?Ha 7, 7°. See also mdtya.
mā- vb. ‘measure’: Av. Skt. ma-, Lt. métior ‘I measure’. à + må- ‘extend’: атӣій npm. past ptc. pass. (6242. П) ‘noble’ DB 1.7; DBa 11. fra- + mā- ‘command’ (‘decide, judge’, acc. to Hz. ApI 154-6; ‘plan,’ Hinz, ZDMG 95.233-5); see also framülar-, framdnd-. јтатауаіа imf. mid. ($214, 5285.11) XPg 5. framatam nsn. past pte. pass. ($242.IT) DSf 19f°, 56.
таш- vb. ‘flee’: meaning established by Мат. and АКК. versions (Hüsing, KZ 38.258); probably to Skt. munthate ‘flees’ (Jn. JAOS 38.122). атида imf. ($211) DB 2.2, 71; 3.41f, 71.
Maka- sb. ‘Maka’, a province of the Persian Empire (lit
==== leaf 226
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado.
(1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm. DSf 50, 54. Майа] ipm. DB 2.23. MddatSuva lpm. DB 2.23.
(2) ‘Media’: Мада пзш. DB 1.15°, 41; 2.7; DPe 10; DNa 22; DSe 21°; Рб 8°; XPh 19. Madam asm. DB 1.47; 2.22, 28f, 48f, 68, 65 bis; 3.32f; 4.20. Méddam-ca DB 1.66f. Madaiy lsm. DB 1.84, 59; 2.15, 17, 22, 28, 66 bis, 72, 92; 3.77; DBe 10f.
tman- vb. ‘think’: Av. man-yele, Skt. mán- yale, Gk. utuova ‘(I bave thought of,) I desire’, Lat. memini ‘I remember’, pIE *men-. See also manah-. maniyary lst sg. mid. (§214, 5238.1) DNb 38. amaniyazy lst sg. imf. mid. (8214, 6233.11) DSI 3f. mantydhaiy 2d sg. subj. mid. (831, $222.11, §234.1) DB 4.39 (manl. . .); DPe 20 (maniydhay, $27, 552.11); DNa 38 (maniya- [...); XPh 47 (maniyaty, without the h*: $27, $52.VI, Lg. 13.302; Hz. AMI 8.66, ApI 243-4). maniyál|taty) sub). mid. (5222.1) DB 4.50.
^man- vb. ‘remain’: Av. man-, iterative pres. manaya- (8123, $215), Gk. pvo, Lt. maneo; prob- ably specialization of pIE *men- ‘think’ (see ‘man-) in meaning ‘remain thinking. amdnaya imf. DB 2.48, 63; amünaiya ($48) DB 2.28.
mana'uwin- adj. ‘mindful, wilful, hot-tem- pered’: from manah- + -win- (§155.V), cf. Lg. 15.170, JNES 4.47 (Hz. ApI 242 otherwise, wrongly). manauvis (remade from -07, $187) пэш. DNb 13.
manah- sb. ‘thinking power, power of will’ (Jn. Iran. Rel. $70; Kent, JNES 445-7, 232): Av. manah-, Skt. mánas-, Gk. дё ‘courage’, pIE *menos *menes- (5124.4, 4156.1). Decl., $185.I. See also manawin-, and -manis- with reduced grade in second syllable, in Ardumuni&, Harā- manik, perhaps [manis-. тапа&-са (8105) asn.
DNb32. manahà isn. (JNES 4.45; wrongly gen., Hz. ApI 240-2 and Sen 235) DNb 14.
méaniya- sb., probably ‘personal property’ in the houses; nt. adj. as collective sb., from тӣпа-, GAv. demüna-, Ау. nmana- ‘abode, house’ ($126), extension of root seen in Skt. dáma- ‘house’, Gk. 0óuos, Lt. domus. For varying views, see Tm. Lex. 116, with lit.; Gray, JAOS 21.17, 33.281-3; Bthl. AiW 1168; MB Gr. §261; Fay, JAOS 34.330-1. méaniyam-cé asn. DB 1.65.
+mamaita, see Atamatta-.
тауйта- sb. ‘doorknob’: Skt. maytikha- ‘peg’, perhaps to Skt. mi- (pres. minétz) ‘fix (as in the earth) 
==== leaf 227
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
EU: ET TORR ON |
INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne -
LEXICON 203
‘martiya- adj. as sb. ‘man’: -ize- extension of pIE *morios, Av. marata- ‘mortal, man’, NPers. márd, Skt. mária- (§31, $106, $122, 5242.11), ef. ~o- extension in Av. masya-, Skt. mártya- ($144.IV). See also wmartiya-, *Martiya-.
martiya nsm. DB 1.21, 36, 48, 74, 77; 2.8, 14, 79; 3.12, 22, 70, 78; 4.38, 65, 68; 5.5°, 7°; DNa 46; ОМ 16, 19, 21, 24; XPh 51. martiyà узш. "Ма 56. martiyam asm. DB 3.57; DNa 3; DNb 12, 22; DSe 3; DSf 2, 16f; DSs 2; DSt 3°; рле 2; DE 4f; XPa 2; XPb 4f; XPe 21; XPd 3f; XPf 3; XPh 3; XE 5; XV 4; A'Pa 3P; А°Не 3f; A?Pa 3f. martiyahyé gsm. DNa 4, 44; ОМ 3; DSe 4f; DSf
. 8; D8s 5^; DSt 4^; DZe 2f; DE 6; XPa 3; ХРЬ 6;
ХРе 3; XPd 4f; ХРі 4f; XPh 4; XE 7; XV 5; AlPa 5°; A?He 4f; martthya A3Pa 4f (852.VI; hardly phonetie, as taken by Morgenstierne, Ácta Or. 1.253). martiyá npm. DB 1.571; 4.80, 82; DSf 47, 49, 51, 52, 54. татітуй apm. DB 2.77; 3.48, 50, 74, 90, 91. татйуйтат gpm. DB 4.87. martiyaibiš ipm. DB 1.56f.
? Martiya- sb. ‘Martiya’, a Susian rebel: Elam. mar-tiia, АКК. mar-t-ta; same аз 'martiya-, specialized as man’s name (§168.Ib, $164.III; but ef. HK Iran. Eigenn. 13-4, Phil. 66.183-4, ApKI 1.54, 2.26). Martia nsm. DB 2.8; 4.15; DBf 1. Martiyam asm. DB 2.12f.
mard- vb. ‘crush’: Av. marad- ‘destroy’, Skt. mrd- ‘rub, crush’, Lt. mordet ‘bites’, pIE *merd- (Foy, KZ 35.48). See also Marduniya-.
vi- + mard- ‘destroy’: vimardatiy (830, $213) DSe 40f. wyamarda imf. (written viya : marda, $44; cf. also $52.IV, $228.II, and Lex. s.v. -di-) DB 5.11.
Marduniya- sb. 'Mardonius, father of Gobryas: Elam. mar-du-nu-ia, Gk. Марббио; per- haps deriv. to *marduna- ‘vintner’ (§144.IV, 8147. П, $153.1, $164.1V), ef. NPers mul ‘wine’, Skt. mydvikd- ‘grapevine’ (Bthl. AW 1151; otherwise Justi, INB 195), which possibly contains root mard- ‘crush (the grapes in the wine-making)’. Marduniyahya gsm. DB 4.84.
mav- vb. ‘send’: ef. Lt. moved Ч move’. [0т]- арай imf. mid. as pass. ($213, $235.II) DB 4.92 (dubious conj. of Kent, JAOS 62.269).
Mazdàh- adj. ‘wise’ (5156.1, $160.Ia): regu- larly compounded in Auramazdah- (q.v.); both
parts declined, but without an intervening word- divider, in Aurahya Mazdaha (8$185.IV) ХРе 10.
maskd- sb. ‘(inflated) skin’; NPers. mask, АКК. mas-ku-u ‘skin’, Aram. ma
```


## [2026-09-14T01:57:18.979Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (234,235,236,237):\n    print('==== leaf',i); print(t[i][:3500]); print()\nEOF",
 "description": "Kent leaves 234-237"
}
```


### [2026-09-14T01:57:20.235Z] TOOL RESULT

```
Exit code 1
==== leaf 234
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: list index out of range
```


## [2026-09-14T01:57:26.442Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r\"hadā|hadä|hadis|hakaram|hamaranam|ham-|'with'\", p):\n        for m in re.finditer(r\"hadā|hakaram|hamaranam|hamdtar|hama-\", p):\n            print(i, p[max(0,m.start()-120):m.start()+200].replace('\\n',' '))\n        print('---')\nEOF",
 "description": "Grep Kent for OP ha-/hadā"
}
```


### [2026-09-14T01:57:27.654Z] TOOL RESULT

```
---
63 -sté-, pAr. ni-Sd-, unchanged in Iranian and generalized: n2y-aStayam, т-а ауа, contracted ni-Sàya. Skt. sam-aranam, OP hamaranam; but with pre- fix, ufhamaranakara, with double writing of the initial, $ being the value after u, and A being the value when initial in the separate word. Perhaps also OP PatiSuvart§ for Ра
---
65 rgava- to Margu-, duS-iydra- to yàr-, vazra- in vazra-ka- to *vazy-, eühara- in Gira-vahara- to *yasr-, u-zma- to гат-, hama- to ham-; perhaps Gau-baruva- to baru-, müha- о mah-, viða- to vid-. IIT. With no obvious simpler nominal or verbal form: ama- in Arsdma-, asa- aspa-, u-ba-, poss. ^upa-, kaufa-, kara-, daiva-, d
---
---
---
85 . sdrvasya (haruvahyaya is a defec- tive writing not indicating the length of the vowel), ef. Isf. ahyayà (8199). Ш. OP hama- ‘one and the same’ (Av. hama-, Skt. samá-) has hama DB 4.92, either nsm. Лата? or asn. as adv. *hama? with pron. nt. -d (in DB 4.90, asn. as adv., 1f correetly read); gsf. hama- hyàyà, formed on
85 efec- tive writing not indicating the length of the vowel), ef. Isf. ahyayà (8199). Ш. OP hama- ‘one and the same’ (Av. hama-, Skt. samá-) has hama DB 4.92, either nsm. Лата? or asn. as adv. *hama? with pron. nt. -d (in DB 4.90, asn. as adv., 1f correetly read); gsf. hama- hyàyà, formed on stem extracted from gsm. *ham
85 DB 4.92, either nsm. Лата? or asn. as adv. *hama? with pron. nt. -d (in DB 4.90, asn. as adv., 1f correetly read); gsf. hama- hyàyà, formed on stem extracted from gsm. *hamahyd, like isf. ahydyd and haruwvahydyd. §204. THe NuwERALS are scantily represented in OP, since they are commonly indicated by nu- merical signs (
---
---
95 бтуа. B. As predicate to a nominative subject: DB 1.1 adam Dérayavaus, 1.7 vayam Hazámanikiya даһуйатаћу, 2.27 avabasém hamaranam kartam. C. As appositive to a nominative: DB 1.1 adam Dérayavaus zXayabiya vazraka. D. By anticipation for another case, normally with a resumptive pronoun or adverb which de- fines the case
---
96 tivà ava akunavayata ‘either by night or by day, that was done’; DB 2.61f Güravaharahya mahya jiyam- nam patiy avat sam hamaranam kartam ‘on the last of the month Thuravahara, then by them the battle was fought’. L. To express specification: námà as in Margus nimd dahyau$ ‘a province Margiana by name’ (DB 3.11), if пат
---
103  loc. уйй à, prep. w. abl. radiy, postp. w. gen. vi-, pref. w. verbs and nouns. hacà, prep. w. abl., loc., instr., adv. hadā, prep. w. instr. The inseparable prefixes are the following: a- an-, the common negative prefix. u- (= *u-) ‘well’, duš- ll’. ha- ham-, equal in meaning to Gk. civ and Lt. com- as prefixes. The u
---
106  айу DNb 46f ‘and I had the strength to develop them’. (b) to express purpose, with verbs of motion: only in the phrase hamaranam сатіапату ‘to make battle’ (DB 1.93f, and 10 other oc- currences), depending upon @# ‘he went’, paraua (pl. ptc.) ‘they went forth’, јла ауа ‘he sent forth’. §283. Тнв Parricrptes in OP have
---
107 minated or habitual and repeated. The two tenses are seen in the variations of the same phrase: aorist in DB 1.90 avadd hamaranam akuma ‘then we made battle’, and imperfect in DB 2.23 ayadà hamaranam akunaus ‘there he made battle’, both denoting terminated action. So also the im- perfect adadd ‘created’ is used in the 
107 tions of the same phrase: aorist in DB 1.90 avadd hamaranam akuma ‘then we made battle’, and imperfect in DB 2.23 ayadà hamaranam akunaus ‘there he made battle’, both denoting terminated action. So also the im- perfect adadd ‘created’ is used in the phrases at the beginning of DPd, DNb, DSe, precisely as the aorist adà
---
109 rect or an indirect question with the indicative. Perhaps there should be included here also aciy ‘then’ (§291.IV); and hakaram ‘once’ (DNb 34f), used with the subjunctive as the equivalent of a future general condition (‘once let there be seen ... = 5 at any time there shall have been seen’). $294, Tue CONJUNCTION уйй
---
120  With names of places, 32 occurrences. The E | common sequence is typified by DB 2.39 Tigra -% nama йай Arminiyaty wadā hamaranam akunava a ‘A stronghold by name Tigra, in Armenia—there 4 they made battle.’ A more elaborate phrase isin 4 DB 1.58f, quoted above. After the place name and A пата or námà follows a generic 
---
136 am : ajanam : vasiy : ыз MR E rau 90 208. Е ае айай : соод t ^ d : ш ч. TS ii айа = ооа sr : ds -hadi 21 І muti : тат : hamaranam : 94 cartanaiy : pasiva : hamaranam : akumá : Auramazdámaiy : upastüm : abara : vašnā : Aurama 95 zdīha : küram : tyam : Naditabairahyd : adam : ajanam : vasiy : aniya : üpiyá : уай : à 96 p
136  208. Е ае айай : соод t ^ d : ш ч. TS ii айа = ооа sr : ds -hadi 21 І muti : тат : hamaranam : 94 cartanaiy : pasiva : hamaranam : akumá : Auramazdámaiy : upastüm : abara : vašnā : Aurama 95 zdīha : küram : tyam : Naditabairahyd : adam : ajanam : vasiy : aniya : üpiyá : уай : à 96 pisim : parábara : Andmakahya : māhyā
136  ajanam : vasiy : aniya : üpiyá : уай : à 96 pisim : parábara : Andmakahya : māhyā : 11 : raucabis : бака: dha :avatà : hamaranam : akuma Notes то DB I: Our text of DB is based essentially on KT's examina- fion and edition, supplemented by the examinations of the original by Jackson and Cameron. The notes inelude the a
136 avam; ^ pasá]- va; S Aya; " par[ulva[m]eliy; 2 Аста; *agau[balà; 87 Auramazddmaiy; 9 ауада; * Bübirum : yale; * miam; М hamaranam; **dpryà. WB, from Wb.s reading of КІ. °з squeezes, add the following, also in roman, which were not visible to KT, nor to RI.:  asi]yava; ** Madame-; ** abiy : md-. "TRANSLATION or DBI: 81.
---
139 a : hauv : Vidarna : ha 22 dà : kara : айуауа : yafà : Madam : parárasa : Māruš : пата : vardanam : Ma 23 дау : ауада : hamaranam : akunaus : hada : Мада : һуа : Màdaisuvà 24 :ma(iSta : dha : hauv : adakaiy : пау : avadà : аһа : Auramazdimary : u 25 раѕійт : арага : vasnà : Auramazdáha : kāra : hya : тара : avam : kàra
139 am : kàram : t 26 yam : hamiciyam : aja : vasiy : Animakahya : mähyä : XXVII : raueabis : fakat 27 à : аһа : avatüsám : hamaranam : kartam : pasáva : hauv : Ката : һуа : manā : Карада : пат 28 à : dahydus : Mádaiy : avadà : mam : amánaiya : y8tà : adam : arasam : Mada ' 20m : 08у : Dàrayavaus : xšāyaðiya : адаг х : nàm
139 a : Dadarsi 32 š : aSiyava : yafà : Arminam : parárasa : pasáva : hamigiya : hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш :
139 hagmatà : paral 33 tà : patiš : Dādaršim : hamaranam : cartanaiy : Züzahya : пата : àvahanam : А 34 rmíniyaiy : avadà : hamaranam : akunava : Auramazdimaiy : upastàm : a 35 bara : vasnà : Auramazdàha : kāra : һуа : manā : avam : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09aka
139 m : küram : {уаш : hamigiyam : 36 aja : vasiy : Oüravaharahya : máhya : VIII : raucabis : 09akatà : dha : ava 87 à$üm : hamaranam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hama
139 nam :kartam : бабу : Dárayavaus : z3àyaffya : patiy : duv 38 itiyam : hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hami
139 hamigiyà : hagmatà : paraitd : patiš : Dàdar&im : hamaranam : carta 3€ nay : Tigra : пата : didà : Arm‘niyavy : avadà : hamaranam : akunava : А 40 uramazdàmaiy : upastàm : арага : vašnā : Ашатагдаћа : kāra : һуа : тапа :a 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бака
139 41 vam : káram : tyam : hamigiyam : aja : vasiy : G9üravüharahya : mihya : ХҮШ 42 :raueabiá : бакаќа : аһа : ауабадат : hamaranam : kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : 
139  kartam —— : 00у : Daraya 43 vaus : xšāyaðiya : patiy : citiyam : hamictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giy
139 ictyd : hagmatà : paraita : pat 44 iš : Dádar&im : hamaranam : cartanaiy : Uyama : nama : didi : Arm'myaty :a 45 vadā : hamaranam : akunava : Auramazdimaiy : upastam : арага : vaSnà : Aurama 46 zdàha : kāra : һуа : manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha
139  manā : avam : küram : tyam : ham?giyam : aja : vasiy : Oàigarea 7 d :mábyà : IX : raucabis : Nakata : dha : ауада ат : hamaranam : kartam : pasava 48 : Dadarsis : citā : mim : amánaya : Arm/niyaiy : yiti : adam : arasam : Ма - == 4 T= 122 OLD PERSIAN . DB П 49 dam : іу : Därayavauš : xšāyaðiya : pasáva : Vaumisa : nàm
139 a : Vaumisa : a 52 Syava : yatà : Arminam : parárasa : pasàva : hamiçzyā : hagmatà : paraitā : pa ^ 58 tiš : Vaumisam : hamaranam : cartanaly : Izalà : пата : dahyáus : Абшау M 54 à : avadà : hamaranam : akunava : Auramazdamaiy : upastàm : арага : vasnà : Au 55 ramazdaha : kava : hya : mani : ауага : Кахал : tyam : ham
139  : hagmatà : paraitā : pa ^ 58 tiš : Vaumisam : hamaranam : cartanaly : Izalà : пата : dahyáus : Абшау M 54 à : avadà : hamaranam : akunava : Auramazdamaiy : upastàm : арага : vasnà : Au 55 ramazdaha : kava : hya : mani : ауага : Кахал : tyam : hamiciyam : aja : vasiy : 56 An&makahya : máhy& : XV : raucabiá : 0akatà : 
139 ani : ауага : Кахал : tyam : hamiciyam : aja : vasiy : 56 An&makahya : máhy& : XV : raucabiá : 0akatà : aha : ауада а : hamaranam : 57 kartam (айу: Dàrayavaus : xšāyaðiya : patiy : duvitiyam : ham 58 iciyd : hagmata : paraità : patiš : Vaumisam : hamaranam : cartanaly : Au 59 tiyàra : лата : dahyius : Armmiyaiy : ауада
139 am : 57 kartam (айу: Dàrayavaus : xšāyaðiya : patiy : duvitiyam : ham 58 iciyd : hagmata : paraità : patiš : Vaumisam : hamaranam : cartanaly : Au 59 tiyàra : лата : dahyius : Armmiyaiy : ауада : hamaranam : akunava : 60 Auramazd&maiy : upastàm : арага : vasnà : Auramazdaha : kara : һуа : ma 61 ni : avam :
139 yd : hagmata : paraità : patiš : Vaumisam : hamaranam : cartanaly : Au 59 tiyàra : лата : dahyius : Armmiyaiy : ауада : hamaranam : akunava : 60 Auramazd&maiy : upastàm : арага : vasnà : Auramazdaha : kara : һуа : ma 61 ni : avam :
---
140  káram : tyam : hamiciyam : aja : vasiy : Güravüharahya : mah 62 ya : jiyamnam : рабу : avatiSàm : hamaranam : kartam : pasàva : Vaumisa 63 :cità : mim : amanaya : Árminiy&ty : yata : adam : arasam : Madam 64 :08tiy : Dirayavaus : xšāyaðiya : pasáva : adam : nijàyam : haca : 65 Babiraus : айуауаш :
140 am : Kud"ru$ : nama : 66 vardanam : Мадалу : avada : hauv : Fravartis : һуа : Madaty : xSdyafiya : a 67 gaubatà : ài$ : hadā : kara : patiš : mim : hamaranam : cartanaiy,: pasáva : hamarana 68 m : akuma : Auramazdimaiy : upastàm : арага : vasnà : Auramazdaha : Кагат 69 : tyam : Fravartais : adam : ajanam : vasiy : Aduk
140 danam : Мадалу : avada : hauv : Fravartis : һуа : Madaty : xSdyafiya : a 67 gaubatà : ài$ : hadā : kara : patiš : mim : hamaranam : cartanaiy,: pasáva : hamarana 68 m : akuma : Auramazdimaiy : upastàm : арага : vasnà : Auramazdaha : Кагат 69 : tyam : Fravartais : adam : ajanam : vasiy : Adukanatsahya : máhyà : XXV :та 
140 агат 69 : tyam : Fravartais : adam : ajanam : vasiy : Adukanatsahya : máhyà : XXV :та 70 ucabiš : &akatà : dha: ауада : hamaranam : akumá : @ātiy : Dàrayavaus : x 71 šāyaðiya : pasàva : hauv : Fravarüs : hada : kamnaibi$ : asabāraibiš : amufa : Ra _ 72 gi : nama : dahyaus : Mádaiy : avapara : asiyava : pasiva : adam : 
140 К 84 dram : hamigiyam : һуа : mana : naiy : gaubataly : avam : jatà : pas 85 āva : Taxmaspáda : hada : kira : aSiyava : hamaranam : akunau’ : had ) 86 à : Cigataxm& : Auramazdimaty : upastàm : арага : vašnā : Auramaz 87 daha : kara : һуа : mana : avam : kàram : tyam : hamiciyam : aja : uta : C 88 igataxmam : agarbaya :
140  : Vištāspa : 95 ауага : hadé : kara : hyasaty : anu&ta : dha : ViSpauzáti$ : пата : уагда 96 nam : Parbavaiy : avadà : hamaranam : akunaus : hada : Paréavaibis : Auramazdàmaiy 97 : upastàm : abara : vašnā : Auramazdáha : V зра : avam : kàram : tyam : hamiciya | 98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabi
140 avam : kàram : tyam : hamiciya | 98 m : aja : vasiy : Viyaxnahya : máhyà : X XII : raucabis : Sakata : dha : avatáSám : hamaranam : kartam DB II Nores то DB II: * asabirazbi$, form established by азага DNb 41-5. *a{muéa] Hüsing, Wb., for afbiy] RL, abliy} KT. * {Mudräya] Wb., KT, after the Elam. u avadā : dha legible, 
---
143 ON 125 4 :pasáva : Vistáspa : āyasatā : avam : kāram : ašiyava : Patigraba 5 nā : nama : vardanam : Рагдауају : ауада : hamaranam : akunaus : hada: 6 hamigiyaibis : Auramazdàmaty : upastám : abara : vašnā : Auramaz 7 daha : Vi&táspa : avam : küram : tyam : hamiciyam : аја : vasiy.: Ga $ rmapadahya : mahya : I : rauca :
143 spa : avam : küram : tyam : hamiciyam : аја : vasiy.: Ga $ rmapadahya : mahya : I : rauca : 0akatam : dha : avaflásàm : hamaranam : ka 9rtam : 88у : Darayavaus : xSayafiya : pasiva : dahy&us : ma 10 ni :abava : ima : tya : mană : kartam :Parfüavaiy : §atiy : Darayavau 11 š: xšāyaðiya : Margué : nàmá : dahyáus : hauvmai
143 : paraidty : ava 15 m : кагат : jadiy : hya : mana : пазу : gaubataiy : pasáva : DadarSis : hada : К 16 Ārā : a’iyava : hamaranam : akunaus : hadá : Márgavaibi$ : Auramazd 17 &àmaly : upastim : арата : vana : Auramazdaha : kara : hya : mana : avam : кагат 18 : tyam : hamigiyam : aja : vasiy : Agiyádiyahya : mahya : XXI
143 m : кагат 18 : tyam : hamigiyam : aja : vasiy : Agiyádiyahya : mahya : XXIII : raucabi 19 š : бакеќӣ : dha : avaðāšām : hamaranam : kartam  :@айу: Darayavau 20 $ : xSdyafiya : pasàva : dahy&us : manā : abava : ima : tya : ma 21 nā : kartam : Baxtriya — :08tiy : Dárayavaus : xSaya 22 fiya : I martiya : Vahyazdáta, : пат
143 nam : Parsaly : а 35 vadā : hauv : Vahyazdáta : һуа : Bardiya : agaubatà : ài : 36 hada : kara : patiš : Artavardiyam : hamaranam : eartanaiy : pas 97 ava : hamaranam : akunava : Áuramazdámaiy : upastàm : abara : va 38 Snà : Auramazdaha : kāra : hya : manā : avam : káram : tyam : Vahya 39 zdàátahya : aja : vasiy : Güra
143 hyazdáta : һуа : Bardiya : agaubatà : ài : 36 hada : kara : patiš : Artavardiyam : hamaranam : eartanaiy : pas 97 ava : hamaranam : akunava : Áuramazdámaiy : upastàm : abara : va 38 Snà : Auramazdaha : kāra : hya : manā : avam : káram : tyam : Vahya 39 zdàátahya : aja : vasiy : Güravaharahya : mahya : XII : raucabis : 
143 ram : tyam : Vahya 39 zdàátahya : aja : vasiy : Güravaharahya : mahya : XII : raucabis : бака 40 tà : aha : avađðāšām : hamaranam : kartam 4 : Gdtiy : Dārayavauš : xsāyaði 41 ya : pasáva : hauv : Vahyazdáta : hada : kamnaibis : asabáraibis : a 42 mufa : aSiyava : Paxsyàuvadàm : hacd : avadaga : kāram : àyasa 43 tā : hy
143 s : a 42 mufa : aSiyava : Paxsyàuvadàm : hacd : avadaga : kāram : àyasa 43 tā : hy&param : 418 : patiš : Artavardiyam : hamaranam : cartana 44 iy : Parga : nama : Каша : avadā : hamaranam : akunava : Auramazdima 45 iy : upastám : арага : vaSnà : Àuramazdáha : kara : hya : manā : ava 46 m : kàram : tyam : Vahyazdatahya 
143 kāram : àyasa 43 tā : hy&param : 418 : patiš : Artavardiyam : hamaranam : cartana 44 iy : Parga : nama : Каша : avadā : hamaranam : akunava : Auramazdima 45 iy : upastám : арага : vaSnà : Àuramazdáha : kara : hya : manā : ava 46 m : kàram : tyam : Vahyazdatahya : aja : vasiy : Garmapadahya : mah 47 ya : V :raucabis : S
143 46 m : kàram : tyam : Vahyazdatahya : aja : vasiy : Garmapadahya : mah 47 ya : V :raucabis : Sakata : Sha : avatiaSàm : hamaranam : kartam : uta : ava -48 m : Vahyazditam : agarbiya : utà : martiya : tyaisaiy : (габат 49 à : anuSiy& : áhata : agarbàya | :9àtiy : Darayavaus : xš 90 ауайуа : pasiva : adam : ava : Vahyazd
143 vahaus : xsayatiyahyà : gaubataiy : pasāva : hauv : kara : айуа 60 va : tyam : Vahyazdata : früisaya : abiy : Vivànam : hamaranam : cartanaiy : К 61 āpišakāniš : nàmà : didà : ауада : hamaranam : akunava : Auramazdimal _ 62 y : upastàm : abara : va&nà : Auramazdaha : kāra : һуа : manā : avam : káram : tya Be 63 m : ham
143 60 va : tyam : Vahyazdata : früisaya : abiy : Vivànam : hamaranam : cartanaiy : К 61 āpišakāniš : nàmà : didà : ауада : hamaranam : akunava : Auramazdimal _ 62 y : upastàm : abara : va&nà : Auramazdaha : kāra : һуа : manā : avam : káram : tya Be 63 m : hamigiyam : aja : vasiy,: Animakahya : mahya : XIII: raucabi$ : @ak
143 ram : tya Be 63 m : hamigiyam : aja : vasiy,: Animakahya : mahya : XIII: raucabi$ : @akatā : аһа: a ^ V a 64 vatüsSàm : hamaranam : kartam : айу : Darayavaus : хёйуабіуа
---
144  : patiy : h 65 yàparam : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiy
144 ram : hamiciya : hagmatà : paraità : patiš : Vivanam : hamaranam : cartana 66 iy : Gadutava : nàmà& : dahyáus : avadd : hamaranam : akunava : Auramazdima 67 iy : upastam : abara : vasnà : Auramazdāha : kira : һуа : mana : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā : 
144  : avam : káram : t 68 yam : hamigiyam : aja : vasiy ; Viyaxnahya : mahya : ҮП : raucabié : ðakatā : 69 аһа : avaásàm : hamaranam : kartam : fàtiy : Dárayavaus : xšāyaðiya : 70 pasáva : hauv : martzya : һуа : avahy& : kárahyà : mafia : dha : tyam : Va 71 hyazdata : fr&isaya : abiy : Vivánam : hauv : amufa : hada : kamn
---
151 : Pársa : тапа : badaka : avamSém : табат : aku 9 navam : pasáva : haw : Gaubaruva : hada : kara : aSiyava : 10 Uvjam : hamaranam : akunaus : hada : Üvjiyaibi�
---
153 6.53-82 makes and adopts the following emendations which are not discussed in my article, and which JI do not accept: " hadā : karla : S[ugdam; % laniyam] for [vasiy], * [aniya] for [haus], 27 21055 for ша їт; " hyalilam : тан Ма, which violates the recorded length of the gaps. Eilers JNES 7.106-10 proposes, after yadá
---
---
---
---
---
---
---
194 60.Ia; wrongly Hz. ApI 101-3, who takes -kara- in avükara- and ciyükara- not from kar- ‘do’, but as kara- ‘time’, as in hakaram, q.v.). avakaram nsn. (6259) DNb 6; avdkaram-ca-mary ($109, $133, $135) DNb 2f. avajam, see vaj-. avabà adv. ‘thus, then’: LAv араба: 'ava- + adv. suffix -6@ (§191.If), cf. Skt. td-thd. Often 
---
---
207 sm. DB 149, 53; DSe 37. @& ciy asn. DB 1.58. paruvam-ciy DB 1.63, 67, 69. yaciy (q.v.) DNb 35, 36, 57. haw-cty DPe 23f. hakaram-ciy DNb 34f. [haca-cily DSf 23: vakna-|cily XPg 7f, less likely than vaknalptly, see under apiy. | Citcizri- sb. ‘Cincikhri’, father of Martiya (§163.V): Elam. st-in-sa-ak-ri-1§, Akk. #-in-Sa-
207  Skt. kiyat nsn. ‘how much, how many’, + kara- to root kar- ‘make’ ($160.19; Bthl. AiW 597; hardly to kara- ‘time’, cf. hakaram, as taken by MB Gr $293, Hz. ApI 101-3). ciyakaram nsn. (§259) DNa 39; ciyükaram DNb 50; ciyakaram-ca-maiy (written — : -"m*m*eur; $41, $51, $132, $138.I; Lg. 15.178, — | against Hz. ApI 240) 
---
---
---
```


## [2026-09-14T01:57:34.223Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KNT.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(225,232):\n    print('==== leaf',i, len(t[i]))\n    print(t[i][:400].replace('\\n',' '))\nEOF\necho \"=== search LEXICON headers\"\ngrep -o \"LEXICON 2[0-9][0-9]\" KNT.txt | sort -u | head -40",
 "description": "Inspect Kent tail leaves"
}
```


### [2026-09-14T01:57:35.450Z] TOOL RESULT

```
==== leaf 225 3833
BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11. brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhratar-, Gk. @parnp ‘clan-brother’, Lt. frater, OCS bratru, Gt. brobar, pIE *bhráter- (862, 875.111, $128, $154.П). баі nsm. ($124.5, 5186.1) DB 1.29f, 39f. brazmaniya- adj. ‘prayerful, reverent’ (cf. Kent, Lg. 21.223
==== leaf 226 3746
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32. Müda- (S166.IIT) adj. ‘Median’; masc. as sb. ‘Media’, a province of the Persian Empire: Elam. ma-da, АКК. ma-da-a-a, Gk. pl. Mado. (1) ‘Median’: Mada nm. DB 1.49; 2.14°, 16, 18, 82; 418; DN 1°; APP 2, Madam asm. DB 2.21, 82; 3.30. Mada npm.
==== leaf 227 3685
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36. EU: ET TORR ON | INS SEE cals la pen X AN, ae ete. ЫЗ, Ses f. Av m ee Sm SN Ie e mne - LEXICON 203 ‘martiya- adj. as sb. ‘man’: -ize- extension of pIE *morios, Av. marata- ‘mortal, man’, NPers. márd, Skt. mária- (§31, $106, $122, 5
==== leaf 228 3992
so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V). (1) ‘Egyptian’: Mudrdya nsm. А?Р 19. Mudráyà npm. DSf 50f, 52, 55. (2) ‘Egyptians’, as province: Mudräyā npm. DPe 11f. (3) ‘Egypt’: Mudráya nsm. DB 1.15, 27°; DNa 27; DSe 26°; DSm 7^; XPh 28. Mudrüyam asm. DB 1.32, 33; DZe 8. Mudrayé absm. DSf 41; DZe 11. Mudrüyaty ls
==== leaf 229 3950
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt. mid. with Wb. Symbolae Koschaker 196, nor fut. pass. with Hz. AMI 8.67, ApI 357-8) XPh 39. lwadé- conj. ‘where’: GAv yada, Skt. yada; probably rel. nt. pAr. #00 + postpos. 4. уайд- tya XPh 35f ($133, $29
==== leaf 230 1505
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2. гада- sb. ‘wagon’ (570.11, $148.11), see urata-. Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, KZ 37.564-5; Bthl. AiW 1505; MB Gr. $19
==== leaf 231 1256
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29. vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See als
=== search LEXICON headers
LEXICON 203
```


## [2026-09-14T01:57:42.144Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" KNT.txt; grep -n \"hadi[sš]\\|Hagmatāna\\|Hagmatana\\|hagmatana\" KNT.txt | head -20",
 "description": "Search Kent for Hagmatana"
}
```


### [2026-09-14T01:57:42.242Z] TOOL RESULT

```
5869
845:A’Se 4f [тат (asf. for asn. ima) hadiš; 6 tya (for asf. уйт) afagainàm.
911:Н. pIE ә was the reduction of ë or 6 or à; it became 7 in pAr., but a in all other ЕЕ branches.! *noté|r] father’, OP рий, Skt. рий, Gk. татр. *sedos, ОР hadiš ‘abode’, but *sedos, Gk. os
1635:(2-3) pAr. split of pIE s into s š A, and plr. split of pAr. s into s and A (8115): stanam avas- layam niyašiāyam ачоіа; hadiš niy-asddayam; afaham 6asianaty; nom. ending in baga-" pasti- ріти-&.
1970:regularly given; but it is given with names of provinces only when there is a list of all or several, and is omitted with some larger districts (Kar- тала, Varkàna), with cities (Pársa, if = ‘Persepo- пе’; Passiyduvdda ‘Pasargadae’; Hagmatana 'Ecba- tana’; Arbatra ‘Arbela’; Babirus ‘Babylon’), and with well-known rivers (Ufrätuš ‘Euphrates’;
2038:Loc. Sg. Parsaiy, Mädaiy, Mudrüyaiy, Ujaiy Unjaiy, Pardavaiy, Arminiyaiy, Asagartaty, Hagmatanaty; with added -à, duvarayd, dastayd, spaémardayd, probably kar Saya, {dalrtanayd; nt. uzmaya.
2196:III. Apparently there was also a nt. suffix -as-, not varying within the paradigm nor in the corre- sponding masc. formation: type Skt. kravís ‘Taw flesh’, Gk. xpéas. OP nom.-ace. hadiš from *sed- as, cf. ОК. éðos from *sed-os; ace. abicaris *pasture- land’, see Lex. s.v. In names, Hazd-manis, Ardu- mants, perhaps I-mami$; late gen. Haxdmanis- ahyd adds the gen. ending of -o- stems to the nom. as stem.!
4248:21 ya : adam : akunavam : visam : vašnā : Auramazdáha : 22 akunavam : ima : hadis : tya : QüsAyà : akunavam : 28 haring > аа саа а jfrava
4252:27 nā : upariy : avàm : каш : hadis : frásahya.
4481:XPc = XERXES, PERSEPOLIS C. 1 Бара : vazraka : Auramazda : hya : пойт : bümim : 2 ада : hya : avam : asmànam : ada : һуа : marti 3 yam : ada : һуа : Siyátim ; ada : martiyahyà 4 : һуа : Xšayāršām : XS8m : akunaus : aivam : pa 5 rūnām : XSm : aivam : pariinam : framátàram 6 :adam : XSayarsa : XS : vazraka : XŠ : XSanam : XS: 7 dahyünàm : paruv : zandndm : XS : аһуйуй : b 8 ümiyà : vazrakiya : düraiy : apiy : Darayava 9 haus : XShya : puça : Haxāmanišiya : 6atiy : X 10 šayāršā : XS : vazraka : vašnā : Aurahya Mazdaha : i 11 ma ; hadis : Dárayavaus : XS : akunaus : hya : manā : 12 pità : mim : Auramazda : pátuv : hada : baga 13 ibis : utd : tyamaty : kartam : uta : tyamaiy : 14 pica : Darayavahau’ : XShyá : камат : avaSely 15 : Auramazda : pátuv : hada : bagaibis
4637:3 шу: Xšayäršā : хдйуабїуа : ima : hadis : akunàm : разара : yabà : adam : z$àya
4685:D'Sb = Darius IT, Sesa B. 1 айат: Dárayasaus : XS : vazraka : XŠ : XSyanam : XŠ : DHyünàm XŠ : а 2 hydyd : Вуй: Artazsagahyá : XShyá : puça : Haxamanisiya : 3 batiy : Dürayavaus : XS : ima : hadiš : Arlaxíacü : paranam : akunaus : 4 hya : mand : pilà : ima : hadis : pasava : vasnà : ÁMha : adam : akunavam Notes то D'Sb: Вга. WZKM 39.85-7, after the Akk., restored ? [apara]m ‘upper part’ = ‘part at the top of the slope’, and * [adaram] ‘lower part’ = ‘part lower on the hill’; but Hinz, ZDMG 91.251-2, restores [paranalm and [pasava], in temporal sense, which is preferable. *akunas in copy b. TRANSLATION OF D'Sb: $1. 1-2. ... (= DNa 8-12, with one omission), son of Artaxerxes the King, an Achaemenian. §2. 3-4. Saith Darius the King: This palace Artaxerxes previously built, who was my father; this palace, by the favor of Ahuramazda, I after- wards built (to completion).
4698:A’Sc = Artaxerxes II, Susa c. 0 Dérayavausahya : XShya : puça : 0 Dérayavausahya : V'Staspahya : puça 1 : Haxamanisiya : дану : Artaxsaga : 2 xSayabiya : vazraka : rSayafiya : х 9 šāyaðiyanām : xSdyafiya : dahyün 4 äm : xšāyaðiya : ahydya : bumiyd : 1 5 mam : hadis : uta : imam : usta 6 сапат : tya : afagainám : ta +++++4 ООА : Auramazdà :
4704:3 vasnd : AMhà : imam : hadis : tya : j'vadiy : paradayadàm : adam : akunavam : AM : Anah 4 ita : uta : Mitra : mam : pàtuv : hacd : vispà : gastà : utamaiy : kartam Nores то À'Sd: Text according to the line-divisions of copy da. ‘af... de; ahydya db; ahyd de. ? Hazámanikiya db; Harémaniya da, de. 3 akul... da; аштайт db; akuvanašāša de. *hacá da; lost in db; ha Xà de. * vispá da, de; »*dspa db. * gástà da, db; gastü dc. * uta... da; utamaty db; ufamay de. TRANSLATION ОЕ А284: 61. 1-2. ... (= A’Sa 1), an Achaemenian. $2. 2-4. Saith Artaxerxes the King: By the favor of Ahuramazda this is the palace which T built in my lifetime as a pleasant retreat. May Ahuramazda, Anaitis, and Mithras protect me from all evil, and my building.
```


## [2026-09-14T01:57:44.499Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT hanjamana\"; grep -n \"hanjamana\\|haṇjamana\\|hanjamna\\|haujamana\" BRT.txt | head -20\necho \"=== BRT hangam\"; grep -n \"hangama\\|haṇgama\" BRT.txt | head -10\necho \"=== BRT handarəza\"; grep -n \"handarəz\\|handaraz\\|handarez\" BRT.txt | head -10",
 "description": "Bartholomae greps"
}
```


### [2026-09-14T01:57:44.595Z] TOOL RESULT

```
=== BRT hanjamana
17874:reden, besprechen':  vlspalfO  ^frasnailü vTspaäa  hanjamanalsä  yaU  apinsaltim (3D.,  Augm.)  mazda sca  xardhustrasca "bei  allen  Besprechungen,  bei  allen  Zu- sammenkünften, bei  denen  sich  bespra- chen . ,"  Y.  72.  5.  a)  mit  Angabe des  'mit  — '  durch  o)  Instr.:  anulAaxs *armaitis  matnyS  *p»r3saite ya'hra  ma/%a (ad.)  Y.J7. 12;  —  hs  aSava  yail  p3r3iai dngva  vä  "wer  von  denen,  zu  denen  ich
20235:—  kai  afava  'da  vanat  drvant»m  Yt./,  aS; — pata  nS  ibifyantaipairi  °</jj(als  Vok.)/a armaitiica  SrB.j;  —  hanjamanaisü  yai/ apmsalhm  'd3s^  sara'küitraslä  Y.  12.  5 ;
23944:•  j.  vi-£ar3na-  n.  Trennungsstelle,  Stelle, wo  sich  der  Weg  teilt":  pa%amcS  *'rjnä'> .  .  pahqmia  hanjamana  Y,  4-3.  i ;  — fakqm  '.  .  paiti  'na  Yt  //.  4,  Vyt.  54.
24412:—  °/i7?j(i/n(GPm.)Ä  ra%wqm  'panqm- (GPf.>o  'ratufriünqm  Vr.g.y;  —  'pa- nqm  (GPm.)  arinäm  . .  'panqm'  (GPf.) häirisinqm'  Y.  65.  2;  1.  12»,  2.  11,  g.  18, 2Ö'.2,  7-9^  27.1,  62.8,  77,8,  Ytj.2a,  50, Ä'.39,  70.  145.  J2.  17,  /J.  145'.  '48^  77.1, 1S.6,  ig. 35,  V.  2.  a7f.<,  7j.  16,  7Ä70,  Ny. 4. 1'.  FrW.  7. 1,  N.  22, 3S,  3g,  5g,  Vyt. 50, Vd.  2,  4,  12,  77;  —  'panqm  (GPn.)  däma- nam  Yt70.S4';  7^.135',  Y.7.16,  77.  11, 27.  z,  H.  7. 1',  V.  13. 16,  N.  68,  FrW.  j.  2, 4.1»;  —  'panqm  (GPm.)  anu  mqhnm Yt.  5.  95;  —  'panqm  (GPm.)  maxilt»m "eum  qui  est  omnium  maximus"  Y.  4$. 6,  79.1a,  27.1,  Vr.  77.  ai;  P.  40  (Sp. 52  f.);  —  'panqm  (GPn.)  vahtshm  "id quod  est  omnium  Optimum"  Y.  43-  ^i 44-  7;  — paourvlm . .  'psng  (GPn.)  "primo omnium"  Y.  2Ä1;  —  mihrö  7>?(GPm.?) matdayasnanqm  .  .  >rHiwä{sA.)i!a  .  .  Yt. 70. 120;  —  'paisa  hanjamana^B  Y.  72.  5; S,  P.27',  N.7?',  Yt77.  3%  75.53';  — 'pshu  paiti   barfzähu   Yt70.45;  45;  —
29334:hanjamana-  1770
=== BRT hangam
=== BRT handarəza
```


## [2026-09-14T01:58:44.337Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 syn-\"; python3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r\"syn-, \", t):\n    print(t[max(0,m.start()-200):m.start()+900].replace('\\n',' '))\n    print('-----')\n    break\nfor m in re.finditer(r\"\\bhomo-, \", t):\n    print(t[max(0,m.start()-200):m.start()+600].replace('\\n',' '))\n    break\nEOF",
 "description": "Klein syn- and homo- entries"
}
```


### [2026-09-14T01:58:45.731Z] TOOL RESULT

```
=== KLN 1966 syn-
bly,  diet,  specif,  the Constituent  Assembly  of  the  Polish  Republic. —  Pol.  sejm,  ‘assembly’,  rel.  to  OCzech  snem, Czech  sngm,  for  *syn-imu,  lit.  ‘a  taking  together’, fr.  pref.  syn-,  ‘together’,  and  *imu,  ‘a  taking’;  fr. Pol -jqc,  resp.  Czech  jqti,  ‘to  take’;  rel.  to  OSlav. imq,  j(ti,  ‘to  take’  (orig.  *imo,  cp.  vuz-imq,  ‘I take  away’),  imami,  imejq,  imeti ,  ‘to  have’,  Lith. imu,  ifhti,  Lett,  jemu,  jemt,  ‘to  take';  fr.  I.-E. base  *em-,  ‘to  take’,  whence  also  L.  emere,  ‘to take,  buy’.  See  exempt,  v.,  and  cp.  words  there referred  to. sekos,  n.,  the  sacred  enclosure  of  a  temple.  —  Gk. CTY)x6q,  ‘shrine,  enclosure’;  of  unknown  origin. Selachii,  n.  pi.,  an  order  of  elasmobranch  fishes (ichthyol.)  —  ModL.,  fr.  Gk.  cAXorf  Uc,,  ‘any cartilaginous  fish;  a  shark',  which  prob.  derives fr.  ueXai;,  ‘light,  brightness,  flame’  (see  seleno-), and  is  so  called  from  the  phosphorescent  light these  fishes  are  used  to  emit. seladang,  n.,  gaur,  wild  ox  of  Malaysia.  —  Bor¬ 
-----
,  ‘to  send  homeward’, fr.  home,  n.  See  home. hominy,  n.,  a  meal  made  from  maize.  —  Prob. aphetic  for  Algonquian  auhuminea,  ‘parched com’. homo,  n.,  man  —  L.  homo.  See  human, homo-,  before  a  vowel  hom-,  combining  form meaning  ‘one  and  the  same,  jointly’.  —  Gk. 6(xo-,  6u-,  fr.  opo?  (for  *somos),  ‘one  and  the same,  belonging  to  two  or  more  jointly’,  rel.  to 6poU,  ‘together’,  and  cogn.  with  OI.  samdh, 'even,  the  same’,  L.  similis,  ‘like’,  Goth,  sama, ‘the  same’,  samana,  ‘together’.  See  same  and words  there  referred  to  and  cp.  esp.  homeo-, homalo-,  hama-,  the  first  element  in  Homer  and the  second  element  in  schorlomite. homoblastic,  adj.,  developed  from  cells  of  the same  kind  (biol.)  —  Compound
```


## [2026-09-14T01:58:46.060Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN p.30 (leaf 51)\"; python3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(len(t))\nfor i in (50,51,52):\n    print('==== leaf',i); print(t[i][:2500])\nEOF",
 "description": "Horn page 30"
}
```


### [2026-09-14T01:58:48.139Z] TOOL RESULT

```
=== HRN p.30 (leaf 51)
412
==== leaf 50
- 29 -
124. engehtn (AM.), enguhln *Honig, vergl. terenguhin,
sikengubi7i, sirkenguhln, gezengubln, gulengubm ; arab.
LW. anjuMn, vergl. /vskanjubm (Ibn Beitär) u. a. m.
phlv. angpen, angumen {e beweist das arm. LW.
gazpen *Tamariskenhonig).
bei. vergl. benag, n. b^nay *Honig' (36).
Das erste Glied des Compositums eng Biene' (Wörter-
bücher: änikj enik) vermag ich im Neupersischen nicht
zu belegen; es wird im Gazophylacium citirt, wohin
es aber auch nur aus persischen Originalwörterbüchern
gekommen sein wird. v. Stackeiberg, SAM^KA
H-BKOTOPWXX nEPCH4CKHX^ GIOBAX^ Kh OCETHHGKOMX
H3kIKS, S. 4 glaubt es im oss. LW. Anigol (der Schutz-
geist der Bienen) wieder zu finden ; vergl. auch kurd.
heng 'Biene, Bienenkönigin* (H.-Sch.).
kurd. hingiwin etc., afy. gabm^ garblna, minj. agman,
yidg. agMn scheinen sämmtlich aus dem Np. entlehnt
zu sein.
feig (fiOQTtjyCay xai Toiavrtjv riva vntjQeatuv ayead^ai , Suidas) , ayYcigta und
einige andere Ableitungen. Im Talmud findet sich X^*i;iiX u. a.
ayyaQoq 80 wie das unbelegte np. hengäred *er strengt sich an*, hengär
(Wörterbücher : henkär, henkäred) gehören nicht zu engärden und haben
wohl beide überhaupt nichts mit einander zu tun, trotz de Lagarde^s
Verweis auf das *Loos unserer Landpostboten* (Ges. Abh. 184).
College Jensen hält ayyoQog für babylonisch; er teilt mir
folgende Begründung dieser Ansicht mit:
„Babyl. *agru (*ein Gemieteter, zum Dienst Gemieteter, Ge-
zwungener*) konnte im Neubabylonischen zu *aggaru und dieses weiter
zu *angaru werden. Falls äyyuQo; babyl. *ahgarti = *agru entspricht,
könnte dies aus annlu (d. i. ^Mensch*) agru (^gemieteter , zum Dienst
gezwungener Mann*) oder abil sihri agru oder asgandu agru ('gemieteter
Bote, zum Dienst gezwungener Bote*) abgekürzt sein. Assyr.-babyl.
agäru 'mieten, zum Dienst zwingen* geht auf h-g-r zurück = arab.
hajara, cf. hajr 'Hinderung des freien Willens im Reden, (Obhut)*.
"AyyoQog für babylonisch zu halten, veranlasst mich einerseits die
dann gute Etymologie des Wortes, andererseits der Umstand, dass seine
Synonyma naxavStjc, aayavStjz (aoTfivSv]:.) und herld nur aus dem Babylo-
nischen befriedigend erklärt werden können: ''AnxavStjg, uayavSrjg =
^^^^^^(X) — b*^' (asgandu (askandii?) etc. = älterem ^aknu; herld =
babyl. biirldu (für älteres *(p)hurädn) = 'Eilbote' und 'schnelles Pferd'."
==== leaf 51
— 80 -
125. enguM Tinger, Zehe'; vergl. etigustetl 'Ring'^
engusfioäne Tingerhut* *).
Kä§. ungüss^) (neben engüst, mgüs etc.); mäz. nngus.
aw. angusta- 'Zehe'; phlv. angust^)\ skr. angtistha-
*Daunien, grosse Zehe*.
kurd. LW. engust; oss. d. at'ndje^ ünguljä Tinger
(LW.), t. ängursf (26); af/. güta; wa/. yangl, minj.
augar, §iyn. angast, sar. ingä/t, sangl. ingit.
Dialektisch findet sich Kä§. engxdt, mäz. e)igel^
vergl. skr. atlgün-, angüli- Tinger, Zehe'.
126. efiffist 'Kohle'.
Vergl. skr. angärä- 'Kohle'.
127. engeiten antreiben', Praes. engez-em,
phlv. angfytan antreiben', angejet (AV.), vergl.
ham]vB/t (Geiger, Yätk. Zar., Anni. 52); skr. vgl.
samvignu' 'aufgeregt'.
vergl. oss. d. ve^^nn^ t. viyin erschüttern, bewegen'
(80), bei. gejag n. ge^cig 'schwingen, schleudern,
schlagen' (113).
128. enose 'glücklich, heil!', vergl. hös, nöse, nösin,^)
aw. anaosa- unsterblich'; phlv. anöäak unvergäng-
lich', arm. LW. antcsak, anois,
oss. ämisoriy änusi 'unvergänglich' (119); nicht bei.
anJmy 'Schicksal' (2) (Hübschmann, ZDMG. 44, 555).
129. ö er, jener, Plur. ösän (dialektisch, Lumsden, Per-
sische Grammatik, II, 76 Anm.; vergl. gel. üsüfi,
ühan),
ap. aw. ava- jener'; päz. ö.
Vergl, kurd. ätr, atve jener, er'.
130. o- (Praefix), u-,
aw. ava 'herab, von weg'; phlv. ö; ai. dva.
131. ewam, awam 'Schuld', loam,
phlv. äpäm (PPGL).
bei. LW. warn (288).
^) Aw. *angu8tapäna' (vergl. aw. ranapäna-)'^ oss. d. LW.
ängurstevän.
*) Der Wechsel von st und st ist häufig.
'') Vergl. Fr. Müller, WZKM. 5, 264.
==== leaf 52
— 31 —
Darmesteter's Erklärung (Et. ir. I, 75) aus
*apama' d. i. apa 4- ama- = lat. abemptum ist aus zwei
Gründen unmöglich: erstens weil die Grundbedeutung
von emö nicht ^kaufen*, sondern nehmen* ist (vergl.
lit. imü, ifriti nehmen', air. ein 'nehmen*, ksl. imq,
jpM 'nehmen'); zweitens weil lat. emö auch zu got.
tnman gehört, also seine Urform *^rwö lautet.
132. öbäSten anfüllen; verschlingen (d. i. sich anfüllen)*
Praes. obarem , öbärlden ; öbäs 'Gesindel*, "»JITll^NilN
(Jer. 51, 44).
ap. *6l^;a -f l/'^)ar- (vergl. skr. avapürna") anfüllen';
phlv. avpartan bezw. öpärtan 'verschlingen' (Men., AV.).
133. öreng 'Schmuck (z. B. Vis und Rämin S. 24 Vers 4
V. u.); Thron*.
ap. *avaranga- oder wohl besser '^abiranga- (vergl.
skr. ranga- Tarbe* und auch 'Schauplatz, Theater);
phlv. hil]aürank (statt avrang), AV. 14, 8. (Hörn).
134. euJzen (geschrieben evzen) 'tödtend*, in ser]ewzen
(Sahn. I, 100 Vers 714, 450 Vers 288), hezber\ewzen
(Sahn. I, 356 Vers 659).
aw. aiwi + l/^aw- 'tödten' ; phlv. afzatan (PPGL),
päz. awazadan.
Np. evzendlden der Wörterbücher ist nur eine gram-
matische gelehrte Bildung ; über die Emendation ewzen
vergl. Salemann-Shukovski, Neup. Grammatik, § 7
(dieselbe verbietet die Ableitung von ava-),
135. östUm, ustam 'treu, ergeben' (Vis und Rämin, Seite 78
Vers 12 1).
ap. ^avastaman- 'zuverlässig*, vergl. skr. ava-r
i/^sthä' 'bleiben, verharren*, avasthita- (von Personen)
'standhaft, zuverlässig*; phlv. östam bezw. tistäm
'Helfer (Men., vergl. awastäm, West ib.).
136. öi 'er, jener, vei,
ap. ava' + hya-; päz. öi.
*j Hier scheint es aber ^schwach* zu bedeuten.
```


## [2026-09-14T01:59:01.289Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r\"syn-,\\s*pref\", r\"syn-\\s*,\\s*pref\", r\"CTUV,\\s*\", r\"together\\S*'\\s*\\.\\s*—\\s*Gk\", r\"σύν\"]:\n    ms=list(re.finditer(pat,t))\n    print(pat, len(ms))\n# find 'symposium' entry\nfor w in ['symposium','symbol,','symphony','same,  adj']:\n    i=t.find(w)\n    print('==',w,i)\n    if i>0: print(t[i-300:i+700].replace('\\n',' '))\nEOF",
 "description": "Klein symposium/symbol/symphony entries"
}
```


### [2026-09-14T01:59:02.533Z] TOOL RESULT

```
syn-,\s*pref 1
syn-\s*,\s*pref 1
CTUV,\s* 0
together\S*'\s*\.\s*—\s*Gk 0
σύν 0
== symposium 7499793
(pi.), OIr.  ibim,  ‘I  drink’,  OI.  plbati,  ‘drinks’,  L.  bibere (assimilated  fr.  *pibere),  ‘to  drink'.  See  bibulous and  -ion  and  cp.  poison,  which  is  a  doublet  of potion.  Cp.  also  potable,  potation,  Poterium, potomania,  potometer,  pawnee,  Pistia,  pour- boire,  propine,  symposium.  Cp.  also  the  second element  in  Hydropotes. Derivative:  potion,  tr.  v. potomania,  n.,  1)  dipsomania;  2)  delirium  tremens (tried, )  —  Medical  L.,  compounded  of  Gk. ttotop,  ‘a  drinking,  a  drinking  bout’,  and izavta,  ‘madness,  frenzy’.  See  prec.  word  and mania. potometer,  n.,  an  instrument  for  measuring  mois¬ ture  in  plants.  —  Compounded  of  Gk.  7iot6v, ‘a  drink’,  and  perpov,  ‘measure’.  See  potion  and meter,  ‘poetical  rhythm’. potpourri,  n.,  medley, miscellany.  —  F.,  lit.  ‘rotten pot'.  For  the  first  element  see  pot,  a  round  ves¬ sel’.  F.  pourri  is  the  pp.  of  pourrir,  ‘to  rot’,  fr. VL.  *putrire,  which  cor
== symbol, 915309
,  bolide,  bolometer,  boule, ‘council’,  catabolism,  devil,  diabolic,  discobolus, Eblis,  ecbolic,  Elaphebolion,  emblem,  embolism, emboly,  hyperbola,  hyperbole,  metabolism,  pa¬ rable,  parabola,  parlance,  parley,  parliament, parlor,  parol,  parole,  periblem,  problem,  scy- balum,  symbol,  Tribolium,  Tribulus. ballistics,  n.,  the  study  of  projectiles.  —  See  prec. word  and  -ics. ballonet,  n.,  an  auxiliary  gas  or  air  bag  in  a  bal¬ loon  or  airship.  —  F.  ballonnet,  lit.  ‘a  small balloon’,  fr.  ballon.  See  next  word  and  -et. balloon,  n.  —  F.  ballon,  fr.  It.  pallone,  which  is formed  with  augment,  suff.  -one  fr.  palla,  ‘a ball’,  a  word  of  Teut.  origin;  see  ball,  ‘a  round body’,  and  -oon.  The  b  in  F.  ballon  (fr.  It.  pal¬ lone)  is  due  to  the  influence  of  F.  bade,  ‘ball’. Cp.  pallone. Derivatives:  balloon,  tr.  and  intr.  v.,  and  the hybrid  noun  balloon-ist,  n. ballot,  n.  —  F.  ballotte, 
== symphony 2037861
,  conception.  For the  change  of  Latin  a  (in  capere )  to  »  (in  con¬ cipere)  see  abigeat  and  cp.  words  there  referred to. Derivatives:  conceiv-able,  adj.,  conceiv-abil-ity , n.,  conceiv-able-ness,  n.,  conceiv-abl-y,  adv. concent,  n.,  harmony  ( obsol .)  —  L.  concentus, ‘symphony,  harmony’,  fr.  concinere,  ‘to  sing together’,  fr.  con-  and  canere,  ‘to  sing’.  See  cant, ‘slang  of  beggars’  and  cp.  concert,  n.  For  the change  of  Latin  a  (in  canere)  to  e  (in  con-centus) see  accent  and  cp.  words  there  referred  to. concenter,  concentre,  v.,  to  concentrate.  —  F. concentrer,  fr.  con-  and  L.  centrum,  ‘center’.  See center  and  cp.  next  word, concentrate,  tr.  and  intr.  v.  —  Formed  with  suff. -ate  fr.  con-  and  L.  centrum.  See  prec.  word. Derivatives:  concentrat-ed,  adj.,  concentrat-ion, n.,  concentrat-ive,  adj.,  concentrat-ive-ness,  n., concentrat-or,  n. concentric,  concentrical,  adj.  —  ML.  co
== same,  adj 8417552
n.,  a  genus  of  plants,  the  elder  (bot.) - —  L.  sambucus,  ‘the  elder  tree’,  of  uncertain origin. sambuke,  n.,  a  triangular  stringed  instrument.  — L.  sambiica,  fr.  Gk  <Tap.puxv),  fr.  Aram,  sabb  - khd.  See  Noldeke  in  GOttingische  Gelehrte  An- zeigen,  1884,  p.  1022. same,  adj.,  pron.  and  adv.  —  ME.,  fr.  ON.  samr. ‘the  same’,  rel.  to  OE.  same,  adv.  (in  same  swa, ‘similarly’,  swa  same  swa,  ‘just  as’),  OS.  sama, samo,  OHG.  sama,  adj.  and  adv.,  Goth,  sama, adj.,  OHG.  samant,  MHG.  sament,  samt, ‘together’,  G.  samt,  ‘together  with’,  Goth. samana,  ‘together’,  OE.  samnian,  OS.  samnon, ON.  samna,  OFris.  samnia,  MLG.,  MDu. samenen,  OHG.  samanon,  MLG.,  MHG.  sa- melen,  G.  sammeln,  Du.  tamelen,  ‘to  collect’, lit.  ‘to  bring  together',  OE.  tosamne,  OS.  te- samne,  OFris.  tosamene,  Du.  tezamen,  OHG.  zi- samane,  MHG.  zesamene,  G.  zusammen, ‘together’,  fr.  I.-E.  base  *sem-,  *sm-,  ‘one, t
```


## [2026-09-14T01:59:03.086Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\n# p.1246 -> leaf ~ 1246/2+15 = 638\nfor i in (637,638,639):\n    print('==== leaf',i)\n    print(t[i][:1800])\nEOF",
 "description": "Mann IEC col 1246"
}
```


### [2026-09-14T01:59:04.494Z] TOOL RESULT

```
leaves 858
==== leaf 637
tched'; cf. Ukr. pa-skuda, s. ‘lecher’; Li. skaudüs, adj. ‘painful, offen- sive; man skauda “it aches’; skaudZiü, inf: skaüsti, v. ‘offend’; Latv. cf. skaudrs, adj. ‘keen, painful. (Variant of uncertain phono- logy in Srb. hud ‘bad’; Cz. chudý ‘poor’, dial: Jean’, and R xudój ‘bad; ill; lean’; xudà ‘blame, abuse’, fr. *ksaudh-, *qusoudh- or sim. Cf. Oss. cawd "bad fr. a variant *sKaudh-?) skaug- Sw. skóka, f. ‘whore’; Li. skaugüs, adj. *miser- ly’; skáugis, ‘miser’; Latv. skaugis, m. ‘envious person’ but cf. skaudigs ('envious'. See above) (skaul-, see ksaul-. Thus only in W ysgawl, adj. ‘vehement, dashing’) skaupos, å ‘tuft, bunch, sheaf Lat. (dial.) scopae, fpl. ‘broom’; scopo, are, v. (sweep. WH & EM untenable); (W cf. ysgaw, Br. skað, Cor. scaw.'elder? but the semantic link is obscure); MHG schoup, gs: schoubes, sm., Du. schoof, f., OE sceaf, m., ON skauf, n. ‘sheaf, bundle’; LG Schauw, wf. “flock, swarm’; cf. ON sküfr, m. ('tuft, topknot,, fr. *sküp- or *skübh-); Big. cf. (dial.) skupü, m. “collection, heap', sküpom ('to- gether, unless from a dialect of Srb. type, *su- and *komp-. Thus Mladenov. Isophonic: OCS pro-skupü *depraver, profaner’; -sku- pístvo 'depravity')
skat- — skedhros
10
20
25
30
35
40
45
1152
skauros (skhauros) ‘limping, club-footed'. WP II, 538 Skt. khorah, adj. (‘limping’, fr. *skh-); Gk. skaüros, adj. 'acromegalous'; Lat. scaurus, adj. *club-footed'. (For Sw. skör *overripe, squa- shy', see ksaur-)
(skauth-, possible variant of type skaudh-, q.v. for OPer. skauðis: Arm. xawt)
(skau-, skauu-, ksau- "watch, care’. (Variant sKou-? q.v.). See Supt:S)
skáuios “bent, twisted, left-hand’, etc. See skaiuos. The present variant arises in Alb. i huej, i huaj, adj. ‘strange, foreign’; t&-huej, v. ('alienate', fr. *at-skaujo); EMDu. schou- wen, v. ('avoid'
==== leaf 638
v But R ščegol = 'goldfish"); (ON skikka, v. “arrange, ordain' and skikkja, v. ‘cloak’ are, like G schick-, of ambig. vocalism)
skeibh- “slice, cut, division’. (Gmc. ambig. cf. skeip-) MHG schibe, wf. (2) ‘slice’; E dial. shive, shiv, id.; ON skífa, f. id. & vb. id. Du. schijf, f. id.; Li. skiébas, m. 'firebreak in a wood, clearway', skiebiü, skiébti, v. ‘slice’
skeid-, see skid-)
skeidh- (skeidhrà, skheidh-) ‘slice, cut; blade, cutter, incision". WP II, 543. Cf. ski- dhros, skidros, skh-, etc. Arm. cf. xe, s. lees of grapes’; W (?) ysgwydd, pl. -au, f. ‘shoulder’; Br. skoaz, f. id.; Cor. scoth, pl. scodhow, f. id.; OHG skit, OFris. skid, n, OE. scid, n. ‘slip of wood E shide *roof-shingle; MHG schiten, sv. 1. ‘chop, split’; scht, sn. as OE; cf. G Scheiter-haufen; ON skíð, n. ‘lintel, chip, ski, roof-shingle'; cf. (probably fr. *skidh-) ON skíði, n. ‘sheath’; Sw. skida, f. (2) “pod, shell in view of Li. skydas ‘shield, carapace’; Cz. cf. Stidla, f. ‘stilt’; Li. skiedà beside skiedrà, f. ‘chip’; Latv. cf. Skiedi, mpl. “teeth of weaver's sley’; Li. skíedziu, skíesti, v. ‘divide’; Latv. šķiežu, Skiest, v. ‘scatter, squander’
skeiið (skeið, skheiio, skheio) “divide, split, distinguish, choose’. Cf. WP II 542 Hitt. cf. skyami, 3s. skici, v. (anoint, lit. “dis-
skeg- (skheg-?) — skeko, ið
10
15
20
25
30
35
40
45
1154
tinguish'?); Lat. scio, scire, v. ‘ordain, ap- point; know, be skilled in’; Br. cf. skeZa, v. ‘cut’; cf. skiant, f. ‘mind’; W cf. ysgi, pl. sciod, m. “slice?
skeim- “separation, division’. Cf. skeiio, etc. W cf. ysgwyf, m. ‘shower; scum’; Blg. &Cim, m. *wool-combings'; Li. skiemuó, eps, m. (woof-threads;  shuttle-race; pl. -menys *healds?); Latv. cf. Skiemele, f. *shuttle-race'
(skeip-, cf. skip-, sKip- and skoip-. All the evidence is ambig.) Cf. MHG schibe, wf. 
==== leaf 639
 skélti, v. ‘split; Latv. Skelu, Skelt, id. (NB. There is some confusion in Gmc. between types *skel- and *skil-, q.v.). O-gde in Hitt. skalla(imi), v. (queried: ‘split, têar’). Nominal types: Arm. xelk, g: xelac, ab. xelawk, pl. ‘brain’; OE scelle & scielle, f. ‘cutting, separa- tion’; LG schel, f. ‘difference, separation, boundary’; R scel', f. ‘chink, slit’; Latv. cf. Skelte, id.; Sw. skål, n. “faculty of reason?
skel- (2) ‘dry, wither, decay, crumble’. Cf. WP II, 597 Gk. skéllo, aor: éskela, v. ‘wither, dry’; cf. skeletós *withered'; Li. skeliù, skelsti, v. ‘de- cay, crumble’; cf. Gk. -skelés (‘dry’ in cpds.)
skel- (3) “bent, twisted, wrong'. Variant skhel-, q. v. Arm. xey, i, av, adj. ‘crippled, lame); xeyem, v. ‘cripple’; Lat. scelus, gs: -eris, n. ‘crime’; OFris. skilla, v. ‘quarrel’; Fris. skeel (2) “de- fect, evil, setback, lack, blemish; dispute'; Li. skelià, éti, v. “be indebted'. (Isophone: Gk. skélos, gs: -eos, n. ‘leg, shin’. Lit. 'bend"?). Extension in OHG skélah, adj. (^squinting"; see FK:EWDS: schielen and cf. MHG schélch, gs: schélhes ‘crooked, awry, asquint’). Cf. WP II, 598
skel- (long-grade of type skel- (1), q.v.) “division, part; cut, separation; discernment’ Per. sikal 'thought'; sikalidan, inf. “think”; Arm. xil 'inquiry'; Alb. i hollë, adj. ‘thin, fine’; huall, pl. hoje, m. ‘honeycomb’ beside hoj, hoje, mf. id.; hoj&, f. ‘crag’; cf. té-huell, té-holl, v. (roll out thinly’ fr. *at-skelo); Br. Skil-, cpds. “partly-?; Fris. skiel, s. “peg, esp. one used in netmaking'; ON skáli, m. ‘hut, shed, room’; skál-hüs ‘privy’; Latv. šķēle, f. “slice”; Skeleju, v. id.; Li. cf. skelimas “cleavage”
skelb- (?). Cf. skolb-. Ir. ambig. skelbh-? Ir. scealb, f. ‘splinter’; Du. schelp, MDu. schel- pe, f. 'scallop-shell; (isophonic in OHG sciluf,
skel- — skendó, ið
1
```


## [2026-09-14T01:59:14.156Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8',errors='replace').read()\nm=re.search(r\"syn-,\\s*pref\",t)\nprint(t[m.start()-400:m.start()+1400].replace('\\n',' '))\nEOF\necho \"#### IEC 684\"\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (683,684,685):\n    print('==== leaf',i); print(t[i][:2200])\nEOF",
 "description": "Klein syn- and Mann col 1246"
}
```


### [2026-09-14T01:59:15.409Z] TOOL RESULT

```
omatic- al-ly,  adv. symptomatology,  n.,  the  study  of  symptoms.  — Medical  L.  symptomatologia,  compounded  of Gk.  aupjTTcopa,  gen.  auprcTcipaxo;,  ‘chance, occurrence’,  and  -Xoyta,  fr.  -Xdyos,  ‘one  who speaks  (in  a  certain  manner);  one  who  deals (with  a  certain  topic)’.  See  symptom  and  -logy. Derivatives:  symptomatolog-ic-al,  adj.,  symp- tomatolog-ic-al-ly,  adv. syn-,  pref.  meaning  ‘with,  together  with’.  —  Gk. auv ,  cuv  ‘with,  together  with’  (whence  cuvAc, ‘commun’);  of  uncertain  origin.  Cp.  sy-,  syl-, sym-,  sys-. synaeresis,  syneresis,  n.,  coalescence;  contraction of  two  vowels  into  one  syllable.  —  Gk.  auv- atpeais,  ‘a  grasping  together,  contraction’,  fr. auv  (see  syn-)  and  afpeat;,  ‘a  taking  for  one¬ self,  a  choice’.  See  heresy  and  cp.  aphaeresis, diaeresis. synagogal,  adj.  —  See  synagogue  and  adj.  suff. -al. synagogical,  adj.  —  See  synagogue  and  -ical. synagogue,  synagog,  n.  —  ME.  synagoge,  fr.  OF. sinagoge  (F.  synagogue),  fr.  Late  L.  synagoga,  fr. Gk.  auvavciiyir],  ‘assembly,  synagogue’,  lit.  ‘a bringing  together’,  fr.  ouvaystv,  ‘to  lead  or  bring together’,  which  is  formed  fr.  auv  (see  syn-)  and Syciv,  ‘to  lead’.  See  agent,  adj.,  and  cp.  agon¬ istic.  Gk.  auvaycoyr;  is  prop,  a  loan  translation of  Heb.  keneselh ,  ‘assembly’  (whence  beth  ke- neseth,  ‘synagogue’)  (lit.  ‘house  of  assembly’), fr.  kdnas,  ‘he  assembled'.  Cp.  Kneseth. synallagmatic,  adj.,  expressing  reciprocal  obliga¬ tions.  —  Gk.  auvaXXaypaxixo;,  fr.  auvaX- Xavpa,  gen.  auvaXXdyuxxo;,  ‘covenant,  con¬ tract’,  fr.  auv  (see  syn-)  and  SXXaypx,  ‘a  thing taken  in  exchange’,  from  the  stem  of  aXXaaaeiv, ‘to  exchange,  barter’
#### IEC 684
==== leaf 683
ry’; of a woman: ‘be married"); cf. pro-nuba ‘bridesmaid’; OCS snubljo, snubiti & snobljo, snobiti, v. ‘woo’; OPol. snebiC, v. (of woman: marry")
(snou-, snu-, see Supt: S)
snudos, is ‘fluid’. Cf. WP II, 693. (sneud-, snoud-) Av. (o-gde) snaoó-, v. “make flow'; (e-gde) Ir. snuadhaim, v. ‘flow’; (o-gde) Mir. snuad, s. ‘river’; (z-gde in) W nodd, pl. ion, s. *mois- ture, sap’; OE snot, n. ‘snot; OFris. snotta, wm. id.; Du. snot, s. id.; Icel. cf. (long z-gde) snýta sjer, v. “blow the nose'; OE snytan, v. id.; Li. snuda, mf. (2) 'sniveller
(snüið ‘turn’, see sneu-, neu-)
(snumbh-, see snubh-)
snüs- (snust-) ‘doze’ Gk. cf. nustázo, v. ‘nod, drowse'; E northern dial. to snooze (cf. N. Eng. to crooch = to crouch; to mooch = to mouch, etc.); Fris. cf. snüsterich, adj. *fusty, dusty’; Sw. Norw. snusa, snuse, v. ‘sniff
snoitos, is (snoitt-, snoist-, snoits-) — so, sã, tod
15
20
25
30
35
40
45
1238
snusos, å, io, us ‘daughter-in-law’. WP II, 701 Skt. snusà, id.; Oss. nostä, id.; Arm. nu, gs: nuo, nvo, o-st. id.; Gk. nuós, f. id.; Thrac. nüsà, id.; Lat. nurus, gs: -üs, f. id.; OHG snura, MHG snur and snuor, sf. *brother's wife’: OFris. snore, Fris. snoar, OE snoru, ON snor, id.; OCS snüxa, R snoxa, Srb. snaša, f. *daugther-in-law"
sngh-nu- ‘reach’. Cf. se&h- and WP II, 482 Skt. (ambig. vocalism) saghnómi, v. "be a match for’; Hitt. sanhami, v. “approach; test; attack'; imperative: sah!; OCS (and com. Sl.) segno, -noti, v. ‘reach’; OCz. sahu, 2s: sěžeš, inf. síci, v. id.
snguhó, ið ‘singe, scorch’. (Cf. WP II, 495) Hitt. sanhwami, sanhumi, v. ‘roast: Gk. hápto, v. (2) ‘kindle’; haphé, f. ‘ignition’; cf. áphthai, fpl. “mouth ulcers'; n-áphtha “crude oi (?); MHG cf. (o-gde) senge, f. ‘dryness’; sengen, v. ‘singe, burn’; OE sengan, wv. id.; cf. also G sangeln, v. ‘singe; tingle’; MHG sun- gen ‘be singed’
snt- (sntà, iə) ‘wrong, blame, evil, injury”. Cf. sont-, esnt-, etc. Cret. áta, f. ‘penalty’; Gk. áte, f. ‘mischief; cf. (o-gde) Lat. sons, gs: sontis, adj. ‘guilty’; MHG sünde, id.; OS sundia, OFris. sende, OE synn, f. ‘sin? (OE also ‘injury, feud, crime’); ON synd, pl. -ir, f. as OS
snter- ‘away, apart’. Cf. sm-tero-. WP II, 494. Skt. cf. sanutár ‘apart’; Gk. (Ion.) áter, id
==== leaf 684
et, fix, place’; OCS (and com. Sl.) saZdo, saditi, id.; OPr. cf. (short vowel) sadin-, v. ‘put
sodios, iom, io 'sitting, seat'. WP II, 489. Cf. séd-, etc. and ff. Skt. -sádyam, in upari-° “sitting above’; Gk. cf. á-ozos-, m. (“temple attendant, fr. *sm- sodios); MHG setze, sf. “placing; pledge’; n. Jaw’; OE set, n. ‘seat, camp, setting’; Olr. suide, Ir. suidhe, m. “sitting, seat?
sodos ‘way, manner, gait’. Cf. WP II, 486 Skt. cf. sádam, sádà, adv. ‘always’; Gk. hodós, f. “way, journey, method; cf. also (?) oüdas, gs: -eos, n. ‘ground, floor, paving? beside oüdos, m. (threshold; fr. (?) *soduo-); MHG saz beside saz, gs: satzes, sm. “measure, man- ner; G Satz, m. “sentence, movement in music’; Sw. sätt, n. “manner, way’; E cf. (?) sett, s. ‘cobblestone
sodos, à, io, us ‘settlement, setting, plan- tation, sediment, soot'. Cf. séd-, etc. Skt. (ambig.) sadáb, m. ‘sitting, posture, settle- ment, sediment; ruin'; OE sot, n., ON sót, n., Norw. sot, LG sott, n. ‘soot; OCS sadü, gs & loc. s. -u, m. “plant, tree, woodland’; R sad ‘orchard’; Cz. ‘park’; Pol. sadz, m. 'fish- crate, cran, cage' beside sadze, Cz. saze, fpl. ‘soot’; Lith. suodžiai, mpl. and suodys, gs: -dzio, m. id. WP II, 484
sogh- (soghos, à, iə) “hold, holder, handle’. (Skt. Gk. & Gmc. ambig. See sogh-, and cf.
so- — soib-
20
25
30
35
40
45
1240
segh-, segh-). WP II, 481 Arm. agi, gs: agvo, s. (tail, lit. "holder", cf. also agujc, gs: aguci, s. “holder, setting, clasp, joint, staple’ beside (?) b-ognim, v. ‘be tired”; MHG sacke, sagge, wm. (“common land”, lit. ‘holding’, but see sogh-); Slovak cf. o-soh m. ‘use’; Li. saga, f. “button, clasp, buckle’; sage, f. ‘brooch’. Ambig. are Skt. sahah, adj. “mighty”; sahyam, n. ‘help’, but prob. *sogh- in view of Av. hazaoSo, adj. (agreed', fr. *sogheusio-); cf. however soghuros below. Long-gde in OCS po-sagü, m. ‘fetter; marriage’; po-sag- noti, inf. join; marry’. Ambig. also in Myc. -oko-, cpds. ‘holder’; Gk. okheüs, m. “holder, clasp, thong, bar’; okhós, adj. ‘firm, secure?
soghuros (soghuros) ‘firm, stable’. WP II, 481. Cf. segh-, segh-; sogh-, sogh- Skt. (ambig.) sáhurih, adj. (mighty, victor- ious'; Arm. agur, adj. ‘hard’; Gk. (ambig.) okhurós, adj. ‘strong
soghl
==== leaf 685
soik-, cf. soiqu- and seik- (1), seiquo, siqu-. Ambig. in Skt. & Li.) MHG seihen, v. “strain, filter’; Skt. cf. sekah, m. 'outpour; libation'; sektram, n. ‘ladle’; Li. saikaü, ýti, v. and saikuoju, uoti, v. ‘bale out?
soik- (2) (?) “go, reach’. Evidence ambig. Variant: seik- in Skt. & Gk. Skt. cf. seke, mp. ‘go’; Gk. eko id.; Li. sáikau, yti, v. “try to reach"
soilos (soiolos) ‘cord’. Cf. seio. WP II, 464 Br. hual, pl. -u, m. ‘fetter’; pl. ‘chain’; W hual, pl. -au, m. as Br.; OHG seil, sn. ‘rope’; OE sal, mf. id.; Du. zeel, n. “strap; traces; girth- belt; LG seel, n. “handle of pail’; ON seil, f. “string, line'; Li. sailas, m. “rope, string, bond, tether `
soin- (soinos) (1) ‘slow, lingering’. WP II, 462 Go. sainjan, v. “linger”; MHG seine, adj. *slug- gish’; OE sa&ne, id.; ON seinn, id.; seina, v. ‘delay’; Sw. sen, adj. ‘late’; Li. cf. at-sainus, adj. "lazy, negligent; (z-gde in) Lat. sino, ére, pf: sivi, sup. situm, v. “allow?
soin- (soinos, om, ios, à) (2) *mass, bulk? Skt. sénam, n. “body, bulk’; séna, f. (2) *mass- ed army, hosť’; Av. haena, f. “army, host, esp. of demons"; Per. (Pahlevi) haina ‘army’; Lat. sinus, gs -üs, m. & sinum, n. *big-bellied jar’; Latv. sainis, s. ‘bundle’
soin- (3) “wall, compartment OCS séni, fpl. ‘vestibule’; Cz. síň, f. ‘room, hall’; Li. síena, f. ‘wall, boundary’; Latv. siena, f. ‘wal?’
soiquos ‘container, vessel, bucket’. Cf. siqu- (singu-), seiquð. WP II, 465. (Balt. ambig. cf. seiquos, and cf. seik-, soik-) OE så, m. *tub'; Sw. så, m. id.; ON sár, gs: sás, npl. sáir, m. ‘cask’; Blg. sék, m. (1) ‘tank- ard'; Li. saikas and (ambig.) siekas, m. (a
soidh- — sól- (solos, om, iom, à, io, is, us; sol-)
10
20
25
30
35
40
45
1242
capacity measure); Latv. sieks, id.
soit- (soitor-) (1) Av. hae00, adj. awful; Olr. saíth, saíthar, n. “trouble, sorrow’; Ir. saothar, m. ‘toil’; Br. hüdür, adj. (‘dirty’. (?) false h-)
soit- (soitio) (2) ‘fetter, fascinate, bewitch’. Cf. WP II, 509 W (denom.) hudo, inf. ‘bewitch’; ON seiða, v. id.; OCS sěštọ, sétiti, v. “net cf. sétiti sę, v. ‘recall, mention’; Blg. sěščam, v. ‘sense’; séten, adj. ‘clever’; Li. saičiuų, saisti, v. “fore- tell; Latv. cf. saistīt, inf. ‘fetter’. See next
soitos, à, is, us, iə
```


## [2026-09-14T01:59:25.310Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (686,687):\n    print('==== leaf',i); print(t[i][:2500])\nEOF",
 "description": "Mann leaves 686-687"
}
```


### [2026-09-14T01:59:26.439Z] TOOL RESULT

```
==== leaf 686
so = “bench, quarter-deck"); Lat. solum, n. ‘soil, ground, bottom, sole of foot; solium, n. “seat, throne: solea, f. ‘sole of foot’; cf. also solidus, adj. (/solid, full, entire’. Not as WH); OHG sala, f.; OE sæl, pl. salu, n. ‘hall’; sele, m. id. (and 'dwelling); ON salr, npl. salir, m. “room, floor, ball" beside sel, pl. -ja, n. ‘hut’; OS seli, Let. m. “room, house” beside selida, f. ‘dwelling’; Go. salipwa, f. id. (Lë *hostelry^); OE sælp, f. ‘dwelling’; (the source of OCS selitva *hostelry' and its vocalism un- explained); Blg. (*-0-) sal, pl. -ove, m. ‘raft; Li. salà, f. (2) “village”; cf. át-sala, f. *mud- fla? beside (*-0-) sáolas, m. ‘bench’; Latv. sols, m. id.; solis, s. ‘footstep’. (ON soit, m. ‘sole of shoe’ may be a LW)
soleið (1) “be, dwell’. Cf. sól- above EMAIb. cf. gjell, v. ‘live’; Lat. soleo, ere, v. ‘be wont; cohabit with’; Go. saljan, wv. (1) ‘be, dwell’. (Sw. sóla, v. ‘stay, tarry? seems to derive from a type *suel-)
soleið (2) “offer, yield, bid, afford, sell Go. saljan, v. (2) “offer, sacrifice; MHG sel- len, seln, v. ‘sell; OE sellan, v. “offer, give, supply, lend, promise, sell; ON selja, v. *yield, hand over, sel; Sw. sälja, v. ‘sell; till salu “for sale”; salu, cpds. sale-, id.; cf. ON sala, f. id.; OCS pra-soljo, -soliti, v. "sell": pra-solü, m. ‘vendor’; Latv. (long grade) solu, inf: solit, v. “bid, promise). (The source of Lat. solor, ari, v. ‘comfort, cheer, satisfy’ is uncer- tain, perhaps fr. *suel-)
solkos ‘drag, hook; trail, furrow, track’. (E- gde, of uncertain provenience, in Gk. hélko, fut: helküso ‘drag’, etc. See uelk-, uelqu-) Gk. holkós, m. 'drag, hauling implement; furrow, track’; adj. (attractive? cf. holké, f. ‘dragging’; holkaios, adj. ‘drawn’; Myc. (Py- los) cf. (queried) ksu-keiatewe oka diptera (= *xu-keiatees holkaies diphthérés 'scraper- splitters of stripped leather"); Lat. sulcus, i, m. ‘furrow’; Slovak slak, m. ‘mortise, fence’; slák, m. “violin-bow?
soluos, ios “whole, all, entire, sound, hale’. Cf. sluos St. sárvah, adj. ‘whole’; Av. haurvo, id.; Ober,
soleið — soməlos
10
20
23
30
35
40
45
1244
haruva-, id.; Per. har, adj. & pron. “all”; Tokh. A salu ‘whole’; cf. B solme, adv. ‘wholly’; Arm. OYvÉ£, o-st. ('alive, well, sound, whole’. fr. *solujo-); Alb. i gjallë, adj. ‘alive’; Gk. hólos, oülos, adj. ^whole, sound, entire', cf. a-ollés, adj. ('compact', fr. *sm-solu- ?); Osc. sullus, adj. «all; Lat. cf. soll-emnis & -ennis ‘annual’, soll-ers, -ertis ‘clever’; Ir. soilbh, adj. ‘pleasant’; MHG cf. sal, a
==== leaf 687
ras, -dara: -eimi in Skt. & (variant) Latv. cf. sa-eju; sa-eima, f.; -dhos, -dha in Skt. Slav & Balt.
somolos “together, equal, even, like'. Cf. som- (1), sem- & sm- Skt. samaráh, m. ‘concourse, battle’; Per. hamal, adj. “equal, like’; Arm. amol, s. *coun-
1245
terpart, fellow; amolk, gp: amloc, pl. type *pair, yoke? (fr. *somilo-); Gk. homalós, adj. “level, even’; Umb. cf. sumel, adv. ‘at the same time?
som-. Cpds. ctd. -guer-, -guor- ‘drinking or eating together? in Skt. Arm. (anker) & Latv.; -fen-, -ogen- in Skt. Per. Arm. & Ok: also (z-gde: -gn- in) Skt. Gk., Go. & ON; -niə ‘conscience, know- ledge’ in Skt. OBr. ON, Li. & R; -it- in Skt., W (hefyd ‘also’); -10 in Skt., Go., ON, Sw.; -jug-, -jung- in Skt., Li, Latv.; -logh- in Gk. (á- lokhos, f. ‘wife’, ON, OCS and com. S81. -mān- in Skt., Li., Latv.
somn- (somen-, somnd-) “together, alto- gether, all. WP I, 123 & II, 489 Skt. samanā, adv. ‘together, at once’; f. *to- tality’; Per. hama, hamad, pn. "all": hamàn, hamin, adj. ‘the same; the only’; Arm. amen, amen, ab. s. amena ‘all’; hamajn, adj. “whole, entire’; hama-, cpds. "co": Lat. omnis, adj. Cal" by ‘false’ division, qua *orbis-somnis > orbis omnis); Gk. cf. homás, gs: homádos, f. (the whole’: Per. hamad: OHG samant, sa- ment, fr. *somnd-); Go. samana ‘together’; OHG saman "all at once’; gi-samani, n. ‘troop’; MHG samen(e), OE samen & to-somne, ON saman ‘together’; Sw. (den) samme, f: — sam- ma, n. (det) samma ‘the same’; Hitt. cf. sam- na(mi), and samniya(mi), v. (‘put together’ or sim.)
sõmn-, variant of type sóm-, see somos be- low. WP II, 491 Skt. saman, n. ‘gentleness; conciliation’; Olr. cf. sám, s. ‘ease’; adj. ‘relaxed’; OHG suona, f. ‘conciliation’; MHG suon, suone, mf. *judg- ment; peace, rest’; süene, adj. ‘peacemaking’; OFris. sone, as OHG; Du. zoen, m. as OHG (also: "Masi: ON sónar-, cpds. ‘sacrificial’. (Slavonic sanü, m. ‘worthiness, rank’, sanită, adj. “holy” is entirely ambig. Cf. Kånos (2) and sānos, esános)
somnd-, cf. somn- above Skt. (ambig.) samád, f. ‘battle’; Per. samäd “all, whole’; Arm. ənd, prp. ‘with’; Gk. hóma- dos, m. ‘crowd’; OHG samant, sament, MHG sament, samet, adv. ‘altogether’; OS cf. sa- mad, id.
som- — sonĝuhos
20
25
30
35
40
45
1246
somos ‘together, like, equal, one, some, the same’. WP II, 490. Cf. som-, sem- and sm- Skt. samáh, adj. ‘even, level, like, equal; Av. hamo, id. (and “whole'); Ober hama- ‘the same’; Tokh. A sam, B sàme ‘together’; Hitt. cf. sanas ‘one’; Gk. homós, adj. “like, equal; homo-, cpds.;
```


## [2026-09-14T01:59:27.142Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"\\[pdf page\" BQT_v1_pages.txt | head -5\necho \"---\"\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=re.split(r'\\[pdf page (\\d+)\\]',t)\nprint(len(pages))\nEOF",
 "description": "Inspect BQT v1 pages file"
}
```


### [2026-09-14T01:59:28.314Z] TOOL RESULT

```
---
1
```


## [2026-09-14T01:59:34.258Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v1_pages.txt BQT_v1.txt BQT_alt_v1.txt; do echo \"== $f\"; python3 -c \"\nt=open('$f',encoding='utf-8',errors='replace').read()\nprint('len',len(t),'ff',t.count(chr(12)))\nprint(repr(t[:300]))\n\"; done",
 "description": "Inspect BQT v1 files"
}
```


### [2026-09-14T01:59:35.487Z] TOOL RESULT

```
== BQT_v1_pages.txt
len 1285412 ff 776
'\x0c۱ ۵ ۱! ۱\n7 موم ۳ لام\nم ۱ 0 و طق صفرررنیاعدریرماروی\n۰ ۱ "۳\n۳\nم و اس مر هر وه او\n7 رین خلت ریز یتایب بره ات\nلف\u200cبال ۶۲ .یرک\nا اند کل داي رشب , رمع\nفان تا تا\nرن 9 3\nکرحم تن\nاد شش مرا\nمو رم | مر\nوک رهب اه نات مج\nلش\nوان روکد ور\n۱ و\nطراول ؛ | ع اس\nچاپ دوم فروردین ۱۳۴۳\nبا تجدید نظر کامل\nبسرمایه کنابفروشی ا'
== BQT_v1.txt
len 1531945 ff 0
'\n\n\n۱ ۵ ۱! ۱ \n\n\n7 موم ۳ لام \nم ۱ 0 و طق صفرررنیاعدریرماروی \n۰ ۱ "۳ \n\n\n۳ \n\n\nم و اس مر هر وه او \n7 رین خلت ریز یتایب بره ات \nلف\u200cبال ۶۲ .یرک \n\nا اند کل داي رشب , رمع \n\n\nفان تا تا \nرن 9 3 \nکرحم تن \nاد شش مرا \n\n\nمو رم | مر \nوک رهب اه نات مج \nلش \nوان روکد ور \n۱ و \nطراول ؛ | ع اس \n\n\nچاپ دوم فروردین ۱۳۴۳ \nبا'
== BQT_alt_v1.txt
len 1536166 ff 0
'۱( او ۰۱۱۱ زب ۱ \n\n\n۸ ۲ ۲ ۱۵ \n۲ هه ی ۳ فاد \nم / ۱ ۳ ۱ و م2 مسترورتیاددی\u200cباروی) \n۳ كت \u200cٍ\u200c \n\n\nو مس ۳ > \n\n\n2 رضینن ییازان \nملف\u200cبال ۶۲ ۰ یرک ۱ \nاب ند خی دپ رتم . ور \n\n\nرصان ۰ ور شوه دازون خات ستاو \nو مه 0۷ \nسس ره \nتا مر \nمرهج ام زود نات مرک \nساوان و1 مش \nب ۸ \nعل ۱ ول و | ح سس \nچاپ دوم فروردین ۱۳۴۲ \n\n\nبا '
```


## [2026-09-14T01:59:38.576Z] TOOL CALL #28: Bash

```json
{
 "command": "timeout 300 python3 tools/ref_page.py BQT:166 2>&1 | head -60",
 "description": "Fetch BQT page 166"
}
```


### [2026-09-14T01:59:39.705Z] TOOL RESULT

```
no scan of BQT covers printed page 166 (see 'scans' in refs_online.json)
```


## [2026-09-14T01:59:44.414Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('data/verification/sources/refs_online.json'));b=d['BQT']\nprint(b.get('page_offset'));print(b.get('lookup_hint'));print(b.get('scans'))\"",
 "description": "BQT page offset info"
}
```


### [2026-09-14T01:59:45.537Z] TOOL RESULT

```
vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').
grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned volume use: python3 tools/ref_page.py BQT:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)
[{'volume': '3', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', 'first_printed': 1208, 'last_printed': 1925, 'pdf_offset': -1205, 'page_map': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pagemap.json', 'lang': 'fas', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', 'ocr_note': '689/721 pdf pages OCRed (tesseract fas+eng, mediocre); pages are separated by form-feeds and tagged [pdf page N]; remaining pages via tools/ref_page.py'}, {'volume': '4', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', 'first_printed': 1920, 'last_printed': 2475, 'pdf_offset': -1917, 'lang': 'fas', 'offset_note': 'printed = pdf+1917, checked at pdf 150 and 500', 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt'}, {'volume': '5', 'file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', 'first_printed': 1, 'last_printed': 290, 'pdf_offset': 5, 'lang': 'fas', 'note': "vol 5 = ta'liqat (addenda) with its own pagination 1-290; cite as BQT5:<page>. Plain BQT:<n> with n<1208 refers to vols 1-2 (OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt), not to this scan.", 'ocr_text': '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', 'requires_volume': True}]
```


## [2026-09-14T01:59:55.583Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,p in enumerate(t):\n    if 'انجمن' in p or 'اندوه' in p:\n        print(i, [w for w in ('انجمن','اندوه','انجام','انگیختن') if w in p])\nEOF",
 "description": "Find anjoman/andoh in BQT v1"
}
```


### [2026-09-14T01:59:56.831Z] TOOL RESULT

```
60 ['انجمن']
61 ['انجمن']
66 ['انجمن']
81 ['انجمن']
90 ['انجمن']
104 ['انجمن']
124 ['انجمن']
144 ['انجمن']
149 ['انجمن']
152 ['انجمن']
169 ['انجمن']
171 ['انجمن']
246 ['اندوه']
316 ['انجمن', 'انگیختن']
379 ['اندوه']
385 ['انجمن']
389 ['اندوه']
392 ['انجمن']
434 ['اندوه']
511 ['اندوه']
576 ['اندوه']
596 ['اندوه']
624 ['اندوه']
666 ['انجمن']
676 ['اندوه']
685 ['اندوه']
687 ['اندوه']
688 ['اندوه']
689 ['اندوه']
693 ['انجمن']
720 ['اندوه']
729 ['اندوه']
738 ['اندوه']
749 ['اندوه']
```


## [2026-09-14T02:00:01.247Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (384,385,386,389,390):\n    print('==== leaf',i)\n    print(t[i][:2200])\n    print()\nEOF",
 "description": "Print BQT v1 leaves 384-390"
}
```


### [2026-09-14T02:00:02.561Z] TOOL RESULT

```
==== leaf 384
انج - بفتح اول وسکون ثانی و جیم»
اطراف 2 روی و رخار ( ۱ ) باشد -
«بمعنی بیرون رفتن وبیرون کشیدن‌هم آمدم‌است
- وامر بان معنی هم حست بمنی بیرون بکش .
انحام ۱
و آخر هرکار و هوچیز باشد ه بنظام آیشوهاعل
رانیز گویند که‌بنهایت رساننده و با خرآورنده(۲)
و شهات برسان .
اتحباد ه با بای ابجد . ععرب انگبار
نت آی نت یاعد سم نگ وتو
پواسیر دانافم است .
نالك و خای نقطه‌دار ساکن ۰ بمعنی چین وشکن
ری و اندام و غیره باشد .
) نجحت باجیم فارسی بروزن‌بدبخت»
انش ‌ باجیم؛ بر وز ند حعنی ب رجستن
باشد .
| نجخیدن « بنثاك‌بروزن‌ب رگزیدن,
درهم کشیده شدن پوست روی و اندام باشد -
انحشان » منم ناك بروزن مردمان ؛
)۱ ساره
0
اصل‌آلانجدان خوانند ۴ ؛وبعضی گویند تسنای‌است
و آن جانوری باشد. شببه بآدمی .
انجر لك - بکس ثاك وفتح رای فرخت
وسکون کاف » نام دشتی‌و صحرادیست غیرمعلوم-
و مرزنگوش را نیز گوبند و آن نومی آزرباحین
است که در دوا ها بکاد برند و درعریی ! ذان‌الفار
کویند ۴ .
اتجره - بروزن پنجره ؛ نباتی است که
آنرا بعربی بنات النار گویند بقتح بای ابجد ؛ و
نخم آن را قرض‌خوانند وتخم آن مستعمل‌است.
سه‌درم آنرا با شیر نازه بشورند قوت باه دهد
و بکوبند وبا عصل برقضیب مالند سطب کرداند .
)نج ۴ - بنتح اول و سکون ثٌانی
وکسر جیم و سین بی‌نقطة بالف کشده ؛ بمعنئی
ابوخلسا ۴ است که نوعی ازسرخ مردیاشد و آنرا
عربی شجرءالدم گویند , خون شکم را ببندد .
انح - با خن نقطهدار » بروزن و ععنی
انجخ ۱ سا که جچن و شکنج روی واندام عاشد .
انحکك - باکاف مروزن‌مردمك ءدانه‌ای
باشد سیله شبیه یداه امرود و مفز فد دارد
وآنرا بخورند . خاصتشآاست که هرچند فراش
خبال جاروب سنبل ی تا
بوست آن باه نون
۴ - ۹6۱66۱ «لك۱ سی۱۹۷*.
انحرك « لك ۱ مس ۱۱۲ > .
۶ ملای ۲:۲۷ *.
است توجهی نکر دها ند)

==== leaf 385
- بو -
) فحل س بفتم اول وکسر ثالث و سکون
نانی ولام» رسثنی باشد که آیرا خطمی خوانند ۳
عالمتاب است .
انجمن! - ینم اك و قح میم وسکون
نون ۰ مجلس و مجمم را کویشد - بمعنیکروه
انحوج - بروزن محلوح , چوب عود
باشد ؛ و بهترین وی‌آن تکهدر ته آب‌شیند .
کونند عود یخ درختی است که آنرا میکنند
و در زیر خاكث دفن میکنند تا مدنی همین بعداز
آن برمیآورند » پوسیدة آنرا میتراشند و بافی
عود خالص می‌ماند . بهترین آن مندلی باشد .
افحوخ - بررزن مطبوخ . چن‌وشکن
روی و اندام باشد از عابت چیری دا سبسد: ۳
و بژمرده شدن میوه را نیز گفته اند - و بمعنی
آب ده ن که آنرا ت فکویند هم امذه است .
| نج و یادن - بروزن سر پوشیدن .
برهم ش کشیدن بوست روی و اندام وا گومند .
افحوسا؟ » باسن بی‌شقطه بالف کشیده.
بحنی انجسا است که نوعی از سرخ مرد باشد
و بعربی شجرةالدم خوانند » خون را بندد .
انحوع - با عن نقطه دار , بر وزن
وهعنی انجوخ اس که چن و شکن روی واندام
باشد - و آب دهن را نیز گونند .
| نجوغیدان - بروزن‌ومعنی اجوخیدن
است که برهم کشیده شدن پوست روواندام‌باشد .
انجیره
| نحو لد مس بر وزن مفلوك » نام دشتی
و بیابانی‌است نامملوم؟ .
) نجیدن ؟ - بروزن رنجیدن , بمعنی
استره زدن باشد بعنی حجامت کردن - و بمعنی
دیزه ریزه کردن هم گفته‌اند - و بیرون کشیدن‌را
پیز گوبند - و بمعنی زين آب دادن هم بنظر
آ مایت :
انجیفه ه بروژ نگندیده , بلغفت‌بونانی
کندنای کوهی باشد که‌بمربی حشیشةالکلب‌خوااند
و صوف‌الارض نب زکویند - و دشوار زابیدن زنان
را سودمند بود - و بفارسی بمعثی دبزه‌ریزه کرده
شده باشد .
انحیر بر وزن
زنجیس ۰ میوه است
معروف -ومطلق‌سوراخ
را کویندعموماسوسوراخ
کون,! خصوصا - ونام
جوی ات درهرات
و آنرا جوی‌انجیل بلام
هم میگویند .
انجیر ۸3 ه ناممیوءاست درهندوستان
) نحیر دن « بنتح‌اول ودال ابجدیروزن
شمشیر زن» بمعنی سوراخ کردن باشد, چه‌انجیر
بممتی سوراخ است .
انجیره * بروزنزتجیره ۰ بمعنی‌آنجیر
۲ ۰ و ره : دائرمالمعارف اسلام .
9 افجرك .
بمعنی پاشیدن , جممعا : از هم پاشیدن .

==== leaf 386
انجین
از توابم بزد - و ناوچهٌ مقمد و سوراخ کون را
نیز گویند ٩‏ . #
| نجین۲ بروزن‌دنگین» بمعنی ریز مر بزه
باشد و ربزه کننده را نیز گویشد - و امر باین
ممنی هم هست عئی ریزه و
کاهگل مالنده عم بنظر آمده است
| نحخطینا - بنتح اود و 1
و حای بی‌نقطةٌ مفتوح بفای زده و طای حطی به
تحتانی رسیده و نون بالف کشیده ۰ بلفت‌سربانی
نوحی از گل انار است , و گویشد درخت آن یر
از کل ثمری دیگری ندارد » ریش روده و رش
های کهنه را نافع است . و آنرا بشیرازی گل
صد. بر کت خوانند .
فك - بروزنومعنی چند وبععنی چندان
و چندین باشد - و شسار مجهول هم.عست از
و اصل السوی بیخیدرخت‌انداست - و مخ نکفئن
مك و کمان باشد که آبا چناست با چتن -
وسخن کفتن از روی تعجب‌را لیز گونند. وبمعنی
شکر وشک رگذاری رت و امد و امیدواری م‌
مت ۵ .
ا فك - بروزن‌عمدا؛بممن ی کلابهوکاهگل
بر بام و دیوار مالیدن باشد - وکاهگل مالندرا
را نیز گفته‌اند - وبمعنی غیبت وخبث وبد کوبی
هم هست - و خوابی‌را نیز گونن دکه صلحاوانقیا
ستند و روبای صادقه همانست - ودر عر می‌ممحنی
شبنم باشد .
فداچه ۷ - بروندراچه . بل‌زن
و :ازند (۱) قکر و اندشه را گوند . *
افداد - بنتح او بر وزن اقار ",
وبیتی آویند موازی وشد قح تیه ا داد س » بکر را و سکون سین بی
برش انیت 0۳ و عذرا چشم رسول را بانگش تکند .
(۱) چك : ژند وباژند
۱ رك : انجیر . ۴ -رك : انجبدن. ۴ - پهلوی ۵۳۵( بسیار, عدد مبهم ) «اونوالا
8 +مناس۲۷۹» ازابرانی
۴ شکر کزاری. ۵ تیزضیر
۹ رك: انداژه ۰
منتهیآلارب ه
از: فا6 بمعنی خوب + 22861161۳ ,
: انجیل متی , انجیل‌مرقس . انجیل لوفا
( برهان قاطع ۴۳ )

==== leaf 389
اف
او رفتی . بکشب بای شد و آتش را بکشت
راندروی درمیان دربا کم کردید ..
سین می‌نقطه , نام یکی از حکمای بونان است
گوند درطبابت اعجاز مکاربردی ۴
نلم مکی از مبلوزان تورانیی است ۳
دوازده د بردست گر کین ملاد کشنه شد" شلد ,
| ند ۴ بسکون کاف , تسضر اند
است , واند عددی باشد مجهول میان سه و نه
و انرا بعربی بضم خوانند - وهرچیز کم را نیز
نس ,۰
ند گان بروزن بند گان ۰ نلم‌شهری
۳ است مایین سمرقند و چین ء معرب آن
اند دی نم‌اول وثالثولام ۳
نانی وسین م‌نقطه » نام شهرست درحدود حغرب
- ونام جزیره‌ای هم هست‌در بالای کوهی ؛ وبهر
دوممنی فتح اول و ثالث ورابع هم امده است
! ند مه ‌ بروزن صردهه: » باد آوردن
غمپای گذخنه باشد .
که درمقایل بیرون است
ی
خبون وبرادر اراس
«مناس۹ ۲۷ .راد: ۳
اند
کرداند . آنرا بعربی قوباکویشد .
افو ج -بروزن محلوج» بمعنی‌اندوب
است وآن جوششی است با خارش که عرب قوبا
شف
] ند و خقی* - بروزن‌افروختن» بمعنی
جمم کردن وفراهم آوردن باشد - بمعئی قرض
و ایس دادن ‌‌ زد ابیت
اند‌و.- وزن مقصود ۰ کاهمگل
) ندودن۱ - بروزن‌فرمودن . کاهگل
و کلابه مالیدن باشد - ومطلا وملمع کردن دا
نیز کوید .
ا فك و ۷ - بروزن سردوز؛ بمعنی‌فراهم
آورده وجمم کرده شده باشد - وامر باین حمنی
همست عنی جمع کن وفراه آور .
اندول بروزن ممقول ۰ کلیمی باشد
کهآنرا برچهارچوب بامیخها سکم کنندوبجهت
استراحت برآن نشینند . و این در ملك زنگبار
مصمول است »
| ندو ف » بنتح رابع وسکون نون‌ودال
ابجد » از انباع است بمعنی تار وعار که زبروزس
شده رازهم باشدم باشد .
آف‌وه٩‏ - بروزن انبوه , گرشکی ول
ودلگیربرا اگوبند ف
| زد و۸ چم ثالث » مخفف اندوه است
» و اوزن ۳6000۲ ومادر ۸5۷۵۵
۴ - نیز اندیرما, در اوستا
۴ پهلوی 12702۷ (کم »کمی)
فعه در صفحة ۱۷

==== leaf 390
انسجان
که کرفتگی دل ودلگیری باشد .
اندهان بروزن مردمان ؛ جمم انده
باشد چنانکه جانور را جانوران ومردمرا عردمان
کویند . واین جمم بخلاف‌قیای است چه‌بنیراز
جاتور را بالف ونون جمع وان کرد .
نده‌قو و » بت دوقاف و سکون دو
واو ؛ دوایی‌است که آنرا حندقوفی‌خوانشد * کلف
را نافع است ,
انفی ‏ بر وزن لندی » بمعنی خاسه
باشد که درعقابل خرجی‌است - وبمعنی‌امیدواری
هم آمده است - وبجای لفظ بودکه.و باشد که
هم استعمال میکنند - وبمعنی‌آن لحظه هم‌هت
" وبمعنی تیزهم آمد» است که بعربی‌ایضا خوانند .
اند یدن عه بر وزن خندیدن . سمحنی
تعجب کردن باشد - و سخنی را ليز گونند که
از رویه خك وزرب تک کته شود .
اند یشه - بر وژن هم پیشه » بممنی
فکروخیال باشد - و بمعنی فری ویم هم آمده
است .
) ند باث بروزن نزديك , لفظی است
از کلمات تمنی که در غربی لیت و لعل وعسی
۱ -رك : اندوب واندوج .
بقیه ازصفحةٌ ۱۷۱
(9
کویند بعنی باشدکه و بود که و بابد که -
وبمعنی زبرا, که و از برای آن واز ابنجهت‌هم
گفته‌اند .
) نفد و ه با ذال قطه دار و رای‌بی شطه
پروژن لبلبو » پا زهر باشد و انرا فاد زهر نیز
کوبند , وبجای زال نقطه دار زای هوزهم آمده
اشنت: ۵
افر » بفتح اول وانی‌وسکونرای‌فرشت»
هرچیززشت وید را کوشد .
اثر وب بر وزن منکوب » جوششی
است با خارش که بمربی فوبا خوانند و بعضی
گونند جوهدی است که آنرا شارسی گر
و بتازی جرب خوانند , و با زای نتطه دار حم
کنته اند ۱ .
انز دو - شم اول و زای هوز و رای
فرشت بواو رسیده » سحنی بازهر است وفاد زهر
نی گونشه .
افز دوت »بر وزن و معنی عنزروت
است» وآن صمفی باشد نلخ که بیشتر درمرهمها
بکاربرند؟ وعتزروت معرب آنست » و در مود
الغضلا باین ععتی با ذال نقطه‌دار و بای آیجد ‌‌
آمده است که انذروب باشد .
۷ ره : اندوختن.
. درونی؛ داخلی . باطنی‎ > ٩
* بارتولمه ۹۸۸ * تیب ک۱۰۰۵ که
```


## [2026-09-14T02:00:33.431Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'اندرز' in p and 380<i<400: print(i,'اندرز')\n    if 'هنگام' in p and 380<i<400: print(i,'هنگام')\nEOF\necho \"=== v4 2368 -> pdf 451\"\ngrep -n \"\\[pdf page 45[0-3]\\]\" incoming/BQT/BQT_v4_pages.txt | head",
 "description": "Find andarz in BQT and locate v4 page"
}
```


## [2026-09-14T02:00:34.563Z] TOOL CALL #33: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'));b=d['MON']\nprint(json.dumps(b,ensure_ascii=False,indent=1))\"",
 "description": "MON reference details"
}
```


### [2026-09-14T02:00:34.594Z] TOOL RESULT

```
388 اندرز
394 هنگام
=== v4 2368 -> pdf 451
18267:[pdf page 450]
18306:[pdf page 451]
18358:[pdf page 452]
18395:[pdf page 453]
```


### [2026-09-14T02:00:35.708Z] TOOL RESULT

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
```


## [2026-09-14T02:00:45.597Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18306,18358p' incoming/BQT/BQT_v4_pages.txt",
 "description": "BQT vol4 pdf page 451 (printed 2368)"
}
```


### [2026-09-14T02:00:45.650Z] TOOL RESULT

```
[pdf page 451]
همشوند تس هخا
عالمتاب است چه با عیسی علیه اللام درايك | دارند- وبمعنی موافق* ومتابع وهمرازهم‌هست-
آشمان‌اند۹ #۰ : ویمعنی راضی وشاکر وخرسند۹ - وراضی شدن
همخوند بفتح اول وخای نقطه‌دار | و شاکر بودن و خرسند کزدیدن هم بنظن آهده
وواو معدوله پروزن همچند » مخفف هم‌خداوند است۷ .
است‌وآفراخواجه تاش‌هم میگوبندینی دوشخص همداستانی۸ - بانای قرشت بروزن
که يك صاحب و يك خداوند داشته باشند ؟ - | عرش‌آشیانی » زریرا کوبند که از رعایا در وجه
ویممنی شطهةٌ مقابل ونفیض وشد هم بنظن آمده | خراج ومال وجهات میگیرند و بمبی مال‌الرضا
است۴ . خوانند واین درزمان انوشیروان پیداغد وقبل‌از
همداستان؟ - دوک را کوبند که آن قوت لایموتی برعایا میدادند و آاچه س
پهوسته‌با هم مخ نکنند وحکایت بگوبندوصحبت | رسانیده بودند از ایغان میگرفتند.۹ ##

۹ - صحیح : دريك آسماست. ر4: همایةٌ مسیح. ۲ - ر4 : خوند ,

۴ - رشیدی بهمین‌ممنی آورده است. .۴ - از: هم (پیشوند اغترا4) ۳ داستان(۸.م ).

- نخون پد رکشت همداستات ز دانا غنیدستم این داستان .

فردوسی طوسی «فرهنکه نظام» .

۹ - «همداستان خرسند باشد.» «سحاح الفرس لسغ طاعتی» -

۷ - باین معنی همداستانی است. ر4 :۸ ۸ - از : همداستان (۸.م.) 1
ی (خاصل مصدر » اسم معنی) ؛ موافقت :

پندی و همداستانی کنی که جان داری و جالستان ی کتی.

فردوسی طوسی (کشته شدن آبرج بدمت برادران) «شاهنامة بخ ج ۹*۱

۹ -« درتاریخ طبری آورده که نوشیروان همةٌ رعیت را گرد کرده همةٌ زمین‌هارامساحت
نموده » بهمداستانی- که آنرا هرسال سه بار وبا چهار پاربدهند خراج قرارداد » ولهذا آن‌خراج
را همداستانی بمنی مال‌الرضا نام نهاد.» «جهانگیری» ولی درسخ تاریخ بلعمی (ترجمة طبری) که
در دستری ها بوددرفصل «درن کرخبر عدل انوشروان وخراح‌لهادن برولایتها» با وجود شرح چنین
خراج » نام «همدامتانی» باد شده است . همچنين درشاهنامةٌ فردوسی در عنوان «بخشید ن کسری
پادشاهی را بچهاربهروتدبیر کردن‌خراج را» ذ کراین‌کلمه نیامده. ر4: شاهنامدیخ ج ۸ص ۲۳۱۶
‎٩‏ ووقصل بند ۲۳۱۹ - *۲. درفپرست ولف هم‌کلمه فقط بمعتی مذکور درح ۸ آهده است . .

5 همخوابه - بفتح اول وواومعدوله‌وقتح باء (درنلفظ کنوی بکسرباه) از: هم (پیشوند
اختر41) + خواب ۸ (پودد) ؛ زوجهٌ مرد » همرء هم بالین هم بستر » کل ی که پادیگری در
يلك بستر بخواید :

ور لبود دلبر همخوابه پیش دست توا ن کرد درآغوش خوبش.

«گلتان صس ۶۱۲4

۵ همدان - بنتح اول ودوم» پهلوی ۴18224088 «مار کوارت » شم‌رستانهای ابران
مس » پارسی‌باستان 13(81221282) 118 « کنت. پارسی‌باستان ۲ 112081081288۲۱
«اغپیگل‌س 4 ۰۲۸ ۳ ۳۵81278 که‌پایتخت شاهیدرعهد. مادهابود. درعیلامی18-228 ۰88-702
آکدی 9-88-338-12-01 ۰ بودانی ۳8۵)858ع۸ "۰ 786841۵088 محتملا مشتق از

بقیه در حاشیةٌ صفحهٌ بعد
[pdf page 452]
```


## [2026-09-14T02:00:54.894Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '18358,18396p' incoming/BQT/BQT_v4_pages.txt",
 "description": "BQT vol4 pdf page 452"
}
```


### [2026-09-14T02:00:54.989Z] TOOL RESULT

```
[pdf page 452]
- ۳۹۹ عمرفقشس
همدست! - بنتح اولودالابجدبروزن همراد - با رای قرغت بروزن فرهاده
کم بت . بمعنی شريك ورفیق و متفق باشد - | دوکس راکوبند که درهمت وسفاوتر و شجاعت
وبمعنی همنشین وهمر- وهم‌زور در قوت‌وقدرت | وجوانمردی وکرم همچوهم باشند چه رادیمعتی
وشآن وش و کت وعظمت هم هست. . سغاوت وشجاءت وهمت‌وجوانمردی هم‌هت۹ -
همدستان < بروزن سرمتان", جمع همراز۷ - بروزن پرواز . محرم‌اسرار
همدست است بمعنی «منشینان وهمکاران | را کوبند بمنی شخصی که ازو هیج چیز پنهان
وشربکان ورفیةان وهمسران - وبمعنی‌همداستان | لکنند ... .
هم هت ۴ - و بمعنی دست بدست نیز آمده همر افته۸ - با فا بروزن دوخواسته.
است۴ . بمعنی مفهوم است بعتی‌آنچه بفهم درآید.#
ههمدم؟۴ - بروزن مرهم . بیالةٌ شراب همر س؟ - بروز نک رکس, بممنی‌درم
خوریرا کویند - ودوغواص را نیز گفته‌اند که وم | ودینارباشد .
وفی هردوموافق باغدیمنی وقتیک‌وم‌نگاهدارند | اهمرفشده « بفتح اول و رای قرشت
هردوبرایر نگاه توانند داشت تا چون دم شخصی | وسکون ثانی وفای سمقص » اسبی را کوین د که
که دربیرون دربا است تمام شود آبراکه درون | داخل در پنج سال شده باشد و همه دنداتهایش
دربا است فی‌الحال پرآورند تاهلاك نشود 8 . پر آمده باشد ؛ وبجای فا واوهم کفته‌اندکه‌همرو
۱ - از: هم (پیشود اعترا4) +دست (هم.) + ۴ - مغفف «همداستان» .
۴ - رشیدی باین معنی ولیز به‌منی هم سخن وهم نغمه‌آورده (رك : دستان) .
۴ - از: هم (پیهود اخترا4) + دم (۸.م.)؛ کردی 13601-461 (طرفدارء وابته بيك
دسته) «ژابا س40۱>. 6 - رشیدی بهمین معانی آورده است .
‎۹٩‏ - رادی باین «منی است وهراد» صفت است .
۷ - از : هم (پیهوند اعتراك) + راز(ه.م.) ۸ - برساختهٌ دسالیر«فاب۱ ص4۷
«فرهنکه دسانیرص ۲۷۵ .۰ ‎٩‏ - برساخته دساتیر «فرهنگه دساتیر ص۲۷۵ م
همراه - بفتح اول . از : «م ( پیخود ادتراه ) ۲ رام * هامراء (ه.م.) ؛ زباکی
180 (دوست) «کربرسن س ۸۱ + کیلگی 817-78 ؛ دوبا چندکس که باهم» راهی‌را عای
کنند ؛ هم سفر- مجازاً متفق , متحد .
همراهی - بفتح اول.از: «مراء (ه.م.) ی (حاصل مصدر. اسم معتی) عمل*مراه»
هم‌سفری - مجازاً موافقت - اعانت » باری .
بقیه از حاعیهٌ صفحهٌ اقبل
۵ (۳ 528 < اوستا8۳ < 068) 83818 (از ربشهٌ 8870) بممنی(جای [شهر ]اجتماعات)
رك : کنت ایا , اشپیگل ایضاً . «مدان از شمال محدود است به قزوین و خمه » از مفرب
بکرماشاهان , از جنوب به عراق وملایر » از مشرق به ساوه وزرند . برای اطلاع از تقیمات
حکومتی‌آن درعود اغیز, ر : کیهان . جفرافیای سیاسی ص ۳۸۵-۳۷۹ ؛ در تقیمات کئولی
همدان جزو استان پنجم است, طولآن۶۸ درجه و۳۱ دقیقه » عرض۳8 درجه و4۸ دقیقه,اربقاع
۹ امتر. مقرفرماندار است ودز ۳۹۸ کیلومتری باخترتهران وافع است . دارای4 بخش است.
جسیت ۱۲۳۲۸ «راهتیای آبران , بشربهٌ دالرء جغرافيايي ستاد ارش م۱ ۱۴۳۵
[pdf page 453]
همزاد نی
```


## [2026-09-14T02:01:06.701Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### PHD\"; grep -n -i \"handarz\\|hangām\\|hangam\\|han[jǰ]aman\\|hangēxt\\|handōh\\|andōh\\|andūd\\|anduxt\" PHD.txt PHD_mackenzie.txt | head -40\necho \"### NYB\"; grep -n -i \"handarz\\|hangam\\|hanjaman\\|hangex\\|andoh\\|andud\" NYB_vol2_glossary.txt | head -30",
 "description": "MacKenzie and Nyberg greps"
}
```


### [2026-09-14T02:01:06.784Z] TOOL RESULT

```
### PHD
PHD.txt:125:did ... add other. add dig |YTMAL < А *?{т?1 | N di] yesterday. delete *drém ... (read balgam) drubušt ... add protective. drust [drw(d)st' ... duš-čihr ... add ill-natured. duš-nām [-n^m | (M dwjn'm), N ~] add ill-famed. dušwār [dwáw?l | (M dwjw'r), ... ékanag ... for obedient read loyal, faithful. ~th : for obedience read loyalty, faithfulness. for Farrēbāg... read KFarrēbāy [pinb(^)g] ... frayad |pl(y)d^t' | N faryad] ... delete M pry'd. frazand |prz/znd | ... frusag ... add M prwšg. garódman ... read | P grdm'n. gazdum |gcd(w)m, gzd(w)m |... guftàr ..., ~th : add eloquence. hambar |hm-, hnb] |... add  hamest |hmyst'] whose good and bad deeds weigh equal. ~(ag)an |-(k)^n'] limbo, the neutral station between heaven and hell. delete hammist ..., ~(ag)an ... handarz ... add M °’ndrz. hammoxtan, hammoz-, ~i8n : add learning. hast |TWMNYA < A tmny ; ... add hūg [HZWLYA < A hzyr’; hwk' | M hwg, N xiig] pig. add hūkar(ag) |hwkl(k') | N xükara] porcupine. (not hedgehog) add *huzārag [hwc’lk | N хијага) little, small, few. !jadag ... add fortune. jüdan ... | M jwwdn, jwy- ... add karawuš [kl wš| N ^] wine-press. delete karbunag ... read karbūg |klpwk', klbwk'| lizard. kardagān ... add service (ofthe gods). delete karxēš vds
PHD.txt:308:dahigān [dhywk’n' | N dihgān] countryman, farmer. dahliz [d^hlyc | (M dhryz), N ~] portico. dahm [d?hm] virtuous, pious; a full member of the Mazdean community, initiate. dahom [hwm | M dhwm, N ~] tenth. dalman [d”/mn' | N dál(man)] lammergeyer, eagle. dam- , ~išn, v. daftan. īdām [d”m | = M] creature, creation. здат [Pm | = M, N ~] tame animal. здат [d’m | P d’mg, N ~] net, snare, trap. dāmād [d?r?t! | M 424, N ~] bridegroom, son-in-law. ~ih: condition of a bridegroom, son-in-law. daménag [dmynk'] fan. damidan [dmytn'] = daftan. dān-, —išn, v. dānistan. -dàn [-d’n' | = M, N ~] suffix, -holder, -container. dàn(ag) [d”x(k)! | N ~a] seed, grain. Н dānāg [4>рА! | М dwg, N dana] knowing, wise. ША zn kh ~ih: knowledge, wisdom. ar dandàn [KK A < А kk’; dnd’n' | = M, N ~] tooth. dānistan, dān- [YDOYTWN-stn' < A У yd‘; d’n-stn' | M d^n-ystn, N ~] know. ~ign: knowledge. ~i8ndmand [- отпа) knowing. dar [BBA < A bb’; dl | M dr, N =] door; palace; chapter, subject. dar [d?] | M d@’r-, N ~] tree, gallows; wood. dar-, -išn, v. dāštan. -dār [-d'/| M -d’r, N ~] suffix, -holder, -keeper. Р darāy [dPg | J ~, N darāy] bell. *darak [dlk'] section, paragraph. darband [B B Abnd | N ~] gate. darbās [dips] palace. dard [dit! | M drd, N ~] pain. ~отапа [отла | M -wmnd, N ~mand] ill, suffering. dārēn [d'/yn! | М drwyn] wooden. darģāh [dig’s | N ~] doorway. dargardih [d*/krtyh | M d’rgyrdyh] crucifixion. dar-handarzbed [BB A-, dl-hndlcpt'] chamberlain. darigbed [dlykpt'] palace superintendent. *darmag [d?/mk!'] fine, delicate. darmān [dim?n! | M drmn, N ~] remedy, medicine. darridan, darr- [SDKWN-tn! < A V sdg; dl-ytn! | N <] split, tear. dàrüg [d"Iwk! | М drwg, N dari] drug, medicament. dār-wāzīg [Tlw cyk! | N dár-bàz] (pole-)acrobat. darz [dlc | N ~] seam. ~ig [-уА! | N darzi] tailor.
PHD.txt:391:haméstür 41 handarzénidan
PHD.txt:392:hamēstār, —ih [hmyst!l, -yh] = hamēmāl, ~ih. hamésag [hmyfk! | M hmyšg, N —a] always. ^h : eternity. ~-86z [-swe] ever-burning. hamē-wahār [hmy whl | N haméfa-bahar] marigold. ham-éwénag [Am'dwynk!'] of the same kind, homogeneous. ham-góhr (hmgwhl! | M hmgwhr] of the same substance or nature, consubstantial. ham-ginag [hmgwnk! | M hmgwng] likewise, so. P hāmharz [A())mAlc | P I? mhyrz] adjutant, attendant. hāmīn [A*myn! |= M] summer. ~ig [-yk'] (of) summer. hāmist [KHDE, v. hammis ; )”mst!] all. ham-kār [hmk’l | N ~] collaborator. 7h : collaboration. hāmkišwar [mkyfwl | M. -wr] universe. hammis [KH DE < A k-hdh), ат... ~: together with. hammist [hmyst'] stagnant, peaceful. ~(ag)an [-(kYn'] limbo, the neutral station between heaven and : hell. vl hammóxtan, hammoz- [ALPWN-tn! < A У "Ip: hmwhtn', hmwc-, Ki hmsoz- | M hmwxtn, N āmēxtan, ámóz-] teach; learn. -išn: teaching. hammdxtar [Amwht?!] learner. ~th: learning. hammóz- , ~i8n, v. hammóxtan. —@йг [kmwcek?l | N āmēzgār] teacher. ham-nibardih [hmnpityh] (single) combat. hamēūģ [/tmwg] equal, like. hámón [k mwn' | N kāmūn] level, flat. hámoyén [/?mwdyn!] all. ham-pursag [hmpwrsk!] consulting, taking counsel. ^h : consultation. ham- |-ránih [Am nyh] battle, combat. ~-samiain [-s"m?n!] contiguous. ~-sardag [-sltk'] of the same kind, like. ~-sayag [-sdk! | N hamsáya) neighbour. ~-tag [-t*k! | N hamid] equal, peer. «tan [-tn'] of the same stature, build. ~=-tihmag [-twhmk'] relative, relation. hamwar [hmwl | N hamwār] level, abreast. hámwiür(ag) [%()mw?/, -k! | N hamwdara] always. ham-zamān [hm ODNA | N —] instantly, immediately. handām [And*m | = P, N andàm] member, limb. handarz [hndle | N andarz] advice, injunction, testament. handarzénidan, handarzén- [hndleyn-ytn!] advise.
PHD.txt:394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
PHD.txt:738:advice handarz, pand.
PHD.txt:739:advise handarzénidan.
PHD.txt:867:assembly hanjaman.
PHD.txt:1192:chamberlain dar-handarzbed,
PHD.txt:1296:community hanjaman; wālan.
PHD.txt:1340:congregation hanjaman.
PHD.txt:2083:gathering  čīnišn, ` harróbiin(ih); (group) gund, hanjaman.
PHD.txt:2438:injunction handarz.
PHD.txt:2963:occasion bar, jar, hangām.
PHD.txt:3959:testament handarz.
PHD.txt:4017:time амат, bar, gah, hangām, jar, zamān(ag), zurwán.
PHD.txt:4018:timely hangamig.
PHD.txt:5376:garānīh darhandarzbed yarranidan garan yarranisn gramigih gramig grāmag drāyīdan, grāyīdan drāz, grāb draxt griy- grih dargūh garasman 1 3uriw griwag grīwbān driyos driyöšīh darigbed dilér drëm griyistan
PHD_mackenzie.txt:555:       handarz .,. add M 'ndrz.
PHD_mackenzie.txt:1892:dar-handarzbed [BBA-, dl-hndlept ' ] chamberlain.
PHD_mackenzie.txt:2741:ham&tlr                         41                handarz~nidan
PHD_mackenzie.txt:2789:handarz [hndlc i N andarz] advice, injunction, testament.
PHD_mackenzie.txt:2790:handarzenidan, handarzen- [hndlc,,,,-ytn ] advise.
PHD_mackenzie.txt:2819:hangam [hng)m IN ......] time, occasion.
PHD_mackenzie.txt:2845:hanJaman [hncmn l I (P )njmn, M hnzmn), N anJuman] gathering, assembly,
PHD_mackenzie.txt:5894:abstain pahrextan.                        advice handarz, pando
PHD_mackenzie.txt:5895:abuse (n.) dusniim, wad-wiizag.           advise handarzenidan.
PHD_mackenzie.txt:5986:assembly hanJaman.                       back (av.) abiiz.
PHD_mackenzie.txt:6139:camel ustar.                            chamberlain dar-handarzbed.
PHD_mackenzie.txt:6197:clay gil; gilen.                         community hanJaman; walan.
PHD_mackenzie.txt:6246:congregation hanjaman.                       cool (v.) afsardan.
PHD_mackenzie.txt:6871: impalpable agriftar.                      injutlction handarz.
PHD_mackenzie.txt:7157:nice xwas.                             occasion bar, Jar, hangam.
PHD_mackenzie.txt:7779:testament handarz.                        thrust spoxtan.
PHD_mackenzie.txt:7791:time awam, bar, gah, hangam, Jar,        treasury ganJ.
PHD_mackenzie.txt:10519:grah                        N~     darhandarzbed        \¥,Q.)~~
PHD_mackenzie.txt:11208:besazenisnih   AU~~,                          darhandarzbcdI   \¥'eu~",*~\
PHD_mackenzie.txt:11890:huskoh                    N\~"",           hanjamanig                 ,1)t6~    ,...
PHD_mackenzie.txt:11892:                       ~'.YO"'"            hanJaman                     lyG~ "..
PHD_mackenzie.txt:12013:xwedodah          ,.vu "ta lA'                 handarz                         ~t"'
### NYB
445:motion: šutan, dväristan, opastan, ete., and with ēstātan and nisastan (also ~ 6). — 2. prep. in, local, temporal and figura- tive: ~ Pārs; ~ im xünak P1:6; ~ miyàn i in the middle of 865; ~ han hangam at the time 613; ~ ham zamān at the same time 127°; ~ zamān in due time 221, etc.; ~ sap in the night 529, 614; ~ hàsr for a single moment 663; ~ hàn in the meantime 5615-17; — xtatäyeh + Xösrör 1184; ~ Vistasp šāh kisvarikan when V. was the emperor of the world 365; — freftür ~ : concerning 3419-20, 10923; spasdārēh ~ , an-ispās ~ : to, against; with other substantives, v. these separately ; — together with another prep.: ~ 6 into, on to, up to: ~ 6 nun 404; with apakandan, burtan, guméxtan (also without 6), hištan, kartan (v.s.v. kar); apar ~ 402, — Av. (131 sq.) antara, antarš, OP antar (better read antara^); MPrthPrs ’ndr; Paz. NP andar; v. also niyandar.
618:ä-rasan [?lsn'] convention, assembly ; cas. obl. pat-šān —-ēh Plsnyh] 10924, — FrP 12 KNŠY> (for KNS») = hanjaman, drasan; certainly < à + rasan from rasan.
727:2aš [^5] the independent form of the cas. obl. 3d p. sg. = enel. -$ (g. v.); always preceding the w. to which it belongs; used 1. anaphorically in the interior of a sentence after a part of the sentence which has been placed first for emphasis: andar han Zartuxst | aš hac miyān Gp i hömikän burt || u pat uléh Zartuxšt | aš han i dašn paitištān hac Osan rote burt 5615-1? (Markwart's reading, Cat. 114 n. 1, is a failure); õi (pron.) mar | aš 6 pasčh gàv apāc rānēnīt 485; — not anaphorically: Ot (prep.) fravahr + Zartuxst | aš (viz. the snake) zafar frac zat 4012-13; purr-x"arrahéh i ax" à astómand | aš hac tan xYarrah from his (viz. Zartuxšt's) bodily splendour 377-8; — taking up an encl. -§ at the beginning of the sentence, after a part of the sen- tence which carries a lengthy attribute: api-š hamäk damik i-š apar rāh bit | aš *perävanihit kart 3316-17; — after an ad- verbial phrase beginning the sentence: adak apar pat jamän | aš hanjamanénit mūtak :61° (where aš anticipates mūtak, cf. s. v. -š). — 2. to introduce the apo- dosis (as api-$, adak-i8): after kakar 31?! ; after ka 327. 3319. 341. 565. 5717. 924. after a relative clause 3219, 9824, 100?7— 101?. — Probably identical with MPrthPrs š, written as an independent w. with two dots above (another explanation of this § v. A-H III, Gloss s. v.; ? in a fragmentary context [S] is obscure). Cf am, at, atün, asän.
1191:dar [BB”] door 75"; gate, pl. ~ -ihā 8713.18, 11472; hac an ~ in another way 813; har ~ every category 111”; — a royal person's court P1:4. P2:9. 39. 55, 131, 1710, 208-9. 617. 705. 1077. 1097. 1123. — SW form of Av. (766) dvar-, OP duvara-: MPrs dr, Paz. NP dar- as against NW: MPrth br, NP bar. — V. darak, dar-band and dar-handarz-pat.
1196:dar-handarz-pat v. handarz-pat. *darik [*dlyk] courtier, court dignitary
1243:davistan [LHTWN-stn'], davitan [dwytn', LHTWN-tn'] to run, pt. = pret. 3d p. sg. davist [LHTWN-st'] 71%; pass. constr.: devän hanjaman davit [dwyt'] (by the devs an assembly was run at =) the devs hurriedly arranged an assembly 424, .. MPrs dw-, Verbum 173; NP davidan.
1872:adverbs and conjunctions: hac hàm | handarzčnitan [—-ynytn'] to give direc-
1880:handarz [hndlc'] counsel, advice 41%. 62 (heading). — Ps. hndley ‘command, law’; MPrs ?ndrz (S); NP andarz.
1881:tions, warnings, to instruct: apt-m züpihä „.. handarzenit he 7615-16,
1882:handarz-pat [hndlept'] chancellor, chief judge, head of the treasury of a province or a corporation, administrator of pro- perty: Sakistin ~ P 1:6; dar-~ 7 vàs- puhrakän the court administrator of the (royal) properties 1118-19, v. 2vdspuhrakdan and Périkhanian, REA V, 1968, 20-21 (cf s.v. väspuhr); [yztpt MLKTH-n hndrzpty KZSPrth 1. 27 = yztpt ZY b’ny(!)kn hndicpt Prs 1. 33 = Gr. v. InodtBad Bactrrcodyv avčapčaBIŠ (enumer- ated among the lower ranks of court officials). — Arm lw. handerjapet ‘the Master of the Royal household’, already in the Bible (e.g. 1 Kings 16:9 = Gr oixovéuoc), then often ‘director, manager” in different functions; when speaking of Persian officials the authors use the form anderjapet: Sakstan a. P‘aust. Buz. 4,45, mogac a. ‘the chancellor of the Magi? ibd. 4,47, or in the idiomatic Persian form Movan a. EliSe (5th c.), Hist. of the Vardans (Venedig 1838), 138. 142 (thus the MSS; the ed. han-).
1894:handóhakan [hndwhkn'] anxious 4?. — Also handöhaken, J.-Prs ’ndwhgyn Isa 1:2. Arm. lw. andohakan ‘disquieting, dreadful’.
1897:hangäm [hng’m] time, epoch, season 27°. 142°, 613. — MPrs ’ng’m (S); Paz. hangam; NP hangam. — Cf àvàm.
1906:hangaxtär [hng’ht’l] instigator: anäkeh ~, of Ahriman 679%, — For hangextär
1921:hanjaman [hnemn'] meeting, assembly, congregation 4214. 6615, 7022, 91%. 10328, -Av. (1770) hanjamana-; MPrth hnjmn; MPrs hnznm (A-H I); NP anjuman; Ps. "newmnyh'y ‘congregations’.
1923:hanjamanénitan [~-ynytn'] to speak in the assembly, Lat contionari, 619.
1924:hanjamanik who speaks in the assemblies, orator, eloquent, epithet of Narčsang 6019, renders Av. (1477) vydxana-.
2282:ken andar). — 8. as a kind of izäfat, mostly introducing an apposition: hán mart ... ke ahlav Zartuxšt 4919-17, 4317-18, adak-iš čišan guft ke dätär Ohurmazd 58°; han vartēnišn ... ke fraškart-kartārēh i veh 9921-22.25—26. without an antecedent: bavēt . ke Spitāmān Zartuxšt it may be S. Z. 6023; 597: an. imitation of the Av. idioms azom yö ahurö mazdå; hanjamanam fra- barata yo dadvd ahurö mazda ete.; — seldom introducing a gen.: han x¥arrah ke ... Eran dēhān ké-c ahlav Zartuxst
4017:2vaspuhrakan adj. of väspuhr: belonging to, or characteristic of, a member of the elan or family entitled to share the patrimony (chiefly people of the upper or highest classes of the society): 1. subst. the patrimony itself: dar-handarzpat + ~ 11, v. handarzpat. [- 2. distinguished, prominent, comp. ~-tar, sup. ~-tom DkM 2921-17; adv. ~-tha especially, par- ticularly, e. g. DkM 413?!.] — Correspond- ing to Arm sephakan, v.s. v. vispuhr. vāspuhrakānīk adj. = ®väspuhrakän 2, comp. ~-tar 1068.
5176:hanjamana-: hanjaman
5458:vyāxana-: hanjamanīk
5630:hnjmn: hanjaman
5778:’ndrz: handarz
6004:hn’m: hannam hng'r-: hangärtan hnng: "hangomand hnzftn, hnz'm-: hanjàm- hnzmn: hanjaman hrw: har
6634:hangam: hangäm
6990:andarz: handarz
7004:anjuman: hanjaman
7504:Armenian andohakan: handöhakan apa: ap
```


## [2026-09-14T02:01:08.756Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### CHEUNG vaig\"; grep -n \"uaig\\|\\*uai(H)g\\|vaēg\\|vaeg\" CHEUNG.txt | head -20\necho \"### CHEUNG dau\"; grep -n \"^\\*dau\\|\\*daHu\\|to smear\" CHEUNG.txt | head -20",
 "description": "Cheung greps"
}
```


### [2026-09-14T02:01:08.826Z] TOOL RESULT

```
### CHEUNG vaig
### CHEUNG dau
5241:*dau2 65 
5253:*dau! *to speak, chat' 
5286:*dau? ‘to run’ 
5323:*dau? ? ‘to be skilful’ 
5335:*daub ‘to strike, hit, pick ?” 
5358:*dauč! (*dauj ?) ‘to milk, traire (< **to draw’ ?)’ 
5371:*dauHl 67 
5422:*dauH! ‘to burn’ 
5482:* dauH? ‘to smear, rub (on)’ 
5489:*dauxs 69 
5495:*SOGDIAN: BSogd. ó w ‘to smear, plaster’ || (+ *ham-) BSogd. ’nö’w, MSogd. ’nöw 
5496:‘to smear, anoint’ 
5506:zadudan/zaday- ‘to polish, clean’ || (+ *ham-) NP andudan/anday- ‘to smear, 
5508:original meaning of NP 4ludan/alay- appears to be ‘to smear’, v. Horn 1893: 10. The 
5515:against’ || (+ *ham-) Yi. da-/davd- ‘to smear’ 
5522:whereas IE cognates cannot be cited in support of Ir. *dauH! ‘to smear, rub (on)’. It 
5538:*dauxš ‘to suck, suckle, milk’ 
7632:*NEIR: Pash. yandol ‘to dislike’ (+ *pari-) Oss. D. feelgandun/faelgzst ‘to smear; 
8076:*CHORESMIAN: yrcy- ‘to roll; to get rid of; to smear with clay’ || (+ *ati-) cyrcy- (tr.) 
9457:*dauH?.
```


## [2026-09-14T02:01:24.254Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### CHEUNG angextan\"; grep -n \"angextan\\|angēxtan\\|angéxtan\\|angixtan\" CHEUNG.txt | head -20\necho \"### CHEUNG uai\"; grep -n \"^\\*uai\\|\\*uaig\\|\\*ua(i)g\" CHEUNG.txt | head -20\necho \"### CHEUNG gam ham\"; grep -n \"anjam\\|anjuman\\|hanjam\" CHEUNG.txt | head\necho \"### andoh HUB/HRN\"; grep -n -i \"andoh\\|andûh\\|andūh\\|anduh\" HRN.txt HUB.txt | head -20",
 "description": "Cheung angextan and andoh sources"
}
```


### [2026-09-14T02:01:24.364Z] TOOL RESULT

```
### CHEUNG angextan
7275:angextan/angez- ‘to stir up, incite’ 
40712:angéxtan/angéz-, 97 
### CHEUNG uai
26425:*uai ? ‘to cut off, sacrifice ?' 
26507:*uaid! ‘to know? 
26531:*uaid2 409 
26659:*uaiH 411 
26684:*uaiH ‘to hunt, chase; to run’ 
26778:*uaij 413 
26820:*uaij ‘to shake, swing’ 
26894:*uais 415 
26897:*uaip ‘to swing, shake’ 
26930:*uais ‘to enter’ 
26979:*uais ? ‘to be concerned, occupied; to work for ?' 
27003:*uaiZd ‘to raise’ 
56007:*uaic (s.v.), *uar(H)', *zaus 
56013:*uaic (s.v.), *xšad, *zaË 
56276:*uai 
56457:*uaic 
56598:*uaid^ 
57513:*uaizd 
57777:*uaic 
57825:*uaic 
### CHEUNG gam ham
7371:*ham-) MMP hnz’m-, BMP hnc’m- /hanjam-/ ‘to finish, fulfil = DMMPP: 227b, 
7443:‘Apostle, Prophete (esp. Mohammad)’ || (+ *ham-) NP anjuman ‘company, 
25471:Pres.: IND. 1sg. BMP hncm /hanjam/, 3sg. BMP hncyt /hanjéd/; Inf: BMP hyhtn /hixtan/; Partic.: BMP 
35206:hne’m- /hanjam-/, 99 
40715:anjuman, 100 
### andoh HUB/HRN
HUB.txt:4995:= koh 'Berg'; anduh = andoh *Kummer : htiS = hds 'Ver-
```


## [2026-09-14T02:01:27.461Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG 7260-7300 (angextan ctx)\"; sed -n '7250,7300p' CHEUNG.txt\necho \"=== CHEUNG uaij 26820\"; sed -n '26815,26900p' CHEUNG.txt",
 "description": "Cheung angextan and *uaij entries"
}
```


### [2026-09-14T02:01:27.552Z] TOOL RESULT

```
=== CHEUNG 7260-7300 (angextan ctx)


*PIE— > LIV: — | Pok.: 354 

*REFERENCES: JIFL II: 211b, 201b, 275a; Morgenstierne 1942: 263; Fraenkel II: 143; Abaev, Slovar’ II: 
305 f.; EVS: 110a, 96a f., WIM II: 671; DKS: 90b; Vahman — Asatrian 1987: 89; Lecoq 2002: 576b, 
594a, 616b 


*gaiz ? *to disturb, stir, incite, excite ?' 

*MIDDLE PERSIAN: (+ *ni-) BMP nkyc- /nigez-/ ‘to expound’ || (+ *ham-) BMP 
hngyc- /hangéz-/ ‘to arouse, stimulate, stir up’, BMP hngycyn- /hangézén-/ (sec. 
caus.) ‘to resuscitate’ 

(+ *ni-) Pres.: IND. 3sg. BMP nkycyt /nigézéd/; Inf.: BMP nkyhtn /nigextan/ || (+ *ham-) Pres.: IND. 3pl. 
BMP hngycynd /hangézénd/; Caus.: IND. 3sg. BMP hngycynyt /hangézénéd/ 


*SOGDIAN: (+ *ham-) ? BSogd. ’nyyznykh ‘emetic, un (remède) excitant 
(Benveniste, TPS: 232 ad 5). Š This technical term is found in a medical Buddhist 
text twice (P 19.5, P 19.11). 

*NWIR: NP gej, Kurd. gEZ confused, astonished’ (with suff.) Bakht. gez ‘mad’, ? 
Meim. darem gianä/dar a-gizn- ‘to clear, explain, elucidate’ || (+ *ham-) NP 
angextan/angez- ‘to stir up, incite’ 

*NEIR: Oss. І. qyzyn/qyzt, D. gizun/gizt ‘to threaten; to behave hostile, be male- 
volent; to start to rain’ || (+ *ham-) Oss. I. ænqizyn/ænqyzt, D. engezun/engizt ‘to 
be in a state of fermentation; to ferment’ (sec. prefixation). 0 Oss. I. angizyn, D. 
angezun has a secondarily attached æn- (< (*ham-): if the prefixation was old, it 
would have become I. **zngizyn, D. **angezun. Formally this secondary forma- 
tion would derive from the "simplex" I. qyzyn, D. £izun, whose meanings are dif- 
ficult to reconcile with I. engizyn, D. aengezun. The only way to do so would be if 
we start from an older meaning such as *‘to disturb, be stirring’, which could have 
developed into either *‘to cause disturbance, stir up trouble, strife’ (whence ‘to act 
in a hostile, malevolent way’) or it could have referred to the weather, cf. Engl. 
storm (cognate with to stir). 

*PIE ? 0 Apparently quoting from Lidén KZ 61: 1ff., Pokorny, l.c. only mentions the 
Oss. verbs as Ir. cognates, which would go back to an IE root *geig- 'stechen, 
beißen’. Not only is the reconstruction *geig-, with two unaspirated voiced stops, 
phonologically impossible for PIE, also the inclusion of the Oss. forms can be 


98 *gaml 


doubted, if their meanings have risen only secondarily. Considering the other Iranian 
cognates of the Oss. forms, we have to rule out any relationship with the IE forms 
cited by Pokorny as cognates: Arm. kcanem ‘to bite, sting’, kc-u ‘bitter, rancid’, 
=== CHEUNG uaij 26820

EVS: 90a; WIM I: 73; WIM II/1: 85; WIM III: 118 £; Abaev, Slovar’ IV: 117 f£; Paul 1998: 319a; 
Steblin-Kamenskij 1999: 389; Cabolov 2001: 199 


*uaij ‘to shake, swing’ 

*AVESTAN: YAv. vij- ‘to shake, swing ?' || (+ *fra-) YAv. frauuaeya- “swinging 
forward’ (Yt 10.96, Yt 10.132) || (+ *ni-) ‘to swing down(wards)’ = Liste: 54 

Partic.: pres. YAv. vaéjant- (? Yt 19.92, ? F 431), perf. pass. YAv. -niuuixta- (Yt 6.5) 

*MIDDLE PERSIAN: BMP wyc- /wéz-/ ‘to swing, fling, sprinkle’ || (+ *ui-) MMP 
whyz-, ВМР wyhyc- /wihéz-/ ‘to move, progress, set out’. 0 On the etymology of 
MMP whyz-, BMP wyhyc- see Nyberg 1974 II: 211b. The older etymology of 


Henning 1933: 178 has been rejected by Nyberg. > DMMPP: 342b 
Pres.: IND. 3sg. ВМР wycyt /wézéd/, 3р1. BMP wycynd /wézénd/; Inf: BMP wyhtn /wextan/ || (+ *ui-) 
Pres.: IND. 3sg. MMP whyzyd, 3р1. BMP wyhycynd /wihezend/ 


*PARTHIAN: (+ *ati-) 'dwyxs- ‘to shake (the head)’ > DMMPP: 25b 


414 *uaij 


(+ *ati-) Pres.: IND. 3pl. 'dwyxsynd {hapax} 

*SOGDIAN: BSogd. wyc, CSogd. wyc ‘to move, shake [intr.]’ || (+ *apa-) BSogd. 
pw’yc- ‘to shake, be agitated’ || (+ *a-) ? BSogd. ’’wys ‘to confuse, disorder’, 
CSogd. ’wyZ ‘to become agitated, angry’ || (+ *pati-) ptw’yc ‘to shake, be agitated’. 
© On CSogd. ’wyz "The etymological possibilities are numerous", Sims-Williams 
1984: 149. 

Pres.: IND. 3sg. BSogd. wyct, 3р1. BSogd. wycnt, CSogd. wycnt, SUBJ. 3sg. BSogd. wyc’t, Partic.: pres. 
BSogd. wyc’y || (+ *apa-) Pres.: SUBJ. 3sg. BSogd. pw’yc’t || (+ *ä-) Impf.: IND. 35р. CSogd. "wyZ 
Partic.: perf. pass. BSogd. "wystk ‘ksubdha’ 

*CHORESMIAN: ? wc- ‘to shake’ (rather from *ua(n)ë ?) = Samadi: 211 

*NWIR: NP bextan/bez- ‘to shake’, Bal. gé(h)t, gétk/géj- ‘to put, swing, turn towards; 
pour into; miscarry, abort’, Zaz. viziyayis/viz(iy)en- ‘to come out, appear’, Yar. 
vast, Isfah. vär-vezän/vär-vez-, Meim. a:-vaft-/a:re-vez-, Mah. wöstän, Natan. är- 
vast ‘to jump, leap’, ? Qohr. vut (pret. stem) “о hang, be suspended’ || (+ *a-) NP 
avextan/avez-, Meim. dar evidz-/dar a-vi:tai- ‘to hang, suspend [intr.]’, Khuns. 
aviz-/aviza ‘to hang on [tr.]’, (inch. ?) ? Kurd. (Kurm.) avasin/awas-, (Sor.) hał- 
awasin/awes- ‘to hang on’ (formally difficult) || 

*NEIR: Oss. I. wigyn/wygd, D. wegun/wigd ‘to shake; wave’, Sh. (Baj.) wuc-t ‘to 
move, stir, go (slowly), rock, swing, shake’, ? (Baj.) wuz-/wuzd ‘to move, stir’ || (+ 
*4-) Oss. I. awynzyn/awygd, D. awinzun/awigd ‘to hang’, ? Sh. avezun ‘to hang’ 
*MISC: ? Arm. (LW) vizem ‘I flow, miscarry’ 

*SANSKRIT: vej ‘to dart up or back, to move up (of a wave), flee, twitch, move 
quickly’ (RV, AV+) = EWAia II: 577 

Q The root is a blend of *yaité and *uaij! according to Nyberg 1974: 210; 
Sims-Williams 1989: 263. It should be noted though that we can distinguish two, 
sharply defined, meanings for an (apparently) single root, viz. ‘to move’ and ‘to 
shake, swing’. This is also found in Germanic: ‘to move’ and ‘to yield, give ground, 
weichen’ respectively. Although, obviously, it is possible that we may still deal with 
one and the same root, it is probably better to reconstruct two different 
(homonymous ?) roots. 

«PIE *ueig- ‘to (start to) swing, shake [vel am IT = LIV: 667 f. | Pok.: 1130 f. 

*IE COGNATES: Gr. eixo ‘I yield, give ground’ (with sec. -к-), OE wican ‘to yield, 
give ground’, ON víkja ‘to move, turn; respond, take action’, OHG wihhön ‘to jump, 
leap’, NHG weichen 

*REFERENCES: Christensen, Contributions I: 156, 255; Abrahamian 1936: 133; Lambton 1938: 40a f.; 


Abaev, Slovar’ I: 87 f., WIM I: 66; EVS: 87b, 96a; Abaev, Slovar’ IV: 108 Ё; Werba 1997: 376 Ё; Paul 
1998: 317b; Cabolov 2001: 98; Lecoq 2002: 656b; Shahbakhsh: s.v. géj- 


*uais 415 


*uaip ‘to swing, shake’ 

*AVESTAN: Y Av. vaep- (vif) ‘to engage in homosexual activities, be a passive’ || (+ 
*ара-) ‘to throw off (?)’ = Liste: 54
```


## [2026-09-14T02:01:43.913Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### CHEUNG andoh\"; grep -n -i \"andoh\\|andóh\\|andöh\" CHEUNG.txt | head\necho \"### HRN anjuman etc\"; grep -n -i \"enjumen\\|engumen\\|encumen\\|endôh\\|endoh\\|endarz\\|hengâm\\|hengam\\|encâm\\|enjâm\" HRN.txt | head -20\necho \"### HUB\"; grep -n -i \"anjuman\\|andarz\\|hangam\\|anjam\" HUB.txt | head -10",
 "description": "Horn/Hübschmann/Cheung on anjuman, andoh"
}
```


### [2026-09-14T02:01:44.020Z] TOOL RESULT

```
### CHEUNG andoh
26012:(+ *ham-) BMP ’ndwh /andöh/ ‘sorrow’, MMP ’ndwxyn ‘sad, sorrowful’ 
26033:*NWIR: NP tuxSidan ‘to strive’, taxsa ‘diligent’ || (+ *ham-) NP andoh ‘anxious’ 
26037:*MISC: (+ *ham-) Arm. (LW) andohakan ‘dreadful’ 
34895:"ndwh /andoh/, 400 
40704:andoh, 400 
52273:andohakan, 400 
### HRN anjuman etc
11624:enjumen 114.
### HUB
534:114. Hier fehlt zd. hanjamana- *Versammlung'.
2695:inf. saxtan (ptc. saxta gewogen ), praes. sanjam {-sanj
4407:muy- in muyanandarzbad (Hoffmann, Ausziige p. 50), phi.
4477:Auch sonst gelegentlich : hingam (A. M.) = hangam
7684:ap. ham- = np. aw- in anjuman Tersammlung = zd. han-
7688:scheint h noch in hanjar, hinjfar *Weg' H. 1106 und hangam,
7691:geblieben ist in hangam *time' Shk. 249 {Ogam Min. Gl. 149
7692:ist falsch gelesen fur angam oder hangam), handurun Min.
7693:Gl. 99 (aus dem Avesta: handvarena-), hanjaman Min. Gl.
7703:'einmar (5. Jhd.) -^ np. hangam^) *Zeit'; angarem *bringe in
```


## [2026-09-14T02:01:49.570Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG 25995-26045\"; sed -n '25990,26045p' CHEUNG.txt\necho; echo \"=== HUB 7680-7710\"; sed -n '7678,7712p' HUB.txt\necho; echo \"=== HUB 530-540\"; sed -n '528,540p' HUB.txt",
 "description": "Cheung andoh root, Hubschmann ham- prefix"
}
```


### [2026-09-14T02:01:49.656Z] TOOL RESULT

```
=== CHEUNG 25995-26045
(Aeol.) съркес̧ (pl.) ‘(pieces of) meat’, ? Olrish turc (m.) ‘boar’, are semantically 
possible, but not very informative with regard to morphology and derivation. 

«PIE? > LIV: 656 | Pok.: 1102 


*QuaxS (tux&) ‘to be busy, working on’ 

*AVESTAN: Av. Ofaxs- ‘to take care of’, OAv. @BaxSah- (n.) ‘effort, work’ (Y 33.3, Y 
46.12) > Liste: 26 

Pres. them.: IND. 3pl. med. YAv. 0Baxsonte (Yt 10.14), INJ. 25р. OAv. 0Baxšo (Y 29.2); Partic.: pres. 
med. Y Av. 0Baxsomna- (Yt 5.65) 

*OLD PERSIAN: (+ *ham-) ha™taxs- ‘to work with, effect’. © Cf. Kent, Le: 
"contamination of *tas- ‘to cut, form’, Skt. taks- ‘form by cutting’ ... and pAr. 
*tuaks-, Av. Owaxs- (mid.) be busy’ ...". = Kent: 185b f. 

MED.; Pres. them.: IND. 3sg. ha"taxsataiy <h-t-x-3-t-i-y > (DNb 16), impf. lsg. hamataxSata 
<h-m-t-x-3-t-a> (DB 4.65), «h-m-a-[t]-x-&-t-a > (DB 4.92), 3du. hamataxsa" tà «h-m-t-x-&-t-a» (DB 4.82) 
*MIDDLE PERSIAN: MMP twxs- ‘to strive, be busy with, diligent’, BMP twhs- /tuxs-/ 
‘to strive, struggle with’, (sec. caus.) MMP twxsyn- ‘to make diligent, industrious’ || 
(+ *ham-) BMP ’ndwh /andöh/ ‘sorrow’, MMP ’ndwxyn ‘sad, sorrowful’ 
c DMMPP: 33 1b, 47a 

Pres.: IND. 3sg. BMP twhsyt /tuxsed/, 3р1. MMP twxsynd, MMP twxsynd, IMPV. 2sg. BMP twhs /tuxs/; 
Partic.: pres. MMP twxs’g, (pl. MMP twxš’g’n ‘striving’, perf. pass. BMP twhsyt /tuxsid/; Inf.: BMP 
twhsytn /tuxsidan/, caus. MMP twxsynydn 

*PARTHIAN: twxS- ‘to strive, be busy with’ = Ghilain: 48 | DMMPP: 331b 

Pres.: IND. 3sg. "twxsyd, 3р1. "twxsynd 

*SOGDIAN: (+ *ham-) BSogd. ’nt(’)wxs, CSogd. ’ntwxs, MSogd. ’ndwxs ‘to strive, 
endeavour’ 

Pres.: IND. 3sg. BSogd. ’nt’wxst, 3р1. (subj. ?) BSogd. ’nt’wxs’nt, SUBJ. 15р. BSogd. ’nt’wxs’n, OPT. 
lsg. CSogd. "ntwxsym ’zw (Weber 1970: 152), 3sg. MSogd. "ndwxsyy, IMPV. 2р1. BSogd. ’ntwxst’, 
MSogd. ’ndwxsö’, Partic.: pres. BSogd. ’nt’wxs’k, BSogd. "ntwxs'k, MSogd. *’ndwxsy (BBB: 39); Inf.: 
BSogd. ’ntwxs’y, BSogd. ’ntwxs’k, pret. BSogd. ’nt’wxs’t 

*CHORESMIAN: (+ *ham-) ’ndyx (m.), ‘пах (m.) ‘sorrow, sadness’ 

*NWIR: NP tuxSidan ‘to strive’, taxsa ‘diligent’ || (+ *ham-) NP andoh ‘anxious’ 
*NEIR: Oss. I. tyxsyn/tyxst, D. tuxsun/tuxst ‘to be restless, confused, concerned; to 
be burdened; to be in a difficult situation; to succeed in’ 

*MISC: (+ *ham-) Arm. (LW) andohakan ‘dreadful’ 

*SANSKRIT: tvaks ‘to be working, active, strong’ (RV) = EWAia I: 683 f. 


*yab/fl 401 


9 This Ш. root has no certain IE correspondences. It is interpreted as a desiderative 

=== HUB 7680-7710
alien noch als solche gefiihlten Komp. mit hu-.
§ 107. Anlaut. h schwand im Np.:
a) in der Partikel ap. ham- als 1. Glied von Kompo-
sitis vor folgendem g, jf, d, b (= ap. k, g, 6, y, t^ d, p, J),
vor welchen Konsonanten m wohl schon im Ap. zu n (= n,
n, n, w), das nicht geschrieben wird, geworden war: daher
ap. ham- = np. aw- in anjuman Tersammlung = zd. han-
jfamana- ; anddm 'Korper, Glied' = zd. handdma- ; angCLrdan
'meinen', zd. hankcLrayemi ; anbaStan *anfullen', skr. sampUray-
u. 8. w., vgl. Horn Nr. 110-127; unten § 151. Doch er-
scheint h noch in hanjar, hinjfar *Weg' H. 1106 und hangam,
hingam *Zeit* H. 1109. Ebenso liegen die Verhaltnisse im
Pazend, vgl. Shk. 229—230, Min. Gl. 10—12, wo h nur
geblieben ist in hangam *time' Shk. 249 {Ogam Min. Gl. 149
ist falsch gelesen fur angam oder hangam), handurun Min.
Gl. 99 (aus dem Avesta: handvarena-), hanjaman Min. Gl.
99. Im Pehlevi unterscheidet die Schrift nicht zwischen
an und han (sowie hu, xu^ if, o). Im Armenischen ist h
erhalten in hambar *Speicher nebst Ableitungen (5. Jhd.),
neben dem auch ambar vorkommt ; handerjapet (5. Jhd.) =
anderjapet; handes *Erweisung {svS^thg), Bewahrung, Muste-
rung (5. Jhd.) = skr. samd^ga- 'Anweisung', zd. handae-
sayaTluha (ipt. med.); haniar 'Einsicht, Verstand' (5. Jhd.)
= np. hanjar 'Weg' (?), dagegen geschwunden in .ambar
*Speicher' = np. anbar, syr. ^<^3DN; angam 'mal* {mi angam
'einmar (5. Jhd.) -^ np. hangam^) *Zeit'; angarem *bringe in
Rechnung* (Sebeos 138) = np. angaram; andacem unter-
suche, priife* (Elise 14), np. andaz *Plan', andaza 'Maass*,
aber noch arab. muhandis Teldmesser , handasat ^Geometrie'*^),
talm. Dn;n, niil er mass' Lag. A. Stud.; andam *Glied
(5. Jhd.) = np. andam *Glied', auch 'Symmetric' (= Gliede^
rung ), ab er noch arab. hadama^) zerstSrte, handam *Sym-
*J Neben hangatn , hangama 1) tempus, 2) conventus fiihrt
Yullers auoh angam^ angHma an.
^) Yom Arab, zunaohst aua dem Syrisohen entlehnt.— 217 —

=== HUB 530-540
spielen*, bdzi 'Spiel' zu geh5ren, sondern kann z. B.
zu skr. bhaj *Antheil geben, Antheil erhalten' (vgl.
'bhdjin theilhaftig*), zd. baz 'zutheilen* gehoren. Das
anlautende an- ist regelrecht aus ap. ham vor Ver-
schlusslauten entstanden (siehe den zweiten Theil
unter m),
114. Hier fehlt zd. hanjamana- *Versammlung'.
115. Trotz Horn's Hinweis auf ctdan = Wnmeln, lesen,
pflticken, schneiden' lasst sich anjtdan, pr. anfinam
(Sal. Shuk. p. 53) 'zersehneiden, zerstiickeln' (vgl.
anjan-tdan *findere') init skr. sam-ci *aufschichten, zu-
sammenlegen, ansammeln' nur schwer vereinigen. Phi.
andUan 'krunimen' habe ich friiher zu skr. anc *biegen'
```


## [2026-09-14T02:02:02.332Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (47,48,49):\n    print('==== leaf',i); print(t[i][:3000]); print()\nEOF",
 "description": "Horn pages 26-28"
}
```


### [2026-09-14T02:02:03.424Z] TOOL RESULT

```
==== leaf 47
— 26 —
109. iimed ^Hoffnung, umimd, ömed, vergl. ^utunted.
phlv. nmet bezw. ö)net (auch auf einer Gemme, Hörn,
Mitteilungen, Heft IV, S. 38), ömeivar (vd. 3, 32), vergl.
(inömet,
LW. kurd. umäd, umld; af/. umed; bei. tumned, n.
ömBS (281).
ai. *ava -;- l^may- einsenken*, vergl. methi- ^Pfeiler,
Pfosten (?). Dazu auch bei. s. nük aufgerichtet'
(Bartholomae, ZDMG. 44, 553).
110. enhäz^) 'Genosse, Gemahl, Gemahlin, lumbäz.
Ursprünglich *Spielgenosse*, statt *henwaz? Dann
vergl. np. hä/ten (No. 150).
111. enhästen^) 'anfüllen, anhäufen', Praes. enbär-em,
enhärden, enbär^).
aw. hqm -\- l^par-^ hampäfraiti 'er mästet*; phlv.
anhüstan anhäufen', anhar , anbar(i)sn , anh(ä)rok\pat
(Gemme), arm. LW. awbar, hamhar (davon hambarem),
hambarakapet; ai. sam-r- V^par-.
112. enhoylden>^) 'duften'.
aw. hqm+V^bud', skr. sam -\- [^budh- , allerdings
nur in der Bedeutung wahrnehmen, merken*.
113. en^äm 'Ende', enjamlden, vergl. ferjam,
ap. *hanjäma' 'Ende, Abschluss' ; aw. vergl. henjas-
ente sie (die Conten) werden abgeschlossen* (Geld n er
Studien I, 5) ; phlv. anjam, anjamimtan (Bund.), bezw.
han-.
Die augenscheinlich sekundäre Bildung enjäften
'beendigen* (vergl. ferjaften) findet sich nur in der
jüd.-pers. Bibelübersetzung (jnSNÜN Is. 16, 4, ^:^nSNJ:N
Is. 10, 22).
114. erCßumen 'Versammlung*.
ap. *hanjamana-; phlv. hanjaman bezw. anjaman;
vergl. mand. LW. JN0''K'3Nn (Nöldeke, Mand. Gr.
305), syr. LW. JOOT (de Lagarde, Ges. Abh. 40),
Siehe vorhergehende Seite Note 1.
^) Die Wörterbücher überliefern auch die Form enpästen.

==== leaf 48
— 27 —
arab. LW. hinzamn 'Menschenmenge' (de Lagaide,
Armen. Studien, No. 1235).
115. en^lden zerschneiden, zerstückeln', Praes. enjln-em,
ap. *Aam + [/cay- (aw. und ai. 'zusammenlegen,
ansammeln etc.') ; phlv. ancUan bezw. han- , anj-
^krümmen, zusammenziehen (Bund.).
Zu dem Bedeutungs Wechsel vergl. np. ciden 'sam-
meln; schneiden'.
116. end *so viel, einige'; vergl. endek, endi, bes]end.
phlv. and 'so, so viel', andak Venig',
kurd. hind 'so viel', hindik 'wenig'.
Vom Pronominalstamm er-, aber nicht gleich aw.
avant-, phlv. havand, vd. 15 (48).
117. endäyiten * werfen', Praes. endäz-em, endaz 'Plan,
Absicht', endüze 'Mass'.
phlv. andäytan 'werfen'; sinnen* (Bund.), andäcak
*Mass', andäöUan erwägen , ermessen', andäc(i)sn
'Meinung ; arm. LW. amiacem 'überlegen', arab. LW.
muhandis 'Feldmesser', hmdasat 'Geometrie' u. a. m.
(de Lagarde, Arm. Stud., No. 116).
aw. hqm + {/^tac- ; Bedeutungswechsel wie auch bei
np. perdä/ten (No. 286).
118. endäm 'Körper, Glied'.
aw. hondäma- 'Glied' ; phlv. andäm, arm. LW. andam.
119. {i)ender 'm\ vergl. enderün,
ap. a(n)tar 'in, innerhalb'; aw. antare; phlv. andar^);
ai. antdr; arm. vergl. ender/c, ^nterk 'Eingeweide'
(H. No. 109).
Steht enderün für enderän (zu ün für an vergl. gerdün
No. 904), wozu man z. B. Sahn. I, 61 Vers 525 ver-
gleiche 2)? Vergl. jNTD, Ps. 68, 7, 8 (Grill).
120. {2)'ender in peder\euder {ped]ender), mader]ender
{mäd\ender)^ beräder]ender, /'aher]ender etc. 'Stief-'.
skr. antard' 'anderer, verschieden von'; osset. ändär
'andere, fremd' (20); got. anpar; lit. antras.
^) Phlv. andarg ist Unsinn.
') Das Pehlevi hat auch schon andarün (für aw. aw/ara-).

==== leaf 49
- 28 -
Die Etymologie stammt von Nöldeke (mündliche
Mitteilung).
121. enderyiur, der^ur (früher: ender /^r) ^passend, an-
gemessen, ender/iird, der/urd, ender/urden ^) (Sahn.
I, 79 Vers 318).
Nöldeke schlägt vor (mündliche Mitteilung), die
Worte an [/^svar- *glänzen anzuschliessen.
122. endöyiteu 'sammeln, erwerben', Praes. endöz-em,
endö/is'^),
phlv. andö/tan, andöcet sammeln, erwerben* (Men.,
AV.).
Siehe unter np. tö/ten (No. 462).
123. euffärden ^glauben, wähnen*, engüsten, Praes. enrjär-
em, engäris^ engäre 'Rechnungsbuch'.
Käs. engöstdn sprechen' (s. v. herf zeden),
aw. hanlcärat/emi j hankere&a-, hankereti- 'Zählung'
(Geldner, KZ. 27. 239 Note 1); phlv. angärtan,
angärttan glauben, zählen' (Men., AV.); ai. 2 i^kar-
gedenken' (?).
oss. d. analuHj aüyalim ^meinen, glauben', t. änqül-
dän *ich vermute* (25); af/. angeral 'denken, sich
einbilden'; kurd. LW. angerin; arm. LW. angarem
'halten für; georg. und Thusch LW. angarisi bezw.
angris 'Rechenschaft' (Hüb seh mann, Osset. Etym.
No. 25)3).
^) Impersonalo.
*) Nur aus einem Verse des fragwürdigen AbuM Ma*änl belegt,
was im Grunde nicht yiel sagen will. Eine andere solche *ünform* ist
phlv. ämöxt(i)sn (aw. äxsö^ y. 45, 2).
^) Über das gr. LW. ayyaoo; ist schon so viel Falsches geschrieben
worden (erst ganz kürzlich hat noch 8. Bugge, BB. 14, 62, ausser
ai. ähgira-, dugiras- und gr. nyyfXo? sogar lat. amhuläre dazu gestellt und
Ceci, Appunti Glottologi, No. 8, vergl. Indog. Forsch. I, Anzeiger 2,
158, ist ihm darin gefolgt), dass es am Platze sein dürfte, hier kurz
auf das Wort einzugehen. Als Grundbedeutung giebt Hesych fQyartjg,
vntjQFTtjZt ax^oifooot; an; arjfjL<xCvfi Sf. xai rov: fx SiwJo^f]'^ ßaaiXixovg yQa/u-
juaTofpogov^. Suidas hat nur die letzte Bedeutung mit dem Hinzufügen
ol (Vf nvToi xai aaiaV^Ti« (lies aaydvdai); vergl. auch Herod. VIII, 98
Tovro To SQuat^jua twv InntJoy xaXh'ovai U^^nai ayyixQiliov, Dazu ayya()fvu)
```


## [2026-09-14T02:02:17.946Z] TOOL CALL #43: Bash

```json
{
 "command": "sed -n '1,40p' tools/fetch_source.py",
 "description": "Inspect fetch_source tool"
}
```


### [2026-09-14T02:02:17.993Z] TOOL RESULT

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


## [2026-09-14T02:02:24.936Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%D9%85%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%DB%8C%D8%AE%D8%AA%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D9%87\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%B1%D8%B2\" \\\n \"https://en.wiktionary.org/wiki/%D9%87%D9%86%DA%AF%D8%A7%D9%85\" ; do\n python3 tools/ref_page.py --help >/dev/null 2>&1\n python3 tools/fetch_source.py \"$u\" --note \"page 442, root Sem 1/Sm: Persian reflexes of ham- compounds\" 2>&1 | tail -2\ndone",
 "description": "Archive Wiktionary Persian pages"
}
```


### [2026-09-14T02:02:29.267Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9941fcb1494b3692.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cbdfcf1655b6ddf9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e3eb396112c7ab3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d7af55838b31c7bb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3a3797668acf932e.txt
```


## [2026-09-14T02:02:33.289Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 9941fcb1494b3692 cbdfcf1655b6ddf9 1e3eb396112c7ab3 d7af55838b31c7bb 3a3797668acf932e; do\necho \"=========== $f\"\npython3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('Persian')\n# print etymology sections\nfor m in re.finditer(r'Etymology', t):\n    print(t[m.start():m.start()+700].replace('\\n',' '))\n    print('  ---')\nEOF\ndone 2>&1 | head -120",
 "description": "Extract etymology sections"
}
```


### [2026-09-14T02:02:34.715Z] TOOL RESULT

```
=========== 9941fcb1494b3692
Etymology    2.2   Noun    2.2.1   Derived terms    2.2.2   Descendants    2.3   Further reading    3   Persian    Toggle Persian subsection    3.1   Etymology    3.2   Pronunciation    3.3   Noun    3.3.1   Inflection    3.3.2   Descendants    4   Urdu    Toggle Urdu subsection    4.1   Etymology    4.2   Pronunciation    4.3   Noun    4.3.1   Declension    4.4   References    4.5   Further reading    Toggle the table of contents    انجمن    10 languages    বাংলা   فارسی   Na Vosa Vakaviti   Bahasa Indonesia   Kurdî   Malagasy   پښتو   Русский   سرائیکی   اردو    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Ed
  ---
Etymology    3.2   Pronunciation    3.3   Noun    3.3.1   Inflection    3.3.2   Descendants    4   Urdu    Toggle Urdu subsection    4.1   Etymology    4.2   Pronunciation    4.3   Noun    4.3.1   Declension    4.4   References    4.5   Further reading    Toggle the table of contents    انجمن    10 languages    বাংলা   فارسی   Na Vosa Vakaviti   Bahasa Indonesia   Kurdî   Malagasy   پښتو   Русский   سرائیکی   اردو    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened U
  ---
Etymology    4.2   Pronunciation    4.3   Noun    4.3.1   Declension    4.4   References    4.5   Further reading    Toggle the table of contents    انجمن    10 languages    বাংলা   فارسی   Na Vosa Vakaviti   Bahasa Indonesia   Kurdî   Malagasy   پښتو   Русский   سرائیکی   اردو    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From
  ---
Etymology  [ edit ]    Borrowed from Persian انجمن ( anjoman , “ meeting, assembly ” ) , from Middle Persian 𐭧𐭭𐭰𐭬𐭭 ( hanjaman , “ congregation, assembly, community ” ) , itself from Avestan 𐬵𐬀𐬧𐬘𐬀𐬨𐬀𐬥𐬀 ( haṇjamana , “ assembly ” ) .   Noun  [ edit ]    انجمن • ( encümen ) ( definite accusative انجمنی ( encümeni ) , plural انجمنلر ( encümenler ) )    society , association , club , circle , a group of people who meet to engage in a common interest   Synonyms: جمعیت ( cemʼiyet ) , محفل ( mahfil )    convocation , assembly , meeting , reunion , any gathering of persons for a specific purpose   Synonyms: اجتماع ( ictimaʼ ) , جمعیت ( cemʼiyet ) , درنك ( dernek ) , مجلس ( meclis ) , محفل ( mahfil )  
  ---
Etymology  [ edit ]    From Middle Persian 𐭧𐭭𐭰𐭬𐭭 ( hanjaman , “ congregation, assembly, community ” ) , from Avestan 𐬵𐬀𐬧𐬘𐬀𐬨𐬀𐬥𐬀 ( haṇjamana , “ assembly ” ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔan.d͡ʒu.ˈman/    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒʊ.mán]    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒʊ.mán]   ( Kabuli ) IPA ( key ) : [ʔän.d͡ʒʊ.mán]    ( Hazaragi ) IPA ( key ) : [ʔän.d͡ʒu.mán]    ( Iran, formal ) IPA ( key ) : [ʔæn.d͡ʒo.mǽn]    ( Tajik, formal ) IPA ( key ) : [ʔän.d͡ʒu.mán]    Rhymes: -an    Readings   Classical reading ?    anjuman   Dari reading ?    anjuman   Iranian reading ?    anjoman   Tajik reading ?    anjuman   Noun  [ edit ]    انجمن • (
  ---
Etymology  [ edit ]    Borrowed from Classical Persian انجمن ( anjuman , “ meeting, assembly ” ) . First attested in c. 1564 as Middle Hindi انجمن ( anjmn /⁠anjuman⁠/ ) . [ 1 ]    Pronunciation  [ edit ]    ( Standard Urdu ) IPA ( key ) : /ən.d͡ʒʊ.mən/    Rhymes: -ən    Hyphenation: اَنْ‧جُ‧مَنْ    Noun  [ edit ]    اَنْجُمَنْ • ( anjuman )  f ( Hindi spelling अंजुमन )    meeting , assembly , gathering   Synonym: مَحْفِل ( mahfil )   1981 , “ دل چیز کیا ہے آپ مری جان لیجئے ”, in Akhlaq Mohammed Khan (lyrics), Mohammed Zahur Khayyam (music), Umrao Jaan , performed by Asha Bhosle : اس انجمن میں آپ کو آنا ہے بار بار is anjuman mẽ āp ko ānā hai bār bār You will have to come again and again to th
  ---
=========== cbdfcf1655b6ddf9
=========== 1e3eb396112c7ab3
Etymology    1.2   Pronunciation    1.3   Noun    1.3.1   Derived terms    1.3.2   Descendants    1.4   References    Toggle the table of contents    اندوه    5 languages    فارسی   Kurdî   Malagasy   Bahasa Melayu   Türkçe    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Persian  [ edit ]   
  ---
Etymology  [ edit ]    Inherited from Middle Persian [script needed] ( ’ndwh /⁠andōh⁠/ , “ sorrow ” ) . Noun form of the verb اندوهیدن .    Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔan.ˈdoːh/    ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪oːʱ]    ( Dari, formal ) IPA ( key ) : [ʔän̪.d̪oːʱ]   ( Kabuli ) IPA ( key ) : [ʔän̪.d̪oː]    ( Hazaragi ) IPA ( key ) : [ʔän̪.d̪ʊː]    ( Iran, formal ) IPA ( key ) : [ʔæn̪.d̪uːʱ]    ( Tajik, formal ) IPA ( key ) : [ʔän̪.d̪ɵʰ]    Rhymes: -oːh    Readings   Classical reading ?    andōh   Dari reading ?    andōh   Iranian reading ?    anduh   Tajik reading ?    andüh   Noun  [ edit ]    اندوه • ( andōh / anduh ) ( Tajik spelling андӯҳ )    s
  ---
=========== d7af55838b31c7bb
=========== 3a3797668acf932e
Etymology    1.2   Pronunciation    1.3   Noun    1.3.1   Derived terms    1.3.2   Descendants    1.3.3   References    Toggle the table of contents    هنگام    5 languages    فارسی   Magyar   Kurdî   Malagasy   Русский    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance   move to sidebar   hide    From Wiktionary, the free dictionary   Persian  [ edit ]    Ety
  ---
Etymology  [ edit ]    From Middle Persian [script needed] ( hngʾm /⁠hangām⁠/ , “ time, occasion ” ) ; by surface analysis , هن ( han , “ alternative form of همـ ( ham- , “ co- ” ) ” ) +‎ گام ( gām , “ step ” ) . [ 1 ] Akin to Old Armenian հանգամանք ( hangamankʻ , “ details, circumstances, way ” ) , an Iranian borrowing.   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /han.ˈɡaːm/    ( Dari, formal ) IPA ( key ) : [häŋ.ɡɑːm]    ( Dari, formal ) IPA ( key ) : [häŋ.ɡɑːm]   ( Kabuli ) IPA ( key ) : [ʔäŋ.ɡɑːm]    ( Hazaragi ) IPA ( key ) : [ʔäŋ.ɡɔːm]    ( Iran, formal ) IPA ( key ) : [hæŋ.ɡɒːm] , [heŋ.ɡɒːm]    ( Tajik, formal ) IPA ( key ) : [häŋ.ɡɔm]    Rhymes: -aːm    Readings 
  ---
```


## [2026-09-14T02:02:44.342Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sem-\" \\\n \"https://en.wiktionary.org/wiki/%CF%83%CF%8D%CE%BD\" \\\n \"https://en.wiktionary.org/wiki/%E1%BD%81%CE%BC%CF%8C%CF%82\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AF%D9%86\" \\\n \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%D8%A7%D9%85\" \\\n \"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D8%A7%D9%88%D8%B1\" \\\n \"https://en.wiktionary.org/wiki/samovar\" \\\n \"https://www.etymonline.com/word/samovar\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 442, root Sem 1/Sm (PIE *sem-): checking node forms\" 2>&1 | tail -1\ndone",
 "description": "Archive more sources"
}
```


### [2026-09-14T02:02:49.937Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/00537653f130356c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/63a9551438c4964d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/5549d700561e59d6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/843aa331f5d79bba.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2be1bee953011c4b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d70a48d9b09bcd65.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ac7ccb998e11d40d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0f44bdb2d71f209a.txt
```


## [2026-09-14T02:02:54.310Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in 00537653f130356c 63a9551438c4964d 5549d700561e59d6 843aa331f5d79bba 2be1bee953011c4b d70a48d9b09bcd65 ac7ccb998e11d40d 0f44bdb2d71f209a; do\necho \"=========== $f\"\npython3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\nms=list(re.finditer(r'Etymology\\s*\\[ edit \\]', t))\nfor m in ms[:3]:\n    print(t[m.start():m.start()+900].replace('\\n',' '))\n    print('  ---')\nif not ms:\n    print(t[:1200].replace('\\n',' '))\nEOF\ndone 2>&1 | head -150",
 "description": "Extract etymologies from archived pages"
}
```


### [2026-09-14T02:02:55.833Z] TOOL RESULT

```
=========== 00537653f130356c
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sem- FETCHED: 2026-09-14T01:59:54Z STATUS: 200 TITLE: Reconstruction:Proto-Indo-European/sem- - Wiktionary, the free dictionary  Reconstruction:Proto-Indo-European/sem- - Wiktionary, the free dictionary    Jump to content    Main menu    Main menu   move to sidebar   hide    Navigation   Main page   Community portal   Requested entries   Recent changes   Random entry   Help   Glossary   Contact us   Special pages    Search    Search    Appearance    Donations    Create account    Log in    Personal tools    Donations    Create account    Log in    Contents   move to sidebar   hide    Beginning   1   Proto-Indo-European    Toggle Proto-Indo-European subsection    1.1   Root    1.1.1   Derived terms    1.2   References    1.3   Further reading    Toggle the table of contents    Reconstruction:Proto-Indo-European/ sem-    Add languages    Reconstruction    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Get shortened URL    Prin
=========== 63a9551438c4964d
Etymology  [ edit ]    Homeric and Old Attic ξῠ́ν ( xŭ́n ) and Mycenaean Greek 𐀓𐀱 ( ku-su /⁠*ksun⁠/ ) point to Proto-Hellenic *ksún ; further origin uncertain.   The dative that this preposition governs continues the PIE comitative-instrumental.   Pronunciation  [ edit ]    IPA ( key ) : /sýn/ → /ˈsyn/ → /ˈsin/    ( 5 th BCE Attic ) IPA ( key ) : /sýn/    ( 1 st CE Egyptian ) IPA ( key ) : /ˈsyn/    ( 4 th CE Koine ) IPA ( key ) : /ˈsyn/    ( 10 th CE Byzantine ) IPA ( key ) : /ˈsyn/    ( 15 th CE Constantinopolitan ) IPA ( key ) : /ˈsin/    Preposition  [ edit ]    σῠ́ν • ( sŭ́n ) ( governs the dative )    beside ; with    Usage notes  [ edit ]    In compounds it has similar connotations, such as completeness and/or simultaneity.   Derived terms  [ edit ]    μετᾰξῠ́ ( metăxŭ́ )   ξῠνός ( xŭnós )   σῠν- ( sŭn- )    Descendants  [ edit ]    Greek: συν ( syn )    Yevanic: שִׁין ( šin )    
  ---
=========== 5549d700561e59d6
Etymology  [ edit ]    From Proto-Hellenic *homós , from Proto-Indo-European *somHós ( “ same, alike ” ) . Cognate with εἷς ( heîs , “ one ” ) , as well as Old English sama ( English same ), Sanskrit सम ( sama ) , Old Persian 𐏃𐎶 ( hama ) , Old Church Slavonic самъ ( samŭ ) . [ 1 ]    Pronunciation  [ edit ]    IPA ( key ) : /ho.mós/ → /oˈmos/ → /oˈmos/    ( 5 th BCE Attic ) IPA ( key ) : /ho.mós/    ( 1 st CE Egyptian ) IPA ( key ) : /(h)oˈmos/    ( 4 th CE Koine ) IPA ( key ) : /oˈmos/    ( 10 th CE Byzantine ) IPA ( key ) : /oˈmos/    ( 15 th CE Constantinopolitan ) IPA ( key ) : /oˈmos/    Adjective  [ edit ]    ὁμός • ( homós )  m ( feminine ὁμή , neuter ὁμόν ) ; first / second declension    same , common , joint    Declension  [ edit ]    First and second declension of ὁμός ; ὁμή ; ὁμόν ( Attic )   Number   Singular   Dual   Plural   Case/Gender   Masculine   Feminine   Neuter   Mas
  ---
=========== 843aa331f5d79bba
URL: https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AF%D9%86 FETCHED: 2026-09-14T02:02:47Z STATUS: 200 TITLE: اندودن - Wiktionary, the free dictionary  اندودن - Wiktionary, the free dictionary    Jump to content    Main menu    Main menu   move to sidebar   hide    Navigation   Main page   Community portal   Requested entries   Recent changes   Random entry   Help   Glossary   Contact us   Special pages    Search    Search    Appearance    Donations    Create account    Log in    Personal tools    Donations    Create account    Log in    Contents   move to sidebar   hide    Beginning   1   Persian    Toggle Persian subsection    1.1   Pronunciation    1.2   Verb    1.2.1   Derived terms    Toggle the table of contents    اندودن    5 languages    فارسی   Magyar   Kurdî   Malagasy   Русский    Entry    Discussion    English    Read    Edit    View history    Tools    Tools   move to sidebar   hide    Actions   Read    Edit    View history    General   What links here   Related changes   Upload file   Permanent link   Page information   Cite this page   Get shortened URL    Print/export   Create a book   Download as PDF   Printable version    In other projects   Appearance
=========== 2be1bee953011c4b
Etymology  [ edit ]    Borrowed from Classical Persian اَنجام ( anjām ) .   Noun  [ edit ]    انجام • ( anjām )  m    end , conclusion , outcome    tip , extremity    Persian  [ edit ]    Etymology  [ edit ]    From Middle Persian [Term?] ( /⁠hanǰām⁠/ , “ end, completion, outcome ” ) , from Old Persian [script needed] ( *hanǰāma- , “ end, conclusion ” ) , from Proto-Iranian *ham- + *gam ( “ to come ” ) , ultimately from Proto-Indo-European *gʷem- ( “ to go, stand ” ) . Compare Sanskrit संगम ( saṃgama ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔan.ˈd͡ʒaːm/    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒɑːm]    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒɑːm]   ( Kabuli ) IPA ( key ) : [ʔän.d͡ʒɑːm]    ( Hazaragi ) IPA ( key ) : [ʔän.d͡ʒɔːm]    ( Iran, formal ) IPA ( key ) : [ʔæn.d͡ʒɒːm]    ( Tajik, formal ) IPA ( key ) : [ʔän.d͡ʒɔm]    Rhymes: -aːm    Readings   Classical 
  ---
Etymology  [ edit ]    From Middle Persian [Term?] ( /⁠hanǰām⁠/ , “ end, completion, outcome ” ) , from Old Persian [script needed] ( *hanǰāma- , “ end, conclusion ” ) , from Proto-Iranian *ham- + *gam ( “ to come ” ) , ultimately from Proto-Indo-European *gʷem- ( “ to go, stand ” ) . Compare Sanskrit संगम ( saṃgama ) .   Pronunciation  [ edit ]    ( Classical Persian ) IPA ( key ) : /ʔan.ˈd͡ʒaːm/    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒɑːm]    ( Dari, formal ) IPA ( key ) : [ʔän.d͡ʒɑːm]   ( Kabuli ) IPA ( key ) : [ʔän.d͡ʒɑːm]    ( Hazaragi ) IPA ( key ) : [ʔän.d͡ʒɔːm]    ( Iran, formal ) IPA ( key ) : [ʔæn.d͡ʒɒːm]    ( Tajik, formal ) IPA ( key ) : [ʔän.d͡ʒɔm]    Rhymes: -aːm    Readings   Classical reading ?    anjām   Dari reading ?    anjām   Iranian reading ?    anjâm   Tajik reading ?    anjom   Noun  [ edit ]    Dari   انجام    Iranian Persian   Tajik   анҷом    انجام • ( anjâm 
  ---
Etymology  [ edit ]    Borrowed from Classical Persian انجام ( anjām ) , from Middle Persian [script needed] ( hanǰām , “ end, completion, outcome ” ) .   Pronunciation  [ edit ]    ( Standard Urdu ) IPA ( key ) : /ən.d͡ʒɑːm/    Audio ( Pakistan ) : ( file )    Rhymes: -ɑːm    Noun  [ edit ]    اَن٘جام • ( añjām )  m ( Hindi spelling अंजाम )    end , finishing    result , conclusion   اس کا انجام ٹھیک نہیں ہو گا۔ is kā añjām ṭhīk nahī̃ ho gā The result of it won't be right.    Declension  [ edit ]    Declension of انجام    singular   plural   direct   اَن٘جام ( añjām )    اَن٘جام ( añjām )    oblique   اَن٘جام ( añjām )    اَن٘جاموں ( añjāmõ )    vocative   اَن٘جام ( añjām )    اَن٘جامو ( añjāmo )    References  [ edit ]    Platts, John T. ( 1884 ), “ انجام ”, in A dictionary of Urdu, classical Hindi, and English , London: W. H. Allen & Co.    Ushojo  [ edit ]    Etymology  [ edit ]    F
  ---
=========== d70a48d9b09bcd65
Etymology  [ edit ]    From Russian самова́р ( samovár , “ self-boiler ” ) ; from само́ ( samó , “ self ” ) + вари́ть ( varítʹ , “ to boil; to cook ” ) .   Apparently mediated or influenced by Persian سماور ( samâvar , “ samovar ” ) .   Noun  [ edit ]    سماور • ( semaver )    samovar    Descendants  [ edit ]    Turkish: semaver    Persian  [ edit ]    Persian Wikipedia has an article on: سماور    Wikipedia fa    Etymology  [ edit ]    From Russian самова́р ( samovár ) , literally “self-boiler”; from само́ ( samó ) “self” + вари́ть ( varítʹ ) “to boil” or “to cook”. Northern Luri سںمۋںر ( səmüər ) .   Noun  [ edit ]    سماور • ( samâvar )    samovar    Retrieved from " https://en.wiktionary.org/w/index.php?title=سماور&oldid=92048204 "   Categories : Ottoman Turkish terms borrowed from Russian   Ottoman Turkish terms derived from Russian   Ottoman Turkish lemmas   Ottoman Turkish nouns   
  ---
Etymology  [ edit ]    From Russian самова́р ( samovár ) , literally “self-boiler”; from само́ ( samó ) “self” + вари́ть ( varítʹ ) “to boil” or “to cook”. Northern Luri سںمۋںر ( səmüər ) .   Noun  [ edit ]    سماور • ( samâvar )    samovar    Retrieved from " https://en.wiktionary.org/w/index.php?title=سماور&oldid=92048204 "   Categories : Ottoman Turkish terms borrowed from Russian   Ottoman Turkish terms derived from Russian   Ottoman Turkish lemmas   Ottoman Turkish nouns   Persian terms derived from Russian   Persian lemmas   Persian nouns    Hidden categories: Pages with entries   Pages with 2 entries   Persian undefined derivations    This page was last edited on 17 August 2026, at 06:07.   Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Po
  ---
=========== ac7ccb998e11d40d
Etymology  [ edit ]    From Russian самова́р ( samovár , “ self-boiler ” ) ; from само́ ( samó , “ self ” ) + вари́ть ( varítʹ , “ boil, cook ” ) .   Pronunciation  [ edit ]    IPA ( key ) : /ˈsæməvɑː(ɹ)/ , /ˌsæməˈvɑː(ɹ)/    Audio ( US ) : ( file )    Noun  [ edit ]    samovar ( plural samovars )    A metal urn with a spigot , for boiling water for making tea. Traditionally, the water is heated by hot coals or charcoal in a chimney-like tube which runs through the center of the urn. Today, it is more likely that the water is heated by an electric coil.  1901 [ 1878 ], chapter 25, in Constance Garnett , transl., Anna Karenina ‎ [1] , translation of Анна Каренина ( Anna Karenina ) by Leo Tolstoy , part 3: The samovar was beginning to sing; the laborers and the family, having disposed of the horses, came in to dinner.    1919 , Ronald Firbank , Valmouth , hardback edition, Duckworth, page 1
  ---
Etymology  [ edit ]    Borrowed from Russian самова́р ( samovár ) .   Pronunciation  [ edit ]    Audio ( Baku ) : ( file )    Hyphenation: sa‧mo‧var    Noun  [ edit ]    samovar ( definite accusative samovarı , plural samovarlar )    samovar    Declension  [ edit ]    Declension of samovar    singular   plural   nominative  samovar samovarlar    definite accusative  samovarı samovarları    dative  samovara samovarlara    locative  samovarda samovarlarda    ablative  samovardan samovarlardan    definite genitive  samovarın samovarların    Possessive forms of samovar    nominative   singular   plural   mənim ( “ my ” )    samovarım    samovarlarım    sənin ( “ your ” )    samovarın    samovarların    onun ( “ his/her/its ” )    samovarı    samovarları    bizim ( “ our ” )    samovarımız    samovarlarımız    sizin ( “ your ” )    samovarınız    samovarlarınız    onların ( “ their ” )    sam
  ---
Etymology  [ edit ]    Borrowed from Russian самова́р ( samovár ) . By surface analysis , samo- ( “ self- ” ) +‎ vařit ( “ to boil ” ) .   Pronunciation  [ edit ]    IPA ( key ) : [ˈsamovar]    Rhymes: -ovar    Hyphenation: sa‧mo‧var    Noun  [ edit ]    samovar   m   inan ( diminutive samovárek )    samovar ( metal urn used to make tea )   Coordinate terms: čajovar , kávovar    Declension  [ edit ]    Declension of samovar ( hard masculine inanimate )   singular   plural   nominative   samovar    samovary    genitive   samovaru    samovarů    dative   samovaru    samovarům    accusative   samovar    samovary    vocative   samovare    samovary    locative   samovaru    samovarech    instrumental   samovarem    samovary    Further reading  [ edit ]    “ samovar ”, in Příruční slovník jazyka českého (in Czech), 1935–1957    “ samovar ”, in Slovník spisovného jazyka českého (in Czech), 1960
  ---
=========== 0f44bdb2d71f209a
URL: https://www.etymonline.com/word/samovar FETCHED: 2026-09-14T02:02:49Z STATUS: 200 TITLE: Samovar - Etymology, Origin & Meaning  Samovar - Etymology, Origin & Meaning    Search   Log in    Columns   Forum   Apps   Premium    Log in    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z    Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.   About  Who Did This   Sources   Introduction   Links    Support  Premium   Patreon   Donate with PayPal   Merch    Apps  Get Chrome Extension   Get iOS App   Get Android App    Dark  Auto  Light   Terms of Services Privacy Policy    English (English)   © 2001–2026 Douglas Harper & Talia Felix    Advertisement Remove Ads   Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.   Origin and history of samovar    samovar (n.)    "copper urn, used in Russia and nearby regions, in which water is kept boiling for use as needed in making tea," 1830, from Russian samovar , literally "self-boiler," from sam "self" (from PIE root *sem- (1) "one; as one, together with") + varit "to boil" (from Old Church Slavonic variti "to cook," from PIE root *wer- "to burn"); but this i
```


## [2026-09-14T02:03:09.679Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\npython3 - <<'EOF'\nt=open('0f44bdb2d71f209a.txt',encoding='utf-8').read()\ni=t.find('samovar (n.)')\nprint(t[i:i+1400].replace('\\n',' '))\nEOF\necho \"=== angixtan file\"; grep -o \"Etymology.\\{0,400\\}\" cbdfcf1655b6ddf9.txt | head -3\necho \"=== andarz file\"; grep -o \"Persian.\\{0,600\\}\" d7af55838b31c7bb.txt | head -3",
 "description": "Read etymonline samovar and check empty pages"
}
```


### [2026-09-14T02:03:11.364Z] TOOL RESULT

```
samovar (n.)    "copper urn, used in Russia and nearby regions, in which water is kept boiling for use as needed in making tea," 1830, from Russian samovar , literally "self-boiler," from sam "self" (from PIE root *sem- (1) "one; as one, together with") + varit "to boil" (from Old Church Slavonic variti "to cook," from PIE root *wer- "to burn"); but this is perhaps folk-etymology if the word is from Tatar sanabar "tea-urn."  also from 1830    Entries linking to samovar    *sem- (1)    Proto-Indo-European root meaning "one; as one, together with."   It might form all or part of: anomalous ; anomaly ; assemble ; assimilate ; ensemble ; facsimile ; fulsome ; hamadryad ; haplo- ; haploid ; hendeca- ; hendiadys ; henotheism ; hetero- ; heterodox ; heterosexual ; homeo- ; homeopathy ; homeostasis ; homily ; homo- (1) "same, the same, equal, like;" homogenous ; homoiousian ; homologous ; homonym ; homophone ; homosexual ; hyphen ; resemble ; same ; samizdat ; samovar ; samsara ; sangha ; Sanskrit ; seem ; seemly ; semper- ; sempiternal ; similar ; simple ; simplex ; simplicity ; simulacrum ; simulate ; simulation ; simultaneous ; single ; singlet ; singular ; some ; -some (1); -some (2); verisimilitude .   It might also be the source of: Sanskrit sam "together," samah "even, level, similar, identical;" Avestan hama "similar, the same;" Greek hama "together with, at the same time," hom
=== angixtan file
=== andarz file
```


## [2026-09-14T02:03:18.528Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nwc -c cbdfcf1655b6ddf9.txt d7af55838b31c7bb.txt; head -c 600 d7af55838b31c7bb.txt; echo; echo ---; head -c 600 cbdfcf1655b6ddf9.txt",
 "description": "Inspect the two empty-looking files"
}
```


### [2026-09-14T02:03:18.593Z] TOOL RESULT

```
10419 cbdfcf1655b6ddf9.txt
  156 d7af55838b31c7bb.txt
10575 total
URL: https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D8%B1%D8%B2
FETCHED: 2026-09-14T02:02:28Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found
---
URL: https://en.wiktionary.org/wiki/%D8%A7%D9%86%DA%AF%DB%8C%D8%AE%D8%AA%D9%86
FETCHED: 2026-09-14T02:02:27Z
STATUS: 200
TITLE: انگیختن - Wiktionary, the free dictionary

انگیختن - Wiktionary, the free dictionary 

 Jump to content 

 Main menu 

 Main menu

 move to sidebar 
 hide 

 Navigation

 Main page 
 Community portal 
 Requested entries 
 Recent changes 
 Random entry 
 Help 
 Glossary 
 Contact us 
 Special pages 

 Search 

 Search 

 Appearance 

 Donations 

 Create account 

 Log in 

 Personal tools 

 Donations 

 Create account 

 Log in 

 Contents

 move to sid
```


## [2026-09-14T02:03:21.228Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -o \"Persian \\[ edit \\].\\{0,900\\}\" cbdfcf1655b6ddf9.txt | head -2",
 "description": "Persian section of angixtan"
}
```


### [2026-09-14T02:03:22.313Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:03:23.355Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/syn-\" \"https://www.etymonline.com/word/sincere\" \"https://www.etymonline.com/word/symbol\" \"https://www.etymonline.com/word/seem\" \"https://www.etymonline.com/word/same\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 442, root Sem 1/Sm: Greek syn- and Latin/Germanic reflexes\" 2>&1|tail -1; done",
 "description": "Archive etymonline pages"
}
```


### [2026-09-14T02:03:25.923Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a63d3195e5c3542c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b7809040cea698f0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3210bc26b0a72135.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cad53ff4b8c52162.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e2c67a696bafbc83.txt
```


## [2026-09-14T02:03:29.236Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in a63d3195e5c3542c b7809040cea698f0 3210bc26b0a72135 cad53ff4b8c52162 e2c67a696bafbc83; do\necho \"==== $f\"\npython3 - \"$f.txt\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1],encoding='utf-8').read()\ni=t.find('Origin and history of')\nprint(t[i:i+900].replace('\\n',' '))\nEOF\ndone",
 "description": "Read etymonline entries"
}
```


### [2026-09-14T02:03:30.600Z] TOOL RESULT

```
==== a63d3195e5c3542c
Origin and history of syn-    syn-    word-forming element of Greek origin (corresponding to Latin con- ) meaning "together with, jointly; alike; at the same time," also sometimes completive or intensive, from Greek syn (prep.) "with, together with, along with, in the company of," from PIE *ksun- "with" (source also of Russian so- "with, together," from Old Russian su(n)- ).   The Greek prefix was assimilated to -l- , reduced to sy- before -s- and -z- , and altered to sym- before -b- , -m- and -p- . Very productive from c. 1860 in forming words for modern sciences. Since 1970s also with a sense of "synthetic."   Entries linking to syn-    asymptote (n.)    "straight line continually approaching but never meeting a curve," 1650s, from Greek asymptotos "not falling together," from a- "not" (see a- (3)) + assimilated form of syn "with" (see syn- ) + ptotos "fallen," verbal adjective from pi
==== b7809040cea698f0
Origin and history of sincere    sincere (adj.)    1530s, "pure, unmixed, unadulterated;" also "free from pretense or falsehood," from French sincere (16c.), from Latin sincerus , of things, "whole, clean, pure, uninjured, unmixed," figuratively "sound, genuine, pure, true, candid, truthful" (unadulterated by deceit), a word of uncertain origin.   There has been a temptation to see the first element as Latin sine "without." But there is no etymological justification for the common story that the word means "without wax" ( *sine cera ), which is dismissed out of hand by OED, Century Dictionary ("untenable"), and others, and the stories invented to justify that folk etymology are even less plausible. Watkins has it as originally "of one growth" (i.e. "not hybrid, unmixed"), from PIE *sm-ke-ro- , from *sem- "one" (see same ) + root of crescere "to grow" (from PIE root *ker- (2) "to grow"). 
==== 3210bc26b0a72135
Origin and history of symbol    symbol (n.)    mid-15c., simbal , "creed, formal summary of religious belief," from Late Latin symbolum "creed, token, mark," from Greek symbolon "token, watchword, sign by which one infers; ticket, a permit, license," etymologically "that which is thrown or cast together." It is from assimilated form of syn- "together" (see syn- ) + bole "a throwing, a casting, the stroke of a missile, bolt, beam," from bol- , nominative stem of ballein "to throw" (from PIE root *gwele- "to throw, reach").   The sense evolution in Greek is from "throwing things together" to "contrasting" to "comparing" to "token used in comparisons to determine if something is genuine." The Greek word was applied c. 250 by Cyprian of Carthage to the Apostles' Creed, on the notion of the "mark" or "outward sign" that distinguishes Christians from pagans.    Hence also "something which stan
==== cad53ff4b8c52162
Origin and history of seem    seem (v.)    c. 1200, impersonal, hit semeth ( it seems ), "it appears (that something is so);" also with adjectives or phrases, "to appear to be (in some condition), have or present an appearance of being," from Old Norse soema "to honor; to put up with; to conform to (the world, etc.)," a verb derived from the adjective soemr "fitting."   This is reconstructed to be from Proto-Germanic *somiz (source also of Old English som "agreement, reconciliation," seman "to conciliate," source of Middle English semen "to settle a dispute," literally "to make one;" Old Danish söme "to be proper or seemly"), from PIE *somi- , suffixed form of root *sem- (1) "one; as one, together with" (also compare same ).   With other verbs ( seem to be , etc.) from c. 1200. Sense of "appear to oneself, think oneself" is from 1630s. Also in Middle English "to present oneself, appear; 
==== e2c67a696bafbc83
Origin and history of same    same (adj.)    "identical, equal; unchanging; one in substance or general character," from Proto-Germanic *samaz "same" (source also of Old Saxon, Old High German, Gothic sama , Old High German samant , German samt "together, with," Gothic samana "together," Dutch zamelen "to collect," German zusammen "together"), from PIE *samos "same," from suffixed form of root *sem- (1) "one; as one, together with."   Old English seems to have lost the adjective except in the adverbial phrase swa same "the same as" (literally "so same"). But the word that emerged in Middle English as "the ordinary adjectival pronominal designation of identity" [OED] is considered to be more likely (or mostly) from the Old Norse cognate same , samr "same." In its revival it replaced synonymous ilk .   As a pronoun, "the person or thing just mentioned," from c. 1300. In Middle English also
```


## [2026-09-14T02:03:38.954Z] TOOL CALL #53: Bash

```json
{
 "command": "pdftoppm -f 442 -l 442 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg442-p442 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/",
 "description": "Render PDF page 442"
}
```


## [2026-09-14T02:03:40.615Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor m in re.finditer(r'hanjamana', t):\n    print(t[max(0,m.start()-300):m.start()+500].replace('\\n',' '))\n    print('----')\nEOF",
 "description": "Bartholomae hanjamana entry"
}
```


### [2026-09-14T02:03:41.134Z] TOOL RESULT

```
total 20844
drwx------ 3 sfmqrb sfmqrb   12288 Sep 13 22:03 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   92443 Sep 13 21:13 391-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  129993 Sep 13 21:11 394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21316 Sep 13 21:11 394-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44712 Sep 13 21:14 400-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  116049 Sep 13 21:14 400-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   99858 Sep 13 21:16 404-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   91913 Sep 13 21:18 411-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:23 412-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79667 Sep 13 21:24 414-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  110116 Sep 13 21:31 417hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   88133 Sep 13 21:31 417-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12361 Sep 13 21:31 417-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45082 Sep 13 21:33 421-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96996 Sep 13 21:38 428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18073 Sep 13 21:38 428-zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21962 Sep 13 21:38 428-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb  112884 Sep 13 21:41 429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16099 Sep 13 21:41 429-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96248 Sep 13 21:43 431-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   94911 Sep 13 21:46 432-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  115297 Sep 13 21:42 436-full.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1227534 Sep 13 21:24 afm74-420.png
-rw-rw-r-- 1 sfmqrb sfmqrb  908713 Sep 13 21:23 afm76-421.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1904 Sep 13 21:57 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep 13 21:29 ahd430.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   46904 Sep 13 21:10 beekes410.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    1158 Sep 13 21:33 bqt1328-ftr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1151 Sep 13 21:33 bqt1328-hdr-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1872 Sep 13 21:33 bqt1328-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3114 Sep 13 21:33 bqt1330-top-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:00 bqt1-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  309946 Sep 13 21:35 bqt2123-fn-435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  267233 Sep 13 22:02 bqt439-l254.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   21513 Sep 13 21:39 build2-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   19296 Sep 13 21:42 build3-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66340 Sep 13 21:06 build-389.py
-rw-rw-r-- 1 sfmqrb sfmqrb   60725 Sep 13 21:08 build-390.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66850 Sep 13 21:11 build-391.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67328 Sep 13 21:13 build393.py
-rw-rw-r-- 1 sfmqrb sfmqrb   65361 Sep 13 21:10 build-394.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53331 Sep 13 21:06 build-395.py
-rw-rw-r-- 1 sfmqrb sfmqrb   49820 Sep 13 21:12 build-396.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61718 Sep 13 21:06 build-398.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55842 Sep 13 21:13 build-400.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56563 Sep 13 21:13 build-401.py
-rw-rw-r-- 1 sfmqrb sfmqrb   45908 Sep 13 21:12 build-405.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52807 Sep 13 21:06 build-406.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63772 Sep 13 21:13 build-407.py
-rw-rw-r-- 1 sfmqrb sfmqrb   44609 Sep 13 21:22 build-412.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55188 Sep 13 21:23 build-414.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53220 Sep 13 21:24 build-415.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76184 Sep 13 21:30 build-417.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56437 Sep 13 21:35 build-418.py
-rw-rw-r-- 1 sfmqrb sfmqrb   55739 Sep 13 21:45 build-419.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59029 Sep 13 21:41 build-422.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56950 Sep 13 21:42 build-425.py
-rw-rw-r-- 1 sfmqrb sfmqrb   63145 Sep 13 21:40 build-426.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53942 Sep 13 21:37 build-428.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66449 Sep 13 21:40 build-429.py
-rw-rw-r-- 1 sfmqrb sfmqrb   52975 Sep 13 21:39 build-430.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56759 Sep 13 21:42 build-431.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21413 Sep 13 21:37 build-434.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50426 Sep 13 21:45 build-435.py
-rw-rw-r-- 1 sfmqrb sfmqrb   61435 Sep 13 21:55 build-438.py
-rw-rw-r-- 1 sfmqrb sfmqrb    2291 Sep 13 20:56 c404-empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77003 Sep 13 21:01 c404-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4255 Sep 13 20:56 c404-patil.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34837 Sep 13 20:57 c404-pest.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46825 Sep 13 20:57 c404-symp2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34820 Sep 13 20:56 c404-symp.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35928 Sep 13 21:11 c412_cedar.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42397 Sep 13 21:11 c412_makrome.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81867 Sep 13 21:12 c412_makrome_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54838 Sep 13 21:11 c412_meqrameh.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62842 Sep 13 21:12 c412_meq_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4665 Sep 13 21:12 c412_sedr_zoom2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35561 Sep 13 21:12 c412_sedr_zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11820 Sep 13 21:11 crop411_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    8609 Sep 13 21:11 crop411_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4088 Sep 13 21:11 crop411_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5339 Sep 13 21:28 crop419_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5380 Sep 13 21:28 crop419_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1676 Sep 13 21:28 crop419_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4192 Sep 13 21:28 crop419_d.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3506 Sep 13 21:29 crop419_grk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4444 Sep 13 21:29 crop419_skt.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25580 Sep 13 21:26 crop428a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6915 Sep 13 21:26 crop428b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   54756 Sep 13 21:26 crop428c.png
-rw-rw-r-- 1 sfmqrb sfmqrb   48027 Sep 13 21:26 crop428d.png
-rw-rw-r-- 1 sfmqrb sfmqrb   12740 Sep 13 21:36 crop-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44719 Sep 13 21:39 e0-434.json
-rw-rw-r-- 1 sfmqrb sfmqrb   20203 Sep 13 20:57 edit_about.py
-rw-rw-r-- 1 sfmqrb sfmqrb    6853 Sep 13 21:12 edit_research.py
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep 13 21:14 ffprof
-rw-rw-r-- 1 sfmqrb sfmqrb   49815 Sep 13 21:44 gen-420.py
-rw-rw-r-- 1 sfmqrb sfmqrb 1434288 Sep 13 21:31 irn-425.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  200105 Sep 13 21:31 irn-425.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  929137 Sep 13 22:03 kent2-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     146 Sep 13 22:03 kent-448.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:57 knt-440.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep 13 21:58 knt443.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   45281 Sep 13 21:58 meta-443-knt.json
-rw-rw-r-- 1 sfmqrb sfmqrb  120893 Sep 13 20:58 pg390b.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   39607 Sep 13 20:58 pg390b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  113843 Sep 13 20:57 pg391big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18836 Sep 13 20:57 pg391crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81140 Sep 13 20:57 pg391.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34659 Sep 13 20:58 pg391root.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21174 Sep 13 20:58 pg391sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75438 Sep 13 20:56 pg392.png
-rw-rw-r-- 1 sfmqrb sfmqrb  101976 Sep 13 20:57 pg393.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb   85891 Sep 13 21:00 pg399-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45417 Sep 13 21:00 pg399-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43498 Sep 13 21:00 pg399-sog.png
-rw-rw-r-- 1 sfmqrb sfmqrb  167174 Sep 13 20:58 pg400big.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24547 Sep 13 20:58 pg400_fa_heli.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23086 Sep 13 20:58 pg400_fr2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14689 Sep 13 20:58 pg400_french.png
-rw-rw-r-- 1 sfmqrb sfmqrb   32600 Sep 13 20:58 pg400_kasak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35662 Sep 13 20:58 pg400_kasak3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22852 Sep 13 20:58 pg400_kasak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79028 Sep 13 20:57 pg400.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70671 Sep 13 21:01 pg402.png
-rw-rw-r-- 1 sfmqrb sfmqrb  136264 Sep 13 20:56 pg404hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   71542 Sep 13 20:56 pg404.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63962 Sep 13 20:58 pg405.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63610 Sep 13 20:57 pg406.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79866 Sep 13 20:59 pg407.png
-rw-rw-r-- 1 sfmqrb sfmqrb   21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb   37449 Sep 13 21:14 pg409.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100242 Sep 13 21:09 pg410hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   18557 Sep 13 21:09 pg410-k2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   17676 Sep 13 21:09 pg410-kadm2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6217 Sep 13 21:09 pg410-kadm.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7410 Sep 13 21:09 pg410-persian.png
-rw-rw-r-- 1 sfmqrb sfmqrb   65183 Sep 13 21:08 pg410.png
-rw-rw-r-- 1 sfmqrb sfmqrb   23704 Sep 13 21:09 pg410-q2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    1736 Sep 13 21:09 pg410-qedam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   64940 Sep 13 21:11 pg411_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   56566 Sep 13 21:10 pg411.png
-rw-rw-r-- 1 sfmqrb sfmqrb  161139 Sep 13 21:11 pg412_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74221 Sep 13 21:11 pg412.png
-rw-rw-r-- 1 sfmqrb sfmqrb  481466 Sep 13 21:14 pg412_uhi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   35423 Sep 13 21:09 pg413.png
-rw-rw-r-- 1 sfmqrb sfmqrb   36532 Sep 13 21:12 pg414-greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74486 Sep 13 21:12 pg414.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3823 Sep 13 21:16 pg415-emptybox.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78342 Sep 13 21:16 pg415hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   73449 Sep 13 21:11 pg415.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39289 Sep 13 21:17 pg416-v.png
-rw-rw-r-- 1 sfmqrb sfmqrb   55756 Sep 13 21:17 pg417.png
-rw-rw-r-- 1 sfmqrb sfmqrb  178105 Sep 13 21:15 pg418hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87213 Sep 13 21:15 pg418.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28628 Sep 13 21:15 pg418-raj2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   13818 Sep 13 21:15 pg418-raj3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    6734 Sep 13 21:15 pg418-rajidan.png
-rw-rw-r-- 1 sfmqrb sfmqrb  114625 Sep 13 21:28 pg419_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79366 Sep 13 21:26 pg419.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72677 Sep 13 21:27 pg420b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66620 Sep 13 21:27 pg420.png
-rw-rw-r-- 1 sfmqrb sfmqrb   31408 Sep 13 21:27 pg421.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66285 Sep 13 21:29 pg422.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66328 Sep 13 21:27 pg423.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74989 Sep 13 21:24 pg424.png
-rw-rw-r-- 1 sfmqrb sfmqrb   67629 Sep 13 21:26 pg426.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154381 Sep 13 21:26 pg428hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   61436 Sep 13 21:23 pg428.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7200 Sep 13 21:23 pg429-crop1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7703 Sep 13 21:23 pg429-crop2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4400 Sep 13 21:23 pg429-crop3.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168822 Sep 13 21:23 pg429hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78202 Sep 13 21:23 pg429.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81124 Sep 13 21:24 pg431.png
-rw-rw-r-- 1 sfmqrb sfmqrb   92551 Sep 13 21:33 pg432.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74286 Sep 13 21:24 pg433.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46452 Sep 13 21:28 pg435-n1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   42245 Sep 13 21:28 pg435-n4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89932 Sep 13 21:28 pg435.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66400 Sep 13 21:31 pg436.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60815 Sep 13 21:36 pg437-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153828 Sep 13 21:36 pg437hi-437.png
-rw-rw-r-- 1 sfmqrb sfmqrb  100480 Sep 13 21:42 pg438.png
-rw-rw-r-- 1 sfmqrb sfmqrb   82782 Sep 13 22:03 pg439.png
-rw-rw-r-- 1 sfmqrb sfmqrb   75018 Sep 13 22:03 pg440.png
-rw-rw-r-- 1 sfmqrb sfmqrb   84851 Sep 13 22:03 pg442-p442.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77924 Sep 13 21:59 pg443.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70076 Sep 13 21:57 pg444.png
-rw-rw-r-- 1 sfmqrb sfmqrb   24437 Sep 13 22:00 pg444-serom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   19924 Sep 13 22:00 pg444-sibum.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11542 Sep 13 22:00 pg445-crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74593 Sep 13 22:00 pg445.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47049 Sep 13 22:03 pg446.png
-rw-rw-r-- 1 sfmqrb sfmqrb  145450 Sep 13 22:01 pg450hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11427 Sep 13 22:01 pg450-pechkam.png
-rw-rw-r-- 1 sfmqrb sfmqrb   79151 Sep 13 22:00 pg450.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11602 Sep 13 22:01 pg450-shangarf.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63836 Sep 13 21:59 pg452.png
-rw-rw-r-- 1 sfmqrb sfmqrb   78966 Sep 13 21:58 pg453.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74797 Sep 13 22:01 pg454.png
-rw-rw-r-- 1 sfmqrb sfmqrb  102312 Sep 13 22:00 pg456-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70887 Sep 13 22:00 pg456hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   33661 Sep 13 21:58 pg456.png
-rw-rw-r-- 1 sfmqrb sfmqrb   43086 Sep 13 21:58 pg458.png
-rw-rw-r-- 1 sfmqrb sfmqrb       0 Sep 13 21:57 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  387279 Sep 13 21:13 sem410.html
-rw-rw-r-- 1 sfmqrb sfmqrb   59726 Sep 13 21:14 u_mak.png
-rw-rw-r-- 1 sfmqrb sfmqrb   49161 Sep 13 21:14 u_meq.png
-rw-rw-r-- 1 sfmqrb sfmqrb   34177 Sep 13 21:14 u_sedr.png
-rw-rw-r-- 1 sfmqrb sfmqrb   47858 Sep 13 21:06 write397.py
-rw-rw-r-- 1 sfmqrb sfmqrb   59484 Sep 13 21:11 write-402.py
-rw-rw-r-- 1 sfmqrb sfmqrb   43710 Sep 13 21:22 write409.py
-rw-rw-r-- 1 sfmqrb sfmqrb   28665 Sep 13 21:19 write410.py
-rw-rw-r-- 1 sfmqrb sfmqrb   47575 Sep 13 21:42 write436.py
```


### [2026-09-14T02:03:42.279Z] TOOL RESULT

```
 frasta  (3S/AorM.)  ma- natgha  "noch  lässt  er  sich  von  VM,  be- raten, 0  M."  Y.  4p.  2;  —  ahurö  yehyä vahml  vohü  frah  mananha  ". .  in  dessen Preis  ich  mich  von  VM.  habe  beraten lassen"  Y.  4$.  6.  8)   Med.    'sich   be- reden, besprechen':  vlspalfO  ^frasnailü vTspaäa  hanjamanalsä  yaU  apinsaltim (3D.,  Augm.)  mazda sca  xardhustrasca "bei  allen  Besprechungen,  bei  allen  Zu- sammenkünften, bei  denen  sich  bespra- chen . ,"  Y.  72.  5.  a)  mit  Angabe des  'mit  — '  durch  o)  Instr.:  anulAaxs *armaitis  matnyS  *p»r3saite ya'hra  ma/%a (ad.)  Y.J7. 12;  —  hs  aSava  yail  p3r3iai dngva  vä  "wer  von  denen,  zu  denen  ich dby  Google 999  traa-  8  ß  —  frosastay-  looo jetzt  sprechen  will,  ist  ein  Asa-,  wer  äa\hsmijrast3"''>  manatjM  
----
amqn  Y.57. 16;  3,  16,  30,  Ytp.9f.*;  — zqm  . .  ya%a  rai^ake  (näml.  haoma)  . .  '<'' huru%ma  Y./0.43);  Vr.p.i;  —  urvanö akäs^Sii{&A.)  shuire  'da  jaitntqm  Y.oo.  i —  kai  afava  'da  vanat  drvant»m  Yt./,  aS; — pata  nS  ibifyantaipairi  °</jj(als  Vok.)/a armaitiica  SrB.j;  —  hanjamanaisü  yai/ apmsalhm  'd3s^  sara'küitraslä  Y.  12.  5 ; —  'dqmla  tara%uilT7m^ä  yazamaidl  Y. 42.  2.  Undeutlich:  hä^anrB^am  (sd.) •dai  ttxlqm  F.  24.  [FrW.p.'i:  lies maidaoxt)m.\  l)  va  Verbindung  mit ahura-,  ff*wra-*l :  sd.,  auch fdSt  (Sp.  386u,). KompA.J>,  E.  —  Zum  V.  maxdä-;  e\g,  'memor, der  («lies)  merkt'.   —    iHe».  S  3^3,  414.  — Pü.:   ökrmOMd;    s,  noch  No.   1  fl.    —    ■)  V Shrmatd,    mit    der    Erl. ;    öhtmasdih    u    j iaiih  u 
----
  IS.  einer  Ableit.  aus  m;  S  //f.  —  Be- stimmung ganz  unsicher,  da  das  Wort  aus dem  Zusainmenhuig  geriisen  ist.  Vll.  stammt es  aus  V.  2.    lo;  s.  Pu.  —  Pü. :  a/Ä •  j.  vi-£ar3na-  n.  Trennungsstelle,  Stelle, wo  sich  der  Weg  teilt":  pa%amcS  *'rjnä'> .  .  pahqmia  hanjamana  Y,  4-3.  i ;  — fakqm  '.  .  paiti  'na  Yt  //.  4,  Vyt.  54. Zum  V.  iiar-,  —  ai,  vicarana-  d.  'Bewegung'.  — Yä.:yul  rawünii.  —  0  So  Pt4;   NA.  •rani. •  j.  vi6ida-  n.  'Kalk,  Gips,  Mörtel':  asa- nafraa  . .  'caih/a  . .  tütuxha  (sd.)  V.  ö^.  5 1 ; —  dva  äim  nara  tsSi^e  .  .  upa.siambtm (sd.)  'ialsva  dim  nidai^yan  V.  (V.  10. Et.?  —  Pü.  (zu  V.  6):  ga^'),  (w  V.  *): fehlt.  —  ■)  D.  i.  'aus  .fa/  (=  np.  ^-a/'Kalk') bestehend';  s.  d
----
imus"  Y.  4$. 6,  79.1a,  27.1,  Vr.  77.  ai;  P.  40  (Sp. 52  f.);  —  'panqm  (GPn.)  vahtshm  "id quod  est  omnium  Optimum"  Y.  43-  ^i 44-  7;  — paourvlm . .  'psng  (GPn.)  "primo omnium"  Y.  2Ä1;  —  mihrö  7>?(GPm.?) matdayasnanqm  .  .  >rHiwä{sA.)i!a  .  .  Yt. 70. 120;  —  'paisa  hanjamana^B  Y.  72.  5; S,  P.27',  N.7?',  Yt77.  3%  75.53';  — 'pshu  paiti   barfzähu   Yt70.45;  45;  — dby  Google vispa-  Schluss i463_^    *päku  (fem.  statt  ntr.)  kar^Shu  Ytio. 16.  Anhang.  vXspa-  mit  Gen.  part"; a)  Sing,  mit  Gen.  Sing.:  %rilüin  . .  nagm?m ..vTspfm  aitake  syao%nahe"€\a.T>r\\\e\.. die  Hälfte  . .  das  Ganze  dieser  Tat"  V. Ä  100-102.  b)  Plur.  mit  Gen.  Plur,: ks  *fe  (APm.)  vtrnhinqm  (sd.)  vanat  nl •pe  v?r3tbinqm  janai  Y.  5. 14. Undeut
----
  'Schacht",  von  der eisernen  Feste  Franrasyam  im  Erdinnem** : tarn  yazata .  .franrase  'kaine  paiti  ''atths zimS  Yt_5,  41. •)  Im  Sn.  hang  1  ä/rasiäi,  was  auf  ein  mp. andn  (d.i.  hangan\)  i  fr'  schliessen  läist.  Vgl. Aog.  6/:  eigen  fräsyäk  kacdlat  i  tamVi  ään  säxt hanjamana-  1770 min  iarl,  Y,  //.  ^  PüErl. :  iui  drupiänh  ('Feste') pirämön  kart  eitel;  s.  noch  unter  painiji^asia: Weiteres  bei  DsT.  fillr.  2.  315,  ZA.  /.  m, 2.  377- •  j.  han-k^ratay-,  h»n-k%  g.  hän-k«  £ 'Vollziehung,  Vollendung',  i)  von  den Gahäs  sva.  'vollkommene  Rezitation': iaj  asii  rä^wqm  */ram)r»tis  ka$  gS%a- nqm  *hank}rnti^  Y.  77. 1.  2)  von  den da%ra--  sva.  'Abschluss,  Abrechnung';  yä iiuds  dad^nts  däiranqm  (sd.)  .  .  yahä  tä atshm
----
```


## [2026-09-14T02:03:52.414Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nhead -3 kent-448.txt; echo ---; grep -n \"hada\\b\\|hadā\\|hakaram\\|LEXICON 21\" kent2-448.txt | head -20",
 "description": "Check scratchpad Kent OCR"
}
```


### [2026-09-14T02:03:52.486Z] TOOL RESULT

```
<html>
<head><title>404 Not Found</title></head>
<body>
---
2132:‘this’, prep. hada ‘with’ belong to Pahlavi of the 
4136:KT’s hada : kar|a : Salkam. 
4736:*sm-dhe, OP hada, Skt. sahd ‘with’. 
5222:OP hada ‘with’, Skt. sahd, from plK *sm-dhe; 
12351:A. With hada, to denote accompaniment either 
12437:J. With prepositions: hada (see A); anw (see 4 
12513:I brought horse(s)’; in DB 5.24f avadd hada kara 
13026:hada, prep. w. instr. 
13088:hada ‘with’, of accompaniment, of hostile associa- 
13826:‘then’ (§291.IV); and hakaram ‘once’ (DNb 34f), 
17188:56 mahyd : X : raucabis : Gakataé : aha :avaidé : adam : hada : kamnaibiS : martiyaibi 
17647:23 daiy : avada : hamaranam : akunaus : hada : Mada : bya : Madaisuva 
17737:71 Sayaéiya : pasava :hauv : FravartiS : hada : kamnaibis : asabaraibis : amufa : Ra _ 
17765:85 ava : Taxmaspada : hada : kird : aSiyava : hamaranam : akunaud : had ) 
17785:95 astyava : hada : kara : hyasacy : anusya : dha : ViSpauzati§ : nima : varda 
17787:96 nam : Parbavaiy :avada : hamaranam : akunaug : hada : Paréavaibis : Auramazdamaiy 
18093:5 na : nama : vardanam : Parbavaiy : avada : hamaranam : akunaus : hada: 
18111:15 m : karam : jadiy : hya : mand : naly : gaubataiy : pasiva : DadarSis : hada : k 
18147:‘$3 dam : pasiva : Artavardiya : hada : kird : aSiyava : Pirsam ~ 
18154:36 hada : kara : patiS : Artavardiyam : hamaranam : cartanaiy : pas
```


## [2026-09-14T02:03:56.568Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ngrep -n \"LEXICON\" kent2-448.txt | tail -20\necho \"===\"; sed -n '4720,4760p' kent2-448.txt\necho \"=== 5210\"; sed -n '5205,5235p' kent2-448.txt",
 "description": "Kent lexicon h- section"
}
```


### [2026-09-14T02:03:56.683Z] TOOL RESULT

```
25426:LEXICON 
25704:LEXICON 
26000:LEXICON 
26285:LEXICON 
26571:LEXICON 
26849:LEXICON 
27147:LEXICON 
27436:LEXICON 
27732:LEXICON 
28023:LEXICON 195 
28309:LEXICON 
28575:LEXICON 199 
28832:LEXICON 
29101:LEXICON 
29380:LEXICON 
29661:LEXICON 
29918:LEXICON 209 
30190:LEXICON 
30459:LEXICON 
30726:LEXICON 
===
same development as before a vowel; it 1s possible 
that OP akariya"td is based rather on *ekerzonio. 

S67. PLE m AND n became pAr. a before con- 
sonants. 

*mbhi, OP abiy, Skt. abht, oHG umbt (but see 
"Lex. s.v. abty). 

*hmtom ‘100’, in @ata-gué (uncertain etymology, 

see Lex. s.v.). 

*bhndh-to-, OP basta- (§85), Skt. baddhd-, cf. Eng. 
bound. 
negative prefix *n- in a-xSaina-, a-xsala-, etc. 
*sm-dhe, OP hada, Skt. sahd ‘with’. 
{. Before a vowel or 7 or u, pIE 2 and m must, 


1 Leg. 18.79-82. ? Phonetically proper when the 7 was 
preceded by two consonants, or by one consonant which 
was itself preceded by a long vowel or a diphthong: 
Kdgerton, Lg. 10.257. ? The OP must not be normalized 
akr- (like the Skt.), since &r became zr in Iranian; 
$108.1. 


27 


like 7 (§66.1[), appear as o” and om, which 

became OP an and am: 

*g%em-sét, Skt. gamyat, OP d-jamiyd ‘may it come’ 
(with analogical j, §101). 

neg. prefix *on- in An-dhita (never so written, 
see Lexicon) “The Spotless Goddess’. 

=== 5210
established’ (on -§-, §117), Skt. dsddayam. 
plE insep. prefix *dus- ‘ill’, OP dus-, Av. dus-, 

Skt. dus-, Gk. due-. 
pIE *dyttijo- ‘second’, OP dustiya-m, Skt. 

dvitiya-. 

OP d from pAr. dh from pIE dh: 
plE *dhé- ‘put’, OP ada ‘he created’, Skt. ddhat. 
plE *dher- ‘hold’, OP déraydmiy ‘I hold’, Skt. 

dhardyams. 
plE *dhyor- ‘door’, in OP loc. duvarayad, Av. 

dvar-, Skt. dhvar-, cf. Gk. @ipa. 
OP ba*daka ‘subject’, to pIE *bhendh-, §75.III. 
OP hada ‘with’, Skt. sahd, from plK *sm-dhe; 
same suffix in avada, ida, ada-katy. 

With Skt. d from plE dh by Grassmann’s 
Law (§73.IV): 
plE *dhrugh-je- in OP adurujiya ‘he lied’, Skt. 

drihyatt ‘he deceives’, Gm. friigen; pli 

*dhrougho- in OP drauga- ‘Lie’, Skt. dréha- 

drégha- ‘injury’. 
plE *dhighé, OP dida ‘wall’, cf. Skt. deha-, Gk.
```


## [2026-09-14T02:04:02.923Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nsed -n '30180,30290p' kent2-448.txt",
 "description": "Kent lexicon page 211"
}
```


### [2026-09-14T02:04:02.975Z] TOOL RESULT

```
Siyatt- sb. ‘welfare, peace (on earth), happi- 
ness (also after death)’ (Hz. AMI 3.40, 8.68-9, 
RHRel. 113.26-7, Ap] 318-22): LAv. Sati- ‘Joy’, 
also in queen’s name (Gk.) Qapb-caris, Lt. quiés 
quvét-is ‘quiet’ ($104, §152.11], §179.111); see also 


= we Sacra a een 


LEXICON 


Siydia-. For ‘happiness after death’, see JNES 
7.108 with notes 10 and 11. Siyatt§ nsf. DB 5.20°, 
36°; DPe 23. Sydtim asf. DNa 4; DNb 2f; DSe 
4°; DSf 3; DSs 4°; DSt 4°; DZe 2; DE Sf; XPa 3; 
XPb 5f; XPe 3, XPd 4; XPf 4; XPh 3; XE 6; 
XV 5; A'Pa 4°; A?’He 4; miswritten sdyatam 
(§55.1) A'Pad. 


Siyav- vb. ‘set, forth, go’: GAv syav-, LAv. 
Sav-, NPers. ‘sv, Skt. cydvati, Gk. cebw ‘I start 
quickly after, chase, cause to chase’, plE *gieu- 
($104). adzyavam Ist sg. imf. (§213) DB 1.84, 
91;2.3,65;5.21. aszyavaimf. DB 1.38 bis, 41, 80; 
2.2f, 17, 22, 32, 51f, 72, 85, 95°; 3.4, 16, 28, 32, 
33, 42, 59f, 72, 73f, 82, 87, 5.9; XPf 33f. akyava” 
od pl. imf. (§232.11) DB 1.76. 


Skaurim, see under skaubt-. 
Sta-, see under sia-. 


zana- sb. ‘human being’: Av. zana-, Skt. jdna-, 
Gk. yovos ‘child, offspring’, pIE *gono- (§88, §143.- 
I); in paruzana-, Varkazana-, vispazana-. 


zam- sb. ‘earth’: Av. nom. 24, Gk. xapat ‘on 
the earth’, Lt. humus ‘earth’, Lith. zémé, pIE 
*Ghem- (811, §142, §148.11), ef. *@5hem- in Skt. 
ksam-, Gk. ydav; in Uvirazmi-, uzma-. 


[za}rianayd with Med. z-, alternative restora- 
tion for {da}rianayd; see dartana-. 


Zazdna- sb. ‘Zazana’, a town on the 
Euphrates above Babylon: Elam. za-tz-za-an, Akk. 
za-za-an-nu (§120). Zazéna nsm. DB 1.92. 


ztirakara- sb. ‘evil-doer’ (§143.V, §160.Ia): 
zurah- ‘evil’ (§105, §119, $120) + kara- ‘doer’ 
(§99, §122), to vb. kar-.  ziirakara nsm. DB 
4.64, 68. 


ztirah- sb. ‘deceit, wrong’: Av. ziirah-, NPers. 
zr ‘lie’, cf. Skt. hudras- ‘crookedness, deceit, trap’ 
(§9.1V, §88, $120, $156.11); see also zirakara-. 
zura asn. DB 4.65. 


Ziizahya- sb. ‘Zuszahya’, a town in Armenia: 
Flam. su-iz-za, Akk. zu-t-zu (§120).  Zrizahya (all 
characters visible acc. to Cameron) DB 2.33. 


zbd- vb. ‘call’ (Lg. 19.226-7; Hz. AMI. 8.67, 
Apl 367): Av. zav- and 2bd, pres. zbaya-, Skt. ha- 
and hwd-, pres. hvaya-, pI *ghud- (Med. 2b-, 
§89.VI, §91, §120); see also hazdna-. 

pati- + zbaya- ‘proclaim’ (used of prohibitions 


211 


only, By. BSLP 42.2.70): patiyazbayam Ist sg. 
imf. (§214) XPh 38. 


Zra"ka- adj. ‘Drangian’; masc. as sb., 
‘Drangiana’, a province of the Persian Empire: 
Elam. str-ra-an-qa, Akk. za-ra-an-ga, Gk. (Hdt.) 
Lapayyat, (Polybius) Apayyqvn, (Strabo) 
Apayyravh, (Arian) Zapayyar (§9.1, §33, §88, 
§120, §128; ef. MB Gr. §119). 

(1) ‘Drangian’: Zraké for nsm. (§56.11T} AP 9. 
(2) ‘Drangiana’: Zraka nsm. DB 1.16; DPe 
15f; DNa 24; DSe 23°; DSm 8°; XPh 20. 


ha- insep. prefix (§204.1), anteconsonantal 
(§132.1): Av. ha-, Skt. sa-, Gk. a-, Lt. sem-, pIE 
*sm-, zero-grade of pI *sem- ‘one’, Gk. eis & 
(from *sem-s *sem); in hakara-, hada. See also 
ham-, hama-. 


haind- sb. ‘army’: Av. haénd-, Phi. hén, Skt. 
sénd- (§118.1, §147.1T). — haind nsf. DPd 19. 
hainayd abst. DPd 16f.
```


## [2026-09-14T02:04:09.199Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\nsed -n '30290,30470p' kent2-448.txt",
 "description": "Kent lexicon page 212"
}
```


### [2026-09-14T02:04:09.259Z] TOOL RESULT

```
hauv pron. ‘this one’, pron. adj. ‘this’ (§11, 

§263): pLE nsm. *so, nsf. *sd, Av. hé (from *so-s), 
ha, Skt. sa-s sa, Gk. 0 4 ‘the’, + particle *u, Skt. 
u ‘also’, seen in Gk. rav-v ‘altogether’, obros ‘this’ 
from *so-u-tos, probably also in OP u-td ‘and’, 
OP hdw shows the regular contraction of d-x 
($1I8.1V, $196); but *sdu, with @ by analogy of 
the fem., was generalized as masc.-fem. in Av. 
hdu, Skt. a-sdu. See also hawam, hya. 

haw) pron. nsm. AsH 8, 14; DB 1.86, 38, 41, 47, 
47{, 74, 76, 78, 81; 2.10, 14, 16°, 17, 19, 24, 98f,; 
3.28f, 26f, 28, 55, 71, 79, 80, 82, 88; 4.8°, 9, 10, 
12, 18, 15, 16, 17, 18, 20, 21, 22, 24, 25, 26, 28, 
29°, 30; 5.26°; DPd 2; DSf 9, 9f, 30, 31, 38, 39; 
DSp 1°; XPh 54; XV 18, 21. hawy-mary DB 
2.79. hau-maiy DSf 10. hau-saiy DPd 3; DSp 
2°. hau-dim DSf 32. hau-dis D8s 6°. 

haw nsf. ($196) DB 5.4f; hauv-maiy DB 3.11; 
hauy-taiy DNa 57; hauv-cry DPe 23f. 

haw adj. nsm. DB 1.82, 92°; 2.21, 27, 66, 71; 
3.3, 30, 41, 54, 59, 70, 91°; 5.9°. 


haumavarga- adj. ‘hauma-drinking’ or 
‘hauma-preparing’ (§160.la): Elam. u-mu-mar-ga, 
Akk. ti-mu-ur-ga-’, Gk. ’Auipywt. From hauma- 
($149.0), Av. haoma-, Skt. séma- name of a plant, 
also a drink prepared from the juice of its crushed 
stems, to root Av. hau-, Skt. su~ ‘press’, + varga- 
(§31, §143.D, of unknown connections. hauma- 


212 


varga npm. DNa 25; DSe 24f°; XPh 26; as nsm. 
(§56.11), ArP 14. 


hauvam pron. ‘he’, nsm. DB 1.29: haw (q.v.) 
+ -am from adam, tuvam, ete. (§48, §137, §196). 
Cf. MB Gr. §158. 


hakaram adv. ‘once’ (§191.JII, §204.1): Av. 
hakarat ‘once’, Skt. sakft, ef. Gk. a-rat, Lit. sem-el; 
ha- (q.v.) + *hyt ‘time’ (ef. Lith. kaftas ‘time’), 
remade to -karam after kara- ‘maker’ (Hz. Apl 
181). Cf. also By. Gr. §828. hakaram-ciy DNb 
34f. 


ha™karta- (§140.V) pte. adj., nt. as sb., ‘co- 
operation’: ham- + karta- ‘done’, past. pte. pass. 
tokar-. {halkartahyd gsn. DNb t6f (Kent, JNES 
4,42-3; not karrpahyd or [ulkarrtahyd, with Haz. 
ApI 283-5; not [halkarrtahyd, with dittography 
of r*, with Kent, Lg. 15.170). 


Hazxamanis- sb. ‘Achaemenes’ (§161.Ib), 
founder of the Achaemenian dynasty: Elam. ha- 
ak-ga-man-nu-i3, Akk. a-ha-ma-ni-i%’, Gk. 
’Axaens. From haxd-, LAv. nsm. haza, Skt. 
nsm. sdkhé ‘friend’, + manzs-, with reduced grade 
of vowel in ultima (§63.1], $124.4, $156.IV, 
$185.11, nl), otherwise identical with manah- 
(q.v.). See also Haxdmanisiya-. Hazadmanis 
nsm. DB 1.6; DBa 8. Hazxdmanisahya gsm. ($57, 
§185.017; ef. Hz. AMI 4.138, 8.31-4) AmH 3f. 


Hazdmanisya- adj. as sb. ‘Achaemenian’: 
adj. to preceding ($144. ITI, §159, §185.n1; hardly 
-Sya- from -tya-, as suggested by MB Gr. §262, 
ef. Hz. AMI 4.133, 831-4). Hazaman sya nsm. 
AsH 4; CMa 2; CMb 2°; CMe°; DB 1.8; DBa 4; 
DPa 5; DPb; DPe 5; DPh 3; DNa 18; DSb 11; 
D8d 2; DSe 12; DSf 7f; DSg 2; DSi 2°; DS} 2; 
DSk 3; DSm 2; DSy 3; DZb 6; DZe 6f; DE 20; 
DH 2; XPb 20f; XPe 9; XPd 14; XPe 4; XPf 
14f; XPh 12; XPj; XPk; XSc 2; XE 20; XV 
15f; A'Pa 16°; A‘; D*Sb 2; A*Se 1; A’Sdb 2; A?Ha 
5; A®?Hb; A’He 15; A*Pa 20f; Wa 7f; Wb 8f; We 
Of; Wd 9f. Héazdmanisiya ($538) XPa 10f. 
Hazdmani#ya (§22) DSa 2f; A’Sda, de 2. Haza- 
man kiya (§22, $51) A’Sa8. Haxdmanixiyd npm. 
DB 1.7; DBa 10. 


Ha™gmatana- sb. ‘Ecbatana’, a royal resi- 
dence in Media: Elam. ag-ma-da-na, Akk. a-ga- 
ma-ta-nu, Gk. (Hdt.) ’AyBarava, (Aesch., 
Aristoph.) "ExBarava, NPers. Hamddan. Prob- 
ably deriv. of ha-gmata- (q.v., under gam-; §103.- 


OLD PERSIAN 


IV, §147.II): ‘City of Gatherings’. Hagmatanaty 
ism. DB 2.76, 771. 


haca prep. ‘irom’: GAv. hacd, LAv. hacd, Skt. 
séca ‘with’ (on meanings, see Fay, JAOS 31.403- 
12): instr. sg. of thematic root-noun to pI: *seq*- 
‘follow’, Av. hacadle, Skt. sdcate, Gk. émeras, Lt. 
sequitur, Gr. satlvan ‘see’ (§99). Syntax §271. 

(1) With abl.: DB 1.36, 40, 61; 2.64; 3.2, 26; 
4.37; DPd 11, 16, 17 bis; DPe 20; DNa 18, 46, 52; 
D8Se 17, 38; DSf 31, 34, 35°, 35, 36, 38, 39, 41, 42, 
43, 44; DZe 7, 10, 11; XPh 16, 57; A’Sa 5°; A’Sda 
4 (hasd de 4, §49b); A*?Ha 6°. hacd-ma DB 1.19, 
23; 2.6, 12, 16, 93°; 3.27, 78, 81; 4.92; DPe 9, 
DNa 20; DSe 19°; XPh 18. 

(2) With loc. form as abl.: DPh 7; DSf 33, 44; 
DH 5. 

(3) With instr. form as abl.: DPh 5; DH 4. 

(4) With ablatival adverbs: hacd avadaSa DB 
1.37; 3.42, 80; DSe 47f°; DSf 47. hacd parunryata 
DB 1.7, 8, 45; DBa 11, 12. [hacd-ca}ly didradasa 
DSf 23. 

(5) With preceding encl. pron. in acc.: -sim 
hacé DB 1.50 (Bang, ZDMG 48.534; Bv. BSLP 
31.2.64-5). 

(6) With anacoluthic naming-phrase in nom.: 
hacd Pirdva nama rauta DZc 9. 


ha'- vb. ‘hang’: Skt. safj- ‘fasten’, pres. 
sdjatt. 
fra- + ha7y- ‘hang out’ for display (Foy, KZ 
35.39), namely the rebel’s skin, stuffed with straw 
(Konig, RulD 73-4; wrongly ‘imprison’, Sen 45): 
frahajam (st sg. imf. (§213) DB 2.78. 


had- vb. ‘sit’: Av. had-, Skt. sad-, Lt. sedet, 
NEng. sit. See also hadzé-, and possibly 
Vistaspa-. 
ni- + §ad- ($117), caus. ni-sddaya- ($76.11, 
§122, §123.2, §132.2-3, §215) ‘set down, establish’: 
niyasddayam (§226.I1) Ist sg. imf. DNa 36. nisa- 
dayam (§23.1, §140.11T) XPh 34f (ef. Hz. AMI 
8.65, ApI 180-1). 


hada prep. with imstr. ‘with’: GAv. hada, 
LAy. hada, Skt. sahd, pIE *sm-dhe ($11, §67, §76.- 
ITT); Ar. *sa- (see OP ha-) + adv. suffix -dhe as 
in ida@ ete. Syntax §270.1. DB 1.56, 93; 2.1f, 
21f, 23, 67, 71, 85, 85f, 95°, 96; 3.5, 15, 16, 33, 
36, 41, 71, 73, 86; 5.9°, 10°, 21, 24; DPd 14, 22, 
24°; DPe 8; DSe 50; DSt 8°; XPb 28; XPe 12, 


LEXICON 


15; XPd 18; XPg 13; XSe 5°; XV 26; A'Pa 23; 
D¥8a 3. 


hadazaya, uncertain word (§163.VII), Sb 1. 


hadis- sb. ‘seat, abode, palace’: Av. haéts-; 
deriv. of had- ‘sit’; for suffix cf. Hazd-mants- to
```


## [2026-09-14T02:04:24.909Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\ngrep -n \"ham- insep\\|hama- adj\\|hama- pron\\|^ham- \" kent2-448.txt | head\necho ---\nsed -n '30470,30560p' kent2-448.txt | grep -n \"ham\" ",
 "description": "Kent ham- entry"
}
```


### [2026-09-14T02:04:24.993Z] TOOL RESULT

```
26342:ham- + gam- ‘come together, assemble’: ha™- 
26714:ham- + taxs- ‘work with, cooperate with, ef- 
27239:ham- + dar- ‘get hold of, obtain’: hamadarayaiy 
30502:ham- insep. prefix, ‘together, with’, like Lt. 
30512:hama- adj. ‘one and the same’: Av. hame-, 
---
8:ha"dugd- sb. ‘record, statute’: ham- + dugd-, 
33:ham- insep. prefix, ‘together, with’, like Lt. 
35:cognate): Av. ham-, Skt. sam-; originally identical 
38:Ha-gmatina-, ha-dugd-, ham-arana-, ha-micrya-, 
40:kam~ (see under amazamatd). See also hama-. 
43:hama- adj. ‘one and the same’: Av. hame-, 
45:deriv. of pIE *sem- ‘one’, cf. ha- and ham-. Deecl., 
46:§203.II]. See also hamétar-, hamapilar-. hama 
49:62.268-9). hamahydyd gsf. formed on gsm. 
50:*hamahyd (cf. ahydyd toa-), DB 4.4, 41, 45, 52, 60. 
53:hamédtar- adj. ‘having the same mother (as 
54:another person, specified)’ (§161.IIa): hama- + 
55:médtar-, with haplology (§129). hamata (§62, 
62:hamapitar- adj. ‘having the same father (as 
63:another person, specified)’ (§161.[[a): hama- + 
64:pitar- father’, hamapilé nsm. (§124.5, §186.II, 
68:hamarana- sb. ‘battle’: Av. hamarana-, Skt. 
69:samdrana-; sb. to verbal epd. ham- + ar- (§82, 
71:hamaranakara-. hamaranam nsn. DB 2.27, 37, 
72:42, 47, 56, 62, 98; 3.8, 19, 40, 47, 64, 69. hamara- 
75:36, 37, 43, 44, 60, 61, 65, 66; 5.10°. hamarand 
79:hamaranakara- sb. ‘battle-maker, warrior’: 
80:hamarana- + kara- ‘maker’, from root kar- (§160.- 
81:Ta}. Cf. also ushamaranakara-. hamaranakara 
85:hamiciya- adj. ‘rebellious’, ag sb. ‘rebel’: 
86:deriv. of ham- (or ha-) + miga- ‘friend’ (see 
90:modeled to ham- by association with ham-arana-
```


## [2026-09-14T02:04:31.276Z] TOOL CALL #60: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg442-p442.png"
}
```


### [2026-09-14T02:04:31.817Z] TOOL RESULT

```

```


## [2026-09-14T02:04:31.813Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T02:04:45.412Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 442 -l 442 -r 600 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg442hi-442\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg442hi-442.png'); print(im.size)\nW,H=im.size\n# samavar persian box: approx x 0.63-0.78, y 0.545-0.575 of page (based on 1700x2200 ratio)\nim.crop((int(W*0.60),int(H*0.535),int(W*0.80),int(H*0.575))).save('c442-samavar.png')\nim.crop((int(W*0.60),int(H*0.375),int(W*0.80),int(H*0.455))).save('c442-fa8.png')\nEOF\nls -la c442-*.png",
 "description": "Crop samavar and Persian loan boxes"
}
```


### [2026-09-14T02:04:50.556Z] TOOL RESULT

```
(5100, 6600)
-rw-rw-r-- 1 sfmqrb sfmqrb 5703 Sep 13 22:04 c442-fa8.png
-rw-rw-r-- 1 sfmqrb sfmqrb 2377 Sep 13 22:04 c442-samavar.png
```


## [2026-09-14T02:04:52.753Z] TOOL CALL #62: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c442-samavar.png"
}
```


### [2026-09-14T02:04:52.772Z] TOOL RESULT

```

```


## [2026-09-14T02:04:59.494Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg442hi-442.png'); W,H=im.size\nim.crop((int(W*0.60),int(H*0.555),int(W*0.80),int(H*0.60))).resize((int(W*0.20*1.5),int(H*0.045*1.5))).save('c442-samavar2.png')\nEOF\necho ok",
 "description": "Recrop samavar region"
}
```


### [2026-09-14T02:05:01.333Z] TOOL RESULT

```
ok
```


## [2026-09-14T02:05:03.615Z] TOOL CALL #64: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c442-samavar2.png"
}
```


### [2026-09-14T02:05:03.631Z] TOOL RESULT

```

```


## [2026-09-14T02:05:08.546Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg442hi-442.png'); W,H=im.size\nim.crop((int(W*0.58),int(H*0.595),int(W*0.80),int(H*0.625))).resize((int(W*0.22*2),int(H*0.03*2))).save('c442-samavar3.png')\nim.crop((int(W*0.55),int(H*0.40),int(W*0.80),int(H*0.46))).resize((int(W*0.25*2),int(H*0.06*2))).save('c442-fa8b.png')\nEOF\necho ok",
 "description": "Crop lower for samavar and Persian loans"
}
```


### [2026-09-14T02:05:10.575Z] TOOL RESULT

```
ok
```


## [2026-09-14T02:05:12.885Z] TOOL CALL #66: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c442-samavar3.png"
}
```


### [2026-09-14T02:05:13.006Z] TOOL RESULT

```

```


## [2026-09-14T02:05:13.001Z] INPUT

[Image: original 2244x396, displayed at 2000x353. Multiply coordinates by 1.12 to map to original image.]


## [2026-09-14T02:05:19.869Z] TOOL CALL #67: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c442-fa8b.png"
}
```


### [2026-09-14T02:05:20.113Z] TOOL RESULT

```

```


## [2026-09-14T02:05:20.095Z] INPUT

[Image: original 2550x792, displayed at 2000x621. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-14T02:05:26.549Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg442hi-442.png'); W,H=im.size\nim.crop((int(W*0.55),int(H*0.455),int(W*0.80),int(H*0.50))).resize((int(W*0.25*2),int(H*0.045*2))).save('c442-fa8c.png')\nEOF\necho ok",
 "description": "Crop sambol/sampozium"
}
```


### [2026-09-14T02:05:28.487Z] TOOL RESULT

```
ok
```


## [2026-09-14T02:05:30.818Z] TOOL CALL #69: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c442-fa8c.png"
}
```


### [2026-09-14T02:05:30.992Z] TOOL RESULT

```

```


## [2026-09-14T02:05:30.990Z] INPUT

[Image: original 2550x594, displayed at 2000x466. Multiply coordinates by 1.27 to map to original image.]


## [2026-09-14T02:05:42.982Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg442hi-442.png'); W,H=im.size\nc=im.crop((int(W*0.70),int(H*0.478),int(W*0.78),int(H*0.497)))\nc=c.resize((c.width*5,c.height*5), Image.LANCZOS)\nc.save('c442-symp-zoom.png'); print(c.size)\nEOF",
 "description": "Zoom sampozium word"
}
```


### [2026-09-14T02:05:44.753Z] TOOL RESULT

```
(2040, 630)
```


## [2026-09-14T02:05:47.274Z] TOOL CALL #71: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c442-symp-zoom.png"
}
```


### [2026-09-14T02:05:47.489Z] TOOL RESULT

```

```


## [2026-09-14T02:05:47.486Z] INPUT

[Image: original 2040x630, displayed at 2000x618. Multiply coordinates by 1.02 to map to original image.]


## [2026-09-14T02:06:01.075Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npdftotext -f 442 -l 442 EtymologicalDictionary-persian-english.pdf - 2>/dev/null | head -60",
 "description": "Extract text layer of page 442"
}
```


### [2026-09-14T02:06:02.179Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T02:06:19.608Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad\npdftoppm -f 442 -l 442 -r 1200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf pg442uhi-442 2>/dev/null\npython3 - <<'EOF'\nfrom PIL import Image\nim=Image.open('pg442uhi-442.png'); W,H=im.size; print(W,H)\nc=im.crop((int(W*0.705),int(H*0.480),int(W*0.775),int(H*0.496)))\nc=c.resize((c.width*3,c.height*3), Image.LANCZOS); c.save('c442-symp-zoom2.png'); print(c.size)\nEOF",
 "description": "Ultra-high-res crop of sampozium"
}
```


### [2026-09-14T02:06:34.358Z] TOOL RESULT

```
/usr/lib/python3/dist-packages/PIL/Image.py:3186: DecompressionBombWarning: Image size (134640000 pixels) exceeds limit of 89478485 pixels, could be decompression bomb DOS attack.
  warnings.warn(
10200 13200
(2142, 633)
```


## [2026-09-14T02:06:36.906Z] TOOL CALL #74: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c442-symp-zoom2.png"
}
```


### [2026-09-14T02:06:37.096Z] TOOL RESULT

```

```


## [2026-09-14T02:06:37.093Z] INPUT

[Image: original 2142x633, displayed at 2000x591. Multiply coordinates by 1.07 to map to original image.]


## [2026-09-14T02:07:06.110Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### WLD Bd2 sem-\"; python3 - <<'EOF'\nimport re\nt=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'sem-\\s*\\(?:?\\s*som', p) or ('in eins zusammen' in p) or ('sem-' in p and 'som-' in p and 'eins' in p):\n        print('leaf',i, p[:400].replace('\\n',' ')); print('...')\nEOF",
 "description": "Walde-Pokorny sem- entry"
}
```


### [2026-09-14T02:07:07.417Z] TOOL RESULT

```
### WLD Bd2 sem-
leaf 494 490                                           sem   „in einem, zugleich“ (ob nach Brugmann II ^ 2, 897 als ^a^ar mit ai. smaf bildungsverwandt?), wozu a/urjodjuevog    ovvayaycov Hes., d/ndouai (e^-,                                                      *     jTOoa-, xar-, oov-) ^sammle^^, dvrXog „Haufen Getreide, Schober^, djuaXla „Garbe“ (s. Schulze Qu. ep. 365 Anm. 3, Solmsen Beitr. 1 185, Becht
...
leaf 495                                                   sem-                                      491  Geschlecht^, gr. djuoyviog ds.,           ai. sama-jatJya „gleichartig‘', anord. samfedra,  S/LioTidrcoQ     ap. hamapiter-’       „von demselben Yater'^ smmmdri^ ofiojxrixQiog „von derselben Mutter^'.    Auf ein ^-Pem. ^sonu^ *sml „B^isammensein, groBer Haufe, Yereinigung, z. T. auch kampfendes Aneina
...
```


## [2026-09-14T02:07:08.053Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### SYN Buck 'same'\"; grep -n \"SAME\\b\" SYN.txt | head -5\necho \"### SKT simple\"; grep -n \"^SIMPLE\\|Simple\\.\" SKT.txt | head -5\necho \"### LKT samovar\"; grep -n -i \"samowar\\|samovar\" LKT.txt | head -5",
 "description": "Buck, Skeat, Lokotsch greps"
}
```


### [2026-09-14T02:07:08.148Z] TOOL RESULT

```
### SYN Buck 'same'
### SKT simple
17295:Simple.  (F.-LO  F.  simple. '^'L.  sim- pHcfm,  ace.  of  simplex,  lit.  'one-fold.'  — L.  sim-^  from  the  base  sama*,  the  same (appearing  also  in  sin-guii,  one  hj  one, sem-el,  once,  sim-ul,  together) ;  anil  piie-, from  pHeare,  to  fold :  see  Same  and  Fly. Der.  simplicity,  F.  simplicity,  froin  L.  ace simpHcitatem  ;  simpli-fy,  to  make  simple.
### LKT samovar
```


## [2026-09-14T02:07:22.475Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### MON samavar\"; grep -o \".\\{80\\}سماور.\\{160\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -4\necho \"### MON symphony\"; grep -o \".\\{40\\}سمفونی.\\{160\\}\" MON_part1.txt MON_part2.txt 2>/dev/null | head -3\necho \"### ARY anjoman\"; grep -n \"انجمن\\|اندرز\\|هنگام\" incoming/ARY/ARY_pages.txt | head -8",
 "description": "Mo'in and Aryanpur greps"
}
```


### [2026-09-14T02:07:22.607Z] TOOL RESULT

```
### MON samavar
### MON symphony
### ARY anjoman
917:۱-برابری و اخوت.۲- رفتار نیمه جنونآمیز و سرمستانه هنگام نبرد یا تهاجم یا مراسم وابسته به
988:(81371۸86/3) گزارش می‌دهند که حتی در قرن سوم بیش از میلاد نیز رومیان هنگام احساس خطر
1083:می‌شد. در روم باستان» هنگام جنگ کشاورزان عادی تبدیل به سربازان ماهر می‌شدند. در اسپارت
1174:چون در آن هنگام هنوز الفپا اختراع نشده بود. ولی بررسی واژگان کهن‌ترین متوّن سانسکریت و
10998:چم این واژه در زبان‌های ژرمنی: استراحت» مدت» هنگام.
12450:۰ | کی (به چم "چه وقت"» "چه هنگام")
```


## [2026-09-14T02:07:30.038Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D8%B3%D9%85%D8%A7%D9%88%D8%B1/\" --note \"page 442: Mo'in entry for سماور (MON:1918)\" 2>&1|tail -1\npython3 tools/fetch_source.py \"https://vajehyab.com/?q=%D8%B3%D9%85%D8%A7%D9%88%D8%B1&d=moein\" --note \"page 442: Mo'in سماور\" 2>&1|tail -1",
 "description": "Fetch Mo'in entry for samavar"
}
```


### [2026-09-14T02:07:32.900Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/4a6b49c3f8426395.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6b12397f08a11eba.txt
```


## [2026-09-14T02:07:36.008Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\ngrep -o \"معین.\\{0,250\\}\" 4a6b49c3f8426395.txt | head -5; echo \"-----\"; grep -o \"سماور.\\{0,200\\}\" 4a6b49c3f8426395.txt | head -6; echo \"==== vajehyab\"; grep -o \"سماور.\\{0,200\\}\" 6b12397f08a11eba.txt | head -5",
 "description": "Read Mo'in samavar entry"
}
```


### [2026-09-14T02:07:37.084Z] TOOL RESULT

```
معین ). 
معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل 
-----
سماور - معنی در دیکشنری آبادیس
سماور - معنی در دیکشنری آبادیس 
سماور
سماور. [ س َ وَ ] ( روسی ، اِ ) یک قسم ابزاری فلزی جهت جوش آوردن آب که آتش خانه را در میانش قرار داده اند.
سماور
سماور واژه ای روسی �самовар� به معنای خودجوش یا وسیله ای که خودش آب را می جوشاند می باشد . 
==== vajehyab
سماور | واژه یاب
سماور | واژه یاب 
سماور
سماور گذارند تا دود را خارج کند. 2 - سوراخ بالای آسیا که آب از آن روی پره های آسیا ریزد.
سماور و ظرف های آشپزخانه به کار می رفت .
```


## [2026-09-14T02:08:59.387Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BRT.txt',encoding='utf-8',errors='replace').read()\nfor pat in [r'han-dar3za', r'han-dar', r'h9n-dar', r'darazayeiti', r'han-gama', r'han-gam']:\n    ms=list(re.finditer(pat,t))\n    print(pat, len(ms))\n    for m in ms[:2]:\n        print('   ', t[max(0,m.start()-200):m.start()+300].replace('\\n',' '))\nEOF",
 "description": "Bartholomae han-darəz / han-gama"
}
```


### [2026-09-14T02:09:00.432Z] TOOL RESULT

```
han-dar3za 0
han-dar 0
h9n-dar 0
darazayeiti 0
han-gama 0
han-gam 0
```


## [2026-09-14T02:09:03.183Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -o \"han-[a-z0-9ə8]\\{2,12\\}\" BRT.txt | sort | uniq -c | sort -rn | head -40",
 "description": "List han- compounds in Bartholomae OCR"
}
```


### [2026-09-14T02:09:04.374Z] TOOL RESULT

```
      1 han-ta
      1 han-kusra
      1 han-kana
      1 han-iifi
      1 han-gnt
      1 han-dvar3na
      1 han-draxta
      1 han-draman
      1 han-danian
```


## [2026-09-14T02:09:11.478Z] TOOL CALL #82: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg442-p442.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/442.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/442.png",
 "description": "Copy page image for audit"
}
```


### [2026-09-14T02:09:11.582Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 84851 Sep 13 22:09 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/442.png
```


## [2026-09-14T02:09:14.028Z] TOOL CALL #83: Bash

```json
{
 "command": "sed -n '1,60p' /home/sfmqrb/git/rishe/tools/verify_check.py",
 "description": "Inspect verify_check requirements"
}
```


### [2026-09-14T02:09:14.082Z] TOOL RESULT

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
```


## [2026-09-14T02:09:25.941Z] AGENT

Now I'll write the verification file.


## [2026-09-14T02:18:05.980Z] TOOL CALL #84: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-442.json",
 "content": "{\n  \"pdf_page\": 442,\n  \"book_page\": 412,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Sem 1, Sm\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *sem- 'one; as one, together with' (zero grade *sm̥-), Pokorny 2. sem- 902-905; Watkins/AHD sem-1\",\n      \"note\": \"Pokorny IEW pp. 902-905 (POK_03.txt leaves 137-142) heads the entry '2. sem- „eins“ und „in eins zusammen, einheitlich, samt, mit“' and organises it exactly as Nourai's chart does: (1) numeral 'one' (Gk. εἷς, Lat. semper, sem-per), (2) *semo- 'irgendeiner' (Skt. sama-, Av./OP hama-), (3) '*in eins = zusammen, mit': sm̥- (Skt. sa-ha, Av. hada, OP hadā), som- (Skt. sám-, Av./OP ha(m)- 'mit'), and *somo-s (Gk. ὁμός, Av./OP hama-, Goth. sama). Watkins (AHD, sem-1) gives the same root with the gloss 'One; also adverbially \\\"as one,\\\" together with', citing '[Pok. 2. sem- 902.]'. Nourai's headword 'Sem 1' = the full grade *sem-, 'Sm' = the zero grade *sm̥- (Kent's pIE *sm̥-, s.v. OP ha-). Root, language label and the implicit gloss are all correct, and the two page numbers he cites (902 for the head of the entry, 904 for the *somo-s section that feeds the Greek and Russian boxes) are exact. The one systemic caveat, flagged at the Greek node below, is that Pokorny himself (p. 904) and all later authorities detach Greek σύν/ξύν from this root.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *sem- «یک؛ با هم، یکجا» (صورت صفر آن *sm̥-) در فرهنگ پوکورنی (چاپ ۱۹۵۹، صص ۹۰۲–۹۰۵) زیر سرواژهٔ «2. sem- „eins“ und „in eins zusammen“» و در پیوست واتکینز (AHD) زیر sem-1 ثبت شده است؛ پس نام ریشه، برچسب زبانی و ارجاع صفحه‌ای نورایی هر سه درست است. آنچه نورایی «Sm» می‌نامد همان ستاک صفرِ *sm̥- است که در ایرانی باستان به ha-/ham- و در سنسکریت به sa-/sam- بدل شده است (کنت، ذیل ha-). تنها اشکال بنیادین — که در جعبهٔ یونانی پایین‌تر شرح داده شده — این است که خودِ پوکورنی در ص ۹۰۴ و پس از او واتکینز، کلاین و بیکس واژهٔ یونانی σύν/ξύν را از این ریشه جدا می‌کنند و آن را به *ksun بازمی‌گردانند. در مجموع: ادعای نورایی دربارهٔ خودِ ریشه درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/sem-\",\n        \"https://www.etymonline.com/word/samovar\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:902\",\n          \"status\": \"supports\",\n          \"note\": \"POK_03.txt leaf 137 (printed p. 902): '2. sem- „eins“ und „in eins zusammen, einheitlich, samt, mit“. 1. Mit vorherrschender Zahlwortbedeutung „eins“: Arm. mi „eins“ (*sm-ios); gr. εἷς, ἕν, μία (*sems, *sem, *sm-ia) ... lat. sem-per „in einem fort, immer“'. Exactly the root Nourai draws.\"\n        },\n        {\n          \"ref\": \"POK:904\",\n          \"status\": \"supports\",\n          \"note\": \"POK_03.txt leaf 141 (printed p. 904): 'Von som- stammt somo-s: ai. samá- „eben, gleich, derselbe“ ... av. ap. hama- „gleich, derselbe“ ... gr. ὁμός „gemeinsam; ähnlich, gleich, eben, glatt“, ὁμοῦ Adv. „zusammen“ ... got. sama „derselbe“'. This is the page that underwrites the Greek and the Germanic boxes.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. sem-1 (AHD_watkins1985.txt line 916)\",\n          \"stance\": \"supports\",\n          \"note\": \"'sem-1. One; also adverbially “as one,” together with. I. Full-grade form *sem- ... II. O-grade form *som- ... III. Lengthened o-grade form *sōm- ... IV. Zero-grade form *sm̥- ... [Pok. 2. sem- 902.]' — the full derivative list covers SINGLE, SIMPLE, SIMILAR, SIMULTANEOUS, ASSEMBLE, RESEMBLE, SAME, SOME, SEEM, HOMO-, ANOMALOUS, SAMOVAR, i.e. every English word in Nourai's boxes except the syn- words.\"\n        },\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny II 488-491 (incoming/WLD/WLD_Bd2_pages.txt leaves 494-495)\",\n          \"stance\": \"supports\",\n          \"note\": \"The sem- article runs over printed pp. 490-491 with 'sem „in einem, zugleich“' and '*somo-s ... gr. ὁμός ... ὁμοπάτωρ, ap. hamapitar- „von demselben Vater“, ὁμομήτριος' — the same material Pokorny later condensed.\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, col. 1246 (IEC.txt leaf 687)\",\n          \"stance\": \"supports\",\n          \"note\": \"'somos „together, like, equal, one, some, the same”. WP II, 490. Cf. som-, sem- and sm- | Skt. samáh ... Av. hamō ... Gk. homós, adj. “like, equal”; homo-, cpds.' — Mann's col. 1245 has 'somolos ... Gk. homalós'.\"\n        },\n        {\n          \"src\": \"KNT\",\n          \"where\": \"Kent, Old Persian, Lexicon p. 211 s.v. ha-\",\n          \"stance\": \"supports\",\n          \"note\": \"'ha- insep. prefix, anteconsonantal: Av. ha-, Skt. sa-, Gk. ἁ-, Lt. sem-, pIE *sm̥-, zero-grade of pIE *sem- “one”, Gk. εἷς ἕν; in hakara-, hadā. See also ham-, hama-.' — this is the explicit source for Nourai's second headword 'Sm'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"han-jâmana; han-jâma; han-gmatana; han-vaěg\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The prefix is Old Iranian *ham- (Av. ham-/haṇ-, OP ham-) < PIE *som-, which before a following consonant assimilates to haṇ-/han-; the arrow root -> Avestan is therefore right in principle. Word by word: (1) haṇjamana- 'assembly, gathering' is genuine Avestan (Y 12.5 'hanjamanaiš', Y 72.5 'vīspaēšū ... hanjamanaēšū \\\"bei allen Zusammenkünften\\\"'), Bartholomae AiW col. 1770; = ham- + jam-/gam- 'to come' — confirmed. (2) 'han-jâma \\\"come to end\\\"' is not an attested Avestan lemma; Horn (Grundriss no. 113) and Wiktionary reconstruct the etymon of NP anjām as Old Persian *hanjāma- 'Ende, Abschluss', and Avestan only supplies the finite hənjasəṇte 'they are brought to a close' — the form is real but the language label should be Old Persian (reconstructed). (3) 'han-gmatana' is Old Persian Haᵑgmatāna- 'Ecbatana', Kent Lexicon p. 212, not Avestan (Spiegel's normalisation Hangmatāna is quoted by Mo'in at BQT 2368) — again mislabelled. (4) 'han-vaēg \\\"swing together, excite\\\"' is the weak link: Avestan does have vaēj-/vij- 'to shake, swing' (Cheung, *uaij), and Horn 1893:30 compared Skt. sam-vigna- and Pahlavi hamvēxt, but Cheung (2007, s.v. *gaiz) derives MP hangēz-/hangēxtan — the actual etymon of NP angīxtan — from *ham-gaiz- 'to disturb, stir, incite', because *ham-vaij- would have given MP **hanwēz-/hamwēz-, not the attested hangēz- with g. On that word modern scholarship prefers a different second element, so the node takes the verdict 'disputed'.\",\n          \"derivation_fa\": \"پیشوند این جعبه ایرانی باستان *ham- (اوستایی ham-/haṇ-، پارسی باستان ham-) از هندواروپایی *som- است که پیش از همخوان به haṇ-/han- بدل می‌شود؛ پس پیکانِ «ریشه ← اوستایی» در اصل درست است. اما واژه‌به‌واژه: (۱) haṇjamana- «انجمن، گردهمایی» اوستایی اصیل است (یسنا ۱۲٫۵ و ۷۲٫۵) و بارتولومه آن را در ستون ۱۷۷۰ آورده است — درست. (۲) *han-jāma «به پایان رسیدن» در اوستا گواهی نشده؛ هرن (بند ۱۱۳) و ویکی‌واژه ریشهٔ «انجام» را پارسی باستانِ بازسازی‌شدهٔ *hanjāma- می‌دانند، پس برچسب زبانی باید «پارسی باستان» باشد. (۳) han-gmatana در حقیقت پارسی باستان Haᵑgmatāna- «هگمتانه» است (کنت، ص ۲۱۲؛ معین در حاشیهٔ برهان ص ۲۳۶۸ صورت Hangmatāna اشپیگل را نقل می‌کند) و اوستایی نیست. (۴) han-vaēg نقطهٔ ضعف این جعبه است: اگرچه ستاک اوستایی vaēj-/vij- «جنبیدن، لرزاندن» واقعی است و هرن (۱۸۹۳، ص ۳۰) آن را با سنسکریت sam-vigna- سنجیده، چونگ (۲۰۰۷، ذیل *gaiz) فارسی میانهٔ hangēxtan/hangēz- را از *ham-gaiz- «برانگیختن، آشفتن» می‌گیرد، زیرا *ham-vaij- در فارسی میانه به hanwēz- می‌انجامید نه hangēz-. بنابراین پژوهش امروزی این یک بند را رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%D9%85%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%D8%A7%D9%85\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:902-904\",\n              \"status\": \"partial\",\n              \"note\": \"POK_03.txt leaf 141 (p. 904): 'som-: ai. sám- „zusammen, zugleich mit“, av. ap. ha(m)- „mit“ (in Verbindung mit Verben und in Zs. mit Nomina ...)'. Pokorny confirms the Avestan/Old Persian prefix ham- under this root, but he cites none of Nourai's four compounds.\"\n            },\n            {\n              \"ref\": \"HRN:30\",\n              \"status\": \"supports\",\n              \"note\": \"Horn, Grundriss p. 30 no. 127 (HRN.txt leaf 51): 'engēḵtan ‚antreiben‘, Praes. engēz-em, phlv. angēxtan ‚antreiben‘, angēǰēt (AV.), vergl. ham|vēḵt (Geiger, Yātk. Zar., Anm. 52); skr. vgl. samvigna- ‚aufgeregt‘.' — this is exactly Nourai's han-vaēg -> angīxtan claim, and it is Horn's (1893) view; Cheung 2007 supersedes it.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW col. 1770 s.v. hanjamana-\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt shows the headword line 'hanjamana- 1770' and the citations 'vīspaēšu frasnāiti vīspaēšu hanjamanaēšū ... „bei allen Besprechungen, bei allen Zusammenkünften“ Y. 72.5'; the neighbouring column has 'han-kərətay-, hən-kə „Vollziehung, Vollendung“' — i.e. a whole family of Av. ham-/han- compounds, but no *han-davaθa- and no *han-vaēg-.\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon p. 212 s.v. Haᵑgmatāna-\",\n              \"stance\": \"partial\",\n              \"note\": \"'Haᵑgmatāna- sb. “Ecbatana”, a royal residence in Media: Elam. ag-ma-da-na, Akk. a-ga-ma-ta-nu, Gk. (Hdt.) Ἀγβάτανα, (Aesch., Aristoph.) Ἐκβάτανα, NPers. Hamadān. Probably deriv. of ha-gmata- (q.v., under gam-): “City of Gatherings”.' Supports the derivation, contradicts the language label 'Avestan'.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007, s.v. *gaiz (p. 97 f.) and *uaij (p. 413)\",\n              \"stance\": \"contradicts\",\n              \"note\": \"s.v. *gaiz '? to disturb, stir, incite, excite': '(+ *ham-) BMP hngyc- /hangēz-/ “to arouse, stimulate, stir up” ... (+ *ham-) NP angextan/angez- “to stir up, incite”'. The separate root *uaij 'to shake, swing' (YAv. vij-) yields MP wēz-/wextan and NP bēxtan, āvēxtan — not angēxtan.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien §107 (HUB.txt line 7684) and p. 114 note\",\n              \"stance\": \"supports\",\n              \"note\": \"'ap. ham- = np. an- in anjuman ‚Versammlung‘ = zd. hanjamana-; andām ‚Körper, Glied‘ = zd. handāma-; angārdan ‚meinen‘, zd. hankārayemi ... Doch erscheint h noch in hanjar ... und hangām, hingām ‚Zeit‘' — the sound law behind the whole box; and his note to Horn no. 114: 'Hier fehlt zd. hanjamana- ‚Versammlung‘.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"anjoman «انجمن»; anjâm «انجام ( سرانجام )»; Ekbâtân «اکباتان ( همدان )»; angîxtan «انگیختن ( انگیزه )»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"All four are regular New Persian outcomes of Old Iranian *ham-compounds, with the sound change described by Hübschmann §107 (initial h- of *ham- is lost in New Persian, and m assimilates to n before the following stop/affricate): (1) انجمن anjoman < MP hanjaman [hncmn'] 'gathering, assembly, congregation' (MacKenzie, CPD 41) < Av. haṇjamana-; the Arabic loan هنزمن hinzamn 'crowd' preserves the h- (Horn no. 114). (2) انجام anjām < MP hanjām [hnc'm] 'end, completion, outcome' (MacKenzie), with the verb hanjāftan, hanjām- 'finish, complete'; < OIr. *ham-gāma- (Wiktionary: PIr *ham- + *gam- 'to come' < PIE *gʷem-, hence the chart's cross-reference to Gwa); the derivative سرانجام sar-anjām is a later New Persian compound. (3) اکباتان/همدان: OP Haᵑgmatāna- 'place of assemblies' > Greek Ἀγβάτανα (Herodotus) and Ἐκβάτανα (Aeschylus, Aristophanes) > Latin Ecbatana > the modern learned Persian اکباتان; the inherited line OP Haᵑgmatāna- > MP Hamadān gives modern همدان (Mo'in's footnote at Borhan p. 2368 lists Pahl. Hamatān, OP Hagmatāna, Elam. Ag-ma-ta-na, Akk. A-ga-ma-ta-nu, Gk. Ἀγβάτανα/Ἐκβάτανα, 'from hangmata, root GAM, meaning \\\"place of assemblies\\\"'). (4) انگیختن angīxtan < MP hangēxtan, hangēz- 'arouse, stimulate, stir up' (MacKenzie; Horn no. 127), with the modern deverbal انگیزه angīza 'motive'; the Middle-to-New Persian step is certain, but the Old Iranian etymon is *ham-gaiz- (Cheung) rather than the chart's *ham-vaig-, so this one word is only 'plausible'.\",\n          \"derivation_fa\": \"هر چهار واژه بازماندهٔ قاعده‌مند ترکیب‌های ایرانی باستان با پیشوند *ham- اند و قانون آوایی‌ای که هوبشمان (بند ۱۰۷) بیان کرده بر آن‌ها حاکم است: «ه» آغازیِ ham- در فارسی نو می‌افتد و «م» پیش از همخوان انسدادی/سایشی به «ن» بدل می‌شود. (۱) «انجمن» از فارسی میانهٔ hanjaman «گردهمایی، مجمع» (مکنزی، ص ۴۱) از اوستایی haṇjamana-؛ صورت معرّبِ «هنزمن» هنوز «ه» را نگاه داشته است (هرن، بند ۱۱۴). (۲) «انجام» از فارسی میانهٔ hanjām «پایان، سرانجام» و فعل hanjāftan/hanjām-، از ایرانی باستان *ham-gāma- «به هم آمدن» (ویکی‌واژه: *ham- + *gam-)؛ «سرانجام» ترکیب متأخر فارسی نو است. (۳) «هگمتانه»ی پارسی باستان (Haᵑgmatāna-) در یونانی به Ἀγβάτανα و Ἐκβάτανα و از آنجا به لاتین Ecbatana و سپس به صورت عالمانهٔ «اکباتان» به فارسی بازگشته است، حال آنکه صورت موروثی همان «همدان» است؛ معین در حاشیهٔ برهان قاطع (ص ۲۳۶۸) دقیقاً همین زنجیره را با ارجاع به کنت و اشپیگل آورده و معنای آن را «جای [شهر] اجتماعات» از ریشهٔ GAM دانسته است. (۴) «انگیختن» از فارسی میانهٔ hangēxtan/hangēz- «برانگیختن» (مکنزی؛ هرن بند ۱۲۷) و «انگیزه» مشتق نوِ آن؛ گذارِ فارسی میانه به فارسی نو قطعی است، اما صورت ایرانی باستانِ آن بنا بر چونگ *ham-gaiz- است نه *ham-vaig-. پس: ادعای نورایی در سه واژه درست و در «انگیختن» با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%D9%85%D9%86\",\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AC%D8%A7%D9%85\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:167\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan-e Qate' printed p. 167 = BQT_v1_pages.txt leaf 385: 'انجمن ۱ - به ضم اول و فتح میم و سکون نون، مجلس و مجمع را گویند - بمعنی گروه' — the headword is on the page Nourai cites (the page number is confirmed by the footnote continuation notes 'بقیه در صفحهٔ ۱۷۱' on leaf 389 / 'بقیه از صفحهٔ ۱۷۱' on leaf 390). Mo'in's Latin-script etymological footnote is present at the foot of the leaf but the Persian OCR of it is unreadable.\"\n            },\n            {\n              \"ref\": \"BQT:166\",\n              \"status\": \"partial\",\n              \"note\": \"BQT_v1_pages.txt leaf 384 (= printed p. 166) carries the انجام entry ('انجام ... و آخر هر کار و هر چیز باشد'); the entry is there, but the OCR of the etymological footnote is illegible.\"\n            },\n            {\n              \"ref\": \"BQT:2368\",\n              \"status\": \"supports\",\n              \"note\": \"Borhan vol. 4, printed p. 2368 (pdf page 451, incoming/BQT/BQT_v4_pages.txt), Mo'in's footnote 5: 'همدان - بفتح اول و دوم، پهلوی Hamatān «مارکوارت، شهرستانهای ایران»، پارسی باستان Hagmatāna «کنت»، Hangmatāna «اشپیگل» ... که پایتخت شاهی در عهد مادها بود. در عیلامی Ag-ma-ta-na، آکدی A-ga-ma-ta-nu، یونانی Ἀγβάτανα ... محتملا مشتق از', continued on the next page as 'hangmata (از ریشهٔ GAM) بمعنی (جای [شهر] اجتماعات) رک: کنت ایضاً، اشپیگل ایضاً'. Exactly Nourai's claim, on exactly the page he cites.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 41 (PHD.txt line 394)\",\n              \"stance\": \"supports\",\n              \"note\": \"'hanjaman [hncmn'] (P ʾnjmn, M hnzmn), N anjuman] gathering, assembly, congregation, community'; 'hanjām [hncʾm | N anjām] end, completion, outcome'; 'hangēxtan, hangēz- [hngyhtn', hngyc- | N an~] arouse, stimulate, stir up'. All three Middle Persian antecedents in one column.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, glossary s.v. hanjaman\",\n              \"stance\": \"supports\",\n              \"note\": \"'hanjaman [hncmn'] meeting, assembly, congregation 42.14, 66.15 ... — Av. (1770) hanjamana-; MPrth hnjmn; NP anjuman; Ps. ʾnwmnyhʾy “congregations”.' Nyberg's cross-reference to Bartholomae col. 1770 is the same one used above.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss nos. 113-114 (pp. 26-27) and no. 127 (p. 30)\",\n              \"stance\": \"supports\",\n              \"note\": \"'113. enjām ‚Ende‘ ... ap. *hanjāma- ‚Ende, Abschluss‘ ... phlv. anjām, anjāmīnītan (Bund.), bezw. han-.' | '114. enjumen ‚Versammlung‘. ap. *hanjamana-; phlv. hanjaman bezw. anjaman; ... arab. LW. hinzamn ‚Menschenmenge‘.' | '127. engēḵtan ‚antreiben‘ ... phlv. angēxtan.'\"\n            },\n            {\n              \"src\": \"KNT\",\n              \"where\": \"Kent, Old Persian, Lexicon p. 212\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. Haᵑgmatāna-: '... Gk. (Hdt.) Ἀγβάτανα, (Aesch., Aristoph.) Ἐκβάτανα, NPers. Hamadān. Probably deriv. of ha-gmata- ...: “City of Gatherings”.' The Greek doublet Ἀγβάτανα/Ἐκβάτανα is the source of both اکباتان and Ecbatana.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"han-davatha; han-du; han-dareza; han-gama\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Again the prefix is Old Iranian *ham- < PIE *som-, correctly attached to the root; the trouble is in two of the four second elements. (1) 'han-davatha \\\"depressed\\\"', offered as the etymon of NP اندوه, is not an attested Avestan word, and modern Iranian etymology derives andōh from an entirely different verb: Cheung (2007) s.v. *θuaxš/tuxš 'to be busy, working on' (Av. θβaxš-, OAv. θβaxšah- 'effort', OP hamataxš- 'to work with') lists '(+ *ham-) BMP ʾndwh /andōh/ \\\"sorrow\\\"', with Sogd. ʾnt(ʾ)wxs 'to strive', Chorasmian ʾndyx 'sorrow' and Arm. LW andohakan. So the chart's cross-reference to Dheu 2 is rejected. (2) 'han-du \\\"to smear together\\\"' is sound in substance: Cheung's Iranian root *dauH² 'to smear, rub (on)' shows '(+ *ham-) NP andūdan/anday- \\\"to smear\\\"' beside Buddhist Sogdian ʾnδʾw 'to smear, anoint' — though Cheung warns that 'IE cognates cannot be cited in support of Ir. *dauH \\\"to smear\\\"', so the further link to PIE *dheu- (chart: Dheu 3) is doubtful. (3) 'han-dareza' = *ham-darza-, from Av. darəz- 'to bind, fasten' (whence also NP درز darz 'seam'), gives MP handarz 'advice, injunction, testament' — confirmed. (4) 'han-gama' = *ham-gāma- 'a coming together, (appointed) time', from gam- 'to go, come' (chart: Gwa), gives MP hangām — confirmed.\",\n          \"derivation_fa\": \"پیشوند این جعبه نیز همان *ham- ایرانی باستان از *som- هندواروپایی است و پیوند آن با ریشه درست است؛ اشکال در دو جزء دوم است. (۱) *han-davaθa- «افسرده» که نورایی آن را ریشهٔ «اندوه» می‌داند در اوستا گواهی نشده، و ریشه‌شناسی امروزی andōh را از ستاک دیگری می‌گیرد: چونگ (۲۰۰۷) ذیل *θuaxš/tuxš «کوشیدن، سرگرم بودن» (اوستایی θβaxš-، پارسی باستان hamataxš-) صورت «(+ *ham-) ʾndwh /andōh/ “اندوه”» را آورده و سغدی ʾntwxs و خوارزمی ʾndyx «اندوه» را گواه می‌گیرد. پس ارجاع نورایی به ریشهٔ Dheu 2 مردود است. (۲) han-du «اندودن» از دید ماده درست است: چونگ ذیل *dauH² «اندودن، مالیدن» می‌آورد «(+ *ham-) فارسی نو andūdan/anday-» و سغدی بودایی ʾnδʾw «اندودن»؛ ولی خود او تصریح می‌کند که برای این ریشهٔ ایرانی هم‌ریشهٔ هندواروپایی نمی‌توان آورد، پس پیوند با Dheu 3 مشکوک است. (۳) han-dareza همان *ham-darza- از ستاک اوستایی darəz- «بستن» (که «درز» فارسی نیز از آن است) و در فارسی میانه handarz «اندرز، وصیت» — درست. (۴) han-gama همان *ham-gāma- «به هم آمدن، وقت» از gam- که به hangām فارسی میانه رسیده — درست.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D9%87%D9%86%DA%AF%D8%A7%D9%85\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT:172\",\n              \"status\": \"partial\",\n              \"note\": \"Printed pp. 171-172 of Borhan-e Qate' (BQT_v1_pages.txt leaves 389-390) are indeed the اندودن / اندوه / اندوختن stretch ('اندودن - بروزن فرمودن، کاهگل و گلابه مالیدن باشد', 'اندوه - بروزن انبوه، گرفتگی دل و دلگیری را گویند'), and اندرز stands two leaves earlier (leaf 388 = p. 170); Mo'in's Latin-script footnotes are printed at the foot of these pages but the Persian OCR renders them as garbled strings ('و اوزن ...'), so their exact wording could not be quoted. The page reference is right; it is a Persian dictionary page and says nothing about Avestan *han-davaθa-.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007 s.v. *θuaxš (tuxš), p. 400, and s.v. *dauH² 'to smear, rub (on)', p. 67 ff.\",\n              \"stance\": \"contradicts\",\n              \"note\": \"*θuaxš: 'Av. θβaxš- “to take care of” ... OP (+ *ham-) haᵐtaxš- “to work with, effect” ... (+ *ham-) BMP ʾndwh /andōh/ “sorrow”, MMP ʾndwxyn “sad” ... CHORESMIAN (+ *ham-) ʾndyx “sorrow, sadness” ... NWIR: NP tuxšidan “to strive” ... (+ *ham-) NP andoh “anxious”'. This contradicts Nourai's han-davaθa/Dheu 2. For andūdan it supports him: '*dauH² “to smear, rub (on)” ... BSogd. ʾnδʾw “to smear, anoint” ... (+ *ham-) NP andudan/anday- “to smear”'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 41 (PHD.txt lines 392-394)\",\n              \"stance\": \"supports\",\n              \"note\": \"'handarz [hndlc | N andarz] advice, injunction, testament'; 'handūdan, *handāy- [hndwtn' | (M ʾnwd), N an~] smear, plaster, anoint'; 'hangām [hngʾm | N ~] time, occasion'. Three of the four Persian outcomes have their Middle Persian ham-forms here; MacKenzie has no entry for *handōh.\"\n            },\n            {\n              \"src\": \"NYB\",\n              \"where\": \"Nyberg, Manual of Pahlavi II, s.vv. handarz, hangām, handōhakān\",\n              \"stance\": \"supports\",\n              \"note\": \"'handarz [hndlc'] counsel, advice 41.9, 62 — Ps. hndlcy “command, law”; MPrs ʾndrz (S); NP andarz.'; 'hangām [hngʾm] time, epoch, season — MPrs ʾngʾm (S); Paz. hangām; NP hangām.'; 'handōhakān [hndwhkn'] anxious — Arm. lw. andohakan “disquieting, dreadful”.'\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW cols. ~1765-1790 (han-/hąm- compounds)\",\n              \"stance\": \"silent\",\n              \"note\": \"A grep of BRT.txt for han- compounds yields han-kərətay-, han-dvarəna-, han-draxta-, han-kana-, hanjamana- etc., but no *han-davaθa-, no *han-darəza- and no *han-gama- as headwords — the first of these appears to be Nourai's own reconstruction.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Persian\",\n          \"words\": \"andŭh «اندوه»; andŭdan «اندودن»; andarz «اندرز»; hengâm «هنگام»\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"Three of the four are textbook cases of the Hübschmann §107 rule (*ham- > an-, with h- lost): اندودن andūdan < MP handūdan, handāy- 'smear, plaster, anoint' (MacKenzie) < *ham-dauH-; اندرز andarz < MP handarz 'advice, injunction, testament' (MacKenzie, Nyberg) < *ham-darza-; هنگام hangām < MP hangām 'time, occasion' — one of the few words (with hanjar) in which the initial h- was NOT lost, as Hübschmann expressly notes ('Doch erscheint h noch in ... hangām, hingām ‚Zeit‘'), and Wiktionary analyses it as han- (= ham- 'co-') + gām 'step'. The fourth, اندوه andūh, is real and does continue MP andōh 'sorrow' (Wiktionary: 'Inherited from Middle Persian ʾndwh /andōh/ \\\"sorrow\\\"'), but its Old Iranian source is *ham-tuxš-/*ham-θβaxš- 'to strive, be hard put' (Cheung, with Sogd. ʾntwxs, Chorasmian ʾndyx 'sorrow'), not the chart's *han-davaθa-; the semantic path was 'to be hard pressed, exert oneself' > 'distress, grief'. The node therefore takes the verdict of its worst word.\",\n          \"derivation_fa\": \"سه واژه از چهار واژهٔ این جعبه نمونه‌های آشکار همان قاعدهٔ هوبشمان‌اند (*ham- > an- با افتادن «ه»): «اندودن» از فارسی میانهٔ handūdan/handāy- «اندودن، گچ‌کاری کردن» (مکنزی) از *ham-dauH-؛ «اندرز» از فارسی میانهٔ handarz «پند، وصیت» (مکنزی، نیبرگ) از *ham-darza-؛ و «هنگام» از فارسی میانهٔ hangām «وقت» که — چنان‌که خود هوبشمان تصریح می‌کند — از معدود واژه‌هایی است که «ه» آغازین در آن‌ها نیفتاده است، و ویکی‌واژه آن را han- (= هم-) + gām «گام» تحلیل می‌کند. اما «اندوه» هرچند به‌درستی دنبالهٔ andōh فارسی میانه است، ریشهٔ ایرانی باستانش *ham-tuxš-/*ham-θβaxš- «کوشیدن، در تنگنا بودن» است (چونگ؛ با گواه سغدی ʾntwxs و خوارزمی ʾndyx «اندوه») نه *han-davaθa-؛ تحول معنایی آن «در فشار بودن، کوشیدن» ← «غم، اندوه» است. پس پژوهش امروزی این یک بند را رد می‌کند و بقیهٔ جعبه درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D9%87\",\n            \"https://en.wiktionary.org/wiki/%D9%87%D9%86%DA%AF%D8%A7%D9%85\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"BQT\",\n              \"status\": \"partial\",\n              \"note\": \"The volume-less citation 'BQT' points to the same stretch as the parent node: BQT_v1_pages.txt leaf 388 (p. 170, اندرز), leaf 389 (p. 171, اندودن / اندوه / اندوختن), leaf 394 (p. 176, هنگام). The entries exist and the glosses match Nourai's ('اندوه ... گرفتگی دل و دلگیری'), but Borhan is a definition dictionary and Mo'in's etymological footnotes on these pages are illegible in the OCR.\"\n            },\n            {\n              \"ref\": \"MON\",\n              \"status\": \"not_checked\",\n              \"note\": \"No page number is given, and the six-volume Farhang-e Farsi is not online at all (refs_online.json, MON: 'still no scan of the 6-vol Amir Kabir edition ... Only the 2-vol Adena condensation exists'); the condensation (MON_part1/part2) has no separate اندوه etymology.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 41\",\n              \"stance\": \"supports\",\n              \"note\": \"'handūdan, *handāy- ... smear, plaster, anoint'; 'handarz ... advice, injunction, testament'; 'hangām ... time, occasion' — with the New Persian outcomes an~ / andarz / hangām printed in the entries themselves.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien §107\",\n              \"stance\": \"supports\",\n              \"note\": \"'ap. ham- = np. an- als 1. Glied von Kompositis vor folgendem g, j, d, b ... Doch erscheint h noch in hanjar, hinjar ‚Weg‘ und hangām, hingām ‚Zeit‘' — explains both the an- of andūdan/andarz and the surviving h- of hangām.\"\n            },\n            {\n              \"src\": \"CHEUNG\",\n              \"where\": \"Cheung 2007 s.v. *θuaxš, p. 400\",\n              \"stance\": \"contradicts\",\n              \"note\": \"'(+ *ham-) BMP ʾndwh /andōh/ “sorrow” ... NP tuxšidan “to strive”, taxša “diligent” || (+ *ham-) NP andoh “anxious”' — a different etymon for اندوه from the one drawn.\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Old Persian\",\n          \"words\": \"ha 1; ha-dâ; ham; ham-karta\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Every item is in Kent's Old Persian lexicon on the two pages Nourai cites. p. 211: 'ha- insep. prefix, anteconsonantal: Av. ha-, Skt. sa-, Gk. ἁ-, Lt. sem-, pIE *sm̥-, zero-grade of pIE *sem- \\\"one\\\", Gk. εἷς ἕν; in hakara-, hadā' — i.e. exactly Nourai's 'ha 1: one, with'. p. 212: 'hadā prep. with instr. \\\"with\\\": GAv. hadā, LAv. haδa, Skt. sahá, pIE *sm̥-dhe; Ar. *sa- (see OP ha-) + adv. suffix -dhe as in idā' (Kent restates it in §67: '*sm̥-dhe, OP hadā, Skt. sahá \\\"with\\\"'). p. 212 also: 'haᵐkarta- ptc. adj., nt. as sb., \\\"cooperation\\\": ham- + karta- \\\"done\\\", past ptc. pass. to kar-' — Nourai's 'ham-karta: cooperation' with its cross-reference to Kwer (PIE *kʷer- 'to make') verbatim, attested at DNb 16f. p. 213 completes the set: 'ham- insep. prefix, \\\"together, with\\\", like Lt. com-: Av. ham-, Skt. sam-; ... in Ha-gmatāna-, ha-dugā-, ham-arana-, ha-miçiya-' and 'hama- adj. \\\"one and the same\\\": Av. hama-, ... deriv. of pIE *sem- \\\"one\\\", cf. ha- and ham-.'\",\n          \"derivation_fa\": \"هر چهار مدخل این جعبه دقیقاً در همان دو صفحه‌ای است که نورایی ارجاع داده است. کنت در ص ۲۱۱ می‌نویسد: «ha- پیشوند جدانشدنی ... اوستایی ha-، سنسکریت sa-، یونانی ἁ-، لاتین sem-، هندواروپایی *sm̥-، ستاک صفرِ *sem- “یک”؛ در hakara- و hadā». در ص ۲۱۲: «hadā حرف اضافه با ابزاری، “با”: گاهانی hadā، اوستایی متأخر haδa، سنسکریت sahá، هندواروپایی *sm̥-dhe؛ ایرانی *sa- به‌علاوهٔ پسوند قیدی -dhe». و در همان صفحه: «haᵐkarta- صفت مفعولی، به‌عنوان اسم خنثی، “همکاری”: ham- + karta- “کرده”، اسم مفعول از kar-» که در کتیبهٔ DNb سطر ۱۶ آمده است — یعنی همان «ham-karta» با ارجاع به ریشهٔ Kwer. ص ۲۱۳ نیز ham- و hama- را جداگانه از *sem- می‌گیرد. ادعای نورایی به‌تمامی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"KNT:211\",\n              \"status\": \"supports\",\n              \"note\": \"Kent, Old Persian (1953), Lexicon p. 211: 'ha- insep. prefix (§204.I), anteconsonantal (§132.I): Av. ha-, Skt. sa-, Gk. ἁ-, Lt. sem-, pIE *sm̥-, zero-grade of pIE *sem- “one”, Gk. εἷς ἕν; in hakara-, hadā. See also ham-, hama-.' (The local KNT.txt is an incomplete OCR that omits the H- section of the lexicon; read from the fuller OCR of archive.org/details/oldpers, where the running head 'LEXICON 211' precedes this entry.)\"\n            },\n            {\n              \"ref\": \"KNT:212\",\n              \"status\": \"supports\",\n              \"note\": \"Kent p. 212: 'hakaram adv. “once”: Av. hakarət, Skt. sakŕ̥t, cf. Gk. ἅπαξ, Lit. sem-el; ha- (q.v.) + *kr̥t “time”'; 'haᵐkarta- (§140.V) ptc. adj., nt. as sb., “cooperation”: ham- + karta- “done”, past ptc. pass. to kar-. [ha]kartahyā gsn. DNb 16f'; 'hadā prep. with instr. “with”: GAv. hadā, LAv. haδa, Skt. sahá, pIE *sm̥-dhe'; 'Haᵑgmatāna- sb. “Ecbatana” ... deriv. of ha-gmata- ...: “City of Gatherings”'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 903 (POK_03.txt leaf 138)\",\n              \"stance\": \"supports\",\n              \"note\": \"'3. ‚*in eins = zusammen, mit‘; sm̥-: ai. sa-há, sadha- ‚gemeinsam, zusammen‘ = av. haδa, ap. hadā ‚zusammen‘ ... som-: ai. sám- ‚zusammen, zugleich mit‘, av. ap. ha(m)- ‚mit‘.' Pokorny cites the very Old Persian forms of this box.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, sem-1 IV\",\n              \"stance\": \"supports\",\n              \"note\": \"'IV. Zero-grade form *sm̥-. 1. Greek ha-, a-, together ... 9. Extended form *sm̥ma in Greek hama, together with, at the same time' — the same zero grade Kent posits for OP ha-/hadā.\"\n            },\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae, AiW s.v. haδa / hakərət\",\n              \"stance\": \"supports\",\n              \"note\": \"BRT.txt has the Avestan counterparts (haδa 'zusammen', hakərət 'einmal', han-kərətay- 'Vollziehung, Vollendung' at col. 1770) that Kent compares with OP hadā, hakaram and haᵐkarta-.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Greek\",\n          \"words\": \"homos, homalos; sun; sun-phonos; sun-ballein; sun-posion\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The node splits cleanly in two. (a) ὁμός 'same, common, joint' and ὁμαλός 'level, even, like' are securely from this root: Wiktionary derives ὁμός from Proto-Hellenic *homós < PIE *somHós 'same, alike' (cognate εἷς, OE sama, Skt. sama-, OP hama-), Pokorny p. 904 lists 'gr. ὁμός \\\"gemeinsam; ähnlich, gleich\\\"', and Mann col. 1245-1246 has 'somolos ... Gk. homalós \\\"level, even\\\"' and 'somos ... Gk. homós'. (b) σύν 'with, together with' and the compounds σύμφωνος, συμβάλλειν, συμπόσιον built on it are NOT accepted as belonging here. Pokorny himself, on the very page Nourai cites (904), writes: 'falls lit. sù \\\"mit\\\" dazugehört, könnte es samt aksl. sǫ und gr. ξύν, σύν \\\"mit\\\" auf idg. *ksu bzw. *ksun zurückgeführt werden'; Watkins consequently gives a separate root entry 'ksun. Preposition and preverb meaning \\\"with.\\\" 1. Greek sun, xun, together, with: SYN-. ... [In Pok. 2. sem- 902.]'; Klein (the very page Nourai cites, p. 1557) says 'syn-, pref. ... — Gk. σύν, ξύν \\\"with, together with\\\"; of uncertain origin'; Wiktionary notes that Homeric/Old Attic ξῠ́ν and Mycenaean ku-su point to Proto-Hellenic *ksún, 'further origin uncertain'; Etymonline gives PIE *ksun-. So four of the five entries in this box hang on a derivation that modern scholarship rejects.\",\n          \"derivation_fa\": \"این جعبه دو بخش ناهمگون دارد. الف) ὁμός «یکسان، مشترک» و ὁμαλός «هموار، همانند» به‌یقین از همین ریشه‌اند: ویکی‌واژه ὁμός را از یونانی آغازین *homós و آن را از هندواروپایی *somHós می‌گیرد (هم‌ریشه با εἷς، sama سنسکریت و hama پارسی باستان)؛ پوکورنی نیز در ص ۹۰۴ «gr. ὁμός» را زیر همین ریشه آورده و مان در ستون‌های ۱۲۴۵–۱۲۴۶ صورت‌های somolos و somos را با همین واژه‌های یونانی ثبت کرده است. ب) اما σύν «با، همراه» و ترکیب‌های آن (σύμφωνος، συμβάλλειν، συμπόσιον) امروزه از این ریشه جدا شمرده می‌شوند. خودِ پوکورنی در همان ص ۹۰۴ می‌نویسد که σύν و ξύν را می‌توان به *ksu/*ksun بازگرداند؛ واتکینز مدخل جداگانه‌ای به نام ksun ساخته است؛ کلاین در همان ص ۱۵۵۷ که نورایی ارجاع می‌دهد می‌گوید «σύν، ξύν: خاستگاهش نامعلوم است»؛ و ویکی‌واژه با استناد به ξῠ́ν هومری و ku-su میسِنی صورت یونانی آغازین *ksún را بازسازی می‌کند. پس چهار مدخل از پنج مدخل این جعبه را پژوهش امروزی رد می‌کند.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%E1%BD%81%CE%BC%CF%8C%CF%82\",\n            \"https://en.wiktionary.org/wiki/%CF%83%CF%8D%CE%BD\",\n            \"https://www.etymonline.com/word/syn-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"contradicts\",\n              \"note\": \"Watkins 1985 keeps two entries: 'sem-1 ... II.2.b. Greek homos, same: HOMEO-, HOMO-; ANOMALOUS; c. Greek homilos, crowd: HOMILY. 3. Suffixed form *som-alo- in Greek homalos, like, even, level' — supports the first line of the box; but 'ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: SYN-. 2. Russian so-, s-, with, in sputnik ... [In Pok. 2. sem- 902.]' — a separate root for the rest of the box.\"\n            },\n            {\n              \"ref\": \"KLN:1557\",\n              \"status\": \"contradicts\",\n              \"note\": \"Klein 1966, p. 1557 (the syn- column, between 'symptomatology' and 'synaeresis'): 'syn-, pref. meaning “with, together with”. — Gk. σύν, ξύν “with, together with” (whence σύνδε, “commun”); of uncertain origin. Cp. sy-, syl-, sym-, sys-.' The page number is exact; the content refuses the derivation.\"\n            },\n            {\n              \"ref\": \"IEC:1246\",\n              \"status\": \"supports\",\n              \"note\": \"Mann, An Indo-European Comparative Dictionary, col. 1246 (IEC.txt leaf 687): 'somos “together, like, equal, one, some, the same”. WP II, 490. Cf. som-, sem- and sm- | Skt. samáh ... Av. hamō ... Gk. homós, adj. “like, equal”; homo-, cpds.'; col. 1245: 'somolos “together, equal, even, like” ... Gk. homalós, adj. “level, even”; Umb. sumel, adv. “at the same time”.' Supports the ὁμός/ὁμαλός half only.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 904 (POK_03.txt leaf 141)\",\n              \"stance\": \"partial\",\n              \"note\": \"'mit aksl. sǫ- ablautend ist *sęn-, sę (*som) ... falls lit. sù ‚mit‘ dazugehört, könnte es samt aksl. sę und gr. ξύν, σύν ‚mit‘ auf idg. *ksu bzw. *ksun zurückgeführt werden; vgl. Schwyzer Gr. Gr. 2, 487.' Pokorny lists σύν under sem- but already treats *ksun as the likelier source.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 490-491\",\n              \"stance\": \"supports\",\n              \"note\": \"The *somo-s section cites 'gr. ὁμός ... ὁμογνιος, ai. sama-jātīya ‚gleichartig‘, anord. samfeðra, ὁμοπάτωρ, ap. hamapitar-' — supports the ὁμός line of the box.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Simple\",\n              \"stance\": \"silent\",\n              \"note\": \"Skeat treats sim- (same, semel, simul, singuli) but has no bearing on σύν.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"French\",\n          \"words\": \"homogene; symphonie; symbole; symposium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The four French words do go back to the Greek forms in the parent box, but not one of them reached French directly from Greek: homogène (1503) is from Medieval Latin homogeneus < Gk. ὁμογενής (ὁμο- 'same' + γένος 'kind'); symphonie (12th c.) from Latin symphonia < Gk. συμφωνία; symbole (14th c.) from Late Latin symbolum < Gk. σύμβολον; and symposium is not an inherited French word at all but a 19th-century learned borrowing of Latin symposium < Gk. συμπόσιον, used in French with its Latin spelling (whence its identical shape here). The arrow is thus right in substance but skips the Latin stage that Nourai himself draws separately in the Latin box below.\",\n          \"derivation_fa\": \"هر چهار واژهٔ فرانسوی سرانجام به همان صورت‌های یونانی جعبهٔ بالا می‌رسند، اما هیچ‌یک بی‌واسطه از یونانی به فرانسه نرفته‌اند: homogène (۱۵۰۳) از لاتین میانهٔ homogeneus و آن از ὁμογενής یونانی؛ symphonie (سدهٔ دوازدهم) از symphonia لاتین و آن از συμφωνία؛ symbole (سدهٔ چهاردهم) از symbolum لاتین متأخر و آن از σύμβολον؛ و symposium اصلاً واژهٔ موروثی فرانسوی نیست، بلکه وام‌واژه‌ای عالمانه از لاتین symposium (< συμπόσιον) در سدهٔ نوزدهم است که املای لاتین خود را نگاه داشته است. پس پیکان از نظر ماده درست است ولی مرحلهٔ لاتین را — که خودِ نورایی در جعبهٔ پایین‌تر جداگانه کشیده — نادیده می‌گیرد: با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symbol\",\n            \"https://www.etymonline.com/word/syn-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.vv. symbol, symposium, homo-\",\n              \"stance\": \"supports\",\n              \"note\": \"s.v. homo-: 'Gk. ὁμο-, ὁμ-, fr. ὁμός (for *somos), “one and the same, belonging to two or more jointly”, rel. to ὁμοῦ “together”, and cogn. with OI. samáh, L. similis, Goth. sama.' Klein routes symbol/symposium through Latin (symbolum, symposium) into the modern languages.\"\n            },\n            {\n              \"src\": \"FSD\",\n              \"where\": \"Funk & Wagnalls, s.v. symphony/symposium\",\n              \"stance\": \"silent\",\n              \"note\": \"Consulted for a French-mediation statement; F&W treats these as Latin-Greek learned words and says nothing specific about French transmission.\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"Persian\",\n          \"words\": \"homožen «هموژن»; samfonî «سمفونی»; sambol «سمبول»; sampozîyom «سمپوزیوم»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"These are 20th-century French loans into Persian, and the Persian shapes betray French rather than English or Latin phonology: هموژن homožen renders French homogène with the French voiced fricative [ʒ] written ژ (an English loan would have given *homojinos/هموجنس); سمفونی samfonī renders symphonie with French final -ie > -ī and French initial [s] for sy-; سمبول sambol renders symbole with the French rounded final -ole (English 'symbol' would give سمبل); سمپوزیوم/سمپوزیم sampozīyom renders the French learned form symposium read in French fashion, [sɛ̃pozjɔm]. The route is the standard one for Iranian technical and musical vocabulary after the Dar al-Funun (1851) and the French-language schooling of the late Qajar and early Pahlavi period. Note on the script: the printed page (see data/verification/sources/refs/ocr/BOOK/442.png) appears to set the last word as «سمپوزیم» without the second و; the JSON gives the now-standard spelling «سمپوزیوم».\",\n          \"derivation_fa\": \"این چهار واژه وام‌واژه‌های سدهٔ بیستمی فارسی از فرانسه‌اند و صورت آوایی فارسی آن‌ها آشکارا فرانسوی است نه انگلیسی یا لاتین: «هموژن» برگردان homogène فرانسوی است با همان سایشی واکدار [ʒ] که در فارسی «ژ» نوشته می‌شود (اگر از انگلیسی می‌آمد «هموجنوس» می‌شد)؛ «سمفونی» برگردان symphonie با «ـی» پایانی فرانسوی؛ «سمبول» برگردان symbole با مصوت گرد پایانی فرانسوی (از انگلیسی «سمبل» می‌شد)؛ و «سمپوزیوم» خوانش فرانسویِ symposium. راه این وام‌گیری همان راه همیشگی واژگان فنی و موسیقایی ایران پس از تأسیس دارالفنون (۱۲۳۰ش/۱۸۵۱م) و رواج آموزش فرانسوی در اواخر قاجار و اوایل پهلوی است. ادعای نورایی درست است. یادداشت خوانشی: در صفحهٔ چاپی، واژهٔ آخر ظاهراً «سمپوزیم» (بدون واو دوم) حروف‌چینی شده و در فایل استخراجی صورت امروزی «سمپوزیوم» آمده است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1921\",\n              \"status\": \"not_checked\",\n              \"note\": \"Mo'in's six-volume Farhang-e Farsi is not available online in any form (refs_online.json, MON: 'no scan of the 6-vol Amir Kabir edition ... on archive.org, Google Books, HathiTrust, noorlib, ketabnak'), and the 2-volume Adena condensation on disk (MON_part1/part2) has no entry for سمفونی or هموژن; page numbers cannot be mapped to the online (vajehyab/abadis) text.\"\n            },\n            {\n              \"ref\": \"VOP:372\",\n              \"status\": \"not_checked\",\n              \"note\": \"Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371) — refs_online.json records 'RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Purchase second-hand only.' This is, however, exactly the right kind of reference for this node (a dictionary of European loanwords in Persian).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt / MON_part2.txt (2-vol Adena condensation)\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for سمفونی, سمبول, هموژن and سمپوزیوم in both OCR files returns nothing — the condensation drops the European-loanword volume.\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. homo-\",\n              \"stance\": \"supports\",\n              \"note\": \"Gives the Greek base ὁμός behind French homogène and hence Persian هموژن; the French intermediary is what the Persian ژ proves.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"English\",\n          \"words\": \"symphony\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English symphony came in twice along the route the chart draws. Middle English symphonie (c. 1300, 'harmony of sound') is from Old French symphonie, from Latin symphonia, from Greek συμφωνία 'concord of sound', from σύμφωνος 'harmonious' (σύν + φωνή 'voice, sound' — Nourai's cross-reference Bhâ 2 = PIE *bʰeh₂- 'to speak'). The modern musical sense, 'an extended orchestral composition', is a 17th-18th-century re-borrowing under the influence of Italian sinfonia. The French -> English arrow is therefore right; the only caveat is the one inherited from the Greek box: the σύν element is now referred to PIE *ksun, not *sem-.\",\n          \"derivation_fa\": \"واژهٔ انگلیسی symphony دو بار و از همان راهی که نورایی کشیده وارد شده است: صورت انگلیسی میانهٔ symphonie (حدود ۱۳۰۰ م، به معنی «هماهنگی آوا») از فرانسهٔ کهن symphonie، از symphonia لاتین، از συμφωνία یونانی «هم‌آوایی» که خود از σύμφωνος (σύν + φωνή «آوا») ساخته شده است — همان ارجاع نورایی به ریشهٔ Bhâ 2. معنای موسیقایی امروزین («سمفونی» به‌عنوان قطعهٔ ارکستری) وام‌گیری دوبارهٔ سده‌های هفدهم و هجدهم زیر تأثیر sinfonia ایتالیایی است. پس پیکان «فرانسه ← انگلیسی» درست است؛ تنها اشکال همان اشکال جعبهٔ یونانی است که جزء σύν را امروزه به *ksun بازمی‌گردانند نه به *sem-.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/syn-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 index (AHD_watkins1985.txt line 2331): 'SYMPHONY bha-2 ... SYN- ksun' — Watkins analyses symphony exactly as σύν + *bʰā- 'to speak', which is Nourai's cross-reference, but files the syn- element under ksun.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. syn- and concent\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's syn- article ('Gk. σύν, ξύν “with, together with”; of uncertain origin. Cp. sy-, syl-, sym-, sys-') covers the sym- of symphony; his entry 'concent, n., harmony (obsol.) — L. concentus, “symphony, harmony”' shows Latin con- as the calque of Greek syn-.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Symphony\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat routes the word F. symphonie < L. symphonia < Gk. συμφωνία < σύν + φωνή, the same chain.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An unlabelled pass-through box: Latin is the vehicle by which the Greek forms of node 6 reached English. The relevant Latin items are the straight Hellenisms symbolum 'token, creed' (< σύμβολον), symposium 'drinking party' (< συμπόσιον) and Medieval Latin homogeneus (< ὁμογενής); all three keep the Greek shape with the regular Latin substitutions y for υ and -um for -ον. Latin borrowed them, it did not inherit them, so no sound change from PIE *sem- is involved on this leg.\",\n          \"derivation_fa\": \"این جعبهٔ بی‌واژه فقط نقش گذرگاه دارد: لاتین حاملی است که صورت‌های یونانی جعبهٔ ۶ را به انگلیسی رسانده است. واژه‌های مربوط عبارت‌اند از symbolum «نشانه، اقرارنامه» (از σύμβολον)، symposium «بزم» (از συμπόσιον) و homogeneus لاتین میانه (از ὁμογενής)؛ هر سه صورت یونانی را با جایگزینی‌های قاعده‌مند لاتین (y به‌جای υ و -um به‌جای -ον) نگاه داشته‌اند. لاتین این‌ها را وام گرفته و به ارث نبرده است، پس در این حلقه هیچ دگرگونی آوایی از *sem- هندواروپایی در کار نیست. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symbol\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.vv. symbol, symposium\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein derives symbol from Late Latin symbolum < Gk. σύμβολον and symposium from Latin symposium < Gk. συμπόσιον; his 'potion' article lists symposium among the derivatives of Gk. πότον 'a drink'.\"\n            },\n            {\n              \"src\": \"LEW\",\n              \"where\": \"Walde, Lateinisches etymologisches Wörterbuch (LEW_1910.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Walde treats only inherited Latin vocabulary; symbolum/symposium are entered, if at all, as Greek loans without IE discussion.\"\n            }\n          ]\n        },\n        {\n          \"id\": 11,\n          \"lang\": \"English\",\n          \"words\": \"homogenous, symbol, symposium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Three learned Latin-mediated borrowings. homogenous (the book's spelling; the general-purpose adjective is homogeneous, 1640s, from Medieval Latin homogeneus < Gk. ὁμογενής 'of the same kind' = ὁμο- + γένος; 'homogenous' proper is a 19th-century biological term 'similar through common descent') — its first element ὁμο- is the only member of this box that is securely from PIE *sem-. symbol (mid-15c. 'creed, formal summary of religious belief', from Late Latin symbolum < Gk. σύμβολον 'token, sign', etymologically 'that which is thrown together', from σύν + βάλλειν 'to throw' — Nourai's cross-reference Gwel 1 = PIE *gʷelh₁- 'to throw, reach'). symposium (1711, from Latin symposium < Gk. συμπόσιον 'drinking party', from σύν + πόσις 'drinking' — his cross-reference Pô 2 = PIE *peh₃(i)- 'to drink'); the sense 'conference, collection of essays' is from 1784 after Plato's dialogue. The Latin -> English arrow and both compound analyses are correct; the σύν element again belongs to *ksun rather than *sem-.\",\n          \"derivation_fa\": \"هر سه وام‌واژهٔ عالمانه و از راه لاتین‌اند. homogenous (املای کتاب؛ صفت عمومی انگلیسی homogeneous است، از ۱۶۴۰م، از لاتین میانهٔ homogeneus و آن از ὁμογενής یونانی «هم‌گونه» = ὁμο- + γένος؛ خودِ homogenous اصطلاحی زیست‌شناختی از سدهٔ نوزدهم است) — جزء نخست آن، یعنی ὁμο-، تنها عضو این جعبه است که به‌یقین از *sem- می‌آید. symbol (نیمهٔ سدهٔ پانزدهم، نخست به معنی «اقرارنامهٔ ایمان»، از symbolum لاتین متأخر و آن از σύμβολον یونانی «نشانه»، تحت‌اللفظ «آنچه به هم افکنده شود»، از σύν + βάλλειν «افکندن» — همان ارجاع نورایی به Gwel 1). symposium (۱۷۱۱م، از symposium لاتین و آن از συμπόσιον «بزم می‌گساری»، از σύν + πόσις «نوشیدن» — ارجاع نورایی به Pô 2)؛ معنای «همایش» از ۱۷۸۴م و به تقلید از رسالهٔ افلاطون است. پیکان «لاتین ← انگلیسی» و تجزیهٔ هر دو ترکیب درست است؛ تنها جزء σύν است که به *ksun تعلق دارد نه به *sem-.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symbol\",\n            \"https://www.etymonline.com/word/syn-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.vv. symbol, potion (cross-reference list), homo-\",\n              \"stance\": \"supports\",\n              \"note\": \"Klein's ballistics/ball article ends the derivative list '... parole, periblem, problem, scybalum, symbol, Tribolium' under Gk. βάλλειν, and his 'potion' article lists '... pour-boire, propine, symposium' under Gk. πότον — exactly Nourai's cross-references Gwel 1 and Pô 2.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 index\",\n              \"stance\": \"supports\",\n              \"note\": \"'SYMBOL gʷele-1 ... SYMPOSIUM pō(i)- ... SYN- ksun' and, under sem-1, 'HOMO- sem-1, HOMOLOGRAPHIC sem-1' — Watkins splits the compounds exactly as described here.\"\n            }\n          ]\n        },\n        {\n          \"id\": 12,\n          \"lang\": \"Russian\",\n          \"words\": \"samo-war, samo-vari, samo-varitî\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Russian самовар samovar 'samovar' is transparently само- samo- 'self' + варить varítʹ 'to boil, cook', i.e. literally 'self-boiler', which is Nourai's gloss; the second element is his cross-reference Wer 5 (PIE *wer- 'to burn', via Old Church Slavonic variti 'to cook'). The first element сам/само- continues PIE *somH-o- 'same, self' — Watkins, sem-1 III.2: 'Suffixed lengthened o-grade form *sōm-o- in Russian sam, samo-, self: SAMIZDAT, SAMOVAR.' Two caveats. (a) The chart's word-list is a segmentation, not three Russian lemmas: only самовар is a word; варить/варит is the verb and 'samo-vari' is not Russian at all. (b) Etymonline records the standing doubt: 'but this is perhaps folk-etymology if the word is from Tatar sanabar \\\"tea-urn\\\"' — i.e. the compound may be a Russian re-analysis of a Turkic term, in which case the *sem- connection is secondary.\",\n          \"derivation_fa\": \"واژهٔ روسی самовар (samovar) آشکارا از само- «خود» و варить «جوشاندن، پختن» ساخته شده است، یعنی تحت‌اللفظ «خودجوش» — همان معنایی که نورایی آورده؛ جزء دوم همان ارجاع او به ریشهٔ Wer 5 (هندواروپایی *wer- «سوختن»، از راه variti اسلاوی کلیسایی کهن) است. جزء نخست، сам/само-، بازماندهٔ *somH-o- «همان، خود» است؛ واتکینز در بند III.2 مدخل sem-1 می‌نویسد: «صورت o-ی کشیدهٔ پسوندی *sōm-o- در روسی sam، samo- “خود”: SAMIZDAT، SAMOVAR». دو نکته: (الف) فهرست واژه‌های این جعبه تجزیه است نه سه واژهٔ روسی؛ تنها самовар واژه است و «samo-vari» اصلاً صورت روسی نیست. (ب) اتیمآنلاین تردید رایج را ثبت کرده است: «شاید این ریشه‌شناسی عامیانه باشد اگر واژه از sanabar تاتاری “سماور” آمده باشد» — یعنی ممکن است ترکیب روسی بازتحلیل واژه‌ای ترکی باشد. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/samovar\",\n            \"https://en.wiktionary.org/wiki/samovar\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD:1148\",\n              \"status\": \"supports\",\n              \"note\": \"Nourai's page number is from the 1975/76 New College dictionary, whose main-entry 'samovar' (c. p. 1148) carries the root reference. The corresponding root entry, Watkins 1985 s.v. sem-1: 'III.2. Suffixed lengthened o-grade form *sōm-o- in Russian sam, samo-, self: SAMIZDAT, SAMOVAR.' The index likewise gives 'SAMOVAR sem-1, wer-7', matching both of Nourai's cross-references.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 904-905\",\n              \"stance\": \"supports\",\n              \"note\": \"'aksl. samъ ‚ipse, solus, unus‘' is listed with *somo-s; this is the direct antecedent of Russian сам.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs\",\n              \"stance\": \"silent\",\n              \"note\": \"grep of LKT.txt for samowar/samovar returns nothing — Lokotsch does not treat the word as an orientalism, which is a small argument against the Tatar sanabar hypothesis.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, cols. 1245-1246 (somn-, somos)\",\n              \"stance\": \"supports\",\n              \"note\": \"'somos “together, like, equal, one, some, the same” ... Hitt. cf. sanas “one”; Gk. homós' — Mann's Slavic material under som-/somos underwrites Russian сам.\"\n            }\n          ]\n        },\n        {\n          \"id\": 13,\n          \"lang\": \"Persian\",\n          \"words\": \"samâvar «ساموار»\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The derivation itself is certain: Persian سماور samāvar is a direct loan from Russian самовар, taken over during the 19th century along with the object itself through Russo-Iranian trade across the Caucasus and the Caspian (whence also Ottoman Turkish semaver and Northern Luri səmüər); Dehkhoda marks the headword '(روسی، اِ)' and abadis glosses it 'سماور واژه‌ای روسی самовар به معنای خودجوش'. Wiktionary gives 'سماور (samâvar): From Russian самова́р, literally “self-boiler”'. The problem is the script field: the JSON prints «ساموار» (s-ā-m-ū-ā-r), which is not a Persian word and is not what the book prints. The page itself (rendered at 1200 dpi, saved as data/verification/sources/refs/ocr/BOOK/442.png) clearly sets «سماور» — sīn, mīm, alef, wāw, rā — against the transliteration 'samâvar'. This is an extraction error, not a mistake of Nourai's.\",\n          \"derivation_fa\": \"خود ریشه‌شناسی قطعی است: «سماور» فارسی وام مستقیم از самовар روسی است که در سدهٔ نوزدهم همراه با خودِ آن ابزار و از راه بازرگانی ایران و روسیه در قفقاز و کرانهٔ خزر به فارسی آمد (و از همان راه semaver ترکی عثمانی و səmüər لری شمالی)؛ دهخدا سرواژه را «(روسی، اِ)» نشانه‌گذاری کرده و آبادیس آن را «واژه‌ای روسی самовар به معنای خودجوش» می‌خواند، و ویکی‌واژه نیز همین را می‌گوید. اشکال در میدان خط فارسیِ فایل استخراجی است: در آنجا «ساموار» آمده که اصلاً واژهٔ فارسی نیست و آنچه کتاب چاپ کرده نیز نیست. تصویر صفحه با تفکیک ۱۲۰۰ نقطه بر اینچ (ذخیره‌شده در data/verification/sources/refs/ocr/BOOK/442.png) به‌روشنی «سماور» (س‌م‌ا‌و‌ر) را در برابر آوانگاری samâvar نشان می‌دهد. پس این خطای خوانش اسکن است، نه خطای نورایی.\",\n          \"error_in\": \"extraction\",\n          \"book_prints\": \"سماور\",\n          \"correct_form\": \"سماور\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D8%B3%D9%85%D8%A7%D9%88%D8%B1\",\n            \"https://abadis.ir/fatofa/%D8%B3%D9%85%D8%A7%D9%88%D8%B1/\",\n            \"https://www.etymonline.com/word/samovar\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:1918\",\n              \"status\": \"not_checked\",\n              \"note\": \"The six-volume Mo'in is not online and its page numbers cannot be mapped (refs_online.json, MON). The nearest accessible substitute, Dehkhoda via abadis.ir, gives 'سماور. [س َ وَ] (روسی، اِ) یک قسم ابزاری فلزی جهت جوش آوردن آب که آتش‌خانه را در میانش قرار داده‌اند' — the same Russian origin Nourai claims, and with the spelling سماور.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"MON_part1.txt / MON_part2.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"grep for سماور in the 2-volume Adena condensation returns nothing.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"incoming/ARY/ARY_pages.txt\",\n              \"stance\": \"silent\",\n              \"note\": \"Aryanpur's dictionary of Indo-European roots in Persian has no سماور entry (grep returns only unrelated هنگام hits) — expected, since it is a modern Russian loan, not an inherited word.\"\n            },\n            {\n              \"src\": \"LKT\",\n              \"where\": \"Lokotsch\",\n              \"stance\": \"silent\",\n              \"note\": \"No samovar entry; Lokotsch covers European words of oriental origin, not Persian words of European origin.\"\n            }\n          ]\n        },\n        {\n          \"id\": 14,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An unlabelled pass-through box for the Germanic branch. Three distinct Proto-Germanic formations descend from PIE *sem- and feed the English box below: *samaz 'same' (< *som-o-), *sumaz 'some, a certain one' (< zero grade *sm̥-o-) and *sōmiz 'fitting, seemly' (< lengthened grade *sēm-i-). Watkins sets them out under sem-1 II.2.a, IV.3 and III.1 respectively; Pokorny 904-905 gives the same three: 'got. sama ‚derselbe‘, aisl. samr', 'got. sums ‚irgend ein, ein gewisser‘, as. ags. ahd. sum', and 'aisl. sóma (*sōmen) ‚passen, geziemen‘, sómi m. ‚Ehre‘ ... engl. seem ‚ziemen, scheinen‘ ist nord. Lw.'\",\n          \"derivation_fa\": \"این جعبهٔ بی‌واژه فقط شاخهٔ ژرمنی را نشان می‌دهد. سه ساخت جداگانهٔ ژرمنی آغازین از *sem- هندواروپایی برآمده و جعبهٔ انگلیسی پایین را تغذیه می‌کنند: *samaz «همان» (از *som-o-)، *sumaz «برخی، یکی» (از ستاک صفر *sm̥-o-) و *sōmiz «شایسته، درخور» (از ستاک کشیدهٔ *sēm-i-). واتکینز آن‌ها را به‌ترتیب در بندهای II.2.a و IV.3 و III.1 مدخل sem-1 آورده و پوکورنی نیز در صص ۹۰۴–۹۰۵ همین سه را ثبت کرده است: «got. sama ‚همان‘»، «got. sums ‚برخی‘» و «aisl. sóma ‚درخور بودن‘ ... engl. seem وام‌واژهٔ نُرسی است». ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/same\",\n            \"https://www.etymonline.com/word/seem\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. sem-1: 'II.2.a. Germanic *samaz, same, in Old Norse samr, same: SAME'; 'III.1. Suffixed form *sēm-i- in Germanic *sōmiz in Old Norse sœmr, fitting, agreeable (< “making one,” “reconciling”): SEEM, SEEMLY'; 'IV.3. Suffixed form *sm̥-o- in Germanic *sumaz in: a. Old English sum, one, a certain one: SOME; b. Old English -sum, like: -SOME1.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 904-905\",\n              \"stance\": \"supports\",\n              \"note\": \"'got. sama ‚derselbe‘, aisl. samr, inn sami ‚derselbe‘ ... ahd. der samo'; 'got. sums ‚irgend ein, ein gewisser‘, Pl. ‚einige, manche‘, aisl. sumr'; 'aisl. sóma (*sōmen) ‚passen, geziemen‘, sómi m. ‚Ehre, Auszeichnung‘ ... engl. seem ‚ziemen, scheinen‘ ist nord. Lw.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 490-491\",\n              \"stance\": \"supports\",\n              \"note\": \"Same Germanic material in the older presentation of the *somo-s section (got. sama, samana, anord. samfeðra).\"\n            },\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. same\",\n              \"stance\": \"supports\",\n              \"note\": \"'same, adj., pron. and adv. — ME., fr. ON. samr, “the same”, rel. to OE. same ... Goth. sama, adj., OHG. samant, MHG. sament, samt “together” ... fr. I.-E. base *sem-, *sm̥-, “one, ...”'\"\n            }\n          ]\n        },\n        {\n          \"id\": 15,\n          \"lang\": \"English\",\n          \"words\": \"same, some, seem\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"same: Old English lost the adjective (it survives only in the adverbial phrase swā same 'in like manner'), so Middle English same is generally taken from Old Norse samr, samr < Proto-Germanic *samaz < *som-o-; it displaced the native ilk in the 12th-13th centuries. some: Old English sum 'a certain one' < Proto-Germanic *sumaz < the zero grade *sm̥-o-, with the regular Germanic development of syllabic *m̥ to um; the suffix -some1 is the same word. seem: c. 1200, a Norse loan like same, from Old Norse sœma 'to conform to, honour', a denominative to sœmr 'fitting' < Proto-Germanic *sōmiz < *sēm-i-, literally 'making one, reconciling' — the semantic path 'to be fitting' > 'to appear to be' is English. All three are what Watkins lists under sem-1 and Etymonline under *sem- (1).\",\n          \"derivation_fa\": \"same: انگلیسی کهن این صفت را از دست داده بود (جز در ترکیب قیدی swā same «همان‌گونه»)، از این‌رو صورت انگلیسی میانهٔ same را وام‌واژهٔ نُرسی کهن samr می‌دانند، از ژرمنی آغازین *samaz و آن از *som-o-؛ این واژه در سده‌های دوازدهم و سیزدهم جای ilk بومی را گرفت. some: از انگلیسی کهن sum «یکی، کسی» از ژرمنی آغازین *sumaz و آن از ستاک صفر *sm̥-o- با تحول قاعده‌مند *m̥ هجایی به um در ژرمنی؛ پسوند -some نیز همین واژه است. seem: از حدود ۱۲۰۰م و مانند same وام نُرسی است، از sœma نُرسی کهن «درخور بودن، گرامی داشتن»، برساخته از sœmr «شایسته» از ژرمنی آغازین *sōmiz و آن از *sēm-i- به معنی تحت‌اللفظی «یکی کردن، آشتی دادن»؛ تحول معنایی «درخور بودن ← به‌نظر رسیدن» ویژهٔ انگلیسی است. هر سه دقیقاً همان‌هایی‌اند که واتکینز زیر sem-1 و اتیمآنلاین زیر *sem- (1) آورده‌اند: ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/same\",\n            \"https://www.etymonline.com/word/seem\",\n            \"https://www.etymonline.com/word/samovar\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"Nourai gives no reference for this node; the parent Germanic box carries 'AHD', which supports it (see the parent's ref_check).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.v. same\",\n              \"stance\": \"supports\",\n              \"note\": \"'same, adj. ... — ME., fr. ON. samr, “the same” ... fr. I.-E. base *sem-, *sm̥-, “one, ...”' — Klein, like Etymonline, makes it a Norse loan.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Same (cross-referred from Simple)\",\n              \"stance\": \"supports\",\n              \"note\": \"Skeat's 'Simple' entry sends the reader to 'Same' for L. sim-, 'from the base sama-, the same', linking the Germanic and Latin halves of this chart under one base.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985 index\",\n              \"stance\": \"supports\",\n              \"note\": \"'SAME sem-1 ... SOME sem-1 ... -SOME1 sem-1 ... SEEM sem-1' (index lines 2209, 2276).\"\n            }\n          ]\n        },\n        {\n          \"id\": 16,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"A second unlabelled pass-through box, this one for the inherited (not borrowed) Latin material: semel 'once' and simul (older semol, semul) 'at the same time' from *sem-el-; similis 'of the same kind' from *sm̥-alo-; singulus 'single, one by one' from *sem-golo-; simplex and simplus 'one-fold' from *sm̥-plek-/*sm̥-plo-; and (per Watkins) sincerus from *sm̥-kēro- 'of one growth'. Pokorny 903 sets out the same series: 'ablaut. lat. similis ‚ähnlich‘ (*semelis ‚von ein und derselben Art‘), simul, älter semol, semul ‚zugleich‘ ... erweitertes *semlis ‚einmal‘ in semel, umbr. sumel ‚zugleich‘'; and p. 902 'lat. sim-plus, -plex ‚einfach‘'.\",\n          \"derivation_fa\": \"این هم جعبهٔ گذرگاهیِ دومی است، اما برای مادهٔ موروثی لاتین (نه وام‌گرفته): semel «یک‌بار» و simul (کهن‌تر semol، semul) «هم‌زمان» از *sem-el-؛ similis «هم‌گونه» از *sm̥-alo-؛ singulus «تک، یک‌یک» از *sem-golo-؛ simplex و simplus «یک‌لا» از *sm̥-plek- و *sm̥-plo-؛ و بنا بر واتکینز sincerus از *sm̥-kēro- «یک‌رُست». پوکورنی در ص ۹۰۳ همین رشته را می‌آورد: «لاتین similis ‚همانند‘ (از *semelis ‚از یک گونه‘)، simul کهن‌تر semol/semul ‚هم‌زمان‘ ... و *semlis گسترش‌یافته در semel، اومبریایی sumel» و در ص ۹۰۲ «لاتین sim-plus، -plex ‚یک‌لا‘». ادعای نورایی درست است.\",\n          \"sources\": [],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"supports\",\n              \"note\": \"Watkins 1985 s.v. sem-1: 'I.2. Suffixed form *sem-el- in Latin simul, at the same time: SIMULTANEOUS; ASSEMBLE, ENSEMBLE. 3. Suffixed form *sem-golo- in Latin singulus, alone, single: SINGLE. 4. Compound *sem-per- ... IV.4. Suffixed form *sm̥-alo- in Latin similis, of the same kind, like: SIMILAR; ASSIMILATE, RESEMBLE. 5. Compound *sm̥-kēro-, of one growing (see ker-3). 7. Compound *sm̥-plek-, “one-fold” ... in Latin simplex: SEMPLICE, SIMPLEX, SIMPLICITY. 8. Compound *sm̥-plo- ... in Latin simplus, simple: SIMPLE.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"Pokorny 902-903 (POK_03.txt leaves 137-138)\",\n              \"stance\": \"supports\",\n              \"note\": \"'sm̥- als 1. Kompositionsglied: ... lat. sim-plus, -plex ‚einfach‘'; 'Mit l-Suffixen: gr. ὁμαλός ... ablaut. lat. similis ‚ähnlich‘ (*semelis), simul, älter semol, semul ‚zugleich‘ ... *semlis ‚einmal‘ in semel, umbr. sumel ‚zugleich‘'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Simple (SKT.txt line 17295)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Simple. (F.-L.) F. simple, L. simplicem, acc. of simplex, lit. “one-fold.” — L. sim-, from the base sama-, the same (appearing also in sin-guli, one by one, sem-el, once, sim-ul, together); and plic-, from plicare, to fold: see Same and Ply.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny II 490\",\n              \"stance\": \"supports\",\n              \"note\": \"The same Latin set (similis, simul, semel, simplex) appears in the older Walde-Pokorny presentation of the sem- article.\"\n            }\n          ]\n        },\n        {\n          \"id\": 17,\n          \"lang\": \"English\",\n          \"words\": \"single, simple, sincere, similar; simulate, simultaneous, resemble, assemble\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Seven of the eight are straightforward. single (14c.) < Old French sengle < Latin singulus; simple (12c.) < Old French simple < Latin simplus/simplex 'one-fold'; similar (1610s) < Medieval Latin similaris < Latin similis; simulate (1620s) < Latin simulare 'to make like', denominative of similis; simultaneous (1650s) < Medieval Latin simultaneus, from Latin simul 'at the same time'; resemble (14c.) < Old French resembler < re- + sembler < Latin simulare; assemble (13c.) < Old French assembler < Vulgar Latin *assimulare 'to bring together', ad- + simul. All are in Watkins's sem-1 derivative list. The exception is sincere (1530s, via French sincère from Latin sincerus 'pure, unmixed'), which Watkins assigns to a compound *sm̥-kēro- 'of one growth' (*sem- + *ker- 'to grow') but which Etymonline, following OED, calls 'a word of uncertain origin' and reports only as 'Watkins has it as originally \\\"of one growth\\\"'. The node is therefore 'plausible': one of its eight words rests on a contested analysis.\",\n          \"derivation_fa\": \"هفت واژه از هشت واژهٔ این جعبه بی‌اشکال‌اند: single (سدهٔ چهاردهم) از sengle فرانسهٔ کهن و آن از singulus لاتین؛ simple (سدهٔ دوازدهم) از simple فرانسهٔ کهن و آن از simplus/simplex «یک‌لا»؛ similar (۱۶۱۰م) از similaris لاتین میانه از similis؛ simulate (۱۶۲۰م) از simulare لاتین «همانند کردن»؛ simultaneous (۱۶۵۰م) از simultaneus لاتین میانه از simul؛ resemble (سدهٔ چهاردهم) از resembler فرانسهٔ کهن (re- + sembler < simulare)؛ و assemble (سدهٔ سیزدهم) از assembler فرانسهٔ کهن و آن از *assimulare لاتین عامیانه (ad- + simul). همهٔ این‌ها در فهرست مشتقات sem-1 نزد واتکینز آمده‌اند. استثنا واژهٔ sincere (۱۵۳۰م، از فرانسهٔ sincère و لاتین sincerus «ناب، ناآمیخته») است که واتکینز آن را ترکیب *sm̥-kēro- «از یک رویش» می‌داند ولی اتیمآنلاین به پیروی از فرهنگ آکسفورد آن را «واژه‌ای با خاستگاه نامعلوم» می‌خواند و تحلیل واتکینز را تنها به‌عنوان یک نظر نقل می‌کند. پس این جعبه در مجموع با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/sincere\",\n            \"https://www.etymonline.com/word/samovar\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 s.v. sem-1 supplies SINGLE, SIMPLE, SIMPLEX, SIMPLICITY, SIMILAR, ASSIMILATE, RESEMBLE, SIMULTANEOUS, ASSEMBLE, ENSEMBLE, and the index (line 2259) confirms 'SIMILAR sem-1 SIMPLE sem-1 SIMPLEX sem-1 SIMPLICITY sem-1 SIMULTANEOUS sem-1 ... SINGLE sem-1'. SINCERE, however, is entered only as 'Compound *sm̥-kēro-, of one growing (see ker-3)', i.e. as an inference, and SIMULATE is not separately indexed under this root (it belongs with SIMILAR via similis).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein 1966 s.vv. simple, similar, sincere\",\n              \"stance\": \"partial\",\n              \"note\": \"Klein derives simple/similar from L. simplus/similis and the base *sem-, but flags sincerus as of disputed origin, exactly as OED does.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Simple\",\n              \"stance\": \"supports\",\n              \"note\": \"'L. sim-, from the base sama-, the same (appearing also in sin-guli, one by one, sem-el, once, sim-ul, together); and plic-, from plicare, to fold' — Skeat's analysis is Nourai's.\"\n            },\n            {\n              \"src\": \"LEW\",\n              \"where\": \"Walde, LEW (1910) s.v. sincerus\",\n              \"stance\": \"partial\",\n              \"note\": \"Walde already lists sincerus among the words of uncertain formation; the 'sm̥-ker-' analysis is a modern conjecture, not a settled result.\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T02:18:06.029Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-442.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T02:18:11.216Z] TOOL CALL #85: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-442.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 442",
 "description": "Validate JSON and run verify_check"
}
```


### [2026-09-14T02:18:12.608Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'disputed': 4, 'plausible': 4, 'confirmed': 8, 'transcription_suspect': 1}
root verdicts: {'confirmed': 1}
ref checks: {'partial': 5, 'supports': 10, 'not_checked': 8, 'contradicts': 2}
books consulted: {'supports': 33, 'partial': 4, 'contradicts': 3, 'silent': 9} | by book: {'KLN': 8, 'POK': 5, 'SKT': 5, 'BRT': 3, 'CHEUNG': 3, 'PHD': 3, 'AHD': 3, 'WLD': 3, 'KNT': 2, 'HUB': 2, 'NYB': 2, 'MON': 2, 'LEW': 2, 'LKT': 2, 'HRN': 1, 'FSD': 1, 'IEC': 1, 'ARY': 1}
```


## [2026-09-14T02:18:36.041Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-442.json` written; `verify_check.py 442` reports 17/17 nodes, 0 PROBLEM lines.

**Page 442 (book 412), entry 0 — root "Sem 1, Sm" (PIE \*sem- "one, together"): root confirmed.**
Node verdicts: 8 confirmed · 4 plausible · 4 disputed · 1 transcription_suspect.

Disputed:
- **#1 Avestan `han-vaěg` → #2 `angîxtan`** — Cheung 2007 s.v. \*gaiz derives MP hangēz-/hangēxtan from \*ham-gaiz-, not \*ham-vaij- (\*ham-vaij- would give MP \*hanwēz-). Horn 1893:30, which Nourai cites, is the superseded view. Same node also mislabels OP Haᵑgmatāna- and reconstructed OP \*hanjāma- as Avestan.
- **#3 Avestan `han-davatha` → #4 `andŭh`** — unattested form; Cheung (s.v. \*θuaxš) derives MP andōh "sorrow" from \*ham-tuxš- (Av. θβaxš-, OP hamataxš-), with Sogd. ʾntwxs, Chwar. ʾndyx. Nourai's ☞Dheu 2 is rejected.
- **#6 Greek `sun`, `sun-phonos`, `sun-ballein`, `sun-posion`** — σύν/ξύν is not from \*sem-: Pokorny himself (p.904) points to \*ksu/\*ksun; Watkins has a separate root "ksun"; Klein p.1557 (the very page cited) says "of uncertain origin"; Wiktionary/Etymonline: Myc. ku-su → PHel. \*ksún. ὁμός/ὁμαλός in the same box are fine.

Transcription / **extraction error for the owner to fix**:
- **#13 Persian samâvar** — JSON has «ساموار»; the printed page (rendered at 1200 dpi, copy saved to `data/verification/sources/refs/ocr/BOOK/442.png`) clearly prints **«سماور»**. `error_in: extraction`.
- Minor, not flagged as a node verdict: node #8's last word appears on the page as «سمپوزیم» (no second و); JSON normalises to «سمپوزیوم».

Ref-check highlights: BQT:2368 is exact (Mo'in's همدان footnote gives Pahl. Hamatān / OP Hagmatāna / Spiegel's Hangmatāna / "hangmata از ریشهٔ GAM = جای اجتماعات"); KNT:211–212 is exact and verbatim (ha-, hadā < \*sm̥-dhe, haᵐkarta- "cooperation"); POK:902,904 exact; IEC:1246 = "somos"; KLN:1557 correct page but contradicts. MON:1918/1921 and VOP:372 not checkable (6-vol Mo'in and Moshiri have no scan anywhere). Note: the local `KNT.txt` OCR is truncated and omits the whole H- section of Kent's lexicon — worth re-OCRing.
