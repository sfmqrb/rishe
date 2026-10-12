# Verification process log — verify-page-482


## [2026-09-14T03:08:16.071Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 482 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-482.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-482.json. Write /home/sfmqrb/git/rishe/data/verification/page-482.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 482` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T03:08:17.115Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T03:08:17.959Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T03:08:17.976Z] TOOL RESULT

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


## [2026-09-14T03:08:18.384Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-482.txt"
}
```


### [2026-09-14T03:08:18.407Z] TOOL RESULT

```
1	=== PDF page 482 (book page 452) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Steu 2, Teu 2, Teup : to push, beat, hit, also throw  (refs POK:1032)
4	#1 (parent #0) [Avestan] refs=SNS:147 | tap 1 : to hit, hurt, destroy
5	  #2 (parent #1) [Persian] refs=SNS:147 | tabâh «تباه ( تبه )» : ruined, destroyed, bad | NOTE: IEC:1365 derives these words from Indo-European root "Tâbh: to rot"
6	#3 (parent #0) [Sanskrit] refs=POK:1034; SNS:147 | tup, tub : to hurt, destroy
7	#4 (parent #0) [Sanskrit] refs=POK:1032 | tuj : to press, push, throw
8	  #5 (parent #4) [Old Persian] refs=BQT:172; FFD:32 | ham-tauj, ham-taug, ham-taux : to throw together, pile up, store ☞Sem 1
9	    #6 (parent #5) [Pahlavi] refs=BQT:172; AEF:159 | ham-tôxtan, han-dôzh : to store, add up, save
10	      #7 (parent #6) [Persian] refs=BQT:171; AEF:159 | andŭxtan «اندوختن ( اندوزیدن )» : to save, store
11	#8 (parent #0) [Germanic] refs=AHD:1543 | staup : deep, projecting ; stubb : stump, stub ; stukkjam : fragment, covering
12	  #9 (parent #8) [English] refs=AHD | steep ; stub ; stucco
13	#10 (parent #0) [Latin] refs=AHD:1544 | stupěre : to be stunned, stupid ; studěre : pressing forward, study
14	  #11 (parent #10) [English] refs=AHD | stupid, stupendous, study, student
15	--- entry 1 ---
16	ROOT [Indo-European] Stewe : to cluster, condense  (refs POK:1035)
17	#1 (parent #0) [Sanskrit] refs=POK:1035; AHD | stupa : a round mass, ball
18	  #2 (parent #1) [Turkish] refs=HJB:933 | top, tob : ball, cannon ball
19	    #3 (parent #2) [Persian] refs=HJB:933; BQT:526 | tŭp «توپ» : ball, cannon
20	#4 (parent #0) [Greek] refs=AHD | stuppě : tuft, toe
21	  #5 (parent #4) [Latin] refs=AHD | stuppâre : to stop with toe
22	    #6 (parent #5) [English] refs=None | stop, stuff
23	--- entry 2 ---
24	ROOT Stha -> redirect to Stâ
25	--- entry 3 ---
26	ROOT Stig -> redirect to Steig
27	--- entry 4 ---
28	ROOT Stoigh -> redirect to Steigh
29	
```


## [2026-09-14T03:08:21.024Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-482.json",
 "description": "Read source JSON page 482"
}
```


### [2026-09-14T03:08:21.066Z] TOOL RESULT

```
{
  "pdf_page": 482,
  "book_page": 452,
  "entries": [
    {
      "root": {
        "name": "Steu 2, Teu 2, Teup",
        "lang": "Indo-European",
        "refs": "POK:1032",
        "gloss": "to push, beat, hit, also throw"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "SNS:147",
          "words": [
            {"translit": "tap 1", "gloss": "to hit, hurt, destroy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "SNS:147",
          "words": [
            {"translit": "tabâh", "gloss": "ruined, destroyed, bad", "script": "تباه ( تبه )"}
          ],
          "note": "IEC:1365 derives these words from Indo-European root \"Tâbh: to rot\"",
          "quote": {
            "text": "بسی شیر و دیو و پلنگ و نهنگ - تـبـه شد به چنگم به هنگام جنگ",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:1034; SNS:147",
          "words": [
            {"translit": "tup, tub", "gloss": "to hurt, destroy", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:1032",
          "words": [
            {"translit": "tuj", "gloss": "to press, push, throw", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Old Persian",
          "refs": "BQT:172; FFD:32",
          "words": [
            {"translit": "ham-tauj, ham-taug, ham-taux", "gloss": "to throw together, pile up, store", "script": null, "see": ["Sem 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "Pahlavi",
          "refs": "BQT:172; AEF:159",
          "words": [
            {"translit": "ham-tôxtan, han-dôzh", "gloss": "to store, add up, save", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "BQT:171; AEF:159",
          "words": [
            {"translit": "andŭxtan", "gloss": "to save, store", "script": "اندوختن ( اندوزیدن )"}
          ],
          "note": null,
          "quote": {
            "text": "ترک دنیا به مردم آموزند - خویشتن سیم و غله اندوزند",
            "poet": "Sa`dî"
          }
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD:1543",
          "words": [
            {"translit": "staup", "gloss": "deep, projecting", "script": null},
            {"translit": "stubb", "gloss": "stump, stub", "script": null},
            {"translit": "stukkjam", "gloss": "fragment, covering", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "steep", "gloss": null, "script": null},
            {"translit": "stub", "gloss": null, "script": null},
            {"translit": "stucco", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD:1544",
          "words": [
            {"translit": "stupěre", "gloss": "to be stunned, stupid", "script": null},
            {"translit": "studěre", "gloss": "pressing forward, study", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 10,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "stupid, stupendous, study, student", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Stewe",
        "lang": "Indo-European",
        "refs": "POK:1035",
        "gloss": "to cluster, condense"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:1035; AHD",
          "words": [
            {"translit": "stupa", "gloss": "a round mass, ball", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Turkish",
          "refs": "HJB:933",
          "words": [
            {"translit": "top, tob", "gloss": "ball, cannon ball", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "HJB:933; BQT:526",
          "words": [
            {"translit": "tŭp", "gloss": "ball, cannon", "script": "توپ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "stuppě", "gloss": "tuft, toe", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "stuppâre", "gloss": "to stop with toe", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "stop, stuff", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Stha",
        "redirect": "Stâ"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Stig",
        "redirect": "Steig"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Stoigh",
        "redirect": "Steigh"
      },
      "nodes": []
    }
  ]
}
```


## [2026-09-14T03:08:21.794Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-14T03:08:21.846Z] TOOL RESULT

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
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt` (truncated before the lexicon's h–z section, ~p. 208 on)
  `/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT_full.txt` (complete archive.org djvu text — use this for lexicon pages 208–215: haumavarga-, siyamam, etc.)
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


## [2026-09-14T03:08:57.931Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SNS','BQT','FFD','AEF','HJB','IEC','AHD','MON','ARY','PHD','CHEUNG','TTS','LKT','SKT','KLN','HRN','HUB','BRT','KNT','NYB','WLD','SYN','FSD','WEB','FRS']:\n    v=d.get(k)\n    print(k, json.dumps(v, ensure_ascii=False)[:600] if v else 'MISSING')\n\""
}
```


## [2026-09-14T03:08:58.611Z] TOOL CALL #6: Bash

```json
{
 "command": "ls data/verification/ | head -50 && echo --- && ls data/verification/page-48*.json 2>/dev/null"
}
```


### [2026-09-14T03:08:59.027Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_
SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه‌شناسی فارسی» (مهرافروز) print-only: https://www.gisoom.com/book/11154690/ ; German original: https://archive.org/details/grundrissderneu00horngoog", "lookup_hint": "Not online (searched archive.org, 
HJB {"title": "H. Yule & A. C. Burnell, Hobson-Jobson, 2nd ed. by W. Crooke, London 1903 (Delhi reprint 1968)", "edition_found": "1903 Crooke edition (pagination identical to the 1968 reprint)", "kind": "archive_djvu", "url": "https://archive.org/details/hobsonjobsonagl02croogoog", "identifier": "hobsonjobsonagl02croogoog (others: bub_gb_6Z5iAAAAMAAJ, hobsonjobsonglos00yulerich, india.history.resource.89053)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HJB.txt", "page_offset": "leaf = printed + 35..51 (plates inserted; e.g. leaf 83 = p.32, leaf 319 = p.270, leaf 535 = p.4
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-
CHEUNG MISSING
TTS {"title": "H. Vámbéry, Etymologisches Wörterbuch der turko-tatarischen Sprachen, Leipzig 1878 (repr. Osnabrück 1972)", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/etymologischesw00vmuoft (Toronto scan; also Google/bub_gb copies)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/TTS/TTS_vambery1878_uoft_djvu.txt"], "page_offset": 
LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W
FRS {"title": "Asadi Tusi, Loghat-e Fors, ed. Mojtaba'i & Sadeqi, Kharazmi 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/LughatEFurs-AbuMansurAliBinAhmadAsadiTusiFarsi (Abbas Eqbal's 1319/1940 Tehran edition); also dli.ernet.439493 / dli.ernet.437743 (Horn's 1897 Göttingen edition, 'Lughat Faras')", "lookup_hint": "Look up the headword (entries grouped by final letter); FRS_pages.txt has \\f page breaks (567 leaves). Pagination differs from the 1365 Kharazmi edition Nourai cites — verify the entry, not the page.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/s
```


### [2026-09-14T03:08:59.080Z] TOOL RESULT

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
data/verification/page-48.json
```


## [2026-09-14T03:09:01.281Z] TOOL CALL #7: Bash

```json
{
 "command": "sed -n 1,120p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T03:09:01.331Z] TOOL RESULT

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


## [2026-09-14T03:09:03.776Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== POK 1032 area ===\"; python3 - <<'EOF'\nimport re\n# POK_01 leaf = p + 8 ; POK_02 leaf = p - 344 ; find which file has p 1032\nimport os\nfor f,off in [('POK_02.txt',-344),('POK_03.txt',None)]:\n    print(f, os.path.exists(f))\nEOF\ngrep -n \"page_offset\" -A2 /home/sfmqrb/git/rishe/data/verification/sources/refs_online.json | head -5"
}
```


### [2026-09-14T03:09:04.848Z] TOOL RESULT

```
=== POK 1032 area ===
POK_02.txt True
POK_03.txt True
22:  "page_offset": "vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...').",
23-  "covers_etymology": true,
24-  "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
--
74:  "page_offset": null,
```


## [2026-09-14T03:09:08.704Z] TOOL CALL #9: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['POK']['page_offset']); print(d['POK'].get('lookup_hint'))\""
}
```


## [2026-09-14T03:09:09.577Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; for f in POK_02.txt POK_03.txt POK_full.txt; do echo \"== $f\"; grep -n \"steu-\" $f | head -20; done"
}
```


### [2026-09-14T03:09:09.780Z] TOOL RESULT

```
POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>
Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/pokorny-etymological-dictionary/ (entry pages with page numbers) and StarLing https://starlingdb.org/cgi-bin/query.cgi?basename=\data\ie\pokorny&root=config
```


### [2026-09-14T03:09:10.847Z] TOOL RESULT

```
== POK_02.txt
== POK_03.txt
3404:mit  anderer  Bedeutung:  ahd.  stiura,  mhd.  stiure  , Stütze,  Steuerruder, Unterstützung,  Steuer',  nhd.  Steuer  f.  und  (aus  dem  Nd.)  n.,  ags.  steor  f. (Steuerruder',  aisl.  styri  n.  , Steuerruder',  mnd.  stür(e)  n.  , Steuerruder',  f. n.  ,Regierung;  Hilfe,  Gegenwehr',  f.  ,Unterstützung',  got.  us-stiurei  ,Zü- gellosigkeit',  mnd.  unstüre  ds.,  got.  stiurjan  »feststellen,  behaupten',  nhd. iur  Steuer  der  Wahrheit,  aisl.  styra  ,ein  Schiff  steuern;  regieren',  ags. Hieran  ds,,  ahd.  stiurren  , stützen,  steuern,  lenken';  wohl  ursprüngl.  , Pfahl, Steuerruder  (sekundär:  damit  stützen,  lenken)',  mit  aisl.  staurr,  gr.  atav- P<^S  (s.  oben)  unter  *steu-ro-:*st9u-ro-  vereinbar,  das  von  *st(h)äu-  nicht ganz  getrennt  werden  könnte;
3407:zu  ai.  sthürd-  usw.  stellt  sich  wohl  idg.   steu-ro-   ,Stier  (und^ Großvieh/:
4629:7.  a:  das  Wort  für  Stier:  gr.  lavQog,  alb.  tarok,  lat.  taurus,  osk.  ravQOfi^ umbr.  turuf,  toru  ,tauros',  apr.  tauris  ,Bison',  lit.  tauras  ds.,  aksl.  turb ,Auerochs'  (Trautmann  315,  Vasmer  3,  154),  entweder  aus  idg.  *tduro-s  (vgl. ai.  tüm-ra-  , strotzend'  als  Beiname  des  Stieres),  oder  wegen  des  orienta- lischen Stierkultes  mit  ursemit.  Hauru  (arab.  twr)  zusammenhängend;  gall. tarvos  (mir.  tarh,  cymr.  tarw),  venet.  ON  Tarvisium,  wohl  nach  kelt.  carvos ,Hirsch'  umgestaltet;  aisl.  pjöii-,  ndl.  dial.  deur  usw.,  sind  nach  aisl.  stjörrj ahd.  stior  umvokalisiert,  deren  Bedeutung  wiederum  von  unserem  Worte beeinflußt  ist  (s.  oben  idg.  *steu-ro-  S.  1010);
== POK_full.txt
81356:support, steer)', with Old Icelandic staurr, gr. araupoc; (see above) under *steu-ro- : *stau- 
81359:to Old Indie sthura- etc. stellt sich probably Indo Germanic steu-ro- ^buW (and anderes 
82919:Root / lemma: steu-2 
86733:Germanic *steu-ro-S. 1010);
```


## [2026-09-14T03:09:13.167Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '82890,82990p' POK_full.txt"
}
```


### [2026-09-14T03:09:13.227Z] TOOL RESULT

```
with the tongue anstoften, stottern'; 

from *steub{h)-ma, *stoub{h)-ma: cymr. ystumi. "bend, turn, shape', bret. stumm6s. 
(ins Irish borrowed Middle Irish stuaimmi. " ability, capacity '), also "Fluftbiegung'; dastum 
"das Einsammein' (Loth RC. 48, 354 ff); compare Old English stupian. 

Old High German stobaron "obstupere'; 

Old Icelandic 5/J/^"stump', Middle Low German stufM]. "dull', stuven= Old Icelandic 
s/y/& "abstumpfen, cavitate '; Old Icelandic stofn^ stump, foundation '; Old English stofn 
ds.. Old Icelandic stubbr, sfubb/m. "stump, trunk'. Old English stybbn. " stump '; 

with Germanic -p-: Old Icelandic stupa' tower'. Old English stupian, mnl. stupen's\c\r\ 
biJcken'; ablaut. Old English steap'\r\\g\r\, ragend' (engl. steep ^ steep'). Middle High 
German 5/0^/" hochragender rocks' {Hohestaufen), Middle High German stiefsieep"; Old 
Icelandic staupu. "hole, goblet'; Old English steap. Old High German Middle High German 
s/o^rgoblet'; Old English stoppa^ bowl, basin, bucket, pail '; from "abgestutzt = stolen; 
looted ' expounded sich Old Icelandic s^i/p- "Stief-' (s^t7p/'"Stiefsohn'), Old English steop-. 
Old High German stiof-, stiuf-. Modern High German Stief-, Old English abe-stTepan^vnuq, 
rob', a-st/eped\eoj\/a\st'. Old High German ar-, bi-stiufan^Vc\e parents or the Kinder 
berauben'; 



Latvian staupe^ Pferdefufltapfen '; stupe, stups^ Besenstumpf; (ruptured, broken) rod'. 

References: WP. ll615ff.,WH. II 608ff., Trautmann 331, Vasmer3, 109, 160. 
Page(s): 1032-1034 

Root / lemma: steu-2 

Meaning: to praise 

Note: only indo-iran. under gr. 

Material: Old Indie stauti, stavateetc. "lobt, praises ', participle stuta- "gepriesen', stutf-i. " 

laudation, praise ', stotar- "Lobsanger' etc., Avestan s/ac»///"lobt, praises, besingt; prays ', 



participle stuta-, stuiti-, staotar-etc, extended Old Indie stobhatr praises, jauchzt'; gr. 
areuTai '(*ruhmt sich) verspricht boasting '. 
References: WP. II 620. 
Page(s): 1 035 

Root / lemma: steue- 
Meaning: to get dense or tight 

Note: perhaps stau-, stau-. stuW\Vc\ stai-\ sff-: s//-a-"sich verdichten, stocken' as 
extension eines *sta- auffaftbar 

Material: Old \n6\c ghrfa-stavah Akk. PI. ' lard, drip'; prthu-stu-^W\\h a breiten Zopfe', st'u-k- 
a, stuka-m. " tuft of wool, Flocke', stoka-m. 'drip', with the meaning-development " clots, 
roundish thing', probably Latvian s/J^/s 'Wickelkind' and Old Indie stuka-m. "kid, child, the 
young of an animal '; Old Indie stu-p-a-, stupa- m. "Haarschopf, gr. *aTunr|, aTumrn " 
oakum ' (out of it Latin stupa, stuppa ds); gr. OTucpu) "pull together, make dense, hard, 
schmecke herb', GTOppa "zusammenziehendes tool ', gtui^jk; "dasZusammenziehen, 
Beizen', arOnTiKO^ "zusammenziehend', oiQ(p6q, OTOcppoc;, OTucpvoc; "herb, 
zusammenziehend', oiu[}vdq "tight, firm, compact '; perhaps gr. otu^, oiu\/6q in PI. 
"durchdringender frost, Eiseskalte', OTuyoc; n. "(* shudder, shiver) repugnance, hate', 
GTuysu) " hate, verabscheue, dread', yet compare above S. 1033; 

Church Slavic studb studb "coldness', s/K/7(?//"erkalten' and stydetT be ashamed' 
("*solidify, congeal '); russ. istygnutb, stugnutb " congeal, freeze '. 

References: WP. II 620, Vasmer 3, 33 ff. 
Page(s): 1 035 

Root / lemma: steib(h)-, sffb(h)-, steip- sffp- 

Meaning: pole, stick; stiff 

Material: 1 . steib(h)-, sfib(h)- Old Indie stibhi- m. "Rispe, tussock '; gr. aTi(pp6(; "dense 

(zusammengedrangt), tight, firm, strong', aiTcpoq n. "Zusammengedrangtes, heap'; 

Armenian step "frequent, often', as Subst. " power, compulsion ', stipem "drange, force, 
coerce '; gr. OTsipu) "make dense, trete tight, firm, betrete', aTinT6(; "tight, firm, thickset ', 
GTipapoq ds., GTipoq m. "the betretene path, track ', aix^do,, -aSoc; " lair from Streu or straw 
etc.', GTOipn "das Stopfen, Ausstopfung', OTOipa^u) "haufe an', afipn " hoarfrost '; 

Old Church Slavic stbbib, stbb/o {russ. stebelb) " stalk', stbb///e^KaKa[}r\'; Lithuanian 
s/5/Z?/a/"Schienbeine', st/ebas^ stick, pillar, mast ', Latvian s//Z?a "staff, rod', Old Prussian 



s//Z?//7/s'Schlittenbein', Lithuanian s/Zib/s "membrum virile': Litliuanian st/ebt/s 's\ch high 
uplift, set up', Latvian s//Z?/'betaubt become', Lithuanian s//ei6'5s "staff, pillar, mast ', 
Latvian sf/ebrs' bulrush'. 

2. steip-, sffp-. Latin stipes, -itisxx\. "picket, pole, stem, shaft, pole', stTpo, -are "dense to 
press together, pile up, collect, accumulate, gedrangt vollstopfen', obsfipus " sideways 
willing, inclined'; 

with I stipulai. " stem, straw'; unclear are stips, st/p/s' currency, gift, Spende'; 
s/!^eA7o'/i//77"Soldatenlohnung, tax, tribute, pay, guerdon, reward ' {*stipi-pendiom), stipulor, 
-^/"/""bedinge mirfrom'; Umbrian steplatu, 5//p/5/c»"stipulat5'; 

gr. PN IfiTTOJv to *aTTno(; = Old English stTf, Middle High German (actually md.) stTF stiff 
erect', besides Old Frisian stef{7); Middle Low German s//Ve'/e"pad', Middle High German
```


## [2026-09-14T03:09:14.185Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"lemma: (s)teu\" POK_full.txt; grep -n \"lemma: steu\" POK_full.txt; grep -n \"lemma: teu\" POK_full.txt"
}
```


### [2026-09-14T03:09:14.330Z] TOOL RESULT

```
7517:{ve- 5/7///-e (participle of alb. 5/7/KA7y"push with difficulty') see Root /lemma: (s)teu-1\ "to 
8097:in alb. shtynj, shtyj'poke, push' {*studnid)\ see Root / lemma: (s)teu-1\ "to push, hit' 
82766:Root / lemma: (s)teu-1 
82919:Root / lemma: steu-2 
82936:Root / lemma: steue- 
86424:Root / lemma: teuk- 
86439:Root / lemma: teu-1, teud- teug- teuk-, teup- 
86443:Root / lemma: teu-2 
86462:Root / lemma: teup- 
86485:Root / lemma: teus- 
86536:Root / lemma: teu- teu-, teua-, tuo- tu-
```


## [2026-09-14T03:09:19.175Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '82766,82800p' POK_full.txt; echo \"=== teu sections ===\"; sed -n '86424,86500p' POK_full.txt"
}
```


### [2026-09-14T03:09:19.285Z] TOOL RESULT

```
Root / lemma: (s)teu-1 

Meaning: to push, hit 

Note: with conservative extensions 

Material: A. (s)teu-k-. gr. tuko(; 'hammer, chisel; battle axe ', tukI^u) "bearbeite stone ', 

TUKOvri 'Dreschvorrichtung' (by Hes. Turavn); Old Irish /o//" hollow', /c»//'cave, hole' {*tukslo- 

), cymr. /m/// 'foramen', adj. "perforatus', bret. /c»^//'hole'; probably Old High German duken 

'press, niederdriJcken', Old English dy{a)n, deo/7 'press, constrain, oblige, prick' (see 

accurately under tuengh-' beset'), 

Latvian tukstet^ knock', taucet"\n mortar stampfen', russ. -Church Slavic /stbkngt/ 
'effodere'. Old Church Slavic thkat/^to weave, prick', etc.; 

maye alb. {*stuk) //7^/r' mortar' common alb. s- > th- 

Old Icelandic styggr^ au^vj , irate, unfriendly', nl. stug, older stugge^ stiff, unfriendly, 
abstoftend' can originally 'abstossend' and ' stiff ' sein and in letzteren case with 
Lithuanian stukt/{see below) under sfeo'p^-'steif dastehen' combined become. 

B. (s)teu-g-. Old Indie tujati, tunjati, /^/75/r//"throngs, stoftt', Med. 'kommt in schnelle 
Bewegung'; 



Middle Irish tuagi. "axe' and "bow', newer stuag, /Ja^a//77 "hit with the axe', tocht'part, 
piece'; expressives *sfoukka\n bret. studh^ arrowhead, feather', stuc'henn^ fascicle, 
sheaf, Brotschnitte' (nir. stuaic^ tableland, hill, plateau, cusp, peak' etc. is brit. loanword); 
compare Modern High German Stuck = " piece ' and 'Stauche' {LoVc\ RC. 42, 320 ff.); 

=== teu sections ===
Root / lemma: teuk- 

Meaning: sprout, seed, offspring 



Material: Old Indie tuc-i. 'Kinder, progeny ' (besides tuj-t ds. with folk etymology 
extension of the Tenuis); tokamu. " progeny, Kinder'; tokman-u. "young stem, sprout', 
Avestan taoxman-n. " seed, sperm, germ, sprout', PI. " kinship'. Old pers. taumat ' family, 
seed, sperm, germ, sprout'; khotansak. tt/man-n. " seed, sperm ', np. turn, afghan. toma^ 
seed, sperm '; Middle High German o'/e/7/e/''grandchild, grandson'. 
References: WP. I 713, VasmerS, 149, Mayrhofer 508, 527; 
See also: perhaps to teu-k- "to swell', above S. 1081 {teu-). 
Page(s): 1 085 

Root / lemma: teu-1, teud- teug- teuk-, teup- 
See also: see above S. 1032 ff. under (s)teu-. 
Page(s): 1 079 

Root / lemma: teu-2 
Meaning: to listen to, observe 

Material: Latin tueor, -en, tuitusdx\(^ tutatus sum' beirachten, observe, shield ', intu(e)or 
"consider', originally in-, ob-, con-tuor con-tud; /J/^s "certainly'; Old Irish cumtuth' 
protec\.\or\'{*kom-uc/-tou/tus), mcymr. /i/d"cover', tudec/'s\eeve, wrapping, dress', bret. dial. 
/^ec(abret. *tudoc) "Kissenbezug'; Old Irish /Jas-ce/Y "northern', bret. /^5 "links' {*teu-sto-)\ 
Celtic *feu-to-'\n mcymr.M" magician ', Middle Irish tuatha/dds., Old Irish /J5///7 "northern', 
Middle Irish tuath'Wnks, northern, mad, wicked, evil' (from "*gunstig, good' as Antiphrasis 
zur appellation the ungliJckbringenden Linken); in addition Gothic A'/Z/A'"das Gute', Old 
Icelandic f^ydr'mM, friendly', f^yda' friendship'. Old English gedfede'good, tugendhaft', 
gedTedan ' s\c\r\ (friendly) anschlieften'; probably also Old English deaw' custom, custom'. 
Old Saxon thau, Old High German gethau 'D\sz\p\'\n' as "*observantia'; perhaps also gr. 
Tuaasi iK£T£U£i Hes. (denominative eines *tut6(; with similar meaning as Gothic P/uf^Jan 
"segnen' from P/'uf^). 

References: WP. I 705 f., WH. II 713 f.. Loth RC 43, 160 ff. 
Page(s): 1079-1080 

Root / lemma: teup- 

Meaning: to get down, conceal oneself 

Material: Gr. £VTuna(; Adv., II. 24, 163, if meaning "cowering, crouching'; presumably Old 

Icelandic f^optat " thwart ' ("auf the gehockt wird'). Old High German doftai.. Middle Low 

German duchti.. Old English doftds. (wherefore Old Icelandic t^optixw. " Mitruderer', Old 

English ^edc»//a "comrade'. Old High German gidufto' Mitruderer, comrade') and Gothic 



I=>iubjd^ clandestine ', t^iubs^\h\ef, Old Icelandic t^jofr, Old English deof. Old Saxon thiof, 
Old High German oVioZ? 'thief; 

Lithuanian tupiu, tupt/'s\ch hinhocken, in die Knie place', tup/'u, tupetr crouch, in den 
Knien sit', Latvian tupt^ crouch '. 

References: WP. I 714. 
Page(s): 1 085 

Root / lemma: teus- 

Meaning: to empty 

Material: Avestan Kaus. taosayeiti^ makes loose, allows loose' {*touseid), Inchoativ {*tus- 

sRo) Avestan fus9n's\e verlieren die Fassung', baluci fusag, thuay' abandon become'; 

Old Indie tuccha-, tucchya- {*tus-sRo-, *tus-sR-Jo-) " empty, bare, lacking, deserted, 

abandoned, forsaken, worthless', afghan. tas^ empty, bare, lacking'; Latin tesquau. PI. 

"Einoden' {*tueskua)\ Old English dost^ manure'. Old High German dostds. 

("*Ausleerung'); Old Church Slavic tbstb ' kevoc,' , russ. tosc/j" empty, bare, lacking; lean,
```


## [2026-09-14T03:09:28.143Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '82800,82890p' POK_full.txt"
}
```


### [2026-09-14T03:09:28.198Z] TOOL RESULT

```
presumably Lithuanian s/^/7^/s"Messerstumpf', stukt/^\n die Hohe ragen'; and Old 
Church Slavic tbstati s^^a-nviybzxV; 

Swedish stuka^ dazzle, blind with bright light', Norwegian s/5^/r5 "bump, poke, injure, 
stottern', mnl. nnd. s/J/re/7"bump, poke, stratify, layer, astonish'. Modern High German 
verstauchen {irom dem Low German), Dutch verstuiken^ dislocate, luxate, crick '; Old 
Frisian stak^ stiff ' to Norwegian stauka; 

Middle Low German s/o/re/7 "prick, stochern', engl. dial, s/o/re "das fire schijren'. Modern 
High German stoche(r)n\ without aniaut. s-: Old Icelandic t^oka^ move, change, go'. Old 
English dc»ce/75/7"umherlaufen'; 

Old High German Middle High German stoc, -ekes 'Stock, staff, tree truck' (probably 
"*abgeschlagener bough or stem', compare abstocken). Old English 5/occ "stick, stem, 
stump'. Old Icelandic stokkr'tree truck, picket, pole, block ', next to which with the 
meaning " stiff Low German stuck, Middle High German Modern High German stocken' 
stiff become'; Old Icelandic stykki. Old English stycce. Old High German stucki. Modern 
High German Stuck' piece '; 

Old High German stuhhai.. Middle High German stuchem. f. "weit offener Armel am 
Frauengewand (actually Armelstumpf), Kopftuch', Modern High German Stauche, Middle 
Low German s/J/re "stump, further Armel'; with u. Old English stocut "long Armel'; 

manche neigen zur assumption eines meaning-Kernes " stiff ' (from which "bump, poke' 
has evolved), and for comparison with Lithuanian stukt/"\n die Hohe stand' (Old Lithuanian 
staug/net/" amb\e' , actually " stiff, stolpernd go'); compare russ. stugnutb " congeal, freeze 
(*stiff, rigid become?)', gr. aruysc; PI. "Eiskalte', GTuyoc; n. "repugnance, hate', aTuysu) " 
hate, verabscheue, dread', gtu^. Gen. aTUY6c;f. "das Verhaftte, frost'; FIN Itu^, see below 
S. 1035; 

dubious and only under the assumption from " ablaut derailment ' possible is die 
affiliation from Gothic s//gc75/7"zusammenstossen with', ^5-s//^^5/7"anstossen', Old 
Icelandic s/0/r/ri/5 stem V. "spray', Intr. "break, crack, spring, fall, run'; Old English st/ncan' 
whisk, steam, whirl up; stink'. Old Saxon Old High German stincan 'stink, smell'; Kaus. Old 



Icelandic st0kkva \er\agen, sprinkle', Old English 5/e/7ca/7 "scatter', Middle High German 
steuken 'st\nk make'; Old Saxon stank, stunk, Old English stenc^smeW, odor, fetidness ', 
Old High German stanc^ds., also fragrance '. 

C. (s)teu-d- Old Indie tundate, tudat/ ^stoflt, stachelt, sticht', toda- m. "Stachler, Lenker'; 
Armenian t'ndal, /'/7o'e/'erschuttert become'; 



from Gr. presumably names as TuSsuc;, TuvSapswc;; doubtful Tuvvoq ' |jiKp6(; ' ('*grind ', 
Old Indie tunna-1 (under the influence of common Celtic -ns-, -nt- > -nn-), rather babble- 
word with consonant stretch as tut96(; " totally small; young '); 

alb. shtynj^ poke, push' {*studn/d); 

Latin tundo -ere, tutudfbump, poke, hit, hammer', tudes, -///s 'hammer', tud/tare Wo\ent 
bump, poke', probably also tuss/s' cough ' (if in addition Umbrian tuderl\nem', tuderato 
"finitum', so that "limit, boundary' actually "Endpunkt; whereof man anstoftt'?); studeo, -ere 
"sich ernstlich worum bemijhen, eager betreiben, sich befleiftigen', stud/um ^Streben, 
eagerness ' ("*whereupon aim' from "whereupon hit'); 

Maybe alb. tund' shake' a Latin loanword. 

Old Irish do-tu/tlaWV (das /of PI. -tu/ttet^rom * -to-tud/ontj; abret. ar-stud' cuspis ', bret. 
as/^z "Ungeziefer', cymr. cystudd 'pa\n', etc.; 

Gothic stautan {0\6 Icelandic stautasdcm. V.), Old Saxon stotan. Old High German 
5/oz5/7"bump, poke'; Middle High German Modern High German stutzen'\N\t\r\ den 
Hornern Stolen, sudden stillestehen, zuriJckprallen', Middle High German 5/c»/ze"stem, 
clot, chunk'; Old Icelandic steytr. Old High German stoz' shove '; Old High German st/'uz. 
Modern High German S/e/yS(with md. e/for eu) actually "*abgestutzter Korperteil' 
(compare Modern High German S/c»/?"die Schwanzfedern of Vogels in the jargon spoken 
by hunters '); 

Old Icelandic stutr'horn, stump, ox'. Middle Low German s//7/"thigh, rump'; Swedish 
Norwegian 5/0/5 "stottern, stumble'. Modern High German (Low German) 'stottern' due to 
of nasal present Old Icelandic s/^///" "short'. Old English 5/j//7/a/7 "stutzen' 

D. ^s^te^-p- (occasionally -t>-, -b^-) "bump, poke'; also "stick, stump'. 

Old Indie p/'a-5/i//77yoa//(uncovered), topat/, tupat/, tumpati, tumpat/^ siofhi', tupara-' 
unhorned '; 



gr. TUTTTOo "hit', tutto(; "blow, knock, Eindruck'; GTUTTa^si ppovrg, iiJOcpsT cbGsT Hes., 
oiuTToq "stick, Stiel, stalk'; with -b^^- GTucpsAi^u) "hit, mifthandle', aTU(pA6(; "rough, stony '; 
about aTU(p£A6(; "herrisch' s. Leumann Homer. Worter 269 f.; 

Latin stuprum^ shame', esp. "die Entehrung through lubricity ' (originally "die dafiJr 
verhangte Prijgelstrafe'?); stuped, -ere^ rigid stand; betaubt, betreten sein, stutzen', 
s/^yOe/7o'i/s"erstaunlich, staunenswert'; with -t{H)- perhaps ///£/M/'e"wankeln, strauchein, 
with the tongue anstoften, stottern';
```


## [2026-09-14T03:09:40.746Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== AHD steu ===\"; grep -n \"steu-\\|steu2\\|stupa\\|steua-\" AHD_watkins1985.txt | head -40"
}
```


### [2026-09-14T03:09:40.823Z] TOOL RESULT

```
=== AHD steu ===
222:sta-. V. Zero-grade extended root *sti- (< *stuo) . . . VI. Secondary full-grade form *“steua-...
999:nare, to make firm, establish (dé-, thoroughly; see de-): DESTINE; b. Latin obstindre, to set one’s mind on, persist (ob-, on; see epi): OBSTINATE. 8. Suffixed form *séa-tu- in Latin status, manner, position, condition, attitude: STATE, STATISTICS, STATUS. 9. Suffixed form *sto-dhlo- in Latin stabulum, standing place: STABLE. 10. Suffixed form *si-dhli- in Latin stabilis, standing firm: ESTAB- LISH, STABLE!. 11. Suffixed form *sf-td- in Greek -statés, one that causes to stand, a standing: -sTAT; ENSTATITE. III. Zero-grade form *st-, *st()- (before vowels). 1. Reduplicated form *si-sio)- in: a. Latin sis- tere, to set, place, stop, stand: ASSIST, CONSIST, DESIST, EXIST, INSIST, INTERSTICE, PERSIST, RESIST, SUBSIST; b. Greek histanai (aorist stanai), to set, place: APOSTASY, CATASTASIS, DIASTASIS, ECSTASY, EPISTASIS, EPISTEMOL- OGY, METASTASIS, PROSTATE, SYSTEM; Cc. Greek histos, web, tissue ( < “that which is set up”): HISTO-; HISTIO- cyTE. 2. Compound form *iri-st-i-, “third person stand- ing by” (see trei-). 3. Compound form *por-st-i-, “that which stands before” (*por-, before, forth; see per’), in Latin postis, post: PosT!. 4. Suffixed form *st-o- in compound *upo-st-o-, “one who stands under” (see upo). IV. Extended root *std@u- (< *staau-), becoming *stau- before consonants, *stdw- before vowels; basic meaning “stout-standing, strong.”’ 1. Suffixed extended form *staw-d in Germanic *st6w6 in Old English stéw, place: stow. 2. Probable o-grade suffixed extended form *stow-yad in Greek stoa, porch: STOA, STOIC. 3. Suffixed extended form *stau-ro- in: a. (i) Latin instaurdre, to restore, set upright again (in-, on; see en): STORE; INSTAURATION (ii) Latin restaurdre, to restore, rebuild (re-, anew, again; see re-): RESTORE; b. Greek stauros, cross, post, stake: STAUROLITE. 4. Variant *tau-ro-, bull (see tauro-). V. Zero-grade extended root stii- (< *stua-). Suffixed form “*sti-lo- in Greek stulos, pillar: STYLITE; AMPHISTYLAR, ASTYLAR, EPISTYLE, HYPOSTYLE, PERI- STYLE, PROSTYLE, STYLOBATE. VI. Secondary full-grade form *steua-. Suffixed form *steua-ro- in Sanskrit stha- vira-, thick, stout, old: THERAVADA. VII. Variant zero-grade extended root *stu-. Suffixed form *stu-t- in Old English stuthu, studu, post, prop: STUD'. VIII. Sec- ondary full-grade form *steu-. 1. Suffixed form *steu-raé in Germanic *steur6, “a steering,” in Old English stéor, a steering: STARBOARD. 2. Germanic denominative *steur- Jan in: a. Old English stieran, to steer: STEER}; b. Old Norse styra, to steer, with its derivative stjérn, a rudder, a steering, akin to the possible source of Middle English sterne, stern of a boat: STERN?. 3. Suffixed form *steu-ro-, a larger domestic animal, in Germanic *steu- raz, ox, in Old English stéor, steer: STEER?. 4. Probably Germanic diminutive *steur-ika- in Old English stirc, stierc, calf: sTIRK. See stak-. [Pok. std- 1004.]
1026:Middle Dutch stuyver, stiver: STIVER. II. Extended form *steud-. 1. Nasalized form *stu-n-t- in Germanic *stunt- jan in Old English styntan, to dull: stinT!. 2. Germanic *staut- in: a. Old High German stézan, to push: sTOss; b. Middle Low German and Middle Dutch stéten, to force, akin to the source of Middle English stutten, to stutter: sTUTTER. III. Extended form *steug-. 1. Ger- manic *stukkaz in: a. Old English stocc, tree trunk: stock; b. Old High German stoc (> German Stock), staff: ALPENSTOCK; Cc. Old French estoc, rapier, sword point: TUCK’, 2. Germanic *stukkjam in: a. Old High German stukki, crust, fragment, covering: SHTICK; b. Italian stucco, stucco: stucco. 3. Germanic *stok- in Dutch stoken, to poke, thrust: sTOKER. IV. Suffixed (stative) zero-grade extended form *stup-é- in Latin stupére, to be stunned: STUPENDOUS, STUPID; STUPEFY. V. Suffixed (stative) extended zero-grade form *stud-é- in Latin *studére, to be diligent (< “to be pressing for- ward”): STUDENT, STUDY. VI. Extended zero-grade form *stug- in Greek Stux, the river Styx (< “hatred”): Styx. VII. Variant zero-grade form *tud-. 1. Latin tudes, ham- mer: TOIL!. 2. Suffixed form *tud-ti- in Latin tussis, cough: TussIs. 3. Nasalized form *tu-n-d- in Latin tun- dere, to beat: CONTUSE, OBTUND, PIERCE, RETUSE. VIII. Variant zero-grade form *tup-. 1. Suffixed form *tup-o- in Greek tupos, a blow, mold, die: TYPE; ANTI- TYPE, ARCHETYPE. 2. Nasalized form *tu-m-p- in Greek tumpanon, drum: TYMPANUM. [Pok. 1. (s)teu- 1032.] steu(e)-. To condense, cluster. Possible root. 1. Extended form *stip- in: a. Greek stuppé, tuft, tow: STOP, STUPE; b. Sanskrit stipah, tuft of hair, crown of the head: STUPA. 2. Extended form *stibh- in Greek stuphein, to contract: sTYPTIC. [Pok. steua- 1035.]
```


## [2026-09-14T03:09:42.342Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT tap ===\"; grep -n \"^tap\\|tap-\\b\" BRT.txt | head -30; echo \"=== BRT search 'tap' entries ===\"; grep -n \"tap, taf\\|1tap\\|2tap\\|tap  \" BRT.txt | head -20"
}
```


### [2026-09-14T03:09:42.416Z] TOOL RESULT

```
=== BRT tap ===
=== BRT search 'tap' entries ===
4206:spmtap  Yt.Ä38='.
```


## [2026-09-14T03:09:51.281Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1020,1026p' AHD_watkins1985.txt | cut -c1-4000"
}
```


### [2026-09-14T03:09:51.375Z] TOOL RESULT

```
ster-*, Star. 1. Suffixed form “ster-s- in Germanic “ster- rén- in Old English steorra, star: STAR. 2. Suffixed form *stér-ld- in Latin stélla, star: STELLAR, STELLATE; CON- STELLATION. 3. Oldest root form “aster- in Greek astér, star, with its derivative astron, star, and possible com- pound astrapé, asteropé, lightning, twinkling (< “looking like a star”; Ops, stem op-, eye, appearance; see okw-): ASTER, ASTERIATED, ASTERISK, ASTERISM, ASTRAEA, ASTRAL, ASTRO-; ASTEROID, ASTRAPHOBIA, DISASTER, Sterope. 4, Iranian stem *s¢dr- in Persian sitareh, star: ESTHER. [Pok. 2. ster- 1027.]
ster-4. To rob, steal. 1. Possibly dissimilated form in Germanic *ste/an in Old English stelan, to steal: STEAL. 2. Germanic derivative noun *stél-ithé (-ithd, abstract suffix) in Middle English stelth, stealth: STEALTH. 3. Ex- tended dissimilated form in Germanic frequentative *stalkon in Old English *stealcian, to move stealthily: STALK?. [Pok. 3. ster- 1028.]
ster-5. Barren. Latin sterilis, unfruitful: STERILE. [Pok. 6. ster- 1031.]
(s)ter-n-. Name of thorny plants. Extension of ster-1. Suffixed zero-grade form *tr-n-u- in Germanic *thurnu-, thorn, in Old English thorn, thorn: THORN. [Pok. 7. (s)ter-n- 1031.]
(s)teu-. To push, stick, knock, beat; with derivatives referring to projecting objects, fragments, and certain related expressive notions and qualities. I. Extended forms *steup-, steub-. 1. Germanic *staup- in Old English stéap, lofty, deep, projecting: STEEP!. 2. Germanic *staupilaz in Old English stypel, st@pel, steeple: STEEPLE. 3. Germanic *steup-, “bereft” (< “pushed out”), in Old English stéop-, step-: STEP-. 4. Germanic *stip- in Old English stipian, to stoop: stoop}. 5. Germanic expres- sive form *stubb- in Old English stubb, stybb, stump: STUB. 6. Germanic *stuf-, “fragment,” small coin, in
steu(8)-
Middle Dutch stuyver, stiver: STIVER. II. Extended form *steud-. 1. Nasalized form *stu-n-t- in Germanic *stunt- jan in Old English styntan, to dull: stinT!. 2. Germanic *staut- in: a. Old High German stézan, to push: sTOss; b. Middle Low German and Middle Dutch stéten, to force, akin to the source of Middle English stutten, to stutter: sTUTTER. III. Extended form *steug-. 1. Ger- manic *stukkaz in: a. Old English stocc, tree trunk: stock; b. Old High German stoc (> German Stock), staff: ALPENSTOCK; Cc. Old French estoc, rapier, sword point: TUCK’, 2. Germanic *stukkjam in: a. Old High German stukki, crust, fragment, covering: SHTICK; b. Italian stucco, stucco: stucco. 3. Germanic *stok- in Dutch stoken, to poke, thrust: sTOKER. IV. Suffixed (stative) zero-grade extended form *stup-é- in Latin stupére, to be stunned: STUPENDOUS, STUPID; STUPEFY. V. Suffixed (stative) extended zero-grade form *stud-é- in Latin *studére, to be diligent (< “to be pressing for- ward”): STUDENT, STUDY. VI. Extended zero-grade form *stug- in Greek Stux, the river Styx (< “hatred”): Styx. VII. Variant zero-grade form *tud-. 1. Latin tudes, ham- mer: TOIL!. 2. Suffixed form *tud-ti- in Latin tussis, cough: TussIs. 3. Nasalized form *tu-n-d- in Latin tun- dere, to beat: CONTUSE, OBTUND, PIERCE, RETUSE. VIII. Variant zero-grade form *tup-. 1. Suffixed form *tup-o- in Greek tupos, a blow, mold, die: TYPE; ANTI- TYPE, ARCHETYPE. 2. Nasalized form *tu-m-p- in Greek tumpanon, drum: TYMPANUM. [Pok. 1. (s)teu- 1032.] steu(e)-. To condense, cluster. Possible root. 1. Extended form *stip- in: a. Greek stuppé, tuft, tow: STOP, STUPE; b. Sanskrit stipah, tuft of hair, crown of the head: STUPA. 2. Extended form *stibh- in Greek stuphein, to contract: sTYPTIC. [Pok. steua- 1035.]
```


## [2026-09-14T03:10:04.647Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG andoz/handoz ===\"; grep -n \"handōz\\|handoz\\|andūxtan\\|anduxtan\\|andōxtan\\|handōxtan\\|hndwz\\|hndwht\" CHEUNG.txt | head -30; echo \"=== CHEUNG tauč ===\"; grep -n \"tauč\\|\\*tauc\" CHEUNG.txt | head -30"
}
```


### [2026-09-14T03:10:04.717Z] TOOL RESULT

```
=== CHEUNG andoz/handoz ===
25239:Pres.: IND. 3sg. BMP ’/hndweyt /(h)andozed/; Inf.: BMP ’/hndwhtn /(h)andoxtan/; Part.: perf. pass. 
25240:MMP hndwxt, BMP "/hndwht /(h)andoxt/; Pass.: pres. IND. 3р1. MMP hndwcyhyynd 
=== CHEUNG tauč ===
```


## [2026-09-14T03:10:07.066Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD ===\"; grep -n \"handōxtan\\|handōz\\|hndwhtn\\|handoz\" PHD.txt PHD_mackenzie.txt | head -20; echo \"=== NYB ===\"; grep -n \"handōxtan\\|handōz\\|hndwhtn\" NYB_vol2_glossary.txt | head -20; echo \"=== HRN anduxtan ===\"; grep -n \"andūḫtan\\|andūchtan\\|anduchtan\\|andōchtan\" HRN.txt | head -20"
}
```


### [2026-09-14T03:10:07.153Z] TOOL RESULT

```
=== PHD ===
PHD.txt:394:handāxtan, handāz- [hnd@htn', hnd?c- | M hnd?c-, № an~] plan, allot, reckon, judge. ~išn: judgement. handāxtār [%nd”%t”[] planner. handāz-, ~išn, v. handaxtan. ~ag [hnd?ck! | N andáza] measure, manner; ~ 1: like. handēmān [hndym’n' | = M] before, in the presence of. ~th: audience, presence. handēmānģar [kndym’ nkl] introducer (into the presence). „lt: introduction. handéSidan, handēš- [Ahndyti-ytn! | M hndy§-, N an~] think, consider, reflect. išn: thought, reflection. handēšīdār [hndyfyt?I] thoughtful. handēxtan, handēz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. „-išn(īh): acquisition. handraxtag [hndl htk! | P ?ndrxt] oppressed. ~ih: oppression, suffering. handüdan, *handāy- [hndwtn' | (M ?nwd), N an~] smear, plaster, anoint. hangad [hngt! | P ?ngd] fortunate, rich. ~ih: fortune, wealth. hangām [hng’m | N ~] time, occasion. ~ig [-yk!] timely. hangarag [hng’lk' | N angara] reckoning. hangardan, hangàr- [hng’l-tn' | M hng^r-, N an~] consider, reckon. ~išn: consideration. hang��xtan, hangéz- [hngyhtn', hngyc- | (M hgjyn-), N an~] arouse, stimulate, stir up. ~išn: arousing. hangirdénidan, hangirdén- [hngityn-ytn'] complete, summarize. hangirdig [kngltyk'] complete, perfect; summary. ~ih: completion, summary. hangdSidag [hngw£ytk! | M ”ngwšydg] way, manner, likeness. ~ 1: like. hanģrāyīdan [hngl’dytn'] lament. hangrüdag [hnglwtk'] lamenting. hanj-, v. hixtan. hanjaftan [hncptn' | P hnjft, (M hnzpt)] be finished. hanjāftan, hanjām- [hnc’tn', hnm- | P hnj ft, hnjm-, (M hnzpt, N anjāmīdan)] finish, complete, carry out. hanjām [kne m | N anjám] end, completion, outcome. hanjaman [hncmn! | (P ?njmn, M hnzmn), N anjuman] gathering, assembly, congregation, community. ~ig [-yk'] (notable) member of the community. hanjīdan [hnc-ytn' | N ~] = hixtan.
PHD_mackenzie.txt:2809:handfixtan, handoz- [hndwhtn l , hndwc- I N an-] gain, acquire, amass.
PHD_mackenzie.txt:5913:acquisition handozisn, windisn.           agility ~abukih.
=== NYB ===
1895:handóxtan [hndwhtn'] to collect, to ac- quire, to gain 73°12, — MPrs pres. pass. 3d p. pl. ’ndweyhyynd (Sogd 165. 17); Paz. NP andodtan, NP also andozidan; < ham + tóxtan (g. v.). :
=== HRN anduxtan ===
```


## [2026-09-14T03:10:11.814Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '25190,25270p' CHEUNG.txt"
}
```


### [2026-09-14T03:10:11.888Z] TOOL RESULT

```
pt’w’z ‘he endured’, dur. CSogd. pt’w’sq (GMS: §644); Partic.: pres. BSogd. pt’’wyn’k ‘patient’ 
*CHORESMIAN: t’w’n ‘compensation, fine’ (< NP) 

*BACTRIAN: TOOL, тоо ‘means, assets’, тооооуо, тоооуо ‘fine, Compensation’ 
=> S-W, Bact.: 226a 

*NWIR: NP tavänistan/tavän-, Kurd. tiwänin, Awrom. taway/taw-, Gil. (Rsht.) tan-, 
Gur. (Kand.) -tauw-/-tàü, Isfah. tunän (supplet. ša- < *x8aH), Khuns. tünis, Natan. 
-ton-est/ton-, Shamerz. -tün- (-ton-), Siv. tan-, ten-/tänis ‘to be able’ 

*NEIR: Oss. I. tyx, D. tux& ‘power, might’ 

*SANSKRIT: (ol ‘to be strong’ (RV) > EWAia I: 638 

*PIE *teuHoj- ‘to swell, be strong’ = LIV: 639 f. | Pok.: 1080 ff. 


*IE COGNATES: RussCS tyti ‘to become fat’, ? Gr. oa.og ‘healthy’ (Peters 1980: 290) 
*REFERENCES: KPF II: 190; Christensen, Contributions I: 61, 257; Christensen, Contributions II: 156; 
Abrahamian 1936: 132; MacKenzie 1966: 110; WIM I: 73; Abaev, Slovar’ III: 344 f.; WIM II: 117; 
Benzing 1983: 609; Werba 1997: 290 f. 


*tauj! ‘to impel, hasten’ 

*MIDDLE PERSIAN: (+ *pari-) MMP prdwz ‘impulse, thrust, energy’ = DMMPP: 
278a 

*NEIR: Oss. I. tynzyn, D. tunzun/tunst ‘to hasten, hurry, press on’. © The stem of the 
Oss. forms matches the Skt. pres. stem ѓийја-. The connection with Chor. tnc- ‘to 
hasten, hurry’, cited by Abaev, Slovar’ III: 338 f., is incorrect: the impf. stem t’ncy- 
clearly points to an original stemvowel *-a-. 

*SANSKRIT: toj ‘to impel, drive, set in motion’ (RV) © EWAia I: 670 

*PIE *(s)teug- ‘to set in motion, impel’ = LIV: 602 | Pok.: 1032 f. 

*IE COGNATES: MWelsh estwng ‘to yield, budge’, NHG stauchen ‘to thrust’, ? Gr. 


ocvyéo ‘I hate, loathe’ 
*REFERENCES: MacKenzie 1979: 531; Werba 1997: 191; Plath 2000: 409 ff. 


*tauj2 ‘to acquire, gather, gain’ 

*MIDDLE PERSIAN: (+ *ham-) MMP ’ndwc-, MMP hndwxt (pret. stem), BMP 
"/hndwc- / (h)andoz-/ ‘to gain, acquire, amass’ = DMMPP: 180b 

Pres.: IND. 3sg. BMP ’/hndweyt /(h)andozed/; Inf.: BMP ’/hndwhtn /(h)andoxtan/; Part.: perf. pass. 
MMP hndwxt, BMP "/hndwht /(h)andoxt/; Pass.: pres. IND. 3р1. MMP hndwcyhyynd 


*KHOTANESE: (+ *ham-) hadaj- ‘to accumulate, assemble’ 
*NWIR: NP töxtan/töz- ‘to acquire, gain, collect’ || (+ *ham-) NP andöxtan/andöz- ‘to 
acquire, collect’ 


388 *tauj3 


*SANSKRIT: ? tuj- ‘offspring’ (RV 4.1.3, 5.41.9), tujáye (inf) ‘to procreate’ 
c EWAia I: 652, fn. 

The precise origin of *tauj’ is unclear. The root postulated here may be related to 
BSogd. twö’k, CSogd. twdy, MSogd. twoyh ‘heap, mass’, NP tödah ‘mass(es)’ 
(without an "enlargement" *-j-). See also *,Өџа(п). 


*PIE — 2 LIV: — | Pok.: 1080 ff. 
*REFERENCES: Horn 1893: 89 f.; Nyberg II: 95a; DKS: 450a; Cabolov 2001: 330 


WIR ‘to (re)pay, pay back (a debt, fine, vel sim.), expiate’ 
*MIDDLE PERSIAN: MMP twz- ‘to expiate, pay for’, BMP twc- /toz-/ ‘to pay a debt, a 


fine; to give back, return anything (borrowed)! = DMMPP: 331a 

Pres.: IND. 3sg. BMP tweyt /tozed/, 3р1. MMP twzynd
```


## [2026-09-14T03:10:40.054Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN ===\"; grep -n \"andōḫtan\\|andôchtan\\|andūz\\|andōz\\|anduz\\|tōḫtan\\|toechtan\" HRN.txt | head; sed -n '/andōḫtan/,+3p' HRN.txt | head -5; echo \"=== HRN p89 area: leaf=printed+21 => leaf 110 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==111' HRN.txt | head -60"
}
```


### [2026-09-14T03:10:41.124Z] TOOL RESULT

```
=== HRN ===
=== HRN p89 area: leaf=printed+21 => leaf 110 ===
— 89 —
395. tund schnell, heftig, stark'.
aw. Hvant" (= Hnvant-), [/'tav-, vergl. tuvan (No. 401).
396. tunder, tundur ^Donner .
Vergl. ai. i/^tan-, tdnyati erschallen, laut tönen,
rauschen', tanayitnü- 'donnernd', tanyatii' 'Donner';
lat. tonare, tonitnis; ags. pnnjan, punor, nhd. Donner^
engl, thufider,
397. tenuk *düun, zart, fein'.
ai. tanu-, tdnuka- *dünn, fein\
kurd. tenik; oss. f(wäg (248); bei. tanak, n. fana/,
fanaU (377); sar. tanük,
398. teng 'en^Q,
aw. tahcista- (Superl. von ta/tna- 'kräftig'); phlv. tanf/
eng', tmigih 'Enge'; arm. fanjr 'dicht' (H. No. 110).
kurd. tenk *enge; bei. tank, n. tanJc, tahanH (378);
af/. tangat/l; wsi/, t^mg, sar. tong,
Vergl. auch Bartholomae, Studien II, 44, 51.
399. tenlden 'drehen, spinnen', tede 'Spinnengewebe*, tane
'Zettel, Aufzug (am Webstuhl)'.
aw. [/^tan-; phly, tatak, vd. 7 (36) (für aw. täfdaena-):
ai. |/"^aw-, tanoti, 'dehnen, spannen'.
400. tHj tu, tö (FirdüsT)^) 'du, vergl. -et 'dein', -tan 'euer'.
ap. iuvam 'du'; aw. tum, tväm, tu, tava; päz. tö {tu);
ai. tvdm, tdva; arm. du 'du' (H. No. 85).
kurd. ttr, af/. ta (obliqu. tä, di); oss. d. du, t. di
(112).
401. tuvan 'vermögend, mächtig', tuvanä, tuvanisten.
aw. i/^taV' 'können, vermögen', tavä[cä; phl. tuvän
(geschrieben J^D-n), tuvämk, tuvän(i)stan; ai. l^tav-,
tavlti; arm. tevem 'bleiben, dauern, aushalten, Stand
halten (H. No. 273).
402. töften 'sammeln; ausgeben, zahlen', Praes. töz-em;
'k^Tin-TND 'Vergeltung' (Is. 34, 11; 35, 4).
*) Die Aussprache tö ist zwar nicht überliefert, sie ist aber wohl
bei FirdQsi in den Fällen anzunehmen , wo das WorMhetrisch lang
gemessen wird, z. B. Öflhn. I, 189 Vers 1080 und sehr oft. Vergl. dö
*zwei'.
```


## [2026-09-14T03:10:44.996Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==112' HRN.txt | head -40"
}
```


### [2026-09-14T03:10:46.083Z] TOOL RESULT

```
— 90 —
phlv. töxtan , töjet 'büssen (übersetzt aw. l^cdy-
*büssen'), töj(i)sn 'Strafe, Busse; arm. toiz *Einbusse,
Strafe', tiigan , tu^em 'bestrafen*, tti^im 'bezahlen,
büssen', tuganem, ttiganim (Hübschmann, No. 276).
Eine ältere Form ist nicht vorhanden. Die Grund-
bedeutung scheint im Neupersischen 'sammeln' zu
sein^). Geiger, Ostiranische Kultur S. 35 Note 1
will aw. taozya- (vd. 1, 20) an die, so viel ich sehe,
nicht belegte Bedeutung 'Plünderung von np. töz
anschliessen, doch ist dies ganz unsicher.
403. töle 'junger Hund' (SF).
aw. {spO) taiirimö; phlv. taritk (vd. 13 (45), y. 10
(21), Bund.), türuk bezw. töruk (vd. 5 (98), Var.,
Thonnelier)-); ai. tdruna-; kurd. tüle (LW.) junger
Hund, Jagdhund'.
Dagegen np. töre 'Schakal' ^) (g. törCy Käs. törä, türe^
tiird s. V. röbah und seyäl); phlv. törak (PPGl.); kurd.
tiire 'Otter' (H.-Sch.) ; bei. tölag, n. May 'Schakal' (398).
Np. töle etc. beruhen auf «-Epenthese.
404. tih 'leer', tiht, tehi, ^mn (Is. 19, 3).
g. tohl,
aw. tusen^^ie entleeren sich' (Bartholomae, Studien
n, 52); phlv. tuhik 'leer; ai. tuöchyä-, skr. ^wccÄa- 'leer'.
bei. tnsag , n. fusay ausgehen, erlöschen, verlassen
*) Die Originalwörterbücher geben dem häufigen klnetoz (Stellen
in der Sahn. - Ausgabe I, p. XVIII) die Bedeutung 'Rache wünschend'
und fassen daher tö/ien als Verlangen, wünschen*.
Arm. toiz könnte übrigens entlehnt sein, vergl. Bartholomae
Studien II, 34.
') Vielleicht zu emendiren in törak', Justins Polemik (Bund. s. v.)
gegen de Lagarde, Ges. Abh. 53 Note 3 ist hinfällig, wenn sie sich
nur auf die Autorität der Handschriften stützt. Im Pehlevl wird gerade
der grösste Unsinn auch mit der grössten Consequenz von den Schreibern
immer wiederholt.
V
'j Belegt in FR und FJ durch einen Vers Qaträn^s (Metr.
Hezej):
tenhä men ü yetc sehr-i pur ez -/esrnH tu hä men
sere ü yeke desf4 pur ez rohe ü töre.
```


## [2026-09-14T03:10:55.579Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"andöften\\|andöfte\\|endöften\\|andöz\\|endöz\\|andöḫ\" HRN.txt | head; echo \"---HUB---\"; grep -n \"andö\\|andū\\|handö\" HUB.txt | head -20; echo \"--- NYB toxtan ---\"; grep -n \"tōxtan\\|tóxtan\\|twhtn\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-14T03:10:55.662Z] TOOL RESULT

```
1452:122. endöyiteu 'sammeln, erwerben', Praes. endöz-em,
---HUB---
--- NYB toxtan ---
1860:ham-toZik [hmtweyk] having debts in common with another, jointly responsible for a debt (debts) 70°. — Paz. ham00ji; from tóxtan.
1895:handóxtan [hndwhtn'] to collect, to ac- quire, to gain 73°12, — MPrs pres. pass. 3d p. pl. ’ndweyhyynd (Sogd 165. 17); Paz. NP andodtan, NP also andozidan; < ham + tóxtan (g. v.). :
3793:tóxtan [twhtn'] čož- [twe-] to pay a debt, a fine; to give back, return anything (borrowed): ken tēžēt he will take his revenge 4522, — Cf (Paz.) men hom Ādīnē i xin-xaGh u xin-06é u xin i haft-anbadaa pa farzanda Gēžom (Adino for Adēnāi, xin for ken, anbädaa faulty reading for óbüda = öbätak v. I, XV n. 2) ‘I am Adönäi, desiring revenge and taking revenge, and I shall revenge myself upon the children during seven genera- tions’ SGV XIV, 5-7, reproducing Ex. 20: 5. — MPrth twj- ‘to pay, to atone for’, Ghilain 63; MPrs twzysn ‘penalty, ex- piation'; Paz. 0óxtan 002-; NP toxtan toz-, kin-toz ‘bellicose, one who foments dissension and lawsuits’. — V. also tēg.
```


## [2026-09-14T03:10:57.384Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '1445,1470p' HRN.txt"
}
```


### [2026-09-14T03:10:57.444Z] TOOL RESULT

```
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
```


## [2026-09-14T03:11:05.202Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== FFD ===\"; grep -n \"اندوخت\\|اندوز\" incoming/FFD/FFD_pages.txt | head -20"
}
```


### [2026-09-14T03:11:05.263Z] TOOL RESULT

```
=== FFD ===
888:اندوختن
890:اندوخت < فارسی میانه 1304071 < ایرانی باستان 827۳-120-1۵*. برای 18 >
894:اندوز <ج فارسی میانه 2 جح ایرانی باستان 2۵-4۵-8۵ *. برای ۵ > آرای.[
```


## [2026-09-14T03:11:06.403Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SNS tap/tabah ===\"; grep -n \"tabāh\\|tabah\\|tap-\\|tp'h\" SNS.txt SNS_pages.txt | head -20"
}
```


### [2026-09-14T03:11:06.463Z] TOOL RESULT

```
=== SNS tap/tabah ===
SNS.txt:9346:, ^ tapayeiti, /-tap-:*-,' 
SNS.txt:9409:. - l > .*.»..l*--tabah: -o'Ot' 
SNS.txt:31265:tabah 147/13 
SNS_pages.txt:6148:                                         /-tap-:*-,'
SNS_pages.txt:6238:                                                        - > .*.»..l*--tabah:
SNS_pages.txt:15807:sSdarvan 196/9        savSnd 203/20-272/3              s&zag 202/13           tabah 147/13
```


## [2026-09-14T03:11:10.416Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9330,9420p' SNS.txt"
}
```


### [2026-09-14T03:11:10.474Z] TOOL RESULT

```
T« 



U; ^__L o-L ^l, 



Iff 



\° 



, ^ tapayeiti, /-tap-:*-,' 

t 4 Pt i, Aap- *.— ; c p gnpe 83) ta£6an .. , 



\T/T^ 



( V V*«)*» 8 taXt! ^"" 



pelotan I ram §rbad: Y&b***J(F* twt^xjjw : •A.T,_,bS jJ 

•j5j« :pSrCz: C^Jf 
: jzk(AiWb. 862) aojah- :j' pairi. aojastara-:^- 
PYLwzy : j V^ tfj-ky (Mir. Man. II, 64) pyrwz 

■ Xo/tt^ f^tf^V'^) 'ifeiW :p§r6zgar: >J(2P-»«J 

■ T/TT^ lT-f/H^ >j?/j£jN :pSrOzgartar: Vjj^'O 

\^/U«^ -CMpAxW rperOzgartum: -6»)°^ 3 k j *-> 



M/\o<£ m /V ^ Wif/fc. 817)pa§man- : fc- 

.YA/i««^ -j^j^ : P Sm * 92»w: -*»w» « ^«J 

* 



,Liiii— ,U**b *sS 



\fY 



c— ^llj ^_^tl 4.1; 4j|^ 



Iff 



0*/rA^^»x.J.W« rf ^»tcu:hIg ray: J**,,,- 

b5v 1 mardOman skast. : *&* ^ 

^> . ^ : Skaned : TBLWN , yt,j> • ^ —» 
. w , ft ^ ^:ma 5 IkanSd: *»£«• -* ^ 

. o^i : skast : TBLWN , t : y : '""V 
. T/U J .c-l«uSi*»be skast: ru&i--» 
Wtti.nV^ .. K :kah: T BN':^:-i 

. - l > .*.»..l*--tabah: -o'Ot' 
„ T._T:tubh,tub,tuph,/tu P L/ta P :^ ^ 

, .f^^tawah : V CPM- ^^ 

* 



• JhJ-4 'o^jj '*■** -i>»*« :tastlg: JL>t**0-«>* 
SeiZey, B505. VII;: 1934, p. 280. :iSJ* 5 l JCw l tf l
```


## [2026-09-14T03:11:12.161Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=860 && NR<=900' incoming/FFD/FFD_pages.txt; echo \"=== find page tag ===\"; awk 'NR<=890 && /pdf page/{p=$0} END{}' incoming/FFD/FFD_pages.txt; grep -n \"pdf page\" incoming/FFD/FFD_pages.txt | awk -F: '$1<900' | tail -3"
}
```


### [2026-09-14T03:11:13.201Z] TOOL RESULT

```
«انجامید» مادةٌ ماضی جعلی است» از مادهٌ مضارع ساخته شده است. مادةٌ ماضی
«انجام» در فارسی میانه 1272[311 بوده است.

بازماندةٌ 31-12[-82۳* ایرانی باستان است. برای 1۵ -> آراست. 1470 پیشوند
فعلی است. 31[ به جای 370[ آمده است. در فارسی میانةٌ مانوی 18۳831۲ و 82۳2211
به‌جای 1۵0[311 آمده است.

انجام ج فارسی میانه 822[370 + ایرانی باستان 370-8[-822*. برای 2 -> آرای. 1
پیشوند فعلی است. 8/[370 صورت بالاندهٌ ریشهٌ 8/1270 به معنی «حرکت کردن» است.
صورت بالاندةُ ريشهٌ 8/[87 معنی واداری دارد و با پیشوند فعلی 1۵70 به معنی
«به‌هم آوردن») است. «آمدن» و «فرجامیدن) هم از 8/1370 آمده‌اند > «آمدن؛ و
«فرجامیدن».

انداختن
انداخت + فارسی میانه 8228371: طرح کردن» برنامه‌ریزی کردن. سعدی در بوستان
[pdf page 37]
انا ی فعلهای فارسی دری
می‌گوید:
نباید سخن گفت ناساخته نشاید بریدن نینداخته

< ایرانی باستان 12-13-1۵*. 1200 پیشوند فعلی است. برای 13 > اراست. 131
صورت اصلی 13 است» # پیش از 1 به #بدل شده است. 13 صورت بالاندة 12۴است»
به معنی «دویدن». از 12 در فارسی دری «گداختن» و «پرداختن» و «تاختن» هم آمده‌اند
ی گداختن و پرداختن و تاختن.

انداز ج فارسی میانه ۳23۵437 < ایرانی باستان 8۵۳-130-۸*. برای ۵ > آرای. 5
به‌جای ا آمده است.

اندوختن

اندوخت < فارسی میانه 1304071 < ایرانی باستان 827۳-120-1۵*. برای 18 >
آراست. 1200 پیشوند فعلی است. 408 صورت اصلی 127 استء 8 پیش از ۲ به * بدل
شده است. ريشةٌ 1208 به معتی «پرداختن» است.

اندوز <ج فارسی میانه 2 جح ایرانی باستان 2۵-4۵-8۵ *. برای ۵ > آرای.[
به‌جای 8 آمده است.

اندودن

اندود < فارسی میانه 132480 < ایرانی باستان ۴۳۵۳-4-16 برای 1۵ -> آراست.
0 پیشوند فعلی است. ربشهٌ 7 به معنی «پاک کردن» است. > زدودن.
=== find page tag ===
819:[pdf page 35]
841:[pdf page 36]
875:[pdf page 37]
```


## [2026-09-14T03:11:38.309Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== SNS pages ctx ===\"; sed -n '6225,6250p' SNS_pages.txt; echo \"=== page tags near ===\"; grep -n \"pdf page\" SNS_pages.txt | awk -F: '$1<6250' | tail -3"
}
```


### [2026-09-14T03:11:39.329Z] TOOL RESULT

```
=== SNS pages ctx ===
                                                                                                              (*j±*fj t5rlk
                                                                                                                                 .,b          tamisra-:             ^   JAie         ta$ra-: ;l       4u
                   .

                                                                                                                                      :
                                                                                                                                                   L     Wir. Van. II, 68}It'ryg: >:^

                                                               K :kah: T      BN':^:-i
                       Wtti.nV^                           ..



                                                                                             -o'Ot'
                                                        - > .*.»..l*--tabah:
          „   T._T:tubh,tub,tuph,/tuP
                                                    .
                                                         l


                                                                         L/taP           :^           ^


                                                                                                          ta.wy.urvata          .^t-^l^.^^^^u^tavart: *W                                                          16
,
          .f^^tawah                 :   V       CPM-
                                                                                         ^^                          .f/1T* •*^*^b^b-U2U^I J CM.I^TTtfl,b,t=-l
=== page tags near ===
```


## [2026-09-14T03:11:39.467Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC leaf ~697 Tabh ===\"; grep -n \"Tabh\\|tābh\\|tabh-\\|to rot\" IEC.txt | head -20"
}
```


### [2026-09-14T03:11:39.527Z] TOOL RESULT

```
=== IEC leaf ~697 Tabh ===
11323:mug- (1) ‘rot, mildew; filth’ Alb. mug, v. “allow to rot; EMDu. mok, f. 'slut'; G Much, m. ‘mildew, fungus’; cf. mucheln, v. ‘grow mouldy’; OE (alleged) moc ‘filth’, in hlose-moc ‘filth of pigsty’; EME muck, adj. ‘moist’; s. as Eng.; ON myki, f., mod. mykja, f. ‘dung’; Norw. mökk ‘muck’; Sw. cf. mocka, v. ‘defaecate’; Br. cf. mon, m. (human dung, ambig. perh. fr. *mugno-). . (For OCS müzdivü ‘rotting’, see mud-)
13824:Arm. cf. (variant w. *ph-) but, gs: pto, adj. ‘Totten’; OLat. putis, adj. id. beside Lat. pu- tris, adj. ‘rotten; nasty’; Gk. cf. pütho, v. frot, if metath. for *phuto); W (variant w. *ph-) pwd, m. “rot; footrot; radical in Li. püti, v. ‘to rot"; Latv. pūt, id. Cf. putros (2). (A form with assimilated vowels occurs in Arm. hot, o-st. ‘stink’. With short vowel here probably Lat. puteus, m. “well, pit', but a LW fr. Gk. bussós, via Etruscan is possible, for the cons. cf. kalübion » clypeus, clypeum)
14817:rüd- ‘rot, rubbish? Lat. rüdus, adj. Con the turn, souring'. For rudis, & rüdus ‘rubble’ see ghreud-, ghroud-, ghrud-); OHG rozzen, OFris. rotia, LG & Du. rotten, OE rotian, Sw. rutta, ON rotna, v. ‘sto rot' beside Du. roten ‘ret — flax’; Icel. rota, v. id.; cf. also OE ryt ‘rubbish, under- growth'; ON rytja, f. “trash”
17473:sthabh- (stabh-) (1) ‘fix, stop, hold, estab- lish’. (Most forms are indistinguishable from those represented under sthab-, q. v.). Cf. WP IL, 624. Verbal forms: Skt. stabhnámi, stabhnómi, pp: stabhitáh, stabdhah, v. “stop, fix, prop’; Oss. cf. stavd, adj. (fat, thick’, fr. *sthabht-); Hitt. staphi, tr. ‘shut’; mp. ‘stop, come to rest’; Ir. cf. sta- bhuighim, v. ‘straddle’; W safaf, 3sg: saif, v. ‘will stand; MHG staben, intr. ‘stiffen’; Du. staven, v. (1) ‘prop’; E to stave off ‘avert’; to stave in, p.t. stove in ‘dent’; ON stafa, v. ‘assign’; stefja, v. ‘prevent’. Nominal types sthabhos, is, å (1) in Tokh. A stop, stow, s. ‘stick’; Gk. staphís, f. (2) ‘delphinium’; Ir. stabh, m. “log; stalwart’; sabh, f. (2) ‘stump, Stick, bolt; W saf, pl. -ion, f. ‘stand, fixity:'; Go. stafs, m. ‘letter; MHG stap, gs: stabes, sm. “post, stick’; LG staff, pl. stäw, m. “staff”; OE staf, pl. stafas, m. id. & "letter; Du. staf, m., staaf, f. “staff, stave’; Sw. cf. stáver, mpl. ‘staves of a barrel; Li. stabas, m. ‘idol’; Latv. stabs, m. 'post, pillar. Ambig. *-b- or *-bh-: OPr. stabis, s. ‘stone’. See next
17474:sthabh- (stabh-) (2) “hard, dry, stiff, with- ered’. Cf. sthabh- above. WP II, 625. See next Gk. staphís, f. ‘dried grape’; Ir. sabh, adj. ‘strong, able’; Fris. staf, adj. ‘sterile; dullwit- teď’; Li. cf. stabas, m. (2) ‘paralysis’
18183:tabh- (?) *rot, corruption, stench'
18222:tām- (2) ‘swell, distend' Lat. tama, f. ‘swelling of feet; W tofi, inf., tawf, 3sg. 'distend'. (Hybridism may be pre- sent in Lat. con-tàminàre ‘contaminate’, cf. tabh-?). (Isophone in Latv. tameju, v. “intend: tame, f. “plan, proposal)
```


## [2026-09-14T03:11:49.907Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('SNS_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\ntarget=6238\nn=sum(1 for l in lines[:target] if '\\f' in l)\nprint('form feeds before line',target,'=',n)\nEOF\npython3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['SNS'].get('page_offset')); print(d['SNS'].get('notes'))\""
}
```


## [2026-09-14T03:11:50.502Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '18180,18190p' IEC.txt"
}
```


### [2026-09-14T03:11:51.191Z] TOOL RESULT

```
form feeds before line 6238 = 89
242 leaves; page offset not determined (OCR too poor to read printed numbers) — locate by transliteration then read the page image
OCR quality is POOR: Persian text mostly garbage, Latin transliterations partially readable. Verification will usually need the page image.
```


### [2026-09-14T03:11:51.237Z] TOOL RESULT

```
surio ‘dangle, swing, sway”. Cf. suer-, suor- and suir-. (Gk. ambig.) Gk. aíro, v. (‘raise’. Associated with a-eíro, id. See suer-); Li. svyriu, Eti, v. intr. ‘dangle, hang’. Cf. also Gk. artáo, v. ‘hang’; Li. svirtis, f. 'swing-beam, bar, windlass’; araiós (2) ‘flimsy, weak’; Li. svirüs, adj. ‘flimsy, tottery'. (For Gk. araiós (1) “thin”, see ursios)
1365
-t (-ti), ablative inflexion and adverbial suf- fix. Cf. -öt Vedic cf. sanát “from early times’; Skt. Gr “from that’; Hitt. cf. arunac ‘from the sea"; ne- pisac *nebisac' ‘from heaven”; (but -t is an in- strumental sign in Hitt, cf. wetenit 'by water); Alb. cf. véndit (from the place'. Cf. uesntis); dóret (“by hand’. Cf. ghér-); OLat. donod: Skt. danat “from a gift; Osc. amvíanud ‘from a street corner’; Lat. cf. sed (but, lit. ‘by itself”, as G allein "but: OCS cf. strümotí (utterly', as Alb. shqimi-t, id.); Li. cf. anot (“according to”. Cf. *onos, à or *anos, à); also Li. vienas vienat “one only”. (A similar suffix, of type *-to, arises in Go. dala-pa ‘below’; cf. Hitt. wedanda “by water; Osc. pureto “from fire") tà “thus, thereby, therein, therefore, thus. Cf. tō Oss. (*tā or *to) tà, conj. “but, yet; Hitt. ta “here, there’; Gk. té, adv. id. EMAIb. tue (particle of continuity, as in tue klaté ^weep- ing’, see klauió); OHG (*tà or *tō) duo, cj. ‘then’; Srb. ta, cj. ‘so’; Latv. tà, id., cf. ta kā, cj. (so that', fr. *tà qua)
tabh- (?) *rot, corruption, stench'
Per. tabah, s. ‘corruption’; tabah, adj. ‘cor- rupt’; Lat. tàbes, gs: -is, f. and tabum, n. 'de- cay, corruption, gore, filth’; cf. tàbeo, ere, v. ‘toť; ON beta, tr, pefja, intr. ‘smel’. (WP untenable). (Cf. WP I, 701)
Gen, eio, ið "touch; caress’. WP I, 703 Hom. Gk. cf. tetagón, gs: -óntos, adj. *grasp- ing’; OLat. Geo ére, v. (touch? Fest); cf. tagax, adj. lightfingered', beside tango, Ere (as OLat. w. infix); OE (w. expressive dou- bling) paccian, v. ‘stroke, touch’; Srb. and Slovene tãžiti, inf. ‘soothe’; Li. cf. pa-togüs, adj. “comfortable, convenient; su-togti, inf. ‘agree’; Latv. pa-tags, adj. (convenient
-t (-ti) — taios, us
I
20
25
30
```


## [2026-09-14T03:12:02.031Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== PHD tabah ===\"; grep -no \"tabāh[^ ]*[^|]\\{0,120\\}\" PHD.txt | head -5; grep -n \"tabah\\|tab.h\" PHD_mackenzie.txt | head -10; echo \"=== NYB tabah ===\"; grep -n \"tabāh\\|tabah\\|tp'h\" NYB_vol2_glossary.txt | head -5"
}
```


## [2026-09-14T03:12:04.020Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BRT tap/tafnu ===\"; grep -n \"tafnah\\|tafnu\\|tāpayeiti\\|tapayeiti\" BRT.txt | head -10; echo \"=== BRT 'tap' headword ===\"; grep -n \"^tap\\|[^a-z]tap-[^a-z]\" BRT.txt | head -20"
}
```


### [2026-09-14T03:12:04.965Z] TOOL RESULT

```
=== PHD tabah ===
ugrep: error: error at position 617
0-\x8f][\x80-\xbf][\x80-\xbf]){0,120}
        exceeds complexity limits___/


4868:tabAh [tp)h I N -] ruined, spoilt, destroyed•
4870:tabAhihistan, tabahih- [tp)hyh-stn l I J tb)hh-] be ruined.
6368:defiled iiliidag.                              iiniistih, kastiirih, tabahih, wanisn,
7499:ruin(ation) abesihisn(ih), tabahih,        school     dibirestiin,    frahangestiin,
7502:    tabahihistan.                          scorn afsos, riyahrih.
7634:     temar, zarig.                      spoilt anast(ag), mudag, tabah,
8178:tabah                      ~v'"         dol                        \~,o
8179:tabahih                ~QJ'"            targuman                 \~~
8181:tabahihistan   \\~Q.)ll»                tarwcnidan              \\~~) 1"
=== NYB tabah ===
3728:to be spoiled 81**. — Paz. tawāh; NP tabāh.
```


### [2026-09-14T03:12:05.032Z] TOOL RESULT

```
=== BRT tap/tafnu ===
7136:[  da^at  . .  '"krasca  . .  paitHarat  N.  ■j4;  — j  iävanänS  (sd.)  dilityS  gätus  fralarqn  barts- ,  mqn  aparqm  ''i<ri)  N.79;  79 ; — '"ai^a  yff  dim *frähincin  (sd.)  *antarp  'tartmca  barsmaca \  ". .  zwischen  dem  Feuer  und  dem  B.  (an ■  der  Opferstätte)"  N.  08''\  c)  GS.  mit I  ta/nav-  m.  Flur.  'Feuergluten'  sva.  'Fieber- lanfälle':  kö pagiryS..'%rS  tafnus  därayat tanaot  haca    masyehe  V.  20.  i.  d)    Es
11926:•  j.  tafnah-  n.  i)  'Hitze,  Glut'  (nur  Ab- leit.).  2)  'Fieberhitze,  -glut':  yaiÖa  hi hqm  °nS  jasat  (Sp,  501  u.)  avi  tanuye  zsis- nuye  V.  7. 70.
11931:•  j.  tafnah'vant-  Adj.  'Gluthitze  enthal- tend':  mäaA^m  ..  *'natfhuntfm'1  Ytj.S-
18506:•  j.  'naeza-  m.  Name  einer  Krankheit: aüalfva  daxmalha  kamiavamU  axtiica gannusla  tafnusca  'zasca  sSrastisYaV.j.SJ ; —  paiHstätSe  gamiSusca  tafttaolca  'sahe^a sarastSisca  Yt/J.  131.
30660:I  aniars  mar?h>m^a  hvanca  Yt  6.  5;  — \yakra  aval  hvar»  uxaiti  F.^bj  — ya^ ^  hvar?  utuxsyeiti '^t.  6.  2;  3; — yat  hvar? '  raoxsne  tapayeiti  Yt6.i;  —  hau  Aa (GS.)  vaxiat  a  ha  fraimS-datSit  "von Sonnenaufgang  bis  Sonnenuntergang"  Yt 5.  91  usw.'';  ~ pasca  hü  fraitRSJaiilm  . . pasca  "hvs''  nStt  ueux^atnnS  (sd.)  Yt. 4-8;  —  para  avalAhe  hü  ^war/tS  (sd-) Y.ig.&;  —  raocä  (sd.)  a  . .  hü  paiti alwamm  V.  2.  10;  Yt /2.  3;  —  hvar» raocS  Vr,  ig.  2,  Yt  6.\\  —  ima  raocä bamiitjm  bar»simanqm  avat  (sd.)  yat hvar!  avaci  Y.j6.6;  Yi.ig.a;  —  raaci x'Jng  (GS.)  asnqm  uxsä  (sd.)  aiiirus  Y. 50.10; —  »r^jli..pourusa  hvarS pifyasü (sd.)  Y.  50.  a;  —  yS  acist»m  *vaenaAh! (sA.)  aog>da  gqm  astbya  kvancä  Y._j2. 10;
=== BRT 'tap' headword ===
11912:•  j.  tap- V. 'heiss  sein',  Praes.  4b(Kaus.) tapa-''^,  14  (Inkoh.)  la/sa-,  30  (Kaus.) tapaya:  ~  PPfP.  'iap/a-.  [S.  noch taßa..]
```


## [2026-09-14T03:12:13.733Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"^\\*tap\\|\\*tap[0-9]\\? ‘\\|\\*tafs\\|\\*tabH\" CHEUNG.txt | head -20"
}
```


### [2026-09-14T03:12:13.788Z] TOOL RESULT

```
3298:*tap ‘to seize, attach, stick, strike’ 
24669:*tap ‘to warm up, heat’ 
24686:*tap 379 
25332:*tap ‘to twist, wind’ 
55127:*tap (s.v.), *zarH' (s.v.)
```


## [2026-09-14T03:12:14.907Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== MON tabah ===\"; grep -n \"تباه\" MON_part1.txt MON_part2.txt | head -8; echo \"=== MON top ===\"; grep -n \"توپ\" MON_part1.txt MON_part2.txt | head -8"
}
```


### [2026-09-14T03:12:14.993Z] TOOL RESULT

```
=== MON tabah ===
MON_part2.txt:835:کرده و به اشتباه کپسول فوق کلیوی نام 
MON_part2.txt:2380:غلط : ۸۱۱ [ع.] (مص‌ل.) اشتباه کر دن» خطا 
MON_part2.txt:2382:اغلاط. در اشتباه. چه غلط‌ها: (عم.) چه 
MON_part2.txt:2404:خطاء از روی اشتباه» اشتباها. به غلط (بر) 
MON_part2.txt:2421:۳900 خواندن با نوشتن اشتباه داشتن. 
MON_part2.txt:2429:خطا کردن, به خطا رفتن» اشتباه کردن. در 
MON_part2.txt:6367:هر شخص ستمکار و تباهکار. 
MON_part2.txt:7286:فساد؛ ٩2د)‏ ۳2 (مصل.) تباه شدن. نابود 
=== MON top ===
MON_part2.txt:1857:درونی و قسمت سطحی سیتوپلاسم 
MON_part2.txt:9033:داشته‌اند. توپ این بازی باید ّ چرم ساخته 
MON_part2.txt:9037:تقسیم می‌شود. هر دسته سعی می‌کند توپ 
MON_part2.txt:9039:بازیکنان باید توپ را با پا بزنند و اگر به 
MON_part2.txt:9043:دروازه توپ را با دست هم بگیرد. 
MON_part2.txt:19351:(تبانجه» تفنگک» توپ). 
MON_part2.txt:31255:گردون. ارابه‌ای که توپ را حمل کند. 
MON_part2.txt:31268:سیتوپلاسم آنها دو هسته دیده و و نکن
```


## [2026-09-14T03:12:19.082Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== CHEUNG 3298 ===\"; sed -n '3290,3320p' CHEUNG.txt; echo; echo \"=== CHEUNG 24669 ===\"; sed -n '24669,24700p' CHEUNG.txt"
}
```


### [2026-09-14T03:12:19.208Z] TOOL RESULT

```
=== CHEUNG 3298 ===
phonologically conforms to the category of forms with long middle vowel, e.g. 
mayüra- ‘peacock’, on which see Lubotsky, Early Contacts:305 ff. 


*PIE— > LIV: – | Pok.: 
*REFERENCES: IIFL I: 246a; DKS: 139a; Shahbakhsh: s.v. ¿am- 


*tap ‘to seize, attach, stick, strike’ 

*KHOTANESE: ? Khot. cev- ‘to get? — SGS: 34 

*SOGDIAN: (+ *fra-) MSogd. Br’cp- ‘to press’ (cf. Sims-Williams, apud Sundermann 
1981: 181b) 

Impf.: IND. 3pl. MSogd. Br'cp nt (MKG: 593) 

*CHORESMIAN: čp- ‘to attach to, contrive (a lie) against (someone)’ = Samadi: 58 f. 


*éarH 33 


*NWIR: NP capidan/cap-, Gur. (Kand.) ёараи$ап kär-, Khuns. Cap-/Cäpä ‘to plunder, 
rob’ (LW), Bal. campit/Camp-, canpit/Canp- ‘to snatch’, NP cafsidan, Abz. 
cawsowa/caws-, Nn. Cäsb-, Qohr. Caspada/éasp-, Tr. Cawsa(ya)/Caws- (inch.) ‘to 
stick, adhere’, ? Anar. Capowger ‘robber, thief? 

*NEIR: Oss. cevyn/cavd, D. cævun/cavd ‘to hit, strike’, Yghn. Cümf-/£ümfta ‘to push 
(to)’, Sh. cäp-/cäpt ‘to feel, touch’, Oss. І. cefsyn/cefst, D. caefsun/caefst (inch.) ‘to 
stick, glue’, M. cab-/cavd ‘to pluck’ || (+ *us-) Oss. I. sk’afyn/sk’eft, D. (z)sk’zfun 

=== CHEUNG 24669 ===
*tap ‘to warm up, heat’ 

*AVESTAN: YAv. tap- “о be(come) hot’ || (+ *4-) ‘to warm’ || (+ *ham-) ‘to 
be(come) hot’ — Liste: 24 

Pres. inch.: INJ. 3sg. YAv. tafsat- (Y 9.11, rep.), SUBJ. 3pl. YAv. tafsan (V 3.32); Caus.: pres. IND. 3sg. 
YAv. täpaiieiti (Yt 6.1, Yt 7.4, Yt 17.20, etc.), ? YAv. "a.tapaiieiti (V 9.41); Partic.: perf. pass. YAv. 
ham.tapta- (V 4.46) 

*MIDDLE PERSIAN: MMP t’b- ‘to shine’ ?, BMP t’p- /tab-/ ‘to heat, burn (up); shine’. 
© No certain attestations in MMP, DMMPP: ibid. > DMMPP: 321a 

Pres.: IND. 3sg. BMP t’pyt /tabéd /, SUBJ. 35р. ? MMP t’b’d {rather Pth. 7}, OPT. 3sg. ? MMP ®t’byy, 
ІМРУ. 2sg. BMP t^p /tab/; Inf.: BMP t’ptn /taftan/; Partic.: perf. pass. BMP грі /tafi/; Pass.: pres. IND. 
35р. BMP t’pyhyt /tabihed/ 


*tap 379 


*PARTHIAN: t’b- ‘to shine, burn’ || (+ *abi-) *bd’b ‘sunshine’ || (+ *pati-) pt’b- ‘to 
burn into’ || (+ *ui-) wyt’b- ‘to shine’ (young formation) = Ghilain: 72 | DMMPP: 
321a f., 9, 360a 

Pres.: IND. 259. t’byh, 35р. t’byd, t'byd, 3р1. t'bynd, SUBJ. 3sg. t’b’h; Partic: perf. pass. П t^b'd, t’b’d || 
(+ *pati-) Pres.: IND. 3sg. pt'byd, IMPV. 2pl. pt’byd || (+ *ui-) Pres.: IND. 3sg. wyt'byd, SUBJ. 2sg. 
wyt’b’h; Partic.: perf. pass. II wyt’b’d 

*KHOTANESE: ttav- (ttau(s)-) ‘to be(come) hot’ || (+ *a) LKh. ауу- ‘to heat’ || (+ 
*nis-) nastau-/nistau-, (inch.) OKh. nastos- ‘to be consumed’ || (+ *pati-) 
pattav-/pattau- ‘to burn up; illuminate’ || (+ *ui-) LKh. byav- ‘to be hot’ || (+ *ham-) 
OKh. handau- ‘to become hot’, LKh. hamdev- (caus.) ‘to ripen’ = SGS: 38, 9, 67,
```


## [2026-09-14T03:12:29.156Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 3
}
```


### [2026-09-14T03:12:29.163Z] TOOL RESULT

```


```


## [2026-09-14T03:12:32.496Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D8%A8%D8%A7%D9%87",
 "prompt": "Give the full Persian etymology section for تباه (tabâh): Middle Persian form, Old/Proto-Iranian reconstruction, any cited sources (Hasandust, MacKenzie), and the meaning."
}
```


## [2026-09-14T03:12:34.910Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AE%D8%AA%D9%86",
 "prompt": "Give the full Persian etymology for اندوختن (andūxtan): Middle Persian form, Proto-Iranian root, cited sources, related words (توختن tōxtan, اندوز andōz)."
}
```


### [2026-09-14T03:12:37.998Z] TOOL RESULT

```
# Persian Etymology for تباه (tabâh)

**Middle Persian Form:**
The word derives from Middle Persian [script needed] (tpʾh /⁠tabāh⁠/), meaning "injury."

**Proto-Iranian Reconstruction:**
From Proto-Iranian *tap-, potentially tracing back to Proto-Indo-European *tep- ("to be warm, to be hot").

**Comparative Evidence:**
Sanskrit ताप (tāpa, "heat; torment") provides comparative support for this etymological pathway.

**Cited Source:**
The page includes a classical Persian text citation from c. 1250 by Zartusht Bahrām-i Pazhdaw's Zarātusht Nāma, demonstrating historical usage of the adjective meaning "lost" or "ruined."

**Note:**
The entry indicates that the Middle Persian script form requires specification, and no modern scholarly sources (such as Hasandust or MacKenzie) are explicitly cited in this Wiktionary entry.
```


### [2026-09-14T03:12:41.387Z] TOOL RESULT

```
# Persian Etymology of اندوختن (andūxtan)

**Middle Persian Origin:**
The word is "Inherited from Middle Persian [Book Pahlavi needed] (hndwhtn' /⁠handōxtan⁠/, 'to gain, acquire, amass')."

**Etymology Chain:**
The Wiktionary entry traces the term back to Middle Persian *handōxtan*, which carried the semantic sense of acquisition and accumulation. The source document does not provide explicit Proto-Iranian roots or intermediate etymological stages beyond the Middle Persian form.

**Related Terms:**
- Present stem: اندوز (anduz)
- Past stem: اندوخت (anduxt)
- Synonym: جمع کردن (jam' kardan)
- Archaic synonym: الفختن (alfaxtan)

**Documented Source:**
MacKenzie's *A Concise Pahlavi Dictionary* (1971) provides lexicographic support for the Middle Persian form, though the webpage does not elaborate on broader Indo-European connections or Proto-Iranian reconstructions.

The entry emphasizes the transitive verb meaning "to collect, amass, gather" without detailing the prehistoric linguistic ancestry beyond Middle Persian.
```


## [2026-09-14T03:13:03.776Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-14T03:13:03.823Z] TOOL RESULT

```
#!/usr/bin/env python3
"""Fetch ONE cited page of a scanned reference, on demand.

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
"""
import sys, os, json, subprocess, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "verification", "sources")
TABLE = os.path.join(SRC, "refs_online.json")
REFS = os.path.join(SRC, "refs")
OCR = os.path.join(REFS, "ocr")
TESSDATA = os.path.join(REFS, "tessdata")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__); return 2
    m = re.match(r"^([A-Z]+)(\d*):(\d+)$", args[0])
    if not m:
        print("expected ABBR:page (e.g. BQT:918 or MON5:528)"); return 2
    abbr, vol, page = m.group(1), m.group(2), int(m.group(3))
    table = json.load(open(TABLE, encoding="utf-8"))
    ref = table.get(abbr, {})
    scans = ref.get("scans") or []
    if vol:
        scans = [s for s in scans if str(s.get("volume", "")) == vol] or scans
    scan = None
    for s in scans:
        if s.get("requires_volume") and not vol:
            continue
        if s.get("first_printed", 0) <= page <= s.get("last_printed", 10**9):
            scan = s; break
    if "--pdf-page" in argv:
        pdf_page = int(argv[argv.index("--pdf-page") + 1])
        scan = scan or (scans[0] if scans else None)
    elif scan:
        pdf_page = None
        pm = scan.get("page_map")
        if pm and os.path.exists(pm):
            pdf_page = json.load(open(pm)).get("map", {}).get(str(page))
        if pdf_page is None:
            pdf_page = page + int(scan.get("pdf_offset", 0))
            print(f"(no exact page map; using offset {scan.get('pdf_offset', 0)} -> pdf page {pdf_page}; check the printed number and re-run with --pdf-page if off)")
```


## [2026-09-14T03:13:04.380Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HJB 933 top ===\"; grep -n \"TOPE\\|tope\\b\" HJB.txt | head -20"
}
```


### [2026-09-14T03:13:04.435Z] TOOL RESULT

```
=== HJB 933 top ===
164:Southern  India  has  contributed  to  the  Anglo-Indian  stock  words  that  are in  hourly  use  also  from  Calcutta  to  Peshawur  (some  of  them  already  noted under  another  cleavage),  e.g,  betel,  mango,  jack,  cheroot,  murigoose,  pariah, bandicoot,  teak, patcharee,  chatty,  catechu,  tope  (*a  grove'),  curry,  mulligatawny, congee.    Mamooty  (a  digging  tool)  is  familiar  in  certain  branches  of  the
7413:1883. — "For  the  same  reason  mymxa  seek the  tope,  and  the  'blue  jay,'  so-called,  and the  little  green  ooppersmitii  hooting  ventri- loquistically." — Trwes  on  my  Frontier^  154.
8258:DAGK)BA,  s.  Singhalese  ddgaba^ from  Pali  dkdtuffahbhoj  and  Sansk. dhatu-^arhhoj  *  Relic  -  receptacle  * :  ap- plied to  any  dome -like  Buddhist «hrine  (see  TOPE,  PAGODA).  Gen. Cunningham  alleges  that  the  Chaitya was  usually  an  empty  tope  dedicated to  the  Adi-Buddha  (or  Supreme,  of the  quasi-Theistic  Buddhists^  whilst the  term  Dhdttt-aarbha,  or  Dhagoha,  was properly  applied  only  to  a  tope  which was  an  actual  relic-shrine,  or  repository of  ashes  of  the  dead  (Bhilsa  Topes^  9). ["The  Shan  word  * JSTto*,'  or  * Taty'  and the  Siamese  ^Sat-oop,'  for  a  pagoda placed  over  portions  of  Qaudflma's uody,  such  as  his  flesh,  teeth,  and hair,  is  derived  from  the  Sanskrit '  Dhdtu-garba,'  a  relic  shrine "  (ITaZfc^^, A  Thownnd  Miles,  308).]
8828:other  metalfi,  as  the  denarius  aeruy  and the  denarius  attn,  or  aureus"  (James Prinsep,  in  Essays,  &c.,  ed.  by  Thomas, i.  19).  But  it  was  long  before  the  rise of  Islam  that  the  knowledge  and  name of  the  denarius  as  applied  to  a  gold coin  had  reached  India.  The  inscrip- tion on  the  east  gate  of  the  great  tope at  Sanchi  is  probably  the  oldest  in- stance preserved,  though  the  date  of that  is  a  matter  greatly  disputed.  But in  the  AmarakMia  (c.  a.d.  600)  we liave  *dln&re  'vi  cha  nislikah,*  i.e,  'a nuMcah  (or  gola  coin)  is  the  same  as dinAxa.'  And  in  the  Kalpas&tra  of fihadrabahu  (of  about  the  same  age) %  36,  we  have  'dinara  mdlaya,'  'a  neck- lace of  dinars,'  mentioned  (see  Max MuUer  below).  The  dindr  in  modem Persia  is  a  very  small  imaginary  coin, of  which  10,000  make  a  tomanii  (q.v.^. In  the  Middle  Aces  we  find  Arabic writers  applying  tne  term  dindr  both to  the  staple  gold  coin  (corresponding to  the  gold  mohr  of  more  modem times)  and  to  the  staple  silver  coin (corresponding  to  what  has  been  called since  the  16th  century  the  rupee). [Also  see  YuU,  Cathay,  ii.  439  seqq.  See BEANEB.]
20740:STUPA.    See  TOPE.
22374:TOPE,  s.  Tbis  word  is  used  in three  quite  distinct  senses,  from  dis- tinct origins.
22378:TOPE-KHANA.
22380:TOPEEIVALA.
22382:"Tope."      See    under    TOPE-
22391:1814.— "It  is  a  general  practice  when  a plantation  of  mango  trees  is  made,  to  dig a  well  on  one  side  of  it.  The  well  and  the tope  are  married,  a  ceremony  at  which  all the  village  attends,  and  large  siuns  are often  expended."— Forbejf,  Or,  Mem.  iii.  56.
22393:TOPE-KHANA,  s.  The  Artillery, Artillery  Park,  or  Ordnance  Depart- ment, Turco-Pers.  Wv-kfuxmy  *  cannon- house*  or  *  cannon-aepartment.'  The word  is  the  same  that  appears  so  often in  reports  from  Constantinople  as  the Tophaneh.  Unless  the  traditions  of Donna  Tofana  are  historical,  we  are strongly  disposed  to  suspect  that  Aqua Tofana  may  have  had  its  name  from this  word.
22397:TOPEE,  s.  A  hat,  Hind.  (opt.  This is  sometimes  referred  to  Port,  topoy  *  the top '(also  Uype^  *a  top-knot,'  and  topete, a  *  toupee'),  which  is  probably  identical with  English  and  Dutch  top,  L. German  ioppy  Fr.  topety  &c.  But  there is  also  a  simpler  Hind,  word  top,  for a  helmet  or  hat,  and  the  quotation from  the  Roteiro  Vocabulary  seems  to show  that  the  word  existed  in  India when  the  Portuguese  first  arrived. With  the  usual  tendency  to  specialize foreign  words,  we  find  this  word becomes  specialized  in  application  to the  sola  hat.
22401:TOPEEWALA,  s.  Hind,  topiwaldy *one  who  wears  a  hat,'  generally  a European,  or  one  claiming  to  be  so. Formerly  by  Englishmen  it  was  habi- tually applied  to  the  dark  descendants of  the  Portuguese.  R.  Drummond says  that  in  nis  time  (before  1808^ I  Topeewala  and  PnggryuYi/a  were  used in  Guzerat  and  the  Mahratta  country for  *  Europeans'  and  *  natives.'  [The S.  Indian  form  is  Toppikdr,]  The author  of  the  Persian  Life  of  Hydur Naik  (Or.  Tr.  Fund,  by  Miles)  calla
22663:Little  importance  is  to  be  attached to  Pinto's  linguistic  remarks  such  as that  quoted,  or  even  to  the  like  dropt by  Couto.  We  apprehend  that  Pinto made  exactly  the  same  mistake  that Sir  John  Barrow  did  ;  and  we  need not  wonder  at  it,  when  so  many  of  our countrymen  in  India  have  supposed hackery  to  be  a  Hindustani  word,  and when  we  find  even  the  learned  H.  H. Wilson  assuming  tope  (in  the  sense  of
```


## [2026-09-14T03:13:10.141Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '22374,22396p' HJB.txt"
}
```


### [2026-09-14T03:13:10.195Z] TOOL RESULT

```
TOPE,  s.  Tbis  word  is  used  in three  quite  distinct  senses,  from  dis- tinct origins.
a.  Hind,  fop,  'a  cannon.'  This  is Turkish  tcf,  adopted  into  Persian and  Hindustani.  We  cannot  trace  it further.  [Mr.  Platts  regards  T.  to6, top,  as  meaning  originally  *a  ronnd mass,'  from  Skt  ^Spo,  for  which  see below.]
b.  A  ffrove  or  orchard,  and  in Upper  India  especially  a  mango- orchard.  The  word  is  in  aniversal use  by  the  English,  bat  is  quite  un- known to  the  natives  of  Upper  India. It  is  in  fact  Tarn,  tdppu,  TeL  iopv, [which  the  Madras  GUi$.  derives  from Tarn,  toguy '  to  collect,']  and  must  hAve been  carried  to  Ben^l  by  foreigners at  an  early  period  of  JEiiropean  traffic. But  Wilson  is  curiously  mistaken  in supposing  it  to  he  in  common  use  in Hindustan  by  natives.  The  word  used by  them  is  bdgh,
c.  An  ancient  Buddhist  monument in  the  form  of  a  solid  dome.  The word  tdp  is  in  local  use  in  the  X.W, Punjab,  where  ancient  monuments  i4 this  kind  occur,  and  appears  to  come from  Skt.  stupa  through  the  P^i  or
TOPE-KHANA.
935
TOPEEIVALA.
Prakrit  thu'po.  According  to  Sir  H. Elliot  (i.  605),  Siujpa  m  Icelandic signifies  *a  Tower.'  We  cannot  find  it in  Cleasby.  The  word  was  first  intro- duced to  European  knowledge  by  Mr. Elphinstone  in  his  account  of  the Tope  of  Manikyala  in  the  Rawul Pindi  district.
"Tope."      See    under    TOPE-
[1884.— "The  big  gun  near  the  Central Museum  of  Labor  called  the  Zam-Zamah or  Bhanjianvati  top,  seems  to  have  held much  the  same  place  with  the  Sikhs  as the  Malik-i-Maid&n  held  in  Bijapur." — Bombay  Oazftteer^  xxiii.  642.]
b.-
1673._".  .  .  flourish  pleasant  Tops  of Plantains,  Cocoes,  Guiavas. "—/ryer,  40.
„  "The  Country  is  Sandy;  yet plentiful  in  Provisions ;  in  all  places,  Tops of  Trees."— /6irf.  41.
1747._"The  Topea  and  Walks  of  Trees in  and  about  the  Bounds  will  furnish  them with  firewood  to  bum,  and  Clay  for  Bricks is  almost  everywhere."— -Rr/KM-^  of  a  Council of  War  at  Ft.  St.  David,  in  Constu,  of  May 5,  MS.  in  India  Office.
1754.— "A  multitude  of  People  set  to  the work  finished  in  a  few  days  an  entrench- ment, with  a  stout  mud  wall,  at  a  place called  Faoquire's  Tope,  or  the  grove  of  the Facquire." — O-nw,  i.  273.
1799.__«Upon  looking  at  the  Tope  as  I came  in  just  now,  it  appeared  to  me,  that when  you  get  possession  of  the  bank  of  the Nnllahi  you  have  the  Tope  as  a  matter  of course."— UW/in^ton,  Besp,  i.  28.
1809.—"  .  .  .  behind  that  a  rich  country, covered  with  rice  fields  and  topes." — Ld. VaUntia,  i.  557.
1814.— "It  is  a  general  practice  when  a plantation  of  mango  trees  is  made,  to  dig a  well  on  one  side  of  it.  The  well  and  the tope  are  married,  a  ceremony  at  which  all the  village  attends,  and  large  siuns  are often  expended."— Forbejf,  Or,  Mem.  iii.  56.
[1839.— "Tope  is  an  expression  used  for  a mound  or  barrow  as  far  west  as  Peshawer. .  .    "—Elphimtone,  Caubiil,  2nd  ed.  i.  108.]
TOPE-KHANA,  s.  The  Artillery, Artillery  Park,  or  Ordnance  Depart- ment, Turco-Pers.  Wv-kfuxmy  *  cannon- house*  or  *  cannon-aepartment.'  The word  is  the  same  that  appears  so  often in  reports  from  Constantinople  as  the Tophaneh.  Unless  the  traditions  of Donna  Tofana  are  historical,  we  are strongly  disposed  to  suspect  that  Aqua Tofana  may  have  had  its  name  from this  word.
1687.—"  The  Toptchu  These  are  Gunners, called  so  from  tne  word  Tope,  which  in Turkish  signifies  a  Cannon,  and  are  in number  about  1200,  distributed  in  62  Cham- bers ;  their  Quarters  are  at  Tophaiia,  or the  place  of  Guns  in  the  Suburbs  of  Con- stantinople."—/JymM^'i  Present  State  of  the Ottoman  Empire,  p.  94.
1726.  —  "  Isfandar  Chan,  chief  of  the Artillery  (called  the  Daroger  (seeDABOGA) of  theTopscanna)."—  Valentijn,  iv.  {SuraUe), 276.
1765.— "He  and  his  troops  knew  that  by the  treacheiy  of  the  Tope  Ehoxmah  Droger (see  DABOGA),  the  cannon  were  loaded with  powder  ovAj^—HolvoeU,  Hid,  Events, &c.  i.  96.
```


## [2026-09-14T03:13:23.414Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'NR>=22340 && NR<=22375' HJB.txt | grep -n \"^[0-9]\\{3\\}$\\|93[0-9]\" | head; echo \"---\"; grep -n \"^93[0-9]$\" HJB.txt | tail -20"
}
```


### [2026-09-14T03:13:24.358Z] TOOL RESULT

```
---
22264:930
22285:931
22334:933
22379:935
```


## [2026-09-14T03:13:34.421Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== BQT v1 انداختن/اندوختن ===\"; grep -n \"اندوخت\\|اندوز\" BQT_v1_pages.txt | head -20; echo \"=== BQT v1 توپ ===\"; grep -n \"^.\\{0,40\\}توپ\" BQT_v1_pages.txt | head -20"
}
```


### [2026-09-14T03:13:35.537Z] TOOL RESULT

```
=== BQT v1 انداختن/اندوختن ===
4978:اندوز عربی که فصیح‌ترین لغات‌است_معجز آرا و کرامت‌پیرا نمود» جل
13038:افر و خشن؟ « بروزن اندوختن بسعنی
13625:است بعنی بهمرسانید و اندوخت و جمع کرد .
13627:بپمرسانیدن و جمم کردن و اندوختن باشد .
13631:بروژن و معنی الفختن است که اندوختن و جمم
13639:است که جم کر ردن واندوختن باشد ‏ و امر بدین
13644:واندوختن باشد.
13651:واندوختن باشد .
14349:۷ ره : اندوختن.
20677:بلخفتن ۱ ست که بمعنی جمم کردن و اندوختن
25644:باشد که اندوخته و ذخسره و یی انداز است
29848:واندوخته باشد , و بکسر اول بر دزن نکوهیده
31557:نمودن و اندوختن و حاصل کردن - و گزارین
31712:وبمعنی کشیدن - و اندوختن- ودوختن- وجستن
31713:عم هست۷ - و امر بکشبدن - و اندوختن -
31759:اندوختن و کشیدن وادا کردن باشد» یمنی کزارد
31760:وادا کرد - واندوخت وحاصل‌نمود و کشید .
31762:ناخت و تاراج کردن باشد ۷ - و بمعنی‌اندوختن
=== BQT v1 توپ ===
3292:تلمن » توپا ؛ تورا » توما تیبا * تین » تیناه جاتن » جانونتن» جاسونتن »
4165:انگشتانه» بادنجان باروت؛ بورانی؛تفنگ و توپ؛و قستی از لغات‌ارویایی راهم
23224:بمعنی جزئی باشد که دربرابر کنی استوپاز تاربان
31437:چرخ حمل‌شود- بك‌بته ازقماش‌وجز آن- توپ
31438:زدن » توپ الداختن- در اصطلاح فمار . بروی
31443:تو بال . و توپال۱ , لفت اول با بای
```


## [2026-09-14T03:13:42.593Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target in [13625,14349,31437]:\n    n=sum(1 for l in lines[:target] if '\\f' in l)\n    print('line',target,'-> leaf',n)\nEOF"
}
```


### [2026-09-14T03:13:43.688Z] TOOL RESULT

```
line 13625 -> leaf 371
line 14349 -> leaf 385
line 31437 -> leaf 744
```


## [2026-09-14T03:13:51.245Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"hand\\|handu\\|handoz\\|andux\\|anduz\" BQT_v1_pages.txt | head -20; echo \"=== leaf 385 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==386' BQT_v1_pages.txt | head -60"
}
```


### [2026-09-14T03:13:52.265Z] TOOL RESULT

```
=== leaf 385 ===
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
```


## [2026-09-14T03:14:01.801Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in range(384,398):\n    L=leaves[i]\n    if 'اندو' in L or 'اندا' in L:\n        print('=== leaf',i,'===')\n        for ln in L.split('\\n'):\n            if 'اندو' in ln or 'اندا' in ln: print('   ',ln.strip())\nEOF"
}
```


### [2026-09-14T03:14:02.855Z] TOOL RESULT

```
=== leaf 384 ===
    ری و اندام و غیره باشد .
    درهم کشیده شدن پوست روی و اندام باشد -
    انجخ ۱ سا که جچن و شکنج روی واندام عاشد .
=== leaf 385 ===
    روی و اندام باشد از عابت چیری دا سبسد: ۳
    برهم ش کشیدن بوست روی و اندام وا گومند .
    وهعنی انجوخ اس که چن و شکن روی واندام
    است که برهم کشیده شدن پوست روواندام‌باشد .
=== leaf 386 ===
    و اصل السوی بیخیدرخت‌انداست - و مخ نکفئن
    ۹ رك: انداژه ۰
=== leaf 387 ===
    است. واندازمومقیای‌ومقذار چیزی‌رانی زکویند ۱
    و بممنی مصدرهم افخة ابت که انداختن ,اشد.
    انداده ۷ » بروزن خمیازه ۰ یمانتهر
    چیز را گویند - و فیای کردن و اندازه گرفتن
    انداوه بفتح واو , مالهٌ استادان بثا
    آثای4 « بروزن هسابه , بمعنی‌انداوه
    انداختن .
=== leaf 389 ===
    افو ج -بروزن محلوج» بمعنی‌اندوب
    اندول بروزن ممقول ۰ کلیمی باشد
    | زد و۸ چم ثالث » مخفف اندوه است
=== leaf 390 ===
    ۱ -رك : اندوب واندوج .
    ۷ ره : اندوختن.
```


## [2026-09-14T03:14:08.959Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (389,390):\n    print('===== leaf',i,'=====')\n    print(leaves[i][:2600])\nEOF"
}
```


### [2026-09-14T03:14:10.034Z] TOOL RESULT

```
===== leaf 389 =====
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
===== leaf 390 =====
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


## [2026-09-14T03:14:26.667Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; timeout 300 python3 tools/ref_page.py BQT:171 --image 2>&1 | head -40"
}
```


### [2026-09-14T03:14:27.773Z] TOOL RESULT

```
no scan of BQT covers printed page 171 (see 'scans' in refs_online.json)
```


## [2026-09-14T03:14:42.044Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad 2>/dev/null || cd /tmp; for n in 389 390; do curl -sL -o bqt-482-$n.jpg \"https://archive.org/download/borhan-ghate-v1/page/n$n.jpg?fit=height\" --max-time 90; echo \"$n: $(file bqt-482-$n.jpg 2>/dev/null | cut -c1-80) $(stat -c%s bqt-482-$n.jpg 2>/dev/null)\"; done; pwd"
}
```


### [2026-09-14T03:14:45.669Z] TOOL RESULT

```
389: bqt-482-389.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, 520653
390: bqt-482-390.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, 527392
/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad
```


## [2026-09-14T03:14:49.267Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 -c \"\nfrom PIL import Image\nfor n in (389,390):\n    im=Image.open(f'bqt-482-{n}.jpg'); w,h=im.size; print(n,w,h)\n    im.crop((0,int(h*0.75),w,h)).resize((w*2,int(h*0.25*2))).save(f'bqt-482-{n}-foot.png')\n\" 2>&1 | tail -5"
}
```


### [2026-09-14T03:14:51.553Z] TOOL RESULT

```
389 2479 3508
390 2479 3508
```


## [2026-09-14T03:14:53.432Z] TOOL CALL #53: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt-482-389-foot.png"
}
```


### [2026-09-14T03:14:53.814Z] TOOL RESULT

```

```


## [2026-09-14T03:14:53.809Z] INPUT

[Image: original 4958x1754, displayed at 2000x708. Multiply coordinates by 2.48 to map to original image.]


## [2026-09-14T03:15:02.626Z] TOOL CALL #54: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt-482-390-foot.png"
}
```


### [2026-09-14T03:15:02.997Z] TOOL RESULT

```

```


## [2026-09-14T03:15:02.994Z] INPUT

[Image: original 4958x1754, displayed at 2000x708. Multiply coordinates by 2.48 to map to original image.]


## [2026-09-14T03:15:15.315Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad; python3 -c \"\nfrom PIL import Image\nim=Image.open('bqt-482-390.jpg'); w,h=im.size\nim.crop((0,int(h*0.60),w,int(h*0.80))).resize((int(w*1.8),int(h*0.20*1.8))).save('bqt-482-390-foot2.png')\n\""
}
```


### [2026-09-14T03:15:16.922Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:15:19.010Z] TOOL CALL #56: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt-482-390-foot2.png"
}
```


### [2026-09-14T03:15:19.329Z] TOOL RESULT

```

```


## [2026-09-14T03:15:19.324Z] INPUT

[Image: original 4462x1262, displayed at 2000x566. Multiply coordinates by 2.23 to map to original image.]


## [2026-09-14T03:15:53.469Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BQT\ncat > data/verification/sources/refs/ocr/BQT/171.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, vol. 1, printed p. 171 — read from the archive.org scan\n borhan-ghate-v1 leaf n389 (https://archive.org/download/borhan-ghate-v1/page/n389.jpg).\n Page identified by the footnote catch-line «بقیه در صفحهٔ ۱۷۲».]\n\nHeadword (col. 2):\nاندوختن* — بروزن افروختن، بمعنی جمع کردن و فراهم آوردن باشد — بمعنی قرض و وام دادن ...\n\nFootnote 5 (bottom of p. 171):\n۵ ـ پهلوی handôxtan (از handôzh «اندوز»، بمعنی جمع کردن)، مرکب\nبقیه در صفحهٔ ۱۷۲\n\n[Other footnotes on the same page, for neighbouring headwords:\n ۳ ـ پهلوی handak (کم، کمی) «مناس ۲۷۶»، رك: اند.\n ۴ ـ از اسپانیولی Andalucia ...\n ... Vandarəmainish ...]\nEOF\ncat > data/verification/sources/refs/ocr/BQT/172.vision.txt <<'EOF'\n[Borhan-e Qate', ed. Mo'in, vol. 1, printed p. 172 — read from the archive.org scan\n borhan-ghate-v1 leaf n390 (https://archive.org/download/borhan-ghate-v1/page/n390.jpg).\n Page identified by the catch-line «بقیه از صفحهٔ ۱۷۱».]\n\nContinuation of footnote 5 of p. 171 (s.v. اندوختن):\n\n  بقیه از صفحهٔ ۱۷۱\n  از: ham-tôxtan (گردآوردن، کسب کردن ـ پرداختن)، از ایرانی باستان ham-taug\n  و ham-tauj، مشتق از سانسکریت turjati, tuj (فشار دادن، راندن، انداختن، پراندن) «نیبرگ ۱۰۰».\n\n[i.e. NP اندوختن < Pahl. handôxtan (< handôzh 'andōz', 'to gather'), compound of\n ham-tôxtan 'to gather, acquire — to pay', from Old Iranian ham-taug / ham-tauj,\n derived from Sanskrit turjati, tuj 'to press, drive, throw, make fly' — citing Nyberg p. 100.]\n\nNeighbouring footnotes on the same page:\n  ۶ ـ پهلوی handûtan «تاوادیا ۱۶۰:۲»، «اونوالا ۲۱۵»، مرکب از: han-du اوستایی،\n      جزو اول han (هم) و جزو دوم du (مالیدن، پاک کردن) «بارتولمه ۶۸۸».\n  ۷ ـ رك: اندوختن.   ۸ ـ پهلوی handôh «نیبرگ ۱۰۰»، رك: اندوهگین.\nEOF\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt-482-389.jpg data/verification/sources/refs/ocr/BQT/171.png\ncp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/bqt-482-390.jpg data/verification/sources/refs/ocr/BQT/172.png\nls -la data/verification/sources/refs/ocr/BQT/ | head"
}
```


### [2026-09-14T03:15:54.523Z] TOOL RESULT

```
total 68676
drwxrwxr-x  2 sfmqrb sfmqrb   20480 Sep 13 23:15 .
drwxrwxr-x 14 sfmqrb sfmqrb    4096 Sep 13 22:36 ..
-rw-rw-r--  1 sfmqrb sfmqrb  368375 Sep  4 13:39 0001.png
-rw-rw-r--  1 sfmqrb sfmqrb    1684 Sep  4 13:39 0001.txt
-rw-rw-r--  1 sfmqrb sfmqrb  534367 Sep  4 13:39 0049.png
-rw-rw-r--  1 sfmqrb sfmqrb    2677 Sep  4 13:39 0049.txt
-rw-rw-r--  1 sfmqrb sfmqrb  620205 Sep 13 22:39 1024.png
-rw-rw-r--  1 sfmqrb sfmqrb    1735 Sep 13 22:39 1024.vision.txt
-rw-rw-r--  1 sfmqrb sfmqrb    1076 Sep  4 15:27 103.vision.txt
```


## [2026-09-14T03:15:55.635Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; ls site/pages/482.jpg 2>/dev/null; pdftoppm -f 482 -l 482 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482 && echo OK && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482.png"
}
```


### [2026-09-14T03:15:57.401Z] TOOL RESULT

```
site/pages/482.jpg
OK
-rw-rw-r-- 1 sfmqrb sfmqrb 77682 Sep 13 23:15 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482.png
```


## [2026-09-14T03:15:59.675Z] TOOL CALL #59: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482.png"
}
```


### [2026-09-14T03:16:00.255Z] TOOL RESULT

```

```


## [2026-09-14T03:16:00.252Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T03:16:14.366Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; pdftoppm -f 482 -l 482 -r 400 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482hi.png'); w,h=im.size; print(w,h)\nim.crop((int(w*0.20),int(h*0.555),int(w*0.55),int(h*0.585))).resize((int(w*0.35*3),int(h*0.03*3))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482-tow.png')\n\""
}
```


### [2026-09-14T03:16:17.468Z] TOOL RESULT

```
3400 4400
```


## [2026-09-14T03:16:19.729Z] TOOL CALL #61: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482-tow.png"
}
```


### [2026-09-14T03:16:19.856Z] TOOL RESULT

```

```


## [2026-09-14T03:16:19.854Z] INPUT

[Image: original 3570x396, displayed at 2000x222. Multiply coordinates by 1.78 to map to original image.]


## [2026-09-14T03:16:23.430Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482hi.png'); w,h=im.size\nim.crop((int(w*0.18),int(h*0.595),int(w*0.58),int(h*0.625))).resize((int(w*0.40*3),int(h*0.03*3))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482-tow2.png')\n\""
}
```


### [2026-09-14T03:16:24.929Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:16:27.257Z] TOOL CALL #63: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482-tow2.png"
}
```


### [2026-09-14T03:16:27.389Z] TOOL RESULT

```

```


## [2026-09-14T03:16:27.386Z] INPUT

[Image: original 4080x396, displayed at 2000x194. Multiply coordinates by 2.04 to map to original image.]


## [2026-09-14T03:16:31.059Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482hi.png'); w,h=im.size\nim.crop((int(w*0.18),int(h*0.625),int(w*0.58),int(h*0.650))).resize((int(w*0.40*3),int(h*0.025*3))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482-tow3.png')\n\""
}
```


### [2026-09-14T03:16:32.590Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:16:35.002Z] TOOL CALL #65: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482-tow3.png"
}
```


### [2026-09-14T03:16:35.131Z] TOOL RESULT

```

```


## [2026-09-14T03:16:35.129Z] INPUT

[Image: original 4080x330, displayed at 2000x162. Multiply coordinates by 2.04 to map to original image.]


## [2026-09-14T03:16:42.693Z] TOOL CALL #66: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; mkdir -p data/verification/sources/refs/ocr/BOOK; cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg482.png data/verification/sources/refs/ocr/BOOK/482.png; ls -la data/verification/sources/refs/ocr/BOOK/482.png"
}
```


### [2026-09-14T03:16:42.773Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 77682 Sep 13 23:16 data/verification/sources/refs/ocr/BOOK/482.png
```


## [2026-09-14T03:16:44.007Z] TOOL CALL #67: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/stop",
 "prompt": "Full etymology of \"stop\": Old English forstoppian, Vulgar Latin *stuppare, Latin stuppa, Greek stuppe. Quote the chain."
}
```


### [2026-09-14T03:16:48.666Z] TOOL RESULT

```
# Etymology Chain for "Stop"

Based on the Online Etymology Dictionary entry, here's the etymological progression:

The verb "stop" traces back through Old English **_forstoppian_** ("to stop up, stifle"), which itself derives from a Germanic borrowing of Vulgar Latin **_*stuppare_** ("to stop or stuff with tow or oakum"). This Latin term originated from **_stuppa_** ("coarse part of flax, tow").

The dictionary notes: "These words are said by many sources to be a Germanic borrowing of Vulgar Latin *stuppare 'to stop or stuff with tow or oakum'...from Latin stuppa 'coarse part of flax, tow.'"

However, the source also mentions that some etymologists, including Barnhart, propose "the whole Germanic group might be native, from a native base *stoppon," indicating scholarly debate about whether the ultimate origin is truly Latin or indigenous Germanic.
```


## [2026-09-14T03:16:51.608Z] TOOL CALL #68: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/stuff",
 "prompt": "Full etymology of the noun \"stuff\": Old French estoffe, estoffer, and whether it comes from Latin stuppa/Greek stuppe or from Germanic (Old High German stopfon)."
}
```


## [2026-09-14T03:16:53.405Z] TOOL CALL #69: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/top#Turkish",
 "prompt": "Give the Turkish etymology of \"top\" (ball, cannon): Ottoman Turkish, Old Turkic, Proto-Turkic reconstruction, and any mention of Sanskrit stupa. Also list descendants (Persian توپ etc.)."
}
```


### [2026-09-14T03:16:56.763Z] TOOL RESULT

```
# Etymology of "Stuff"

The noun "stuff" originates from early 14c. English, derived from Old French *estoffe*, meaning "quilted material, furniture, provisions."

## Disputed Origins

The ultimate source remains uncertain. French etymological sources suggest it comes from Old High German *stopfon* ("to plug, stuff") or a related Frankish word. However, the OED considers this connection "open to strong objections."

## Semantic Evolution

The word's meaning expanded significantly over time:

- **c. 1400**: "material for working with in various trades"
- **early 15c.**: "military stores and supplies"
- **mid-15c.**: "goods or possessions generally" and "substance or matter of unspecified kind"
- **1550s**: figuratively, "what a person is made of"
- **1570s**: "worthless ideas" (as in *stuff and nonsense*)
- **1929**: "narcotic, dope, drug"

The verb form emerged in mid-14c., initially meaning "furnish" or "reinforce," later developing culinary applications (stuffing poultry) and modern slang uses.
```


### [2026-09-14T03:16:58.051Z] TOOL RESULT

```
# Turkish Etymology of "top" (ball/cannon)

Based on the Wiktionary content provided, I found **no etymological information** about the Turkish word "top" (meaning ball or cannon).

The article only covers the English word "top" and its etymology from Middle English and Old English sources. While the Turkish section lists "top" as a noun with declension and derived terms, it does not provide etymological details for the Turkish term.

The content does not include:
- Ottoman Turkish etymology
- Old Turkic origins
- Proto-Turkic reconstructions
- Any connection to Sanskrit stupa
- Persian descendants (توپ)

To obtain this etymological information, you would need to consult the Turkish Wiktionary entry for "top" directly, or academic sources on Turkish and Persian loanwords in these languages.
```


## [2026-09-14T03:17:01.212Z] TOOL CALL #70: WebFetch

```json
{
 "url": "https://www.nisanyansozluk.com/kelime/top",
 "prompt": "Give Nişanyan's etymology of Turkish \"top\" (ball, cannon): Old Turkic/Proto-Turkic forms, first attestations, and whether any Sanskrit or Indo-European origin is proposed."
}
```


## [2026-09-14T03:17:03.045Z] TOOL CALL #71: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D8%AA%D9%88%D9%BE",
 "prompt": "Give the Persian etymology of توپ (tup) 'ball, cannon': what language it was borrowed from (Turkish/Ottoman), and any further origin given."
}
```


### [2026-09-14T03:17:04.810Z] TOOL RESULT

```
I cannot provide the etymology information you're requesting based on the content supplied. The webpage excerpt shown only contains the header, navigation elements, and footer of Nişanyan Sözlük (Nişanyan Dictionary), but does not include the actual dictionary entry for the word "top" or any etymological data about its Proto-Turkic origins, Sanskrit connections, or historical attestations.

To obtain this information, you would need to access the full dictionary entry for "top" on the Nişanyan Sözlük website directly.
```


### [2026-09-14T03:17:07.401Z] TOOL RESULT

```
# Persian Etymology of توپ (tup)

According to the Wiktionary entry, the word توپ derives from **Turkic languages**. The source states: "From Turkic. Compare Turkish top."

The entry does not provide any further etymological origin beyond identifying it as a Turkic borrowing. No ultimate source language is specified in the documentation.
```


## [2026-09-14T03:17:10.564Z] TOOL CALL #72: WebSearch

```json
{
 "query": "Wiktionary Proto-Turkic *top ball Old Turkic topık etymology Turkish top"
}
```


### [2026-09-14T03:17:17.095Z] TOOL RESULT

```
Web search results for query: "Wiktionary Proto-Turkic *top ball Old Turkic topık etymology Turkish top"

Links: [{"title":"top - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/top"},{"title":"Reconstruction:Proto-Turkic/topïk - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/top%C3%AFk"},{"title":"طوپوز - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%B7%D9%88%D9%BE%D9%88%D8%B2"},{"title":"topuz - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/topuz"},{"title":"topuk - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/topuk"},{"title":"Reconstruction:Proto-Turkic/top - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/top"},{"title":"توپ - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%D8%AA%D9%88%D9%BE"},{"title":"Category:Old Turkic terms derived from Proto-Turkic - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Old_Turkic_terms_derived_from_Proto-Turkic"},{"title":"Category:Turkish terms derived from Proto-Turkic - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Category:Turkish_terms_derived_from_Proto-Turkic"},{"title":"Old Turkic","url":"https://en.wikipedia.org/wiki/Old_Turkic"}]

Based on the web search results, here is information about the etymology of Turkish "top" related to Proto-Turkic and Old Turkic:

Turkish "top" is inherited from Ottoman Turkish طوپ (top), from Proto-Turkic *top ("round thing"). It is cognate with Azerbaijani top, Uzbek to'p, Uyghur توپ (top), Kazakh доп (dop) and others.

Regarding the Proto-Turkic *topïk variant, the search results show that Karakhanid had تُبِقْ (topık, "small ball, pellet; ankle bone"), and Turkish "topuk" derives from Ottoman Turkish طوپوق (topuk), from Proto-Turkic *topïk ("knee; kneecap; ankle").

Additionally, Proto-Turkic *topuz ("mace, club") is a development of *top ("round thing, ball"), showing how the basic root meaning expanded to related forms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:17:20.504Z] TOOL CALL #73: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/top",
 "prompt": "Give the Proto-Turkic *top reconstruction: meaning, descendants (Turkish top, Azerbaijani, Uzbek, Uyghur, Kazakh), and any borrowings into Persian/Armenian/etc. Note if any Indo-European or Sanskrit origin is proposed."
}
```


## [2026-09-14T03:17:23.286Z] TOOL CALL #74: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%82%E0%A4%AA",
 "prompt": "Give the Sanskrit etymology of स्तूप (stūpa): meaning, Proto-Indo-European root, cognates (Greek stupos/stuppe, Latin stupere?), and descendants."
}
```


### [2026-09-14T03:17:26.695Z] TOOL RESULT

```
# Proto-Turkic *top Reconstruction

## Meaning
The Proto-Turkic term *top* meant "round thing, ball" according to the Wiktionary entry.

## Descendants
The word spread across multiple Turkic branches:

**Oghuz branch:** Turkish *top*, Azerbaijani *top*, Ottoman Turkish *top*, Turkmen *top*, Gagauz *top*

**Karluk branch:** Uzbek *to'p*, Uyghur *توپ* (top)

**Kipchak branch:** Tatar *туп* (tup), Bashkir *туп* (tup), Kazakh *доп* (dop), Kyrgyz *топ* (top), Crimean Tatar *top*, Karakalpak *top*

**Other branches:** Chuvash *тупӑ* (tup̬ă), Khalaj *top*

## Borrowings
The term entered numerous non-Turkic languages through Ottoman Turkish and Persian:

Persian *توپ* (top/tup) → Hindi *तोप* (top), Urdu *توپ* (top)

Greek *τόπι* (tópi), Albanian *top*, Armenian *թոփ* (tʻopʻ), Georgian *თოფი* (topi), and Slavic languages (Macedonian *топ*, Serbo-Croatian *top*, Slovene *top*)

## Etymology
The document contains no discussion of Indo-European or Sanskrit origins for this reconstruction.
```


### [2026-09-14T03:17:29.857Z] TOOL RESULT

```
# Sanskrit Etymology of स्तूप (stūpa)

## Meaning
The Sanskrit term refers to a "mound" or "heap," and specifically denotes Buddhist monuments (stupas/dagobas) or "relic shrine[s] or casket[s], containing bone or hair from a deceased relative or saint."

## Proto-Indo-European Origin
The word derives from "Proto-Indo-Iranian *stúHpas," and scholars consider it related to स्तुका (stukā, meaning "tuft of hair").

## Cognates
External comparisons include:
- Ancient Greek: στυππεῖον (stuppeîon, "coarse hemp fiber") and στῡ́φω (stū́phō, "to contract, draw together")
- Old Armenian: ստև (stew, "(camel's) hair")
- Proto-Finnic: *tup'as ("mound, tuft"), possibly borrowed from the Proto-Indo-Iranian source

## Descendants
The term spread across multiple languages: Pali (thūpa), Prakrit, Gandhari, Chinese (塔婆), Burmese, Thai, Telugu, and English (stupa).
```


## [2026-09-14T03:17:39.443Z] TOOL CALL #75: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/stucco",
 "prompt": "Etymology of \"stucco\": Italian stucco, Germanic/Langobardic *stukki, Old High German stukki 'crust, piece, covering', PIE root. Also briefly: does Etymonline link it to PIE *(s)teu- 'to push, stick, knock, beat'?"
}
```


## [2026-09-14T03:17:40.958Z] TOOL CALL #76: WebFetch

```json
{
 "url": "https://www.etymonline.com/word/study",
 "prompt": "Etymology of \"study\": Old French estudier, Latin studium/studere 'to be diligent', and the PIE root given (e.g. *(s)teu- 'to push, stick, knock, beat'). Quote the root line."
}
```


### [2026-09-14T03:17:44.018Z] TOOL RESULT

```
# Etymology of "Stucco"

Based on the Etymonline entry, stucco's etymology traces through Italian to Germanic roots:

**Direct origin:** The term comes from Italian *stucco*, likely derived from Germanic sources like Old Saxon *stukki* and Old High German *stukki*, meaning "crust, piece, fragment."

**PIE connection:** The document indicates the Germanic root relates to the Proto-Indo-European root *\*sta-* meaning "to stand, make or be firm." However, there is a noted alternative theory: "said to be from an extended form of PIE root *(s)teu-* 'to push, stick, knock, beat'" though this appears to be a secondary or disputed etymology rather than the primary accepted one.

The entry suggests *\*sta-* is the more probable PIE ancestor, though both theories connect to the concept of something solid or structural.
```


### [2026-09-14T03:17:44.047Z] TOOL RESULT

```
# Etymology of "Study"

The word "study" traces back through Old French *estudiier* to Latin *studium* ("study, application") and *studere* ("to be diligent").

The ultimate Proto-Indo-European root is cited as:

> "*(s)teu- (1) 'to push, stick, knock, beat'"

According to the etymology source, the semantic development reflects "pressing forward, thrusting toward," which evolved into the meaning of "striving after" knowledge and learning.
```


## [2026-09-14T03:17:52.322Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN stucco/stop/stuff/stupid ===\"; grep -no \"stucco, n\\..\\{0,300\\}\" KLN_1966.txt | head -3; grep -no \"stop, tr\\..\\{0,400\\}\\|stop, intr\\..\\{0,300\\}\" KLN_1966.txt | head -3; grep -no \"stuff, n\\..\\{0,350\\}\" KLN_1966.txt | head -3; grep -no \"stupid, adj\\..\\{0,250\\}\" KLN_1966.txt | head -3"
}
```


### [2026-09-14T03:17:53.399Z] TOOL RESULT

```
=== KLN stucco/stop/stuff/stupid ===
```


## [2026-09-14T03:17:54.057Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== LKT top ===\"; grep -n \"top\\b.\\{0,200\\}Kanone\\|Kanone\" LKT.txt | head -10; echo \"=== TTS top ===\"; grep -n \"top.\\{0,120\\}Kugel\\|Kugel.\\{0,80\\}top\" incoming/TTS/TTS_vambery1878_uoft_djvu.txt | head -10"
}
```


### [2026-09-14T03:17:55.197Z] TOOL RESULT

```
=== LKT top ===
1721:'Fülle  von  Milch  und  Wasser;  Stimmen- gewirr'; hieraus  it.  gazzarra  'Lärm', gazzurro  'Freude,  der  man  durcii Kanonenschüsse  oder  militärische  Musik Ausdruck  gibt',  sp.  algazara,  pg.  alga- zarra  'Kampfgeschrei'.
1782:'Kugel'  [Horn  NpEt  S.  207,  Nr.  928], ebenso  tk.  kuUe,  gülle  'Kanonenkugel'; hieraus  rum.  ghiulea  'dass.,  Bombe', bulg.  gulle,  serb.  zulle  'Kugel  zum Schießen'.    [Sain.ö2.   Bern  SlEtWb  375.
=== TTS top ===
10635:cag.  tob,  top  — RsiVite.  Kugel,  Knäuel,  Busch;  topi=^eme  runde, 
10642:osm.  <o2>  =  Kugel,  Ballen;  /e2>e=  Spitze,  Hügel;  topalak,  tomh- 
14496:<o/>,  top  (Kugel)  192.
```


## [2026-09-14T03:17:59.620Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '10630,10650p' incoming/TTS/TTS_vambery1878_uoft_djvu.txt"
}
```


### [2026-09-14T03:17:59.689Z] TOOL RESULT

```
zusammen. 

I.    f— . 

cag.  tob,  top  — RsiVite.  Kugel,  Knäuel,  Busch;  topi=^eme  runde, 
halbkugelföi-mige  Kappe  in  Chokand ;  tojtah  —  der  Knoten 
eines  Strickes;  fOjf>ca/i;  =  fettes,  rundes  Pferd;  topic,  töpie 
(top  hije?)  =  ie,iiQ,  runde  Stute;  töj)e,  tüpe,  tipe  =  E.ügel, 
oberer  Theil,  Kopfscheitel;  fo/^^ama/c  =  sammeln ;  föpclcn- 
meJc=^  rnnci  zugespitzt  werden. 

osm.  <o2>  =  Kugel,  Ballen;  /e2>e=  Spitze,  Hügel;  topalak,  tomh- 
aZaZ;  =  kugelrund;  <ojja!Z  =  krumm,  hinkend  (eigentl.  der  zu- 
sammengeschrumpfte runde  Zustand  eines  Gliedes). 

kaz.  <M&a7as>Ma/;  =  sich  zusammenkauern,  sich  zusammenziehen. 

CUV.  <M&e  =  Anhöhe,  Hügel,  oben;  #Vi'6pZ;=  Schopf  der  Vögel. 

alt.    töbö,  ^ööe  =  Hügel.
```


## [2026-09-14T03:18:00.944Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== KLN stuppa ===\"; grep -n \"stuppa\" KLN_1966.txt KLN_1971.txt | head -10; echo \"=== SKT stop/stuff ===\"; grep -n \"stuppa\\|stupa\" SKT.txt | head -10"
}
```


### [2026-09-14T03:18:01.022Z] TOOL RESULT

```
=== KLN stuppa ===
KLN_1971.txt:85789:L. *stuppare, ‘to stop with flax or tow’ (whence 
KLN_1971.txt:85791:stuppa, stupa, ‘the coarse part of flax, tow’. See 
KLN_1971.txt:232553:perh. a blend of VL. *stuppare , ‘to stop with tow’ 
KLN_1971.txt:232786:(j bot .) — ModL., fr. L. stipa, stupa, stuppa , ‘the 
KLN_1971.txt:233245:fed). These words derive fr. ML. stuppare , ‘to 
KLN_1971.txt:233248:tow’), fr. L. stuppa, stupa, ‘the coarse part of 
KLN_1971.txt:234584:The derivation of OF. estoffe, etc., fr. L. stuppa , 
KLN_1966.txt:13692:estop,  tr.  v.,  to  bar;  (law),  to  bar  by  estoppel.  — AF.  and  OF.  estoper  (F.  etouper),  ‘to  stop’,  fr. L.  *stuppare ,  ‘to  stop  with  flax  or  tow’  (whence also  It.  stoppare,  OProven?.  estopar),  Fr.  L. stuppa,  stupa,  ‘the  coarse  part  of  flax,  tow’.  See stop.
KLN_1966.txt:36827:Stipa,  n.,  a  genus  of  plants,  the  feather  grass (bot.)  —  ModL.,  fr.  L.  stipa,  stupa,  stuppa,  ‘the coarse  part  of  flax,  tow,  hards’,  fr.  Gk.  ax’jTT-rr,. See  stupe.
KLN_1966.txt:36906:stop,  tr.  and  intr.  v.  —  ME.  stoppen,  fr.  OE.  for- stoppian,  ‘to  stop  up,  close',  rel.  to  MLG.  (  = Du.)  stoppen,  OHG.  stopfon  (MHG.,  G.  stop- fen).  These  words  derive  fr.  ML.  stuppare,  ‘to stop  with  tow’  (whence  also  It.  stoppare, OProvenQ.  estopar,  F.  itouper,  ‘to  stop  with tow’),  fr.  L.  stuppa,  stupa,  ‘the  coarse  part  of flax,  tow’,  fr.  Gk.  axu7nt7),  of  s.m.,  which  is cogn.  with  OI.  stupdfi,  ‘tuft  of  hair’.  The  Teut. words  mentioned  were  influenced  in  meaning  by L.  stupere,  ‘to  be  stunned,  be  stupefied’.  Cp. stopple,  estop,  estoppel.
=== SKT stop/stuff ===
18623:Stop.  (L.)  Not  E..  but  L.  M.  E.  rtep /c«,  A.  S.  stoppian,  to  stop  up  ;  so  alto  Ou. siopptn,  to  stop,  stuff,  cram.  Swcd.  stpppa^ Dan.  itoppt.  C*.  stopftti.  IIaI.  stoppart,  to stop  up  with  low.  Low  L.  ttupart,  to  stop up  with  tow,  cram,  stop.  All  from  L. stupa,  ttuppa,  coarse  part  of  Abje,  hanls^ oakum,  tow.  Cf.  Gk.  otiIvt;,  vtusvt},  the same ;  Skt.  stumhh,  to  slop.  Allied  to Stub,  Stupid,  Stomp.  Dor.  ttopp-U,  Le stopper.
18624:estop.  (F.  -  L.)  A  law  term  ;  to  stop, impede.  —  O.  F.  tstoptr\  Low  L.  stupaft (above).
18735:StufT,  materials.  (F.-L.)  O.  F.  atofe. *  stufTe ; '  Cot.  —  L.  stupa,  stuppm,  the  coarse part  of  flax,  hards,  tow;  the  pronunciation of  this  L.  word  being  Gennanised  before  it passed  into  French  (Dies).  Cf.  G.  staff, slufT,  materials.  %  The  sense  of  the  L. word  is  better  preserved  in  the  verb  to stuff,  i,  e.  to  cram,  to  stop  up,  <.'».  ttcp/en, to  fill,  stuff,  quilt,  from  Low  L.  stuppatt, to  stop  up ;  wDcnce  also  £.  Stop,  q.  v.
```


## [2026-09-14T03:18:10.452Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '234575,234595p' KLN_1971.txt; echo \"=== stucco KLN ===\"; grep -n \"stucco\" KLN_1966.txt | head -3"
}
```


### [2026-09-14T03:18:10.541Z] TOOL RESULT

```
meant orig. ‘silk’, i.e. ‘stuff that contracts’, and 
ult. derive fr. Gk. <rru<petv, ‘to contract, draw 
together’, fr. I.-E. base *stu-bh -, an enlargement 
of base *$t(h)au-, *st(h)u-, ‘to condense ; stiff, up- 
right’; see steer, ‘to direct’ .TheGreek origin of OF. 
estoffe and its equivalents is substantiated by the 
fact that silk culture (originating in China) was 
introduced into Byzantium by Justinian as early 
as in 552; see Kluge-Mitzka, EWDS., p. 752. 
The derivation of OF. estoffe, etc., fr. L. stuppa , 
‘tow’, occurring in most etymological dictiona- 
ries, must be rejected. 

Derivatives : stuff, adj., stuff-ing, n., stuff-y, adj., 
stuff-i-ly, adv., stuff-i-ness, n. 
stuff, tr. and intr. v. — Late ME., fr. OF, estoffer 
(F. itoffer), ‘to use material in making (some- 
thing), to stuff’, which is rel . to, and prob. derives 
from estoffe, ‘stuff material’. See stuff, n. 
Derivative: stuff-ing , n. 

=== stucco KLN ===
33734:Sarah,  also  Sara,  1)  fem.  PN. ;  2)  in  the  Bible,  the wife  of  Abraham  and  the  mother  of  Isaac.  — Lit.  ‘princess’,  fr.  Heb.  sarah,  fem.  of  sar, ‘prince’,  fr.  sarar,  ‘he  ruled’,  which  is  rel.  to Akkad,  sharru,  ‘king’,  sharratu,  ‘queen’, sarangousty,  n.,  stucco  made  waterproof.  —  Pers. sarangushti,  ‘paste  for  painting  the  tips  of  the fingers’,  fr.  sar,  ‘head,  extremity,  tip’,  and  an- gusht,  ‘finger’.  Pers.  saris  cogn.  with  Gk.  xapa, ‘head’,  L.  cerebrum,  ‘brain’;  see  cerebrum  and cp.  serang,  scraskier,  sircar.  Pers.  angusht  is  rel. to  Avestic  angushta-,  ‘toe,  finger’,  OI.  angusthah, ‘big  toe,  thumb’,  and  cogn.  with  Gk.  ayxdw, ‘elbow’,  ayxuXo?,  ‘crooked,  curved’,  L.  angulus, ‘angle,  corner’ ;  see  angle,  ‘corner’.
36848:stochastic,  adj.,  conjectural.  —  Gk.  axo/aoxino;, fr.  axo/a^eaDm,  ‘to  aim  at,  guess,  conjecture’, fr.  oxoyoq,  ‘aim,  target,  mark’,  from  base *stegh-,  ‘to  point,  prick,  sting'.  Cp.  the  nasalized var.  *stengh-,  whence  the  English  verb  sting (q.v.)  For  the  ending  see  adj.  suff.  -ic. stock,  n.  —  ME.  stok,  fr.  OE.  stocc,  ‘trunk,  log, stock’,  rel.  to  ON.  stokkr,  ‘block  of  wood,  trunk of  a  tree',  Dan.  stok,  Swed.  stock,  OS.,  OFris. stok,  MDu.  stoc,  ‘tree  trunk,  stump’,  Du.  stok, ‘stick,  cane’,  OHG.,  MHG.  stoc,  ‘tree  trunk, stick’,  G.  Stock,  ‘stick,  cane’,  and  to  OE.  stycce, OS.  stukki,  ON.  stykki,  Swed.  stycke,  MDu. stuc(ke),  Du.  stuk,  OHG.  stucci,  MHG.  stiicke, G.  Stuck,  ‘piece’,  OE.  stocu,  ON.  stuka,  OHG. stuhha,  ‘sleeve’,  and  cogn.  with  Lith.  stugti,  ‘to be  prominent’,  stimgis,  ‘knife  handle’,  OI.  tujati, tuhjati,  ‘he  pushes’.  OF.  estoc,  ‘stem,  trunk’,  It. stocco,  ‘dagger;  rapier’,  are  Teut.  loan  words. Cp.  chock,  stoccado,  stoker,  stook,  stucco,  and the  second  element  in  alpenstock,  linstock, maulstick.
37109:Derivatives:  stubborn-ly,  adv.,  stubborn-ness ,  n. stucco,  n.,  a  kind  of  fine  plaster  used  as  a  coating for  walls.  —  It.,  fr.  OHG.  stucchi,  ‘crust,  coat¬ ing,  piece’  (whence  MHG.  stiicke,  G.  Stiick, ‘piece’);  rel.  to  OS.  stukki ,  ON.  stykki,  OE. stycce,  ‘piece’,  and  to  E.  stock  (q.v.) Derivatives:  stucco,  tr.  v.,  stucco-er,  n. stuck,  past  tense  and  pp.  of  stick.  —  Formed prob.  on  the  analogy  of  stung,  past  tense  and pp.  of  sting.  See  stick,  v. stud,  n.,  a  collection  of  horses.  —  ME.  stod, stode ,  fr.  OE.  stod,  ‘stud,  herd  of  horses’,  rel.  to ON.  stod,  MLG.  stod,  OHG.,  MHG.  stuot, ‘herd  of  horses’,  G.  State,  ‘mare’,  and  cogn. with  OSlav.  stddo,  ‘herd’,  Lith.  stodas,  ‘a  drove of  horses’.  These  words  derive  fr.  I.-E.  *stddho-, an  enlargement  of  base  *sta-,  ‘to  stand’,  and orig.  meant  ‘a  standing  place  for  horses’.  See state  and  cp.  steed.
```


## [2026-09-14T03:18:32.770Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== WLD Bd2 steu ===\"; grep -n \"st(h)eu-\\|steu-p-\\|stū̆p\\|stup-\" incoming/WLD/WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T03:18:32.843Z] TOOL RESULT

```
=== WLD Bd2 steu ===
```


## [2026-09-14T03:18:34.720Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== IEC steup/stupos ===\"; grep -n \"^steup\\|^stupos\\|^steubh\\|^steug\\|^steud\\|steupos\\|stupa\" IEC.txt | head -20; echo \"=== SYN ball ===\"; grep -n \"Skt. stūpa\\|stupa\" SYN.txt | head"
}
```


### [2026-09-14T03:18:34.826Z] TOOL RESULT

```
=== IEC steup/stupos ===
17219:steud- (stud-, sth-) “press, push’. Cf. stoud-, (sth-), stud-, sthud- & steuið. WP II, 618. (E-gde explicit: Gmc. & Slav). E-gde in MHG stiezen, sv. “push? Alb. cf. shtyej, v. (push, ambig. cf. steuio); Lat. (z-gde) studeo, Gre, v. “apply oneself, concentrate on); MHG (z-gde) stuz, gs: stutzes, sm. “jol; G cf. stutzen, v. ‘buffet’; OCS cf. Studi, f. (1) ‘gait, manner, way’; W cf. (variant) sut, m. ‘manner’; sud, m. ‘shape’ (both fr. *steut- or *stout-)
17220:steug- (stüg-) ‘bend, curve, twist MI. stuag, f., stuagh, m. (1) “arch, bow; roll; book: (*stüg- in) G verstauchen, Du. ver-stuiken, v. ‘sprain’; (for Fris. stjūch, adj. ‘surly, stubborn" see next)
17234:steuplis, steuplo(n), cf. stüp-. Variant steupr- (stupr-). Arm. ambig. Ir. stualán, m. ‘simpleton’; OCS Stupli, adj. ‘feeble’; cf. (variant) Arm. t'iwr, o-st. ‘wrong, askew’; Lat. (z-gde) stuprum, n. ^wrong-doing'
17292:*ore-crusher); Ukr. stupa, f. ‘stamping-mill’; cf. stupom, adv. “at a walking pace’; OCS cf. postopü, m. ‘step, pace’; Blg. stápa, f. ‘mortar, treadle’; Cz. cf. po-stup, m. ‘method’; Li. stampinti, intr. ‘trail, drag’
=== SYN ball ===
9953:It. stoffa, Fr. étoffe (Sp. estofa), Rum. stofd, fr. the Gme. word seen in NHG stof, this fr. Lat. stuppa ‘coarse linen, tow’, fr. Grk. ortamn (perh. : Skt. stupa- ‘tuft of hair’, Walde-P. 2.620). This is preferable to the usual deriv. of Gmc. fr. Romance, though the ins and outs of borrowing are complicated. REW 8332.
11989:2. MUat. stufa (stuba, stupa), It. stufa, Fr. étuve, Sp. estufa, used for ‘hot bath, hothouse’, etc. and finally (lIt., Sp.) for ‘stove’, OE stofa ‘hot bath’, OHG stuba ‘bathroom, heated room’, MLG stove (> ME stove ‘hot-air bath, sweating-room’, also ‘heatedsitting-room or bedroom’; NE stove in present sense since about 1600; > NIr. stdv, W. stof, etc.) The continental Gme. forms de- veloped in the direction of ‘room’ and spread to Balto-Slavie mostly in this sense (cf. 7.21). But the development to ‘stove’, asin NE and Romance, shows itself in some of the Balkan derivs., namely (in form through Hung. szoba, now only ‘room’) Turk., Bulg. soba, Rum. sobé, NG copra (soba). Stender- Petersen 249.
15368:7 af bes, ee tmelt’, ete. rk. ae : a ‘make stoop, overthrow, oo fe also ‘cast metals’, Dan. an t’, caus. to ON stupa,
```


## [2026-09-14T03:18:47.288Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la incoming/WLD/ 2>/dev/null | head; echo \"=== grep stuppa in WLD Bd2 ===\"; grep -n \"stuppa\\|stupa\\|stûpa\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"=== WLD band3 index steu ===\"; grep -n \"stuppa\\|stûpa-\\|stupa-\" WLD_band3.txt | head -10"
}
```


### [2026-09-14T03:18:47.369Z] TOOL RESULT

```
total 146216
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb  2993454 Sep  4 14:06 WLD_Bd1_1930_dli_70244_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 42256714 Sep  4 14:06 WLD_Bd1_1930_dli_70244_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4327601 Sep  4 14:06 WLD_Bd1_pages.txt
-rw-rw-r--  1 sfmqrb sfmqrb  2417287 Sep  4 14:06 WLD_Bd2_1927_dli_106624_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 94865800 Sep  4 14:06 WLD_Bd2_1927_dli_106624_text.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  2833963 Sep  4 14:06 WLD_Bd2_pages.txt
=== grep stuppa in WLD Bd2 ===
41117:stupas pi. „Blutfedern, kleine Ruten".
41133:werden", nhd. stdupen; aisl. stupa „steif emporstehn, in die Hohe ragen",
41154:u. stif, stuh, stupe, st0p,               Vf. LEWb,^ u. stupa, stupeo, stuprum^ tituho, Boi-
41184:{stupa- in der Bed. „Hauptbalken eines Hauses“ erinnert allerdings an
41186:(daraus lat. stupa, stuppa ds.); gr. crvqxv „ziehe zusammen, mache dicht,
41200:weisen lett. stupa „Blutfeder, kleine Rute^*', stupe, stups „Besenstumpf“,
=== WLD band3 index steu ===
```


## [2026-09-14T03:18:50.078Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '41175,41210p' incoming/WLD/WLD_Bd2_pages.txt; echo \"=== page tag near ===\"; grep -n \"pdf page\" incoming/WLD/WLD_Bd2_pages.txt | awk -F: '$1<41200' | tail -2"
}
```


### [2026-09-14T03:18:51.111Z] TOOL RESULT

```
       mittlung ermoglichen wiirde und ind. st- gegeniiber sth^- in stha- „stehn“
       vielleicht kein            durchschlagender Scheidungsgrund ist.
     Ai, ghrta-stavah Acc. pi. „Tropfen   von geschmolzener Butter^ (erinnert
in der   Bed. an gr. oriaQ); prthu-siu- „niit einem breiten Zopfe% stii-h-a,
stuka-m. „Zotte, WolB oder Haarflo eke, Zopf“, stokd- m. „Tropfen“ (kaum
umgestellt aus "^skota-^ zu skut- „traufeln“, Wackernagel Ai. Gr. 1 277 m. Lit.),
(Iit.s^wA’a 5 „Klumpen“ s. S. 615), mit der Bed.-Entw. „Klumpchen, rundliches
Ding‘‘, wahrscheinlich lett. stiHiis „Wickelkind“ und ai. stuka- m. „Kind,
Tierjunges“; ai. stu-p-a- m. „Schopf, Haarbusch“, stupd- m. „SchopP'
{stupa- in der Bed. „Hauptbalken eines Hauses“ erinnert allerdings an
sthuna „Saule“ u. dgl. unter sta-, stan- „stehn“), gr. orvict}, OTvnjir] „Werg“
(daraus lat. stupa, stuppa ds.); gr. crvqxv „ziehe zusammen, mache dicht,
hart, schmecke herb‘‘, oxvppa „zusammenziehendes Mitteh*, oxvxpK; „das Zu-
sammenziehen, Beizen^‘,                    orvmiy.og „zusammenziehend“,                           axvq)6g,    oxvcpQog,
oxvcpvog „herb, zusammenziehend'", oxvpvog „fest, kompakt”.
     Vgl. Pick              145, 570,      Prellwitz^ u. oxvjirj,          oxv(p(o,     Persson Beitr. 309,
714, 949          (aisl.   suein-stauli „Knabe“?).
     Wohl hier (nicht h^i steu-d-,                       „sto6en“) sind einzureihen;                   \eit, studins,

studi „Sulze'' (Prellwitz), aksL st^ld^ „Kalte“, stynqti „erkalten“   und stydHi
„8ich                              mss. istygnuth, stugnui'b „gefrieren“, gr.
          schamen'' (,,*erstarren“) ;
arv|, oxvyog im PL „durchdringender Prost, Eiseskalte^, oxvyog n. „(*Schau-
der) Abscheu, Ha6'‘, oxvyeco „has8e, verabscheue, fiirchte^ (aber lit. stiigti
„in die Hohe stehn“, ir. stuaic „Zinne'' s. unter steu-, steug- „sto8en“; ebenso
weisen lett. stupa „Blutfeder, kleine Rute^*', stupe, stups „Besenstumpf“,
anord. stufr „Stumpf“, gr. oxvTiog „8tock, Stiel, Stengel^ auf eine von den
obigen 2?-Pormen ganz verschiedene Gdbed.).
                                                                                    «

1. (s)teg-                 mit sth-),
                   „decken‘‘       (ai.

     Ai. sihdgati, sthagayaH ,,verhullt, verbirgt'*;                        gr. oieyco             „decke,     schiitze
usw.**,      oreyog, xeyog n.             (= air. tech),    oxiytj,    xeyrj „Dach, Haus**, oxsyavog
 j.deckend, schirmend; bedeckt, versteckt**,                          oxeyvog „bedeckend, schutzend;
=== page tag near ===
```


## [2026-09-14T03:19:00.508Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"steu-, steud-\\|(s)teu-\\|steu-p-, steu-b-\\|steup-, steub-\" incoming/WLD/WLD_Bd2_pages.txt | head -10; echo \"---\"; grep -n \"tumpati\\|tupati\\|tujati\" incoming/WLD/WLD_Bd2_pages.txt | head -10"
}
```


### [2026-09-14T03:19:00.578Z] TOOL RESULT

```
41027:    3.     (s)teu-d-:
---
```


## [2026-09-14T03:19:04.017Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"tumpáti\\|tópati\\|tumpati\\|tup&ti\\|tuñjáti\\|tunjati\\|tujáti\" incoming/WLD/WLD_Bd2_pages.txt | head; echo \"=== around 40900-41030 headings ===\"; sed -n '40960,41000p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-14T03:19:04.090Z] TOOL RESULT

```
=== around 40900-41030 headings ===
weiter Armel“, anord, (Lw.?) stfika „ Armel, Ausbau, Yorsprung*'',^ mit u
ags. stocu f. „langer Armek' (wie earm-, hand-stoce „Handstauche, Armel",
Falk-Torp u. stok). Hierher afries. sMh „Maiitel" (S. 621).
   Diese germ. Sippe zu (s)feug~ „sto6en" z. B. nach Ehrismann PBrB. 18,
215 ff., Kluge ® 439, Yf. LEWb.^ 747f. (Lit.). Dagegen iieigen Fick IIP
494, Falk-Torp u. stoJc, stylcke, skive I (vgl. auch stub), Weigand-Hirt 955,
975 zur Annalame eines Bed.-Kernes ;,steif- (woraus „stofien" entwickelt
sei; doch s. die Yorbemerkung) und zum Yergleich mit lit. stiigstu, stugti
„in die Hohe stehn", stugs-au, ~dti „steif dastehn" (alit. staugineti „schlendern"
eigentlich „steif, stolpernd gehn"?                   von Bezzenberger BB. 12, 241 mit norw.
stauka, s. o., verglichen; aber nir. stuaic ,,Spitze, Zinne, hervorragende
Felsspitze" ist wegen des sU brit. oder germ. Lw., Fick 11^314), die
tatsachlicb zu steu — sta sich stellen (aber vielleicht gJi fortsetzen, s. o, 1),
sowie mit russ. istggmih, stugmdh „gefrieren (^steif, starr werden?)", gr.
orvyeg pi. „Eiskalte", OTvyog „Abscheu, HaB", oTvyEco „hasse, verabscheue,
fiirchte",      die     eher     zu steu-        „sich      verdichten,       sich   ballen"   zu   gehoren
scheinen.
      Yielleicht      ist     auch got. stigqcm          ,,sto6en‘'     {histugq{s‘l)   „Anstofi"),   agutn.
stinqua, aschwed. stlnka „prallen"  von einem nas. Praesens ^stung-yS (:ai.
tunjdti) aus durch Ablautentgleisung entstanden (Osthoff Par. I 363 f., Bgm.
II 2 3, 284; Lit. iiber das vielumstrittene Wort und die flgd. germ. Sippe
bei Osthoft* aaO. und bei Falk-Torp u. stinke, Reichelt KZ. 39, 78); die
andern germ. Sprachen bieten freilich mit dieser Herleitung kaum ver-
einbare Bedd., die aber anderer etymologischer Herkunft sein konnen
      Aisl.   st0kua st. Y. „spritzen              intr.,    bersten, springen, zsschrecken (auch
prallen)"; norw. stokka                auch „stinken", ags. stincan „stieben, dampfen, auf-
wirbeln; stinken", as. stinken „stinken“, ahd. stincan „stinken, riechen";
kaus. aisl. st^kkua „verjagen, besprengen", ags. stencan „zerstreuen“, mhd.
stenken „stinken machen'"; as. stank, stunk, ags. stenc ,,Geruch, Gestank",
ahd. stanc jjds., auch Duft"; Bed.-Kern dieser Gruppen scheint etwas wie
,,stiebea"      (wie bei "^dheu-,            dem    ebenfalls   Worte fiir Geruch entstammen,
und bei dt. rauchen              :   riechen), vgl.      Franck - van Wijk u. stinken (die Bed.
..stinken" mit Feist GWb. 250 wieder aus anderer Quelle herzuleiten, ist
kein AnlaB). Weitere Ankniipfung fraglich; mir. toclit „Ge 3 tank" hatte,
wenn nach Stokes KZ 41, 389 als ^tong-to- verw'andt, dieselbe Bed.-Entw.
hinter sich; es  kann namlich nicht mit gr. rayyog „ranzig", zdyyeiv „ranzig
sein", zdyyog n., zayyg „ranziger Geruch‘‘ (von Fick BB. 3, 163 mit stinken
vb.)    auf ein idg. tong-            :   tdng- (oder foug-)     3
                                                                     ,ranz,   ubelriechend" zuriickgehn,
wozu allenfalls, doch sehr unsicher, germ. *stekja- in isl. sfcekr ,,stinkend",
stcekja „stinken",            norw. mdartl. si(Bk ,, bitter, ranzig",
```


## [2026-09-14T03:19:09.305Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '41090,41160p' incoming/WLD/WLD_Bd2_pages.txt"
}
```


### [2026-09-14T03:19:09.376Z] TOOL RESULT

```
diavoia Hes.,       ysgovra rvp^ov  Pedersen KZ. 39, 363; daS nach Meillet
                                         (s,

Msl. 9, 154, Pedersen aaO., zw. Persson IP. 35, 209 arm. fmbir „BetaU“
bung, betaubender Trank", fmbrel „obstupefieri“ aus nachststehendem ^hiynp-
erwachsen seien, ist nicht wahrscheinlich eher zu lat. temetum^ s. Charpen-
                                                         ;


tier IF. 25, 250 a 3) mit -bh- orvcpeXi^o} „sto6e, miBhandle", orv(psX6g, orvfpkog
                          ;


„rauh, fest, hart, grausam";
   lat. stiiprum „Schande, bes. die Entehrung durch alle Arten von Un-

zucht" (ursprgl. „die dafiir verhangte Priigelstrafe, Staupung oder Aus-
stoBung"); stupeOj ere „starr stehn (bes. von unbewegtem Wasser); betaubt,
betreten sein, stutzen", stupendus „erstaunlich, staunenswert"     mit                 ;



vielleicht titubc[>re „wankeln, straucheln, mit der Zunge anstoSen, stottern".
  Abg. hpati „palpitare",   t^p^t^ „strepitus“, t%p'htati „palpitare, calcare";
  lett.         „PferdefuBtapfen", staupains „ausgetretener Weg"; stupe,
           staupe
stups „Besenstumpf; das nachgebliebene Ende von etwas gebrochenem",
stupas pi. „Blutfedern, kleine Ruten".
  Ahd. stobaron „obstupere‘\
   Aisl. stiifr „Stumpf", norw. stuv „Baumstumpf, Stamm, Sterz", mnd. stUve
m. „Stumpf, Zengrest", adj. „stumpf, abgestutzt", stuven                       —
                                                                 aisl. sty fa „ab-
stumpfen, abhauen"; aisl. stofn „das untere Ende eines Stamm es, Grund-
lage": ags. stofn ds., aisl. stubbr^ stubbi m. „Stumpf, Baumstumpf", ags.
stybb n. „Baumstumpf';
   mit germ, -pp- (iig. pn^), nach langem Vokal -p-: mnd. stoppe, mhd.
stupfe, Demin, mnd. nl. (und durch Entlehnung nhd.) stoppel ,,Stoppel,
Stachel", ahd. sfupfila ds. (Siitterlin IF. 4, 103f); ahd. sttipf, siopfo^ stopfa
..kurzer Stich, Punkt, stimulus",              wovon ahd. stupfon, stupfen, nhd. stupfen,
tiipfen^ stilpfen, tilpfen „leicht beriihrend stofien, stacheln, antreiben" (versch.
von and. stuppon, mhd. nhd. stopfen aus mit. stiippare jjmit Werg stopfen";;
mnd. stupe „KrampfanfaH", mnd., mhd. (eig. md.) stupe, nhd. Staupe „Schand-
pfahl, woran Yerbrecher gebunden wurden, um mit Ruten gestrichen zu
werden", nhd. stdupen; aisl. stupa „steif emporstehn, in die Hohe ragen",
ags. stilpian, mnl, stuypen „sich vorn uberneigen" (aus „in die Hohe ragen");
ags. steap „hoch, ragend" (engl. steep „steil“), mhd. stouf „hochragender
Felsen" {Rohenstaufen), mhd. stief „steil"; aisl. staup n. „Yertiefung in
einem Wege";         ags. steap,       ahd.    mhd. stouf „Becher" (eher               eig.   „Stumpf,
Stutzen,    Stutzbecher"         als   „steil“),      nhd.    Stiefel    „Bierglas";
                                                                     stoppa                ags.
„Kubel, Eimer") wofur mhd. stubech^ stiibich „Fa6, ein best. MaB", holl.
      „Feuerkieke" die Entstehung von -pp- aus idg. -pn- stiitzt); aus „ab-
gestutzt = beraubt" erklart sich auch aisl. stjUp- „Stief-" {stjUpr „Stief-
sohn"), ags. steop-, ahd. sHof-, stiuf-, nhd. Stief-, ags. a-stiepan „berauben",
a-stieped „verwaist", ahd. ar-, bi-stiufan „der Eltern oder der Kinder be-
rauben"     (vgl. lat.   pnvignus:prlvus),
  Eine nas. Form (mit idg. 6?) aisl. norw. stumpa „sturzen, sich iiberbeugen"
(Yf. LEWb.2 7 gl g y titubo).
  Ygl. z. B. Pick IM45,            ni^ 496      f.,   Ehrismann PBrB. 18, 217 ff.             (ausfiihr-
lich libers Germ.),           Wood a ^ No. 576, Uhlenbeck Ai. Wb. 344, Falk-Torp
620                                               steu      (s)teg-



u. stif, stuh, stupe, st0p,               Vf. LEWb,^ u. stupa, stupeo, stuprum^ tituho, Boi-
sacq    u.    rvmco,

2.   steu- jjlaut preisen^.
     Ai, stauti, stavate usw.               „lobt,     preist*^,   Ptc.    stutd-h ,jgepriesen% stuti-h
„Lob,     Preis‘^,         stdfdr-    „Lobsanger“ usw.,            av. staolti „lobt,              preist,    besingt;
betet",      Ptc,      stiita-^      stuiti-^   staotar-    usw.,     erweitert         ai.        stobhati    j,preist,
```


## [2026-09-14T03:19:26.068Z] TOOL CALL #89: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/?q=tup&iencoding=iast&lang=en",
 "prompt": "What do Monier-Williams and other dictionaries give for the Sanskrit roots तुप् (tup), तुभ् (tubh) and तुज् (tuj)? Give the glosses (e.g. 'to hurt, injure', 'to push, urge, impel') and any cognates mentioned."
}
```


### [2026-09-14T03:19:27.232Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


## [2026-09-14T03:19:31.142Z] TOOL CALL #90: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A5%81%E0%A4%9C%E0%A5%8D",
 "prompt": "Sanskrit root तुज् (tuj): give the meanings and any Proto-Indo-European / Proto-Indo-Iranian root cited."
}
```


## [2026-09-14T03:19:31.693Z] TOOL CALL #91: WebSearch

```json
{
 "query": "Monier-Williams Sanskrit root \"tup\" \"tubh\" \"to hurt, injure\" topati tumpati"
}
```


### [2026-09-14T03:19:35.388Z] TOOL RESULT

```
# Sanskrit Root तुज् (tuj)

**Meanings:**
The root तुज् has three primary meanings:
1. "to strike, hit, push"
2. "to press out"
3. "to flow forth"

**Proto-Indo-European Origin:**
The entry cites the PIE root **(s)tewg-**, which means "to push, hit." This root is cognate with Proto-Germanic *stukkaz ("stump, stick"), which gave rise to English "stock."
```


### [2026-09-14T03:19:38.517Z] TOOL RESULT

```
Web search results for query: "Monier-Williams Sanskrit root "tup" "tubh" "to hurt, injure" topati tumpati"

Links: [{"title":"Tup: 7 definitions","url":"https://www.wisdomlib.org/definition/tup"},{"title":"Tump, Tuṃp: 6 definitions","url":"https://www.wisdomlib.org/definition/tump"},{"title":"Monier-Williams Sanskrit Dictionary 1872 Advanced","url":"https://www.sanskrit-lexicon.uni-koeln.de/scans/MW72Scan/2020/web/webtc2/index.php"},{"title":"Monier-Williams Sanskrit English Dictionary Page 0498","url":"http://www.ibiblio.org/sripedia/ebooks/mw/0400/mw__0498.html"},{"title":"A Sanskrit English Dictionary : Monier-williams, Monier, Sir : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/in.ernet.dli.2015.31959"},{"title":"Monier Williams - Sanskrit-English Dictionary 1872 | PDF","url":"https://www.scribd.com/document/321388649/Monier-Williams-Sanskrit-English-Dictionary-1872"},{"title":"Monier-Williams: A Sanskrit-English Dictionary (1872)","url":"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm"},{"title":"The Monier-Williams Sanskrit-English Dictionary | Learn Sanskrit Online","url":"https://learnsanskrit.org/monier/"},{"title":"A Sanskrit English Dictionary Sir Monier Monier Williams : Williams : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/nSrb_a-sanskrit-english-dictionary-sir-monier-monier-williams"},{"title":"Tump (disambiguation)","url":"https://en.wikipedia.org/wiki/Tump_(disambiguation)"}]

Based on the search results, I found information about the Sanskrit root from the Monier-Williams dictionary and related Sanskrit lexical sources:

The Sanskrit root tup has forms topati and tupati; tuph, tophati and tuphati; tump, tumpati and tumpati; tumph, tumphati and tumphati, meaning "to injure" or "to hurt" (from the Monier-Williams Sanskrit-English Dictionary).

The root is listed as class 1 and 6, with forms topati, tup, toph, tuph meaning "to hurt," and cognates include tubh, tump, as well as Greek τύπ-τ-ω and Latin stupeo.

The related root tuṃp has forms topati, tupati, and tumpati, meaning "to injure" or "to hurt".

The search results confirm that these roots and their conjugated forms (tumpati, topati, etc.) are documented in the Monier-Williams dictionary and other Cologne Digital Sanskrit Dictionaries as having the meaning of causing injury or hurt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T03:19:46.686Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n 1,25p tools/fetch_source.py"
}
```


### [2026-09-14T03:19:46.735Z] TOOL RESULT

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
```


## [2026-09-14T03:19:54.011Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://en.wiktionary.org/wiki/%D8%AA%D8%A8%D8%A7%D9%87' \\\n 'https://en.wiktionary.org/wiki/%D8%A7%D9%86%D8%AF%D9%88%D8%AE%D8%AA%D9%86' \\\n 'https://en.wiktionary.org/wiki/%D8%AA%D9%88%D9%BE' \\\n 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/top' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%82%E0%A4%AA' \\\n 'https://en.wiktionary.org/wiki/%E0%A4%A4%E0%A5%81%E0%A4%9C%E0%A5%8D' ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 482, roots Steu2/Stewe: Persian tabah, anduxtan, tup; Proto-Turkic top; Skt stupa, tuj\" 2>&1 | tail -1; done"
}
```


### [2026-09-14T03:19:56.976Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e13e47b8aa65294e.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f17dc41e111d40a3.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0d6e38bf134f09a0.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2171a83055c1bd22.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/70d90587937b504a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/c35c7cc329ef6c6f.txt
```


## [2026-09-14T03:20:00.497Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; for u in \\\n 'https://www.etymonline.com/word/stop' \\\n 'https://www.etymonline.com/word/stuff' \\\n 'https://www.etymonline.com/word/stucco' \\\n 'https://www.etymonline.com/word/study' \\\n 'https://www.wisdomlib.org/definition/tup' ; do\n python3 tools/fetch_source.py \"$u\" --note \"page 482: English stop/stuff/stucco/study from (s)teu-; Skt root tup\" 2>&1 | tail -1; done"
}
```


### [2026-09-14T03:20:03.271Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e43a8cbd38f1d664.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b4b9991cf65f7410.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9f5c2aa388559f45.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/baed8b2200804502.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/dfa9e5dc9f861ac4.txt
```


## [2026-09-14T03:20:07.541Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web; for f in e43a8cbd38f1d664 b4b9991cf65f7410 9f5c2aa388559f45 baed8b2200804502 dfa9e5dc9f861ac4 2171a83055c1bd22; do echo \"--- $f $(wc -c <$f.txt)\"; grep -o \"stuppa\\|stopfon\\|stukki\\|studere\\|to injure\\|round thing\" $f.txt | sort -u | head -4; done"
}
```


### [2026-09-14T03:20:08.616Z] TOOL RESULT

```
--- e43a8cbd38f1d664 9324
stopfon
stuppa
--- b4b9991cf65f7410 9314
stopfon
stuppa
--- 9f5c2aa388559f45 7416
stukki
--- baed8b2200804502 9276
studere
--- dfa9e5dc9f861ac4 7318
--- 2171a83055c1bd22 4645
round thing
```


## [2026-09-14T03:20:59.654Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i in (743,744,745):\n    L=leaves[i]\n    print('=== leaf',i,'===')\n    print(L[:1200])\n    print('...')\nEOF"
}
```


### [2026-09-14T03:21:00.874Z] TOOL RESULT

```
=== leaf 743 ===
چرمی کشتی گیرانرا خصوصا.
قئیك ه بنتح اول بر وزن ابجد. مستشضل
خاموش بودن ولرزیدن باشد ». نی میلرزد
وخاموش میگردد - و جنم الث بمعنی جسم کل
است همچنانکه روان بد نفی کل است چه تن
بممنی جسم و روآن بمعتی نفی و بد بمعنی همه
و بازیگران در زیر بغل گرفته بنوازند؟ -
و چناغ زین اسب - و دامنة زین را یز گویند,
و باین دو مه‌ثی بقتح اول‌همامده است » وبجای
حرف اول طای حطی هم درست است - و با بای
فارسی دریچُ زرگری و قاری باشد » و آن
فالبی است که چیزها از طلا ونقره و امثال آن
و کل باشدا .
لنیسه ‏ بر وزن مدرسه؛ قالی را گویند
خواه کرمانی و خواه جوشقانی » وحعرب آن
طنضه است
تنبك بشم اول بر وزن اردك باانگشت
ایهام وسبابه ووسطی گرفتن چیزی‌خوردنی‌باشد »
بعنی بسر انکشت چیزی برداشتن و خوردن -
و دهلی باشد دم دراز که ازچوب و سفال ساز ند
درآن ریزند ۴ , وباین معنی بتقدیم بای فارسی
برنون هم آمده‌است» و بعضی دریچهٌ زین امپ -
وطاف زین را دم نز گفته‌اند ۳.
قنبل » بر وزن صندل . کال و بیکار
وهیجکار6 - ومسخرء را گوبند - و چنم اول .
بر وزن بلبل , حیله و نیرنگه ومکر و فریب
وجادومی بودا" ؛ و باین معنی بروزن فر کل هم
آمده است که بضم ثالث باشد .
۴ ظ , حمحف نك (ع. م).
تبنك را چ و کر لهی بی‌شك ربخته کر برآبد از تبك.»
ودرحاشه أزنخه ن: «تبتك دریچه‌لی بود که شالب اژو ربخته‌ها کنند از هرصورت * »
وازنسخةج:تنبك( کذا)دریچه وقالب ومر کب
...
=== leaf 744 ===
تنیلیت۱ عبا تای فرشت درآخر بر وزن
عندلیب , بارکوچکی را گویند که بربار بز رکه
بندند و گاه بربالای چاروا نهند و بر بالای آن
موار شوند - ویك لنکه بار را نیز کنته‌اند.
لثبوو » بر وزن زنبور ۰ سازست
مشهور , و ععرب‌ان طنبور ۴
تنبو لك بر وزنمقلو 2
بععث ی کیاده باشد ء و آن کمالی
است‌بسیار کم زور و بمعنی
جناغ زین هم آمده است که
دامنزین وتسمهرکاب باشد ؟-
و طاق زین را یز کوبند ۴ .
تتبول «بروزن مقبول
برگی باشد که دره‌ندوستان‌پان
کویند وبا هك وفوفل خور ند
و کیاده را ی زگوند . و آن
کمالی باشد کم زور 6 وفام
قلمه‌است درهندومتان . تنبور (طنبور)
آنیه س بر وزن انبه » چوبی کنده
وبزر گه باشپ که در پس در نهند تا در کشوده
نگردد .
لنسدن بروزن‌خندیدن» بمعنی‌لرژیدن
ات
و طییدن و حر کت کردن باشد - و بمعنی کمین
کردن هم حست .
تنبياگ سب بشم اول وسکون ثانی‌وکاف ؛
بىمنی تتبك است و آن دهلی باشد دم دار که
مسر ؟ان‌وبازمگران درزیر بغل گیرند ولواز نش
وجناغ زین اسبرا نیز گوبند٩‏ * و با بای‌فلرسی
مده است .
ناگ ه با نای فرشت بر وزن غناقد .
نم پادشاهی بوده است - و نام مردی هم‌هست.
تنته ۷ < بفتح اول و فوقانی و سکون
تالی» تنیده و پرد؛ عنکبوت راگونتد وضم‌اول
و فتح ثالث زلبورسرخ باشد .
قنج۸ ه بفتم اول بر وزن رنج » سنعنی
درهم پیچیدن و فراهم فشردن باشد - و بمعنی
از پی درآمدن و فراهم نشاندن هم هست. و هر
فاعل را نیز گویند که بحسنده
...
=== leaf 745 ===
زند ۱ - چم اول و سکون انی و دال
سوق نت کا مرلین مامت ردر چم
که از جای برجهد و جهنده باشد . و خشم -
و خشمکین و نحنبناگ ودرشت - وتواناء و قربهرا
نیز گویند. وبمعنی غرل ییابالی ودبو هم هست-
وس رکوه را نیز گفته‌اند - و بمعنی بلند وبلندی
‌م آمده است.
تنل بار آه تند معلوم بابای ابجد بالف
کلبده و برای قرشت زده » موذباث را کوشد
مانتد شیر و پلنگه و مار و عقرب و زنبور
- ومورچه وامثال آن- وهرجانوری که جانوردبگررا
شورد.
ند بود - بنم بای ابجد و سکون
واو مجهول و رای فرشت » جستن و برجتن رآ
گونند» و باین معنی بجای بای ابجد بای حطی
اههد سح
تنلیر 5 عه بضم اول وفتح ثالك وسکون
۱ -اوستا ۷2۵۸ ه (ه . 2)۷29۵6) ,از ربشة 4۵۷, فس: توان (تواستن) «اسفة
۵ هرب انرابطةٌ *نند»رابا «نوان» ممتقدنیست «هوبشمان ۳۹۵ اورامانی00) «ل . اورامان
۷ سننانی 00 ۰ منکری و سرخه و لاسکردی 10۳0 , شهمیرزادی لا « ۵ . ۲
ص۱۹۹ .گیلکی ۱94 . ۴ فرهنگ دساتیر ۷4۰ .
۴ - قس: ریش هشدی‌باستان 20], 180201 ( صدا پیجیدن , صدا: صدادادن ).
5 (رعد) ,لاینی ۱۵۵2۲6 , کلاتاذ00), انگلیسی 410846۲ «اسشق ٩۳۹۲‏ , اففانی
متداول 12002۲ ,اففانی محض 1812 (رعد) «هوبشان ۰۳۹۰ :
عالی و رای قرشت » ممعنی خرنده باشد هموعاً -
و رعد را گویند خصوصا " و نم ثالث هم آهده
است - و بلبل را ی زگوبندکه عربان عتدليب
خوانند ۴ ۰
لین در دادن عم کنابه از راضی شدن
وقبول کردن باشد . 3
لنفد 
...
```


## [2026-09-14T03:21:09.506Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nfor i,L in enumerate(leaves):\n    if 'توپ زدن' in L or 'توپ‌زدن' in L:\n        print('leaf',i)\n        print(L[:1500])\n        break\nEOF"
}
```


### [2026-09-14T03:21:10.611Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T03:21:13.710Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; python3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\nleaves=t.split('\\f')\nhits=[i for i,L in enumerate(leaves) if 'توپ' in L]\nprint(hits)\nfor i in hits[-3:]:\n    print('=== leaf',i,'===')\n    print(leaves[i][:1800])\nEOF"
}
```


### [2026-09-14T03:21:14.656Z] TOOL RESULT

```
[110, 138, 574, 754, 755]
=== leaf 574 ===
داریلب ْ ۱ 4 ۲و
بمعنی جزئی باشد که دربرابر کنی استوپاز تاربان
بمعنی جزئیات؟ .
یازج با زای فارسی بر وزن‌آز رخ
تممنی مالش وان باشد۷ .
پارش بکرزای‌هوزبروزن خواهشی»
کیاه و علف ژبادتی را از مان غله زار کندن
ودور افکندن باشد» همحئانکه براش شاخهای
زیادتی درخت را بربدن‌است
پادن * بر وزن
0 .بز کوهی را گونند ۱
پار اهه- با زای
فارسی‌بروزن کارنامه »بمعنی
پاچ له ات که لقب -
وفرین و حمال باشده .
محبوب شوخ و شنگه را کوبند .
با ه بر وزن فارباب » زراعتی را
گویند که با آب رودخانه و اشال آن مزروع
بار او » باوا بممنی پازباب است که
زراعت ما آب رودخانه و کاریز مزروع شده
شود
باشد .
پار یفن - بی وزن‌خاریدن » بمعنی
پرواز کردن باشد .
بار بنکون‌زای‌نقطه‌دار: بمعنی‌بیفش-
و نازك و لطیف باشد۴ .
اد ه بکون زای فارسی, نام دهی‌است
از پلو کات طوس؟
باراچ- با زای هوز و جبم فارسی بروزن
تاراج » دایةٌ شیر دهنده و عاماچه را کوب »
وبعربی قابله ومر‌شمه خوانند ۵.
بار تادری س باتای‌فرشت بروذن! میاری:
پار ند" بروزن
بایند. تفسیر زندباشد وزند پازن
٩‏ -ویز «شهربت از کوز کانان» برشاهراه‌کاروان وبیار نعمت».«حدودالمالم» معرب‌آن
فاریاب . لک متفر ۴ - در دساتیر آهده « فرهنگ دساتیر ۲۳۷ »
وشاهدی بافته سل .. ۴ - معرب آن‌فاژ.  *‏ ویازاح 1
بنازه مادر ابلم طفل بخت‌ترا زر میکند اندر کنارچون یازاج. متصور غیرازی. *لفت‌نامه.
۱ - ساختة دسائیر«فاب4۷:۱» اکن دساتبر ص۲۳۷ «پازنازی» وجمعآن ذپازتازبان» آمده.
پاسار میکند من وخوبان را: تنك آمدم زیاژخ وپاسارش. ناصرخرو. «لفت نامه*.
۸ - ویاژن. بهلوی 0261۳8 «اسشق۲ ۰6۷۷ 02080 «اوتوالا ۰۰۵٩٩‏ ۳۵810 (یزنر) "
«اسشق ۰۲۷۲ . ٩‏ - ره : پاچ نامه و پاش نامه.
*- مرکب از: یا زند؛ جزو اول از اوسنابی 0661 بمنی ضد وصاحب هردو است .
جزودوم از کلمهٌ 8۷2041 اوستابی مشتق است ودرارمنی بمعنی شرح وبیان و کزارش | ست (رك :
زند) پی اصل این کلمه در اوسئا باید 222101 0210 باشد و آن اصطلاحا عارنت از زبان
پهلوی بدون لفات هزوارش ۰ بديهي است که‌شات این‌زبان پسازجملةٌ تازبان وشابد درفرنهای‌دوم
وسوم حجری صورت گرفته » بدبنطریق که آ
=== leaf 754 ===
ی ت یخن نازكك و کباب
هم‌آمده است .
تواهی ه بر وزن و ممنی تباهی
ات که نابود کرده شده و خابع گردیده وبکمال
نرسیده باشد ۰
توان نم اول پروزن جوان . قوت
وقدرث رتوالایی باشدا - و بمعنی ابر هم هست
که بمریی‌سحاب گویند- وممکن بودن هرچیزرا
یز کنته‌اند؟ .۶
وافچه؟ - بروزن ومعنی‌یانچه‌است
که بعربی لطمه گوبند .# قها۷ » بنم اول و بای فرسی بالف
تو اهه - بفتح اول وهای هوز » قليةٌ | کشیده . بلفت زند و پازند(۱) سیب را گویند
بادنجان را کوبند - و کوکو ۴ وخاکینهرا نیز . | وجربی تفاح خوانند .
- اوستا - 1۵۷ ۵ ( توانستن , قدرت داشتن ) ۰ 62] 2۷2 » پهلوی ۷28 ,
هندی باستان -52۵۷, 12۷141.ارمنی 46۷617 (ماندن» دوام کردن . تحمل کردن» استقامت -
داشتن) «اسشق 4*۱* «نبر ٩۷۲۸۵‏ .«مسینا ۱4۹ :۰0۲ ۴ -بمعنی اخیردر دساتیر آهده
۱۳ ۴ -لفتی است‌در: تیانچه (عم) . ۴ .ره :ک وکنك وکوکو .
۵ رك: تباهی . ۱ -مز» ۵02 20۳2), پهلوی 96۷»,سب «یونکی ۱۱۸.
۵ قوافا -لفةبشم‌اول (درتداول امروز بفتح),از: نوان ۱-۲ (پسوند فاعلی باصفت مشبهه)؛
قادر, کسیکه ازعهد؛ انجام کاربرآ ید زورمند, نیرومند:
مبازوان توانا و فوت سردست خطاست ینجهٌ مسکین ناتوان بشکست .
کلتان ۲۹*.
۵ قوالستن -لفةیض‌اول (در نداول امروز بفتح) وکسر چیارم (در لهِجدُ مرکزی)؛ از :
توان ۲+ ستن (پسوند مسدری)؛ پهلوی ۷۵0)1(50217) «اسشق 4۰۱ [رك: توان] ؛قدرت‌داشتن
مقثدر بودن .
توالنگر لغب اول (درتداول امروز بفتح) وفتح پنجم, جهلوی ۱۷20-127 «اونوالا
۵ «منا ٩۲:۱4‏ ؛ ترونمند» مالدار» غنی؛
کر کنن خاه مهد نز کی نشناسد توانگر از دروش.«گلتان ۵۱*.
۵ توانگری -لفتنم اول(درتداول امروز بفتح) وفتح پنجم , پهلوی 0۷۵-18:110)
«ب رکه ۰۲۲۸ « اونوالا ۰۵۳٩‏ مالداری» روت .
۵ قوپ _ازتر کی, سلاحیاستآتشین
دارای لوله‌ای بزر که از آهن بامفرغ که برروی
چرخ حمل‌شود- بك‌بته ازقماش‌وجز آن- توپ
زدن » توپ الداختن- در اصطلاح فمار . بروی
دست حرف برخاستن درصورنیکه دست خود
پت‌تر ازدست حربف‌باشد. «ناظم‌الاطباه» -نوپ توب
و ثشر زدن » سختان درشت و سخت بک یگفتن .
۵ توب‌جی -ازن رکی, لشکری که بانوپ کار کند , که‌سلاحش توپ است
=== leaf 755 ===
صوا داد نت
تو بال . و توپال۱ , لفت اول با بای
ابجد ودیگری با بای فارسی بروزن دومال ‏ ,
بععنی مس باشد که بعربی‌نحای کویند - وبراده
وسوش مس ونقزه و امثالآنرا نیز گفته‌اند -
وبعضی گویند مس و! هن وامثالآ نرا چون بتابند
ودچکوش وبتك برآن زنند ریزهایی که از آن
میریزد ومیپ‌شدآنهارا توبال میگویند » و این
اسح است چه توبال النحاس ریزه‌هابی را گویند
که بوفت چکوش زدن ازمی‌افنه میپاشد وآنرا
پوست مس‌میکوبندوآن لیف نو از حس‌سوخته
است ۰ وهمحنین نو بالالحدید | نجه ازآهن تفته
ریزد گویند. | کرتوبال وبراده‌آهن بر کسی‌ندند
که درخواب دندان بدندان بساید و بکراجد(۱)
دیگرآن فعل :کند » و اکر از آن قدری
در شراب بزهر آمیخته وبزند زهر را بخود
در (۲) کشد . واکر آن شرابرا بخورند زبان
نکند؟ .
و باهلن(۳) ۰ نم میم ولام و سکون
نون » بلغت بونانی فوعی از متوعاست(4) وآنرا
بمربی علفی خوانند » بر که آن مانند ب رکه
کبر باشد وچون شاخی از آن بثکتندشیر بسیاری
ازآن روان شود .
توبان؟ بروزن خوبان» تنبان‌چرمی
که کشت ی کیران پوشند ۴ :
)۱ خم۳: بکرچد.رك: کراجبدن.
(4) چش: تیوعاست. ر4ٌ: بوغ.
تو بر لو - با واز مجهول بروزن مو
برمو ۰ بمعنی لابرلا و نه برته باشد- و بمعنی‌هی
دریی ودنبال بکدیگر نیز بنظر آمده است -
و لام حلوابی هم هت - وعزار خانة گوسفند را
نیز گویند - ومردم سر درخود وحرام توشه با
(ه) هم میگفته‌اند ۹
و بژه ع با ثانی مجهول و فتح
زای هوز بروزن موصده ؛ بیخ صنق خربزه را
بند .
تو بك - و قو شالت اول با بای ابجد
ودویم با بای فارسی» حم اول بر وزن خوبك .»
بمعل ی کنجینه ومخزن باشد * و بفتم اول ند-ز
بایتمعنی گفته‌اند , و بهمین معنی بجای پای‌ابجد
تای فرشت و نون و بای حطی هر سه آمده
است :
تو بکی حه بسکون بای ابجد و باکاف
بر وزن تویچی ؛ نام درمی‌است که در قديم زده
بودند و رایج بوده ۵ .
و به - بنم اول و سکون ثالی و فتح
بای ابجد » قوی قزح راگویند » و باين معنی
بجای بای ابجد بای حطی هم آهده است .
توت" « نم املوسکون ثالی‌وفوفانی,
میوه ابست ممروف . سفیدآن فایم مقلم انجیر
(۷) خم۳: -در. (۳) خم۳: توباملون.
۳ سرك: لك[ : ۰.6
۴ -بارم خبرر
```


## [2026-09-14T03:21:24.456Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"tebäh\\|tebah\\|tabäh\\|tebâh\" HRN.txt | head; echo \"--- HUB ---\"; grep -n \"tabâh\\|tebâh\\|tebah\" HUB.txt | head; echo \"--- ARY تباه/توپ/اندوختن ---\"; grep -n \"تباه\\|اندوخت\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-14T03:21:24.548Z] TOOL RESULT

```
--- HUB ---
--- ARY تباه/توپ/اندوختن ---
9364:کردی (0/5[4): ,لش ,نآق2۸ سلتی (کلنی) (81.7/6): تباهع
```


## [2026-09-14T03:21:31.932Z] TOOL CALL #100: WebFetch

```json
{
 "url": "https://abadis.ir/fatofa/%D8%AA%D8%A8%D8%A7%D9%87/",
 "prompt": "What does the فرهنگ معین (Mo'in) section say for تباه — give the origin tag in brackets (e.g. [په.] Pahlavi) and the definition. Also any Dehkhoda etymology."
}
```


### [2026-09-14T03:21:37.872Z] TOOL RESULT

```
# تباه — Mo'in Dictionary Entry

**فرهنگ معین (Mo'in):**
"(تَ ) \[ په . \] (ص . ) فاسد، ضایع"

The origin tag is **[په.]** (Pahlavi), and the definition means "corrupt, wasted."

**Dehkhoda Etymology:**
The Dehkhoda section traces تباه to Pahlavi **tapāh**, noting it functions as an adjective that can combine with verbal forms. It's defined as something that has become corrupted, lost its proper state, or been destroyed—encompassing meanings from "ruined" to "destroyed" to "futile."
```


## [2026-09-14T03:21:40.800Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 tools/fetch_source.py 'https://abadis.ir/fatofa/%D8%AA%D8%A8%D8%A7%D9%87/' --note \"page 482, entry 0 node 2: Mo'in and Dehkhoda on تباه (Pahlavi tapāh)\" 2>&1 | tail -1"
}
```


### [2026-09-14T03:21:43.040Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e71fc61bef1e29a3.txt
```


## [2026-09-14T03:22:12.160Z] AGENT

Now I'll write the verification file.


## [2026-09-14T03:29:39.591Z] TOOL CALL #102: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-482.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n \"pdf_page\": 482,\n \"book_page\": 452,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-13\",\n \"entries\": []\n}\n\n# ---------------------------------------------------------------- entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Steu 2, Teu 2, Teup\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *(s)teu- 'to push, stick, knock, beat' (Pokorny IEW 1032-1034), with the conservative extensions *(s)teu-k-, *(s)teu-g-, *(s)teu-d-, *(s)teu-p-\",\n \"note\": (\"Pokorny 1032-1034 heads the entry '(s)teu-1, Meaning: to push, hit; Note: with conservative extensions' \"\n          \"and covers there the k-, g-, d- and p-extensions; at p. 1079 he prints 'teu-1, teud-, teug-, teuk-, teup- \"\n          \"-- see above S. 1032 ff. under (s)teu-', which is exactly why Nourai's headword lumps Steu, Teu and Teup together. \"\n          \"The numbers in the headword are Nourai's own entry-numbering, not Pokorny's: Pokorny's steu-2 is 'to praise' (1035), \"\n          \"his teu-2 'to listen to, observe' (1079-1080) and his separate teup- 'to get down, conceal oneself' (1085) are different roots. \"\n          \"Language label ('Indo-European') and gloss ('to push, beat, hit') are correct; the added 'also throw' is Nourai's own extension \"\n          \"drawn from the Sanskrit tuj branch (Skt. tuj- 'to impel, drive, set in motion'). Walde-Pokorny II 615-620 and Watkins/AHD \"\n          \"s.v. (s)teu- give the same root. The Avestan/Persian branch hung under it (nodes 1-2, tabah) does not belong here.\"),\n \"note_fa\": (\"ریشهٔ هندواروپایی آغازین *(s)teu- «راندن، زدن، کوفتن» است که پوکورنی در «واژه‌نامهٔ ریشه‌شناختی هندواروپایی» صفحه‌های ۱۰۳۲ تا ۱۰۳۴ \"\n             \"با گسترده‌های *(s)teu-k-، *(s)teu-g-، *(s)teu-d- و *(s)teu-p- آورده است؛ در صفحهٔ ۱۰۷۹ نیز teu-, teud-, teug-, teuk-, teup \"\n             \"را تنها ارجاع به همان مدخل دانسته، و همین سبب شده که نورایی هر سه صورت را در یک سرواژه گرد آورد. شماره‌های «۲» در Steu 2 و Teu 2 \"\n             \"از شماره‌گذاری خود نورایی است نه پوکورنی. والده-پوکورنی (جلد ۲، ص ۶۱۵–۶۲۰) و واتکینز (پیوست ریشه‌های هندواروپایی فرهنگ American Heritage) \"\n             \"نیز همین ریشه و همین معنا را می‌آورند. ادعای نورایی دربارهٔ خودِ ریشه درست است؛ تنها افزودهٔ «also throw» برداشت خود اوست.\"),\n \"sources\": [\"https://www.etymonline.com/word/study\"],\n \"ref_check\": [\n   {\"ref\": \"POK:1032\", \"status\": \"supports\",\n    \"note\": (\"POK_full.txt line 82766 ff.: 'Root / lemma: (s)teu-1 / Meaning: to push, hit / Note: with conservative extensions ... \"\n             \"References: WP. II 615 ff., WH. II 608 ff. / Page(s): 1032-1034' -- exactly Nourai's root, language and gloss \"\n             \"(grep -n 'lemma: (s)teu' POK_full.txt).\")}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Bd. II 615-620 (WLD_Bd2_pages.txt ll. 40960-41160)\", \"stance\": \"supports\",\n    \"note\": \"Walde-Pokorny run the same family: '(s)teu-d-' at l. 41027, the p-extension with 'lat. stuprum ... stupeo, ere \\\"starr stehn ... betaubt, betreten sein\\\"', 'ags. steap \\\"hoch, ragend\\\" (engl. steep \\\"steil\\\")', 'aisl. stubbr, stubbi m. \\\"Stumpf\\\"'; the running head of l. 41154 reads '620  steu  (s)teg-'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)teu- (AHD_watkins1985.txt l. 1024-1026)\", \"stance\": \"supports\",\n    \"note\": \"'(s)teu-. To push, stick, knock, beat; with derivatives referring to projecting objects, fragments ... [Pok. 1. (s)teu- 1032.]'\"},\n   {\"src\": \"IEC\", \"where\": \"steud-, steug- (IEC.txt ll. 17219-17220)\", \"stance\": \"partial\",\n    \"note\": \"Mann has 'steud- (stud-, sth-) \\\"press, push\\\". ... WP II, 618' but splits the family into many separate lemmas (steug- there is 'bend, curve, twist').\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Avestan\", \"words\": \"tap 1\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Bartholomae's Altiranisches Woerterbuch knows only ONE Avestan root tap-, and it means 'to be hot': \"\n   \"'j. tap- V. \\\"heiss sein\\\", Praes. tapa-, (Inkoh.) tafsa-, (Kaus.) tapaya-, PPfP. tapta-' (AirWb col. ~638, BRT.txt l. 11912), \"\n   \"with the nominal tafnah- 'Hitze, Glut; Fieberhitze' (l. 11926). Cheung, Etymological Dictionary of the Iranian Verb (2007) p. 379 \"\n   \"likewise has only '*tap \\\"to warm up, heat\\\": YAv. tap- \\\"to be(come) hot\\\", caus. tapaiieiti; BMP t'p- /tab-/ \\\"to heat, burn; shine\\\"; \"\n   \"Pth. t'b-; Khot. ttav-', which continues PIE *tep- 'to be warm' (Pok. 1069), NOT *(s)teu- 'to push'. \"\n   \"There is no Avestan tap- 'to hit, hurt, destroy'; Nourai has read that gloss back out of Tavoosi's Shayast ne Shayast glossary (SNS), \"\n   \"whose entry for tabah cites a root tup-/tap- beside Skt. tubh, tub, tuph. The destructive sense is real but reaches Persian by the \"\n   \"heat root (Skt. tapati 'burns, torments', tapa- 'heat; torment'), not by the push root.\"),\n \"derivation_fa\": (\"در «فرهنگ ایرانی باستان» بارتولومه تنها یک ریشهٔ اوستایی tap- ثبت شده است به معنی «گرم بودن/شدن» (tafsa- ستاک آغازی، \"\n   \"tapaya- سببی، tapta- صفت مفعولی) و مشتق tafnah- «گرما، تب». چونگ نیز در «فرهنگ ریشه‌شناختی فعل ایرانی» (۲۰۰۷، ص ۳۷۹) همین ریشه \"\n   \"*tap «گرم کردن» را می‌آورد که دنبالهٔ ریشهٔ هندواروپایی *tep- «گرم بودن» است، نه *(s)teu- «راندن، زدن». ریشهٔ اوستاییِ tap- به معنی \"\n   \"«زدن و نابود کردن» در هیچ منبعی نیست؛ نورایی این معنا را از واژه‌نامهٔ «شایست ناشایست» طاووسی گرفته که در مدخل «تباه» ریشهٔ tup-/tap- \"\n   \"و سنسکریت tubh, tub, tuph را یاد کرده است. معنای ویرانگری از همان ریشهٔ «گرما» می‌آید (سنسکریت tapati «می‌سوزاند، شکنجه می‌دهد»). \"\n   \"پژوهش امروزی این پیوند را رد می‌کند.\"),\n \"sources\": [W + \"%D8%AA%D8%A8%D8%A7%D9%87\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:147\", \"status\": \"partial\",\n    \"note\": (\"SNS.txt l. 9409-9410 (glossary entry for tabah, keyed to text page/line 147/13 -- cf. the word index at l. 31265 'tabah 147/13'): \"\n             \"the OCR reads '...tabah:' followed by 'tubh, tub, tuph, /tup-/tap-'. Tavoosi therefore does give Nourai's Sanskrit forms and a \"\n             \"root tup-/tap-, but the entry is about Persian tabah, not about an independent Avestan verb tap- 'to strike'; and the OCR of this \"\n             \"book is poor (refs_online.json: 'Persian text mostly garbage, Latin transliterations partially readable').\")}\n ],\n \"consulted\": [\n   {\"src\": \"BRT\", \"where\": \"AirWb s.v. tap- (BRT.txt l. 11912; tafnah- l. 11926)\", \"stance\": \"contradicts\",\n    \"note\": \"'j. tap- V. \\\"heiss sein\\\", Praes. 4b(Kaus.) tapa-, 14 (Inkoh.) tafsa-, 30 (Kaus.) tapaya: ~ PPfP. tapta-' -- the only Avestan tap-, and it means 'to be hot'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 379, s.v. *tap (CHEUNG.txt l. 24669 ff.)\", \"stance\": \"contradicts\",\n    \"note\": \"'*tap \\\"to warm up, heat\\\" -- AVESTAN: YAv. tap- \\\"to be(come) hot\\\" ... PARTHIAN t'b- \\\"to shine, burn\\\"'. Cheung's other *tap (l. 3298) is in fact *cap 'to seize, strike' (Khot. cev-, NP capidan), not an Avestan tap-.\"},\n   {\"src\": \"POK\", \"where\": \"(s)teu-1, POK_full.txt ll. 82766-82890\", \"stance\": \"silent\",\n    \"note\": \"Pokorny's whole (s)teu- article cites no Iranian/Avestan form at all; the Indo-Iranian material is Sanskrit only (tudati, tujati, tupati).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"tabâh\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"The word itself is impeccable: MacKenzie CPD has 'tabah [tp'h | N ~] ruined, spoilt, destroyed' and 'tabahihistan' \"\n   \"(PHD_mackenzie.txt l. 4868-4870), Nyberg's Pahlavi glossary 'Paz. tawah; NP tabah' (NYB_vol2_glossary.txt l. 3728), and NP \"\n   \"تباه with the contracted doublet تبه (the Ferdowsi line quoted in the chart uses تبه for the metre). Middle Persian intervocalic \"\n   \"-p- was voiced to -b- (tapah > tabah), whence NP tabah/tabahi. What is wrong is the parentage: modern etymologies attach it to \"\n   \"Proto-Iranian *tap- 'to be(come) hot' (PIE *tep-), with the semantic path 'burn' > 'torment' > 'ruin' -- so Wiktionary \"\n   \"('From Middle Persian tp'h /tabah/, from Proto-Iranian *tap-, possibly from PIE *tep- \\\"to be warm\\\"; compare Sanskrit tapa- \"\n   \"\\\"heat; torment\\\"'), and Mo'in/Dehkhoda simply tag it Pahlavi tapah. Nourai's derivation from *(s)teu- 'to push' has no support. \"\n   \"The chart's own NOTE is accurate as a citation -- Mann, IEC 1365, really does print 'tabh- (?) \\\"rot, corruption, stench\\\": \"\n   \"Per. tabah, s. \\\"corruption\\\"; ... Lat. tabes ... cf. tabeo, ere, v. \\\"to rot\\\"' -- but that is Mann's idiosyncratic lemma \"\n   \"(Latin tabes belongs to PIE *teh2- 'to melt'), and it is not followed by Iranists either. Of the two, the *tap- 'heat/torment' \"\n   \"route is the one modern scholarship takes.\"),\n \"derivation_fa\": (\"خودِ واژه بی‌گمان است: «تباه» از فارسی میانهٔ tabah (نوشتهٔ tp'h) «ویران، تباه‌شده» است (مکنزی، «فرهنگ کوچک پهلوی»)، \"\n   \"و نیبرگ نیز پازند tawah و فارسی نو tabah را ثبت کرده؛ پِ ایرانی باستان میان دو واکه در فارسی میانه به ب نرم شده (tapah > tabah). \"\n   \"گونهٔ کوتاه‌شدهٔ «تبه» در بیت فردوسیِ همین صفحه به کار رفته است. آنچه نادرست است پدرِ این واژه است: ریشه‌شناسی امروزی آن را به \"\n   \"ایرانی آغازین *tap- «گرم شدن» (هندواروپایی *tep-) می‌بندد و تحول معنایی «سوختن ← شکنجه ← ویرانی» را در نظر می‌گیرد (قس سنسکریت \"\n   \"tapa- «گرما؛ رنج»)؛ معین تنها نشانهٔ [په.] می‌گذارد و دهخدا صورت پهلوی tapah را می‌آورد. یادداشت خودِ نمودار هم درست نقل شده است: \"\n   \"مان در صفحهٔ ۱۳۶۵ واقعاً «tabh- «پوسیدن»» را با لاتینی tabes کنار هم نهاده، ولی این نظر شخصی اوست و پذیرفته نیست. \"\n   \"بنابراین پژوهش امروزی ادعای نورایی را رد می‌کند و به جای آن ریشهٔ *tap- «گرما» را می‌گذارد.\"),\n \"sources\": [W + \"%D8%AA%D8%A8%D8%A7%D9%87\", \"https://abadis.ir/fatofa/%D8%AA%D8%A8%D8%A7%D9%87/\"],\n \"ref_check\": [\n   {\"ref\": \"SNS:147\", \"status\": \"partial\",\n    \"note\": \"SNS.txt l. 9409: the Shayast ne Shayast glossary entry 'tabah' (text ref. 147/13) cites Skt. 'tubh, tub, tuph' and a root 'tup-/tap-'. It is Nourai's source, but it is one 1986 Iranian glossary, and it does not connect the word to PIE *(s)teu-.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 81 s.v. tabah (PHD_mackenzie.txt l. 4868)\", \"stance\": \"partial\",\n    \"note\": \"'tabAh [tp)h | N -] ruined, spoilt, destroyed'; 'tabAhihistan, tabahih- [tp)hyh-stn'] be ruined' -- confirms the Middle Persian ancestor, gives no root.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II (NYB_vol2_glossary.txt l. 3728)\", \"stance\": \"partial\",\n    \"note\": \"'...to be spoiled 81**. -- Paz. tawah; NP tabah' -- the Pazand/NP equation, no Indo-European root.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD col. 1365 (IEC.txt l. 18183-18184)\", \"stance\": \"contradicts\",\n    \"note\": \"'tabh- (?) \\\"rot, corruption, stench\\\": Per. tabah, s. \\\"corruption\\\"; tabah, adj. \\\"corrupt\\\"; Lat. tabes ... ON pefa \\\"smel\\\". (WP untenable). (Cf. WP I, 701)' -- i.e. exactly the alternative the chart's NOTE reports, and a different root from Nourai's.\"},\n   {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in via abadis.ir s.v. تباه\", \"stance\": \"partial\",\n    \"note\": \"'(تَ) [ په. ] (ص.) فاسد، ضایع' -- Mo'in marks it simply as Pahlavi; the Dehkhoda section of the same page gives Pahlavi tapah.\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss (HRN.txt, grep 'tabah/tebah')\", \"stance\": \"silent\",\n    \"note\": \"no entry for tabah in Horn's Grundriss; Huebschmann's Persische Studien is likewise silent (grep returned nothing).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"tup, tub\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Pokorny's section 'D. (s)teu-p- (gelegentlich -b-, -bh-) \\\"bump, poke\\\"; also \\\"stick, stump\\\"' opens with \"\n   \"'Old Indic pra-stumpati, topati, tupati, tumpati, tumpati \\\"stoesst\\\", tupara- \\\"unhorned\\\"' (POK 1032-1034). Monier-Williams \"\n   \"lists the roots tup (topati/tupati), tuph, tump, tumph, all glossed 'to injure, hurt', with tubh as a byform -- exactly Nourai's \"\n   \"'tup, tub: to hurt, destroy'. The b-/bh- variants are Pokorny's own parenthesis, so 'tub' is not a misprint. The Greek cognates \"\n   \"tupto 'I strike' and tupos 'a blow, mould' and Latin stupere belong to the same zero-grade *tup-.\"),\n \"derivation_fa\": (\"پوکورنی در بخش D گسترده‌ای *(s)teu-p- (و گاه با -b- و -bh-) می‌آورد و نخستین گواه آن سنسکریت topati, tupati, tumpati \"\n   \"«می‌کوبد، می‌زند» است (صص ۱۰۳۲–۱۰۳۴). مونیه-ویلیامز نیز ریشه‌های tup (topati/tupati)، tuph، tump و tumph را «آسیب رساندن، زدن» \"\n   \"معنی کرده و tubh را گونهٔ آن آورده است؛ پس «tub» در کتاب نورایی غلط چاپی نیست بلکه همان گونهٔ با -b- است که پوکورنی در پرانتز \"\n   \"یاد کرده. هم‌ریشه‌های یونانی tuptō «می‌زنم» و tupos «ضربه، قالب» و لاتینی stupēre هم از همین صورت کاهیدهٔ *tup- اند. \"\n   \"ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.wisdomlib.org/definition/tup\"],\n \"ref_check\": [\n   {\"ref\": \"POK:1034\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt (lemma (s)teu-1, Page(s) 1032-1034), section D: 'D. (s)teu-p- (occasionally -b-, -bh-) \\\"bump, poke\\\"; also \\\"stick, stump\\\". Old Indic pra-stumpati, topati, tupati, tumpati, tumpati \\\"stoesst\\\", tupara- \\\"unhorned\\\"'.\"},\n   {\"ref\": \"SNS:147\", \"status\": \"partial\",\n    \"note\": \"SNS.txt l. 9410 does list 'tubh, tub, tuph' at the tabah entry -- the forms are there, but as an etymology of Persian tabah, which is a different claim.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 619-620 (WLD_Bd2_pages.txt ll. 41090-41154)\", \"stance\": \"supports\",\n    \"note\": \"the p-extension section with 'gr. stuphelizo \\\"stosse, misshandle\\\" ... lat. stuprum ... stupeo, ere \\\"starr stehn ... betaubt sein\\\"' -- same family, same Sanskrit base.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. (s)teu- VIII\", \"stance\": \"supports\",\n    \"note\": \"'VIII. Variant zero-grade form *tup-. 1. Suffixed form *tup-o- in Greek tupos, a blow, mold, die: TYPE ... 2. Nasalized form *tu-m-p- in Greek tumpanon, drum'.\"},\n   {\"src\": \"IEC\", \"where\": \"Mann, IECD (IEC.txt)\", \"stance\": \"silent\",\n    \"note\": \"Mann has no separate tup-/tubh- lemma at the places grepped (steud-/steug- ll. 17219-17220 cover the d-/g- forms only).\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Sanskrit\", \"words\": \"tuj\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Pokorny, section 'B. (s)teu-g-': 'Old Indic tujati, tunjati, tunjati \\\"throngs, stoesst\\\", Med. \\\"kommt in schnelle \"\n   \"Bewegung\\\"' (POK 1032). Wiktionary's article on the root तुज् (tuj) gives 'to strike, hit, push; to press out; to flow forth' \"\n   \"and derives it from PIE *(s)tewg- 'to push, hit' (cognate with Proto-Germanic *stukkaz 'stump', English stock). Cheung EDIV 387 \"\n   \"sets up Iranian *tauj-1 'to impel, hasten' from 'PIE *(s)teug- \\\"to set in motion, impel\\\" = LIV: 602 | Pok.: 1032 f.', with \"\n   \"Skt. tuj- as its Indic match. Nourai's gloss 'to press, push, throw' renders Mo'in's Persian gloss in BQT (فشار دادن، راندن، \"\n   \"انداختن، پراندن) and is accurate.\"),\n \"derivation_fa\": (\"پوکورنی در بخش B گسترده‌ای *(s)teu-g- سنسکریت tujati, tuñjati «می‌راند، می‌کوبد» را نخستین گواه آورده است (ص ۱۰۳۲). \"\n   \"ویکی‌واژه نیز ریشهٔ تُج (तुज्) را «زدن، راندن، فشردن» معنی کرده و آن را از هندواروپایی *(s)tewg- گرفته است؛ چونگ هم ریشهٔ ایرانی \"\n   \"*tauj¹ «راندن، شتافتن» را از همین *(s)teug- می‌داند. معنایی که نورایی داده («فشار دادن، راندن، انداختن») ترجمهٔ همان یادداشت \"\n   \"معین در حاشیهٔ برهان قاطع است و درست است. ادعای نورایی درست است.\"),\n \"sources\": [W + \"%E0%A4%A4%E0%A5%81%E0%A4%9C%E0%A5%8D\"],\n \"ref_check\": [\n   {\"ref\": \"POK:1032\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt: 'B. (s)teu-g-. Old Indic tujati, tunjati, tunjati \\\"throngs, stoesst\\\", Med. \\\"kommt in schnelle Bewegung\\\"' -- inside the article whose Page(s) line is 1032-1034.\"}\n ],\n \"consulted\": [\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 387 s.v. *tauj1 (CHEUNG.txt l. ~25213)\", \"stance\": \"supports\",\n    \"note\": \"'*tauj1 \\\"to impel, hasten\\\" ... SANSKRIT: tuj \\\"to impel, drive, set in motion\\\" (RV) ... PIE *(s)teug- \\\"to set in motion, impel\\\" = LIV: 602 | Pok.: 1032 f.'\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. stock (KLN_1966.txt l. 36848)\", \"stance\": \"supports\",\n    \"note\": \"'... and cogn. with Lith. stugti \\\"to be prominent\\\" ... OI. tujati, tunjati, \\\"he pushes\\\"' -- Klein puts Skt. tuj in the same root family as the Germanic stock/stucco words.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II ~617 (WLD_Bd2_pages.txt l. 40977)\", \"stance\": \"supports\",\n    \"note\": \"'... von einem nas. Praesens *stung-yo (: ai. tunjati) aus durch Ablautentgleisung entstanden' -- the same equation.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Old Persian\", \"words\": \"ham-tauj, ham-taug, ham-taux\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"These are reconstructions, not attested Old Persian: Kent's Old Persian lexicon has no ham-tauj-, and the label should \"\n   \"read 'Old Iranian'. Nourai is copying Mo'in's footnote in Borhan-e Qate' verbatim; the footnote (vol. 1, p. 171 n. 5, continued on \"\n   \"p. 172) reads: 'پهلوی handoxtan (از handozh «اندوز»، بمعنی جمع کردن)، مرکب ... از: ham-toxtan (گردآوردن، کسب کردن ـ پرداختن)، از \"\n   \"ایرانی باستان ham-taug و ham-tauj، مشتق از سانسکریت turjati, tuj (فشار دادن، راندن، انداختن، پراندن) «نیبرگ ۱۰۰»' -- i.e. exactly \"\n   \"Nourai's ham-taug/ham-tauj and his Sanskrit parent. Abolqasemi (FFD p. 32, s.v. اندوختن) sets up *ham-tauxta- for the past stem \"\n   \"(whence Nourai's third form ham-taux: -ct- > -xt-) and *ham-tauca- for the present stem, but assigns the root to tauc 'to pay' \"\n   \"(پرداختن), not to tuj. Cheung's EDIV (2007) goes further and deliberately splits *tauj-2 'to acquire, gather, gain' (the source of \"\n   \"handoz-) from *tauj-1 'to impel' (< PIE *(s)teug-), noting 'The precise origin of *tauj-2 is unclear. The root postulated here may \"\n   \"be related to BSogd. twd'k ... NP toda \\\"mass\\\"', and gives it no PIE root. So the link Nourai draws is the Mo'in/Nyberg tradition; \"\n   \"it is possible but no longer the standard view.\"),\n \"derivation_fa\": (\"این صورت‌ها گواهی‌شده نیستند و بازسازی‌اند؛ در واژه‌نامهٔ پارسی باستان کِنت ham-tauj- نیامده است و برچسب درست \"\n   \"«ایرانی باستان» است نه «پارسی باستان». نورایی عیناً حاشیهٔ معین بر برهان قاطع را نقل کرده است: «پهلوی handôxtan (از handôzh \"\n   \"«اندوز»، بمعنی جمع کردن)... از: ham-tôxtan (گردآوردن، کسب کردن ـ پرداختن)، از ایرانی باستان ham-taug و ham-tauj، مشتق از سانسکریت \"\n   \"turjati, tuj» (برهان قاطع، ج۱، ص۱۷۱ پانوشت ۵ و دنبالهٔ آن در ص۱۷۲، به نقل از نیبرگ ۱۰۰). ابوالقاسمی در «ماده‌های فعل‌های فارسی دری» \"\n   \"ص۳۲ ستاک گذشته را *ham-tauxta- و ستاک حال را *ham-tauča- بازسازی کرده (č پیش از t به x بدل شده) ولی ریشه را tauč «پرداختن» می‌داند. \"\n   \"چونگ در «فرهنگ ریشه‌شناختی فعل ایرانی» ریشهٔ *tauj² «گردآوردن» را از *tauj¹ «راندن» جدا می‌کند و می‌نویسد خاستگاه آن روشن نیست. \"\n   \"پس ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [],\n \"ref_check\": [\n   {\"ref\": \"BQT:172\", \"status\": \"supports\",\n    \"note\": (\"read from the page image (borhan-ghate-v1 leaf n390 = printed p. 172; catch-line «بقیه از صفحهٔ ۱۷۱»), saved to \"\n             \"data/verification/sources/refs/ocr/BQT/172.vision.txt: 'از: ham-tôxtan (گردآوردن، کسب کردن ـ پرداختن)، از ایرانی باستان \"\n             \"ham-taug و ham-tauj، مشتق از سانسکریت turjati, tuj (فشار دادن، راندن، انداختن، پراندن) «نیبرگ ۱۰۰»'. Nourai's node is a \"\n             \"direct translation of this footnote.\")},\n   {\"ref\": \"FFD:32\", \"status\": \"partial\",\n    \"note\": (\"Abolqasemi, Fe'lha-ye Farsi-ye Dari, printed p. 32 = FFD_pages.txt pdf page 37, s.v. اندوختن: 'اندوخت < فارسی میانه [handōxt] \"\n             \"< ایرانی باستان *ham-tauxta-. ham پیشوند فعلی است ... č پیش از t به x بدل شده است. ریشهٔ tauč به معنی «پرداختن» است' and \"\n             \"'اندوز < فارسی میانه [handōz] < ایرانی باستان *ham-tauča-'. He gives the *ham-taux- form Nourai cites, but roots it in tauc \"\n             \"'to pay', not Sanskrit tuj.\")}\n ],\n \"consulted\": [\n   {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon (KNT.txt / KNT_full.txt)\", \"stance\": \"silent\",\n    \"note\": \"no ham-tauj-/ham-taug- in the Old Persian lexicon: the form is not attested in the Achaemenid inscriptions, so 'Old Persian' is a mislabel for 'Old/Proto-Iranian'.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV pp. 387-388 s.v. *tauj2 (CHEUNG.txt ll. 25232-25250)\", \"stance\": \"partial\",\n    \"note\": \"'*tauj2 \\\"to acquire, gather, gain\\\" -- MIDDLE PERSIAN (+ *ham-) MMP 'ndwc- ... NWIR: NP toxtan/toz- ... (+ *ham-) NP andoxtan/andoz- ... The precise origin of *tauj2 is unclear ... PIE -- | Pok.: 1080 ff.' Cheung keeps it apart from *tauj1 < *(s)teug-.\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II 95a/100, s.v. handoxtan (NYB_vol2_glossary.txt l. 1895)\", \"stance\": \"supports\",\n    \"note\": \"'handoxtan [hndwhtn'] to collect, to acquire, to gain ... < ham + toxtan (q.v.)' -- the ham- + tauj analysis Mo'in cites from Nyberg.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Pahlavi\", \"words\": \"ham-tôxtan, han-dôzh\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Middle Persian handoxtan / handoz- 'to gain, acquire, amass' is solidly attested: MacKenzie CPD 'handoxtan, handoz- \"\n   \"[hndwhtn', hndwc- | N an~] gain, acquire, amass; ~isn(ih): acquisition'; Manichaean MP 'ndwc-, pret. hndwxt (Cheung, DMMPP 180b). \"\n   \"Nyberg analyses it '< ham + toxtan', i.e. the preverb ham- 'together' prefixed to toxtan/toz- 'to pay, requite' -- in New Persian \"\n   \"ham- + t- yields and- by voicing and nasal assimilation (ham-toz > handoz > andoz). Nourai's two forms are exactly Mo'in's: \"\n   \"ham-toxtan (the analysed compound) and handozh (Mo'in's spelling of the present stem handoz). The gloss 'to store, add up, save' \"\n   \"matches MacKenzie 'amass' and Nyberg 'to collect, to acquire, to gain'.\"),\n \"derivation_fa\": (\"فعل فارسی میانهٔ handōxtan / handōz- «به دست آوردن، گرد آوردن، اندوختن» به‌خوبی گواهی شده است: مکنزی در «فرهنگ کوچک \"\n   \"پهلوی» آن را با املای پهلوی hndwhtn' و ستاک حال hndwc- آورده، و در پهلوی مانوی نیز 'ndwc- و ستاک گذشتهٔ hndwxt هست. نیبرگ ساختار آن \"\n   \"را ham + tōxtan می‌داند، یعنی پیشوند ham- «با هم» بر ستاک tōxtan/tōz- «پرداختن، تاوان دادن»؛ در گذر به فارسی نو ham-t- به and- بدل \"\n   \"شده است (همگونیِ خیشومی و واک‌دار شدن t پس از m/n). دو صورتی که نورایی آورده همان‌هایی است که معین در حاشیه نوشته: ham-tôxtan و \"\n   \"handôzh. ادعای نورایی درست است.\"),\n \"sources\": [W + \"%D8%A7%D9%86%D8%AF%D9%88%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:172\", \"status\": \"supports\",\n    \"note\": \"the same footnote read from the page image (ocr/BQT/172.vision.txt): 'پهلوی handôxtan (از handôzh «اندوز»، بمعنی جمع کردن)، مرکب ... از: ham-tôxtan'.\"},\n   {\"ref\": \"AEF:159\", \"status\": \"not_checked\",\n    \"note\": \"Khaleqi Motlaq's Asas-e Eshteqaq-e Farsi (the Persian version of Horn's Grundriss) is print-only (refs_online.json: 'Not online'). Its German original, Horn no. 122, was checked instead -- see consulted/HRN.\"}\n ],\n \"consulted\": [\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD p. 41 s.v. handoxtan (PHD.txt l. 394; PHD_mackenzie.txt l. 2809)\", \"stance\": \"supports\",\n    \"note\": \"'handoxtan, handoz- [hndwhtn', hndwc- | N an~] gain, acquire, amass. ~isn(ih): acquisition.'\"},\n   {\"src\": \"NYB\", \"where\": \"Nyberg II s.v. handoxtan (NYB_vol2_glossary.txt l. 1895)\", \"stance\": \"supports\",\n    \"note\": \"'handoxtan [hndwhtn'] to collect, to acquire, to gain 73.12 -- MPrs pres. pass. 3d p. pl. 'ndweyhyynd (Sogd 165.17); Paz. NP andoxtan, NP also andozidan; < ham + toxtan (q.v.).'\"},\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 122 (p. 30; HRN.txt l. 1452) and no. 402 (p. 89)\", \"stance\": \"supports\",\n    \"note\": \"'122. endoxten \\\"sammeln, erwerben\\\", Praes. endoz-em ... phlv. andoxtan, andocet \\\"sammeln, erwerben\\\" (Men., AV.). Siehe unter np. toxten (No. 402).' -- at no. 402 Horn adds of toxtan 'Eine aeltere Form ist nicht vorhanden', i.e. he offers no pre-Middle-Persian root.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 387 s.v. *tauj2\", \"stance\": \"supports\",\n    \"note\": \"'(+ *ham-) MMP 'ndwc-, MMP hndwxt (pret. stem), BMP /hndwc- /(h)andoz-/ \\\"to gain, acquire, amass\\\"; Inf.: BMP /hndwhtn /(h)andoxtan/'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Persian\", \"words\": \"andŭxtan\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"NP اندوختن andūxtan / present stem اندوز andūz- continues MP handoxtan/handoz- with the regular loss of initial h- \"\n   \"before a vowel (hand- > and-, cf. handaxtan > andaxtan, hangam > hangam/angam, handesidan > andisidan) and the New Persian raising \"\n   \"of MP -o- to -u-. Horn no. 122 records both the NP verb and its Pahlavi source; Borhan-e Qate' p. 171 has the headword اندوختن \"\n   \"'بمعنی جمع کردن و فراهم آوردن باشد' ('to gather and bring together') with Mo'in's footnote 5 giving Pahlavi handoxtan. The \"\n   \"secondary form اندوزیدن andūzīdan printed in the chart's script field is the denominative built on the present stem (already \"\n   \"Nyberg: 'NP also andozidan'), and is what Sa'di's line quoted in the chart uses (اندوزند). Gloss 'to save, store' is right.\"),\n \"derivation_fa\": (\"«اندوختن» (ستاک حال: اندوز) دنبالهٔ فارسی میانهٔ handōxtan / handōz- است؛ هـ آغازین پیش از واکه در فارسی نو افتاده \"\n   \"است (قس handāxtan > انداختن، handēšīdan > اندیشیدن) و ō فارسی میانه در فارسی نو به ū بدل شده. هرن در شمارهٔ ۱۲۲ «گروندریس» هم \"\n   \"صورت فارسی نو و هم منبع پهلوی آن را آورده است. در برهان قاطع (ج۱، ص۱۷۱) سرواژهٔ «اندوختن» با معنی «جمع کردن و فراهم آوردن» آمده و \"\n   \"معین در پانوشت ۵ آن را به پهلوی handôxtan بازبرده است. صورت «اندوزیدن» که در نمودار در کنار آن آمده فعلِ ساخته‌شده از ستاک حال است \"\n   \"(نیبرگ نیز آن را ثبت کرده) و همان است که در بیت سعدیِ نقل‌شده به کار رفته. ادعای نورایی درست است.\"),\n \"sources\": [W + \"%D8%A7%D9%86%D8%AF%D9%88%D8%AE%D8%AA%D9%86\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:171\", \"status\": \"supports\",\n    \"note\": (\"read from the page image (borhan-ghate-v1 leaf n389 = printed p. 171, identified by the catch-line «بقیه در صفحهٔ ۱۷۲»); \"\n             \"saved to data/verification/sources/refs/ocr/BQT/171.vision.txt: headword 'اندوختن* ـ بروزن افروختن، بمعنی جمع کردن و فراهم \"\n             \"آوردن باشد' with footnote '۵ ـ پهلوی handôxtan (از handôzh «اندوز»، بمعنی جمع کردن)، مرکب'.\")},\n   {\"ref\": \"AEF:159\", \"status\": \"not_checked\",\n    \"note\": \"Asas-e Eshteqaq-e Farsi is not available online (refs_online.json). Horn's German original (the book AEF translates) was read instead at no. 122.\"}\n ],\n \"consulted\": [\n   {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no. 122 (HRN.txt l. 1452)\", \"stance\": \"supports\",\n    \"note\": \"'122. endoxten \\\"sammeln, erwerben\\\", Praes. endoz-em, endoxis; phlv. andoxtan, andocet \\\"sammeln, erwerben\\\" (Men., AV.).'\"},\n   {\"src\": \"PHD\", \"where\": \"MacKenzie, CPD s.v. handoxtan\", \"stance\": \"supports\",\n    \"note\": \"'[... | N an~]' -- MacKenzie's own cross-reference marks New Persian andoxtan as the continuation.\"},\n   {\"src\": \"CHEUNG\", \"where\": \"EDIV p. 387\", \"stance\": \"supports\",\n    \"note\": \"'*NWIR: NP toxtan/toz- \\\"to acquire, gain, collect\\\" || (+ *ham-) NP andoxtan/andoz- \\\"to acquire, collect\\\"'.\"},\n   {\"src\": \"MON\", \"where\": \"Wiktionary s.v. اندوختن (citing MacKenzie 1971)\", \"stance\": \"supports\",\n    \"note\": \"'Inherited from Middle Persian hndwhtn' /handoxtan/, \\\"to gain, acquire, amass\\\"', present stem اندوز.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Germanic\", \"words\": \"staup; stubb; stukkjam\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"All three are Watkins's reconstructions under (s)teu-, and Nourai's glosses are Watkins's word for word: \"\n   \"'I. Extended forms *steup-, steub-. 1. Germanic *staup- in Old English steap, lofty, deep, projecting: STEEP. ... \"\n   \"5. Germanic expressive form *stubb- in Old English stubb, stybb, stump: STUB. ... III. Extended form *steug-. ... \"\n   \"2. Germanic *stukkjam in: a. Old High German stukki, crust, fragment, covering: SHTICK; b. Italian stucco, stucco: STUCCO.' \"\n   \"Walde-Pokorny II 619-620 has the same material from the other side ('ags. steap \\\"hoch, ragend\\\" (engl. steep \\\"steil\\\"); \"\n   \"aisl. stubbr, stubbi m. \\\"Stumpf\\\", ags. stybb n. \\\"Baumstumpf\\\"'). Formally: PIE *steup-/*steub- gives Gmc *staup-/*stubb- by \"\n   \"Grimm's law (*p > f is avoided here because the forms are *steup- with the s-mobile cluster; the geminate -bb- of *stubb- is \"\n   \"expressive), and *steug- gives Gmc *stukk-.\"),\n \"derivation_fa\": (\"هر سه صورت بازسازی‌های واتکینز در پیوست ریشه‌های هندواروپایی فرهنگ American Heritage اند و معناهایی که نورایی داده \"\n   \"واژه‌به‌واژه از همان‌جاست: ژرمنی *staup- در انگلیسی کهن stēap «بلند، برآمده» (انگلیسی steep)، صورت تأکیدی *stubb- در انگلیسی کهن \"\n   \"stubb/stybb «کُنده» (انگلیسی stub)، و *stukkjam در آلمانی علیای کهن stukki «پوسته، پاره، پوشش» که ایتالیایی stucco از آن است. \"\n   \"والده-پوکورنی (ج۲، ص۶۱۹–۶۲۰) نیز همین گواه‌ها را آورده‌اند. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/stucco\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1543\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 (= the appendix Nourai's AHD page numbers refer to) s.v. (s)teu-: 'Germanic *staup- in Old English steap, lofty, deep, projecting: STEEP', '*stubb- in Old English stubb, stybb, stump: STUB', '*stukkjam in ... Old High German stukki, crust, fragment, covering ... Italian stucco: STUCCO' (AHD_watkins1985.txt ll. 1024-1026).\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 619-620 (WLD_Bd2_pages.txt ll. 41119-41145)\", \"stance\": \"supports\",\n    \"note\": \"'aisl. stubbr, stubbi m. \\\"Stumpf, Baumstumpf\\\", ags. stybb n. \\\"Baumstumpf\\\"'; 'ags. steap \\\"hoch, ragend\\\" (engl. steep \\\"steil\\\")'.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. stock and stucco (KLN_1966.txt ll. 36848, 37109)\", \"stance\": \"supports\",\n    \"note\": \"'stucco, n. ... It., fr. OHG. stucchi, \\\"crust, coating, piece\\\" ... rel. to OS. stukki, ON. stykki, OE. stycce, \\\"piece\\\", and to E. stock'; s.v. stock the same group is made cognate with 'OI. tujati, tunjati \\\"he pushes\\\"'.\"},\n   {\"src\": \"POK\", \"where\": \"POK 1032-1034 section A/C/D\", \"stance\": \"supports\",\n    \"note\": \"'Old Icelandic stubbr, stubb m. \\\"stump, trunk\\\", Old English stybb n. \\\"stump\\\"'; 'ablaut. Old English steap \\\"hoch, ragend\\\" (engl. steep)'; 'Old High German stucki ... \\\"piece\\\"'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 9, \"lang\": \"English\", \"words\": \"steep; stub; stucco\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"steep < OE steap 'lofty, projecting, deep' (Gmc *staup-), the adjective surviving with the sense 'precipitous' from \"\n   \"Middle English on; stub < OE stubb, stybb 'tree-stump' (Gmc *stubb-); stucco is not a native word but a 16th-c. loan from Italian \"\n   \"stucco 'plaster coating', itself a Langobardic/Germanic loan into Italian from OHG stukki 'crust, piece, covering' -- so English \"\n   \"receives the Germanic word by the Romance detour. Etymonline: 'stucco ... from Italian stucco, likely derived from Germanic sources \"\n   \"like Old Saxon stukki and Old High German stukki, \\\"crust, piece, fragment\\\"' (Etymonline hedges between PIE *sta- and '(s)teu-'; \"\n   \"Watkins and Klein both put it under (s)teu-/stock).\"),\n \"derivation_fa\": (\"steep از انگلیسی کهن stēap «بلند، برآمده» است (ژرمنی *staup-) که معنای «سراشیب تند» را در انگلیسی میانه گرفت؛ \"\n   \"stub از انگلیسی کهن stubb/stybb «کُندهٔ درخت» (ژرمنی *stubb-)؛ اما stucco واژهٔ بومی انگلیسی نیست بلکه وام‌واژه‌ای است از ایتالیایی \"\n   \"stucco «گچ‌بری، اندود» که خود از راه لُمباردی از آلمانی علیای کهن stukki «پوسته، پاره» به ایتالیایی رفته است؛ یعنی انگلیسی این واژهٔ \"\n   \"ژرمنی را با چرخشی از راه زبان‌های رومی پس گرفته است. (اتیمانلاین میان ریشهٔ *stā- و *(s)teu- مردد است، ولی واتکینز و کلاین هر دو \"\n   \"آن را زیر همین ریشه می‌نهند.) ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/stucco\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. (s)teu- explicitly ends the three sub-entries with the English keywords 'STEEP', 'STUB' and 'STUCCO'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. stucco (KLN_1966.txt l. 37109)\", \"stance\": \"supports\",\n    \"note\": \"'stucco, n., a kind of fine plaster used as a coating for walls. -- It., fr. OHG. stucchi, \\\"crust, coating, piece\\\" ... and to E. stock (q.v.)'.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 619\", \"stance\": \"supports\",\n    \"note\": \"'ags. steap \\\"hoch, ragend\\\" (engl. steep \\\"steil\\\")' -- the OE > NE steep line.\"},\n   {\"src\": \"POK\", \"where\": \"POK 1032-1034 section D\", \"stance\": \"supports\",\n    \"note\": \"'ablaut. Old English steap \\\"hig, ragend\\\" (engl. steep \\\"steep\\\") ... Old Icelandic stubbr, stubb m. \\\"stump, trunk\\\"'.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 10, \"lang\": \"Latin\", \"words\": \"stupěre; studěre\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Both are stative verbs in -e- built on zero grades of two different extensions of the root: stupere 'to be stunned, \"\n   \"be numb' < *stup-e- (the p-extension *(s)teu-p-), and studere 'to be diligent' < *stud-e- (the d-extension *(s)teu-d-, cf. Latin \"\n   \"tundo, tutudi 'to beat'). Watkins: 'IV. Suffixed (stative) zero-grade extended form *stup-e- in Latin stupere, to be stunned: \"\n   \"STUPENDOUS, STUPID; STUPEFY. V. Suffixed (stative) extended zero-grade form *stud-e- in Latin *studere, to be diligent \"\n   \"(< \\\"to be pressing forward\\\"): STUDENT, STUDY.' Nourai's gloss 'pressing forward, study' is Watkins's parenthesis copied across; \"\n   \"the semantic bridge is 'to push/press at something' > 'to apply oneself'. The book's ě renders the long e of stupere/studere \"\n   \"(Nourai's usual transliteration, as in stuppe = Greek stuppe).\"),\n \"derivation_fa\": (\"هر دو فعل «حالت‌نما»ی لاتینی با پسوند -ē- بر پایهٔ دو گسترده از یک ریشه‌اند: stupēre «مات و بی‌حس بودن» از \"\n   \"*stup-ē- (گسترده‌ای با -p-) و studēre «کوشیدن، پشتکار داشتن» از *stud-ē- (گسترده‌ای با -d-، قس لاتینی tundō «می‌کوبم»). \"\n   \"واتکینز همین دو را جداگانه آورده و معنای «پیش‌راندن» را برای studēre در پرانتز نهاده است؛ همان پرانتز است که نورایی آن را به \"\n   \"صورت «pressing forward» در نمودار آورده. تحول معنایی روشن است: «فشار آوردن بر چیزی» ← «جدّ و جهد کردن». ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/study\"],\n \"ref_check\": [\n   {\"ref\": \"AHD:1544\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. (s)teu- IV-V: 'Latin stupere, to be stunned: STUPENDOUS, STUPID; STUPEFY' and 'Latin *studere, to be diligent (< \\\"to be pressing forward\\\"): STUDENT, STUDY'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK 1032-1034, sections C and D\", \"stance\": \"supports\",\n    \"note\": \"'studeo, -ere \\\"sich ernstlich worum bemuehen, eager betreiben\\\", studium \\\"Streben, eagerness\\\" (\\\"*whereupon aim\\\" from \\\"whereupon hit\\\")' (C. (s)teu-d-); 'stuped, -ere \\\"rigid stand; betaeubt, betreten sein\\\", stupendus' (D. (s)teu-p-).\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 619 (WLD_Bd2_pages.txt ll. 41097-41100)\", \"stance\": \"supports\",\n    \"note\": \"'lat. stuprum \\\"Schande\\\" ... ; stupeo, ere \\\"starr stehn (bes. von unbewegtem Wasser); betaeubt, betreten sein, stutzen\\\", stupendus \\\"erstaunlich\\\"'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Stop (SKT.txt l. 18623)\", \"stance\": \"supports\",\n    \"note\": \"Skeat groups 'Stub, Stupid, Stump' as allied words of the same root.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 11, \"lang\": \"English\", \"words\": \"stupid, stupendous, study, student\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"A well-known Latin-to-English chain: stupid (1540s) < Middle French stupide < Latin stupidus 'struck senseless', \"\n   \"from stupere; stupendous (1540s) < Late Latin stupendus, the gerundive of stupere; study (n. c.1300, v. c.1300) < Old French \"\n   \"estudie/estudier < Latin studium/studere; student (late 14c.) < Latin studentem, present participle of studere. Etymonline files \"\n   \"study under 'PIE root *(s)teu- (1) \\\"to push, stick, knock, beat\\\"', with the semantic note 'pressing forward, thrusting toward' \"\n   \"> 'striving after'. No Iranian or Semitic link is involved; one source covering the chain suffices.\"),\n \"derivation_fa\": (\"زنجیرهٔ آشنای لاتینی ← فرانسوی ← انگلیسی است: stupid از فرانسوی میانه stupide از لاتینی stupidus «مات‌شده» \"\n   \"(از stupēre)؛ stupendous از لاتینی متأخر stupendus (صفت وجوبی همان فعل)؛ study از فرانسوی کهن estudie/estudier از لاتینی \"\n   \"studium/studēre؛ و student از studentem، اسم فاعل studēre. اتیمانلاین نیز study را زیر ریشهٔ هندواروپایی *(s)teu- «راندن، زدن» \"\n   \"می‌نهد و تحول معنایی «پیش‌راندن ← کوشیدن در پی چیزی» را یادآور می‌شود. ادعای نورایی درست است.\"),\n \"sources\": [\"https://www.etymonline.com/word/study\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. (s)teu- lists precisely STUPENDOUS, STUPID, STUPEFY (IV) and STUDENT, STUDY (V).\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966/1971 s.vv. stupid, study\", \"stance\": \"supports\",\n    \"note\": \"Klein derives stupid from L. stupidus (fr. stupere) and study from OF. estudie, fr. L. studium -- the same chain.\"},\n   {\"src\": \"POK\", \"where\": \"POK 1032-1034 sections C, D\", \"stance\": \"supports\",\n    \"note\": \"Latin studeo/studium and stupeo/stupendus are the Latin evidence of the root in Pokorny's own article.\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ---------------------------------------------------------------- entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Stewe\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *steu(ə)- 'to condense, cluster, get dense' (Pokorny IEW 1035, 'steue-')\",\n \"note\": (\"Pokorny 1035 has the lemma 'steue-, Meaning: to get dense or tight' with the note 'perhaps stau-, stau-, stu- ... as an \"\n          \"extension of *sta-', material: 'Old Indic stu-k-a, stuka- \\\"tuft of wool\\\", stu-p-a-, stupa- m. \\\"Haarschopf\\\", gr. *stupe, \"\n          \"stuppe \\\"oakum\\\" (out of it Latin stupa, stuppa), gr. stupho \\\"pull together, make dense\\\"'. Watkins renders it 'steu(e)-. \"\n          \"To condense, cluster. Possible root. [Pok. steua- 1035.]' -- so Nourai's root name, language and gloss are all right, though \"\n          \"both Pokorny ('perhaps') and Watkins ('possible root') hedge about whether it is separate from *sta- 'to stand'. \"\n          \"The Turkish/Persian branch hung under it (nodes 2-3) does not belong to this root.\"),\n \"note_fa\": (\"پوکورنی در صفحهٔ ۱۰۳۵ مدخل steuə- «انبوه و فشرده شدن» را می‌آورد و آن را شاید گسترده‌ای از ریشهٔ *stā- «ایستادن» می‌داند؛ \"\n             \"گواه‌های آن سنسکریت stuka- «طرهٔ پشم»، stūpa- «کاکل، توده»، یونانی στύππη «الیاف خام کتان» (که لاتینی stuppa از آن است) و \"\n             \"یونانی στύφω «به هم فشردن» است. واتکینز نیز آن را «steu(ə)-: انبوه شدن، خوشه شدن؛ ریشهٔ احتمالی» می‌نامد. نام ریشه، برچسب \"\n             \"زبانی و معنایی که نورایی داده درست است، هرچند هر دو مرجع با احتیاط سخن گفته‌اند. شاخهٔ ترکی/فارسی (گره‌های ۲ و ۳) به این \"\n             \"ریشه نمی‌پیوندد.\"),\n \"sources\": [W + \"%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%82%E0%A4%AA\"],\n \"ref_check\": [\n   {\"ref\": \"POK:1035\", \"status\": \"supports\",\n    \"note\": \"POK_full.txt (grep -n 'lemma: steue' -> l. 82936): 'Root / lemma: steue- / Meaning: to get dense or tight ... Material: ... Old Indic stu-p-a-, stupa- m. \\\"Haarschopf\\\", gr. *stupe, stuppe \\\"oakum\\\" (out of it Latin stupa, stuppa ds) ... References: WP. II 620 ... Page(s): 1035'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 620 (WLD_Bd2_pages.txt ll. 41180-41190)\", \"stance\": \"supports\",\n    \"note\": \"'ai. stu-p-a- m. \\\"Schopf, Haarbusch\\\", stupa- m. \\\"Schopf\\\" ... gr. stupe, stuppe \\\"Werg\\\" (daraus lat. stupa, stuppa ds.); gr. stupho \\\"ziehe zusammen, mache dicht, hart\\\"'.\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. steu(e)- (AHD_watkins1985.txt l. 1026)\", \"stance\": \"supports\",\n    \"note\": \"'steu(e)-. To condense, cluster. Possible root. 1. Extended form *stup- in: a. Greek stuppe, tuft, tow: STOP, STUPE; b. Sanskrit stupah, tuft of hair, crown of the head: STUPA. 2. Extended form *stibh- in Greek stuphein, to contract: STYPTIC. [Pok. steua- 1035.]'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 6.21 'cloth' (SYN.txt l. 9953)\", \"stance\": \"supports\",\n    \"note\": \"'... fr. Lat. stuppa \\\"coarse linen, tow\\\", fr. Grk. stuppe (perh. : Skt. stupa- \\\"tuft of hair\\\", Walde-P. 2.620)' -- Buck cites the same WP page for the same equation.\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Sanskrit\", \"words\": \"stupa\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"The word and the root are right, the gloss is not. Sanskrit stūpa- (also stupa-) means 'tuft of hair, crown of the \"\n   \"head' and then 'heap, mound; Buddhist relic-mound' -- Pokorny 1035 'ai. stu-p-a-, stupa- m. \\\"Haarschopf\\\"', Watkins 'Sanskrit \"\n   \"stupah, tuft of hair, crown of the head: STUPA', Wiktionary 'from Proto-Indo-Iranian *stuHpas, related to stuka \\\"tuft of hair\\\"; \"\n   \"compare Ancient Greek stuppeion \\\"coarse hemp fibre\\\" and stupho \\\"to contract\\\"'. Nourai's 'a round mass, ball' is not a \"\n   \"dictionary sense of stūpa; it is lifted from Crooke's bracketed note in Hobson-Jobson ('Mr. Platts regards T. tob, top, as meaning \"\n   \"originally \\\"a round mass\\\", from Skt. stupa'), i.e. from the very claim the next node rests on. Phonologically the form is a \"\n   \"p-extension of the zero grade *stu-, exactly parallel to Greek stuppe.\"),\n \"derivation_fa\": (\"خودِ واژه و ریشه درست است، اما معنایی که نورایی داده نادرست است. سنسکریت stūpa- به معنی «کاکل، فرق سر» و سپس \"\n   \"«توده، تپه؛ بنای یادمانی بودایی» است — پوکورنی «Haarschopf»، واتکینز «tuft of hair, crown of the head»، و ویکی‌واژه آن را از \"\n   \"هندوایرانی آغازین *stuHpas و هم‌ریشه با stukā «طرهٔ مو» می‌داند و یونانی στυππεῖον «الیاف خام کنف» را هم‌تبار آن می‌شمارد. \"\n   \"«تودهٔ گرد، گوی» که نورایی نوشته از یادداشت کروک در Hobson-Jobson گرفته شده که آن را به پلاتس نسبت می‌دهد. از نظر آوایی این صورت \"\n   \"گسترده‌ای با -p- بر پایهٔ صورت کاهیدهٔ *stu- است، درست مانند στύππη یونانی. ادعای نورایی با احتیاط پذیرفتنی است.\"),\n \"sources\": [W + \"%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%82%E0%A4%AA\"],\n \"ref_check\": [\n   {\"ref\": \"POK:1035\", \"status\": \"partial\",\n    \"note\": \"Pokorny has 'Old Indic stu-p-a-, stupa- m. \\\"Haarschopf\\\"' -- the word, under this root, but glossed 'tuft of hair', not 'a round mass, ball'.\"},\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins: 'b. Sanskrit stupah, tuft of hair, crown of the head: STUPA' -- same word, same root, different gloss from Nourai's.\"}\n ],\n \"consulted\": [\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 620\", \"stance\": \"partial\",\n    \"note\": \"'ai. stu-p-a- m. \\\"Schopf, Haarbusch\\\", stupa- m. \\\"Schopf\\\"' with the parenthesis that the sense 'Hauptbalken eines Hauses' rather recalls sthuna 'Saeule' under *sta-.\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson s.v. TOPE c. (HJB.txt l. 22374 ff., printed pp. 933-934)\", \"stance\": \"partial\",\n    \"note\": \"'c. An ancient Buddhist monument in the form of a solid dome ... appears to come from Skt. stupa through the Pali or Prakrit thupo' -- HJB's own use of stupa is 'mound/dome', and its gloss 'a round mass' is attributed to Platts, not asserted.\"},\n   {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt l. 9953)\", \"stance\": \"supports\",\n    \"note\": \"'perh. : Skt. stupa- \\\"tuft of hair\\\", Walde-P. 2.620'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Turkish\", \"words\": \"top, tob\",\n \"verdict\": \"disputed\",\n \"derivation\": (\"Turkish top 'ball; cannon' is native Turkic, not a Sanskrit loan. It goes back to Proto-Turkic *top 'round thing, \"\n   \"ball', with a full Turkic family across all branches (Azerbaijani top, Turkmen top, Uzbek to'p, Uyghur top, Tatar/Bashkir tup, \"\n   \"Kazakh dop, Kyrgyz top, Chuvash tupa, Khalaj top) and derivatives *topik 'kneecap, ankle-bone' (Karakhanid topik) and *topuz \"\n   \"'mace'. Vambery's Etymologisches Woerterbuch der turko-tatarischen Sprachen p. 192 already sets it in that native family \"\n   \"('cag. tob, top -- Kugel, Knaeuel, Busch; topalak = der Knoten eines Strickes; tope, tuepe, tipe = Huegel, oberer Theil, \"\n   \"Kopfscheitel; topmak = sammeln', with Chuvash tube 'Anhoehe' and Altai tobo 'Huegel'), i.e. a Turkic root 'round lump, heap, \"\n   \"top of something'. Nourai's arrow Sanskrit stupa > Turkish top comes from a bracketed remark added by W. Crooke to Hobson-Jobson, \"\n   \"attributing it to J. T. Platts; Yule's own text there says flatly of Turkish top: 'We cannot trace it further.' No Turcologist \"\n   \"accepts the Sanskrit source, and there is no historical channel for it (the word means 'cannon' only from the 15th c., long after \"\n   \"any Indic contact would have to be posited).\"),\n \"derivation_fa\": (\"«top» ترکی به معنی «گوی؛ توپ جنگی» واژه‌ای بومی ترکی است، نه وام‌واژه‌ای از سنسکریت. ریشهٔ آن ترکی آغازین *top \"\n   \"«چیز گرد، گوی» است و در همهٔ شاخه‌های ترکی بازمانده دارد (آذربایجانی و ترکمنی top، ازبکی toʻp، اویغوری توپ، تاتاری و باشقیری tup، \"\n   \"قزاقی dop، قرقیزی top، چوواشی tupă) و مشتقاتی مانند *topïk «کاسهٔ زانو، قوزک» و *topuz «گرز» دارد. وامبری نیز در «فرهنگ ریشه‌شناختی \"\n   \"زبان‌های ترکی-تاتاری» (ص۱۹۲) همین واژه را در خانوادهٔ بومی ترکی نهاده است. پیوندی که نورایی کشیده (سنسکریت stūpa ← ترکی top) از \"\n   \"یادداشتی است که کروک در ویرایش دوم Hobson-Jobson در قلاب افزوده و آن را به پلاتس نسبت داده؛ حال آنکه متن خودِ یول می‌گوید: \"\n   \"«نمی‌توانیم آن را فراتر از این پی بگیریم». پژوهش امروزی این ریشه‌یابی را رد می‌کند.\"),\n \"sources\": [W + \"Reconstruction:Proto-Turkic/top\"],\n \"ref_check\": [\n   {\"ref\": \"HJB:933\", \"status\": \"partial\",\n    \"note\": (\"Hobson-Jobson s.v. TOPE a. (HJB.txt l. 22375; the printed page-head numerals 933 and 935 bracket this text at ll. 22334 and \"\n             \"22379, so the entry stands on pp. 933-934): 'a. Hind. top, \\\"a cannon.\\\" This is Turkish top, adopted into Persian and \"\n             \"Hindustani. We cannot trace it further. [Mr. Platts regards T. tob, top, as meaning originally \\\"a round mass,\\\" from Skt. \"\n             \"stupa, for which see below.]' -- Nourai's whole chain is here, but as a bracketed editorial suggestion that the dictionary's \"\n             \"own text declines to endorse.\")}\n ],\n \"consulted\": [\n   {\"src\": \"TTS\", \"where\": \"Vambery p. 192 (TTS_vambery1878_uoft_djvu.txt ll. 10635-10648)\", \"stance\": \"contradicts\",\n    \"note\": \"'cag. tob, top -- Kugel, Knaeuel, Busch; topi = eine runde, halbkugelfoermige Kappe in Chokand; topalak = der Knoten eines Strickes; tope, tuepe, tipe = Huegel, oberer Theil, Kopfscheitel; topmak = sammeln ... osm. top = Kugel, Ballen ... cuv. tube = Anhoehe, Huegel ... alt. tobo = Huegel' -- a native Turkic nest, no foreign source suggested.\"},\n   {\"src\": \"MON\", \"where\": \"Wiktionary, Reconstruction:Proto-Turkic/top\", \"stance\": \"contradicts\",\n    \"note\": \"'*top: round thing, ball', with descendants in Oghuz, Karluk, Kipchak, Chuvash and Khalaj and loans into Persian, Greek, Albanian, Armenian, Georgian and Slavic; no Indo-European or Sanskrit origin is discussed.\"},\n   {\"src\": \"LKT\", \"where\": \"Lokotsch (LKT.txt)\", \"stance\": \"silent\",\n    \"note\": \"grep for 'Kanone'/'top' returns only unrelated entries (algazara l. 1721, guelle l. 1782); Lokotsch has no entry deriving Turkish top from Sanskrit.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"tŭp\",\n \"verdict\": \"confirmed\",\n \"derivation\": (\"Persian توپ tūp 'ball; cannon' is a loan from Ottoman/Azerbaijani Turkish top, taken over with the Ottoman artillery \"\n   \"vocabulary (whence also توپچی tūpčī 'gunner' < Turkish topçu, and Turco-Persian توپخانه tūpxāna 'artillery park', the Tophane of \"\n   \"Istanbul). Mo'in's supplementary entry in Borhan-e Qate' (vol. 1, p. 526) says so in one word: 'توپ ـ از ترکی، سلاحی است آتشین \"\n   \"دارای لوله‌ای بزرگ از آهن یا مفرغ که بر روی چرخ حمل شود ...' ('from Turkish; a firearm with a large iron or bronze barrel carried \"\n   \"on a wheel'), immediately followed by 'توپ‌چی ـ از ترکی'. Wiktionary s.v. توپ: 'From Turkic. Compare Turkish top.' From Persian the \"\n   \"word passed on to Hindi/Urdu तोप/توپ. Nourai's arrow Turkish > Persian is therefore right; only its parent (node 2) is wrong.\"),\n \"derivation_fa\": (\"«توپ» فارسی وام‌واژه‌ای است از ترکی عثمانی/آذربایجانی top که همراه با اصطلاحات توپخانهٔ عثمانی به فارسی آمده است \"\n   \"(از همین راه «توپچی» از topçu ترکی، و «توپخانه»). معین در مدخل افزودهٔ خود در برهان قاطع (ج۱، ص۵۲۶) کوتاه و روشن نوشته است: \"\n   \"«توپ ـ از ترکی، سلاحی است آتشین دارای لوله‌ای بزرگ از آهن یا مفرغ که بر روی چرخ حمل شود...» و بی‌درنگ پس از آن «توپ‌چی ـ از ترکی». \"\n   \"ویکی‌واژه نیز می‌گوید «از ترکی؛ قس Turkish top». از فارسی هم به هندی و اردو (तोप/توپ) رفته است. پس همین پیوند (ترکی ← فارسی) که \"\n   \"نورایی کشیده درست است؛ تنها پدرِ آن (گرهٔ سنسکریت) نادرست است.\"),\n \"sources\": [W + \"%D8%AA%D9%88%D9%BE\", W + \"Reconstruction:Proto-Turkic/top\"],\n \"ref_check\": [\n   {\"ref\": \"BQT:526\", \"status\": \"supports\",\n    \"note\": \"BQT_v1_pages.txt, form-feed leaf 754 (printed p. ~526, matching Nourai's citation): the Mo'in-added entry 'توپ ـ از ترکی، سلاحی است آتشین دارای لوله‌ای بزرگ از آهن یا مفرغ که بر روی چرخ حمل شود ... توپ زدن، توپ انداختن ...' and next 'توپ‌چی ـ از ترکی، لشکری که با توپ کار کند'.\"},\n   {\"ref\": \"HJB:933\", \"status\": \"supports\",\n    \"note\": \"Hobson-Jobson s.v. TOPE a.: 'This is Turkish top, adopted into Persian and Hindustani' (HJB.txt l. 22375); and s.v. TOPE-KHANA: 'Turco-Pers. top-khana, \\\"cannon-house\\\" ... the Tophaneh [of Constantinople]'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"MON\", \"where\": \"Wiktionary s.v. توپ (Persian)\", \"stance\": \"supports\",\n    \"note\": \"'From Turkic. Compare Turkish top.' -- no further origin given.\"},\n   {\"src\": \"TTS\", \"where\": \"Vambery p. 192\", \"stance\": \"supports\",\n    \"note\": \"'osm. top = Kugel, Ballen' -- the Ottoman form that Persian borrowed.\"},\n   {\"src\": \"HJB\", \"where\": \"Hobson-Jobson, TOPE-KHANA (HJB.txt l. 22393)\", \"stance\": \"supports\",\n    \"note\": \"'Turco-Pers. top-khana \\\"cannon-house\\\" or \\\"cannon-department\\\". The word is the same that appears so often in reports from Constantinople as the Tophaneh' -- the Ottoman route of the loan.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Greek\", \"words\": \"stuppě\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"stuppě : tuft, toe\",\n \"correct_form\": \"stuppē : tuft, tow\",\n \"derivation\": (\"The Greek word is right: stuppe (στύππη, also στύπη) 'tow, oakum, the coarse fibre of flax or hemp', the p-extension \"\n   \"of the root's zero grade, matching Sanskrit stūpa- 'tuft'. What is wrong is the English gloss: Nourai's source, Watkins, prints \"\n   \"'Greek stuppe, tuft, TOW' (tow = the coarse broken fibre of flax), and the printed page of the dictionary (pdf p. 482, book p. 452) \"\n   \"shows 'tuft, toe' -- so this is Nourai's own misprint, faithfully carried into the JSON; the page image was checked and is filed at \"\n   \"data/verification/sources/refs/ocr/BOOK/482.png. The same misprint recurs in the Latin node (#5, 'to stop with toe'), which \"\n   \"confirms it is a systematic slip of 'tow' for 'toe' in the book, not an extraction error.\"),\n \"derivation_fa\": (\"خودِ واژهٔ یونانی درست است: στύππη (و گونهٔ στύπη) «الیاف خام کتان یا کنف، پنبهٔ کهنه»، که گسترده‌ای با -p- بر صورت \"\n   \"کاهیدهٔ ریشه است و با سنسکریت stūpa- «طره» می‌خواند. آنچه نادرست است ترجمهٔ انگلیسی آن است: منبع نورایی، یعنی واتکینز، «tuft, tow» \"\n   \"نوشته است (tow همان الیاف زبر کتان است)، اما در صفحهٔ چاپی کتاب (ص ۴۵۲) «tuft, toe» آمده است. تصویر صفحه بررسی شد: خطای چاپی خودِ \"\n   \"کتاب است و استخراج داده درست و وفادار است. همین لغزش در گرهٔ لاتینی (#۵، «to stop with toe») نیز تکرار شده که نشان می‌دهد نویسنده \"\n   \"«tow» را «toe» نوشته است. خطای چاپی کتاب.\"),\n \"sources\": [W + \"%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%82%E0%A4%AA\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"supports\",\n    \"note\": \"Watkins 1985 s.v. steu(e)-: '1. Extended form *stup- in: a. Greek stuppe, tuft, TOW: STOP, STUPE' -- the reference Nourai cites prints 'tow', the book prints 'toe'.\"}\n ],\n \"consulted\": [\n   {\"src\": \"POK\", \"where\": \"POK 1035 s.v. steue-\", \"stance\": \"supports\",\n    \"note\": \"'gr. *stupe, stuppe \\\"oakum\\\" (out of it Latin stupa, stuppa ds)' -- 'oakum' = tow, i.e. loose flax/hemp fibre.\"},\n   {\"src\": \"WLD\", \"where\": \"Walde-Pokorny II 620 (WLD_Bd2_pages.txt l. 41185)\", \"stance\": \"supports\",\n    \"note\": \"'gr. stupe, stuppe \\\"Werg\\\" (daraus lat. stupa, stuppa ds.)' -- German Werg = tow.\"},\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. stop and Stipa (KLN_1966.txt ll. 36906, 36827)\", \"stance\": \"supports\",\n    \"note\": \"'fr. L. stuppa, stupa, \\\"the coarse part of flax, tow\\\", fr. Gk. stuppe, of s.m., which is cogn. with OI. stupah, \\\"tuft of hair\\\"'.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Latin\", \"words\": \"stuppâre\",\n \"verdict\": \"transcription_suspect\",\n \"error_in\": \"book\",\n \"book_prints\": \"stuppâre : to stop with toe\",\n \"correct_form\": \"stuppāre : to stop (up) with tow\",\n \"derivation\": (\"The derivation is standard: Greek stuppe was borrowed into Latin as the noun stuppa/stupa 'the coarse part of flax, \"\n   \"tow' (classical, e.g. Pliny), and from it Vulgar/Medieval Latin formed the verb *stuppare 'to stop up with tow, to caulk' (whence \"\n   \"Italian stoppare, Old Provencal estopar, Old French estoper, French etouper). Klein 1966 s.v. stop gives the chain verbatim: \"\n   \"'These words derive fr. ML. stuppare, \\\"to stop with tow\\\" ... fr. L. stuppa, stupa, \\\"the coarse part of flax, tow\\\", fr. Gk. \"\n   \"stuppe'. Two caveats on Nourai's box: (a) the gloss again misprints 'tow' as 'toe' (checked on the printed page, pdf 482 -- \"\n   \"the book's error, faithfully extracted; image at data/verification/sources/refs/ocr/BOOK/482.png); (b) stuppare is not classical \"\n   \"Latin but a Late/Vulgar Latin denominative -- what Latin actually borrowed from Greek is the noun stuppa.\"),\n \"derivation_fa\": (\"خودِ اشتقاق درست است: یونانی στύππη به لاتینی به صورت اسم stuppa/stupa «الیاف زبر کتان» وام گرفته شد (در لاتینی \"\n   \"کلاسیک، مثلاً نزد پلینیوس) و از آن در لاتینی عامیانه/قرون‌وسطایی فعل *stuppāre «با الیاف کتان بستن، درز گرفتن» ساخته شد که \"\n   \"ایتالیایی stoppare، پرووانسی کهن estopar و فرانسوی کهن estoper از آن است. کلاین در مدخل stop همین زنجیره را می‌آورد. دو نکته: \"\n   \"نخست آنکه معنای انگلیسیِ نوشته‌شده باز هم «toe» است به جای «tow» — بررسی تصویر صفحهٔ چاپی نشان داد که خطای چاپی خودِ کتاب است نه \"\n   \"خطای خوانش اسکن؛ دوم آنکه stuppāre لاتینیِ کلاسیک نیست بلکه ساختهٔ لاتینی عامیانه است و آنچه لاتینی از یونانی وام گرفت اسمِ \"\n   \"stuppa بود. خطای چاپی کتاب.\"),\n \"sources\": [\"https://www.etymonline.com/word/stop\"],\n \"ref_check\": [\n   {\"ref\": \"AHD\", \"status\": \"partial\",\n    \"note\": \"Watkins s.v. steu(e)- takes Greek stuppe straight to the English keywords 'STOP, STUPE' without spelling out the Latin verb; the gloss he gives for stuppe is 'tuft, tow' (not 'toe').\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. stop (KLN_1966.txt l. 36906) and estop (l. 13692)\", \"stance\": \"supports\",\n    \"note\": \"'These words derive fr. ML. stuppare, \\\"to stop with tow\\\" (whence also It. stoppare, OProvenc. estopar, F. etouper, \\\"to stop with tow\\\"), fr. L. stuppa, stupa, \\\"the coarse part of flax, tow\\\", fr. Gk. stuppe'.\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.v. Stop (SKT.txt l. 18623)\", \"stance\": \"supports\",\n    \"note\": \"'Ital. stoppare, to stop up with tow. Low L. stupare, to stop up with tow, cram, stop. All from L. stupa, stuppa, coarse part of flax, hards, oakum, tow. Cf. Gk. stupe, stuppe, the same; Skt. stumbh, to stop.'\"},\n   {\"src\": \"POK\", \"where\": \"POK 1035\", \"stance\": \"supports\",\n    \"note\": \"'gr. *stupe, stuppe \\\"oakum\\\" (out of it Latin stupa, stuppa ds)' -- the Greek > Latin borrowing of the noun.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"English\", \"words\": \"stop, stuff\",\n \"verdict\": \"plausible\",\n \"derivation\": (\"STOP is confirmed: ME stoppen < OE forstoppian 'to stop up, stifle', related to MLG/Dutch stoppen and OHG stopfon, \"\n   \"all early Germanic borrowings of Vulgar/Medieval Latin *stuppare 'to stop or stuff with tow' (Klein 1966 s.v. stop; Skeat s.v. \"\n   \"Stop; Etymonline gives the same chain, noting Barnhart's minority view that the Germanic group 'might be native, from a native \"\n   \"base *stoppon'). STUFF is contested. Skeat derives it straight from the Latin word ('O.F. estofe ... -- L. stupa, stuppa, the \"\n   \"coarse part of flax, hards, tow; the pronunciation of this L. word being Germanised before it passed into French (Diez)'), and \"\n   \"Buck (Dict. of Selected Synonyms 6.21) likewise: 'It. stoffa, Fr. etoffe ... fr. the Gmc. word seen in NHG Stoff, this fr. Lat. \"\n   \"stuppa \\\"coarse linen, tow\\\", fr. Grk. stuppe (perh. : Skt. stupa- \\\"tuft of hair\\\", Walde-P. 2.620)'. But Klein 1971 rejects it \"\n   \"flatly -- 'The derivation of OF. estoffe, etc., fr. L. stuppa, \\\"tow\\\", occurring in most etymological dictionaries, must be \"\n   \"rejected' -- and derives stuff instead from Greek stuphein 'to contract' (IE *stu-bh-, i.e. still the same root family, \"\n   \"different branch); Etymonline/OED leave the source uncertain, with Old High German stopfon or a Frankish word as the usual \"\n   \"alternative. So Nourai's box is right for stop and only half-right for stuff. Note also that the English words descend from the \"\n   \"Vulgar/Medieval Latin verb via Germanic and Old French, not directly from Latin as the single arrow suggests.\"),\n \"derivation_fa\": (\"«stop» بی‌گمان است: انگلیسی میانه stoppen از انگلیسی کهن forstoppian «بستن، درز گرفتن»، هم‌خانوادهٔ آلمانی سفلای \"\n   \"میانه stoppen و آلمانی علیای کهن stopfōn، که همگی وام‌گیری کهن ژرمنی از لاتینی عامیانه *stuppāre «با الیاف کتان بستن» اند (کلاین، \"\n   \"اسکیت، اتیمانلاین). اما «stuff» محل اختلاف است: اسکیت آن را یکسره از لاتینی stuppa می‌گیرد (فرانسوی کهن estofe) و باک نیز همین \"\n   \"را می‌گوید (ایتالیایی stoffa، فرانسوی étoffe از واژهٔ ژرمنیِ Stoff، آن هم از لاتینی stuppa از یونانی στύππη)؛ ولی کلاین در \"\n   \"ویرایش ۱۹۷۱ آن را صریحاً رد می‌کند («این اشتقاق باید رد شود») و stuff را از یونانی στύφω «به هم فشردن» می‌داند، و اتیمانلاین و \"\n   \"فرهنگ آکسفورد خاستگاه آن را نامعلوم می‌گذارند و بیشتر به stopfōn ژرمنی می‌گرایند. پس نمودار برای «stop» درست و برای «stuff» \"\n   \"نیم‌درست است؛ افزون بر این، راه انتقال از لاتینی به انگلیسی از میان ژرمنی و فرانسوی کهن گذشته است، نه مستقیم. \"\n   \"با احتیاط پذیرفتنی است.\"),\n \"sources\": [\"https://www.etymonline.com/word/stop\", \"https://www.etymonline.com/word/stuff\"],\n \"ref_check\": [\n   {\"ref\": \"None\", \"status\": \"not_checked\",\n    \"note\": \"the node carries no reference in the book (refs=None); the claim was checked against Klein, Skeat, Buck and Etymonline instead.\"}\n ],\n \"consulted\": [\n   {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. stop (l. 36906); Klein 1971 s.v. stuff, n. (KLN_1971.txt ll. 234575-234587)\", \"stance\": \"partial\",\n    \"note\": \"supports stop ('fr. ML. stuppare ... fr. L. stuppa ... fr. Gk. stuppe'); contradicts stuff ('The derivation of OF. estoffe, etc., fr. L. stuppa, \\\"tow\\\", occurring in most etymological dictionaries, must be rejected'; he derives it 'ult. fr. Gk. stuphein, \\\"to contract\\\", fr. I.-E. base *stu-bh-').\"},\n   {\"src\": \"SKT\", \"where\": \"Skeat s.vv. Stop and Stuff (SKT.txt ll. 18623, 18735)\", \"stance\": \"supports\",\n    \"note\": \"'Stuff, materials. (F.-L.) O.F. estofe ... -- L. stupa, stuppa, the coarse part of flax, hards, tow ... The sense of the L. word is better preserved in the verb to stuff, i.e. to cram, to stop up ... from Low L. stuppare, to stop up; whence also E. Stop.'\"},\n   {\"src\": \"SYN\", \"where\": \"Buck 6.21 (SYN.txt l. 9953)\", \"stance\": \"supports\",\n    \"note\": \"'It. stoffa, Fr. etoffe (Sp. estofa), Rum. stofa, fr. the Gmc. word seen in NHG Stoff, this fr. Lat. stuppa \\\"coarse linen, tow\\\", fr. Grk. stuppe ... This is preferable to the usual deriv. of Gmc. fr. Romance ... REW 8332.'\"},\n   {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. steu(e)-\", \"stance\": \"partial\",\n    \"note\": \"lists 'STOP, STUPE' under Greek stuppe but does NOT list STUFF anywhere under the root.\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\n\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-482.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/build-482.py"
}
```


### [2026-09-14T03:29:40.941Z] TOOL RESULT

```
written
```


## [2026-09-14T03:29:44.680Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 -m json.tool data/verification/page-482.json > /dev/null && echo \"JSON OK\"; python3 tools/verify_check.py 482"
}
```


### [2026-09-14T03:29:45.952Z] TOOL RESULT

```
JSON OK
nodes verified: 17/17
node verdicts: {'disputed': 3, 'confirmed': 9, 'plausible': 3, 'transcription_suspect': 2}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 8, 'supports': 12, 'not_checked': 3}
books consulted: {'contradicts': 5, 'silent': 5, 'partial': 8, 'supports': 37} | by book: {'POK': 7, 'WLD': 7, 'KLN': 7, 'CHEUNG': 5, 'MON': 4, 'PHD': 3, 'NYB': 3, 'HRN': 3, 'SKT': 3, 'IEC': 2, 'AHD': 2, 'HJB': 2, 'SYN': 2, 'TTS': 2, 'BRT': 1, 'KNT': 1, 'LKT': 1}
```


## [2026-09-14T03:29:52.717Z] TOOL CALL #104: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; python3 - <<'EOF'\nimport json\nd=json.load(open('data/verification/page-482.json',encoding='utf-8'))\nbad=[]\nfor e in d['entries']:\n    if not e.get('note_fa'): bad.append(('entry',e['entry'],'note_fa'))\n    for k in ('ref_check','consulted','sources','note'):\n        if k not in e: bad.append(('entry',e['entry'],k))\n    for n in e['nodes']:\n        for k in ('derivation','derivation_fa','ref_check','consulted','verdict','lang','words','sources'):\n            if not n.get(k) and k!='sources': bad.append((e['entry'],n['id'],k))\n        if n['verdict']=='transcription_suspect':\n            for k in ('error_in','book_prints','correct_form'):\n                if not n.get(k): bad.append((e['entry'],n['id'],k))\nprint('missing:',bad)\nprint('bytes', open('data/verification/page-482.json','rb').read()[:3])\nEOF"
}
```


### [2026-09-14T03:29:53.773Z] TOOL RESULT

```
missing: []
bytes b'{\n '
```


## [2026-09-14T03:29:54.245Z] AGENT

You've hit your session limit · resets 2:50am (America/Toronto)
