# Verification process log — verify-page-289


## [2026-09-06T21:59:22.995Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 289 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-289.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-289.json. Write /home/sfmqrb/git/rishe/data/verification/page-289.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 289` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-06T21:59:24.548Z] AGENT

I'll start by reading the instructions.


## [2026-09-06T21:59:25.243Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-06T21:59:25.260Z] TOOL RESULT

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


## [2026-09-06T21:59:25.269Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-289.txt"
}
```


### [2026-09-06T21:59:25.281Z] TOOL RESULT

```
1	=== PDF page 289 (book page 259) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Kwei 1, Qwei, Qwi : to pay back, revenge, punish  (refs POK:637)
4	#1 (parent #0) [Avestan] refs=POK:637; SYN:826,1447 | kây 1 : be punished ; kaěnâ : punishment ; kâtha : revenge ; čitha : penalty ; čisti : sorrow
5	  #2 (parent #1) [Persian] refs=POK:637; KLN:1759 | kîn «کین» : hostility, revenge | extra: کینه
6	  #3 (parent #1) [Sogdian] refs=SOD:203 | kyn, kynh : vengeance, hatred
7	#4 (parent #0) [Greek] refs=KLN:1447 | poině : penalty
8	  #5 (parent #4) [English] refs=AHD | punish, penalty, pain
9	--- entry 1 ---
10	ROOT [Indo-European] Kwei 2, Kwoi : to pile up, build, make  (refs POK:637)
11	#1 (parent #0) [Avestan] refs=POK:637,638 | kay 2, kaeš, čay, čî 1 : to select, prepare ; čayeti, činvaiti : selects, sorts ; pairi-čayeti : set around ☞Per 1 ; ham-či, ham-čay : to put together ☞Sem 1 ; vi-čay, vi-kay : to choose apart, select ☞Wi
12	  #2 (parent #1) [Persian] refs=POK:637; BQT:167,380,676; HRN:204; AEF:152,582 | čîdan «چیدن» : to put in order, arrange, cut ; parčîn «پرچین» : fence ; anjîdan «انجیدن» : to cut up in pieces, pierce ; gozîdan «گزیدن ۱» : choose | extra: گلچین ، برگزیدن | NOTE: HUB:18 does not agree that "čîdan" and "anjîdan" are related.
13	  #3 (parent #1) [Avestan] refs=HRN:90; FFD:47 | taug, taux : to pay
14	    #4 (parent #3) [Pahlavi] refs=HRN:90; FFD:47 | tôxtan : to pay
15	      #5 (parent #4) [Persian] refs=HRN:90; FFD:47 | tozîdan «توزیدن» : to pay | extra: توختن ، توز ، کینه توز
16	#6 (parent #0) [Old Persian] refs=KNT:209 | sâ 1 : to build, pile up ; fra-sâ : build, erect
17	  #7 (parent #6) [None] refs=None | 
18	#8 (parent #0) [Avestan] refs=KNT:209 | spâ 2 : throw away
19	  #9 (parent #8) [Pahlavi] refs=KNT:209 | pari-sp : wall (built around) ☞Per 1
20	    #10 (parent #9) [None] refs=None | 
21	#11 (parent #0) [Avestan] refs=POK:637 | kaěš : make ; fra-kaěš, vi-kaěš : to prepare, arrange
22	  #12 (parent #11) [None] refs=None | 
23	#13 (parent #0) [Greek] refs=AHD | poiein : to create
24	  #14 (parent #13) [English] refs=None | poem, poet
25	
```


## [2026-09-06T21:59:28.930Z] TOOL CALL #3: Bash

```json
{
 "command": "cat data/extracted/batch/page-289.json && echo \"=== MATRIX ===\" && cat data/verification/sources/SOURCE_MATRIX.md",
 "description": "Read source JSON and source matrix"
}
```


### [2026-09-06T21:59:29.054Z] TOOL RESULT

```
{
  "pdf_page": 289,
  "book_page": 259,
  "entries": [
    {
      "root": {
        "name": "Kwei 1, Qwei, Qwi",
        "lang": "Indo-European",
        "refs": "POK:637",
        "gloss": "to pay back, revenge, punish"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:637; SYN:826,1447",
          "words": [
            {"translit": "kây 1", "gloss": "be punished", "script": null},
            {"translit": "kaěnâ", "gloss": "punishment", "script": null},
            {"translit": "kâtha", "gloss": "revenge", "script": null},
            {"translit": "čitha", "gloss": "penalty", "script": null},
            {"translit": "čisti", "gloss": "sorrow", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:637; KLN:1759",
          "words": [
            {"translit": "kîn", "gloss": "hostility, revenge", "script": "کین"}
          ],
          "script_extra": "کینه",
          "note": null,
          "quote": {
            "text": "گفتم زمن ای ماه چرا مهر بریدی؟ - گفتا که فلک بامن بد مهر به کین بود",
            "poet": "Hâfez"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Sogdian",
          "refs": "SOD:203",
          "words": [
            {"translit": "kyn, kynh", "gloss": "vengeance, hatred", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 0,
          "lang": "Greek",
          "refs": "KLN:1447",
          "words": [
            {"translit": "poině", "gloss": "penalty", "script": null}
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
            {"translit": "punish, penalty, pain", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    },
    {
      "root": {
        "name": "Kwei 2, Kwoi",
        "lang": "Indo-European",
        "refs": "POK:637",
        "gloss": "to pile up, build, make"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:637,638",
          "words": [
            {"translit": "kay 2, kaeš, čay, čî 1", "gloss": "to select, prepare", "script": null},
            {"translit": "čayeti, činvaiti", "gloss": "selects, sorts", "script": null},
            {"translit": "pairi-čayeti", "gloss": "set around", "script": null, "see": ["Per 1"]},
            {"translit": "ham-či, ham-čay", "gloss": "to put together", "script": null, "see": ["Sem 1"]},
            {"translit": "vi-čay, vi-kay", "gloss": "to choose apart, select", "script": null, "see": ["Wi"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "POK:637; BQT:167,380,676; HRN:204; AEF:152,582",
          "words": [
            {"translit": "čîdan", "gloss": "to put in order, arrange, cut", "script": "چیدن"},
            {"translit": "parčîn", "gloss": "fence", "script": "پرچین"},
            {"translit": "anjîdan", "gloss": "to cut up in pieces, pierce", "script": "انجیدن"},
            {"translit": "gozîdan", "gloss": "choose", "script": "گزیدن ۱"}
          ],
          "script_extra": "گلچین ، برگزیدن",
          "note": "HUB:18 does not agree that \"čîdan\" and \"anjîdan\" are related.",
          "quote": {
            "text": "به خنجر همه تنش انجیده اند - بر آن خاک و خونش برنجیده اند",
            "poet": "Labîbî"
          }
        },
        {
          "id": 3,
          "parent": 1,
          "lang": "Avestan",
          "refs": "HRN:90; FFD:47",
          "words": [
            {"translit": "taug, taux", "gloss": "to pay", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 4,
          "parent": 3,
          "lang": "Pahlavi",
          "refs": "HRN:90; FFD:47",
          "words": [
            {"translit": "tôxtan", "gloss": "to pay", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Persian",
          "refs": "HRN:90; FFD:47",
          "words": [
            {"translit": "tozîdan", "gloss": "to pay", "script": "توزیدن"}
          ],
          "script_extra": "توختن ، توز ، کینه توز",
          "note": null,
          "quote": {
            "text": "چو وامش بتوزی درم صد هزار - بده تا بدارد زما یادگار",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 6,
          "parent": 0,
          "lang": "Old Persian",
          "refs": "KNT:209",
          "words": [
            {"translit": "sâ 1", "gloss": "to build, pile up", "script": null},
            {"translit": "fra-sâ", "gloss": "build, erect", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 0,
          "lang": "Avestan",
          "refs": "KNT:209",
          "words": [
            {"translit": "spâ 2", "gloss": "throw away", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 8,
          "lang": "Pahlavi",
          "refs": "KNT:209",
          "words": [
            {"translit": "pari-sp", "gloss": "wall (built around)", "script": null, "see": ["Per 1"]}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 11,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:637",
          "words": [
            {"translit": "kaěš", "gloss": "make", "script": null},
            {"translit": "fra-kaěš, vi-kaěš", "gloss": "to prepare, arrange", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 12,
          "parent": 11,
          "lang": null,
          "refs": null,
          "words": [],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 13,
          "parent": 0,
          "lang": "Greek",
          "refs": "AHD",
          "words": [
            {"translit": "poiein", "gloss": "to create", "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        },
        {
          "id": 14,
          "parent": 13,
          "lang": "English",
          "refs": null,
          "words": [
            {"translit": "poem, poet", "gloss": null, "script": null}
          ],
          "script_extra": null,
          "note": null,
          "quote": null
        }
      ]
    }
  ]
}
=== MATRIX ===
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


## [2026-09-06T21:59:31.593Z] TOOL CALL #4: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KLN','SOD','AHD','BQT','HRN','AEF','HUB','FFD','KNT','WLD','IEC','PHD','NYB','MON','ARY','BRT','SKT','FSD','WEB','CHEUNG','ISS','DKS']:\n    if k in d: print(k, json.dumps(d[k],ensure_ascii=False)[:400])\n    else: print(k,'MISSING')\n\"",
 "description": "Check refs_online entries"
}
```


### [2026-09-06T21:59:33.186Z] TOOL RESULT

```
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft 
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-in
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-
SOD {"title": "Badr al-Zaman Gharib (Qarib), Sogdian–Persian–English Dictionary, Farhangan, Tehran 1374/1995", "kind": "archive_djvu", "url": "https://archive.org/details/SogdianDictionary", "lookup_hint": "Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in 
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://a
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, pri
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; 
AEF {"title": "Jalal Khaleqi Motlaq, Asas-e Eshteqaq-e Farsi, vol. I (آ–خ), Bonyad-e Farhang-e Iran 1356/1977 — this is the Persian TRANSLATION of Paul Horn's Grundriss der neupersischen Etymologie (HRN) with Hübschmann's Persische Studien (HUB) notes and added Persian/Pahlavi evidence", "kind": "catalog", "url": "https://openlibrary.org/works/OL38785552W (vol. 1, 1356) ; 2015 complete ed. «فرهنگ ریشه
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1
FFD {"title": "Mohsen Abolghasemi, Fe'l-ha-ye Farsi-ye Dari, Qoqnus, Tehran 1374/1995", "kind": "local_scan_ocr", "url": "https://asmaneketab.ir/product/کتاب-ماده-های-فعلهای-فارسی-دری-محسن-اب/ -> https://dl.eliteraturebook.com/app/public/attachments/6925d29630b83.PDF (free PDF site; grey)", "lookup_hint": "Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/downloa
KNT {"title": "R. G. Kent, Old Persian: Grammar, Texts, Lexicon, AOS 1950/1953", "edition_found": "1950 first ed. (Google/AOS scan 'oldpers'); 2nd ed. 1953 has same pagination for the lexicon apart from small additions", "kind": "archive_djvu", "url": "https://archive.org/details/oldpers", "identifier": "oldpers (also old-persian-grammar-texts-lexicon; oldpersiangramma0000kent is lending-only)", "loca
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DL
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/I
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mac
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verific
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/a
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sou
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-D
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-di
CHEUNG MISSING
ISS {"title": "H. W. Bailey, Indo-Scythian Studies: Khotanese Texts VI (Prolexis to the Book of Zambasta), Cambridge 1967", "edition_found": "not found; Bailey's Dictionary of Khotan Saka (1979) downloaded as the closest substitute", "kind": "google_books_preview+archive_restricted", "url": "https://books.google.com/books?id=4upthUgWo9YC (CUP 2009 reprint, partial preview) ; HathiTrust mdp.39015034317
DKS MISSING
```


## [2026-09-06T21:59:39.294Z] TOOL CALL #5: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/sources/refs_online.json'))\nfor k in ['POK','SYN','KLN','SOD','AHD','HRN','KNT','BRT','HUB','FFD','BQT','AEF','PHD','NYB']:\n    e=d[k]\n    print('==',k, e.get('page_offset'), '|', e.get('local_file'), '|', str(e.get('lookup_hint'))[:300])\n\" ; echo \"--- verify_check ---\"; sed -n 1,80p tools/verify_check.py"
}
```


## [2026-09-06T21:59:39.571Z] TOOL CALL #6: Bash

```json
{
 "command": "head -c 3000 data/verification/page-259.json"
}
```


### [2026-09-06T21:59:41.200Z] TOOL RESULT

```
== POK POK_01: leaf = p + 8 ; POK_02: leaf = p - 344 ; POK_03: leaf = p - 762 to -766 (varies slightly). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/POK_01.txt | Roots are headwords at line start, often numbered (e.g. '1. deru-'); each entry ends with 'WP. I 177' style refs (Walde-Pokorny) - useful for cross-checking WLD. POK_full.txt (from the indo-european.info / IED dump) has blocks 'Root / lemma: deru-' ... 'Page(s): 214-217' so grep -n 'lemma: deru' giv
== SYN leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt | Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.
== KLN KLN_1966: TWO printed pages per leaf: leaf ~= floor(p/2) + 12 (+-2), e.g. leaf 178 = p.333, leaf 438 = p.853, leaf 748 = p.1469. Vol. I = pp. 1-853, Vol. II = pp. 855-1776. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt | Headword at line start followed by comma and part of speech, e.g. grep -n '^evade,' KLN_1966.txt ; derivatives 'Derivatives: ...' end each entry. Nourai's 'KLN:164'-style numbers are 1966 two-volume pages.
== SOD printed page ≈ leaf − 66 in SOD_pages.txt (0-based \f blocks; 645 leaves; English intro precedes) | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/SOD.txt'] | Entries are numbered (e.g. '5809 nYkr'k B ...'); Nourai's SOD:NNNN numbers may be entry numbers (1–~10,800) rather than pages — check both. grep the Sogdian transliteration or the English gloss in SOD_pages.txt; printed page ≈ leaf − 66 (leaf 322 = p.256). Or archive.org full-text page search (retur
== AHD 1985 Watkins ed.: leaf = printed + 29 (e.g. leaf 41 = p.12). NOTE: Nourai's page numbers (1505-1550) are for the 1976 AHD appendix, which is NOT open online; the 1985 book has the same root entries (slightly revised) on pp. 1-109, so locate by root name, not page. | /home/sfmqrb/git/rishe/data/verification/sources/refs/AHD_watkins1985.txt | Online: single page https://ahdictionary.com/word/indoeurop.html with one anchor per root, e.g. ...indoeurop.html#deru- (also reachable from any word page via 'Indo-European roots' link); this is the revised 2000/2011 text. Local 1985 text: roots are bold headwords at line start, e.g. grep -n '^deru
== HRN leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt | Entries are numbered paragraphs: 'NNN. word 'meaning'' at line start, e.g. grep -n '^ *169\. ' or grep the Persian word in transliteration (bay, bak...). Nourai cites Horn by page; Horn's numbered entries are also cited by number in Hübschmann.
== KNT leaf = printed + 13 for pp. <~150, +15 for the Lexicon (pp. 164-215), e.g. leaf 166 = p.151. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/KNT.txt | Lexicon (Part III, pp. 164 ff.) headwords are transliterated OP words at line start followed by part of speech, e.g. grep -n '^apadana-' ; section refs like '$147'. Nourai's page numbers should fall in 164-215 for lexicon citations.
== BRT Columns 1-1874 are printed at the top of each column; the scan mostly has TWO columns/pages per leaf: leaf ~= col/2 + 10..40 (e.g. leaf 10 = col 1, leaf 603 = col 1138, leaf 910 = col 1743). Grep the column number rather than computing. local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt | Nourai's BRT numbers are Bartholomae's COLUMN numbers. Headwords are Avestan/OP in transliteration in bold at line start; OCR of the special transliteration is noisy - grep on a distinctive Latin gloss or the German meaning in quotes. Column numbers appear as standalone numbers at leaf tops.
== HUB leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt | Part I (pp. 1-115) follows Horn's numbering: entries look like 'NNN. word' with Horn's number; Part II is grammar by paragraph (§). grep the transliterated Persian word or Horn's entry number.
== FFD 115 leaves (PDF pages); printed page = PDF page − 5 (PDF 40 = p.35). 2nd printing 1385 of the same Qoqnus setting (ISBN 964-311-015-X). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_asmaneketab.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/FFD/FFD_pages_faseng.txt'] | Searched archive.org (Persian/Latin titles, author), ketabnak, noorlib, general web (pdf/download): nothing; only a related paid e-book 'واژگان زبان فارسی دری' (fidibo). ketabnak.com/book/45024 is a different book (فهرست فعلهای فارسی).
== BQT vol 1 (BQT_v1_pages.txt, 777 leaves): printed page ≈ leaf − 210 near the start of the dictionary text (leaf 296 = p.86), ≈ leaf − 220 in the middle (leaf 414 = p.194, leaf 534 = p.314), ≈ leaf − 228 near the end (leaf 740 = p.512); leaves 0–~205 are Mo'in's introduction (pages numbered in words). vol 2 (BQT_v2_pages.txt, 684 leaves): printed page ≈ leaf + 543 (±3), derived from running-head numerals; verify with the 'بقیه در صفحهٔ N' continuation notes at page bottoms. Nourai's BQT:918 → vol 2, leaf ≈ 375. || vol 3 (BQT_v3_pages.txt, 721 leaves): printed page ≈ PDF page + 1209 near the start (pdf 9 = p.1218, pdf 130 = p.1339), +1207 in the middle (pdf 300 = p.1507), ≈ +1203 near the end; the scan has some duplicated/mis-ordered pages and a reported gap at pp.1291-1294 — always confirm with the running-head numeral. vol 4 (553 leaves): printed = PDF page + 1917 throughout (pdf 100 = 2017, 300 = 2217, 551 = 2468). vol 5 تعلیقات (293 leaves, separately paginated): printed ≈ PDF page − 5 (pdf 150 = p.145, pdf 200 = p.195); its notes are keyed to page numbers of the main volumes ('صفحهٔ ۶۳۳ ...'). | ['/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v1.txt (raw djvu.txt, no page breaks)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/BQT_v2.txt (raw)', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v3_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v4_pages_faseng.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_picofile.pdf', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages.txt', '/home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/BQT/BQT_v5_pages_faseng.txt'] | grep the headword in BQT_v1_pages.txt / BQT_v2_pages.txt (pages separated by \f; leaf N = N-th \f-block, 0-based); or use archive.org full-text page search (returns leaf index of hits): curl -sG 'https://{server}/fulltext/inside.php' --data-urlencode item_id={id} --data-urlencode doc={file-stem} --d
== AEF None | None | Not online (searched archive.org, ketabnak, noorlib, web; only bookshop listings). Because it is a translation of Horn/Hübschmann, verify AEF citations against HRN (archive.org, see Western agent's refs; local HRN.txt) and HUB (local HUB.txt): the entry order (آ–خ) follows Horn's numbering. The 2015
== PHD leaf = printed + 21 (e.g. leaf 22 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.txt | Headword = Pahlavi in transliteration at line start, followed by Pahlavi script (not OCRed) and gloss, e.g. grep -n '^abar '. Alternative PDF: https://www.parsianjoman.org/wp-content/uploads/2015/09/A-Concise-Pahlavi-Dictionary.pdf (8.4 MB).
== NYB Part II: leaf = printed + 8 (e.g. leaf 9 = p.1). local file has \f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf> | /home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt | Nourai's 'NYB' numbers are Part II (Glossary) pages. Headwords are Pahlavi in transliteration at line start (e.g. grep -n '^apar'), with Avestan/OP/NP cognates and 'Bthl.' refs.
--- verify_check ---
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


### [2026-09-06T21:59:41.229Z] TOOL RESULT

```
{
  "pdf_page": 259,
  "book_page": 229,
  "verified_by": "claude-opus-5",
  "verified_on": "2026-09-06",
  "entries": [
    {
      "entry": 0,
      "root": "Kerd 1, Kred",
      "verdict": "confirmed",
      "modern_form": "PIE *ḱḗr, oblique stem *ḱr̥d- (root *ḱerd-) 'heart'; with the compound *ḱred-dʰeh₁- 'to place one's heart, trust'",
      "note": "Pokorny p.579 bottom–580 heads the entry exactly '(kered-:) kerd-, kērd-, kr̥d-, kred- ‘Herz’', so Nourai's headword 'Kerd 1, Kred', the language label 'Indo-European' and the gloss 'heart' all reproduce his source correctly; AHD (Watkins) has 'kerd-1. Heart. [Pok. kered- 579.]'. The one substantive caveat concerns the 'kred-' half: Pokorny himself (p.580) says the kred-dhē- 'believe' group is 'nicht hierher' (not to be connected with 'heart'), and Buck 17.15, Klein s.v. heart and Ernout–Meillet s.v. cor agree; modern standard works (Watkins/AHD, de Vaan 2008 s.v. crēdō, Wiktionary) do connect it, analysing *ḱred-dʰeh₁- as 'to place one's heart'. Nourai therefore follows the newer, now dominant, view — but not the page of Pokorny he cites. The Iranian branch has a further complication that the chart passes over: Indo-Iranian shows a voiced aspirate initial (Skt. hṛd-, Av. zərəd-, PII *ȷ́ʰā́rd) where *ḱ- is expected, 'unexplained voiced aspiration' (Wiktionary), 'mit init. as if fr. IE gh, due to a blend with some other word' (Buck 251).",
      "note_fa": "ریشهٔ هندواروپایی آغازین *ḱḗr (ستاک غیرفاعلی *ḱr̥d-، ریشهٔ *ḱerd-) به معنی «دل، قلب» است و پوکورنی در ص ۵۷۹–۵۸۰ سرواژه را دقیقاً «kerd-, kērd-, kr̥d-, kred-: Herz» آورده؛ پس نام ریشه، برچسب زبانی و معنایی که نورایی داده درست است. تنها نکتهٔ محل بحث بخش kred- است: خودِ پوکورنی در ص ۵۸۰ پیوند kred-dhē- «باور داشتن» را با «دل» رد می‌کند و باک و کلاین و ارنو–مه‌یه نیز همین نظر را دارند، اما واتکینز (AHD)، دِ وان و ویکی‌واژه آن را می‌پذیرند و *ḱred-dʰeh₁- را «دل نهادن» می‌دانند؛ یعنی نورایی از دیدگاه نو پیروی کرده است نه از صفحه‌ای که به آن ارجاع داده. نکتهٔ دیگر آنکه در هندوایرانی به جای *ḱ- انسدادی واکدارِ دمیده دیده می‌شود (سنسکریت hṛd-، اوستایی zərəd-) که هنوز توضیح قطعی ندارد.",
      "sources": [
        "https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/%E1%B8%B1%E1%B8%97r",
        "https://en.wiktionary.org/wiki/credo%23Latin",
        "https://www.etymonline.com/word/heart"
      ],
      "ref_check": [
        {
          "ref": "POK:579",
          "status": "supports",
          "note": "P
```


## [2026-09-06T21:59:58.620Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full lemma kʷei ===\"\ngrep -n \"lemma: k\" POK_full.txt | grep -i \"ei\" | head -40\necho \"=== POK_full Page(s): 636 / 637 / 638 ===\"\ngrep -n \"Page(s): 63[5-9]\" POK_full.txt | head -20"
}
```


### [2026-09-06T21:59:58.677Z] TOOL RESULT

```
=== POK_full lemma kʷei ===
44557:Root / lemma: keid- 
44575:Root / lemma: keis- 
45133:Root / lemma: kemero- komero-, keinero- 
47064:Root / lemma: kei- 
47070:Root/ lemma: kei-\ to move, go, departure, *die, derived from Root/ lemma: Rei-1\ to lie 
47396:Root / lemma: kleiR- 
47526:Root / lemma: kleg-, klog- klag-, klang- kleg-, klog- kleig- kleik- 
47677:Root / lemma: knei-g^h-, knei-b- 
47903:Root / lemma: kol(eli- : 'glue' derived from a reduction of the extended *glei-b'^- Root / 
48281:Root / lemma: krei-1 
48306:Root / lemma: krei-2, kreig-, kreik- 
48832:Root / lemma: kseip-, kseib- 
48854:Root/ lemma: kseiJo^-{*ghseiJo'^-) 
49019:Root / lemma: kueiek- or kelak-, kolak- 
49214:Root/ lemma: keiner-: cancer, turtle, derived from Root/ lemma: kam-er-\ to bend, curve, 
52439:Root / lemma: k''ei-1(t){*k''ehu-tj Note: common Proto Germanic -u- > -u-, -y-, -/-. 
52551:Root / lemma: k''ei-2{*k''ehu-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
53158:Root / lemma: k^t^ei- 
53463:Root / lemma: k''rei-{*k''ehur-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
89525:lemma: Rt^ei-: "to settle' : Root/ lemma: kt^eO)-, kt^aO')-: "to acquire, possess'. 
=== POK_full Page(s): 636 / 637 / 638 ===
52371:Page(s): 635 
52393:Page(s): 635 
52549:Page(s): 636-637 
52578:Page(s): 637-638 
52608:Page(s): 638 
52636:Page(s): 638-639 
52640:Page(s): 636 
52758:Page(s): 639-640 
53127:Page(s): 635-636 
53156:Page(s): 636
```


## [2026-09-06T21:59:59.952Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== AHD kwei ===\"\ngrep -n -i \"^kwei\" AHD_watkins1985.txt | head\necho \"=== KNT p209 area: sa- fra-sa ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==225 || NR==224 || NR==226' KNT.txt | head -120"
}
```


### [2026-09-06T22:00:02.021Z] TOOL RESULT

```
=== AHD kwei ===
=== KNT p209 area: sa- fra-sa ===
1; DSe 1°; DSE 1°; D8s 1^; DSt 1; рле 1°; DE 1; XPa 1; XPb 1; XPc 1; XPd 1; XPf 1; XPh 1; XE 1; XV 1; A!Pa 1^; A*He 1; A®Pa 1, 25. bagaha npm. ($10, $119, $172) DB 4.61, 63. bagünám gpm. AsH 7; DPd 1f; DPh 9; D8f 9; DSp 1°; DH 7; XE 2; XV 2; A’He 2. bagaibiš ipm. DPd 14f, 22, 24; DSe 50f°; DSt 8; XPb 28f; XPe 12f, 15; XPd 18; XPg 13f; XSc 5°; XV 26; A'Pa 23°. Вот ($42) ipm. D’8a 3. |
Bagábigna- sb. ‘Bagabigna’, a Persian, father of Hydarnes: Elam. ba-qa-pi-ig-na; from baga- ‘sod’ + d-bigna-, pte. in -na- of an unidentified verbal root, cf. perhaps Skt. bija-m ‘seed’ (575.1, $103.IV, $160.Ie, $243). Baglalbignah{ya} gsm. DB 4.84f.
Bagabuxía- sb. ‘Megabyzus’, an ally of Darius against Gaumata: Elam. ba-qa-bu-uk-5a, Akk. ba-ga-bu-ki-$u, Gk. MeyaButos. From baga- ‘sod’ + deriv. of root baug- ‘free’ ($102, §151): ‘God-freed’ (§160.Jc). Balgabluzsa nsm. DB 4.85.
Bagayddi- adj. ‘Bagayadi’, seventh month, Sept.-Oct.: Elam. байцай$, АКК. tasritu. From baga- ‘god’, with vriddhi (8126, §165), + yad- ‘worship’, with lengthened vowel ($126, $165) and formative -2- (8152.1): ‘God-Worship Month’ (8159, $161.Ia), probably referring to Mithras, since Phl. and NPers. call this month Mihr
‘(Month of) Mithras’ (Justi, ZDMG 51.247; Bthl. AiW 952-3). Bágayádait gsm. DB 1.55.
bàji- sb. ‘tribute’: NPers. Баг; deriv. (§152.1, $165) of root seen in Skt. bhdga- ‘portion, dis- penser’, OP baga- ‘god’, the verb being Skt. bhájatt ‘apportions’, Av. bag-, РЫ. bäztän (§101, $122, $128, $126). Балт asf. DB 1.19; DPe 9; DNa 19; DSe 18; XPh 17.
batugara- sb. ‘drinking cup, saucer’: if genu- ine ($55.11; JAOS 56.215; Schaeder, БРАМ 1935. 489-96), from batu- ‘wine’ ($153.1; etymology un- certain, but Hz. ApI 114 quotes Bariaxy from Athenaeus, bk. xi, page 784a, as the Persian word for ‘phiale, cup’) + -gara- (8143.1) ‘devouring, drinking’ ($160.Ia), cf. Av. aspé.gard ‘horse-de- vouring’, Skt. aja-gará- ‘goat-swallower, boa con- strictor’, Gk. dnuo-Bédpos ‘people-devouring’, Lt. carni-vorus ‘flesh-eating’, from root in Av. gar- ‘devour’, Skt. girdit, Lt. vorat, plE *g*er-. Bv. J As. 228.233-4 suggests, and На. AMI 8.9-17, Ap! 118—5, accepts cognation rather with Skt. galati ‘drips’, gdlayat ‘pours’, as ‘wine-pourer’, cf. Lt. рате ‘pour (as an offering to the gods)’, and NPers. piyàüla ‘drinking cup’, from *pati-gdra-. bülugara пет. ($56.V) АЧ.
ba*d- vb. ‘hind’: Av. band-, Skt. bandh-, Gt. bindan, pIE *bhendh-. See also badaka-. basta (NPers. bäst) nsm. past pte. pass. (867, $85, 5120, $122, 5182.1, 52421) DB. 1.82; 2.75, 90; 5.26. basta apm. DB 3.88".
ba"daka- sb. ‘subject, servant’ (cf. König, Кыр 64): Phi. bandak, NPers. bändäh; deriv. (§146.1T) of OP *ba"da- ‘bond, fetter’, Av. banda-, Skt. bandhd-, to pIE root *bhendh- (OP ba"d-; $39, $75.11, $111, §122, 8132.1). badaka пет. DB 2.20, 30, 49f, 82; 3.13, 31, 56, 85; 5.8. badakā npf. DB 1.19.
Bábiru- sb. (Babairu- because of Pali Báveru-, MB Gr. $80) ‘Babylon’, a city (S56.III, $166); ‘Babylonia’, a province of the Persian Empire; by transfer, ‘Babylonian’: Elam. ba-pi-li, Akk. bab-ilu, bab-ilàni ‘gate of the god(s)’, Gk. Вав (§75.V, $107). See also Babirwiya-. Bahrus пет. DB 1.14, 80; DPe 10f; РМа 26; DSe 25; DSm 7°; XPh 22; as ethnic ($56.11), DN xvi, A?P 16. Babirum asm. DB 1.83f, 91 bis; 2.2, 3, 3f; 3.82, 84, 87; 4115, 30. \Babiraus absm. ($168, 6182.1) DB 2.65. Варта lsm. DB 1.78, 81;
200 OLD PERSIAN
2.5, 6; 3.79, 88, 92; 4.2; DBd 7f; DBi 11 (written Bab*raw, $22); DSf 33 as loc. with усій, 33 as abl. with Ласа (hardly a real abl., corresponding to Av. -aut despite Hz. AMI 3.55n, Kent ЈАО 53.16).
Bābirwiya- adj. ‘Babylonian’: deriv. ($144.- ПТ) to preceding. — Bábiruviya nsm. DB 1.77, 79; 8.81; 4.13; DSf 20. Babiruviyam asm. DB 3.86. Babiruviyé npm. DB 3.78; DSf 53f. Bäbiruviyä apm. DB 3.88.
bar- vb. ‘bear, lift up, esteem’: present stem bara-, Av. батат, N Pers. bard, Skt. bhárati, Gk. dpa, Lt. fert, Gt. batrip, pIE *bhere/o- (8213). See also ubarta-, uSabdri-, Gaubaruva-, bara-. bara^tiy 3d pl. ($122, 5232.1) DB 5.22f (written berety, 522); DNa 42. abaram Ist sg. imf. ($61, $75.III, 5226.1) DB 1.2
2; 4.66. abara imf. ($40, $84, 5228.) DB 1.25, 55, 88, 94; 2.25, 34f, 40, 45, 54, 60, 68, 86, 97^; 3.6, 17, 37, 45, 62, 67 (written ar?r^, 854.11), 87; 4.61, 62; DNa 50f; DSf 19°, 32; XPh 33, 45. abara” 3d pl. imf. ($10, $40, $84, $106, 8232.1) DPe 10; DSe 18°; DSf 34. aba- raha” 3d pl. imf. ($10, $218, $282.11) DNa 19f; XPh 17 (written орт, §54.1). abara"tà 3d pl. imf. mid. ($10, $236.II) DB 1.19. abariya imf. pass. (535.1, $220, $228.IT) DSf 23°, 31f, 35, 36, 38f, 40, 48, 45. abariya" 3d pl. imf. pass. ($220, 8232.11) DSf 41, 47.  baratuv imv. (5237.П) AmH 11^; DPd 14; DSk 5. аталаш inf. ($238) DNb 41.
à + bar- ‘perform’: dbaratiy ($218, $228.1) DNb 25. Cf. also Hz. Ар] 110-1, who refers to à-bar- certain other forms listed above as augmented forms of uncompounded bar-.
pati- + à + bar- ‘bring back, restore’: райуй- baram Ist sg. imf. DB 1.68 (but -à- perhaps only by influence of pardbartam, JAOS 62.275; 558, $206c).
para + bar- ‘bear away, take-away’: pardbara imf. DB 1.71, 96. pardbartam nsn. past pte. pass. (§242.1) DB 1.62, 67f.
pari- + bar- ‘protect, preserve’ (cf. Hz. Ар 112-3): paribarümiy Ist sg. (8226.]) DNb 17. paribarühy 2d sg. subj. ($27, $136, §222.IT, 4227.1) DB 4.78; paribaráh*-di$ (827, etc.) DB 4.74. pari- barā 2d sg. imv. (5237.1) DB 4.72, 88.
fra- + bar- ‘proffer, grant’: frábara imf. AmH 7; AsH 9; DB 1.12, 25, 60; DPd 3f, 7f; DPh 8; DNa 33; DSf 11; DSm 3°; DSp 2°; D8s 6; DZc 4; DH 7; A’He 18f, 20.
bara- sb. ‘bearmg, bearer’: Av. -bara-, Skt. -bhara-, Gk. -фороѕ, pIE "bhoros ($32, $122, $1431, ҮТ), to root bar- ‘bear’, in aritibara-, takabara-, vacabara-; also bāra- ‘borne by, rider of’, with vriddhi (8122, $126, 5148.1), in asabdra-, ef, usabüri-. See Hz. Ар] 95.
bard- vb. ‘be high’: Ау, baraz- ‘high’, baraz- ant- ‘lofty’, NPers. burz ‘high’, Skt. brhánt- ‘lofty’, OHG berg ‘mountain’, pIE *bhergh-; in Bardiya-, barsan-, probably in brazman-.
Bardiya- sb. Smerdis’, brother of Cambyses ($16411): Elam. bir-h-ia, АКК. bar-zi-ia, Gk. Урёрӧ ($29.02, $30). Репу. (§144.1V) of OP bard- ‘be high’ (575.11): ‘The Exalted’. Bardiya пет. DB 1.30, 32, 39, 52f; 3.25, 35, 54; 4.9, 27, 82; DBb 4f; DBh 5. Bardiyam asm. DB 1.31 bis, 51.
barSan- sb. ‘height, depth’ (S81): Av. barazan- .
(ВМ. AiW 950); deriv. of OP bard- (575.1, $155.1; Scheil 21.26; Konig, Burgbau 51; Hz. AMI 3.57; Bv. Gr. $812; Kent, JAOS 51.204, 99.15). bar$nà ism. (806, $120) DSf 26, 26f.
bav- vb. ‘become, be’: present stem bava- (8213), Av. bavatti, Skt. bhdvati, Gk. ote ‘grows’, Lt. fut ‘I was’, Lith. butt ‘to be’, NEng. be, pIE *bheu-. See also büm:-. bavatiy (§122, §228.1) XPh 55, 56. bæa"ty 3d pl. ($232.1) DNb 14 (башайу in 2d copy, Hz. ApI 115; ef. $48). abavam Ist sg. imf. DB 1.28, 60, 72; 4.5; 5.4^; DSm 6°; XPf 35, 36f; XPh 30; XSe 4°. abava imf. ($228.IT) DB 1.32, 38, 34, 40, 48, 77, 80; 2.16f, 17, 80, 94; 3.10, 11, 20, 27, 28, 76, 82, 83; 5.5, M^, 30; DSf 25; XPf 26.  abava^ 3d pl. imf. ($112, $232.IT) DB 1.76; 2.7, 93; 3.78; 4.34. bavātiy sub). ($222.11, §228.1) DNa 43, 45f; DNb 59 (Lg. 15.74; confirmed by photograph, JNES 444). [biyjä 2d sg. opt. ($114, $218.11, $223.I, $227.11) DB 4.69. буй opt. Cbhy-net, Bv. Gr. $232, comparing Av. buyd{ from *bhu-iët; but ВЫ. Gdr. IP 1. $143 takes as *bhy-i48t, = Lt. fiet, which may be either non-thematie opt. or thematic subj.; $114, $122, 5208, $218.II, §223.1, $228. ID) DB 4.56 bis, 58, 59, 741, 75, 78f, 79°.
bigna-, in d-bigna-, see Bagabigna-.
biimi- sb. ‘earth (= world or ground)’: Av. bümi-, NPers. büm, Skt. (RV) nom. bháümi bhümis; deriv. of root bhav- (see bav-) in grade bhi-, cf. Skt. aor. ábhüt, Gk. ёфо ($11, $65, §152.1V, §179.- IIT).
LEXICON
bümim asf. DNa 2, 32; DSe 2°; DSf 1; DSt 2; DZe 1f; DE 2; XPa 1; XPb 2; XPc 1; XPd 2; XPf 2; ХР 1f; ХЕ 3; XV 2f; A!Pa 2^; A?He 2. ратат, asf. ($55.1) A3Pa 2. bümiyà sf. (8179.IT) DNa 11f; DSb 9; DSe 10; Рб 5; DSs 2°, 3°; DZb 4; DZe 6; DE 17f; XPa 9; XPb 17; XPe 7f; XPd 12; XPf 12, 25; XPh 10; ХР); XE 17; XV 13; A'Pa 18°; A?8e 4°; Wb 7; Wc 8; Wd 8.
BU nsf. ($42) DSf 24, 28. 
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
Maka- sb. ‘Maka’, a province of the Persian Empire (lit. on location given in JAOS 56.217-8): Elam. ma-ak-qa, АКК. ma-ak, cf. Gk. pl. Мака ($99, $1322, SI4LITD. See also Mactya-. Maka nsm. DB 1.17; DPe 18.
magu- sb. ‘Magian’, member of a priestly order of Media: Flam. ma-ku-i3, АКК. ma-qu-&u, Gk. Méyos ($153.1). Uncertain material on mean- ing and etymology, Kónig, Klotho 4 chap. 12, and RulD 66. magus nsm. DB 1.36, 44, 46, 64, 66, 101; 4.8; DBb 2. magum asm. DB 1.50, 54, 57, 73; 4.81.
Maciya- adj. ‘Macian’; pl., name of a prov- ince of the Persian Empire: deriv. of Maka- ($99, $113, 8132.2, $144.01). Maciya пет. A?P 29. Масту for nsm. (856.11) DN xxix. Macy npm. DNa 30; DSe 230; XPh 25.
madtar- sb. ‘mother’: Av. matar-, Skt. matdr-, Gk. Dor. ратар, Lt. mäter, pIE nom. *maté, stem *máler- ($154.П): in hamdtar-.
таша conj. ‘lest, that not, not’: mà ‘not’ + conj. tya (§133, 4292р).  matya-mam (5133) DB 1.52. тайа DB 4.43, 48, 71.
mabista- adj. ‘greatest’, equal to ‘crown prince’ in XPf (Speiser ap. Kent, Lg. 9.40-1; Hz. Apl 254-8): Av. masista-, NPers. mähist, Gk. ppxio ros ‘longest’ (radical vowel after that in anxos Jength"); superl. to pIE *mak-ros, Gk. накр, Lt. macer ‘thin’, pLE root *mak- (887) ‘be long and slender’ + superl.,suffix.<ste-) (S117, $156.11,
202 OLD PERSIAN
4190.1), Gk. -сто-, Av. -tšta-, Skt. (with aspira- tion) -gha-. таб: а пет. AsH 6; DB 2.13,
```


## [2026-09-06T22:00:07.008Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR>=232 && NR<=234' KNT.txt | head -80"
}
```


## [2026-09-06T22:00:08.076Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_full block around 52549 (k''ei-2) ===\"\nsed -n '52549,52620p' POK_full.txt"
}
```


### [2026-09-06T22:00:08.462Z] TOOL RESULT

```
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


### [2026-09-06T22:00:08.504Z] TOOL RESULT

```
=== POK_full block around 52549 (k''ei-2) ===
Page(s): 636-637 

Root / lemma: k''ei-2{*k''ehu-) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to pile, stow, gather 

Material: Old Indie cinSti, cayati^ piles up, lines up; collects, accumulates; joins, is based ', 
caya-xx\. " accumulation, heap '; kaya-xx\. " abdomen, body ' (actually "* build, figure, body 
structure '; or "*mass'?); cita^ layer, woodpile, pyre, stake', citi-\. " accumulation, layer, 
pyre, stake', cTtiA. " the collecting '; 

Avestan kay-, cayeiti, c/nva/f/^{*\egere) aussuchen, choose 'with i//- "divide, 
distinguere', with ham- "colligere, (Schrittlangen) aneinanderlegen'; np. c/0'5/7 "gather, 
collect'; 

gr. ttoi£(jo "create' (arg. -Boeotian STToiFnas ), then also " poetize, write poetry ', 
denominative of a *noi-F6-(; " constructing, creating ' (compare apTO-noi6(; " baker '); 



Old Bulgarian cinh (probably i/-stem: Old Indie cino-ti, Avestan cinvaiti, yet in Slavic with 
/"the first syllable, as Old Indie cTtf-) 'order, row, rank', ciniti^ sort, order, arrange, put in a 
line, build ', probably also kir. koju, kojfty^ instigate, prepare something evil', as gr. cpovov 
noisTv "murder instigate '), poln. dial, /ro/ics/i^ "succeed, proceed, go ahead'. 

A 5- further formations in Avestan kaes- (with Praverbien) " to place together, heap up, 
pile, arrange ', fra- "prepare, make ready ', i//-" prepare, get ready ' (Bartholomae Wb. 
429). 

References: WP. I 510, WH. II 406, Berneker538, Trautmann 124. 
Page(s): 637-638 

Root / lemma: Iceia-, k''lie-{*IC'ehu-es) Note: common Proto Germanic -u- > -u-, -y-, -/-. 
Meaning: to rest quietly, quiet, peaceful 

Material: Old Indie cira-m^ indecisiveness, delay', cira-^ lasting, continuing; ongoing, long 
'; Old pers. siyati-s^ complacency ' (= Latin quies), Avestan sa///-5 "pleasure, joy' {s- = sy-, 
compare gathav. syeitibyd), Avestan syata-, sata- " pleases ' (= Latin quietus), a-sata- " 
unhappy ' (= Latin inquietus), Flapu-aaTK;, Avestan saista- " most cozily, most gratifyingly ', 
np. sao' "blithe, glad', oss. ancayun^x^^'C; sogd. sV gleeful '; 

Armenian han-gcim^\ lie, rest ', han-gisV tranquility ' {-g'h from *-k"i-)\ 

Latin quies, -etis' tranquility ', quie-sco, -scere, -vT, -turn 'rest', with formants -/c»-(as 
Germanic 77by/7-) tranquTius, tranquiiius' peaceful' {trans + kfios); 

Maybe alb. ^e/e "quiet' a Latin loanword. 

Gothic tveila. Old English fiwJl, Old High German (ii)wJla " while, time'. Old Icelandic 
/7i//7a "couch, bed, place for resting ', hvlld' tranquility ', Gothic fveiian' stay, linger, 
hesitate, cease'. Old English HwaiaUH, Old High German wTion, -en' stay, linger'; 

Old Church Slavic pokojb " tranquility ', pokojg, pokojiti' calm, appease ', pocijg, pociti 
"rest'; 

Tocharian B sa/e"rich' (: Avestan syata-' pleases '); 

Lycian tezi' sarcophagus ' from *k"jetis{'7), Pedersen Lycian and Hittite 50. 

References: WP. I 510, WH. II 406, Trautmann 124. 
Page(s): 638 



Root / lemma: IceR-, IcoR-, IceR-s- {* k^ehuR-s-) 

Meaning: to seem, see, show 

Material: Old Indie /ras'a/e 'appears, glares, gleams, shines', cakasiti, ca/ras/a/e "shines, 

looks ', kasa-'C(\. ' being visible, shine'; 

Avestan akasaV perceives '; npers. 5^5/7 "expert, skillful', /7/ga/7 "sight'; s-extension
```


## [2026-09-06T22:00:15.597Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '52430,52550p' POK_full.txt"
}
```


### [2026-09-06T22:00:15.650Z] TOOL RESULT

```
cough ' ( *k"os-la) (common alb. -si- > -If-) 

Maybe alb. peshtyj^ spit' : cymr. pesyc:/?^ 'cough' a Celtic loanword. 

References: WP. I 506, Trautmann 119. 

Page(s): 649 

Root / lemma: k''ei-1(t){*k''ehu-tj Note: common Proto Germanic -u- > -u-, -y-, -/-. 

Meaning: to observe; to appreciate 

Note: 

(common Avestan Slavic k> c: alb. k> ts >q: Greek Tocharian labialized k"'-> /-). 

Material: 

In a- grade: 

A. Old Indie cayatr perceives, observes, is shy, is concerned ', cayu-^ showing reverence 

' = Old Bulgarian cajg, cajatr expect, wait, hope ' (lengthened grade *k"'el-d)\ 

Old Indie clnotl, c/M//" notices', citf-t ' sympathy, appreciation ', cf-tt "ghost, intellect': 
gr. ari^u) " not to honour, not to heed, slight, treat lightly, deprive of honour due ' from *a-Ti- 
T- " unheeding '; 

In e- grade: 

k^epj-ro-'m gr. ir\^6q, "warden, guard', rripsoo " perceive, protect; observe, wait, hide out 
and wait, lie in wait and make a surprise attack', perhaps also Old Indie cara-rr\. " spy, 
scout '; it may be added because of Old Indie cayatr\s anxious ' with zero grade also gr. 
TETiriMai "be grieving ', tetihux; "timorous, grieving '? 

To *kei- "move' (above S. 538 f.) belongs ke[i]so-, kepJsaWvne' in: 

In a- grade: 

Old Church Slavic casb m. " time' {* h2''ai-ska). 

In o- grade: 

alb. kohe, kohai. " time', {*hi''ei-ska) Jokl Mel. Pedersen 159^ f. 

Note: 



Also alb. pas/'moment' : Old Church Slavic cash m. a Slavic loanword. 

In a- grade: 

B. Old Indie cayate^rachi, straft', cetar-^ avenger', apa-citi-i. "repayment' (= anoTiOK;, 
tIgk;); 

Avestan kay-^ repay, atone', e.g. c/kayaTshaW atone, punish, curse, avenge ', pairi-a- 
kayayanta^ sie sollen als Bufte auf sich nehmen ', kaena-i. "penance, atonement' (= 
noivri, Slavic cena, compare also Lithuanian kaina), npers. km- "enmity, hate, rage, fury', 
Avestan ka&a-n. "repayment', ci&i-i. " atonement through payment', c/'z?a"ds., 
punishment ', osset. C///75' "honour' (as Tipn); 

In e- grade: 

gr. Tiu) and fiu) (Arcadian teIu) reshuffling after STSiaa, Tsiau)), Fut. fiou), Aor. etigq, 
participle Pass. Tsrl^jsvot; " assess; esteem, honour', noAu-TTTO(; " highly honored ', aTi£TO(; 
"unhonoured, not honouring or regarding '; 

hom. fivu), Attic fivu) (*tivF-u)) " atone, pay ', Med. " allow to pay or atone, punish ', 
Tivupsvai (Eur. Or. 323), hom. Tsivurai (as Cretan anoTSivuTw after STSiaa, Tsiau)); Fut. 
Tsiou), Aor. ETEioa (Thessalian nsTaai, Cypriot TreioEi ), tIgk; " payment, penance, 
atonement, punishment, revenge, vengeance ', noivr) " atonement, punishment, revenge, 
vengeance ' (out of it Latin poena); i\\xx\ " appraisal; honour; penance, atonement, 
punishment ', arlpoq " dishonouring, derisive '; 

probably Middle Irish cin, Gen. c//7ac/ "blame' {*k"'inu-t-s, compare Tivu-rai); 

In a- grade: 

Lithuanian kaina^ value, worth, price'; Old Prussian er-k/h/nt'{oit\r\e devil) set free, 
release '; 

In e- grade: 

Old Bulgarian cena^ valuation, price, satisfaction, penalty, punishment; honour, price ', 
cen/t/" assess '. 

In a- grade: 



Old Bulgarian kajQ, kajati s§^ feel repentance ', pokajati s§^ make penance, atonement ', 
okajati^ deplore, lament ', russ. /r^'^fe "rebuke", -sja^ feel repentance '. 

In e- grade: 

root extension k^eis-, A'"i9/lC- (compare above Old Indie cit, citi-)\ 

Old Irish ad-cT{*k"is-e-t) " sees ', cTall\. "reason' = cymr. pwyll, bret. poellAs. {*k"eis-la), 
etc. (Lewis-Pedersen 350); 



Old Indie cetati, cfketatr hat acht auf etwas, nimmtWahr', Perf. ciketa, participle 
cikitvan^ understanding, knowing ', Avestan ciki&va^ thinking over, deliberative ', Old Indie 
ciW-\. " thought, reasoning, discernment', Avestan cist'h ds.. Old Indie cinta^ thought, care 



Old Bulgarian cbtQ, cistT count, calculate, read a script; honor', *k''i-t-ti-> Cbstb{= Old 
Indie cftti-h) "worship, veneration, honour'; with ani. s- Latvian skietu, skitu, sA75/"mean', 
Impers. "shine, appear, seem'. 

In a- grade: 

Latvian skaittV count, recite prayers ', Lithuanian skait-au, -///"count, read '. 

References: WP. I 508 f., Trautmann 113, 124, 135, 138, SchwyzerGr. Gr. 686, 697. 
Page(s): 636-637
```


## [2026-09-06T22:00:34.551Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== POK_02 leaf 293 (p.637) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==294' POK_02.txt | head -60"
}
```


### [2026-09-06T22:00:36.168Z] TOOL RESULT

```
=== POK_02 leaf 293 (p.637) ===
*  (zum  i-St.  geworden  in  lit.  dial.  sunis,  lett.  suns, apr.  sunis  ,Hund*) ;  ^Form  lett.  suntana  ,großer  Hund' ;  lett.  kuna  ,Hündin' wohl  mit  westidg.  Gutt.,  Trautmann  Bsl.  Wb.  310?  oder  das  Ä  von  kuca ds.  (Lockruf);  vgl.  Büga  Kalba  ir  s.  I  196;  ganz  fraglich  aber  russ. poln.  suka  , Hündin';
toch.  A  kuj  Obl.  korij  B  Nom.  ku.
Die  Bedeutung  von  lat.  canis  als  ,unglücklicher  Wurf  beim  Würfelspiel' kehrt  in  gr.  xvcov  wieder,  sowie  in  ai.  Sva-ghnin-  eigentlich  ,Hundetöter', d.  i.  ,der  die  schlechten  Würfe  vermeidende,  gewerbsmäßige,  auch  unred- liche Spieler' ;  vgl.  auch  gr.  y,ivdvvog  , Gefahr  (*Hundswurf)'  aus  *y,vv-dvvogy zu  ai.  dyütd  , Spiel'?  Schwyzer  Gr.  Gr.  1,  335  oben.
WP.  I  465 f.,  WH.  I  152 f.;  Kurylowicz  Accentuation  19;  nach  Specht Idg.  Dekl.  32,  121  f.  Ableitung  von  der  Farbwurzel  2.  keu-,  S.  594.
ktires-,  kuers-,  kurs-  , Gehölz,  Baum'??
Gr.  TtqXvog  , Steineiche',  falls  aus  *Ä;wfs-7io-s(?)  :  ^aX\.  prenne  ,arborem  gran- dem',  cymr.  corn.  bret.  prenn  ,Baum'  (*ku7'es-no-)',  ablaut.  air.  crann (*kurs-no-),  Gen.  cruinn  ds.,  cymr.  prys  (prysg)  , Gehölz'  (*kurs-to-)  ]  ags. hyrst  , Gebüsch,  Gehölz',  as.  ahd.  mnd.  hörst,  hurst  ds.,  nhd.  Horst ,Raubvogelnest'  (*ku2's-to-',  weniger  wahrscheinlich  oben  S.  548);  slav. *chvorst^,  ksl.  chvrastije,  russ.  chvörost  ,Reisig,  Strauch',  slov.  hrdst  , Eiche* (*kuors-to-?),  mit  unerklärtem  Anlaut.
WP.  I  524,  Morris- Jones  Welsh  Gr.  128,  Machek  Slavia  16  (1939),  182  f., Mikkola  ürslav.  Gr.  177.  J.  B.  Hofmann  (Etym.  Wb.  des  Gr.  284)  be- trachtet gr.  TZQLvog  wegen  des  kar.  ON  nglraaaog  als  vorgriechisch-klein- asiatisch.
Kh.'
kba  kha!  Interjektion  des  Lachens;  mit  z.  T.  einzelsprachlicher  Neu- schöpfung.
Ai.  hdkhati  (Gramm.)  ,lacht';  arm.  xaxank  , Gelächter',  gr.  xcr^d^cü (aus  *xax«?w)  flache  laut';  lat.  cachinnö,  -äre  ,hellauf  lachen',  cachinnus , Gelächter';  ahd.  kachazzen,  kichazzen,  ags.  ceahhettan  ,laut  lachen';  aksl. usw.  chochotati  ds. ;  vgl.  lit.  kikenti,  kiknoti  ,kichern'.
Ähnliche  Schallwurzel  käk-  ^auslachen'  in  gr.  xijxa^w  ,schmähe';  ahd. huohön  , spotten,  höhnen',  as.  höhi-llk  ^lächerlich';  mit  germ.  -k-:  ags. hocor  n.  , Spott'.
WP.  I  336,  WH.  I  126.  Vgl.  oben  S.  497  Jia  ha.
^  Die  bei  WP.  I  341,  348  f.,  399  angeführten  Wurzeln  khäd-  ,beißen',  khähh-  :  khöbh- jkraftlos',  kherw  ,graben'  sind  nicht  als  idg.  zu  erweisen,  ebensowenig  das  von  Specht (Idg.  Dekl.  263,  Anm.  4)  angesetzte  khä-mo-  , krumm';  die  von  ihm  (S.  256)  angeführten ai.  Beispiele  khalati-,  kharva-f  khara-.  khanda-,  khora-  sind  säm
```


## [2026-09-06T22:00:36.699Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 punish/penalty/pain ===\"\ngrep -n \"^punish,\" KLN_1966.txt; grep -n \"^penalty,\" KLN_1966.txt; grep -n \"^pain,\" KLN_1966.txt; grep -n \"^poem,\" KLN_1966.txt; grep -n \"^poet,\" KLN_1966.txt\necho \"=== AHD watkins kwei ===\"\ngrep -n -i \"kwei\" AHD_watkins1985.txt | head -20"
}
```


### [2026-09-06T22:00:36.798Z] TOOL RESULT

```
=== KLN 1966 punish/penalty/pain ===
27948:penalty,  n.  —  F.  penalite,  fr.  ML.  poenalitatem, acc.  of  poendlitds,  fr.  L.  poenalis,  ‘of  punish¬ ment’,  fr.  poena,  ‘punishment’.  See  penal  and  -ty and  cp.  penality,  which  is  a  doublet  of  penalty.
26944:pain,  tr.  and  intr.  v.  —  ME.  peynen,  fr.  OF.  pener (3rd  person,  sing,  peine),  fr.  ML.  poenare,  ‘to penalize’,  fr.  L.  poena.  See  pain,  n.
29335:poem,  n.  —  MF.  poeme  (F.  poeme),  fr.  L.  poema, fr.  Gk.  7i0LT)[ia,  ‘something  done;  a  composition in  verse,  poem’,  from  the  stem  of  ttoieiv,  ‘to make’.  See  poet  and  -m.
29337:poet,  n.  —  ME.  poete,  fr.  OF.  poete  (F.  poete),  fr. L.  poeta,  fr.  Gk.  7:oiy)xy|?,  ‘one  who  makes,  an artificer,  a  poet’,  fr.  ttoieiv,  ‘to  make’,  fr.  I.-E. base  *qwei-,  ‘to  make',  whence  also  OI.  cindti, cayati,  ‘gathers,  heaps  up,  piles  up’,  citlh, ‘heaping  up,  piling  up,  ‘collecting,  collection’, OSlav.  cinu,  ‘act,  deed,  order',  ciniti,  ‘to  arrange, put  in  order’,  Cp.  poem,  poesy,  posy  and  the second  element  in  epopee,  onomatopoeia,  phar¬ macopoeia.  Cp.  also  payyetan,  piyyut. Derivatives:  poetaster  (q.v.),  poet-ess,  n.,  poetic (q.v.),  poetize  (q.v.),  poetry  (q.v.) poetaster,  n.  —  ModL.,  formed  fr.  L.  poeta  (see poet)  with  the  pejorative  suff.  -aster. Derivatives:  poetaster-ing,  n.,  poetaster-ism,  n., poetastr-y,  n.,  poetastr-ic,  poetastr-ic-al,  adjs. poetic,  adj.  —  MF.  (=  F.)  poetique,  fr.  L .  poeti- cus,  fr.  Gk.  t:olt]tix6?,  ‘capable  of  making,  ac¬ tive,  creative,  productive ;  pertaining  to  poetry, poetic’,  fr.  7io[.7]x6?,  ‘made’,  verbal  adj.  of Troietv,  ‘to  make’.  See  poet  and  adj.  suff.  -ic and  cp.  -poietic.
=== AHD watkins kwei ===
650:kwed-. To sharpen. Germanic *hwatjan in Old English hweittan, to whet: WHET. [Pok. k¥ed- 636.] kwei-. To hiss, whistle. Imitative root. Germanic *hwi-n- and *hwis- in: a. Old English hwinan, to whine: WHINE; b. Old English Awisprian, to whisper: WHISPER; Cc. Old English hAwistlian, to whistle: WHISTLE. [Pok. 2. kuei- 628.] kvei-'. To pay, atone, compensate. Suffixed o-grade form *koi-néd in Greek poiné, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE?, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA. [Pok. k#ei-t- 636.] kwei-2. To pile up, build, make. O-grade form *koi- in: a. Sanskrit kayah, body: CHEETAH; b. suffixed form *koi-wo-, making, in denominative verb *k“oiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATO- POEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kyei- 637.] kweia-'. To value, honor. Suffixed zero-grade form *kvi-ma (< *kvia-md) in Greek timé, honor, worth: TImocrAcy. [In Pok. kvei-(t-) 636.] kweia-2. To rest, be quiet. I. Suffixed zero-grade variant form *k¥i-lo- (< *kvia-lo-). 1. Germanic *hwilé in: a. Old English Awil, while: WHILE; b. Old English hwilum, sometimes: WHILOM. 2. Possibly Latin tranguillus, tran- quil (trdns-, across, beyond; see tere@-2): TRANQUIL. IL. Variant form *kvyé- (< *kwyes-) in Latin quiés, quiet (> quiétus, calm, retiring), and in requiés, rest, and requiescere, to rest: COY, QUIET; ACQUIESCE, REQUIEM, REQUIESCAT. [Pok. k¥eis- 638.] kweit-. White; to shine. Suffixed form *kweit-o-. 1. Ger- manic *hwitaz in: a. Old English hwit, white: WHITE; b. Middle Dutch wijting, whiting: WHITING?; c. Old High German hwiz, wiz, white; EDELWEIss. 2. Germanic *hwaitjaz in Old English hwé&te, wheat (from the fine white flour it yields): WHEAT. [Pok. 3. kuei- 628.] kwek-. To appear, see, show. Variant form *kveg- in Slavic *kaz- in Russian ukazat’, to order: UKASE. [Pok. k#ek- 638.] kvel-1, To revolve, move around, sojourn, dwell. I. Basic form *kvel- in Latin colere, to till, cultivate, inhabit: COLONY, CULT, CULTIVATE, (CULTURE); INCULT, INQUI- LINE, SILVICOLOUS. II. Suffixed form *k¥el-es- in Greek telos, “completion of a cycle,” consummation, perfection, end, result (> teleos, perfect, complete): TELIC, TELIUM, TELO-; ENTELECHY, TALISMAN, (TELEOLOGY), TELEOST, TELEUTOSPORE. III. Suffixed reduplicated form *k/(e)- kvl-o-, circle. 1. Germanic *hwewlaz in Old English hwéol, hweogol, wheel: WHEEL. 2. Greek kuklos, circle, wheel: CYCLE, CYCLO-, CYCLOID, CYCLONE, CYCLOSIS; BICYCLE, ENCYCLICAL. 3. Sanskrit cakram, circle: CHUK- KER. IV. O-grade form *kvol-. 1. Suffixed form *k¥ol-so-, “that on which the head turns,” neck, in: a. Germanic *h(w)alsaz in (i) Old Norse hails, neck, ship’s bow: HAWSE (ii) Middle Dutch hals, neck: RINGHALS (iii) Germanic compound *h(w)als-berg-, “neck-protector,” gorget (*ber- gan, to protect; see bhergh-'), in Old French hauberc, hauberk: HAUBERK; b. Latin collum, neck: COL, COLLAR, COLLET, CULLET; ACCOLADE, DECOLLATE!, DECOLLETE, MACHICOLATE, (MACHICOLATION), TORTICOLLIS. 2. Suf- fixed form *kol-d in Latin -cola and incola, inhabitant (in-, in; see en): -COLOUS; PRATINCOLE. 3. Suffixed form *kvol-o- in: a. Latin anculus, “he who bustles about,” servant (an-, short for ambi-, around, about; see ambhi): ANCILLARY; b. Greek polos, axis of a sphere: POLE}, PULLEY; c. Greek -kolos, herdsman, in boukolos, cow- herd: BucoLic. 4. Suffixed zero-grade form *k»J-i- in Greek palin, again (< “revolving”): PALIMPSEST, PALIN- DROME, PALINGENESIS, PALINODE. [Pok. 1. k¥el- 639.] kvel-2, Far (in space and time). 1. Lengthened-grade form *kvél- in Greek téle, far off: TELE-. 2. Suffixed zero-grade form *k»l-ai in Greek palai, long ago: PALEO-. [Pok. 2. kuel- 640.]
1348:CHASM ghai- CHASSIS kap- CHASTE kes-2 CHAUDFROID kele-1 CHEAP caupd CHECK tké- CHECKMATE tké- CHEER ker-! CHEESE? kWo- CHEETAH kWeij-2, skai- CHEILOSIS ghel-una CHELICERA ker-1 CHELONIAN gheli- CHEMOTROPHY threph- CHENILLE kwon- CHENOPOD ghans- CHERISH ka- CHERNOZEM kers-1 CHERRY ker-6 CHERSONESE ghers-, sna- CHESS’ kap-
1398:coy kweie-2 CRAB! gerbh- CRACK gere-2 CRACKNEL gere-2 -CRACY  kar-1 CRADLE ger-2 CRAKE gere-2 CRAM ger-! CRAMBO skerbh- CRAMP! ger-2 CRAMP2 ger-2 CRANBERRY gere-2 CRANE
1441:EsLis gWela-1 EBULLIENCE beu-! ECBOLIC gWele-1 ECCENTRIC kent- ECCHYMOSIS gheu- ECCLESIA kela-2 ECCRINE krei- ECEsIsS weik-1 ECHARD segh- ECHELON skand- ECHIDNA ang¥hi- ECHINO- ang¥hi- ECHINUS angVhi- ECHO (s)wagh- ECHOLALIA 1a- ECLAIR kelo-2 ECLAIRISSEMENT kelo-2 ECLAMPSIA [ap- ECLECTIC leg-! ECLIPSE leikw- ECLOSION kleu-3 ECOLOGY weik-1 ECONOMY weik-1 ECRU kreue-1 ECSTASY sta- ECTO- eghs ECTOSARC twerk- ECU skei- ECUMENICAL welk-1 ECZEMA yes- EDACIOUS ed- EDAPHIC sed-! EDDY eti EDELWEISS _athal-, kweit- EDEMA oid- EDENTATE dent- EDGE ak-
1673:ILLATION tele- ILLITERATE deph- ILLUMINATE leuk- ILLUSION leid- ILLUSTRATE leuk- IMBECILE bak- IMBIBE p6(i)- IMBRICATE ombh-ro- IMBRUE_bhreu-2 IMBUE ombh-ro- IMMACULATE macula IMMANENT men-3 IMMATURE ma-1 IMMENSE mé6-2 IMMERSE mezg-! IMMINENT men-2 IMMIX meik- IMMODERATE med- IMMODEST med- IMMOLATE mele- IMMORTAL mer-2 IMMUNE mei-1 IMMURE mei-3 IMP bheue- IMPAIR ped-1 IMPALE pag- IMPARITY pere-2 IMPART pere-2 IMPEACH ped-1 IMPECCABLE ped-1 IMPECUNIOUS peku- IMPEDE ped-! IMPEL pel-6 IMPEND (s)pen- IMPERATIVE pere-1 IMPERIAL pere-1 IMPETRATE peter- IMPETUS _pet- IMPINGE pag- IMPIOUS pius IMPLEMENT pele-1 IMPLICATE plek- IMPONE apo- IMPORT per-2 IMPORTANT per-2 IMPORTUNE per-2 IMPOSE apo- IMPOTENT poti- IMPOUND bend- IMPRECATE prek- IMPRESS! per-5 IMPRIMIS_ per! IMPRINT per-5 IMPROBITY pert IMPROMPTU em- IMPROVE es-, pert IMPUDENT (s)peud- IMPUGN peuk- IMPUNITY kweij-1 IMPUTE peu- IN-l ne
1898:MUSTARD meu- MUSTELINE mis- MUSTER men-! MUSTY meug-2 MUTATE mei-1 MUTCHKIN med- MUTE mul- MUTILATE mut- MUTTER mul- MUTTON mel-1 MUTUAL mei-1 MUZHIK man-1 MUZZLE musum MY me-1 MYCELIUM walso- -MYCETE meug-2 MYCO- meug-2 MYCORRHIZA wrad- MYELO- mis- MYIASIS § mu-2 MYLONITE mele- MYNA mad- MYNHEER me-1 MYO- mis- MYOCARDIUM kerd-1 MYOPIA mut-, okw- MYOSOTIS miis-, ous- MYRIAD meu- MYRMECO- morwi- MYROBALAN gWel@-2 MYSELF me-! MYSOPHILIA meu- MYSOPHOBIA meu- MYSTAGOGUE ag- MYSTERY! mut- MYSTERY? mei-2 MYSTIC mul- MYSTICETE miis- MYTHOPOEIC kWeij-2 MYXO- meug-2
2033:PAGE? pag- PAGEANT pag- PAILLASSE pel-1 PAIN kWei-1
2074:PENAL kWej-1 PENALTY kWei-1 PENCHANT (s)pen- PENCIL pes- PENDANT (s)pen- PENDENTIVE (S)pen- PENDULOUS (s)pen- PENGUIN weid- -PENIA (s)pen- PENICILLIUM pes- PENIS pes-
2084:-PHAGE bhag-1 -PHAGIA bhag-! PHAGO- bhag-1 -PHAGOUS  bhag-! PHALANGE bhelg- PHALANX bhelg- PHALAROPE bhel-1, ped-1 PHALLUS bhel-2 PHANEROGAM bha-! PHANTASM_ bha-! PHANTASMAGORIA bha-1 PHANTOM bha-1 PHARMACOPOEIA kWei-2 PHARYNX bher-2 PHASE bha-1 -PHASIA bha-2 PHELLEM bhel-2 PHELLODERM bhel-2 PHELLOGEN _bhel-2 PHENO- bha-1 PHENOMENON bha-1 PHEROMONE bher-1 PHILANDER ner-2 PHILANTHROPY ner-2 PHILATELY tela- -PHILE bhilo- -PHILIA bhilo- PHILLUMENIST leuk- PHILO- bhilo- PHILODENDRON deru -PHILOUS _bhilo- PHILTER bhilo- PHLEGETHON bhel-1 PHLEGM bhel-1 PHLEGMATIC bhel-1 PHLOEM bhlieu- PHLOGISTON bhel-1 PHLOGOPITE bhel-1, okw- PHLOX bhel-1 PHLYCTENA bhlieu- -PHOBE bheg¥- -PHOBIA bhegw- PHOEBE bheigw- PHOEBUS bheigw- PHONE! bha-2 -PHONE bha-2 PHONEME bha-2 PHONETIC bha-2 PHONO- bha-2 -PHONY bha-2 -PHORE bher-1 -PHORESIS bher-1 -PHOROUS bher-1 PHOS- bha-1 PHOSPHENE bha-1 PHOSPHORUS bha-1 PHOT bha-1
2094:PINE? kwei-1 PINEAL peie- PINFOLD bend- PINNA pet- PINNACE peie- PINNACLE pet- PINNATE pet- PINNULE pet- PINOCYTOSIS p6(i)- PINON peio- PINTLE bend- PINTO peig-1 PIOLET skep- PIONEER ped-1 PIOUS pius
2178:REIGN reg-! REIMBURSE bursa REINDEER dheu-1, ker-1 REINFORCE bhergh-2 REITERATE i- REJECT yé- REJOICE gau- REJUVENATE yeu- RELAPSE leb-! RELATE tele- RELAX slég- RELAY slég- RELEGATE leg-1 RELENT lento- RELIEVE leg¥h- RELINQUISH leikw- RELUCENT leuk- RELUCT leug-! RELY leig-1 REMAIN men-3 REMAND man-2 REMARK merg- REMEDY med- REMEMBER (s)mer-! REMEX ere-! REMINISCENT men-! REMIT (s)meit(a)- REMORA mere- REMORSE mer-2 REMOTE meue- REMOVE meue- REMUDA mei-1 REMUNERATE mei-! RENAISSANCE gene- REND rendh- RENDER do- _ RENDEZVOUS wOS RENEGADE ne RENEGE ne RENITENT kneigh- RENOUNCE neu-! RENOVATE newo- RENOWN no-men- RENT! do- REPAIR! pere-1 REPAND pete- REPARTEE pere-2 REPAST pa- REPEAT pet- REPEL pel-6 REPENT2 rép-1 REPERTORY pere-! REPINE kWei-1 REPLENISH pele-! REPLETE pele-1 REPLEVIN plegan REPLICATE plek- REPORT per-2 REPOSE! paus- REPOSIT apo- REPREHEND ghend- REPRESENT e@S- REPRESS per-5 REPRIMAND per-5 REPRISAL ghend- REPRISE ghend- REPROACH pert REPROVE per? REPTILE rép-1 REPUBLIC ré- REPUDIATE (s)peud- REPUGN peuk- REPUTE peu-
2180:REQUIEM kWeie-2 REQUIESCAT kWeia-2 REQUIRE quaerere REREDOS dorsum, re- RESCIND skei- RESCRIPT skribh- RESCUE kwét- RESEAU  era-2 RESECT sek- RESEMBLE sem-! RESENT sent- RESERVE ser-1 RESERVOIR ser-1 RESIDE sed-! RESIGN sekw-1 RESILE sel-4 RESIST sta- RESOLVE leu-1 RESORB srebh- RESOUND swen- RESPECT spek- RESPIRE spirare RESPITE spek- RESPLENDENT spel-2 RESPOND _spend- REST? sta- RESTITUTE sta- RESTIVE sta- RESTORE sta- RESTRICT  streig- RESULT sel-4 RESUME em- RESUSCITATE kei-3 RETAIN ten- RETALIATE telo- RETCH ker-2
2323:sTuD2 sta- STUDENT (s)teu- sTUDY (s)teu- STULTIFY _ stel- sTUM stam- STUMBLE stam- STUMP stebh- STUN (s)tena- STUPA steu(@)- STUPE steu(9)- STUPEFY (s)teu- STUPENDOUS (s)teu- STUPID (s)teu- STURDY trozdo- STUTTER (s)teu- stTy2  steigh- STYLITE sta- STYLOBATE gWa-, sta- STYPTIC steu(@)- Styx (s)teu- SUASION swad- SUAVE swad- SUB- upo SUBALTERN al-1 SUBAUDITION au-5 SUBDUCTION deuk- SUBDUE deuk- SUBITO ei-! SUBJACENT yé- SUBJECT yé- SUBJOIN yeug- SUBJUGATE yeug- SUBLUNARY leuk- SUBMERGE mezg-! SUBMIT (s)meit(9)- SUBORDINATE ar- SUBORN ar- SUBPOENA kwei-1 SUBREPTION rép-1 SUBROGATE reg-1 SUBSCRIBE skribh- SUBSEQUENT sekw-1 SUBSIDE sed-1 SUBSIDY sed-1 sUBSIST sta- SUBSTANCE sta- SUBSTITUTE sta- SUBSTRATUM ster-2 SUBSTRUCTION | ster-2 SUBSUME em- SUBTEND ten- SUBTERFUGE bheug-', upo SUBTERRANEAN ters- SUBTLE teks- SUBTRACT tragh- SUBULATE syU- SUBVENTION gWa- SUBVERT wer-3 SUCCEED ked- succincT kenk-1 succor kers-2 succuBUS keu-2 SUCCULENT seud-2 SUCCUMB keu-2 SUCCUSSION kwét- SUCH swo-
2389:THYME dheu-! -THYMIA dheu-1 THYROID dhwer- TICK? deigh- TICK3 dhé-1 TICKET steig- TIDE! da- TIDE2 da- TIDINGS da- TIE deuk- TIERCE trei- TIFFANY bha-1 TIGER steig- TIGHT tenk-2 TILE (s)teg- TILLER? teks- TILLERS del-3 TILT? del-3 TIMBER deme-1 TIME da- TIMOCRACY kWeig-1 TINCT teng- TINGE teng- TINSEL skeei- TINT teng-
2400:TRAIN OIL dakru- TRAIT tragh- TRAITOR d6- TRAJECT yé TRAMMEL macula, trei- TRAMP der-! TRAMPOLINE der-1 TRANCE ei-1 TRANQUIL kweie-2 TRANS- tere-2 TRANSACT ag- TRANSCEND skand- TRANSCRIBE  skribh- TRANSDUCER deuk- TRANSECT sek- TRANSFER bher-1 TRANSFIGURE dheigh- TRANSFIX dhig¥- TRANSFUSE gheu- TRANSGRESS ghredh-
```


## [2026-09-06T22:00:52.660Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KNT grep frasa / sa- vb ===\"\ngrep -n \"fra-sa\\|frāsa\\|frasa\\|frasah\\|frāšahya\\|frasahya\" KNT.txt | head -20\necho \"--- awk pages 226-231 headers ---\"\nfor i in 226 227 228 229 230 231; do echo \"### NR=$i\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | grep -o \"^[0-9]* OLD PERSIAN\\|LEXICON$\\|^[0-9]\\{3\\}$\" | head -3; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -c 200; echo; done"
}
```


### [2026-09-06T22:00:54.276Z] TOOL RESULT

```
=== KNT grep frasa / sa- vb ===
1758:-a- stems: frasa-, spaümaida-, Ainaira-, Auliydra-,
2528:I. The Sigmatic Aorist is seen in niy-aparsam ‘I inscribed’ (or -apiSam?)}, to root pai8-, pIE *peik-; in mid. adarSiy ‘I held’, to root dar-, pIE *dher-; perhaps in pass. -asahya in frasah[ya]. The aorist endings 3d sg. -s-t, pl. -s-nf, may also be respon- sible for the endings of @1$ -diSa" to root ay- (8208); akunaus akunavasa to kar-; adurujiyasa to durujiya-; abaraha to bar-.
2696:G. Ав dative of indirect object, in DB 1.12 Auramazdá хёасат manā frübaro, DB 1.81f kürahy& naiy azdà абага ‘it was not known to the people’, DB 1.75 kdrahyd агава afaha, DSa 5 nsahyd frasam badaydtary.
4201:1 adam : Dārayavauš : XS : vazraka : XS XSyan 2 ат : XS DHnàm : Vistáspahy& : риса : Ha 3 xümanifya : 08у : Dàrayavaus : XS 4 : vaSnà : AMha : adam : ava : akunavam : tya : 5 akunavam : visahyà :frašam : Oadayataly Note то DSa: * frasam : 9adayátaiy, Hz. ApI 156-8, for the previously accepted frasia : 0adayámaiy; but Hinz, ZDMG 95.223-5, supporta a[dam : visa]hyà : frašta : @адауйтаїу. TRANSLATION OF DSa: 1. 1-3. Tam... (= DPa 1-5). $2. 3-5. Saith Darius the King: By the favor of Ahuramazda I have done that which I have done; to every one may it seem excellent.
4316:Notes то D§j: * [paruv}iyaba naiy ‘nicht in einem einzigen Anhieb�� Brd.; [пратш)|туаба naty ‘wie nie zuvor’ Hz. Api 103; [+++-+]:yaa@ тату ‘nicht planlos’ Hinz, ZDMG 95.240-1. € frasam ðadayāļtaiy}) Hz., аз in Da 5, q.v.; frasta Gadaya{maiy} Scheil, supported by Hinz, ZDMG 95.224.
4342:| TT TTT tert +++ nas 2 lam : akunavam : дану : Da 3 rayavauk : XS : тата : AMha : Cis 4 àyà : idä : frasam : akunavam Nore то рдо: Hinz, ZDMG 95.255-7, restores in рагі as an inscription of Darius II (D*8d). TRANSLATION OF DSo:... І made. Saith Darius the King: By the favor of Ahuramazda, I constructed here at Susa an excellent (building).
5189:ufraSa- ufrasta- adj. ‘well punished": u- ‘well’ + pte. fraSta- or frasta- (893) ‘questioned, investi- gated? to root fraó-: pIE *su-prekto- (§33, 75, $242.II. — ufrasiam asm. DB 1.22, 4.66f; ufra&lam DB 438. ufrasa-diy apm. DB 4.69 (JAOS 35.351-2, ef. Bv. Gr. $845; not loc. ufrastë + prep. айту, as taken by ВШ. IF 12.110, A1W 60-1, Mt. Gr. $818).
5471:да"4- vb. ‘seem’: Av. sand-, Skt. chand- (887, $215). @adaydlary subj. mid. ($222.II) DB 4.49; DSa 5; 08) 6 (for text, see under frasa-; cf. 554.1). ðadaya inj. ($224, 5228.11, §237) DNa 58; рМ 53.
5709:fraša- adj. ‘excellent’ (‘tauglich’, König Burg- bau 48, Brd. АКМ 39.87): Av. frasa- ‘directed toward, useful’, formed on adv. fraša to frünk-, Skt. adv. praca to ртайс-, from pra- + añe- (Bthl. AiW 1006-7); the irregular -3- for -s- of Sy- may be a contamination of *frasa- and *frasya- (otherwise ВБ. IF 2,266-7; borrowed from Aves- tan aec. to Hz. ApI 162). Hz. ApI 156-65 (recant- ing derivation from fra- + záy- ‘shine’, ‘brilliant’, AMI 3.1-11) takes as deriv. of pra-, through an idiom of racing or fighting, as 'extra (certamen), hors (concours)’, and therefore "incomparable, su- preme’. Cf. also Hz. RHRel. 113.26; Bailey, BSOS 6.595-7; Kent, Lg. 15.169. — frasam nsn. DSa 5, DS] 6 (see frasta-, for reading). frasam asn. DNb 2; DSf 56, 56f; DSo 4^; DSs 1°.
5710:frašta DSa 5, DS] 6: discussed by Bv. ВІР 30.1.63-4, Gr. $103, Gray AJP 53.67, Brd. WZKM 39.20-1; but fra$am @adaydlary and not frašta ðadayämaiy ($54.11) should be read in both pas- sages (Hz. AMI 3.9-10, ApI 156-8). See under frasa-.
--- awk pages 226-231 headers ---
### NR=226
201
202 OLD PERSIAN
BUyà Isf. DSd 2°; DSf 7, 15, 16, 18, 24^; DSg 2; DSi 2, 4; DS) 1°; DSy 2; D'Sb 2; A’Sa 1; А4 2; A?Ha 2; A?He 9, 17; А?Ра 11.
brdtar- sb. ‘brother’: Av. brätar-, NPers. biraddr, Skt. bhra
### NR=227
24; 3.70; DPd 1; DPh 9; DSf9; DSp 1°; DH 7; XE 2; XV if; АНе1. [ma8]jiSta-ISàm] DB 5.27. mati&- lam asm. DB 2.20, 83; 3.12, 31, 57, 85; 5.6, 8, 12, 28; XPF 32.
Müda- (S166.IIT) adj. ‘Median’
### NR=228
ion), Lt. mort-uos (after vi-vos ‘liv- ing), pIE *mrios ($80, $109, $122, §242.1); see OP mar-, and cf. Hz. АрІ 249-51. тапа пзш. XPh 48, 55. marlahyá gsm. РВ 5.20, 36.
EU: ET TORR ON 
### NR=229
204
so a province of the Persian Empire, ‘Egypt’; тазе. sg. as sb., ‘Egypt’, a province: Elam. mu-is-sa-ri-ia, АКК. mi-sir (S6, §76.V).
(1) ‘Egyptian’: Mudrdya nsm. А?Р 19. Mudráyà
### NR=230
d sg. opt. mid. ($223.II, $284.1I) XPh 50. yadiyaiša” (8220, 5228.11, 4282.101; written 11924, $5.1; cf. Hz. AMI 8.67, ApI 357-8) 3d pl. opt. pass. (Ogden ap. JAOS 58.325; not yadiyatš 2d sg. opt.
### NR=231
206
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. r
```


## [2026-09-06T22:00:54.343Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT kaena / kaetha / citi / cisti ===\"\ngrep -n \"kaēnā\\|kaena\\|kaSnä\\|kaonä\" BRT.txt | head -10\necho \"=== SOD kyn ===\"\ngrep -n \"kyn\" SOD_pages.txt | head -20"
}
```


### [2026-09-06T22:00:54.410Z] TOOL RESULT

```
=== BRT kaena / kaetha / citi / cisti ===
8864:kaenan-
8911:•  j.  kaenan-  Adj.  'der  die  Rache  vollzieht, Rächer';    yat    'na    nijasiini   azjm  bridrO
=== SOD kyn ===
4376:    Hen. JRAS 1945, 152.22, 153.10, -m>xyy                        209 »pkyn B
4381:                                                                  210 »pkyn>k B                         ^_<^W
4382:                                                                      apkene ('pkyny(y)) ©<*apaka- =»»pkyn
4386:                                                                  211 »pkyn»y B                                  ^
4387:                                                                      apkene     ^>*pkyn*k
4396: 212 "pkynch  B
4402: 213 »pkyny(y)      M => »pkyn>k                                             apik       =*}pyk                              L?^1    \ji'
5903:745 >Ysy>wnkyn S                             J*Jofs~          759 >ytW B, S
7290:1218 toy'zkyn S                                         _u*jU        GMS 632; BBB 614; BSTBL, Dhy. 2; TSP; MDii
8673:1691 >st,wrh B, S                                                        1702 'stkyn'y B                                      J**^
8782:         101 etc. >nkynpw, VJ 38b; GMS 366, *skamb-,                     (a)skaruP, askruf ? ©<*skarf
12409:3048 pysykyn B                    (^^C^oJL- *!*.*>• tj^j*               Pyyj-
13509:                                                                  3426 8'rwkync     M                          ^J^S ^^3^
13515:                                                                  3427 SVwqync =» 5,rwkync
13517:                                                                  3428 8'nvkynyy    M                                    ^[f
15283:4056 y'mqyn      C, M =» y'mkyn                                   GMS 773; VJ 1448
15284:4057 y>mkyn B, S                             ^&ly      3S
15306:              b =* y>mkyn
15468:      GcOlament                                                  4133 ynqyn     C =* ynkyn
15529:4132 ynkyn B                                                         with effort ?, with toil ?
```


## [2026-09-06T22:01:04.936Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SOD entries numbered near 200-215 ===\"\ngrep -n \"^ *20[0-9] \\|^ *21[0-5] \\| 20[0-9] [a-z'>]\" SOD_pages.txt | head -30\necho \"=== SOD standalone kyn entry ===\"\ngrep -n \"kyn \" SOD_pages.txt | grep -v \"'pkyn\\|>pkyn\\|mkyn\\|nkyn\\|zkyn\\|ykyn\\|wkyn\\|qkyn\" | head -20\necho \"=== SOD_pages leaf 269 (p.203) ===\"\nawk 'BEGIN{RS=\"\\f\"} NR==270' SOD_pages.txt | head -40"
}
```


### [2026-09-06T22:01:06.891Z] TOOL RESULT

```
=== SOD entries numbered near 200-215 ===
4335:                                                                  200 »p>rs S                    ^yi^>,
4341:190 »p B, M, C                        (0yA ^> Jjt)j\              201 wp>t =* *P*t
4344:            >p ©f.; ace. -wh; ob. -y(hh ob. pi. ~ty               202 yt »p»t =» "p»t »p»t
4345:                                                                  203 »p>y- B.M.S       ^^ ^) &fSj> <ojuA,<
4381:                                                                  210 »pkyn>k B                         ^_<^W
4386:                                                                  211 »pkyn»y B                                  ^
4396: 212 "pkynch  B
4402: 213 »pkyny(y)      M => »pkyn>k                                             apik       =*}pyk                              L?^1    \ji'
4404: 214 "pm'nwk    M                        0^— «— ' 1 i^rf f iJCjU<^»l
4411: 215 Mpny   M                                                               ap-zamb(e)           (spznph)              j^u <v7jUT
4882:    ayamban =>*y>mPn, 'ympn                                               200 ff, Livsic. »/; Mack. BSTBL n p8
4888:     ayand       ©3pl. pres.   =$*y\ 'sty1                             MD; Gersh. Melanges Benv. 201 f. 203 n 10
6355:        CMS 1477; TSP; BSTBL, Dhy. 142; Frag. Len.                           203 p43
9454:           0o)erect, (to)pull, (resettle                                      VJ; TSP; BSTBL, Dhy. 305; GMS 200 n 1; Gersh.
14003:          210                                                                p95; Benv. Eti 323
19097: 215                                                                                                                            mr
19738:         210 86.16; mydmyd "every day", BSTBL, Dhu.                 mediation
24827:       Mack. BSTBL, Dhy. 207 p59; Benv. Notesi 47;
25479:7561 pVyy*ws- ~* ptyws-, ptyyws-                                       Sund. AoFviii 1981, 28R 22 p!99, 203 n 371
30621:           Benv. 209 nl3; Sund. MHC p26, 29
32159:     VJ 1022, 205 etc. pl06; TSP 21 ii 13; KG 619;                  TSP I3ii 14 n p228; SCE 359; Ben v. Vxtra et
32859:         120; wnh, Dhy. 344; ace. wnw, BBB a7; wn\                      Mack. BSTBL, Vim. 204 n p27
36873:11400 zrywn B                                                         GMS 940; S W, RL 209 n 23; TSP 2.152, 324,
=== SOD standalone kyn entry ===
4376:    Hen. JRAS 1945, 152.22, 153.10, -m>xyy                        209 »pkyn B
16752:     y/xaz/zta ? ^yzt'kyn                                               GMS 285; Hen. Tales. 469.37
16757:4556 Y?t*kyn B                                                          refinement
23141:     paSaman ©ob. -yh                                        6766 pS'stkyn B                                  Uy* 0l£s.T
23180:                                                                  6784 pS'yskyn B                              Jb^jlSiT
26091:7753 ptkyn =* ptkntw
27967:8403 r^kyn     B                                                          Frag. Len.38.5; Frag. 2a.29; r'Syh, BSTBL; TSP;
30459:9266 smY'kyn M                   j^\^\ptJik^tS\^LLjj\
32336:     wa-zawarkenst ©elat. adj. =^z}wrkyn                            upend    ©3pl. opt. =»wp-, pynt
36300:11211 z'wrkyn B, M, S                                 Ul_jJ *JL>j^J
36314:11212 zNvrqyn M, C =* z}wrkyn                                                       882.14, 914R4
=== SOD_pages leaf 269 (p.203) ===
     kysny                                                                                                            204


          TSP 2.810-11; Sogdica. p29 n 1; GMS 1056;            5133 ki-yu
                                                                    qyw C
                                                                                                                    Uijl**
            BSTBL, Vim. 31, Dhu. 257; Bailey. Prolcxis. 47
                                                                    lo it, to thai                               jf4<U>*
    5119 kysny B -* kysn>k
                                                                    C2 gloss.; Bcnv. JA 1951, 321
    5120 kysr S                                          ^J
         kesar (qysr)                                          5134 kyw}n B, M
                                                                                                         V^ ' cK J «$yf
                                                                    k£w<in
         Caesar                                                     Saturn, Saturday
         Hen. Tales. 478; KG 451, 466; STii 4.2, 20, 26, 29
                                                                    TSP 22.5, 6, 9, 10, 12, n p234; BBB 724; Hen.
    5121 qysr     C «► kysr                                           Tales. 484
                                                              5U5 kyw>6        B, M,S                oT ^>-* <oT .-»>*
         kesarkan
                                                                    ki/ywe/yS ? (qywyd, kywy5) «»k-
         (a kind of )coin, denarius                                 to it, towards it
         STi 36.4; GMS 1063; C2, 69V 14                             VJ 830, TSP 2, 200; GMS 1404; Frag. Len.; MDii(
                                                                      C2 gloss, n pi 16
   5123 kys- B, M                               d^    ^iT
         ki/9S ©inf. -*y                                      5136 kywnt => k-
                                                              5137 qywnt C                                           jT^
         GcOdecrease
         TSP 7.82; STii 9.16, 18; GMS 953, 1585; Hen. AM           kiwand (qywnO) ^kym'nt, qwynt, k-
                                                                   to him, to it
           1952, 203.3
                                                                   STii 2.12; 1.25; GMS 411; C2 gloss.
   5124 kysp B, M                                      ^
        kisp ©<lcarsvar\ Parth. qysfr                         5138 kywyS =* k-, kyw*y8
        country                                               5139 qywyd C ^ kyw*y8
         GMS 241; >flt-kysp(>\ TSP 3.207; -kyspyh, GMS        5140 qywn8 =¥ qywnt
           147                                                5141 kyy    M -» ky
   5125 kysph B                                j^*c^JV        5142 kyy' M ^ ky>
        kis(a)p ©<Av. kasyapa
                                                              5143 kyy >tyy M -» ky>                        ,,
```


## [2026-09-06T22:01:13.118Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 268 269; do echo \"##### leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' SOD_pages.txt | head -70; done"
}
```


### [2026-09-06T22:01:14.806Z] TOOL RESULT

```
##### leaf 268
                                                                                                                  202

 qwtr

5063 qwtr     C -► kwt'r                                     5080 kwzpVy ,B                        jl^.ciU.jUK
                                                                  kuzpawe
                                                                  zeal, energy
5064 kwtr'k =4 kwtr>y
5065 kwtr'y     B                  .J^(* V-^) ^ly*.               BSTBL, Dhu. 67; Benv. Notesi 41, Notesii 219
        kutre (kwttr'k, kwtr>k)                              5081 kwz(z) B                                     $J
        (related /<?)family
                                                                  koz ©<Av. kauzda\ Khot. kuysa
        TSP 2.30, 8.167, 171, 16.22; kwttrCkh TSP 2.547;
                                                                  crooked, hunchbacked
          BSTBL, Dhu. 25, 163, 219; f. adj. kwtr'nch,
                                                                  SCE 94, 317; Bailey. Prolexis. 50; -kwz}k (in
          Frye 5                                                    compd. )
5066 kwts'r     S(MD) =» kwrts>r
                                                             5082 ky B, M, S         (o^ y^> y)J ^^S          «£7 «T
5067 kwttr'k ^ kwtr>y
                                                                  ke (qy, kyy) ©<*ka(h)ya; Av. ko ©rel. pron4
5068 kwtty B                                  dj^^tjjj'             interrog. pron.; particle; conj. =^}ky
     ku/rti =*kwrty                                               who, that, which, he who, that which
        crore, ten million                                        EGSii 131; GMS 402, 1503-7, 1581; S W, C2
        BSTBL, Dhy.; TSP 2.179, 8.107
                                                                    p214 n p84.4; kfty, kyy Hyy% "who", GMS
5069 kwty =* >kwt-(y), }kw(-)ty                                     1506, 1523
                                                             5083 qy C =* ky
5070 kww' *» kwl
                                                             5084 ky> B,M,S                       Jrf^i&itf
5071 kww2 -» kw2
                                                                  kya (kyy\ >kyZY, qy>) ©*kahya- ^>ky
5072 qwy      M, C, S ^o ^yU oy     j*)£ <ol^T «lAo«S <6y-        who, which, whose
                                                                  GMS 1450, 1508; BBB 758; TSP 5.18; STii 1.49;
        kawi (kw*yst) ©<Av. kavi ^qw1
        giant, hero                                                 BSTBL, Dhu. 88; -kyywt, Anc. Lett. 2.49
        Hen. BSOAS 11.53f; C2, 13V19; Benv. JA 1959,         5085 qy> C, M -» ky>
          128; BSTii 886.5 pi. kw(>)yst "giants" GMS 1186;   5086 ky'ty -» qyt
          Hen. BSOAS 11,70.15,68.12                          5087 kyc B                         (^r^W      jU^g/
5073 qwy'q C                                                      kec
                                              JjM^J^              stupefied, giddy
     kawyak    ©f. n.
     heroism, bravery
                                                                  Benv.
                                                                    733 TSP 6.193 n p207; "movement" Hen. Texts.
     C2, 66V 16, 68V 6

5074 kwyc -» *k>wc-                                          5088 kyc>kh B                                        Pf
                                                                  kicak ? ©Skt. kita
5075 qwynt C                                            ^k        worm
     k(u)wint ? -»qywnt
     to that                                                      SCE 166

        STii 125 p586; GMS 411, 1463                         5089 ky8py    B

5076 kwyst'yc B               ? «LubL!{G)jb^(«u U^y)              kiOPe
                                                                  bat   ? ©<*ka0wiya-t Av. kaOwa
     k(u)wistec ©kuist <kuinst <*kuinct <*kuncit
     (related /o)sesame or hemp                                   TSP 13.20; SW, IIJ 1976,59
        TSP 2.892 n pl80; Hen. Texts. 734; kwync\ CII        5090 kySprm       B
          1990 B9                                                 keSparm ?
5077 kwyt     S(AL)-* qwynt                                       whoever
                                                                  TSP 17.35                                    f^>
5078 kwzp,B                       Jli«^V<JS,j<jli£*
     kuzp/b (kwzp) ^kwjp                                     5091 kySrp    B
     active, zealous                                              kiOrop, kisp ? ©<*krsw ^'kySrp
     TSP 3.65 n pl97; BSTBL, Dhu. 200                             form
                                                                                                                        J^
5079 kwzp =* kwzp                                                 BSTBL, Vim. 108; Hen. Texts. 721; GMS 141 n fc
                                                                                                         fW<j I
##### leaf 269
                                                                                                              M*

     203


     5092 kym'nt B                                                   5105 kyr-2 B                                              -^T
          kimand (qymnt) =*k-                                             ker ©<Av. karaya =»qs-, kst-
          to the, to this                                                                                                  kysn*k

            EGSii 129; GMS     1404, 1490; VJ 947, C2 gloss.               GMS 540 n 1- BSTBL, Vim. 30, kyr\ 2sg. pres.
                                                                           (to)sow    '
                                                                             subj.; AVS 104
     5093 qymnt     C =» kym'nt
     5094 qymG* C                                      c^U<^l^j      5106 kyrMn     B =* kyr>n, kr»n
          resurrection
                                                                     5107 qyr"n      M =* kyr>n
I           C2, 55R25, 57V 10                                        5108 kyr'n
                                                                           Cf-U
                                                                           kiran
                                                                                    B, M, S         (j^^j^^^/
                                                                                    (kyr*n, kyr*nh, qyr>n) ©<Av. karan
    5095 kymyS       M                                         ^k
            kime8/G (qymyS) =»k-                                              =»nykr}n, *pw kyr'n, nymy5 kyr'n, }ws*y kyr'n,
            to this                                                          xwrtxyz, xwrsn qyr'n, pJsy kyr'n
                                                                           side, direction
           GMS    1485; C2 gloss.; BSTii 893.24, 32
                                                                           GMS 111, 244; VJ; TSP; SCE; BSTBL; BBB;
    5096 qymy6      C =* kymyS               I
                                                                              MDii; Frag. Lcn.; MSP bl46; W-Li, ii: Gropp.
    5097 qyn     C -> kyn(h)                                                  p40; C2 gloss.; Sund. AoFviii 1981, 28R8 pl99;
    5098 kyn'k     B                                          ^*              Hen. Cosm. 312.88; BSTBL, kyr>nw, Dhy. 285;
         kinak     <£><*akinaka\ GK aklnakes
                                                                              Vaj. 18; kyr'nK VJ 33b; JfcyrVz, Dhu. 58, 148,
         sword
                                                                              293; qr>nt C2, 94R6 n pi 67.6
           TSP 6.7 n p202; BSTBL, Vim. 136; Prolexis. 84
                                                                     5109 qy^n      M, C -> kyr'n
    5099 kynWwytk      M, S                      ^   j» ^ > «S uy*
                                                                     5110 kyr>nh =* kyr'n
         kcn-osuydc ~»kyn(h)
         free from hatcrd                                            5111 qyrm C *> kyrm-
                                                                     5112 kyrm- B, M, S                                         >
           Gersh. Sogd. Cpds. 148; Sogdica. 60.10
                                                                           kirm, kirm (qyrm) ©<Skt. krmi         ©nom. ob. -y;
    5100 kynpr B                                       j^j/oj^               inst. -J; ace. -w\ pi. qyrmyst
         kenPar
                                                                           snake, worm
           hating, vengeful                                                GMS 140, 512; TSP 2.1042, 1072, 1073, 1077,
           BSTBL, Padm. 36; GMS       1131
                                                                              3.83, 135, 247, 6.9; SCE 118, 233, 324; Frag.
    5101 kynpry> B                                                            2a.3, 16; BBB b90; MSP p47; C2, 51V 12,
                                                     mjS   <*&*?
         ken(3arya
                                                                              57V32-, kyrm\ SCE 145, 358; kyrmw, TSP 13.18
           vengeance, hatred                                         5113 kyrmpwn S                            j^ r 'j>- «j^ ^^
           TSP 9.120                                                      kirm-pun
    5102 kyn(h) B, M                                                      snake hole
                                                           <^<j/
         ken (qyn) ©<Av. £ae/ia         ©ob. -yh                          Frag. 2a.l2; Benv. Notesii 49
           ^kyn^ws^vytk
         vengeance, hatred                                           5114 kirmne
                                                                          kyrmnyy M                              a>j^J'ly>J'
           GMS 120; TSP 2.1186; BBB bl7; Sogdica. 60.10;
                                                                          cankered, woxmediworm-eaten)
             STii 6.4.35; Frag. Len. 52.7; -/t, TSP 2, 169,
                                                                          Sogdica. 34.24; Hen. Cosm. 307.33
             13.12; kynyh, TSP 2.196
                                                                     5115 qyrmyr    C                                  yj^^
    5103 kynp> B                             J&*JZ                        ki/armir, kormir ^krnVyr
         kinapa, kimba <U<Syr. gnp\ <Akk. qunnapu
```


## [2026-09-06T22:01:21.170Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### HRN leaf 111 (p.90)\"; awk 'BEGIN{RS=\"\\f\"} NR==112' HRN.txt | head -60"
}
```


## [2026-09-06T22:01:22.307Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### HRN leaf 225 (p.204)\"; awk 'BEGIN{RS=\"\\f\"} NR==226' HRN.txt | head -60\necho \"##### HUB leaf 28 (p.18)\"; awk 'BEGIN{RS=\"\\f\"} NR==29' HUB.txt | head -60"
}
```


### [2026-09-06T22:01:22.812Z] TOOL RESULT

```
##### HRN leaf 111 (p.90)
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


### [2026-09-06T22:01:24.318Z] TOOL RESULT

```
##### HRN leaf 225 (p.204)
— 204 —
b ehren kann (ee ö biigrEzeö)\ Wenn man hier von
'fliehen* ausgehen wollte, so würde die Erklärung sehr
gezwungen sein.
915. giristen, giristen *klagen, weinen', Impt. girl ^) girye,
giryjden (Sahn. I, 107 Vers 837).
aw. [/^gar-, gerente 'anrufen*; phlv. grlstan 'weinen,
klagen (AV.), g(i)rt/TnUan (AV.) ; ai. [/^gar-, gpidti 'an-
rufen'.
kurd. girin weinen ; oss. d. yär, t. qär 'Geschrei,
Ton, Laut, Stimme* (88); bei. greag, n. girey 'lärmen,
schreien, heulen, weinen*, Impt. bigri (117)^).
916. fße^endj guzend (AM. S. 38 Zeile 7) 'Schade Leid',
bezendT 'Elend'.
aw. "^mjainti-, vergl. ai. vi -i- iXAa«-, vihanti- ; phlv.
agajand bezw. agazand (AV.).
917. gu^ärden 'auseinander setzen, darlegen, bezahlen ;
gtizäris, güzärisn (Wörterbücher)^), guzäre; vergl. vecer
(vejer) 'richterliche Entscheidung (unbelegt).
skr. vi + [/"car-, Caus. 'erwägen, in Betracht ziehen,
prüfen ; phlv. v(i)cartan (AV.), v(i)car(i)sn^)j v(i)cartar
'verständig (für aw. cazdönkvaM-, arm. LW. vcar 'Be-
zahlung*.
918. guziden 'aussuchen, erwählen*, Praes. giizm-em, guzin
'erwählt'.
aw. vi H- [/^öay- 'aussuchen* ; phlv. v{i)öUany v{i)cwet
(AV.), arm. LW. vöit 'rein, lauter*; skr. vi-^ i^cay-
'auslesen, aussuchen'.
bei. gicinag, n. gisainay auswählen, aussuchen* (104).
*) Im Reim bei Eth6, Morgenländische Forschungen, S. 59,
Zeile 5 v. u. (Dies Citat verdanke ich Herrn Prof. Nöldeke).
2) Hübsohmann, ZDMG. 44, 557.
3) Vu 11 er 8 8. V. menisn hat falsch gttSärisn; beide Stämme
sind nicht zu verwechseln, doch werden sie in den Wörterbüchern
immer zusammen geworfen.
*) Phlv. *v%närisn^ vltiärfan* ist wohl auch r{i)c" zu lesen (ein aw.
c ist eingedrungen, wie öfter); die Bezeichnung des i in der Praepo-
sition vi wäre sehr aufiPäUig.
##### HUB leaf 28 (p.18)
- 18 -
aller Erklarungsversuche noch vollkommen dunkel.
Ap. Grundform *avamaiti-, zd. *avama^ti'?
110. Np. hamhd^ nach Zenker = 'Mitspieler ist gebildet
aiis ham 'derselbe' = ap. hama- und "^baz ^SpieF (vgl.
haz^. *Spier), also = Masselbe Spiel spielend'. Dagegen
braucht anhdx 'Genosse, Theilhaber nicht zu baxtan
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
gestellt.
117. Der „Bedeutungswechsel* von zd. hafitaday- 'zusam-
menlaufen lassen' zu np. anddz- Verfen, entwerfen,
messen' ist nicht erkl^rt. Die Laute stimmen.
120. Vgl. afgh. plandar *Stiefvater von plar 'Vater' wie np.
pidandar von pid = pidar. ^)
121. Np. andarx^ar *passend' stimmt nicht gut zur Wzl.
svar glanzen*. Auch ist es mit dieser Wurzel irn Zend
(von hvar- 'Sonne' und x^arenah- 'MajestS,t' abgesehen)
wie im Iranischen schlecht bestellt, da zd. x^'aretd- und
x'^ared^a- (bei Justi = Glanz) nicht 'Glanz' bedeuten.
122**" (p.254). Salem ann's Gleichung: ati/a8t*Spinngewebe'
= ap. *ha(n)basta' kann auch ich nicht fiir richtig halten.
Naher liegt es, np. anbast, anbasta *ligatus' = zd. ham
-\- basta- 'gebunden , skr. sambaddha^ *zusanimenge-
bunden, geschlossen' zu setzen.
') So Btimmt auch afgh. plar-marai 'Waise' zu np. pidar-murda
'Waise' - dem der Vater gestorben ist.
```


## [2026-09-06T22:01:53.603Z] AGENT

Now let me launch web research in parallel while I continue with local reference books.


## [2026-09-06T22:02:13.960Z] TOOL CALL #20: Agent

```json
{
 "description": "Web research entry 0 kwei-1",
 "subagent_type": "general-purpose",
 "prompt": "You are helping verify etymologies for the rishe project (repo /home/sfmqrb/git/rishe). Do WEB research only (WebFetch/WebSearch) — do not write any files except via the archiving tool below. Work on PDF page 289, entry 0.\n\nThe chart (Ali Nourai, Etymological Dictionary of Persian/English, 1999) claims:\nROOT [Indo-European] \"Kwei 1, Qwei, Qwi\" = \"to pay back, revenge, punish\" (ref POK:637)\n- node #1 [Avestan] kây 1 \"be punished\"; kaěnâ \"punishment\"; kâtha \"revenge\"; čitha \"penalty\"; čisti \"sorrow\"\n- node #2 [Persian] (from #1) kîn «کین» \"hostility, revenge\" (also کینه kīne)\n- node #3 [Sogdian] (from #1) kyn, kynh \"vengeance, hatred\"\n- node #4 [Greek] (from root) poině \"penalty\"\n- node #5 [English] (from #4) punish, penalty, pain\n\nResearch and report on EACH of these, with attention to:\n1. The PIE root: modern reconstruction *kʷey- \"to pay, atone, compensate\" (Pokorny kʷei-1, 636-637). Is Nourai's label/gloss right?\n2. Avestan forms: kay-/kāy- \"to atone, punish\", kaēnā- \"punishment, retribution, vengeance\", kaēθa- \"punishment/retribution\" (Nourai writes \"kâtha\"), čiθi- \"atonement by payment\" (Nourai \"čitha\"), and especially čisti- — Nourai glosses it \"sorrow\"; check Bartholomae/Wiktionary: Avestan cisti- actually means \"insight, understanding, wisdom\" and belongs to the *kʷeys- \"to perceive\" extension. Is Nourai's gloss wrong?\n3. NP کین kīn / کینه kīne from Av. kaēnā- via Middle Persian kēn — confirm the MP form and the sound change (Av. aē > MP ē > NP ī).\n4. Sogdian kyn/kynh (kēn) \"vengeance\" — Gharib derives it from Av. kaēnā.\n5. Greek ποινή poinḗ \"blood-money, fine, penalty\" — is it from the same root, cognate with (not descended from) Avestan kaēnā? Latin poena borrowed from Greek; English pain (OF peine < L poena), penalty (ML poenalitas), punish (OF puniss- < L pūnīre < poena). Note whether Greek poinḗ is a *sister* of the Avestan word rather than the parent of the Avestan words (Nourai draws Greek from the root directly, which is right).\n\nFor EVERY web page you actually read and rely on, archive it by running:\npython3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note 'page 289 entry 0 <root/node>, used for <what>'\n(batch several in one Bash call). Only report URLs you archived successfully.\n\nGood sources: en.wiktionary.org (including Reconstruction:Proto-Indo-European/kʷey- and Reconstruction:Proto-Iranian pages, and the pages for کین, کینه, ποινή, poena, pain, penalty, punish), etymonline.com, ahdictionary.com/word/indoeurop.html.\n\nReturn a compact report: for each of the root and nodes #1-#5, give (a) the modern consensus form + gloss, (b) the precise derivation chain with sound changes/dates, (c) verdict suggestion (confirmed/plausible/disputed/etc.), (d) the list of ARCHIVED URLs. Be precise about forms and diacritics. Do not write any report file."
}
```


### [2026-09-06T22:02:15.945Z] TOOL RESULT

```
Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: a4c2648835495748b (internal ID - do not mention to user. Use SendMessage with to: 'a4c2648835495748b', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes. You know nothing about its results until that notification arrives — do not report, assume, or predict them; continue other work or respond to the user in the meantime.
Do not duplicate this agent's work — avoid working with the same files or topics it is using.
output_file: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tasks/a4c2648835495748b.output
Do NOT Read or tail this file via the shell tool — it is the full subagent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```


## [2026-09-06T22:02:37.455Z] TOOL CALL #21: Agent

```json
{
 "description": "Web research entry 1 kwei-2",
 "subagent_type": "general-purpose",
 "prompt": "You are helping verify etymologies for the rishe project (repo /home/sfmqrb/git/rishe). Do WEB research only (WebFetch/WebSearch) — do not write files except via the archiving tool below. Work on PDF page 289, entry 1.\n\nThe chart (Ali Nourai, Etymological Dictionary of Persian/English, 1999) claims:\nROOT [Indo-European] \"Kwei 2, Kwoi\" = \"to pile up, build, make\" (ref POK:637)\n- #1 [Avestan] kay 2, kaeš, čay, čî 1 \"to select, prepare\"; čayeti, činvaiti \"selects, sorts\"; pairi-čayeti \"set around\"; ham-či, ham-čay \"to put together\"; vi-čay, vi-kay \"to choose apart, select\"\n- #2 [Persian] (from #1) čîdan «چیدن» \"to put in order, arrange, cut\"; parčîn «پرچین» \"fence\"; anjîdan «انجیدن» \"to cut up in pieces, pierce\"; gozîdan «گزیدن» \"choose\"  (also گلچین golčīn, برگزیدن bar-gozīdan)\n- #3 [Avestan] (from #1) taug, taux \"to pay\"\n- #4 [Pahlavi] (from #3) tôxtan \"to pay\"\n- #5 [Persian] (from #4) tozîdan «توزیدن» \"to pay\" (also توختن tōxtan, توز tōz, کینه‌توز kīne-tūz)\n- #6 [Old Persian] (from root) sâ 1 \"to build, pile up\"; fra-sâ \"build, erect\"  (ref KNT:209)\n- #8 [Avestan] (from root) spâ 2 \"throw away\" (ref KNT:209)\n- #9 [Pahlavi] (from #8) pari-sp \"wall (built around)\"\n- #11 [Avestan] (from root) kaěš \"make\"; fra-kaěš, vi-kaěš \"to prepare, arrange\"\n- #13 [Greek] (from root) poiein \"to create\"\n- #14 [English] (from #13) poem, poet\n\nResearch each, focusing on:\n1. PIE *kʷey- (Pokorny 2. kʷei- 637-638) \"to pile up, build, make\"; Watkins/AHD \"kʷei-2 To pile up, build, make\". Confirm.\n2. Avestan čay-/či- \"to gather, select\", činuuaiti; vī-čay- \"to select\" (> NP گزیدن gozīdan via MP wizīdan); ham-čay-; pairi-čay-. Also Av. kaēš- \"to heap up, arrange\" and Nourai's \"kay 2\".\n3. NP چیدن čīdan \"to gather, arrange, pluck\" from MP čīdan/čīnīdan; پرچین parčīn \"fence, wattle\" — is it really pari-čay- \"set around\", or a different formation (par + čīn)? Check Hasandust/Wiktionary/Dehkhoda.\n4. انجیدن anjīdan \"to cut in pieces, pierce\" — Hübschmann (Persische Studien p.18 no.115) explicitly REJECTS Horn's connection with čīdan/Skt. sam-ci. What is the modern view?\n5. گزیدن gozīdan \"choose\" < MP wizīdan < Av. vī-čay- (note the w- > g- change typical of NP: wi- > gu-). Confirm.\n6. توختن tōxtan / توزیدن tōzīdan \"to pay, atone\" and کینه‌توز kīne-tūz — Cheung's Etymological Dictionary of the Iranian Verb has root *tauč \"to pay/atone\"? Is there an Avestan \"taug/taux\"? Horn (Grundriss p.90) says \"Eine ältere Form ist nicht vorhanden\" (no older form attested) and that Pahlavi tōxtan translates Avestan kāy- 'to atone'. So does an Avestan taug- exist at all? Check Bartholomae/Cheung/Wiktionary/Hasandust. Also: is tōxtan/tōzīdan related to PIE *kʷei-2 'to pile' at all, or to a separate root?\n7. Old Persian: is there an OP verb \"sā-\" meaning \"to build, pile up\", with fra-sā-? Kent's Old Persian Lexicon p.209 — check what OP frašam / frasa- means ('excellent'), and whether Kent lists a root sā- 'build'. Also Avestan \"spā- 2 throw away\" and Middle Persian parisp / parasp \"wall\" (< Old Iranian *pari-spā- 'thrown around'?). Check Wiktionary/MacKenzie/Iranica for parisp پریسپ.\n8. Greek ποιέω poieîn \"to make\"; poem/poet via Latin poēma/poēta. Confirm from Etymonline/Wiktionary/Beekes.\n\nFor EVERY web page you actually read and rely on, archive it:\npython3 /home/sfmqrb/git/rishe/tools/fetch_source.py '<URL>' --note 'page 289 entry 1 node #N, used for <what>'\n(batch several per Bash call). Only report URLs you archived successfully.\n\nReturn a compact report: per node, (a) modern consensus, (b) precise derivation chain with sound changes and intermediate forms, (c) verdict suggestion (confirmed/plausible/disputed/unverified), (d) archived URLs. Be precise about forms. Do not write any report file."
}
```


### [2026-09-06T22:02:39.436Z] TOOL RESULT

```
Async agent launched successfully. (This tool result is internal metadata — never quote or paste any part of it, including the agentId below, into a user-facing reply.)
agentId: a5bc06c1c5656c766 (internal ID - do not mention to user. Use SendMessage with to: 'a5bc06c1c5656c766', summary: '<5-10 word recap>' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes. You know nothing about its results until that notification arrives — do not report, assume, or predict them; continue other work or respond to the user in the meantime.
Do not duplicate this agent's work — avoid working with the same files or topics it is using.
output_file: /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/tasks/a5bc06c1c5656c766.output
Do NOT Read or tail this file via the shell tool — it is the full subagent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
```


## [2026-09-06T22:02:46.962Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG tauc / taug ===\"\ngrep -n -i \"tau[čcčg]\\|\\*tauc\\|toxtan\\|tōxtan\" CHEUNG.txt | head -30\necho \"=== CHEUNG kay / kaen ===\"\ngrep -n -i \"^\\*kai\\|\\*kaHi\\|kaēnā\\|kaena\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T22:02:47.027Z] TOOL RESULT

```
=== CHEUNG tauc / taug ===
5390:taugte', NHG taugen, etc., despite the apparent semantic difficulties (cf. EWAia, 
5392:useful’, i.e. ‘sie taugt’ ? (Lubotsky) 
5396:*IE COGNATES: Gr. eum ‘I prepare’, Goth. (pret.) daug ‘was useful’, NHG taugen. 
5680:*NEIR: Oss. I. baezzyn/beezt, beezzyd, D. bæzzun/bæzt ‘to suit, fit, be fit for, taugen’ 
14577:CSogd. ywxs- ‘to learn, study, be taught’, BSogd. ywc, CSogd. ywc, MSogd. ywc 
15923:ie. “gewaltsam niederbeugen und untertauchen (?) [Чо push under by force’]. 
25227:*IE COGNATES: MWelsh estwng ‘to yield, budge’, NHG stauchen ‘to thrust’, ? Gr. 
27102:formation of vac corresponding to Skt. ucyate ‘is taught! (< oc). Insler's 
41626:toxtan/toz-, 387, 388 
54000:stauchen, 387 
54003:taugen, 67 
=== CHEUNG kay / kaen ===
3135:*kaiHaja- ? 
15359:*kaiH (*taiH’) ? ‘to move, to set in motion ?” 
24189:*Kai ‘to live, dwell’
```


## [2026-09-06T22:02:49.090Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== PHD tox / parisp / wizid / cid ===\"\ngrep -n \"^tōxtan\\|^tōz\\|^tōxt\\|tōxtan\\|parisp\\|parasp\\|^wizī\\|^wizīdan\\|^čīdan\\|^činēn\\|^kēn \" PHD.txt | head -30\necho \"--- PHD_mackenzie ---\"\ngrep -n \"tōxtan\\|parisp\\|wizīdan\\|čīdan\\|^kēn\" PHD_mackenzie.txt | head -30"
}
```


### [2026-09-06T22:02:49.168Z] TOOL RESULT

```
=== PHD tox / parisp / wizid / cid ===
130:delete ozarak ... padist ... add threat. pad-nigerián ... for cared for, guarded read carefully. add  parisp [plsp | M prysp] wall. ?pid ... add (M pyt). purnay [pwin'd = Av. pərənayu-] adult. add  purr-marg |-mlg| deadly, baneful. raz ... add M rz. add rebas [lyp's | N ~] rhubarb. ?ristag ... add N rasta. add гох [lhw' | N <] rook, castle (chess). sahistan ... read (M shyd, P s‘y-). add sārwār [s ]w I helmet. add  sayistan, say- [ŠKBHWN-tn < A Vškb | P sy-] lie down.
5147:wizīhīdan
--- PHD_mackenzie ---
599:add parisp [pisp I M prysp] wall.
```


## [2026-09-06T22:02:55.905Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG lines mentioning toz- / tox ===\"\ngrep -n \"toz-\\|tōz\\|tozidan\\|tōzīdan\\|toxt\" CHEUNG.txt | head -30"
}
```


### [2026-09-06T22:02:55.947Z] TOOL RESULT

```
=== CHEUNG lines mentioning toz- / tox ===
24368:Yzgh. tozan-/tazant ‘to turn, whirl’, Sh. (Baj.) täz-/täzd, Rosh. téz-/tézd, Bart. toz-/ 
25264:*MIDDLE PERSIAN: MMP twz- ‘to expiate, pay for’, BMP twc- /toz-/ ‘to pay a debt, a 
35645:twc- /toz-/, 388 
41626:toxtan/toz-, 387, 388 
47709:toxtedol, 394
```


## [2026-09-06T22:02:58.193Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== CHEUNG kay/ci select ===\"\ngrep -n \"\\*[Cc]ai\\b\\|\\*Kai\\b\\|\\*CaiH\\|cinuuaiti\\|činuuaiti\\|cinvaiti\" CHEUNG.txt | head -20\necho \"=== CHEUNG index guzidan/gozidan/cidan ===\"\ngrep -n \"guzidan\\|gozidan\\|cidan/\\|čīdan\\|wizidan\" CHEUNG.txt | head -20"
}
```


### [2026-09-06T22:02:58.284Z] TOOL RESULT

```
=== CHEUNG kay/ci select ===
3059:*CaiH2 ? 29 
24189:*Kai ‘to live, dwell’ 
55187:*bar (s.v.), *cai', *daiz (s.v.), 
55195:*cai! (s.v.), *diHp (s.v.), 
56006:*cai! (s.v.), *9гйў (s.v.), 
56012:*cai! (s.v.), *tarH? (s.v.), 
56726:*cai', *garj’, Маш] 
56881:*bar (s.v.), *cai', *daiz (s.v.), 
57240:*cai! (s.v.), *drauH 
57626:*CaiH’, *cial 
=== CHEUNG index guzidan/gozidan/cidan ===
2943:*NWIR: Widely attested: NP čīdan/čīn- ‘to collect, gather’, cin (impv.) ‘pluck !’, Bal. 
2950:gather, pluck’ || (+ *pari-) NP parcidan/parcin- ‘to beat down the point of a driven 
2952:‘bramble’ || (+ *ui-) NP guzidan/guzin-, Bal. gicint/gicin- ‘to choose, select, elect’ 
41066:guzidan/guzin, 27 
41245:parcidan/parécin-, 27
```


## [2026-09-06T22:03:02.245Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== CHEUNG *cai1 block (around 2900-2990) =====\"\nsed -n '2900,2995p' CHEUNG.txt"
}
```


### [2026-09-06T22:03:02.296Z] TOOL RESULT

```
===== CHEUNG *cai1 block (around 2900-2990) =====

Pres. nu-: INJ. 3sg. OAv. vicinaot (Y 46.17), OPT. med. 35р. YAv. vicinaeta (V 16.2); Aor. athem.: INJ. 
159. YAv. -саёт (Yt 13.11), med. 3р1. OAv. visiiata (Y 30.3, Y 30.6), SUBJ. 2р1. OAv. vicaiiada (Y 
46.15); Aor. them.: INJ. 35р. ? YAv. -caiiat (Yt 13.28, ? P 56), med. ? YAv. hancaiiata (V 9.9), 3pl. ? 
Y Av. -caiion (Yt 13.22), SUBJ. 3pl. YAv. caiian (N 1); Partic.: pres. cinuuant- (Y 46.10, Y 56.13); Inf.: 
OAv. vicidiiai (Y 31.5, Y 49.6) 

*MIDDLE PERSIAN: MMP cyn-, BMP cyn- /ёш-/ ‘to gather, collect; tend (fire) || (+ 
*pari-) MMP przyd (past stem) “о shut in, imprison; fix in, fasten in’ || (+ *ni-) 
MMP псуп- ‘to pile up, heap together’ || (+ *ui-) MMP wcyd, ВМР woyt /wizid/ 
(past stem) ‘to choose” = DMMPP: 132, 283a, 240a, 337b 

Pres.: IND. 3sg. BMP cynyt /ётга/, 3р1. BMP cynynd /ёшёпа/, IMPV. 2р1. MMP cynyd-; Partic.: pres. 
MMP cyn’g, perf. pass. MMP cyyd, BMP cytk /cidag/; Inf.: MMP cyydn; Pass.: pres. IND. 3sg. MMP 
cynyhyd || (+ *ni-) Pres.: IND. 3sg. MMP nycynyd, MMP “ncynyd; Partic.: perf. pass. MMP ncyd 
*PARTHIAN: cyn- ‘to gather, collect’ || (+ *ni-) ncyn- ‘to pile up, heap up together’ || 
(+ *ш-) wZyn- ‘to choose’ = Ghilain: 85 | DMMPP: 132a, 240a, 338 

Pres.: IND. 3pl. cynynd || (+ *ni-) Pres.: IND. 3sg. ncynyd || (+ *ui-) Pres.: IND. 2sg. wycyn’h, 3sg. 
wZynyd, Partic.: perf. pass. wjydg, wyzyd, wjyd 

*KHOTANESE: (+ *pari-) pargyifia- ‘treasury, storeroom, enclosure’ 

*SOGDIAN: (+ *pati-) BSogd. pc’y ‘to profit’ || (+ *ш-) CSogd. wen-, MSogd. wcy- 
‘to choose, select’ 

(+ *pati-) Pres.: IND. 3sg. BSogd. pc’yt || (+ *ui-) Pres.: IMPV. 2sg. CSogd. wycn’; Pret.: IND. 3sg. 
MSogd. weytw ó rt; Partic.: perf. pass. wyctyt (pl.) ‘chosen’ 

*CHORESMIAN: (+ *upa-) ben- ‘to collect (wood) and heap up’, (pass./intr.) b/pcy- ‘to 
swell up, [intr.] blow up’ || (+ *ui-) m/wen- ‘to collect, gather’ || (+ *ham-) m/ncn- 
‘to close’, (pass.) m/nen- ‘to be closed’. Q Concerning b/pcy-, the cautiously 
suggested etymologies of MacKenzie III: 321 and Samadi (1.с.), *api-tusia- (*tauS 
‘to (be) empty’, q.v.) and *pati-Orusia- (*OraHu ‘to nourish’, q.v.) respectively, are 
both semantically and phonologically cumbersome. The Chor. form perhaps reflects 


*čai2 27 


pass. *upa-čija-, cf. Skt. upa-cit- (f.) ‘a particular disease, a kind of swelling disease’ 
(VS). || Samadi: 14, 148, 212, 120 

*NWIR: Widely attested: NP čīdan/čīn- ‘to collect, gather’, cin (impv.) ‘pluck !’, Bal. 
čit/čin- ‘to pick, gather’, Kurd. činīn/čin- (Kurm.) ‘to reap; to mow’, (Sor.) ‘to 
gather, glean [ear of corn]’, Awrom. Cıniay/Cın- ‘to pluck’, (caus.) Kurd. (Kurm.) 
candin/Cin-, (Sor.) candin/cén- ‘to sow, plant’, Gur. (Kand.) -cin- ‘to gather, reap, 
pluck, heap’, Abz. cida/Cen-, Abyan. Cia/Cin-, Ard. ёепае/ёеп-, Khuns. ¢in-/ci ‘to 
pluck, pick’, Jow. bam-tfi/a-tfin-, Meim. á:rem tfi:n/a:r etfi:n-, Nn. Ceye/Cin-, Natan. 
čiä, Qohr. cida/cin-, Tr. Ciya/sn-, Varz. Cinde/éin- ‘to reap, gather’, Semn. -cinc- ‘to 
gather, pluck’ || (+ *pari-) NP parcidan/parcin- ‘to beat down the point of a driven 
nail so as to fix it; to rout’, Gur. (Kand.) párcin 'thorn-hedge', Bakht. parzin 
‘bramble’ || (+ *ui-) NP guzidan/guzin-, Bal. gicint/gicin- ‘to choose, select, elect’ 
*NEIR: Sh. ci(y)-/cid, Rosh. cay-/cid, Bart. ciy-/cid, Sarig. cey-/cid ‘to reap, harvest’, 
Yghn. Gin-/cita, ? Wa. Cip-, čbīp-/čopt ‘to collect, pick’, Yi. &ü-/Cüvd, M. jüv-/juvd 
‘to pick, choose’ (< *ёіпџа- ?), M. Cin-/Einoy- ‘to build a wall’, cinv- ‘to collect; to 
build’ || (+ *abi-) Wa. vjin-/vjit- ‘to cover with a roof’ || (+ *pari-) Yi. parzin 
‘enclosure for sheep’, parZini ‘thorn-hedge’ || (+ *ni-) Yi. laZino ‘pile of firewood? || 
(+ *ш-) Sh. (Baj.) wijin-/wijid, Bart. wijin-/wijid ‘to release, sort out, cleanse, 
remove’, Wa. wicin-/wicind- ‘to disperse, scatter grain’ || (+ *ham-) Sh. anjic ‘clay 
jar for keeping nuts, dried apricots, etc.’ (*han-citi-ci-, EVS: 14b) || (+ *?) ? Yzgh. 
расӣ ‘stubble-field’. 0 On Sh. ci(y)-/cid, etc., hardly likely EVS: 25a: *draja-/ 
*drita-. Perhaps, the Pamir forms are old borrowings from Persian (or another 
Iranian language ?). 

*SANSKRIT: cay ‘to gather, pile up ' (RV+) = EWAia I: 531 

© The long -7- frequently found in Wlr. forms is analogical, cf. Hübschmann 1895: 
137, perhaps from the infinitive of causive-denominative formations in dan. There 
are no past stems with short 1 in Persian, for instance. 

PIE *K"ei- ‘to pile up, to heap, make’ = LIV: 378 f. | Pok.: 637 f. 


*IE COGNATES: Gr. xoiéo ‘I make, produce, compose’, OCS činiti ‘to arrange’ 
*REFERENCES: KPF I: 206a; KPF II: 190; Christensen, Contributions I: 257; Lambton 1938: 41b, 77b; 
IFL П: 200b f., 518b, 240b, 225b Ё; Andreev — PeSéereva: 239a; MacKenzie 1966: 92; EVS: 25a, 89b, 
52b, 14b, 116a; WIM I: 67; Werba 1997: 181 £; Steblin-Kamenskij 1999: 126, 379 f., 389; Cabolov 
2001: 237, 228; Lecoq 2002: 120, 123, 125 (passim); ESIJa II: 205 f£; Shahbakhsh: s.v. gicin-; Korn 
2005: 313, 371, 85, fn. 48, 395 (passim) 


*&aË чо atone, pay penalty’ 

*AVESTAN: Y Av. ci- (caii-, kaii-, kae-) ‘to atone’ = Liste: 22 

Pres. athem. red.: SUBJ. 3sg. YAv. cikaiiat (V 7.38, V 13.10, V 13.31, etc.), 3du. YAv. cikaiiato (F 48, F 
50, F 117), 3р1. YAv. "cikaiion (V 15.12, V 15.22, V 14.40), IMPV. 2sg. Y Av. ба... cici (? ба... “cicidi, 


28 *čai3 


F 238); Partic.: pres. desid. med. YAv. aißi.cicisomna- (N 63), Caus.: pres. OPT. med. 3pl. YAv. 
pairi.ākaiiaņta (Yt 10.122)
```


## [2026-09-06T22:03:02.679Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"===== CHEUNG *tauc block (around 25230-25300) =====\"\nsed -n '25230,25310p' CHEUNG.txt"
}
```


### [2026-09-06T22:03:02.733Z] TOOL RESULT

```
===== CHEUNG *tauc block (around 25230-25300) =====
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

*PARTHIAN: twj-, twc- ‘to pay, expiate’ = Ghilain: 63 | DMMPP: 330b 

Pres.: IND. 3sg. twcyyd, SUBJ. 15р. “twj’n, IMPV. 2р1. twjyd 

*SOGDIAN: CSogd. twZ, MSogd. twj, SSogd. tw(y)’z- ‘to pay (oft. © On the Sogd. 
1-umlaut and subsequent "Brechung", cf. GMS: $191. 

Pres.: SUBJ. 3sg. CSogd. twžt, Impf.: IND. 3sg. MSogd. twj; Fut.: IND. 3sg. CSogd. tw2Ztq’; Caus.: pres. 
SUBJ. 1sg. SSogd. twy’z’n, SUBJ. 3sg. SSogd. twy’z’t, SSogd. twy’z’ty, impf. IND. 3sg. SSogd. tw’z, 
fut. IND. 15р. SSogd. twy’z’m km 

*CHORESMIAN: twy ‘poll-tax’ (Benzing 1983: 617) 

*BACTRIAN: Go ‘to pay’ = S-W, Bact.: 227a 

*NWIR: NP töxtan/töz- ‘to pay a debt, return anything borrowed’ || (+ *ham-) NP 
andöxtan/andöz- ‘to collect a debt’ 

*MISC: Arm. (LW) tuZem ‘to expiate’, Arm. (LW) toyz ‘expiation, penalty’ 

0 The origin of the root *tauj’ is unknown: it could be identical to *tauf". 


*tauS ‘to (be) empty’ 

*AVESTAN: Y Ау. tuš- ‘to (be) empty’ = Liste: 26 

Pres. inch.: INJ. 3pl. YAv. tusan (V 3.32); Caus.: pres. IND. 3sg. YAv. (apa) taosaiieiti (Yt 10.48, Yt 
14.63, etc.) 


*MIDDLE PERSIAN: MMP twhyg, BMP twhyk /tuhig/ ‘empty’ = DMMPP: 330b 
*PARTHIAN: twsyg ‘empty’ = DMMPP: 331a 

*KHOTANESE: tussaa- ‘empty’ 

*NWIR: NP tuhi ‘empty’, Bal. tust/tus- ‘to suffocate’, tost/tos- ‘to extinguish’ 

*NEIR: ? Sh. (Baj.) tüy-/tüyd ‘to ache, hurt’, Rosh. tüy-/tüyd, Yzgh. toy-/toyd ‘to 
suffer’, Sariq. toy-, tawg- ‘to suffer, worry, be tormented’, Oss. I. tysszeg, Sh. tis,
```


## [2026-09-06T22:03:22.065Z] TOOL CALL #28: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '2985,3070p' CHEUNG.txt"
}
```


### [2026-09-06T22:03:22.112Z] TOOL RESULT

```
Pres. athem. red.: SUBJ. 3sg. YAv. cikaiiat (V 7.38, V 13.10, V 13.31, etc.), 3du. YAv. cikaiiato (F 48, F 
50, F 117), 3р1. YAv. "cikaiion (V 15.12, V 15.22, V 14.40), IMPV. 2sg. Y Av. ба... cici (? ба... “cicidi, 


28 *čai3 


F 238); Partic.: pres. desid. med. YAv. aißi.cicisomna- (N 63), Caus.: pres. OPT. med. 3pl. YAv. 
pairi.ākaiiaņta (Yt 10.122) 

MIDDLE PERSIAN: MMP cy- ‘to mourn, grieve, be troubled’, MMP kyn ‘hate, 
malice, revenge’ > DMMPP: 131b, 219b 

Pres.: IND. 3sg. MMP cyyd, IMPV. 2pl. cyyd; Partic.: pres. MMP cy’g 


*PARTHIAN: kyn ‘hate, malice, revenge? > DMMPP: 219b 

*NWIR: Oss. D. kine, kena ‘revenge’ 

*NEIR: NP kén ‘anger, wrath’ 

*SANSKRIT: cay ‘to punish, take revenge’ (RV) = EWAia I: 532 

0 The root *čař is usually not distinguished from *čai!, cf. Hoffmann — Forssman 
1996: 205; AiW: 441. However, the distinction as made by Kellens (et al.) is 
semantically justifiable. 

PIE *K"ei- ‘to collect a debt, take revenge, punish’ > LIV: 595 f. | Pok.: 636 

*IE COGNATES: Lyc. А ttiti, B kikiti ‘sentences (as payment, penalty)’, Gr. tivo ‘I 
pay, settle (a score)’, тіуорол ‘to cause to pay, punish, avenge’, лоуў ‘blood- 
money, punishment, revenge’ 

*REFERENCES: Abaev, Slovar’ I: 596; Nyberg II: 117b f.; Werba 1997: 182 f. 


* Kai? “о see, observe, perceive’ 

*AVESTAN: OAv. cailas-ca (n.) ‘attention, respect’ (Y 45.5) || (+ *ш-) ҮАУ. (Gsg.m.) 
vikaiehe ‘witness’ (F762, Klingenschmitt 1968: 246) 

*MIDDLE PERSIAN: (+ *ui-) MMP gwg’y, BMP gwk’dy /gugay/ ‘witness, testifier’ 
=> DMMPP: 166b 

*PARTHIAN: (+ *ui-) wyg’h ‘witness’  DMMPP: 352b 

*KHOTANESE: (+ *ui-) bye ‘witness’ 0 From *ui-käjäuäh ?, with loss of intervocalic 
*k, ЕП. shortening: *8í> *aj. = SGS: 336 

*SOGDIAN: (+ *pati-) ? SSogd. ptskwy- ‘to reply; explain’, Sogd. ptskwy ‘to 
(re)turn’, BSogd. ptskwy-, CSogd. pcwqy- ‘to say (to a superior), entreat’, MSogd. 
ptskwy ‘to speak, say’ || (+ *ui-) CSogd. wyc’w’, CSogd. wyc’wyt ‘martyr(s)’, 
CSogd. wyc'wqy' (f.) ‘witness, martyrdom’ 

(+ *pati-) Widely attested: Pres.: IND. 159. SSogd. ptskwy’m, MSogd. ptskwy’m (ВВВ: 40), dur. CSogd. 
pcqwy’msq, INJ. 1sg. SSogd. “ptskwyw, etc. 

*BACTRIAN: С1- ‘to see, consider’ || (+ *ui-) owyaAg ‘witness’, ovyaAgavo (pl.) 
‘witnesses’ = S-W, Bact.: 223b, 212b 

*NEIR: Oss. I. cyt, D. cite ‘honour, oun", I. kad, D. kadæ ‘fame; honour, hommage" 
|| (+ *ш-) Oss. D. igawun/igawd ‘to look sad’ 

*MISC: (+ *ui-) Arm. (LW) vkay ‘witness’ 

*SANSKRIT: cay ‘to perceive, to observe’ (RV+) 

*PIE *K"ei- ‘to observe, be observant’? > LIV: 377 f. | Pok.: 636 f. 

*IE COGNATES: Gr. тіо ‘I honour’, OCS ¿ajo ‘I expect, hope for’ 


*CaiH2 ? 29 
*REFERENCES: Abaev, Slovar’ I: 327, 565, 541; Werba 1997: 182 


*а1Н! ‘to sew’ 

*MIDDLE PERSIAN: (+ *upa-) MMP ’bzyn- ‘to sew, tailor = DMMPP: 18b 

(+ *upa-) Pres.: IND. 3р1. BMP ’bzynynd, IMPV. 2sg. MMP ’bzyn 

*PARTHIAN: Pth. ’bjyn’gr ‘tailor’ > DMMPP: 18b
```


## [2026-09-06T22:03:33.635Z] TOOL CALL #29: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### SYN leaf 850 (p.826)\"; awk 'BEGIN{RS=\"\\f\"} NR==851' SYN.txt | head -50"
}
```


## [2026-09-06T22:03:35.176Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### SYN leaf 1471 (p.1447)\"; awk 'BEGIN{RS=\"\\f\"} NR==1472' SYN.txt | head -30\necho \"##### KLN leaf for p.1447: ~ floor(1447/2)+12 = 735\"; for n in 735 736 737; do echo \"--- leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -c 300; echo; done"
}
```


### [2026-09-06T22:03:36.727Z] TOOL RESULT

```
##### SYN leaf 850 (p.826)
oor’ (below). Miihl.-Endz. 2085 f.
lett. mazlurigs, cpd. of maz ‘little’ and turigs ‘wealthy’ (11.51).
6. ChSl. ubogti, nebogtt, SCr. ubog, Boh, Mg Pol. ubogi, Russ. ubogyj, neg. epds. beside bogati% ‘rich’
ae ti] rich’, etc. ; ChSl. nist renders Grk. rrwxés more quently than ubogit, mostly as sb.
*  FTaybs
Digitized by Arya Samaj Foundation Chennai and eGangotri
SION PROPERTY, COMMERCE 733
‘poor person, beggar’ (Jagié, Entsteh- ungsgesch. 408; and so Russ. niscij mostly ‘beggar’), fr. *nistyo- or *niskyo-, precise analysis uncertain but based on a form cognate with Skt ni- ‘down’, ChSl. nizi ‘down’, etc: Zubaty, KZ 31.58 ff. Meillet, Etudes 2.380f. End- zelin, Z. sl. Ph. 13.78.
SCr. siromagan, cf. late (Serb.-)ChSl. siromacht, siraki ‘poor’, fr. ChSl. szrz ‘orphaned’ (2.75).
Boh. chudy = Pol. chudy ‘lean, wretched’, SCr. hud, Russ. chudoj ‘evil, bad’ (Russ. also ‘lean’), ChSl. chudi ‘small, insignificant’, etc. perh. : Skt. ksud- ‘crush, pound’, ksudra- ‘small’. Walde-P. 1.502. Berneker 405.
Pol. biedny, Russ. bednyj (= Boh. bidny, SCr. bijedan ‘wretched, miser- able’, ChSl. bédintt ‘maimed’) : ChSl. béda ‘necessity’, béditt ‘compel’, etc. Berneker 54. Walde-P. 2.185 f.
7. Skt. daridra-, lit. ‘wandering about, roving’, hence ‘poor’ and as sb. ‘beggar’ : daridra- intens. to dra- ‘run’. Walde-P. 1.795. Ublenbeck 121.
Skt. nir-dhana, neg. cpd. of dhana- ‘property, wealth’ (11.41).
Av. drigu-, driyu-, etym.? Walde-P. 1.821. Barth. 777 f.
Av. aSaéta-, neg. cpd. of Saéta- ‘wealth’ (11.42).
11.53 BEGGAR
Sartdvos, haxonépns Get bidagwa Lith. elgeta, ubagas pats N skal a olmusu- Lett. nabags, diedelnieks tant maor is ag Dane” tigger Scr ‘proafil matdigo, mendigane  ‘S¥- —‘téggare Boh. Zebra ; rae : 8 wedla Pol. zebrak : bee ‘begging’) te begger(e) Russ. nistij caro E beggar Skt. bhikgu-, daridra-, Hone” Du. —_bedelaar yacaka- Kerbara OHG  betalari Av ;
MHG betelere NHG betiler
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
784 SELECTED INDO-EUROPEAN SYNONYMS
?
The majority of the words for ‘beggar are from verbs for ‘ask for’ (18.35). But several are in origin opprobrious epithets (like NE bum), based in part upon certain physical or mental defects.
1. Grk. rrwxés : ret ‘timid, fearful, cowering’, rrwoow ‘cower, cringe’, rrjc0w “cower, crouch’, (these: zirrw ‘fall’, mérrwxa, etc.). Walde-P. 2.19. Boi- sacq 823.
NG fnridvos, fr. {nr ‘seek, ask for’ (11.31, 18.35).
NG dtaxonépns, fr. dtaxovd ‘serve’ (formerly also ‘beg’, now draxovebw), fr. dtaxovos ‘servant, deacon’.
2. Lat. mendicus (> Sp. mendigo), prob. orig. ‘defective, unsound’ : men- dum and menda ‘physical defect, fault’, W. man ‘spot, mark (on the body)’, Skt. minda- ‘physical defe
```


### [2026-09-06T22:03:38.599Z] TOOL RESULT

```
##### SYN leaf 1471 (p.1447)
lad, epd. of ym- with recipro- eal or refl. force and Ilad ‘kill, slay’, earlier ‘strike’ (4.76).
Br. en em ganna, refi. of kanna ‘strike’ (9.21).
4. Goth. weihan, ON vega, OF wigan (OHG pple. wigant, wikant), MHG wigen : Ir. fichim, etc. (above, 3).
ON berjask, refl. of berja ‘strike’ (9.21).
Dan. slaas, Sw. sldss, refl. of slaa, sld ‘strike’ (9.21); similarly also NHG sich schlagen.
ME kempe, Du. kampen (MLG kem- pen > Dan. kempe, Sw. kdmpa), NHG kémpfen (OE campian, OHG champfan, MHG kempfen, chiefly ‘fight a duel’),
Digitized by Arya Samaj Foundation Chennai and eGangotri
WARFARE 1371
derivs. of OE camp ‘battle’, MHG kampf, OHG campf ‘duel’, NHG kampf ‘battle’ (20.12).
OE feohtan, ME fehte, fihte, NE fight, Du. vechten (MLG > Sw. fakia; Dan. fegte poet. or arch.), OHG fehtan, MHG vehten, NHG fechten (now mostly ‘fence’), prob. as orig. ‘pull hair’ : Lat. pectere ‘comb’, Grk. wexréw ‘shear, clip’, wéxw ‘comb’, Lith. pests ‘pluck, pull’, refl. pestis ‘scuffle’ (cf. Leskien, Lit. Lesebuch p. 2, last 12 lines). Cf. Sp. pelear (above, 2) and NHG raufen ‘pluck, pull’, sich raufen ‘scuffle’. Walde- P. 2.17. Franck-v. W. 724.
OE winnan ‘labor, toil’ (9.13), also ‘strive, fight’.
5. Lith. kovoti : kova ‘battle’ (20.12) and following.
Lith. kautis, Lett. kauties, refl. of Lith. kauti, Lett. kaut ‘strike’ (Lett. kaut also ‘fight’ in NT, James 4.2) : ChSl. kovati, Russ. kovat’, etc. ‘forge’ (9.61), ON hoggva, OE héawan, etc. ‘strike, hew’ (9.22), Lat. ciidere ‘pound, beat’. Walde-P. 1.330. Walde-H. 1.300.
Lith. mustis, refl. of musti ‘strike’ (9.21).
6. ChSl. piréti se, refl. of pirétz ‘con- tend, dispute’ : pirati ‘wash’ (by beat- ing), Lith. pertt ‘bathe (by striking with a besom)’, Arm. hari, ehar ‘struck’, Av. parat- ‘fight’, parat-, Skt. prt- ‘battle’, OPers. partaram acc. sg. (NR a 47; ‘foe’ ’ or ‘battle’?). Walde-P. 2.42.
ChSl. bora, brati, SCr. boriti se : ON berja ‘strike’, refl. berjask ‘fight’ (above), Lat. ferire ‘strike’, etc. (9.21). Berne- ker 76.
SCr. biti se, Boh. béti se, Pol. bié sie, Russ. dit'sja, all refl. of the Slavic word for ‘strike’, ChSl. biti, etc. (9.21).
Boh. bojovati, deriv. of boj = ChSl. bojt ‘battle’ (this : bit?, above). Berne- ker 68.
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
‘ i Digitized by Arya Samaj Foundation Chennai and eGangotri
1372 SELECTED INDO-EUROPEAN SYNONYMS
Pol. walezyé : walka ‘fight, combat, struggle’, Boh. valka ‘war’ (20.13).
Russ. srazat'sja, refl. of srazat’ ‘throw down, fling down, smite’, cpd.. of razit’ ‘beat, smite’ beside raz ‘blow’, ChSl. u-razili ‘strike’, etc. (9.21).
Russ. drat'sja, refl. of drat’, ChSl. diratt ‘tear’ (9.28).
7. Skt. yudh-, Av. yud- : Grk. soutyy ‘fight, battle’, Lith. judéti ‘move, be in motion’, judinti ‘agitate, move, shake’, Pol. judzié ‘tempt, entice’, and Lat. tubére ‘command’ (as orig. ‘stir, rouse’). Walde-P. 1.208 f.
Av. parat-:ChSl. piréti se, ete. (above, 6).
20.12 BATTLE (sb.)
Grk. ypaxn Goth. wathjo orrosta, bardagi, vig, Lett. kauja
NG pexN ON
Lith. kova, mudis
##### KLN leaf for p.1447: ~ floor(1447/2)+12 = 735
--- leaf 735
derives  fr.  VL. sanguem.  See  prec.  word.  F.  de,  ‘of,  from’, comes  fr.  L.  de,  ‘from,  away  from’;  see  de-.  F. beeuf,  ‘ox,  bullock’,  comes  fr.  L.  bovem,  acc.  of bos;  see  bovine.
sang-froid,  n.,  presence  of  mind,  composure.  — F.,  fr.  MF.,  lit.  ‘cold 
--- leaf 736
 ‘soap’,  which  is a  Teut.  loan  word.  See  soap.
Derivative:  saponaceous-ness,  n.
Saponaria,  n.,  a  genus  of  plants  of  the  pink  fam¬ ily  (bot.)  —  ModL.,  fr.  ML.  saponarius,  ‘per¬ taining  to  soap',  fr.  L.  sapo,  gen.  saponis,  ‘soap’ (see  saponaceous  and  -
--- leaf 737
um,  fr.  sar- pere,  ‘to  cut  off,  lop,  trim’,  fr.  I.-E.  base  *srep-, *srp-,  ‘to  seize,  rob’,  whence  also  Gk.  ap7 xrh ‘sickle’,  dpud^av,  ‘to  snatch,  seize’,  dpTrdyr), ‘hook,  rake’.  See  harpy  and  -ment  and  cp.  assart, sarong,  n.,  the  chief  garment
```


## [2026-09-06T22:03:49.401Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SYN: PUNISHMENT concept ===\"\ngrep -n \"PUNISH\\|21\\.2[0-9] \" SYN.txt | head -20\necho \"=== SYN poinē / kaena ===\"\ngrep -n \"kaéna\\|kaena\\|kaēnā\\|rown\\|поіуђ\\|poena.*punishment\" SYN.txt | head -20"
}
```


### [2026-09-06T22:03:49.465Z] TOOL RESULT

```
=== SYN: PUNISHMENT concept ===
35446:21.11 Law (General = Lat. zis) 21.32 ConDEMN 21.12 Law (Special = Lat. lér) 21.83 Convict (vb.) 21.13 Lawsuit “21.84 Acquit 21.14 Lawyrr 21.35 Guiuty 21.15 Court 21.86 INNocENT 21.16 JupGE (vb.) 21.87 Prnauty, PUNISHMENT 21.162 Drcipr 21.38 Fine : 21.17 JuDGMENT 21.39 Prison, JAIL 21.18 JupGE (sb.) 21.41 Crm 21.21 PLAINTIFF 21.42 Murprr 21.22 DErenDANT 21.43 ADULTERY 21.23 Wrrness (sb.) 21.44 Rapr (sb.) 21.24 Swrar 21.45 Tuurt 21.25 OatH 21.46 ARson 21.31 AccusE 21.47 PrERroRY
35764:21.21 PLAINTIFF
35815:21.22 DEFENDANT
=== SYN poinē / kaena ===
1168:Lat. ripa ‘riverbank’ : Grk. épelrw, ‘throw down’, épelmia ‘ruins’, épirvar ‘abrupt cliffs’, ON rifa ‘tear to pieces’ (NE rive), etc. Development fr. ‘thrown down’ to ‘abrupt, steep’ as in Lat. abrup- tus and Grk. épimva:, then specialized to the (steep) ‘riverbank’. Hence It. ripa, riva, Fr. rive ��bank’ (but Sp. riba, Rum. ripa ‘slope, embankment’, not ‘river- bank’), and the derivs., which are used in wider sense of (‘bank-territory’, hence) ‘shore’, Fr. rivage, riviére, It. riviera, Sp. ribera, etc. Walde-P. 2.345. Ernout-M. 866. REW 7328. >
1970:3. Ir. cdo (gen. ciach), NIv. ceo, perh. : Ir. ciar ‘dark brown’, OF har ‘gray’ (NE hoar), ete. Walde-P. 1.360.
2304:NHG kerl. Perh. as ‘full-grown man’ : | séri- ‘woman, female’) Lat. pibés Grk. yépw, Skt. jarant- ‘old man’. | ‘adult’. Walde-P. 2.83. Ernout-M, Walde-P. 1.600. Falk-Torp 497. | 819f. Kluge-G. 296. 2.22 WOMAN Grk. yur Goth. qiné Lith. moteris, moteriskeé, NG yuvaixa ON kona Zmona Lat. mulier, féemina Dan.  kvinde Lett. steva It. donna Sw. kvinna ChSl. Zena Fr. femme OE cwene, wif, wifman SCr. Zena Sp. mujer ME —  quene, wife, woman Boh. Zena Rum. femeie NE woman Pol. kobieta Tr. ben, fracc Du. vroww Russ. ZenSéina Nir. bean OHG  wib, quena Skt.  jani-, nari-, stri- W. gwraig, benyw, dynes MHG wip Av. Jant-, ndtri-, strz- Br. maouez NHG frau, weib
2684:following the husband, hence in sense b); ‘taking the hand’ (either husband taking the hand of the bride, hence sense a, or conversely, hence sense b); ‘veiling’ (of the bride, hence orig. in sense b) ; ‘crown- ing’ (orig. used of the one performing the ceremony, then in mid. or refl. ‘get crowned’, of either party).
2688:NG orepav-dvopat, used with special reference to the ceremony, lit. ‘be crowned’ fr, orépavos ‘crown’ (wreaths are placed on the head of the bride and groom). Hence the similar use of Rum. cununa (fr. sb. cunund, Lat. corona ‘crown’) and other Balkan words. Pus- cariu 448. Sandfeld, Ling. balk. 35.
3760:Color words underlie some, as ‘brown’ in the Gme. words for ‘bear’ (3.73) and an IE word for ‘beaver’ (NE beaver, etc.); ‘gray’ in Lith. pelé ‘mouse’ (3.63) and prob. a widespread word for ‘hare’
4100:2. Goth. stiur ‘male calf’ (renders rév pocxov), ON stjorr (rare), OE stéor, OHG stior, all mostly ‘young ox’, MHG, NHG stier ‘bull’ (but dial. ‘ox’), NE steer ‘(young) ox’ (in U.S., where oxen are used for hauling, steer is still ‘young ox’, but otherwise and regularly in the packing industry steer is the grown cas- trated animal raised for beef, and oz is
4218:On vedr, Dan. vedder, Sw. vddur, OF weder (also ‘wether’), OHG widar (also ‘wether’), NHG widder : Goth. wiprus ‘lamb’, orig. ‘yearling’, like Lat. vitulus ‘calf’, etc. (3.24) : Grk. éros ‘year’, etc. Walde-P. 1.251. Shift from ‘lamb’ to the grown male, either ‘ram’ or ‘wether’.
4230:3.27. ‘Wether’. The castration of male sheep for fattening is an old and almost universal practice, and the ‘weth- er’ (understood here in the technical sense of NE wether ‘castrated sheep’) is the grown sheep par excellence. Hence the generic word for ‘sheep’, where it is not a distinctively feminine form, may be commonly applied to the ‘wether’ ; even though distinctive terms for the latter exist. Some of these are unfamil- iar to the layman (as NE wether except in bellwether). Conversely some words that were originally specific for ‘wether’ have become generic (as Fr. mouton) or through generic use have acquired a new specialization (as Fr. brebis ‘ ewe’, fr. Lat. vervex ‘wether’).
4631:4, OE colt, used for the young of a horse, ass, or even a camel, ME colte, NE colt: Sw. kull ‘brood, litter’, Sw. dial. kult ‘pig, overgrown boy’, Norw. kult ‘thick round shape, block’, Skt. gadi- ‘young ox’, Goth. kilpet ‘womb’, OE cild ‘child’, etc. Walde-P. 1.614. Falk-Torp 593, 430. Cf. ON hiann ‘block’ and ‘young bear’, NE cub: Norw. kubbe ‘block, stump’.
4967:the general Gmc. word : Lith. béras ‘brown’, OE Obriin ‘brown’, ete. Walde-P. 1.166. Falk-Torp 77.
4987:Gme. word, prob. : Skt. puccha- ‘tail’, Walde-P. 2.82. Falk-Torp 281. Feist 144. Cf. Sp. raposa and W. llwynog. ON refr (masc.), Dan. rev, Sw. rdv, perh. as ‘red’: ON jarpr ‘brown ’,OE eorp ‘darkish’, etc. Walde-P. 1.146. Falk-Torp 931. Hellquist 871.
5004:Skt. harina-, deriv. of hari- ‘reddish brown’.
5031:6. Skt. kapi- : kapila- ‘brownish, red- dish’, fr. ‘smoke-colored, Grk. xamvés, etc.? Walde-P. 1.379. Prob. source of Egypt. gephi, Grk. xios, xfBos, etc. Schrader, Reallex. 1.16.
5060:‘lean’, reflecting the popular notion that the elephant cannot bend its legs and sleeps leaning on a tree, a notion that is apparently referred to by Aristot. HA 498* and persisted in medieval and mod- ern times (cf. Sir Thomas Browne, Pseudodoxia 3.1). Briickner 500.
6113:Lat. armus mostly ‘shoulder, fore- quarter’ of animals, rarely ‘arm’ of men; Goth. arms, etc., general Gmc.; OPruss. armo ‘arm’; ChSl. ramo, rame, SCr. rame ‘shoulder’, Boh. rdmé, rameno, mostly ‘arm’, Pol. ramie, ‘shoulder, arm’; Skt. trma- ‘forequarter’ of an animal; Av. arama- in aramd-Sita- ‘thrown by the arm’; Arm. armuka ‘elbow’.
9383:Both the unripe pod and the grown seeds of the ‘bean’ are common articles of food. In several languages, instead of a comprehensive term like NE bean, there are two words, distinguished ac- cording to the variety. The commonest source is the notion of ‘swelling’.
10083:Pol. koronka or pl. koronki, dim. of korona (fr. Lat. coréna) ‘crown’ with de- velopment through ‘coronet, chaplet, rosary’, etc. Briickner 257.
10892:Bresette (> NG KATKETO; Dan. kaskel), dim. of casque ‘helmet’, fr. Sp. casco ‘skull, crown (of hat), helmet’, orig. ‘otsherd’, fr. cascar ‘break’. RIEW oo4I. Sp. sombrero, fr. sombra ‘shade’ (1.63). Sp. gorra, fr. Basque gorri ‘red’. REW 3822. Rum. példrie, of dub. orig., perh. by dissim. for *pdrdrie fr. pdr ‘hair’ (Lat. pilus). Tiktin 1110. 4. Ir. culpait (NIr. culpaid) ‘hood’, most common sort of head-covering, fr. lat. culcita ‘sack of feathers, cushion’. Vendryes, De hib. voc, 134. is, ce fr. Fr. toque a kind of ‘cap’, REW 86010, Basque?). Henry 265. Br. fain amillscheg 849, nault, Valé Ousenn, also kara- (cf. Er- its shape 7 ‘pparently, as named for
10979:Lith. nometas ‘headdress or veil of married women’ (cf. Lalis and NSB S.v.), epd. of nuo ‘down, from, away’ and deriv. of mesti ‘throw’, i.e. some- thing ‘thrown over and down’ from the head.
```


## [2026-09-06T22:03:51.313Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN 1966 punish entry ===\"\ngrep -n \"^punish,\" KLN_1966.txt\ngrep -n \"punish,  tr\" KLN_1966.txt | head\necho \"--- search 'punish' headword ---\"\ngrep -n \"^punish\\b\\|^punish \" KLN_1966.txt | head\necho \"=== KLN penal ===\"\ngrep -n \"^penal,\" KLN_1966.txt\necho \"=== KLN pain, n ===\"\ngrep -n \"^pain,  n\" KLN_1966.txt"
}
```


### [2026-09-06T22:03:51.413Z] TOOL RESULT

```
=== KLN 1966 punish entry ===
31018:Derivative:  Punic,  n.,  the  Punic  language, puniceous,  adj.,  purple  red.  —  L.  piiniceus,  fr.  Pu¬ nicus,  ‘Punic’.  See  prec.  word  and  -eous.  For sense  development  see  Phoenician, punish,  tr.  and  intr.  v.  —  ME.  punisshen,  fr.  MF.
--- search 'punish' headword ---
=== KLN penal ===
27946:penal,  adj.,  1)  pertaining  to  punishment;  2)  liable to  punishment.  —  ME.,  fr.  MF.  (=  F.)  penal, fr.  L.  poenalis,  ‘of  punishment’,  fr.  poena,  ‘pun¬ ishment’,  fr.  Gk.  rotvr,,  ‘bloodmoney,  fine, penalty,  punishment’,  which  stands  for  *qwoina- and  derives  fr.  I.-E.  base  *qwei-,  *q"’i-,  ‘to  res¬ pect,  consider,  honor,  pay,  expiate,  punish’, whence  also  Gk.  tieiv,  ‘to  esteem,  honor,  value’, TlfcTj,  ‘price,  worth,  honor,  esteem,  respect’, tIveiv,  ‘to  pay  a  price,  punish,  take  vengeance’, tIuk ;,  ‘payment,  punishment,  vengeance’,  OI. cinSti,  cayati,  ‘observes,  notices,  perceives",  cay- ate,  ‘revenges’,  Avestic  kdy-,  ‘to  requite,  be fined’,  kaena,  ‘punishment,  vengeance’,  OSlav. cena,  ‘honor,  price’,  ceniti,  ‘to  estimate,  value’, kajati  rg,  ‘to  repent’,  Lith.  kdina,  ‘value,  price’. Cp.  pain.  Cp.  also  impunity,  pine,  v.,  Poinae, punish,  subpoenal,  timocracy,  Timothy,  Tisi- phone,  xenotime.  Cp.  also  Pinnotheres,  synteresis. Derivatives: penal-ist,  n.,  penal-ize,  tr.  v.,  penal- iz-ation,  n.,  penal-ly,  adv.,  penalty  (q.v.)
=== KLN pain, n ===
```


## [2026-09-06T22:04:06.589Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== KLN Poinae ===\"; grep -n \"^Poinae\\|Poinae,\" KLN_1966.txt | head\necho \"=== total leaves KLN_1966 ===\"; awk 'BEGIN{RS=\"\\f\"} END{print NR}' KLN_1966.txt\necho \"=== leaf 891 ===\"; awk 'BEGIN{RS=\"\\f\"} NR==891' KLN_1966.txt | head -c 800; echo\necho \"=== leaf 880-885 sample ===\"; for n in 880 885; do echo \"--- $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' KLN_1966.txt | head -c 300; echo; done"
}
```


### [2026-09-06T22:04:08.347Z] TOOL RESULT

```
=== KLN Poinae ===
27946:penal,  adj.,  1)  pertaining  to  punishment;  2)  liable to  punishment.  —  ME.,  fr.  MF.  (=  F.)  penal, fr.  L.  poenalis,  ‘of  punishment’,  fr.  poena,  ‘pun¬ ishment’,  fr.  Gk.  rotvr,,  ‘bloodmoney,  fine, penalty,  punishment’,  which  stands  for  *qwoina- and  derives  fr.  I.-E.  base  *qwei-,  *q"’i-,  ‘to  res¬ pect,  consider,  honor,  pay,  expiate,  punish’, whence  also  Gk.  tieiv,  ‘to  esteem,  honor,  value’, TlfcTj,  ‘price,  worth,  honor,  esteem,  respect’, tIveiv,  ‘to  pay  a  price,  punish,  take  vengeance’, tIuk ;,  ‘payment,  punishment,  vengeance’,  OI. cinSti,  cayati,  ‘observes,  notices,  perceives",  cay- ate,  ‘revenges’,  Avestic  kdy-,  ‘to  requite,  be fined’,  kaena,  ‘punishment,  vengeance’,  OSlav. cena,  ‘honor,  price’,  ceniti,  ‘to  estimate,  value’, kajati  rg,  ‘to  repent’,  Lith.  kdina,  ‘value,  price’. Cp.  pain.  Cp.  also  impunity,  pine,  v.,  Poinae, punish,  subpoenal,  timocracy,  Timothy,  Tisi- phone,  xenotime.  Cp.  also  Pinnotheres,  synteresis. Derivatives: penal-ist,  n.,  penal-ize,  tr.  v.,  penal- iz-ation,  n.,  penal-ly,  adv.,  penalty  (q.v.)
29347:Poinae,  n.  pi.,  the  goddesses  of  vengeance  in Greek  mythology.  —  Gk.  IIoivaE,  pi.  of  txoivt), ‘bloodmoney,  fine,  penalty,  punishment’,  fr. I.-E.  base  *qwoina-,  whence  also  Avestic  kaena-, ‘vengeance,  punishment’,  OSlav.  cena ,  ‘price’, Lith.  kaina,  ‘price’.  L.  poena,  ‘punishment’,  is borrowed  fr,  Gk.  txoivt.  See  penal.
=== total leaves KLN_1966 ===
903
=== leaf 891 ===
  universolog- ist,  n.
univocal,  adj.,  having  one  meaning  only.  —  Form¬ ed  with  adj.  suff.  -al  fr.  Late  L.  univocus,  which is  compounded  of  L.  unus,  ‘one’,  and  vox,  gen. vocis,  ‘voice,  sound’.  See  uni-  and  vocal, unkempt,  adj.,  not  combed;  untidy.  —  Formed fr.  priv.  pref.  un-  and  ME.  kempt,  pp.  of  kemben, fr.  OE.  cemban,  ‘to  comb’,  which  stands  in  gra¬ dational  relationship  to  OE.  camb,  ‘comb’.  See comb.
unless,  conj.  —  Fr.  earlier  onlesse,  ontesse  that, i.e.  ‘on  less  that’.  Cp.  F.  a  moins  que,  ‘unless’, lit.  ‘on  less  that’,  and  see  on  and  less, unmeet,  adj.,  not  meet;  unsuitable.  —  ME.  un- mete,  fr.  OE.  unm&te,  ‘not  meet’.  See  priv.  pref. un-  and  m
=== leaf 880-885 sample ===
--- 880
� I.-E.  base  *tro-g-,  *tri-g-  is  an  enlargement  of base  *ter-,  *tr-,  ‘to  go  through,  pass  beyond’. See  term  and  cp.  words  there  referred  to. Derivatives:  trout-er,  n.,  trout-y,  adj. trouvaille,  n.,  a  lucky  find,  windfall.  —  F.,  fr.
trouver,  ‘to  find’.  
--- 885
of  two',  fr.  did,  ‘two’.
Derivatives:  twigg-ed,  twigg-en,  twigg-y,  adjs. twilight,  n.  —  ME.,  fr.  MFIem.  twilicht,  a  var.  of twe(e)-licht,  corresponding  to  MLG.  twelicht (see  F.  J.  Bense,  Dictionary  of  the  Low-Dutch Element  in  the  English  Vocabulary,  p.  516).
```


## [2026-09-06T22:04:21.747Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"--- page-number-looking lines ---\"\ngrep -n \"^ *1[45][0-9][0-9] *$\" KLN_1966.txt | head -20\necho \"--- leaf index of 'penal,' 29347 Poinae ---\"\npython3 - <<'EOF'\nimport io\nt=open('/home/sfmqrb/git/rishe/data/verification/sources/refs/KLN_1966.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor target,name in [(27946,'penal'),(29347,'Poinae'),(29337,'poet'),(31018,'punish'),(27948,'penalty')]:\n    upto='\\n'.join(lines[:target])\n    print(name,'leaf',upto.count('\\f'))\nEOF"
}
```


### [2026-09-06T22:04:23.671Z] TOOL RESULT

```
--- page-number-looking lines ---
34164:1401
34193:1402
34241:1405
34468:1413
34538:1416
34661:1422
34721:1424
34722:1425
34760:1426
34761:1427
34814:1428
35054:1439
35080:1440
35081:1441
35136:1442
35161:1443
35193:1445
35205:1444
35251:1446
35289:1448
--- leaf index of 'penal,' 29347 Poinae ---
penal leaf 614
Poinae leaf 644
poet leaf 644
punish leaf 678
penalty leaf 614
```


## [2026-09-06T22:04:28.961Z] TOOL CALL #35: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nimport re\nlines=open('KLN_1966.txt',encoding='utf-8',errors='replace').read().split('\\n')\nnums={}\nfor i,l in enumerate(lines):\n    s=l.strip()\n    if re.fullmatch(r'1?\\d{1,4}',s):\n        try: nums[i]=int(s)\n        except: pass\nkeys=sorted(nums)\nimport bisect\ndef near(ln):\n    j=bisect.bisect_left(keys,ln)\n    out=[]\n    for k in keys[max(0,j-2):j+2]:\n        out.append((k,nums[k]))\n    return out\nfor target,name in [(27946,'penal'),(29347,'Poinae'),(29337,'poet'),(31018,'punish'),(26944,'pain v')]:\n    print(name, near(target))\nEOF"
}
```


### [2026-09-06T22:04:30.840Z] TOOL RESULT

```
penal [(27931, 1150), (27932, 1131), (28003, 1153), (28047, 1154)]
Poinae [(29245, 1200), (29300, 1206), (29377, 1209), (29405, 1210)]
poet [(29245, 1200), (29300, 1206), (29377, 1209), (29405, 1210)]
punish [(30793, 1264), (31006, 1273), (31069, 1274), (31070, 1275)]
pain v [(26809, 1107), (26861, 1108), (26948, 1113), (26982, 1114)]
```


## [2026-09-06T22:04:40.916Z] TOOL CALL #36: Bash

```json
{
 "command": "ls site/pages/289.jpg 2>/dev/null; pdftoppm -f 289 -l 289 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg289 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/"
}
```


### [2026-09-06T22:04:43.330Z] TOOL RESULT

```
site/pages/289.jpg
total 100080
drwx------ 3 sfmqrb sfmqrb     4096 Sep  6 18:04 .
drwx------ 4 sfmqrb sfmqrb     4096 Sep  6 16:32 ..
-rw-rw-r-- 1 sfmqrb sfmqrb   533122 Sep  6 17:21 afm41_a.png
-rw-rw-r-- 1 sfmqrb sfmqrb   508509 Sep  6 17:21 afm41_b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   969829 Sep  6 17:21 afm41.png
-rw-rw-r-- 1 sfmqrb sfmqrb  1322100 Sep  6 17:20 afm46.png
-rw-rw-r-- 1 sfmqrb sfmqrb   416305 Sep  6 17:20 afm46_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb      638 Sep  6 17:59 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    76489 Sep  6 17:24 bqt1237_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   362419 Sep  6 17:50 bqt1583_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb   456331 Sep  6 16:54 bqt1594_foot.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2824 Sep  6 16:59 bqt83_head.png
-rw-rw-r-- 1 sfmqrb sfmqrb   703015 Sep  6 17:50 bqt_fn4.png
-rw-rw-r-- 1 sfmqrb sfmqrb   299015 Sep  6 17:50 bqt_fn.png
-rw-rw-r-- 1 sfmqrb sfmqrb   325427 Sep  6 17:50 bqt_n552.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   315487 Sep  6 17:50 bqt_n553.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   330101 Sep  6 17:50 bqt_n554.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   560485 Sep  6 17:53 bqtv2_650_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   541712 Sep  6 17:53 bqtv2_651_s.png
-rw-rw-r-- 1 sfmqrb sfmqrb   729454 Sep  6 17:53 bqtv2_n650.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   702551 Sep  6 17:53 bqtv2_n651.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   100817 Sep  6 17:36 bqt_v3_111.png
-rw-rw-r-- 1 sfmqrb sfmqrb   110820 Sep  6 17:36 bqt_v3_112.png
-rw-rw-r-- 1 sfmqrb sfmqrb    91526 Sep  6 16:59 bqt_v3_83.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64531 Sep  6 16:53 build261.py
-rw-rw-r-- 1 sfmqrb sfmqrb    60498 Sep  6 17:11 build269.py
-rw-rw-r-- 1 sfmqrb sfmqrb    97300 Sep  6 17:16 build270.py
-rw-rw-r-- 1 sfmqrb sfmqrb    52615 Sep  6 17:36 build275.py
-rw-rw-r-- 1 sfmqrb sfmqrb    74145 Sep  6 17:43 build278.py
-rw-rw-r-- 1 sfmqrb sfmqrb    72342 Sep  6 17:58 build283.py
-rw-rw-r-- 1 sfmqrb sfmqrb     5043 Sep  6 17:05 c1.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3501 Sep  6 17:05 c2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    56424 Sep  6 17:05 c3.png
-rw-rw-r-- 1 sfmqrb sfmqrb    78058 Sep  6 17:05 c4.png
-rw-rw-r-- 1 sfmqrb sfmqrb 60831599 Sep  6 18:01 cad_k.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  2530822 Sep  6 18:01 cad_k.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    37980 Sep  6 17:16 c_av.png
-rw-rw-r-- 1 sfmqrb sfmqrb    29703 Sep  6 17:16 c_cros.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1174 Sep  6 17:16 c_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    95615 Sep  6 16:39 coord_pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4560 Sep  6 16:39 crop_ak2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4014 Sep  6 16:39 crop_ak.png
-rw-rw-r-- 1 sfmqrb sfmqrb    25373 Sep  6 16:42 crop_alk.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24852 Sep  6 17:04 crop_fr269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    43238 Sep  6 16:55 crop_germ269.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51654 Sep  6 17:04 crop_gk269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     2585 Sep  6 17:05 crop_gk271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    64142 Sep  6 17:02 crop_gr267.png
-rw-rw-r-- 1 sfmqrb sfmqrb     6411 Sep  6 16:39 crop_gr.png
-rw-rw-r-- 1 sfmqrb sfmqrb    23559 Sep  6 16:42 crop_kohul.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59386 Sep  6 16:39 crop_lat2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    51357 Sep  6 16:55 crop_latin269.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4761 Sep  6 16:39 crop_lat.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3974 Sep  6 16:37 crop_me2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3300 Sep  6 16:37 crop_me.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10236 Sep  6 16:39 crop_op2.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4935 Sep  6 16:37 crop_op.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5599 Sep  6 16:37 crop_pers.png
-rw-rw-r-- 1 sfmqrb sfmqrb    22007 Sep  6 17:10 crop_sak.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5110 Sep  6 17:10 crop_sax.png
-rw-rw-r-- 1 sfmqrb sfmqrb     4854 Sep  6 17:10 crop_shekar.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1249 Sep  6 17:05 crop_sirish.png
-rw-rw-r-- 1 sfmqrb sfmqrb    30419 Sep  6 17:02 crop_skt267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    10043 Sep  6 16:58 crop_slav.png
-rw-rw-r-- 1 sfmqrb sfmqrb    24463 Sep  6 16:58 crop_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb  2144625 Sep  6 17:55 dmmpp.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    31044 Sep  6 17:50 e0.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17126 Sep  6 17:54 e1.json
-rw-rw-r-- 1 sfmqrb sfmqrb    18004 Sep  6 17:56 e2.json
-rw-rw-r-- 1 sfmqrb sfmqrb  5301166 Sep  6 17:01 ediv.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb  1773345 Sep  6 17:01 ediv.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  1845041 Sep  6 18:04 gharib.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  3698758 Sep  6 17:50 IEC_full_djvu.txt
-rw-rw-r-- 1 sfmqrb sfmqrb      228 Sep  6 16:34 jscheck.js
-rw-rw-r-- 1 sfmqrb sfmqrb     4265 Sep  6 17:53 kapi_script.png
-rw-rw-r-- 1 sfmqrb sfmqrb     1433 Sep  6 16:45 merge262.py
-rw-rw-r-- 1 sfmqrb sfmqrb    63035 Sep  6 16:56 mk265.py
-rw-rw-r-- 1 sfmqrb sfmqrb    73111 Sep  6 17:13 mk267.py
-rw-rw-r-- 1 sfmqrb sfmqrb    71564 Sep  6 17:08 mk268.py
-rw-rw-r-- 1 sfmqrb sfmqrb    41609 Sep  6 17:31 mk274.py
-rw-rw-r-- 1 sfmqrb sfmqrb    51778 Sep  6 17:32 mk276.py
-rw-rw-r-- 1 sfmqrb sfmqrb    46494 Sep  6 17:52 mk279.py
-rw-rw-r-- 1 sfmqrb sfmqrb    16605 Sep  6 17:54 mk280b.py
-rw-rw-r-- 1 sfmqrb sfmqrb    17667 Sep  6 17:56 mk280c.py
-rw-rw-r-- 1 sfmqrb sfmqrb    43177 Sep  6 17:50 mk280.py
-rw-rw-r-- 1 sfmqrb sfmqrb    58322 Sep  6 17:51 mk282.py
-rw-rw-r-- 1 sfmqrb sfmqrb  8373934 Sep  6 17:00 mk.pdf
-rw-rw-r-- 1 sfmqrb sfmqrb   378445 Sep  6 17:00 mk.txt
-rw-rw-r-- 1 sfmqrb sfmqrb    11601 Sep  6 16:42 p262-g01.json
-rw-rw-r-- 1 sfmqrb sfmqrb    10625 Sep  6 16:43 p262-g02.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19393 Sep  6 16:46 p262-g03.json
-rw-rw-r-- 1 sfmqrb sfmqrb    19959 Sep  6 16:44 p262-g04.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12063 Sep  6 16:43 p262-g05.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12051 Sep  6 16:44 p262-g06.json
-rw-rw-r-- 1 sfmqrb sfmqrb    12737 Sep  6 16:44 p262-g07.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17259 Sep  6 16:46 p262-g08.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17820 Sep  6 16:53 p262-g09.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17855 Sep  6 16:45 p262-g10.json
-rw-rw-r-- 1 sfmqrb sfmqrb    14983 Sep  6 16:44 p262-g11.json
-rw-rw-r-- 1 sfmqrb sfmqrb    25352 Sep  6 16:46 p262-g12.json
-rw-rw-r-- 1 sfmqrb sfmqrb    17745 Sep  6 16:44 p262-g13.json
-rw-rw-r-- 1 sfmqrb sfmqrb   105748 Sep  6 16:39 p263hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     5565 Sep  6 17:22 p275_krei_empty.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53703 Sep  6 17:22 p275_pahlavi.png
-rw-rw-r-- 1 sfmqrb sfmqrb     7106 Sep  6 17:34 p279_greek.png
-rw-rw-r-- 1 sfmqrb sfmqrb    12970 Sep  6 17:34 p279_word.png
-rw-rw-r-- 1 sfmqrb sfmqrb     3647 Sep  6 17:34 p279_xsaeta.png
-rw-rw-r-- 1 sfmqrb sfmqrb   130651 Sep  6 17:48 p283_arrow.png
drwxrwxr-x 2 sfmqrb sfmqrb     4096 Sep  6 18:02 p284
-rw-rw-r-- 1 sfmqrb sfmqrb    43108 Sep  6 17:51 p284_e0_fa.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89734 Sep  6 17:51 p284_e0.png
-rw-rw-r-- 1 sfmqrb sfmqrb    59639 Sep  6 17:48 p284_e2b.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106502 Sep  6 17:48 p284_e2.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66777 Sep  6 16:42 pg261.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84660 Sep  6 16:39 pg262.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71156 Sep  6 16:38 pg263.png
-rw-rw-r-- 1 sfmqrb sfmqrb    92930 Sep  6 16:37 pg264hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    57862 Sep  6 16:35 pg264.png
-rw-rw-r-- 1 sfmqrb sfmqrb    13324 Sep  6 16:57 pg265_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb    86370 Sep  6 16:57 pg265.png
-rw-rw-r-- 1 sfmqrb sfmqrb    79922 Sep  6 16:42 pg266.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70622 Sep  6 16:56 pg267.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69592 Sep  6 16:52 pg268.png
-rw-rw-r-- 1 sfmqrb sfmqrb    71754 Sep  6 16:55 pg269.png
-rw-rw-r-- 1 sfmqrb sfmqrb   122626 Sep  6 16:58 pg270hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    87489 Sep  6 16:55 pg270.png
-rw-rw-r-- 1 sfmqrb sfmqrb   115300 Sep  6 17:05 pg271hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66696 Sep  6 17:04 pg271.png
-rw-rw-r-- 1 sfmqrb sfmqrb    68566 Sep  6 16:58 pg272.png
-rw-rw-r-- 1 sfmqrb sfmqrb    66829 Sep  6 17:28 pg273_crop.png
-rw-rw-r-- 1 sfmqrb sfmqrb   157304 Sep  6 17:10 pg273hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70615 Sep  6 17:27 pg273.png
-rw-rw-r-- 1 sfmqrb sfmqrb    65586 Sep  6 17:18 pg274.png
-rw-rw-r-- 1 sfmqrb sfmqrb    80338 Sep  6 17:21 pg275.png
-rw-rw-r-- 1 sfmqrb sfmqrb    76740 Sep  6 17:15 pg276.png
-rw-rw-r-- 1 sfmqrb sfmqrb    44171 Sep  6 17:16 pg277.png
-rw-rw-r-- 1 sfmqrb sfmqrb    89267 Sep  6 17:26 pg278.png
-rw-rw-r-- 1 sfmqrb sfmqrb   168655 Sep  6 17:34 pg279hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    75777 Sep  6 17:34 pg279.png
-rw-rw-r-- 1 sfmqrb sfmqrb    82065 Sep  6 17:34 pg280.png
-rw-rw-r-- 1 sfmqrb sfmqrb    61535 Sep  6 17:39 pg281.png
-rw-rw-r-- 1 sfmqrb sfmqrb    70575 Sep  6 17:34 pg282.png
-rw-rw-r-- 1 sfmqrb sfmqrb    74784 Sep  6 17:47 pg283.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:50 pg284hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    81024 Sep  6 17:51 pg284.png
-rw-rw-r-- 1 sfmqrb sfmqrb   144566 Sep  6 17:49 pg284_top.png
-rw-rw-r-- 1 sfmqrb sfmqrb    84487 Sep  6 17:53 pg285.png
-rw-rw-r-- 1 sfmqrb sfmqrb   106264 Sep  6 17:53 pg286hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb    69883 Sep  6 17:52 pg286.png
-rw-rw-r-- 1 sfmqrb sfmqrb    72442 Sep  6 17:59 pg287.png
-rw-rw-r-- 1 sfmqrb sfmqrb    53847 Sep  6 17:58 pg288.png
-rw-rw-r-- 1 sfmqrb sfmqrb    90831 Sep  6 18:04 pg289.png
```


## [2026-09-06T22:04:46.317Z] TOOL CALL #37: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg289.png"
}
```


### [2026-09-06T22:04:46.910Z] TOOL RESULT

```

```


## [2026-09-06T22:04:46.906Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-06T22:05:02.201Z] TOOL CALL #38: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && python3 -c \"\nfrom PIL import Image\nim=Image.open('pg289.png')\nprint(im.size)\nim.crop((820,980,1330,1060)).resize((1530,240)).save('p289_labibi.png')\n\""
}
```


### [2026-09-06T22:05:04.225Z] TOOL RESULT

```
(1700, 2200)
```


## [2026-09-06T22:05:06.434Z] TOOL CALL #39: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289_labibi.png"
}
```


### [2026-09-06T22:05:06.454Z] TOOL RESULT

```

```


## [2026-09-06T22:05:18.138Z] TOOL CALL #40: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in $(seq 228 240); do echo \"### NR=$i :: $(awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | grep -oE \"^[0-9]{3}|[0-9]{3} OLD PERSIAN|LEXICON\" | head -2 | tr '\\n' ' ')\"; done"
}
```


### [2026-09-06T22:05:19.889Z] TOOL RESULT

```
### NR=228 :: LEXICON 
### NR=229 :: 204 
### NR=230 :: LEXICON 
### NR=231 :: 206 
### NR=232 :: 
### NR=233 :: 
### NR=234 :: 
### NR=235 :: 
### NR=236 :: 
### NR=237 :: 
### NR=238 :: 
### NR=239 :: 
### NR=240 ::
```


## [2026-09-06T22:05:22.335Z] TOOL CALL #41: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor i in $(seq 231 240); do echo \"======== NR=$i\"; awk -v n=$i 'BEGIN{RS=\"\\f\"} NR==n' KNT.txt | head -c 400; echo; done"
}
```


### [2026-09-06T22:05:23.907Z] TOOL RESULT

```
======== NR=231
am. rak-qa-an, АКК. ra-ga-’, Gk. ‘Payys, now Rai near Teheran. kagä nsf. DB 2.71f. Ваду absf. DB 8.2.
гада- sb. ‘wagon’ (570.11, $148.11), see urata-.
Irad- vb. ‘leave’: Skt. rah-, pres. rahati 'sep- arates, leaves’, to pIE *regh-, Av. razah- 5isola- tion’, or to pIE *redh-, NPers. (through Ars. РЫ.) rähäð ‘he gets free from’; Fr. Müller, WZKM 11.208-4; Foy, K
======== NR=232
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.I
======== NR=233

======== NR=234

======== NR=235

======== NR=236

======== NR=237

======== NR=238

======== NR=239

======== NR=240
```


## [2026-09-06T22:05:32.260Z] TOOL CALL #42: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' KNT.txt\necho \"--- grep spa / parisp / pari-sp ---\"\ngrep -n \"spā\\|spa- vb\\|parisp\\|pari-sp\\|'throw away'\\|throw away\" KNT.txt | head -20\necho \"--- grep 'sā-' style ---\"\ngrep -n \"^sā-\\|^sä-\\|^sa- vb\\|sā- vb\\|'pile up'\\|pile up\" KNT.txt | head -20\necho \"--- tail of leaf 232 ---\"\nawk 'BEGIN{RS=\"\\f\"} NR==232' KNT.txt | tail -c 2500"
}
```


### [2026-09-06T22:05:34.558Z] TOOL RESULT

```
leaves: 232
--- grep spa / parisp / pari-sp ---
2036:Sparda, Mudráyà, Küsa, Yaun, Gadard, Kar- mand; nt. duSiyárà, vispā, gastá.
4691:5 nah*ta : uid : M'bra : тат: pdtw : hacá : vispā : дазїй : Ша : imam : tya : akundm : má : vijanátu : mà : vinàttayátiy
--- grep 'sā-' style ---
--- tail of leaf 232 ---
1); -vā .. -vä ‘either... or...’: Av. và, Skt. và, pIE *ue, ef. Lt. -ve.  z$apa-ü rawca-paíi-a DB 1.20. hya-»à DB 4.68. imai-vä DB 4.71, 78, 77. yadi- vä DNb 25, 29.
vaina- present stem of vb. ‘see (mid.) seem’: Av. vaéna-, NPers. bindd, Skt. véda ‘knows’, vinddte ‘finds’, Lt. videt ‘sees’, videtur ‘seems’; pAr. *uaid- na-, plr. *yaina- ($69, 588.1, $130, $210.III; Reichelt, Aw. Ер. $157). See also Vidafarnah-. vainümiy lst sg. (4226.1) DNb 36, 36f, 39, 40. avaina imf. DB 2.76, 90; DNa 32. vainataiy mid. as pass. (8235.1) DNb 2; XPa 16. vaináhy 2d sg. subj. ($37, $222.11, $227.1) DB 4.70, 73, 77; DNb 29. vaindtiy subj. ($222.11) DS} 5°. vainātaiy subj. mid. as pass. ($222.П) DNb 35.
vau- adj. ‘good’ ($11, §153.1); nt. as sb. ‘the good, (religious) goodness’: Av. nsm. vaphus, nsn. vohu, Skt. nsm. vásuş, nsn. vdsu, pIE *yesu-; in Dérayavau-, Vaumisa-, Vahauka-, Vahyazdata-.
Va'umisa- sb. ‘Vaumisa’, a Persian officer of Darius: Elam. ma-u-mi-i8-8a, АКК. ti-mi-is-st, Gk. (Plutarch) Rutens; cpd. of vatu- and mifra- ‘friend’ (849c, $78, $148.ILD): ‘Friend of the Good’ §160.- Ib; cf. MB Gr. $51). Vaumisa nsm. DB 2.49, 51, 62. Vaumisam asm. DB 2.53, 58.
vaz$- vb. ‘grow’, see (Луах${та-.
Waj- vb. ‘be strong’: Skt. vaj-, бјаз- ‘strength’, Av. aof
```


## [2026-09-06T22:06:11.673Z] TOOL CALL #43: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"parisp\\|parasp\\|pari-sp\" NYB_vol2_glossary.txt | head\necho \"--- NYB kēn ---\"; grep -n \"^kēn\\|^kēn \" NYB_vol2_glossary.txt | head\necho \"--- NYB tōxtan/tōz ---\"; grep -n \"tōxt\\|tōz\\|toxt\" NYB_vol2_glossary.txt | head\necho \"--- NYB wizīdan/čīdan ---\"; grep -n \"^čīdan\\|^wizīdan\\|^čin\\|^wizī\" NYB_vol2_glossary.txt | head"
}
```


### [2026-09-06T22:06:11.761Z] TOOL RESULT

```
2953:pargän [plg?n'] "wall 935 (read, with Dh.: ... pahnai i damik; pērāmēn Harburz ~ H. is a wall all around it). — < *pari- küna- ‘that which is thrown up all around’ from pari + kan- ‘to throw’, v. apakandan; cf parisp.
2959:parisp [plsp'], with indef. art. —-& [~-’y] wall 11421. — OIr *pari-spä- from pari + Av. (1615 sq.) !spá- ‘to throw’, cf par- gan; MPrthPrs prysp; Arm. lw. parisp.
5340:Ispä: parisp
6094:prysp: parisp
--- NYB kēn ---
--- NYB tōxtan/tōz ---
3793:tóxtan [twhtn'] čož- [twe-] to pay a debt, a fine; to give back, return anything (borrowed): ken tēžēt he will take his revenge 4522, — Cf (Paz.) men hom Ādīnē i xin-xaGh u xin-06é u xin i haft-anbadaa pa farzanda Gēžom (Adino for Adēnāi, xin for ken, anbädaa faulty reading for óbüda = öbätak v. I, XV n. 2) ‘I am Adönäi, desiring revenge and taking revenge, and I shall revenge myself upon the children during seven genera- tions’ SGV XIV, 5-7, reproducing Ex. 20: 5. — MPrth twj- ‘to pay, to atone for’, Ghilain 63; MPrs twzysn ‘penalty, ex- piation'; Paz. 0óxtan 002-; NP toxtan toz-, kin-toz ‘bellicose, one who foments dissension and lawsuits’. — V. also tēg.
3812:tugrän, or turgän with the same Prth. metathesis as in tyrg = tirg < tigra- ‘swift’ (A-H ITI) or in the Arm. lw. turž ‘penalty’ < *tužra- (v. tog, toxtan). Prs tgwi'n shows the inverse Sogdian spelling -gw- for -wg- (Henning, BSOS IX, 1938, 548—550), thus representing tugrān, whence tiran according to the common SW phonetic rule. For Turdn, and designating the same country, Yàqult (3,554) quotes the form Tuwärän, which evidently goes back to *tugārān. (NB: no attention has been paid here to the Hast Turkistani names Qayodpot, Sogd twyry, MPrth twr’n Sh (S), MPrs ch?r twgrystn, ete.; I have no competence to meddle in the learned discussions inspired by Pelliot’s article Tokharien et Koutchéen, JA 224 1934, 23-106, and carried on between Bailey: BSOS VIII, 1936, 884-917, TPhS 1947 (1948), 126—153 (cf also BSOAS XIII, 1950, 403 sg.) — and Henning: BSOS IX, 1938, 545-571, A. M., N.S. I, 1949, 159-162. This much may be stated: all the twgrn etc. dealt with in the present article are quite distinct from the Tokharians: Tuxärän and Tuxā- ristän, whose capital was Balkh. V. also Tarn 515-519].
5692:we: täyitan trw-: tarvenitan tšyndyft: tisnak&h twj-: toxtan twrn: Tur tybhrg: dépahr tyrg: Turan tyrs-: tarsitan
6830:00, Ou, tu: td Oaxtan, 00ž-: toxtan tua, tva: tuvan tug: togéh
--- NYB wizīdan/čīdan ---
```


## [2026-09-06T22:06:13.720Z] TOOL CALL #44: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad && curl -s -L --max-time 120 \"https://archive.org/download/oldpers/oldpers_djvu.txt\" -o kent_full.txt && ls -la kent_full.txt && grep -n \"throw away\\|pile up\" kent_full.txt | head -20"
}
```


### [2026-09-06T22:06:21.776Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 944060 Sep  6 18:06 kent_full.txt
29100:*lud-, Av. spa- ‘throw, throw away, set down’,
```


## [2026-09-06T22:06:32.037Z] TOOL CALL #45: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nsed -n '29060,29140p' kent_full.txt"
}
```


### [2026-09-06T22:06:32.080Z] TOOL RESULT

```
from the OP form *visadana-: Med. vispa- ‘all’ + 
Med. zana- ‘man, human being’ ($9.11, §88, $90). 
uspazananim gpf. DNa 10Ї; DSe 9f; DZc 5. 


LEXICON 200 


Vistaspa- sb. ‘Hystaspes’, father of Darius: 
Elam. mi-iš-da-aš-ba, Akk. wufia-as-pa, Gk. 
‘Loraonns. Prior element višta- perhaps pte. of 
(Av.) vaés- ‘come in ready for action’ (Bthl. AiW 
1326), Skt. vi$- ‘enter’, second part aspa- ‘horse’: 
‘Having ready horses’ (§9.IT, §9.n2, $93, $161.ITa, 
Lg. 21.55-8; current etymology unlikely: višta- 
pte. of vi- + had- ‘sit, settle down’, Skt. vi-sad- 
‘sink, despond’, giving meaning ‘Having spiritless 
horses’, which would be an ill-omened name; and 
this ptc. would be OP *vrsasta- or the equivalent 
of Skt. visanna-, not vista-; also wrongly Hüsing, 
OLZ 15.537-41, who takes prior part as a reduced 
form of vahišta- ‘best. Vistaspa nsm. DSf 13; 
ХРЇ 17f, 20. У: азра ($22) DB 1.4; 2.93, 94, 
97; 3.4, 7; DBa 5. Уг азрат asm. DSf 57Р. 
Vstaspam (822) DB 3.2, 3. Vistaspahyà gsm. 
DPa 4f; DPb; DPe 4; DPh 2; DNa 12f; DSc; 
D$d 2; DSf 7; DSg 2; DSi 2; DS} 1°; D8m 2°; 
DSy 2f; DZb 5; DZe 6; DE 19f; DH 2; ХР? 18; 
AIc 14; Wa 5f; Wb 7t; We 8f; Wd 8f. Vstaspa- 
hyà (822) DB 12f, 4; DBa 3, 5; DSa 2; DSb 9f; 
DSe 117; DSk 2; Аза 3; A’Sc 0°; A?Ha 4°; A?Pa 
18f, 19. 


Vispauzati- sb. ‘Vishpauzati’, a town in 
Parthia; Elam. mi-iš-ba-u-za-ti-iš. — Vis|paluz(a]- 
. &snef. DB 2.95. 


sã- vb. ‘erect, build’: probably from pIE 
*lud-, Av. spa- ‘throw, throw away, set down’, 
Ars. РЫ. pari-sp ‘wall’ (800; Bv. Gr. $113, ef. 
Коше, Burgbau 49-50; wrongly Bv. BSLP 30.1.- 
66-7). 

fra- + să- ‘erect, build’: frasah|ya] s-aor. pass. 
($218.1, §220) DSf 27 (1st sg. act. }тазаһа[т| is 
possible, as proposed by Kent, JAOS 53.15, and 
approved by Schaeder, Ung. Jrb. 15.562.n2). 


Saka- adj. ‘Scythian’ ($116, $143.TIT) ; masc. 
sg. as sb., ‘Seythia’ as province or district; masc. 
pl. also as name of the province, often with modi- 
fiers (cf. JNES 2.304-5; for other discussion, cf. 
A. Hermann, AfOF, Betheft 1, Festschrift Oppen- 
heim 157-64 [1933], and J. Kluge, Klio, Веће 
41, Saka-Studien [1939]). Elam. sa-ak-ga, АКК. 
gi-mi(r)-ri, Gk. Хкобтѕ, Zeta. See also Saka-. 
Probably ‘dog’ in good sense, = ‘guardian of the 
flocks’, pIE *kyon-, Med. отака ‘dog’ (Herod. 
1.110), ef. Van Windekens, Beitr. z. Namen- 
forschung 1.98-102. | 

(1) ‘Scythian’: Saka пет. DBk 2. Saka npm. 


as пет. ($56.III) DN xv; A?P 14, 15, 24. Saká 
npm. DB 5.31. ака apm. DB 5.22", 25. Sa- 
kaibiš ipm. for abpm. (§252F) DPh 5; DH 4. 

(2) ‘Scythians’, a province of the Persian Em- 
pire: байа npm. DPe 18; DNa 25, 251, 28; DSe 
24^, 25^; XPh 26 bis. 

(3) ‘Scythia’: Saka nsm. DB 1.16f; 2.8. 


Saka- sb. ‘Scythia’, fem. of preceding, as sb. 
Saküm asf. DB 5.211.
```


## [2026-09-06T22:06:48.051Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ngrep -n \"LEXICON [0-9]*\\|^2[01][0-9] OLD PERSIAN\\|OLD PERSIAN$\" kent_full.txt | sed -n '1,400p' | awk -F: '$1>28500 && $1<29600'"
}
```


### [2026-09-06T22:06:50.232Z] TOOL RESULT

```
28527:LEXICON | 205 
28806:LEXICON 
29065:LEXICON 200 
29337:LEXICON
```


## [2026-09-06T22:07:04.718Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nfor L in 222 223 224 225; do curl -s -L --max-time 60 \"https://archive.org/download/oldpers/page/n${L}_w800.jpg\" -o kent_n${L}.jpg; echo \"$L: $(file -b kent_n${L}.jpg)\"; done"
}
```


### [2026-09-06T22:07:14.845Z] TOOL RESULT

```
222: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 827x1252, components 1
223: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 926x1248, components 1
224: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 842x1244, components 1
225: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 936x1267, components 1
```


## [2026-09-06T22:07:17.211Z] TOOL CALL #48: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/kent_n224.jpg"
}
```


### [2026-09-06T22:07:17.235Z] TOOL RESULT

```

```


## [2026-09-06T22:07:35.968Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BQT v1 انجیدن ===\"; grep -n \"انجیدن\" BQT_v1_pages.txt | head\necho \"=== BQT v1 پرچین ===\"; grep -n \"پرچین\" BQT_v1_pages.txt | head\necho \"=== BQT v2 چیدن ===\"; grep -n \"چیدن\" BQT_v2_pages.txt | head\necho \"=== BQT v2 توزیدن/توختن ===\"; grep -n \"توزیدن\\|توختن\" BQT_v2_pages.txt | head\necho \"=== BQT v3 گزیدن ===\"; grep -n \"گزیدن\" incoming/BQT/BQT_v3_pages.txt | head -5"
}
```


### [2026-09-06T22:07:36.069Z] TOOL RESULT

```
=== BQT v1 انجیدن ===
=== BQT v1 پرچین ===
=== BQT v2 چیدن ===
4577: ‫‪YY‬‬                                                                                             ‫چیدن‪‎‬‬
4766:                        ‫نون » مخفف چیدن باشد ‪3.‬‬
5611: ‫چیدن ه بکر جیم ظرسی‪.‬‬                  ‫جشم‬                                                            ‫آویزید ‪۰‬‬
6136:                            ‫‪ = ۵‬چیدن (م‪ = ).‬چییدن («‪.‬م‪ ).‬ورك ‪ :‬اسفا ‪۱‬‬
7171:  ‫چیزی‌را نکیزوبن دکه درحم مالیده باشند ‪٩‬‏ ‪.‬‬      ‫است ‪ -‬وبرچیدن مرغ‌دانه را آززمین ‪ -‬و کشتی‬
7871: ‫‪۶(8‬چیدن) ‏ تپرانی ‪021016‬؛ گرفتن میوه از درخت ‪ -‬گزبدن » انتخاب کردن ‪ -‬دانه از‬
7873:  ‫باط و متاع ‪ -‬گرفتن ناخن وستردن موی ‪« :‬نگوبی که‌دوبدن و برهنه بودن و ناخن ناچیدن‬
7947:  ‫‪ ۸‬اوستا‪ ۱ 42۷01 . ۷819290-‬حزو‬          ‫‪ - ۷‬یز بمعنی چیدن (هم) است ‪.‬‬
13893:     ‫پیچیدنآواز گروایند درکوه وحمام کن‬                   ‫و ساز واغمه باشد ‪ .‬جه خنیا گرخو اننده وساز الم‬
17726:‫و واو ک»نابه ازدرهم پیچیدن ‪ -‬و ینهان کردن‪-‬‬
=== BQT v2 توزیدن/توختن ===
=== BQT v3 گزیدن ===
8209:است از - ۷2۲ ۵ بمعنی برگزیدن » برتری دادن و گروبدن 1 وثیربه بعنی برگزیده, ‎Rwy‏
15938:گردد و کرمکی است شبیه ‎Sete‏ جهت ضع فگزیدن نتواند » ومگس ریزه »وبهمی‌الفوغاء
29554:’ کوشه کرفتن و دوری گزیدن را 55 گفته‌اند -
44431:را یز کویند ۴ - وامر بگزیدن هم هست یعنی
44461:‏۴ - اسم قاعل مرخم ‎Dy.‏ گزیدن .
```


## [2026-09-06T22:07:41.379Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\np='BQT_v2_pages.txt'\nt=open(p,encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\n# find leaf index for line 7871\nupto='\\n'.join(lines[:7871])\nleaf=upto.count('\\f')\nprint('leaf(0-based)=',leaf,'-> printed approx',leaf+543)\nprint('\\n'.join(lines[7860:7960]))\nEOF"
}
```


### [2026-09-06T22:07:43.126Z] TOOL RESULT

```
leaf(0-based)= 134 -> printed approx 677
                   ‫وز ولات خراح بردارد ‪.‬‬                                        ‫گر شود چیرو تاج بردارد‬
          ‫‪.‬‬        ‫نظامی کنجوی‪.‬ه کنجینه ‪1‬‬

                                   ‫باین معنی مصحف*تبر» ‪.‬ا لغتی است از آن ‪ .‬رك تمر ‪.‬‬                              ‫‪- ۴‬‬

  ‫در اردو چیره ‪۵۳‬آ[ (نواری که دور دستار بندند) ‪.‬‬                       ‫‪-‬‬    ‫©‬           ‫رکه ‪ :‬چیر ‪.‬‬                  ‫‪۴‬‬

 ‫اوستا‬   ‫‪YT‬‏‬       ‫ب رگز ‪.‬دن) «منای ‪۰‬‬                    ‫(چدن ‪۰‬‬      ‫جیلان ‪ -‬بقتح سوم » بهلوی ‪natîc‬‏‬

 ‫‪ . ۷ - 8880‬حندی باستانی ‪1C. 1-60‬‏ بلوچی ‪8401C‬‏ اسفا ‪۷ : ۱‬ص ‪۸۲۱۰۲۹۳٤‬‏ گیلکی‬
 ‫‪۶(8‬چیدن) ‏ تپرانی ‪021016‬؛ گرفتن میوه از درخت ‪ -‬گزبدن » انتخاب کردن ‪ -‬دانه از‬
  ‫زمین برداشتن مرغ و فروبردن ‪ -‬زدن شاخه هایکیاه‪ -‬بر بالای هم گذاشتن چیزی ‪ -‬گستردن‬
  ‫باط و متاع ‪ -‬گرفتن ناخن وستردن موی ‪« :‬نگوبی که‌دوبدن و برهنه بودن و ناخن ناچیدن‬
                         ‫قابوسنامه چاپ لقمسی ‪.‌ 6۵۱‬‬                   ‫( درمراسم‌حج) ‪«<¢‬‬     ‫تابیراستن چراست‬                      ‫و موی‬

  ‫)‪ .‬حاصل مصدرچیره‪.‬‬       ‫( مصدری‬          ‫ی‬           ‫بفتح سوم » از ‪ :‬چیرء (چیرکه) ‪+‬‬           ‫¬‬   ‫چیری‬                 ‫‪#‬‬

 ‫؛ غالب شدن ‪,‬طفر‬          ‫بد«ییر کے “‪٤٤‬‏ «مناس ‪ « 012۲66 ,۲۲ :۰۷۲‬میا ‪۲۳۱‬‬                                             ‫بهلوی ‪۷‬‬
                                                                                                    ‫‪۰‬‬           ‫ره‬   ‫عافتن ‪ ۰‬رك‪:‬‬


  ‫‪ #‬چیز ‪ -‬بپلوی ‪« 056‬منای ‪ »۰۷۲:۷‬پ=ارسی باستان ‪( 160516‬شینی) الزا‪.>0)1‬‬
 ‫افغانی ع ‪ « 2‬هوبشمان ‪ »۷۵4‬ورك‪ :‬یبر که ‪ 0‬و اسفا ‪٣ :۱‬ص‏ ‪» ۲۲۱‬گیلکی ‪ 216‬؛ شیشی»‬
 ‫هرچه موجود باشدهربودنی» امور ظاهری وباطنی‪ «:‬وچیزهاء پنهانی والهی همیشه غالب‌تر وقوی‌نر‬
                             ‫بود از چیزهاء طبیمی‌و ظاهری‪ ».‬ک«شف المحجوب سجتالی ‪.*۲۷‬‬

                                                                                                    ‫بقه از صفحهٌ ‪۵۷٩‬‏‬

  ‫حمداله مستوفی درترهة القلوب‌مقالهً‪( ۳‬چاپ لیترانج‪۱۳۳۱‬‬                              ‫نیرگ‪۰٤‬‏ ابوستی‪ .‬مندهش ‪۰‬‬
 ‫ولی‌درشاهنامة فردوسی ناسخان بغلط «خنجت »ر‪ :‬فهر ست ولف»‬                            ‫وة‬    ‫‪۷۸-۱۲- ۸-۵۸‬چصت‬                                ‫ص‬
 ‫ود وآشکده معروف «آز رکشتپ» در کار‬                                ‫ضط کرده‌اند ‪ :‬این در باچه دراظر زرتشتان مقدس‬
   ‫‪ ۰‬مصحف دییخ» («‪.‬م‪).‬‬         ‫ظ‬     ‫‪"۱‬‬            ‫‪.‬‬    ‫اشنکه درمتن بمعنی کوه گرفته ‪ ۰‬خطاس‬                  ‫ِ‬   ‫آن قرار داشت‬


 ‫‪ #‬چهلم ‪ -‬بکراولوضم سوم از‪ :‬اچمه(لب‪۳‬س‪-‬وندعددی)؛ عددتر تببی‌چهل»مر تبفچپل‪.‬‬
                                                                           ‫چهل‌منار ‪ -‬رك ‪ :‬چل مناره ‪۰‬‬                ‫‪+‬‬
  ‫یود‬                                                                                            ‫مه‬
           ‫نکی است ‪.‬‬
                   ‫درخاله آویزند گ‪.‬وبند ر‬               ‫ابن کلمه ازتوابع است وبمعنی‌چیزی کم واند که‬
 ‫چیلان ‪ -‬با ثالی مجپول بکرویزلنان»‬
‫عناب را گونند‪ ,‬وآن‌مبوه‌ای‌باشدشبیه مالس ‪e‬‏‬
                                                         ‫چزو = بر وزن یکو خار بست‬
‫آولات وادواتی که اآزهن سازند همچو زرفین‬                 ‫کلانرا گویند که خار های خود را مانند قر‬
‫در ‪.‬وزنجیر و حاقپای کوچك و براق زین ولجام‬                                                         ‫اندازد ‪.‬‬
                   ‫اسب )‪ (۲‬و رکاب وامثالآن ‪.‬‬
                                                         ‫چیزه بوڈ ‪ -‬بابایابجد (‪ )۱‬و ذال‬
‫جلا نه= بائالی مجهول بروزن دیوانه»‬
‫بمعنی چیلان باشد که عناب است وآنرا سنجد‬                 ‫چه چیزه بوذ کرمیب را کویند که شتا فرین‬
                              ‫کر دان هگموبند ‪.‬‬                                                    ‫باشد ‪٩‬‏‬

‫چن = بروزن سدن » شهرست معروف‬                             ‫چیستان ‪ - ۲‬بروزن سیتان ‪ .‬بمعنی‬
    ‫ومشهور ‪٩‬‏ ‪ -‬و به‌عنیشکنج هم مده است‬                   ‫پرسیدن باشد و آنکراولغبزهنمد ‪ ۰‬بوعربی‬
                                                          ‫آزمده‬
                                                              ‫ماهیت نی‬         ‫اغلوطه خوانند ‪ --‬وبمطی‬
‫کنابه‌ازییر‬        ‫نودن۔‬
                       ‫کبر‬
                         ‫انفبرا‬
                              ‫چی‬
                                                                                                ‫است ‪.# ۴‬‬
‫شدن ‪ -‬و روی درهم کشیدن و در شب شدن‬
                                                                       ‫میم ؛‬    ‫وزن‬   ‫گا‬    ‫جع‬
                                          ‫باشد ‪3 .‬‬       ‫برده مانئدی‬


‫چینو د ‪ » 8‬بروزن میرود» پل صراطرا‬                        ‫باشد که آترا از چوبهای باريك سازند و ازپیش‬
                                   ‫ات ‪3:‬‬    ‫(‪ )۱‬یکی وت‬                         ‫(‪ )۱‬چك‪ :‬بابا ‪.‬‬

‫آن‪ ,‬غالب لغزها با‬         ‫‪+‬‬   ‫یت‬   ‫از ‪:‬‬    ‫‪۴‬‬         ‫ظ‪ ,‬ازبرساخته های فرفه‌آنر کوان ‪.‬‬      ‫‪۱‬‬
                                     ‫«چیت‌آن ‏‪ ٩۲...‬آغاز گردد (ترکب‌کلمه باضمیر» رك‪ :‬زینهار)‪:‬‬
        ‫«لبیبی؟‪.‬‬
                     ‫سری‪.‬‬     ‫گوی دانش ز موبدان‬               ‫اگر این چیتان تو بکشابی‬
  ‫‪ - ۴‬باین معنی از دساتیر است‪ « .‬فرهنك دساتیر ‪۳4۲٩‬‏ وصحیح بدین معنی «چیستی»‬
  ‫‪ - ۴‬ازترکی «چیغ» نوعی حصیز که‌ازلی‌بافته ودرجدارهای خیمه‌اصب‬           ‫(ه‪.‬م‪ ).‬است ‪۰‬‬

                                ‫کننده توعی برده حصری که در مدخل خیمه آویزند‪« .‬جفتای ‪۹۳‬‬
‫‪su = 8‬اص‪.ahRN‬‏ درختی ازتبرء عاابها ‪ . 56602010018113‬دارای میوه هابیاست که‬
                                            ‫«گللاب ‪ , ۰۳۲۰‬رك ‪ :‬چیلانه ‪.‬‬
                                                                      ‫بعنوان ملن‌بکار میرود‪ .‬ک‬
  ‫چنتان» دررهلوی ( ‪ )۳8052)0۵‬ت«اوادیا ‪ )/02)560۵ ۲۰ : ۹۵۱‬م«سینا‬                             ‫‪۱‬‬
 ‫چبنعقيده محققان از نام سللهٌ بادثاهان ]‪ 1*51‬اخذشده «‪. 965‬ص‪< ۵61۴۵۳1-0015 .‬‬                          ‫‪۲‬‬
  ‫چين (دراصطلاح عام) شامل‌چین خاص ‪ ,‬تکسرتان باسین کيانك و تبت است ‪ .‬چين خاس‌بمساحت‬
  ‫کلو هتر هربعم و دارای ‪ 664‬میلبون سکنه‌استو محدود ابسمتنجوری» مفولستان؛‬                           ‫‪۰‬‬
 ‫تبت» امپرانوری‌هند وهندوچن فرانسه‪ .‬باشغعت آن‌نانکن ‪niknaN‬‏ و ثپرهای عمد آن‌بی مينك‬
   ‫‪( Pel -‬یکن) « هانگ‌چئو ‪l€C-‬‏ ‪ . gnaH‬فوچئوناع» ‪uF -‬‏ ‪.‬اوچانگ‪,[-80200‬‬                                ‫‪8‬‏‬
  ‫‏‪ , 2۵02 ja‬چنگه‌تو ‪U‬‏ ‪ , gneC -‬خانگهای ‪îahgnahS‬‏ « تن تن ‪nist‬‏ ‪neiT -‬‬
                     ‫وهان کئو ‪€K‬‏ ‪ 1211 -‬است ‪.‬رك د‪:‬ائرة المعارف اعلام ‪. 60 :‬‬
  ‫‪ ۸‬اوستا‪ ۱ 42۷01 . ۷819290-‬حزو‬          ‫‪ - ۷‬یز بمعنی چیدن (هم) است ‪.‬‬
   ‫‪۸۷‬‬               ‫تیه‬
   ‫==‬                                                                           ‫چمته‬


‫گویند ‪ - ۴‬وهرمرتبه ازکل باشدکه بردبوار‬      ‫گویند بلغت زد و یازند (‪ » )۱‬وباین معنی با‬
                             ‫‪.‬‬   ‫گذارند ‪۴‬‬   ‫خای نفطه دار ورای بینقطه هم آمده است که‬


‫چینه دان = بادالابجدبروزن بی‌زبان‪,‬‬                                        ‫خینور باشد ‪.‬‬
                ‫حیثه ‪ = ۲‬بروزن زینه ؛ داه مرغان را | حوصلة مرغاتراکویند ‪#. ۴‬‬
```


## [2026-09-06T22:08:02.371Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 382 383 384; do echo \"======== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -c 1200; echo; done"
}
```


### [2026-09-06T22:08:03.922Z] TOOL RESULT

```
======== leaf 382
یوتانی۱ وممنیآن‌بفارسی « سنگه زاییدن آمان
کن » باشد . وآن دانه ایست ساهرنگه بمقداو
جوژبوا. بغایت املی‌وصلب ودشوارشکن: وچون
بجنبانند مفز آن در درون وی صدا کند وآنرا
بشیرازی « کن ابلیس » خوانند نم کاف فارسی
ونون ۰ یعنی خایةٌ شبطان و بعربی حجرالولادة
گوبند . چه هرگاه در زیر زنان آستن دود
کنند زود بزایند و اکر باشیرزنان سح قکنند
وقدری پشم را بدان بیالایند و زنی‌ که نمی زاید
بوفت جماع بخود بر گیرد آستن قود.. گو یف
چونآنرا دردست گیرند وبا کسی مخاصمت کنند
برآ نکس غالب‌آیند .
| ناغاطسی - باغننقطه داربالفکفیده
وطای حطی مضموم بسین بی‌نقطه زده ۰ بونالی
سنکی باشد که چون آنرا بآب بسابند رنگی
مانند خون از آن برآید و با شیر زنان درچشم
چکانند ورم چشم و بیاری آب آمدن از چشم
را�
======== leaf 383
اتبارش
که پر کرده باشد - و بمعنی پرنسمت و با نعست
هم اجه ات ۵
نبادش! -بروزن‌افزایش. پر کردنی‌را
کوبند . و آن چیزی باشد که جوف درون
چیزبرا بان پر کنند. وأنرا بعربی حشوخوانند.
انبار "سیر وزن دمساز » خومات و رفیق
و همتا را گویند . "
نباشت ۱0 بروزن برداشت ۳ ماضی
انباشتن است ععنی کر و ممل و گرداند ۰
۶ ۵۸۱ ه ۳ > ۳
انباشتی ۲۷ " سبروزن برداشتن,بسنی
پر کردن و مملو گردانیدن و آنبار نمودن باشد .
افیا ۴ - باغی تقطم‌دار .دوزن‌را گوبند
دیگری‌را انباغ باشد .8
اثبان باد - بکر نون و با بای ابجد
بروزن می‌دان‌کار. مردم فربه - و بیکاره وهیجکاره
را گوند ۰
برمی آورند .
اثبر ب بنتح اول وضم الث وسکون‌انی
و رای فرشت » التی باشد از آهن که ز رکران
و مسکران طلا و مس تفته دا بدان گیرند ,وبه
عربی کلوب خو
======== leaf 384
سب ی ٩5‏
| بودن بروزن افزودن, بربالای حم
چیدن باشد .
اثبوذن س با زال قطه‌دار بروزن‌اندودن,
بمعنی اسل‌کاینات و آفرینش باشد .
ایوس » بروزن اضوی , تخمی باشد
بنظر آحده است ۰
| بو سیدن - بانستانی مجپول بروزن
افزوییدن , بمعنی پدید آمدن و ظاهر شدن -
و موجود گردبدن باشد .
اثبوه » بروزن اندره » بمعنی‌فرورختن
دبوار باشد - و بمعتی پر و عملو و بسیار نیز
امده خواه بساری مردم و خواه چیزی دیگر
باشد - و دم قصبه است در بالای کوهی از
مضافات دیلمان .
اثبوی « بر وزن بدبوی » بعنی بوی
کردن باشد ٩‏ - و چیزی‌را نیز گوبند که ببوی
آهده و کندیده باشد - و مطلق‌بوی رانیز گونشد
خواه بوی خوب و خواه بوی بد باشد - و بوی
کننده را نیز کوش که فاعل باشد - و اهر باین
معنی هم هست عنی بوی کن و سوی ۰
) بو ی (۱) » بکر�
```


## [2026-09-06T22:08:11.425Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 385 386 387 388; do echo \"======== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"انج\\|نجید\\|انجی\" | head -20; done"
}
```


### [2026-09-06T22:08:13.349Z] TOOL RESULT

```
======== leaf 385
1:انج - بفتح اول وسکون ثانی و جیم»
22:اصل‌آلانجدان خوانند ۴ ؛وبعضی گویند تسنای‌است
24:انجر لك - بکس ثاك وفتح رای فرخت
39:انجخ ۱ سا که جچن و شکنج روی واندام عاشد .
======== leaf 386
5:انجمن! - ینم اك و قح میم وسکون
20:بحنی انجسا است که نوعی از سرخ مرد باشد
23:وهعنی انجوخ اس که چن و شکن روی واندام
27:انجیره
30:) نجیدن ؟ - بروزن رنجیدن , بمعنی
35:انجیفه ه بروژ نگندیده , بلغفت‌بونانی
46:و آنرا جوی‌انجیل بلام
48:انجیر ۸3 ه ناممیوءاست درهندوستان
50:شمشیر زن» بمعنی سوراخ کردن باشد, چه‌انجیر
52:انجیره * بروزنزتجیره ۰ بمعنی‌آنجیر
======== leaf 387
1:انجین
34:۱ رك : انجیر . ۴ -رك : انجبدن. ۴ - پهلوی ۵۳۵( بسیار, عدد مبهم ) «اونوالا
40:: انجیل متی , انجیل‌مرقس . انجیل لوفا
======== leaf 388
11:) ند ام ۴ « بروزن انجام , معروفت که
```


## [2026-09-06T22:08:16.713Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==386' BQT_v1_pages.txt | sed -n '25,60p'\necho \"----- footnotes leaf 386/387 -----\"\nawk 'BEGIN{RS=\"\\f\"} NR==386' BQT_v1_pages.txt | tail -20\necho \"===== leaf 387 head =====\"\nawk 'BEGIN{RS=\"\\f\"} NR==387' BQT_v1_pages.txt | sed -n '25,45p'"
}
```


### [2026-09-06T22:08:19.124Z] TOOL RESULT

```
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
----- footnotes leaf 386/387 -----
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
===== leaf 387 head =====
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
```


## [2026-09-06T22:08:28.328Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 598 599 600 601 602; do echo \"======== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | grep -n \"پرچ\\|رچین\\|پرچین\" | head -10; done"
}
```


### [2026-09-06T22:08:29.751Z] TOOL RESULT

```
======== leaf 598
======== leaf 599
======== leaf 600
======== leaf 601
======== leaf 602
```


## [2026-09-06T22:08:32.457Z] TOOL CALL #55: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 596 600 604 608; do echo \"======== leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' BQT_v1_pages.txt | head -8; done"
}
```


### [2026-09-06T22:08:34.168Z] TOOL RESULT

```
======== leaf 596
۳۷۸ <
و او را پخته خوار حم کویند..
لته گای » بناولرکان بالف کشیده
و بواو زده» داروی چنداست که درآب جوشانند
خوانتد .3
یخحج - بفتح اول وسکون ثانی و جیم
فارسی٩‏ .۰ اش بخت و بخش ۳ توب
۳ ۷
======== leaf 600
در بای فارسی
بر - فتح اول و سکون ثانی» هحروف
است که بال و پر باشد و عربان رش‌خوانند ۷
واز سر کتف نا سرانگشتانرانیز گوشد - وروشنی
وشماع و پرتو را هم کنته‌اند؟ - و دامن و کناره
حرچیز باشد همچو پ رکلاءو کنار؛ کلاه»ویرببابان
و پربینی هم بنظر آمده است که دامن بپابان
وکناره بینی باشد و ترك کلاهرا تین کفته‌اند -
======== leaf 604
پر یی ۱ ۰ بر وژن پروین ؛ حساری
باشد که از خاروخللاشه وشاخ درختان بر دورباغ
وفالیز و کشت زارساز ند وچوبهای‌سر‌تیزوخاربرا
نیز گوبند که برسرهای دبوارها اصب کنند -
و محک کردن چیزی باشد درچیزی مانندمیخی
که برتخثه زنند ودبالةٌآن را ازجاب‌دیگر خم
رهند ومحکم کنشد 5 ۰
فرداش ؛ بمعنی خصومت ر جنگ و جدال باشد
======== leaf 608
-_۳۸۳
و ثالكث بتحنالی رسیده و واو مفتوح بنون ودال
ابجد زده , بىني صریح باشد که در مقابل رمز
وایماست . ۱
رس ح_بفتح اول بروزن‌دری, پردمرا
کویند که بر روی چیز ها پوشند و از جاها
آویزند . *
پرسا! - بضم اول وسکون ثانی و سین
```


## [2026-09-06T22:08:41.247Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==604' BQT_v1_pages.txt | tail -14\necho \"=== leaf 596/608 page nums check: 378 and 383 ===\""
}
```


### [2026-09-06T22:08:42.831Z] TOOL RESULT

```
فردوسی طوسي. «لفت نامه»
قه ازصفحهٌ ۳۷۸
وبوم‌هاست . «پرچم بقلم پورداود. سالئامة ابران جاوبدان سال۱۳۲۷». آفای دهضدا در لفت نامه
ذبل‌برچم؛ پس از نقل فول مولف برهان دریاب «کاو بحری؟ نوشته‌اند: ظاهراً مراد رشنه‌های‌دهان
کار بحری, وال (بالن) باشد که درزبر سنان علم تا رمح و باب ‌گردن اسب می‌بستند . وعجب این
است که کلم پرچم بدانسا نکه در فارسی علاقة لیزه وئیز ریشه‌های مصفاة و پالونه گونه‌ای درطرف
دهان نوعی وال ( بالن ) را نامیده‌اند ؛ در زبان فراسه یز کلمةٌ 18008 همانطور بپردو معنی
آمده است :
دارد فرسش بدیین شانی پرچم دم شیر آسمانی . خافالی‌شروالی.
کاوی نشان دهند دراين قلزم نگون لیکن نه پرچم است مر لورا؛ نه عتبر است.
اثیراخسيکتی.
مجازاً موی کیسو «رشیدی» وکا کل «برهانن»: ۱
بیکی دست‌می خالص ایمان نوشتد بیکی دست د کر پرچم کافر کیرند.
مولوی بلخی رومي -
=== leaf 596/608 page nums check: 378 and 383 ===
```


## [2026-09-06T22:08:50.068Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== ARY latin index: kin / cidan / gozidan / tuxtan ===\"\ngrep -n -i \"KIN\\b\\|KINE\\b\\|CIDAN\\|GOZIDAN\\|GUZIDAN\\|TUXTAN\\|TOXTAN\\|PARCIN\" incoming/ARY/ARY_latin_index_pages.txt | head -20\necho \"=== ARY persian: کین ===\"\ngrep -n \"کین\\b\\|کینه\" incoming/ARY/ARY_pages.txt | head -10"
}
```


### [2026-09-06T22:08:50.128Z] TOOL RESULT

```
=== ARY latin index: kin / cidan / gozidan / tuxtan ===
626:cate 32.9044 gl 2 yhy DLL! 3I JS Gate 1 Ky SS gt Akin Slates hy
5133:MACKENZIE: (SKIN) 133 HOLD FRISIAN) 88 3.3
6261:wet : ZIN, KIN. (OLD FRISIAN) S523
6264:BARNHART: (cum 166] KIN GERMAN) ist
6270:we bu oly KIN DUTCH) ache
9137:BARNHART: (KIN) 565 (OLD HIGH GERMAN) pS giST
9141:ONIONS: (KIN) 505 CENNAN, CYN j
9142:SKEAT: (KIN) 322 KIN ENGLISH) gundS3i
9447:KVINDE, KONE —«(DANISH) S\ail2 KIN ARMENIAN) «gi 5)
9475:ZIN, KIN. (OLD FRISIAN) oS 3,3 ZANVA HAVESTAN) glogl
9483:KIN (DUTCH) gle GENA, GENAE :(LATIN) oY |
11150:| OLD IRISH) 6 5439! SNAZ, SNACIDAN (PAHLAVI) 5 4
12139:HUL DANISH) Sails KUN, QING, KIN (KURDISH) 52,5
12140:HAL (SWEDISH) $48 yo KUN, KIN BALUCHI gp yh
12262:ER-KININT:(OLD PRUSSIAN) Sey, KIN KURDISH) 53,5
15599:Att rly Got 5 jai (KUN, KIN 2 ph (QING, KUN 3352 SUKUN 215 58g) "05" ge sl so jly LE -1
=== ARY persian: کین ===
985:کین‌تر همین کار را می‌کردند. مثلاً در داستان جنگ تروا آمده است که آقاممنون
2006:اوستایی (4887/400):: دنکن آلناتی کین (05724۸40 27101 0ا0):
2105:اسلد یکین ((نم ویو رم ۰ ۰ |15 ,299300 7۶00
2387:۸۸ ایسلند یکین (7ف/012/۸۲ایی5 صتم): 10
2597:ایسلند یکین (۷010۸۸ی5 صام): برهمی (/لف80/78(1): وا نی ها
2814:۸13۸1 ,۸13813۸۵ انگلیسی کین (5#لا2۷0 صا): 8۲05
3021:انگلیس یکین (بل5/ا0108(/0): ۷۷۸۹ ,6ل8ن1 9 (ه8) :22/مق هط
3155:ایسلند یکین ((7۵ مهم صا۵): ۷۸۸
3212:۹ فریزی کین (زنلعلم ضام: 880001۸ گالی (ب3لتلا0۸): ۸۸
3327:آلمان یکین (30م 0294زا اه رشاید) 3119 ماه
```


## [2026-09-06T22:08:52.793Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC (Mann) kʷei / qwei ===\"\ngrep -n \"^k[uw]ei\\|^qwei\\|poinē\\|poinä\\|kaenā\" IEC.txt | head -20\necho \"=== WLD band3 register kʷei ===\"\ngrep -n \"kaena\\|poinē\\|kʷei\" WLD_band3.txt | head -10\necho \"=== SYN 21.37 PENALTY ===\"\ngrep -n \"21.37\\|PENALTY, PUNISHMENT\\|Prnauty\" SYN.txt | head"
}
```


### [2026-09-06T22:08:52.872Z] TOOL RESULT

```
=== IEC (Mann) kʷei / qwei ===
=== WLD band3 register kʷei ===
=== SYN 21.37 PENALTY ===
35446:21.11 Law (General = Lat. zis) 21.32 ConDEMN 21.12 Law (Special = Lat. lér) 21.83 Convict (vb.) 21.13 Lawsuit “21.84 Acquit 21.14 Lawyrr 21.35 Guiuty 21.15 Court 21.86 INNocENT 21.16 JupGE (vb.) 21.87 Prnauty, PUNISHMENT 21.162 Drcipr 21.38 Fine : 21.17 JuDGMENT 21.39 Prison, JAIL 21.18 JupGE (sb.) 21.41 Crm 21.21 PLAINTIFF 21.42 Murprr 21.22 DErenDANT 21.43 ADULTERY 21.23 Wrrness (sb.) 21.44 Rapr (sb.) 21.24 Swrar 21.45 Tuurt 21.25 OatH 21.46 ARson 21.31 AccusE 21.47 PrERroRY
```


## [2026-09-06T22:09:04.889Z] TOOL CALL #59: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^ *826 \\|826 SELECTED\\| 826$\\|^826\" SYN.txt | head\necho \"---\"\ngrep -n \"1447\\|1446 SELECTED\\|LAW$\" SYN.txt | head\necho \"=== find 21.37 section ===\"\ngrep -n \"21\\.37\" SYN.txt | head"
}
```


### [2026-09-06T22:09:06.943Z] TOOL RESULT

```
21061:826 SELECTED INDO-EUROPEAN SYNONYMS
---
3377:2.61 FATHER-IN-LAW 2.62 MOTHER-IN-LAW
3421:2.63 SON-IN-LAW 2.64 DAUGHTER-IN-LAW
3480:2.66 SISTER-IN-LAW
6720:‘blow’ (10.38) ; Sp. resollar, Rum. rdsufla (whence sb. rdsuflare), fr. new cpd. parallel to Lat. resptrare. REW 8430. Puscariu 1447.
35445:CHAPTER 21 LAW
35481:LAW
35648:LAW
35682:LAW
35843:LAW
=== find 21.37 section ===
```


## [2026-09-06T22:09:09.187Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '21050,21120p' SYN.txt"
}
```


### [2026-09-06T22:09:09.236Z] TOOL RESULT

```
Rum. pret; ;
i 7 - pret; OF r.
ML 2, ME ee [> W. pris], NE price _~8n., Sw. pris] Du.
ae NHG preis), orale, as
” “Scompense’ neut, of an
adj. *pretios fr. the IE prep. *preti, *proti in Skt. prati ‘against, back’, ChSl. protivi ‘towards’, ete. (these fr. IE *per, pro, ete. and so ultimately connected with Grk. répynue ‘sell’, Lith. pirktz ‘buy’, etc., 11.81; but this remote formal con- nection is without bearing upon the se- mantic development). Walde-P. 2.38. Ernout-M. 808. REW 6746. Falk- Torp 850.
3. Ir. lig, liag (also ‘value’), NIr. luach (also ‘value, cost’): W. golud ‘riches’ (11.42), Goth. laun, etc. ‘wages’ (11.78), etc. Walde-P. 2.380. Pedersen 1.54.
4. Goth. wairp (and andawair pi [and- wair pi cod. Arg.], epd. of and [a]- ‘against, in return’) = ON verd, OE weorb, ME worth, OHG werd, MHG wert ‘worth, value, price’ (NE worth, NHG wert, etc.), beside adjs. Goth. wairps, ON verdr ‘worth, worthy’, etc., perh. : Ir. frith-, MW guwrth, W. wrth ‘against’, fr. the root in Lat. vertere ‘turn’, Goth. wairpan, etc. ‘become’. Walde-P. 1.275. Falk- Torp 1403.
Dan., Sw., ME pris, NE price, etc., above, 2.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
——— oo
826 SELECTED INDO-EUROPEAN SYNONYMS
5. Lith. kaina, ChSI. céna, etc., gen- eral Slavic (Russ. cena > Lett. cena) : Av. kaéna- ‘revenge, punishment’, Grk. mow? ‘retribution, penalty’, IE *k”oina-, fr. the root in Grk. ziw ‘estimate, honor’, tiuy, etc. (above, 1). Walde-P. 1.509. Berneker 124.
Lith. kaina is now the accepted word for ‘price’, whence vb. kainoti ‘cost’ in kiek kainoja ‘how much does it cost?’, etc. Cf. NSB and Hermann, Lit.- deutsches Gespriichsb. 144. Lalis and Kurschat have preké or prekia for ‘price’, but this is now ‘wares’ like Lett.
11.88 DEAR (= Costly, Expensive)
Grk. — xodvreAts, Teptos Goth. galaufs NG axptBés ON dyrr Lat. carus Dan. dyr
It. caro Sw. dyr Fr. cher OE déore Sp. caro ME dere Rum. scump NE dear Tr. logmar Du. duur Nir. daor OHG tiurt W. drud MHG ltiur(e) Br. ker NHG teuer
A few of the words listed are deriva- tives of those for ‘price’, ‘cost, expense’, or the like; and a few come through the notion of ‘stingy’. But the most wide- spread development is from ‘dear, be- loved’ or ‘esteemed, worthy’ through ‘highly valued’ to ‘dear, expensive’. This may rest in part, but not wholly, on semantic borrowing from Lat. carus. There is no trace of such use of Grk. iros.
Omitted are the words which, while meaning literally ‘costly’, are not the common words for ‘dear’ as applied to an article for sale, but are used mostly in in a figurative sense, more nearly ‘cost- ly’, ‘precious’ or ‘extravagant’. Thus Lat. pretidsus fr. pretium ‘price’ and sometimes ‘dear, expensive’, but mostly ‘valuable, precious’; and the numerous
CC-O0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
prece (: Lith. pirktt ‘buy’, etc.). Fraen. kel, Z. sl. Ph. 6.87.
6. Skt. vasna- : Gr. vos, above, 1.
Skt. milya- prob. : mila- ‘root, foun- dation’.
Skt. argha-, Av. arafah- (NPers. arz ‘price’) : Skt. arh-, Av. araj- ‘be Worth’ Lith., Lett. alga ‘wages’ (11.78). Walde. P. 1.91. Barth. 192.
Av. paraska-, prob. (*prt-ska-) : Skt, a-prata- ‘without recompense’, and Lat, pretium, etc. (above, 2). Walde-P. 2.38, Barth. 896.
ete.,
Lith. brangus Lett. ddargs ChSl.  dragit SCr. skup Boh. drahy Pol. drogi
Russ. dorogoj Skt. mahdargha-, bahumi- lya-, etc.
Av. are
derivatives of It. costo, ete. ‘cost? (11.72), as It., Sp. costoso, OF r. costeus (> ME costouse > W. costus), Fr. cotteux, NE costly, NHG kostbar, etc. 1. Grk. zodvredjs, cpd. of zodb ‘much’ and last member fr. rédos ‘tax, toll, duty’ (11.69). Grk. riptos, fr. riuy ‘price’ (11.87). NG dxpiBés, fr. class. Grk. axpifis ‘exact, precise, accurate’ then (fr. ‘exact in money matters’) ‘parsimonious, stin- gy’ and hence ‘dear’ (as SCr. skup, be- low). 2. Lat. carus (> It., Sp. caro, Fr. cher) ‘dear’ = ‘beloved’ (16.28) and ‘ex- pensive’ (Plaut. in both senses). Rum. scump, fr. Slavic, cf. Bulg. ska- pu, etc. below, 6. 3. Ir. logmar, epd. of log ‘price’ and mar, mor ‘great’.
possEsslo
Macbain 123 undoubtedly and hence ‘cheap’ as
5 dere. i But 7 ‘enslaved’
gor rT.
7 é y’ fr. earlier sense mad,
rievous’ (Spur- orig.
both senses, MBr.
‘dear’ in er ‘d quer = Fr. cher
, Norm. Fr. (above): Henry 4, Goth. ig j et lu-galauys sive y also fil ON yar, etc.
Br. fk
63.
ifs = moduredns “expen- = rodbrimos ‘Very ‘dear,
ON dgrr, fiuri
es valued, worthy’ (later ‘dear,
beloved’) and ‘dear, expensive’, etym.
dub, ‘Falk-Torp 172. Weigand-H.
2.1040 f.
In parts of the U.S. dear is not the
48 opposites ( i
Down, ; negative com- th 4 = pose) to those for ‘dear’, latter, Th them are unrelated to the Sonable’, ai ss peat , ‘fair, rea- Ome : ‘ : Of the Words foy ‘cheap’ preaieed
ero
(henge mostly a terms, as Lat. vilis D, DUE this is by tS etivs.), NE 'S by no means general
CC-0. In Public Domain
N, PROPERTY, COMMERCE
Digitized by Arya Samaj Foundation Chennai and eGangotri
827
colloquial word, but rather high = ‘high- priced’.
NE expensive (in US. less restricted than in England), fr. a Lat. type *ez- pensivus, fr. expendere ‘spend’, but asso- ciated with expense (11.72). NEDs.v.
5. Lith. brangus, etym.? (: Du. pronk ‘ostentation, show’?). Uhlenbeck 205. Franck-v. W. 524.
Lett. ddrgs, either cognate with, or borrowed from, the Slavic (below). Miihl.-Endz. 1.448.
6. ChSl. dragi, etc., general Slavic (in the modern languages also ‘dear, be- loved’), etym. dub. Berneker 213.
SCr. skup, also ‘stingy’, Bulg. skapit ‘dear, expensive, stingy’, in the other Slavic languages only ‘stingy’, Russ. skupoj, Boh. skoupy, Pol. skapy (11.54).
7. Skt. mahargha-, epd. of maha- ‘large, great’ and argha- ‘price’ (11.87).
Skt. bahumilya-, cpd. of bahu- ‘much, many’ and milya- ‘price’ (11.87).
11.89 CHEAP
Gtk, ebreAs, etwvos Goth. Lith.  pigus NG ormpbs ON udyrr Lett.  éts te Dan. _ billig GhBU teste i; hae mercato (vile) Sw. billig SCr.  jeftin & @) bon marché OE —undéor Boh. lacing Tum ‘ain ME good chepe, undere Pol. tani in nm NE cheap Russ. deSevyj Met sor Du. goedkoop, billajk Skt. —_alpakrita- ¥. aa See untiuri Av. sOstess
eo mare hoa, untiure, wolveil(e)
. “ mat NHG billig, wohlfeil
me of t cant a St fae.
ormed he words for cheap’ are | (and quite the opposite in NHG billig,
```


## [2026-09-06T22:09:18.154Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^14[34][0-9] SELECTED\\|SELECTED INDO-EUROPEAN SYNONYMS$\\|^ *14[0-9][0-9] \" SYN.txt | awk -F: '$1>35000 && $1<37000' | head -20\necho \"---- context around 35440-35470 ----\"\nsed -n '35435,35460p' SYN.txt"
}
```


### [2026-09-06T22:09:19.880Z] TOOL RESULT

```
35049:SELECTED INDO-EUROPEAN SYNONYMS
35103:1404 SELECTED INDO-EUROPEAN SYNONYMS
35148:1406 SELECTED INDO-EUROPEAN SYNONYMS
35192:1408 SELECTED INDO-EUROPEAN SYNONYMS
35250:1410 SELECTED INDO-EUROPEAN SYNONYMS
35287:1412 SELECTED INDO-EUROPEAN SYNONYMS
35335:1414 SELECTED INDO-EUROPEAN SYNONYMS 20.47 CAPTIVE, PRISONER
35376:1416 SELECTED INDO-EUROPEAN SYNONYMS
35439:1418 SELECTED INDO-EUROPEAN SYNONYMS
35460:1420 SELECTED INDO-EUROPEAN SYNONYMS
35503:1422 SELECTED INDO-EUROPEAN SYNONYMS
35555:1424 SELECTED INDO-EUROPEAN SYNONYMS
35611:1426 SELECTED INDO-EUROPEAN SYNONYMS
35660:1428 SELECTED INDO-EUROPEAN SYNONYMS
35707:14380 SELECTED INDO-EUROPEAN SYNONYMS
35755:1432 SELECTED INDO-EUROPEAN SYNONYMS
35812:1434 SELECTED INDO-EUROPEAN SYNONYMS
---- context around 35440-35470 ----
Lett. glinétuve, fr. gliinét ‘watch, lurk’, fr. Sw. dial. gluna ‘squint at’. Miihl.-Endz. 1.631.
6. ChSl. (late), Russ. zasada, SCr.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
1418 SELECTED INDO-EUROPEAN SYNONYMS
zasjeda, Pol. zasadska, fr. za ‘behind’ and | fr. sad- ‘sit’) most commonly used for derivs. of verb for ‘sit’, ChSl. sédétz, etc. | the ‘soma-festival’, also ‘house, asylum’,
(12518). and ‘assumed form, disguise’, and now Boh. zdloha, fr. za ‘behind’ and deriv. | attested for ‘ambush’ in Kaut. Arth. 7.17, of lezeit ‘lie’ (12.14). 10.2-4 (cf. translation of J. J. Meyer, p.
7. Skt. sattra- (lit. a ‘seating, session’, | 14, note 6).
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
CHAPTER 21 LAW
21.11 Law (General = Lat. zis) 21.32 ConDEMN 21.12 Law (Special = Lat. lér) 21.83 Convict (vb.) 21.13 Lawsuit “21.84 Acquit 21.14 Lawyrr 21.35 Guiuty 21.15 Court 21.86 INNocENT 21.16 JupGE (vb.) 21.87 Prnauty, PUNISHMENT 21.162 Drcipr 21.38 Fine : 21.17 JuDGMENT 21.39 Prison, JAIL 21.18 JupGE (sb.) 21.41 Crm 21.21 PLAINTIFF 21.42 Murprr 21.22 DErenDANT 21.43 ADULTERY 21.23 Wrrness (sb.) 21.44 Rapr (sb.) 21.24 Swrar 21.45 Tuurt 21.25 OatH 21.46 ARson 21.31 AccusE 21.47 PrERroRY
21.11 LAW (General= Lat. zis) Grk. — vdpos Goth. witdp Lith. tezsé NG VOULKT, VOULKG ON rétir Lett. likumi Lat. ids Dan. ret ChSise seer. It. diritto Sw. ratt SCr.  pravo Fr. droit OE rtht, lagu Boh. prdvo Sp. derecho ME right, lawe Pol.  prawo Rum. drept NE law Russ. pravo Ir. dliged, cert Du. recht Skt. dharma-, smrti- Nir. dlighe(adh), reacht OHG  reht Av. asa-, OPers. arta- W. cyfraith MHG reht Br. guwir (reiz) NHG recht
The ‘law’ in its general sense, the in- stitution or body of laws (Lat. zis), is in part expressed: by the same words as those denoting a specific law (Lat. lézx), or by the plural or derivs. of the latter. More commonly, however, the two no- tions are expressed by different terms, though even then the distinction is not always rigidly maintained. Especially the plural of words for ‘léx’ may be used collectively = ‘itis’.
The words for ‘itis’ are mostly based on the notion of ‘what is right’, con- nected with adjectives for ‘right’ (these
in part from ‘straight, upright’, ‘true’, or ‘fitting’), or on ‘usage, custom’. One is from ‘memory’ through ‘tradition’. The Lat. zis was in origin a term of religious cult, asindicated by its cognates, and the Indo-Iranian words covered primarily religious law. Other examples of the religious source of legal terms will be noted occasionally in this chapter.
1. Grk. voyuos, in earliest use ‘usage, custom’, hence ‘law’ in both senses : ven ‘dispense, distribute, apportion’. Walde-P. 2.330. Boisacq 663.
NG vouos mostly ‘léx’; for ‘itis’ either
1419
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
wetted ae
a5
a
|
Digitized by Arya Samaj Foundation Chennai and eGangotri
1420 SELECTED INDO-EUROPEAN SYNONYMS
```


## [2026-09-06T22:09:25.974Z] TOOL CALL #62: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"^144[4-9] SELECTED\\|^1450 SELECTED\\|PENALTY, PUNISHMENT\\|Prnauty, PUNISHMENT\\|PENALTY$\" SYN.txt | head\necho \"---\"\nsed -n '36400,36520p' SYN.txt | head -0\ngrep -n \"^14[45][0-9] SELECTED\" SYN.txt | head"
}
```


### [2026-09-06T22:09:28.026Z] TOOL RESULT

```
35446:21.11 Law (General = Lat. zis) 21.32 ConDEMN 21.12 Law (Special = Lat. lér) 21.83 Convict (vb.) 21.13 Lawsuit “21.84 Acquit 21.14 Lawyrr 21.35 Guiuty 21.15 Court 21.86 INNocENT 21.16 JupGE (vb.) 21.87 Prnauty, PUNISHMENT 21.162 Drcipr 21.38 Fine : 21.17 JuDGMENT 21.39 Prison, JAIL 21.18 JupGE (sb.) 21.41 Crm 21.21 PLAINTIFF 21.42 Murprr 21.22 DErenDANT 21.43 ADULTERY 21.23 Wrrness (sb.) 21.44 Rapr (sb.) 21.24 Swrar 21.45 Tuurt 21.25 OatH 21.46 ARson 21.31 AccusE 21.47 PrERroRY
---
```


## [2026-09-06T22:09:31.460Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"kaénd-\\|kaéna-\\|kaena-\\|kaéna\\|Av. kaé\" SYN.txt | head -20\necho \"--- 21.37 area: search 'PUNISHMENT' ---\"\ngrep -n -i \"punishment\" SYN.txt | awk -F: '$1>35800' | head -20"
}
```


### [2026-09-06T22:09:33.356Z] TOOL RESULT

```
21062:5. Lith. kaina, ChSI. céna, etc., gen- eral Slavic (Russ. cena > Lett. cena) : Av. kaéna- ‘revenge, punishment’, Grk. mow? ‘retribution, penalty’, IE *k”oina-, fr. the root in Grk. ziw ‘estimate, honor’, tiuy, etc. (above, 1). Walde-P. 1.509. Berneker 124.
--- 21.37 area: search 'PUNISHMENT' ---
```


## [2026-09-06T22:09:37.434Z] TOOL CALL #64: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} END{print \"leaves:\",NR}' SYN.txt\ntail -c 600 SYN.txt\necho; echo \"--- last running heads ---\"\ngrep -n \"SELECTED INDO-EUROPEAN SYNONYMS\" SYN.txt | tail -5"
}
```


### [2026-09-06T22:09:39.151Z] TOOL RESULT

```
leaves: 1545
tivéd- ételt (prefix sti-), Russ. svidetel’, SCr. sujedok, Boh. svédek, Pol. Swiadek.
2. Grk. paprus, gen. -vpos (nom. also ndprup, Hom. pdprupos), NG pédprupas : peéptuva ‘care’, Lat. memor ‘mindful of’, Skt. smr- ‘remember’, ete. Prob. based on *yap-rv- (IE -iu- suffix in abstracts, etc.) orig. ‘testimony’. Walde-P. 2.689. Boisacq 612.
3. Lat. testis, lit. ‘the third’ (= Ir. triss ‘third’), fr. *tristi- : trés ‘three’. Cf. Osc. irstus ‘testés’ (fr. *tris-to-), tris- taamentud ‘testamentd’. Hence testi- montium ‘testimony��� > It. (lea
--- last running heads ---
35611:1426 SELECTED INDO-EUROPEAN SYNONYMS
35660:1428 SELECTED INDO-EUROPEAN SYNONYMS
35707:14380 SELECTED INDO-EUROPEAN SYNONYMS
35755:1432 SELECTED INDO-EUROPEAN SYNONYMS
35812:1434 SELECTED INDO-EUROPEAN SYNONYMS
```


## [2026-09-06T22:09:45.898Z] TOOL CALL #65: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\npython3 - <<'EOF'\nt=open('SYN.txt',encoding='utf-8',errors='replace').read()\nlines=t.split('\\n')\nfor ln,pg in [(21061,826),(35812,1434),(35103,1404)]:\n    print(pg,'-> leaf',('\\n'.join(lines[:ln])).count('\\f'))\nEOF"
}
```


### [2026-09-06T22:09:47.734Z] TOOL RESULT

```
826 -> leaf 894
1434 -> leaf 1536
1404 -> leaf 1504
```


## [2026-09-06T22:09:52.348Z] TOOL CALL #66: Bash

```json
{
 "command": "python3 -c \"\nimport json;d=json.load(open('/home/sfmqrb/git/rishe/data/verification/sources/refs_online.json'))\nprint(d['SYN'])\""
}
```


### [2026-09-06T22:09:54.060Z] TOOL RESULT

```
{'title': 'C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949', 'edition_found': '1949 (reprint scans, same pagination in all printings)', 'kind': 'archive_djvu', 'url': 'https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca', 'identifier': 'a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca', 'local_file': '/home/sfmqrb/git/rishe/data/verification/sources/refs/SYN.txt', 'page_offset': 'leaf = printed + 24 (e.g. leaf 26 = p.2). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf online at https://archive.org/details/<identifier>/page/n<leaf>', 'lookup_hint': "Organised by concept number (e.g. '4.42 EYE'); each section has a table of words then numbered discussion paragraphs '1. ...', '2. ...'. grep the concept heading (all caps English word) or a printed page number line.", 'notes': 'Two other open copies: dictionaryofselectedsynonyms...buck_963_N, fock_a-dictionary-...; restricted: dictionaryofsele0000carl.', 'cites': 'page number of Buck, A Dictionary of Selected Synonyms (1949)'}
```


## [2026-09-06T22:09:59.243Z] TOOL CALL #67: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\nID=a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca\nfor L in 1548 1549 1550; do curl -s -L --max-time 90 \"https://archive.org/download/$ID/page/n${L}_w1000.jpg\" -o syn_n${L}.jpg; echo \"$L: $(file -b syn_n${L}.jpg | head -c 80)\"; done"
}
```


### [2026-09-06T22:10:05.961Z] TOOL RESULT

```
1548: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 1
1549: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 1
1550: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 1
```


## [2026-09-06T22:10:08.626Z] TOOL CALL #68: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/syn_n1549.jpg"
}
```


### [2026-09-06T22:10:08.656Z] TOOL RESULT

```

```


## [2026-09-06T22:10:21.067Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s --max-time 60 \"https://archive.org/advancedsearch.php?q=title%3A%28selected+synonyms%29+AND+creator%3A%28Buck%29&fl%5B%5D=identifier&fl%5B%5D=title&rows=10&output=json\" | python3 -m json.tool 2>/dev/null | head -40"
}
```


### [2026-09-06T22:10:23.339Z] TOOL RESULT

```
{
    "responseHeader": {
        "status": 0,
        "QTime": 91,
        "params": {
            "query": "title:(selected synonyms) AND creator:Buck",
            "qin": "title:(selected synonyms) AND creator:(Buck)",
            "fields": "identifier,title",
            "wt": "json",
            "rows": 10,
            "start": 0
        }
    },
    "response": {
        "numFound": 6,
        "start": 0,
        "docs": [
            {
                "identifier": "buck-c-d-selected-indo-european-synonyms",
                "title": "Selected Indo European Synonyms"
            },
            {
                "identifier": "DictionaryOfSelectedSynonymsInThePrincipalInoEuropeanLanguages",
                "title": "Dictionary of selected synonyms in the principal Ino European Languages"
            },
            {
                "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca",
                "title": "A Dictionary of Selected Synonyms in the Principal Indo-European Languages | Carl Darling Buck"
            },
            {
                "identifier": "dictionaryofsele0000buck",
                "title": "A dictionary of selected synonyms in the principal Indo-European languages : a contribution to the history of ideas"
            },
            {
                "identifier": "dictionaryofsele0000carl",
                "title": "A Dictionary Of Selected Synonyms In The Principal Indo-European Languages"
            },
            {
                "identifier": "bwb_S0-ATR-889",
                "title": "A Dictionary of Selected Synonyms in the Principal Indo-European Language"
```


## [2026-09-06T22:10:27.131Z] TOOL CALL #70: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s -L --max-time 180 \"https://archive.org/download/DictionaryOfSelectedSynonymsInThePrincipalInoEuropeanLanguages/DictionaryOfSelectedSynonymsInThePrincipalInoEuropeanLanguages_djvu.txt\" -o buck2.txt; ls -la buck2.txt; grep -n \"21.37 PENALTY\\|PENALTY, PUNISHMENT\" buck2.txt | head"
}
```


### [2026-09-06T22:10:31.410Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 137595 Sep  6 18:10 buck2.txt
```


## [2026-09-06T22:10:34.760Z] TOOL CALL #71: Bash

```json
{
 "command": "cd /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad\ncurl -s -L --max-time 300 \"https://archive.org/download/buck-c-d-selected-indo-european-synonyms/buck-c-d-selected-indo-european-synonyms_djvu.txt\" -o buck3.txt; ls -la buck3.txt; grep -n \"PENALTY, PUNISHMENT\" buck3.txt | head"
}
```


### [2026-09-06T22:10:38.651Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 146 Sep  6 18:10 buck3.txt
```


## [2026-09-06T22:10:45.384Z] TOOL CALL #72: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT cisti Einsicht ===\"\ngrep -n \"cisti\\|čisti\\|Einsicht\" BRT.txt | head -20\necho \"=== BRT kaeS / kaesa ===\"\ngrep -n \"kaeS\\|kaes-\\|kaesa\" BRT.txt | head -10"
}
```


### [2026-09-06T22:10:45.449Z] TOOL RESULT

```
=== BRT cisti Einsicht ===
8016:•  g.  isayant-  Adj.  'eilrig  sich  küm- mernd um  -,  Sorge  tragend  für  — '  (Ijok.): yadä  asd'l  mahyä  vasS  xsayä  (sd.)  ai *hudänaos  -yas  g^rjzdä  RySin  ".  .  dann werde  ich  (auch)  eifrig  dafür  Sorge  tragen, dass  der  Einsichtige  es"'  bekomme"  Y. J0.9.
9395:•  ].  karsvar-,  -van-  n. 'Kreis' der  Erde,  vgl  iasuxra%',i,an:  —  V\,tkctdiakxraihimi 'Erdteü'":  />//«/  -^.^r»  j-«/  x^aniraiim\  ■  feasu.xraO-wan-  Adj.  (auch  fem.) Yt.i£.i5,^o.i5,67,i33,Y.57-3i.y./p.39,  -der  geringe  Einsicht  besitzt':  noit  ia H.  /.  I4i  -  't'^rp  yat  ar.>zahi  Yt.  i2.  9;  „^i^^a  -^wa  (NSf.)  "nicht  darum  (?)  ein ,„_,..  _  .„./   .,..„  j.^/  vouru.bar»iU:^^^^  ^„„  geringer  Einsicht"  N.40'>.
10368:haca  "StfCa  ". ,  aus  der  Höhle  der  Dr"  \  •  g.  ganbiim  Inf.  'festzuhalten  an  — ' ^•3-T>  — yat  .  .  paiii  fra^stim  bavainli ,  {Wk.):  ahyä  vatthlus  manatihs  syaoiiann anrS.mainyavanqm  'tarn  (GP.  als  Subj.) ,  vaocat  g"  huxralus  sp?iitamcä  ärmaittm "v/o  es  am  meisten  Höhlen  .  .  gibt"  V.rfoMr/»(sd.)  "an  dieses  guten  Sinnes  Werken j,  loj  22  (als  Ob].); —  'öaF.21.  ■  hat  der  Einsichtige  festzuhalten  erklärt  und
10609:mönnäat  (sd.)  .  .  jyStSul  .  .  'tum  ('Plan')  |  itJ.107 Y-J2.9;  — ya  angrayä  karapanS  urspa- ydntJ  (sd.)  yäcä  'tä  (IS.,  'Absicht')  dus»- xid^ra  .  .  'S:.  48.  10;  —  vT6vä  avoi kava  Orca  ('Absicht')  paraiti  V.  75. 2.  a)  'Geisteskraft,  Einsicht,  Verstand  ; Gedächtnis  kraft,  Weisheit':  mana  'üwa^a ästica  (sd.)  Yt/.  26;  —  tat  müi  'tSui ('Verstand')  manankascä  vTä%?m  (sd.)  Y. .,^6'.  18;  —  hyat  .  .  ma-dj  .  .  gal^ascä tasü  damäsca  (sd.)  . .  -tus'cä  (AP. ;  'Geistes- kräfte').. Y.j/.i  i;  —  data  't^us  ('Geistes- kraft')  ..rdzA^f  vaha  sähtt  (sd.)  mananha Y,  50. 6 ;  —  hvd  -'iwa  ('Geisteskraft')  damis (sd.)  ahm  Y.  _?/.;;  —  vJdva  yai^l  güzrä (sd.)  singha»hg..vai3hsul  °'>:ina  ('Geistes- kraft') mananhö  Y.48.3;  —  aiJ  h^m firasvä  (sd.)  Jiw,?  '>wit  ('Verstand')  Y. 53-y<  —  *vfm4   aiat  hava   -^wa  Y.21
11443:•  j.,  g.  '(Sistay-  f.  'Denken;  Erkenntnis, Einsicht':  °ff''  ui§täis  syaokanä  ahm  spsn- vaiiaA.)  Y.5/.  ai;  —  isn^  ä  vanhSul ;imaS  manauhs  'tis  "wer  fsind)  die,  bei denen  die  Erkenntnis  des  guten  Sinns  sich einfinden  wird?"  '^.48.11;  — Sya  Hl  hv8 *ptä  asahya  mazdä  "in  (Folge)  dieser  Er- kenntnis: er,  M.,  ist  der  Vater  des  A" Y,  4-].  2 ;  —  hyat  ka^rä  fsA)  manS  bavat yahrä  'H/  atshat  mafkä  Y.jo.g;  —  mana xrdhwäca  °Hca  "durch  meine  Geisteskraft und  Einsicht"  Yt-/.a6; — xi'tvS yat  ahmi xratus  .  .  aitims  .  .  •tif  YL  /,  7;  F.  ig;  — prp'^yä  . .  a/ffi/  . .  a/navaihyä  -ISis'  Vr.  q. 4.  A)  als  Gottheit:  haomanqm  .  .  assis .  .  °isis  baiSaza  kaämnanqm  Vr.  fj.  i;  — ■ sonst  mit  vattula-.  aiim  ..  °tlm  vanuhTm Yi.4.1;  —  a^öil..-'t5is  vankuya  "jwiJ.. Y.7.14;  V.ip.39,  Yt//.i6.
11461:•  j.  £istä-  t.  'Erkenntnis,  Einsicht'  (nur Komp.).  A)  mit  razi'tä-  ('die  richtigste Eindchf )  Name  einer  Gottheit,  an  die  Yt.  jä' gerichtet  ist:  Hat  hE  hävSya  anoe  j^azaite rasiftam  °tqm  (statt  NS.)  asaonim  Yt  io. 126;  —  kaxaya  razistayi  'tayä  Yt.  11.  16; V.J^.  39;  —  sonst  mit  mazäalatä-  und asaoni-:  yat  kl  dahat  razista  'la  mazda-
11470:•  j.  distiSrant-  Adj.  'einsichtsvoll,  einsich-  i  (usw.)?';  a)  an  Raum,  Umfang,  AusdehnuDg: tig":  aitims  yat  ahmt  cistis  näumS 'va  Yt  'i-anid  (S?.)  aahm  aite  kata  ..  V.5.  11; ^-  7-  —  'va/iya   *nä  niijmalibya  kävanaiibya
13275:•  ).,  g.  3da(y)-  -.di-f.  i)  'Sehen,  Blick'.  — a)  'Einsicht'.  3)  'Absicht".
13750:•  j.,  g.  duS.xratav-  i)  m.  'schlechte  Ab- sicht, übler  Wille':  ^ci;  'xra^wä(\%.)  aisi- m»n  vandsn  (sd.)  Y.  4g.  4.  a)  Adj. (auch  fem.?)  'von  schlechter  Einsicht'  oder
13765:•  j.  'duS.dätay- ''  f  'schlechte  Einsicht, Mangel  an  Einsicht':  'iayä»  (GS.  als  AblS.) fraista  dmantS  "wegen  Mangels  an  Ein- sicht sind  die  meisten  glaubensfeiadlich" Aog.  sOm.
13847:•  j,,  g.  duz-dä(y)-'*  Adj.  1)  'des  Einsicht schlecht  ist,  unverständig*:  zaurva  *'dq'''> *fi',rS  k>r»naoiti  "das  Alter  macht  die  Väter unverständig"  V.  iij.  43  (?)3>.  a)  bes.  in Religionsangclegenheiten:  asca  hadarths fr^/  vJsyatil  nöit  'där»hs  "und  zwischen ihnen  beiden  haben  die  Verständigen  die rechte  Wahl  getroffen,  nicht  die  Unver- ständigen" Y.jo.  3.  2)  'des  Absichten schlecht  sind,  der  Böses  im  Sinn  hat,  arg- listig': 'da  .  .  yS  ayävani  Yt.  JO.  52;  — axtyS  °äA  ttmatfuhh  Yt.5. 82;  —  axflm 'dam  Yt.j.82;  —  hunu/{sd.)  ta  'da  ySi hinlj  "(und)  darum  (ist  er)  von  bösen Absichten  gegen  die  Seienden  erflillt" Y.  5^,  10*';  —  da!va  .  .  drvanlB  'dartftö V.  19.  3,  28,  33,  44f.',  47;  —  alSmS  °dä Y.  57.  a5,  Vt.70.  97;  —  hs  yS  'da  arvrS mainyus  V,  ig.  i,  44,  Vt.  77,  ig,  FrW.  S.  t; —  ha<a  'da  attra  mainys  V.jg.ia;  —
16236:Eig.  'Tiel  Einsicht  beiitiend'.
17205:•  j.  bar9zi-8ä(y)- :  '%i~  Adj.  'von  hoher Einsicht':  'zaiiis'''  (NSm.)  iava  vlstäsps Ytj.  108,  5-19,  17.53; —  sraosfm  "zai- Im'^  (ASm.)  Y.57.  II.
20145:•  j.  masyö.xra&wä-  f  'grössere  Einsicht^: talla  yä  kasujcratus  ''hmqm  nöit paitiimti "wenn(?)  wer  geringe  Einsicht  besitzt,  nicht nach  grösserer  Einsicht  strebt"  V.  7. 59.
20146:VIL  durch  Haplol.  ^3p6)  aus  ■•xro^imi^nu-, Ableit.  aut  ''scn&toan-,  alio  eig.  'Zustand  des, der  grössere  Einsicht  besitzt'.  aSuff.  ar.  I^ä- s.  Wh.  Gr.i  S  »J^b  bE.,  Bgu.  Grdr.  3.  iil. Geringe  Stelle.  ~  Pü.:  jr  mos  xraiih  rü  apar bähend,  erl. :  ehrpaüilän  nt  girind,
22743:1)  'etwas  (Akk.)  wählen,  sich  auswählen, sich  entscheiden  für  — ,  sich  überzeugen von  — ,  glauben,  ■n^i^eii%ai' ;  Med.^':  hyat Ti  a.d^aoma  (sd.)  .  .  upa.Jasat  hyat  vir^ natil  (3P.)  acistim  manS  ",  .  so  dass  sie sich  das  schlechteste  Denken  ausenrähl- ten"  Y,^.  6;  —  aya  *niainivS  varata (aPPrM.)  yi  drsgva  aältä  vtryxyS  aitm mainyus  spSnistB  .  .  yascä  .  .  "unter  diesen beiden    Geistern    wählten    sich    der    zur
24281:•  j.  'vira-  a.  'Verstand,  Einsicht'*. KompE.    —    np,  vir;    DsT.  6tlr.  3.  183.    — ')    iBed.   t.    SWienAW.    6/.    850.  231    vlrTA
24658:•  j.  *vya9Ta-'>  n.  'Hoffnung,  Gegenstand der  HoShung':  afiyH  vatihsui  mananhö /yaohana  vaocat  girsbqm  (sd.)  huxratui spmtqmca  ärmaitlm  .  .  täcS  vTspä  aAura %wahml  mazdä  xSa'krdt  ä  vSya%rä^'* "an  . .  hat  der  Einsichtige  festzuhalten  er- klärt und  an  . .  und  an  all  den  Hoff- nungen, o  Ah.,  in  deinem  Reich,  o  M." 'i.34. 10.
29199:sich  konzentriren,  sammeln';  J  ''mSyasträ.- baranä  (Sp.  1190  u.)  .  .  hyat  'rä  manä bavat  ya%ra  cistis  anhat  mafhä  ".  .  auf dass  da  die  Gedanken  sich  sammeln,  wo die   Einsicht    noch    schwankend   ist"    Y.
30170:•  j.,  g.  hu-xratav-  Adj.  'des  Einsicht  gut ist,  ems  ich  tsvoll':  haomö ..  •tus\.g,  23;  — fratanmät  lg  (näml.  haomahe)  havamm  . . 'tvSiyS.)  Y.10.2;  3; —  vastryö ^ao^anäii snsvS  hqs  'tul  ntmanhä  (Sp.  1068  u.)  Y.
=== BRT kaeS / kaesa ===
3304:•  j.  a-daratö.tkaesa-  Adj.  'der  den  Lehrer nicht  achtet':  vlspe  drrantö  tanu.drujö yS'^ •sd'''  vXspe  'sS'*  yß'>  asnifs'ß'''  "alle  sind ungläubig  und  leibhaftig  mit  der  Dr.  ver- bunden, die  den  Lehrer  nicht  achten;  all die  achten  den  Lehrer  nicht,  die  (ihm) ungehorsam  sind"  \.i(J.i8.
5668:•  }.  ari.tkaesa-  Adj.  'die  rechte  Lehre btsitiend,  kennend,  rechtgläubig';  °wm'> fstaa  NS.)  bm>sM  ya'^a  rahus  Az.  7.
6919:•  j.  ahurö.tkaesa-  Adj.  (fem.  'si-)-.  s. unter  ahura.tk'.
8924:•  j.  'kaeS-  V.  'struere';  nur  mit  Praev. Praes.  2  caesa-,  5  .vV/.-",  30  (Iter.)  caS- s-aya-.
8929:•  j.,  g.  ^kaes-  V.  'lehren'.   Praes.  i  .W/-;
11897:auf  diese  Weise',  zurückweisend;  a)  avavat kavaim  ^armd  ya%a  yat  .  .  us./ravayBit (sd.)  . .  f  asti  kavalm  ifarmS  %rä^nm  . . Yt.  ig.  6Bi  b)  als  Korrelat  von  iya^ 'wie':  s?rao^  ita  astü  .  .  hyaf  paour- vXm  f  ust3mfm(sd.)cyt  Y.  56.  i,  Vr.  g. 7.  c)  bei  elliptischer  Ausdrucksweise im  Sinn  von  'das  (Gesagte)  gilt  ,  .':  Aaea hä  vaxiat  [.  .]  mailyai  xsape  palrisacäiti t°  Aatna  t°  *ami.gäme  ".  .  das  gilt  im Winter,  das  im  Sommer"  N.ji;  48',  103Q); —  tat^giiniakva  %rigamlm  f  lkaesaAe{sA.) f  *vtkayehe  f  arüaAe  f  arikavanS  F. 2jb.  7)  wie  unser  schwach  toniges  (zeit- liches und  räumliches)  'da'  zur  Belebung einer  Schilderung  (usw.):  na  t°  para.- irihyeiti  avi  jqfnavS  raonqm  a  f  mirTy^m .tisvazaitcupa  tarn  kiArptm  fratauAaraiü \..3t°  msnyim  utvazaite  ,  .  avi  bar^i- navs  gairinam  . .  nä  f  frasusaUi  .  .  upa
14719:•  j.,  g.  'tkaeSa-  m.  i)  'Lehre'  bes.  auf religiösem  Gebiet,  'Glaubenslehre';  a)  im gAw.  spez.  von  der  Lehre  des  falschen Glaubens  'Irr-,  Afterlehre'":   a^^ä  ahmät
```


## [2026-09-06T22:11:18.413Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT spa- werfen ===\"\ngrep -n \"'spa-\\|spa-  V\\|spä-  V\\|werfen'\" BRT.txt | head -20"
}
```


### [2026-09-06T22:11:18.459Z] TOOL RESULT

```
=== BRT spa- werfen ===
3492:—  ai.  äpa,  np.  af-gandan  ('wegwerfen',  Bthl. IF.  //.  il6)JJ.  —  Pü.:  ii;tf,  (Komp.  auch): ape  hac,  apäl;  s.  nocli  No.  1.  —  "J  apa  F2d (Pü.:  <?^i-'und<t//)ist  aus  Komp.  losgeschält. — apa  x'aitju!  VyC.  44  stammt  aus  Y.  JJ,  4,  — »)  Pü.!  mideuilich.  —  J)  S.  noch  ^bar-  No.  19.
5815:•  j.  a-st9n»ta-  Adj.  'nicht  niederzuwerfen': 'taca  amuyamna  yazamaide  Vr.  7.  i.
6721:•  ].,  p.  "ah-  V.  'werfen'.  Praes.  26  ahya-, auhya-  (,  aäha-  '>,  ar^ia-'l).  PPf  P.  atta-; Absol.  'ashm,
6722:1)  'werfen  (eine  Waffe),  schiessen':  arstii yqm  *an/iyeili'^  avi.>tiiiris  Yt  10.  ao;  *2i; —  tiyris" .  ,  yi'm  an/iaf  »rsxsö  (sd.)  Yt  8. 6;  —  äsyatjka  Avastayn  {sA.)  *arikima- nayäi^  (GD.)  Y.57.  28;  —  yalat  hvasttm (sd.)  *a»Ayeiti''>  Yt/0. 21;  —  asia  F. 7.  2)  II  militärisch  'werfen'  sva.  'drängen in  — '  (Lok.):  aniy<^  äpiyä  *,lAyata^'>  "der Feind  wurde  ins  Wasser  gedräng "" /.  19.
6724:mit  ava  'herabwerfen':  * avanhynti^''  F. 23  a«^
19176:•  g.  ni  mar^dyäi  Inf.  'niederzufegen,  zu Boden  zu  werfen':  ka'^ä  alai  drupm  dyqm sastayS  (sd.)  iiT  Alm  m'  %wahya  mq'i^räii
23301:mit  ni  'überziehen,  Überwerfen':  ym "utg)r»snävayö  (sd.)  *niva!3h>nti*^  yeii  .  , N.p4.
26751:Ableit  aus  *siirii-  f.  'Niederwerfen',  »um  V. ^star-,  —  Pü. ;  visiarisnömand. j.    slirmli  N.  103:    lies  stirittinli,    1.   ^slar- mit  No.  2.
26904:•  j.  'spä-  V.  'iacere'',  abicere'.  Praes.  17 spaya-,  j-Aor.  i  ipak-. —  PPfP.  'spata-, PFP.  pfkwa--''>.
26916:•  j.,  g.  ^spä-  V.  'proficere'.  Praes,  lob spanv-,  spsnv-.
```


## [2026-09-06T22:11:19.607Z] TOOL CALL #74: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor n in 296 297 298 299 300; do echo \"==== POK_02 leaf $n\"; awk -v n=$n 'BEGIN{RS=\"\\f\"} NR==n' POK_02.txt | head -c 250; echo; done"
}
```


### [2026-09-06T22:11:21.762Z] TOOL RESULT

```
==== POK_02 leaf 296
erung;  von  Junker  mit  dem  k  des  Plurals  gleichgesetzt);
gr.  og-TB  (hier  hinter    dem  Relativum;    s.  Schwyzer   Gr.  Gr.  II  575 f.);
lat.  quom-que,  cunque,  umbr.  pumpe  ursprüngl.  ,*wann  auch  immer*, dann  mit  Verblassen  de
==== POK_02 leaf 297
obachten,  scheuen, ehren*,  andrerseits  ,animadvertere,  strafen,  rächen,  büßen;  Sühne, Geldstrafe,  deren  Wert,  Preis,  Schätzung',  woraus  , Hoch  Schätzung, Ehre*  ebenfalls  gewinnbar  ist;  k'Ae^iyro-  , beobachtend,  schützend*, 
==== POK_02 leaf 298
',  okajati  ,bejammern*, russ.  kdjath  ,tadeln*,  -sja  ,Reue  empfinden*.
Wurzelerweiterung  k"eis-,  k"eit-  (vgl.  oben  ai.  cüj  citi-):
Air.  ad-cl  (*k^is-e-t)  ,sieht*,  clall  f.  , Verstand'  ==  cymr.  pwyllj  bret. poell  ds.  (*k}^eis
==== POK_02 leaf 299
iyäti-s ,Wohlbehagen'  (=  lat.  quies\  av.  säiti-s  , Freude'  (§-  =  sy-,  vgl.  gathar. syeitihyö)y  av.  syäta-,  säta-  ,erfreut'  (=  lat.  quietus),  a-säta-  ,unfroh' (=  lat.  inquietus),  Uagv-aarLgy  av.  säista-  ,behaglichst, 
==== POK_02 leaf 300
de'  Pind.),  hom.  teXid-w  ,bin,  werde',  kret.  reXo^ai ,s(TOf,iaL^,  kypr.  TsvxaL  ,er  wird  sein',  auch  xelog  n.  ,Ende',  eigentl.  ,"Wende' [TBleo)  ,vollende',  TsXsioq,  riXeoq  aus  *TeXe(j-fo-Q  ,fertig,  vollendet,  reif, erwachsen'
```


## [2026-09-06T22:11:32.608Z] TOOL CALL #75: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"##### POK_02 leaf 297 (p.636)\"; awk 'BEGIN{RS=\"\\f\"} NR==297' POK_02.txt\necho \"##### POK_02 leaf 298 (p.637)\"; awk 'BEGIN{RS=\"\\f\"} NR==298' POK_02.txt"
}
```


### [2026-09-06T22:11:34.387Z] TOOL RESULT

```
##### POK_02 leaf 297 (p.636)
obachten,  scheuen, ehren*,  andrerseits  ,animadvertere,  strafen,  rächen,  büßen;  Sühne, Geldstrafe,  deren  Wert,  Preis,  Schätzung',  woraus  , Hoch  Schätzung, Ehre*  ebenfalls  gewinnbar  ist;  k'Ae^iyro-  , beobachtend,  schützend*, k'ioi-nä  ,Strafe,  Wert',  k'Ai-ti-  ,Verständnis*  und  jVergeltung',  k^i-t-ti- jEinsicht,  Ehre'.
A.  Ai.  cäyati  ,nimmt  wahr,  beobachtet,  hat  Scheu,  hat  Besorgnis*,  cäyü- ,Ehrfurcht  bezeugend*  =  abg.  ^«/p,  cajati  ,erwarten,  warten,  hoffen' (dehnstufiges  *Ä;^e2-ö);
ai.  cinöti,  cikiti  ,bemerkt',  citi-  f.  ,Verständnis',  ci-t  f.  , Geist,  Intellekt' : gr.  äTL^o)  ,beachte  nicht'  von  ^-rt-r-  ,nicht  achtend';
k}^e[i]-ro-  in  gr.  rrjQÖg  »schützend,  wahrend',  TrjQeo)  ,nehme  wahr,  behüte; beobachte,  passe  ab,  lauere  auf,  vielleicht  auch  ai.  cära-  m.  ,Kundschafter, Späher';  darf  wegen  ai.  cdyati  ,hat  Besorgnis'  mit  Tief  stufe  auch  gr. Terirj^ai  ,bin  betrübt',  rsxLTjojg  ,furchtsam,  betrübt'  angereiht  werden? Zu  *kei-  ,bewegen'  (oben  S.  538  f.)  gehört  ke[i]so-,  ke[i]sä  ,Zeit'  in  aksl. cas^  m.  :alb.  kohe,  Jokl  M61.  Pedersen  159^  f.
637
B.  Ai.  cdyate  ,rächt,  straft*,  cBtdr-  ,Rächer*,  dpa-cüi-  f.  ,Vergeltung* (=r  djtönaLg,  TiOig)]
av.  ^äy-  ^vergelten,  büßen*,  z.  B.  cikayat  ,soll  büßen,  strafen,  rächen*, pairi-ä-kayayanta  ,sie  sollen  als  Buße  auf  sich  nehmen',  kaenä-  f.  ,Buße* (=  ^OLvrjy  sl.  cäna,  vgl.  auch  lit.  käina),  npers.  km-  ,Feindschaft,  Haß, Zorn',  av.  käd'a-  n.  ,Vergeltung',  cid'i-  f.  , Sühne  durch  Geld',  ci^ä  ,ds., Strafe',  osset.  cithä  ,Ehre'  (wie  rt^i});
gr.  t/o)  und  zto)  (ark.  reio)  Umbildung  nach  exsioa^  Tsiow),  Fut.  -rfffw, Aor.  eriaa,  Partiz.  Pass.  zerl^svog  , schätzen;  hochschätzen,  ehren',  ttoXv- rltog  ,hochgeehrt',  äxisrog  ,ungeehrt;  nicht  ehrend';
hom.  rtvo)^  att.  xho)  {*XLvf-o))  ,büße,  bezahle'.  Med.  ,lasse  zahlen  oder büßen,  strafe'  tcvv^svaL  (Eur.  Or.  323),  hom.  relwraL  (wie  kret.  dftoTSLvvra) nach  sreiaa,  Teiao))]  Fut.  tsIgco,  Aor.  ezsioa  (thess.  ftetaat,  kypr.  neiaei u.  dgl.),  Tiaig  , Zahlung,  Buße,  Strafe,  Rache',  noivri  , Sühne,  Strafe,  Rache* (daraus  lat.  poena)]  rifii^  , Schätzung;  Ehre;  Buße,  Strafe*,  Url^og  ,ohne  Ent- gelt; ungeehrt*;
wahrscheinlich  mir.  ein,   Gen.  cinad  , Schuld'  (*k^inu-t-s,  vgl.  Tivv-TaC)'^
lit.  kdina  ,Wert,  Preis';  apr.  er-kmint  ,(vom  Teufel)  befreien';
abg.  cena  ^tiixtj  Ehre,  Preis',  cäniti  ^niiäad-ai  schätzen',  ö-stufig  abg. kaj^,  kajati  se  ,Reue  fühlen',  pokajati  s§  ,Buße  tun
##### POK_02 leaf 298 (p.637)
',  okajati  ,bejammern*, russ.  kdjath  ,tadeln*,  -sja  ,Reue  empfinden*.
Wurzelerweiterung  k"eis-,  k"eit-  (vgl.  oben  ai.  cüj  citi-):
Air.  ad-cl  (*k^is-e-t)  ,sieht*,  clall  f.  , Verstand'  ==  cymr.  pwyllj  bret. poell  ds.  (*k}^eis-lä)y  usw.  (Lewis-Pedersen  350);
ai.  cBtatiy  ciketati  ,hat  acht  auf  etwas,  nimmt  wahr*,  Perf.  cikita^  Partiz. cikitvdn  ,verstehend,  wissend*,  av.  cikid-vä  , überdenkend,  überlegend*,  ai. citti-  f.  , Denken,  Einsicht*,  av.   cisti-  ds.,  ai.  cintä  , Gedanken,  Sorge*;
abg.  c&^Q,  cisti  ,zählen,  rechnen.  Geschriebenes  lesen ;  ehren',  *k^i-t-ti-  > chsth  (=  ai.  citti-h)  , Verehrung,  Ehre';  mit  anl.  s-  lett.  äJcietu,  skitu,  SUist , meinen',  Impers.  , scheinen',  sÄ:ai^i^  , zählen,  Gebete  aufsagen',  lit.  skait-au, -yti  jZählen,  lesen'.
WP.  I  508  f.,  Trautmann  113,  124,  135,  138,  Schwjzer  Gr.  Gr.  686,  697.
k'Xei-  ,aufschichten' ;  daher  ,aufhäufen,  sammeln',  ,der  Ordnung  nach  auf oder  zu  einander  legen',  ,aufbauen',  abgeschwächt  ,machen'. Ai.  cinöti^  cdyati  ,schichtet,  reiht;    sammelt,  häuft  an;    fügt  zusammen, baut  auf,  cdya-  m.  ,  Anhäufung,  Haufe,  Aufwurf;  kdya-  m.  ,Leib,  Körper* (eig.    ,*Gliederbau*;    oder    ,*Masse*?);    citä    ,Schicht,    Holzstoß,   Scheiter- haufen*, citi-  f.  , Anhäufung,  Schicht,  Scheiterhaufen',  clti-  f.  ,das  Sammeln' ; av.  kay-^  cayeitij  cinvaiti  ,(*legere)  aussuchen,  wählen*  mit  vi-  ,scheiden,
638  '
distinguereS  mit  harn-  .colligere,  (Schrittlängen)  aneinanderlegen* ;  np.  Sidat jSammeln* ;
gr.  Ttoieo)  ,mache*  (arg.-böot.  iTtoifvjas  u.  dgl.),  dann  auch  , dichte',  Deno-^ minativ  eines  *7toL-f6-g  , aufbauend,  machend'  (vgl.  dQTO-Ttoiög  ,Bäcker*)*^
abg.  ^im  (wahrscheinlich  w-St. :    ai.  cinö-ti,   av.  cinvaitij   doch  im  Slar, mit  l  der  ersten  Silbe,  wie  ai.  citi-)  , Ordnung,  Reihe,  Rang',  ciniti  ,ordnen reihen,    bilden',    wohl    auch   klr.    kojüj   kojity   ,anzetteln,   bereiten   (etwas Böses',  wie  gr.  g)6vov  tvolscv  ,Mord  anstiften'),  poln.  dial.  koic  sie  ,gelingeii  ' vonstatten  gehn'.
Eine  s-Weiterbildung  in  av.  kae§-  (mit  Präverbien)  ,struere',  frä-  ,2n- richten,  bereiten',  vi-  ,zu-,  herrichten'  (Bartholomae  Wb.  429).
WP.  I  510,  WH.  II  406,  Berneker  538,  Trautmann  124.
k"eid-,  kniie-  , behaglich  ruhen',  k^iie-t-s  ,Behagen',  k^iie-to-s  ,froh*, k^i-lo-  ,ruhig'.
Ai.  cird-m  , Zögern,  Verzögerung',  cird-  ,langdauernd,  lang';  apers.  s
```


## [2026-09-06T22:11:54.850Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nawk 'BEGIN{RS=\"\\f\"} NR==52' incoming/FFD/FFD_pages.txt | head -60\necho \"=========== also search توختن/توزیدن in FFD\"\ngrep -n \"توختن\\|توزیدن\\|تۆز\" incoming/FFD/FFD_pages.txt | head"
}
```


### [2026-09-06T22:11:56.625Z] TOOL RESULT

```
[pdf page 52]
ماده‌های ماضی و مضارع فارسی دری شش ۴۷
تفس « ایرانی باستان 12۳8-8*. برای 2 > آرای. 8 نشانه‌ای بوده که برای ساختن
مادهٌ آغازی از ريشه به کار می‌رفته است. ريشةٌ 187 به معنی «گرم‌شدن» است. 0 پیش از 5
به ؟ بدل شده است.
توان 3
توانست < فارسی میانه 113۷۷2291. مادةٌ ماضی جعلی است از 10۷۷3 که اسم بوده به
معنی «نیرو) ۰
توان + فارسی میانه 1۷38: اسم و فعل کمکی غیرشخصی.
1در فارسی میانه مادهٌ ماضی جعلی می‌ساخته است. در فارسی دری هم (<شت»
همان کار را کرده است: «خواهِست» به جاأی «خواست»» «کایست».
توختن
توخت + فارسی میانه 1574 < ایرانی باستان 1۵-:120*. برای 12 > آراست. 1208
صورت اصلی 120 است» 8 پیش از 1 به #بدل شده است. ريشهٌ 1308 به معنی «پرداختن»
توز « فارسی میانه 132 < ایرانی باستان ۵-[1۵*. برای 2 -> آرای. [به جای 8 آمده
در فارسی میانه به معنی «پرداختن» و «توبه و جبران کردنْ» است. در فارسی
دری به معنی «فرو کردن و کشیدن و پرداختن» آمده است. شاهنامه:
چو وامش بتوزی درم صد هزار بده تا بدارد زماینادگار
بجستن
جست < ایرانی باستان 7۶-1*. برای 12 -> آراست. 104 صورت اصلی فا است» ‎٩‏
‏پیش از ۶ به 8 بدل شده است. 04 که صورت ضعیف 7204 است» «نبرد کردنْ» معنی
می‌دهد.

=========== also search توختن/توزیدن in FFD
1309:توختن
```


## [2026-09-06T22:12:25.060Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== HRN kin ===\"; grep -n \"^ *[0-9]*\\. *kin\\|kin  'Hass\\|kin  ,Hass\\|kln \" HRN.txt | head\necho \"=== HRN cidan ===\"; grep -n \"cidan\\|clden\\|čīdan\\|ciden\" HRN.txt | head\necho \"=== HRN parcin ===\"; grep -n \"parcin\\|parcln\" HRN.txt | head\necho \"=== HRN toz ===\"; awk 'BEGIN{RS=\"\\f\"} NR==111' HRN.txt | tail -25"
}
```


### [2026-09-06T22:12:27.248Z] TOOL RESULT

```
=== HRN kin ===
=== HRN cidan ===
1414:Zu dem Bedeutungs Wechsel vergl. np. ciden 'sam-
7493:sein wie in kiisüden statt gusciden. Anderenfalls würde
=== HRN parcin ===
=== HRN toz ===
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


## [2026-09-06T22:12:42.128Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nfor f in MON_part1.txt MON_part2.txt; do echo \"### $f\"; grep -c \"\" $f; grep -n \"کین\" $f | head -3; done"
}
```


### [2026-09-06T22:12:43.797Z] TOOL RESULT

```
### MON_part1.txt
99339
1023:کنند» مخزن اب؛ ایدان» ایکین تالات. 
1481:تسکین دهنده» شخصی که مردم رابه زیان 
1575:9 ان شرامکین کشتی :زم آیروه 
### MON_part2.txt
94500
155:و تسکین دهندة سرفه است و در موارد 
321:که مردم را بفریبد» خداع. خاین. کینه‌ور. 
707:کین ات بیان ره ونه بر تین
```


## [2026-09-06T22:12:53.369Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && wc -l index.jsonl && tail -20 index.jsonl | python3 -c \"\nimport sys,json\nfor l in sys.stdin:\n    d=json.loads(l); print(d.get('sha') or d.get('hash') or '', d.get('url'))\n\""
}
```


### [2026-09-06T22:12:55.295Z] TOOL RESULT

```
3208 index.jsonl
 https://www.iranicaonline.org/articles/cista-and-cisti-avestan-derivatives-of-the-verb-cit-to-notice-to-understand/
 https://ia800601.us.archive.org/19/items/OldPersian/Kent-OldPersian_djvu.txt
 https://starlingdb.org/cgi-bin/response.cgi?single=1&basename=/data/ie/pokorny&text_number=1085&root=config
 https://starlingdb.org/cgi-bin/response.cgi?single=1&basename=/data/ie/pokorny&text_number=1086&root=config
 https://www.etymonline.com/word/poet
 https://www.etymonline.com/word/poem
 https://ahdictionary.com/word/indoeurop.html
 https://starlingdb.org/cgi-bin/response.cgi?single=1&basename=%2Fdata%2Fie%2Fpokorny&text_number=1085&root=config
 https://ia600300.us.archive.org/BookReader/BookReaderJSIA.php
 https://archive.org/download/grundrissderneu00horngoog/grundrissderneu00horngoog_djvu.txt
 https://archive.org/download/persischestudie00hbgoog/persischestudie00hbgoog_djvu.txt
 https://en.wiktionary.org/wiki/%DA%A9%DB%8C%D9%86%D9%87
 https://www.etymonline.com/word/penalty
 https://archive.org/download/altiranischeswr00bartgoog/altiranischeswr00bartgoog_djvu.txt
 https://en.wiktionary.org/wiki/%D5%BA%D5%A1%D6%80%D5%AB%D5%BD%D5%BA
 https://en.wiktionary.org/wiki/%CF%80%CE%BF%CE%B9%CE%AD%CF%89
 https://dsal.uchicago.edu/cgi-bin/app/steingass_query.py?qs=%D8%AA%D9%88%D8%B2%D9%8A%D8%AF%D9%86&searchhws=yes
 https://dsal.uchicago.edu/cgi-bin/app/steingass_query.py?qs=%D8%A7%D9%86%D8%AC%D9%8A%D8%AF%D9%86&searchhws=yes
 https://dsal.uchicago.edu/cgi-bin/app/steingass_query.py?qs=%D9%BE%D8%B1%DA%86%D9%8A%D9%86&searchhws=yes
 https://en.wiktionary.org/wiki/%CF%80%E1%BF%B6%CF%81%CE%BF%CF%82
```


## [2026-09-06T22:13:02.633Z] TOOL CALL #80: Bash

```json
{
 "command": "mkdir -p /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/pg289.png /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/289.png && ls -la /home/sfmqrb/git/rishe/data/verification/sources/refs/ocr/BOOK/ | tail -5"
}
```


### [2026-09-06T22:13:02.704Z] TOOL RESULT

```
-rw-rw-r--  1 sfmqrb sfmqrb  90918 Sep  5 10:16 92.png
-rw-rw-r--  1 sfmqrb sfmqrb  93420 Sep  5 10:18 94.png
-rw-rw-r--  1 sfmqrb sfmqrb  78178 Sep  5 10:14 95.png
-rw-rw-r--  1 sfmqrb sfmqrb  72929 Sep  5 10:19 96.png
-rw-rw-r--  1 sfmqrb sfmqrb  65608 Sep  5 10:43 99.png
```


## [2026-09-06T22:13:06.728Z] TOOL CALL #81: Bash

```json
{
 "command": "python3 tools/fetch_source.py 'https://archive.org/download/oldpers/oldpers_djvu.txt' --note 'page 289 entry 1 nodes #6/#8/#9, Kent Old Persian Lexicon p.209 s.v. sa- \"erect, build\", fra- + sa-, Av. spa- \"throw away\", Ars. Phl. pari-sp \"wall\"' 2>&1 | tail -3"
}
```


### [2026-09-06T22:13:10.142Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/14b1d00a111388e7.txt
```


## [2026-09-06T22:13:17.085Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== SKT poet/poem/punish/pain ===\"\ngrep -n \"^POET\\|^POEM\\|^PUNISH\\|^PAIN\\|Poet\\.\\|poet, \" SKT.txt | head -10\ngrep -n \"poet (F\" SKT.txt | head\necho \"=== SKT search ===\"\ngrep -n -i \"poena.*poine\\|ποινή\\|poinh\\|poine\" SKT.txt | head -10"
}
```


### [2026-09-06T22:13:17.161Z] TOOL RESULT

```
=== SKT poet/poem/punish/pain ===
14303:POEM.
15164:PUNISH. ^L. /muVwrn,  ■  point;  tee
=== SKT search ===
```


## [2026-09-06T22:13:19.070Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== IEC Mann poinē ===\"; grep -n \"poinē\\|poinā\\|qoi-nā\\|k*oinā\" IEC.txt | head -10\necho \"=== IEC kʷei ===\"; grep -n \"qei-\\|qeiō\\|qeiŏ\" IEC.txt | head -10"
}
```


### [2026-09-06T22:13:19.130Z] TOOL RESULT

```
=== IEC Mann poinē ===
=== IEC kʷei ===
```


## [2026-09-06T22:13:22.696Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '14295,14315p' SKT.txt; echo \"-----\"; sed -n '15158,15172p' SKT.txt\necho \"=== FSD poinē / poena ===\"; grep -n \"poinē\\|Gk. poine\\|poine, penalty\\|poin\" FSD_vol3.txt | head -5"
}
```


### [2026-09-06T22:13:22.778Z] TOOL RESULT

```
implicate,  tU)     From piUarf,  (o  involve.  — L.  I'w-  vw^ to  fold.
implicit  (L.)  L.  impHriit of  impliiare  (above).
imply.  iF.-L)  Cointfl  it (i»),  and  p(y ;  as  if  from  a  F. but  the  F.  foitD  was  impli,jHt<^  sliU emphUr  (whence  E.  tmphy).  S« (above).
perplex.  (F  -  '  ^    '*--te«^j( first  in    use.-.]  pCTpioi
tangled:*  Cot.-!    ,     .        w?.«fcai^ terwoven  —  L.  /■f,   Lhocotigtiif .  J
PNEUMATIC, prp.  of  ptuicrr,  to  WMVe  ;  see
F-L.'i  From  M  E.//di'Asb., K,  //«/,  f>hi:.  put.  a  fold  (F. fiuatum,  ncut.  oi piuaiuj.  pp.  of to  fold  ;  see  Ply  (abovtV h  (3\  ibc  same  as  pleach  (below). eh,  plash.  10  intertwine  bou;;hs  in t.  (F.-L)     M.  E,//^r-^^«.-O.F.
tXtt  piarrr.  *  to  plash,  plait  younc Ac;  Cot.  — Low  L.  pUfsa^  a woven  bouphs  ;  put  lor  pUctia  •. far/mr,  to  weave ;  extended  from JkK.  to  weave,  whence  also  plicate,
POEM.
359
I
toother  fonn  of  plait  (above). Kt.  (F.— L>  F. //itm/,  prcs.  pi.  of I  bend  :  ice  Ply  (above), tt  (7),  ■  fold,  to  fold.  (F.-L.) w^,  •  Wuh  raany  a  folded  plisht, Ifjt.  a6.  Misspelt  lot plite  \  Caaucet Vj«.  to  fold,  Troil.  ii.  697 ;  pdle, .  T.  loiotj.  h  U  the  fern,  form  of O-  F.  /////.  -L.  //iVi/a,
ti),  »  conspiracy.  (F.-L.)  Short ^(0/ :  for  ibc  loss  of  com-,  cf._/t»f/ «*•/.  f/(j*/  for  disport^  &c.  —  F.  *-o«'
complot.  conspiracv  ;'  Cot.  Dicz derives  this  from  L.  complUitum,
€9mpiuitus,  pp.  of  (ompiUare,  to ■e.  involve,  entangle  ;   see  oom-
P^fT  -  L.)  M.  E.  TTplicn  - ^w-r,  the  old  form  aftenvards  re< &T  the  '  learoed  '  form  rrpiipttr,  to L.  wt-plkcrt.  lit  to  foltl  back  ;  as  a II*  to  reply.  Der.  rtplUa.  a  repeti- ~  "  d.  rtplica^  a  «b.  due  to  nc/Zi'- t.  reply.
ilOjKr.  in  architecture ;  to  dis- ic-  (F.  — L.)     In    both  senses.
{iroved  to  be  a  coutractioa  for wvc).     Dor.  splay-footed.       ^ (F.-L.)    M.E. /Mr;*//.  -  P. ^pli,  pliant. —  L.  mppluem.  ace. with  the  old  sense  of  *  bending imp-   (/M^),  under  ;  /AV-,  as nr,  to  fold.
t.  (F  -  L)  F.  sMpptiant, pp.'icr,  to  pray  humbly.  — L. e  below.
L.)     From  pp.  of  L.  ittp- «•  L.  rvJ^fU',  stem  of under  or  downi.  beseeching ; (above  >.
tJie   Mine   root   wc   also    hare 'iiy,    dou-blf^  du-pHc-at*.
-----
pounce  (iV  to  seize  with  the  cls< (^F.  —  L.)  Orig.  a  term  in  hawkio{ hawk's  claws  were  Icrmed  poumei. pounce  is  also  a  punch  nr  stamp  1  Nsn \.  pounson  or  puHJ^un  was  a  dag^  iB bour).  Fonifctd  as  if  from  an  ^».  F. poHcer*,  to  pierce,  not  rccortlcd, we  find  Span,  pumhar,  to  pierce,  ■a' sb  puncha,  a  prickle  (the  enact of  K.  pounce,  a  hawk's  laloo\  Tlie /ttf#/-Atfr  answers  to  a  I^w  L. not  found,  but  rcgulnrly  formed  &•• pUHCtus,  pp.  oi fmni^ere.
ptinch  1,1),  to  perforate.  (F.-D  w puiuhen,  to  prick  ;    which   seems been  coined  from  the  %\>.punck%cn, Puiuoun.  a  dagger,  awl.     Se«  be'
ptmcheon  (i),  a  punch  or  a' L.)      M.   E.  pumhffn^  pmnspum poiHson,    'a   bodkin,   also    a    ] stamp,'  SiC.\    Cot.     Cf.  Sf«a. punch.  ItaL/wiMww,  a  pvndx* A  wine-barrel.  —  L.  ptmetumm, puNc/io,  a  pricking,  panctarci of  this  word  was  changed  fron mosc.,  whilst  at  the  same  titne  tlbr was  changed  from  '  pricking'  to  "
—  L.  pynctus,  pp.  o(puffgrrt»  to  pritk also  Puncheon  ( 2\.
punctate,  jiuociured.  (L.)  i from  L.  punct-um^  a  print ;  wtlh  vA (L.  -atus).
punotiiio.  (Span  «  U)  %«r tiiht  a  nice  point  o(  honour;  ^
PUNISH. ^L. /muVwrn,  ■  point;  tee
(F.  —  L.)    F.  fon^tuft. '  punc-
',  »  Low  L.  puTUtuaHs,  *  L.
point ;  see  point  (above).
Ee.  (L.*)     From  pp.  of  Low  L.
deterrninc,  dchnc  •  L. /wwf-
(abore).
L  (L)     L./Ki«r/vra,  %  prick.
i  pp.  6i puMgtre,  to  prick.
=== FSD poinē / poena ===
975:having magnetie poles and a rotating member, a point on
1079:wryneck — m.fbob. n. A four-pointed flSh-JIg, for eateb-
2455:parts, composed with ruuiiterpoint am _
2954:that the southeast trade wind blows at its appointed time
3268:one magnet on a second at any point causes the latter to set
```


## [2026-09-06T22:13:30.517Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\nsed -n '31018,31022p' KLN_1966.txt | head -c 1200; echo; echo \"---- pain n ----\"; grep -n \"pain,  n\\.\" KLN_1966.txt | head; sed -n '26940,26946p' KLN_1966.txt | head -c 900"
}
```


### [2026-09-06T22:13:30.609Z] TOOL RESULT

```
Derivative:  Punic,  n.,  the  Punic  language, puniceous,  adj.,  purple  red.  —  L.  piiniceus,  fr.  Pu¬ nicus,  ‘Punic’.  See  prec.  word  and  -eous.  For sense  development  see  Phoenician, punish,  tr.  and  intr.  v.  —  ME.  punisshen,  fr.  MF.
(=  F.)  puniss-,  pres.  part,  stem  of  punir,  ‘to punish’,  fr.  OF.  punir,  fr.  L.  punire,  ‘to  punish’, fr.  archaic  poenire,  fr.  poena,  ‘penalty,  punish¬ ment’.  See  penal  and  cp.  words  there  referred  to. For  the  ending  see  verbal  suff.  -ish.  For  the change  of  L.  oe  to  u  cp.  Punicus,  fr.  Poenus  (see Punic),  miinire,  ‘to  build  a  wall’,  fr.  earlier  moe- nire,  fr.  moenia,  ‘wall’.
Derivatives:  punish-able,  adj.,  punish-abil-ity, n.,  punish-er,  n.,  punishment  (q.v.) punishment,  n.  —  ME.  punisshement,  fr.  MF .  pu- nissement,  fr.  punir,  fr.  OF.  See  prec.  word  and
-ment.
punition,  n.,  punishment.  —  ME.  punicion,  fr. MF.  (=  F.)  punition,  fr.  L.  punitionem,  acc.  of punitio,  ‘punishment’,  fr.  punitus,  pp.  of  punire. See  punish  and  -ition.

---- pain n ----
26942:Derivative:  paillett-ed,  adj. pain,  n.  —  ME.  peyne,  fr.  OF.  (=  F.)  pain,  fr.  L. poem,  ‘compensation,  punishment,  penalty’,  fr. Gk.  Ttoivrj,  ‘punishment’.  See  penal.
26944:pain,  tr.  and  intr.  v.  —  ME.  peynen,  fr.  OF.  pener (3rd  person,  sing,  peine),  fr.  ML.  poenare,  ‘to penalize’,  fr.  L.  poena.  See  pain,  n.
27205:Eccles.  L.  pdpa,  ‘pope’.  See  papa  and  -acy. papain,  n.,  a  vegetable  enzyme  (biochem.)  — Formed  fr.  papaya  with  subst.  suff.  -in. papal,  adj.  —  ME.,  fr.  MF.  (=  F.)  papal,  fr.
L.  palea,  ‘chaff’,  which  is  cognate  with  OI. palavah,  ‘chaff’,  OSlav.  pltva,  Russ,  peleva, Lith.  pelus  (pi.),  Lett.  p?lus,  pfiavas  (pi.), OPruss.  pelwo,  ‘chaff’  (Hung,  pelyva,  ‘chaff’, is  a  Slavonic  loan  word),  Gk.  eit(-7tXo(f)o<;, ‘omentum’,  and  prob.  also  with  L.  pellis  (for *pel-nis),  ‘skin’,  for  which  see  pellicle.  Cp. pallet,  ‘mattress’.
paillette,  n.,  1)  a  piece  of  metal  used  in  enamel painting;  2)  spangle. — -F.,  ‘spangle,  paillette, dimin.  of  paille,  ‘straw’.  See  prec.  word  and  cp. pallet.  For  the  ending  see  suff.  -ette.
Derivative:  paillett-ed,  adj. pain,  n.  —  ME.  peyne,  fr.  OF.  (=  F.)  pain,  fr.  L. poem,  ‘compensation,  punishment,  penalty’,  fr. Gk.  Ttoivrj,  ‘punishment’.  See  penal.
Derivatives:  pain-ful,  adj.,  pain-ful-ly,  adv., pain-ful-ne
```


## [2026-09-06T22:13:37.512Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\necho \"=== BRT column near spa- (line 26904) ===\"\npython3 - <<'EOF'\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nprint('\\n'.join(lines[26898:26920]))\nEOF"
}
```


### [2026-09-06T22:13:39.208Z] TOOL RESULT

```
=== BRT column near spa- (line 26904) ===
•  j.  spaSitay-"  £  'Beobachten,  Be- trachten': yaXsqmia  . .  mafyaka  aiwila^a- (sd)fa  'ta^a^a  gairinam  nätnam  dahar) Yt  19. 6.
Nom.  Mt  mit  ilay-  ($  18$  Ha.  2)  aas  dem j-Aor.  de*  V,  i/ai-').  —  ')  Es  ist  vU.  s/^r iD  lesen.  U  könnte  durch  das  vorhergehende Wort  veranlasst  sein.
g.  '"tfahAä:  %.  'sfias-  mit  No.   I.
•  j.  spa£tar-  m,  'Späher,  Beobachter': •ta  nqma  aAmi  (nämC  AhAf.)  Yt  1. 13.
Zum  V.  ipas:  —  lat.  'sptctor.  —  PS.;  pispän, erl.  1  hl  ääm  rat  fäsjiäyem.
•  j.  'spä-  V.  'iacere'',  abicere'.  Praes.  17 spaya-,  j-Aor.  i  ipak-. —  PPfP.  'spata-, PFP.  pfkwa--''>.
'wegwerfen  sva.  wegschaffsD,  -nehmen, beseitigen,  tilgen':  *'spayätP  zT  . .  daena mäxdayasnis  nars  ästavanahe  bandim  .  . anap3r?%;mt  Radium  ..  *dintänsp)r3^gm /Jran(sd.)..V.j.4i;  43  PüZ.*",  *N.J/J>; —  altücij  {Sp.  591  m.)  asidyS  *späf»Aaiti äslavanalibyS  . .  V.^j.  40.
mit  apa  'abwerfen,  ablegen,  exuere': maynä  apa,spayat  vasträ  "nackt  (war  er), die  Kleider  hatte  er  abgeworfen"  Yt. 19.  So- mit aipi  'zurückwerfen,  -schleudern  auf  -' {upa  mit  Akk.):  ustrahe..yd  kafim  aipi.- spayäli . .  ttpa  vaylanfm  huxsnao%re  (sd.) hupaUiitäne  Yt.  14. 13.
mit  ava  —  ?  — :  asta  avaspayama yyx.44.
mit  avi  'hineinwerfen  zu  — ,  hin  zu  — (aca  mit  Akk.)  von  -  weg'  (Abi):  avi t»n  spayäi  spintayi  armatsi^  (Sp.  337  o.) t>mff  Hca  V.J.  35.
mit  upairi  'oben  drauf  legen,  darüber- slecken':  Jo/  tl  (nämL  aurvantg)  . .  frä.-
yxixta  *hqm.h>qmi^A.)ia , .  d^nta  hukarita *upairi.s'paia-l  aka  YLro.us.
wxpara  'fortschleudern' :/ara  kamfr^aa spayäti  .  .  para  kam^r^ha  voiaite  mi^rff.- drujqm  "fort  schleudert  er  (naml.  Mihra) die  Köpfe  .  .,  davon  fliegen  die  Köpfe der  .  ."  Yt/o.  37.
-näifra  i)  'fort-,  hinwerfen  in  — '  (Akk.): mä  Mai»  .  .  atfrsi  vairim  (Sp.  1365  o.) fraspayöii  Aog.2&  2)  'zu  Boden  wer-
fen': pascaSa  dls  fraspayeüi  mihrg  .  . pancataynäi  satcrfnaii'ca  .  .  Yt  JO.43. EL?  —  S,  noch  pairi.späiay:  —  Pä.:  infgati- dan,  Npü.  (in  Vt.  T^:  a/gandan,  —  <)  Gl>N. BB.  17.  99  hat  fairijpatay-  und  ufotrLtpäfa- ausser  Acht  gelassen;  s.  aach  naiuspä-.  — >)  S.  die  Bern,  data  im  Ntc.  —  3)  Ea  Uetit hiei  nur  das  Wort  ifaytiü;  offenbar  wird damit  auf  V.  j.  41  angespielt.  —  4)  Hds. •sfalä.
•  j.  'tpa-  Adj.  'der  wirft,  schleudert (od.  dgiy.
KompE.  —  Zum  V.  ij^-.
•  j.,  g.  ^spä-  V.  'proficere'.  Praes,  lob spanv-,  spsnv-.
'etwas  (Akk.)  fördern,  vorwärts  bringen': armatsi^  «3  sptfäs  hvH  Hstl  uxtäii  yyao- ^anä  daOiä  a/^m  spsnvai  "durch  Fromm- ergebenheit wird  man  heilig;  ein  solcher fördert  durch  sein  Denken,  seine  Worte und  sein  Tun,  durch  sein  Ich  das  Asa" Y.5/.  2i*>.  Undeutlich:  aesi>  *zT växs . . a  (Sp.  300  o.)  vacs  ahuns  vairyö  . .  ama- he^a  virUraynaAe^a  urunaca  daenala  Span- vanti  H.  i.  4'*,
ksl.  speti,  ahd.  spustn  •proficere';  vgl.  ai. sphätäy  f.;  s,  daiu  IF.  /.  173.  —  Pü,  (lO  Y.): an  I  baoandak  mlnän  marl  miaÜHii  ki  frazä- nai  pa  stuf  an  u  hiniin;  Ü  den  i  ahräilh aaiiäyfnitär;  (in  H.):  ff  an  i  gäwiht  .  .  amä- ■uandih  u  piröikanh  u  ruväm  u  den  äff  atoiäyt/-, s.  No.  I.  —  I)  S.  noch  ip>nia-  No.  15.  — >J  Die  FuEoneen  der  Stelle  durch  Pü..  Hauc Arda  Virs,(  305  und  Dst.  ZA.  3.  648  sind grammatisch  gleich  uninlüsig.
•  g-  (.  3)  'spä-  n.  'Gedeihen,  Glück': t}m  .  .  ys  tis  w}n  (Sp.  405  u.)  hsr^i  ipsn- (kV.)cä  aspsncä  Y.  4$.  9.  a)  im  eschato- logischen  Sinn  (nur  Ableit).
KompE. ;  Ableit.  —  It.  *ipä;  worin  ar.  *ij^ -  lu  aea/;  Sp.  1561  -  und  *sphä-  -  s.  ispä-  - znsammengef allen  sein  können;  t.  zn  ipaya- %ra-.  —  iPB. !  ätäHih,  Sü.t  samädkänam.  — •>  Die  Meinung,  es  mDsse  des  Melrnins  hilbei jwf  •  statt  sf  gelesen  werden  -  Bthu  Gi^is  ' 9  -,  was  die  Herleitong  ans  ar.  *j^ilä-  aus- schlösse, ist  irrig.
```


## [2026-09-06T22:13:48.481Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs\ngrep -n \"pairi.spä\\|pairi\\.spa\\|pairispa\\|pairi\\.späitay\" BRT.txt | head -5\necho \"---\"\npython3 - <<'EOF'\nlines=open('BRT.txt',encoding='utf-8',errors='replace').read().split('\\n')\nimport re\nfor i,l in enumerate(lines):\n    if 'pairi.sp' in l or 'pairi. sp' in l:\n        print(i, l[:400]); \nEOF"
}
```


### [2026-09-06T22:13:50.522Z] TOOL RESULT

```
3000:jf. ;  —  hyal  ds  fyao^anl  mTsdavan  (sd.) '  ivam:a  (sd.)  simqmia  simötirqm^a  dprtta . .  'iim  (ASf.)  .  .  °^,Ji  vanuAim  aslm  '  huk>r3ta  upairispatä  °ka  (IS.)  bastqm  Yt vaKAatrvi  \.43.^;    —    aübyö  masdä  'kä   ;o.i25.
5770:'iSsüa  (AP.)'"'  vans^sia  *mastrr}nasca  .  . z^mäoa  hqm.raiiiwayaii  Yt  to.jx;  —  fisii 'tarn  nSit  varsqm  pairi.späili  \.6.2q;   7;
10731:Monatstag:  'Gräfte  vairyehe  aySxlustahe . . S.  1. 4;  vgl.  2. 4,  Y.  i6. 3.  aa)  als  Be- zeichnung des  unter  Xs.%  Obhut  stehenden Metalls,  mit  vairya-  Adj.:  kariasät  fra- käraysil  liyra  '^ra  *vairya  V.g.io;  — °ir3i  vairyli  pairiAarim  pairi^araysil V.ij.ß;  —  ayao/ia&um  vä  srum  vä mfyma(sd.)  '^ra  vairyaV,  16,6;  —  *Aqm.- ivqmca  .  .  (sd.)  *upairispata  aka  bastqm ''kr?m  vainm  Yt/0.135.
15623:•  j.  pairi.spätay-  f.  'Herumwerfen,  Hin- werfen, Hin{ein)fanenlassen' :  nöil  attqm nöil  varsqm  . .  'ipäiti  apqm  ästryattte  "sie
16704:upairi.späta    aka    bastqm    (APn.?)    Yt.
---
5769 'iSsüa  (AP.)'"'  vans^sia  *mastrr}nasca  .  . z^mäoa  hqm.raiiiwayaii  Yt  to.jx;  —  fisii 'tarn  nSit  varsqm  pairi.späili  \.6.2q;   7;
15622 •  j.  pairi.spätay-  f.  'Herumwerfen,  Hin- werfen, Hin{ein)fanenlassen' :  nöil  attqm nöil  varsqm  . .  'ipäiti  apqm  ästryattte  "sie
16703 upairi.späta    aka    bastqm    (APn.?)    Yt.
19063 1426  m.)  aüha  druß  nyaiaite  (sd.)  FrVf.S. i; —  «•  mlapqm  airava  aitviäi/ v^rfihyS . .  iaräi  (sd.)  Y.17. 24;  —  n'  astqm  n°* .  .  pairi.späiti  (sd.)    afqm   astryärüe  V,  6.
26632 mit  ä  'sündigen,  sich  versündigen,  in den  Zustand  der  Sündigkeit  geraten;  sündig sein,  sich  im  Zustand  der  Süodigkeit  be- finden', Akt  und  Med.;  i)  absolut:  vlsatti (sd.)  ainyS  "usyS  null  ainyS  ^vlsimnö *äsiryäte  ava  ^vJsalte  (sd.)  *na^a.cil ästryeite  (in  pass.  Sinn  'non  pcccatur') P,57;  —  ya%a  .  .  äai^y^t  a^a  äsfryati "als  ob  er  ,  ,  so  versündigt  e
26912 fen': pascaSa  dls  fraspayeüi  mihrg  .  . pancataynäi  satcrfnaii'ca  .  .  Yt  JO.43. EL?  —  S,  noch  pairi.späiay:  —  Pä.:  infgati- dan,  Npü.  (in  Vt.  T^:  a/gandan,  —  <)  Gl>N. BB.  17.  99  hat  fairijpatay-  und  ufotrLtpäfa- ausser  Acht  gelassen;  s.  aach  naiuspä-.  — >)  S.  die  Bern,  data  im  Ntc.  —  3)  Ea  Uetit hiei  nur  das  Wort  ifaytiü;  offenbar  wird damit  auf
29968 •  j.  ^ham.ivä-  f.  Name  eines  Teils  vom  Ge- schirr des  mit  Pferden  bespannten  Wagens, vli  'Deichsel':  äal  ti  (näml.  aurvants)  vXspa /rü.yuxta  'vqmca  simqmca  simöihrqmca dirita  huhr^la  ^upairi.späta  aka  bastom "und  die  (Renner)  sind  alle  angeschirrt an  die  Deichsel  und  den  Halsring  und das  Joch,  die  mit  dem  aufgespaltenen wohlgefertigten  üb  ergesteckten  Za
```


## [2026-09-06T22:13:56.123Z] AGENT

Now let me write the verification file, starting with entry 0.


## [2026-09-06T22:17:04.280Z] TOOL CALL #88: Bash

```json
{
 "command": "mkdir -p /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289 && cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289/e0.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPOK_ST = \"https://starlingdb.org/cgi-bin/response.cgi?single=1&basename=%2Fdata%2Fie%2Fpokorny&text_number=1085&root=config\"\nAHD = \"https://ahdictionary.com/word/indoeurop.html\"\nBRT_TXT = \"https://archive.org/download/altiranischeswr00bartgoog/altiranischeswr00bartgoog_djvu.txt\"\nSOD_TXT = \"https://archive.org/download/SogdianDictionary/GharibSogdianDictionnary_djvu.txt\"\nIRANICA_CISTA = \"https://www.iranicaonline.org/articles/cista-and-cisti-avestan-derivatives-of-the-verb-cit-to-notice-to-understand/\"\n\nentry0 = {\n  \"entry\": 0,\n  \"root\": \"Kwei 1, Qwei, Qwi\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *kʷey- 'to pay, atone, compensate; to requite, avenge' (Pokorny kʷei-1(t), pp. 636-637; Watkins/AHD kʷei-1)\",\n  \"note\": \"Pokorny's headword on pp.636-637 is a deliberately lumping one — 'worauf achten', from which on the one hand 'ehrerbietig beobachten, scheuen, ehren' and on the other 'animadvertere, strafen, rächen, büßen; Sühne, Geldstrafe, deren Wert, Preis, Schätzung'. Nourai's gloss 'to pay back, revenge, punish' is exactly Pokorny's section B (p.637) and exactly Watkins/AHD's split root 'kʷei-1. To pay, atone, compensate. [Pok. kʷei-(t-) 636.]'. The name, the language label 'Indo-European' and the gloss are therefore all right, and the variants 'Qwei, Qwi' are just Nourai's transcription of *kʷei-/*kʷi-. The one thing a reader should know is that modern work (LIV, Cheung 2007, Wiktionary) splits Pokorny's single entry into at least three homophonous roots: *kʷey- 'to pay, avenge' (Cheung *čai3), *kʷey- 'to perceive, heed' with the extensions *kʷeys-/*kʷeyt- (Cheung *čai4), and *kʷey- 'to pile up' (= the next chart, Kwei 2, Cheung *čai1). That split is what makes the last word of node #1, čisti-, misplaced and mis-glossed.\",\n  \"note_fa\": \"ریشهٔ هندواروپاییِ آغازینِ *kʷey- «تاوان دادن، کفّاره پرداختن، انتقام گرفتن، کیفر دادن». پوکورنی در صفحهٔ ۶۳۶–۶۳۷ این ریشه را یکجا و با دو شاخهٔ معنایی آورده است: از سویی «نگریستن، حرمت نهادن» و از سوی دیگر «کیفر دادن، انتقام گرفتن، تاوان و دیه پرداختن»؛ معنایی که نورایی نوشته دقیقاً همان شاخهٔ دوم (بخش B صفحهٔ ۶۳۷) است و با ریشهٔ *kʷei-1 در فرهنگ واتکینز (AHD) نیز مو به مو می‌خواند. بنابراین نام ریشه، برچسب زبانی و معنای آن درست است. تنها نکتهٔ لازم آنکه پژوهش امروزی (LIV، چونگ ۲۰۰۷، ویکی‌واژه) مدخل واحد پوکورنی را به چند ریشهٔ هم‌آوا می‌شکند: *kʷey- «تاوان دادن»، *kʷey- «دریافتن، توجه کردن» (با گسترش‌های *kʷeys-/*kʷeyt-) و *kʷey- «انباشتن» (که نمودار دوم همین صفحه است)؛ و همین شکستن است که نشان می‌دهد واژهٔ آخرِ گرهٔ ۱، یعنی čisti-، در جای درست ننشسته است.\",\n  \"sources\": [\n    POK_ST,\n    AHD,\n    W + \"Reconstruction:Proto-Indo-European/k%CA%B7ey-\",\n    W + \"Reconstruction:Proto-Indo-European/k%CA%B7oyn%C3%A9h%E2%82%82\"\n  ],\n  \"ref_check\": [\n    {\"ref\": \"POK:637\", \"status\": \"supports\",\n     \"note\": \"Pokorny IEW p.636 heads the entry 'kʷei-1(t)' and p.637 opens section B: 'Ai. cáyate «rächt, straft», cētar- «Rächer», apa-citi- f. «Vergeltung» … av. kāy- «vergelten, büßen» … kaenā- f. «Buße» (= ποινή…) … gr. … ποινή «Sühne, Strafe, Rache» (daraus lat. poena)'. Read on POK_02.txt leaf 297-298 (= printed 636-637); the root name and the gloss 'to pay back, revenge, punish' are exactly this section.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW pp.636-637 (POK_02.txt leaves 297-298; POK_full.txt 'Root/lemma: kʷei-1(t)', 'Page(s): 636-637')\", \"stance\": \"supports\",\n     \"note\": \"'…andrerseits «animadvertere, strafen, rächen, büßen; Sühne, Geldstrafe, deren Wert, Preis, Schätzung»' — Nourai's gloss is Pokorny's section B verbatim.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, s.v. kʷei-1 (AHD_watkins1985.txt line 650)\", \"stance\": \"supports\",\n     \"note\": \"'kʷei-1. To pay, atone, compensate. Suffixed o-grade form *koi-nā in Greek poinē, fine, penalty, borrowed into Latin as poena, penalty: PAIN, PENAL, (PENALTY), PINE2, PUNISH… [Pok. kʷei-t- 636.]' — Nourai's root gloss is word-for-word Watkins.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 508 f. (cited by Pokorny at the foot of the entry)\", \"stance\": \"supports\",\n     \"note\": \"Pokorny closes the entry 'WP. I 508 f., Trautmann 113, 124, 135, 138, Schwyzer Gr. Gr. 686, 697'; Walde-Pokorny I 508f. is the older statement of the same root. Bd. I itself is not in the local library (only WLD_band3.txt, the index volume), so this is checked only through Pokorny's back-reference.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 1949, 11.87 PRICE, p.826 (SYN.txt line 21061)\", \"stance\": \"supports\",\n     \"note\": \"'Lith. kaina, ChSl. cěna, etc., general Slavic … : Av. kaēna- «revenge, punishment», Grk. ποινή «retribution, penalty», IE *kʷoina-, fr. the root in Grk. τίω «estimate, honor», τιμή…'\"}\n  ],\n  \"nodes\": []\n}\n\nN = entry0[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Avestan\",\n  \"words\": \"kây 1; kaěnâ; kâtha; čitha; čisti\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Four of the five forms are Pokorny p.637 copied in Pokorny's own order: Av. kāy- 'vergelten, büßen' (Nourai 'kây 1'; the gloss 'be punished' is loose — the verb is active 'to requite, atone for, avenge', e.g. čikaiiaṱ 'soll büßen, strafen, rächen', pairi-ā-kayayanta 'sie sollen als Buße auf sich nehmen'); kaēnā- f. 'Buße, Strafe, Vergeltung, Rache' (Bartholomae AiW 429f., 'Zum V. kāy-. — np. kīn'), an o-grade *kʷoi-neh2- derivative; kāθa- n. 'Vergeltung' (Nourai's 'kâtha' with long â is Pokorny's kāθa-, not kaēθa-, so the transliteration is right); čiθi- f. 'Sühne durch Geld' / čiθā- 'ds., Strafe' (Nourai 'čitha : penalty'). The fifth word is wrong: Av. čisti- does not mean 'sorrow'. Bartholomae glosses čisti-/čistā- 'Denken; Erkenntnis, Einsicht' (BRT.txt line 11443, 11461) and Kellens (Encyclopaedia Iranica s.v. ČISTĀ) 'the action noun čisti «intuition, idea» … derivatives of the verb cit «to notice, to understand»'. Pokorny does list it on the cited page, but under the root extension kʷeis-/kʷeit- ('ai. citti- f. «Denken, Einsicht», av. cisti- ds., ai. cintā «Gedanken, Sorge»'), i.e. in the 'perceive/heed' half of his lumped entry, not in the 'punish/atone' half; the gloss 'sorrow' looks like Pokorny's 'Sorge' from the following Sanskrit word cintā carried across by mistake. Cheung 2007 assigns the čisti- family to *čai4 'to see, observe, perceive' (Pok. 636f.), a root distinct from *čai3 'to atone, pay penalty' (Pok. 636) which carries kāy-/kaēnā-. So one word out of five is both mis-glossed and, on the modern split, out of place.\",\n  \"derivation_fa\": \"چهار صورت از پنج صورت این گره، همان مادّهٔ اوستایی صفحهٔ ۶۳۷ پوکورنی است و به همان ترتیب: اوستایی kāy- «تاوان دادن، کفّاره دادن» (نورایی «kây 1: کیفر دیدن» نوشته که کمی نادقیق است؛ فعل معلوم است نه مجهول، مانند čikaiiaṱ «باید کیفر دهد، انتقام گیرد»)؛ kaēnā- «کیفر، تاوان، انتقام» که بارتولومه (ستون ۴۲۹–۴۳۰) آن را «به فعل kāy-» بازمی‌گرداند و خودش می‌افزاید «فارسی نو kīn»؛ kāθa- «تاوان، جزا» (املای «kâtha» با الف کشیده درست است و صورت kaēθa- نیست)؛ و čiθi-/čiθā- «کفّارهٔ نقدی، جریمه». امّا واژهٔ پنجم نادرست است: čisti- اوستایی به معنی «اندوه» نیست، بلکه بارتولومه آن را «اندیشه، شناخت، بصیرت» و کلنز در ایرانیکا «بینش، دریافت» معنی کرده‌اند. پوکورنی این واژه را در همان صفحه ولی زیر گسترشِ kʷeis-/kʷeit- «دریافتن» آورده است و در کنارش سنسکریت cintā «اندیشه، نگرانی (Sorge)» — گویا نورایی همان «Sorge» را به اشتباه بر čisti- نهاده است. چونگ نیز این خانواده را ذیل ریشهٔ جداگانهٔ *čai⁴ «دیدن، دریافتن» می‌گذارد، نه *čai³ «تاوان دادن». پس ادعای نورایی دربارهٔ چهار واژه درست و دربارهٔ یکی نادرست است.\",\n  \"sources\": [POK_ST, BRT_TXT, IRANICA_CISTA, W + \"Reconstruction:Proto-Indo-European/k%CA%B7oyn%C3%A9h%E2%82%82\"],\n  \"ref_check\": [\n    {\"ref\": \"POK:637\", \"status\": \"partial\",\n     \"note\": \"p.637 has kāy-, kaēnā-, kāθa-, čiθi-, čiθā- exactly as drawn ('av. kāy- «vergelten, büßen» … kaenā- f. «Buße» … av. kāθa- n. «Vergeltung», čiθi- f. «Sühne durch Geld», čiθā «ds., Strafe»'), and it has čisti- on the same page — but under 'Wurzelerweiterung kʷeis-, kʷeit-' with the gloss 'ai. citti- f. «Denken, Einsicht», av. cisti- ds.', i.e. 'thought, insight', not 'sorrow'.\"},\n    {\"ref\": \"SYN:826\", \"status\": \"supports\",\n     \"note\": \"Buck 11.87 PRICE, p.826 (SYN.txt line 21061): 'Av. kaēna- «revenge, punishment», Grk. ποινή «retribution, penalty», IE *kʷoina-'.\"},\n    {\"ref\": \"SYN:1447\", \"status\": \"not_checked\",\n     \"note\": \"By the chapter's own pagination (CHAPTER 21 LAW begins p.1419) p.1447 should be §21.37 PENALTY, PUNISHMENT, but the open archive.org scan of Buck (a-dictionary-of-selected-synonyms-…-by-ca) breaks off at p.1435 and no other open copy carries the page; leaf n1549 of that item is already the back cover.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW cols. 429-430 (kaēnā-) and the čisti-/čistā- entries, BRT.txt lines 11443, 11461\", \"stance\": \"partial\",\n     \"note\": \"kaēnā- 'Strafe, Vergeltung, Rache… Zum V. kāy-. — np. kīn' supports the first four words; but 'j., g. čisti- f. «Denken; Erkenntnis, Einsicht»' and 'j. čistā- f. «Erkenntnis, Einsicht»' contradict the gloss 'sorrow'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *čai3 'to atone, pay penalty' (pp.27-28) and *čai4 'to see, observe, perceive' (p.28)\", \"stance\": \"partial\",\n     \"note\": \"*čai3: 'YAv. ci- (caii-, kaii-, kaē-) «to atone» … MMP kyn «hate, malice, revenge» … PIE *kʷei- «to collect a debt, take revenge, punish» → LIV 595 f. | Pok. 636'. The čisti- family belongs instead to *čai4 (Pok. 636 f.), which Cheung keeps apart — so čisti- does not belong on this chart.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 636-637 (POK_02.txt leaves 297-298)\", \"stance\": \"supports\",\n     \"note\": \"German text quoted in ref_check above; the Avestan list is Nourai's list.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Persian\",\n  \"words\": \"kîn\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"NP کین kīn 'enmity, rancour, revenge' (extended کینه kīne with the abstract suffix -a) continues Middle Persian ⟨kyn'⟩ kēn 'hate, malice, revenge' (MacKenzie CPD 51; Nyberg II s.v. tōxtan quotes kēn tōzēt 'he will take his revenge'), Parthian kyn (Cheung *čai3), from Proto-Iranian *kainā- < PIE *kʷoi-neh2-. Pokorny states the New Persian outcome himself on the cited page: 'kaenā- f. «Buße» … npers. kīn- «Feindschaft, Haß, Zorn»'. Sound history: the Old Iranian diphthong *ai (Avestan aē) monophthongises to ē already in Middle Persian, and Middle Persian ē is raised to ī in early New Persian — hence aē > ē > ī, the spelling کین keeping the old yāʾ. Strictly the New Persian word descends through the (unattested) Old Persian *kainah rather than through the Avestan word itself, so the arrow Avestan → Persian is the usual Iranological shorthand for 'from the Old Iranian form of which Av. kaēnā- is the attested witness'. The compound کینه‌توز kīne-tūz 'vengeful' (see node #5 of the next chart) is the same word.\",\n  \"derivation_fa\": \"«کین» و صورت گستردهٔ آن «کینه» از فارسی میانهٔ kēn (نوشتهٔ ⟨kyn'⟩) «کینه، دشمنی، انتقام» است — مکنزی در فرهنگ کوچک پهلوی ص ۵۱ و نیبرگ ذیل tōxtan با شاهدِ kēn tōzēt «انتقام خواهد گرفت» — و آن از ایرانی باستان *kainā-، از هندواروپایی *kʷoi-neh₂-. خودِ پوکورنی در همان صفحهٔ ۶۳۷ می‌نویسد «npers. kīn «دشمنی، کینه، خشم»». دگرگونی آوایی روشن است: مصوّت مرکّب ایرانی باستانِ ai (که در اوستایی aē نوشته می‌شود) در فارسی میانه به ē ساده شده و ē فارسی میانه در فارسی نو به ī بدل گشته است؛ املای «کین» همان یایِ کهن را نگاه داشته است. تنها نکتهٔ فنّی آنکه نیای مستقیم واژهٔ فارسی صورت پارسی باستانِ *kainah است نه واژهٔ اوستایی؛ پیکان «اوستایی ← فارسی» در این نمودار، مانند بیشتر کتاب‌های ریشه‌شناسی، به معنی «از همان صورت ایرانی باستان که گواه اوستاییِ آن kaēnā- است» به کار رفته. ادعای نورایی درست است.\",\n  \"sources\": [POK_ST, W + \"%DA%A9%DB%8C%D9%86\", W + \"%DA%A9%DB%8C%D9%86%D9%87\", BRT_TXT],\n  \"ref_check\": [\n    {\"ref\": \"POK:637\", \"status\": \"supports\",\n     \"note\": \"'kaenā- f. «Buße» (= ποινή, sl. cěna, vgl. auch lit. káina), npers. kīn- «Feindschaft, Haß, Zorn»' — Pokorny draws the Persian word from the Avestan one on exactly the cited page.\"},\n    {\"ref\": \"KLN:1759\", \"status\": \"not_found\",\n     \"note\": \"Klein 1966 p.1759 is in the letter U ('univocal, unkempt, unless…'; KLN_1966.txt leaf 891); the Klein entries that carry this etymology are 'penal' (p.1150, with 'Avestic kāy- «to requite, be fined», kaena «punishment, vengeance»') and 'Poinae' (p.1206). Nourai's page number does not point at any entry relevant to Persian kīn — checked by locating the printed page numerals in the OCR (nearest markers 1758/1759 at that leaf).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary p.51 s.v. kēn [kyn' | = M, N kīn(a)]\", \"stance\": \"supports\",\n     \"note\": \"'kēn [kyn' | = M, N kīn(a)] hate, malice, revenge' — MacKenzie himself gives NP kīn and kīna as the continuations of MP kēn.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.95 s.v. tōxtan (NYB_vol2_glossary.txt line 3793)\", \"stance\": \"supports\",\n     \"note\": \"'kēn tōzēt he will take his revenge 4522' — the MP noun kēn in situ; the article also gives 'NP tōxtan tōz-, kīn-tōz'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 *čai3, MIDDLE PERSIAN / PARTHIAN section\", \"stance\": \"supports\",\n     \"note\": \"'MMP kyn «hate, malice, revenge»; Parthian kyn «hate, malice, revenge»; Oss. D. kine, kena «revenge»; NP kēn «anger, wrath»'.\"},\n    {\"src\": \"BRT\", \"where\": \"AiW cols. 429-430 s.v. kaēnā-\", \"stance\": \"supports\",\n     \"note\": \"the entry closes 'Zum V. kāy-. — np. kīn'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Sogdian\",\n  \"words\": \"kyn, kynh\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Gharib's Sogdian dictionary entry 5102 (printed p.203, exactly Nourai's SOD:203) reads: 'kyn(h) B, M — ken (qyn) © < Av. kaēnā © ob. -yh — vengeance, hatred', with references GMS 120, TSP 2.1186, BBB b17, Sogdica 60.10, STii 6.4.35, Frag. Len. 52.7, kynyh TSP 2.196. The word, both spellings, the gloss and the derivation from Av. kaēnā- are Gharib's own; ⟨kynh⟩ is the oblique in -h that Gharib notes ('ob. -yh'). Phonetically Sogd. kēn shows the same Old Iranian *ai > ē monophthongisation as Middle Persian kēn. Gharib's neighbouring entries confirm the semantics: 5100 kynpr kēnβar 'hating, vengeful', 5101 kynpry' kēnβaryā 'vengeance, hatred', 5099 kyn-wswytk 'free from hatred'.\",\n  \"derivation_fa\": \"در فرهنگ سغدی بدرالزمان قریب، مدخل ۵۱۰۲ در صفحهٔ ۲۰۳ — همان صفحه‌ای که نورایی ارجاع داده — چنین است: «kyn(h) [متون بودایی و مانوی] ken (qyn) < اوستایی kaēnā، حالت غیرفاعلی ‎-yh‎: کین، دشمنی». پس هم دو صورت، هم معنا و هم گرفتن آن از kaēnā- اوستایی، همه از خودِ قریب است. از نظر آوایی سغدی kēn همان یکسان‌شدن مصوّت مرکّب ایرانی باستانِ ai به ē را نشان می‌دهد که در فارسی میانه هم دیده می‌شود، و ‎kynh‎ صورت غیرفاعلی است. مدخل‌های پیرامون نیز همین معنا را تأیید می‌کنند: kēnβar «کینه‌ور» و kēnβaryā «کین‌ورزی». ادعای نورایی درست است.\",\n  \"sources\": [SOD_TXT],\n  \"ref_check\": [\n    {\"ref\": \"SOD:203\", \"status\": \"supports\",\n     \"note\": \"SOD_pages.txt leaf 269 (printed p.203) entry 5102: 'kyn(h) B, M / ken (qyn) ©<Av. kaēnā ©ob. -yh / vengeance, hatred / GMS 120; TSP 2.1186; BBB b17; Sogdica. 60.10; STii 6.4.35; Frag. Len. 52.7; -h, TSP 2, 169, 13.12; kynyh, TSP 2.196'. Nourai's SOD number here is a page, not an entry number (entry 203 is ʾpʾy-).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"SOD\", \"where\": \"Gharib, Sogdian Dictionary, entries 5099-5102 (p.203)\", \"stance\": \"supports\",\n     \"note\": \"quoted above; plus 5100 'kynpr B — kēnβar — hating, vengeful' and 5101 'kynpry' B — kēnβaryā — vengeance, hatred'.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 *čai3\", \"stance\": \"partial\",\n     \"note\": \"Cheung's *čai3 article lists MMP/Parthian kyn and Oss. kine but no Sogdian noun — silent on the Sogdian form, though it belongs to the same root; the Sogdian evidence is Gharib's.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 637\", \"stance\": \"partial\",\n     \"note\": \"Pokorny gives kaēnā- and npers. kīn but no Sogdian; 'silent' for Sogdian specifically.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Greek\",\n  \"words\": \"poině\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Ancient Greek ποινή poinḗ f. 'blood-money, wergeld; fine, ransom, penalty, requital, vengeance' < Proto-Hellenic *kʷoinā́ < PIE *kʷoi-neh2-, the same o-grade *-neh2- abstract as Avestan kaēnā-, Old Church Slavonic cěna 'price' and Lithuanian káina 'price'. Pokorny writes the equation out on the cited page: 'kaenā- f. «Buße» (= ποινή, sl. cěna, vgl. auch lit. káina)' and, in the Greek section, 'ποινή «Sühne, Strafe, Rache» (daraus lat. poena)'. Nourai's tree shape is right here: he hangs Greek off the root rather than off the Avestan node, and ποινή is indeed a sister formation of kaēnā-, not a descendant of it. His gloss 'penalty' is correct but narrow — the oldest Homeric sense is the blood-price paid for a killing.\",\n  \"derivation_fa\": \"یونانی باستان ποινή «خون‌بها، دیه؛ جریمه، کیفر، انتقام» از یونانیِ آغازین *kʷoinā́ و آن از هندواروپایی *kʷoi-neh₂- است؛ یعنی همان ساختِ درجهٔ o با پسوند ‎*-neh₂-‎ که kaēnā- اوستایی و cěna اسلاوی کهن «بها» و káina لیتوانیایی «بها» نیز از آن‌اند. پوکورنی در همان صفحهٔ ارجاع‌شده این برابری را صریح آورده است: «kaenā- «تاوان» (= ποινή، اسلاوی cěna، نیز لیتوانیایی káina)» و در بخش یونانی «ποινή «کفّاره، کیفر، انتقام» (که لاتینی poena از آن است)». شکل درختِ نورایی در اینجا درست است: او یونانی را مستقیماً از ریشه گرفته نه از گرهٔ اوستایی، و به‌راستی ποινή هم‌ریشه (خواهرِ) kaēnā- است نه فرزندِ آن. تنها معنایی که داده اندکی تنگ است؛ کهن‌ترین معنای هومری آن «خون‌بها» است.\",\n  \"sources\": [POK_ST, W + \"%CF%80%CE%BF%CE%B9%CE%BD%CE%AE\", W + \"poena\"],\n  \"ref_check\": [\n    {\"ref\": \"KLN:1447\", \"status\": \"not_found\",\n     \"note\": \"Klein 1966 p.1447 falls in the letter S ('sarment, sarong'; KLN_1966.txt leaf 737, page numerals 1446/1448 in the OCR). Klein's actual treatment of ποινή is s.v. 'penal' p.1150 ('fr. L. poenalis … fr. poena, «punishment», fr. Gk. ποινή, «bloodmoney, fine, penalty, punishment», which stands for *qwoina- and derives fr. I.-E. base *qwei-, *qwi-…') and s.v. 'Poinae' p.1206 ('Gk. Ποιναί, pl. of ποινή … fr. I.-E. base *qwoina-, whence also Avestic kaena-, «vengeance, punishment», OSlav. cena «price», Lith. kaina «price». L. poena, «punishment», is borrowed fr. Gk. ποινή'). So Klein does say exactly what the arrow says, but not on p.1447.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. penal (p.1150) and Poinae (p.1206)\", \"stance\": \"supports\",\n     \"note\": \"'Poinae … fr. I.-E. base *qwoina-, whence also Avestic kaena- «vengeance, punishment», OSlav. cena «price», Lith. kaina «price». L. poena, «punishment», is borrowed fr. Gk. ποινή.'\"},\n    {\"src\": \"POK\", \"where\": \"IEW 637\", \"stance\": \"supports\",\n     \"note\": \"'ποινή «Sühne, Strafe, Rache» (daraus lat. poena)' and 'kaenā- f. «Buße» (= ποινή…)'.\"},\n    {\"src\": \"SYN\", \"where\": \"Buck 11.87 PRICE, p.826\", \"stance\": \"supports\",\n     \"note\": \"'Av. kaēna- «revenge, punishment», Grk. ποινή «retribution, penalty», IE *kʷoina-'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷei-1\", \"stance\": \"supports\",\n     \"note\": \"'Suffixed o-grade form *koi-nā in Greek poinē, fine, penalty, borrowed into Latin as poena, penalty'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"English\",\n  \"words\": \"punish, penalty, pain\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"All three come through Latin poena, which is itself a loan from Greek ποινή (Klein s.v. Poinae: 'L. poena «punishment» is borrowed fr. Gk. ποινή') — the arrow #4→#5 silently passes over Latin, which is the immediate donor. pain: ME peyne < OF (=F) peine < L poena 'compensation, punishment, penalty' (Klein p.1108-13 s.v. pain, n.); the earliest English sense c.1300 is 'punishment, penalty', the sense 'suffering' developing from 'the pain of punishment'. penalty: c.1500, from OF pénalité and ML poenalitatem, acc. of poenalitas, from L poenalis 'of punishment' (Klein s.v. penalty p.1150). punish: ME punisshen < MF puniss-, present-participle stem of punir < OF punir < L pūnīre, archaic poenīre, from poena (Klein s.v. punish p.1273-4; the oe > u change as in Punicus for Poenus). AHD's own list under kʷei-1 is 'PAIN, PENAL, (PENALTY), PINE2, PUNISH; IMPUNITY, PENOLOGY…', of which Nourai's three are a subset — his 'AHD' reference is therefore exactly right.\",\n  \"derivation_fa\": \"هر سه واژه از راه لاتینی poena به انگلیسی رسیده‌اند و خودِ poena وام‌واژه‌ای است از یونانی ποινή (کلاین ذیل Poinae: «لاتینی poena از یونانی ποινή گرفته شده است»)؛ پیکانِ نمودار از یونانی یکراست به انگلیسی می‌رود و حلقهٔ لاتینی را ناگفته می‌گذارد. pain: انگلیسی میانه peyne از فرانسهٔ باستان peine از لاتینی poena «تاوان، کیفر»؛ معنای نخستین آن در حدود ۱۳۰۰ میلادی «کیفر» بوده و معنای «درد» از «رنجِ کیفر» پدید آمده است. penalty: از حدود ۱۵۰۰ میلادی، از فرانسوی pénalité و لاتینی میانه poenalitas، از poenalis «کیفری». punish: انگلیسی میانه punisshen از ستاکِ اسم فاعلِ فرانسویِ puniss- (مصدر punir) از لاتینی pūnīre که صورت کهن‌ترش poenīre است. فهرست خودِ واتکینز ذیل *kʷei-1 چنین است: PAIN, PENAL, PENALTY, PINE², PUNISH… و سه واژهٔ نورایی زیرمجموعهٔ همان است؛ پس ارجاع «AHD» او دقیق است. ادعای نورایی درست است.\",\n  \"sources\": [AHD, \"https://www.etymonline.com/word/pain\", \"https://www.etymonline.com/word/punish\", \"https://www.etymonline.com/word/penalty\", W + \"poena\", W + \"pain\", W + \"punish\", W + \"penalty\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. kʷei-1 (AHD_watkins1985.txt line 650) lists 'PAIN, PENAL, (PENALTY), PINE2, PUNISH; IMPUNITY, PENOLOGY, (PUNITORY), (REPINE), SUBPOENA' — Nourai's three words all appear; the online AHD appendix has the same list.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. pain n. (p.1108), penal/penalty (p.1150), punish (p.1273)\", \"stance\": \"supports\",\n     \"note\": \"'pain, n. — ME. peyne, fr. OF. (= F.) peine, fr. L. poena, «compensation, punishment, penalty», fr. Gk. ποινή, «punishment». See penal.'; 'punish … fr. L. pūnīre, «to punish», fr. archaic poenīre, fr. poena'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, kʷei-1; index entries PAIN kʷei-1, PENAL kʷei-1, PENALTY kʷei-1, SUBPOENA kʷei-1\", \"stance\": \"supports\",\n     \"note\": \"index lines 2033, 2074, 2323 of AHD_watkins1985.txt list PAIN, PENAL, PENALTY, SUBPOENA under kʷei-1.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary s.v. PUNISH\", \"stance\": \"silent\",\n     \"note\": \"the local OCR of Skeat is badly garbled at this point ('PUNISH. ^L. /muVwrn, ■ point; tee', SKT.txt line 15164) and yields nothing usable.\"}\n  ]\n})\n\njson.dump(entry0, io.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289/e0.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289/e0.py"
}
```


### [2026-09-06T22:17:06.309Z] TOOL RESULT

```
ok 5
```


## [2026-09-06T22:17:49.956Z] TOOL CALL #89: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json,glob\nfor p in sorted(glob.glob('data/verification/page-2*.json'))[-8:]:\n    d=json.load(open(p))\n    for e in d['entries']:\n        for n in e['nodes']:\n            if not n.get('words'):\n                print(p, n.get('id'), n.get('lang'), n.get('verdict'), '|', (n.get('derivation') or '')[:220])\nEOF"
}
```


### [2026-09-06T22:17:52.353Z] TOOL RESULT

```
data/verification/page-282.json 3 Hindustani confirmed | An empty pass-through box: the Persian compound šīr-o-šakar was carried into Hindustani (Hindi-Urdu) as sīrsakar / śīrśakar, the name of the puckered striped cloth, during the Mughal period, and it is from that Hindustan
data/verification/page-283.json 8 French plausible | Empty pass-through box for French calibre, first attested in the mid-16th c. (perhaps already late 15th c.) in the sense 'internal diameter of a gun barrel', the form from which English caliber and Persian کالیبر come. K
data/verification/page-283.json 13 Arabic plausible | An empty pass-through box standing for the Arabic form of the name. Arabic does have القوقاز al-Qawqāz (and the older جبل القبق Jabal al-Qabq) for the Caucasus, and it is ultimately the Graeco-Latin name; so a Latin/Gree
data/verification/page-286.json 5 None unverified | An empty box. On the render of pdf page 286 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/286.png) a wide blank rectangle is drawn to the right of the 'Old Persian kupsins' box, joined to it by an arrow, wi
data/verification/page-288.json 2 None unverified | An empty box, and empty in the printed book too: pdf p.288 (book p.258) shows a plain rectangle to the right of the Avestan box with no language header, no reference and no word, joined to it by an arrow. There is nothin
data/verification/page-288.json 4 None unverified | The second empty box, again blank on the printed page: a rectangle to the right of the Old Persian box, no language header, no reference, no word, reached by an arrow from Old Persian. Nothing to verify. As with node #2
```


## [2026-09-06T22:25:15.916Z] TOOL CALL #90: Bash

```json
{
 "command": "cat > /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289/e1.py <<'PYEOF'\n# -*- coding: utf-8 -*-\nimport json, io\n\nW = \"https://en.wiktionary.org/wiki/\"\nPOK2 = \"https://starlingdb.org/cgi-bin/response.cgi?single=1&basename=/data/ie/pokorny&text_number=1086&root=config\"\nPOK1 = \"https://starlingdb.org/cgi-bin/response.cgi?single=1&basename=/data/ie/pokorny&text_number=1085&root=config\"\nAHD = \"https://ahdictionary.com/word/indoeurop.html\"\nCHEUNG_TXT = \"https://ia801606.us.archive.org/26/items/etymological-dictionary-of-the-iranian-verb/Etymological%20Dictionary%20of%20the%20Iranian%20Verb_djvu.txt\"\nKENT_TXT = \"https://archive.org/download/oldpers/oldpers_djvu.txt\"\nKENT_TXT2 = \"https://ia800601.us.archive.org/19/items/OldPersian/Kent-OldPersian_djvu.txt\"\nHRN_TXT = \"https://archive.org/download/grundrissderneu00horngoog/grundrissderneu00horngoog_djvu.txt\"\nHUB_TXT = \"https://archive.org/download/persischestudie00hbgoog/persischestudie00hbgoog_djvu.txt\"\nBRT_TXT = \"https://archive.org/download/altiranischeswr00bartgoog/altiranischeswr00bartgoog_djvu.txt\"\nST_TOZ = \"https://dsal.uchicago.edu/cgi-bin/app/steingass_query.py?qs=%D8%AA%D9%88%D8%B2%D9%8A%D8%AF%D9%86&searchhws=yes\"\nST_ANJ = \"https://dsal.uchicago.edu/cgi-bin/app/steingass_query.py?qs=%D8%A7%D9%86%D8%AC%D9%8A%D8%AF%D9%86&searchhws=yes\"\nST_PAR = \"https://dsal.uchicago.edu/cgi-bin/app/steingass_query.py?qs=%D9%BE%D8%B1%DA%86%D9%8A%D9%86&searchhws=yes\"\n\ne = {\n  \"entry\": 1,\n  \"root\": \"Kwei 2, Kwoi\",\n  \"verdict\": \"confirmed\",\n  \"modern_form\": \"PIE *kʷei- 'to pile up, heap, stow, gather; to build, make' (Pokorny 2. kʷei- pp.637-638; Watkins/AHD kʷei-2; LIV 378 f.)\",\n  \"note\": \"Pokorny 637-638 heads the entry 'kʷei- «aufschichten»; daher «aufhäufen, sammeln», «der Ordnung nach auf oder zu einander legen», «aufbauen», abgeschwächt «machen»' — i.e. exactly Nourai's 'to pile up, build, make'; Watkins/AHD has 'kʷei-2. To pile up, build, make. [Pok. 2. kʷei- 637.]'; Cheung 2007 s.v. *čai1 gives 'PIE *kʷei- «to pile up, to heap, make» = LIV: 378 f. | Pok.: 637 f.'. Root name, language label, gloss and page reference are all right, and the second name 'Kwoi' is the o-grade *kʷoi- that gives Greek poiéō. Where the chart goes wrong is not the root but two blocks bolted onto it: (a) nodes #3-#5, the tōxtan/tōzīdan family, which has no PIE etymology at all and whose Avestan link (through the Pahlavi glossing of kāy-) points at the OTHER root, Kwei 1 (Pok. 636); and (b) nodes #6, #8, #9, Kent's Old Persian sā- / Avestan spā- / Pahlavi parisp cluster, which Kent (Old Persian p.209, §90) derives from a PIE palatal *ḱu̯ā- — a series phonologically incompatible with a labiovelar *kʷ-, which in Old Persian gives k/c, never s. Nodes #1, #2, #11, #13, #14 are a faithful and substantially correct copy of Pokorny 637 f.\",\n  \"note_fa\": \"ریشهٔ هندواروپایی آغازین *kʷei- «انباشتن، روی هم چیدن، گرد آوردن؛ ساختن». پوکورنی در صفحهٔ ۶۳۷–۶۳۸ سرواژه را چنین آورده است: «aufschichten» و از آنجا «انباشتن، گرد آوردن، به ترتیب روی هم نهادن، بنا کردن» و در معنای ضعیف‌شده «ساختن»؛ واتکینز نیز *kʷei-2 «انباشتن، ساختن» و چونگ ذیل *čai¹ همین را با ارجاع به LIV ۳۷۸ و پوکورنی ۶۳۷ می‌آورد. پس نام ریشه، برچسب زبانی، معنا و شمارهٔ صفحه همه درست است و «Kwoi» همان درجهٔ o یعنی *kʷoi- است که ποιέω یونانی از آن ساخته شده. خطا در خودِ ریشه نیست، در دو دسته‌ای است که نورایی به آن چسبانده است: نخست گره‌های ۳ تا ۵ (خانوادهٔ توختن/توزیدن) که هیچ ریشه‌شناسی هندواروپایی شناخته‌شده‌ای ندارد و تنها پیوند اوستایی‌اش — از راه ترجمهٔ پهلوی kāy- — به ریشهٔ دیگرِ همین صفحه (Kwei 1، پوکورنی ۶۳۶) می‌رسد؛ و دوم گره‌های ۶، ۸ و ۹ (sā- پارسی باستان، spā- اوستایی و parisp پهلوی) که کنت خود آن‌ها را در صفحهٔ ۲۰۹ به ریشهٔ *ḱu̯ā- کامی‌شده بازمی‌گرداند، و آن با *kʷ لبی‌کامی سازگار نیست، چون *kʷ در پارسی باستان به k/c بدل می‌شود نه به s. در برابر، گره‌های ۱، ۲، ۱۱، ۱۳ و ۱۴ رونوشت وفادار و تا حد زیادی درستِ صفحهٔ ۶۳۷ پوکورنی‌اند.\",\n  \"sources\": [POK2, AHD, CHEUNG_TXT],\n  \"ref_check\": [\n    {\"ref\": \"POK:637\", \"status\": \"supports\",\n     \"note\": \"IEW 637 (POK_02.txt leaf 298 = printed 637): 'kʷei- «aufschichten»; daher «aufhäufen, sammeln», «der Ordnung nach auf oder zu einander legen», «aufbauen», abgeschwächt «machen».' The entry runs 637-638, so Nourai's POK:637 is the opening page.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 637-638 (POK_02.txt leaf 298; POK_full.txt 'Root/lemma: kʷei-2', 'Page(s): 637-638')\", \"stance\": \"supports\", \"note\": \"quoted above; the whole Avestan/Persian/Greek material of nodes #1, #2, #11 and #13 stands on this page.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷei-2 (AHD_watkins1985.txt line 650)\", \"stance\": \"supports\", \"note\": \"'kʷei-2. To pile up, build, make. O-grade form *koi- … b. suffixed form *koi-wo-, making, in denominative verb *kʷoiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET… [Pok. 2. kʷei- 637.]'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *čai1 'to heap up, gather, collect' (pp.26-27)\", \"stance\": \"supports\", \"note\": \"'PIE *kʷei- «to pile up, to heap, make» = LIV: 378 f. | Pok.: 637 f. *IE COGNATES: Gr. ποιέω «I make, produce, compose», OCS činiti «to arrange»'.\"},\n    {\"src\": \"WLD\", \"where\": \"Walde-Pokorny I 510 (Pokorny's own back-reference at the foot of the entry: 'WP. I 510, WH. II 406, Berneker 538, Trautmann 124')\", \"stance\": \"supports\", \"note\": \"the older statement of the same root; Bd. I is not in the local library, so checked only through Pokorny's citation.\"}\n  ],\n  \"nodes\": []\n}\nN = e[\"nodes\"]\n\nN.append({\n  \"id\": 1, \"lang\": \"Avestan\",\n  \"words\": \"kay 2, kaeš, čay, čî 1; čayeti, činvaiti; pairi-čayeti; ham-či, ham-čay; vi-čay, vi-kay\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The core is Pokorny 637 word for word: 'av. kay-, čayeiti, činvaiti «(*legere) aussuchen, wählen» mit vī- «scheiden, distinguere», mit ham- «colligere, (Schrittlängen) aneinanderlegen»; np. čīdan «sammeln»' — so kay-/čay-/čī-, the present forms čayeiti (Nourai prints 'čayeti', a slip for čaiieiti) and činuuaiti, and the compounds ham-čay- and vī-čay- are all straight out of the cited page, and Cheung *čai1 documents them from the texts (OAv. vī-cinaot̰ Y 46.17, YAv. vī-cinaēta V 16.2, OAv. vīciiātā Y 30.3/30.6, vī-caiiaθā Y 46.15, YAv. han-caiiata V 9.9, part. cinuuaṇt-, inf. OAv. vīcidiiāi Y 31.5/49.6). kaēš- likewise belongs here on Pokorny's own showing (see node #11). Two items are not supported. (i) 'pairi-čayeti: set around' is not an attested Avestan verb: Cheung's *čai1 has no Avestan pairi- compound (the pari- forms he lists are Middle Iranian, MMP prcyd 'to shut in, fasten in'), and the only Avestan pairi- form of a čay- root, pairi.ākaiiaṇta Yt 10.122, belongs to the atonement root *čai3 (Pok. 636), i.e. the previous chart. The *pari-čai- needed for parčīn is a Middle/New Iranian formation reconstructed from prcyd, parčīn, Gurani párčin, Yidgha parzin, Khotanese pargyiña- 'enclosure'. (ii) 'vi-kay' as a variant of vī-čay- is doubtful: the attested YAv. vī-kaii- (Gsg. vīkaiiehe 'witness', Frahang 762) belongs to Cheung's *kai3 'to see, observe, perceive' (Pok. 636 f.), the root of MP gugāy / Parthian wygʼh / Armenian vkay 'witness', not to 'choose'.\",\n  \"derivation_fa\": \"هستهٔ این گره واژه‌به‌واژه از صفحهٔ ۶۳۷ پوکورنی است: «اوستایی kay-، čaiieiti، činuuaiti «برگزیدن، انتخاب کردن»، با پیشوند vī- «جدا کردن»، با ham- «گرد آوردن»؛ فارسی نو čīdan «گرد آوردن»». پس kay-/čay-/čī-، صورت‌های مضارع čaiieiti (که نورایی «čayeti» چاپ کرده و لغزش حروف‌چینی است) و činuuaiti، و ترکیب‌های ham-čay- و vī-čay- همه از همان صفحه‌اند و چونگ نیز آن‌ها را با شواهد متنی (یسنا ۴۶٫۱۷، وندیداد ۱۶٫۲، یسنا ۳۰٫۳، وندیداد ۹٫۹ و…) گواهی کرده است. امّا دو مورد پشتوانه ندارد: نخست «pairi-čayeti: پیرامون نهادن» که فعل اوستایی مستندی نیست؛ چونگ برای این ریشه هیچ ترکیب اوستاییِ pairi- نمی‌آورد و تنها صورتِ pairi- که در اوستا هست (pairi.ākaiiaṇta در یشت ۱۰٫۱۲۲) به ریشهٔ «کفّاره دادن» یعنی نمودار پیشین همین صفحه تعلق دارد؛ صورتِ *pari-čai- که «پرچین» را توضیح می‌دهد بازسازی‌ای از داده‌های ایرانی میانه و نو است. دوم «vi-kay»: صورت اوستایی vī-kaii- که در فرهنگ اویم آمده معنی «گواه» دارد و به ریشهٔ *kai³ «دیدن، دریافتن» می‌رود که فارسی میانهٔ gugāy و پارتی wygʼh و ارمنیِ وام‌گرفتهٔ vkay از آن است، نه به «برگزیدن». پس ادعای نورایی در بیشتر بخش‌ها درست و در دو مورد پذیرفتنی نیست.\",\n  \"sources\": [POK2, CHEUNG_TXT, BRT_TXT, POK1],\n  \"ref_check\": [\n    {\"ref\": \"POK:637,638\", \"status\": \"partial\",\n     \"note\": \"p.637 has kay-, čayeiti, činvaiti, vī-, ham- and np. čīdan exactly as drawn, and p.638 adds 'Eine s-Weiterbildung in av. kaēš- (mit Präverbien) «struere», frā- «zurichten, bereiten», vī- «zu-, herrichten» (Bartholomae Wb. 429)'. Pokorny has no pairi- compound and no 'vi-kay' — those two forms are Nourai's additions.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col.429 s.v. ¹kaēš- (BRT.txt line 8924) and the čay-/či- entries\", \"stance\": \"supports\",\n     \"note\": \"'j. ¹kaēš- V. «struere»; nur mit Praev. Praes. 2 caēša-, … (Iter.) caēšaiia-'; a separate 'j., g. ²kaēš- V. «lehren»' follows (line 8929). Bartholomae's Wb. 429 is the page Pokorny cites.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 *čai1 (AVESTAN section, pp.26-27) and *kai3 (p.28)\", \"stance\": \"partial\",\n     \"note\": \"*čai1 documents čaii-, činuuaiti, vī- and ham- compounds from the texts, but lists no Avestan pairi- form; *kai3 'to see, observe, perceive' has 'YAv. (Gsg.m.) vīkaiiehe «witness»' with MP gugāy, Parth. wygʼh, Arm. LW vkay — so 'vi-kay' is a different root.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985 s.v. kʷei-2\", \"stance\": \"silent\",\n     \"note\": \"Watkins cites only the Sanskrit and Greek reflexes of this root (kāyaḥ 'body', poiein); no Avestan material at all.\"}\n  ]\n})\n\nN.append({\n  \"id\": 2, \"lang\": \"Persian\",\n  \"words\": \"čîdan; parčîn; anjîdan; gozîdan\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Three of the four are solid, the fourth is the one Nourai himself flags. چیدن čīdan 'to gather, arrange, pluck', pres. čīn-, continues MP čīn- (MMP/BMP cyn-, past ptc. cytk /čīdag/, inf. cyydn), Parthian cyn-, from Old Iranian *čai- = Av. čaii-/činuuaiti; Pokorny states the outcome himself on the cited page ('np. čīdan «sammeln»'). The long ī of the New Persian infinitive is analogical, not inherited (Hübschmann 1895:137, repeated by Cheung: 'there are no past stems with short i in Persian'). گلچین golčīn is gol 'flower' + the present stem čīn. پرچین parčīn 'thorn-hedge, wattle fence; a clenched nail' is *pari- + čai-, but as a Middle/New Iranian compound, not from an Avestan pairi-čay-: the witnesses are MMP prcyd 'to shut in, fasten in', NP parčīdan/parčīn-, Gurani (Kandulai) párčin 'thorn-hedge', Bakhtiari parzin 'bramble', Yidgha parzin 'enclosure for sheep', Khotanese pargyiña- 'storeroom, enclosure' (Cheung *čai1); Borhān-e Qāṭeʿ p.380 defines it 'حصاری که از خار و خلاشه و شاخ درختان بر دور باغ و پالیز و کشتزار سازند'. گزیدن gozīdan 'to choose', pres. gozīn-, is *wi-čai-: Av. vī-čay- (vīcinaot̰, inf. vīcidiiāi) > MP wizīdan (MMP wcyd, BMP wcyt), Parthian wžyn- > NP gozīdan, with the regular early-NP shift of initial wi- to gu- (as wizārdan > gozārdan); برگزیدن is bar + gozīdan. Horn no.918 (p.204, Nourai's HRN:204) gives precisely this: 'guzīden «aussuchen, erwählen» … aw. vi + √čay- «aussuchen»; phlv. v(i)čītan, v(i)čīnēt; arm. LW včit; skr. vi + √cay-'. انجیدن anjīdan 'to cut into pieces, cup (bleed), pierce' is the disputed word: Horn (no.115, p.27) derived it from *ham + čay-, and Hübschmann rejected the semantics on the page Nourai's own NOTE cites — 'Trotz Horn's Hinweis auf čīdan = «sammeln, lesen, pflücken, schneiden» lässt sich anjīdan, pr. anjīnam «zerschneiden, zerstückeln» … mit skr. sam-ci «aufschichten, zusammenlegen, ansammeln» nur schwer vereinigen' (Persische Studien p.18, no.115). Modern scholarship sides with Hübschmann: Cheung's *čai1 has no such derivative and his dictionary has no root that yields anjīdan at all. The chart's NOTE is accurate, and the objection it records is the view that has prevailed.\",\n  \"derivation_fa\": \"از چهار واژهٔ این گره سه تا استوارند و چهارمی همان است که خودِ نورایی در یادداشتش نشان کرده. «چیدن» با ستاک حال «چین-» دنبالهٔ فارسی میانهٔ čīn- (مصدر čīdan) و پارتی cyn- است، از ایرانی باستان *čai- که همان čaii-/činuuaiti اوستایی است؛ پوکورنی خود در همان صفحه «np. čīdan «گرد آوردن»» را آورده است. یای کشیدهٔ مصدر فارسی قیاسی است نه موروثی (هوبشمان ۱۸۹۵ ص ۱۳۷، و چونگ همان را تکرار می‌کند). «گلچین» گل + ستاک حالِ چین است. «پرچین» از *pari- + čai- است، امّا همچون ترکیبی ایرانی میانه/نو، نه از فعلِ اوستاییِ pairi-čay-: گواهانش فارسی میانهٔ مانوی prcyd «بستن، محبوس کردن»، فارسی نو پرچیدن/پرچین-، گورانی párčin «پرچینِ خار»، بختیاری parzin، یدغه parzin «آغل گوسفند» و ختنی pargyiña- «انبار، محوطه» است؛ برهان قاطع نیز در صفحهٔ ۳۸۰ آن را «حصاری که از خار و خلاشه و شاخ درختان بر دور باغ و پالیز و کشتزار سازند» تعریف می‌کند. «گزیدن» با ستاک «گزین-» از *wi-čai- است: اوستایی vī-čay- ← فارسی میانه wizīdan ← فارسی نو گزیدن، با تحول قاعده‌مندِ wi- آغازین به gu- در فارسی نو (مانند wizārdan > گزاردن)؛ «برگزیدن» نیز بر + گزیدن است، و هرن در بند ۹۱۸ صفحهٔ ۲۰۴ — همان صفحه‌ای که نورایی ارجاع داده — دقیقاً همین را آورده. امّا «انجیدن» جای بحث است: هرن (بند ۱۱۵) آن را از *ham + čay- گرفت و هوبشمان در صفحهٔ ۱۸ همان کتاب پیوند معنایی را رد کرد: «با وجود اشارهٔ هرن به čīdan، پیوند دادن انجیدن «تکه‌تکه کردن» با سنسکریت sam-ci «روی هم انباشتن» به‌سختی ممکن است». پژوهش امروزی جانب هوبشمان را می‌گیرد؛ در فرهنگ فعل‌های ایرانیِ چونگ اصلاً ریشه‌ای که انجیدن از آن بیاید وجود ندارد. پس یادداشت خودِ کتاب درست است و همان رأیی که نقل کرده امروز پذیرفته است.\",\n  \"sources\": [POK2, CHEUNG_TXT, HRN_TXT, HUB_TXT, W + \"%DA%86%DB%8C%D8%AF%D9%86\", W + \"%DA%AF%D8%B2%DB%8C%D8%AF%D9%86\", W + \"%D9%BE%D8%B1%DA%86%DB%8C%D9%86\", W + \"%D8%A8%D8%B1%DA%AF%D8%B2%DB%8C%D8%AF%D9%86\", ST_ANJ, ST_PAR],\n  \"ref_check\": [\n    {\"ref\": \"POK:637\", \"status\": \"partial\",\n     \"note\": \"p.637 has 'np. čīdan «sammeln»' — the first word only; parčīn, anjīdan and gozīdan are not in Pokorny.\"},\n    {\"ref\": \"HRN:204\", \"status\": \"supports\",\n     \"note\": \"Horn, Grundriss p.204 no.918 (HRN.txt leaf 226): 'guzīden «aussuchen, erwählen», Praes. guzīn-em, guzīn «erwählt». aw. vi + √čay- «aussuchen»; phlv. v(i)čītan, v(i)čīnēt (AV.), arm. LW. včit «rein, lauter»; skr. vi + √cay- «auslesen, aussuchen». bel. gičinag «auswählen»'.\"},\n    {\"ref\": \"BQT:167\", \"status\": \"partial\",\n     \"note\": \"Borhān-e Qāṭeʿ vol.1 (BQT_v1_pages.txt leaf 386, printed ≈167) s.v. انجیدن: 'بروزن رنجیدن، بمعنی استره زدن باشد یعنی حجامت کردن ـ و بمعنی ریزه ریزه کردن هم گفته‌اند ـ و بیرون کشیدن را نیز گویند'. The word and Nourai's gloss are there; Moʿin gives no etymological footnote for it, so BQT does not support the derivation, only the word.\"},\n    {\"ref\": \"BQT:380\", \"status\": \"partial\",\n     \"note\": \"Borhān vol.1 leaf 604 (printed ≈380; the page carries the continuation note 'بقیه از صفحهٔ ۳۷۸'): 'پرچین ... حصاری باشد که از خار و خلاشه و شاخ درختان بر دور باغ و پالیز و کشتزار سازند و چوبهای سرتیز و خار را نیز گویند که بر سرهای دیوارها نصب کنند ـ و محکم کردن چیزی باشد در چیزی مانند میخی که بر تخته زنند و دنبالهٔ آن را از جانب دیگر خم دهند و محکم کنند'. Both senses Steingass gives; again the word, not the etymology.\"},\n    {\"ref\": \"BQT:676\", \"status\": \"supports\",\n     \"note\": \"Borhān vol.2 (BQT_v2_pages.txt leaf 134, printed ≈676-677) s.v. چیدن carries Moʿin's etymological footnote, which despite rough OCR clearly gives 'پهلوی čītan … اوستا [-čay] … هندی باستانی … بلوچی … گیلکی … تهرانی', with the gloss 'گرفتن میوه از درخت ـ گزیدن، انتخاب کردن ـ دانه از زمین برداشتن ـ بر بالای هم گذاشتن چیزی' — i.e. Moʿin derives چیدن from Pahlavi čītan and the Avestan čay- root, exactly Nourai's arrow, and even records the sense 'to place one on top of another'.\"},\n    {\"ref\": \"HRN:204\", \"status\": \"supports\", \"note\": \"(see above; the same page also underlies AEF:582, the Persian translation of Horn)\"},\n    {\"ref\": \"AEF:152,582\", \"status\": \"not_checked\",\n     \"note\": \"Khāleqi-Moṭlaq's Asās-e Ešteqāq-e Fārsi (the Persian translation of Horn with Hübschmann's notes) is not online — searched archive.org, ketabnak, noorlib; only bookshop listings. Because it is a translation of HRN/HUB, the substance is covered by the HRN:204 and HUB:18 checks.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 *čai1, NWIR section (p.27)\", \"stance\": \"partial\",\n     \"note\": \"'NP čīdan/čīn- «to collect, gather» … || (+ *pari-) NP parčīdan/parčīn- …, Gur. (Kand.) párčin «thorn-hedge», Bakht. parzin «bramble» || (+ *ui-) NP guzīdan/guzīn-, Bal. gicint/gicin- «to choose, select, elect»' — supports čīdan, parčīn and gozīdan; anjīdan does not occur anywhere in Cheung.\"},\n    {\"src\": \"HUB\", \"where\": \"Hübschmann, Persische Studien p.18 no.115 (HUB.txt leaf 29)\", \"stance\": \"contradicts\",\n     \"note\": \"'Trotz Horn's Hinweis auf čīdan = «sammeln, lesen, pflücken, schneiden» lässt sich anjīdan, pr. anjīnam «zerschneiden, zerstückeln» (vgl. anjānīdan «findere») mit skr. sam-ci «aufschichten, zusammenlegen, ansammeln» nur schwer vereinigen.' — precisely the objection the chart's own NOTE records.\"},\n    {\"src\": \"HRN\", \"where\": \"Horn, Grundriss no.918 p.204 and no.115 p.27\", \"stance\": \"supports\",\n     \"note\": \"no.918 for gozīdan (quoted above); no.115 is Horn's anjīdan article, from OP *ham + √čay-, which is what Hübschmann then rejects.\"},\n    {\"src\": \"BQT\", \"where\": \"Borhān-e Qāṭeʿ, ed. Moʿin, pp. ≈167 (انجیدن), ≈380 (پرچین), ≈676 (چیدن)\", \"stance\": \"partial\",\n     \"note\": \"quoted in ref_check; supplies the words and, for چیدن, Moʿin's Pahlavi/Avestan footnote.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. wizīdan / čīdan\", \"stance\": \"supports\",\n     \"note\": \"the local OCR of PHD is thin here, but MacKenzie's wizīdan 'to choose' and čīdan/čīn- 'to gather' are the forms Cheung cites as BMP wcyt /wizīd/ and cyn- /čīn-/ with inf. cyydn.\"}\n  ]\n})\n\nN.append({\n  \"id\": 3, \"lang\": \"Avestan\",\n  \"words\": \"taug, taux\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"There is no Avestan verb taug-/taux-. Bartholomae's Altiranisches Wörterbuch has no such root (only taoxman- 'seed', taoždya- Vd 1.19-20, and tak- 'to run'), and Cheung's article on the relevant root, *tauǰ3 'to (re)pay, pay back (a debt, fine), expiate', has no AVESTAN section at all — it begins with Middle Persian. Horn, on the very page Nourai cites (p.90, no.402), says so in as many words: after 'phlv. tōxtan, tōžēt «büssen» (übersetzt aw. √kāy- «büssen»), tōž(i)šn «Strafe, Busse»; arm. tvižّ «Einbusse, Strafe»' he writes 'Eine ältere Form ist nicht vorhanden' — no older form is extant — and dismisses Geiger's attempt to attach Av. taoždya- as 'ganz unsicher'. What Nourai's other reference actually gives is a RECONSTRUCTION, not an Avestan word: Abolqāsemi, Feʿl-hā-ye Fārsi-ye Dari p.47 (Nourai's FFD:47) writes 'توخت < فارسی میانه tōxt < ایرانی باستان *tauxta-… ریشهٔ taug به معنی «پرداختن»' and 'توز < فارسی میانه tōz < ایرانی باستان *tauč-a-' — i.e. Old Iranian *taug-/*tauxta- and *tauč-, starred forms. So the node's language label is wrong (Old Iranian reconstruction, not Avestan), and the edge from node #1 (Av. kay- 'to select') is wrong twice over: the Pahlavi verb translates Avestan kāy- 'to atone', which belongs to the OTHER root on this page (Kwei 1, Pok. 636), and Cheung's verdict on *tauǰ3 is 'The origin of the root *tauǰ3 is unknown: it could be identical to *tauǰ2' — no PIE etymon, no LIV entry.\",\n  \"derivation_fa\": \"فعلی به نام taug-/taux- در اوستا وجود ندارد. در فرهنگ ایرانی باستانِ بارتولومه چنین ریشه‌ای نیست (تنها taoxman- «تخم»، taoždya- و tak- «دویدن») و چونگ در مدخل *tauǰ³ «تاوان دادن، وام گزاردن، کفّاره پرداختن» اصلاً بخش «اوستایی» ندارد و از فارسی میانه آغاز می‌کند. هرن نیز در همان صفحه‌ای که نورایی ارجاع داده (صفحهٔ ۹۰، بند ۴۰۲) پس از آوردن «پهلوی tōxtan، tōžēt «کفّاره دادن» (که ترجمهٔ اوستایی kāy- «کفّاره دادن» است)» صریح می‌نویسد: «صورت کهن‌ترى در دست نیست»، و کوششِ گایگر برای پیوند دادن آن به taoždya- اوستایی را «کاملاً نامطمئن» می‌خواند. آنچه مرجع دیگر نورایی می‌دهد نیز صورتی بازسازی‌شده است نه واژه‌ای اوستایی: ابوالقاسمی در «فعل‌های فارسی دری» صفحهٔ ۴۷ می‌نویسد «توخت < فارسی میانه tōxt < ایرانی باستان *tauxta-… ریشهٔ taug به معنی پرداختن» و «توز < فارسی میانه tōz < ایرانی باستان *tauč-a-» — یعنی صورت‌های ستاره‌دار ایرانی باستان. پس برچسب زبانیِ این گره نادرست است و پیکانِ آن از گرهٔ ۱ (kay- اوستایی «برگزیدن») دو خطا دارد: فعل پهلوی ترجمهٔ kāy- اوستایی است که به ریشهٔ دیگرِ همین صفحه تعلق دارد، و خودِ ریشهٔ *tauǰ³ به گفتهٔ چونگ «خاستگاهش ناشناخته است». پژوهش امروزی این گره را رد می‌کند.\",\n  \"sources\": [CHEUNG_TXT, HRN_TXT, BRT_TXT],\n  \"ref_check\": [\n    {\"ref\": \"HRN:90\", \"status\": \"contradicts\",\n     \"note\": \"Horn p.90 (HRN.txt leaf 112), continuation of no.402: 'phlv. tōxtan, tōžēt «büssen» (übersetzt aw. √kāy- «büssen»), tōž(i)šn «Strafe, Busse»; arm. tviž «Einbusse, Strafe»… Eine ältere Form ist nicht vorhanden. Die Grundbedeutung scheint im Neupersischen «sammeln» zu sein. Geiger… will aw. taoždya- (vd. 1, 20) … anschliessen, doch ist dies ganz unsicher.' Horn denies that an older (Avestan) form exists, and the Avestan verb he does name is kāy-, i.e. the root of the previous chart.\"},\n    {\"ref\": \"FFD:47\", \"status\": \"partial\",\n     \"note\": \"Abolqāsemi, Feʿl-hā-ye Fārsi-ye Dari p.47 (FFD_pages.txt pdf page 52) s.v. توختن: 'توخت < فارسی میانه tōxt < ایرانی باستان *tauxta-. … tauxta صورت اصلی taug است، g پیش از t به x بدل شده است. ریشهٔ taug به معنی «پرداختن» [است]. توز < فارسی میانه tōz < ایرانی باستان *tauč-a-'. So FFD does give taug/taux — but as a starred OLD IRANIAN root, never as an attested Avestan word, and with no PIE affiliation.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *tauǰ3 'to (re)pay, pay back…, expiate' (pp.387-388)\", \"stance\": \"contradicts\",\n     \"note\": \"the article lists MMP twz-, BMP twc- /tōz-/, Parth. twj-/twc-, CSogd. twž, Bactrian τωζ-, NP tōxtan/tōz-, Arm. LW tužem, toyž — and NO Avestan; it closes 'The origin of the root *tauǰ3 is unknown: it could be identical to *tauǰ1 [sc. *tauǰ2].' The neighbouring *tauǰ2 'to acquire, gather, gain' is likewise given '*PIE — | LIV: — | Pok.: 1080 ff.'\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae, AiW, t- section\", \"stance\": \"silent\",\n     \"note\": \"no entry taug-, taux- or taok-/tauk- of any kind; the nearest forms are taoxman- 'Same' and taoždya- (Vd 1.19), which Horn expressly refuses to connect.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.95 s.v. tōxtan (NYB_vol2_glossary.txt line 3793)\", \"stance\": \"partial\",\n     \"note\": \"gives the Middle Persian verb and its Parthian and New Persian relatives ('MPrth twj- «to pay, to atone for»… NP tōxtan tōz-, kīn-tōz'), but names no Avestan antecedent.\"}\n  ]\n})\n\nN.append({\n  \"id\": 4, \"lang\": \"Pahlavi\",\n  \"words\": \"tôxtan\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"The Middle Persian verb is well attested and Nourai's gloss is right: Nyberg II 95 'tōxtan [twhtn'] tōž- [twc-] to pay a debt, a fine; to give back, return anything (borrowed): kēn tōzēt he will take his revenge'; Cheung *tauǰ3 gives MMP twz- 'to expiate, pay for', BMP twc- /tōz-/ 'to pay a debt, a fine', 3sg. tōzēd, and beside it *tauǰ2 with NP tōxtan/tōz- 'to acquire, gain, collect' (the sense Horn calls the Grundbedeutung in New Persian). The edge from node #3 is sound on FFD's own terms — Abolqāsemi p.47 derives MP tōxt from Old Iranian *tauxta-, past participle of the root *taug-, with g > x before t, and MP tōz from *tauč-a-, the -č- stem beside the -g- stem — provided one reads node #3 as a reconstructed Old Iranian root rather than an Avestan word. What cannot stand is the position of the whole branch under Kwei 2: neither Cheung nor LIV nor Pokorny attaches *tauǰ to *kʷei-, and Cheung says outright that its origin is unknown.\",\n  \"derivation_fa\": \"این فعل فارسی میانه به‌خوبی گواهی شده و معنایی که نورایی داده درست است: نیبرگ در جلد دوم صفحهٔ ۹۵ می‌آورد «tōxtan [twhtn'] tōz- [twc-] پرداختن وام یا جریمه؛ بازگرداندن چیز عاریتی: kēn tōzēt انتقام خواهد گرفت»، و چونگ ذیل *tauǰ³ صورت‌های فارسی میانهٔ مانوی twz- «کفّاره دادن» و کتابی twc- /tōz-/ «وام و جریمه پرداختن» را ثبت کرده است. پیکان از گرهٔ ۳ به این گره، بنا بر خودِ ابوالقاسمی، درست است: او در صفحهٔ ۴۷ فارسی میانهٔ tōxt را از ایرانی باستان *tauxta- (اسم مفعول ریشهٔ *taug-، با بدل شدن g به x پیش از t) و tōz را از *tauč-a- می‌گیرد — به شرط آنکه گرهٔ ۳ را ریشه‌ای بازسازی‌شدهٔ ایرانی باستان بدانیم نه واژه‌ای اوستایی. آنچه پذیرفتنی نیست جای این شاخه زیر ریشهٔ Kwei 2 است؛ نه چونگ، نه LIV و نه پوکورنی *tauǰ را به *kʷei- نبسته‌اند و چونگ صریح می‌گوید خاستگاه آن ناشناخته است.\",\n  \"sources\": [CHEUNG_TXT, HRN_TXT],\n  \"ref_check\": [\n    {\"ref\": \"HRN:90\", \"status\": \"supports\",\n     \"note\": \"Horn p.90: 'phlv. tōxtan, tōžēt «büssen» … tōž(i)šn «Strafe, Busse»' — the Pahlavi verb and its meaning are exactly Horn's, even though Horn denies it an older ancestor.\"},\n    {\"ref\": \"FFD:47\", \"status\": \"supports\",\n     \"note\": \"'توخت < فارسی میانه tōxt < ایرانی باستان *tauxta-… g پیش از t به x بدل شده است' — Abolqāsemi's MP form and the sound change g > x / _t are exactly this arrow.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II p.95 (NYB_vol2_glossary.txt line 3793)\", \"stance\": \"supports\",\n     \"note\": \"'tōxtan [twhtn'] tōž- [twc-] to pay a debt, a fine; to give back, return anything (borrowed): kēn tōzēt he will take his revenge 4522 … MPrth twj- «to pay, to atone for», Ghilain 63; MPrs twzyšn «penalty, expiation»; Paz. tōxtan tōz-; NP tōxtan tōz-, kīn-tōz.'\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary s.v. tōxtan, tōz-\", \"stance\": \"supports\",\n     \"note\": \"MacKenzie's BMP twc- /tōz-/ 'to pay a debt, a fine; to give back' is quoted verbatim by Cheung (DMMPP: 331a) — the local PHD OCR is defective at this leaf, so the reading is taken from Cheung's citation of it.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 *tauǰ3 and *tauǰ2, pp.387-388\", \"stance\": \"partial\",\n     \"note\": \"confirms the Middle Persian verb but detaches it from any PIE root: '*PIE — | LIV: — | Pok.: 1080 ff.' for *tauǰ2 and 'The origin of the root *tauǰ3 is unknown' for *tauǰ3.\"}\n  ]\n})\n\nN.append({\n  \"id\": 5, \"lang\": \"Persian\",\n  \"words\": \"tozîdan\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"The Persian words are all real and the link to Pahlavi tōxtan/tōz- is uncontroversial. The primary New Persian verb is توختن tōxtan with present stem توز tōz- ('to pay a debt; to gain, collect'); توزیدن tōzīdan is the regular secondary infinitive built on that present stem (Steingass 335 'to pay; to gain, collect; to draw, spread'), and توز tōz is the bare stem used as a noun. کینه‌توز kīne-tūz 'vengeful, one who takes revenge' is kīn(e) + tōz-, and it is the very compound Horn quotes at this entry ('kīne-tōz «Vergeltung»', Is. 34,11; 35,4) and Nyberg gives as 'NP tōxtan tōz-, kīn-tōz'. Nourai's Ferdowsi shāhed, 'چو وامش بتوزی درم صد هزار / بده تا بدارد ز ما یادگار', is the same verse Abolqāsemi prints under this entry on FFD p.47. Note that the compound کینه‌توز actually joins the two charts of this page: کین belongs to Kwei 1 (Av. kaēnā-) and توز to the unattached Iranian root *tauǰ, so neither half is from Kwei 2.\",\n  \"derivation_fa\": \"واژه‌های فارسی این گره همه واقعی‌اند و پیوندشان با پهلوی tōxtan/tōz- محل بحث نیست. مصدر اصلی در فارسی نو «توختن» با ستاک حال «توز-» است («وام گزاردن؛ به دست آوردن، گرد کردن») و «توزیدن» مصدر ثانویِ قاعده‌مندی است که بر همان ستاک حال ساخته شده (استینگاس ص ۳۳۵)، و «توز» همان ستاک است که اسم شده. «کینه‌توز» از کین(ه) + توز- است و همان ترکیبی است که هرن در بند ۴۰۲ می‌آورد و نیبرگ نیز «NP tōxtan tōz-, kīn-tōz» ثبت کرده است. بیتِ شاهدِ نورایی از فردوسی («چو وامش بتوزی درم صد هزار / بده تا بدارد ز ما یادگار») همان بیتی است که ابوالقاسمی در صفحهٔ ۴۷ ذیل همین مدخل نقل کرده. نکتهٔ خواندنی آنکه «کینه‌توز» درست دو نمودار این صفحه را به هم می‌دوزد: «کین» از ریشهٔ نخست (kaēnā- اوستایی) است و «توز» از ریشهٔ ایرانیِ بی‌نسبِ *tauǰ؛ پس هیچ‌کدام از ریشهٔ دوم نیست.\",\n  \"sources\": [CHEUNG_TXT, HRN_TXT, ST_TOZ],\n  \"ref_check\": [\n    {\"ref\": \"HRN:90\", \"status\": \"supports\",\n     \"note\": \"Horn no.402 (p.89, HRN.txt leaf 111): 'tōxten «sammeln; ausgeben, zahlen», Praes. tōz-em; kīne-tōz «Vergeltung» (Is. 34,11; 35,4)' — the New Persian verb, its present stem and the compound کینه‌توز, all as in the chart.\"},\n    {\"ref\": \"FFD:47\", \"status\": \"supports\",\n     \"note\": \"'توز < فارسی میانه tōz < ایرانی باستان *tauč-a-… در فارسی میانه به معنی «پرداختن» و «توبه و جبران کردن» است. در فارسی دری به معنی «فرو کردن و کشیدن و پرداختن» آمده است. شاهنامه: چو وامش بتوزی درم صد هزار / بده تا بدارد زما یادگار' — Abolqāsemi prints the same Ferdowsi verse Nourai quotes.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 *tauǰ3, NWIR section (p.388)\", \"stance\": \"supports\",\n     \"note\": \"'NP tōxtan/tōz- «to pay a debt, return anything borrowed» || (+ *ham-) NP andōxtan/andōz- «to collect a debt»'.\"},\n    {\"src\": \"NYB\", \"where\": \"Nyberg II 95 s.v. tōxtan\", \"stance\": \"supports\",\n     \"note\": \"'NP tōxtan tōz-, kīn-tōz «bellicose, one who foments dissension and lawsuits»'.\"},\n    {\"src\": \"ARY\", \"where\": \"Aryanpur, Farhang-e Riše-hā-ye Hend-o-Orupāyi (ARY_pages.txt / ARY_latin_index_pages.txt)\", \"stance\": \"silent\",\n     \"note\": \"greps for توختن / توزیدن / TUXTAN / TOXTAN in both the Persian and the Latin index files return nothing usable — the OCR of this book is too poor at these headwords to yield a reading.\"}\n  ]\n})\n\nN.append({\n  \"id\": 6, \"lang\": \"Old Persian\",\n  \"words\": \"sâ 1; fra-sâ\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"Nourai's citation is exact — Kent, Old Persian, Lexicon p.209 reads 'sā- vb. «erect, build»: probably from pIE *ḱu̯ā-, Av. spā- «throw, throw away, set down», Ars. Phl. pari-sp «wall» (§90; Bv. Gr. §113, cf. König, Burgbau 49-50; wrongly Bv. BSLP 30.1.66-7). fra- + sā- «erect, build»: frāsah[ya] s-aor. pass. (§218.I, §220) DSf 27' — so both words, both glosses and the connection with Av. spā- and Phl. pari-sp are Kent's, on precisely the cited page. What is not Kent's is the attachment to *kʷei-. Kent derives sā- from PIE *ḱu̯ā-, a palatal *ḱ plus *u̯; his §90 sets up the correspondence Median sp : Old Persian s : Sanskrit h/ś for that cluster (as in aspa-/asa- 'horse' < *eḱu̯o-, vispa-/visa- 'all' < *u̯iḱu̯o-) and flags the etymology as uncertain. A labiovelar *kʷ, by contrast, gives Old Persian k or c, never s: the two cannot be the same root. The Old Persian verb is besides very thinly attested — the whole thing rests on the single damaged form frāsah[ya] at DSf 27, for which Kent himself offers the alternative 1sg. act. frāsaha[m], and Cheung's Etymological Dictionary of the Iranian Verb recognises no Iranian root of this shape. (Note that OP frašam 'excellent' at DSa 5 / DSj 6 is a different word, from fra- + *arč-.)\",\n  \"derivation_fa\": \"ارجاع نورایی دقیق است: کنت در فرهنگ پارسی باستان صفحهٔ ۲۰۹ می‌نویسد «sā- فعل «برافراشتن، ساختن»: احتمالاً از هندواروپایی *ḱu̯ā-، اوستایی spā- «انداختن، دور انداختن، فرو نهادن»، پهلویِ اشکانی pari-sp «دیوار»… fra- + sā- «برافراشتن، ساختن»: frāsah[ya] در کتیبهٔ DSf سطر ۲۷». پس هر دو واژه، هر دو معنا و پیوند با spā- اوستایی و parisp پهلوی از خودِ کنت است و در همان صفحه. امّا آنچه از کنت نیست، بستنِ این‌ها به ریشهٔ *kʷei- است: کنت آن را از *ḱu̯ā- می‌گیرد، یعنی همخوان کامی‌شدهٔ *ḱ به‌علاوهٔ *u̯، و در بند ۹۰ همان کتاب برابری «مادیِ sp : پارسی باستانِ s : سنسکریتِ ś/h» را برای این خوشه می‌نشاند (چنان‌که aspa-/asa- «اسب» و vispa-/visa- «همه»)، و خود آن را «قطعی نه» می‌خواند. حال آنکه *kʷ لبی‌کامی در پارسی باستان k یا c می‌دهد نه s؛ این دو نمی‌توانند یک ریشه باشند. افزون بر این، فعل پارسی باستان بسیار کم‌گواه است و همهٔ آن بر یک صورتِ آسیب‌دیده در کتیبهٔ داریوش در شوش استوار است که خودِ کنت خوانش دیگری هم برایش پیشنهاد می‌کند. پژوهش امروزی این پیوند را نمی‌پذیرد.\",\n  \"sources\": [KENT_TXT, KENT_TXT2, CHEUNG_TXT],\n  \"ref_check\": [\n    {\"ref\": \"KNT:209\", \"status\": \"partial\",\n     \"note\": \"Kent p.209 (verified against the page image, archive.org oldpers leaf n224, running head 'LEXICON 209'): 'sā- vb. «erect, build»: probably from pIE *ḱu̯ā-, Av. spā- «throw, throw away, set down», Ars. Phl. pari-sp «wall» (§90…). fra- + sā- «erect, build»: frāsah[ya] s-aor. pass. (§218.I, §220) DSf 27 (1st sg. act. frāsaha[m] is possible…).' The forms and glosses are Kent's exactly; the PIE root Kent gives is *ḱu̯ā-, not *kʷei-, so the reference supports the node but contradicts its placement under this root.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KNT\", \"where\": \"Kent, Old Persian, Lexicon p.209 and §90\", \"stance\": \"partial\", \"note\": \"quoted above; §90 is the Med. sp : OP s : Skt. ś/h correspondence, with Kent's own caveat that the etymology is not certain.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 (Iranian verbal roots in s-/sp-)\", \"stance\": \"silent\",\n     \"note\": \"no root *saH-/*spaH- 'to build, erect' is recognised; Cheung's only *spaH is 'to satisfy, eat one's fill'. The Old Persian hapax is not treated.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 637-638, kʷei-2\", \"stance\": \"silent\",\n     \"note\": \"Pokorny's entry contains no Old Persian material at all — no sā-, no fra-sā-; the node has no support from the root's own article.\"},\n    {\"src\": \"TLM\", \"where\": \"Tolman, Ancient Persian Lexicon\", \"stance\": \"silent\",\n     \"note\": \"Tolman's lexicon (1908) predates the Susa foundation charter reading on which Kent's sā- rests and has no such entry.\"}\n  ]\n})\n\nN.append({\n  \"id\": 7, \"lang\": None,\n  \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": \"An empty box, empty in the printed book too: the render of pdf p.289 (200 dpi, copied to data/verification/sources/refs/ocr/BOOK/289.png) shows a wide blank double-ruled rectangle to the right of the 'Old Persian sâ 1 / fra-sâ' box, joined to it by an arrow, with no language header, no reference and no word. Nothing to verify. Nourai's habit elsewhere is to leave such a box where he expected a Persian or English continuation and found none — here presumably a New Persian reflex of OP fra-sā-, which does not exist.\",\n  \"derivation_fa\": \"جعبه‌ای خالی است و در خودِ کتاب هم خالی است: در تصویر صفحهٔ ۲۸۹ (که در data/verification/sources/refs/ocr/BOOK/289.png نگهداری شده) مستطیلی دوخطّه و تهی در سمت راست جعبهٔ «پارسی باستان sâ 1 / fra-sâ» دیده می‌شود که با پیکانی به آن پیوسته است، بی هیچ نام زبان، ارجاع یا واژه. چیزی برای راستی‌آزمایی نیست. عادت نورایی در جاهای دیگر همین است که چنین جعبه‌ای را آنجا خالی می‌گذارد که انتظار دنبالهٔ فارسی یا انگلیسی داشته و نیافته است؛ اینجا احتمالاً بازماندهٔ فارسیِ fra-sā- را می‌جسته که وجود ندارد.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the printed book.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"pdf page 289 rendered at 200 dpi (data/verification/sources/refs/ocr/BOOK/289.png)\", \"stance\": \"silent\", \"note\": \"the box is blank on the page; the extraction (lang null, words []) is faithful.\"}]\n})\n\nN.append({\n  \"id\": 8, \"lang\": \"Avestan\",\n  \"words\": \"spâ 2\",\n  \"verdict\": \"disputed\",\n  \"derivation\": \"The Avestan verb is real: Bartholomae, AiW, has 'j. ¹spā- V. «iacere», «abicere». Praes. 17 spaya-, s-Aor. 1 spāš-. — PPfP. spāta-', with the compounds apa-spā- 'abwerfen, ablegen, exuere' (Yt 19.80 maγnā apa.spayaṱ vastrā 'naked he was, he had thrown off his clothes'), aipi-spā-, upairi-spā-, para-spā- 'fortschleudern' (Yt 10.37) and frā-spā- 'zu Boden werfen' (Yt 10.43), plus the noun pairi.spātay- f. 'Herumwerfen, Hinwerfen' (V 6.29). So 'throw away' is exactly Bartholomae's 'abicere'; Nourai's '2' is his own homonym number, not Bartholomae's (Bartholomae's ¹spā- is the 'throw' verb, ²spā- 'proficere', ³spā- n. 'Gedeihen'). What is wrong is again the parentage: this is Kent's comparandum for OP sā- < PIE *ḱu̯ā- (Old Persian p.209, §90), a palatal cluster, and it cannot be a reflex of the labiovelar *kʷei-. Pokorny's kʷei-2 article names no Avestan spā- at all, and Cheung has no Iranian verbal root of this shape and meaning.\",\n  \"derivation_fa\": \"فعل اوستایی واقعی است: بارتولومه در فرهنگ ایرانی باستان می‌آورد «j. ¹spā- فعل «iacere»، «abicere» [انداختن، دور انداختن]، مضارع spaya-، اسم مفعول spāta-» با ترکیب‌هایی چون apa-spā- «به دور افکندن، جامه از تن کندن» (یشت ۱۹٫۸۰: «برهنه بود، جامه‌ها را افکنده بود»)، para-spā- «به دور پرتاب کردن» (یشت ۱۰٫۳۷) و frā-spā- «بر زمین زدن» (یشت ۱۰٫۴۳)، و نیز اسمِ pairi.spātay- «پیرامون افکندن، فرو افکندن» (وندیداد ۶٫۲۹). پس «دور انداختن» دقیقاً همان abicere بارتولومه است؛ شمارهٔ «۲» از آنِ نورایی است نه بارتولومه (نزد بارتولومه ¹spā- همین فعلِ «انداختن» است). امّا نسبِ گره باز نادرست است: این همان صورتی است که کنت در صفحهٔ ۲۰۹ برای مقایسه با sā- پارسی باستان آورده و آن را از *ḱu̯ā- کامی‌شده می‌گیرد، و چنین خوشه‌ای نمی‌تواند بازتاب *kʷ لبی‌کامی باشد. در مقالهٔ kʷei-2 پوکورنی هیچ spā- اوستایی نیست و چونگ نیز ریشهٔ فعلیِ ایرانی به این صورت و معنا ندارد.\",\n  \"sources\": [BRT_TXT, KENT_TXT, KENT_TXT2],\n  \"ref_check\": [\n    {\"ref\": \"KNT:209\", \"status\": \"partial\",\n     \"note\": \"Kent p.209 s.v. sā- cites 'Av. spā- «throw, throw away, set down»' — the form and gloss are Kent's, but Kent's PIE ancestor for the group is *ḱu̯ā-, not *kʷei-, and §90 marks the etymology as uncertain.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.v. ¹spā- (BRT.txt line 26904) and pairi.spātay- (line 15622)\", \"stance\": \"supports\",\n     \"note\": \"'j. ¹spā- V. «iacere», «abicere». Praes. 17 spaya-, s-Aor. 1 spāš-. — PPfP. spāta-'; 'j. pairi.spātay- f. «Herumwerfen, Hinwerfen, Hin(ein)fallenlassen»'. Bartholomae's Pahlavi gloss for the verb is afgandan.\"},\n    {\"src\": \"POK\", \"where\": \"IEW 637-638\", \"stance\": \"silent\",\n     \"note\": \"no Avestan spā- anywhere in the kʷei-2 article.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007, sp- roots\", \"stance\": \"silent\",\n     \"note\": \"the only *spaH in Cheung is 'to satisfy, eat one's fill'; the 'throw' verb is not treated (it is nominal-derivative material rather than a productive Middle/New Iranian verb).\"}\n  ]\n})\n\nN.append({\n  \"id\": 9, \"lang\": \"Pahlavi\",\n  \"words\": \"pari-sp\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Middle Persian parisp 'wall' is securely attested and its derivation from pari- + spā- is the standard one. MacKenzie's addenda to the Concise Pahlavi Dictionary add the entry outright: 'parisp [plsp | M prysp] wall.' Nyberg, Manual of Pahlavi II, gives the etymology in full: 'parisp [plsp'], with indef. art. -ē [~-'y] wall 114.21. — OIr *pari-spā- from pari + Av. (1615 sq.) ¹spā- «to throw», cf. pargān; MPrthPrs prysp; Arm. lw. parisp' — and his cross-reference pargān [plgʾn'] 'wall' < *pari-kāna- 'that which is thrown up all around' shows the same semantic pattern with a different verb of throwing. Bartholomae's Avestan noun pairi.spātay- 'a throwing around' is the direct formal parallel. The word was borrowed into Armenian as պարիսպ parisp 'city wall' (5th c.). So the edge #8 → #9, 'Avestan spā- «throw» → Pahlavi pari-sp «wall (built around)»', is exactly right; only the position of the whole cluster under Kwei 2 is not (see nodes #6 and #8).\",\n  \"derivation_fa\": \"«پریسپ» فارسی میانه به معنی «دیوار» به‌خوبی گواهی شده و گرفتن آن از pari- + spā- همان تحلیل معیار است. مکنزی در ملحقات فرهنگ کوچک پهلوی مدخل را می‌افزاید: «parisp [plsp | مانوی prysp] دیوار». نیبرگ در جلد دوم دستور پهلوی ریشه را کامل می‌دهد: «parisp دیوار … از ایرانی باستان *pari-spā-، از pari به‌علاوهٔ ¹spā- اوستایی «انداختن» (بارتولومه ستون ۱۶۱۵)؛ پارتی و فارسی میانهٔ مانوی prysp؛ وام‌واژهٔ ارمنی parisp»؛ و ارجاع او به pargān «دیوار» از *pari-kāna- «آنچه گرداگرد بالا ریخته شده» همان الگوی معنایی را با فعلِ انداختنِ دیگری نشان می‌دهد. اسم اوستاییِ pairi.spātay- «پیرامون افکندن» نزد بارتولومه همتای صوری مستقیم آن است. این واژه در سدهٔ پنجم میلادی به ارمنی هم رفته است: պարիսպ «باروی شهر». پس پیکان از گرهٔ ۸ به ۹ کاملاً درست است؛ تنها جای این خوشه زیر ریشهٔ Kwei 2 نادرست است.\",\n  \"sources\": [KENT_TXT, W + \"%D5%BA%D5%A1%D6%80%D5%AB%D5%BD%D5%BA\"],\n  \"ref_check\": [\n    {\"ref\": \"KNT:209\", \"status\": \"supports\",\n     \"note\": \"Kent p.209 s.v. sā- ends '…Ars. Phl. pari-sp «wall» (§90; Bv. Gr. §113, cf. König, Burgbau 49-50)'. Nourai's word, hyphenation and gloss 'wall (built around)' are Kent's.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"NYB\", \"where\": \"Nyberg, Manual of Pahlavi II s.v. parisp (NYB_vol2_glossary.txt line 2959)\", \"stance\": \"supports\",\n     \"note\": \"'parisp [plsp'], with indef. art. -ē [~-'y] wall 114.21. — OIr *pari-spā- from pari + Av. (1615 sq.) ¹spā- «to throw», cf pargān; MPrthPrs prysp; Arm. lw. parisp.' Line 2953 s.v. pargān gives the parallel '< *pari-kāna- «that which is thrown up all around»'.\"},\n    {\"src\": \"PHD\", \"where\": \"MacKenzie, Concise Pahlavi Dictionary, addenda (PHD.txt line 130; PHD_mackenzie.txt line 599)\", \"stance\": \"supports\",\n     \"note\": \"'add parisp [plsp | M prysp] wall.'\"},\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW s.v. pairi.spātay- (BRT.txt line 15622)\", \"stance\": \"supports\",\n     \"note\": \"'j. pairi.spātay- f. «Herumwerfen, Hinwerfen, Hin(ein)fallenlassen»' — the Avestan nominal formation on pari- + spā- that matches parisp.\"}\n  ]\n})\n\nN.append({\n  \"id\": 10, \"lang\": None,\n  \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": \"A second empty box, blank on the printed page as well: on the render of pdf p.289 a plain double-ruled rectangle stands to the right of the 'Pahlavi pari-sp' box, joined by an arrow, with no language header, no reference and no word. Nothing to verify. The obvious candidate for what Nourai left out is New Persian پاسب/پاسپ or the Armenian loan parisp; the ☞Per 1 pointer on the pari-sp box already sends the reader to another chart.\",\n  \"derivation_fa\": \"دومین جعبهٔ خالی، که در صفحهٔ چاپی نیز تهی است: در تصویر صفحهٔ ۲۸۹ مستطیلی دوخطّه و بی‌نام در سمت راست جعبهٔ «پهلوی pari-sp» دیده می‌شود که با پیکانی به آن پیوسته است، بی هیچ نام زبان، ارجاع یا واژه. چیزی برای راستی‌آزمایی نیست. آنچه احتمالاً باید در آن می‌آمد دنبالهٔ فارسی نو یا وام‌واژهٔ ارمنیِ parisp بوده است؛ نشانهٔ ☞Per 1 روی جعبهٔ pari-sp نیز خواننده را به نمودار دیگری می‌فرستد. خطای خوانش اسکن در کار نیست؛ استخراج وفادار است.\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the printed book.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"pdf page 289 rendered at 200 dpi (data/verification/sources/refs/ocr/BOOK/289.png)\", \"stance\": \"silent\", \"note\": \"the box is blank on the page; the extraction (lang null, words []) is faithful.\"}]\n})\n\nN.append({\n  \"id\": 11, \"lang\": \"Avestan\",\n  \"words\": \"kaěš; fra-kaěš, vi-kaěš\",\n  \"verdict\": \"plausible\",\n  \"derivation\": \"Nourai copies his source exactly. Pokorny closes the kʷei-2 article (p.638) with 'Eine s-Weiterbildung in av. kaēš- (mit Präverbien) «struere», frā- «zurichten, bereiten», vī- «zu-, herrichten» (Bartholomae Wb. 429)', and Bartholomae AiW col.429 does have 'j. ¹kaēš- V. «struere»; nur mit Praev. Praes. 2 caēša-, … (Iter.) caēšaiia-', with a separate ²kaēš- 'lehren' following. So the forms, the preverbs and the glosses 'make / prepare, arrange' are all in the cited page, and 'struere' is indeed 'to pile up, build'. The caveat is that this equation has not survived: LIV and Cheung recognise a single root *čaiš / *kaiš 'to assign, make known, teach' (Av. čiš-, tkaēša- 'teaching', + para-/fra-; MMP qys- 'to teach', BMP kēš 'faith, religion' > NP کیش kēš), from PIE *kʷeis- 'to observe, see' — i.e. the s-extension of the OTHER kʷei- (the perceiving one, Pokorny 636 f., with OIr. ad-cí 'sees'), not of *kʷei- 'to pile up'. Under that analysis Bartholomae's two kaēš- are one verb and belong on the previous chart, not this one.\",\n  \"derivation_fa\": \"نورایی اینجا منبع خود را بی‌کم‌وکاست رونویسی کرده است. پوکورنی مقالهٔ kʷei-2 را در صفحهٔ ۶۳۸ چنین می‌بندد: «گسترشِ s-داری در اوستایی kaēš- (با پیشوندها) «struere [روی هم چیدن، ساختن]»، با frā- «آماده کردن، فراهم آوردن»، با vī- «مرتب کردن» (بارتولومه ص ۴۲۹)»؛ و بارتولومه نیز در ستون ۴۲۹ «j. ¹kaēš- فعل «struere»؛ تنها با پیشوند» را دارد و ²kaēš- «آموزاندن» را جدا. پس صورت‌ها، پیشوندها و معناها همه در همان صفحهٔ ارجاع‌شده هست. امّا این برابری در پژوهش امروزی نمانده است: LIV و چونگ یک ریشهٔ واحد *čaiš/*kaiš «برنهادن، شناساندن، آموزاندن» می‌شناسند (اوستایی čiš-، tkaēša- «آموزه»؛ فارسی میانهٔ مانوی qys- «آموزاندن»، کتابی kēš «دین» که «کیش» فارسی از آن است) و آن را از هندواروپایی *kʷeis- «دیدن، دریافتن» می‌گیرند، یعنی گسترشِ s-دارِ ریشهٔ دیگر (پوکورنی ۶۳۶ به بعد) نه این ریشه. بنابراین ادعای نورایی با احتیاط پذیرفتنی است: با منبعش می‌خواند، امّا با رأی امروز نه.\",\n  \"sources\": [POK2, POK1, BRT_TXT, CHEUNG_TXT],\n  \"ref_check\": [\n    {\"ref\": \"POK:637\", \"status\": \"supports\",\n     \"note\": \"IEW 638 (the second page of the kʷei-2 article, POK_02.txt leaf 298): 'Eine s-Weiterbildung in av. kaēš- (mit Präverbien) «struere», frā- «zurichten, bereiten», vī- «zu-, herrichten» (Bartholomae Wb. 429).' Nourai's node is this sentence turned into a box.\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"BRT\", \"where\": \"Bartholomae AiW col.429 (BRT.txt lines 8924, 8929)\", \"stance\": \"supports\",\n     \"note\": \"'j. ¹kaēš- V. «struere»; nur mit Praev. Praes. 2 caēša-, 5 [caēš-], 30 (Iter.) caēšaiia-'; immediately after, 'j., g. ²kaēš- V. «lehren». Praes. 1 …' — the very column Pokorny cites.\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 s.v. *čaiš / *kaiš 'to assign, make known, teach'\", \"stance\": \"contradicts\",\n     \"note\": \"Cheung recognises only one root of this shape and derives it from PIE *kʷeis- 'to observe, see' (LIV 381), with MMP qys- 'to teach', BMP kēš 'faith, religion' > NP kēš; there is no *kaiš 'to pile up, build' in his dictionary.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, kʷei-2\", \"stance\": \"silent\",\n     \"note\": \"Watkins lists no Avestan material under kʷei-2 at all, so nothing bears on kaēš-.\"}\n  ]\n})\n\nN.append({\n  \"id\": 12, \"lang\": None,\n  \"words\": \"\",\n  \"verdict\": \"unverified\",\n  \"derivation\": \"The third empty box on this chart, blank in the book as well: on the render of pdf p.289 a plain rectangle stands to the right of the 'Avestan kaěš / fra-kaěš, vi-kaěš' box, joined by an arrow, with no language header, no reference and no word. Nothing to verify. Had it been filled, the natural continuation would have been Middle Persian kēš > New Persian کیش 'religion, creed' — which is exactly the descendant that belongs to Cheung's *čaiš, i.e. to the other root (see node #11).\",\n  \"derivation_fa\": \"سومین جعبهٔ خالی این نمودار که در کتاب نیز تهی است: در تصویر صفحهٔ ۲۸۹ مستطیلی ساده در سمت راست جعبهٔ «اوستایی kaěš / fra-kaěš، vi-kaěš» دیده می‌شود که با پیکانی به آن پیوسته است، بی نام زبان، بی ارجاع و بی واژه. چیزی برای راستی‌آزمایی نیست. اگر پر می‌شد، دنبالهٔ طبیعی آن فارسی میانهٔ kēš و فارسی نوِ «کیش» (دین، آیین) بود — و همان بازمانده‌ای است که چونگ آن را به ریشهٔ *čaiš یعنی ریشهٔ دیگر می‌بندد (نگاه کنید به گرهٔ ۱۱).\",\n  \"sources\": [],\n  \"ref_check\": [{\"ref\": \"None\", \"status\": \"not_checked\", \"note\": \"the box carries no reference in the printed book.\"}],\n  \"consulted\": [{\"src\": \"BOOK\", \"where\": \"pdf page 289 rendered at 200 dpi (data/verification/sources/refs/ocr/BOOK/289.png)\", \"stance\": \"silent\", \"note\": \"the box is blank on the page; the extraction (lang null, words []) is faithful.\"}]\n})\n\nN.append({\n  \"id\": 13, \"lang\": \"Greek\",\n  \"words\": \"poiein\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Ancient Greek ποιέω poiéō, inf. ποιεῖν poieîn 'to make, produce, create; (later) to compose poetry'. Pokorny states it on the cited page: 'gr. ποιέω «mache» (arg.-böot. ἐποίϝησε u. dgl.), dann auch «dichte», Denominativ eines *ποι-ϝό-ς «aufbauend, machend» (vgl. ἀρτο-ποιός «Bäcker»)' — i.e. the verb is denominative from an o-grade *kʷoi-wo- 'making', which is why Nourai's root box carries the second name 'Kwoi'. The digamma is guaranteed by the Argive/Boeotian ἐποίϝησε. Watkins/AHD has the same: 'suffixed form *kʷoi-wo-, making, in denominative verb *kʷoiw-eyo- in Greek poiein, to make, create'. Cheung lists Gr. ποιέω and OCS činiti as the Indo-European cognates of Iranian *čai1. The chart is right to hang Greek off the root rather than off the Avestan node: ποιέω is a cognate of Av. čay-, not a descendant of it.\",\n  \"derivation_fa\": \"یونانی باستان ποιέω (مصدر ποιεῖν) «ساختن، پدید آوردن، آفریدن» و در کاربرد پسین‌تر «شعر سرودن». پوکورنی در همان صفحه می‌آورد: «یونانی ποιέω «می‌سازم» (در آرگوسی-بئوتیایی ἐποίϝησε) و سپس «شعر می‌گویم»، فعلِ برساخته از *ποι-ϝό-ς «سازنده، بناکننده» (سنجیدنی با ἀρτο-ποιός «نانوا»)» — یعنی فعل از صورت اسمیِ درجهٔ o یعنی *kʷoi-wo- «سازنده» ساخته شده است، و همین است که نام دوم جعبهٔ ریشه، «Kwoi»، را توجیه می‌کند. وجود واکِ ϝ (دیگاما) را صورت آرگوسی ἐποίϝησε تضمین می‌کند. واتکینز نیز همین را دارد و چونگ ποιέω یونانی و činiti اسلاوی کهن را هم‌ریشه‌های هندواروپاییِ *čai¹ ایرانی می‌شمارد. شکل درختِ نورایی درست است: یونانی را از خودِ ریشه گرفته نه از گرهٔ اوستایی، چون ποιέω هم‌ریشهٔ čay- است نه فرزندِ آن. ادعای نورایی درست است.\",\n  \"sources\": [POK2, AHD, W + \"%CF%80%CE%BF%CE%B9%CE%AD%CF%89\"],\n  \"ref_check\": [\n    {\"ref\": \"AHD\", \"status\": \"supports\",\n     \"note\": \"Watkins 1985 s.v. kʷei-2: 'b. suffixed form *koi-wo-, making, in denominative verb *kʷoiw-eyo- in Greek poiein, to make, create: POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATOPOEIA, PHARMACOPOEIA, PROSOPOPEIA. [Pok. 2. kʷei- 637.]'\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"POK\", \"where\": \"IEW 637 (POK_02.txt leaf 298)\", \"stance\": \"supports\",\n     \"note\": \"'gr. ποιέω «mache» … dann auch «dichte», Denominativ eines *ποι-ϝό-ς «aufbauend, machend» (vgl. ἀρτο-ποιός «Bäcker»)'.\"},\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. poet (p.1206-9)\", \"stance\": \"supports\",\n     \"note\": \"'…fr. ποιεῖν, «to make», fr. I.-E. base *qwei-, «to make», whence also OI. cinóti, cáyati, «gathers, heaps up, piles up», citíḥ, «heaping up, piling up», OSlav. činŭ, «act, deed, order», činiti, «to arrange, put in order».'\"},\n    {\"src\": \"CHEUNG\", \"where\": \"Cheung 2007 *čai1, IE COGNATES\", \"stance\": \"supports\",\n     \"note\": \"'*IE COGNATES: Gr. ποιέω «I make, produce, compose», OCS činiti «to arrange»'.\"}\n  ]\n})\n\nN.append({\n  \"id\": 14, \"lang\": \"English\",\n  \"words\": \"poem, poet\",\n  \"verdict\": \"confirmed\",\n  \"derivation\": \"Both words reach English through Latin from Greek — the arrow #13 → #14 passes over Latin and French, which are the real intermediaries. poet: ME poete, from Old French poete (12c.), from Latin poēta, from Greek ποιητής poiētḗs 'one who makes, an artificer, a poet', agent noun to ποιεῖν. poem: from Middle French poème, from Latin poēma, from Greek ποίημα poíēma 'something made; a composition in verse', the -ma abstract to the same verb. Klein s.v. poet gives the whole chain and traces it 'fr. I.-E. base *qwei-, «to make»', which is precisely Nourai's root; Watkins/AHD lists POEM, POESY, POET, POETIC under kʷei-2. The box carries no reference in the book, but AHD (cited on the Greek box above it) covers it.\",\n  \"derivation_fa\": \"هر دو واژه از راه لاتینی و از یونانی به انگلیسی رسیده‌اند؛ پیکانِ نمودار از یونانی یکراست به انگلیسی می‌رود و حلقه‌های لاتینی و فرانسوی را ناگفته می‌گذارد. poet: انگلیسی میانه poete از فرانسهٔ باستان poete (سدهٔ دوازدهم) از لاتینی poēta از یونانی ποιητής «سازنده، صنعتگر، شاعر» که اسم فاعلِ ποιεῖν است. poem: از فرانسوی میانه poème از لاتینی poēma از یونانی ποίημα «ساخته‌شده؛ سرودهٔ منظوم» که اسم مصدرِ ‎-ma‎ دارِ همان فعل است. کلاین همهٔ این زنجیره را می‌آورد و آن را «از ریشهٔ هندواروپایی *qwei- «ساختن»» می‌گیرد، یعنی همان ریشهٔ نورایی، و واتکینز نیز POEM و POESY و POET و POETIC را ذیل *kʷei-2 فهرست کرده است. جعبه در کتاب ارجاعی ندارد، امّا ارجاع AHD روی جعبهٔ یونانیِ بالای آن پوشش‌دهندهٔ آن است. ادعای نورایی درست است.\",\n  \"sources\": [AHD, \"https://www.etymonline.com/word/poet\", \"https://www.etymonline.com/word/poem\"],\n  \"ref_check\": [\n    {\"ref\": \"None\", \"status\": \"not_checked\",\n     \"note\": \"the English box on this chart carries no reference of its own in the printed book; the AHD citation on the Greek box immediately to its left covers the chain (Watkins kʷei-2: POEM, POESY, POET…).\"}\n  ],\n  \"consulted\": [\n    {\"src\": \"KLN\", \"where\": \"Klein 1966 s.v. poem and poet (p.1206-9)\", \"stance\": \"supports\",\n     \"note\": \"'poem, n. — MF. poème (F. poème), fr. L. poema, fr. Gk. ποίημα, «something done; a composition in verse, poem», from the stem of ποιεῖν, «to make»'; 'poet, n. — ME. poete, fr. OF. poete (F. poète), fr. L. poeta, fr. Gk. ποιητής, «one who makes, an artificer, a poet», fr. ποιεῖν, «to make», fr. I.-E. base *qwei-, «to make»'.\"},\n    {\"src\": \"AHD\", \"where\": \"Watkins 1985, kʷei-2 and index (MYTHOPOEIC kʷei-2, PHARMACOPOEIA kʷei-2)\", \"stance\": \"supports\",\n     \"note\": \"'POEM, POESY, POET, POETIC, -POIESIS, -POIETIC; MYTHOPOEIC, ONOMATOPOEIA, PHARMACOPOEIA, PROSOPOPEIA' under kʷei-2.\"},\n    {\"src\": \"SKT\", \"where\": \"Skeat, Concise Etymological Dictionary, s.v. POEM\", \"stance\": \"silent\",\n     \"note\": \"the local OCR of Skeat at 'POEM' (SKT.txt line 14303) is a garbled block of unrelated text (plait/pleach entries) and yields nothing readable.\"}\n  ]\n})\n\njson.dump(e, io.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289/e1.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint(\"ok\", len(N))\nPYEOF\npython3 /tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289/e1.py"
}
```


### [2026-09-06T22:25:19.100Z] TOOL RESULT

```
ok 14
```


## [2026-09-06T22:25:31.878Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe\npython3 - <<'EOF'\nimport json, io, os\nbase='/tmp/claude-1000/-home-sfmqrb-git-rishe/b3fc9033-a4ae-4052-ab02-8a5f609ee6da/scratchpad/p289/'\ne0=json.load(open(base+'e0.json')); e1=json.load(open(base+'e1.json'))\n# de-duplicate ref_check entries in e1 node 2\nfor n in e1['nodes']:\n    seen=set(); out=[]\n    for rc in n.get('ref_check',[]):\n        k=(rc['ref'],rc['status'])\n        if k in seen: continue\n        seen.add(k); out.append(rc)\n    n['ref_check']=out\ndoc={\"pdf_page\":289,\"book_page\":259,\"verified_by\":\"claude-opus-5\",\"verified_on\":\"2026-09-06\",\"entries\":[e0,e1]}\njson.dump(doc, io.open('data/verification/page-289.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint('written')\n# check archived urls\nidx=set()\nfor line in open('data/verification/sources/web/index.jsonl',encoding='utf-8'):\n    try: idx.add(json.loads(line).get('url'))\n    except: pass\ndef urls(o):\n    out=[]\n    if isinstance(o,dict):\n        for k,v in o.items():\n            if k=='sources' and isinstance(v,list): out+= [x for x in v if isinstance(x,str)]\n            else: out+=urls(v)\n    elif isinstance(o,list):\n        for v in o: out+=urls(v)\n    return out\nmissing=sorted(set(u for u in urls(doc) if u not in idx))\nprint('MISSING FROM ARCHIVE:', len(missing))\nfor m in missing: print('  ',m)\nEOF"
}
```


### [2026-09-06T22:25:33.744Z] TOOL RESULT

```
written
MISSING FROM ARCHIVE: 0
```


## [2026-09-06T22:25:36.163Z] TOOL CALL #92: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-289.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 289"
}
```


### [2026-09-06T22:25:37.915Z] TOOL RESULT

```
JSON OK
nodes verified: 19/19
node verdicts: {'plausible': 4, 'confirmed': 8, 'disputed': 4, 'unverified': 3}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 8, 'supports': 13, 'not_checked': 6, 'not_found': 2, 'contradicts': 1}
books consulted: {'partial': 10, 'supports': 29, 'silent': 14, 'contradicts': 3} | by book: {'CHEUNG': 12, 'BRT': 7, 'POK': 6, 'NYB': 5, 'AHD': 5, 'PHD': 4, 'KLN': 4, 'BOOK': 3, 'SKT': 2, 'SOD': 1, 'SYN': 1, 'HUB': 1, 'HRN': 1, 'BQT': 1, 'ARY': 1, 'KNT': 1, 'TLM': 1}
```


## [2026-09-06T22:25:53.514Z] TOOL CALL #93: Bash

```json
{
 "command": "python3 -c \"\nimport json\nd=json.load(open('data/verification/page-289.json'))\nfor e in d['entries']:\n    print('ENTRY',e['entry'],e['root'],e['verdict'])\n    for n in e['nodes']:\n        print('  #%s'%n['id'], n['lang'], '|', n['verdict'], '| refs:', [ (r['ref'],r['status']) for r in n['ref_check']], '| consulted:', [(c['src'],c['stance']) for c in n['consulted']])\n\""
}
```


### [2026-09-06T22:25:55.418Z] TOOL RESULT

```
ENTRY 0 Kwei 1, Qwei, Qwi confirmed
  #1 Avestan | plausible | refs: [('POK:637', 'partial'), ('SYN:826', 'supports'), ('SYN:1447', 'not_checked')] | consulted: [('BRT', 'partial'), ('CHEUNG', 'partial'), ('POK', 'supports')]
  #2 Persian | confirmed | refs: [('POK:637', 'supports'), ('KLN:1759', 'not_found')] | consulted: [('PHD', 'supports'), ('NYB', 'supports'), ('CHEUNG', 'supports'), ('BRT', 'supports')]
  #3 Sogdian | confirmed | refs: [('SOD:203', 'supports')] | consulted: [('SOD', 'supports'), ('CHEUNG', 'partial'), ('POK', 'partial')]
  #4 Greek | confirmed | refs: [('KLN:1447', 'not_found')] | consulted: [('KLN', 'supports'), ('POK', 'supports'), ('SYN', 'supports'), ('AHD', 'supports')]
  #5 English | confirmed | refs: [('AHD', 'supports')] | consulted: [('KLN', 'supports'), ('AHD', 'supports'), ('SKT', 'silent')]
ENTRY 1 Kwei 2, Kwoi confirmed
  #1 Avestan | plausible | refs: [('POK:637,638', 'partial')] | consulted: [('BRT', 'supports'), ('CHEUNG', 'partial'), ('AHD', 'silent')]
  #2 Persian | disputed | refs: [('POK:637', 'partial'), ('HRN:204', 'supports'), ('BQT:167', 'partial'), ('BQT:380', 'partial'), ('BQT:676', 'supports'), ('AEF:152,582', 'not_checked')] | consulted: [('CHEUNG', 'partial'), ('HUB', 'contradicts'), ('HRN', 'supports'), ('BQT', 'partial'), ('PHD', 'supports')]
  #3 Avestan | disputed | refs: [('HRN:90', 'contradicts'), ('FFD:47', 'partial')] | consulted: [('CHEUNG', 'contradicts'), ('BRT', 'silent'), ('NYB', 'partial')]
  #4 Pahlavi | plausible | refs: [('HRN:90', 'supports'), ('FFD:47', 'supports')] | consulted: [('NYB', 'supports'), ('PHD', 'supports'), ('CHEUNG', 'partial')]
  #5 Persian | confirmed | refs: [('HRN:90', 'supports'), ('FFD:47', 'supports')] | consulted: [('CHEUNG', 'supports'), ('NYB', 'supports'), ('ARY', 'silent')]
  #6 Old Persian | disputed | refs: [('KNT:209', 'partial')] | consulted: [('KNT', 'partial'), ('CHEUNG', 'silent'), ('POK', 'silent'), ('TLM', 'silent')]
  #7 None | unverified | refs: [('None', 'not_checked')] | consulted: [('BOOK', 'silent')]
  #8 Avestan | disputed | refs: [('KNT:209', 'partial')] | consulted: [('BRT', 'supports'), ('POK', 'silent'), ('CHEUNG', 'silent')]
  #9 Pahlavi | confirmed | refs: [('KNT:209', 'supports')] | consulted: [('NYB', 'supports'), ('PHD', 'supports'), ('BRT', 'supports')]
  #10 None | unverified | refs: [('None', 'not_checked')] | consulted: [('BOOK', 'silent')]
  #11 Avestan | plausible | refs: [('POK:637', 'supports')] | consulted: [('BRT', 'supports'), ('CHEUNG', 'contradicts'), ('AHD', 'silent')]
  #12 None | unverified | refs: [('None', 'not_checked')] | consulted: [('BOOK', 'silent')]
  #13 Greek | confirmed | refs: [('AHD', 'supports')] | consulted: [('POK', 'supports'), ('KLN', 'supports'), ('CHEUNG', 'supports')]
  #14 English | confirmed | refs: [('None', 'not_checked')] | consulted: [('KLN', 'supports'), ('AHD', 'supports'), ('SKT', 'silent')]
```


## [2026-09-06T22:26:09.622Z] TOOL CALL #94: Bash

```json
{
 "command": "python3 - <<'EOF'\nimport json, io\np='data/verification/page-289.json'\nd=json.load(open(p))\ne1=d['entries'][1]\nadd_en = \" Extraction note: in the Labibi shahed on the Persian box (node #2) the JSON reads 'بر آن خاک و خونش برنجیده اند', but the printed page (crop of data/verification/sources/refs/ocr/BOOK/289.png) clearly shows 'بر آن خاک و خونش پشنجیده اند' — a data-side misreading of پشنجیده as برنجیده that the owner should fix. Everything else on the page (words, scripts, references, empty boxes) is extracted faithfully.\"\nadd_fa = \" یادداشت دربارهٔ استخراج: در شاهدِ لبیبی زیر جعبهٔ فارسی (گرهٔ ۲)، فایل استخراج‌شده «بر آن خاک و خونش برنجیده اند» دارد، حال آنکه صفحهٔ چاپی به‌روشنی «بر آن خاک و خونش پشنجیده اند» است؛ این خطای خوانش اسکن است و باید در داده اصلاح شود. باقیِ صفحه (واژه‌ها، املای فارسی، ارجاع‌ها و جعبه‌های خالی) درست استخراج شده است.\"\ne1['note'] += add_en\ne1['note_fa'] += add_fa\njson.dump(d, io.open(p,'w',encoding='utf-8'), ensure_ascii=False, indent=1)\nprint('ok')\nEOF\npython3 -m json.tool data/verification/page-289.json > /dev/null && python3 tools/verify_check.py 289"
}
```


### [2026-09-06T22:26:11.409Z] TOOL RESULT

```
ok
nodes verified: 19/19
node verdicts: {'plausible': 4, 'confirmed': 8, 'disputed': 4, 'unverified': 3}
root verdicts: {'confirmed': 2}
ref checks: {'partial': 8, 'supports': 13, 'not_checked': 6, 'not_found': 2, 'contradicts': 1}
books consulted: {'partial': 10, 'supports': 29, 'silent': 14, 'contradicts': 3} | by book: {'CHEUNG': 12, 'BRT': 7, 'POK': 6, 'NYB': 5, 'AHD': 5, 'PHD': 4, 'KLN': 4, 'BOOK': 3, 'SKT': 2, 'SOD': 1, 'SYN': 1, 'HUB': 1, 'HRN': 1, 'BQT': 1, 'ARY': 1, 'KNT': 1, 'TLM': 1}
```


## [2026-09-06T22:26:32.629Z] AGENT

Page 289 (book p.259) verified — `data/verification/page-289.json`, `verify_check.py 289` shows 0 PROBLEM lines.

**Counts** — 2 entries, 19/19 nodes. Roots: 2 confirmed. Nodes: 8 confirmed, 4 plausible, 4 disputed, 3 unverified (the three empty pass-through boxes, blank in the book too). Ref checks: 13 supports, 8 partial, 1 contradicts, 2 not_found, 6 not_checked. 29 supporting `consulted` entries across POK, WLD(via POK), AHD, SYN, KLN, BRT, KNT, PHD, NYB, CHEUNG, SOD, HRN, HUB, BQT, FFD, SKT, TLM, ARY.

**Disputed**
- Entry 1 #2 «انجیدن» anjīdan — only this one word of the four: Horn (no.115) derived it from *ham-čay-, Hübschmann PS 18 no.115 rejects it (the very note the chart itself prints), Cheung has no such root. čīdan, parčīn and gozīdan are confirmed (HRN:204, BQT:167/380/676, Cheung *čai1).
- Entry 1 #3 Avestan "taug, taux" — no such Avestan verb exists. Bartholomae has none; Cheung's *tauǰ³ has no Avestan section and calls its origin unknown; HRN:90 (Nourai's own ref) says "Eine ältere Form ist nicht vorhanden". FFD:47 gives *taug-/*tauxta- as **Old Iranian reconstructions**, not Avestan. The Pahlavi verb glosses Avestan kāy- — i.e. the *other* root on this page.
- Entry 1 #6 OP sâ 1 / fra-sâ and #8 Av. spâ 2 — KNT:209 is cited exactly, but Kent derives them from PIE *ḱu̯ā- (palatal, §90, flagged "etymology not certain"); *kʷ gives OP k/c, never s, so the cluster cannot belong under Kwei 2. The words and the #8→#9 pari-sp link are sound (Nyberg: parisp < OIr *pari-spā-).

**Notable non-fatal findings**
- Entry 0 #1: Av. čisti- is glossed "sorrow" — it means "insight, understanding" (Bartholomae, Kellens in Iranica). Looks like Pokorny's "Sorge" from the adjacent Skt. cintā carried across. Other four words (kāy-, kaēnā-, kāθa-, čiθi-) confirmed.
- Nourai's two Klein page numbers are wrong: KLN:1447 (for Gk poinē) lands in "sa-", KLN:1759 (for kīn) in "un-"; the right pages are 1150 (penal) and 1206 (Poinae), which do say what the arrows say. SYN:1447 could not be checked — the open Buck scan breaks off at p.1435.
- Entry 1 #11 kaēš- is a faithful copy of POK 638, but LIV/Cheung reassign it to *kʷeis- "observe" (> NP کیش).

**Extraction error for the owner to fix** — `data/extracted/batch/page-289.json`, entry 1 node #2, Labībī quote: JSON has «بر آن خاک و خونش **برنجیده** اند»; the printed page reads «... **پشنجیده** اند». Everything else on the page is extracted faithfully. Page render saved to `data/verification/sources/refs/ocr/BOOK/289.png`.
