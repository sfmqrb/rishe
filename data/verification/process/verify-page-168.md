# Verification process log — verify-page-168


## [2026-09-05T20:36:39.990Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 168 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-168.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-168.json. Write /home/sfmqrb/git/rishe/data/verification/page-168.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 168` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-05T20:36:41.802Z] AGENT

I'll start by reading the instructions.


## [2026-09-05T20:36:42.512Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-05T20:36:42.525Z] TOOL RESULT

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


## [2026-09-05T20:36:42.727Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-168.txt"
}
```


### [2026-09-05T20:36:42.742Z] TOOL RESULT

```
1	=== PDF page 168 (book page 138) ===
2	--- entry 0 ---
3	ROOT Gargelos -> redirect to Gwer 3
4	--- entry 1 ---
5	ROOT [Akkadian] Gassu : mortar  (refs HRN:199)
6	#1 (parent #0) [Avestan] refs=HRN:199 | vîčiča : mortar, gypsum
7	  #2 (parent #1) [Old Persian] refs=HRN:199 | gač : chalk | NOTE: MON and HUB:90 derive this word from Arabic word "jass" which is derived from the same Akkadian root.
8	    #3 (parent #2) [Persian] refs=SNS:310 | gač «گچ» : chalk
9	#4 (parent #0) [Greek] refs=AHD:588; AKD:32 | gupsos : gypsum
10	  #5 (parent #4) [Arabic] refs=BQT:1776; TAD:20 | jabsîn, jass, jafsîn : chalk
11	    #6 (parent #5) [Persian] refs=BQT | jabsîn «جبسین» : chalk
12	  #7 (parent #4) [Latin] refs=AHD | gypsum
13	    #8 (parent #7) [English] refs=None | gypsum
14	--- entry 2 ---
15	ROOT [Indo-European] Ğaulos : vessel, boat  (refs IEC:388)
16	#1 (parent #0) [Persian] refs=AEC:388; BQT:1044 | zowraq «زورق» : boat ; zowraqî «زورقی» : a boat-shaped hat
17	#2 (parent #0) [Greek] refs=AHD:539; IEC:388 | gaulos, galea : merchant ship
18	  #3 (parent #2) [Latin] refs=AHD:539 | galeota, galea : ship
19	    #4 (parent #3) [English] refs=AHD:539 | galleon, galiot, galliot, galley
20	--- entry 3 ---
21	ROOT Gě -> redirect to Gěi
22	--- entry 4 ---
23	ROOT Gebh -> redirect to Geph
24	--- entry 5 ---
25	ROOT [Indo-European] Gěi, Gě, Gî : to sing, song  (refs POK:355)
26	#1 (parent #0) [Avestan] refs=POK:355; KLN:169 | gâ 1 : to sing ; gâtâ : song, religious hymn
27	  #2 (parent #1) [Persian] refs=MON6:1648; MON:3190; KLN:169 | gât «گات ( گاتها )» : Zoroastrian religious songs ; gâh 1 «گاه۱ ( سه گاه ، چهارگاه )» : music, tune
28	#3 (parent #0) [Sanskrit] refs=POK:355 | gâ : to sing ; gâyatî : sings ; bhagavant-gita : sound of sublime ☞Bhag
29	  #4 (parent #3) [Old Persian] refs=MON:4878 | niğây : praise
30	    #5 (parent #4) [Pahlavi] refs=MON:4878 | niğâyišn : praise
31	      #6 (parent #5) [Persian] refs=BQT:2224 | nîyâyeš «نیایش» : praise
32	  #7 (parent #3) [English] refs=KLN:169 | Bhagavad-Gita
33	
```


## [2026-09-05T20:36:46.019Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-168.json",
 "description": "Read source JSON for page 168"
}
```


### [2026-09-05T20:36:46.058Z] TOOL RESULT

```
{
  "pdf_page": 168,
  "book_page": 138,
  "entries": [
    {
      "root": {
        "name": "Gargelos",
        "redirect": "Gwer 3"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gassu",
        "lang": "Akkadian",
        "refs": "HRN:199",
        "gloss": "mortar",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "HRN:199",
          "words": [
            {
              "translit": "vîčiča",
              "gloss": "mortar, gypsum",
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
          "lang": "Old Persian",
          "refs": "HRN:199",
          "words": [
            {
              "translit": "gač",
              "gloss": "chalk",
              "script": null
            }
          ],
          "script_extra": null,
          "note": "MON and HUB:90 derive this word from Arabic word \"jass\" which is derived from the same Akkadian root.",
          "quote": null
        },
        {
          "id": 3,
          "parent": 2,
          "lang": "Persian",
          "refs": "SNS:310",
          "words": [
            {
              "translit": "gač",
              "gloss": "chalk",
              "script": "گچ"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": {
            "text": "به سنگ و به گچ دیو دیوار کرد - نخست از برش هندسی کار کرد",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:588; AKD:32",
          "words": [
            {
              "translit": "gupsos",
              "gloss": "gypsum",
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
          "lang": "Arabic",
          "refs": "BQT:1776; TAD:20",
          "words": [
            {
              "translit": "jabsîn, jass, jafsîn",
              "gloss": "chalk",
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
          "lang": "Persian",
          "refs": "BQT",
          "words": [
            {
              "translit": "jabsîn",
              "gloss": "chalk",
              "script": "جبسین"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 4,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {
              "translit": "gypsum",
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
          "parent": 7,
          "lang": "English",
          "refs": null,
          "words": [
            {
              "translit": "gypsum",
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
        "name": "Ğaulos",
        "lang": "Indo-European",
        "refs": "IEC:388",
        "gloss": "vessel, boat",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Persian",
          "refs": "AEC:388; BQT:1044",
          "words": [
            {
              "translit": "zowraq",
              "gloss": "boat",
              "script": "زورق"
            },
            {
              "translit": "zowraqî",
              "gloss": "a boat-shaped hat",
              "script": "زورقی"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD:539; IEC:388",
          "words": [
            {
              "translit": "gaulos, galea",
              "gloss": "merchant ship",
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
          "lang": "Latin",
          "refs": "AHD:539",
          "words": [
            {
              "translit": "galeota, galea",
              "gloss": "ship",
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
          "lang": "English",
          "refs": "AHD:539",
          "words": [
            {
              "translit": "galleon, galiot, galliot, galley",
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
        "name": "Gě",
        "redirect": "Gěi"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gebh",
        "redirect": "Geph"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Gěi, Gě, Gî",
        "lang": "Indo-European",
        "refs": "POK:355",
        "gloss": "to sing, song",
        "note": null
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:355; KLN:169",
          "words": [
            {
              "translit": "gâ 1",
              "gloss": "to sing",
              "script": null
            },
            {
              "translit": "gâtâ",
              "gloss": "song, religious hymn",
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
          "refs": "MON6:1648; MON:3190; KLN:169",
          "words": [
            {
              "translit": "gât",
              "gloss": "Zoroastrian religious songs",
              "script": "گات ( گاتها )"
            },
            {
              "translit": "gâh 1",
              "gloss": "music, tune",
              "script": "گاه۱ ( سه گاه ، چهارگاه )"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:355",
          "words": [
            {
              "translit": "gâ",
              "gloss": "to sing",
              "script": null
            },
            {
              "translit": "gâyatî",
              "gloss": "sings",
              "script": null
            },
            {
              "translit": "bhagavant-gita",
              "gloss": "sound of sublime",
              "script": null,
              "see": ["Bhag"]
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Old Persian",
          "refs": "MON:4878",
          "words": [
            {
              "translit": "niğây",
              "gloss": "praise",
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
          "lang": "Pahlavi",
          "refs": "MON:4878",
          "words": [
            {
              "translit": "niğâyišn",
              "gloss": "praise",
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
          "lang": "Persian",
          "refs": "BQT:2224",
          "words": [
            {
              "translit": "nîyâyeš",
              "gloss": "praise",
              "script": "نیایش"
            }
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:169",
          "words": [
            {
              "translit": "Bhagavad-Gita",
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


## [2026-09-05T20:36:46.793Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-05T20:36:46.838Z] TOOL RESULT

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


## [2026-09-05T20:36:53.072Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['HRN','SNS','AHD','AKD','BQT','TAD','IEC','AEC','POK','KLN','MON','HUB','BRT','KNT','PHD','NYB','WLD','SYN','SKT','ARY','FVQ','AFM','PLA','LKT','LEW','LAT','FSD','WEB','AFA','ARB','SIN','RCH','DEV','PHN']:\n    v=d.get(k)\n    print(k, json.dumps(v,ensure_ascii=False)[:600] if v else 'MISSING')\n    print()\n\""
}
```


### [2026-09-05T20:37:30.819Z] TOOL RESULT

```
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries 

SNS {"title": "Mahmoud Tavoosi, Vazhe-name-ye Shayast ne Shayast (A Glossary of Shayast ne Shayast), Shiraz University 1365/1986", "kind": "archive_djvu", "url": "https://archive.org/details/VajnameShayest", "lookup_hint": "grep the Pahlavi transliteration (Latin) in SNS_pages.txt / SNS.txt, e.g. 'xist', 'ahyō'; page images at https://archive.org/details/VajnameShayest/page/n<leaf>. Use the inside.php search (see BQT) for better hit-to-leaf mapping.", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SNS.txt

AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr,

AKD {"title": "H. Zimmern, Akkadische Fremdwörter als Beweis für babylonischen Kultureinfluss, Leipzig 1917 (2nd ed.)", "edition_found": "1915 first edition (1917 is the 2nd, enlarged ed.; pagination may differ slightly)", "kind": "archive_djvu", "url": "https://archive.org/details/akkadischefremdw00zimmuoft", "identifier": "akkadischefremdw00zimmuoft", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AKD.txt", "page_offset": "leaf = printed + 8 (e.g. leaf 21 = p.13). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://

BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118

TAD {"title": "Tobia al-Unaysi (طوبيا العنيسي), Tafsir al-alfaz al-dakhila fi al-lugha al-'arabiyya ma'a dhikr asliha bi-hurufihi (2nd ed. Cairo 1932, ed. Yusuf Tuma al-Bustani; later Library of Lebanon reprint) — Nourai lists it under Arabic authors ('Unaysi T.'); its Table IV line was lost in the OCR", "kind": "archive_djvu", "url": "https://archive.org/details/TOB1932ARAR (1932 ed.); also https://archive.org/details/ar113lang79 and https://archive.org/details/elshandawily14640", "lookup_hint": "Alphabetical Arabic headwords; grep the Arabic headword in TAD_pages.txt (86 leaves) or TAD.txt; insi

IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open 

AEC MISSING

POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_

KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/h

MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په

HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) fol

BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1

KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt", "page_offset": "leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \\

PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-

NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf

WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.3901506621039

SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves

SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves

ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it 

FVQ {"title": "Arthur Jeffery, The Foreign Vocabulary of the Qur'an, Gaekwad's Oriental Series LXXIX, Baroda 1938", "kind": "archive_djvu", "url": "https://archive.org/details/foreignvocabular030753mbp (other copies: in.ernet.dli.2015.68878, .507015, .277274, .56841, .217779, GakewadsOrientalSeriesVol.LXXIX...)", "lookup_hint": "Entries alphabetical by Arabic word (transliterated); grep in FVQ_pages.txt; printed page p = leaf p+17 (leaf 61 = p.44, leaf 313 = p.296).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FVQ_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sou

AFM {"title": "Addi Shir (أدّي شير), Kitab al-Alfaz al-Farisiyya al-Mu'arraba, Beirut 1908 (Nourai: Library of Lebanon reprint 1980, same pagination)", "kind": "archive_djvu", "url": "https://archive.org/details/unset0000auth_c2g3 (1908 ed.; also 20250405_20250405_0055, plaintive27_gmail_20190316_1912)", "lookup_hint": "Alphabetical Arabic headwords in parentheses, e.g. '( الأرجان )'; grep in AFM_pages.txt / AFM.txt; inside.php search works. Also on shamela/al-maktaba sites as text (search 'الألفاظ الفارسية المعربة أدي شير').", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/

PLA {"title": "A. Asbaghi, Persische Lehnwörter im Arabischen, Wiesbaden 1988", "edition_found": null, "kind": "archive_djvu", "url": "https://archive.org/details/asbaghi-asya-persische-lehnworter-im-arabischen-1988-harrassowitz (user upload, unrestricted download)", "identifier": null, "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_asbaghi_1988_ia_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/PLA/PLA_pages.txt"], "page_offset": "301 lea

LKT {"title": "K. Lokotsch, Etymologisches Wörterbuch der europäischen Wörter orientalischen Ursprungs, Heidelberg 1927", "edition_found": "1927", "kind": "archive_djvu", "url": "https://archive.org/details/etymologische00lokoguat", "identifier": "etymologische00lokoguat", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LKT.txt", "page_offset": "leaf = printed + 26 (e.g. leaf 28 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Numbered entries: 

LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f b

LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for mos

FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt

WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/W

AFA {"title": "S. Fraenkel, Die aramäischen Fremdwörter im Arabischen, Leiden 1886 (repr. Hildesheim 1962, same pagination)", "edition_found": "1886", "kind": "archive_djvu", "url": "https://archive.org/details/diearamischenfr00fraegoog", "identifier": "diearamischenfr00fraegoog (also bub_gb_SzdbAAAAQAAJ)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AFA.txt", "page_offset": "leaf = printed + 30 (e.g. leaf 38 = p.8). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>",

ARB {"title": "al-Jawaliqi, al-Mu'arrab min al-kalam al-a'jami, Tehran 1966 (reprint of Ahmad M. Shakir's Cairo 1361/1942 edition)", "kind": "archive_djvu", "url": "https://archive.org/details/mo3rb (probably the Shakir edition) ; https://archive.org/details/almo3rab_gwaliqy_f_abduraheem (F. 'Abd al-Rahim ed., Damascus 1990) ; also uc1.aa0003615705 / AAlexandrina-148752 (Sachau's Leipzig 1867 ed.) ; text on shamela.ws", "lookup_hint": "Alphabetical Arabic headwords; grep in ARB_mo3rb.txt / ARB_abdulraheem.txt (raw, no page breaks); edition of mo3rb not confirmed — check its title page image.", "lo

SIN {"title": "B. Laufer, Sino-Iranica, Chicago 1919 (Field Museum Anthr. Ser. XV.3, pp. 185-630)", "edition_found": "1919", "kind": "archive_djvu", "url": "https://archive.org/details/sinoiranicachine153lauf", "identifier": "sinoiranicachine153lauf (also sinoiranicachin00laufgoog, jstor-29782155)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SIN.txt", "page_offset": "leaf = printed - 172 (e.g. leaf 15 = p.187). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "loo

RCH {"title": "J. Richardson, A Dictionary, Persian, Arabic and English, new ed. by F. Johnson, London 1829 (Lahore reprint 1984)", "edition_found": "1829 Johnson edition (DLI scan, 1814 leaves)", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.24303", "identifier": "in.ernet.dli.2015.24303 (other editions: 1806-10 a-dictionary-persian-arabic-and-english-vol.-i, india.history.resource.17812; 1852 Johnson dictionarypersia00johnuoft)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/RCH.txt", "page_offset": "leaf ~= printed + 93..94 (e.g. leaf 336 =

DEV {"title": "L. M. Devic, Dictionnaire étymologique des mots français d'origine orientale, Paris 1876", "edition_found": "1876", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairety00devi", "identifier": "dictionnairety00devi (also dictionnairetym02devigoog, fr105comparative41)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/DEV.txt", "page_offset": "leaf = printed + 26 (pp. <80) to +30 (pp. >84), e.g. leaf 29 = p.3, leaf 118 = p.88. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.

PHN {"title": "A. P. Pihan, Dictionnaire étymologique des mots de la langue française dérivés de l'arabe, du persan ou du turc, Paris 1866", "edition_found": "1866", "kind": "archive_djvu", "url": "https://archive.org/details/dictionnairetym01pihagoog", "identifier": "dictionnairetym01pihagoog (others: bub_gb_QnsSAAAAIAAJ, dictionnairetym00pihagoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHN.txt", "page_offset": "leaf = printed + 31 (e.g. leaf 33 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://ar
```


## [2026-09-05T20:37:37.883Z] TOOL CALL #6: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN grep gac ===\"; grep -n -i -E 'ga[cčč]|gypsum|Gips' HRN.txt | head -40\necho; echo \"=== HRN page 199 (leaf 220, NR=221) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==221' HRN.txt | head -60"
}
```


## [2026-09-05T20:37:38.807Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB grep ===\"; grep -n -i -E 'gac|gač|Gips|gyps' HUB.txt | head -40\necho; echo \"=== HUB page 90 leaf 100 NR=101 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==101' HUB.txt | head -60"
}
```


### [2026-09-05T20:37:39.553Z] TOOL RESULT

```
=== HRN grep gac ===
2196:Form bezen, im Gacophylacium und bei Woliaston
3580:Schmähen, Geringachtung', tiraskriya, wozu np. ter
7742:kurd. af/. LW. gac 'Mörtel'.

=== HRN page 199 (leaf 220, NR=221) ===
— 199 -
889. ffäh *Ort (in Comp.) ; Thron*.
ap. gä&U' 'Ort; Thron', vergl. /7afja(>[}/«(5(</ ; aw. gätn-
Ort; Thron'; phlv. gas\ ai. gütü- 'Gang, Bahn, Kaum*,
afy. ^yälai.
890. f/e^^Mörtel'.
aw. vlöica- 'Mörtel'; phlv. gaö^ gaöln.
kurd. af/. LW. gac 'Mörtel'.
Die Zusammenstellung mit aw. vlcica^ ist unsicher ').
891. (ßtidüften 'schmelzen', Praes. gudäz-em, gudäzclnlden
(Vis und Rrimin, 69 Zeile 1(3; AM. 105 Zeile 1).
aw. vUa/ti- 'Schmelzen, Thauen', vUaöina-; phlv.
v{i)täxian (AV., Bund.), v(i)taö(i)sn,
892. f/iidäre 'Brett (zum Dachdecken)' (unbelegt).
aw. Vitara- 'Brett, Planke (zur Herstellung eines
Kinderpferchs)' (vd. 14, 14), Rückert, vergl. Spiegel,
Kommentar I, 342 und Geldner KZ. 25, 568 Note 37.
893. ffudästen hinüberführen, hinüberziehen', Praes. gu-
där-em; guöesten 'überschreiten, passiren', Praes. //m-
öer-em; guödr 'Furt -), gudäris, guderäniden.
g. veddrte; Käk V. heidornan, Q. baudernädin.
ap. vi + l^tar-, vigatarayäma 'wir überschritten' ; aw.
vUaretö.{tanU'; ^hlv, v(i)tärt an ^ v(i)tartan {A.Y.), v{i)tar(e)
'Furt*^); arm. LW. vtar; ai. vi + iX^ar-, vitirati 'er
durchläuft, durchzieht', vitärdyati 'er führt hinüber'.
kurd. buhürtin, behartin 'die Zeit hinbringen.
Vergl. oss. d. tarun, t. farjn, färin 'treiben, jagen,
entfernen' (245); bei. tarag, n. faray 'umwenden, um-
kehren' (381); vergl. wa/. türt 'Furt'.
894. -ger '-tuend, -Macher', z. B. ähenger, dadger,
aw. 'kara- 'machend'; phlv. -kar^ -.^^rr; ai. -kara-.
1) Anders Geldner, KZ. 25, 582 Note 10; die drei daselbst
vorgeschlagenen Etymologieen sind aber sämmtlich lautgesetzlich falsch,
ganz abgesehen davon, dass die drei verglichenen neupersischen Worte
überhaupt bedenklich sind.
«j Kurd. büär 'Furt' (H.-8ch.).
') Im Pehlevl bedeutet v(i)tartan^ v(Otlntan (für av^. l^^ra^»-)
auch häufig 'sterben*, wie im Neupersischea derguSesteu (vergl. zu dem
Sprachgebrauch West, Öäy. näsäy. II, 38).
```


### [2026-09-05T20:37:41.319Z] TOOL RESULT

```
=== HUB grep ===
3206:890. Np. gac 'Kalk' = phi. paz. gad Shk. 245 = arab.
3207:Jass 'Gips', syr. ges§a erweisen anl. g als urspriinglich.
3208:Arab. pers. jfabstn gypsum' aus gr. yvifjogj yviptvog (nicht— 91 —
8102:vgl. gr. yapyivog (Lehnwort?); ga6 *Kalk' = paz. gac, aus
8103:phi. *gacc?y vgl. arab. ja?s 'Gips, syr. gessa, gr. yvxpog
8879:mogac anderjapet bei Faustus 157), ^YA.magupat, vgl.

=== HUB page 90 leaf 100 NR=101 ===
— 90 ~
881. Lies arm. LW. U^n 'GroU, Hass, Feindschaft, Rache',
davon fcinavor 'groUend', vgl. np. klnvarj kmavar *6roll
hegend'. Dazu afgh. LW. kma fem. 'malice, spite,
rancor, hatred*.
883. Iranische Wurzel ist jedenfalls ga (= skr. *ga oder
'^gha). Zd. gamd'bereiti" iibersetzt Darmesteter
wieder wie Spiegel durch 'Schritt'. Np. gan = kurd.
gan (ZDMG. 38, 84) setzt ein ap. ^gdna- coitus' vor-
aus.
885. Zd. atare-vazana- == 'Blasebalg , vgl. ZPGl. p. 21 und
61, Darmesteter, Zend-Avesta II, p. 214 (= phi.
ataxs-va:2flnUar), Uebrigens liegt kein Grund vor an-
zunehmen, dass g von gd» 'Zange\ gazidan *beissen'
u. s. w. aus V entstanden sei. Vgl. phi. gazitan ^^
paz. gazldan *to bite, sting, gazd(u)m 'Scorpion Gl.
and Ind. 259, 265, Shk. 246. Die Etymologie ist also
falsch.
888. Np. gdv *Rind' setzt einen ap. ace. sg. gdvam, eine
analogische Neubildung fiir alteres "^gdm = zd. gqm,
skr. gam voraus, wahrend np. go-^ gav = ap. gau- der
Composita (wie Gaubruva-) oder gav- der schwachen
Casus ist. — Das angefuhrte arm. gavazan heisst
*Stab, Hirtenstab, Gerte und ist = np. gavaz ^stimulus
quo asini et boves impelluntur , zd. gavdz- *Ochsen-
stachel', skr. go-djana- *Rinder-antreibend' (sc. 'Stock').
— Davon zu unterscheiden np. gavaz = gavazn 'cer-
vus, dama*, g. go gevezm *Hirsch* ZDMG. 36, 63 ^=
afgh. LW. gavazn 'an elk\ Vgl. auch afgh. gavaz
'Gemse'. — Fiir osset. t/og lies yog. — Zu gOivmes
'Buffer = zd. *gao-ma^a- 'Kuh-widder' fiige noch die
LW. bal. gatnes^ gvamSs 'Biififer, afgh. gavmes 'a male
buffalo*.
889. Dazu arm. gah 'Thron, Sessel, Sitz, Rang, Wiirde*
(alt und haufig).
890. Np. gac 'Kalk' = phi. paz. gad Shk. 245 = arab.
Jass 'Gips', syr. ges§a erweisen anl. g als urspriinglich.
Arab. pers. jfabstn gypsum' aus gr. yvifjogj yviptvog (nicht
```


## [2026-09-05T20:37:56.115Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HUB p.91 (leaf 101, NR=102) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==102' HUB.txt | head -25\necho; echo \"=== HUB context around line 8102 ===\"; sed -n '8090,8115p' HUB.txt"
}
```


### [2026-09-05T20:37:57.686Z] TOOL RESULT

```
=== HUB p.91 (leaf 101, NR=102) ===
— 91 —
umgekehrt wie Prellwitz, Etym. Wb. der griech.
Sprache meint).
892. Darmesteter iibersetzt zd. vUara- durch allee' und
vergleicht np. gtiJar a ferry, a passage* (vgl. guSar
*Durchgang'). Auch unsicher.
893. Np. guddSta/n =- 'vorbei lassen, passiren lassen, lassen'
ist Causativum zu gudastan Voriibergehen , vorbei-
gehen, vergehen'.
895. Np. garr *Kratze' stimmt jedenfalls lautlich voU-
kommen zu zd. garenu^.
897. Vullers hat gurdzldan (mit u) einherstolzieren,
ebenso Sal. Shuk. gurdztdan *sieh wiegend gehn\
Fr. Miiller, WZKM. 8, 189 stellt das Wort zu gurdz
*£ber , ich halte an der Zusammenstellung mit skr.
vraj fest.
898. Np. girdn *schwer = ap. ^grana-?
899. Vgl. zd. vareti' in hqmvareti- *Tapferkeit\ Phi. gurt
steht fiir alteres *vurt = ap. "^vrta-.
900. Vgl. auch ZDMtt. 30, 138—141. Das in der Note
angefiihrte vird 'Schiiler hat keinesfalls etwas mit np.
sdgird 'Schiiler' = phi. asdkert zu thun.
901. Np. gird 'Umkreis, rund, rings* liegt im Phi. als
g(i)rt vor, vgl. Phi. Vd. p. 211, Z. 9, Bdh. Gl. 219,
6uj. Abal. 74 u. s. w. und das dazu gehOrige gird<i

=== HUB context around line 8102 ===
fhl, *micak; dd0, ddza*Lsick\ arm. dod (medic. Schriften) in
doci xez = Xack-gummi'; pazan = pdzan, kavtz = kavHz
s. oben, raja^ raza oben p. 66 ^). Np. ocaj *Kreuz' aus alterem
"^xac = arm. xac *Kreuz* ist arm. LW.
•
§ 117. Wenn nun 6 nach tonenden Lauten zu z, Zyj
geworden ist, so sollte 6 nach Vokalen und r im Np. nicht
mehr vorkommen. Dies ist dennoch der Fall in: ha6a =
ha66a (oft bei Firdusi) Junges', das auf phi. *va66ak (aus
vat'Cak oder ahnl.) zuriickgeht und sein cd erst in neuerer
Zeit zu d vereinfacht hat ; xarcang 'Krebs* = phi. kardang
(volksetym. an xar 'Esel' und 6ang angeiehnt ? oben p. 54),
vgl. gr. yapyivog (Lehnwort?); ga6 *Kalk' = paz. gac, aus
phi. *gacc?y vgl. arab. ja?s 'Gips, syr. gessa, gr. yvxpog
(Lehnwort ?) ; hed^ ex *irgend ein', erst im Mp. aus g = gr =
ap. aiva- ein* und 6 = ci ^= ap. ciy zusammengesetzt^),
vgl. agat'ci, mamc (dial.) u. s. w. H. 451.
Aus jiingerer Zeit muss auch das Deminutivsuffix ^)
(fa, tea (VullerS; Gram. p. 234) stammen: bayda 'GtSiTtchen,
aluca 'Mirabelle* [dlu Tflaume'), baztca 'res lusoriae', darlca
'Thiirchen, Fenster, Gussform' = arm. daricak *Gussform'
(11.— 13. Jhd.), huzUa a kid' JRAS. 1894, 448, suroi^ca
*R5theln (auch surxtza, vgl. turbzza *Radieschen' *) von turb
'Rettich' bei Rosen, Np. Sprachf. p. 36).
Geschwunden ist c vielleicht in kas *jemand' = zd.
kascit, ap. kasciy, Vgl. pas *hinter = zd. pasha {paskCU),
```


## [2026-09-05T20:37:58.088Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AKD grep gass/gypsum/Gips ===\"; grep -n -i -E 'gassu|ga..u.*Gips|Gips|gypsum|yvip|γύψ' AKD.txt | head -40\necho; echo \"=== AKD p.32 leaf 40 NR=41 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==41' AKD.txt | head -60"
}
```


### [2026-09-05T20:37:59.620Z] TOOL RESULT

```
=== AKD grep gass/gypsum/Gips ===
430:natbuhu,  nadbalm  wahrsch.  (Ziegel) schiebt  (neben  einem  natbalai,  nadbalai Gießbach,  von  tabdhi  gießen)  :  >  bibl.-aram.,  jüd.-aram.  nidbdl;  auch  midbdJc Bauschicht,  Steinlage  (>  arab.  midmdk).  akk.  gnssu  Gips  :  >
432:aram.  ga.'^sä  (^  arab.  gass,  giss,  guss,  auch  qass,  qiss),  griech.  yvifjog,  lat. gypsum,  Gips.
973:akk.  gassu  Gips  s.  oben  S.  31  f.  akk.  hipru  Erdpech,   As-

=== AKD p.32 leaf 40 NR=41 ===
 s.  oben  S.  14.  akk.
saniHu  ein  Teil  der  Mauer  :  >  viell.  aram.  sdwJtd  Ecke  O  arab. sdivijai,  auch  wohl  späthebr.  PI.  zdwijjöt).  akk.  zirrn  Einfassung
od.  ä.  :  >  viell.  hebr.  ser,  jüd.-aram.  zirä  Kranzleiste.  Vgl.  auch  noch unten  S.  38  zur  Bed.  Halskette.
akk.  qariiu  Kornboden,  eig.  wohl  Gebälk  :  ^  wohl  hebr.  qord Balken,  denom.  qcrä  bälken,  mdqdre  Gebälk,  aram.  qäritä  Balken  O  arab. qarijjat).  akk.  gimiru  Balken  :  ^  aram.  gdSürd  u.  Jca.snrd.  —  Vgl.
auch  unten  S.  44  zu  gisru  Brücke.  akk.  gas  im  Stange,  vieU.  auch
Querbalken  :  >  neuhebr.  ^«.«.s  Brett,  Querstange,  wohl  auch  jüd.-aram. gäSOsä  Schiffsstange.
akk.  igäni  VTand  :  >  viell.  aram.  ^iggdrd,  "eggdrd  Dach  O  arab. ^iggär,  "ingdr).  akk.  imdu,  indu  Stütze  (eines  Hauses,  einer  Wand;
von  emedu,  'md,  stehen)  :  davon  viell.  beeinflußt  hebr.  'ammüd  Säule, phön.  'md^  aram.  'anmulda  O  wohl  arab.  'amüd\  südarab.  'md,  äth. 'amd.  akk.  gidlatti  Wulst,  Kugel  (an  einem  Säulenkapitell  :  >
wohl  hebr.  gidld.  Zu  hebr.  hapiör  Säulenknauf,  s.  unten  S.  55
unter  Jcaptarn.
akk.  libiMn,  st.  c.  libnat  Ziegelstein  :  >  hebr.  hbcnd,  aram.  hbentd^ Idiettü  O  arab.  libnat,  labinat)^  südarab.  Ibt,  sowie  wahrsch.  griech.  /;  Jillv&oi.
akk.  agurru  gebrannter  Ziegelstein  :  ^  aram.  'ägurd  O  arab. 'ägurr,  ^dgdr,  desgl.  pers.  dgdr,  armen,  agur,  griech.  ayovQog).  akk.
natbuhu,  nadbalm  wahrsch.  (Ziegel) schiebt  (neben  einem  natbalai,  nadbalai Gießbach,  von  tabdhi  gießen)  :  >  bibl.-aram.,  jüd.-aram.  nidbdl;  auch  midbdJc Bauschicht,  Steinlage  (>  arab.  midmdk).  akk.  gnssu  Gips  :  >
      32      
aram.  ga.'^sä  (^  arab.  gass,  giss,  guss,  auch  qass,  qiss),  griech.  yvifjog,  lat. gypsum,  Gips.
akk.  Jcamdtu  Außenseite  od.  ä.  (am  Hause)  :  >  viell.  aram.  haivivatä Fenster  (>>  arab.  hawwat,  kuivwat).  akk.  cqjtu,  PI.  apäti.,  appäti
Fenster,  Öffnungen  in  einem  Hause  (viell.  <[  sum.  ah)  :  >  viell.  hebr. "ab,  PI.  "iibhhn  als  bautechn.  Ausdr.,  und  wohl  sicher  jüd.-aram.  'aptci  Erker, Vorbau.  [Dagegen  ist  akk.  Iiillnni  Öffnungen  in  dem  Vorbau  eines
Hauses  <  westsemit.  (hebr.)  hidlun  Fenster.]  akk.  jiuraSdinnu
Loch  od.  it.  :  ;>  viell.  hebr.  parsddön  Eicht.  3,22  (falls  eine  Räumlichkeit im  Hause  und  nicht  vielmehr  einen  Körperteil  bedeutend).
akk.  kutallu  Rückseite,  Hinterseite  des  Körpers,  dann  auch  eines Gebäudes  :  >  wohl  aram.  kutlä  Wand,  Seite  O  wohl  späthe
```


## [2026-09-05T20:38:53.375Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT vicica ===\"; grep -n -i -E 'v[iī][cč][iī][cč]a|vīčiča|vicica' BRT.txt | head -20\necho \"=== BRT nyay ===\"; grep -n -E 'nyāy|nyay|niiāii|nyāiš|nyāis' BRT.txt | head -30\necho \"=== BRT gāθā / gatha ===\"; grep -n -E 'gāθā|gāθa|gaθā' BRT.txt | head -20"
}
```


### [2026-09-05T20:38:53.458Z] TOOL RESULT

```
=== BRT vicica ===
=== BRT nyay ===
13113:yahmat  haca  Jräkwirisal  näfs  airyanqm °Hyunqm  ^r^m  airyanqm  'hyunqm  Yt. '^■^7)  —  ifar^Rö  .  .  yat  asti  airyanqm 'Ayunqm  Ytip.  56;  V. /^.  39;  —  iava/ftn :^arpnd  'hrähr^m  airyanqm  "AyunamYl-ig. 69;/?.  10; —  avavat  kavaSm  3^ar>ns yaha yat  iöa  anairym  °Ahus  hakat  usäi  us.frs- vayöit  (sd.)  Yl.  ip.  6  8 ;  —  taurvayeiti  anairya *'/iAävS(3isA'P.)Yt.iS.2;  —  airaityanqm tat  °Ayunqm  Vf/y^rai  uzjasaiH  N.(iS;  — aiioitaradyJ  haca  'nhubyö  Yt  i'j.  14;  — mi>r)m  .  .  yim  yazmte  daiAkupatayS  .  . aniar»  -iiihu  (AD.)  papr^täne  Yt.  10.  8; r_5.  49;  —  hasaaräis  (näml.  asH  mihrS) aiitary  °Ryu  (AD.)  Yt.  /o.  117;  —  yd  .  . karafanö  urapayeintl  (sd.)  yacä  xrata *Ju£>sc/a'irä  "Ayunqm  Y.4^'.io;  —  säsia 'rthSui  äaähupailii  *äxsta  isimnS  'lihave amtm  is^mnS  tanuye  YtJÖ^.  19;  —  sSsta 'itißaus  hams^ia%rö  Yt  13.  r8,  69,  75.  50; — fraiimatcltl!  'Xyunqm  Yt  13.  95;  *lo.  18; —  nöit  me..  ährava  . .  'iiifiava  (LS,)  earät Y.p,  34;  —  Siihqm  'hyunqm  yä  anyä rajSit  Y.ig.  18;  —  bawrSil paiti  'tJihaove Yti.ag.  a)  GS.  mit  GS.  des  Landes- namens  zur  Bezeichnung  der  Gebürtigkeit bei  EN.:  parlatgava  dazgrS^ava  apa- jTjVavi  (sd.)  'iähfus'  Ytrj.i2j;  127;  — ^rüJ  atv5jar3(^  fyultahe  tanyehe  tanyayä •tViÄÄ/ Yl  jy.  125;  125';  —  s,  noch tnzavant-  daitiksus  EN.  a)  bes.  im Gegensatz  zu  Haus,  Gemeine  und  Gau***; a)  im  gAiw.:  *S  sl  dimSnsm  vTs)m  v3 söihnrrt  vä 'Ayäm  vä  adaj  du^iäcd(sd.) .. Y.jt.  18;  —  yP  Auäänus  d^manahyä  xla- %r?m  iiSi^rahyS  vä  'AySus  vä  .  .fi-ada'iiäi (sd.)  asppmaia  Y.Jl.  16;  —  ga  JrSnKis' (sd.)  /tfiiraAyä  vä  'AySus  vä  Y.4ß.^; —  ähnlich:  patri  jfaSSuf  airyamanascä dadaiii  (sd.)  tiSil  ma  xsnäus  yä  v^rvsSnä (sd.)  ..  naida  'hy3u!  ..  sästärB  (sd.)  Y.46. 1.  b)    im  jAw.:    */ratainitm   .  .  yä
14600:•  j.  ^rit-  m.  EN.  eines  Gläubigen:  'tö agvs.sar^S  (sd.)  fytiitake  ianyehe  tanyaya dairfhSul  aiaonS  Yt  13. 125.
18972:—  ai.  nimai-  a.  'Huldigung';  vgL  mp.  namät, np.  namäs  'Gebet'.  —  Pü.  1  nyäyäit ;  itamii-, a.  noch  No.  3ff.,  6f.  —  ')  Pfi.:  nyayihiamandih.
22976:yanqm  dalvanqm  .  .  vTspanqm  daevanqm "nyanamca  drvatam  Y.  27.  1;  Ytj.  22,  13. 137;  —  P"'*^  mainyaoyä^  drujat  *'nyaya- affa  *drv5.ikyat  Yt  /J.  7 1 .
=== BRT gāθā / gatha ===
```


## [2026-09-05T20:38:54.938Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK p355 ===\"; grep -n -E '^gē[iī]|gēi-|gī-.*singen|355' POK_full.txt | head -20\necho \"--- POK_01 leaf for p.355 = leaf 363 -> NR=364 ---\"; awk 'BEGIN{RS=\"\\f\"} NR==364' POK_01.txt | head -70"
}
```


### [2026-09-05T20:38:57.320Z] TOOL RESULT

```
=== POK p355 ===
4501:(below likewise; Kuhn KZ. 30, 355; different Specht Dekl. 125). 
17095:References: WP. I 772 f., WH. I 345 f., 347, 349 f., 355, 357 f., 727, 732, 860, Schwyzer 
23187:RC 20, 355) from *d^uorato-\ compare gall. Ic/ora/o/? "grille, lattice door' in gallorom. 
25067:yet s. Schuize EN 2204, 355); 
27615:References: WP. II 352, Holthausen Altwestn. Wb. 355. 
28152:excitement, help'(*a//-c»/'-/o), etc. (Loth RC 40, 355); compare also Ifor Williams RC 43, 
30010:Page(s): 354-355 
31749:Page(s): 355 
34138:Berneker 355 considers doubtingly for Old Church Slavic grozdh "grape', grozrrb ds. a 
35801:Page(s): 355-356 
44001:References: WP. I 355 f., WH. I 173 f., Trautmann 118 f. 
44271:References: WP. I 355, WH. I 202, Specht Indo Germanic Del<l. 52. 
66554:torch', ablaut, to Old English cTnan, above S. 355) wird Modern High German Kiefer, 
83683:References: WP. II 522 f., WH. II 528 f., Wackernagel-Debrunner III 355 f., Ross TPS 
91678:References: WP. I 272 f., II 373, Trautmann 355, 362, Vasmer 1, 186 f., E. Fraenkel KZ. 
--- POK_01 leaf for p.355 = leaf 363 -> NR=364 ---
```


## [2026-09-05T20:39:00.939Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31700,31760p' POK_full.txt\necho \"=== 30010 context ===\"; sed -n '29975,30015p' POK_full.txt"
}
```


### [2026-09-05T20:39:01.013Z] TOOL RESULT

```
Meaning: glowing coals 

Note: 

Root / lemma: g(e)u-lo- : glowing coals derivded from Root / lemma: ker(9)-3\ to burn 

Material: With Asuffix: 

Irish guar coa\' (< *geulo- or * goulo); 

Old Icelandic kolu. " charcoal ', Old English colm. "coal', engl. coal. Old Frisian kolei.. 
Old High German kolom., also kolu.. Middle High German kolu., kol(e)xx\., kolei., Swiss 
c/7c»//e "gleam'. 

In addition with /"-suffix (or previously reshaped from *^^/c»- after Armenian hur^f\re'): 

Armenian Ara/r "fire, glowing coals' (< *guro-, *gura-), krak-aran^ siove, hearth, fireplace, 
glowing frying pan '. 

References: WP. I 563. other possibilities by W. Schuize Kl. Schr. 479. 
Page(s): 399 

Root / lemma: ge(i)- : gd(i)- : 57- 

Meaning: to sing, to cry 

Note: onomatopoeic word 

Material: Old Indie gayatiax\6 gati^ sings', gatu-xx\. and gTtf-i. " song', ^/?a-"sung, 

chanted', gatha^ song, verse' = Avestan ga&a^ song of religious content '; 

Old Russian gaju, gajati^ crow, squawk ', russ. gajb m. " Jackdaw's croaking, clamor', 
gakatb " groan, croak, caw ' etc.; 

Baltic *geidd\v\ Lithuanian gfeduav\6 gfestu, g/edot/" s\ng, cackle, crow, squawk ', 
Latvian dziedu, dz/edaf 's\ng'; in addition Lithuanian gystu, gydau, gyst/'to sing, begin 
crow ', ga/dysm. "rooster, cock', giesmei. "Kirchenlied', Latvian dziesmai. " song ', gaWs 
m. "rooster, cock'. 

Maybe Latin ^a/A/s "rooster, cock' : alb. 5/e/" rooster, cock' 

Tocharian A kak, B kaka^ he shouted ' (redupl., to Old Indie gati), present 3. PI. kenehc 
[*gei-n-l), Pedersen Tochar. 183, 263. 

References: WP. I 526 f., Trautmann 76, W. Schuize KZ. 27, 425 = Kl. Schr. 52. 



Page(s): 355 



Root / lemma: geu-, gau-, gu-{*sgeu-) 

Meaning: to bend, curl; a kind of vessel 

Note: 

Root/ lemma: geu- gsu- gu-\ to bend, curl; a kind of vessel probably derived from Root/ 

=== 30010 context ===

Lithuanian ^e/Z?^5 "clumsy, unadept, unskillful ', geibstu, gefbtT become weak, collapse, 
perish '; in addition with Aniaut variant ^t/ after Trautmann KZ. 42, 372: Lithuanian 
gvaibstu, gvafbtr become senseless, unconscious, swoon, faint, blackout ', intens. 
gvaibeti?, Latvian (with dissimilation reduction of z/ before b, or borrowing from Lithuanian? 
s. MiJhlenbach-Endzelin I 582, 695, 698) gibstu, gibC sink, fall, bend down ', geibstu, geibt 
" perish, die', geiba^ dizziness, giddiness; swindle, clumsy, weak person', gaiba^ foolish 
woman '. 



geim- : 



Norwegian dial. /re//77a"bend askew, hold the head askew, swing, bin und herschweben 
', /r//77a" turn, sway (with joy) '. 

geis- : 

Old Icelandic /re/sa "bend, crook', PN ATs/] isl. ^e/s "round belly', Norwegian dial. i(eis 
"movement, curvature ', ids' hump, hunchback ', Swedish icesa' flee in wild escape ', 
Swedish Norwegian dial, idsa' squint, leer, cross one's eyes, blink'. In addition further with 
gramm. variation Old Frisian i(era. Old Saxon icerian, iderian. Old High German iceran' 
turn, twist ' (wherefore the retrograde formation /remand icera' turn, circular movement, 
spin '), Middle High German i<eren. Modern High German i<ehren, Swiss chTre"' nach 
einer Seite neigen '. (Different about /reAa/? Scheftelowitz BB. 28, 296, it with Armenian cir' 
circle ' combined, wherefore Petersson PBrB. 44, 178 still placed osset. zTiin, zeiun' slue, 
turn, turn around reverse '.) 

Here also with Petersson LUA 1922, 2, 39 ff. Armenian /r//re/ "crook, bend' (to *i<ii<< 
*gisuoll), and russ. dial, zichatb, zichatbsja " bend, give way, yield to, sway ', zichijatb " 
make something stagger '? 

References: WP. I 545 f., Persson Beitr. 83 ff., WH. I 597. 
Page(s): 354-355 



Root / lemma: gel^
```


## [2026-09-05T20:39:15.092Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC gaulos ===\"; grep -n -i -E 'gaulos|γαυλ|gaul-|ǵaulos|gaulo' IEC.txt | head -30\necho \"=== IEC leaf 209 (p.387/388) ===\"; awk 'BEGIN{RS=\"\\f\"} NR==210' IEC.txt | head -80"
}
```


## [2026-09-05T20:39:17.000Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 Bhagavad ===\"; grep -n -i 'bhagavad' KLN_1966.txt KLN_1971.txt | head -10\necho \"=== KLN gatha ===\"; grep -n -i -E \"^Gatha|Gatha,|'Gatha\" KLN_1966.txt KLN_1971.txt | head -10\necho \"=== KLN gypsum ===\"; grep -n -i 'gypsum' KLN_1966.txt | head -10\necho \"=== KLN galley ===\"; grep -n -i -E \"galley|galleon|galiot\" KLN_1966.txt | head -20"
}
```


### [2026-09-05T20:39:17.305Z] TOOL RESULT

```
=== IEC gaulos ===
61:DorriN, G.: La langue gauloise. Grammaire, textes et glossaire. Réimpression de Pédition de Paris 1920. Reprint Slatkine, Geneva 1980
11749:Gk. nípto, nízo, id.; cf. Skt. (redup.) nenikte, mp., pp: niktáh, id. (pp. as in Gk. á-niptos *unwashed"); MIr. nigim, Ir. nighim, v. ‘wash’, cf. also Ir. pp: nighte, adj. “washed, clean’; OCS cf. nístvy, fpl. “trough”; Cz. necky, fpl. *washtub' (Slav. vocalism ambig. esp. in view of Blg. no&cvi, pl. ‘kneading-trough’. A Gaul- ish form nectos ‘pure’ is alleged.) Ir. neagaim, v. ‘notch’; MHG nicken, wv. tr. “bend, force down’; OCS oo nísti, beside (intensive) nizajo, ati ‘pierce’. (Isophones in OCz. nZu, nzieti “pine, fade’; Li. ninZu, nyZti ‘form a scab; itch’, niZius ‘itchy’, and Latv. (e-gde) nieza ‘itch’; niezet, inf. id. See niĝ- (3)
=== IEC leaf 209 (p.387/388) ===
r. bēr, id.; Go. qaíru ‘stake, thorn’
guēros ‘consuming; consumer’. grade variant of guer-, q. v.) Skt. jāráh (epithet of Agni); Arm. kir, o-st. Time; kirk “passion, impulse’; cf. krak, dim. ‘fire’; Li. cf. geréjas, géróvas, m. (*drinker', lit. *consumer?)
guesó, ið ‘extinguish; be extinguished’. WP I, 693. Cf. guest- Skt. jáse “am exhausted”; Av. zah-, jáh-; Tokh. kás-, B kes-; Gk. cf. s-bénnumi, fut. s-béso; Sw. kväsa ‘stifle’; long o-gde in OCS ga&o, gasiti (and com. Sl.); extn. in Go. us-qistjan ‘kill’; Li. gestu, inf. gesti ‘extinguish’ beside gëstü,
(Long-
gesti ‘go out, of light’; Latv. dzesu, dzēst *ex- .
tinguish"; dzeseju, et, id.
guest- (variant of gues-, q. v.) Go. us-, fra-qistjan ‘kill’; Du. ver-kwisten ‘waste’; NGer. Quiste *loss'; Li. cf. gesteriu, eti ‘decay, go bad"
gueto, ið ‘proclaim, pronounce, ban’.
guernu- — guiglos (guigil-)
20
25
30
35
40
45
358
Arm. kocem ‘call, name” (cf. SEM : AIE : §§ 16, 91, 130); Lat. vetō ‘forbid’; cf. also ar-biter ‘umpire, witness’; Go. qiþan, OHG quedan, OE cweðan ‘say’; ON kviðja ‘forbid’ beside Icel. kviður ‘saying’, kviða, f. ‘poem’
guetru (guetəros) ‘neck, collarbone’ Skt. jatru ‘collarbone’; Av. cf. jataras, n., ja- taro, m. (queried ‘col, mountain pass’), LG quedder ‘collar, belt’ beside kader ‘crop, goi- tre’
'guetu (guetuə) ‘resin, gum’. WP I, 672 Skt. jatu ‘resin, gum, lac’; Tokh. cf. bez, Dig. bedzä ‘honeycomb’; Gallo-Lat. cf. betu-men, bitu-men, vitu-men (‘pitch’. “Bitumen ex ea Galli excoquunt' — Pliny); Gael. (*-&- or uml. by *-u) bíth ‘resin, gum, birdlime'; W cf. bedw ‘birches’, as source of gum?; Cor. bedhow, id.; Ir. cf. beathóg, id.; OE cweodu, n. (2) *resin'; cf. Icel. z-gde kvoóa, id.; Sw. kåda, id. Extensions in Lat. vitrum “glass”, vitellus *egg- yolk' (for the semantics, cf. LLat. glesum ‘amber, crystal", fr. Gmc. "glass: z-gde in Gk. alábastron ‘alabaster’, lit. 'saltglass', as seen in hals ‘salt’. Alb. gastare “glass? is of obscure or- igin. (Type *guet-tro-, *guot-tro- or sim.)
(gual-, see gul- (1) & (2)). WP I, 691
(guənā, guon-, see guena woman"). WP I, 681
guou- (gu-) “ox; filth’. See guóu- and cpds. R- and z-gde forms in Skt. eu beside -gaváb, cpds.; OBr. bu- in bu-es ‘stable’; OW bu- in bu-al *drinking-horn'; ON kýr, as, ds kú; R cf. gumnó, Cz. humno *threshing-floor, barn’, fr. *guou- or *gueu-mn, lit. *ox-press' beside Cz. hov-ézí, adj. ‘beef, hov-ado ‘beast’; hov- no, R gov-no “dung”
guibhro, ið «dash, shake". Lat. vibro, are; OE cf. cwifer-lice ‘zealously’; E to quiver
guigeió, guigueio, guigu- ‘enliven; come to life". Cf. guiguos, guiglos Lat. vigeo, ére; MHG quicken; OE cwician
guigio ‘chirp’ Gael. biog, s. id.; LG kwieken, id. Li. cf. Zvie- giu, ti ‘squeal’, fr. a type *8ueig-)
guiglos (guigil-) "lively, vital; liveliness, guts’. Cf. guigeió Lat. vigil, adj. «alert; s. ‘watchman’; Hes.
 
359
(Thracian?) zíglas, pl. ‘vitals, guts’; Latv. dial. Zigls ‘lively, dashing’
guiguåmi ‘go’. Variants gaio, ghíghami, q. v. Skt. jígami, jagami; Hom. bíbëmi, bibáo; other forms ambig.
guiguð, ið, see guigeið
guiguos “live, alive’. Variant of type guïuo-, q.v. and cpds. WP I, 670 Gmc. forms: cwicu, cwic, cucu in OE; MHG quëc; ON kvikr; Sw. kvick. (Gk. zizánion, if
Thracian: ‘darnel, quitchen? & Du. kweek: OE Å cwice conflicts w. a supposed Sumerian back-
ground of type zizan “wheat')
gui£0, io “burn, sting’. Cf. giĝö (2). (The Arm. and Sl. evidence is ambiguous) Arm. kcem ‘prick, sting’; kic, gs kco
```


### [2026-09-05T20:39:17.442Z] TOOL RESULT

```
=== KLN 1966 Bhagavad ===
KLN_1971.txt:25005:ment in Bhagavadgita, and in bahadur. 
KLN_1971.txt:29105:Bhagavad-Gita, the celebrated dialogue between 
KLN_1971.txt:180046:sheesh, Bhaga, Bhagavad-Gita. For E. - ous (in 
KLN_1966.txt:4302:baksheesh,  n.,  a  gratuity ;  a  tip.  —  Pers.  bakhshish, lit.  ‘gift’,  a  derivative  of  the  verb  bukhshidan,  ‘to give’,  fr.  I.-E.  base  *bhag-,  ‘to  distribute,  share out’,  whence  also  OI.  bhdjati,  ‘assigns,  allots, apportions,  enjoys,  loves’,  bhagah,  'allotter,  dis¬ tributor,  master,  lord’,  Gk.  9ay£tv,  ‘to  eat’. See  -phagous  and  cp.  Bhaga  and  the  first  ele¬ ment  in  Bhagavadgita,  and  in  bahadur.
KLN_1966.txt:4885:Bhagavad-Gita,  the  celebrated  dialogue  between Krishna  and  Arjuna  inserted  in  the  Maha- bharata.  —  OI.  Bhdgavadgita,  ‘the  song  of  the Sublime  One’,  compounded  of  Bhaga,  suff. -vant  (corresponding  to  Gk.  -Fevr-,  -evt-)  and gi-td,  ‘song’,  prop.  fern.  pp.  of  gdyale,  ‘sings, calls',  from  the  I.-E.  imitative  base  *ga-,  *gi-, whence  also  Avestic  ga&a,  Pers.  gah,  ‘song’, Lith.  giedoti,  'to  sing’,  giesme,  ‘song’,  Lett. diesma,  ‘song’.
KLN_1966.txt:28431:-phagous,  combining  form  meaning  ‘eating,  feed¬ ing  on’,  as  in  creophagous,  xylophagous.  —  Gk. -9ayo;,  ‘eater  of’,  from  the  stem  of  9xyetv,  ‘to eat’,  which  is  cogn.  with  Ol.  bhajati,  ‘assigns, allots,  apportions,  enjoys,  loves’,  bhagah,  ‘al¬ lotter,  distributor,  master’,  bhaksati,  ‘eats, drinks,  enjoys’,  Avestic  baya-,  OPers.  baga-, ‘master,  god’,  lit.  ‘distributor’,  OSlav.  bogu, ‘god’,  bogatu,  ‘rich’,  u-bogu,  ne-bogii,  ‘unfortu¬ nate’.  All  these  words  derive  fr.  l.-E.  base *bhag-,  ‘to  distribute,  share  out’.  Cp.  the  second element  in  esophagus.  Cp.  also  bahadur,  bak¬ sheesh,  Bhaga,  Bhagavad-Gita.  For  E.  -ous  (in -phagous),  as  equivalent  to  Gk.  -o;,  see  -ous. -phagy,  also  -phagia,  combining  form  meaning
=== KLN gatha ===
KLN_1971.txt:9209:Agatha, fern. PN. — L., fr. Gk. dya-9-r], fern, of 
KLN_1966.txt:1914:Agatha,  fern.  PN.  — -  L.,  fr.  Gk.  ayaOy,  fern,  of dyadic,  ‘good’.  See  agatho-.
=== KLN gypsum ===
7682:Derivative :  cincture,  tr.  v. cinder,  n.  —  OE.  sinder,  ‘impurity  of  metal, dross’,  rel.  to  OS.  sinder,  ON.  sindr,  Dan  sinder, MLG.,  MDu.  sinder,  Du.  sintel,  OHG.  sintar, MHG.  sinter,  sinder,  G.  Sinter,  and  cogn  with OSlav.  sfdra,  ‘sinter’,  Czech  sddra  (for  *sen- dhrd),  ‘gypsum’.  Cp.  sinter.  The  spelling  of  sinder was  influenced  by  F.  cendre ,  ‘ashes’,  with  which it  has  nothing  in  common.
16081:Gesneria,  n.,  a  genus  of  plants  (bot.)  —  ModL., named  after  the  Swiss  naturalist  Konrad  von Gesner  (1516-65).  For  the  ending  see  suff.  -ia. gesso,  n.,  plaster  of  Paris.  —  It.,  fr.  L.  gypsum, ‘plaster,  gypsum’.  See  gypsum, gest,  n.,  an  exploit,  a  deed  (archaic).  —  F.  geste, lit.  ‘something  done’,  fr.  L.  gesta,  ‘deeds,  acts’, neut.  pi.  of  gestus,  pp.  of  gerere,  ‘to  bear,  carry, produce,  do’.  See  gerent  and  cp.  jest,  which  is  a doublet  of  gest.  Cp.  also  res  gestae.
16950:gypseous,  adj,  1)  containing  gypsum;  2)  resem¬ bling  gypsum.  —  L.  gvpseus,  ‘of  gypsum’,  fr. gypsum.  See  gypsum  and  -ous. gypsiferous,  adj,  producing  gypsum.  —  See gypsum  and  -ferous.
16951:Gypsophila,  n,  a  genus  of  plants  of  the  pink family  (bot)  —  ModL,  compounded  of  Gk. yuil*/?,  ‘chalk,  gypsum’,  and  9Uelv,  ‘to  love’. See  gypsum  and  philo-. gypsous,  adj.  —  A  var.  of  gypseous, gypsum,  n.  —  L,  fr.  Gk.  yuij/oc,  ‘chalk’,  of  Sem. origin.  Cp.  Arab,  jibs,  Mishnaic  Heb.  gebhes, gephes,  ‘plaster,  mortar,  gypsum’,  which  prob. derive  fr.  Akkad,  gassu  (whence  also  Aram. gassd,  whence  Arab,  jass,  jiss,  juss,  qa$s,  qisf), ‘gypsum’.  —  Cp.  gesso.
34487:seleniferous,  adj.,  containing  selenium  (chem.)  — See  selenium  and  -ferous. selenite,  n.,  a  variety  of  gypsum.  —  L.  selenites, fr.  Gk.  rtzKryii-cr,',  short  for  aeXryT-'qc  Xtflo?, lit.  ‘moon  stone’,  fr.  ae'/.ryt] ,  ‘moon’  (see  seleno- and  subst.  suff.  -ite);  so  called  because  it  was supposed  to  wax  and  wane  with  the  moon. Derivative:  selenit-ic,  adj. selenium,  n.,  name  of  a  nonmetallic  element (chem.)  —  ModL.,  coined  by  its  discoverer,  the Swedish  chemist  Jons  Jakob  Berzelius  (1779- 1848),  fr.  Gk.  ceXy)vr,,  ‘moon’;  so  called  by  him because  of  its  resemblance  to  tellurium,  the  ele¬ ment  called  after  the  earth.  See  seleno-  and  2nd -ium.
36068:spar,  n.,  a  nonmetallic  lustrous  mineral.  —  LG. spar,  ‘gypsum’,  fr.  MLG.,  rel.  to  OE.  spaer-  in spser-sian,  ‘gypsum’,  and  to  spxren,  ‘of  gypsum’ ; cp.  fluorspar.  The  modem  use  of  spar  is  due  to a  confusion  with  G.  Spat,  ‘spar’;  see  spathic and  cp.  feldspar.
=== KLN galley ===
5060:bird,  n.  —  ME.  brid,  bird,  fr.  OE.  bridd,  ‘young bird’,  of  uncertain  origin ;  possibly  in  gradational relationship  to  breed,  brood, bireme,  n.,  a  galley  having  two  banks  of  oars.  — L.  biremis,  formed  fr.  bi-  and  remus  (for  *res- mos),  ‘oar’,  which  is  cogn.  with  Gk.  Ipfacciv, Att.  £p£tteiv,  ‘to  row’,  tp&irfi,  ‘rower’,  kpcrpoq, spETpov,  ‘oar’,  OI.  aritdr-,  ‘rower’,  arttrah,  ‘oar’, OE.  rowan,  ‘to  row’,  roder,  ‘rudder’.  See  row, ‘to  propel  a  boat’,  rudder,  and  cp.  the  second element  in  unireme,  trireme,  quadrireme,  quin- quereme.  Cp.  also  remex.
6025:caboose,  n.,  i)  a  ship’s  galley;  2)  the  trainmen's car  on  a  goods  train.  —  Du.  kabuis,  fr.  MLG. kabuse,  a  compound  word,  the  first  element  of which  is  prob.  rel.  to  cabin.  The  second  element in  MLG.  kabuse  was  perh.  orig.  identical  with MLG.  bus  (=  Du.  huts) ;  see  house.  Hence MLG.  kabuse  and  Du.  kabuis  would  prop, mean  ‘cabin  house’.
15688:4)  helmet  made  of  leather.  Gk.  y dkbi)  is  prob. cogn.  with  OI.  girih,  girikd,  ‘mouse’,  L.  gUs, ‘dormouse’.  Cp.  galley.  Cp.  also  Glires,  loir, galeated,  adj.,  covered  with  a  helmet-shaped structure.  —  L.  galeatus,  pp.  of  galedre,  ‘to cover  with  a  helmet’,  fr.  galea.  See  galea  and adj.  suff.  -ate  and  -ed.
15699:galiot
15701:named  after  the  Spanish  botanist  Mariano Martinez  de  Galinsoga  (died  in  1 797). galiot,  galliot,  n.,  a  small  swift  galley.  —  F. galiote,  fr.  OF.  galie.  See  galley, galipot,  gallipot,  n.,  resinous  substance  of  certain pines.  —  F.  galipot,  of  unknown  origin. Galium,  n.,  a  genus  of  plants,  the  bedstraw  (hot.) —  ModL.,  fr.  Gk.  yotliov,  ‘bedstraw’,  coined  by Dioscorides  fr.  yaXoc,  ‘milk’  (see  galactic);  so called  by  him  because  used  in  place  of  rennet. For  the  ending  see  suff.  -ium. gall,  n„  bile.  —  ME.  galie,  gawle,  fr.  OE.  gealla, galla,  rel.  to  ON.  gall,  OS.,  OHG.  galla,  MHG., G.  galie,  and  cogn.  with  Gk.  /oAr),  L.  fel,  fr.  I.-E. base  *ghel-,  ‘to  shine;  yellow,  yellowish  green, green’.  See  choler  and  cp.  words  there  referred  to. gall,  n.,  gallnut.  —  F.  galie,  fr.  L.  galla,  ‘gallnut’, prop,  ‘a  globulous  excrescence’,  fr.  I.-E.  base *gel-,  ‘to  form  into  a  ball’.  See  glebe,  globe, and  cp.  ellagic.
15706:galleass,  n.,  a  large  three-masted  galley.  —  F. galeasse  (also  gate  ace),  fr.  It.  galeazza,  augment, of  galea,  ‘galley’.  See  galley, galleon,  n.,  a  large  ship  formerly  used  esp.  by the  Spaniards.  —  Sp.  galeon,  formed  fr.  ML. galea,  ‘galley’,  with  augment,  suff.  -on.  See galley  and  -oon.
15708:Derivative:  galleri-ed,  adj. galley,  n.  —  ME.  galei,  galeie,  fr.  OF.  galie,  fr. ML.  galea,  fr.  Byzant.  Gk.  yaAea,  which  derives fr.  Late  Gk.  yaAla,  name  of  a  seafish,  and  ult. fr.  Gk.  yxXsT],  ‘weasel’.  See  galea  and  cp.  galiot, galleass,  galleon,  gallipot, galliambic,  n.,  name  of  a  meter  in  Greek  and Roman  prosody.  —  Formed  with  suff.  -ic  fr. L.  galliambus,  ‘a  song  of  the  priests  of  Cybele’, fr.  Gk.  yaXAia^oi;,  which  is  compounded  of TdcXXo?,  ‘priest  of  Cybele’  (a  name  related  to r aXAo;,  a  river  of  Phrygia,  whose  water  caused madness),  and  (a \i$oq,  ‘iambus’.  See  iambus. Derivative:  galliambic,  adj. galliard,  adj.,  gay.  —  OF.  (=  F .)  gaiUard,  ‘strong, vigorous,  merry’,  of  uncertain  origin, galliard,  n.,  a  lively  dance  of  the  16th  cent.  — Fr.  prec.  word.
15717:Galliformes,  n.  pi.,  an  order  of  birds  including the  common  domestic  fowl  ( ornithol .)  —  ModL., compounded  of  gallus,  ‘cock’,  and  forma, ‘form,  shape’.  See  gallinaceous  and  form,  n. galligaskins,  n.  pi.,  loose  breeches.  —  OF.  gar- guesque,  metathesis  of  greguesque,  fr.  It.  gre- chesca,  prop.  fern,  of  grechesco,  ‘Grecian’,  fr. Greco,  ‘Greek’ ;  influenced  in  form  by  galley  and Gascony.  See  Greek  and  -esque. gallimaufry,  n.,  a  medley.  —  F.  galimafree,  ‘hash, ragout’,  a  compound,  whose  first  element  is related  to  OF.  galer,  ‘to  make  merry,  to  live well’,  which  is  of  uncertain  origin;  the  second element  is  identical  with  Picard  mafrer,  ‘to  eat much’,  which  is  borrowed  fr.  MDu.  maffelen, of  s.m.
15720:Gallio,  n.,  a  careless  official;  an  easy-going  per¬ son.  —  From  Gallio,  name  of  a  Roman  pro- consul  (mentioned  in  Acts,  XVIII,  17). galliot,  n.  —  A  var.  spelling  of  galiot. gallipot,  n.,  a  pot  for  holding  medicines.  —  Com¬ pounded  of  galley  and  pot.  The  orig.  meaning was  ‘pot  shipped  in  a  galley'. gallipot,  n.  —  A  var.  spelling  of  galipot, gallium,  n.,  a  rare  metallic  element  ( chem .)  — ModL.,  coined  by  the  French  chemist  Paul- fimile  Lecoq  de  Boisbaudran  (1838-1912),  the discoverer  of  this  element,  from  L.  Gallia,  the former  name  of  France  (cp.  Gallic,  Gaul).  The name  gallium  may  also  be  an  allusion  to  his
16501:grab,  n.,  a  kind  of  vessel  used  in  the  Indian ocean.  —  VArab.  ghrab,  fr.  Arab,  ghurdb, ‘raven;  galley’,  of  imitative  origin.  Cp.  Heb,
31281:Derivative:  quadripleg-ic,  adj. quadrireme,  n.,  a  galley  having  four  banks  of oars.  —  L.  quadriremis,  compounded  of  quadri- and  remus,  ‘oar’.  See  bireme  and  cp.  words there  referred  to.
31431:quinquereme,  n.,  a  galley  having  five  banks  of oars.  —  L.  quinqueremis,  fr.  quinque,  ‘five’,  and remus,  ‘oar’.  See  quinque-  and  bireme  and  cp. words  there  referred  to.
40198:trireme,  n.,  a  galley  having  three  banks  of  oars.
40809:unireme,  n.,  a  galley  having  but  one  bank  of  oars. —  Formed  on  analogy  of  bireme,  etc.,  fr.  L. unus,  ‘one’,  and  remus,  ‘oar’.  See  uni-  and  bireme. unison,  n.,  concert,  harmony.  —  MF.  (=  F.)  unis- son,  fr.  ML.  unisonus,  ‘having  only  one  sound’, compounded  of  L.  Onus,  ‘one’,  and  sonus, ‘sound’.  See  uni-  and  sound,  ‘noise’, unit,  n.  —  Shortened  fr.  unity.
```


## [2026-09-05T20:39:38.580Z] TOOL CALL #15: Bash

```json
{
 "command": "pdftoppm -f 168 -l 168 -r 300 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg168 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


## [2026-09-05T20:39:40.359Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC grep gaul ===\"; grep -n -E 'gaulo|gaulos|gāulo|ǵaulo' IEC.txt | head\necho \"=== IEC grep 'merchant ship' ===\"; grep -n -i 'merchant ship' IEC.txt | head\necho \"=== IEC grep galea ===\"; grep -n -E 'galea' IEC.txt | head"
}
```


### [2026-09-05T20:39:41.657Z] TOOL RESULT

```
total 17104
drwx------ 2 sfmqrb sfmqrb    4096 Sep  5 16:39 .
drwx------ 4 sfmqrb sfmqrb    4096 Sep  5 16:02 ..
-rw-rw-r-- 1 sfmqrb sfmqrb  752374 Sep  5 16:12 bqt362_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  624515 Sep  5 16:12 bqt362.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 1032029 Sep  5 16:13 bqt362_mid.png
-rw-rw-r-- 1 sfmqrb sfmqrb  385716 Sep  5 16:13 bqt363_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  338175 Sep  5 16:13 bqt363_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb  692415 Sep  5 16:13 bqt363.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  956665 Sep  5 16:11 bqt553_foot2.png
-rw-rw-r-- 1 sfmqrb sfmqrb  746413 Sep  5 16:11 bqt553_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb  512022 Sep  5 16:10 bqt553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  154316 Sep  5 16:07 bqt_bot389.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168738 Sep  5 16:07 bqt_bot390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  520653 Sep  5 16:07 bqt_n389.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  527392 Sep  5 16:07 bqt_n390.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   67648 Sep  5 16:29 build128.py
-rw-rw-r-- 1 sfmqrb sfmqrb  105345 Sep  5 16:30 build132.py
-rw-rw-r-- 1 sfmqrb sfmqrb   62948 Sep  5 16:36 build134.py
-rw-rw-r-- 1 sfmqrb sfmqrb   56126 Sep  5 16:29 build136b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   13830 Sep  5 16:22 build136.py
-rw-rw-r-- 1 sfmqrb sfmqrb   66341 Sep  5 16:28 build139.py
-rw-rw-r-- 1 sfmqrb sfmqrb   53260 Sep  5 16:29 build142.py
-rw-rw-r-- 1 sfmqrb sfmqrb   76989 Sep  5 16:32 build145.py
-rw-rw-r-- 1 sfmqrb sfmqrb   50861 Sep  5 16:34 build148b.py
-rw-rw-r-- 1 sfmqrb sfmqrb   21485 Sep  5 16:29 build148.py
-rw-rw-r-- 1 sfmqrb sfmqrb    7816 Sep  5 16:35 c_am2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   14765 Sep  5 16:35 c_am3.png
-rw-rw-r-- 1 sfmqrb sfmqrb   10038 Sep  5 16:35 c_empty2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4123 Sep  5 16:34 crop_am.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4986 Sep  5 16:34 crop_arabic_refs.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7702 Sep  5 16:34 crop_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb   16978 Sep  5 16:34 crop_morocco.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:18 kent.txt
-rw-rw-r-- 1 sfmqrb sfmqrb     222 Sep  5 16:30 leaf.py
-rw-rw-r-- 1 sfmqrb sfmqrb   57617 Sep  5 16:20 mk129.py
-rw-rw-r-- 1 sfmqrb sfmqrb   74680 Sep  5 16:26 mk131.py
-rw-rw-r-- 1 sfmqrb sfmqrb   33365 Sep  5 16:25 mk133.py
-rw-rw-r-- 1 sfmqrb sfmqrb   42635 Sep  5 16:29 mk140.py
-rw-rw-r-- 1 sfmqrb sfmqrb   51288 Sep  5 16:30 mk143.py
-rw-rw-r-- 1 sfmqrb sfmqrb   11831 Sep  5 16:32 node4.png
-rw-rw-r-- 1 sfmqrb sfmqrb    7427 Sep  5 16:32 node7.png
-rw-rw-r-- 1 sfmqrb sfmqrb  944060 Sep  5 16:13 oldpers_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    6054 Sep  5 16:36 p152_e0left.png
-rw-rw-r-- 1 sfmqrb sfmqrb    2672 Sep  5 16:36 p152_node2.png
-rw-rw-r-- 1 sfmqrb sfmqrb   22067 Sep  5 16:29 part0.json
-rw-rw-r-- 1 sfmqrb sfmqrb   14156 Sep  5 16:22 part1.json
-rw-rw-r-- 1 sfmqrb sfmqrb   53212 Sep  5 16:08 pg130_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74748 Sep  5 16:08 pg130.png
-rw-rw-r-- 1 sfmqrb sfmqrb  107108 Sep  5 16:08 pg130_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80793 Sep  5 16:15 pg131.png
-rw-rw-r-- 1 sfmqrb sfmqrb   46793 Sep  5 16:20 pg133.png
-rw-rw-r-- 1 sfmqrb sfmqrb   87739 Sep  5 16:10 pg134.png
-rw-rw-r-- 1 sfmqrb sfmqrb   66991 Sep  5 16:16 pg135.png
-rw-rw-r-- 1 sfmqrb sfmqrb   68320 Sep  5 16:08 pg136_300.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63248 Sep  5 16:08 pg136.png
-rw-rw-r-- 1 sfmqrb sfmqrb   45014 Sep  5 16:12 pg137.png
-rw-rw-r-- 1 sfmqrb sfmqrb   74330 Sep  5 16:11 pg138.png
-rw-rw-r-- 1 sfmqrb sfmqrb   70436 Sep  5 16:10 pg140.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63658 Sep  5 16:13 pg144.png
-rw-rw-r-- 1 sfmqrb sfmqrb   89133 Sep  5 16:09 pg145.png
-rw-rw-r-- 1 sfmqrb sfmqrb   60631 Sep  5 16:11 pg147.png
-rw-rw-r-- 1 sfmqrb sfmqrb   81770 Sep  5 16:20 pg148.png
-rw-rw-r-- 1 sfmqrb sfmqrb   72186 Sep  5 16:30 pg149.png
-rw-rw-r-- 1 sfmqrb sfmqrb  131595 Sep  5 16:32 pg151_hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb   96854 Sep  5 16:29 pg151.png
-rw-rw-r-- 1 sfmqrb sfmqrb  154426 Sep  5 16:36 pg152_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   62516 Sep  5 16:35 pg152.png
-rw-rw-r-- 1 sfmqrb sfmqrb   39131 Sep  5 16:28 pg153.png
-rw-rw-r-- 1 sfmqrb sfmqrb   63033 Sep  5 16:30 pg154.png
-rw-rw-r-- 1 sfmqrb sfmqrb   77057 Sep  5 16:32 pg155.png
-rw-rw-r-- 1 sfmqrb sfmqrb  169880 Sep  5 16:34 pg158_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   80624 Sep  5 16:34 pg158.png
-rw-rw-r-- 1 sfmqrb sfmqrb  124379 Sep  5 16:31 pg159_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   27814 Sep  5 16:31 pg159.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4694 Sep  5 16:31 pg159_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb  168057 Sep  5 16:34 pg161_600.png
-rw-rw-r-- 1 sfmqrb sfmqrb   76745 Sep  5 16:34 pg161.png
-rw-rw-r-- 1 sfmqrb sfmqrb   25911 Sep  5 16:32 pg163.png
-rw-rw-r-- 1 sfmqrb sfmqrb   59398 Sep  5 16:33 pg164.png
-rw-rw-r-- 1 sfmqrb sfmqrb   86005 Sep  5 16:39 pg168.png
-rw-rw-r-- 1 sfmqrb sfmqrb   44812 Sep  5 16:34 pg532.png
-rw-rw-r-- 1 sfmqrb sfmqrb  153161 Sep  5 16:34 pg532_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    4868 Sep  5 16:14 prt.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  333088 Sep  5 16:16 sod135_c.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1817364 Sep  5 16:16 sod135.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  101641 Sep  5 16:15 sod136_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb 1892712 Sep  5 16:15 sod136.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   56398 Sep  5 16:26 write144.py
```


### [2026-09-05T20:39:41.714Z] TOOL RESULT

```
=== IEC grep gaul ===
61:DorriN, G.: La langue gauloise. Grammaire, textes et glossaire. Réimpression de Pédition de Paris 1920. Reprint Slatkine, Geneva 1980
=== IEC grep 'merchant ship' ===
=== IEC grep galea ===
```


## [2026-09-05T20:39:47.399Z] TOOL CALL #17: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg168.png"
}
```


### [2026-09-05T20:39:47.958Z] TOOL RESULT

```

```


## [2026-09-05T20:39:47.956Z] INPUT

[Image: original 2550x3300, displayed at 1546x2000. Multiply coordinates by 1.65 to map to original image.]


## [2026-09-05T20:40:02.491Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD gac ===\"; grep -n -i -E \"^gac|gac |gacc|gač\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== PHD niyayisn ===\"; grep -n -i -E \"niyāyišn|niyayisn|nyʾdšn|niyāyi\" PHD.txt PHD_mackenzie.txt | head -20\necho \"=== NYB gac ===\"; grep -n -i -E \"gac|niyāyišn|nyʾdšn\" NYB_vol2_glossary.txt | head -20"
}
```


### [2026-09-05T20:40:02.558Z] TOOL RESULT

```
=== PHD gac ===
PHD.txt:2184:gypsum gač.
PHD.txt:5314:diz, gač, gaz
PHD.txt:5316:kāmistanī gačēn gazdum
PHD_mackenzie.txt:10452:gacen                                \t'U           yask                        \~
=== PHD niyayisn ===
PHD.txt:514:nihuftan, nihumb- [zhwptn', nhwmb- | = M, N <) cover, hide, conceal, clothe, nihumbidan [nhwmbytn'] = nihuftan. *nikóhidan, nikóh- [nkwh-ytn' | N ~] blame, execrate. ~išn: blame. ~išnīg : blameworthy, execrable. nil [nyl | N ~] indigo. nilópal [nylw(k)pl | N ~, nilēfar] lotus, water-lily. nimüdan, nimāy- [nmwtn', nmd- | M nmwdn, nm’y-, N ~] show, guide. nirfs- [nlps-] wane, decrease. ~išn: decrease, diminution. nirmad [nylmt'] profit, interest. ~ӧтапа [-’wmnd] profitable. P nisag [nys’k' | P nys’g] bright, splendid. niš- [nyi- | M nyyš-ydn, J ~] see, observe. nišān-, v. nišāstan. nīšān [ny$*x! | = M, N nisàn] sign, mark, banner. nišast [nsst! | N ~] association. nišastan, nišīn- [Y TY BWN-stn! < A V у; пт! | M nist, (nfyy-), N ~] sit. nišāstan, nišān- [Y TY BWN.stn!, 2n-; nP?stn!, nP?n- | M nf?st, (nP5y-), N ~] set, seat, plant, found. nišāyišn [n£ din! | M n$?y-, v. niSástan] foundation. nišēb [niyp | N ~] declivity; astr. dejection. ~ig [-yk'] declining. nišēm (nidm | M nšym, N ~an] seat, perch. ~ag [-k'] residence, abode. niSin-, v. niSastan. niwāģ [nw k! | M ng, N nawa] music, song, melody. *niwé [nwyk! | (N nuwéd)] good news. *niwéy-, -išn, v. niwistan, *niwéyénidan [nwykyn-ytn'] = niwistan. niwistan, *niwéy- [nwstn', nwyd- | nwyk-] announce, consecrate. —išn(ih): announcement. nixwār- [nswb’l- | M nyxw’r-] hasten. -išn: haste. niyübag [nyd’pk' | M ny’bg] becoming, fitting, suitable. ~th: suitability. niyāģ [nyd?k! | M nyg, N niya] grandfather, ancestor. niyāyišn [xyd?dšn! | N ~if] prayer, praise. niyāz [nyd?c | M ny’z, N ~] need, want, misery. —ómand [2wmnd | N ~mand] needy. ~6mandih: poverty. niyē(x)šidan, niyē(x)š- [n(y)duhš-ytn! | M nywi-, N niyófidan] hear. ~išn: hearing. І nizār [nz?l | (P nyz?*wr), N ~] weak, feeble.
PHD.txt:3199:praise (n.) afrin, burzišn, niyāyišn, stāyišn, šnāyišn.
PHD.txt:3202:prayer namāz, niyāyišn; ahunawār, āfrīnagān, hūmāst.
PHD_mackenzie.txt:3811:niyayisn [nyd'dsn' I N -if] prayer, praise.
PHD_mackenzie.txt:7317:praise (n.) afrin, hurzisn, niyayisn,          progress (y.) wihez-.
PHD_mackenzie.txt:7322:prayer namaz, niyayisn; ahunawar,                 padistadan.
=== NYB gac ===
1882:handarz-pat [hndlept'] chancellor, chief judge, head of the treasury of a province or a corporation, administrator of pro- perty: Sakistin ~ P 1:6; dar-~ 7 vàs- puhrakän the court administrator of the (royal) properties 1118-19, v. 2vdspuhrakdan and Périkhanian, REA V, 1968, 20-21 (cf s.v. väspuhr); [yztpt MLKTH-n hndrzpty KZSPrth 1. 27 = yztpt ZY b’ny(!)kn hndicpt Prs 1. 33 = Gr. v. InodtBad Bactrrcodyv avčapčaBIŠ (enumer- ated among the lower ranks of court officials). — Arm lw. handerjapet ‘the Master of the Royal household’, already in the Bible (e.g. 1 Kings 16:9 = Gr oixovéuoc), then often ‘director, manager” in different functions; when speaking of Persian officials the authors use the form anderjapet: Sakstan a. P‘aust. Buz. 4,45, mogac a. ‘the chancellor of the Magi? ibd. 4,47, or in the idiomatic Persian form Movan a. EliSe (5th c.), Hist. of the Vardans (Venedig 1838), 138. 142 (thus the MSS; the ed. han-).
2775:niyāyišn [nyd’dän'] worship, adoration, of the Fire 6621-22; yast u ~ u izišn u azbčiyišn 7019. — Renders Av. nomah-, v. namic. < *nigäyisn from gäy-, Skr gayati ‘to sing’; MPrth ng’y- pres. ‘to sing’, ng'd ‘song’ (Ghilain 86).
```


## [2026-09-05T20:40:04.492Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS gac ===\"; grep -n -i -E \"gac|gač|گچ\" SNS_pages.txt | head -20\necho \"=== TAD jabsin ===\"; grep -n -E \"جبسين|جبسين|الجبسين|جص\" TAD_pages.txt | head -20\necho \"=== TAD p20 ===\"; grep -n \"pdf page 2[0-9]\" TAD_pages.txt | head -5"
}
```


### [2026-09-05T20:40:04.561Z] TOOL RESULT

```
=== SNS gac ===
12319:                                                                                                                                                            •E5 :gac:
12328:      d, ;^;)..ii*ii-L E           SU^U« 0l^.-JjV :gackard:                           ,                                                                              :         :                           Y   ,
12345:                                                                                                        (o*** !*&       gac:                        ;>*      ^^— c-i-j^^f igacSn:
16202:                          gac 310/18                             girand 182/20            goved 325/19
16204:                          gacfin 312/6                           gired 265/17             govern 325/15
16206:                          gac kard 311/23                        girem 265/13             govend 326/1
=== TAD jabsin ===
822:‫جص ‪( -‬وجَّدص وجفسين وجس وجسين ب)وناني ‪50587‬م وفي اللائينية‬
=== TAD p20 ===
```


## [2026-09-05T20:40:18.317Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SNS entry ===\"; sed -n '12315,12350p' SNS_pages.txt\necho \"=== SNS pagetag near 12319 ===\"; awk 'NR<=12319 && /pdf page/{p=$0; n=NR} END{}' SNS_pages.txt; grep -n \"pdf page\" SNS_pages.txt | awk -F: '$1<12350' | tail -3"
}
```


## [2026-09-05T20:40:19.036Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD line 815-830 ===\"; sed -n '812,832p' TAD_pages.txt\necho \"=== TAD page tags before 822 ===\"; grep -n \"pdf page\" TAD_pages.txt | awk -F: '$1<830' | tail -3"
}
```


### [2026-09-05T20:40:20.555Z] TOOL RESULT

```
=== SNS entry ===


j !.»>,>*      :yazisn I yazdan:                         «uo « hsuO .f-t/lY^

                                                                                                                                                            •E5 :gac:
                                                                                                                                                                 "                       fVi
                                                                                                                                                                                                      &
                                                                                                                          VMtfX'S UtVb-. 1437)vlcica-                                    k»
                                                                                          i*o«J                                                                                      t
      iA/1A^       (     Y*»*»      .iij)    oxtflj^o^/f^idazisn:

                                                                                                                 tkU tf*y.. kamgm: y sBHN,
IV)                                                                                       • ,5e,                                                            in            y>         ^I*fjO
      d, ;^;)..ii*ii-L E           SU^U« 0l^.-JjV :gackard:                           ,                                                                              :         :                           Y   ,
                                           o-^U *.b«jl 5                                                                                        cu_^Uj c-,b «*b *jlj
                                     lij
                                                                                                                                                                                                       dt

                                                                                                                                                                                              \t/x*s



~t\ Ai*C -^i*3'3j-»^
                                 yezI.syaQais :j^-*S:yezI:                     —?S*                                            •   X/\&'S           tfSt&hn pifrmi         & -yazfim: &0

                                                                                                dSgha-                  L diha- icaSj^m daja-: t-
                                                                                                               :                                                              d5#      :oT ^*U
                                                   .o-i-fo :Iast, 60:                 <J 3                                                                   tv/ta^* -{GNPE 117)           cin:
                      (Jackson. 106) sastl-              :    *-   xsvasti-:    fc-
                                                                                                                                   <v>
                                                                                                        (o*** !*&       gac:                        ;>*      ^^— c-i-j^^f igacSn:
                                                                                                                                           ej                                                     *VO

                •A1/1T^ .^jo-A.ff:                sast ud sas, 66:_^>*M>»
                                                                                                              •*/i£3<"»/iAf(|3 :yast:                           yZBHWN, t       :   >*:        V^if*
         -cA* "o P >^J ^^i*fiUi
=== SNS pagetag near 12319 ===
```


### [2026-09-05T20:40:22.987Z] TOOL RESULT

```
=== TAD line 815-830 ===
‫ا معناه‬    ‫خف وحذاء وففىي الافرنسية ‪6‬طعماوع كالوش مأخوذ م ‪.‬ناليوناني ‪52‬‬
                                         ‫رجل مخنشب مرادفه خف الخفة‬

                                               ‫جرم ‪ -‬فارسيرم أي حار‬
‫ببطالي ‪#1‬ههمماع معتاه لوميمرادفه جريدة وصحيفة الاخبار‬
                                                    ‫حر نال ا‬

                                             ‫ومحضر لا تكتبه العامة في الحوادث‬
      ‫جزدان ‪ -‬فارمي « جزدان » وهو القمطر ومحفظة الاوراق والعديبة‬
                        ‫عوية ات رك دوين »روسن طريل اناق‬
‫جص ‪( -‬وجَّدص وجفسين وجس وجسين ب)وناني ‪50587‬م وفي اللائينية‬
                          ‫نامرع وهو سلنات الكلس الممتزج بالماء يطلى به‬
‫جغرافية ‪ -‬وناني مركب من‪ 3‬أي أرض و ‪0518‬م أي كتدب ووصف‬
                                                  ‫مرادفه مخطيط الارض ووصتها‬

                     ‫جذت ‪ -‬نري « جُفت »‪6‬معناه زوج خلاف الفرد‬

‫حمل ‏‪ ٠‬فارمي « شتال » وهو نوع من الذئاب صغير الثة وفي اللاتينية‬
                      ‫فنالا نانع أيكلت ذهبي ويرجمته بعضهم بانآوى‬

‫جلاب وجُلاب ‪ -‬فارسي معناء ماء الورد ويزاد به سكر أوعل عفد‬
=== TAD page tags before 822 ===
```


## [2026-09-05T20:40:34.251Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT search vicica variants ===\"; grep -n -E \"vi[cčĉ]i[cčĉ]a|vTcica|vicica|vlcica|vIcica\" BRT.txt | head -20\necho \"=== BRT 'Mörtel' ===\"; grep -n -i \"mörtel\\|mortel\" BRT.txt | head -20"
}
```


### [2026-09-05T20:40:34.312Z] TOOL RESULT

```
=== BRT search vicica variants ===
=== BRT 'Mörtel' ===
23946:•  j.  vi6ida-  n.  'Kalk,  Gips,  Mörtel':  asa- nafraa  . .  'caih/a  . .  tütuxha  (sd.)  V.  ö^.  5 1 ;
```


## [2026-09-05T20:40:35.774Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== TAD leaf of line 822 ===\"; awk 'NR<=822{n+=gsub(/\\f/,\"\")} END{print \"formfeeds before line 822:\", n}' TAD_pages.txt\necho \"=== TAD total leaves ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' TAD_pages.txt\necho \"=== head of TAD_pages ===\"; head -5 TAD_pages.txt"
}
```


### [2026-09-05T20:40:37.860Z] TOOL RESULT

```
=== TAD leaf of line 822 ===
formfeeds before line 822: 23
=== TAD total leaves ===
86
=== head of TAD_pages ===
                                     ‫الف‬
           ‫ياكابىاللبناك‬  ‫‪َ8‬‬
                       ‫نببى‬
```


## [2026-09-05T20:40:46.642Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '23930,23960p' BRT.txt\necho \"---- nearest column numbers ----\"; awk 'NR>=23800 && NR<=23990' BRT.txt | grep -n -E \"^ *1[0-9]{3} *$|14[0-9][0-9]\" | head -20"
}
```


### [2026-09-05T20:40:48.520Z] TOOL RESULT

```
•  j.  vi-kant^e  Inf.:  s.  unter  *kantSe.
•  j.  *vi-kaya-''  m.  'Zeuge':  'yB  F.  8;  — tat  tkaisaheisA.)  tat  'yehe  F.  27  b.
Zum  V.  kay-;  eig.  'Scheider',  näml.  der  Tat- sachen.—  arm.  LW.  viay,  HGU.IF.^119. — Pa.:  göt.li'-l.  —  ')  Hds.  ziiiay'  und  viiai',  — >)  VgL  zLes.  des  Worts  und  zu  den  übrigen Wörtern  für  'Zeuge'  Bthl,  IF,  /2.  95.
•  j.  vik^rvt-uitäna-  Adj.  'das  Leben,  die Lebenskraft  zerstörend':  fraeäbaotaaAfm (sd.)  «ifl>j/w  'n>m  V.5.37,  y.  12,  z^.  i.
*vi-k3tii-  Adj.  eig.  'entzweimachend',  lum  V.
'kar-;  vgl.  ai.  vikala-  Adj.  'ungestalt'  (woiu IF.  J.  194I.  ~  Pü.:  yut  Ürrintfi  yin.  — O  S.  kar)!-.
dby  Google
1437
vi£ä
gibt,    ohne    dass  Blut  fliesst  (vgl.  unter  la^ai,'
vtkaai-);  sva.  :^ara-  tar    j'f.,  Ed.
Pii.j  vixrün');  j/ixtünömaiui'}.  —  ')  Zar  Ver- schiedenheit dei  Bedeutung  s.  zB.  ai.  viccias- Adj.  —  •)  S.  zu  xrita-.
•  j.  vicSä  Adv.  'weg";  F.Ä
Eig.  IS.  einer  Ableit.  aus  m;  S  //f.  —  Be- stimmung ganz  unsicher,  da  das  Wort  aus dem  Zusainmenhuig  geriisen  ist.  Vll.  stammt es  aus  V.  2.    lo;  s.  Pu.  —  Pü. :  a/Ä
•  j.  vi-£ar3na-  n.  Trennungsstelle,  Stelle, wo  sich  der  Weg  teilt":  pa%amcS  *'rjnä'> .  .  pahqmia  hanjamana  Y,  4-3.  i ;  — fakqm  '.  .  paiti  'na  Yt  //.  4,  Vyt.  54.
Zum  V.  iiar-,  —  ai,  vicarana-  d.  'Bewegung'.  — Yä.:yul  rawünii.  —  0  So  Pt4;   NA.  •rani.
•  j.  vi6ida-  n.  'Kalk,  Gips,  Mörtel':  asa- nafraa  . .  'caih/a  . .  tütuxha  (sd.)  V.  ö^.  5 1 ;
—  dva  äim  nara  tsSi^e  .  .  upa.siambtm (sd.)  'ialsva  dim  nidai^yan  V.  (V.  10.
Et.?  —  Pü.  (zu  V.  6):  ga^'),  (w  V.  *): fehlt.  —  ■)  D.  i.  'aus  .fa/  (=  np.  ^-a/'Kalk') bestehend';  s.  dazu  Hbu.  PSt.  90.
•  g.  vi-didyäi  Inf.  'zu  unterscheiden':  tat möi  vic'  vaocä  .  .  viduyl  vohä  mana^ihä mSneS  daidyäl  ythyä  mä  >nlii{sA.)  "davon gib  mir  Kunde  - .,  damit  ich,  o  VM.,  1 unterscheide,  begreife  und  {im  Gedächtnis) ' behalte,  . ."  Y.ji,  5;  —  frö  vh  fralsya  . . mrai(i  (sd.)  .  .  fr>s  vlcidyai  yd^a  l  srä- vayaiinä  ". .,  damit  wir  richtig  unterschei- den können,  wie  wir  sie  verkünden  sollen" Y..^.6.
Zum  V.  iay-.  —  Pü. :  vifart.  {räsl)  afi  vianim.
•  g.  vi-ciiha-  n.  i)  'Scheidung,  Sonderung': aisqmcJt  ä  ahm!  %wahml  mOMda  °^ffi  aipi "von  ihnen  werde  ich,  o  M.,  künftig  von  dir  [ geschieden  werden"  Y. 32.  8 ''.  2)  'Ent-  , Scheidung':  tal  msi  xraiSus  manar»hascä\ '%int  "das  ist  meines  Verstands  und  Sinnes  | Entscheidung"  Y.  46.  iS;  ^  mit  Gen.  obj.: sraotä  *g}us'.<lii'  (sd.)  vahistä  .  .  ävar>na •%aAy3  "das  Beste  . .  für  die  Entscheidung zwischen  den  beiden  Glaubensbekennt- nissen"   Y.  JO.  a'>.  [Vt  12. 1:  lies  vl-
Zum  V.  iay..  —  PS.  (dRn.):  aj>f  vidi,  api viätitm,    apf  vicinisn.     —     D  Wärtl.:    'ab    bis
271  c
•  j.  vi-CiSra-  Adj.  'ausgezeichnet,  hervor- ragend': kat  asti  mq%rak<  sp>ntahe  ars.- äatsm  .  .  fraidabm  .  .  *'r?m  "'   Vt  12.  i ;
—  kva  (sd.)  täcUgSul  'ra  paiti.barS  *ratu- /ris  H.  1081^);  —  'r?mi'ii  F.2jb(?)'>.
ai.  vicUra-  Adj.  —  Pü.  (zu  F.);  afie  paitäkih, (zu  a.y.  ausgelassen.  —  O  NA.  -äj»,;  s.  aber F  I,  J  10.  —    »)  S,  iSt  Wkst  SBE.  ^/.  480.
•  j.  tßtn  barasma  aycuaisa  . .  fraHndhwan vidinaOTwar«  .  .  frataraiibyS  (sd.)  raocä Yt/j.  55.         Ob  Adv.?
Geringe  Stelle.     Vgl.  zu  rrahaa%viari.
•  j.,  g.  vi-Cira-  Adj.  (fem.  'r3-)  i)  'ent- scheidend, die  Entscheidung  treffend':  hvS 'rS  ahurS  "er,  Ah.,  hat  die  Entscheidung" Y.  2g.  4;  —  fravasayS  .  .  yä  .  ,  ranmS vivaitTs  °ra  Yt  13.  40.  a)  'der  sich entschieden,  die  tfberzeugung,  Gewissheit gewonnen  hat':  ys  vä  xsayqs  adqs  driiä  . . °rö  Aas  ".  .  wenn  er  dessen  sicher  ist" V.4tf.S".
Zum  V.  iay:  —  Vgl.  micoista:  —  np.  vaür 'Gelehrter' ;  ai.  vgl.  nidtä-  Adj.  —  Pfi.  (zu  Y. 2g) :  ape  vieitär,  erl.  1  kär  u  dätasiän  afl  viciiüt, (zu  Y.  46) :  vifarl,  erl. :  röhiai  an  niart  veh muri.  —  O  Unrichtig  Ggr.  OK.  450.
---- nearest column numbers ----
24:143^  vouru.n«inah-  —  vohu.b9r«ti^  1433
63:1433  vohu.fryaaa-  —  "i
95:I43S  vohvavant-  —  Wxrümant-  1436
138:1437
170:1439
```


## [2026-09-05T20:41:31.935Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v2 جبسین ===\"; grep -n \"جبسین\\|جبسين\" BQT_v2_pages.txt BQT_v1_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt 2>/dev/null | head\necho \"=== BQT زورق ===\"; grep -n \"زورق\" BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head\necho \"=== BQT نیایش ===\"; grep -n \"نیایش\" incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt 2>/dev/null | head"
}
```


### [2026-09-05T20:41:32.032Z] TOOL RESULT

```
=== BQT v2 جبسین ===
=== BQT زورق ===
incoming/BQT/BQT_v4_pages.txt:7734:(زورق ) , 888 (قنات » ناودان ؛ راه آب ) « ژابا صس 4۱۷ ‎٩‏ - رك : ناودان .
BQT_v2_pages.txt:3183:‫جوسق ‪ -‬بفتح اول بر وزن زورق ‪۰‬‬                                   ‫که ارگیل باد » معرب آن‬
BQT_v2_pages.txt:30008:  ‫زورق‬                                                                                                    ‫ت‬
BQT_v2_pages.txt:30090:                                                              ‫زورق سیمیی» کنابه از ماه یکب‬
BQT_v2_pages.txt:30116:         ‫رك ‪ :‬زورمندی (ح)‪: ‎‬‬         ‫‪۴‬‬                 ‫رك ‪ :‬زورق‪.‬‬     ‫‪۴‬‬            ‫رك ‪ :‬زورقی‪.‬‬    ‫‪٩‬‬
=== BQT نیایش ===
incoming/BQT/BQT_v5_pages.txt:3722:عبادت » نیایش .
incoming/BQT/BQT_v5_pages.txt:3727:کردن » نیایش کردن » خدمت کردن .
incoming/BQT/BQT_v5_pages.txt:6008:ومطلوب بود » وایرآنیان زرتشتی در نیایشهای خود از اهورمزدا در ردیف
incoming/BQT/BQT_v4_pages.txt:12327:نیایش ۱ - بر وزن ستایش » بمعنی را * - بکس اول بروزن گیراء بلفت
incoming/BQT/BQT_v4_pages.txt:12339:ماه ۰ آب وآتش بترتیب خورشید لیایش » مهر نیایش .» ماه لیایش » اردویسور بانو نیش و آتش
incoming/BQT/BQT_v4_pages.txt:19294:اسح, دونیایش- است بنام « هورخش کبیر» و «هورخش صفیر». انگارنده « هورخش کپیر > را در
```


## [2026-09-05T20:41:34.017Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM zawraq ===\"; grep -n \"زورق\" AFM_pages.txt | head\necho \"=== PLA zawraq ===\"; grep -n -i \"zawraq\\|zauraq\\|زورق\" incoming/PLA/PLA_pages.txt | head\necho \"=== LKT galee/galeere ===\"; grep -n -i \"galee\\|Galeere\\|gaulos\" LKT.txt | head"
}
```


### [2026-09-05T20:41:34.089Z] TOOL RESULT

```
=== AFM zawraq ===
2429:وقال في التاج في ترجمة السنبوق وهي لغة في السلبوك :«زورق سفر يعمل في سواحل
=== PLA zawraq ===
=== LKT galee/galeere ===
3329:'Gefäß',  ebenso  tk.,  sowie  ma^una  'Schiff (Kelekian  Kämüs  1093  a];  hieraus  it. maona  'tk.  Galeere',  frz.  mahone,  maho- ne,  kat.  sp.  mahona  'dass.'.  [DE  299. Devic  DEt  155.    Eguilaz  442.
```


## [2026-09-05T20:41:42.294Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v2_pages.txt incoming/BQT/BQT_v4_pages.txt; do echo \"== $f ==\"; grep -n \"pdf page\" $f | head -3; done\necho \"=== v2 tags around 30008 ===\"; grep -n \"pdf page\" BQT_v2_pages.txt | awk -F: '$1<30010' | tail -2\necho \"=== v4 tags around 12327 ===\"; grep -n \"pdf page\" incoming/BQT/BQT_v4_pages.txt | awk -F: '$1<12330' | tail -2"
}
```


### [2026-09-05T20:41:44.678Z] TOOL RESULT

```
== BQT_v2_pages.txt ==
== incoming/BQT/BQT_v4_pages.txt ==
1:[pdf page 1]
2:[pdf page 2]
23:[pdf page 3]
=== v2 tags around 30008 ===
=== v4 tags around 12327 ===
12282:[pdf page 306]
12320:[pdf page 307]
```


## [2026-09-05T20:41:48.966Z] TOOL CALL #28: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:2224 2>&1 | head -60"
}
```


### [2026-09-05T20:41:56.536Z] TOOL RESULT

```
(no exact page map; using offset -1917 -> pdf page 307; check the printed number and re-run with --pdf-page if off)
REF: BQT:2224  PDF: data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf page 307  OCR-lang: fas

لیایش <<
وقت غیار کردن بدان چسبند وزورکنند تا کاو | بروزن مردمان » سنگینیی باشد که درخواب بر
آهن بیشتر بزمین فرو رود و زمین را بیشتر | مردم افتد و عربان عبدالجته و کابوس خوانند -
بشکافد ۰ و خیش چوبی است که برکردن کاو | و بمعنی صرع هم آمده است و آن علتی باشد
زراعت گذارند . معروف .
نیایش ۱ - بر وزن ستاش » بمعنی یر * - بکس اول بروزن کیرا, بلفت
آفرین و تحسین - و دعائی باشد که از روی | زند و پازند آتش راکویند وبمربی نار خوانند.
قرع وزاری کنند ۴ - وبمعنی مهربانی هم‌آمده نیرم ۹ - بفتح اولورای بی نقطه‌وسکون
است . ثالی ومیم, نام نربمان است که پدرسام جد رسام
نیپال ۴ بفتح اول وبای فارسی‌بروزن | باشد . ۱
احوال ‏ نام محلی وجابی است که مغك خوب نیرنج ۷ « بکس اول بر وزن پیرج .
از جاآورند وبمدازمعك تبتی‌معك نیپالی‌بهترین | بمعنی‌مکن وحیله وسحر وافون وطلسم‌وجادویی
اقام معك است . باشد , وبعضی کوبند لیرنج معرب لیرنگه‌است.
نیدلان ۴ - بفتح اولولام بالف کشید. نیرنگ ۸ - باکاف فارسیبروزن‌و+منی

- پهلوی 89291907 ( پرستیدن ) - بیز 81802119080 ۰ ایرانی باستان -
طونم . ساسکریت 8878 (آواز خوادن) . ۶« نیب رکه ص۱۵۸*.

۴ - در جزو ادعيةٌ خرده اوستا » پنج نماز وآفرین راکه راجم است بخورشید » مهر »
ماه .آب وآتش بترتیب خورشید لیایش » مهر بیایش .. ماه لیایش » اردویسور بانو تیایش و آش
نیایش نامند. «پورداود. خرده اوستا س۰۱۰۳: «لیایش » دعا وآفرین بود. فردوسی (طوسی) گوید:

همیدون بزاری لیایش کرفت جهان آفرین را ستاش کرفت».

« لغت فری ص ۲۰۹ .۰

۴ «دلوم216 « آن2م316 , ام منلکت كوچك متقلی است در شمال هندوستان »
دز منطفهٌ هیمالیا , بین تبت از جهت شمال وکشور هندوستان از سه جهت دیگر » مساحت آن
+ کیلومترمربع وقریب ۳۰۶۶۶۹۰ سکنه دارد. ۴ - عربی است و درقاموسآورده
« رشیدی » « اللیدلان بکسرالنون والدال وتشم‌الدال : الکابوس . وقیل شیء مثله .»

8 از ]ود رید را که بمعنی‌آتش امت 0811078 . ۵82112 ۰ 28118
خوانده‌اند » بعش محققان صحیح آرا روژیه داسته‌اند که 31۲92 خوانده شود . رك :
« یونکر ص ۲:۷۵ + وقی : نار (عربی) [جمع : لیران]: <* نربمان (ء.م.) وازهمان
رشه. ۷ - معرب « بیرنگه » (ه.م.) , رك : دزی ج ۲ اس ۹۳۱: لیرنچات ۳ نارنجیات .

۸ - پهلوی 817808 « تاوادیا ۲:۱۹۳*. نیرنگه ( در پهلوی ) بمعنی مراسم دینی‌است
ولیراج و جمع‌آن لیرنجات معرب اين کلمه است. در نخ خطی سنا ووسپرد و وندیداد که در
ابران نوشته شده » لیرنگها (مراسم دینی ومناسك مذحبی) بسیارضبط شده. بسیاری ازادءةٌمشتصر
چه بزبان اوستایی وچه بزبان پهلوی وپازند » هم تبرنگه نامیده شده , چنانکه : برنگه آش.
لبردگه کستی نو بریدن . لیرنگه دست شو , نبرنگه کستی بستن . برای این لیرنگها تأثیرات
فوق طبیعی قائّل شده‌اند و از برای هر پیش آمد يد ودفع هر آسیبی‌بیبرنگه مخصوصی‌خوأنده‌میشدد.

بقیه در حاشةٌ صفحةٌ بمد
```


## [2026-09-05T20:42:09.182Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1044 2>&1 | head -45"
}
```


## [2026-09-05T20:42:09.792Z] TOOL CALL #30: Bash

```json
{
 "command": "python3 tools/ref_page.py BQT:1776 2>&1 | head -45"
}
```


### [2026-09-05T20:42:11.643Z] TOOL RESULT

```
no scan of BQT covers printed page 1044 (see 'scans' in refs_online.json)
```


### [2026-09-05T20:42:18.741Z] TOOL RESULT

```
REF: BQT:1776  PDF: data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf page 573  OCR-lang: fas

۱ کجیل ۱۷۷۹
محله‌ایست در تبریز , و لام قبرستانی هم هست | علیه‌الرحمه درآن قبرستان است ‎٩‏ ۰
بیان ششم
درکاف فارسی با جم فارسی مشسّمل‌برسه هت
گچ۲ < بفتح اول وسکون ثانی, خاکی | بکمانچه۴ -
اشد که آنرا پزند وبدان خانه سفیدکنند . گلچه؟ - بنتح اول وئانیمخفف: کیرا
گچات - بکر اول. بروزن و معنی | کوبند که زبان اوبفساحت جاری نباشد ؛ وباین
غجك است وآن سازی‌باشد ممروف ومشهور(٩)‏ | معنی باتشدید ثانی هم بنظر (۲)آهده است .
بیان هفتم
در کافی فارسی با دال احد مشتَمز اس دوازده لفت
کل - بفتح اول وسکون نانی » بمعنی کوبنده . 4
کدا باشد که گدایی کننده‌است- و کدایی رایز گداده - بنم: اول بروزن‌شمارهبالاخانٌ
() چش : - ومشهور . (۲) خم ۱۱:,- بنظر .
- اکنون محله‌ای درتبریز بنام محلهٌ کجیل اززهی هست. وقبرستان گجیل هم‌ممروف
بوده؛ واباغ گلتان» درمحلآن قبرستان ایجاد شدماست . تذ کرمولف‌راجع بقبرشمی‌تبریزی‌قابل
تخل است. ۴ - پهلوی » پازند 826 . معرب‌آن جص, سربانی 86858 ۰ كلمةٌ عریی - فارسی
حسن 80510[ (8(05010) ازبونانی8۳0908. 8121091808 آمده «هوبشمان *۸۹» ور4:
امشق ۰۸۹۰ کردی 811762 «زابا ص۳۹۲ > و8360 (آهك) «ژابا ص۳۵۷ ؛ در اکدی82550 <-
جیصین,کلی«معجمیات عربیه - سامیه ص۲۱۸ ور: کج. ۴ نچك ۳ غرل «فرهنگه نظام»:
زهر مو چو ن گچك: میکرد فرباد دل اصحاب میگشت از غم‌آراد,
خوارزمی « فرهنگه نظام » .
ای - رد رشیدی. در سیزوار 756 بمعنی شخ سکم عقل تاضیح ونیز لفظی است که‌با
آن بزها را میخوانند ۰ ۸« فرهنگه نظام » - 8 - بمعنی گدایی است » رك :کدا :
شکرت چو آرزو شد ز لب شکر فروشش چو عبای دوس زو تر ز شکن فروش کدکن.
مولوی «فرهنگه‌نظام». ورك : رشدی .
- بکسر اول (در لهجه مرکزی) » دراوستایی 820 (خواهش کردن.خواستن).
هندی باستان 811411 ( من خواهش میکنم ) « بارتولمه 2۸۷ > » کردی 2 42 ( کدا)
«زابا ص۳۵۷ 2 » کیلکی 4 - قس : عربی : تکدیه , و اکداه؛ آنکه از دیگران چیزی
(پول » خوردلی ویوشیدی) برای رفع حاجت طلید : «گفت (ملك) این گدای شوخ مبذر را ...
برانید . » «کلتان ص ۳۱ . بقیه درحاشيةٌ صفحهٌ ۱۷۷۷
```


## [2026-09-05T20:42:34.237Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '29995,30030p' BQT_v2_pages.txt\necho \"=== nearby footnote lines with زورق ===\"; sed -n '30080,30120p' BQT_v2_pages.txt"
}
```


### [2026-09-05T20:42:34.309Z] TOOL RESULT

```
                                                                                       ‫رك ‪ :‬ژواغار ‪.‬‬          ‫‪۴‬‬
      ‫زحلق‌مرخ‌باعت فروچکیدی گل(خون‪.‬دهشدا)‪.‬‬                     ‫® ‪ -‬زواله‌اش‌چوشدی‌از کمانگروهه‌برون‬
  ‫‪۲‬‬    ‫«لفت فرس‪٩۳۰۵‬‏‬   ‫کسایی مروزی‪.‬‬

                ‫‪( ]612۲۷ = ۷‬فر) «لك ‪۲‬س ‪. )۵۲۲‬‬                                   ‫‪.‬‬     ‫فنا»ن‬
                                                                                          ‫زبا‬
                                                                                            ‫‪ ۷‬رك ‪ :‬ز‬
  ‫‪۰‬‬     ‫‪ °‬رك‪ :‬لفت فرس ص‪41‬‬                     ‫رك‪ :‬زاووق‪. ‎‬‬              ‫‪٩‬‬            ‫زیانه (ه‪.‬م‪‌ ).‬‬       ‫ص‬   ‫‪۸‬‬

           ‫«رواله» (هم‪).‬‬    ‫‪ -‬ظ ‪ ,‬مسحف‬       ‫‪۱‬‬       ‫‪۰‬‬    ‫‪۰۳۱‬‬       ‫ص‬   ‫‪ ۶‬زوار» است ‪ .‬رك‪ :‬لفت فری‬             ‫مصحف‬     ‫وظ‬

      ‫‪۴‬هز‪ .20۵2,20012 .‬بپلوی ‪ 012111‬دزد« بودکر‪ ۸۰۱‬قراتمجاغلیط‪«2068‬رهارله‪.*۲۵۲‬‬
  ‫زورق‬                                                                                                    ‫ت‬
                                                                                                          ‫اع‬‫سم‬
 ‫زود خیز‪ -‬زود مملوم است » با خای‬                            ‫کسی‌است که حیزی و مخنشی را اوبنانهاد و ازو‬
‫نقطمدار بتحتاتی‌رسیده ویزای اقطهدار زده‪ ,‬کنابه‬                                                   ‫رانیده شد ‪۱‬‬

                  ‫از فرمانبردار وخدمتکار باشد‪.‬‬              ‫رو به = صم اول وفتح مای‌فارسی‪ .‬بلفت‬
‫زود سبره کنابه کایز‌است که از‬                                ‫نزدوپازند(‪)۱‬؛به‌عنی‌قرض بباشید‌ودبعنر‌خوانند‪.‬‬
             ‫زودسر شود ودلگر کردد‪.‬‬         ‫صصت‬
                                                            ‫‪ = ۴‬با ثالی مجپول‌وبای‌فارسی‬         ‫دون‬
                                                            ‫‪ ۰‬حربة مردم گیلان است» وان‬           ‫بر ورن چوبین‬
                        ‫وصاحب جمعیت باشد ‪.‬‬                  ‫ران دوشاخ باشد و در‬          ‫کده‬
                                                                                           ‫نیز کوچکی بو‬
 ‫رور = بفتح‌اولوثانی بروزن نظرءیمعنی‬                        ‫و نام سرکاوی‬    ‫‪-‬‬   ‫فدرم بدان جنگ مکرده‌اند‬


‫زبر است ‪ ۱‬که بالا باشد چه درفارسی بای ابجد‬                                                            ‫‪.‬‬   ‫هم هت‬


                  ‫و واو بهم تبدیل مییابند ‪. ۷‬‬               ‫روخ ‪ - ۴‬بروزن شوخ ‪ .‬کوشت‌پاره‌ای‬
‫رورا = بفتح اول وسکون انی و وای‬                             ‫که بر تن مردم بروید و آن را بسربی ولول‬
‫کشده ‪ ۳‬دح له بغداد ‪۳‬‬       ‫(( بالف‬      ‫بی نقطه‬                                                       ‫خوانند ‪۲#.‬‬
‫کوبندو بعضیکوبند زورا‪,‬فداداست وعربی‌است‪. ۷‬‬                  ‫دواشنا ؟ ‪ -‬باشین نقطه‌دار ونون بر‬‫‪ ۱‬ز‬
‫رورانه* = فبتحر‌وآوزلن‌همخانه‪ ,‬بندی‬                         ‫وزن زود ار جا » نذر و نذوراتیرا کونند که‬
=== nearby footnote lines with زورق ===
 ‫دورن = بنالی مجهول وفتح ثالث بر‬                              ‫ردودق ددلی ک=نابه از خورشيد‬
‫ونام یادشاهی‬   ‫_‬   ‫‪ ۰‬نام ولامی اسخ ‪۵‬‬           ‫وزن سوزن‬
                                                                                                  ‫عالم آراست‪.‬‬

 ‫لیزبوده ‪-۷‬وبکسرئالث بروزن»ومن؛بمه‌نی‌درم‌باشد‬
‫‪.۷‬‬      ‫است‬
          ‫‌هشت‬
             ‫هو‬‫بچهل‬
                  ‫حن‌‬
                    ‫کهبعربی‌درهمکوبند وآ‬
                                                              ‫زورق سیمیی» کنابه از ماه یکب‬
‫اول و سکون الی‬          ‫م‬    ‫رور نی =‬
‫وئالت ونون بتحتالی کشنده ‪٩‬‏ بلفت‌ز اد ویازاد (‪)۱‬‬
                                                             ‫رورفی‪ ۲‬حنوعی اکزلاه قلندران ‪.‬اعد‬
                                                                                     ‫وآن شیبه است مکشتی ‪۱‬‬
‫وبفتح‬    ‫رکبه خوانند ‪- ۸‬‬    ‫و هر ی‬       ‫را گوند‬      ‫زاو‬


         ‫الث بروزن سوزنی هنوب بزوزن باشد‪.‬‬
 ‫زوره = بروزن کوزه »‪.‬گربه وموبه‬
                              ‫ر‬                               ‫‪:‬ممنی صاحب فوت و توانا باشد چه‌مند بمعنی‬
                               ‫و توحده زا گویتن ً‬


                                                              ‫ه با نون ومیم‌بروزن نبرزین»‬        ‫رلوبدم‬
                                         ‫‪۲ ٩‬‬     ‫‪۰‬‏‬



 ‫روس د بفتح اول وانی بروزن حش»‬
                                                              ‫پارچه‌ای گرویاند کهبادام خاسی ازجالب پعت‬
‫و بضم انی بروزن خمش نیز گفته‌اند ‪ -‬وباثانی‬                                              ‫برگریبان جامه دوزند‪.‬‬

 ‫رودو‪3‬م = بنم اول ونالك وفتح‌دال | مجهول بروزن‌هوش» بممنی خشمکین ونرش‌روی‬
 ‫ابجد وسکون میم » بمعنی زور و قوت و تکبر ‪۱‬وتندخویو کج طبیمت وزودرنج باشد‪-٩‬ولیرومند‏‬
                                                                          ‫(‪ )۱‬چك ‪ :‬ژند و باژند ‪.‬‬
         ‫رك ‪ :‬زورمندی (ح)‪: ‎‬‬         ‫‪۴‬‬                 ‫رك ‪ :‬زورق‪.‬‬     ‫‪۴‬‬            ‫رك ‪ :‬زورقی‪.‬‬    ‫‪٩‬‬
     ‫از بر ‪-‬اخته‌های فرقهٌ آذر کیوان ‪ -‬و ایز اکمتابی است ازین فرقه «درشناختن‬                       ‫‪۴‬‬
     ‫آغاز و انجام وزمان ر جهان وجهایان وشناخت راه نيك از بد و غیرها » کفتار ابراهیم زردشت‬
      ‫پیغمبر ايران (!) ترجمه‌و توضیح آذر پژوه اسپپالی ‪ ۰‬واين کتاب در «آ ین هوشنك » بمال ‪۲۹۲۱‬‬
     ‫‪ - 6‬شهر کی ازحدودنشابور‪«.‬حدودالعالم ‪.*۷۲۵‬‬                       ‫بجاپ سنگی رسده است ‪.‬‬        ‫فمری‌درتهران‬
```


## [2026-09-05T20:42:49.647Z] TOOL CALL #32: Bash

```json
{
 "command": "python3 tools/fetch_source.py --help 2>&1 | head -20; grep -n '\"AEC\"\\|AEC' data/verification/sources/refs_online.json | head"
}
```


### [2026-09-05T20:42:51.909Z] TOOL RESULT

```
Save a web source used during verification, for later cross-checking.

    python3 tools/fetch_source.py <URL> [--note "why it was fetched"]

Downloads the URL, converts the HTML to plain text, stores it as
data/verification/sources/web/<sha1(url)>.txt and appends a line to
data/verification/sources/web/index.jsonl  ({url, file, fetched, bytes, status, title, note}).
Prints the stored path. Re-fetching the same URL within a day is skipped.
```


## [2026-09-05T20:42:58.600Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/%CE%B3%CE%B1%CF%85%CE%BB%CF%8C%CF%82\" \"https://en.wiktionary.org/wiki/%CE%B3%CF%8D%CF%88%CE%BF%CF%82\" \"https://www.etymonline.com/word/galley\" \"https://en.wiktionary.org/wiki/%D8%B2%D9%88%D8%B1%D9%82\"; do\npython3 tools/fetch_source.py \"$u\" --note \"page 168 verification (gaulos/gypsos/galley/zawraq)\"; done 2>&1 | tail -20"
}
```


### [2026-09-05T20:43:03.240Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/84feb0138152f73c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/2e2945210a9d3844.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ec1e788ca9cbbd63.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ee856515010ca429.txt
```


## [2026-09-05T20:43:06.336Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## gaulos\"; grep -n -A25 -i \"Etymology\" 84feb0138152f73c.txt | head -50\necho \"######## gypsos\"; grep -n -A25 -i \"Etymology\" 2e2945210a9d3844.txt | head -40"
}
```


### [2026-09-05T20:43:06.404Z] TOOL RESULT

```
######## gaulos
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Inflection 
72-
73- 1.3.2 
74- Descendants 
75-
76- 1.4 
77- References 
78-
79- Toggle the table of contents 
80-
81- γαυλός 
82-
83- 4 languages 
84-
85- Ελληνικά 
86- Latviešu 
87- Malagasy 
--
147: Etymology
148- [ edit ] 
149-
150- A connection with γύαλον ( gúalon ) , γωλεός ( gōleós ) , Old Norse kjóll ( “ ship ” ) has been considered. But this word can be considered, as γαῦλος ( gaûlos ) denoting a Phoenician merchant-ship, as being via Phoenician or a near language from Akkadian 𒄖𒌌𒇻 ( gullu , “ a container ” ) , 𒄖𒌌𒆷𒌅 ( gullatu , “ ewer ” ) , a vinicultural word of unascertainable non-Semitic origin, being via its variant 𒄣𒇷𒌋 ( qulliu , “ a bowl ” ) the source of Biblical Hebrew גֻלָּה ( gullāh ) , Ugaritic 𐎂𐎍 ( gl ) , Aramaic קוּלְתָא ( qulləṯā ) , Arabic قُلَّة ( qulla ) , جُلَّة ( julla ) , Classical Syriac ܩܽܘܠܬܳܐ ( qulləṯā ) , which passed into Latin culullus ( “ wine jug ” ) and into Ancient Greek κόλλαθον ( kóllathon , “ a unit of liquid measure used in Syria ” ) .
151-
152- Pronunciation
153- [ edit ] 
154-
155- IPA ( key ) : /ɡau̯.lós/ → /ɣaˈβlos/ → /ɣaˈvlos/ 
156-
157- ( 5 th BCE Attic ) IPA ( key ) : /ɡau̯.lós/ 
158-
159- ( 1 st CE Egyptian ) IPA ( key ) : /ɡawˈlos/ 
160-
161- ( 4 th CE Koine ) IPA ( key ) : /ɣaˈβlos/ 
162-
163- ( 10 th CE Byzantine ) IPA ( key ) : /ɣaˈvlos/ 
164-
165- ( 15 th CE Constantinopolitan ) IPA ( key ) : /ɣaˈvlos/ 
166-
167- Noun
168- [ edit ] 
169-
######## gypsos
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
69-
70- 1.3.1 
71- Declension 
72-
73- 1.3.2 
74- Derived terms 
75-
76- 1.3.3 
77- Descendants 
78-
79- 1.4 
80- References 
81-
82- 2 
83- Greek 
84-
85- Toggle Greek subsection 
86-
87- 2.1 
88: Etymology 
89-
90- 2.2 
91- Noun 
92-
93- 2.2.1 
94- Declension 
95-
96- 2.2.2 
97- Further reading 
98-
99- Toggle the table of contents 
100-
101- γύψος
```


## [2026-09-05T20:43:07.658Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"######## galley etymonline\"; sed -n '1,80p' ec1e788ca9cbbd63.txt\necho \"######## zawraq\"; grep -n -B3 -A25 -i \"Etymology\" ee856515010ca429.txt | head -60"
}
```


### [2026-09-05T20:43:07.821Z] TOOL RESULT

```
######## galley etymonline
URL: https://www.etymonline.com/word/galley
FETCHED: 2026-09-05T20:43:02Z
STATUS: 200
TITLE: Galley - Etymology, Origin & Meaning

Galley - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 

 Quick and reliable accounts of the origin and history of English words. Scholarly, yet simple.

 About
 Who Did This 
 Sources 
 Introduction 
 Links 

 Support
 Premium 
 Patreon 
 Donate with PayPal 
 Merch 

 Apps

Get Chrome Extension 

Get iOS App 

Get Android App 

 Dark
 Auto
 Light

 Terms of Services Privacy Policy 

 English (English) 
 © 2001–2026 Douglas Harper & Talia Felix 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of galley 

 galley (n.) 

 13c., "seagoing vessel having both sails and oars," from Old French galie , galee "boat, warship, galley," from Medieval Latin galea or Catalan galea , from Late Greek galea , of unknown origin. The word has made its way into most Western European languages. Originally "low, flat-built seagoing vessel of one deck," once a common type in the Mediterranean. Meaning "cooking range or cooking room on a ship" dates from 1750.

 The printing sense of galley , "oblong tray that holds the type once set," is from 1650s, from French galée in the same sense, in reference to the shape of the tray. As a short form of galley-proof it is attested from 1890.
 also from 13c. 

 Entries linking to galley 

 galleon (n.) 

 kind of large ship, 1520s, from French galion "armed ship of burden," and directly from Spanish galeón "galleon, armed merchant ship," augmentative of galea , from Byzantine Greek galea "galley" (see galley ) + augmentative suffix -on . Developed 15c.-16c., it was shorter, broader, and with a higher stern superstructure than the galley. In English use, especially of Spanish royal treasure-ships or the government warships that escorted private merchant ships in the South American trade.

 GALLEON. The accepted term for the type of ship which the Spaniards used in 1588; that is, an armed merchantman of exceptional quality, combining the strength of the mediaeval trader with some of the finer lines and fighting features of the GALLEY. [Sir Geoffrey Callender, "Sea Passages," 1943]

 Italian agumented form of galea , galeaza , led to a different 16c. ship-name in English, galliass (1540s).

 galley-slave (n.) 

 1560s, from galley (n.) in the "ship" sense + slave (n.). The ships were often rowed by slaves or convicts.

 galleywest 
 galliot 
 gallipot 
 See All Related Words (5) 
######## zawraq
59- Toggle Arabic subsection 
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
71- Declension 
72-
73- 1.4 
74- References 
75-
76- 2 
77- Persian 
78-
79- Toggle Persian subsection 
80-
81- 2.1 
82: Etymology 
83-
84- 2.2 
85- Pronunciation 
86-
87- 2.3 
88- Noun 
89-
90- Toggle the table of contents 
91-
92- زورق 
93-
94- 10 languages 
95-
96- Español 
97- فارسی 
98- Français 
99- Magyar 
100- Kurdî 
101- Malagasy 
102- Polski 
103- Русский 
104- Türkçe 
105- 中文 
106-
107- Entry 
--
165-
166- Wikipedia ar 
167-
168: Etymology
169- [ edit ] 
170-
171- Borrowed from Persian زورق ( zowraq , “ skiff, lake-boat ” ) .
172-
173- Pronunciation
174- [ edit ]
```


## [2026-09-05T20:43:52.151Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### zawraq persian etym\"; sed -n '168,240p' ee856515010ca429.txt\necho \"#### gypsos etym body\"; sed -n '100,175p' 2e2945210a9d3844.txt"
}
```


### [2026-09-05T20:43:52.203Z] TOOL RESULT

```
#### zawraq persian etym
 Etymology
 [ edit ] 

 Borrowed from Persian زورق ( zowraq , “ skiff, lake-boat ” ) .

 Pronunciation
 [ edit ] 

 IPA ( key ) : /zaw.raq/ 

 Noun
 [ edit ] 

 زَوْرَق • ( zawraq )  m ( plural زَوَارِق ( zawāriq ) ) 

 boat , dinghy , skiff 

 Declension
 [ edit ] 

 Declension of noun زَوْرَق ( zawraq )

 singular

 basic singular triptote 

 indefinite

 definite

 construct

 informal

 زَوْرَق 
 zawraq 

 الزَّوْرَق 
 az-zawraq 

 زَوْرَق 
 zawraq 

 nominative

 زَوْرَقٌ 
 zawraqun 

 الزَّوْرَقُ 
 az-zawraqu 

 زَوْرَقُ 
 zawraqu 

 accusative

 زَوْرَقًا 
 zawraqan 

 الزَّوْرَقَ 
 az-zawraqa 

 زَوْرَقَ 
 zawraqa 

 genitive

 زَوْرَقٍ 
 zawraqin 

 الزَّوْرَقِ 
 az-zawraqi 

#### gypsos etym body

 γύψος 

 10 languages 

 Dansk 
 Ελληνικά 
 Français 
 Italiano 
 Kurdî 
 Latviešu 
 Malagasy 
 Polski 
 Русский 
 Türkçe 

 Entry 

 Discussion 

 English 

 Read 

 Edit 

 View history 

 Tools 

 Tools

 move to sidebar 
 hide 

 Actions

 Read 

 Edit 

 View history 

 General

 What links here 
 Related changes 
 Upload file 
 Permanent link 
 Page information 
 Cite this page 
 Get shortened URL 

 Print/export

 Create a book 
 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 Ancient Greek
 [ edit ] 

 Etymology
 [ edit ] 

 Of unknown origin. 
Possibly a Wanderwort , cf. Akkadian 𒅎𒌓 (IM.BABBAR /⁠gaṣṣu⁠/, “gypsum”) > Classical Syriac ܓܨܐ (gaṣṣā, “gypsum”) and Middle Persian gc (gač, “gypsum”).
```


## [2026-09-05T20:43:58.798Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk 'NR>240 && NR<400' ee856515010ca429.txt | grep -n -A12 \"^ Persian\" | head -40\necho \"----\"; sed -n '240,330p' ee856515010ca429.txt | grep -v '^\\s*$' | head -40"
}
```


### [2026-09-05T20:44:01.108Z] TOOL RESULT

```
117: Persian
118- [ edit ] 
119-
120: Persian Wikipedia has an article on: زورق 
121-
122- Wikipedia fa 
123-
124- Etymology
125- [ edit ] 
126-
127- From Middle Persian *zōwrak . Maybe cognate with Latin galea ( “ helmet ” ) .
128-
129- Pronunciation
130- [ edit ] 
131-
132- ( Classical Persian ) IPA ( key ) : /zaw.ˈraq/ 
----
 زَوْرَقِ 
 zawraqi 
 dual
 indefinite
 definite
 construct
 informal
 زَوْرَقَيْن 
 zawraqayn 
 الزَّوْرَقَيْن 
 az-zawraqayn 
 زَوْرَقَيْ 
 zawraqay 
 nominative
 زَوْرَقَانِ 
 zawraqāni 
 الزَّوْرَقَانِ 
 az-zawraqāni 
 زَوْرَقَا 
 zawraqā 
 accusative
 زَوْرَقَيْنِ 
 zawraqayni 
 الزَّوْرَقَيْنِ 
 az-zawraqayni 
 زَوْرَقَيْ 
 zawraqay 
 genitive
 زَوْرَقَيْنِ 
 zawraqayni 
 الزَّوْرَقَيْنِ 
 az-zawraqayni 
 زَوْرَقَيْ 
 zawraqay 
 plural
 basic broken plural diptote 
 indefinite
 definite
 construct
 informal
```


## [2026-09-05T20:44:21.624Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 224 225 226; do echo \"=== NR $n ===\"; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | head -8; awk -v N=$n 'BEGIN{RS=\"\\f\"} NR==N' IEC.txt | grep -n -E \"^3[0-9][0-9]$|^[0-9]{3}$\" | head; done"
}
```


### [2026-09-05T20:44:24.010Z] TOOL RESULT

```
=== NR 224 ===
r. gonim, goinim ‘wound, gore’; OCS gonjọ, -iti ‘chase’; Latv. ganu, it ‘put out to graze’
guhonos, à, is ‘blow, chase, slaughter’. Cf. guhen-, etc. WP I, 679 Skt. ghanáh; Av. vand; Oss. qün, gänä ‘wound’; Arm. ğan, i-st. ‘effort’; Gk. phónos, phoné ‘slaughter’; cf. synth. cpd. phthónos, m. ‘envy, reproof; Alb. záné, xânë ‘padlock’; Mir Ir. guin, goin, f. wound"; MIr. con-guin ‘violation; compunction’; Cz. hon, m. ‘drive, chase’; OCS iz-gonü ‘chasing’; Big. s-gani (*-0-) ‘gang, crowd’; Li. gánas ‘pasture; tend- ing; drover’; Latv. gans ‘drover’. Cf. the cpds.
383
of type *guou-guhon- in Vedic go-hán “killing of cattle’; Gk. boú-phonos *'ox-killing'; Latv. gov-gans ‘drover’
guhoreið ‘warm, heat'. Cf. guher-, guhermos, etc. Olr. goirim, id.; OCS gorjọ, čti Chur", and com. SL); Li. gariü, éti, v. ‘steam’. For the o-gde root, cf. OLat. formus, and perh. Gk. Phorüe ‘Titan’. See next
guhormos ‘hot, warm’. Cf. guhermos, guher-, guhor- & guhrnos. WP I, 687-8 Skt. gharmáhb, s.; Av. garomo, adj.; garomus, s.; Per. garm, adj.; OPer. garma-, id.; OLat. for- mus; Go. *warms, and com. Gmc.; OPr. gor- me, s. (*-?a-)
guhoros, is “heat, warmth; hot place, burn’. WP I, 688. Cf. guher-, etc. Lat. cf. (Isidor) forvus ‘hot’; OIr. guire, MIr. & Ir. gor, sg Br. gor m. ‘heat’; (pl. iu, m. ‘abscess’ to guhr-, q.v.); OCS gorü, s.; Cz. hof, m.f. ‘heartburn’ beside vy-hor 'burnt-out spot: OCS gorikyj ‘hot’; Li. gáras ‘heat, zeal, steam’; pra-garas ‘hell’; Latv. gars ‘spirit: steam’; OPr. goro (for *goàro 'ashpit, hearth’). Long-grade in Blg. R. gari; R u-gàr; Srb. gar
guhrā (?), see guhros (guhros) and ghur-, ghu- ros. (Lat. fória suggests a type w. initial *guh-; Germanic, w. *ghu-; Celtic forms ambig.)
3:383
19:384
=== NR 225 ===
 -yti ‘scour’. Variant in Du. grint (gravel, fr. *guh- rend-). Of uncertain connexions are Alb. grí, gs grini ‘whetstone’; er, aor. grina, v. ‘whet’; OE grind ‘crash’, grinde ‘shingle’; Br. brenn *bran', fr. either *gurendh- or *bhrendh-
guhretos “narrow, close; closeness' Lat. fretus, üs, m. & fretum, n. “strait”; Li. grétas ‘close, adjoining"; gretà ‘alongside’; gré- Cum, gréciui ‘near’. (For Lat. fretus see Supt. dhret-: OCS drëtt ‘to confirm")
guhrét- (guhrést-, guhrot-, guhrt-) “warm, heat; burn, warmth'. Cf. guhre- Olr. cf. grís, Ir. gríos “burning; warmth' (fr. *euhrest-); mod. Ir. also: ‘embers’; ON gráó ‘warm wind’; cf. W graid (burning! adi: m. ‘heat of the sun’ beside gwres (^warmth' < *guhrotis beside *guhrest-); Arm. cf. éah, i-st. Ctorch, fr. *guhrtis); OCS gréti, inf. (and com. SI.) ‘to warm’. Cf. guhrt-
guhro-, r-gde of guhré-, guhret-, etc. q.v.
guhriio (?) ‘crush, pound’. (All the evidence is ambig.)
385
Gk. (?) cf. Hes. thriésai "to wanton’; thrió ‘festivity of Apollo, and his kind’; thrízo (2) ‘mow’; Lat. frio, friare ‘crush’, of ambiguous phonology, but cf. Gk. thriaí ‘pebbles — as used for divination’; Alb. (ambig.) grij, aor. griva & grijta, inf. pp. grimé *mince, chop; punish, destroy’; Li. cf. grystu, gristi ‘annoy, bore?
guhrndó (guhrmdo) ‘grunt, growl’ (?). (Am- biguous. Cf. guhremdh-) Lat. frendo, ére (2) *grunt' is ambig. but equa- tes w. MHG. G grunzen: E to grunt
6:385
21:386
=== NR 226 ===
hrn-ec, -ek, id.; Srb. grnac. id. Cf. ON orna v. ‘warm’. (For the semantics cf. Skt. kundam ‘firepit’ and ‘pot’, and that Aus- tralian aborigines still build earth-ovens. Cf. the structure of the Sardinian nuraghi, of co- nical shape, primitive blast-furnaces?)
guhrn- (2) (?) “group, crowd? OE worn, id.; Cz. sou-hrn “set, collection’; cf. hrnouti ‘amass’; Srb. grnuti, id.
guhrt-, cf. guher-, guhor-, etc. Skt. ghatah, adj. ‘zealous, fiery’; m. ‘pot’; Arm. gah, Let ‘firebrand, torch'. The zero-gde seems to be present in Gk. thár-gelos, s. “pot for firstfruits'; thar-gelía “June harvest cele- bration’
guhurs- ‘foulness’. Cf. ghuros, guhros Gk. cf. phüro ‘mix, defile’; OE worsm, worms ‘pus’. A variant formula of type *guhrs- may be present in Gk. pharikón “a poison-plant
387
?agh- (?aghis, os, iô(n), iə) ‘tip, spike’. WP I, 570. See next Arm. cag, Let ‘tip, peak’; OE ceacga ‘gorse’; Du. keg, kegge, f. ‘wedge’; Li. Zágas ‘stack’ beside Zaginai ‘stumps of young firs, palisade’
$agholos ($aghilo-, $aghlo-) (1) ‘spike, point’. Variant: gaghoros. Cf. &agh-. WP I, 570 Oss. zágàl ‘nail’; OHG kegil ‘peg’: MHG. Du. kegel ‘cone; skittle, icicle’. Variants in Oss. dzagur ‘chisel’: Li. Ziogras ‘stake’, fr. a type *saghuro-, *&aghro-; Icel. kógur, n. fringe"; Li. Zágaras ‘twig’; pl. ‘brushwood’; Zagre ‘plow- share’ beside Zagáre, id.
$agholos ($aghilos, $aghlios) (2) ‘rogue’. Same as (1)?
5:387
23:388
```


## [2026-09-05T20:44:28.539Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==227' IEC.txt | head -40"
}
```


### [2026-09-05T20:44:30.637Z] TOOL RESULT

```
eside garen ‘stalk’; Latv. zars ‘branch’. (LW fr. Gaul. in Fr. jarret ‘ham, bock’, cf. E garter: jarretière)
$aros, is, us ‘voice, noise, cry’. (cf. gouor- for alternatives). WP I, 537 Skt. (-ă-) cf. járe, mp., Av. jar- ‘cry, bawl; creak’; Per. zar? (lamentation’. Ambig. cf. guel-); Oss. zar ‘singing, song"; zarin, v. ‘sing’; Arm. cf. (?) ci-carn (‘swallow — bird”, in view of ci- cayim, v. ‘laugh’, as an extn. of cay laughter"); Gk. (ambig.) gérus, (Dor. -à-) ‘voice’; Ir. gáir ‘cry, laugh”; gáire ‘laughter’; W gawr ‘cry’; Du. cf. koeren ‘coo, croon’
$aulos (?) “vessel, boat’ Per. cf. zauraq ‘ship, vessel’; Gk. gaülos "mer. chant-ship'; gaulós *milkpail'. Cf. geul-
$auros (Celtic variant: &aruos, cf. tauros, ta- ruos) “raw, wild, violent, fierce'. Cf. WP I, 610 for Celtic forms Gk. gaüros ‘arrogant’, cf. a-gaurós ‘refined, noble"; Ir. garbh, W garw, Br. garð, garv, Cor. garow 'rough, rude'; Gallo-Lat. in It. garbo (2) “sharp, tart and in Rumansch £erv ‘raw,
389
clammy’; ON cf. keyra ‘spur on, drive’; Cz. cf. zulit ‘rave, rage"; Li. Ziaurüs ‘fierce, cruel; Ziaureju, eti ‘rave, rage’. (For Av. zuro ‘force’, cf. 8hul- (2)
$au- ($auos, $auio) "land, region, settle-
ment. (Variant: gaueso?) Gk. gë, gara (cf. Lacon. gabergo- "and wor. ker); Dacian, Thracian in place-names: Arge-, Burri-, Pulpi-, Rami-, Singi-, Thermi-dava; Moldavia *mountain-land'; cf. also variant Pulpu-deva *Philippopolis'; Illyr. cf. names of peoples: Daorsoi, Daorsioi, Daversi, beside the personal name Daverzeus; Sequanian (perh.) gavisa 'lands??; Du. (?) kei *cobble- stone’; Alb. dhe, gs dheu, m. “land, earth?
Ge (ge, go) sentence-link ‘so, and, also’. Cf. WP I, 542 & I, 98. Gk. ambig.
Gk. ge; Alb. dhe; (OCS Ze, Zi fr. ge, q. v.; cf. also OCS -Zde "-soever'; Li. -gi, fr. *go). Un- certainly Arm. z- (acc. sign)
£ebolos, à, ios "pendant. (Evidence ambig.) Oss. zàbül, zäbólä, adj. "pendant, s. ‘rag’; Li. Zebeljs *fircone'
$ebh- “jaw? (gebhl-, $obh-). Cf. 2obh-
Oir. cf. gibis, id. (*&ebhost-); G Kebe (3) “fish- gil; MLG cf. kéver, -e ‘beetle’ (G. Käfer fr. LG and OE ceafor ‘beetle’ represent an o-gde formula, as also OE ceafl ‘jaw, cheek’, fr. *ŝobh-, q. v. Cf. also E dial. to chavvel ‘to gnaw away, chew at’; long-gde in OS kaflos ‘jaws’ and in Li. Zébeju, eti ‘munch’. Isophones, of uncertain origin, are Oss.dzibir, dzubur "bar. row, hook-plow? and LG Keffer, ‘mechanical crane’. The root &ebh- appears to be present in ON kjaptr, kjoptr ‘jaw’; kjapta, mod. kjafta *chatter, jaw?)
edu (?) “flesh, fleshworm'
Arm. cetuk, dim. type *fleshworm'; ON kjot, Sw. kótt “flesh?
&eguer- (?) (an ambig. formula, cf. geger-) Skt. jagalah (adj. ‘fraudulent’; m. “a liquor’); Oss. záqgàr ‘harsh’; G cf. keck ‘downright; gay; sound, firn?
&e0, ið (Legs-) ‘jerk, buffet, knock?
Arm. cecem ‘beat, pound’; cec, s. ‘beating, pounding’; LG kicken, v. ‘knock, buffet, kick’; E to kick; G cf. kicksen ‘jab, nudge’; Li. žeg- sið, éti ‘hiccup’ (fr. *&egsio)
$au- (ĝauos, $auio) — ĝen-
20
25
30
35
40
45
390
$eibh- “bully, abuse, hurt? G dial. kiben ‘bully, abuse’; G fr. LG keifen, id.; Du. kijven, id.; Sw. kiva, id.; E cf. to chivvy (ME: “harass'); Li. žiebiù, “ti (2) “hit, dash, rush?
Leidh- ‘fight, wound, abuse? OE cidan ‘quarrel; complain’; cid ‘strife’; Li. žeidžiù, Zeisti, v. “hurt, wound"; (o-gde in Zaiz- dà *wound)
ĉel- laugh; laughter’. WP I, 622 Arm. cayr, gs cayu id. (see SEM: AI, § 15, note 3); Gk. géla “brilliance”; geláo “laugh” be- side gel&o ‘shine’; gélos, geloios, adj. ‘merry’
elu (8eleu-, gleu-) *lee
```


## [2026-09-05T20:44:54.725Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD watkins gei/ga sing ===\"; grep -n -i -E \"to sing|gā-.*sing|gei-\" AHD_watkins1985.txt | head -20\necho \"=== IEC gai- sing ===\"; grep -n -E \"^gaio|gai-|gaiō.*sing|'sing'\" IEC.txt | head -20"
}
```


### [2026-09-05T20:44:54.816Z] TOOL RESULT

```
=== AHD watkins gei/ga sing ===
122:The verb “‘to live” was gei-; it formed an adjective *g”i-wos, “alive,” which survives in English quick, whose original sense is seen in the Biblical phrase the quick and the dead. For the notion of begetting there are two roots, tek- and the extremely widely repre- sented gene-, which appears not only as a verb but also in various nominal forms like *gen-os, “race,” and the prototypes of Eng- lish KIN and KIND.
485:gé@i-2. To sing. Contracted from *geai-. Zero-grade form *gi- (< *gia-) in Sanskrit gitd, song: BHAGAVAD-GITA. [Pok. géi)- 355.]
510:*ghait-d in Greek khaité, long hair: CHAETA; (CHAETOG- NATH). [Pok. ghait-d- 410.] ghalgh-. Branch, rod. Germanic *galgon- in: a. Old English g(e)alga, cross, gallows: GALLOWS; b. Old North French gauge, gauge: GAUGE. [Pok. ghalgh- 411.] ghans-. Goose. 1. Germanic *gans- (nominative plural *gansiz) in: a. Old English gds (nominative plural gés), goose: GOOSE!; (GOSHAWK); b. Old Norse gas, goose, diminutive geslingr, gosling: GOSLING. 2. Germanic *ganr- in Old English ganra, gandra, gander: GANDER. 3. Germanic *gandton- in Old English ganot, gannet: GANNET. 4, Suffixed form *ghans-er- in Latin dnser (< *hanser), goose: ANSERINE; MERGANSER. 5. Basic form *ghans- in Greek khén, goose: CHENOPOD. [Pok. ghans- 412.) ghasto-. Rod, staff. 1. Variant form *ghazdh- in Ger- manic *gazdaz in: a. Old English gierd, gerd, staff, twig, measuring rod: YARD}; b. Old Norse gaddr, rod, goad, spike: GAD?. 2. Form “ghast-d- in Latin hasta, spear: HASLET, HASTATE. [Pok. 1. ghasto- 412.] ghé-. To release, let go; (in the middle voice) to be released, go. Contracted from *ghea-. 1. Germanic vari- ant form *gaian in Old English gdn, to go: GO; AGO, FOREGO!, FoRGO. 2. Suffixed form *ghé-ro- in Latin hérés, heir (? < “orphan” < “bereft”):; HEIR, HEREDITA- MENT, HEREDITY, HERITAGE; INHERIT. 3. Suffixed o-grade form *ghé-ro-, “empty space,” possibly in: a. Greek khéros, place, country, particular spot: CHO- ROGRAPHY; b. Greek denominative khorein, to move, go, spread about, make room for: -CHORE; ANCHORITE. 4. Perhaps suffixed zero-grade form *gha-l- in Greek khalan, to slacken, let down (but this is more likely of unknown origin): CALANDO, CHALONE; ACHALASIA. 5. Suffixed zero-grade form *gho-t(w)d- in Germanic *gatwon-, a going, in Old Norse gata, path, street: GAIT. [Pok. ghé- 418.] ghebh-el-. Head. 1. Germanic *gablaz, top of a pitched roof, in Old Norse gafl, gable: GABLE. 2. Dissimilated form *khephel- in Greek kephalé, head: CEPHALIC, CEPH- ALO-, -CEPHALOUS; ENCEPHALO-, ENKEPHALIN, HYDRO- CEPHALUS. [Pok. ghebh-el- 423.] ghedh-. To unite, join, fit. 1. Lengthened o-grade form *ghédh- in Germanic *gédaz, “fitting, suitable,” in Old English géd, good: GooD. 2. Germanic *gaduri, “in a body,” in Old English tégezdere (t6, to; see de-), together: TOGETHER. 3. Germanic “gadurén, “to come or bring together,” in Old English gad(e)rian, to gather: GATHER. [Pok. ghedh- 423.] ghei-'. To propel, prick. 1. Suffixed and extended o-grade form *ghoidh-d in Germanic *gaidé, goad, spear, in Old English gdd, goad: GOAD. 2. Suffixed form *ghei-s- per- haps in nasalized zero-grade form *ghi-n-s- in Sanskrit himsati, he injures: AHIMSA. [Pok. 1. ghei- 424.] ghei-2. Theoretical base of *ghyem-, *ghiem-, winter. 1. Form *ghiem- in Latin hiems, winter: HIEMAL. 2. Suf- fixed variant form *gheim-ri-no- in Latin hibernus, pertaining to winter: HIBERNACULUM, HIBERNATE. 3. Suffixed zero-grade form *ghim-ar-ya, “female animal one year (winter) old,” in Greek khimaira, she-goat: CHIMERA. [Pok. 2. ghei- 425.] gheis-. Used of the emotion of fear or amazement (origi- nal part of speech uncertain). Suffixed o-grade form *ghois-do- in Germanic *gaistaz, a ghost, in: a. Old English gdst, ghost: GHOST; AGHAST; b. Old High Ger- man geist, ghost: POLTERGEIST; Cc. Germanic denomina- tive *gaistjan in Old English g&stan, to scare: GAST. [Pok. gheis- 427.] ghel-'. To call. 1. Germanic “gel-, *gal-, in: a. Old Eng- lish gellan, giellan, to sound, shout: YELL; b. Old English gielpan, to boast, exult: YELP; c. Old English galan, to sing: NIGHTINGALE. 2. Reduplicated form *ghi-ghl- in Greek kikhilé, thrush, later also the name for a kind of wrasse (a sea fish that has bright colors and jagged waving fins, reminiscent of the plumage of a bird):
540:(COVEN), (COVENANT), EVENT, INTERVENE, INVENT, MIS- ADVENTURE, PARVENU, PREVENIENT, PREVENT, PROV- ENANCE, (PROVENIENCE), REVENANT, REVENUE, SOUVENIR, SUBVENTION, SUPERVENE. 3. Suffixed zero-grade form *gvm-yo- in Greek bainein, to go, walk, step, with basis (< *gm-ti-), a stepping, tread, base, and -batés (< *gwa-to-, zero-grade of gd-, contraction of *gaa-), agential suffix, “one that goes or treads, one that is based”: BASE!, BASIS; ABASIA, ACROBAT, ADIABATIC, AMPHISBAENA, ANABAENA, DIABASE, DIABETES, STEREO- BATE, STYLOBATE. 4, Suffixed zero-grade form “g“(g)-u- in compound form “pres-gu-, “going before” (see per’). 5. Basic form *gvd- in Greek béma, step, seat, raised platform: BEMA. 6. Sanskrit jigdti, he goes: JUGGER- NAUT. [Pok. g¥d- 463.] gvadh-. To sink. Possible root. 1. Suffixed form *guadh-u- in Greek bathus, deep (> bathos, depth): BATHOS, BATHY-. 2. Greek benthos, depth, may be formed on bathus by analogy with penthos, grief, and pathos, passion, suffering (or it may be from an unrelated root *g¥(e)ndh-): BENTHOS. 3. Suffixed variant form *gudh-yo- in Greek bussos, bottom of the sea: ABYSS. [Pok. gddh- 465.] g’ébh-'. To dip, sink. Suffixed zero-grade form *gvabh-yo- in Greek baptein, to dip: (BAPTIST), BAPTIZE; ANABAPTIST. [Pok. g¥ébh- 465.] g”ébh-2. Hypothetical base of some Germanic words associated with the notion of sliminess. 1. Middle Dutch quac-, unguent, liquid, in obsolete Dutch quacksalver, quacksalver: QUACKSALVER. 2. Low German quabbeln, to shake like jelly, tremble, akin to Middle English quaven, to tremble: QUAVER. [Pok. 2. g¥ébh- 466.] grei-. Also gveia-. To live. I. Suffixed zero-grade form *gwi-wo-, *gi-wo- (< *gi9-wo-), living. 1. Germanic *kwi(k)waz in: a. Old English cwic, cwicu, living, alive: QUICK, QUICKSILVER; b. as a name for couch grass (from its rapid growth), in Old English cwice, couch grass: (COUCH GRASS), QUITCH GRASS. 2. a. Latin vivus, living, alive: VIVIFY, VIVIPAROUS; b. Latin denominative vivere, to live: VIAND, VICTUAL, VIVA, VIVACIOUS, VIVID; CON- VIVIAL, REVIVE, SURVIVE. 3. Further suffixed form *gvi- wo-td in Latin vita, life: VIABLE, VITAL; LIGNUM VITAE, VITAMIN. II. Suffixed zero-grade form *gia-o- in Greek bios, life (> bioté, way of life): BIO-, BIOTA, BIOTIC; AEROBE, AMPHIBIOUS, ANABIOSIS, CENOBITE, MICROBE, RHIZOBIUM, SAPROBE, SYMBIOSIS. III. Variant form *gwyd- (< *gvyoo-). 1. Greek z0é, life: AzO-, (DIAZO). 2. Suffixed form *gvy6-yo- in Greek zdon, zdion, living being, animal: (-Z0A), -ZOIC, ZOO-, ZOON, -ZOON. IV. Pre- fixed and suffixed form *su-g~ia-es- (*su-, well; see su-), “living in good condition,” in Greek hugiés, healthy: HYGEIA, HYGIENE. [Pok. 3. gei- 467.] g”eia-. To press down, conquer. Sanskrit jayati, he con- quers: JAIN. [Pok. gveio- 469.] gvel-'. To pierce. 1. Suffixed o-grade form “gvol-eyo- in Germanic *kwaljan in Old English cwellan, to kill, destroy: QUELL. 2. Suffixed zero-grade form *g“/-yo- in Germanic *ku/jan in Old English *cyllan, to kill, perhaps the source of Middle English killen, to kill: KILL}. 3. Full-grade form *gvel- in Greek beloné, needle: BEL- ONEPHOBIA. [Pok. 1. g¥el- 470.] gel-2. To fly; a wing. Possibly in Latin voldre, to fly: VOLANT, VOLATILE, VOLE2, VOLITANT, VOLLEY. gvel-3, To swallow. Dissimilated to *gel-. 1. Germanic *kel- in Old English ceolu, throat, dewlap, perhaps akin to Middle English cholle, throat: JowL?. 2. Germanic *keluz in Old Norse Aj6ir, keel: KEEL}. 3. Suffixed zero-grade form “gul-d in Latin gula, gullet, throat, palate: GOLIARD, GULAR, GULES, GULLET. 4, Extended (expressive) form *glutt- in: a. Latin gluttire, gliitire, to swallow: GLUT; DEGLUTITION; b. Latin glutté, a glutton: GLuTTon. [In Pok. 2. gel- 365.] gvelbh-. Womb. 1. Suffixed form *gvelbh-u- in Greek delphus, womb, whence delphis, dolphin (referring to its
581:BIT), GAMBOL, (GAMBREL), (GAMMON3), (JAMB). 2. Suf- fixed form *kamp-ulo- in Greek kampulos, bent: CAMPYLOTROPOUS. [Pok. kam-p- 525.] kan-. To sing. 1. Germanic *han(e)ni in Old English hen(n), hen: HEN. 2. Latin canere, to sing (> cantdre, to sing): CANOROUS, CANT?, CANTABILE, CANTICLE, CANTIL- LATE, (CANTO), CANTOR, CANZONE, CHANT; ACCENT, DESCANT, ENCHANT, (INCANTATION), INCENTIVE, PRE- CENTOR, RECANT. 3. Latin oscen, a singing bird used in divination (< *obs-cen, “one that sings before the au- gurs”; ob-, before; see epi): OSCINE. 4. Suffixed form *kan-men- in Latin carmen, song, poem: CHARM}. [Pok. kan- 525.] kand-. To shine. 1. Suffixed (stative) form *kand-é- in Latin candére, to shine: CANDENT, CANDID, (CANDIDA), (CANDIDATE), CANDLE, CANDOR; INCANDESCE. 2. Latin transitive *candere, to kindle, in compound incendere, to set fire to, kindle (in-, in; see en): (INCENDIARY), IN- CENSE. [Pok. kand- 526.] kannabis. Hemp. Late Indo-European word borrowed from an unknown source. 1. Germanic *hanipiz in Old English henep, henep, hemp: HEMP. 2. Greek kannabis, hemp: CANNABIS, (CANVAS). kanto-. A corner, a bending. Celtic *cantos, rim, border, in Latin cantus, canthus, iron ring around a carriage wheel, a wheel, rim (> Italian canto, corner): CANTEEN, CANTON; DECANT. [Pok. kan-tho- 526.] kap-. To grasp. I. Basic form *kap-. 1. Germanic *haf- in Old English hefeld, thread used for weaving, heddle (a device which grasps the thread): HEDDLE. 2. Germanic *haftjam in Old English heft, handle: Harr. 3. Form *kap-o- in Germanic *habai-, *habén in Old English habban, to have, hold: HAVE. 4. Germanic hafigaz, “containing something,” having weight, in Old English hefig, heavy: HEAVY. 5. Germanic *hafnd-, perhaps “place that holds ships,” in Old English hefen, a haven: HAVEN. 6. Germanic habukaz in Old English h(e)afoc, hawk: HAWK}, 7, Latin combining form -ceps (< *kap-s), “taker.” II. Suffixed form *kap-yo-. 1. Germanic *hafjan in Old English hebban, to lift: HEAVE. 2. Latin capere, to take, seize, catch: CABLE, CAPABLE, CAPACIOUS, CAPIAS, CAPSTAN, CAPTION, CAPTIOUS, CAPTIVATE, CAPTIVE, CAP- TOR, CAPTURE, CATCH, (CHASE!); ACCEPT, ANTICIPATE, CONCEIVE, DECEIVE, EXCEPT, INCEPTION, (INCIPIENT), INTERCEPT, INTUSSUSCEPTION, MUNICIPAL, NUNCUPA- TIVE, OCCUPY, PARTICIPATE, PERCEIVE, PRECEPT, RE- CEIVE, (RECOVER), RECUPERATE, (RX), SUSCEPTIBLE. III. Suffixed form *kap-s- in Latin capsa, repository, case: CAISSON, CAPSICUM, CAPSID, CAPSULE, CASE2, CHASE?, CHASES, CHASSIS, CHESS?; ENCHASE. IV. Length- ened-grade variant form *kdép-. 1. Germanic *hof- in compound *bi-hdf, “that which binds,” requirement, obligation (*bi-, intensive prefix; see ambhi), in: a. Old English behdf, use, profit, need: BEHOOF; b. Old English behéfian, to have need of: BEHOOVE. 2. Greek k6pé, oar, handle: copePpop. Compare ghabh-. [Pok. kap- 527.] kap(h)o-. Hoof. Lengthened-grade form kdp(h)-o- in Germanic *héfaz in Old English Adf, hoof: Hoor. [Pok. kapho- 530.] kapro-. He-goat, buck. Latin caper, he-goat (> capra, she-goat): CABRILLA, CABRIOLET, CAPELLA, CAPRIOLE, CHEVRON; CAPRIC ACID, CAPRICORN, CAPRIFIG, CAPROIC ACID. [Pok. kapro- 529.] kaput. Head. 1. Germanic *haubidam, *haubudam, in Old English héafod, head: HEAD. 2. Latin caput, head (> Italian capo, head): CABEZON, CADET, CAPE?, CAPITAL, CAPITAL, CAPITATE, CAPITATION, CAPITELLUM, CAPITU- LATE, CAPITULUM, CAPO!, CAPRICE, CAPTAIN, CATTLE, CAUDILLO, CHAPITER, CHAPTER, CHIEF, CHIEFTAIN; BI- CEPS, CHAMFRON, DECAPITATE, KERCHIEF, MISCHIEF, OCCIPUT, PRECIPITATE, RECAPITULATE, SINCIPUT, TRI- ceps. [Pok. kap-ut- 529.] kar-', Hard. I. Variant form ker-. 1. Suffixed o-grade form *kor-tu- in Germanic *harduz in: a. Old English hard,
919:seng“h-. To sing, make an incantation. 1. Germanic *singan in: a. Old English singan, to sing: SING; b. Old High German singan (> German singen), to sing: MEIs- TERSINGER, MINNESINGER, SINGSPIEL. 2. Suffixed o-grade form *songvh-o-, singing, song, in Germanic *sangwaz in Old English sang, song, song: SONG. [Pok. sength- 906.]
920:senk-. To burn. Suffixed (causative) o-grade form *sonk- eyo- in Germanic *sangjan, to cause to burn, in Old English sengan, to singe: SINGE. [Pok. senk- 907.] sent-. To head for, go. 1. Germanic suffixed form *sinth- nan in Old High German sinnan, to go: WITHERSHINS. 2. Suffixed (causative) o-grade form *sont-eyo- in Ger- manic *sandjan, to cause to go, in Old English sendan, to send: SEND!. 3. Suffixed o-grade form *sont-o- in Ger- manic *sandaz, that which is sent, in Old English sand, message, Messenger: GODSEND. 4. Perhaps suffixed form *sent-yo- in Latin sentire, to feel (< “to go mentally”): SCENT, SENSE, (SENSILLUM), SENTENCE, SENTIENT, SEN- TIMENT, SENTINEL; ASSENT, CONSENT, DISSENT, PRESEN- TIMENT, RESENT. [Pok. sent- 908.]
1128:wed-2, To speak. 1. Possibly oldest root form *awed- becoming *awed- in reduplicated form *awe-ud- dissimi- lated to *aweid-, with suffixed o-grade form *awoid-o- respectively in Greek aeidein (Attic aidein), to sing, and aoidé (Attic didé), song, ode (but more likely a separate root *aweid- becoming Greek *aweid-, to sing): ODE; COMEDY, EPODE, HYMNODY, MELODY, MONODY, PARODY, RHAPSODY, TRAGEDY. 2. Sanskrit vddah, sound, state- ment: THERAVADA. [Pok. 6. au- 76.]
=== IEC gai- sing ===
4558:ghāið (ghāmi, ghíghami) ‘go, move, de- part'. Cf. gai-, gíga-. WP I, 543 Skt. hayáàmi, jáhami ‘go, move; depart'; Per. gayam ‘copulate’; Arm. gam "come: Gk. kíkhemi ‘arrive’; OHG gàahen, gigahen ‘hurry’; MHG gàhe, gæhe "baste beside OHG gen "oo: OE gān, id. (& com. Gmoc.); Cz. cf. hej-no “flock of birds’; Li. (ambig.) góju, góti 'amble; wade’; Latv. gāju (‘I went But cf. gāi-)
5307:guoiuos, à “alive; Die O-gde variant of guluos, etc. cf. guoiið & next Skt. cf. jaivah (vrddhi: “of the soul’); Li. gai- vüs ‘lively’; gaivalas ‘element’; ON cf. kveikja (2) ‘touse’. WP I, 670
5887:(&uhaidros, see guhaidros and Supt.: gai-
```


## [2026-09-05T20:44:56.233Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT gatha ===\"; grep -n -E \"ga%ä|ga\\?ä|gäQä|Gesang|gäOä\" BRT.txt | head -20\necho \"=== BRT 'Lied' ===\"; grep -n -i \"'Lied'\" BRT.txt | head -20"
}
```


### [2026-09-05T20:44:56.296Z] TOOL RESULT

```
=== BRT gatha ===
3212:mit  paiti  i)  'etwas  (Akk.)  beantworten, worauf  antworten':  paili  //  (als  Akk.) Shaydit  aSsa  paiti.irista  tumascS..  "darauf soll  der  Verunreinigte  antworten:  tum" ." Y.g.i2.  1)  'Jmdm.  (Dat.,  Gea)  ant- worten auf  — '  (Akk.),  im  kirchlichen Wechselgesang:  äaj  *atravaxsaAe {sd.)  yal ,.  zaokralca  vacim  failiMoaySi  aHä  ratus N.  7J;  72  (wo  paiti.aoayät);  —  aoäj  an- yalsqm  rähivqm  (nämL  väam)  paiti.äla- yöit  "darauf  soll  er  (der  Zaotar)  den  Ä.s auf  der.  andern  Seite  (auf  Ihren  Gesang) antworten"  N.  83.         [S.  noch  paityäüa-^
10337:•  j.  gahra-  n.  'Singen',  Gesang'. KompA,  E.  —  Zum  ai.  V.  gäyati.  —  ai.  vgl, gäyaträ-  m-,  n.
15323:mit  apa  dnwS.:  yn  ga%ä  asrsvayö  afa tansm  *piTynti^'^''*  N.42.
22023:mit  ä  Kaus.  i)  'Jemandem  (Dat.,  Gen.) etwas  zusprechen,  zu-,  überweisen,  widmen, weihen':  sral/lam  al  tdi  kshrpim  k3krpqm ävaläayamaAl  "pulcenimam..  tibi  formam formarum  dedicamus"  Y,jö.6;  —  stüts garS  .  .  oAurSi  .  .  acä  avafdayamahl  Y. 4'-  ^;  4-  i;  —  hai'ake  urunS  Aaomq ilva^ayainahl  Yi.li.i;  i',  13,  16',  21, 4.  2,  Y.  4.  2  ff.,  24. 1,  3',  5;  — yai  usäähm yat  ävisttm'*''  yäha  dri  ava^ayaf  ahurS .  .  ya%a  dis  az>m  yS  zaota  3va^yemi  . . viovä  däityqm  avistim  Vr. //.  19;  19;  — paili  tl  m^rvya  . .  imä  srvä  v  " imä  srvä  ävasoayemi  "ich  weise  dir . .  diese Nägel  zu,  ich  überweise , ."  V.  77. 9 ; — Aaoms aviits^*^  aiwi.visis  YL  10.  i^o.  2) 'Je- mandem (Dat.)  etwas  anvertrauen':  ahmät fumankl  ävaidayamaidl  gag%Bscä  tan- vasiä  . .  Y.5&  2;  —  aat  dll  ava^ayamahi ga%äbys  . .  Y.5J.  i;  i.
22249:1. 1;  —  maiamya  vaca  frasrävayamnahe N,  20;  *26,  26,  33;  —  nitima  vaca  gäiiä srävayH  N.  27;  —  mt^rsm  ..yeiihe  vSxS gfmänahe  .  .  vi  Äafta  karhiqn  /asaiti yatcit  mmartka  vsHm  iaraiti  {Sp.  ^^sf.) yai  gaoi(sA.)ät  Yt/0.85;  73;  —  tmrr/S yS  parSäars  .  .  ä%rS  vScim  sururtaeiti FrW.  10.  41 ;  —  b»r3Z>m  barSi  zaota  välim Yt.  17. 61;  Y.  70.4,  Yt5. 123;  —  yat  bä faiti . .  näirikaca  apinnSyükasca .  .Janilm baraiti  väcim  V.J.  11;  —  yS  mq'hrä  (sd.) *vacim'''  ..  baraiti  V.  50.  6;  —  a^rä *väcim'''  baraitj  mihaAvacä  vä  *»n{.- vaeä  (sd.)  vä  Y.31.J2;  —  yeriAe /räyB (sd.)  sbaymtam  sraistfm  susruye  väHm Yt  i7. 1 7 ;  — *GS.  mit  avaifat-  (sd.)  '(Wehe- tum  der  Rede  sva.)  Weherufen':  daragSm äyü  (sd.)  timatfhs  äus^ar»^Sm  (sd.)  avaSäs (sd.)  vacö{G%.)  Y.J7.  ao.  a)  'Gesang' beim  Gottesdienst:  eis  saotarsi&d.)  kairim
26978:—  vat?m  °t>m  hma»hm  Y.  16.  5,  Ny.  /,  8, S.  2.  32;  —  °ta  srTra  duyla  (sd.)  akurahe mazda  Y.ig.13;  —  äiarf  Ua  ra%aistara Ny.  5.6;  —  ätnm  't»m  . .  iaxmtm  hsnt^m rahaistanm  Y.62.Z  Gl.;—  ä^r5  urvaä- Itahe  -iahe  .  .  Yty.  85;  —  s.  noch  s  a, b.  2)  sonst;  a)  von  mq^ra-'°*  (Stverz., Sp.iiy&m.):  mqkrai  "taiExtr.i-jVSw,  'tu, 'tfm,  'tahe,  *''taj^'^  — .  b)  von  gaha-: ga%äby5  °tabys  ratuxsa^raijrif  (Stverz.) aiaariiiylf  Y. 55.1; usw.—  °tS~.        c)  sonst:
27224:Zum  V.  irav-.  —  np.  sutöd  'Gesang'.  —  Pü.i nifföiUn  u  ämunisn,  erl.:  ta  nigösend  u  mar- lumin  Smutzfid.  —  >)  Vgl.  zVerb.  V.JS-  11: sraalä  mal  miriidälä  mSi.
27346:—  *anSsl?r>tö . .  ava  yh  *anyä  (jüia\.gähä) srävaysit  ^.46,  30;  4S;  —  ya  gä^ä *afsmainrBqn  (sd.)  * srävayats  (3D,) '"  .  , vacaslaltivat  *srävayats'^'>  N.  2_j;  —  yS ga%ä pairi.uxiaiti  (sd.)  *srävayanti  N.  J2j
27526:yasamaide  hävauämm  .  ,  Slravaxstm  .  , |G.j.s;  V,5,57,58;  —  vUäi  v!  anusa ipmtä  staotä  Uä  zbitä  . .  Y.14. 1 ";  Vr. 5.1; —  stofftarxa  'tanca  tiatania  Yt.j. i;  —  az3m  ..  'ta  rlrJ/ (Sp.  1327  o.) slaotanqm  yesnyanam  frasrao%r3mca  .  . fräyastlnüa  Vr.j.  7;  —  tum  tta  akra^m *sactasie  (Sp.  1607  o.)  *  'V1.3.  7;  — ya^a dis  atpm  y5  °ta  itva^ayemi  vi%vä  a^qm yasn»mca  vahmimca  . ,  Vr.  Jr.  1 9 ;  —  kaha 'la  xsata  vala  SfS  .  .  yazätte  Y,  6^.  9; 9,  Yt5.  131,  so.  120;  —  bfr7Z3in  barät  'la väiim  Aisbmra  pasia  banstna  Yt/7.61; 10. 137,  138;  —  dayata  . .  aps  ttiäva- yaia  '^re  yeztmnai  ahmaktm^a  maxda- yamanqm  fräyatsmnattam  .  .  Y.6S.  12; 2,  39.30;  —  hana^a  tu  tum  taj  mtcd^m ya^  'ta  hanayamnS  ättha  frayB.kumatB  . . Y. 55.30;  —  ar?dvT  .,  -5«  (statt  Gen.) väHm  paitiimarfmna  Yt  5.113;  —  daAmd •la  tanupiriia  (sd.)  upa.sraotarl!  N.jS; 3g^;  — surunaoiti  *'tai1  upa.sraotaraiiqm (sd.)nöit upa.sra0tarB  •tarB{GS.)'ta  raiufris N.  27;  2/';  ~  Si  '/arI{GS.)  iairim  ai^Aai myatdahe  *ayqn?  (ya/)  *ga%asca  fratrsva- yaiti  vantnca  af3he  (Sp.  108  m.)  *astvaite paiti.ähaySt  aka  ratul  '"Was  ist  das  Amt des  Z.  am  Tag  des  My."}'  'Dass  er  die G.  vorträgt  und  der  Gemeinde  auf  ihren Gesang  mit  <£iia  ratus  (msv.)  antwortet'" N.  72;  —  aat  *atravaxiahe  (sd-,  oämL  kai- rim  arahaf)  yat  . .  •Prälat  väcim  paiti.- aiaya^  H.  J3 ; — yaha  ahB  vairyS  'tä  frä ml  mrOt! . .  a%a  ratus  aiäi^^  kaca  fra aidva  vjtva  mraotü  "y.  a.  v.  soll  der  Z. aufsagen  . .  a.  r.  a.  h.  soll  der  wissende Gläubige  (sva.  die  Gemeinde,  s.  Sp.  250  0.) aufsagen"  V.J.  25;  25**,  N.jj*; —  kä^a 'ta  ga'ha  frasravayäilii  *>iaänlF.vacastasta (sd.)  *mahmya  vaca  sardkvstri  mana "'wie  soll  der  Z.  die  G.  vortragen?"  In der  (ersten)  Halbstrophe  (jeweils)  mit mittelstarker  Stimme  im  £<ir-i2^»jVnschen Zeitmass'"  N.j_j; — yat'ta  ahurtm  masdqm yazäiti  *mao^näi  barasmqn  paitiiareii  N. J0;~'ta  g}ui*paityapöis(%A.) paoiryO  */ra- »harsitti.  "/J-iyi; — yezica  *a!fe  ratavd  *ana- iaxta(sd.)*para.iyayanti  °ta  viipf.ratu^toais (sd.)  *ra!%wayeiii  N.  80;  —  'ta  *^anahaxtS parayat  dahistäi  arivacasttmäi  saoknm ralxsaiti  "ein  nichtqualifizirter  Z.  soll  weg- gehen und  das  Z.-Amt  einem  Überlassen, der  .  ."  N.  i¥o;    —    cvaiti    naram    *iaxlö
28628:j  N.  42;  —  spa  .  .  stamantm  kl  mai  nyä- saym  .  .  dasimm  hl  gaeiTtn  .  .  Aöyum  kl \gaosfm  upa^Wfrfsayitt  .  .  doTimtn  Al 'paßyqm  .  .  kaoyqm  hl  paiiyqm  upa.- ksr^ntay^n  .  .  dum^mcil  Al  (zu  a)  upa.- '^lionsaym  V.  13. 30  ff,;  8.  40,  5. 1 7  ff.  (oft), 49,  H.2.  18,  36;  —  Aavatianö  (sd.)  äaityS gatuÜ  .  .  Aaffyaj  *Al^^  *nalmat  Omatars R  7p;  *7P'^  Yl/o.  ioo',  126,  Ä  38,  V. 79.  2;  —  nairika  .  .  airime  (sd.)  gätüm ^?  (fem,;  zu  ß)  nisAihalta  V.i6.&;g.^^ (mask,);  —  ahmi  nairi . .  b^m/ayän/i  fsd.) /l . ,  mänh^m^a  hvarfca  aamca  Al{za  a) bfr^Jaim  V, 7.  52;  —  sünahe  .  .  asti  sl haHn  ya%a  a^aurune  V,  13.  44;  44'; —  yS  ga'hanqm  *anu.tnaiti  (sd.)  *afm.- mainyete . .  anyS  vä  hl  (zu  a)  daAmB  srvth ga%ä  dalaiti  N.  25;  —  azdibji. .  *usäan3m h  i (Plnr.)  alat  k^rmaot  Y.  6. 50; — *Aixsa»e . .  drvatqm  .  .  anyqm   i4?(PIur.)  avarptqta
=== BRT 'Lied' ===
10318:•  j.  gäSS-  f.  'Lied'  uzw.  religiösen  Inhalts; 1)  insbes.  von  den  fünf  Hymnen,  bez. Hymnensammtungen,  die  in  Y.  28—34, 43—51,  59  erhalten  sind*':  sraobm  .  .  y5 paoiryd  "^.J  frasrävayatya panca  . .  zara- iu/traAe  *a/smaimvan  (sd.)  vacastastivaf malMzaintls  mal.paiti./rasä  Y.57,8;  7/. 6, G.  7.6;  —  akunavaitlm  (Stverz.)  °'i:qm aiaonlm  .  .  mai.afsmanam  mat.vaüäslallim map.äzaintim  matpjnsvlm  mat.paiti.p?r>s- Vlm  map  varfiibyjca  *pa^?byasca  kufra- mtrttqm  . .  küfrayaslqm  . .  Vr.  14.  o  f.;  usw.; — ahunafalca{^A.)  'Lariam  ^.46;  —  uita- vaitya  (Stverz.)  '"^aya  handatä  ya^amaide . .  haitiPca  afsmans^a  vacasca  vacaslal- llmca  /rasraa'knmca  ..'Vj.iS.y,  usw.;  — sp)ni:1.mainyBm  (Stverz.)  '"^qm  asaonzm  . . Vüiuxsa'irqm  (Stverz.)  '^qm  ..vaAisISistim (Stverz.)  'iqm\x.2.Zl;m-»i.  2)Bezeich- nung  für  alle  (anscheinend)**'  im  Gä^ä- dialekt  verfassten  Stücke  des  Awesta,  d.  s.  — ausser  den  eigentlichen  0<i>äs  —  AtxYHapt. und  die  vier  heiligen  Gebete  (V.  27. 13— 15, 54.  i  )'*'>;  nur  Plur-,  womit  entweder  die Gesammtheit  dieser  Li  tteratur  oder  einzelne Abschnitte  daraus  gemeint  sind  (s.  auch  A): imäsf  tg  haoma  °^ii  imä  h^nti  staomsyS'^. /0. 18;  — farS  amisä  sp>nta  ''ka  gJurvJin Y.2S.0;  —  tipma  vi  0(7  dcflö«/"/ Y.2(V.o, 430,  47-o,5io,S3°''  —  '"i'^byS  spintäbyd ratuxsa^räbyS  (Stverz.)  alaonibyö  Y.55.  i ; usw.;  —  tä  713  hmti  °äi7  har^'iravaitista
```


## [2026-09-05T20:45:12.776Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 tools/fetch_source.py \"https://abadis.ir/fatofa/%DA%AF%D8%A7%D9%87/\" --note \"page 168, root Gei, Persian gah 1 (music/tune) - Mo'in entry\" 2>&1 | tail -2\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/%DA%AF%D8%A7%D9%87\" --note \"page 168, root Gei, Persian gah\" 2>&1 | tail -2"
}
```


### [2026-09-05T20:45:17.407Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/3308cb93f29ca2fc.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/6de8e3ad6b73bce9.txt
```


## [2026-09-05T20:45:20.513Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### abadis گاه (moein)\"; grep -n -A20 \"فرهنگ معین\" 3308cb93f29ca2fc.txt | head -40\necho; echo \"#### wiktionary گاه\"; grep -n -B2 -A12 \"Etymology\" 6de8e3ad6b73bce9.txt | sed -n '1,60p'"
}
```


### [2026-09-05T20:45:20.596Z] TOOL RESULT

```
#### abadis گاه (moein)
70: فرهنگ معین
71-
72- [ په . ] (اِ. )۱ - آهنگ ، آواز.۲ - (پس . )به صورت پسوند در نام های آهنگ های موسیقی به کار رود: سه گاه ، چهارگاه .
73- ۱ - (پس . ) علامت اسم زمان که در آخر کلمه درمی آید مانند شامگاه صبح گاه ، و علامت اسم مکان نیز می باشد مانند دانشگاه ، آرامگاه . ۲ - (اِ. ) زمان ، وقت . ۳ - عصر، دوره .
74- [ په . ] (اِ. ) ۱ - تخت شاهی ، سریر. ۲ - مسند. ۳ - جا، مکان . ۴ - بوتة زرگران . 
75-
76- فرهنگ عمید
77-
78- ۱. وقتی، زمانی، هنگامی.
79-۲. بعضی اوقات، گاه گاهی.
80-۳. (اسم ) وقت، زمان، هنگام.
81-۴. زمان (در ترکیب با کلمۀ دیگر ): بامگاه، شامگاه، سحرگاه.
82-۵. مکان (در ترکیب با کلمۀ دیگر ): بزمگاه، پرستشگاه، رزمگاه، کشتارگاه، لشگرگاه.
83-۶. (اسم ) [قدیمی] فصل، موسم.
84-* گاه از گاه: [قدیمی] = * گاه گاه
85-* گاه به گاه: = * گاه گاه
86-* گاه گاه: بعضی اوقات.
87-* گاه وبیگاه:
88-۱. وقت و بی وقت.
89-۲. [قدیمی] همه وقت.
90-ظرفی که در آن سیم وزر ذوب می کردند، بوتۀ زرگری: شهان به خدمت او از عوار پاک شوند/ بدان مثال که سیم نبهره اندر گاه (فرخی: ۳۴۳ ).
--
249: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
250-
251- لینک ها 
252-
253- حقوق این سامانه وابسته به دیکشنری آبادیس می باشد. 
254-
255- استفاده از نوشتارهای این دیکشنری، با ذکر منبع، آزاد است. 
256-
257- © 2006-2026 abadis.ir

#### wiktionary گاه
66-
67- 1.3 
68: Etymology 1 
69-
70- 1.3.1 
71- Noun 
72-
73- 1.3.1.1 
74- Derived terms 
75-
76- 1.3.1.2 
77- Descendants 
78-
79- 1.3.2 
80- Adverb 
--
84-
85- 1.4 
86: Etymology 2 
87-
88- 1.4.1 
89- Noun 
90-
91- 1.4.1.1 
92- Derived terms 
93-
94- 1.4.2 
95- References 
96-
97- 2 
98- Sindhi 
--
104-
105- 2.2 
106: Etymology 
107-
108- 2.3 
109- Noun 
110-
111- 2.4 
112- References 
113-
114- Toggle the table of contents 
115-
116- گاه 
117-
118- 6 languages 
--
223- goh
224-
225: Etymology 1
226- [ edit ] 
227-
228- From Middle Persian [Book Pahlavi needed] ( gʾs ) , 𐫃𐫀𐫍 ( gʾh /⁠gāh⁠/ , “ place, throne, bed; time ” ) , from Old Persian [script needed] ( gāθu- , “ place; throne, chair ” ) , from Proto-Iranian *gātu- / *gāθu- , from Proto-Indo-Iranian [Term?] , from Proto-Indo-European *gʷem- ( “ to step ” ) . Cognate with Avestan 𐬔𐬁𐬙𐬎 ( gātu , “ place, seat, throne ” ) and Sanskrit गातु ( gātú , “ going; way; place ” ) , and Northern Luri گێ ( gı , “ time, shift ” ) . Compare the Iranian borrowings: Old Armenian գահ ( gah ) , Classical Syriac ܓܗܐ ( gāhā ) , Arabic جَاه ( jāh ) . Doublet of جاه ( jâh ) , which passed through Arabic.
229-
230- Noun
231- [ edit ] 
232-
233- گاه • ( gāh / gâh ) ( Tajik spelling гоҳ ) 
234-
```


## [2026-09-05T20:45:31.387Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nawk 'NR>280' 6de8e3ad6b73bce9.txt | grep -n -A14 \"^ Etymology 2\" | head -30"
}
```


### [2026-09-05T20:45:33.818Z] TOOL RESULT

```
1: Etymology 2
2- [ edit ] 
3-
4- Inherited from Middle Persian [Book Pahlavi needed] ( gʾs /⁠gāh⁠/ , “ Gatha ; hymn, song ” ) , from Avestan 𐬔𐬁𐬚𐬁 ( gāθā , “ Gatha ; song ” ) , from Proto-Indo-Iranian *gaHtʰás ( “ song ” ) from Proto-Indo-European *g⁽ʷ⁾eH-tHó-s , from the root Proto-Indo-European *g⁽ʷ⁾eH- ( “ to sing, cry ” ) .
5-
6- Noun
7- [ edit ] 
8-
9- گاه • ( gāh / gâh ) ( Tajik spelling гоҳ ) 
10-
11- ( archaic ) hymn , song 
12-
13- ( Can we verify ( + ) this sense?) Gatha , the most archaic segment of the Avesta , composed by Zoroaster himself
14-
15- Derived terms
```


## [2026-09-05T20:45:47.714Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%A7%DB%8C%D8%B4/\" \"https://en.wiktionary.org/wiki/%DA%AF%DA%86\" \"https://en.wiktionary.org/wiki/%D9%86%DB%8C%D8%A7%DB%8C%D8%B4\"; do python3 tools/fetch_source.py \"$u\" --note \"page 168 verification (niyayes / gac)\"; done 2>&1 | tail -5\ngrep -n \"گاتها\\|گات ها\" data/verification/sources/refs/MON_part1.txt data/verification/sources/refs/MON_part2.txt 2>/dev/null | head -5"
}
```


### [2026-09-05T20:45:53.191Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/aed0a4f6ad050155.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a07d432fbfb7527f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0c794c39de4978db.txt
```


## [2026-09-05T20:45:56.966Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### abadis نیایش moein\"; grep -n -A8 \"فرهنگ معین\" aed0a4f6ad050155.txt | head -14\necho; echo \"#### wikt گچ\"; awk 'NR>150' a07d432fbfb7527f.txt | grep -n -A6 \"^ Etymology\" | head -20\necho; echo \"#### wikt نیایش\"; awk 'NR>150' 0c794c39de4978db.txt | grep -n -A6 \"^ Etymology\" | head -20"
}
```


### [2026-09-05T20:45:59.825Z] TOOL RESULT

```
#### abadis نیایش moein
69: فرهنگ معین
70-
71- (یِ ) [ په . ] (اِمص . ) دعا، ستایش . 
72-
73- فرهنگ عمید
74-
75- ۱. دعا از روی تضرع و زاری.
76-۲. پرستش
77-۳. آفرین، ستایش: همه نیکویی ها ز گیتی به توست / نیایش ز فرزند گیرم نخست (فردوسی: ۲/۲۱۰ ). 
--
280: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد. 
281-
282- لینک ها 
283-

#### wikt گچ
6: Etymology
7- [ edit ] 
8-
9- Inherited from Middle Persian [Book Pahlavi needed] ( gc /⁠gač⁠/ , “ plaster, gypsum ” ) , ultimately from Akkadian 𒅎𒌓 ( IM.BABBAR /⁠gaṣṣu⁠/ , “ gypsum ” ) . Compare Khotanese [script needed] ( gatsä , “ gypsum ” ) , Arabic جَصّ ( jaṣṣ , “ plaster ” ) , Classical Syriac ܓܨܐ ( gaṣṣā , “ plaster ” ) from the same source.
10-
11- Pronunciation
12- [ edit ] 

#### wikt نیایش
```


## [2026-09-05T20:46:15.149Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN sing gāyati ===\"; grep -n \"gāyati\\|gayati\" SYN.txt | head -5\necho \"=== SYN galea/ship ===\"; grep -n -E \"galea|gaulos\" SYN.txt | head -5\necho \"=== WLD Bd1 gypsum/gaulos ===\"; grep -n -i \"gaulos\\|yvipos\\|Gips\" incoming/WLD/WLD_Bd1_pages.txt 2>/dev/null | head -5\necho \"=== WLD band3 gei sing ===\"; grep -n -E \"gā\\(i\\)-|gē\\(i\\)-|geiə\" WLD_band3.txt | head -5\necho \"=== SKT gypsum/galley ===\"; grep -n -i -E \"^gypsum|gypsum,|galley,\" SKT.txt | head -5"
}
```


### [2026-09-05T20:46:15.247Z] TOOL RESULT

```
=== SYN sing gāyati ===
=== SYN galea/ship ===
35015:Lat. cassis, galea Sw. hjelm SCr. kaciga
35029:Lat. galea (‘leather helmet’), prob. loanword fr. Grk. yadé ‘weasel, marten’, through generalization of ‘weasel skin’ to ‘skin, leather’. Cf. Grk. xuvén, lit. ‘dog’s skin’, but usually ‘helmet’. Walde-P. 1.630. Ernout-M. 409 (ad- versely). Walde-H. 1.579.
=== WLD Bd1 gypsum/gaulos ===
=== WLD band3 gei sing ===
=== SKT gypsum/galley ===
7335:Galley,  a  low  built  ship.   (F  ^ ga/t'ie.  —  O.  F.  golie ;  Low  L  ga/rm.  a Orig   nnknomi.
23588:rcl.  bice,  bijon.  blond,  blouse,  brattice, te«  (il,  biet'ze  (2),  broil  (2).  buffer  (,0, ffer  (3).  buffet  (I),  buffet  (j),  huffoon. ruattft  (burgoiict),  busk  (i),  buttress, t>ba|^  {»),  culibcr  ^calibre),  calipers, lirer,  champagne,  chcval-dc-frise,  chi- Bcry,  chiffonier,  cockaJe.  curlew,  davit, le,  dtMase,  drab  (a),  drape,  dupe,  ease, ibiiitlc  (O,  embattle  (a),  cmblaion,  era- S*  { I  \  emboM  (2),  embrasure,  embroider, ibroil,  entice,  entrench,  fribble,  frieze  (i), ppery,  furbelow,  galley,  galliot,  gallon, rland,  gasccmade,  gavotte,  gibbet,  giblets, (3),  gingham,  gobelin,  gormandise, lUTnand,  graze  (l)?,  greaves  (,a),  grouse, illotine,  guxxle,  harass,  haricot  (i),  hari- (a\  harlequin,  harlot,  harridan,  hnunt, ik  ;a],  jacKetf  jostle,  lawn  (^a),  lees, tch,  loo,  lozenge,  magnolia,  maraud, utia,  martinet,  martingale,  martlet,  mich, Trtise,  musit.  Nicotian,  pamphlet?,  pa- Kv  pedigree?,  pillory,  pinch,  pinchbeck vritma/  name),  pirouette,  piss,  pittance, plin,    ricochet,    roan,    sautcmc,    savoy,
23619:Creek  from  Persian :  cinnabar  (dnoper). l^Uinfrom  Greek  from  Persian :  aspara* I,  gypsum,  laudanum,  Magi,  tiar>y f^enek  from  Latin  from  Greek  from rsian:  caper  (2),  jujube,  ma^ic,  myrtle, XwA'ue,  parria,  satsaif,  ''£*''-
```


## [2026-09-05T20:46:17.857Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AFM جص ===\"; grep -n \"الجص\\|جص )\\|( جص\" AFM_pages.txt | head -5\necho \"=== ARB جص ===\"; grep -n \"الجص\" ARB_mo3rb.txt ARB_abdulraheem.txt 2>/dev/null | head -5\necho \"=== FSD gypsum ===\"; grep -n -i \"gypsum\" FSD_vol2.txt | head -3\necho \"=== HJB / LKT gips ===\"; grep -n -i \"gips\\|gypsum\" LKT.txt | head -5"
}
```


### [2026-09-05T20:46:17.950Z] TOOL RESULT

```
=== AFM جص ===
=== ARB جص ===
=== FSD gypsum ===
28196:frlttingjf.  (formelting  slass-maklng material),  garbagesf. (a  clestruotor),  hardening^.  (lor  atiffenlng  h!ttd)udieH), Improvlngsf.  (a  calcining  and  retinlng  furnace) ,   li(iuation> r.  or  Hquldatloiirf.  (for  separating  metals  of  different  inclt- Inff.pointH),  melti!ig=f.  (for  glass,  etc.),  moreor}-=f.  (tor obtaining  mercury  by  roasting  cinnabar),  oxidlzlngd., plumbers’ f.  (a  portable  so Werlng»IuruiU!e),  potsf.  (torliot- tle-gliws),mlwcSnK‘f.  (tororoa),  refiningd.,  regcncrat- 8ng»f.,  regenerative  f.,  or  regenoratory  f.  (a  raotallurgienl furnace  in  wWob  the  outgoing  gases  heal  the  Incoming  air), reheating af.  (for  ijlooma),  reverberatory  f.  (see  eevkk- BEn.vrouY),  roasUngsf.  (fororo),  sealing^f.  (tor  removin  ' scale  from  iron  alieots,  as  in  tin-plate  manufacture) .   smclt- logrf.,  solderingof-  (for  melting  .solder),  spreadtogsr.  (a aattenlng-furnaoo).  sweatSngrf.  (a liquation-rurnace),  tern- perlng'i.,  testaf.  (a  reverberatory  reflning-Iurnaco  for argenUterous  alloys),  weidingsf.,  etc.;  (2)  from  some  miv ohanlcal  feature,  arrangement,  or  characteristic :   as,  arc  f,  (In which  an  electric  arc  la  used  for  melting  steel,  etc.),  Mast gasrf.  (gas»hurning,  with  forced  draft),  block sf.  (a  bloom- ery),  blowpipe  f.  (having  powdered  fuel  blown  through  a pipe),  crucible  f.  (tor  reducing  ore,  etc.),  cupola  f.  (for melting  iron,  etc.;  see  cupola) ,   diaphragm  f.  (tor roasting ores  while  they  drop  from  one  shelf  to  another) ,   dumb  f. (for  ventilating  a   mine) ,   electric  f.  (a  smelting-furnace  in which  the  heat  Is  caused  by  an  electric  current),  enginesf. (a  boiler-furnace),  flowing (a  cupola  furnace),  gallery  f. (used  in  vitriol  distillation),  Indiuction  f.  (In  which  an  Iron ring  or  circular  channel,  forming  a   secondary  circuit,  ts  used to  fuse  metals,  as  Iron  and  steel,  when  an  alternating current  Is  applied  to  a   primary  circuil).  Injection  f.  (a laboratory  furnace  heated  by  a   flame  of  gas  and  air) ,   lamp« f.  (for  laboratory  use)  ,   mill  *f.  (tor  reheating  puddletUron), muHle*f.  (a  oupollng-turnaeo  having  a   muffle),  opens hearth  f.,  reflectlng«arc  f.  (acting  by  heat  rellectod  from a   voltaic  arc),  revolving  f.,  ring'top  f.  (a  eliarcoal-rurnaeo for  snioothlng-lrcm.s),  rotary  f.  (Hoe  kotari),  .shafj»f.  (an ore-reducing  furnace  In  which  tho  charge  falls  through  the flames  in  a   chimney),  spherical  f.,  tanksf.,  wlndsf.  (for melting,  having  a   iiowerful  nat- ural draft),  etc.;  (3)  from  the substance  treated  or  produced; as,  cast-stcel  f.  (a  cementation- furnace  for  rendering  steel homogeneou.s),  gypsumuf.  (for calcining  sulfate  of  lime) ,   lamp- black-f.  (for  Imperfect  conihus- tion  of  dead-oil.  etc.,  in  inahing lampblack) ,   lead  «f.,  malleablcj Iron  f.,  nltrlcmcld  f.  (for  salt- evaporation),  slag-f.  (reducing). soda«f.,  sulfatc-f.  (for  making salt-cake),  sugar-f.  (evaporat- ing cane-julce),  wroughtdron f.  (a  puddllng-funiaoe),  etc.;  (4) from  tho  inventor  or  place  of origin:  as.  Almain,  almond, or  tierman  f.  (for  separating, metals  from  flinders),  Belgian f.  (for  beating  zinc  ores  to  liber- ate the  metal),  Blchcroux’s  f.
28971:and  below  .stand-  I.  Mortising -gago.  2.  hhect- metal nrd  Bivc  being  Base.  3.  Gago  for  dotermmmg  screw- known  is  foL  and  ■Pitihes.  4.  Gage  for  setting  clapimards. lim,  or  in.ii<le  and  oumile  gages.  3.  -A  standard  measure- metit.  dlinenslcm.  quantity,  or  amount,  (1)  The  distance between  rails  or  between  wheel-treads,  as  In  a   railway.  See BitoAD-GAGK  tiiul  MAHaow-GAGE,  (2)  The  exposed  length of  a   tile,  slate,  or  shingle.  (:i)  The  amount  of  gypsum  added to  lime  plaster  to  hasten  its  .setting.  (4)  The  composition of  plaster  of  Paris  and  other  substances  used  In  making moidlugs,  decorations,  etc.  (6)  The  flneneas  of  a   textile  or netted  fabric,  as  Lace.  (0)  The  diameter  of  the  horo  of  a gun.  (7)  A   strip  of  metal  or  other  material  hy  which  the exact  space  occupied  by  type  of  a   certain  kind,  or  the  length of  a   page,  or  the  width  of  a   margin,  is  determined.  (8)  A notched  strip  of  polished  metal  or  hard  wood,  used  in  type- founding  to  regulate  the  dimensions,  slopes,  etc.,  of  letters. (iP  Same  as  gbip,  re.,  7.  ilO)  An  instrument  such  as  the .siphon-gage,  by  which  the  degree  of  exhaustion  in  the  re- ceiver of  an  air-pump  is  indicated.  3.  A'auf.  (1)  The draft  of  a   vessel.  (2)  The  position  of  a   ve.ssel  with regard  to  the  wind  and  to  another_  vessel.
28990:especially  liquid  contents.  2,  A   small  bank  of  slack or  other  rubbish  at  the  mouth  of  a   ntine-headiiig,  to fence  it  ofT,  3.  Gyp.stmi,  imed  in  pla.ster  to  cau.se  it  te> set.  4.  The  addition  of  gypsum  to  piaster,  gaag'tngt. —   gag'Ing*eal'd-per,  re.  A   tool  combining  calipers  with  » graduated  scratch-gage.— g. -line,  re.  The  graduated  scale on  the  rod  or  rule  employed  in  determining  the  capacity of  barrel.s,  etc,—  g.-rod,  g.<rule,  n.  A   gage-rod.
=== HJB / LKT gips ===
1752:'Gips'  [aus  gr.  yü^oq,  lat.  gypsum]; hieraus  it.  gesso,  pg.  gesso,  sp.  yeso,  algez [woraus  dann  wieder  ar.  gass,  vulg.  gess nach  dem  Orient  zurückgewandert  ist]. Die  übrigen  europäischen  Formen  des Wortes  sind  unmittelbar  aus  dem  Lat., z.  B.  frz.  gypse  [gewöhnlich  pMtre], dtsch.  Gyps,  Gips.  [Doch  i.st  es  nicht unwahrscheinhch,  daß  das  gr.-lat.  Grund- wort selbst  wieder  aus  dem  Orient stammt,  vgl.  hebr.  gä^ls  'Kristall'  Hiob 28,  18;  ZDMG  XXV,  542  f.  In  der  Tat deuten  der  alte  Gebrauch  des  Gipses  bei den  Ägyptern  und  in  Äthiopien  (vgl. Herodot  3,  24  u.  7,  69)  sowie  die  Her- kunft der  besten  Sorten  aus  Syrien (vgl.  Plinius  36,  59)  auf  orientalischen Ursprung  auch  des  Namens.]  Übrigens ist  auch  tk.  alcy  'Gips'  eine  verderbte Form  für  ar.  al-gibs.
2386:Vollständig-  kafr  aljahüd  'Judenpech, Asphalt';  hieraus  sp.  acafelar  'Tür  oder Fenster  zumauern,  eine  Wand  mit Gips  oder  Kalk  tünchen'  [Dicc  Gast  21a], pg.  acafelar  'mit  Stein  und  Kalk  zu- mauern' [Constancio  Dicc  9  c].  —  DE 51/52.
2869:'Koptisch,  ägyptisch',  fem.  kubtlja;  hier- aus sp.  alcabtea  'sehr  feine  Leinwand' [DE  78].  —  Auf  das  or.  Grund  wort  geht natürlich  der  Landesname  Aegyptus  mit seinen  Ableitungen  zurück,  z.  B.  Adj. aegyptus;  hieraus  it.  ghetto  'Judenviertel' [freilich  durch  Kontamination  mit  *jec- tns  'Gießerei'  <;  *jectare  <  jactare, weil  sich  in  Venedig,  wo  im  Jahre  1516 das  erste  Ghetto  eingerichtet  wurde,  an dieser  Stelle  vorher  Gießereien  befunden hatten,  vgl.  SPITZER  in  WuS  VI,  204/205 und  VII,  205].  Auf  aegyptius  ist  zurück- zuführen: frz.  igyptien  'Zigeuner'  [statt des  gewöhnlicheren  boMmien;  im  The- aterargot von  Paris  'schlechter  Schau- spieler'], engl.gipsy,  sp.güano  [die  beiden letzteren  auch  in  derBedeutung'Schmied', da  das  Gewerbe  des  Kaltschmiedes  sehr häufig  von  Zigeunern  ausgeübt  wird].  [ML 236.  Roth  Vi  Fr  4 1/42.  Warth  FEt  Wh  43.
```


## [2026-09-05T20:46:36.845Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK gaulos ===\"; grep -n -i \"gaulos\\|gaulós\\|milkpail\\|milk pail\" POK_full.txt | head -10\necho \"=== POK gypsum/Gips ===\"; grep -n -i \"gypsum\" POK_full.txt | head -5\necho \"=== HRN niyayes ===\"; grep -n -i \"niyāyišn\\|niyayisn\\|niyāyiš\\|nijāji\\|niyāyeš\\|nijâjis\" HRN.txt HUB.txt | head -10\necho \"=== CHEUNG gay sing ===\"; grep -n -E \"\\*gā|gāy|'to sing'\" CHEUNG.txt | head -10"
}
```


### [2026-09-05T20:46:36.936Z] TOOL RESULT

```
=== POK gaulos ===
60837:innr|MoAY6(;, (3ouijoAy6(; " steed-, Kuhmelker ', aiJoAy£U(;, apsAKirip " a milking-pail, milkpail 
60843:propose openly, publish, promulgate '; mulctra' a milking-pail, milkpail '; 
60856:High German chumelktra' a milking-pail, milkpail ' (perhaps replicated Latin mulctra). Old 
=== POK gypsum/Gips ===
52019:doubtful gr. Tiravoqf., m. " calc, lime, limestone, gypsum, chalk ' {*Ruit-3no-s), KiTiavoc; 
=== HRN niyayes ===
=== CHEUNG gay sing ===
```


## [2026-09-05T20:46:41.556Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"to sing\" CHEUNG.txt | head -10\necho \"=== HRN gah / gat ===\"; awk 'BEGIN{RS=\"\\f\"} NR==221' HRN.txt | grep -n -A4 \"889\""
}
```


### [2026-09-05T20:46:44.024Z] TOOL RESULT

```
6654:*CHORESMIAN: ? fn- ‘to sing’ (< *to praise, please with a song’ ?), Bry’k “honoured, 
7089:*gaH ‘to sing, call’ 
7106:*SANSKRIT: га ‘to sing’ (RV+) © EWAia I: 482 
7110:«PIE *¢™ eH-(i-) ‘to sing" > LIV: 183 | Pok.: 355 
7112:*IE COGNATES: ORuss. gajati ‘to croak [ravens]’, Lith. giedöti ‘to sing’ 
10181:Xan-/Xat- ‘to speak, say; to sing’, Yzgh. X"an-/X' ant- ‘to read (prayers, spells)’, 
11266:*Haré ‘to sing’ 
11268:*KHOTANESE: OKh. äljs- to sing’ = SGS: 11 
11270:*SANSKRIT: arc ‘to sing, praise’ (RV, AV+) = EWAia I: 114 
11272:«PIE *H;erk"- ‘to sing, praise" = LIV: 240 | Pok.: 340 
=== HRN gah / gat ===
2:889. ffäh *Ort (in Comp.) ; Thron*.
3-ap. gä&U' 'Ort; Thron', vergl. /7afja(>[}/«(5(</ ; aw. gätn-
4-Ort; Thron'; phlv. gas\ ai. gütü- 'Gang, Bahn, Kaum*,
5-afy. ^yälai.
6-890. f/e^^Mörtel'.
```


## [2026-09-05T20:46:48.265Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7089,7115p' CHEUNG.txt"
}
```


### [2026-09-05T20:46:48.314Z] TOOL RESULT

```
*gaH ‘to sing, call’ 

*AVESTAN: YAv. pairi.ga.vacah- ‘who sings the words around’ (Y 57.20), YAv. 
barazi.gädra- ‘singing high’ (Yt 10.89), Y Av. fragädra- (n.) ‘Absingen’, Y Av. ga0a- 
‘song, gatha’ 

*KHOTANESE: gaha- ‘verse’ 

*SOGDIAN: CSogd. Z'y, MSogd. j’y ‘to speak, talk’ (Schwartz, l.c.) 

Pres.: IND. 250. dur. CSogd. Zysq, 3р1. MSogd. j’ynd, dur. CSogd. Z'yntqn, SUBJ./OPT. 3sg. CSogd. 
Z’yt, 3р1. (dur. ?) CSogd. "Z'ynt; Fut.: SUBJ. Leg. CSogd. Z’ynq’; Partic.: pres. CSogd. Z’yq ‘talking’ 
*NWIR: (+ *apa-) ? NP afgan ‘lamentation, groaning, cries for help’ 

*NEIR: Yghn. Zoy-/Zóyta ‘to read, sing; to study’, Yzgh. yay-/yayd ‘to call’, Yi. 
žāy-/išt-, M. Zay-/St- ‘to say, speak’ 

*SANSKRIT: га ‘to sing’ (RV+) © EWAia I: 482 

© The MIr. (verbal) forms, Pth. ng’y-, etc. are rather from *Jad. 

«PIE *¢™ eH-(i-) ‘to sing" > LIV: 183 | Pok.: 355 

*IE COGNATES: ORuss. gajati ‘to croak [ravens]’, Lith. giedöti ‘to sing’ 

*REFERENCES: IFL П: 277a; Morgenstierne 1942: 263; Andreev — Peščereva: 370b; Schwartz, Gs 
Henning: 387, fn. 10; EVS: 38b; DKS: 82b; Werba 1997: 283
```


## [2026-09-05T20:46:55.809Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"niyāyišn\\|niyayisn\\|ny’yšn\\|nyāyišn\" CHEUNG.txt | head -10\necho \"---\"; grep -n \"^\\*Jad\\|\\*ǰad\\|Jad ‘to ask\" CHEUNG.txt | head -5"
}
```


### [2026-09-05T20:46:55.873Z] TOOL RESULT

```
14863:‘to entreat; honour’, BMP nyd’dsn /niyayisn/ ‘prayer, praise, worship’. © The loss of 
35428:nyd’dsn /niyayisn/, 221 
---
```


## [2026-09-05T20:46:57.989Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14845,14890p' CHEUNG.txt"
}
```


### [2026-09-05T20:46:58.038Z] TOOL RESULT

```
*jad 221 


Pres. ja-: IND. 1sg. YAv. jaióiiemi (Y 9.19 ff., Y 65.12), ҮАУ. jaióiiami (Y 65.11), 2sg. Y Av. jaidiiehi (Y 
11.2), 3sg. Y Av. “frajaidiieiti (F 248), 3pl. YAv. paiti.jaióiieinti (V 19.29), INJ. Zeg YAv. jaidiiat, 3р1. 
YAv. jaióiion (Yt 5.58), SUBJ. 3pl. YAv. "jaióiiánti (Yt 5.86 Ё), ОРТ. Zeg. YAv. jaióiioi$ (Y 65.10); 
Partic.: pres. YAv. jaiöliant- (Yt 5.19, Yt 5.53, Yt 10.11, etc.), med. Y Av. jaióiiamna- (Y 9.23, Y 68.21); 
Y Av. auua.jasti- (f.) ‘request’ (Y 65.10). 0 Kellens 1984: 258 apparently emends Y Av. SUBJ. med. 3pl. 
jaidiiante to “jaidiianti, which receives a justification on p. 43. 

*OLD PERSIAN: Jad- ‘to pray, ask’ — Kent: 184b 

Pres. Ја-: IND. 1sg. jadiyamiy <j-di-i-y-a-mi-i-y> (DPd 21, РМа 54), <j-di-i-y-a-mi-i-y> (XPh 59), 
<[]-[di]-li]-[y]-[a]-[mi]-Li]-y> (XSc 4) 

*MIDDLE PERSIAN: BMP zd- /zay-/ ‘to ask, demand, implore’ || (+ *ni-) MMP nyz’y- 
‘to entreat; honour’, BMP nyd’dsn /niyayisn/ ‘prayer, praise, worship’. © The loss of 
the velar *-g- in BMP nyd’dsn /niyayısn/, which may appear to be irregular, is due 
to the presence of the front vowel / glide -iy-, cf. MMP nyws-, ВМР n(y)dwhs- 
/niyö(x)s-/, NP niyös- ‘to listen’ (< *ni- + *gau$) MMP pyg’m, NP payam 
‘message’ (< *pati+ *gam!). > DMMPP: 256b f. 

Pres.: IND. 25р. BMP zdyh /zayé/, 1р1. BMP zdym /zayém/; Inf.: BMP zstn; Pass.: pret. IND. 3sg. BMP 
zst /zast/ || (+ *ni-) Pres.: IND. 2р1. MMP nyz’yd, 3р1. MMP nyz’ynd, SUBJ. 3pl. MMP *nyz’y’nd 
*PARTHIAN: (+ *a-) 'g'dg, "y'dg ‘wish’ || (+ *ni-) ng’y- ‘to pray, supplicate’, ng’d 
‘prayer, obeisance’, nyz’y- ‘to entreat; honour’. © On nyz’y- and MMP nyz’y- (etc.) 
cf. Gershevitch 1965: Le The Pth. verb nyz’y- is perhaps a borrowing from MP. 
= Ghilain: 60, 99, 86 | DMMPP: 29a, 256b f., 240 

(+ *ni-) Pres.: IND. Ipl. ng’y’m, 1р1. ng’y’m, 1р1. ng’y’m, 2р1. ng’yd, 3р1. nyg’ynd, SUBJ. 1pl. ng’y’m, 
ng’y’’m; Partic.: perf. pass. II nyz’y’’d 

*KHOTANESE: (+ *pati-) pajäd- ‘to ask for’ © SGS: 64 f. 

*SOGDIAN: (+ *ä-) BSogd. ”’y’yö, MSogd. ’’yy6 ‘to wish, desire’ || (+ *upa-) BSogd. 
"py ów ‘praise, fame’ || (+ *ni-) CSogd. ny’d’ (Е), MSogd. ny’ö’ ‘request, entreaty’ 
(+ *а-) Pres.: IND. 150. BSogd. ”’y’yö’m, 1р1. MSogd. ’’yyéym (BBB: 42) 

*CHORESMIAN: (+ *4-) m/’y’zy- ‘to wish, desire” = Samadi: 3 

*BACTRIAN: Cup- (pret. stem) ‘to request (as a bride)’ || (+ *a-) ayaAyo ‘wish’ 
c» S-W, Bact.: 192b f., 177a 

*NWIR: ? Abz. jay “quarrel, dispute’
```


## [2026-09-05T20:47:08.231Z] TOOL CALL #54: Bash

```json
{
 "command": "sed -n '1,80p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T20:47:08.289Z] TOOL RESULT

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


## [2026-09-05T20:47:10.922Z] TOOL CALL #55: Bash

```json
{
 "command": "sed -n '80,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-05T20:47:10.961Z] TOOL RESULT

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


## [2026-09-05T20:47:43.037Z] AGENT

Now I'll write the verification file.


## [2026-09-05T20:51:04.732Z] TOOL CALL #56: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build168.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json\n\nW = \"https://en.wiktionary.org/wiki/\"\n\ndoc = {\n  \"pdf_page\": 168,\n  \"book_page\": 138,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-05\",\n  \"entries\": []\n}\n\n# ---------------- entry 1: Akkadian Gassu ----------------\ne1 = {\n  \"entry\": 1,\n  \"root\": \"Gassu\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"Akkadian gaṣṣu (logographic IM.BABBAR) 'gypsum, plaster'\",\n  \"note\": (\"The root box is right in substance: Akkadian gaṣṣu is a real word and it is the \"\n           \"ultimate source of the whole Wanderwort family (Aramaic/Syriac gaṣṣā, Arabic jaṣṣ, \"\n           \"Greek γύψος, Latin gypsum, MP/NP gač). Nourai's gloss 'mortar' is loose — the word \"\n           \"means 'gypsum, plaster' (Horn's German 'Mörtel' for NP gač is what he is translating). \"\n           \"The shape of the chart, however, is wrong in two places: (a) Nourai routes MP/NP gač \"\n           \"through an Avestan word vīčiča-, which no source supports; (b) he hangs Arabic jaṣṣ \"\n           \"off Greek gypsos, whereas Zimmern and Klein derive jaṣṣ straight from Aramaic gaṣṣā \"\n           \"(only jabsīn / jafsīn come from Greek). Note that Nourai's own reference HRN:199 \"\n           \"(Horn no. 890) says nothing about Akkadian at all — the Akkadian etymon comes from \"\n           \"AKD:32 (Zimmern), which he cites only on the Greek node.\"),\n  \"note_fa\": (\"ریشهٔ اکدی gaṣṣu «گچ، اندود» واژه‌ای واقعی است و امروزه آن را سرچشمهٔ همهٔ این خانوادهٔ \"\n              \"واژگانی می‌دانند: آرامی/سریانی gaṣṣā، عربی جصّ، یونانی gypsos، لاتینی gypsum و فارسی میانهٔ \"\n              \"gač > فارسی نو «گچ». پس خودِ ریشه و برچسب زبانی درست است، هرچند معنای «ملاط» که نورایی \"\n              \"آورده دقیق نیست و باید «گچ، اندود» باشد. اما دو حلقهٔ نمودار نادرست است: نخست آنکه گچِ فارسی \"\n              \"را از راه واژه‌ای اوستایی (vīčiča-) می‌آورد که هیچ منبعی آن را تأیید نمی‌کند، و دیگر آنکه «جصّ» \"\n              \"عربی را از یونانی می‌گیرد، حال آنکه تسیمرن و کلاین آن را یکراست از آرامی gaṣṣā می‌دانند. \"\n              \"افزون بر این، مأخذی که خودِ نورایی برای ریشه آورده (هرن، ص۱۹۹) اصلاً از اکدی سخنی نمی‌گوید.\"),\n  \"sources\": [W + \"%CE%B3%CF%8D%CF%88%CE%BF%CF%82\", W + \"%DA%AF%DA%86\"],\n  \"ref_check\": [\n    {\"ref\": \"HRN:199\", \"status\": \"partial\",\n     \"note\": (\"Horn, Grundriss p.199 no. 890 (HRN.txt leaf 220): 'geč \\\"Mörtel\\\". aw. vīčica- \"\n              \"\\\"Mörtel\\\"; phlv. gač, gačīn. kurd. LW. gac \\\"Mörtel\\\". Die Zusammenstellung mit aw. \"\n              \"vīčica- ist unsicher.' — Horn has the Persian/Pahlavi/Avestan material Nourai uses \"\n              \"but no Akkadian word and no Akkadian etymology; and he himself calls the Avestan \"\n              \"connection 'unsicher'.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"AKD\", \"where\": \"Zimmern, Akkadische Fremdwörter, pp. 31–32\", \"stance\": \"supports\",\n     \"note\": (\"AKD.txt leaf 41: 'akk. gaṣṣu Gips : > aram. gaṣṣā (> arab. ǧaṣṣ, ǧiṣṣ, ǧuṣṣ, auch \"\n              \"qaṣṣ, qiṣṣ), griech. γύψος, lat. gypsum, Gips.' — the Akkadian etymon exactly as \"\n              \"Nourai's root box, but the Arabic goes through Aramaic, not through Greek.\")},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. 'gypsum' (KLN_1966.txt l.16951)\", \"stance\": \"supports\",\n     \"note\": (\"'gypsum, n. — L., fr. Gk. γύψος, \\\"chalk\\\", of Sem. origin. Cp. Arab. jibs, Mishnaic \"\n              \"Heb. gebhes, gephes … which prob. derive fr. Akkad. gassu (whence also Aram. gassā, \"\n              \"whence Arab. jass, jiss, juss, qaṣṣ, qiṣṣ), \\\"gypsum\\\".'\")},\n    {\"src\": \"POK\", \"where\": \"Pokorny IEW, grep 'gypsum'/'Gips'\", \"stance\": \"silent\",\n     \"note\": \"No IE root; Pokorny knows the word only as the Greek loan (POK_full.txt l.52019 mentions τίτανος 'lime, gypsum' elsewhere). As expected for a Semitic Wanderwort.\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch no. ~1752 s.v. 'Gips'\", \"stance\": \"partial\",\n     \"note\": (\"LKT.txt l.1752: 'Gips [aus gr. γύψος, lat. gypsum] … woraus dann wieder ar. ǧaṣṣ, \"\n              \"vulg. ǧess nach dem Orient zurückgewandert ist … Doch ist es nicht unwahrscheinlich, \"\n              \"daß das gr.-lat. Grundwort selbst wieder aus dem Orient stammt.' Lokotsch has the \"\n              \"Arabic coming back from Romance, but concedes an oriental source for the Greek.\")}\n  ],\n  \"nodes\": []\n}\n\ne1[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"vîčiča\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"The Avestan word is real but the arrow is not. Bartholomae AiW col. 1437 lists Younger \"\n                 \"Avestan vīčiδa- n. 'Kalk, Gips, Mörtel', attested only in Vendidad 8.51 and 6.10, and \"\n                 \"labels its etymology 'Et.?' — unknown; the Pahlavi Vendidad simply glosses it gač, which \"\n                 \"is why Horn (1893, no. 890) juxtaposed the two, adding at once 'die Zusammenstellung mit \"\n                 \"aw. vīčica- ist unsicher'. Nourai's spelling vīčiča follows Horn's 1893 reading (also in \"\n                 \"SNS:310); the standard reading since Bartholomae 1904 is vīčiδa-. No source derives the \"\n                 \"Avestan word from Akkadian gaṣṣu, and phonetically an Avestan borrowing would not give \"\n                 \"v-: Hübschmann (PSt. 90) showed that the initial g- of gač is original, guaranteed by \"\n                 \"Aramaic/Syriac gaṣṣā and Arabic jaṣṣ. The Akkadian word reached Iran directly (Wiktionary, \"\n                 \"s.v. گچ: MP gač 'ultimately from Akkadian gaṣṣu'), not through Avestan.\"),\n  \"derivation_fa\": (\"واژهٔ اوستایی هست، ولی پیکان نادرست است. بارتولومه در «فرهنگ ایرانی باستان» ستون ۱۴۳۷ صورت \"\n                    \"اوستایی نو vīčiδa- «گچ، آهک، ملاط» را می‌آورد (تنها در وندیداد ۸٫۵۱ و ۶٫۱۰) و در برابر \"\n                    \"ریشه‌شناسی آن می‌نویسد «؟». ترجمهٔ پهلوی وندیداد این واژه را gač برگردانده و همین سبب شده \"\n                    \"هرن (۱۸۹۳، شمارهٔ ۸۹۰) این دو را کنار هم بگذارد، اما خودِ او بی‌درنگ می‌افزاید که «این \"\n                    \"همسنجی نااستوار است». نگارش vīčiča در کتاب، خوانش کهنِ هرن است؛ خوانش معیار از بارتولومه \"\n                    \"به بعد vīčiδa- است. هیچ منبعی این واژهٔ اوستایی را وام‌گرفته از اکدی gaṣṣu نمی‌داند و \"\n                    \"هوبشمان (ص۹۰) نشان داده که «گ» آغازیِ گچ اصلی است و آرامی/سریانی gaṣṣā و عربی جصّ آن را \"\n                    \"گواهی می‌کنند. پس ادعای نورایی در این حلقه پذیرفتنی نیست.\"),\n  \"sources\": [W + \"%DA%AF%DA%86\"],\n  \"ref_check\": [\n    {\"ref\": \"HRN:199\", \"status\": \"partial\",\n     \"note\": (\"Horn no. 890 (HRN.txt leaf 220) does print 'aw. vīčica- \\\"Mörtel\\\"' beside 'phlv. gač' — so \"\n              \"the forms are Nourai's — but Horn adds 'Die Zusammenstellung mit aw. vīčica- ist unsicher' \"\n              \"and never mentions Akkadian, so he does not support the arrow drawn.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Altiranisches Wörterbuch col. 1437 (BRT.txt l.23946)\", \"stance\": \"contradicts\",\n     \"note\": (\"'j. vičiδa- n. \\\"Kalk, Gips, Mörtel\\\": … V. 8.51 … Et.? — Pü. (zu V.6): gač … D. i. \\\"aus gač \"\n              \"(= np. gač \\\"Kalk\\\") bestehend\\\"; s. dazu Hbm. PSt. 90.' Bartholomae reads -δ-, declares the \"\n              \"etymology unknown, and treats the Pahlavi gač only as the translator's gloss.\")},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p. 90 (note to Horn 890) and §117 p. 90\", \"stance\": \"contradicts\",\n     \"note\": (\"HUB.txt l.3206: 'Np. gač \\\"Kalk\\\" = phl. paz. gač Shk. 245 = arab. ǧaṣṣ \\\"Gips\\\", syr. geṣṣā \"\n              \"erweisen anl. g als ursprünglich.' Hübschmann uses the Semitic forms to prove the g- is \"\n              \"original, i.e. he rejects a derivation from a v-initial Avestan word.\")},\n    {\"src\": \"SNS\", \"where\": \"Tavoosi, Vazhe-name-ye Shayast ne Shayast, p. 310 s.v. gac\", \"stance\": \"partial\",\n     \"note\": (\"SNS_pages.txt l.12319 prints the entry 'gac' with the cross-reference '(1437) vīcica-', i.e. \"\n              \"it repeats Horn's/Bartholomae's juxtaposition (with Bartholomae's column number) without \"\n              \"asserting a derivation.\")}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Old Persian\", \"words\": \"gač\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"Two things are wrong here. (1) The language label: gač is not Old Persian — it is not \"\n                 \"attested in the Achaemenid inscriptions; it is Middle Persian / Book Pahlavi gc (gač), \"\n                 \"with the Pazand form gač (MacKenzie, PHD, English index 'gypsum gač', and the derivative \"\n                 \"gačēn 'of plaster'), and it is attested in the Pahlavi Šāyast nē Šāyast (SNS:310). \"\n                 \"(2) The parentage: no source takes MP gač from Avestan vīčiδa-. Wiktionary (s.v. گچ) and \"\n                 \"Wiktionary's γύψος entry both make MP gač a direct reflex of the Akkadian/Aramaic word \"\n                 \"(Akkadian gaṣṣu > Syriac gaṣṣā; cf. Khotanese gatsä 'gypsum'), i.e. a sister of Arabic \"\n                 \"jaṣṣ, not a descendant of an Avestan word. Nourai's own NOTE is therefore closer to the \"\n                 \"truth than his arrow: Mo'in (BQT:1776 footnote) and Hübschmann p.90 connect gač with \"\n                 \"Arabic jaṣṣ / Syriac gaṣṣā / Akkadian gaṣṣu; modern scholarship keeps the direction \"\n                 \"Akkadian → Aramaic → (Arabic, and independently) Iranian, and does NOT make Persian gač \"\n                 \"a loan from Arabic.\"),\n  \"derivation_fa\": (\"دو نکته در این جعبه نادرست است. نخست برچسب زبانی: gač «پارسی باستان» نیست و در کتیبه‌های \"\n                    \"هخامنشی نیامده؛ صورت فارسی میانه (پهلوی) gač است — مکنزی آن را ثبت کرده (gač، gačēn \"\n                    \"«گچین») و در متن پهلویِ «شایست نشایست» ص۳۱۰ نیز آمده است. دوم پیوند نسبی: هیچ منبعی \"\n                    \"gačِ فارسی میانه را از vīčiδa-ی اوستایی نمی‌گیرد؛ ویکی‌واژه آن را یکراست بازماندهٔ همان \"\n                    \"واژهٔ اکدی/آرامی می‌داند (اکدی gaṣṣu > سریانی gaṣṣā؛ قس ختنی gatsä)، یعنی خواهرِ «جصّ» \"\n                    \"عربی، نه فرزندِ واژه‌ای اوستایی. جالب آنکه یادداشت خودِ نورایی به حقیقت نزدیک‌تر از پیکان \"\n                    \"اوست: معین (حاشیهٔ برهان قاطع ص۱۷۷۶) و هوبشمان (ص۹۰) نیز گچ را با جصّ عربی و gaṣṣā \"\n                    \"سریانی و gaṣṣu اکدی می‌سنجند — با این تفاوت که پژوهش امروزی گچِ ایرانی را وام از عربی \"\n                    \"نمی‌داند، بلکه وام‌گیری مستقلی از همان سرچشمهٔ بین‌النهرینی می‌شمارد.\"),\n  \"sources\": [W + \"%DA%AF%DA%86\"],\n  \"ref_check\": [\n    {\"ref\": \"HRN:199\", \"status\": \"partial\",\n     \"note\": (\"Horn no. 890 gives 'phlv. gač, gačīn' — Pahlavi, expressly not Old Persian — under NP geč, and \"\n              \"flags the Avestan comparison as uncertain. So HRN supports the form but neither the language \"\n              \"label nor the arrow.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary (PHD.txt l.2184, l.5314)\", \"stance\": \"supports\",\n     \"note\": \"English–Pahlavi index 'gypsum gač', and the Pahlavi list 'diz, gač, gaz' / 'gačēn' — MacKenzie knows gač as a Middle Persian word, confirming the label should be Pahlavi, not Old Persian.\"},\n    {\"src\": \"HUB\", \"where\": \"Persische Studien §117 (HUB.txt l.8102) and p.90 note to 890\", \"stance\": \"contradicts\",\n     \"note\": \"'gač \\\"Kalk\\\" = paz. gač, aus phl. *gačč?, vgl. arab. jaṣṣ \\\"Gips\\\", syr. geṣṣā, gr. γύψος (Lehnwort?)' — a Middle Persian word tied to the Semitic group, not to Avestan.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.1776, Mo'in's footnote 2 s.v. گچ\", \"stance\": \"partial\",\n     \"note\": (\"ref_page.py BQT:1776 (v3 pdf p.573): 'پهلوی، پازند gač. معرب آن جص، سریانی geṣṣā … در اکدی \"\n              \"gaṣṣu' — Mo'in makes gač Pahlavi/Pazand and Arabic jaṣṣ the mu'arrab of it, with Akkadian \"\n              \"gaṣṣu behind; no Avestan and no Old Persian stage.\")}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Persian\", \"words\": \"gač «گچ»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"New Persian گچ gač 'plaster, gypsum' is the regular continuation of Middle Persian gač \"\n                 \"(Book Pahlavi gc, Pazand gač), which is itself the Iranian member of the Mesopotamian \"\n                 \"Wanderwort: Akkadian gaṣṣu → Aramaic/Syriac gaṣṣā → (independently) MP gač, Khotanese \"\n                 \"gatsä, Arabic jaṣṣ. There is no sound change to explain — the word passes unaltered from \"\n                 \"Sasanian to New Persian, and the Ferdowsi line quoted in the chart (به سنگ و به گچ دیو \"\n                 \"دیوار کرد) shows it in the earliest New Persian. Nourai's chart is right about the word \"\n                 \"and its Akkadian ancestry; only the Avestan/'Old Persian' staging above it is wrong.\"),\n  \"derivation_fa\": (\"«گچ» فارسی نو دنبالهٔ بی‌واسطهٔ gačِ فارسی میانه (پهلوی گ‌چ، پازند gač) است و هیچ دگرگونی \"\n                    \"آوایی در میان نیست. این واژه شاخهٔ ایرانیِ یک واژهٔ سرگردانِ بین‌النهرینی است: اکدی gaṣṣu \"\n                    \"← آرامی/سریانی gaṣṣā، و از همان سرچشمه به‌طور جداگانه فارسی میانه gač، ختنی gatsä و \"\n                    \"عربی «جصّ». شاهدِ فردوسی که در نمودار آمده کهن‌ترین کاربرد آن را در فارسی دری نشان می‌دهد. \"\n                    \"پس ادعای نورایی دربارهٔ خودِ واژه و خاستگاه اکدی آن درست است؛ تنها حلقه‌های اوستایی و \"\n                    \"«پارسی باستان» که بالای آن گذاشته نادرست‌اند.\"),\n  \"sources\": [W + \"%DA%AF%DA%86\"],\n  \"ref_check\": [\n    {\"ref\": \"SNS:310\", \"status\": \"supports\",\n     \"note\": (\"Tavoosi's Šāyast nē Šāyast glossary, word index: 'gac 310/18' (SNS_pages.txt l.16202), with \"\n              \"'gac kard 311/23' and 'gačēn 312/6'; the entry on p.310 (SNS_pages.txt l.12319) prints \"\n              \"'gac:' with the cross-reference to Bartholomae col. 1437. So p.310 is exactly the page \"\n              \"Nourai cites and it does attest the word.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.1776 s.v. گچ + Mo'in's footnote 2\", \"stance\": \"supports\",\n     \"note\": (\"'گچ - بفتح اول و سکون ثانی، خاکی باشد که آنرا پزند و بدان خانه سفید کنند'; footnote: 'پهلوی، \"\n              \"پازند gač. معرب آن جص، سریانی geṣṣā … کردی gač … در اکدی gaṣṣu' (ref_page.py BQT:1776).\")},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. gač / gačēn\", \"stance\": \"supports\",\n     \"note\": \"PHD.txt l.2184 'gypsum gač' and l.5316 'gačēn' — the Middle Persian antecedent of the New Persian word.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn no. 890, p.199\", \"stance\": \"supports\",\n     \"note\": \"'geč \\\"Mörtel\\\" … phlv. gač, gačīn' — the NP→MP link is Horn's, and it is uncontroversial.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Greek\", \"words\": \"gupsos\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Ancient Greek γύψος 'chalk, gypsum, plaster' (Herodotus, Theophrastus) is a Semitic \"\n                 \"loanword taken over during the archaic/classical contact with the Levant: Akkadian gaṣṣu \"\n                 \"passed into Aramaic/Syriac gaṣṣā, and Greek rendered the Semitic emphatic ṣ with ψ before \"\n                 \"the -os ending (γύψ-ος), with u-vocalism as in the West-Semitic variants (Arabic ǧuṣṣ, \"\n                 \"Mishnaic Hebrew gebhes/gephes 'plaster'). Klein and Zimmern both state the chain \"\n                 \"explicitly; Wiktionary is more cautious ('of unknown origin; possibly a Wanderwort, cf. \"\n                 \"Akkadian gaṣṣu > Syriac gaṣṣā and MP gač'), but nobody proposes an Indo-European source, \"\n                 \"so Nourai's Akkadian → Greek arrow is the standard view.\"),\n  \"derivation_fa\": (\"یونانی باستان γύψος «گچ، اندود» (هرودوت، تئوفراستوس) وام‌واژه‌ای سامی است که در دورهٔ \"\n                    \"داد و ستد یونانیان با شام وارد یونانی شده: اکدی gaṣṣu ← آرامی/سریانی gaṣṣā، و یونانی \"\n                    \"صادِ مفخّم سامی را با ψ نشان داده و پایانهٔ -ος بدان افزوده است؛ واکهٔ u نیز با گونه‌های \"\n                    \"سامی غربی (عربی جُصّ، عبری میشنایی gebhes) می‌خواند. کلاین و تسیمرن این زنجیره را با \"\n                    \"همین صراحت آورده‌اند و ویکی‌واژه محتاطانه آن را «واژهٔ سرگردان» می‌نامد؛ هیچ‌کس خاستگاه \"\n                    \"هندواروپایی برای آن پیشنهاد نکرده است. پس ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%CE%B3%CF%8D%CF%88%CE%BF%CF%82\"],\n  \"ref_check\": [\n    {\"ref\": \"AKD:32\", \"status\": \"supports\",\n     \"note\": (\"Zimmern, Akkadische Fremdwörter, p.31/32 (AKD.txt leaf 41): 'akk. gaṣṣu Gips : > aram. gaṣṣā \"\n              \"(> arab. ǧaṣṣ …), griech. γύψος, lat. gypsum, Gips.' — precisely Nourai's Akkadian → Greek → \"\n              \"Latin line.\")},\n    {\"ref\": \"AHD:588\", \"status\": \"not_checked\",\n     \"note\": \"AHD:588 is a page of the main dictionary body of the 1975 New College edition (the entry 'gypsum'), not of Watkins's IE-roots appendix; only the appendix (AHD_watkins1985.txt) is on disk and it has no gypsum root — as expected for a Semitic loan.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. gypsum (KLN_1966.txt l.16951)\", \"stance\": \"supports\",\n     \"note\": \"'L., fr. Gk. γύψος, \\\"chalk\\\", of Sem. origin … which prob. derive fr. Akkad. gassu (whence also Aram. gassā …).'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, word-list of borrowings (SKT.txt l.23619)\", \"stance\": \"partial\",\n     \"note\": \"Skeat files gypsum under 'Latin from Greek from Persian', i.e. an older view that made the Greek word Iranian (from gač) rather than Akkadian; the direction of the loan is the point at issue, the oriental source is not.\"},\n    {\"src\": \"POK\", \"where\": \"Pokorny IEW\", \"stance\": \"silent\", \"note\": \"No IE root for γύψος; grep of POK_full.txt returns only unrelated 'lime/gypsum' glosses (l.52019).\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Arabic\", \"words\": \"jabsîn, jass, jafsîn\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Two of the three words hang correctly under Greek, one does not. جبسين jabsīn and جفسين \"\n                 \"jafsīn are Arabic adaptations of Greek γύψινος gypsinos 'made of gypsum' (the adjective, \"\n                 \"not the noun), with the usual Arabic treatment of Greek υ as -i- and of the Greek \"\n                 \"nominative ending as -īn; Hübschmann already stated this ('Arab. pers. jabsīn \\\"gypsum\\\" \"\n                 \"aus gr. γύψος, γύψινος', PSt. pp.90–91), and Mo'in repeats it in the BQT:1776 footnote \"\n                 \"citing Hübschmann 89. جصّ jaṣṣ, however, is not from Greek: Zimmern and Klein derive it \"\n                 \"from Aramaic gaṣṣā, i.e. straight from Akkadian gaṣṣu, with the regular Aramaic g- → \"\n                 \"Arabic ǧ- and the emphatic ṣ preserved — a sister of Persian gač, not a descendant of \"\n                 \"gypsos. The node therefore mixes a Greek-mediated pair with a directly Semitic word.\"),\n  \"derivation_fa\": (\"از سه واژهٔ این جعبه، دو تا درست زیر یونانی نشسته‌اند و یکی نه. «جبسین» و «جفسین» \"\n                    \"برگردان عربیِ صفت یونانی γύψινος (gypsinos) «گچی» است؛ υ یونانی در عربی به ـِ و پایانهٔ \"\n                    \"یونانی به ـین بدل شده است. هوبشمان (ص۹۰–۹۱) همین را گفته و معین در حاشیهٔ برهان قاطع \"\n                    \"ص۱۷۷۶ با ارجاع به هوبشمان آن را تکرار کرده است. اما «جصّ» از یونانی نیامده: تسیمرن و \"\n                    \"کلاین آن را از آرامی gaṣṣā و در نهایت از اکدی gaṣṣu می‌دانند، با ابدال قاعده‌مندِ گ \"\n                    \"آرامی به ج عربی و نگهداشتِ صاد؛ یعنی «جصّ» خواهرِ «گچ» است نه فرزندِ gypsos. پس این \"\n                    \"حلقه با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W + \"%CE%B3%CF%8D%CF%88%CE%BF%CF%82\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:1776\", \"status\": \"supports\",\n     \"note\": (\"ref_page.py BQT:1776 (Borhan v3 pdf p.573), Mo'in's footnote 2 to گچ: 'پهلوی، پازند gač. معرب \"\n              \"آن جص، سریانی geṣṣā. کلمهٔ عربی-فارسی jabsīn (jafsīn) از یونانی gypsos, gypsinos آمده \"\n              \"«هوبشمان ۸۹» … در اکدی gaṣṣu' — supports the Greek source of jabsīn/jafsīn and, at the same \"\n              \"time, shows jaṣṣ as the mu'arrab of gač rather than a Greek loan.\")},\n    {\"ref\": \"TAD:20\", \"status\": \"supports\",\n     \"note\": (\"al-Unaysi, Tafsir al-alfaz al-dakhila (TAD_pages.txt l.822, leaf 24): \"\n              \"'جص - (وجص وجفسين وجبسين) يوناني gypsos وفي اللاتينية gypsum وهو سلفات الكلس الممتزج بالماء \"\n              \"يطلى به' — al-Unaysi puts all the Arabic forms, jaṣṣ included, under Greek gypsos, which is \"\n              \"exactly Nourai's arrow (though modern Semitists split jaṣṣ off).\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien pp. 90–91, note to Horn 890\", \"stance\": \"supports\",\n     \"note\": \"HUB.txt l.3208 / leaf 102: 'Arab. pers. jabsīn \\\"gypsum\\\" aus gr. γύψος, γύψινος (nicht umgekehrt wie Prellwitz … meint).' Hübschmann even insists the direction is Greek → Arabic.\"},\n    {\"src\": \"AKD\", \"where\": \"Zimmern pp.31–32\", \"stance\": \"partial\",\n     \"note\": \"'akk. gaṣṣu Gips : > aram. gaṣṣā (> arab. ǧaṣṣ, ǧiṣṣ, ǧuṣṣ, auch qaṣṣ, qiṣṣ), griech. γύψος' — jaṣṣ comes from Aramaic, in parallel with (not out of) the Greek.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. gypsum\", \"stance\": \"partial\",\n     \"note\": \"'Cp. Arab. jibs … which prob. derive fr. Akkad. gassu (whence also Aram. gassā, whence Arab. jass, jiss, juss …)' — same split.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"Persian\", \"words\": \"jabsîn «جبسین»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Persian جبسین jabsīn 'gypsum' is the Arabic word taken back into Persian — a learned/\"\n                 \"pharmacological borrowing of the kind common in the medical literature, where the Greek \"\n                 \"term had already entered Arabic through the translation movement of the 9th c. Mo'in, in \"\n                 \"the very footnote Nourai is citing (BQT:1776), calls it 'کلمهٔ عربی-فارسی' — an \"\n                 \"Arabic-Persian word — and traces it to Greek gypsos/gypsinos after Hübschmann, so the \"\n                 \"Arabic → Persian arrow, and the fact that Persian has both the inherited گچ and the \"\n                 \"borrowed جبسین as a doublet, is well founded.\"),\n  \"derivation_fa\": (\"«جبسین» فارسی همان واژهٔ عربی است که دوباره به فارسی بازگشته؛ وامی است دانشورانه و بیشتر \"\n                    \"در متون پزشکی و داروشناسی، از آن دست وام‌واژه‌هایی که از راه نهضت ترجمهٔ سدهٔ سوم هجری \"\n                    \"از یونانی به عربی و از عربی به فارسی رسیده‌اند. معین در همان حاشیه‌ای که نورایی بدان \"\n                    \"ارجاع می‌دهد (برهان قاطع ص۱۷۷۶) آن را «کلمهٔ عربی-فارسی» می‌خواند و به پیروی از هوبشمان \"\n                    \"از یونانی gypsos/gypsinos می‌گیرد. پس «گچ» و «جبسین» در فارسی دوگانه (doublet)‌اند: \"\n                    \"یکی میراثی و دیگری وام‌گرفته. ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%CE%B3%CF%8D%CF%88%CE%BF%CF%82\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT\", \"status\": \"supports\",\n     \"note\": (\"Borhan-e Qate', Mo'in's footnote on p.1776 (ref_page.py BQT:1776): 'کلمهٔ عربی - فارسی \"\n              \"jabsīn (jafsīn) از یونانی gypsos, gypsinos آمده «هوبشمان ۸۹»' — Nourai's bare 'BQT' on this \"\n              \"node is the same footnote he cites as BQT:1776 on the Arabic node.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"HUB\", \"where\": \"Persische Studien p.90 (note to 890)\", \"stance\": \"supports\",\n     \"note\": \"'Arab. pers. jabsīn \\\"gypsum\\\" aus gr. γύψος, γύψινος' — Hübschmann labels the word explicitly 'Arabic-Persian', i.e. current in Persian too.\"},\n    {\"src\": \"TAD\", \"where\": \"al-Unaysi, leaf 24 (printed ~p.20)\", \"stance\": \"supports\",\n     \"note\": \"'جص - (وجص وجفسين وجبسين) يوناني gypsos …' — jabsīn listed among the borrowed forms.\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 7, \"lang\": \"Latin\", \"words\": \"gypsum\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Latin gypsum is a straight borrowing of Greek γύψος, taken over with the neuter -um \"\n                 \"ending as usual for Greek technical nouns in -ος (cf. Plinius, Nat. Hist. 36.59-60, who \"\n                 \"discusses the best kinds from Syria and Cyprus). Latin y renders Greek υ. From Latin come \"\n                 \"Italian gesso and Spanish yeso (Klein s.v. gesso), and the learned form gypsum survives \"\n                 \"unchanged in the modern scientific vocabulary.\"),\n  \"derivation_fa\": (\"لاتینی gypsum وام مستقیم از یونانی γύψος است، با پایانهٔ خنثای -um که در وام‌گیری \"\n                    \"اسم‌های فنی یونانیِ ‎-ος به لاتین معمول است؛ حرف y لاتینی همان υ یونانی را می‌نماید. \"\n                    \"پلینیوس (تاریخ طبیعی ۳۶٫۵۹–۶۰) از بهترین گونه‌های آن در سوریه و قبرس سخن گفته است. از \"\n                    \"لاتین، ایتالیایی gesso و اسپانیایی yeso برآمده و صورت دانشورانهٔ gypsum بی‌تغییر در \"\n                    \"زبان علمی امروز مانده است. ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%CE%B3%CF%8D%CF%88%CE%BF%CF%82\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"not_checked\",\n     \"note\": \"Nourai cites AHD without a page; the Latin < Greek step is in the main dictionary body of the 1975 New College edition, which is not on disk (only Watkins's IE appendix is).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. gypsum and gesso\", \"stance\": \"supports\",\n     \"note\": \"'gypsum, n. — L., fr. Gk. γύψος'; 'gesso, n., plaster of Paris. — It., fr. L. gypsum' (KLN_1966.txt ll.16081, 16951).\"},\n    {\"src\": \"AKD\", \"where\": \"Zimmern p.32\", \"stance\": \"supports\",\n     \"note\": \"'… griech. γύψος, lat. gypsum, Gips.'\"},\n    {\"src\": \"LKT\", \"where\": \"Lokotsch s.v. Gips\", \"stance\": \"supports\",\n     \"note\": \"'[aus gr. γύψος, lat. gypsum]; hieraus it. gesso, pg. gesso, sp. yeso, algez' (LKT.txt l.1752).\"}\n  ]\n})\n\ne1[\"nodes\"].append({\n  \"id\": 8, \"lang\": \"English\", \"words\": \"gypsum\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"English gypsum is a direct 17th-century learned borrowing of the Latin word (first \"\n                 \"attested in English scientific writing in the 1640s), not a popular inheritance through \"\n                 \"French — French uses gypse/plâtre. It is the mineralogical name for hydrated calcium \"\n                 \"sulphate, the material of plaster of Paris; the doublet gesso came separately via \"\n                 \"Italian. The unbroken chain Akkadian → Greek → Latin → English is exactly what Klein and \"\n                 \"Zimmern give.\"),\n  \"derivation_fa\": (\"انگلیسی gypsum وام دانشورانه‌ای است که در سدهٔ هفدهم میلادی (نخستین کاربردها در دههٔ \"\n                    \"۱۶۴۰) یکراست از لاتین گرفته شده، نه از راه فرانسه (که gypse/plâtre به کار می‌برد). این \"\n                    \"واژه نام کانی‌شناختیِ سولفات کلسیم آبدار است. صورت gesso هم جداگانه از ایتالیایی به \"\n                    \"انگلیسی رسیده و دوگانهٔ آن است. زنجیرهٔ اکدی ← یونانی ← لاتین ← انگلیسی دقیقاً همان است \"\n                    \"که کلاین و تسیمرن آورده‌اند؛ ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%CE%B3%CF%8D%CF%88%CE%BF%CF%82\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. gypsum, gypseous, Gypsophila\", \"stance\": \"supports\",\n     \"note\": \"KLN_1966.txt ll.16950-16951: the English family (gypseous, gypsiferous, Gypsophila, gypsum) is derived from Latin gypsum < Gk. γύψος.\"},\n    {\"src\": \"FSD\", \"where\": \"Funk & Wagnalls, 'gypsum-furnace', 'gage' (FSD_vol2.txt ll.28196, 28990)\", \"stance\": \"supports\",\n     \"note\": \"The word is current English for the mineral used in plaster ('the amount of gypsum added to lime plaster to hasten its setting').\"}\n  ]\n})\n\ndoc[\"entries\"].append(e1)\nPYEOF\necho ok"
}
```


### [2026-09-05T20:51:07.735Z] TOOL RESULT

```
ok
```


## [2026-09-05T20:53:08.642Z] TOOL CALL #57: Bash

```json
{
 "command": "cat >> /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build168.py <<'PYEOF'\n\n# ---------------- entry 2: Indo-European Ğaulos ----------------\ne2 = {\n  \"entry\": 2,\n  \"root\": \"Ğaulos\",\n  \"verdict\": \"disputed\",\n  \"modern_form\": \"Ancient Greek γαυλός / γαῦλος 'round vessel, milk-pail; Phoenician merchant ship' — a Semitic (Akkadian gullu / gullatu) loanword, not a PIE root\",\n  \"note\": (\"Nourai's root box is copied faithfully from Mann: IEC col. 388 has 'ĝaulos (?) \\\"vessel, boat\\\". \"\n           \"Per. cf. zauraq \\\"ship, vessel\\\"; Gk. gaūlos \\\"merchant-ship\\\"; gaulós \\\"milkpail\\\". Cf. ĝeul-' — \"\n           \"the very gloss, the very Persian and Greek words. But Mann marks it with a question mark, and \"\n           \"Pokorny has no such root at all. Modern scholarship goes the other way: Wiktionary (with Beekes) \"\n           \"takes γαῦλος 'Phoenician merchant-ship' to be a loan 'via Phoenician or a near language from \"\n           \"Akkadian gullu \\\"a container\\\", gullatu \\\"ewer\\\"', the same Wanderwort that gave Hebrew gullāh, \"\n           \"Aramaic/Syriac qulləṯā, Arabic qulla, Latin culullus. So the box is a Semitic culture-word, \"\n           \"not an Indo-European root. Worse, Nourai has silently attached the galley family (Gk./Lat. \"\n           \"galea) to it, which belongs to a completely different and unrelated word.\"),\n  \"note_fa\": (\"جعبهٔ ریشه را نورایی وفادارانه از مان (Mann) گرفته است: در «فرهنگ تطبیقی هندواروپایی» ستون ۳۸۸ \"\n              \"آمده «ĝaulos (؟) ظرف، کشتی؛ فارسی zauraq، یونانی gaūlos «کشتی بازرگانی»، gaulós «سطل شیر»» — \"\n              \"همان معنا و همان واژه‌های فارسی و یونانی. اما مان خود در برابر آن نشانِ پرسش گذاشته و پوکورنی \"\n              \"اصلاً چنین ریشه‌ای ندارد. پژوهش امروزی راه دیگری می‌رود: γαῦλος «کشتی بازرگانی فنیقی» را \"\n              \"وام‌واژه‌ای می‌داند که از راه فنیقی از اکدی gullu «ظرف» و gullatu «کوزه» آمده است — همان واژهٔ \"\n              \"سرگردانی که عبری gullāh، سریانی qulləṯā، عربی «قُلّه» و لاتینی culullus از آن‌اند. پس این جعبه \"\n              \"یک واژهٔ فرهنگیِ سامی است، نه ریشهٔ هندواروپایی. افزون بر آن، نورایی خانوادهٔ galea/galley را نیز \"\n              \"بی‌هیچ سندی بدان چسبانده که واژه‌ای یکسره جداست. پژوهش امروزی این ریشه را نمی‌پذیرد.\"),\n  \"sources\": [W + \"%CE%B3%CE%B1%CF%85%CE%BB%CF%8C%CF%82\", \"https://www.etymonline.com/word/galley\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:388\", \"status\": \"supports\",\n     \"note\": (\"Mann, An Indo-European Comparative Dictionary, col. 388-389 (IEC.txt form-feed page 227): \"\n              \"'ĝaulos (?) \\\"vessel, boat\\\" Per. cf. zauraq \\\"ship, vessel\\\"; Gk. gaūlos \\\"merchant-ship\\\"; \"\n              \"gaulós \\\"milkpail\\\". Cf. ĝeul-'. Nourai's root box is verbatim Mann, including the Persian \"\n              \"word; the '(?)' is Mann's own reservation, which Nourai drops.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"Pokorny IEW (grep 'gaulos', 'milkpail')\", \"stance\": \"silent\",\n     \"note\": \"No lemma *ĝaulos; the only 'milkpail' hits (POK_full.txt ll.60837-60856) are under the root for 'milk' (ἀμολγεύς, mulctra), unrelated.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny\", \"stance\": \"silent\",\n     \"note\": \"Grep of the WLD volumes for gaulos/γαυλός returns nothing; the etymon is absent from the standard IE comparative dictionary.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck, Dict. of Selected Synonyms §12.73/§4.86 (SYN.txt l.35029)\", \"stance\": \"contradicts\",\n     \"note\": \"Buck on galea: 'Lat. galea (\\\"leather helmet\\\"), prob. loanword fr. Grk. γαλέη \\\"weasel, marten\\\", through generalization of \\\"weasel skin\\\" to \\\"skin, leather\\\"' — galea has nothing to do with a vessel or boat.\"}\n  ],\n  \"nodes\": []\n}\n\ne2[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Persian\", \"words\": \"zowraq «زورق»; zowraqî «زورقی»\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"Both words are real and correctly glossed. Persian زورق zowraq 'skiff, small boat' goes \"\n                 \"back to a Middle Persian *zōwrak (Wiktionary), and it is Persian that gave Arabic زَوْرَق \"\n                 \"zawraq 'boat, dinghy, skiff' (pl. zawāriq), not the other way round — so this is an \"\n                 \"Iranian word that travelled into Arabic and came back to Persian in Arabicised dress. \"\n                 \"زورقی zowraqī is the Persian relative adjective in -ī used substantivally: Borhan-e Qate' \"\n                 \"defines it 'نوعی از کلاه قلندران است و آن شبیه است بکشتی' — a kind of qalandar's cap \"\n                 \"shaped like a boat, exactly Nourai's gloss. What is not established is the arrow itself: \"\n                 \"the only authority for attaching zowraq to an Indo-European *ĝaulos is Mann's queried \"\n                 \"entry, which merely writes 'Per. cf. zauraq'; no Iranist derivation of the word exists, \"\n                 \"and Wiktionary stops at MP *zōwrak.\"),\n  \"derivation_fa\": (\"هر دو واژه واقعی‌اند و معنی‌شان درست آمده است. «زورق» فارسی به فارسی میانهٔ *zōwrak \"\n                    \"بازمی‌گردد و همین واژهٔ ایرانی است که به عربی رفته و «زَوْرَق» (جمع: زوارق) شده — نه \"\n                    \"برعکس؛ یعنی وام‌گیریِ رفت‌وبرگشتی از فارسی به عربی و باز به فارسی. «زورقی» صفت نسبیِ \"\n                    \"فارسی است که اسم شده؛ برهان قاطع آن را چنین آورده: «نوعی از کلاه قلندران است و آن شبیه \"\n                    \"است بکشتی» — درست همان معنایی که نورایی نوشته. آنچه اثبات‌نشده مانده خودِ پیکان است: \"\n                    \"تنها گواهِ پیوند «زورق» با ریشهٔ فرضی هندواروپایی، مدخل پرسش‌دارِ مان است که همان‌جا هم \"\n                    \"فقط می‌نویسد «قس فارسی zauraq». هیچ ریشه‌شناسی ایرانی‌شناسانه‌ای این پیوند را نپرداخته \"\n                    \"است؛ پس با احتیاط پذیرفتنی است.\"),\n  \"sources\": [W + \"%D8%B2%D9%88%D8%B1%D9%82\"],\n  \"ref_check\": [\n    {\"ref\": \"AEC:388\", \"status\": \"supports\",\n     \"note\": (\"'AEC' is not a key in Nourai's bibliography (it is absent from refs_online.json); the printed \"\n              \"page (pdf 168) really does read 'AEC:388', evidently the author's misprint for IEC:388 — the \"\n              \"same page of Mann he cites on the root box, and Mann's col. 388 does read 'Per. cf. zauraq \"\n              \"\\\"ship, vessel\\\"' under ĝaulos. Book misprint, faithfully extracted.\")},\n    {\"ref\": \"BQT:1044\", \"status\": \"partial\",\n     \"note\": (\"The Borhan entries are where Nourai says: BQT_v2_pages.txt l.30090 f. has 'زورق سیمین، کنایه \"\n              \"از ماه' and 'زورقی - نوعی از کلاه قلندران است، وآن شبیه است بکشتی', with cross-references \"\n              \"'رك: زورق' / 'رك: زورقی'. So Borhan supports the two words and their glosses; Mo'in's \"\n              \"etymological footnote on that page is too damaged in the OCR (and the page is outside the \"\n              \"available BQT scans) to be read, so the etymology is unchecked.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"IEC\", \"where\": \"Mann col. 388\", \"stance\": \"supports\",\n     \"note\": \"'ĝaulos (?) \\\"vessel, boat\\\" Per. cf. zauraq \\\"ship, vessel\\\"' — the only book that connects the Persian word to the root.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' s.v. زورق / زورقی (BQT_v2_pages.txt ll.30008, 30090)\", \"stance\": \"supports\",\n     \"note\": \"The headwords and the 'boat-shaped qalandar cap' sense are both there.\"},\n    {\"src\": \"PLA\", \"where\": \"Asbaghi, Persische Lehnwörter im Arabischen\", \"stance\": \"silent\",\n     \"note\": \"grep for zawraq / زورق in PLA_pages.txt returns nothing — Asbaghi does not list it among the Persian loans in Arabic.\"},\n    {\"src\": \"AFM\", \"where\": \"Addi Shir, al-Alfaz al-farisiyya al-mu'arraba\", \"stance\": \"silent\",\n     \"note\": \"The only hit for زورق (AFM_pages.txt l.2429) is a quotation from the Taj al-'Arus s.v. sunbuq ('زورق سفر يعمل في سواحل …'), not an entry deriving zawraq from Persian.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Greek\", \"words\": \"gaulos, galea\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"γαῦλος / γαυλός is genuine and correctly glossed: Herodotus (3.136, 6.17) uses γαῦλος of \"\n                 \"the round-built Phoenician merchantman, and γαυλός is a milk-pail/round vessel. But it is \"\n                 \"almost certainly not Indo-European: Wiktionary, following Beekes, derives it 'via \"\n                 \"Phoenician or a near language from Akkadian gullu \\\"a container\\\", gullatu \\\"ewer\\\"'. \"\n                 \"'galea' does not belong here at all. There is no classical Greek γαλέα 'merchant ship'; \"\n                 \"the ship-word is Byzantine Greek γαλέα (attested from the 9th c. in Byzantine naval \"\n                 \"texts), from Late Greek γαλία, a sea-fish, ultimately γαλέη 'weasel' (Klein), and \"\n                 \"Etymonline flatly calls Late Greek galea 'of unknown origin'. Classical Greek γαλέα is \"\n                 \"not a ship but the source of Latin galea 'leather helmet' (Buck). Nourai has merged two \"\n                 \"unrelated words on the strength of their look.\"),\n  \"derivation_fa\": (\"γαῦλος/γαυλός واژه‌ای راستین و درست معنی‌شده است: هرودوت (۳٫۱۳۶ و ۶٫۱۷) آن را برای کشتی \"\n                    \"بازرگانیِ گِردساختِ فنیقی به کار برده و γαυλός سطل شیر و ظرف گِرد است. اما به احتمال \"\n                    \"بسیار هندواروپایی نیست؛ ویکی‌واژه به پیروی از بیکس آن را وامی از اکدی gullu «ظرف» و \"\n                    \"gullatu «کوزه» از راه فنیقی می‌داند. اما «galea» اصلاً به این خانواده تعلق ندارد: در \"\n                    \"یونانی کلاسیک γαλέα به معنی «کشتی بازرگانی» وجود ندارد؛ واژهٔ کشتی، γαλέα یونانیِ \"\n                    \"بیزانسی (از سدهٔ نهم میلادی در متون دریایی) است که کلاین آن را از γαλία «ماهیِ دریایی» و \"\n                    \"سرانجام از γαλέη «راسو» می‌گیرد، و اتیمانلاین یکسره می‌نویسد «خاستگاهش ناشناخته است». \"\n                    \"بنابراین نورایی دو واژهٔ بی‌ربط را تنها به گواهِ شباهت ظاهری یکی گرفته است؛ این حلقه \"\n                    \"پذیرفتنی نیست.\"),\n  \"sources\": [W + \"%CE%B3%CE%B1%CF%85%CE%BB%CF%8C%CF%82\", \"https://www.etymonline.com/word/galley\"],\n  \"ref_check\": [\n    {\"ref\": \"IEC:388\", \"status\": \"partial\",\n     \"note\": \"Mann col. 388 has 'Gk. gaūlos \\\"merchant-ship\\\"; gaulós \\\"milkpail\\\"' — supports the gaulos half of the node, but Mann does not mention galea at all.\"},\n    {\"ref\": \"AHD:539\", \"status\": \"not_checked\",\n     \"note\": \"A page of the main dictionary body of AHD New College 1975 (the galleon/galley entries), which is not on disk; Watkins's IE-roots appendix, the only AHD text available here, has no such root.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. galley (KLN_1966.txt l.15708)\", \"stance\": \"contradicts\",\n     \"note\": \"'galley, n. — ME. galei, galeie, fr. OF. galie, fr. ML. galea, fr. Byzant. Gk. γαλέα, which derives fr. Late Gk. γαλία, name of a seafish, and ult. fr. Gk. γαλέη \\\"weasel\\\".'\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Galley (SKT.txt l.7335)\", \"stance\": \"contradicts\",\n     \"note\": \"'Galley, a low built ship. (F — ?) O.F. galie; Low L. galea. Orig. unknown.'\"},\n    {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt l.35029)\", \"stance\": \"contradicts\",\n     \"note\": \"'Lat. galea (\\\"leather helmet\\\"), prob. loanword fr. Grk. γαλέη \\\"weasel, marten\\\".'\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Latin\", \"words\": \"galeota, galea\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"Classical Latin galea means 'helmet' (Buck: a loan from Greek γαλέη 'weasel', via \"\n                 \"'weasel-skin' > 'leather cap'), never 'ship'. The ship-word galea is Medieval Latin, \"\n                 \"borrowed from Byzantine Greek γαλέα in the Mediterranean naval vocabulary of the 9th-11th \"\n                 \"centuries, and galeota is its Italian/Medieval-Latin diminutive ('small galley'). Neither \"\n                 \"continues Greek γαῦλος: the vocalism (-au- vs -a-), the meaning and the chronology all \"\n                 \"diverge, and Mann, whom Nourai follows for the root, does not connect them. What the \"\n                 \"chart draws as Greek gaulos → Latin galea is a conflation of a classical Greek Semitic \"\n                 \"loan with a medieval nautical term of unknown origin.\"),\n  \"derivation_fa\": (\"galea در لاتینِ کلاسیک «کلاهخود» است — بنا بر باک، وامی از یونانی γαλέη «راسو» از راه \"\n                    \"«پوست راسو» ← «کلاهِ چرمی» — و هرگز «کشتی» نبوده است. galeaی به معنی کشتی، لاتینِ میانه \"\n                    \"است که در واژگان دریایی مدیترانه در سده‌های نهم تا یازدهم میلادی از یونانی بیزانسی γαλέα \"\n                    \"گرفته شده، و galeota مصغّرِ ایتالیایی/لاتینِ میانهٔ آن است («کشتیِ کوچک»). هیچ‌یک دنبالهٔ \"\n                    \"γαῦλος یونانی نیست: نه واکه‌ها می‌خوانند (‎-au- در برابر ‎-a-)، نه معنا و نه تاریخ؛ و مان \"\n                    \"هم که نورایی ریشه را از او گرفته این دو را به هم نمی‌پیوندد. پژوهش امروزی این حلقه را \"\n                    \"رد می‌کند.\"),\n  \"sources\": [\"https://www.etymonline.com/word/galley\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:539\", \"status\": \"not_checked\",\n     \"note\": \"Main-dictionary page of the 1975 AHD New College edition; not available on disk. No AHD IE root covers galley.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. galley, galiot, galleass\", \"stance\": \"contradicts\",\n     \"note\": \"'galiot, galliot, n., a small swift galley. — F. galiote, fr. OF. galie'; 'galleass … fr. It. galeazza, augment. of galea' — all from ML galea < Byzantine Greek, not from gaulos.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck (SYN.txt l.35029)\", \"stance\": \"contradicts\",\n     \"note\": \"Latin galea is glossed 'leather helmet' and derived from Greek γαλέη.\"},\n    {\"src\": \"IEC\", \"where\": \"Mann col. 388\", \"stance\": \"silent\",\n     \"note\": \"Mann's ĝaulos entry lists no Latin reflex at all.\"}\n  ]\n})\n\ne2[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"English\", \"words\": \"galleon, galiot, galliot, galley\",\n  \"verdict\": \"plausible\",\n  \"derivation\": (\"The English words are real and their immediate history is exactly as drawn — but from \"\n                 \"Medieval Latin galea, not from Greek gaulos. Galley is Middle English galei, galeie \"\n                 \"(13th c.), from Old French galie, from Medieval Latin galea; galiot/galliot is Old French \"\n                 \"galiote, a diminutive of galie ('a small swift galley'); galleon is 16th-century, from \"\n                 \"Spanish galeón, an augmentative of galea (Etymonline: 1520s, 'armed merchant ship'). So \"\n                 \"the node is right as a Romance-to-English chain and wrong only in its ultimate ancestor: \"\n                 \"Etymonline traces the family no further back than Late Greek galea, 'of unknown origin'.\"),\n  \"derivation_fa\": (\"واژه‌های انگلیسی واقعی‌اند و تاریخ نزدیکشان درست همان است که در نمودار آمده — اما از \"\n                    \"لاتینِ میانهٔ galea، نه از gaulosِ یونانی. galley از انگلیسی میانهٔ galei/galeie (سدهٔ \"\n                    \"سیزدهم) از فرانسهٔ کهن galie از لاتینِ میانه galea است؛ galiot/galliot همان galiote \"\n                    \"فرانسهٔ کهن، مصغّر galie؛ و galleon از سدهٔ شانزدهم از اسپانیایی galeón، صورت بزرگ‌ساز \"\n                    \"galea. پس زنجیرهٔ رومی به انگلیسی درست است و تنها نیای نهاییِ آن نادرست: اتیمانلاین این \"\n                    \"خانواده را از γαλέαِ یونانیِ متأخر فراتر نمی‌برد و می‌گوید خاستگاهش ناشناخته است. با \"\n                    \"احتیاط پذیرفتنی است.\"),\n  \"sources\": [\"https://www.etymonline.com/word/galley\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD:539\", \"status\": \"not_checked\",\n     \"note\": \"Main-dictionary page of AHD New College 1975 (galleon/galley entries), not on disk.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein s.vv. galley, galleon, galiot (KLN_1966.txt ll.15701, 15706, 15708)\", \"stance\": \"partial\",\n     \"note\": \"'galleon, n. … Sp. galeón, formed fr. ML. galea, \\\"galley\\\", with augment. suff. -on'; 'galley … fr. OF. galie, fr. ML. galea, fr. Byzant. Gk. γαλέα' — supports the English forms, contradicts the gaulos ancestry.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat s.v. Galley (SKT.txt l.7335)\", \"stance\": \"partial\",\n     \"note\": \"'O.F. galie; Low L. galea. Orig. unknown' — the English words are confirmed, the origin left open.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e2)\nPYEOF\necho ok"
}
```


### [2026-09-05T20:53:10.996Z] TOOL RESULT

```
ok
```


## [2026-09-05T20:56:39.913Z] TOOL CALL #58: Bash

```json
{
 "command": "cat >> /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build168.py <<'PYEOF'\n\n# ---------------- entry 5: Indo-European Gěi, Gě, Gî ----------------\ne5 = {\n  \"entry\": 5,\n  \"root\": \"Gěi, Gě, Gî\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *gē(i)- : *gā(i)- : *gī- 'to sing, to cry' (Pokorny 355; LIV *gʷeH-(i-), Cheung *gaH)\",\n  \"note\": (\"Root, language label, gloss and the three ablaut grades are all exactly Pokorny's. IEW 355: \"\n           \"'ge(i)- : gā(i)- : gī-, Meaning: to sing, to cry. Note: onomatopoeic word. Old Indic gāyati and \"\n           \"gāti \\\"sings\\\", gātu- and gīti- \\\"song\\\", gīta- \\\"sung\\\", gāthā \\\"song, verse\\\" = Avestan gāθā \"\n           \"\\\"song of religious content\\\"; Old Russian gaju, gajati; Lithuanian giedoti \\\"sing\\\"; Tocharian \"\n           \"A kāk …'. Watkins/AHD gives the same root (gē(i)-2, 'To sing'), and Cheung 2007 reconstructs \"\n           \"Proto-Iranian *gaH 'to sing, call' with the same PIE base. The one part of the chart that \"\n           \"modern scholarship rejects is the niyāyišn branch (nodes 4-6), which Cheung assigns to a quite \"\n           \"different root, *ǰad 'to ask, pray'.\"),\n  \"note_fa\": (\"ریشه، برچسب زبانی، معنا و هر سه پایهٔ آواگردانی (Gěi، Gě، Gî) دقیقاً همان است که پوکورنی در \"\n              \"ص۳۵۵ آورده: «ge(i)- : gā(i)- : gī- «سراییدن، بانگ زدن»، واژه‌ای آوایی (نام‌آوا). سنسکریت \"\n              \"gāyati و gāti «می‌سراید»، gātu- و gīti- «سرود»، gīta- «سروده‌شده»، gāthā «سرود» = اوستایی \"\n              \"gāθā؛ روسی کهن gajati؛ لیتوانیایی giedoti «سراییدن»…». واتکینز در پیوستِ ریشه‌های \"\n              \"هندواروپاییِ AHD نیز همین ریشه را با همین معنا آورده و چونگ (۲۰۰۷) ریشهٔ ایرانی آغازین *gaH \"\n              \"«سراییدن، خواندن» را از همین پایه بازسازی کرده است. تنها بخشی از نمودار که پژوهش امروزی رد \"\n              \"می‌کند شاخهٔ «نیایش» (گره‌های ۴ تا ۶) است که چونگ آن را به ریشهٔ دیگری، *ǰad «خواستن، دعا \"\n              \"کردن»، بازمی‌گرداند. جز آن، ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%DA%AF%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:355\", \"status\": \"supports\",\n     \"note\": (\"Pokorny IEW p.355 (POK_full.txt ll.31718-31749): 'Root / lemma: ge(i)- : gā(i)- : gī-, \"\n              \"Meaning: to sing, to cry. Note: onomatopoeic word. Old Indic gāyati and gāti \\\"sings\\\" … \"\n              \"gāthā \\\"song, verse\\\" = Avestan gāθā \\\"song of religious content\\\" … References: WP. I 526 f. \"\n              \"… Page(s): 355.' Nourai's three headwords are Pokorny's three ablaut grades.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins, AHD IE Roots (AHD_watkins1985.txt l.485)\", \"stance\": \"supports\",\n     \"note\": \"'gē(i)-2. To sing. Contracted from *geəi-. Zero-grade form *gī- (< *giə-) in Sanskrit gītā, song: BHAGAVAD-GITA. [Pok. gē(i)- 355.]'\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 526 f. (cited by Pokorny)\", \"stance\": \"supports\",\n     \"note\": \"Pokorny's own reference line for the lemma is 'WP. I 526 f.', i.e. Walde-Pokorny carries the same root; the volume itself is not among the scans on disk (only Bd. III, the index).\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung, Etym. Dict. of the Iranian Verb, s.v. *gaH (CHEUNG.txt ll.7089-7112)\", \"stance\": \"supports\",\n     \"note\": \"'*gaH \\\"to sing, call\\\" … YAv. gāθa- \\\"song, gatha\\\"; Khotanese gaha- \\\"verse\\\"; Sanskrit gā \\\"to sing\\\" (RV+) … PIE *gʷeH-(i-) \\\"to sing\\\" > LIV: 183 | Pok.: 355.'\"}\n  ],\n  \"nodes\": []\n}\n\ne5[\"nodes\"].append({\n  \"id\": 1, \"lang\": \"Avestan\", \"words\": \"gâ 1; gâtâ\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Avestan has both the verb and the noun. The root gā(y)- 'to sing' shows in compounds such \"\n                 \"as pairi.gā.vacah- 'who sings the words around' (Y 57.20), barəzi.gāθra- 'singing high' \"\n                 \"(Yt 10.89) and the abstract gāθra- n. 'Singen, Gesang' (Bartholomae col. 1035, 'zum ai. V. \"\n                 \"gāyati'). gāθā- f. is the corresponding *-tā- action noun, PIE *gʷeH-tH-eh₂- > PII \"\n                 \"*gaHtʰā-, and is Bartholomae's 'Lied, und zwar religiösen Inhalts', the technical term for \"\n                 \"the five hymn-collections of Zarathushtra preserved in Yasna 28-34, 43-51, 53 — the \"\n                 \"Gathas. Sanskrit gāthā- 'song, verse' is its exact cognate, which is why Pokorny prints \"\n                 \"the equation 'ai. gāthā = Avestan gāθā'. Nourai's node is correct in form, language and \"\n                 \"meaning.\"),\n  \"derivation_fa\": (\"اوستایی هم فعل را دارد و هم اسم را. ستاک gā(y)- «سراییدن» در ترکیب‌هایی چون \"\n                    \"pairi.gā.vacah- «آن‌که واژه‌ها را گرداگرد می‌سراید» (یسنه ۵۷٫۲۰) و barəzi.gāθra- «بلندسرا» \"\n                    \"(یشت ۱۰٫۸۹) و اسم مصدر gāθra- «سرودن، سرود» (بارتولومه، ستون ۱۰۳۵: «به فعل سنسکریت \"\n                    \"gāyati») دیده می‌شود. gāθā- اسمِ ساخته‌شده با پسوند *-tā- است: هندواروپایی *gʷeH-tH-eh₂- ← \"\n                    \"هندوایرانی *gaHtʰā-؛ بارتولومه آن را «سرود، آن هم با محتوای دینی» تعریف می‌کند، یعنی \"\n                    \"نام فنیِ پنج دستهٔ سرودهای زردشت در یسنه‌های ۲۸–۳۴، ۴۳–۵۱ و ۵۳. سنسکریت gāthā- هم‌ریشهٔ \"\n                    \"دقیق آن است و پوکورنی همین برابری را آورده است. ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%DA%AF%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:355\", \"status\": \"supports\",\n     \"note\": \"IEW 355 prints the equation 'gāthā \\\"song, verse\\\" = Avestan gāθā \\\"song of religious content\\\"' in the material of the lemma gē(i)-.\"},\n    {\"ref\": \"KLN:169\", \"status\": \"supports\",\n     \"note\": (\"Klein p.169 s.v. Bhagavad-Gita (KLN_1966.txt l.4885): '… gī-tā, \\\"song\\\", prop. fem. pp. of \"\n              \"gāyate, \\\"sings, calls\\\", from the I.-E. imitative base *gā-, *gī-, whence also Avestic gāθa, \"\n              \"Pers. gāh, \\\"song\\\", Lith. giedoti …' — Klein's line contains both the Avestan and the \"\n              \"Persian words of Nourai's next node.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW cols. 1035-1036 (BRT.txt ll.10318, 10337)\", \"stance\": \"supports\",\n     \"note\": \"'j. gāθā- f. \\\"Lied\\\" und zwar religiösen Inhalts; 1) insbes. von den fünf Hymnen … die in Y. 28—34, 43—51, 53 erhalten sind'; and 'j. gāθra- n. \\\"Singen, Gesang\\\" … Zum ai. V. gāyati.'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *gaH\", \"stance\": \"supports\",\n     \"note\": \"Lists YAv. pairi.gā.vacah-, barəzi.gāθra-, fragāθra-, gāθa- 'song, gatha' under Proto-Iranian *gaH 'to sing, call'.\"}\n  ]\n})\n\ne5[\"nodes\"].append({\n  \"id\": 2, \"lang\": \"Persian\", \"words\": \"gât «گات ( گاتها )»; gâh 1 «گاه۱ ( سه گاه ، چهارگاه )»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Both Persian words continue Avestan gāθā through Middle Persian. Avestan gāθā- gave MP \"\n                 \"gāh 'Gatha; hymn, song' (written gʾs); in New Persian this yields, on one hand, the \"\n                 \"learned Zoroastrian term گات gāt / plural گاتها gāthā (a form kept close to the Avestan \"\n                 \"with -t, used by Parsi and modern Iranian Zoroastrian writers for the Gathas), and on the \"\n                 \"other hand the inherited گاه gāh 'melody, tune', which survives above all as the second \"\n                 \"element of the names of the dastgāhs: سه‌گاه, چهارگاه. Wiktionary's Etymology 2 for گاه is \"\n                 \"precisely this: 'Inherited from Middle Persian gāh \\\"Gatha; hymn, song\\\", from Avestan \"\n                 \"gāθā \\\"Gatha; song\\\", from PII *gaHtʰás, from PIE *g(ʷ)eH-tHó-s, from *g(ʷ)eH- \\\"to sing, \"\n                 \"cry\\\"'. It is a genuine homonym of the other گاه ('place, time, throne', from Old Persian \"\n                 \"gāθu-, Horn no. 889), and Mo'in keeps them apart as separate lemmas, which is why Nourai \"\n                 \"writes 'gâh 1'.\"),\n  \"derivation_fa\": (\"هر دو واژهٔ فارسی از راه فارسی میانه به gāθāی اوستایی می‌رسند. gāθā- اوستایی در فارسی \"\n                    \"میانه gāh «گاه، سرود، گات» شده است؛ در فارسی نو از یک سو اصطلاح دینیِ «گات» و جمعِ آن \"\n                    \"«گاتها» را داریم (صورتی نزدیک به اوستایی با ت پایانی که پارسیان و زردشتیان ایرانی برای \"\n                    \"سرودهای زردشت به کار می‌برند) و از سوی دیگر «گاه» میراثی به معنی «آهنگ، نغمه» که بیش از \"\n                    \"همه در نام دستگاه‌ها بازمانده است: سه‌گاه، چهارگاه. ویکی‌واژه در ریشه‌شناسی دومِ «گاه» \"\n                    \"دقیقاً همین را می‌گوید. این «گاه» با «گاهِ» دیگر (جای، زمان، تخت — از پارسی باستان \"\n                    \"gāθu-، هرن شمارهٔ ۸۸۹) هم‌آواست نه هم‌ریشه، و معین نیز آن دو را مدخل‌های جداگانه آورده \"\n                    \"است؛ از همین روست که نورایی «گاه۱» نوشته. ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%DA%AF%D8%A7%D9%87\", \"https://abadis.ir/fatofa/%DA%AF%D8%A7%D9%87/\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:3190\", \"status\": \"supports\",\n     \"note\": (\"Mo'in's lexicon, via abadis.ir/fatofa/گاه (فرهنگ معین section): the first گاه lemma reads \"\n              \"'[ په . ] (اِ. ) ۱ - آهنگ ، آواز. ۲ - (پس . ) به صورت پسوند در نام های آهنگ های موسیقی به کار \"\n              \"رود: سه گاه ، چهارگاه .' — 'melody, voice', used as a suffix in the names of musical modes, \"\n              \"tagged Pahlavi. That is Nourai's gâh 1 with his very examples; the 'place/throne' گاه is a \"\n              \"separate lemma further down.\")},\n    {\"ref\": \"KLN:169\", \"status\": \"supports\",\n     \"note\": \"Klein p.169 s.v. Bhagavad-Gita: '… whence also Avestic gāθa, Pers. gāh, \\\"song\\\"' — Klein explicitly puts Persian gāh 'song' under this root.\"},\n    {\"ref\": \"MON6:1648\", \"status\": \"not_checked\",\n     \"note\": \"Mo'in vol. 6 is the a'lam (proper-name) volume, where گاتها is treated as the title of the Zoroastrian hymns; vols 5-6 are not on vajehyab/abadis and no scan is in the local library, so this page could not be opened.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. گاه (abadis mirror)\", \"stance\": \"supports\",\n     \"note\": \"Three separate گاه lemmas: [په.] 'آهنگ، آواز' + musical-mode suffix; the temporal/local suffix; and [په.] 'تخت شاهی، سریر؛ مسند؛ جا، مکان'. Nourai's gâh 1 matches the first exactly.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn no. 889, p.199\", \"stance\": \"partial\",\n     \"note\": \"'gāh \\\"Ort (in Comp.); Thron\\\". ap. gāθu- \\\"Ort; Thron\\\" … aw. gātu- \\\"Ort; Thron\\\"; phlv. gās; ai. gātu-' — Horn treats only the homonym 'place/throne', i.e. he does not contradict gāh 'tune' but shows why the two must be kept apart.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *gaH\", \"stance\": \"supports\",\n     \"note\": \"Khotanese gaha- 'verse' beside YAv. gāθa- shows the *gāθa- > *gāh development within Iranian that the Persian word presupposes.\"}\n  ]\n})\n\ne5[\"nodes\"].append({\n  \"id\": 3, \"lang\": \"Sanskrit\", \"words\": \"gâ; gâyatî; bhagavant-gita\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"Sanskrit gā- (root gai) 'to sing', 3sg. present gāyati 'he sings' (Rigveda onwards), past \"\n                 \"participle gīta- 'sung' > gītā f. 'song', with gāthā- 'song, verse'. Pokorny's material \"\n                 \"for the lemma is precisely 'Old Indic gāyati and gāti \\\"sings\\\", gātu- and gīti- \\\"song\\\", \"\n                 \"gīta- \\\"sung\\\", gāthā \\\"song, verse\\\"'. Bhagavad-gītā is the tatpuruṣa compound \"\n                 \"bhagavat- 'the Blessed/Sublime One' (from bhaga- 'apportioner, lord', PIE *bʰag-) + gītā \"\n                 \"'song', i.e. 'the Song of the Sublime One' — Klein's own wording. Nourai's spelling \"\n                 \"'bhagavant-gita' uses the strong stem bhagavant- and his gloss 'sound of sublime' is a \"\n                 \"loose rendering of that, but the analysis is right; the cross-reference ☞Bhag points at \"\n                 \"the correct second root.\"),\n  \"derivation_fa\": (\"سنسکریت gā- (ستاک gai) «سراییدن»، سوم‌شخص مفرد حال gāyati «می‌سراید» (از ریگ‌ودا به بعد)، \"\n                    \"اسم مفعول gīta- «سروده» و از آن gītā «سرود»، و نیز gāthā- «سرود، بند». مادهٔ پوکورنی برای \"\n                    \"این ریشه دقیقاً همین‌هاست. «بهگودگیتا» ترکیبی است از bhagavat- «خداوندگار، آن بزرگوار» \"\n                    \"(از bhaga- «بخش‌کننده، سرور»، هندواروپایی *bʰag-) و gītā «سرود»، یعنی «سرودِ آن بزرگوار» \"\n                    \"— همان تعبیری که کلاین آورده است. نگارش «bhagavant-gita» در کتاب ستاک قویِ bhagavant- را \"\n                    \"به کار برده و معنی «آوای شکوهمند» ترجمه‌ای آزاد است، اما تحلیل درست است و ارجاع «☞Bhag» \"\n                    \"نیز به ریشهٔ درست اشاره می‌کند. ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%DA%AF%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:355\", \"status\": \"supports\",\n     \"note\": \"IEW 355: 'Old Indic gayati and gati \\\"sings\\\", gatu- and gīti- \\\"song\\\", gīta- \\\"sung, chanted\\\", gatha \\\"song, verse\\\"' — all three of Nourai's Sanskrit items.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins (AHD_watkins1985.txt l.485)\", \"stance\": \"supports\",\n     \"note\": \"'gē(i)-2. To sing … Zero-grade form *gī- (< *giə-) in Sanskrit gītā, song: BHAGAVAD-GITA.'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein p.169 s.v. Bhagavad-Gita\", \"stance\": \"supports\",\n     \"note\": \"'OI. Bhāgavadgītā, \\\"the song of the Sublime One\\\", compounded of Bhaga, suff. -vant … and gī-tā, \\\"song\\\", prop. fem. pp. of gāyate, \\\"sings, calls\\\".'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *gaH\", \"stance\": \"supports\",\n     \"note\": \"'SANSKRIT: gā \\\"to sing\\\" (RV+) — EWAia I: 482.'\"}\n  ]\n})\n\ne5[\"nodes\"].append({\n  \"id\": 4, \"lang\": \"Old Persian\", \"words\": \"niğây\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"No such Old Persian word is attested. Kent's Old Persian lexicon has jad- 'to pray, ask' \"\n                 \"(1sg. jadiyāmiy, DPd 21, XPh 59), not *ni-gāy-. Nourai's form is a back-projection of the \"\n                 \"Middle Persian stem. The substance of the claim — that niyāyišn belongs to the root gā- \"\n                 \"'to sing' — was Nyberg's: 'niyāyišn … < *nigāyišn from gāy-, Skr gāyati \\\"to sing\\\"; MPrth \"\n                 \"ng'y- pres. \\\"to sing\\\", ng'd \\\"song\\\" (Ghilain 86)', and Mo'in adopted it from Nyberg in \"\n                 \"the Borhan footnote Nourai cites. But Cheung 2007 rejects it twice over: under *gaH he \"\n                 \"notes 'The MIr. (verbal) forms, Pth. ng'y-, etc. are rather from *ǰad', and under *ǰad 'to \"\n                 \"ask, pray' (Av. jaiδiia-, OP jad-) he files 'BMP nyd'dsn /niyāyišn/ \\\"prayer, praise, \"\n                 \"worship\\\"', explaining the apparently irregular loss of *-g- by the following front \"\n                 \"vowel/glide (cf. MMP nyws- / NP niyōš- 'to listen' < *ni-gauš-, NP payām < *pati-gam-). So \"\n                 \"the older etymology Nourai reproduces is now the minority view, and the node's language \"\n                 \"label is wrong as well.\"),\n  \"derivation_fa\": (\"چنین واژه‌ای در پارسی باستان گواهی نشده است. در واژه‌نامهٔ کنت تنها jad- «دعا کردن، \"\n                    \"خواستن» آمده (اول‌شخص jadiyāmiy در DPd ۲۱ و XPh ۵۹)، نه *ni-gāy-. صورتی که نورایی آورده \"\n                    \"بازسازیِ واپس‌نگرِ ستاک فارسی میانه است. اصلِ ادعا — که «نیایش» به ریشهٔ gā- «سراییدن» \"\n                    \"بازمی‌گردد — از آنِ نیبرگ است: «niyāyišn … از *nigāyišn، از gāy-، سنسکریت gāyati \"\n                    \"«سراییدن»؛ پارتی ng'y- «سراییدن»، ng'd «سرود»»، و معین همین را از نیبرگ در حاشیهٔ برهان \"\n                    \"قاطع (همان مأخذی که نورایی می‌آورد) گرفته است. اما چونگ (۲۰۰۷) دو بار آن را رد می‌کند: \"\n                    \"ذیل *gaH می‌نویسد «صورت‌های ایرانی میانه، از جمله پارتی ng'y-، بهتر است از *ǰad گرفته \"\n                    \"شوند»، و ذیل *ǰad «خواستن، دعا کردن» (اوستایی jaiδiia-، پارسی باستان jad-) خودِ \"\n                    \"niyāyišn را جای می‌دهد و افتادنِ ظاهراً بی‌قاعدهٔ *-g- را با واکه/غلتِ پیشینِ پس از آن \"\n                    \"توضیح می‌دهد (قس نیوش < *ni-gauš-، پیام < *pati-gam-). پس ریشه‌شناسی کهنی که نورایی \"\n                    \"بازگفته امروز دیدگاه اقلیت است و برچسب «پارسی باستان» نیز نادرست است.\"),\n  \"sources\": [W + \"%DA%AF%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:4878\", \"status\": \"partial\",\n     \"note\": (\"Mo'in's lexicon entry نیایش (abadis mirror) reads only '(یِ ) [ په . ] (اِمص . ) دعا، ستایش' — \"\n              \"it tags the word Pahlavi and gives no Old Persian form. The Latin-script etymological \"\n              \"material of the print edition, which is what Nourai is citing, corresponds to the fuller \"\n              \"footnote in Borhan (see node #6): 'پهلوی niyāyišn (پرستیدن) … ایرانی باستان … سانسکریت gā \"\n              \"(آواز خواندن) … نیبرگ ص۱۵۸'. So Mo'in supports the gā- etymology and an 'Old Iranian' \"\n              \"(ایرانی باستان) stage, but not an Old Persian word niğāy.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.184b\", \"stance\": \"contradicts\",\n     \"note\": \"Cheung quotes it: 'OLD PERSIAN: jad- \\\"to pray, ask\\\" — Kent: 184b. Pres. ja-: IND. 1sg. jadiyamiy <j-di-i-y-a-mi-i-y> (DPd 21, PMa 54)'. There is no Old Persian *nigāy- in the corpus.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *gaH and s.v. *ǰad (CHEUNG.txt ll.7110, 14863)\", \"stance\": \"contradicts\",\n     \"note\": \"'The MIr. (verbal) forms, Pth. ng'y-, etc. are rather from *ǰad'; and under *ǰad: 'BMP nyd'dsn /niyāyišn/ \\\"prayer, praise, worship\\\". The loss of the velar *-g- … is due to the presence of the front vowel / glide -iy-.'\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary p.158 s.v. niyāyišn\", \"stance\": \"supports\",\n     \"note\": \"'niyāyišn [nyd'dšn'] worship, adoration … < *nigāyišn from gāy-, Skr gāyati \\\"to sing\\\"; MPrth ng'y- pres. \\\"to sing\\\", ng'd \\\"song\\\" (Ghilain 86).' This is the source of Nourai's (and Mo'in's) derivation.\"}\n  ]\n})\n\ne5[\"nodes\"].append({\n  \"id\": 5, \"lang\": \"Pahlavi\", \"words\": \"niğâyišn\",\n  \"verdict\": \"disputed\",\n  \"derivation\": (\"The Middle Persian word is real and well attested: Book Pahlavi nyʾdšn' /niyāyišn/ \"\n                 \"'prayer, praise, worship' (MacKenzie: 'niyāyišn [nyd'dšn' | N ~iš] prayer, praise'; \"\n                 \"Nyberg: 'worship, adoration, of the Fire … Renders Av. nəmah-'), the name of the five \"\n                 \"Nyāyišn prayers of the Khordeh Avesta. It is a regular -išn abstract from the present \"\n                 \"stem niyāy-. What is disputed is precisely what Nourai's arrow asserts, namely that this \"\n                 \"stem is *ni-gāy- from gā- 'to sing': Nyberg (whom Mo'in follows) reconstructs *nigāyišn \"\n                 \"and points to Parthian ng'y- 'to sing', but Cheung 2007 assigns Parthian ng'y- 'to pray, \"\n                 \"supplicate' and MP niyāyišn to the root *ǰad 'to ask, pray' (Av. jaiδiia-, OP jad-, MP \"\n                 \"zay-), with MMP nyzʾy- 'to entreat; honour' as the same formation, and explains the loss \"\n                 \"of the velar by the following -iy- (as in niyōš- 'to listen' < *ni-gauš-). The written \"\n                 \"form Nourai gives, niğāyišn with ğ, is itself an attempt to show that lost velar.\"),\n  \"derivation_fa\": (\"واژهٔ فارسی میانه راست و پرگواه است: پهلویِ کتابی nyʾdšn' /niyāyišn/ «دعا، ستایش، پرستش» \"\n                    \"— مکنزی: «niyāyišn، دعا، ستایش»؛ نیبرگ: «پرستش و نیایش، از جمله نیایشِ آتش… برگردانِ \"\n                    \"اوستایی nəmah-». همین است نام پنج «نیایش» خردهٔ اوستا (خورشید نیایش، مهر نیایش، ماه \"\n                    \"نیایش، آبان نیایش، آتش نیایش). ساختِ آن قاعده‌مند است: اسم مصدر با پسوند ‎-išn از ستاک \"\n                    \"حالِ niyāy-. آنچه مورد اختلاف است همان چیزی است که پیکان نورایی ادعا می‌کند، یعنی اینکه \"\n                    \"این ستاک *ni-gāy- از gā- «سراییدن» باشد: نیبرگ (و به پیروی او معین) *nigāyišn را \"\n                    \"بازسازی می‌کند و به پارتی ng'y- «سراییدن» استناد می‌کند، اما چونگ همان ng'y- را «دعا \"\n                    \"کردن، لابه کردن» می‌خواند و آن را با niyāyišn به ریشهٔ *ǰad «خواستن، دعا کردن» \"\n                    \"بازمی‌گرداند و افتادنِ «گ» را با ‎-iy-ِ پس از آن توضیح می‌دهد (مانند «نیوش» از \"\n                    \"*ni-gauš-). نگارشِ niğāyišn با «ğ» در کتاب نیز کوششی است برای نشان دادنِ همان «گ» \"\n                    \"افتاده.\"),\n  \"sources\": [W + \"%DA%AF%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"MON:4878\", \"status\": \"partial\",\n     \"note\": \"Mo'in tags نیایش '[په.]' (Pahlavi) and, in the parallel Borhan footnote, gives 'پهلوی niyāyišn (پرستیدن)' with Sanskrit gā 'to sing' and a reference to Nyberg p.158 — so he supports the Pahlavi form and the gā- etymology, but he offers no Old Persian antecedent for it.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. niyāyišn (PHD.txt l.514)\", \"stance\": \"supports\",\n     \"note\": \"'niyāyišn [nyd'dšn' | N ~iš] prayer, praise.' — the form and meaning, without an etymology.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II, glossary (NYB_vol2_glossary.txt l.2775)\", \"stance\": \"supports\",\n     \"note\": \"'niyāyišn [nyd'dšn'] worship, adoration, of the Fire 6621-22 … Renders Av. nəmah- … < *nigāyišn from gāy-, Skr gāyati \\\"to sing\\\"; MPrth ng'y- pres. \\\"to sing\\\", ng'd \\\"song\\\" (Ghilain 86).'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung s.v. *ǰad (CHEUNG.txt l.14863)\", \"stance\": \"contradicts\",\n     \"note\": \"'MIDDLE PERSIAN: BMP zd- /zay-/ \\\"to ask, demand, implore\\\" || (+ *ni-) MMP nyzʾy- \\\"to entreat; honour\\\", BMP nydʾdsn /niyāyišn/ \\\"prayer, praise, worship\\\". The loss of the velar *-g- … is due to the presence of the front vowel / glide -iy-.'\"}\n  ]\n})\n\ne5[\"nodes\"].append({\n  \"id\": 6, \"lang\": \"Persian\", \"words\": \"nîyâyeš «نیایش»\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"The edge drawn here — Pahlavi niyāyišn → New Persian نیایش niyāyeš 'praise, prayer' — is \"\n                 \"beyond dispute: the Middle Persian -išn abstract passes into New Persian as -eš with the \"\n                 \"regular raising/shortening of the Sasanian -išn, exactly as ستایش, دانش, کوشش. It is old \"\n                 \"in New Persian; the Borhan footnote quotes Ferdowsi, 'همیدون بزاری نیایش گرفت / جهان \"\n                 \"آفرین را ستایش گرفت', and glosses the headword 'بمعنی آفرین و تحسین - و دعائی باشد که از \"\n                 \"روی تضرع و زاری کنند'. Mo'in tags it '[په.]', Pahlavi. Only the ultimate root behind the \"\n                 \"word is contested (see nodes #4-5): Nyberg and Mo'in put it under gā- 'to sing', Cheung \"\n                 \"2007 under *ǰad 'to ask, pray'.\"),\n  \"derivation_fa\": (\"این حلقه — از niyāyišnِ پهلوی به «نیایش» فارسی — بی‌چون‌وچرا درست است: اسم مصدرِ ‎-išnِ \"\n                    \"فارسی میانه در فارسی نو به ‎-ش بدل می‌شود، درست مانند «ستایش»، «دانش» و «کوشش». این واژه \"\n                    \"در فارسی دری کهن است؛ حاشیهٔ برهان قاطع (ص۲۲۲۴) بیتِ فردوسی را گواه می‌آورد: «همیدون \"\n                    \"بزاری نیایش گرفت / جهان‌آفرین را ستایش گرفت» و خودِ مدخل را چنین معنی می‌کند: «بمعنی \"\n                    \"آفرین و تحسین، و دعائی باشد که از روی تضرع و زاری کنند». معین نیز آن را «[په.]» \"\n                    \"برچسب زده است. تنها ریشهٔ نهاییِ واژه مورد اختلاف است (نگاه کنید به گره‌های ۴ و ۵): \"\n                    \"نیبرگ و معین آن را از gā- «سراییدن» می‌گیرند و چونگ از *ǰad «خواستن، دعا کردن».\"),\n  \"sources\": [\"https://abadis.ir/fatofa/%D9%86%DB%8C%D8%A7%DB%8C%D8%B4/\"],\n  \"ref_check\": [\n    {\"ref\": \"BQT:2224\", \"status\": \"supports\",\n     \"note\": (\"ref_page.py BQT:2224 (Borhan vol. 4 pdf p.307) is exactly the نیایش page: 'نیایش ۱ - بر وزن \"\n              \"ستایش، بمعنی آفرین و تحسین - و دعائی باشد که از روی تضرع و زاری کنند. ۲ - وبمعنی مهربانی هم \"\n              \"آمده است.' Mo'in's footnote 1 gives 'پهلوی [niyāyišn] (پرستیدن) … ایرانی باستان … سانسکریت \"\n              \"gā (آواز خواندن) … نیبرگ ص۱۵۸', and footnote 4 lists the five Nyāyišn prayers of the Khordeh \"\n              \"Avesta with Ferdowsi's line. Precisely Nourai's claim, sourced to Nyberg.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"BQT\", \"where\": \"Borhan-e Qate' p.2224 with Mo'in's footnotes\", \"stance\": \"supports\",\n     \"note\": \"Headword, glosses, the Ferdowsi shāhed and the Pahlavi/Sanskrit etymological footnote citing Nyberg p.158.\"},\n    {\"src\": \"MON\", \"where\": \"Farhang-e Mo'in s.v. نیایش (abadis mirror)\", \"stance\": \"supports\",\n     \"note\": \"'(یِ ) [ په . ] (اِمص . ) دعا، ستایش .' — an -eš abstract of Pahlavi origin.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie s.v. niyāyišn\", \"stance\": \"supports\",\n     \"note\": \"'niyāyišn [nyd'dšn' | N ~iš] prayer, praise' — MacKenzie himself notes the New Persian continuation ('N ~iš').\"}\n  ]\n})\n\ne5[\"nodes\"].append({\n  \"id\": 7, \"lang\": \"English\", \"words\": \"Bhagavad-Gita\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": (\"English Bhagavad-Gita is a direct 18th-century borrowing of the Sanskrit title, current in \"\n                 \"English from Charles Wilkins's translation of 1785 ('The Bhagvat-Geeta, or Dialogues of \"\n                 \"Kreeshna and Arjoon'). The second element is gītā 'song', the feminine past participle of \"\n                 \"gāyate 'sings', i.e. the *gī- zero grade of the root of this chart — which is why Watkins \"\n                 \"cites BHAGAVAD-GITA as the sole English derivative of gē(i)-2. The chart's long arrow \"\n                 \"straight from the Sanskrit box to English is therefore correct: there is no intermediate \"\n                 \"language, the word entered English from Sanskrit through the Calcutta orientalists.\"),\n  \"derivation_fa\": (\"«Bhagavad-Gita» در انگلیسی وامی مستقیم از عنوان سنسکریت است و از ترجمهٔ چارلز ویلکینز در \"\n                    \"۱۷۸۵ («گفت‌وگوهای کریشنا و ارجونا») در این زبان رواج یافته است. جزء دوم آن gītā «سرود» \"\n                    \"است، اسم مفعول مؤنثِ gāyate «می‌سراید»، یعنی همان پایهٔ صفرِ *gī- از ریشهٔ همین نمودار؛ از \"\n                    \"همین رو واتکینز تنها بازماندهٔ انگلیسیِ ریشهٔ gē(i)- را همین واژه می‌داند. پس پیکان بلندِ \"\n                    \"نمودار از جعبهٔ سنسکریت یکراست به انگلیسی درست است: زبان واسطی در میان نیست و واژه از \"\n                    \"راه شرق‌شناسان کلکته به انگلیسی رسیده است. ادعای نورایی درست است.\"),\n  \"sources\": [W + \"%DA%AF%D8%A7%D9%87\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:169\", \"status\": \"supports\",\n     \"note\": (\"Klein p.169 (KLN_1966.txt l.4885): 'Bhagavad-Gita, the celebrated dialogue between Krishna \"\n              \"and Arjuna inserted in the Mahabharata. — OI. Bhāgavadgītā, \\\"the song of the Sublime One\\\", \"\n              \"compounded of Bhaga, suff. -vant … and gī-tā, \\\"song\\\", prop. fem. pp. of gāyate, \\\"sings, \"\n              \"calls\\\", from the I.-E. imitative base *gā-, *gī-, whence also Avestic gāθa, Pers. gāh, \"\n              \"\\\"song\\\" …' — the page number is right and the entry supports the whole node.\")}\n  ],\n  \"consulted\": [\n    {\"src\": \"AHD\", \"where\": \"Watkins (AHD_watkins1985.txt l.485)\", \"stance\": \"supports\",\n     \"note\": \"'gē(i)-2. To sing … Zero-grade form *gī- (< *giə-) in Sanskrit gītā, song: BHAGAVAD-GITA. [Pok. gē(i)- 355.]'\"},\n    {\"src\": \"KLN\", \"where\": \"Klein s.v. baksheesh / -phagous (KLN_1966.txt ll.4302, 28431)\", \"stance\": \"supports\",\n     \"note\": \"Klein cross-refers Bhagavad-Gita to the base *bhag- 'to distribute, share out' for the first element, matching Nourai's ☞Bhag.\"}\n  ]\n})\n\ndoc[\"entries\"].append(e5)\n\nimport io\nwith io.open(\"/home/sfmqrb/git/rishe/data/verification/page-168.json\", \"w\", encoding=\"utf-8\") as f:\n    json.dump(doc, f, ensure_ascii=False, indent=2)\n    f.write(\"\\n\")\nprint(\"written\")\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/build168.py && python3 -m json.tool data/verification/page-168.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 168"
}
```


### [2026-09-05T20:56:44.529Z] TOOL RESULT

```
written
JSON OK
nodes verified: 19/19
node verdicts: {'disputed': 6, 'confirmed': 10, 'plausible': 3}
root verdicts: {'confirmed': 2, 'disputed': 1}
ref checks: {'partial': 6, 'supports': 13, 'not_checked': 7}
books consulted: {'contradicts': 11, 'partial': 8, 'supports': 30, 'silent': 4} | by book: {'KLN': 9, 'CHEUNG': 5, 'HUB': 4, 'PHD': 4, 'BQT': 4, 'SKT': 3, 'BRT': 2, 'HRN': 2, 'AKD': 2, 'IEC': 2, 'SYN': 2, 'MON': 2, 'AHD': 2, 'NYB': 2, 'SNS': 1, 'POK': 1, 'TAD': 1, 'LKT': 1, 'FSD': 1, 'PLA': 1, 'AFM': 1, 'KNT': 1}
```


## [2026-09-05T20:57:02.652Z] AGENT

Done — `/home/sfmqrb/git/rishe/data/verification/page-168.json` written; `verify_check.py 168` reports 19/19 nodes, 0 PROBLEM lines.

**Page 168 (book p. 138) — 3 real entries, 19 nodes**
- Node verdicts: 10 confirmed, 3 plausible, 6 disputed. Root verdicts: 2 confirmed (Gassu, Gěi), 1 disputed (Ğaulos).
- Ref checks: 13 supports, 6 partial, 7 not_checked. 22 books consulted (30 supports / 11 contradicts / 8 partial / 4 silent).

**Disputed items**
- *Gassu* #1 Avestan **vîčiča** — Bartholomae (AiW 1437) reads vīčiδa- and marks it "Et.?"; Horn himself calls the link to gač "unsicher"; no source derives it from Akkadian.
- *Gassu* #2 "Old Persian" **gač** — gač is Middle Persian/Pazand (MacKenzie, Hübschmann), not Old Persian, and comes straight from the Akkadian/Aramaic word, not via Avestan. Nourai's own NOTE is closer to the truth than his arrow.
- *Ğaulos* ROOT — Wiktionary/Beekes make Gk. γαῦλος an Akkadian (gullu/gullatu) loan via Phoenician; Pokorny and Walde-Pokorny have no such root. (Mann IEC:388 does print "ĝaulos (?) vessel, boat" verbatim, question mark included.)
- *Ğaulos* #2 Greek **galea** and #3 Latin **galeota, galea** — the galley word is Byzantine Gk. γαλέα of unknown origin (Etymonline, Skeat); classical Lat. galea = "helmet" < Gk. γαλέη "weasel" (Buck). Unrelated to gaulos.
- *Gěi* #4 Old Persian **niğây** and #5 Pahlavi **niğâyišn** — Cheung 2007 assigns MP niyāyišn and Pth. ng'y- to the root *ǰad "to ask, pray" (Av. jaiδiia-, OP jad-), explicitly rejecting the *ni-gāy- analysis that Nyberg p.158 → Mo'in → Nourai use. No OP *niğāy is attested (Kent has only jad-).

**Book misprint (extraction faithful, no data fix needed)**
- Entry *Ğaulos*, Persian node prints **AEC:388**; AEC is not a bibliography key — it is Nourai's misprint for IEC:388 (Mann), the same page as the root box, which does read "Per. cf. zauraq".

No extraction errors found: the JSON matches the printed page (pdf 168) in every node, word, script and reference.
