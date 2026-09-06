# Verification process log — verify-page-249


## [2026-09-06T16:00:44.111Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 249 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-249.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-249.json. Write /home/sfmqrb/git/rishe/data/verification/page-249.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 249` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T16:00:45.731Z] AGENT

I'll start by reading the agent instructions.


## [2026-09-06T16:00:46.441Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T16:00:46.456Z] TOOL RESULT

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


## [2026-09-06T16:00:46.823Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-249.txt"
}
```


### [2026-09-06T16:00:46.835Z] TOOL RESULT

```
1	=== PDF page 249 (book page 219) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kei 4; Koi-to : to lie, rest; bed, couch, home, domain  (refs POK:539)
4	#1 (parent #0) [Greek] refs=POK:539; TAD:2 | koite, ari-koite : (decorated) bed ; koiman : put to sleep ; koimeterion : sleeping room
5	  #2 (parent #1) [Arabic] refs=TAD:2; FVA:30 | arîkeh : throne ; a.r.k : bed
6	    #3 (parent #2) [Persian] refs=FVA:30; MON:210; BQT:112 | arîkeh «اریکه» : bed, throne, domain ; arâek «ارایک» : thrones, domains
7	  #4 (parent #1) [Latin] refs=AHD:217 | coemeterion : sleeping room, graveyard
8	    #5 (parent #4) [English] refs=AHD | cemetery
9	#6 (parent #0) [Sanskrit] refs=AHD:1196 | siva : auspicious, dear
10	  #7 (parent #6) [Persian] refs=MON5:960 | Šîvâ «شیوا ۲» : one of the Hindu Gods
11	  #8 (parent #6) [English] refs=AHD | Siva, Shiva : the God of destruction and reproduction in Hinduism
12	#9 (parent #0) [Latin] refs=AHD | cîvis : a member of the household, citizen
13	  #10 (parent #9) [English] refs=AHD | civil, civic, city, civilization
14	#11 (parent #0) [Old High German] refs=AHD | heim : home ; heimerich : house ruler
15	  #12 (parent #11) [Old French] refs=AHD | ham, hamlet : village
16	    #13 (parent #12) [English] refs=AHD | hamlet, Hamlet
17	  #14 (parent #11) [English] refs=AHD:615 | Henry
18	--- entry 1 ---
19	ROOT Kek -> redirect to Keg
20	--- entry 2 ---
21	ROOT [Indo-European] Keku, Qeque; Teuk-os : club, hammer; beak, peak, tip  (refs WLD1:381; POK:543; IEC:1390)
22	#1 (parent #0) [Avestan] refs=POK:543 | kakuš, čakuš : ax, hammer
23	  #2 (parent #1) [Pahlavi] refs=BQT:613 | cakôč : ax
24	    #3 (parent #2) [Persian] refs=POK:543; SYN:597; BRT:575; MON:1268; IEC:1390 | čakkoš «چکش» : hammer ; čâqŭ «چاقو» : knife | extra: چکوچ ، چاکوچ | NOTE: IEC links "čakkoš" to "čowgân". See root "Čop"
25	#4 (parent #0) [Old Persian] refs=POK:543 | queke : club, staff
26	  #5 (parent #4) [None] refs=None | 
27	#6 (parent #0) [Pahlavi] refs=MON:1300 | čakât : peak, tip
28	  #7 (parent #6) [Persian] refs=FRS:80; MON:1300 | čakâd «چکاد» : peak, summit, high point | extra: چکاده
29	#8 (parent #0) [Sanskrit] refs=IEC:1390 | čokah : peak, hammer
30	
```


## [2026-09-06T16:00:50.035Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-249.json",
 "description": "Read source JSON for page 249"
}
```


### [2026-09-06T16:00:50.074Z] TOOL RESULT

```
{
  "pdf_page": 249,
  "book_page": 219,
  "entries": [
    {
      "root": {
        "name": "Kei 4; Koi-to",
        "lang": "Indo-European",
        "refs": "POK:539",
        "gloss": "to lie, rest; bed, couch, home, domain"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Greek",
          "refs": "POK:539; TAD:2",
          "words": [
            {"translit": "koite, ari-koite", "gloss": "(decorated) bed", "script": null},
            {"translit": "koiman", "gloss": "put to sleep", "script": null},
            {"translit": "koimeterion", "gloss": "sleeping room", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Arabic",
          "refs": "TAD:2; FVA:30",
          "words": [
            {"translit": "arîkeh", "gloss": "throne", "script": null},
            {"translit": "a.r.k", "gloss": "bed", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "FVA:30; MON:210; BQT:112",
          "words": [
            {"translit": "arîkeh", "gloss": "bed, throne, domain", "script": "اریکه"},
            {"translit": "arâek", "gloss": "thrones, domains", "script": "ارایک"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 1,
          "lang": "Latin",
          "refs": "AHD:217",
          "words": [
            {"translit": "coemeterion", "gloss": "sleeping room, graveyard", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "cemetery", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "AHD:1196",
          "words": [
            {"translit": "siva", "gloss": "auspicious, dear", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "MON5:960",
          "words": [
            {"translit": "Šîvâ", "gloss": "one of the Hindu Gods", "script": "شیوا ۲"}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 6,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "Siva, Shiva", "gloss": "the God of destruction and reproduction in Hinduism", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "cîvis", "gloss": "a member of the household, citizen", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "civil, civic, city, civilization", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Old High German",
          "refs": "AHD",
          "words": [
            {"translit": "heim", "gloss": "home", "script": null},
            {"translit": "heimerich", "gloss": "house ruler", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": "Old French",
          "refs": "AHD",
          "words": [
            {"translit": "ham, hamlet", "gloss": "village", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 12,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "hamlet, Hamlet", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 11,
          "lang": "English",
          "refs": "AHD:615",
          "words": [
            {"translit": "Henry", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kek",
        "redirect": "Keg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Keku, Qeque; Teuk-os",
        "lang": "Indo-European",
        "refs": "WLD1:381; POK:543; IEC:1390",
        "gloss": "club, hammer; beak, peak, tip"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:543",
          "words": [
            {"translit": "kakuš, čakuš", "gloss": "ax, hammer", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Pahlavi",
          "refs": "BQT:613",
          "words": [
            {"translit": "cakôč", "gloss": "ax", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "POK:543; SYN:597; BRT:575; MON:1268; IEC:1390",
          "words": [
            {"translit": "čakkoš", "gloss": "hammer", "script": "چکش"},
            {"translit": "čâqŭ", "gloss": "knife", "script": "چاقو"}
          ],
          "script_extra": "چکوچ ، چاکوچ",
          "note": "IEC links \"čakkoš\" to \"čowgân\". See root \"Čop\"",
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "POK:543",
          "words": [
            {"translit": "queke", "gloss": "club, staff", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "MON:1300",
          "words": [
            {"translit": "čakât", "gloss": "peak, tip", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "FRS:80; MON:1300",
          "words": [
            {"translit": "čakâd", "gloss": "peak, summit, high point", "script": "چکاد"}
          ],
          "script_extra": "چکاده",
          "note": null,
          "quote": {
            "text": "بیامد دوان دیده بان از چکاد - که آمد از ایران سپاهی چو باد",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "IEC:1390",
          "words": [
            {"translit": "čokah", "gloss": "peak, hammer", "script": null}
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


## [2026-09-06T16:00:50.295Z] TOOL CALL #4: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T16:00:50.356Z] TOOL RESULT

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


## [2026-09-06T16:01:18.058Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['POK','AHD','TAD','FVA','FVQ','MON','BQT','IEC','WLD1','WLD','SYN','BRT','FRS','KLN','SKT','PHD','NYB','HRN','HUB','ARY','LKT','TTS','LEW','LAT','AFM','PLA']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:700] if v else 'MISSING')\n\""
}
```


## [2026-09-06T16:01:18.478Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/ | head -50; echo ---; ls /home/sfmqrb/git/rishe/tools/"
}
```


### [2026-09-06T16:01:19.802Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie
== TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; inside.php search works.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/TAD_pag
== FVA {"title": "S.M. Nahvi, Farhang-e Vazheha-ye Arabi dar Farsi (dakhil), Tohi/Azadi 1368/1989", "kind": "catalog", "url": "https://openlibrary.org/works/OL4602367W (edition OL2012991M: Intisharat-i Islami 1368/1989, 582 pp)", "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: no digital copy found.", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: still no digital copy on any permitted platform. Library catalogues list the 1368 book under the variant title «فرهنگ ریشهٔ وام‌واژه‌های عربی (لغات عربی مستعمل در فارسی دخیل)» — reconcile with Nourai's title when buying. Catalogue record only."}
== FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ.txt"], "page_offset": "printed page = leaf − 17 (0-based \\f blocks in FVQ_pages.txt; 
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct
== WLD1 MISSING
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 
== FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS.txt"], "page_
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<i
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' nu
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/
== LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 'NNNN. word (language) meaning' - Lokotsch is usually cited by entry number, but Nourai cites pages.
== TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": "TTS_pages.txt: 253 leaves; printed page N = leaf N+30.", "lookup_hint": "Not searched exhaustively 
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.o
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detec
== AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFM.txt"], "page_offset": "19
== PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 leaves (pdftotext -layout, \\f-separated): printed page = leaf(1-based) − 15 (leaf 291 = p.276).", "loo
```


### [2026-09-06T16:01:19.850Z] TOOL RESULT

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
build_site.py
fetch_source.py
ganjoor.py
__pycache__
ref_index_latin.py
ref_index_pages.py
ref_locator
ref_ocr_book.py
ref_page.py
research.py
validate.py
verify_archive_sources.py
verify_check.py
verify_export_process.py
verify_publish.sh
```


## [2026-09-06T16:01:22.377Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-06T16:01:22.456Z] TOOL RESULT

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


## [2026-09-06T16:01:27.957Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'BEGIN{RS=\"\\f\"} NR==548' POK_01.txt | head -80",
 "description": "Print POK p.539"
}
```


## [2026-09-06T16:01:29.373Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"koimeterion\\|koimēt\\|koitē\\|koite\" AHD_watkins1985.txt | head -20; echo \"=== kei-1\"; grep -n \"^kei-\\|kei-1\\|kei-¹\" AHD_watkins1985.txt | head -20",
 "description": "Grep AHD for kei"
}
```


### [2026-09-06T16:01:29.662Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T16:01:29.718Z] TOOL RESULT

```
=== kei-1
582:kei-'
595:kei-'. To lie; bed, couch; beloved, dear. I. Basic form *kei-. 1. Suffixed form *kei-wo- in: a. Germanic *hiwa- in Old English hiwan, members of a household: HIND?;
596:kei-?
599:kei-2, Referring to various adjectives of color. 1. Suffixed o-grade form *koi-ro- in German *hairaz, “gray-haired,” old, venerable, hence master, in: a. Old English har, gray, hoary: HOAR; b. Old High German hér, worthy, exalted: JUNKER; Cc. Middle Dutch here, master, lord: YOUNKER. 2. Suffixed zero-grade form *ki-wo- in Germanic *hiwam in Old English hiw, héo, color, appearance, form: HUE}. [Pok. 2. Rei- 540.]
600:kei-3. To set in motion. I. Possibly extended o-grade form *koid- with suffixed form *koi-d-ti- in Germanic *haissiz in: a. Old English h&s, a command, a bidding: HEST; b. Old English compound beh#s, a vow, promise, com- mand (be-, intensive prefix; see ambhi): BEHEST (but perhaps to be referred to a separate root *kaid-). Il. Zero-grade form *ki-. 1. Form *ki-eyo- in Latin ciére (past participle citus), with its frequentative citdre, to set in motion, summon: CITE; EXCITE, INCITE, OSCITANCY, RESUSCITATE, SOLICITOUS. 2. Suffixed form *ki-neu- in Greek kinein, to move (> kinésis, motion): KINEMATICS, -KINESIS, KINETIC; CINEMATOGRAPH, CINEMATORADIOG- RAPHY, HYPERKINESIA, KINESIOLOGY, KINESTHESIA, KININ, (TELEKINESIS). [Pok. kei- 538.]
1340:CELLA kel-2 CELLAR kel-2 CELLARER kel-2 CEMBALO keu-2, kleu-3 CEMENT kae-id- CEMETERY kei-1 CENACLE sker-1 -CENE_ ken-3 CENOBITE gWei-, kom CENOGENESIS ken-3 CENOTAPH dhembh-, ken-4 Cenozoic ken-3 CENSOR kens- CENSUS kens- CENT dekm CENTAL dekm CENTAVO dekm CENTENARIAN dekm CENTENARY dekm CENTENNIAL dekm CENTER kent- CENTESIMAL dekm CENTESIS kent- CENTI- dekm CENTIGRADE ghredh- CENTIME dekm CENTNER dekm CENTO kentho- CENTRIFUGAL bheug-'
1364:ciTy kei-1
1365:civic kei-1
1366:CIVIL kei-1 CLADOCERAN kel-1, ker-1
1605:HIDE! (s)keu- HIDE? (s)keu- HIDE? kei-1 HIDROSIS sweid-2 HIE kigh- HIEMAL = ghei-2 HIERARCH eis-! HIERARCHY eis-! HIERATIC  eis-1 HIERO- eis-1
1616:HIND? = kei-1
1676:INCIDENT kad- INCINERATE keni- INCIPIENT kap- INCISE kae-id- INCITE kei-3 INCLINE klei- INCLUDE kleu-3 INCONDITE dhé-1 INCREASE ker-3 INCUBATE keu-2 INCULT kWwel-1 INCUMBENT keu-2 INCUNABULUM kei-1 INCUR kers-2 INCUS kau-2 INDEMNIFY dap- INDEMNITY dap- INDENT! dent- INDENTURE dent- INDEX deik- INDICATE deik- INDICT deik- INDIGEN gene- INDIGENOUS gene- INDIGENT eg- INDIGN dek-1 INDIGNANT dek-1 INDIGNATION dek-1 INDITE deik- INDOLENT del-3 INDOMITABLE deme-2 INDUCE deuk- INDURATE deru INDUSTRY en, ster-2 INEBRIATE 6g¥h- INEFFABLE bha-2 INELUCTABLE leug-1 INEPT ap-1
```


## [2026-09-06T16:01:33.796Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '590,600p' AHD_watkins1985.txt",
 "description": "AHD kei-1 full entry"
}
```


### [2026-09-06T16:01:33.841Z] TOOL RESULT

```
kau-'. To howl (imitative). 1. Reduplicated suffixed form *ka-kau-ro- in Sanskrit cakorah, partridge: CHUKAR. 2. Reduplicated form *k6-kii-o- in Greek kdkuein, to wail, lament: Cocytus. [Pok. kau- 535.]
kau-2, To hew, strike. 1. Germanic *hawwan in: a. Old English héawan, to hew: HEW; b. Old Norse héggva, to cut: HAGGLE; c. Old ‘French hove, a hoe: HOE. 2. Ger- manic *hawwé6 in Old Norse hégg, a gap, a cutting blow, akin to the source of HAG?. 3. Germanic *haujam in Old English hieg, hay, cut grass: HAY. 4. Suffixed form *kau-do- in Latin ciidere (< *caudere), to strike, beat: incus. [Pok. kdu-, 535.]
kaul-. Stalk, stem. Latin caulis, stalk, stem, cab- bage-stalk, cabbage: CAULICLE, CAULINE, COLE, KALE; AMPLEXICAUL, CAULESCENT, CAULIFLOWER, COLCAN- NON, COLESLAW, KAILYARD SCHOOL, KOHLRABI. [Pok. kau-l- 537.)
ked-. To go, yield. 1. Lengthened-grade form *kéd- in Latin cédere, to go, withdraw, yield: CEASE, CEDE, CES- SION; ABSCESS, ACCEDE, ACCESS, ANCESTOR, ANTECEDE, CONCEDE, CONCESSION, DECEASE, EXCEED, INTERCEDE, PRECEDE, PREDECESSOR, PROCEED, RECEDE, RETRO- CEDE, SECEDE, SUCCEED. 2. Prefixed and suffixed form *ne-ked-ti-, “from which one cannot draw back” (*ne-, not; see ne), in Latin necesse, inevitable, unavoidable: NECESSARY. [In Pok. sed- 884.]
keg-. Hook, tooth. 1. Germanic *hakan- in: a. Old Norse haki, hook, akin to Old English haca, hook: HAKE; b. Middle Low German hake, hook: HARQUEBUS. 2. Ger- manic lengthened form *Adka- in: a. Old English héc, hook: HOOK; b. Middle Dutch hok, hoec, hook: HOOKER}. 3. Germanic *hakila- in Middle Dutch hekel, hatchel, a flax comb with long metal hooklike teeth: HECKLE. 4. Germanic *hakkijan in Old English -haccian, to hack to pieces as with a hooked instrument: Hack!. [Pok. keg- 537.]
kei-'. To lie; bed, couch; beloved, dear. I. Basic form *kei-. 1. Suffixed form *kei-wo- in: a. Germanic *hiwa- in Old English hiwan, members of a household: HIND?;
kei-?
b. suffixed Germanic form *hiwid6 in Old English higid, hid, a measure of land (< ‘household”): HIDE®. 2. Suf- fixed form *kei-wi- in Latin civis, citizen (< “member of a
- household”): cITy, CIVIC, CIVIL. II. O-grade form *koi-. 1. Suffixed form *koi-nd- in Latin ciinae, a cradle: INCUNABULUM. 2. Suffixed form *koi-m-d- in Greek koiman, to put to sleep: CEMETERY. III. Suffixed zero-grade form *ki-wo- in Sanskrit siva, auspicious, dear: SHIVA. [Pok. 1. kei- 539.]
kei-2, Referring to various adjectives of color. 1. Suffixed o-grade form *koi-ro- in German *hairaz, “gray-haired,” old, venerable, hence master, in: a. Old English har, gray, hoary: HOAR; b. Old High German hér, worthy, exalted: JUNKER; Cc. Middle Dutch here, master, lord: YOUNKER. 2. Suffixed zero-grade form *ki-wo- in Germanic *hiwam in Old English hiw, héo, color, appearance, form: HUE}. [Pok. 2. Rei- 540.]
kei-3. To set in motion. I. Possibly extended o-grade form *koid- with suffixed form *koi-d-ti- in Germanic *haissiz in: a. Old English h&s, a command, a bidding: HEST; b. Old English compound beh#s, a vow, promise, com- mand (be-, intensive prefix; see ambhi): BEHEST (but perhaps to be referred to a separate root *kaid-). Il. Zero-grade form *ki-. 1. Form *ki-eyo- in Latin ciére (past participle citus), with its frequentative citdre, to set in motion, summon: CITE; EXCITE, INCITE, OSCITANCY, RESUSCITATE, SOLICITOUS. 2. Suffixed form *ki-neu- in Greek kinein, to move (> kinésis, motion): KINEMATICS, -KINESIS, KINETIC; CINEMATOGRAPH, CINEMATORADIOG- RAPHY, HYPERKINESIA, KINESIOLOGY, KINESTHESIA, KININ, (TELEKINESIS). [Pok. kei- 538.]
```


## [2026-09-06T16:01:35.668Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"koimáō\\|koimetérion\\|Wiege\\|ḱei-\\|kei-, ki-\\|1\\. ḱei-\" POK_full.txt | head -20; echo ===; grep -n \"539\" POK_full.txt | head",
 "description": "Grep POK_full"
}
```


### [2026-09-06T16:01:35.725Z] TOOL RESULT

```
Exit code 1
(eval):1: == not found
```


## [2026-09-06T16:01:50.080Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"tkei-\\|HAMLET\\|HAUNT\\|Haimirich\\|haimaz\" AHD_watkins1985.txt | head -20",
 "description": "AHD tkei"
}
```


### [2026-09-06T16:01:50.129Z] TOOL RESULT

```
1094:tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *()koi-mo- in Germanic *haimaz, home, in: a. Old Eng- lish hdm, home: HOME; b. Old Norse heimr, home: NIFLHEIM; C. Middle Dutch hame, hame (< “covering”): HAME; d. Old French ham, village, home: HAMLET; e. Germanic *haimatjan, to go or bring home, in Old French hanter, to frequent, haunt: HAUNT. 2. Zero-grade form *tki- in Greek kti- in ktizein, to found, settle: AMPHYCTYONY. 3. Probable zero-grade form *tki- in Latin si- in suffixed form *si-tu- in situs, location: SITUATE, SITUS. [Pok. 1. hei- 589, Athei- 539.] to-. Demonstrative pronoun. For the nominative singular see so-. 1. Germanic *thé- in: a. Old English thé, thy (instrumental case), by the: THE!, THE?; NATHELESS; b. Middle Dutch de, the: pEcoy. 2. Germanic *thauh, “for all that,” in Old Norse thd, though, akin to the Scandinavian source of Middle English though, though: THOUGH. 3. Germanic *thasi- in Old English thes, this, this: (THESE), THIS. 4. Germanic *thana- in Old English thanne, thenne, thenne, than, then: THAN, THEN. 5. Ger- manic *thanana- in Old English thanon, thence: THENCE. 6. Germanic *thér in Old English ther, thér, there: THERE. 7. Germanic *thathro in Old English theder, thider, thither: THITHER. 8. Germanic nomina- tive plural *thai in Old English tha and Old Norse their, they: THEY. 9. Germanic genitive plural *thaira in Old Norse their(r)a, theirs: THEIR. 10. Germanic dative plural *thaimiz in Old Norse theim and Old English thém, them: THEM. 11. Extended neuter form *tod- in: a. Ger- manic *that in Old English thet, that: THAT, (THOSE); b. Greek to, the: TAUTO-. 12. Germanic *thus- in Old English thus, thus: THUS. 13. Adverbial (originally accu- sative) form *tam in Latin tandem, at last, so much (> Anglo-Norman tant): TANDEM, TANTAMOUNT. 14. Suf- fixed reduced form *t-dli- in Latin tdlis (plural tdlés), such: TALES. [Pok. 1. to- 1086.] tolky-. To speak. Metathesized form *tlokv- in Latin loqui, to speak: LOCUTION, LOQUACIOUS; ALLOCUTION, CIRCUMLOCUTION, COLLOQUIUM, (COLLOQUY), ELOCU- TION, GRANDILOQUENCE, INTERLOCUTION, MAGNIL- OQUENT, OBLOQUY, PROLOCUTOR, SOLILOQUY, VENTRILOQUISM. [Pok. tolk¥- 1088.] tong-. To think, feel. 1. Germanic *thank6n in: a. Old English thancian, to thank: THANK; b. Old English thencan, to think: THINK. 2. Germanic *(ga)thauht- (*ga-, collective prefix; see kom) in Old English (ge)- thoht, thought: THOUGHT. 3. Germanic factitive *thunk- Jan in Old English thyncan (third person singular present indicative thyncth), to seem: METHINKS. [Pok. 1. tong- 1088.] tragh-. To draw, drag, move. Rhyming variant dhragh-. Latin trahere, to pull, draw: TRACT!, TRACTABLE, TRAC- TION, TRAIL, TRAIN, (TRAIT), TREAT; ABSTRACT, AT- TRACT, CONTRACT, DETRACT, DISTRACT, EXTRACT, PORTRAY, PROTRACT, RETRACT, SUBTRACT. [Pok. tragh- 1089.] treb-. Dwelling. 1. Zero-grade form *trb- in Germanic *thurp- in Old English thorp, village, hamlet: THORP. 2. Latin trabs, beam, timber: TRABEATED, TRABECULA, TRAVE; ARCHITRAVE. [Pok. treb- 1090.] trei-. Three. I. Nominative plural form *treyes. 1. Ger- manic *thrijiz in Old English thrie, thréo, thri, three, with its derivatives thriga, thriwa, thrice, and thritig, thirty, and thréotine, thirteen: THREE, THRICE, THIRTY, THIRTEEN. 2. Latin trés (> Italian tre and French trois), three: TREY, TRIO; TRAMMEL, TRECENTO, TREPHINE, TRIUMVIR, TROCAR. II. Zero-grade form *tri-. 1. Suffixed form *tri-tyo- in: a. Germanic *thridjaz, third, in (i) Old English thrid(d)a, thirdda, third: THIRD (ii) Old Norse thrithi, third: RIDING?; b. Latin tertius (neuter tertium), third: TERCEL, TERCET, TERTIAN, TERTIARY, TIERCE; SESTERCE. 2. Latin évi-, three: TRI-, TRIPLE. 3. Greek t7i-, three: TRI-; TRICLINIUM, TRICROTIC, TRIDACTYL, TRI- GLYPH, TRITONE. 4. Sanskrit tri, three: TRIMURTI.
1239:AMITY amma AMMUNITION mei-3 AMNESIA men-! AMNESTY men-1 AMNIOCENTESIS kent- AMOEBA mel-1 AMONG mag- AMORETTO amma AMORTIZE mer-2 AMOUNT ad-, men-2 AMOUR amma AMPHI- ambhi AMPHIBIOUS gWei- AMPHIBOLE gWelg-1 AMPHIBRACH mregh-u- AMPHIMACER mak- AMPHIMIXIS meik- AMPHIOXUS ak- AMPHISBAENA gWa- AMPHISTYLAR sta- AMPHITHECIUM dhé-1 AMPHORA bher-1 AMPHOTERIC ambho AMPHYCTYONY  tkei- AMPLEXICAUL kaul-, plek- AMPLIFY dhé-1 AMPUTATE peu- AMRITA mer-2, ne AMYLUM mele- AN! oi-no-
1579:HAG2 kau-2 HAGGARD kagh- HAGGLE kau-2 HAGIO- yag- HAIL! kaghlo- HAIL? kailo- HAKE keg- HALBERD bhardha, kelp- HALE! kailo- HALE? kele-2 HALF skel-1 HALIBUT bhau- HALL kel-2 HALLOW kailo- HALO-  Sal-1 HALT! kel-3 HALT? kel-1 HALTER! kelp- HALTER? § sel-4 HAM konemo- HAMADRYAD deru, sem-! HAME_ tkei- HAMLET tkei- HAMMER ak- HANDIWORK kom HANDSEL sel-3 HANG konk- HANKER konk- HANUMAN genu-2 HAP kob- HAPLESS kob- HAPLOID pel-3, sem-1 HAPPEN kob- HAPPY kob- HARANGUE koro- HARBINGER koro- HARBOR koro- HARD kar-1 HARDS_ kes-! HARDY! = kar-1 HARE kas- HARM kormo- HARMONY ar- HARNESS _nes-1 HARPOON  serp-1 HARPSICHORD ghere- HARQUEBUS keg- HARRY koro- HART ker-1 HARTEBEEST ker-1 HARUSPEX ghere- HARVEST kerp- HASH! =skep- HASLET ghasto- HASTATE ghasto- HAT kadh- HATCHET skep- HATE kad- HATRED ar-, kad- HAUBERK kWel-1 HAUGH kel-2 HAUGHTY al-3 HAUL kele-2 HAULM kolem- HAUNT tkei- HAUSTELLUM aus-2 HAUSTORIUM aus-2 HAUTBOY al-3, busk- HAVE kap- HAVEN kap- HAW2 kagh- HAWK! kap- HAWKER keu-2 HAWSE kWel-1 HAWSER al-3 HAY kau-2 HAZEL koselo- HE! ko-
1638:HOMAGE dhghem- HOMBRE dhghem- HOME tkei-
1914:NIBBLE ken-2 NICE ne, skei- NICHE nizdo- NICKNAME aug-? NICTITATE kneigh- NIDDERING nei- NIDE_ nizdo- NIDIFY dhé-1, nizdo- NIDUS nizdo- NIECE nepot- NIELLO negW-ro- NIFLHEIM nebh-, tkei- NIGGARD_ ken-2 NIGH néhw-iz NIGHT nekw-t- NIGHTINGALE ghel-1 NIGHTMARE mer-2 NIGRESCENCE neg¥-ro- NIGRITUDE neg¥-ro- NIGROSINE negW-ro- NIHILISM ne NIHILITY ne
2265:SITAR ten-, trei- SITH sé@-2 SITUATE tkei- situs tkei-
```


## [2026-09-06T16:01:51.930Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -c \"\" POK_full.txt; grep -n \"kei-, ki-\\|1. k̑ei-\\|ḱei-\" POK_full.txt | head; echo \"---01---\"; grep -n \"koiman\\|koίμη\\|koimáō\\|Wiege\\|civis\" POK_01.txt | sed -n 1,20p",
 "description": "Locate Pokorny kei entry"
}
```


### [2026-09-06T16:01:52.009Z] TOOL RESULT

```
93771
---01---
```


## [2026-09-06T16:02:05.462Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && for f in POK_01.txt POK_02.txt POK_03.txt; do echo \"== $f\"; python3 -c \"\nimport sys\nt=open('$f',encoding='utf-8',errors='replace').read()\np=t.split('\\f')\nprint('leaves',len(p))\nprint(repr(p[300][:200]))\n\"; done",
 "description": "Inspect POK files"
}
```


### [2026-09-06T16:02:07.474Z] TOOL RESULT

```
== POK_01.txt
leaves 364
'7ni)  und  edu,  est  ds.,  Supin.  estw^  apr.  Ist,  isticei  , essen*»\naksl.  jamh  (*^mh),  3.  Sg.  jast^  (*est^,  idg.  *ed-ti),  3.  PI.  jadetz  ([^J *ednti),  Infin.  jasti  (alt  ästi),  Su'
== POK_02.txt
leaves 434
"  I  514  f..  WH.  I  45.  245  ff..  250.  846,  Trautmann  125.\n2.  k^el-  .fern  (örtlich  und  zeitlich)'  in:\nai.   caramd-   .der  letzte,  äußerste',   cirds   ,lang  (zeitlich)',   gr.  TfjXe"
== POK_03.txt
leaves 430
" habeS  bret.  tizaff  ,empfange^  (auf  Grund  einet  ^^^ ,das  Empfangene,  HabeO,  cymr.  teg  ,schön,  hübsch'  (vgl.  zur  Bei  i^- pwgr),  air.  etig  =  cjmv.  annheg  ^häßlich'  {*n-teki-)]  o"
```


## [2026-09-06T16:02:14.403Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"koTt-r]\\|koitē\\|koi/ir\\|cīvis\\|civis\" POK_02.txt | head -20; echo \"=== kei\"; grep -n \"^1\\. k.ei-\\|k\\^ei-\\|Uegen, sich lagern\\|liegen, sich lagern\" POK_02.txt | head -20",
 "description": "Find Pokorny kei entry"
}
```


### [2026-09-06T16:02:14.469Z] TOOL RESULT

```
=== kei
4812:k^o-,  k^.e-,  fem.  k^ä]  k^ei-  (vermutlich  einst  nur  im  Nom.  Akk.  Sg.). kY,u-  (nur  im  Adv.) ;  die  betonten  Formen  sind  Interrogativa,  die  im! betonten  Indefinita;  einzel sprachlich  z.  T.  Relativum  geworden.
4844:2.  Stamm  k^ei-,  gleiche  Form  für  Maskul..  Neutr.  und  Femin.:
```


## [2026-09-06T16:02:20.952Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,leaf in enumerate(t):\n    if 'sivá' in leaf or 'siva-' in leaf or 'civis' in leaf or 'Heim,' in leaf:\n        print('LEAF',i, leaf[:300].replace('\\n',' '))\n        print('---')\nEOF",
 "description": "Find Pokorny leaf with siva/civis"
}
```


### [2026-09-06T16:02:23.402Z] TOOL RESULT

```
LEAF 198 äbula  PL  , Wiege  ,Nest'  (*koi-na)  und  anord.  hldj  hidi  n. ,Lager  des  Bären'  (*kei-to-)', hitt.  Mediopassiv  ki-it-ta  (kitta)  und  ki-it-ta-ri  (kittari)  ,liegt' ;  vielleicht auch  lyk.  sijeni  ,liegt'  (Pedersen,  Ljkisch  u.  Hitt,  17). Mit  dem  Begriffe  ,Heim,  traut,  lieb': 
---
```


## [2026-09-06T16:02:26.335Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (196,197,198,199):\n    print('==== LEAF',i)\n    print(t[i][:2600])\nEOF",
 "description": "Print Pokorny leaves 196-199"
}
```


### [2026-09-06T16:02:29.378Z] TOOL RESULT

```
==== LEAF 196
el, StoppeP ;
germ.   *häkuda-  m.  ,Hecht'  (nach  den  spitzen  Zähnen)  in  ags.  hacodA *hakida  in  ags.   hacid  m.,  ahd.  hacMt,  hechit,  mnd.   heket  ^Hecht^^
lit.  kenge  f.  , Haken,  Klinke';
slav.  *kog^th  m.  in  russ.  kögoth  ,Klaue,  gekrümmte  Eisenspitze^,  osorb. kocht  ,Dorn,  Stachel'  (:  germ.  *hakuda-)-
vielleicht  hierher,  als  ,au£  einen  Haken   hinaufhängen,  wie  mit  einei Haken   kratzen,   reizen':   bulg.  kdcbj  kdc(ii)vam   ,erhebe,   erhöhe,    hänge*^ za-kdchj   -kdcam   ,hänge,    fasse,   necke',    serb.    zäkaciti    ,anhaken',   sloven. kdclti  ,necken,  ärgern'  (Berneker  465  f.).
WP.  I  382  f.,  WH.  I  307,  Trautmann  112,  Wissmann  Nom.  postverb. 182  f.,   Petersson,  Heterokl.  9 1  f . ;   Stokes  BB.  25,  252.
•'« kei-    ,in    Bewegung    setzen,    in    Bewegung   sein'    (:    koi-  :  kf-);    eu-Basis] (z.  T.  mit  22-Infix)  ki-{n-)eu-;  schwere  Basis  kiQ-  (:  Jcie-?).
Gr.  xio)  ,gehe  weg,  fahre'  ist  späte  Neubildung  zum  Aor.  e/.LOv]  Imper.i Y.U,  Partiz.  xiwy;
hom.  Präteritum  fxsr-sytiad-s,  -d-ov  {i  metr.  Dehnung)  , folgte  nach,  durch- streifte', Y.iazo'  s-ALvelvo  Hes.  (schwere  Wz.);  dvo-ytlvÖLog,  -y.lvöag  ,Esel- treiber',  y,Lvda^  , beweglich,  ei'nivrjTog''  (vgl.  zur   Bildung  äXlvdo),  ytvXlvdüijy
von  ki-n-eu-  :  gr.  y.tvv^ai  , werde  bewegt,  erschüttert,  gehe',  yavvaaoy,ai, ,sch wanke  hin  und  her',  '/.ivio)  ,setze  in  Bewegung,  treibe'  (*xlv«J^-ü>) ;
alb.  q^oj  , wecke,  erwecke'  (*kien{ö)j  qoj  , schicken,  senden'  (*ds-köj\ cys,  cyt  , reize,  necke'  (*ter-k{u-t-{ö),  syei^  syen  (*kiu-n-iö)  ,bestürmen,  an- fallen' (Jokl  Mel.  Pedersen  149 f.');
lat.  cieöj  eiere  (sekundär  ciö,  clre)  ,in  Bewegung  setzen,  rege  machen, herbeirufen'  (eiere  =  idg.  ki(i)e-??)j  citus  ,schnell',  cito,  -äre  ,in  Bewe- gung setzen,  kommen  lassen,  vorladen',  solli-citus  ,ganz,  stark  bewegt, beunruhigt,  in  Angst  und  Gefahr',  cunctus  (*con-citos),  gesamt,  sämtlich*.
Erweiterungen  von  der  einfachen  Wurzelform  kei-  aus :
Mit  d  (cZ-Präsens?):  vielleicht  ir.  cid-  z.  B.  mcisse  ,invecta',  Pass.  Konj. as-cesar   gl.    ,exseri'   (usw.,  Pedersen  KG.  II  490  f.),   sehr   wahrscheinlich  "^ got.  haitanj  ahd.  heisan,  ags.  hätan,  as.  hetan,  anord.  heita  ^heißen  {j=  aa- treiben),  befehlen,  anrufen,  nennen^;   vgl.  osset.  sidin  , rufend
I
539
Mit  i(o)- Formans:  Auf  *kEi-lo-s  ,bewegt,  wippend'  kann  beruhen:  lit. Jctele,  kyU,  lett.  cielaioa^  apr.  kylo  , Bachstelze',  acec
==== LEAF 197
 s:  ai.  cistati  ,bewegt  die  Glieder,  ist  in  Bewegung',  cesta- n.j  cestä ^Bewegung,  Gebärde'.
Wurzelform  ki-eu-  ohne  Nasalinfix:
ai.  cydvate  ,regt  sich,  geht  fort',  av.  5(y)avaite  ,setzt  sich  in  Gang, Marsch',  apers.  asiyavam  ,marschierte',  ai.  cyautnd-  n.  ,Unternehmung, Bemühung',  av.  syaod-na-  n.  ,Tun,  Handeln,  Wirken',  syaoman-  n.  ,Tat, Werk';
arm.  cu  (=  ai.  cyuti-)  , Aufbruch',  cvem  ,ich  breche  auf,  reise  ab',  Aor. (zum  Präs.  ert'am)  cogay  ,ich  ging'  (^kioit-)-,
gr.  Gsvo)  ,setze  in  rasche,  heftige  Bewegung',  Med.  ,eile,  bin  erregt' (aevstai  =  cyavate]  der  Diphthong  kann  nach  den  außerpräs.  Formen und  nach  unthemat.  Gevxai  festgehalten  sein),  hom.  saavTO  ,eilte',  Partiz. Perf.  ioav^svog,  iTvl-aavTog  ,herandrängend,  daherstürmend'  (=  ai.  cyutä- ,getrieben',  vgl.  av.  fra-süta-  ,in  Gang  gekommen*),  Ttav-avöir]  ,in  Eile'; att.  aovfxai  , bewege  mich  rasch  oder  heftig'  (^aoföofiaij^  avsi  (Bacchyl.) ,treibt',  iaoorjixevov  TsdoQvßri^hov,  öq^Tjjj^vov  Hes.,  hom.  Xao-Gaöog  ,die Völker  zum  Kampfe  antreibend';  att.  T€Vjj,ü)i.iaL  ,betreibe'  (vgl.  av.  syao- man-)-,  Tsvrd^u)  ,beschäftige  mich  anhaltend  mit  etwas';  eine  Dehnstufen- bildung wie  ai.  cyautnd-^  aber  rnit  geschwundenem  u^  ist  das  wohl  hierher gehörige  gcjtqov  ,das  hölzerne  Rad',  kTtlaooiXQOv  ,Radreifen'.
WP.  I  361  ff.,  WH.  I  213  f.,    Schwyzer  Gr.  Gr.  I  679,  686,  745.
I.'  kei-  ,liegen ;  Lager,  Heimstätte,  traut,  lieb  (von  derselben  Siedlung') ; koi'to-  , Lager' ;  kei-mo-,   koi-mo-  , vertraut',    kei-uo-,  ki-uo-   ds.
Ai.  süe  (älter  sdye)^  3.  PI.  sei%  av.  saUe  (:  gr.  -KelxaL)  ,liegt',  3.  PL sözVe,  ai.  sayate,  -ti  ,liegt,  ruht',  §ayä,  sayyä  , Lager',  madhyama-si-  ,in der  Mitte  sich  lagernd,  liegend',  ni-sl-tlia-  m.  »Mitternacht',  usw. ;
gr.  Y,sZTai  jliegt',  3.  PL  -/.eazai  aus  *xejnt-j  umgebildet  nach  y.sl-,  hom. xelaTat]  jung  ist  hom.  -Asoviai  (:  ai.  sayante)]  '/.oZxog  m.,  xotr^  f.  , Lager', äy,OLTig  , Gemahlin'  (mit  ion.  Psilose  aus  *&'-xoiTi$);  vgl.  bret.  {d)argud ,leichter  Schlaf  (^-are-koito-)]  v.oi^da)  , bringe  zu  Bett,  schläfere  ein'  (vgl. got.  haims,  air.  cöim,  lett.  säimey  auch  lit.  seimyna,  ags.  hceman).  Zweites Kompositionsglied  -x^-o-  in  Ttsqioöog,  vsoaaög,  u.  dgl.  Sehr  wahrscheinlich lat.  cünaej  cün
==== LEAF 198
äbula  PL  , Wiege  ,Nest'  (*koi-na)  und  anord.  hldj  hidi  n. ,Lager  des  Bären'  (*kei-to-)',
hitt.  Mediopassiv  ki-it-ta  (kitta)  und  ki-it-ta-ri  (kittari)  ,liegt' ;  vielleicht auch  lyk.  sijeni  ,liegt'  (Pedersen,  Ljkisch  u.  Hitt,  17).
Mit  dem  Begriffe  ,Heim,  traut,  lieb':
540  •
mit  i-Suffix  ai.  Hla-  n.  , Gewohnheit,  Charakter*,  air.  ce{i)le  , Genosse, Gatte*  (*kei-U{o-s\  mit  sekundärem  i  cymr.  cilydd  , Genosse*,  usw.;
mit  i22-Suffix:
gr.  7ioi(.iaa)  (s.  oben),  yLsmrjhov  ,aufbewahrtes  Gut*  (von  *%aliia  n.  ,Lager*)' dehnstufig  xcj.aiy  f.  ,Dorf*  (*^ö[i]mä);
air.  com,  cöem  ,lieb*,  acymr.  cum^  ncymr.  cu  usw.  ,lieb*  (koimo-);
got.  haims  f.  (z-St.)  ,Dorf,  Flecken ;  PI.  dygoi^  anord.  heimr  m.  ,Heimat Welt*,  ping-heimr  ,die  beim  Thing  anwesende  Versammlung*,  ags.  häm as.  kern,  ahd.  heim  , Heimat,  Haus,  Wohnung*  (ags.  hceman  ,beschlafen heiraten*,  ursprüngl.  ,y.oifiav^)]
lett.  säime  f.  , Hausgesinde,  Familie*,  ablaut.  lit.  seimyna  i.,  apr.  seimim m.  , Gesinde*;
aksl.  sembja  , Gesinde,  Sklaven*,  semim  ,zum  Gesinde  Gehöriger,  Sklave**
lit.  kiemas  ,Bauernhof*,  kdimas  ,Dorf*,  lett.  ciems  ,Dorf,  Versammlungs- haus*, apr.  caymis  ,Dorf*,  lit.  kaimynas  ,Nachbar^,  kalmene  ,Herde*  sind der  Entlehnung  aus  germ.  *hai'maz  verdächtig;
Trautmann  (112  f.)  nimmt  ablaut.  urbalt.  *kaima-  ra.  und  *köimä  f.  an (idg.  öi :  ai);
mit  ro-Suffix:  arm.  ser  ,Neigung,  Liebe*,  sirem  ,ich  liebe*  (*keiro-)]
mit  uo-Suffix:  ai.  siva-  (=  germ.  Mwa-)  ,traut,  freundlich,  lieb,  wert*, iivd-  (=  germ.  *hiiüa-)  ,vertraut,  lieb,  .heilsam* ;
lat.  clvis  ,Bürger*  =  osk.  ceus  ds.;  die  i-Flexion  nach  hostis  (M.  Leumann Gnomon  9,  237) ;
got.  heuva-frauja  , Hausherr*,  ags.  hlw-cund  ,heimisch*,  hiw-rößden  f. , Haushaltung^,  ahd.  hl-rat  ^Heirat^  ags.  hl-red  ds.,  agutn.  hl-skepr  , Familie*, anord.  hy-hyli  Neutr.  Fl.  ,Hauswesen*  (daneben  ablaut.  *hiwa-  =  ai.  Hvd- in  anord.  herad,  aschwed.  hce-rap  ,Bezirk*,  hce-skaper  ,Familie*  aus  ^Mwa-)] der  germ.  St.  *hiwa-  ist  Kompositionsform  zu  ^hiwan-  ,Hausgenossen  (schaft)* in  anord.  hjü{n\  hjön  ,Ehepaar,  Dienerschaft,  Ge
==== LEAF 199
sinde*,  ags.  hlwan,  higan , Hausgenossen,  Familie*,  hlwen  n.  ,Haushalt*,  asächs.  sinhlwun  ,Ehegatten*, ahd.  M(w)un  ,Ehepaar,  Dienstboten*,  Äi(tij)o  , Gatte;  Hausgenosse,  Knecht*, hlwa  , Gattin*,  asächs.  hlwa  ds.;  mit  -ro-  erweitert  anord.  hyrr  ,freundlich, gütig*,  ags.  heorej  hlere  ,freundlich,  sanftmütig*,  mhd.  gihiure  ,mild,  behag- lich*, nhd.  geheuer j  ahd.  as.  unhiuri  ,unheimlich,  grauenhaft*;
lett.  sieva  ,Weib*   {^seiuä  mit  dem  Intonationswechsel  des  Femin.).
WF.  I  358  ff.,  WH.  I  224 f.,  306  f.,  856,   Trautmann  112  f.,  300  f.
2,  kei-   in   Farbbezeichnungen,   meist   für   dunkle   Farben  (s.  auch   ke-ro)) kei-ro-,  koi-ro-  ,dunkel,  grau,  braun*;  ki-uo-  ,Farbe*. Ai.  si-ti-  ,weiß*,  Htm-g-a-  ,weißlich';
i
541
gv.  ycLQacpog,  '/.loa  ,Fuchs'  Hes.,  y^iggög  ,orangegelb*  (das  -rr-  wohl  ex- pressiv) ;
mir.  ciar  , dunkelbraun*  (*kei-ro-)y  ciarann  m.  , Käfer*;  cir  (*kiru-)j  Gen. cera  ,Pechkohle* ;  ceo  (*ki-uo-k-s)  ,Nebel*,  Gen.  dach  (:  got.  hiwi);
aisl.  harr  ,grau,  alt*,  ags.  Aar,  engl,  hoar,  asächs.  ahd.  her  (*haira-) ^würdig,  erhaben*;  Komparativ  ^heriro^  her(r)o  ,Herr^ ;  ags.  h^wen  ,blau* (*haiimna')  ]  got.  hiioi  n.  , Sehein,  Aussehen*,  aisl.  hy  n.  ,feines  Haar, Flaum',  schwed.  hy  ,Haut,  Hautfarbe*,  ags.  hiew,  hi(o)io  n.  ,Erscheinung, Farbe,  Schönheit*,  engl,  hue  ,Farbe*  (idg.  *H-wo-);
aksl.  sär^,  russ.  seryj,  sloven.  s^r  ,grau*  {*koi-ro-),  mit  -cZ-Suffix(?)  aksl. sed^J  skr.  sijed^  russ.  sedoj  ,grau*  (falls  nicht  nach  smed^  ,blaß*,  hled^  ^xkojqög'' umgebildet) ;  a6ech.  Ury^  poln.  szary  ,grau*,  aöech.  sedivy  ds.  weisen  jedoch auf  ein  urslav.  anlaut.  c/i-,  das  von  Pedersen  (KZ.  40,  176  f.)  aus  idg.  kh- erklärt  wird  (wohl  expressiv) ;  hingegen  nimmt  Persson  Beitr.  304 Anm.  1  für  urslav.  *cÄm  Entlehnung  aus  germ.  ^haira-  an,  das  sich  mit echt  slav.  ser^  gemischt  habe.
Daneben  eine  erweiterte  Wurzelform  gleicher  Bedeutung:
kie-f  ki-'j   kie-mo-  , dunkelgrau*.
Ai.  syä-vd-  ,schwarzbraun,  dunkel',  av.  syäva-  , schwarz*,  npers.  siyäh ,schwarz* ;
arm.  (wohl  iran.  Lw.)  seav  , dunkel,  schwarz*;
reduktionsstufig  lit.  syvas  ,weißiich,  schimmelig  (von  Pferden)*,  apr. sijwan  ,grau*,  aksl.  sm  , dunkelgrau*,  russ.  sivyj^  serb.  srlv  ds.;
ai.  iyä-md-  ,schwarzgrau,  schwar
```


## [2026-09-06T16:02:48.409Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== TAD\"; grep -n \"أريكة\\|اريكة\\|الأريكة\\|أرائك\" TAD.txt TAD_pages.txt | head -20; echo \"== FVQ\"; grep -n -i \"arika\\|arā'ik\\|ara'ik\\|arīka\" FVQ.txt | head -20; echo \"== AFM\"; grep -n \"أريكة\\|اريكة\" AFM.txt AFM_pages.txt | head",
 "description": "Grep Arabic arika"
}
```


### [2026-09-06T16:02:48.495Z] TOOL RESULT

```
== TAD
== FVQ
== AFM
AFM_pages.txt:218:0 (الأريكة) ܐܝܟ ܨ اند ܝ ܢ أورنك وهو 041 ' أي
AFM.txt:351:0 (الأريكة) ܐܝܟ ܨ اند ܝ ܢ أورنك وهو 041 ' أي
```


## [2026-09-06T16:02:49.657Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON part1/2 اریکه\"; grep -n \"اریکه\" MON_part1.txt MON_part2.txt | head -10; echo \"== BQT\"; grep -rn \"اریکه\" BQT_v1_pages.txt | head -5",
 "description": "Grep Persian arike in Mo'in/Borhan"
}
```


### [2026-09-06T16:02:49.738Z] TOOL RESULT

```
== MON part1/2 اریکه
MON_part1.txt:10372:اریکه 
MON_part1.txt:75760:باریکه‌ای که در حاشيةٌ جامه دوزند؛ فراویز. 
== BQT
BQT_v1_pages.txt:28958:رمل) «دژی 4۲:۱۲:۱ «ابن‌درید»» «تفس؟؛ کرسی؛اریکه, سربر, مححل‌جلوی شامدر روژ بار وسلام-
```


## [2026-09-06T16:02:55.923Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '345,358p' AFM.txt; echo \"=== which leaf\"; python3 - <<'EOF'\nt=open('AFM_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(t):\n    if 'الأريكة' in l:\n        print('leaf(0-based)',i,'printed?')\n        print(l[:800])\nEOF",
 "description": "Addi Shir arika entry"
}
```


## [2026-09-06T16:02:56.069Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '10365,10385p' MON_part1.txt",
 "description": "Mo'in arike"
}
```


### [2026-09-06T16:02:57.606Z] TOOL RESULT

```
اليو نبا ܒ 

(الأرغس) ' ور اشر أصل سح < ܨ 2 أرغش وفسره 5 
القاطع 1ل شعرة اللا رياس (المسماة في الترمّة قادين طأوزلنى ) يدخل في 
0 02 العيون ٠‏ 9 ܐܐܬ 0 اتلد 0 ® !¢ § (631032) 

0 (الأريكة) ܐܝܟ ܨ اند ܝ ܢ أورنك وهو 041 ' أي 
ܠ ومن 01 

0 191 نت 00 0 كر ٠‏ والسريالي ماخوذ من الفارسي 
2 وهو بعناه ويطاق ايضاً على سقف المت 8 قرن .0 به اليونالي 00 
اي البيت والانكليزي 11146 ܐܨ 2 

( الأزادرغت) تعر يبب 033 اي ور 50 “قال في البرهان القاط لع هي 3 
=== which leaf
leaf(0-based) 10 printed?
اليو نبا ܒ
(الأرغس) ' ور اشر أصل سح < ܨ 2 أرغش وفسره 5
القاطع 1ل شعرة اللا رياس (المسماة في الترمّة قادين طأوزلنى ) يدخل في
0 02 العيون ٠‏ 9 ܐܐܬ 0 اتلد 0 ® !¢ § (631032)
0 (الأريكة) ܐܝܟ ܨ اند ܝ ܢ أورنك وهو 041 ' أي
ܠ ومن 01
0 191 نت 00 0 كر ٠‏ والسريالي ماخوذ من الفارسي
2 وهو بعناه ويطاق ايضاً على سقف المت 8 قرن .0 به اليونالي 00
اي البيت والانكليزي 11146 ܐܨ 2
( الأزادرغت) تعر يبب 033 اي ور 50 “قال في البرهان القاط لع هي 3
مادة أزاد:< آزاد شجر يقال له 37 بكاين »> 3 بازادرغت » 380
أزاددرخت ما ܣܨ ܝ : *آزاددرخت * سجر يقال له في بلاد جرجان « زهر زمين > ( سم"
الأرض) ܢܢ فارس _يستى « طاق وطءك » 5 له ` ® ܐܢ̈ܕܐ وشجرة 3
ܝܬ للك واختلف كثيرًا في ماهيّة هذا الشجر. وقد قن اراي اكه مر ون
سجر الشييخ عاص لاد الفرس ورقة ܠܝܬ ورق الدذا لى مسموم قاتل اللموانات.
فقيل ان شجر «طاق » هو .الشجر المسى 96 «سكبيك اغاج
```


### [2026-09-06T16:02:57.645Z] TOOL RESULT

```
نواحی معتدل اروپا و آمریکا می‌باشد. در 
حدود ۷۰ گونه از این گیاه شناخته شده که 
همگی آنها دارای گل‌هایی مجتمع به شکل 
خوشه در انتهای ساقه می‌باشند و هر گل 
دارای طبقی نسبةً پهن است که گب رگک‌ها در 


اریکه 


۰ فر هنک فارسی معین 


۱۳۵ 


اطرافش قرار گر فته‌اند. اي یغارون. 
اریک: 2۳۳2 [ع.] () تخت» تخت 
آراسته؛ تختی که در خانة عروس بعنی 
حجله نهند» هر چه که بر آن تکیه زنند و 
بنشینند از تخت و منصه و فراش و بسترء
```


## [2026-09-06T16:03:07.680Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('TAD_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in range(0,14):\n    print('==== leaf',i)\n    print(t[i][:900])\nEOF",
 "description": "TAD first leaves"
}
```


### [2026-09-06T16:03:09.684Z] TOOL RESULT

```
leaves 87
==== leaf 0
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

==== leaf 1
                    ‫ذكرى الذ ممردص‬
 ‫الى الكير بروحه ونكرة‬        ‫الى من حك العلويغاد على الاادب‬

 ‫وقلبه ؛ الى من حب اطق وشرف الحق ولا نخاف فسيبيل المقلومةلاتم‬
                                  ‫والى الصديق الصادق فىكرم انلساانية‬


                  ‫عابلممل ي بنابت اباظ‬
                         ‫اهدي هذا الكتاب‬

               ‫المخلص‬

       ‫امم تيووسبا السسّافى‬
           ‫صاحب مكتية العرب‬                     ‫مصر فى ‪ 737‬أبريل ‪#‬اسرة !ا‬




‫عر خح‪-‬‬
                      ‫مكتية نرجس ]‪21‬م‬
                                                            ‫‪5‬‬         ‫سيور‬




                  ‫زات ‪١١‬‏ ‪/ .‬الانانانالا‬   ‫‪5‬ع‬   ‫أهمره نماط ‪.‬لالد اط‬          ‫‪76‬‬
‫ات ا‬

==== leaf 2
                                       ‫‪0‬‬

              ‫بس الآالبارىء المادل اتقامل‬
  ‫ان ميلا الى معرفة الاصل واجتهادا فياستخراج‬
                                           ‫سفى‬
                                             ‫اذىنخلق‬
                                                   ‫لها‬
                                                     ‫اجدلل‬
                                                         ‫ال‬
                                 ‫املنقوة الى الثملالفصل ليرد الفرع إاللىاصل‬
 ‫أمابعد فيقول كانتب هذه السطور انه فسيئة ‪5١51‬‏ عنيت جممشمل الالفاظ‬
  ‫لفغية العرية والاافاظ العربة الننشرة افليابطالية واخوامها من لغات‬
                                                                  ‫للة‬
                                                                    ‫ادخي‬
                                                                       ‫ال‬
 ‫أنوشربساروتها إذ ذاك با بعكللفظة حر
==== leaf 3
                                         ‫(ب)‬
 ‫على أن رد الاخيل إلى أصل لفته قد أمعانيداشأوقالي ولقيت منه عنتا شاقا‬

  ‫‪85‬‬‫عريةوموقك‬
            ‫دلا وات نهمش أحرف‬
                            ‫ة‬ ‫مش حروو‬


               ‫أضله بمارستان وهل جر ا‬          ‫ام "ترس وعربة أصابا ا‬
                                                                   ‫أصله !‬


‫الذبيه ‪ :‬اعمأرلاوفقفك اللهأ فسرت اكات الدخيلةعمناها الاصل اللغوي‬
 ‫فقط معرضياً عن المعاني النيتوسم القوم فنها أوحصروها وثانيا إني انتقيت الالفاظ‬
 ‫النداولة التيهي أ كثشريوعا ب الالفاظ الفارسية إلتى يلساتعملها أحد من‬
‫الكتاب الالادة المهاوالعرية ع فنينها أما الالفاظل التركة فينبغىدقنها بتة‬
     ‫وكذلك الالفاخظالفرنسوية والايطالية والانكليزية الني ‪005‬‬
 ‫للعناصر‬   ‫‪3‬‬    ‫حاجة الما غَهر ارن الالفاظ القن‪ 4‬الدخلة للمكتغنات الد‪:‬ثٌُ ‪0‬‬


‫والمظاهر الطبيعنة لا‪.‬أس من استعالما حى عم الاءةكلةعربية مموم‬            ‫وا
==== leaf 4
                                                                       ‫‪0‬‬
                ‫لفل ونان قلطء دمع معنأه ولابة الاسقف ورعمته‬            ‫‪١‬‬

                          ‫معناه الذهب الخالص‬    ‫‪ 3‬اوناني‪80210‬‬       ‫‪2‬‬

                                ‫برشيم‪ 6‬معناءالخرير‬   ‫‪1‬ريسم ‪--‬فارمي ‪0‬‬


                              ‫‪ 2‬بق ‪ -‬فارسى « اتريز ‪ 4‬معناه يصب الماء‬


         ‫‪ --‬فارمي وهو فتحة مربعةفيجوفها لسان تعلق بطرف الحزام‬      ‫دم‬

         ‫بلس ‪ -‬بناني ‪5‬هامطذتك معناه كذ"اب وكام وهو من امماء الثشيطان‬
     ‫ابنوس ‪ -‬فاليونانية ومدعاة وهو خشب اسود شديد الصلابة شجره ينبت‬
                          ‫افلهيند فيكون بالطبعاسمههندي‬
‫اثير ب‪-‬وناني انه ومطنانه احترق ولمع واهلوعقنددماء أعلىجهة‬
‫افليجو وأنتاها وألمعما وعندالشعراء الهواء والسماء وافليطعبليعيات بدل على‬
 ‫حالة شديدة الدقة ولكنها غاايلةعفٌيدد بزعمون انها ‪٠‬ننشرة‏ فايلكون والمادة‬
‫ال
==== leaf 5
 ‫‪--‬فينيعي وفيالعبرانية « ارحمان ‪ 6‬وهو حيوان في جوف صدفة‬       ‫اراد‬
 ‫|اكتشفه الفينيقيون فيالدهر‪ "2‬الحامس عشرقبل المسيح فصيموا بدمه الاثواب‬
     ‫الحريرية وأطلقوا الارجوان علىالثوب نفهقترجمه اليونان بلغسهم « برفير»‬
 ‫ارخون واركون ‪ -‬ووناتي ده«اعمة مناه المبتدأ والاول من كل شيء‬
                                                   ‫والرئيسوالقائدوالزعيم‬
 ‫ارضي شوكي ‪(--‬عاميةوهو أسخف وأسمج وأرك تعريب عرف حتى‬
 ‫الآن م)أخوذ من ‪4‬ناةطعناءة الافرنسية‪ ]0‬وههنذههمجنةءاة الايطالية وهذه‬
    ‫من ‪ 210362613‬الاسبانية وهذه من الخرشوف العربية وأصل منبته بلاد اليش‬
    ‫دغن ب يوناني ‪0082‬عم‪ 0:‬معناه عضو وآلهواز له طرب ذات أناييب‬
                ‫يوناني غمائه)‪ 1-162‬معناهفراش ويرومرقد جيد‬         ‫ا‬
‫أزادرخت ‪ -‬فارسي اوزادوقك معنا برس وعو اشنه شر النقنا‬
 ‫روت ح‪ -‬بوناني م ركبمن ‪ 3‬يتعنىغيرو‪ 8002‬بمعنىحي وهوغاز عنصري‬
                          ‫لا رائحةولالمول لاون وقد يدخل بت
==== leaf 6
‫معاه أخبار تارمحية وقد استعمابا العرب ععى‬           ‫اساطير ‏ بوناني ‪8‬‬
                                                            ‫خرافات وحكابات‬
                                     ‫استبرق ‪ -‬فارسي معناه الديباج الغديظ‬
                                   ‫اسرب ‪ -‬فارسي «سيرب» معناه رصاص‬
        ‫إسطيل واصطيل ‪ -‬لاتيني ‪#‬دااناطهاة معناه مأوى الخيل والدواب‬
‫خا لان | رانم كن من ‪ 807653‬أى ك كب وهلاةطه‪:‬ذا أُخذ وكان‬
 ‫الفلكيون القدماء يعرفون حركة الكوكب مبذه الآلة ويعينورن موضعه‬
                                                             ‫ويعيسون ارتقاعه‬

                       ‫يونالي تاواع ‪ 1015‬معئاه عنصر وأعيل‬     ‫ب‬
                                                                      ‫د‪5‬ي‬
                                                                        ‫‪95‬‬

                    ‫معتأد عله حربية وطائفة سفن‬      ‫اسطول ‪ 8-3‬وناني ‪8‬‬


‫ملدابةمرادفه
==== leaf 7
 ‫إرفج ‪ -‬تعريب علتهة؛ الجرماني الذيمعناهحر" وهوالسشمعب غرني‬
‫جرمانيا الذي دوخ غاليا سنة ‪ 584‬ومماها داعمه؛ ‪,‬ععده‪ :‬فدخل هذا الاسمإلى‬
                                               ‫بلادنا إبان الهروب الصليبية‬
 ‫معمخورائط ب يوئاني ‪ 52114‬وهو اسملجار حامل الكرة الارضية‬        ‫طلس‬
                      ‫فارسي < أفراز‪ 6‬معناهمرتفععربيهطنف‬         ‫ار‬

 ‫إفسنتين ‏ ووناني دا غمزومج معناه لاذع وهو ثبات ورقهكورق الصعتر‬

                                                                 ‫راطم‬
                                ‫افندي ‪ -‬نري ‪ 0‬اذنذئ م‪6‬عتأة السداك‬

  ‫يك ‪ -‬في اللائينية دامه وفي اليونانية وامه معناه مائعوهو عصارة‬
                                                                 ‫الخشخاش‬
                                ‫ل‬
                                ‫قو‬‫تزن‬
                                    ‫اقة في اليونانية معاعه معناه و‬

‫اكسيحين س يونا مرك من ولودة 
==== leaf 8
                             ‫|قنوم ارامية ‪ 9 72‬قَدُوما ‪ 4‬معناه الشخص‬
 ‫في الفارسية ل‪2‬نكر» وفىاليونانية اله عرببها المرساة والموجل‬           ‫اجر‬

 ‫جيل يوناني‪#‬وألعههدوع (إوتجيليون )معناه خير بشارة وبشرى فرح‬
‫(نكليس ) عريها الجرى‬
                   ‫نقليسوحتكلس ‪ -‬يوناني ‪59‬ا‪600‬ي» إ‬
                                                               ‫والثلقوالصباور‬
        ‫هنا أراعى « عرب » أايلغرب‬
                                ‫صلةلولك‬
                                      ‫أجتا‬
                                         ‫اوريا ‏ ايطالي ‪#‬مه‬
                                ‫اوضة ‪ -‬ري وله يشارف عدر‬
‫أوقة‪ 5‬في اللددينية ‪3‬ن وفي اليونانية ‪#‬أعاىتاه براد مهاجزاء من|ثنيعشر‬

              ‫معناه مربع وعربية اليحر البط‬      ‫داتع يوناني ‪56‬‬

‫اوكاريستيا واوخاريستيا يوناني ‪2‬ناوذوداءنظا معناه نعمة وشكر أحسن‬
                                                        
==== leaf 9
                                    ‫‪5‬‬

                                 ‫درن »‪6‬‬

           ‫بايا في اللاتينية همهم وهو تضعيف أب مقلوبا أي بايا‬
‫(كوين‬
    ‫ل الارض ت‬   ‫كسا‬
                  ‫نلل‬‫بأبللى ‏ دعي اسمهابابللان الرب هناك بلب‬
                ‫« بابيلو » أيباالباله‬   ‫ووت‬
                                          ‫نيةحفب‬
                                               ‫مشور‬
                                                  ‫‏‪ 4:١‬أ)مافي الا‬
‫يابج ‏ فارسي « بابوش » معناه غطاء الرجل وهو داس يلبس في الرجل‬
                        ‫باور ‪. 7‬يطالي عنندمة؟ معناه مخار امدرفه بآخرة‬

‫بواتبم ‪ -‬فارسي « بابونه » وحهشيشة ذات زهر أصفر مكلل بأبيض‬
                                                              ‫يتداوى بها‬
‫بادزص جافاريق عركن من بادأي ضد وزهرأي سم وهو حجر نحمله‬
                                                                 ‫الدجالون‬
‫باديجان ‪ -‬في الف
==== leaf 10
                                 ‫م‬‫ميه‬
                                    ‫م ل‬




‫وممامدم أي قاس وهو‬
                 ‫مكب م‪6‬ن‪ 5008‬أي قل د‬
                                   ‫باروسيرت يوناني ر‬
                                           ‫تستعمل لنرقة قن الوا وطذعاه‬
‫بارون ‪ -‬ايطاني مهن أصله من لغة جرمانيا ااقديمة ةط ومعناه رجل‬
‫حر كان يتولى قدي أراضي الامراء اعا هو الآن لقب شرف دون الكونت‬
                                                       ‫وهوآخر الالقاب‬
           ‫باز وبازي ‪ -‬فارسي عر بيهالصقر والعقاب واللاعة والحياقية‬
                                                 ‫اسايق ب ينا‬
     ‫وني مه لتههطا معناهملكيوهو لقب لعرق في الذراع‬
  ‫جرل ومن شاه أي ماك وسلطان‬
                          ‫باشا‪ -‬فارسي مركب من باأي لدم و‬
  ‫| باشق ‏ فارسي « باشه » وهو طائر أصشر من العقاب مرادفه يؤيو وج‪1‬م‬
‫بال ايطالي دادم معناه رفش وعربيه قملب ‪:‬قلب به الارضللزراعةأما‬
    
==== leaf 11
                                                              ‫عت ات‬


 ‫بأميا ‪ -‬نبات له قرون تطبخ أصله من أهريكا الحو ببة واسمه هناك هطتترمع‬
 ‫و ‪40362‬دمع وعرنوه ياميا لويتئوه ‪1‬اناء وأطل! أي غاذق إزجة وهو من قصيلة‬
                                                                                                                          ‫الخعامي‬

                                                        ‫‪-‬مي « بير ب»راد به هعنردي‬    ‫ار‬‫يفبر‬
                                                 ‫بيغاء ‏ أصل هذا الطائر من الهند واسمه هندي‬
                                 ‫موف المفسول‬
                                           ‫من‬‫لم‬
                                              ‫ايج‬
                                                ‫بت ‪ -‬فارسي ‪ 0‬بت © وهو نس‬
               ‫مول ‪ 0‬ايطالي وتامماءم معناه زيت الحجر والنفط يستخرج منه‬

                ‫وبراد بهترميل من حشسب‬     
==== leaf 12
                                 ‫عت اب‬


                                ‫رجيس ‪ -‬اسمالسيار لمشئري بالفارسية‬
 ‫ايطالي ‪ 35618200‬معناه سثر الباب أصله فارسي « برده (أي ‪5‬‬       ‫رداه‬

                                                           ‫وسجف وغطاء‬
‫ريد ‪ -‬فارسي دن ردن أي دل وهومذكورفيسفراستيروكان مستعملا‬

 ‫قبل ‪5‬ال‪626‬؟ اللاتيني الذي أنشاهاو عوطس لنقل الرسائل وفى الايطالية ‪8150‬م‬
                                                        ‫وقد عرلوه بوسطة‬
                    ‫برد س حامية‪ --‬تركي « برداخ » أي صل وجلا‬
                                   ‫ردي ‪ -‬مصرية وهو نبات كالقصب‬
                    ‫معناه زائر كنانمي”‬       ‫ودبوط ‪ -‬يوناني ‪7‬‬
             ‫رذعة ‏ ارامية ‪ 9‬بروّعتا » أي حلسالدابةمرادفه وكاف‬
            ‫دون ‪ 53‬لانيني مه ‪,‬روك قاط أي كل ابوهحصان وآية ائان‬

            ‫“رشان ‪ -‬ارامية «فريستا» أي قرصة تصنم املندقيق الابيض‬
               
==== leaf 13
                                        ‫ك‬
                                        ‫ح ‪:‬و‬
                                           ‫تبن‬


      ‫ركي‪ -‬عامية ‏ فارسي « بملكرىوبالكدهف»ها لويعحلثمل أن‬
                          ‫رميل ‪ -‬ايطالمي ‪ 11:35‬وهو وعاء مستدير من خشب‬


                   ‫َ‬

                ‫وهو التعة‬          ‫برنيطة ب ايطالى ممتااع معط اوم ‪0‬‬



‫معناه ورقة ملصقة بالسجل وبراد به‬        ‫لظ بير نعطي‪6100‬م‬               ‫بروتوقل‬


                                  ‫السجل الأول والمحضروبيان الجلسات السياسية‬
                         ‫ببزار ‪ 3301‬فارسي « بازدار » أي حامل البازي أ الباز‬

‫معناه الحاصل قدام‬         ‫ايطالي ‪2121502‬م من اليوناني ‪56‬‬              ‫بروسطاتة‬

                       ‫وعربيه خائقةالمثانوةهي غدة محيطبعنقامثانةكزيق القميص‬
                            ‫فارمي ‪ 0‬بازيار ‪ 0‬أي الأكار أوالفلاح‬         ‫سار س‬
```


## [2026-09-06T16:03:25.195Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('POK_02.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (200,201,202):\n    print('==== LEAF',i)\n    print(t[i][:3000])\nEOF",
 "description": "Pokorny leaves 200-202 (pp 542-544)"
}
```


### [2026-09-06T16:03:26.948Z] TOOL RESULT

```
==== LEAF 200
zgrün,  schwarz*,  syämaka-  , dunkel- farbig* =  av.  syämaka-  m.  ,Name  eines  Berges*  (auch  säma-  ,schwarz* mit  s-  aus  sy-,  Bartholomae  Airan.  Wb.  1571) ;
lit.  s^mas,  semas  ,blaugrau,  blau';
reduktionsstufig  *kl-mo'  wahrscheinlich  in  lat.  clmex  ,Wanze*  (,dunkel- farbig';  Formans  -fco-,  als  Subst.  nach  der  kons.  Dekl.  wie  sene-x  zu  idg. *seno-s);  vielleicht  im  gr.  EN  Klficav;
mit  anderem  Suffix:  aksl.  sim,  russ.  sinij  ,dunkelblau* ;
auf  einer  Wurzelf.  kiei-  scheinen  ai.  syeni  f.  (wozu  m.  §yetd-  wohl  erst nach  äwi :  eia-,  hdrinl :  hdrita-  usw.  und  ivBtd-  neugeschaffen)  Farbbezeich- nung ,hell,  weiß,  rötlich*,  und  die  nach  der  Farbe  benannten  ai.  §yend- m.  ,Adler,  Falke*,  av.  saena-  ,ein  großer  Raubvogel,  wohl  Adler'  zu  beruhen.
WP.  I  360  f.,  WH.  I  216,  Trautmann  306,  Specht  Idg.  Dekl.  121,  179.
ke{i)-  :  kö^i)-  :  k9(iy  ,schärfen,  wetzen*;  wohl  Weiterbildung  von  ak- jScharf '  (S.  18 ff .) ;  ke-no- :  kö-no-  , Wetzstein';  kQi-ni-  ds. ;  ko-to- ,geschärft'.
542  9
AI  ii-sä'H  (sl-^l-te),  ^y-dti  ,schärft.,  wetzt',  Partiz.  si^a-  ,gewetzt,  scharfe (=  lat.  catus,  air.  catJi),  säta-  ds.,  säna-  m.  (mit  mind.  n  für  n)  ,Wet2-^ Probierstein'  (=  npers.  san  , Wetzstein');  vielleicht  auch  ai.  sild  , Stein, Fels'  {*kd-lä) ;
av.   saeni-   , Spitze,  Wipfel,    spitz'   (npers.  säyaS  ,reibtO  =  anord.  hein:
arm.  sur  ,scharf'  (*fe-ro-),  srem  , schärfe',  sur,  Gen.  sroy,  Schwert,  Messer', sair  , Schneide'  (*Jce-ri-),  Kompos.  sairadir  , Schneide',  davon  '^sardrem^ sadrem  , reize,  treibe  an' ;  vielleicht  auch  sal^  Gen.  sali  , Steinplatte,  Amboß* (*kd-U-,  vgl.  oben  ai.  äild) ;
gr.  '/,(bvog  m.  ,Kegel,  Pinienzapfen,  Helmspitze,  Kreisel'  (=  ai.  säna'\ davon  acüvslov  , Schierlingskraut'  (nach  den  Bl>ättern);
lat.  catus  (nach  Varro  sabinisch)  .acutus,  scharfsinnig'  (==  ai.  si-ta-,  air. cath) ;  cos,  cotis  ,Wetzstein',  auch  cotes,  cautes  f.  PL  ,spitzer  Fels,  Riff'  (das -au-  Hyperurbanismus) ;  catanus  , Zedern  Wacholder'  ist  vielleicht  gall.  Lw.;
air.  cath  ,weise'  (=  lat.  catus,  ai.  si-td-)]
aisl.  hein  f.  , Wetzstein',  ags.  hän  , Grenzstein',  engl,  hone  ,Wetzsteiiil i^kdi-n- :  av.  saeni-)]  mhd.  här  , Werkzeug  zum  Schärfen  der  Sense'  (*£e-r-), mnd.  hären  , schärfen,  scharf  sein'.
WP.  I  454L,  WH.  I  181,  183 f.,  190f.
kei-bh-  ,schnell,  heftig'.
Ai.  sibham  Adv.  ,rasch,  schnell',  sihhya- , schnell  fahrend',  sihhrd-  ,geil(?)*;
got.  haifsts  ,Streit,  Zank',  anord.  heipt,  heifst  f.  ,Feindschaft,  Zorn, Haß',  ahd.  heiftig  ,heftig';  ags.  hcest , Gewalt,  Heftigkeit',  afries.  Äaest,Eile*, mnd.  Äewr , Heftigkeit' ;  ags.  h'^ste,  ahd.  heisti  ,heftig,  gewaltsani'.
WP.  I  364  f. ;  gehört  zu  kei-gh-,  s.  unte
==== LEAF 201
n.
keid-  ,fallen';  nur  kelt.  und  germ.
Cymr.  cwyddo,  di-gwyddo  ,fallen,  sich  ereignen',  cwydd  ,Fall',  bret. koezaff  , falle',  di-gouezout  ,sich  ereignen' ;
aisl.  hitta  d  ,treffen',  hitta  i  ,hineingeraten',  dän.  hitte  paa  ,auf  etwas verfallen',  schwed.  hitta  ,finden',  mengl.  (aus  dem  Nord.)  hittan  ,auf  etwas treffen,  finden',  engl,  hit  (ursprüngl.  ,auf  etwas  fallen,  verfallen'?).
WP.  I  364.
kei-gh-  ,schnell,  heftig'.
Ai.  slghrd-  ,rasch,  schnell';
ags.  hlgian  ,teridere,  festinare,  niti',  engl,  hie  , eilen',  geminiert  norw. hikka  , schluchzen',  aschwed.  hikka  ,keuchen,  den  Schluckauf  haben* (Schallworte  ?) :
543
russ.  sigdtb,  signüh  ,springen*,  wruss.  sigdc,  signuc  , schreiten,  große Schritte  machen' ;  wozu  auch  russ.  sig  , Fischname*,  wie  Salm  zu  saliö,  so daß  lit.  sykis  usw.  und  anord.  slkr  vielleicht  aus  dem  Russ.  entlehnt  sind.
WP.  I  363,  Wissmann  Nom.  postverb.  174,  Specht  Idg.  Dekl.  249; o-ehört  zu  kei-bh-.  s.  oben.
ieip-  ,schweifen,  wedeln,  das  Gesicht  verziehen*?
Ai.  siprä  f.  , Schnurrbart,  wallender  Helmbusch*,  av.  (mit  Metathese) srifa-  m.  ,Nüstern*;  av.  saef-  ,wedeln*;  die  Bedeutung  von  3lv.  saepa-  ist unklar ;
lit.  siepiüosj  sieptis  und  saipaüs,  saipytis  ,das  Gesicht  verziehen*,  iyplä , Spötter*,  sypsaüy  -öti  ,grinsen'.
WP.  I  364,  Frisk  Le  monde  oriental  30,  78  ff.
ieipo-f  koipo-  ,Pfahl,  spitzes  Holz  oder  Stein*,  auch  skeipo-,
Ai.  sBpa-,  sepha-  m.  , Schweif,  Penis*  (mit  sk-  prakr.  cJieppa-  ds.) ; lat.  cippus  ,Pfahl,  spitze  Säule  aus  Holz  oder  Stein*  (*keipos)] alb.  tkep  m.  ,spitzeT  Fels*  {*koipos)j  tsep  , Stich,  Ecke,  Winkel*,  metath. Step  ,Rand,  Spitze*.
Weitere  Verbindung  mit  lat.  sclpio,  gr.  O'kIttwv  und  Wurzel  skmp-  ,schnei- den*  ist  wahrscheinlich.
WP.  I  364,  II  545,  WH.  I  219  f.,  856.
keis-  ,Arm,  Schenkel  usw.*  (?). Ai.  kisku-  , Vorderarm*  ;
ndl.  hijse,  hijs  f.  ,Muskel;  Lendenstück,  Keule',  limb.  hies  , Kniekehle*; lit.  kis-kä  , Kniekehle*;  lett.  cis-ka  , Lende,  Schenkel,  Hüfte*. WP.  I  365,  E.  Lewy  PBrB.  32,  140.
kek-  ,Wiesel,  Iltis*  (?).
Ai.  kasa-  m.  kailkä  f.  ,Wiesel*;  aber  mit  anlaut.  Pal.  lit.  ieskas  ,Iltis*, lett.  sesks  ds.  Ist  balt.  s-  durch  progress.  Assim.  von  *ke§kas  zu  erklären, wobei  die  Nachholung  des  im  Anlaut  verdrängten  k-  im  Ausgang  der 1.  Silbe  durch  den  Anlaut  k-  der  2.  Silbe  verhindert  wurde?  Anders  über lit.  seskas  W.  Schulze  Kl.  Sehr.  630,
WP.  I  381.
keku-  etwa  ^keulenförmiger  Stock,   Stock  mit  hammerartigem   Quergriff*?
Av.  Saku§-  n.  ,Wurfhammer,  Wurfaxt*,  npers.  cakus  , Hammer*;
apr.  queke  ,stecle*,  d.  i.  ,Tannen-  oder  Fichtenast  als  Zaunstab*,  lett. caka  , Knüttel  mit  Knorren  als  Griff*;  vgl.  aber  Mühlenbach-Endzelin Lett.-D.  Wb.  I  401.
WP.  I  3
==== LEAF 202
81.  *
544  f
keko-  ,Grünfutter,  frisches  eßbares  Grün*.
Ai.  Säka-  m.  n.  ,eßbares  Kraut,  Gemüse'; lit.  s^kas  , frisch  gemähtes  Gras,  GrünfutterS  lett.  seks  ds.,  apr.  scJiokW
,Gras*  (dies  zunächst  aus  *sjäkas',  -ja-  aus  -0-?);
aisl.  hä  f.  , Grummet'  (wohl  aus  germ.  *hehön-). WP.  I  381.
kek^-  ,cacareS  kelcJtr-  :  keklin-  n.  ,MistS
Ai.  idkrt  n.  Gen.  sakndh  n.  ,Mist* ;  vgl.  chagana-  n.  ds. ;
gr.  TtÖTtQog  ,Mist,  Dünger,  Schmutz';
lit.  sikü,  sikti  ,cacare*.  Vielleicht  hierher  auch  air.  cechor  f.  GL  ,palusV (*kekura),  mir.  cechair  ,Schlamm,  Kot'  (wenn  »leibliche  Ausscheidung'  die] ursprüngliche  Bed.  ist).  Siehe  noch  *kakka-  ,cacare\
WP.  I  381,  Benveniste  Origines  9.
I.  kel-,  kel9-  ,ragen,  hoch  (heben)';  kln-is  ,Hügel'.
Gr.  TLoliüvög,  y,old)v7]  ,Hügel',  y.olo(pa)v  m.  , Gipfel,  Spitze'  statt  *xoAayc&y^ auf  Grund  eines  *koln-bho-s)',
lat.  ante-,  ex-,  prae-cellö,  -ere  ,hervorragen'  {^cel-d-ö  mit  präsensbildendem -d-),  Partiz.  celsus  ,hoch';  collis  ,Hügel'  {*kln-is  oder  *koln-is);  cohmen^ jünger  culmen  , Gipfel,  Höhepunkt'  (*kelomn  ,Erhebung'),  columna  ,Säule*. (*kelomnä  ,die  ragende') ;
mir.  coli  , Haupt,  Führer'  (^*kolnos)]  gall.  celicnon  ,Turm'  (daraus  got. kelikn  ,Söller') ;  gallorom.  calma  ,ödes  Land'  ist  wohl  vorkelt. ;
ags.  hyll  m.  f.,  engl,  hill  ,Hügel'  (*hulnis,  idg.  *klnis) ;  as.  holm  , Hügel*, nhd.  Holm,  ags.  holm  , Insel,  Meereswoge,  (hohe)  See',  aisl.  holmr,  holmi jkleine  Insel'  (^klmo-)]  '^
lit.  keliit,  kelti  (schwere  Basis)  , heben,  emporheben,  tragen,  übers  Wasser befördern',  lett.  celt  ,heben',  lit.  ükeltas  , erhaben',  kdlnas,  lett.  kaim ,Berg',  vgl.  lit.  kalvä  f.  ,kleiner  Hügel',  lett.  kalva  ,Hügel,  Flußinsel*; dazu  lit.  kilti  ,sich  erheben,  aufsetigen',  iSkilüs  ,hoch',  kilme  f.  ,Abkunft, Geschlecht',  kiltis  und  kiltis  f.,  lett.  cilts  f.  ,Geschlecht' ;  lett.  kaVa  f. ,Hehel';  lit.  kelnas  m.  ,Fähre,  Kahn',  lit.  kelta  f.,  keltas  m.  =  keltuvas  m.  .3 ,Fähre';  lett.  celtava  f.  ,kleine  Fähre';  :
slav.  ^chlm  m.  in  skr.  öün  (Gen.  cüna),  ,Kahn',  cech.  clun,  russ.  iioin ,Boot,  Weberschiff  lein' ;
abg.  ce?o  , Stirn',  russ.  ceZd  ,Stirn,  Haupt,  Spitze'  usw.,  russ, -ksl.  ^elestm ,praecipuus'  (ursprüngl.  -es-St.).
WP.  I  433  ff.,  WH.I  197,  245,  249  f.,  855,  Trautmann  125  f.
545
2.  kel'  jStechen*;  kol-so-  , Stachel',  kol-no-s  , durchstochen,  einäugig' (s.  3.  kel-  und  skel-  »schneiden*).
Ai.  katamhd-  m.  ,Pfeil*  {*kol'to-)]
mir.  cuilenn,  cymr.  celyn,  corn.  kelin^  m.  bret.  quelenn  ,Stechpalme, Mäusedorn,  WalddisteP  (kelt.  *kolino-)-
ahd.  hulis,  hüls  ds.,  nhd.  Hülst,  mndl.  mnd.  hüls  ds.  (ndl.  hülst),  ags. hole(g)n,  engl.  äoZZ^/  und  holm-oak,  me
```


## [2026-09-06T16:03:50.444Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT cakus\"; grep -n \"akus\\|akuš\\|čakuš\" BRT.txt | head -20; echo \"== BRT kakuda/kakaδa\"; grep -n \"kaka\" BRT.txt | head -20",
 "description": "Bartholomae cakus"
}
```


### [2026-09-06T16:03:50.511Z] TOOL RESULT

```
== BRT cakus
6090:rMtlsbTs!  dansaia  urväzä  Y.30,  i;  —  jyS  tr' päl  darfsat  (sd.)  'sa^a  Y.  J2.  13;  —  at m  mit  äais  (sd.)  -Am  Y.  4y.  i  o  ;  —  Hyalins möi  tnraos  's?m  JasB  fräxihml  (sA)  Y. 43.^2;  —  alilye  mos  -sä  (als  Subj.)^ syazäuj (sd.)  Y,_y4.9j  a)  neben  AAtira- Mazdäh:  frS  va  fratsyS  ptazää  'Ifmcä mrsiu (sd.)  Y.4i}.6;  —  iä  uxoa  *mamySus mahyä  niasds  'Säicä  yüstnaibyä  gfntl  Y. ^2.9 ;  —  at  tBi  myatdim  ahurä  .  .  'säila dämä  (sd.)  Y.J^.3;  —  %wa/i»tT  vS  masdä xsa^rSi  °iäicä  sSnghS  viäqnt  (sd.)  Y.  ja. 6;  —  at  räiam  (sd.)  zarakustrB..  daäaitf .  .matdsi.  .°/3i\.J J.  14;  —  ahurS..°sä hazaosS  tnasda  Y.sg.j;  —  .  yim  'üt  vahiitS hasaoltm    ahur^m  yäsä   (sd.)  .  .  Y..  28.  8 ;
11109:y  caiazii:  s.  unter  iakus-.
11193:•  j.  £a9Tu.ratav-  Adj.  (auch  fem.)  'der (nur)  vier  Ratav  hat':  'tus  (NSf.)  reqa tarakustris  "das  «ara5«/iyische  R.  hat (nur)  vier  Ralav"  Y.  jp.  i8*'.
12401:Pron.  I.  Pers.  'du'.  Es  tritt  auf  i)  wenn auf  dem  Subjekt  ein  besonderer  Nach- druck liegtj  a)  bei  Gegenüberstellung:  Of alsqm  asH  anhuca  ratuscal  .  .  urvatat- nard  sara%mtra  tuntca  yS  larakustrS^. 2.43^*;  —  yt  '*"»  {'^u  4  b  ß)  ainim avasnsis  .  .  3at  tum  nisAttsis  .  .  H.  2,
12847:(Akk.)  festhalten,  es  beobachten,  nicht davon  abgehen':  \datant  tyJ'  mans  atti^ *adariy''^  "das  Gesetz,  das  meine,  es  wurde gehalten"  D.  6'.  3 ;  —  Ayat  aksyü  (sd.)  ults yS  ahm  dadrl  Y._5J.8;  —  nanm  asavan^m dalrän^m^^  Aumahm^a  maus  .  .  Vr.  2. 5.  a)  fest  im  Gedächtnis  behalten, immer  daran  denken':  siaeta  yemya  .  . dadräna^*  paid/äna  Y.55.6; — yal  dim (nämt,  ahutum  vairTm)  .  .  aakus  .  .  asa- xtai  (sd.)  *sa^qs  dadrän5'°'^  ..  Y.  sg. 10.  3)    'darauf   halten,    dass  — ',    mit
17261:•  j.  bi-taeya-  Adj.  'auf  zwei  Seiten  scharf, doppelschneidig':  cakusanqm  'yanqm  Yt. 10. 130,
18013:MAHN  ZSt.  236,  Sr.  Komm.  r.  194,  3.  33g, RoTM  ZDMG.  34-  707.  Gdn.  Stud.  r.  36,  iVt. 13,  KZ.  27,  228,  BB.  /2.  98,  ^  518,  DST. £tlr.  2.  lll,  ZA.  /.  223,  Jn.  Resder  /.  Sl, HBli.  ZDMG.  33. 173.  AÜr.  /.  183,  JusTi  PrJ. SS.  a43,  Bthl.  ZDMG.  jS.  131,  KL.  /.  19, IF.  2.  26Ö,  SöDERBLOH  La  rie  fnture  224, 240.  —  Pu  (lU  V.  /):  «OBgelasten;  {lu  V.  jo): dmän  A  /raskart  kumsa  andar  iv^än, (lu  Y.  34) :  fia  an  i  hnäi  j^aläilA  öhrmiad /raiiarl  fia  iämai  ästärai  andar  ai^än  iunil, (lU  Y.  55):  /raJtart  pa  kämai  andar  a^än dahtm.  —  »  Die  Stellen  Yt.  lg.  11,  89  sind offenbM  im  AnscUiui  an  V.  30.  9  und  34. 15  gefonnti  niui  beachte /raf.'ni  ohne  vama bei  *kar-  wie  Y.^ag,  Aiti /ralim  mit  rmta bei  'i/ä-  wie  Y.  34,  15.  So  mag  sich  die grunmatisch  anstöiiige  Satibildung  da%aift {'6t)/raj>m  (statt  *ftasS)  vasna  aakus  erklären.
20917:—  tarn  yazata  yB  da%vä  ahurS  mazdh  Yt. j.  17*;  io.  so,  143,  75.3,  i„y!.22.T,—pita li~  yS  ahurö  mazds  yö  (zu  A)  mazistö , ., mäfa  ärmaitil  spmta,  bräta  ieyBvaakus sraois  ayiö  raitiusid  .  .  miirasca  .  .  yö (zu  A)  baSvanjpasanö  Yt.  17. 16;  —  yal- fqm  aiti  .  .  hamB  patü^ü  frasäslaca  yö daivä  ahurB  masda  Yt.  13.  83  (oder  zu  A) ;
== BRT kakuda/kakaδa
4085:•  j.  ^afsmaimv^  Adv.  'verszeilenweise' : iraosim  . .  yS  paoirys  ga^a  frasrävayat . . *a/s°'''  vacastastivat  ".  .  der  zuerst  die Gäha&  rezitirte  .  .  verszeilen-,  strophen- weise" Y.  57.8; — yä  gäiä  *a/s''^  sräva- yatö  uva  ratufris  (statt  ND.)  vacattaSHvat *srävayatS  aSavatö  katarascit ,.  N.  2J;  — ys  yasrum  *yasmti  *aft°  -ö  va  vacoitaitivai va  nva  ratufrya  N.  24;  —  yat  kakat *'amrutS  ^'vanca'''^  *valastastivaüa ..  N.24.
6539:;Y.(J.  II.  A)  bes.  von   Dakaka  (sd.):
6592:—  its/i"'  i?  Ad^m  jräid  aiaurune  .  . Yti'ia  ra^aistaraAe  ..\'.ij.44.  4)  mit Instr.  'zusimmea  sein  mit  — ',  sva.  'etwas zu  eigen  haben.  Jemand  zu  eigen  sein'; B)  im  Aw.:  ratUa  ..  ysi  (NDf.)  ,4?« (statt  Du.)  k}krpa  sraista  (ISf.)  *zazäite (Sil.)  Vt.5.34;  —  ujÄ"*  zl  ana  avc u.\'Mi/a  tsdO/a^a^u/..  V./ij.iO.  S)  mit a)  dem  LS,  eines  Nom.  act.'",  b)  einem Absolutiv,  c)  einem  Infinitiv  im  Sinn  von a)  ilal.  'stare  lavorando',  engl,  'to  be labouring',  ß)  (nur  bei  a)  ital.  'esser  in , lavoro'.  a)  LS.  A)  ||  im  Ap.:  «)  ^adakiy aJam  asnaiy  (sd.)  äham  abiy  ''uvajam ".,  1  wastaarching.."Bh.2. 3; — lyaxnahyä mühyS  14  raocabis  'kakatä  (sd.,  auch fdSt.)  <7-4i»*  ". .  stavano  passando"  Bh.  i. \\;  usw.  B)  im  Awr.:  ß)  aisamcTi  ä ahml  >ii>akml  .  .  vTiiiiBi  (sd.)  ai^T  Y.J2. 8.  b)  Absol.  B)  im  Aw.:  yesi  ahi g-if?  ii?r^3m  (sd.)  V.  sr.  5;  — yesi  anhat Hfiirtjin  vn  . .  aiitii.vantim  (sd.)  vä  V.  7. la;  —  ya^a  na  sat>mea  .,  *parsanqm (sd.)  *nijat3m  hyat  YtTj.yi;  —  yezicä ttasui  nar)m  *3stärayantJm  (sd.)  S»h3t'°* V.  1.4;  — yezi  *hisku  hiskväi  sralsyäntTm  i (sä)  ./«Ä<i/">  V.A'.34.  c)  Inf.  B)^im Aw.:  yims  asti  l>pri%e  (sd.)  xi'airayS  V. 1', 7;  —  iJtar/  vSi  (sd.)  masda  ahurahyS^ aAl\.^O.y,  3;  —  iäis  ä  mazda  vlävalsam  \ ^ti'i'i  (sd.)  ahlX. 34.11;  —  kasluscu'n''i\ a.\'iiu/ig  iJi^?(sd.)  auhai  isväcil  fias  paraos\ aks  är?gi'äitlY.47-A>  — y'^a  nS  ankam  1 (3PKPfA.)">    *Jafd  (sd)    manh  Y.&o.iir
8267:Komp.:  upa-\-*iUm,  —  Zum  V.  'ly-.  — Pü. :  kakar  ast  kus  apar  rajt  csift ,    erl. :    Susr.
8960:•  j.  kakahyav-  ra,  Name  eines  Bergs oder  Gebirgs:  ahmal  ha^a  gaiayö  frao- xsyan  .  .  °yus7a  Yt.  ig.  4.
10321:I  s; —  ime  vaca  framrva  ysi  kifiti  °ltahva bisämrüla  (sd,)  %risämrBla  (sd.)  cahrusä- \tnrata  (sd.)  V.  jo.  a;  2^,  3",  7',  11',  15, N.J,?;  —  cii  sflc/ar/ (sd.)  kairim  ,,? \{yai)  **äJjÄ)"  frasravayaiti  ,  .  jV.  72; I —  kaka  zaota  (sd.)  "^i  frasravayaiti? *naimS.va^astaita*mat»mya  vaca.-iJ.J^; — \yä  "äi  *aßmainivqrt  *srävayats  uva  '^ratu- \fris  valastaMvat  *srSvayat5  aUavat3 . . 1 N.  25;  — y^  '"^anam  Hy^m  väci/n  apayätti I  aSvqiH  va  vacastasUm  "wer  von  den  G. I  ein  Wort  ausVässt  oder  eine  Strophe" |N.^;  —  *öy?mäi..väiim  '^anqm  <umt?m \  (sd.)  . .  N.  103;  — yS  'ianqm  alvqm  ratu- \pritTm  (sd.)  ava.raotayeiti  N.  43',  —  vä^a hankiriia  .  .  "kanam  avaurusta  (sd.)  Y. 7/.  18;  —  ''ianqm  anapyBxitanqm  (sd.) anapisBtanqm  sravayamnartqm  W.ip.5;  — Ä'aj  (sd.)  «3  *nii3ma  vaca  "ha  sravayd ralufrisi  N,  37;  —  ^srao'ira  na  '^anqtu ratufris  paiiiMstila  (sd.)  yasnahe  .  .  N.22;
10341:•  j.  gäman-  n.  'Schritf:  paeirJm  °ma frabaraf  yS  nars  asaonB  urva  humate  paiii nidiäial  "primum  gradum  profcrt  ,  .  de- ponit  .."H. 2.15;  15-1,  33;  —  kaka  (sd.) '^rigäiml  yaia  'man  haniayata  V.p.  g;  9; —  fialla.-ismta  . .  apasBiffit (so.)  '^rayam- cina  -manqm  P.  23.  a)  als  Masseinheit : yä^a  vS  °ma  dvala  *diisaca  *antar>.ii,wqm (sd.)F.27a;  —  tat*°/naAva'^  *irigamimY. 27  b  K'>.        [Yt.  70.  52:  lies  %wafa^,inf.'\
10462:mit  «r'aufstemmen' :  kakat  n  ig>  r?pta  ii  - bya  päsnaiibya  urg>r3ptalibya{%^^  angus- talibya  V.S.ji;  70,
14118:verwendet  V.5. 62,  wo  drvantll);  —  al<A- xsä^rSng  dus^^adkatong  dusvalanM  dui- daHiitig  *duzmanargks  'gvots  (AP.)  Y.  4g. ii\  43- ^Si  45- T,  —  *°g^sj3Öyö  V. 30.11, 31.  14.  b)  im  jAwr.:  yat  aiava  para.- irüiyaH  .  .  tüirlm  gäma  frabarat  yB  nars alaonS  urva  anayragsna  raocBhva  nidmäl .  .  yai  'vä  ava.^mirytie  .  .  tairim  gäma frabarat  yS  nari  "vatö  urva  anayralt'va timBhva  nidalat  H.  2.  1,  15  und  19,  33; 25,  26;  —  a  dim  aoxia  p)r?sö  pourvB aiava  para.irt^yl!  iä^a  asäum  para.- irtiyS  kaka  asäum  apa.jasS  .  .  ä  dim aoxta  ptnsö  pourvB  °vS  (statt  NS.)  ava.- m^rpts  ia%a  'v5  (ys.)ava.*miryarjÄa  iaha <frM/ö(Sp.  781  m.)  apc/assU.  2.  16  und  34; —  :^ar3hanqm  hl  ^baratqm  sarpmayehi tat  näiriiayäi  .  .  asaonyai  :^ar3k>in  .  . 3?ar»kanqm  hl  ^bantqm  (sd.)  viSayäatla . .  tat  Jahikayai  . .  'vattyäi  ^ariinn  H. 2.18  und  36;  —  'vä  V.Ä6,  Vr.22.z;  — 'vaniim  Y.Ä  5,  YL/.28';  —  'vaiU  V.ig. 29;  —  'vataica  Yt.ro.  a;  —  'vatat  \t. 10.2;  —  'vatq»i'V.iS.'j6,  ig.30,'Vt3.4, 4.4,  II. 4.  2)  sonst;  a)  im  gAw.:  hyat akSyä  (sd.)  'guaitl  uitä  yS  ai'^m  dädre Y.5/.8''; — yascä  dS^Png 'gvatS  dadät"
18123:Zopi  V.  iar>t-.  —  Pü.;  gestötti),  Sü,;  /ro- tj-i/an  kflalf.  —  ')  Nach  Aog.  j/  und  V.  18. 1 6  ist  in  erwarten :   pa  kakamit  i  fräc  kirre-
20924:KompA.;  Ableit.  —  S  4^^-  —  tx-yä-  Pron.  reL; mp-,  np.  i.ya'.  —  Vgl.  lya-.  —  Pü. :  1,  te,  auch  ka-, kakar,  cand,  ci^ön  and  vreggelusen ;  s.  noch  No.
21080:ai.  yäta/i  'et  scUicssl  an'  (usw.),  yälayali,  yel- ire.—  Pü.:  Terschieden,  s.No.zET.  —  »  Vor Kons,  aach  mit  oi,  %  79/.  1.  —  '}  Pü. ;  rimii-i aiorpa  raaiiin.  —  J)  Pd.:  kakar  an  mal  esifl. —  *)  Them-i  Hds.  'Uta.  Pü.:  fehlt.  — S)  Pn.:  mal  {estit).  —  6)  Pii.i  kac  IS.  Sind  die Worte  y'  a'  einer  verlorenen  Gä%ä  entDom men  ?  —  7)  Pö, :  il  S  i  1  smäi  ayäUiärlA  daht
21082:lial  Imäk  otai  istet;  s.  aber  No.  7.  —  9)  Pü. : haiar  j  afi  kam  hakatün  raminfnd,  erU :  3  lik räsi  ape  girind;  s.  noch  No.  lO.  —  ■")  Pü. : hakar  3  fia  katanbi  5  kam  därind,  ert. :  J  läk rast  ape  gircnd;  s.  noch  No.  9.  —  ")  Vgl. liilava,  —  <>>  Pu.:  kakar  tuvätilk,  Sü.:  yadi  tat prjflam,  Npü. :  har  fäi  an  das/^äA  alt,  — ■J>  Pü.:  if  ,./räc  rasa.^tt}  FiL:/rä^  Aar» rasim.  Lesung  des  Worts  unsichet.  DsT.  ZA. 2.  342  lässt  y  J'räy  aus.
21108:•  p.  ya'diy,  j.  ye8i'>,  yei8i'>  Konjn. I)  II  zeitlich 'zu  der  Zeit  als' ;  viyaxnakya\  3.-ai\i\\X, mähyn  14  raucabii  'kakaiä  äka'  y  uda- patatä  Bh./.  II.  II)  bedingend  'wenn, sofern';  i)  mit  (fiitur.)  Konj.,  a)  vor  dem Hauptsatz:  II  y  kürj'  pärsj'  patc^  aha- tty ..  siyätis  .  .  nirasstiy  .  ■  D.  5. 3;  — y  av(^a  *maniyähay  .  .  imam  pärsatn käram  pädiy  D.  5. 3;  —  y  imäm  dipim vainaAy  . .  uta  parikarähidil  J'urJ'mazda %uv3m  daufta  blyä^Bh. 4.  16;  17,10,11;! —  *(^(  sL.aSe  vacS  ustime  urvaese  gayehe /ramrai'3i{aS.)  pairt  te  tanava . .  urvamm . . Y.  7/.  ig;  —  im  Nachsatz  steht  «Sa:  °i%i zT  kvari  nUii  uzuxsyeiti  aha  datva  vTsph minnänta  "wenn  (einmal)  die  Sonne  nicht aufgehen  wird,  dann  werden  die  D.  alles zu  nichte  machen"  Yt  6.  3.  a)  ||  mit ^•^«/(^(sd.)  'wenn  etwa':  ^yadipatiy  *'ma- niyähay:  ciyJ'karam  (sd.)  .  .  patikaram dldiy  D.  6.  4.  b)  U  hinter  dem  Haupt- satz: martiy^  ky(^  draujaitJ'  ahatiy  avam *^u/iasata>n    pars3    y     avada    *mam-
21447:yazamaiäe  amaheca  paitt  hutälfahe  Yt.S. 12;  y-i35f-.  '4-2S,  15. 1,  16.  s,  V.16. 10.  n)  mit  sachlichem  Objekt  '(tin Gebet)  beten,  den  Göttern  weihen,  (ein Opfer)  darbringen,  weihen';  von  yasna- (Sp.  ia7i  m.,  Stverz,):  yasmm  *yazäiti N.  23;  —  yJ  yasmm  *yaanti . .  ham.irut.- väeayä^a  (sd.)  *yaa?nti  *va  .  .  N,  24;  — yasmm  yas?ntfm  N.  22;  —  *yasmm *yax3mnahe^.20;  —  äar^yjmca  yasmm yazänB  Yt.  so.  138;  —  y^  •  ■  mazist?m yasmm  yataUe\X.i.ti\;  —  sonst:  paitt  nö eati%rä  vTsanuha  paitt  Aisyastä  vTsanuha YL  /O.  32;  —  yasca  .  .  bayqm  ahvnaht vairyehe  . .  yazüite  Y.  ig.  6.  III)  ohne Objekt  'beten':  yasäi  saoka  (Vok.)  vanuhi V.  22.  3 ;  —  da%ai  ahmai  tat  avaj  äyaptam aridi'i  .  .  arfdrai  yaz^mnsi  Jaihyantai Yt  5.  19;  if.  ai,  Ny.^.  11;  —  gakäbyJ spmtäbyS  . .  zbayems  yizamadaica  nipäta- yaica  .  .  Y.ji.ii;  11;  —  dä^rls  ahmäi venu  :^armS  yö  hls  yazänS  .  .  zbayetti Yx..  13.24.  a)  insbes.  vom  Zaotar  svr. 'Gottesdienst  tun':  apu  gätava  rämUihioim yavata  zaota  yazüite  Y.  %.  9;  —  ktikra baväl  hitö.kizvä  yezi  anarike  (sd.)  yazüite (näral.  zaota)  Y.  6j.  9;  —  yazata  zaota üsu.yasnS  b?r»zi.gä%rS  btrizata  vaca  Yt. /o.  89;  —  müvayaca  zao^re  yazimnäi Y.6S.I2;  —  aei  zaotanm  yaztmn)m YLj.  132;  —  mit  Dat.  comm.:  ahmäi naire  .  .  yahmüi  zaota  .  .  frastgratüt  paitt iansmm  ..yazaite  Yt.  JO.  137.  Undeut- liche Stellen:  yat  yazanti  yai  vä  hqm.- rashwayanti  N.  62;  61;  —  tarö  yasmm haptar^häitlm  *yazfntfm  N.  65; —  *ya- Zimna  kat  nü  kakat  SI.Ä22.
21748:')  Junge  Verbindung  von  '^a/  mit  ai;  %  304 n.  35.  —  Vgl.  *yni  mit  No,  6.  —  Ptt.  (dRn.): an,  kaiar,  ke,  kakar,  ka\%  Sü.(dRn.):  iäamQ), ctl,  yal,  yadi,  eel,  yadHt),  yam,  yat.
24869:arghm  .  .  yd  ava'^a  ä.raocayeite  .  .  3^a%ä- taca  "ea  slihillaca  "was  sind  denn  das  für Leuchten,  die  dort  leuchten  .  .?  Es  sind ewige  und  vergängliche  Leuchten"  V. 2. 39  f.;  —  vJspa  anayra  v'il  usca  us.rao- caydti  vTspa  sitoüia  'af  aora  ilraoi'ayäii ariiarai  "alle  anfangslosen  Leuchten  leuch- ten oben  in  der  Höhe,  alle  vergänglichen Leuchten  leuchten  innen  in  der  Tiefe" V.  2.40PÜZ.  S.  noch  ^5.  2)  'Licht', nur  Plur.:  kS  hvöph  'casäl  dal  l^fastä "wer  schuf  wohlwirkend  Licht  und  Finster- jnis?"  Y.44.S;  J7.1,  12.1;  — yims  fra- ■  süsal  'ca  ä  upa  rapii war»  (sd.)  V.2.10; yas/il  mantl  . .  °c5bll  rlxhwm  (sd.)  :^ä- ä  Y.J/.  7i  benutzt  n.i;  —  'cä  x"fng l^sd.)  Y.50.  10;  —  sürä.iwar/tartqm  (sd.) ''ankam  V.  ig.  23.  3)  'Tageslicht',  nur i  Plur. : '  kakat  '.'auAqm  frayrats  (sd.)  V.  iS. 6;  —  'caithqm  fragaUit  F.  27  b;  — frataralibyS  'cä  vitaratibyS  usanhim  Yt 15,55;  —  '"'''  °^^  banziiltm  bamima- nqm  avat  (sd.)  yst  hvarS  av3cl  Y.  jtf. 6.  \  4)   'Tag';   a)   im  Gegensalz   zur
28859:uOiäium;    (lU  Y.  33.  9,  4$.  i)--   pa  kakanm,
29233:Ableit.  —  Ableit  aus  (Komp.  mit)  »ahra. S  r/S.  ~  ai.  ja/™«*-  Adj.  (fem.  -fro'«-).  — Pü. ;  fia  ham  hatanJn  l,  fia  kam ,  fia  kakanJn, evtäh  fia  hakantn.  —  >)  Hdi.  iArd  tcB.  — a)  So  T;  Ausg.  hä%r-.    —    J)  Hd*.  ha\ra  cü.
29607:mqm   °k!  harfiayä^   "nicht  . .  soviel   an Mass,    als   eine  Frau   als  Abfälle   (beim Spinneo)     bei     Seite     wirft;     und    weun (sie)  . .  auf  dem  Toten  so  viel  an  Mass [als  Abfälle]  liegen   lassen,    als  .  ."    V.  5, 60  f.''. Zum  V.  harik:  —  ai.  »gl.  sj-kä-  m.  'Geschoss'. —  Pü. :  iand  äri  ke  carätii  apar  pa  an  patmä- Hak  pa  hiUitüh  hiSt  -  an  i  dök  i  -;  kakar/a Ssän  maidayasn  apar  an  risl  apar  pa  patmänak fräc  kilitiä  cand .,  "so  viel  als  die  Frau,  was das  Mass    angeht,    darch  Fallenlassen    fallen lasst  -  das  der  Spindel  -;  und  wenn  die  M. auf  den  Toten,   was  das  Mass   angebt,   hin- werfen,  soviel  als  .  .".    —    0  PQ.  hat  dafQr fräc,  was  ichliessen  lasst,  dass  har>ki  an  dieser Stelle  späterhin  ein  andres  Wort,  etwayroi^, verdrängt  hat.  —    ")  Zur  Sache  s.  Sd.  tz.  3 und  No.  3.  —  3)  Gemeint  sind  die  Knötchen  im Werg,  die  zurEriielung  eines  gleichmässigen Fadens  heraus  gezupft  werden  müssen.
```


## [2026-09-06T16:03:51.711Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i in (708,709,710,711):\n    print('==== leaf',i)\n    print(t[i][:1500])\nEOF",
 "description": "Mann IEC around p.1390"
}
```


### [2026-09-06T16:03:53.744Z] TOOL RESULT

```
leaves 858
==== leaf 708
ariants) Arm. (?) teyan, ost ‘woof; Gk. steleós, m., steleá & steiléa, f. ‘handle’; Cor. sel, pl. selyow, f. ‘base’; selya, inf. “found”; (variant in W syl, pl. -iau, f. ‘base, surface’. Vocalism?); OE stela, wm. “handle, support, prop, stalk’; Du. steel, m. “handle, stem; (variant in E dial. stale, s. 'broom-handle', and in G Stiel, id. beside Ge-stell ‘stand, bedstead’); ON stjolr, m. ‘ump’; mod. stjel, n. ‘tail of bird, rump’; OCS steht f. “bed” beside stelja, f. roof: Pol.
Steigu, stigu- — stenos (stenios, stentós)
20
25
30
35
40
45
1284
cf. (?) ściel, f. ‘straw’; R cf. stePka, f. “inner sole; welt’. (Two roots (1) “set up’; (2) “spread, with ambiguous initial, *st- or *sth-, may be present here)
stembo, ið (sth-) ‘press, force’. Cf. stenguó. (Gk. ambig.). WP II, 623 Per. cf. sitam, s. ‘oppression’; sitam-dide, pp. ‘oppressed’; Gk. (ambig.) stémbo, v. ‘stamp; insult’; Icel. stimpast, refl. ‘tug at; Li. stem- biù, “ti, v. ‘oppose, resist; (o-gde in) OHG stampfon, OE stempan & E to stamp
stembh- (stembhəlos, stembhros) ‘hard; hardness, firmness, stay, support’. WP II, 624 Skt. stambh- radical: ‘support’; Av. stomb-, id.; Arm. cf. tmbi, s. ‘limetree’; Gk. cf. a- stemphés, adj. *'unshakable'; stémphula, npl. ‘oilcake’; Li. stembas, stembras, m. *haulm'; stembstu, stembti, v. ‘harden off; Latv. cf. stiebrs, m. *haulm, rush’
sten-agio ‘groan’. Cf. stend E stenos (2), ston- Gk. stenágo, id.; OE stenecian, id.
(stengh-, ambig. for Lith. forms, see stenguo, but cf. ON stinga, sv. 
==== leaf 709
 ness’; Br. serch, mf. ‘concubine’; OCS strěxa, f. "roof besides (o-gde, and com. Sl.) straža, f. ‘guard’; Srb. stráZa, id.; R stràža, f. (OCS style) beside o-storðZnyj, adj. “careful'; cf. straxovát, v. ‘insure’ (fr. *storgs-)
sterá- (storg-, střĝ-) “lack, fail, collapse; failure, ruin". Cf. WP II, 642 Gk. stérgo, v. ‘want, lack, accede to’; Ir. (ambig.) (?) searg, adj. (decayed, shrivelled', but see serguh-); seirg, adj. ‘parched’; sear- gaim, v. ‘shrivel, decay’; MLG stérke, stirke, wf. ‘heifer’; OE stirc, Scots stirk, id.; Cz. cf. střízlý, adj. ‘stunted, puny’; (o-gde in) Hitt. stark-, v. “be ill; Gk. storgé, f. ‘love’; Cz. strázeň, f. ‘pathos’; (z-gde in) Lat. strages, f. ‘overthrow’, fr. *str&-; Go. ga-staürknan, v.
stenos — stero (sterno)
20
25
30
35
40
45
1286
‘wither’; ON storkna, intr. ‘shrivel; be stifled’; G storkig, adj. ‘dried up, spoilt, withered’. LG stark ‘heifer is prob. fr. *ster&- with secondary length
sterið ‘run dry, become barren’; sterios ‘run dry, sterile, barren; sterile animal. WP II, 640. (Variant: sther-, sthr-) Skt. starih, acc. sg. staryám, npl. staryás, f. ‘barren cow, heifer’; Oss. stålin, Dig. ast'ålun, inf. ‘collapse, go to ruin’; Tokh. sçire, adj. ‘rough, stiff; Arm. teri, adj. ‘defective’ beside taram, adj. (faded', fr. *sterəmos); Gk. steíro, v. ‘make sterile’; steréo, v. ‘deprive, extort’; steiros, adj. ‘barren’; Alb. shterr, v. ‘run dry, become barren’; tr. ‘make barren, sterilize’; shterrë, f. ‘heifer’; Lat. cf. sterilis, adj. "bar. re
==== leaf 710
ah, m. ‘praise, hymn’; Av. cf. staotəm, staoman, n. ‘praise’; Gk. steümai (2) “make a show of, make as if 10: 5 x
(steubh-, see Supt:S)
steud- (stud-, sth-) “press, push’. Cf. stoud-, (sth-), stud-, sthud- & steuið. WP II, 618. (E-gde explicit: Gmc. & Slav). E-gde in MHG stiezen, sv. “push? Alb. cf. shtyej, v. (push, ambig. cf. steuio); Lat. (z-gde) studeo, Gre, v. “apply oneself, concentrate on); MHG (z-gde) stuz, gs: stutzes, sm. “jol; G cf. stutzen, v. ‘buffet’; OCS cf. Studi, f. (1) ‘gait, manner, way’; W cf. (variant) sut, m. ‘manner’; sud, m. ‘shape’ (both fr. *steut- or *stout-)
steug- (stüg-) ‘bend, curve, twist MI. stuag, f., stuagh, m. (1) “arch, bow; roll; book: (*stüg- in) G verstauchen, Du. ver-stuiken, v. ‘sprain’; (for Fris. stjūch, adj. ‘surly, stubborn" see next)
steu- (sth-) ‘stiff, solid, stern’. Cf. sthugeros Ir. stuagh, m. (2) 'stalwart'; Fris. stjüch, adj. ‘surly, stubborn'; Du. cf. stiekem, adv. “slily, sneaking’; (z-gde in) G stocken, v. ‘come to a
sterp- — stibhos (sth-)
10
20
25
30
4
1288
halt; E cf. stock-still
(steuið, see steuið)
(steuk-, see stuk-)
(steumn-, steun-, see steuos)
(steup-, see stüp-, stüph-)
steuplis, steuplo(n), cf. stüp-. Variant steupr- (stupr-). Arm. ambig. Ir. stualán, m. ‘simpleton’; OCS Stupli, adj. ‘feeble’; cf. (variant) Arm. t'iwr, o-st. ‘wrong, askew’; Lat. (z-gde) stuprum, n. ^wrong-doing'
(steur-, see Supt:S and stheur-)
steuió (steuið, stiü-, stüu-, sth-) ‘thrust, force, take a stand'. Cf. steud- Hom. Gk. steümai, v. “
==== leaf 711
 immerse’. Nominal types: Gk. stigmé, f. “point, puncture; moment Go. stiks, m. “point of time, moment: OE stice, m. ‘sting, stab, stitch in the side’; sticca, wm. ‘stick, peg’; ON stik, npl. ‘stakes, piles’ beside stika, f. ‘stick’; Cz. steh, m. ‘stitch’; Pol. $cieg, m. id.; R (dim.) stežòk, m. id. Sw cf. also stick, n. ‘stitch’; sticka, f. ‘stick’
stigh- (stigh-), see steigh-, stoigh- Skt. cf. ati-, pra-stighnomi, v. ‘step’; W cf. siád ‘crown of head’; OCS stigna, f. “boule- vard, forecourt beside stígnoti, Cz. stihnout, v. ‘go; reach’; MHG cf. stigel, stigele, s & wf. ‘stile’ beside stige, stie, f. ‘sty’; Li. dial. stingù, stigti, v. “arrive, get to, come’; Latv. cf. stidzeju, v. ‘climb; become’. Nominal types in Av. stij, f. ‘battle’; Gk. stíkhes, pl. “lines, series’ beside stíkhos, m. “line, row'; OHG stëg, m. ‘footbridge, path’; stëga, f. ‘stairway’; OE stige, m. ‘ascent, descent’; ON ster stier, m., stig, n. ‘step, pace, path, degree’; OCS stíza, stízja, f. “path? beside stígní, stigna, f. “public square’; OCz. stzě, f. ‘path’; R stezjà, id.; Srb. staza, id.; Latv. stiga, f. ‘beeline’; (long-gde in) Ir. stíog, m. ‘dash, fit’. Extn. in ON stétt, f. ‘paving; degree; order; keelson'; stéttr, m. (crank, fr. *stight-)
stipolos, à (stíplos, à; sth-) “stem, pole,
stibhoros, stibhros (sth-) — stngh- (sthngh-)
20
25
30
35
45
1290
Stick, prop, base’. See next
Oss. tifil, s. (1) ‘straw, haulm'; Lat. stipula, f. id.; Ir. seol, m. ‘loom; bed'; W syl, pl. iau, f. “ground, base’; MHG
```


## [2026-09-06T16:04:02.551Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Wurfhammer\\|Wurfaxt\" BRT.txt | head; echo \"=== IEC\"; python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i,l in enumerate(t):\n    if re.search(r'\\bteukos\\b|\\bkeku\\b|\\bkakuš|cakuš|chakush', l):\n        print('leaf',i, l[:400].replace('\\n',' '))\nEOF",
 "description": "BRT Wurfhammer + IEC teukos"
}
```


### [2026-09-06T16:04:04.797Z] TOOL RESULT

```
11110:•  j.  £aku£-  n.  'Wurfhammer,  Wurfajct'  als Waffe:  hasaarptn  'tufottam^K, Mtafjanam "lauseDd  zweischneidige  Wurfäxte"  Yt  10. 130;  —  »J(V  akavd  nBit  •kJZ-ö  (NP.)'' YtJ.18.  ,
=== IEC
leaf 765 ophonic: Slovak: cüdit', Cz. cídit ‘cleanse, polish, purify’; Cz. cf. cudny ‘proper, moral: Blg. Cud, m. custom") teud- (teud-, tud-) (2) ‘beat, bang, crash’. Cf. tund- & tud- as a separate item. WP I, 513 & 745; II, 554 MHG dies, sm. “bang; noise; jolt'; (o-gde in) dos, sm. id.; OE péot, n. ‘din, howP'; peote, f. ‘gush, rush’; Sw. tjut, n. “howP'; tjuta, v. id.; Ir. cf. tuaim, f. ‘heavy blow, ban
```


## [2026-09-06T16:04:11.218Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11100,11115p' BRT.txt; echo \"=== col markers near\"; awk 'NR>10980 && NR<11120' BRT.txt | grep -n \"^ *5[67][0-9] *$\" | head",
 "description": "BRT cakus context"
}
```


## [2026-09-06T16:04:12.461Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8',errors='replace').read().split('\\f')\nimport re\nfor i in range(760,772):\n    l=t[i]\n    if 'teuk' in l or 'teukos' in l:\n        print('leaf',i)\n        j=l.find('teuk')\n        print(l[max(0,j-1500):j+2000])\n        break\nEOF",
 "description": "IEC teukos entry"
}
```


### [2026-09-06T16:04:12.880Z] TOOL RESULT

```
•  j.  £aeiiasta-')  m.  Name  eines  Sees*': 't)m  vairlm  S.  2.9;  —  'iahe  varffi/ tfy. 5,5;  —  tarn  yatata  .  .  Aaosrava  *pasne varöi?  'tahe  jafrahe  urväpahe  Yt5.49.
*}Des6^run>'ii-SeesimnordwestlichenFe[sien; s.  Ggr.  OK.  119,  Jn.  Zor.  197,  Marquart Eranlahr  108,  Bd.  22.  2:  vor  i  cieasi  andar älKtfiilaiän,  12.  36,  33.  8,  7.   I4.
Eig.  'weisschimmemd',  S  ^02  TL  b;    ai.  vgl
tandrä-  Adj.    —    ■>  Sie  NA.   hat   mehrmals
falsch  ösiHit';  s.  Ntr.
•  j.  iaetvnti-  £'>  -?-:  *ft'  F./o.
Pa.!  fiattail*.  —  ■)  So  nach  Pü.  VII.  3PPA. ID  iael-t
•  j.  (Sacäamna-  Adj.,  PPi7(Fut)M.:  s. ioy  mit  No.  4.
•  j.  calsmaH'  n.  'strucrio'(?). KompE.  ~  Zum  V.  'iaei..
y  caiazii:  s.  unter  iakus-.
•  j.  £aku£-  n.  'Wurfhammer,  Wurfajct'  als Waffe:  hasaarptn  'tufottam^K, Mtafjanam "lauseDd  zweischneidige  Wurfäxte"  Yt  10. 130;  —  »J(V  akavd  nBit  •kJZ-ö  (NP.)'' YtJ.18.  ,
np.  iatu!  'Hammer';  vgl.  Gdh.  KZ.  3$.  531 mit  Hbm.  PSI.  sa.  —  Pü.  |ia  Yt.  /):  iül  i h.,>ijil{%a  nach  Päi).  Sü. :  <ainii  j).  —  ■)  Them. —  »  Neubildung  nach  der  j;-Dekl.  (S  3^3), veranlasst  durch  das  vorhergehende  Nomen; man  beachte  den  Reim.  —  Ji  Daher  Dst. •disque';  doch  passt  das  nicht  lu  YL  10.
•  g.   £ag9d-  Adj.   'bietend,  gewährend',
mit  Akk.:  tal  vS  nS  haiaosh»hs  (sd)  . .
daidyli  savS , .  yagtmHSnhU {sA.)  lumanhä
masdä  raf^nm  'g>dö  (NP.)  Y.5/.ao.
=== col markers near
12:564
42:566
73:570
88:572
96:573
99:574
118:576
```


### [2026-09-06T16:04:15.213Z] TOOL RESULT

```
leaf 765
ophonic: Slovak: cüdit', Cz. cídit ‘cleanse, polish, purify’; Cz. cf. cudny ‘proper, moral: Blg. Cud, m. custom")
teud- (teud-, tud-) (2) ‘beat, bang, crash’. Cf. tund- & tud- as a separate item. WP I, 513 & 745; II, 554 MHG dies, sm. “bang; noise; jolt'; (o-gde in) dos, sm. id.; OE péot, n. ‘din, howP'; peote, f. ‘gush, rush’; Sw. tjut, n. “howP'; tjuta, v. id.; Ir. cf. tuaim, f. ‘heavy blow, bang; OCS tuma, f. ‘plague’ (if fr. *teudma). Cf. Srb. Cudam se, -ati, se, v. “be frightened"; ON pjóstr, m. (‘fury’, fr. a type *teudstos); Srb. cula, f. (“cudgel', fr. *teudla). (Slovak pod-cudky, m. pl. “siftings? is from cudit inf. ‘cleanse’, etc, of uncertain origin, see teud- (1))
teugos “fat, thick’. (Celtic variant: teguos. For metath. cf. tauros, $auros in their Celtic forms.
teubh- — teukso, ið
15
20
25
30
35
40
45
1390
Germanic variant: tigus) Mir, tiug, adj. ‘thick, dense’; Br. téó “fat, bul- ky; W tew “fat, thick’; Cor. tew, id., MHG dic, gs: dickes, adj. id. (fr. *tigus); Fris. Sw. tjock, id.; ON pjokkr, id. beside pykkr, id.; cf. Icel. piótta, f. (tough meat”, fr. *teugtà or *tiguta). (For OCS togü, Cz. tuhy, R tugój, see tongh-)
teuk- (teukos, à) (1) “tip, point, peak, beak’. Cf. tuk- (1) & keukos, à (1) Skt. Gokab, am. mn. ‘a root'; Per. cf. Caugan, s. “bat, club’; čukuš, s. ‘hammer’; Alb. suké, f. “hill, peak’; Ligur. (in Swiss) tschuggi, f. id.; Mir tuag, f. ‘axe’; Br. Suk, m. ‘nape, shoulder, chignon’: Blg. čuk, m. ‘hammer’; Srb. &üka, f. Cpeak, point’, fr. a variant *keuka); Latv. cf. Cukurs, m. “peak, point, gable’. (Indo-Iran. forms ambig.)
teuk- (2) “press; pressure, force’. Cf. tuk- (2) and next. See teuquó Arm. tok, ost ‘persistence’; tokam, v. (per. sist, endure'. Cf. SEM: AIE: § 56: IE -eu- > Arm. -0-); OHG diuhen, wv. “press, force” beside dühen, id. (fr. *tükio); G deuen, v. *tolerate; atone for; Li. cf. tüksti, intr. v. ‘bang’. (Gmc. forms ambig. Cf. teuquó as a variant in OE)
teuk- (touk-, tuk-) (3) “fat; fat part, buttock’. Cf. tuk- (2) & touk-. WP I, 711 Tokh. B cf. wi-cükaine ‘the two haunches, buttocks'; Olr. cf. (*-eu- or *-ou-) tuachail, adj. ‘pregnant’; OHG dioh, n., MHG diech, gs: diehes, n.; OE péoh, n.; ON þjó, n. ‘thigh, haunch’; Icel. ‘buttock’; Du. dij, f. as OHG; EMDu. dije, f. id.
teukså “girl, young female’. Cf. teuquio. (Norse type: touksàá) Norw. (landmal) taus, def: tausa; Norw. tós, Sw. tös, f. & n. ‘girl, wench’, (o-gde); Slovene Cuba, f. ‘heifer’; Blg. cf. (dim.) čuška, f. *cun- nus”. (Isophonic: Skt. Coksab, à, adj. pure)
teukso, ið (1) ‘chatter, twaddle’ W cf. tuch, m. ‘grunt, groan’; Rust, s. “non- sense’; Li. Ciauksti, v. (1) “twitter; stammer”; cf. čiauškalas, m. ‘twittering; twaddle’ beside (o-gde) tauskiu, tauksti, v. ‘twaddle’
teuksó, ið (2), see touks-. E-gde in MHG diusen, v. (lug, tousle; ge
```


## [2026-09-06T16:04:42.191Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD\"; grep -n -i \"cagad\\|čagād\\|cakuc\\|čakuč\\|cakuč\\|cakug\" PHD.txt PHD_mackenzie.txt | head -20; echo \"== NYB\"; grep -n -i \"cakuc\\|cagad\\|čakuč\" NYB_vol2_glossary.txt | head",
 "description": "MacKenzie/Nyberg for cakuc, cagad"
}
```


### [2026-09-06T16:04:42.286Z] TOOL RESULT

```
== PHD
PHD.txt:296:čābuk [c’Swk! | N ~] agile, nimble; excellent. ~th: agility. čādur [c?twl | N ~] sheet, veil. éagad [ck*t! | (N ¿ahad), J ¿eyad] peak, summit. сабаг [cki] wife (of the second degree). саһ [ол | N ~] pit, well. čahār [ALBA < A?rb‘; ch?l | M с, N ~] four. ~dah [cl’ldh | N ~] fourteen. ~-рау [cb Ip d | N ~ > čārwā] quadruped. čakēk [ckwk | N ~, cakáwak] lark. čakuč [cktwc | N čakuš] hammer. čambar [cmbl | N ~] circle, hoop. čamišn [cmšn! | M cmbyšn (?)] urination; lavatory. ` бапа [спа | = M, N ~] how many, much?; so many, much; some, a few. ~ih: amount, quantity. čandal [cndl | N ~] sandalwood. čandīdan, čand- [cnd-ytn! | (M cn-ystn)] tremble, quake. ~išn: trembling, movement. čang [eng | M bung, N ~] harp. ~-sray [-sPd] harpist. са�� [c7] = Carag. багар [clk' | M erg] pasture, grazing; flock. čārag [c?]k! | N ~a] means, remedy. ~garih [-glyh] ability, savoir faire. Carb [с/р | P crb, N ~] mild, gentle; fatty, oily. ~ih: gentleness; fattiness. ~išn [-sn'] fat, oil. ~і&потапа [-šrwmnd) oleaginous. Carm [с/т | M crm, N ~] skin, hide, leather. čārūģ [c wk! | N čārū] lime, mortar. „ēn [-yn!] limy. Carz [сіх | N ~] bustard. čāšīdan [c'$-ytn!] = čāštan. čašm [A YNE < A ‘ynh; ст | = M, N ~] eye. léaSmag [cfmk! | М cšmg, N ~a] spring, source. tčašmaģ [cfmk!] renowned. čašmaģāh [cšmk?s | M csmg’h] obvious, public, notorious. ~ih: notoriety, condemnation. čašm-arešk [cém ?ly$k!] envious. ^h: envy. čašm-dīd [cšm dyt'] visible, obvious. čāšnīg [c nyk! | M спус, N čāšnī] taste.
PHD.txt:2193:hammer čakuč, potk.
PHD.txt:3067:peak balën, bašn, čagād, tērag.
PHD.txt:3887:summit bālist, čagād, sar, térag.
PHD_mackenzie.txt:7223:owl bUf/g.                             peak balen, basn, cagad, terag.
PHD_mackenzie.txt:8443:cagad                    \tU'c;       cinisn
== NYB
```


## [2026-09-06T16:04:43.236Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== BRT Scheitel\"; grep -n \"Scheitel\\|Wirbel\" BRT.txt | head -10; echo \"== HRN cakus\"; grep -n -i \"cakus\\|čakuš\\|Hammer\" HRN.txt | head -20",
 "description": "BRT kakada, Horn hammer"
}
```


### [2026-09-06T16:04:43.319Z] TOOL RESULT

```
== BRT Scheitel
9833:l'Q.i  hac  dtüin  afiar  vailat  (gescht.  i'')0  hae fiixai')  i  silTiar  "rechls  auf  dem  EückgtBl  0 beim  drillen  Wirbel" a).  Vorher  steht:  apar\ buland  fa  sar  i  kSf  "oben  auf  der  Spitze  des , Höckers",  —  >>  Zu  vaslan  'drehen',  rgl.  lat. virUbra.  —  ")  Eig.  'Knoten'
20395:•  j.  'msrszav-  n.  'Wirbel'  des  Halses  und Rückens:  yavata  . .  tii/ainti  °tu/a  ttünB gayehe  'sula  x&  uimnahe  "bis  er  entzwei
20396:schlägt  die  Wirbel,  die  Säulen  des  Lebens, die  Wirbel,  die  Quellen  der  Lebenskraft" Yt/o.  71.
25570:■  j.  urvaesa-  m.  'vertex,  Wirbel'  im Wasser;  vansdJtavanhsm  aps  'am  Yt  14. 29.  2)  "Wende'  des  Wegs, 'Wendepunkt' der  Rennbahn:  tl  .  .  fravas>nti  darai- urvals»m  t^twanS  's?m  nsAmna  "die  . . fahren  jetit  weiter  zu  der  fernen  Wende des  Wegs,  um  den  Wendepunkt  zu  er- reichen .  ."  Yt.  IJ.  58;  —  ^fläa  as/>a  ,  . aparat  haca  *s:l^  fratanm  'am  *näs?m>ta "wie  Rosse  .  .,  die  vom  hintern  Wende- punkt (der  Rennbahn)  her  den  vorderen Wendepunkt  erreichen  wollen"  VytSjj; —  °sU  F.p.  a)  überhaupt  'Ziel,  Ende': ushme  °se  gayehe  "am  äussersten  Ziel  des LebcDs"  Y.7r.iSi  '61  H.j.15;  —  damBil'si apiml  "beim  letzten  Ende  der  Schöpfung" Y.  4J.  5;  6;  —  apjmt  ankSus  'st  "beim letzten  Ende  des  Lebens"  Y.f/.ö;  —  'sa
== HRN cakus
3077:Fayfür (Kaiser von Byzanz) v. Hammer, Geschichte der schönen
4092:443. eekuS 'Hammer .
4093:aw. cakusqm, yt. 10, 130 'Hammer', Geldner, KZ.
9926:cHüc, — Statt cakusqm lies cakusqm,
```


## [2026-09-06T16:05:01.516Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '11090,11112p' BRT.txt | cat -n | head -30; echo \"=== HRN 443\"; sed -n '4085,4100p' HRN.txt",
 "description": "BRT column markers and Horn 443"
}
```


### [2026-09-06T16:05:01.579Z] TOOL RESULT

```
     1	.      die  Relativ,  und  Konjnnktioiissatze ,    die    als
     2	Subjekt,  Objekt  usw.  erscheinen.  —  -  *"
     3	ist   I
     4	anzunehmen,
     5	ob,Google
     6	S75
     7	äae£asta-
     8	£axravEmt-
     9	576
    10	hochtonige  Wörter  dazwischen  stehen,  die nicht  zu  dem  mit  i'J  angeschlossenen  Skttt eil gehören.  Enklitika  trennen  nicht,  s.Y.jg.3 tSp.  569  o.),  41--  4  (Sp.  5Ö7  n.);  vgl.  Yt.  /.  i9(Sp. 573  u.).  —  3I  c'H  iwischen  iwei  verbundenen Duilen  verknüpft  nicht  diese  untereinander, sondernbeideiusunmeniUcinGlied  mit  einem oder  mehr  andern;  s.  Bthl.  BU.  /O.  268.  So  Y. 30.  II,  3/.  4,  Vr.  p.  5.  —  4>  Man  erwartete iu/rtumniafias^a  V  ffsaniühi.  —  J)  Man  ver- langte vircAuilniH  .  ,  vätäM  kyal .  .  earaii.  — <'1  5.  dazu  Cld.  KZ.  30.  545,  31.  157,  Proa. 43.  —  7>  oSäi  und  Uubyä^  gehören  als  Eweiles Glied  Eusammen,  s.  Sp.  5JÖ  m.  —  S>  Man  sollt« yat  haemim  gavafa  r"  .  .  erwarten.  —  9>  Für Stellen  wie  Y.  9.  18,  Yt.  fj.  1,  19.  67  nsw. ist  Bildung  von  Gruppen  anzunehmen,  deren Glieder  iT.  asynibetisch  aneinander  gereiht sind.  Im  Folgenden  werden  nur  diese  Gruppen berückiichiigt.  Doch  ist  begreiflicher  Weise die  Grenze  nicht  überall  mit  Sicherheit  lu bestimmen;  s.  i,  B.  Y.  5/.  7,  Sp,S7i  o.  (vgl. dagegen  Y.  44.  6),  Yt.  //.  14,  Sp.  570  m.  — ■o)  Nach  Ausweis  des  Metrums  Glosse.  — ■')  Man  tivanei  yaniyai^  xia^r^m.  —  '»)  Von denen  in  Strophe  1  d  :  yaifä  . .  die  Rede  ist. —  ij)  Normal  wäre  ainraiS  m'.  —  ■«)  Statt des  regelrechten  aSilra  aparäJim^m.  —  <i)  tä ist  enklitisch;  vgL  No,  2.
    11	•  j.  £aeiiasta-')  m.  Name  eines  Sees*': 't)m  vairlm  S.  2.9;  —  'iahe  varffi/ tfy. 5,5;  —  tarn  yatata  .  .  Aaosrava  *pasne varöi?  'tahe  jafrahe  urväpahe  Yt5.49.
    12	*}Des6^run>'ii-SeesimnordwestlichenFe[sien; s.  Ggr.  OK.  119,  Jn.  Zor.  197,  Marquart Eranlahr  108,  Bd.  22.  2:  vor  i  cieasi  andar älKtfiilaiän,  12.  36,  33.  8,  7.   I4.
    13	Eig.  'weisschimmemd',  S  ^02  TL  b;    ai.  vgl
    14	tandrä-  Adj.    —    ■>  Sie  NA.   hat   mehrmals
    15	falsch  ösiHit';  s.  Ntr.
    16	•  j.  iaetvnti-  £'>  -?-:  *ft'  F./o.
    17	Pa.!  fiattail*.  —  ■)  So  nach  Pü.  VII.  3PPA. ID  iael-t
    18	•  j.  (Sacäamna-  Adj.,  PPi7(Fut)M.:  s. ioy  mit  No.  4.
    19	•  j.  calsmaH'  n.  'strucrio'(?). KompE.  ~  Zum  V.  'iaei..
    20	y  caiazii:  s.  unter  iakus-.
    21	•  j.  £aku£-  n.  'Wurfhammer,  Wurfajct'  als Waffe:  hasaarptn  'tufottam^K, Mtafjanam "lauseDd  zweischneidige  Wurfäxte"  Yt  10. 130;  —  »J(V  akavd  nBit  •kJZ-ö  (NP.)'' YtJ.18.  ,
    22	np.  iatu!  'Hammer';  vgl.  Gdh.  KZ.  3$.  531 mit  Hbm.  PSI.  sa.  —  Pü.  |ia  Yt.  /):  iül  i h.,>ijil{%a  nach  Päi).  Sü. :  <ainii  j).  —  ■)  Them. —  »  Neubildung  nach  der  j;-Dekl.  (S  3^3), veranlasst  durch  das  vorhergehende  Nomen; man  beachte  den  Reim.  —  Ji  Daher  Dst. •disque';  doch  passt  das  nicht  lu  YL  10.
    23	•  g.   £ag9d-  Adj.   'bietend,  gewährend',
=== HRN 443
aus t. qapnn*<i *fangen, erhaschen* entlehnt.— 99 —
442. öu8t 'flink, tätig, passend'.
ai. l/cörf-, corföf^e 'antreiben ; sich beeilen' (Nöldeke,
mündliche Mitteilung).
Fr. Mtiller's (WZKM. 5, 68) Ableitung des Wortes
aus aw. cista- bezw. cista- ist schon wegen der Vokal-
difl^erenz (doch vergl. np. miizd) wenig wahrscheinlich.
443. eekuS 'Hammer .
aw. cakusqm, yt. 10, 130 'Hammer', Geldner, KZ.
25, 531 Note 210.
Das neupersische Wort ist nicht klar; eine Neben-
form ist öeköd oder deköj, vergl. dialektisch Kasan:
ceküSy rakoz, caküs, ödkös, vergl. kurd. cäqü, cek (H.-Sch.).
Nöldeke schlägt vor (mündliche Mitteilung), auch np.
öäk 'Spalt, Bruch' zu öekus zu stellen.
444. {\)ceni *Essen', cemfden 'trinken'.
```


## [2026-09-06T16:05:03.140Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== MON چاقو\"; grep -n \"چاقو\" MON_part1.txt MON_part2.txt | head -5; echo \"== MON چکاد\"; grep -n \"چکاد\" MON_part1.txt MON_part2.txt | head -5; echo \"== MON چکش\"; grep -n \"چکش\" MON_part1.txt MON_part2.txt | head -5; echo \"== FRS چکاد\"; grep -n \"چکاد\" FRS.txt FRS_pages.txt | head -5",
 "description": "Mo'in and Loghat-e Fors greps"
}
```


### [2026-09-06T16:05:03.246Z] TOOL RESULT

```
== MON چاقو
MON_part1.txt:29360:با چاقو بریده می‌شود مانند سدیمء در نفت 
MON_part1.txt:49532:چاقولو 
MON_part1.txt:49544:چاقو: 52( چاکوه قس, چاکوچ؛ چکش| 
MON_part1.txt:49549:چاقوکشی: .5-1008 (حامص.) عمل 
MON_part1.txt:76092:است که با چاقو به آسانی بریده می‌شود. 
== MON چکاد
MON_part2.txt:6424:میان موی سر؛ چکاد» چکاده. فرق سر: سر 
MON_part2.txt:14634:قله: (م)۱ام, (ع. قلة] (.) سر کوهء چکاد؛ 
MON_part2.txt:24676:مابین فرق و بیشانی» چکاد. 
MON_part1.txt:50919:چکاد: 2٩‏ (رآس, قله| (ا.) تارکك سره 
MON_part1.txt:65171:سرکوه قله. تارکك سره چکاد. بالای هر 
== MON چکش
MON_part2.txt:8357:چکش خوارند و قابل تبدیل به مفتول شدن 
MON_part2.txt:9189:حرارت زیاد چکش خوار است. چگالی آن 
MON_part2.txt:10410:مو و ران باریکك و سم کوچکش آن را به 
MON_part2.txt:14165:۸ خاصیت تورق و چکش‌خواری آن 
MON_part2.txt:15137:قندشکننده] (ص‌فا. .) چکشی که ۳ 
== FRS چکاد
FRS.txt:4872:چنانکه پیشانی‌راجکاد کوتدسر 5 نوه را نمز چکاد خوانند فر دوسی گفت 
FRS.txt:4876:بغغم بسیار بود » س ( مثل متن )۰ ۳ - چ :روخ چکاد کلمتیست فهلوی » روخ 
FRS.txt:4877:روده باشد وچکادبالای پیثانی و بیهلوی روخ چکاد اصام بود .ن : دوخ چکاد [کذا] 
FRS.txt:4880:را ازینبه دانه بیرون کنند گونندفلخود . ٩‏ -ن : چکادسر کوه بود» س (مثلمتن ) » 
FRS.txt:4881:3 .چکاد و هباك و کلال مبان سر باشد» طاهر فضل کوید :
```


## [2026-09-06T16:05:20.046Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '49535,49555p' MON_part1.txt; echo \"=== chakad MON\"; sed -n '50915,50930p' MON_part1.txt",
 "description": "Mo'in chaqu and chakad"
}
```


### [2026-09-06T16:05:20.115Z] TOOL RESULT

```
جاقالو: 5ات [تر. ف. - چاق + آلو(د)) 
(ص‌مف.) (عم.) فربه» چاق. 

چائچور: "بت |- چاقلور - چاخچور] 
(.) شلوار گشاد و بلند و کف‌دار زنانه که آن 
را بر روی شلیته و تنبان‌ها می‌پوشیدند و 
دارای لیفه و پندی بود که در زیر شکم بسته 
اه 

چاقو: 52( چاکوه قس, چاکوچ؛ چکش| 
(.) آلتی مرکب از تبغهٌ فولادین و دسته‌های 
چوبین و آن برای بریدن و تراشیدن بکار 
رود. 

چاقوکشی: .5-1008 (حامص.) عمل 
چاق وکش. 

جاک: »2 (.) شکاف. ترا کك. رخنه. باره. 
سفیدةً صبح. در یچه. 

چاک: *08(- چک - جک ] (ا.) قباله باغ و 
=== chakad MON
جند ک ردن. 

چکساچک: :5:2-505 (- چک چک| 
(امر.) سخن و خبری که در افواه افتد. 
چکاد: 2٩‏ (رآس, قله| (ا.) تارکك سره 
بالای سرء فوق سر. بالای پیشانی؛ جبهه. سر 
کوه» قله, سیر » سحبه. 

چکامه: (0-)2۳02ن [ - جنغامه < چکٌّامه | 
(۱.) قصیده» شعر. ضح.. این کلمه با کات 
بارسی و تازی هر دو آمده. 
جکامه‌سرا(ی): (0ت«م (- 
جکامه‌سراینده] (ص‌فا.) قصیده‌سرا» شاعر. 
چکان: 62-0 (رص‌فا.) چکنده. چکاننده. 
ضح.- در ترکیبات نیز به معنی «چکاننده» 
اخلا قطر ه چکان.
```


## [2026-09-06T16:05:22.227Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"cemetery\\|coemeterium\\|koimeterion\" KLN_1966.txt | head -5; echo \"== SKT\"; grep -n \"cemetery\" SKT.txt | head -3; echo \"== KLN civil/city\"; grep -n \"^civil\\|^city\\|civis, \" KLN_1966.txt | head -5",
 "description": "Klein cemetery"
}
```


### [2026-09-06T16:05:22.314Z] TOOL RESULT

```
1466:Acoemeti,  n.,  pi.,  name  of  an  order  of  Eastern monks.  —  Eccles.  L.,  fr.  Gk.  dxot|j.Y]xoi,  ‘the sleepless  ones’,  from  a-  (see  priv.  pref.  a-)  and xoijjLav,  ‘to  lull  to  sleep’.  See  home  and  cp. cemetery.
6731:catacomb,  n.,  an  underground  cemetery.  —  F. catacombe ,  fr.  Late  L.  catacumba ,  dissimilated fr.  *cata  tumbas ,  ’beside  the  tombs’  (prob.  under the  influence  of  L.  - cumbere ,  ‘to  lay  oneself down,  to  lie').  See  cata-  and  tomb.
6946:cemetery,  n.  —  Late  L.  coemeterium,  fr.  Gk. y.oiur,-nr,ptov,  ‘sleeping  room,  burial  place’,  fr. xoiuxv,  ‘to  put  to  sleep’,  which  is  rel.  to  xoi-ri), ‘place  to  lie  down  in,  bed’,  xot-ro;,  ‘place  to  lie down  in,  bed;  sleeping,  sleep’,  xoitcov,  ‘bed¬ chamber’,  xei(jl<xi,  ‘I  lie  down,  lie  asleep’,  xcoptr), ‘village’,  fr.  I.-E.  base  *kei~,  ‘to  lie,  rest’,  whence also  Goth,  halms,  ‘village’,  OE.  ham,  ‘home, house,  dwelling’.  See  home  and  cp.  city,  civil. Cp.  also  the  second  element  in  neossine. cenacle,  n.,  a  dining  room.  —  F.  cenacle ,  fr.  L. cenuculum,  'dining  room’,  fr.  cena,  ‘dinner’, which  stands  for  *qert-sna  (cp.  Oscan  kersnu, of  s.m.),  lit.  ‘portion’,  fr.  I.-E.  base  *qert-,  ‘to cut’,  whence  also  OI.  kpntdti,  ’cuts’,  Lith.  kertu, kirsti,  ‘to  hew’.  Arm.  k'ert'em,  ‘I  skin,  flay’,  and prob.  Hitt,  karsh-,  ‘to  cut  off’.  Base  *qert-  is an  enlargement  of  base  *qer~,  ‘to  cut’,  for  which see  carnal.
7799:*kei-,  ‘to  lie,  settle  down’,  whence  also  Gk. xcicrDm,  ‘to  lie,  to  lie  asleep',  xei[x7]Xtov,  ‘treas¬ ure’,  lit.  ‘anything  stored  up’,  xoi^av,  ‘to  put to  sleep’,  >coip.r;Ty)piov,  "a  sleeping  room,  a  burial place’,  xolrt),  ‘place  to  lie  down  in,  bed’.xotfo;, ‘place  to  lie  down  in,  bed ;  sleeping,  sleep’,  xcojj.7), ‘village’,  the  second  element  in  veomroi;  (for ‘a  young  bird’,  and  in  nap.mhc (for*  7tEpi-xto-<;),  ‘beyond  the  regular  number, odd’,  lit.  ‘lying  beyond’,  OSIav.  semija,  ‘family, domestic  servants’,  Lith.  seima ,  seimyna,  Lett. saime ,  OPruss.  seimins,  ‘domestic  servants’, Lett,  sieva,  ‘wife’,  OSIav.  po-sivu,  ‘able,  fit’, Goth,  haims,  ‘village’,  OE.  ham,  ‘home,  house, dwelling’,  OIr.  cdim,  coem,  ‘dear,  beloved’,  OW. cum,  ModW.  cu,  of  s.m.,  and  prob.  also  OI. sivah,  sivah,  ‘kind,  friendly,  gracious’.  All  these words  denote  relationship  or  love  to  the  family or  clan.  See  home  and  cp.  city,  citizen.  Cp. also  cemetery,  cimelia,  coma,  ‘insensibility’, incunabula,  neossine,  neossology,  perissad,  Peris- sodactyla,  quiet,  Siva.
15429:frith,  n.,  enclosure;  wooded  land,  brushwood.  — ME.,  fr.  OE.  fridu,  ‘peace,  security’  (cp.  OE. fridgeard,  ‘enclosure,  court’).  For  sense  develop¬ ment  cp.  MHG.  vride,  ‘enclosure’,  G.  einfrie- digen,  ‘to  fence  in,  enclose’,  Friedhof,  ‘cemetery’, which  are  rel.  to  G.  Friede,  ‘peace’.  See  free  and cp.  words  there  referred  to.
== SKT
3219:hence,  cement    Perhaps  for  crtfrMtm from  eadtrt^  to  cut. Cemetery.  (L— Gk.)     Low /rri'wm.  — Gk.  KOitir}H}fiio¥,  a  sli cemetery.  — Gk.  Koifiaa/,  I  lull pass.,  to  fall  asleep.    Allied  to down.     (VK1-) coma.  (Gk.)    Gk.  Hwfta,  a  deep
== KLN civil/city
7752:civil
7792:Citrus,  n.,  genus  of  shrubs  and  trees,  including citrons,  lemdns,  etc.  —  L.  citrus,  ‘citron  tree’, fr.  Gk.  xsSpo?.  See  citron, citric,  adj.  —  Formed  fr.  prec.  word  with  suff.  -ic. cittern,  n.  —  A  var.  of  cither(n). city,  n.  —  ME.  cite,  fr.  OF.  cite  (F.  cite),  fr.  L. civitatem,  acc.  of  civitas,  ‘citizens  of  a  commu¬ nity,  citizenship,  state’,  fr.  civis,  ‘member  of  a community,  citizen’.  See  civil  and  -ty  and  cp. Olt.  cittade  (whence  It.  cittd),  OProveng.  and Catal.  ciutat,  Sp.  ciudad.  Port,  cidade,  ‘city, town’,  Rum.  cetate,  ‘castle,  fortress’,  which  all derive  fr.  L.  civitatem.
7796:civics,  n.,  the  science  dealing  with  the  duties  and rights  of  citizens.  —  See  prec.  word  and  -ics. civil,  adj.  —  F.,  fr.  L.  chilis,  ‘pertaining  to  a  cit¬ izen,  pertaining  to  public  life;  polite’,  fr.  civis, ‘member  of  a  community,  citizen’,  fr.  I.-E.  base
7797:civility
7800:civility,  n.  —  OF.  civilite  (F.  civilite),  fr.  L.  civili- tatem,  acc.  of  civiUtas,  ‘the  art  of  governing, politics;  courteousness,  politeness’,  fr.  civilis. See  prec.  word  and  -ity.
```


## [2026-09-06T16:05:43.008Z] TOOL CALL #35: Bash

```json
{
 "command": "pdftoppm -f 249 -l 249 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"$SCRATCH/pg249\" 2>/dev/null || pdftoppm -f 249 -l 249 -r 200 -png -singlefile /home/sfmqrb/git/rishe/EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg249; ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/",
 "description": "Render PDF page 249"
}
```


## [2026-09-06T16:05:43.523Z] TOOL CALL #36: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T16:05:45.657Z] TOOL RESULT

```
total 9404
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 12:05 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    1100 Sep  6 12:04 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  180887 Sep  6 11:56 bqt1637_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   50592 Sep  6 11:56 bqt1637_kaz.png
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
-rw-rw-r-- 1 sfmqrb sfmqrb   12820 Sep  6 11:05 crop_germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb    3408 Sep  6 11:05 crop_guthjo.png
-rw-rw-r-- 1 sfmqrb sfmqrb  111118 Sep  6 11:19 crop_habl.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9001 Sep  6 11:05 crop_node12.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5564 Sep  6 11:05 crop_node1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    5286 Sep  6 11:05 crop_varathra.png
-rw-rw-r-- 1 sfmqrb sfmqrb   11652 Sep  6 11:13 c_xzn.png
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
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:52 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   33321 Sep  6 11:51 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   75263 Sep  6 12:04 pg251.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   53545 Sep  6 12:03 w241.py
```


### [2026-09-06T16:05:45.663Z] TOOL RESULT

```


```


## [2026-09-06T16:05:49.155Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg249.png"
}
```


### [2026-09-06T16:05:49.652Z] TOOL RESULT

```

```


## [2026-09-06T16:05:49.648Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T16:06:04.811Z] TOOL CALL #38: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1ey-",
 "prompt": "What is the root, its meaning, and which descendants are listed (Greek koitē/koimaō, Latin cīvis, Sanskrit śiva-, Germanic haimaz/heim)? Is Germanic *haimaz derived from this root or from *tḱey-?"
}
```


## [2026-09-06T16:06:06.977Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A3%D8%B1%D9%8A%D9%83%D8%A9",
 "prompt": "What does Wiktionary say about the Arabic word أريكة (arīka): meaning, root, and etymology? Is it native Arabic (root ʔ-r-k) or a loan from Greek or Persian?"
}
```


## [2026-09-06T16:06:09.094Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%DA%A9%D8%B4",
 "prompt": "Persian چکش: etymology — Middle Persian form, Avestan čakuš, and any cognates. Quote the etymology section."
}
```


## [2026-09-06T16:06:10.067Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D8%A7%D9%82%D9%88",
 "prompt": "Persian چاقو (čāqu) 'knife': what etymology does Wiktionary give? Turkic loan or native Iranian? Quote it."
}
```


### [2026-09-06T16:06:11.261Z] TOOL RESULT

```
# Proto-Indo-European Root ḱey-

**Root and Meaning:**
The reconstructed root is "*ḱey-" (imperfective), with meanings: "to be lying down" and "to settle."

**Key Descendants Listed:**

- **Greek:** κοίτη (koítē) - derived from *ḱoy-teh₂
- **Latin:** cīvis - derived from *ḱéy-wo-s ("intimate, dear, friendly")
- **Sanskrit:** शिव (śivá, "auspicious") - derived from *ḱéy-wo-s

**Regarding Germanic:**
The page lists *hīwą/*hīwô as deriving from Proto-Germanic (itself from *ḱéy-wo-s), not from *tḱey-. The article separately references "*tḱey-" as a related but distinct root in its "See also" section, suggesting they are separate etymological sources.
```


### [2026-09-06T16:06:13.254Z] TOOL RESULT

```
# Arabic Word أريكة (arīka)

## Meaning
The word has two primary definitions:
1. **Sofa** — a piece of furniture for sitting
2. **Throne** — a royal seat of authority

## Etymology
The origin is disputed. According to Wiktionary, the etymology is "Unknown" but scholars have proposed multiple theories:

**Iranian Theory**: Researchers suggest a possible connection to Classical Persian اورنگ (awrang, "throne"), though this connection is described as "difficult."

**Native Arabic Theory**: Alternative explanations propose connecting it to native Arabic roots, either:
- The word أَرَاك (ʔarāk, "toothbrush tree"), since these trees provided shelter and food for animals and humans
- A possibly obsolete verb meaning "to persevere, to bide" — fitting the semantic field of "a place of abode"

The native origin theory suggests that even if related to the plant name, that relationship "likely derives from the plant name" rather than vice versa.

## Conclusion
Wiktionary categorizes أريكة as "borrowed from Iranian languages" while acknowledging substantial uncertainty about its true origin.
```


### [2026-09-06T16:06:15.304Z] TOOL RESULT

```
# Etymology of Persian چکش (Hammer)

The word چکش traces back through several linguistic layers:

**Middle Persian origin:** "From earlier چکوچ (čakuč), from Middle Persian ckwc (čakuč, 'hammer')"

**Avestan connection:** The Middle Persian term derives from Avestan 𐬗𐬀𐬐𐬎𐬱 (cakuš, "battle-axe")

**Proto-Indo-European root:** This ultimately stems from "*keku-" meaning "cudgel, hammer shaped stick"

The entry notes that چکش is a doublet of چاقو (čâqu), sharing common ancestry. The word also descended into Arabic as شاكوش (šâkûš).
```


### [2026-09-06T16:06:17.659Z] TOOL RESULT

```
# Etymology of Persian چاقو (čāqu)

According to Wiktionary, the word has **native Iranian origins**, not a Turkic loan. The entry states:

> "From earlier چاکو (čākū) from Middle Persian [Book Pahlavi needed] (ckwc /⁠čakuč⁠/, "hammer"), from Avestan 𐬗𐬀𐬐𐬎𐬱 (cakuš, "battle-axe"), from Proto-Indo-European *keku- ("cudgel, hammer shaped stick")."

The Wiktionary article does mention a related Turkish word, noting the term is a "Doublet of چکش (čakuš)," but it traces the Persian etymology back through Middle Persian and Avestan to Proto-Indo-European roots, making it a native Iranian word family rather than a borrowed Turkic term.
```


## [2026-09-06T16:06:26.077Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/t%E1%B8%B1ey-",
 "prompt": "What is *tḱey- and which descendants (Proto-Germanic *haimaz 'home', Greek ktizein, Latin situs)? Does the page say it is distinct from *ḱey- 'to lie'?"
}
```


## [2026-09-06T16:06:27.385Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/hamlet",
 "prompt": "Etymology of hamlet: Old French hamel/hamelet, Frankish *haim, Germanic. Quote it. Also anything about Henry?"
}
```


## [2026-09-06T16:06:28.496Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/Henry",
 "prompt": "Etymology of the name Henry: Old French Henri, Old High German Haimirich 'home ruler'? Quote."
}
```


## [2026-09-06T16:06:30.730Z] TOOL CALL #45: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%DA%A9%D8%A7%D8%AF",
 "prompt": "Persian چکاد (čakād) 'summit, peak': what etymology does Wiktionary give (Middle Persian čagād, Avestan kakaδa- etc.)? Quote."
}
```


### [2026-09-06T16:06:31.699Z] TOOL RESULT

```
# Proto-Indo-European *tḱey-

**What it is:** This is a reconstructed Proto-Indo-European root with three core meanings: "to cultivate," "to settle," and "to live." It's classified as an imperfective verb root.

**Key descendants include:**
- Proto-Germanic *haimaz (English "home")
- Ancient Greek ktízō (κτίζω) and related terms
- Latin sinō and pōnō
- Sanskrit kṣiti (क्षिति) and kṣema (क्षेम)

**Distinction from *ḱey-:** Yes, the page explicitly distinguishes them. Under "See also," it references "*ḱey-" as a separate entry, suggesting they are treated as distinct roots despite their phonetic similarity.

**Etymology note:** The page indicates *tḱey- was "reanalysed" from *tḱéyti, suggesting it emerged through morphological reanalysis rather than being an original root form. The asterisk denotes it's a reconstruction based on comparative evidence, not directly attested in historical texts.
```


### [2026-09-06T16:06:33.200Z] TOOL RESULT

```
# Etymology of Hamlet

Based on the Online Etymology Dictionary, the word "hamlet" originates from Old French *hamelet*, a diminutive of *hamel* meaning "small village." The source traces further back through Frankish *\*haim* and Proto-Germanic *\*haimaz* ("home"), ultimately deriving from the PIE root *\*tkei-* meaning "to settle, dwell."

**Key quote:**
> "small village without a church, little cluster of houses in the country," early 14c., *hamelet*, from Old French *hamelet* "small village," diminutive of *hamel* "village"

The "-let" suffix is a diminutive noun-forming element from Old French, making "hamlet" literally a "small home/village."

**Regarding Henry:** The provided content contains no information about anyone named Henry. The references to "Hamlet" in the document pertain to Shakespeare's play, not a person named Henry.
```


### [2026-09-06T16:06:34.150Z] TOOL RESULT

```
# Etymology of Henry

The name Henry originates from Old High German *Heimerich*, meaning "ruler of the house." The Online Etymology Dictionary explains: "from Old High German _Heimerich_, literally 'the ruler of the house,' from _heim_ 'home'...+ _rihhi_ 'ruler.'"

The name traveled through several languages before reaching English:
- **Old High German**: Heimerich
- **German**: Heinrich
- **Late Latin**: Henricus
- **French**: Henri
- **English**: Henry

The "ruler" component derives from a Proto-Indo-European root meaning "to lead, rule," while "home" traces back to Germanic words for dwelling and household. After the Norman Conquest, Henry became one of the most widely adopted names in England.
```


### [2026-09-06T16:06:35.177Z] TOOL RESULT

```
Based on the Wiktionary content provided, the etymology section does not mention Middle Persian čagād, Avestan kakaδa-, or similar forms. Instead, it states:

"Akin to Old Armenian ճակատ (čakat, 'forehead'), an Iranian borrowing. Note also Lithuanian kaktà ('forehead, brow')."

The entry traces the Persian word's origin to related terms in Armenian and Lithuanian meaning "forehead," rather than to the Middle Persian and Avestan forms you referenced.
```


## [2026-09-06T16:07:06.677Z] TOOL CALL #46: Bash

```json
{
 "command": "python3 tools/ref_page.py TAD:2 --image 2>&1 | tail -30",
 "description": "Fetch TAD page 2 image"
}
```


## [2026-09-06T16:07:07.989Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json;d=json.load(open('refs_online.json'));print(json.dumps(d['BQT'],ensure_ascii=False,indent=1)[:2000])\"",
 "description": "BQT page offset info"
}
```


### [2026-09-06T16:07:08.517Z] TOOL RESULT

```
no scan of TAD covers printed page 2 (see 'scans' in refs_online.json)
```


### [2026-09-06T16:07:09.918Z] TOOL RESULT

```
{
 "title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)",
 "kind": "archive_djvu+local_scan_ocr",
 "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.",
 "lookup_hint": "grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \\f; leaf N = N-th \\f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/borhan-ghate-v1 for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}. Secondary: Dehkhoda (vajehyab.com/?q=<word>&d=dehkhoda, parsi.wiki, abadis.ir/fatofa/<word>/) quotes Borhan and often Mo'in's footnotes as (حاشیهٔ برهان قاطع چ معین). noorlib.ir/book/info/10294 is a 1-vol Nima 1380 Borhan without Mo'in's notes. | For pages in a scanned
```


## [2026-09-06T16:07:26.261Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,l in enumerate(t):\n    if 'اریکه' in l or 'ارايك' in l:\n        print('leaf',i,'---')\n        j=l.find('اریکه')\n        print(l[max(0,j-300):j+300])\nEOF",
 "description": "Borhan vol1 arike"
}
```


## [2026-09-06T16:07:26.461Z] TOOL CALL #49: WebSearch

```json
{
 "query": "Sanskrit \"coka\" Monier-Williams meaning root cokṣa"
}
```


### [2026-09-06T16:07:28.170Z] TOOL RESULT

```
leaves 777
leaf 698 ---
: مقدمه کتاب حاضر :
نخاری.  .‏ ت»ه تعاری - (زبان) ؛ رگ : مقدمه کتاب حاضر:تخلری- نخار ستان - ره :
مقدمة کتاب حاضر: شخاری. ‏ . ۵ قخت - بفتح‌اول» پهلوی/20] «ناوادبا ۱5۵ «مسیناله ۲:۱4
ادکاشمی 48166 (سربر)« کربرسن ۹۷ کیلکی/816),ممربآن نیز تخت (نخت‌خواب» ستر» نخت
رمل) «دژی 4۲:۱۲:۱ «ابن‌درید»» «تفس؟؛ کرسی؛اریکه, سربر, مححل‌جلوی شامدر روژ بار وسلام-
شهر وعفر سلطنت_هرجای مسطح وهموار- نشیمنگاه چوبین باآهنین چهار پایه .
( بر هان فاطع۱۴)
۵ - ء زیر قیصران وگاه تخت اردشیر
```


### [2026-09-06T16:07:36.077Z] TOOL RESULT

```
Web search results for query: "Sanskrit "coka" Monier-Williams meaning root cokṣa"

Links: [{"title":"Monier-Williams Sanskrit-English Dictionary --च","url":"https://sanskrit.inria.fr/MW/91.html"},{"title":"Coka, Cōkā: 5 definitions","url":"https://www.wisdomlib.org/definition/coka"},{"title":"Buddhi","url":"https://en.wikipedia.org/wiki/Buddhi"},{"title":"Raksha (Vedic)","url":"https://en.wikipedia.org/wiki/Raksha_(Vedic)"},{"title":"Aesthetics of Sanskrit Poetry from the Perspective of Computational Linguistics: A Case Study Analysis on Siksastaka","url":"https://arxiv.org/pdf/2308.07081"},{"title":"R","url":"https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English/R"},{"title":"Vik%E1%B9%A3epa","url":"https://en.wikipedia.org/wiki/Vik%E1%B9%A3epa"},{"title":"Lexicographical Studies In Jaina Sanskrit - Jain Quantum","url":"https://jainqq.org/booktext/Lexicographical_Studies_In_Jaina_Sanskrit_Romanized/032134"},{"title":"Middle English Dictionary Entry","url":"https://quod.lib.umich.edu/m/middle-english-dictionary/dictionary/MED8313"}]

Based on the search results, I found information from the Monier-Williams Sanskrit-English Dictionary about both terms:

**Coka (चोक):** The root of Cleome felina, as found in the Bhāvaprakāśa text.

**Cokṣa (चोक्ष):** Cokṣa is described as an adjective meaning "pure, clean (persons)", with references to classical Sanskrit texts like Manu Smṛti and the Mahābhārata.

The two terms appear to be distinct entries in the Monier-Williams dictionary. While "coka" refers to a plant (specifically the root of Cleome felina, a plant used in Ayurvedic medicine), "cokṣa" is an adjective related to purity or cleanliness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T16:07:47.172Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && head -c 400 BQT_v1_pages.txt; echo; grep -c \"pdf page\" BQT_v1_pages.txt; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (150,151,152):\n    print('=== leaf',i, t[i][:300].replace('\\n',' '))\nEOF",
 "description": "BQT v1 page mapping"
}
```


### [2026-09-06T16:07:48.944Z] TOOL RESULT

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

0
=== leaf 150 مقد‌مه صد وچپل ودق _ 1۱۱- گیاه‌شناسی. حسی نگل کلاب. چاپ دوم. ازانتشارات شر کت سپامی چپر . ۱۳۷۸شمسی (-- گلگلاب). ۱۱۷-اللغاتالنو اثبة و الاهتشهادات الحفتائية.رك: شمار؛175 مأخذ اروپایی (-جفتایی). ۸ لفت فر س. علی ان احمد‌اسدی طوسی. بتصحیح عباس اقبال. نپران. چاپغانه مجلس ۱۳۱۹شمسی. لفت نامه علی اکبر دهخدا
=== leaf 151 صد وچپل وسه ماخذ مزدیسناو تأثیر آن‌در ادیات بادسی .محمدهمن. از انتشارات . دانشگاه :پر ان شمارة؟. جابشا نة دانشگام۱۳۲ شمسی. . (عمزدیسنا). ۷.- مسا لك المما لك.( کتاب). ابو اسحاق | بر اهیم بن‌مصدفارسی امطخری. لیدن. بریل ۱۹۲۷ میلادی. (-مسالك).. ۸- مصباحالارواح. اوحدی کرمانی. نغة خطی متعلق باقای احمد افش
=== leaf 152 مقدمه ۱ صد وچپل وچپار ۰ نصاب طبری- رك:شمارء ۱۶ . ۱ قشایس الفنون فیءر ایسالفیون. محدین محبود آملی . باهتمام میرزا احمد. نپران ۱۳۰۹ قمری. ۰ ۱۴۳ النقودالعر بية و علم النمیات. باهتمام اب انستاس 0 الکر ملی‌الیفدادی. قاهره۱۹۳۹ «یلادی (< نقود). ۴ نو دوز ناهه . من-وب‌بخيام . بتصحیح مجتبی مینوی.تهران . کتابخ
```


## [2026-09-06T16:07:58.008Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(180,340):\n    l=t[i]\n    if re.search(r'(?<!\\d)۱۱[0-9](?!\\d)', l[:400]) or re.search(r'(?<!\\d)۱۱[0-9](?!\\d)', l[-400:]):\n        print('leaf',i, repr(l[:120]), '...', repr(l[-120:]))\nEOF",
 "description": "Find BQT v1 printed page 112"
}
```


### [2026-09-06T16:07:59.724Z] TOOL RESULT

```
leaf 265 'و شین فرشت » بممنی در آوجخته باشد چه اندر\nآکیشید پمنی الدر آوشت - و چنکه درچیزی\nزده ودراز کردمرا نیز گویند.- وبمعنی دراز' ... 'فت نامه * .\n]له _ مخفف آگاه» رك : ۲گاه. آیاری - رك : آتش بهرام .\n۰ آگیبیفی - و آکیشبدن بممنی آویختن و پیچیدن . رك : کش .'
```


## [2026-09-06T16:08:15.668Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (320,325,330,335,340,350):\n    print('=== leaf',i, t[i][:180].replace('\\n',' '))\nEOF",
 "description": "BQT v1 leaves 320-350"
}
```


### [2026-09-06T16:08:17.369Z] TOOL RESULT

```
=== leaf 320 ار که واستر بشندند ودرعلف زارها (۱) سردهند تابچرد؛ و باین معنی نم اول و انی مشهور است ار کال -بکر اول و سکون ثانی با کاف بالف کشیده وبکاف دیگر زده » قطرباران (۲) کوچك‌را کویند که ن
=== leaf 325 << ۶+ )راد - یک اول بر وزن خبار » بن و تك آب را خوانند - و دستار را یز گویند - و هی چیز که بر پا یکشند مانند شلوار وتتبان و در عربی بممنی‌زن باشد که درمقابل هرداست- و بسمتي لنگی و 
=== leaf 330 اسپخحول بکسر اول و سکون‌انی و بای فارسی مکور و خای نقطه دار حضموم‌بواو ولام زده » بععتی‌پیخال است که فضله وافکند گی اسیر ۱ س با بای فارسی بر وزن مهتر» سپررا گونند و بعریی جثه خوانن
=== leaf 335 اسیندار هف ۱ - بش میم وسکون ذال نقطه دار. بروزن ومعنی اسفندارمن است که مام دواژدهم باشد از سال شمسی - و نام روز پنبم بود از حرماه شمسی ؛ و فارسیان این روز را درین ماء مبارك شمرند و
=== leaf 340 استرش -ایم اول و لت و قحرابم و سکون‌شین قرشت ۰ آنی راکوبند کهزمین‌را بدان شیار کنند . وسکون‌ثانی ونون وکاف فارسی» مردم کیاه باشد, وآن گیاهبت مانند مردم و نگونار بود ورسشة آن بجای م
=== leaf 350 اسکندروی و دختثر از دارا حامله بودوأنظهار نمیکردتابوی دهن‌اورا با اسکندروی که آنرا بفارسی سیر کوشد علاح کردند و مدازآن فرزند بوجود آعد او را لسکنتو منم نهلدند . و تلم «ادر او ناهید
```


## [2026-09-06T16:08:26.904Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in range(319,326):\n    print('=== leaf',i)\n    print(t[i][:1400])\nEOF",
 "description": "BQT v1 leaves 319-325 full"
}
```


### [2026-09-06T16:08:28.732Z] TOOL RESULT

```
=== leaf 319
سس سا
مشهور که افلاطون وضع (۱) کرده است ؛» و
ی گونند .ارغنون
ترجبة مزامیر است
بعنی جمیم ساز های
»؛ وبسنی دیگر
کرنند چرن هزار
آدمی از پبر و جوان ارغنون باریری ۷
همه پیکبار بآراز های مخالفبکدیگر چیزی
بخواد هد آن حات را
ارعنون خوانند » و
جمعی دمگر گفته اند
که ارغتون ساز وآواز
هفتاد دختر خواننده
و ماژنده است که همه
ارغنون دستی مك چیز را بیکبار و (۲)
پيك‌آهنگه باهم بخوانند و بنواژند .
ارغوان ی رت
پهلوان ۰ ممروف است و آن
بهار درختی باشد بفایت سرخ
ورنگین؛ طبیعت آن‌سرد وخشك
است اگراز بهارآن (۳) شربتی
ساژند و بخورند رفم خمار کند
و چوب آنرا بوزانند (4) ی
ابرو مالند » سیاه برآبد ومعرب
آن ارجوان ۴ است ؟ .
)۱ چش : آن .
)4( خم۳ : سوزند .
اراد
ادغون » بر وزن کردون » اسب تند
وتیز را کوند ۴ ,- و مخفف ارغنون هم هست
که ماز ممروف باشد ۵ . ۱
ارغیده « بر وزن غمدیده . ناه
وخشم آلود را کونند ۱ .
ار ان » با قاف بر وزن درمان . بلفت
رومی ۷ حنایی باشد که بر دست و پا بندند .
خوردن نیم متقال از آن قولشج را بکشابد .
گوند چون طفلی را ایدای ابله ی آوردن
باشد فدري ب رکف بای او صالند ایمن بود از
آنکه از (4) چشم او برآید » و باین معتی‌بجای
نون قاف هم بنظر آمده است - و بلفت فرب
الافصی نوعی از بادام کوهی است که آنرا
لوزالبربر کونند و روغن آنرا زیت الهرجان
خوانند .
ار قش بکسر قاف بر وزن ورزش »
بمعنی فهیده و کار دان باشد » و درجای دیگر
بجای فانی فای مقتوح ( ٩‏ ) نوشنه بودند بمعنی
ار لك - بفتح اول و سکون ثالی و کاف
فارسی قلمة کوچکی باشد که در مبان فلمبزر که
لاف وم زیت بو علایت مساق -
و بزبان علمی اهل ند اسمی است از اس
=== leaf 320
ار که
واستر بشندند ودرعلف زارها (۱) سردهند تابچرد؛
و باین معنی نم اول و انی مشهور است
ار کال -بکر اول و سکون ثانی با
کاف بالف کشیده وبکاف دیگر زده » قطرباران
(۲) کوچك‌را کویند که نرم باران باشد .#۶
ار گنج - بنم اود و سکون ثانی
و کاف فارسی مفتوح بنون و جیم زده ۰ نام
شهربت از ولات خراسان که در سرحد ماوراه
النهر واقع شده است .
اد کو تن - با نون و تای فرشت
وزن بهلو شکن ی 12۳
بخشیدن و بخشاش باشد ‏ .
اد کی ه بر وزن اصفیاء جوی آب را
گویند بلفت زند و بازند (۳) ۴ .
اد « پکر اول و فتح ثانی و سکون
میم » نام شخصی است (4) که ساز جنکه (ه)
را وضع کرده است - و دد عربی نام بهشت شداد
است - و شانة کیر را قیز گوید .
3 قاط انیم ی مین بلط بات
اهل یمن درخت کایی‌را کویند و آن درختیست
مانند درخت خرما و کاو ی کل آن درخت است »
در نهایت خوشبوبی و آن در ملك دکن بسیار
است .
ار ماس « نم طای.حطی و سکون
)۱ خم. ۳ : علفزار .
(4) چش : - است
)۷( خم ۳ : نهایت .
م۰٩‏
سین بی قطه » نام ,مکی آزپادشاهان بونان است
کویند کل مخنوم در زمان اوبپمرسید وصورت
.او را برآن. نقش میکرده اند .
ادعال ‏ بر وژن پرکال ۰ بلفت یمنی
(٩)چوبی‏ است شببه بفرفه درغایت (۷)خوشبوبی
و قرفه چوبی است شبیه‌بدار چینی » خوردن‌آن
ار مان پنتح اول بر وزن فرمان »
بمعنی آرزو و حسرت باشد ؛ چه ارمان خور
حسرت‌خور ندسرا کوند - و رنج بردن وپشیمانی
و دریغ و افوس دا نیز گفته‌اند - و نوعی از
دارو باشد که بوی آن ببوی فرفه ماند » وبیخ
دندانرا سخت کند - و بکسر اول هرچیز که‌آن
پعاریت باشد - و نام شهر (۸) و مدینه‌ای هم
هت .
ار ما لین » بروزن ترسانیدن » بممنی
آرزو و حسرت 
=== leaf 321
سب ۱۰۵ تت
ضحاك می فرمود بکشند و مغز سرایشالرا بجهت
مارالی که از کتف او برآهده بودند حاضر
سازند ء يك‌فررا آزاد میکرهد و میگریزانیدد
و بجای مفز سر او مفز سر کوسفند داخل می
لمودند . و گوبند کردان صحرا نثین از دل
آلجمات اند .
ارمز پشم أول بروزن هرمز . نام
روز اول است از هرماه‌شمسی - و نام فرشته‌است
که امور و مصالح روز ارمز بدو تعلق دارد- و
نام سثار؛ مشتری است - و نام پسر اسفندیار
ین
ارمن
که ادرس بیغمیر باشد و اورا هرمی هرامه
ليز کویند . ۱
ار هغان « باغین شقطمدار بروزن‌پپلوان,
نحفه و سوغانی را کورند ۴ که چون از جابی
یایند بجهت دوستان بطریق ره آورد (۷)یاور ند
و آن را ارعفاتی بر وزن لن ترانی هم گویند ,
و ضم ثالث بر وزن مردمان هم اشتقت اد
وآنرا بعربی‌عراشه خوانند - ودرم و دیتار رالیز
کته
ار مك بشم اول‌بروزن‌اروك» پشمینه‌ای
باشد پوشیدلی .
ارمز است که نام ستار مشتری - و نام روز اول
حر ماه - و لام یس اسفتد بار (۱)- و نام فرشته‌ای
باشد .
آرمس - بر وژن و حعنی هرهس است
(۱ چش : اسیندبار . )۱( خ ۳ ؛ راه‌آورد .
۱- اوستا ۸12208۷ ۸۷۲2 . پارسی باستان ۸۲2۳8280 . پهلوی
0 :, در فلرسی هرمزد (ختح میم) . هرمزد (بضم میم) » اورمزد » هورمزد , هرمزهم
آمده . نام خدای مزدیسنا , مر کب از اهوره در اوستا و ۸511۳۵ در ساسکریت از ريش 250
ساتسکریت و لا20 اوستا بمعنی سرور و مولی « دارستتر . زند اوستا . ج ۱ ص ۲۱-۲۰ > ؛
مزدا در اوستا « بسنا 4۰ : ۱ بمعی حافظه آمده . در کانها ( بسنا 4۵ : ۱) یمعنی بخاطر
سپردن وبیاد داشتن است . این کلمه در سانسکریت صورت 126025 بمنی داش و هوش است »
بنابراین چون‌با اهوره استعمال شود ازآن معن
=== leaf 322
ارمند
زلایتی‌است از کوهستان آنربابجان و مولدشیرین
مشهور آبجا بوده و ابریشم ارمنی منسوب بدانجا
است - و مخثف اگر من باشد در محاورات ؛
وبنعنی اول بکسر اول هم .کفتهاند .
از من « بروزن‌فرزند , مخففآرمیده
مند است یسی صاحب آرام و آرام گرنته .
از هنفه - بر وزن شرمنده » بمعنی
ارمنده.است که آرمیده و آرام گرفه باشث .
آزهنین « بر وزن مدجبین ۰ نام پس
لشطی بن‌بویان است - وبلفت رومی انار صحرابی
را گویند و بعربی رمان البری خوانند ؛ ویضی
درخت انار صحرایی را کفتداند ؛ و بضی گونند
قاف اول مکسور و ثانی حفتوح .
از هنيه » بکس اول » شهر ست‌معروف
کهآ تشکده درخش ۱ در آفجاست .گویند بانی
ارمنیه وشیراز ۴ و آتشکد؛درخش, رای‌مجوسی
۴ بوده که الحال براس‌البقل مشهور است؛ ودرهم
بغلی منسوب بیاوست .
ار مود بر وزن و معنی امرود است
و آن میوه‌ای باشد حمروف * .
اد هون ه بر وزن گردون ء زری‌باشد
که پیش از کار کردن بمزدور دهند وآنرابمبی
عربون و اربون خوانند ‏
(۱) چك : ژند ویاژند .
کرفن باشد ۵ .
ار هیا - بنتح اول یوذن انبیا. ام یکی
از پیغمبران بتیاسرالیل‌است ۷ -ونام ریفس
سو نام حترت‌علی علیه‌السلام نیز حست - و نام
بیت‌المقدس + و نام بلیان (۲) بن ملکان باشد»
ویضم اول وکسر اول هم بنظر آمدنة است .
از مك - بر وزن فهمید . مخفف آرمید
است که ماضی آرمیدن باشد بعنیقرا گرفت
و ساکن شد .
از میفه ۰ بر وزن فهمده مخقف
آرمیده است که قرار گرفته و ساکن شده(۳)
باشد .
از هین « پروزن پروین ؛ نام پسرچهارم
برادر کوچك کاوس باشد .
ار هیا » بر وزن مهسیما » بلف‌سریانی
موشادر باشد و آن چست مانند نمك و یشتی
سفید کران بکاربرند و بسنی کویند ,بونانی‌است
=== leaf 323
از یا
وجیم. , بمعنی آرنج است ت که بندگاه ساعد
وبازو باشد وبحربی مرفق خوانند .
ار ندان بر وزن‌قلمدان 4 يو
و حاشاً باشد .
ار نوار بنثح وأو بر وزن سی فراز »
نام خواهر جمشید است که با خواهر دبگرشهر
از در حبالهٌ ضحاك بودند و عاقبت بفربدون‌متفل
شدند .
ادن لیر - با بای ابجد و زای فارسی
بر وزن الم یجد , چوب بقم را گویند که بدان
چزها رنگ کنند و آزرا تبرخون هم خوانتد
ومعرب آن طبرخون است ؛ و بعضی بتقدیم بای
ایهد بر بای حطی بر وزن سحر خی زگفته اند .
ار و4 ه بر وزن پروانه , نام کلی
است که آنرا خیری صحراب یگونند. چون‌قدری
از آن بخو رکنند هر بزی بدی و گنده‌ا ی که‌دز
جابی باشد برطرف کردد (۱ ) و زابل شود -
ونوعی آزشتر هم‌هست .
زند واوستا بمعنی ۳3 ۳ ی ۰
اروس - بنتح اول و ثالك مجهول
بر وزن عروس , متاع و اسباب و کالا را گوشد.
ارو تن - با فوفانی بر وزن سبوشکن
بت زند و پازند )٩(‏ بسنی شتن باشد ۴ .
و آرونمن ,یعنی بشویم من ؛ واروئید بعنی بشوئید
)۱ خم ۳ : کند .
لاتننی( فرانسه 2۴066 ) درپهلوی ۷۳۷۵۲ .
شما. که امر بشستن باشد .
ارو ثف ۴ « بر وزن ومعتی الوند است
و آن کزهی باشد درنواعی عمدان . کگویند
شخصی در آن کوء آسوده است که نام او اروند
بوده و آن کوه را بنام او خوانشد - و دربای
محیط - و کر آب - و دجلهةٌ بغداد را یز
کفته‌اند؟ - ونام چشمه‌ایست درسیستان . کوشد
نی سیباری درآن چشمه روبده استآنجه ازآن
ت منگه شده است و آنجه در
سرون آب است و از آب بر آمده است نی‌است
درهبان آب اس
و شاخ و ب رکه دارد - و بمعنی حسرت و آرزو
هم آمده است - و فر و شکوه و زیبایی را لیز
گویند - و بممنی تجربه وآزمایش حم هست .
و تام پدر لهر
=== leaf 324
ارء جان
اره‌جان با ثاتی‌هشدد و جیم بروزن
پهلوان » نام شهری است که ما ین آن شهر
وش رازشصت فرسنکه واه است وا ترا هوام‌ارمغان
خوانند باغین نقطه دار .
ار هفت- باها بروزن زریفت ۰ یکی از
پیغمبران‌است باعتقاد کفرء هند؟ . وایشان شش
طایفه‌اندهمه فایل به تناسخ . گویند چپار عزار
ارهفت‌خواهد آعد ود ازآن آفربنش لوف
خواهد شد .
ار هنگ- بروزن فرهنگه . نام صبف
ایست از بدخشان . و درآن قصبه زبارنگاهیست
وماعتقادمردم آ نجا سرامام حسین علیه‌السلامدر] نجا
ار یب - نم اول و کر ثانی و سکون
نحتانی مجهول و بای ایجد . بمعنی محرف
و کج باشد و تی کان قیقاح گویند .
ار یحا - بر وزن مسیحاه ام دهی است
در ولات شام .
از بد ور لت ع بکسر اول ونانی‌وسکون
ثالث و دال و کسر بای
آبجد و رای قرشت
و تحتانی ساکن ودال
دیگر » اين لت از
توأبع است و بمعنی
دوابی باشد مانند بباز
میان‌شافته وازس-تان
آرند . بر بواسیر طلا
کنندتافع باشدوخوردن
آن زنانرا خون حیض
1 آرید برردد
ار یس با تحتانی‌مجپول بروزن ائیس:
بمعنی‌زبرلك و هوشیار باشد- ودرعریی بممنی‌متابع
آضفته اسب وگن ارل وئانی شدد هم درعرمی
مزارع و زراعت کننده را گوبند .
ار یش « بر وزن کشیش , بمعنی‌اول
ارس است که عاقل و زبرك و هوشیار باشد .
ار هاگ -_ بر وزن شريك , بلفت زند
و پازند (۱) بمعنی دور است که درمقابل نزديك
باشد ۴ . # 1
بقه ازصفحهٌ ۱٩۱۱‏
خانوادژ ۲1500065 که درآ بهای گرم فراوانت
٩016 16 ۲‏ ( از : مپندی فریدیا)
وخوابگاه نیکو. « خس * .
( برهان قاطع ۷)
=== leaf 325
<<
۶+ )راد - یک اول بر وزن خبار » بن
و تك آب را خوانند - و دستار را یز گویند -
و هی چیز که بر پا یکشند مانند شلوار وتتبان
و در عربی بممنی‌زن باشد که درمقابل هرداست-
و بسمتي لنگی و لنگ فوطه هم حست .
ار ار با یکسر اول و رابم و بای
قرسی باه کنیده , شلور و یبا گویند .
از ارو ‌ِ ۳ اول بی وت گل
حم گفته اند .
از از ۵ بن: بغنح اول و ثالی بالف کشیده
09۳ 7
از یر مه بای ایب بر وزن جش ؛
بیاد گرفتن و بخاطر نگاهداشتن باشد » و بعربی
حفظ گوبند ,
از بر کاد شدن ح«رابای‌فارسی, کنابه
از بخودی و ی اختباری و انطراب کردن
باشد .
اه بر بی وزن س گرم . سعنی
است که کنابه از طوع و رضاو رغبت و از ته
دل ومکنون خاطر باشد» غایتش ازی نگو شکنابه
ازته دل شنیدن باشد» وازین دندان کنابه ازته دل
گفتن - و کنانه از ذخیره و جمم‌شده هم‌هست.
ك ره : ار .
سمعنی أز
آز بن سی وف - بسنی اژین‌دسان
است که کنابه از رضا و رغیت و از قه دل
و طیب خاطر باشد .
از بی سی ودو ۵ندان- بسنی
از بن سی و دو است که کتایه از طوع و رضا
و رغبت باشد .
از بن "وش « کابه ازکمالللات
و بندکی و خدتکاری از ته دل و مکنون‌خاش
باشد .
از یی ناخی ت کابه ‏ از فخیره
وجمم شدء باشد - و کنابه از اطاعت و بند کی
و ته دلی هم ست .
از پوست بر ]هت - کابه از
کثف راز و احوال خود کردن - و ترگ دیا
نمودن و از خودی و ضانیت باز آمدن -
وخندان بودن - و بمقصود رسیدن باشد .
از یر » بروزن تقصیر » بمعنی ازبرست
که بیاد گرفتن و حفظ بالد - ۰
از خ - بر وزن ملخ ۰ دندانهای سخت
باشد که از بدن آدمی بر آبد و درد تکند
و آبرا بعربی تژلول کویند ۱ .
از حر افتادن - کنابه از مردن
واز عالم رفتن باشد .
```


## [2026-09-06T16:08:45.819Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('=== leaf 328'); print(t[328][:600])\nEOF\necho \"############ v2\"\npython3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nfor i,l in enumerate(t):\n    if 'چکوچ' in l or 'چاکوچ' in l:\n        print('leaf',i)\n        j=max(l.find('چکوچ'),0)\n        print(l[max(0,j-500):j+700])\n        print('-----')\nEOF",
 "description": "BQT v1 leaf 328 and v2 chakuch"
}
```


### [2026-09-06T16:08:47.746Z] TOOL RESULT

```
=== leaf 328
اراد
باشد ٩‏ - و کنابه از مردم شجاع و قهرآلود حم
هت - ورایت و سرعلم را نیز گوبند ۴ -
وپادشاه تال و ححاك ماراترا هم گفته‌اند ۴ .
ادها « با کاف‌معنی آخراژدهاست
که نحاك ماران باشد ۴ .
اژدهای فلك - اثارء بشدنین رأی
و ذنب است - و تلی‌را نیز گویندکه ازجلهة
چهل و حشت صورت فلك باشد ٩‏ .
ارم خح اول و سکون انی و غن
نقطه دار , شاخهابی را گویند که از درخت بریده
باشند و بعربی جلمه خوانند٩‏ .
ار کان با کاف‌بروزن دربان ؛ بمعتی
مردم کاهل و باطل و مهمل و بیکار باشد .
باگد شبکه دار که ازیس آن نگاه توان کرد .
۱
ظ
از گهی -باها پروزنک رکدن : بمعنی
از کهان است که کاهل و باطل و مهمل وبیکار
بش
۸ ۰
آز لد - بفتح اول و 
############ v2
leaves 684
leaf 109
      ‫ر‬                            ‫‪ :‬چکاد ‪.‬‬   ‫رک‬     ‫‪-‬‬   ‫‪۴‬‬

  ‫‪ - ۷‬ركه‪ :‬چفتك‪.‬‬           ‫ول ‪ -‬وز رك‪ :‬چکلچك‪.‬‬              ‫‪ - ۴‬امروز» ‪ -‬عاذ گوبند‪-: ۵ .‬‬
      ‫‪« -‬چکری ربواس بود» «لفت فری ‪۲۲6‬‬                           ‫‪ 4#‬لغتی در «چکه ‪.«( €‬م‪).‬‬
                    ‫‪ — ۰‬اردو«چهو کری» (دختر) «فرحاك انگلسی باردو عبدالحق‪lriG„ :‬‏‬
        ‫‪.‬‬    ‫چکس‬     ‫‪:‬‬   ‫رکه‬    ‫‪۴‬‬         ‫ا کا کان‬                      ‫‪ :‬چکه‪.‬‬          ‫ا‬
   ‫چکوچ‪.‬چاکوج ‪.‬‬                ‫‪:‬‬
                               ‫هر‬‫ک‪-‬‬
                                  ‫‪۵‬‬          ‫(یوند مصدری)‬        ‫ن‬
                                                                 ‫د‪۳‬‬‫بم‪).‬‬
                                                                      ‫‪ -‬از‪ :‬چکی (ه‪.‬‬

-----
leaf 110
   ‫‪0‬‬      ‫ی‬

                                                      ‫اول وثانی» بروزن رمعنی‬                       ‫جک‬

                                                      ‫‪ ۱‬و باین ‪۰‬عتی با‬     ‫باشد‬   ‫استت که کنجشك‬           ‫جنك‬
 ‫جکوچ ‪ = ۳‬بفتح‌اول وثانی‌بواو کشیده‬
                                                      ‫کاف فارسی همآمده است ‪ -‬وبند و طناب (‪)۱‬‬
‫وبجیم فارسی زده ‪ ,‬افزر اری باشف سر تفر و دسته‬

 ‫دار مر آسیاباتراکه بدان آسا را قز کنند ‪-‬‬            ‫ابرمشمی را فیزکویند ؛ و باینمعنی بقتح ثانی‬
                                                                                                 ‫همگفته‌اند ‪.‬‬
 ‫وبمعنی تیز کردنآسیا هم هت ؛ وبجای حرف‬
‫انی 
-----
```


## [2026-09-06T16:08:58.442Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint(t[110][:3000])\nEOF",
 "description": "BQT v2 leaf 110 full"
}
```


### [2026-09-06T16:09:00.471Z] TOOL RESULT

```
   ‫‪0‬‬      ‫ی‬

                                                      ‫اول وثانی» بروزن رمعنی‬                       ‫جک‬

                                                      ‫‪ ۱‬و باین ‪۰‬عتی با‬     ‫باشد‬   ‫استت که کنجشك‬           ‫جنك‬
 ‫جکوچ ‪ = ۳‬بفتح‌اول وثانی‌بواو کشیده‬
                                                      ‫کاف فارسی همآمده است ‪ -‬وبند و طناب (‪)۱‬‬
‫وبجیم فارسی زده ‪ ,‬افزر اری باشف سر تفر و دسته‬

 ‫دار مر آسیاباتراکه بدان آسا را قز کنند ‪-‬‬            ‫ابرمشمی را فیزکویند ؛ و باینمعنی بقتح ثانی‬
                                                                                                 ‫همگفته‌اند ‪.‬‬
 ‫وبمعنی تیز کردنآسیا هم هت ؛ وبجای حرف‬
‫انی لام کهفمته‌اند ‪ -‬و چکش استادان مسکر‬                       ‫و‬              ‫‪A‬‏‬              ‫حکله ‪-‬‬

                        ‫وگزرر(‪ )۲‬را قکیوزنند ‪#.‬‬        ‫بحکد ‪ -‬وقطره وچکسن‌را‬
                                                                           ‫مطل آله از جابیب‬


 ‫چکو لش ‪ -‬بنتماول و واو مجهول بر‬                                                        ‫تکيوزبند ‪* . ۴‬‬
‫وزنمکوكد» تامکاحی |ست کهآ برا خرفه کوند‬
‫و پمربی بقلةالحمقا خوانند ‪ --‬چوكاوك را بير‬             ‫و میم بتحتانی رسیده وزای نقطه دار مفتوح‬
‫لهملیم باشد ‪ - ۷‬و مضی کویند‬    ‫ب‌اوندا ک‬
                                       ‫اته‬
                                         ‫گف‬            ‫که مول آ«می وحبوانات‬           ‫بکاف زده ‪٠‬‏ مر ی ات‬

 ‫که پرنده‌ایت که آ را سرخاب میگوند ‪- ۷‬‬                 ‫دیگرقطره قطره میچکد؛ رواآبعربیتقطیرالبول‬
 ‫ونام‌نغمه ابت از موسیقی‪ - ۸‬و نم اول بمعنی‬                                                             ‫خوانند ‪.‬‬
                                   ‫کنجك باشد ‪٩‬‏ ‪.‬‬
                                                       ‫س بفتح اول کورانی وسکون‬                   ‫چکن‬
‫چکه‪ -‬بنتح اول و انی مشدد » بمعنی‬                        ‫نون» نوعی‌از کشیده وزر کش دوزی وخهه‌دوزی‬
  ‫ورد‬
    ‫قطره باشد ‪*٩-‬‏ وبا ثالی‌غیر مشدد کوچك خ‬            ‫باشف‬   ‫دوخنه‬    ‫و حامه وقبابی را که چنن‬           ‫باشد ‪-‬‬

                                    ‫را (ک‪۳‬و)ند‪. ۱۱‬‬    ‫چکی دوزی کوبند؛ وبکسراول وثانی همآمده‬
  ‫(‪)۳‬خم ‪ ۳‬چش ‪ :‬خورد را ‪.‬‬                ‫(‪ )۲‬چش‪ :‬زر کران را ‪.‬‬          ‫(‪ )۱‬چش ‪ :‬بند طناب ‪.‬‬
                                           ‫‪ - ١‬رک ‪ :‬چنك‪ .‬چضو ‪ ,‬چنو که » چکوکت‪: ‎‬‬
               ‫ور باشه‌ای سوی بطان مپر ‪.‬‬
                                       ‫ک‬                      ‫اکر بازی اندر چگك کم نگر‬
          ‫بوشکور بلخی‪«.‬لفت فرس ‪.*۲۷۲‬‬
                                                               ‫چکره ‪.‬‬      ‫چك‬    ‫رکه ‪:‬‬       ‫‪- ۴‬‬

   ‫‪.‬‬    ‫چکن‬    ‫‪:‬‬   ‫رک‬   ‫‪ - ۴‬از ‪ :‬جك (چکیدن) ‪ +‬میز(هم) ‪ +‬ک (یسوند) ‪.‬‬
                        ‫‪-‬‬    ‫‪۴‬‬


 ‫‪.‬کش ‏ درتر کیع وت «چکوش» بمعتی‌ابزاری فلزی که‬    ‫ر‪-‬ک ‪:‬کچواج چ‬    ‫®‬
             ‫رد چ‪:‬کاوك ‪.‬‬    ‫‪۱‬‬         ‫‪۳۱‬‬                   ‫کار کران بکار برند‬
       ‫‏‪ ٩‬رك‪ :
```


## [2026-09-06T16:09:24.544Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN 597 area\"; python3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\ni=597+24\nprint('=== leaf',i)\nprint(t[i][:900])\nEOF\necho \"== FRS page for chakad\"; python3 - <<'EOF'\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/FRS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i,l in enumerate(t):\n    if 'چکاد' in l:\n        print('leaf',i, l[:200].replace('\\n',' '))\nEOF",
 "description": "Buck 597 and Asadi chakad page"
}
```


## [2026-09-06T16:09:24.771Z] TOOL CALL #57: WebSearch

```json
{
 "query": "Greek \"ἀρίκοιτος\" OR \"arikoite\" bed word attested LSJ"
}
```


### [2026-09-06T16:09:26.329Z] TOOL RESULT

```
== SYN 597 area
leaves 1545
=== leaf 621
NG iabere Dan. flaa ChSl.  (dirati)
c pears Sw. jld SCr. — derati, guliti
Ie Pier OE fléan, hyldan Boh.  dfiti
4 . — desollar ME fle(n) _ Pol. —zdzieraé, tupié
male jupui NE flay, skin Russ. _ sdirat’
Ir. fennaim Du. villen Skt. bso
Nir. feannaim OHG scintan, fillen Av. vi-nad-
W. — blingo, digroent MHG _schinden, villen
Br. _—digroc’henna NHG - schinden, hiuten
Words for ‘flay’ are mostly from roots seen also in words for ‘tear’ or ‘peel’ or are derivs. of words for ‘skin, hide’.
Secondary uses, as ‘flog, despoil, plunder’, etc., are widespread, and in some languages ‘flay’ in the old literal sense 1s Now more commonly expressed by new derivs. of words for ‘skin’ (so od not flay, in common use), or by ae fe them (Russ. sdirat!
‘oat, ete.), though such phr. entered in the the, phrases are not 1. TE *der- in d ‘ oa words for ‘flay’ and a ee 1.797 ff. ay’ : Grk. 3¢ ith 6¢ Honk felts 7 €pw 
== FRS page for chakad
leaf 125                                      ‫‪۹۰۱‬‬        ‫ت‪]۱‬‬    ‫‪۱‬‬                               ‫|حرکانش همه ره هثر است‬                                                       ‫بسیار باشد [ رو دکی گ
leaf 333                                       ‫‪۳۱‬‬                                         ‫تویل"‬                                             ‫پیش پیشانی بود [ غواص گوید ‪:‬‬                           ‫و ر
leaf 337                                         ‫‪۳۸‬‬                                          ‫چال‬     ‫مرغی بود چندزاغ[ وطعمکوشتش چون کوشت بط باشد عماره گوید‪:‬‬ ‫ال ‪۱‬‬    ‫چو‬‫یاکندهمه‌وادیش را بببط‬
```


### [2026-09-06T16:09:33.716Z] TOOL RESULT

```
Web search results for query: "Greek "ἀρίκοιτος" OR "arikoite" bed word attested LSJ"

Links: [{"title":"bed - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/bed"},{"title":"κοῖτος - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%CE%BA%CE%BF%E1%BF%96%CF%84%CE%BF%CF%82"},{"title":"κοίτη - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/%CE%BA%CE%BF%CE%AF%CF%84%CE%B7"},{"title":"Learn Ancient Greek - Ancient Greek (LSJ)","url":"https://lsj.gr/index.php?title=LSJ%3ALearn_Greek&mobileaction=toggle_view_desktop"},{"title":"LSJ:GreekEnglishLexicon - Ancient Greek (LSJ)","url":"https://lsj.gr/wiki/LSJ:GreekEnglishLexicon"},{"title":"LSJ","url":"https://lsj.gr/wiki/Main_Page"}]

The search results show various Greek words for "bed" in the LSJ (Liddell, Scott, Jones Lexicon), including κοίτη (koitē), κοῖτος (koitos), κλίνη (klinē), λέκτρον (lektron), λέχος (lechos), and εὐνή (eunē), but they do not contain any results for the specific word "ἀρίκοιτος" (arikoitos) or its variants. 

The search did not find this particular word in the LSJ. It's possible that:

1. This word may be extremely rare or attested only in fragmentary sources
2. It may be a hapax legomenon (a word attested only once)
3. The word may not be included in the standard LSJ dictionary
4. There may be variant spellings or forms that need to be searched differently

If you're researching this word for an academic purpose, you might want to consult:
- The full LSJ text directly on their website
- TLG (Thesaurus Linguae Graecae) databases
- Specialized papyrological or epigraphic resources
- Academic articles on rare Greek vocabulary

Would you like me to try a more specific search variant?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-06T16:09:43.901Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"9\\.47\\|HAMMER\" SYN.txt | head -10",
 "description": "Buck hammer section"
}
```


### [2026-09-06T16:09:43.943Z] TOOL RESULT

```
8096:Lett. laisks : laist ‘let go’, etc., Lith. leisti ‘let, permit’ (: Goth. létan, ete., above, 4; see 19.47). Miihl.-Endz, 2.411,
13319:k’, Swiss ferch ‘oak wood’ (Weigand-H. 1.566); CHG furha, etc. ith shift to ‘pine’ or “fir (8.64, 8.65), also Goth. fairgunt, OE firgen ‘mountain’ (1.22). Walde-P. 9.47 ff. Ernout-M. 838. Lat. rdbur, a special kind of oak (as It. rovere, Fr. rouvre, but Sp., Port. roble generic ‘oak’), early form rdbus (whence rabustus ‘of oak, hard, strong’), named from its reddish heart-wood, and with dial. 6: Lat. ruber ‘red’, etc. Walde-P. 2.358. Ernout-M. 867. fr. chéne, OF. chaisne (influenced by fraisne, fréne ‘ash’), chasne, fr. a Gall. ee (orig. Celtic?). REW 1740. ee eae ff. Gamillscheg 215. oe ; stejar oak’ beside steajer ‘pole, Gee a ne floor), fr. parallel alederi ae ae Slavic word, Ch&l. hayrick Pati ae aaa pole’ (of e ae , SCr, stozer ‘doorpost’ ee, with Rum. shift fr, eae oe 0 ae Tiktin 1490, Bees Me No trees, used pene where there ; r ‘tree’) : Grk. alyi-
13511:9.44 9.45 9.46 9.47 9.48 9.49 9.50 9.51 9.52 9.53 9.54 9.55 9.60 9.61 9.62 9.63 9.64 9.65 9.66 9.67 9.68 9.69 9.71 9.72 9.73 9.74. 9.75 9.76 9.81 9.82 9.83 9.84 9.85
13516:Saw (sb.) HAMMER
14959:OE prawan ‘twist, turn’ (NE G draen id. (NHG drehen), t *ter- (*tré-, etc.), perh. h a rotary motion’, ‘orsent development to ae whence ‘bore’, the ee most ly in Grk., but also in Lat. terebra ‘auger and the Celtic words for ‘suger’ (9.47). From an extension of the same root also Grk. rpfw ‘wear out’, rpiraw ‘bore’, rpbravov ‘auger’, Lith. trupéti ‘break in pieces’, etc. Walde-P. 1.728 ff.
14965:Sp. taladrar, barrenar, derivs. of taladro, barrena ‘auger’ (9.47).
14974:Pol. swidrowaé, Russ. buravit’, sverlit’, derivs. of Pol. swider, Russ. burav, sverlo ‘auger’ (9.47).
14981:594 SELECTED INDO-EUROPEAN SYNONYMS 9.47 AUGER
15039:9.49 HAMMER (sb.) Grk. cdipa Goth. ba Lith plaktukas (kujis) NG odupl ON hamarr Lett. dmars, veseris Lat. malleus Dan. hammer ChSl. mlatit It. martello Sw. hammar(e) SCr.  tekié Fy, marteau OE hamor, bytl Boh.  kladivo Sp. martillo ME —hamer Pol. = mlot Rum. ciocan NE hammer Russ. molot Ir. ordd Du. hamer Skt. mudgara-, ghana- NIr.  castir OHG  hamar Av. (€akus-) W. morthwyl MHG hamer Br. morzol NHG hammer
15085:MIr., NIr. tairnge: Gall. tarinca, taringa ‘iron spike’, fr. the same root as Ir. tarathar ‘auger’ (9.47). Marstran- der, Festskr. til Alf Torp 242 f.
```


## [2026-09-06T16:09:45.236Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('FRS_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nl=t[333]\nj=l.find('چکاد')\nprint(l[max(0,j-800):j+900])\nEOF",
 "description": "FRS chakad entry"
}
```


### [2026-09-06T16:09:47.240Z] TOOL RESULT

```
      ‫و روی برکردار یل‪۴‬‬           ‫وریل‬
                                                         ‫قس‬‫پشت خول" و‬
‫ساق چون سومان و دندان بر ال دستره ]‬

                              ‫داهل و داهول *‬
 ‫علامتهاست کهبزمین کنند و دام بگستر انندکه تخجیر از دا هل بترسد و‬

                                                  ‫بدام افتد [پوشکور رید ‪:‬‬
    ‫گوبی‌زدامو داهل جستستم |‬                 ‫موه نیافتستم کایدونم ‪0‬‬


                                      ‫‪7‬مر‬
 ‫نشکنج بودعنی بدوانگشت گرفتن و بدوناخن فذردن بود و بتازی قرض‬

                                                     ‫خوانند[ آغاجی گوید‪:‬‬
‫رواست باری گردل برد مونس داد ]‬              ‫نمان نخحل دارم زدوست بربازو‬




 ‫‪ - ۱‬ن ‪ ۰‬تویل‌یش بشانی‌بود سوی‌جکاد چم‪ .‬توبل‌يش‌بيشاني گاهازبالاسویعیان‌سر بود‬
 ‫‪ :‬تویل‬    ‫و چکاد نیز همین باشد و تازی چون آنجا موی نرود اصلم خوانندش ‪ ۰‬س‬
‫‪ - ۳‬چ ‪ ۰‬قیر‬      ‫‪ _ ۲‬س ‪:‬کگوژ» چ ‪ :‬خوهل‬        ‫بشانی باشد از اثراز سرچون چکاد‬
 ‫سند و قصد دام‬
             ‫ء ‪-‬ل ‪ :‬داهول علامتها بود که بر زمین زاند تا تغجی‌ها از آن باهر‬
‫کنند داهل‌نیز خوانند چ ‪ .‬دامل‌علامتهاست که برزمن فرو زنند وازیراودام بگتر انند‬
 ‫تخاجیر از داهل بترسد و بدام آهنك کند و در دام انتد »س مثل چ فقط ‪ « :‬اندر‬
 ‫نخجل آن‌چیز‬     ‫‪٩‬‏ ‪-‬ن‪:‬‬    ‫‪ - ۰‬چ ‪.‬ک چونبنم ‪۰‬‬        ‫پزنند » بجای «فروزنند» ‪.‬‬
 ‫است که بسردو ناخ نگیرند » چ ‪ :‬تخجل نشکنج باشد و گویند ناخن بر گرفتن بود؛‬
 ‫س ‪ :‬نخجل‌نشکنج بود وبتازی فرض خوانند یعنی‌بسرناخ نکسی‌را گرفتن‌بود وفشردن‬
 ‫؛ تشبیل‬   ‫‪ ۰‬نشسل شست ماهی بود » س‬    ‫‪۷-0‬‬     ‫شتر دوستان بابکدیگر کنند‬    ‫وان‬
‫شستهاه یگب بود» ‪ ۰‬نشپیلآ هن‌بارءباشد که برسرهوی اسببندندوبدان‌ماهی گرند‪.‬‬
```


## [2026-09-06T16:10:04.307Z] TOOL CALL #60: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱey-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tḱey-\" \\\n \"https://en.wiktionary.org/wiki/أريكة\" \\\n \"https://en.wiktionary.org/wiki/چکش\" \\\n \"https://en.wiktionary.org/wiki/چاقو\" \\\n \"https://en.wiktionary.org/wiki/چکاد\" \\\n \"https://www.etymonline.com/word/hamlet\" \\\n \"https://www.etymonline.com/word/Henry\" \\\n \"https://www.wisdomlib.org/definition/coka\" ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 249 verification (roots Kei 4 / Keku): $u\" 2>&1 | tail -2\ndone",
 "description": "Archive web sources"
}
```


### [2026-09-06T16:10:09.464Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/157c56c3f0a4fc36.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b71c6b2a24d4efe3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/35745a4f20f781b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9947c1305180ded4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c2c684dc0a3faa39.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b3175cc86b6116d8.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/509e52454bc94b92.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec1e5ec3e0b4e3fb.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a85f291e06611160.txt
```


## [2026-09-06T16:11:01.538Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification && python3 - <<'EOF'\nimport json,glob\nfor f in sorted(glob.glob('page-2*.json'))[-8:]:\n    d=json.load(open(f))\n    for e in d['entries']:\n        for n in e.get('nodes',[]):\n            if not n.get('words'):\n                print(f, n.get('id'), n.get('verdict'), '|', (n.get('derivation') or '')[:200])\nEOF",
 "description": "Convention for empty nodes"
}
```


## [2026-09-06T16:11:02.722Z] TOOL CALL #62: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Hamlet",
 "prompt": "Etymology of the English given name/surname Hamlet, and of Shakespeare's Hamlet — is it from Old Norse Amlóði/Amleth, or from Old French Hamelet (diminutive of Germanic Hamo, from *haim 'home')?"
}
```


### [2026-09-06T16:11:03.387Z] TOOL RESULT

```
page-239.json 5 plausible | Empty pass-through box. Two Latin forms actually fill it, and they belong to the two different words of node #4: Medieval Latin sandalum/santalum 'sandalwood' (Etymonline s.v. sandalwood: 'from Mediev
page-239.json 6 confirmed | Empty pass-through box = Old French sandal / sandale. Etymonline s.v. sandalwood: English sandell (late 14c.) 'from Old French sandale, from Medieval Latin sandalum'; Klein s.v. sanders: 'OF. sandre, 
page-240.json 1 confirmed | Empty pass-through box: the word Nourai means is Syriac ܟܢܘܢܐ (kānūnā) 'brazier, hearth', borrowed from Akkadian kanūnu with the regular Aramaic determined-state ending -ā. Aramaic and Akkadian were i
page-240.json 2 confirmed | Empty pass-through box: Arabic كانون (kānūn), pl. كوانين, 'brazier, fire-pan, hearth', borrowed from Syriac/Aramaic kānūnā, not from an Arabic root (there is no Arabic root k-n-n that yields this shap
page-240.json 7 confirmed | Empty pass-through box: Arabic قفص (qafaṣ) / قفس (qafas) 'cage, coop'. It came in from Aramaic/Syriac ܩܘܦܣܐ qup̄sā, ܩܦܣܐ qap̄sā 'cage, box' — Addi Shir's entry cites the Syriac form and Fraenkel — whi
page-240.json 10 confirmed | Empty pass-through box standing for the French continuations of Latin capere and capsa: chasse 'frame, reliquary' and its derivative châssis 'framework', caisse/casse 'case', câble 'cable', capsule (a
page-242.json 20 confirmed | An empty pass-through box standing for French démocratie (attested 1370s in Oresme's translation of Aristotle's Politics, re-popularised in the 1789 Revolution), the intermediary through which Greek d
```


### [2026-09-06T16:11:10.961Z] TOOL RESULT

```
# Etymology of Hamlet

Based on the Wiktionary article, the name's origins trace through multiple languages rather than deriving from Old French:

The word comes "From [Latin](https://en.wikipedia.org/wiki/Latin "w:Latin") _[Amlethus](/w/index.php?title=Amlethus&action=edit&redlink=1 "Amlethus (page does not exist)")_, as written by 13th-century Danish historian [Saxo Grammaticus](https://en.wikipedia.org/wiki/Saxo_Grammaticus "w:Saxo Grammaticus"), and borrowed into English by way of [François de Belleforest](https://en.wikipedia.org/wiki/Fran%C3%A7ois_de_Belleforest "w:François de Belleforest")'s [French](https://en.wikipedia.org/wiki/French_language "w:French language") _[Hamlet](#French)_."

The ultimate source was "Old Danish _[Amlethæ](/w/index.php?title=Amleth%C3%A6&action=edit&redlink=1 "Amlethæ (page does not exist)")_, corresponding to [Old Norse](https://en.wikipedia.org/wiki/Old_Norse "w:Old Norse") _[Amlóði](/w/index.php?title=Aml%C3%B3%C3%B0i&action=edit&redlink=1 "Amlóði (page does not exist)")_ ("fool"), claimed to be suggestive of the way that Hamlet acts in the play, from _[ama](/wiki/ama#Old_Norse "ama")_ ("to annoy")."

The documented etymology supports Old Norse/Old Danish origins, not the Old French diminutive theory you mentioned.
```


## [2026-09-06T16:11:23.108Z] TOOL CALL #63: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Hamlet\" --note \"page 249 verification: is English 'Hamlet' from OF hamelet or ON Amlóði\" 2>&1 | tail -1; mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg249.png data/verification/sources/refs/ocr/BOOK/249.png && ls -la data/verification/sources/refs/ocr/BOOK/249.png",
 "description": "Archive Hamlet page, copy page PNG"
}
```


### [2026-09-06T16:11:25.108Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0bb66061d76d51a8.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 82530 Sep  6 12:11 data/verification/sources/refs/ocr/BOOK/249.png
```


## [2026-09-06T16:11:37.632Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nprint('leaves',len(t))\nimport re\nfor i,l in enumerate(t):\n    if 'κοιμάω' in l or 'koiman' in l or ('haims' in l and 'civis' in l) or ('kei-' in l and 'Lager' in l and 'civis' in l):\n        print('leaf',i, l[:200].replace('\\n',' '))\nEOF",
 "description": "Walde-Pokorny Bd1 kei"
}
```


### [2026-09-06T16:11:39.479Z] TOOL RESULT

```
leaves 895
leaf 367 „Lager“, dxomg „Gemahlin" (mit jon. Pailose aus *a-xomg), vgl. bret. argud „leichter Schlaf" (*are-koito -, Loth Rc. 22, 334) xoiuam bringe zu      ;              ,   Bett, schlafere ein“ (vgl. got. h
```


## [2026-09-06T16:11:43.291Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (366,367,368):\n    print('=== leaf',i)\n    print(t[i][:1800])\nEOF",
 "description": "WLD Bd1 kei entry context"
}
```


### [2026-09-06T16:11:45.177Z] TOOL RESULT

```
=== leaf 366
358                                                  kas-, kas          kei-



client wegen Casiltnum                   ,
                                              Gasilins,    Casulius          ,
                                                                                  Casellius      (Schulze               EN. 550)
keinen Glauben melir.
     Eine Brweiterung der Stamme *kasen- (: kas-n-o-) und *kaseu-, kasou-
(:    kas-u-o-) mit Formans -clho-                       und Schwundstufe der "Wzsilbe scheinen
gr. gavdog         „blond“         (-«- auffiillig;      aus einem Paradigma -cor -avog zu er-                :




klaren?)          und £ov&og          „gelblich,        braunlieh" (Persson 'Wzerw. 135                                  Anm. 1,
          Fick I 4 42, 377, Hirt Abl. 118, 137); der etwas verschiedene
Beitr. 896,
Farbenwert dieser Worte steht der YerkniipfuDg nicht im Wege.


kas-, kas- „zurecht\veisen, amveisen'h
      Ai. gusli     (
                        casati )    „weist zureeht,             ziichtigt,         herrscht,              befiehlt,       belehrt“
Ptc. Aor. r.iZaitt- „untenveisend-‘, ristd- „zurechtgewiesen, angewiesen, unter-
wiesen“ (jiinger casta-, wie av. sashi-), av. sasti „heiBt, lehrt“, Opt. sisoti,
<i-slsta- „verheiBen‘‘, ai. qastar- „Bestrafer, Gobi etch' = av. sdstar- „Gebieter,
Machthaber, Fiirst“, mp. sastar „Herrscher, Tyrann“, ai. gclstrd- n. „An-
weisung, Yorschrift, Belehrung, Lehrbuch“, av. sux v an- n. „Lehre“, sdsna
„Lehre, Gebot“, ai. gisti- f. „Ziichtigung, Bestrafung, GeheiB, Befehl“
(jiinger cast!-), gisya- „zu unter\veisen“, m. „Sehiiler“;
   arm. (Hiibschmann Arm. St. I 48, Arm. Gr. I 488 f.) sast „Schelte, Yor-
wurf, Drohung, Strenge, Autoritat"' sastan „schelte, drohe, scharfe ein, ge-
biete“, sastik
=== leaf 367
„Lager“, dxomg „Gemahlin" (mit jon. Pailose aus *a-xomg), vgl. bret.
argud „leichter Schlaf" (*are-koito -, Loth Rc. 22, 334) xoiuam bringe zu      ;              ,


Bett, schlafere ein“ (vgl. got. haims, air. coim, lett. saime, auch lit. iseimyna                             ;



ags. Ji&manl).    Zweites Zsglied            nach Brugmann IF. 17, 351 ff. in
jiegiaoog, veoooog, "Aurptooa u. dgl.  Sehr wahrscheinlich lat. ciinae, cun fi-
bula PI. „Wiege, Nest"           (
                                     *koi-na    ;
                                                    s.    Yf. LEWb. 2 s. v.)       und anord. hid, hidi
n. „Lager des          Biiren"
                        (
                          *kei-to - ,                Bugge BB. 3, 118;
                                                        nicht besser nach
Noreen Ltl. 204 zu an. skide „Scheide" als s-lose Yariante).
  Mit dem Begriffe „Heim, traut, lieb":
     mit ro- Suffix: arm. ser „Ycigung, Liebe", sirem „ich liebe"                                  (* keiro
Bugge KZ. 32, 25, Scheftelowitz BB. 28, 284);
   mit «o-Suffix: ai. geva- (= germ, hlwa ) „traut,                         freundlich,       lieb,   wert",
giva- (= germ. *hiwa-) „vertraut, lieb, heilsam";
     lat.              = osk. ceus ds. (dagegen
            civis „Biirger"                         da „Mann", Fick II 4 75
                                                                      ir.

ist vielmehr = cia „wer, jemand"   Falk-Torp u. hjon N. mit Lit., Pedersen KG.
                                           s.

II 209); got. heiiva-frauja „Hausherr“, ags. hlw-cund „heimisch", hliv-rceden
f.    „Haushaltung“, ahd.        hi-rat     „IIeirat“,          ags. hl-red        ds.,   agutn.   hi-slcepr
„Familie“, anord. hy-byli Neutr.           
=== leaf 368
360

  Ygl. Curtius 5 145, Ficb I 4 42, 43, 421 (Trennung der Worte fiir „liegen“
und „traut“), III 4 87, ZupitzaJGutt. 49, 184 f. usw.               —
                                                      Hirt BB. 24, 286 und
besonders Bezzenberger BB. 27, 168 vereinigen unter einer versch. Wz. qdi-
„sich gesellen, scharen“, got. usw. Jiaims mit lit. kiemas „Bauernhof“, Mimas
„Dorf‘, lett. c'icms „Dorf, Yersammlungshau9 der Herrnhuter“, apr. caymis
„Dorf‘, lit. kaimynas „Nachbar“, kaimene „Herde“ (die aber der Entlehnung
aus germ. *haimaz verdiichtig sind nacb v. Grienberger SBAk. Wien 142,
YIII 105, Uhlenbeck PBrB. 30, 286, bzw. westidg. Guttural haben konnen)
und gr. y.d)/rtj „Dorf;<, y.wjuog „Festgelage“ (ware qd[i]ma, -mo-) aber die                  ;


gr. Worte sind auch anderer Deutung fahig (s. hem- „stopfen) und anord.
ping-heimr ist keine Stiitze fiir die Gdbed. „sicb scharen“.


2.    kei- in Farbbezeicbnungen, bes. fiir dunkle Farben                     (s.       aucli u. Jcor-).

  Ai. *rera- wohl in gerabha- m. Name verscbiedener Schlangen (Petersson
KZ. 46, 128), vgl. unten clra- ,.Boa“.
     Mir. ciar „dunkel“ (* kei-ro -);          anord.   liurr,   ags. liar „altersgrau,            grau“
(*koi-ro-)      — alid. as. her „wiirdig, erhaben“ (ursprgl. von ergrauten Mannern),
Komp. *heriro her(r)o „Herr“; ob hierher aksl. sen, russ. seryj „grau“, wo-
                       ,


neben mit schwierigem s- poln. szary eech. serif „grau“ (nicht nach Uhlen-
                                                  ,

beck IF. 17, 97 mit ai. cya-md- usw. im Anlaut iibereinstimmend, s. dagegen
Pedersen KZ. 40, 176f., der mit Reclit urslav. *chen postuliert, unter An-
satz von idg. kh-, der aber am anders zu etymologisierenden gr. yoioog
„Ferkek‘ keine Stiitze findet, s. Pe
```


## [2026-09-06T16:12:09.703Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== KLN hamlet\"; grep -n \"^hamlet\\|hamlet,  n\" KLN_1966.txt | head -3; grep -n \"hamlet\" KLN_1966.txt | head -3; echo \"== KLN Henry\"; grep -n \"Heimerich\\|Haimirich\\|Henry\" KLN_1966.txt | head -5; echo \"== SKT hamlet\"; grep -n \"Hamlet\\|hamlet\" SKT.txt | head -3; echo \"== MON shiva\"; grep -n \"شیوا\" MON_part1.txt MON_part2.txt | head -5",
 "description": "Klein hamlet/Henry, Mo'in shiva"
}
```


### [2026-09-06T16:12:09.831Z] TOOL RESULT

```
== KLN hamlet
17136:Hamites,  n.,  a  genus  of  extinct  cephalopods ( paleontol .)  —  ModL.,  fr.  L.  hamus,  ‘hook’.  See hamulus  and  subst.  suff.  -ite. hamlet,  n.,  a  small  village.  —  ME.  hamelet,  fr. MF.  hamelet,  dimin.  of  hamel  (whence  F.  ha- meau),  itself  a  dimin.  of  OF.  ham,  fr.  Frankish *haim,  ‘home’,  which  is  rel.  to  OHG.  heim,  OE. ham,  ‘home’.  See  home  and  the  dimin.  suffixes, -el  and  -et.
2139:alcornoque,  n„  the  bark  of  several  trees.  —  Sp., Port,  ‘cork  tree’,  a  hybrid  coined  fr.  Arab,  al-, ‘the’,  and  L.  quercus,  ‘oak’,  changed  into  *quer - nus.  See  cork  and  cp.  Quercus. alcove,  n.,  1)  a  recessed  section  in  a  room;  2)  any recess.  —  F.  alcove ,  fr.  Sp.  alcoba,  fr.  Arab,  al- qubbah,  fr.  al-,  ‘the’,  and  qubbah,  ‘arch,  vaulted tent’,  which  is  rel.  to  Arab,  qabba,  ‘it  was  bent’, and  to  Heb.  qubbd \  ‘vaulted  tent’,  Syr.  qebha- bhd,  ‘vault,  vaulted  tent’,  Akkad,  qababu, ‘shield’.  All  these  words  are  derivatives  of  the Sem.  base  q-b-b,  ‘to  be  bent,  crooked,  vaulted’, aldea,  n.,  hamlet,  villa.  —  Sp.  and  Port.,  ham¬ let’,  fr.  Arab,  al-,  ‘the’,  and  dayah,  ‘farm,  ham¬ let’.  Cp.  aldeia.
2141:aldehyde,  n.  ( chem .)  —  Coined  by  the  German chemist  Justus  von  Liebig  (1803-73)  from  the abbreviation  of  alcohol  de/rw/rogenatum,  alco¬ hol  deprived  of  hydrogen  . aldeia,  n.,  hamlet.  —  Port,  aldeia.  See  aldea. alder,  n.,  tree  rel.  to  the  birch.  —  ME.,  formed with  excrescent  d  fr.  OE.  alor ,  which  is  rel.  to OS.  elora,  ON.  dir,  Dan.  die,  el,  Swed.  al, MDu.  else,  Du.  els,  OHG.  erila  (fr.  earlier elira),  G.  Erie,  fr.  Teut.  •atiso;  cogn.  with Russ,  dlicha  (for  *alisa-),  ‘alder’,  Pol.  olcha,  of s.m.,  OSlav.  jellcha,  L.  alnus  (for  *alsnos),  Lith.
17126:ham,  n.,  the  inner  or  hinder  part  of  the  knee;  the thigh  of  an  animal  (anat.)  —  ME.  hamme,  fr. OE.  hamm,  rel.  to  ON.  hom,  MLG.,  MDu., MHG.,  dial.  G.  hamme,  Du.  ham,  OHG.  hamma, and  cogn.  with  Gk.  xwipt],  ‘part  between  knee and  ankle’,  OIr.  cnaim,  ‘bone’.  Cp.  the  first element  in  hamshackle.  Cp.  also  cnemial. Derivative:  hamm-y,  adj. ham,  n.,  a  hamlet,  village,  town;  used  as  a  suff. in  place  names  (now  dial.  Engl.)  —  OE.  ham, ‘dwelling,  home’.  See  home, hama-,  combining  form  meaning  together  with; at  the  same  time  with.  —  Gk.  apcc,‘  together with’.  See  same.
== KLN Henry
437:Liddell  and  Scott,  A  Greek-English  Lexicon,  in  Henry  Stuart  Jones  s  recension,  Oxfor  ,
444:Skinner,  Henry  Alan,  The  Origin  of  Medical  Terms,  2nd  ed.,  Baltimore,  1961.
1167:generation.  —  Coined  by  the  English  biologist Thomas  Henry  Huxley  (1825-95)  in  1870  fr. Gk.  ijiioc;,  ‘without  life’,  and  viveaiQ,  ‘origin, source’.  See  abio-  and  genesis  and  cp.  bio¬ genesis.
1982:agnomen,  n.,  name  added  to  the  surname  ( Roman antiq.)  —  L.  agnomen,  fr.  ad-  and  OL.  gnomen (whence  L.  nomeri),  ‘name’.  See  name  and  cp. nominal.  Cp.  also  cognomen, agnostic,  n.,  one  who  professes  that  the  existence of  a  First  Cause  and  the  essential  nature  of things  are  not  and  cannot  be  known.  —  Coined by  Thomas  Henry  Huxley  (1825-95)  in  1869  on analogy  of  gnostic  fr.  Gk.  dyvoxrxo?,  ‘unknown, not  to  be  known’.  See  priv.  pref.  a-  and  gnostic. Derivative:  agnostic,  adj.
4555:bathybius,  n.,  a  slimy  substance  dredged  up  from the  Atlantic  (zoo/.)  —  ModL.,  coined  by  the English  biologist  Thomas  Henry  Huxley  (1825- 95)  in  1868  fr.  Gk.  (3atW<;,  ‘deep’  and  fJlo?, ‘life’.  See  bathy-  and  bio-, bathyscaphe,  n.,  a  diving  apparatus  for  reaching great  depths.  —  Compounded  of  bathy-  and Gk.  rrxa'prj,  ‘boat’.  See  scapho-. bathysphere,  n.,  a  spherical  diving  apparatus  for the  observation  and  study  of  the  depths  of  the sea.  —  Compounded  of  bathy-  and  Gk.  <79<xtpa, "ball,  globe,  sphere’.  See  sphere, batik,  n.,  a  method  of  coloring  designs  on  cloth. —  Javan,  batik,  ‘spotted,  speckled’. Derivatives:  batik,  tr.  v.,  batik-er,  n. batiste,  n.  —  F.,  named  after  its  first  maker,  Bap¬ tiste  of  Cambrai,  who  lived  in  the  13th  cent, batman,  n.,  an  officer’s  servant.  —  A  hybrid coined  fr.  F.  bat,  ‘packsaddle’,  and  E.  man.  See bathorse.
== SKT hamlet
7279:fuat  (1),  to  become  mouldy.  (F.— L.) In  Hamlet,  iv.  4.  3g.  Coined  from  fttstgd at  fttity^  answerin?  to  O.  V.fttstt,  '  fusty, tasting  of  the  cask/  Cot.-O.  lp.fusli»  a ca<^k,  orig.  a  stock,  tnmk.  log.  — L./MJ//m (as  above).
8778:hamlet   tF.-O.LowG.)    ME. lei,  'limin.  of  O.  F.  kamcl  iF    '■'-"^' hamlet.       Formed,  with  dimi from  O.  Fries,  ham.  a  home,  l^^         _^
13431:patch  (3),  a  paltry  fellow.  1,0.  Low  G.) Temp.  iii.  J.  71.  Patch  meant  a  fool  or jester,  from  the  parti-coloured  or  patch- like dress  f  Wolscy  had  two  fools  so  named (Nares).  The  tame  word  as  patch  0)* Der,  patch-ockf  a  clown,  a  dimin.  foim, Spenser,  V^iew  of  Ireland,  Globe  ed.,  p,  63'), cot.  2  ;  spelt /o/a:^,  Hamlet,  iii,  J.
== MON shiva
MON_part2.txt:90312:هشیاری: 1" (- هشیواری - هوشیاری] 
MON_part2.txt:90317:هشیوار: ۱۵۹-۲ [- هشبار - هوشبار | 
MON_part2.txt:92387:هوشیار: :۰.18 [- هشیار - هشیوار] (ص.) 
MON_part1.txt:15121:شدن» شیوا شدن. (امص.) زبان اوری» 
MON_part1.txt:15122:روشن گفتاری» شیوا سخنی.
```


## [2026-09-06T16:12:22.007Z] TOOL CALL #67: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249 && echo ok",
 "description": "Make scratch dir"
}
```


### [2026-09-06T16:12:22.060Z] TOOL RESULT

```
ok
```


## [2026-09-06T16:16:42.249Z] TOOL CALL #68: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249/build.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_KEY   = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/ḱey-\"\nW_TKEY  = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/tḱey-\"\nW_ARIKA = \"https://en.wiktionary.org/wiki/أريكة\"\nW_CAKOS = \"https://en.wiktionary.org/wiki/چکش\"\nW_CAQU  = \"https://en.wiktionary.org/wiki/چاقو\"\nW_CAKAD = \"https://en.wiktionary.org/wiki/چکاد\"\nE_HAM   = \"https://www.etymonline.com/word/hamlet\"\nE_HENRY = \"https://www.etymonline.com/word/Henry\"\nW_HAMLET= \"https://en.wiktionary.org/wiki/Hamlet\"\nW_COKA  = \"https://www.wisdomlib.org/definition/coka\"\n\nPOK539 = {\"src\":\"POK\",\"where\":\"Bd. I 539-540 (POK_02.txt leaves 197-199)\",\"stance\":\"supports\",\n \"note\":\"'1. ḱei- \\\"liegen; Lager, Heimstätte, traut, lieb (von derselben Siedlung)\\\"; koi-to- \\\"Lager\\\"; kei-mo-, koi-mo- \\\"vertraut\\\"' — with gr. κοῖτος/κοίτη 'Lager', κοιμάω 'bringe zu Bett', lat. cīvis, ai. śiva-, got. haims, ahd. heim.\"}\nWLD358 = {\"src\":\"WLD\",\"where\":\"Bd. I 358-360 (incoming/WLD/WLD_Bd1_pages.txt leaves 366-368)\",\"stance\":\"supports\",\n \"note\":\"Same entry as Pokorny's: 'κοίτη \\\"Lager\\\", ἄκοιτις \\\"Gemahlin\\\" … κοιμάω \\\"bringe zu Bett, schläfere ein\\\" (vgl. got. haims …)'; 'lat. civis \\\"Bürger\\\" = osk. ceus'; 'ai. śeva- (= germ. *hiwa-) \\\"traut, freundlich, lieb, wert\\\"'.\"}\nAHDKEI = {\"src\":\"AHD\",\"where\":\"Watkins 1985 s.v. kei-1 (AHD_watkins1985.txt line 595)\",\"stance\":\"supports\",\n \"note\":\"'kei-1. To lie; bed, couch; beloved, dear. … *kei-wi- in Latin civis … *koi-m-o- in Greek koiman, to put to sleep: CEMETERY. III. Suffixed zero-grade *ki-wo- in Sanskrit siva, auspicious, dear: SHIVA. [Pok. 1. kei- 539.]'\"}\nKLNKEI = {\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 7799 (s.v. civil) and 6946 (s.v. cemetery)\",\"stance\":\"supports\",\n \"note\":\"'fr. I.-E. base *kei-, \\\"to lie, settle down\\\", whence also Gk. κεῖσθαι …, κοιμᾶν …, κοιμητήριον …, κοίτη … Goth. haims, OE. hām … and prob. also OI. śivaḥ, śivaḥ, \\\"kind, friendly, gracious\\\".'\"}\n\nentry0 = {\n \"entry\": 0,\n \"root\": \"Kei 4; Koi-to\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *ḱey- 'to lie down, rest; to settle, be at home; dear' (o-grade noun *ḱoy-to- 'bed, resting place', *ḱoy-mo- 'homely, dear')\",\n \"note\": \"Pokorny I 539-540 '1. ḱei- \\\"liegen; Lager, Heimstätte, traut, lieb\\\"; koi-to- \\\"Lager\\\"' — Nourai's two-line heading 'Kei 4 / Koi-to' with the gloss 'to lie, rest; bed, couch, home, domain' reproduces exactly that; Watkins kei-1 'To lie; bed, couch; beloved, dear [Pok. 1. kei- 539]'. Language label (Indo-European) and gloss are right. The doubtful parts of the chart are not the root but three of its branches: the Greek→Arabic arīka link (modern sources do not derive أريكة from Greek), the Germanic 'home' branch (today reconstructed as a separate root *tḱey- 'to settle'), and the inclusion of Shakespeare's 'Hamlet' among the reflexes of Old French hamel.\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *ḱey- «دراز کشیدن، آرمیدن؛ جای خواب، خانه، عزیز» است؛ پوکورنی (ج۱، ص۵۳۹-۵۴۰) همین ریشه را با صورت اسمی *ḱoy-to- «بستر» آورده و واتکینز نیز در پیوست ریشه‌های هندواروپایی همان را تکرار کرده است. پس عنوان و معنای ریشه در نمودار نورایی درست است. اما سه شاخه از شاخه‌های آن جای چون‌وچرا دارد: وام‌گیری «اریکهٔ» عربی از یونانی (که پژوهش امروزی آن را نمی‌پذیرد)، شاخهٔ ژرمنی heim «خانه» (که امروز به ریشهٔ جداگانهٔ *tḱey- «سکنا گزیدن» بازبرده می‌شود) و آوردن نام «Hamlet» شکسپیر در کنار واژهٔ hamlet.\",\n \"sources\": [W_KEY, W_TKEY],\n \"ref_check\": [{\"ref\":\"POK:539\",\"status\":\"supports\",\"note\":\"Pokorny I 539 (POK_02.txt leaf 197, the page marked 539 sits in leaf 196): '1. ḱei- \\\"liegen; Lager, Heimstätte, traut, lieb (von derselben Siedlung)\\\"; koi-to- \\\"Lager\\\"' — precisely Nourai's root and gloss.\"}],\n \"consulted\": [POK539, WLD358, AHDKEI, KLNKEI],\n \"nodes\": []\n}\n\nn = entry0[\"nodes\"].append\n\nn({\"id\":1,\"lang\":\"Greek\",\"words\":\"koite, ari-koite; koiman; koimeterion\",\"verdict\":\"plausible\",\n \"derivation\":\"Greek κοίτη (koítē) 'bed, resting place' and κοῖτος 'lying down, sleep' are the regular o-grade *ḱoy-teh₂/*ḱoy-to- of *ḱey-; κοιμάω (koimáō) 'put to bed, lull to sleep' is built on *ḱoy-mo- 'homely'; κοιμητήριον (koimētḗrion) 'sleeping-room, dormitory' is the -τήριον noun of place from it, taken over by early Christian writers (3rd c. AD) for a burial ground. All three are in Pokorny 539 and in Klein s.v. cemetery. The fourth form, 'ari-koite', is the weak point: no compound ἀρι-κοίτη 'decorated bed' is recorded in LSJ; what Greek does have is ἄκοιτις 'bedfellow, wife' (< *sm̥-koiti-, with Ionic psilosis) and, in Celtic, *are-koito- (Breton argud 'light sleep') which Pokorny quotes. Nourai's 'ari-koite' looks like a form invented to bridge Greek κοίτη to Arabic arīka.\",\n \"derivation_fa\":\"واژه‌های یونانی κοίτη «بستر»، κοῖτος «خفتن» و κοιμάω «به خواب کردن» همگی از همان ریشهٔ *ḱey- با درجهٔ o (یعنی *ḱoy-) ساخته شده‌اند و κοιμητήριον «خوابگاه» اسم مکان از κοιμάω است که مسیحیان سدهٔ سوم میلادی آن را به معنی «گورستان» به کار بردند؛ پوکورنی (ص۵۳۹) و کلاین هر سه را آورده‌اند. اما صورت چهارم، «ari-koite» به معنی «بستر آراسته»، در فرهنگ لیدل-اسکات یونانی یافت نمی‌شود؛ آنچه در یونانی هست ἄκοιτις «هم‌بستر، همسر» است. به گمان قوی نورایی این صورت را برای پیوند دادن κοίτη به «اریکهٔ» عربی ساخته است.\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"POK:539\",\"status\":\"supports\",\"note\":\"POK_02.txt leaf 197: 'gr. κοῖτος m., κοίτη f. \\\"Lager\\\", ἄκοιτις \\\"Gemahlin\\\" … κοιμάω \\\"bringe zu Bett, schläfere ein\\\"' — κοίτη/κοιμάω yes, ἀρι-κοίτη absent.\"},\n  {\"ref\":\"TAD:2\",\"status\":\"partial\",\"note\":\"TAD_pages.txt leaf 5 (= printed p.2, the alif list begins on leaf 4) carries, between أرغن and أزادرخت, an entry marked 'يوناني' glossed 'معناه فراش و… مرقد جيد'; al-Unaysi does class the word as Greek but the headword and the Greek etymon are illegible in this OCR, and no scan of p.2 is available (tools/ref_page.py TAD:2 → 'no scan covers printed page 2').\"}],\n \"consulted\":[POK539, WLD358, KLNKEI]})\n\nn({\"id\":2,\"lang\":\"Arabic\",\"words\":\"arîkeh; a.r.k\",\"verdict\":\"disputed\",\n \"derivation\":\"Arabic أَرِيكَة (arīka) pl. أَرَائِك (arāʾik) 'couch, throne' is a Qurʾānic word (18:31, 36:56, 76:13). Nourai, following al-Unaysi (TAD), makes it a borrowing of Greek κοίτη / *ἀρι-κοίτη. No modern authority supports that route: Greek κ- would not give Arabic ʾ-, and no Greek ἀρικοίτη exists. Wiktionary calls the origin 'unknown', citing (a) a difficult connection with Classical Persian اورنگ (awrang) 'throne' and (b) a native derivation from the tree-name أَرَاك (ʾarāk) or from a lost verb 'to bide, abide'. Addi Shir (AFM p.10 of the alif section) states outright that الأريكة comes from Persian اورنك (awrang). Arabic lexicography treats it as a regular fiʿīla formation on a root ʾ-r-k, which is what Nourai's second entry 'a.r.k' records. So: the word and the root are real, but the Greek etymology drawn by the arrow is not the modern view.\",\n \"derivation_fa\":\"واژهٔ عربی «أَرِيكَة» (جمع: أرائك) به معنی «تخت، اورنگ» در قرآن هم آمده است (کهف ۳۱، یس ۵۶). نورایی به پیروی از طوبیا العنیسی آن را وام‌واژه‌ای از κοίτη یونانی می‌داند، ولی هیچ منبع امروزی این راه را نمی‌پذیرد؛ کاف یونانی در عربی به همزه بدل نمی‌شود و صورت *ἀρι-κοίτη هم در یونانی وجود ندارد. ویکی‌واژه ریشه را «ناشناخته» می‌خواند و دو احتمال می‌آورد: وام‌گیری از «اورنگ» فارسی، یا ساختی بومی از ریشهٔ ء ر ک (هم‌ریشه با «أراک»). ادّی شیر نیز در «الألفاظ الفارسیة المعربة» می‌نویسد که «الأریکة» از «اورنک» فارسی است. پس خودِ واژه و ریشهٔ سه‌حرفی درست است، اما پیکان یونانی→عربی را پژوهش امروزی رد می‌کند.\",\n \"sources\":[W_ARIKA],\n \"ref_check\":[{\"ref\":\"TAD:2\",\"status\":\"partial\",\"note\":\"See node #1: the entry on TAD p.2 (leaf 5) is marked 'يوناني' and glossed 'فراش … مرقد', so al-Unaysi is indeed Nourai's authority for the Greek claim, but his Greek form cannot be read in the OCR and no page scan exists.\"},\n  {\"ref\":\"FVA:30\",\"status\":\"not_checked\",\"note\":\"FVA (Nahvi, Farhang-e vazheha-ye arabi dar farsi, 1368) has no digital copy anywhere (refs_online.json: 'RE-SEARCH 2026-09: still no digital copy on any permitted platform').\"}],\n \"consulted\":[{\"src\":\"AFM\",\"where\":\"AFM.txt line 351 / AFM_pages.txt leaf 10, s.v. (الأريكة)\",\"stance\":\"contradicts\",\"note\":\"'(الأريكة) … أورنك …' — Addi Shir derives the Arabic word from Persian اورنك 'throne', not from Greek.\"},\n  {\"src\":\"FVQ\",\"where\":\"grep 'arika|ara'ik|arīka' in FVQ.txt\",\"stance\":\"silent\",\"note\":\"Jeffery's Foreign Vocabulary of the Qur'an has no entry for أريكة/أرائك — he did not regard the Qur'anic word as a foreign borrowing.\"},\n  {\"src\":\"KLN\",\"where\":\"grep 'arika' in KLN_1966.txt\",\"stance\":\"silent\",\"note\":\"Klein knows no English word from this Arabic form; nothing on a Greek→Arabic route.\"}]})\n\nn({\"id\":3,\"lang\":\"Persian\",\"words\":\"arîkeh «اریکه»; arâek «ارایک»\",\"verdict\":\"confirmed\",\n \"derivation\":\"Persian اَریکه (arīke) 'couch, throne, seat of power' and the plural ارائک (arāʾek) are straightforward Arabic loans in Persian: Moʿin's dictionary marks اریکه '[ع.]' (= Arabic) and glosses it 'تخت، تخت آراسته؛ تختی که در خانهٔ عروس … نهند، هر چه که بر آن تکیه زنند و بنشینند'. اریکه entered literary Persian with the Qurʾānic vocabulary and is today mostly used in the political metaphor 'اریکهٔ قدرت' ('the throne of power'), which is Nourai's 'domain'. ارائک is the Arabic broken plural taken over unchanged; the chart's Persian spelling ارایک is the informal spelling of أرائک (with yā for the hamza-carrier).\",\n \"derivation_fa\":\"«اَریکه» و جمع آن «ارائک» در فارسی وام‌واژهٔ عربی‌اند؛ معین در فرهنگ فارسی آن را با نشان «[ع.]» آورده و چنین معنی کرده است: «تخت، تخت آراسته؛ تختی که در خانهٔ عروس … نهند، هر چه که بر آن تکیه زنند و بنشینند». این واژه با واژگان قرآنی به فارسی ادبی راه یافته و امروز بیشتر در ترکیب «اریکهٔ قدرت» به کار می‌رود که همان معنی «قلمرو» در نمودار است. املای «ارایک» در کتاب صورت ساده‌شدهٔ «أرائک» است. ادعای نورایی در این حلقه (عربی ← فارسی) درست است؛ تنها منشأ یونانیِ خودِ واژهٔ عربی جای تردید دارد.\",\n \"sources\":[W_ARIKA],\n \"ref_check\":[{\"ref\":\"MON:210\",\"status\":\"supports\",\"note\":\"Moʿin, Farhang-e Farsi s.v. اریکه (MON_part1.txt line 10372 ff.): 'اریکه … [ع.] (اِ) تخت، تخت آراسته؛ تختی که در خانهٔ عروس یعنی حجله نهند، هر چه که بر آن تکیه زنند و بنشینند از تخت و منصه و فراش و بستر' — Arabic loan, exactly Nourai's glosses; the page number cannot be matched because the local copy is the 2-vol Adena reprint.\"},\n  {\"ref\":\"BQT:112\",\"status\":\"not_found\",\"note\":\"Borhan-e Qateʿ vol. 1: the running head ۱۰۵ falls on leaf 321 of BQT_v1_pages.txt (leaf = printed + 216), so printed p. 112 = leaf 328, which contains اژدها/ازغ/ازگان — not اریکه; and the ار… entries (leaves 319-324) run ارغنون … اریاگ with no headword اریکه at all (Borhan is a dictionary of Persian words, and اریکه is Arabic). Only occurrence of اریکه in vols 1-2 is inside Moʿin's gloss on تخت (leaf 698).\"},\n  {\"ref\":\"FVA:30\",\"status\":\"not_checked\",\"note\":\"No digital copy of FVA exists (refs_online.json).\"}],\n \"consulted\":[{\"src\":\"MON\",\"where\":\"MON_part1.txt line 10372, s.v. اریکه\",\"stance\":\"supports\",\"note\":\"'اریکه … [ع.] (اِ) تخت، تخت آراسته…' — tagged [ع.], i.e. borrowed from Arabic.\"},\n  {\"src\":\"BQT\",\"where\":\"BQT_v1_pages.txt leaves 319-324 and 328\",\"stance\":\"silent\",\"note\":\"No اریکه headword in Borhan-e Qateʿ; Moʿin uses the word only as a gloss for تخت (leaf 698: 'کرسی، اریکه، سریر…').\"},\n  {\"src\":\"AFM\",\"where\":\"AFM.txt line 351\",\"stance\":\"partial\",\"note\":\"Addi Shir has the Arabic word as a Persian loan from اورنك — i.e. a Persian→Arabic→Persian round trip rather than Greek→Arabic→Persian.\"}]})\n\nn({\"id\":4,\"lang\":\"Latin\",\"words\":\"coemeterion\",\"verdict\":\"plausible\",\n \"derivation\":\"The Latin form is coemētērium (Late Latin, ecclesiastical, from the 3rd c. AD onwards in Tertullian and the Church Fathers), a straight transliteration of Greek κοιμητήριον with the regular Greek -ον > Latin -um substitution; Old French cimitiere, cimetiere then gives Middle English cimitery/cemetery. Klein: 'cemetery, n. — Late L. coemeterium, fr. Gk. κοιμητήριον, \\\"sleeping room, burial place\\\", fr. κοιμᾶν, \\\"to put to sleep\\\"'; Skeat has 'Low L. coemeterium'. The chart's 'coemeterion' keeps the Greek ending and is therefore not an actual Latin word-form; the sense given ('sleeping room, graveyard') is right, since in Christian Latin the word meant precisely a burial ground viewed as a dormitory of those awaiting resurrection.\",\n \"derivation_fa\":\"صورت درست لاتینی coemētērium است (لاتینِ کلیسایی از سدهٔ سوم میلادی)، که رونویسی مستقیم κοιμητήριον یونانی است با بدل شدن پایانهٔ ‑ον یونانی به ‑um لاتینی؛ سپس فرانسهٔ کهن cimetiere و انگلیسی میانه cemeterie از آن پدید آمد. کلاین می‌نویسد: «cemetery از لاتین متأخر coemeterium، از یونانی κοιμητήριον». صورتی که کتاب چاپ کرده («coemeterion») پایانهٔ یونانی را نگه داشته و از این رو واژهٔ لاتینی راستین نیست؛ ولی معنایی که داده («خوابگاه، گورستان») درست است، زیرا در لاتینِ مسیحی این واژه گورستان را چون خوابگاه مردگانِ چشم‌به‌راه رستاخیز می‌نامید.\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"AHD:217\",\"status\":\"partial\",\"note\":\"AHD:217 is a body page of the 1975 New College edition (s.v. cemetery), which is not accessible; the Watkins appendix in the local AHD_watkins1985.txt (line 595) does carry the same claim: '*koi-m-o- in Greek koiman, to put to sleep: CEMETERY'.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 6946 s.v. cemetery\",\"stance\":\"partial\",\"note\":\"'Late L. coemeterium, fr. Gk. κοιμητήριον, \\\"sleeping room, burial place\\\"' — same chain, but the Latin form is coemeterium, not *coemeterion.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt line 3219 s.v. Cemetery\",\"stance\":\"partial\",\"note\":\"'Cemetery. (L.—Gk.) Low L. coemeterium. — Gk. κοιμητήριον, a sleeping-place. — Gk. κοιμάω, I lull … (√KI-)'.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt s.v. kei-1\",\"stance\":\"supports\",\"note\":\"CEMETERY listed under kei-1 via Greek koiman.\"}]})\n\nn({\"id\":5,\"lang\":\"English\",\"words\":\"cemetery\",\"verdict\":\"confirmed\",\n \"derivation\":\"English cemetery is first recorded late 14c. (cimitery, Chaucer's period) from Old French cimitiere and directly from Late Latin coemeterium; the modern spelling with -e- restores the Latin/Greek vowel. Klein and Skeat both give exactly this chain, and Watkins files CEMETERY under kei-1. The 'graveyard' sense is the Christian Latin one, not a later English development.\",\n \"derivation_fa\":\"واژهٔ انگلیسی cemetery نخستین بار در اواخر سدهٔ چهاردهم میلادی به صورت cimitery دیده می‌شود، از فرانسهٔ کهن cimitiere و مستقیماً از لاتین متأخر coemeterium؛ املای امروزی با ‑e‑ صورت لاتینی/یونانی را بازسازی کرده است. کلاین و اسکیت هر دو همین زنجیره را می‌آورند و واتکینز نیز CEMETERY را ذیل kei-1 آورده است. ادعای نورایی در این حلقه درست است.\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 595, kei-1: '… Greek koiman, to put to sleep: CEMETERY'; and the index line 1340 'CEMETERY kei-1'.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 6946\",\"stance\":\"supports\",\"note\":\"'cemetery, n. — Late L. coemeterium, fr. Gk. κοιμητήριον…'\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt line 3219\",\"stance\":\"supports\",\"note\":\"'Cemetery. (L.—Gk.) Low L. coemeterium…'\"}]})\n\nn({\"id\":6,\"lang\":\"Sanskrit\",\"words\":\"siva\",\"verdict\":\"confirmed\",\n \"derivation\":\"Sanskrit शिव (śivá-) 'auspicious, kind, dear', already Rigvedic, is the *ḱi-wo-/*ḱey-wo- adjective of *ḱey- — the exact formal match of Germanic *hīwa- 'household member, spouse' and of Latin cīvis. Pokorny 540 lists 'ai. śiva- (= germ. *hīwa-) \\\"traut, freundlich, lieb, wert\\\"'; Watkins: 'Suffixed zero-grade form *ki-wo- in Sanskrit siva, auspicious, dear: SHIVA'. The euphemistic use of the adjective as the name of the god Śiva ('the Auspicious One', a taboo-avoiding epithet of Rudra) is standard Indological doctrine, so Nourai's gloss and his onward arrows are right.\",\n \"derivation_fa\":\"واژهٔ سنسکریت शिव (śivá-) «خجسته، مهربان، عزیز» که در ریگ‌ودا هم آمده، صفتی است از ریشهٔ *ḱey- با پسوند ‑wo- (*ḱi-wo-)، درست هم‌ساخت با *hīwa- ژرمنی و cīvis لاتینی. پوکورنی (ص۵۴۰) می‌نویسد: «ai. śiva- (= germ. *hīwa-) traut, freundlich, lieb, wert» و واتکینز نیز همین را ذیل kei-1 آورده است. کاربرد این صفت به‌عنوان نام خدا (شیوا، «آن خجسته») لقبی تابوگریزانه برای رودرا است و در هندشناسی پذیرفته است؛ پس این گره درست است.\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"AHD:1196\",\"status\":\"partial\",\"note\":\"AHD:1196 is the body page of the 1975 New College edition (s.v. Siva), not accessible; the local Watkins 1985 appendix (AHD_watkins1985.txt line 595) makes the same claim: 'Suffixed zero-grade form *ki-wo- in Sanskrit siva, auspicious, dear: SHIVA.'\"}],\n \"consulted\":[POK539, WLD358, AHDKEI]})\n\nn({\"id\":7,\"lang\":\"Persian\",\"words\":\"Šîvâ «شیوا ۲»\",\"verdict\":\"confirmed\",\n \"derivation\":\"Persian شیوا as the name of the Hindu god is a modern transcription of Sanskrit/Hindi Śiva, taken over in the 19th-20th c. through Persian writing on India and through European orientalist works; Moʿin lists it in the aʿlām volumes as شیوا ۲ (his homograph number 2), which is exactly the citation Nourai gives (MON5:960). It is a borrowing, not an inherited Iranian word — and it must not be confused with the native Persian adjective شیوا ۱ 'eloquent, fluent', a different word entirely (Moʿin's lexicon volumes have only that one: 'شیوا سخنی، زبان‌آوری').\",\n \"derivation_fa\":\"«شیوا» به‌عنوان نام خدای هندو، آوانگاری تازهٔ Śiva سنسکریت/هندی است که در سده‌های سیزدهم و چهاردهم خورشیدی از راه نوشته‌های فارسی دربارهٔ هند و آثار خاورشناسان اروپایی وارد فارسی شده است؛ معین آن را در جلد اعلام با شمارهٔ «شیوا ۲» آورده که همان ارجاع نورایی است. این واژه وام‌واژه است نه میراث ایرانی، و نباید آن را با «شیوای ۱» فارسی به معنی «فصیح، رسا» یکی گرفت که واژه‌ای یکسره جداست (در جلدهای واژگانی معین تنها همین یکی هست: «شیوا سخنی، زبان‌آوری»).\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"MON5:960\",\"status\":\"not_checked\",\"note\":\"Moʿin vols 5-6 (aʿlām) are not among the local files; the local MON_part1/2 (2-vol Adena lexicon reprint) has شیوا only in the sense 'eloquent' (MON_part1.txt line 15121: 'شیوا شدن … زبان‌آوری، روشن گفتاری، شیوا سخنی'), which is a different word.\"}],\n \"consulted\":[{\"src\":\"MON\",\"where\":\"MON_part1.txt line 15121\",\"stance\":\"silent\",\"note\":\"The lexicon volumes carry only شیوا 'eloquent'; the god belongs to the aʿlām volumes that the local copy lacks.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt s.v. kei-1\",\"stance\":\"supports\",\"note\":\"Confirms that the god's name is Sanskrit siva 'auspicious, dear' (SHIVA), which is what the Persian form transcribes.\"}]})\n\nn({\"id\":8,\"lang\":\"English\",\"words\":\"Siva, Shiva\",\"verdict\":\"confirmed\",\n \"derivation\":\"English Siva/Shiva is a direct scholarly borrowing of Sanskrit Śiva, current in English since the late 18th c. (Sir William Jones and the Asiatick Researches); Watkins files SHIVA under kei-1 through *ki-wo- 'auspicious, dear'. Nourai's gloss 'the God of destruction and reproduction' is the usual English handbook description of the third member of the trimūrti.\",\n \"derivation_fa\":\"«Siva/Shiva» در انگلیسی وام‌واژه‌ای است مستقیم از śiva سنسکریت که از اواخر سدهٔ هجدهم میلادی (ویلیام جونز و «پژوهش‌های آسیایی») در انگلیسی رواج یافته است؛ واتکینز SHIVA را ذیل kei-1 و از صورت *ki-wo- «خجسته، عزیز» آورده است. توضیح نورایی («خدای نابودی و باززایی») همان تعریف رایج در کتاب‌های انگلیسی برای سومین خدای تری‌مورتی است. این گره درست است.\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 595: '… in Sanskrit siva, auspicious, dear: SHIVA.'\"}],\n \"consulted\":[AHDKEI, KLNKEI]})\n\nn({\"id\":9,\"lang\":\"Latin\",\"words\":\"cîvis\",\"verdict\":\"confirmed\",\n \"derivation\":\"Latin cīvis 'member of a household/community, citizen' (Oscan ceus) continues *ḱey-wi-, an i-stem remade (after hostis) from the *ḱey-wo- adjective seen in Sanskrit śiva- and Germanic *hīwa-; the semantic path is 'belonging to the same settlement' > 'fellow-townsman' > 'citizen'. Pokorny 540 and Walde-Pokorny I 359 both print 'lat. cīvis \\\"Bürger\\\" = osk. ceus'; Watkins: 'Suffixed form *kei-wi- in Latin civis, citizen (< \\\"member of a household\\\")' — literally Nourai's gloss.\",\n \"derivation_fa\":\"واژهٔ لاتینی cīvis «عضو خانواده/اجتماع، شهروند» (اسکیایی ceus) دنبالهٔ *ḱey-wi- است، یعنی ستاک i که بر پایهٔ صفت *ḱey-wo- (همان که در śiva- سنسکریت و *hīwa- ژرمنی دیده می‌شود) و به قیاس hostis ساخته شده است؛ تحول معنایی از «هم‌آبادی» به «هم‌شهری» و سپس «شهروند» رفته است. پوکورنی (ص۵۴۰) و والده-پوکورنی (ج۱ ص۳۵۹) هر دو «lat. cīvis = osk. ceus» را آورده‌اند و واتکینز نیز همین را با معنی «عضو خانواده» ثبت کرده است؛ پس ادعای نورایی درست است.\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 595: '2. Suffixed form *kei-wi- in Latin civis, citizen (< \\\"member of a household\\\"): CITY, CIVIC, CIVIL.'\"}],\n \"consulted\":[POK539, WLD358, KLNKEI]})\n\nn({\"id\":10,\"lang\":\"English\",\"words\":\"civil, civic, city, civilization\",\"verdict\":\"confirmed\",\n \"derivation\":\"All four are Latinate: civil < Old French civil < Latin cīvīlis; civic < Latin cīvicus (16th c., directly from Latin); city < Middle English cite < Old French cité < Latin cīvitātem 'body of citizens, state' (which displaced the older sense 'town' only in Anglo-French); civilization is an 18th-c. French/English derivative of civiliser, ultimately of cīvīlis. Klein s.v. city: 'ME. cite, fr. OF. cite, fr. L. civitatem, acc. of civitas … fr. civis'; Watkins indexes CITY, CIVIC, CIVIL under kei-1.\",\n \"derivation_fa\":\"هر چهار واژه از راه لاتین آمده‌اند: civil از فرانسهٔ کهن civil و آن از cīvīlis لاتین؛ civic در سدهٔ شانزدهم مستقیم از cīvicus لاتین؛ city از انگلیسی میانه cite، از فرانسهٔ کهن cité، از cīvitātem لاتین «جامعهٔ شهروندان، دولت‌شهر»؛ و civilization ساختی است در سدهٔ هجدهم بر پایهٔ civiliser فرانسوی. کلاین ذیل city همین زنجیره را می‌آورد و واتکینز نیز CITY، CIVIC و CIVIL را ذیل kei-1 فهرست کرده است. این گره درست است.\",\n \"sources\":[W_KEY],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt index lines 1364-1366: 'CITY kei-1 / CIVIC kei-1 / CIVIL kei-1'.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt lines 7792-7800\",\"stance\":\"supports\",\"note\":\"'city, n. — ME. cite, fr. OF. cite (F. cité), fr. L. civitatem, acc. of civitas … fr. civis'; 'civil, adj. — F., fr. L. civilis … fr. civis'.\"},\n  AHDKEI]})\n\nn({\"id\":11,\"lang\":\"Old High German\",\"words\":\"heim; heimerich\",\"verdict\":\"plausible\",\n \"derivation\":\"OHG heim 'home, house, dwelling' (Gothic haims 'village', ON heimr, OE hām) and the compound name Heimirīch 'home-ruler' (heim + rīhhi 'ruler') are real. Pokorny does put got. haims / ahd. heim under 1. ḱei- 539 ('Mit dem Begriffe \\\"Heim, traut, lieb\\\"'), which is Nourai's authority. But Walde-Pokorny I 360 already records the dissent (Hirt, Bezzenberger separating haims under a root *qoi- 'sich gesellen'), and today the Germanic word is normally derived from a distinct root *tḱey- 'to settle, dwell' (Wiktionary: PGmc *haimaz < *tḱoy-mo-; Watkins prints a separate entry 'tkei-. To settle, dwell, be home … *(t)koi-mo- in Germanic *haimaz', although he still cross-cites Pok. 539). So the arrow is defensible on Nourai's source but not on the current reconstruction, where *ḱey- 'lie' and *tḱey- 'settle' are two roots.\",\n \"derivation_fa\":\"واژهٔ آلمانی علیای کهن heim «خانه، سرای» (گوتی haims «دِه»، نورس کهن heimr، انگلیسی کهن hām) و نام مرکب Heimirīch «فرمانروای خانه» (heim + rīhhi «فرمانروا») هر دو واقعی‌اند. پوکورنی خودِ haims/heim را ذیل همین ریشهٔ ۱. ḱei- در ص۵۳۹ آورده و مأخذ نورایی همین است؛ اما والده-پوکورنی (ج۱ ص۳۶۰) اختلاف نظر هیرت و بتسنبرگر را یاد می‌کند و امروزه این واژهٔ ژرمنی را از ریشهٔ جداگانهٔ *tḱey- «سکنا گزیدن» می‌گیرند (ویکی‌واژه: *haimaz < *tḱoy-mo-؛ واتکینز نیز مدخل جداگانهٔ tkei- دارد هرچند هنوز به ص۵۳۹ پوکورنی هم ارجاع می‌دهد). پس این پیکان بر پایهٔ مأخذ نورایی پذیرفتنی است ولی با بازسازی امروزی، که *ḱey- و *tḱey- را دو ریشهٔ جدا می‌داند، نمی‌خواند.\",\n \"sources\":[W_TKEY, W_KEY],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"AHD_watkins1985.txt line 1094 has a separate root: 'tkei-. To settle, dwell, be home. 1. Suffixed o-grade form *(t)koi-mo- in Germanic *haimaz, home … Old English hām: HOME … Old French ham, village, home: HAMLET', with the bracket citing Pokorny 539 alongside a second page — so Watkins both separates the root and keeps a link to Pok. 539.\"}],\n \"consulted\":[POK539,\n  {\"src\":\"WLD\",\"where\":\"Bd. I 360 (WLD_Bd1_pages.txt leaf 368)\",\"stance\":\"partial\",\"note\":\"'Hirt BB. 24, 286 und besonders Bezzenberger BB. 27, 168 vereinigen unter einer versch. Wz. qoi- \\\"sich gesellen, scharen\\\", got. usw. haims mit lit. kiemas …' — Walde-Pokorny already flags that the 'home' words may belong to another root.\"},\n  {\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 7799 (s.v. civil, base *kei-)\",\"stance\":\"supports\",\"note\":\"Klein (1966) still lists 'Goth. haims, \\\"village\\\", OE. ham, \\\"home, house, dwelling\\\"' under the same base *kei- 'to lie, settle down'.\"}]})\n\nn({\"id\":12,\"lang\":\"Old French\",\"words\":\"ham, hamlet\",\"verdict\":\"plausible\",\n \"derivation\":\"The Old French word is ham 'village', a borrowing from Frankish *haim (the West Germanic word of which OHG heim is the High German form), with the diminutives hamel (> Modern French hameau) and hamelet. So the transmission is Frankish → Old French, not Old High German → Old French; and 'hamlet' at this stage is Old French hamelet, a double diminutive, not a simple synonym of ham. Klein: 'hamlet … fr. MF. hamelet, dimin. of hamel (whence F. hameau), itself a dimin. of OF. ham, fr. Frankish *haim, \\\"home\\\", which is rel. to OHG. heim, OE. ham'. The gloss 'village' is right.\",\n \"derivation_fa\":\"صورت فرانسهٔ کهن ham «دِه» است که وام‌واژه‌ای است از فرانکی *haim (همان واژهٔ ژرمنی باختری که صورت آلمانی علیای آن heim است)، با مصغّرهای hamel (که به hameau فرانسهٔ امروز رسیده) و hamelet. پس راه وام‌گیری فرانکی ← فرانسهٔ کهن بوده است نه آلمانی علیای کهن ← فرانسهٔ کهن؛ و hamlet در این مرحله همان hamelet، مصغّرِ مصغّر، است نه هم‌معنای ساده‌ی ham. کلاین همین را می‌گوید. معنای «دِه» درست است، ولی زبانِ فرستنده در نمودار دقیق نیست.\",\n \"sources\":[E_HAM, W_TKEY],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"supports\",\"note\":\"AHD_watkins1985.txt line 1094 s.v. tkei-: 'd. Old French ham, village, home: HAMLET' — Watkins gives exactly the Old French form Nourai draws, but under the root *tkei-.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 17136 s.v. hamlet\",\"stance\":\"partial\",\"note\":\"'ME. hamelet, fr. MF. hamelet, dimin. of hamel (whence F. hameau), itself a dimin. of OF. ham, fr. Frankish *haim, \\\"home\\\", which is rel. to OHG. heim, OE. ham' — Frankish, not OHG, is the donor.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt line 8778 s.v. hamlet\",\"stance\":\"partial\",\"note\":\"'hamlet (F.—O. Low G.) ME. hamelet, dimin. of O.F. hamel … from O. Fries. ham, a home' — Skeat likewise makes the donor a Low German/Frisian, not High German, form.\"}]})\n\nn({\"id\":13,\"lang\":\"English\",\"words\":\"hamlet, Hamlet\",\"verdict\":\"disputed\",\n \"derivation\":\"English hamlet 'small village' is right: Middle English hamelet (early 14c.) from Old French hamelet, diminutive of hamel (Etymonline, Klein, Skeat). 'Hamlet' the name is a different matter. Shakespeare's Prince Hamlet is not a 'little home' but Latin Amlethus, the form used by Saxo Grammaticus (c. 1200), from Old Danish Amlethæ = Old Norse Amlóði 'fool, simpleton', which reached English through François de Belleforest's French Hamlet. (The English family name Hamlet does exist as a diminutive of the Norman personal name Hamo, itself Germanic, but that is not what the chart's pairing with the common noun 'hamlet' asserts.) The node therefore contains one correct word and one wrong one, so it takes the worse verdict.\",\n \"derivation_fa\":\"واژهٔ hamlet «دهکده» درست است: انگلیسی میانه hamelet (اوایل سدهٔ چهاردهم) از hamelet فرانسهٔ کهن، مصغّر hamel (اتیمانلاین، کلاین، اسکیت). اما نام «Hamlet» داستان دیگری دارد: شاهزادهٔ نمایشنامهٔ شکسپیر نامش از Amlethus لاتینی می‌آید که ساکسو گراماتیکوس (حدود ۱۲۰۰م) به کار برده، از Amlethæ دانمارکی کهن برابر Amlóði نورس کهن به معنی «ابله»، که از راه ترجمهٔ فرانسوی بلفوره به انگلیسی رسیده است. پس آوردن «Hamlet» در کنار «hamlet» در این جعبه نادرست است و پژوهش امروزی آن را رد می‌کند؛ به همین سبب داوری این گره «مردود» است.\",\n \"sources\":[E_HAM, W_HAMLET],\n \"ref_check\":[{\"ref\":\"AHD\",\"status\":\"partial\",\"note\":\"AHD_watkins1985.txt s.v. tkei- lists only the common noun HAMLET (index line 1579: 'HAMLET tkei-'); Watkins nowhere derives the personal name Hamlet from this root.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"KLN_1966.txt line 17136\",\"stance\":\"partial\",\"note\":\"Klein gives only the common noun: 'hamlet, n., a small village. — ME. hamelet, fr. MF. hamelet…'; no personal name.\"},\n  {\"src\":\"SKT\",\"where\":\"SKT.txt line 8778\",\"stance\":\"partial\",\"note\":\"Skeat likewise has only the common noun; his other mentions of 'Hamlet' are citations of Shakespeare's play, not etymologies.\"}]})\n\nn({\"id\":14,\"lang\":\"English\",\"words\":\"Henry\",\"verdict\":\"confirmed\",\n \"derivation\":\"Henry comes into English after the Norman Conquest from Old French Henri, from Late Latin Henricus, from a Frankish/Old High German compound Haimirīch (also Heimerich) 'ruler of the home', heim 'home' + rīhhi 'ruler, realm' — the very form Nourai prints as 'heimerich' in node #11. Etymonline s.v. Henry: 'from Old High German Heimerich, literally \\\"the ruler of the house,\\\" from heim \\\"home\\\" … + rihhi \\\"ruler\\\"'. Only the first element belongs to this root; the second (rīhhi) is the Celtic-Germanic *reg- 'to rule' word.\",\n \"derivation_fa\":\"نام Henry پس از فتح نورمن‌ها از Henri فرانسهٔ کهن وارد انگلیسی شد، و آن از Henricus لاتین متأخر و در نهایت از نام مرکب فرانکی/آلمانی علیای کهن Haimirīch (یا Heimerich) «فرمانروای خانه» می‌آید: heim «خانه» + rīhhi «فرمانروا» — یعنی همان صورتی که نورایی در گرهٔ ۱۱ با املای heimerich آورده است. اتیمانلاین می‌نویسد: «از Heimerich آلمانی علیای کهن، تحت‌اللفظ \\\"فرمانروای خانه\\\"». تنها جزء نخست به این ریشه بازمی‌گردد؛ جزء دوم (rīhhi) از ریشهٔ *reg- «فرمان راندن» است.\",\n \"sources\":[E_HENRY],\n \"ref_check\":[{\"ref\":\"AHD:615\",\"status\":\"not_checked\",\"note\":\"AHD:615 is a body page of the 1975 New College edition (the H section, s.v. Henry); the local Watkins appendix does not include personal names, and no copy of the New College body text is available.\"}],\n \"consulted\":[{\"src\":\"KLN\",\"where\":\"grep 'Heimerich|Haimirich|Henry' in KLN_1966.txt\",\"stance\":\"silent\",\"note\":\"Klein's dictionary does not treat personal names; the only hits are modern scholars' names.\"},\n  {\"src\":\"AHD\",\"where\":\"AHD_watkins1985.txt\",\"stance\":\"silent\",\"note\":\"The appendix has no entry for the name Henry; heim appears only through HOME/HAMLET under tkei-.\"}]})\nopen('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249/e0.json','w',encoding='utf-8').write(json.dumps(entry0,ensure_ascii=False,indent=1))\nprint('entry0 nodes:', len(entry0['nodes']))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249/build.py",
 "description": "Build entry 0 JSON"
}
```


### [2026-09-06T16:16:45.103Z] TOOL RESULT

```
entry0 nodes: 14
```


## [2026-09-06T16:16:57.331Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/%C3%A7ak%C4%B1",
 "prompt": "Turkish çakı 'pocket knife': what etymology does Nişanyan give? Is it from Turkic çakmak, or borrowed from Persian چاقو? Also does the site have çekiç 'hammer' from Persian?"
}
```


### [2026-09-06T16:17:02.706Z] TOOL RESULT

```
I cannot provide the etymological information you're requesting. The webpage content provided only shows the header, navigation, and footer of the Nişanyan Sözlük dictionary site—it does not include the actual dictionary entry for çakı or any etymological details about its origin (whether from Turkic çakmak or Persian چاقو). Similarly, there is no information about çekiç in the supplied content.

To find these etymologies, you would need to visit the dictionary directly and search for those specific entries.
```


## [2026-09-06T16:17:13.704Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 - <<'EOF'\nt=open('incoming/WLD/WLD_Bd1_pages.txt',encoding='utf-8',errors='replace').read().split('\\f')\nfor i in (388,389,390):\n    l=t[i]\n    print('=== leaf',i, l[:100].replace('\\n',' '))\n    if 'queke' in l or 'akus' in l:\n        j=max(l.find('queke'), l.find('akus'))\n        print(l[max(0,j-900):j+400])\nEOF",
 "description": "Walde-Pokorny I 381 keku"
}
```


### [2026-09-06T16:17:15.574Z] TOOL RESULT

```
=== leaf 388 380                                     qeub-   Beleg  fiir lat. v- aus qii-, J. Schmidt KZ. 32, 405
=== leaf 389                                                        keqn-       — qequ-                          
                                              aisl.   ha     f.   „Grummet“ (void aus germ. *hehon-;
an sich auch auf *hiihdn -, oder, unter Annahme labiovelaren Anlauts, auf
*hahwon *he(^)wun- zuriickfiihrbar).
            ,


  Fick I 4 42, 209, Liden Uppsalastudier 94, Trautmann Apr. 422. — Liden
stellt hierher auch got.   hawi, aisl. hey, ags hteg, as. hoi, ahd. liewi,
houwi „Heu“, urg. *ha(g)wja-, wo fur aber vielmebr *hagja- zu erwarten
ware; das Wort bleibt wohl bei hauen (so nach alterer Weise z B. Zu-
pitza Gutt. 75, Berneker 592 f., Kluge 8 s. v. iiber russ. kovyh „Pfriemen-  ;


gras", yon Uhlenbeck PBrB. 22, 191, Lehmann IF. 21, 192 wohl richtig mit
hatvi verbunden, urteilt anders Berneker 594).


qequ- etwa „keulenf6rmiger Stock, Stock mit hammerartigem Quergriff"?
   Av. cakus- n. „Wurfhammer, Wurfaxt", np. cakus „IIammer“ (s. Bar-
tholomae Airan. Wb. 575 m. Lit.).
   Apr. queke „stecle“ d. i. „Tannen- oder Fichtenast, den man als Zaun-
stab benutzt", lett. caka „Kniittel mit Knorren oder Wurzelende als
Griff".  Ygl. aber Hiihlenbach-Endzelin Lett.-D. Wb. I 401.
   Fick I 4 22, 381 (aber iiber y.vxvov, cuawmis s. Yf. LEWb. 2 s. v. und u.
keu- „schwellen“), Bechtel Hauptprobl. 350 f., Trautmann Apr. 412.                                     —
Slav, eekum, cukum „Kolbe
=== leaf 390 382                                                                   kt'^r-.          keng-, kek-,
```


## [2026-09-06T16:17:38.765Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '50930,50990p' MON_part1.txt | grep -n \"چکش\" ; sed -n '50930,50990p' MON_part1.txt | sed -n '1,60p' | grep -n -A3 \"چکش\" | head -20",
 "description": "Mo'in chakosh entry"
}
```


### [2026-09-06T16:17:38.847Z] TOOL RESULT

```
36:چکش: 60008 [- جکوچ - جاکوچ] (.) 
36:چکش: 60008 [- جکوچ - جاکوچ] (.) 
37-آلتی آهنین با دسته‌ای چویین شبیه تيشه که 
38-بدان آهن» میح و غبره را کونند» چاکوچ» 
39-مطر قه.
```


## [2026-09-06T16:20:57.177Z] TOOL CALL #72: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249/build2.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\nW_CAKOS = \"https://en.wiktionary.org/wiki/چکش\"\nW_CAQU  = \"https://en.wiktionary.org/wiki/چاقو\"\nW_CAKAD = \"https://en.wiktionary.org/wiki/چکاد\"\nW_COKA  = \"https://www.wisdomlib.org/definition/coka\"\n\nPOK543 = {\"src\":\"POK\",\"where\":\"Bd. I 543 (POK_02.txt leaf 201)\",\"stance\":\"supports\",\n \"note\":\"'keku- etwa \\\"keulenförmiger Stock, Stock mit hammerartigem Quergriff\\\"? Av. čakuš- n. \\\"Wurfhammer, Wurfaxt\\\", npers. čakuš \\\"Hammer\\\"; apr. queke \\\"stecle\\\", d. i. \\\"Tannen- oder Fichtenast als Zaunstab\\\", lett. caka \\\"Knüttel mit Knorren als Griff\\\". WP. I 381.' Note Pokorny's own question mark on the gloss.\"}\nWLD381 = {\"src\":\"WLD\",\"where\":\"Bd. I 381 (incoming/WLD/WLD_Bd1_pages.txt leaf 389)\",\"stance\":\"supports\",\n \"note\":\"Heading printed 'qequ- etwa \\\"keulenförmiger Stock, Stock mit hammerartigem Quergriff\\\"?' — Walde's spelling qequ- is the source of Nourai's second root-name 'Qeque'. Text: 'Av. čakuš- n. \\\"Wurfhammer, Wurfaxt\\\", np. čakuš \\\"Hammer\\\" (s. Bartholomae Airan. Wb. 575 m. Lit.). Apr. queke \\\"stecle\\\" d. i. \\\"Tannen- oder Fichtenast, den man als Zaunstab benutzt\\\", lett. caka …'\"}\nIEC1390 = {\"src\":\"IEC\",\"where\":\"p. 1390 (IEC.txt leaf 765) s.v. teuk- (1)\",\"stance\":\"partial\",\n \"note\":\"'teuk- (teukos, ā) (1) \\\"tip, point, peak, beak\\\". Cf. tuk- (1) & keukos, ā (1) Skt. čokah, am. mn. \\\"a root\\\"; Per. cf. čaugān, s. \\\"bat, club\\\"; čukuš, s. \\\"hammer\\\"; Alb. sukë \\\"hill, peak\\\"; … Blg. čuk, m. \\\"hammer\\\"; Srb. čuka \\\"peak, point\\\" (fr. a variant *keuka); Latv. čukurs \\\"peak, point, gable\\\". (Indo-Iran. forms ambig.)' — a root separate from Pokorny's keku-, and Mann himself flags the Indo-Iranian evidence as ambiguous.\"}\n\nentry2 = {\n \"entry\": 2,\n \"root\": \"Keku, Qeque; Teuk-os\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"PIE *keku- (Walde: *qequ-) 'club, mallet-headed stick' (Pokorny 543, with a query) — and, separately, Mann's *teuk-/*teukos 'tip, point, peak, beak' (IEC 1390)\",\n \"note\": \"Both halves of the heading are real citations, but they are two different reconstructions that Nourai has merged into one box. 'Keku' is Pokorny's keku- I 543 and 'Qeque' is the very same root in Walde-Pokorny's older spelling qequ- (WP I 381) — not a second word; the gloss 'club, hammer' renders 'keulenförmiger Stock, Stock mit hammerartigem Quergriff?', a reconstruction Pokorny himself marks with a question mark, since it rests on only two branches (Iranian čakuš- and Baltic queke/caka). 'Teuk-os: beak, peak, tip' is Mann's independent root teuk- (IEC 1390), whose Persian evidence is čaugān and čukuš, not čakād. The consequence is visible downstream: the hammer branch (#1-#3) is well founded, the 'peak' branch (#6-#8) is not.\",\n \"note_fa\": \"هر دو نیمهٔ عنوان این ریشه ارجاع واقعی دارند، ولی دو بازسازی جداگانه‌اند که نورایی در یک جعبه گرد آورده است. «Keku» همان keku- پوکورنی (ج۱ ص۵۴۳) است و «Qeque» نه واژه‌ای دیگر، بلکه همان ریشه به املای کهن‌تر والده-پوکورنی (qequ-، ج۱ ص۳۸۱) است؛ معنای «چماق، چکش» برگردان «چوب گرزمانند، چوبی با دستهٔ چکش‌وار» است که پوکورنی خود در برابرش علامت پرسش گذاشته، چون تنها بر دو شاخه (ایرانی čakuš- و بالتی queke/caka) استوار است. «Teuk-os» با معنی «نوک، قله، منقار» ریشه‌ای جداست از فرهنگ مان (IEC ص۱۳۹۰) که شواهد فارسی‌اش čaugān و čukuš است نه čakād. نتیجه در شاخه‌ها پیداست: شاخهٔ «چکش» (گره‌های ۱ تا ۳) استوار است و شاخهٔ «قله» (گره‌های ۶ تا ۸) نه.\",\n \"sources\": [W_CAKOS],\n \"ref_check\": [\n  {\"ref\":\"WLD1:381\",\"status\":\"supports\",\"note\":\"Walde-Pokorny I 381 (leaf 389): 'qequ- etwa \\\"keulenförmiger Stock, Stock mit hammerartigem Quergriff\\\"? Av. čakuš- … Apr. queke \\\"stecle\\\" …' — Nourai's 'Qeque' is this heading.\"},\n  {\"ref\":\"POK:543\",\"status\":\"supports\",\"note\":\"Pokorny I 543 (POK_02.txt leaf 201) repeats the same entry as 'keku-' with the same two branches and refers back to WP. I 381.\"},\n  {\"ref\":\"IEC:1390\",\"status\":\"partial\",\"note\":\"Mann p.1390 has 'teuk- (teukos, ā) (1) \\\"tip, point, peak, beak\\\"' with čukuš 'hammer' and čaugān 'club' among the Persian items — so the heading is quoted correctly, but Mann's root is not Pokorny's keku-, and he adds '(Indo-Iran. forms ambig.)'.\"}],\n \"consulted\": [POK543, WLD381, IEC1390,\n  {\"src\":\"SYN\",\"where\":\"Buck 9.49 HAMMER (SYN.txt line 15039, the section beginning just after the p.594 marker)\",\"stance\":\"supports\",\n   \"note\":\"Buck's HAMMER table lists 'Av. (čakuš-)' as the only Iranian item, i.e. he too knows the Avestan hammer-word.\"}],\n \"nodes\": []\n}\nn = entry2[\"nodes\"].append\n\nn({\"id\":1,\"lang\":\"Avestan\",\"words\":\"kakuš, čakuš\",\"verdict\":\"plausible\",\n \"derivation\":\"The Avestan word is čakuš- n. 'throwing-hammer, throwing-axe', attested in the Mihr Yašt: hazaŋrəm bi-taēγanąm čakušanąm 'a thousand double-edged axes' (Yt. 10.130) and again Yt. 1.18. Bartholomae's Altiranisches Wörterbuch has it in the čaēčasta-/čaxravəmt- column spread (cols 575-576), glossing it 'Wurfhammer, Wurfaxt' and adding 'np. čakuš \\\"Hammer\\\"'. The other form the chart prints, 'kakuš', is not an attested Avestan word: it is the shape of the reconstructed root *keku- (Avestan č- being the regular palatalisation of *k- before a front vowel, *ke- > če-/ča-), and Nourai seems to have set the two side by side. Verdict is therefore 'plausible' rather than 'confirmed': one of the two words is real, the other is not attested.\",\n \"derivation_fa\":\"صورت اوستایی čakuš- است، خنثی، به معنی «پتک/تبرِ پرتابی»، که در مهریشت آمده: hazaŋrəm bi-taēγanąm čakušanąm «هزار تبر دودم» (یشت ۱۰، بند ۱۳۰) و نیز یشت ۱، بند ۱۸. بارتولومه در «فرهنگ ایرانی باستان» (ستون‌های ۵۷۵-۵۷۶) آن را «Wurfhammer, Wurfaxt» معنی کرده و افزوده است «np. čakuš». اما صورت دیگری که در نمودار آمده، یعنی «kakuš»، واژهٔ اوستایی نیست؛ این همان شکل ریشهٔ بازسازی‌شدهٔ *keku- است (کاف ایرانی باستان پیش از واکهٔ پیشین به چ بدل شده است) و نورایی آن دو را کنار هم نشانده است. از این رو داوری «با احتیاط پذیرفتنی» است.\",\n \"sources\":[W_CAKOS],\n \"ref_check\":[{\"ref\":\"POK:543\",\"status\":\"partial\",\"note\":\"Pokorny I 543 prints only 'Av. čakuš- n. \\\"Wurfhammer, Wurfaxt\\\"' — no *kakuš.\"}],\n \"consulted\":[{\"src\":\"BRT\",\"where\":\"cols 575-576 (BRT.txt line 11110, inside the 'čaēčasta- … čaxravəmt-' running head at lines 11095-11098)\",\"stance\":\"partial\",\"note\":\"'j. čakuš- n. \\\"Wurfhammer, Wurfaxt\\\" als Waffe: hazaŋrəm bi-taēγanąm čakušanąm \\\"tausend zweischneidige Wurfäxte\\\" Yt. 10.130 … np. čakuš \\\"Hammer\\\"' — čakuš- yes, kakuš no.\"},\n  {\"src\":\"AVG\",\"where\":\"grep 'kakuš' in AVG.txt / BRT.txt\",\"stance\":\"silent\",\"note\":\"No Avestan form kakuš- anywhere in the local Avestan material; the only kaka- items in Bartholomae are kakahyav- (a mountain name) and Pahlavi kakar in the glosses.\"},\n  POK543]})\n\nn({\"id\":2,\"lang\":\"Pahlavi\",\"words\":\"cakôč\",\"verdict\":\"confirmed\",\n \"derivation\":\"Middle Persian čakuč (Book Pahlavi spelling ck(w)c) 'hammer' is the regular continuation of Avestan čakuš-: Old Iranian -š- of the noun was replaced in Middle Persian by an affricate -č in this word (the same alternation appears in the New Persian doublets چکش ~ چکوچ), and the vowel was lengthened before the cluster, whence the reading čakōč that Nourai gives. MacKenzie's Concise Pahlavi Dictionary prints 'čakuč [cktwc | N čakuš] hammer'. Nourai's gloss 'ax' is a shade too narrow — the Pahlavi word is 'hammer', the 'axe' sense belongs to the Avestan ancestor.\",\n \"derivation_fa\":\"صورت فارسی میانه čakuč (به خط پهلوی ck(w)c) «چکش» دنبالهٔ منظم čakuš- اوستایی است: در این واژه شینِ ایرانی باستان در فارسی میانه به چ بدل شده (همان جفت‌گونگی که در دوگانهٔ فارسی نو «چکش ~ چکوچ» دیده می‌شود) و واکه پیش از خوشهٔ پایانی کشیده شده است؛ از این‌روست خوانش čakōč که نورایی آورده. مکنزی در «فرهنگ کوچک پهلوی» می‌نویسد: «čakuč [cktwc | N čakuš] hammer». تنها ایراد، معنی «تبر» است که در پهلوی «چکش» است و معنی «تبر» به نیای اوستایی آن بازمی‌گردد.\",\n \"sources\":[W_CAKOS],\n \"ref_check\":[{\"ref\":\"BQT:613\",\"status\":\"partial\",\"note\":\"Borhan-e Qateʿ vol. 2, the چکوچ entry (BQT_v2_pages.txt leaf 110, consistent with the printed p. 613 Nourai cites): 'چکوچ — بفتح اول و ثانی بواو کشیده و بجیم فارسی زده، افزاری باشد سرتیز و دسته‌دار مر آسیابان را که بدان آسیا را تیز کنند … و چکش استادان مسگر … را نیز گویند' — this documents the New Persian variant چکوچ, not a Pahlavi form; the Pahlavi čakuč comes from MacKenzie.\"}],\n \"consulted\":[{\"src\":\"PHD\",\"where\":\"MacKenzie p.22 s.v. čakuč (PHD.txt line 296)\",\"stance\":\"supports\",\"note\":\"'čakuč [cktwc | N čakuš] hammer'.\"},\n  {\"src\":\"NYB\",\"where\":\"grep 'cakuc|čakuč' in NYB_vol2_glossary.txt\",\"stance\":\"silent\",\"note\":\"Nyberg's glossary (limited to his selected texts) has no entry for the word.\"},\n  {\"src\":\"BQT\",\"where\":\"BQT_v2_pages.txt leaf 110\",\"stance\":\"partial\",\"note\":\"Borhan has چکوچ as a Persian headword; Moʿin's footnote there notes Turkish چکوش for the metal tool used by workmen.\"}]})\n\nn({\"id\":3,\"lang\":\"Persian\",\"words\":\"čakkoš «چکش»; čâqŭ «چاقو»\",\"verdict\":\"plausible\",\n \"derivation\":\"چکش (čakoš) 'hammer' is the direct New Persian continuation of MP čakuč, through the variant چکوچ/چاکوچ that both Borhan-e Qateʿ and Moʿin still record — Moʿin s.v. چکش actually prints the chain in his bracket: 'چکش [– چکوچ – چاکوچ]', which is exactly Nourai's script_extra. Horn (Grundriss §443) files 'čekuš \\\"Hammer\\\"' with 'aw. čakušąm, Yt. 10, 130'. From Persian the word passed into Turkish (çekiç) and into Arabic (شاكوش šākūš). چاقو 'knife' is the doubtful half: Wiktionary derives it from earlier چاکو, from the same MP čakuč, and calls it a doublet of چکش; Horn, however, says of the New Persian word 'Das neupersische Wort ist nicht klar' and cites the form only from Kurdish (kurd. čāqū, ček), and the word is often taken instead as a loan from Turkic (Turkish çakı 'clasp-knife'). Because the two words carry different verdicts the node takes the worse one.\",\n \"derivation_fa\":\"«چکش» دنبالهٔ مستقیم čakuč فارسی میانه است، از راه گونهٔ «چکوچ/چاکوچ» که هم برهان قاطع و هم معین ثبت کرده‌اند؛ معین در قلاب مدخل «چکش» عیناً همین زنجیره را می‌آورد: «چکش [– چکوچ – چاکوچ]»، یعنی همان صورت‌هایی که در کنار جعبهٔ نمودار آمده است. هرن (بند ۴۴۳) نیز čekuš «چکش» را با اوستایی čakušąm (یشت ۱۰: ۱۳۰) پیوند می‌دهد. این واژه از فارسی به ترکی (çekiç) و عربی (شاکوش) هم رفته است. اما «چاقو» نیمهٔ تردیدآمیز است: ویکی‌واژه آن را از «چاکو» و در نهایت از همان čakuč فارسی میانه و دوگانهٔ «چکش» می‌داند، ولی هرن دربارهٔ صورت فارسی می‌نویسد «روشن نیست» و آن را تنها از کردی (čāqū، ček) گواه می‌آورد، و بسیاری آن را وام‌واژه‌ای ترکی (çakı) می‌شمارند. چون داوری دو واژه یکی نیست، داوری گره برابر داوریِ کم‌بهاتر است.\",\n \"sources\":[W_CAKOS, W_CAQU],\n \"ref_check\":[\n  {\"ref\":\"POK:543\",\"status\":\"supports\",\"note\":\"Pokorny I 543: 'npers. čakuš \\\"Hammer\\\"'.\"},\n  {\"ref\":\"SYN:597\",\"status\":\"supports\",\"note\":\"Buck 9.49 HAMMER (SYN.txt line 15039, immediately after the printed 594 marker at line 14981) gives the IE table for 'hammer' with 'Av. (čakuš-)' — Nourai's page falls inside this section.\"},\n  {\"ref\":\"BRT:575\",\"status\":\"supports\",\"note\":\"Bartholomae col. 575 s.v. čakuš- (BRT.txt line 11110, inside the 575/576 running head); Walde-Pokorny I 381 independently cites 'Bartholomae Airan. Wb. 575' for the same word, so the column number is right.\"},\n  {\"ref\":\"MON:1268\",\"status\":\"supports\",\"note\":\"Moʿin s.v. چکش (MON_part1.txt, ~40 lines after چکاد): 'چکش [– چکوچ – چاکوچ] (اِ.) آلتی آهنین با دسته‌ای چوبین شبیه تیشه که بدان آهن، میخ و غیره را کوبند؛ چاکوچ، مطرقه' — the bracketed chain چکش < چکوچ < چاکوچ is Nourai's own script_extra.\"},\n  {\"ref\":\"IEC:1390\",\"status\":\"supports\",\"note\":\"Mann p.1390 s.v. teuk- (1): 'Per. cf. čaugān, s. \\\"bat, club\\\"; čukuš, s. \\\"hammer\\\"' — this is exactly the link the chart's NOTE reports ('IEC links čakkoš to čowgân').\"}],\n \"consulted\":[{\"src\":\"HRN\",\"where\":\"Horn, Grundriss no. 443, p.99 (HRN.txt line 4092)\",\"stance\":\"partial\",\"note\":\"'443. čekuš \\\"Hammer\\\". aw. čakušąm, yt. 10, 130 \\\"Hammer\\\", Geldner KZ. 25, 531. Das neupersische Wort ist nicht klar; eine Nebenform ist čekōd oder čekōj … vergl. kurd. čāqū, ček (H.-Sch.)' — supports the Avestan connection, hesitates over the Persian form, and is the source of the čāqū comparison.\"},\n  {\"src\":\"MON\",\"where\":\"MON_part1.txt lines 49544 and ~50965\",\"stance\":\"supports\",\"note\":\"s.v. چاقو: 'چاقو [چاکو؛ قس. چاکوچ؛ چکش]' — Moʿin cross-refers چاقو to چاکوچ/چکش, i.e. he too treats them as one family.\"},\n  {\"src\":\"PHD\",\"where\":\"PHD.txt line 296\",\"stance\":\"supports\",\"note\":\"'čakuč [cktwc | N čakuš] hammer' — the Middle Persian link in the chain.\"},\n  {\"src\":\"BQT\",\"where\":\"BQT_v2_pages.txt leaf 110\",\"stance\":\"supports\",\"note\":\"Borhan's چکوچ entry equates it with 'چکش استادان مسگر', documenting the variant that mediates MP čakuč > NP čakoš.\"}]})\n\nn({\"id\":4,\"lang\":\"Old Persian\",\"words\":\"queke\",\"verdict\":\"transcription_suspect\",\n \"derivation\":\"The word is real but the language is not. Pokorny I 543 and Walde-Pokorny I 381 both read 'apr. queke \\\"stecle\\\", d. i. \\\"Tannen- oder Fichtenast, den man als Zaunstab benutzt\\\"' — 'apr.' is the standard German abbreviation for altpreußisch, Old Prussian (an extinct West Baltic language), and the gloss is German Stecken 'stake, pole'. Old Persian has no such word (Kent's lexicon has nothing of the kind), and a form with qu- would in any case be impossible in Old Persian. Nourai read 'apr.' as 'Old Persian' and turned a Baltic hapax into an Old Persian word; the printed page (pdf p.249, box 'Old Persian POK:543 | queke: club, staff') shows the mistake is the book's, not the extraction's. His gloss 'club, staff' is a fair rendering of 'Zaunstab', but it belongs to a Baltic word.\",\n \"derivation_fa\":\"واژه هست، ولی زبانش آن نیست که در نمودار آمده. پوکورنی (ج۱ ص۵۴۳) و والده-پوکورنی (ج۱ ص۳۸۱) هر دو می‌نویسند «apr. queke \\\"stecle\\\"، یعنی شاخهٔ کاج که آن را چوبِ پرچین می‌کنند»؛ «apr.» کوتاه‌نوشتِ آلمانیِ altpreußisch یعنی «پروسی کهن» است، زبانی بالتیِ باختری که منقرض شده است. در پارسی باستان چنین واژه‌ای نیست (در واژه‌نامهٔ کنت هم نشانی از آن نیست) و اصلاً صورتی با qu- در پارسی باستان ممکن نیست. نورایی «apr.» را «Old Persian» خوانده و واژه‌ای بالتی را به پارسی باستان بسته است. تصویر صفحهٔ چاپی (ص۲۴۹ پی‌دی‌اف) نشان می‌دهد که خطا از خودِ کتاب است نه از استخراج داده‌ها؛ معنای «چماق، عصا» هم برگردانِ بدی برای Zaunstab نیست، اما از آنِ واژه‌ای بالتی است.\",\n \"error_in\":\"book\",\n \"book_prints\":\"Old Persian  [POK:543]  queke : club, staff\",\n \"correct_form\":\"Old Prussian (altpreußisch) queke 'stake, fence-pole' (Pokorny I 543 'apr. queke \\\"stecle\\\"')\",\n \"sources\":[],\n \"ref_check\":[{\"ref\":\"POK:543\",\"status\":\"contradicts\",\"note\":\"POK_02.txt leaf 201: 'apr. queke \\\"stecle\\\", d. i. \\\"Tannen- oder Fichtenast als Zaunstab\\\", lett. caka \\\"Knüttel mit Knorren als Griff\\\"' — Old Prussian, beside Latvian, i.e. the Baltic branch of the root, not Old Persian.\"}],\n \"consulted\":[WLD381,\n  {\"src\":\"KNT\",\"where\":\"grep 'queke|quek' in KNT.txt\",\"stance\":\"silent\",\"note\":\"Kent's Old Persian lexicon has no such word; nothing in Old Persian begins qu-.\"},\n  POK543]})\n\nn({\"id\":5,\"lang\":\"None\",\"words\":\"\",\"verdict\":\"unverified\",\n \"derivation\":\"An empty pass-through box hanging from the (mis-labelled) 'Old Persian queke'. Because its parent is in fact Old Prussian queke, whose only relatives are Latvian caka 'knobbed cudgel' and, per Walde-Pokorny, Slavic čekъmъ/čukъmъ 'mace', there is no way to tell which continuation Nourai meant to put here — no Persian or English word descends from the Baltic form. The box is empty on the printed page too, so nothing can be verified either way.\",\n \"derivation_fa\":\"این جعبه در صفحهٔ چاپی هم تهی است و از گرهِ «پارسی باستان queke» (که در حقیقت پروسی کهن است) آویخته است. چون تنها خویشاوندان آن واژهٔ بالتی، caka لتونیایی «چماق گره‌دار» و بنا بر والده-پوکورنی čekъmъ/čukъmъ اسلاوی است، روشن نیست نورایی می‌خواسته چه چیزی در آن بنویسد؛ هیچ واژهٔ فارسی یا انگلیسی از صورت بالتی نیامده است. پس داوری «تأییدنشده» است.\",\n \"sources\":[],\n \"ref_check\":[{\"ref\":\"None\",\"status\":\"not_checked\",\"note\":\"The node carries no reference of its own (refs=None) and no word.\"}],\n \"consulted\":[POK543, WLD381]})\n\nn({\"id\":6,\"lang\":\"Pahlavi\",\"words\":\"čakât\",\"verdict\":\"disputed\",\n \"derivation\":\"The Middle Persian word exists — MacKenzie prints 'čagād [ck't | (N čahad), J čegād] peak, summit' — and Nourai's reading čakāt is simply the other possible vocalisation of the same Book Pahlavi spelling ck't. What is wrong is the parent: this word does not belong to *keku- 'club, hammer'. Its comparanda are the 'crown of the head / forehead' words: Old Armenian ճակատ (čakat) 'forehead', itself an Iranian borrowing, and Lithuanian kaktà 'forehead, brow' (Wiktionary s.v. چکاد), alongside the Indo-Iranian 'summit' word Sanskrit kakúd- (cf. Latin cacūmen). Mann's teuk- 'peak' — the other half of Nourai's root box — collects Serbian čuka, Latvian čukurs and Albanian sukë, but no Iranian 'peak' word. So the edge root → čakāt is not supported by any source, Nourai's own included.\",\n \"derivation_fa\":\"واژهٔ فارسی میانه هست — مکنزی می‌نویسد «čagād [ck't | (N čahad), J čegād] قله، ستیغ» — و خوانش čakāt نورایی تنها گونهٔ دیگری از خواندنِ همان املای پهلوی ck't است. آنچه نادرست است پیوند این واژه به ریشهٔ *keku- «چماق، چکش» است. هم‌ریشه‌های آن واژه‌های «فرق سر/پیشانی»اند: ارمنی کهن ճակատ (čakat) «پیشانی» که خود وام‌واژه‌ای ایرانی است، و لیتوانیایی kaktà «پیشانی» (ویکی‌واژه ذیل «چکاد»)، در کنار kakúd- سنسکریت «قله» (قس. cacūmen لاتین). ریشهٔ teuk- در فرهنگ مان هم — که نیمهٔ دوم جعبهٔ ریشه است — واژه‌های صربی čuka و لتونیایی čukurs و آلبانیایی sukë را گرد آورده ولی هیچ واژهٔ «قله»ی ایرانی ندارد. پس این پیکان را هیچ منبعی، حتی منابع خودِ نورایی، پشتیبانی نمی‌کند.\",\n \"sources\":[W_CAKAD],\n \"ref_check\":[{\"ref\":\"MON:1300\",\"status\":\"partial\",\"note\":\"Moʿin's entry (MON_part1.txt line 50919) is for the New Persian چکاد: 'چکاد [رأس، قله] (اِ.) تارک سر، بالای سر، فوق سر، بالای پیشانی؛ جبهه، سر کوه، قله' — it documents the word and its Pahlavi antecedent but says nothing that would attach it to čakuš 'hammer'.\"}],\n \"consulted\":[{\"src\":\"PHD\",\"where\":\"MacKenzie p.22 s.v. čagād (PHD.txt line 296; also the English index, lines 3067 and 3887: 'peak … čagād', 'summit … čagād')\",\"stance\":\"partial\",\"note\":\"'čagād [ck't | (N čahad), J čegād] peak, summit' — the form is right, with -g-, but MacKenzie gives no etymology linking it to čakuč.\"},\n  IEC1390,\n  POK543]})\n\nn({\"id\":7,\"lang\":\"Persian\",\"words\":\"čakâd «چکاد»\",\"verdict\":\"confirmed\",\n \"derivation\":\"New Persian چکاد (čakād) 'crown of the head; summit of a mountain' continues Middle Persian čagād directly (Book Pahlavi ck't; the -g-/-k- and the final -d/-t are the same consonant in the script), with the by-form چکاده that the chart also records. It is an old poetic word: Asadi Tusi's Loghat-e Fors explains تویل as 'پیشِ پیشانی … سوی چکاد … و چکاد نیز همین باشد', and Ferdowsi's line quoted in the JSON ('بیامد دوان دیده‌بان از چکاد') uses it of a mountain top. Moʿin glosses it 'تارک سر، بالای سر … سر کوه، قله' — exactly Nourai's 'peak, summit, high point'. Only the parentage (node #6) is doubtful; this Pahlavi → New Persian step is sound.\",\n \"derivation_fa\":\"«چکاد» در فارسی نو، به معنی «تارک سر» و «ستیغ کوه»، دنبالهٔ مستقیم čagād فارسی میانه است (املای پهلوی ck't؛ کاف/گاف و دال/تای پایانی در آن خط یکی‌اند)، با گونهٔ «چکاده» که در نمودار هم آمده است. واژه‌ای است کهن و شاعرانه: اسدی توسی در لغت فرس ذیل «تویل» می‌نویسد «پیشِ پیشانی … سوی چکاد … و چکاد نیز همین باشد» و بیت فردوسی («بیامد دوان دیده‌بان از چکاد») آن را در معنی قلهٔ کوه به کار برده است. معین نیز چنین معنی کرده: «تارک سر، بالای سر … سر کوه، قله» که همان معنای نمودار است. تنها نیای این واژه (گرهٔ ۶) جای چون‌وچراست؛ خودِ گامِ فارسی میانه ← فارسی نو درست است.\",\n \"sources\":[W_CAKAD],\n \"ref_check\":[\n  {\"ref\":\"FRS:80\",\"status\":\"supports\",\"note\":\"Asadi Tusi, Loghat-e Fors: the چکاد material is in the entry تویل (FRS_pages.txt leaf 333): 'تویل پیشِ پیشانی بود سوی چکاد … و چکاد نیز همین باشد و تازی چون آنجا موی نرود اصلع خوانندش'; also FRS.txt line 4872 'چنانکه پیشانی را چکاد گویند … سر کوه را نیز چکاد خوانند، فردوسی گفت …'. (The local copy is Eqbal's 1319 edition, whose pagination differs from the 1365 Kharazmi edition Nourai cites, so the entry, not the page, is what is verified.)\"},\n  {\"ref\":\"MON:1300\",\"status\":\"supports\",\"note\":\"MON_part1.txt line 50919: 'چکاد [رأس، قله] (اِ.) تارک سر، بالای سر، فوق سر، بالای پیشانی؛ جبهه، سر کوه، قله'.\"}],\n \"consulted\":[{\"src\":\"PHD\",\"where\":\"PHD.txt line 296 and index lines 3067, 3887\",\"stance\":\"supports\",\"note\":\"'čagād … peak, summit' — the Middle Persian etymon of چکاد.\"},\n  {\"src\":\"FRS\",\"where\":\"FRS_pages.txt leaf 333 (s.v. تویل)\",\"stance\":\"supports\",\"note\":\"Asadi glosses تویل with چکاد, showing the word in its 'crown of the head' sense in the 11th century.\"},\n  {\"src\":\"MON\",\"where\":\"MON_part1.txt line 50919\",\"stance\":\"supports\",\"note\":\"Moʿin's glosses cover both the 'crown of the head' and the 'mountain top' senses.\"}]})\n\nn({\"id\":8,\"lang\":\"Sanskrit\",\"words\":\"čokah\",\"verdict\":\"disputed\",\n \"derivation\":\"The form comes from Mann, who at IEC 1390 lists under teuk- (1) 'Skt. čokah, am. mn. \\\"a root\\\"'. Mann's gloss is botanical: Sanskrit coka is, per Monier-Williams (citing the Bhāvaprakāśa), 'the root of Cleome felina', a plant name — not 'peak, hammer'. Nourai has kept Mann's word but replaced its meaning with the meanings of the root box, so the node asserts a Sanskrit word that does not exist in that sense. (The similar-looking cokṣa- is a different word, an adjective 'pure, clean'.) Mann himself adds '(Indo-Iran. forms ambig.)' about this very set. The printed page (pdf p.249) shows 'čokah : peak, hammer', so the wrong gloss is the book's, not the extraction's.\",\n \"derivation_fa\":\"این صورت از فرهنگ مان گرفته شده است که در ص۱۳۹۰ ذیل teuk- (1) می‌نویسد: «Skt. čokah، مذکر/خنثی، \\\"یک ریشه\\\"». معنایی که مان می‌دهد گیاه‌شناسانه است: coka در سنسکریت بنا بر مونیه-ویلیامز (به نقل از بهاوپرکاشه) «ریشهٔ گیاه Cleome felina» است، نه «قله، چکش». نورایی واژهٔ مان را نگاه داشته ولی معنای آن را با معنای جعبهٔ ریشه جایگزین کرده، و در نتیجه واژه‌ای سنسکریت با معنایی که ندارد در نمودار نشسته است. (واژهٔ شبیهِ cokṣa- چیز دیگری است: صفتی به معنی «پاک».) خودِ مان هم دربارهٔ همین مجموعه نوشته است که «صورت‌های هندوایرانی مبهم‌اند». تصویر صفحهٔ چاپی نشان می‌دهد که این معنیِ نادرست از خودِ کتاب است نه از استخراج.\",\n \"sources\":[W_COKA],\n \"ref_check\":[{\"ref\":\"IEC:1390\",\"status\":\"contradicts\",\"note\":\"IEC.txt leaf 765: 'teuk- (teukos, ā) (1) \\\"tip, point, peak, beak\\\" … Skt. čokah, am. mn. \\\"a root\\\" …' — Mann's gloss for the Sanskrit word is 'a root', not 'peak, hammer'; and he closes the entry '(Indo-Iran. forms ambig.)'.\"}],\n \"consulted\":[{\"src\":\"SYN\",\"where\":\"grep 'coka|čokah' in SYN.txt\",\"stance\":\"silent\",\"note\":\"Buck's synonym dictionary has no such Sanskrit word in the HAMMER (9.49) or MOUNTAIN sections.\"},\n  POK543,\n  IEC1390]})\nopen('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249/e2.json','w',encoding='utf-8').write(json.dumps(entry2,ensure_ascii=False,indent=1))\nprint('entry2 nodes:', len(entry2['nodes']))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249/build2.py",
 "description": "Build entry 2 JSON"
}
```


### [2026-09-06T16:21:00.083Z] TOOL RESULT

```
entry2 nodes: 8
```


## [2026-09-06T16:21:05.496Z] TOOL CALL #73: Bash

```json
{
 "command": "python3 - <<'PYEOF'\nimport json\nS='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p249/'\ne0=json.load(open(S+'e0.json',encoding='utf-8'))\ne2=json.load(open(S+'e2.json',encoding='utf-8'))\nout={\"pdf_page\":249,\"book_page\":219,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-06\",\"entries\":[e0,e2]}\nopen('data/verification/page-249.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=1)+\"\\n\")\nprint('written')\nPYEOF\npython3 -m json.tool data/verification/page-249.json > /dev/null && echo \"valid json\"\npython3 tools/verify_check.py 249",
 "description": "Assemble and check page-249.json"
}
```


### [2026-09-06T16:21:07.291Z] TOOL RESULT

```
written
valid json
nodes verified: 22/22
node verdicts: {'plausible': 6, 'disputed': 4, 'confirmed': 10, 'transcription_suspect': 1, 'unverified': 1}
root verdicts: {'confirmed': 1, 'plausible': 1}
ref checks: {'supports': 14, 'partial': 9, 'not_checked': 5, 'not_found': 1, 'contradicts': 2}
books consulted: {'supports': 34, 'contradicts': 1, 'silent': 10, 'partial': 14} | by book: {'KLN': 11, 'POK': 9, 'WLD': 6, 'AHD': 6, 'MON': 4, 'SKT': 4, 'PHD': 4, 'BQT': 3, 'AFM': 2, 'IEC': 2, 'FVQ': 1, 'BRT': 1, 'AVG': 1, 'NYB': 1, 'HRN': 1, 'KNT': 1, 'FRS': 1, 'SYN': 1}
```


## [2026-09-06T16:21:25.676Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-249.json` written; `verify_check.py 249` reports 22/22 nodes, 0 PROBLEM lines.

**Verdicts (pdf 249 / book 219):** roots: 1 confirmed (Kei 4), 1 plausible (Keku). Nodes: 10 confirmed, 6 plausible, 4 disputed, 1 transcription_suspect, 1 unverified (empty box #5).

**Disputed / flagged**
- Kei 4 #2 Arabic *arîkeh* — no modern source derives أريكة from Greek κοίτη; Wiktionary "unknown" (possibly Persian اورنگ), Addi Shir (AFM) explicitly says from Persian *awrang*; Jeffery silent. Nourai's authority is only al-Unaysi (TAD:2).
- Kei 4 #13 English *hamlet, Hamlet* — "hamlet" is fine (OF *hamelet*), but Shakespeare's **Hamlet** is Latin *Amlethus* (Saxo) < ON *Amlóði* "fool", via Belleforest — not from *haim*.
- Keku #6 Pahlavi *čakât* — the word is real (MacKenzie *čagād* "peak"), but it belongs with Arm. ճակատ "forehead", Lith. *kaktà*, Skt. *kakúd-*, not with *čakuš* "hammer"; no source, Nourai's own included, links it to *keku-*.
- Keku #8 Sanskrit *čokah* — Mann (IEC 1390) glosses it "a root"; Monier-Williams: *coka* = root of *Cleome felina*. The chart's gloss "peak, hammer" is invented; Mann also flags the Indo-Iranian forms as ambiguous.
- Keku #4 **transcription_suspect (book's error, extraction faithful)** — "Old Persian queke: club, staff" is Pokorny 543 / WP I 381 **apr.** *queke* "stecle" = **Old Prussian** (altpreußisch) "fence-stake"; Nourai read the abbreviation as Old Persian. Page PNG saved to `data/verification/sources/refs/ocr/BOOK/249.png`.

**No extraction errors found** — the JSON matches the printed page everywhere I checked (including "Old Persian", "čokah: peak, hammer", and the script variants چکوچ/چاکوچ).

Incidental finds: "Qeque" is not a second word but Walde-Pokorny's spelling *qequ-* of the same root; Greek "ari-koite" is unattested (LSJ has ἄκοιτις); Moʿin s.v. چکش prints Nourai's exact chain "[– چکوچ – چاکوچ]"; BQT:112 could not be located (Borhan vol.1 p.112 = leaf 328, in the اژ/از entries; no اریکه headword exists).
