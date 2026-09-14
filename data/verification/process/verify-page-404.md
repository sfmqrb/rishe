# Verification process log — verify-page-404


## [2026-09-14T00:53:04.125Z] INPUT

Read the instructions in /home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md and follow them exactly for PDF page 404 only. Chart text: /home/sfmqrb/git/rishe/data/verification/agent/charts/page-404.txt; source JSON: /home/sfmqrb/git/rishe/data/extracted/batch/page-404.json. Write /home/sfmqrb/git/rishe/data/verification/page-404.json, run `python3 /home/sfmqrb/git/rishe/tools/verify_check.py 404` (fix any PROBLEM lines), and reply with the short summary described in the instructions.


## [2026-09-14T00:53:05.301Z] AGENT

I'll start by reading the instructions.


## [2026-09-14T00:53:05.972Z] TOOL CALL #1: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/AGENT_INSTRUCTIONS.md"
}
```


### [2026-09-14T00:53:05.983Z] TOOL RESULT

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


## [2026-09-14T00:53:06.476Z] TOOL CALL #2: Read

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/agent/charts/page-404.txt"
}
```


### [2026-09-14T00:53:06.498Z] TOOL RESULT

```
1	=== PDF page 404 (book page 374) ===
2	--- entry 0 ---
3	ROOT [Indo-European] Pis, Pais : crush, grind  (refs WLD2:1)
4	#1 (parent #0) [Avestan] refs=WLD2:1 | pišant : crushing, grinding ; pîštra : flour
5	  #2 (parent #1) [Persian] refs=HUB:42; MON:782 | pest, past 2 «پست ۲» : flour, crushed roasted wheat
6	#3 (parent #0) [Sanskrit] refs=WLD2:1 | pinašti : crushed ; pîštah : flour
7	--- entry 1 ---
8	ROOT Pislos -> redirect to Pilo
9	--- entry 2 ---
10	ROOT Plat -> redirect to Pele
11	--- entry 3 ---
12	ROOT Ple -> redirect to Pel 1
13	--- entry 4 ---
14	ROOT Pneu -> redirect to Skěu 1
15	--- entry 5 ---
16	ROOT Pô 1 -> redirect to Apo
17	--- entry 6 ---
18	ROOT [Indo-European] Pô 2, Pôi, Pî : to drink  (refs POK:839)
19	#1 (parent #0) [Sanskrit] refs=POK:839 | pâti : drinks ; pâtila : a large drinking vessel | NOTE: The link between "pâti" and "pâtila" is not certain.
20	  #2 (parent #1) [Persian] refs=MON:643 | pâtîl «پاتیل» : a large liquid container | extra: پاتیله | NOTE: For another possible root of "pâtîl" see root "Batiaxě".
21	#3 (parent #0) [Avestan] refs=POK:839 | vispo-pitay : drunk
22	#4 (parent #0) [Greek] refs=AHD | pusis : drunk ; sun-posion : a drinking party ☞Sem 1
23	  #5 (parent #4) [Latin] refs=None | 
24	    #6 (parent #5) [French] refs=VOP:216 | symposium
25	      #7 (parent #6) [Persian] refs=VOP:216 | sampozîyom «سمپوزیوم» : a "drinking party"
26	    #8 (parent #5) [English] refs=KLN:1557 | symposium
27	#9 (parent #0) [Latin] refs=POK:839 | bibere : to drink ; pôtus : drunk
28	  #10 (parent #9) [English] refs=AHD | potion, poison ; beer, beverage
29	--- entry 7 ---
30	ROOT Pod -> redirect to Ped
31	--- entry 8 ---
32	ROOT Pôi -> redirect to Pô 2
33	--- entry 9 ---
34	ROOT Poin -> redirect to Spen
35	
```


## [2026-09-14T00:53:07.821Z] AGENT

I'll read the source JSON and the reference index.


## [2026-09-14T00:53:09.177Z] TOOL CALL #3: Bash

```json
{
 "command": "cat /home/sfmqrb/git/rishe/data/extracted/batch/page-404.json",
 "description": "Read source JSON for page 404"
}
```


### [2026-09-14T00:53:09.237Z] TOOL RESULT

```
{
  "pdf_page": 404,
  "book_page": 374,
  "entries": [
    {
      "root": {
        "name": "Pis, Pais",
        "lang": "Indo-European",
        "refs": "WLD2:1",
        "gloss": "crush, grind"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Avestan",
          "refs": "WLD2:1",
          "words": [
            {"translit": "pišant", "gloss": "crushing, grinding", "script": null},
            {"translit": "pîštra", "gloss": "flour", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "HUB:42; MON:782",
          "words": [
            {"translit": "pest, past 2", "gloss": "flour, crushed roasted wheat", "script": "پست ۲"}
          ],
          "note": null,
          "quote": {
            "text": "بیاورد جامی ز یاقوت زرد - پر از شکّر و پست با آب سرد",
            "poet": "Ferdowsî"
          }
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "WLD2:1",
          "words": [
            {"translit": "pinašti", "gloss": "crushed", "script": null},
            {"translit": "pîštah", "gloss": "flour", "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {"root": {"name": "Pislos", "redirect": "Pilo"}, "nodes": []},
    {"root": {"name": "Plat", "redirect": "Pele"}, "nodes": []},
    {"root": {"name": "Ple", "redirect": "Pel 1"}, "nodes": []},
    {"root": {"name": "Pneu", "redirect": "Skěu 1"}, "nodes": []},
    {"root": {"name": "Pô 1", "redirect": "Apo"}, "nodes": []},
    {
      "root": {
        "name": "Pô 2, Pôi, Pî",
        "lang": "Indo-European",
        "refs": "POK:839",
        "gloss": "to drink"
      },
      "nodes": [
        {
          "id": 1,
          "parent": 0,
          "lang": "Sanskrit",
          "refs": "POK:839",
          "words": [
            {"translit": "pâti", "gloss": "drinks", "script": null},
            {"translit": "pâtila", "gloss": "a large drinking vessel", "script": null}
          ],
          "note": "The link between \"pâti\" and \"pâtila\" is not certain.",
          "quote": null
        },
        {
          "id": 2,
          "parent": 1,
          "lang": "Persian",
          "refs": "MON:643",
          "words": [
            {"translit": "pâtîl", "gloss": "a large liquid container", "script": "پاتیل"}
          ],
          "script_extra": "پاتیله",
          "note": "For another possible root of \"pâtîl\" see root \"Batiaxě\".",
          "quote": null
        },
        {
          "id": 3,
          "parent": 0,
          "lang": "Avestan",
          "refs": "POK:839",
          "words": [
            {"translit": "vispo-pitay", "gloss": "drunk", "script": null}
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
            {"translit": "pusis", "gloss": "drunk", "script": null},
            {"translit": "sun-posion", "gloss": "a drinking party", "script": null, "see": ["Sem 1"]}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 5,
          "parent": 4,
          "lang": "Latin",
          "refs": null,
          "words": [],
          "note": null,
          "quote": null
        },
        {
          "id": 6,
          "parent": 5,
          "lang": "French",
          "refs": "VOP:216",
          "words": [
            {"translit": "symposium", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 7,
          "parent": 6,
          "lang": "Persian",
          "refs": "VOP:216",
          "words": [
            {"translit": "sampozîyom", "gloss": "a \"drinking party\"", "script": "سمپوزیوم"}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 8,
          "parent": 5,
          "lang": "English",
          "refs": "KLN:1557",
          "words": [
            {"translit": "symposium", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 9,
          "parent": 0,
          "lang": "Latin",
          "refs": "POK:839",
          "words": [
            {"translit": "bibere", "gloss": "to drink", "script": null},
            {"translit": "pôtus", "gloss": "drunk", "script": null}
          ],
          "note": null,
          "quote": null
        },
        {
          "id": 10,
          "parent": 9,
          "lang": "English",
          "refs": "AHD",
          "words": [
            {"translit": "potion, poison", "gloss": null, "script": null},
            {"translit": "beer, beverage", "gloss": null, "script": null}
          ],
          "note": null,
          "quote": null
        }
      ]
    },
    {"root": {"name": "Pod", "redirect": "Ped"}, "nodes": []},
    {"root": {"name": "Pôi", "redirect": "Pô 2"}, "nodes": []},
    {"root": {"name": "Poin", "redirect": "Spen"}, "nodes": []}
  ]
}
```


## [2026-09-14T00:53:11.227Z] TOOL CALL #4: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json\nd=json.load(open('refs_online.json'))\nfor k in ['WLD','POK','HUB','MON','AHD','KLN','VOP','BQT','HRN','PHD','NYB','BRT','IEC','SYN','SKT','WEB','FSD','ARY']:\n    print(k, json.dumps(d.get(k), ensure_ascii=False)[:500])\n\""
}
```


### [2026-09-14T00:53:13.251Z] TOOL RESULT

```
WLD {"title": "A. Walde & J. Pokorny, Vergleichendes Wörterbuch der indogermanischen Sprachen, 3 vols., Berlin/Leipzig 1927-32", "edition_found": "ONLY Band 3 (1932 Register/index volume) found open; Bände 1-2 (the dictionary proper) not found online", "kind": "archive_djvu", "url": "https://archive.org/details/in.gov.ignca.20339 ; Band I (1930): https://archive.org/details/in.ernet.dli.2015.70244 (DLI; title misspelled 'Vwrgleichendes'; dup. in.gov.ignca.20337) ; Band II (1927): https://archive.org
POK {"title": "J. Pokorny, Indogermanisches etymologisches Wörterbuch, Bern 1959 (Band I, pp. 1-1183)", "edition_found": "1959 Band I, scanned in three parts (Toronto copies); plus a database dump with page numbers", "kind": "archive_djvu", "url": "https://archive.org/details/indogermanisches01pokouoft", "identifier": "indogermanisches01pokouoft, indogermanisches02pokouoft, indogermanisches03pokouoft (+ Indogermanisches-Etymologisches-Woerterbuch)", "local_file": "/home/sfmqrb/git/rishe/data/verific
HUB {"title": "H. Hübschmann, Persische Studien, Strassburg 1895", "edition_found": "1895 (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/persischestudie00hbgoog", "identifier": "persischestudie00hbgoog (duplicate: persischestudie01hbgoog)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HUB.txt", "page_offset": "leaf = printed + 10 (e.g. leaf 11 = p.1). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); open a leaf onli
MON {"title": "Mohammad Mo'in, Farhang-e Farsi (6 vols, Amir Kabir 1363/1984; vols 1–3 lexicon, vol 4 foreign compounds, vols 5–6 a'lam/proper names)", "kind": "website+archive_djvu", "url": "https://vajehyab.com/?q=<word>&d=moein  (also https://vajehyab.com/moein/<word>) ; https://abadis.ir/fatofa/<word>/ (section فرهنگ معین)", "lookup_hint": "Entry text of the lexicon volumes is online at vajehyab/abadis, including Mo'in's bracketed origin tags such as [په.] (Pahlavi), [ع.] (Arabic), [فر.] (French
AHD {"title": "W. Morris (ed.), The American Heritage Dictionary of the English Language, New College Edition (1975/76), Appendix 'Indo-European Roots' pp. 1505-1550 (by Calvert Watkins)", "edition_found": "Watkins, The American Heritage Dictionary of Indo-European Roots (1985 standalone ed.) + current online appendix (2nd/3rd ed.)", "kind": "archive_djvu+website+archive_restricted", "url": "https://ahdictionary.com/word/indoeurop.html ; New College Edition scans (1610 pp, include the IE appendix pp
KLN {"title": "E. Klein, A Comprehensive Etymological Dictionary of the English Language, 2 vols., Elsevier 1966-67", "edition_found": "1966/67 two-volume edition (pp. 1-1776), scanned two printed pages per leaf; plus the 1971 one-volume 'unabridged' edition (different pagination, no page markers)", "kind": "archive_djvu", "url": "https://archive.org/details/a-comprehensive-etymological-dictionary-of-the-english-language-by-ernest-klein", "identifier": "a-comprehensive-etymological-dictionary-of-the
VOP {"title": "Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi, Alborz 1371/1992", "kind": "none", "url": null, "lookup_hint": "Searched archive.org, ketabnak, noorlib, web: not found (only unrelated similar-title books, e.g. Zomorrodian's فرهنگ ریشه‌شناختی واژه‌های دخیل اروپایی, ketabnak 132354).", "local_file": null, "page_offset": null, "covers_etymology": true, "notes": "RE-SEARCH 2026-09: nothing — no catalogue record with a scan, no ebook. Decoys: ketabnak 132354 (Zomorrodian), Google 
BQT {"title": "Borhan-e Qate' (M.H. Tabrizi), ed. Mohammad Mo'in with etymological footnotes; Nourai cites Amir Kabir 1362/1983 (photo-reprint of Mo'in's 2nd ed., Ibn Sina 1342/1963, 5 vols, continuous pagination)", "kind": "archive_djvu+local_scan_ocr", "url": "https://archive.org/details/borhan-ghate-v1 (vol 1, آ–ت, printed pp. 1–~550) ; https://archive.org/details/borhan-ghate-v2 (vol 2, ث/ج–?, printed pp. ~550–~1230); vols 3–5 NOT found on archive.org (also checked borhan-ghateh-j-1 / borhan-qat
HRN {"title": "P. Horn, Grundriss der neupersischen Etymologie, Strassburg 1893", "edition_found": "1893 (Google scan, Univ. Michigan)", "kind": "archive_djvu", "url": "https://archive.org/details/grundrissderneu00horngoog", "identifier": "grundrissderneu00horngoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/HRN.txt", "page_offset": "leaf = printed + 21 (e.g. leaf 22 = p.1; leaf 60 = p.39). local file has \\f between leaves (0-based leaf index i == i-th form-feed page); op
PHD {"title": "D. N. MacKenzie, A Concise Pahlavi Dictionary, Oxford 1971", "edition_found": "1971 (open scan; plus PDF on parsianjoman.org)", "kind": "archive_djvu", "url": "https://archive.org/details/a-concise-pahlavi-dictionary", "identifier": "a-concise-pahlavi-dictionary (lending copies: concisepahlavidi0000dnma, bwb_Y0-EBW-590; Persian translation: a-concise-pahlavi-dictionary-in-persian-by-mackenzie-d.-n.-z-lib.org)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/PHD.t
NYB {"title": "H. S. Nyberg, A Manual of Pahlavi, Wiesbaden 1964-74 (Part II: Glossary, 1974)", "edition_found": "1964 (Part I texts) and 1974 (Part II glossary)", "kind": "archive_djvu", "url": "https://archive.org/details/a-manual-of-pahlavi-1-henrik-samuel-nyberg", "identifier": "a-manual-of-pahlavi-1-henrik-samuel-nyberg (both parts in one item)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/NYB_vol2_glossary.txt", "page_offset": "Part II: leaf = printed + 8 (e.g. leaf 9 
BRT {"title": "C. Bartholomae, Altiranisches Wörterbuch, Strassburg 1904 (repr. de Gruyter 1979, same pagination)", "edition_found": "1904 (Google scan, Univ. Michigan) - pagination identical to the 1979 reprint", "kind": "archive_djvu", "url": "https://archive.org/details/altiranischeswr00bartgoog", "identifier": "altiranischeswr00bartgoog", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/BRT.txt", "page_offset": "Columns 1-1874 are printed at the top of each column; the scan m
IEC {"title": "S. E. Mann, An Indo-European Comparative Dictionary, Hamburg 1984-87", "edition_found": "1984-1987 (complete, cols./pp. 1-1682)", "kind": "archive_djvu", "url": "https://archive.org/details/mann-an-indo-european-comparative-dictionary-1984-1987", "identifier": "mann-an-indo-european-comparative-dictionary-1984-1987", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/IEC.txt", "page_offset": "TWO printed pages per leaf: leaf ~= p/2 + 15 (e.g. leaf 412 = p.794, leaf 6
SYN {"title": "C. D. Buck, A Dictionary of Selected Synonyms in the Principal Indo-European Languages, Chicago 1949", "edition_found": "1949 (reprint scans, same pagination in all printings)", "kind": "archive_djvu", "url": "https://archive.org/details/a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "identifier": "a-dictionary-of-selected-synonyms-in-the-principal-indo-european-languages-by-ca", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S
SKT {"title": "W. W. Skeat, A Concise Etymological Dictionary of the English Language, Oxford (new ed. 1911; reprints to 1967 share pagination)", "edition_found": "1911 'new and corrected impression' (Google scan)", "kind": "archive_djvu", "url": "https://archive.org/details/aconciseetymolo01skeagoog", "identifier": "aconciseetymolo01skeagoog (1882 first ed.: bub_gb_4ZkRAAAAIAAJ, in.ernet.dli.2015.158267 - different pagination)", "local_file": "/home/sfmqrb/git/rishe/data/verification/sources/refs/S
WEB {"title": "Webster's New Twentieth Century Dictionary of the English Language, Unabridged, 2nd ed. (1978 printing)", "edition_found": "2nd ed., 1962 printing, Volume 1 only (A-?); vol. 2 not found open", "kind": "archive_djvu", "url": "https://archive.org/details/ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w", "identifier": "ejhc_websters-new-twentieth-century-dictionary-second-edition-volume-1-by-noah-w (restricted full copies: webstersnewtwent00webs_0 1977, w
FSD {"title": "Funk & Wagnalls New Standard Dictionary of the English Language, New York 1940 printing (first published 1913, same plates)", "edition_found": "1913 printing, 4 vols. (Digital Library of India scans); the 1940 printing is the same setting/pagination", "kind": "archive_djvu", "url": "https://archive.org/details/in.ernet.dli.2015.147439", "identifier": "in.ernet.dli.2015.147439 (vol I A-Dive), in.ernet.dli.2015.272042 (vol II), in.ernet.dli.2015.83695 (vol III), in.ernet.dli.2015.147440
ARY {"title": "Manuchehr Aryanpur Kashani, Farhang-e Rishe-hā-ye Hend-o-Orupāyi-ye Zabān-e Fārsi (فرهنگ ریشه‌های هند و اروپایی زبان فارسی), Isfahan, Jahan-e Ketab? (c. 2005), 545 pp. NOT one of Nourai's references — supplied by the project owner as an independent modern cross-check.", "kind": "local_scan_ocr", "url": "", "lookup_hint": "Alphabetical by Persian headword; each entry gives the PIE root, cognates by language, and page citations to Pokorny, MacKenzie, Buck, Amindarov, AHD and Borhan-e Qa
```


## [2026-09-14T00:53:17.598Z] TOOL CALL #5: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && sed -n '1,200p' SOURCE_MATRIX.md"
}
```


### [2026-09-14T00:53:17.642Z] TOOL RESULT

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
```


## [2026-09-14T00:53:18.081Z] TOOL CALL #6: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/data/verification/sources/refs/ | head -80"
}
```


### [2026-09-14T00:53:18.120Z] TOOL RESULT

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
```


## [2026-09-14T00:53:21.495Z] TOOL CALL #7: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && ls && grep -n \"pdf page\" WLD_Bd2_pages.txt | head -20"
}
```


### [2026-09-14T00:53:21.559Z] TOOL RESULT

```
WLD_Bd1_1930_dli_70244_djvu.txt
WLD_Bd1_1930_dli_70244_text.pdf
WLD_Bd1_pages.txt
WLD_Bd2_1927_dli_106624_djvu.txt
WLD_Bd2_1927_dli_106624_text.pdf
WLD_Bd2_pages.txt
```


## [2026-09-14T00:53:22.698Z] TOOL CALL #8: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pō(i)-\\|pō(i)\\|pōi-\\|po(i)-\" POK_full.txt | head -20; echo ---; grep -n \"839\" POK_full.txt | head -5"
}
```


### [2026-09-14T00:53:22.765Z] TOOL RESULT

```
---
2959:References: WP. I 2, Trautmann 4, Pokorny Urill. 70, 113, M. Forster Themse 839. 
27455:References: Persson Beitr. 839. 
28521:To what extent those from Persson Beitr. 666, 773, 839 f. considered as extensions of 
56149:References: WP. II 408 ff., WH. I 823 ff., 827 f., 832 ff., 839, Trautmann 151 f., 164; 
68593:Page(s): 838-839
```


## [2026-09-14T00:53:25.160Z] TOOL CALL #9: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Page(s): 83[89]\" POK_full.txt | head -20"
}
```


### [2026-09-14T00:53:25.238Z] TOOL RESULT

```
68334:Page(s): 838 
68544:Page(s): 838 
68562:Page(s): 838 
68593:Page(s): 838-839 
68607:Page(s): 839 
68799:Page(s): 839 
68850:Page(s): 839-840
```


## [2026-09-14T00:53:27.114Z] TOOL CALL #10: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '68560,68810p' POK_full.txt"
}
```


### [2026-09-14T00:53:27.318Z] TOOL RESULT

```
References: WP. II 90. 

Page(s): 838 

Root / lemma: pneu- 

Meaning: to breathe 

Material: Gr. nvsu) (nvsuaai) "blow, pant, gasp, breathe, smell', ttveOmq "das Wehen, 

breath, breeze, breath etc.', nvorj "das Wehen, snort'; in addition perhaps also noinvuu) 



'sich rijhren, astir sein', trans, "sich eager wherewith beschaftigen', Perf. TTsnvuaGai " 
spiritually astir, sensible, wise sein', nvuT6(; spcppajv, auxppojv Hes., apnvuaGai "again 
zum Bewufttsein come', if "sich riJhren, astir, esp. spiritually astir' from "beim Laufe 
keuchen' and "breathe = agile, lively sein' has evolved; 

Old Icelandic fnysa'pant, sniff, snort'. Old English fneosan^ sneeze' {fnora^6as 
Niesen'), Middle High German pfnusen^pant, sniff, snort, sneeze' {pf- schallverstarkend 
for /), pfnustm. "unterdrijcktes laughter', Norwegian fnysa' giggle '; besides Germanic 
*fnes-, *fnds-, *fnas-:0\6 English fnesan ^ an\r\e\are' , fnsestxr\. "breath, breath, breeze', 
/^^5e//a/7"schnarchen, pant, sniff, snort'. Middle High German pfnasen ^ pant, sniff, snort', 
pfnastm. "das snort'. Old High German /^as/ed/7 "anhelare'; Old Icelandic fn0sa'pant, 
sniff, snort'; Old Icelandic fnasa'pant, sniff, snort'; Old High German fnaskazzen, 
fneskezzen. Middle High German phneschen pant, sniff, snort, pant, gasp'; 

Germanic fneh-:0\6 High German fnehan. Middle High German pfnehen breathe, pant, 
sniff, snort, pant, gasp'. Old High German /^a/7/e/7/e "schnaubend' (Middle High German 
pfnuhtxw. "snort' braucht nicht die zero grade from Indo Germanic /7/7e:/-widerzuspiegeln). 

References: WP. II 85, Wissmann Nom. Postverb. 18 f., Schwyzer Gr. Gr. 1, 696. 
Page(s): 838-839 

Root / lemma: ppksti- 

Meaning: fist 

Material: Old High German fust. Old English fyst= Old Bulgarian p^stb {*pinstb) "fist'. 

Note: Obviously Root/ lemma: ppksti-i\s\! derived from penk^eixve (fingers)' 

References: WP. II 84, Trautmann 218 f.; 

See also: to Germanic farjxan {pak- and pag-, S. 788) or to penk^e^\\ynf . 

Page(s): 839 

Root / lemma: polo- : polo- 
Meaning: swollen, fat, big 

Material: Latin polled, -ere^^\n strong, vermoge', Denomin. eines *pollos\xoxx\ *pol-no-, in 
addition pollex, -ids m. " thumb, big, giant toe'; proto Slavic palb in russ. bez-palblj 
"fingerlos'; Old Russian-Church Slavic yOa/bCb " thumb ' {*poliko-), etc. ; perhaps in addition 
as "with the thumb touch ' npers. palldan^ seek, feel', Bulgarian palam' search, seek'. Old 
High German fuolen. Modern High German fuhlen. Old English faelan, engl. feel, ( *fdljan). 
Old Icelandic felma 'tap, grope ', ablaut, falmads. 
References: WP. II 7, 102, WH II 332 f., Vasmer 2, 305. 



Page(s): 840-841 



Root / lemma: porRo-s 
Meaning: pig 

Note: 

From an extended zero grade of Root/ lemma: eghi-\ " hedgehog ' derived Root/ lemma: 

ghers-, gher-\ "rigid, *pig' > Root/ lemma: porRo-s\ "pig' : lllyrian-italic-celtic g'^h- > p-. 

Material: Sakisch pasa{*parsa), Kurdish purs, borrowed Finnish porsas, Mordovian purts 

"swine'; 

Latin porcus^ihe tanned swine', Umbrian porca, purca^ porcas '; Middle Irish orcm. 
"piglet, young animal', abrit. Orcades {W\Vc\ gr. ending) = Middle Irish /nns/ Ore' Orkney- 
islands'; 

Note: 

Latin porous 'the tamed swine' < {*ghdr-n-k) > alb. o'e/'/r "piglet, sow'. 

Old High German farfajhn., Old English fearhm. n. "swine', (Danish /^^e "piglet throw'); 
Lithuanian parsas'a castrated boar'. Old Prussian /?/-a5//5/7 "piglet' {*parsistian)\ Old 
Bulgarian y0/'55^, -^/e "swine, piglet' (deminut. /7/-Suff.); to Latin porolhus'oi s\N\ne' 
compare Lithuanian yOa/'5/e/7a"Ferkelfleisch', to Latin yOC»/ri//i/s "Schweinchen' das 
Lithuanian parse/zs "piglet'. Old High German farheli. Middle High German varohelTn, 
Modern High German Ferkel. 

References: WP. II 78, WH. II 341, Trautmann 207, Benveniste BSL. 45, 74 ff.; after 
Specht Indo Germanic Dekl. 34 to perR- "tear open' (see 821 ). 
Page(s): 841 

Root / lemma: pos 

Meaning: by, about, around, beside 

Note: probably *p+ os, Gen.-Abl. to Y^Jp-^ above S. 53 f. 

Material: Gr. in Arcadian-Cypriot and auf gr. Inschriften Phrygiens TToq, vor vowel also no-, 

geltungsgleich with rrpoc; (see *per'out - about', Nr. 8) and Doric rroTi; Lithuanian pas 

preposition "an, by'; probably also Old Church Slavic yoo in the meaning " behind, after'; 

compare das erhaltene 5- in Old Church Slavic poz-dbA6']. "late', poz-de Mn. "late', 

pozderije {paz-derije) "KaAapin, arunsTov'. To Lithuanian pas a\so pastaras'\he letzte, 

hinterste'. 



derivatives: 1. witli -//probably Armenian as/'after', Adverbal and preposition "after = 
secundum, gemaft'; in addition stor'the untere part'?; Latin post, Old Latin poste'aiter, 
behind ', ortlich and zeitlich, Adverbal and preposition m. Akk., Oscan pust, post, Umbrian 
post, pus'post' ortlich and zeitlich, preposition m. Abl., therefrom Latin posterns, Oscan 
pustrer\x\ postero', Umbrian postra, Latin postumus, Oscan pustmafsj 'postremae'; 
Umbrian postne, Latin poneirom *posti-ne, Oscan pustin, Umbrian pustin {irom *posti en) 
"je after' preposition m. Akk.; Umbrian pust-na/af' post\cas', purnaes ^post\c\s'; Latin 
/7c»s//c^s"hinten situated'. 

2. -ko-0\6 Indie /75sca(lnstr.) Adv. "behind, westlich, later' = Avestan pasca preposition 
" behind, after', ortlich and zeitlich. Old Indie pasca/ (Abl.) preposition " behind, after, 
westlich', Avestan paskatAdv. "vonhinten her, hinterdrein' spacial and zeitlich; Lithuanian 
paskul pasku/ (Dat) Adv. "afterwards, nachher', preposition "after'. 

3. In ending still controversial is ap. pasa ^aiter', preposition ortlich and zeitlich; alb. pas, 
Geg /77i6'as preposition " behind, after' (Indo Germanic *pos+ Demonstr. s/). 

References: WP. II 78 f., WH. II 347 ff., Trautmann 207, Schwyzer Gr. Gr. 2, 508. 
Page(s): 841-842 

Root / lemma: pot/s 

Meaning: owner, host, master, husband 

Material: Old \nd'\c pat/-, Avestan pa///- "master, mister, lord, master, consort, partner'; Old 

Indie /Oa//7/"" mistress, wife', Avestan paz?/?/- 'mistress'; Old \nd\c patyate^\r\errsc\nt, is 

teilhaftig' (: Latin potior); 

Avestan x'ae-pati- "er selbst'; 

gr. hogk; ' husband ', nowia "mistress (of Hauses), wife'; 5£a-noiva 'mistress of 
Hauses' (*5£a-novia, from *5£a-noTvia), 5£a-n6Tr|<;, -ou "master, mister of Hauses' (see 
above S. 198); alb. pata^had', y05s/7e"gehabt' {*pot-to-) (to a present as Latin potior. Old 
Indie yoa/ya/e); 

Latin potis {potior, potissimus) "wealthy, mighty', possum. Old Latin also potis sum 
"kann', potui, potensirom an e-denominative as Oscan putiad ^possW, putians 'poss\nt', 
Latin potestas^ power', potior, -TrT{potrtur and potTtui) "sich bemaehtigen'; com-pos 
"teilhaftig' (*"Mitherr'), tiospes, -itis' guest's friend ', pael. iiospus {*gtiosti-pots^ Qasihexx'); 
ein unflektiertes *poti 'selbst' placed in utpote^as natijrlich, da namlich, namely', actually 



*ut *pote{esf) "as es possible is = naturiicli', furtlierwitli syncope in m/hr-, meo-, suapte 
etc.; 

Gotliic bru^-fa^s^ bridegroom ', /7£//70'a-/&A'5"Befelilsliaber about 100 Mann'; engl. fad 
"strong, valiant, big, large'; 

Lithuanian pa/s "husband' and "selbsf (old patis), Latvian pats^ householder ' and 
"selbsf, Lithuanian K/espa/s "master, mister' (old viespatis). Old Prussian pattiniskun f\Vk. f. 
" matrimony '; f. Old Lithuanian viespatnr, *patn/'under influence of *yOa//- transfigured to 
*patr\n Old Prussian waispattin f\Vk. "wife, woman', Lithuanian pat/^\N\ie', Latvian pat/ 
"Wirtin'; indekl. particle Lithuanian pat, Latvian yC>a/"selbst, even, straight'; about Old 
Church Slavic gospodb "master, mister', see above S. 453; 

Hittite -yC»s/"eben(so), also, rather'; Tocharian A pa/s "husband'. 

References: WP. II 77 f., WH. I 660 f., II 350 f., 379 f., Trautmann 208, Benveniste 
Origines 1, 63 f., Pedersen Hittite 77 f., Endzelin Latvian Gr. 396 f. 
Page(s): 842 

Root / lemma: po-ti 

Meaning: against 

Note: through das Adv.-forms -//(compare *proti- : *pro above S. 815 f.) from *po (see 

below *apo' ab') extended 

Material: Avestan pa/'t/, ap. /05//y proverb, and preposition "against, entgegen, to, auf, by'; 

"an; for, um'; "from - from'; "in - toward, in'; hom., Boeotian, lak. etc. nori "np6(;' proverb. 

and preposition "against - toward, against, compared with; an, to', "in - toward, from-'. 

References: WP. II 77, Schwyzer Gr. Gr. 2, 508 f. 

Page(s): 842 

Root / lemma: pougo- or pougho- 

Meaning: clear, sound 

Note: only Celtic and Slavic 

Material: Old Irish o^"jungfraulich', oge"Jungfraulichkeit'; Czech pouhy^ pure, bare, 

simple, just'. 

References: WP. II 77. 

Page(s): 843 

Root / lemma: p6(i)-1 : (pa/-?:) pT- 



Meaning: to graze 

Material: Old Indie pati, Avestan /7a///"hutet, bewacht, schijtzt', Old Indie go-pa- m. 
"herdsman, shepherd', Avestan /'a/75-/0a'Beinschutz, -schiene'. Old Indie /Oayi/-"Huter' 
(compare noju), pala- m. "Wachter, herdsman, shepherd', -/0ai/5/7"schutzend', ap. xsa^''a- 
/7ai/aA7"Landvogt, Satrap'; Old \v\6\c nr-pT-ti-i. 'Mannerschutz'; nr-p-a-m. 'MannerschiJtzer 
=king'; patra- n. ' container ' (= Gothic fodr); 

gr. nu)u 'herd' (n. to Old Indie payu-), noipnv 'herdsman, shepherd' (: Lithuanian 
piemud), noi|jr|v 'herd', noipaivw 'treibe auf die Weide, hijte; ziehe auf; -nG)\xa {po-mn) 
'cover'; 

Gothic fodru. (= Old Indie patra-, yet agrees in addition in pronunciation of only Old 
English fodoi) 'BriKri, vagina'. Old English fodor, fodor' sheath, vagina'; Late Old Icelandic 
fodrv^. 'food (of clothing)' from Middle Low German voder^s.; Old High German 
(fedar)fdtar^ cav\v\a\ Late Old High German fuoter^Vc\eca\ Modern High German Futter{oi 
clothing), Futterat, 

Lithuanian yO/e/77^0' herdsman, shepherd', Akk. pfemeni{ *pdimen-). 

References: WP. II 72, Trautmann 204, 207 f. 
Page(s): 839 

Root / lemma: pd(i)-2: pA-and (from pd-from) pa- 
Meaning: to drink 

Grammatical information: Aoristwurzel, wherefore secondary present pi-po-mi, pi-bo-mi, 
themat. pi-bo 

Material: Old Indie paZ/'trinkt', Aor. apat, pay-ayati, payate 'trankt' (: Old Church Slavic 
pq/'g, pojiti), panamu. 'Trunk' (: gr. Eunojvoq 'pleasant to drink' Hes., Middle Irish ant 
'vessel'). Inf. patave^io drink' (= Old Prussian poOtweiAs.), patar-, patar-rw. 'Trinker' (= 
Latin potords.), -pay/a-, -payya-'io water, soak. Trunk' (= Old Prussian pou/sm. 'das
```


## [2026-09-14T00:53:30.098Z] TOOL CALL #11: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '68810,68870p' POK_full.txt"
}
```


### [2026-09-14T00:53:30.185Z] TOOL RESULT

```
Latin potords.), -pay/a-, -payya-'io water, soak. Trunk' (= Old Prussian pou/sm. 'das 
Trinken'), patra- n. 'drinking vessel' {*pd-t/o-m= Latin pocu/um ^ gob\et'); participle Pass, 
ablaut. yO/?^-'getrunken (habend)', p/t/-t 'das Trinken, Trunk', Avestan vispo-pitay- 
'alltrankend'; Old Indie Inf. patum, patave. Gerund. pTtva- (: Latin potusm. ' drink, 
beverage, liquid which is swallowed to quench one's thirst, draught, potion'); redupl. 
athematic present 3. PI. pi-p-ate, participle pf-p-ana-, Aor. a-pipT-ta-, thematic /0/Z?a//"trinkt' 
(= Old Irish ibid); 

Armenian ampem^ drink ' (formation unclear); 



gr. nivu), Lesbian ircbvoo (of Nominal stem *pd-no-, compare above suttojvoix;) " drinl< ', 
Fut. (Konj.) niopai, Aor. sniov, Imper. nTGi, Perf. nsnajKa, Med. TT£no|jai " drink ', TTaJ|ja, 
TTOija n. Trinken, drink, beverage, liquid which is swallowed to quench one's thirst, 
draught, potion', -noioq, m., hogk;, -\oc, and -sux; f. ds., norrip m., norripiov n. " drinking cup 
', ttTvov n. "Gerstentrank', niniGKU) (Fut. mau)) 'give to drink'; 

alb. yO/" 'drink' etc.; 

Latin bibo, -ere' drink ' (assimil. from * pibd\ Faliscan pipafo'\ werde drink'; Latin poto, - 
are' drink strong', potus' drunk, intoxicated, getrunken' (= Lithuanian puotai. 
'Zechgelage'), potus, -usxx\. ' drink, beverage, liquid which is swallowed to quench one's 
thirst, draught, potion' (= Old Indie /Oa/i//77 Inf.), potidi. 'Trinken, drink, beverage, liquid 
which is swallowed to quench one's thirst, draught, potion' (: gr. aiJ-nwTK; f. 'Ebbe', Old 
Prussian poJ/'drink' from *pdti-), pocu/um 'gob\et' {*pd-tlo-m), potorvn. 'Trinker' (= Old 
\v\6\c patar-); Umbrian puni, poni'xwWV! (: Old \v\6\c panam' beverage, drink '); Old Irish ibid 
{*pibeti) 'trinkt', Verbalnom. Dat. Sg.c»^/(disyllabic) 'Trinken' {*poJa-lo-)\ acymr. iben 
'bibimus', corn, ei/a/'bibo'. Middle Breton euaff6s.\ Middle Irish ani. 'drinking vessel' (: 
Old Indie y05/75/r7 'Trunk'); 

Balto-Slavic */Oo/oand *plid' drink ' in Old Prussian yoo/e///' trinkt', poOism. 'das Trinken', 
Old Church Slavic pi/'g, pifi' drink '; pirb m. 'Bankett', pivon. ' beverage, drink ', Czech etc. 
'beer'; Kaus. Old Church S\av'\c pq/'g, pq/it/ 'iranke'; Balto-Slavic *pdta- and *pTta- 
'getrunken' in Lithuanian puotai. 'Trinkgelage' and Old Church Slavic pitijb 'trinkbar'; 
Balto-Slavic *p^tiu\^6 *pTti\. 'das Trinken' in Old Prussian Inf. poOt{*pdti-) and slov. p?tt ' 
beverage, drink ' (Infin. *pitij\ Balto-Slavic * potu- m. 'das Trinken' in Old Prussian Inf. 
puton, poutonan6 poutwe/'dnnk', ablaut, passive russ. -Church Slavic yO/fe. 

References: WP. II 71 f., WH. I 103 f., Trautmann 228 f. 
Page(s): 839-840 

Root / lemma: pou- : pau- : pu- 

Meaning: small, little; young (of animals) 

Material: 1. With -o-suffix; Gothic fawaiP\. 'wenige'. Old Icelandic far' little, wortkarg', fa- 

t0/cr' arm' (as Latin pauper). Old High German fao, fo' little ', Dat. PI. fouuem. Old Saxon 

fa. Old English fea, PI. feawe, engl. /fen/ 'wenige'. 

2. With formants -Aro-/ Latin paucus' little ', pauper' arxx\' {*pauco-paros ox pau-paros?' 
little erwerbend, little sich constituting, originating '); Old High German fob' little '; 



Maybe alb. {*pauc-) pak' little' a Latin loanword. 

With suffix -/o-; Latin paul(l)us "small, little ' ( *pauks-lo-), pauxillus " totally little ' ( *pauk- 
s-lo-lo-).
```


## [2026-09-14T00:53:45.076Z] TOOL CALL #12: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && grep -n \"\\[pdf page\" WLD_Bd2_pages.txt | head -30"
}
```


### [2026-09-14T00:53:45.141Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:53:47.465Z] TOOL CALL #13: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && head -40 WLD_Bd2_pages.txt; echo \"=== formfeeds:\"; python3 -c \"\nd=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read()\nprint(len(d.split(chr(12))))\n\""
}
```


### [2026-09-14T00:53:48.663Z] TOOL RESULT

```
                ALOIS WALDE


VERGLEICHENDES WORTERBDCH
                            DER


  INDOGERMANISCHEN SPRACHEN

          HERAUSGEGEBEN UNO BEARBEITET
                            VON

               JULIUS POKORNY


                      II.   BAND




             B£|UN UND LEIPZIG 1*927

       WALTER DE GRUYTER & CO.
  VORMALS G. J. GOSCHEN'SCHE VERLAGSHANDLUNG -
  J.   GUTTENTAG, VERLAGSBUCHHANDLUNG - GEORG
        REBIER - KARL J. TROBNER - VEIT & COMP.
central a     -              iJlGAL
    EIBRaKY,                 HI.
Am.
lh.^.JM.-..
0*11 No...Hl.l/.fE‘^/fV^;.
(pais?): pis- „zerstaiDpfen, zermalmen^^                      (bes.   Gretreide);   zum    Sachlichen
     vgl. Meringer AYS. I 3ff.
  Ai. pind^i             „zerreibt,        zerstampft'^   (3, pi.   piklnti =   lat. plnsiint)^   pi^ci-
^gemahlen*-^,          „Meh]“, pvMar- ^^Zerreiber^^ (: lat. pistor)^ av.
                        n.
 „zerstampfend‘’^ gr. titIooco (zum Anlaut vgl. z. B, 7t(T)6hg u. pel- „Burg“)
                          ;


=== formfeeds:
725
```


## [2026-09-14T00:53:52.776Z] TOOL CALL #14: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 -c \"\nd=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i,p in enumerate(d[:4]):\n    print('=== leaf',i,'===')\n    print(p[:3000])\n\""
}
```


### [2026-09-14T00:53:53.868Z] TOOL RESULT

```
=== leaf 0 ===

=== leaf 1 ===

=== leaf 2 ===

=== leaf 3 ===
                ALOIS WALDE


VERGLEICHENDES WORTERBDCH
                            DER


  INDOGERMANISCHEN SPRACHEN

          HERAUSGEGEBEN UNO BEARBEITET
                            VON

               JULIUS POKORNY


                      II.   BAND




             B£|UN UND LEIPZIG 1*927

       WALTER DE GRUYTER & CO.
  VORMALS G. J. GOSCHEN'SCHE VERLAGSHANDLUNG -
  J.   GUTTENTAG, VERLAGSBUCHHANDLUNG - GEORG
        REBIER - KARL J. TROBNER - VEIT & COMP.
```


## [2026-09-14T00:53:56.312Z] TOOL CALL #15: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/WLD && python3 -c \"\nd=open('WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i in range(4,8):\n    print('=== leaf',i,'===')\n    print(d[i][:4000])\n\""
}
```


### [2026-09-14T00:53:57.432Z] TOOL RESULT

```
=== leaf 4 ===
central a     -              iJlGAL
    EIBRaKY,                 HI.
Am.
lh.^.JM.-..
0*11 No...Hl.l/.fE‘^/fV^;.

=== leaf 5 ===
(pais?): pis- „zerstaiDpfen, zermalmen^^                      (bes.   Gretreide);   zum    Sachlichen
     vgl. Meringer AYS. I 3ff.
  Ai. pind^i             „zerreibt,        zerstampft'^   (3, pi.   piklnti =   lat. plnsiint)^   pi^ci-
^gemahlen*-^,          „Meh]“, pvMar- ^^Zerreiber^^ (: lat. pistor)^ av.
                        n.
 „zerstampfend‘’^ gr. titIooco (zum Anlaut vgl. z. B, 7t(T)6hg u. pel- „Burg“)
                          ;


 „stampfe, schrote^^ (wohl aus Ttrivo-tpy; vgl. Brgm. 11^3,279, 381), jirtopa,
Ttxtodvri „enthulste Gerste“, nrioiQi Ttiiapog „das Stampfen“, Tteomiopaxa
 „ausgepreBte YYeintrauben^^ (diss. aus ^neQiTvdGjbLara^ Sommer GrLtst, 75 f.,
 Jacobsohn KZ. 42, 276); lat, pinsOj -ere, pinsio, pinso, plso, -are „zer-
stampfen, zerstoBen^^ {p^s- mit Nasalreduktion aus pins-)^ pistum, plsiiw,
pinsHiim; pistor „Kornstampfer; Backer*^^, plso „M6rser^^, pila ds., pllum
 „ Morserkeule        (und „Wurfspie6‘^, Kropatschek Jb. d. d. arch. lust
 23,  79 if.),  pistilliim „Stampfek^; umbr. pistn „pistum“; unsicher ahd.
fesa „Hulse des Getreides, Spreu, Getreide in der Hiilse^^, nhd. Fese
 (s. u. pcs-    „blasen“); mud. vlsel „M6rser“, und ^vohl auch mhd. vise!
 „penis^‘ (kaum zu ^pes-         „das mannliche Glied“; Franck Wb. 1083,
 Franck - van Wijk 742f., Fick 111^ 242); lit. paisyti „(Gerste) abklopfen,
 den Gerstenkornern die Grannen abscblagen^^, wo hi auch (vgl. mhd.
 visel) lit. p^stl „coire cum femina^" (s. u. pes- „das mannliche Glied“);
 abg. p>hm und phcJiajq, phcJwti „stoBen^, phseno „Mehk“, pbseniea „triti-
 cum''^,   r.  pseno „Hirse^‘, sloven, pesta, poln. piasta „Stampfek‘, cech.
pecliovati „stampfen“.       Curtius 276f., 498, Fick 1^78, 24Sf., 472.    Die
Hochstufe der Wz. ist ^'pais- nach Ausweis von gr. naico „schlage^^
(fjza(cja), wenn dies, wie wahrscheinlich, aus ^Tialoco entstanden ist (s. u.
peti-- „schlagen^); allerdings hat es Anlaut gr. rr-, nicht nx-} tit- lage vor
in Tixaio) „sto6e an etwas (intr.), strauchle, irre, habe wobei Ungluck"^
iduTcticav eig. ^geradaus stoBend oder aufsohlagend“) s. u. pet- „auf etwas
lossturzen“ am Schlusse), die freilich von der Bed. „im Morser stoBen^'
erheblich abweichen und daher in ihrer Zugehorigkeit vie! zweifelhafter sind,

paas-     „los-, ablassen^^
  Gr. Tiavo}          „mache aufhoren^^, med. „h6re auf, lasse ab^', navJ.a „Ruhe^*,
7zavocoA}j       yjEast^;
   apr. pausto „wild“, abg. ptisfz „dde, wiist^. pustiti^ russ. piistitb,
pushdth „lassen, loslassen^, sloven, pust „Fasching“, delopiist „Feier-
abend“ usw. Solmsen IF. 31, 483. Allerdings wird navco von Schwyzer
IF. 30, 443 f, anders beurteilt: STiavoa xtva xivog „schlug jemanden von
etwas fort, machte ihn wovon ablassen"^, wornach navoy neu geschaffen sei,

     S.   aueli unter Sp..
   Walde     ,
                 Etymolos^^’sciies   Worterbuch,   if.                                      1

=== leaf 6 ===
2                                             pauson   —   pak'


faSt   er als Aorist         zu naico ~ napico^            lat.   pavio;   doch   s.   die   Bedeiiken
Kretschmers H. 6, 307 f., wie auch                                jzavocokij einer Gdbed. „Schlag‘‘
durchaus widerstreben.
paason- : pusoH- j,Gdttername“.
   Ai. Pusan- m. „vedischer Gott, Hiiter und Mehrer der Herden und
des menschlichen Besitzes uberhaupt “5 gr. Ilav^ ark. Ildmv (^Ildvocov).
Dohring Et. Beitrage (Progr. Konigsberg 1907) S. 1 1, Schulze KZ. 42, 81 374.                        ,


Die vom ind. Standpunkte aus naheliegende Terb. mit indyaii, pusndti,
posati j^gedeiht, wachst zu, macht gedeihen, ernahrt^^, nd-pnsndti „futtert
auf, macht fett^, p6sa-li „Gedeihen, Wachstum“ (Uhlenbeck ai. Wb. 173)
kann zu Recht bestehn, da Ablautformen mit idg. eii daneben nicht vor-
liegen.

pak- und pag- „festmachen^^, u. zw. teils durch Einrainmen (Pflock, Pfosten),
     teils durch Zusammenfugen (Fuge; festgefiigt, kompakt, fest; z. T.
     auch Fessel. Strick).
  Dab nach Meriuger IF. 21 31 1 ff. ein ^pulc- „flechteii und binden^‘ und
                                          ,


     ein *pdg~ „ein Fachwerk machen“ sich erst nachtraglich zu einer Ein-
     heit zusammengeschlossen hatten, ergibt sich aus dem Materiale nicht.
  Ai. pag- (i. ph padbMk) „Schlinge, 8trick“,^«m- m. ds. {pdray ati
panjara-j n. „Kafig“, pajrd- wenn „feist, derb, kraftig^* (? oder „glanzend'-?
s. Bechtel Hauptprobleme 262, Uhlenbeck Ai. Wb. 152, Brugmann IF.
                                                                       9, 349).
  Av. pas- ,,aneinander befestigen, zusammenfugen^^, mit paiti- und ava-
„zusammen-, aneinander fesseln“ fs9hts „mit Fesseln^^, potirupaxUa- „YieI,
reich gefaltet“       (s.   Bthl. Grdr. I 13,       Wb. 1029, 900).
   Gr. ndooaXog^ natt. ndxrakog „ Pflock, Kagel“          TzrjoocOj att. Tiiproj
.^nyyvv/ud^; jzijyvvpi (dor. -a-) „befestige durch Hineinschlagen, Hinein-
stecken, Zusammenfugen; lasse erstarren^^ {Inayy^v, Ttenrjyay Tirjy.Tog)^ Tzfjypa
,,Gefugtes,      Gestelle"*,     nriyog       „fest, stark‘‘       (ob davon nyyarov .       .
                                                                                                   „Raute,
Ruta       graveolens"^?),     vavnriyog „Schiffbaumeister‘‘,              TiriyvUg Adj.      f.   „reifig,
eisig^^,    Ttdyog   m. „Eis, Reif^ (s. auch d. Pi. ndyeoi „Frost'^), horn. „Pels-
spitze, -klippe, Hiigel, Berg“, Tidyry {^aa^va) „Reif, Frost'', Jiayy „Schlinge,
Falle'', Tiaxxoco „mache fest, verschliefie, verstopfe", d-na^ ^einfach";
7id| adv. ,,st! nun gutl“ (s. Meister Die Mim. d. H., 74Sf.; vgl.                      dt.   ^halt"!").
S.   noch jrd| unter ^pahs- „Schuh".
       paciscor, pactus sum „ein Ubereinkommen, einenYertrag oderYer-
gleich festmachen, abschlieflen'', alat. pacio „pactio", pacunt {c echt oder
alte Schreibung fiir ^?), pax, -cis „Friede; freundliche Gesinnung" (umbr.
pase tua „pace tua" in der Anrede an Gottheiten), pahis „Pfabl'' aus
*paxhs^ vgl. Demin, paxilhis; pango {jyegngl; geneuert       nach fregi^ und
panxi „befestigen, einschlagen; aneinanderfugen, schriftlich verfassen, fest-
setzen" (zur Nasaliening desPraes. vgl. germ,          Frohde BB. 16, 189,
und ai. panjai'a- „Kaflg“, Uhlenbeck Ai. Wb. s. v.), compagts „Fuge'%
pdgina     die zum Blatt gefiigten Papyrusstreifen) „Blatt Papier, Seite,
Kolnmne" (s. auch Hartmann H. 4, 37*8 gegen Stowassers W. St. 31, 149
Herleitung aus dikzog (fgylvi]). pagus ,,Landgemeindeverband einer Bauern-
schaft, Dorf, Bau'', propago, xyrdpages ,.Setzlinge, Absenker", propdgare
 „einen Absenker in der Erde festmachen, daher fortpflanzen" (s. Yf.

=== leaf 7 ===
                                                     pak       pag-                            3


LEWb.2 s. V.          ;
                          nicht zn      ir,   al,   cymr. ael            umbr. pase (s. o.),
Adv.    yjCaiisa“,        osk.    priipukid „exante pacto,            ex praefinito^, umbr. p^.
marruc. pacri- „propitius, placatus“ (vgl. den o-St. got.      usw.  zu                    ;


mars, pacre s. auch Hermann KZ. 48, 120). air. accai d. sg. „Fesselung^
(^pakni-;   s.    Stokes         St. 2, 168,        Zupitza KZ. 36, 234, Thurneysen Hdb. 103);
mir. ^ge „Glied^^                             ml „angenehm^^ (^pagli-; Strachan BB. 20, 24;
Oder ah ^pokli- zu aisl. fc^gil^gr ds,, s. 1. ^pek-P):,   cymr. aelod „GIied‘’^
{^'paglatii-^ Zupitza BB. 25, 91).
   Germ, Kasalpraes.             (: lat. pango) in got, faJian^ aisl. /o, ags. fan,

ahd. fahaUj as. fdhan und fangan „fangen^‘, got. gafdhs m., aisl. fengr m.,
ags. feng m., ahd. fang ^Fang, Beute^^; ahd. ftioga „Fuge^^, gafnogi „passend^‘,
hi’fuoge „Ehestifterin^^, ahd. fuogen^ ar. fdgian „fugen“, ags. gefegan „pas-
sen, verbmden“, mhd. vagen „fdgen“; got. gafahrjan „zubereiten“, fagrs
,,geschickt, geeignet“, aisL /a^r, ags, fcegr (engl. fair\ oixA, fagar „sch6n^^
(: umbr.            Von pa^-: as, fac „Umfassung, Umzaunung^, mnd. vak
m. „Umfriedigung, Zaun, Abteilung'^^ ahd. fak „Umfassung, Mauer, XJm-
zaunung im Wasser fiir den Fischfang, Abteilung^^, nhd. FaeJi^ einfach^
von zeitlicher Abteilung ags. fcBC „Zeitraum‘^, mnd. vaken^ vake^ spatmhd.
gevack „oft^^, mhd. drier vacher „dreimaF^ (s. zuletzt Loewe KZ. 47, 134;
verfehlt    Wiedemann BB, 27, 260).
     Sloven, russ. pas „Fuge^, sloven, pas „Bretterwand“ (Uhlenbeck PBrB.
22, 189; liber        pazucha usw. s. u. "^deits- „Arm“); lit. (Lehnworte?)
pozas ,,FaIz, Fuge'^, pozyfi „falzen“ (Prellwitz u. nrjyvvpC).
   Curtius 267 f., Fick    77, 471, P                  HP
                                       224, Vf. LEWb.^ 551 f. m. Lit.
   Fernbleiben: ah\ tinolaim „sanimle^^ (s. Pedersen KG. II 511 gegen
Fick II^ 49); air. oc „juxta, prope^^                      =
                                        cymr. ivnCj ivng „prope^^ (Brugmann
Festschr. f. Stokes 31, BSGW. 1901, J09; es widerspricht das o der kelt.
Gdf. "^onk    .; s. andererseits Pedersen KG. I 126 gegen die Verbd, von
              .   .



air. oc mit cymr. ach y laio „bei ihm“, wortlich „pres de sa main^^ durch
Vendryes EC. 31, 103f.).
   arm. hoc „dicht, gedrangt, kompakt^ (Hubschmann Arm. Gr. I, 468 zw.
                                    —
                                                                                                   ;


s. u. "^ped- „fassen“).     Trotz nknyya „bin erstarrt, steiP ist lit. plaukal
pdpeze „die Haare stehen aufrecht^ (Zupitza Gutt. 197) fernzuhalten und
allenfalls mit ai. pdpajt (Pick I^ 77), wenn dies „ stand starr^*^ bedeutet,
unter idg, "^peg- ,,starren“ sonderzuatellen.
paks- „Schuh^ ?
   Gr. jrdf* vTxoSrjpa evvTzodrjrov Hes.^ ^nd^eta (Quelle von lat. haxea „leichte
Art Sandalen^^) verbindet Fick IP 6 mit air. assa ,,8occus^^, 6 assaib „sandalis",
mi-t-asigfhe dti galUasti „calcia te gallicas tuas“ (nicht nach Loth Ec. 17,
434 Lw. aus ags. hosu).
   Wohl zu ^pdk- ,,festmachen, zsfiigen^^ als „unter die Sohle gebunden^.
pEg- (bes. es-            St. ^%[e]s-)        oder (peg-:) pog-: pog- „ Achsel, Hiifte, Lende,
       Seite^.
     Al, paksd- m. ,.,Achsel (Fliigel, Pittich), Seite, Halfte^,                     n. „Achsel,
                            nach Breal KZ. 20, 80 zu lat. pectus,, woriiber
Seite, Halfte, PliigeP (nicht
s. u. ^pek- „Wolle rupfen"^; Velar wird erwiesen durch:) lett. paksis
„Hausecke^, aif paks'eyn „bei Seite^^ (Bezzenberger BB. 16, 120); lang-
```


## [2026-09-14T00:54:06.292Z] TOOL CALL #16: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pišant\\|pisant\\|pištra\\|pistra\\|pišta\\|pista-\" BRT.txt | head -30"
}
```


### [2026-09-14T00:54:06.370Z] TOOL RESULT

```
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
```


## [2026-09-14T00:54:07.236Z] TOOL CALL #17: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"pist\\|pi[sš]\" HUB.txt | sed -n '1,60p'"
}
```


### [2026-09-14T00:54:07.289Z] TOOL RESULT

```
88:aus Bh. I, 95, 96 {apiyd, apisim) beseitigt ist. Jeden-
406:*) Vgl. auoh phi. stik ip sftk-pistan *with prominent breasts'
561:apis, gr. ^/ttntg, ahd. imbi stehen erhebliche Schwierig-
846:heisst nach Geldner (Pischel - Geldner, Ved.
849:halt, Versteck' etc. (Pischel-Geldner, Ved. Stud. I,
1371:312. Die Form piSman u. s. w. ist verkiirzt aus paslman, das
1380:murdan des Judenpersischen zeigt, dass piSmurdan
1390:auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
1403:WZKM. 6, 184 (pistdn = pEstan Gl. and. Ind. 113 =
1414:320. Np. plst - nicht pist — heisst *MehI, gerSstetes Mehl'.
1425:323. Np. %i(i8aifkijtdan, pisanfidan *besprengt werden =
1543:handen ist, np. piS- auf ap. patis zuriickzufuhren, ist
2032:zd. x^a^tU' (= *Ader, Pischel-Geldner, Ved. Stud.
2894:sein an pidar u, s. w. wie pusar, pisar (aus pus) etc.
2917:Socin, kurd. Samnil. II, 317, si 'alezan', hespisi 'un
2978:turpis, foetens' zu erwahnen ^= zd. fra + gainti-.
3687:Pischel-Geldner, Ved. Stud. I, 37).
4463:ataSy arm. LW. afas (Sebeos), phi. ataocs^ zd. atars; pisan-
4465:(oben p. 42) ; aspist {ispist, vspust) 'Luzerne = phi. aspast ;
4812:fjLi6&6g] supuS, supus neben sipiS u. s. w. 'Laus == zd. spis;
4817:von zd. ap. ni-, vgl. ap. nipistam geschrieben', nipiStanaiy- 138 -
4883:Shk. 269; diz- *b6se* = duz, ap. dws-, zd. dus-, dui-; pisar
4891:*) Jetzt wird pisdr *Sohn* und pddUr *Vater' gesproohen.— 140 —
6086:e) Vorschlag von u in: uspus 'Laus' = zd. spis;
6102:*Laus' (auch sipis u. s. w.) = zd. spis; supoxtan [sip^xtan)
6212:*schreiben', ap. nipistanaii/; kdbln *Mitgift* = kdvm JRAS.
6288:asp *) 'Pferd' = zd. aspa-, dazu aspist Xuzerne' H. 79 ; as-
6564:^) Zd. fs auch ^=- pis in nc^su aus *napfsu, loc. pi. von napat-.— 186 --
6597:2) Wie aber verhalt sich np pistan 'Brust' zu zd. fstana-? Vgl.
6598:oben p. 41. Etwa pistan (aus ^pdatdna-?) zu. fstana' (aus *pstana-)
7251:ap. "^Old^at-, zd. drisat-] pus 'Sohn (daraus pnsar, pisar
7544:ap. *nipaisamiy {niyapisam ist sigm. Aorist ^- idg. ni-e-pik^-
7814:§ 71 und Horn Nr. 696—708. In sipis, supus u. s.w. 'Laus'
7815:fur supus etc. = zd. spis ist das anlautende s an das aus-
7856:*) Vgl. zarah i akfuda Mas kaspische (eigentl. *blaue*) Meer*
8410:das Verhaltniss von zd. fstdna- zu np. pistan 'Brust', siehe
8440:= ap. nipistanaiy, pr. nuvesam, Wrzl. pdk^ ; histan 'lassen*,
8445:= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.
9482:lecken* = brShm. episoh Uh u. a. w.— 2G5 -
10656:pis^ 42.
10657:pistdn 41, 186.
```


## [2026-09-14T00:54:13.541Z] TOOL CALL #18: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1405,1430p' HUB.txt; echo \"=== index ===\"; sed -n '10650,10665p' HUB.txt"
}
```


### [2026-09-14T00:54:13.599Z] TOOL RESULT

```
318. 7m pus vgl. Spiegel, WZKM. I, 250.
219. Np. pasa/nd *angenehm, gefallig, gebilligt, will-
kommen', paz. pasandfdan *to approve* Skh. 263 ist mit
Spiegel aus *pat-sand zu erklaren. Vgl. skr. chad,
Shand gefallen', Shanda- gefallig*, zd. sad^ ap. ^ad.
') Fehlt bei H r n.— 42 —
Dem Sinne nach Hesse sich mit pasafid auch zd. paiti-
zanta- *wiIlkommen' vergleichen, dem aber im Neu-
persischen *pazand entsprechen miisste.
320. Np. plst - nicht pist — heisst *MehI, gerSstetes Mehl'.
Also nach Nr. 316 zu stellen.
321. Im Afgh. sind puSt *Riicken und |?ws<^ 'Stiitze' Lehn-
worter ; echt ist pu^tai *Rippe' = skr. pr^ti- *Rippe* (das
von skr. prstha- 'Riicken = zd. parsti-, np. pust doch
wohl zu trennen ist).
Hier fehit: paSm 'Wolle', skr. paksman- 'Augen-
wimpern, Haar' (am Reh), paksa- Flugel'; ahd. fahs
*Haarschopf, gr. 7raxoi;*Vliess', tio xog *Schaf wolle, Vliess',
an, fcer *Schaf (J oh. Schmidt, Pluralbild. p. 148).
Vgl. Fr. Muller, WZKM. 7, 372.
323. Np. %i(i8aifkijtdan, pisanfidan *besprengt werden =
phi. pasindUan Viesein Bdh. 26, 10 kann sehr wohl
zur Wrzl. skr. sin6 gestellt werden. Es ist entstanden
aus pat + sinMaUy die Form sine- fur June trat regel-
recht ein nach den auf i endigenden Praepositionen
(vgl. skr. abhi'Sindafi *begiessen, besprengen , ni$incati
=== index ===
p^rdz 45.
pes 45.
pidrdm 38.
pi/i 46.
pir 38, 131, 146.
jofrar 45.
pis^ 42.
pistdn 41, 186.
pizinurdan 41.
pizdhidan 41.
p5/ad 43.
po5^ 43.
po^a 43.
pwfc 43.
pw/ = pwW 195, 207.
ptiia 43.
```


## [2026-09-14T00:54:19.395Z] TOOL CALL #19: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^316\\.\\|^ *316\\.\\|31[4-7]\\.\" HUB.txt | sed -n '1,20p'; echo ===; sed -n '1380,1406p' HUB.txt; echo \"=== 8440 ===\"; sed -n '8435,8450p' HUB.txt"
}
```


### [2026-09-14T00:54:19.463Z] TOOL RESULT

```
Exit code 1
1384:314. Der Paragraph ist vollkommen verfehlt und zu streichen.
1399:316. Np. past niedrig, gering' ist nicht = skr. upasti-,
1402:317. Etym. dunkel, auch nach Fr. M tiller's Erklarung,
9664:p. 41, Nr. 314. Vgl. WZKM. 8, 272.
(eval):1: == not found
```


## [2026-09-14T00:54:21.888Z] TOOL CALL #20: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '1384,1405p' HUB.txt; echo \"=== 8440 ===\"; sed -n '8438,8450p' HUB.txt"
}
```


### [2026-09-14T00:54:21.938Z] TOOL RESULT

```
314. Der Paragraph ist vollkommen verfehlt und zu streichen.
Vgl. Fr. Miiller, WZKM. 7, 371, dessen positive
Ausfiihrungen {piidh-tdan = pati + s + Wzl. von
np. justan, vgl. phi. vijustan WZKM. 8, 92) freilich
auch nicht einwandfrei sind. Ich lehne also np. piz-
aus patis (wie oben bis- aus abis) ab. Ich finde patis
auch nicht in np. paSkam^ {piskam^ baskam, biSkam)
*domu8 aestiva, aula, atrium, coenaculum, porticus =
arm. patSkam (patsgam^ patsgamb, patskamb) *Gemach,
Halle, Stockwerk*, sondern fiihre np. paSkam = arm.
patskamb auf ap. *pati-skamba~^ das ich zu zd. fra-
skemba- vd. 2, 26 ('Stiitzmauer Geldner, 'batiment
avec balcon* Darmesteter) stelle, zuriick. Im mittel-
persischen wurde *patskamb zu *paskamb, ehe pat-
(vor andern Consonanten als s, s, d) zu pai- wurde.
316. Np. past niedrig, gering' ist nicht = skr. upasti-,
das zu *bast geworden ware, sondem = *patta-y skr.
patita-, Vgl. oben Nr. 92.
317. Etym. dunkel, auch nach Fr. M tiller's Erklarung,
WZKM. 6, 184 (pistdn = pEstan Gl. and. Ind. 113 =
*payastdna', das zu zd. fStana- nicht stimmt).
318. 7m pus vgl. Spiegel, WZKM. I, 250.
=== 8440 ===
hihist 'Paradies' == zd. vahista-; xist 'ZiegeF, skr. istako-;
ristan *spinnen, pr. resam, Wrzl. reik^; nivistan 'schreiben*
= ap. nipistanaiy, pr. nuvesam, Wrzl. pdk^ ; histan 'lassen*,
skr. srsta-, Wrzl. serg^ ; hast ^) 'acht* = zd. asta, idg. okHOu ;
biristan 'braten' mit st aus skt von Wrzl. iran. brj und
bri^g = idg. bhrzg, oben p. 27.
b) = st: dost Treund' == ap. daustar-; §ast 'sechzig'
= zd. xsvasti- ; pist 'Mehl' = skr. pista- ; mahist (ZDM6.
46, 139) = ap. mad^ista- ; bargustuvan 'Pferdepanzer H. 205,
oben p. 27. Durch spateren Vokalausfall entstand st aus
sat in bTst 'zwanzig* = zd. visaiti und diivest zweihundert*
= zd. duy^ saite.
Im Phi. steht st hauiBiger fiir urspr. st im Auslaut,
```


## [2026-09-14T00:54:37.528Z] TOOL CALL #21: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Mehl\" HRN.txt | head -40"
}
```


### [2026-09-14T00:54:37.575Z] TOOL RESULT

```
599:\^. ärd 'Mehl'.
602:38, 428); phlv. ärd ^Mehl'.
3062:Mehl zerrieben'.
4446:oben No. 13), arab. LW. x^iskar 'Mehl', phlv. /nsk[a]r
```


## [2026-09-14T00:54:39.346Z] TOOL CALL #22: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '3050,3075p' HRN.txt"
}
```


### [2026-09-14T00:54:39.396Z] TOOL RESULT

```
319. pesend zufrieden, angenehm', pesendlden.
ap. *M/)rt -T- K^arf-; aw. [^sad- (Geldner 1 [/sad-,
KZ. 27, 242), vergl. sendah-, vahmö.sendah- (?)2) (auch
l/"sac/- 'sitzen' kommt mit inligirtem Nasal vor, vergl.
ai. ilsandt- 'Sessel*, ksl. sedq 'ich sitze', apr. sindäts),
Spiegel, Commentar II, 311 (nur fälschlich mit
Praep. paiti; die Aussprache pisend findet sich nur
in dem türkischen FS.).
320. pist 'Mehr.
aw. pistra-; ai. l/'pes- 'zerreiben, zerstampfen {pistä-^
skr. pistaka-),
wa/. pös^; siyn. pist, sar. pa/t geröstetes Korn , zu
Mehl zerrieben'.
321. 2>ie«f 'Rücken'.
Kä§. mäz. past.
aw. parsti' 'Kücken'; phlv. piist; ai. prsti-, prsthd-,
kurd. pist, zaza past; af/. pw5^ bezw. pt^j^^ 'Rippe';
bei. n. put (444) ; wa/. par^.
322. pusek, pösek *Katze' ('Dialekt von Transoxanien' BQ.)^).
gel. plöa (?).
In Indien spricht man piser ; die nämUche Aussprache soll auch
})yser bei Fleischer, Neup. Gramm. 2, S. 7 ausdrücken. Piser ist in
seinem / durch pider beeinilusst; die Endung -er ist nach der der
anderen Verwandtschaftsnamen angefügt (Bartholomae, BB. IX,
129).
*) Fayfür (skr. hhayaputra-) als Titel des Kaisers von China ist
```


## [2026-09-14T00:54:52.706Z] TOOL CALL #23: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پست\" MON_part1.txt | head -20; echo \"=== part2\"; grep -n \"پست\" MON_part2.txt | head -20; echo \"=== sizes\"; wc -l MON_part1.txt MON_part2.txt"
}
```


### [2026-09-14T00:54:52.796Z] TOOL RESULT

```
1175:شکرء کف چوبکک و مغز پسته. نوعی از 
1810:نوک پستان. آبله از هم گسستن: : بیرون زدن 
1815:پستان‌های گاو می‌زند (۲۰ تا ۳۰ دانه). 
2184:پست و بلند و سراشیب. درهم آميخته» < 
2359:پستانداران و عالیترین موجود زند؟ روی 
5961:پستی. 
6632:شبیه شلغم است و برگش شبیه اسپست و 
9307:زونان؛ سفلگان؛ فرومایگان» مردم پست. 
9836:ردیل تر» خوارتر» زبون‌تر» پست‌تر» اخس؛ 
10075:ار غ: ب»ه (ص.) بادام و پسته و فندق و گردو 
10888:(طبقهٌ پست»» زیردستان؛ مق. اعالی. اسافل 
10910:جای‌ها. اسب آبی: (امر.) (جاذ.) پستانداری 
17544:به زیر آمدن. (امص.) پستی. انحطاط فکر: 
17545:پستی اند بشه. 
17566:افتادن» پست شدن. (امص.) بستی» پایین 
17594:صندوق پست انداخت. سباشرت کردن) 
17850:تیرةٌ نخستینان از شاخ پستانداران» از گُونة 
18675:نا کسان» مردم پست» بی‌سر و پایان» سفلهة 
20820:بال: ۰۶ (.) (جان.) یکی از پستانداران 
21577:خورا ک‌های پست و خشن و نابجا خورد. 
=== part2
165:مغاً کث» زمین پست؛ زمین گود. غار ررف: 
553:(آب)؛ م. ظاهر. کود؛ پست. 
557:غایط: 2۲۰:(ع. غائط ] (.) زمین پست 
655:پسته و گردو و کنجد سازند؛ حلوای مغزی» 
762:باز گویند مانند غده مترشحه شیر در پستان و 
824:گرم است. نزد پستانداران این غده از دو 
1904:مردم بی‌سر و پا و پست» اوبانی. 
2005:تفت در جنین پستانداران نیز قبل از تشکیل 
2127:فزات پست با فزات گرانبها مانند طلا و 
2214:جاریه؛ ج. غلمان. غلام پست: مأمور پست 
3177:غامضه. زمین‌های هموار. اراضی پست نرم. 
3714:نقطهٌ گداز و نقطةً جوش غیر فلزها پست 
4665:کوه. زمین پست میان دو پشته. 
5062:پست شود و به اراده و به عبارت دیگر تجلیه 
5126:می‌دارند با به جوراب يا کرست و با پستان‌ها 
5652:نشسیب: بسلندی و پستی. سربالایی و 
6032:فر خند ه: (۵-) ]1۵ فرح + شل۵) پست. 
6850:زبون» پست» فرومایه. ناتوان. (امر.) (مس.) 
7305:(گیا.) پسته. 
7327:فسر ده پستان: ع-] | - افسر ده‌یستان ] 
=== sizes
  99339 MON_part1.txt
  94500 MON_part2.txt
 193839 total
```


## [2026-09-14T00:55:00.537Z] TOOL CALL #24: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پست\" MON_part1.txt | sed -n '1,5p'; echo \"--- look for headword region: پسته/پستان\"; grep -n \"^پست\\|^ *پست\" MON_part1.txt | head; echo \"--- incoming MON\"; ls -la incoming/MON/ 2>/dev/null; grep -c \"پست\" incoming/MON/MON_2vol_Adena_v1_djvu.txt 2>/dev/null"
}
```


### [2026-09-14T00:55:00.638Z] TOOL RESULT

```
1175:شکرء کف چوبکک و مغز پسته. نوعی از 
1810:نوک پستان. آبله از هم گسستن: : بیرون زدن 
1815:پستان‌های گاو می‌زند (۲۰ تا ۳۰ دانه). 
2184:پست و بلند و سراشیب. درهم آميخته» < 
2359:پستانداران و عالیترین موجود زند؟ روی 
--- look for headword region: پسته/پستان
1815:پستان‌های گاو می‌زند (۲۰ تا ۳۰ دانه). 
2184:پست و بلند و سراشیب. درهم آميخته» < 
2359:پستانداران و عالیترین موجود زند؟ روی 
5961:پستی. 
17545:پستی اند بشه. 
23316:پست‌ام: ۱22 [ع. ۰ (ص.) خسندان» 
23401:پستک: ماد (ص. .) خادم» خدمتکار. 
23418:پستن: 2۶-۱27 (ست؛» ننددء خواهد بست» 
25840:پستیادسنج: لودع.ت (افا.) ژرف‌نگر؛ 
26894:پستانداری از راسته جوندگان که نسبة بز رگ 
--- incoming MON
total 48692
drwxrwxr-x  2 sfmqrb sfmqrb     4096 Sep  4 14:06 .
drwxrwxr-x 23 sfmqrb sfmqrb     4096 Sep  4 14:06 ..
-rw-rw-r--  1 sfmqrb sfmqrb 20113727 Sep  4 14:06 MON_2vol_Adena_v1_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4377831 Sep  4 14:06 MON_2vol_Adena_v1_djvu.txt
-rw-rw-r--  1 sfmqrb sfmqrb 21014767 Sep  4 14:06 MON_2vol_Adena_v2_archive.pdf
-rw-rw-r--  1 sfmqrb sfmqrb  4331421 Sep  4 14:06 MON_2vol_Adena_v2_djvu.txt
175
```


## [2026-09-14T00:55:03.838Z] TOOL CALL #25: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '23280,23340p' MON_part1.txt"
}
```


### [2026-09-14T00:55:03.908Z] TOOL RESULT

```
مرتب کردن بساط. بهم پیچید بیجیدن ساط: در 
نوردیدن بسطء بهم زدن بساط. . بهم خوردن 
ساط: درهم ریختن دستگاه. پهن کردن 
ساط: سفره تهاه کت ون ساط 
مع رکه گیری را گستردن. بجیدن ساط: ۰ جمع 
کردن ساط. از بين بردن» زابل کر دن. . جمع 
کردن ساط: برچیدن ساط. جور بودن 
بساط: کامل بودن و مرتب بودن سفره 
میخواران يا قماربازان. کامل و مرتب بودن 
لوازم و اشیای بساط‌انداز. جور کردن ساط: 
مهیا ساختن وسایل بازی و قمار برای 
قماربازان یا خوراک و مشروب برای 
میخواران. درنوردیدن ساط: طی کردن 
ساط. دزهم نبجدن ساط. جمع کردن 
سفر ۵. طی کردن ساط: 0 ساط. 
در بیچیدن ساط. . جمع کردن سفره. 
طت: ادها [ع. . ساطة | (مص‌ل.) 
ساده بودن» بی‌تکلف بودن. (امص.) شیرین 
زیسانی» لطسیفه گسویی. بسی آمیختگی. 
گشاده‌رویی در صحبت و نوازش مهمان. 
سادگیء بسیرنگی» بی‌نیرنگی. (شیم.) 


چگونگی جسم مفرد (بسیط). 

بساک: 0 تاجی که از گل‌ها و 
ریاحین و اسپرغم‌ها و برگ مورد می‌ساختند 
و پادشاهان و بزر کان و دلیران روزهای عید 
و جشن و مردمان در روز دامادی بر سر 
می‌گذاشتند. ( گیا.) برجستگی دکمه مانند 
انتهای مبلة پرچم گل که مسحتوی دانه‌های 
گرده می‌باشد. 

بسالت: ۱022 [ع. سالة ] (امص.) دلبری» 
دلاوری» یلی؛ شجاعت. 

پست‌ام: ۱22 [ع. ۰ (ص.) خسندان» 
گشاده‌روی» سیار تبسم کننده. 

بسان: ۵-2-6 (ق‌مر.) مثل» شبه» نظیر» 
مانند. . صح. - دایم الااضافه است. 

بسانی: 029-27-1 [آس + ان (جمع) 3 
نسبت ] (ص‌نسه.) متعدد و متکشر ت 
فراوان. 

بساو ایسی : 02۷8 (حامص.) لمس. (.) 
لا مسه. 

بس‌اویدن: 2۷-700 [- پساویدن] 
(مصم.) لمس کردن» سودن. 

بسباس: 5 (ص.) هر زه» بی‌معنی. 
بستاسه: )فده [معر. بزباز.] (ا.) 
(گیء) گل درخت جوزیویاکه سابقاً در 
تداوی مورداستفاده داشته است؛ برباز» 
چارگون پسپاسه» قشرالعفص. 

ست. 9251 (مص خم.) سستن » سد کردن: 
ست و بند: زدوبندهای سیاسی و اداری. 
(کد.) استحکام و ضبط و ربط. (اسف. ۱.)
```


## [2026-09-14T00:55:12.366Z] TOOL CALL #26: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پست:\" MON_part1.txt MON_part2.txt incoming/MON/MON_2vol_Adena_v1_djvu.txt incoming/MON/MON_2vol_Adena_v2_djvu.txt | head -20"
}
```


### [2026-09-14T00:55:12.427Z] TOOL RESULT

```
incoming/MON/MON_2vol_Adena_v1_djvu.txt:31637:پست: 6۱ ([در تسحت امسر کسی قرار 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:31660:پست: ۲2۵ ,اد۲ [ساییدن» خرد کردن] (.) 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:31914:پست: ۲06 (.) بالا» زبر. قسمت خلفی تن 
incoming/MON/MON_2vol_Adena_v1_djvu.txt:49704:چاهی که از آن آب در آبد. چاه پست: چاه 
MON_part1.txt:31637:پست: 6۱ ([در تسحت امسر کسی قرار 
MON_part1.txt:31660:پست: ۲2۵ ,اد۲ [ساییدن» خرد کردن] (.) 
MON_part1.txt:31914:پست: ۲06 (.) بالا» زبر. قسمت خلفی تن 
MON_part1.txt:49704:چاهی که از آن آب در آبد. چاه پست: چاه 
MON_part2.txt:2214:جاریه؛ ج. غلمان. غلام پست: مأمور پست 
incoming/MON/MON_2vol_Adena_v2_djvu.txt:2214:جاریه؛ ج. غلمان. غلام پست: مأمور پست
```


## [2026-09-14T00:55:14.406Z] TOOL CALL #27: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '31625,31690p' MON_part1.txt"
}
```


### [2026-09-14T00:55:14.462Z] TOOL RESULT

```
سودن] (مص‌م.) (پساوید» پساود» خواهد 
ساوید» بیساو» بساونده» ساویده) دست 
مالیدن» لمس کردن. 

پس‌ پر ده. (0-)6-02۲02-.[ (امر.) سرای» 
خانه» حرم» حرامسرا. عالم غیب. در نهان. 
پس پر یر وز: ]۲.۳2 (ق‌سر.) دو روز 
پیش از دیروز. 

پس پشت.: ۲.5 (ق‌مسر.) شت‌سر» 
دنبال» عقب‌سر. 

پست: 6۱ ([در تسحت امسر کسی قرار 
گیرنده] (ص.) پایین» فرود» زیر» تحت» 
سفل؛ مق. بالا روی» فوق» علو. (.) بستی؛ 
مق. بالاء بلندی. (ص.) کوتاه» کم ار تفاع 
قصیر. برابر با زمین» هموار» یکسان با خاکث. 


(.) زمین هموار گو» مغاکث» گودی. نشیب» 
قنوع. (ص.) خراب) مق. آباد. نابود» معد و م. 
دون» خوار» دانی. ذلیل» زیون بی‌مقداره 
بی‌اعستبار» مغلوب. فرومایه» بی‌سروپا 
خسس» بخیل» حقیر» رذل. تنگگ چشم» 
اندک بین» کاسد. (تص.) آنکه نتواند به بال 
همت به مدارج کمالات حقانی یا مر تبه‌ای از 
مراتب دیگر پرواز کند. (ق.) از بن و بیخ. 
تند» چانکك» چالاکك. ساده» آسان. راحت»؛ 
آرام» آسوده» فار غ‌بال. هراسان» مضطرب؛ 
مشوش. ناگوار» تلخ. سست» ضعیف. 
ببهوش؛ بی‌خبر از خود. بیزار» نفور. سخت 
خرد و ریزه و نرم. (مس.) بم) مق. زیر) تبز. 
نبهره» ناروا. بست و بلند دنا دیده: مجرت؛ 
آزموده» سر د و گرم چشید ه. 

پست: ۲2۵ ,اد۲ [ساییدن» خرد کردن] (.) 
هر نوع آرد (عموماٌ). آردی که گندم و جو 
و نخود آن را بریان کرده باشند (خصوصا)؛ 
آرد بو دادهء تلخان» قاووت» سویق. سبوس» 
سبوسه» نخاله. مرکبی باشد که بعضی از 
چله‌نشینان و فقیران و جوکیان هندوستان از 
جکر آهو و مغز بادام و امثال آن سازند که 
هرگاه مقدار پسته‌ای از آن بخورند تا چند 
روز محتاج به طعام نشوند. پست خوردن و 
نای زدن بهم راست نیاید (مثل): قاووت در 
دهن گر فته در ای دمدن امکان ندار د. 
پست. ۱ (۱.) اداره‌ای که نامه‌ها و امانات 
را از جایی بسجایی می‌برد و می‌رساند؛ 
چابارخانه. شخصی که نامه‌ها و امانات را 
می‌رساند؛ چاپار» چپر» پیکث» برید. منازلی 
در راه شهرها که در آن مرکوب برای حمل 
مسافر و بار نگاه دارند. محل خدمت 
مأموران انتطامی» پاسگاه (فره.) شغل» مقام. 
پست امدادی: پاسگاهی که برای کمکث در 
مسواقع ضصروری ساخته شود. ست 
امدادی آموزشگاه‌ها: شفاخانه (فره.) بست 


بستا فرهنگک فارسی معین 


۳۷ 


ژاندارم: پاسگاه ژاندارم.
```


## [2026-09-14T00:55:28.659Z] TOOL CALL #28: Bash

```json
{
 "command": "ls /home/sfmqrb/git/rishe/tools/ && sed -n '1,40p' /home/sfmqrb/git/rishe/tools/fetch_source.py"
}
```


### [2026-09-14T00:55:28.730Z] TOOL RESULT

```
build_site.py
fetch_source.py
ganjoor.py
jscheck.js
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


## [2026-09-14T00:55:35.377Z] TOOL CALL #29: Bash

```json
{
 "command": "for u in \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peys-\" \\\n \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%83-\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA\" \\\n \"https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84\" \\\n \"https://www.etymonline.com/word/symposium\" \\\n ; do python3 tools/fetch_source.py \"$u\" --note \"page 404 verification (roots Pis/Pais, Po 2)\"; done 2>&1 | tail -20"
}
```


### [2026-09-14T00:55:39.301Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/70c23b3b6b85a17a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/de14cf77d6b5e09a.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/b58226ca1420e6c7.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/0af573ddd8850565.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/f1d41b1a5d5e611a.txt
```


## [2026-09-14T00:55:41.662Z] TOOL CALL #30: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && echo \"### peys\"; head -c 3000 70c23b3b6b85a17a.txt; echo; echo \"### peh3\"; head -c 3000 de14cf77d6b5e09a.txt"
}
```


### [2026-09-14T00:55:41.763Z] TOOL RESULT

```
### peys
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peys-
FETCHED: 2026-09-14T00:55:37Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/peys- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/peys- - Wiktionary, the free dictionary 

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

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Derived terms 

 1.1.2 
 Descendants 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ peys- 

 Add languages 

 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *peys- [ 1 ] [ 2 ] [ 3 ] 

 to grind , to crush 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *peys- (47 c, 0 e) 

 *pi-né-s-ti ~ *pi-n-s-énti ( nasal-infix present ) [ 2 ] 
 Proto-Indo-Iranian: *pinášti ( see there for further descendants )

 Proto-Italic: *pinsō 
 Latin: pinsō 

 *pis-é-ti ( zero-grade present ) 
 Proto-Balto-Slavic: *pištei 
 Latgalian: pist 

 Latvian: pist 

 Lithuanian: pi̇̀sti 

 Proto-Slavic: *pьxati [ 4 ] [ 5 ] ( see there for further descendants )

 *peys-Hō ~ *pis-Hne-s 
 Proto-Italic: *peisō 
 Latin: pīsō 

 *pis-e-no-m 
 Proto-Balto-Slavic: *pišena 
 Proto-Slavic: *pьšenò [ 6 ] ( see there for further descendants )

 *pis-tó-s 
 Proto-Indo-Iranian: *pištás 
 Proto-Indo-Aryan: *piṣṭás 
 Sanskrit: पिष्ट ( piṣṭá , “ crushed, ground ” ) 

 Proto-Iranian: *pištás 
 Middle Persian: pst' ( “ brown flour ” ) ( possibly ) 

 Proto-Italic: *pistos 
 Latin: pistus 

 *pis-tlo-m [ 2 ] 
 Proto-Indo-Iranian: *pištram 
 Proto-Iranian: *pištram 
 Avestan: 𐬞𐬌𐬱𐬙𐬭𐬀   n ( pištra , “ bruise, injury ” ) 

 Proto-Italic: *pistlom , *pistlā 
 Latin: pīlum , pīla , Pīlumnus , pistillum 

 *póys-eye-ti (eye-causative)
 Latgalian: paiseit(i) ( “ to knead, to pound, to beat ” ) 

 Latvian: paisīt 

 Latvian: paise ( “ tool, device (e.g., flax, hemp) 
### peh3
URL: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%83-
FETCHED: 2026-09-14T00:55:37Z
STATUS: 200
TITLE: Reconstruction:Proto-Indo-European/peh₃- - Wiktionary, the free dictionary

Reconstruction:Proto-Indo-European/peh₃- - Wiktionary, the free dictionary 

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

 move to sidebar 
 hide 

 Beginning

 1 
 Proto-Indo-European 

 Toggle Proto-Indo-European subsection 

 1.1 
 Root 

 1.1.1 
 Alternative reconstructions 

 1.1.2 
 Derived terms 

 1.1.3 
 Descendants 

 1.2 
 References 

 Toggle the table of contents 

 Reconstruction:Proto-Indo-European/ peh₃- 

 Add languages 

 Reconstruction 

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
 Get shortened URL 

 Print/export

 Download as PDF 
 Printable version 

 In other projects

 Appearance

 move to sidebar 
 hide 

 From Wiktionary, the free dictionary

 This Proto-Indo-European entry contains reconstructed terms and roots . As such, the term(s) in this entry are not directly attested , but are hypothesized to have existed based on comparative evidence.

 Proto-Indo-European
 [ edit ] 

 Root
 [ edit ] 

 *peh₃- [ 1 ] [ 2 ] 

 to drink 
 Synonym: *h₁egʷʰ- 

 Alternative reconstructions
 [ edit ] 

 *peh₃(y)- [ 3 ] 

 Derived terms
 [ edit ] 

 Terms derived from the Proto-Indo-European root *peh₃- (77 c, 0 e) 

 *péh₃-t ~ *ph₃-ént ( root aorist ) 

 *pí-ph₃-e-ti ( thematic reduplicated present ) 

 *pe-póh₃-e ~ *pe-ph₃-ḗr ( reduplicated perfect ) 
 Proto-Hellenic: 
 > ? Ancient Greek: πέπωκα ( pépōka ) ( or an inner-Greek formation ) [ 2 ] 
 ⇒ ? Ancient Greek: πώνω ( pṓnō ) 

 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: पपौ ( papáu ) 

 *péh₃-mn̥ 
 Proto-Hellenic: *pṓmə 
 Ancient Greek: πῶμα ( pôma ) , πόμα ( póma ) 

 *péh₃-ti-s ~ *ph₃-téy-s 
 Proto-Hellenic: *pótis 
 Ancient Greek: πόσις ( pósis ) 

 Proto-Indo-Iranian: *pHtíš 
 Proto-Indo-Aryan: *pHtíṣ 
 Sanskrit: पीति ( pītí ) 

 *ph₃-tó-s ( past passive ) 

 *péh₃-tlo-m 
 Proto-Celtic: *ɸotlom 
 Old Irish: ól ( see there for further descendants )

 Proto-Indo-Iranian: *páHtram 
 Proto-Indo-Aryan: *páHtram 
 Sanskrit: पात्र ( pā́tra ) ( see there for further descendants )

 Proto-Italic: *pōklom 
 Latin: pōculum ( see there for further descendants )

 *peh₃-ter- 
 Proto-Indo-Iranian: 
 Proto-Indo-Aryan: 
 Sanskrit: पातृ ( pā́tṛ
```


## [2026-09-14T00:55:51.551Z] TOOL CALL #31: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pistra\\|pišta\\|pisant\\|pišan\\|pis-\\b\" BRT.txt | head -20; echo \"=== search 'Mehl'\"; grep -n \"Mehl\" BRT.txt | head -20"
}
```


### [2026-09-14T00:55:51.616Z] TOOL RESULT

```
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
=== search 'Mehl'
6149:KompE.  —  Aus  ir.  *ärla-%  %  3^2,  aSg.  — VgL  np.  äri/'Mehl',  arm.  aiü  'inablen';  Hbm. AGr.  /.  414.  —  Pü.;  artai,  (m  V.  7):  fehlt, doch  s.  NA.  ,
10408:•  j.  gunda-  m.,  gundä-  f.  'zum  Backen ! angerührtes  Mehl,  Mehlteig,  Te igb allen' :  | yat  'ds  d-:iyäl  "wenn  der  Teig  (zum  Backen) ' zurecht  gelegt  wird"  V.?.32j — lia  miimHl ..nmlne  ai)ih3i  "lAy.?/"  "hier  soll  dauernd im  Haus  vorhanden  sein  von  diesem  Mehl-  \ teig"  V.,j.32.  I
11913:r)  Inkoh.*. 'heiss'  werden':  'tafsatca  ha mai.ys  x^isatla  (sd.)  Y..9.11;  —'za/ar, tafsqn  aya  masS  "im  Maul  soll  es  ihnen durch  iim   (den  Mehlteig)   heiss   werden]
16419:•  j.piäant- Adj. 'zerstossend,  durch Stossen  si.  piffä-  n.  'Mehl'').  —  Pü.: /«oi").—  'i  Ob zerhackend">:ww37a>i«..7'är;7«a>i^wrt/a/y;  ^''  W"-  A''^'-  '■  S  235b?-»>  S.  in  '/ilfra- {%&.)  amra.namäi  'ial5  upara.»amat  Yt.  •  S-  piSyant-  Adj.,  PPA.:  s.  pah-, J4-19-                                                         I"  j.  piixJia-  Adj.  {fem.  *3ä-)  'der  fUnfte
29669:mit  pairi    'durchseihen,    filtriren':    äai\araxJ'    näm<^    anniniy^    °tahya  pu%^i^ *äsnatars  {sA.;  naml.  kairim  a»kaf\    yat  hauv  udapataiä  bäbirauv  Bh.j.  13. ..  to«^».  tüiriMnal  N.  75;  -'luum-  .  j    hasiMma-  Adj.  'der  Mehligste':  •»,« ta,r,.har,^mU  Y.  27  .(,•>;  -^  m,^_r„n,m  ^.^,,^    ^^^    „%Uili    rMm    imrm!  Y.
```


## [2026-09-14T00:55:58.271Z] TOOL CALL #32: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"pi.tra-\" BRT.txt | head -20"
}
```


### [2026-09-14T00:55:58.321Z] TOOL RESULT

```
3399:—  'rum  (GS.)  hö  rätanam  . .  isänAaaa (sd.)  Yl  ig.  53;  53';  F.  7^';  — paiH.ä3n?m ainim  baraiti  ..  diwiat  haca  'va  sauAaite V, /<y,  i;  2—4;  —  hial  n3  'va  a^aururum /ia:a  *gai>äöU  *parayat  "wie  weit  soll  ein , Priester  auf  Priesterdienst  aus  dem  Haus gehen?"  N.4; — nsit  ml  apqm  -va  aiwi/ti/. ■  vpnioye  (so.)  dai^Aava  carät  Y.p.z4;  — yS  *mainyde  davi^einti  haomimla  'va- ÄfMi"^  Y.  JO.  15; — 'runqmca  paitl.ajqinm (sd.)..^;/  *iyeyqm  düräi  as^.TsS(sd.)  dah- yunqm  V.42.6;  N.4;  —  °va  dürai/rakat5 (sd.)  Yl/ö.  17; — atl:mi  ma'irjm  mä  fra- äaisayöis  anyat  pure  vä  .  .  'va/iäi*^  vä Yti4.46;  —  °va  kqm^.na/5  Vyt^;  — 'vatum  yaoiäa'^^S  dahmayat  pars  ßfritsit ..daiiiMupailim..V.g.zT,  7.41-  A)  ins- bes.  als  Bezeichnung  für  den  eisten,  den Priesterstand  (s.  unter  ^piltra-):  "va  ra- >aistä  vastrys ßuyqt  hainsY.ig.iT,ii.S, Ytij.89,V.5.28,y*45'; — 'varum  asläya ra^alstärvm  . .  västrXm  /iüyant?m  Vr.j.  2;
5548:•  jj  g-  'airyaman-,  g.  airyäman-  m. 'Genosse'  uzw.  priesterlicher,  Angehöriger des  ersten  oder  Priesteratands  (s.  unter 'pistra-),  'Sodale' ;  Sing,  auch  koU.  'Soda- lität',  nur  gAw.:  iJ  yama  kp  x^allus  {%<!.) dätäis  anhat  yp  ,  .  Y.  /fg.  7 ;  —  ahyScH x'aSus  (sd.)  yjsal  ahyä  virizsntm  mat yamnn  . .  Y.J2.1;  —  yf  '^jvaj  masdn asruinm  . .  yazli  (sd.)  apa  K^'aüSuScä  tar>- maitTm  virn^nahyiilä  . .  'yamanascä  . .  Y. 33-4  i  —  y^  asäuia  vahiils  :^aSä  (sd.) vä  al  vä  v>r>iSny3  yämiiä  (IS.  als  Subj.)  '> vil .  .  Y.  JJ.  3;  —  pairl  clausus  'yama- nascä  dadaili  ndii  .  .  i-ir>z5nä  (sd.)  Y.46. I.  A)  Name  einer  Gottheit":  vairya sar)ha  para.äi'd  upa.vasanuha  avi  nmli' mm  yamaini  imat  sanhsis  'yamanäi  J' "A^,  geh  weg,  fahr  hin  ins  Haus  zu  A., das  sollst  du  dem  A.  kund  machen"  V.
11187:•  j.  £a9Tu.piätra-  Adj.  'vier  Stände  ent- ' haltend,  umfassend'  '• :  aUaica  vacS . .  '^ri.-  i afsnum  (sd.)  'nm  panca.ralu  Y.  75.16.
18391:'Vieh  auffüttern,  au&iehen,  Vieh  züchten"', nur  PPA.  ßuyant-  'ViehzUchter,  Freund der  Viehzucht*:  ySi  msimim  vandm  (sd.) . .  :^äü  hiiubls  /luyasü  aßuyanti  ". .  die Feinde  der  Viehzucht  unter  deren  Freun- den" 'Y.4f).ar''>;  —  nsil  »nzajySi  frajyaitis (sd.)  nsit  fsuyenlt  dngvasB  pairl  Y. 2p.  5.  a)  mit  västrya-  (sd.):  ai zl'kwa fsuyaniaila  vaslryäicä  %wSrPstä  (sd.) tatasä  Y.  29.  6;  —  at  kl  aya  ß-avantä (sd.)  västrlm  afiyai  /luyanlimY. 31.  10; Yt  10. 60.  a)  als  Bezeichnung  für  den dritten  Stand  {'pi/tra-),  'der  viehzUchtende Bauer",  geg.  a^ravan-  (Stverz.),  ra%alitar- (und  Aatay-):  ä^rava  rdSialsta  vastryS fsuyqs  hüitis  Y-ig.  17  usw.;  —  väsfrtm fluyaniim  Vr.^.  2  usw.;  —  västryai fiu-
```


## [2026-09-14T00:56:03.519Z] TOOL CALL #33: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '16410,16425p' BRT.txt"
}
```


### [2026-09-14T00:56:03.565Z] TOOL RESULT

```
■  ■*'■  5^^*  Gdn,  VSl  ?.  18.  der  aber  nur  iT.  Richtiges  gibt
•  j.   pisinah-   m.   EN.   eines   iranischen  |     KompE.  — Zum  v./fl?j.,eig. 'Färbung,  Farbe'; Fürsten  aus  der  A'af fly-Dynastie,  Enkels      vgl.  ai-  ''«™°- m-  -  np.  __vgU  >™  'Hand-
-        ..     ■'      ■'.  .'  --  werk,  Gewerbe'.  —   Vw.: ptiak  \\n  ^v..: -uiäya
des    Kaväla:    kavBü  -natths   alaonS  Yt. '
,h).
13.  132;    —  yimca   kavam    'mm  (AS.)->   ,  ^  ^^5^^»-  m.  i)  'Quetschung.  Quetsch- Ei|!'Bed.?     Ob  A(ygl.  aipty^sinah-  (zum  V.   r"*^^'    Jü"   j^'^Pfe«'   Instrument   beige- '■'■r/B''«flj-,  S2.i)?  — »Sid'/aE.   brachte  Wunde':  _>■?  jfiwe  'nm  jatntt  ytm
-   ,   —  ar."*7-i1   ,  „.„.         .  ,j  
•  j.  pisra-  m.  Bezeichnung  einer  Vor-  ^,^.^,^  ,^^  ^^J/^^^^aiW"  (sd.)  V.  5. nchtung  zum  Schweissen  von  MetaUen:  ^  ^)  '(Ausgequetschtes  sva.)  MehT: -rai  hüca  zaranyöaa!j,ät  . .  'rat  haca  ,r>-  ^^^  ,^^  ^  ^^  ia?  darva  «ru^J  "wenn ,aii^.sa^äi  'rat  haca  «ySsji^Pät .  .  'rai^;^  ^j^j^j  ^^^  Teiganmachen)  zurecht haca  haosaJnam5.,a^ilt  V.  8.  87-90.  ,  gelegt  wird,  dann  heulen  die  D."  V.  j.32.
Et.  ?    Falsch  JK.  A  hymn  44.  -  Pu. :  p  dt  ar.    «  ^^^   ^.    ^'  ^.^_^^.     _    ^^,_  ^^    ^..^    .^^^,^
•  j.piäant- Adj. 'zerstossend,  durch Stossen  si.  piffä-  n.  'Mehl'').  —  Pü.: /«oi").—  'i  Ob zerhackend">:ww37a>i«..7'är;7«a>i^wrt/a/y;  ^''  W"-  A''^'-  '■  S  235b?-»>  S.  in  '/ilfra- {%&.)  amra.namäi  'ial5  upara.»amat  Yt.  •  S-  piSyant-  Adj.,  PPA.:  s.  pah-, J4-19-                                                         I"  j.  piixJia-  Adj.  {fem.  *3ä-)  'der  fUnfte
PPA.;    Praes.  I  oder  3.    —    Vgl.  ai.  finöüi,   „mä/iyB  (näml.  ralus)  vTsyB  zanhimB  däR-
ksl.  P^l""i--  ^v^.^mtar~  O  Falsch  Cld.  j      ^^  zard^mirö  'Ib  Y.  /p.  18;  Yt  J^.  15,
KZ.  j/.  366,  vgl.  IF.  g,  261.  !-;,  ' , ,  .^        '         .  •"
^  ^  ^  j  V.  4.  2,  Vd.  72;   —  pamrjm  .  .  «»rtm  . .
•  j-,  *V- pisi'  Adj.,  nur  KompA.: -?-.   4^,»,  yamm    Y.p.ao;  V.^.  7,  28,  5.30', Vgl.  KZ.  j/.  26Ö.  I  jj  24>,  N.tf;,  <92,  Vd.  J2;  —  'osm  aSalsam
•  p.  *piäiyä'^vädä-  f.  Name  einer  syao>nanqm  V.  75. 8;  4.3a,  /.  7;  —  'oa Gegend'");  hattv . .  asiyavJ*  -rfa«  Bh.j.7;  (NSf.)  zaftjJ«/ (sd.)V./4.9;F./,/0,Vd.J2;  — —   gaumatc^  ..  udapafatä    hacä    'dayä  ''flii(NPn.)  vIspavohuYti.T,  —  'tayeiihe
```


## [2026-09-14T00:56:15.219Z] TOOL CALL #34: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport re\nt=open('b58226ca1420e6c7.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+6000])\nEOF"
}
```


### [2026-09-14T00:56:16.330Z] TOOL RESULT

```
From Wiktionary, the free dictionary

 See also: بست , پشت , and تست 

 Persian
 [ edit ] 

 Etymology 1
 [ edit ] 

 Compare Armenian պստիկ ( pstik ) .

 Adjective
 [ edit ] 

 Dari

 پست 

 Iranian Persian

 Tajik

 паст 

 پست • ( past ) ( Tajik spelling паст ) 

 low 

 abject , ignoble 
 Mehdi Akhavan-Sales , Khan-e Hashtom 
 پهلوان هفت خوان، اکنون

طعمه ی دام و دهان خوان هشتم بود
و می اندیشید
که نبایستی بگوید، هیچ
بس که بی شرمانه و پست است این تزویر. The hero of the Seven Labours,
Was the prey of trap and mouth of the eighth labour now.
And he was thinking
That he should not say anything
For this trick is such a shameless and ignoble one. 

 Descendants
 [ edit ] 

 → Kazakh: пәс ( päs ) 

 → Turkmen: pes 

 Etymology 2
 [ edit ] 

 Noun
 [ edit ] 

 پست • ( pist / pest ) ( Tajik spelling пист ) 

 flour , meal 

 browned flour 

 Etymology 3
 [ edit ] 

 Etymology tree

 Proto-Indo-European *h₂ep 

 Proto-Indo-European *-o 

 Proto-Indo-European *h₂epó 
 Proto-Indo-European *h₂pó 
 Proto-Italic *po 

 Proto-Indo-European *teḱ- 

 Proto-Indo-European *-éyti 

 Proto-Indo-European *tḱéyti bf. 
 Proto-Indo-European *tḱey- 

 Proto-Indo-European *-né- 

 Proto-Indo-European *-ti 

 Proto-Indo-European *tḱinéti 
 Proto-Italic *sinō 

 Proto-Italic *pozinō 
 Latin pōnō 
 Latin positus 
 Italian posto bor. 
 French poste bor. 
 Persian پست 

 Borrowed from French poste .

 Noun
 [ edit ] 

 Dari

 پوسته 

 Iranian Persian

 پست 

 Tajik

 почта 

 پست • ( post ) 

 post 
 Synonyms: برید ( barid ) , چاپار ( čâpâr ) 

 email 

 Derived terms
 [ edit ] 

 اداره پست ( edâre-ye post , “ post office ” ) 
 پست الکترونیکی ( post-e elektroniki , “ email ” ) 
 پست کردن ( post kardan , “ to send by post ” ) 
 پستخانه ( post-xâne , “ post office ” ) 
 پستچی ( post-či , “ mailman ” ) 
 پستی ( posti , “ postal ” ) 
 کد پستی ( kod-e posti , “ postcode ” ) 

 Retrieved from " https://en.wiktionary.org/w/index.php?title=پست&oldid=92019380 "

 Categories : Persian lemmas 
 Persian adjectives 
 Persian terms with quotations 
 Persian nouns 
 Persian terms derived from the Proto-Indo-European word *h₂epó 
 Persian terms derived from Latin 
 Persian terms derived from the Proto-Indo-European root *teḱ- 
 Persian terms borrowed from French 
 Persian terms derived from Proto-Indo-European 
 Persian terms derived from the Proto-Indo-European root *tḱey- 
 Persian terms derived from Proto-Italic 
 Persian terms derived from Italian 
 Persian terms derived from French 

 Hidden categories: Pages with entries 
 Pages with 1 entry 
 Requests for transliteration of Persian quotations 
 Pages with etymon 
 Persian entries with etymon 
 Pages with etymology trees 
 Persian entries with etymology trees 
 Persian entries with etymology texts 
 Pages using etymon with no ID 
 Persian entries referencing pages with etymology sections missing etymons 

 This page was last edited on 15 August 2026, at 21:23.

 Definitions and other text are available under the Creative Commons Attribution-ShareAlike License ; additional terms may apply. By using this site, you agree to the Terms of Use and Privacy Policy. 

 Privacy policy 

 About Wiktionary 

 Disclaimers 

 Legal & safety contacts 

 Code of Conduct 

 Developers 

 Statistics 

 Cookie statement 

 Mobile view 

 Search 

 Search 

 Toggle the table of contents 

 پست 

 9 languages 

 Add topic
```


## [2026-09-14T00:56:27.112Z] TOOL CALL #35: Bash

```json
{
 "command": "pdftoppm -f 404 -l 404 -r 200 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404 && ls -la /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/"
}
```


### [2026-09-14T00:56:28.801Z] TOOL RESULT

```
total 2216
drwx------ 2 sfmqrb sfmqrb   4096 Sep 13 20:56 .
drwx------ 4 sfmqrb sfmqrb   4096 Sep 13 20:49 ..
-rw-rw-r-- 1 sfmqrb sfmqrb    592 Sep 13 20:53 agents.txt
-rw-rw-r-- 1 sfmqrb sfmqrb  95654 Sep 13 20:53 bqt390_436_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  34040 Sep 13 20:54 bqt390_436_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 124665 Sep 13 20:53 bqt390_662_foot.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb  93636 Sep 13 20:53 bqt390_662_top.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 537986 Sep 13 20:53 bqt390_n436.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb 527696 Sep 13 20:53 bqt390_n662.jpg
-rw-rw-r-- 1 sfmqrb sfmqrb   3627 Sep 13 20:54 crop14-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb   4873 Sep 13 20:54 crop18-394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  55136 Sep 13 20:50 pg390.png
-rw-rw-r-- 1 sfmqrb sfmqrb  75438 Sep 13 20:56 pg392.png
-rw-rw-r-- 1 sfmqrb sfmqrb 145431 Sep 13 20:54 pg394hi.png
-rw-rw-r-- 1 sfmqrb sfmqrb  96039 Sep 13 20:53 pg394.png
-rw-rw-r-- 1 sfmqrb sfmqrb  72433 Sep 13 20:54 pg397.png
-rw-rw-r-- 1 sfmqrb sfmqrb  77067 Sep 13 20:55 pg398.png
-rw-rw-r-- 1 sfmqrb sfmqrb  64776 Sep 13 20:54 pg399.png
-rw-rw-r-- 1 sfmqrb sfmqrb  71542 Sep 13 20:56 pg404.png
-rw-rw-r-- 1 sfmqrb sfmqrb  21327 Sep 13 20:55 pg408-ampus.png
-rw-rw-r-- 1 sfmqrb sfmqrb  33681 Sep 13 20:55 pg408-germ.png
-rw-rw-r-- 1 sfmqrb sfmqrb  78365 Sep 13 20:54 pg408.png
-rw-rw-r-- 1 sfmqrb sfmqrb     40 Sep 13 20:53 queue.txt
```


## [2026-09-14T00:56:31.605Z] TOOL CALL #36: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404.png"
}
```


### [2026-09-14T00:56:32.037Z] TOOL RESULT

```

```


## [2026-09-14T00:56:32.034Z] INPUT

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]


## [2026-09-14T00:56:49.028Z] TOOL CALL #37: Bash

```json
{
 "command": "pdftoppm -f 404 -l 404 -r 500 -png -singlefile EtymologicalDictionary-persian-english.pdf /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404hi && python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404hi.png')\nprint(im.size)\nW,H=im.size\n# persian symposium node approx x 940-1200/1545, y 1080-1170/2000\nim.crop((int(0.60*W),int(0.535*H),int(0.80*W),int(0.585*H))).resize((int(0.20*W*2),int(0.05*H*2))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-symp.png')\nim.crop((int(0.38*W),int(0.485*H),int(0.80*W),int(0.535*H))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-empty.png')\nim.crop((int(0.60*W),int(0.42*H),int(0.80*W),int(0.49*H))).save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-patil.png')\n\""
}
```


### [2026-09-14T00:56:52.692Z] TOOL RESULT

```
(4250, 5500)
```


## [2026-09-14T00:56:55.222Z] TOOL CALL #38: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-symp.png"
}
```


### [2026-09-14T00:56:55.249Z] TOOL RESULT

```

```


## [2026-09-14T00:57:09.745Z] TOOL CALL #39: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404hi.png')\nW,H=im.size\nc=im.crop((int(0.665*W),int(0.553*H),int(0.755*W),int(0.575*H)))\nc=c.resize((c.width*3,c.height*3),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-symp2.png')\nprint(c.size)\n\""
}
```


### [2026-09-14T00:57:11.284Z] TOOL RESULT

```
(1146, 363)
```


## [2026-09-14T00:57:13.401Z] TOOL CALL #40: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-symp2.png"
}
```


### [2026-09-14T00:57:13.438Z] TOOL RESULT

```

```


## [2026-09-14T00:57:19.160Z] TOOL CALL #41: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-empty.png"
}
```


### [2026-09-14T00:57:19.175Z] TOOL RESULT

```

```


## [2026-09-14T00:57:23.272Z] TOOL CALL #42: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-patil.png"
}
```


### [2026-09-14T00:57:23.287Z] TOOL RESULT

```

```


## [2026-09-14T00:57:28.900Z] TOOL CALL #43: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404hi.png')\nW,H=im.size\nc=im.crop((int(0.72*W),int(0.150*H),int(0.79*W),int(0.175*H)))\nc=c.resize((c.width*4,c.height*4),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-pest.png')\n\""
}
```


### [2026-09-14T00:57:30.712Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:57:32.726Z] TOOL CALL #44: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-pest.png"
}
```


### [2026-09-14T00:57:32.742Z] TOOL RESULT

```

```


## [2026-09-14T00:57:48.838Z] TOOL CALL #45: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%AA/\" --note \"page 404, root Pis: Mo'in/Dehkhoda entry for پست (flour)\" 2>&1 | tail -3"
}
```


### [2026-09-14T00:57:51.862Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/9653781727c7882c.txt
```


## [2026-09-14T00:57:54.490Z] TOOL CALL #46: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"آرد\\|معین\\|دهخدا\\|pest\\|pist\" 9653781727c7882c.txt | head -40"
}
```


### [2026-09-14T00:57:54.591Z] TOOL RESULT

```
20: لغت نامه دهخدا
74: فرهنگ معین
77: ( ~. ) [ فر. ] (اِ. ) ۱ - کار رساندن نامه ها و بسته ها از جایی به جای دیگر. ۲ - سازمانی که عهده دار این کار است . ۳ - محل خدمت . ۴ - شغل و مقام اداری . ۵ - وظیفة معین هر بازیکن در بازی های گروهی ، نقش (فره ). ،~ الکترونیک ایمیل . ، ~ اکسپرس نوعی خدمات 
79: (پِ یاپَ ) (اِ. ) ۱ - هر نوع آرد. ۲ - آرد بریان شدة گندم یا جو. ۳ - سپوس ، پوست گندم یا جو. 
97:۱. آرد.
98:۲. آرد بوداده، آرد گندم یا جو یا نخود بریان کرده: منم روی از جهان در گوشه کرده / کفی پست جوین ره توشه کرده (نظامی۲: ۱۰۷ ).
110: /pest/ آرد بریان شده
114: ( پِست ) ( ن ) ؛ مخلوطی از خاک قند و آردگندم برشته ( یا آرد کنار ) ؛ پودر شده هر چیز؛ نماد ریزی و پودری
261: پِست در پارسی میانه به معنی آرد تفته است.
288:کردی: pist / post
338:منبع لغت نامه دهخدا
415: پِست با تلفظ pest
425: به پِست و شِکَر بیامیخت: پِست، آردی که گندم و جو و نخود آن را بریان کرده باشند. [برهان قاطع] واژه ئی که به وفور در متون کهن به کار رفته. در لهجه ی طبری به آن پِهِه گویند[واژه نامه ی طبری، ص ٨٧] ترکیب و طرز ساختن آن را مادربزرگ ها به یاد دارند: گندم، جو و ذرّت را از هر کدام به مقدار مساوی با مقدار برنج و با مقدار مساوی تخم هندوانه و خربزه و گاورس با مقداری داردانه ( که در کوه ها می چینند، به قصد معطر کردن ) پس از تمیز کردن پاک می شویند، خشک می کنند، تَفت می دهند و سپس آسیا می کنند و پس از الک کردن نرمه ی آردی از آن باقی می ماند که همان پِست است، غالباً با شکر یا خاکه قند می آمیزند. 
430:به پِست و شِکَر بیامیخت: پِست، آردی که گندم و جو و نخود آن را بریان کرده باشند. [برهان قاطع] واژه ئی که به وفور در متون کهن به کار رفته. در لهجه ی طبری به آن پِهِه گویند[واژه نامه ی طبری، ص ٨٧] ترکیب و طرز ساختن آن را مادربزرگ ها به یاد دارند: گندم، جو و ذرّت را از هر کدام به مقدار مساوی با مقدار برنج و با مقدار مساوی تخم هندوانه و خربزه و گاورس با مقداری داردانه ( که در کوه ها می چینند، به قصد معطر کردن ) پس از تمیز کردن پاک می شویند، خشک می کنند، تَفت می دهند و سپس آسیا می کنند و پس از الک کردن نرمه ی آردی از آن باقی می ماند که همان پِست است، غالباً با شکر یا خاکه قند می آمیزند. 
436: پِست:آرد ، گرد چیزی
457: آبادیس از سال 1385 فعالیت خود را در زمینه فن آوری اطلاعات آغاز کرد. نخستین پروژه آبادیس، سایت دیکشنری آبادیس بود. دیکشنری آنلاین آبادیس از ابتدا تاکنون تغییرات بسیاری کرده و ویژگی های مختلفی به آن اضافه شده است. آبادیس افزونه ای کاربردی برای مرورگرهای فایرفاکس و کروم و اپلیکیشن موبایل طراحی کرده است که میتوانید از لینک های بالا دانلود کنید. دیکشنری آبادیس شامل بخش هایی نظیر دیکشنری به زبان های مختلف از جمله انگلیسی، فارسی، عربی و همچنین بیست دیکشنری تخصصی با تلفظ انگلیسی و آمریکایی، ترجمه مخفف و کلمات اختصاری، مترجم آنلاین متن، لغتنامه دهخدا، فرهنگ معین، فرهنگ فارسی عمید، فرهنگ مترادف ها و متضاد ها، معادل فارسی کلمه یا به شیوه درست تر برابر پارسی واژه، فرهنگ سره، عبارات مصوب فرهنگستان زبان و ادب فارسی، دانشنامه عمومی، دانشنامه اسلامی، دیکشنری نام ها، هم خانواده یاب، تصویر مرتبط با کلمه، معنی در حل جدول کلمات متقاطع و ابزارهایی مانند واژه ساز ، راهنمای انتخاب اسم و ... می باشد.
```


## [2026-09-14T00:58:06.884Z] TOOL CALL #47: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"symposium\" KLN_1966.txt | head -10; echo \"=== 1971\"; grep -n \"symposium\" KLN_1971.txt | head -10"
}
```


### [2026-09-14T00:58:06.950Z] TOOL RESULT

```
29830:potion,  n.,  a  drink;  a  dose  of  liquid  medicine  or poison.  —  ME.  pocioun,  fr.  MF.  (—  F.)  potion, fr.  L.  pdtionem,  acc.  of  polio,  ‘a  draft,  drink’, rel.  to  potare ,  ‘to  drink’,  potor,  ‘drinker’,  pocu- lum  (for  *pdtlom),  ‘a  drinking  cup’,  posca,  ‘a drink  of  vinegar  and  water’,  fr.  I.-E.  base  *po(i)-, *pi-,  ‘to  drink’,  whence  also  OI.  pad,  ‘drinks’, payayati,  payate,  ‘gives  to  drink’,  Arm.  impem, ‘I  drink’,  Gk.  irfvsiv,  ‘to  drink’,  -kqgic,,  ‘a  drink’, •jtoTov,  ‘that  which  one  drinks,  a  drink’,  tcoto?, ‘a  drinking,  a  drinking  bout’,  n 6t»]s,  ‘drinker’, 7roTr)p,  7TOT7)pi,ov,  ‘a  drinking  cup’,  Alb.  pi,  ‘I drink’,  OSlav.  pijg,  piti,  ‘to  drink’,  pivo,  ‘bever¬ age’,  Russ.,  Czech,  Slovak,  etc.,  pivo,  ‘beer’, OPruss.  poiit,  ‘to  drink’,  poieiti,  ‘drink!’  (pi.), OIr.  ibim,  ‘I  drink’,  OI.  plbati,  ‘drinks’,  L.  bibere (assimilated  fr.  *pibere),  ‘to  drink'.  See  bibulous and  -ion  and  cp.  poison,  which  is  a  doublet  of potion.  Cp.  also  potable,  potation,  Poterium, potomania,  potometer,  pawnee,  Pistia,  pour- boire,  propine,  symposium.  Cp.  also  the  second element  in  Hydropotes.
37829:symposiac,  adj.,  pertaining  to  a  symposium.  —  L. symposiacus,  fr.  Gk.  oupTroataxo?,  ‘pertaining to,  or  fit  for,  a  drinking  party’,  fr.  aupjrootov. See  symposium  and  -ac.
37830:symposial,  adj.,  pertaining  to  a  symposium.  — Formed  fr.  symposium  with  adj.  suff.  -al. symposiarch,  n.,  president  of  a  symposium.  —  Gk auprroaiapyoq,  compounded  of  aupxoaiov, ‘drinking  party’,  and  ‘leader,  chief  ruler’.
37831:See  next  word  and  -arch, symposium,  n.,  1)  in  ancient  Greece,  a  drinking party ;  2)  a  meeting,  conference  for  conversation or  discussion.  —  L.,  fr.  Gk.  aupndaiov,  ‘a  drink¬ ing  feast’,  lit.  ‘a  drinking  together’,  fr.  auv  (see syn-)  and  x6ai?,  ‘a  drinking’,  which  is  rel.  to 7uveiv,  ‘to  drink’.  See  potion, symptom,  n.  —  Late  L.  symptoma,  fr.  Gk. oupimopa,  ‘chance,  occurrence’,  lit.  ‘a  falling together’,  fr.  aupirlrtTeiv,  ‘to  fall  together’,  fr. auv  (see  syn-)  and  irtTrreiv,  ‘to  fall’,  which
=== 1971
188741:boire, propine, symposium. Cp. also the second 
239101:symposiac, adj., pertaining to a symposium. — L. 
239104:See symposium and -ac. 
239106:symposia!, adj., pertaining to a symposium. — 
239107:Formed fr. symposium with adj. suff. -al. 
239109:symposiarch, n., president of a symposium. — Gk 
239114:symposium, n., 1) in ancient Greece, a drinking
```


## [2026-09-14T00:58:12.387Z] TOOL CALL #48: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37700 && NR<=37835' KLN_1966.txt | grep -n \"^[0-9]\\{3,4\\}\\|155[0-9]\\|156[0-9]\" | head -20"
}
```


### [2026-09-14T00:58:13.380Z] TOOL RESULT

```
1:1553
29:Swertia,  n.,  a  genus  of  plants  of  the  gentian family  (bot.)  —  ModL.,  named  after  the  Dutch botanist  Emanuel  Swert  (Sweert)  (born  in  1552). For  the  ending  see  1st  suff.  -ia. swerve,  intr.  and  tr.  v.,  to  turn  aside  —  ME.  swer- ven,  fr.  OE.  sweorfan,  ‘to  scrub,  file’,  rel.  to  ON. sverfa,  ‘to  scour,  file’,  OS.  swebran,  ‘to  wipe  off’, OFris.  swerva,  ‘to  rove’,  OHG.  swerban,  ‘to wipe,  rub’,  Du.  zwerven,  ‘to  rove,  wander', Goth,  af-swairban,  ‘to  wipe  off’,  and  possibly cogn.  with  W.  chwerfu,  ‘to  whirl,  roll’,  and  with Gk.  aupsiv,  to  trail,  drag,  sweep  away’.  See syrma.
62:1554
69:1555
107:1556
```


## [2026-09-14T00:58:15.717Z] TOOL CALL #49: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37800 && NR<=37860' KLN_1966.txt | grep -n \"^155[0-9]$\\|^156[0-9]$\" "
}
```


### [2026-09-14T00:58:16.780Z] TOOL RESULT

```
7:1556
```


## [2026-09-14T00:58:19.594Z] TOOL CALL #50: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37806 && NR<=37900' KLN_1966.txt | grep -n \"^155[0-9]$\\|^156[0-9]$\"; echo \"--- lines 37806-37840 numbering context\"; sed -n '37806,37812p;37826,37836p' KLN_1966.txt | cut -c1-120"
}
```


### [2026-09-14T00:58:20.735Z] TOOL RESULT

```
1:1556
--- lines 37806-37840 numbering context
1556
symbolic,  symbolical,  adj.  —  L.  symbolicus,  fr. Gk.  aupjioXtxo;,  ‘pertaining  to  a  symbol’,  fr. <jdp(3o
symbolist,  n.,  1)  one  who  uses  symbols;  2)  one versed  in  the  interpretation  of  symbols;  3)  one who  regar
Derivatives:  symbolist,  symbolist-ic,  symbolist- ic-al,  adjs.,  symbolist-ic-al-ly,  adv. symbolization,  n.  —  F
Derivative:  symboliz-er,  n. symbolo-,  combining  form  meaning  ‘symbol’.  See symbol.
symbology,  n.,  the  study  of  symbols.  —  Contrac¬ tion  of  symbolology,  fr.  Gk.  aupfioXov,  ‘token, symbol
Derivatives:  symbolog-ic-al,  adj.,  symbolog-ist, n.
Symplocos,  n.,  a  genus  of  plants,  the  sweetleaf (bot.)  —  ModL.,  fr.  Gk.  aupTCXoxo;,  ‘connect¬ ed’,  
sympodium,  n.,  an  apparent  main  axis  composed of  successive  branches  (bot.)  —  ModL.,  formed fr.  sym-  and
Derivatives:  sympodi-al,  adj.,  sympodi-al-ly, adv.
symposiac,  adj.,  pertaining  to  a  symposium.  —  L. symposiacus,  fr.  Gk.  oupTroataxo?,  ‘pertaining to,  or  
symposial,  adj.,  pertaining  to  a  symposium.  — Formed  fr.  symposium  with  adj.  suff.  -al. symposiarch,  n., 
See  next  word  and  -arch, symposium,  n.,  1)  in  ancient  Greece,  a  drinking party ;  2)  a  meeting,  conference
symptomatic
37  Mcl
stands  for  *m-Ttxeiv,  fr.  *pt~,  zero  degree  of I.-E.  base  *pet-,  ‘to  fly,  to  fall’.  See  feather  and 
symptomatic,  adj.  —  Late  L.  symptomaticus,  fr. symptoma,  gen.  -atis.  Cp.  Gk.  aup.Trxcop.aTi.xoi;, ‘accide
-atic.
```


## [2026-09-14T00:58:27.657Z] TOOL CALL #51: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37830 && NR<=37900 && /^15[0-9][0-9]$/{print NR\": \"$0}' KLN_1966.txt | head"
}
```


### [2026-09-14T00:58:28.711Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T00:58:30.717Z] TOOL CALL #52: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR>=37830 && NR<=38000 && /^ *15[0-9][0-9] *$/{print NR\": \"$0}' KLN_1966.txt | head"
}
```


### [2026-09-14T00:58:31.821Z] TOOL RESULT

```
37971: 1565
```


## [2026-09-14T00:58:38.012Z] TOOL CALL #53: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"beverage\" AHD_watkins1985.txt | head -10"
}
```


### [2026-09-14T00:58:38.099Z] TOOL RESULT

```
148:The names for a number of insects can be reconstructed in the protolanguage, includ- ing the wasP (wopsa), the hornet (*kras-ro-, a derivative of ker-', “head,” from the shape of the insect), and the fly (mu-2). The BEE (bhei-') was particularly important as the producer of honey, for which we have the common Indo-European name melit-. Honey was the only source of sugar and sweetness (swad-, “sweet,” is ancient), and notably was the base of the only certain Indo-European alcoholic beverage, MEAD, medhu-, meaning in different dialects both “mead” (“wine” in Greece) and “honey.” The Germanic lan- guages have innovated, perhaps from a taboo on speaking the name while gathering wild honey; the common Germanic English word HONEY is from an old color adjective for “yellow,” k(e)neko-.
865:pdo(i)-. To drink. Contracted from *poo(i)-. I. Basic form *p6(i)-. 1. Suffixed reduced form *pd-to- in Latin pdtus, drunk (> pdtdre, to drink): POISON, POTABLE, POTATION, POTATORY, POTION. 2. Reduplicated form *pi-poa-o-, whence *pi-bo-, assimilated to *bi-bo- in Latin bibere, to drink: BEVERAGE, BIB, BIBULOUS; IMBIBE. 3. Suffixed zero-grade form *po-ti-, *po-ti- in Greek posis, drink, drinking: sympostum. II. Zero-grade form *pi- (< *pia-). 1. Suffixed form *pi-ro- in Old Church Slavonic piri, feast (> Russian pir, feast): prroG. 2. Suffixed (nasal present) form *pi-no- in Greek pinein, to drink: prnocy- tosis. [Pok. 2. pd(i)- 839.]
1294:BENIGN deu-?, gene- BENTHOS gWadh- BENUMB nem- BEQUEATH gWet-2 BEQUEST gWet-2 BEREAVE reup- BERM bhrem-2 BERRY bha-1 BERSERKER bher-3 BESPEAK spreg- BESPRENT spergh- BEsT bhad- BETOKEN deik- BETRAY d6- BETROTH deru BETTER bhad- BETWEEN dwo- BETWIXT dwo- BEVEL bat- BEVERAGE pO(i)- BEWITCH weik-2 BEZOAR gWhen-1, pa- BHAGAVAD-GITA g@i-2 BI- dwo-
```


## [2026-09-14T00:58:50.319Z] TOOL CALL #54: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"^beer,\\|beer,  n\" KLN_1966.txt | head -5; echo ---; grep -n \"BEER\" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-14T00:58:50.387Z] TOOL RESULT

```
4652:been,  pp.  of  be.  —  ME.  ben,  fr.  OE.  beon,  ‘been’, pp.  of  beon,  ‘to  be’,  See  be. beer,  n.  —  OE.  beor,  rel.  to  OS.,  OHG.  bior,  ON. fi/orr,  OFris.fi/dr, MLG., MDu.  her,  Du.,  MHG., G.  bier,  fr.  Eccles.  L.  biber  (pi.  biberes),  ‘drink, beverage’,  fr.  L.  bibere,  ‘to  drink’.  See  beverage. Derivatives:  beer-ish,  adj.,  beerish-ly,  adv.,  beer- y,  adj.,  beer-i-ly,  adv.,  beer-i-ness,  n. beestings,  biestings,  n.,  first  milk  of  a  cow  after calving.  —  ME.  bestinge,  fr.  OE.  bysting,  fr. by st,  beost,  which  is  rel.  to  OS.,  OHG.  biost, MDu.,  Du.,  MHG.,  G.  biest,  ‘beestings’,  and  in vowel  gradation  to  Norw.  budda  (for  Vruzda), ‘beestings’,  fr.  I.-E.  base  *bhou-,  *bhu-,  ‘to  swell’. See  belly.
34976:shillibeer,  n.,  1)  an  omnibus;  2)  a  hearse  with  seats for  the  mourners.  —  Named  after  the  English coach  builder  George  Shillibeer  (1797-1866). shilling,  n.  — -  ME.  schilling,  shilling,  fr.  OE. scilling,  rel.  to  OS.,  Dan.,  Swed.,  OFris.,  OHG. skilling,  ON.  skillingr,  MDu.  scillinc,  scellinc, Du.  schelling,  MHG.  schillinc,  G.  Schilling, Goth,  skilliggs,  fr.  Teut.  * skilling ,  prob.  assimi¬ lated  fr.  *skildling,  and  rel.  to  Goth,  skildus,  OE. scield,  sceld,  etc.,  ‘shield’  (see  shield,  n.) ;  formed with  -ing,  a  suff.  used  in  the  Teut.  languages  to form  nouns  denoting  coins  (cp.  farthing,  penny). shilly-shally,  n.  and  intr.  v.  —  From  former  shill I  —  shall  I,  from  the  old  subjunctive  shill  I  ? and  the  indicative  shall  II shim,  n.,  a  slip  of  wood.  —  Of  unknown  origin. Derivatives:  shim,  tr.  v.,  to  fill  with  a  shim, shimm-er,  n.
---
```


## [2026-09-14T00:58:56.480Z] TOOL CALL #55: Bash

```json
{
 "command": "for u in \"https://www.etymonline.com/word/beer\" \"https://www.etymonline.com/word/poison\" \"https://www.etymonline.com/word/beverage\"; do python3 tools/fetch_source.py \"$u\" --note \"page 404 root Po 2: English descendants\"; done 2>&1 | tail -5"
}
```


### [2026-09-14T00:58:58.623Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/a2a69e82434d7fe6.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/1b4e221f1b6bbffd.txt
/home/sfmqrb/git/rishe/data/verification/sources/web/8dd1ac41265d48c0.txt
```


## [2026-09-14T00:59:02.427Z] TOOL CALL #56: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && for f in a2a69e82434d7fe6 1b4e221f1b6bbffd 8dd1ac41265d48c0 f1d41b1a5d5e611a; do echo \"=== $f\"; python3 - \"$f\" <<'EOF'\nimport sys,re\nt=open(sys.argv[1]+'.txt',encoding='utf-8').read()\ni=t.find('Advertisement')\ni2=t.find('(n.)')\nprint(t[max(0,i2-200):i2+1800] if i2>0 else t[:1500])\nEOF\ndone"
}
```


### [2026-09-14T00:59:03.817Z] TOOL RESULT

```
=== a2a69e82434d7fe6
lumns 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of beer 

 beer (n.) 

 alcoholic drink made from grain (generally barley), infused with hops and boiled and fermented, Middle English ber , from Old English beor "strong drink, beer, mead," cognate with Old Frisian biar , Middle Dutch and Dutch bier , Old High German bior , German Bier ; a West Germanic word of much-disputed and ambiguous origin.

 It is probably a 6c. West Germanic monastic borrowing of Vulgar Latin biber "a drink, beverage" (from Latin infinitive bibere "to drink," from PIE root *po(i)- "to drink"). Another suggestion is that it comes from Proto-Germanic *beuwoz- , from *beuwo- "barley." The native Germanic word for the beverage was the one that yielded ale (q.v.). "The word occurs in OE., but its use is rare, except in poetry, and it seems to have become common only in the 16th c. as the name of a hopped malt liquor." [OED]

 Beer was a common drink among most of the European peoples, as well as in Egypt and Mesopotamia, but was known to the Greeks and Romans only as an exotic product. [Buck] 

 They did have words for it, however. Greek brytos , used in reference to Thracian or Phrygian brews, was related to Old English breowan "brew;" Latin zythum is from Greek zythos , first used of Egyptian beer and treated as an Egyptian word but perhaps truly Greek and related to zymē "leaven."

 Spanish cerveza is from Latin cervesia "beer." Old Church Slavonic pivo , source of the general Slavic word for "beer," is originally "a drink" (compare Old Church Slavonic piti "drink"). French bière is a 16c. borrowing from German. U.S. slang beer goggles , through which every potential romantic partner looks desirable, is from 1986.

 Entries linking to beer 

 ale (n.) 

 "intoxicating liquor made by malt fermentation," Old English ealu "ale, beer," from Proto-Germanic *aluth- (s
=== 1b4e221f1b6bbffd
s 
 Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of poison 

 poison (n.) 

 c. 1200, poisoun , "a deadly potion or substance," also figuratively, "spiritually corrupting ideas; evil intentions," from Old French poison , puison (12c., Modern French poison ) "a drink," especially a medical drink, later "a (magic) potion, poisonous drink" (14c.), from Latin potionem (nominative potio ) "a drinking, a drink," also "poisonous drink" (Cicero), from potare "to drink" (from PIE root *po(i)- "to drink").

 A doublet of potion . For similar form evolution from Latin to French, compare raison from rationem , trahison from traditionem . The more usual Indo-European word for this is represented in English by virus . The Old English word was ator (see attercop ) or lybb (cognate with Old Norse lyf "medicinal herbs;" see leaf (n.)).

 For sense evolution, compare Old French enerber , enherber "to kill with poisonous plants." In many Germanic languages "poison" is named by a word equivalent to English gift (such as Old High German gift , German Gift , Danish and Swedish gift ; Dutch gift , vergift ). This shift might have been partly euphemistic, partly by influence of Greek dosis "a portion prescribed," literally "a giving," used by Galen and other Greek physicians to mean an amount of medicine (see dose (n.)).

 Of persons detested or regarded as exerting baleful influence, by 1910. The slang meaning "alcoholic drink" is by 1805 in American English ( p otus as a past-participle adjective in Latin meant "drunken").

 As an adjective from 1520s; with plant names from 18c. Poison ivy is recorded by 1784 for a shrub-vine of North America causing an itching rash on contact; poison oak for poison ivy or related species is by 1743. Poison sumac (1817), causing an even more severe rash, is a swamp-border tree noted for the brilliant red of its leaves in fall
=== 8dd1ac41265d48c0
Forum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of beverage 

 beverage (n.) 

 "drink of any kind," mid-13c., from Anglo-French beverage , Old French bevrage , from Old French boivre "to drink" (Modern French boire ; from Latin bibere "to imbibe;" from PIE root *po(i)- "to drink") + -age , suffix forming mass or abstract nouns (see -age ).
 also from mid-13c. 

 Entries linking to beverage 

 bevy (n.) 

 early 15c., collective noun of quails and ladies, from Anglo-French bevée , which is of unknown origin. One supposed definition of the word is "a drinking bout," but this perhaps is a misprint of bever (see beverage ). If not, perhaps the original sense is birds gathered at a puddle or pool for drinking or bathing. But the quest for a clear and logical origin in such a word might be futile. "These old names for companies of men and animals are however very fantastical and far-fetched" [OED].

 -age 

 word-forming element in nouns of act, process, function, condition, from Old French and French -age , from Late Latin -aticum "belonging to, related to," originally neuter adjectival suffix, from PIE *-at- (source of Latin -atus , past participle suffix of verbs of the first conjugation) + *-(i)ko- , secondary suffix forming adjectives (see -ic ).

 *po(i)- 

 *pō(i)- , Proto-Indo-European root meaning "to drink."

 It might form all or part of: beer ; bever ; beverage ; bib ; bibitory ; bibulous ; hibachi ; imbibe ; imbrue ; pinocytosis ; pirogi ; poison ; potable ; potation ; potion ; symposium .

 It might also be the source of: Sanskrit pati "drinks," panam "beverage;" Greek pinein "to drink," poton "that which one drinks," potos "drinking bout;" Latin potare "to drink," potio "a potion, a drinking," also "poisonous draught, magic potion;" Old Church Slavonic piti "to drink," pivo "beverage."

 Advertisement Want to remove ads? Log in to
=== f1d41b1a5d5e611a
rum 
 Apps 
 Premium 

 Log in 

 Advertisement Remove Ads 
 Want to remove ads? Log in to see fewer ads, and become a Premium Member to remove all ads.

 Origin and history of symposium 

 symposium (n.) 

 "convivial meeting for drinking, conversation, and intellectual stimulation," 1711, from Latin symposium "drinking party, symposium," from Greek symposion "drinking party, convivial gathering of the educated" (related to sympot ē s "drinking companion"), from assimilated form of syn- "together" (see syn- ) + posis "a drinking," from a stem of Aeolic ponen "to drink" (from PIE root *po(i)- "to drink")

 The symposium usually followed a dinner, for the Greeks did not drink at meals. Its enjoyment was heightened by intellectual or agreeable conversation, by the introduction of music or dancers, and by other amusements. [Century Dictionary] 

 Reflecting the Greek fondness for mixing wine and intellectual discussion, the modern sense is especially from the word being used as a title for one of Plato's dialogues. 

 Earlier in English as "account of a gathering or party" (1580s, the title of Plato's work). The sense of "a meeting on some subject" is from 1784. The Greek plural is symposia , an attendee is a symposiast , and the leader of one is a symposiarch (c. 1600 in English). Related: Symposiac (adj.); symposial ; sympotical .
 also from 1711 

 Entries linking to symposium 

 *po(i)- 

 *pō(i)- , Proto-Indo-European root meaning "to drink."

 It might form all or part of: beer ; bever ; beverage ; bib ; bibitory ; bibulous ; hibachi ; imbibe ; imbrue ; pinocytosis ; pirogi ; poison ; potable ; potation ; potion ; symposium .

 It might also be the source of: Sanskrit pati "drinks," panam "beverage;" Greek pinein "to drink," poton "that which one drinks," potos "drinking bout;" Latin potare "to drink," potio "a potion, a drinking," also "poisonous draught, magic potion;" Old Church Slavonic piti "to drink," pivo "beverage."

 syn- 

 word-forming element of Greek
```


## [2026-09-14T00:59:14.151Z] TOOL CALL #57: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nt=open('0af573ddd8850565.txt',encoding='utf-8').read()\ni=t.find('From Wiktionary')\nprint(t[i:i+3000])\nEOF"
}
```


### [2026-09-14T00:59:15.296Z] TOOL RESULT

```
d
```


## [2026-09-14T00:59:17.768Z] TOOL CALL #58: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && head -20 0af573ddd8850565.txt; wc -c 0af573ddd8850565.txt"
}
```


### [2026-09-14T00:59:17.813Z] TOOL RESULT

```
URL: https://en.wiktionary.org/wiki/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84
FETCHED: 2026-09-14T00:55:38Z
STATUS: -1
TITLE: 

FETCH FAILED: HTTP Error 404: Not Found156 0af573ddd8850565.txt
```


## [2026-09-14T00:59:22.407Z] TOOL CALL #59: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/\" --note \"page 404, root Po 2: Mo'in/Dehkhoda entry for پاتیل\" 2>&1|tail -2; echo ---; cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"پاتیل\" incoming/ARY/ARY_pages.txt | head -10; echo \"=== BQT\"; grep -n \"پاتیل\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-14T00:59:24.948Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/057e68e9bb3bcd09.txt
---
=== BQT
8301:داله دائه شود آنگاه در پاتیلی کنند و عسل در
```


## [2026-09-14T00:59:27.312Z] TOOL CALL #60: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n \"معین\\|دهخدا\\|patil\\|پاتیل\" 057e68e9bb3bcd09.txt | head -30"
}
```


### [2026-09-14T00:59:27.352Z] TOOL RESULT

```
4:TITLE: پاتیل - معنی در دیکشنری آبادیس
6:پاتیل - معنی در دیکشنری آبادیس 
10: پاتیل
13: مترادف پاتیل : دیگ، سیاه مست
18: لغت نامه دهخدا
20: پاتیل. ( اِ ) ظرف بزرگ مسین و جز آن که دهانه ٔآن فراختر از شکم است و در آن چغندر و آشهای بزرگ وفرنی و امثال آن پزند. پاتیله. تیان. طنجیر. لوید. و رجوع به پاتیله و پاتله شود. || ( در حمام ) ظرف بزرگ مسین با دهانه فراخ که زیر خزانه گذارند و از بن آن آتش کنند تا آب خزانه گرم شود. تیان.
21:- پاتیل شدن ؛ در تداول عوام ، خفتن و بی خبری بعلت مستی و سکر. 
25: دیگ مسی دهان فراخ که ته آن گرداست، پاتیله هم گویند
29: فرهنگ معین
37:* پاتیل شدن: (مصدر لازم ) ‹پاتیلی شدن› [عامیانه، مجاز] مستِ مست شدن و از پا درآمدن. 
45: پاتیل یک ظرف بزرگ فلزی ( قابلمه ) برای پختن غذا یا جوشاندن آب روی یک آتش باز است، این ظرف دهانی باز و اغلب دسته ای قوسی شکل دارد. 
46:پاتیل ها در دنیای پیشرفته به عنوان وسیله آشپزی به شدت از مد افتاده اند. یک استفادهٔ متداول در فرهنگ غربی، استفاده از پاتیل به عنوان وسیلهٔ جادوگر است، کلیشه ای که بوسیلهٔ ادبیات داستانی مختلف مانند نمایشنامه مکبث نوشته شکسپیر محبوب شده است. در ادبیات معمولاً جادوگران معجون هایشان را در پاتیل آماده می کنند. در فولکلور ایرلندی، یک پاتیل مکان نگهداری گنج لپرکان ها را لو می دهد. 
47:در برخی از اشکال ویکا، با ترکیب جنبه های اسطوره شناسی سلتی، پاتیل با الهه کریدوِن مرتبط است. اسطوره شناسی ولز هم، از پاتیل هایی صحبت می کند که برای جنگجویان ارتش مفید بودند. 
48:در شاخه دوم مَبی نوگیون در داستان برانون، دختر لیر، دِ پِیر دادنی ( پاتیل تولد دوباره ) پاتیلی جادویی است که می توان جنگجویان مرده را در آن قرار داد تا زنده شوند، فقط آنها قدرت سخن گفتن نخواهند داشت. [ ۱] گمان می رود که این جنگجویان فاقد روح هستند، آن ها می توانند دوباره به میدان نبرد برگردند تا زمانیکه دوباره کشته شوند. در ویکا و برخی از اشکال دیگر سیستم های اعتقادی نئوپاگان یا پاگان پاتیل هنوز در کارهای جادویی مورد استفاده قرار می گیرد. 
49:اغلب پاتیل از چدن ساخته می شود و برای سوزاندن بخور بر روی یک صفحه زغال چوب، برای ساخت نمک سیاه ( مورد استفاده در مراسم تبعید ) ، برای مخلوط کردن گیاهان، یا برای سوزاندن عریضه ها ( کاغذی با کلمات قدرت یا خواسته های نوشته شده در آنها ) استفاده می شود. پاتیل ها نه تنها نماد الهه، بلکه نماد رحم نیز هستند ( چون چیزی را توی خود نگه می دارند ) و بر روی یک محراب نشان دهندهٔ زمین است، چون ابزار کاربردی است. پاتیل ها اغلب در مغازه های عصر جدید یا «متافیزیکال» فروخته می شوند و ممکن است نمادهای قدرت های مختلفی باشند که بر روی آنها نوشته شده است. 
50:جام مقدس ماهیت بریتن گاهی اوقات پاتیل نامیده می شود، گرچه به طور سنتی جام در مورد فنجان دسته دار بیشتر از ظرف بزرگی که کلمهٔ پاتیل برای بیان آن به کار می رود استفاده می شود. ممکن است این از ترکیبی از جام افسانه ای با اسطوره های پیشین سلتیک از پاتیل های جادویی حاصل شده باشد. 
51: wiki: پاتیل 
53: پاتیل (ریخته گری). پاتیل[ ۱] ظرفی است با پوشش نسوز که فلز گداخته از کوره در آن ریخته و به وسیلهٔ آن به قالب ها منتقل می شود. 
54:در ریخته گری پس از آنکه قالب ها کاملاً مستحکم شد و درجه حرارت پیش گرم هم به اندازه لازم رسید نوبت به مرحله بارریزی است. تخلیهٔ مذاب از کوره یا پاتیل در قالب را بارریزی یا مذاب ریزی می نامند. مرسوم ترین روش بارریزی ریختن ثقلی مذاب توسط پاتیل است. گاه نیروی ثقل برای پرکردن قالب کافی نیست و علاوه بر آن از نیروی گریز از مرکز هم استفاده می شود. 
55: wiki: پاتیل (ریخته گری) 
66: دیگ، پاتیل، کوره، تنور، تون حمام و غیره، بوته آزمایش
68: دیگ، پاتیل، کتری بزرگ
70: دیگ، پاتیل، کتری بزرگ
78: پاتیل
79:حدود سال ۱۳۱۵ شرکت نفت انگلیس وایران در شرق دهلران برای ذخیره اب شیرین تانکری نصب می کنند و مردم چون تانکر اب ندیده بودند خیال می کرده اند که پاتیلی است به همین دلیل نام ان منطقه را پاتیل گذاشته اند.
83:2. پات همان پاتیل خودمان است، دیگ، که بیشتر یادآور دیگ بزرگی است که در صنایع ذوب، مواد مذاب درون آن قرار دارد. 
101:• فرهنگ فارسی، محمد معین، انتشارات امیر کبیر، تهران، ۱۳۷۵
105: پاتیل =دیگ دهانه گشاد وبزرگی که مسی ویا رویی است وبرای پختن غذا برای افرد بیشتر استفاده می کنند .
111: پاتیل:دیگِ گشاده دهان مسی، پاتیله
112:نمونه:پاتیلی پرکندوبرای غرشمال ها بیاورد. ( کلیدر، ج۶, ص۱۷۶۹ ) محمدجعفر نقوی
```


## [2026-09-14T00:59:30.302Z] TOOL CALL #61: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && sed -n '29,40p' 057e68e9bb3bcd09.txt"
}
```


### [2026-09-14T00:59:30.339Z] TOOL RESULT

```
 فرهنگ معین

 [ سنس . ] (اِ. ) دیگ بزرگ مسی ، دیگ خزانة حمام .
 (ص . ) (عا. ) سیاه مست . 

 فرهنگ عمید

 دیگ دهان فراخ معمولاً از جنس مس.
* پاتیل شدن: (مصدر لازم ) ‹پاتیلی شدن› [عامیانه، مجاز] مستِ مست شدن و از پا درآمدن. 

 فرهنگستان زبان و ادب
```


## [2026-09-14T00:59:37.863Z] TOOL CALL #62: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.sanskritdictionary.com/?iencoding=iast&q=p%C4%81tila&lang=sans&action=Search\" --note \"page 404, root Po 2: Sanskrit pātila lookup\" 2>&1|tail -2"
}
```


### [2026-09-14T00:59:39.309Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/f34f5ab56bfc4a49.txt
```


## [2026-09-14T00:59:41.632Z] TOOL CALL #63: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"pātila\\|patila\\|पातिल\" f34f5ab56bfc4a49.txt | head -20; echo \"--- size\"; wc -c f34f5ab56bfc4a49.txt"
}
```


### [2026-09-14T00:59:41.700Z] TOOL RESULT

```
--- size
183 f34f5ab56bfc4a49.txt
```


## [2026-09-14T00:59:43.695Z] TOOL CALL #64: ToolSearch

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 2
}
```


### [2026-09-14T00:59:43.703Z] TOOL RESULT

```


```


## [2026-09-14T00:59:46.594Z] TOOL CALL #65: WebFetch

```json
{
 "url": "https://www.sanskritdictionary.com/p%C4%81tila/155644/1",
 "prompt": "Does the Sanskrit word pātila exist? What does it mean? Also give pātra and pātrī meanings."
}
```


## [2026-09-14T00:59:47.016Z] TOOL CALL #66: WebSearch

```json
{
 "query": "Sanskrit \"pātila\" Monier-Williams meaning vessel"
}
```


### [2026-09-14T00:59:47.990Z] TOOL RESULT

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```


### [2026-09-14T00:59:52.632Z] TOOL RESULT

```
Web search results for query: "Sanskrit "pātila" Monier-Williams meaning vessel"

Links: [{"title":"Monier-Williams Sanskrit-English Dictionary --स","url":"https://sanskrit.inria.fr/MW/295.html"},{"title":"Patra, Pātra: 53 definitions","url":"https://www.wisdomlib.org/definition/patra"},{"title":"Monier Monier-Williams","url":"https://en.wikipedia.org/wiki/Monier_Monier-Williams"},{"title":"Monier Williams Sanskrit-English Dictionary (online)","url":"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc/indexcaller.php"},{"title":"Monier-Williams: A Sanskrit-English Dictionary (1872)","url":"https://gretil.sub.uni-goettingen.de/gretil/6_sres/2_dict/mwse72_u.htm"},{"title":"Monier-Williams Sanskrit Dictionary 1899 Advanced","url":"https://www.sanskrit-lexicon.uni-koeln.de/scans/MWScan/2020/web/webtc2/index.php"},{"title":"Monier Williams - Sanskrit-English Dictionary 1872 | PDF","url":"https://www.scribd.com/document/321388649/Monier-Williams-Sanskrit-English-Dictionary-1872"},{"title":"Monier-Williams Sanskrit English Dictionary Page 0498","url":"http://www.ibiblio.org/sripedia/ebooks/mw/0400/mw__0498.html"},{"title":"A Sanskrit English Dictionary : Monier-williams, Monier, Sir : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/in.ernet.dli.2015.31959"},{"title":"Vimana","url":"https://en.wikipedia.org/wiki/Vimana"}]

The search results don't contain specific information about the Sanskrit word "pātila" in the Monier-Williams dictionary. However, the results do show related information about Sanskrit vessel terms. For example, Pātra (पात्र) is defined as "A vessel in general" in the Monier-Williams Sanskrit-English Dictionary.

To find the specific definition of "pātila" in Monier-Williams, you would need to access the complete Monier-Williams Sanskrit-English Dictionary directly through one of these online resources: the Sanskrit-Lexicon website (sanskrit-lexicon.uni-koeln.de) or the INRIA Sanskrit Dictionary portal (sanskrit.inria.fr), which provide digitized versions of the complete dictionary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T00:59:56.377Z] TOOL CALL #67: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.wisdomlib.org/definition/patila\" --note \"page 404, root Po 2: Sanskrit pātila lookup (wisdomlib)\" 2>&1|tail -2"
}
```


### [2026-09-14T00:59:58.302Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/0e1193229a1c4b6b.txt
```


## [2026-09-14T01:00:00.497Z] TOOL CALL #68: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/web && grep -n -i \"patila\" 0e1193229a1c4b6b.txt | head -30; wc -c 0e1193229a1c4b6b.txt"
}
```


### [2026-09-14T01:00:00.548Z] TOOL RESULT

```
1:URL: https://www.wisdomlib.org/definition/patila
4:TITLE: Patila, Pāṭīla: 5 definitions
6:Patila, Pāṭīla: 5 definitions 
138: Patila, Pāṭīla: 5 definitions
151: Patila means something in Marathi, Hindi, biology. If you want to know the exact meaning, history, etymology or English translation of this term then check out the descriptions on this page. Add your comment or reference to a book if you want to contribute to this summary article. 
161:Patila in Biology glossary 
167: 1) Patila in India is the name of a plant defined with Acalypha hispida in various botanical sources. This page contains potential references in Ayurveda, modern medicine, and other folk traditions or local practices It has the synonym Ricinocarpus hispidus (Burm. f.) Kuntze (among others).
168: 2) Patila is also identified with Aristolochia bracteata .
169: 3) Patila is also identified with Cissampelos pareira It has the synonym Cocculus villosus Wall., nom. illeg. (etc.).
177: If you are looking for specific details regarding Patila, for example chemical composition, pregnancy safety, side effects, diet and recipes, health benefits, extract dosage, have a look at these references.
180: Discover the meaning of patila in the context of Biology from relevant books on Exotic India 
190:Patila in Marathi glossary 
200: Discover the meaning of patila in the context of Marathi from relevant books on Exotic India 
209:Patila in Hindi glossary 
218: Discover the meaning of patila in the context of Hindi from relevant books on Exotic India 
227:Patila in Kannada glossary 
236: Discover the meaning of patila in the context of Kannada from relevant books on Exotic India 
240: Starts with ( +21 ): Patilabbhamana , Patilabbhanti , Patilabbhati , Patilabha , Patilabha Sutta , Patilabha-chanda , Patilabhabhavana , Patilabhabhumi , Patilabhagata , Patilabhahetu , Patilabhahi , Patilabhaka , Patilabhakala , Patilabhakarana , Patilabhakaranattha , Patilabhakattha , Patilabhakhetta , Patilabhakkama , Patilabhakkhana , Patilabhamanasa .
241: Full-text ( +32 ): Patili , Patilaki , Ganasavashina , Mukaddama , Tilavida , Paraganapatila , Patelaki , Patelapatavari , Patela , Gamvapahani , Tilasankranta , Manaca , Polista , Pateli , Mukadama , Patilapatavari , Dasarabakara , Kacivahivata , Beshami , Gamvasavashina .
245: Search found 11 books and stories containing Patila, Pāṭīla, Patīlā; (plurals include: Patilas, Pāṭīlas, Patīlās). You can also click to the full overview containing English textual excerpts. Below are direct links for the most relevant articles:
7683 0e1193229a1c4b6b.txt
```


## [2026-09-14T01:00:15.169Z] TOOL CALL #69: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== HJB patila\"; grep -n -i \"patila\\|pateela\\|patili\" HJB.txt | head -10; echo \"=== ARY\"; grep -n \"پاتیل\\|پاتیله\" incoming/ARY/ARY_pages.txt incoming/ARY/ARY_latin_index_pages.txt | head; echo \"=== LKT batiaca\"; grep -n -i \"batiak\\|batiac\" LKT.txt KLN_1966.txt | head"
}
```


### [2026-09-14T01:00:15.250Z] TOOL RESULT

```
=== HJB patila
10627:GBE7  PABTBIDGE.  The  com- mon Anglo-Indian  name  of  the  Hind. tltar,  common  over  a  great  part  of  India, Ortygomis  Ponticeriana,  Gmelin.  "Its call  is  a  peculiar  loud  shrill  cry,  and has,  not  unaptly,  been  compared  to  the word  Pateeta-pateela-vateela,  quickly repeated  but  preceded  oy  a  single  note, uttered  two  or  three  times,  each  time with  a  higher  intonation,  till  it  gets, as  it  were,  the  key-note  of  its  calE" — Jerdon,  ii.  566.
=== ARY
=== LKT batiaca
```


## [2026-09-14T01:00:18.603Z] TOOL CALL #70: WebSearch

```json
{
 "query": "ریشه‌شناسی واژه «پاتیل» حسن‌دوست فرهنگ ریشه‌شناختی"
}
```


## [2026-09-14T01:00:19.363Z] TOOL CALL #71: WebSearch

```json
{
 "query": "Hindi \"patila\" पतीला cauldron etymology Sanskrit pātra Persian patil"
}
```


### [2026-09-14T01:00:25.096Z] TOOL RESULT

```
Web search results for query: "ریشه‌شناسی واژه «پاتیل» حسن‌دوست فرهنگ ریشه‌شناختی"

Links: [{"title":"فرهنگ ریشه‌شناختی فارسی، محمد حسن‌دوست، 1393 تهران، فرهنگستان زبان و ادب فارسی، دورۀ پنج جلدی","url":"https://lsi-linguistics.ihcs.ac.ir/article_1976.html"},{"title":"ایبنا - حسن‌دوست: نوشتن «فرهنگ ریشه‌شناختی زبان فارسی» 16 سال زمان برد","url":"http://www.ibna.ir/fa/doc/shortint/232985/%D8%AD%D8%B3%D9%86-%D8%AF%D9%88%D8%B3%D8%AA-%D9%86%D9%88%D8%B4%D8%AA%D9%86-%D9%81%D8%B1%D9%87%D9%86%DA%AF-%D8%B1%DB%8C%D8%B4%D9%87-%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C-%D8%B2%D8%A8%D8%A7%D9%86-%D9%81%D8%A7%D8%B1%D8%B3%DB%8C-16-%D8%B3%D8%A7%D9%84-%D8%B2%D9%85%D8%A7%D9%86-%D8%A8%D8%B1%D8%AF"},{"title":"(PDF) نقد فرهنگ ریشه‌شناختی زبان فارسی [نوشتۀ دکتر محمد حسن‌دوست Review of \"An Etymological Dictionary of the Persian Language,\" by M. Hassandoust] | Ahmad Reza Qaemmaqami - Academia.edu","url":"https://www.academia.edu/24471058/%D9%86%D9%82%D8%AF_%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87_%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C_%D9%86%D9%88%D8%B4%D8%AA%DB%80_%D8%AF%DA%A9%D8%AA%D8%B1_%D9%85%D8%AD%D9%85%D8%AF_%D8%AD%D8%B3%D9%86_%D8%AF%D9%88%D8%B3%D8%AA_Review_of_An_Etymological_Dictionary_of_the_Persian_Language_by_M._Hassandoust_"},{"title":"فرهنگ ریشه‌شناختی زبان فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%AE%D8%AA%DB%8C_%D8%B2%D8%A8%D8%A7%D9%86_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"فرهنگ ریشه‌شناسی فارسی - ویکی‌پدیا، دانشنامهٔ آزاد","url":"https://fa.wikipedia.org/wiki/%D9%81%D8%B1%D9%87%D9%86%DA%AF_%D8%B1%DB%8C%D8%B4%D9%87%E2%80%8C%D8%B4%D9%86%D8%A7%D8%B3%DB%8C_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C"},{"title":"پاتیل - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/"},{"title":"پاتیل به انگلیسی - معنی در دیکشنری آبادیس","url":"https://abadis.ir/fatoen/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/"}]

Based on the search results, I found information about the etymological entry for the word "پاتیل" (pātīl) in Hasandoust's etymological dictionary.

According to Hasandoust's Etymological Dictionary of Persian Language (فرهنگ ریشه شناختی زبان فارسی), the word "پاتیل" (pātīl) refers to a pot or vessel generally, and specifically a wide-mouthed pot used for cooking sweets. The word appears to derive from Hindi origins; compare with Sanskrit: pātili, which means a trap (for catching deer) or a small clay vessel (for begging).

Hasandoust's Etymological Dictionary of Persian Language is a specialized dictionary for Persian etymology authored by Mohammad Hasandoust and published in 2014 in five volumes by the Academy of Persian Language and Literature.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


### [2026-09-14T01:00:26.541Z] TOOL RESULT

```
Web search results for query: "Hindi "patila" पतीला cauldron etymology Sanskrit pātra Persian patil"

Links: [{"title":"Patra, Pātra: 53 definitions","url":"https://www.wisdomlib.org/definition/patra"},{"title":"Patila, Pāṭīla: 5 definitions","url":"https://www.wisdomlib.org/definition/patila"},{"title":"पात्र - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%BE%E0%A4%A4%E0%A5%8D%E0%A4%B0"},{"title":"Patil - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/Patil"},{"title":"Patili, Pāṭilī, Pātilī, Pātili: 9 definitions","url":"https://www.wisdomlib.org/definition/patili"},{"title":"Pati (title)","url":"https://en.wikipedia.org/wiki/Pati_(title)"},{"title":"Patra","url":"https://en.wikipedia.org/wiki/Patra"},{"title":"Patala, Pāṭalā, Paṭala, Pātāla, Pāṭala, Pātala, Pata-ala: 61 definitions","url":"https://www.wisdomlib.org/definition/patala"},{"title":"Patil (title)","url":"https://en.wikipedia.org/wiki/Patil_(title)"},{"title":"पतला - Wiktionary, the free dictionary","url":"https://en.wiktionary.org/wiki/%E0%A4%AA%E0%A4%A4%E0%A4%B2%E0%A4%BE"}]

Based on the search results, I found relevant information about the etymology of "patila" (पतीला). Here's what I discovered:

In Hindi, Patīlā (पतीला) refers to a huge cooking brass-kettle. 

Regarding the Sanskrit connection, the search results indicate that Hindi borrowed the word पात्र (pātra) from Sanskrit, though the results show this refers to a vessel or container more broadly. The search did find the Hindi form "पतीला (patīlā)" listed alongside the Sanskrit-derived "पात्र (pātra)", suggesting a linguistic relationship.

However, the search results did not contain specific information about:
- A direct Persian etymology for "patila"
- The specific Sanskrit term "pātra" in relation to cauldrons
- How the Persian element might have influenced the word

The search results show that Patil (as a surname) derives from Sanskrit पट्टकिल (paṭṭakila), but this refers to an administrative title meaning "village head," not a cooking vessel. To provide more complete etymological information about the Persian connection you mentioned, I would need to search for additional sources specifically addressing Persian influence on Hindi cookware terminology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```


## [2026-09-14T01:00:32.792Z] TOOL CALL #72: Bash

```json
{
 "command": "python3 tools/fetch_source.py \"https://www.wisdomlib.org/definition/patili\" --note \"page 404, root Po 2: Sanskrit pātilī / pātili lookup for Persian پاتیل\" 2>&1|tail -1; cd /home/sfmqrb/git/rishe/data/verification/sources/web && python3 - <<'EOF'\nimport glob,os\nf=sorted(glob.glob('*.txt'),key=os.path.getmtime)[-1]\nt=open(f,encoding='utf-8').read()\nprint(f)\ni=t.find('definitions')\nprint(t[i:i+3500])\nEOF"
}
```


### [2026-09-14T01:00:34.833Z] TOOL RESULT

```
/home/sfmqrb/git/rishe/data/verification/sources/web/90d4964fb411c577.txt
90d4964fb411c577.txt
definitions

Patili, Pāṭilī, Pātilī, Pātili: 9 definitions 

 -->

 -->

 -->

 Home 

 About 

 Contact 

 Newsletter 

 Shop 

 Links 

 Photos 

 TOOLS 

 Support me on Patreon 

 Resources 

 Resources 

 Buddhism 

 Hinduism 

 Jainism 

 India History 

 Shaivism 

 Shaktism 

 Vaishnavism 

 Pancaratra 

 Vedic Hinduism 

 Ganapatya 
 -->

 Theravada 

 Mahayana 

 Tibetan Buddhism 

 Arts 

 Arthashastra 

 Ayurveda 

 Chandas 
 -->
 Dhanurveda 
 -->
 Dharmashastra 

 Gandhashastra 
 -->
 Itihasa 
 -->
 Jyotisha 

 Katha 
 -->
 Kavya 

 Linguistics 

 Mimamsa 
 -->
 Natyashastra 

 Nitishastra 
 -->
 Nyaya 
 -->
 Philosophy 

 Purana 

 Rasa-shastra 

 Samkhya 
 -->
 Shiksha 
 -->
 Shilpa-shastra 

 Vaisheshika 
 -->
 Vastu-shastra 

 Vedanta 
 -->
 Vyakarana 
 -->
 Yoga 

 Ganita 

 Sanskrit 

 Pali 

 Marathi 

 Kosha 
 -->

 Science 

 Various traditions 

 All glossaries 

 Subhashita 

 -->

 Patili, Pāṭilī, Pātilī, Pātili: 9 definitions

 Glossary 

 Sanskrit 

 Pātilī 

 [Declension, feminine] 
 Quicksearch 
 Literal search 

 Introduction 
 Languages Marathi 
 Sanskrit 
 Hindi 
 Tamil 

 See also 

 -->

 Introduction:
 Patili means something in Hinduism , Sanskrit, Marathi, Hindi, Tamil. If you want to know the exact meaning, history, etymology or English translation of this term then check out the descriptions on this page. Add your comment or reference to a book if you want to contribute to this summary article. 

 Languages of India and abroad
 Marathi-English dictionary

[ «previous 
 (P) 

 next» ]
— 

Patili in Marathi glossary 

Marathi > 

 -->

 pāṭilī (पाटिली).—f The salary or allowance of pāṭīla . 2 The office of pāṭīla .
 Source : DDSA: The Molesworth Marathi and English Dictionary context information Marathi is an Indo-European language having over 70 million native speakers people in (predominantly) Maharashtra India. Marathi, like many other Indo-Aryan languages, evolved from early forms of Prakrit, which itself is a subset of Sanskrit, one of the most ancient languages of the world.

 Discover the meaning of patili in the context of Marathi from relevant books on Exotic India 
 Sanskrit dictionary

[ «previous 
 (P) 

 next» ]
— 

Patili in Sanskrit glossary 

Sanskrit > 

 -->

 Pātilī (पातिली).—
 1) A snare, trap.
 2) A small earthen vessel (Mar. pāteleṃ ).
 3) A woman of a particular class.
 Source : DDSA: The practical Sanskrit-English dictionary Pātilī (पातिली).—f. ( -lī ) 1. A trap or snare for catching deer. 2. A small earthen vessel or pot, especially used by religious mendicants. 3. A woman of a particular class. E. pāta falling, ilac aff. fem. aff. ṅīp .
 Source : Cologne Digital Sanskrit Dictionaries: Shabda-Sagara Sanskrit-English Dictionary 1) Pātilī (पातिली):— f. (only [cf. Lexicographers, esp. such as amarasiṃha, halāyudha, hemacandra, etc.]; [from] √ pat ?), a trap or snare for catching deer
 2) a small earthen pot (used by mendicants)
 3) a woman of a [particular] class.
 Source : Cologne Digital Sanskrit Dictionaries: Monier-Williams Sanskrit-English Dictionary Pātilī (पातिली):— (lī) 3. f. A trap or snare for catching deer; a small earthen pot used by religious mendicants; woman of a particular class.
 Source : Cologne Digital Sanskrit Dictionaries: Yates Sanskrit-English Dictionary Pātilī (पातिली):— f. 
 1) Schlinge. —
 2) eine Art Thongefäss. —
 3) eine Art Weib [ Hemacandra’s Anekārthasaṃgraha 3, 665.] [ Medinīkoṣa l. 110.]
 Source : Cologne Digital Sanskrit Dictionaries: Böhtlingk a
```


## [2026-09-14T01:00:54.306Z] TOOL CALL #73: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"vispo.pitay\\|vlspo.pitay\\|pitay-\\|piiay\" BRT.txt | head -10"
}
```


### [2026-09-14T01:00:54.356Z] TOOL RESULT

```
24506:•  g.  inspö.pitay-  Adj.  (auch  fem.)  'all- tränkend': -apaica  va  .  .  ag»nyh  (sd.)  .  . 'pailliiXPf.y^  V.3S.S.
27010:spitay-
27041:•  j.  apitay-  EN,  eines  Gläubigen**:  'tsii uspasnaos  aiaonS  "des  Sp.,  Sohns  des Us'p.  .."  Yty.i2i.
```


## [2026-09-14T01:01:08.048Z] TOOL CALL #74: Bash

```json
{
 "command": "python3 -c \"\nfrom PIL import Image\nim=Image.open('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404hi.png')\nW,H=im.size\nc=im.crop((int(0.225*W),int(0.535*H),int(0.40*W),int(0.585*H)))\nc=c.resize((c.width*2,c.height*2),Image.LANCZOS)\nc.save('/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-greek.png')\n\""
}
```


### [2026-09-14T01:01:09.467Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:01:12.067Z] TOOL CALL #75: Read

```json
{
 "file_path": "/tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/c404-greek.png"
}
```


### [2026-09-14T01:01:12.090Z] TOOL RESULT

```

```


## [2026-09-14T01:01:36.846Z] TOOL CALL #76: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"peis-1\\|peis-\\b\" POK_full.txt | head -10"
}
```


### [2026-09-14T01:01:36.886Z] TOOL RESULT

```
65176:Root / lemma: peis-2, speis- 
70786:e. reup- ^ausre'\Q>en, tear, break, rupture'; roupa-^ho\e, aperture ', rupeis-xocV! .
```


## [2026-09-14T01:01:39.103Z] TOOL CALL #77: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '65130,65200p' POK_full.txt"
}
```


### [2026-09-14T01:01:39.169Z] TOOL RESULT

```
*eska\xoxx\ * eiska or *eidska) by chance? s. also above S. 794. 

Note: 

From PIE the cognate for fish passed to Altaic languages: 

Protoform: *pusa ( ~ -Jo-) 

Meaning: a k. of fish 

Mongolian protoform: *basir]ga 

Tungus protoform: *puse- 

Japanese protoform: *pansai 

References: WP. II 11, WH. II 310, Max Forster Themse 840 f. 

Page(s): 796 

Root / lemma: {peis-'H) : pis- 

Meaning: to grind 

Material: Old Indie pinasti^ grinds, crushes ' (3. PI. pisanti= Latin pinsunt), pista- ' ground 

', n. 'meal, flour', pestar-^ Zerreiber ' (: Latin pistoi), Avestan pisant-^ crushing '; gr. 

TTTiaau) ' stamp, grind coarsely ' (probably expressives qq), nriapa, nTiaavr) ' shelled 

barley ', nrioK;, nTia[j6(; ' stamping ', nspiniapaTa ' squeezed bunches of grapes ' (diss. 



from *TT£pnTTia|jaTa); Latin pTnso, -ere, pinsid, pi(n)sd, -are^ crush, grind ' {pTs-mVc\ nasal 
reduction from pins-), *pTstum, pTnsum, pinsitum; pistor^ baker ', p/sd "mortar", pTla6s., 
pTIum " mortar club ' (and 'spear, lance'), pistillum " Stampfer '; Umbrian pistu ' pistum '; 
Middle Low German iz/se/" mortar'. Middle High German /^se/' penis'; Lithuanian Iterat. 
paisyti^ (Gerste) abklopfen, den Gerstenkornern die Grannen abschlagen ', primarily yO/s//" 
coire cum femina '; Old Church Slavic pbsgau6 pbchajg, pbchat/^bump, poke', *pbseno 
"meal, flour', russ. psenou. " shelled millet ', Czech Iterat. yOec/701/5//" stomp'. 
Maybe alb. bishti^ tail ' a Baltic loanword. 

References: WP. 111, WH. II 267, 307 f., Trautmann 220 f., Schwyzer Gr. Gr. 1 , 692. 
Page(s): 796 

Root / lemma: peis-2, speis- 

Meaning: to blow 

Material: With s-/ Latin spTro, -are'b\o\N, breathe, breathe' {*speis-), spTritus, -Js "breath, 

breeze, breath, soul, ghost'; spiraculum^ air hole '; 

without 5-.'0ld \v\6\c picchora^ whistle, flute'; Middle High German vTsen, vfsten^ einen 
Wind streichen lassen ', K7s/"breaking wind, fart'. Old English ffsting6s., ndd. ffster^ podex 
', Dutch veest{*faist) "breaking wind, fart'. Old Icelandic ffsa^ fart ', Norwegian ffsa^s. and 
"blow'. Modern High German fispern, fispe/n'h\ss'; Balto-Slavic *pTsketi^ cheeps, whistles ' 
in Lithuanian pysketi^ bang ', Slavic *piscg, *piscati\x\ russ. piscu, piscatb " cheep, 
screech, shriek, scream, squawk, cackle, croak, yell ', Church Slavic pistalbi. " whistle ', 
Old Church Slavic p/sAa// "whistle' etc.; 

maybe alb. piskaV\o srceam', piscame^ scream' Slavic loanwords. 

with /^formants: cymr. ffun {*spoi-na) "breath'. 

References: WP. 1111, WH. II 575 f., Trautmann 221 . 
Page(s): 796 

Root / lemma: pej(9)-, pi-
```


## [2026-09-14T01:01:54.934Z] TOOL CALL #78: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"=== WLD Bd2 p.71-72 (po(i)) find\"; python3 -c \"\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nimport re\nfor i,p in enumerate(d):\n    if 'trinken' in p and ('pd(i)' in p or 'po(i)' in p or 'pöi' in p or 'bibo' in p):\n        print('leaf',i); print(p[:2500]); break\n\""
}
```


### [2026-09-14T01:01:56.099Z] TOOL RESULT

```
=== WLD Bd2 p.71-72 (po(i)) find
leaf 75
                                                   pin    — pD(i)                                   71


pin „Hokstuck“.
   Ai. pinaka-m „Stab, Stock, Keule“; gv. mvai, -axo? „Sparre, Balken,
Brett, Schreibtafel, Gremalde“; abg. ptnh m. „Bauinstamin, -strunk". Fick
1* 83, 48^; Perssons Beitr. 410 a 3 weitere Ankniipfung an spei „spitz,
spitzes Holzstiick^ ist unwabrscheinlich.


pilo- „TIaar% es-St. *piles-
    Lat. p^liis „Haar“,               wovon wohl als Kollektiv „*Haarknauer' auch pila
„Ball, Ballen'^        (s. Yf.       LEWb.^ s. v.); ob dazu, im ^1. und der Bed. durch
Tiregov     beeinfluBt,          auch      gr. nxlXov „Peder, Plaumfeder“? (s. u. pet- „auf
etwas lossturzen^)              ;
                                     auf einem -es-St. beruht *pil-s-6s „verfilzt“, in gr.
TtiXog „Filz‘‘ {7iiXi(D             .jfilze, presse Z8.“), lat. pilleus, -etmi „Filzkappe, Filz-

mutze“       (so,    nicht pileus,auch nach dem Romanischen, s. Meyer-Liibke
KZ. 33, 308 f.),        abg. phsh „Filz“. J. Schmidt KZ. 32, 387 f., s. auch Yf.
LEWb.2 s. V.; dt. Filz s. u. pel- „sto6en'^

po(i):pT und (von po aus) po „trinken“. Langdiphthongische Wz. nach
    Schulze KZ. 27, 420 f. Praes. *pi-po-mi (oder wohl *pi-l)omi), pi-po’
    me, themat. *pi-h6, wobei h nach Thumeysen lA. 22, 65, Hdb. 138 wohl
    der im Inlaut erhaltene urspriingliche Wz. kons. ist, der im Anlaut
    durch friihidg. Anlautwandel zu p verhartet wurde; vgl. auch Brug-
       mann IP 3, 37.
   Themat, Praes. ai. pibati „trinkt“, lat. bibo, -ere, air. ib- ds. (z. B. 3. sg. ni ib
„er trinkt nicht“, ibid 2. pi. Imp, „trinketl“), acymr. iben „bibimus“, corn.
evaf „bibo“, bret. emjf. Unthemat. ai. pi-p-ate 3. pL, pi-p-Clna-, pi-pana-
Ptc., apiplta (: nuit-oxco, falisk. pipafo „ich werde trinken“ (wohl mit -d-,
wie lat. dd-bo, trotz GL 5, 317; vgl. auch pf. med. gr. 7tmoTai)\ si.pd-ti
,,trinkt“,pay-dyati „gibt zu trinken, trankt“, pdyaie „trankt“ (: abg. pojq,
air.        ai,     „getrunken, getrunken habend"' (abl. gr. jrdrog „Trank“,
lat. pdtus „getrunken habend“, vgl. auch potus „Trank“, lit. puta „Zechge-

lage“, pUi-h „Trunk‘‘ (= abg. piti Inf. „trinken“; abl. gr. nooig „Trunk, das
Trinken‘‘,  und ajujicong „Ebbe“, lat. poti-o das Trinken“); ai. patave inf.
„zu trinken^ (= apr. poutivei ) patar-, pdtdr- „der TrinkeF‘ = lat. potor ds.
                                              ;


abl. gr. oivojtor^Q „Weintrinker“, itoxriq, 7toxr\qiov „TrinkgefaB, BecheP',
woraus o. TioxeQefji „poculum“)
```


## [2026-09-14T01:02:02.183Z] TOOL CALL #79: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\np=d[75]\nprint(p[2500:5200])\n\""
}
```


### [2026-09-14T01:02:03.406Z] TOOL RESULT

```
, paira- n. „TrinkgefaB“ (= lat. pochim, po-
ctilum „Becher“)     -payia-, -payya- „zu tranken, Trunk“ (= apr. poTds m.
                            ;


„das Trinken“); pcina- n. „Trunk‘^ (vielleicht dazu mir. dn „TrinkgefaB‘^
—   Alb. pi „trinke'‘ (usw., s. G. Meyer BB. 8, 189, Wb. 336).     Arm. timp               —
„Trunk“, 9mbem, ompem „trinke“ wohl hieher, aber formell unklar (Lit. bei
Brgm. IP 3, 37).                — Gr.   tzTvco,   aol. tkovco „trinke“     (fut. Jtiopat   alter Konj.,
ETtiov, Tii&i,      aol. Ttcb&i, ^ejtcoxa, TZETzopat), Ticbpa, Tzojua n, „Trank“ usw. (s. o.),
Tiimoy.oy „gebe zu trinken^^, mvov „Gerstentrank“.     Lat. bibo usw. (s. o.),
posca „Mischtrank“ (: esea),                 —
                                Air. ib-, an s. o. air. dul (zweisilbig), mir.-
                                                                      ;



nir.   ol    dat.    Inf.       „trinken‘*   (ob zu abg. pojitil          s.   Pedersen KG. II 414,
674;      nicht iiberzeugender               bei    Stokes KZ. 41, 388;      on-fais „diving“, en
jjWasseF').         — lAt^plHa           s. o.:    apr.         puton, poiitm, potdivei „trinken^‘
(usw., 8. Bezzenberger KZ. 41, 120 a 2, Trautmann Apr. 412 und oh^n pauis).
— Abg.       pljq, piti ,,trinken^‘, plvo „Trank‘‘ (lit. pyvas, apr. piwis, peivo „Bier“
```


## [2026-09-14T01:02:07.799Z] TOOL CALL #80: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('incoming/WLD/WLD_Bd2_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\np=d[75]+d[76]\nimport re\nfor m in re.finditer('pitay|vispo|av\\\\.', p):\n    print(p[max(0,m.start()-150):m.start()+200].replace(chr(10),' '))\n    print('---')\n\" | head -30"
}
```


### [2026-09-14T01:02:09.062Z] TOOL RESULT

```
<string>:5: SyntaxWarning: invalid escape sequence '\.'
                                        po(i):(p9i?:)       — pa- aus poln. piivo ds.), fojq, pojiti „trankeii'' (ac. panost „Trunkenheit“ ist kein Slav. Rest der Stufe         Prusik KZ. 35, 600, sondern aus ^pbj-anosih ent- standen.            Osten-Sacken IF. 32, 314).    Curtias 280, Fick I* 84, 482,      46, Yf. LEWb.^ 88 f. Brugmann II ^ 3, 3
---
  s.    Schulze KZ. 27, 426) „Yieh weiden,         hiiten^; daraus allgemeineres „schutzen,                       auch durch Bedeck en“.    Ai. pati, av. pCiiti „hutet, bewacht, schiitzt^^, ai. go-pd- m. „Hirt“, av. r ana-pci „Beinschutz, -schiene^*, ai. pagii- „hutend“ (vgl. nmv), paid- m. „Wachter, BQrt“ {paldyati „bewacht, hutet‘‘), -pcivan „sch
---
raus allgemeineres „schutzen,                       auch durch Bedeck en“.    Ai. pati, av. pCiiti „hutet, bewacht, schiitzt^^, ai. go-pd- m. „Hirt“, av. r ana-pci „Beinschutz, -schiene^*, ai. pagii- „hutend“ (vgl. nmv), paid- m. „Wachter, BQrt“ {paldyati „bewacht, hutet‘‘), -pcivan „schutzend“, ap. xmO^a-pavan „LandYOgt, Satrap‘‘; ai. nr-pi-ti-li 
---
```


## [2026-09-14T01:02:15.040Z] TOOL CALL #81: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== SYN drink\"; grep -n \"5\\.13 *DRINK\\|DRINK (vb\" SYN.txt | head -5; echo \"== SYN flour\"; grep -n \"FLOUR\" SYN.txt | head -5; echo \"== IEC pōi\"; grep -n \"pōi\\|pō-, pī\\|pi-bō\\|pōtos\" IEC.txt | head -10; echo \"== IEC peis\"; grep -n \"pisō\\|pinsō\\|pistos\" IEC.txt | head -10"
}
```


### [2026-09-14T01:02:15.150Z] TOOL RESULT

```
== SYN drink
8422:5.13 DRINK (vb.)
== SYN flour
9177:5.55 MEAL, FLOUR
== IEC pōi
== IEC peis
12596:peil- "a tool, file, scraper, knife'(?) OHG fila, f., MHG vile, sf., OE feol, f. (fle and com. Gmc.); OCS pila, f. ‘saw’; Cz. pila, id. beside pilnik, m. ‘file’; Srb. pila ‘saw, file’; Li. peilis, gs. 20. m. ‘knife’; Latv. peilis, id.; cf. Li. pielà ‘saw’. (Lat. pila ‘pestle’ is prob. fr. *pisla or *pisdhla, see pis-, pistos, etc.)
12933:pisimnos, à ‘ground, pounded, small. Cf. pisio, pistos, etc. Skt. Av. pi&-, v. root ‘grind’; Gk. cf. ptisáne, f. (“pearl barley, barley-gruel, fr. *d-pision-); LLat. pisinnus, adj. ‘tiny’; G Fesen, Vesen, m. ‘spelt; grain-husk'; R pšenò, n. ‘millet; Slo- vene ‘groats’; OPr. cf. som-pisinis (‘coarse bread": Skt. sam-piš-); Skt. cf. pista-pesanah, m. ‘flour, meal
12934:pisið (pins-) ‘crush, pound’. WP II, 1. Cf. pisimnos, pistos Skt. pinsami, pp: pistah, v. id.; Av. piš-, id.; Gk. (cpd.) ptísso, id. (fr. *d-pisio); Lat. piso, ére & pinso, ére, sup. pinsum, but adj: pistus, v. id.; Li. pisü, pisti, v. ‘coire’
12938:pislom, à ‘pestle, crusher’. Cf. pisio, pistos, pisimnos Lat. pilum, n. ‘pestle’; cf. pila, f. ‘mortar’;
12941:pistos «crushed, pounded; powder, bruise’. Cf. pisið, etc. Skt. piştáh, id.; pistám, n. ‘flour; Av. cf. pistrō, m. ‘crush, bruise’; Oss. fästä, Iron. fäxt, s. ‘mortar for crushing’; Gk. cf. psísis, f. (for *d-pis-, f. crushing); Lat. pistus, adj. “pound- ed R pest, m. ‘pestle’; cf. Cz. pist, gs: -u, m. ‘pestle; crushing-mill'; Li. cf. piesta, f. id. beside Latv. piesta, f. ‘mortar for crushing. (Cz. & Balt. (?) *peist-)
12942:pistrio ‘knead, pound’. Cf. pisio, pistos, etc. Av. cf. pistro, m. ‘crush, bruise’; Arm. trem, v. ‘knead’; LLat. pistrio, Ire, v. id. (also in Fr. pétrir, id.). (Isophone: G fiestern, v. *fling")
12949:pistos — plag-
```


## [2026-09-14T01:02:22.406Z] TOOL CALL #82: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"‘drink’\\|'drink'\" IEC.txt | grep -n -i \"pō\\|poti\\|pot-\\|pib\" | head -10; echo \"=== try\"; grep -n \"^pōtos\\|pōtos\\|pōti\\|pibō\\|pī-\" IEC.txt | head -15"
}
```


### [2026-09-14T01:02:22.486Z] TOOL RESULT

```
7:12856:pibō ‘drink’. WP II, 71 S kt. píbami, pibe, id.; Lat. (assimilated conss.) bibo, ére, pf: bibi, id.; Falisc. pafo or pipafo; fut. ‘shali drink’; Of ibim, MIr. ibhim ‘drink, quaff; W yfaf *will drink'; Br. éva, Cor. eva, inf. ‘drink’; Icel. cf. fipa, v. tr. (*confuse', lit. “make drunk?)
=== try
12856:pibō ‘drink’. WP II, 71 S kt. píbami, pibe, id.; Lat. (assimilated conss.) bibo, ére, pf: bibi, id.; Falisc. pafo or pipafo; fut. ‘shali drink’; Of ibim, MIr. ibhim ‘drink, quaff; W yfaf *will drink'; Br. éva, Cor. eva, inf. ‘drink’; Icel. cf. fipa, v. tr. (*confuse', lit. “make drunk?)
```


## [2026-09-14T01:02:26.613Z] TOOL CALL #83: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '8422,8470p' SYN.txt | cut -c1-400; echo \"=== FLOUR\"; sed -n '9177,9215p' SYN.txt | cut -c1-400"
}
```


### [2026-09-14T01:02:26.750Z] TOOL RESULT

```
5.13 DRINK (vb.)
Lith.  gerli Lett. dzert Chsl.  piti SCr. pitt Boh. pili se) a 170d Russ. pit’ Skt. pa- Av. 2’ar-
‘move, glide’). Cf. also Toch. A tsuk- ‘drink’ : Lat. dicere ‘draw, lead’, etc. Walde-P. 1.874. Feist 125. G.S. Lane, Language 14.27.
3. Lith. gertz, Lett. dzert : ChSl. zrétz, Skt. gr-, Lat. vorare, Grk. BiBpooxw, LE *gver- ‘swallow, devour’. Walde-P.. 1.682 ff.
4, Av. x’ar- ‘consume, eat, drink’, x’asar- ‘a drinker’, see 5.11.
The words for the sb. ‘drink’ are near- ly all obvious derivs. of the roots appear- ing in the verbs, as Grk. wGpa, roots, Lat. potid, potus, NHG getrank, etc. Those of different orig. are as follows:
Ir. deog, Nir. deoch, W. diod, MW diawt, OCorn. diot, MBr. diet, orig. ob- scure. Walde-P. 1.786. Stokes 146.
Ir. lind (NIz. lionn ‘ale’), W. llyn, prob. the same word as Ir. lind (s-stem), W. llyn ‘lake, pond’ (1.48). Pedersen 1.37. Persson, Beitriige 878. But sepa- rated by Walde-P. 2.438.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
332 SELECTED INDO-EUROPEAN SYNONYMS 5.14 HUNGER (sb.) Grk. ids, xetva Goth. hithrus, grédus Lith. alkis, badas NG weiva ON hungr Lett. izalkums, bads Lat. famés Dan. hunger ChSl. glad It. fame Sw. hunger SCr. glad Fr. faim OE hungor Boh. hlad Sp. hambre ME hunger Pol. gléd Rum. /foame NE hunger Russ. golod Ir. gorle Du. honger Skt. kgudh-, ksudha- Nir. ocras, goria OHG hungar Ay. $ud- W. newyn 
Words for ‘hunger’ come by speciali- zation from either ‘want, distress, wast- ing away’ or ‘desire, longing’. Cf. the specialization of NE starve from OF steorfan ‘die’.
1. Grk. Atpds : Aowwds ‘plague’, Ard- fouat ‘withdraw, shrink’, Goth. aflinnan ‘depart’, ON linna ‘cease’, etc., IE *lez-. Walde-P. 2.388. Whatever the ultimate relations of the various IE roots *lei-, the immediate Greek development is fr. ‘waste away’ to ‘hunger’.
Grk. weiva, Ion. zelvy, fr. *réa: Grk. revia ‘poverty’, xévns ‘poor’, mévouat ‘toil, be poor’, xévos ‘toil’, outside con- nections dub. Walde-P. 2.8 f., 661.
2. Lat. famés (> Romance words) etym. dub. Walde-P. 1.829. Ernout- M. 328f. Walde-H. 1.451.
3. Ir. nina, NIr. naoine ‘famine’, W. newyn, Br. naon ‘hunger, famine’, OCorn. naun (gl. famis), prob: Goth. naups, OHG not, OE néad ‘necessity, distress’ (NE need). Walde-P. 2.316. Pedersen 1.61. Stokes 193.
Ir. gorte, NIr. gorta : Ir. goirt ‘bitter, painful’, fr. the root of gorim ‘heat’, ChSI. goréti ‘burn’, etc. (1.85). Walde- P. 1.688. Pedersen 1.33.
NIr. ocras, cpd. of od- and root of
caraim ‘love’. Pedersen 1.476.
4. Goth. hithrus, ON hungr, OE hun- gor, etc. general Gme.: Grk. xévxg: mew (Phot.), xeyxer” emidaxver (Hesych.), Lith. kenkia ‘it hurts’, kanka ‘pain’, ON ha ‘vex, distress’. Walde-P. 1.401. Falk- Torp 432. Feist 273.
Goth. grédus (once =. \iu6s) with adj. grédags : ON gradr ‘hunger, greed’, OF gr@dig ‘hungry, greedy’ (NE greedy, whence greed), fr. *ghrédh-, prob. an ex- tension of *gher-, in Goth. gairnjan, OE giernan ‘desire’ (NE yearn), Osc.- Umbr. her- ‘wish’, etc. Walde-P. 1.601. Feist 220. Walde-H. 1.658. Otherwise Falk-Torp 339.
5. Lith. alkis, Lett. izalkums : Lith. alkti, Lett. alkt, ChSl. alkati ‘be hungry’, outside connections dub. Walde-P. 1.159.
Lith. badas, Lett. bads, prob. : Skt. badh- ‘press, urge’, badha- ‘distress’. But cf. Mithl.-Endz. 1.248.
6. ChSI. glad, etc., general Slavic: ChSl. zlidéti ‘long for, desire’, also(?) Skt. grdh- ‘be eager, long for’, gardha- ‘desire’. Walde-P. 1.633. Berneker 320.
7. Skt. ksudh-, ksudha-, Av. sud-, NPers. gud : Skt. ksudh- ‘be hungry’; outside connections?
‘Hunger’ fr. ‘desire’.
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
;00D AND DRINK; COOKING AND UTENSILS 333 5.15 THIRST (sb.) Goth. aurstei Lith. troSkulys, tro’kimas
siya, 51005 ON _porsti Lett. slapes Gtk. ite Dan. ¢¢rst ChSl. Zezda NG wits ee torst SCr. Zed Lat. ae OE purst, byrst Boh,  Zizert It. soif ME thurst, thirst Pol. —pragnienie Boe a NE _ thirst Russ. Zazda a i yee Du durst Skt. irsna-, pity fart OHG  durst Av. tar$na- Nir. tart, iola MHG durst W. ile NHG durst
sec Bi come, through the W. syched, Br. sec’hed fr. W. sych,
parched’, or, like
longing’ (as & from ‘thirst for’). 1, Derivs. of IE *ters- in Grk. répco-
ua ‘become dry’, Lat. torrere ‘make dry’, Goth. paursjan ‘be thirsty’, OHG derran ‘make dry’, Skt. trs- ‘be thirsty, etc. Walde-P. 1.737f. Ernout-M. 1048. Pedersen 1.81.
Ir. fart; Goth. Jaurstez, OE purst, etc. general Gme.; Lith. troskulys, troskimas (trokstt ‘be thirsty’, trogskus ‘thirsty’); Skt. irsnd-, Av. targna-.
2. Grk. diva, Styos, with vb. dude, etym.? Boisacq 192.
3. Lat. sitis (> Romance words) prob.: Grk. g0tovs ‘wasting away, decay’, Skt. keiti- ‘disappearance, destruction’. Walde-P. 1.506. REW 7961,
Pa Lah, Wace 1g ase ‘65, Walde-P. 1.197, 2.8.
Ir. secc ‘dry’, loanwords fr. Lat. siccus ‘dry’ (: sttis? see 15.84), Loth, Mots lat. 209.
5. Goth. paurstei, etc., above, 1.
6. Lett. slapes : slapt ‘be thirsty, be- come weak’, Lith. slopti ‘become weak or choke with thirst’ prob. fr. a parallel form of the root (*slap- in ON slafast ‘slacken’): Lith. slabnas, ChSl. slabi ‘weak’, etc. (Walde-P. 2.432, but with- out inclusion of Lett. sldpes, etc.). Miuhl.-Endz. 3.924.
7. ChSl. Zezda (vb. zezdati), SCr. zed, Boh. Zizen, Russ. zazda : Lith. pasigesti ‘long for’, godas ‘greed’, Grk. bécoacat ‘pray for’, 780s ‘longing’, etc. IE *g’hedh-. Walde-P. 1.673.
Pol. pragnienie, fr. pragnaé ‘be thirsty’ : Boh. prahnouti ‘be parched’ (as with thirst), Pol. prazyé, etc. ‘roast’ (5.18). Briickner 434.
8. Skt. irsnd-, Av. tarsna-, above, 1.
5.16 SUCK (vb.)
Grk, » 7 NG ee (a0a:), BUS dew Goth. (daddjan) Lith. Zisti, ciulpli Lat. shee ee @ (it.) ON saga Lett.  zist, dét (sitkt) Hs Weciare ms Dan.  suge, die ChSl. _ siisati 8UuCEr, Léler oere Sw. — suga, dia SCr. _ sisati ie upar ma OE stican, stigan Boh. _ ssalt ee Rigam co ME _ suke Pol. —_ssaé : 7,  sugi : NE suck Russ. sosat Nb, a Du. zuigen Skt.  dha- (ciis-) | 8tgno, OHG _ stigan (taen =
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
334
Most of the verbs for ‘suck’ belong to one of two considerable groups of cog- nates. Some are derived from the nouns for a woman’s ‘breast’ or ‘teat’, and some are of imitative origin reflect- ing the sound of sucking.
=== FLOUR
5.55 MEAL, FLOUR
Grk.  &Aevpov Goth.
Lith. miltaz
NG dete ON mjol Lett.  miltz Lat. farina Dan. mel ChSl. maka It, farina Sw. mjél SCr. _ braSno ee farine OE melu Boh. mouka Tun lg ME mele, flour Pol. maka i i ind NE meal, flour Russ. muka Nir si Du. meel Skt. pista- Vv. mn OHG melo Av. iStra- * — blawd MHG mel e Br Bleud NHG mehl
Words for ‘meal’ are mostly from
a a ‘grind’ (5.56) or ‘crush’, one Pitom the name of a cereal,
Tk ag Mh ‘grind’ (6.56),
edn Br, bleud, OCorn. blot : oN mjol, OF melu, etc.,
ay ith, miltai, Lett. miltz 2, “an; Hitt. memal. ‘ring, Sug NG aebpr, fr. aréw ‘ : aleur ‘meal’, atauri
mill’, fr, (fers Igy,’ "aM ‘rind? (5.56), Walde-P.
3. Lat. farina (> Romance words), SCr. brasno (ChSI. brasino ‘food’, 5.12) : Lat. far ‘spelt, grain’, Goth. barizeins ‘made of barley’, OE bere ‘barley’, etc. Walde-P. 2.134. Ernout-M. 330. Walde-H. 1.455.
4. Ir. men, NIr. min: Lith. minti ‘tread, break flax, prepare skins’, ChSI. meti, ‘compress’, etc. Walde-P. 2.263.
5. ME, NE flour, the same word as flower, came to be used of the flower or finest part of the meal, then especially though not exclusively for the fine meal
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
Digitized by Arya Samaj Foundation Chennai and eGangotri
362 SELECTED INDO-EUROPEAN SYNONYMS
of wheat, leaving meal for the coarser | Lith. méinkyti ‘knead’, ete,
products. NED s.v. 6. ChSI. maka, Boh. mouka, Pol.
maka, Russ. muka : ChSl. mekiiki ‘soft’, | Lat. pinsere ‘crush’, etc. (5.56),
5.56 GRIND Grk. ddA Goth. malan Lith. malt NG aGw ON mala Lett. malt Lat. molere Dan. male ChSl.  mléti It. macinare Sw. mala SCr. — mlijeti Fr. moudre OE grindan Boh. = mliti Sp. moler ME _sgrinde Pol. mleé Rum. mdcina NE grind Russ. molot’ Ir. melim Du. —malen Skt. (pis-) Nir. meilimn OHG malan Av. bom ee W. malu MHG maln, malen Br. mala NHG  mahlen
The earliest process of converting grain into meal was ‘crushing’ by pound- ing, whence later the ‘grinding’ between two stones. For the earlier process there is a distinctive group of cognates, namely Grk. rriccw (also ‘winnow’), Lat. pinsere, Skt. pis- (Walde-P. 2.1. Er- nout-M. 770). But such was also the more original force of IE *mel-, which furnishes most of the European words fo
1. TE *mel-. Walde-P. 2.284 ff. Er- nout-M. 626 f.
Lat. molere (> Fr. moudre, Sp. mo- ler); Ir. melim, NIr. metlim, W. malu, Br, mala; Goth. malan, ON mala, etc.,
CC-0. In Public Domain. Gurukul Kangri Collection, Haridwar
5, Walde-P. 2.268. Briickner 327 ise
7. Skt. pista-, Av. pistra- : Skt. pis.
general Gme. except in English; Lith, malti, Lett. malt; ChSl. mlétz, etc., gen- eral Slavic; Hitt. 3 sg. mallai, 3 pl. mal- lanzi (Sturtevant, Hitt. Gram, 243 ey),
2. Grk. adéw, late édybw, NG &dWu : Arm. atam ‘grind’, atauri ‘mill’, aleur, ‘meal’, Skt. anu- ‘fine, thin’. Walde-P. 1.89. Boisacq 43.
3. It. macinare, Rum. mdcina, fr. VLat. *machindre a new denom. of Lat. machina ‘machine’, with specialization to ‘grind’. REW 5206.
4. OE grindan, ME grinde, NE grind : Du. grind, grint ‘gravel, coarse meal’, Lat. frendere ‘crush, bruise, gnash the teeth’, Lith. grendu, gresti ‘rub, scrape’, ete. Walde-P. 1.656 ff. Walde-H. 1.545.
5. Skt. pis- ‘crush’, representing the earlier process, whence pista- ‘meal’, see above.
yooD 5.57
Digitized by Arya Samaj Foundation Chennai and eGangotri
AND DRINK; COOKING AND UTENSILS 363
MILL
(Words in parentheses ‘Handmill’)
Goth. -gairnus
Lith. malunas (girnos)
gdm, BEADS ON kvern, mylna Lett.  sudmalas (dzirnavas) ork. ate Dan.  meflle (kvern) ChSI. Zritniivi, zritny NG role, molina Sw. kvarn SCr. mlin (rvanj) Jae ulino OE cweorn, mylen Boh.  mlyn (Zerna) Ite noulin ME mylne, mille (quern) Pol. mlyn (zarna) i. molino 7) NE mill (quern) Russ. mel’/nica oe moar (rignild Du. molen ’ Skt. (pesana-) i brad, ae OHG  muli(n) (quirn) Av. (sudus-) Nir en) ME
```


## [2026-09-14T01:02:34.100Z] TOOL CALL #84: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"قاووت\\|سویق\\|تلخان\" BQT_v1_pages.txt | head -10"
}
```


### [2026-09-14T01:02:34.163Z] TOOL RESULT

```
25682:و آن دا بعربی سویق خوانند چه سویق الشعیر
```


## [2026-09-14T01:02:37.322Z] TOOL CALL #85: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '25660,25700p' BQT_v1_pages.txt; echo \"=== page tag\"; awk 'NR<=25682 && /\\[pdf page/{p=$0} END{}' BQT_v1_pages.txt; grep -n \"\\[pdf page\" BQT_v1_pages.txt | awk -F: '$1<25682' | tail -2"
}
```


### [2026-09-14T01:02:38.428Z] TOOL RESULT

```
بت و سا
ستد و داد مکن هر کر جز دستادست
س شاه را فرخ اسفند یار ۰
ی ره و بو
که بسادست خلاف‌آرد وصحست برد.
ابوشکور بلخی. < لت نامه * .سا نیدن- بروزن «سانیدن, آب دادن
باغ وزراعت را کویند ۱ .
بی‌او کند . با واوه بروزن و همتی
ساو ند ۲ ‌ِ پروزن دما تد, قاف؛شمررا
گومند همحو دچار ونگار و بهار ۰
پساو هدن - بر وزن رسانیدن » بمعنی
دست مالیدن و لامه کردن باشد ۴ - و بمعنی
بست* ت‌ بقتح اول‌وسکون انیو فوفانی»
معروف‌است که نقیض بلند باشد- وژمین همواررا
نیز کوبند - و بمعنی خراب هم هست که در
مقابل آباداست- و کنابه ازمردم خسیس وبخیل
و دون همت باشد ترد محقفن آنکه نتواند
ومع -
ببال همت پرواز عروج بمدارح کمالات حفانی
یامرتبه‌ای از مراتب دیگی کند - و بکسر اول
هر آردی را گویتد عموما و آردی که کندم
وجو و نخود آن‌را بربان کرده باشاد خصوصاً ٩‏
و آن دا بعربی سویق خوانند چه سویق الشعیر
آرد جو بربان کرده و سوبق الحنطه آرد گندم
بربان کرده را گویند - و مر کبی باشد که بعضی
ازچله نشینان وفقیرآن و جو کیان هندوستان از
جکر آهو و مغز بادام و امثال آن سازند که
حرگاء مقدار پته‌ای از آن بخورند ناچند روز
محتاح مطعام شوند . #
ستا۲ س بفتح اول وسکون ثانیوفوقانی
بالف کشیده. برسرکاری رفت نکه قبل‌ازین شروع
حرآن شده ناش ۹
تر کاری وباغی پسان هموار و ناهموارهٌ .
مولوی بلخی‌رومی.* لقت نامه».
عمه باوه همه خام وهمه سست
معانی از چکاوه نا بساوند . لمیبی -
ومخنف آن پسوند بمعنی مزید موخر » بعنی جزوی که باخرکلمه ملحق شود وتفییری در ععنی
ان دهد» اطلاق شود. «لفت نامه» .
مر گوهر خردرا نپساود
۴ - ظاهراً مصمحف « می کردن » است . «لفت نامه» .
1511 (در تحت اهر کسی قرارگیرنده) ؛ در وخی ۳254, شهنی 0156 *اسشق ۳۱۹ ورگ :
=== page tag
```


## [2026-09-14T01:02:49.124Z] TOOL CALL #86: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && awk 'NR<=25760 && /\\[pdf page/{n=NR\": \"$0} END{print n}' BQT_v1_pages.txt; echo \"---- following lines\"; sed -n '25700,25730p' BQT_v1_pages.txt"
}
```


### [2026-09-14T01:02:50.214Z] TOOL RESULT

```
---- following lines
1511 (در تحت اهر کسی قرارگیرنده) ؛ در وخی ۳254, شهنی 0156 *اسشق ۳۱۹ ورگ :
تب رکف ۱۹۹ ( ذیل : 6۳۵5020 ) ۰ کلکی ۳85 , رني ۳25 , نطنزی 0251 « .۱ ص
۲ سنگری ا۳85 , شهسرزادی ۳25 « . اس ۰۱۹۳ . ۱ - هرن این کلمه را
56 آورده» ازاوستابی 01511162 ؛ هندی باسثان ۳658 ( سابیدن ». خردکردن ؛ له کردن) .
وخی 054 , شغنی ۳۸50 . سربکلی ۳96 (گندم برشته, آرد ساییده) «اسشق ۳۲۰». طبری
8 , مازندرانی کنونی ۳۱۷۵ . پهلوی 665۸ « کارنامهة اددشیر در ۱۴ * «واژه نامه ۱۸۵ * :
۰ پیامبر ) ابشانرا بغانٌ سلمان فرود آورد وقوت ابشان قراخ کرد از یست جو وخرعا« نرجمة
بلممی». «لفت نامد» . ۲ - بهلوی 02508 بمعنی آغاز و انجام ( هزوارشی‌آن04152۳.
۳ « بونکر ۱۲۲ *.
۵ پست - بنم اول مأخون ارفرانه ۳۵/56ازلانینی ۳0562 . اداره‌ای که حمل و نقل
نامه‌ها وامانت‌ها رابمهده دارد. معرب‌آن «بوسطة» درعربی جدید «نفی» .
۳ سح ساوبدن:
ندهیج عدبری: نه‌سلطانی. ناصرخرو بلخی. «لفت نامه*.
ه۵ فی : هندی باستانحمشوق است.
بی جانشین ۳ ۳
شخصی ات که چون صاحب دکان برخیزد او
یجای صاحب د کان بنشیند وکالا بقروشد
ی خم زدن - کنابه از کریختن
باشث .
ی دست گردن ۰ کنابه از پنبان
کردن وذخیره‌نهادن باشد .#8
پستادست - با دال ابجد بروزن
هرجا هست + بمعنی نسیه پاشد و آن خربدن
اسباب واچناسی است که بعد از چند روز قیمت
مدهند ۱ # .
پستان مادد بر بدن « کنابه از
حرعی رشره وبی‌همنی- وحق‌ناشناسی وبی‌حشفتی
ویی هقی سنارتن بنشد. 9
سته‌شکر فشان- کنایه‌از لب ودهان
9 رد : مساوست .
پستای - بکس اول , اوستا 15100202 (یستان) .
```


## [2026-09-14T01:03:03.373Z] TOOL CALL #87: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"pdf page\" BQT_v1_pages.txt | head -3; echo \"---\"; head -5 BQT_v1_pages.txt"
}
```


### [2026-09-14T01:03:03.447Z] TOOL RESULT

```
---
۱ ۵ ۱! ۱
7 موم ۳ لام
م ۱ 0 و طق صفرررنیاعدریرماروی
۰ ۱ "۳
۳
```


## [2026-09-14T01:03:06.542Z] TOOL CALL #88: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read()\npages=d.split(chr(12))\nprint('pages:',len(pages))\n# find which page contains سویق الشعیر\nfor i,p in enumerate(pages):\n    if 'سویق الشعیر' in p:\n        print('formfeed page index',i)\n        break\n\""
}
```


### [2026-09-14T01:03:07.733Z] TOOL RESULT

```
pages: 777
formfeed page index 628
```


## [2026-09-14T01:03:12.535Z] TOOL CALL #89: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources && python3 -c \"\nimport json; d=json.load(open('refs_online.json'))['BQT']\nprint(json.dumps(d,ensure_ascii=False,indent=1))\n\""
}
```


### [2026-09-14T01:03:13.648Z] TOOL RESULT

```
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


## [2026-09-14T01:03:18.643Z] TOOL CALL #90: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && python3 -c \"\nd=open('BQT_v1_pages.txt',encoding='utf-8',errors='replace').read().split(chr(12))\nfor i,p in enumerate(d):\n    if 'پاتیل' in p or 'باتیل' in p:\n        print('leaf',i)\n        import re\n        j=p.find('پاتیل')\n        if j<0: j=p.find('باتیل')\n        print(p[max(0,j-600):j+900])\n        print('=====')\n\" | head -60"
}
```


### [2026-09-14T01:03:19.671Z] TOOL RESULT

```
leaf 260
ه - پممنی آقتاب سر
دبولر است که کنابه ازانتهای عمر وزوال‌زند کالی
۲ قتاب‌سو ار کنانه از می دم سح رخیز
باشد . *
آ فتاب گر دش کنابه ازتمام روی
زمین - وهرچیز کهآآفتاب برآن بتابد - وحربارا
نیز کوبند و آن جانورست مانند چلپاسه .
۲ فتاب گر دك « بفتح کاف فارسی .
جانورست شبیه بجلیاسه که بسریانی « حرزون »
خواننه - و گل آفتاب پرست را نیز گوبند ٩‏ .
هو سس
فتاب گیر « بکرکاف‌فارسی‌وسکون
جافقت تب
0
] فر فان ۴ - با نون و کاف فارسی
بروزن کافرستان » نام نسکی است با
و يك نك کتاب زند (۲) بعنی فسمتی است
بیست و يك قسم کناب مذ کور .
آفر وده با واو مجهول و زای هوز
نوی را گود .
ی و تقو ۳
ی مس ۱
داله دائه شود آنگاه در پاتیلی کنند و عسل در
آن ریزند وبر سرآتش نهند تا نيك بپزد وسخت
(۱) چش : خربوزه . (۲) چك : ژند .
۱ _ ره : آقتاب‌پرست و آقا ب گردان . ۴ - مشنفآفریشگان ۱ عکرشته ز نمازهای زرتششان
موسوم به «آفربنگان» است که درطی سال» درجشنها ومواقع مختلف بجای آورده ميشود. چهارتای
آنها که مهمترین آفرینکان بشمار میروند » در عتن اوستای کلدنر 261006) باين ترتیب ضبط
شده است: آفریشگان دهمان (مقدسان) ء آفرشکان کانها . آفررنگا نکهنبار , آفررنگان‌رپیتوین
(برای شرح نها رلك : خرده‌اوستا تألیف آقای پورداود) آفرینگان مرکب است از آفرین بمعنی
دعا و نيایش . و همچنین بممنی دعای نيك وستایش است در برابر نفرین ( رل : آفرین ) دهارله
در فرهنگ خود ( ص ۱۲۹ ک نا ۳ افربگان 2171820 نماز دی بارسان » جمم اف يك
مربوط یکمهةٌ زند ( اوستائی ) 81610 بمعنی نماز تقدیس است . » لیب یکوید :
از اطاعت باپدر زردشت بر خود بنك آفرینگا نکنته است
ايشکه فرهتکه توبسان آنرا مکی از یت و يك نسك اوستا دانسته اند صحیح نست
« مزدسنا ۱۳۹-۱۳۶ ۰.۰ ۴ - پهلوی ۸0۷۴6509
=====
```


## [2026-09-14T01:03:25.541Z] TOOL CALL #91: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs/incoming/ARY && grep -n \"پست\" ARY_pages.txt | head -20; echo \"=== latin index PIS\"; grep -n -i \"PIS\\b\\|PES\\b\\|PO(I)\\|POI-\" ARY_latin_index_pages.txt | head -20"
}
```


### [2026-09-14T01:03:25.617Z] TOOL RESULT

```
90:نژادهای «پست‌تر» بیشتر شد. بهمین دلیل در سرزمین‌های دور از آلمان درصد مردم چشم آبی و
95:پست‌تر از آریایی‌های ناب (یعنی آلمانی‌ها و اسکاندیناوی‌ها) بودند؛ تا چه رسد به ایرانی‌ها و
134:پست شدن نژادی و تیرگی نسبی رگ مو و چشم آنها شد. موضوع پرتری‌های نژادی (که امروزه
391:محسوب می‌شدند) به وجود آمدند. به همین دلیل این زبانها «پست» هستند و مرتباً دگرگون
424:ندارد. ولی چون هنوز پایبند داستان برج بابل بودند این عدم شباهت را ناشی از دانحراف» و «پستی»
1167:و غیره مواجه کرده است. ولی علیرغم همه‌ی پستی و بلندی‌هاء زبان‌های ایرانی امروز (فارسی»؛ کردی
2402:اسپست. اسبست(به چم "یونجه") | ۸۵
3336:۶ ۸ بر (به چم "سینه و پستان")
3847:۱ بند (به چم "ریسمان"» *طناب"»"وسلیه‌ی پستن") / ۱۳۳
4906:۸ / پستان
4930:معنی واژه‌ی ۳18 در زبان فرانسه: پستان گاو.
5568:1۸31۸7۸381712 لپستانی (5اءا۳0۵):
7953:لپستانی (بقذناه): 06 0
9851:چم این واژه در زبان‌های رومانس: پست. :
12339:چم اين واژه در سانسکریت: پستان زن
13587:چم این واژه در زبان یونانی؛ پستان,
13651:۱ این واژه‌ی کودکانه تقریاً در تمام زبان‌های هند و اروپایی وجود دارد و رابطه‌ی آن پا آمادر" و پستان "تیه"
=== latin index PIS
976:OTL AF rapes OLY abst y tr GEL] Ge ar OWIly go y alps F
1030:WSL GT hy 2 al ata a an elie SI AM al pis sete eg Sia bly (te
1164:AB SET JS ons ste 59 (Gps Sica Say esl ') 65 pis Dltatls Lg as
1237:eel PES yy jhe jie gal yo oF aa
1337:gPIS (Sjlasls y PISSEN LAT y PISS cK glao§ly colt es wo5ly-t
1394:OPES VY 9 VY (2S): abi olny UGNIS -(LITHUANIAN) gly)
1626:via Lopes Kags ODDF (WELSH) 535
1818:capes wiedt Egat
2430:pleegl glaagl b 25 go wells cal.» 4eT STABULUM 2 503!) 5 "Sant pes asta
4192:HOLD CHURCH $PAVIC) 345 539-1 PES, PEDIS LATIN) 3
4505:FATER PIT, PITH, PIS -(BALUCHI) gr sh
4800:SPENIS — :(OLD PRUSSIAN) HS 3.4 POITRINE, PIS :(FRENCH) 413
4807:(POITRINE, PIS) 108 SPENI
4814:gf ole 31) Obj 92 PIS rss me
4941:AY topes Baas HOLD ENGLISH) pS g=3Si\
4980:FINF :(OLD HIGH GERMAN) yf aT PIS H(TORHARIAN B) B gos
5147:FUUL DANISH) Slail PIS KURDISH) 52,5
5273:FYR «(OLD SCANDINAVIAN) oS 51 PIs. KURDISH) 535°
5330:TEMPORA —:(PORTUGUESE) gt TAPES GREEK) gin
5352:TeKO LITHUANIAN) «i p) TAGHT, TASHAL, Ossett) pis)"
```


## [2026-09-14T01:03:31.241Z] TOOL CALL #92: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && echo \"== PHD\"; grep -n -i \"pēst\\|pest \\|pyst\" PHD.txt PHD_mackenzie.txt | head -10; echo \"== NYB\"; grep -n -i \"pēst\\|pyst\" NYB_vol2_glossary.txt | head -10"
}
```


### [2026-09-14T01:03:31.326Z] TOOL RESULT

```
== PHD
PHD.txt:549:pazzām- [pz^m-] mature, ripen (intr.). ~išn: maturation, ripening. pazzáménidan [pz’myn-ytn'] = pazzāftan. pēčīdan, pēč- [pyc-ytn' | N ~] twist, entwine. pēm [pym] milk. péménidan, pémén- [5ymyn-ytn'] cause to well up, swell up. pen [p(y)n'] mean, miserly, niggardly. ~ih: meanness. pérámoón [pyPmwn! | M pyrmwn, N ~miin] around, péróz [pylwe | M pyrwz, N ~] victorious. ~th: victory. pérózgar [pylwekl | N ~] victorious. ~ih : victory. pés [pys | N ~] mottled, leprous; leper. pēsīdan, pēs- [pys-yin'] colour, adorn. ~iSn: adornment. pestān [pyst?n' | N ~] breast. pēš [LOYN! < A I-‘yn; руї | = M, N ~] before. IpéSag [py$k! | N péfa] trade, craft; guild, caste. *pēšaģ [pysk'] limb, member, part. pëššánig [pyš”nyk! | N pēšānī] forehead. pēšār [py | M py?r] leader, guide. ~ büdan: be guilty (of), commit. pēšārwār [руло], v. pëšyàr] urination. péSémàl [руѓут?/, v. hamēmāl] plaintiff. ~ih: prosecution, pēšēnīg [pysynyk! | (M pysyn(g), N pésina)] former; foremost, noble. pëš-gāh [pyšg”5 | N ~) audience chamber; foremost seat. pēš-kār [py$k'/ | N ~] servant. pēšēbāy [byš')wp?d | M руйору, N péfwa] leader, vanguard. ~th: leadership. pēš-pāraģ [pyšp*/k! | N —a] an appetizer. pēšyār [pyšk”/ | N ~] urine. petit [pytyt! = Av. paitita-] penance. ~ig [-yk'] penitent. ~igih: penitence. petyárag [p(y)tyd'lk! = Av. paityára- | M pty’r, N patydra] evil, mis- fortune; adversary; astr. detriment, ~th: (onslaught of) evil. рі [AB' < А "bur р(у) | M pyd] father. *pid [5(5)!! | P pyd] meat, flesh. pidar [AB Ytl, v. ipid ; ру | M pydr, N ~] father. pih [pyhw'] food, victuals. pīh [TL BA = A trb; рур | N ~] fat, tallow. pil [py] | M pyl, N ~] elephant; (chess) bishop. --bān [-p’n' | N ~] elephant-driver.
PHD.txt:551:pillagan [plk’n' | M pylg, N ~] steps, ladder. pim [pym] pain, pang, sorrow. ~gén [-kyn'] sorrowful. pir [руі | N ~] old, aged, ancient. ~ih: age. piring [pling | M pryng, (N pirind)] monochrome damask, pist [pst! | N ~] browned flour. pistag [pstk! | IN pista] pistachio nut. pišīz [pšyc | N ~] small copper coin, ‘farthing’. pēhišn [pwhsn'] corruption, decay. pēlāwad [pwPft! | М pwl'wd, N pēlād] steel. ~ën [-yn!] (made of) steel. pondik [pndk' | Ar. b/fundug] hazel-nut. por [pwl | N —] francolin. pēryētkēš [pwlyw(k)kyf = Av. paoiryē.tkaēša-| (one of) the first teachers of the Mazdean religion. ~ЛЬ : the primal doctrine of the Mazdean religion. pēst [pwst! | = M, N ~] skin, hide; bark, shell. mēn [-yn! | N ~in] (made of) skin. pēšīdan, pēš- [pws-yin' | N <] cover, put on, wear. ~išn: covering. potk [pwtk' | N ~] sledge-hammer. poxtan, paz- [APPWN-tn' < А V?ph; pwhtn', pc- | M pwxtn, N ~] cook, bake. рӧу- [pwd- | (P pwd-), N ~] run. ~iSnig : running. p6z(ag) [pwc(k!) | N pēz(a)] snout, muzzle. püdag [pwtk! | N pūda) foul, rotten. —ih: rottenness. 1puhl [pwhl | N pul] bridge. *puhl [pwhl] expiation, atonement; punishment. puhlénidan [ pwhlynytn'] cause to atone. purnāy [pwln’d] adult. purr (MALE < A mlh; pul | M pur, N ~} full. =-ģāh [-g’s] at the fullness of time, about to die. ~-тюаһ [-mh] full moon. —-rawišnih [-lwbsnyh] fullness. ~-sardag [-sltk'] of all kinds. --xwarrah [-G DE] full of glory. pursidan, purs- [pwrs-ytn' | M pwrs-ydn, N ~] ask. Vu re: Е ~iSn: question. — ~i$nig : responsible. pus [BRE < A br-h; pws | = M, N =] son. ~ar [BREI, pwsl | M pwsr, N ~] son. —yàn [pwsd?n! | M pwsy’n] womb. pušt [52001 | = M, N ~] back; support, protection.
PHD.txt:3685:skin Carm, dawāl, pēst; tēz; (a.) post- én; ~bag hambān, mašk; ~ 'table- cloth! maškīzag.
PHD_mackenzie.txt:786: abestan ['pystn' I P 'b)-'stn, N abistan] = abustan.
PHD_mackenzie.txt:4204:pesUin [pyst)n l IN....,] breast.
== NYB
541:apastäk [’pst’k] "scripture, the sacred writings of the Parsis in their original language; any quotation, or text, from the same scripture" (West, Gloss of AV, p. 13): the Avesta, the Canon to Zoro- astrianism 94?1, 107—112 passim. — West transliterates Avistak and also quotes the spelling ’pyst’k; Paz. awastā, Skr. v. avasta-väc or avista-väc. Modern Iranology has adopted Avesta as working form, and generally accepts the etymology given by F. C. Andreas: < OIr *upa-stā- 'funda- : ment, fundamental text’ (GrIrPh II, 2), cf the next w.; as to apa-: api- v.S.v. apa-.
1456:ēstišn [Pystšn', ystšn'] v. n. of ēstātan, used as pred.: has to, must stand fast, persevere 65’; subst. persistence 34?!; standstill, cessation of progress, of the stars 57. — V. also dstisn(éh).
3165:post [pwst'] skin 54%; pl. pēstihā [pwstyh?] 1079. — OP pavastä ‘clay en- velope of a tablet’, Benveniste, BSL XLVII, 1951, 42-49 (thus also Kent); MPrs pwst (A-H II), Paz. NP post.
3610:Sapistän [Spst’n'] harem 11416. 116%, — KZŠPrth 1. 28 špystn = Prs ZY #pstn, Gr. v. edvodyoG.
6295:nytpr-: nihvārišn pršhwr: Patisxtärgar špystn: Sapistän twgrn: Turan wlgšy: Valaxš
```


## [2026-09-14T01:03:37.605Z] TOOL CALL #93: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"bibo, -ere\\|bibo, bibi\\|^bibo\" LEW_1910.txt LAT.txt | head -5; echo \"== potus\"; grep -n \"poculum\\|pōculum\" LAT.txt | head -5"
}
```


### [2026-09-14T01:03:37.693Z] TOOL RESULT

```
LAT.txt:7217:bibo, -ls, bibi, (bibitum), bibere: boire. S'emploie absolument
== potus
14181:de pdtus, poculum.
45564:riture, fourrage" et, tardif, "fait de manger" (comme poculum "fait
48523:poculum: v. potus.
49568:poculum (arch. pocolom, pocolo), -i n.: de *po-tlo-m "vase a boire",
```


## [2026-09-14T01:03:40.339Z] TOOL CALL #94: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '7217,7240p' LAT.txt; echo \"=== potus\"; grep -n \"^potus\\|^poto\" LAT.txt | head -5"
}
```


### [2026-09-14T01:03:40.415Z] TOOL RESULT

```
bibo, -ls, bibi, (bibitum), bibere: boire. S'emploie absolument
ou avec complement, cf.GLK. Supp.«08,36, proprie sunt neutra quae per
se plenum sensum habent ut uiuo, spiro, sedeo, bibo. Au sena moral: boire
les paroles de; s'impregner de.- Ancien, usnel; panroman. M.L.1074.
Bibitum, bibiturus n 1 apparaissent gubre avant le III e a.ap.J.-C.
Dans la bonne langne, c'est potum, potus,poturus qui sont employds; mais
bibitum et ses derives devaient etre largement repandus dans la langue
parlee, comme le montrent les repr^sentants romans; cf.M.L.1075 bibita,
1076 bibitio, 1077 bibitor, 1078 *bibitoria, 1079 *bibitura, 1080
*bibitus.
Derivas et compos^s: bibo,-onis m.: ivrogne (nom d'un ver) et bibio,
cf.Isid.13,8,16 bibiones sunt qui in uino nascuntur, quosuulgo mu¬
stiones a musto appellant ; et Sofer p.164 et 175; M.L.i076a; bibax et
bibdculus adj .; bibosus (cr^ation de Laberius d'apres uinosus) ; bibu¬
lus-, bibilis (Cael.Aurei. ) = 7 ioxi,(J.oc.
biber,-ris m.: boisson. Nom postverbal de biber, infinitif syncop^
de bibS (cf.gr. 7 tTv), frequemment attest£ dans la langue populaire,
Titin.C0m.78, Caton Orig.131, Fann.Hist.3, et condamn^ par Caper, GLK
VII 108,10 (cf .agger)-, d'ob biberdrius . Cf.Du Cange s.u .biberis. Cf.
M.L.abbiberare, 13. Biberius: formation plaisante pour Tiberius (Suet.
Tib.43); Bibesia f.: Perediam et Bibesiam Plautus (Curc.444) finxit sua
consuetudine, cum intellegi uoluit cupiditatem edendi et bibendi, F.,
336,34»
Composes plantiniens: multibibus, merobibus (Curc.77). Verbes i pri-
=== potus
7244:potus) n'est conservae qu'aux extr6mit6s du domaine indo-europ 4 en, ob
51320:potus uel pothus codd.) | Sin autem praecepta uetant ne dicere:
```


## [2026-09-14T01:03:47.090Z] TOOL CALL #95: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Symposium\\|SYMPOSIUM\" SKT.txt | head -3; echo \"== beer\"; grep -n \"^BEER\\|BEER,\" SKT.txt | head -3; echo \"== poison\"; grep -n \"^POISON\\|POISON,\" SKT.txt | head -3"
}
```


### [2026-09-14T01:03:47.175Z] TOOL RESULT

```
19028:Symposium,  a  tnerry  feast.  (L.«»Gk.) L.  symposium.  —  Gk.  avftriatov,  a  driiiking- party,  bantjuet.  — Gk.  trvfi-  ^for  tfvr),  to- gether ;  ro-,  base  of  wI-ww'KQ,  I  drank,  w6- att,  a  drink.    See  Potable.
== beer
== poison
```


## [2026-09-14T01:03:49.778Z] TOOL CALL #96: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"Beer,  a\\|Beer, a\\|Beverage,\\|Poison,\" SKT.txt | head -5"
}
```


### [2026-09-14T01:03:49.837Z] TOOL RESULT

```
(Bash completed with no output)
```


## [2026-09-14T01:03:52.681Z] TOOL CALL #97: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n -i \"beverage\" SKT.txt | head -3; grep -n -i \"malt  liquor\\|malt liquor\" SKT.txt | head -3; grep -n -i \"Potable\" SKT.txt | head -3"
}
```


### [2026-09-14T01:03:52.773Z] TOOL RESULT

```
15130:Punch  (3),  a  beverage.  ( Hindi. -SIct.) So  calloi  from  consisting  o\  fivt  inj^redients, spirit,  water.  Icmoo-juicc.  sugar,  %pice  ;  in- trodoccd  from  Indie,  b^  vk)  ot  Ocia,-«  mcxk.
17104:iytitp.  —  Span,  xaropt,  a.  drink.  —  At skardb,  shurdb,  wine,  beverage,  syruj] Arab,  root  skariba  (above).
14631:expostulate.    <L.)      From  pp.  o-' ejr/vrfu/arr,  to  demand  cameilly. PostUTB ;  see  Position. Posy ;  see  Poem. Pot.    (C.-L.)     M.  K. GacX.poif,  W.pof,  Uret./ F.  pof,    f>ii.  pot,  Ac.     A  • cl.    Irish  pvt  auH,   I    drink, polart:  sec  Potable.     (^PA.!
14635:POTABLE.
14647:(F.  -  L.)    F.  /tf/iVw.  -   L. of  potw,   a    draoght  — L. Mnk ;  see  Potable. see  Pol. ;  Kc  FotAble. \S[>an.  -  Hayt  i )    Spaa,  patata, ^Hayti  batata,  the  same, thnut;  see  Poke  (i). (L.)     I^p6ttnl-,  stem  of  p&ttm, jura.  pArt.  of  posse,  to  be  able, am  able     Posntm  is   iboit  lot from  /p/a,   powerful,  orig.  *a id  to  Ski.  pati,  a  roaster,  lord, ;  Rum  -/vhiV  \ngtu-poiU,  lord. Ill,  'feeder.'  from  /a,  to  fctd. Allied  to  Paator.     Der.  «wri'
```


## [2026-09-14T01:04:01.984Z] TOOL CALL #98: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"سمپوزیوم\\|سمپوزیم\\|سمپوز\" MON_part1.txt MON_part2.txt incoming/ARY/ARY_pages.txt 2>/dev/null | head; echo \"== done\""
}
```


### [2026-09-14T01:04:02.064Z] TOOL RESULT

```
MON_part1.txt:79557:سمپوزیوم: ۰ 5270۲0770۳ ضیافتی که در 
== done
```


## [2026-09-14T01:04:04.216Z] TOOL CALL #99: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && sed -n '79550,79570p' MON_part1.txt"
}
```


### [2026-09-14T01:04:04.278Z] TOOL RESULT

```
تقسیم در اعضا تشکیل می‌دهد که بین این 
شبکه‌ها عقده‌های محیطی وجود دارند. 
سمپاشی: 024-7 [ع. ف.] (حامص.) 
باشیدن ض در جایی برای انهدام حشرات 
مانند مکس؛ پشه و غیره. (مج.) گفتن 
سخنانی برای تولید اختلاف در میان جمعی 
ود درادن جد کی : 
سمپوزیوم: ۰ 5270۲0770۳ ضیافتی که در 
آن س از صرف طعام به باده گساری 
می‌برداختند و مهمانان به تماشای رقص 
زسبارویان و شنیدن مسوسیقی مشغول 
می‌شدند. ضیافت؛ مهمانی. جمعیتی که 
هدفش مباحثات دوستانة فلسفی و علمی 
است. مجمعی که در آن اشخاص مختلف 
راجع به موضوعی واحد مقالاتی تهیه کنند يا 
سخنرانی‌های ایراد نمایند. 

سمت.: 82001 [ع.] (مصل.) ملازم راهی 
گردیدن. به راستی و میانه راه رفتن. (ا.) راه 
(راست)» ج. سموت. روش نیکو. قصد» 
آهنگ. صورت» هیشت. طرف» جانب:
```


## [2026-09-14T01:04:18.266Z] TOOL CALL #100: Bash

```json
{
 "command": "cd /home/sfmqrb/git/rishe/data/verification/sources/refs && grep -n \"ksun\\|SYN- \" AHD_watkins1985.txt | head -5"
}
```


### [2026-09-14T01:04:18.358Z] TOOL RESULT

```
648:English hréowan, to distress, grieve: RUE!, RUTH. 2. Ex- tended o-grade form *krous- in Greek krouein, to strike: ANACRUSIS. [Pok. 3. kreu- 622.] kreup-. Scab; to become encrusted. 1. Germanic *hrub- in: a. Middle Low German ruffelen, to crumple, akin to the Germanic source of Middle English ruffelen, to ruffle, roughen: RUFFLE}; b. Germanic compound *ga-hrub- (*ga-, intensive prefix; see kom) in Middle Dutch grof, harsh: GRuFF. 2. Suffixed o-grade form *kroup-d in Serbo-Croatian krupa, groats (perhaps > German Graupe, barley): GRAUPEL. [Pok. kreup- 623.] kreus-. To begin to freeze, form a crust. 1. Suffixed zero-grade form *krus-to- in: a. Latin crusta, crust: CROUTON, CRUST, CRUSTACEAN, CRUSTACEOUS, CRUS- TOSE; b. Greek krustallos, ice: CRYSTAL, CRYSTALLINE, CRYSTALLO-. 2. Suffixed zero-grade form *krus-es- in Greek kruos, icy cold, frost: cryo-. [Pok. 1. B. kreu- 621.] kreut-. Also kreudh-. Reed. Germanic *hreuda- in Old English hréod, reed: REED. [Pok. kreut- 623.] kropo-. Roof. Germanic *hréfam in Old English hrdf, roof: ROOF. [Pok. krdpo- 616.] krut-. Musical instrument. 1. Germanic *Arut- in Old French rote, a stringed instrument: ROTE3, 2. Geminated form *krutté in Welsh crwth, an ancient Celtic instru- ment: CROwD?. [Pok. krut- 624.] ksero-. Dry. 1. Lengthened-grade form *kséro- in Greek xéros, dry: XERO-; ELIXIR, PHYLLOXERA, XEROPHTHAL- MIA. 2. Perhaps suffixed variant form “kseres-no- in Latin serénus, serene, bright, clear: SERENE. [Pok. ksero- 625.] ksun. Preposition and preverb meaning “with.” 1. Greek sun, xun, together, with: syN-. 2. Russian so-, s-, with, in sputnik, fellow traveler (see pent-): SPUTNIK. [In Pok. 2. sem- 902.] ku-. Hypothetical base of a variety of conceivably related Germanic words meaning “a hollow space or place, enclosing object, round object, lump,” and some other derivative denotations. 1. Germanic *kubdn-, hut, shed, room, in: a. Old English cofa, bedchamber, closet: COVE!; b. Middle Dutch cubbe, “pen, stall,” fish basket, akin to the probable source of CUBBY; C. Germanic compound *kubawald-, probably “house ruler,” household god (wald-, power; see wal-), in Middle High German kobolt, an underground goblin: COBALT, KOBOLD. 2. Germanic *kutam in Old English cot, cottage: COT?, (COTTAGE). 3. Germanic *kutdn- in Old English cote, shelter: CoTE!. 4. Germanic *k(e)ud- in: a. Old English codd, bag, husk: cop?; b. Old English cudele, cuttlefish (from its ink bag): CUTTLE. 5. Germanic k(e)ut- in Old English *cieter, intestines (probably > Middle English chiterling): cx1T- TERLINGS. 6. Germanic *kukk- in Middle English cok, haycock, pile of straw: cock?. 7. Germanic *kuk- in Old English cicen, chicken: CHICKEN. 8. Germanic *kugg- in Swedish kugge, cog, akin to the possible Scandinavian source of Middle English cogge, cog: coc}. 9. Germanic *kuggila in Old English cycgel, rod, cudgel: CUDGEL. 10. Germanic *keulaz in: a. Low German kielswin, keel- son: KEELSON; b. Middle Dutch iel, ship, keel of a ship: KEEL?, 11. Germanic *kijp- in Middle Dutch kipe, cask, tub, basket: COOPER. 12. Germanic *kunt- in Middle Low German kunte, vulva, akin to the Low German source of Middle English cunte, vulva: CUNT. 13. Germanic kird- in Icelandic kiird, to crouch, lie in wait, akin to the Scandinavian source of Middle English couren, to cower: COWER. 14. Possibly Old Norse kiiga, to oppress, akin to the probable source of cow?. [In Pok. géu- 393.] kus-. A kiss. Germanic *kussaz, a kiss, with denominative *kussjan in Old English cyssan, to kiss: Kiss. [Pok. ku-, kus- 626.] kwat-. To ferment, be sour. Possible root. Suffixed vari- ant form *kwét-so- in Common Slavic *kvasi in Russian kvas, kvass: Kvass. [Pok. kuat(h)- 627.] kwe, And (enclitic). Latin -que, and: SESQUI-, UBIQUITY. [Pok. kve 635.]
812:os-. Ash tree. Germanic “aski- in Old English zsc, ash: ASH?2. [Pok. 6s- 782.] 6s-. Mouth. 1. Latin ds (stem 6r-), mouth, face, orifice, and derivative dstium (< suffixed form *6s-to-), door: ORAL, OS!, OSCULATE, OSCULUM, OSTIARY, OSTIUM, USHER; INOSCULATE, ORIFICE, ORINASAL, OROTUND, OSCITANCY, PERORAL. 2. Possibly Latin auriga, chari- oteer (< *6r-ig-, “he who manages the (horse’s) bit”; -ig-, driving, from *ag-; see ag-): AURIGA. [Pok. 1. 6us- 784.] ost-. Bone. 1. Latin os (stem oss-), bone: 082, OSSEOUS, OSSICLE, OSSUARY; OSSIFRAGE, OSSIFY. 2. Greek osteon, bone: OSTEO-; ENDOSTEUM, EXOSTOSIS, PERIOSTEM, SYN- OSTOSIS, TELEOST. 3. Suffixed form *ost-r- in: a. Greek ostrakon, shell, potsherd: OSTRACIZE, OSTRACOD; b. Greek ostreon, oyster: OYSTER; C. variant form in Greek astragalos, vertebra, ball of the ankle joint, knuck- lebone, Ionic molding: ASTRAGAL, ASTRAGALUS. [Pok. ost(h)- 783.] ous-. Also aus-. Ear. 1. Suffixed form *ous-en- in Ger- manic *auzan- in Old English éare, ear: EAR}. 2. Suffixed form *aus-i- in Latin auris, ear: AURAL!, AURICLE; AURIFORM, ORMER. 3. Latin auscultdre, to listen to (*aus- + *kli-to-, inclined; see klei-): AUSCULTATION, scouT!. 4. Suffixed basic form *ous-os- in: a. Greek ous (stem 6t-), ear: OTIC, OTO-; MYOSOTIS, PAROTID GLAND; b. Greek Jagés, hare (< */ag-ous-, “with drooping ears”; *lag-, to droop; see slég-). [Pok. dus- 785.] owi-. Sheep. 1. Germanic *awi- in Old English ewe, eowu, ewe: EWE. 2. Latin ovis, sheep: OVINE; OVIBOS. [Pok. oui-s 784.] pa-. To protect, feed. Contracted from *pas-. 1. Suffixed form *pé-trom in Germanic *fodram in: a. Old English fédor, fodder: FODDER; b. Old French feurre, fodder: FORAGE; C. Old French forreure, trimming made from animal skin, fur (< “sheath, case, lining”): FuR. 2. Suf- fixed form *pd-dhlom (doublet of *pd-trom) in Latin padbulum, food, fodder: PABULUM. 3. Extended form *pat- in: a. Germanic *féd-, food, in Old English foda, food: Froop; b. Germanic denominative *fédjan, to give food to, in Old English fédan, to feed: FEED; Cc. suffixed form *pdt-tro- in Germanic *fdstra- in Old English fostor, food, nourishment: FOSTER. 4. Extended form *pds- in: a. suffixed form *pds-sko- in Latin pdscere, to feed: PASTURE; ANTIPASTO, PESTER, REPAST; b. Latin pdstor, shepherd: PASTOR; C. suffixed form *pds-t-ni- in Latin pGnis, bread (diminutive pastillus, medicine tablet): PANADA, PANATELA, PANNIER, PANOCHA, PANTRY, PAS- TILLE, (PENUCHE); APPANAGE, COMPANION, (COMPANY). 5. Suffixed form *pd-ti- in Iranian *pdti- in Persian pdd, protecting against: BEZOAR. 6. Suffixed form *pd-won-, protector, in Old Persian khshathra-pdvd, protector of the province: SATRAP. [Pok. pd- 787, 1. pd(i)- 839.] pag-. Also pak-. To fasten. 1. Lengthened-grade form *“pak- in Germanic *fogjan, to join, fit, in Old English fégan, to fit closely: FAY}. 2. Nasalized form *pa-n-g- in: a. Germanic *fangiz, seizure, in (i) Old English fang, feng, plunder, booty: FANG (ii) Dutch vangen, to catch: VANG; b. Latin pangere, to fasten: COMPACT!, IMPINGE. 3. Root form *pak- in: a. Latin pdx, peace (< “a binding together by treaty or agreement”): PACE?, PAY!, PEACE; APPEASE, PACIFIC, PACIFY; b. Latin pacisci, to agree: PACT. 4. Suf- fixed form *pak-sio- in: a. Latin pdlus, stake (fixed in the ground): PALE!, PALISADE, PEEL’, POLE?; IMPALE, TRA- VAIL, (TRAVEL); b. probably Latin pdla, spade: PALETTE, PEEL*. 5. Lengthened-grade form *pdg- in: a. Latin pdagus, “boundary staked out on the ground,” district, village, country: PAGAN, PEASANT; b. Latin pdgina, “trellis to which a row of vines is fixed,” hence (by metaphor) column of writing, page: PAGE?, PAGEANT; c. Latin prépdgés (pré-, before, in front; see per'), layer of vine, offspring (< “a fixing before”): PROPAGATE; d. Greek pégnunai, to fasten, coagulate: PECTIN, PEGMA- TITE. [Pok. pak- 787.] pan-. Fabric. 1. Germanic *fandn- in: a. Old English
1041:IDIO-, IDIOM, IDIOT; IDIOMORPHIC, IDIOPATHY, IDIOSYN- CRASY. 11. Variant form *swei- in Irish féin, self: SINN FEIN. [Pok. se- 882.]
2281:SPRINGE spergh- SPRINKLE (8)preg- SPRIT sper-4 SPROUT sper-4 SPRY (s)preg- SPUME (S)poi-mo- SPUR spere- SPURGE peue- SPURN spere- SPURRY (s)preg- SPURT sper-4 SPUTNIK ksun, pent- SPUTTER spyeu- SPUTUM spyeu- SPY spek- SQUAD kWetwer- SQUALENE (8)kWal-o- SQUARE kWetwer- SQUASH2 kwét- SQUAT ag- SQUIRE skei- SQUIRREL ors-, skeoi- STABLE! sta- STABLE? sta- STACK steg- STACTE stag- STADDLE sta- STADHOLDER sta- STAFF! stebh- STAG stegh- STAGE sta- STAGGER steg- STAGNANT stag- STAIN teng-
2331:SWING sweng(w)- SWINGE sweng(w)- SWINGLETREE sweng(w)- SWIRL swer-2 SWITCH swei-2 SWIVEL swei-2 swoop swei-2 SWORD swer-4 SYCAMORE moro- SYCOPHANT bha-! SYLLABLE (s)lag’- SYLLEPSIS (s)lag¥- SYLLOGISM leg-1 SYMBIOSIS gWei- SYMBOL gvele-1 SYMPATHY kWent(h)- SYMPATRIC peter- SYMPHONY bha-2 SYMPHYSIS bheue- SYMPODIUM ped-! SYMPOSIUM pd@(i)- SYMPTOM pet- SYN- ksun SYNAGOGUE ag- SYNALEPHA leip-
```


## [2026-09-14T01:04:34.511Z] TOOL CALL #101: Bash

```json
{
 "command": "mkdir -p data/verification/sources/refs/ocr/BOOK && cp /tmp/claude-1000/-home-sfmqrb-git-rishe/8c8336bb-8745-4a62-a326-6760238436df/scratchpad/pg404.png data/verification/sources/refs/ocr/BOOK/404.png && ls -la data/verification/sources/refs/ocr/BOOK/404.png; sed -n '1,60p' tools/verify_check.py"
}
```


### [2026-09-14T01:04:34.618Z] TOOL RESULT

```
-rw-rw-r-- 1 sfmqrb sfmqrb 71542 Sep 13 21:04 data/verification/sources/refs/ocr/BOOK/404.png
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


## [2026-09-14T01:04:36.609Z] TOOL CALL #102: Bash

```json
{
 "command": "sed -n '60,140p' /home/sfmqrb/git/rishe/tools/verify_check.py"
}
```


### [2026-09-14T01:04:36.678Z] TOOL RESULT

```
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


## [2026-09-14T01:14:06.664Z] TOOL CALL #103: Write

```json
{
 "file_path": "/home/sfmqrb/git/rishe/data/verification/page-404.json",
 "content": "{\n  \"pdf_page\": 404,\n  \"book_page\": 374,\n  \"verified_by\": \"claude-opus-5\",\n  \"verified_on\": \"2026-09-13\",\n  \"entries\": [\n    {\n      \"entry\": 0,\n      \"root\": \"Pis, Pais\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *peys- 'to crush, grind (esp. grain)'\",\n      \"note\": \"Nourai's headword and gloss reproduce Walde-Pokorny verbatim: WLD II 1 opens with '(pais?): pis- „zerstampfen, zermalmen“ (bes. Getreide)'. Pokorny 796 restates it as '(peis-1) : pis- to grind'; Wiktionary/LIV write *peys-. The alternant 'Pais' is Walde's own hesitant full grade (built on Gk. παίω, which Pokorny later dropped from this root), so it is a legitimate quotation of the cited reference rather than an invention, but modern reconstruction knows only e-grade *peys-/zero-grade *pis-. Language label (Indo-European) and gloss ('crush, grind') are right. The Persian branch of this chart is exceptionally well supported: Horn no. 320, Hübschmann no. 320, Mo'in's footnote in Borhan-e Qate', MacKenzie's Pahlavi pist and Buck 5.55 all give the same Av. pištra- → MP pist → NP pest chain.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *peys- «کوبیدن، ساییدن (به‌ویژه غلّه)» ریشه‌ای است که پوکورنی (صفحهٔ ۷۹۶) و والده–پوکورنی (جلد ۲، صفحهٔ ۱) هر دو ثبت کرده‌اند؛ صورت دوم «Pais» همان صورت پرسشی است که والده با علامت تردید آورده و پژوهش امروزی آن را کنار گذاشته است. نام زبان و معنای ریشه درست است و شاخهٔ فارسی آن (اوستایی pištra- ← پهلوی pist ← فارسی پِست) را هرن، هوبشمان، حاشیهٔ معین بر برهان قاطع و مکنزی یکسره تأیید می‌کنند. ادعای نورایی درست است.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peys-\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"WLD2:1\",\n          \"status\": \"supports\",\n          \"note\": \"Walde-Pokorny Bd. II p. 1 (leaf 5 of WLD_Bd2_pages.txt) is literally the first entry of the volume: '(pais?): pis- „zerstampfen, zermalmen“ (bes. Getreide); zum Sachlichen vgl. Meringer WS. I 3ff.' — Nourai's 'Pis, Pais : crush, grind' is a direct rendering of that headword, and the page number is exact.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"POK\",\n          \"where\": \"p. 796, s.v. '(peis-1) : pis-'\",\n          \"stance\": \"supports\",\n          \"note\": \"'Root/lemma: (peis-1) : pis- | Meaning: to grind | Material: Old Indic pinasti ‚grinds, crushes‘ (3.pl. pisanti = Latin pinsunt), pista- ‚ground‘, n. ‚meal, flour‘, pestar- ‚Zerreiber‘ (: Latin pistor), Avestan pisant- ‚crushing‘ ... References: WP. II 1' — Pokorny cites exactly the page Nourai cites (POK_full.txt line ~65160).\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. pisiō (pins-) and pistos\",\n          \"stance\": \"supports\",\n          \"note\": \"'pisiō (pins-) ‘crush, pound’. WP II, 1. ... Skt. pinasmi, pp. pistah; Av. piš-, id.; Gk. ptíssō; Lat. pisō, pinsō' and 'pistos “crushed, pounded” ... Skt. piṣṭáḥ; piṣṭám n. ‘flour’; Av. cf. pištrō m. ‘crush, bruise’' (IEC.txt lines 12934, 12941) — Mann too refers the whole set to WP II 1.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, IE roots appendix\",\n          \"stance\": \"silent\",\n          \"note\": \"Grepped AHD_watkins1985.txt for 'peis', 'pis-', 'pistor': Watkins has no *peis-/*pis- 'crush' entry (the root has no English reflex he tracks other than through Latin pistor/pistil, which he does not list), so the American Heritage appendix is silent on this root.\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 5.55 'MEAL, FLOUR' and 5.56 'GRIND'\",\n          \"stance\": \"supports\",\n          \"note\": \"Buck's table for 'meal, flour' gives 'Skt. pista-, Av. [p]istra-', with note 7 'Skt. pista-, Av. pistra- : Skt. pis-', and under 5.56 GRIND: 'For the earlier process there is a distinctive group of cognates, namely Grk. ptíssō, Lat. pinsere, Skt. pis- (Walde-P. 2.1)'. Independent confirmation that the Avestan and Sanskrit words for 'flour' belong to this root.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Avestan\",\n          \"words\": \"pišant; pîštra\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Av. pišaṇt- is the present participle of the verb piš- 'to pound, crush' (< PIE *pis-, zero grade of *peys-), formally the exact match of Skt. piṇṣánt- and of Lat. pinsō; Bartholomae AiW glosses it 'zerstossend, durch Stossen zerhackend'. Av. pištra- n./m. is the *-tro-/-tlo- instrument-and-result noun of the same verb (*pis-tlo-m), with the regular Iranian s > š after i; Bartholomae gives it two senses, 1) 'Quetschung, Quetschwunde, durch ein stumpfes Instrument beigebrachte Wunde' and 2) '(Ausgequetschtes, sva.) Mehl' (Vd. 3.32), and it is sense 2 that Nourai's gloss 'flour' reproduces. Wiktionary lists only sense 1 ('bruise, injury') for pištra-, but Bartholomae, Horn (no. 320 'aw. pistra-'), Mo'in's footnote in Borhan and Buck 5.55 all use the 'flour' sense, so the gloss stands.\",\n          \"derivation_fa\": \"اوستایی pišaṇt- صفت فاعلی (اسم فاعل) فعل piš- «کوبیدن، خرد کردن» است و دقیقاً برابر سنسکریت piṇṣánt- و لاتین pinsō است؛ سِ ایرانی باستان پس از i به ش بدل شده است. pištra- نیز از همین ستاک با پسوند *-tra-/-tlo- ساخته شده و بارتولومه دو معنا برای آن می‌آورد: ۱) «له‌شدگی، زخم ناشی از ضربهٔ ابزار کُند» و ۲) «آرد» (ویدیوداد ۳، ۳۲). نورایی معنای دوم را آورده است که همان معنای مورد استفادهٔ هرن و باک است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peys-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"WLD2:1\",\n              \"status\": \"supports\",\n              \"note\": \"WLD II 1 (leaf 5): after the Sanskrit forms it prints 'av. [pišaṇt-] „zerstampfend“' (the Avestan word itself is lost in the OCR, but the German gloss 'zerstampfend' = 'crushing, grinding' survives and matches Nourai's gloss for pišant exactly).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW, s.v. pišaṇt- and ²pištra- (BRT.txt line 16419)\",\n              \"stance\": \"supports\",\n              \"note\": \"'j. pišaṇt- Adj. ‚zerstossend, durch Stossen zerhackend‘' and '²pištra- m. 1) ‚Quetschung, Quetschwunde, ... durch ein stumpfes Instrument beigebrachte Wunde‘ ... 2) ‚(Ausgequetschtes sva.) Mehl‘ ... V. 3.32 ... (si. piṣṭá- n. ‚Mehl‘)'. Both of Nourai's Avestan words, with his glosses.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 5.55 MEAL, FLOUR (SYN.txt line 9177 ff.)\",\n              \"stance\": \"supports\",\n              \"note\": \"Buck's word-table for 'meal, flour' lists Skt. pista-, Av. pistra-; note 7: 'Skt. pista-, Av. pistra- : Skt. pis-'. Independent confirmation of the 'flour' sense of Av. pištra-.\"\n            },\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 796\",\n              \"stance\": \"partial\",\n              \"note\": \"Pokorny lists only 'Avestan pisant- ‚crushing‘' under this root; he does not repeat pištra- (which Walde-Pokorny and Bartholomae do), so on the second word he is silent rather than contrary.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pest, past 2 «پست ۲»\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"NP پست pest/pist 'flour; parched-grain meal (Arabic sawīq)' continues MP pist [pst'] 'browned flour' (MacKenzie CPD 68), itself from Old Iranian *pišta-/pištra- (Av. pištra- 'flour'), i.e. the *-to- participle/*-tlo- noun of piš- 'to crush', with the normal Middle Iranian št > st before the New Persian period. Horn Grundriss no. 320 sets it out exactly as Nourai does ('pist ‚Mehl‘. aw. pistra-; ai. √peš- ‚zerreiben, zerstampfen‘ (piṣṭá-, piṣṭaka-)'), adding the Pamir cognates Wakhi pōšt, Shughni pišt, Sarikoli pašt 'roasted grain ground to flour'. On the vowel: Hübschmann p. 42 no. 320 corrects Horn to 'Np. pīst — nicht pist'; Borhan-e Qate' vocalises the flour word with kasra ('و بکسر اول هر آردی را گویند عموماً') and Mo'in prints '(پِ یا پَ)', which is precisely Nourai's double reading 'pest, past'; the '2' is Mo'in's homograph number (Mo'in's پست ۱ = 'low', پست ۳ = the French loan 'post/mail'). Note that Nourai's chart correctly keeps this word apart from the homograph past 'low, base' (Hübschmann no. 316: past < *patta-, Skt. patita-).\",\n          \"derivation_fa\": \"«پِست» در فارسی نو به معنی آرد و به‌ویژه آرد گندم و جوی بریان‌کرده (معادل عربی آن سویق)، دنبالهٔ فارسی میانهٔ pist است که مکنزی آن را به معنی «browned flour» ضبط کرده، و آن از ایرانی باستان *pišta-/pištra- (اوستایی pištra-) می‌آید؛ خوشهٔ شت در دورهٔ میانه به ست بدل شده است. معین در حاشیهٔ برهان قاطع می‌نویسد: «هرن این کلمه را pīst آورده، از اوستایی pištra؛ هندی باستان peṣ (ساییدن، خردکردن، له کردن)؛ وخی pūšt، شغنی pišt، سریکلی pašt (گندم برشته، آرد ساییده)؛ پهلوی pēst، کارنامهٔ اردشیر ۱۴». خوانش دوگانهٔ نورایی (pest / past) همان ضبط معین «(پِ یا پَ)» است و عدد ۲ شمارهٔ هم‌نگاشت در فرهنگ معین است. ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/%D9%BE%D8%B3%D8%AA\",\n            \"https://abadis.ir/fatofa/%D9%BE%D8%B3%D8%AA/\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"HUB:42\",\n              \"status\": \"supports\",\n              \"note\": \"Hübschmann, Persische Studien p. 42, §320 (HUB.txt line 1414; the page break '— 42 —' stands a few lines above, and the index reads 'pīst 42'): 'Np. pīst — nicht pist — heisst ‚Mehl, geröstetes Mehl‘.' The page Nourai cites is exactly where Hübschmann treats this word; he confirms the meaning 'flour, roasted flour' and only corrects the vowel length.\"\n            },\n            {\n              \"ref\": \"MON:782\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in Farhang-e Farsi, homograph پست ۲: 'پست [ساییدن، خرد کردن] (ا.) هر نوع آرد (عموماً). آردی که گندم و جو و نخود آن را بریان کرده باشند (خصوصاً)؛ آرد بو داده، تلخان، قاووت، سویق' (MON_part1.txt line 31660; via abadis: '(پِ یا پَ) (اِ.) ۱ - هر نوع آرد. ۲ - آرد بریان شدهٔ گندم یا جو'). Mo'in's etymological bracket '[ساییدن، خرد کردن]' is the same 'crush, grind' root Nourai draws; the page number is internally consistent with MON:643 for پاتیل in the same volume.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss no. 320 (HRN.txt line 3059)\",\n              \"stance\": \"supports\",\n              \"note\": \"'320. pist ‚Mehl‘. aw. pistra-; ai. √peš- ‚zerreiben, zerstampfen‘ (pištá-, skr. pištaka-), waḵ. pōšt; šiyṅ. pišt, sar. pašt ‚geröstetes Korn, zu Mehl zerrieben‘.' This is Nourai's arrow (Av. pištra- → NP pist) verbatim.\"\n            },\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate' ed. Mo'in, s.v. پست (BQT_v1_pages.txt leaf 628 ≈ printed p. 403), text + Mo'in's footnote 1\",\n              \"stance\": \"supports\",\n              \"note\": \"Text: 'بست ... بفتح اول ... نقیض بلند ... و بکسر اول هر آردی را گویند عموماً و آردی که گندم و جو و نخود آن را بریان کرده باشند خصوصاً و آن را بعربی سویق خوانند'. Mo'in's footnote: '۱ - هرن این کلمه را [pīst] آورده، از اوستایی pištra؛ هندی باستان peṣ (ساییدن، خردکردن، له کردن). وخی pūšt، شغنی pišt، سریکلی pašt (گندم برشته، آرد ساییده) «اسحق ۳۲۰». طبری ...، پهلوی pēst «کارنامهٔ اردشیر ۱۴»'.\"\n            },\n            {\n              \"src\": \"PHD\",\n              \"where\": \"MacKenzie, CPD p. 68 s.v. pist (PHD.txt line 551)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pist [pst' | N ~] browned flour.' The Middle Persian link that Nourai's chart skips over; MacKenzie's New Persian equivalent '~' is the same پست.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi (ARY_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Grepped 'پست' in ARY_pages.txt: all hits are the adjective پست 'low' in the introductory chapters and پستان 'breast'; there is no headword for the flour word.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"pinašti; pîštah\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Skt. pináṣṭi 'crushes, grinds' is the nasal-infix present *pi-né-s-ti of *peys- (3 pl. piṁṣánti = Lat. pinsunt), and piṣṭá- is its *-to- participle 'ground', used as a neuter noun piṣṭám 'meal, flour' — Nourai's 'pîštah' is the nominative piṣṭáḥ in his usual -ah rendering of visarga. One slip of gloss: pináṣṭi is an active present 'crushes, grinds', not the passive 'crushed' (that is piṣṭá-); the forms and the derivation are otherwise exactly those of the cited reference. Sanskrit piṣṭá- and Avestan pištra- are thus the Indo-Iranian pair on which the whole chart rests.\",\n          \"derivation_fa\": \"سنسکریت pináṣṭi «می‌ساید، خرد می‌کند» زمان حال با میانوند خیشومی (*pi-né-s-ti) از ریشهٔ *peys- است و piṣṭá- صفت مفعولی همان ریشه که به صورت اسم خنثی معنی «آرد» گرفته است؛ صورت «pîštah» نورایی همان صورت نهادی piṣṭáḥ است. تنها لغزش کوچک، معنای «crushed» برای pinašti است که باید «می‌ساید» (معلوم) باشد. در کل ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peys-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"WLD2:1\",\n              \"status\": \"supports\",\n              \"note\": \"WLD II 1 (leaf 5): 'Ai. pináṣṭi „zerreibt, zerstampft“ (3. pl. piṁṣanti = lat. pinsunt), piṣṭá- „gemahlen“, [piṣṭa-] n. „Mehl“, peṣṭar- „Zerreiber“ (: lat. pistor)'. Both of Nourai's Sanskrit words are on the cited page, with the glosses he gives (except that pináṣṭi is active).\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"POK\",\n              \"where\": \"p. 796\",\n              \"stance\": \"supports\",\n              \"note\": \"'Old Indic pinasti ‚grinds, crushes‘ (3.PL pisanti = Latin pinsunt), pista- ‚ground‘, n. ‚meal, flour‘'.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. pistos (IEC.txt line 12941)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pistos “crushed, pounded; powder, bruise” ... Skt. piṣṭáḥ, id.; piṣṭám, n. ‘flour’'.\"\n            },\n            {\n              \"src\": \"SYN\",\n              \"where\": \"Buck 5.56 GRIND\",\n              \"stance\": \"supports\",\n              \"note\": \"'Skt. pis- ‘crush’, representing the earlier process, whence pista- ‘meal’'.\"\n            }\n          ]\n        }\n      ]\n    },\n    {\n      \"entry\": 6,\n      \"root\": \"Pô 2, Pôi, Pî\",\n      \"verdict\": \"confirmed\",\n      \"modern_form\": \"PIE *peh₃(y)- / traditional *pō(i)- : *pī- 'to drink'\",\n      \"note\": \"Pokorny p. 839-840 heads the entry 'pō(i)-2 : pō(y)- and (from pō-i-) pī- | Meaning: to drink', so Nourai's triple 'Pô 2, Pôi, Pî' and the page number reproduce the cited source exactly, down to the '2' that distinguishes it from pō(i)-1 'to graze/protect' on the same page. In laryngeal terms the root is *peh₃- (Wiktionary, LIV; alternative *peh₃(y)-), which is the same thing written modernly: *peh₃-ti- > Gk. pósis, *ph₃-tó- > Lat. pōtus. Language label and gloss correct. Three problems elsewhere in the chart: the Sanskrit 'pâtila' (and hence the Persian پاتیل branch) does not belong to this root; the Greek headword is printed 'pusis' for pósis; and English 'beer' is only one of two competing accounts. NB: on the printed page an entirely empty, unlabelled box hangs to the right of the Avestan node — a blank placeholder in the book with no language, word or reference, correctly ignored by the extraction.\",\n      \"note_fa\": \"ریشهٔ هندواروپایی آغازین *peh₃(y)- «نوشیدن» که در سنت قدیم‌تر *pō(i)-/*pī- نوشته می‌شده است. پوکورنی در صفحهٔ ۸۳۹ دقیقاً همین سه صورت را سرمدخل کرده است، پس عنوان ریشه و شمارهٔ صفحه درست است. اما در درون نمودار سه اشکال هست: انتساب سنسکریت «pâtila» (و از راه آن «پاتیل» فارسی) به این ریشه پذیرفتنی نیست؛ صورت یونانی «pusis» غلط چاپی به‌جای pósis است؛ و انگلیسی beer تنها یکی از دو فرضیهٔ رقیب است. همچنین در صفحهٔ چاپی یک کادر خالی و بی‌عنوان کنار گرهٔ اوستایی دیده می‌شود که محتوایی ندارد.\",\n      \"sources\": [\n        \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%83-\",\n        \"https://www.etymonline.com/word/beverage\"\n      ],\n      \"ref_check\": [\n        {\n          \"ref\": \"POK:839\",\n          \"status\": \"supports\",\n          \"note\": \"Pokorny IEW: 'Root/lemma: pō(i)-2 : pō(y)- and (from pō-i-) pō- [pī-] | Meaning: to drink | Grammatical information: Aoristwurzel, wherefore secondary present pi-pō-mi, pi-bō-mi ... References: WP. II 71 f., WH. I 103 f., Trautmann 228 f. | Page(s): 839-840' (POK_full.txt line 68799 ff.). Nourai's three root variants and his page number are taken straight from this entry.\"\n        }\n      ],\n      \"consulted\": [\n        {\n          \"src\": \"WLD\",\n          \"where\": \"Walde-Pokorny Bd. II p. 71 (leaf 75 of WLD_Bd2_pages.txt)\",\n          \"stance\": \"supports\",\n          \"note\": \"'pō(i): pī und (von pō aus) pō „trinken“. Langdiphthongische Wz. nach Schulze KZ. 27, 420 f. Praes. *pi-pō-mi ... Themat. Praes. ai. pibati „trinkt“, lat. bibo, -ere, air. ib- ds.' — the earlier edition of the same entry.\"\n        },\n        {\n          \"src\": \"AHD\",\n          \"where\": \"Watkins 1985, s.v. pō(i)-\",\n          \"stance\": \"supports\",\n          \"note\": \"'pō(i)-. To drink. Contracted from *poa(i)-. ... 1. Suffixed reduced form *pō-to- in Latin pōtus, drunk (> pōtāre, to drink): POISON, POTABLE, POTATION, POTATORY, POTION. 2. Reduplicated form *pi-pō-o-, whence *pi-bo-, assimilated to *bi-bo- in Latin bibere, to drink: BEVERAGE, BIB, BIBULOUS; IMBIBE. 3. Suffixed zero-grade form *pō-ti- in Greek posis, drink, drinking: SYMPOSIUM. [Pok. 2. pō(i)- 839.]'\"\n        },\n        {\n          \"src\": \"IEC\",\n          \"where\": \"Mann, s.v. pibō (IEC.txt line 12856)\",\n          \"stance\": \"supports\",\n          \"note\": \"'pibō ‘drink’. WP II, 71. Skt. píbami; Lat. (assimilated conss.) bibo, -ere, pf. bibi, id.; Falisc. pafo or pipafo; OIr. ibim ...'\"\n        },\n        {\n          \"src\": \"SYN\",\n          \"where\": \"Buck 5.13 DRINK (vb.)\",\n          \"stance\": \"supports\",\n          \"note\": \"Buck's table for 'drink' gives 'ChSl. piti, SCr. piti, Russ. pit', Skt. pā-' and notes 'The words for the sb. ‘drink’ are nearly all obvious derivs. of the roots appearing in the verbs, as Grk. pôma, Lat. potio, potus'.\"\n        }\n      ],\n      \"nodes\": [\n        {\n          \"id\": 1,\n          \"lang\": \"Sanskrit\",\n          \"words\": \"pâti; pâtila\",\n          \"verdict\": \"disputed\",\n          \"derivation\": \"The first word is right: Skt. pāti 'drinks' (RV) is the thematised root present of *peh₃- (Pokorny 'Old Indic pāti ‚trinkt‘', beside the reduplicated píbati and the causative pāyáyati 'gives to drink'); the same root gives pātra- n. 'drinking vessel' (= Lat. pōculum < *peh₃-tlo-m) and pātar- 'drinker' (= Lat. pōtor). The second word is not: there is no Sanskrit pātila 'a large drinking vessel'. What the lexica have is pātilī (पातिली), f., attested only in the native lexicographers (Amarasiṃha, Hemācandra, Medinīkośa), glossed by Monier-Williams 'a trap or snare for catching deer; a small earthen pot (used by religious mendicants); a woman of a particular class', and derived by MW hesitantly from √pat 'to fall' ('[from] √pat ?'), not from √pā 'to drink' — and 'a small earthen pot' is the opposite of 'a large drinking vessel'. Nourai's own NOTE ('The link between \\\"pâti\\\" and \\\"pâtila\\\" is not certain') concedes the weak point; modern scholarship takes the harder line that pātilī has nothing to do with the root 'to drink' at all, and that if the pot-sense is old it is more likely a derivative of pātra-/pātrī with the -ila suffix. Verdict for the node = disputed, driven by the second word only.\",\n          \"derivation_fa\": \"واژهٔ نخست درست است: سنسکریت pāti «می‌نوشد» از همین ریشه است و هم‌ریشهٔ pātra- «ظرف نوشیدن» (= لاتین pōculum) است. اما واژهٔ دوم پذیرفتنی نیست: در سنسکریت صورتی به شکل pātila به معنی «جام بزرگ» در دست نیست؛ آنچه هست pātilī (पातिली) است که تنها در فرهنگ‌نامه‌های بومی آمده و مونیر–ویلیامز آن را «دام آهوگیری؛ کوزهٔ کوچک سفالین گدایان؛ زنی از طبقه‌ای خاص» معنی کرده و با تردید از ریشهٔ √pat «افتادن» گرفته است، نه از √pā «نوشیدن». خود نورایی هم در یادداشت نمودار به نااستواری این پیوند اعتراف کرده است؛ پژوهش امروزی آن را رد می‌کند.\",\n          \"sources\": [\n            \"https://www.wisdomlib.org/definition/patili\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%83-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:839\",\n              \"status\": \"partial\",\n              \"note\": \"Pokorny p. 839 has the first word — 'Old Indic pāti ‚trinkt‘, Aor. apāt, pāy-ayati, pāyate ‚tränkt‘ ... pātra- n. ‚drinking vessel‘ (*pō-tlo-m = Latin pōculum ‚goblet‘) ... pātar-, pātār- m. ‚Trinker‘' — but no pātila anywhere in the entry. The vessel word Pokorny recognises is pātra-, not pātila.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II p. 71 (leaf 75)\",\n              \"stance\": \"partial\",\n              \"note\": \"'si. pā-ti „trinkt“, pāy-áyati „gibt zu trinken, tränkt“ ... pātra- n. „Trinkgefäß“ (= lat. poclum, poculum „Becher“)'. Same picture as Pokorny: pāti and pātra- yes, pātila no.\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, s.v. pō(i)-\",\n              \"stance\": \"partial\",\n              \"note\": \"Watkins reconstructs *peh₃-tlo-m for the vessel word (Sanskrit pātra, Latin pōculum); no *-ila formation is recognised.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, IE Comparative Dictionary\",\n              \"stance\": \"silent\",\n              \"note\": \"Grepped IEC.txt for 'patila', 'pātil': no entry; Mann's material for this root is pibō, pōtos, pōtis only.\"\n            }\n          ]\n        },\n        {\n          \"id\": 2,\n          \"lang\": \"Persian\",\n          \"words\": \"pâtîl «پاتیل» (پاتیله)\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"NP پاتیل / پاتیله pātīl(a) 'large open-mouthed copper cauldron (also the boiler under a bath-house cistern)' is indeed marked as an Indic loan by the very dictionary Nourai cites: Mo'in's entry reads 'پاتیل [سنس.] (ا.) دیگ بزرگ مسی، دیگ خزانهٔ حمام', '[سنس.]' being his tag for Sanskrit. Hasandust likewise takes it from Indo-Aryan (Hindi patīlā 'large cooking pot'), comparing Skt. pātilī 'a small earthen pot'. So the arrow 'Indic → Persian' is well founded, and the word is late (not in Borhan-e Qate' as a headword — it occurs there only inside a recipe — and unknown to Horn and Hübschmann), which fits a Persian–Indian contact loan of the Islamic period rather than an inherited word. What does not follow is the rest of the chain: since Skt. pātilī is not a derivative of √pā 'to drink' (Monier-Williams: 'from √pat ?'), پاتیل cannot be traced to PIE *peh₃-. Nourai's cross-reference in the box ('For another possible root of \\\"pâtîl\\\" see root \\\"Batiaxě\\\"', i.e. Gk. batiakē 'a Persian cup') shows he was himself undecided; neither alternative is established.\",\n          \"derivation_fa\": \"«پاتیل» (و صورت دیگر آن «پاتیله») در فارسی به معنی دیگ بزرگ مسین و دهان‌گشاد است. معین در برابر این مدخل نشانهٔ «[سنس.]» (= سنسکریت) گذاشته و این دقیقاً همان ادعای نورایی است؛ حسن‌دوست نیز آن را وام‌واژه‌ای هندی (هندی patīlā) می‌داند و به سنسکریت pātilī «کوزهٔ کوچک سفالین» ارجاع می‌دهد. پس پیکان «هندی/سنسکریت ← فارسی» پذیرفتنی است، امّا وصل کردن آن به ریشهٔ «نوشیدن» درست نیست، زیرا pātilī از √pā مشتق نشده است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://abadis.ir/fatofa/%D9%BE%D8%A7%D8%AA%DB%8C%D9%84/\",\n            \"https://www.wisdomlib.org/definition/patili\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"MON:643\",\n              \"status\": \"supports\",\n              \"note\": \"Mo'in Farhang-e Farsi s.v. پاتیل: '[ سنس . ] (اِ. ) دیگ بزرگ مسی ، دیگ خزانة حمام .' (read via abadis.ir «فرهنگ معین» block). The bracket '[سنس.]' is Mo'in's Sanskrit origin tag, exactly the claim of Nourai's arrow; the page (vol. 1 p. 643) is also consistent with MON:782 for پست in the same volume.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BQT\",\n              \"where\": \"Borhan-e Qate' ed. Mo'in, vol. 1 (BQT_v1_pages.txt)\",\n              \"stance\": \"silent\",\n              \"note\": \"Grepped 'پاتیل'/'باتیل' in BQT_v1_pages.txt: the only occurrence is inside another entry's recipe ('... آنگاه در پاتیلی کنند و عسل در آن ریزند', leaf 260). Borhan has no پاتیل headword and therefore no Mo'in footnote on it.\"\n            },\n            {\n              \"src\": \"HRN\",\n              \"where\": \"Horn, Grundriss der neupersischen Etymologie\",\n              \"stance\": \"silent\",\n              \"note\": \"Grepped HRN.txt for 'patil': no entry — Horn does not treat پاتیل, consistent with a late loanword.\"\n            },\n            {\n              \"src\": \"HUB\",\n              \"where\": \"Hübschmann, Persische Studien\",\n              \"stance\": \"silent\",\n              \"note\": \"Grepped HUB.txt for 'patil': nothing; Hübschmann does not discuss the word.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi\",\n              \"stance\": \"silent\",\n              \"note\": \"Grepped 'پاتیل' in ARY_pages.txt: no entry, i.e. Aryanpur does not claim an Indo-European pedigree for it either.\"\n            }\n          ]\n        },\n        {\n          \"id\": 3,\n          \"lang\": \"Avestan\",\n          \"words\": \"vispo-pitay\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Av. vīspō.pitay- is real and does belong to this root: it is a compound of vīspa- 'all' with a *-ti- abstract of *peh₃(y)-/pī- (the zero-grade pī-ti- that also gives Skt. pītí- 'a drinking, draught' and Lat. pōti-ō). Bartholomae AiW lists it 'g. vīspō.pitay- Adj. (auch fem.) ‚alltränkend‘', epithet of the aġənyā 'cows/waters' at Y. 38.5, and Pokorny quotes the same form on p. 839 as 'Avestan vispo-pitay- ‚alltränkend‘'. The gloss in the chart is wrong: the word means 'giving drink to all, all-watering' (an active/causative sense), not 'drunk' — that gloss belongs to Lat. pōtus in the Latin box two rows down. Route and root are right, the meaning is not; hence plausible rather than confirmed.\",\n          \"derivation_fa\": \"اوستایی vīspō.pitay- واژه‌ای است واقعی و از همین ریشه: مرکّب از vīspa- «همه» و اسم معنای *-ti- از صورت کاهشیدهٔ pī- (هم‌ریشه با سنسکریت pītí- و لاتین pōtiō). بارتولومه آن را «همه‌سیراب‌کننده (alltränkend)» معنی کرده و آن را صفت آب‌ها/گاوان در یسنا ۳۸،۵ دانسته است؛ پوکورنی نیز در صفحهٔ ۸۳۹ همین صورت و همین معنا را می‌آورد. پس معنای «drunk» در نمودار نادرست است (آن معنا از آنِ لاتین pōtus است). ریشه درست است، معنا نادرست؛ با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%83-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:839\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny p. 839 in the pō(i)-2 entry: 'participle Pass. ablaut. pītá- ‚getrunken (habend)‘, pītí-ḥ ‚das Trinken, Trunk‘, Avestan vispo-pitay- ‚alltränkend‘'. The form and its position under this root are Pokorny's own; the gloss he gives is 'all-watering', not 'drunk'.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"BRT\",\n              \"where\": \"Bartholomae AiW s.v. vīspō.pitay- (BRT.txt line 24506)\",\n              \"stance\": \"partial\",\n              \"note\": \"'g. vīspō.pitay- Adj. (auch fem.) ‚alltränkend‘: apōca vā .. aġənyǎ .. [vīspō.]pitayǎ Y. 38.5.' Confirms the word and its Avestan status, contradicts the gloss 'drunk'.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II 71-72\",\n              \"stance\": \"silent\",\n              \"note\": \"The 1927 entry lists the Indo-Iranian material (ai. pāti, pibati, pātra-, pāna-) but not vīspō.pitay-, which Pokorny added in 1959.\"\n            }\n          ]\n        },\n        {\n          \"id\": 4,\n          \"lang\": \"Greek\",\n          \"words\": \"pusis; sun-posion\",\n          \"verdict\": \"transcription_suspect\",\n          \"derivation\": \"The second word is impeccable: Gk. συμπόσιον sumpósion 'drinking party' = σύν 'together' + πόσις 'drinking' + -ιον, the institution of the post-dinner wine party described by Plato and Xenophon; Nourai's 'sun-' is his standard rendering of συν- and his cross-reference '☞ Sem 1' for that element is right, since Pokorny files Gk. σύν/ξύν under 2. sem- (p. 902), just as Watkins does ('ksun ... [In Pok. 2. sem- 902]'). The first word is a misprint: the Greek noun is πόσις pósis f. 'a drinking, a drink' (< *peh₃-ti-s ~ *ph₃-téy-s), not *pusis, and it means 'a drink/drinking', not 'drunk'. The very reference Nourai cites gives the right form: Watkins, 'Suffixed zero-grade form *pō-ti- in Greek posis, drink, drinking: SYMPOSIUM'. I rendered PDF p. 404 at 200 and 500 dpi and read the box: the printed page itself shows 'pusis : drunk', so the extraction is faithful and the error is the book's (an o/u slip, with the gloss of Latin pōtus carried over).\",\n          \"derivation_fa\": \"واژهٔ دوم کاملاً درست است: یونانی سومپوسیون (sumpósion) «بزم می‌گساری» مرکّب است از پیشوند سین‌ («با هم») و pósis «نوشیدن»؛ ارجاع نورایی به ریشهٔ Sem 1 برای جزء نخست نیز درست است، زیرا پوکورنی و واتکینز هر دو سینِ یونانی را زیر sem- (صفحهٔ ۹۰۲) آورده‌اند. امّا صورت «pusis» خطاست: واژهٔ یونانی pósis است به معنی «نوشیدن، نوشیدنی»، نه «drunk». تصویر صفحهٔ چاپی (PDF ۴۰۴) را با دقت ۵۰۰ دی‌پی‌آی دیدم: خود کتاب «pusis : drunk» چاپ کرده، پس خطای چاپی کتاب است و خوانش اسکن درست است.\",\n          \"error_in\": \"book\",\n          \"book_prints\": \"pusis : drunk\",\n          \"correct_form\": \"posis (πόσις) 'a drinking, a drink'\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symposium\",\n            \"https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/peh%E2%82%83-\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 s.v. pō(i)-: '3. Suffixed zero-grade form *pō-ti-, *pō-ti- in Greek posis, drink, drinking: SYMPOSIUM.' The reference supports the derivation of sympósion but prints the Greek word as 'posis' with the gloss 'drink, drinking' — i.e. it contradicts both the form 'pusis' and the gloss 'drunk' in the chart.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. symposium (KLN_1966.txt line 37831, printed p. 1556/1557)\",\n              \"stance\": \"supports\",\n              \"note\": \"'symposium, n., 1) in ancient Greece, a drinking party ... — L., fr. Gk. συμπόσιον, ‘a drinking feast’, lit. ‘a drinking together’, fr. σύν (see syn-) and πόσις, ‘a drinking’, which is rel. to πίνειν, ‘to drink’. See potion.'\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II 71\",\n              \"stance\": \"supports\",\n              \"note\": \"'abl. gr. πόσις „Trunk, das Trinken“, und ἄμπωτις „Ebbe“, lat. potio „das Trinken“' — the Greek word is πόσις and means 'drink, drinking'.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Symposium (SKT.txt line 19028)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Symposium, a merry feast. (L.–Gk.) L. symposium. — Gk. συμπόσιον, a drinking-party, banquet. — Gk. συμ- (for σύν), together; πο-, base of πέπωκα, I drank, πόσις, a drink. See Potable.'\"\n            }\n          ]\n        },\n        {\n          \"id\": 5,\n          \"lang\": \"Latin\",\n          \"words\": \"\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Empty pass-through box: Latin symposium, the direct loan of Gk. συμπόσιον taken over unchanged (with the usual -ον > -um) and used by Cicero and Varro of the Greek institution and as the title of Plato's dialogue; it is the form from which both the French and the English word in the boxes below are taken. Klein states the step: 'symposium ... — L., fr. Gk. συμπόσιον'.\",\n          \"derivation_fa\": \"کادر خالی واسطه: لاتین symposium وام‌گیری مستقیم از یونانی سومپوسیون است با تبدیل معمول پایانهٔ -ον به -um؛ همین صورت لاتین سرچشمهٔ صورت فرانسوی و انگلیسی در کادرهای بعدی است. کلاین همین مسیر را ثبت کرده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symposium\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"None\",\n              \"status\": \"not_checked\",\n              \"note\": \"The box carries no reference in the book (refs=None) and no word; nothing of Nourai's own to check.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. symposium\",\n              \"stance\": \"supports\",\n              \"note\": \"'— L., fr. Gk. συμπόσιον, ‘a drinking feast’' — the Latin intermediate is explicit.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Symposium\",\n              \"stance\": \"supports\",\n              \"note\": \"'(L.–Gk.) L. symposium. — Gk. συμπόσιον' — same two-step chain.\"\n            }\n          ]\n        },\n        {\n          \"id\": 6,\n          \"lang\": \"French\",\n          \"words\": \"symposium\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"French symposium is a learned borrowing of Latin symposium, first in the antiquarian sense 'Greek drinking party' (17th–18th c., in translations of Plato and Xenophon) and then, in the 20th c. and under Anglo-American influence, in the modern sense 'scholarly conference on one theme' — which is the sense the Persian box below carries. The Latin → French step is uncontroversial; what is not independently verifiable is Nourai's implicit claim that it was specifically French (rather than English, or Latin directly) that mediated the word to Persian, a claim resting entirely on Moshiri's VOP p. 216, of which no copy exists online or on disk.\",\n          \"derivation_fa\": \"فرانسوی symposium وام‌واژه‌ای عالمانه از لاتین است، نخست به معنی تاریخی «بزم می‌گساری یونانی» و سپس در سدهٔ بیستم به معنی «هم‌اندیشی علمی». خود این مرحله تردیدبردار نیست؛ آنچه قابل راستی‌آزمایی مستقل نیست این است که همین صورت فرانسوی (و نه انگلیسی) واسطهٔ ورود واژه به فارسی بوده باشد؛ منبع نورایی (فرهنگ واژه‌های اروپایی مشیری، ص ۲۱۶) در دسترس نیست. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symposium\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"VOP:216\",\n              \"status\": \"not_checked\",\n              \"note\": \"Mahshid Moshiri, Farhang-e Vazheha-ye Orupayi dar Farsi (Alborz 1371): refs_online.json records kind='none' — no scan on archive.org, ketabnak or noorlib, no ebook; the page cannot be checked.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. symposium\",\n              \"stance\": \"partial\",\n              \"note\": \"Klein derives the English word straight from Latin and does not mention a French stage; he thus supports Latin → modern European languages but not specifically Latin → French → Persian.\"\n            },\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in, s.v. سمپوزیوم (MON_part1.txt line 79557)\",\n              \"stance\": \"partial\",\n              \"note\": \"Mo'in prints the Latin-script etymon as 'symposium' without naming a European intermediary: 'سمپوزیوم: symposium ضیافتی که در آن پس از صرف طعام به باده‌گساری می‌پرداختند ... مجمعی که در آن اشخاص مختلف راجع به موضوعی واحد مقالاتی تهیه کنند یا سخنرانی‌هایی ایراد نمایند'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 7,\n          \"lang\": \"Persian\",\n          \"words\": \"sampozîyom «سمپوزیوم»\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Modern Persian سمپوزیوم sampozīyom 'symposium, scholarly conference' is a 20th-century European loan, and Mo'in's dictionary confirms both the word and its two senses ('a banquet at which, after the meal, they drank wine ... a gathering at which different people present papers or lectures on a single topic'), printing the etymon in Latin letters as 'symposium'. The Persian shape shows the usual adaptation of European -sym- as سم‌ sam- and of the ending -ium as -یوم -iyom. Whether the immediate donor was French (Nourai/Moshiri) or English is not decided by any source I could reach: the modern conference sense is itself an Anglicism in French, and Persian took most of its academic vocabulary of the 1930s–50s through French, so French mediation is likely but unproved. One detail of form: the printed page prints «سمپوزیم» (with a single و), while the JSON gives the standard spelling «سمپوزیوم» that Mo'in also uses — see the summary for the extraction note.\",\n          \"derivation_fa\": \"«سمپوزیوم» وام‌واژه‌ای اروپایی از سدهٔ بیستم است. معین آن را با ریشهٔ لاتین‌نویسِ symposium ثبت کرده و دو معنای «بزم باده‌گساری پس از شام» و «مجمع علمی یک‌موضوعی» را برای آن آورده است. در وام‌گیری، sym- اروپایی به «سم‌» و پایانهٔ -ium به «ـیوم» بدل شده است. این‌که زبان میانجی فرانسوی بوده باشد یا انگلیسی، با منابع در دسترس قطعی نمی‌شود؛ احتمال فرانسوی بیشتر است. با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symposium\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"VOP:216\",\n              \"status\": \"not_checked\",\n              \"note\": \"Moshiri's Farhang-e Vazheha-ye Orupayi dar Farsi is not available in any scan (refs_online.json: kind='none', re-searched 2026-09); the claim of French mediation cannot be checked against Nourai's source.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"MON\",\n              \"where\": \"Mo'in, s.v. سمپوزیوم (MON_part1.txt line 79557)\",\n              \"stance\": \"supports\",\n              \"note\": \"'سمپوزیوم: symposium ضیافتی که در آن پس از صرف طعام به باده گساری می‌پرداختند و مهمانان به تماشای رقص زیبارویان و شنیدن موسیقی مشغول می‌شدند ... مجمعی که در آن اشخاص مختلف راجع به موضوعی واحد مقالاتی تهیه کنند' — confirms the Persian word, its spelling with و, and the 'drinking party' → 'conference' sense development.\"\n            },\n            {\n              \"src\": \"ARY\",\n              \"where\": \"Aryanpur, Farhang-e Rishe-ha-ye Hend-o-Orupayi\",\n              \"stance\": \"silent\",\n              \"note\": \"Grepped 'سمپوز' in ARY_pages.txt: no entry (Aryanpur's dictionary covers inherited vocabulary, not modern European loans).\"\n            }\n          ]\n        },\n        {\n          \"id\": 8,\n          \"lang\": \"English\",\n          \"words\": \"symposium\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"English symposium is a direct learned borrowing of Latin symposium (< Gk. συμπόσιον), first used in English in the 1580s as the title of Plato's dialogue, then from 1711 of a convivial drinking-and-conversation meeting, and from 1784 in the modern sense 'meeting on a given subject'; the plural stays Greek (symposia), and the derivatives symposiarch (c. 1600) and symposiac keep the Greek shape. Nourai's chart routes it through the (empty) Latin box, which is right; it does not go through French.\",\n          \"derivation_fa\": \"انگلیسی symposium وام‌گیری مستقیم از لاتین (و از راه آن یونانی) است؛ نخست در دههٔ ۱۵۸۰ میلادی به‌عنوان نام رسالهٔ افلاطون، از ۱۷۱۱ به معنی مجلس باده و گفتگو و از ۱۷۸۴ به معنی هم‌اندیشی علمی. مسیری که نورایی رسم کرده (یونانی ← لاتین ← انگلیسی) درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/symposium\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"KLN:1557\",\n              \"status\": \"supports\",\n              \"note\": \"Klein vol. II (the entry stands between the page markers 1556 and 1565 in KLN_1966.txt, i.e. on printed p. 1556/1557, exactly where Nourai cites it): 'symposium, n., 1) in ancient Greece, a drinking party; 2) a meeting, conference for conversation or discussion. — L., fr. Gk. συμπόσιον ... See potion.'\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Symposium (SKT.txt line 19028)\",\n              \"stance\": \"supports\",\n              \"note\": \"'Symposium, a merry feast. (L.–Gk.) L. symposium. — Gk. συμπόσιον, a drinking-party, banquet.'\"\n            },\n            {\n              \"src\": \"AHD\",\n              \"where\": \"Watkins 1985, index and s.v. pō(i)-\",\n              \"stance\": \"supports\",\n              \"note\": \"'SYMPOSIUM pō(i)-' in the English index; in the root entry, 'Greek posis, drink, drinking: SYMPOSIUM'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 9,\n          \"lang\": \"Latin\",\n          \"words\": \"bibere; pôtus\",\n          \"verdict\": \"confirmed\",\n          \"derivation\": \"Two Latin reflexes of the same root by two different formations. bibō, bibere 'to drink' is the inherited reduplicated present *pi-bh₃-e-ti > Italic *pibō, with regressive assimilation p…b > b…b (Faliscan still has pipafo 'I shall drink', and Old Irish ibid, Skt. píbati preserve the p-); Ernout-Meillet note the postverbal biber 'boisson' beside it. pōtus is the *-to- participle *ph₃-tó- 'drunk, having drunk', which also yields the noun pōtus, -ūs 'a drink' and, denominatively, pōtāre 'to tipple' and pōtiō 'a drinking, draught'; the vessel word pōculum < *peh₃-tlo-m belongs to the same set. Pokorny p. 839 lists precisely these forms under this root.\",\n          \"derivation_fa\": \"دو بازماندهٔ لاتینی از یک ریشه با دو ساخت: bibere از زمان حال دوگانه‌سازی‌شدهٔ *pi-bō می‌آید که پِ آغازین به ب همگون شده است (فالیسکی هنوز pipafo دارد و سنسکریت píbati و ایرلندی کهن ibid پِ را نگاه داشته‌اند)؛ pōtus صفت مفعولی *-to- است به معنی «نوشیده‌شده» که از آن pōtāre و pōtiō و pōculum ساخته شده است. پوکورنی در صفحهٔ ۸۳۹ همین صورت‌ها را زیر این ریشه آورده است؛ ادعای نورایی درست است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/beverage\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"POK:839\",\n              \"status\": \"supports\",\n              \"note\": \"Pokorny p. 839-840: 'Latin bibō, -ere ‚drink‘ (assimil. from *pibō), Faliscan pipafo ‚ich werde drink‘; Latin pōtō, -āre ‚drink strong‘, pōtus ‚drunk, intoxicated, getrunken‘ (= Lithuanian puota f. ‚Zechgelage‘), pōtus, -ūs m. ‚drink‘ ... pōculum ‚goblet‘ (*pō-tlo-m), pōtor m. ‚Trinker‘.' Both of Nourai's Latin words, on the cited page.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"LAT\",\n              \"where\": \"Ernout-Meillet, s.v. bibo (LAT.txt line 7217) and poculum (line 49568)\",\n              \"stance\": \"supports\",\n              \"note\": \"'bibo, -is, bibi, (bibitum), bibere: boire ... Ancien, usuel; panroman' and 'biber, -ris m.: boisson. Nom postverbal ... infinitif syncopé de bibō (cf. gr. πιεῖν)'; 'poculum (arch. pocolom), -i n.: de *po-tlo-m “vase à boire”'. Also 'de pōtus, poculum' at line 14181.\"\n            },\n            {\n              \"src\": \"IEC\",\n              \"where\": \"Mann, s.v. pibō (IEC.txt line 12856)\",\n              \"stance\": \"supports\",\n              \"note\": \"'pibō ‘drink’. WP II, 71. Skt. píbami ...; Lat. (assimilated conss.) bibo, -ere, pf. bibi, id.' — states the assimilation explicitly.\"\n            },\n            {\n              \"src\": \"WLD\",\n              \"where\": \"Walde-Pokorny Bd. II 71\",\n              \"stance\": \"supports\",\n              \"note\": \"'lat. pōtus „getrunken habend“, vgl. auch potus „Trank“ ... lat. poti-o „das Trinken“'.\"\n            }\n          ]\n        },\n        {\n          \"id\": 10,\n          \"lang\": \"English\",\n          \"words\": \"potion, poison; beer, beverage\",\n          \"verdict\": \"plausible\",\n          \"derivation\": \"Three of the four are textbook: potion (ME pocioun, from Old French potion, from Lat. pōtiōnem 'a drink, draught') and poison (c. 1200 poisoun, from Old French poison/puison 'a drink, medical draught, magic potion', from the same Lat. pōtiōnem) are a doublet pair, the semantic narrowing 'drink' → 'deadly drink' happening inside Gallo-Romance (compare Fr. raison < rationem for the phonetic development); beverage (mid-13c., from Anglo-French beverage, Old French bevrage, from boivre < Lat. bibere) comes from the other Latin verb in the box above, which is why Nourai groups it with beer. beer is the doubtful one: Klein takes OE bēor 'strong drink' (with OHG bior, ON bjórr, Du. bier) straight from Ecclesiastical/Vulgar Latin biber 'drink, beverage' (< bibere), a 6th-century monastic borrowing — which is exactly Nourai's arrow — but an equally old alternative derives it from Proto-Germanic *beuwoz- from *beuwo- 'barley', and Etymonline calls the word 'of much-disputed and ambiguous origin'. Note also that the box's reference is AHD, and Watkins lists POISON, POTION, POTABLE and BEVERAGE under pō(i)- but NOT beer.\",\n          \"derivation_fa\": \"سه واژه از چهار واژه بی‌چون‌و‌چرا درست‌اند: potion از فرانسوی کهن potion و آن از لاتین pōtiōnem «نوشیدنی»؛ poison هم دوگانهٔ (doublet) همان واژه است که در فرانسوی کهن از «نوشیدنی دارویی» به «زهر» تحوّل معنایی یافته؛ beverage از فرانسوی کهن bevrage و از ریشهٔ لاتین bibere. امّا beer مورد اختلاف است: کلاین آن را وام‌واژه‌ای راهبانی از لاتین کلیسایی biber «نوشیدنی» می‌داند (همان ادعای نورایی)، ولی فرضیهٔ رقیب آن را از ژرمنی آغازین *beuwo- «جو» می‌گیرد؛ واتکینز نیز در همین ریشه، beer را نیاورده است. پس گره در مجموع با احتیاط پذیرفتنی است.\",\n          \"sources\": [\n            \"https://www.etymonline.com/word/beer\",\n            \"https://www.etymonline.com/word/poison\",\n            \"https://www.etymonline.com/word/beverage\"\n          ],\n          \"ref_check\": [\n            {\n              \"ref\": \"AHD\",\n              \"status\": \"partial\",\n              \"note\": \"Watkins 1985 s.v. pō(i)- lists 'POISON, POTABLE, POTATION, POTATORY, POTION' under *pō-to- (Latin pōtus) and 'BEVERAGE, BIB, BIBULOUS; IMBIBE' under the reduplicated *bi-bo- (Latin bibere) — three of Nourai's four words. BEER does not appear in the entry, and the index (AHD_watkins1985.txt line 1294) files 'BEVERAGE pO(i)-' but has no BEER at all under this root.\"\n            }\n          ],\n          \"consulted\": [\n            {\n              \"src\": \"KLN\",\n              \"where\": \"Klein, s.v. beer (KLN_1966.txt line 4652) and potion (line 29830)\",\n              \"stance\": \"supports\",\n              \"note\": \"'beer, n. — OE. bēor, rel. to OS., OHG. bior, ON. bjórr, OFris. biār ... fr. Eccles. L. biber (pl. biberes), ‘drink, beverage’, fr. L. bibere, ‘to drink’. See beverage.' and 'potion, n. ... fr. L. pōtiōnem ... fr. I.-E. base *pō(i)-, *pī-, ‘to drink’ ... Cp. poison, which is a doublet of potion.' Klein supports all four of Nourai's words, beer included.\"\n            },\n            {\n              \"src\": \"SKT\",\n              \"where\": \"Skeat, s.v. Potion / Potable (SKT.txt line 14647)\",\n              \"stance\": \"supports\",\n              \"note\": \"'... L. potio, a draught — L. ... drink; see Potable' (the OCR of this column is poor, but the Potion → L. potio → Potable chain is legible).\"\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}\n"
}
```


### [2026-09-14T01:14:06.703Z] TOOL RESULT

```
File created successfully at: /home/sfmqrb/git/rishe/data/verification/page-404.json (file state is current in your context — no need to Read it back)
```


## [2026-09-14T01:14:10.473Z] TOOL CALL #104: Bash

```json
{
 "command": "python3 -m json.tool data/verification/page-404.json > /dev/null && echo \"JSON OK\" && python3 tools/verify_check.py 404"
}
```


### [2026-09-14T01:14:12.686Z] TOOL RESULT

```
JSON OK
nodes verified: 13/13
node verdicts: {'confirmed': 6, 'disputed': 1, 'plausible': 5, 'transcription_suspect': 1}
root verdicts: {'confirmed': 2}
ref checks: {'supports': 8, 'partial': 3, 'not_checked': 3}
books consulted: {'supports': 21, 'partial': 6, 'silent': 8} | by book: {'WLD': 4, 'KLN': 4, 'SKT': 4, 'ARY': 3, 'IEC': 3, 'BRT': 2, 'SYN': 2, 'POK': 2, 'HRN': 2, 'BQT': 2, 'AHD': 2, 'MON': 2, 'PHD': 1, 'HUB': 1, 'LAT': 1}
```


## [2026-09-14T01:14:15.328Z] TOOL CALL #105: Bash

```json
{
 "command": "python3 tools/verify_archive_sources.py 404 2>&1 | tail -20"
}
```


### [2026-09-14T01:14:16.607Z] TOOL RESULT

```
10 cited URLs, 0 not yet archived
archived 0, failed 0
```


## [2026-09-14T01:14:34.510Z] AGENT

All 10 cited URLs are archived, and `verify_check.py 404` reports 0 PROBLEM lines.

**Page 404 (book p. 374) — 2 non-redirect entries, 13 nodes; 8 redirect entries skipped.**

Verdicts: roots 2 confirmed · nodes 6 confirmed, 5 plausible, 1 disputed, 1 transcription_suspect.
Ref checks: 8 supports, 3 partial, 3 not_checked (all VOP, which has no copy anywhere).

- **disputed** — *Pô 2*, node #1 Sanskrit **pâtila** "a large drinking vessel": no such word. The lexica have only *pātilī* (lexicographers' word), MW glossing it "a trap/snare; a **small earthen pot** (of mendicants)" and deriving it hesitantly from √*pat*, not √*pā* "drink". Nourai himself flags the link as uncertain. This also weakens the Persian پاتیل branch (node #2, marked plausible: Mo'in's "[سنس.]" tag and Hasandust's Hindi *patīlā* do support an Indic loan, but not a tie to the "drink" root).
- **transcription_suspect** — *Pô 2*, node #4 Greek **"pusis : drunk"**: `error_in: "book"`. Rendered p. 404 at 500 dpi and read the box — the printed page really does show *pusis*; the word is Gk. πόσις *pósis* "a drinking, a drink". Watkins (the reference Nourai cites) prints "posis, drink, drinking". Page PNG saved to `data/verification/sources/refs/ocr/BOOK/404.png`.

Other notes worth the owner's eye (not extraction errors): Av. *vispo-pitay* is glossed "drunk" but Bartholomae/Pokorny give "alltränkend" = "all-watering" (node marked plausible); English *beer* under this root follows Klein but Watkins omits it and Etymonline calls the origin "much-disputed" (node #10 plausible).

**Extraction issues for the owner (JSON vs printed page):**
- Entry 6, node #7: JSON script is `سمپوزیوم`, the page prints `سمپوزیم` (one و). The JSON form is the standard modern spelling (and Mo'in's), so it reads like a silent normalisation rather than a misread.
- Entry 6: an empty, unlabelled box hangs to the right of the Avestan node on the printed page. It has no language, word or reference; the extraction drops it, which is right — flagging only so it isn't mistaken for a lost node.

Strongest confirmations: WLD II p. 1 is literally the first entry of the volume, "(pais?): pis- zerstampfen, zermalmen" — Nourai's root quoted verbatim; and the Persian پست branch is corroborated five ways (Horn no. 320, Hübschmann p. 42 no. 320, Mo'in's footnote in Borhan giving Pahlavi *pēst* from the Kārnāmag, MacKenzie's `pist` "browned flour", Buck 5.55).
