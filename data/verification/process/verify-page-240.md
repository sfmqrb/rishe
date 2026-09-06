# Verification process log — verify-page-240


## [2026-09-06T15:45:20.170Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 240 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-240.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-240.json. Write /home/sfmqrb/git/rishe/data/verification/page-240.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 240` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T15:45:21.883Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T15:45:22.577Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T15:45:22.591Z] TOOL RESULT

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


## [2026-09-06T15:45:22.940Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-240.txt"
}
```


### [2026-09-06T15:45:22.960Z] TOOL RESULT

```
1	=== PDF page 240 (book page 210) ===
2	--- entry 0 ---
3	ROOT [Akkadian] Kânŭnu : fireplace  (refs MON:2875; BQT:1580)
4	#1 (parent #0) [Syriac] refs=MON:2875 | 
5	  #2 (parent #1) [Arabic] refs=MON:2875 | 
6	    #3 (parent #2) [Persian] refs=BQT:1580; MON:2875 | kânŭn «کانون ۱» : fireplace, hart
7	--- entry 1 ---
8	ROOT [Indo-European] Kap, Qap : grasp  (refs POK:527)
9	#1 (parent #0) [Old Persian] refs=BQT:636 | čifsati : attach
10	  #2 (parent #1) [Persian] refs=POK:527; HRN:98; IEC:473 | časbîdan «چسبیدن» : to attach | extra: چسپیدن ، چپسیدن ، چفسیدن ، چسب
11	#3 (parent #0) [Old Persian] refs=POK:527; HUB:89 | kapithe : a box for measuring grain
12	  #4 (parent #3) [Pahlavi] refs=MON:3010 | kapîč
13	    #5 (parent #4) [Persian] refs=MON:3010 | kavîz «کویز» : a measure of capacity | extra: کویژ ، کفیز ، قفیز
14	#6 (parent #0) [Greek] refs=None | kapsa : box, cage
15	  #7 (parent #6) [Arabic] refs=MON:2700 | 
16	    #8 (parent #7) [Persian] refs=BQT:1534 | qafas «قفس» : cage
17	#9 (parent #0) [Latin] refs=POK:524 | capere : to take ; capsa : case, box ; for-ceps : fire tongs ☞Gwher
18	  #10 (parent #9) [French] refs=None | 
19	    #11 (parent #10) [Persian] refs=MON:1997,2777,2896 |  | extra: کپسول ، کابل ، شاسی
20	    #12 (parent #10) [English] refs=AHD | case, capsule, cable, chassis ; catch, receive, deceive, forceps | NOTE: See root "Habl: rope" for another possible root for "cable".
21	  #13 (parent #9) [English] refs=AHD | capstan, caption, captive, accept, except
22	#14 (parent #0) [Germanic] refs=AHD | hâben : to have ; hafigaz : containing something, heavy
23	  #15 (parent #14) [English] refs=None | have, heavy
24	--- entry 2 ---
25	ROOT [Old Persian / Avestan] Kapastay, Kapasti : poison, a bitter plant  (refs BRT:436)
26	#1 (parent #0) [Pahlavi] refs=HRN:187 | kapast : poison
27	  #2 (parent #1) [Persian] refs=BQT:1588 | kabast «کَبست» : poison | extra: کَبستو
28	
```


## [2026-09-06T15:45:26.032Z] AGENT

I'll start by reading the source JSON and the reference infrastructure.


## [2026-09-06T15:45:27.454Z] TOOL CALL #3: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-240.json | head -200",
 "description": "Read page 240 source JSON"
}
```


## [2026-09-06T15:45:27.925Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-06T15:45:29.292Z] TOOL RESULT

```
{
    "pdf_page": 240,
    "book_page": 210,
    "entries": [
        {
            "root": {
                "name": "K\u00e2n\u016dnu",
                "lang": "Akkadian",
                "refs": "MON:2875; BQT:1580",
                "gloss": "fireplace"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Syriac",
                    "refs": "MON:2875",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 2,
                    "parent": 1,
                    "lang": "Arabic",
                    "refs": "MON:2875",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 2,
                    "lang": "Persian",
                    "refs": "BQT:1580; MON:2875",
                    "words": [
                        {
                            "translit": "k\u00e2n\u016dn",
                            "gloss": "fireplace, hart",
                            "script": "\u06a9\u0627\u0646\u0648\u0646 \u06f1"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": {
                        "text": "\u0686\u0648 \u06af\u06cc\u0631\u062f \u0622\u062a\u0634 \u062e\u0634\u0645 \u062a\u0648 \u0628\u0627\u0644\u0627 - \u0646\u06cc\u0627\u0628\u062f \u0627\u0632 \u062f\u0648 \u0639\u0627\u0644\u0645 \u0646\u06cc\u0645 \u06a9\u0627\u0646\u0648\u0646",
                        "poet": "Anvar\u00ee"
                    }
                }
            ]
        },
        {
            "root": {
                "name": "Kap, Qap",
                "lang": "Indo-European",
                "refs": "POK:527",
                "gloss": "grasp"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "BQT:636",
                    "words": [
                        {
                            "translit": "\u010difsati",
                            "gloss": "attach",
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
                    "refs": "POK:527; HRN:98; IEC:473",
                    "words": [
                        {
                            "translit": "\u010dasb\u00eedan",
                            "gloss": "to attach",
                            "script": "\u0686\u0633\u0628\u06cc\u062f\u0646"
                        }
                    ],
                    "script_extra": "\u0686\u0633\u067e\u06cc\u062f\u0646 \u060c \u0686\u067e\u0633\u06cc\u062f\u0646 \u060c \u0686\u0641\u0633\u06cc\u062f\u0646 \u060c \u0686\u0633\u0628",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 3,
                    "parent": 0,
                    "lang": "Old Persian",
                    "refs": "POK:527; HUB:89",
                    "words": [
                        {
                            "translit": "kapithe",
                            "gloss": "a box for measuring grain",
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
                    "lang": "Pahlavi",
                    "refs": "MON:3010",
                    "words": [
                        {
                            "translit": "kap\u00ee\u010d",
                            "gloss": null,
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
                    "lang": "Persian",
                    "refs": "MON:3010",
                    "words": [
                        {
                            "translit": "kav\u00eez",
                            "gloss": "a measure of capacity",
                            "script": "\u06a9\u0648\u06cc\u0632"
                        }
                    ],
                    "script_extra": "\u06a9\u0648\u06cc\u0698 \u060c \u06a9\u0641\u06cc\u0632 \u060c \u0642\u0641\u06cc\u0632",
                    "note": null,
                    "quote": null
                },
                {
                    "id": 6,
                    "parent": 0,
                    "lang": "Greek",
                    "refs": null,
                    "words": [
                        {
                            "translit": "kapsa",
                            "gloss": "box, cage",
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
                    "lang": "Arabic",
                    "refs": "MON:2700",
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 8,
                    "parent": 7,
                    "lang": "Persian",
                    "refs": "BQT:1534",
                    "words": [
                        {
                            "translit": "qafas",
                            "gloss": "cage",
                            "script": "\u0642\u0641\u0633"
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 9,
                    "parent": 0,
                    "lang": "Latin",
                    "refs": "POK:524",
                    "words": [
                        {
                            "translit": "capere",
                            "gloss": "to take",
                            "script": null
                        },
                        {
                            "translit": "capsa",
                            "gloss": "case, box",
                            "script": null
                        },
                        {
```


### [2026-09-06T15:45:29.329Z] TOOL RESULT

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


## [2026-09-06T15:45:38.113Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -m json.tool data/extracted/batch/page-240.json | sed -n '200,400p'",
 "description": "Rest of page 240 JSON"
}
```


## [2026-09-06T15:45:39.571Z] TOOL CALL #6: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['MON','BQT','POK','HRN','IEC','HUB','AHD','BRT','PHD','KLN','AKD']:\n    print(k, json.dumps(d.get(k),ensure_ascii=False)[:700]); print()\n\"",
 "description": "Ref lookup hints"
}
```


### [2026-09-06T15:45:39.940Z] TOOL RESULT

```
                        {
                            "translit": "for-ceps",
                            "gloss": "fire tongs",
                            "script": null,
                            "see": [
                                "Gwher"
                            ]
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 10,
                    "parent": 9,
                    "lang": "French",
                    "refs": null,
                    "words": [],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 11,
                    "parent": 10,
                    "lang": "Persian",
                    "refs": "MON:1997,2777,2896",
                    "words": [],
                    "script_extra": "\u06a9\u067e\u0633\u0648\u0644 \u060c \u06a9\u0627\u0628\u0644 \u060c \u0634\u0627\u0633\u06cc",
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
                            "translit": "case, capsule, cable, chassis",
                            "gloss": null,
                            "script": null
                        },
                        {
                            "translit": "catch, receive, deceive, forceps",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": "See root \"Habl: rope\" for another possible root for \"cable\".",
                    "quote": null
                },
                {
                    "id": 13,
                    "parent": 9,
                    "lang": "English",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "capstan, caption, captive, accept, except",
                            "gloss": null,
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 14,
                    "parent": 0,
                    "lang": "Germanic",
                    "refs": "AHD",
                    "words": [
                        {
                            "translit": "h\u00e2ben",
                            "gloss": "to have",
                            "script": null
                        },
                        {
                            "translit": "hafigaz",
                            "gloss": "containing something, heavy",
                            "script": null
                        }
                    ],
                    "script_extra": null,
                    "note": null,
                    "quote": null
                },
                {
                    "id": 15,
                    "parent": 14,
                    "lang": "English",
                    "refs": null,
                    "words": [
                        {
                            "translit": "have, heavy",
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
                "name": "Kapastay, Kapasti",
                "lang": "Old Persian / Avestan",
                "refs": "BRT:436",
                "gloss": "poison, a bitter plant"
            },
            "nodes": [
                {
                    "id": 1,
                    "parent": 0,
                    "lang": "Pahlavi",
                    "refs": "HRN:187",
                    "words": [
                        {
                            "translit": "kapast",
                            "gloss": "poison",
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
                    "refs": "BQT:1588",
                    "words": [
                        {
                            "translit": "kabast",
                            "gloss": "poison",
                            "script": "\u06a9\u064e\u0628\u0633\u062a"
                        }
                    ],
                    "script_extra": "\u06a9\u064e\u0628\u0633\u062a\u0648",
                    "note": null,
                    "quote": {
                        "text": "\u0686\u0631\u0627 \u06a9\u0634\u062a \u0628\u0627\u06cc\u062f \u062f\u0631\u062e\u062a\u06cc \u0628\u062f\u0633\u062a - \u06a9\u0647 \u0628\u0627\u0631\u0634 \u0628\u0648\u062f \u0632\u0647\u0631 \u0648 \u0628\u06cc\u062e\u0634 \u06a9\u0628\u0633\u062a",
                        "poet": "Ferdows\u00ee"
                    }
                }
            ]
        }
    ]
}
```


### [2026-09-06T15:45:41.489Z] TOOL RESULT

```
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol 

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.c

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index 

HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the 

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstruct

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by parag

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifie

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between 

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<ident

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO pri

AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by semantic field; Akkadia
```


## [2026-09-06T15:45:46.653Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\n# POK page 527 -> POK_01 leaf = p+8 = 535\nawk 'BEGIN{RS=\"\\f\"} NR==536' POK_01.txt | head -80",
 "description": "Pokorny p.527"
}
```


## [2026-09-06T15:45:47.930Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"kap-, kəp-\\|kap-, kap-\\|^kap-\" POK_full.txt | head -20; echo ---; grep -n \"kap-\" AHD_watkins1985.txt | head -20",
 "description": "Grep Pokorny full and AHD for kap-"
}
```


### [2026-09-06T15:45:48.486Z] TOOL RESULT

```
(Bash completed with no output)
```


### [2026-09-06T15:45:48.562Z] TOOL RESULT

```
44234:Root / lemma: kap-, kap- 
---
502:ghabh-. Also ghebh-. To give or receive. 1. Form *ghebh- in Germanic *geban in: a. Old English giefan, to give: GIVE; b. compound *far-geban (*far-, away; see per'), to give away, in Old English forgi(e)fan, to give, give up, leave off (anger), remit, forgive: FORGIVE. 2. Suf- fixed form *ghebh-ti-, something given (or received), in Germanic “giftiz in Old Norse gipt, gift, a gift: GIFT. 3. O-grade form “*ghobh- in Germanic *gab-ulam, some- thing paid (or received), in Old English gafol, tribute, tax, debt: GAVEL2. 4. Form *ghabh-é- in: a. Latin habére, to hold, possess, have, handle (> habitdre, to dwell): ABLE, BINNACLE, HABILE, HABIT, HABITABLE, (HABI- TANT), (HABITAT); (COHABIT), EXHIBIT, INHABIT, IN- HIBIT, PREBEND, PROHIBIT, (PROVENDER); b. Latin débére (dé-, away from; see de-; third person plural present passive debentur), to owe: DEBENTURE, (DEBIT), DEBT, DEVOIR, DUE, (DUTY); (ENDEAVOR). Compare kap-. [Pok. ghebh- 407.]
547:brand, piece of burning wood, sword: BRAND; b. Old Norse brandr, piece of burning wood, akin (in the sense “blackened by fire,” dark-colored) to the possible Scandi- navian source of Middle English brende, brindled: BRIN- DLED; c. Dutch branden, to burn, distill: BRANDY; d. Old French brand, sword: BRANDISH. 3. Suffixed form *gvher-mo- in Greek thermos, warm, hot (> thermé, heat): THERM, -THERM, THERMO-, -THERMY; HYPOTHER- iA. 4. O-grade form *gvhor- in Latin forceps, pincers, fire tongs (< “that which holds hot things”; -ceps, agential suffix, “-taker”; see kap-): FORCEPS, FORCIPATE. 5. Suffixed o-grade form gvhor-no- in: a. Latin fornus, fornéx, oven: FORNAX, FURNACE, HORNITO; b. probably Latin fornix, arch, vault (< “vaulted brick oven”): FORNICATE. [Pok. g¢her- 493, bhereu- 143.]
581:BIT), GAMBOL, (GAMBREL), (GAMMON3), (JAMB). 2. Suf- fixed form *kamp-ulo- in Greek kampulos, bent: CAMPYLOTROPOUS. [Pok. kam-p- 525.] kan-. To sing. 1. Germanic *han(e)ni in Old English hen(n), hen: HEN. 2. Latin canere, to sing (> cantdre, to sing): CANOROUS, CANT?, CANTABILE, CANTICLE, CANTIL- LATE, (CANTO), CANTOR, CANZONE, CHANT; ACCENT, DESCANT, ENCHANT, (INCANTATION), INCENTIVE, PRE- CENTOR, RECANT. 3. Latin oscen, a singing bird used in divination (< *obs-cen, “one that sings before the au- gurs”; ob-, before; see epi): OSCINE. 4. Suffixed form *kan-men- in Latin carmen, song, poem: CHARM}. [Pok. kan- 525.] kand-. To shine. 1. Suffixed (stative) form *kand-é- in Latin candére, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. 2. Latin transitive *candere, to kindle, in compound incendere, to set fire to, kindle (in-, in; see en): (INCENDIARY), IN- CENSE. [Pok. kand- 526.] kannabis. Hemp. Late Indo-European word borrowed from an unknown source. 1. Germanic *hanipiz in Old English henep, henep, hemp: HEMP. 2. Greek kannabis, hemp: CANNABIS, (CANVAS). kanto-. A corner, a bending. Celtic *cantos, rim, border, in Latin cantus, canthus, iron ring around a carriage wheel, a wheel, rim (> Italian canto, corner): CANTEEN, CANTON; DECANT. [Pok. kan-tho- 526.] kap-. To grasp. I. Basic form *kap-. 1. Germanic *haf- in Old English hefeld, thread used for weaving, heddle (a device which grasps the thread): HEDDLE. 2. Germanic *haftjam in Old English heft, handle: Harr. 3. Form *kap-o- in Germanic *habai-, *habén in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, “containing something,” having weight, in Old English hefig, heavy: HEAVY. 5. Germanic *hafnd-, perhaps “place that holds ships,” in Old English hefen, a haven: HAVEN. 6. Germanic habukaz in Old English h(e)afoc, hawk: HAWK}, 7, Latin combining form -ceps (< *kap-s), “taker.” II. Suffixed form *kap-yo-. 1. Germanic *hafjan in Old English hebban, to lift: HEAVE. 2. Latin capere, to take, seize, catch: CABLE, CAPABLE, CAPACIOUS, CAPIAS, CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAP- TOR, CAPTURE, CATCH, (CHASE!); ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT, INCEPTION, (INCIPIENT), INTERCEPT, INTUSSUSCEPTION, MUNICIPAL, NUNCUPA- TIVE, OCCUPY, PARTICIPATE, PERCEIVE, PRECEPT, RE- CEIVE, (RECOVER), RECUPERATE, (RX), SUSCEPTIBLE. III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE2, CHASE?, CHASES, CHASSIS, CHESS?; ENCHASE. IV. Length- ened-grade variant form *kdép-. 1. Germanic *hof- in compound *bi-hdf, “that which binds,” requirement, obligation (*bi-, intensive prefix; see ambhi), in: a. Old English behdf, use, profit, need: BEHOOF; b. Old English behéfian, to have need of: BEHOOVE. 2. Greek k6pé, oar, handle: copePpop. Compare ghabh-. [Pok. kap- 527.] kap(h)o-. Hoof. Lengthened-grade form kdp(h)-o- in Germanic *héfaz in Old English Adf, hoof: Hoor. [Pok. kapho- 530.] kapro-. He-goat, buck. Latin caper, he-goat (> capra, she-goat): CABRILLA, CABRIOLET, CAPELLA, CAPRIOLE, CHEVRON; CAPRIC ACID, CAPRICORN, CAPRIFIG, CAPROIC ACID. [Pok. kapro- 529.] kaput. Head. 1. Germanic *haubidam, *haubudam, in Old English héafod, head: HEAD. 2. Latin caput, head (> Italian capo, head): CABEZON, CADET, CAPE?, CAPITAL, CAPITAL, CAPITATE, CAPITATION, CAPITELLUM, CAPITU- LATE, CAPITULUM, CAPO!, CAPRICE, CAPTAIN, CATTLE, CAUDILLO, CHAPITER, CHAPTER, CHIEF, CHIEFTAIN; BI- CEPS, CHAMFRON, DECAPITATE, KERCHIEF, MISCHIEF, OCCIPUT, PRECIPITATE, RECAPITULATE, SINCIPUT, TRI- ceps. [Pok. kap-ut- 529.] kar-', Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English hard,
723:man-?, Hand. 1. Latin manus, hand: MANACLE, MANAGE, (MANEGE), MANNER, MANUAL, MANUBRIUM, MANUS; AMANUENSIS, MAINTAIN, MANEUVER, MANICOTTI, MANI- CURE, MANIFEST, MANIPLE, MANIPULATION, MANSUE- TUDE, MANUFACTURE, MANUMIT, MANURE, MANUSCRIPT, MASTIFF, MORTMAIN, QUADRUMANOUS. 2. Suffixed form *man-ko-, maimed in the hand, in Latin mancus, maimed, defective: MANQUE. 3. Latin compound man- ceps, “he who takes by the hand” (-ceps, agential suffix, “taker”; see kap-), purchaser: EMANCIPATE. 4. Latin compound manddre, “to give into someone’s hand” (dare, to give; see d6-), entrust, order: MANDAMUS, MANDATE; COMMAND, (COMMANDO), COMMEND, COUN- TERMAND, DEMAND, RECOMMEND, REMAND. [Pok. ma-r- 740.]
839:parative) form *pro-tero- in Greek proteros, before, former: HYSTERON PROTERON, PROTEROZOIC. VI. Exten- ded forms *prai-, *prei-. 1. Latin prae, before: PRE-; PRETERIT. 2. Suffixed (comparative) form *prei-yos- in Latin prior, former, higher, superior: PRIOR2. 3. Suffixed form *prei-wo- in: a. Latin privus, single, alone (< “standing in front,” “isolated from others”): PRIVATE, PRIVILEGE, PRIVITY, PRIVY; DEPRIVE; b. Latin proprius, one’s own, particular (< pré priv6, in particular, from the ablative of privus, single): PROPER, PROPERTY; APPRO- PRIATE, PROPRIOCEPTION, PROPRIOCEPTOR. 4. Extended form *preis- in: a. suffixed (superlative) form *preis-mo in (i) Latin primus (< *prismus; ablative plural primis), first, foremost: PREMIER, PRIMAL, PRIMARY, PRIMATE, PRIME, PRIMITIVE, PRIMO, PRIMUS; IMPRIMIS, PRIMA FACIE, PRIMAVERA, PRIMEVAL, PRIMIPARA, PRIMOGENI- TOR, PRIMOGENITURE, PRIMORDIAL (ii) Latin compound princeps, “he who takes first place” (-ceps, “-taker”; see kap-), leader, chief, emperor: PRINCE, PRINCIPAL, PRIN- CIPLE; b. suffixed form *preis-tano- in Latin pristinus, former, earlier, original: PRISTINE. VII. Extended form *pres- in compound “*pres-g“u-, “going before” (*gvu-, to go; see gWa-), in Greek presbus, old, old man, elder: PRESBYTER, (PRIEST); PRESBYOPIA. VIII. Extended form *proti in Greek pros, against, toward, near, at: PROS-; PROSOPOPEIA. Other possibly related forms are grouped under per-2, per-3, per-4, per-5, and per-’. [Pok. 2. A. per 810.] per-?. To lead, pass over. A verbal root belonging to the group of per’. I. Full-grade form *per-. 1. Suffixed form *per-tu-s in Germanic “*ferthuz, place for crossing over, ford, in Old Norse fjérdhr, an inlet, estuary: FIRTH, FJORD. 2. Suffixed form *per-ond in Greek peroné, pin of a brooch, buckle (< “that which pierces through”): PERONEAL. II. O-grade form *por-. 1. Germanic *faran, to go, in: a. Old English faran (> Middle English faren), to go on a journey, get along: FARE; WAYFARER, WAY- FARING, (WELFARE); b. Old High German faran, to go, travel: GABERDINE. 2. Suffixed form *por-o-, passage, journey, in Greek poros, journey, passage: PORE”; EMPO- RIUM, POROMERIC. 3. Suffixed (causative) form *por- eyo-, to cause to go, lead, conduct, in Germanic *farjan, to ferry, in Old English ferian, to transport: FERRY. 4. Lengthened-grade form *pdér- in: a. Germanic suffixed form *f6r-ja- in Old English (ge)féra, “fellow-traveler,” companion (ge-, together, with; see kom): FERE; b. Ger- manic suffixed (causative) form *fér-jan in Old High German fuoren, to lead: FUHRER. 5. Possibly suffixed form *por-no-, feather, wing (< “that which carries a bird in flight”), in: a. Germanic *farnd, feather, leaf, in Old English fearn, fern (having feathery fronds): FERN; b. Sanskrit parnam, leaf, feather: PAN2. III. Zero-grade form pr-. 1. Suffixed form *pr-tu-, passage, in: a. Ger- manic *furdu- in Old English ford, shallow place where one may cross a river: FORD; b. Latin portus, harbor (< “passage”): PORT!; IMPORTUNE, OPPORTUNE. 2. Suffixed form *pr-té in Latin porta, gate (> Old French porte, door): PORCH, PORT’, PORTAL, PORTCULLIS, PORTE-CO- CHERE, PORTER®, PORTICO, PORTIERE, PORTULACA. 3. Suffixed (denominative) form *pr-to- in Latin portdre, to carry: PORTS, PORTABLE, PORTAGE, PORTAMENTO, PORTATIVE, PORTER}; COMPORT, DEPORT, EXPORT, IM- PORT, (IMPORTANT), PORTFOLIO, PURPORT, RAPPORT, REPORT, (SPORT), SUPPORT, TRANSPORT. [Pok. 2. B. per 816.]
938:skep-. Also kep-. Base of words with various technical meanings such as “to cut,” “to scrape,” “to hack.” 1. Germanic *skap- in: a. Old English gesceap (ge-, collective prefix; see kom), form, creation (< “cutting”): SHAPE; b. Old English -scipe, state, condition (collective suffix): -sHIP; c. Dutch -schap, “-ship,” condition (collec- tive suffix): LANDSCAPE. 2. Germanic ablaut variant *skOpo-, “thing cut out,” container, in Middle Dutch and Middle Low German schdépe, bucket for bailing water: scoop. 3. Germanic *skaftaz in Old English sceaft, rod of a spear: SHAFT! 4, Germanic expressive form *skabb- in: a. Old English sceabb, a scab, scratch: sHaBBy; b. Old Norse skabb, a scab: scaB. 5. Variant form *skabh- in: a. Germanic *skaban in (i) Old English sceafan, to scrape, pare away: SHAVE (ii) Old High German skaban, to scrape: SAPSAGO; b. Latin scabere, to scrape: SCABIES; c. suffixed form *skabh-ro- in Latin scaber, rough (< “scratched”’): SCABROUS; d. Greek skaphé, boat (< “thing cut out”): SCAPHOID; BATHYSCAPH. 6. Variant form *skap- in Latin scapula, shoulder blade (used as a tool for scraping): SCAPULA. 7. Variant form *kap- in: a. Latin capd, castrated cock: CAPON; b. Late Latin capuldre, to cut: SCABBLE. 8. O-grade form *kop- in: a. suffixed form *kop-yd- in Germanic *hapjo, a cutting tool, ax, sickle, in (i) Old High German hdppa, happa, sickle, akin to the Germanic source of Old Provencal apcha, small ax: PIOLET (ii) Medieval Latin hapia, ax, and Old French hache, small ax: HASH!, HATCHET; NUT- HATCH, QUEBRACHO; b. suffixed form *kop-yo- in Greek koptein, to strike, cut: COMMA; APOCOPE, SARCOPTIC MANGE, SYNCOPE; C. Russian kopat’, to hack, with de- rivative kop’e, lance, in kopeika, kopeck: KOPECK. 9. Pos- sibly zero-grade variant form *skup(h)- in Greek skuphos, a cup (but more likely of obscure origin): SCYPHISTOMA, SCYPHOZOAN. [Pok. 2. (s)kep- 931.] sker-!, Also ker-. To cut. I. Basic forms *sker-, *ker-. 1. Germanic *skeran in Old English scieran, sceran, to cut: SHEAR. 2. Germanic *skeraz in: a. Old English scéar, plowshare: SHARE?; b. Old English scearu, scaru, portion, division (but recorded only in the senses of “fork of the body,” “tonsure”): SHARE!. 3. Germanic *skér- in: a. *skér-6- and *sker-ez- in Old English scéar, scissors: SHEARS; b. compound *skér-berg-, “sword protector,” scabbard (see bhergh-') in Old High German scarberc, scabbard, akin to the possible Germanic source of Anglo- Norman escaubers, scabbard: SCABBARD. 4. Germanic *skur- in Old Norse skor, notch, tally, twenty: SCORE. 5. Germanic suffixed form *skar-jam in Old Norse sker, low reef (< “something cut off’’): scaR?. 6. Suffixed o-grade extended form *skord-o- in Germanic *skardaz in Old English sceard, a cut, notch: SHARD. 7. Extended form *skerd- in suffixed zero-grade form *skrd-o- in Germanic *skurtaz in: a. Old English scort, sceort, “cut,” short: SHORT; b. Old English scyrte, undergarment (< “cut piece”): SHIRT; c. Old Norse skyrta, shirt: SKIRT. 8. Germanic extended form *skerm- in: a. Old High German skirmen, to protect, akin to the source of Old French eskermir, to fight with a sword, fence: SKIRMISH; b. Middle Dutch scherm, shield: SCREEN. 9. Variant form *kar- in Latin caré (stem carn-), flesh: CARNAGE, CARNAL, CARNASSIAL, CARNATION, CARNIVAL, CARRION, CARUNCLE, CHARNEL, CRONE; CARNIVOROUS, INCAR- NATE. 10. Suffixed o-grade form *kor-yo- in Latin co- rium, leather (originally “piece of hide”): CORIACEOUS, CORIUM, CUIRASS, CURRIER; EXCORIATE. 11. Suffixed zero-grade form *kr-to- in Latin curtus, short: CURT, CURTAL, KIRTLE. 12. Suffixed o-grade form *kor-mo- in Greek kormos, a trimmed tree trunk: cor. 13. Suffixed o-grade form *kor-i- in Greek koris, bedbug (< “cutter”): corREopsis. II. Extended roots *skert-, *kert-. 1. Zero-grade form *krt- or o-grade form *kort- in Latin cortex, bark (< “that which can be cut off”): CORTEX; DECORTICATE. 2. Suffixed form *kert-snd- in Latin céna, meal (< “portion of food”): CENACLE. III. Extended root
1135:Old English war, seaweed: SEAWARE. 3. Suffixed zero-grade form *wi-ria- in Latin (of Celtic origin) viriae, bracelets: FERRULE. 4. Suffixed form *wei-ti- in Ger- manic *with- willow, in Old English withig, wiry: wITHY. 5. Suffixed zero-grade form *wi-t- in Germanic withj6n- in Old English withthe, supple twig: wITHE. II. Form *weia-, zero-grade *wi- (< *wia-). 1. Suffixed form *wi-ti- in Latin vitis, vine: VISE; VITICULTURE. 2. Suffixed form *wi-td- becoming *wittd in Latin vitta, headband: viTTA. 3. Suffixed form *wi-ri- probably in Greek iris, rainbow, and Iris, rainbow goddess: (IRIDACEOUS), IRIDO-, IRIS, IRIS; (IRIDIUM), (IRISITIS). 4. Suffixed form *wi-n- per- haps in Greek is (genitive inos), sinew: EXINE, INOSITOL, INOTROPIC. [Pok. 1. wei- 1120.] wei-?. To go after something. Suffixed o-grade form in Germanic *wai-thj6-, “pursuit,” with denominative *waithanjan, to hunt, plunder, in Old French gaaignier, gaigner, to obtain: GAIN}; ROWEN. [Pok. 3. wei- 1123.] wei-%. To wither. Extended form *weis- in Germanic *wis- in suffixed form *wis-n-6n in Old English wisnian, to wither, shrivel, shrink: wizEN. [Pok. 2. wei- 1123.] wei-*. Vice, fault, guilt. 1. Suffixed zero-grade form *wi-tio- in Latin vitium, fault, vice: vICE1, vICcIoUs, VITIATE. 2. Suffixed form “wi-tu- in: a. Latin vitiligo, tetter (< “blemish”): vITILIGO; b. Latin vituperdre, to abuse (perhaps formed after Latin recuperdre, to regain; see kap-): VITUPERATE. [Pok. 1. wi- 1175.] weid-. To see. I. Full-grade form *weid-. 1. Germanic *witan, to look after, guard, ascribe to, reproach, in: a. Old English witan, to reproach: Twit; b. Old Proven- gal guida, a guide: GUIDE; c. Germanic derivative noun *witi- in Old English wite, fine, penalty: WITE!. 2. Suf- fixed form *weid-to- in Germanic *wissaz in: a. Old English wis, wise: WISE!; b. Old English wisdém, learn- ing, wisdom (-d6ém, abstract suffix; see dhé-'): WISDOM; c. Old High German wissago, seer, prophet: WISEACRE; d. Germanic *wissdén-, appearance, form, manner, in (i) Old English wise, wis, manner: WISE? (ii) Old French guise, manner: GUISE. 3. Suffixed form *weid-es- in Greek eidos, form, shape: EIDETIC, EIDOLON, IDOL, IDYLL, -OID; IDOCRASE, KALEIDOSCOPE. 4. Perhaps Greek Haidés (also Aidés), the underworld, perhaps “the invisi- ble” (> French Hadés): HADAL, Hangs. II. Zero-grade form *wid-. 1.Germanic *wit- in: a. Old English wit, witt, knowledge, intelligence: wit}; b. Old English wita (genitive plural witena), wise man, councilor: WITENAGE- MOT. 2. Germanic *witan in Old English witan, to know: WIT2; UNWITTING. 3. Suffixed form *wid-to- in Germanic *wissaz, known, in Old English gewis, gewiss, certain, sure: IWIS. 4. Form *wid-é- (with participial form *weid-to-) in Latin vidére (past participle visus), to see, look: VIDE, VIEW, VISA, VISAGE, VISION, VISTA, VOYEUR; ADVICE, (ADVISE), BELVEDERE, CLAIRVOYANCE, ENVY, EVIDENT, INTERVIEW, PREVISE, PROVIDE, REVIEW, SU- PERVISE, SURVEY. 5. Suffixed form *wid-es-ya in Greek idea, appearance, form, idea: IDEA, IDEO-. 6. Suffixed form *wid-tor- in Greek histdr, wise, learned, learned man: HISTORY, (STORY!); POLYHISTOR. 7. Suffixed nasal- ized form *wi-n-d-no- in: a. Irish fionn, white (< “clearly visible”): COLCANNON; b. Welsh gwyn, gwynn, white: PENGUIN. 8. Celtic compound *dru-wid-, ““knower of trees” (*dru-, tree; see deru-). III. Suffixed o-grade form *woid-o- in Sanskrit vedah, knowledge: VEDA; RicG- VepaA. [Pok. 2. ufe)di- 1125.] weidh-. To divide, separate. 1. Suffixed zero-grade form *widh-ewo-, “bereft,” feminine *widh-ewd-, “woman separated (from her husband by death),” in Germanic *widuw6 in Old English widuwe, widow: wiDow. 2. Zero-grade form *widh- in Latin dividere, to separate (dis-, intensive prefix): DEVISE, DIVIDE, POINT-DEVICE. [Pok. weidh- 1127.] weie-. Vital force. Perhaps related to wi-ro-. Zero-grade form *wi- (< *wia-) in Latin vis, force, with irregular
1208:ABAFT apo- ABANDON bha-2 ABASE bassus ABASH bat- ABASIA gWa- ABATE battuere ABBREVIATE mregh-u- ABDICATE deik- ABDUCENS deuk- ABDUCT deuk- ABELE albho- ABERRATION ers-1 ABET bheid- ABEYANCE bat- ABHOR ghers- ABIDE bheidh- ABJECT yé- ABJURE yewes- ABLATION  tele- ABLAUT apo-, kleu-1 ABLE ghabh- ABLUTION leu(@)- ABNEGATE ne ABNORMAL gné- ABODE bheidh- ABOLISH al-3 ABORT er-! ABOUND wed-1 ABOUT ud- ABOVE upo ABRADE réd- ABRIDGE mregh-u- ABROGATE reg-1 ABROSIA gWere-4 ABRUPT reup- ABSCESS ked- ABSCISE kae-id- ABSCOND dhé-1 ABSENT eS- ABSOLUTE leu-1 ABSOLVE feu-1 ABSORB srebh- ABSTAIN ten- ABSTRACT tragh- ABSTRUSE treud- ABSURD swer-2 ABULIA gWele-1 ABUT bhau- ABYSS gWadh- ACANTHO- ak- ACANTHOPTERYGIAN pet- ACANTHUS ak- ACAPNIA kwép- ACCEDE ked- ACCELERATE kel-3 ACCENT kan- ACCEPT kap- ACCESS ked- ACCIDENT kad- ACCIPITER Oku- ACCLAIM kele-2 ACCLIVITY klel- ACCOLADE kwel-1 ACCOMMODATE med- ACCOMPLISH pele-1 ACCORD kerd-1 accosT kost- ACCOUNT peu- ACCRUE_ ker-3 ACCUMBENT keu-2 ACCUMULATE keue-2 ACCURATE cira ACERATE ak- ACERB ak- ACETABULUM ak- ACETIC ak- ACETUM = ak- ACHALASIA ghé-
1248:ANTIG ant- ANTICIPATE kap- ANTIDOTE d6- ANTINOMIAN nem- ANTINOMY nem- ANTIPASTO pa- ANTIPHON bha-2 ANTIPODES ped-1 ANTIQUE ant- ANTITHESIS dhé-1
1282:BEE? bheug-3 BEECH bhago- BEEF gWou- BEETLE! bheid- BEETLE? bhau- BEFALL p(h)ol- BEFORE pert BEGET ghend- BEHEST kei-3 BEHIND ko- BEHOOF kap- BEHOOVE kap- BELAY legh- BELCH bhel-4 BELDAM deu-2 BELEAGUER legh- BELEMNITE gWele-1
1328:CABARET kamer- CABEZON kaput CABLE kap- CABRILLA kapro- CABRIOLET kapro- CACHE ag- CACHEXIA segh- caco- kakka- CACODYL kakka- CACOETHES kakka-, s(w)e- CACOPHONOUS bha-2, kakka- CACOPHONY kakka- CACUMINAL keu-2 CADASTER  steigh- CADAVER kad- CADELLE kat-1 CADENCE kad- CADENT kad- CADET kaput CADRE kWetwer- CADUCEUS kar-2 CADUCICORN kad-, ker-1 CADUCOUS kad- CAECILIAN kaiko- CAECUM kaiko- CAELUM_ kae-id- CAESURA kae-id- CAGE keua-2 CAHIER kWetwer- CAINOTOPHOBIA ken-3 CAIRD kerd-2 CAISSON kap-
1334:CANDENT kand- CANDID kand- CANDIDA kand- CANDIDATE kand- CANDLE kand- CANDOR kand- CANESCENT kas- CANICULA kwon- CANINE kwon- CANKER kar-1 CANNABIS kannabis CANOROUS_ kan- CANT? kan- CANTABILE kan- CANTEEN kanto- CANTICLE kan- CANTILLATE kan- CANTO kan- CANTON kanto- CANTOR kan- CANVAS kannabis CANZONE kan- CAPABLE kap- CAPACIOUS kap- CAPE2 kaput CAPELLA kapro- CAPIAS kap- CAPITAL! kaput CAPITAL? kaput CAPITATE kaput CAPITATION kaput CAPITELLUM kaput CAPITULATE kaput CAPITULUM kaput CAPO! kaput CAPON skep- CAPRIC ACID kapro- CAPRICE kaput CAPRICORN kapro-, ker-1 CAPRIFIG kapro- CAPRIOLE kapro- CAPROIC ACID kapro- CAPSICUM kap- CAPSID kap- CAPSTAN kap- CAPSULE kap- CAPTAIN kaput CAPTION kap- CAPTIOUS kap- CAPTIVATE kap- CAPTIVE kap- CAPTOR kap- CAPTURE kap- CAR kers-2 CARAMEL kolem- CARAT ker-1 CARAVANSARY tere-2 CARBON ker-4 CARBUNCLE ker-4 CARCINO-  kar-1 CARCINOGEN kar-1 CARCINOMA kar-1 CARD? kars- CARDIA kerd-1 CARDIAC kerd-1 CARDIO- kerd-1 CARDOON kars- CARE gar- CAREEN kar-1 CAREER kers-2 CARESS ka- CARET kes-2 CARGO kers-2 CARICATURE kers-2 CARIES ker-5 CARILLON kWetwer- CARINA kar-1 CARIOLE kers-2 CARL karlaz CARLING karlaz CARMINATIVE kars- CARNAGE sker-1 CARNAL sker-1 CARNASSIAL_ sker-1 CARNATION sker-1 CARNET kWetwer- CARNIVAL legh-, sker-1 CARNIVOROUS = sker-1 CAROCHE kers-2 CAROL aulo- CAROTID ker-1 CAROUSE ud- CARP! ger-2 “CARP kerp- CARPAL kwerp- CARPEL kerp- CARPENTER kers-2 CARPET kerp- CARPO- kerp-
1336:CASE2 kap- CASHIER kes-2 CASTE kes-? CASTIGATE kes-2 CASTLE kes-2 CASTRATE kes-2 CATA- kat-1 CATABOLISM gWele-1 CATACHRESIS gher-5 CATACLYSM kleu-2 CATALECTIC slég- CATALEPSY (s)lag¥- CATALOGUE leg-1 CATALYSIS leu-1 CATAMENIA mé-2 CATAPLEXY plak-2 CATAPULT pél- CATARRH sreu- CATASTASIS sta- CATASTROPHE streb(h)- CATCH kap- CATCHPOLE pau- CATECHIZE (s)wagh- CATEGORY ger-1 CATER-CORNERED kWetwer- CATERPILLAR pilo- CATHEDRA sed-1 CATHEPSIN kat-1 CATHETER yé- CATHODE sed-2 CATHOLIC sol- CATION ei-1 CATOPTRIC okw- CATTLE kaput CAUDILLO kaput CAUDLE kele-1 CAULESCENT kaul- CAULICLE kaul- CAULIFLOWER _bhel-3, kaul- CAULINE kaul- CAUSTIC kéu- CAUTERY kéu- CAUTION keue-1 CAVE keue-2 CAVEAT keue-1 CAVERN keue-2 CAVETTO keue-2 CAVIL  kel-8
1345:CHASE! kap-
1346:CHASE2 kap-
1347:CHASES kap-
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1389:cons deuk- CONATION ken-1 CONCAVE keue-2 CONCEAL kel-2 CONCEDE ked- CONCEIVE kap- CONCERN krei- CONCESSION ked- CONCH konk(h)o- CONCHA konk(h)o- CONCHO- konk(h)o- CONCIERGE servus CONCILIATE kela-2 CONCISE kae-id- CONCLAVE kleu-3 CONCLUDE kleu-3 CONCOCT pekw- CONCOMITANT ei-1 CONCORD kerd-1 CONCOURSE kers-2 CONCRESCENCE ker-3 CONCRETE ker-3 CONCUBINE keu-2 CONCUPISCENCE kwép- CONCUR kers-2 CONCUSS kwét- CONDEMN dap- CONDENSE dens-2 CONDESCEND skand- CONDIGN dek-1 CONDIMENT dhé-1 CONDITION deik- CONDOLE del-3 CONDONE do- CONDOTTIERE deuk- CONDUCE deuk- CONDUCT deuk- CONDUPLICATE dwo- CONE k6-
1394:CONVOLVE wel-3 CONVULSE wel-4 cook pekw- cOoKY kak-2 cooL gel-3 COOPER ku- COOPERATE op-1 CO-OPT op-2 COORDINATION ar- COPE! kel-1 COPEPOD kap- COPIOUS op-1 COPRO- kekw- COPULA ap-! COPULATE ap-1 COPY op-1 CORACIIFORM ker-2, merph- CORACOID ker-2 CORBEL ker-2 CORBINA ker-2 CORD ghere- CORDATE kerd-1 CORDIAL kerd-1 CORDIFORM kerd-1 CORDON ghere- COREOPSIS sker-! CORGI kwon- CORIACEOUS sker-1 CORIUM §sker-1 cOoRM sker-! CORMORANT ker-2 CORN! gre-no- CORN2 ker-1 CORNEA ker-1 CORNEL ker-6 CORNEOUS ker-1 CORNER ker-1 CORNET ker-1 CORNICULATE ker-1 CORNIFICATION ker-1 CORNU_ ker-1 CORNUCOPIA op-! CORONA sker-3 CORONOID  sker-3 CORPORAL! kWrep- CORPORAL’ kWrep- CORPORATE kWrep- CORPOREAL kWrep- CORPOSANT kWrep-, sak- CORPS kWrep- CORPSE kWrep- CORPULENCE kWrep- CORPUS krep- CORPUSCLE kWrep- CORRADE réd- CORRECT reg-! CORRIDOR kers-2 CORRIE kWer-2 CORROBORATE reudh-! CORRODE réd- CORRUGATE ruk-2 CORRUPT reup- CORSAGE kWrep- CORSAIR kers-2 CORSE kWrep- CORSET kWrep- CORTEGE gher-1 CORTEX sker-1 CORUSCATE sker-2 CORVEE reg-! CORVINE ker-2 Corvus ker-2 CORYDALIS_ ker-1 CORYMB_ ker-1 CORYNEBACTERIUM bak-, ker-1 CORYPHAEUS_ ker-1 COSMONAUT nau-2 COSMOPOLITE pele-3 cosmos kes-3 cost sta-
1416:DECEIVE kap- DECEMBER dekm DECEMVIR dekm, wi-ro- DECENARY dekm DECENNIUM at-, dekm DECENT dek-! DECI- dekm DECIDE kae-id- DECIDUOUS _ kad- DECIMAL dekm DECIMATE dekm DECK! (s)teg- DECK? (s)teg- DECKLE (s)teg- DECLAIM kele-2 DECLARE kele-2 DECLINE klei- DECLIVITY kKlei- DECOCT pekw- DECOLLATE! kWwel-1 DECOLLETE kwel-1 DECOR dek-! DECORATE dek-1 DECOROUS dek-1 DECORTICATE sker-1 DECOY keue-2, to- DECREASE ker-3 DECREE krei- DECREPIT ker-2 DECREPITATE ker-2 DECUMBENT keu-2 DECUPLE dekm, pel-3 DECURRENT kers-2 DECUSSATE dekm DEDANS en DEDICATE deik- DEDUCE deuk- DEDUCT deuk- DEED dhé-1
```


## [2026-09-06T15:45:56.550Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '44230,44290p' POK_full.txt",
 "description": "Pokorny kap- entry"
}
```


### [2026-09-06T15:45:56.606Z] TOOL RESULT

```
inundation on the fields leaves behind ', sapas' stem, straw, bough'. 
References: WP. I 345, Specht Indo Germanic Dekl. 27. 
Page(s): 529 

Root / lemma: kap-, kap- 

Meaning: a piece of land 

Material: Gr. Kpnoc;, Doric kc(tto(; "garden', Hes. Konuc; Kpnoc; (Cretan " uncultivated small 

area of land', s. Gl. 3, 303); Old High German huoba. Old Saxon hoba^ a piece of land ', 

Modern High German Hufe, Hube, alb. /royos/?/© "garden'. 

References: WP. I 345, Specht Indo Germanic Dekl. 27, places here Old High German 

habaro etc. " oat '. 

See also: S. under under kapro- 

Page(s): 529 

Root / lemma: kar- 
Meaning: wax 

Material: Gr. kx\^6q, " wax ', Kripiov "honeycomb, a cutaneous disease', although Doric 
Kap6(; can be secure enough, out of Ion. -Attic are loanwords from this dialect group, Latin 
cera as gr. loanword; 

Lithuanian korys^ honeycomb, honeycomb of the bees'. 

In -dh- extention: 

Maybe {*kro-dh^ krodbe'beehWe'. 



Latvian karesHom. PI. ds.; 

poln. skarzyk'the thrust in tlie beehive'. 

References: WP. I 355, WH. I 202, Specht Indo Germanic Del<l. 52. 
Page(s): 532 

Root / lemma: kau(a)la : kula 

Meaning: abscess, boil 

Material: Gr. Ionian KriAri, Attic KoAri "swelling, lump, growth, esp. a tumor', poupojvoKnAri 

"hernia'; KaAa^si OYKOurai. Axaioi Hes., KaAaija o^koq, Hes. (Ionian Kv\kr\ from *mV-zK-a, 

Attic ach. KaA-r|, -a from KaF-sA-a?); 

Old Norse haull. Old English heala. Old High German holai. "hernia' {*kau[9]la, at most 
*kau[9]la)\ 

zero grade Church Slavic Ay/5"ds.'; russ. k/7a'6s.; knag in a tree', serb. k/7a6s.; 
Lithuanian dial, ku/ei. " hunch, outgrowth, knag'. 

References: WP. I 333, Trautmann 144.
```


## [2026-09-06T15:45:57.415Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; awk 'BEGIN{RS=\"\\f\"} NR==533' POK_01.txt | head -60; echo \"=== p527 leaf536 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==536' POK_01.txt | head -60",
 "description": "Pokorny printed pages 524 and 527"
}
```


### [2026-09-06T15:45:59.209Z] TOOL RESULT

```
=== p527 leaf536 ===
```


## [2026-09-06T15:46:03.137Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"Page(s): 527\" POK_full.txt | head; echo ---; grep -n \"Page(s): 524\" POK_full.txt | head",
 "description": "Find Pokorny pages 527 and 524"
}
```


### [2026-09-06T15:46:03.201Z] TOOL RESULT

```
43824:Page(s): 527-528 
---
43399:Page(s): 524 
43417:Page(s): 524 
43443:Page(s): 524-525 
44194:Page(s): 524
```


## [2026-09-06T15:46:05.115Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '43770,43830p' POK_full.txt",
 "description": "Pokorny 527-528 root entry"
}
```


### [2026-09-06T15:46:05.176Z] TOOL RESULT

```
purpose, benefit, advantage'. Modern High German Behuf' end, purpose, aim, goal '; 



[Old Norse haukr{ *hQbukr), Old English heafoc^ hawk' (out of it mcymr. hebawc, and 
from this Old Irish sebocc^ia\cov\''). Old Saxon habuk-\v\ EN, Old High German habuh^ 
hawk' from Germanic *habuka- (Finnish loanword havukka), are to be compared probably 
better with russ. (etc.) kobec, poln. kobuz^ names of falcon's kinds '] 

Maybe alb. {*gabokna) gabonja, zhgabonja, shqiponja^ eagle' (common alb. -kn- > -nj-). 
Albanian has preserved allophones shift k- .-^-guttutals (typical in Celtic Baltic languages). 

with the meaning from gr. KaTTTOo and Germanic pyO as intens. consonant-Gemination 
(due to the root form in por b^ or b) Modern High German (actually ndd.) happen, hapsen 
" devour '. holl. happen^ snatch ' ; 

Lithuanian kuopa\. 'troop, multitude, crowd, dividing off, partitioning off, 2. " ransom for 
distrained livestock ' (= gr. Kcbnn); Latvian kampju, kampV gripe, catch'; 

about Trojan name KaTTU(;, Latin capys, cap^s 'falcon' (lllyrian?) s. Bonfante REtlE 2, 
113. 

The vocalism is absolutely almost a, also in Old Indie kapatT{Vc\a\. as an isolated word 
could not have been 5 as derailment for /= a); besides occasional e{cepi, hafi) and 6 
(Kcbnn, Lithuanian kuopa, presumably also Germanic hof-), the barely placed as normal 
grades {e: a s) (vocalization by Reichelt KZ. 46, 339). The same vocal relation between 
Oscan hafiest: hipid, Lithuanian gabenti: preterit atgebau, Gothic gabei: Old Norse gsefr, 
considering of vocalization appears in the root aniaut and auslaut (final sound ) sway 
between Tenuis (*A tenuis consonant is one which is unvoiced and unaspirated. That is, it 
has a voice onset time close to zero), voiced-nonaspirated, voiced-aspirated, which can be 
explained from the imitation of short snapping sounds {kap, ghap, gbabh etc.) and 
imitation of quick snaps through this sound ("catch, grasp, snap '). 

About that in detail Collitz preterit 85 ff., K. H. Meyer IF. 35, 224-237; s. also above S. 
407ff.; different EM3 173. 

Altaic etymology : 

Protoform: *kap"e 

Meaning: to squeeze, press together 
Turkic protofomn: *Klp- 
l\^ongolian protoform: *kajici 
Tungus protoform: *kap- 



Comments: KW 180, BnaflMMMpL\OB 270, Poppe 48. A Western isogloss. Despite Doerfer's 
doubts (TMN 1, 450), the Turk, and Mong. forms cannot be separated from each other. It 
is interesting also to mention the forms meaning 'to wink' ( < *'press eyelids together') 
among the reflexes of PT *Klp- (usually confused with *Klp- 'spark') and the TM derivative 
*kapta- (usually confused with *kapta- 'flat'). Cf. also *k'ap'V. 

References: WP. I 342 ff., WH. I 159 f., 169. 
Page(s): 527-528 

Root / lemma: kar-1 

Meaning: to scold, punish 

Material: Gr. Kopvp l,x\\x\cx, auT6Kapvo(; auT0^npi0(; Hes.;
```


## [2026-09-06T15:46:08.038Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '43700,43775p' POK_full.txt",
 "description": "Pokorny kap- start of entry"
}
```


### [2026-09-06T15:46:08.107Z] TOOL RESULT

```
r 

XoiviK£(; '; with Indo Germanic enpers. caspTdan, capsTdan, cafsTdan^ grasp, capture, 
catch '; 

gr. KQTTETic; "a measure of capacity ', Kairn " crib, manger ', Karravri ds., Thessalian " the 
cross-piece in a chariot seat, the side-pieces ', Kanru) ' snap, swallow ', Kcbnn 'handle, 
grasp'; 

alb. kap^ gripe, seize, catch', kapase^ oil vessel ', /ra/r? "have' {*kapmi or * kab{h)mi- io 
root form *Aabh- to Modern High German haben); 

Latin capio, -ere, cepl captus^take', au-ceps, -cupare^ a bird-catcher, fowler', parti- 
ceps^ sharing, partaking, participant ', capax^ that can contain or hold much, wide, large, 
spacious, roomy, capacious, susceptible, capable of, good, able, apt, fit for, suitable ', 
capedo, -/n/'s' a bowl or cup used in sacrifices; drinking vessel', capu/us 'barrow, bier, 
later coffin' and 'handle, grasp, that by which any thing is seized or held ', capu/a' a small 
bowl with handles ' {capulare' von einem Gefaft ins andere schopfen '), caputrum' loop 
for catching a thing; esp. halter ' (but capis, -idis " a bowl with one handle, used in 
sacrifices ', Umbrian kapife' a bowl with one handle, used in sacrifices ', Oscan KaniSirop 
" a pot, jar ' maybe from gr. OKacpic; with 5-drop in all three Italian languages; certainly is 
capisterium \oarmor(i from GKacpiarripiov); capsa' a repository, box, esp. for books, 
bookcase, satchel ', capsus "the carriage body; cage for wild animal' (out of it gr. Kaiya, 
Kajjijja); 

Maybe alb. {*capsa) kafsha' (*captive) animal ' from " cage for wild animal ' common alb. ■ 
ps- > - fsh- similar to npers. caspTdan, capsTdan, cafsTdan ' grasp, capture, catch '; also 
from Latin capesso' seize ' > alb. kafshoj' (*seize with the teeth) bite '. 



Latin captus, -a= Old Irish cachf maid, female servant, slave ', cymr. caeth's\aye\ 
acorn, caid^ taken prisoner, captive ', nbret. keaz^ unlucky, arm', gall. Moeni-captus^ 
slave of Main (river in Germany) ', Middle Irish cachtaim " to take somebody prisoner' = 
Latin captare' try to seize ' (coincidental also = asachs. hafton' stick '); Irish cuan 
{*kapno-) "(sea-) harbor, seaport '; 

Gothic -hafts {= Latin captus, Irish cacht) " to be marked with something ', Old Norse 
haptr^ a prisoner, captive ', haptu. 'manacle'. Old English hseftm. "captive, slave, band, 
strap, manacle', n. " haft, handle, grasp'. Old Saxon haft^ a binding ', Old High German 
haft^ bound, attached, engaged, caught, afflicted with ', m. n. 'custody, manacle', whereof 
Old Norse heftiu. " haft, hold, grasp'. Old High German heftiu. " haft, handle, grasp' and 
Gothic ha ft/an lasten, clip, bind'. Old Norse hefta^b\n6, hinder'. Old English haeftan. Old 
Saxon heftan. Old High German heften^b\v\6, arrest, detain'; Modern High German 
haschen ( *hafskdh) = Swedish dial, haska " run after to catch up '; 

Gothic hafjan{= Latin capid} "heave'. Old Norse hefja {hafda). Old Saxon hebbian. Old 
English hebban. Old High German heffen, heven. Middle High German Modern High 
German heben {S\n\ss only 'hold, stop'); in addition (compare to form Latin habere) Gothic 
haban, -a/b'a'hold, stop, have'. Old Norse hafa {hafda). Old Saxon hebbian. Old English 
habban. Old High German haben'have'; 

Old Norse -hafn. "lifting'. Old English bsefn.. Middle Low German haf'sea' (ndd. Haf/), 
Middle High German hap, -bes 'sea, harbor'; Old Norse hgfni. ' harbor'. Old English 
hsefenie) f.. Middle Low German havene. Middle High German habenei. ds. (Modern High 
German Hafenirom Ndd.; compare Irish cuan); Old High German havanm. 'pot, pan, 
kitchenware ', Modern High German Hafen, Old Norse hgfugr. Old English hefig. Old 
Saxon hebig. Old High German hebTc, -g' heavy ' (actually 'holding something'); Old 
English hefe, haefem.. Old High German heve, hepfo. Modern High German Hefe( what 
lifts the dough '); isl. Norwegian dial, havaldu. 'band, strap'. Old English hefeld. Middle 
Low German hevelte {* hafadia-; Old High German haba. Modern High German Handhabe 
' hold, grasp'; 

Old Norse hafrm. ' creel, basket for holding fish after they have been caught ' (eas in 
Latin cep?); 

Old Norse hofu. ' the right measure or relation', h0fa ' aim, fit, send ', Gothic 
gahobains' abstemiousness, austereness ', Old English behofian' have need of, need ', 
Old High German bihuobida' praesumtio ', Middle High German behuofm. ' business, 
purpose, benefit, advantage'. Modern High German Behuf' end, purpose, aim, goal '; 



[Old Norse haukr{ *hQbukr), Old English heafoc^ hawk' (out of it mcymr. hebawc, and 
from this Old Irish sebocc^ia\cov\''). Old Saxon habuk-\v\ EN, Old High German habuh^
```


## [2026-09-06T15:46:15.375Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '43670,43702p' POK_full.txt",
 "description": "Pokorny kap- header and Indo-Iranian material"
}
```


### [2026-09-06T15:46:15.432Z] TOOL RESULT

```
Old Norse hgfudu. ' head'; in Germanic besides Gothic haubiP^ head ', Old Norse 
haufud. Old English heafod. Old High German houbit. Modern High German Haupt 
through amalgamation with one to Old Indie kakubh-i. "cusp, peak, acme, apex '. 

Maybe alb. kagube^ bush '. 

Old High German /7Ji75 "bonnet' etc. (compare keu-2) respective words; Cretan Kucpspov n 
Kucpnv KEcpaAnv Hes. 

With Asuffixes: Old Indie kapala-n. "bowl, cranium, Pfanne am Schenk^ 
schalenformiger oder scherbenformiger Knochen ', Pahlavi kaparak {Sc\\ei{e\om\.z BB. 28, 
144) "vessel', kapolf kneecap ', kapola- m. "cheek'; 



Old English hafola^\\ea6\ 

doubtably is affiliation from Latin cap/7/us'\r\a\r, esp. hair of the head ', see WH. I 158. 

References: WP. I 346 f., WH. I 158, 163 f. 
Page(s): 529-530 

Root / lemma: kap- 

Meaning: to grab 

Note: (Varianten s. am Schlusse); various in words for Gefafte 

Material: Old Indie kapatrtwo handful ' (/Middle Indie for t), Old pers. n KaniGn ' 5uo 

r
```


## [2026-09-06T15:46:24.523Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN leaf 119 (p.98) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==120' HRN.txt | head -60",
 "description": "Horn p.98"
}
```


## [2026-09-06T15:46:25.683Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB leaf 99 (p.89) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==100' HUB.txt | head -60",
 "description": "Hübschmann p.89"
}
```


### [2026-09-06T15:46:25.979Z] TOOL RESULT

```
=== HRN leaf 119 (p.98) ===
— 98 —
Auch np. ceh7'e (Wörterbücher jehre) 'Spinnrad' ge-
hört hier; dialectisch (Kasan) lautet das Wort cörd,
cöre, cir d. i. *care. In Vöniäün (Kä§än) bedeutet
car/^ auch ^Wetzstein (s. v. sunhade),
438. cer^n Teil, Haut\
s,w,carema7i' Teil'; phlv. carmm- ledern (vd. 18 (6)
Gl.); ai. cärmaU' 'Fell'.
oss. t. mr, curm, (315); afy. carman; kurd. LW.
car7n,
439. cerTdeti, weiden', cerend, cerägah {^^irrrd, Is. 30, 23),
cerämden.
aw. l/"6^ar-, caraiti gehen* ^) ; phlv. fehlt, vergl. aber
arm. LW. carak 'Weide', carakem; ai. [/car-, cdrati
'wandern, umherstreichen, weiden'.
kurd. darin \ af/. car[edal; oss. d. carun^ t. cärin
'leben, wohnen (317); bei. öarag, n. cara/ 'wandern,
umhergehen ; weiden, grasen ; reiten' (55).
Spiegel, Commentar I, 160 will auch np. cemen
'Wiese' (aus "^cermen) zu [/'car- stellen, doch ist dies
unsicher; aw. yavö.öaränlm (vd. 5, 5) wird kaum
'Getreidefeld' bedeuten, vergl. Geldner, KZ. 25, 200.
440. cesm 'Auge 2).
aw. dasman- 'Auge'; phlv. casm, casm[gäh, öasmak
('Quelle') ; ai. öaksm- 'Auge'.
kurd. zaza öim ; oss. d. caste, t. cäsf (318) ; bei. Sam,
n. c'am *Auge', öamay 'Quelle' (52, 53) ; wa/. cözm^ äi/n.
sar. cem^ sangl. sam^ minj. cam,
441. cespEden, cepsiden, cefslden (Inchoat.) 'packen, fassen*.
Zu lat. capiö (Nöldeke, mündliche Mitteilung).
Also vergl. got. hafjan 'heben', hafts 'behaftet, ge-
fesselt'; gr. aaini] 'Griff'; air. cacht 'Sklave; lett. kampt
'fassen' 3).
*) Nach Bezzenberger wäre ap. a6a]crtr/.s*Gememde weide*,
doch vergl. oben Seite 38 Anm. 1.
') AM. hat immer cism. Im 8ähn. reimt auf cesm häufig /psw,
wo man vielleicht auch cism und ^ism lesen darf.
*) Alb. kap *greife, fasse an, nehme gefangen* ist nach G. Meyer
aus t. qapnn*<i *fangen, erhaschen* entlehnt.
```


### [2026-09-06T15:46:27.948Z] TOOL RESULT

```
=== HUB leaf 99 (p.89) ===
- 89 -
und Impt.) = kandol („in the past tenses'') kann
doch nur LW. sein (np. praes. kanam, perf, handam).
Die Differenz zwischen iran. han- und skr. khan ist
noch nicht befriedigend erklart.
870. Np. kamzak ist durch das Deminutivsuffix ak von
kaimz abgeleitet. Phi. kanlSak ware = np. kanlza,
Vgl. Darmesteter, Etud. iran. I, p. 288. Ueber
dial, kine s. Mann, ZDMG. 47, 705.
871. Np. hutdh oder kdtah (nach dem afgh. LW. kdtah) heisst
eigentlich 'kurz* (nicht 'klein*) und ist von np. kddak
*Kind' = phi. kotak *a child, an infant' Gl. and Ind.
201, arm. LW. kotak *der Eleine' (Beiname des armen.
Konigs Xoarov bei Faust us von Byz.) zu trennen.
Letzteres ist durch Suffix ak von *kOt = ap. ^kauta-
abgeleitet, zu dem das auf schwachster Wurzelstufe
stehende zd. ktUaka- *klein* gehSrt. Horn's Erklarung
von kodak aus ^kvataka- (vom Pronominal stamm kva-,
ku"?) ist mir unverstandlich.
872. Np. fcil^a 'irdene Krug, Kanne* = afgh. kUza an earthen
vessel for water with a spout* ist abgeleitet mittelst
des Suffixes a (= phi. ak) von kUz = arm. LW. kuz
'Krug, Kanne' = arab. LW. hOz *kleiner Krug und
geht mit diesem auf ein ap. *kuza (oder *kuja) zuriick.
Ueber zd. xawza- vgl. oben Nr. 483.
Hier fehlt np. Uui {kUz und kUza) gekriimmt' {kuz-pust
Fird. I, 503, Z. 7), afgh. ko^ (LW.?) crooked, bent*
= skr. kubja^ 'krumm, bucklig*.
873. Die Zusammenstellung setzt eine idg. Wrzl. kul-
(hochstufig ketd^ kouT) voraus, die es nicht giebt.
874. Zu streichen.
875. Dazu arm. LW. ioAai 'Berg, Woge' und nach Geiger
afgh. kvah *H6cker .
Hier fehlt np. kavl», kavHz = arab. LW. qafiz u. s. w., phi.
kapU (so zu lesen) Gl. and Ind. 197 u.s.w., arm. LW.
kapic 'ein Maass fur Getreide' etc., ap. xan/drj de La-
garde, Ges. Abh. 198.
```


## [2026-09-06T15:46:40.784Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; ls -la MON_part1.txt MON_part2.txt 2>/dev/null; python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(json.dumps(d['MON'],ensure_ascii=False,indent=1))\nprint(json.dumps(d['BQT'],ensure_ascii=False,indent=1))\n\"",
 "description": "MON and BQT ref details"
}
```


### [2026-09-06T15:46:42.904Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 4377831 Sep  4 14:06 MON_part1.txt
-rw-rw-r-- 1 sfmqrb sfmqrb 4331421 Sep  4 14:06 MON_part2.txt
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
 "notes": "Persian OCR is mediocre: headwords and Mo'in's footnotes (e.g. '۱ - رك: ابر کوه', Pahlavi/Avestan Latin forms) are mostly readable but with many character errors; search with short substrings and tolerate errors. BQT_v1_pages.txt was built from the djvu.xml; BQT_v2_pages.txt from pdftotext -layout of the _text.pdf. Volumes 3–5 (roughly ح/خ–ی and the تعلیقات volume) are not online in full text; for those use Dehkhoda quotations of Borhan/Mo'in via vajehyab/abadis/parsi.wiki, or page images on noorlib (different edition). | Vols 3-5 scans (image only) in incoming/BQT; vols 1-2 have OCR text files BQT_v1_pages.txt / BQT_v2_pages.txt. Offsets verified by eye at several pages (v3 drifts by ~4 pages; page_map gives exact positions once built). || UPDATE: vols 3-5 now downloaded (image-only PDFs, verified as Mo'in's edition from title pages and the Latin footnotes) and OCRed locally. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); *_pages_faseng.txt = 'fas+eng' model (better for the Latin-script Pahlavi/Avestan etyma, worse for Persian). Pages separated by \\f; leaf N = N-th \\f-block 0-based = PDF page N+1. Search with short substrings and tolerate OCR errors. Provenance caveat: picofile is a general file host, the uploads are not from a library; treat as a grey copy (the book is in copyright in Iran). | vol 4 (م–ی) OCR text, tesseract fas+eng, pages tagged [pdf page N], printed = pdf+1917 | vol 5 (ta'liqat) OCR text, printed = pdf-5 | vol 3 (ش–ل) OCR text (689/721 pages), printed ≈ pdf+1203..1209 | BQT_v2_pages.txt: printed page = leaf + 540 (verified by catch-lines at pp. 838-855, 869, 904); earlier estimate +543 was 3 pages off.",
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


## [2026-09-06T15:46:49.423Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 leaf 96 (p.636) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==97' BQT_v2_pages.txt | head -70",
 "description": "BQT p.636"
}
```


## [2026-09-06T15:46:50.135Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nfor p in 329 375 383; do echo \"=== pdf page $p ===\"; grep -n \"\\[pdf page $p\\]\" BQT_v3_pages.txt; done",
 "description": "Locate BQT v3 pdf pages"
}
```


### [2026-09-06T15:46:51.313Z] TOOL RESULT

```
=== BQT v2 leaf 96 (p.636) ===
      ‫سرب‬                                                                                       ‫‪۳۳‬‬

‫حت آلت‬    ‫یًابر‬ ‫جوصا‬
                   ‫کاهشند نيك شود خص‬      ‫ب‬          ‫ون‬
                                                      ‫وزن سرشخ › مخفف چشم زخم‪ .‬است ‪٩‬‏ آ‬

             ‫وجراحتی که مادرزاد با‬
 ‫وشدبا؛ین معتی‬                     ‫ل‬ ‫س‬ ‫ا‬ ‫ن‬ ‫ت‬        ‫وزی باشد خصوضا اطقال را که سیب‬
                                                                                 ‫زا‬‫آتی‬
                                                                                     ‫آف‬

                                                    ‫دیدن وتعریف کردن بعضی ازمردم بهم‌میرسد‪. .‬‬
‫چشم آب دادن = کتانه از تماشا‬                        ‫چشفر ‪ -‬بافابروزن ششدر» بمعنی‌چشیر‬
                                         ‫‪.‬‬   ‫کردن‬
                                                     ‫است کهشان پ بااشد عموماً ‪.-‬وتشان پسابیاع‬
‫چشم | رو ‪-‬رباای قرشت (‪ )۱‬وواو‬                                              ‫‪۶‬‬          ‫باشد خصوماً ‪۰ ۲‬‬


‫مجهول بروزن شفتالو چیزی کهبجهت دفع‌چشم‬               ‫حثاث = بکراول وسکون‌نانی وکاف؛‬
‫زخم رچشم بت سار ند اعم ازا نکه برایآدمی با‬          ‫بمعئی اقرون وغالب و زبادتی و افزونی وعالب‬
       ‫را‬
      ‫وی‬    ‫حوانات دبگر نبکشت زار وباغ وخ‬
         ‫سانه‬                                                                    ‫شدن وغلبه باشد ‪۰‬‬
                            ‫اومثارآن باشد ‪.‬‬         ‫ه بر وزن پشم‪ ..‬معروف است که‬           ‫چم‬


 ‫‪ -‬باغین قطمدار بروزن‬       ‫چشم !غل‬                                            ‫عرب عکیونبند ‪- ۴‬‬
‫دربا دل » از گوشةٌ چشم نگاه کردن باشد اعماز‬                                ‫ودانسیاهی‌باشد لغزنده‬
                                                                             ‫که آنرا در داروهای‬
‫وکا ونازسونگاه کنندعرانیز‬   ‫‪ 5‬عمزه‬   ‫قهر و عض‬
                                                                               ‫چشم بکار برند وچون‬
                                     ‫گوبند ‪. ۸‬‬
             ‫حشم | غلیدن ‪٩‬‏ آ‬
 ‫=زروی قهروغضب‬
                                                    ‫بعد اصزلآانیه کرده ‪١ı‬‏ پلك بالا ‪ -‬پلك‬
                  ‫بگوشة چشم نگاه کردن باشد ‪.‬‬         ‫باين ‪ -۳‬حدقه (مردمك)‬

                                                                    ‫(‪ )۱‬چك ‪ :‬بارا ‪.‬‬
                     ‫رك ‪ :‬چشیر ‪.‬‬     ‫‪۴‬‬                         ‫چشم زخم ‪.‬‬       ‫رك ‪:‬‬     ‫‪- ۱‬‬

      ‫=‪0‬تاکه»‪ .‬اوستان‪hsac ]2۳‬‏ «اسفا‪:۱‬‬
                                     ‫‪ ( 0۳08516 - ۴‬در شاهنامه بخاشم قافیه آمده) ‪۳۲‬‬
       ‫‪ ۲‬ص ‪ <4‬رك ‪ :‬اسشق و هوبشمان ‪ › ۰44‬پپلوی ‪ « 0711152‬تاوادیا ‪ ۲1 : ۰۷۲‬اونوالا ‪۰۷۵‬‬
      ‫کلکی ‪ 0۳1۱۰‬فریزندی» برنی‌ونطنزی ‪« 00182‬ك ‪۱ .‬ص‪ ۰ ۸۸۲۰‬سمنانی» لاسگردی‌وشهمیرزادی‬
      ‫‪ . 01‬منکریل(افقت»‪ .‬سرخه‌بی ‪ 0520‬دك ‪۲ .‬ص ‪ “6۸‬اورامانی اء «‪ .2‬اورامان‪»۱۲۱‬‬
      ‫در مروشاهجان نیز ‪11‬ا‪٥‬‏‬   ‫در بیتی از رود کی چمش «تارینسیستانص‪۷٩ ۹۱۳‬‏ ورك ‪ :‬چمش ‪.‬‬
      ‫هلت فری اسدی ص‪ ۰ ۲۵۳‬سریکلی ‪ . 01660‬شفنی ‪,0780‬بلوچی ‪ 071۵6‬بودغا ‪ » 016‬وخی‬
                                             ‫ص‪ )۹‬ورك ‪ :‬چم ‪.‬‬ ‫‪ « 12‬اسفا ‪۹۲ : ۱‬‬
  ‫‪-‬یم مومن درتحفه ذیل ت«شميزج » آرد ‪ « :‬معرب از چشمیزاك فارسی امت‬
                                                                ‫‪۴‬ک‬‫ح‬
      ‫واورا چشمك وچشم نامند‪ .‬دانه‌است بقدر بهدانه مثلث و سیاه و براق ‪ ۰»...‬و ذیل چ«شمیزج »‬
      ‫و «چشمك» و «چشوم» گوید‪:‬ه تشمیزج است»؛ رك ‪ :‬چشام و تشمیز وممرب آن «ششم» بکسر اول‬
      ‫® ‪ -‬نیز سفیدی میان سرفاوقاف وواو راگویند ‪ « :‬وچشمپای واو وقاف‬                      ‫است «تفس؟‪.‬‬
              ‫و فا در خور ‪ere‬‏ و بر نك اندازه بود نهتنگه ونه فراخ» «نوروزنامه ‪۷۱۱٩ ۷8۰‬‏ ‪.‬‬
      ‫‪« -‬چشمآ لوی‌نگرستن‬                 ‫‪ _ ۱‬مخفف« چشمآغیل» («‪.‬م‪ ).‬ورك‪ :‬چشمآغلیدن‪.‬‬
      ‫بيك کوشة چشم بودو چشماغل نیزکوبند ‪ « ».‬لفت فرس‪۹٩۹۱‬‏ ح ‪». 4‬‏ ‪ - 4‬باین معنی‌اسم‬
  ‫‪۱‬‬       ‫از ‪ .‬چشم آغل ‪ +‬بدن (مصدری)‪.‬‬          ‫‪٩‬‏‬               ‫فلعل است باحذف «نده» ازآخر ‪.‬‬
          ‫ب(رهان قاطع هه)‬                                         ‫‪۱‬‬
```


### [2026-09-06T15:46:53.177Z] TOOL RESULT

```
=== pdf page 329 ===
23857:[pdf page 329]
=== pdf page 375 ===
27299:[pdf page 375]
=== pdf page 383 ===
27872:[pdf page 383]
```


## [2026-09-06T15:47:02.228Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in چسبیدن چفسیدن چسپیدن چسبید; do echo \"--- $w ---\"; grep -n \"$w\" BQT_v2_pages.txt | head -5; done\necho \"=== leaf 95 (p.635) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==96' BQT_v2_pages.txt | grep -n \"چس\" | head -20",
 "description": "Find chasbidan in Borhan v2"
}
```


### [2026-09-06T15:47:04.644Z] TOOL RESULT

```
--- چسبیدن ---
5451:‫چست ‪ = ۷‬بش‌اول‌وسکون‌ثانی وفوقانی‪.‬‬                   ‫چسبیدن * ۔ بباای فارسی بورزن‬
5468:   ‫چسفیدن» «صراح» ‪« .‬الضیف (عیبی) » چسبیدن تیرازشانه «‪٩‬‏ مجمل‌اللفه » « المیل » بچسپیدن‬
7505:‫بی نقطه ‪ .‬بروزق ومعنی چسبیدن (‪ )۱‬است اعم‬                             ‫چوده بنم اول وسکون ثانی وزای‌هوز‬
20425:‫دندان ادن = بممنی چسبیدن باشد‬
21223:‫وفتح ثالث و نون » ظرفی باشد که درآن شیر‬                         ‫چسبیدن(‪ )۳‬وملصق شدن ‪ -‬ورسدن‪ -‬ولغزندن‬
--- چفسیدن ---
--- چسپیدن ---
5468:   ‫چسفیدن» «صراح» ‪« .‬الضیف (عیبی) » چسبیدن تیرازشانه «‪٩‬‏ مجمل‌اللفه » « المیل » بچسپیدن‬
--- چسبید ---
3145:                                                  ‫که بر همچسبیده اند‪ .‬خوردن آن منع هوی‬
5451:‫چست ‪ = ۷‬بش‌اول‌وسکون‌ثانی وفوقانی‪.‬‬                   ‫چسبیدن * ۔ بباای فارسی بورزن‬
5468:   ‫چسفیدن» «صراح» ‪« .‬الضیف (عیبی) » چسبیدن تیرازشانه «‪٩‬‏ مجمل‌اللفه » « المیل » بچسپیدن‬
7052:‫آم مقدارست کمتر از ده‬            ‫باشد کاک‬              ‫یر ندو‪-‬چوب‌خوشةانگو ر که‌برتاك چسبیدء(‪)۱‬‬
7505:‫بی نقطه ‪ .‬بروزق ومعنی چسبیدن (‪ )۱‬است اعم‬                             ‫چوده بنم اول وسکون ثانی وزای‌هوز‬
=== leaf 95 (p.635) ===
7:‫چسنگه » بروزن پلنگه » مردم کل‬                     ‫چسته = بفتح اول بروزن دسته» بمعنی‬
35:          ‫خاشاك وار بر سرآبآمدآن چسنك ‪.‬‬         ‫‪- ۱‬سرمت ‪ ...‬فراخ چودرآب‌غرقه شد‬
```


## [2026-09-06T15:47:09.282Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport io\nt=open('BQT_v2_pages.txt',encoding='utf-8').read()\npages=t.split('\\f')\n# find page containing line 5451 context\nfor i,p in enumerate(pages):\n    if 'چسبیدن' in p and 'چست' in p:\n        print(\"leaf\",i,\"printed\",i+540)\n        print(p[:4000])\n        break\nEOF",
 "description": "Borhan chasbidan page"
}
```


### [2026-09-06T15:47:11.015Z] TOOL RESULT

```
leaf 94 printed 634
                                           ‫بیان نهم‬
                  ‫در جیم فارسی با زای هوز مشتمل برشش لغت‬
‫جز ده = بفتح‌اول وثالك وسکون‌نانی »‬                ‫=فتح اول وسکون‌انی » میمون‌را‬
                                                                               ‫جز ب‬
‫بمعنی‌چزدره است که جزغاله باشدیعنی دلبه وییه‬                             ‫کون دکه حمدونه است ‪.‬‬
                       ‫‪۰‬‬   ‫ریزه کرد بربان‌شده؟‬     ‫جز ‪۵‬ه بفتح‌اول وسکون‌انی ودال‌ابجد‪,‬‬
‫‪ -‬یکراول وسکون ثانی و غین‬          ‫چزع‬             ‫جالور کیست شبیه بملخ که پیوسته درغله زارها‬
              ‫‪۲‬‬   ‫لقطه دار‪ .‬خارمشت را گوند ‪۴‬‬       ‫ور هوای کرم فرباد طولانی کند و در‬ ‫می‌باشد د‬
                                                    ‫نی جاهاآ نرا بگیرند و بربان کنند وبشخورند‪.‬‬
‫چزك ‪ -‬پکر ارل وسکون ثانی‬
‫واف » پمعنی چزغ است که خار پشت‬  ‫ک‬                  ‫» بارهای‌دنده‬   ‫بروزن محمره‬   ‫جز در ه‬

                        ‫باشد‪ . ۴‬٭‬                         ‫ویبه بربان کرد روغن گرفته کروایندا ‪.‬‬


                                           ‫بان دهم‬
                  ‫در جیم فارسی با سین بی‌نةطه مشتمن بر چپار لت‬

‫چست ‪ = ۷‬بش‌اول‌وسکون‌ثانی وفوقانی‪.‬‬                   ‫چسبیدن * ۔ بباای فارسی بورزن‬
‫| جلد و چالاك و چابك باشد ‪ -‬و هرچیز که يك‬               ‫یشدگر‬
                                                            ‫دی با‬
                                                                ‫‌جسم‬
                                                                   ‫یافتن‬
                                                                       ‫مال ب‬
                                                                           ‫ج"اص‬
                                                                              ‫بیدن‬
                                                                                 ‫رقص‬
‫که انفصال آن مشکل بود ‪ -‬و چیزیرا محکم | و باندام درجابی شیند ‪ -‬و محکم ‪ -‬و ازك ‪-‬‬
‫و زیبارا همکفته‌اند ‪ -‬و بمعنی تنکه و چسبان‬         ‫بدست گرفتن ‪ -‬و بمعنی مل کردن حم آمده‬
 ‫هم هت ‪ ۸‬که نقیض فراخ و کشاد باشد ‪-‬‬                                                    ‫است ‪. ۷‬‬

  ‫‪ ۴‬رکه‪ :‬چزغ‪. ‎‬‬         ‫‪ - ٩‬رك‪ :‬چزده‪ ۴ .‬رك‪ :‬چزدره‪ - ۴ . .‬رك ‪ :‬چزك ‪.‬‬
  ‫‪ = ۵‬چیسدن (ه‪.‬م‪ = ).‬چفیدن ( «‪.‬م‪ »).‬از ریشة ابرانی لهاع ‪ , #‬افتانی ع‬
   ‫(چین دکی)‪( 02۳5260 .‬چسبنده) «اسشق‪ .‬هویشمان ‪ « ۱686‬اسفا ‪: ۱‬ص‪۷٤۲‬‏ » ‪.۹۲۱‬‬                   ‫‪0‬‬
  ‫‪ - ۱‬بمعنی مل كردن رك‪« 5۵1. 4981, 454 :‬هوبتمان ‪« : ۱44‬لطا (عریی)‬
   ‫چسفیدن» «صراح» ‪« .‬الضیف (عیبی) » چسبیدن تیرازشانه «‪٩‬‏ مجمل‌اللفه » « المیل » بچسپیدن‬
    ‫«مصادر زوزنی» «المیل والمیلان ‪ ...‬چپیدن» «تاح‌ال‌سادر ببپقی» » متعدی آن » چسپایدن ‪:‬‬
              ‫د از افادات علامه‌دهشد!ا»‪.‬‬   ‫چبانیدن» «مجمل‌اللفه»‬    ‫«الاستمالة(عریی) » سوی خوش‬
   ‫‪ - ۷‬هندی باستان_ ‪1 , 000‬ا‪ 46‬اغا ‪۲ :۱‬ص ‪ ۲۲۳۲۰‬ساب کرت ‪(112006‬راندن»‬
            ‫تحريك‪ .‬عجله کردن) « اسشق ‪ ۲64۲۰‬پهلری ‪1181۵0٥1۷‬‏ (دوبدن) دریکبه‪۳‬ع‪۲‬؟»‪.‬‬
           ‫است ‪.‬‬     ‫ار ارکانش باد درست‬               ‫فراخ و کرنه چست‌است‬        ‫خانه‬
                                                                                    ‫کر‪۱‬‬
                                                                                      ‫‪۸‬‬
       ‫امیر خرو دهلوی ‪.‬‬
                                             ‫‪ #‬چرك ‏ رك ‪ :‬لفات متفرقةٌ پابان کتاں ‪.‬‬
```


## [2026-09-06T15:47:23.852Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; grep -n \"cifs\\|čifs\\|kapi\\|kapiθ\\|kapitha\" KNT.txt | head -20; echo \"=== BRT 436 ===\"; grep -n \"kapasti\\|kapastay\\|kapast\" BRT.txt | head -20",
 "description": "Kent and Bartholomae lookups"
}
```


### [2026-09-06T15:47:23.911Z] TOOL RESULT

```
=== BRT 436 ===
9027:•  j,  kapastay-  f.  Name  einer  infektiösen, zu  Kriegszeiten  auftretenden  Krankheit'':
20572:•  j,  inüi«^-  f.  Name  einer  Daevr.  ptn/te "Si  pifitte  kapastis  V.  11. 9.
```


## [2026-09-06T15:47:27.621Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '9015,9045p' BRT.txt; echo \"--- which leaf/col ---\"; python3 - <<'EOF'\nt=open('BRT.txt',encoding='utf-8').read()\nimport re\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'kapastay-' in p:\n        print('leaf',i)\n        # print column numbers found\n        print(re.findall(r'\\b4[0-9]{2}\\b', p)[:20])\nEOF",
 "description": "Bartholomae kapastay entry"
}
```


### [2026-09-06T15:47:29.413Z] TOOL RESULT

```
')  Der  Esel  gil'  nn'er  den  slasm-  (Grossrieh) Hir  das  wenigst  wertTolle  Tier.  Die  Reihenfolge ist  (V.  7.  42):  Esel,  Rind,  Ross,  Kamel.  Vgl. GüR.  OK.  36L  ').
Et.?    —     ¥ü.:  lor.    —     ')  PDw.  *B,?/  'EseLs-
fiillen'.  vorauf  G<iR.  verweist,    kann    ich  mit
k'  nicht  vermitteln.
•  }.,  g.  kat  Adv.,  an  der  Spitze  des  Satzes; i)  'wann';  -4'  tä  nara  irista  ..nasus  upa.- dvqsaitii  . .  isar>  pasca  parairistim  V,  -j, \l.  2)  als  Fragepart. 'obwohl?,  num?': if=''  asavä  inazdä  vSng/iat  drjgvanim» "wird  der  .,^/aanhänger,  o  M.,  den  Drug- genossen  überwinden?'  Y.  ^iV.  2 ;  —  h asava  .  .  ranat  dnantjmf  asava  vana[ drvantjm  Yty.  28;  —  kat  möi  un-ä  isi (sd.)  caAyil  avauhS  "ob  (wohl)  .  .*'  Y.  50. i;  —  alä  k'  ^wä  darssäiij  i!S&?i  Y.  J<V,5;
—  k°  ta  Aaowa  yaoidiiyqn{%A.)  ai^h^n},. yaozdayqtt    anhm   V.ö.^if.;  7-23,5.57;
—  *i*  he  Vif  as.'m  *v}rxy,ll  N.  li\  —  k'  ta pd^a  frayqn  pasi'qtn  .  J  iiöit  t/i  pa'^>'r frayqn  piisrqm  ..  V,.V.i4f.;  —  6'  nä  .. tanii.p^rSiäi  .  .  gius  aiiilitya (^A.\  iislndli N.  /<V;  i/;,  ;7'>.  Unklar;  k'  kam  "^risa vibarst  N.  10^'.         [Yt.7.2*:  lies  idoa.]
ASn.  aus  tkn-.  —  oi.  kii/  Fragepart.  —  M.: *.-»,  («.  Vt.  /),  IWS.,,  (lu  Y.  .-ili  *•>.  - •)  Eig,  'was?  witd  ..  besiegtn?';  ebenso  im Ai.;  vgl.  daiu  Dmr.  VglS.  3.  261.  —  n  kat fehlt,  aber  I'Q.:  fi;3n.
•  '].  katmöLurvä-  fem.  Adj.  'die  Worte
^rt/ m^^i' «/T,(  enthaltend,  damit  beginnend': "j'ii  /iäitis(sil.)  ''  Y.  50  Überschr. ;  —  'i-qr/i AiJiilm'*  vazamaide  Y.  50. 12. ■)  1>.  i.  "V.  50.
•  p.  ka''pada-'>  m.  Name  einer  I^nd- schaft  in  Medien,  Cambadene:  'da''  iulm.'t" dahyäui  miidaiv  Bh. :;.  ö.
FüV  KZ.  37.  531  will  h^p-fdii-.
•  j,  kapastay-  f.  Name  einer  infektiösen, zu  Kriegszeiten  auftretenden  Krankheit'':
"ira    airy<i    daiü/ii'tvd  frqs    hyät  .  . pqma  nöit  'tis  Yt. -S'.  56;  —  pjr.me  tnüi'.i •nne  "lis  V.u. ff.
?:t.?0.  —  Pü.:  fehlt;  Kyo.:  kF«ü.  ei\.:  n.i kiMii  li.iti  ,/,ijl  kitnad.  —  ')  Man  setit  wegen np.  kiihijsl  'Koloquinle'  die  Bedeutung  'Gift' oder  'plante  vüni'neuse'  an,  was  mir  nicht  lu passen  scheint.  Eber  ka-/<a'Uiy-  (s.  unter t,-nu,A„-y,  vgl.  lat.  A^/«.
•  p.  ka''büjiya-  m.  EN.  eines  persischen Königs;  Katnbyses,  Sohn  Ats  Kyros:  'ya* näma'    küraus    fui:''a*  .  .  paruvam    idä
dby  Google
"kan-  Noten
438
:rri7vrt>(>fl*  ühJ*  Bh.  /.  10;  lo';  — pasav^
'ytr  ''uvsmarsiyus  (sd.)    amarhata    Bh.  /,
11;  —  xsai'am  lya''  gaumäicr  .  .  adins"
'\am    Bh. /.  12;  12;    —    avahyä    'ya/ivil
i'r.ltä  bardiyi^  mlma'  äkt^   Bh.  /.  10;  10,
11;  —  haeiJ  °_j'ä*  Bh. /.  11.
El?  Man  hal  das  Wort  zu  ai.  kamboja-  \A:y,\
Itez.  eines  Volks,  gesteUt.    Fuv  KZ.  35.  61,  :
37.  543  letlegt  kam  {ai.  kam  'bene')+*-  (iura  \
V.  Awi'-):  ähnlich  auch  JusTl  NB.  490.   Eli  er  ,
»II.  *ki/'bü'-^''jiyä-  'mit  Sehnen  aus  -?  -';  s.  ■
V>j--  j
--- which leaf/col ---
leaf 266
['438', '490']
```


## [2026-09-06T15:47:41.375Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; echo \"=== HRN p.187 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==209' HRN.txt | head -60; echo \"=== grep kabast ===\"; grep -n \"kabast\\|kapast\" HRN.txt | head",
 "description": "Horn p.187 kabast"
}
```


### [2026-09-06T15:47:43.292Z] TOOL RESULT

```
=== HRN p.187 ===
- 187 - -
Gras (Saccliiinmi spontaneum L); doch ursclieint im
V
I'ehlevr auch schon läh (PPGL), kahnipai (Säy. nätJiy.
II, 115), indess sind beide Stellen jung.
840*"" kehest, kehestü, kel)este^ kewest, DDDD (Jer. 8, 14)
'Koloquinthe ; Gift, Aristolochia (?)\
aw. kapasti- (Spiegel, zuletzt Ar. Periode 46);
phlv. kapast (Bund.).
Die Bedeutung des aw. Wortes ist ganz unsicher
(vergl. Geldner, »5 Yasht, 77) ; lit. kopustas 'Kohlkopf,
das Spiegel vergleicht, gehört bestimmt nicht hierher.
841. kelfk *Kebhuhn*, arab. LW. (jabj^ qahjat.
vergl. skr. kajnnjala^ 'Haselhuhn*; bei. kainnjar^
n. I^awinjar 'Rebhuhn' (li)0).
LW. kurd. keü^ qewy, vergl. Kas. köik, kcnrk; af/.
kabk; bei. kabg, n. kaivg (120).
'Eine starke Verstümmelung* der sansk.-bel. Formen
(Geiger) kann das neupersische Wort nicht sein;
in der Stammsilbe {kebk aus *kapak) sind sie aber
gewiss identisch (etwa auch mit kebiiter?). Ihr Ver-
bal tniss zu gr. nuy.Tcdfirj^ arm. knffav, syr. qaqqewä, alle
'Rebhuhn (Hübschmann, ZDMG. 46, 241 No. 60),
ist unklar.
842. kebüter 'Taube, nni5D (Jer. 48, 28), kebüd 'blau',
keffer (inbD, Ps. 56, 1, Litbl. f. or. Ph. 11, 19:^, kebük.
ai. kapota- 'Taube; grau, bleigrau (taubenfarbig,
vergl. kapöta-)\ vergl. jain. käö {*kapötu-) 'Nuance
der Hautfarbe zwischen blau und rot* (Leumann bei
Feist, Got. Etym., S. 144); phlv. kapötar 'Taube'
(Papyrus, Hörn, ZDMG. 43, 50), kcqM 'blau (Men.
27, 50 'der blaue Wolf, vergl. palang IJD kapötar
"ij:n'»*lp 'der Panther, den man kapötar^ d. i. tauben-
farbig, nennt* im sog. Iran. Bund,, briefliche Mitteilung
von Dr. E. W. West vom 23. 11. 1891); arm. LW.
kapoit 'blau (vergl. Bartholomae, BB. XVII, 101).
kurd. kewük, kavök^ kötir; af/. kavntar , kautar;
bei. kapöt (191), köntar (210); wa;^. kibit, sar. cabnnd,
=== grep kabast ===
7307:aw. kapasti- (Spiegel, zuletzt Ar. Periode 46);
7308:phlv. kapast (Bund.).
```


## [2026-09-06T15:47:53.233Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nt=open('BQT_v3_pages.txt',encoding='utf-8').read()\nimport re\nblocks=t.split('\\f')\nwant={329,375,383,376,384,330}\nfor b in blocks:\n    m=re.search(r'\\[pdf page (\\d+)\\]', b)\n    if m and int(m.group(1)) in want:\n        print(\"########## pdf\",m.group(1),\"printed ~\",int(m.group(1))+1205)\n        print(b[:2600])\nEOF",
 "description": "Borhan v3 pages for qafas, kanun, kabast"
}
```


### [2026-09-06T15:47:55.984Z] TOOL RESULT

```
########## pdf 329 printed ~ 1534
[pdf page 329]
۳۹

قعنوی

مرفی است‌بفایت خوش‌ردگه و حوش‌آوازه کوبند
منقار او سیسد و مت سوراخ ,دارد ود رکوه
بلندی مقابل پادنشیند و صداهای عجیب وغریب
از منفار او ‎aT,‏ وسبب ‎OV‏ مرغان بپارجمع
آیند . از آ نها چندیرا کرفته ‎Leak‏ خود سازد .
‎aS‏ حزار سال ‎ISG‏ ز چون زار سال
بگذرد نو عمرش ‎at ATS‏ سیار جمح‌نازد
و بی بالای ‎OT‏ نشیند و سرودن آغاژ کتدومسث

۷

گردد و یال برحم زند چنانکه آی از بال ار
بجهد و درهیزم افتد و خود با هيزم بسوزد واز
خاکسترش بیضه‌ای‌پدیدآبد و او را جفت نمیباشد

و. موسیقی را از آواز او ‎lads‏

‎gd‏ ۱ = بروزن ‎sil‏ بسنی
ققنس است و آن ‎gy‏ باشد که هزارسال عس
کدد و عافبت بسوزو .

‏بیان چهاردهم

‏درقاف با لام مشتمل برپنجاه ويك لفت و کنایت

‎oe -‏ اول و ثاپی بالف کشیده .
پمعنی فلاخن است ۴ - و بمعنی اشخار وقلياهم
آمده است که زاج ‎che‏ باهد .

‎a) ols sows‏ موضعی است‌در
شیراز و شیخ سعدی درآنجا مدفون است ۴ .

‏قلاچودی ۴ ت با جیم فارسی » برد
وزن و معنی فراچوری است که شمشیر آبدار
‎ath‏ .

‏لارون * - بارای بی ‎abt‏ بروزن
فلاطون « نقیبان لشکر را گویند «

‏قالادی ‏ نم اول و نی بالف کشیده

‏و رای بی‌قطه بتحتالی رسعده.نوعی ازانجیرسفید
(۱) چش : کازران.

‎. ‏ققنی‎ : dy ٩
.> ‏اظفری‎

‎+ ‏و سرآن زرد میشود‎ ath

‏ولاز ار رفلاژاره 1 - جتح‌اولوزای
تقطمدار بالف کشیده » درلفت اول و زای فارسی
در لفت دوم و ‎(x) “3 shes‏ ء پر لله‌است
میاه و سفید از جن سکلاغ که او راکلاغ پیسه
و ‎Ke‏ خوانند .

‏قلاسنگ ۷ - بفتح اول وسین‌بی قطه
و سکون نون و ‎GE‏ فارسی . فلاخن ‎wa Sly‏
و آن کفه‌ایت که از ابریشم و امثال آن بافند
و بر دو سر ‎OT‏ دو ریمان بندند و شاطران
و شبانان بدان سنگه الذاز ند .

‎+ ‏مشدد بریزن فراشی‎ gt ‏با‎ = PMS
‏و مفلی‎ ae ‏و لوند و بی‎ Ga ‏مردم بی‌نام‎

‏)9( چك : ‎py‏ را .
۴ - ترکی ‎Ga‏ فلاخن > فرهنگه نظام بنقل از ‎Kans‏
‏۴ - قلات ( بفتح اول ) ده بزرکی است ازدهستان حومةّبخش‌مر کزی‌شهرستان

‏شیراز ۰ ۳۳ کیلومتری شمال باختر شیراز ۰ 4 کیلومتری ‎Legs‏ شیراز باردکان . «قلات ‎NIT‏
‏موضمیست درشیرا ‎S‏ مدفن ‎Gane‏ است و ‎AT ne‏ اهل شیراز است وآنجا حوضی است مثمن پر
ماهی ومردمآ نجارخت‌شویند وه کازر گام کویند وبعداز چهل روزازنوروزانبوهی عظیم درآ نجاشود.»
‎ged)?‏ ۴ س قراچوری ‎pe)‏ ۰ -ظ . مسحف « قلاروز » ‎Com)‏

‏۰ = کلازارد ‎Ape)‏ ظ. جزواو ل کلم هکلاز ‎Com)‏ کلاز = کلاژء ‎Ey = Cpe)‏
قلاغ  ‎CIT‏ (طبری . صاب ‎ )۵4۱‏ کلاچ (کیلکی) است . ۷ - رشیدی کوید :
«قلاسنکه وقلماستکه وقلماء فلاخن باشد که بدان‌سنگه اندازند بقبه ‎am banks Lesley‏


########## pdf 330 printed ~ 1535
[pdf page 330]
—\ery—

و ازکاینات (۱) مجرد رااگویند ۷ .
قلاشیره ۴ = ‎pc‏ اول و شین‌قطمدار
بتحتانی رسیده ورای بی‌نقطة مفتوح , قلیاواشضار
است که زاج سیاه باشد .
قلاقل پکسر اول وفتح قاف‌وسکون
لام. نام درخت انارسحرالی است و آنرا قلفلان
‎e‏ میگویند ۴ و بعربی رمان البری خوانند .
قلاوود ۴ ‎ly b=‏ بر وزن فبادوز .
سواراتیرا گوبند که‌ببجهت محافظت لشکردریرون
لشکر میباشند ؛ و بتخظیف واو هم آمده است
که بروزن تجاوز باشد ؛ و با رای بی نقطه ‎eh‏
‏.کفته‌اند ‎aa Sy‏ ترکی است .
‎ald‏ بنم_اول و سکون ‎GU‏ و بای
ایجد » بزبان اندلس تخمی باشد بیار صلب
و ‎ash‏ نقره درخشنده و ‎ade‏ بود 9 چون‌آترا
با شراب بخورند سنگه مثانه را بربز اند ‎Gite‏
‏اول درعربی ‎Ole‏ هرچیزرا گوبندعموما- وبم‌عنی

(۱) چك : کائنات .

حل باشد خموصاً - و بمعنی بی گردانیده وعکس
هم آعده است - و ناسرء را نیز گوبن دکه‌بلرایج
‎acl‏ - و ‎ine‏ چپ هم هت له قوف راست
باشد ‎٩‏ .
قلبه - ‎gm‏ اول‌بروزن ‎le‏ چویی‌باشد
,کاو آ هن را بدان سب سازند و تزعین‌را شبار
‎OS‏ = بنتح اول وسکون‌نالی وفوقالی.
بمعتی قلتبان است که دبوث و فواده ویی حمیت
باه ۷ - ویکس اول. سای هندبراگویند ۸
‎LT,‏ بعربی حب القلت خواند . رنگه ‎OT‏
‏عودی ‎ath‏ و اندام او باندام کندم کوچکی‌بود .
‎OLS‏ = بنتم او بر وزن همزبان +
سنگی باشد کوتاء و آنرا بشکل امتواله تراشند
یعنی مدور طولالی و بر پشتهای بام غلطانند ‎٩‏
‏تا پشت‌بام سخت و محکم کردد - و مردم دبوث
و بی‌حمیت و بچشم خودیینو قوادمرانی ز ‎tain‏

< astucieux.rusé  شلقاو ‏«فلاش (ازفارسی)‎ : (rao Xe) ‏دزی نود‎ - ٩

id, - ۴

۴ قلفل = قلاقلا < قلاقل = قلقلان = ‎dolichos cuneifolius‏

+ دزی ج ۲ ص ۰۳۹۹ . مابرهوف آنرا محتملا با ‎crotalaria‏ ( از بقولات ) تطبیق میکند

. ‏راد : قلقل‎ . ۳۲۶ jae?

۴ سح قلاوز ‏ قلوز ‏ فلووز = قلابوز (ترکی بکسر قاف)

‎Laie‏ لشکر وراهیر «کاشفری ‎Ve‏ 404-8۰۳ » «رشیدی*.

‏هر که در ره بی قلاوزی رود

‏هر دو روزه ‎oly‏ صد ‎ML‏ شود.
« مولوی . مثنوی چاپ‌خاور صس ‎ANEN‏

‎herbe aux perles = Lithospermum officinale L.= ‏نم عربی‎ ۵

‏+عقار۳۲۹ ف» .

‎. ‏رل : قاموی , منتهی‌الارب , محبطالمحیط ء دزی‎ - ٩

‏۷ = قرت ‎(yw)‏ رك : فرته » قرتبان » قرتبوس » فلته , قلتبان . قلتبوی » کتبان ,

‎. ‏قرنی‎ cl

‎. ۳۹۲ ‏ج ۲ ص‎ Se? grémile= A

‎٩‏ = غلتبان , ظ . از : غلت [ قی : غلطك ]+ بان )=( « فرهنگه نظام».

‏بقیه ازسفحدٌ ۱۰۳۹

‏نکه وفلماخن ‎CC‏ بوده.» ولی بقول فرهنگه

‎yl Lau,‏ هرسه لفظ بفاسث و دراصل فلاخن سنگه
آطفری«قلا» ترکی وبمعنی‌فلاخن است. راه: فرهنگ‌نظام. امروز درتداول «قلاب سنگه» گویند .

########## pdf 375 printed ~ 1580
[pdf page 375]
کول ۲ زن اس
‎SI‏ = بر وزن و معنی کابل است + کاووس ‎sly be‏ بروزن ناموی ‎He‏
‏و آن شهری ‎th‏ ممروف ‎٩‏ - و مضفف بکاول | کی از پادشاهان کیان باشد ۴ ؛ و بسی نمرود
‎See‏ ترکان توشمال میگویند۴ -وسفرچی | راکویند 6 ؛ و جممی‌فرعون ‎wereld)‏
‏یز کت ۴ - کدی ‎Rog oi‏ پك ولطیف ۷" و اصیل و لجیب و مستولی باشد
‎UT‏ جریی کرات‌الکرم خوانند .کرم و ‎cee‏ | - ومژید بتأبید الهی را یز گوبند ۷ سوبمعنی
است در چهارم و سیم ‎AN)‏ شعله وشرر - ونتدی هم‌آمده است ۰ ورسم الخط
کاو نحك - بفتح ‎NE‏ و جیم‌وسکون آن در اين زمان بيك ‎gly‏ است حمچو طاوی
نون ‎aby‏ خیار بادرنگی را گوش دکه سبز وتاژه | وداود وامتالآن -
و بزرکه ‎Pash‏ کاو و لگ ۸ - ‎gow‏ اولکاورك اس تکه
است سرخ وزهردار وب‌وخالهای ‎oe‏ باشدویشتر بر وزن شاعول » بمعنی
در فالیزها بهم رسد و خربزه را شابم کند _ | چاشنی گیر است که سفرچی باشد - و ‎Jal‏ را
و کرم شب تاب را یز گفته اند که عروسك گوی که تیان توشمال میخوانند.
‎ath‏ . کاوه *۱-بنتح ‎sly‏ . تام آهنگری‌بوده

(۱) چك : چهارم وسوم ؛ چش : سیم زچهارم .

۱ -رك : کابل . ۳ جفتابی « بکاول » ( صاحب منصب » ‎SST‏ مأمور
چشیدن مشروبانت ) « جفتابی ص ۱۵۸ * ‎ay‏ : کاوول . ۴ - ,4 لفت فرسس۲۷۲.

۴ 5 7 پهلوی ‎ps « Kayds‏ ر کت ۱۲۵ » و باعنوان « کی» کیکاوسآمده . دراوستا
‎Kava ۵‏ جزء اول همان لقب(کی) (ه.م.) ‎col‏ و جزء دوم درست معلوم نست .بارتولمه
حدس میزند از ریش ‎USA‏ باشد بمعنی « دارای منبع فراوان » . وی در روایات ایرانی پر
‎aipivanghu‏ و ‎ty‏ کیقباد داسته شده . در بهرام بشت بند ۳۹ و زامیادشت شد٩۷‏ ازو نام
‎ory‏ شده . نام کاوی بصورت ‎Ushana‏ در وداآمده و بثابرین وی یکی از شهرباران دورة هند
و ایرالی است . رك : شاهان کیانی و هخامنشی بقلم نگارنده س ۳۷ .

‎ose - ©‏ پرواز کردن کاوس بربالهای ‎she‏ عقاب در بارة نُرود نیز روایت شده » هردو
را یکی پنداشته‌اند . ‎٩.‏ - درفرهنگه دساتیر : نظیف ‎yh - ۷  .‏ معالی از دساتیر«فرهنگه
سای ر ۲۵۹ . ۸ رك :کاورك.  ‎٩‏ - رك :کاول. *9- پپلوی162۷88 . ما در«اختر
کاوبان » و « درقش ‎Ob IT‏ » («.م.) تحفیقات خاورشناسان را نقل کرده ‎gal‏ . کرستنن رساله‌ای
‎ob‏ دانمار کي بعنوان ‎Smeden 162۷۵ og det gamle persike Rigsbanner,‏
‎ory D.Vid . Selsk . hist . fil. Medd ., 11.7‏ و کوشیده است ثابت کند که
اقمانة کاوه در اوستا و کتب دینی زرتشتی سابقه لداشته و ‎ue‏ بعهد ساسانی امت ( بابد دانست
که در اوستا اسطلاح 1626502 ‎Gaush‏ آمده . رثك : درفش کاوبان . م.م. ) » و متعلق‌بمهد
ساساتی است وآنرا - بطرز افسانه‌های بیار قدیمی دیگر - ساخته‌اند تا بتوانند اسطلاح«درقتی
کاوبان » را تعبیر کنند . و حال ‎GT‏ معنی حقیقی آن « درفشس شاهی » است (کاوبان‌مربوط
‎on‏ اوستابی ‎Kavi‏ شاه .کی » است . ره : کررستنن. سامان ص ۱۹۸ ح4).نيز کرستنن
‎ay‏ : من نميتوانم عقیده‌ای راکه ‎Justi, Levy‏ واخراً ‎Sarre‏ اتخاذ کرده‌اند مبنی‌براینکه
درفتی که بر موزاييك ممروف « جنگه اسکندر | ویز روی چند سک قدیمی پاری نقش شده,
هم
########## pdf 376 printed ~ 1581
[pdf page 376]
—\ear—

مشهور که فردون را بیدا کرد و برس ضحاك
آورد ۱ ۰ + درفش ‎GLE‏ موب باوست - و
ناف مشك را نیز کویند .

کاویانی ددفش ۴ ‎dee‏ دون
است منسوب ‎KG‏ + چه‌آن پوستی بوده
که‌کاوه در وقت‌کارکردن برمیان خود ميسته.

کاویدن (۱) ۳ - بروزن ‎Woe‏
‎ae‏ کافتن وجستجو کردن ۴ - وکیرابدست
وزبان آزار دادن باشد ۵ .

کاو یش - با اك بتحنانی رسید‌وبشن
له دار زده « تلروف و آنای دوغ و ماست را
‎Vue‏

‎Ys‏ بر وزن و معنی کابین است
که مهرزنان باشد و آن مبلفی است که دروقت
تکاح کردن عقرر کنند .

‏کاو یناث - بنتح نون و سکون ‎GB‏ +
درشیراز مطلق‌سار (۳) را گونند ‎gel‏ ازماخ‌خوار
وغیر ملخ خوار .

‏0 چش : کاونه .

‎. ‏چش : جاوبده‎ (yx)

‏کاب

‏گاه ‎Sn‏ ها . علف خشکه را
کونند ‎A‏ - و امر پکاستن وکاهیدن ‎٩‏ وضیف
شدن هم هت .

‏گاه پارینه ‎oly‏ دادن = ‎ats‏
‏از لاف زدن 6 وحکایت وسخنان گذشته گفتن وبر
گذشته فخر کردن و نازبدن ‎ath‏ و ‎ASOT‏
‏کپنه اد دادن هم میگویند .

‎oF‏ دبا *۱- ‎a‏ رای قرشت‌وبای‌ابجد
‎at DL‏ » صمخ درخت جوزی است ‎tobe‏
‏وببضی کوبند صمغ درخت جوزرومی‌استوبسبی
‎gay Nigel ine‏ خوانند , و بعنی‌دیگر کوشد
صمغ درختی است مانند پته , همچو ‎aS‏
‏سوزد ‎LT,‏ سیدالکباریت خوانند وکاء رامجانب
خودکشد . هر که با خود دارد از برفان ایمن
باشد » و بسن ی گوبند درحدود رون چشمه‌ایست
که برمیجوشد و چون‌باد ‎Oly‏ میوزدبته‌میشود
وکهربای خاصه آنست ‎LT,‏ بعربی مصیاح‌الروم
خوانند ؛ وبسن ی ‎ae SF‏ ستگی است زردهمچنان

‏که شبه سنگی است سیاه . اقاعلم .
(۳) چك ‎tee‏ سال .

‎) ‏داستان کاوه را فردوسی و طبری وبلعمی ومسعودی و ثعالبی وخوارزمی ( مفانیح‎ - ٩

‏و ابن‌خلدون وتواریخ دیبگرآوردهاند .

‎_f . ‏قبل‎ tated ‏ح‎

‏= کافتن(هم.) ‎GET?‏ ۸۳۷ >
۴ - یکاوید کالاش را سر بسن

‏۴ رك ‎Gap:‏ کلویان , اختر کاوبان » ‎Sys‏
‏از :کاو ‎Cpa)‏ (- یدن (پواد عصدری ‎ )‏ کایدن ‎Cem)‏

‏که داند که چه بات زر وگپر.
عنصری پلخی « لت فری ۶۱۷ *. .

‎QTL ci? ۵‏ مکاوند » و برکی بهانه و زحمت منهید. روزی شما میرسد.بدان

‏خرسند باشید .» « انجیل فارسی ص ۳4 * .

‏1 —> درسامی کوید ظرفی که درآن ماست

‏کنند و حرکت.دهند تا مسکه ‎OT‏ برآید » وبحذف الف لیز آمده» « رشیدی *.

‎(pm) ws = ۲‏ . رك : تذ ‎Ld WS‏ چاپ لیدن ج۱ ص۸۵ س ۱6 وص۱۸۷ی*۲
‎Lai,‏ ج۱همان کتاب ‏ صسکج . ۸ هندی باستان -1862, پهلوی]68 ‎cate gets‏ «ناوادیا
۲ ور : هویشمان: ‎ate‏ کردی ‎kab‏ ۰ 68 « ژابا س ۳۲۱ ‎٩‏ .

‎die Cake ‏اسشق‎ « kahrupai ‏رك : کاستن , کاهیدن . ۳ پپلوی‎ - ٩

‏ص۱۰۰ ‎Ne‏ با ‎kabrupak‏ > تاوادبا ۱۹۲ » .65,5 ‎keh - riba‏ « ژابا س ۰۳۲۱ ۳۵۲ >
مر کپ از : ‎Pol‏ ربا ( رباینده ) . مخفف‌آن ( ویز عمرب ‎COT‏ کپربا ‏ کپروا = ‎SUCCIN‏
‏(فی) « دزی ص ‎4٩40‏ : ۲» = (ممرب) کلربا «عقار ۱۹۵ *.

########## pdf 383 printed ~ 1588
[pdf page 383]
کبود پشت
رسیده و ثالك بالف "کشیده و ‎Ope‏ زده » دم
قربه‌ایست از مضافات لیشابور ‎٩‏ - و تخمی باشد
که آترا ‎al Le‏ خوالند .
کبوود پشت؟ = بنمبای‌فارسی‌وسکون
‎oot‏ ونای فرشت . کنابه ازآسمان است.
کبود حصاد - بسنی کبود ‎ct‏
‏است ۳ کهکنابه از آسمان باشد.

‎OF‏ - با دال ‎aml‏ بروزن کبوتر»

‎. ‏ماهیان کوچكخورند؛‎ VT, ‏باشددرآب‎ OS

‏وبستی گویند مرغی است آبی وماهی‌خوار ‎WT,‏
‏بوتیمارخوانند ؛ وجممی گوبند کرمی‌است‌بز رکه
وماهی خوار که جز درشب پیدا نشود وروزمخفی
باشد ۴ .

‏کبود طشت * ۰ بنتح طای حطی .
کنابه از آسمان است .

‏کبوده = بر وزن نبوده » نام چوپان
افراسیاب بوده ۷ - ردرختی باشد بز رکک۷ که
‎oT‏ لطیف و خوش آینده باشد ؛ و بعضی

‏(۱) چك » چش : و .

‏مهو ات

‏کوند درخث پشه غال است - و لوعی ازیید ,

‏هست ؛ وبسی گونند درخت بیدمشك است.

‏کبوس ۸ ۰ با راو مجهول بر وزن
مجوس » بمعن ی کج وناراست ‎ath‏ . ودرفرهنگه
جهانگیری باین معنی بجای حرف ثالی‌بای‌حطی
هم‌آمده است .

‏کبوكه ‎٩‏ @ بفتح اولرئانی ‎sly‏ کشیده
‎Gy‏ زده ؛ مرغی است کبود رنگه بمقدارباشه.
‎SS‏ با هم جنس خود جفت نشود ؛ وبسنی
کویند مرفی است آبی وسرخ رنگه ‎UTS‏
‏سرخاب گویند وترکان عنقد خوانند - و بتشدید
تانی ‎Aske‏ باش دکه عربان ابوالءلیش‌خوانند.

‏. کبه ‎el‏ بنم اول و فتح انی مشدد »

‏شيشه با شاخ با کدوبی باشد که حجامان آنرابر
محل حجامت نهند و بمکند ۱۱ و معربآن‌قبه
است - و برآمدکی هرچیز را 55 گوینداوبفیس
تشدید هم درست است ؛ و پفتح اول نیز بنظر
‎oul‏ است؛ وبا بای فارسی هم هست.

‎٩‏ - در معجم البلدان یاقوت آمده : « کبوزان بذال معجمه و آخر آن نون ؛ موضی
است .> ۴ - مصحف : «کبود تشت, یمتی آسمان » « رشیدی »- کبود طشت ( «م. )

‎. ‏تشت وخایه < طشت وخایه‎ oS ‏طشت‎ : dy

‎“tert

‏۴ -«کبودر »کرمکی بود خرد درآب . خورش او ماهی خرد بود (ظ . وخورش‌ماهی

‎: ‏دهشدا ( رودکی (سمرفندی ) کوید‎ . oy
‏ماهی آسان گرد کبودر ۰ گوبی‎
Cem) ‏تشت‎ oy Sm 6

‏بولت ماهی است دشمنانت کبودر. < افت قری*۱۹ *.
۱ رك : فهرست ولف .

‎Populus 2102 - ۲‏ درختی از نوع ‎hae‏ ازتیرء بیدها «گل گلاب ۲۷۲ .

‎. ۳۲۱ ‏-قی :کردی ۷۵002 ( فوزی ,کوژ ) « ژابا‎ A

‎٩‏ = «کپوك » مرغی است آسمان کون » چند باشد و او را از جنس خود جفت نبود.
کرد مرغان کردد تأ از ابشان بچه‌آرد . منجيك (ترمذی) گوید :

‏خارش ‎ST‏ و بضوی اندر غمی شده

‏همچون کپوك خواستمی جفت کام‌کام.

‎. ‏حمچون کبوك خاسته می‌جست کامکام ) » « لغت فرس ۲۸5 -۷ ۴ . فس: کبوتر‎ : JO)

‏۶- رك : قبه .

‎aly gb wy‏ بمکد وال

‎Looe 4 Som ۱‏ حجامان بود. معروقی گوید :
کیرتو کوش ‎Soe‏ مکد ‎Sy‏

‎. ٩ ۵۷ ‏فرس‎ cal?

########## pdf 384 printed ~ 1589
[pdf page 384]
کبی - بر وزن صبی ۰ میمون سیاه‌را
گونند ‎٩‏ .

کییتا (۱) - بنم ارد و فوقانی بالف
کشیده بر وزن هوبدا , حلوايی باشد که از ‎Pe‏
‏بادام و پسته وگردکان و کنجد وامثال ‎OT‏ پز ند
وآنرا حلوای‌متزی‌هم ‎a Kae‏ وبعربی ناطفه(۲)
خوانند و معرب ‎OT‏ فبیطا بائد ؛ و بسنی کوشد
‎yh‏ است که ازشکرو کنجد پزند ۴ - ویضم‌اول
‎gt Sy‏ طمامی است که از خمیر آرد گندم
سازند و خورند و بعربی قطایف گویشد ‎ST,‏
‏قطایف نیت چه بعریی ‎ty‏ قطایف را کنافه
مخوانند .

‎pee CET‏ اول و فتح انی و رابع
وسکون تحتانی وکاف ‎LT‏ زنه راکوبند وآن
آلتی باش دکهآسیا را بدان تیز کنندگ .

‎ated diy y's POST‏ بمعنی کبیتا
امت که حلوای مقزی باشد ۵ .

‏کبیچه ‎che (r)‏ اول بروژن‌دریچه,

‏چارواییرا گونند که زیر ‎oles‏ او ورم وآمای(ع)
(۱) چش : کبییا .

‏(4) چش :- وآمای .

‏(۷) چش : داطقه .
)0( چش : طلا واقره.

‏که

‏کرده باشد - و پشت خار را ‎ja‏ کوبند و ‎OF‏
‏چوبکی باشد که باندام ‎dents‏ دست با اندام‌دیگر
سازند وپشت بدان خارند .

‏کمیك ‎oe‏ اول بر وزن وزید , لحیم
زرکری ‎we Sl,‏ وآن چیزی باشد که طلاونقره
ومی را باآن بهم وصل وپیوند کنند ‎٩‏ -وسریشم
را ليز کوبند و آن چیزی بائد که درودگران
‎oye‏ )0( واستخوانرا بدان بهم چبانند ‎٩‏ .

‏کبیدن - بکسر اول بروزن نشیمن ۰
بمعنی ازجای کشتن وازجای کتبدن و کردانیدن
‎ath‏ .

‎pao OT‏ اول و کر ثالی بر وزن
کلیچه . آردیراگویند که گندم آنرا بربان کرده
باشند - وآرد برنج رنخود وجوبربا نکردءوغیر
پربانکرده را ‎Ga‏ گوبند - و بمه‌تی دلیده (5)
هم آمده است که درشته و شکته شد نکندم
ویلغور باشد .

‏کبیسه ۲ - بر وزن هربسه » زسادتی
بائدکه آنرا مثجمان در ماه شباط اعتبار کنند
(۳) چش :کبیچه .

‏(۰) چش : ولینه .

‏۱ - کبی‌دربرهان میمون ‎he‏ لوشته واین از دووجه خطاست : یکی آنکه بای فارسی
است‌نه تازی « دوم[ نکه‌قیدییجاست .(سراجاللغات بنفل فرهنگه نظام ج ه ص لط . ) هوبتمان
( ص۸۷ ) «کبی» فارسی را معادل «کپی» داند . رثك : کپی . ۰

‏۴ کییته ۳ فیطه (ممرب) ‏ قبیطا (معرب) ‏ فبیده (درتداول) « کییتا . ناطف

‎: ‏مرغز یکوبد‎ lb say
‏ور همه زندکان ترینه شوند‎

‏۴ رك : جهانگیری .

‏۷ -رك :کید .

‏ت وکبیتای کنجدین منی .* « لفت‌فری ص۷ ۴ ۰
۴ کییتا ( معرب : قبیطه ) .
‎٩‏ -کرم کردم تخته‌بندش ا ‎ES‏ کنجدی

‏وز شباد نخم مرغش برقلم ‎hae pine‏
‎ble,‏ « فرهنگه ‎ot piles‏

‏۲ از سربانی کبدشتا « ‎ESF an ۲ Pr)‏
عربی ار ‎te‏ نبد ‎Yo‏ =

‏بالناه. کم آمد سال‌ای‌التی‌بسترق‌منهایوم وذلك فی کل اربع‌سنین.» « منتهی‌الارب » چون مدت‌سیر
‎ch,‏ دور زمین ( وبقول قدماآفتاب ) ‎Wo‏ روز وه ساعت و ‎4٩‏ دقیقه وکسرست ۰ معمولا سال
را ۳۹۵ روز گیرند و کور مزیور را محفوظ دارند تا در هر چپار سال يك روز حساب کنند و
برروزهای سال بیقزایند تا درجمله ۳۹۹ روزشود . رك : التفهیم ۲۲۲-0۱ . و عربیآن دی ۰
است «گاه شماری ‎Aveo Glee‏
```


## [2026-09-06T15:48:11.318Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8').read()\nblocks=t.split('\\f')\ndef find(pat):\n    out=[]\n    for b in blocks:\n        m=re.search(r'\\[pdf page (\\d+)\\]', b)\n        if re.search(pat,b): out.append(m.group(1) if m else '?')\n    return out\nfor w in ['کبست','کانون','قفس','کبستو']:\n    print(w, find(w)[:12])\nEOF",
 "description": "Locate headwords in Borhan v3 OCR"
}
```


### [2026-09-06T15:48:12.880Z] TOOL RESULT

```
کبست ['14', '248', '381']
کانون ['373']
قفس ['286', '327', '529']
کبستو []
```


## [2026-09-06T15:48:16.475Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 - <<'EOF'\nimport re\nt=open('BQT_v3_pages.txt',encoding='utf-8').read()\nblocks=t.split('\\f')\nfor want in ['381','373','327']:\n    for b in blocks:\n        m=re.search(r'\\[pdf page (\\d+)\\]', b)\n        if m and m.group(1)==want:\n            print(\"######## pdf\",want)\n            print(b[:3000]); print()\nEOF",
 "description": "Print Borhan pages for kabast, kanun, qafas"
}
```


### [2026-09-06T15:48:19.949Z] TOOL RESULT

```
######## pdf 381
[pdf page 381]
aS
‏را ماست با‎ col JT te ‏آش: کیر باشد‎
‏گویند. با بمعنی‌آش است‎

کیرد = ‎ch‏ ۳ و الی‌وثالت‌وسکون
کاف » کیاهی است خاردار که ‎IGT‏ بعربی ‎CLs‏
‏و بثیرازی خارسوحك و صفاهالی هردا گوبند
و در مرب حمض(۱) الامیر خوانشد.ضماد کردن
بر ورمهای گرم تافع است .

کیروا ۱ باواو بر وزن و ‎we‏
‏کبرپاست که آشکیر باشد چه درفارسی‌بای!بجد
و ‎Jas ce aly‏ میابند چن‌انکه ماست با را
ماست‌وا هم میگو بند .

کبریت ۴ = یک اول وسکون ثانی
و ات بتحتانی رسده و بفوقالی زده ۰ گو گرد
راکوبند وآ نکرم و خشك است ددچهارم وافام
آن درک و کرد مذ کور میشود = و زر خالص را
نیز گفته‌اند . عربی‌است

کیست © بفتح اول وثانی بروزن ‎oS‏
‏رستنیی‌باشد تلخ شبیه بدستنبوی که بعربی‌حنظل
وبفارسی خربزهتلخ گویند؟ . و ‎aah‏ چارموضع
شخصی را عقرب گزید دو درم حنظل بآن شخص
دادند تا مخورد. همن که خورد درد بررطرف شد.

(۱) خم۱ : خنس

. ‏(هم)‎ b= ۱

رو اس

اکر حنظل را بمقدار ‎ety‏ ناختی سوراخ کنند
و پراز دوغن زبق ‎Wik‏ و سوراخ ‎LT‏ باخمیر
محکم بگیرند و بر بالای آنش نهند تا جوشی
چند بزند و بعد از ‎OF‏ بردارند و برموی سفید
مالند سیام کند. ‎oly‏ خضابیت آزموده؛ وبسنی
کویند کیست غیر حنظل است وآن گیاهی باشد
بغابت ‎ight‏ وزهر ‎Jee‏ را نیز کبست گویند -
و در ‎Meith fe‏ پوست نی‌شکر را گفته‌اند.

کبمتو * = بر وژن ارسطو » بمعنی
‎Sash ST‏ زه ‎AS‏ و حنظل است

کسته * = بفتح اول و ‎yt‏ و سکون
سین و فوقالی » بمعئو کبتو بائد که حنظل
وزه ‎AS‏ است .

‎SS‏ بنتح اول و سکون انی و کاف
تازی » دست را
گوبند که‌عربان
بدخوانندوبضی
کف دست را
گفته‌اند ‎٩‏ -و
باکاف فارسی پر نده

‏ایت مشهور و معروف۷ - ‎ob‏ دوقسم میباشد:

‏۴ - در زبان اکدی صورت ‎Kupritu‏ آمده و ازآنجا

‎۰81۳۵6 ‏ودر عبری‎ Bafti ‏ودرآرامی فلسطین‎ guetta ‏زبانهای‌سامی دیگررفته. درآرامی‎ ine

‏در عربی« کبربت» «معجمیات عربیه - سامیه ص ‎NAN‏

‎pS = ۳‏ = کیته (هم) :

‏کیست نام فارسی ‎he‏ است « فولری ‎TE‏ ۰۷۹۱ ۶ عقار ۱۵۸ ف »۰ معرب آن کية است

‏«عقار ۱۵۸ © اوستا -
روز من کشت ازفراق تواشب

‏۴ کست ۴ کسته ‎Cem)‏

‎«bis ۸۵۰ ‏«اسشق‎ kapast ‏پهلوی‎ .kapasti
‏دال ]دهخدا) کبست.‎ gg] ‏توش من‌شدازآن دهاات(از اندهانت‎

‏اورمزدی ‎ol?‏ فری 4۵ >.

‎oS = 8‏ کبتو (هم):

‏با ابنهمه لطافت وشیربنی‌سخن ‏ با من‌بگاه ‎Cab‏ زدن‌چونکیسته‌بی. نزاری قهستانی «رشیدی».
۲ - سراج احتمال میدهد باين ‎ine‏ «کقك » را بتسحیف خوانه‌اند «فرهنگه‌نظام».
۷ - قن : مانسکریت ‎kapinjala_‏ ( دراج (. بلوچی ‎kawinjar . kapinjar‏
‎(LS)‏ »کردی ع ‎qewgh , keu‏ قی ‎kabk sisal. kawk , kdik gus:‏ بلوچی
8 , 18۷8 . رك : اسشق ۸4۱ ‎ELT‏ پرنده‌ای از ‎tes‏ «ماکیانپا» است که بجهت استفاده

‏از کوشت

‏وی ۰ آلرا شکا رکنند .


######## pdf 373
[pdf page 373]
کان ’= بسکون نون معروفت‌وعربی
ممدن خوانند سوبمعت ی کندن هم‌هست؟ .

‎UT‏ »بر وزن دانا . بمعنی نادان و ابله
و احمق و یعقل باشد ۴ - و چوب بن خوشةً
انگور وخرما را یز گوبند ۴ - ویارای‌ازخوشةً
الگور وخرما را هم کنته‌اند۴ .

‎be‏ ؟ © پسکون زای تقطه‌دار بروزن
‎ht‏ چوب بن‌خوشتخرما را گومندیمنی‌جابی که
بنغل چسییده باشد ۵ .

‎OS » TOT‏ نون‌ودال ابجد.بمعنی
قند است - وشکررا نیز گویند .

‎we Set . ‏بنتح کاف‎ » SOT
‏کهکان را میکند ۷ - و امر بان معتی‌همهت‎
DB ping - ‏وفرهاد را بیز گوبند بطریق کنایه‎ -

‎. cds -:۱ ‏خم‎ )۱(

‏مرو

‏ت کیب اخافی است ۸ .

‏کانور © بروزن کافور ء کندوی غله را
کوبند بعنی ظرفی که غله درآ ن کنند.

‏کافون = بروزن فانون , بیعنیآتشدان
باشد مطلقاًاعم از کلشن با منقل آنشی ‎٩‏ -
و کیرا یز کوبند که مردم او را کرامی دارند
و مخنش قبول کنند - و طرز و روش و قاعده
را نیز گویند ‎-٩*‏ و بلفت سریانی نا بستی از
ماه‌های رومیست کهکا نون اول وکانون آخر ‎cash‏
‏وآن ماه سیم وچپارم است ‎MY‏

‏کانیرو @ با تحتانی‌مجهول و رای‌قرشت
‎sly‏ کشیده بروزن نانیکو » دارویست که آنرا
مازربون گویند و بجهت دفع (۱) ‎Wt‏ بکار
‎aT‏ .

‎XV AEN? ‏(مسدن)‎ KAD ‏کندن ) «اسشق ۰۸۳۹ . پهلوی‎ ( kam ot ‏پارسی‎ - ٩

‏کردی ‎Kad‏ ( ممدن . فلز ) « ژایا ۳۷۳ > .

‏۴ « خویشتن ‎US‏ ساخته ‎soy‏ چیزهایی کرد که مردمان از آن ‎clas) agate‏ ©

‏« تاریخ سیستان ص ۷۹۹ وص بط ؟ .
۴ « کناز ‎Cpe)‏ = کنز(هم).

‏(سمرقندی) گوید :

‎Lie ۴‏ «کاباز ۴ (هم.) ۰

‏۵ « کااز . بن ‎es‏ رطب باشد.رودکی

‏من بدان آعدم بضدمت تو که برآید رطب ز کانازم .> «لفت ‎SVG DS‏
‎dy - ٩‏ قند ,کند ‎ .‏ ۷ -از:کانط کن (کننده) ۰ ۸ - ظ . مصحف «کاف
کن » ‎pe)‏ کاف دوم) اشاره به« کن‌فیکون» ( ‎Sear‏ ۳۹دیی» ) باشد.  ‎٩‏ -کانون در
عربی و سربالی بمعنی آتشدان است و نیز بدو ماه کانون اول و کانون دوم اطلاق شده » واصل
کلمه سامی‌است, وآن ازعصر اکدی بدین دوماء اطلاق گردیده. درزبان اکدی 68008011 بمعنی
(آنشدان) است وبپربك‌ازدوماه مزبورهم ‎cond CAT‏ بدین اعتبار که درآن دوء‌سرمای زمتان‌ظاهر
کردد ومردم باخطرار در کانون (آمشدان)آتش افروزند. « معجمیات عربیه - سامیه ص ۲۷۰۳ :
راست کفتی سپه رکالون کشت واختران اندران میان اخگر .
« معزی تیشابوری س ۱۲۷*.
*- از بونانی ‎Canon  ]8060‏ )4( قاعده » فالون . دائرةالمعارف اسلام: ‎ORT‏
‎-٩ ce‏ این تام در کتیبه‌های پالمیررآمده (رك: ‎S.A.Cook,A Glossary‏
‎Of the Aramaic Inscriptions‏ فهرست. نحت‌همی‌کلمه) و آن‌مطایق ‎marheshw4nt,‏
‎oy‏ . بعدها کالون نام دوماه سربانی کردید ‎pon‏ ۲.46600 با 420۳۵3 و ‎bray‏ ع .
در عربی این ماهها بنام کانون‌الاول و کانون الاخر مستعمل ابت . « ونیشکه . «ائرة المعارف
اسلام ‎ao og:‏


######## pdf 327
[pdf page 327]
قلر: آب ۱0۳

عرع رکه سرو کوهی ‎th‏ میگیرند و آن را ‎wl‏ .

بعربی حياة المونی خوانند ۱ ۱ قتظرهر دنس ‎gine‏ پوبه کردن است
قظرق ‎OT‏ = مبرون ‎et‏ کنابه | که نند و تیز براء رفتن باشد ۴ .
از تیغ و شمشیر ۴ و پیکان ‎wi‏ واسلحة صبقل قطر 9.958 — بنتحزای شله‌داروسکون
زده ؟ هم هت . را و دال بی نقطه , کتابه از آقتاب عالمتاب
قطره 555 (۱) ‎alse‏ از ايرباند | ‎ect‏
‏که عربان سحاب کوبند ۴ و آنرا آب دزد هم
بیان دوازدهم

در قاف با فا مشتمل بر ده لفت ‏ و کنایت
قفا ور ‎ol‏ مت ‎GG‏ فارسی ‎ots‏ | داکویند ۷

از مظلومان باشد ۴ . قفس = بفتح اول و ثانی بروزن‌هوس ‏
قفاهیر * - بر وزن مثاهیر » صورت | معروفت و آن ‎x tle‏

خوب و روی ‎SI‏ را کوبند . باشد شبکه‌دار که از
قفای‌فلك حه کنایه از حوادث فلکی چوب و برنج و آهن‌و

است ۴ . امثال آن‌بافندوجانوران

‎yo‏ بفتح اول و سکون ‎GE‏ و رای ‎ig‏ و حشیرا در آن
‎ects‏ نام دارومی است‌که آنراکتوت )9( | کنند ۸ و معرب آن
خوانند و آن‌مانند عثقه برخارترنجبن پیچد ‎AV‏ | قص باشد صاد بی -
و در عربی زمین خالی و بیابان بی ‎OT‏ و علف | نقطه ‎٩‏ (۳) .

‏(۱) چك. چش : فطر؛ دزد . (۷) چش : کشوت.

‏(۳) چك: - بی‌قطه .

‏۱ - (مر) « قطران کظربان . شبر# درخت ابهل ‎pats‏ ارز ومانند آن , فطران بالفتح
والکر مثله » < منتهی‌الارب » از ماد ق ط ر عربی (چکیدن) = ‎goudron‏ (فر) دار ۳4

‎dW ۴‏ رشیدی . ۴ - در رشبدی > قطره دزد یمنی آفتاب - و بعضی ابر را
کفته‌اید.» ‎Uy‏ بهر دومعنی صحیح است و راجع ‎OT a‏ دزد » رگ : مزدسنا س۳4 -
‎HF‏ : رشیدی . ۵ دربارٌ ‎UIT!‏ مسحف درصفحهٌ نود ودو ‎Oley Leads‏

‏توضیح داده شده . ۱ - مصحف «قفز پزای معجمه؛ نبات کشوث است.»«تحفشحکیممومن».
۲ - رك : قاموی » منتهی‌الارب . ۸ - اصلا بونانی‌است . (نقی‌زاده . یاد کار 4
‎(VY‏ در ‎gly‏ 68۳98, لانینی 68۳58 بمعنی جعبه وسندوقةٌ است . مولف «تفس» این‌وجه
‎Glee!‏ را نمی‌پذیرد و کلمه را عربی محض میداند . ‎٩‏ - (عر) ‎a?‏ مح رکه » ینجره
‎AT,‏ است‌کار کشت راکه کندم درآن کرده بغرمن آرند . » «منتهی‌الارب» - سبدی که پرند گان
را ‎oS ols‏ ببازار برد « دزی ج۲س ۳۸۳ .
» یل - رك : لفات ‎ATOLL Gi‏
```


## [2026-09-06T15:48:51.021Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD kapic ===\"; grep -n \"kapīč\\|kapic\\|kabīz\\|kapīz\" PHD.txt PHD_mackenzie.txt | head\necho \"=== PHD kapast ===\"; grep -n \"kapast\\|kabast\" PHD.txt PHD_mackenzie.txt NYB_vol2_glossary.txt | head\necho \"=== PHD casp ===\"; grep -n \"časp\\|caspīdan\\|cafs\" PHD.txt PHD_mackenzie.txt | head\necho \"=== NYB kanun/kapic ===\"; grep -n \"kapīč\\|kapic\" NYB_vol2_glossary.txt | head",
 "description": "MacKenzie and Nyberg lookups"
}
```


### [2026-09-06T15:48:51.113Z] TOOL RESULT

```
=== PHD kapic ===
=== PHD kapast ===
=== PHD casp ===
=== NYB kanun/kapic ===
```


## [2026-09-06T15:48:52.897Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG kap/caps ===\"; grep -n \"časp\\|cafs\\|capsīdan\\|čafs\" CHEUNG.txt | head -20\necho \"=== IEC 473 area: kap ===\"; grep -n \"kap-\\|kapiō\\|capiō\" IEC.txt | head -20",
 "description": "Cheung and Mann lookups"
}
```


### [2026-09-06T15:48:52.961Z] TOOL RESULT

```
=== CHEUNG kap/caps ===
3314:rob’ (LW), Bal. campit/Camp-, canpit/Canp- ‘to snatch’, NP cafsidan, Abz. 
=== IEC 473 area: kap ===
6740:kap- ‘seize, take’, etc. see kapið
6745:kapolos, à (kapol-) “holder; knob, head, top’. WP L 346. Cf. kapið, kapsel- Skt. cf. kapalam ‘skull, bowl; potsherd, lid’; Lat. capulus, um ‘hilt; penis; coffin; noose’; capula ‘cup’; cf. Br. kavel (pl. kavellu), beside kével, m. (‘cradle, basket, fish-crate’, fr. a type *kapsilo-); OE hafela, hafola ‘head’; ON he- fill, pl. heflar ‘reefknot’; Mod. cf. hafald, n. ‘heald’; Fris. cf. haffel ‘mouth, snout, beak’; MHG, MLG hebel, hevel ‘lever’; Finn. LWW kapula ‘round stick’; kappale ‘piece, head’; kapla ‘fetters’; kapalo *swaddle-band'. (The di- versity of meanings can be combined under the caption kap- ‘hold’, see kapið. Cf. kop-)
6748:kopiec ‘mound’; (kopica ‘pile, sheaf is prob. to kop-, q.v.); Cz. kopec “hill; Li. (LW?) kap- čius ‘hillock’ beside kapurnas, id.
6749:(kapitos, å variant of kaptos, å, q.v. and cf. kapið, kap- “hold, holder’ MHG hebede ‘possession’; ON hefð ‘right of possession’; Sw. hävd, pl. -er, id. beside häfta ‘constipation’; häfte ‘handle; stitch’)
6750:kapið, kapmi ‘take, seize, lift. WP I, 342. Cf. kap- and cpds. Gk. kápo, kápto; Alb. kap; Lat. capio, Ere; W cáf, 3s: caiff “will have, will eet: Go. hafjan ‘raise, heave’; MHG haben, hàn (1) “hold”, beside heben, MLG heven ‘raise; begin’; ON hefja, id. beside Sw. håva ‘net, catch’; Li. cf. kápt! ‘grab! gotcher! beside (*-a-) kopiu, -ti (2) ‘grab’; Latv. kapju,t ‘climb, go, march’ be- side nasalized kampju,t ‘seize’ and kapju,t (2)
6762:kapnos (?), (kap-) ‘soot, smoke’. Cf. kuap-. WP I, 379 Gk. kapnós ‘smoke, soot: Myc. cf. kapinija (for *kapnja *chimney"); cf. Gk. kápo ‘exhale’; Sw. (?) hamn (2) ‘shadow’; OCS cf. kopoti, m. ‘soot’; R. id.; beside Li. kvapnüs ‘vaporous, aromatic”
6769:kansalos (kapsilos, kapsulio-), à, om, io “holder; container”. Cf. kapsos, kap-, etc. WP I, 342
6772:kapsð (form of kap-, see kapið, kapmi) “catch, seize, hold’. WP I, 342 Per. cf. Caspam ((adhere', but Per. č- derives fr. *k- usually before IE *-e/i); Arm. kabnum ‘shut, cover’; Lat. (Plautus) capso, 3s capsit, v. “will take’; W caffio “catch? beside caiff 3s ‘will take, get’; OE hæpsian ‘fasten’; Li. kap- siù, éti ‘peck’
6773:kapsos, å “hold; holder’. Cf. kap-mi, kapið, kapso, etc. Arm. cf. kapank “enclosure, lid, trap'; Gk. kápsa “box, chest'; Lat. capsus, -um ‘stall, pen, coach-box'; capsa (as Gk. LW?); LLat. capsus “bladder, holder, nave’; W caff, pl. -iau ‘grasp, grapple, dungrake'; OHG haspa ‘skein’; MHG haspe ‘clasp, buckle’; OE haepse ‘hasp, clasp’; ON hespa ‘hasp; skein’; Sw. haspa ‘bolt, latch’. WP I, 342
6775:kaptos (kapitos, a) “held, captive; hold, hol- der, slave'. Cf. kap-, etc. WP I, 342 Arm. kot (“handle”, fr. *kaptus, phonol. of ko- toy ‘column, obelisk’ fr. Lat. capitulum); kajt', i-st. (2) ‘basket’; Lat. captus, adj. captus, üs, m.; Ir. cacht ‘servant’; Mir also ‘shackle’ (f.); Br. kaut, kavut, v. inf. “have, hold, find"; m. <‘ possession”: W LW? caeth ‘enslaved; slave’; Go. hafts ‘having’; OHG haft ‘caught, held; captive’; MHG (‘bond, fetter; f. ‘capture’, also as OHG); OHG (variant) habid, habida, MHG hebede ‘possession’; ON haftr, f: hafta ‘pri- soner’; hepti ‘haft; OE hæft, m. ‘bond; priso- ner’; haft, n. ‘haft (adj. ‘captive’); Latv. kāpt, inf. ‘to take? (beside iz-kapts, gp -kapčću, f. (‘scythe:. Of ambig. phonology, cf. kop-). De- nom. in Fris. heftsje, Du. hechten, Sw. häfta, Norw. hefte, etc.; variant in Ir. caist. f. ‘deceit, guile’; W cast, pl. iau, m. ‘trick’ (fr. *kapstis). See kaptio for further exx.
9150:Ks-kap-, aphetic for eKs-kap-, see eks, kap- Oss. sKüfín, äskäfín ‘snatch’; Lat. cf. ex-cipið, id.; Cz. cf. chopiti, inf. id.
15424:skåbh- ‘scab, scale, sore, canker’. WP II, 562 Lat. scabiés, gs: -iēi, f. ‘scab, ch": MHG schabe, wf. (2) ‘moth, grub’; OE -sceafa, wm. (in mæl- ‘canker’) beside OE sceabb- in -ede, adj. ‘scabby, sore’; E scab (from Norse}; beside shabby, adj.; Sw. skabbe, wn. ‘scab’ beside skabbig, adj. ‘scabby’; (long-gde in) Upper MHG schuop, schuope, s. & w.m. ‘scale’; schuopen, v. ‘flake off”. Verbal types in Gk. Skápto, aor. pass. eskáphēn, v. 'dig'; Lat. scabo, ére, pf: scabi, v. “scratch? beside sca- beo, ere, v. "be scurvy’; LLat. scabio, Ire, v. ‘tch’; Go. skaban, wv. (shave. Gmc. forms ambig. cf. skap-); MHG schaben, OE scafan, sv. 6.; ON skafa, sv. 6 p.t. skóf, v. ‘shave, scrape, pare’; R cf. skoblit, inf. id.; Li. ska- biù, skobti, v. ((1) ‘têar, pluck, trim’. Iso- phonic w. skåb-type above); Latv. skabīt, inf. “hew, fell
15440:skabhtos (assimilated to skaptos. Cf. skăbh-, and skap- as a separate entry) Gk. skaptós, adj. (dug, diggable'. Here, in view of skápto, pf. éskapha, v. 'dig); OE (ambig.) sceafóa, sceafoóa, wm. (“chip, shav- ing’. Cf. skap-); Li. skábtas, m. ‘gouge’
15472:skapo, ið (skap-) ‘chip, dig, scrape, Cut, Cf. skabhos (2). WP II, 560 Oss. cf. Küpi, kapi, s. “hoe, hook’, fr. *skhàp-); Gk. cf. skapáne, f. “hoe, spade’; Alb. hap, v. (- nji gropë ‘dig — a hole"); Lat. cf. scapula, f. 'shoulder-blade'; (ambiguous forms are Go. skaban, sv. 6 and Gmc. generally, see skabh-); OCS (ambig.) skopljo, skopiti, v. (&castrate', but cf. skop-); Li. skapiü, inf: skópti, v. Cgouge, scrape, cut, strip, pluck’: *á/a) cf. skaptos
15789:skopeið, skopio ‘cut, strike’. Cf. skopos. (Vo- calism of Balto-S1. ambig.) Br. skei, pp: skoet, v. “beat, strike’; OCS sko- pljo, skopiti, v. ‘castrate’; R skopit,, inf. id.; Li. cf. skaptas, m. ‘carver’ (vocalism ambig. cf. skap-)
```


## [2026-09-06T15:49:02.486Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3295,3325p' CHEUNG.txt",
 "description": "Cheung context for cafsidan"
}
```


### [2026-09-06T15:49:02.545Z] TOOL RESULT

```
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
/(#)sk’aft (sk’avd) ‘to carry, drag (quickly); to grab’, Wa. skaf- ‘to slip, shift to’ || (+ 
*ni-) Oss. I. nysevyn/nyzavd, D. nizzvun/nizevd, (inch.) D. niz&vsun/niz&vst ‘to 
touch (on)’, ? Sh. (Baj.) nijüv-/nijüvd ‘to pack up, put to bed’ || (+ *ham-) Oss. I. 
anzavyn/znzavd, D. anzzevun/enzevd ‘to touch’. > The derivation of Wa. skaf- 
from *us-kaf-, with prev. *us- ‘up’, is semantically implausible, cf. *us-kas’ ‘to
```


## [2026-09-06T15:49:04.551Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8').read()\npages=t.split('\\f')\nfor i,p in enumerate(pages):\n    if 'kapsō' in p or 'kapso (form of kap-' in p or \"kapsð (form of kap-\" in p:\n        print('leaf',i,'-> printed ~',(i-15)*2)\n        break\nEOF",
 "description": "IEC leaf for kapso"
}
```


### [2026-09-06T15:49:07.631Z] TOOL RESULT

```
leaf 271 -> printed ~ 512
```


## [2026-09-06T15:49:19.482Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8').read()\npages=t.split('\\f')\nimport re\nfor i in (269,270,271,272):\n    p=pages[i]\n    print('--- leaf',i,'---')\n    print(p[:200].replace('\\n',' '))\n    print('...tail:',p[-200:].replace('\\n',' '))\nEOF",
 "description": "IEC page numbering check"
}
```


## [2026-09-06T15:49:19.825Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '3325,3350p' CHEUNG.txt",
 "description": "Cheung etymology note for *cap"
}
```


### [2026-09-06T15:49:21.803Z] TOOL RESULT

```
--- leaf 269 ---
ta) beside Mod. Br. cammed, f. (/pace, step; felloe’, whence Lat. gambita > Fr. jante & E jaunt); Gaul. cambutta (err. for *cambitta (?) *shepherd's crook’); Arm. kant, s. “holder, handle’. (The prove
...tail: atv. kankars, m. 'tatter) kankulos, à (?) Gk. kagkülé (fCoakgall. Hes.); Blg. kákül rer got’ (kannəbis, see Supt.) (kanthos, us, kant- ‘side, edge, corner’. As- sumed to be a Celtic form of type *kamp
--- leaf 270 ---
tós, with contamination of Gk. kanthós). WP I, 351 Gk. kanthós (‘corner of the eye’. Of uncertain relationship w. the following forms. LW in Lat. canthus, id.); Alb. kând, kënd ‘corner, tip, edge’ (Al
...tail: con- tinent kapnos (?), (kap-) ‘soot, smoke’. Cf. kuap-. WP I, 379 Gk. kapnós ‘smoke, soot: Myc. cf. kapinija (for *kapnja *chimney"); cf. Gk. kápo ‘exhale’; Sw. (?) hamn (2) ‘shadow’; OCS cf. kopoti,
--- leaf 271 ---
 m. ‘soot’; R. id.; beside Li. kvapnüs ‘vaporous, aromatic” (kapõl-. see kapolos. Only in Skt. kapalam ‘skull’, etc.) kapos “hold, holder, holding". Cf. kapā, ka- pio, kapolos and next. MLG cf. haven,
...tail: ios, see kapitios. (A variant capud oc- curs in LLat. AS:GLL) kar- (1) “love, desire’. Cf. kāros (1) Arm. cf. karawt, Let (‘desire’; adj. ‘needy’); Hitt. cf. kariyami ‘yield, gratify’; MIr. car, adj. 
--- leaf 272 ---
“loving”; cara, pl. carait ‘friend’; Ir. caraim, v. ‘love’; cara, pl. caraid ‘friend’; Br. kér “belov- ed’; W caru, v. ‘love, like’; OW car, pl. carant ‘friend; kinsman’; W câr, pl. ceraint, id. be- s
...tail: gs"). The apparent isophones: OCS -krakü “leg? in dlügo-? long-legged'; Srb. krák, Blg. krak-át, m.(!), id.; Li. kárka "bock, ham, fetlock, trotter, lower leg of insect; R Ó-korok ‘ham’ point equally
```


### [2026-09-06T15:49:21.847Z] TOOL RESULT

```
from *us-kaf-, with prev. *us- ‘up’, is semantically implausible, cf. *us-kas’ ‘to 
ascend, go up’ (*kas” ‘to fall’). || Sh. (Baj.) nijüv-/nijüvd from *ni-Cauba-, cf. Lat. 
cubare, etc. ??, EVS, l.c. 

© This root may have an IE etymology. The connection with Gr. kat, Lat. capere, 
etc. (cf. IEW, l.c.) 1s semantically very attractive. IE "a" would not palatalize the 
preceding velar in (Dir. though: Ir. *č- in *¿ap- is from *éak/g- ? 

*PIE ? *k(e)H»p- ( *kap-) ‘to grab, stick to’? = LIV: 344 f. | Pok.: 527 ff. 

*IE COGNATES: Gr. karnıo ‘I grab; I snap, swallow’, Lat. capio ‘I take’, Goth. hafjan 
‘to lift’, haftjan ‘to stick, attach’, (ppp.) -hafts ‘stuck with’, NHG haften ‘to stick to’, 
haben, Engl. to have, etc. 

*REFERENCES: Horn 1893: 98 f£; KPF II: 212; Andreev — PeSéereva: 242a; Abaev, Slovar’ I: 306, 294, 


159; Abaev, Slovar’ II: 194 f.; EVS: 23b, 48b; WIM I: 67; Abaev, Slovar’ HI: 121 f.; Lecoq 2002: 122, 
125, 129, 607b (passim); ESIJa П: 221 ff.; Shahbakhsh: s.v. Camp- 


*CarH ‘to come and go, wander’ 

*AVESTAN: car- ‘to come and go’ || (+ *para-) ‘to pass over’ || (+ *ui-) ‘to go to and 
fro’ || (+ *ham-) ‘to walk around’ — Liste: 21f.
```


## [2026-09-06T15:49:35.188Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8').read()\npages=t.split('\\f')\nprint(len(pages))\nfor i in (250,251,252):\n    print('--- leaf',i,'---', pages[i][:160].replace('\\n',' '))\nEOF",
 "description": "IEC leaf 251 check"
}
```


### [2026-09-06T15:49:37.163Z] TOOL RESULT

```
858
--- leaf 250 --- ry; anger’ fr. *irs-); cf. also OE iersian ‘rage; enrage’; Li. cf. irstu, irsti “be angry) and Finn. (?) irstas (^wanton'. Queried Balt. LW : YHT : SKES, I). Cf
--- leaf 251 --- e Gallo-Lat. esox: W eog, id. (fr. *isiok-?) isios, a (2) ‘pleasure’ (Skt. type: *isis) Skt. isíh ‘ease’; Av. išyō “desired, dear’; Gk. cf. an-18 *un-ease' -isk
--- leaf 252 --- d, W gwerth-yd, f. ‘spindle’; Lat. laet- itia, trīst-itia, etc.; OS ban-edi, binithi ‘death- blow’; OCS rozn-ica ‘difference’, plen-ica (*plait', fr. *plekn-) b
```


## [2026-09-06T15:49:53.889Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD kanunu ===\"; grep -n -i \"kanunu\\|kinūnu\\|kanūnu\\|kānūn\" AKD.txt | head -10\necho \"=== AFA kanun ===\"; grep -n -i \"kanun\\|kānūn\" AFA.txt | head -10\necho \"=== AFM qafiz/qafas ===\"; grep -n \"قفيز\\|قفص\\|كانون\" AFM.txt | head -20",
 "description": "Zimmern, Fraenkel, Addi Shir lookups"
}
```


### [2026-09-06T15:49:53.976Z] TOOL RESULT

```
=== AKD kanunu ===
=== AFA kanun ===
=== AFM qafiz/qafas ===
5174:( القتقص ) وهو معروف قيل معرب وقيل عربي واستقاقه من القفص بمنى المع
```


## [2026-09-06T15:49:56.794Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN capsule/case ===\"; grep -n \"capsa, 'box\\|L. capsa\\|capsa (\\|kap-, to grasp\\|kap-, 'to grasp\" KLN_1966.txt | head -20\necho \"=== KLN qafiz ===\"; grep -n \"qafiz\\|kafiz\" KLN_1966.txt LKT.txt PLA_pages.txt 2>/dev/null | head -10\necho \"=== LKT qafas/qafiz ===\"; grep -n -i \"qafiz\\|kafiz\\|cafiz\\|qafas\" LKT.txt | head -20",
 "description": "Klein and Lokotsch lookups"
}
```


### [2026-09-06T15:49:56.887Z] TOOL RESULT

```
=== KLN capsule/case ===
6473:Capsella,  n.,  a  genus  of  plants  of  the  mustard family  (bot.)  —  ModL.,  dimin.  of  L.  capsa, ‘box,  receptacle’.  See  capsule  and  -ella. Capsicum,  n.,  a  genus  of  plants  of  the  potato  fa¬ mily  (bot.)  —  ModL.,  irregularly  formed,  fr.  L. capsa.  See  case,  ‘box’,  and  cp.  capsa,  capsule, capsize,  tr.  and  intr.  v.,  to  overturn;  to  upset.  — Of  uncertain  origin.
=== KLN qafiz ===
KLN_1966.txt:6099:See  cement  and  cp.  words  there  referred  to. Derivatives:  caesur-al,  caesur-ic,  adjs. cafard,  n.,  a  hypocrite.  —  F.,  ‘hypocrite’,  fr. Arab,  kafir ,  ‘infidel’,  part,  of  kafara,  ‘he  blotted out,  covered;  he  denied’,  with  substitution  of the  French  pejorative  suff.  -ard  for  the  unusual ending  -ir.  See  Kaffir  and  -ard. cafardise,  n.,  hypocrisy.  —  F.,  ‘hypocrisy’,  for¬ med  fr.  prec.  word  with  suff.  -ise. cafe,  n.,  i)  coffee;  2)  coffeehouse;  restaurant.  — F.,  fr.  It.  caffi,  fr.  Turk,  qahve ,  fr.  Arab.  qahvah, ‘wine;  coffee’.  See  coffee, cafeteria,  n.,  a  restaurant  at  which  the  patrons serve  themselves  from  the  food  displayed  at  a counter.  —  Mexican  Sp.,  meaning  ‘retail  coffee store’.  Cp.  F.  cafetidre  and  see  prec.  word, caffeine,  caffein,  n.,  an  alkaloid  obtained  from coffee  and  tea  ( chem .)  —  F.  cafeine,  fr.  cafe, ‘coffee’.  See  coffee  and  chem.  suff.  -ine,  resp.  -in. cafila,  n.,  a  convoy  of  travelers,  caravan.  —  Arab. qdfilah,  fem.  used  as  a  collective  noun  fr.  qifil, ‘one  who  returns  from  a  journey’,  part,  of  qa- fala,  ‘he  returned  from  a  journey’, cafiz,  n.,  a  measure  of  capacity.  —  Sp.,  fr.  Arab. qafiz,  a  measure  for  com. caftan,  n.,  a  long-sleeved  garment  worn  in  Tur¬ key,  Egypt,  etc. — T atV.qaftdn,  fr.  Arab,  qaftdn, fr.  Pers.  khaftan.
=== LKT qafas/qafiz ===
2384:Anab.  I,  5,  6)  und  nahmen  es  in  der Form  kafyz  an"];  hieraus  kat.  cafiz, sp.  pg.  cahiz,  it.  (dial.  Calabrien)  cavizzu, siz.  vafisu  'ein  Ölmaß'  [dem  Dezimal- system zum  Trotz  noch  in  ganz  Sizilien allgemein  gebraucht].  [DE  244.  Egui- laz  H54.  ML  1478.  GrSVociSic  229. De  Sacv  ChrAr  III,  498.
```


## [2026-09-06T15:50:00.452Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2370,2390p' LKT.txt; echo \"=== AFM 5170-5180 ===\"; sed -n '5168,5180p' AFM.txt; echo \"=== AFM qafiz ===\"; grep -n \"قفيز\" AFM.txt | head",
 "description": "Lokotsch cafiz entry and Addi Shir qafas"
}
```


### [2026-09-06T15:50:00.524Z] TOOL RESULT

```
'Kaffer'  entstanden].  [Tendlau  126. Kluge  221.
993.  Ar.  kafas:
'Kätig'  [über  aram.  kafsä  aus  gr.  Kdipa, lat.  capsa],  ebenso  tk.  kafes ;  hieraus rum.  cafas  'Gitter',  insbesondere  'Roll- laden an  den  Haremsfenstern'  und  'um- gitterte Abteilung  in  einer  Kirche' ;  bulg. serb.  kafez  'Käfig,  Gitter' ;  sp.  pg.  alcahaz 'Käfig',  ferner  mlat.  cabassium,  cabacius, cabacus  'Kiepe',  frz.  cabas,  sp.  capazo, capacho,  pg.  cabaz  'aus  Weidengeflecht hergestellter  Korb' ;  engl,  cabas  'Arbeits- körbchen für  Damen',  ndl.  kabas  'Binsen- oder Strohkörbchen',  dtsch.  Kabaß  'ge- flochtene Slrohtasche'  [dial.,  z.  B.  köl- nisch, s.  König,  Wörterbuch  der  Kölner Mundart.  Köln  1905.  S.  85bj.  [Devic DEt  74.    Bern  SlEtWb  468.
994.  Ar.  kaffa:
'Wagschale;  alles,  was  hohl  und  rund ist'  [auch  'innere  Handfläche',  vgl.  hier Nr.  990] ;  hieraus  siz.  gaffa  'Eisenstange, die  an  den  beiden  Enden  zurückgebogen ist,  Krampe',  sard.  gaffa,  kat.  sp.  gafa 'Haken',  plr.  'Brillengestell',  frz.  gaffe, pr.  gaf  'Haken'.    [GrSVociSic  237.
995.  Ar.  kaflfa:
'Ohrfeige'  [eigentlich  dasselbe  Wort  wie hier  Nr.  994],  vulg.  keffe,  ebenso  tk., dazu  Vb.  tk.  kefelemek  'ohrfeigen';  hier- aus rum.  chelfäni  'durchprügeln',  chel- fänealä  'Prügelei'.
996.  Ar.  käflla: 'Reisegesellschaft,   Karawane',  hieraus sp.  pg.  cufila  'dass.,  Haufen,  Menge'; angloind.  capla  'Geleitzug  zur  See'.  [DE 244.    Hobson-Jobson  142.
997.  Ar.  käflr:
Part,  praes.  act.  des  Vbs.  kafara  'leug- nen, ungläubig  sein',  also  'Ungläubiger'; hieraus  sp.  pg.  cafre  'roh,  grausam,  un- gebildet', frz.  cafard  'scheinheilig'  [mit der  pejorativen  Endung  a?-d;  schon  im Ar,  hatte  das  Wort  den  Sinn  'Hypokrit', s.  Dozy  Suppl  s.  v. ;  ausführlich  GRÜN- BAUM in  ZDMG  XL,  240].  —  Aus  dem- selben Grundwort  kommt  der  Name  des südafrikanischen  Stammes  der  Kaffern; sp.  pg.  cafre,  engl,  caffer,  caffre,  coffree usw.  —  Wegen  der  Worte  Giaur,  giaour, giaurro  s.  hier  Nr.  632.  [DE  245. Eguilaz  354.  ML  4655.  Hobson-Jobson 140/142.
998.  Ar.  kaf  iz :
Ein  Hohlmaß,  'Scheffel'  [aus  gr.  Kairiön. aber  wohl  über  pers.  kaviz,  kavlz  ent- lehnt, s.  ZDMG  L,  647;  LI,  301  und V.  KREMER  in  SBKAW  Wien  CXX (1889),  III,  12:  „In  Babylonien  lernten die  Araber  das  alte  dort  übliche  Ge- treidemaß Kauiöri  kennen  (Xenophon
Ar.  kafr.]
80
Anab.  I,  5,  6)  und  nahmen  es  in  der Form  kafyz  an"];  hieraus  kat.  cafiz, sp.  pg.  cahiz,  it.  (dial.  Calabrien)  cavizzu, siz.  vafisu  'ein  Ölmaß'  [dem  Dezimal- system zum  Trotz  noch  in  ganz  Sizilien allgemein  gebraucht].  [DE  244.  Egui- laz  H54.  ML  1478.  GrSVociSic  229. De  Sacv  ChrAr  III,  498.
999.  Ar.  kafr:
Vollständig-  kafr  aljahüd  'Judenpech, Asphalt';  hieraus  sp.  acafelar  'Tür  oder Fenster  zumauern,  eine  Wand  mit Gips  oder  Kalk  tünchen'  [Dicc  Gast  21a], pg.  acafelar  'mit  Stein  und  Kalk  zu- mauern' [Constancio  Dicc  9  c].  —  DE 51/52.
1000.  Hebr.  käliäl: 'Versammlung,  Gemeinde';  hieraus  russ. kagal  'Gemeinde  bei  den  Juden,  jüdi- scher Gemeindevorstand'.  —  Gorjajew 126.
1001.  Mal.  kähau:
'Eine  Art  kleiner  Affen  mit  langem Schwänze  von  verschiedener  Farbe' [fehlt  bei  Pijn,  aber  Roorda  van  Eysinga, Maleisch  en  Nederduitsch  woordenboek. Batavia  1825.  S.  302;  onomatopoetisch nach  seiner  Stimme,  vgl.  dajak.  kahau 'rufen'] ;  hieraus  engl,  kahau  'ein  lang- nasiger  Affe  mit  langem  Schwänze  aus Borneo,  Semnopithecus  nasalis'  [auch prohoscis-monkey  genannt].  [JAOS XVIII,  63/64.
1002.  Ar.  kahba:
=== AFM 5170-5180 ===
الأحق : 

50 ܕܠܐ( غلاف المكحلة مركن ٠‏ 3 الكحل ومن دان 
دهي اداة تاحق الأمياء ٠‏ فتدل على ܐܨ ܬ 1 القَْرَة وهي 52 اا نوص لعطر 
1 1 ا ` ن 1125101 9 (فرنئكل 00 

( القتقص ) وهو معروف قيل معرب وقيل عربي واستقاقه من القفص بمنى المع 
( ܐ المحيبط ) 9 ܝܐܘ ܚܝ 5ܬ܂131 ܐ( الامل ܘܩܦܣܐ 
وهى ܘܬ ܩܦܣ اى حزن وحدس وقنض واخداً.و ܩܦܣܐ ܕ ܒܝܬ ܩܦܬܐ 
هري ÷ (راجع فرتكل ص 1 ܠܬܒ ܘܠܣܐ والرومي” 


_ ¥ ܙ - 
=== AFM qafiz ===
```


## [2026-09-06T15:50:22.473Z] TOOL CALL #38: ToolSearch

```json
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 2
}
```


### [2026-09-06T15:50:22.480Z] TOOL RESULT

```


```


## [2026-09-06T15:50:26.831Z] TOOL CALL #39: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%86%D9%88%D9%86",
 "prompt": "Give the full etymology of Persian کانون 'fireplace, brazier' and any Arabic كانون section: what Akkadian/Syriac/Aramaic forms are cited, and the exact Akkadian form (kinūnu or kanūnu)?"
}
```


## [2026-09-06T15:50:28.629Z] TOOL CALL #40: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%81%D8%B5",
 "prompt": "Give the Arabic قفص (qafaṣ) etymology in full: is it from Aramaic/Syriac qofsā, Greek κάψα, Latin capsa? And the Persian قفس section."
}
```


### [2026-09-06T15:50:31.644Z] TOOL RESULT

```
# Etymology of Persian کانون

Based on the provided Wiktionary content, the etymology section offers limited information:

**Available Information:**
The entry states that Persian کانون is "Borrowed from Arabic _كَانُون_." However, the page does not provide:

- Any Akkadian forms (kinūnu or kanūnu)
- Any Syriac or Aramaic citations
- Etymology beyond the Arabic borrowing
- Detailed etymological history tracing the word back to ancient languages

**Limitation:**
The Wiktionary article excerpt provided contains only a basic etymology noting the Arabic source. It does not include the deeper etymological chain or historical linguistic information you're seeking regarding Akkadian or other ancient Near Eastern language forms.

To obtain that comprehensive etymological data, you would need to consult more specialized etymological dictionaries or academic linguistic resources beyond this particular Wiktionary entry.
```


### [2026-09-06T15:50:33.940Z] TOOL RESULT

```
# Etymology of Arabic قفص (qafaṣ)

According to Wiktionary, the Arabic term derives from **Aramaic** _qūp̄sā_ / _qap̄əṣā_ / Syriac _qap̄əsā_ / _qap̄əṣā_ meaning "cage," which itself comes from **Ancient Greek** _kápsa_ or **Latin** _capsus_.

The documentation indicates this borrowed pathway: "From Aramaic... from Ancient Greek... or Latin."

## Persian Descendants

The entry shows that Classical Persian adopted the Arabic term as both **قَفَس** (qafas) and **قَفَص** (qafaṣ), which subsequently spread through numerous languages including Azerbaijani, Gujarati, Hindustani, Uyghur, Ottoman Turkish, Kurdish, and Kazakh, each adapting the word to their phonological systems.
```


## [2026-09-06T15:50:37.304Z] TOOL CALL #41: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%86%D9%88%D9%86",
 "prompt": "Give the Arabic كانون (kānūn) etymology in full: what Aramaic/Syriac and Akkadian forms are cited (kinūnu? kanūnu?), and the meanings (brazier/fireplace, month names)."
}
```


## [2026-09-06T15:50:38.662Z] TOOL CALL #42: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%81%DB%8C%D8%B2",
 "prompt": "Etymology of qafīz / قفیز - a dry measure. What Persian/Old Persian/Greek forms are cited?"
}
```


### [2026-09-06T15:50:41.025Z] TOOL RESULT

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-06T15:50:44.131Z] TOOL RESULT

```
# Etymology of Arabic كانون (kānūn)

## Aramaic/Syriac Forms
The entry cites two related Aramaic forms: "כָּנוֹנָא" (Hebrew script) and "ܟܢܘܢܐ" (Syriac script), both transliterated as *kānōnā*.

## Akkadian Forms
Two Akkadian cuneiform variants are referenced:
- **𒆠𒉈** (KI.NE) representing */⁠kanūnu⁠/*
- **𒆠𒉡𒉡** (ki-nu-nu) representing */⁠kinūnu⁠/*

## Meanings
The Akkadian term encompasses "brazier, kiln, stove, hearth" plus "a name of a ritual and also the month it takes place." The related Arabic terms كَانُون الْأَوَّل and كَانُون الثَّانِي function as month names in modern Arabic (December and January respectively).

The etymological chain flows from older Akkadian forms through Aramaic into Arabic, with the primary semantic thread connecting heating/cooking implements to calendar divisions.
```


## [2026-09-06T15:50:51.323Z] TOOL CALL #43: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/keh%E2%82%82p-",
 "prompt": "Give the reconstruction, meaning, and the list of descendants (Latin capio/capsa, Germanic *habjaną/*habjaz, Greek, Iranian) for PIE *keh₂p-."
}
```


## [2026-09-06T15:50:52.724Z] TOOL CALL #44: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%86%D8%B3%D8%A8%DB%8C%D8%AF%D9%86",
 "prompt": "Etymology of Persian چسبیدن (časbidan) 'to stick, adhere': what Proto-Iranian root and cognates are given?"
}
```


### [2026-09-06T15:50:58.288Z] TOOL RESULT

```
# Etymology of چسبیدن

Based on the Wiktionary entry provided, the etymology section states that this Persian verb was "Inherited from Classical Persian _چسپیدن_ (časpīdan)."

However, the document does not provide information about the Proto-Iranian root or cognates for this word. The etymology only traces the term back to its Classical Persian ancestor, without explaining its deeper historical origins or related terms in other Iranian languages.
```


### [2026-09-06T15:50:59.035Z] TOOL RESULT

```
# Proto-Indo-European *keh₂p- (Alternative Form)

## Reconstruction
**\*keh₂p-** is listed as an alternative reconstruction of the primary root \*kap-.

## Meaning
The root carries two main senses:
1. "to seize, to grab" (dynamic sense)
2. "to hold" (stative sense)

## Key Descendants

**Latin:**
- capere (verb: to seize) → capiō
- capsa (noun: box, container)

**Germanic:**
- \*habjaną (to have, hold)
- \*habnō (harbor)

**Greek:**
- κήπος (kêpos: garden, orchard)
- κάπη (kápē: crib)

**Iranian:**
- \*čap- (to seize, attack, stick, strike)
- Persian چسپیدن (časpidan: to stick)

The page notes this root is "possibly a non-Indo-European loanword" and may be "onomatopoeic or sound-symbolic" in origin.
```


## [2026-09-06T15:51:20.417Z] TOOL CALL #45: Bash

```json
{
 "command": "pdftoppm -f 240 -l 240 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg240\" && ls -la \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/\"",
 "description": "Render PDF page 240"
}
```


### [2026-09-06T15:51:23.216Z] TOOL RESULT

```
total 6988
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 11:51 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  6 10:51 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     902 Sep  6 11:50 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb   92182 Sep  6 10:55 bqt1854.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66580 Sep  6 10:57 bqt2023.png
-rw-rw-r-- 1 sfmqrb sfmqrb   69965 Sep  6 11:25 bqt2242crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   28189 Sep  6 11:25 bqt2417crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb  431133 Sep  6 11:16 bqt2420_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb    9548 Sep  6 11:25 bqt2meta.json
-rw-rw-r-- 1 sfmqrb sfmqrb   81018 Sep  6 11:16 build213.py
-rw-rw-r-- 1 sfmqrb sfmqrb   67391 Sep  6 11:49 build225.py
-rw-rw-r-- 1 sfmqrb sfmqrb   71757 Sep  6 11:47 build232.py
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
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:44 p216
drwxrwxr-x 2 sfmqrb sfmqrb    4096 Sep  6 11:49 p233
-rw-rw-r-- 1 sfmqrb sfmqrb   17907 Sep  6 11:25 part1.json
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
-rw-rw-r-- 1 sfmqrb sfmqrb   81131 Sep  6 11:51 pg240.png
-rw-rw-r-- 1 sfmqrb sfmqrb   97613 Sep  6 11:49 pg242.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1209522 Sep  6 11:39 sin_goog.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  147680 Sep  6 11:20 sns167.jpg
```


## [2026-09-06T15:51:26.131Z] TOOL CALL #46: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg240.png"
}
```


### [2026-09-06T15:51:26.557Z] TOOL RESULT

```

```


## [2026-09-06T15:51:26.550Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T15:51:39.667Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs; sed -n '43390,43450p' POK_full.txt | head -70",
 "description": "Pokorny page 524 content"
}
```


### [2026-09-06T15:51:39.732Z] TOOL RESULT

```
and perhaps kqAAoiov n. (mostly PI.) ' cockscomb, crest on head of cock, rooster's comb '. 

/■stem Old Norse halr{*hali-) 'man, husband, master, mister' (poet.). Old English 
/7^/e(^dy/'man, husband', asachs. helid. Old High German helfd^mau, husband, 
combatant, hero ', Old Swedish halith, besides ^stem Old Norse bg/drlree farmer, man, 
husband' {*halut^). 

References: WP. I 356, 443, Specht Indo Germanic Dekl. 128, 195; Seller, The primaren 
gr. Steigerungsformen 68 ff. 
Page(s): 524 



Root / lemma: kalni- 

Meaning: narrow passage 

Material: Latin callis^ lane, trod, path, footpath, forest path, pathway, sideway, trackway, 

mountain-track, forest pastures '; 

bulgar. k/an/k'room between stove, hearth and wall', serb. klanac. Gen. klanca^ defile, 
narrow passage between mountains ', sloven, klanec' defile, narrow passage between 
mountains, mountain path, rivlet of a brook, village lane ', Czech klanec^ saddle, pass, 
narrow road between mountains '. 

References: WP. I 356 f., WH. 1140 f. 
Page(s): 524 

Root / lemma: kamb- 
Meaning: ' bend, curve, crook ' 
See also: see below (s)kamb- 
Page(s): 525 

Root / lemma: kam-er- 

Meaning: to bend, curve, vaulted 

Material: Old Indie kmarati {ox\\y Dhatup.) 'is crooked'; 

Avestan kamarai. 'belt, girdle' (and '* dome '); 

gr. KpsAsGpov 'beam, ceiling, roof, house' (probably dissim. from *K[j£p£9pov), Kopiapa ' 
dome, four-poster bed; covered cart ' (to Solmsens BPhW. 1906, 852 f. assumption Carian 
origin, Kopapa AsysTai ra aacpaAr), s. Boisacq 402 Anm.; Latin loanword camera, camara^a 
vault, an arched roof, an arch'); at most KapTvoq 'oven' (certainly this could have derived 
from a culture word); 

Latin camur(us), -a, -^/t? 'arched, writhed, crooked, humped ' (dial.), genuine Latin 
camerus. 

References: WP. I 349 f., WH. I 146 f., 149 f., 306, Feist 6, 256; 
See also: s. also kam-p-. 
Page(s): 524-525 

Root / lemma: kam-p- 
Meaning: to bend 



Material: Old Indie kapana'\NO'cr(\, caterpillar, inchworm' {*kmpena), kampate '\.remb\es\ if
```


## [2026-09-06T15:51:48.163Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"کانون\" \"قفس\" \"کویز\" \"کپسول\" \"شاسی\"; do echo \"--- MON $w ---\"; grep -oh \".\\{0,140\\}$w.\\{0,160\\}\" MON_part2.txt MON_part1.txt 2>/dev/null | head -3; done",
 "description": "Mo'in 2-vol lookups"
}
```


### [2026-09-06T15:52:03.483Z] TOOL RESULT

```
--- MON کانون ---
--- MON قفس ---
--- MON کویز ---
--- MON کپسول ---
--- MON شاسی ---
```


## [2026-09-06T15:52:06.758Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nhead -c 600 MON_part2.txt; echo; echo \"SIZE:\"; wc -c MON_part2.txt; echo \"--- grep simple ---\"; grep -c \"کان\" MON_part2.txt; grep -c \"ا\" MON_part2.txt",
 "description": "Check MON OCR file content"
}
```


### [2026-09-06T15:52:06.873Z] TOOL RESULT

```
معین» محمد» ۱۲۹۱ ۱۳۵۰. 


۰ 
۳ 


فرهنگ معین / محمد معین. -- تهران: آدنا: کتاب راه نو ۰۱۲۸۱ 


۲ج 
(دوره) :964-7252-51-2 :158 
(ج.۲) 964-7252-53-6 :158۷ (ج.۱) 964-7252-52-8 :5۳81] 
فهر ستنویسی بر اساس اطلاعات فیپا. 
۱. فارسی -- واژه‌نامه‌ها. الف. عنوان. 
۴۵ف ۲۹۵۴/۸۷ ۳112 ۳ فا ۴ 
۱۳۸۱ 
کتابخانه ملی ایران ۷۹۵ - ۸۱م 


انتشارات آدنا 
فر هنگ دوجلدی معین 
گردآورنده عزیزالته علیزاده 
�
SIZE:
4331421 MON_part2.txt
--- grep simple ---
630
68149
```


## [2026-09-06T15:52:12.235Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"کانو\" \"قفس\" \"کاتون\" \"کویز\" \"کپسول\"; do echo \"--- $w ---\"; grep -oh \".\\{0,100\\}$w.\\{0,140\\}\" MON_part2.txt | head -4; done",
 "description": "MON part2 partial greps"
}
```


### [2026-09-06T15:52:27.217Z] TOOL RESULT

```
--- کانو ---
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,140}
                          \___exceeds complexity limits


--- قفس ---
ugrep: error: error at position 84
xbf][\x80-\xbf]*){0,140}
                        \___exceeds complexity limits


--- کاتون ---
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,140}
                            \___exceeds complexity limits


--- کویز ---
ugrep: error: error at position 86
-\xbf][\x80-\xbf]*){0,140}
                          \___exceeds complexity limits


--- کپسول ---
ugrep: error: error at position 88
80-\xbf][\x80-\xbf]*){0,140}
                            \___exceeds complexity limits
```


## [2026-09-06T15:52:31.228Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('MON_part2.txt',encoding='utf-8').read()\nfor w in ['کانون','قفس','کویز','کپسول','شاسی','کبست','کاول','کابل']:\n    idxs=[m.start() for m in re.finditer(re.escape(w),t)][:3]\n    print('###',w,len(idxs))\n    for i in idxs:\n        print('   ',t[max(0,i-120):i+180].replace('\\n',' '))\nEOF",
 "description": "Mo'in 2-vol python grep"
}
```


### [2026-09-06T15:52:32.987Z] TOOL RESULT

```
### کانون 3
    گتر شد و به قدر  يکث گربه گردید از کیسه خارج می‌شود و با  مادر چرا می‌کند و در مواقم خطر در کیسه  مادر داخل می‌گردد.    کانون فرهنگ فارسی معیر ۱۳۹    کانوا: 3 (.) قسمی نخ که از ابر یشم با  کرک ریسند و بدان لباس‌های زمستانی مانند  بلوز» ژا کت و غیره بافند.   ک‌انون: ۷5۰5(ع. سر. از اکدی] (.)  آتشدان (
    ح. اين نام از عصر ا کدی اطلاق  شده و در کتسه‌های لمیر هس به ی ام  ماه‌های سال اطلاق کر دیده و آن مطایق با  2 بود. بعدها کانون نام دو 9  سریانی گردید: کانون اول: (- کانون الاول)  و آن ماه سوم از ماه‌های سریانی مشهور به  «شهور رومی» است. کانون آخر: (- کانون  الاخر) و آن ماه چهارم از ماه‌های سریانی  مش
     شده و در کتسه‌های لمیر هس به ی ام  ماه‌های سال اطلاق کر دیده و آن مطایق با  2 بود. بعدها کانون نام دو 9  سریانی گردید: کانون اول: (- کانون الاول)  و آن ماه سوم از ماه‌های سریانی مشهور به  «شهور رومی» است. کانون آخر: (- کانون  الاخر) و آن ماه چهارم از ماه‌های سریانی  مشهور به «شهور رومی» است. (ف.) م
### قفس 3
    مکث  می‌گیرد و غرض از آن تحصیل ملک ضبط  اختلاف متواتر است و فایده آن حفظ کلام  خدااست تا تحریف و تغسر در ان راه نباید.  قفسرانتخانه: (ع)ه«8 7 [ع. ف.] (امر.)  جایی که مردان در آن به خواندن کتاب؛  روزنامه و مجله پرداز ند.   فرائی: آ-2::(ع. ف.] (حامص.) قرائت    قرآن؛ قرآن‌خوانی.  فراب: 9 [ع.] .( ظرفی ش
    شود: (- قوشون] (.) مجموعه  سپاهیان؛ ار تش.   فص: (5)5ه۲ [ع.] (.) (یز.) استخوانی است  پهن و میانی که در جلو استخوان‌بندی قفسة  سینه وافع است. طولش در حدود ۲۰  سانتیمتر و به شکل خنجر است و دارای  یک دسته و یکث تنه و یک انتها است که به  زایدة خنجری موسوم است. سطح قدامسی  استخوان قص به پوست مربوط است و 
       ثفر : ۲(ع.] (.) بیابان بی اب و علف؛   زمين بی آب و علف که در آن جانور و    انسان سا کن نباشد؛ ج. قفار.   ففس: دار [- قفسء معر. صندوق» جعبه ]  (.) آلتی است که از چوب؛ برنج» آهن و  غیر آن سازند و دارای شبکه‌ها است و  پرندگان وحشی را در آن نگاه دارند. قفس  (قفسه) سینه: (بز.) محوطة قفس مانندی که  به 
### کویز 1
      کفه: ()۵ه (.) پلةٌ ترازو.   کفیدن: ۷۸۲-1 [- کفیتن - کافتن ‏ کفتن ]  (مصل.) از هم باز شدنء شکافته شدن.  کفیز: ۲۸۲32 [- کویز - کویژ معر. قفیز ] (1.)  پیمانه‌ای است برای غلات.   کفیل: ۱[ [ع.] (ص.) آنکه از دیگری  کفالت کند؛ ضامن» پایندان؛ ج. کفلاء (غم.)  کسی که ادارة وزارتخانه یبا اداره و با  موّسه‌ای
### کپسول 3
    آید که در وسط قسمت محیطی  جای می‌گیرد. به همین مناسبت در قدیم غدد  فوق کلیوی را ساختمانی کیسه‌یی تصور  کرده و به اشتباه کپسول فوق کلیوی نام  نهاده‌اند. بهترین ماده‌ای که ار قسمت مرکزی  هر یکث از این غدد ترشح و وارد خون  می‌شود آدرنالین نام دارد که یک هورمون  سمپاتیکو میمتیکث است. مهمترین موادی که  ا
     نبود. چا.  ۲(   کیپسول: اتاه۵! (.) چاشنی تفنگ. (کیا.)  گونه‌ای میوةٌ خشکث شکوفا که از چند برچه  بسوجود آمده است. میوهٌ کپسول دارای  اشکال متعدد است. در برخی میوه‌ها قسمتی  از میوه مانند سر پوش از روی قسمت دیگر  برداشته می‌شود. در این صورت کپسول را  بنام مجری يا پیکسید می‌خوانند مانند میوة  بارهنگ و
    کپسول دارای  اشکال متعدد است. در برخی میوه‌ها قسمتی  از میوه مانند سر پوش از روی قسمت دیگر  برداشته می‌شود. در این صورت کپسول را  بنام مجری يا پیکسید می‌خوانند مانند میوة  بارهنگ و گل ناز و برخی دیگر بواسطة  سوراخ‌هایی که در زیر صفحه کلاله واقع  است دانه را آزاد می‌کنند» در | ین صورت  ناه رشق تلا تک
### شاسی 3
    طلق: پدرگان (آنچه به فرزند رسیده باشد  ار بدر) ب دوستگان؛ درمگان؛ دینا رگان.  ج - به آخر اسم روز و ماه شمسی ( که اسم  امشاسیند یا فرشته‌ای است) ملحق گردد و  دال بر تطبیق نام روز با نام ماه است و  ایرانسیان باستان چسنین روزی را جشن  سی‌گرفنتند: آبانگان. د -دال بر لیاقت:  شایگان (- شاهگان). ه- دال بر 
     مرکب است و آن  از تذکر حالات مطبوع مفقود و از اندوه  فعلی که آنها را احاطه کرده است و غیره  ترکیب شده (دکتر سیاسی. روانشاسی تربیتی  ص ۳۳۳). ضصح. «مالنخولیا» بصورت‌های:  مالیخولیا؛ ماخولیا» ملتخولیا؛ مالیخ؛ مالنخ ۲  غیر ه در امده.   مالیدن: 2121-07 (جماع کردن» ساییدن»  مالبدن ] (مالید» مالد؛ خواهد م
     شود نقل  کرده. امکان دارد که هفت سین ( - ۷ س)    ۳۱ «۴    فرهنگ فارسی معین    اشاره به هفت سینتا (هفت مقدس). (- هفت  امشاسیندان) باشد (نظر آقای بورداود). خود  سفرةٌ مزبور را با محتویات آن نیز هفت‌سین  گویند.   ه_فت عضو: ۲-۰7 [ن. ع.] (امر.)  مجموعه هفت عضو از اعضای بدن ادمی.   هفت‌کهنه: (0-)002-. (ا
### کبست 1
    راین کاپهل» مها کال» ابو جهل قاریوزی»  قتاءالنعام» شجر؟ٌ خبیثه» شجرة الخبیثه؛  خطبان» کست. کسته» حبه الهید» فنک»  حمطل» کبستو» هبیده» خربزة ابوجهل» زهر  گیاه» خريزة تلخ» کسه. ضح.- دانه این گیاه  را حب‌الحنضل نامند. هندوانه زلف: زلف  سیاه. با یک دست چند هندوانه لد کردن:  در آن واحد با نداشتن تن وسایل
### کاول 3
    آذرین  کائولن بر اثر تأثیر آب‌های اسیدی (آب  باران بر ات جل ۲ هوا در آن) به مروز  زمان انجام می‌گردد؛ بدین جهت تشکیلات  کاولن در محاورت سنگ‌های آذرین  قدیمی دیده می‌شود. فرمول کائولن را  می‌توان بصورت,۲۹:0۵۲,۸1/۲۵۳ ۲۳۱۳۵  نوشت و بنابراین یک سیلیکات ثیدراتة  آلومنیوم است. ک‌ائولن بسطوری که از  فرمولش
    ۷17۷ (.) تفحص» تجسس»   تفتیش. کندن» حفاری. به ناخن کاویدن   دا زخم و و غیره را). به کاوکاو بودن: در  نحث و گفتگو بودن.  کاولی‌ساز: 2-[/۵۷۵ [- کاولی‌سازنده]  وج زد ی یت   شت و ناهموار سازد. (کد.) کسی که چشم چشم  بای زا موی ان  کاونده: (0-)7:32:-2۷(افا.) تفحص کننده؛  تجسس کننده. کننده» حفار. بحث کننده
     تفتیش. کندن» حفاری. به ناخن کاویدن   دا زخم و و غیره را). به کاوکاو بودن: در  نحث و گفتگو بودن.  کاولی‌ساز: 2-[/۵۷۵ [- کاولی‌سازنده]  وج زد ی یت   شت و ناهموار سازد. (کد.) کسی که چشم چشم  بای زا موی ان  کاونده: (0-)7:32:-2۷(افا.) تفحص کننده؛  تجسس کننده. کننده» حفار. بحث کننده.    ستیز ه کننده.   ک
### کابل 3
    اده از  خاک چینی جهت ساختن ظروف در  مملکت چین انجام شده است؛ خاک چینی»  کاباره: 02:0 (.) میکده. میخانه؛  مشروب‌فروشی.   کابل: ا (.) مفتول فلزی لفاف‌دار و سیم  زیرزمینی یا زیردریایی که جهت برق و تلفن  وتلگراف‌بکا رآید.   کابل‌کشی: ۲:01 (فر. ف.]  (حامص.) کشیدن سیم‌های زیرزمینی یا زیر  دریایی برای برق 
    نه؛  مشروب‌فروشی.   کابل: ا (.) مفتول فلزی لفاف‌دار و سیم  زیرزمینی یا زیردریایی که جهت برق و تلفن  وتلگراف‌بکا رآید.   کابل‌کشی: ۲:01 (فر. ف.]  (حامص.) کشیدن سیم‌های زیرزمینی یا زیر  دریایی برای برق و تلفن و تلگراف؛ کشیدن  کابل.   کاینه: «معظ۲ [منظر ه] (1.) چشم.  و ۵ (.) حالتی که به شخص  خواییده دس
    راف‌بکا رآید.   کابل‌کشی: ۲:01 (فر. ف.]  (حامص.) کشیدن سیم‌های زیرزمینی یا زیر  دریایی برای برق و تلفن و تلگراف؛ کشیدن  کابل.   کاینه: «معظ۲ [منظر ه] (1.) چشم.  و ۵ (.) حالتی که به شخص  خواییده دست دهد و او پندارد که شحصی  با شیثی سنگین بر سین او افتاده و او را  می‌فشار د. در نتبجه نفس خوایده تک شود
```


## [2026-09-06T15:52:52.824Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nfor f in ['ARY_latin_index_pages.txt','ARY_pages.txt']:\n    t=open(f,encoding='utf-8').read()\n    for w in ['KAP','چسبیدن','کویز','کبست','قفس']:\n        idxs=[m.start() for m in re.finditer(re.escape(w),t)][:2]\n        if idxs: print('###',f,w)\n        for i in idxs:\n            print('   ',t[max(0,i-150):i+200].replace('\\n',' '))\nEOF",
 "description": "Aryanpur lookups"
}
```


### [2026-09-06T15:52:54.405Z] TOOL RESULT

```
### ARY_latin_index_pages.txt KAP
    ggy pe  pens Ob ysl y sta Kole gaat y2 (COGNATE) ay ar slrosly saan bus tS (eral IKUOFA 5 ken! fo i.g0 35) KOU aby hy ta patsy Ste es AKUPO: 34-5 yl (KAPAS: gl ga) SCUAN 24S ot) | HHLAINS eS (KAUFA, Aly ged (HEAP: gunlSit KKVAB : glial KOPAK > gh KUWI 252, SCHOOP sygscln Oldee 3 py caoleay ikian Sslemb Ith | y uaa Sarl oT Lily abby be eel greta sag
    HEFFEN YCIFSATI  :(OLD PERSIAN) iol 54 HEBEN :(GERMAN) gisT AFGHANI) (4) glail HEBBAN (OLD ENGLISH) oa lS CHASP, CHASPAN HEAVE ENGLISH) g-JS31 CACHT, KAPATI :(SANSKRIT) cu Suse HAEVE (DANISH) jul KAPTEIN, KOPE AGREEK) gy HAFVA (SWEDISH) (548 y= LATIN) 3 HAEVE ANORWEGIAN) «553,5 CAPERE, CAPTARE, CAPIO coat HEFFEN DUTCH) gacle HAFJAN " Hucortive) 638
```


## [2026-09-06T15:52:55.157Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN case box ===\"; grep -on \"case,  n.,  a  box.\\{0,700\\}\" KLN_1966.txt | head -2\necho \"=== KLN capsule ===\"; grep -on \"capsule,  n\\..\\{0,450\\}\" KLN_1966.txt | head -2\necho \"=== KLN chassis ===\"; grep -on \"chassis,  n\\..\\{0,400\\}\" KLN_1966.txt | head -2\necho \"=== SKT case ===\"; grep -on \"CASE (1).\\{0,350\\}\\|Case (1).\\{0,350\\}\" SKT.txt | head -3",
 "description": "Klein and Skeat English words"
}
```


### [2026-09-06T15:52:56.812Z] TOOL RESULT

```
=== KLN case box ===
=== KLN capsule ===
6475:capsule,  n.  —  L.  capsula,  ‘a  small  box  or  chest’, dimin.  of  capsa,  ‘repository,  box,  chest,  case’. See  case,  ‘box’,  and  cp.  Capsa,  Capsella,  Cap¬ sicum.  For  the  ending  see  suff.  -ule. Derivatives:  capsule,  tr.  v.,  capsui-ar,  capsul-ate, capsul-at-ed,  adjs.,  capsul-at-ion,  n.,  capsul-er,  n. captain,  n.  —  ME.  capitain,  fr.  OF.  ( =  F.)  capi- taine,  fr.  Late  L.  capitdneus,  ‘head,  chief’,  fr. L.  caput,  gen. 
=== KLN chassis ===
7266:chassis,  n.,  framework.  —  F.  chassis,  ‘frame, framework’,  fr.  chasse,  ‘frame’,  fr.  L.  capsa, ‘chest,  box’.  See  case,  ‘chest’,  and  cp.  chase, ‘iron  frame’,  and  sash,  ‘framework’, chaste,  adj.  —  OF.  (=  F.),  fr.  L.  castus,  exempt (from  mistakes),  free,  pure,  chaste’,  prob.  the pp.  of  carere,  ‘to  be  without,  be  wanting,  be  free from,  abstain  from’,  which  prob.  m
=== SKT case ===
```


## [2026-09-06T15:53:08.604Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -on \"case,  n.,  a  chest.\\{0,500\\}\\|case,  n.,  chest.\\{0,500\\}\\|cable,  n\\..\\{0,400\\}\\|capstan,  n\\..\\{0,300\\}\\|heavy,  adj\\..\\{0,300\\}\\|have,  tr\\..\\{0,300\\}\" KLN_1966.txt | head -8",
 "description": "Klein cable, capstan, heavy, have"
}
```


## [2026-09-06T15:53:10.052Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_latin_index_pages.txt',encoding='utf-8').read()\nblocks=t.split('\\f')\nfor i,b in enumerate(blocks):\n    if 'CIFSATI' in b:\n        m=re.search(r'\\[pdf page (\\d+)\\]', b)\n        print('block',i,'tag',m.group(1) if m else None)\n        print(b[:900])\nEOF",
 "description": "Aryanpur page for CIFSATI"
}
```


### [2026-09-06T15:53:10.287Z] TOOL RESULT

```
4673:have,  tr.  and  intr.  v.  —  ME.  behaven,  fr.  OE. behabban,  ‘to  restrain’,  formed  fr.  be-  and habhan, ‘to  have’  (see  have).  The  orig.  meaning  was  ‘to have  (oneself)  under  one’s  control’.
6015:cable,  n.  —  ME.  cable,  cabel,  kable,  fr.  F.  cable, fr.  Port,  cable,  which  is  a  blend  of  Arab,  habl, ‘rope,  cable’,  and  VL.  cap(u)lum,  ‘a  halter  for cattle’,  fr.  capid,  capere,  ‘to  catch,  seize,  take, hold’.  Arab,  habl  is  rel.  to  habala,  ‘he  bound’, Heb.  hebhel,  ‘rope,  cord’,  Ethiop.  habal,  ‘rope’, habala,  ‘he  bound’,  Akkad,  nahbalu,  ‘rope, snare’,  Aram,  h
6474:capstan,  n.,  a  device  for  hauling  up  anchors.  — F.  cabestan,  fr.  OProven;.  cabestan,  fr.  cabe- stran,  pres.  part,  used  as  a  noun,  fr.  L.  capist- rare,  ’to  tie  with  a  halter’,  fr.  capistrum,  ‘halter’, fr.  capere," to  catch,  seize,  hold’.  Cp.  F.  chevetre, ‘halter’,  which  al
17309:have,  tr.  v.  —  ME.  habben,  haven,  fr.  OE.  hab- ban,  ‘to  hold,  possess,  have’,  rel.  to  ON.  hafa, OS.  hebbjan,  OFris.  habba,  hebba,  OHG.  haben, MHG.,  G.  haben,  Goth,  haban,  ‘to  have’,  and to  OE.  hebban,  etc.,  ‘to  lift,  raise’,  fr.  Teut.  base *haf-,  ‘to  hold,  have’,  cor
17376:heavy,  adj.  —  ME.  hevy,  fr.  OE.  he  fig,  rel.  to  OS. hefiig,  OHG.  hebig,  hevig,  LG.  hevig,  ON. hofugr ,  hofigr,  ‘heavy’,  and  to  OE.  hefe,  ‘weight’, hebban,  ‘to  lift,  raise’.  See  heave  and  -y  (repre¬ senting  OE.  -ig).
17377:heavy,  adj.
34903:have,  tr.  and  intr.  v.  —  ME.  schaven,  shaven,  fr. OE.  sceafan,  scafan,  ‘to  scrape,  shave,  polish’, rel.  to  ON.  skafa,  Dan.  skave,  Swed.  skara,  OS. scaban,  MDu.  scaven,  Du.  schaven,  OHG.  ska- ban,  MHG.,  G.  schaben,  Goth,  skaban,  fr.  I.-E. base  *skap-,  a  collateral  form
```


### [2026-09-06T15:53:12.525Z] TOOL RESULT

```
block 221 tag 222
[pdf page 222]
i,
leetlasl
OAS 20S (hi Ay Se FH) ed Cdk 9 Bled y AGAR Bll 2S oH
(LITHUANIAN) lp) CHERME (KURDISH) «52,6
KALYBAS, KALYVAS KARKA- SANSKRIT) og Sail
KHELLOS, CHELLOS <(GREEK) cli»
REFERENCES bok, COLUMBA LATIN) 3
POKORNY, SSS*S*~*«CT AB (OLD HIGH GERMAN) yf gisST
ory i gbi ily HULIWA
airy sans aabicadd HELM (ua}(GERMAN) glST
HEFFEN YCIFSATI  :(OLD PERSIAN) iol 54
HEBEN :(GERMAN) gisT AFGHANI) (4) glail
HEBBAN (OLD ENGLISH) oa lS CHASP, CHASPAN
HEAVE ENGLISH) g-JS31 CACHT, KAPATI :(SANSKRIT) cu Suse
HAEVE (DANISH) jul KAPTEIN, KOPE AGREEK) gy
HAFVA (SWEDISH) (548 y= LATIN) 3
HAEVE ANORWEGIAN) «553,5 CAPERE, CAPTARE, CAPIO coat
HEFFEN DUTCH) gacle HAFJAN " Hucortive) 638
KOOPA LITHUANIAN) g\ =) (OLD SCANDINAVIAN) aS gL!
KAMPT LATVIAN) (3) 99 HEFJA
CACHT = (OLD IRISH) <4 54) HEFJA HOLD NORSE) oS 955
CAETH WELSH) 53 HEBBIAN (OLD SAXON) 4S y-Slu
KAP, KAPASE HALBANIAN) gidT HEVA x
```


## [2026-09-06T15:53:30.319Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nfor f,label in [('incoming/PLA/PLA_pages.txt','PLA'),('AFM_pages.txt','AFM'),('TAD_pages.txt','TAD'),('ARB_mo3rb.txt','ARB')]:\n    try: t=open(f,encoding='utf-8',errors='replace').read()\n    except Exception as e: print(f,e); continue\n    for w in ['قفيز','قفیز','كافيز','قفص']:\n        for m in list(re.finditer(re.escape(w),t))[:2]:\n            i=m.start()\n            print('###',label,w,'::',t[max(0,i-180):i+240].replace('\\n',' '))\nEOF",
 "description": "Asbaghi, Addi Shir, al-Unaysi for qafiz/qafas"
}
```


### [2026-09-06T15:53:32.412Z] TOOL RESULT

```
### AFM قفص :: ة مركن ٠‏ 3 الكحل ومن دان دهي اداة تاحق الأمياء ٠‏ فتدل على ܐܨ ܬ 1 القَْرَة وهي 52 اا نوص لعطر 1 1 ا ` ن 1125101 9 (فرنئكل 00 ( القتقص ) وهو معروف قيل معرب وقيل عربي واستقاقه من القفص بمنى المع ( ܐ المحيبط ) 9 ܝܐܘ ܚܝ 5ܬ܂131 ܐ( الامل ܘܩܦܣܐ وهى ܘܬ ܩܦܣ اى حزن وحدس وقنض واخداً.و ܩܦܣܐ ܕ ܒܝܬ ܩܦܬܐ هري ÷ (راجع فرتكل ص 1 ܠܬܒ ܘܠܣܐ والرومي”_ ¥ ܙ - 0035 والحرمالي 8 والايطاليالي 5 5 وهو 5 : 3 1 * (التَمَنْدَر والتَيْدر) اليم الم
### TAD قفص :: 01‬معناه زنبيل من خلاف‬   ‫غلاف اللكحلة ‏ فارسي مركب ون كف أي كلل ؤذا نوعو‬               ‫تدان ‪-‬‬                                               ‫صيغة ظرف المكان تلصق بالاسياء‬ ‫قفص ‪ -‬عرنيمحض وقفسالفارسي التركي مأخوذ منقفصالعربي و دومه)!‬   ‫ميةدوع اللاتينية معناها عليةوخْرّانة مخنشب أما االقلفصيوفنانية‬                                                                ‫هونان‬                                        
### TAD قفص :: ارسي مركب ون كف أي كلل ؤذا نوعو‬               ‫تدان ‪-‬‬                                               ‫صيغة ظرف المكان تلصق بالاسياء‬ ‫قفص ‪ -‬عرنيمحض وقفسالفارسي التركي مأخوذ منقفصالعربي و دومه)!‬   ‫ميةدوع اللاتينية معناها عليةوخْرّانة مخنشب أما االقلفصيوفنانية‬                                                                ‫هونان‬                                                                    ‫الي‬          
### ARB قفيز :: للسان أن أصل ” ابر يب ““ مكيال معروف عندهم من الطعام » وأنه يطلق على الأرض باعثيا رأ نه  بزاع فيه هذا القدر من المكل ٠‏ كا قالوا « أعطاه صاعا من حرة الوادى » أى مسيزرصاع © وأعطاه  قفيزا أى ميزر قفيز » ولذلك قالوا : <« ألخر ب قدر ما يزرع فيه من الأرض »6 ٠‏ وجمفمه «أحرية «  و «جربان » بشم ابليم وسكون الراء ٠‏ والظاهى أن المادة عرب لا معرية ٠‏   09 ”*الطودياء©* بم اليم وكدر الذال المهملة وتميف الياء وبالمسدٌ ٠‏ هكزا فى 
### ARB قفيز ::  ابر يب ““ مكيال معروف عندهم من الطعام » وأنه يطلق على الأرض باعثيا رأ نه  بزاع فيه هذا القدر من المكل ٠‏ كا قالوا « أعطاه صاعا من حرة الوادى » أى مسيزرصاع © وأعطاه  قفيزا أى ميزر قفيز » ولذلك قالوا : <« ألخر ب قدر ما يزرع فيه من الأرض »6 ٠‏ وجمفمه «أحرية «  و «جربان » بشم ابليم وسكون الراء ٠‏ والظاهى أن المادة عرب لا معرية ٠‏   09 ”*الطودياء©* بم اليم وكدر الذال المهملة وتميف الياء وبالمسدٌ ٠‏ هكزا فى ب . والذى  ف ا
### ARB قفص :: ئة 6 وأنا جا أس ف مسحك قباء من توأجى المدشة» 3 عس سية حسنة  الشارة» رائقة الإشارة» مع ون تناد خ راف الفلرقي درام عاق قصلت  هناك ركعتين أحيقها 6 م رفعت يدبأ ودعت بدعاء معت فيه بن القفصاحة  واللشوحع 6 واععدت عناها دمع غير د ولا نوع والثتت تقول وهى  معتلة :  عر 1 7 آذ 01-7 3 5  8 مزل القطر بعك هم قنطوا كَ ويا وى الذعاء والمارن  2 _- ِ- 1 سهه اا 55  يكون ماشئت أن كونوما 4*# قدرت أن لايكون لم يكن  ١ 5‏ 2  وسأتنى عن لبر ال
### ARB قفص ::  » ه  فق : ١‏ ) دالاسا   (0) ف ث « تقاصص» وموخظا ؛    (») فى 6 «ثوا اتمها» . وما هنا دو الدذى فى ما ثر النسخ و  60 ضبطت ققى ب بشم القاف والفاء. وق المهرة :  7 لل لاسا ته   ن: ِ في قفص دن املا جه أو قفص دل  (0) «ذا القول لم أجده إلا عند الأولف ٠‏    « فى تفص أو قفص من اللملانكة أرمن النور» ٠‏ وق الاسا  النور» .ول أجد الحديث 6 ولم يذ كه صاحب الهاي ٠‏  وذمم اذى شير أنه تعريب ” ققس “ الذى جعناه »ثم أحذ ينقل أن الكلمة أرا
```


## [2026-09-06T15:53:44.484Z] TOOL CALL #57: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%D9%82%D9%81%D9%8A%D8%B2",
 "prompt": "Etymology of Arabic قفيز (qafīz), a dry measure: what Middle Persian / Old Persian / Greek forms are cited (kapīč, καπίθη)?"
}
```


## [2026-09-06T15:53:46.005Z] TOOL CALL #58: WebFetch

```json
{
 "url": "https://en.wiktionary.org/wiki/%DA%A9%D8%A8%D8%B3%D8%AA",
 "prompt": "Is there an entry for Persian کبست (kabast) 'colocynth'? Give any etymology (Middle Persian kapast, Avestan kapasti-)."
}
```


### [2026-09-06T15:53:51.114Z] TOOL RESULT

```
# Etymology of قفيز (qafīz)

Based on the Wiktionary entry, the word traces back through multiple ancient languages:

**Middle Persian**: The etymology cites Middle Persian [Book Pahlavi needed] (kpyc /⁠kabīz⁠/)

**Ancient Greek**: "καπίθη" (kapíthē), attested in Xenophon's *Anabasis*

**Old Armenian**: "կապիճ" (kapič)

The entry explains that this dry measure originates from Aramaic and ultimately derives from even older sources, including Demotic Egyptian *kpḏ*. The various language forms demonstrate how this measurement unit spread across the Mediterranean and Near Eastern regions through trade and cultural contact, with related terms appearing in Persian, Kurdish, Turkish, and Romance languages.
```


### [2026-09-06T15:53:52.203Z] TOOL RESULT

```
# Entry for Persian کبست (kabast)

Yes, there is an entry for this word. According to Wiktionary, **کبست** (kabast) is a Persian noun meaning "colocynth."

## Etymology

The etymology section notes that the origin is "Unknown" with questionable historical attestations. However, scholars have proposed connections to earlier forms:

- A possible link to Middle Persian *kawastīg* (a flowering plant from the Greater Bundahishn)
- A dubious connection to Avestan *kapastiš*, which refers to an infectious disease
- An alternative theory by Lagarde suggesting a suffix derived from Old Armenian *kapem* ("to bind"), since colocynth plants are creeping vines

The entry explicitly states: "Unknown. Questionable if attested in the Greater Bundahishn" and notes these proposed etymologies remain uncertain.

## Related Terms

Synonyms include حنظل (hanzel) and other Persian terms for bitter melon or colocynth variants.
```


## [2026-09-06T15:54:15.579Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%86%D9%88%D9%86' --note 'page 240, root Kanunu: Arabic kanun < Aramaic/Syriac kanona < Akkadian kanunu/kinunu brazier' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%86%D9%88%D9%86' --note 'page 240, root Kanunu: Persian kanun borrowed from Arabic kanun' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%82%D9%81%D8%B5' --note 'page 240, root Kap node 7/8: Arabic qafas < Aramaic qufsa < Greek kapsa / Latin capsus' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%D9%82%D9%81%D9%8A%D8%B2' --note 'page 240, root Kap node 3-5: Arabic qafiz < MP kabiz/kapic, Greek kapithe (Xenophon Anabasis), Arm. kapic' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/keh%E2%82%82p-' --note 'page 240, root Kap/Qap: PIE *keh2p-/*kap- to seize; descendants Lat capio/capsa, Gmc *habjana, Iranian *cap-, Pers caspidan' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%86%D8%B3%D8%A8%DB%8C%D8%AF%D9%86' --note 'page 240, root Kap node 2: Persian chasbidan < Classical Persian chaspidan' 2>&1 | tail -3\npython3 tools/fetch_source.py 'https://en.wiktionary.org/wiki/%DA%A9%D8%A8%D8%B3%D8%AA' --note 'page 240, root Kapastay node 2: Persian kabast colocynth, etymology unknown; Av. kapastis link dubious' 2>&1 | tail -3",
 "description": "Archive web sources"
}
```


### [2026-09-06T15:54:19.824Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/1f00e3faf679eaa6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/996d2a2f5df34dc4.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/9bf55a85c0bfccf1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/3bef6be4374d0f8b.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/cde0fd884f8751c1.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/957ed1225d522ffe.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e841d4532dc5841.txt
```


## [2026-09-06T15:54:22.884Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe; sed -n '1,80p' tools/verify_check.py",
 "description": "Read verify_check.py"
}
```


### [2026-09-06T15:54:22.920Z] TOOL RESULT

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
```


## [2026-09-06T15:54:25.407Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb; sed -n '80,140p' git/rishe/tools/verify_check.py",
 "description": "Rest of verify_check"
}
```


### [2026-09-06T15:54:27.768Z] TOOL RESULT

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


## [2026-09-06T15:54:54.550Z] AGENT

Now I'll write the verification file.


## [2026-09-06T15:54:57.671Z] TOOL CALL #62: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg240.png\" /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/240.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/240.png",
 "description": "Archive page image"
}
```


### [2026-09-06T15:54:57.731Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 81131 Sep  6 11:54 /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/240.png
```


## [2026-09-06T16:03:48.748Z] TOOL CALL #63: Bash

```json
{
 "command": "cat > \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk240.py\" <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW_KANUN = \"https://en.wiktionary.org/wiki/%D9%83%D8%A7%D9%86%D9%88%D9%86\"\nW_KANUN_FA = \"https://en.wiktionary.org/wiki/%DA%A9%D8%A7%D9%86%D9%88%D9%86\"\nW_QAFAS = \"https://en.wiktionary.org/wiki/%D9%82%D9%81%D8%B5\"\nW_QAFIZ = \"https://en.wiktionary.org/wiki/%D9%82%D9%81%D9%8A%D8%B2\"\nW_KAP = \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/keh%E2%82%82p-\"\nW_CASB = \"https://en.wiktionary.org/wiki/%DA%86%D8%B3%D8%A8%DB%8C%D8%AF%D9%86\"\nW_KABAST = \"https://en.wiktionary.org/wiki/%DA%A9%D8%A8%D8%B3%D8%AA\"\n\ndoc = {\n \"pdf_page\": 240,\n \"book_page\": 210,\n \"verified_by\": \"claude-opus-5\",\n \"verified_on\": \"2026-09-06\",\n \"entries\": []\n}\n\n# ------------------------------------------------------------------ entry 0\ne0 = {\n \"entry\": 0,\n \"root\": \"Kânŭnu\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"Akkadian kanūnu / kinūnu 'brazier, hearth, kiln' (logogram KI.NE)\",\n \"note\": \"The root box is right in every part. Akkadian kanūnu (also kinūnu, written KI.NE) 'brazier, stove, hearth' is well attested (CAD K s.v. kinūnu); it also names a winter ritual and the month in which it fell. Nourai's spelling Kânŭnu matches the a-vocalism variant. Mo'in's own footnote to Borhan-e Qate' gives exactly this Akkadian etymon and exactly this route (Akkadian > Aramaic/Syriac > Arabic > Persian), and Mo'in's Farhang tags the headword [ع. سر. از اکدی] 'Arabic, Syriac, from Akkadian'. Nourai's chart leaves the intermediate boxes empty, but the forms are Syriac ܟܢܘܢܐ kānōnā and Arabic كانون kānūn. Note that this is كانون ۱ only: the homonym کانون 'rule, canon, centre' is from Greek kanōn and is a different word (Mo'in flags it separately) — Nourai correctly disambiguates with «کانون ۱».\",\n \"note_fa\": \"ریشهٔ اکدی kanūnu/kinūnu «آتشدان، منقل، کوره» (با نگارهٔ KI.NE) واژه‌ای است کاملاً شناخته و در فرهنگ آشوری شیکاگو ثبت شده؛ بنابراین نام زبان و معنایی که نورایی داده است درست است. حاشیهٔ معین بر برهان قاطع (ص ۱۵۸۰) همین ریشهٔ اکدی و همین راه وام‌گیری را می‌آورد و در فرهنگ فارسی معین نیز مدخل «کانون» با نشانهٔ [ع. سر. از اکدی] آمده است؛ یعنی از اکدی به آرامی/سریانی ܟܢܘܢܐ kānōnā، از آن به عربی كانون و سپس به فارسی. توجه شود که «کانون» به معنی «قاعده و مرکز» واژهٔ دیگری است و از یونانی kanōn می‌آید؛ نورایی با آوردن «کانون ۱» درست تفکیک کرده است. ادعای نورایی درست است.\",\n \"sources\": [W_KANUN, W_KANUN_FA],\n \"ref_check\": [\n  {\"ref\": \"MON:2875\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. کانون (2-vol Adena OCR, MON_part2.txt): 'ک‌انون: [ع. سر. از اکدی] (اِ.) آتشدان ... این نام از عصر اکدی اطلاق شده و در کتیبه‌های [تدمر/پالمیر] هم به نام ماه‌های سال اطلاق گردیده ... بعدها کانون نام دو ماه سریانی گردید: کانون اول ... کانون آخر'. The bracket tag [ع. سر. از اکدی] = 'Arabic, Syriac, from Akkadian' is Nourai's whole chain in three words.\"},\n  {\"ref\": \"BQT:1580\", \"status\": \"supports\", \"note\": \"Borhan-e Qate', Mo'in's footnote 9 to کانون (vol 3 scan, BQT_v3_pages.txt pdf leaf 373 ≈ printed p.1578-80): 'کانون در عربی و سریانی بمعنی آتشدان است و نیز بدو ماه کانون اول و کانون دوم اطلاق شده، و اصل کلمه سامی است، و آن از عصر اکدی بدین دو ماه اطلاق گردیده. در زبان اکدی [kanūnu] بمعنی (آتشدان) است ... «معجمیات عربیه - سامیه ص ۲۷۰»'. Footnote 11 adds that the name occurs in the Palmyrene inscriptions (S. A. Cook, A Glossary of the Aramaic Inscriptions) and later became the Syriac month name.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol 3, printed ~p.1578-80 (pdf leaf 373), Mo'in's fn. 9 and 11 to کانون\", \"stance\": \"supports\", \"note\": \"'اصل کلمه سامی است، و آن از عصر اکدی ... در زبان اکدی [kanūnu] بمعنی (آتشدان) است'\"},\n  {\"src\": \"MON\", \"where\": \"s.v. کانون\", \"stance\": \"supports\", \"note\": \"'[ع. سر. از اکدی] (اِ.) آتشدان'\"},\n  {\"src\": \"AKD\", \"where\": \"AKD.txt, grep -i 'kanunu|kānūn'\", \"stance\": \"silent\", \"note\": \"Zimmern, Akkadische Fremdwörter, has no entry for kanūnu/kinūnu in the OCR text — the brazier word is not among his Akkadian loan-words in Aramaic/Arabic.\"},\n  {\"src\": \"AFA\", \"where\": \"AFA.txt, grep -i 'kanun'\", \"stance\": \"silent\", \"note\": \"Fraenkel, Die aramäischen Fremdwörter im Arabischen: no hit for kānūn in the OCR (he treats Aramaic words in Arabic, and kānūn is not in the searchable text).\"}\n ],\n \"nodes\": []\n}\n\ne0[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Syriac\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box: the word Nourai means is Syriac ܟܢܘܢܐ (kānūnā) 'brazier, hearth', borrowed from Akkadian kanūnu with the regular Aramaic determined-state ending -ā. Aramaic and Akkadian were in continuous contact in Babylonia from the 8th c. BCE on, and Akkadian household and calendar vocabulary passed into Aramaic in bulk; the same word also became the Syriac name of the two winter months Kānōn qdem / Kānōn ḥray (December / January), the season of braziers, which is how it reached Arabic كانون الأول / كانون الثاني. Mo'in's footnote records that the name is already in the Palmyrene Aramaic inscriptions.\",\n \"derivation_fa\": \"این جعبه در کتاب خالی است؛ صورت مورد نظر سریانی ܟܢܘܢܐ (kānūnā) «آتشدان، منقل» است که از اکدی kanūnu وام گرفته شده و پسوند حالت معرفهٔ آرامی ‎-ā‎ به آن افزوده شده است. از سدهٔ هشتم پیش از میلاد آرامی و اکدی در بین‌النهرین در تماس پیوسته بودند و بسیاری از واژه‌های خانگی و تقویمی اکدی به آرامی راه یافت. همین واژه نام دو ماه زمستانی سریانی (کانون اول و کانون آخر) نیز شد و از این راه به عربی رسید. حاشیهٔ معین یادآور می‌شود که این نام در سنگ‌نبشته‌های آرامی تدمر (پالمیر) هم دیده می‌شود. ادعای نورایی درست است.\",\n \"sources\": [W_KANUN],\n \"ref_check\": [\n  {\"ref\": \"MON:2875\", \"status\": \"supports\", \"note\": \"Mo'in's origin tag on کانون is '[ع. سر. از اکدی]' — the سر. (Syriac) is precisely this node.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol 3, Mo'in's fn. 11 to کانون (pdf leaf 373)\", \"stance\": \"supports\", \"note\": \"'این نام در کتیبه‌های پالمیر آمده (رك: S. A. Cook, A Glossary of the Aramaic Inscriptions) ... بعدها کانون نام دو ماه سریانی گردید'\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt, grep 'kanun'\", \"stance\": \"silent\", \"note\": \"Klein has no English derivative of this Semitic word, so no entry; recorded as a negative result.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Arabic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box: Arabic كانون (kānūn), pl. كوانين, 'brazier, fire-pan, hearth', borrowed from Syriac/Aramaic kānūnā, not from an Arabic root (there is no Arabic root k-n-n that yields this shape with ā-ū; the ك-ن-ن root means 'to cover, shelter' and is a secondary folk-attachment). The same loan gave the Levantine month names كانون الأول and كانون الثاني, still the ordinary Arabic names of December and January, which betray the Syriac calendar as the channel.\",\n \"derivation_fa\": \"این جعبه نیز خالی است و مقصود عربی كانون (جمع: کوانین) «آتشدان، منقل» است که از سریانی/آرامی kānūnā وام گرفته شده، نه ساختهٔ ریشهٔ عربی. ریشهٔ ک‌ن‌ن عربی به معنی «پوشاندن و پناه دادن» است و پیوند دادن کانون به آن ریشه‌شناسی عامیانه است. نام دو ماه كانون الأول و كانون الثاني (دسامبر و ژانویه) در شام تا امروز به کار می‌رود و همین نشان می‌دهد که راه ورود واژه، تقویم سریانی بوده است. ادعای نورایی درست است.\",\n \"sources\": [W_KANUN],\n \"ref_check\": [\n  {\"ref\": \"MON:2875\", \"status\": \"supports\", \"note\": \"'[ع. سر. از اکدی]' — the ع. (Arabic) box of Nourai's chart.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol 3, Mo'in's fn. 9 to کانون\", \"stance\": \"supports\", \"note\": \"'کانون در عربی و سریانی بمعنی آتشدان است و نیز بدو ماه کانون اول و کانون دوم اطلاق شده'\"},\n  {\"src\": \"MON\", \"where\": \"s.v. کانون\", \"stance\": \"supports\", \"note\": \"origin tag [ع. سر. از اکدی]\"},\n  {\"src\": \"AFM\", \"where\": \"AFM.txt (Addi Shir), grep 'كانون'\", \"stance\": \"silent\", \"note\": \"Addi Shir's list of Persian words Arabicized has no كانون, consistent with the word being Aramaic and not Persian in origin.\"}\n ]\n})\n\ne0[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Persian\", \"words\": \"kânŭn «کانون ۱»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian کانون (kānūn) 'fireplace, hearth, brazier' is an Arabic loan of the Islamic period, taken over unchanged in shape (Arabic kānūn > NP kānūn); the Anvari verse quoted on the page ('چو گیرد آتش خشم تو بالا…نیم کانون') already uses it in the 12th c. in the literal 'brazier' sense. Modern Persian has extended it metaphorically to 'centre, focus, society, club', which is where it collides with the unrelated کانون < Greek kanōn 'rule' — Mo'in keeps the two apart and so does Nourai's «کانون ۱». The chart's gloss 'hart' is a typo for 'hearth'.\",\n \"derivation_fa\": \"«کانون» در فارسی نو وام‌واژه‌ای عربی از دورهٔ اسلامی است که بی هیچ دگرگونی آوایی (عربی kānūn > فارسی kānūn) پذیرفته شده است؛ بیت انوری که در همین صفحه آمده («چو گیرد آتش خشم تو بالا… نیابد از دو عالم نیم کانون») نشان می‌دهد که در سدهٔ ششم هجری هنوز به معنی حقیقی «آتشدان» به کار می‌رفته است. در فارسی امروز معنای مجازی «مرکز، مجمع، انجمن» یافته و همین آن را با «کانون» دیگر (از یونانی kanōn «قاعده») هم‌آوا کرده است؛ معین این دو را جدا آورده و نورایی هم با نشانهٔ «کانون ۱» درست تفکیک کرده است. ادعای نورایی درست است. (واژهٔ hart در معنای انگلیسی، غلط چاپی به جای hearth است.)\",\n \"sources\": [W_KANUN_FA, W_KANUN],\n \"ref_check\": [\n  {\"ref\": \"BQT:1580\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' s.v. کانون (vol 3, pdf leaf 373): 'کانون = بروزن قانون، بمعنی آتشدان باشد مطلقاً اعم از گلخن یا منقل آتشی ... و بلغت سریانی نام دو تن از ماه‌های رومی است که کانون اول و کانون آخر باشد', with Mo'in's Akkadian footnote attached.\"},\n  {\"ref\": \"MON:2875\", \"status\": \"supports\", \"note\": \"Mo'in s.v. کانون: '[ع. سر. از اکدی] (اِ.) آتشدان'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol 3, printed ~p.1578-80 s.v. کانون\", \"stance\": \"supports\", \"note\": \"'بمعنی آتشدان باشد مطلقاً اعم از گلخن یا منقل آتشی'\"},\n  {\"src\": \"MON\", \"where\": \"s.v. کانون\", \"stance\": \"supports\", \"note\": \"'[ع. سر. از اکدی] (اِ.) آتشدان'\"},\n  {\"src\": \"HRN\", \"where\": \"HRN.txt, grep 'kanun'\", \"stance\": \"silent\", \"note\": \"Horn's Grundriss der neupersischen Etymologie has no entry — as expected, since he treats inherited Iranian words and not Arabic loans.\"},\n  {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, grep 'kanun'\", \"stance\": \"silent\", \"note\": \"MacKenzie has no Pahlavi kānūn, confirming that the word entered Persian only after the Arab conquest.\"}\n ]\n})\n\ndoc[\"entries\"].append(e0)\n\n# ------------------------------------------------------------------ entry 1\ne1 = {\n \"entry\": 1,\n \"root\": \"Kap, Qap\",\n \"verdict\": \"confirmed\",\n \"modern_form\": \"PIE *kap- / *keh₂p- 'to seize, grasp, hold'\",\n \"note\": \"Pokorny 527-528 'Root/lemma: kap-, kəp-; Meaning: to grab', and Watkins/AHD 'kap-. To grasp. [Pok. kap- 527]'. Nourai's page number is exactly right and his gloss 'grasp' is Watkins' word. The doublet spelling 'Kap, Qap' is Nourai's own notation for the labiovelar-less plain velar; Pokorny writes kap-, kəp- (full and reduced grade), and Wiktionary now writes *keh₂p- with a laryngeal (LIV 344 f. *keh₂p-). Pokorny himself remarks that the vocalism is 'absolutely almost a' and that the root, with its variants kap-/ghabh-/gʰabʰ-, looks like an imitation of 'short snapping sounds'; Wiktionary calls it 'possibly a non-Indo-European loanword ... onomatopoeic or sound-symbolic'. So the root box is right, but it is one of the shakier PIE reconstructions, and the related root ghabh- (Lat. habēre, Eng. give) is kept separate by both Pokorny and Watkins ('Compare ghabh-').\",\n \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kap- «گرفتن، چنگ زدن» است؛ پوکورنی در صفحهٔ ۵۲۷-۵۲۸ آن را با عنوان «kap-, kəp-: to grab» آورده و واتکینز در پیوست فرهنگ American Heritage نیز «kap-. To grasp. [Pok. kap- 527]». پس شمارهٔ صفحه‌ای که نورایی داده و معنایی که آورده هر دو درست است. صورت دوگانهٔ «Kap, Qap» نشانه‌گذاری خود نورایی است؛ ویکی‌واژه امروز آن را با حنجره‌ای *keh₂p- بازسازی می‌کند. باید افزود که خود پوکورنی این ریشه را از آواهای تقلیدی («صدای ناگهانی چنگ زدن») می‌داند و ویکی‌واژه احتمال وام‌واژهٔ غیرهندواروپایی بودن آن را مطرح می‌کند؛ نیز ریشهٔ نزدیک ghabh- (لاتینی habēre) را هم پوکورنی و هم واتکینز جدا نگه می‌دارند. ادعای نورایی دربارهٔ خود ریشه درست است.\",\n \"sources\": [W_KAP],\n \"ref_check\": [\n  {\"ref\": \"POK:527\", \"status\": \"supports\", \"note\": \"POK_full.txt line ~43698: 'Root / lemma: kap- ; Meaning: to grab ; ... References: WP. I 342 ff., WH. I 159 f., 169. Page(s): 527-528'. The entry contains the Latin, Greek, Germanic, Celtic and Iranian material Nourai puts on the chart.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"POK_full.txt, 'Root / lemma: kap-', Page(s) 527-528\", \"stance\": \"supports\", \"note\": \"'Meaning: to grab ... The vocalism is absolutely almost a ... imitation of short snapping sounds (kap, ghap, ghabh etc.)'\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 342 ff. (cited by Pokorny at the foot of the kap- entry)\", \"stance\": \"supports\", \"note\": \"Pokorny's own reference line 'References: WP. I 342 ff.' — Walde-Pokorny Bd. I p.342 is the parent article for this root.\"},\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt line 581 s.v. kap-\", \"stance\": \"supports\", \"note\": \"'kap-. To grasp. I. Basic form *kap- ... 3. Form *kap-o- in Germanic *habai-, *habēn ... 4. Germanic hafigaz, \\\"containing something,\\\" having weight ... II. Suffixed form *kap-yo- ... Latin capere ... III. Suffixed form *kap-s- in Latin capsa, repository, case ... [Pok. kap- 527.]'\"},\n  {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 271 (~printed p.510-512), s.vv. kapiō/kapmi, kapsō, kapsos\", \"stance\": \"supports\", \"note\": \"Mann: 'kapiō, kapmi \\\"take, seize, lift\\\". WP I, 342 ... Gk. kápo, kápto; Alb. kap; Lat. capiō'; 'kapsō (form of kap-) \\\"catch, seize, hold\\\" ... Per. cf. časpam'\"}\n ],\n \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Old Persian\", \"words\": \"čifsati\",\n \"verdict\": \"disputed\",\n \"derivation\": \"No such verb exists in the Old Persian corpus. Old Persian is known from the Achaemenid royal inscriptions only, and its lexicon (Kent, Old Persian, 1953, lexicon pp. 164-215) contains no *čifsati- / *čafs-; a 3rd sg. present in -ati of this shape is a Sanskrit-style citation form, not an attested Old Persian word. The form is however not Nourai's invention: Aryanpur Kashani's Farhang-e Rishe-hā-ye Hend-o-Orupāyi lists 'ČIFSATI (OLD PERSIAN)' in the index to this very root, next to Pashto CHASP/CHASPAN, Sanskrit KAPATI, Latin CAPERE, Gothic HAFJAN (ARY_latin_index_pages.txt, pdf page 222 = printed 223), and Nourai reproduces Aryanpur's box wholesale. What the sources really reconstruct is an Old/Proto-Iranian root *čap- 'to seize, stick, strike' with an s-inchoative stem *čap-s-/*čafs- (Cheung, Etymological Dictionary of the Iranian Verb, s.v. *čap; Horn no. 441). The right label for the box is therefore 'Old Iranian *čafs-/*čaps-', not 'Old Persian čifsati'; and the vowel should be a, not i.\",\n \"derivation_fa\": \"چنین فعلی در پیکرهٔ پارسی باستان وجود ندارد. پارسی باستان تنها از سنگ‌نبشته‌های هخامنشی شناخته می‌شود و در واژه‌نامهٔ کنت (Old Persian، ۱۹۵۳) هیچ *čifsati یا *čafs- نیامده است؛ صورتی با پایانهٔ ‎-ati‎ (سوم‌شخص مفرد حال) شیوهٔ نقل واژه‌های سنسکریت است نه پارسی باستان. با این همه این صورت ساختهٔ نورایی نیست: آریان‌پور کاشانی در «فرهنگ ریشه‌های هند و اروپایی زبان فارسی» (ص ۲۲۳) ذیل همین ریشه «ČIFSATI (OLD PERSIAN)» را در کنار CHASP، CHASPAN افغانی، KAPATI سنسکریت، CAPERE لاتینی و HAFJAN گوتی آورده و نورایی همان جدول را بازنویسی کرده است. آنچه پژوهش امروزی بازسازی می‌کند ستاک ایرانی باستان *čap- «گرفتن، چسبیدن، زدن» با ستاک آغازی ‎(inchoative)‎ *čap-s-/*čafs- است (چونگ، ذیل *čap؛ هرن، شمارهٔ ۴۴۱). پس برچسب درست این جعبه «ایرانی باستان *čafs-» است نه «پارسی باستان čifsati»، و واکهٔ آن a است نه i. پژوهش امروزی این صورت را رد می‌کند.\",\n \"sources\": [W_KAP],\n \"ref_check\": [\n  {\"ref\": \"BQT:636\", \"status\": \"partial\", \"note\": \"Borhan-e Qate' s.v. چسبیدن is on printed p.634 (BQT_v2_pages.txt leaf 94), i.e. Nourai's 636 is two pages out. Mo'in's footnote 5 there reads '= چیسدن (ه.م.) = چفیدن (ه.م.). از ریشهٔ ایرانی … čapsēdan (چسبنده) «[اساس اشتقاق]. هوبشمان ۱۶۸…»' — Mo'in cites an IRANIAN root and Hübschmann, and gives no Old Persian form at all, still less čifsati.\"}\n ],\n \"consulted\": [\n  {\"src\": \"ARY\", \"where\": \"ARY_latin_index_pages.txt, pdf page 222 (printed 223), index block for the root kap-\", \"stance\": \"supports\", \"note\": \"'HEFFEN / ČIFSATI :(OLD PERSIAN) … CHASP, CHASPAN (AFGHANI) … CACHT, KAPATI :(SANSKRIT) … CAPERE, CAPTARE, CAPIO (LATIN) … HAFJAN (GOTHIC)' — with 'REFERENCES: POKORNY'. This is evidently Nourai's source for the form, but Aryanpur is not an authority on the Old Persian corpus.\"},\n  {\"src\": \"KNT\", \"where\": \"KNT.txt, grep 'cifs|kapi|kapitha'\", \"stance\": \"silent\", \"note\": \"Kent's Old Persian lexicon returns nothing for čifs-/kapiθ-; the Old Persian corpus simply does not contain these words.\"},\n  {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt, root *čap 'to seize, attach, stick, strike'\", \"stance\": \"contradicts\", \"note\": \"Cheung sets up Proto-Iranian *čap-, with NP čafsīdan, Qohrudi časpāda/časp-, Ossetic cæfsyn (inch.) 'to stick, glue' — an inchoative *čap-s-, not an Old Persian *čifsati.\"},\n  {\"src\": \"HRN\", \"where\": \"HRN.txt p.98, no. 441\", \"stance\": \"contradicts\", \"note\": \"'441. čespīden, čepsīden, čefsīden (Inchoat.) \\\"packen, fassen\\\"' — Horn labels the s as an inchoative suffix on a Persian verb and cites no Old Persian antecedent.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"časbîdan «چسبیدن»; extra: چسپیدن ، چپسیدن ، چفسیدن ، چسب\",\n \"verdict\": \"plausible\",\n \"derivation\": \"New Persian چسبیدن (časbīdan) 'to stick, adhere', older and more correct چسپیدن (časpīdan), with the metathesised چپسیدن (čapsīdan) and the fricativised چفسیدن (čafsīdan) — exactly the three variants Horn prints — plus the deverbal noun چسب (časb) 'glue'. The stem is Iranian *čap-s-, an s-inchoative of *čap- 'to seize, stick', continued in Ossetic cæfsyn 'to stick', Balochi čampit 'to snatch', Pashto časp-. Pokorny does put the Persian here: at the head of the kap- article he writes 'with Indo-Germanic … npers. časpīdan, čapsīdan, čafsīdan \\\"grasp, capture, catch\\\"', and Horn 441 refers it 'zu lat. capiō (Nöldeke, mündliche Mitteilung)'. The reservation is phonological and is why this is 'plausible', not 'confirmed': PIE *k before *a should stay k in Iranian (whence kaf-, not čaf-), so the initial č- is unexplained. Mann notes it in so many words ('Per. cf. časpam \\\"adhere\\\", but Per. č- derives fr. *k- usually before IE *-e/i'), and Cheung concludes: 'The connection with Gr. καπτω, Lat. capere … is semantically very attractive. IE \\\"a\\\" would not palatalize the preceding velar in (O)Ir. though: Ir. *č- in *čap- is from *ček/g-?'. So the Persian word is real and the sense fits, but the equation with *kap- is an old and still unresolved conjecture.\",\n \"derivation_fa\": \"«چسبیدن» در فارسی نو، و صورت کهن‌تر و درست‌تر «چسپیدن» (časpīdan)، همراه با گونهٔ مقلوب «چپسیدن» و گونهٔ سایشی‌شدهٔ «چفسیدن» — یعنی همان سه صورتی که هرن ثبت کرده — و اسم مصدرِ «چسب». ستاک آن ایرانی *čap-s- است، ستاک آغازی ‎(inchoative)‎ با ‎-s-‎ از ریشهٔ *čap- «گرفتن، چسبیدن»، که در آسی cæfsyn «چسبیدن»، بلوچی čampit و پشتو časp- نیز بازمانده است. پوکورنی در آغاز مدخل kap- خود صریحاً «npers. časpīdan, čapsīdan, čafsīdan» را در همان ریشه جای می‌دهد و هرن (شمارهٔ ۴۴۱) آن را به پیروی از نُلدکه با لاتینی capiō می‌سنجد. اما یک ایراد آوایی هست و به همین سبب حکم ما «با احتیاط پذیرفتنی» است: در ایرانی، k آغازین پیش از a دگرگون نمی‌شود و باید kaf- می‌داد نه čaf-؛ مان به این نکته اشاره کرده و چونگ نیز می‌گوید پیوند معنایی «بسیار جذاب» است ولی «a هندواروپایی نمی‌تواند واک پیشین را کامی کند»، پس شاید *ček/g- در کار باشد. بنابراین خودِ واژه اصیل و معنا درست است، ولی پیوند آن با *kap- فرضیه‌ای است دیرین و هنوز ناتمام.\",\n \"sources\": [W_KAP, W_CASB],\n \"ref_check\": [\n  {\"ref\": \"POK:527\", \"status\": \"supports\", \"note\": \"POK_full.txt, kap- article (Page(s) 527-528), opening Material paragraph: '… with Indo Germanic enpers. caspīdan, capsīdan, cafsīdan \\\"grasp, capture, catch\\\"' — the three Persian variants stand in Pokorny's own text on the cited page.\"},\n  {\"ref\": \"HRN:98\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.98 no. 441 (HRN.txt leaf 119): 'čespīden, čepsīden, čefsīden (Inchoat.) \\\"packen, fassen\\\". Zu lat. capiō (Nöldeke, mündliche Mitteilung). Also vergl. got. hafjan \\\"heben\\\", hafts \\\"behaftet, gefesselt\\\"; gr. σκάπη \\\"Griff\\\"; air. cacht \\\"Sklave\\\"; lett. kampt \\\"fassen\\\".'\"},\n  {\"ref\": \"IEC:473\", \"status\": \"not_found\", \"note\": \"Mann's page 473 falls among the i- entries (IEC.txt leaf ~251: isios, -isk-). The relevant Mann article, 'kapsō (form of kap-, see kapiō, kapmi) \\\"catch, seize, hold\\\". WP I, 342. Per. cf. časpam (\\\"adhere\\\", but Per. č- derives fr. *k- usually before IE *-e/i)', stands at leaf 271 ≈ printed p.510-512. The content supports Nourai, but the page number does not match.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"p.98 no. 441\", \"stance\": \"supports\", \"note\": \"'čespīden, čepsīden, čefsīden (Inchoat.) \\\"packen, fassen\\\". Zu lat. capiō'\"},\n  {\"src\": \"CHEUNG\", \"where\": \"CHEUNG.txt s.v. *čap 'to seize, attach, stick, strike'\", \"stance\": \"partial\", \"note\": \"'This root may have an IE etymology. The connection with Gr. καπτω, Lat. capere, etc. (cf. IEW, l.c.) is semantically very attractive. IE \\\"a\\\" would not palatalize the preceding velar in (O)Ir. though: Ir. *č- in *čap- is from *ček/g-? *PIE ? *k(e)H₂p- (*kap-) … LIV: 344 f. | Pok.: 527 ff.'\"},\n  {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 271 s.v. kapsō\", \"stance\": \"partial\", \"note\": \"'Per. cf. časpam (\\\"adhere\\\", but Per. č- derives fr. *k- usually before IE *-e/i)' — Mann files the Persian here but flags the same phonological difficulty.\"},\n  {\"src\": \"BQT\", \"where\": \"vol 2, printed p.634, Mo'in's fn. 5 to چسبیدن\", \"stance\": \"supports\", \"note\": \"'= چیسدن = چفیدن. از ریشهٔ ایرانی … čapsēdan (چسبنده) «… هوبشمان …»' — an Iranian root with the čapsēdan variant.\"},\n  {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, grep 'časp|cafs'\", \"stance\": \"silent\", \"note\": \"MacKenzie has no Pahlavi *časpīdan; the verb is first recorded in New Persian.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 3, \"lang\": \"Old Persian\", \"words\": \"kapithe\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Old Persian *kapiθā-, a dry measure. It is not preserved in the cuneiform corpus but is recorded in Greek transcription as ἡ καπίθη, glossed by Xenophon (Anabasis I.5.6) as δύο χοίνικες, i.e. two choinikes (≈2 litres); Pokorny prints it in the kap- article exactly so: 'Old pers. ἡ καπίθη \\\"δύο χοίνικες\\\"', beside Old Indic kapaṭī 'two handfuls'. The word is thus a nominal derivative of *kap- 'to grasp', literally 'a handful, what the hand holds', and Nourai's gloss 'a box for measuring grain' is a shade too concrete — it is the measure itself, not a box. The language label is right in the philological sense (Xenophon says the Persians used it); note that the attestation is Greek, not Old Persian script.\",\n \"derivation_fa\": \"پارسی باستان *kapiθā-، پیمانه‌ای برای غله. این واژه در خط میخی به دست نیامده، ولی به نویسه‌گردانی یونانی ἡ καπίθη ثبت شده و گزنفون در «آناباسیس» (۱٫۵٫۶) آن را «دو خوینیکس» (نزدیک دو لیتر) معنی کرده است؛ پوکورنی در همان صفحهٔ ۵۲۷ عیناً می‌آورد: «Old pers. ἡ καπίθη \\\"δύο χοίνικες\\\"» و در کنارش سنسکریت kapaṭī «دو مشت». پس این واژه اسمی است ساخته از ریشهٔ *kap- «گرفتن»، در اصل «یک مشت، آنچه دست فرا می‌گیرد». معنایی که نورایی داده («جعبه‌ای برای پیمانهٔ غله») اندکی مادی‌تر از حد است؛ خودِ پیمانه است نه ظرف. ادعای نورایی درست است، با این یادآوری که گواهی واژه یونانی است نه میخی.\",\n \"sources\": [W_QAFIZ, W_KAP],\n \"ref_check\": [\n  {\"ref\": \"POK:527\", \"status\": \"supports\", \"note\": \"POK_full.txt, kap- article, Material: 'Old Indic kapaṭī \\\"two handful\\\" (Middle Indic for t), Old pers. ἡ καπίθη \\\"δύο χοίνικες\\\"' — literally Nourai's node, on his cited page.\"},\n  {\"ref\": \"HUB:89\", \"status\": \"supports\", \"note\": \"Hübschmann, Persische Studien p.89 (HUB.txt leaf 99), addendum to no. 875: 'Hier fehlt np. kavīz, kavīž = arab. LW. qafīz u.s.w., phl. kapīč (so zu lesen) Gl. and Ind. 197 u.s.w., arm. LW. kapič \\\"ein Maass für Getreide\\\" etc., ap. καπίθη de Lagarde, Ges. Abh. 198.' — 'ap.' = altpersisch καπίθη, exactly Nourai's Old Persian box.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"POK_full.txt, kap- article, p.527\", \"stance\": \"supports\", \"note\": \"'Old pers. ἡ καπίθη \\\"δύο χοίνικες\\\"'\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien p.89, add. to no. 875\", \"stance\": \"supports\", \"note\": \"'ap. καπίθη de Lagarde, Ges. Abh. 198'\"},\n  {\"src\": \"LKT\", \"where\": \"LKT.txt no. 998 'Ar. kafīz'\", \"stance\": \"supports\", \"note\": \"'Ein Hohlmaß, \\\"Scheffel\\\" [aus gr. καπίθη, aber wohl über pers. kavīz, kavīz entlehnt … \\\"In Babylonien lernten die Araber das alte dort übliche Getreidemaß καπίθη kennen (Xenophon Anab. I,5,6) und nahmen es in der Form kafyz an\\\"]'\"},\n  {\"src\": \"KNT\", \"where\": \"KNT.txt, grep 'kapi|kapitha'\", \"stance\": \"silent\", \"note\": \"Kent's Old Persian lexicon has no kapiθā-, as expected for a word known only from Greek transcription.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 4, \"lang\": \"Pahlavi\", \"words\": \"kapîč\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Middle Persian kapīč / kabīz (Book Pahlavi kpyc), the same dry measure carried on from Old Iranian *kapiθā- with the regular Middle Iranian outcome of the diminutive/instrument suffix -ča(ka)- and intervocalic weakening of the dental. Hübschmann states the form and the reading explicitly ('phl. kapīč (so zu lesen)') and adduces the Armenian loan կապիճ (kapič) 'a measure for grain', which fixes the Middle Iranian shape independently: Armenian borrowed Parthian/Middle Persian words in the Arsacid and early Sasanian period with faithful preservation of -č. The Arabic borrowing qafīz (with p > f, as regularly in Arabic renderings of Iranian p) confirms the same base.\",\n \"derivation_fa\": \"فارسی میانه kapīč / kabīz (به خط پهلوی کتابی kpyc)، همان پیمانهٔ غله که از ایرانی باستان *kapiθā- بازمانده و پسوند ‎-ča(ka)-‎ در آن به ‎-č‎ فارسی میانه بدل شده است. هوبشمان صورت و خوانش را صریح می‌آورد: «phl. kapīč (so zu lesen)»، و وام‌واژهٔ ارمنی կապիճ (kapič) «پیمانه‌ای برای غله» را نیز گواه می‌گیرد؛ ارمنی واژه‌های پارتی و فارسی میانه را در دورهٔ اشکانی و ساسانیِ آغازین با حفظ دقیق ‎-č‎ وام گرفته است، پس این وام‌واژه صورت میانه را مستقلاً تأیید می‌کند. معرّب آن «قفیز» است که در آن p ایرانی طبق قاعده به f بدل شده. ادعای نورایی درست است.\",\n \"sources\": [W_QAFIZ],\n \"ref_check\": [\n  {\"ref\": \"MON:3010\", \"status\": \"supports\", \"note\": \"Mo'in, Farhang-e Farsi s.v. کفیز (MON_part2.txt): 'کفیز: [- کویز - کویژ معر. قفیز] (اِ.) پیمانه‌ای است برای غلات' — Mo'in equates kafīz = kavīz = kavīž and marks qafīz as the Arabicised form; the Pahlavi antecedent is what the print edition adds in Latin script.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HUB\", \"where\": \"Persische Studien p.89, add. to no. 875\", \"stance\": \"supports\", \"note\": \"'phl. kapīč (so zu lesen) Gl. and Ind. 197 u.s.w., arm. LW. kapič \\\"ein Maass für Getreide\\\"'\"},\n  {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, grep 'kapīč|kapic|kabīz'\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary does not list the measure; it is known from the Pahlavi glossaries (Hübschmann's 'Gl. and Ind. 197') rather than from MacKenzie's core corpus.\"},\n  {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'kapīč|kapic'\", \"stance\": \"silent\", \"note\": \"Nyberg's Manual of Pahlavi glossary has no entry either — a negative result, not a contradiction.\"},\n  {\"src\": \"LKT\", \"where\": \"LKT.txt no. 998\", \"stance\": \"supports\", \"note\": \"'aus gr. καπίθη, aber wohl über pers. kavīz, kavīz entlehnt' — the Iranian stage is the bridge to Arabic.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 5, \"lang\": \"Persian\", \"words\": \"kavîz «کویز»; extra: کویژ ، کفیز ، قفیز\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian کویز (kavīz), variant کویژ (kavīž), a measure of capacity for grain, from MP kapīč: intervocalic -p- lenites to -v- (as in āp > āb, kapōtar > kabūtar / kavūtar), and the final -č devoices/spirantises to -z/-ž in this word as often in measure-names. The Arabic borrowing قفیز (qafīz), taken over in Iraq from the Sasanian land-tax vocabulary, was re-borrowed into Persian as کفیز/قفیز, so that the chart's four spellings are two Iranian forms plus one Arabic round-trip. Mo'in states this in one line: 'کفیز [= کویز = کویژ، معرّب قفیز] پیمانه‌ای است برای غلات'. From Arabic qafīz the word travelled on into Spanish/Catalan cafiz, cahiz and Sicilian vafisu.\",\n \"derivation_fa\": \"«کویز» و گونهٔ «کویژ» در فارسی نو، پیمانه‌ای برای غله، از فارسی میانهٔ kapīč: پ میان دو واکه در فارسی نو به و نرم شده (چنانکه āp > آب و kapōtar > کبوتر/کووتر) و چ پایانی در نام این پیمانه به ز/ژ بدل شده است. صورت معرّب آن «قفیز» است که عرب‌ها آن را در عراق از اصطلاحات خراج ساسانی گرفتند و سپس همان معرّب به شکل «کفیز/قفیز» به فارسی بازگشت؛ پس چهار املای این جعبه دو صورت ایرانی است به‌علاوهٔ یک دوگانهٔ رفت‌وبرگشتی از راه عربی. معین در یک سطر همین را می‌گوید: «کفیز [= کویز = کویژ، معرّب قفیز] پیمانه‌ای است برای غلات». از عربی قفیز واژه به اسپانیایی و کاتالانی cafiz و cahiz و سیسیلی vafisu نیز رفته است. ادعای نورایی درست است.\",\n \"sources\": [W_QAFIZ],\n \"ref_check\": [\n  {\"ref\": \"MON:3010\", \"status\": \"supports\", \"note\": \"Mo'in s.v. کفیز (MON_part2.txt): 'کفیز: [- کویز - کویژ معر. قفیز] (اِ.) پیمانه‌ای است برای غلات.' — all four of Nourai's spellings (کویز، کویژ، کفیز، قفیز) in a single bracket.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"s.v. کفیز\", \"stance\": \"supports\", \"note\": \"'[- کویز - کویژ معر. قفیز] (اِ.) پیمانه‌ای است برای غلات'\"},\n  {\"src\": \"HUB\", \"where\": \"Persische Studien p.89, add. to no. 875\", \"stance\": \"supports\", \"note\": \"'Hier fehlt np. kavīz, kavīž = arab. LW. qafīz u.s.w.'\"},\n  {\"src\": \"LKT\", \"where\": \"LKT.txt no. 998 'Ar. kafīz'\", \"stance\": \"supports\", \"note\": \"'wohl über pers. kavīz, kavīz entlehnt … hieraus kat. cafiz, sp. pg. cahiz, it. (dial. Calabrien) cavizzu, siz. vafisu \\\"ein Ölmaß\\\"'\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. cafiz\", \"stance\": \"supports\", \"note\": \"'cafiz, n., a measure of capacity. — Sp., fr. Arab. qafiz, a measure for corn.'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 6, \"lang\": \"Greek\", \"words\": \"kapsa\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Greek κάψα (kápsa) 'box, chest' is a real word with the right meaning, but it is not an independent Greek reflex of PIE *kap- as the chart's arrow from the root box implies: it is a loan from Latin. Pokorny says so in the kap- article itself — Latin 'capsus \\\"the carriage body; cage for wild animal\\\" (out of it gr. κάψα, κάμψα)' — and Mann marks Latin capsa 'as Gk. LW?' the other way round while still listing Gk. kápsa under kapsos. Latin capsa/capsus is the genuine *kap-s- formation (Watkins: 'III. Suffixed form *kap-s- in Latin capsa, repository, case'). The word entered Greek in the Roman imperial period along with much Latin household and administrative vocabulary, and it is from Hellenistic/Byzantine Greek (or directly from Latin in Syria) that Aramaic took it. So the sense, the form and the destination are right; only the arrow's direction from the PIE root, bypassing Latin, is wrong.\",\n \"derivation_fa\": \"یونانی κάψα (kápsa) «جعبه، صندوقچه» واژه‌ای واقعی است با همان معنا، اما بر خلاف آنچه پیکان کتاب می‌رساند بازماندهٔ مستقل *kap- هندواروپایی در یونانی نیست، بلکه وام‌واژه‌ای است از لاتینی. خود پوکورنی در همان مدخل kap- می‌نویسد که لاتینی capsus «قفس جانور وحشی» بوده و «κάψα و κάμψα یونانی از آن است». صورت اصیل ساخته‌شده از *kap-s- همان لاتینی capsa است (واتکینز: «صورت پسوندی *kap-s- در لاتینی capsa»). این واژه در دورهٔ امپراتوری روم همراه انبوهی از واژه‌های خانگی و دیوانی لاتینی وارد یونانی شد و آرامی آن را از یونانیِ هلنیستی/بیزانسی (یا مستقیماً از لاتینیِ شام) گرفت. پس معنا و صورت و مقصد درست است و تنها جهت پیکان — یعنی رفتن از ریشه به یونانی بی‌واسطهٔ لاتینی — نادرست است؛ ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [W_QAFAS, W_KAP],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"POK_full.txt, kap- article p.527\", \"stance\": \"partial\", \"note\": \"'capsa \\\"a repository, box, esp. for books\\\" … capsus \\\"the carriage body; cage for wild animal\\\" (out of it gr. κάψα, κάμψα)' — Greek from Latin, not from PIE directly.\"},\n  {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 271 s.v. kapsos\", \"stance\": \"partial\", \"note\": \"'kapsos, ā \\\"hold; holder\\\" … Gk. kápsa \\\"box, chest\\\"; Lat. capsus, -um \\\"stall, pen, coach-box\\\"; capsa (as Gk. LW?)' — Mann lists both but is unsure which borrowed from which.\"},\n  {\"src\": \"LKT\", \"where\": \"LKT.txt no. 993 'Ar. kafas'\", \"stance\": \"supports\", \"note\": \"'\\\"Käfig\\\" [über aram. kafsā aus gr. κάψα, lat. capsa]' — Lokotsch routes the Arabic word through Aramaic from Greek κάψα / Latin capsa, i.e. Nourai's next two boxes.\"},\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kap-\", \"stance\": \"partial\", \"note\": \"'III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSULE, CASE², CHASSIS' — Watkins knows the *kap-s- formation only in Latin, not in Greek.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 7, \"lang\": \"Arabic\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box: Arabic قفص (qafaṣ) / قفس (qafas) 'cage, coop'. It came in from Aramaic/Syriac ܩܘܦܣܐ qup̄sā, ܩܦܣܐ qap̄sā 'cage, box' — Addi Shir's entry cites the Syriac form and Fraenkel — which is in turn the Greek κάψα / Latin capsa, capsus of the previous box. The Iranian-style p of the Aramaic form is rendered by Arabic f, and the Greek/Latin -s- is written with ص in the classical orthography. Arabic lexicographers were themselves divided: al-Muḥīṭ (quoted by Addi Shir) reports 'قيل معرب وقيل عربي واشتقاقه من القفص بمعنى الجمع', and al-Unaysi flatly calls it 'عربي محض'; but the Greek-Latin source is now standard.\",\n \"derivation_fa\": \"این جعبه در کتاب خالی است و مقصود عربی قفص/قفس «قفس پرندگان» است. این واژه از آرامی/سریانی ܩܘܦܣܐ (qup̄sā) و ܩܦܣܐ (qap̄sā) «قفس، جعبه» به عربی رسیده — ادّی شیر همین صورت سریانی را می‌آورد و به فرنکل ارجاع می‌دهد — و آن خود همان κάψα یونانی و capsa/capsus لاتینی جعبهٔ پیشین است. پِ آرامی در عربی به ف بدل شده و س یونانی-لاتینی در املای کلاسیک با «ص» نوشته شده است. خودِ لغویان عرب دو دسته بوده‌اند: محیط المحیط (به نقل ادّی شیر) می‌گوید «قیل معرّب وقیل عربی واشتقاقه من القفص بمعنی الجمع» و العنیسی آن را «عربی محض» می‌خواند؛ اما امروز خاستگاه یونانی-لاتینی پذیرفتهٔ همگان است. ادعای نورایی درست است.\",\n \"sources\": [W_QAFAS],\n \"ref_check\": [\n  {\"ref\": \"MON:2700\", \"status\": \"supports\", \"note\": \"Mo'in s.v. قفس (MON_part2.txt): 'ققس: [- قفص، معر. صندوق، جعبه] (اِ.) آلتی است که از چوب، برنج، آهن و غیر آن سازند و دارای شبکه‌ها است و پرندگان وحشی را در آن نگاه دارند.' — Mo'in marks the Persian word as the Arabic معرّب and glosses the source sense as 'box, chest'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AFM\", \"where\": \"AFM.txt s.v. (القفص)\", \"stance\": \"supports\", \"note\": \"'( القفص ) وهو معروف قيل معرب وقيل عربي واشتقاقه من القفص بمعنى الجمع (محيط المحيط) … [Syriac] ܩܦܣܐ … (راجع فرنكل ص …)' — Addi Shir gives the Syriac qap̄sā and refers to Fraenkel.\"},\n  {\"src\": \"LKT\", \"where\": \"LKT.txt no. 993 'Ar. kafas'\", \"stance\": \"supports\", \"note\": \"'\\\"Käfig\\\" [über aram. kafsā aus gr. κάψα, lat. capsa], ebenso tk. kafes; hieraus rum. cafas, bulg. serb. kafez, sp. pg. alcahaz'\"},\n  {\"src\": \"TAD\", \"where\": \"TAD_pages.txt s.v. قفص\", \"stance\": \"partial\", \"note\": \"'قفص - عربي محض وقفس الفارسي التركي مأخوذ من قفص العربي … [Latin] معناها علبة وخزانة من خشب أما القفص فيونانية' — al-Unaysi records the Greek/Latin comparison but himself prefers a purely Arabic origin.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 8, \"lang\": \"Persian\", \"words\": \"qafas «قفس»\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"New Persian قفس (qafas) 'cage', an Arabic loan of the Islamic period taken over with the sīn spelling (Arabic ṣād regularly appears as س in Persian orthography of such words). Mo'in's footnote in Borhan-e Qate' says exactly what Nourai's chart draws: 'اصلاً یونانی است … در یونانی kapsa، لاتینی capsa بمعنی جعبه و صندوقچه است' — while noting that the author of the Farhang-e Tafsīr (تفس) refused the Greek etymology and held the word to be pure Arabic. From Persian and Arabic the word spread further (Ottoman Turkish kafes, Romanian cafas, Serbo-Croatian kafez).\",\n \"derivation_fa\": \"«قفس» در فارسی نو وام‌واژه‌ای عربی از دورهٔ اسلامی است که با املای «س» پذیرفته شده (صادِ عربی در چنین واژه‌هایی در فارسی معمولاً به «س» نوشته می‌شود). حاشیهٔ معین بر برهان قاطع دقیقاً همان چیزی را می‌گوید که نمودار نورایی نشان می‌دهد: «اصلاً یونانی است… در یونانی kapsa، لاتینی capsa بمعنی جعبه و صندوقچه است»، و می‌افزاید که مؤلف «تفس» این وجه اشتقاق را نپذیرفته و واژه را عربی محض دانسته است. از فارسی و عربی این واژه به ترکی عثمانی kafes، رومانیایی cafas و صربی kafez نیز رفته است. ادعای نورایی درست است.\",\n \"sources\": [W_QAFAS],\n \"ref_check\": [\n  {\"ref\": \"BQT:1534\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' s.v. قفس (vol 3, BQT_v3_pages.txt pdf leaf 327 ≈ printed p.1532-34): 'قفس = بفتح اول و ثانی بروزن هوس، معروف است و آن … شبکه‌دار که از چوب و برنج و آهن و امثال آن بافند و جانوران و حشر را در آن کنند و معرب آن قفص باشد صاد بی‌نقطه', with Mo'in's fn. 8: 'اصلاً یونانی است. (تقی‌زاده، یادگار …) در یونانی kapsa، لاتینی capsa بمعنی جعبه و صندوقچه است. مؤلف «تفس» این وجه اشتقاق را نمی‌پذیرد و کلمه را عربی محض می‌داند.'\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol 3, printed ~p.1532-34 s.v. قفس, Mo'in's fn. 8\", \"stance\": \"supports\", \"note\": \"'در یونانی kapsa، لاتینی capsa بمعنی جعبه و صندوقچه است'\"},\n  {\"src\": \"MON\", \"where\": \"s.v. قفس\", \"stance\": \"supports\", \"note\": \"'[- قفص، معر. صندوق، جعبه]'\"},\n  {\"src\": \"LKT\", \"where\": \"LKT.txt no. 993\", \"stance\": \"supports\", \"note\": \"'über aram. kafsā aus gr. κάψα, lat. capsa'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 9, \"lang\": \"Latin\", \"words\": \"capere : to take; capsa : case, box; for-ceps : fire tongs (☞Gwher)\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All three Latin items are correct and all three are in Pokorny's kap- article: 'Latin capiō, -ere, cēpī captus \\\"take\\\"'; 'capsa \\\"a repository, box, esp. for books, bookcase, satchel\\\"'; and the combining form -ceps '\\\"taker\\\"' (Watkins: 'Latin combining form -ceps (< *kap-s), \\\"taker\\\"'). Forceps is correctly cross-referenced to Gwher: it is formic-/for- 'hot' (PIE *gʷher-) + -ceps, so literally 'that which holds hot things' — Watkins says so verbatim under gʷher-: 'Latin forceps, pincers, fire tongs (< \\\"that which holds hot things\\\"; -ceps, agential suffix, \\\"-taker\\\"; see kap-)'. The one flaw is the citation: Pokorny p.524 carries kal-, kalni- and kam-er-, not kap-; the Latin material stands on pp.527-528, i.e. the same page Nourai gives for the root box.\",\n \"derivation_fa\": \"هر سه واژهٔ لاتینی درست است و هر سه در همان مدخل kap- پوکورنی آمده‌اند: «Latin capiō, -ere, cēpī captus \\\"take\\\"»؛ «capsa: مخزن و جعبه، به‌ویژه برای کتاب»؛ و جزء ترکیبی ‎-ceps‎ «گیرنده» (واتکینز: «صورت ترکیبی لاتینی ‎-ceps‎ ‏(< *kap-s) \\\"گیرنده\\\"»). ارجاع «forceps» به ریشهٔ Gwher نیز درست است: این واژه از for- «گرم» (هندواروپایی *gʷher-) و ‎-ceps‎ ساخته شده، یعنی «آنچه چیزهای داغ را می‌گیرد»؛ واتکینز ذیل *gʷher- عیناً همین را می‌نویسد. تنها ایراد، شمارهٔ ارجاع است: صفحهٔ ۵۲۴ پوکورنی به ریشه‌های kal-، kalni- و kam-er- می‌پردازد و مواد لاتینی مورد نظر در صفحهٔ ۵۲۷-۵۲۸ است، یعنی همان صفحه‌ای که نورایی برای خودِ ریشه آورده. جز این خطای ارجاع، ادعای نورایی درست است.\",\n \"sources\": [W_KAP],\n \"ref_check\": [\n  {\"ref\": \"POK:524\", \"status\": \"not_found\", \"note\": \"Checked POK_full.txt for 'Page(s): 524': it holds 'kal-' (Old Norse halr, OE hæleþ), 'kalni- \\\"narrow passage\\\" (Latin callis)' and 'kam-er- \\\"to bend, curve\\\"' — nothing about capere/capsa. Pokorny's Latin kap- material is on pp.527-528. Nourai's 524 is a slip for 527.\"}\n ],\n \"consulted\": [\n  {\"src\": \"POK\", \"where\": \"POK_full.txt, kap- article, p.527\", \"stance\": \"supports\", \"note\": \"'Latin capiō, -ere, cēpī captus \\\"take\\\", au-ceps, -cupare \\\"a bird-catcher, fowler\\\", parti-ceps … capsa \\\"a repository, box, esp. for books, bookcase, satchel\\\", capsus \\\"the carriage body; cage for wild animal\\\"'\"},\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kap- and s.v. gʷher-\", \"stance\": \"supports\", \"note\": \"kap-: '7. Latin combining form -ceps (< *kap-s), \\\"taker\\\"'; gʷher-: '4. O-grade form *gʷhor- in Latin forceps, pincers, fire tongs (< \\\"that which holds hot things\\\"; -ceps, agential suffix, \\\"-taker\\\"; see kap-): FORCEPS, FORCIPATE.'\"},\n  {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 342 ff. (Pokorny's reference for kap-)\", \"stance\": \"supports\", \"note\": \"cited by Pokorny as 'References: WP. I 342 ff., WH. I 159 f., 169' at the end of the kap- article, WH = Walde-Hofmann's Latin dictionary s.vv. capiō and capsa.\"},\n  {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 271 s.v. kapiō\", \"stance\": \"supports\", \"note\": \"'kapiō, kapmi \\\"take, seize, lift\\\". WP I, 342 … Lat. capio, -ere'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 10, \"lang\": \"French\", \"words\": \"\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Empty pass-through box standing for the French continuations of Latin capere and capsa: chasse 'frame, reliquary' and its derivative châssis 'framework', caisse/casse 'case', câble 'cable', capsule (a learned 16th-c. borrowing of Latin capsula), chasser 'to chase, catch' (< VLat. *captiāre), recevoir, décevoir (< L. recipere, decipere), cabestan 'capstan'. French is the correct intermediary for almost everything in the two boxes below it: Latin -pt- and -ps- went to Old French -ss-/-ch-, giving the doublets case/chase and capsa/châsse that English then borrowed twice over.\",\n \"derivation_fa\": \"این جعبه خالی است و نمایندهٔ بازماندگان فرانسوی capere و capsa لاتینی است: chasse «قاب، ضریح» و مشتق آن châssis «چارچوب»، caisse/casse «جعبه»، câble «کابل»، capsule (وام‌گیری عالمانه از capsula لاتینی در سدهٔ شانزدهم)، chasser «شکار کردن، گرفتن» (از لاتینی عامیانه *captiāre)، recevoir و décevoir (از recipere و decipere)، و cabestan. فرانسوی برای تقریباً همهٔ واژه‌های دو جعبهٔ زیرین واسطهٔ درستی است: خوشه‌های ‎-pt-‎ و ‎-ps-‎ لاتینی در فرانسویِ کهن به ‎-ss-/-ch-‎ بدل شدند و همین دوگانه‌های case/chase و capsa/châsse را پدید آورد که انگلیسی هر دو را جداگانه وام گرفت. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. chassis, capsule, cable, capstan\", \"stance\": \"supports\", \"note\": \"'chassis, n., framework. — F. châssis, \\\"frame, framework\\\", fr. chasse, \\\"frame\\\", fr. L. capsa, \\\"chest, box\\\"'; 'capstan, n. … — F. cabestan, fr. OProvenç. cabestan … fr. L. capistrare … fr. capere'\"},\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kap-\", \"stance\": \"supports\", \"note\": \"'III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE², CHASE², CHASE³, CHASSIS, CHESS²; ENCHASE' — all of these reached English through French.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 11, \"lang\": \"Persian\", \"words\": \"extra: کپسول ، کابل ، شاسی\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Three modern French technical loans in Persian, all of the late Qajar/Pahlavi period when French was the language of Iranian engineering and medicine: کپسول (kapsūl) < F. capsule (both the pharmaceutical capsule and the percussion cap of a rifle — Mo'in glosses it 'چاشنی تفنگ' as well as the botanical capsule); کابل (kābl) < F. câble 'insulated wire, underground/undersea cable' (Mo'in: 'مفتول فلزی لفاف‌دار و سیم زیرزمینی یا زیردریایی…', and کابل‌کشی is tagged [فر. ف.] = French + Persian); شاسی (šāsi) < F. châssis 'chassis'. All three preserve the French vowels and stress and none passed through Arabic, so the arrow French → Persian is exactly right.\",\n \"derivation_fa\": \"سه وام‌واژهٔ فنیِ فرانسوی در فارسی، همه از دورهٔ اواخر قاجار و پهلوی که زبان مهندسی و پزشکی ایران فرانسوی بود: «کپسول» از capsule فرانسوی (هم کپسول دارویی و هم چاشنی فشنگ؛ معین هر دو معنا را می‌آورد)، «کابل» از câble «سیم روکش‌دار زیرزمینی یا زیردریایی» (معین: «مفتول فلزی لفاف‌دار و سیم زیرزمینی یا زیردریایی…» و مدخل «کابل‌کشی» را با نشانهٔ [فر. ف.] یعنی فرانسوی + فارسی آورده)، و «شاسی» از châssis. هر سه واکه‌ها و تکیهٔ فرانسوی را نگاه داشته‌اند و هیچ‌یک از راه عربی نیامده‌اند؛ پس پیکان فرانسوی ← فارسی کاملاً درست است. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"MON:1997,2777,2896\", \"status\": \"supports\", \"note\": \"All three headwords are in Mo'in's Farhang (MON_part2.txt): 'کپسول: (اِ.) چاشنی تفنگ. (گیا.) گونه‌ای میوهٔ خشک شکوفا…'; 'کابل: (اِ.) مفتول فلزی لفاف‌دار و سیم زیرزمینی یا زیردریایی که جهت برق و تلفن و تلگراف بکار آید' with 'کابل‌کشی: [فر. ف.]'; شاسی is likewise a French loan in the same dictionary. The three page numbers cannot be checked against the 6-vol edition (no scan exists), but the entries are all present.\"}\n ],\n \"consulted\": [\n  {\"src\": \"MON\", \"where\": \"s.vv. کپسول, کابل, کابل‌کشی\", \"stance\": \"supports\", \"note\": \"'کابل‌کشی: [فر. ف.] (حامص.) کشیدن سیم‌های زیرزمینی یا زیر دریایی' — the [فر.] tag marks French origin.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. capsule, chassis, cable\", \"stance\": \"supports\", \"note\": \"'capsule, n. — L. capsula, \\\"a small box or chest\\\", dimin. of capsa'; 'chassis … F. châssis … fr. L. capsa'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 12, \"lang\": \"English\", \"words\": \"case, capsule, cable, chassis; catch, receive, deceive, forceps\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Seven of the eight are right, and right by this route. case (the box) < Old North French casse < Latin capsa; capsule < French capsule < L. capsula, dim. of capsa; chassis < F. châssis < chasse < L. capsa; catch < Old North French cachier < VLat. *captiāre, frequentative of capere; receive < ONFr. receivre < L. recipere; deceive < OFr. decevoir < L. decipere. All six are in Watkins' list under kap- II and III. Two qualifications. (a) cable: Klein derives it from 'F. câble, fr. Port. cable, which is a blend of Arab. ḥabl \\\"rope, cable\\\", and VLat. cap(u)lum, \\\"a halter for cattle\\\", fr. capiō' — so the chart's own NOTE ('See root \\\"Habl: rope\\\" for another possible root') is well taken, and modern opinion is genuinely split, with Watkins keeping cable under kap- and Klein making it a hybrid. (b) forceps did not come through French: it is a direct learned borrowing of Latin forceps into 17th-c. English scientific and surgical writing, and it belongs primarily under gʷher- 'to heat' with only its second element -ceps from kap-. Placing it under the French box is the node's one real error.\",\n \"derivation_fa\": \"از هشت واژهٔ این جعبه، شش تا کاملاً درست و از همین راه‌اند: case «جعبه» از فرانسویِ شمالیِ کهن casse از capsa لاتینی؛ capsule از capsule فرانسوی از capsula لاتینی؛ chassis از châssis؛ catch از cachier فرانسویِ شمالیِ کهن از *captiāre لاتینی عامیانه؛ receive از receivre از recipere؛ و deceive از decevoir از decipere. همهٔ اینها در فهرست واتکینز ذیل kap- آمده‌اند. اما دو نکته: نخست «cable» که کلاین آن را «آمیزه‌ای از حَبل عربی و cap(u)lum لاتینی عامیانه» می‌داند؛ پس یادداشت خود نورایی («برای cable ریشهٔ Habl را هم ببینید») بجاست و امروز هم آرا دوگانه است. دوم «forceps» که از راه فرانسوی نیامده، بلکه در سدهٔ هفدهم مستقیماً از لاتینی به زبان علمی و جراحی انگلیسی وارد شده و در اصل به ریشهٔ *gʷher- «گرم» تعلق دارد و تنها جزء دوم آن ‎-ceps‎ از kap- است؛ نهادن آن زیر جعبهٔ فرانسوی تنها خطای واقعی این جعبه است. روی هم رفته ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. kap-: 'II. Suffixed form *kap-yo- … 2. Latin capere, to take, seize, catch: CABLE, CAPABLE … CAPTURE, CATCH, (CHASE¹); ACCEPT … DECEIVE … RECEIVE'; 'III. Suffixed form *kap-s- in Latin capsa … CAPSULE, CASE², … CHASSIS'. FORCEPS is listed by Watkins under gʷher-, not kap-.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. cable, capsule, chassis\", \"stance\": \"partial\", \"note\": \"'cable, n. — ME. cable, cabel, kable, fr. F. câble, fr. Port. cable, which is a blend of Arab. ḥabl, \\\"rope, cable\\\", and VL. cap(u)lum, \\\"a halter for cattle\\\", fr. capiō, capere' — Klein splits cable between Semitic ḥabl and Latin capere, exactly the alternative Nourai's own NOTE points to.\"},\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt, index lines for CABLE, CASE², CAPSULE, CHASSIS, CATCH, RECEIVE, DECEIVE, FORCEPS\", \"stance\": \"partial\", \"note\": \"'CABLE kap-', 'CASE² kap-', 'CHASSIS kap-', 'CATCH kap-', 'DECEIVE kap-' — but 'FORCEPS' is indexed under gʷher- (with -ceps cross-referenced to kap-).\"},\n  {\"src\": \"SKT\", \"where\": \"SKT.txt, grep 'CASE (1)'\", \"stance\": \"silent\", \"note\": \"Skeat's Concise Dictionary OCR did not return the entry under the search patterns tried; no result either way.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 13, \"lang\": \"English\", \"words\": \"capstan, caption, captive, accept, except\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"All five go back to Latin capere and are so listed by Watkins: caption < L. captiō 'a taking'; captive < L. captīvus, from captus, the participle of capere; accept < L. acceptāre, frequentative of accipere (ad- + capere); except < L. excipere (ex- + capere). capstan is the one with a longer road — English took it from French cabestan, which is from Old Provençal cabestran, present participle of cabestrar 'to halter', from Latin capistrāre, from capistrum 'halter', itself from capere (Klein s.v. capstan) — but the ultimate Latin source is still capere, so the arrow from the Latin box is right, even if the box skips the Provençal/French stage.\",\n \"derivation_fa\": \"هر پنج واژه به capere لاتینی بازمی‌گردند و واتکینز همه را ذیل kap- آورده است: caption از captiō «گرفتن»؛ captive از captīvus (از captus، اسم مفعول capere)؛ accept از acceptāre، صورت مکرّرِ accipere (‏ad- + capere)؛ و except از excipere (‏ex- + capere). تنها capstan راه درازتری پیموده: انگلیسی آن را از cabestan فرانسوی گرفته، فرانسوی از cabestran پرووانسالیِ کهن (اسم فاعل cabestrar «افسار زدن») و آن از capistrāre لاتینی از capistrum «افسار» و سرانجام از capere (کلاین ذیل capstan). پس سرچشمهٔ لاتینی درست است و تنها منزل پرووانسالی/فرانسوی در نمودار نیامده. ادعای نورایی درست است.\",\n \"sources\": [],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. kap-: 'Latin capere, to take, seize, catch: … CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAPTOR, CAPTURE, CATCH …; ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT …' — all five of Nourai's words are in Watkins' list.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kap- and index lines 'ACCEPT kap-', 'ANTICIPATE kap-', 'CAPSTAN kap-', 'CAPTION kap-', 'CAPTIVE kap-'\", \"stance\": \"supports\", \"note\": \"index entries confirm each word individually.\"},\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.v. capstan\", \"stance\": \"partial\", \"note\": \"'capstan, n., a device for hauling up anchors. — F. cabestan, fr. OProvenç. cabestan, fr. cabestran, pres. part. used as a noun, fr. L. capistrāre, \\\"to tie with a halter\\\", fr. capistrum, \\\"halter\\\", fr. capere, \\\"to catch, seize, hold\\\"' — Latin ultimately, but through Provençal and French, not straight from Latin as the chart draws it.\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 14, \"lang\": \"Germanic\", \"words\": \"hâben : to have; hafigaz : containing something, heavy\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Both Germanic forms are taken verbatim from Watkins' kap- article, which reads '3. Form *kap-o- in Germanic *habai-, *habēn in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, \\\"containing something,\\\" having weight, in Old English hefig, heavy: HEAVY.' Nourai's 'hâben' is Watkins' *habēn (Proto-Germanic *habēną, the stative *-ē- verb), and 'hafigaz' is *hafigaz / *habīgaz, an adjective in *-iga- built on the verbal root, literally 'holding something'. Pokorny gives the same set: 'Gothic haban, -aiþ \\\"hold, stop, have\\\", Old Norse hafa, Old Saxon hebbian, Old English habban, Old High German habēn \\\"have\\\"; … Old English hefig, Old Saxon hebig, Old High German hebīc \\\"heavy\\\" (actually \\\"holding something\\\")'. The p ~ b/f alternation is Grimm's law plus Verner's law operating on PIE *kap-. The gloss 'containing something' is Watkins' own quotation marks.\",\n \"derivation_fa\": \"هر دو صورت ژرمنی عیناً از مدخل kap- واتکینز گرفته شده است: «صورت *kap-o- در ژرمنی *habai-، *habēn، در انگلیسی کهن habban \\\"داشتن، نگاه داشتن\\\"» و «ژرمنی hafigaz، \\\"دارندهٔ چیزی\\\"، یعنی سنگین، در انگلیسی کهن hefig». پس «hâben» نورایی همان *habēn (ژرمنی آغازین *habēną، فعل حالتیِ ‎-ē-‎) و «hafigaz» همان صفت ساخته‌شده با پسوند ‎*-iga-‎ بر همان ستاک است، تحت‌اللفظ «دارندهٔ چیزی». پوکورنی نیز همین مجموعه را می‌آورد: گوتی haban، نورس کهن hafa، ساکسون کهن hebbian، انگلیسی کهن habban، آلمانی علیای کهن habēn؛ و «انگلیسی کهن hefig … آلمانی علیای کهن hebīc \\\"سنگین\\\" (در اصل \\\"دارندهٔ چیزی\\\")». دگرگونی p هندواروپایی به f/b نتیجهٔ قانون گریم و قانون ورنر است. ادعای نورایی درست است.\",\n \"sources\": [W_KAP],\n \"ref_check\": [\n  {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt s.v. kap-: '3. Form *kap-o- in Germanic *habai-, *habēn in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, \\\"containing something,\\\" having weight, in Old English hefig, heavy: HEAVY.' — Nourai's two forms and both glosses come straight from here.\"}\n ],\n \"consulted\": [\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kap-, sections I.3 and I.4\", \"stance\": \"supports\", \"note\": \"'Germanic hafigaz, \\\"containing something,\\\" having weight'\"},\n  {\"src\": \"POK\", \"where\": \"POK_full.txt, kap- article p.527-528\", \"stance\": \"supports\", \"note\": \"'Gothic haban, -aiþ \\\"hold, stop, have\\\", Old Norse hafa, Old Saxon hebbian, Old English habban, Old High German habēn \\\"have\\\"; … Old English hefig, Old Saxon hebig, Old High German hebīc \\\"heavy\\\" (actually \\\"holding something\\\")'\"},\n  {\"src\": \"IEC\", \"where\": \"IEC.txt leaf 271 s.v. kapiō\", \"stance\": \"supports\", \"note\": \"'Go. hafjan \\\"raise, heave\\\"; MHG haben, hān (1) \\\"hold\\\", beside heben, MLG heven \\\"raise; begin\\\"'\"}\n ]\n})\n\ne1[\"nodes\"].append({\n \"id\": 15, \"lang\": \"English\", \"words\": \"have, heavy\",\n \"verdict\": \"confirmed\",\n \"derivation\": \"Modern English have < Middle English habben, haven < Old English habban 'to hold, possess, have' < Proto-Germanic *habjaną/*habēną; heavy < ME hevy < OE hefig < PGmc *hafigaz, literally 'holding (something)', hence 'weighty'. Klein s.v. have gives the whole Germanic family (ON hafa, OS hebbjan, OFris. habba, OHG haben, Goth. haban) 'fr. Teut. base *haf-, \\\"to hold, have\\\"', and s.v. heavy relates OE hefig to OE hefe 'weight' and hebban 'to lift'. Note that English have is NOT related to Latin habēre despite the resemblance — that is under PIE *gʰabʰ- (Watkins ghabh-) — a trap Nourai avoids by putting have under kap-.\",\n \"derivation_fa\": \"انگلیسی امروزین have از انگلیسی میانهٔ habben/haven و آن از انگلیسی کهن habban «داشتن، نگاه داشتن» از ژرمنی آغازین *habjaną/*habēną؛ و heavy از انگلیسی میانهٔ hevy و انگلیسی کهن hefig از ژرمنی *hafigaz، تحت‌اللفظ «دارندهٔ چیزی» و از آنجا «سنگین». کلاین ذیل have تمام خانوادهٔ ژرمنی را می‌آورد (نورس کهن hafa، ساکسون کهن hebbjan، فریزی کهن habba، آلمانی علیای کهن haben، گوتی haban) «از ستاک ژرمنی *haf- \\\"نگاه داشتن، داشتن\\\"» و ذیل heavy، hefig را با hefe «وزن» و hebban «بلند کردن» می‌سنجد. نکتهٔ مهم آنکه have انگلیسی با habēre لاتینی هم‌ریشه نیست — با آنکه شبیه‌اند — و habēre به ریشهٔ *gʰabʰ- تعلق دارد؛ نورایی درست از این دام پرهیز کرده و have را ذیل kap- آورده است. ادعای نورایی درست است.\",\n \"sources\": [W_KAP],\n \"ref_check\": [\n  {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"Nourai gives no reference for this box; it inherits the AHD citation of the parent Germanic box.\"}\n ],\n \"consulted\": [\n  {\"src\": \"KLN\", \"where\": \"KLN_1966.txt s.vv. have, heavy\", \"stance\": \"supports\", \"note\": \"'have, tr. v. — ME. habben, haven, fr. OE. habban, \\\"to hold, possess, have\\\", rel. to ON. hafa, OS. hebbjan, OFris. habba, hebba, OHG. haben, MHG., G. haben, Goth. haban … fr. Teut. base *haf-, \\\"to hold, have\\\"'; 'heavy, adj. — ME. hevy, fr. OE. hefig, rel. to OS. hefiig, OHG. hebig, hevig … and to OE. hefe, \\\"weight\\\", hebban, \\\"to lift, raise\\\"'\"},\n  {\"src\": \"AHD\", \"where\": \"AHD_watkins1985.txt s.v. kap-\", \"stance\": \"supports\", \"note\": \"'…in Old English habban, to have, hold: HAVE'; '…in Old English hefig, heavy: HEAVY'. The index lines read 'HAVE kap-' and 'HEAVY kap-'. Watkins keeps Latin habēre separate under ghabh- ('Compare kap-').\"}\n ]\n})\n\ndoc[\"entries\"].append(e1)\n\n# ------------------------------------------------------------------ entry 2\ne2 = {\n \"entry\": 2,\n \"root\": \"Kapastay, Kapasti\",\n \"verdict\": \"plausible\",\n \"modern_form\": \"Avestan kapastay- / kapasti- f., name of an epidemic disease (Bartholomae); traditionally rendered 'poison, colocynth' after NP kabast\",\n \"note\": \"The two forms are real and are Bartholomae's own citation forms, but two things in the box need correction. (1) The language label 'Old Persian / Avestan' should be Avestan alone: the word occurs in Yašt 8.56 and Vidēvdād 11.9 (kapastiš); there is no Old Persian attestation, and Kent's lexicon has none. (2) The gloss is the disputed part. Bartholomae (AiW col. 436) heads the entry 'kapastay- f. Name einer infektiösen, zu Kriegszeiten auftretenden Krankheit' and adds in the footnote: 'Man setzt wegen np. kabast \\\"Koloquinte\\\" die Bedeutung \\\"Gift\\\" oder \\\"plante vénéneuse\\\" an, was mir nicht zu passen scheint' — i.e. the sense 'poison / poisonous plant' that Nourai prints is precisely the one Bartholomae rejects as a back-projection from the New Persian word. Horn agrees the Avestan meaning is 'ganz unsicher' (citing Geldner). Wiktionary today calls the whole etymology of کبست 'Unknown' and the link to Av. kapastiš 'dubious', mentioning Lagarde's alternative (a derivative of Old Armenian kapem 'to bind', the colocynth being a creeper) and a possible MP kawastīg in the Greater Bundahišn. So the chain is a long-standing scholarly guess that is still current in Persian lexicography (Mo'in prints it), but it is not established.\",\n \"note_fa\": \"هر دو صورتی که نورایی آورده واقعی‌اند و همان صورت‌های استنادی بارتولومه‌اند، اما دو نکته باید اصلاح شود. نخست، برچسب «پارسی باستان / اوستایی» باید تنها «اوستایی» باشد: این واژه در یشت ۸ بند ۵۶ و وندیداد ۱۱ بند ۹ (kapastiš) آمده و هیچ گواهی پارسی باستان ندارد؛ در واژه‌نامهٔ کنت هم نیست. دوم، معنا محل نزاع است: بارتولومه در ستون ۴۳۶ فرهنگ ایرانی باستان مدخل را چنین می‌آورد: «kapastay- مؤنث، نام بیماری واگیردار که در روزگار جنگ پدید می‌آید» و در پانوشت می‌افزاید که معنی «زهر» یا «گیاه زهرآگین» را «به سبب کبستِ فارسی نو» به آن داده‌اند و «به نظر من مناسب نمی‌نماید». هرن نیز معنی واژهٔ اوستایی را «کاملاً نامطمئن» می‌خواند. ویکی‌واژه امروز ریشهٔ «کبست» را «ناشناخته» می‌داند و پیوند آن با kapastiš اوستایی را «مشکوک» می‌شمارد و به فرضیهٔ لاگارد (مشتق از kapem ارمنی کهن به معنی «بستن»، چون کبست گیاهی رونده است) اشاره می‌کند. پس این زنجیره حدسی دیرین است که در فرهنگ‌نویسی فارسی (از جمله در حواشی معین) هنوز نقل می‌شود، اما اثبات‌شده نیست؛ ادعای نورایی با احتیاط پذیرفتنی است.\",\n \"sources\": [W_KABAST],\n \"ref_check\": [\n  {\"ref\": \"BRT:436\", \"status\": \"partial\", \"note\": \"Bartholomae, Altiranisches Wörterbuch col. 436 (BRT.txt line 9027, leaf 266): 'kapastay- f. Name einer infektiösen, zu Kriegszeiten auftretenden Krankheit: … pāma nōit ˟is Yt. 8.56; — pama mūiš …is V.11.9.' Footnote: 'Man setzt wegen np. kabast \\\"Koloquinte\\\" die Bedeutung \\\"Gift\\\" oder \\\"plante vénéneuse\\\" an, was mir nicht zu passen scheint. Eher ka-pasti- …' — the page number is right and the forms are right, but Bartholomae's gloss is a disease name and he explicitly disputes Nourai's 'poison'. He also gives the word as Avestan (Yašt, Vidēvdād), not Old Persian.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BRT\", \"where\": \"AiW col. 436 s.v. kapastay-\", \"stance\": \"partial\", \"note\": \"'Name einer infektiösen, zu Kriegszeiten auftretenden Krankheit' + footnote rejecting 'Gift'.\"},\n  {\"src\": \"HRN\", \"where\": \"HRN.txt p.187, no. 840a\", \"stance\": \"partial\", \"note\": \"'aw. kapasti- (Spiegel, zuletzt Ar. Periode 46); phlv. kapast (Bund.). Die Bedeutung des aw. Wortes ist ganz unsicher (vergl. Geldner, 5 Yasht, 77)'\"},\n  {\"src\": \"KNT\", \"where\": \"KNT.txt, grep 'kapast'\", \"stance\": \"silent\", \"note\": \"no Old Persian kapasta-; confirms that the 'Old Persian' half of Nourai's language label has no support.\"},\n  {\"src\": \"AVG\", \"where\": \"AVG.txt (Jackson, Avesta Grammar)\", \"stance\": \"silent\", \"note\": \"grammar, not lexicon; no entry for the word.\"}\n ],\n \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n \"id\": 1, \"lang\": \"Pahlavi\", \"words\": \"kapast\",\n \"verdict\": \"plausible\",\n \"derivation\": \"Middle Persian kapast, cited by Horn from the Bundahišn ('phlv. kapast (Bund.)') as the link between Avestan kapasti- and New Persian kabast; the Avestan -ay-/-i- stem simply loses its ending in Middle Persian, giving a consonant-final kapast with no other change. Mo'in repeats the form in his footnote to Borhan-e Qate' ('پهلوی kapast'). The reservation is that the Pahlavi attestation is not secure: MacKenzie's Concise Pahlavi Dictionary has no kapast, and Wiktionary reports that what the Greater Bundahišn actually has may be kawastīg, a flowering plant, so that the Pahlavi step is 'questionable if attested'. The step is therefore reasonable but resting on a single, contested passage.\",\n \"derivation_fa\": \"فارسی میانه kapast که هرن آن را از بندهش نقل می‌کند («phlv. kapast (Bund.)») و حلقهٔ واسط میان kapasti- اوستایی و «کبست» فارسی نو می‌شمارد؛ ستاک اوستایی در فارسی میانه پایانهٔ خود را از دست می‌دهد و kapastِ پایان‌بسته می‌ماند، بی هیچ دگرگونی دیگر. معین نیز در حاشیهٔ برهان قاطع همین صورت را می‌آورد: «پهلوی kapast». اما گواهی پهلوی استوار نیست: در فرهنگ کوچک پهلوی مکنزی مدخل kapast نیامده و ویکی‌واژه یادآور می‌شود که آنچه در بندهش بزرگ آمده شاید kawastīg (نام گیاهی گلدار) باشد؛ پس این پله بر یک شاهدِ تنها و مورد مناقشه استوار است. ادعا با احتیاط پذیرفتنی است.\",\n \"sources\": [W_KABAST],\n \"ref_check\": [\n  {\"ref\": \"HRN:187\", \"status\": \"supports\", \"note\": \"Horn, Grundriss p.187 no. 840a (HRN.txt leaf 209): '840ᵃ kebest, kebestū, kebeste, kewest, [Hebrew-script form] (Jer. 8, 14) \\\"Koloquinthe; Gift, Aristolochia(?)\\\". aw. kapasti- (Spiegel, zuletzt Ar. Periode 46); phlv. kapast (Bund.). Die Bedeutung des aw. Wortes ist ganz unsicher…' — Nourai's Pahlavi form and the page are exactly Horn's.\"}\n ],\n \"consulted\": [\n  {\"src\": \"HRN\", \"where\": \"p.187 no. 840a\", \"stance\": \"supports\", \"note\": \"'phlv. kapast (Bund.)'\"},\n  {\"src\": \"PHD\", \"where\": \"PHD.txt / PHD_mackenzie.txt, grep 'kapast|kabast'\", \"stance\": \"silent\", \"note\": \"MacKenzie's Concise Pahlavi Dictionary has no kapast — the word is not in his corpus.\"},\n  {\"src\": \"NYB\", \"where\": \"NYB_vol2_glossary.txt, grep 'kapast'\", \"stance\": \"silent\", \"note\": \"Nyberg's glossary likewise has no entry.\"},\n  {\"src\": \"BQT\", \"where\": \"vol 3, Mo'in's fn. to کبست (pdf leaf 381 ≈ printed p.1586-88)\", \"stance\": \"supports\", \"note\": \"'اوستا kapasti، پهلوی kapast «[اساس اشتقاق] ۸۵۰…»' — Mo'in gives the same Avestan and Pahlavi forms, citing Horn's paragraph number.\"}\n ]\n})\n\ne2[\"nodes\"].append({\n \"id\": 2, \"lang\": \"Persian\", \"words\": \"kabast «کَبست»; extra: کَبستو\",\n \"verdict\": \"plausible\",\n \"derivation\": \"New Persian کبست (kabast), also کبستو (kabastū) and کبسته (kabaste), is unquestionably a real word: Borhan-e Qate' defines it as 'رستنیی باشد تلخ شبیه به دستنبوی که بعربی حنظل و بفارسی خربزهٔ تلخ گویند' — the colocynth, Citrullus colocynthis — and adds that 'زهرِ مهلک را نیز کبست گویند', which is the 'poison' sense of Nourai's gloss. Ferdowsi's line quoted on the page ('چرا کشت باید درختی بدست ـ که بارش بود زهر و بیخش کبست') uses it exactly so. Phonetically the descent from MP kapast is regular: intervocalic p is voiced to b (kapast > kabast), and کبستو adds the common Persian plant-name extension -ū. What is only plausible, not confirmed, is the ultimate ancestry: Horn calls the Avestan meaning 'ganz unsicher', Bartholomae rejects the equation, and Wiktionary marks the etymology of کبست 'Unknown', noting Lagarde's alternative derivation from Old Armenian kapem 'to bind' (colocynth is a creeping vine). So the word and its meaning are confirmed; the arrow above it is the uncertain part.\",\n \"derivation_fa\": \"«کَبست» در فارسی نو، و گونه‌های «کبستو» و «کبسته»، واژه‌ای است کاملاً اصیل: برهان قاطع آن را چنین تعریف می‌کند: «رستنیی باشد تلخ شبیه به دستنبوی که بعربی حنظل و بفارسی خربزهٔ تلخ گویند»، یعنی هندوانهٔ ابوجهل (Citrullus colocynthis)، و می‌افزاید «زهرِ مهلک را نیز کبست گویند» — همان معنایی که نورایی آورده. بیت فردوسی در همین صفحه («چرا کشت باید درختی بدست ـ که بارش بود زهر و بیخش کبست») دقیقاً در همین معناست. از نظر آوایی، تحول از kapast فارسی میانه قاعده‌مند است: پِ میان دو واکه واک‌دار شده و به ب بدل گشته (kapast > kabast)، و «کبستو» با پسوند ‎-و‎ ساخته شده که در نام گیاهان فارسی فراوان است. آنچه تنها «پذیرفتنی با احتیاط» است نه قطعی، تبار دورتر واژه است: هرن معنی صورت اوستایی را «کاملاً نامطمئن» می‌داند، بارتولومه این برابرنهاد را رد می‌کند و ویکی‌واژه ریشهٔ کبست را «ناشناخته» می‌شمارد و از فرضیهٔ لاگارد (از kapem ارمنی کهن «بستن») یاد می‌کند. پس خودِ واژه و معنایش تأییدشده است و تنها پیکانِ بالای آن نامطمئن.\",\n \"sources\": [W_KABAST],\n \"ref_check\": [\n  {\"ref\": \"BQT:1588\", \"status\": \"supports\", \"note\": \"Borhan-e Qate' s.v. کبست (vol 3 scan, BQT_v3_pages.txt pdf leaf 381 ≈ printed p.1586-88): 'کبست: بفتح اول و ثانی … رستنیی باشد تلخ شبیه بدستنبوی که بعربی حنظل و بفارسی خربزه‌تلخ گویند … و بعضی گویند کبست غیر حنظل است و آن گیاهی باشد بغایت تلخ، و زهر مهلک را نیز کبست گویند'; the adjacent headword 'کبستو = بر وزن ارسطو، بمعنی … زهر … و حنظل است' is Nourai's extra form; Mo'in's footnote: 'کبست نام فارسی حنظل است «[فولرس]… عقار ۱۵۸» … اوستا kapasti، پهلوی kapast «[اساس اشتقاق] ۸۵۰»'.\"}\n ],\n \"consulted\": [\n  {\"src\": \"BQT\", \"where\": \"vol 3, printed ~p.1586-88 s.vv. کبست, کبستو, کبسته + Mo'in's footnotes\", \"stance\": \"supports\", \"note\": \"'کبست نام فارسی حنظل است … اوستا kapasti، پهلوی kapast'\"},\n  {\"src\": \"MON\", \"where\": \"MON_part2.txt, list of synonyms for حنظل\", \"stance\": \"supports\", \"note\": \"Mo'in lists 'کبست، کبسته، … کبستو، … خربزهٔ تلخ' among the names of حنظل (colocynth), confirming both the headword and Nourai's extra form کبستو.\"},\n  {\"src\": \"HRN\", \"where\": \"p.187 no. 840a\", \"stance\": \"supports\", \"note\": \"'kebest, kebestū, kebeste, kewest … \\\"Koloquinthe; Gift, Aristolochia(?)\\\"' — Horn has both کبست and کبستو and both senses Nourai gives.\"},\n  {\"src\": \"ARY\", \"where\": \"ARY_pages.txt / ARY_latin_index_pages.txt, grep 'کبست'\", \"stance\": \"silent\", \"note\": \"Aryanpur's Indo-European roots dictionary does not treat کبست (it is not derived from an IE root in his scheme).\"}\n ]\n})\n\ndoc[\"entries\"].append(e2)\n\nout = \"/home/sfmqrb/git/rishe/data/verification/page-240.json\"\nwith open(out, \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\", out)\nPYEOF\npython3 \"/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/mk240.py\"",
 "description": "Write page-240 verification JSON"
}
```


### [2026-09-06T16:03:51.637Z] TOOL RESULT

```
written /home/sfmqrb/git/rishe/data/verification/page-240.json
```


## [2026-09-06T16:03:56.351Z] TOOL CALL #64: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-240.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 240",
 "description": "Validate and run verify_check"
}
```


### [2026-09-06T16:03:58.541Z] TOOL RESULT

```
JSON OK
nodes verified: 20/20
node verdicts: {'confirmed': 14, 'disputed': 1, 'plausible': 5}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 18, 'partial': 1, 'not_found': 2, 'not_checked': 3}
books consulted: {'supports': 42, 'silent': 13, 'contradicts': 2, 'partial': 9} | by book: {'BQT': 7, 'KLN': 7, 'AHD': 7, 'MON': 6, 'LKT': 6, 'HRN': 5, 'PHD': 4, 'IEC': 4, 'POK': 4, 'HUB': 3, 'AFM': 2, 'ARY': 2, 'KNT': 2, 'CHEUNG': 2, 'NYB': 2, 'TAD': 1, 'WLD': 1, 'SKT': 1}
```


## [2026-09-06T16:04:19.575Z] AGENT

0 PROBLEM lines. Page 240 (book p. 210) verified — 3 entries, 20 nodes.

**Verdicts:** nodes — 14 confirmed, 5 plausible, 1 disputed; roots — 2 confirmed (Kânŭnu, Kap/Qap), 1 plausible (Kapastay).

**Disputed**
- *Kap* #1 **Old Persian "čifsati"** — no such verb in the Old Persian corpus (Kent silent). Nourai copied it from Aryanpur's IE-roots index (ARY printed p.223, which lists "ČIFSATI :(OLD PERSIAN)"). Horn 441 and Cheung reconstruct an Old/Proto-Iranian *čap-/*čap-s-, not an Old Persian *čifsati.

**Plausible (with the reason)**
- *Kap* #2 časbīdan — Pokorny p.527 does print "npers. časpīdan, čapsīdan, čafsīdan" and Horn 441 links it to Lat. capiō, but Mann and Cheung both flag that PIE *k before *a should not palatalize (č- unexplained).
- *Kap* #6 Greek kapsa — real word, but a loan **from** Latin capsa/capsus (Pokorny says so in the same article); the arrow straight from PIE bypasses Latin.
- *Kap* #12 English box — six of eight fine; *cable* is a Latin/Arabic ḥabl hybrid per Klein (Nourai's own NOTE anticipates this), and *forceps* is a direct 17th-c. Latin borrowing, not French, and belongs under gʷher-.
- *Kapastay* root + both nodes — Bartholomae (AiW 436) glosses Av. kapastay- as an epidemic-disease name and **explicitly rejects** the sense "poison/poisonous plant" as back-projected from NP kabast; Horn calls the Avestan meaning "ganz unsicher"; Wiktionary now marks کبست "Unknown", MP kapast questionably attested (possibly kawastīg). Also the language label should be Avestan alone — there is no Old Persian attestation.

**Bad reference (book error, not extraction)**
- *Kap* #9 Latin cites **POK:524**, which in Pokorny holds kal-/kalni-/kam-er-; capere/capsa are on 527-528. Slip for 527.
- *Kap* #2 cites **IEC:473**, which falls among Mann's i- entries; the supporting article (kapsō, with "Per. cf. časpam") is at ~p.510-512.
- *Kap* #1 cites BQT:636; Borhan's چسبیدن is on printed p.634 (Mo'in's footnote gives an *Iranian* root, no Old Persian form).

**Extraction errors: none.** I rendered the printed page (copied to `data/verification/sources/refs/ocr/BOOK/240.png`) and the JSON is faithful throughout, including "čifsati", "POK:524", "hâben/hafigaz" and all Persian script extras. The only in-book typo is the gloss "hart" for "hearth" on kânŭn.

Best confirmations found: Hübschmann p.89 (add. to no. 875) gives the whole kapithē → phl. kapīč → np. kavīz/kavīž → Arab. qafīz chain verbatim; Mo'in's Borhan footnote and his Farhang tag `[ع. سر. از اکدی]` give the Akkadian → Syriac → Arabic → Persian route for کانون exactly as drawn.

Files: `/home/sfmqrb/git/rishe/data/verification/page-240.json`; 7 web sources archived via `fetch_source.py`.
