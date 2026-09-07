# Verification process log — verify-page-336


## [2026-09-07T16:16:56.322Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 336 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-336.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-336.json. Write /home/sfmqrb/git/rishe/data/verification/page-336.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 336` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-07T16:17:00.097Z] AGENT

I'll start by reading the instructions.


## [2026-09-07T16:17:00.916Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-07T16:17:00.936Z] TOOL RESULT

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


## [2026-09-07T16:17:01.462Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-336.txt"
}
```


### [2026-09-07T16:17:01.485Z] TOOL RESULT

```
1	=== PDF page 336 (book page 306) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Mer 2
4	Mer-d, Mer-k
5	Mor-to
6	Smerd : to rub away, harm, die
7	destroy
8	mortal man
9	painful  (refs POK:735,970; AHD:1529)  PART 2
10	#1 (parent #0) [Latin] refs=AHD | mors : death ; môr-târium : ground down, mortar ; mordĕre : to bite ; morbus : disease
11	  #2 (parent #1) [English] refs=AHD | mortal, mortuary, mortgage ; mortar ; remorse ; morbid
12	#3 (parent #0) [Old High German] refs=AHD; KLN:1461 | smerzan : painful
13	  #4 (parent #3) [English] refs=KLN:1461 | smart
14	--- entry 1 ---
15	ROOT [Indo-European] Mer 3 : to disturb  (refs POK:737)
16	#1 (parent #0) [Sanskrit] refs=HRN:101,181 | â-marš : to tolerate, be quiet ; pra-marš : to forget
17	  #2 (parent #1) [Persian] refs=BQT:706,1448 | xâmŭš «خاموش» : quiet, turned off
18	#3 (parent #0) [Avestan / Old Persian] refs=FFD:65 | muš, fra-â-muš : to forget
19	  #4 (parent #3) [Pahlavi] refs=FFD:65 | frâmŭštan : to forget
20	    #5 (parent #4) [Persian] refs=FFD:65; MON:2506 | faramŭšîdan «فراموشیدن» : to forget | extra: فراموشانیدن ، فرموشیدن
21	فراموش ، فرامش، فرامشت ، فرامِشی
22	#6 (parent #0) [Germanic] refs=AHD | 
23	  #7 (parent #6) [English] refs=None | mar : to damage
24	--- entry 2 ---
25	ROOT Mer-d -> redirect to Mer 2
26	--- entry 3 ---
27	ROOT Mereg -> redirect to Merg
28	--- entry 4 ---
29	ROOT [Avestan] Mereğa
30	Saĕna-mereğa : a large bird
31	dark hawk bird  (refs BQT:190; KLN:959)
32	#1 (parent #0) [Pahlavi] refs=BQT | murğ, merv : bird ; sĕn-murv : hawk bird
33	  #2 (parent #1) [Persian] refs=BQT:1211,1990; SYN:183 | morğ «مُرغ ١» : bird ; sîmorğ «سیمرغ» : a legendary bird
34	#3 (parent #0) [Sogdian] refs=SOD:217 | mrğ : bird
35	
```


## [2026-09-07T16:17:05.859Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-336.json",
 "description": "Read source JSON page 336"
}
```


### [2026-09-07T16:17:05.911Z] TOOL RESULT

```
{
  "pdf_page": 336,
  "book_page": 306,
  "entries": [
    {
      "part": 2,
      "root": {
        "name": "Mer 2\nMer-d, Mer-k\nMor-to\nSmerd",
        "lang": "Indo-European",
        "refs": "POK:735,970; AHD:1529",
        "gloss": "to rub away, harm, die\ndestroy\nmortal man\npainful"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Latin",
          "refs": "AHD",
          "words": [
            {"translit": "mors", "gloss": "death", "script": null},
            {"translit": "môr-târium", "gloss": "ground down, mortar", "script": null},
            {"translit": "mordĕre", "gloss": "to bite", "script": null},
            {"translit": "morbus", "gloss": "disease", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "mortal, mortuary, mortgage", "gloss": null, "script": null},
            {"translit": "mortar", "gloss": null, "script": null},
            {"translit": "remorse", "gloss": null, "script": null},
            {"translit": "morbid", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Old High German",
          "refs": "AHD; KLN:1461",
          "words": [
            {"translit": "smerzan", "gloss": "painful", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "English",
          "refs": "KLN:1461",
          "words": [
            {"translit": "smart", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mer 3",
        "lang": "Indo-European",
        "refs": "POK:737",
        "gloss": "to disturb"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "HRN:101,181",
          "words": [
            {"translit": "â-marš", "gloss": "to tolerate, be quiet", "script": null},
            {"translit": "pra-marš", "gloss": "to forget", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:706,1448",
          "words": [
            {"translit": "xâmŭš", "gloss": "quiet, turned off", "script": "خاموش"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan / Old Persian",
          "refs": "FFD:65",
          "words": [
            {"translit": "muš, fra-â-muš", "gloss": "to forget", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "FFD:65",
          "words": [
            {"translit": "frâmŭštan", "gloss": "to forget", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "FFD:65; MON:2506",
          "words": [
            {"translit": "faramŭšîdan", "gloss": "to forget", "script": "فراموشیدن"}
          ],
          "script_extra": "فراموشانیدن ، فرموشیدن\nفراموش ، فرامش، فرامشت ، فرامِشی",
          "note": null,
          "quote": {
            "text": "چون تیغ بدست آری مردم نتوان کشت - نزدیک خداوند بدی نیست فرامُشت",
            "poet": "Nâser-Khosrow"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Germanic",
          "refs": "AHD",
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "mar", "gloss": "to damage", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Mer-d",
        "redirect": "Mer 2"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Mereg",
        "redirect": "Merg"
      },
      "nodes": []
    },
    {
      "root": {
        "name": "Mereğa\nSaĕna-mereğa",
        "lang": "Avestan",
        "refs": "BQT:190; KLN:959",
        "gloss": "a large bird\ndark hawk bird",
        "see": ["Kei 1"]
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Pahlavi",
          "refs": "BQT",
          "words": [
            {"translit": "murğ, merv", "gloss": "bird", "script": null},
            {"translit": "sĕn-murv", "gloss": "hawk bird", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "BQT:1211,1990; SYN:183",
          "words": [
            {"translit": "morğ", "gloss": "bird", "script": "مُرغ ١"},
            {"translit": "sîmorğ", "gloss": "a legendary bird", "script": "سیمرغ"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sogdian",
          "refs": "SOD:217",
          "words": [
            {"translit": "mrğ", "gloss": "bird", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
```


## [2026-09-07T16:17:06.478Z] TOOL CALL #4: Bash

```json
{
 "command": "cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source matrix"
}
```


### [2026-09-07T16:17:06.514Z] TOOL RESULT

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


## [2026-09-07T16:17:28.840Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','AHD','KLN','BQT','MON','HRN','FFD','SOD','SYN','WLD','IEC','BRT','PHD','NYB','HUB','CHEUNG','SKT','LEW','LAT','FSD','WEB','ARY','IRN','FSF']:\n    v=d.get(k)\n    print('==',k, json.dumps(v,ensure_ascii=False)[:1200])\n\""
}
```


### [2026-09-07T16:17:30.205Z] TOOL RESULT

```
== POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt", "page_offset": "POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' gives the printed page directly. Online alternatives: https://indo-european.info/p
== AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp.1505-1550): https://archive.org/details/americanheritag00morr (1980 pr.), americanheritage1986morr, americanheritage0000unse_o7u0 — all lending; HathiTrust mdp.39015031593562 search-only", "identifier": "watkins-american-heritage-dictionary-of-indo-european-roots-1985", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt", "page_offset": "1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page.", "lookup_hint": "Online: single page https://ahdictiona
== KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein (1966); EtymologicalDictionary (1971 one-vol.)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt", "page_offset": "KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-styl
== BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qateh = same vol-1 scan; dli.ministry.25441 = a different Indian edition in 10 parts; McGillLibrary-118596-1400 = Adib Tusi's supplement, not the dictionary) ; vols 3-5: user-uploaded scans on picofile.com (links from farhangoadabeirani.blogsky.com post-482): vol 3 https://s3.picofile.com/file/8230740968/borhane_ghatee_jelde_3.pdf.html (ش–ل, Ibn Sina 2nd ed. 1342, 721 pp), vol 4 https://s6.picofile.com/file/8230741184/borhane_ghatee_jelde_4.pdf.html (م–ی, 553 pp), vol 5 https://s3.picofile.com/file/8230741300/borhane_ghatee_jelde_5.pdf.html (تعلیقات, Amir Kabir 5th pr. 1376, 293 pp). Same set behind login on ketabnak.com/book/55304-55307 and /58249.", "lookup_hint": "grep the headword in BQT_v1
== MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French) but WITHOUT the Latin-script Pahlavi/Avestan forms of the print edition (tested دیوار: shows '[ په . ] (اِ.) ۱- جداری از سنگ...'). Page numbers cannot be mapped online. Archive.org has only a 2-vol abridgement: https://archive.org/details/abu-abdurahman-kurdi-f_barid_01_20171226 (الف–ع) and ..._02_20171226 (غ–ی) = 'فرهنگ معین دوجلدی', Adena 1381, compiled by عزیزالله علیزاده — different pagination from the 6-vol edition; OCR downloaded as MON_part1.txt / MON_part2.txt (no page breaks).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part1.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/MON_part2.txt", "/home/sfmqrb/git/rishe/data/verification/source
== HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.", "notes": "OCR of German Fraktur-free text is decent; Persian script is not OCRed.", "cites": "page number of Horn, Grundriss der neupersischen Etymologie (1893); entries are also numbered"}
== FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt"], "page_offset": "115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X).", "covers_etymology": true, "notes": "Actual title is «ماده‌های فعل‌های فارسی دری» (Qoqnus). Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tessera
== SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --data-urlencode path={dir} --data-urlencode q={word}   (get server/dir from https://archive.org/metadata/{id}; e.g. server=ia800104.us.archive.org dir=/23/items/SogdianDictionary for BQT vol 1). Leaf images: https://archive.org/details/{id}/page/n{leaf}", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt"], "page_offset": "printed page ≈ leaf − 66 in SOD_pages.txt (0-based \\f blocks; 645 leaves; English intro precedes)", "covers_etymology": true, "notes": "
== SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt", "page_offset": "leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", "notes": "Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.", "cites": "page number of Buck, A Dictionary of Selected Synonyms (1949)"}
== WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org/details/in.ernet.dli.2015.106624 ; HathiTrust pdus full view mdp.39015066210405 / mdp.39015066210397 (browser only from this host)", "identifier": "in.gov.ignca.20339 (Band 3); also in.ernet.dli.2015.106625 (Band 3 duplicate)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/WLD_band3.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_text.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd1_1930_dli_70244_djvu.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD/WLD_Bd2_1927_dli_106624_t
== IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 650 = p.1270). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Reconstructed headword at line start followed by gloss in quotes and 'WP I, 456' refs, e.g. grep -n '^koks-' IEC.txt. Alphabetical by IE root.", "notes": "", "cites": "column/page number of Mann, An Indo-European Comparative Dictionary (1984–87)"}
== BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.", "notes": "Nourai's Table IV says 1979; that is the unchan
== PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).", "notes": "", "cites": "page number of MacKenzie, A Concise Pahlavi Dictionary (1971)"}
== NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.", "notes": " local_files: /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt (Part II, pp. 1-286); /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol1.txt (Part I, plain djvu.txt)", "local_files": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "/home/sfmqrb/git/rishe/da
== HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.", "notes": "Built from djvu.xml (no hocr); OCR quality moderate.", "cites": "page number of Hübschmann, Persische Studien (1895)"}
== CHEUNG null
== SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/SKT.txt", "page_offset": "leaf = printed + 20 (e.g. leaf 27 = p.7). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in caps at line start, e.g. grep -n '^TREE' SKT.txt; entries are terse with '(E.)', '(F.-L.)' language tags.", "notes": "Nourai says '1882-1967'; the 1967 Oxford reprint reproduces the 1911 rewritten edition, so the 1911 scan is the right pagination.", "cites": "page number of Skeat, Concise Etymological Dictionary"}
== LEW {"title": "A. Walde (& J. B. Hofmann), Lateinisches etymologisches Wörterbuch, 3rd ed., Heidelberg 1938-56", "edition_found": "2nd ed. 1910 (open); 3rd ed. 1938 vol. 1 is lending-only (lateinischesetym0000awal)", "kind": "archive_djvu", "url": "https://archive.org/details/lateinischesetym0000aloi", "identifier": "lateinischesetym0000aloi (1910); restricted 1938: lateinischesetym0000awal", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LEW_1910.txt", "page_offset": "1910 ed.: leaf = printed + 12 (e.g. leaf 15 = p.3). Page numbers of the 3rd ed. differ. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start. For 1938 pagination borrow lateinischesetym0000awal.", "notes": ""}
== LAT {"title": "A. Ernout & A. Meillet, Dictionnaire étymologique de la langue latine, 3rd ed., Paris 1951", "edition_found": "1951 (3rd ed.) - matches Nourai", "kind": "archive_djvu", "url": "https://archive.org/details/ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine", "identifier": "ernout-a.-meillet-a.-dictionnaire-etymologique-de-langue-latine (4th ed. 1959 lending-only: dictionnairetymo0000unse; another open copy: DictionnaireEtymologiqueDeLaLangueLatine)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/LAT.txt", "page_offset": "leaf = printed + 18 for most of the book (e.g. leaf 21 = p.3); drifts in places (leaf 219 = p.301 -> -82?? probably a mis-detected number) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Latin headword in bold at line start followed by gender/declension, e.g. grep -n '^pater,'.", "notes": "Built from djvu.xml; large (4.6 MB)."}
== FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440 (vol IV Sabi-Z)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSD_vol1.txt", "page_offset": "vol1: leaf = p + 41..56 (drifts; e.g. leaf 87 = p.46, leaf 612 = p.556); vol3: leaf = p - 1466 (e.g. leaf 215 = p.1681); vol4: leaf = p - 2144..2148 (e.g. leaf 229 = p.2373); vol2 offset not reliably detected (pages ~ 700-1640) - grep the headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword in bold at line start with pronunciation; etymology in brackets at entry end '[< L. ...]'. Very large OCR (16 MB per vol); grep -n '^word' vol file.
== WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, webstersnewtwent01webs 1983)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/WEB_vol1.txt", "page_offset": "not reliably detected (page_numbers.json sparse); grep headword. local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>", "lookup_hint": "Headword bold at line start; etymology in brackets. 2nd-edition pagination is the same across 1958-1983 printings, so a 1978 page number can be checked in the 1962 vol. 1 scan for words A-(mid alphabet); vol. 2 only via lending copies.", "notes": "", "cites": "page number of Webster's New Twentieth Century Dictionary, 2nd ed."}
== ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qate'. Find the page via the headword index incoming/ARY/ARY_headwords.json (when built) and fetch it with: python3 tools/ref_page.py ARY:<printed page> --image", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_latin_index_pages.txt"], "page_offset": "printed page = pdf page + 1", "scans": [{"file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/ARY_aryanpur_kashani_rishehaye_hend_o_orupayi.pdf", "first_printed": 1, "last_printed": 546, "pdf_offset": -1, "lang": "fas+eng", "ocr_text": "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY/
== IRN {"title": "Bahram Farahvashi, Iranvij, Tehran University Press 1368/1989", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ایرانویج-بهرام-فره-وشی/ -> https://dl.eliteraturebook.com/storage/img/ایرانویج.pdf (free PDF site; grey) ; Google Books kP8bAAAAIAAJ (1368 ed., no view)", "lookup_hint": "archive.org 'Iranvej' item is a radio programme, not the book; nothing on ketabnak/noorlib. | For pages in a scanned volume use: python3 tools/ref_page.py IRN:<page> --image (renders + OCRs only that page; Read the PNG when OCR is poor)", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_eliteraturebook.pdf", "/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/IRN/IRN_pages.txt"], "page_offset": "222 leaves; printed page = PDF page − 11 (PDF 101 = p.90; chapter openers carry no numeral). 6th printing 1382, same setting as 1368.", "covers_etymology": true, "notes": "Open scan downloaded (image-only) and OCRed. Image-only scan OCRed locally with tesseract 5 (fas.traineddata from github.com/tesseract-ocr/tessdata_fast, stored in incoming/_tessdata). *_pages.txt = 'fas' model (best for Persian); (only the 'fas' pass was run for
== FSF {"title": "Abdolhossein Noushin, Vazhe-namak: Farhang-e Vazheha-ye Doshvar-e Shahnameh (Farhang-e Shahnameh), Donya 1363/1984", "kind": "archive_djvu", "url": "https://archive.org/details/20220809_20220809_1444", "lookup_hint": "grep the headword in FSF_pages.txt (alphabetical glossary); use inside.php search for leaf numbers. Also https://archive.org/details/nooshinshahnameh is a different Noushin book (گزارشی چند درباره شاهنامه).", "local_file": ["/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF_pages.txt", "/home/sfmqrb/git/rishe/data/verification/sources/refs/FSF.txt"], "page_offset": "484 leaves; edition/printing of this scan not identified — determine offset from printed page numbers on the page text/image when checking", "covers_etymology": false, "notes": "Persian OCR fair (readable prose). Mostly glosses; some Pahlavi/Avestan notes. Edition may differ from the 1363 Donya print Nourai used."}
```


## [2026-09-07T16:17:33.627Z] TOOL CALL #6: Bash

```json
{
 "command": "sed -n 1,200p /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-07T16:17:33.670Z] TOOL RESULT

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


## [2026-09-07T16:17:40.065Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"lemma: mer\" POK_full.txt | head -40\necho \"=== smerd\"\ngrep -n \"lemma: smer\" POK_full.txt | head -20\necho \"=== pages\"\ngrep -n \"Page(s): 735\" POK_full.txt | head; grep -n \"Page(s): 737\" POK_full.txt | head; grep -n \"Page(s): 970\" POK_full.txt | head"
}
```


### [2026-09-07T16:17:40.155Z] TOOL RESULT

```
40298:It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
58134:< kw\; alb. proves that from Root / lemma: mer-2, *extended mer-ek-\ "to shimmer, shine' 
60116:Root / lemma: mer-4, mera- 
60176:Root / lemma: mer-5, mera- 
60183:Root / lemma: mer-5, mera-\ to rub, wipe; to pack, rob, derived from extended Root/ 
60285:It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
60313:Root / lemma: mer-6, mer-s- 
=== smerd
78543:Root / lemma: smerd-, smord- 
78564:Root / lemma: smeru- 
=== pages
60174:Page(s): 735 
60311:Page(s): 735-737 
60328:Page(s): 737-738 
78562:Page(s): 970 
78584:Page(s): 970-971
```


## [2026-09-07T16:17:42.662Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '60110,60340p' POK_full.txt"
}
```


### [2026-09-07T16:17:42.712Z] TOOL RESULT

```
bathe, wallow '. 

References: WP. II 279 f., Trautmann 169, Specht Indo Germanic Dekl. 119. 

Page(s): 734 

Root / lemma: mer-4, mera- 

Meaning: to die 

Note: (= mer-5^ become faded ') 

Material: Old Indie marati, marate ^d'\es\ Armenian meranim^6\e\ gr. Efjoprsv " died ' Hes. 

(compare Lithuanian men's m., mirei. "death', merdeti^be dying'); causative Old Indie 

marayati' slays ', osset. /775/y/7"slay', Lithuanian marinti, serb. mdr/f/6s., etc.; zero grade 

Old Indie mr/yate^6\es', Avestan miryeite{= me'rye'te) ds.. Old pers. a-mariyata^he died ', 

Latin morior {*mr-idr) "I die, expire '; Balto-Slavic *m/re-\n Lithuanian mirstu, m/rt/^6\e', 

Latvian mirstu, m/rtds. (in addition Lithuanian m/re'the dead ', Latvian m/rejsm. " dying, 

death '); Old Church Slavic mtrg, mret/an6 -mbret/6s., Hittite me-ir-ta {mert) " died '. 



participle mf-to-^ dead ' in Old Indie mrta-= Avestan msrsta-^ dead ', Armenian mard 
"person' ("mortal, human being'), Latin Morta, "Death goddess', Balto-Slavic *mirta-^ dead 
' in Lithuanian mirtoji diena^ anniversary of somebody's death ', Old Church Slavic u- 
mrbtijeu. "death', etc.; ^-/77/-to- "immortal, living ' in Old Indie amrta-, Avestan amasa-, gr. 
apppoToq (Aeolic po for pa), therefrom apppoaioc; " belonging to the immortal '; from 
aM(3poTO(; abstracted ppoT6(; " perishable ' and pp6T0(; " blood that has run from a wound, 
gore, coagulated blood ' (M. Leumann, Homer. Worter 126 ff.). 

/77/-/'d-/77 "death' in Old Indie mrta-v\. "death'. Old High German mord. Old English Old 
Icelandic mordu. "murder' (besides *mr-tro-m\v\ Gothic maurt^ru.. Old English mordoru. 
"murder'). 

/T?/-/"/- "death' in Old Indie mrti-, Avestan msreti-, Latin mors, -tis, Lithuanian mirtis. Old 
Church Slavic si>-mrbtb {irorc\ *-mrbtb), serb. smft, etc. 

Maybe alb. /77c»/Y"funerar, /770/^e "death' a Latin loanword. 

/77/-/it/ "death' in Armenian mah, older marfr, with -//■ contaminated: Old Indie mrtyu-, 
Avestan msrs^yu- 6s. 

mor-to-^ perishable ' in Old Indie marta-, Avestan /77as5- "person', with sound change 
mareta-^ perishable, mortal, human being', gr. popT6(; "person, mortal, human being' Hes. 
(for *p6pT0(;); derived *mor-t/o-\n Old Indie martya-, Avestan masya-. Old pers. martiya-^ 
perishable, mortal, human being'. 

mf-u6-^ dead ' in Old Irish mart, cymr. etc. marw, gall. *marvos{U.-\-. 5387a); unclear 
gall. (?) Mori-marusa^ mortuum mare '; through influence oi mr-tu- to *mr-tu-o-\n Latin 
mortuus' dead ', Old Church Slavic mrbtvb {mrbtvb) ds. 

/77d/"0-5 "death' in Old Indie /77a/'a- "death', Lithuanian maras^ plague ', Old Church Slavic 
morb ds. 

After Thieme Studien 55 here (?) gr. papTU(; (*-p<;), -po(;, hom. papTupo(; " witness, 
testifier ' (" Schworender ') from * mrt-tur- {11) "the griping death ' (root /it/e/"- "catch'). 

References: WP. II 276, WH. 112 f., Trautmann 186 f., Thieme Studien 15 ff. 
Page(s): 735 

Root / lemma: mer-5, mera- 
Meaning: to rub, wipe; to pack, rob 



Note: 

Root / lemma: mer-5, mera-\ to rub, wipe; to pack, rob, derived from extended Root/ 

lemma: mah-1 \ to becl<on with the hand; to deceive + with formants -ra-: 

Material: Old Indie mrnati, mrnatT robs ', a-man-tar-^ robber ', amrnaV robbed ', malf-mlu- 

" robber'; but mrnati^ crushes, smashes ', murna-^ crushed, damaged, faded ' belong 

rather to mel-1, also maru-m. 'sand, desert, waste, wasteland, rock'; 

gr. [japaivu) " rub, wipe, consume, weaken'. Pass. " verzehre myself, verschwinde 

i 

allmahlich, ermatte ', |japaaM6(; ' Hinschwinden, Krafteverfall '; papva|jai ' fight '; 
Mappapo(; ' stone, boulder ' (compare Latin rupes : rumpo), later (after papfjaipoj) "white 
stone, marble ' (out of it Latin marmoi); 

Latin morfar/um ' mortar' (due to from *mr-fds' pulverized, ground into fine particles; 
crushed '); about moretum' a rustic dish made of garlic, rue, vinegar, oil ' s. WH. II 112; 
morbus^ a sickness, disease, disorder, distemper, ailment, illness, malady ' {*mor-b^os); 

Old Irish meirb^ inanimate, lifeless ', Middle Irish meirb, cymr. merw^s\ack, weak' {mer- 
uh)\ Middle Irish meirlei. " robbery, theft ', meirlech^ robber '; Old Irish mrath^ betrayal ', 
cymr. brad 6s. ( *mr9-to-) to Old Irish *marnaid' betrays ', subjunctive -mera; 

Old Icelandic /Tre/ya (preterit marda) "hit, grind '; Old High German mam, maramar\6 
mur(u)wi^ friable, tender, mature, ripe, mellow, seasoned ', Old English mearo^ friable, 
tender'. Old Icelandic morna^ wither', Norwegian moren, maren^ rotten, decayed, 
decomposed; brittle '; nisi. morr\. "dust, powder'. Old Swedish mort^^ crumbly mass, offal'; 

Serb, mfva^ crumbs '; Old Bulgarian iz-m rhm brati ^ ro6er^\ Old Russian -moromradr 
gnaw, crumble '; 

Hittite marriattarT it is shattered '. 

morat " goblin ': Old Irish mor-(r)Tgain^\arr\\a, mythological monster having a woman's 
head and torso and a snake's body (Classical Mythology) ', actually " evil queen ' 
(/77d/'/7^5//7 supported in /77d/'"big, large'). Old Icelandic mara. Old High German mara. Old 
English mare {Uo6err\ High German Mahr, Nachtmahr rw.) " the supernatural female being 
which sits down on one's breast at night ', Serbo-Croatian-Church Slavic mora^ witch ', kir. 
mora^ goblin, ghost' etc. 

Maybe alb. {ke-mer) kmer, {te-merr) tmerr, mner, mer^ horror ' a Slavic loanword : Polish 
koszmar^ horror ' < russ. -Church Slavic mara^ emotion, strong feeling ', poln. mara^ 



deception ', etc.; See Root / lemma: mah-1\ to beckon with tlie liand; to deceive + with 
formants -ra- 

mer-g-: 

Middle Low German morken^ crush'. Old English murc(n)ian^ grieve ', murc^ 
oppressive, gnawing (of hunger) '; s. further under {merk-), merg-^ rotten, decayed ' etc., 

mer-d-: 

Old Indie mrdnati {mrdmta-, mrdita-), mardati, mardayati^ grinds, crushes, rubs ', 
Avestan 3. Sg. morandal {= mrnd-) " destroys ' (these Aryan words also are carried in Indo 
Germanic meld-, s. mel-1. Old Indie /77/o'/7a// perhaps instead of *mrnatti {*mr-n-ed-ti) 
through influence of mrnat/{see above S. 735); 

Armenian /77a/'/ 'fight, struggle'; 

gr. pap5r|v to pia^soGai yvvaiKaq ApinpaKiaJrai Hes. {*mrd-); apspSu) "rob' and " blind, 
darken', pspSsi kojAuei pAanrei Hes.; to Aor. ajJEpaai neologism aijeipoj; 

East Frisian murt^ crumbly mass, dust, powder'. Low German murten^ decompose ', 
Middle High German /t?^/^ 'stump', Swiss murz, morz^sxwaW shred'; 

Latvian merdeV let starve ' (latter meaning closer to Lithuanian merdeti, present 
merdmi, merdziu "die', that based on do- or d^opresent to *mer- "die', as also mer-d- "rub' 
would go back to o'opresent; is placed Latvian merdet Wkemse to mer-^d'\e'7); 

Latin mordeo, -ere, momordV to bite, bite into ' (= Old Indie mardayati, mamrde), also 
from feelings and sensations of taste; 

compare the 5-forms: 

gr. apspSvoc;, ap£p5aA£0(; "terrible, dreadful' ("*attritional '), Old High German smerzan 
"ache', 5/775/^0 "pain'. Middle Low German smerten. Low German Dutch smarten. Old 
English smeorfan ^ ache' , engl. 5/77a/Y "biting, sharp, witty ' and " nice, dainty'; compare also 
5/77er{/- "stink'. 

mer-k- 

Old Indie marcayat/" endangers, injures, hurts, disables, damages ', mrkta- "\n\ures, 
hurts, disables', marka-m. " dying, death' = Avestan /77a/7/'/ra- "death', conservative stem 



Old Indie Instr. Sg. mrc-a, Avestan maraxs^r\i\'c\, destruction ', Avestan maranca/t/ "\n\ures, 
hurts, disables, destructs '; Armenian more' young, tender' {*morkio-)\ 

perhaps alb. /770/7-' louse' ( *mdrko-' the scratching '? compare cpGsip ds.: cpGsipoj); 

Maybe alb. {*bddr) momlouse' : gr. cp9£ip ds.: cpGsipw : modern Greek ijjsipa : Basque 
(*9£ipu)) zorn" louse '. 

Note: 

It seems that from Root / lemma: g^hder- : to run, flow, derived Root / lemma: mer-5, 
rnera-: to rub, wipe; to pack, rob, common lllyrian g'^h- > b. 

Latin /77i//ri/5 "mutilated' (out of it sizil. pupKoc; " dumb ') and murc/dus"\d\e, slack'; Middle 
High German /77c»/ye/7 'slack'. 

With ani. 5- Lithuanian smerkt/" condemn, censure, blame, reprobate, reprehend, 
declaim, deplore, sit in judgement ', 5/77a/'/r^s "cruel, savage', pa-smerkt/^spoW, Modern 
High German dial, schmorgen' starve, suffer'. 

Here (as " chaff ') Old English mearg^ sausage ' = Old Icelandic mgrr'6s., intestinal fat ' 
( *marhu-), redupl. gr. pipapKui; " blood sausage '; Hittite mar-kan-zi^ cut up '. 

see also /77e/ifr-i' "sullen' and 1. mei1(- " rotten, blight etc.'. 

mer-s- 

Old Indie masam, masfm kar-^ pulverize ', masi-, masV powder '; 

Old High German morsar/^ mortar' (reshaped from Latin mortarium, s. S. 736), Middle 
High German zermursen ' crush, squeeze hard, squash ', md. zermorschen ds., Swiss 
morsen, mursen' crunch, shove ', Middle High German Low German mursch, murs. 
Modern High German morsch, Dutch morzelen^ grind '. 

References: WP. II 276 ff., WH. 42, 110 ff.; 
See also: identical with mer-4. 
Page(s): 735-737 

Root / lemma: mer-6, mer-s- 
Meaning: to bother, anger, etc.. 



Material: Old Indie mrsyate' forgets, neglects, forgives ', marsa-xw. " patience ', mrsa 
"free, wrong ', Kaus. marsayatT suffers, forgives '; Armenian moranam ^iorqei' (Meillet, 
Esquisse2 40); Gothic marzjan ^ anger' , Old English mierran. Old Saxon merrian. Old 
Frisian meria. Old High German marren, /77e/7'e/7 'hinder, disturb, bother'; Old English a- 
m/erran'spoW, Old Frisian mere'ban6, strap, manacle'; Lithuanian marsas^ oblivion ', in 
addition marsus^ forgetful ', Latvian aiz-marsai. 'forgetfulness'; Lithuanian mirstu, mifsti 
(only with uz-, pa-) and Latvian aiz-mirstu, a/z-m/rst lorgotten' , Lithuanian Kaus. mars/nt/" 
make forget '. 

References: WP. II 279, Trautmann 187. 
Page(s): 737-738 

Root / lemma: met- 

See also: see above S. 703 f. under me-2 and me-3. 

Page(s): 741 

Root / lemma: meug-1 

Meaning: to take by surprise, wily 

Material: Latin muger^ der Falschspieler beim WiJrfelspiel ' {*mug-ro-s^ lurking ');
```


## [2026-09-07T16:17:51.137Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '78540,78570p' POK_full.txt"
}
```


### [2026-09-07T16:17:51.196Z] TOOL RESULT

```
Page(s): 969 

Root / lemma: smerd-, smord- 
Meaning: to stink 

Material: Gr. O|j6p5(jov£(; PI. "Stanker' Hes.; a|jop5o0v auvouaia^£iv; Lithuanian smirdziu, 
sm/rdet/ ^st\nk', Latvian sm/rdef6s., Lithuanian 5/77//'o'e/e "dwarf elder', s/775/'o'//7//"stinkend 
make', Latvian s/77e/io'e//s "Stanker', smards' fetidness ', Lithuanian smar[d]ve. Old 
Lithuanian smarstas' fetidness ' (also smarste, smarstvas, s/77a/'S55"schlechteres fat', 
actually " bad-smelling fat'). Old Prussian smorde^ alder buckthorn, alder dogwood '; Old 
Church Slavic smrbdeti, russ. smerdetb "stink', russ. smorod' fetidness ', smorodina' 
black currant ', poln. smrod, Czech smrad' fetidness '; in addition probably Latin merda 
"ordure, ordure of Leibes'. 

5/77e/'o'- "stink' is eine probably already Indo Germanic verselbstandigte use from 
{s)merd- in Modern High German schmerzen, Latin mordere, s. mer-, merd " chafe ' 
(above S. 736 f), originally also "beiftender smell, odor'. 



References: WP. II 691, WH. II 74 f., Trautmann 271, Vasmer2, 676, Specht KZ 62, 215. 
Page(s): 970 

Root / lemma: smeru- 

Meaning: grease, fat 

Material: Gr. probably apupi(; "Schmirgel zum Abreiben and Polieren', (a)|jupi^u) 'poliere 

through Reiben, anoint, smear, rub', [jupov n. "wohlriechendes Salbol, plant juice ',
```


## [2026-09-07T16:17:59.302Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"mortgage\\|mortuary\" AHD_watkins1985.txt | head -20\necho ===\ngrep -n \"^mer-\\|^smerd\\|^mers-\\|^merǝ\\|^mer\" AHD_watkins1985.txt | head -30"
}
```


### [2026-09-07T16:17:59.354Z] TOOL RESULT

```
Exit code 1
753:mer-2, To rub away, harm. I. 1. Germanic *marén-, goblin, in Old English mare, mere, goblin, incubus: NIGHTMARE. 2. Greek marainein, to waste away, wither: MARASMUS; AMARANTH. 3. Probably suffixed zero-grade form *mr-to-, “ground down,” in Latin mortdrium, mor- tar: MORTAR. 4. Possibly extended root *merd- in Latin mordére (past participle morsus), to bite: MORDACIOUS, MORDANT, MORDENT, MORSEL; PREMORSE, REMORSE. 5. Possibly suffixed form *mor-bho- in Latin morbus, disease (but more likely of unknown origin): MORBID. II. Possibly the same root, but more likely distinct, is *mer-, “to die,” with derivatives referring to death and to human beings as subject to death. 1. Zero-grade form *mr- in: a. suffixed form *mr-tro- in Germanic suffixed form *mur-thra- in Old English morthor, murder: MUR- DER; b. suffixed form *mr-ti- in Latin mors (stem mort-), death: MORT!, MORTAL, MORTUARY; AMORTIZE, (IMMOR-
754:‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
1115:wadh-1. A pledge; to pledge. 1. Germanic *wadi- in: a. Old English wedd, a pledge, marriage: WEDLOCK; b. Old English weddian, to pledge, bind in wedlock: WED; c. Old French gage, a pledge: GAGE!; DEGAGE, ENGAGE, (ENGAGE), MORTGAGE; d. Old North French wage, a pledge, payment, and wagier, to pledge: WAGE, WAGER. 2. Latin praes (< *prai-vad-), surety, pledge (< “that which is given before”; prae-, before; see per’): PRAE- DIAL. [Pok. wadh- 1109.]
1889:MORTGAGE mer-2, wadh-1
1892:MORTUARY mer-2 MORT! mer-2 MORULA moro- MOSAIC men-1 MOSQUITO = mu-2 MOss meu- MOssO meue- MOST mé-3
(eval):3: == not found
```


## [2026-09-07T16:18:03.756Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"smerd-\\.\" AHD_watkins1985.txt | head\ngrep -n \"smerd-,\" AHD_watkins1985.txt | head\necho === mers\ngrep -n \"mers-\" AHD_watkins1985.txt | head\necho === MAR\ngrep -n \"^MAR \\|MAR mer\" AHD_watkins1985.txt | head"
}
```


### [2026-09-07T16:18:03.822Z] TOOL RESULT

```
Exit code 1
754:‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
(eval):4: == not found
```


## [2026-09-07T16:18:07.724Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"smerd\" AHD_watkins1985.txt | head -10\necho \"=== mers / mar\"\ngrep -n -i \"\\bmars-\\b\\|mers-\\|marzjan\\|mierran\" AHD_watkins1985.txt | head -10\necho \"=== SMART\"\ngrep -n \"SMART\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-07T16:18:07.808Z] TOOL RESULT

```
754:‘ TAL), MORTGAGE, MORTIFY, MORTMAIN, POSTMORTEM; c. suffixed form *mr-yo- in Latin mori, to die: MORI- BUND, MURRAIN; d. prefixed and suffixed form *n-mr-to-, “undying, immortal” (*n-, negative prefix; see ne), in (i) Greek ambrotos, immortal, divine (a- + mbrotos, brotos, mortal): AMBROSIA (ii) Sanskrit amrta, immortal (a- + mrta, death): AMRITA. 2. Suffixed o-grade form *mor-t-yo- in Old Persian martiya-, a mortal man, in Iranian compound *martiya-khvdra- (attested in Persian mard-khvdr), ‘‘man-eater”’ (*khudra-, to eat; see swel-'), probable source of Greek mantikhoras (corrupted from martiokhéras), manticore: MANTICORE. See extended root smerd-. [Pok. 4. mer-, 5. mer- 735.]
962:Sao Pain. Extension of mer-?. Germanic *smarta- in Old English smeart, causing pain, painful: SMART. [Pok. smerd- 970.]
2271:SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
=== mers / mar
760:merk-'. To decay. Latin marcére, to decay, wither: MARCESCENT. [Pok. 1. merk- 739.] [merk-2. Italic root, possibly from Etruscan, referring to aspects of commerce. 1. Latin merx (stem merc-), mer- chandise (> mercdri, to trade): MARKET, (MART), MER- CER, MERCHANT; COMMERCE. 2. Latin merces, pay, reward, price: MERCENARY, MERCY. 3. Probably Latin Mercurius, the god of (inter alia) commerce: MERCURY. [In Pok. merk- 739.]] [merph-. Form. Greek root of unknown origin. 1. Suf- fixed o-grade form *morph-G- in Greek morphé, form, beauty, outward appearance: -MORPH, MORPHEME, MOR- PHO-, MORPHOSIS. 2. Possibly borrowed from Greek morphé, via Etruscan, is Latin forma, form, shape, contour, appearance, beauty: FORM, FORMAL, FORMULA; CONFORM, CORACIIFORM, DEFORM. [In Pok. 2. mer- 733.]] mers-. To trouble. Suffixed o-grade form mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.] meu-. Damp; with derivatives referring to swampy ground and vegetation and to figurative qualities of wetness. 1. Extended form *meus- in Germanic *meus-, *mus- in: a. Old English mos, bog: Moss; b. Old Norse mosi, bog, moss, akin to the Scandinavian source of LITMUS. 2. Germanic suffixed form *meuz-i- in Old Norse myrr, bog: MIRE; (QUAGMIRE). 3. Suffixed zero-grade form *mus-to- in Latin mustus, new, newborn (< “wet”): MUST’, MUSTARD. 4. Possibly suffixed extended zero-grade form *mii-ro- in Greek murios, countless (< “flowing, endless”): MYRIAD. 5. Possibly suffixed ex- tended zero-grade form *mud-so- in Greek musos, un- cleanness: MYSOPHILIA, MYSOPHOBIA. [Pok. 1. meu- 741.] meue-. To push away. Latin movére, to move (> mobilis, neuter mobile, fickle, changeable): MOB, MOBILE, MO- MENT, (MOMENTOUS), MOMENTUM, MOSSO, (MOTIF), MO- TION, MOTIVE, MOTOR, MOVE, MOVEMENT; COMMOTION, EMOTION, PROMOTE, (REMOTE), (REMOVE). [Pok. 2. meu- 743.) meug-'. To act surreptitiously. Germanic *muk- or Celtic *mug- in Old French muchier, to skulk: MOOCH. [Pok. 1. meug- 743.] meug-2. Slimy, slippery; with derivatives referring to various wet or slimy substances and conditions. Enlarged form of meu-. 1. Nasalized form *mu-n-g- in Latin mungere, to blow the nose: EMUNCTORY. 2. Possibly Germanic *(s)mug-, referring to wetness and also to figurative slipperiness: a. Old English smoc, shirt: smock; b. Middle High German smuck, “clothing,” adornment, jewel: scHmMuCK; c. Old Norse mugga, driz- zle, akin to the source of Middle English muggen, to drizzle: MuGGY; d. Low German smukkelen, smuggeln, to smuggle (< “to slip contraband through”): SMUGGLE; e. Middle Low German smucken, to adorn (< “to make sleek”): SMUG; f. Old Norse mygla, mold, mildew, akin to the source of Middle English molde, mold: MOLD®. 3. Ger- manic *meuk- in Old Norse mjikr, soft: MEEK. 4. Variant form *meuk- in Latin miicus, mucus: MOIST, MUCILAGE, MUCO-, MUCUS, (MUSTY). 5. Zero-grade variant form *muk- in: a. Greek mukés, fungus, mushroom: -MYCETE, MYCO-; STREPTOMYCES, (STREPTOMYCIN); b. suffixed form *muk-so- in Greek muxa, mucus, lamp wick (< “nozzle of a lamp” < “nostril”): MATCH2, Myxo-. [Pok. 2. meug- 744.] mezg-'. To dip, plunge. 1. Latin mergere, to dip, dive: MERGE; EMERGE, IMMERSE, SUBMERGE. 2. Latin mergus, diver (water bird): MERGANSER. [Pok. 1. mezg- 745.] mezg-*. To knit. Germanic “mésk- in Middle Dutch a maesche, knitted fabric: MESH. [Pok. 2. mezg- 746. [mimos. A mime. Greek noun of unknown origin. MIME, MIMESIS, MIMIC.] [miser. Wretched, unfortunate. Latin adjective of un- known origin. MISER, MISERABLE, MISERY; COMMISER- ATE.]
1816:MAR mers-
=== SMART
962:Sao Pain. Extension of mer-?. Germanic *smarta- in Old English smeart, causing pain, painful: SMART. [Pok. smerd- 970.]
2271:SLOE slii- SLOGAN gar-, sloug- SLOOP sleubh- SLOP! sleubh- sLop2  sleubh- SLUG? sleu- SLUGGARD §sleu- SLUMBER sleu- SLUMGULLION leb-1 SLUMP leb-1 SLURP srebh- SLUSH sleu- SLY slak- SMACK! smeg- SMACK? smeg- SMALL mélo- SMALT mel-1 SMART smerd- SMEAR (s)mer-3 SMEARCASE (s)mer-3 SMELT! mel-1 SMELT2 mel-1 SMILE smei- SMIRK smei- SMITE smé- SMITH smi- SMITHY smi- SMOCK meug-2 SMOKE smeug- SMORGASBORD _ bherdh- SMUG meug-2 SMUGGLE meug-2 SNAIL sneg- SNAKE sneg- SNAP snu- SNARE! (s)ner- SNARE? (s)ner- SNARL!  sner- SNATCH snu- SNEER sner- SNEEZE pneu-
```


## [2026-09-07T16:18:26.791Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"hāmōš\\|hâmoš\\|xāmōš\\|chāmōš\\|chamos\\|hamos\\|framōš\\|framoš\\|frāmuš\\|framus\" HRN.txt | head -30"
}
```


### [2026-09-07T16:18:26.843Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-07T16:18:30.917Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"amōš\\|amoš\\|amosch\\|āmōš\\|mōš\" HRN.txt | head -30\necho \"=== leaf for p.101 (leaf=printed+21 -> leaf 122) and p.181 -> leaf 202\"\nawk 'BEGIN{RS=\"\\f\"} NR==123' HRN.txt | head -60"
}
```


### [2026-09-07T16:18:32.207Z] TOOL RESULT

```
=== leaf for p.101 (leaf=printed+21 -> leaf 122) and p.181 -> leaf 202
— 101 —
in weit ausgedehnterem Grade verwendet. Vergl. -J
(Nu. 53) unter 'Verlorenes Sprachgut*.
452. 6ehüv 'vier , ceharmn, cär^ darum (AM. neben öehärum),
cärlpäi, car[sa (syr. LW. ''1D1NTO*', arab. LW. cahdrsOg),
cdr[deh (Sahn. I, 211 Vers 1479) etc.
aw. öa^warö Vier*; phlv. cahär, päz. cihär; ai.
catcdms; arm. rorU (H. No. 241).
kurd. (Sihna) cacar; af/. calör; oss. d. aippar, t.
cippar (321); wa;^. cahur, cahiir , sar. cavur, cavor,
%n. cavor, cavdr, yayn. t/ö, sangl. sa/ör, niinj. ca//r.
453. rlhr, cihre 'Ursprung; Angesicht'.
ap. Chira- 'Geschlecht, Ursprung; aw. riiira- Ur-
sprung: Gesicht'; phlv. citre (Münzen, Inschriften),
cihr, cihrak, cihrakömand 'die Merkmale der Periode
habend*; ai. citra- 'hell etc.'
kurd. cdre\ afy. cTra, stra,
454. rihil, 6ü 'vierzig*.
aw. ca&waresata Vierzig*; piiz. cihal^ cihU^ cd; ai.
catvdrirlQdU,
kurd. öel, cehl; afy. cctlve^t.
455. ctden sammeln; schneiden', Praes. öm-em, ein, eine,
aw. i/^cay-, mit Praep. /ra *sammeln*; phlv. citaH,
einet (Men.) 'sammeln', cimtan (vd. 5 (159) Gl.); ai.
|/cay- cinoti sammeln, einsammeln'.
kurd. einin 'erndten*; bei. cwaff, n. J'may 'sammeln,
auflesen, aufheben* (60) ; sar. ciy^am, ctdam 'schneiden,
emdten*.
456. eer wacker, mutig*'), eure, eeregl.
ai. cSrU" 'begehend (ein heiliges Werk), Nöldeke
(mündliche Mitteilung); phlv. cer (für aw. Hyra-), certh.
Das Päzend hat den ursprünglichen Majhülvokal
noch bewahrt, der auch im indischen Persisch ver-
schwunden ist.
457. CT» etwas*.
1) Reimt auf Igr, Vis und Rämln, S. 40 Vera 10, rtahn. I, 132
Vers 62.
```


## [2026-09-07T16:18:42.962Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 124 125 126 127 128 129 130 131 132; do echo \"----- leaf $i\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | head -50; done | grep -n -i -A6 -B2 \"mos\\|moš\\|schweig\\|still\" | head -60"
}
```


### [2026-09-07T16:18:44.230Z] TOOL RESULT

```
53-afy. öm, um; bei. hämag, n. häniay, liänvcuj (155);
54-wa/. yüng,
55:464. yritnös^) ^schweigend, still*, /ämösl.
56-skr. a + \/^marS' geduldig ertragen' ; vergl. fcrämös
57-(No. 812).
58-465. ^Jiän, yßne 'Haus , xänef/T.
59-phlv. /ßnak, /an, /änaklk (n''Nn"*2, Nöldeke,
60-ZDMG. 46, 142).
61-Von i^khan- 'graben'. Vergl. np. (arab.) yendeq
```


## [2026-09-07T16:18:50.748Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in 124 125 126 127; do echo \"----- leaf $i\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' HRN.txt | sed -n '1,3p'; done\necho \"===== find 464 leaf\"\ngrep -n \"464\\. \" HRN.txt | head\necho \"===== Horn 812\"\ngrep -n \"812\\.\" HRN.txt | head"
}
```


### [2026-09-07T16:18:51.977Z] TOOL RESULT

```
----- leaf 124
- 102 —
päz. cih (phlv. HD) + cij/ bezw. c7/, in einem Worte
päz. eis (?) (phlv. cnj?^).
----- leaf 125
— 103 —
(7) Gl.), rTstjayee, ä/ezJt (Phlv.-Vend. für aw. [^ha/s-;
AV.), päz. d/ezed (Men.).
----- leaf 126
1-4 -
Hüb.sohniann. Zr»Mü. :>. 42o.
47<.». '/jtjeffte *^'e^tÄ'i>.-T. jiüoklich". ver^l. fer[jriijeste.
----- leaf 127
— 105 —
. y^erbuze, /erbtu^) *Melone' (wörtl. *Eselsgurke').
phlv. /arböjhia, kharbuzak (PP61.), vergl. höjlna =
===== find 464 leaf
4248:464. yritnös^) ^schweigend, still*, /ämösl.
===== Horn 812
2980:812. piSmanj pemän^ ptizmän (8ähn. I, 359 Note 2, Calc.)
7092:812. feramöS Vergessend; Vergessenheit', ferämus^ fera-
12152:, /eramöi 812.
12155:i/«-fa>ö«tJ.'-. 812.
12158:ferämiii 812.
12161:JerämuSt 812.
12649:Äß//fr 812.
16014:/r,.«,öl 812.
18041:+ pra 812.
20793:' samösag 812.
```


## [2026-09-07T16:18:59.950Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '7085,7110p' HRN.txt\necho \"=== which leaf/page contains line 7092\"\nawk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"812. feramöS\")>0) print \"leaf(1-based)=\"n; }' HRN.txt\nawk 'BEGIN{RS=\"\\f\"} NR==202 || NR==203 {print \"--- leaf\",NR; print substr($0,1,120)}' HRN.txt"
}
```


### [2026-09-07T16:19:01.532Z] TOOL RESULT

```
(128)). Man könnte natürlich auch schon im Pehlevl ffäx lesen, doch
sclM'iiit OS besser, «lor Päzondausspraclie, welche h hat, zu folgen.— 181 —
811. ferüx Vorwärts, aufwärts; offen' etcJ).
aw. frq^ Vorwärts' (schw. St. ^frac-^ vergl. N. pr.
FrOdi/a-); phlv. fräd- (päz. fräz^ frfl^); ai. pränc-
(schw. St. präC') ^vorwärts*.
oss. räzäi Von vorn* etc. (210).
812. feramöS Vergessend; Vergessenheit', ferämus^ fera-
muSt^ fer(a)mösiden (Vis und RämTn, S. 50 V. 13).
ai. pra + |/';/?«rs-, ////ifya^c Vergessen' ; y\\]w , framös
bezw. farmös^ framöst^).
bei. samusag, samDsay, n. samusay^ Samösay Ver-
gessen (361), mit anderem Pracfix.
813. ferbih, ferheh^ ferhl (d. i. "^ferhiQi)) 'fett'. Vergl. np.
pih (No. 365).
aw. frapi^wa- 'Voizug, first-rate' (Geldner, Ve-
dische Studien 11, 17iJ)'^); phlv. frapili hi^zw. farpfh;
ai. prapitüd' (vergl. Geldner a. a. (). 155 folg.).
LW. wa;^. farhl^ sar. farhe,
Jüd.-pers. HO*!^ (Is. 17, 4) geht auf ein ap. *//(/-
2)itU' zurück.
814. ferjätn *Ende\
ap. ^frajäma- {{^gani- 'gehen*); \)\\\v, frajäm bezw.
farjam 'Ende', frajämtnltany vergl. fraj(a)ftan (AV.,
jung in Kolophonen. Siehe No. 113).
815. ferxane V^eise, gelehrt*, ferzanegl.
=== which leaf/page contains line 7092
leaf(1-based)=203
--- leaf 202
— 180 —
ap. ^\^, fra\ plilv. fra bezw. /ar, arm. LW. ]ira-\
ai. ]prd,
kurd. AiZ-, hol-,
808. /<9ri* 'Glanz, Majestä
--- leaf 203
— 181 —
811. ferüx Vorwärts, aufwärts; offen' etcJ).
aw. frq^ Vorwärts' (schw. St. ^frac-^ vergl. N. pr.
FrOdi/a
```


## [2026-09-07T16:19:12.855Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"marš\\|mar/s\\|maṛš\" CHEUNG.txt | head -40"
}
```


### [2026-09-07T16:19:12.906Z] TOOL RESULT

```
17746:*marš ‘to forget’
```


## [2026-09-07T16:19:15.504Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '17740,17820p' CHEUNG.txt"
}
```


### [2026-09-07T16:19:15.555Z] TOOL RESULT

```
‘doubt’ 
*REFERENCES: EVS: 49b, 48b; Werba 1997: 313 


*marš ‘to forget’ 

*MIDDLE PERSIAN: (+ *fra-à-) MMP fr’mws-, ВМР pl’mws- /framos-/ ‘to forget’. © 
Henning 1933: 185 is sceptical about the connection of the Persian forms with 
*mars (on account of the Pahlavi and Manichaean forms), for which he quotes 
Hübschmann 1895: 84. > DMMPP: 154a 

Pres.: IND. 3sg. BMP pl’mwsyt /framosed/, IMPV. 2р1. MMP m’ pr’mwsyyd, ВМР m’ plmwsyt /ma 
framosed/ ‘don’t forget!’; Partic.: pres. BMP pl’mws’n /framosan/, perf. pass. MMP fr’mwst 
*PARTHIAN: fr’mwS- ‘to forget? > DMMPP: 154a 

Pres.: IND. 35р. fr'mwšyd, SUBJ. 2sg. fr’mws’; Partic.: perf. pass. fr’mwst 


*maucl 269 


*KHOTANESE: ? marsyarä (impv. 2р1.) ‘forget’? {hapax} || (+ *fra-a-) hämura- 
‘forgetfulness, forgetting’ = SGS: — 

*SOGDIAN: (+ *fra-a-) ? BSogd. fr’’wyscy, BSogd. Br'wcy, MSogd. fr’wycyh 
‘forgetfulness’ 

*NWIR: (+ *fra-à-) NP firämüstan, Bal. Samust/Samüs- (intr.), šamošt/šamoš- (tr.) ‘to 
forget’ 

*NEIR: (+ *fra-(a-)) Yghn. firomic/S- ‘to forget’ (< NP ?), Yi. formo-/farmísc-, M. 
formiy-/formisk-, Wa. rom(s1)s-/romost ‘to forget’ 

*MISC: (+ *fra-) Огт. š'amot ‘forgetfulness’, Par. nhamur ‘forgetful’ 

*SANSKRIT: mars ‘to forget’ (RV+) = EWAia II: 332 

«PIE *mers- ‘to forget’ = LIV: 440 f. | Pok.: 737 f. 


*IE COGNATES: Lith. uz-mifsti, Toch. märs-, Arm. mofana- ‘to forget’ 
*REFERENCES: IIFL II: 209a, 537a; DKS: 324b f., 477b f.; Werba 1997: 366; Adams 1999: 455 f.; 
Steblin-Kamenskij 1999: 302; Shahbakhsh: s.v. Samus-; Korn 2005: 117, 132, 146 f., 316, 387 


*marZd ‘to have pity, forgive’ 

*AVESTAN: OAv. moroZd- ‘to have pity’ = Liste: 44 

Pres. them.: IMPV. 2р1. OAv. mereZdatà (Y 33.11) 

*MIDDLE PERSIAN: (+ *ā-) MMP "'()mwrz- BMP "mwic- /amurz-/ ‘to forgive, 
absolve’ = DMMPP: 41а 

Pres.: IND. 1sg. BMP /amurzém/, 1р1. BMP /amurzem/, 3pl. MMP "mwrzyynd ‘they show mercy [= 
Sogd. prm’ndy’ kwn’nd]’; Partic.: perf. pass. BMP ’mwlcyt /amurzid/, MMP ’mwrzyd 

*PARTHIAN: (+ *4-) "тууа ‘compassion’ = DMMPP: 40b 

*KHOTANESE: mulysdi- (f.) ‘compassion’ 

*NWIR: Bal. marzit/marz- ‘to absolve, forgive, bless, encourage, support’ || (+ *a-) 
NP amurzidan/amurz- ‘to forgive, absolve’, borrowed into Bal. amurzit/amurz- ‘id.’, 
Qohr. ämerz-, Yzd. amorz- ‘to forgive’ 

*SANSKRIT: тага ‘to take pity, pardon’ (RV+) = EWAia II: 326 f. 

© The Пг. root *marzd has no IE correspondences. On the possible interpretations of 
the peculiar structure of this root see EWAia, l.c. 


*PIE — = LIV: 444 f. | Pok.: 737 f. 
*REFERENCES: Bailey 1936: 338; DKS: 338a f.; Werba 1997: 365; Kümmel 2000: 375; Lecoq 2002: 
641b; Shahbakhsh: s.v. marz!-, amurz- 


*maut! ‘to release, let loose/free’ 

*CHORESMIAN: (+ *uz-) m/zmxs- (intr./inch.) “о (go to) sleep’, m/zmx’sy- (sec.
```


## [2026-09-07T16:19:29.468Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD\nawk 'BEGIN{RS=\"\\f\"} NR>=68 && NR<=72 {print \"===== block\",NR; print}' FFD_pages.txt | head -120"
}
```


### [2026-09-07T16:19:30.679Z] TOOL RESULT

```
===== block 68
[pdf page 68]
ماده‌های ماضی و مضارع فارسی دری سا ۳و۶
شو < فارسی میانه 32 + ایرانی باستان 32-۵*. برای 2 > آرای.
شست.
شست < فارسی میانه 5081 ج ایرانی باستان 3508-1۵*. برای 1۵ -> آراست. 7504
صورت اصلی 3۷8 است. 4 پیش از 1 به 5 بدل شده است. 7504 صورت ضعیف ريشةٌ
40 و آَن به معنی «تحریک کردن» است.
شوی < فارسی میانه 50 < ایرانی باستان 35200-8*. برای 2 آرای. «شور) به جای
اشوی» جدید است > جستن.
شکافت < فارسی میانه 531 < ایرانی باستان ۴2-31-1۵ برای 12 -> آراست. 2
پیشوند فعلی است. 831 صورت بالاندهٌ ریشهٌ قاا است و ۴۵۲ به معنی «شکافتن» است.
شکاف < فارسی میانه 5۶ + ایرانی باستان 2-3۶-۵*. برای 2 -> آرای.
شکست < فارسی میانه 5۵91 < ایرانی باستان ۹16۵۶-12*. برای 18 -> آراست. ‎٩1۵0‏
‏صورت اصلی ۶۵8 است. 4 پیش از ۲ به 8 بدل شده است. ۹24 صورت ضعیف ريشةٌ
4 است.برای‌ضعیف کردن ريشه #حذف شده‌است. 5۵74 به‌معنی «شکستن»است.
شکن < فارسی میانه 5۵7 < ایرانی باستان ۶1۸2-۵*. برای 2 -> آرای.
شکفت < فارسی میانه 5/1
شکف جشکوف ج فارسی میانه 501
شکیفت < ایرانی باستان ۴۶1۵1۲1۵. برای 18 - آراست. ‎٩1۸10‏ صورت اصلی ‎٩۳۵۲‏

===== block 69
[pdf page 69]
جوا را فعلهای فارسی دری
است. این ريشه به معنی «صبر کردنْ» است.

شکیب < فارسی میانه 51650 < ایرانی باستان 8-م۶۵1*. برای ۵ > آرای.

شمردن

شمرد + فارسی میانه 530076 < ایرانی باستان 1-37:۳4۵ط۵*. برای 18 -> آراست.
201 پیشوند فعلی است. ۳7337 صورت اصلی 55 است. ۵ بعد از آبه 5بدل شده است و
#به جای 27 در صورت ضعیف ريشه آمده است. ريشهٌ ۰1337 که صورت دیگرش 11۵7
است و از آن «آمار» آمده» به معنی «شمردن» است.

شمر, شمار < فارسی میانه 0570۱۶ 0337 < ایرانی باستان 1-57037-8ط۵*. برای 2
< آرای. 3۳37 صورت بالاندةٌ ريشةٌ ۸۸۲ است. 580۲ با حذف 4 از ۰5307۵
به‌قیاس با ۷8۵7 و ۷۷270 به‌وجود آمده است.

شناخت + فارسی میانه 5031. به جای 50371 باید 5034 می آمد» از 3۸3-18* ایرانی
باستان. ظاهراً به قیاس با فعلهایی چون ۹32و ‎٩381‏ بوده که 5371 به وجود آمده است.

شناس < فارسی میانه 5039 < ایرانی باستان 3503-6۵*. 58 برای ساختن ماد آغازی
به کار می‌رفته است. ريشهٌ 583*به معنی «شناختن» است.

شنودن :

شنود < فارسی میانه 25084 < ایرانی باستان ۴۹58-12 برای 1۵ > آراست. 7608
صورت ضعیف ريشهةٌ 7573۷ است» به معنی «شنودن».

«(شنید» و «شنفت» صورتهای دیگر «شتود» هستندء هر دو در فارسی دری به وجود
آمده‌اند.

شنو + فارسی میانه 252۷ ه ایرانی باستان 5۵۷-۵*. برای ۸ > آرای.

===== block 70
[pdf page 70]
ماده‌های ماضی و مضارع قارسی دری سس ۶۵
ی یف ۰
شیفت + ایرانی باستان 33۳۵-۲1۵*. برای 1۵ -> آراست. 0ه7537 صورت اصلی
آنه5۷* است. 0 پیش از 1 بدل به آ شده است. ريشهٌ 8۷۵10*به معنی «جنبیدن) است.
شیب < فارسی میانه 580 + ایرانی باستان 35۷/۵10-۵*. برای 2 > آرای.
«شیفته» صفت فاعلی گذشته از «شیفتن» است و در بیت زیر از گرشاسبنامةٌ اسدی
«(مشیب) به معنی («ناراحت مشو) به کار رفته است:
شکیب آور از درد و بر من مشیب که از مهر بسیار بهتر شکیب
فراموشیدن, فرموشیدن
فراموشید. فرموشید + فارسی میانه 1 ماد ماضی جعلی است. از ماده
مضارع ساخته شده است. در فارسی دری «فرامشت» بازماندة 11371۵31 فارسی میانه
است. 1۳30۵1 بازمانده 112-3-7108-1۵* ایرانی باستان است. برای 2 > آراست. 3و 5۵
هر دو پیشوند فعلی هستند. ريشةٌ کار" ظاهراً به معنی «فراموش‌کردن» است.
فراموش, فرموش < فارسی میانه 137۵5 < ایرانی باستان 172۵-3-۳۵5-۵*. برای 2
> آرای. 13۵05 صورت افزودةٌ ریشهٌ 05 است.
فرجامیدن
«فرجامید» مادهٌ ماضی جعلی است. از مادهٌ مضارع ساخته شده است.
فرجام + فارسی میانه 17[300 < ایرانی باستان 370-2[-17۵*. برای ۵ -> آرای. 370[/ظ
صورت بالاندهٌ ريشةٌ 8/[278 است. 8/1270 به معنی «حرکت کردن» است. صورت بالاندةٌ
آن با پیشوند فعلی ۵ به معنی «به پایان‌رساندن» است. در فارسی میانه ماد ماضی :
به صورت 178[31۲ آمده است» از ایرانی باستان 17[348*, با آمدن 31[ به‌جای
«آمدن) و «انجامیدن» هم از 8/۵7 آمده‌اند -> «آمدن) و «انجامیدن).
فرستادن
فرستاد + فارسی میانه 1۲68130 1138110 هر دو ماده ماضی جعلی هستند. از 11

===== block 71
[pdf page 71]
و فعلهای فارسی دری
ماده مضارع.
فرست س فارسی میانه 1۳681 ج ایرانی باستان - ها5زه ۳ *: فرستاده. قاقنه۲؟ صفت
[ مفعولی گذشته است از پیشوند فعلی 8 و هاگٌذ: صفت مفعولی گذشته از فا صورت
ضعیف ريشهٌ قَة: «روانه‌شدن ‏ وکردن» و برای پسوند 2 > آراست.
قرشته از 121512-1۵ آمده است.
فرسودن
فرسودن. فرسای در فارمسی دری بسیط است. اما از نظر تاریخی از پیشوند 2 و
«سودن» و «سای) ساخته شده است + سودن.
فرمودن
فرمود « فارسی میانه 1۳۵7004 + 1۳2۵034 < ایرانی باستان 1۳۵-3-12*. برای 12 -> .
آراست. 178 پیشوند فعلی است. 33 ريشه است به معنی «اندازه گرفتن». 1۳۵/14 به‌قیاس
با فعلهایی چون 8737 و ۹۳84 به وجود آمده است. :
فرمای < فارسی میانه 172۵08 < ایرانی باستان ۴1۳۵-3-8 12 نشانه‌ای برده که
برای ساختن مادهٌ مضارع از ريشه به کار می‌رفته است.
فروختن
فروخت < فارسی میانه 1۳071 < ایرانی باستان 1۵-0-1۵ *. برای ۵ > آراست. ۲۵
پیشوند فعلی است. 1 صورت اصلی 0 است. ۴ پیش از 1 به # بدل شده است. ۷1
صورت ضعیف ۷۷۵و آن به معنی «گفتن» است. ۱
فروش دج فارسی میانه 1۳05 ج 105 «<ایرانی باستان ۲۳۵-۵55 *. ‎٩‏ برای ساختن
ريشةٌ جدید به کار می‌رفته و 1 پیش از 5 به #بدل شده است.
فرهیختن
فرهیخت + فارسی میانه 1۳80451 < فارسی باستان 0۵-1۵ -1۳۵*. < ایرانی باستان

===== block 72
[pdf page 72]
ماده‌های ماضی و مضارع قاری دری سس ۶۷
۴1۳-4۵ برای 1۵ > آراست. 2۵ پیشوند فعلی است. ۹38 صورت اصلی 83 است. 8
پیش از 1به #بدل شده است. ۹88 صورت ضعیف ريشةٌ ۹228 است. «برای ضعیف کردن
ريشه حذف شده است. 5288 به معنی «کشیدن» است.
فرهنج ج فارسی میانه [112822 < فارسی باستان 8-[0۵0 -8۵* < ایرانی باستان
2-[172-8۵2*. برای 2 - آرای. [به جای 8 آمده است. + آهختن.
«آهنگ» و «فرهنگ» هم از ريشةٌ 988 گرفته شده‌اندء به شرح زبر:
آهنگ + فارسی میانه 30228 < فارسی باستان 0208-8 -3* < ایرانی باستان
۶3-8288-2. 3 پیشوند و 2 پسوند است.
فرهنگ < فارسی میانه 13022 < فارسی باستان 0۵88-8 -8۸* < ایرانی باستان
```


## [2026-09-07T16:19:49.805Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"vergessen\\|Vergessen\" BRT.txt | head -20"
}
```


### [2026-09-07T16:19:49.849Z] TOOL RESULT

```
9062:mit  lii,  niy  'eingraben,  verscharren':  yö iiars  .,  irtri'iusS  zumc  kshrpa  nikaiiiti  V. j.  40  PüZ.;  —  altafia  ..  aSta  vastra  fraca k3r3ntm  niia  kanaym  V.  7.  12;  —  yat aialta  zimS  nikante  (3SPM.)  späiias^a  .  . ttimskante  (sd.)  V.J.  36;  8;—  jarW  (sd,) .  .  zjme  nikante  (NDf.)  V.  7.  47;  j. ra.  a)  II  'vergraben'  sva.  'aus  der  Er- innerung verschwinden  machen,  in  Ver- gessenheit bringen':  uta  lyt/'  kunavahy ava''faiy  a''ura''mazdä  nika''tuv  "und  was du  tust,  das  soll  dir  AHM.  in  Vergessen- heit bringen"  Bh.  4.  1 7  ''.
18419:—  Pü.!//b/4)  kartär  i  nfwaiih,  (lu  A);  ßüiA) mänst.  —  ')  Hds.  ßaSüiö.m'.  —  >)  NeubÜ- dang  zum  NS.  ßHSiisüimq%r»,  als  die  eig.  Be- deutung vergessen  war.  —  3)  NA.  'itjtufira.
20100:Abieil.  —  marsa<van-  eig,  'das  Vergessen  be- wirkend';    %.     GDN.     KZ.     2$.     405;     »gl-     "■     •^'"^^
20101:marfa-  Adj.  'schwer  lu  vergessen',  np.  farä- mSi  'ver^.isend'  (s.  dazu  IF.  4.  130).  —  Pü.: sH  i  nihän  nrmän ;  vgl.  zu  marsoi/na-  und  HaIIC SBayrAW.  1S6S  II.  25,  DST.  ZA.  a.  241.  - ')  Die  SPreussAW.  ig.  423  vorgeschlagene Fassung  halte  ich  oichl  ^r  richtig.
24096:niA,  (inV.  5J):  afi  iudakiittii.  —  »Statt •iya,  S  j6S.  31,  —  ')  Hds.  vüdim;  Pö.:  o. Blocket  Lex.  144  verweist  unlei  viidim  auf iioiiya-;  das  ist  aber  vergessen.  VgL  iSt.  Y. 5*-  4-
```


## [2026-09-07T16:19:54.956Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '20085,20110p' BRT.txt\necho \"=== leaf\"\nawk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"marfa-  Adj.\")>0) print \"leaf(1-based)=\"n}' BRT.txt"
}
```


### [2026-09-07T16:19:56.205Z] TOOL RESULT

```
dby  Google
"53
:i54
. .  frampr^öii  V.$.  4a.  3)  '(einen  Ver- trj^  aufheben':  vaii.,mi^r3m  kirmaoiti *zastS.mat5 .  .framinzaUi . .  antar^  urvaitya (sA.)  frada^aifi  V.4.3;  sf.*.  4)  'fgrt-
fliegen':  dz'a  ämarvtsn  dva  vJmamin  äva framanssn  (statt  Du.)  "die  zwei  (Federn) sollen  auf,  , .  hin  und  her, . .  fortfliegen" Yt.  14.  4S-
mit  nj\  s.  Inf.
mit  vi  hin  und  herfliegen':  dva  ämars- zm  .  .  vlinartan  . ,  framanzin  (sd.)  Yt, '4- 45-,
a\.  marfli,  m^Jinü,  ni-mfTijyät\  Cip.  mälidan 'reiben',  woss.  märsin  '(egen'.  —  Vgl.  miriiää-. —  Pü.  (mit/z-a): /™/  mätUan,  (mit  alfä):  afar ..  däi  d^är  ('Mauer');  Npü.  {lu  Yt.  14.  45): mälii  äiäa»,  [in  YL  14.  21):  dar  man.  — ')  Nur  im  Inf.
•  j.  maraza-  m.  'Mark,  Grenzgebiet*: anusi^  plrftn  "z^m  avahistäl  "zwangs- weise soll  er  sich  in  das  äusserste  Grenz- gebiet" begeben"  V.  ^.  5^1.
mp.,  np.  man.  —  Pu. :  a^arsandihä  fa  an /röltiim  mars  äff  tslind;  Erl.  undeutlich.  — ■)  Wo  ei  wegen  der  anruhigen  Nachbuschaft Km  gefährlichsten  isl.
j.  marixämyeke  Yt.  /j.    126  !ie»  mim'.
■  j.  maräaona-  Adj.  'mit  (dem  Dana) Mariavan  in  Verbindung  stehend,  von ihm  henlihrend':  ihye/O  'tarn  V.i^.i,  i, 43;  —  ihyejaKkS  'nahe  yt6.4;  13.  130.
Ableit.  aus  martavan-.  —  PO. :  sei  i  iiikäi,  ratvan, Npü.:  marg i »Ulan  äyanda.  So.:  mftyiir gvfla-
•  j.  maräavan-  m.  Name  eines  Dafva*^: k:j  atti  i^yejä  'saonS  "welches  sind  die Gefahren  (von  Seiten)  des  M.V  V.  iS.  8  '>.
»)  Der  den  Abfall  vom  rechten  Glauben  be- wirkt; vgl.  V.  iS.  9  und  und  unten  iEL
Abieil.  —  marsa<van-  eig,  'das  Vergessen  be- wirkend';    %.     GDN.     KZ.     2$.     405;     »gl-     "■     •^'"^^
marfa-  Adj.  'schwer  lu  vergessen',  np.  farä- mSi  'ver^.isend'  (s.  dazu  IF.  4.  130).  —  Pü.: sH  i  nihän  nrmän ;  vgl.  zu  marsoi/na-  und  HaIIC SBayrAW.  1S6S  II.  25,  DST.  ZA.  a.  241.  - ')  Die  SPreussAW.  ig.  423  vorgeschlagene Fassung  halte  ich  oichl  ^r  richtig.
•  j.mariö.kara- Adj.  — ?— 'h  v»rihrayn»m ..arsö.karym  'nm  frals.kar?m  Yt.  1^.28.
Npü. ;  htmär  ktinanda.  —  ')  Erklärungsvercuch bei  Gdn.  jYt.  74  ('versöh Blich'),  Dst.  ZA  2. 568  ('qui  fait  mouiir').
•  j,  maräü-  f  'Bauch,  Wanst*  uzw.  daiv- ischcr  Wesen'':  nätrya  va  pu%rahe  vS Aaoyä  vä  *hty&  (GS.)*>  "für  des  Weibes
oder  Sohnes  oder  für  den  eignen  Wanst" Y.  u.  u
i  ans  ar.  xs,  vgl.  mirttänn:  —  Pü.:  mulän, Sü. ;  duf/odaram,  —  i)  Im  GegensBti  zu  h™- %war:  ~   ')  Vgl.  iFlex.  Bthl,  IF.  p.  276.
•  j.  marzdilca-:  s.  unter  m?r?zdika: Ableit.
•  j.  marf  dika'vant-  Adj,  'erbarmungsvoll, barmherzig*:  hadiiasca  (sd.)  . .  -vatö  Vr.
P-S-,
AbleiL  —  Pü. :  ämurasnämand.
=== leaf
leaf(1-based)=641
```


## [2026-09-07T16:20:04.330Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==640 || NR==641 || NR==642 {print \"--- leaf\",NR; print substr($0,1,200)}' BRT.txt"
}
```


### [2026-09-07T16:20:05.614Z] TOOL RESULT

```
--- leaf 640
üj/a-'EXf. — Zum  V.  'mar-;  %  2/2.  —  Vgl.  marila-,  — (Ü.  ntär^a-  m.  —  Pü. :  martum.  —  i)  Vgl. Var.  —  ")  Wo  'lihyä  statt  't^ahyä  getcbrieben ist  —  3)  KoU.  
--- leaf 641
m.  AGr.  /.  476,  IFAnz.  10.  23;  dara noch  Wn.  AiGr.  /.  277.  —  >)  Gegen  den  An- sati  eines  fem.  "vt-  sprechen  die  Epitheta.— ')  VgL  mp.  ier  unter  baoiryo:
•  j.  maraz- 
--- leaf 642
130;  —  °W  (statt GSf.)  va  afs  'sS  vS  äa/afl&(sd.)  Yt.  i/. 4;  —  andvT  . .  'sH  (GS.)''  xtayete  (sd.) xfarpnaahd  ydha  .  .  Yt  5. 96.
Ableit  —  mp.  (Pü.)  masi  gr.  vgl.
```


## [2026-09-07T16:20:11.604Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==94 || NR==95' HUB.txt | head -70"
}
```


### [2026-09-07T16:20:13.278Z] TOOL RESULT

```
— 83 —
noch nfther stehen wtirde als die KZ. 27, 107—108
besprochenen Zendfonnen, die zu einer arischen Wurzel
ksvib Oder kSvibh geh5ren.
801. Dazu arm. asxSt Vothbraun* (vom Pferd), phi. sBtvars
'rothhaarig Bdh. Gl. 192, kurd. SS Tuchs* (Pferd)
Socin, kurd. Samnil. II, 317, si 'alezan', hespisi 'un
cheval alezan* Justi-Jaba Diet.
803. Zd. xsa^rya- ist im Neup. durch sahn vertreten.
Also Ser 'L5we' davon zu trennen.
804. Phi. SSpOk (Jasna 61, 11) = ap.*ariaipa- oder *xsvaipa-?
Vgl. oben Nr. 800.
805. Arm. gund 'Abtheilung eines Heeres, Corps, Schar'
(bei den S^ltesten Schriftstellern) = arab. /wwd, pi.
junud^ ajndd 'Soldaten*, syr. guddd *Schar', mand. gunda
(N5ldeke, Mand. Gr. 78), phi. gund weisen in ihrer
Uebereinstimmung auf urspr. anl. g, nicht v, Im
Armen. findet sich g = pers. g aus v erst bei Schrift-
stellern des 7. Jhd., wahrend gund (mit g) im 5. Jhd.
belegt und vor diesem entlehnt ist. Daher Zusammen-
hang mit skr. vpida- oder zd. vq^toa- unwahrsehein-
lich.
806. Die Zusammenstellung widerspricht alien Lautgesetzen.
808. Lies ap. Vindafamd (im Nominativ, Thema Vinda-
famah-), Np. farrux gliicklich' = phi. farraxv setze
ich = ap. *fama(h)uvan' (mit Suffix van fiir ursp. vant),
vgl. WZKM. 7, 377 ; np. farxunda glUcklich' = phi.
*farraxvand'ak = ap. *farna{h)uvanta' aus *farnah-
vant?^) Die Nebenform farrah (von farr) geht nicht
auf ein phi. *farnak, sondern, wie np. farrihl *Herr-
liehkeit* zeigt, auf ein phi. ^farreh (vgl. syr. B^l^niB
Farrahanns N. pr. bei Hoffmann, Ausziige p. 72) =
ap.*/arwaAa- (oder ein ahnlich erweitertes farnah-) zu-
riiek, vgl. np. xurrah = paz. x^areh Min. Gl. {x^arehe
Shk. 255) = zd. x^arenaflha- (oder ein sLhnlich er-
weitertes x^arenailh').
*) YgL zd. ac^arenahha nom. sg., afarenafihvanta instr. sg.,
x'arenanhuniem = x^arenahhentem ace. sg.
6*
— 84 —
809. Np. fara = skr. prak Vorn, vor etc.
810. ^"p. farax = phi. /r^au, geschrieben fraxv scheint ein
ap. *fra(k)uva" vorauszusetzen. Ebenso Fr. Miiller,
WZKM. 7, 378.
812. Zu der vorgeschlagenen Etym. passt das o von phi.
psiz. framos, farmos (Min. 61. 75, Shk. 244), np. fara-
moS nicht. Doch ware np. faramnst = skr. ^pramrsta-,
*pramrsti-. Dames hat nh, sa-musay^ sa^musay (mitw,
u) *to forget'.
813. Gegensatz von zd. frapi^wa- gut genahrt, gedeihend'
= np. farbih pinguis, robustus, florens, copiosus' ist
zd. tardpt&wa- vd. 13, 20 = *sehleeht genS-hrt*. Np.
farbt JRAS. 1894, p. 477 = phi. frapfh = zd. *fra-
p^d^wa-? Zur jiid. pers. Form vgl. paz. pad = phi.
pit ^fat' Shk. 261.
Nach 816 ware nach Salemann np. farasp = phi. frasp
(Gl. and Ind. 98) = zd. fraspaU zu erwahnen. Die
Bedeutung des letzteren ist nicht sicher, Darmesteter
vermuthet *Teppich\
818. 6r. 6 naQaadyyriq; arm. LW. hrasax.
819. Lies zd. ^frasta- = ar. *pra8th'ta-f vgl. die Nach-
trage bei Horn p. 259. Dazu stimmt freilich der Vokal
von np. ftriMta 'Bote* nicht, der durch paz. frista =
phi. fnstak oder frestak *Bote' (Shk. 245) alt bezeugt
wird. Hat Anlehnung .an firista, alter fireSta JRAS.
1894, 478 'Bote, Engel' = phi. /rgs^afe = ap. */raisf a-
stattgefunden ?
Hier nach Salemann np. faryand res sordida,
turpis, foetens' zu erwahnen ^= zd. fra + gainti-.
820. Lies ap. framdnO-.
```


## [2026-09-07T16:20:27.326Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" BQT_v2_pages.txt; grep -n \"\\[pdf page\" BQT_v2_pages.txt | head -3\necho \"=== search خاموش\"\ngrep -n \"خاموش\" BQT_v2_pages.txt | head -20"
}
```


### [2026-09-07T16:20:27.402Z] TOOL RESULT

```
41071
=== search خاموش
9586:     ‫اسم فعل بمعتی خاموش بای ‪ ۱‬ساکت شو‪(« :‬روباه) گفت‬
9592:                              ‫خاموش ‪ ۱‬که اکر حودان بفرض کوبند ( روباه) شتر است وکر‬
9594:                        ‫‪:‬‬   ‫از ‪ :‬خاموش ‪ +‬ی (مصدری)؛ سکوت ‪ .‬دم فروستن‬                  ‫‪ ۶‬خامو کی‬
9596:               ‫بوقت کفتن گوفتن بوقت خاموشی‪.‬‬                   ‫دوچیز طیره عقل است دم فروبستن‬
10055:‫گویند وبمعنی گلوفشردن‌وخفه کردن وخفه‪- ۴‬‬                                                 ‫یمنی خاموش بش ودم نزن ‪.‬‬
13354:‫اول و تشدید انی» در عسربی شراب فروش را‬                  ‫وعمارت رانیز گفته‌اند ‪ -‬وبمعنی‌خاموش وخاموش‬
13662:‫وجراغ‌خاموش کشته وامثال آن برآبدخصوسا‪- ۸‬‬               ‫کنابه ازءمود صبح‌است‬          ‫سدم‬     ‫حنحر‬
19812:                                                                                              ‫کتابه از خاموشی است ‪.‬‬
20061:‫مدمه = بفتح اول بر وزن زمزمه »‬                                     ‫دم تسلیم عیکسرثالی» کنابه‌ازخاموشی‬
27362:‫خموش وخاموش هآمده است ؛ وبروزن‌خاموش‬
27414:                                                      ‫خاموش » بمعنی‬                      ‫راو وس‬
27479: ‫ربان ران = با رای فرشت بر وزن‬                     ‫خاموش کردن صدعی است بدلابل و جوابیکه‬
27486: ‫تندن ‪ -‬کنابه از خاموش‬
27499:                                                    ‫ربان لست = کنابه از خاموش شدن‬
33875:  ‫گنر‪:‬کسی باتوستهد بخاموشی آن‬     ‫س‪#‬تهیدن ‪ -‬بکسر اول و دوم »رك ‪:‬‬
33877:                                    ‫ستهنده رابنشان وجواب احمقان خاموشی دان‪« ».‬فابوسنامه ‪.>۲۷‬‬
```


## [2026-09-07T16:20:31.985Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pdf page\" BQT_v2_pages.txt | head -3\necho \"--- form feeds:\"\nawk 'BEGIN{RS=\"\\f\"} END{print NR\" leaves\"}' BQT_v2_pages.txt\necho \"--- leaf containing line 9586\"\nawk 'NR<=9586' BQT_v2_pages.txt | tr -cd '\\f' | wc -c"
}
```


### [2026-09-07T16:20:34.257Z] TOOL RESULT

```
--- form feeds:
683 leaves
--- leaf containing line 9586
164
```


## [2026-09-07T16:20:40.399Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==165' BQT_v2_pages.txt"
}
```


### [2026-09-07T16:20:41.743Z] TOOL RESULT

```
        ‫ل‬                                                                                             ‫خامالیون‬

‫د با هیم تحتانی کشبده‬           ‫خامامیلره‬
                                                            ‫میونانی دوابی‌است کهآ تراماذربون کویند » وآن‬
 ‫ولام کور بنون زده » بیونالی گیاهی است که‬                   ‫دوقسم است ‪ :‬ساه ومقید » سیاه انرا خامالاون‬
     ‫آنرا بابوته گویند ‪.‬گرم و خشك اعت دارو‬                  ‫مالی ‪ ۱‬کویند و بعربی قانل‌النمر وخانق‌النمر‬
    ‫و بعربیفاالحارض خوانند ‪ .‬بویدن‌آن خواب‬              ‫خوانند ؛ چه هرگاه بلنگه و بوز آررا بخور ند‬
                                             ‫آورد ‪.‬‬         ‫میر تدوسفد آ لراخامالاونل قس ‪ ۳‬کونند؛‬
                                                                                                  ‫البته ب‬

    ‫‪۲‬انون‌تحتالی رسیده‬
                     ‫خاما یطی سب‬                            ‫وخی گونند‪ .‬ستفه‌ضری‌است* ‪ -‬وبعضی دیگی‬
‫»‬    ‫بی فقطهُ ساکن‬    ‫من‬    ‫و‬   ‫مکور‬   ‫حطی‬   ‫طای‬   ‫و‬
                                                                                          ‫گفتها ند خامالاون‌نوعی‬
‫ببوناتی حششی باشد (‪]:)۳‬نراکای است بنفش‬
                                                                                          ‫از سوسمار است که‬
‫رن که شیرازبان ترا ماش‌دارو خوانند‪ .‬برقاترا‬
                                                                                          ‫آرا بریالی حربا‬
       ‫همگفته‌اند‪۶3 .‬‬   ‫دارد و آلرا کمافطوسی‬    ‫صود‬
                                                                                           ‫کوند گووشتاوسم‬
      ‫شنت‬
        ‫قتحرشی‬
             ‫دکرالث وف‬
                     ‫خامثه ب‬                                                              ‫قانل است ‪ .‬اکرفدری‬
‫دوایی است که آنرا شیتره گوبند ‪ ۷‬و عربان‬                                                    ‫از آن بخورد کی‬
                                                                                    ‫دهند در حال بمیرد‬
                                       ‫‪۰‬‬   ‫درجة وم‬
                                                                            ‫ویعریی اندالارش خوانند ‪. ۴‬‬
‫کنابه از محو کردن‬           ‫‪۰‬‬   ‫خام کر دن‬
                                                            ‫خاما لبون ‪ = ۴‬بکرلام وتستانی بواه‬
                            ‫وبرطرف نمودن باشد‪#.‬‬
                                                            ‫کشیده وینون زده » بلغت بونانی مازربون سیاه‬
‫حامه = بروزن نامه » قلم را گویند‬                            ‫است و آن دوایی است (‪ )۱‬که بر برض و هق‬
‫را‬          ‫دره‬
              ‫توو ه‬
                  ‫که بدان چیزی نوسند ‪۸‬‬
                     ‫)‪ ۳‬خم ‪ : ۳‬است‬                 ‫)‪ (۲‬خم‪ :۳‬است‬              ‫‪.‬‬       ‫‪:‬د‬
                                                                                      ‫(‪ )۱‬خبم‪۳‬اش‬

     ‫(فر)‬      ‫‪۵۶‬‬               ‫‪ ۳‬وی‬           ‫(فر) «لك ‪ ۲‬صە› ‪.‬‬          ‫‪0061672 ۲10‬‬
                                                                                   ‫‪< ۱‬‬
      ‫رك‪ :‬ح‪ ۸‬صفحة پیش‪ - ® .‬بونانی ‪00160۳120121‬‬                 ‫رك ‪ :‬خامالا‪f .‬‏‬   ‫‪-‬‬    ‫‪۴‬‬      ‫م›>‪.‬‬     ‫« لك ‪٣‬ص‏‬

     ‫‪ - ۱‬بونانی کلااا‪« 20۳21‬اختینگاس»‬                   ‫‪.‬‬      ‫«اشتینکاس» = ‪« 61110100۳26‬لك »س‬
                                                       ‫‪ « Lepidium‬لك ‪۲‬س ‪. ۷‬‬                    ‫‪۷‬‏ =‬
            ‫بمدح خواجة ختلان بجشنها خامه‪.‬‬              ‫هب برادران منازین سپس سیه مکنید‬
      ‫منحك ترمذی‪ « .‬لغت‌فری ‪۳۱6‬‬
                                             ‫‪#‬امش ‪ -‬بضمسوم » مخفف خاموی («‪.‬م‪. ).‬‬
                                                                               ‫خ‬
     ‫‪#‬امو ش‪ -‬سان‌کربت_ ‪( 2 5۲۵۵۳۳‬تحمل صبر کردن ) «(ا)سفا ‪‎ : ۱‬ص ‪> ٩۷‬‬
                                                                   ‫خ‬
     ‫اسم فعل بمعتی خاموش بای ‪ ۱‬ساکت شو‪(« :‬روباه) گفت‬
                                                   ‫گنگف_ منطةی‪-‬منقطع ‪-‬‬                        ‫‪ ¢‬می‌زبان‬   ‫ساکت‬

     ‫تخلیص من‬        ‫غم‬
                      ‫رراآيم‬
                           ‫کفتا‬
                              ‫خاموش ‪ ۱‬که اکر حودان بفرض کوبند ( روباه) شتر است وکر‬
                                                                        ‫باشد (دارد(ن ل‪)).‬؟ ک«لتان‪.»۹۳‬‬
                        ‫‪:‬‬   ‫از ‪ :‬خاموش ‪ +‬ی (مصدری)؛ سکوت ‪ .‬دم فروستن‬                  ‫‪ ۶‬خامو کی‬

               ‫بوقت کفتن گوفتن بوقت خاموشی‪.‬‬                   ‫دوچیز طیره عقل است دم فروبستن‬
      ‫«کلتان‪.»۹‬‬
```


## [2026-09-07T16:20:52.034Z] TOOL CALL #28: Bash

```json
{
 "command": "sed -n 1,60p tools/ref_page.py"
}
```


### [2026-09-07T16:20:52.070Z] TOOL RESULT

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


## [2026-09-07T16:20:55.626Z] TOOL CALL #29: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nprint(json.dumps(d['BQT'].get('scans'),ensure_ascii=False,indent=1)[:2000])\n\""
}
```


### [2026-09-07T16:20:57.044Z] TOOL RESULT

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


## [2026-09-07T16:21:12.569Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} END{print \"v1 leaves:\",NR}' BQT_v1_pages.txt\necho \"--- persian digits search in leaves 160-170 of v2\"\nawk 'BEGIN{RS=\"\\f\"} NR>=160 && NR<=170 {printf \"leaf %d: \",NR; print substr($0,1,80)}' BQT_v2_pages.txt"
}
```


### [2026-09-07T16:21:13.794Z] TOOL RESULT

```
v1 leaves: 777
--- persian digits search in leaves 160-170 of v2
leaf 160:   ‫خاکبیز‬                                                            
leaf 161:     ‫پا‬     ‫‪۵‬‬




‫‪۰‬‬   ‫با ذال نقطه �
leaf 162:                                                                                 
leaf 163:     ‫‪۷۰۵ -‬‬                                                        
leaf 164:                                                                                 
leaf 165:         ‫ل‬                                                                
leaf 166: ‫خاهاء بلا‬                                                         
leaf 167:      ‫ا =‬   ‫=ړ‬
                                                    
leaf 168:  ‫اور‬                                                                   
leaf 169:         ‫ا‬
‫خرو داروست وآترا خو لنجان هم میگو
leaf 170:  ‫خابه نهادن‬
```


## [2026-09-07T16:21:24.240Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==164 {print}' BQT_v2_pages.txt | grep -n \"۷۰\\|٠٧\" | head\nawk 'BEGIN{RS=\"\\f\"} NR==166 {print}' BQT_v2_pages.txt | grep -n \"۷۰\" | head\necho \"--- any 706/708\"\nawk 'BEGIN{RS=\"\\f\"} NR>=162 && NR<=168 {printf \"leaf %d: \",NR; n=0; while (match($0,/[۰-۹]{3}/)) {print substr($0,RSTART,RLENGTH); $0=substr($0,RSTART+RLENGTH); n++; if(n>6) break}; print \"\"}' BQT_v2_pages.txt"
}
```


### [2026-09-07T16:21:25.502Z] TOOL RESULT

```
60:   ‫« مثنوی چاپ ‪ ۷۰۳۱‬قمری ص‪٤ ۲۱‬ی‏ ‪.۱۱‬‬
--- any 706/708
leaf 162: ش�
ع�
ز�
ر�
ر�
ز�
ش�

leaf 163: ۷�
�۵
ش�
ر�
س�
ر�
ش�

leaf 164: پ�
ذ�
ذ�
ط�
ر�
غ�
ر�

leaf 165: ش�
ر�
س�
ر�
ذ�
ز�
س�

leaf 166: س�
ر�
ر�
ر�
ر�
ع�
»�

leaf 167: ش�
ر�
ز�
س�
ر�
ر�
ز�

leaf 168: ع�
ط�
ع�
ط�
ز�
ر�
ص�
```


## [2026-09-07T16:21:30.743Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\npython3 -c \"\nimport json,os\nm=json.load(open('BQT_v3_pagemap.json'))['map']\nfor p in ['1448','1447','1449','1211','1990']:\n    print(p, m.get(p))\n\""
}
```


### [2026-09-07T16:21:31.998Z] TOOL RESULT

```
1448 241
1447 240
1449 242
1211 2
1990 None
```


## [2026-09-07T16:21:36.121Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 241\\]/{print}' BQT_v3_pages.txt | head -80"
}
```


### [2026-09-07T16:21:37.561Z] TOOL RESULT

```
[pdf page 241]
ay
‏اول وسکون آخ رکه کاف‎ ails
‏بلشد » بمعنی پشت است که در مقابل رو است‎

و جربی ظهر خوانند - و در بعضی حیز ومخنث
را کفته‌اند - وپلید و پلشت (۱) و زبون را ح‌

میگویند .

‎SUS‏ ۱ - بح اول و ‎GE‏ بر وزن
فلاخن » جوی لو ‎AI‏ عمیق راکونندکه دران
علزه ‎OT‏ جاری وروان شده باشد - و جوی بلند
را نیز کوبند همچو جوییکه درک کوه وامثال
‎ASOT‏ باشند - و بمعنی بلند هم آمده‌است که
تقیض پست باشد .

‏قراهرد ۴ - بنتح ‎Dey Jol‏ نام
پس رستم بن زال است 5

‏فررامش ۴ = ‎Soi‏ وضم‌میم.مخفف

‎. ‏پشت‎ se )۱(
. ‏بوزن‎ : the )۳(

‎. ‏سفرکن سافرکند (هم)‎ ٩

‎. * ‏«بوستی. نام نامه‌س*۹ستون۲‎ (gate) ‏بمعنیآمرزندة‎ Wd

‏۴ - فراموش(ه.م.) > فرامش.

‎: ‏چك‎ (x)

‏66 اس

‎Gols‏ است که از اد رفتن و ازخاطرمحوشدن
باشد .

‏فر امشت = بقتح اول وثالی‌بالف کشیده
و میم مضموم ‎pte‏ و نای قرشت زده ؛ بمعنی
فراموش است که ازباد رفتن باشد سوآنچه کسی
در دست گیرد هم فرامشت خوانند.2 *

‎dice = VOUS‏ ودون‌وسکون‌جيم,
بمعنی‌کابوی است و ‎OT‏ منگینیی پاش دکه‌درخواب
برمردم افتد .

‎SOUS‏ - با نون بروزن ‎Sls‏ , تام‌مادر
فربدون است ۷ ۰

‏فر اوار ‎A‏ = با واو بروزن ‎allyl?)‏
‎LEN,‏ تابتانی راگویند ؛ و باین معنی بحذف
الف هم‌آمده است که فروار باشد .*#

‏و شم مي ‎a‏

‏- از: فر ( پیتاوند بمعنی پیش )۳ آمرز.
۴ - مشفف*«فراموش»(«م.) .
- از: فرا (پیشوند) +-مشت. ۷ رل: فدرنجك,

‏درفنجك « برفنجك. ۷ - فرانك بناگاه بد در جهان ( نهآ گاه بد زين نهان . دهشدا )
که‌فرزند او شاه بد برجهان. فردوسی‌طوسی ‎A‏ فری ۳۰۹ .

‎Banga A‏ فرباله _ پروار (هم.).
‎o‏ فراموش - بفتح اول فرامشت ‏ فراش ( مخقف ) ۰ فراموشدن ( وس‌ررامن)

‏پهلوی ‎framésb_‏ ( از 2 بردن ) , پازند - ‎woe , farmdsh‏ باستان ۳0875-4۳8
6 ( فراموش کردن (. پلوچی ‎_.Shaméshag . shamushag‏
0280 ر11ع5]12-۳1091:8 > استق_هوبشمان» ۸۱». فرامشت](2۳810118] = ‎co Sot‏
‎pramrshti - , ۰ pramrshta _‏ © > هوبشمان ۸۱۲ > ‎OF ps‏ پس از ذکروجوه اشتقاق
هرن وهوبشمانگوید : فرامش پهلوی باید از _ ‎framush‏ ۵ از - ‎framursb‏ © تاشی ‎ous‏
‏باشد و ‎omurshta_‏ از ‎musht_‏ - مأخون است « نب که ص ۷۲ ‎٩‏ ؛ ازباد رفته .ازخاطر
محوشدء +$ اموش کردن » ‎abil‏ بردن: « دوستان صمیمازکلمةٌ حق خاموش شدند وصحبت
دیرین فراموش کردند. » » کلستان ۳۸ * .

‏© فراوای - بفتح‌اول . اوستا ‎fravdn(g)p?‏ ( افزونی « بیار ), کردی ‎ferawin‏
‏( نهار » غذای ظهر ) « ژابا س ۰ ؛ بسیار » وافر » کثبر : « ملك زاده‌ای گنج فراوان از
پدر میرات بافت. » «کلتان 4۰ » .
```


## [2026-09-07T16:22:05.588Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=200 && NR<=230 {printf \"leaf %d | \",NR; print substr($0,1,60)}' BQT_v1_pages.txt"
}
```


### [2026-09-07T16:22:06.839Z] TOOL RESULT

```
leaf 200 | لح گ دستور ز بان پاررسی
و «زربخشی�
leaf 201 | در
فرو
معانی حروف و کلمات: خداو ند
leaf 202 | 0 دسئور زبان پارسی
و کلفادر. که هع�
leaf 203 | مقدار محافنظت اتصاف
رنگ
حاصل مصد�
leaf 204 | له ۱ قواعد دستور واملاء پارسی
فاد
leaf 205 | دیباچذ مز ف لح
«بیارا» و میم نهی «
leaf 206 | لط قواعد دستورواهلع پارسی
وبی تش�
leaf 207 | دیباچة مو اب ۳
«مردمان » و * اسبان 
leaf 208 | 
leaf 209 | 
leaf 210 | ۱ بروزن جاء امر بآآمدن باشد (۱)
یع�
leaf 211 | اشارتمت بر ضی‌کامل و عقل کل » و ا�
leaf 212 | ۳
است از سال هی » و آن بودن خورشید 
leaf 213 | آي ول
آب لح » بکرناك ؛ خراب انگوری
leaf 214 | آت خوست « بر وزن ارت ۰
مکی دج ماه ک
leaf 215 | آب ست
آب دست ب بر وژن‌خاربست , امس
leaf 216 | ساختن ناشد .
" .ریز - بر وزن خاه ریز 
leaf 217 | " ]یست - بنتح ثاك و سکون رابم
و فوقا
leaf 218 | "آب سیه « یکی اك , مخخف آب
سیاء انت 
leaf 219 | آب صفت بودن - کنابه از یار
بفم و فا
leaf 220 | ات
آآب کبوث- بکس ات ؛ دربای‌چین
ر�
leaf 221 | نواحی باشند از دنبال شخصي که آب م�
leaf 222 | 0
آش
تلم رودخانه ایست که آنرا رودخ
leaf 223 | ۱ آخن آب پرود ۱ ۱ اه
کیره راگونند �
leaf 224 | وا ثِ آ دامن
وکاف ۰ بمننی آش زده ا�
leaf 225 | آش محقان
۰ ۲ تش ذهقان ه بکر رابم » 
leaf 226 | و مطیخی و آهنگر و امثال آنرایز کو�
leaf 227 | کویند . ۱ 1
| تین پنجه - بتح بای فارس
leaf 228 | عمل کردن ویبروی تىودن ناحکام شرم�
leaf 229 | که در آن حاسلی ونفعی لبوده باشد ٩�
leaf 230 | ] خشیگه ه با کان فارسی » بی وزن
ومع
```


## [2026-09-07T16:22:10.868Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=396 && NR<=402 {printf \"===== leaf %d\\n\",NR; print substr($0,1,400)}' BQT_v1_pages.txt"
}
```


### [2026-09-07T16:22:12.148Z] TOOL RESULT

```
===== leaf 396
یاف
چنکالی ومالیده 3۳ وان یش کی
با روغن وشیرینی بهم‌بمالند .
انگشتو) ۰ بکس الك و داد بالف
کشیده . نی باشد که آنرا برروی آعل زغال
وغیره بز ند.
انگشته - بنم الث بر وزن خریشته ؛
۳ باشد ازچوب مانشد ینجه دست ودسته یز
دارد که پرزیگرا
===== leaf 397
انگوز زیتونی . .
وبعربی اصابع‌المذاری گوبند .
) نگوژه؟ - با زای فارسی بر وزن
سنبوصه ؛ صمغ درخت انکدان باشد و به_بی
حلثیت و صمن‌المحروث خوانند . و تخم آنرا
بذرالانجره وقریض کویند .
که کوی کربان وتکمة کلامرا اژآن‌بگذرانند -
اس�
===== leaf 398
نوهیان - بکرم بروزن‌مجوسیان.
لاله باشد » و درصحاحالادوبه بهمین ححنی‌باسقاط
نون آخر آورده‌استو گفنهاست که‌این لفت‌روهی
است واه اعلم ..
) و لیفن(۱) » بروزن‌بولیدن » بسعنی
ناله و زاری و نوحه کردن باشد .
انهو با س با های هوز و
===== leaf 399
کوبند که بدشواری از انا شود و حل
9
| ثیشه - بر‌رزن‌همینه .جاسوی‌وچاپلوی
هر چیز بسته و منجمد بأشدچه درفارسی‌سینوشن
تب ۱۵۰ ,
0 زمین ۰ ء ظرفی باشد ازسنال
مانند مو وخمچأیزگی که دوغ وا جر آ ‌کنند
او * نم اول : و سکونِ نافی » ۳
۳ 0 ه�
===== leaf 400
رل اس
یفکن - و بشم اول ناله و زاربراگویند . *
او باریدن ۱ - بنتح اول بروزن سر
خاریدن ؛ ناجاویده فرو بردن را گویشد و بعری
پلع خوانند ‏ و بمعنی افگندن هم هست-ویضم
اول بممتی ناله و زاری کردن باشد .
5 ۱ ۳۹
او باش ‏ بر وزن افراش » مردم
===== leaf 401
واجب و بفستا وا گیبتد و جر هی اهنت »
و آن‌قدارست ازسرانگشت ,کوچك ۷ مرانگشت
بزر که دست آدمی ۰
اوذست » بروژن بدست » بمعنی‌آودی
اس ت که وجب و بدست وشبر باشد .
و مدشه‌ایست .
ذاز شلمدار وسکون رای بی‌شطه ؛ بات بونانی ۷
آب را گویشد 
===== leaf 402
ای ۸ اه
نیز خواشد ره ۳
اورمز ۱ نم اول و میم و سکون
وین ثالث و زای قطمدار . دام متارة
ی باشد - و فام روز اول است از هر صله
نيك است در این روز نو پوشیدن‌وسفر
کردن" و مهر بر کاغذ نهادن » و بد است قرض
و وام دادن - و نام فرشته ایست که تد
```


## [2026-09-07T16:22:21.745Z] TOOL CALL #36: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in BQT_v1_pages.txt BQT_v2_pages.txt incoming/BQT/BQT_v3_pages.txt incoming/BQT/BQT_v4_pages.txt incoming/BQT/BQT_v5_pages.txt; do echo \"### $f\"; grep -n -i \"meregh\\|mereg\\|saena\\|saëna\\|saéna\\|sacna\\|murv\\|mrgh\" \"$f\" | head -10; done"
}
```


### [2026-09-07T16:22:23.171Z] TOOL RESULT

```
### BQT_v1_pages.txt
### BQT_v2_pages.txt
### incoming/BQT/BQT_v3_pages.txt
### incoming/BQT/BQT_v4_pages.txt
### incoming/BQT/BQT_v5_pages.txt
```


## [2026-09-07T16:22:34.050Z] TOOL CALL #37: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 380<=i+1<=420:\n        nums=re.findall(r'[۰-۹]{3}',p[:300])\n        print(i+1,nums[:5])\nEOF"
}
```


### [2026-09-07T16:22:35.369Z] TOOL RESULT

```
380 []
381 []
382 []
383 []
384 []
385 []
386 []
387 []
388 ['۱۹۹']
389 []
390 []
391 []
392 []
393 []
394 []
395 []
396 []
397 []
398 []
399 ['۱۵۰']
400 []
401 []
402 []
403 []
404 []
405 ['۲۵۷', '۲۵۲']
406 []
407 []
408 []
409 []
410 []
411 []
412 []
413 []
414 []
415 []
416 []
417 []
418 []
419 []
420 []
```


## [2026-09-07T16:22:43.061Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    n=i+1\n    if 208<=n<=260 or 370<=n<=392:\n        nums=re.findall(r'[۰-۹]{1,4}',p[:200])\n        print(n,nums[:6],'|',re.sub(r'\\s+',' ',p[:60]))\nEOF"
}
```


### [2026-09-07T16:22:44.340Z] TOOL RESULT

```
208 [] | 
209 [] | 
210 ['۱', '۱', '۴'] | ۱ بروزن جاء امر بآآمدن باشد (۱) یعنی بیا و بمربی تعالکویند -
211 ['۷', '۲', '۲'] | اشارتمت بر ضی‌کامل و عقل کل » و او را ضس حلهیه گویتد ۷ - آب 
212 ['۳', '۱'] | ۳ است از سال هی » و آن بودن خورشید باشد هر" برج قرب - - و دا
213 ['۱', '۰'] | آي ول آب لح » بکرناك ؛ خراب انگوری باشد -‏ وکنابه از اتك چش
214 ['۰'] | آت خوست « بر وزن ارت ۰ مکی دج ماه کید منم باینسسنی بفتح‌خا ف
215 ['۷'] | آب ست آب دست ب بر وژن‌خاربست , امستجا کردن بآب - و وضو ساختن
216 [] | ساختن ناشد . " .ریز - بر وزن خاه ریز . ادبخانه و مستراح را گ
217 ['۱', '۲'] | " ]یست - بنتح ثاك و سکون رابم و فوقالی . کرشت ترنج را گویند 
218 ['۸', '۱', '۲'] | "آب سیه « یکی اك , مخخف آب سیاء انت که شراب انگوری - و علت ک
219 [] | آب صفت بودن - کنابه از یار بفم و فایده رسانیدن باشد - و بالق
220 [] | ات آآب کبوث- بکس ات ؛ دربای‌چین را کوید.و آن را جریی محر اخض
221 [] | نواحی باشند از دنبال شخصي که آب میبرد روان شوند تا بهرجا که 
222 ['۱'] | 0 آش تلم رودخانه ایست که آنرا رودخانة آهو ٩‏ فیز میگویشد . آ
223 ['۱', '۱', '۱', '۲'] | ۱ آخن آب پرود ۱ ۱ اه کیره راگونند ؛ یمنی حرچی ز که بدان آش ا
224 ['۰'] | وا ثِ آ دامن وکاف ۰ بمننی آش زده اس ت که چنساق‌باشد . * ] نش
225 ['۰', '۲', '۱'] | آش محقان ۰ ۲ تش ذهقان ه بکر رابم » آنثی را کوبند که دهفان بد
226 ['۲', '۶', '۳', '۰'] | و مطیخی و آهنگر و امثال آنرایز کوند . * ۲ تشکدة بهر ام - کنا
227 ['۱', '۱'] | کویند . ۱ 1 | تین پنجه - بتح بای فارسی » کاریکر (۱) و لستاد 
228 [] | عمل کردن ویبروی تىودن ناحکام شرمعت باشد . ] چالك - با جیم فا
229 ['۲', '۴'] | که در آن حاسلی ونفعی لبوده باشد ٩‏ . ۲ خر لك » بر وزن ناخنك 
230 ['۱'] | ] خشیگه ه با کان فارسی » بی وزن ومعنی آخشیج است ت ۱ که نفض و
231 ['۱', '۰'] | آده | ده » بر وزن جاده » دو چوب بلندی اس ت که در زمین فرو بر
232 [] | رنه حهای نی وآن بودن آفتاب‌است در برج فوی - و نام روز نهم با
233 ['۵'] | ] تربلدگان وت که تیربز شهر آنولابت است . کوبند وقتشکه آغور ۵
234 [] | آآذد بردفی - نام آنشکده ششم است که در فاری برزین نام , شخصی 
235 ['۴'] | آترخردار و خستکار آشکده را کوند . 8 این 0 میداشه ؛ غز مه ممد
236 ['۳', '۳', '۴'] | آذرشپ - و " مرکق ۳ ۳ ] در شین « بکر شین وسکون نحتانی و نون .
237 ['۵', '۴'] | آخر کون نت آ داد کش ها یکی کنق. و کون بحتانی مجپول و شین قسر
238 ['۱'] | 7 در هما بون - بن‌ها . بابساحرهای بوده از نسل سام و. خدمت آت
239 ['۱'] | آرا آداه بروزن خارا . آرایش. وآرایش کننده و آراینده را کویند
240 ['۳', '۵'] | ت برایو بی اه آرامی رة حواشی صفحة .۳ ۵ آرامی_نام قومی از فبا
241 ['۷۲'] | آرامی - پرایی ۷۲٩‏ س آرامی بکاربردند. بدبنوجه زبان آرام یکه 
242 ['۱', '۴', '۱'] | مخفف آوداس تکه نام روز بیست و پنجم از هر ماه شمی باشد ۱- و م
243 ['۰', '۰', '۰'] | ]دی ح بکر الث و رايع و سکون تحتانی ۰ بمعنی ممنوی باشد که در 
244 ['۰'] | دوع ۰ با غن نقطه دار سس وزن فاروق , بادی را گویند که از کلو 
245 ['۱'] | در دل کسی‌جای کند ؛ وباین معلی بازای نفطه‌دار هم آمده است . 
246 ['۵'] | سب چ ح آزا۵ذارو- با دال ابجد بالف کشیده و رای فرشت عضوم بواو
247 [] | آزدن رذن . بازای فارسی » بروزن و معنی آزدن بلشد که خلانیدن س
248 [] | ده آ زر نگ - بفتح رأیم بوزن با درنگه . بمعلی غم سخت و محنت ص
249 [] | رود 5 با زای هوژ بر وزن ساطور » صاحب حرص و آز را کونند که حر
250 ['۳', '۴'] | ۳ آسا آن را « حب الآس » خوانند ۴. کونند عمای موسی علیه السلا
251 [] | آسیابان باشد چه آسیا راآس میگویند . آس بری « بکس تالث و فتح 
252 ['۱', '۲'] | بمعثی بطانه است - و کنابه باشد. اسقی » بر وزن راستی » بمعنی 
253 ['۱۰', '۳'] | آسمار با میم بروزن شاخار , ورخت ]| کهکثانرا کویند و بعربی مج
254 ['۱'] | اندلختن و عداوت بهمر‌سانبدن علق باو دارد . ستستان » بکس تون 
255 ['۶', '۴'] | است که موسی علیه‌اللام را پرورد . ۶ ]شام - بائن .قطمدار بروز
256 ['۷'] | ی آشنا کر خابة سک آنی است ۷ . خالهرا نیز گویند چنانکه گوبند 
257 ['۳', '۰', '۳', '۱', '۶', '۷'] | آشناو ۳ ف_ رای فرشت ۰ بمعنی شناور باش که شناکننده | شور و فت
258 ['۰', '۱', '۱', '۰'] | ۰- 1 حه شا فه ۱ - بروزن‌تلزبانه.بمعنیآشیان است که خانهٌ مرغا
259 ['۱'] | شخصی دییگر - وبمعنی تحريك‌نمودن وبرشورانیدن بجنگه هم هست که 
260 [] | "-هِ- " ]غود ع بنم ات و سکون واو وزای هوز. .. شیری باشد که ا
370 ['۵', '۱', '۵'] | 9 تست سس با وس سید بد و تسس سح برایر ,۵ ۱ - # 0 « ۵ و رم 7
371 [] | 
372 [] | حم اي ٩‏ سه معلوم » نام کتابی از بپودان است: - بلفت بونانی و
373 ['۳'] | آزامه ناه روند بخورند سل را منعطم سازد . واکر اژدو درهم بشتر
374 ['۱', '۴'] | 7 وه پوشند - وبکسراول هم آهده است بمعنی نوعی از دیبای ساه , 
375 ['۰', '۰', '۰', '۱', '۰'] | (که ۰ ۰ ی بیان بیست و یکم در همره باکاف فارسی مشتمل برهشت لغ
376 [] | - ٩ پاي‎ -- الاطینی « باطای‌حطی بر وژن‌قباچینی» بافت رومی ٩‏
377 [] | الرك- بفتح اول و انی و سکون را و دال بی نقطه . جوالی باشد از
378 [] | -- هي ٩‏ ح الفیدن - بر وزن بر چدن » بنعثی الفنجیدن است که کس
379 ['۱', '۳۳'] | او فد بروزن و معنی اروند باشدکه نام کوهی است بلند در نواحی ه
380 ['۱', '۱', '۰', '۴'] | 2 اهر ) - بقتح اول و انی و رای بی‌نقطه بالف کشید» » بلفتزندو
381 ['۷', '۱', '۲۳'] | که زر بائد! .۷ امی‌صادق - بنم اول , اشاره (۱) به حضرت رسالت 
382 ['۱'] | یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان کن » باشد . وآن دا
383 ['۵'] | اتبارش که پر کرده باشد - و بمعنی پرنسمت و با نعست هم اجه ات 
384 ['۰'] | سب ی ٩5‏ | بودن بروزن افزودن, بربالای حم چیدن باشد . اثبوذن 
385 ['۱', '۱'] | انج - بفتح اول وسکون ثانی و جیم» اطراف 2 روی و رخار ( ۱ ) با
386 ['۳', '۰'] | - بو - ) فحل س بفتم اول وکسر ثالث و سکون نانی ولام» رسثنی با
387 ['۲'] | انجین از توابم بزد - و ناوچهٌ مقمد و سوراخ کون را نیز گویند 
388 ['۱۹۹', '۱'] | -۱۹۹ - )اد « بروزن پرواژ ؛ ممنی شسد - و میل نمودن - و حمله ک
389 [] | اندر خور ا ندز خو در - بنمخای نفطه‌داروسکون واو ممدو له و را
390 ['۴', '۳'] | اف او رفتی . بکشب بای شد و آتش را بکشت راندروی درمیان دربا ک
391 [] | انسجان که کرفتگی دل ودلگیری باشد . اندهان بروزن مردمان ؛ جمم
392 [] | رن ار ه- باازای فارسی بر وزن غمزه ؛ مرجماث باشد و آثرا ببربی
```


## [2026-09-07T16:22:59.463Z] TOOL CALL #39: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"سیمرغ\\|سيمرغ\" BQT_v1_pages.txt | head -20\necho \"=== leaves\"\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'سیمرغ' in p or 'سيمرغ' in p:\n        print('leaf',i+1)\nEOF"
}
```


### [2026-09-07T16:23:01.031Z] TOOL RESULT

```
26758:چه کویند او را سیمرغ بز رکه کرد وسیمر غ‌را
=== leaves
leaf 653
```


## [2026-09-07T16:23:16.754Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfor n in (379,380):\n    print('===== leaf',n)\n    print(t[n-1][:1500])\nEOF"
}
```


### [2026-09-07T16:23:18.730Z] TOOL RESULT

```
===== leaf 379
او فد بروزن و معنی اروند باشدکه
نام کوهی است بلند در نواحی همدان ۱ . گویند
دوازده هزار چشمه آب از داسن آن کوه بر
۳۳
4 « بفتح اول وثانی و خفای ها » مقل
ازرق باشد و آن صمغ مانندیست دوامی - ویضم
ثانی و ظهور حا عقاب را گویند وآن برنده‌ایست
ممروف که پر او را بر‌تیر نصب کنند. و بانشدبد
ثانی هم درست تور >
الا - بفتح اول و سکون ثانی و تحثانی
وت
بالف کشیده . بلفت بونانی خطمی صحرابی را
کوش و عرین شح‌الدر ج خوانند .
الیاس ۴ یکسر اول و سکون ثانی
و تحتانی بالف کشیده و بسین بی نقطة زده . نام
پیغمبرست. مشپور و او پسرزادة سامبن فوح‌است
و عمحضرت. خضر- و ومیادشاه بر خر کمدربای
گپلان باشد .
الیز - بفتح اول و کسر ثانی وسکرن
تعنانی و زای هوز . جفته و لکد انداختن اسب
و استر و سابر ستور باشد ۴
است» » وم رکب استعمال کنند حمجو جامهام
و خامه‌ام یی جامهٌ دن و خامهٌ من - و بمعنی
اين باشد ۷ و عرب هذا کوبند همییو امروز
وامسال یمنی امن دوز واین سال ۷ .
اماج ین اول بر وزن کماج , نوعی
از آش آرد است - و پفتح اول توة خاک که
نشانة ثبر بر آن نهند - ونشانة تير و افزار
برزیگران باشد .
اماری ۸ بکر اول پروزن اشاره ,
بمعنی حساب وشماره باشد, چه امار گیر حساب
۳ راگونشد ۰
امامون » با میم بروزن‌قلاطون .بلفت
بونانی ٩‏ دوایی است که آ نرابفارسی ماهلووبعربی
حیاما خوانند .گرم و خشث اتتخ دردوم ؛بول
را براند .
امف » بفتح اول وسکون‌ثانی ودال‌ابجد .
بمعنی هنگام و زمان و موسم باشد .٩*‏
(۱) چك : سیوم .
۱ - پهلوی 2۱۷600 و من-وب‌بدان 21۷60016 داونوالا ۲۸۹» دراوستا 20۳۷۵۳
بمعنی تندمند , دارای تندی وئیزی. ۳ رگ : آله. ۴ - ۱1188 , ایلیا جاوززا۴
«جفری ٩۷‏ - ۹۸ پیفمبر بنی اسرائیل معاصرآحاب پادشاهاسراثبل «قاموی مقدس ۵-۱4۶ ۱4*.
۴ - رك : آلیز
===== leaf 380
2
اهر ) - بقتح اول و انی و رای بی‌نقطه
بالف کشید» » بلفتزندوپازند (۱) شراب‌انگوری
باشد - و بسکون انی خرالاغ راگویند ۱ .*
اهروت ه با تای‌قرشت . بروزن‌ومعنی
امرود است و ان موه‌ای باشد ععروف ۰
امر ود ۴ ع با دال » بر وژن و عمنی
امررت است و آن هیوه‌ای باشد معروف .
اهشاسیند " » با شین نقطه دار و سین
بی‌نقطه بای فارسی بروزن سیلآب کند . فرشنه
وملك را گویند .
امشاسیند است که فرشته وملك ماشد .
امعاسین ‌ بفتح اول وسکون انی‌وعجن
بی‌نقطه بالف کشیده وسین بی‌نقطه بتحتانی رسیده
و بنون زده ۰ بلفت رومی ۴ آب غوره را گویند
و بعربی ماءالحصرم خوانند.
اهقیالان - بنتم اول وضم ثانی وفتح‌غین
نقطه‌رار وسکون تحتانی ولام بالف کشید. و بنون
زده ؛ نام درختی است هعروف ومشپور بمغیلان .
گونند حنضمکی را ازب رک آن‌میسازند وآنرا
بعربی شو کفالمصربه خوانند ؛ و بتشدید انی هم
منظر آ مده استد د
(۱) چك ؛ ژند و پاژند .
املاق - تکتر اول و سئون ثانی ولام
تالف کیده و بقاف زده » تلم ولاسی است از
کنر
امنه ت شح اول وئانی و نون ۰ پشتهیزم
امس » بفتح اول وضم شانی وسخون
واو وسین بی‌نقطه . تخمی باشد که بر روی نان
باشند وا نان‌خواه دز گویند. و باهیزمممدوده
هم بتظر آمده است .
وکسر واو و سین بی‌نقطة ساکن و نون بتحتانی
رسیده » دو زن را گونند که يك شوحر داشته
باشند وهريك مردیگری را اموسنی بووه .
امهوسیندا « با هار سین بی نقطه
و بای فارسی بر وزن اندوهمند . بمعتی ملكث
و فرعته بادد .
امهو سغند! ه با ها . بروزن وععنی
ژر باشد .
امیان - بروزن ومعنی همیان است که
۲
عوستی ۹6۵ 9
«نایتی #۱۹۳
علامت‌تفی و11966[(8 از ربشة 1512۴ (مردن), جزه دوم سپنته (اسپند) بمعنی مقدس, جمعاً بمنی
جاودان مقدس, وآن ءنوان هفت فرشتة بزرکگست که نام‌دش تای آنها در ضمن ماع
```


## [2026-09-07T16:23:38.799Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\nfor i,p in enumerate(t):\n    n=i+1\n    head=p[:120]\n    for m in re.finditer(r'[۰-۹]{3}',head):\n        v=int(''.join(str(fa.index(c)) for c in m.group()))\n        if 1<=v<=600 and abs(n-v-189)<=6:\n            print('leaf',n,'num',v,'offset',n-v)\nEOF"
}
```


### [2026-09-07T16:23:40.246Z] TOOL RESULT

```
leaf 388 num 199 offset 189
```


## [2026-09-07T16:23:45.565Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re, collections\nt=open('BQT_v1_pages.txt',encoding='utf-8').read().split('\\f')\nfa='۰۱۲۳۴۵۶۷۸۹'\nc=collections.Counter()\nhits=[]\nfor i,p in enumerate(t):\n    n=i+1\n    head=p[:150]\n    for m in re.finditer(r'[۰-۹]{3}',head):\n        v=int(''.join(str(fa.index(ch)) for ch in m.group()))\n        if 1<=v<=700:\n            c[n-v]+=1\n            hits.append((n,v,n-v))\nprint(c.most_common(8))\nfor h in hits:\n    if h[2] in [x[0] for x in c.most_common(3)]:\n        print(h)\nEOF"
}
```


### [2026-09-07T16:23:46.836Z] TOOL RESULT

```
[(4, 3), (3, 2), (-129, 2), (-198, 2), (-185, 2), (15, 2), (-5, 2), (-63, 2)]
(4, 1, 3)
(4, 133, -129)
(26, 155, -129)
(125, 121, 4)
(125, 121, 4)
(158, 155, 3)
(159, 155, 4)
```


## [2026-09-07T16:23:56.921Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"simurgh\\|simurg\\|murgh\\|Avestic mere\\|mereghō\\|saēna\\|saena\" KLN_1966.txt | head -20\necho \"=== 1971\"\ngrep -n -i \"simurgh\\|simurg\" KLN_1971.txt | head -10"
}
```


### [2026-09-07T16:23:56.995Z] TOOL RESULT

```
35275:simurg,  n.,  a  gigantic  bird  in  Persian  mythology, prob.  identical  with  the  roc.  — -  Pers.  simurgh, rel.  to  Avestic  saend  mereyd,  ‘eagle’,  OI.  syenaft, ‘eagle’.  Arm.  (in,  ‘kite’.
=== 1971
222331:simurg, n., a gigantic bird in Persian mythology, 
222332:prob. identical with the roc. — Pers. simurgh,
```


## [2026-09-07T16:24:05.567Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} {n++; if (index($0,\"simurg,\")>0) print \"leaf(1-based)=\"n}' KLN_1966.txt\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read().split('\\f')\ni=None\nfor k,p in enumerate(t):\n    if 'simurg,' in p: i=k\nprint('leaf idx0',i,'-> est printed', (i-12)*2)\nprint(t[i][:300])\nEOF"
}
```


### [2026-09-07T16:24:07.207Z] TOOL RESULT

```
leaf(1-based)=769
leaf idx0 768 -> est printed 1512
 Pure  is  dealt  with  as  an  impostor  and  is  believed only  after  he  has  proved  his  identity, simoniac,  n.,  one  who  practises  simony;  adj.,  per¬ taining  to  simony.  —  ML.  simoniacus,  fr.  simo- nia.  See  simony.
Derivatives:  simoniae-al,  adj.,  simoniac-al-ly, adv.
simony,
```


## [2026-09-07T16:24:14.538Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read().split('\\f')\nfor i in (490,491,492):\n    print('==== leaf idx0',i)\n    print(t[i][:600])\nEOF"
}
```


### [2026-09-07T16:24:16.013Z] TOOL RESULT

```
==== leaf idx0 490
ux,  gen.  lucis,  ‘light’.  See  lucent  and  -ule.
luculent,  adj.,  clear,  lucid.  —  ME.,  fr.  L.  luculen- tus,  ‘bright,  brightly  burning’,  formed  from  the stem  of  lux,  gen.  lucis,  ‘light’  (see  lucent),  with suff.  -u-lentus,  meaning  ‘full  of,  abounding  in, rich  in’.  Cp.  L.  opulentus,  ‘rich,  wealthy*,  lit.  ‘re-
910
sourceful,  powerful’,  fr.  ops.  gen.  opis,  ‘strength, might;  riches’  (see  opulent).
Derivative:  luculent-ly,  adv.
Lucullan,  Lucullean,  adj.,  pertaining  to,  or  resem¬ bling  L.  Licinius  Lucullus  (about  1 10-57),  a  Ro¬ man  gener
==== leaf idx0 491
  border',  and  with  E. limp,  adj.  and  v.  (qq.v.)  Cp.  limb, ‘edge’.  Cp.  also lunch.
Derivatives:  lump,  tr.  v.,  to  make  into  a  lump; intr.  v.,  to  form  into  lumps,  lump-er,  n.,  lump¬ ing,  adj.,  lump-ing-ly,  adv.,  lump-ish,  adj.,  lump- ish-ly,  adv.,  lump-ish-ness,  n.,  lump-y,  adj.,  lump- i-ly,  adv.,  lump-i-ness,  n. lump,  intr.  v.,  to  look  sullen;  tr.  v.,  to  dislike.
Of  uncertain  origin.
i  nun,  n.,  the  moon-goddess  ( Roman  mythol.)  — l ..  Luna  ‘moon*.  See  lune.
912
lunacy,  n.  —  Formed  fr.  lunatic  with  suff.  -cy. lunar,  adj.,  
==== leaf idx0 492
an instrument’,  and  -ist.  Cp.  lutist. lute,  n.,  a  cohesive  substance.  —  ME.,  fr.  MF. (=  F.)  lut,  fr.  L.  lutum,  ‘mud,  clay’,  which  stands for  *lutom  and  is  rel.  to  -luere  in  polluere  (for *por-luere),  ‘to  pollute,  contaminate’,  and  to  lus¬ trum  (for  *lu-strom),  ‘slough,  bog,  morass’.  See pollute  and  cp.  lutetia,  Lutetian.
Derivatives:  lute,  tr.  v.,  lut-er,  n.,  lut-ing,  n. lute,  n.,  a  stringed  instrument.  —  ME.,  fr.  OF. lut  (F.  luth),  fr.  OProven?.  laiit,  fr.  Arab,  al- ‘iid  (whence  also  Sp.  laud,  Port,  alaude.  It. liuto)
```


## [2026-09-07T16:24:23.114Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'(?m)^\\s*(958|959|960|961)\\s*$',p):\n        print('leaf idx0',i, re.findall(r'(?m)^\\s*(9[0-9]{2})\\s*$',p))\nEOF"
}
```


### [2026-09-07T16:24:24.559Z] TOOL RESULT

```
leaf idx0 514 ['958']
```


## [2026-09-07T16:24:27.705Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('KLN_1966.txt',encoding='utf-8').read().split('\\f')\np=t[514]\nprint(p[:2500])\nEOF"
}
```


### [2026-09-07T16:24:29.260Z] TOOL RESULT

```
at’  (in  physics  it  is  used  in  the meaning  of  ‘a  million  times’,  e.g.  megavolt  —  a million  volts).  —  Fr.  Gk.  pEyap,  fem.  psyiXv], neut.  peyx,  ‘great,  large,  mighty’,  which  is  cogn. with  L.  magnus,  ‘great,  large,  much,  abundant’, Goth,  mikils,  OE.  micel,  mycel,  ‘great,  big, many’.  See  mickle  and  cp.  magnum.  Cp.  also omega,  acromegaly,  almagest,  Agastache. megacephalic,  megacephalous,  adj.,  large-headed.
—  Compounded  of  mega-  and  Gk.  xeqpaXir), ‘head’.  See  cephalic,  resp.  cephalous.
Megaceros,  n.,  a  genus  of  mammals  of  the  deer family  (zool.)  —  ModL.,  compounded  of  mega- and  Gk.  x£pa?,  ‘horn’.  See  cerato-.
Megachile,  n.,  a  genus  of  bees  (zool.)  —  ModL., compounded  of  mega-  and  Gk.  ypThoc,,  ‘lip’. See  chilo-.
megal-,  form  of  megalo-  before  a  vowel, megalith,  n.,  a  huge  prehistoric  stone.  —  Com¬ pounded  of  mega-  and  Gk.  >.£f>o<g,  ‘stone’.  See litho-.
Derivative:  megalith-ic,  adj. megalo-,  before  a  vowel  megal-,  combining  form meaning  ‘large,  great’  (in  medicine  it  is  used  to denote  abnormal  enlargement).  —  Gk.  psyaXo-, peyaX-,  enlarged  stem  of  pEyoo;  (gen.  peyaXou), ‘large,  great,  mighty’.  See  mega-, megalocardia,  n.,  abnormal  enlargement  of  the heart  (med.)  —  Medical  L.,  compounded  of megalo-  and  Gk.  xapSia,  ‘heart’.  See  cardio-. megalocephalic,  adj.  —  The  same  as  megacephal¬ ic.
megalomania,  n.,  mania  for  great  things;  delu¬ sion  of  greatness  (med.)  —  Medical  L.,  com¬ pounded  of  megalo-  and  Gk.  pavia,  ‘madness’. See  mania.
Derivative:  megalomani-ac,  adj. megalosaur,  n.,  any  animal  of  the  genus  Megalo- saurus.  —  See  Megalosaurus. megalosaurian,  adj.,  pertaining  to  the  megalo- saurs;  n.,  a  megalosaur.  —  See  prec.  word  and -ian.
Megalosaurus,  n.,  a  genus  of  gigantic  dinosaurs ( paleontol .)  —  ModL.,  compounded  of  megalo- and  Gk.  craopop,  ‘lizard’.  See  sauro-. megaphone,  n.  —  Compounded  of  mega-  and Gk.  9fovif),  ‘voice’.  See  phone,  ‘speech  sound’, megapode,  also  megapod,  n.,  any  of  the  birds  of the  family  Megapodiidae.  —■  See  next  word. Megapodiidae,  n.  pi.,  a  family  of  birds  inhabiting Australia  and  the  Malay  Archipelago  (orni- thol.)  —  ModL.,  formed  with  suff.  -idae  fr. mega-  and  Gk.  7toui;,  gen.  71086;,  ‘foot’.  See podo-.
megaron,  n.,  the  great  hall  in  the  Greek  palace, es
```


## [2026-09-07T16:24:37.768Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read().split('\\f')\nfor i in (768,769,770):\n    print('leaf idx0',i, re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$',t[i]))\n# also find 1461 marker (KLN:1461 for smerzan/smart)\nfor i,p in enumerate(t):\n    if re.search(r'(?m)^\\s*(146[0-2])\\s*$',p):\n        print('page-marker leaf',i, re.findall(r'(?m)^\\s*(14[0-9]{2})\\s*$',p))\nEOF"
}
```


### [2026-09-07T16:24:39.153Z] TOOL RESULT

```
leaf idx0 768 ['1448']
leaf idx0 769 ['1449', '1450', '1451']
leaf idx0 770 []
```


## [2026-09-07T16:24:45.834Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if re.search(r'(?m)^smart,',p) or 'smart, adj' in p or 'smart,  adj' in p:\n        print('leaf idx0',i, re.findall(r'(?m)^\\s*(1[0-9]{3})\\s*$',p))\n        m=p.find('smart')\n        print(p[max(0,m-200):m+1400])\n        break\nEOF"
}
```


### [2026-09-07T16:24:47.213Z] TOOL RESULT

```
leaf idx0 775 []
aragdus,  fr.  Gk.  aptdpa- ySo g.  See  emerald.
smaragdite,  n.,  a  green  variety  of  amphibole.  — F.,  formed  with  subst.  suff.  -ite  fr.  Gk.  ofxdpa- ySoc,  ‘emerald’.  See  prec.  word, smart,  intr.  v.  —  ME.  smerten,  fr.  OE.  smeortan, rel.  to  MDu.  smerten,  smarten,  Du.  smarten, OHG.  smerzan,  MHG.  smerzen,  G.  schmerzen, ‘to  pain*,  orig.  to  bite’,  rel.  to  LG.  marten,  ‘to
fall  to  pieces,  to  decay’,  and  cogn.  with  Gk. apspSvog,  aptEpSaXsog,  ‘terrible,  fearful’,  lit. ‘rubbing,  crushing’,  OI.  mardayati,  ‘grinds, rubs,  crushes’,  mdrdati,  mrdnati,  ‘presses,  rubs’. Arm.  mart,  ‘combat,  fight’.  L.  mordere,  ‘to bite’,  Lett,  merdet,  ‘to  waste,  emaciate;  to  starve (tr.);  fr.  I.-E.  base  *(s)mer-d-,  a  -(/-enlargement of  base  *(s)mer-,  ‘to  rub,  pound,  consume,  wear away,  exhaust,  worry;  to  be  consumed’,  whence Gk.  puxpaivstv,  ‘to  waste  away’.  Cp.  smart,  n. and  adj.  Cp.  also  almuerzo,  amaranth,  ambrosia, amrita,  mar,  marasmus,  marble,  marcid,  mar¬ moreal,  morbid,  morceau,  mordant,  mordent, morsel,  mortal,  mortar,  murder,  murrain,  pre¬ morse,  remorse,  smorzando.
Derivatives:  smart,  adj.  (q.v.),  smart,  adv., smart-ing,  adj.,  smart-ing-ly,  adv.,  smart-en,  tr. v.,  smart-y,  adj.
smart,  n.  —  ME.  smert,  fr.  OE.  smeart,  rel.  to MDu.  smerte,  smarte,  Du.  smart,  OHG.  smerzo, MHG.  smerze,  G.  Schmerz,  ‘pain’,  and  to  OE. smeortan,  ‘to  smart,  pain’.  See  smart,  v. smart,  adj.  —  ME.  smerte,  ‘painful’,  fr.  OE. smeart.  See  smart,  n.
Deriva
```


## [2026-09-07T16:25:30.394Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### PHD framōš / murw / sēnmurw\"\ngrep -n \"^framō\\|^framoš\\|framōš\\|^murw\\|^sēnmurw\\|sēnmurw\\|^murwag\" PHD.txt | head -20\necho \"### PHD_mackenzie\"\ngrep -n \"framōš\\|murw \\|sēnmurw\" PHD_mackenzie.txt | head -20"
}
```


### [2026-09-07T16:25:30.453Z] TOOL RESULT

```
### PHD framōš / murw / sēnmurw
### PHD_mackenzie
2331: fral(a)murw [pllmwlw I M frlymwrw] peacock.
3253: -(ag) murw [_kl I N kaskina] ·magpie.
3614:murw [mwlw l I M mWTW, (N mUTY)] bird.
4542:2Sen murw [synmwlw 1 (N simury)] a fabulous bird.
8592:                            -c.. V      frasamurw                 ~~Q)
9065:sen murw               \ t6 K»          salag
9118:padir~r                 -,~~        murw                       \~~
```


## [2026-09-07T16:25:36.607Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"framos\\|framoš\\|fram6\\|pl'mws\\|plmws\" PHD_mackenzie.txt PHD.txt | head -20\necho \"### PHD.txt murw\"\ngrep -n \"murw\" PHD.txt | head -20"
}
```


### [2026-09-07T16:25:36.675Z] TOOL RESULT

```
PHD.txt:325:farr-, v. xwarrah. Farrūbāģ [plwb(’)g] the first major Fire of Sasanian Eran, that of priests and nobles. farrox [plhw' | M prwx, N ~] fortunate, blessed, happy. ~ih: fortune, joy, happiness. filāsūfā [pyPswkp!y] philosopher. frabih [plpyh | (P frbyw), N farbih] fat, stout. Fradadafš [pldtpš = Av. fradašafšū-| the south-eastern continent of the earth. fradág [MHL < A mhr; ИРА! | N farda] tomorrow. frādahišnīh [pP dhšnyh] increase, progress. fradom [AWLA < Ar. !?wD; pltwm | (M prtwm)] first. ~th: first, beginning. fragan [plk?n'] base, foundation; origin. fragandan, fragan- [plkn-dn'} lay foundations. frahang [pl’hng | N farhang] education; knowledge. --estàn [-st?n!] school. frahanj-, v. frahixtan. frahist [p/h(y)st! | (M pryst)] most (superlative of freh), frahixtag [plhhtk' | N farhixta] educated, trained, skilled. frahixtan, frahanj- [plhhtn', pDhnc- | P frhynj-, N far~] educate, teach, instruct. framādār [рж?РЦ commander, ruler, chief. framān [pim^n! | M frmn, N farman] order, command; a minor degree of sin. ~-burdar [-bwlt?l | N -bardār] obedient, submissive. framāy-, ~išn, v. framüdan. framds [bl(?)mwš | M pr’mws, N farámos] forgotten. framošidan [plmwšytn'] = framuštan. framüdan, framāy- [plmwin', plm'd- | M prm'dn, prmy-, N far~] order, command. — $n: order, commandment. frāmuštan, frāmēš- [pl(?)mws-in' | M prhmwst, pr’mwi-, N fard~] forget. franaftan, *franam- [pinptn!, *plnm- | M prnpt, prnm-] go, proceed, depart. franāftan, franām- [pin!ptn!, pli m- | P fri m-] 1. lead, conduct, re- move, promote; 2. profess, propagate (faith). ~išn: removal, promotion, profession. frarast [p/”Pst'] a cubit (18 in.). fràrón [p lwn'] righteous, honest. ~ih : righteousness, honesty. frasang [plsng | N farsang) parasang (4 Roman miles).
PHD_mackenzie.txt:2309:framosidan [plmwfytn l ] = framustan.
PHD_mackenzie.txt:6639:forgotten anayiid, frAmos.                   fruitful baromand.
PHD_mackenzie.txt:8621:framosidan               ,\tu'\)   ~ C,)   parwar-                           _\~Q)
PHD_mackenzie.txt:8651:frazaftan                \\lOeu~Q)         framos
PHD_mackenzie.txt:8653:fras, pars                    ~0           fram6s-
PHD_mackenzie.txt:8707:framos-           -""'U~4)       friixih                 ~~Q)
### PHD.txt murw
333:fra$(a)murw [plfmwlw! | M fréymwrw] peacock.
398:P hd [Aw' | = P] that, he. Hóm [kwm | N ~] the sacred plant Haoma (ephedra). homānāģ [h(w)m’rk' | N hamana, J xumana], 6 .. . ~: like. ~th: likeness. hómast [hwn'st!] various series of prayers. hómyjén, -ïg [hwmyn!, -yk'] of Haoma. ~ӧтапа [-'wmnd] prepared with Haoma. Ногааа [hwrdt' | M hrwd'd, N Xurdād] Perfection, the fifth Amahra- spand, guardian of water; cal. 3rd month; 6th day. hdsag [hwsk' | М лое, N xēša] ear of corn, cluster; astr. Spica, Virgo. hēšēnīdan, hoSen- [hwsyn-ytn'] (cause to) wither. hēšīdan, hēš- [hws-ytn' | M hwi-, N x~] dry up, wither. héy(ag) [hwy, -k! | M hwy] left(-hand). Hróm [hlwm | M hrwm, N Рат] Byzantium, Rome. ~ayig [-dyk'] Greek, Byzantine, Roman. hu- [hw- | = M] good-, well-. ~ih: good, goodness. hu-bóy [hwbwd] sweet-smelling, fragrant. ~th: fragrance. hu-čašm [hwesm] unenvious, benevolent. ~ih: benevolence. hu-čihr [hweyhl | M hweyhr, (N xujir)] fair, beautiful. hudà(ha)g [hwa?(h)k' = Av. hudàáh-] good, beneficent. ~th: beneficence. hu-|-dast [hwdst'] skilful. ~-dén [-dyn'] of good (i.e. Mazdean) religion. ~-ddsSag [-dušk'] very pleasing. m-ēwāz [-"yw'c] of good speech, affable. —-ëwàzih : affability. ~-fraward [-plwit'] blessed, the late. hugar [hwgl] easy; beneficent. hu-|-&ówisn [hwgwbsn'] of good speech. ~-gugar [-gwk’l] easily digestible. ~-kunign [-kwnsn'] of good behaviour. „-mānīh [-m’nyh] good-mindedness, benevolence. humat [hwmt' = Av. humata-] good thought. humāy [hwm’y | N ~] a bird of good omen; eagle. hu-menišn [hwmynsn'] of good thought. hu-murwāģ [Awmwlw’k'] auspicious. hunar [hwal | M hwnr, N ~] virtue, ability, skill. hunarāwand [kwn wnd | M hwnr'wynd] skilled, virtuous. ~th: skill, virtue. hunarómand [kwn wmnd | N hunarmand] = hunarāwand. hunidan [kwnytn'] extract, express (juice). huniyág [/sonyd?k! | N xunyá] delightful. ~th: delight, entertainment.
426:kardan, kun-, (P Каг-) [OBYDWN-in' < А У Фа; krtn!, kwn-, (kl-) | M kyrdn, kwn-, (P kr-), N ~] do, make, act, perform. ~išn, v. kunišn. kardār [krt-, kil | N ~] active; worker, doer. ~th: activity. kard-espās [krtsf?s] servant, attendant. kārezār [A /yc! | M k*ry2*r, N kārzār] battle(-field). kār-framān [%'/p/mn' | М k’rprm’n, Ar. qahramán] manager, overseer. karg [klg | N ~] rhinoceros. kargās [klk’s | N kargas] vulture. kárig [k’lyk'! | N kari] active; warrior. ~ih: activity. kark [АА | N ~] chicken, hen. karkéhan [k/kyhn'] chalcedony. karm [Айт | P krm] action. karmir [klmyr] red, crimson. kār-nāmaģ [Rr mk!] record, chronicle. karr [k/ | M qr, N ~] deaf. karx68 [klhwš | (IN čarxušt)] wine-press. *karzang [kleng | M kyrzng, (ЇЧ xarcang)] crab; astr. Cancer. kas [4 YŠ < A?y£ | M ks, N ~] person, somebody. ~-iz [-c] anybody, (with a negative) nobody. kāskēn [k’skyn'] lapis lazuli. (аб) murw [-&! | N kāskīna] *magpie. ~ën [-yn'] blue-green; of lapis lazuli. kastan, kāh- [R’stn', Ph- | N ~] diminish, decrease, lessen. ~iSn: decrease, diminution. kastār [kst?]] destroyer, wrongdoer. ~ih: destruction, iniquity. kāstār [ks 1] diminisher. kaš [Rs | N ~] armpit. kaSawag [kšwk! | N kašaw] tortoise. kašk [АА | N ~] dried buttermilk. kaštīg [Astyk' | N kaštī] boat, ship. tkawādak [kw’tk'] young; baby; v. kodak. ikay [AYM T < А ?уті | N ~] when? 2kay [kd | N ~] title of the dynasty of Wištāsp (patron of Zoroaster), Kayanian. ~ak [-&!] ruler hostile to Zoroaster. kayk [kdyh! | N ~] flea. kë [MNW < A mn-w | M ky, N ki] who, which. P keč [kyc | = P] person, somebody. kéd [ду | P gydyg] soothsayer, magician. ~igih [-ykyh] soothsaying, prophecy. keh [ks | M kyh, N ~] small(er), less(er), young(er). ~tar [-il | N ~] = keh.
493:Р murd [то | P mort !] death. murdan, mir- (YMYTWN-tn! < A ymwtwn, V mwt; mulin' | M murd, myr-, N ~] die. murdār [mwrt?], mwld?l | N ~] carrion. murnjénidan, murnjén- (mwlncyn-ytn'] destroy. murw [mwlw! | M mwrw, (N mury)] bird. murwāģ [mwlw’k' | M mwrw’, N murwd] omen. murwizag [mwlwyck'] little bird. murw-nīš [mwlwnys] augur, soothsayer. must [mwst'] force, violence. ž*must [mwst'] = must. *must [mwst'] complaint. must|-abarmānd [mwst!’plm’nd] aggressive, aggressor. ~gar [-kl] violent, rebellious, mustómand [mwst?wmnd | N mustmand] complaining, unhappy. ImuSk [отео | N ~] musk. 2mušk [mwsk! | (N mis)] mouse, rat. must [mzvšt! | N ~] fist. muštan, māl- [mwéstn', wl- | N ~] rub, sweep.
563:sang 74 sén murw
564:sang [KYPA < A kyp’; CCA (in error); sng | (P?sng), N ~] stone, rock. -~sar [-s?1] stony place. sanj-, v. saxtan. sanwar [snwl = Av. 0anwar-] bow. sar [LOYŠE < A r'šh; sl | M sr, N ~] head; top, summit; end, begin- ning. | sarāsar [s?s] | N ~] from end to end. sard [s/t! | M srd, N ~] cold. ^Àh: coldness. sardag [sltk' = Av. sarada- | (M s’rg), J srdg] sort, kind. sardsér [s/tsyl | N ~] cold region, uplands. sārēnīdan, sárén- [s’/yn-ytn'] provoke. sargen [slgyn' | N sargin] dung, manure. sarmāģ [s/m?k! | N затта] coldness. sarw [slw(b)' | M srw, N ~] cypress. sas [ss | N ~] bug. sāstār [s”st”7 | P s?s?r] commander; tyrant. ~ih: tyranny. Sawah [sw’h = Av. sawahi-] the western continent of the earth. saxt [sQ)At! | N ~] strong, hard, severe(ly); very. “Аһ: strength, severity. saxtag [shtk! | (N saxtiyán)] morocco leather. saxtan, ѕапј- [s’htn', snc- | N ~] weigh. sāxtan, sáz- [s*htm!, ?c- | (P s?*c-), N ~] make, prepare; tolerate. sāxtārīh [Pht yh] toleration, forbearance. saxwan [МРУА < А mly’; shwn' | М sxwn, N suxan] word, speech. say-, v. südan. sayag [sg dk! | M ғур, N sáya] shade, shadow. lsaz- [sc- | M sz-, N ~] be fitting, proper, worthy. --i$n(ih): fitness, worthiness. 26а2-, —išn, v. sazistan, saz-, v, sáxtan. sazāģ [sk | N sazá] fitting, worthy. ~th: fitness, worthiness. ~ ~war [-w/ | N sazāwār] = затар. sazistan, *saz- [sc-stn'] pass. ~išn: passing, transience. ~iSnig : transient, perishable, mortal. sé [3; TLTA < А tl? | M sh, N si] three. sëb [syf | N ~] apple. sēj [sye = Av. 'Gyejah- | N ~) danger, trouble. --ómand [-”zvmnd | N —mand] dangerous. sel [si | N —] spear, javelin. sém [sym | N —] — asém. !sén(ag) [syn(k)! | N sina] breast, chest. *sén murw [synmzlw | (N simury)] a fabulous bird.
894:augur murw-nis.
895:auspicious humurwag.
999:bird murw, way, wayendag; little ~ murwizag ; ~ of good omen humāy; ~ of prey škarag.
2699:magpie kaskén(ag) murw.
2975:omen jadag, jahišn, murwāg.
3066:peacock fra&(a)murw.
3661:simurgh sén-murw.
4644:frašn frašagirdīg frašagird frašamurw fradāg fradom fradomīh pardag pambagén pambag passaxt passáxtan passox passáz- passāzišn pasen pasēmāl pasēmālīh brin-t bridan™ passazagih passazag past, pist pistag
4808:sen murw sezd sézdén haftād*
4853:[138] mese murdir aay’ AV murwag 26 morwārīd -O*6 murwizag _ m» 55 murw wy Ww $6 murwnīš we NV 5G murnjén- 51136 murnjēnīdan 131936 mērd, murd
```


## [2026-09-07T16:25:47.326Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### NYB framōš / murw\"\ngrep -n -i \"framōš\\|framoš\\|fram6š\\|frāmušt\" NYB_vol2_glossary.txt | head -10\necho \"--- murw\"\ngrep -n -i \"^murw\\|murw \" NYB_vol2_glossary.txt | head -10\necho \"### SOD mrγ\"\ngrep -n \"mr'γ\\|mrγ\\|mryγ\\|bird\" SOD_pages.txt | head -20"
}
```


### [2026-09-07T16:25:47.402Z] TOOL RESULT

```
### NYB framōš / murw
2493:"maškar enemy, the probable Ir. eguiva- lent of OAram Š'NH = SANE ‘hater’ 12812; inFrP 14 ~ is the Ir. equivalent of MSN’ = MSANNE, pt. Pa‘el of the same vb. in its recent form with S instead of S. — In all probability the same as Av. (1153) maršo.kara- left without trans- lation by Bthl, but certainly ‘killer’, one of the three epithets of Verethraghna Yt.. 1428: maršo.kara- arsö.kara- frašo. kara- which correspond to the Milr. epi- thets of Zurvàn: asögar frašogar zarogar, the last meaning 'making weak, slack' and rendering marsö.kara-. Ci Nyberg, . JA 214, 1929, 240, 219, 1931, 86-91. OIr marša- must then mean 'weak' slack’ (etymology obscure; to be com- bined with Skr mrs-. v.s. v. framoš?) and maršo.kara- ‘making (the limbs) slack’ = ‘killing’, ef Hom. Xdot oi yvia ‘he
--- murw
### SOD mrγ
6344:      bird ry   ©-\ pred. inst. ^mry1                                       amyamand ?                                        JfL
11728:                                                                         bird, flying parwazane (brwz'ny)
19259:             bird                                                              "Adam's apple", Sogdica. 56, 29; Benv. Notesiv
30072:      mynah birdioleaster- fruit piercer)                              9146 -s
37753:(to)bc purified    1308                   bird 901,2793,5432                     (to)blush 9251, 9398
38900:                                                                                mynah bird       9134
```


## [2026-09-07T16:25:56.814Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *5432\\|^ *5432 \\| 5432 \" SOD_pages.txt | head\necho \"--- around 5432 entry\"\ngrep -n \"5432\" SOD_pages.txt | head -5\necho \"--- 901 and 2793\"\ngrep -n \" 901 \\|^ *901 \" SOD_pages.txt | head -5"
}
```


### [2026-09-07T16:25:58.087Z] TOOL RESULT

```
19255:       5432 mry-' B, M, S                      «x>t ^
--- around 5432 entry
19255:       5432 mry-' B, M, S                      «x>t ^
37753:(to)bc purified    1308                   bird 901,2793,5432                     (to)blush 9251, 9398
--- 901 and 2793
6342:901 Wy-     B                                                         915 'my'nVnt B
```


## [2026-09-07T16:26:02.343Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '19245,19275p' SOD_pages.txt\necho \"=== which leaf\"\npython3 - <<'EOF'\nt=open('SOD_pages.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if '5432 mry' in p:\n        print('leaf(0-based)',i,'printed approx',i-66)\n        import re\n        print(re.findall(r'\\[pdf page \\d+\\]',p)[:2])\nEOF"
}
```


### [2026-09-07T16:26:03.839Z] TOOL RESULT

```
       5420 mrc JJnd^ M              J ' ^ o/ jU* i^\ tSj*                           GMS 485, 526, 1661; Hen. Cosm. 307, 35; MDii
            marc(e)-J3andam (mrc(y) bnd>m)
■iM                    mm*
 i
       in
                                                                                                                          mrt'ny'kh
               -v. A-5, 15; MDii pl84, 15; mrYy> Frag. Len.
               68.13; C2, 11R24
                                                                             maryunde (mrywntk) ©pi -/ ^mry'wnt'k
                                                                             lump, clod, ball
       5432 mry-' B, M, S                      «x>t ^
            mry, mary ©Av. mdrdYa ©nom. ob. -y; inst.                        GMS 138, 149; Hen. Tales. 485 n 7; TSP 3.290-5,
                                                                               2 pi. mrYwnlU TSP 3.290; YrS mrYwndyy
               -)()); pi. mrY^ysi ^'mry-
             bird                                                              "Adam's apple", Sogdica. 56, 29; Benv. Notesiv
                                                                               499
             GMS 485, 1174, 1182; TSP 2.155, 456, 3.139, 189
               & etc.; BSTBL; SCE; Frag. Len.; BBB; SCE 105,           5442 mrywntk          B =* mrywndy
               252, 270; BBB 511; GMS 1240, 1186; Frag. Len.           5443 mrywr C                                  (-jy^jTlT^j
                                                                            maryur/I
                                                                                egg
               29.4, 71.12: O3 12, 84a 10
                                                                            twisted locks, curly hair
       5433 mry-3 B                       jljipL^iJj**
            marx ©nom. -y; ace. -w =*mrx-                                   Sund. AoFviii 1981, 25R 5 p 191 n 238                     >SJ
            straight, flat            v                                5444 mryyz'tkZ-y B                            Mj^t-'r*
            GMS 491, 520, 1191; SCE 65; VJ 1497; BSTBL,                     morye-zate
              Dhy. 18; TSP 5.28, 54; adv. "equally" TSP
              2.870, 3.248 n pi 99, 7.21                                    BSTBL, Vaj. 2, Dhu. 38; Benv. Notesiv 497

      5434 mry* B                  (^)fV'j'>y^                              MRK* -»MMLK(>)
=== which leaf
leaf(0-based) 283 printed approx 217
[]
```


## [2026-09-07T16:26:10.028Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8').read().split('\\f')\np=t[206]\nprint(p[:2500])\nEOF"
}
```


### [2026-09-07T16:26:11.339Z] TOOL RESULT

```
h. kilpet ‘womb’, OE cild ‘child’, etc. Walde-P. 1.614. Falk-Torp 593, 430. Cf. ON hiann ‘block’ and ‘young bear’, NE cub: Norw. kubbe ‘block, stump’.
5. Lith. kumelys, Lett. kumelg, see 3.41, under ChSl. konji.
6. ChSl. Zrébe, etc., the general Slavic word : Grk. Bpédos ‘fetus, babe, young of an animal’. Walde-P. 1.689. Briick- ner 666.
7. Skt. kigora-, etym.?
CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
172 SELECTED INDO-EUROPEAN SYNONYMS
3.46 ASS, DONKEY
Grk. —bvos -Goth. asilus Lith. asilas NG = yatdapos, yatdotpl ON asni Lett. ezelis youdpt Dan. assel ChSl.  osilit Lat.  asinus Sw. dsna SCr. osao, magarac Tt. asino, somaro OE assa, esol , Boh.  osel Fr. ane ME asse Pol. osiot Sp. asno, burro NE donkey, ass Russ. osel Rum. asin, mdgar Du. ezel Skt. gardabha-, rdsabha- iin asan OHG  esil Av. xara-, ka9wa- Nir. asal MHG sel W. asyn NHG esel Br. azen
The majority of the European words for ‘ass, donkey’ are derived, mostly through Latin, from some Asiatic name for this animal, the appearance of which in Europe was relatively late. Other words reflect the function of the ass as ‘beast of burden’, or sometimes other characteristics such as ‘lascivious’ or ‘harsh braying’. Schrader, Reallex. 1.271.
1. Grk. dvos (prob., see below), Lat. asinus, loanwords fr. some Asiatic source, ultimately prob. the same word as Su- merian ansu ‘ass’. Schrader lic. Er- nout-M. 79. Walde-H. 1.72 ff.
Lat. asinus, or in part dim. asellus, is the source of the common European words, the Romance, Celtic, Gme. (ON asni, Sw. asna fr. OF r. asne; Dan. esel fr. LG or HG; OE assa perh. fr. Ir. asan) and, through Gmc., the Balto- Slavic.
2. Grk. évos is prob. fr. the same source as Lat. asinus, though the precise phonetic relation is obscure. The old view that it belongs with Lat. onus ‘load, burden’ (cf. NG youapt, It. soma- ro, below) has recently been revived by Grégoire, Byzantion 13.288 ff.
NG yatdapos, yaidépu, yatdotpr, fr. yatdapioy occurring in pap. of the 6th to 8th cent. a.p., parallel to a gaydor in a 4th cent. Talmudic text, with somewhat
similar forms in other Semitic writings, doubtless a word of Asiatic origin, pre- cise source uncertain. Hatzidakis Mec. 2.560 with references.
NG yopép., fr. neut. of adj. youdprs, deriv. (suffix fr. Lat. -drius) of class. Grk. youos ‘load’. Cf. It. samaro (below, 3), NG dial. Bacrayé(s), Bacrayovp, and goprixe ‘donkey’, fr. adjs. Bacrayés (: Bao- Taf ‘carry’) and ¢opr
```


## [2026-09-07T16:26:16.264Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8').read().split('\\f')\nimport re\nfor i in range(214,221):\n    p=t[i]\n    print('==== leaf idx0',i, re.findall(r'(?m)^\\s*(1[78][0-9])\\s',p)[:3])\n    print(re.sub(r'\\s+',' ',p[:400]))\nEOF"
}
```


### [2026-09-07T16:26:17.507Z] TOOL RESULT

```
==== leaf idx0 214 []
. ci, matad Du. hond Skt. — gvan- Nir. madra(dh), gadhar OHG hunt Av. span- W. ct MHG hunt ; Br. ki NHG hund CC-O. In Public Domain. Gurukul Kangri Collection, Haridwar ee eee i } ! i } ' Digitized by Arya Samaj Foundation Chennai and eGangotri ANIMALS 179 -_ the earliest and most wide- 5. OE docga (once, in a gloss), ME he dog is stic animals. Evidence dogge, NE dog, orig. unknown. Dis- read of a
==== leaf idx0 215 ['180']
, MHG zohe, NHG dial. zope, zauche, perh. as orig. ‘bearer’ : OHG ziohan ‘draw, nourish’ (Walde-P. 1.781. Falk-Torp. 1297). Lith. kale: Ir. cuilén ‘puppy’, ete. (3.612). Among others, either of imi- tative orig. or obscure, are Fr. lice (now obs. or dial.), Br. gart, ON tik, Norw., Sw. dial. tk, Lett. kun’a, Boh. cubka, Pol., Russ. suka (see above, 1). CC-0. In Public Domain. Gurukul Kangri Collec
==== leaf idx0 216 ['181']
chorro, of Basque orig. REW 5959a. Diez 435. Sp. perrillo, dim. of perro ‘dog’. 3. Ir. cuilén, etc., above, 1. W. cenau, ceneu ‘puppy’ and ‘lion’s, wolf’s cub’, etc. with Ir. cano ‘wolf’s cub’ : Skt. kanina- ‘young’, Grk. xacvds ‘new’ (14.13, 14.14), also prob. ChSI. stene, etc. (below, 6). Walde-P. 1.398. Pedersen 1.121. 4. ON hvelpr, Dan. hvalp, Sw. valp, OE hwelp, ME whelpe, NE whelp (now arch.
==== leaf idx0 217 ['182']
 irs, as clearly in Aris- toph. Ach. 879. As domestic cat evi- dently in Aristot. HA 540510, Plut. Mor. 2.144c, and later, until the word was replaced by xarra, quotable from 6th cent. a.p. 2. Lat. félés, possibly : W. beleu ‘mar- ten’. Walde-P. 2.177. Walde-H. 1.474. In Plaut, Rud. 3.4.43 ‘mouser’, prob. CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar aa a Sel Digitized by Arya Samaj 
==== leaf idx0 218 []
de-P. 2.312. Er- nout-M. 645 f. Grk. pis; Lat. mis; ON, OF, OHG mus, ete., all the Gmc. words; ChSl. myst, etc., all the Slavic words; Skt. mis-, NPers. mug; Arm. mukn; Alb. mt. 2, NG movrixds, pop. movrix, fr. pds Tlovrixos ‘Pontic mouse’ (Aristot. HA 600°14, Pliny 8.82, etc.). 3. It. sorcio, Rum. goarece, fr. Lat. sdrex ‘shrewmouse’. Fr. souris fr. *soricius. REW 8098, 8101. It. topo ‘mouse’ or 
==== leaf idx0 219 ['184']
231, Peg, Terenat, ete. Walde-P.| 6. Skt., Av. vi- : Lat. avis (above, 2). Br. ae ee on Skt. paksin-, deriv. of paksa- ‘wing’ algo “infutions Br. lapous ‘bird’ but | (4.392). at. a eet and so prob. fr. Av. maraya- used of large birds ‘locust’, with us. locusta (‘lobster’ and) | (Barth. 1172), NPers. murgh ‘bird? : f unexplained p for ¢ as in | Skt. mrga- ‘wild animal’ (3.11). CC-0. In Public Domai
==== leaf idx0 220 []
adr, fiskikarl Lett. zvejnieks, zvejs Lat. piscaior Dan. ker ChSl. rybart It. pescator Sw. _ fiskare SCr. ribar Fr. pécheur OE jiscere Boh. rybd7 Sp. pescador ME sfissher Pol. rybak Rum. pescar NE fisherman Russ. rybak, rybolov Ir. tascach Du. _—visscher Skt. kaivarta-, dhivara-, Nir. iascaire OHG fiscari matsyajivat-, etc. W. pysgolwr MHG vischere Br. pisketaer NHG fischer Nearly all the words
```


## [2026-09-07T16:26:25.039Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mar.ya-\\|mereya-\\|m.r.ya-\" BRT.txt | head -10\necho \"=== saena\"\ngrep -n -i \"saena\\|saëna\\|saöna\\|sacna\" BRT.txt | head -20"
}
```


### [2026-09-07T16:26:25.127Z] TOOL RESULT

```
19936:•  ].,  p.  "mar-  V.  'sterben*.  Piaes.  27 mirya-'^,  mariya-; s-Aoi.  i  mari-, —  PPfP. varyta-;  PFP,  'imrt'^wa:  —    Vgl.    noch
=== saena
3658:•  j.  ap«m9n),  g.  ap3ni9m  Adv.:  s.  apma-, ■  j.  a-p9r9tö.tanü-  Adj.  'auf  des  Leib kein  Makel  haftet,  makellosen  Leibes"*: Aagat^rnt  gavam  axsaenanqm  'nunqnt  V. 22.4.
8416:•  j.  upäiri.sacna-  Adj.,  Plur.  mit  iikata- (5d.)Name  eines  Gebirgszugs:  ahmat  hala
17842:xSaena-  1)  Adj.  (fem.  -«r-)  'aus :i'  anhat  zarpnainisi^sA.)  , ,  'ia^iis
21092:{ia)  fa  ätt  liahim,  Sü. :  niam*,  yadi  dSaena, tvam  tiiyä  dityä.
25786:•  j.  'saena-  m.  Name  eines  grossen  Raub- vogels, wohl  des  Adlers:  ya'äia  Aau  masa m»rrfll  'nS  Yt.  l4-A^s  —  "/"^  avqm  vartam yqm  •nake..yä  vaoh  vTspS-^i/ (sd.)  aama YL12. 17.
25788:I  j.  'saena-  m.  EN.  eines  GIäiibigen*>: 'nahe  ahüm.jtütB  asaons . .  yH  paoiryS  saiB.- aghryS  fraxstata  paiti  aya  ama  "des  S., Sohns  des  A.  . .,  der  zuerst  mit  hundert SchUlem  auftrat  . ."  YLy.97;  —  HyrSis ■nahe  "des  Z.,  Sohns  des  S."  Yt.ij.  126. *)  Der  vom  loo.  bis  zum  200.  Jahr  der  lora- %»?/rischen  Religion  gelebt  haben  soll;  s.  DkB. '97  iS-  2.17).  West  SEE.  37.  230,  262,  47.  83.
25794:•  j.  saenay-  i)  Adj.  'spitz'  (nur Komp.).  2)  m.  'Spitze,  Wipfel';  •ni? (AP.)  marnai  umaranqm{sd.)  Yt  14.  21.
```


## [2026-09-07T16:26:31.385Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"m.  'Vogel\\|'Vogel'\\|Vogel\" BRT.txt | head -20"
}
```


### [2026-09-07T16:26:31.455Z] TOOL RESULT

```
5799:•  j.  asta'va-  Adj.  'mit  einem  Knochen Teisehcn';  °v3  vä  taxmahe  mirr/ake pars- nai'SvS..  "wer  einen  Knochen  des  starken Vogels  oder  eine  Feder  (als  Amulet)  trägt .." YL/4.3(S.
6419:*)  So  nach  Sd.  14-  8,  der  Riv'.-Stelle  bei Sp.  Komm.  /.  374  (mur-/  i  hi  eiefd  x'änand) und  SWienAW.  6/.  839.  2\.  Dem  Vogel  werden die  abgescbniUenen  Nägel  überwiesen;  sie  bilden xeine  WaiTen  gegen  die  D(ü-um,;  s.  V.  //.  9  und Bd.  ig.  19  r,
9251:srayä  voumkaiaya  Y,  65. 4;  —  ys  haaiay-j  S/-'^v^'^'jU^'ond''zD"'"w',/irLter ...va  uruassayat  '«o»  Yt,5.  131;  —  ^-i  HriÄ^-^  No^T).  -  mp,  fl'ü.  Tu  V.'s  49" rasmanS  hqm.ststse  (sd.)  ^5  ^'na  ">  J'  karkäi,  vgl.  np.  (Npa,)  kargas. iHndayänti  Yt,  jj.  39;  —  yaoz)nH  »aA'«j.*kahrkäs5.parana-"  Adj. 'mit  Federn •«ff  (NP.)'>  rasmans  Ytio.36.  2)  zeitlich  ^  des  (Vogels)  Kakrklsa  versehen':  isunqm (nur  Komp.).  ^-paranum'^  Yt/o.isg.
9369:•  j.  karäiptar-  m.  Name  eines  Vogels, I 'accipiter'*' ■':   kö  avalia  dainqm  mSzda-
9370:' yasnim  vT.barat  altaShxi  varpf^a  yd  yitnö I  ksrsnaoti  .  .  vti  'ta  "Wer  hat  dort  , ,  ver- breitet? ..  Der  Vogel  K."  V.2.  42.
11821:Vgl.  'laxl;  —  ai.  taili  'er  schiesst  dahin' (Vogel,  Wasser),  np.  läzad  'et  läuft,  er  lisst laufen'!);  ksL  It/rtü  'er  läuft,  fliessl'.  —  I'ü.: lacitan,  (lU  V.  2):  taeenUaii;  ».  noch  No.  4. — ')  Oder  Kms.  (Praes.  30)?  Aber  auch/ro- la/al  hat  kaus.  Iledeulung,  und  ebenso  toxi-. VglT  im  Übr.  Bthl.  IF.  /.  489.  —  »)  NA. fruilacS.  —  3)  Man  erwartete  V»«?/«;  vgl. BTHU  KZ.  39.  563.  —  4)  Pii.:  ape  tn£  il (statt  la/ilf\  etl. :  ai  apäk  apr  iautl.—Si  Weitres beiFRMÜLLER  WZKM.  //.  285.  —  *>S.  'i^aij-No.
11903:tqm  vanqm  aiiti  "es  stirbt  da  ein  Mann da  fliegt  ein  Vogel  auf  .  .  er  frisst  den Körper  an  . .  da  fliegt  der  Vogel  (wieder) auf  . .  Da  macht  sich  ein  Mann  auf  .  . er  geht  zu  dem  Baum  . ."  V.3,if.;  — nil  t"  äpim  hituaiü  avi yavB.caränJm  (sd.) V.5.5-
11991:so  gross  als  der  Leib  dieses  meines  Vogels,  ^^omäi  Y.  //_.  7;  —  fravaM  . .  taxmä  .  .
11994:OWörtl.:  Leibesgrösse  dieses  Vogels    —  mihrftH    ..    'tanam    asti    °l3m     (statt
15705:'na  lanQm  aiwiM/äis  ana  'na  kamjrykjm paiH.saaAa^a  "eine  Feder  des  Vogels  V. sollst  du  dir  suchen,  mit  dieser  Feder sollst  du  über  deinen  Leib  streichen*', mit  dieser  Feder  deinen  Feind  bannen" Yt  74.35.  !*)   'Flügel':  ya^a    max^ä
17662:•  j.  fra'pt«r9-Jät-  Adj.  '(im  Flug  sich  be- wegend, FlUgeltier,  spez.)  Vogel';  vtspamca gqm  .  .  'jätqmca  (ASf.) "'  ravascaratqmca Y.  77. 9;  —  dsmqn  .  .  yäca  °jqn  (APn.)'* yäia  ravascarqn  \k.8.^Z\  —  ratavB  -jäta (APm.)  .  .  ravascarata  Vr.  2.  i ;  —  ratavS 'Jafqm  (GP.)  ..  ravasäiratqm  Vr.7.  i,  Yt
17664:*)  Als  Ralav  der  Vögel  {iiäyaHdakän,  mumän) wird  Bd.  34.  1 1  und  Vr.  /.  i  Pü.  der  Vogel KatUpt  (zn  Bd.  3^  11 :  karUpt  kc  larx  :fännid-, Sp.  458  m.),  aber  Bd.  34-  ag  der  Vogel  Camri! genannt;  s.  noch  Mx.  6z.  9  und  WCST  SBE. 24.   lOg.
18969:•  j.,  g.  'namah-  n.  'Verehrung,  Ehrerbie- 1 tung,  Huldigung,  Ehrfurcht{sbezeigung)':  | parinavö  .  .  m^vyaAe  .  .  patmrva  hl  °mö  '■ baraiti  paourva  sfartnä  "wer  eine  Feder  \ des  . .  Vogels  hat,  der  gewinnt  sich  zuert Huldigung  .  ."  Yt.  14.  36;  —  sonst  nur  in ' Beziehung  auf  Gottheiten  gebraucht:  haomö .  .  yakmäi  kvan  .  .  dural  'mS  l/ao6ayeiü  1 Yt.  jo.  90;  —  namistaAyä  {sd.)  °maaAä'^ fiii  .  .  paitJ.jamyä  Y.jß.s;  ~~  tat  vS  11}  \ hazaosanks(f.d.)  . .  daiäySi  savH  ahm  vohü\ manatihä  .  .  yaz:>mniN/iS {sA.)  °mai^h3''*\ Y.j/.  20;  —  at  töi  myazdtm  ..  'maahä^ .  .  däm3  (sd.)  y.^^.  3;  —  tsm  ttS  staotais 'maahS  ^a.vlvanlö  (sd.)  Y.  45-  8 ;  —  'maaka  ' aoara  data  ajasani  upara  data  Yt.JO.  118; 118;  —  mi%rim  . .  pairi.jasäi  vantaca 'maahaca  Yt/o.  6;  —  kn  nS  (näml.yVa- Tialls)  stavät  .  .  asa.näsa  "maaha  Yt.  /J. 50; —  'maAT  fySntä  *akura.mazdä  'mahi (LS.  als  Inf)  usSmahi  'mat»ki  (DS,  als Inf.)  vTsilmaidJ  "wir  haben  Freude  an  deiner Verehrung,  o  AAM.,  wir  wünschen  (dich) zu  verehren,  wir  sind  bereit  (dich)  zu  ver- ehren" ^.58.  3JI;  —  mit  Dat  des  Gottes, dem  die  Huldigung  gilt:  'matgkä  a/ni  . . avat  ituyl'^.  12.  3;  —  a/  3  %waAmai  äkre rtltqm  (sd.)  'manAS  .  .  Y.  4j.  9.  a)  bes. NS.  in  elliptischen  Sätzen«;  der  Name  der Gottheit  folgt  im  a)  Vok,:  °m^  urvaireV. ig.  18;  YLi.  21;  —  'num^l  kttvatm  y^arms Yt  /.  2 1 ;  18.  7.  b)  Dat  oder  Gen. :  'mB ahuräi  mazdai  °mS  anDsaHbyH  sp^ntaeibyS *mS^  .  .  'ms  gsul  'mS  gayehe  'mS  lara- "kusirahe ..frava^e  'mstn^'^  vJspayh  afaonS stBis  Y.  68.  22;  g.3,  16,  JO.  13, 17',  2o',Yt /.2iJ,7.iS,  JO.91, V./5.25';  — gave  am^m gave  'm?mi*  Vt/i^.  61,  c)  Vok.  hinter dem  enkl.  Dat-Gen.  des  Fron.  2.  Person: n;mas>  ti  aAura  mazda  .  .  'mB  vS  amf^ä spinta  Ny.  /.  1 ;  j.  4,  Y.58. 7,  V.  21. 1*;  — •mS  vS  gaha  alaonilY.  28.0,  43.  o,  47.0, ^i.o,  SS-o-  d)  Lok.:  'mir  airyene  vai- JaAi  Ytl.21.  OhneWert:  'ttU!  tistrim
20365:•  j.  m^rwa-  m.,  n.''  'Vogel',  spcz.  von grösseren*':  S  tat  °y?m  (NS.)  uzvazaite haca  .  .  "es  fliegt  dann  ein  Vogel  herauf aus  . ."  V.5. 1;  i;  —  aai  %wa  (nämL haomtm)  .  .  spitUa  fradaxita  -fa  (NP.)  .  . vJbarm  Y./0. 11;  —  upa  tarn  vanqm aiiti  yqm  ks  'ys  "er  geht  hin  zu  dem Baum,  zu  dem  jener  Vogel  {zuvor  ge- flogen war)"  V.  5.  3^';  —  iaxmahe  'yahe Yt. /4.  36';  —  'yahe  parmS  tmnyanqm Yt  74.36;  — ydha  na  'ys  huJ>armB{si.) Yt  13. 70.  A)  mit  Gattungsbestimmung: hau  maza  °ys  saenS  {sä.)  Yt/4.41;  — °yahe  k>hrpa  üahriasahe  (sd.)   Yt5.  61;
20369:ai.  mfga-m.  'Waldtier'  (Gazelle),  auch'Vogel'; np.  murf  'Vogel;  Huhn'.  —  Pü. :  mun:  — ')  Nur  für  V,  J.  1  gesichert;  s.  Db».  VglS. /.  129.  —  »)  Wie  Adler,  Geier,  Hubn;  im Gegensatz  zu  iv^-.  ~-  J)  Im  Nebensatz  fehlt das  Verbum ,   etwa  ufia,'iyäya.
22133:barsein,  sva.)  so  dass  es  gesehen  werden kann,  sichbarlich,  vor  aller  Augen' :  V  ahmat haca  i^arfttS  mgrrjahe  Afhrpa  frasusat "sichtbarlich  in  Gestalt  eines  Vogels  . ." Yt  j_9.34;  —  v°  ahmat  para  dafva  pataym "sichtbarlich  trieben  sich  vor  ihm  dieZ^cffu herum"  Ytiß- 8o'>;  80'.
23501:•  j.  vär«n-gan-  m.  Name  eines  Vogels*': msn-jahe  . .  'nn/tnahe'^  par»rum  ayasaisa Yt.  14-  35-
23513:•  j.  vära-gan- :  °jn-  m.  Name  eines Vogels'*:  afimäi  .  .  ajasa^  vazfmnS  v»r»- %rayne  .  .  niirr/ahe  kthrpa  •ynake'''  . . yS  vayam  aiti  asUtS  Yt.  i^l.  19;  —  lusai il'arynS  yimai  kaca  . .  mirriahe  kthrpa -ynahe''^  Vt /p.  35.
23514:Vgl.  värin-gan-.  —  Eig.  Bed.?  Man^  hat  den Vogel  Damen  mit  'flügelschlagend'  überaetit nnd  für  *3i'J/'-  auf  np.  fj/ 'Feder,  Flügel'  nnd ai.  J-äta-  m.  verwiesen;  5.  Sp.  Komm.  3.  1Ö4, Heu.  KZ.  27.  607.  Aber  ai.  vära-  bedeutet 'Schweifhaar',  bes.  des  Kosses  (wie  lit.  ialtd), und  np,  bäl  ist  vielmehr  gleich  ai.  barha-  [v') 'Schwan ife der"  lu  seWen,  Ander»  jetii  Richtir IF.  p.  185.  —  Npü.:  fehlt.  —  II  Welche»? Falsch  Dst.  ZA.  z.  566;  vgl.  Hbm.  PSi.  87. HoRN  GlrPh.  7  b.  56.  —  '}  Them.
24521:♦)  Vgl.  Mx.  62.  37;  "das  Neit  des  Vogels Sin  (tinmurv)  ist  auf  dem  Baume  1  j/u/itl  1  Aar' vis/  ISxmai";  Bd.  g.  5;  "der  Baum  i  harvisp töxmak   steht   im  See  frai^kni-i",   18.  9:    "den
```


## [2026-09-07T16:26:44.982Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(len(t))\nfor n in (667,668,669,670,671):\n    p=t[n-1]\n    print('==== leaf',n, 'has سیمرغ:', 'سیمرغ' in p)\n    print(p[:200].replace('\\n',' | '))\nEOF"
}
```


### [2026-09-07T16:26:46.272Z] TOOL RESULT

```
684
==== leaf 667 has سیمرغ: False
   ‫—‬       ‫شا‬                                                                                   ‫سسموبه‬ |  | ‫وبتحتالی زده ‪ ۰‬چیزیت از اسرون‌آلات کومفند‬                  ‫ابن لفت هم درمجمع‌الفری سر
==== leaf 668 has سیمرغ: False
  ‫ی‬                                                                                                ‫ات‪۷‬‬ |                                                                                            
==== leaf 669 has سیمرغ: True
‫ودرین روز گوشت وسیر برادر پیازخورندو گویند‬               ‫رگاعی ئىز هت که سوسته در آبرای استاده‬ |  | ‫که خوردن‌آن ايمن بودن ازمس جن است‌وجن‬                                   ‫حیض را‬        ‫روبد و خو
==== leaf 670 has سیمرغ: False
  ‫حسدان‬                                                                                                  ‫ت‬ |                                                                                          
==== leaf 671 has سیمرغ: False
 ‫==‬                                                                                               ‫ستیاره با‬ | ‫و بنون زده» لوعی از گیاه باشد مانند فرتالعن‬                       ‫پنج الگشت است واآنر
```


## [2026-09-07T16:26:49.505Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\np=t[668]\ni=p.find('سیمرغ')\nprint(p[max(0,i-1200):i+1500])\nEOF"
}
```


### [2026-09-07T16:26:50.827Z] TOOL RESULT

```
‬‬
 ‫(وز چهاردهم )درد بماه‬
                     ‫سور (جشن) ‪ .‬بقول بیرونی کوش روز ر‬
                                                     ‫‪ - ۴‬از ‪ :‬سیر ( وم )‬
     ‫جشنی بوده است موسوم به ‪ ۵‬سیرسور»‪ .‬دراین روز سیر وشراب میخوردند و برای دفع‌ثرثیاطین‬
     ‫سبزبهای مخصوصی بگاوشت می‌پختند «آثار الباقیه ص ‪ ۶ ۹۲۲‬بشتهاا ص‪٩ 4۷۳‬‏ وبنابراین روز‬
     ‫‪E‬‏ اشباع شدن ‪ ۰‬حاامی که از خوردن غذا باندازة‬                      ‫ثست ‪.‬‬    ‫مراه شمسی‬
                                                                                        ‫چهاردهم ه‬

                                                                                      ‫کافی پدید آید ‪.‬‬
                ‫مانده زین کوهه را ميان دوراه‪.‬‬            ‫‪- ۴‬سرمیشتش( گورخر) از ادیمسياه‬
      ‫نظامی کنجوی ‪ « .‬هفت بیکر چاپ‌ارمغان‌ص‪.»۳۷‬‬
     ‫ذر نکرده‌اند و *بپرمان »‬
                            ‫بیروتی و ابن! کفانی در انواع ءاقوت چنین نامی را ک‬               ‫‪۵9‬‬
      ‫و«بهرمانی» را نوعی ازیاقوت بکاردده‌اند ‪ .‬رك‪ :‬فهرست‌الجماهر وفهرست نخب‌الذخائر‪-« .‬یرمان»‬
                                                                ‫‪ 2‬بهرمان » است ‪۱‬‬    ‫ممنی مصحف‬         ‫بهردو‬

     ‫‪ - ۱‬رشیدی کوید ‪ :‬بم‌عنی سیمرغ زیرا که سی رنف دارد و ءولف سراج براواعتراض‬
      ‫کرده وسی را «محضکثرت » دانته است » ولی ابن اشتفاق عامبانه است ‪ .‬جزو اول آن«سی»‬
                           ‫همان است که در ‪9‬سیمر غ > آمده (رك ‪ :‬سیمرغ) وجزو دوم ‪ ۶‬رنگ» است ‪.‬‬

                                                                    ‫`‬      ‫بقیه‌از صفتد‪۳۶۲۱‬‬
       ‫‪ -۶‬پهلوی ‪ ( 701815‬هزواریآن ‪« )7(2)۷015 . 0۳۵05‬بونکر ‪ » ۱۸‬ورك ‪ :‬توما =‬
      ‫کیاحی از نوع سوسنها و دارای چندین جنس مختلف است و بعضی از نهارابرای‌ا‪-‬تفاده‬       ‫‪0‬‬
     ‫ازییازبا برکک میکارند مانند سیرمعمولی ‪ 771۷145.۸‬که کلهای آن‌چتری است‌وسوخ آن‌فطمات‬
      ‫ککللاب ‪۱۸۲-۲۸‬‬    ‫جدا گنه برروی بك طبق قرار دارد و پیاز و موسیر هم از انواع آست «‬
```


## [2026-09-07T16:27:01.150Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nfor f,off in [('BQT_v2_pages.txt',542),('incoming/BQT/BQT_v4_pages.txt',None)]:\n    t=open(f,encoding='utf-8').read().split('\\f')\n    print('###',f,len(t))\n    for i,p in enumerate(t):\n        if 'سیمرغ' in p:\n            print(' leaf',i+1, 'approx printed', (i+1+off) if off else '?')\nEOF"
}
```


### [2026-09-07T16:27:02.533Z] TOOL RESULT

```
### BQT_v2_pages.txt 684
 leaf 137 approx printed 679
 leaf 318 approx printed 860
 leaf 669 approx printed 1211
 leaf 676 approx printed 1218
 leaf 677 approx printed 1219
 leaf 678 approx printed 1220
### incoming/BQT/BQT_v4_pages.txt 553
 leaf 195 approx printed ?
 leaf 308 approx printed ?
```


## [2026-09-07T16:27:05.956Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('BQT_v2_pages.txt',encoding='utf-8').read().split('\\f')\nfor n in (676,677,678):\n    p=t[n-1]\n    i=p.find('سیمرغ')\n    print('==== leaf',n)\n    print(p[max(0,i-600):i+900])\nEOF"
}
```


### [2026-09-07T16:27:07.222Z] TOOL RESULT

```
==== leaf 676
                                   ‫بروی زمن آمد‪ ».‬و ایز در دشکرد کتاب‬
                                                    ‫صل ‪٤۲‬‏ بند ‪ ۷۱‬وی اشزاگردان‬
                                                                             ‫نفهم‬
                                                    ‫زرتشت ممرفی شده ‪ .‬محققان کلمه سنه‬
                                                   ‫را دراوستا بشاهین وعقاب ترجمه کرده الد‬
                                                   ‫ویا ‪( 028۵۲2۷‬اوستابی) بکی‌دانته‌اند‬
                                                    ‫ونی شك‌بین دومفهوم‌سشةاوستابی وسیمرغ‬
                                                   ‫فارسی ‪ -‬بعنی‌اطلاق آن برمرغ مشهور وام‬
           ‫سیمر غ واژدها ‪ -‬اثر ی ‪ .‬درورش‬           ‫حکیمی دانا_رابطه‌ای‌موجود است‪ .‬میدالیم‬

  ‫که درعهد کهن روحانیان و موبدان علاوه بروظایف دبنی شغل پزشکی میورزیدنده بتابرین تصور‬
  ‫مشود یکی از خردمندان روحالی عهد باستان که دام وی‪-‬مننه‪-‬از نام برنده مزبور اتخان شده‌بوده‬
  ‫سمت روحالی مهمی دائته که انمتای آن خوبی در اوستا آشکار است وازجاب دیگر وی بطبیات‬
 ‫و مداوای بیماران شهرت بافته بود ‪ .‬بعد هاستنه (نام روحالی مذ کور) را بمعنی لفوی‌خود ‪ -‬فام‬
  ‫مرغ گرفتند وجنبة پزشکی اورا در اوستا بدرختی که آشیانة مرغ سنه است در خداینامه‬
 ‫شواهنامه بخود سیمرغ دادند » چنانکه در بهرام بشت بند ‪ ۸۳ -۶۳‬آمده ‪« :‬کیکه استخوان‬
  ‫باپری ازین مرغ دلیر ( وارغن ) با خود داشته باشد هیچ مرد دلیری او را تواند براندازد وله‬
  ‫به در صفح ‪۲۱۲۱‬‬

==== leaf 677
                                   ‫نقه ازصفحة ‪۱۱۲۱‬‬
    ‫سازد‬   ‫بزرگه دارد و اورا از فر برخوردار‬   ‫نزد کان کرامی و‬   ‫بر اورا هماره‬   ‫آن‬



  ‫آری پناء بخشد آن پر « مرغان مرغ » در هنگام برابر شدن با هماوردان خوخوار و ستمکار ‪.‬‬
  ‫داردد گان آن پرکمتر گرد بابند ‪ .‬همه بترسند از کسکه تعوبذ پرمرغ وارغن با اوست‪ ».‬در‬
 ‫میئو گك خرت (یازند) آمده (ترجمهٌ وست فصل ‪۲٩‬‏ بند ‪* :)4* - ۷۳‬آشبان سين مورو(سیمر غ)‬
  ‫هاه سن‌مورو لزآن‬‫بردرخت«هروسپ تخمك» است که آبرا « جدبیش» (گضزدند) میخوانند روگ‬
‫برخیزد هز ار شاخه از آن درخت بروند وچون برآن سند هزار شاخه ازآن بشکند وتضمهایش "‪.‬‬
  ‫ببعد ؛ سیمرغ بقلمدگارنده‪ .‬مجلهة ابران لیکه چاپ‌بمینی‬       ‫فاب ‪۱‬ص‪۲۰۳‬‬     ‫پرا کنده گردد ‪ ۰.‬رك‪:‬‬
                                                   ‫ج ]‪ 11۷۸2‬شمارة ‪۱-۲‬ص‪ ۱-۱۱‬بخش فارسی‪.‬‬
                              ‫‪۴‬‬

==== leaf 678
:‬‬   ‫رك‬   ‫‪-‬‬               ‫«منتپی الارب؟‪.‬‬    ‫باه‌فهان ‪€‬‬


           ‫و باسین معناه با انان او تاسید (‪«)1‬منتهی‌الارب» ‪۰‬‬                  ‫‪ -‬در ‪ :‬سر = باسین ب‬

      ‫‪ - 1‬مسحف سا ( صفت مشبپه از«سنبیدن») و«هوبه سنبا» بمعنی کتف‌سوراخ کن =‬
  ‫همجمل‌التواریخ‬       ‫‪* :‬ویارسبان اورا شایور هو به سنا خوالدندی‪».‬‬                ‫است‬   ‫لقب شایور دوم‬     ‫نوالا کتاف»‬


  ‫‪ = ۹‬رك‪ :‬ممجم‌البلدان‬
                                ‫‪ - ۸‬سینافام جدچهارم شیخاست‬                   ‫سینه(ه‪.‬م‪.).‬‬   ‫‪=¥‬‬       ‫والقصصص‪۳"٤‬؟‪.‬‏‬

  ‫‪°1‬‏ = ‪ ٩10 600‬از ‪ :‬سن ( رك‪ :‬سیمرغ) ‪ +۳‬دخت ( ر که‪:‬اسشق ‏‪( Y1‬‬                  ‫ورك ‪ :‬طور‪.‬‬
  ‫فریزندی ‪ ۰‬برلی‬ ‫‪۰‬‬ ‫ی‬ ‫ک‬ ‫ل‬ ‫ی‬‫»‬‫ک‬ ‫‪۵‬‬ ‫‪۱‬‬ ‫‪۱‬‬ ‫‪2‬‬ ‫ا‬ ‫ل‬ ‫ا‬ ‫و‬ ‫ن‬ ‫و‬ ‫ا‬ ‫«‬ ‫‪0‬‬ ‫‪5‬‬ ‫ی‬ ‫و‬ ‫ل‬ ‫ې‬‫‪-‬‬‫ي‬  ‫لفة بمعنی دختر سیمرغ ‪.‬‬
   ‫ونطنزی ‪ 805‬د که‪ .‬اص ‪ » ۰ ۹۸۲‬سمنالی ‪. 8015‬سنگری وسرخه‌یی ولاسگرری ‪. 62815‬‬
       ‫ردن وشکم که شامل قلب است ‪.‬‬            ‫شهمیرزادی ‪ 8015‬ک«ه ‪۲ .‬ص ‪ » ۸۱‬؛بضی ازتنه بگین‬
  ‫_ نة الجمن؛ صدر مجلس‪ 2 :‬و آستن‌فراخ می کنند ومب‌شواهند که درسنها فحمنها‬                                 ‫‪۴‬‬

                                                                             ‫بنشینند ‪( » ...‬انجیل فارسی ص‪.)۸۹۲‬‬
      ‫‪-‬کر اول وسوم ‪ ,‬از فرانوی ‪ 8006016‬از بونائی ‪ ( 2016016‬حر کت‬
                                                               ‫س‪#‬ینها ب‬
  ‫آمده) » معرب آن پیز«سیتماه «تفس» ؛ درفراسوی سینماً مشفف سینما توکراف است و آن‬
```


## [2026-09-07T16:27:18.349Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT\nawk 'BEGIN{RS=\"\\f\"} /\\[pdf page 73\\]/{print}' BQT_v4_pages.txt | head -60"
}
```


### [2026-09-07T16:27:19.615Z] TOOL RESULT

```
[pdf page 73]
مرظب -۱۹۹۰-
وآن زباده از نیم شبراز زمین بلند وبفایت سبز | اطیر خوانند ۴ - وکنابه ازآفتاب هم‌هت 8 -
و خرم و درهم روییده باشد ۱ - و لام آشهری | و پنجهٌ زنجبیل را نیز گفته اند یمنی پارچه ای
و مدینه‌ای هم هت ۲ - وعربان خلطیدن ستور | از زنجبیل که چاد شاخ داشته باشد .
راکویند در طفزار وتمامکیاء وطلف را چریدن مرغاب « بنم اول بروزن سرخاب .
وخوربن ۴ - و بفتح اول و ثانی » هم دراعرمی نام رودخانه ات که از پپلوی مروشاهجان
آب دهن راکویند ۴ - وبضم اول وسکون‌نانی» | میگذرد وآنرا مرورود هم میگوبندیمنی‌رودخانهٌ
معروف است که مطلق پرندگان باشد و عربان | مرو ‎٩‏ .8
۱ - ر4 : مرغزار » معرب مرخ « مرج » » اوستا- ۳387884 ( چمن ) » آرمنی ع
8 (چین) » سربانی ع 462۹۲27 (چین)»کردی ۰۲۵1۳۴ ۳336۲802 (چمن)
« اسشق ‎٩۷۵‏ قاط » ورك : هوبشمان ایضاً . درعربی نیز « مرخ » «منتهی‌الارب» آمده :
بله کرد ازآن سوکه بود آب و مرغ پیت از بر دامن ربگه ورغ .
و رك : مرغزار . آسدی طوسی « لغت فرس ۲۶۱ 4.
۲ - مرغاب ( بفتح اول) قربه‌ایست ازهرات وازقرای مالین - ونام نهری بمروشاهجان-
و لهری بسره «ممجم‌البلدان» رك:می‌غاب- « مغ سپید » موضمی‌است درهرات. رك : چهار مقالةٌ
عروضی‌طیم نگارنده س٩4‏ . ۴ - مرغ بالفتح » آب دهان روان»... گیاه ترچریدن, جای
کرفتن درکیاه و غلطیدن درآن « منتهی‌الارب >. ۴ - پپلوی 32۳۷ ( پرنده » مرغ ):
اوستا 339798108 ( پرنده » ماکیان ) « بارتولمه ۱۱۷۲ * « نیب رکه س ۱۵۳ ۰ نیز پپلوی
۲85 , هندی باستان -12788 ( حیوان جنکلی » مرغ ) » قس : کردی 1331۳21۷1 (اردك).
افغانی ۳2788۸ . استی 122۳80 . ( پرنده ) . بلوچی ع (9) 22078 ۰ 1331۳80 ( پرنده »
مرغ خانگی) » مازسرانی ۳38788 « اسشق ۹۷۵ > - درفارسی نیزبمعنی مرغ خانگی(ماکبان)
استممال شود .
* - نو دعی سبح را شب افروزی روز را مرخ و مرغ را روزی .
نظامی کنجوی « کنجینةٌ کنجوی ص ۱۶۲ *.
‎٩‏ - باین معنی در ممجم‌البلدان بغتح میم‌آمده‌است ولی مینورسکی ۸117813410 ضبط
کرده‌است ر4: ترجمةٌ حدودالعال. فهرست .- مرغاب جنم‌ميم مر‌کز ناحیتی‌است بنام مشهدمرغاب
در فاری۷ بفاصلةٌ 2۸ کیلومتری استخر و بکی از قرای آن مشهد مادر سلیمان است . «کیهان .
جغرافیای سیاسی ص ۳-۲۲۲ و رك : ح۲.
۶ مرغالی - بنم اول » از : مرغ ۳ آبی ( منسوب
به آب ) » زباکی 33۳882۷1 ( اردك) « کربرسن ص۸۷ > ۳۹
کیلکی 1ط3طع ۳ ( مرغایی ) » نوعی از پرندکان پرده‌دار ۹
که قم اهلی آن اردك است . و غالباً در آب زندکی میکند . ۳
منقارش پهن و درکنتاره دارای قیغه های ریزبست که آیرا ماش
الك خارج میکند و ذرات غذائی را نگاه میدارد . مرغایی
```


## [2026-09-07T16:27:29.534Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8').read().split('\\f')\np=t[160]\nprint(p[:200])\ni=p.find('murw')\nprint('---')\nprint(p[max(0,i-800):i+800])\nEOF"
}
```


### [2026-09-07T16:27:30.993Z] TOOL RESULT

```
rms "wnyt', ’wnym = nët, onem are only found in some MSS, and wanting in most; they
are secondary formations (for *önayet |
ete.), önitan having been associated with the numerous vbs. in -itan. The Pa
---
rms "wnyt', ’wnym = nët, onem are only found in some MSS, and wanting in most; they
are secondary formations (for *önayet |
ete.), önitan having been associated with the numerous vbs. in -itan. The Paz. readings qnaióan qnaédan seem to be influenced by nayitan.
öpär- [’wp’l-] pres. to swallow 7216; the pres. stem used in compounds: asp ~ mart ~ swallowing horses and men 31". — MPrs ’wb’rdn (A-H I); Paz. pres. hu- pared; NP aubüstan or aubdridan; < Olr *qva-pärayati, caus. of ava + Av. (851) 4par-.
ēpastan [wpstn'; NPLWN-stn'] öft- [wpt-] to fall, in all senses; to set, of a star 510; ka-t cašm 6 zräi ēftēt when thine eye falls upon the sea, when thou catchest sight of the sea 672; hac . .. 60... 926, 2219-20 ete.; pat rod öpast he fell prone (making rpocxuvnov) 11%, eto.; -ka Átur yazét a
```


## [2026-09-07T16:27:36.503Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"murw\" NYB_vol2_glossary.txt | head -10\npython3 - <<'EOF'\nt=open('NYB_vol2_glossary.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'murw' in p:\n        print('leaf(0-based)',i,'printed',i-8)\nEOF"
}
```


### [2026-09-07T16:27:37.761Z] TOOL RESULT

```
2595:murvik [mwlw'k] an augury, an omen 181. - MPrth mwrgw’g (S); MPrs mwrw’; nyw-murwh ‘of good augury’ (A-H II); Paz. murväi; NP murvà.
leaf(0-based) 148 printed 140
```


## [2026-09-07T16:27:50.958Z] TOOL CALL #66: Bash

```json
{
 "command": "sed -n 1,50p /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-07T16:27:50.990Z] TOOL RESULT

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
```


## [2026-09-07T16:27:57.614Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://en.wiktionary.org/wiki/خاموش\" \"https://en.wiktionary.org/wiki/فراموش\" \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mers-\" \"https://en.wiktionary.org/wiki/مرغ\" \"https://en.wiktionary.org/wiki/سیمرغ\"; do\n  python3 tools/fetch_source.py \"$u\" --note \"page 336: Mer 3 / Mereğa verification\" \ndone"
}
```


### [2026-09-07T16:28:04.362Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/8c822745e57a063c.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f0e8a23c73545e28.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/73e12d933f62d008.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/d2cc991adb956e6f.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/221dca62bcc95883.txt
```


## [2026-09-07T16:28:07.586Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### خاموش\"; grep -n -A25 \"Persian\" 8c822745e57a063c.txt | grep -i -B3 -A18 \"etymology\" | head -60"
}
```


### [2026-09-07T16:28:07.642Z] TOOL RESULT

```
#### خاموش
82: Toggle Persian subsection 
83-
84- 2.1 
85- Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Adjective 
92-
93- 2.3.1 
94- Alternative forms 
95-
96- 2.3.2 
97- Derived terms 
98-
99- 2.3.3 
100- Descendants 
101-
102- 2.4 
103- References 
--
251: Persian
252- [ edit ] 
253-
254- Etymology
255- [ edit ] 
256-
257: From Middle Persian hʾmwš ( xāmōš , “ silent ” ) , perhaps from Proto-Indo-European *mers- ( “ to forget ” ) ; cognates include Latvian aizmirst ( “ to forget ” ) . Compare also Old Armenian համր ( hamr ) .
258-
259- see also the verb form خاموشیدن . 
260-
261- Pronunciation
262- [ edit ] 
263-
264: ( Classical Persian ) IPA ( key ) : /xaː.ˈmoːʃ/ 
265-
266- ( Dari, formal ) IPA ( key ) : [xɑː.móːʃ] 
267-
268- ( Dari, formal ) IPA ( key ) : [xɑː.móːʃ] 
269- ( Kabuli ) IPA ( key ) : [xɑː.móːʃ] 
270-
271- ( Hazaragi ) IPA ( key ) : [xɔː.mʊ́ːʃ] 
272-
--
356- Urdu
357- [ edit ] 
358-
359- Etymology
360- [ edit ] 
361-
362: Borrowed from Classical Persian خَاموش ( xâmôš ) .
363-
364- Pronunciation
365- [ edit ] 
366-
367- ( Standard Urdu ) IPA ( key ) : /xɑː.moːʃ/ 
368-
369- Adjective
```


## [2026-09-07T16:28:16.327Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### فراموش\"; sed -n '/^ Persian$/,/^ References/p' f0e8a23c73545e28.txt | head -60\necho; echo \"#### PIE mers-\"; sed -n '1,200p' 73e12d933f62d008.txt | sed -n '/Etymology/,/Derived/p' | head -60"
}
```


### [2026-09-07T16:28:17.548Z] TOOL RESULT

```
#### فراموش
 Persian
 [ edit ] 

 Etymology
 [ edit ] 

 From Middle Persian [script needed] ( pl(ʾ)mwš /⁠fra/ā-mōš⁠/ , “ forgotten ” ) , ultimately from Proto-Iranian *fra- ( “ forward ” ) + *ā- ( “ to, at ” ) + *marš- ( “ to forget ” ) , the latter two components from Proto-Indo-European *h₂éd ( “ to, at ” ) + *mers- ( “ to forget, annoy, disturb, neglect ” ) .

 Cognates include Baluchi شموشگ ( šamóšag , “ to forget ” ) , English mar ( “ to spoil, damage ” ) , Armenian մոռանալ ( moṙanal , “ to forget, fail ” ) , Sanskrit मृष्यति ( mṛṣyati , “ to forget ” ) , Latvian aizmirst ( “ to forget ” ) , Tocharian A märs- ( “ to forget ” ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /fa.raː.ˈmoːʃ/ 

 ( Dari, formal ) IPA ( key ) : [fä.ɾɑː.móːʃ] 

 ( Dari, formal ) IPA ( key ) : [fä.ɾɑː.móːʃ] 
 ( Kabuli ) IPA ( key ) : [fä.ɾɑː.móːʃ] 

 ( Hazaragi ) IPA ( key ) : [pʰuɾ.muʃt̪] 

 ( Iran, formal ) IPA ( key ) : [fæ.ɹɒː.múːʃ] 

 ( Tajik, formal ) IPA ( key ) : [fä.ɾɔ.mɵ́ʃ] 

 Rhymes: -oːʃ 

 Readings

 Classical reading ? 

 farāmōš

 Dari reading ? 

 farāmōš

 Iranian reading ? 

 farâmuš

 Tajik reading ? 

 faromüš

 Audio ( Iran ) : ( file ) 

 Adjective
 [ edit ] 

 فراموش • ( farâmuš ) 

 Dari

 فراموش 

 Iranian Persian

 Tajik

#### PIE mers-
 Etymology 

 1.2 
 Root 

 1.2.1 
 Derived terms 
 Etymology
 [ edit ] 

 According to Kloekhorst, perhaps an s-extension of *mer- ( “ to die, disappear ” ) . [ 1 ] 

 Root
 [ edit ] 

 *mers- [ 2 ] 

 to forget 

 Derived terms
```


## [2026-09-07T16:28:24.718Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### مرغ\"; grep -n -m3 -A12 \"^ Etymology\" d2cc991adb956e6f.txt | head -60\necho; echo \"#### سیمرغ\"; grep -n -m3 -A12 \"^ Etymology\" 221dca62bcc95883.txt | head -50"
}
```


### [2026-09-07T16:28:24.787Z] TOOL RESULT

```
#### مرغ
62: Etymology 1 
63-
64- 1.1.1 
65- Noun 
66-
67- 1.1.1.1 
68- Derived terms 
69-
70- 1.1.1.2 
71- Descendants 
72-
73- 1.1.2 
74- Further reading 
--
77: Etymology 2 
78-
79- 1.2.1 
80- Noun 
81-
82- 1.2.1.1 
83- Descendants 
84-
85- 1.2.2 
86- Further reading 
87-
88- 2 
89- Pashto 
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
122- 3.3.2 
123- Descendants 

#### سیمرغ
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Proper noun 
69-
70- 1.3.1 
71- Descendants 
72-
73- 1.4 
74- References 
--
148: Etymology
149- [ edit ] 
150-
151- Inherited from Middle Persian 𐭮𐭩𐭭𐭬𐭥𐭫𐭥 ( synmwlw /⁠sēn-murw⁠/ ) . [ 1 ] According to folk etymology a compound of سی ( sī  / si , “ thirty ” ) and مرغ ( murġ  / morġ , “ bird ” ) . See also The Speech of the Birds .
152-
153- Pronunciation
154- [ edit ] 
155-
156- ( Classical Persian ) IPA ( key ) : /siː.ˈmurɣ/ 
157-
158- ( Dari, formal ) IPA ( key ) : [siː.mʊɾɣ] 
159-
160- ( Dari, formal ) IPA ( key ) : [siː.mʊɾɣ]
```


## [2026-09-07T16:28:27.177Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '/^ Persian$/,/^ Pashto$/p' d2cc991adb956e6f.txt | head -60"
}
```


### [2026-09-07T16:28:28.475Z] TOOL RESULT

```
 Persian
 [ edit ] 

 Persian Wikipedia has an article on: مرغ 

 Wikipedia fa 

 Etymology
 [ edit ] 

 Inherited from Middle Persian 𐭬𐭥𐭫𐭥𐭠 ( mwlw' /⁠murw⁠/ ) (Manichaean Middle Persian 𐫖𐫇𐫡𐫇 ( mwrw ) ), [ 1 ] from Proto-Iranian *mr̥gáh ( “ bird ” ) . Compare Middle Persian 𐭬𐭥𐭫𐭥𐭠 ( mwlw' /⁠murw⁠/ ) , Parthian 𐫖𐫇𐫡𐫃 ( mwrg /⁠murγ⁠/ ) , Avestan 𐬨𐬆𐬭𐬆𐬖𐬀 ( mər ə γa ) , Pashto مرغه ( mërğë ) , Ossetian маргъ ( marǧ ) , Baluchi مرگ ( murg ) , Old Armenian սիրամարգ ( siramarg ) and լորամարգ ( loramarg ) .

 Pronunciation
 [ edit ] 

 ( Classical Persian ) IPA ( key ) : /ˈmurɣ/ 

 ( Dari, formal ) IPA ( key ) : [mʊɾɣ] 

 ( Dari, formal ) IPA ( key ) : [mʊɾɣ] 
 ( Kabuli ) IPA ( key ) : [mʊɾɣ] 

 ( Hazaragi ) IPA ( key ) : [muɾɣ] 

 ( Iran, formal ) IPA ( key ) : [moɹɢ̥] 

 ( Tajik, formal ) IPA ( key ) : [muɾʁ] 

 Rhymes: -urɣ 

 Readings

 Classical reading ? 

 murġ

 Dari reading ? 

 murġ

 Iranian reading ? 

 morġ

 Tajik reading ? 

 murġ

 Audio ( Iran ) : ( file ) 

 Noun
 [ edit ] 

 مرغ • ( murġ / morġ ) ( plural مرغ‌ها ( murġ-hā / morġ-hâ ) , or مرغان ( murġān / morġân ) , Tajik spelling мурғ ) 

 hen 
 تخم‌گذاری مرغ ― tuxm-guzārī-yi  / toxm-gozâri-ye murġ  / morġ ― hen laying eggs 

 ( synecdochic ) chicken (regardless of sex)
```


## [2026-09-07T16:28:38.437Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\ngrep -n \"pdf page\" WLD_Bd2_pages.txt | head -3\npython3 - <<'EOF'\nimport re\nt=open('WLD_Bd2_pages.txt',encoding='utf-8').read().split('\\f')\nprint(len(t))\n# find printed page 276\nfor i,p in enumerate(t):\n    if re.search(r'(?m)^\\s*27[5-9]\\s*$', p[:400]) or re.search(r'\\b276\\b', p[:200]):\n        print(i, re.sub(r'\\s+',' ',p[:120]))\nEOF"
}
```


### [2026-09-07T16:28:39.903Z] TOOL RESULT

```
725
280  ; 276 mer- mhd. hrehen^ aisl. hrja, hra „plotzl
```


## [2026-09-07T16:28:43.469Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (279,280,281,282,283,284):\n    p=t[i]\n    print('==== idx',i)\n    print(p[:1200])\nEOF"
}
```


### [2026-09-07T16:28:44.789Z] TOOL RESULT

```
==== idx 279
                                                          mer-                                                275

ist    vielmehr= av. mahrlcd- m. „Tod, Verderben^^ Bartholomae Airan. Wb*
 1146,       s.       auch Meillet Et. 220).

      mer 9) g\   {

      Lit.        mirgu,                ^flimmern, vor den Augen             sein“,       lett.   mirgstu^   mirgt
„flimmern, blinken^, mirgas „pl6tzliches Hervorblinken^^,                                  lit.   mdrgas „bunt^^,
mdrguti y,bunt schimmern^, lett. marga „Schiinmer^, murgi j^Phantasiebilder,
Ifordlicht^^;
      russ. morgat'b „blinzeln,                  winken“; Yielleicht gr. daaQvy'jq usw. (wenn v               —
vor g,        s. 0.);

      aisl. myrkr y*mirkwa-)^ acc.                 myrkvan ^^dunkeP^,                      myrkvi m. „Finster-
                                                   mjeguh (dies also nicht
nis“, as. mirki, skgs, mierce ^Aunkel ; ^\h, mjergute,
zu *meigh~ ^NebeP^) „Nebel, Finsternis“ (Jokl SBAk. Wien 168, I 57).
  Dagegen dt. Marke, aisl. merki n. „Zeic}ien, Fahne^^ usw. eher zu mog
.,abstreifen“               s.   d. ;   mir. merge, Acc. pi. merggi ^Banner, Fahiie“                    (Fi
==== idx 280
             ;




276                                                       mer-


mhd. hrehen^ aisl. hrja, hra „plotzlich aufleuchten‘^, got. hraJv atigins j,Augen-
blick’^ usw.      an, die     aber besser zu ai. hhrajati, bhra^ate (s. %hereg-^ hhereJc-)
gestellt    werden         (Lit. bei   Berneker II 85).

3,    mer- „sterben“.
     Ai.   mdrate „stirbt“; mriydte ds.,                   av. miryeite (^md'^ryeHe) ds.,   ap.   ama-
riyata „er starb“, =lat.            ai, Kaus. marayati „totet“, vgl. aksl. u-

moriti {u-marjati) „toten^; fo-Ptc. ai. mrtd-                        =
                                                 av. mdrdta- „gestorben, tot‘^,
ai. mrtd-m „Tod^, av. mdsa-             (^mrta-^ Bartholomae Wb. tl75j, ai.
amta- == av. am9sa- „unsterblicb“, arm. mard „Mensch^ {^mrtos\ abd.
mord^ ags. anord. mord                     n.    „Mord“ {^mHoni]         daneben "^mr-trom in got.
maurjn'     n.,   ags. niordor n.              „Mord“),    gr. figoTog „sterblich,m."Mensch“, a>-
^Qoro^ „unsterbiich'' (aus "^/ugaiog nach jLiogrog^ dvdgcoTiogy '&v7]r6g Hes.
umgefarbt, oder nach Debrunner GGA. 1910, 16 Aolismus; kaum nach
Brugmann-Thumb GrGr.^ 88 Bildung wie          
==== idx 281
                                                        mer-                                                                  277


Danielsson Sertum                phil. C. F. Johansson                       oblatum 81 ff.); morhiis „Krank-
heit^‘ (ygl. juagaojudg; Gdf. ^mor-lhos, vgl. tabum, tabes von Wz.          *?nor-
duos^ zur Wzf. "^merd-, wiirde b aus du voraussetzen, was fiir den Inlaut
mindestens fraglich ist, s. Niedermann IF. 15, 1 9, PerssonBeitr. 21 3fF, m. Lit.)';
                                                                               1




     miY. meirb, cjmr. merw j^schlaff, schwach“ (mer-ui-);                                     air.                   ,,Verrat^^

{*mr9-to-) zu        ^marnaid,
                     air.

     Aisl. meria (Praet. mar da) „stoBen,              ahd. maro^ mar aw imd
                                                                     zerstofien*^;                                       i



mtir(u)tvi ^^milrbe^ zart, reiP, ags. mearo „murbe, zart^^ (aber aisL meyrr
^miirbe*’^ nicht aus ^moru- umgestellt, s. Persson Beitr. 821 f. und u. *7nawro-);
aisl. morna j,hinwelken ^5 norw. mdartl. morna^ mama „zu faulen anfangen",

morer
==== idx 282
278                                        mer-


  mer-q-:
   ai. marcdyati ^gefahrdet, versehrt, beschadigt“, 7nrhtd- ^versehrt“, markd-

m, „Hinsterben, Tod“ = av. mahrka- „Tod, Yerderben’^, kons. St. ai. mrc-d
i. sg  ,
        av. m97'dxs n. sg. „Verderben, Zerstdrung^ (s, Bartholomae Airan. Wb.
1172),       mdroncaiti „versehrt, zerstort*'; arm. wore- ;,jung, zart^^ (^morqip-
Peterssoa KZ. 47, 280); vielleicht alb. mar „Laus“ {^morqo-, „die kratzende
oder dgl.^^ ? vgl. (pd’EiQ ds. (p^dgeo; Jokl SBAk. Wien 168 I 58); lat. mur-
                                  ;


CHS „verstuinme]t“ (s. Yf. LEWb.^ s. v.; scheint ein ptc. auf -wo-,
wie oB^,facus „factus“ nsw., Johansson KZ. 30, 443 Anm. J, Havers IP. 25,
388); ahd.                 „schlafF“ {got, gamaiirgjan „verkurzen^^ nsw. s. hingegen.
u. *mregJiii- „kurz“),  s. Pick    107f., 515 (in Yerbindung mit der wohl ur-
sprunglichen Wz. merq- ^morschen, faulen, dissolvi^), Zupitza Gutt. 135.
   Mit anl. s- lit. smefkti „in Not zu versetzen suchen'^, smarMs „gransam“,
paSTYierkti „verderben“, nhd. mdartl. schmorgen „darben, notleiden^^ (Zupitza
Gutt. 137).
   Hieher (als ,jHaeksel“) oder zu merq- „dissolvi‘‘ (von nassen Pleischteilen)
==== idx 283
                                        (mer*) mor-                              279

  lett.merdU ^abmergeln, hungern lassen, unbarmherig behandeln; eines
Menschen Tode beiwohnen^ (letztere Bed. naber zu lit. mcrdeti, Praes.
m^dmi, merdmi „sterben“, das auf einem do- oder i?Ao-Praes. zu "^mer-
„sterben“ beruht, wie auch mer-d- „reiben^^ im letzten Grund auf ein
solches (?o-Praes. zuriickgehn wird; ist lett. merdetoMch. in der Bed. „hungern
lassen“ von „sterben lassen, hinwerden lassen^^ ausgegangen, also naber zu
mer- ^sterben^^ zu zieben?), Persson Beitr. 2t3ff.
  lat. mordeo, -ere, mornordi „bei6en“   (= ai. marddyati, mamrde), auch
von Gefiiblen und Geschmacksempfindungen, was auch die Briicke zur
Bed. der folgenden mit s- anl. Pormen schist:
   gr. ojLUQdvog, oyegdaXeog „schrecklich, furcbtbar^^ (*„aufreibend, plagend^^),
uhd. smermn „schmerzen‘^, smerzo „Schmerz^^ mnd. smerten „sohmerzen'‘‘,
nd. ndl. smarten bes. von dem durch Scheuerwunden verursachten Scbmerz
(s. Palk-Torp u. smerte),   ags. smeortan ^schmerzen^, engl. smart „beiBend,
scharf, witzig“ (iocus niordens) und „nett, zierlicb“ (Ebel KZ. 1, 226,
                                                                   Pi
==== idx 284
                                                                          ;




280                                        meradh    mere-


poln. 7norqg ,,dunkler Streif; bunt gestreift; bunt gestreiftes Tier,  Hemd'^
u. dgl. ;  Solmsen [Jagic-Festschrift 576 ff.], Berneker II 18 (und 22, wo
gegen Solmsens Anreihung von russ. mar^ „Sonnenglut‘‘ usw. s. mer-
5
 ,flimniern'^), Petersson LUA. 1916, 40; nacb letzterem hieher auch gr.
jUOQvov eidog aerov xal ^av&og Hes. („schmutziggelb^‘), juoQzog jueXag (paiog
               *                                                                •




Hes., vielieicht auch mit s-Erw. arm. mrayl „Dunkel, S^ebel, Wolke; finster,
dunkek* {^mnhiyl auf Grund von                      mafaxul „ dicker Dampf,
Dunkel“ (mrso-^ und lit. murszinu „besudle“, mut'{1c)szlmii „Avasche, patsche,
8udle“ (dies kaum zu meregh- „benetzen‘^).
   Urspriingliche Beziehung zu mer- „flimmern'‘ ist nicht erweislicb, wenn-
gleich „]euchten‘‘ und „schwarz“ auch bei andern Wzln dieser Bed. neben-
einanderstehn.          —
                     S. noch u. smel- „schwelen“.


meradh- „aufsprudeln, aufschiitteln^.
       Gr. ^gdooco,     att. pgaiTo^^d),aor, e^gdoa, jon. ix-
```


## [2026-09-07T16:28:53.848Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD\npython3 - <<'EOF'\nt=open('WLD_Bd2_pages.txt',encoding='utf-8').read().split('\\f')\nimport re\nfor i in range(276,290):\n    p=t[i]\n    if 'ergessen' in p or 'marzjan' in p or 'mrsyate' in p or 'mfsyate' in p:\n        print('==== idx',i)\n        j=p.find('ergessen')\n        print(p[max(0,j-1500):j+900])\nEOF"
}
```


### [2026-09-07T16:28:55.154Z] TOOL RESULT

```
==== idx 283
ch smerd- „stinken“.
   m er-s-.
   Ai. masam,      mastm kar-      „pulverisieren“, masi-,   masi „Pulver“ (Persson
Beitr. 220);
   ahd. morsari j,Morser^^ (umgebildet aus  lat. mortarium), mbd, zermilrsen
,,zerdrucken, zerquetschen^,  md. zermorschen ds., schweiz. morsen, miirsen
„zermalmen, kleinsto6en“, mhd. nd. rmirsch, mnrs nhd. morsch, ndl. mor-
zelen ^-zerreiben^ (s. Kluge EW. s. v., Wood Men. 21, 40 f.; das tonlose s
frotz der Schwundstufe zwingt nicht, in den germ. Worten mit Petersson
Stud, zu Portunatovs Regel 95 f. eine s-Weiterbildung von mer-d- zu sehen).
   Lat. marra „Hacke“ ist vielmehr orientalisch, s. Vf. LEWb.^ s. v. Weidner
Gl. 4. 303.
   Dazu wohl (s. Persson Wzerw. 85, Pranck KZ. 37, 130, Uhlenbeck Ai.Wb.
21S,      Wood Men. 21, 40   f.,   Mod. Phil. 5, 18)
                                              einerseits got. marsjan „argern,
Anstofi      geben^,   ags. mierran,  merrian, ahd. merren „argerD, storen,
                                        as.
hindern"^, ags, amierran „verderben, zerstoren, hindern^, mhd. marren
^,zogern, sich aufhalten“ usw. (s. auch Palk-Torp 1516 u. merle\ andrerseits
(nach Bed.-Verhaltnissen wie ai. mdrdJiati „la6t nach, vernachlassigt, ver-
giSt^^ : djiiakdvvco, Wz. me?-, mel-d-, zerreiben^), die Gruppe Pick          109,
286) ai. mHyate ,,vergi6t, vernachlassigt, duldet, verzeiht“, marsa- m. „ge-
duldiges Ertragen^, mrsa j,umsonst, vergebens; irrig, unwahr“, marsayati
„ duldet, verzeiht'*^, lit. mirsz-td, -au, mirszti „vergessen, auBer acht lassen^,
marszas „Vergessen^ (~ ai. marsa-), marsziis „verge61ich“, arm. (Pedersen
KZ. 36, 99) moranam         ^vergesse^^.


 (mer-) mor- „schwarzen, dunkle Parbe, Schmutzfleck“.
   Gr. jnoQvyog „oxoTeiv6g'', yeuoQvyaevog ,,(rauch)geschwarzt“:        russ.   mard-
       -lb   ..schmieren, sudeln, pfuschen; verunglimpfen, verlaumden% sa „sich
 besudeln, kacken (von Kindem)*’, maruska jjPleck, Mak' marend (graphisch
 fiir marend) „Parberr6te‘‘, klr. marovdtyj „unrein‘', cech. morons „asch-
 farbig gestreiftes Rind*',    moraiy ,,schwarz gestreift“, morovaty „ds., fleckig",
```


## [2026-09-07T16:29:04.449Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^mers-\\|^merso-\\|^mer-\\|^mor-to\\|^morto-\\|^mortis\\|^merdh\" IEC.txt | head -20\necho \"=== mṛgo bird\"\ngrep -n \"^mr̥go\\|^mrgo\\|^mergo-\\|^merg\" IEC.txt | head -10"
}
```


### [2026-09-07T16:29:04.510Z] TOOL RESULT

```
10658:mer- (mern-) (e-gde radical of type mr-, q. v. with extensions, and cf. mruos (moruos), etc. Per. cf. miram, inf. murdan die: Arm. mef- nim, meranim, aor, meraj, id.; merot, gs -i, ab. s. -av ‘mortal; Hitt. (queried) mernun, 1sg. (T die? or ‘cause to die") beside merr- die: W meru, inf. ‘droop’ beside merth, pl. -i, m. exhaustion’, fr. *mertis); Cor. cf. mernans, m. ‘death’; Latv. mernéju, et ‘starve’
=== mṛgo bird
10661:mergi, io ‘wicker; bracket, crosspiece, prop, forked stick’. Cf. mesgó (1) Lat. mergae 'pitchforks, reaping-hooks'; (o- gde in) Gk. mórgos ‘wicker cart-body'; LG cf. Micke, f. ‘forked stick, pitchfork’; OCS, Big. mrěža, f. ‘neťľ; R merëža ‘net, net-trap'; Cz. mříže 'iron bars, grille’; (isophonic in Ir. mearg, f. ‘wrinkle’; Li. merga, merge ‘girl’)
10662:merg- (1) "dark gloomy, grim; darkness, stain, grimness'. Cf. WP II, 282 & 314 Olr. merg, f. ‘decay, rust’; Ir. meirg, f. ‘stain, rust; OS mirki, OE mirce, adj. ‘grim, gloomy, dark’; LG Mirken, pl. ‘grimaces’; Blg. cf. mréz- gav “grim, hostile, overcast
```


## [2026-09-07T16:29:08.624Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"mersio\\|merso\\|mers-\\|marsa\\|mrsyate\\|mṛṣyate\" IEC.txt | head -10\necho \"=== mrgos\"\ngrep -n \"\\bmrgos\\|mrgo-\\|mr̥gos\" IEC.txt | head -5\necho \"=== mortos\"\ngrep -n \"^mortos\\|^morto\\|mortis\\|^mrtos\" IEC.txt | head -8"
}
```


### [2026-09-07T16:29:08.700Z] TOOL RESULT

```
5090:guabh- ‘swallow, engulf, immerse’. WP I, 674 Av. jaiwis ‘deep’; Gk. báptō ‘dip, dye, wash’; baphé ‘immersion’; cf. Hes. bákhtho húdatos ‘quaff water; MHG er-queben ‘choke’; E to quaff ‘drink in gulps’; ON kvefja ‘immerse, drown’; Sw. kväva ‘stifle’; kvaf ‘sultry; anxie- ty; Norw. cf. kvamne ‘choke while eating’,
10346:mars- (marsó, io; marsos) ‘bad; be bad, err; wickedness, error'. Cf. mors- Hitt. mars- ‘be bad’; marsas ‘bad, corrupt’; Alb. í marrë ‘mad’; Arm. (?) cf. maš “outworn, old’; mašem ‘wear out, corrode’; Go. marzjan, v. “scandalize'; OE mearr “evil, deceptive’;
=== mrgos
=== mortos
11176:mortos ‘dead, killed; death’. Cf. moros, mō- ros, mrtuos, məruos. WP II, 276 Skt. mártah, m. “mortal, man’; Ober cf. mar- tiya, adj. as s. ‘man’; Per. mard, s. “man? be- side murde, pp. "dead Av. maroto, adj. & s. as Skt.; LW in Arm. mard, ost ‘man’ (fr. Iran.) but inherited in mart, í-st, s. ‘battle, war’; Gk. mortós, adj. & m. as Skt.; Lat. (am- big.) morta, f. “fate, angel of death; Ir. mort, m. ‘murder, death’; Br. (ambig.) mors, adj. ‘sluggish’? beside morza, v. ‘benumb’; G cf. Mährde, f. ‘dalliance, delay; LW in Finn. marto, adj. ‘sterile’
11301:mrtos (dead; mortal, being, creature’. Cf. mer-, mortos, mró, etc. & next. Variant: mort-. WP II, 276 Skt. mrtáh, pp. (dead; Ober marta, id.; Av. moroto, id. (and 'death"); Oss. mard “dead; corpse’; Lat. cf. Morta, f. ‘one of the Fates’; Olr. mart, m. (carcase; steer’, fr. *mort-); Ir. mart, m. ‘head of cattle, carcase of beef; MHG mort, gs mordes, sm ‘murder; strang- les; OFris. morth, m. “crime, murder, dead child; LG Mort, m. ‘bogey, nightmare’; ON cf. myrða, v. ‘to murder; Li. cf. mirtinai, adv. ‘fatally’
12434:pág- (1) ‘harden, fix, fit. Cf. paK-. WP II, 3 and panĝ- Skt. paj-, radical ‘grow stiff; cf. pajráh “solid, stout’; Oss. fáz, Dig. fázà, s. lawn, flowerbed’; Arm. hoc, adj. ‘compact (fr. *pagus, cf. SEM: AE: $ 3); Gk. pégnümi, inf: pagénai ‘fix’; pégós “compact? beside págos, m. 'congeal- ment, rock, ice’; páge, pagís, f. ‘trap’; págios, ad). “fixed, firm'; OLat. pago, ére, (Lat. pango, ere) ‘fix’; pàgus, gs: -1, m. ‘landmark’; im- pages, f. ‘tenon, peg, panel-frame'; pàges and com-pàges, f. “join, setting, juncture, fitting"; LLat. pagino, are ‘compose, construct; Olr. áge, álge, m. ‘joint, member, period"; cf. ai- gred, s. "ice: aigreta, adj. ‘icy; MHG vach, sn. ‘dam, weir; piece, part, partition; fold’; G Fach, Du. vak, n. (fdivision', etc.); OE fæc, n. ‘space, interval; R paz, m. “joint, mortise’; Cz. paže, f. ('arm', fr. *pagio) beside paž-ba *gunstock, wainscot'; pažiti, inf. “box in, wall up, fix’; cf. also OCS paz-nogüti, Cz. paz- nehet claw, talon’; Ukr. cf. paz-ur, Cz. paz-our, m. id.; Ukr. R paz-üxa, f. ‘bosom’; R cf. paz- dir ‘awns’
12495:pald- (?) “fold, pair, pairing; pleat'. Cf. pol-, polt- Lat. palla, f. “long robe’; pallium, n. ‘robe’; MHG valz, sm. ‘seam, rim, groove, mortise; mating of birds’; G Falz, m. ‘seam, rim’; OHG cf. gafalzjan, v. ‘pleat
13327:poksos, is, ios, üs ^wing, side, flank, wall, partition, pigeon-hole'. WP II, 3 Skt. paksáb, m. “wing, side, half, party’; Oss. faxs, pl. fäxstä ‘side’ beside fáxs ‘strip, board’; Gk. puxís, gs: -idos, f. (box. Vocalism as nüx, see noktis above); Myc. cf. pukso(1) (parts of a table, perh. *drawers, flaps"); Latv. paksis, pl "nterlocking beams, tenon-and-mortise joint, corner of box, side’. Cf. also OE fzes, n. ‘border’; Swiss Fácke, f. ‘wing’. Long-gde in R pax, Cz. pach, m. ‘groin’; Cz. also pachy “loose sleeves’; Ukr. paxa, f. ‘armpit’; Blg. pàxove, pl. (^waist': Skt. pāksah “of half, side or party’: Oss. faxs ‘side’)
16666:solkos ‘drag, hook; trail, furrow, track’. (E- gde, of uncertain provenience, in Gk. hélko, fut: helküso ‘drag’, etc. See uelk-, uelqu-) Gk. holkós, m. 'drag, hauling implement; furrow, track’; adj. (attractive? cf. holké, f. ‘dragging’; holkaios, adj. ‘drawn’; Myc. (Py- los) cf. (queried) ksu-keiatewe oka diptera (= *xu-keiatees holkaies diphthérés 'scraper- splitters of stripped leather"); Lat. sulcus, i, m. ‘furrow’; Slovak slak, m. ‘mortise, fence’; slák, m. “violin-bow?
```


## [2026-09-07T16:29:18.396Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"forget\" IEC.txt | head -10\necho \"=== mors-\"\ngrep -n \"^mors-\\|^morsos\\|^mors\" IEC.txt | head -5\necho \"=== mordeo/mrd\"\ngrep -n \"^merd-\\|^mordo\\|^mrd\" IEC.txt | head -5"
}
```


### [2026-09-07T16:29:18.508Z] TOOL RESULT

```
4626:OBr. gabl ‘fork’; W gafl, id.; Br. gaól, gavl “fork, spit' (Celtic LW in G Gabel, etc.); OHG gëbal, MHG gëbel ‘head, skull, gable’; Du. gevel *gable-end'; Slovene žebelj "nat" (A variant of type *ghebhor- arises in Ir. geabar *arge-headed fish’, cf. Gk. képhalos ‘mullet’, and in Latv. Zeburs ‘two-pronged fork") (ghebholos (2) *piece' in OE geofola, giefel *morsel'. See gabholos and cf. WP I, 571) ghed- “acquire; acquisition'. Cf. ghnd- and WP I, 589 Oss. zíd, zudà (‘greedy fr. *ghedu-, *gheduo); Lat. cf. -da (for *-heda in prae-da ‘booty’; hedera ‘ivy’, fr. a neut. pl. *ghedeso; and helluo (?) ‘glutton’, if for *ghed-leuon, see leu-); OE gietan ‘get; ON geta, id. beside geta, f. ‘guess’; MHG -gezs- in a-gezzel "Tor, getful'; er-gezzen ‘forget; (*-6- in) gæze, adj. ‘greedy’ and ON gæta ‘watch, heed', ON gáta ‘riddle’, Sw. gåta, id. and apparently *-0- in Cz. zá-hada, id.; OCS cf. Zadati ('desire', if distinct from ZeZdo, Zedéti, id. See ghnd- and cf. OCz. žádný *beloved") (*-e-); Li. gedáuju, -auti ‘desire’. Uncertainly Alb. gjuej, gjuaj ‘hunt beside gjojé, f. ‘hunt’, fr. *ghed- (cf. the LW rruej, rruaj ‘shave’ fr. Lat. radere). Cf. ghend-. Alb. gjej “find, guess? is ambig. A desiderative form of type *ghedsio occurs
9411:lādh- (?) “lying, lurking, resting’. Ambig. cf. lendh- Gk. lóthð (Dor. -à-) ‘lurk’; lethe, f., léthos, n. ‘forgetting’; cf. also a-l&thés (lit. 'unhidden', hence “evident, true’); MHG cf. (?) lette, wm (soil, loam’, fr. *ladhjo?) and Swiss lóter (flat, of wine”, fr. *ladhrio-?)
11175:v.id.; Li. cf. marsüs, adj. “forgetfuP
11286:mrsio (1), mrsKo ‘forget’. WP IT, 281 Skt. mrsyami (1), id.; Per. cf. fara-muS, adj. ‘forgetful; fara-müsam, inf: -mūšīdan, v. "Tor, get; Tokh. AB márs-, B mars-, id.; Arm. cf. (o-gde) mornam, moranam, id.; Icel. morra, v. idle, doze’; Li. cf. mirštu, inf: miřšti "Tor, get (*mrsKo); (o-gde in) marëus ‘forgetful
16237:sleiu- (sliu-) (1) ‘faint, weak’. Cf. sloiu-, sliuoros Vedic cf. srivyàmi, v. (fail — of seed-crop' beside Skt. sreváyami (o-gde) “cause to fail; ambig. in Lat. ob-livius, adj. ‘forgetful’; ob- liviscor, dep. v. ‘forget’, see sloiu-
16325:sloiu- (sloiuos, sloiueið) ‘crawl, creep; slow, sluggish; sloth’. Cf. sleiu- Skt. sreváyami, v. “cause to fail; Lat. cf. ob- [ivius, adj. ‘forgetful’; oblivium, n. *forgetful- ness’; obliviscor, adj: oblitus, dep. ‘forget’; OHG slēo, gs: slewes, adj. *blunt'; slewen, wv. id.; OS siêu, adj. ‘blunt’; OE slàw, adj. ‘sluggish’; Du. slee, adj. ‘unripe, blunt’; Fris. sleau, adj. ‘slow, limp’ but cf. (variant in) slou war ‘muggy weather’; G schleh, adj. *in- sipid'; ON slær & sljór, adj. ‘blunt; faintheart- ed’; Norw. slóv, adj. ‘blunt, dull, stupid’; Sw.
=== mors-
11182:mors- (morsK-) — moteio
=== mordeo/mrd
11231:mrd- (mrdnó, mrdio) ‘force, press, crush, kil. WP II, 278. Cf. mld-. Indo-Iran. ambig.
```


## [2026-09-07T16:29:26.890Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '11170,11180p' IEC.txt\necho \"--- leaf of 11286\"\npython3 - <<'EOF'\nt=open('IEC.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if 'mrsio (1)' in p: print('leaf idx0',i,'est printed', (i-15)*2)\n    if 'mortos ‘dead' in p: print('mortos leaf idx0',i,'est printed',(i-15)*2)\nEOF"
}
```


### [2026-09-07T16:29:28.261Z] TOOL RESULT

```
799
maravah “wild, deserted'; marih, f. ‘plague,
death’; ku-marah, m., -marib, f. ‘boy; girl
(semantics obscure); Srb. cf. márva ‘cattle’ mors- (morsK-) ‘forger
Tokh. AB mürs-, B mars-, v. id.: Arm. mornam,
v.id.; Li. cf. marsüs, adj. “forgetfuP
mortos ‘dead, killed; death’. Cf. moros, mō- ros, mrtuos, məruos. WP II, 276 Skt. mártah, m. “mortal, man’; Ober cf. mar- tiya, adj. as s. ‘man’; Per. mard, s. “man? be- side murde, pp. "dead Av. maroto, adj. & s. as Skt.; LW in Arm. mard, ost ‘man’ (fr. Iran.) but inherited in mart, í-st, s. ‘battle, war’; Gk. mortós, adj. & m. as Skt.; Lat. (am- big.) morta, f. “fate, angel of death; Ir. mort, m. ‘murder, death’; Br. (ambig.) mors, adj. ‘sluggish’? beside morza, v. ‘benumb’; G cf. Mährde, f. ‘dalliance, delay; LW in Finn. marto, adj. ‘sterile’
(moruis, os, ios, iə "ant, see muruis, etc.)
moruos ‘foul, decayed, dead’. Cf. máruos (moruos, mruos) and meruos, mrsos Av. cf. Mourus (name of a desert-town); Pahl. maruv-; OHG maro, gs marawes, adj. ‘rotten’; OE mear ‘weak, ailing’; Slovak cf. morava ‘lea, grassland’. (Vocalism ambiguously *-o- or *-á- (*-o-))
-mos, de-verbal suffix in formation of nouns Skt. cf. ruk-máh ‘gold ornament’; Hitt. werite- mas ‘fear; Arm. gea-m, gs gemo, ab. s. gemov ((tissue', fr. *guiu-, q. v.); or-m, o-st. ‘wall; Gk. gá-mos (“ marriage”, fr. *$n-, q. v.); iug-mós ‘shout’; kom-mós, stolmós, pal-mós, etc.; Alb. shkel-m, m. (*kick', fr. shkel, v. id.); ngul-m, m. ((thrust, fr. ngul, v. id. See kulið); Ir. gliogr-am, m. ('rattle', fr. gliograim, v. id. See glig-, gligor-); geall-am, m. ( ‘promise’, fr. geall- aim, v. id. See gheldhó); W cf. deddf, f. law: Gk. tethmós, m. id.; Go. cf. maip-ms, m. ('treasure'. See moit- ‘turn, change); MHG cf. bar-m, sm. ‘lap, bosom’; g&l-m, sm. (noise, fr. gëllen); Cz. prám, R poróm Craft ferry” Cf. per-, por-); Li. jaüs-mas, m. (feeling, fr. jaüsti ‘to feel)
mos (mnos) *we, us'. Cf. nós, mes, menes OCS my, id.; Li. mus, acc. ‘us
--- leaf of 11286
mortos leaf idx0 448 est printed 866
leaf idx0 452 est printed 874
```


## [2026-09-07T16:29:35.358Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"### LEW mortarium\"; grep -n \"mortarium\" LEW_1910.txt | head -5\necho \"### LEW morbus\"; grep -n \"^morbus\\|morbus,\" LEW_1910.txt | head -5\necho \"### LEW mordeo\"; grep -n \"^mordeo\" LEW_1910.txt | head -3\necho \"### LAT\"; grep -n \"^mortarium\\|^morbus\\|^mordeo\\|^mors,\" LAT.txt | head -8"
}
```


### [2026-09-07T16:29:35.438Z] TOOL RESULT

```
### LEW mortarium
### LEW morbus
### LEW mordeo
### LAT
38980:mordeo
38994:morbus, -I m.: maladie. Distingue de aegrotatio et de uitium par
39011:mordeo, -es, momordi (memordi et -morsi), morsum, -ere; mordre.
39089:mortarium
39140:mortarium, -I n.: 1° mortier, recipient ou 1' on pile et petrit
```


## [2026-09-07T16:29:39.363Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '38994,39010p' LAT.txt\necho \"-----\"\nsed -n '39011,39040p' LAT.txt\necho \"----- mortarium\"\nsed -n '39140,39165p' LAT.txt\necho \"----- mors\"\ngrep -n \"^mors, mortis\\|^mors,\" LAT.txt | head -3"
}
```


### [2026-09-07T16:29:39.472Z] TOOL RESULT

```
morbus, -I m.: maladie. Distingue de aegrotatio et de uitium par
Cic. Tu.4,13,38, morbum appellant totius corporis corruptionem; aegro¬
tationem morbum cum imbecillitate; uitium cum partes corporis inter
se dissident, ex quo prauitas membrorum, distortio, deformitas. Ancien
(Loi des XII Tables), usuel; non roman.
Derives et composes: morbeo: aoQevw CGL II «47,34; morbidus, conservi
dans les dial.italiens, M.L.5677, d'ou morbido,-as (tardif); morbosus
(d*ou norbidosus, Gloss., contamination de morbidus et de morbosus),
morbositas; morbesco, tardif (Fortun.) qui a surv^cu dans le valenyais
morber, M.L.5676; remorbesco (formd d'aprbs recrudesco?), Enn.Inc.37;
Morbonia, formation plaisante, cf.Suet. Vesp.14, comme Populonia,
MugiSnia, etc.; morb i-f er,-ficus, rares et tardifs. L’adj. etle
verbe qui correspondent le plus souvent a morbus, c’est aeger,
. aegroto.
■ La ressemblance avec morior doit etre fortuite. Le non de la "ma¬
ladie" differe d'une langue indo-europ^enne a 1'autre, ce qui rend
vain de cbercher 1'etymologie de morbus.
-----
mordeo, -es, momordi (memordi et -morsi), morsum, -ere; mordre.
— Ancien (Enn.), usuel, classique. Panroman, sauf roumain. M.L.5679.
Les formes a e mordere que supposent les langues romanes ont du etre
refaites sur momordi, morsum; cf.tondire, spondSre. — Sens physique
et moral, propre et figure, e.g. Cic., Att.13,1«,1, ualde ne momorderunt
epistulae tuae; Tu.4,«0,45, morderi conscientia (cf. 1 1 emploi figure
de gr. 8 cxkvw). Meme emploi de mordax, mordacitas, remordeo, cf.Lucr.
3,827, praeteritis male admissis peccata remordent, qui s'est conserve
dans les 1 . romanes, cf.M.L.7201 renordSre,-dere.
Derives et composes: mordax, -acis; mordacitas; mordacia (forme comme
audacia, et sup^ose par les formes romanes, M.L.567O);
mordicus, adv. o 5 a^. Sans doute ancien adj . pris adverbialement. Est
a mordeS comme medicus a medeor; cf. M.L. 568oa; la forme d’ablatif
mordicibus attest^e par Non.139,32 dans Pl. Au.234 (les mss. de Pl.
ont mordicus ) semble amenee par le parallelisme de cornibus; le
nomin. mordex n'est atteste qu'a partir d'Apulee; mordico,-as; mordi¬
catio ( Cael., Aurei., Diosc. ), M.L. 5680 ; -tluus; enordico; mordosus :
6r)XTt,xoe (Gloss.); norsun,-l (Catul.64,318 laneaque aridulis haerebant
morsa labe Ilis), d'ou morsa dans les 1 . romanes, M.L.5689; morsus, -us
m.: morsure, M.L.5691; morsiuncula; morsico,-as, formation populaire
en -ico comme mordico (cf. fodico, mastico), M.L.5690, d’ou morsicatio;
morsicatim;
admordeo: nordrea (sens physique et moral), M.L. 181, et 182 *admordium,moretum
- 73 6 ~
* armor dium; commordes, M.L.ao88; de-, prae-, re-mordeo, H.L.qsox-,
immorsus: mordu, entame profondement.
Aucun rapprochement sur. On compare souvent des mots dont le sens
concorde.peu avec celni de norde 5 et dont les sens divergent entre
eux aussi bien qne les formes. On ne cite aucune racine indo-europeenne
signifiant nettement "mordre"; la plus claire est celle de gr. 8a hvw
----- mortarium
mortarium, -I n.: 1° mortier, recipient ou 1' on pile et petrit
certaines substances avec un pilon, pistillum', puis tout ob j et res-
semblant a un mortier; 2° substance trituree dans un mortier, pommade.mSrus
- 738 -
Diminutif: mortariolum.. Ancien (Pl., Cat. ). Panroman, sauf roumain,
M.L.5693 et 56g3a; germ. : v. angi, mortere.
Aucune etymologie sure.
m 5 rus, -us £.: aurier; morum n.: mure. - Panroman, M.L.5696 (et
germ.: v.h. u.murboum; celt.: gall. muiyar, etc.) et 5Gg6a; morulus,-a,-um
(Pl.): couleur de mure. Cf. aussi *moricula, M.L.s68ia; morinus sC84a.
Cf.gr.ji.6pov "mure"; trace de o dans [iwpa* auxap,i,v<x H^s. Emprunt
au grec, ou plutSt a une langue mediterran^enne, comme ficus, etc.
M. Pedersen propose une hypothese peu vraisemblable, V. Gr, d. k. Spr . ,
I 67.
morus, -a, -un: fou; quelquefois substantive morus, mora "un fou,
une folle". N'est guere atteste que dans Plaute, avec l’adv. more,
et le compose morologus. Allitere avec mos, cf.Pl., Men.571, utimur
maxume more moro molestoque, et Tri.668. Neron en avait tire par
plaisanterie un verbe morari (equivoquant avec morari): morari eum
[= Claudium ] inter homines desiisse, producta prima syllaba iocabatur,
Suet.Ner.33. Cf. aussi morio,-onis (epoq.imp.).
Emprunt au gr. pwpos.
m6s, moris m. : maniere de se comporter, fa<,on d'agir, physique
ou morale, determinee, non par la loi, mais par l r usage. Designe aussi
souvent la coutume: mos est institutum patrium, i.e. memoria ueterum
pertinens maxime ad religiones caerimoniasque antiquorum, F.146,3,
----- mors
```


## [2026-09-07T16:29:55.638Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"\" LEW_1910.txt; grep -n -i \"morb\" LEW_1910.txt | head -5; grep -n -i \"mortari\" LEW_1910.txt | head -5"
}
```


### [2026-09-07T16:29:55.705Z] TOOL RESULT

```
14866
11080:miluh, milih II 62 milzi I 799 min II $4 mindil IT 24, 73 minig IL 91 minniro, minnist IT 93 minza IT 72 mios II 134 miscan IT 96 missan, missen IT 98, 137 missi II 137 missitat IT 137 mist LI 60 mittt ID 58 mitewari IT 528 mittagarnt, mittila- garni I 71, 635 molawén I 508 morbert IT 114 mord II 113 mornén II 68 morsari, mortart SHE mos II 134 most II 136 mucka IT 133 muhhari, muhh(e)o IT 119 muckazzen IIT 119 mihheimo IT 119 muchilart II 119 mihhon II 119 mil IT 125 mila II 73, 117 muli(n), mulinare IT 104 muljan IT 105 mulhtra IT 121 mund II 24 munih IT 106 munistrt IT 106 munizza II 107 munt IT 35 muntar IT 127 munza IT 72 muoan IT 102 muodar II 50 muodi II 102 muolt(e)ra IT 121
```


## [2026-09-07T16:30:03.800Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor w in \"mortgage,\" \"mortuary,\" \"remorse,\" \"morbid,\" \"mortar,\" \"mortal,\" \"mar,\"; do echo \"### $w\"; grep -n -m1 -o \"$w[^|]\\{0,320\\}\" KLN_1966.txt | head -2; done"
}
```


### [2026-09-07T16:30:05.073Z] TOOL RESULT

```
### mortgage,
(eval):2: bad math expression: operand expected at `^|'
### mortuary,
(eval):2: bad math expression: operand expected at `^|'
### remorse,
(eval):2: bad math expression: operand expected at `^|'
### morbid,
(eval):2: bad math expression: operand expected at `^|'
### mortar,
(eval):2: bad math expression: operand expected at `^|'
### mortal,
(eval):2: bad math expression: operand expected at `^|'
### mar,
(eval):2: bad math expression: operand expected at `^|'
```


## [2026-09-07T16:30:08.953Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\nfor w in ['mortgage,','mortuary,','remorse,','morbid,','mortar,','mortal,','mar,']:\n    i=t.find('\\n'+w)\n    if i<0: i=t.find(w)\n    print('###',w)\n    print(re.sub(r'\\s+',' ',t[i:i+420]))\n    print()\nEOF"
}
```


### [2026-09-07T16:30:10.681Z] TOOL RESULT

```
### mortgage,
mortgage, gage, tr. v., to offer as pledge. — F. gager, fr. gage. See gage, ‘pledge’, and cp. engage, gage, n., a variety of plum. — See greengage, gage, n. — See gauge. gageite, n., a hydrous silicate of magnesium, manganese and zinc (mineral.) — Named after R.B. Gage of Trenton, New Jersey. For the end¬ ing see subst. suff. -ite. gaggle, intr. v., to cackle. 

### mortuary,
 mortuary, adj., 1) pertaining to death; 2) per¬ taining to a burial. — Late L. mortudrius, ‘of the dead’, fr. L. mortuus, ‘dead’, fr. mors, gen. mortis, ‘death’. See mortal and adj. suff. -ary. mortuary, n., 1) formerly a gift claimed by a parish minister from the estate of a deceased parishioner; 2) a deadhouse, morgue. — ME. mortuarie, fr. ML. mortudrium, prop

### remorse,
 remorse, n. — ME. remors, remorse, fr. MF. re- mors (F. remords), fr. VL. remorsus, pp. of re- mordere, ‘to bite again, vex, torment’, fr. re- and mordere, to bite'. See mordant and cp. morsel. Derivatives: remorse-ful, adj., remorse-ful-ly, adv., remorse-less, adj., remorse-less-ly, adv., remorse-less-ness, n. remote, adj. — L. remotus, ‘afar off, remote’, pp. of remo

### morbid,
morbid, adj. — L. morbidus, ‘sickly’, fr. morbus, ‘sickness, disease’, which prob. stands for *mor- bhos, or *mx~bhos, lit. ‘that which consumes’, fr. I.-E. base *mer-, ‘to rub, pound, wear away, consume, exhaust, worry; to be consumed’, whence also Gk. [zapaivstv, ‘to consume, ex¬ haust’, (zapaoptop, ‘consumption’; see Walde- Flofmann, II, pp. 110-111 s.v. morbus. See 

### mortar,
 mortar, n., a vessel for pounding. — - Partly fr. ME. morter, fr. OE. mortere, partly fr. OF. ( = F.) mortier. Both OE. mortere and OF. mortier derive fr. L. mortarium, ‘mortar’ (i.e. ‘vessel in which material is pounded’), whence also MLG. morter, OHG. mortari, morsari, MHG. mor- stere, G. Morser. L. mortarium derives fr. I.-E. *mrtos, ‘rubbed, pounded’, pp. form

### mortal,
 mortal, adj. — ME., fr. MF. mortal, mortel (F. mor tel), fr. L. mortalis, ‘mortal’, fr. mors, gen. mortis, ‘death’, from the stem of morior, mori,' to die’; which is cogn. with OI. mrtih, ‘death’, mriyate, marati, marate, Avestic miryeite, ‘dies’, OI. mart ah, ‘mortal, man’, Avestic mereti-, Lith. mirt'is, OSlav. sumriti, of s.m. ; OI. mrtdh, Avestic mlreta-, ‘dead’

### mar,
mar, p 1 o- sophy. The entries treating these branches of science in this dictionary, virtually contain the most important phases of their history. Two other characteristic features of this dictionary: HYBRID WORDS Scientists are rarely also linguists. This is why many scientific terms are inexactly coined and often erroneous and misleading in sense. Many of these te
```


## [2026-09-07T16:30:17.163Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\nfor m in re.finditer(r'mortgage',t):\n    s=re.sub(r'\\s+',' ',t[m.start()-60:m.start()+380])\n    if 'pledge' in s or 'mort' in s[:80]:\n        print(s); print('---')\nEOF"
}
```


### [2026-09-07T16:30:18.677Z] TOOL RESULT

```
 wage and cp. wed. Cp. also the second element in mortgage, gage, tr. v., to offer as pledge. — F. gager, fr. gage. See gage, ‘pledge’, and cp. engage, gage, n., a variety of plum. — See greengage, gage, n. — See gauge. gageite, n., a hydrous silicate of magnesium, manganese and zinc (mineral.) — Named after R.B. Gage of Trenton, New Jersey. For the end¬ ing see subst. suff. 
---
 hypo- theca, fr. Gk. 6txo9x]X7), ‘a deposit, pledge, mortgage’, from the stem of uxoxiSevou, ‘to put under, lay down, pledge’, which is formed fr. 6x6 (see hypo-) and xt&svai, ‘to put, place’. See thesis. hypothecary, adj., pertaining to a hypothec. — Late L. hypothecate, ‘pertaining to a hypo¬ thec’, fr. hypotheca. See prec. word and adj. suff. -ary. hypothecate, tr. v., to pledge a
---
ecurity without transferring possession or title ; to mortgage. — ML. hypothecate, pp. of hypothecate, ‘to pledge’, fr. Late L. hypotheca. See hypothec and verbal suff. -ate. Derivatives: hypothecation (q.v.), hypothecat¬ or, n. hypothecation, n. — ML. hypothecate, gen. -dnis, fr. hypothecate, pp. of hypothecare. See prec. word and -ion. hypothesis, n., a supposition. — ModL., fr. Gk. 6x6&eo
---
me, be consumed’. See morbid, mordant and cp. mort, mortgage, mor¬ tician, mortify, mortuary, amortize, immortal, immortelle, ambrosia, amrita, smorzando. Cp. also murder, murrain. Derivatives: mortal, n., mortal-ism, n., mortal- ist, n., mortdl-ize, tr. v., mortal-ly, adv. mortality, n. — ME. mortalitee, fr. MF. (= F.) mortalite, fr. OF. mortalite, fr. L. mortalitdtem, acc. of mortdlitas, 
---
tr. v., to bind together with mortar, mortar-y, adj. mortgage, n. — ME. morgage, fr. OF. morgage, mortgage, lit. ‘dead pledge’ (replaced in Modern French by hypotheque). See mortal and gage, ‘pledge’. Derivatives: mortgage, tr. v., mortgage-able, adj., mortgag-ee, n., mortgag-er, n., mortgag-or, n. mortician, n., a funeral undertaker. — Coined on analogy of physician fr. L. mors, gen. mor
---
, adj. mortgage, n. — ME. morgage, fr. OF. morgage, mortgage, lit. ‘dead pledge’ (replaced in Modern French by hypotheque). See mortal and gage, ‘pledge’. Derivatives: mortgage, tr. v., mortgage-able, adj., mortgag-ee, n., mortgag-er, n., mortgag-or, n. mortician, n., a funeral undertaker. — Coined on analogy of physician fr. L. mors, gen. mortis. See mortal. mortification, n. — ME. mortif
---
potheque). See mortal and gage, ‘pledge’. Derivatives: mortgage, tr. v., mortgage-able, adj., mortgag-ee, n., mortgag-er, n., mortgag-or, n. mortician, n., a funeral undertaker. — Coined on analogy of physician fr. L. mors, gen. mortis. See mortal. mortification, n. — ME. mortificacion, fr. MF. (= F.) mortification, fr. Late L. mortificationem, acc. of mortificatio, ‘a killing, putting to d
---
al and gage, ‘pledge’. Derivatives: mortgage, tr. v., mortgage-able, adj., mortgag-ee, n., mortgag-er, n., mortgag-or, n. mortician, n., a funeral undertaker. — Coined on analogy of physician fr. L. mors, gen. mortis. See mortal. mortification, n. — ME. mortificacion, fr. MF. (= F.) mortification, fr. Late L. mortificationem, acc. of mortificatio, ‘a killing, putting to death’, fr. mortifica
---
```


## [2026-09-07T16:30:26.363Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\nfor m in re.finditer(r'mar,\\s*tr\\. v|mar,\\s*ir\\. v|mar,\\s*v\\.',t):\n    print(re.sub(r'\\s+',' ',t[m.start():m.start()+500])); print('---')\nEOF\necho \"### SKT MAR\"\ngrep -n -A4 \"^MAR, to\\|^MAR\\b\" SKT.txt | head -20\necho \"### SKT SMART\"\ngrep -n -A5 \"^SMART\" SKT.txt | head -14"
}
```


### [2026-09-07T16:30:27.916Z] TOOL RESULT

```
### SKT MAR
### SKT SMART
```


## [2026-09-07T16:30:32.318Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\ni=t.find('to injure, damage')\nprint(re.sub(r'\\s+',' ',t[i-300:i+500]))\nEOF\necho \"### SKT search Mar / Smart\"\ngrep -n -i \"^Mar (1)\\|Mar, to spoil\\|MAR (1)\\|to spoil, injure\" SKT.txt | head -5\ngrep -n -i \"smeortan\\|mierran\\|merran\" SKT.txt | head -10"
}
```


### [2026-09-07T16:30:33.829Z] TOOL RESULT

```
### SKT search Mar / Smart
```


## [2026-09-07T16:30:37.793Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"smart\" SKT.txt | head -5\necho \"---\"\ngrep -n -i \"\\bMar\\b\" SKT.txt | head -5\necho \"--- size\"; wc -l SKT.txt"
}
```


### [2026-09-07T16:30:37.864Z] TOOL RESULT

```
9740:knave,  a  boy.  ^ivont,  sl\  fellow.  (£. ; ptrhafs  C.)  M.  E.  huiui  \knavt\  a  boy, servant.  A.  S.  cnafa^  older  form  cnafa^ a  boy.  (So  also  Do.  knaaf,  a  lad,  ser- i-ant ;  Icel.  knapi,  scr\*anl-lioy ;  G.  knabe^ boy.)  All  of  Celtic  origin  (the  Celtic  boys being  servants  to  the  Teutons);  cf.  Gnel. enaf^chf  a  yomigster,  a  stout  smart  boy, orig.  an  adj.  signifying  knobby,  lumpy, stout  \  from  the  sb.  rna/,  a  knob.  We may  therefore  regard  it  ns  ultimately  a dcri>'ative  of  knop ;  see  Ijelow.
13789:Perk,  to  make  smart  or  trim.  (W.)  W, pen,  compact,  trim ;  percu,  to  smarten, trim  ;  peirus,  smart.
14063:pimp,  a  pandar.  (F.-L.)  Orig.  a smartly  dressed  fellow.  —  F.  pimprr,  to dress  ap  smartly.  A  nosali&ed  form  or  F, pipeK  to  pipe,  also  to  bcjjuile,  cheat ;  cf. auo  Prov.  pimpar,  to  render  elegant,  from pimpa,  sb.  (equivalent  to  F.piptau)  mean- iog  (1)  &  pip^'  (')  A  bird-call,  a)  a  snare  [ b&idcs  which,  F.  /i/Vr  meant  to  excel  in  a thing.  Note  also  F.  pimpant.  smart, fipnicc:  and  sec  Littri.  —  ll  pipart,  to chirp  (hence  to  pii)cV
15008:BwonmU'  up  smartly,  trim;  Gascni^e
15580:^ip  (I),  to  strike  smartly;  «  smnrt stroke.  (Scand.)  Dan,  rap,  a  rap,  lap: Swcd.  nj//,  a  blow  j  Swed.  rappa,  to  beat or  imitative  origin  ;  allied  to  Battle. Bap  u).  to  seize  hastily;  tec  Bape  (i). Hapacioas;  see  Rapid. Baps  (i),  a  seizing  by  force.  (Scand.) M-E.  rape,  haste,  hurry.  The  word  has been  affected  by  a  popular  etymology  con nectiog  it  with  L.  raptre,  to  which  it  is unrelated ;  see  rapt  ^below).  Tile  M.  E. rapt,  huiry.  hobtc,  is  a  common  word ;  src Chftocer's  lines  to  Adam  Scrivener. —  Icel. krap,  ruin,  falling  down,  hrapt^r^  a  hurry, hrttpa,  to  hasten  ;  Swed.  rapp,  Dan.  rap, quick  ;  sec  rap  (j)  below.  Der.  rapt,  verb. raffle,  a  kind  of  lottery.  (K.  -  G.) M.  £.  rajle,  a  gnme  at  dice,  — F.  niyCf, ra^i,  a  game  at  three  dice.  — F.  rajter,  to snatch  no.  — G.  raffeln,  to  snatch  up;  fre> qucDL  of  raffen^  to  snatch  away,  cany  off hastily.     Sec  below.
---
599:alchemist^s  uuignun  of  mala^ma,  a  molli- fying application ;  jwrh*^  with  Arab,  al \  '■the)  prcfixerU^Gk.  /ia\a7/ia,  an  emol- lient. *Gk.  itoXaacup  (for  it^KnK-yuv),  to soflcn.  -Gk.  ^laAoiwSr,  soft.    (^MAR.) Amanuensis.  (L.)    See  Manual. Amaranth,  an  unfadinE  flower.     (L.- Gk.)     Properly  amarant,  as  in  Milton  ;  but -anth  is  due  to  confusion  with  Greek  d*"^!, a  flower.  M  L.  amamu/us.  «Gk.  dfiapavror, unfading,  or  as  sb.  unfading  flower. —.Gk. d;  not;  and  fiapalvnv,  to  fade.    (^M.\R.) A.ma8S.  (F.  —  L.  —  Gk. )     See  Macerate. Amatory.  (L.)      L.  ama/oriiu,  loving, —  I.,  amator,  a  lover. —  I,,  amare,  to  love; with  suflix  -tor.    (VKAM.)
7625:claymore,  a  Scottish  bfosflsword. ^GaeL)  Gael.  c'aUMtamk  mcr.  n  jjteil sword.  Here  ciaidheamh  is  cognate  wtili W.  deddyf^  cUddru,  a  sword,  and  with  L glAiiut  The  Gael.  mar.  great,  is  alUfld lo  W.  mawr,  L.  magnus,  great.
9580:iljr  \Mar«).     ui  hsx,jumh-U,jamb-
10037:Ziawn  <i>.  a  spaoe  of groB&d,  a  glade.  ^F.  •  G.  «r  C) lammd  (the  ^  has  beca  droppedV  * isiuSr.  'a  land  or  laaad,  a  vild. khrabbj.  or  grassy  piaa;'  CoL  C£ andSpaa.JbMb*a£cath.  p.  Of  £Mrf origin  ;  rcicned  by  Littr^  to  G.  JUW  f  H /ana),  opes  ooaatiy :  aad  by  Dtei  to  Sa jami,  a  ba»hy  shmb^  of  which  the  j latmam  means  'waste  lands.'  Perfaaia cotDCS  to  the  same  chiag ;  fisr  £.  and  I Idrnd  mar  be  the  same  as  Ihsh  Zsaa.  i (enclosed)  piece  of  land,  ii  the  waK, '  enclosure  *  be  not  originaL  Cf-  W.  XM Gael  lattHj  an  endosurc  piece  of  ba^  |
10941:match  (i),  an  equal,  a  contest,  mar- riage. (E.)  M.  K.  maccht,  maeht,  orig.  b comrade.  *  A.  S.  mmaa^  commonly^mtxirtra, a  comrade,  companiofi,  spouse;  from  the more  original  form  maca^  a  companion. See  further  below.
--- size
24055 SKT.txt
```


## [2026-09-07T16:30:48.003Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -o \"mortarium[^\\n]\\{0,200\\}\" WEB_vol1.txt | head -4\necho \"### WEB mar\"\ngrep -n -o \"merran[^\\n]\\{0,200\\}\\|mierran[^\\n]\\{0,200\\}\" WEB_vol1.txt | head -4\necho \"### FSD mar\"\ngrep -n -o \"mierran[^\\n]\\{0,200\\}\\|merran[^\\n]\\{0,200\\}\" FSD_vol3.txt | head -4\necho \"### FSD smeortan\"\ngrep -n -o \"smeortan[^\\n]\\{0,240\\}\" FSD_vol4.txt | head -4"
}
```


### [2026-09-07T16:30:49.342Z] TOOL RESULT

```
### WEB mar
112709:merran in amerran, amyrran, to dissipate, hinder, obstruct.] to BHG or damage so as to make imperfect, aae ee etc.; to spoil; to impair; to ae ee hurt, deform, injure.
### FSD mar
30370:merrantile svstem See mfri'antile —
### FSD smeortan
```


## [2026-09-07T16:30:52.122Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '112700,112715p' WEB_vol1.txt"
}
```


### [2026-09-07T16:30:52.178Z] TOOL RESULT

```
ma/ple scale, in entomology, any one of a great number of scale insects affecting maple
ees.
ma’ple sir/up, sirup made by boiling down the sap of a certain variety of maple.
ma/ple sug/ar (shyg’), sugar made by boiling down maple sirup.
ma’/ple worm, in zoology, a moth larva that injures or destroys leaves of the maple.
mi/qui (-ké), n. [Sp., from native name.] an ornamental evergreen shrub of the linden family in Chile, whose tough bark is used for making strings for native musical in- struments and its berries for making wine; the Aristolelia maqui.
mii-quis’ (-ké’), n. [Fr., from It. macchia, a thicket, from L. macula, a spot.]
1. a zone of shrubby plants, chiefly_ever- greens, growing in the area around the Medi- terranean, known as a hiding place for fugi- tives, guerrilla fighters, etc.
2. [often M-] pl. mä-quïs’ (-ké’), a French guerrilla fighter against the Nazis in World War II; a member of the military branch of the French underground movement (French Forces of the Interior).
mar, v.t.; marred, pt., pp.; marring, ppr. (ME. marren, merren, from AS. merran in amerran, amyrran, to dissipate, hinder, obstruct.] to BHG or damage so as to make imperfect, aae ee etc.; to spoil; to impair; to ae ee hurt, deform, injure.
blemish; a disfigurement.
maple bor’
å [S. Am.] a lar i i i l. ge guinea pig of Pata- fare Dolichotis patachonica, resembling a a ene cavy of Patagonia.
bit, hermit]. [Fr.; Port. marabute; Ar. mura-
. any ofa knd found in Was especially one : sof putant, a bird of India. tail of Racseuers from the wing coverts and 4. a delja eTabou, used in millinery. dyed Ca white raw silk that can be been taken aoe the natural gum has not
- the Offspri 5 Per: Pring of a griffe z Mara pag cighths Neng! DS mulattora bit, hermit) ETS Port. marabuto; Ar. murā- ae Moslem h z Yam €rmit or holy man, espe- . the to 8 the Berbers and Moors.
```


## [2026-09-07T16:31:08.128Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nimport re\nt=open('ARY_pages.txt',encoding='utf-8').read().split('\\f')\nprint('leaves',len(t))\nfor i,p in enumerate(t):\n    for w in ['خاموش','فراموش','مرغ','سیمرغ']:\n        if w in p:\n            m=re.findall(r'\\[pdf page (\\d+)\\]',p)\n            print(w,'leaf',i,'tag',m[:1])\nEOF"
}
```


### [2026-09-07T16:31:09.440Z] TOOL RESULT

```
leaves 545
مرغ leaf 226 tag ['227']
مرغ leaf 232 tag ['233']
مرغ leaf 400 tag ['401']
```


## [2026-09-07T16:31:12.780Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY\npython3 - <<'EOF'\nt=open('ARY_pages.txt',encoding='utf-8').read().split('\\f')\nfor i in (226,232,400):\n    p=t[i]\n    j=p.find('مرغ')\n    print('==== leaf',i)\n    print(p[max(0,j-700):j+500])\nEOF"
}
```


### [2026-09-07T16:31:14.015Z] TOOL RESULT

```
==== leaf 226
[pdf page 227]
۸ | _چه چي (به چم "چه چیزی)
پسگشت‌ها دشر داد 7 (11006) :01025
۳ 17
0 (1300) 8۸82/0 برهان قاطع زا 9 : ۶۶۴
10 84 او

یادداشت: 1

۱- چم این واژه در برهان قاطع : چنین است: قلاب» کجکه (قلابی که با آن فبل را رانند)» پنجه و انگشتان مردم»

چنگال مرغان و جانوران دیگر (برهان قاطع :: ۹3۴)

۲ چم این واژه در اوستی: بازو,

چم این واژه در کردی: دست.

چم این واژه در ایسلندی کهن: خانه,

چم این واژه در اکثر زبان‌های ژرمنی: قلاب, ۱

1

| جمانگلیس سرواژهی را ی ۵5
اوستایی ((4874): 37 ,۲17 نروژی (08۷۴01۵۷/): 11۷۸ ,3۷1 ,11۷1
پارسی باستان (۶88814۷ 010): لهستانی (۳0[5): اد

,030 روسی (//551۸)+ 11

پپلوی (41آللم). دز چکه (2504)): 40 باآ۳03
تخاری ۸ (۸ ۸(7ل70727۸7): 18 اسلواکی (5701430): 1
تخاری 8 (8 (4۸7ق707): ناه ایرلندی کهن (5[0ل1# صان): ه
سانسکریت (5(/
==== leaf 232
[pdf page 233]
۴ | خاییدن»- خای (به چم
1 دانمارکی (0۸/۷/87): ادا ولزی (#1.97): ۷
سوئدی (35015/7): ۸6 برتونی (/87270۸): 71
۱ نروژی (/0/07۳80149: 506 گالبک (048010]: 5 اقلا
هلندی (007077): 2۱ رم
اسلاوی کهن (۲12شا5 070674 0ا0): پسگشت‌ها ۳۳
۸18 20080
لهستانی (20517): 0 ,تل۸ل 7 (800) ره
روسی (0ل805514): ۰ 3۸1780 ,1۸700 ۳ اد
چکه (2507)): 8 ,۷۸۳5
صربی (//88781۸): 18 ۶ (666 مت
بوهمی (807/8(44/1): ۷0 26 علاط
ایرلندی کهن (81#/# صله): 0۰ 3 (860) :002/5
گالی (37/ال0۸): ۷۷ 0 (866) 7
برهان قاطع + ۷۱
بادداشت:
۹ ۱ چم این واژه در اوستایی و پارسی باستان و پهلری و همه‌ی زبان‌های هند و اروپایی دیگر: تخم (مرغ).
۲ واژه‌های "خاویار" و "خاک" و "خاگینه" نیز همریشه‌ی واژه‌ی "خایه" هستند.
اوستایی (/472574): ۸8۰ ر-۸۷1ا وه
پارسی باستان (/۸ا۸878 02): -1۸۸۷ پسگشت‌ها انخ هبات
سانسکریت (84(51)/7): ۳
۰ ,۸31۸0۸5 ,۴71۸0۸7 809 غل‌لاه
ارمثی (01فا/47/52): ادن ۱۵ برهان قاطع : ۷۱۲۰
یونانی 0888210): 005
لاتین (47100ا): 315
لینوانی (0للاتال72/.ا): درون
یادداشت:
چم این واژه در زبان یونانی: خمیده,
چم این واژه در زبان لاتین: کجکه» قلاب.
۳"

==== leaf 400
[pdf page 401]
اک 66666
۲ | کرک (به چم *مرغ خانگی») ۱
اوستایی (47887/07): کرد ناه روسی ((8/5514): ۳8۵۲ ,۳3۵0175110 رین
پهلری (7شاتلمم): ۸ چک (2507)). ها ده 0:۱
اوستی (05587/6): ۸۴ بلناری (8004۵(۷7): 00
: کردی (70157): 8 نها صربی (52/810): هار
آفغانی (پشت) (47017۸427)+ نا اسلوا کی (8101۸20): هه
تخاری ۸ (۸ للم ۰:70 8۸۲۵0 لیتوانی (/(۵4ا07فتا777).
سانسکریت (54/577): 0 ت30
۷6۰ کته دنله شنز لترنی (لتی) (7۲1۵/۷ا):
ارمنی (47ا۸7/87): ننشای ۱ 7 203۵۳
بونانی (072510): کید اه پروسی کهن (انفاکدت۲۸ صامم): ۸۲70
لانین (4700ه): ‏ 0۸88 ,ق0830 ایرلندی ک
```


## [2026-09-07T16:31:19.520Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"### $f\"; grep -n -o \"فراموشیدن[^\\n]\\{0,160\\}\" $f | head -3; grep -n -o \"فراموش \\[[^\\n]\\{0,120\\}\" $f | head -3; done"
}
```


### [2026-09-07T16:31:21.099Z] TOOL RESULT

```
### MON_part1.txt
### MON_part2.txt
```


## [2026-09-07T16:31:24.751Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -c \"فراموش\" MON_part1.txt MON_part2.txt\ngrep -n -o \"فراموش[^\\n]\\{0,120\\}\" MON_part2.txt | head -6\necho \"### مرغ in MON\"\ngrep -n -o \"مرغ (\\|مرغ \\[[^\\n]\\{0,100\\}\" MON_part2.txt | head -5"
}
```


### [2026-09-07T16:31:26.482Z] TOOL RESULT

```
MON_part1.txt:21
MON_part2.txt:27
2085:فراموش 
2087:فراموشی» نسبان. نادانی. 
5784:فراموش: ۸۲5-4 [- فراموش - فرامشت 
5791:فراموشی عادت دارد؛ ی حافظه. 
5795:فراموشی دادن: کاملاً از باد 
7018:فراموش نمی‌کند و هر سال یکبار به دیدن 
### مرغ in MON
28882:مرغ (
56739:مرغ (
87145:مرغ (
```


## [2026-09-07T16:31:29.874Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '5780,5800p' MON_part2.txt\necho \"=== مرغ entries\"\nsed -n '56735,56750p' MON_part2.txt"
}
```


### [2026-09-07T16:31:29.948Z] TOOL RESULT

```
معلوم کردن. آموختن؛ یاد گرفتن. گسترش 
بافتن؛ گستر ده 4 ۳ و گرگ عادت کر دن. 
فسرام‌اسون: ۸ ۱۸۲ (۱.) عسصو 
فراماسو نری. 
فراموش: ۸۲5-4 [- فراموش - فرامشت 
- فرموش] () از یاد رفتن» از خاطر محو 
شدن. (ص.) از باد رفته» از خاطر محو شده. 
فر اموشخانه: (۱230۸۵ (۱.) این کلمه را 
بجای «فراماسونری» به مناست شباهت 
لفظی و معنوی در فارسی معمول کر ده‌اند. 
فرامسوشکار: 8 (ص‌فا») آنکه 
فراموشی عادت دارد؛ ی حافظه. 
۳ ۱ 0 [- فرامشی 

مشتی | (حامص.) از یادرفتگی. نسبان؛ مق. 
1 ذ کر. به باد فراموشی دادن: کاملاً از باد 
بر دن. 
ثرامین: ۸ ا(معر .] (.) ج‌. 4 ور 
ضح.- «ایز ن تصرف فارسی زبانان عربی‌دان 
است که جمع لفظ فارسی را بطور عربی 
آورده‌اند.» (غیاث. آنند.) ولی در عربی هم 
=== مرغ entries
مسعی : ۱۸57 [ع.] .۲ سعی» کوشش. 
مسلکك؛ راه. تصر ف؟ ج. مساعی. 

مسف: ۱052100 [ع.] (امف. . مک.) محل 
پریدن مرغ (نزدیکك زمین). 

شتا ۰۵۵۲ |ع.] (افا.) ابر نزدیکك 
شسو ند ه۵. مر غ بر نده نز دبک ز ممن. 

مسقّط؛ ادونه [ع.] (. مک.) جای افتادن 
جبزی» محل سقو ط» مسقط؛ ج. مساقط . 
مسقط: 25,۵ [ع.] (. مک.) محل افتادن 
چبزی» محل سقوط مسقط؛ ج. مساقط. 
محل تولد کودک. مسقط رأس: محل تولد؛ 
زادگاه» مسقط 7۳
```


## [2026-09-07T16:31:53.038Z] TOOL CALL #95: Bash

```json
{
 "command": "ls site/pages/336.jpg 2>/dev/null; pdftoppm -f 336 -l 336 -r 150 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg336 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-07T16:31:54.570Z] TOOL RESULT

```
site/pages/336.jpg
total 16664
drwx------ 2 sfmqrb sfmqrb     4096 Sep  7 12:31 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  7 11:48 ..
-rw-rw-r-- 1 sfmqrb sfmqrb     8635 Sep  7 12:07 318-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   101267 Sep  7 12:07 318-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61586 Sep  7 12:18 320-bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115970 Sep  7 12:18 320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86272 Sep  7 12:18 320-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13284 Sep  7 12:18 320-zoom.png
-rw-rw-r-- 1 sfmqrb sfmqrb   107524 Sep  7 12:27 328-top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      471 Sep  7 12:18 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    14937 Sep  7 11:56 arrows.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1413 Sep  7 12:27 box1b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1385 Sep  7 12:27 box1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1132 Sep  7 12:27 box2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1988 Sep  7 12:27 box2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    85949 Sep  7 11:57 bqt2002_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72256 Sep  7 11:58 bqt2002_f1.png
-rw-rw-r-- 1 sfmqrb sfmqrb   161214 Sep  7 11:57 bqt2002_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    83643 Sep  7 12:12 build.py
-rw-rw-r-- 1 sfmqrb sfmqrb     7075 Sep  7 12:13 c331_av1.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10759 Sep  7 12:13 c331_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3537 Sep  7 11:53 c_migare2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1829 Sep  7 11:53 c_migare3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2261 Sep  7 11:53 c_migare4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3958 Sep  7 11:53 c_migare.png
-rw-rw-r-- 1 sfmqrb sfmqrb    19652 Sep  7 11:53 c_semita2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2639 Sep  7 11:53 c_semita.png
-rw-rw-r-- 1 sfmqrb sfmqrb    40259 Sep  7 11:50 ferdowsi2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30950 Sep  7 11:51 ferdowsi3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    28946 Sep  7 11:51 ferdowsi4.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4298 Sep  7 11:50 ferdowsi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     9383 Sep  7 11:55 masjid.wiki
-rw-rw-r-- 1 sfmqrb sfmqrb    33701 Sep  7 12:04 mk319a.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46151 Sep  7 12:09 mk319b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51516 Sep  7 12:09 mk322.py
-rw-rw-r-- 1 sfmqrb sfmqrb    61981 Sep  7 12:06 mk323.py
-rw-rw-r-- 1 sfmqrb sfmqrb    37635 Sep  7 12:04 part_a.json
-rw-rw-r-- 1 sfmqrb sfmqrb    58545 Sep  7 12:09 part_b.json
-rw-rw-r-- 1 sfmqrb sfmqrb    97817 Sep  7 11:50 pg318hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    62558 Sep  7 11:50 pg318.png
-rw-rw-r-- 1 sfmqrb sfmqrb    67293 Sep  7 11:54 pg319.png
-rw-rw-r-- 1 sfmqrb sfmqrb   146848 Sep  7 12:01 pg320hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80891 Sep  7 12:00 pg320.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71522 Sep  7 12:00 pg321.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72193 Sep  7 11:57 pg323.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65279 Sep  7 11:49 pg324.png
-rw-rw-r-- 1 sfmqrb sfmqrb    55902 Sep  7 11:58 pg326.png
-rw-rw-r-- 1 sfmqrb sfmqrb   163982 Sep  7 11:53 pg327hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    73619 Sep  7 11:52 pg327.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69765 Sep  7 12:12 pg329.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72757 Sep  7 12:13 pg330.png
-rw-rw-r-- 1 sfmqrb sfmqrb   128240 Sep  7 12:13 pg331hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    94945 Sep  7 12:12 pg331.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75312 Sep  7 12:17 pg332.png
-rw-rw-r-- 1 sfmqrb sfmqrb   104609 Sep  7 12:27 pg333hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70886 Sep  7 12:26 pg333.png
-rw-rw-r-- 1 sfmqrb sfmqrb    41782 Sep  7 12:18 pg334_bot.png
-rw-rw-r-- 1 sfmqrb sfmqrb    97297 Sep  7 12:18 pg334.png
-rw-rw-r-- 1 sfmqrb sfmqrb    58407 Sep  7 12:18 pg334_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    88659 Sep  7 12:22 pg335.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57846 Sep  7 12:31 pg336.png
-rw-rw-r-- 1 sfmqrb sfmqrb    60414 Sep  7 12:19 pg337.png
-rw-rw-r-- 1 sfmqrb sfmqrb        0 Sep  7 12:18 queue.txt
-rw-rw-r-- 1 sfmqrb sfmqrb       49 Sep  7 12:17 sns53.png
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n53.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb    35039 Sep  7 12:17 sns_n54.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  1021826 Sep  7 12:18 sns_p54.png
-rw-rw-r-- 1 sfmqrb sfmqrb 12288786 Sep  7 12:18 sns_text.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb     1308 Sep  7 11:54 v2001.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    27253 Sep  7 12:02 z_maqd2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    63140 Sep  7 12:02 z_maqd3.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4293 Sep  7 12:01 z_maqd.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2895 Sep  7 12:01 z_meh.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25378 Sep  7 12:01 z_mezna2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    33685 Sep  7 12:01 z_mezna.png
```


## [2026-09-07T16:31:58.090Z] TOOL CALL #96: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg336.png"
}
```


### [2026-09-07T16:31:58.118Z] TOOL RESULT

```

```


## [2026-09-07T16:32:23.168Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n -i \"forget\" KNT.txt | head -5\necho \"--- mars/mrs in KNT lexicon\"\ngrep -n -i \"\\bmarš\\|mṛš\\|marsh\" KNT.txt | head -5\necho \"=== KNT martiya\"\ngrep -n -o \"martiya[^\\n]\\{0,100\\}\" KNT.txt | head -3"
}
```


### [2026-09-07T16:32:24.411Z] TOOL RESULT

```
--- mars/mrs in KNT lexicon
1526:*mer- ‘die’ in marika- ‘menial person’ (see Lex. s.v.), *mor- in martiya ‘man’ (see Lex. s.v.), *mr- in marta ‘dead’, uvä-maršiyuš ‘by self- death’ (see Lex. s.v.); perhaps *m»r- in amari- yata ‘he died’ (cf. Av. miryeite ‘he dies’).
1838:I. Stems in -й-: adj. par-u-, ard-u- in personal name Ardu-mants-, va-u- in personal names Déraya-vau- Vau-misa- Vahau-ka-; substantives baru- in Gau-barw-a-, maršiy-u- ‘death’ in adj. uvd-marSiyu-, mard-u- in Marduniya-, Mag-u-, Hitd-u-, Marg-u-, Kür-u-, uncertain bat-u- in bátu- gara-; loanwords pir-u-, Ufrat-u-; restored loan- word agur-u-; uncertain as to stem, Qatag-u-, sikabr-u-.
=== KNT martiya
585:martiya, Skt. mártya- .
616:martiyahya, Skt. -asya.
635:martiya for -ya?, Skt. -yah. The unwritten consonants may be represented by raised letters in normalized tr
```


## [2026-09-07T16:32:33.924Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/smart\" \"https://www.etymonline.com/word/mar\"; do python3 tools/fetch_source.py \"$u\" --note \"page 336: entry 0 node 4 (smart), entry 1 node 7 (mar)\"; done\nhead -c 400 data/verification/sources/web/$(python3 -c \"\nimport hashlib;print(hashlib.sha1('https://www.etymonline.com/word/smart'.encode()).hexdigest()[:16])\").txt"
}
```


### [2026-09-07T16:32:36.163Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a53efd3dca02a84a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0891ec24b1e7e921.txt
URL: https://www.etymonline.com/word/smart
FETCHED: 2026-09-07T16:32:35Z
STATUS: 200
TITLE: Smart - Etymology, Origin & Meaning

Smart - Etymology, Origin & Meaning 

 Search 
 Log in 

 Columns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of smart 

 smart (v.) 

 M
```


## [2026-09-07T16:32:40.487Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nsed -n '/Origin and history of smart/,/smart (n.)/p' a53efd3dca02a84a.txt | head -40\necho \"#### MAR\"\nsed -n '/Origin and history of mar/,/Entries linking/p' 0891ec24b1e7e921.txt | head -25"
}
```


### [2026-09-07T16:32:41.704Z] TOOL RESULT

```
 Origin and history of smart 

 smart (v.) 

 Middle English smerten , "to cause pain, to suffer pain," from Old English smeortan "be painful," in reference to wounds, from Proto-Germanic *smarta- (source also of Middle Dutch smerten , Dutch smarten , Old High German smerzan , German schmerzen "to pain," originally "to bite"). According to Watkins the Germanic word is perhaps cognate with Latin  mordēre  "to bite, bite into," figuratively "to pain, cause hurt," and both might be from an extended form of PIE root  *mer-  "to rub away, harm." Usually of a lively, pungent, local pain. Related: Smarted; smarts ; smarting .

 smart (adj.) 

 Middle English smert , from late Old English smeart , in reference to hits, blows, etc., "stinging; causing a sharp pain," related to smeortan "be painful" (see smart (v.)). The adjective is not represented in the cognate languages.

 Of speech or words, "harsh, injurious, unpleasant," c. 1300; thus "pert, impudent; on the impertinent side of witty" (by 1630s). In reference to persons, "quick, active, intelligent, clever," 1620s, perhaps from the notion of "cutting" wit, words, etc., or else "keen in bargaining."

 From 1718 in cant as "fashionably elegant;" by 1798 as "trim in attire," "ascending from the kitchen to the drawing-room c. 1880" [Weekley]. For sense evolution, compare sharp (adj.); at one time or another smart also had the extended senses in sharp .

 Attested from late 12c. as a surname, earlier as a component in them, including Christiana Smartknave (1279). In reference to devices, the sense of "behaving as though guided by intelligence" is attested by 1972 ( smart bomb , also the computing smart terminal ). The figurative smart cookie "clever, perceptive person" is by 1926 in newspaper baseball stories.

 smart (n.) 
#### MAR
 Origin and history of mar 

 mar (v.) 

 Middle English merren "to deface, disfigure; impair in form or substance" (early 13c.), from Old English merran (Anglian), mierran (West Saxon) "to waste, spoil," from Proto-Germanic *marzjan (source also of Old Frisian meria , Old High German marren "to hinder, obstruct," Gothic marzjan "to hinder, offend"), from PIE root *mers- "to trouble, confuse" (source also of Sanskrit mrsyate "forgets, neglects," Lithuanian miršti "to forget"). For vowel change, see marsh . Related: Marred ; marring .
 also from early 13c. 

 Entries linking to mar
```


## [2026-09-07T16:33:25.445Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\nfor u in \"https://www.etymonline.com/word/mortar\" \"https://www.etymonline.com/word/morbid\" \"https://www.etymonline.com/word/mortgage\" \"https://www.etymonline.com/word/remorse\" \"https://en.wiktionary.org/wiki/morbus\" \"https://en.wiktionary.org/wiki/mortarium\"; do python3 tools/fetch_source.py \"$u\" --note \"page 336 entry 0: Latin and English nodes of Mer 2\"; done\npython3 tools/fetch_source.py \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/mr̥gáh\" --note \"page 336 entry 4: Proto-Iranian bird word\""
}
```


### [2026-09-07T16:33:31.173Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/e7b8e2757f3427b9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/a47936616fc09495.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/e8efa014c245e275.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/ef4728fc3928e012.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1e804daf11c79c0d.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/188e9fe0efdaedb9.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/99227a4589d473a4.txt
```


## [2026-09-07T16:33:37.611Z] TOOL CALL #101: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\nfor f in e7b8e2757f3427b9 a47936616fc09495 e8efa014c245e275 ef4728fc3928e012 1e804daf11c79c0d 188e9fe0efdaedb9 99227a4589d473a4; do echo \"===== $f\"; sed -n '3,4p' $f.txt; done\necho; echo \"#### mortar\"; sed -n '/Origin and history of mortar/,/mortar (v/p' e7b8e2757f3427b9.txt | head -20\necho \"#### morbid\"; sed -n '/Origin and history of morbid/,/Entries linking/p' a47936616fc09495.txt | head -10"
}
```


### [2026-09-07T16:33:39.047Z] TOOL RESULT

```
===== e7b8e2757f3427b9
STATUS: 200
TITLE: Mortar - Etymology, Origin & Meaning
===== a47936616fc09495
STATUS: 200
TITLE: Morbid - Etymology, Origin & Meaning
===== e8efa014c245e275
STATUS: 200
TITLE: Mortgage - Etymology, Origin & Meaning
===== ef4728fc3928e012
STATUS: 200
TITLE: Remorse - Etymology, Origin & Meaning
===== 1e804daf11c79c0d
STATUS: 200
TITLE: morbus - Wiktionary, the free dictionary
===== 188e9fe0efdaedb9
STATUS: 200
TITLE: mortarium - Wiktionary, the free dictionary
===== 99227a4589d473a4
STATUS: 200
TITLE: Reconstruction:Proto-Iranian/mr̥gáh - Wiktionary, the free dictionary

#### mortar
 Origin and history of mortar 

 mortar (n.1) 

 "mixture of cement, material used (in building) for binding together stones or bricks," mid-13c., from Old French mortier "builder's mortar, plaster; bowl for mixing" (13c.) and directly from Latin mortarium "mortar, mixture of lime and sand," also "crushed drugs," which probably is the same word as mortarium "bowl for mixing or pounding" (see mortar (n.2)), with the sense transferred from the bowl to the material prepared in it. Dutch mortel , German Mörtel are from Latin or French.
 also from mid-13c. 

 mortar (n.2) 

 "bowl for pounding, vessel in which substances are beaten to powder by means of a pestle," c. 1200, from Old French mortier "bowl; builder's mortar" and directly from Latin mortarium "bowl for mixing or pounding," also used of the material prepared in it, a word of unknown origin as it is impossible now to determine which sense was original. Watkins says probably from PIE root *mer- "to rub away, harm;" de Vaan finds this plausible. Late Old English had mortere , from the same Latin source, which might also be a source of the modern word. German Mörser also is from Latin.
 also from c. 1200 

 mortar (n.3) 

 "short cannon, ordnance piece short in proportion to the size of its bore," fired at a high angle and meant to secure a vertical fall of the projectile, 1620s, originally mortar-piece (1550s), from French mortier "short cannon," in Old French, "bowl for mixing or pounding" (see mortar (n.2)). So called for its shape.
 also from 1620s 

 Entries linking to mortar 

 mortarboard (n.) 
#### morbid
 Origin and history of morbid 

 morbid (adj.) 

 1650s, "of the nature of a disease, indicative of a disease," from Latin morbidus "diseased," from morbus "sickness, disease, ailment, illness," according to de Vaan perhaps connected to the root of mori "to die," as "looking like death" (from PIE root *mer- "to rub away, harm," also "to die" and forming words referring to death and to beings subject to death), or from a non-IE word. Meaning "diseased, sickly" is from 1731. Transferred use, of mental states, "unwholesome, excessive, unreasonable" is by 1834. Related: Morbidly ; morbidness . Middle English had morbous "diseased" (early 15c.), from Latin morbosus .
 also from 1650s 

 Entries linking to morbid
```


## [2026-09-07T16:33:46.203Z] TOOL CALL #102: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web\necho \"#### wikt morbus\"; grep -n -A6 \"^ Etymology\" 1e804daf11c79c0d.txt | sed -n '1,30p' | grep -v \"^--$\" | head -20\necho; echo \"#### wikt mortarium\"; sed -n '/^ Etymology$/,/^ Pronunciation/p' 188e9fe0efdaedb9.txt | head -12\necho; echo \"#### PIr mr̥gáh\"; sed -n '/^ Etymology$/,/^ Descendants/p' 99227a4589d473a4.txt | head -20"
}
```


### [2026-09-07T16:33:47.742Z] TOOL RESULT

```
#### wikt morbus
62: Etymology 
63-
64- 1.2 
65- Pronunciation 
66-
67- 1.3 
68- Noun 
85: Etymology 
86-
87- 2.2 
88- Pronunciation 
89-
90- 2.3 
91- Noun 
200: Etymology
201- [ edit ] 
202-
203: Etymology tree
204-
205- Proto-Indo-European *mer- der. ? 

#### wikt mortarium
 Etymology
 [ edit ] 

 From Latin mortārium . Doublet of mortar .

 Pronunciation
 Etymology
 [ edit ] 

 Uncertain. De Vaan suggests that the term could derive from Proto-Italic *morto- , from Proto-Indo-European *mr̥tó- , itself from a possible root *mer- ( “ to die ” ) , whence also Latin morior . [ 1 ] 

 Pronunciation

#### PIr mr̥gáh
 Etymology
 [ edit ] 

 From Proto-Indo-Iranian *mr̥gás .

 Noun
 [ edit ] 

 *mr̥gáh [ 1 ] [ 2 ] 

 hen , bird 

 Inflection
 [ edit ] 

 masculine a-stem

 singular

 dual
```


## [2026-09-07T16:34:40.340Z] TOOL CALL #103: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if '464.' in p:\n        print('leaf(1-based)',i+1)\n        print('header:', repr(p[:40]))\n        j=p.find('464.')\n        print(p[max(0,j-400):j+300])\n        break\nEOF"
}
```


### [2026-09-07T16:34:41.536Z] TOOL RESULT

```
leaf(1-based) 125
header: '— 103 —\n(7) Gl.), rTstjayee, ä/ezJt (Phl'
ai *du willst herabsteigen', d. s^ezun 'hinauf-
steigen' (301).
Das awestische Wort ist nicht sicher; die Päzend-
lesung mit z beweist nichts.
463. xäm *roh, ungekocht'.
ai. amd' *roh*; arm. huni 'roh' (H. No. 171; vergl.
Bartholomae, Studien II, 44. Daneben LW. /aw)5
gr. (Ojiwc; air. 6w.
kurd. xäv; oss. LW. /öm (Hübschniann, S. 133);
afy. öm, um; bei. hämag, n. häniay, liänvcuj (155);
wa/. yüng,
464. yritnös^) ^schweigend, still*, /ämösl.
skr. a + \/^marS' geduldig ertragen' ; vergl. fcrämös
(No. 812).
465. ^Jiän, yßne 'Haus , xänef/T.
phlv. /ßnak, /an, /änaklk (n''Nn"*2, Nöldeke,
ZDMG. 46, 142).
Von i^khan- 'graben'. Vergl. np. (arab.) yendeq
neben kenden,
466. yi^miT 'Quelle, Wasserbassin
```


## [2026-09-07T16:35:12.960Z] TOOL CALL #104: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nt=open('KLN_1966.txt',encoding='utf-8').read()\nfor m in re.finditer(r'\\bmar,\\s*(tr|intr|v)',t):\n    print(re.sub(r'\\s+',' ',t[m.start():m.start()+430])); print('---')\nEOF\necho \"### HRN murg\"\ngrep -n -B2 -A6 \"mury 'Vogel\\|mur/  'Vogel\\|Vogel; Huhn\\|1) mur\" HRN.txt | head -30\ngrep -n \"murf\\|mury\\|murg\" HRN.txt | head -10"
}
```


### [2026-09-07T16:35:14.845Z] TOOL RESULT

```
mar, tr. v., to injure. — ME. merren, marren, fr. OE. merran, mierran, ‘to hinder, obstruct, squander, waste’, rel. to OFris. meria, OHG. marren, merren, ‘to hinder, obstruct , Goth. marzjan, ‘to hinder, offend , OFris. mere, tie, fetter’, and prob. to ON. merja, ‘to crush, bruise’, and cogn. with OI. mrnati, ‘he crushes, bruises’, Gk. p-apatvstv, ‘to put out, quench, extingu
---
### HRN murg
8468-got. marka 'Mark'; air. mruig, bruig; lat. margo
8469-Rand' (weiteres bei Froehde, BB. VII, 327).
8470:975. mury 'Vogel; Huhn, mury[abi 'Ente ^).
8471-mäz. wary.
8472-aw. mereya- 'Vogel'; phlv. mury, murv (auch Papyrus,
8473-Hörn, ZDMG. 43, 51)^); ai. mrgd- 'Waldtiej-; Vogel*.
8474-kurd. vergl. miräwi 'Ente* (H.-Sch.); afy. marya;
8475-oss. d. t. mary 'Vogel* (179); bei. (LW.?) murg, n.
8476-mury *Vogel, Huhn* (243).
8470:975. mury 'Vogel; Huhn, mury[abi 'Ente ^).
8472:aw. mereya- 'Vogel'; phlv. mury, murv (auch Papyrus,
8475:oss. d. t. mary 'Vogel* (179); bei. (LW.?) murg, n.
8476:mury *Vogel, Huhn* (243).
13068:murym 975.
21697:y. muryäh 993.
```


## [2026-09-07T16:35:21.935Z] TOOL CALL #105: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('HRN.txt',encoding='utf-8').read().split('\\f')\nfor i,p in enumerate(t):\n    if \"975. mury\" in p:\n        print('leaf',i+1,'header',repr(p[:20]))\nEOF"
}
```


### [2026-09-07T16:35:23.263Z] TOOL RESULT

```
leaf 240 header '— 218 ~\nmaretan-; pl'
```


## [2026-09-07T16:35:28.735Z] AGENT

Now I'll write the verification file.


## [2026-09-07T16:43:14.554Z] TOOL CALL #106: Bash

```json
{
 "command": "cat > data/verification/page-336.json <<'JSONEOF'\n{\n  \"pdf_page\": 336,\n  \"book_page\": 306,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-07\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Mer 2 / Mer-d, Mer-k / Mor-to / Smerd\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *mer- 'to rub away, wear down, harm' and *mer- 'to die' (Pokorny 4. mer- 'sterben' and 5. mer- 'reiben, wischen', pp. 735-737), with the extensions *mer-d-, *mer-k-, *mer-s-, the o-grade *mor-to- 'mortal, man' and the s-mobile variant *(s)merd- (Pokorny smerd- p. 970)\",\n      \"note\": \"Root, language label and glosses are right. Pokorny prints two lemmas, 4. mer- 'to die' (p. 735) and 5. mer- 'to rub, wipe; to pack, rob' (pp. 735-737), but closes the second with 'See also: identical with mer-4'; Watkins (AHD mer-2) merges them the same way ('Possibly the same root, but more likely distinct, is *mer-, to die'), so Nourai's single box 'Mer 2 ... to rub away, harm, die' follows the standard handbooks. The sub-labels are Pokorny's own extensions: mer-d- (Skt. mardati, Lat. mordeo), mer-k- (Skt. marcayati, Av. mahrka- 'death'), mor-to- ('mor-to- perishable: Skt. marta-, Av. maSa-, OP martiya-'). The one inaccuracy is the reference for 'Smerd: painful': Pokorny's p. 970 lemma is smerd- 'to stink'; the 'pain' words (OHG smerzan, smerzo, Gk. smerdnos, Eng. smart) stand on pp. 736-737 under mer-d-, and p. 970 only cross-refers to them ('smerd- to stink is a probably already Indo-European specialised use from (s)merd- in NHG schmerzen, Lat. mordere, see mer-, merd- above p. 736 f').\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *mer- به دو معنای «ساییدن، فرسودن، آسیب رساندن» و «مردن» است. پوکورنی در ص ۷۳۵ دو مدخل جداگانهٔ mer-4 «مردن» و mer-5 «ساییدن» آورده، ولی خودش در پایان مدخل دوم می‌نویسد «همان mer-4 است»؛ واتکینز نیز در ذیل mer-2 همین دو را یکی گرفته است، پس یکی‌سازی نورایی با سنت فرهنگ‌نویسی هندواروپایی سازگار است. صورت‌های گسترش‌یافتهٔ mer-d-، mer-k-، mer-s- و صورت o-دار *mor-to- «مردنی، آدمی» و گونهٔ با s آغازی *(s)merd- همه از خود پوکورنی است. تنها خطای ارجاع این است که ص ۹۷۰ پوکورنی مدخل smerd- «بوی بد دادن» است و معنای «دردناک» (smerzan، smart) در ص ۷۳۶–۷۳۷ آمده؛ پوکورنی در ص ۹۷۰ فقط به آن صفحه ارجاع می‌دهد. ادعای نورایی در مجموع درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/morbus\",\n        \"https://en.wiktionary.org/wiki/mortarium\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:735\", \"status\": \"supports\", \"note\": \"POK_full.txt lines 60116-60311: 'Root / lemma: mer-4, mera- / Meaning: to die ... Page(s): 735' and 'Root / lemma: mer-5, mera- / Meaning: to rub, wipe; to pack, rob ... mer-d-: ... Latin mordeo ... mer-k-: ... Page(s): 735-737', ending 'See also: identical with mer-4'. Both of Nourai's senses and the extensions Mer-d/Mer-k are on that page.\"},\n        {\"ref\": \"POK:970\", \"status\": \"partial\", \"note\": \"POK_full.txt line 78543: 'Root / lemma: smerd-, smord- / Meaning: to stink ... Page(s): 970'. The page carries the form Smerd but glosses it 'to stink', not 'painful'; it adds 'smerd- stink is ... a specialised use from (s)merd- in Modern High German schmerzen, Latin mordere, s. mer-, merd chafe (above S. 736 f)', which is where the 'painful' sense actually stands.\"},\n        {\"ref\": \"AHD:1529\", \"status\": \"supports\", \"note\": \"The page number belongs to the 1976 New College appendix, which is not open online; the corresponding entry in Watkins 1985 (AHD_watkins1985.txt line 753) is 'mer-2, To rub away, harm ... [Pok. 4. mer-, 5. mer- 735.]' and closes 'See extended root smerd-' - exactly Nourai's box, alphabetical position p. 1529 in a 1505-1550 appendix fits 'mer-'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"pp. 735, 735-737, 970 (POK_full.txt lines 60116, 60176, 78543)\", \"stance\": \"supports\", \"note\": \"'mor-to- perishable in Old Indic marta-, Avestan masa- ... Old pers. martiya-'; 'mer-d-: ... Latin mordeo ... compare the s-forms: gr. smerdnos ... Old High German smerzan ache, smerzo pain ... engl. smart'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II pp. 276-279 (WLD_Bd2_pages.txt leaves 280-283)\", \"stance\": \"supports\", \"note\": \"'3. mer- sterben' (p. 276) with ai. marate, lat. morior, mrti- = lat. mors; 'morbus Krankheit (Gdf. *mor-bhos)' (p. 277); 'mer-q-' (p. 278); p. 279 'lat. mordeo ... gr. smerdnos ... ahd. smerzan schmerzen, smerzo Schmerz ... ags. smeortan, engl. smart beissend, scharf, witzig'. WP II 276 ff. is Pokorny's own reference.\"},\n        {\"src\": \"AHD\", \"where\": \"s.v. mer-2 and smerd- (AHD_watkins1985.txt lines 753-754, 962)\", \"stance\": \"supports\", \"note\": \"mer-2 gives MORTAR, MORDANT/REMORSE, MORBID, MORS/MORTAL/MORTUARY/MORTGAGE; 'smerd-. Pain. Extension of mer-2. Germanic *smarta- in Old English smeart, causing pain, painful: SMART. [Pok. smerd- 970.]'\"},\n        {\"src\": \"KLN\", \"where\": \"p. 1461 s.v. smart (KLN_1966.txt leaf 775)\", \"stance\": \"supports\", \"note\": \"'fr. I.-E. base *(s)mer-d-, a d-enlargement of base *(s)mer-, to rub, pound, consume, wear away, exhaust, worry ... Cp. also ... mar, marasmus, marble, ... morbid, ... mordant, morsel, mortal, mortar, murder, murrain, premorse, remorse' - Klein groups precisely Nourai's box.\"},\n        {\"src\": \"IEC\", \"where\": \"s.v. mortos, mrtos (IEC.txt leaf 448)\", \"stance\": \"supports\", \"note\": \"'mortos dead, killed; death ... WP II, 276 Skt. martah mortal, man; OPer. martiya ... Per. mard' - Mann's *mor-to- = Nourai's Mor-to.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Latin\",\n          \"words\": \"mors; môr-târium; mordĕre; morbus\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Of the four Latin words only mors is certain: mors, gen. mortis 'death' is the zero-grade *mr-ti- of *mer- 'to die' (= Skt. mrti-, Av. mereti-, Lith. mirtis, OCS su-mrti; Pokorny 735, Klein s.v. mortal). mortarium 'pounding bowl; the stuff pounded in it' is taken by Watkins as a suffixed zero-grade *mr-to- 'ground down' and de Vaan calls that plausible (from Proto-Italic *morto- < *mrto-), but Ernout-Meillet say flatly 'Aucune etymologie sure'. mordere 'to bite' is put by Pokorny and Klein under an extension *merd- (= Skt. mardati, mrdnati 'grinds, crushes', Gk. smerdnos 'terrible'), whereas Ernout-Meillet warn 'Aucun rapprochement sur ... On ne cite aucune racine indo-europeenne signifiant nettement mordre' and Watkins hedges with 'Possibly extended root *merd-'. morbus 'disease' was analysed as *mor-bho- 'that which consumes' (Pokorny 736, Klein), but Watkins adds 'but more likely of unknown origin' and Ernout-Meillet judge 'La ressemblance avec morior doit etre fortuite ... ce qui rend vain de chercher l'etymologie de morbus' (de Vaan: perhaps to mori 'look like death', or a non-IE word). Nourai's hyphenated spelling môr-târium is his own morpheme division of the Latin lemma mortarium.\",\n          \"derivation_fa\": \"از این چهار واژهٔ لاتینی تنها mors «مرگ» (ستاک mort-) بی‌گمان از صورت ضعیف *mr̥-ti- ریشهٔ *mer- «مردن» است و با mṛti- سنسکریت و mərəti- اوستایی و mirtis لیتوانیایی هم‌ریشه است. mortārium «هاون» را واتکینز و دِوان از *mr̥-to- «ساییده، کوبیده» می‌گیرند، ولی اِرنو–مِیه می‌نویسند «هیچ ریشه‌شناسی مطمئنی ندارد». mordēre «گزیدن» را پوکورنی و کلاین به گونهٔ گسترش‌یافتهٔ *merd- (قس mardati سنسکریت «می‌کوبد») می‌بندند، اما اِرنو–مِیه هیچ پیوند مطمئنی نمی‌بینند. morbus «بیماری» را کلاین *mor-bʰo- «آنچه می‌فرساید» خوانده، ولی واتکینز می‌گوید «به احتمال بیشتر ریشه‌اش ناشناخته است» و اِرنو–مِیه شباهت آن به morior را تصادفی می‌شمارند. پس ادعای نورایی با احتیاط پذیرفتنی است: یکی از چهار واژه قطعی، دو تا احتمالی، و morbus مشکوک است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mortar\",\n            \"https://www.etymonline.com/word/morbid\",\n            \"https://en.wiktionary.org/wiki/mortarium\",\n            \"https://en.wiktionary.org/wiki/morbus\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 753 s.v. mer-2: '3. Probably suffixed zero-grade form *mr-to-, ground down, in Latin mortdrium, mortar: MORTAR. 4. Possibly extended root *merd- in Latin mordere ...: REMORSE. 5. Possibly suffixed form *mor-bho- in Latin morbus, disease (but more likely of unknown origin): MORBID' and 'suffixed form *mr-ti- in Latin mors (stem mort-), death'. Watkins supports all four arrows but with the hedges 'probably/possibly/more likely of unknown origin'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"LAT\", \"where\": \"pp. 736-738 s.vv. morbus, mordeo, mortarium (LAT.txt lines 38994, 39011, 39140)\", \"stance\": \"partial\", \"note\": \"'La ressemblance avec morior doit etre fortuite. Le nom de la maladie differe d'une langue indo-europeenne a l'autre, ce qui rend vain de chercher l'etymologie de morbus'; 'mordeo ... Aucun rapprochement sur'; 'mortarium ... Aucune etymologie sure'. Ernout-Meillet accept only mors.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II pp. 276-279\", \"stance\": \"supports\", \"note\": \"'mrti- Tod in ai. mrtih ... = lat. mors, mortis'; 'morbus Krankheit (Gdf. *mor-bhos ...)'; 'lat. mordeo, -ere, momordi beissen (= ai. mardayati, mamrde)'; 'ahd. morsari Moerser (umgebildet aus lat. mortarium)' under mer-s-.\"},\n            {\"src\": \"POK\", \"where\": \"pp. 735-737\", \"stance\": \"supports\", \"note\": \"'Latin mortarium mortar (due to from *mr-tos pulverized, ground into fine particles) ... morbus a sickness (*mor-bhos)'; under mer-d-: 'Latin mordeo, -ere, momordi to bite, bite into (= Old Indic mardayati)'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.vv. mortal, mortar, morbid (KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'mortar ... L. mortarium derives fr. I.-E. *mrtos, rubbed, pounded'; 'morbid ... fr. morbus, sickness, which prob. stands for *mor-bhos ... lit. that which consumes, fr. I.-E. base *mer-'; 'mortal ... fr. L. mors, gen. mortis, from the stem of morior'.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"English\",\n          \"words\": \"mortal, mortuary, mortgage; mortar; remorse; morbid\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"All six are ordinary Latin > (Old) French > Middle English loans of the words in the parent box. mortal: ME mortal, fr. OF/MF mortel, fr. L. mortalis (: mors, mortis). mortuary: the adj. fr. Late L. mortuarius, the noun fr. ML mortuarium, both to L. mortuus 'dead' (: mors). mortgage: ME morgage, fr. OF mor(t)gage, literally 'dead pledge' - only the first element is Latin mort- ; the second, gage, is Frankish *waddi (Germanic *wadi-, AHD wadh-1 'pledge'), so the word is half-Germanic and Nourai's single arrow from Latin covers only mort-. mortar: partly fr. OE mortere, partly fr. OF mortier, both fr. L. mortarium; the sense 'building mortar' is transferred from the bowl to what was pounded in it (Etymonline, 13c.). remorse: ME remors, fr. MF remors, fr. VL remorsus, pp. of remordere 'to bite again, vex, torment' (re- + mordere) - the metaphor 'the bite of conscience' (Cic. morderi conscientia). morbid: a learned 1650s formation from L. morbidus 'diseased' (: morbus), first 'of the nature of a disease', from 1834 also of mental states.\",\n          \"derivation_fa\": \"هر شش واژهٔ انگلیسی وام‌واژه‌هایی معمولی از لاتینی‌اند که بیشترشان از راه فرانسهٔ باستان به انگلیسی میانه رسیده‌اند: mortal از mortālis، mortuary از mortuārius/mortuārium (به mortuus «مرده»)، mortar از mortārium (نخست «هاون» و سپس «ملاط» به مناسبت آنچه در هاون می‌کوبیدند)، remorse از remorsus صفت مفعولی remordēre «باز گزیدن، آزردن» (استعارهٔ «گزش وجدان»)، و morbid که واژه‌ای عالمانه از سدهٔ ۱۷ از morbidus است. تنها نکته آنکه mortgage «رهن» دو پاره است: پارهٔ نخست mort- لاتینی است ولی پارهٔ دوم gage از *waddi ژرمنی (فرانکی) است، پس پیکان یگانهٔ نورایی از لاتینی فقط نیمهٔ واژه را توضیح می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mortar\",\n            \"https://www.etymonline.com/word/mortgage\",\n            \"https://www.etymonline.com/word/remorse\",\n            \"https://www.etymonline.com/word/morbid\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt lines 753-754 s.v. mer-2 lists MORTAR under *mr-to-, MORDACIOUS/MORDANT/MORSEL/PREMORSE/REMORSE under *merd-, MORBID under *mor-bho-, and MORTI/MORTAL/MORTUARY/AMORTIZE/IMMORTAL/MORTGAGE/MORTIFY/MORTMAIN/POSTMORTEM under *mr-ti- (mors); the index line 1889 'MORTGAGE mer-2, wadh-1' shows the double etymology of mortgage.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"KLN\", \"where\": \"s.vv. mortal, mortuary, mortgage, mortar, remorse, morbid (KLN_1966.txt)\", \"stance\": \"supports\", \"note\": \"'mortgage, n. - ME. morgage, fr. OF. morgage, mortgage, lit. dead pledge (replaced in Modern French by hypotheque). See mortal and gage, pledge'; 'remorse ... fr. VL. remorsus, pp. of remordere, to bite again, vex, torment'; 'mortuary ... fr. L. mortuus, dead, fr. mors'.\"},\n            {\"src\": \"AHD\", \"where\": \"s.v. mer-2 and wadh-1 (lines 753-754, 1115)\", \"stance\": \"supports\", \"note\": \"wadh-1 'A pledge; to pledge ... c. Old French gage, a pledge: GAGE; DEGAGE, ENGAGE, MORTGAGE' - confirms the Germanic second element.\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.vv. mortar, mortgage, remorse, morbid (fetched 2026-09-07)\", \"stance\": \"supports\", \"note\": \"mortar (n.1): 'mid-13c., from Old French mortier ... and directly from Latin mortarium ... with the sense transferred from the bowl to the material prepared in it'; morbid: '1650s ... from Latin morbidus diseased, from morbus'.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Old High German\",\n          \"words\": \"smerzan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"OHG smerzan 'to hurt, ache' (MHG smerzen, NHG schmerzen), with the noun smerzo 'pain', belongs to the s-mobile form *(s)merd- of the root, i.e. to Nourai's 'Smerd' line: Pokorny prints it among the s-forms of mer-d- ('compare the s-forms: gr. smerdnos, smerdaleos terrible, Old High German smerzan ache, smerzo pain', p. 736 f.), and his separate lemma smerd- 'to stink' (p. 970) is expressly said to be a specialisation of the same (s)merd- 'as in NHG schmerzen, Lat. mordere'. Germanic *smert-a-/*smart- shows the regular Grimm outcome of *(s)merd- (d > t, then OHG t > z after r/before nothing... more precisely PGmc t > OHG z by the second sound shift: *smert-an > smerzan). One correction of wording: smerzan is a verb 'to be painful, to ache', so Nourai's gloss 'painful' renders the adjectival sense of the family (OE smeart, OHG smerzo 'pain'), not the verb itself.\",\n          \"derivation_fa\": \"smerzan آلمانی علیای باستان (آلمانی امروز schmerzen) «درد کردن» با نام‌واژهٔ smerzo «درد» به گونهٔ *s(merd)- یعنی همان خط Smerd در نمودار نورایی می‌رسد؛ پوکورنی آن را در ص ۷۳۶–۷۳۷ در میان «صورت‌های با s» ریشهٔ mer-d- آورده و در ص ۹۷۰ نیز smerd- «بوی بد دادن» را کاربردی ویژه از همان (s)merd- «مانند schmerzen آلمانی و mordere لاتینی» می‌خواند. از *smert-an ژرمنی، با تحول دومِ صامت‌های آلمانی (t > z پس از r)، smerzan به دست آمده است. تنها اصلاح آنکه smerzan فعل است («درد کردن») و معنای «دردناک» به صفتِ همین خانواده (smeart انگلیسی باستان، smerzo «درد») تعلق دارد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/smart\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 962: 'smerd-. Pain. Extension of mer-2. Germanic *smarta- in Old English smeart, causing pain, painful: SMART. [Pok. smerd- 970.]' - the German cognate is not named but the root and the 'pain' sense are Watkins's.\"},\n            {\"ref\": \"KLN:1461\", \"status\": \"supports\", \"note\": \"KLN_1966.txt leaf 775 (pp. 1461-63) s.v. smart, v.: '... rel. to MDu. smerten, smarten, Du. smarten, OHG. smerzan, MHG. smerzen, G. schmerzen, to pain, orig. to bite ... fr. I.-E. base *(s)mer-d-, a d-enlargement of base *(s)mer-'. Exactly the OHG form and the root of Nourai's box.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"POK\", \"where\": \"pp. 736-737 (mer-d-, s-forms) and 970\", \"stance\": \"supports\", \"note\": \"'compare the 5-forms: gr. smerdnos, smerdaleos terrible, dreadful (*attritional), Old High German smerzan ache, smerzo pain, Middle Low German smerten ... Old English smeorfan[sic, smeortan] ache, engl. smart biting, sharp, witty'.\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 279\", \"stance\": \"supports\", \"note\": \"'ahd. smerzan schmerzen, smerzo Schmerz, mnd. smerten schmerzen, nd. ndl. smarten bes. von dem durch Scheuerwunden verursachten Schmerz'.\"},\n            {\"src\": \"KLN\", \"where\": \"p. 1461 s.v. smart\", \"stance\": \"supports\", \"note\": \"as in ref_check; Klein glosses OHG smerzan 'to pain', orig. 'to bite'.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"English\",\n          \"words\": \"smart\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The root affiliation is right but the arrow is not: English smart is not taken from Old High German, it is the inherited English sibling of smerzan. The verb is ME smerten < OE smeortan 'be painful (of wounds)'; the noun and the adjective are ME smert(e) < OE smeart 'stinging, causing sharp pain' < Germanic *smarta- (Watkins), the same *(s)merd- as OHG smerzan, MDu. smerten, G schmerzen. Nourai's own cited page says so verbatim: Klein 1461 'smart, intr. v. - ME. smerten, fr. OE. smeortan, rel. to MDu. smerten ... OHG. smerzan ... G. schmerzen'. The later English senses ('pert, witty' c. 1300, 'clever' 1620s, 'fashionable' 1718) develop from 'cutting, stinging', and the adjective has no cognate in the sister languages (Etymonline). So: same root, wrong route - a cognate drawn as a descendant.\",\n          \"derivation_fa\": \"پیوند ریشه‌ای درست است ولی جهت پیکان نه: smart انگلیسی وام‌گرفته یا برآمده از smerzan آلمانی نیست، بلکه هم‌ریشهٔ (cognate) بومی آن است. فعل آن از smerten انگلیسی میانه و آن از smeortan انگلیسی باستان «درد کردن» است، و نام و صفتش از smeart انگلیسی باستان «گزنده، دردآور» از *smarta- ژرمنی می‌آید؛ یعنی هر دو زبان مستقلاً از *(s)merd- هندواروپایی گرفته‌اند. خودِ مرجعی که نورایی آورده (کلاین ص ۱۴۶۱) همین را می‌گوید: «ME smerten، از OE smeortan، خویشاوند با ... OHG smerzan». معناهای امروزی («زبان‌دار» از ۱۳۰۰م.، «باهوش» از ۱۶۲۰م.، «شیک» از ۱۷۱۸م.) از مفهوم «برنده، گزنده» پدید آمده‌اند. پس ادعای نورایی در ریشه درست و در مسیر نادرست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/smart\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"KLN:1461\", \"status\": \"partial\", \"note\": \"KLN_1966.txt leaf 775: 'smart, intr. v. - ME. smerten, fr. OE. smeortan, rel. to MDu. smerten, smarten ... OHG. smerzan, MHG. smerzen, G. schmerzen, to pain, orig. to bite'; 'smart, n. - ME. smert, fr. OE. smeart'. The page has both words of the arrow but makes them cognates ('rel. to'), not parent and child.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"AHD\", \"where\": \"s.v. smerd- (line 962) and index line 2271 'SMART smerd-'\", \"stance\": \"partial\", \"note\": \"'Germanic *smarta- in Old English smeart, causing pain, painful: SMART' - English smart from Old English, not from OHG.\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. smart (v.), smart (adj.), fetched 2026-09-07\", \"stance\": \"partial\", \"note\": \"'Middle English smerten ... from Old English smeortan be painful ... from Proto-Germanic *smarta- (source also of ... Old High German smerzan ...)'; 'The adjective is not represented in the cognate languages.'\"},\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 279\", \"stance\": \"supports\", \"note\": \"'ags. smeortan schmerzen, engl. smart beissend, scharf, witzig (iocus mordens) und nett, zierlich' - the English word listed beside, not under, OHG smerzan.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 1,\n      \"root\": \"Mer 3\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *mers- 'to forget' (Pokorny 6. mer-, mer-s- 'to bother, anger', pp. 737-738; Watkins mers- 'to trouble'; LIV 440 f. *mers-)\",\n      \"note\": \"Root, language label and gloss are right; 'to disturb' is a fair rendering of Pokorny's 'to bother, anger' and of Watkins's 'to trouble', and the two semantic poles of the family are exactly Nourai's two branches: 'forget' (Skt. mrsyate, NP faramus, Lith. mirsti, Arm. moranam, Toch. mars-) and 'hinder, spoil' (Goth. marzjan, OE mierran > mar). One nuance worth recording: Kloekhorst (cited by Wiktionary) takes *mers- to be an s-extension of *mer- 'to die, disappear', which would make Nourai's Mer 2 and Mer 3 one root at bottom; Pokorny (6. mer- separate from 4./5. mer-) and Watkins keep them apart, and so does Nourai.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *mers- «فراموش کردن» است؛ پوکورنی آن را در ص ۷۳۷–۷۳۸ زیر «6. mer-, mer-s-» با معنای «آزردن، خشمگین کردن» آورده و واتکینز mers- «to trouble». معنای «آشفتن/آشفته کردن» که نورایی داده با هر دو سازگار است، و دو شاخهٔ نمودار او درست همان دو قطب معنایی این خانواده است: «فراموش کردن» (mṛṣyate سنسکریت، فراموش فارسی، miršti لیتوانیایی، moranam ارمنی) و «بازداشتن، تباه کردن» (marzjan گوتی، mierran انگلیسی باستان > mar). نکتهٔ افزودنی آنکه کلوکهورست *mers- را گسترش s-دار ریشهٔ *mer- «مردن، ناپدید شدن» می‌داند که در آن صورت Mer 2 و Mer 3 نورایی در نهایت یک ریشه‌اند؛ اما پوکورنی و واتکینز مانند نورایی آنها را جدا نگه می‌دارند. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mers-\",\n        \"https://en.wiktionary.org/wiki/فراموش\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"POK:737\", \"status\": \"supports\", \"note\": \"POK_full.txt line 60313: 'Root / lemma: mer-6, mer-s- / Meaning: to bother, anger, etc. / Material: Old Indic mrsyate forgets, neglects, forgives, marsa- patience ... Gothic marzjan anger, Old English mierran, Old Saxon merrian ... Lithuanian marsas oblivion ... Page(s): 737-738'.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"POK\", \"where\": \"pp. 737-738 (6. mer-, mer-s-)\", \"stance\": \"supports\", \"note\": \"as quoted; 'References: WP. II 279, Trautmann 187'.\"},\n        {\"src\": \"WLD\", \"where\": \"Bd. II p. 279 (WLD_Bd2_pages.txt leaf 283, s.v. mer-s-)\", \"stance\": \"supports\", \"note\": \"'ai. mrsyate vergisst, vernachlaessigt, duldet, verzeiht, marsa- m. geduldiges Ertragen ... got. marsjan[marzjan] aergern, Anstoss geben, ags. mierran, merrian, ahd. merren aergern, stoeren, hindern ... lit. mirszti vergessen ... arm. moranam vergesse'.\"},\n        {\"src\": \"AHD\", \"where\": \"s.v. mers- (AHD_watkins1985.txt line 760)\", \"stance\": \"supports\", \"note\": \"'mers-. To trouble. Suffixed o-grade form *mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.]'\"},\n        {\"src\": \"IEC\", \"where\": \"s.vv. mors- (morsK-) 'forget' and mrsio/mrsKo 'forget' (IEC.txt leaves 448, 452)\", \"stance\": \"supports\", \"note\": \"'mors- (morsK-) forget: Tokh. AB mars-, B mars-; Arm. mornam; Li. cf. marsus forgetful'; 'mrsio (1), mrsKo forget. WP II, 281 Skt. mrsyami; Per. cf. fara-mus forgetful; fara-musam, inf: -musidan, v. forget; Tokh. AB mars-; Arm. mornam, moranam'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"â-marš; pra-marš\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The Sanskrit root is real and the glosses are right, but the two compound citation forms are analytic reconstructions, not textbook Sanskrit lemmas. Attested (RV onwards) are mrsyate 'forgets, neglects, bears patiently, forgives', the causative marsayati 'endures, forgives' and the noun marsa- m. 'patient endurance' (Walde-Pokorny II 279; Pokorny 737; EWAia II 332 via Cheung s.v. *mars). Nourai's 'â-marš: to tolerate, be quiet' and 'pra-marš: to forget' are taken over from Horn: Grundriss no. 464 explains NP xamos as 'skr. a + sqrt(mars) geduldig ertragen' and no. 812 explains faramos as 'ai. pra + sqrt(mrs-), mrsyate vergessen'. Huebschmann, writing on the same entry (Pers. Stud. 84), gives the corresponding forms with an asterisk (np. faramust = skr. *pramrsta-, *pramrsti-), i.e. the compound is reconstructed. Methodologically the Persian words are not descendants of Sanskrit anyway but of the parallel Old Iranian *(fra-a-)mrs-; the Sanskrit box stands here as the Indo-Iranian witness.\",\n          \"derivation_fa\": \"خودِ ریشهٔ سنسکریت و معناها درست است، اما دو صورت مرکبی که نورایی آورده صورت‌های بازسازی‌شده‌اند نه سرواژه‌های سنسکریت. آنچه از ریگ‌وید به بعد گواهی شده اینهاست: mṛṣyate «فراموش می‌کند، فرو می‌گذارد، شکیبایی می‌کند»، سببیِ marṣayati «تحمل می‌کند، می‌بخشد» و نام‌واژهٔ marṣa- «شکیبایی» (والده–پوکورنی ۲: ۲۷۹؛ چونگ ذیل *marš). صورت‌های «â-marš» و «pra-marš» از هرن گرفته شده است: هرن در شمارهٔ ۴۶۴ خاموش را «skr. ā + √marš» و در شمارهٔ ۸۱۲ فراموش را «ai. pra + √mṛṣ-» می‌خواند، و هوبشمان در ص ۸۴ همان صورت‌ها را با ستاره (*pramṛṣṭa-) می‌نویسد؛ یعنی بازسازی‌اند. از نظر روش هم واژه‌های فارسی فرزندِ سنسکریت نیستند بلکه از *(fra-ā-)mṛš- ایرانی باستان می‌آیند و جعبهٔ سنسکریت اینجا نمایندهٔ هندوایرانی است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mers-\",\n            \"https://en.wiktionary.org/wiki/فراموش\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"HRN:101\", \"status\": \"not_found\", \"note\": \"Horn p. 101 (HRN.txt leaf 123) is the c- section (no. 452 cehar 'four' to no. 457 ci); nothing about mars/xamos. The entry Nourai means is no. 464 on p. 103 (leaf 125): 'xamos schweigend, still, xamosi. skr. a + sqrt(mars) geduldig ertragen; vergl. framos (No. 812)'. The page number is two off.\"},\n            {\"ref\": \"HRN:181\", \"status\": \"supports\", \"note\": \"HRN.txt leaf 203 (p. 181), no. 812: 'feramos Vergessend; Vergessenheit, feramus, feramust, fer(a)mosiden ... ai. pra + sqrt(mrs-), mrsyate vergessen; phlv. framos bezw. farmos, framost'. Exactly Nourai's pra-mars 'to forget'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 279 s.v. mer-s-\", \"stance\": \"supports\", \"note\": \"'ai. mrsyate vergisst, vernachlaessigt, duldet, verzeiht, marsa- m. geduldiges Ertragen, mrsa umsonst, vergebens, marsayati duldet, verzeiht' - both of Nourai's senses ('to tolerate, be quiet' / 'to forget') are in the one Sanskrit root.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *mars 'to forget' (CHEUNG.txt line 17746)\", \"stance\": \"supports\", \"note\": \"'*SANSKRIT: mars to forget (RV+) = EWAia II: 332 ... PIE *mers- to forget = LIV: 440 f. | Pok.: 737 f.' - no compounded Sanskrit citation form given.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 84, ad Horn no. 812 (HUB.txt leaf 95)\", \"stance\": \"partial\", \"note\": \"'Zu der vorgeschlagenen Etym. passt das o von phl. paz. framos, farmos ..., np. faramos nicht. Doch waere np. faramust = skr. *pramrsta-, *pramrsti-' - the Sanskrit compound is starred, and Huebschmann objects to the vocalism.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. mrsio (1), mrsKo 'forget' (IEC.txt leaf 452)\", \"stance\": \"supports\", \"note\": \"'WP II, 281 Skt. mrsyami, id.; Per. cf. fara-mus, adj. forgetful; fara-musam, inf: -musidan, v. forget' - Mann puts the Sanskrit and the Persian side by side under one root.\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"xâmŭš «خاموش»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP xamos/xamus 'silent; extinguished, turned off' does belong to this root in the standard Persian handbooks, but the derivation is Horn's and remains unproven in its detail. Horn no. 464 (p. 103) gives 'xamos schweigend, still ... skr. a + sqrt(mars) geduldig ertragen; vergl. framos (No. 812)', and Mo'in's footnote in Borhan-e Qate' (vol. 2, p. 706/707) repeats it in one line: 'xamos - Sanskrit a-marsa (tolerating, being patient)'. Wiktionary derives it from Middle Persian h'mwsh /xamos/ 'silent' and adds only 'perhaps from Proto-Indo-European *mers-', comparing Latvian aizmirst. The weak points are (a) the initial x-, which an Old Iranian preverb *a- cannot give (the MP spelling h'mwsh points to an initial ha-/xa- whose source is unexplained), and (b) the -os-/-us- vocalism, the same difficulty Huebschmann and Henning raise for framos; Cheung's Etymological Dictionary of the Iranian Verb does not list xamos under *mars at all. The meaning 'turned off (of a lamp, a fire)' is a secondary Persian development from 'silent, quiet'. So: right root, route accepted by the Persian tradition but not established.\",\n          \"derivation_fa\": \"«خاموش» (xāmōš) در سنّت ریشه‌شناسی فارسی به همین ریشه بسته شده، اما بستگیِ جزء‌به‌جزء آن از هرن است و اثبات‌شده نیست. هرن در شمارهٔ ۴۶۴ (ص ۱۰۳) می‌نویسد «xāmōš خاموش، ساکت … skr. ā + √marš (شکیبایی کردن)»، و معین در حاشیهٔ برهان قاطع (ج ۲، ص ۷۰۶/۷۰۷) همان را در یک سطر می‌آورد: «خاموش – سانسکریت ā-marṣa (تحمل، صبر کردن)». ویکی‌واژه آن را از فارسی میانهٔ ⟨hʾmwš⟩ xāmōš «ساکت» می‌گیرد و تنها «شاید از *mers- هندواروپایی» می‌افزاید. دو اشکال باقی است: نخست «خ» آغازی که از پیشوند *ā- ایرانی باستان به دست نمی‌آید، و دوم واکهٔ -ōš که همان دشواریِ framōš است و هوبشمان و هنینگ بر آن انگشت گذاشته‌اند؛ چونگ نیز خاموش را زیر *marš نیاورده است. معنای «خاموش (چراغ)» تحول معنایی متأخر فارسی از «ساکت» است. پس ادعای نورایی با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/خاموش\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/mers-\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:706\", \"status\": \"supports\", \"note\": \"BQT_v2_pages.txt leaf 165 (the previous-but-two leaf carries the printed number 705, so this is p. 706/707), footnote to the headword خاموش: 'خاموش - سانسکریت a-marṣa (تحمل، صبر کردن)', with 'خامش - بضم سوم، مخفف خاموش' just above. Mo'in's footnote is exactly Nourai's arrow.\"},\n            {\"ref\": \"BQT:1448\", \"status\": \"partial\", \"note\": \"BQT vol. 3 p. 1448 (BQT_v3_pages.txt, pdf page 241) is the headword فراموش, not خاموش; its footnote reads 'پهلوی framōš ... باستان *fra-mūš- (فراموش کردن). بلوچی shamushag ... > اشتقاق هوبشمان ... فرامشت framusht = ... pramrshta-, pramrshti- ... هرن و هوبشمان گوید: فرامش پهلوی باید از framush یا framursh ناشی شده باشد'. It supports the Mer-3 > framos chain (node #5) rather than the xamos node it is attached to.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 464, p. 103 (HRN.txt leaf 125)\", \"stance\": \"supports\", \"note\": \"'464. xamos schweigend, still, xamosi. skr. a + sqrt(mars) geduldig ertragen; vergl. framos (No. 812).' Horn is the source of Nourai's arrow and of Mo'in's footnote.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *mars 'to forget' (line 17746 ff.)\", \"stance\": \"silent\", \"note\": \"The entry lists MMP fr'mws-, NP firamustan, Bal. samust-, Khot. hamura-, Sogd. fr''wyscy, but no xamos/xamus; grep of CHEUNG.txt for 'xamos', 'hamos', 'xamus' finds nothing.\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt (Aryanpur, headword index)\", \"stance\": \"silent\", \"note\": \"grep for خاموش in ARY_pages.txt returns no headword entry (only unrelated pages); Aryanpur has no article on this word.\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan / Old Persian\",\n          \"words\": \"muš, fra-â-muš\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"The derivation is right in substance but the label and the shape of the forms are not what the sources know. The Old Iranian root is mars-/*mrs- 'to forget': Bartholomae's Altiranisches Woerterbuch (cols. 1153-54) has Avestan marsa- adj. 'schwer zu vergessen' and marso.kara-/marsavan- 'das Vergessen bewirkend' (a daeva name), citing np. faramos; Cheung reconstructs Iranian *mars 'to forget' (PIE *mers-, LIV 440 f.). Abolghasemi (FFD p. 65), the reference Nourai cites, writes the ancestor as Old Iranian *fra-a-mrs-ta and *fra-a-mrs-a, not *fra-a-mus-; the -u/o- vocalism of muš is a Middle Persian trait (framos) projected back. And no Old Persian form of this root is attested: Kent's lexicon has only *mer- 'die' (martiya, marta, uva-marsiyus 'by self-death'), nothing for 'forget'. So the node should read Avestan/Old Iranian *mrs-, *fra-a-mrs-, and the 'Old Persian' half of the label is unsupported.\",\n          \"derivation_fa\": \"جانِ این پیوند درست است اما برچسب زبان و شکل صورت‌ها با آنچه منابع می‌شناسند نمی‌خواند. ریشهٔ ایرانی باستان marš-/*mṛš- «فراموش کردن» است: بارتولومه در فرهنگ ایرانی باستان (ستون ۱۱۵۳–۱۱۵۴) اوستایی marša- «دیرفراموش‌شدنی» و maršavan- «فراموش‌آورنده» (نام دیوی) را دارد و همان‌جا np. farāmōš را یاد می‌کند؛ چونگ نیز *marš ایرانی را از *mers- هندواروپایی می‌گیرد. ابوالقاسمی در همان صفحهٔ ۶۵ که نورایی ارجاع داده، نیای این فعل را «ایرانی باستان *fra-ā-mṛš-ta / *fra-ā-mṛš-a» می‌نویسد، نه *fra-ā-muš-؛ واکهٔ u/ō در «muš» ویژگی فارسی میانه (framōš) است که به دورهٔ باستان پس‌افکنده شده. از پارسی باستان هم هیچ صورتی از این ریشه گواهی نشده است؛ کنت فقط *mer- «مردن» را دارد (martiya، marta، uvā-maršiyuš). پس ادعای نورایی با اصلاحِ صورت به *mṛš- و حذف «پارسی باستان» پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/فراموش\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FFD:65\", \"status\": \"partial\", \"note\": \"FFD_pages.txt pdf page 70 = printed p. 65 (the page header reads 65): 'فرامشت بازماندهٔ *fra-ā-mṛš-ta ایرانی باستان است ... fra و ā هر دو پیشوند فعلی هستند. ریشهٔ mṛš ظاهراً به معنی فراموش کردن است' and 'فراموش، فرموش < فارسی میانه framōš < ایرانی باستان *fra-ā-mṛš-a'. The page supports the derivation but writes the root *mṛš (Old Iranian), not muš, and does not call it Avestan or Old Persian.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"BRT\", \"where\": \"cols. 1153-54 (BRT.txt leaf 641), s.vv. marsa-, marsavan-\", \"stance\": \"supports\", \"note\": \"'marsa- Adj. schwer zu vergessen, np. faramos vergessend'; 'marsavan- m. Name eines Daeva ... eig. das Vergessen bewirkend'. Bartholomae thus does attest the root in Avestan - but as mars-, not mus-.\"},\n            {\"src\": \"KNT\", \"where\": \"Lexicon/roots, KNT.txt line 1526\", \"stance\": \"silent\", \"note\": \"'*mer- die in marika- ... *mor- in martiya man ... *mr- in marta dead, uva-marsiyus by self-death; perhaps *mer- in amariyata he died'. Kent lists no Old Persian root 'forget'; grep for 'forget' in KNT.txt returns nothing.\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *mars 'to forget'\", \"stance\": \"supports\", \"note\": \"'*mars to forget ... PIE *mers- to forget = LIV: 440 f. | Pok.: 737 f.'; the Avestan line is absent from Cheung's entry (he starts with Middle Persian), but Khotanese marsyara and MP fr'mws- are given.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II Glossary, s.v. maskar (NYB_vol2_glossary.txt line 2493)\", \"stance\": \"partial\", \"note\": \"'In all probability the same as Av. (1153) marso.kara- ... OIr marsa- must then mean weak, slack (etymology obscure; to be combined with Skr mrs-, v.s.v. framos?)' - Nyberg confirms the Avestan forms at AiW 1153 but is unsure of the semantics.\"}\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"frâmŭštan\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"MacKenzie's Concise Pahlavi Dictionary has the verb exactly as drawn: 'framustan, framos- [pl(')mwstn' | M pr'mwst, pr'mws-, N fara~] forget', beside the participle 'framos [pl(')mws | M pr'mws, N faramos] forgotten' and the secondary 'framosidan = framustan'. Morphologically the past stem framost/framust continues Old Iranian *fra-a-mrs-ta (fra- 'forth' + a- + zero-grade of *mars-), with the regular Middle Persian loss of the intervocalic prefix vowel and -rs-t- > -st- (FFD p. 65); the present stem framos- shows the -o- that Huebschmann (Pers. Stud. 84) and Henning (1933: 185, quoted by Cheung) found irregular for *mars- and which is usually explained as a rounding/analogical vocalism of the Middle Iranian period. Manichaean MP pr'mws- and Parthian fr'mws- have the same shape, so the form is well attested in both Middle Iranian corpora.\",\n          \"derivation_fa\": \"فرهنگ کوچک پهلوی مکنزی همین فعل را دارد: «framuštan, framōš- [pl(ʾ)mwštn] فراموش کردن»، در کنار صفت مفعولی «framōš [pl(ʾ)mwš] فراموش‌شده» و صورت ثانوی «framōšīdan = framuštan». از نظر ساخت، ستاک گذشتهٔ framōšt/framušt بازماندهٔ *fra-ā-mṛš-ta ایرانی باستان است (پیشوند fra- «پیش» + ā- + صورت ضعیف ریشهٔ marš-) با تحول قاعده‌مندِ -ršt- > -št- در فارسی میانه (ابوالقاسمی ص ۶۵). واکهٔ ō در ستاک حال framōš- همان است که هوبشمان (ص ۸۴) و هنینگ (۱۹۳۳: ۱۸۵) بی‌قاعده شمرده‌اند و آن را به همگونی/گردشدگی دورهٔ میانه نسبت می‌دهند. صورت‌های فارسی میانهٔ مانوی prʾmwš- و پارتی frʾmwš- نیز همین شکل را دارند، پس این ماده در هر دو پیکرهٔ ایرانی میانه خوب گواهی شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/فراموش\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FFD:65\", \"status\": \"supports\", \"note\": \"FFD printed p. 65: 'در فارسی دری فرامشت بازماندهٔ framōšt فارسی میانه است. framōšt بازماندهٔ *fra-ā-mṛš-ta ایرانی باستان است' - the Pahlavi past stem and its Old Iranian source are given exactly as Nourai draws them.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"p. 76 area, s.vv. framos, framosidan, framustan (PHD.txt line 325; PHD_mackenzie.txt line 2309)\", \"stance\": \"supports\", \"note\": \"'framos [bl(?)mus | M pr'mws, N faramos] forgotten. framosidan [plmwsytn'] = framustan. framustan, framos- [pl(?)mws-tn' | M prhmwst, pr'mws-, N fara~] forget.'\"},\n            {\"src\": \"CHEUNG\", \"where\": \"s.v. *mars, Middle Persian and Parthian sections\", \"stance\": \"supports\", \"note\": \"'(+ *fra-a-) MMP fr'mws-, BMP pl'mws- /framos-/ to forget ... Pres.: IND. 3sg. BMP pl'mwsyt /framosed/ ... Partic. perf. pass. MMP fr'mwst'; and 'Henning 1933: 185 is sceptical about the connection of the Persian forms with *mars (on account of the Pahlavi and Manichaean forms), for which he quotes Huebschmann 1895: 84'.\"},\n            {\"src\": \"HUB\", \"where\": \"p. 84 (ad Horn 812)\", \"stance\": \"partial\", \"note\": \"'Zu der vorgeschlagenen Etym. passt das o von phl. paz. framos, farmos (Min. Gl. 75, Shk. 244), np. faramos nicht' - accepts the form, questions the vowel.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II Glossary (grep 'framos')\", \"stance\": \"partial\", \"note\": \"Nyberg's glossary refers to a framos entry ('to be combined with Skr mrs-, v.s.v. framos?', line 2493) but the lemma itself is not in the OCR of the leaves scanned; NYB p. 140 has only murvik.\"}\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Persian\",\n          \"words\": \"faramŭšîdan «فراموشیدن» (+ فراموشانیدن، فرموشیدن، فراموش، فرامش، فرامشت، فرامِشی)\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"New Persian faramus 'forgotten; forgetfulness' continues Middle Persian framos directly; faramusidan/farmosidan is a Dari-period denominal-secondary infinitive built on the present stem (Abolghasemi p. 65: 'فراموشید ... مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است'), while the older past stem survives in the Classical form faramust/faramesht - which is exactly the word in Nourai's Naser-Khosrow line (nazdik-e xodavand badi nist faramusht). Horn no. 812 (p. 181) lists the whole set 'feramos ..., feramus, feramust, fer(a)mosiden' and cites Vis o Ramin 50.13 for the -iden form; Mo'in's Borhan footnote (vol. 3 p. 1448) and Mann (IEC s.v. mrsio: 'Per. fara-mus, adj. forgetful; fara-musam, inf. -musidan') give the same chain. The variants Nourai prints in Persian script (فرموشیدن، فرامش، فرامشت، فرامشی) are the standard by-forms of the classical language, and Mo'in's Farhang-e Farsi records them under فراموش ('[= فراموش - فرامشت - فرموش]').\",\n          \"derivation_fa\": \"«فراموش» فارسی نو بازماندهٔ مستقیم framōš فارسی میانه است، و «فراموشیدن/فرموشیدن» مصدری ثانوی از دورهٔ دری است که بر پایهٔ ستاک مضارع ساخته شده؛ ابوالقاسمی (ص ۶۵) می‌نویسد «فراموشید … مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است». ستاک گذشتهٔ کهن‌تر در صورت کلاسیک «فرامشت/فراموشت» مانده است، همان که در بیت ناصرخسروِ نقل‌شده در نمودار آمده: «نزدیک خداوند بدی نیست فرامُشت». هرن در شمارهٔ ۸۱۲ (ص ۱۸۱) همهٔ این صورت‌ها را می‌آورد و برای «فرامشیدن» به ویس و رامین ۵۰/۱۳ استناد می‌کند؛ معین در حاشیهٔ برهان قاطع (ج ۳ ص ۱۴۴۸) و مان (ذیل *mṛsio) نیز همین زنجیره را دارند. گونه‌های فارسی‌نویسیِ نمودار (فرموشیدن، فرامش، فرامشت، فرامِشی) همان گونه‌های متعارف زبان کلاسیک‌اند و معین در فرهنگ فارسی ذیل «فراموش» آنها را ثبت کرده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/فراموش\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"FFD:65\", \"status\": \"supports\", \"note\": \"FFD printed p. 65, headword 'فراموشیدن، فرموشیدن': 'فراموشید، فرموشید < فارسی میانه framōšīd؛ مادهٔ ماضی جعلی است، از مادهٔ مضارع ساخته شده است ... فراموش، فرموش < فارسی میانه framōš < ایرانی باستان *fra-ā-mṛš-a'.\"},\n            {\"ref\": \"MON:2506\", \"status\": \"partial\", \"note\": \"The 6-volume Farhang-e Farsi is not online with page numbers; the 2-volume abridgement on disk (MON_part2.txt line 5784) has 'فراموش: [= فراموش - فرامشت - فرموش] (ص.) از یاد رفته، از خاطر محو شده' - it confirms the headword and the by-forms Nourai prints, but the page reference itself could not be checked.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 812, p. 181 (HRN.txt leaf 203)\", \"stance\": \"supports\", \"note\": \"'812. feramos Vergessend; Vergessenheit, feramus, feramust, fer(a)mosiden (Vis und Ramin, S. 50 V. 13). ai. pra + sqrt(mrs-), mrsyate vergessen; phlv. framos bezw. farmos, framost.'\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 3 p. 1448 (BQT_v3_pages.txt pdf page 241), s.v. فراموش\", \"stance\": \"supports\", \"note\": \"Mo'in's footnote: 'پهلوی framōš ... پازند farmōsh ... بلوچی shamushag ... فرامشت framusht = pramrshta-, pramrshti- ... هوبشمان' - and the neighbouring headwords فرامش and فرامشت ('بمعنی فراموش است که از یاد رفتن باشد') are the very variants of Nourai's box.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. mrsio (1), mrsKo 'forget' (IEC.txt leaf 452)\", \"stance\": \"supports\", \"note\": \"'Per. cf. fara-mus, adj. forgetful; fara-musam, inf: -musidan, v. forget' - Mann's only Iranian witness is precisely this Persian verb.\"},\n            {\"src\": \"MON\", \"where\": \"Farhang-e Farsi (2-vol. abridgement), s.v. فراموش\", \"stance\": \"supports\", \"note\": \"'فراموش: [= فراموش - فرامشت - فرموش]' plus فراموشکار، فراموشی; the abridgement drops Mo'in's Latin-script Pahlavi forms.\"}\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"Germanic\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"An empty pass-through box standing for Proto-Germanic *marzjan 'to hinder, offend' (< suffixed o-grade *mors-eyo-), the ancestor of Gothic marzjan 'to offend, cause to stumble', Old Saxon merrian, Old Frisian meria, OHG marren/merren 'to hinder, disturb' and the Old English verb behind mar. Watkins reconstructs exactly this: 'mers-. To trouble. Suffixed o-grade form *mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR', and Walde-Pokorny II 279 lists the same Germanic set under mer-s-. The Germanic *z of *marzjan is the regular voicing (Rhotacism after Verner) of the root-final *-s- of *mers- before the *-yo- suffix.\",\n          \"derivation_fa\": \"این جعبهٔ تهی نمایندهٔ *marzjan ژرمنی آغازین «بازداشتن، آزردن» (از *mors-eyo- با درجهٔ o) است؛ نیای marzjan گوتی «آزردن، لغزاندن»، merrian ساکسونی باستان، merren/marren آلمانی علیای باستان و فعل انگلیسی باستانی است که mar از آن آمده. واتکینز درست همین را بازسازی می‌کند: «mers- to trouble؛ صورت o-دار پسوندی *mors-eyo- در *marzjan ژرمنی، در merran/mierran انگلیسی باستان»؛ والده–پوکورنی (۲: ۲۷۹) نیز همین مجموعهٔ ژرمنی را ذیل mer-s- آورده است. z در *marzjan همان s پایانی ریشه است که پیش از پسوند *-yo- بر اثر قانون ورنر واکدار شده است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"AHD\", \"status\": \"supports\", \"note\": \"AHD_watkins1985.txt line 760: 'mers-. To trouble. Suffixed o-grade form *mors-eyo- in Germanic *marzjan in Old English merran, mierran, to impede: MAR. [Pok. 6. mer- 737.]'\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WLD\", \"where\": \"Bd. II p. 279 s.v. mer-s-\", \"stance\": \"supports\", \"note\": \"'got. marsjan[marzjan] aergern, Anstoss geben, ags. mierran, merrian, as. merrian, ahd. merren aergern, stoeren, hindern, ags. amierran verderben, zerstoeren, hindern, mhd. marren zoegern'.\"},\n            {\"src\": \"POK\", \"where\": \"pp. 737-738 (6. mer-, mer-s-)\", \"stance\": \"supports\", \"note\": \"'Gothic marzjan anger, Old English mierran, Old Saxon merrian, Old Frisian meria, Old High German marren, merren hinder, disturb, bother; Old English a-mierran spoil'.\"},\n            {\"src\": \"IEC\", \"where\": \"s.v. mars- (marso, io; marsos) (IEC.txt leaf 448)\", \"stance\": \"partial\", \"note\": \"'mars- bad; be bad, err; wickedness, error. Cf. mors- Hitt. mars- be bad ... Go. marzjan, v. scandalize; OE mearr evil, deceptive' - Mann files the Germanic verb under a root 'be bad, err' rather than under 'forget/trouble'.\"}\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"English\",\n          \"words\": \"mar\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English mar 'to damage, spoil' is ME merren/marren (early 13c.) from Old English merran (Anglian) / mierran (West Saxon) 'to waste, spoil, hinder', i.e. from the Germanic *marzjan of the parent box; the a-vocalism of the modern form is the Anglian/dialectal development also seen in marsh (Etymonline). Webster's Second gives '[ME. marren, merren, from AS. merran in amerran, amyrran, to dissipate, hinder, obstruct]', and Watkins files MAR under mers-. The chart's arrow (Germanic > English) is therefore right, and the gloss 'to damage' matches the earliest English sense. Klein connects mar to the 'crush' root instead (mar ... rel. to Goth. marzjan ... and prob. to ON. merja 'to crush', cogn. with OI. mrnati), which would attach it to Nourai's Mer 2; the majority view (Pokorny, Walde-Pokorny, Watkins, Etymonline) keeps it here under *mers-.\",\n          \"derivation_fa\": \"فعل mar انگلیسی «آسیب زدن، تباه کردن» از merren/marren انگلیسی میانه (اوایل سدهٔ ۱۳م.) و آن از merran (انگلیایی)/mierran (وست‌ساکسونی) انگلیسی باستان «تباه کردن، بازداشتن» است، یعنی از همان *marzjan ژرمنیِ جعبهٔ مادر؛ واکهٔ a در صورت امروزی همان تحول گویشیِ انگلیایی است که در marsh هم دیده می‌شود. وبستر (چاپ دوم) می‌آورد: «ME marren, merren، از AS merran در amerran, amyrran». واتکینز نیز MAR را ذیل mers- آورده است. پس پیکان نمودار (ژرمنی > انگلیسی) درست است و معنای «to damage» با کهن‌ترین معنای انگلیسی می‌خواند. تنها کلاین این واژه را به ریشهٔ «کوبیدن، ساییدن» (قس merja نورسی باستان، mṛṇāti سنسکریت) می‌بندد که در آن صورت به Mer 2 نورایی تعلق می‌گرفت؛ اما دیدگاه غالب همین جای کنونی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/mar\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"The node carries no reference in the book (refs=None); the parent Germanic box cites AHD, whose mers- entry ends '...to impede: MAR'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"WEB\", \"where\": \"Webster's New Twentieth Century, 2nd ed., s.v. mar (WEB_vol1.txt line 112709)\", \"stance\": \"supports\", \"note\": \"'mar, v.t.; marred ... [ME. marren, merren, from AS. merran in amerran, amyrran, to dissipate, hinder, obstruct.] to ... damage so as to make imperfect; to spoil; to impair; to hurt, deform, injure.'\"},\n            {\"src\": \"Etymonline\", \"where\": \"s.v. mar (v.), fetched 2026-09-07\", \"stance\": \"supports\", \"note\": \"'Middle English merren to deface, disfigure (early 13c.), from Old English merran (Anglian), mierran (West Saxon) to waste, spoil, from Proto-Germanic *marzjan ... from PIE root *mers- to trouble, confuse (source also of Sanskrit mrsyate forgets, neglects)'.\"},\n            {\"src\": \"KLN\", \"where\": \"s.v. mar, tr. v. (KLN_1966.txt)\", \"stance\": \"partial\", \"note\": \"'mar, tr. v., to injure. - ME. merren, marren, fr. OE. merran, mierran, to hinder, obstruct, squander, waste, rel. to OFris. meria, OHG. marren, merren ... Goth. marzjan ... and prob. to ON. merja, to crush, bruise, and cogn. with OI. mrnati, he crushes' - same immediate history, different root affiliation.\"},\n            {\"src\": \"AHD\", \"where\": \"index line 1816 'MAR mers-' and s.v. mers-\", \"stance\": \"supports\", \"note\": \"MAR is filed under mers- 'to trouble'.\"}\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 4,\n      \"root\": \"Mereğa / Saĕna-mereğa\",\n      \"verdict\": \"plausible\",\n      \"modern_form\": \"Avestan mərəγa- m./n. 'bird (especially of the larger kinds)' (< Proto-Iranian *mr̥gáh, PII *mr̥gás, cf. Skt. mr̥ga- 'wild animal'); the phrase mərəγō saēnō 'the bird Saēna' (Yasht 14.41), saēna- being the name of a large bird of prey, probably the eagle (cf. Skt. śyena- 'eagle, falcon')\",\n      \"note\": \"Language label and the first gloss are right: Bartholomae (AiW col. 1172) heads the entry 'mərəγa- m., n. Vogel, spez. von groesseren' - 'especially of the larger ones', and Buck (Selected Synonyms 3.64, pp. 183-84) writes 'Av. maraya- used of large birds (Barth. 1172), NPers. murgh bird : Skt. mrga- wild animal', which is verbatim Nourai's 'a large bird'. Saēna-mereğa is likewise a real Avestan phrase, but as two words: hau maza mərəγō saēnō 'that great bird Saēna' (Yt. 14.41). The gloss 'dark hawk bird' is where the box goes wrong: saēna- is 'a large bird of prey, probably the eagle' (Bartholomae: 'Name eines grossen Raubvogels, wohl des Adlers'), and Mo'in's Borhan footnote reports that 'scholars translate the word sēn in the Avesta as falcon and eagle'; nothing in the sources supports 'dark'. Also note that this Avestan-headed root box is really an Indo-Iranian noun *mr̥ga-, not a verbal root, and Nourai's own cited KLN:959 does not contain it (see ref_check).\",\n      \"note_fa\": \"برچسب زبان و معنای نخست درست است: بارتولومه در ستون ۱۱۷۲ فرهنگ ایرانی باستان مدخل را چنین می‌آورد «mərəγa- نرینه/بی‌جان: پرنده، به‌ویژه پرندگان بزرگ‌تر»، و باک در فرهنگ مترادف‌های هندواروپایی (بخش ۳٫۶۴، ص ۱۸۳–۱۸۴) می‌نویسد «اوستایی mərəγa- برای پرندگان بزرگ به کار می‌رود (بارتولومه ۱۱۷۲)، فارسی نو murγ» که همان «a large bird» نورایی است. ترکیب «سئنه‌مرغ» نیز در اوستا گواهی شده، اما به صورت دو واژه: hau maza mərəγō saēnō «آن مرغ بزرگِ سئنه» (بهرام‌یشت ۴۱). خطا در واژهٔ «dark» است: saēna- نام «پرندهٔ شکاری بزرگ، احتمالاً عقاب» است (بارتولومه) و معین در حاشیهٔ برهان می‌نویسد «محققان کلمهٔ سئنه را در اوستا به شاهین و عقاب ترجمه کرده‌اند»؛ هیچ منبعی معنای «تیره/سیاه» را تأیید نمی‌کند. نکتهٔ دیگر آنکه این «ریشه» در واقع نام‌واژهٔ هندوایرانی *mr̥ga- است نه ریشهٔ فعلی، و ارجاع KLN:959 خودِ نورایی این واژه را ندارد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/مرغ\",\n        \"https://en.wiktionary.org/wiki/سیمرغ\",\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/mr̥gáh\"\n      ],\n      \"ref_check\": [\n        {\"ref\": \"BQT:190\", \"status\": \"not_found\", \"note\": \"Vol. 1 of the Borhan OCR (BQT_v1_pages.txt) has its dictionary text from leaf ~210; the only securely numbered leaf nearby is leaf 388 = printed 199, which puts p. 190 at leaf ~379, the آله/الیاس region (the entry آله 'عقاب، پرنده‌ای معروف' with a footnote 'پهلوی ālūh ... در اوستا ərəzifya'). That is an eagle word but not mərəγa-/saēna-; the سیمرغ material in Borhan is in vol. 2 (leaves 669, 676-78 = pp. ~1211, 1218-20). Either the page number is wrong or it refers to a page of the Amir Kabir printing that the available scan numbers differently.\"},\n        {\"ref\": \"KLN:959\", \"status\": \"not_found\", \"note\": \"Klein p. 958-959 (KLN_1966.txt leaf 514, page marker '958' on the leaf) is the mega-/megalo- run ('megacephalic ... megaron'); no bird word. Klein's actual entry is on p. 1449/1450 (leaf 769): 'simurg, n., a gigantic bird in Persian mythology, prob. identical with the roc. - Pers. simurgh, rel. to Avestic saēnō mereγō, eagle, OI. śyenaḥ, eagle. Arm. c̣in, kite.' - which is precisely what the root box claims, but at a different page.\"}\n      ],\n      \"consulted\": [\n        {\"src\": \"BRT\", \"where\": \"cols. 1172 and ~1345 (BRT.txt lines 20365-20369, 25786)\", \"stance\": \"supports\", \"note\": \"'j. mərəγa- m., n. Vogel, spez. von groesseren ... hau maza mərəγō saēnō Yt. 14.41 ... ai. mṛga- m. Waldtier (Gazelle), auch Vogel; np. murγ Vogel; Huhn. - Pue.: murw'; and 'j. saēna- m. Name eines grossen Raubvogels, wohl des Adlers'. Footnote: 'Wie Adler, Geier, Huhn; im Gegensatz zu vaya-'.\"},\n        {\"src\": \"SYN\", \"where\": \"3.64 BIRD, pp. 183-184 (SYN.txt leaf idx 219 = printed 184)\", \"stance\": \"supports\", \"note\": \"'Av. maraya- used of large birds (Barth. 1172), NPers. murgh bird : Skt. mrga- wild animal (3.11).' The source of Nourai's gloss 'a large bird'.\"},\n        {\"src\": \"KLN\", \"where\": \"p. 1449/1450 s.v. simurg (leaf 769)\", \"stance\": \"supports\", \"note\": \"'Pers. simurgh, rel. to Avestic saēnō mereγō, eagle, OI. śyenaḥ, eagle' - supports the root box but glosses saēna- 'eagle', not 'dark'.\"},\n        {\"src\": \"BQT\", \"where\": \"vol. 2 pp. ~1218-1220 (BQT_v2_pages.txt leaves 676-677), Mo'in's footnote on سیمرغ/سین\", \"stance\": \"partial\", \"note\": \"'محققان کلمهٔ سنه [سئنه] را در اوستا به شاهین و عقاب ترجمه کرده‌اند ... بی‌شک بین دو مفهوم سئنهٔ اوستایی و سیمرغ فارسی ... رابطه‌ای موجود است'; it also quotes Menog i Xrad on 'آشیان سین‌مورو (سیمرغ) بر درخت هروسپ‌تخمک'. Supports the identification, not the gloss 'dark'.\"}\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Pahlavi\",\n          \"words\": \"murğ, merv; sĕn-murv\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Middle Persian murw [mwrw] 'bird' is the regular continuation of Av. mərəγa- / Proto-Iranian *mr̥gáh: the syllabic *r̥ gives Middle Persian ur, and intervocalic/final *-g- is spirantised and written -w (MacKenzie's murw; the same word is Manichaean MP mwrw and Parthian murγ). Nourai's two spellings 'murğ, merv' are two readings of the one Pahlavi grapheme sequence mwrw. The compound sēn-murw [synmwlw] 'a fabulous bird' is Av. mərəγō saēnō with the order reversed and the first element reduced to sēn, and it is the direct source of NP sīmurγ - MacKenzie glosses it '(N sīmurγ)'. The Bundahishn and Menog i Xrad passages Bartholomae and Mo'in quote ('the nest of the bird Sēn (sēnmurw) is on the tree Harwisp-tōxmag') show the word in real Pahlavi context. The gloss 'hawk bird' is acceptable for a bird of prey, though 'the (mythical) bird Sēn' is the accurate rendering.\",\n          \"derivation_fa\": \"murw فارسی میانه (نوشتهٔ mwrw) «پرنده» بازماندهٔ قاعده‌مند mərəγa- اوستایی / *mr̥gáh ایرانی آغازین است: *r̥ هجایی در فارسی میانه به ur بدل شده و *-g- در جایگاه میان‌واکه‌ای/پایانی سوده و به صورت -w نوشته شده است (قس mwrw فارسی میانهٔ مانوی و murγ پارتی). دو صورت «murğ, merv» در نمودار دو خوانشِ همان نویسهٔ mwrw است. ترکیب sēn-murw «مرغ افسانه‌ای» همان mərəγō saēnō اوستایی است با جابه‌جایی دو جزء و کوتاه‌شدن جزء نخست به sēn، و سرچشمهٔ مستقیم «سیمرغ» فارسی است؛ مکنزی خود در برابر آن «(N sīmurγ)» گذاشته است. عبارت‌های بندهش و مینوی خرد که بارتولومه و معین نقل می‌کنند («آشیان مرغ سین بر درخت هروسپ‌تخمک است») این واژه را در بافت واقعی پهلوی نشان می‌دهد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/مرغ\",\n            \"https://en.wiktionary.org/wiki/سیمرغ\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT\", \"status\": \"supports\", \"note\": \"No page is given in the book; the relevant Mo'in footnote is Borhan vol. 4 p. 1990 s.v. مرغ: 'پهلوی murw (پرنده، مرغ): اوستا mərəγa- (پرنده، ماکیان) «بارتولمه ۱۱۷۲»، «نیبرگ ص ۱۵۳» ... هندی باستان mṛga- (حیوان جنگلی، مرغ)'. It states exactly the Avestan > Pahlavi > Persian line of this node.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"PHD\", \"where\": \"pp. 57, 118 area, s.vv. murw, sēn murw, frašamurw (PHD.txt lines 493, 564; PHD_mackenzie.txt lines 3614, 4542)\", \"stance\": \"supports\", \"note\": \"'murw [mwlw' | M mwrw, (N murγ)] bird'; 'sēn murw [synmwlw | (N sīmurγ)] a fabulous bird'; also 'frašamurw [pl(l)mwlw | M fršymwrw] peacock' and 'murw-nīš augur', 'murwāg omen', showing the word's productivity.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 1172, end of the mərəγa- entry\", \"stance\": \"supports\", \"note\": \"'np. murγ Vogel; Huhn. - Pue.: murw' - Bartholomae himself gives the Pahlavi form murw as the reflex.\"},\n            {\"src\": \"NYB\", \"where\": \"Part II Glossary p. 140 s.v. murvik (NYB_vol2_glossary.txt line 2595)\", \"stance\": \"partial\", \"note\": \"'murvik [mwlw'k] an augury, an omen 181. - MPrth mwrgw'g (S); MPrs mwrw'; nyw-murwh of good augury (A-H II); Paz. murvai; NP murva.' The 1974 glossary has the derivative but no separate murw 'bird' lemma (Mo'in's citation 'Nyberg p. 153' is to the older 1931 Hilfsbuch glossary).\"}\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"morğ «مُرغ ١»; sîmorğ «سیمرغ»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP murγ/morγ 'bird; (later, specifically) hen' is inherited from MP murw with the restoration of the velar in writing and pronunciation (murw > murγ), and the narrowing 'bird' > 'domestic fowl' is a New Persian development that Mo'in notes explicitly ('در فارسی نیز بمعنی مرغ خانگی (ماکیان) استعمال شود'). sīmurγ is inherited from MP sēnmurw, with the regular Middle > New Persian change of majhūl ē to ī (sēn > sī) and the loss of -n before m in the compound; the popular explanation 'thirty (sī) birds', found in Rashidi and famous from Attar's Manteq al-Tayr, is folk etymology, as Mo'in says of the parallel word sīrang ('ولی این اشتقاق عامیانه است. جزو اول آن سی همان است که در سیمرغ آمده'). Horn no. 975 (p. 218) sets out the whole line: 'murγ Vogel; Huhn ... aw. mərəγa- Vogel; phlv. murγ, murv; ai. mṛgá- Waldtier; Vogel'.\",\n          \"derivation_fa\": \"«مُرغ» فارسی نو بازماندهٔ murw فارسی میانه است که در آن -w پایانی در نوشتار و گفتار به غ بازگشته (murw > murγ)، و تخصیص معنایی «پرنده» به «ماکیان» تحولی فارسی‌نو است که معین صریحاً یاد می‌کند: «در فارسی نیز بمعنی مرغ خانگی (ماکیان) استعمال شود». «سیمرغ» بازماندهٔ sēnmurw فارسی میانه است با تحول قاعده‌مندِ ē مجهول به ی (sēn > sī) و افتادن ن پیش از م در ترکیب. تعبیر عامیانهٔ «سی مرغ» که رشیدی آورده و از منطق‌الطیر عطار شهرت یافته، ریشه‌شناسی عامیانه است؛ معین در حاشیهٔ «سیرنگ» می‌نویسد «ولی این اشتقاق عامیانه است. جزو اول آن «سی» همان است که در «سیمرغ» آمده». هرن نیز در شمارهٔ ۹۷۵ (ص ۲۱۸) همین زنجیره را می‌آورد. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/مرغ\",\n            \"https://en.wiktionary.org/wiki/سیمرغ\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/mr̥gáh\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"BQT:1990\", \"status\": \"supports\", \"note\": \"BQT vol. 4, printed page 1990 (the page carries '-۱۹۹۰-'; BQT_v4_pages.txt pdf page 73), s.v. مرغ: 'وبضم اول و سکون ثانی، معروف است که مطلق پرندگان باشد' with footnote 4 'پهلوی murw (پرنده، مرغ): اوستا mərəγa- (پرنده، ماکیان) «بارتولمه ۱۱۷۲»، «نیبرگ ص ۱۵۳» ... هندی باستان mṛga- ... قس کردی، افغانی، آسی marγ (پرنده)، بلوچی murγ ... «اشتقاق ۹۷۵»'. Exactly this node.\"},\n            {\"ref\": \"BQT:1211\", \"status\": \"partial\", \"note\": \"BQT_v2_pages.txt leaf 669 (printed ~1211, leaf 163 = 705 + 506) is the سیرنگ page whose footnote points to سیمرغ: 'رشیدی گوید بمعنی سیمرغ زیرا که سی رنگ دارد ... ولی این اشتقاق عامیانه است. جزو اول آن «سی» همان است که در «سیمرغ» آمده (رک: سیمرغ)'. The سیمرغ article itself with Mo'in's long footnote on Avestan saēna is a few leaves later (leaves 676-78 = pp. ~1218-1220), so the page number lands on the cross-reference rather than the headword.\"},\n            {\"ref\": \"SYN:183\", \"status\": \"supports\", \"note\": \"Buck 3.64 BIRD begins on p. 183 and the discussion Nourai uses is at the top of p. 184 (SYN.txt leaf idx 219): 'Av. maraya- used of large birds (Barth. 1172), NPers. murgh bird : Skt. mrga- wild animal'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"HRN\", \"where\": \"no. 975, p. 218 (HRN.txt leaf 240)\", \"stance\": \"supports\", \"note\": \"'975. murγ Vogel; Huhn, murγ[abi Ente. maz. warγ. aw. mərəγa- Vogel; phlv. murγ, murv (auch Papyrus, Horn ZDMG 43, 51); ai. mṛgá- Waldtier; Vogel. kurd. mirawi Ente; afγ. marγa; oss. marγ Vogel; bel. murg, murγ Vogel, Huhn.'\"},\n            {\"src\": \"BQT\", \"where\": \"vol. 4 p. 1990 (مرغ) and vol. 2 pp. 1218-20 (سیمرغ/سین)\", \"stance\": \"supports\", \"note\": \"as in ref_check; the سیمرغ footnote adds 'آشیان سین‌مورو (سیمرغ) بر درخت هروسپ تخمک است' from Menog i Xrad and discusses the Avestan sēn as a person-name and bird-name.\"},\n            {\"src\": \"SYN\", \"where\": \"3.64 BIRD, pp. 183-184\", \"stance\": \"supports\", \"note\": \"as in ref_check; Buck also notes the Skt. mṛga- 'wild animal' connection (his 3.11).\"},\n            {\"src\": \"ARY\", \"where\": \"ARY_pages.txt\", \"stance\": \"silent\", \"note\": \"grep for مرغ/سیمرغ as headwords in Aryanpur's index finds no article (only incidental uses of مرغ in the glosses of چنگ, خایه and کرک).\"}\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sogdian\",\n          \"words\": \"mrğ\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Sogdian mrγ 'bird' (transliterated marγ; attested in the Buddhist, Manichaean and Christian corpora) is the direct Sogdian reflex of Proto-Iranian *mr̥gáh, with the syllabic *r̥ written simply -r- in the Sogdian script and the velar preserved as -γ. Gharib's Sogdian-Persian-English Dictionary entry 5809-range no. 5432 gives 'mrγ- B, M, S | marγ | Av. mərəγa | ... bird', i.e. Gharib herself derives it from the Avestan word of the root box, and lists the oblique/plural forms (nom. ob. -y, pl. mrγ'yst) and references (GMS 485, 1174, 1182; TSP 2.155, 456 etc.). This is the expected sister-form of Pahlavi murw and Parthian murγ.\",\n          \"derivation_fa\": \"«mrγ» سغدی (خوانده marγ؛ در پیکره‌های بودایی، مانوی و مسیحی گواهی شده) بازماندهٔ مستقیم *mr̥gáh ایرانی آغازین است: *r̥ هجایی در خط سغدی تنها با r نوشته شده و واکِ پایانی γ حفظ شده است. غریب در فرهنگ سغدی–فارسی–انگلیسی، مدخل ۵۴۳۲ (ص ۲۱۷)، می‌آورد: «mrγ- B, M, S | marγ | Av. mərəγa | … bird»، یعنی خود او این واژه را از همان واژهٔ اوستاییِ جعبهٔ ریشه می‌گیرد و صورت‌های اِعرابی و جمع (mrγʾyst) و ارجاع‌ها را نیز می‌دهد. این صورت، خواهرِ منتظرهٔ murw پهلوی و murγ پارتی است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Iranian/mr̥gáh\"\n          ],\n          \"ref_check\": [\n            {\"ref\": \"SOD:217\", \"status\": \"supports\", \"note\": \"SOD_pages.txt leaf 283 (0-based) = printed page 217 (printed = leaf - 66), entry '5432 mrγ-' B, M, S | marγ, marγ | Av. mərəγa | nom. ob. -y; ... pl. mrγ'yst | bird | GMS 485, 1174, 1182; TSP 2.155, 456, 3.139, 189 ...'. Nourai's SOD:217 is a genuine page reference and the entry says what the arrow says; the English index of the same dictionary lists 'bird 901, 2793, 5432'.\"}\n          ],\n          \"consulted\": [\n            {\"src\": \"SOD\", \"where\": \"p. 217, entry 5432 (SOD_pages.txt leaf 283)\", \"stance\": \"supports\", \"note\": \"as in ref_check - Gharib cites 'Av. mərəγa' in the entry itself.\"},\n            {\"src\": \"BRT\", \"where\": \"col. 1172 s.v. mərəγa-\", \"stance\": \"supports\", \"note\": \"Bartholomae's entry gives the Iranian reflexes (Pahlavi murw, NP murγ); the Sogdian form is not listed in AiW but is the regular counterpart.\"},\n            {\"src\": \"Wiktionary\", \"where\": \"Reconstruction:Proto-Iranian/*mr̥gáh (fetched 2026-09-07)\", \"stance\": \"supports\", \"note\": \"'*mr̥gáh: hen, bird. From Proto-Indo-Iranian *mr̥gás', with Avestan mərəγa, Parthian mwrg /murγ/, MP mwlw' /murw/ among the descendants.\"}\n          ]\n        }\n      ]\n    }\n  ]\n}\nJSONEOF\npython3 -m json.tool data/verification/page-336.json > /dev/null && echo \"JSON OK\""
}
```


### [2026-09-07T16:43:16.266Z] TOOL RESULT

```
JSON OK
```


## [2026-09-07T16:43:19.678Z] TOOL CALL #107: Bash

```json
{
 "command": "python3 tools/verify_check.py 336"
}
```


### [2026-09-07T16:43:20.981Z] TOOL RESULT

```
nodes verified: 14/14
node verdicts: {'plausible': 5, 'confirmed': 9}
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 13, 'partial': 5, 'not_found': 1, 'not_checked': 1}
books consulted: {'partial': 10, 'supports': 35, 'silent': 4} | by book: {'WLD': 5, 'KLN': 4, 'CHEUNG': 4, 'POK': 3, 'AHD': 3, 'Etymonline': 3, 'IEC': 3, 'HRN': 3, 'BRT': 3, 'NYB': 3, 'HUB': 2, 'ARY': 2, 'PHD': 2, 'BQT': 2, 'LAT': 1, 'KNT': 1, 'MON': 1, 'WEB': 1, 'SYN': 1, 'SOD': 1, 'Wiktionary': 1}
```


## [2026-09-07T16:43:30.502Z] TOOL CALL #108: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport io\np='data/verification/page-336.json'\ns=io.open(p,encoding='utf-8').read()\nold=\"BQT_v2_pages.txt leaf 669 (printed ~1211, leaf 163 = 705 + 506)\"\nnew=\"BQT_v2_pages.txt leaf 669 (printed ~1211: leaf 163 carries the printed number 705, so printed = leaf + 542)\"\nassert old in s\ns=s.replace(old,new)\nio.open(p,'w',encoding='utf-8').write(s)\nEOF\npython3 -m json.tool data/verification/page-336.json >/dev/null && python3 tools/verify_check.py 336 | tail -3"
}
```


### [2026-09-07T16:43:31.976Z] TOOL RESULT

```
root verdicts: {'confirmed': 2, 'plausible': 1}
ref checks: {'supports': 13, 'partial': 5, 'not_found': 1, 'not_checked': 1}
books consulted: {'partial': 10, 'supports': 35, 'silent': 4} | by book: {'WLD': 5, 'KLN': 4, 'CHEUNG': 4, 'POK': 3, 'AHD': 3, 'Etymonline': 3, 'IEC': 3, 'HRN': 3, 'BRT': 3, 'NYB': 3, 'HUB': 2, 'ARY': 2, 'PHD': 2, 'BQT': 2, 'LAT': 1, 'KNT': 1, 'MON': 1, 'WEB': 1, 'SYN': 1, 'SOD': 1, 'Wiktionary': 1}
```


## [2026-09-07T16:43:53.443Z] AGENT

Page 336 verified. `verify_check.py 336`: **14/14 nodes, 0 PROBLEM lines.**

**Verdicts** — nodes: 9 confirmed, 5 plausible. Roots: 2 confirmed (Mer 2, Mer 3), 1 plausible (Mereğa). Ref checks: 13 supports, 5 partial, 1 not_found, 1 not_checked; 49 `consulted` entries across 21 books.

**Plausible / weak items**
- *Mereğa root* — "a large bird" is right (BRT col. 1172 "Vogel, spez. von grösseren"; Buck 3.64 p. 184 quotes the same), and *mərəγō saēnō* is real (Yt 14.41), but the gloss "**dark** hawk bird" is unsupported: saēna- = large bird of prey, prob. eagle (= Skt. śyena-).
- *E0 #1 Latin* — only `mors` is secure; `mortarium`/`mordēre` are "probably/possibly" (Watkins, de Vaan), `morbus` is called of unknown origin by Watkins and Ernout–Meillet ("vain de chercher l'étymologie").
- *E0 #4 English smart* — cognate drawn as descendant: ME smerten < OE smeortan/smeart, not from OHG smerzan; Nourai's own KLN:1461 says "rel. to … OHG smerzan".
- *E1 #1 Sanskrit* — root mṛṣ-/marṣa- real, but `â-marš`/`pra-marš` are Horn's analytic forms (Hübschmann p. 84 stars *pramṛṣṭa-).
- *E1 #2 xâmŭš* — Horn 464 / Mo'in's Borhan footnote ("سانسکریت ā-marṣa") support it; Wiktionary only "perhaps from *mers-", Cheung omits it, and the x- and -ōš- are unexplained.
- *E1 #3 "Avestan / Old Persian muš"* — substance right but form/label off: sources have Av. marša-/maršavan- (BRT 1153-54) and Old Iranian *fra-ā-**mṛš**- (FFD:65, the cited page); Kent has no Old Persian 'forget' root.

**Reference-page problems (book, not extraction)**
- `HRN:101` → not_found; the xāmōš entry is no. 464 on **p. 103**.
- `KLN:959` → not_found; p. 958-59 is the "mega-" run. Klein's *simurg* entry is on **p. 1449/50**.
- `BQT:190` → not_found; p. 190 of vol. 1 is the آله/الیاس region. The سیمرغ material is vol. 2 pp. ~1218-20.
- `BQT:1448` (attached to xāmuš) is actually the **فراموش** headword — supports node #5, not #2. `BQT:1211` lands on the سیرنگ cross-reference; the سیمرغ article is a few pages later. `POK:970` glosses *smerd-* "to stink", not "painful" (that is pp. 736-37). `MON:2506` unverifiable (only the unpaginated 2-vol abridgement is on disk).

**No extraction errors**: I rendered PDF p. 336 and compared box by box — the JSON matches the printed page exactly (including `مُرغ ١`, the Nāser-Khosrow couplet and the empty Germanic box).

Archived 14 web sources via `fetch_source.py` (Wiktionary خاموش/فراموش/مرغ/سیمرغ/*mers-/*mr̥gáh/morbus/mortarium, Etymonline smart/mar/mortar/morbid/mortgage/remorse).
